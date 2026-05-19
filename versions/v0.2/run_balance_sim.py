from __future__ import annotations

import argparse
import csv
import json
import random
from collections import Counter, defaultdict
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, Iterable, List, Sequence, Tuple


ACTIONS: Dict[str, str] = {
    "stop": "暂停操作",
    "ppe": "补全PPE",
    "label": "核对标签",
    "hood": "使用通风橱",
    "waste": "分类回收",
    "cleanup": "隔离与清理",
    "emergency": "使用应急设施",
    "report": "上报负责人",
}


SEVERITY_PENALTY = {
    "low": 1,
    "medium": 2,
    "high": 3,
}


SAFE_ACTIONS = {"stop", "report", "emergency"}
HAND_SIZE = 6


@dataclass(frozen=True)
class Task:
    task_id: str
    name: str


@dataclass(frozen=True)
class Event:
    event_id: str
    name: str
    severity: str
    key_action: str
    assist_actions: Tuple[str, ...]
    containment_combos: Tuple[Tuple[str, ...], ...] = ()
    major_accident_if_missing_key: bool = False
    urgent_only: bool = False


@dataclass(frozen=True)
class Mode:
    name: str
    initial_safety: int
    redraws: int
    progress_target: int
    extra_event_rounds: Tuple[int, ...]
    first_error_no_upgrade: bool = False


@dataclass(frozen=True)
class BotProfile:
    name: str
    key_bonus: int
    assist_bonus: int
    safe_bonus_medium: int
    safe_bonus_high: int
    generic_bonus: int
    synergy_bonus: int
    redraw_medium: bool
    redraw_high: bool
    redraw_low: bool = False
    noise_rate: float = 0.0
    conservative_bias: int = 0


TASKS: Tuple[Task, ...] = (
    Task("T01", "配制酸溶液"),
    Task("T02", "有机溶剂转移"),
    Task("T03", "加热回流"),
    Task("T04", "废液分类处理"),
    Task("T05", "气瓶连接使用"),
    Task("T06", "通风橱内称量与转移"),
    Task("T07", "清理实验台"),
    Task("T08", "紧急情况报告与撤离"),
)


EVENTS: Tuple[Event, ...] = (
    Event("E01", "未佩戴护目镜", "low", "ppe", ("stop",)),
    Event("E02", "试剂瓶标签模糊", "low", "label", ("stop",)),
    Event("E03", "实验台杂乱", "low", "cleanup", ("stop",)),
    Event("E04", "废液桶未及时封口", "low", "waste", ("label",)),
    Event("E05", "挥发性溶剂在开放环境中转移", "medium", "hood", ("stop",)),
    Event("E06", "有机溶剂附近存在火源", "medium", "stop", ("hood",)),
    Event("E07", "地面少量液体洒漏", "medium", "cleanup", ("report",), (("stop", "report"),)),
    Event("E08", "玻璃器皿出现裂纹", "medium", "stop", ("report",)),
    Event("E09", "气瓶未固定", "medium", "stop", ("report",)),
    Event("E10", "通风橱内堆放过多物品", "medium", "cleanup", ("hood",), (("stop", "report"),)),
    Event("E11", "废液混放产生异常气味", "high", "stop", ("report",)),
    Event("E12", "加热装置无人值守", "high", "stop", ("report",)),
    Event("E13", "皮肤接触腐蚀性液体", "high", "emergency", ("report",), urgent_only=True),
    Event("E14", "容器内压力异常升高", "high", "stop", ("report",)),
    Event("E15", "实验台出现小型明火", "high", "emergency", ("report",), urgent_only=True),
    Event("E16", "刺激性气味明显增强", "high", "stop", ("hood", "report")),
)


MODES: Dict[str, Mode] = {
    "teaching": Mode("teaching", initial_safety=9, redraws=3, progress_target=4, extra_event_rounds=(), first_error_no_upgrade=True),
    "standard": Mode("standard", initial_safety=8, redraws=2, progress_target=4, extra_event_rounds=()),
    "challenge": Mode("challenge", initial_safety=7, redraws=1, progress_target=4, extra_event_rounds=(3, 5)),
}


