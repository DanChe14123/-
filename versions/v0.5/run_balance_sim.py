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
    preferred_actions: Tuple[str, ...]
    reward: str
    linked_events: Tuple[str, ...]


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
    initial_hazards: int
    redraws: int
    progress_target: int
    extra_event_rounds: Tuple[int, ...]
    first_error_no_upgrade: bool = False


@dataclass(frozen=True)
class BotProfile:
    name: str
    key_bonus: int
    assist_bonus: int
    task_bonus: int
    safe_bonus_medium: int
    safe_bonus_high: int
    generic_bonus: int
    synergy_bonus: int
    redraw_medium: bool
    redraw_high: bool
    redraw_low: bool = False
    noise_rate: float = 0.0
    conservative_bias: int = 0


@dataclass(frozen=True)
class Strategy:
    strategy_id: str
    name: str


TASKS: Tuple[Task, ...] = (
    Task("T01", "配制酸溶液", ("ppe", "label", "emergency"), "recover_safety", ("E01", "E02", "E13")),
    Task("T02", "有机溶剂转移", ("hood", "stop", "label"), "clear_hazard", ("E05", "E06", "E16")),
    Task("T03", "加热回流", ("stop", "report", "emergency"), "reduce_upgrade", ("E06", "E12", "E14", "E15")),
    Task("T04", "废液分类处理", ("waste", "label", "stop"), "clear_hazard", ("E04", "E11", "E16")),
    Task("T05", "气瓶连接使用", ("stop", "report", "label"), "reduce_upgrade", ("E08", "E09", "E14")),
    Task("T06", "通风橱内称量与转移", ("hood", "cleanup", "label"), "gain_redraw", ("E03", "E05", "E10", "E16")),
    Task("T07", "清理实验台", ("cleanup", "waste", "ppe"), "recover_safety", ("E03", "E07", "E08")),
    Task("T08", "紧急情况报告与撤离", ("report", "emergency", "stop"), "control_choice", ("E11", "E13", "E15", "E16")),
    Task("T09", "危险化学品领用与登记", ("label", "report", "stop"), "reduce_upgrade", ("E02", "E03", "E08")),
    Task("T10", "低温/高温设备使用", ("ppe", "stop", "emergency"), "recover_safety", ("E01", "E12", "E13")),
    Task("T11", "旋蒸或离心设备操作", ("stop", "hood", "cleanup"), "gain_redraw", ("E05", "E08", "E14", "E16")),
    Task("T12", "实验结束后的交接检查", ("cleanup", "waste", "label"), "clear_hazard", ("E03", "E04", "E10", "E12")),
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
    "teaching": Mode("teaching", initial_safety=9, initial_hazards=0, redraws=3, progress_target=4, extra_event_rounds=(), first_error_no_upgrade=True),
    "standard": Mode("standard", initial_safety=8, initial_hazards=0, redraws=2, progress_target=4, extra_event_rounds=()),
    "challenge": Mode("challenge", initial_safety=7, initial_hazards=1, redraws=1, progress_target=4, extra_event_rounds=(3, 5)),
}


BOT_PROFILES: Dict[str, BotProfile] = {
    "expert": BotProfile("expert", 100, 70, 34, 42, 48, 8, 28, True, True, True, noise_rate=0.0, conservative_bias=8),
    "balanced": BotProfile("balanced", 92, 62, 28, 35, 42, 6, 24, True, True, False, noise_rate=0.04, conservative_bias=5),
    "safe": BotProfile("safe", 88, 54, 18, 45, 52, 5, 22, True, True, False, noise_rate=0.06, conservative_bias=12),
    "learner": BotProfile("learner", 80, 48, 20, 30, 36, 4, 18, False, True, False, noise_rate=0.18, conservative_bias=3),
    "reckless": BotProfile("reckless", 72, 34, 12, 10, 16, 7, 10, False, False, False, noise_rate=0.28, conservative_bias=-4),
}

