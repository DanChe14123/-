"use client";

import React, { useMemo, useState } from "react";
import {
  AlertTriangle,
  ArrowRight,
  BookOpen,
  CheckCircle2,
  ClipboardList,
  FlaskConical,
  RefreshCw,
  RotateCcw,
  ShieldCheck,
  Sparkles,
  UsersRound,
} from "lucide-react";
import {
  cardImagePath,
  cardsById,
  cardsByType,
  DIFFICULTIES,
  formatTag,
  PHASE_LABELS,
  POST_ACCENTS,
  RISK_LABELS,
  RISK_ORDER,
  SEVERITY_LABELS,
  TYPE_LABELS,
} from "./gameData.js";
import {
  chooseLead,
  createInitialOptions,
  debrief,
  drawEvent,
  nextRound,
  redrawSelected,
  resolveActions,
  startGame,
  toggleAction,
} from "./gameLogic.js";

function StatTile({ icon, label, value, max, tone }) {
  const pct = max ? Math.max(0, Math.min(100, (value / max) * 100)) : 0;
  return (
    <div className={`stat-tile ${tone ?? ""}`}>
      <div className="stat-icon">{icon}</div>
      <div>
        <span>{label}</span>
        <strong>
          {value}
          {max ? <em> / {max}</em> : null}
        </strong>
      </div>
      {max ? <div className="meter"><i style={{ width: `${pct}%` }} /></div> : null}
    </div>
  );
}

function SetupScreen({ onStart }) {
  const [options, setOptions] = useState(createInitialOptions());
  const strategy = cardsById[options.strategyId];

  return (
    <main className="setup-screen">
      <section className="setup-shell">
        <div className="setup-copy">
          <div className="brand-mark">
            <FlaskConical size={34} />
            <span>实验室安全值班</span>
          </div>
          <h1>在线协作桌面</h1>
          <p>按 v2.0 卡牌数据驱动的浏览器原型。选择模式与人数后，可直接完成抽事件、选择行动、结算风险、复盘知识点和下一轮推进。</p>
        </div>

        <div className="setup-panel">
          <label>
            难度模式
            <select
              value={options.difficultyKey}
              onChange={(event) => setOptions({ ...options, difficultyKey: event.target.value })}
            >
              {Object.values(DIFFICULTIES).map((difficulty) => (
                <option key={difficulty.key} value={difficulty.key}>
                  {difficulty.label}
                </option>
              ))}
            </select>
          </label>
          <p className="field-hint">{DIFFICULTIES[options.difficultyKey].summary}</p>

          <label>
            玩家人数
            <div className="segmented">
              {[2, 3, 4].map((count) => (
                <button
                  type="button"
                  key={count}
                  className={options.playerCount === count ? "selected" : ""}
                  onClick={() => setOptions({ ...options, playerCount: count })}
                >
                  {count} 人
                </button>
              ))}
            </div>
          </label>

          <label>
            本局策略
            <select
              value={options.strategyId}
              onChange={(event) => setOptions({ ...options, strategyId: event.target.value })}
            >
              {(cardsByType.strategy ?? []).map((card) => (
                <option key={card.id} value={card.id}>
                  {card.id} {card.name}
                </option>
              ))}
            </select>
          </label>

          <article className="strategy-preview">
            <img src={cardImagePath(strategy)} alt={strategy?.name} />
            <div>
              <strong>{strategy?.name}</strong>
              <span>{strategy?.summary}</span>
              <small>{strategy?.effect}</small>
            </div>
          </article>

          <button
            type="button"
            className="primary large"
            data-testid="start-game"
            onClick={() => onStart(options)}
          >
            <Sparkles size={18} />
            开始新局
          </button>
        </div>
      </section>
    </main>
  );
}

function PlayerPanel({ game, onChooseLead }) {
  return (
    <aside className="left-rail">
      <div className="rail-title">
        <UsersRound size={18} />
        岗位与玩家
      </div>
      {game.players.map((player) => {
        const active = player.id === game.activeLeadId;
        const accent = POST_ACCENTS[player.post?.id] ?? "teal";
        return (
          <button
            type="button"
            className={`player-card ${active ? "active" : ""} ${accent}`}
            key={player.id}
            onClick={() => onChooseLead(player.id)}
          >
            <div className="player-head">
              <strong>{player.post?.name}</strong>
              <span>{active ? "主导" : "可选"}</span>
            </div>
            <p>{player.post?.summary}</p>
            <div className="player-meta">
              <span>{player.name}</span>
              <span>{player.role?.name}</span>
            </div>
            <div className="contribution">
              <span>贡献</span>
              <b>{player.contribution}</b>
            </div>
          </button>
        );
      })}
    </aside>
  );
}

