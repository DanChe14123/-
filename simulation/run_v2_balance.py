from __future__ import annotations

import argparse
import csv
import json
import random
from collections import Counter, defaultdict
from dataclasses import dataclass, field
from pathlib import Path
from statistics import mean
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
CARDS_PATH = ROOT / "content" / "v2_cards.json"
OUTPUT_ROOT = ROOT / "data" / "v2"

STATES = {"hint": 0, "exposed": 1, "critical": 2}
STATE_NAMES = {0: "hint", 1: "exposed", 2: "critical"}
SEVERITY_DAMAGE = {"low": 1, "medium": 2, "high": 3}
NEW_ACTION_GROUPS = {"emergency", "evacuate", "shutdown", "secure", "isolate", "contain"}


@dataclass(frozen=True)
class ModeConfig:
    safety: int
    target_progress: int
    max_turns: int
    hand_size: int
    redraws: int
    initial_hazards: int = 0
    first_error_grace: bool = False
    extra_event_turn: int | None = None


MODES = {
    "teaching": ModeConfig(safety=12, target_progress=5, max_turns=8, hand_size=8, redraws=4, first_error_grace=True),
    "standard": ModeConfig(safety=10, target_progress=5, max_turns=8, hand_size=7, redraws=2),
    "challenge": ModeConfig(safety=10, target_progress=6, max_turns=8, hand_size=6, redraws=2, initial_hazards=1, extra_event_turn=4),
}


@dataclass
class Player:
    role_id: str
    post_id: str = ""
    contribution: int = 0
    ability_uses: int = 0


@dataclass
class GameState:
    mode: str
    safety: int
    progress: int = 0
    accident: int = 0
    hazards: int = 0
    turn: int = 0
    redraws_used: int = 0
    first_error_used: bool = False
    pending_state: int = -1
    pending_event_id: str = ""
    completed_tasks: int = 0
    knowledge_points: set[str] = field(default_factory=set)
    strategy_flags: set[str] = field(default_factory=set)


def load_cards() -> dict[str, list[dict[str, Any]]]:
    data = json.loads(CARDS_PATH.read_text(encoding="utf-8"))
    grouped: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for card in data["cards"]:
        grouped[card["card_type"]].append(card)
    return grouped


def draw(deck: list[dict[str, Any]], discard: list[dict[str, Any]]) -> dict[str, Any]:
    if not deck:
        deck.extend(discard)
        discard.clear()
        random.shuffle(deck)
    return deck.pop()


def refill_hand(hand: list[dict[str, Any]], deck: list[dict[str, Any]], discard: list[dict[str, Any]], size: int) -> None:
    while len(hand) < size:
        hand.append(draw(deck, discard))


def choose_task(tasks: list[dict[str, Any]], stage_order: list[str], turn: int) -> dict[str, Any]:
    stage = stage_order[min(turn - 1, len(stage_order) - 1)]
    candidates = [task for task in tasks if task["stage"] == stage]
    return random.choice(candidates or tasks)


def choose_event(events: list[dict[str, Any]], task: dict[str, Any]) -> dict[str, Any]:
    task_risks = set(task.get("risk_tags", []))
    candidates = [event for event in events if set(event.get("risk_tags", [])) & task_risks]
    if not candidates:
        candidates = [event for event in events if event.get("phase") == task.get("stage")]
    return random.choice(candidates or events)


def action_score(action: dict[str, Any], event: dict[str, Any], task: dict[str, Any], post_id: str) -> float:
    tags = set(action.get("action_tags", []))
    key = set(event.get("key_actions", []))
    support = set(event.get("support_actions", []))
    conflict = set(event.get("conflict_actions", []))
    preferred = set(task.get("preferred_actions", []))
    score = 0.0
    if tags & conflict:
        score -= 5.0
    if tags & key:
        score += 8.0
    if tags & support:
        score += 3.0
    if tags & preferred:
        score += 2.0
    if post_id in action.get("post_bonus", []):
        score += 1.5
    if action.get("strength") == "emergency" and event.get("severity") == "high":
        score += 1.0
    if action.get("strength") == "basic" and event.get("initial_state") == "critical":
        score -= 0.75
    return score


def choose_actions(
    hand: list[dict[str, Any]],
    event: dict[str, Any],
    task: dict[str, Any],
    post_id: str,
    max_actions: int = 2,
) -> list[dict[str, Any]]:
    ranked = sorted(hand, key=lambda card: action_score(card, event, task, post_id), reverse=True)
    chosen = [card for card in ranked[:max_actions] if action_score(card, event, task, post_id) > 0]
    if not chosen:
        chosen = ranked[:1]
    return chosen


