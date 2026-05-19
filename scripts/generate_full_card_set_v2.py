from __future__ import annotations

import argparse
import json
import math
import shutil
from datetime import datetime
from pathlib import Path
from typing import Any

from PIL import Image, ImageDraw, ImageFont


ROOT = Path(__file__).resolve().parents[1]
CARDS_PATH = ROOT / "content" / "v2_cards.json"
OUTPUT_ROOT = ROOT / "card" / "final" / "v2"
DEFAULT_GENERATED_IMAGE_DIR = (
    Path.home() / ".codex" / "generated_images" / "019d6bca-ac42-7e91-b747-095a694caf7a"
)

CARD_W = 750
CARD_H = 1050
CARD_RADIUS = 34
CARD_MARGIN = 24
INNER_X = 54
INNER_W = CARD_W - INNER_X * 2

TYPE_ORDER = ["event", "task", "action", "role", "post", "strategy", "debrief"]
TYPE_FOLDERS = {
    "event": "events",
    "task": "tasks",
    "action": "actions",
    "role": "roles",
    "post": "posts",
    "strategy": "strategies",
    "debrief": "debriefs",
}
TYPE_LABELS = {
    "event": "事件",
    "task": "任务",
    "action": "行动",
    "role": "角色",
    "post": "岗位",
    "strategy": "策略",
    "debrief": "复盘",
}

SAMPLE_INDEX_MAP = {
    "E02": 4,
    "E05": 6,
    "E15": 7,
    "T03": 8,
    "A01": 9,
    "A08": 10,
    "P01": 11,
    "R02": 12,
}

TAG_LABELS = {
    "any": "通用",
    "balance": "配平",
    "clean": "清洁",
    "communicate": "沟通",
    "contain": "围堵",
    "contamination": "污染",
    "cool": "降温",
    "corrosive": "腐蚀",
    "cut": "锐器",
    "emergency": "应急",
    "equipment": "设备",
    "evacuate": "撤离",
    "exposure": "暴露",
    "fire": "火源",
    "gas": "气瓶",
    "glass": "玻璃",
    "guard": "警戒",
    "heat": "热源",
    "hood": "通风橱",
    "imbalance": "不平衡",
    "inspect": "检查",
    "isolate": "隔离",
    "label": "标签",
    "mixing": "混放",
    "monitor": "监测",
    "neutralize": "中和",
    "overlook": "忽视",
    "oxidizer": "氧化剂",
    "ppe": "PPE",
    "pressure": "压力",
    "record": "记录",
    "replace": "更换",
    "residue": "残留",
    "resource": "资源",
    "review": "复盘",
    "secure": "固定",
    "shutdown": "切断",
    "solvent": "溶剂",
    "spill": "泄漏",
    "splash": "飞溅",
    "stop": "暂停",
    "storage": "储存",
    "unknown": "未知物",
    "ventilation": "通风",
    "verify": "核对",
    "waste": "废液",
    "water": "水路",
}
POST_LABELS = {
    "safety_officer": "安全员",
    "operator": "操作者",
    "recorder": "记录员",
    "resource_manager": "资源管理员",
}
STAGE_LABELS = {
    "prepare": "准备",
    "operate": "操作",
    "close": "收尾",
    "emergency": "应急",
    "setup": "开局",
    "round": "轮值",
    "debrief": "复盘",
    "any": "通用",
}
REWARD_LABELS = {
    "draw": "补充行动资源",
    "clear_hazard": "清除隐患",
    "reduce_accident": "降低事故压力",
    "progress_boost": "加速推进",
    "recover_safety": "恢复安全值",
}
STRENGTH_LABELS = {
    "basic": "基础",
    "strong": "强力",
    "emergency": "应急",
}

