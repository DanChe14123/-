from __future__ import annotations

import json
import re
from dataclasses import dataclass
from pathlib import Path

from PIL import Image, ImageColor, ImageDraw, ImageFilter, ImageFont


ROOT = Path(__file__).resolve().parents[1]
CONTENT_FILE = ROOT / "content" / "all_cards_copy_spec_v0.8.md"
OUTPUT_ROOT = ROOT / "card" / "final" / "v0.8"
PREVIEW_ROOT = OUTPUT_ROOT / "preview"
PRINT_ROOT = OUTPUT_ROOT / "print"
MANIFEST_PATH = OUTPUT_ROOT / "manifest.json"

CARD_W = 1500
CARD_H = 2100
DPI = (300, 300)

TITLE_FONT_CANDIDATES = [
    r"C:\Windows\Fonts\Noto Sans SC Bold (TrueType).otf",
    r"C:\Windows\Fonts\msyhbd.ttc",
    r"C:\Windows\Fonts\simhei.ttf",
]
BODY_FONT_CANDIDATES = [
    r"C:\Windows\Fonts\Noto Sans SC Medium (TrueType).otf",
    r"C:\Windows\Fonts\msyh.ttc",
    r"C:\Windows\Fonts\simsun.ttc",
]

EVENT_SEVERITY = {
    "E01": "低危",
    "E02": "低危",
    "E03": "低危",
    "E04": "低危",
    "E05": "中危",
    "E06": "中危",
    "E07": "中危",
    "E08": "中危",
    "E09": "中危",
    "E10": "中危",
    "E11": "高危",
    "E12": "高危",
    "E13": "高危",
    "E14": "高危",
    "E15": "高危",
    "E16": "高危",
    "E17": "低危",
    "E18": "低危",
    "E19": "中危",
    "E20": "中危",
    "E21": "中危",
    "E22": "中危",
    "E23": "高危",
    "E24": "高危",
}

ROLE_ORDER = ["林澄", "周衡", "顾宁", "程砚"]

ROLE_STYLE = {
    "林澄": {
        "accent": "#5FA8F5",
        "accent_dark": "#2C6FB6",
        "shirt": "#88B7F7",
        "hair": "#242A35",
        "skin": "#F7D4BA",
    },
    "周衡": {
        "accent": "#3F6FB6",
        "accent_dark": "#21497E",
        "shirt": "#4F75B7",
        "hair": "#1E2430",
        "skin": "#F3C8A9",
    },
    "顾宁": {
        "accent": "#E77763",
        "accent_dark": "#AE4B39",
        "shirt": "#ECA08E",
        "hair": "#232733",
        "skin": "#F6CDB7",
    },
    "程砚": {
        "accent": "#6FA57F",
        "accent_dark": "#416B4D",
        "shirt": "#8BB69A",
        "hair": "#212731",
        "skin": "#EEC6A8",
    },
}

THEMES = {
    "低危": {
        "accent": "#4E83D9",
        "accent_light": "#79A8F2",
        "accent_dark": "#2B5FB3",
        "panel": "#EEF4FF",
        "soft": "#DCEBFF",
        "ink": "#1E2A39",
    },
    "中危": {
        "accent": "#F0A045",
        "accent_light": "#F7BC6D",
        "accent_dark": "#C6771A",
        "panel": "#FFF4E6",
        "soft": "#FFE3BF",
        "ink": "#332516",
    },
    "高危": {
        "accent": "#D85A57",
        "accent_light": "#F08A86",
        "accent_dark": "#B53B39",
        "panel": "#FFF0EF",
        "soft": "#FFD9D8",
        "ink": "#381F1E",
    },
    "任务": {
        "accent": "#2D9A92",
        "accent_light": "#53C0B8",
        "accent_dark": "#1B6F68",
        "panel": "#ECFFFB",
        "soft": "#D7F5F1",
        "ink": "#1B2F2D",
    },
    "行动": {
        "accent": "#6B73E6",
        "accent_light": "#8D94F1",
        "accent_dark": "#4249B6",
        "panel": "#F0F2FF",
        "soft": "#E0E4FF",
        "ink": "#23284A",
    },
    "策略": {
        "accent": "#B88B2C",
        "accent_light": "#D4A94B",
        "accent_dark": "#8D6820",
        "panel": "#FFF7E7",
        "soft": "#F8E6BA",
        "ink": "#352916",
    },
}

TASK_TYPE_SHORT = {
    "常规实验": "常规",
    "易燃溶剂操作": "溶剂",
    "加热实验": "加热",
    "收尾操作": "收尾",
    "设备操作": "设备",
    "规范操作": "规范",
    "实验结束": "结束",
    "应急响应": "应急",
    "前处理": "前处理",
    "特殊工况": "特殊",
    "交接与收尾": "交接",
}

ROLE_TO_ID = {"林澄": "R01", "周衡": "R02", "顾宁": "R03", "程砚": "R04"}
SAMPLE_PRINT_IDS = ["E02", "E05", "T02", "A04", "R01", "S02"]


@dataclass
class CardRecord:
    card_id: str
    card_type: str
    heading: str
    fields: dict[str, str]


def ensure_dir(path: Path) -> None:
    path.mkdir(parents=True, exist_ok=True)


def load_font(size: int, *, bold: bool = False) -> ImageFont.FreeTypeFont:
    candidates = TITLE_FONT_CANDIDATES if bold else BODY_FONT_CANDIDATES
    for candidate in candidates:
        if Path(candidate).exists():
            return ImageFont.truetype(candidate, size=size)
    raise FileNotFoundError("No usable Chinese font found.")


def parse_cards() -> list[CardRecord]:
    section_map = {
        "## 2. 24 张事件牌": "event",
        "## 3. 12 张任务牌": "task",
        "## 4. 12 张行动牌": "action",
        "## 5. 4 张角色牌": "role",
        "## 6. 4 张策略牌": "strategy",
    }
    current_type = None
    current_id = ""
    current_heading = ""
    current_fields: dict[str, str] = {}
    out: list[CardRecord] = []
    for raw in CONTENT_FILE.read_text(encoding="utf-8").splitlines():
        line = raw.rstrip()
        if line in section_map:
            current_type = section_map[line]
            continue
        if line.startswith("## ") and line not in section_map:
            current_type = None
            continue
        if current_type and line.startswith("### "):
            if current_id:
                out.append(CardRecord(current_id, saved_type, current_heading, current_fields))
            current_heading = line[4:].strip()
            current_id = current_heading.split()[0]
            saved_type = current_type
            current_fields = {}
            continue
        if current_id and line.startswith("- "):
            match = re.match(r"- ([^：]+)：(.*)", line)
            if match:
                current_fields[match.group(1).strip()] = match.group(2).strip()
    if current_id:
        out.append(CardRecord(current_id, saved_type, current_heading, current_fields))
    return out


def text_size(draw: ImageDraw.ImageDraw, text: str, font: ImageFont.FreeTypeFont) -> tuple[int, int]:
    box = draw.textbbox((0, 0), text, font=font)
    return box[2] - box[0], box[3] - box[1]


def wrap_text(draw: ImageDraw.ImageDraw, text: str, font: ImageFont.FreeTypeFont, max_width: int, max_lines: int | None = None) -> list[str]:
    if not text:
        return [""]
    lines: list[str] = []
    current = ""
    for ch in text:
        test = current + ch
        if text_size(draw, test, font)[0] <= max_width or not current:
            current = test
        else:
            lines.append(current)
            current = ch
    if current:
        lines.append(current)
    if max_lines and len(lines) > max_lines:
        merged = lines[: max_lines - 1]
        tail = "".join(lines[max_lines - 1 :])
        while tail and text_size(draw, tail + "…", font)[0] > max_width:
            tail = tail[:-1]
        merged.append((tail or "") + "…")
        return merged
    return lines


def fit_font(draw: ImageDraw.ImageDraw, text: str, max_width: int, start: int, min_size: int = 26, *, bold: bool = True) -> ImageFont.FreeTypeFont:
    size = start
    while size >= min_size:
        font = load_font(size, bold=bold)
        if text_size(draw, text, font)[0] <= max_width:
            return font
        size -= 2
    return load_font(min_size, bold=bold)


def draw_multiline(
    draw: ImageDraw.ImageDraw,
    xy: tuple[int, int],
    lines: list[str],
    font: ImageFont.FreeTypeFont,
    fill: str,
    line_gap: int = 8,
    *,
    center: bool = False,
) -> int:
    x, y = xy
    _, h = text_size(draw, "高", font)
    for line in lines:
        if center:
            w, _ = text_size(draw, line, font)
            draw.text((x - w / 2, y), line, font=font, fill=fill)
        else:
            draw.text((x, y), line, font=font, fill=fill)
        y += h + line_gap
    return y


def lighten(color: str, amount: float) -> str:
    r, g, b = ImageColor.getrgb(color)
    r = int(r + (255 - r) * amount)
    g = int(g + (255 - g) * amount)
    b = int(b + (255 - b) * amount)
    return f"#{r:02X}{g:02X}{b:02X}"


def darken(color: str, amount: float) -> str:
    r, g, b = ImageColor.getrgb(color)
    r = int(r * (1 - amount))
    g = int(g * (1 - amount))
    b = int(b * (1 - amount))
    return f"#{r:02X}{g:02X}{b:02X}"


def split_items(value: str) -> list[str]:
    value = value.replace("；", "、").replace("，", "、").replace(",", "、")
    return [part.strip() for part in value.split("、") if part.strip()]


def rounded_mask(size: tuple[int, int], radius: int) -> Image.Image:
    mask = Image.new("L", size, 0)
    draw = ImageDraw.Draw(mask)
    draw.rounded_rectangle((0, 0, size[0] - 1, size[1] - 1), radius=radius, fill=255)
    return mask


def add_shadow(base: Image.Image, mask: Image.Image, offset: tuple[int, int] = (0, 20), blur: int = 24, color: tuple[int, int, int, int] = (17, 24, 39, 52)) -> None:
    shadow = Image.new("RGBA", base.size, (0, 0, 0, 0))
    sx, sy = offset
    blur_mask = mask.filter(ImageFilter.GaussianBlur(blur))
    shadow.paste(color, (sx, sy), blur_mask)
    base.alpha_composite(shadow)


def paste_rounded(base: Image.Image, layer: Image.Image, xy: tuple[int, int], radius: int) -> None:
    mask = rounded_mask(layer.size, radius)
    temp = Image.new("RGBA", base.size, (0, 0, 0, 0))
    temp.paste(layer, xy, mask)
    base.alpha_composite(temp)