BOT_PROFILES: Dict[str, BotProfile] = {
    "expert": BotProfile("expert", 100, 70, 42, 48, 8, 28, True, True, True, noise_rate=0.0, conservative_bias=8),
    "balanced": BotProfile("balanced", 92, 62, 35, 42, 6, 24, True, True, False, noise_rate=0.04, conservative_bias=5),
    "safe": BotProfile("safe", 88, 54, 45, 52, 5, 22, True, True, False, noise_rate=0.06, conservative_bias=12),
    "learner": BotProfile("learner", 80, 48, 30, 36, 4, 18, False, True, False, noise_rate=0.18, conservative_bias=3),
    "reckless": BotProfile("reckless", 72, 34, 10, 16, 7, 10, False, False, False, noise_rate=0.28, conservative_bias=-4),
}


def action_label(action_id: str) -> str:
    return ACTIONS[action_id]


def event_lookup(event_id: str) -> Event:
    for event in EVENTS:
        if event.event_id == event_id:
            return event
    raise KeyError(event_id)


class ActionDeck:
    def __init__(self, rng: random.Random) -> None:
        self.rng = rng
        self.draw_pile: List[str] = [action for action in ACTIONS for _ in range(3)]
        self.discard_pile: List[str] = []
        self.rng.shuffle(self.draw_pile)

    def draw(self, count: int) -> List[str]:
        cards: List[str] = []
        while len(cards) < count:
            if not self.draw_pile:
                if not self.discard_pile:
                    break
                self.draw_pile = self.discard_pile
                self.discard_pile = []
                self.rng.shuffle(self.draw_pile)
            cards.append(self.draw_pile.pop())
        return cards

    def discard(self, cards: Iterable[str]) -> None:
        self.discard_pile.extend(cards)


def sample_without_replacement(rng: random.Random, items: Sequence, count: int) -> List:
    return rng.sample(list(items), count)


def choose_team_order(team: Tuple[str, str], rng: random.Random) -> List[str]:
    ordered = list(team)
    rng.shuffle(ordered)
    return ordered


def score_action(
    profile: BotProfile,
    action: str,
    event: Event,
    already_chosen: Sequence[str],
    hand: Sequence[str],
    rng: random.Random,
) -> float:
    score = profile.generic_bonus
    if action == event.key_action:
        score += profile.key_bonus
    if action in event.assist_actions:
        score += profile.assist_bonus
    if event.severity == "medium" and action in SAFE_ACTIONS:
        score += profile.safe_bonus_medium
    if event.severity == "high" and action in SAFE_ACTIONS:
        score += profile.safe_bonus_high
    if action == "report":
        score += profile.conservative_bias
    if action == "stop":
        score += profile.conservative_bias
    if already_chosen:
        prior = already_chosen[0]
        combo = {prior, action}
        if prior == event.key_action and action in event.assist_actions:
            score += profile.synergy_bonus
        if action == event.key_action and prior in event.assist_actions:
            score += profile.synergy_bonus
        for containment_combo in event.containment_combos:
            if combo.issuperset(containment_combo):
                score += profile.synergy_bonus - 4
    if event.urgent_only and action == "emergency":
        score += 20
    if action in already_chosen:
        score -= 50
    if profile.noise_rate > 0:
        score += rng.uniform(-15.0, 15.0) * profile.noise_rate
    return score


def sorted_actions_for_redraw(profile: BotProfile, event: Event, hand: Sequence[str], rng: random.Random) -> List[str]:
    ranked = sorted(
        hand,
        key=lambda action: score_action(profile, action, event, (), hand, rng),
    )
    return list(ranked)


def should_redraw(profile: BotProfile, event: Event, hand: Sequence[str], redraws_left: int) -> bool:
    if redraws_left <= 0 or event.key_action in hand:
        return False
    severity_flag = {
        "low": profile.redraw_low,
        "medium": profile.redraw_medium,
        "high": profile.redraw_high,
    }[event.severity]
    if not severity_flag:
        return False
    hand_set = set(hand)
    for combo in event.containment_combos:
        if set(combo).issubset(hand_set):
            return False
    if {"stop", "report"}.issubset(hand_set) and event.severity != "low":
        return False
    return True