THEMES = {
    "blue": {
        "accent": "#3F7EDB",
        "accent_dark": "#2359A6",
        "accent_soft": "#DDEAFF",
        "bg": "#F6FAFF",
        "panel": "#EEF5FF",
    },
    "orange": {
        "accent": "#EE9A3A",
        "accent_dark": "#B76418",
        "accent_soft": "#FFE5C7",
        "bg": "#FFF9F1",
        "panel": "#FFF1DF",
    },
    "red": {
        "accent": "#D95454",
        "accent_dark": "#A93434",
        "accent_soft": "#FFD8D8",
        "bg": "#FFF7F7",
        "panel": "#FFF0F0",
    },
    "green": {
        "accent": "#49A66A",
        "accent_dark": "#2E7447",
        "accent_soft": "#DDF4E6",
        "bg": "#F7FCF9",
        "panel": "#EDF9F1",
    },
    "teal": {
        "accent": "#3AA6A6",
        "accent_dark": "#247273",
        "accent_soft": "#D9F3F2",
        "bg": "#F5FCFC",
        "panel": "#E9F8F7",
    },
    "purple": {
        "accent": "#7E66D8",
        "accent_dark": "#5541A6",
        "accent_soft": "#E6E0FF",
        "bg": "#F9F7FF",
        "panel": "#F0ECFF",
    },
    "gray": {
        "accent": "#6F7D8C",
        "accent_dark": "#465260",
        "accent_soft": "#E6EBF1",
        "bg": "#F8FAFC",
        "panel": "#EFF3F7",
    },
}

REQUIRED_FIELDS = {
    "event": ["id", "card_type", "name", "summary", "severity", "key_actions", "support_actions", "conflict_actions"],
    "task": ["id", "card_type", "name", "summary", "stage", "preferred_actions", "reward", "knowledge"],
    "action": ["id", "card_type", "name", "summary", "action_tags", "post_bonus", "limits"],
    "role": ["id", "card_type", "name", "summary", "ability_timing", "ability", "preferred_posts", "risk"],
    "post": ["id", "card_type", "name", "summary", "responsibility", "bonus_condition", "contribution_rule"],
    "strategy": ["id", "card_type", "name", "summary", "effect", "cost", "playstyle"],
    "debrief": ["id", "card_type", "name", "summary", "knowledge_point", "correct_action", "why", "review_question"],
}


def load_cards() -> list[dict[str, Any]]:
    data = json.loads(CARDS_PATH.read_text(encoding="utf-8"))
    return data["cards"]


def load_font(size: int, bold: bool = False) -> ImageFont.FreeTypeFont:
    candidates = [
        r"C:\Windows\Fonts\msyhbd.ttc" if bold else r"C:\Windows\Fonts\msyh.ttc",
        r"C:\Windows\Fonts\simhei.ttf",
        r"C:\Windows\Fonts\simsun.ttc",
    ]
    for path in candidates:
        try:
            return ImageFont.truetype(path, size=size)
        except OSError:
            continue
    return ImageFont.load_default()


def text_size(draw: ImageDraw.ImageDraw, text: str, font: ImageFont.ImageFont) -> tuple[int, int]:
    box = draw.textbbox((0, 0), text, font=font)
    return box[2] - box[0], box[3] - box[1]


def wrap_text(draw: ImageDraw.ImageDraw, text: str, font: ImageFont.ImageFont, max_width: int) -> list[str]:
    text = str(text or "").replace("\n", " ").strip()
    if not text:
        return []
    lines: list[str] = []
    current = ""
    for ch in text:
        candidate = current + ch
        if text_size(draw, candidate, font)[0] <= max_width:
            current = candidate
        else:
            if current:
                lines.append(current)
            current = ch
    if current:
        lines.append(current)
    return lines