def vertical_gradient(size: tuple[int, int], top: str, bottom: str) -> Image.Image:
    width, height = size
    tr, tg, tb = ImageColor.getrgb(top)
    br, bg, bb = ImageColor.getrgb(bottom)
    img = Image.new("RGBA", size)
    px = img.load()
    for y in range(height):
        t = y / max(height - 1, 1)
        row = (
            int(tr + (br - tr) * t),
            int(tg + (bg - tg) * t),
            int(tb + (bb - tb) * t),
            255,
        )
        for x in range(width):
            px[x, y] = row
    return img


def draw_round_panel(
    base: Image.Image,
    box: tuple[int, int, int, int],
    fill: str,
    *,
    outline: str | None = None,
    width: int = 2,
    radius: int = 26,
) -> None:
    x0, y0, x1, y1 = box
    panel = Image.new("RGBA", (x1 - x0, y1 - y0), (0, 0, 0, 0))
    draw = ImageDraw.Draw(panel)
    draw.rounded_rectangle((0, 0, x1 - x0 - 1, y1 - y0 - 1), radius=radius, fill=fill, outline=outline, width=width)
    paste_rounded(base, panel, (x0, y0), radius)


def get_theme(card: CardRecord) -> dict[str, str]:
    if card.card_type == "event":
        return THEMES[EVENT_SEVERITY[card.card_id]]
    if card.card_type == "task":
        return THEMES["任务"]
    if card.card_type == "action":
        return THEMES["行动"]
    if card.card_type == "strategy":
        role = card.fields["主角"]
        return {
            **THEMES["策略"],
            "accent": ROLE_STYLE[role]["accent_dark"],
            "accent_light": ROLE_STYLE[role]["accent"],
            "accent_dark": darken(ROLE_STYLE[role]["accent_dark"], 0.15),
            "panel": lighten(ROLE_STYLE[role]["accent"], 0.84),
            "soft": lighten(ROLE_STYLE[role]["accent"], 0.72),
        }
    role = card.fields["主角"]
    return {
        "accent": ROLE_STYLE[role]["accent"],
        "accent_light": lighten(ROLE_STYLE[role]["accent"], 0.18),
        "accent_dark": ROLE_STYLE[role]["accent_dark"],
        "panel": "#F7FAFF",
        "soft": lighten(ROLE_STYLE[role]["accent"], 0.72),
        "ink": "#1E2A39",
    }


def top_right_label(card: CardRecord) -> str:
    if card.card_type == "event":
        return EVENT_SEVERITY[card.card_id]
    if card.card_type == "task":
        return TASK_TYPE_SHORT.get(card.fields.get("类型", ""), "任务")
    if card.card_type == "action":
        return "行动"
    if card.card_type == "role":
        return card.fields.get("正面标题", "角色")
    return "策略"


def build_base_card(theme: dict[str, str]) -> Image.Image:
    base = Image.new("RGBA", (CARD_W, CARD_H), (0, 0, 0, 0))
    card_size = (CARD_W - 80, CARD_H - 80)
    mask = rounded_mask(card_size, 56)
    full_mask = Image.new("L", (CARD_W, CARD_H), 0)
    full_mask.paste(mask, (40, 40))
    add_shadow(base, full_mask)
    card = Image.new("RGBA", card_size, "#FFFFFF")
    draw = ImageDraw.Draw(card)
    draw.rounded_rectangle((0, 0, card_size[0] - 1, card_size[1] - 1), radius=56, fill="#FFFFFF", outline="#D7DFE8", width=3)
    grad = vertical_gradient((card_size[0], 170), theme["accent"], theme["accent_light"])
    grad.putalpha(rounded_mask((card_size[0], 170), 56))
    card.alpha_composite(grad, (0, 0))
    card.alpha_composite(Image.new("RGBA", (card_size[0], 110), (*ImageColor.getrgb(theme["accent_dark"]), 24)), (0, 60))
    base.alpha_composite(card, (40, 40))
    return base


def draw_header(draw: ImageDraw.ImageDraw, card: CardRecord, theme: dict[str, str]) -> None:
    id_font = load_font(54, bold=True)
    tag_font = load_font(48, bold=True)
    draw.text((96, 84), card.card_id, font=id_font, fill="#FFFFFF")
    label = top_right_label(card)
    w, _ = text_size(draw, label, tag_font)
    draw.text((CARD_W - 96 - w, 88), label, font=tag_font, fill="#FFFFFF")