def choose_action(
    profile: BotProfile,
    event: Event,
    hand: Sequence[str],
    already_chosen: Sequence[str],
    rng: random.Random,
) -> str | None:
    if not hand:
        return None
    scored = [
        (score_action(profile, action, event, already_chosen, hand, rng), index, action)
        for index, action in enumerate(hand)
    ]
    scored.sort(reverse=True)
    return scored[0][2]


def containment_hit(event: Event, actions: Sequence[str]) -> bool:
    action_set = set(actions)
    for combo in event.containment_combos:
        if set(combo).issubset(action_set):
            return True
    return False


def evaluate_event(event: Event, chosen_actions: Sequence[str], task_active: bool, first_error_upgrade_waived: bool) -> Dict[str, object]:
    action_set = set(chosen_actions)
    severity_penalty = SEVERITY_PENALTY[event.severity]
    result = {
        "outcome": "",
        "progress_gain": 0,
        "safety_loss": 0,
        "upgrade_gain": 0,
        "major_accident": False,
    }
    if event.key_action in action_set:
        if any(action in event.assist_actions for action in action_set if action != event.key_action):
            result["outcome"] = "full"
            result["progress_gain"] = 1 if task_active else 0
            return result
        result["outcome"] = "partial"
        result["progress_gain"] = 1 if task_active else 0
        result["safety_loss"] = 0 if event.severity == "low" else 1
        return result

    if not event.urgent_only and any(action in event.assist_actions for action in action_set):
        result["outcome"] = "contained"
        result["safety_loss"] = 1 if event.severity != "high" else 2
        return result

    if containment_hit(event, chosen_actions):
        result["outcome"] = "contained"
        result["safety_loss"] = 1
        return result

    if event.major_accident_if_missing_key:
        result["outcome"] = "major_accident"
        result["safety_loss"] = severity_penalty
        result["upgrade_gain"] = 1
        result["major_accident"] = True
        return result

    if event.urgent_only:
        result["outcome"] = "blatant"
        result["safety_loss"] = severity_penalty
        result["upgrade_gain"] = 1
        return result

    result["outcome"] = "error"
    result["safety_loss"] = severity_penalty
    result["upgrade_gain"] = 0 if event.severity == "low" else 1
    if first_error_upgrade_waived and result["upgrade_gain"] > 0:
        result["upgrade_gain"] = 0
    return result


def build_round_schedule(rng: random.Random, mode: Mode) -> List[Tuple[int, bool, Task | None, Event]]:
    tasks = sample_without_replacement(rng, TASKS, 6)
    main_events = sample_without_replacement(rng, EVENTS, 6)
    extra_needed = len(mode.extra_event_rounds)
    extra_events = sample_without_replacement(rng, EVENTS, extra_needed) if extra_needed else []
    schedule: List[Tuple[int, bool, Task | None, Event]] = []
    extra_index = 0
    for round_number in range(1, 7):
        schedule.append((round_number, True, tasks[round_number - 1], main_events[round_number - 1]))
        if round_number in mode.extra_event_rounds:
            schedule.append((round_number, False, None, extra_events[extra_index]))
            extra_index += 1
    return schedule