function RouteBoard({ game }) {
  const stages = ["prepare", "operate", "close", "emergency"];
  return (
    <section className="route-board">
      {stages.map((stage, index) => (
        <div key={stage} className={`route-step ${game.stage === stage ? "current" : ""}`}>
          <span>{index + 1}</span>
          <strong>{PHASE_LABELS[stage]}</strong>
        </div>
      ))}
    </section>
  );
}

function GameCard({ card, title, side = "front", compact = false }) {
  if (!card) {
    return (
      <article className={`game-card empty ${compact ? "compact" : ""}`}>
        <div className="card-placeholder">等待抽牌</div>
      </article>
    );
  }
  return (
    <article className={`game-card ${card.card_type} ${compact ? "compact" : ""}`}>
      <div className="card-label">
        <span>{title ?? TYPE_LABELS[card.card_type]}</span>
        <b>{card.id}</b>
      </div>
      <img src={cardImagePath(card, side)} alt={`${card.id} ${card.name}`} />
      <div className="card-copy">
        <strong>{card.name}</strong>
        <p>{card.summary}</p>
      </div>
    </article>
  );
}

function RiskPanel({ game }) {
  const event = game.currentEvent;
  return (
    <section className="risk-panel">
      <div className="section-title">
        <AlertTriangle size={18} />
        风险状态
      </div>
      <div className="risk-track">
        {RISK_ORDER.map((risk) => (
          <div
            key={risk}
            className={`risk-step ${game.riskState === risk ? "active" : ""} ${risk}`}
          >
            <span>{RISK_LABELS[risk]}</span>
            <small>{risk === "hint" ? "可识别" : risk === "exposed" ? "需行动" : "事故边缘"}</small>
          </div>
        ))}
      </div>
      {event ? (
        <div className="risk-detail">
          <span>{SEVERITY_LABELS[event.severity]}</span>
          <strong>{event.name}</strong>
          <p>关键行动：{(event.key_actions ?? []).map(formatTag).join("、")}</p>
          <p>辅助行动：{(event.support_actions ?? []).map(formatTag).join("、")}</p>
          <p>冲突行动：{(event.conflict_actions ?? []).map(formatTag).join("、")}</p>
        </div>
      ) : (
        <div className="risk-detail muted">抽取事件后显示风险等级、关键行动和冲突行动。</div>
      )}
    </section>
  );
}

function ResultBanner({ game }) {
  if (game.status === "won") {
    return (
      <div className="result-banner success">
        <CheckCircle2 size={20} />
        <div>
          <strong>团队胜利</strong>
          <span>实验进度达标，安全值、事故等级和隐患仍在阈值内。</span>
        </div>
      </div>
    );
  }
  if (game.status === "lost") {
    return (
      <div className="result-banner danger">
        <AlertTriangle size={20} />
        <div>
          <strong>团队失败</strong>
          <span>触发安全值、事故等级、隐患或回合上限失败条件。</span>
        </div>
      </div>
    );
  }
  if (!game.result) return null;
  return (
    <div className={`result-banner ${game.result.outcome}`}>
      {game.result.outcome === "complete" ? <CheckCircle2 size={20} /> : <AlertTriangle size={20} />}
      <div>
        <strong>{game.result.title}</strong>
        <span>{game.result.text}</span>
      </div>
    </div>
  );
}

function ActionHand({ game, onToggle, onRedraw }) {
  const selected = new Set(game.selectedActionIds);
  return (
    <section className="action-hand">
      <div className="hand-title">
        <div>
          <strong>公共行动区</strong>
          <span>最多选择 4 张行动牌进行结算</span>
        </div>
        <button
          type="button"
          className="ghost"
          disabled={selected.size === 0 || game.stats.redraws <= 0 || Boolean(game.result)}
          onClick={onRedraw}
        >
          <RefreshCw size={16} />
          换牌 {game.stats.redraws}
        </button>
      </div>
      <div className="hand-scroll">
        {game.hand.map((card) => (
        <button
          type="button"
          className={`action-card ${selected.has(card.id) ? "selected" : ""}`}
          data-testid={`action-card-${card.id}`}
          key={card.id}
          onClick={() => onToggle(card.id)}
            disabled={!game.currentEvent || Boolean(game.result) || game.status !== "playing"}
          >
            <img src={cardImagePath(card)} alt={`${card.id} ${card.name}`} />
            <span>{card.name}</span>
          </button>
        ))}
      </div>
    </section>
  );
}

