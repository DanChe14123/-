import {
  cardsById,
  cardsByType,
  DIFFICULTIES,
  PHASE_LABELS,
  POST_KEYS,
  RISK_ORDER,
  SEVERITY_LABELS,
} from "./gameData.js";

const STAGES = ["prepare", "operate", "close", "emergency"];

function shuffle(items) {
  const deck = [...items];
  for (let index = deck.length - 1; index > 0; index -= 1) {
    const swap = Math.floor(Math.random() * (index + 1));
    [deck[index], deck[swap]] = [deck[swap], deck[index]];
  }
  return deck;
}

function makeDecks() {
  const taskDecks = Object.fromEntries(
    STAGES.map((stage) => [
      stage,
      shuffle((cardsByType.task ?? []).filter((card) => card.stage === stage)),
    ]),
  );
  const eventDecks = Object.fromEntries(
    STAGES.map((stage) => [
      stage,
      shuffle((cardsByType.event ?? []).filter((card) => card.phase === stage)),
    ]),
  );
  return {
    tasks: taskDecks,
    events: eventDecks,
    actions: shuffle(cardsByType.action ?? []),
    actionDiscard: [],
  };
}

function drawMany(deck, count) {
  return {
    drawn: deck.slice(0, count),
    rest: deck.slice(count),
  };
}

function drawActionCards(state, count) {
  let actions = [...state.decks.actions];
  let discard = [...state.decks.actionDiscard];
  const drawn = [];

  while (drawn.length < count && (actions.length > 0 || discard.length > 0)) {
    if (actions.length === 0) {
      actions = shuffle(discard);
      discard = [];
    }
    drawn.push(actions[0]);
    actions = actions.slice(1);
  }

  return {
    drawn,
    decks: {
      ...state.decks,
      actions,
      actionDiscard: discard,
    },
  };
}

function nextStage(progress, round, difficultyKey, stats) {
  if (difficultyKey === "challenge" && round === 4) return "emergency";
  if (stats.accident >= 2 || stats.hazard >= 3) return "emergency";
  if (progress < 2) return "prepare";
  if (progress < 4) return "operate";
  return "close";
}

function drawTaskForStage(state, stage) {
  let deck = state.decks.tasks[stage] ?? [];
  if (deck.length === 0) {
    deck = shuffle((cardsByType.task ?? []).filter((card) => card.stage === stage));
  }
  const [task, ...rest] = deck;
  return {
    task,
    decks: {
      ...state.decks,
      tasks: {
        ...state.decks.tasks,
        [stage]: rest,
      },
    },
  };
}

function drawEventForPhase(state, phase) {
  let deck = state.decks.events[phase] ?? [];
  if (deck.length === 0) {
    deck = shuffle((cardsByType.event ?? []).filter((card) => card.phase === phase));
  }
  const [event, ...rest] = deck;
  return {
    event,
    decks: {
      ...state.decks,
      events: {
        ...state.decks.events,
        [phase]: rest,
      },
    },
  };
}

function logEntry(type, text) {
  return {
    id: `${Date.now()}-${Math.random().toString(16).slice(2)}`,
    type,
    text,
    time: new Date().toLocaleTimeString("zh-CN", {
      hour: "2-digit",
      minute: "2-digit",
    }),
  };
}

function rotatePosts(round, playerCount) {
  const posts = cardsByType.post ?? [];
  return Array.from({ length: playerCount }, (_, index) => posts[(index + round - 1) % posts.length]);
}

function buildPlayers(playerCount) {
  const roles = shuffle(cardsByType.role ?? []);
  const posts = rotatePosts(1, playerCount);
  return Array.from({ length: playerCount }, (_, index) => ({
    id: `player-${index + 1}`,
    name: `玩家 ${index + 1}`,
    role: roles[index],
    post: posts[index],
    contribution: 0,
  }));
}

function clampNonNegative(value) {
  return Math.max(0, value);
}

function severityLoss(severity) {
  return { low: 1, medium: 2, high: 3 }[severity] ?? 1;
}