def play_game(
    rng: random.Random,
    mode: Mode,
    team: Tuple[str, str],
    capture_log: bool = False,
) -> Dict[str, object]:
    deck = ActionDeck(rng)
    hand = deck.draw(HAND_SIZE)
    state = {
        "safety": mode.initial_safety,
        "progress": 0,
        "upgrade": 0,
        "redraws_left": mode.redraws,
        "turns_resolved": 0,
        "first_error_consumed": False,
    }
    schedule = build_round_schedule(rng, mode)
    turn_logs: List[Dict[str, object]] = []
    turn_records: List[Dict[str, object]] = []

    for round_number, task_active, task, event in schedule:
        state["turns_resolved"] += 1
        ordered_team = choose_team_order(team, rng)
        redraw_used = False

        if any(should_redraw(BOT_PROFILES[bot_name], event, hand, state["redraws_left"]) for bot_name in ordered_team):
            ranked_discards = []
            for bot_name in ordered_team:
                ranked_discards.extend(sorted_actions_for_redraw(BOT_PROFILES[bot_name], event, hand, rng)[:2])
            discard_pool = Counter(ranked_discards)
            to_discard: List[str] = []
            for action, _ in discard_pool.most_common():
                if action in hand and len(to_discard) < 2:
                    hand.remove(action)
                    to_discard.append(action)
            while len(to_discard) < 2 and hand:
                to_discard.append(hand.pop())
            deck.discard(to_discard)
            hand.extend(deck.draw(len(to_discard)))
            state["redraws_left"] -= 1
            redraw_used = True

        hand_before = list(hand)
        chosen_actions: List[str] = []
        for bot_name in ordered_team:
            action = choose_action(BOT_PROFILES[bot_name], event, hand, chosen_actions, rng)
            if action is None:
                continue
            chosen_actions.append(action)
            hand.remove(action)
            if len(chosen_actions) >= 2:
                break

        evaluation = evaluate_event(
            event,
            chosen_actions=chosen_actions,
            task_active=task_active,
            first_error_upgrade_waived=mode.first_error_no_upgrade and not state["first_error_consumed"],
        )
        state["progress"] += int(evaluation["progress_gain"])
        state["safety"] -= int(evaluation["safety_loss"])
        state["upgrade"] += int(evaluation["upgrade_gain"])

        if evaluation["outcome"] in {"error", "blatant"} and int(evaluation["upgrade_gain"]) >= 0:
            state["first_error_consumed"] = True

        deck.discard(chosen_actions)
        hand.extend(deck.draw(HAND_SIZE - len(hand)))

        turn_log = {
            "round": round_number,
            "task_active": task_active,
            "task_id": task.task_id if task else "",
            "task_name": task.name if task else "",
            "event_id": event.event_id,
            "event_name": event.name,
            "severity": event.severity,
            "team_order": ordered_team,
            "hand_before": hand_before,
            "chosen_actions": list(chosen_actions),
            "outcome": evaluation["outcome"],
            "progress_after": state["progress"],
            "safety_after": state["safety"],
            "upgrade_after": state["upgrade"],
            "redraw_used": redraw_used,
        }
        turn_records.append(
            {
                "event_id": event.event_id,
                "outcome": evaluation["outcome"],
                "chosen_actions": list(chosen_actions),
            }
        )
        if capture_log:
            turn_logs.append(turn_log)

        if bool(evaluation["major_accident"]):
            return {
                "result": "loss",
                "loss_reason": "major_accident",
                "excellent": False,
                "progress": state["progress"],
                "safety": state["safety"],
                "upgrade": state["upgrade"],
                "turns_resolved": state["turns_resolved"],
                "redraws_used": mode.redraws - state["redraws_left"],
                "turn_records": turn_records,
                "turn_logs": turn_logs,
            }
        if state["safety"] <= 0:
            return {
                "result": "loss",
                "loss_reason": "safety_zero",
                "excellent": False,
                "progress": state["progress"],
                "safety": state["safety"],
                "upgrade": state["upgrade"],
                "turns_resolved": state["turns_resolved"],
                "redraws_used": mode.redraws - state["redraws_left"],
                "turn_records": turn_records,
                "turn_logs": turn_logs,
            }
        if state["upgrade"] >= 3:
            return {
                "result": "loss",
                "loss_reason": "upgrade_limit",
                "excellent": False,
                "progress": state["progress"],
                "safety": state["safety"],
                "upgrade": state["upgrade"],
                "turns_resolved": state["turns_resolved"],
                "redraws_used": mode.redraws - state["redraws_left"],
                "turn_records": turn_records,
                "turn_logs": turn_logs,
            }

    won = state["progress"] >= mode.progress_target and state["safety"] > 0
    excellent = won and state["progress"] >= 6 and state["safety"] >= 5
    return {
        "result": "win" if won else "loss",
        "loss_reason": "" if won else "progress_shortfall",
        "excellent": excellent,
        "progress": state["progress"],
        "safety": state["safety"],
        "upgrade": state["upgrade"],
        "turns_resolved": state["turns_resolved"],
        "redraws_used": mode.redraws - state["redraws_left"],
        "turn_records": turn_records,
        "turn_logs": turn_logs,
    }