def draw_title_area(draw: ImageDraw.ImageDraw, title: str) -> None:
    font = fit_font(draw, title, 1180, 88, min_size=54, bold=True)
    lines = wrap_text(draw, title, font, 1180, max_lines=2)
    total_h = len(lines) * (text_size(draw, "高", font)[1] + 8) - 8
    start_y = 270 + max(0, (190 - total_h) // 2)
    draw_multiline(draw, (CARD_W // 2, start_y), lines, font, "#111827", 8, center=True)


def draw_chip(draw: ImageDraw.ImageDraw, box: tuple[int, int, int, int], text: str, fill: str, ink: str, font_size: int = 30) -> None:
    draw.rounded_rectangle(box, radius=(box[3] - box[1]) // 2, fill=fill)
    font = fit_font(draw, text, box[2] - box[0] - 30, font_size, min_size=20, bold=True)
    w, h = text_size(draw, text, font)
    draw.text((box[0] + (box[2] - box[0] - w) / 2, box[1] + (box[3] - box[1] - h) / 2 - 2), text, font=font, fill=ink)


def draw_eye_icon(draw: ImageDraw.ImageDraw, center: tuple[int, int], scale: float, color: str) -> None:
    x, y = center
    draw.ellipse((x - 32 * scale, y - 18 * scale, x + 32 * scale, y + 18 * scale), outline=color, width=max(3, int(5 * scale)))
    draw.ellipse((x - 10 * scale, y - 10 * scale, x + 10 * scale, y + 10 * scale), fill=color)


def draw_x_icon(draw: ImageDraw.ImageDraw, center: tuple[int, int], scale: float, color: str) -> None:
    x, y = center
    r = 26 * scale
    draw.ellipse((x - r, y - r, x + r, y + r), outline=color, width=max(3, int(5 * scale)))
    draw.line((x - 11 * scale, y - 11 * scale, x + 11 * scale, y + 11 * scale), fill=color, width=max(3, int(5 * scale)))
    draw.line((x + 11 * scale, y - 11 * scale, x - 11 * scale, y + 11 * scale), fill=color, width=max(3, int(5 * scale)))


def draw_check_icon(draw: ImageDraw.ImageDraw, center: tuple[int, int], scale: float, color: str) -> None:
    x, y = center
    r = 26 * scale
    draw.ellipse((x - r, y - r, x + r, y + r), outline=color, width=max(3, int(5 * scale)))
    draw.line((x - 11 * scale, y + 1 * scale, x - 1 * scale, y + 12 * scale), fill=color, width=max(3, int(5 * scale)))
    draw.line((x - 1 * scale, y + 12 * scale, x + 16 * scale, y - 10 * scale), fill=color, width=max(3, int(5 * scale)))


def draw_info_icon(draw: ImageDraw.ImageDraw, center: tuple[int, int], scale: float, color: str) -> None:
    x, y = center
    r = 26 * scale
    draw.ellipse((x - r, y - r, x + r, y + r), outline=color, width=max(3, int(5 * scale)))
    font = load_font(int(34 * scale), bold=True)
    w, h = text_size(draw, "!", font)
    draw.text((x - w / 2, y - h / 2 - 2), "!", font=font, fill=color)


def draw_bulb_icon(draw: ImageDraw.ImageDraw, center: tuple[int, int], scale: float, color: str) -> None:
    x, y = center
    draw.ellipse((x - 18 * scale, y - 26 * scale, x + 18 * scale, y + 10 * scale), outline=color, width=max(3, int(5 * scale)))
    draw.rectangle((x - 10 * scale, y + 5 * scale, x + 10 * scale, y + 18 * scale), outline=color, width=max(3, int(5 * scale)))
    draw.line((x - 10 * scale, y + 23 * scale, x + 10 * scale, y + 23 * scale), fill=color, width=max(3, int(5 * scale)))


def draw_question_icon(draw: ImageDraw.ImageDraw, center: tuple[int, int], scale: float, color: str) -> None:
    x, y = center
    r = 26 * scale
    draw.ellipse((x - r, y - r, x + r, y + r), outline=color, width=max(3, int(5 * scale)))
    font = load_font(int(30 * scale), bold=True)
    w, h = text_size(draw, "?", font)
    draw.text((x - w / 2, y - h / 2 - 2), "?", font=font, fill=color)


def draw_lab_backdrop(img: Image.Image, box: tuple[int, int, int, int], theme: dict[str, str]) -> None:
    x0, y0, x1, y1 = box
    panel = Image.new("RGBA", (x1 - x0, y1 - y0), "#F8FBFF")
    wall = vertical_gradient(panel.size, "#FFFFFF", lighten(theme["panel"], 0.18))
    panel.alpha_composite(wall)
    draw = ImageDraw.Draw(panel)
    w, h = panel.size

    draw.rounded_rectangle((46, 40, 286, 272), radius=30, fill="#FBFDFF", outline="#C7D6E6", width=4)
    draw.line((166, 40, 166, 272), fill="#D7E4F0", width=3)
    draw.line((46, 156, 286, 156), fill="#D7E4F0", width=3)

    draw.rounded_rectangle((w - 396, 78, w - 62, 316), radius=24, fill="#EEF3F9", outline="#B8C8DA", width=4)
    draw.line((w - 376, 154, w - 82, 154), fill="#C9D7E6", width=3)
    for i in range(3):
        bx = w - 344 + i * 96
        draw.ellipse((bx, 176, bx + 48, 242), outline="#A8BDD1", width=4)
        draw.rectangle((bx + 18, 242, bx + 30, 274), outline="#A8BDD1", width=4)

    draw.rounded_rectangle((w - 470, 338, w - 110, 366), radius=14, fill="#A7B7C9")
    for i in range(3):
        cx = w - 424 + i * 112
        draw_flask(draw, (cx, 312), 0.36, liquid=lighten(theme["accent"], 0.62))

    bench_top_y = h - 178
    bench_front_y = h - 114
    bench = vertical_gradient((w - 180, 86), "#7E94B0", "#637996")
    bench.putalpha(255)
    paste_rounded(panel, bench, (90, bench_top_y), 30)
    draw.rounded_rectangle((108, bench_front_y, w - 108, h - 54), radius=18, fill="#D5DEEA", outline="#9EB0C3", width=3)
    for xx in (164, 382, 600):
        draw.line((xx, bench_front_y + 10, xx, h - 64), fill="#AEBFD0", width=3)
    for xx in (132, 350, 568):
        draw.rounded_rectangle((xx, bench_front_y + 22, xx + 86, bench_front_y + 48), radius=10, fill="#BAC7D6")
    draw.ellipse((130, h - 154, w - 130, h - 104), fill=(40, 58, 84, 28))
    paste_rounded(img, panel, (x0, y0), 30)


def draw_limb(
    draw: ImageDraw.ImageDraw,
    points: list[tuple[float, float]],
    *,
    fill: str,
    outline: str,
    width: int,
) -> None:
    flat = [coord for point in points for coord in point]
    draw.line(flat, fill=outline, width=width + 8)
    draw.line(flat, fill=fill, width=width)
    for x, y in points[1:-1]:
        r = width * 0.18
        draw.ellipse((x - r, y - r, x + r, y + r), fill=fill)


def draw_hand(draw: ImageDraw.ImageDraw, center: tuple[float, float], *, fill: str, outline: str, size: int = 24) -> None:
    x, y = center
    draw.ellipse((x - size, y - size, x + size, y + size), fill=fill, outline=outline, width=3)
    draw.ellipse((x + size * 0.15, y - size * 0.25, x + size * 0.9, y + size * 0.35), fill=fill, outline=outline, width=3)


def draw_badge(draw: ImageDraw.ImageDraw, center: tuple[int, int], accent: str) -> None:
    x, y = center
    draw.rounded_rectangle((x - 28, y - 42, x + 28, y + 42), radius=10, fill="#FFFFFF", outline=accent, width=4)
    draw.ellipse((x - 14, y - 30, x + 14, y - 2), fill=accent)
    draw.rectangle((x - 18, y + 4, x + 18, y + 24), fill=lighten(accent, 0.52))


def draw_notebook(draw: ImageDraw.ImageDraw, box: tuple[int, int, int, int]) -> None:
    x0, y0, x1, y1 = box
    draw.rounded_rectangle(box, radius=12, fill="#B47A52", outline="#72472D", width=4)
    draw.line((x0 + 20, y0, x0 + 20, y1), fill="#72472D", width=3)
    for yy in range(y0 + 18, y1 - 16, 18):
        draw.line((x0 + 32, yy, x1 - 18, yy), fill="#EFD3BF", width=2)


def draw_clipboard(draw: ImageDraw.ImageDraw, box: tuple[int, int, int, int], accent: str) -> None:
    x0, y0, x1, y1 = box
    draw.rounded_rectangle(box, radius=16, fill="#FFFDF6", outline="#5A6877", width=4)
    draw.rounded_rectangle((x0 + 42, y0 - 10, x1 - 42, y0 + 18), radius=8, fill=accent, outline="#5A6877", width=3)
    for yy in range(y0 + 46, y1 - 20, 24):
        draw.line((x0 + 22, yy, x1 - 22, yy), fill="#C0CAD5", width=4)


def draw_bottle(draw: ImageDraw.ImageDraw, center: tuple[int, int], scale: float, *, liquid: str = "#A8D3F7", label_text: str | None = None, label_blur: bool = False, cap: str = "#557DBD") -> None:
    x, y = center
    w = 120 * scale
    h = 212 * scale
    neck_w = 54 * scale
    neck_h = 40 * scale
    draw.rounded_rectangle((x - neck_w / 2, y - h / 2, x + neck_w / 2, y - h / 2 + neck_h), radius=10, fill=cap, outline="#30445E", width=4)
    draw.rounded_rectangle((x - w / 2, y - h / 2 + neck_h - 4, x + w / 2, y + h / 2), radius=24, fill="#F8FCFF", outline="#30445E", width=4)
    draw.rectangle((x - w / 2 + 6, y + 10, x + w / 2 - 6, y + h / 2 - 6), fill=liquid)
    draw.rounded_rectangle((x - w / 2 + 14, y - 10, x + w / 2 - 14, y + 58), radius=12, fill="#FFF6E5", outline="#30445E", width=3)
    if label_blur:
        for i in range(4):
            yy = y + i * 14
            draw.line((x - 34, yy, x + 30, yy + (i % 2) * 2), fill="#A49B88", width=6)
    elif label_text:
        font = load_font(max(18, int(22 * scale)), bold=True)
        yy = y - 2
        for line in label_text.split("\n"):
            w2, h2 = text_size(draw, line, font)
            draw.text((x - w2 / 2, yy), line, font=font, fill="#3A2A1C")
            yy += h2 + 2


def draw_beaker(draw: ImageDraw.ImageDraw, box: tuple[int, int, int, int], liquid: str = "#A5D8F6") -> None:
    x0, y0, x1, y1 = box
    draw.line((x0 + 20, y0, x0, y1), fill="#30445E", width=4)
    draw.line((x1 - 20, y0, x1, y1), fill="#30445E", width=4)
    draw.line((x0, y1, x1, y1), fill="#30445E", width=4)
    draw.line((x0 + 18, y0, x1 - 18, y0), fill="#30445E", width=4)
    draw.polygon([(x0 + 8, y1 - 12), (x1 - 8, y1 - 12), (x1 - 18, y1 - 55), (x0 + 18, y1 - 58)], fill=liquid)


def draw_flask(draw: ImageDraw.ImageDraw, center: tuple[int, int], scale: float = 1.0, *, liquid: str = "#BDD8FF", cracked: bool = False) -> None:
    x, y = center
    pts = [
        (x - 40 * scale, y - 90 * scale),
        (x - 18 * scale, y - 90 * scale),
        (x - 8 * scale, y - 34 * scale),
        (x - 56 * scale, y + 56 * scale),
        (x + 56 * scale, y + 56 * scale),
        (x + 8 * scale, y - 34 * scale),
        (x + 18 * scale, y - 90 * scale),
        (x + 40 * scale, y - 90 * scale),
    ]
    draw.polygon(pts, fill="#F8FCFF", outline="#30445E")
    draw.polygon([(x - 40 * scale, y + 28 * scale), (x + 40 * scale, y + 28 * scale), (x + 24 * scale, y + 52 * scale), (x - 24 * scale, y + 52 * scale)], fill=liquid)
    if cracked:
        draw.line((x - 10 * scale, y - 10 * scale, x + 10 * scale, y + 12 * scale, x - 4 * scale, y + 34 * scale), fill="#D95A57", width=5)


def draw_warning_tape(draw: ImageDraw.ImageDraw, box: tuple[int, int, int, int]) -> None:
    x0, y0, x1, y1 = box
    draw.rounded_rectangle(box, radius=10, fill="#F7D84D", outline="#C8A11A", width=3)
    for xx in range(x0 + 8, x1, 26):
        draw.line((xx, y0 + 4, xx + 18, y1 - 4), fill="#2B2F35", width=5)


def draw_power_icon(draw: ImageDraw.ImageDraw, center: tuple[int, int], scale: float, color: str) -> None:
    x, y = center
    r = 42 * scale
    draw.arc((x - r, y - r, x + r, y + r), 40, 320, fill=color, width=max(4, int(8 * scale)))
    draw.line((x, y - r - 8 * scale, x, y - 10 * scale), fill=color, width=max(4, int(8 * scale)))


def draw_flame(draw: ImageDraw.ImageDraw, center: tuple[int, int], scale: float) -> None:
    x, y = center
    draw.polygon([(x, y - 76 * scale), (x + 52 * scale, y - 8 * scale), (x + 34 * scale, y + 54 * scale), (x, y + 82 * scale), (x - 40 * scale, y + 40 * scale), (x - 56 * scale, y - 6 * scale)], fill="#FF8B3C", outline="#D15A28")
    draw.polygon([(x, y - 38 * scale), (x + 26 * scale, y + 4 * scale), (x + 12 * scale, y + 48 * scale), (x - 8 * scale, y + 56 * scale), (x - 28 * scale, y + 14 * scale)], fill="#FFD56A", outline="#EBAF34")


def draw_cylinder(draw: ImageDraw.ImageDraw, box: tuple[int, int, int, int], *, secure: bool = False, frost: bool = False) -> None:
    x0, y0, x1, y1 = box
    draw.rounded_rectangle(box, radius=(x1 - x0) // 2, fill="#6AA68E", outline="#30445E", width=5)
    draw.rounded_rectangle((x0 + 28, y0 - 32, x1 - 28, y0 + 8), radius=10, fill="#4C6B9F", outline="#30445E", width=4)
    if secure:
        draw.line((x0 - 26, y0 + 96, x0 + 8, y0 + 96), fill="#607D9B", width=10)
        draw.line((x1 - 8, y0 + 96, x1 + 26, y0 + 96), fill="#607D9B", width=10)
    else:
        draw.line((x0 - 42, y0 + 96, x0 - 10, y0 + 122), fill="#D95A57", width=9)
        draw.line((x1 + 42, y0 + 96, x1 + 10, y0 + 122), fill="#D95A57", width=9)
    if frost:
        draw.ellipse((x1 - 28, y0 - 48, x1 + 34, y0 + 16), fill="#EAF6FF", outline="#A2CCE8", width=3)


def draw_fumehood(draw: ImageDraw.ImageDraw, box: tuple[int, int, int, int], *, sash_high: bool = False, cluttered: bool = False) -> None:
    x0, y0, x1, y1 = box
    draw.rounded_rectangle(box, radius=18, fill="#E9EEF5", outline="#5F7288", width=5)
    sash_y = y0 + 74 if sash_high else y0 + 126
    draw.rectangle((x0 + 36, sash_y, x1 - 36, y1 - 70), outline="#97A9BE", width=4, fill="#F8FBFF")
    draw.rectangle((x0 + 36, y0 + 38, x1 - 36, sash_y), fill="#CFD8E6", outline="#97A9BE", width=4)
    if cluttered:
        for i in range(3):
            draw_bottle(draw, (x0 + 110 + i * 92, y1 - 120), 0.45, liquid="#B4D7F8")
    else:
        draw.line((x0 + 76, y0 + 184, x0 + 232, y0 + 184), fill="#7AA5D8", width=8)
        draw.arc((x0 + 86, y0 + 132, x0 + 224, y0 + 234), 20, 160, fill="#7AA5D8", width=5)


def draw_rotavap(draw: ImageDraw.ImageDraw, box: tuple[int, int, int, int], *, loose: bool = False) -> None:
    x0, y0, x1, y1 = box
    draw.rounded_rectangle((x0 + 20, y1 - 70, x1 - 20, y1 - 20), radius=18, fill="#7287A4", outline="#4F637C", width=4)
    draw.rounded_rectangle((x0 + 60, y0 + 40, x0 + 180, y0 + 170), radius=26, fill="#DFE7F1", outline="#5A6E87", width=4)
    draw.ellipse((x0 + 92, y0 + 72, x0 + 148, y0 + 128), fill="#B9C8DB", outline="#5A6E87", width=4)
    draw.line((x0 + 200, y0 + 86, x0 + 320, y0 + 56), fill="#8298B3", width=10)
    draw.line((x0 + 320, y0 + 56, x0 + 410, y0 + 106), fill="#8298B3", width=10)
    if loose:
        draw.line((x0 + 286, y0 + 42, x0 + 320, y0 + 56), fill="#D95A57", width=8)
    draw.rounded_rectangle((x0 + 392, y0 + 100, x0 + 472, y0 + 232), radius=24, fill="#D8F2FF", outline="#5A6E87", width=4)


def draw_centrifuge(draw: ImageDraw.ImageDraw, box: tuple[int, int, int, int], *, shaky: bool = False) -> None:
    x0, y0, x1, y1 = box
    draw.rounded_rectangle(box, radius=28, fill="#E2E7F0", outline="#627389", width=5)
    draw.ellipse((x0 + 70, y0 + 30, x1 - 70, y0 + 140), fill="#CFD7E3", outline="#627389", width=4)
    if shaky:
        draw.line((x0 - 12, y0 + 80, x0 - 34, y0 + 58), fill="#D95A57", width=7)
        draw.line((x1 + 12, y0 + 80, x1 + 34, y0 + 58), fill="#D95A57", width=7)


def draw_sink(draw: ImageDraw.ImageDraw, box: tuple[int, int, int, int]) -> None:
    x0, y0, x1, y1 = box
    draw.rounded_rectangle((x0, y0 + 60, x1, y1), radius=18, fill="#DDE6F2", outline="#64788F", width=4)
    draw.arc((x0 + 40, y0, x0 + 120, y0 + 120), 180, 340, fill="#64788F", width=8)
    draw.line((x0 + 112, y0 + 34, x0 + 156, y0 + 34), fill="#64788F", width=8)
    for dx in [0, 34, 68]:
        draw.line((x0 + 126 + dx, y0 + 60, x0 + 112 + dx, y0 + 118), fill="#7CC8FF", width=4)


def draw_powder(draw: ImageDraw.ImageDraw, box: tuple[int, int, int, int]) -> None:
    x0, y0, x1, y1 = box
    draw.pieslice(box, 180, 360, fill="#E7DFC5", outline="#A99874", width=3)
    for px, py, r in [(x0 + 30, y0 + 20, 10), (x0 + 80, y0 + 36, 7), (x0 + 126, y0 + 26, 12)]:
        draw.ellipse((px - r, py - r, px + r, py + r), fill="#E7DFC5", outline="#A99874")


def paste_centered(base: Image.Image, layer: Image.Image, center: tuple[float, float]) -> None:
    x = int(center[0] - layer.width / 2)
    y = int(center[1] - layer.height / 2)
    base.alpha_composite(layer, (x, y))


def paste_rotated(base: Image.Image, layer: Image.Image, center: tuple[float, float], angle: float) -> None:
    rotated = layer.rotate(angle, resample=Image.Resampling.BICUBIC, expand=True)
    paste_centered(base, rotated, center)


def make_bottle_prop(scale: float, **kwargs: object) -> Image.Image:
    size = (int(220 * scale), int(320 * scale))
    layer = Image.new("RGBA", size, (0, 0, 0, 0))
    draw = ImageDraw.Draw(layer)
    draw_bottle(draw, (size[0] / 2, size[1] / 2 + 6), scale, **kwargs)
    return layer


def make_clipboard_prop(width: int, height: int, accent: str) -> Image.Image:
    layer = Image.new("RGBA", (width, height), (0, 0, 0, 0))
    draw = ImageDraw.Draw(layer)
    draw_clipboard(draw, (12, 18, width - 12, height - 12), accent)
    return layer


def make_notebook_prop(width: int, height: int) -> Image.Image:
    layer = Image.new("RGBA", (width, height), (0, 0, 0, 0))
    draw = ImageDraw.Draw(layer)
    draw_notebook(draw, (8, 10, width - 8, height - 8))
    return layer


def make_beaker_prop(width: int, height: int, liquid: str = "#A5D8F6") -> Image.Image:
    layer = Image.new("RGBA", (width, height), (0, 0, 0, 0))
    draw = ImageDraw.Draw(layer)
    draw_beaker(draw, (20, 16, width - 20, height - 12), liquid=liquid)
    return layer


def draw_role_character(
    img: Image.Image,
    box: tuple[int, int, int, int],
    role: str,
    *,
    pose: str = "neutral",
    coat: bool = True,
    gloves: bool = False,
    goggles: bool = False,
) -> dict[str, tuple[float, float]]:
    draw = ImageDraw.Draw(img)
    style = ROLE_STYLE[role]
    x0, y0, x1, y1 = box
    w = x1 - x0
    h = y1 - y0
    cx = x0 + w * 0.46
    head_cx = cx + w * 0.02
    head_cy = y0 + h * 0.20
    head_w = min(w, h) * 0.28
    head_h = head_w * 1.18
    outline = "#334155"
    shoulder_y = y0 + h * 0.46
    torso_bottom = y0 + h * 1.00
    shoulder_w = w * (0.44 if coat else 0.40)
    waist_w = shoulder_w * 0.80
    torso_left = cx - shoulder_w / 2
    torso_right = cx + shoulder_w / 2
    waist_left = cx - waist_w / 2
    waist_right = cx + waist_w / 2
    neck_w = head_w * 0.20
    neck_h = head_h * 0.15
    arm_fill = "#FFFFFF" if coat else style["shirt"]
    hand_fill = style["shirt"] if gloves else style["skin"]

    draw.ellipse((cx - shoulder_w * 0.52, y0 + h * 0.82, cx + shoulder_w * 0.56, y0 + h * 0.95), fill=(31, 41, 55, 24))

    face_box = (head_cx - head_w / 2, head_cy - head_h / 2, head_cx + head_w / 2, head_cy + head_h / 2)
    ear_offset = head_w * 0.42
    draw.ellipse((head_cx - ear_offset - 12, head_cy - 10, head_cx - ear_offset + 16, head_cy + 30), fill=style["skin"], outline=outline, width=3)
    draw.ellipse((head_cx + ear_offset - 16, head_cy - 10, head_cx + ear_offset + 12, head_cy + 30), fill=style["skin"], outline=outline, width=3)
    draw.ellipse(face_box, fill=style["skin"], outline=outline, width=4)
    draw.rounded_rectangle((head_cx - neck_w / 2, shoulder_y - neck_h - 10, head_cx + neck_w / 2, shoulder_y + 6), radius=8, fill=style["skin"], outline=outline, width=3)

    if role == "林澄":
        draw.pieslice((head_cx - head_w * 0.64, head_cy - head_h * 0.86, head_cx + head_w * 0.64, head_cy + head_h * 0.06), 180, 360, fill=style["hair"], outline=style["hair"])
        draw.polygon(
            [
                (head_cx - head_w * 0.50, head_cy + head_h * 0.00),
                (head_cx - head_w * 0.44, head_cy + head_h * 0.42),
                (head_cx - head_w * 0.28, head_cy + head_h * 0.50),
                (head_cx - head_w * 0.20, head_cy + head_h * 0.14),
            ],
            fill=style["hair"],
        )
        draw.polygon(
            [
                (head_cx + head_w * 0.50, head_cy + head_h * 0.00),
                (head_cx + head_w * 0.44, head_cy + head_h * 0.42),
                (head_cx + head_w * 0.28, head_cy + head_h * 0.50),
                (head_cx + head_w * 0.20, head_cy + head_h * 0.14),
            ],
            fill=style["hair"],
        )
        draw.polygon(
            [
                (head_cx - head_w * 0.24, head_cy - head_h * 0.04),
                (head_cx - head_w * 0.08, head_cy + head_h * 0.10),
                (head_cx, head_cy + head_h * 0.02),
                (head_cx + head_w * 0.10, head_cy + head_h * 0.10),
                (head_cx + head_w * 0.24, head_cy - head_h * 0.04),
            ],
            fill=style["hair"],
        )
    elif role == "顾宁":
        draw.pieslice((head_cx - head_w * 0.66, head_cy - head_h * 0.82, head_cx + head_w * 0.64, head_cy + head_h * 0.04), 180, 360, fill=style["hair"], outline=style["hair"])
        draw.polygon(
            [
                (head_cx - head_w * 0.52, head_cy + head_h * 0.00),
                (head_cx - head_w * 0.42, head_cy + head_h * 0.38),
                (head_cx - head_w * 0.22, head_cy + head_h * 0.38),
                (head_cx - head_w * 0.14, head_cy + head_h * 0.10),
            ],
            fill=style["hair"],
        )
        draw.polygon(
            [
                (head_cx + head_w * 0.48, head_cy - head_h * 0.02),
                (head_cx + head_w * 0.38, head_cy + head_h * 0.32),
                (head_cx + head_w * 0.20, head_cy + head_h * 0.32),
                (head_cx + head_w * 0.12, head_cy + head_h * 0.08),
            ],
            fill=style["hair"],
        )
        draw.polygon(
            [
                (head_cx + head_w * 0.46, head_cy + head_h * 0.10),
                (head_cx + head_w * 0.84, head_cy + head_h * 0.24),
                (head_cx + head_w * 0.66, head_cy + head_h * 0.70),
            ],
            fill=style["hair"],
        )
    elif role == "程砚":
        draw.pieslice((head_cx - head_w * 0.62, head_cy - head_h * 0.82, head_cx + head_w * 0.62, head_cy + head_h * 0.02), 180, 360, fill=style["hair"], outline=style["hair"])
        draw.polygon(
            [
                (head_cx - head_w * 0.48, head_cy - head_h * 0.02),
                (head_cx - head_w * 0.22, head_cy - head_h * 0.20),
                (head_cx - head_w * 0.02, head_cy - head_h * 0.02),
                (head_cx + head_w * 0.18, head_cy - head_h * 0.18),
                (head_cx + head_w * 0.42, head_cy - head_h * 0.02),
            ],
            fill=style["hair"],
        )
    else:
        draw.pieslice((head_cx - head_w * 0.64, head_cy - head_h * 0.82, head_cx + head_w * 0.62, head_cy + head_h * 0.02), 180, 360, fill=style["hair"], outline=style["hair"])
        draw.polygon(
            [
                (head_cx - head_w * 0.46, head_cy - head_h * 0.02),
                (head_cx - head_w * 0.20, head_cy - head_h * 0.18),
                (head_cx, head_cy + head_h * 0.00),
                (head_cx + head_w * 0.20, head_cy - head_h * 0.18),
                (head_cx + head_w * 0.44, head_cy - head_h * 0.02),
            ],
            fill=style["hair"],
        )

    eye_y = head_cy + head_h * 0.04
    eye_dx = head_w * 0.18
    for dx in (-eye_dx, eye_dx):
        draw.ellipse((head_cx + dx - 13, eye_y - 5, head_cx + dx + 13, eye_y + 10), fill="#1F2937")
        draw.ellipse((head_cx + dx - 3, eye_y - 1, head_cx + dx + 3, eye_y + 5), fill="#FFFFFF")
    brow_y = eye_y - 16
    draw.line((head_cx - head_w * 0.22, brow_y, head_cx - head_w * 0.10, brow_y - 1), fill="#495566", width=2)
    draw.line((head_cx + head_w * 0.10, brow_y - 1, head_cx + head_w * 0.22, brow_y), fill="#495566", width=2)
    draw.line((head_cx - 4, head_cy + head_h * 0.18, head_cx + 3, head_cy + head_h * 0.28), fill="#C89278", width=2)
    draw.arc((head_cx - 14, head_cy + head_h * 0.34, head_cx + 14, head_cy + head_h * 0.48), 28, 152, fill="#C66565", width=2)
    draw.ellipse((head_cx - head_w * 0.40, head_cy + head_h * 0.20, head_cx - head_w * 0.18, head_cy + head_h * 0.40), fill="#F7C0B8")
    draw.ellipse((head_cx + head_w * 0.18, head_cy + head_h * 0.20, head_cx + head_w * 0.40, head_cy + head_h * 0.40), fill="#F7C0B8")

    if goggles:
        draw.rounded_rectangle((head_cx - head_w * 0.44, eye_y - 22, head_cx + head_w * 0.44, eye_y + 26), radius=18, fill="#ECF8FF", outline=style["accent_dark"], width=4)
    if role == "程砚":
        draw.rounded_rectangle((head_cx - head_w * 0.40, eye_y - 18, head_cx + head_w * 0.40, eye_y + 18), radius=14, outline="#405164", width=4)
        draw.line((head_cx - 8, eye_y, head_cx + 8, eye_y), fill="#405164", width=3)

    torso_box = (cx - shoulder_w * 0.40, shoulder_y + 8, cx + shoulder_w * 0.40, torso_bottom + 20)
    draw.rounded_rectangle((torso_box[0] + 12, torso_box[1] + 20, torso_box[2] + 10, torso_box[3] + 12), radius=64, fill=(15, 23, 42, 18))
    if coat:
        draw.rounded_rectangle(torso_box, radius=62, fill="#FFFFFF", outline=outline, width=4)
        draw.rounded_rectangle((cx - shoulder_w * 0.11, shoulder_y + 28, cx + shoulder_w * 0.11, torso_bottom + 8), radius=24, fill=style["shirt"])
        draw.polygon(
            [
                (torso_box[0] + 38, shoulder_y + 20),
                (cx - 12, shoulder_y + 124),
                (cx - 2, torso_bottom - 46),
            ],
            fill="#EEF3F8",
            outline=outline,
        )
        draw.polygon(
            [
                (torso_box[2] - 38, shoulder_y + 24),
                (cx + 14, shoulder_y + 122),
                (cx + 4, torso_bottom - 44),
            ],
            fill="#EEF3F8",
            outline=outline,
        )
        pocket = (torso_box[2] - 88, shoulder_y + 176, torso_box[2] - 26, shoulder_y + 248)
        draw.rounded_rectangle(pocket, radius=8, outline=outline, width=3)
    else:
        draw.rounded_rectangle(torso_box, radius=58, fill=style["shirt"], outline=outline, width=4)
        draw.line((torso_box[0] + 56, shoulder_y + 34, torso_box[0] + 28, shoulder_y + 104), fill=darken(style["shirt"], 0.22), width=6)
        draw.line((torso_box[2] - 56, shoulder_y + 34, torso_box[2] - 28, shoulder_y + 104), fill=darken(style["shirt"], 0.22), width=6)

    draw.line((cx - 42, shoulder_y + 14, cx - 6, shoulder_y + 124), fill=style["accent_dark"], width=7)
    draw.line((cx + 42, shoulder_y + 14, cx + 6, shoulder_y + 124), fill=style["accent_dark"], width=7)
    draw_badge(draw, (int(cx), int(shoulder_y + 196)), style["accent_dark"])

    left_shoulder = (torso_box[0] + 40, shoulder_y + 60)
    right_shoulder = (torso_box[2] - 40, shoulder_y + 64)

    pose_map = {
        "inspect": {
            "left_elbow": (cx - shoulder_w * 0.46, shoulder_y + 170),
            "left_hand": (cx - shoulder_w * 0.24, shoulder_y + 244),
            "right_elbow": (cx + shoulder_w * 0.42, shoulder_y + 84),
            "right_hand": (cx + shoulder_w * 0.50, shoulder_y - 16),
        },
        "check": {
            "left_elbow": (cx - shoulder_w * 0.42, shoulder_y + 150),
            "left_hand": (cx - shoulder_w * 0.26, shoulder_y + 220),
            "right_elbow": (cx + shoulder_w * 0.30, shoulder_y + 140),
            "right_hand": (cx + shoulder_w * 0.34, shoulder_y + 220),
        },
        "write": {
            "left_elbow": (cx - shoulder_w * 0.32, shoulder_y + 158),
            "left_hand": (cx - shoulder_w * 0.10, shoulder_y + 222),
            "right_elbow": (cx + shoulder_w * 0.18, shoulder_y + 164),
            "right_hand": (cx + shoulder_w * 0.30, shoulder_y + 226),
        },
        "pour": {
            "left_elbow": (cx - shoulder_w * 0.20, shoulder_y + 130),
            "left_hand": (cx + shoulder_w * 0.08, shoulder_y + 160),
            "right_elbow": (cx + shoulder_w * 0.36, shoulder_y + 76),
            "right_hand": (cx + shoulder_w * 0.56, shoulder_y + 96),
        },
        "operate": {
            "left_elbow": (cx - shoulder_w * 0.08, shoulder_y + 138),
            "left_hand": (cx + shoulder_w * 0.18, shoulder_y + 160),
            "right_elbow": (cx + shoulder_w * 0.30, shoulder_y + 118),
            "right_hand": (cx + shoulder_w * 0.50, shoulder_y + 146),
        },
        "warn": {
            "left_elbow": (cx - shoulder_w * 0.42, shoulder_y + 134),
            "left_hand": (cx - shoulder_w * 0.58, shoulder_y + 204),
            "right_elbow": (cx + shoulder_w * 0.34, shoulder_y + 92),
            "right_hand": (cx + shoulder_w * 0.58, shoulder_y + 78),
        },
        "wash": {
            "left_elbow": (cx - shoulder_w * 0.10, shoulder_y + 140),
            "left_hand": (cx + shoulder_w * 0.10, shoulder_y + 200),
            "right_elbow": (cx + shoulder_w * 0.22, shoulder_y + 132),
            "right_hand": (cx + shoulder_w * 0.38, shoulder_y + 192),
        },
        "neutral": {
            "left_elbow": (cx - shoulder_w * 0.30, shoulder_y + 148),
            "left_hand": (cx - shoulder_w * 0.42, shoulder_y + 238),
            "right_elbow": (cx + shoulder_w * 0.28, shoulder_y + 144),
            "right_hand": (cx + shoulder_w * 0.40, shoulder_y + 234),
        },
    }
    arm_points = pose_map.get(pose, pose_map["neutral"])
    draw_limb(draw, [left_shoulder, arm_points["left_elbow"], arm_points["left_hand"]], fill=arm_fill, outline=outline, width=30)
    draw_limb(draw, [right_shoulder, arm_points["right_elbow"], arm_points["right_hand"]], fill=arm_fill, outline=outline, width=30)
    draw_hand(draw, arm_points["left_hand"], fill=hand_fill, outline=outline, size=21)
    draw_hand(draw, arm_points["right_hand"], fill=hand_fill, outline=outline, size=21)

    return {
        "head_center": (head_cx, head_cy),
        "left_hand": arm_points["left_hand"],
        "right_hand": arm_points["right_hand"],
        "chest_center": (cx, shoulder_y + 150),
        "bench_y": y0 + h * 0.80,
    }


def scene_box() -> tuple[int, int, int, int]:
    return (110, 490, CARD_W - 110, 1305)


def draw_event_scene(img: Image.Image, card: CardRecord, side: str, role: str, box: tuple[int, int, int, int], theme: dict[str, str]) -> None:
    draw = ImageDraw.Draw(img)
    x0, y0, x1, y1 = box
    char_box = (x0 + 8, y0 + 24, x0 + 812, y1 - 16)
    pose = "inspect"
    coat = True
    gloves = False
    goggles = False
    if card.card_id in {"E05", "E06", "E11", "E12", "E16", "E21"}:
        coat = False
        gloves = True
    if card.card_id == "E05" and side == "back":
        goggles = True
    if card.card_id in {"E13"} and side == "back":
        pose = "wash"
    elif card.card_id in {"E05", "E19", "E21"}:
        pose = "operate" if side == "back" else "pour"
    elif card.card_id in {"E17", "E18"}:
        pose = "write" if side == "back" else "check"
    elif card.card_id in {"E07", "E13", "E15", "E23", "E24"}:
        pose = "warn"
    elif card.card_id in {"E09", "E14", "E20"}:
        pose = "check"
    anchors = draw_role_character(img, char_box, role, pose=pose, coat=coat, gloves=gloves, goggles=goggles)

    cx = x0 + 836
    cy = y0 + 356
    cid = card.card_id
    if cid == "E01":
        draw_bottle(draw, (cx, cy + 60), 0.95, label_text="酸液")
        draw_round_panel(img, (x0 + 668, y0 + 126, x0 + 930, y0 + 226), "#FFFFFF", outline="#D8E0E8", width=3, radius=24)
        dd = ImageDraw.Draw(img)
        draw_eye_icon(dd, (x0 + 744, y0 + 176), 0.78, theme["accent_dark"])
        draw_x_icon(dd, (x0 + 856, y0 + 176), 0.78, "#D95A57")
    elif cid == "E02":
        if side == "front":
            bottle = make_bottle_prop(0.96, label_blur=True)
            notebook = make_notebook_prop(182, 136)
            paste_centered(img, bottle, (anchors["right_hand"][0] + 92, anchors["right_hand"][1] - 38))
            paste_rotated(img, notebook, (anchors["left_hand"][0] + 74, anchors["left_hand"][1] + 26), -8)
        else:
            bottle = make_bottle_prop(0.86, label_text="已核对\n标签")
            clipboard = make_clipboard_prop(188, 250, theme["accent"])
            paste_centered(img, bottle, (cx - 110, cy + 26))
            paste_rotated(img, clipboard, (cx + 34, cy + 136), -2)
            draw.line((anchors["right_hand"][0] + 14, anchors["right_hand"][1] + 12, cx - 42, cy + 12), fill=theme["accent_dark"], width=5)
    elif cid == "E03":
        for dx in (-130, 0, 130):
            draw_bottle(draw, (cx + dx, cy + 140), 0.6, liquid="#C5DCF9")
        draw_notebook(draw, (cx - 220, cy + 230, cx - 40, cy + 350))
        if side == "back":
            draw_warning_tape(draw, (cx - 190, cy + 20, cx + 130, cy + 68))
    elif cid == "E04":
        draw.rounded_rectangle((cx - 150, cy + 40, cx + 60, cy + 300), radius=34, fill="#DCE4EF", outline="#607389", width=5)
        draw.rectangle((cx - 118, cy + (22 if side == "front" else 70), cx + 28, cy + (60 if side == "front" else 98)), fill="#607389")
        if side == "front":
            draw_bottle(draw, (cx + 160, cy + 120), 0.55, liquid="#C9DDF5")
        else:
            draw_chip(draw, (cx + 72, cy + 168, cx + 268, cy + 230), "已封口", theme["soft"], theme["accent_dark"], 34)
    elif cid == "E05":
        if side == "front":
            bottle = make_bottle_prop(0.84, label_text="挥发\n溶剂")
            beaker = make_beaker_prop(156, 188)
            paste_rotated(img, bottle, (anchors["right_hand"][0] + 58, anchors["right_hand"][1] - 12), 28)
            paste_centered(img, beaker, (anchors["left_hand"][0] + 124, anchors["left_hand"][1] + 62))
            draw.line(
                (
                    anchors["right_hand"][0] + 78,
                    anchors["right_hand"][1] + 24,
                    anchors["left_hand"][0] + 126,
                    anchors["left_hand"][1] + 8,
                ),
                fill="#BDE4FF",
                width=8,
            )
            draw.line(
                (
                    anchors["right_hand"][0] + 78,
                    anchors["right_hand"][1] + 24,
                    anchors["left_hand"][0] + 126,
                    anchors["left_hand"][1] + 8,
                ),
                fill="#4FA9E5",
                width=3,
            )
        else:
            draw_fumehood(draw, (cx - 290, cy - 118, cx + 240, cy + 286))
            bottle = make_bottle_prop(0.74, label_text="转移\n至柜内")
            paste_centered(img, bottle, (cx - 48, cy + 46))
            draw.line((anchors["right_hand"][0] + 8, anchors["right_hand"][1], cx - 84, cy + 34), fill=theme["accent_dark"], width=5)
    elif cid == "E06":
        draw_bottle(draw, (cx - 90, cy + 30), 0.85, label_text="溶剂")
        draw_power_icon(draw, (cx + 130, cy + 115), 1.0, theme["accent_dark"] if side == "back" else "#D95A57")
        if side == "front":
            draw_flame(draw, (cx + 120, cy + 120), 0.7)
    elif cid == "E07":
        draw.rounded_rectangle((cx - 190, cy + 180, cx + 180, cy + 260), radius=40, fill="#AFD7F8", outline="#5D7EA5", width=5)
        if side == "back":
            draw_warning_tape(draw, (cx - 140, cy + 60, cx + 160, cy + 108))
    elif cid == "E08":
        draw_flask(draw, (cx, cy + 80), 1.3, cracked=(side == "front"))
        if side == "back":
            draw_chip(draw, (cx - 120, cy + 240, cx + 120, cy + 302), "更换器材", theme["soft"], theme["accent_dark"], 34)
    elif cid == "E09":
        draw_cylinder(draw, (cx - 90, cy - 90, cx + 60, cy + 250), secure=(side == "back"))
    elif cid == "E10":
        draw_fumehood(draw, (cx - 240, cy - 90, cx + 260, cy + 290), cluttered=(side == "front"))
        if side == "back":
            draw_chip(draw, (cx - 140, cy + 304, cx + 110, cy + 366), "恢复气流", theme["soft"], theme["accent_dark"], 34)
    elif cid == "E11":
        draw.rounded_rectangle((cx - 140, cy + 40, cx + 70, cy + 300), radius=34, fill="#DCE4EF", outline="#607389", width=5)
        draw.rectangle((cx - 120, cy + 22, cx + 40, cy + 60), fill="#607389")
        if side == "front":
            for i in range(3):
                draw.arc((cx - 80 + i * 10, cy - 30 - i * 20, cx + 60 + i * 10, cy + 80 - i * 20), 30, 150, fill="#B48C64", width=8)
        else:
            draw_warning_tape(draw, (cx - 210, cy + 70, cx + 160, cy + 118))
    elif cid == "E12":
        draw.rounded_rectangle((cx - 170, cy + 110, cx + 130, cy + 210), radius=20, fill="#D7DEE8", outline="#607389", width=4)
        draw_flask(draw, (cx - 30, cy + 10), 1.0)
        if side == "front":
            draw_flame(draw, (cx + 160, cy + 120), 0.45)
            draw.line((cx - 240, cy - 110, cx - 170, cy - 40), fill="#9FA8B5", width=10)
        else:
            draw_power_icon(draw, (cx + 170, cy + 120), 0.9, theme["accent_dark"])
    elif cid == "E13":
        draw_sink(draw, (cx - 210, cy + 60, cx + 100, cy + 310))
        if side == "front":
            draw_info_icon(draw, (cx + 170, cy + 120), 1.0, "#D95A57")
        else:
            draw_check_icon(draw, (cx + 170, cy + 120), 1.0, theme["accent_dark"])
    elif cid == "E14":
        draw_flask(draw, (cx, cy + 70), 1.15)
        if side == "front":
            draw.arc((cx - 170, cy - 50, cx + 170, cy + 190), 200, 340, fill="#D95A57", width=9)
        else:
            draw_power_icon(draw, (cx + 180, cy + 110), 0.95, theme["accent_dark"])
            draw_warning_tape(draw, (cx - 180, cy + 260, cx + 180, cy + 308))
    elif cid == "E15":
        draw_flame(draw, (cx, cy + 90), 1.0 if side == "front" else 0.7)
        if side == "back":
            draw_round_panel(img, (x0 + 770, y0 + 520, x0 + 1000, y0 + 650), "#FFFFFF", outline="#D4DEE9", width=4, radius=26)
            ImageDraw.Draw(img).text((x0 + 820, y0 + 558), "应急设施", font=load_font(38, bold=True), fill="#2D3748")
    elif cid == "E16":
        if side == "front":
            for i in range(3):
                draw.arc((cx - 150 + i * 30, cy - 60 - i * 18, cx + 40 + i * 30, cy + 160 - i * 18), 35, 155, fill="#8FAAB8", width=8)
        else:
            draw_warning_tape(draw, (cx - 180, cy + 230, cx + 180, cy + 278))
            draw_chip(draw, (cx - 90, cy + 300, cx + 130, cy + 360), "优先撤离", theme["soft"], theme["accent_dark"], 34)
    elif cid == "E17":
        draw_clipboard(draw, (cx - 190, cy + 80, cx - 10, cy + 330), theme["accent"])
        draw_bottle(draw, (cx + 120, cy + 120), 0.8, label_text="实物")
        (draw_x_icon if side == "front" else draw_check_icon)(draw, (cx + 40, cy - 10), 0.9, "#D95A57" if side == "front" else theme["accent_dark"])
    elif cid == "E18":
        draw_power_icon(draw, (cx - 20, cy - 10), 1.05, "#D95A57" if side == "front" else theme["accent_dark"])
        draw_clipboard(draw, (cx - 210, cy + 120, cx - 20, cy + 360), theme["accent"])
        if side == "back":
            draw_chip(draw, (cx + 40, cy + 200, cx + 240, cy + 262), "补记录", theme["soft"], theme["accent_dark"], 34)
    elif cid == "E19":
        draw.line((cx - 170, cy + 120, cx + 80, cy + 120), fill="#6B7C92", width=16)
        draw.line((cx + 80, cy + 120, cx + 180, cy + 48), fill="#6B7C92", width=16)
        if side == "front":
            draw.line((cx - 10, cy + 104, cx + 20, cy + 150), fill="#4CC3FF", width=8)
        else:
            draw_chip(draw, (cx - 70, cy + 220, cx + 180, cy + 282), "重新固定", theme["soft"], theme["accent_dark"], 34)
    elif cid == "E20":
        draw_centrifuge(draw, (cx - 230, cy + 10, cx + 150, cy + 300), shaky=(side == "front"))
        if side == "back":
            draw_chip(draw, (cx - 40, cy + 320, cx + 190, cy + 382), "重新配平", theme["soft"], theme["accent_dark"], 34)
    elif cid == "E21":
        draw_rotavap(draw, (cx - 260, cy + 10, cx + 210, cy + 300), loose=(side == "front"))
        if side == "back":
            draw_chip(draw, (cx - 50, cy + 320, cx + 180, cy + 382), "重新固定", theme["soft"], theme["accent_dark"], 34)
    elif cid == "E22":
        draw_fumehood(draw, (cx - 240, cy - 90, cx + 260, cy + 290), sash_high=(side == "front"))
        if side == "back":
            draw_chip(draw, (cx - 120, cy + 308, cx + 120, cy + 370), "调整前窗", theme["soft"], theme["accent_dark"], 34)
    elif cid == "E23":
        draw_powder(draw, (cx - 120, cy + 150, cx + 70, cy + 220))
        if side == "back":
            draw_warning_tape(draw, (cx - 180, cy + 52, cx + 160, cy + 100))
        else:
            draw_info_icon(draw, (cx + 190, cy + 92), 0.9, "#D95A57")
    elif cid == "E24":
        draw_cylinder(draw, (cx - 90, cy - 90, cx + 60, cy + 250), secure=True, frost=(side == "front"))
        if side == "back":
            draw_warning_tape(draw, (cx - 170, cy + 280, cx + 170, cy + 328))


def draw_task_scene(img: Image.Image, card: CardRecord, side: str, role: str, box: tuple[int, int, int, int], theme: dict[str, str]) -> None:
    proxy_map = {
        "T01": "E01",
        "T02": "E05",
        "T03": "E12",
        "T04": "E04",
        "T05": "E09",
        "T06": "E22",
        "T07": "E03",
        "T08": "E24",
        "T09": "E17",
        "T10": "E14",
        "T11": "E21",
        "T12": "E18",
    }
    proxy = CardRecord(proxy_map[card.card_id], "event", proxy_map[card.card_id], {"主角": role})
    draw_event_scene(img, proxy, "back", role, box, theme)


def draw_action_scene(img: Image.Image, card: CardRecord, side: str, role: str, box: tuple[int, int, int, int], theme: dict[str, str]) -> None:
    proxy_map = {
        "A01": "E18",
        "A02": "E01",
        "A03": "E17",
        "A04": "E22",
        "A05": "E04",
        "A06": "E07",
        "A07": "E13",
        "A08": "E24",
        "A09": "E06",
        "A10": "E08",
        "A11": "E19",
        "A12": "E23",
    }
    proxy = CardRecord(proxy_map[card.card_id], "event", proxy_map[card.card_id], {"主角": role})
    draw_event_scene(img, proxy, "back", role, box, theme)


def draw_role_scene(img: Image.Image, card: CardRecord, side: str, role: str, box: tuple[int, int, int, int], theme: dict[str, str]) -> None:
    draw = ImageDraw.Draw(img)
    x0, y0, x1, y1 = box
    if side == "front":
        draw_role_character(img, (x0 + 180, y0 + 70, x1 - 180, y1 - 40), role, pose="neutral", coat=True, goggles=(role == "程砚"))
        draw_chip(draw, (x0 + 90, y0 + 90, x0 + 290, y0 + 152), ROLE_TO_ID[role], theme["soft"], theme["accent_dark"], 34)
        draw_chip(draw, (x1 - 290, y0 + 90, x1 - 90, y0 + 152), card.fields.get("正面标题", "角色"), theme["soft"], theme["accent_dark"], 34)
    else:
        proxy_map = {"林澄": "E17", "周衡": "E21", "顾宁": "E15", "程砚": "E19"}
        proxy = CardRecord(proxy_map[role], "event", proxy_map[role], {"主角": role})
        draw_event_scene(img, proxy, "back", role, box, theme)


def draw_strategy_scene(img: Image.Image, card: CardRecord, side: str, role: str, box: tuple[int, int, int, int], theme: dict[str, str]) -> None:
    draw = ImageDraw.Draw(img)
    x0, y0, x1, y1 = box
    draw_role_character(img, (x0 + 150, y0 + 110, x0 + 700, y1 - 30), role, pose="check", coat=True)
    if side == "front":
        for idx, yy in enumerate([y0 + 220, y0 + 380, y0 + 540]):
            ax0 = x0 + 760
            ax1 = x1 - 110
            draw.rounded_rectangle((ax0, yy, ax1, yy + 86), radius=28, fill=lighten(theme["accent"], 0.78), outline=theme["accent_dark"], width=4)
            draw.line((ax0 + 40, yy + 42, ax1 - 70, yy + 42), fill=theme["accent_dark"], width=8)
            draw.polygon([(ax1 - 70, yy + 20), (ax1 - 20, yy + 42), (ax1 - 70, yy + 64)], fill=theme["accent_dark"])
    else:
        for i, label in enumerate(["效果", "代价", "打法"]):
            y = y0 + 150 + i * 180
            draw.rounded_rectangle((x0 + 760, y, x1 - 80, y + 120), radius=26, fill="#FFFFFF", outline="#D6DFE8", width=4)
            draw_chip(draw, (x0 + 790, y + 26, x0 + 970, y + 84), label, theme["soft"], theme["accent_dark"], 30)


def draw_scene(img: Image.Image, card: CardRecord, side: str, theme: dict[str, str]) -> None:
    box = scene_box()
    draw_round_panel(img, box, "#F6FAFF", outline="#D5E0EC", width=3, radius=34)
    inner = (box[0] + 24, box[1] + 24, box[2] - 24, box[3] - 24)
    draw_lab_backdrop(img, inner, theme)
    role = card.fields.get("主角", "")
    if card.card_type == "event":
        draw_event_scene(img, card, side, role, inner, theme)
    elif card.card_type == "task":
        draw_task_scene(img, card, side, role, inner, theme)
    elif card.card_type == "action":
        draw_action_scene(img, card, side, role, inner, theme)
    elif card.card_type == "role":
        draw_role_scene(img, card, side, role, inner, theme)
    else:
        draw_strategy_scene(img, card, side, role, inner, theme)


def draw_event_front(img: Image.Image, card: CardRecord, theme: dict[str, str]) -> None:
    draw = ImageDraw.Draw(img)
    draw_header(draw, card, theme)
    draw_title_area(draw, card.fields["正面标题"])
    draw_scene(img, card, "front", theme)
    left_box = (110, 1355, 710, 1950)
    right_box = (790, 1355, 1390, 1950)
    draw_round_panel(img, left_box, "#FFFFFF", outline="#D8E0E8", width=3, radius=32)
    draw_round_panel(img, right_box, "#FFFFFF", outline="#D8E0E8", width=3, radius=32)
    draw_eye_icon(draw, (170, 1436), 1.0, theme["accent_dark"])
    label_font = load_font(42, bold=True)
    draw.text((220, 1404), "观察重点", font=label_font, fill="#111827")
    body_font = load_font(34, bold=False)
    lines = wrap_text(draw, card.fields["正面观察重点"], body_font, 500, max_lines=4)
    draw_multiline(draw, (146, 1492), lines, body_font, "#1F2937", 10)
    draw_x_icon(draw, (850, 1438), 1.0, theme["accent_dark"])
    draw.text((900, 1404), "错误倾向", font=label_font, fill="#111827")
    rlines = wrap_text(draw, card.fields["正面错误倾向"], body_font, 480, max_lines=4)
    draw_multiline(draw, (826, 1492), rlines, body_font, "#1F2937", 10)


def draw_event_back(img: Image.Image, card: CardRecord, theme: dict[str, str]) -> None:
    draw = ImageDraw.Draw(img)
    draw_header(draw, card, theme)
    draw_title_area(draw, "正确处置与知识点")
    draw_scene(img, card, "back", theme)
    boxes = [
        (110, 1355, 710, 1615),
        (790, 1355, 1390, 1615),
        (110, 1678, 710, 1938),
        (790, 1678, 1390, 1938),
    ]
    blocks = [
        ("正确处置", card.fields["背面正确处置"], draw_check_icon),
        ("原因", card.fields["背面原因"], draw_info_icon),
        ("知识点", card.fields["背面知识点"], draw_bulb_icon),
        ("复盘问题", card.fields["背面复盘题"], draw_question_icon),
    ]
    for box, (label, body, icon) in zip(boxes, blocks, strict=True):
        draw_round_panel(img, box, "#FFFFFF", outline="#D8E0E8", width=3, radius=30)
        icon(draw, (box[0] + 60, box[1] + 62), 0.95, theme["accent_dark"])
        label_font = load_font(40, bold=True)
        draw.text((box[0] + 108, box[1] + 30), label, font=label_font, fill="#111827")
        body_font = load_font(31, bold=False)
        lines = wrap_text(draw, body, body_font, box[2] - box[0] - 72, max_lines=4)
        draw_multiline(draw, (box[0] + 34, box[1] + 104), lines, body_font, "#1F2937", 8)


def draw_task_front(img: Image.Image, card: CardRecord, theme: dict[str, str]) -> None:
    draw = ImageDraw.Draw(img)
    draw_header(draw, card, theme)
    draw_title_area(draw, card.fields["正面标题"])
    draw_scene(img, card, "front", theme)
    goal_box = (110, 1355, 1390, 1530)
    tags_box = (110, 1550, 1390, 1765)
    actions_box = (110, 1785, 1390, 1950)
    draw_round_panel(img, goal_box, "#FFFFFF", outline="#D8E0E8", width=3, radius=30)
    draw_round_panel(img, tags_box, "#FFFFFF", outline="#D8E0E8", width=3, radius=30)
    draw_round_panel(img, actions_box, "#FFFFFF", outline="#D8E0E8", width=3, radius=30)
    label_font = load_font(36, bold=True)
    draw.text((146, 1386), "任务目标", font=label_font, fill="#111827")
    draw.text((146, 1580), "风险标签", font=label_font, fill="#111827")
    draw.text((146, 1810), "优先行动", font=label_font, fill="#111827")
    body_font = load_font(32, bold=False)
    lines = wrap_text(draw, card.fields["正面任务描述"], body_font, 1180, max_lines=3)
    draw_multiline(draw, (146, 1436), lines, body_font, "#1F2937", 8)
    x = 146
    for tag in split_items(card.fields.get("风险标签", "")):
        width = min(240, max(140, 50 + len(tag) * 36))
        draw_chip(draw, (x, 1640, x + width, 1700), tag, theme["soft"], theme["accent_dark"], 28)
        x += width + 18
    x = 146
    for tag in split_items(card.fields.get("优先行动", "")):
        width = min(290, max(170, 60 + len(tag) * 34))
        draw_chip(draw, (x, 1866, x + width, 1928), tag, lighten(theme["accent"], 0.82), theme["accent_dark"], 27)
        x += width + 16


def draw_task_back(img: Image.Image, card: CardRecord, theme: dict[str, str]) -> None:
    draw = ImageDraw.Draw(img)
    draw_header(draw, card, theme)
    draw_title_area(draw, "任务奖励与教学提醒")
    draw_scene(img, card, "back", theme)
    boxes = [(110, 1355, 1390, 1535), (110, 1560, 1390, 1740), (110, 1765, 1390, 1950)]
    blocks = [
        ("完成奖励", card.fields["完成奖励"]),
        ("常见风险", card.fields.get("风险标签", "")),
        ("教学提醒", card.fields["背面教学提醒"]),
    ]
    for box, (label, body) in zip(boxes, blocks, strict=True):
        draw_round_panel(img, box, "#FFFFFF", outline="#D8E0E8", width=3, radius=28)
        draw_chip(draw, (box[0] + 26, box[1] + 24, box[0] + 210, box[1] + 82), label, theme["soft"], theme["accent_dark"], 28)
        font = load_font(33, bold=False)
        lines = wrap_text(draw, body, font, box[2] - box[0] - 70, max_lines=4)
        draw_multiline(draw, (box[0] + 40, box[1] + 98), lines, font, "#1F2937", 8)


def draw_action_front(img: Image.Image, card: CardRecord, theme: dict[str, str]) -> None:
    draw = ImageDraw.Draw(img)
    draw_header(draw, card, theme)
    draw_title_area(draw, card.fields["正面标题"])
    draw_scene(img, card, "front", theme)
    info_box = (110, 1360, 1390, 1538)
    tags_box = (110, 1568, 1390, 1950)
    draw_round_panel(img, info_box, "#FFFFFF", outline="#D8E0E8", width=3, radius=28)
    draw_round_panel(img, tags_box, "#FFFFFF", outline="#D8E0E8", width=3, radius=28)
    draw_chip(draw, (136, 1388, 350, 1448), "核心用途", theme["soft"], theme["accent_dark"], 30)
    body_font = load_font(34, bold=False)
    lines = wrap_text(draw, card.fields["正面一句话"], body_font, 1180, max_lines=2)
    draw_multiline(draw, (146, 1458), lines, body_font, "#1F2937", 8)
    draw_chip(draw, (136, 1594, 350, 1654), "适用场景", theme["soft"], theme["accent_dark"], 30)
    lines = wrap_text(draw, card.fields["适用场景"], body_font, 1180, max_lines=4)
    draw_multiline(draw, (146, 1660), lines, body_font, "#1F2937", 8)


def draw_action_back(img: Image.Image, card: CardRecord, theme: dict[str, str]) -> None:
    draw = ImageDraw.Draw(img)
    draw_header(draw, card, theme)
    draw_title_area(draw, "适用场景与协同处理")
    draw_scene(img, card, "back", theme)
    boxes = [(110, 1355, 1390, 1535), (110, 1560, 1390, 1740), (110, 1765, 1390, 1950)]
    blocks = [("适用场景", card.fields["适用场景"]), ("不足边界", card.fields["不足场景"]), ("协同行动", card.fields["协同行动"])]
    for box, (label, body) in zip(boxes, blocks, strict=True):
        draw_round_panel(img, box, "#FFFFFF", outline="#D8E0E8", width=3, radius=28)
        draw_chip(draw, (box[0] + 26, box[1] + 24, box[0] + 210, box[1] + 82), label, theme["soft"], theme["accent_dark"], 28)
        font = load_font(33, bold=False)
        lines = wrap_text(draw, body, font, box[2] - box[0] - 70, max_lines=4)
        draw_multiline(draw, (box[0] + 40, box[1] + 98), lines, font, "#1F2937", 8)


def draw_role_front(img: Image.Image, card: CardRecord, theme: dict[str, str]) -> None:
    draw = ImageDraw.Draw(img)
    draw_header(draw, card, theme)
    draw_title_area(draw, f'{card.fields["正面标题"]} {card.fields["正面角色名"]}')
    draw_scene(img, card, "front", theme)
    bottom = (110, 1380, 1390, 1950)
    draw_round_panel(img, bottom, "#FFFFFF", outline="#D8E0E8", width=3, radius=34)
    draw_chip(draw, (140, 1410, 340, 1470), "角色标语", theme["soft"], theme["accent_dark"], 30)
    font = load_font(36, bold=True)
    lines = wrap_text(draw, card.fields["正面标语"], font, 1160, max_lines=2)
    draw_multiline(draw, (150, 1496), lines, font, "#111827", 8)
    draw_chip(draw, (140, 1648, 340, 1708), "角色描述", theme["soft"], theme["accent_dark"], 30)
    body_font = load_font(33, bold=False)
    lines = wrap_text(draw, card.fields["正面角色描述"], body_font, 1160, max_lines=4)
    draw_multiline(draw, (150, 1730), lines, body_font, "#1F2937", 8)


def draw_role_back(img: Image.Image, card: CardRecord, theme: dict[str, str]) -> None:
    draw = ImageDraw.Draw(img)
    draw_header(draw, card, theme)
    draw_title_area(draw, "能力与使用节奏")
    draw_scene(img, card, "back", theme)
    boxes = [(110, 1355, 1390, 1535), (110, 1560, 1390, 1740), (110, 1765, 1390, 1950)]
    blocks = [("角色能力", card.fields["背面能力"]), ("使用节奏", card.fields["背面玩法提示"]), ("适配流派", card.fields["背面玩法提示"])]
    for box, (label, body) in zip(boxes, blocks, strict=True):
        draw_round_panel(img, box, "#FFFFFF", outline="#D8E0E8", width=3, radius=28)
        draw_chip(draw, (box[0] + 26, box[1] + 24, box[0] + 210, box[1] + 82), label, theme["soft"], theme["accent_dark"], 28)
        font = load_font(33, bold=False)
        lines = wrap_text(draw, body, font, box[2] - box[0] - 70, max_lines=4)
        draw_multiline(draw, (box[0] + 40, box[1] + 98), lines, font, "#1F2937", 8)


def draw_strategy_front(img: Image.Image, card: CardRecord, theme: dict[str, str]) -> None:
    draw = ImageDraw.Draw(img)
    draw_header(draw, card, theme)
    draw_title_area(draw, card.fields["正面标题"])
    draw_scene(img, card, "front", theme)
    bottom = (110, 1380, 1390, 1950)
    draw_round_panel(img, bottom, "#FFFFFF", outline="#D8E0E8", width=3, radius=34)
    draw_chip(draw, (140, 1410, 320, 1470), "路线导语", theme["soft"], theme["accent_dark"], 30)
    font = load_font(36, bold=True)
    lines = wrap_text(draw, card.fields["正面导语"], font, 1160, max_lines=3)
    draw_multiline(draw, (150, 1500), lines, font, "#111827", 10)
    draw_chip(draw, (140, 1700, 340, 1760), "主角", theme["soft"], theme["accent_dark"], 30)
    font2 = load_font(34, bold=True)
    draw.text((170, 1800), card.fields["主角"], font=font2, fill="#1F2937")


def draw_strategy_back(img: Image.Image, card: CardRecord, theme: dict[str, str]) -> None:
    draw = ImageDraw.Draw(img)
    draw_header(draw, card, theme)
    draw_title_area(draw, "效果、代价与打法")
    draw_scene(img, card, "back", theme)
    boxes = [(110, 1355, 1390, 1535), (110, 1560, 1390, 1740), (110, 1765, 1390, 1950)]
    blocks = [("效果", card.fields["背面效果"]), ("代价", card.fields["背面代价"]), ("适合打法", card.fields["背面适合玩法"])]
    for box, (label, body) in zip(boxes, blocks, strict=True):
        draw_round_panel(img, box, "#FFFFFF", outline="#D8E0E8", width=3, radius=28)
        draw_chip(draw, (box[0] + 26, box[1] + 24, box[0] + 210, box[1] + 82), label, theme["soft"], theme["accent_dark"], 28)
        font = load_font(33, bold=False)
        lines = wrap_text(draw, body, font, box[2] - box[0] - 70, max_lines=4)
        draw_multiline(draw, (box[0] + 40, box[1] + 98), lines, font, "#1F2937", 8)


def render_card(card: CardRecord, side: str) -> Image.Image:
    theme = get_theme(card)
    img = build_base_card(theme)
    if card.card_type == "event" and side == "front":
        draw_event_front(img, card, theme)
    elif card.card_type == "event":
        draw_event_back(img, card, theme)
    elif card.card_type == "task" and side == "front":
        draw_task_front(img, card, theme)
    elif card.card_type == "task":
        draw_task_back(img, card, theme)
    elif card.card_type == "action" and side == "front":
        draw_action_front(img, card, theme)
    elif card.card_type == "action":
        draw_action_back(img, card, theme)
    elif card.card_type == "role" and side == "front":
        draw_role_front(img, card, theme)
    elif card.card_type == "role":
        draw_role_back(img, card, theme)
    elif card.card_type == "strategy" and side == "front":
        draw_strategy_front(img, card, theme)
    else:
        draw_strategy_back(img, card, theme)
    return img


def save_card(img: Image.Image, path: Path) -> None:
    ensure_dir(path.parent)
    img.save(path, format="PNG", dpi=DPI, optimize=True)


def category_dir(card_type: str) -> str:
    return {"event": "events", "task": "tasks", "action": "actions", "role": "roles", "strategy": "strategies"}[card_type]


def create_preview(cards: list[CardRecord]) -> None:
    ensure_dir(PREVIEW_ROOT)
    html = [
        "<!doctype html><html lang='zh-CN'><head><meta charset='utf-8'><title>v0.8 全卡牌预览</title><style>",
        "body{font-family:'Microsoft YaHei',sans-serif;background:#EEF3F8;margin:0;padding:24px;color:#17202A;}",
        "h1{margin:0 0 8px;font-size:30px;}p{margin:0 0 24px;color:#4B5563;}",
        ".grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(460px,1fr));gap:18px;}",
        ".item{background:#fff;border-radius:20px;padding:18px;box-shadow:0 10px 26px rgba(15,23,42,.12);}",
        ".meta{font-size:15px;color:#4B5563;margin-bottom:10px;}.pair{display:grid;grid-template-columns:1fr 1fr;gap:10px;}",
        ".pair img{width:100%;border-radius:16px;background:#F8FBFF;display:block;}</style></head><body>",
        "<h1>v0.8 全56张卡牌预览</h1><p>本页展示全部卡牌的正反两面成品 PNG，中文文字全部为后期程序化排版。</p><div class='grid'>",
    ]
    for card in cards:
        cat = category_dir(card.card_type)
        title = card.fields.get("正面标题", card.heading)
        role = card.fields.get("主角", "")
        html.append(
            f"<div class='item'><div class='meta'><strong>{card.card_id}</strong> {title} | {card.card_type} | 主角：{role}</div>"
            f"<div class='pair'><img src='../{cat}/{card.card_id}_front.png' alt='{card.card_id} front'><img src='../{cat}/{card.card_id}_back.png' alt='{card.card_id} back'></div></div>"
        )
    html.append("</div></body></html>")
    (PREVIEW_ROOT / "index.html").write_text("".join(html), encoding="utf-8")


def build_print_sheet(image_paths: list[Path], out_path: Path) -> None:
    ensure_dir(out_path.parent)
    page = Image.new("RGBA", (2480, 3508), "#FFFFFF")
    margin_x = 110
    margin_y = 90
    gap_x = 70
    gap_y = 70
    slot_w = 1060
    slot_h = 1030
    for idx, path in enumerate(image_paths):
        img = Image.open(path).convert("RGBA").resize((slot_w, slot_h), Image.Resampling.LANCZOS)
        row = idx // 2
        col = idx % 2
        x = margin_x + col * (slot_w + gap_x)
        y = margin_y + row * (slot_h + gap_y)
        page.alpha_composite(img, (x, y))
    page.convert("RGB").save(out_path, format="PNG", dpi=DPI, optimize=True)


def main() -> None:
    cards = parse_cards()
    ensure_dir(OUTPUT_ROOT)
    manifest_cards = []
    for card in cards:
        cat = category_dir(card.card_type)
        front_path = OUTPUT_ROOT / cat / f"{card.card_id}_front.png"
        back_path = OUTPUT_ROOT / cat / f"{card.card_id}_back.png"
        save_card(render_card(card, "front"), front_path)
        save_card(render_card(card, "back"), back_path)
        manifest_cards.append(
            {
                "card_id": card.card_id,
                "card_type": card.card_type,
                "protagonist": card.fields.get("主角", ""),
                "front_path": str(front_path.relative_to(ROOT)).replace("\\", "/"),
                "back_path": str(back_path.relative_to(ROOT)).replace("\\", "/"),
            }
        )

    role_counts = {role: 0 for role in ROLE_ORDER}
    for item in manifest_cards:
        role_counts[item["protagonist"]] += 1
    MANIFEST_PATH.write_text(json.dumps({"card_count": len(manifest_cards), "side_count": len(manifest_cards) * 2, "role_counts": role_counts, "cards": manifest_cards}, ensure_ascii=False, indent=2), encoding="utf-8")
    create_preview(cards)

    type_map = {card.card_id: category_dir(card.card_type) for card in cards}
    fronts = [OUTPUT_ROOT / type_map[cid] / f"{cid}_front.png" for cid in SAMPLE_PRINT_IDS]
    backs = [OUTPUT_ROOT / type_map[cid] / f"{cid}_back.png" for cid in SAMPLE_PRINT_IDS]
    build_print_sheet(fronts, PRINT_ROOT / "sample_front_sheet.png")
    build_print_sheet(backs, PRINT_ROOT / "sample_back_sheet.png")


if __name__ == "__main__":
    main()