function SidePanel({ game }) {
  const activeDebrief = game.currentEvent ? cardsById[game.currentEvent.debrief_id] : null;
  return (
    <aside className="right-rail">
      <section className="log-panel">
        <div className="section-title">
          <ClipboardList size={18} />
          回合记录
        </div>
        <div className="log-list">
          {game.logs.slice(-8).reverse().map((entry) => (
            <div key={entry.id} className={`log-entry ${entry.type}`}>
              <span>{entry.time}</span>
              <p>{entry.text}</p>
            </div>
          ))}
        </div>
      </section>
      <section className="knowledge-panel">
        <div className="section-title">
          <BookOpen size={18} />
          复盘与知识库
        </div>
        {activeDebrief ? (
          <div className="debrief-card">
            <strong>{activeDebrief.name}</strong>
            <p>{activeDebrief.why}</p>
            <small>{activeDebrief.review_question}</small>
          </div>
        ) : (
          <div className="debrief-card muted">完成结算后可记录本轮复盘知识点。</div>
        )}
        <div className="knowledge-count">
          <span>已复盘</span>
          <b>{game.knowledge.length}</b>
        </div>
      </section>
    </aside>
  );
}

function TopBar({ game, onRestart, onDraw, onResolve, onDebrief, onNextRound }) {
  const difficulty = DIFFICULTIES[game.difficultyKey];
  return (
    <header className="top-bar">
      <div className="app-title">
        <FlaskConical size={28} />
        <div>
          <strong>实验室安全值班</strong>
          <span>{difficulty.label}</span>
        </div>
      </div>
      <div className="stats-strip">
        <StatTile icon={<ShieldCheck size={17} />} label="安全值" value={game.stats.safety} max={difficulty.safety} tone="safe" />
        <StatTile icon={<AlertTriangle size={17} />} label="事故" value={game.stats.accident} max={4} tone="danger" />
        <StatTile icon={<AlertTriangle size={17} />} label="隐患" value={game.stats.hazard} max={5} tone="warn" />
        <StatTile icon={<ArrowRight size={17} />} label="进度" value={game.stats.progress} max={difficulty.targetProgress} tone="progress" />
        <StatTile icon={<ClipboardList size={17} />} label="轮次" value={game.stats.round} max={difficulty.maxRounds} />
      </div>
      <div className="top-actions">
        <button type="button" className="ghost" data-testid="restart-game" onClick={onRestart}>
          <RotateCcw size={16} />
          新局
        </button>
        <button
          type="button"
          className="secondary"
          data-testid="draw-event"
          onClick={onDraw}
          disabled={Boolean(game.currentEvent) || game.status !== "playing"}
        >
          抽事件
        </button>
        <button
          type="button"
          className="primary"
          data-testid="resolve-actions"
          onClick={onResolve}
          disabled={!game.currentEvent || game.selectedActionIds.length === 0 || Boolean(game.result) || game.status !== "playing"}
        >
          结算行动
        </button>
        <button
          type="button"
          className="secondary"
          data-testid="debrief"
          onClick={onDebrief}
          disabled={!game.result || !game.currentEvent}
        >
          复盘
        </button>
        <button
          type="button"
          className="primary dark"
          data-testid="next-round"
          onClick={onNextRound}
          disabled={!game.result || game.status !== "playing"}
        >
          下一轮
        </button>
      </div>
    </header>
  );
}

function GameTable({ game, setGame }) {
  const activeLead = useMemo(
    () => game.players.find((player) => player.id === game.activeLeadId),
    [game.players, game.activeLeadId],
  );

  return (
    <main className="game-screen">
      <TopBar
        game={game}
        onRestart={() => setGame(startGame({ difficultyKey: game.difficultyKey, playerCount: game.playerCount, strategyId: game.strategy.id }))}
        onDraw={() => setGame((state) => drawEvent(state))}
        onResolve={() => setGame((state) => resolveActions(state))}
        onDebrief={() => setGame((state) => debrief(state))}
        onNextRound={() => setGame((state) => nextRound(state))}
      />

      <div className="table-layout">
        <PlayerPanel game={game} onChooseLead={(id) => setGame((state) => chooseLead(state, id))} />

        <section className="center-table">
          <RouteBoard game={game} />
          <div className="main-grid">
            <GameCard card={game.currentTask} title="当前任务" />
            <GameCard card={game.currentEvent} title="当前事件" />
            <RiskPanel game={game} />
          </div>
          <ResultBanner game={game} />
          <div className="lead-strip">
            <span>本轮主导岗位</span>
            <strong>{activeLead?.post?.name} · {activeLead?.name}</strong>
            <small>{activeLead?.post?.responsibility}</small>
          </div>
          <ActionHand
            game={game}
            onToggle={(id) => setGame((state) => toggleAction(state, id))}
            onRedraw={() => setGame((state) => redrawSelected(state))}
          />
        </section>

        <SidePanel game={game} />
      </div>
    </main>
  );
}

export default function App() {
  const [game, setGame] = useState(null);

  if (!game) {
    return <SetupScreen onStart={(options) => setGame(startGame(options))} />;
  }

  return <GameTable game={game} setGame={setGame} />;
}