def stage_post_bonus(task: dict[str, Any], post_id: str) -> float:
    stage = task.get("stage")
    if stage == "prepare" and post_id in {"recorder", "resource_manager"}:
        return 1.25
    if stage == "operate" and post_id == "operator":
        return 1.25
    if stage == "close" and post_id in {"recorder", "resource_manager"}:
        return 1.25
    if stage == "emergency" and post_id == "safety_officer":
        return 1.5
    return 0.0


def choose_action_plan(
    hand: list[dict[str, Any]],
    event: dict[str, Any],
    task: dict[str, Any],
    players: list[Player],
) -> tuple[Player, list[dict[str, Any]]]:
    best_player = players[0]
    best_actions = choose_actions(hand, event, task, best_player.post_id)
    best_score = -999.0
    for player in players:
        actions = choose_actions(hand, event, task, player.post_id)
        score = sum(action_score(action, event, task, player.post_id) for action in actions)
        score += stage_post_bonus(task, player.post_id)
        if score > best_score:
            best_score = score
            best_player = player
            best_actions = actions
    return best_player, best_actions


def maybe_redraw(
    state: GameState,
    hand: list[dict[str, Any]],
    deck: list[dict[str, Any]],
    discard: list[dict[str, Any]],
    event: dict[str, Any],
    config: ModeConfig,
) -> None:
    if state.redraws_used >= config.redraws or len(hand) < 2:
        return
    hand_tags = set().union(*(set(card.get("action_tags", [])) for card in hand))
    if hand_tags & set(event.get("key_actions", [])):
        return
    worst = sorted(hand, key=lambda card: len(set(card.get("action_tags", [])) & set(event.get("support_actions", []))))[:2]
    for card in worst:
        hand.remove(card)
        discard.append(card)
    refill_hand(hand, deck, discard, config.hand_size)
    state.redraws_used += 1


def apply_strategy_setup(strategy: dict[str, Any] | None, state: GameState) -> None:
    if not strategy:
        return
    if strategy["id"] == "S08":
        state.accident = max(0, state.accident - 1)


def evaluate_actions(
    selected: list[dict[str, Any]],
    event: dict[str, Any],
    task: dict[str, Any],
    post_id: str,
) -> str:
    tags = set().union(*(set(action.get("action_tags", [])) for action in selected))
    key = set(event.get("key_actions", []))
    support = set(event.get("support_actions", []))
    conflict = set(event.get("conflict_actions", []))
    post_match = any(post_id in action.get("post_bonus", []) for action in selected)
    if tags & conflict:
        return "wrong"
    if tags & key and ((tags & support) or post_match):
        return "complete"
    if tags & key:
        return "control"
    if tags & support:
        return "maintain"
    return "wrong"