STRATEGIES: Dict[str, Strategy] = {
    "none": Strategy("none", "无策略"),
    "stable_management": Strategy("stable_management", "稳健管理"),
    "efficiency_first": Strategy("efficiency_first", "效率优先"),
    "standards_first": Strategy("standards_first", "规范先行"),
    "risk_isolation": Strategy("risk_isolation", "风险隔离"),
}

EVENTS_BY_ID: Dict[str, Event] = {event.event_id: event for event in EVENTS}
TASKS_BY_ID: Dict[str, Task] = {task.task_id: task for task in TASKS}


def action_label(action_id: str) -> str:
    return ACTIONS[action_id]


def event_lookup(event_id: str) -> Event:
    return EVENTS_BY_ID[event_id]


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
    task: Task | None,
    event: Event,
    already_chosen: Sequence[str],
    hand: Sequence[str],
    hazards: int,
    rng: random.Random,
) -> float:
    score = profile.generic_bonus
    if action == event.key_action:
        score += profile.key_bonus
    if action in event.assist_actions:
        score += profile.assist_bonus
    if task and action in task.preferred_actions:
        score += profile.task_bonus
    if event.severity == "medium" and action in SAFE_ACTIONS:
        score += profile.safe_bonus_medium
    if event.severity == "high" and action in SAFE_ACTIONS:
        score += profile.safe_bonus_high
    if hazards >= 2 and action in SAFE_ACTIONS:
        score += 12
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
        if task and prior in task.preferred_actions and action in task.preferred_actions:
            score += profile.synergy_bonus - 6
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


def sorted_actions_for_redraw(profile: BotProfile, task: Task | None, event: Event, hand: Sequence[str], hazards: int, rng: random.Random) -> List[str]:
    ranked = sorted(
        hand,
        key=lambda action: score_action(profile, action, task, event, (), hand, hazards, rng),
    )
    return list(ranked)


def should_redraw(profile: BotProfile, task: Task | None, event: Event, hand: Sequence[str], redraws_left: int, hazards: int) -> bool:
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
    if task and any(action in hand_set for action in task.preferred_actions) and event.severity == "low" and hazards <= 1:
        return False
    if {"stop", "report"}.issubset(hand_set) and event.severity != "low":
        return False
    return True