function increaseRisk(state) {
  const index = RISK_ORDER.indexOf(state);
  return RISK_ORDER[Math.min(RISK_ORDER.length - 1, Math.max(0, index) + 1)];
}

function endStatus(stats, difficulty, round) {
  if (
    stats.progress >= difficulty.targetProgress &&
    stats.safety > 0 &&
    stats.accident < 4 &&
    stats.hazard < 5
  ) {
    return "won";
  }
  if (stats.safety <= 0 || stats.accident >= 4 || stats.hazard >= 5) {
    return "lost";
  }
  if (round > difficulty.maxRounds && stats.progress < difficulty.targetProgress) {
    return "lost";
  }
  return null;
}

export function createInitialOptions() {
  return {
    difficultyKey: "standard",
    playerCount: 4,
    strategyId: "S01",
  };
}

export function startGame(options = createInitialOptions()) {
  const difficulty = DIFFICULTIES[options.difficultyKey] ?? DIFFICULTIES.standard;
  const decks = makeDecks();
  const shell = {
    started: true,
    status: "playing",
    difficultyKey: difficulty.key,
    playerCount: options.playerCount,
    strategy: cardsById[options.strategyId] ?? cardsByType.strategy?.[0],
    stats: {
      safety: difficulty.safety,
      progress: 0,
      accident: 0,
      hazard: difficulty.initialHazard ?? 0,
      round: 1,
      redraws: difficulty.redraws,
    },
    decks,
    players: buildPlayers(options.playerCount),
    activeLeadId: "player-1",
    hand: [],
    selectedActionIds: [],
    stage: "prepare",
    currentTask: null,
    currentEvent: null,
    riskState: null,
    result: null,
    knowledge: [],
    completedTaskStreak: 0,
    strategyFlags: {},
    logs: [
      logEntry("setup", `开局：${difficulty.label}，${options.playerCount} 人，策略「${cardsById[options.strategyId]?.name ?? "稳健管理"}」。`),
    ],
  };

  const handDraw = drawActionCards(shell, difficulty.handLimit);
  const taskDraw = drawTaskForStage({ ...shell, decks: handDraw.decks }, "prepare");
  return {
    ...shell,
    decks: taskDraw.decks,
    hand: handDraw.drawn,
    currentTask: taskDraw.task,
    logs: [
      ...shell.logs,
      logEntry("task", `当前任务：${taskDraw.task?.name ?? "未抽到任务"}。`),
    ],
  };
}

export function drawEvent(state) {
  if (!state.started || state.status !== "playing" || state.currentEvent) return state;
  const phase = state.currentTask?.phase ?? state.stage;
  const draw = drawEventForPhase(state, phase);
  return {
    ...state,
    decks: draw.decks,
    currentEvent: draw.event,
    riskState: draw.event?.initial_state ?? "hint",
    result: null,
    logs: [
      ...state.logs,
      logEntry(
        "event",
        `抽取事件：${draw.event?.name ?? "无事件"}（${SEVERITY_LABELS[draw.event?.severity] ?? "风险"}，初始${draw.event?.initial_state ? "" : ""}${draw.event?.initial_state ?? ""}）。`,
      ),
    ],
  };
}

export function toggleAction(state, actionId) {
  if (!state.currentEvent || state.result || state.status !== "playing") return state;
  const selected = new Set(state.selectedActionIds);
  if (selected.has(actionId)) {
    selected.delete(actionId);
  } else if (selected.size < 4) {
    selected.add(actionId);
  }
  return {
    ...state,
    selectedActionIds: [...selected],
  };
}

export function chooseLead(state, playerId) {
  return {
    ...state,
    activeLeadId: playerId,
  };
}

function selectedActionCards(state) {
  const selected = new Set(state.selectedActionIds);
  return state.hand.filter((card) => selected.has(card.id));
}