def resolve_turn(
    state: GameState,
    players: list[Player],
    active: Player,
    task: dict[str, Any],
    event: dict[str, Any],
    selected: list[dict[str, Any]],
    strategy: dict[str, Any] | None,
    config: ModeConfig,
) -> dict[str, Any]:
    support_players = [player for player in players if player is not active]
    result = evaluate_actions(selected, event, task, active.post_id)
    severity = event["severity"]
    state_level = max(STATES[event["initial_state"]], state.pending_state)
    task_tags = set(task.get("preferred_actions", []))
    action_tags = set().union(*(set(action.get("action_tags", [])) for action in selected))
    task_match = bool(action_tags & task_tags)
    knowledge = event.get("knowledge", "")
    if knowledge:
        state.knowledge_points.add(knowledge)

    safety_delta = 0
    hazard_delta = 0
    accident_delta = 0
    progress_delta = 0
    next_pending_state = -1

    if result == "complete":
        progress_delta = task.get("progress", 1)
        state.completed_tasks += 1
        if task_match and active.post_id == "operator" and random.random() < 0.2:
            progress_delta += 1
        if state.hazards > 0:
            hazard_delta -= 1
        active.contribution += 2 if active.post_id in {"safety_officer", "operator"} else 1
        for helper in support_players:
            if helper.post_id in {"recorder", "resource_manager"}:
                helper.contribution += 1
    elif result == "control":
        if severity == "low" and task_match:
            progress_delta = 1
        else:
            hazard_delta += 1 if severity != "low" else 0
        active.contribution += 1
        for helper in support_players:
            if helper.post_id == "recorder" and "record" in action_tags:
                helper.contribution += 1
    elif result == "maintain":
        safety_delta -= max(1, SEVERITY_DAMAGE[severity] - 1)
        hazard_delta += 1
        next_pending_state = min(2, state_level + 1)
    else:
        damage = SEVERITY_DAMAGE[severity] + (1 if state_level == 2 else 0)
        if config.first_error_grace and not state.first_error_used:
            accident_delta = 0
            state.first_error_used = True
        else:
            accident_delta += 2 if state_level == 2 else 1
        safety_delta -= damage
        hazard_delta += 1
        next_pending_state = min(2, state_level + 1)
        active.contribution -= 1

    if strategy:
        sid = strategy["id"]
        if sid == "S01" and safety_delta < 0 and "S01_buffer_used" not in state.strategy_flags:
            safety_delta += 1
            state.strategy_flags.add("S01_buffer_used")
        elif sid == "S02":
            if event["severity"] == "high" and result == "wrong":
                accident_delta += 1
            if result == "complete" and progress_delta > 0:
                if "S02_last_complete" in state.strategy_flags and "S02_bonus_used" not in state.strategy_flags:
                    progress_delta += 1
                    safety_delta -= 2
                    state.strategy_flags.add("S02_bonus_used")
                state.strategy_flags.add("S02_last_complete")
            else:
                state.strategy_flags.discard("S02_last_complete")
        elif sid == "S03" and result == "complete":
            hazard_delta -= 1
        elif sid == "S04" and state.pending_state >= 1 and result in {"complete", "control"}:
            hazard_delta -= 1
        elif sid == "S05" and active.contribution == 1:
            active.contribution += 1
        elif sid == "S06" and "equipment" in event.get("risk_tags", []) and result == "control":
            result = "complete"
            progress_delta += 1 if task_match else 0
        elif sid == "S07" and len(state.knowledge_points) % 3 == 0 and result in {"complete", "control"}:
            active.contribution += 1
        elif sid == "S08" and event["severity"] == "high" and accident_delta > 0:
            accident_delta -= 1

    if active.post_id == "recorder" and ("record" in action_tags or "review" in action_tags):
        active.contribution += 1
    elif active.post_id == "resource_manager" and result in {"complete", "control"}:
        active.contribution += 1
    elif active.post_id == "operator" and progress_delta > 0:
        active.contribution += 1

    state.safety += safety_delta
    state.hazards = max(0, state.hazards + hazard_delta)
    state.accident = max(0, state.accident + accident_delta)
    state.progress += progress_delta
    state.pending_state = next_pending_state
    state.pending_event_id = event["id"] if next_pending_state >= 0 else ""

    return {
        "turn": state.turn,
        "task_id": task["id"],
        "event_id": event["id"],
        "post_id": active.post_id,
        "result": result,
        "selected_actions": "|".join(action["id"] for action in selected),
        "progress_delta": progress_delta,
        "safety_delta": safety_delta,
        "hazard_delta": hazard_delta,
        "accident_delta": accident_delta,
        "pending_state": STATE_NAMES.get(state.pending_state, "none"),
    }


def assign_posts(players: list[Player], turn: int) -> None:
    post_cycle = ["safety_officer", "operator", "recorder", "resource_manager"]
    for idx, player in enumerate(players):
        player.post_id = post_cycle[(idx + turn - 1) % len(post_cycle)]


def play_game(cards: dict[str, list[dict[str, Any]]], mode: str, strategy: dict[str, Any] | None, player_count: int) -> tuple[dict[str, Any], list[dict[str, Any]]]:
    config = MODES[mode]
    state = GameState(mode=mode, safety=config.safety, hazards=config.initial_hazards)
    apply_strategy_setup(strategy, state)
    players = [Player(role_id=role["id"]) for role in random.sample(cards["role"], player_count)]
    action_deck = cards["action"][:]
    random.shuffle(action_deck)
    discard: list[dict[str, Any]] = []
    hand: list[dict[str, Any]] = []
    refill_hand(hand, action_deck, discard, config.hand_size)
    stage_order = ["prepare", "prepare", "operate", "operate", "operate", "close", "emergency", "close"]
    turn_logs = []

    for turn in range(1, config.max_turns + 1):
        state.turn = turn
        if state.pending_state == 1:
            state.hazards += 1
        elif state.pending_state == 2:
            state.safety -= 1
        assign_posts(players, turn)
        task = choose_task(cards["task"], stage_order, turn)
        event = choose_event(cards["event"], task)
        maybe_redraw(state, hand, action_deck, discard, event, config)
        active, selected = choose_action_plan(hand, event, task, players)
        for action in selected:
            if action in hand:
                hand.remove(action)
                discard.append(action)
        turn_logs.append(resolve_turn(state, players, active, task, event, selected, strategy, config))
        if config.extra_event_turn and turn == config.extra_event_turn:
            extra_event = random.choice(cards["event"])
            active_extra, selected_extra = choose_action_plan(hand, extra_event, task, players)
            selected_extra = selected_extra[:1]
            for action in selected_extra:
                if action in hand:
                    hand.remove(action)
                    discard.append(action)
            turn_logs.append(resolve_turn(state, players, active_extra, task, extra_event, selected_extra, strategy, config))
        refill_hand(hand, action_deck, discard, config.hand_size)
        if state.safety <= 0 or state.accident >= 4 or state.hazards >= 5:
            break

    win = state.progress >= config.target_progress and state.safety > 0 and state.accident < 4 and state.hazards < 5
    loss_reason = ""
    if win:
        loss_reason = "win"
    elif state.safety <= 0:
        loss_reason = "safety_zero"
    elif state.accident >= 4:
        loss_reason = "accident_limit"
    elif state.hazards >= 5:
        loss_reason = "hazard_overflow"
    else:
        loss_reason = "progress_shortfall"

    row = {
        "mode": mode,
        "strategy_id": strategy["id"] if strategy else "none",
        "strategy_name": strategy["name"] if strategy else "无策略",
        "player_count": player_count,
        "win": int(win),
        "loss_reason": loss_reason,
        "turns": state.turn,
        "progress": state.progress,
        "safety": state.safety,
        "accident": state.accident,
        "hazards": state.hazards,
        "redraws_used": state.redraws_used,
        "completed_tasks": state.completed_tasks,
        "knowledge_count": len(state.knowledge_points),
        "avg_contribution": mean(player.contribution for player in players),
        "max_contribution": max(player.contribution for player in players),
        "min_contribution": min(player.contribution for player in players),
    }
    return row, turn_logs