def team_label(team: Tuple[str, str]) -> str:
    return "+".join(team)


def all_standard_teams() -> List[Tuple[str, str]]:
    names = sorted(BOT_PROFILES)
    pairs: List[Tuple[str, str]] = []
    for index, left in enumerate(names):
        for right in names[index:]:
            pairs.append((left, right))
    return pairs


def run_simulation(games_per_team: int, seed: int) -> Dict[str, object]:
    rng = random.Random(seed)
    summary_rows: List[Dict[str, object]] = []
    action_rows: List[Dict[str, object]] = []
    event_rows: List[Dict[str, object]] = []
    game_rows: List[Dict[str, object]] = []
    sampled_logs: List[Dict[str, object]] = []

    run_matrix: List[Tuple[Mode, Tuple[str, str]]] = []
    for team in all_standard_teams():
        run_matrix.append((MODES["standard"], team))
    for mode_name in ("teaching", "challenge"):
        run_matrix.append((MODES[mode_name], ("balanced", "balanced")))

    for mode, team in run_matrix:
        wins = 0
        excellent_wins = 0
        progress_total = 0
        safety_total = 0
        upgrade_total = 0
        turns_total = 0
        redraw_total = 0
        loss_reasons = Counter()
        action_counter = Counter()
        event_counter = Counter()
        event_outcomes: Dict[str, Counter] = defaultdict(Counter)

        for game_index in range(games_per_team):
            capture_log = game_index < 20
            result = play_game(rng, mode, team, capture_log=capture_log)
            wins += 1 if result["result"] == "win" else 0
            excellent_wins += 1 if result["excellent"] else 0
            progress_total += int(result["progress"])
            safety_total += int(result["safety"])
            upgrade_total += int(result["upgrade"])
            turns_total += int(result["turns_resolved"])
            redraw_total += int(result["redraws_used"])
            if result["loss_reason"]:
                loss_reasons[str(result["loss_reason"])] += 1

            game_rows.append(
                {
                    "mode": mode.name,
                    "team": team_label(team),
                    "game_index": game_index,
                    "result": result["result"],
                    "excellent": int(bool(result["excellent"])),
                    "loss_reason": result["loss_reason"],
                    "progress": result["progress"],
                    "safety": result["safety"],
                    "upgrade": result["upgrade"],
                    "turns_resolved": result["turns_resolved"],
                    "redraws_used": result["redraws_used"],
                }
            )

            for turn_record in result["turn_records"]:
                event_counter[turn_record["event_id"]] += 1
                event_outcomes[turn_record["event_id"]][turn_record["outcome"]] += 1
                for action in turn_record["chosen_actions"]:
                    action_counter[action] += 1
            for turn_log in result["turn_logs"]:
                sampled_logs.append(
                    {
                        "mode": mode.name,
                        "team": team_label(team),
                        "game_index": game_index,
                        **turn_log,
                    }
                )

        games = games_per_team
        summary_rows.append(
            {
                "mode": mode.name,
                "team": team_label(team),
                "games": games,
                "win_rate": round(wins / games, 4),
                "excellent_rate": round(excellent_wins / games, 4),
                "avg_progress": round(progress_total / games, 3),
                "avg_safety": round(safety_total / games, 3),
                "avg_upgrade": round(upgrade_total / games, 3),
                "avg_turns": round(turns_total / games, 3),
                "avg_redraws_used": round(redraw_total / games, 3),
                "loss_major_accident": loss_reasons["major_accident"],
                "loss_safety_zero": loss_reasons["safety_zero"],
                "loss_upgrade_limit": loss_reasons["upgrade_limit"],
                "loss_progress_shortfall": loss_reasons["progress_shortfall"],
            }
        )

        total_action_picks = sum(action_counter.values()) or 1
        for action_id in ACTIONS:
            picks = action_counter[action_id]
            action_rows.append(
                {
                    "mode": mode.name,
                    "team": team_label(team),
                    "action_id": action_id,
                    "action_name": action_label(action_id),
                    "picks": picks,
                    "pick_rate": round(picks / total_action_picks, 4),
                }
            )

        for event in EVENTS:
            appearances = event_counter[event.event_id]
            outcomes = event_outcomes[event.event_id]
            denominator = appearances or 1
            event_rows.append(
                {
                    "mode": mode.name,
                    "team": team_label(team),
                    "event_id": event.event_id,
                    "event_name": event.name,
                    "appearances": appearances,
                    "full_rate": round(outcomes["full"] / denominator, 4),
                    "partial_rate": round(outcomes["partial"] / denominator, 4),
                    "contained_rate": round(outcomes["contained"] / denominator, 4),
                    "error_rate": round(outcomes["error"] / denominator, 4),
                    "blatant_rate": round(outcomes["blatant"] / denominator, 4),
                    "major_rate": round(outcomes["major_accident"] / denominator, 4),
                }
            )

    return {
        "summary_rows": summary_rows,
        "action_rows": action_rows,
        "event_rows": event_rows,
        "game_rows": game_rows,
        "sampled_logs": sampled_logs,
        "seed": seed,
        "games_per_team": games_per_team,
    }