function applyStrategyBeforeDamage(state, safetyLoss, accidentGain) {
  let nextLoss = safetyLoss;
  let nextAccident = accidentGain;
  const flags = { ...state.strategyFlags };
  const strategyId = state.strategy?.id;

  if (strategyId === "S01" && nextLoss > 0 && !flags.s01SafetyUsed) {
    nextLoss = Math.max(0, nextLoss - 1);
    flags.s01SafetyUsed = true;
  }
  if (strategyId === "S08" && nextAccident > 0 && state.riskState === "critical" && !flags.s08CriticalUsed) {
    nextAccident = Math.max(0, nextAccident - 1);
    flags.s08CriticalUsed = true;
  }

  return { safetyLoss: nextLoss, accidentGain: nextAccident, strategyFlags: flags };
}

function applyPostReward(players, leadId, leadPostKey, outcome, actionTags, progressGain, worsened) {
  let drawBonus = 0;
  const nextPlayers = players.map((player) => {
    if (player.id !== leadId) return player;
    let contribution = player.contribution;
    if (outcome === "complete") contribution += 2;
    if (outcome === "control") contribution += 1;
    if (outcome === "wrong") contribution -= 1;

    if (
      leadPostKey === "safety_officer" &&
      ["isolate", "evacuate", "emergency", "report"].some((tag) => actionTags.has(tag)) &&
      ["complete", "control"].includes(outcome)
    ) {
      contribution += 1;
    }
    if (leadPostKey === "operator" && progressGain > 0) {
      contribution += worsened ? 1 : 2;
    }
    if (
      leadPostKey === "recorder" &&
      ["record", "verify", "review", "inspect"].some((tag) => actionTags.has(tag))
    ) {
      contribution += 1;
      drawBonus = 1;
    }
    if (leadPostKey === "resource_manager" && !worsened) {
      contribution += 1;
    }
    return {
      ...player,
      contribution,
    };
  });
  return { players: nextPlayers, drawBonus };
}