def choose_action(
    profile: BotProfile,
    task: Task | None,
    event: Event,
    hand: Sequence[str],
    already_chosen: Sequence[str],
    hazards: int,
    rng: random.Random,
) -> str | None:
    if not hand:
        return None
    scored = [
        (score_action(profile, action, task, event, already_chosen, hand, hazards, rng), index, action)
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


def task_completed(task: Task | None, chosen_actions: Sequence[str], outcome: str) -> bool:
    if task is None:
        return False
    if outcome not in {"full", "partial"}:
        return False
    return any(action in task.preferred_actions for action in chosen_actions)


def apply_task_reward(state: Dict[str, int], task: Task | None) -> str:
    if task is None:
        return ""
    if task.reward == "recover_safety":
        state["safety"] = min(10, state["safety"] + 1)
        return "recover_safety"
    if task.reward == "clear_hazard":
        state["hazards"] = max(0, state["hazards"] - 1)
        return "clear_hazard"
    if task.reward == "reduce_upgrade":
        state["upgrade"] = max(0, state["upgrade"] - 1)
        return "reduce_upgrade"
    if task.reward == "gain_redraw":
        state["redraws_left"] += 1
        return "gain_redraw"
    if task.reward == "control_choice":
        if state["hazards"] > 0:
            state["hazards"] -= 1
            return "clear_hazard"
        state["upgrade"] = max(0, state["upgrade"] - 1)
        return "reduce_upgrade"
    return ""


def cycle_one_hand_card(
    team: Tuple[str, str],
    hand: List[str],
    deck: ActionDeck,
    task: Task | None,
    event: Event,
    hazards: int,
    rng: random.Random,
) -> str:
    if not hand:
        return ""
    scored_cards: List[Tuple[float, str]] = []
    for action in hand:
        total_score = 0.0
        for bot_name in team:
            total_score += score_action(BOT_PROFILES[bot_name], action, task, event, (), hand, hazards, rng)
        scored_cards.append((total_score, action))
    scored_cards.sort()
    discard_action = scored_cards[0][1]
    hand.remove(discard_action)
    deck.discard([discard_action])
    hand.extend(deck.draw(1))
    return discard_action


def evaluate_event(event: Event, chosen_actions: Sequence[str], first_error_upgrade_waived: bool) -> Dict[str, object]:
    action_set = set(chosen_actions)
    severity_penalty = SEVERITY_PENALTY[event.severity]
    result = {
        "outcome": "",
        "safety_loss": 0,
        "upgrade_gain": 0,
        "major_accident": False,
    }
    if event.key_action in action_set:
        if any(action in event.assist_actions for action in action_set if action != event.key_action):
            result["outcome"] = "full"
            return result
        result["outcome"] = "partial"
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
    extra_needed = len(mode.extra_event_rounds)
    schedule: List[Tuple[int, bool, Task | None, Event]] = []
    used_events: set[str] = set()
    for round_number in range(1, 7):
        task = tasks[round_number - 1]
        linked_candidates = [event_id for event_id in task.linked_events if event_id not in used_events]
        if not linked_candidates:
            linked_candidates = list(task.linked_events)
        main_event_id = rng.choice(linked_candidates)
        used_events.add(main_event_id)
        schedule.append((round_number, True, task, event_lookup(main_event_id)))
        if round_number in mode.extra_event_rounds:
            global_candidates = [event.event_id for event in EVENTS if event.event_id not in used_events]
            if not global_candidates:
                global_candidates = [event.event_id for event in EVENTS]
            extra_event_id = rng.choice(global_candidates)
            used_events.add(extra_event_id)
            schedule.append((round_number, False, None, event_lookup(extra_event_id)))
    return schedule


def play_game(
    rng: random.Random,
    mode: Mode,
    team: Tuple[str, str],
    strategy_id: str,
    capture_log: bool = False,
) -> Dict[str, object]:
    deck = ActionDeck(rng)
    hand = deck.draw(HAND_SIZE)
    state = {
        "safety": mode.initial_safety + (1 if strategy_id == "stable_management" else 0),
        "hazards": mode.initial_hazards,
        "progress": 0,
        "upgrade": 0,
        "redraws_left": mode.redraws,
        "redraws_used_total": 0,
        "redraws_gained_total": 0,
        "turns_resolved": 0,
        "first_error_consumed": False,
        "last_upkeep_round": 0,
        "stable_shield_used": False,
        "efficiency_progress_bonus_used": False,
        "standards_first_full_used": False,
        "previous_task_round_completed": False,
    }
    schedule = build_round_schedule(rng, mode)
    turn_logs: List[Dict[str, object]] = []
    turn_records: List[Dict[str, object]] = []

    for round_number, task_active, task, event in schedule:
        state["turns_resolved"] += 1
        upkeep_loss = 0
        if round_number != state["last_upkeep_round"]:
            if state["hazards"] >= 3:
                if strategy_id == "risk_isolation":
                    upkeep_loss = 0
                else:
                    upkeep_loss = 1
            state["safety"] -= upkeep_loss
            state["last_upkeep_round"] = round_number
            if state["safety"] <= 0:
                return {
                    "result": "loss",
                    "loss_reason": "hazard_pressure",
                    "strategy_id": strategy_id,
                    "excellent": False,
                    "progress": state["progress"],
                    "safety": state["safety"],
                    "upgrade": state["upgrade"],
                    "hazards": state["hazards"],
                    "turns_resolved": state["turns_resolved"],
                    "redraws_used": state["redraws_used_total"],
                    "turn_records": turn_records,
                    "turn_logs": turn_logs,
                }
        ordered_team = choose_team_order(team, rng)
        redraw_used = False
        cycled_card = ""

        if strategy_id == "risk_isolation" and state["hazards"] >= 3:
            cycled_card = cycle_one_hand_card(team, hand, deck, task, event, state["hazards"], rng)

        if any(should_redraw(BOT_PROFILES[bot_name], task, event, hand, state["redraws_left"], state["hazards"]) for bot_name in ordered_team):
            ranked_discards = []
            for bot_name in ordered_team:
                ranked_discards.extend(sorted_actions_for_redraw(BOT_PROFILES[bot_name], task, event, hand, state["hazards"], rng)[:2])
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
            state["redraws_used_total"] += 1
            redraw_used = True

        hand_before = list(hand)
        chosen_actions: List[str] = []
        for bot_name in ordered_team:
            action = choose_action(BOT_PROFILES[bot_name], task, event, hand, chosen_actions, state["hazards"], rng)
            if action is None:
                continue
            chosen_actions.append(action)
            hand.remove(action)
            if len(chosen_actions) >= 2:
                break

        evaluation = evaluate_event(
            event,
            chosen_actions=chosen_actions,
            first_error_upgrade_waived=mode.first_error_no_upgrade and not state["first_error_consumed"],
        )
        safety_loss = int(evaluation["safety_loss"])
        upgrade_gain = int(evaluation["upgrade_gain"])

        if strategy_id == "stable_management" and evaluation["outcome"] in {"error", "blatant"} and not state["stable_shield_used"] and safety_loss > 0:
            safety_loss -= 1
            state["stable_shield_used"] = True

        if strategy_id == "standards_first" and evaluation["outcome"] == "contained":
            safety_loss += 1

        if strategy_id == "efficiency_first" and event.severity == "high" and evaluation["outcome"] in {"error", "blatant"}:
            upgrade_gain += 1

        state["safety"] -= safety_loss
        state["upgrade"] += upgrade_gain
        task_done = task_completed(task if task_active else None, chosen_actions, str(evaluation["outcome"]))
        reward_applied = ""
        strategy_effects: List[str] = []
        if task_done:
            state["progress"] += 1

        if evaluation["outcome"] == "full":
            state["hazards"] = max(0, state["hazards"] - 1)
        elif evaluation["outcome"] in {"contained", "error", "blatant"}:
            state["hazards"] += 1

        if strategy_id == "standards_first" and evaluation["outcome"] == "full":
            state["hazards"] = max(0, state["hazards"] - 1)
            strategy_effects.append("extra_hazard_clear")
            if not state["standards_first_full_used"]:
                state["safety"] = min(10, state["safety"] + 1)
                state["standards_first_full_used"] = True
                strategy_effects.append("first_full_recover_safety")

        if evaluation["outcome"] in {"error", "blatant"} and int(evaluation["upgrade_gain"]) >= 0:
            state["first_error_consumed"] = True

        if task_done:
            reward_applied = apply_task_reward(state, task)
            if reward_applied == "gain_redraw":
                state["redraws_gained_total"] += 1

            if strategy_id == "efficiency_first":
                if not state["efficiency_progress_bonus_used"] and evaluation["outcome"] == "full":
                    state["progress"] += 1
                    state["efficiency_progress_bonus_used"] = True
                    strategy_effects.append("first_task_extra_progress")
                elif state["previous_task_round_completed"]:
                    state["hazards"] = max(0, state["hazards"] - 1)
                    strategy_effects.append("consecutive_task_clear_hazard")

        if strategy_id == "risk_isolation" and evaluation["outcome"] in {"full", "partial"} and any(action in {"stop", "cleanup"} for action in chosen_actions):
            state["redraws_left"] += 1
            state["redraws_gained_total"] += 1
            strategy_effects.append("temporary_redraw")

        if task_active:
            state["previous_task_round_completed"] = task_done

        deck.discard(chosen_actions)
        hand.extend(deck.draw(HAND_SIZE - len(hand)))

        turn_log = {
            "round": round_number,
            "upkeep_loss": upkeep_loss,
            "strategy_id": strategy_id,
            "task_active": task_active,
            "task_id": task.task_id if task else "",
            "task_name": task.name if task else "",
            "task_reward": task.reward if task else "",
            "event_id": event.event_id,
            "event_name": event.name,
            "severity": event.severity,
            "team_order": ordered_team,
            "hand_before": hand_before,
            "cycled_card": cycled_card,
            "chosen_actions": list(chosen_actions),
            "outcome": evaluation["outcome"],
            "task_completed": task_done,
            "reward_applied": reward_applied,
            "strategy_effects": strategy_effects,
            "progress_after": state["progress"],
            "safety_after": state["safety"],
            "upgrade_after": state["upgrade"],
            "hazards_after": state["hazards"],
            "redraw_used": redraw_used,
        }
        turn_records.append(
            {
                "round": round_number,
                "task_id": task.task_id if task else "",
                "event_id": event.event_id,
                "outcome": evaluation["outcome"],
                "chosen_actions": list(chosen_actions),
                "task_completed": task_done,
                "reward_applied": reward_applied,
                "strategy_id": strategy_id,
                "strategy_effects": list(strategy_effects),
                "hazards_after": state["hazards"],
            }
        )
        if capture_log:
            turn_logs.append(turn_log)

        if bool(evaluation["major_accident"]):
            return {
                "result": "loss",
                "loss_reason": "major_accident",
                "strategy_id": strategy_id,
                "excellent": False,
                "progress": state["progress"],
                "safety": state["safety"],
                "upgrade": state["upgrade"],
                "hazards": state["hazards"],
                "turns_resolved": state["turns_resolved"],
                "redraws_used": state["redraws_used_total"],
                "turn_records": turn_records,
                "turn_logs": turn_logs,
            }
        if state["safety"] <= 0:
            return {
                "result": "loss",
                "loss_reason": "safety_zero",
                "strategy_id": strategy_id,
                "excellent": False,
                "progress": state["progress"],
                "safety": state["safety"],
                "upgrade": state["upgrade"],
                "hazards": state["hazards"],
                "turns_resolved": state["turns_resolved"],
                "redraws_used": state["redraws_used_total"],
                "turn_records": turn_records,
                "turn_logs": turn_logs,
            }
        if state["upgrade"] >= 3:
            return {
                "result": "loss",
                "loss_reason": "upgrade_limit",
                "strategy_id": strategy_id,
                "excellent": False,
                "progress": state["progress"],
                "safety": state["safety"],
                "upgrade": state["upgrade"],
                "hazards": state["hazards"],
                "turns_resolved": state["turns_resolved"],
                "redraws_used": state["redraws_used_total"],
                "turn_records": turn_records,
                "turn_logs": turn_logs,
            }
        if state["hazards"] >= 4:
            return {
                "result": "loss",
                "loss_reason": "hazard_overflow",
                "strategy_id": strategy_id,
                "excellent": False,
                "progress": state["progress"],
                "safety": state["safety"],
                "upgrade": state["upgrade"],
                "hazards": state["hazards"],
                "turns_resolved": state["turns_resolved"],
                "redraws_used": state["redraws_used_total"],
                "turn_records": turn_records,
                "turn_logs": turn_logs,
            }

    required_progress = 5 if strategy_id == "efficiency_first" else mode.progress_target
    allowed_hazards = 2 if strategy_id == "stable_management" else 3
    upgrade_limit_for_win = 1 if strategy_id == "risk_isolation" else 2
    won = state["progress"] >= required_progress and state["safety"] > 0 and state["hazards"] <= allowed_hazards and state["upgrade"] <= upgrade_limit_for_win
    excellent = won and state["progress"] >= 5 and state["safety"] >= 5 and state["hazards"] <= 1
    return {
        "result": "win" if won else "loss",
        "loss_reason": "" if won else "progress_shortfall",
        "strategy_id": strategy_id,
        "excellent": excellent,
        "progress": state["progress"],
        "safety": state["safety"],
        "upgrade": state["upgrade"],
        "hazards": state["hazards"],
        "turns_resolved": state["turns_resolved"],
        "redraws_used": state["redraws_used_total"],
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
    task_rows: List[Dict[str, object]] = []
    game_rows: List[Dict[str, object]] = []
    sampled_logs: List[Dict[str, object]] = []

    run_matrix: List[Tuple[Mode, Tuple[str, str], str]] = []
    for team in all_standard_teams():
        run_matrix.append((MODES["standard"], team, "none"))
    for mode_name in ("teaching", "challenge"):
        run_matrix.append((MODES[mode_name], ("balanced", "balanced"), "none"))
    for strategy_id in ("stable_management", "efficiency_first", "standards_first", "risk_isolation"):
        run_matrix.append((MODES["standard"], ("balanced", "balanced"), strategy_id))

    for mode, team, strategy_id in run_matrix:
        wins = 0
        excellent_wins = 0
        progress_total = 0
        safety_total = 0
        upgrade_total = 0
        hazards_total = 0
        turns_total = 0
        redraw_total = 0
        task_completed_total = 0
        loss_reasons = Counter()
        action_counter = Counter()
        event_counter = Counter()
        event_outcomes: Dict[str, Counter] = defaultdict(Counter)
        task_counter = Counter()
        task_completion_counter = Counter()
        reward_counter = Counter()

        for game_index in range(games_per_team):
            capture_log = game_index < 20
            result = play_game(rng, mode, team, strategy_id=strategy_id, capture_log=capture_log)
            wins += 1 if result["result"] == "win" else 0
            excellent_wins += 1 if result["excellent"] else 0
            progress_total += int(result["progress"])
            safety_total += int(result["safety"])
            upgrade_total += int(result["upgrade"])
            hazards_total += int(result["hazards"])
            turns_total += int(result["turns_resolved"])
            redraw_total += int(result["redraws_used"])
            if result["loss_reason"]:
                loss_reasons[str(result["loss_reason"])] += 1

            game_rows.append(
                {
                    "mode": mode.name,
                    "team": team_label(team),
                    "strategy_id": strategy_id,
                    "strategy_name": STRATEGIES[strategy_id].name,
                    "game_index": game_index,
                    "result": result["result"],
                    "excellent": int(bool(result["excellent"])),
                    "loss_reason": result["loss_reason"],
                    "progress": result["progress"],
                    "safety": result["safety"],
                    "upgrade": result["upgrade"],
                    "hazards": result["hazards"],
                    "turns_resolved": result["turns_resolved"],
                    "redraws_used": result["redraws_used"],
                }
            )

            for turn_record in result["turn_records"]:
                event_counter[turn_record["event_id"]] += 1
                event_outcomes[turn_record["event_id"]][turn_record["outcome"]] += 1
                if turn_record["task_id"]:
                    task_counter[turn_record["task_id"]] += 1
                if turn_record["task_completed"]:
                    task_completed_total += 1
                    if turn_record["task_id"]:
                        task_completion_counter[turn_record["task_id"]] += 1
                if turn_record["reward_applied"]:
                    reward_counter[str(turn_record["reward_applied"])] += 1
                for action in turn_record["chosen_actions"]:
                    action_counter[action] += 1
            for turn_log in result["turn_logs"]:
                sampled_logs.append(
                    {
                        "mode": mode.name,
                        "team": team_label(team),
                        "strategy_id": strategy_id,
                        "strategy_name": STRATEGIES[strategy_id].name,
                        "game_index": game_index,
                        **turn_log,
                    }
                )

        games = games_per_team
        summary_rows.append(
            {
                "mode": mode.name,
                "team": team_label(team),
                "strategy_id": strategy_id,
                "strategy_name": STRATEGIES[strategy_id].name,
                "games": games,
                "win_rate": round(wins / games, 4),
                "excellent_rate": round(excellent_wins / games, 4),
                "avg_progress": round(progress_total / games, 3),
                "avg_safety": round(safety_total / games, 3),
                "avg_upgrade": round(upgrade_total / games, 3),
                "avg_hazards": round(hazards_total / games, 3),
                "avg_turns": round(turns_total / games, 3),
                "avg_redraws_used": round(redraw_total / games, 3),
                "avg_tasks_completed": round(task_completed_total / games, 3),
                "loss_major_accident": loss_reasons["major_accident"],
                "loss_hazard_pressure": loss_reasons["hazard_pressure"],
                "loss_hazard_overflow": loss_reasons["hazard_overflow"],
                "loss_safety_zero": loss_reasons["safety_zero"],
                "loss_upgrade_limit": loss_reasons["upgrade_limit"],
                "loss_progress_shortfall": loss_reasons["progress_shortfall"],
                "reward_clear_hazard": reward_counter["clear_hazard"],
                "reward_recover_safety": reward_counter["recover_safety"],
                "reward_reduce_upgrade": reward_counter["reduce_upgrade"],
                "reward_gain_redraw": reward_counter["gain_redraw"],
            }
        )

        total_action_picks = sum(action_counter.values()) or 1
        for action_id in ACTIONS:
            picks = action_counter[action_id]
            action_rows.append(
                {
                    "mode": mode.name,
                    "team": team_label(team),
                    "strategy_id": strategy_id,
                    "strategy_name": STRATEGIES[strategy_id].name,
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
                    "strategy_id": strategy_id,
                    "strategy_name": STRATEGIES[strategy_id].name,
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

        for task in TASKS:
            appearances = task_counter[task.task_id]
            completions = task_completion_counter[task.task_id]
            denominator = appearances or 1
            task_rows.append(
                {
                    "mode": mode.name,
                    "team": team_label(team),
                    "strategy_id": strategy_id,
                    "strategy_name": STRATEGIES[strategy_id].name,
                    "task_id": task.task_id,
                    "task_name": task.name,
                    "appearances": appearances,
                    "completions": completions,
                    "completion_rate": round(completions / denominator, 4),
                    "reward": task.reward,
                }
            )

    return {
        "summary_rows": summary_rows,
        "action_rows": action_rows,
        "event_rows": event_rows,
        "task_rows": task_rows,
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
    standard_rows = [row for row in sim_result["summary_rows"] if row["mode"] == "standard" and row["strategy_id"] == "none"]
    best_standard = max(standard_rows, key=lambda row: row["win_rate"])
    weakest_standard = min(standard_rows, key=lambda row: row["win_rate"])
    balanced_standard = next(row for row in standard_rows if row["team"] == "balanced+balanced")
    strategy_rows = [
        row for row in sim_result["summary_rows"]
        if row["mode"] == "standard" and row["team"] == "balanced+balanced" and row["strategy_id"] != "none"
    ]
    strategy_rows.sort(key=lambda row: row["win_rate"], reverse=True)
    return {
        "run_id": run_id,
        "seed": sim_result["seed"],
        "games_per_team": sim_result["games_per_team"],
        "scenarios_tested": len(sim_result["summary_rows"]),
        "best_standard_team": best_standard,
        "weakest_standard_team": weakest_standard,
        "balanced_standard_team": balanced_standard,
        "balanced_strategy_rows": strategy_rows,
    }


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Run balance simulations for boardgame v0.5")
    parser.add_argument("--games-per-team", type=int, default=2000)
    parser.add_argument("--seed", type=int, default=20260408)
    parser.add_argument("--run-id", type=str, default="run_001")
    parser.add_argument(
        "--output-root",
        type=Path,
        default=Path(r"C:\PKU\Term2\实验室安全作品大赛\data\v0.5"),
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
    write_csv(output_dir / "task_stats.csv", sim_result["task_rows"])
    write_csv(output_dir / "game_results.csv", sim_result["game_rows"])

    with (output_dir / "sample_turn_logs.jsonl").open("w", encoding="utf-8") as handle:
        for row in sim_result["sampled_logs"]:
            handle.write(json.dumps(row, ensure_ascii=False) + "\n")

    summary_payload = build_summary_payload(sim_result, args.run_id)
    write_json(output_dir / "summary.json", summary_payload)

    print(json.dumps(summary_payload, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