def fit_lines(
    draw: ImageDraw.ImageDraw,
    text: str,
    max_width: int,
    max_height: int,
    start_size: int,
    min_size: int,
    bold: bool = False,
    max_lines: int | None = None,
) -> tuple[ImageFont.ImageFont, list[str], int]:
    for size in range(start_size, min_size - 1, -1):
        font = load_font(size, bold=bold)
        line_gap = max(4, int(size * 0.22))
        lines = wrap_text(draw, text, font, max_width)
        if max_lines is not None and len(lines) > max_lines:
            lines = lines[:max_lines]
            if lines:
                lines[-1] = truncate_to_width(draw, lines[-1] + "…", font, max_width)
        total_h = len(lines) * (size + line_gap)
        if total_h <= max_height:
            return font, lines, line_gap
    font = load_font(min_size, bold=bold)
    line_gap = max(4, int(min_size * 0.22))
    lines = wrap_text(draw, text, font, max_width)
    max_fit = max(1, max_height // (min_size + line_gap))
    if max_lines is not None:
        max_fit = min(max_fit, max_lines)
    lines = lines[:max_fit]
    if lines:
        lines[-1] = truncate_to_width(draw, lines[-1] + "…", font, max_width)
    return font, lines, line_gap


def truncate_to_width(draw: ImageDraw.ImageDraw, text: str, font: ImageFont.ImageFont, max_width: int) -> str:
    while text and text_size(draw, text, font)[0] > max_width:
        text = text[:-2] + "…"
    return text


def draw_centered_text(
    draw: ImageDraw.ImageDraw,
    xy: tuple[int, int, int, int],
    text: str,
    size: int,
    fill: str,
    bold: bool = False,
) -> None:
    x1, y1, x2, y2 = xy
    font = load_font(size, bold=bold)
    w, h = text_size(draw, text, font)
    draw.text((x1 + (x2 - x1 - w) / 2, y1 + (y2 - y1 - h) / 2 - 2), text, font=font, fill=fill)


def draw_wrapped(
    draw: ImageDraw.ImageDraw,
    xy: tuple[int, int, int, int],
    text: str,
    size: int,
    fill: str,
    bold: bool = False,
    min_size: int = 18,
    max_lines: int | None = None,
) -> None:
    x1, y1, x2, y2 = xy
    font, lines, gap = fit_lines(draw, text, x2 - x1, y2 - y1, size, min_size, bold=bold, max_lines=max_lines)
    cursor = y1
    font_size = getattr(font, "size", size)
    for line in lines:
        draw.text((x1, cursor), line, font=font, fill=fill)
        cursor += font_size + gap


def pills_text(items: list[str] | tuple[str, ...] | str | None, label_map: dict[str, str] | None = None) -> str:
    if items is None:
        return "无"
    if isinstance(items, str):
        values = [items]
    else:
        values = list(items)
    label_map = label_map or TAG_LABELS
    return " / ".join(label_map.get(item, item) for item in values) if values else "无"


def card_sort_key(card: dict[str, Any]) -> tuple[int, int, str]:
    card_id = card["id"]
    prefix = "".join(ch for ch in card_id if ch.isalpha())
    num = "".join(ch for ch in card_id if ch.isdigit())
    return TYPE_ORDER.index(card["card_type"]), int(num or 0), prefix


def theme_for(card: dict[str, Any]) -> tuple[str, dict[str, str], str]:
    ctype = card["card_type"]
    if ctype == "event":
        severity = card.get("severity", "low")
        if severity == "high":
            return "高危", THEMES["red"], "高危"
        if severity == "medium":
            return "中危", THEMES["orange"], "中危"
        return "低危", THEMES["blue"], "低危"
    if ctype == "task":
        stage = card.get("stage", card.get("phase", "task"))
        color = {"prepare": "blue", "operate": "purple", "close": "green", "emergency": "red"}.get(stage, "blue")
        return STAGE_LABELS.get(stage, "任务"), THEMES[color], "任务"
    if ctype == "action":
        strength = card.get("strength", "basic")
        color = {"basic": "blue", "strong": "orange", "emergency": "red"}.get(strength, "blue")
        return STRENGTH_LABELS.get(strength, "行动"), THEMES[color], "行动"
    if ctype == "role":
        return "角色", THEMES["purple"], "角色"
    if ctype == "post":
        return "岗位", THEMES["teal"], "岗位"
    if ctype == "strategy":
        return "策略", THEMES["purple"], "策略"
    return "复盘", THEMES["gray"], "复盘"


def validation_report(cards: list[dict[str, Any]]) -> dict[str, Any]:
    issues = []
    for card in cards:
        required = REQUIRED_FIELDS.get(card.get("card_type"), [])
        missing = [field for field in required if field not in card or card[field] in (None, "", [])]
        if missing:
            issues.append({"id": card.get("id"), "card_type": card.get("card_type"), "missing": missing})
    return {"card_count": len(cards), "issues": issues}


def prepare_sample_illustrations(source_dir: Path) -> dict[str, str]:
    sample_dir = OUTPUT_ROOT / "illustrations" / "samples"
    sample_dir.mkdir(parents=True, exist_ok=True)
    mapping: dict[str, str] = {}
    files = sorted(source_dir.glob("*.png"), key=lambda path: path.stat().st_mtime) if source_dir.exists() else []
    for card_id, index in SAMPLE_INDEX_MAP.items():
        destination = sample_dir / f"{card_id}.png"
        if len(files) >= index:
            shutil.copy2(files[index - 1], destination)
        if destination.exists():
            mapping[card_id] = str(destination.relative_to(ROOT)).replace("\\", "/")
    return mapping


def cover_crop(image: Image.Image, size: tuple[int, int]) -> Image.Image:
    target_w, target_h = size
    src_w, src_h = image.size
    scale = max(target_w / src_w, target_h / src_h)
    new_size = (math.ceil(src_w * scale), math.ceil(src_h * scale))
    resized = image.resize(new_size, Image.Resampling.LANCZOS)
    left = (resized.width - target_w) // 2
    top = (resized.height - target_h) // 2
    return resized.crop((left, top, left + target_w, top + target_h))


def draw_placeholder_illustration(card: dict[str, Any], theme: dict[str, str], size: tuple[int, int]) -> Image.Image:
    w, h = size
    img = Image.new("RGB", size, theme["bg"])
    draw = ImageDraw.Draw(img)
    accent = theme["accent"]
    dark = theme["accent_dark"]
    soft = theme["accent_soft"]
    panel = theme["panel"]

    draw.rounded_rectangle((18, 18, w - 18, h - 18), radius=30, fill=panel)
    draw.ellipse((w - 145, 28, w - 25, 148), fill=soft)
    draw.ellipse((28, h - 145, 145, h - 28), fill=soft)
    draw.rounded_rectangle((80, h - 100, w - 80, h - 64), radius=18, fill="#D5DEE8")
    draw.rounded_rectangle((112, h - 72, 138, h - 28), radius=12, fill="#B5C2CF")
    draw.rounded_rectangle((w - 138, h - 72, w - 112, h - 28), radius=12, fill="#B5C2CF")

    ctype = card["card_type"]
    cx, cy = w // 2, h // 2 + 8
    if ctype in {"event", "debrief"}:
        draw.polygon([(cx, cy - 100), (cx - 105, cy + 82), (cx + 105, cy + 82)], fill="#FFF7DF", outline=dark)
        draw.line((cx, cy - 35, cx, cy + 25), fill=accent, width=12)
        draw.ellipse((cx - 7, cy + 45, cx + 7, cy + 59), fill=accent)
        draw_lab_flasks(draw, w, h, accent, dark)
    elif ctype == "task":
        draw.line((110, cy, w - 110, cy), fill="#A9B9CE", width=10)
        for x in [120, w // 2, w - 120]:
            draw.ellipse((x - 34, cy - 34, x + 34, cy + 34), fill="#FFFFFF", outline=dark, width=4)
        draw_lab_flasks(draw, w, h, accent, dark)
    elif ctype == "action":
        draw.rounded_rectangle((cx - 130, cy - 72, cx + 130, cy + 72), radius=46, fill="#FFFFFF", outline=dark, width=4)
        draw.line((cx - 70, cy, cx + 70, cy), fill=accent, width=18)
        draw.polygon([(cx + 82, cy), (cx + 42, cy - 34), (cx + 42, cy + 34)], fill=accent)
        draw_lab_flasks(draw, w, h, accent, dark)
    elif ctype in {"role", "post"}:
        draw.ellipse((cx - 46, cy - 120, cx + 46, cy - 28), fill="#F4C7A1", outline=dark, width=4)
        draw.rounded_rectangle((cx - 82, cy - 20, cx + 82, cy + 128), radius=36, fill="#FFFFFF", outline=dark, width=4)
        draw.line((cx - 38, cy + 20, cx + 38, cy + 20), fill=accent, width=8)
        draw.ellipse((cx + 98, cy - 48, cx + 168, cy + 22), fill=soft, outline=dark, width=3)
    elif ctype == "strategy":
        draw.line((125, cy + 65, w - 125, cy - 65), fill="#A9B9CE", width=12)
        for x, y in [(125, cy + 65), (cx, cy), (w - 125, cy - 65)]:
            draw.ellipse((x - 34, y - 34, x + 34, y + 34), fill="#FFFFFF", outline=dark, width=4)
            draw.ellipse((x - 15, y - 15, x + 15, y + 15), fill=accent)
    else:
        draw_lab_flasks(draw, w, h, accent, dark)
    return img


def draw_lab_flasks(draw: ImageDraw.ImageDraw, w: int, h: int, accent: str, dark: str) -> None:
    draw.rounded_rectangle((w // 2 - 34, h // 2 - 130, w // 2 + 34, h // 2 - 60), radius=16, fill="#D9F1FF", outline=dark, width=4)
    draw.polygon(
        [
            (w // 2 - 28, h // 2 - 60),
            (w // 2 - 82, h // 2 + 78),
            (w // 2 + 82, h // 2 + 78),
            (w // 2 + 28, h // 2 - 60),
        ],
        fill="#EAF8FF",
        outline=dark,
    )
    draw.arc((w // 2 - 58, h // 2 + 6, w // 2 + 58, h // 2 + 92), start=0, end=180, fill=accent, width=8)
    draw.rounded_rectangle((w // 2 - 115, h // 2 + 86, w // 2 + 115, h // 2 + 108), radius=10, fill=dark)


def draw_card_shell(draw: ImageDraw.ImageDraw, theme: dict[str, str], side_label: str, card: dict[str, Any]) -> None:
    draw.rounded_rectangle((30, 34, CARD_W - 20, CARD_H - 18), radius=CARD_RADIUS, fill="#C7D0DA")
    draw.rounded_rectangle((CARD_MARGIN, CARD_MARGIN, CARD_W - CARD_MARGIN, CARD_H - CARD_MARGIN), radius=CARD_RADIUS, fill="#FFFFFF", outline="#D5DEE8", width=2)
    draw.rounded_rectangle((CARD_MARGIN, CARD_MARGIN, CARD_W - CARD_MARGIN, 98), radius=CARD_RADIUS, fill=theme["accent"])
    draw.rectangle((CARD_MARGIN, 64, CARD_W - CARD_MARGIN, 98), fill=theme["accent"])
    draw.text((54, 43), card["id"], font=load_font(34, bold=True), fill="#FFFFFF")
    draw.text((CARD_W - 56 - text_size(draw, side_label, load_font(28, bold=True))[0], 47), side_label, font=load_font(28, bold=True), fill="#FFFFFF")


def draw_title(draw: ImageDraw.ImageDraw, card: dict[str, Any]) -> None:
    draw.rounded_rectangle((42, 110, CARD_W - 42, 180), radius=18, fill="#FFFFFF")
    draw_wrapped(draw, (64, 120, CARD_W - 64, 174), card["name"], 38, "#111827", bold=True, min_size=26, max_lines=2)


def draw_illustration(
    base: Image.Image,
    card: dict[str, Any],
    theme: dict[str, str],
    sample_mapping: dict[str, str],
    xy: tuple[int, int, int, int],
) -> None:
    x1, y1, x2, y2 = xy
    draw = ImageDraw.Draw(base)
    draw.rounded_rectangle((x1, y1, x2, y2), radius=24, fill=theme["panel"], outline="#D9E1EA", width=2)
    image_path = sample_mapping.get(card["id"])
    if image_path:
        image = Image.open(ROOT / image_path).convert("RGB")
        art = cover_crop(image, (x2 - x1, y2 - y1))
    else:
        art = draw_placeholder_illustration(card, theme, (x2 - x1, y2 - y1))
    mask = Image.new("L", (x2 - x1, y2 - y1), 0)
    mask_draw = ImageDraw.Draw(mask)
    mask_draw.rounded_rectangle((0, 0, x2 - x1, y2 - y1), radius=24, fill=255)
    base.paste(art, (x1, y1), mask)


def draw_module(
    draw: ImageDraw.ImageDraw,
    xy: tuple[int, int, int, int],
    title: str,
    body: str,
    theme: dict[str, str],
    body_size: int = 22,
) -> None:
    x1, y1, x2, y2 = xy
    draw.rounded_rectangle((x1, y1, x2, y2), radius=18, fill=theme["panel"], outline="#D9E1EA", width=1)
    draw.ellipse((x1 + 16, y1 + 15, x1 + 43, y1 + 42), fill=theme["accent"])
    draw.text((x1 + 52, y1 + 13), title, font=load_font(23, bold=True), fill="#111827")
    draw_wrapped(draw, (x1 + 18, y1 + 52, x2 - 18, y2 - 14), body, body_size, "#222B35", min_size=17, max_lines=4)


def draw_modules_grid(
    draw: ImageDraw.ImageDraw,
    modules: list[tuple[str, str]],
    theme: dict[str, str],
    top: int,
    bottom: int,
    columns: int,
) -> None:
    gap = 18
    rows = math.ceil(len(modules) / columns)
    module_w = (INNER_W - gap * (columns - 1)) // columns
    module_h = (bottom - top - gap * (rows - 1)) // rows
    for idx, (title, body) in enumerate(modules):
        row = idx // columns
        col = idx % columns
        x1 = INNER_X + col * (module_w + gap)
        y1 = top + row * (module_h + gap)
        draw_module(draw, (x1, y1, x1 + module_w, y1 + module_h), title, body, theme)


def front_modules(card: dict[str, Any]) -> list[tuple[str, str]]:
    ctype = card["card_type"]
    if ctype == "event":
        return [("风险摘要", card["summary"]), ("关键行动", pills_text(card.get("key_actions")))]
    if ctype == "task":
        return [("任务目标", card["summary"]), ("推荐行动", pills_text(card.get("preferred_actions")))]
    if ctype == "action":
        return [("用途", card["summary"]), ("行动强度", STRENGTH_LABELS.get(card.get("strength"), card.get("strength", "行动")))]
    if ctype == "role":
        return [("角色定位", card["summary"]), ("适配岗位", pills_text(card.get("preferred_posts"), POST_LABELS))]
    if ctype == "post":
        return [("岗位职责", card["responsibility"]), ("奖励条件", card["bonus_condition"])]
    if ctype == "strategy":
        return [("路线导语", card["summary"]), ("适合打法", card["playstyle"])]
    return [("知识主题", card["knowledge_point"]), ("风险摘要", card["summary"])]


def back_modules(card: dict[str, Any], by_id: dict[str, dict[str, Any]]) -> list[tuple[str, str]]:
    ctype = card["card_type"]
    if ctype == "event":
        debrief = by_id.get(card.get("debrief_id", ""), {})
        return [
            ("正确处置", debrief.get("correct_action", "先控制风险，再推进任务。")),
            ("错误倾向", pills_text(card.get("conflict_actions"))),
            ("知识点", card.get("knowledge", debrief.get("knowledge_point", ""))),
            ("复盘问题", debrief.get("review_question", "本轮风险以后如何避免？")),
        ]
    if ctype == "task":
        return [
            ("完成奖励", REWARD_LABELS.get(card.get("reward"), card.get("reward", "奖励"))),
            ("风险标签", pills_text(card.get("risk_tags"))),
            ("推荐行动", pills_text(card.get("preferred_actions"))),
            ("教学知识点", card.get("knowledge", "")),
        ]
    if ctype == "action":
        return [
            ("行动标签", pills_text(card.get("action_tags"))),
            ("适用岗位", pills_text(card.get("post_bonus"), POST_LABELS)),
            ("限制边界", card.get("limits", "")),
            ("协作建议", "先判断事件风险源，再决定是否配合其他行动。"),
        ]
    if ctype == "role":
        return [
            ("能力", card.get("ability", "")),
            ("使用节奏", card.get("ability_timing", "")),
            ("适配岗位", pills_text(card.get("preferred_posts"), POST_LABELS)),
            ("风险", card.get("risk", "")),
        ]
    if ctype == "post":
        return [
            ("职责", card.get("responsibility", "")),
            ("奖励条件", card.get("bonus_condition", "")),
            ("贡献规则", card.get("contribution_rule", "")),
            ("协作提示", "岗位不是限制；所有玩家仍可参与讨论。"),
        ]
    if ctype == "strategy":
        return [
            ("效果", card.get("effect", "")),
            ("代价", card.get("cost", "")),
            ("适合打法", card.get("playstyle", "")),
            ("使用建议", "开局选择后，全局按该路线调整决策重点。"),
        ]
    return [
        ("正确行动", card.get("correct_action", "")),
        ("原因", card.get("why", "")),
        ("复盘问题", card.get("review_question", "")),
        ("关联标签", pills_text(card.get("tags"))),
    ]


def render_front(card: dict[str, Any], sample_mapping: dict[str, str]) -> Image.Image:
    side_label, theme, _ = theme_for(card)
    image = Image.new("RGB", (CARD_W, CARD_H), "#EDF2F7")
    draw = ImageDraw.Draw(image)
    draw_card_shell(draw, theme, side_label, card)
    draw_title(draw, card)
    draw_illustration(image, card, theme, sample_mapping, (54, 196, CARD_W - 54, 625))
    draw_modules_grid(draw, front_modules(card), theme, top=652, bottom=998, columns=2)
    return image


def render_back(card: dict[str, Any], by_id: dict[str, dict[str, Any]]) -> Image.Image:
    side_label, theme, _ = theme_for(card)
    image = Image.new("RGB", (CARD_W, CARD_H), "#EDF2F7")
    draw = ImageDraw.Draw(image)
    draw_card_shell(draw, theme, TYPE_LABELS.get(card["card_type"], side_label), card)
    heading = "知识与复盘" if card["card_type"] in {"event", "debrief"} else "规则与边界"
    draw_wrapped(draw, (64, 122, CARD_W - 64, 176), heading, 38, "#111827", bold=True, min_size=28, max_lines=1)
    placeholder = draw_placeholder_illustration(card, theme, (CARD_W - 108, 250))
    mask = Image.new("L", (CARD_W - 108, 250), 0)
    mask_draw = ImageDraw.Draw(mask)
    mask_draw.rounded_rectangle((0, 0, CARD_W - 108, 250), radius=24, fill=255)
    image.paste(placeholder, (54, 195), mask)
    draw_modules_grid(draw, back_modules(card, by_id), theme, top=470, bottom=998, columns=2)
    return image


def ensure_output_dirs() -> None:
    for folder in set(TYPE_FOLDERS.values()):
        (OUTPUT_ROOT / folder).mkdir(parents=True, exist_ok=True)
    (OUTPUT_ROOT / "preview").mkdir(parents=True, exist_ok=True)
    (OUTPUT_ROOT / "print").mkdir(parents=True, exist_ok=True)


def make_contact_sheet(paths: list[Path], output: Path, columns: int = 10, thumb_w: int = 150, thumb_h: int = 210) -> None:
    rows = math.ceil(len(paths) / columns)
    label_h = 28
    sheet = Image.new("RGB", (columns * thumb_w, rows * (thumb_h + label_h)), "#F4F6F8")
    draw = ImageDraw.Draw(sheet)
    font = load_font(16, bold=True)
    for idx, path in enumerate(paths):
        image = Image.open(path).convert("RGB")
        image.thumbnail((thumb_w, thumb_h), Image.Resampling.LANCZOS)
        col = idx % columns
        row = idx // columns
        x = col * thumb_w + (thumb_w - image.width) // 2
        y = row * (thumb_h + label_h)
        sheet.paste(image, (x, y))
        draw_centered_text(draw, (col * thumb_w, y + thumb_h, (col + 1) * thumb_w, y + thumb_h + label_h), path.stem.replace("_front", ""), 16, "#26313F", bold=True)
    sheet.save(output)


def write_preview_html(cards_meta: list[dict[str, Any]]) -> None:
    lines = [
        "<!doctype html>",
        '<html lang="zh-CN">',
        "<head>",
        '<meta charset="utf-8">',
        "<title>v2 卡牌预览</title>",
        "<style>",
        "body{font-family:Microsoft YaHei,Arial,sans-serif;background:#f3f6fa;margin:24px;color:#172033}",
        ".toolbar{position:sticky;top:0;background:#f3f6fa;padding:10px 0;z-index:2}",
        "button{margin:4px;padding:8px 14px;border:1px solid #ccd5df;border-radius:999px;background:#fff;cursor:pointer}",
        ".grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(180px,1fr));gap:20px}",
        ".card{background:#fff;border-radius:14px;padding:12px;box-shadow:0 6px 18px rgba(20,30,45,.12)}",
        ".pair{display:grid;grid-template-columns:1fr 1fr;gap:8px}",
        "img{width:100%;border-radius:10px;border:1px solid #d9e1ea}",
        ".meta{font-weight:700;margin-bottom:8px}",
        "</style>",
        "<script>",
        "function filterType(t){document.querySelectorAll('.card').forEach(c=>{c.style.display=(t==='all'||c.dataset.type===t)?'block':'none'})}",
        "</script>",
        "</head><body>",
        "<h1>《实验室安全值班》v2 卡牌预览</h1>",
        '<div class="toolbar"><button onclick="filterType(\'all\')">全部</button>',
    ]
    for ctype in TYPE_ORDER:
        lines.append(f"<button onclick=\"filterType('{ctype}')\">{TYPE_LABELS[ctype]}</button>")
    lines.append("</div><div class=\"grid\">")
    for meta in cards_meta:
        lines.append(
            f'<div class="card" data-type="{meta["card_type"]}">'
            f'<div class="meta">{meta["card_id"]} {meta["title"]}</div>'
            f'<div class="pair"><img src="../{meta["folder"]}/{meta["card_id"]}_front.png">'
            f'<img src="../{meta["folder"]}/{meta["card_id"]}_back.png"></div></div>'
        )
    lines.append("</div></body></html>")
    (OUTPUT_ROOT / "preview" / "index.html").write_text("\n".join(lines), encoding="utf-8")


def render_all(args: argparse.Namespace) -> None:
    ensure_output_dirs()
    cards = sorted(load_cards(), key=card_sort_key)
    by_id = {card["id"]: card for card in cards}
    report = validation_report(cards)
    sample_mapping = prepare_sample_illustrations(Path(args.generated_image_dir))

    cards_meta: list[dict[str, Any]] = []
    front_paths: list[Path] = []
    back_paths: list[Path] = []
    for card in cards:
        folder = TYPE_FOLDERS[card["card_type"]]
        out_dir = OUTPUT_ROOT / folder
        front_path = out_dir / f"{card['id']}_front.png"
        back_path = out_dir / f"{card['id']}_back.png"
        render_front(card, sample_mapping).save(front_path, dpi=(300, 300))
        render_back(card, by_id).save(back_path, dpi=(300, 300))
        front_paths.append(front_path)
        back_paths.append(back_path)
        cards_meta.append(
            {
                "card_id": card["id"],
                "card_type": card["card_type"],
                "title": card["name"],
                "folder": folder,
                "front_path": str(front_path.relative_to(ROOT)).replace("\\", "/"),
                "back_path": str(back_path.relative_to(ROOT)).replace("\\", "/"),
                "uses_sample_illustration": card["id"] in sample_mapping,
            }
        )

    make_contact_sheet(front_paths, OUTPUT_ROOT / "preview" / "contact_sheet.png", columns=10, thumb_w=150, thumb_h=210)
    make_contact_sheet(front_paths, OUTPUT_ROOT / "print" / "front_sheets.png", columns=8, thumb_w=225, thumb_h=315)
    make_contact_sheet(back_paths, OUTPUT_ROOT / "print" / "back_sheets.png", columns=8, thumb_w=225, thumb_h=315)
    write_preview_html(cards_meta)

    manifest = {
        "version": "v2",
        "generated_at": datetime.now().isoformat(timespec="seconds"),
        "card_count": len(cards_meta),
        "side_count": len(cards_meta) * 2,
        "sample_illustrations": sample_mapping,
        "type_counts": {ctype: sum(1 for card in cards if card["card_type"] == ctype) for ctype in TYPE_ORDER},
        "validation": report,
        "cards": cards_meta,
    }
    (OUTPUT_ROOT / "manifest.json").write_text(json.dumps(manifest, ensure_ascii=False, indent=2), encoding="utf-8")
    (OUTPUT_ROOT / "validation_report.json").write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps({"card_count": len(cards_meta), "side_count": len(cards_meta) * 2, "issues": len(report["issues"])}, ensure_ascii=False, indent=2))


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Generate v2 full card layout set.")
    parser.add_argument("--generated-image-dir", default=str(DEFAULT_GENERATED_IMAGE_DIR))
    return parser.parse_args()


if __name__ == "__main__":
    render_all(parse_args())