export function resolveActions(state) {
  if (!state.currentEvent || state.selectedActionIds.length === 0 || state.result || state.status !== "playing") {
    return state;
  }

  const difficulty = DIFFICULTIES[state.difficultyKey];
  const actions = selectedActionCards(state);
  const actionTags = new Set(actions.flatMap((card) => card.action_tags ?? card.tags ?? []));
  const event = state.currentEvent;
  const task = state.currentTask;
  const lead = state.players.find((player) => player.id === state.activeLeadId) ?? state.players[0];
  const leadPostKey = POST_KEYS[lead?.post?.id] ?? "operator";
  const hasConflict = (event.conflict_actions ?? []).some((tag) => actionTags.has(tag));
  const keyHits = (event.key_actions ?? []).filter((tag) => actionTags.has(tag));
  let supportHits = (event.support_actions ?? []).filter((tag) => actionTags.has(tag));
  const taskMatches = (task?.preferred_actions ?? []).filter((tag) => actionTags.has(tag));
  const postMatch = actions.some((card) => (card.post_bonus ?? []).includes(leadPostKey));

  if (
    state.strategy?.id === "S06" &&
    (event.tags ?? []).includes("equipment") &&
    ["inspect", "secure"].some((tag) => actionTags.has(tag)) &&
    supportHits.length === 0
  ) {
    supportHits = ["strategy_equipment_support"];
  }

  let outcome = "wrong";
  if (hasConflict || keyHits.length === 0) {
    outcome = supportHits.length > 0 && !hasConflict ? "weak" : "wrong";
  } else if (supportHits.length > 0 || postMatch) {
    outcome = "complete";
  } else {
    outcome = "control";
  }

  let stats = { ...state.stats };
  let riskState = state.riskState;
  let progressGain = 0;
  let drawBonus = 0;
  let cleared = false;
  let worsened = false;
  let resultText = "";
  let resultTitle = "";
  let strategyFlags = { ...state.strategyFlags };

  if (outcome === "complete") {
    cleared = true;
    riskState = null;
    progressGain = 1;
    resultTitle = "完整处置";
    resultText = "命中关键行动，并获得辅助行动或岗位支持，风险清除，实验进度推进。";

    if (taskMatches.length > 0) {
      if (task?.reward === "progress_boost") progressGain += 1;
      if (task?.reward === "draw") drawBonus += 1;
      if (task?.reward === "clear_hazard") stats.hazard = clampNonNegative(stats.hazard - 1);
      if (task?.reward === "recover_safety") stats.safety += 1;
      if (task?.reward === "reduce_accident") stats.accident = clampNonNegative(stats.accident - 1);
    }

    if (state.strategy?.id === "S03") {
      stats.hazard = clampNonNegative(stats.hazard - 1);
    }

    if (state.strategy?.id === "S02") {
      const streak = state.completedTaskStreak + 1;
      if (streak >= 2 && !state.strategyFlags.s02BoostUsed) {
        progressGain += 1;
        stats.safety -= 2;
        strategyFlags.s02BoostUsed = true;
      }
    }
  } else if (outcome === "control") {
    resultTitle = "控制风险";
    resultText = "命中关键行动，但缺少辅助行动或岗位支撑。低危风险可清除，中高危风险留下隐患。";
    if (event.severity === "low") {
      cleared = true;
      riskState = null;
    } else {
      stats.hazard += 1;
    }
  } else if (outcome === "weak") {
    worsened = true;
    riskState = increaseRisk(riskState);
    const loss = severityLoss(event.severity);
    stats.hazard += 1;
    stats.safety -= loss;
    resultTitle = "勉强维持";
    resultText = `缺少关键行动，风险升级为「${riskState}」，隐患增加，安全值下降 ${loss}。`;
  } else {
    worsened = true;
    riskState = increaseRisk(riskState);
    const rawLoss = severityLoss(event.severity);
    const rawAccident = state.riskState === "critical" || event.severity === "high" ? 2 : 1;
    const adjusted = applyStrategyBeforeDamage(state, rawLoss, rawAccident);
    strategyFlags = { ...strategyFlags, ...adjusted.strategyFlags };
    stats.safety -= adjusted.safetyLoss;
    if (!(state.difficultyKey === "teaching" && !state.strategyFlags.firstTeachingMistake)) {
      stats.accident += adjusted.accidentGain;
    }
    strategyFlags.firstTeachingMistake = true;
    resultTitle = "处置错误";
    resultText = `未命中关键行动或打出冲突行动。安全值下降 ${adjusted.safetyLoss}，事故等级增加 ${adjusted.accidentGain}。`;
  }

  stats.progress += progressGain;
  const postReward = applyPostReward(
    state.players,
    lead.id,
    leadPostKey,
    outcome,
    actionTags,
    progressGain,
    worsened,
  );
  drawBonus += postReward.drawBonus;

  const selectedIds = new Set(state.selectedActionIds);
  const remainingHand = state.hand.filter((card) => !selectedIds.has(card.id));
  let nextState = {
    ...state,
    stats,
    riskState,
    players: postReward.players,
    hand: remainingHand,
    selectedActionIds: [],
    completedTaskStreak: outcome === "complete" ? state.completedTaskStreak + 1 : 0,
    strategyFlags,
    decks: {
      ...state.decks,
      actionDiscard: [...state.decks.actionDiscard, ...actions],
    },
    result: {
      outcome,
      title: resultTitle,
      text: resultText,
      cleared,
      worsened,
      keyHits,
      supportHits,
      taskMatches,
      postMatch,
      progressGain,
      actions,
    },
  };

  if (drawBonus > 0) {
    const draw = drawActionCards(nextState, drawBonus);
    nextState = {
      ...nextState,
      decks: draw.decks,
      hand: [...nextState.hand, ...draw.drawn],
    };
  }

  const status = endStatus(nextState.stats, difficulty, nextState.stats.round);
  nextState = {
    ...nextState,
    status: status ?? "playing",
    logs: [
      ...state.logs,
      logEntry("resolve", `${lead.name} 主导「${resultTitle}」：${resultText}`),
      ...(status ? [logEntry(status, status === "won" ? "团队达成实验目标，安全通关。" : "团队触发失败条件，游戏结束。")] : []),
    ],
  };

  return nextState;
}