def summarize(rows: list[dict[str, Any]], turn_logs: list[dict[str, Any]]) -> dict[str, Any]:
    by_scenario: dict[tuple[str, str], list[dict[str, Any]]] = defaultdict(list)
    for row in rows:
        by_scenario[(row["mode"], row["strategy_id"])].append(row)
    scenario_stats = []
    for (mode, strategy_id), items in sorted(by_scenario.items()):
        scenario_stats.append({
            "mode": mode,
            "strategy_id": strategy_id,
            "games": len(items),
            "win_rate": mean(item["win"] for item in items),
            "avg_progress": mean(item["progress"] for item in items),
            "avg_safety": mean(item["safety"] for item in items),
            "avg_accident": mean(item["accident"] for item in items),
            "avg_hazards": mean(item["hazards"] for item in items),
            "avg_knowledge_count": mean(item["knowledge_count"] for item in items),
            "avg_contribution": mean(item["avg_contribution"] for item in items),
            "loss_reasons": dict(Counter(item["loss_reason"] for item in items)),
        })
    action_counter = Counter()
    result_counter = Counter()
    post_counter = Counter()
    for log in turn_logs:
        for action_id in log["selected_actions"].split("|"):
            if action_id:
                action_counter[action_id] += 1
        result_counter[log["result"]] += 1
        post_counter[log["post_id"]] += 1
    total_actions = sum(action_counter.values()) or 1
    return {
        "scenario_stats": scenario_stats,
        "action_pick_rates": {key: value / total_actions for key, value in action_counter.most_common()},
        "result_distribution": dict(result_counter),
        "post_distribution": dict(post_counter),
    }


def write_csv(path: Path, rows: list[dict[str, Any]]) -> None:
    if not rows:
        return
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8-sig", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)


def run(args: argparse.Namespace) -> None:
    random.seed(args.seed)
    cards = load_cards()
    out_dir = OUTPUT_ROOT / args.run_id
    out_dir.mkdir(parents=True, exist_ok=True)
    strategies = [None] + cards["strategy"] if args.include_strategies else [None]
    rows: list[dict[str, Any]] = []
    all_turn_logs: list[dict[str, Any]] = []
    for mode in args.modes:
        for strategy in strategies:
            for _ in range(args.games_per_scenario):
                row, logs = play_game(cards, mode, strategy, args.players)
                rows.append(row)
                all_turn_logs.extend(logs)
    summary = summarize(rows, all_turn_logs)
    summary.update({
        "run_id": args.run_id,
        "seed": args.seed,
        "games_per_scenario": args.games_per_scenario,
        "players": args.players,
        "modes": args.modes,
        "include_strategies": args.include_strategies,
    })
    write_csv(out_dir / "game_results.csv", rows)
    write_csv(out_dir / "turn_logs.csv", all_turn_logs[: min(len(all_turn_logs), args.max_turn_logs)])
    (out_dir / "summary.json").write_text(json.dumps(summary, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps(summary, ensure_ascii=False, indent=2))


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--run-id", default="run_001_rules_baseline")
    parser.add_argument("--games-per-scenario", type=int, default=100)
    parser.add_argument("--seed", type=int, default=20260428)
    parser.add_argument("--players", type=int, default=4)
    parser.add_argument("--modes", nargs="+", default=["teaching", "standard", "challenge"], choices=list(MODES))
    parser.add_argument("--include-strategies", action="store_true")
    parser.add_argument("--max-turn-logs", type=int, default=5000)
    return parser.parse_args()


if __name__ == "__main__":
    run(parse_args())