def write_csv(path: Path, rows: List[Dict[str, object]]) -> None:
    if not rows:
        path.write_text("", encoding="utf-8")
        return
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)


def write_json(path: Path, payload: Dict[str, object]) -> None:
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")


def build_summary_payload(sim_result: Dict[str, object], run_id: str) -> Dict[str, object]:
    standard_rows = [row for row in sim_result["summary_rows"] if row["mode"] == "standard"]
    best_standard = max(standard_rows, key=lambda row: row["win_rate"])
    weakest_standard = min(standard_rows, key=lambda row: row["win_rate"])
    balanced_standard = next(row for row in standard_rows if row["team"] == "balanced+balanced")
    return {
        "run_id": run_id,
        "seed": sim_result["seed"],
        "games_per_team": sim_result["games_per_team"],
        "scenarios_tested": len(sim_result["summary_rows"]),
        "best_standard_team": best_standard,
        "weakest_standard_team": weakest_standard,
        "balanced_standard_team": balanced_standard,
    }


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Run balance simulations for boardgame v0.1")
    parser.add_argument("--games-per-team", type=int, default=2000)
    parser.add_argument("--seed", type=int, default=20260408)
    parser.add_argument("--run-id", type=str, default="run_001")
    parser.add_argument(
        "--output-root",
        type=Path,
        default=Path(r"C:\PKU\Term2\实验室安全作品大赛\data\v0.1"),
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    sim_result = run_simulation(games_per_team=args.games_per_team, seed=args.seed)
    output_dir = args.output_root / args.run_id
    output_dir.mkdir(parents=True, exist_ok=True)

    write_csv(output_dir / "team_stats.csv", sim_result["summary_rows"])
    write_csv(output_dir / "action_stats.csv", sim_result["action_rows"])
    write_csv(output_dir / "event_stats.csv", sim_result["event_rows"])
    write_csv(output_dir / "game_results.csv", sim_result["game_rows"])

    with (output_dir / "sample_turn_logs.jsonl").open("w", encoding="utf-8") as handle:
        for row in sim_result["sampled_logs"]:
            handle.write(json.dumps(row, ensure_ascii=False) + "\n")

    summary_payload = build_summary_payload(sim_result, args.run_id)
    write_json(output_dir / "summary.json", summary_payload)

    print(json.dumps(summary_payload, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