export function debrief(state) {
  if (!state.currentEvent || !state.result || state.knowledge.some((item) => item.eventId === state.currentEvent.id)) {
    return state;
  }
  let nextState = {
    ...state,
    knowledge: [
      ...state.knowledge,
      {
        eventId: state.currentEvent.id,
        debrief: cardsById[state.currentEvent.debrief_id],
      },
    ],
    logs: [
      ...state.logs,
      logEntry("debrief", `复盘知识点：${cardsById[state.currentEvent.debrief_id]?.name ?? state.currentEvent.knowledge}。`),
    ],
  };

  if (nextState.strategy?.id === "S07" && nextState.knowledge.length % 3 === 0) {
    const draw = drawActionCards(nextState, 1);
    nextState = {
      ...nextState,
      decks: draw.decks,
      hand: [...nextState.hand, ...draw.drawn],
      logs: [...nextState.logs, logEntry("strategy", "策略「复盘驱动」触发：团队抽 1 张行动牌。")],
    };
  }

  return nextState;
}

export function redrawSelected(state) {
  if (state.selectedActionIds.length === 0 || state.stats.redraws <= 0 || state.result) return state;
  const selectedIds = new Set(state.selectedActionIds);
  const discarded = state.hand.filter((card) => selectedIds.has(card.id));
  const remaining = state.hand.filter((card) => !selectedIds.has(card.id));
  let nextState = {
    ...state,
    hand: remaining,
    selectedActionIds: [],
    stats: {
      ...state.stats,
      redraws: state.stats.redraws - 1,
    },
    decks: {
      ...state.decks,
      actionDiscard: [...state.decks.actionDiscard, ...discarded],
    },
  };
  const draw = drawActionCards(nextState, discarded.length);
  return {
    ...nextState,
    decks: draw.decks,
    hand: [...nextState.hand, ...draw.drawn],
    logs: [...state.logs, logEntry("redraw", `换牌 ${discarded.length} 张，剩余换牌 ${nextState.stats.redraws} 次。`)],
  };
}

export function nextRound(state) {
  if (state.status !== "playing") return state;
  const difficulty = DIFFICULTIES[state.difficultyKey];
  let stats = { ...state.stats };
  let logs = [...state.logs];
  const flags = { ...state.strategyFlags };

  if (state.currentEvent && state.riskState) {
    if (state.riskState === "exposed") {
      if (!(state.strategy?.id === "S04" && !flags.s04HandoffUsed)) {
        stats.hazard += 1;
        logs.push(logEntry("handoff", "交接链触发：暴露风险遗留，隐患 +1。"));
      } else {
        flags.s04HandoffUsed = true;
        logs.push(logEntry("strategy", "策略「风险隔离」抵消首次交接隐患。"));
      }
    }
    if (state.riskState === "critical") {
      stats.safety -= 1;
      logs.push(logEntry("handoff", "交接链触发：失控风险遗留，安全值 -1。"));
    }
  }

  const round = stats.round + 1;
  const stage = nextStage(stats.progress, round, state.difficultyKey, stats);
  const withRound = {
    ...state,
    stats: {
      ...stats,
      round,
    },
    stage,
    strategyFlags: flags,
    logs,
  };
  const handLimit = difficulty.handLimit + (withRound.players.some((player) => POST_KEYS[player.post?.id] === "resource_manager") ? 1 : 0);
  const draw = drawActionCards(withRound, Math.max(0, handLimit - state.hand.length));
  const taskDraw = drawTaskForStage({ ...withRound, decks: draw.decks }, stage);
  const posts = rotatePosts(round, state.playerCount);
  const players = withRound.players.map((player, index) => ({
    ...player,
    post: posts[index],
  }));
  const status = endStatus(stats, difficulty, round);

  return {
    ...withRound,
    status: status ?? "playing",
    stats: {
      ...stats,
      round,
    },
    decks: taskDraw.decks,
    players,
    activeLeadId: players[0]?.id,
    hand: [...state.hand, ...draw.drawn],
    currentTask: taskDraw.task,
    currentEvent: null,
    riskState: null,
    result: null,
    selectedActionIds: [],
    logs: [
      ...logs,
      logEntry("round", `进入第 ${round} 轮：${PHASE_LABELS[stage]}阶段，任务「${taskDraw.task?.name ?? "未抽到任务"}」。`),
      ...(status ? [logEntry("lost", "回合上限已到且进度不足，游戏结束。")] : []),
    ],
  };
}
