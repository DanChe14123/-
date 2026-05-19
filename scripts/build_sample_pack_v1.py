from __future__ import annotations

import json
from pathlib import Path

from PIL import Image, ImageColor, ImageDraw, ImageFilter, ImageFont, ImageOps


ROOT = Path(__file__).resolve().parents[1]
DATA_PATH = ROOT / "content" / "sample_pack_v1.json"
OUT_ROOT = ROOT / "card" / "samples" / "v1"
CARDS_ROOT = OUT_ROOT / "cards"
HANDBOOK_ROOT = OUT_ROOT / "handbook"
PREVIEW_ROOT = OUT_ROOT / "preview"

CARD_SIZE = (1500, 2100)
PAGE_SIZE = (2480, 3508)
DPI = (300, 300)

TITLE_FONTS = [
    r"C:\Windows\Fonts\Noto Sans SC Bold (TrueType).otf",
    r"C:\Windows\Fonts\msyhbd.ttc",
    r"C:\Windows\Fonts\simhei.ttf",
]
BODY_FONTS = [
    r"C:\Windows\Fonts\Noto Sans SC Medium (TrueType).otf",
    r"C:\Windows\Fonts\msyh.ttc",
    r"C:\Windows\Fonts\simsun.ttc",
]


def ensure_dir(path: Path) -> None:
    path.mkdir(parents=True, exist_ok=True)


def load_font(size: int, *, bold: bool = False) -> ImageFont.FreeTypeFont:
    candidates = TITLE_FONTS if bold else BODY_FONTS
    for candidate in candidates:
        if Path(candidate).exists():
            return ImageFont.truetype(candidate, size=size)
    raise FileNotFoundError("No usable Chinese font found.")


def text_size(draw: ImageDraw.ImageDraw, text: str, font: ImageFont.FreeTypeFont) -> tuple[int, int]:
    box = draw.textbbox((0, 0), text, font=font)
    return box[2] - box[0], box[3] - box[1]


def wrap_text(draw: ImageDraw.ImageDraw, text: str, font: ImageFont.FreeTypeFont, max_width: int) -> list[str]:
    if not text:
        return [""]
    lines: list[str] = []
    current = ""
    for ch in text:
        test = current + ch
        if not current or text_size(draw, test, font)[0] <= max_width:
            current = test
        else:
            lines.append(current)
            current = ch
    if current:
        lines.append(current)
    return lines


def fit_font(draw: ImageDraw.ImageDraw, text: str, max_width: int, max_size: int, *, min_size: int = 24, bold: bool = True) -> ImageFont.FreeTypeFont:
    size = max_size
    while size >= min_size:
        font = load_font(size, bold=bold)
        if text_size(draw, text, font)[0] <= max_width:
            return font
        size -= 2
    return load_font(min_size, bold=bold)


def draw_multiline(
    draw: ImageDraw.ImageDraw,
    xy: tuple[int, int],
    text: str,
    font: ImageFont.FreeTypeFont,
    fill: str,
    max_width: int,
    line_gap: int = 10,
    max_lines: int | None = None,
) -> int:
    x, y = xy
    lines = wrap_text(draw, text, font, max_width)
    if max_lines and len(lines) > max_lines:
        lines = lines[:max_lines]
        last = lines[-1]
        while text_size(draw, last + "…", font)[0] > max_width and last:
            last = last[:-1]
        lines[-1] = last + "…"
    _, h = text_size(draw, "高", font)
    for line in lines:
        draw.text((x, y), line, font=font, fill=fill)
        y += h + line_gap
    return y


def rounded_mask(size: tuple[int, int], radius: int) -> Image.Image:
    mask = Image.new("L", size, 0)
    ImageDraw.Draw(mask).rounded_rectangle((0, 0, size[0] - 1, size[1] - 1), radius=radius, fill=255)
    return mask


def paste_rounded(base: Image.Image, layer: Image.Image, xy: tuple[int, int], radius: int) -> None:
    temp = Image.new("RGBA", base.size, (0, 0, 0, 0))
    mask = rounded_mask(layer.size, radius)
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


def add_shadow(base: Image.Image, box: tuple[int, int, int, int], radius: int = 48) -> None:
    shadow = Image.new("RGBA", base.size, (0, 0, 0, 0))
    layer = Image.new("L", base.size, 0)
    ImageDraw.Draw(layer).rounded_rectangle(box, radius=radius, fill=255)
    blur = layer.filter(ImageFilter.GaussianBlur(28))
    shadow.paste((12, 22, 40, 56), (20, 28), blur)
    base.alpha_composite(shadow)


def draw_panel(base: Image.Image, box: tuple[int, int, int, int], fill: str, outline: str, radius: int, width: int = 3) -> None:
    layer = Image.new("RGBA", (box[2] - box[0], box[3] - box[1]), (0, 0, 0, 0))
    ImageDraw.Draw(layer).rounded_rectangle((0, 0, layer.size[0] - 1, layer.size[1] - 1), radius=radius, fill=fill, outline=outline, width=width)
    paste_rounded(base, layer, (box[0], box[1]), radius)


def draw_icon(draw: ImageDraw.ImageDraw, kind: str, center: tuple[int, int], color: str) -> None:
    x, y = center
    draw.ellipse((x - 22, y - 22, x + 22, y + 22), outline=color, width=4)
    if kind == "eye":
        draw.ellipse((x - 16, y - 9, x + 16, y + 9), outline=color, width=3)
        draw.ellipse((x - 5, y - 5, x + 5, y + 5), fill=color)
    elif kind == "cross":
        draw.line((x - 9, y - 9, x + 9, y + 9), fill=color, width=4)
        draw.line((x + 9, y - 9, x - 9, y + 9), fill=color, width=4)
    elif kind == "check":
        draw.line((x - 9, y + 1, x - 1, y + 11), fill=color, width=4)
        draw.line((x - 1, y + 11, x + 12, y - 8), fill=color, width=4)
    elif kind == "info":
        font = load_font(30, bold=True)
        w, h = text_size(draw, "!", font)
        draw.text((x - w / 2, y - h / 2 - 2), "!", font=font, fill=color)
    elif kind == "bulb":
        draw.ellipse((x - 12, y - 18, x + 12, y + 8), outline=color, width=3)
        draw.rectangle((x - 7, y + 6, x + 7, y + 15), outline=color, width=3)
    elif kind == "question":
        font = load_font(28, bold=True)
        w, h = text_size(draw, "?", font)
        draw.text((x - w / 2, y - h / 2 - 2), "?", font=font, fill=color)


def load_crop(path: Path, crop_box: list[int], target_size: tuple[int, int]) -> Image.Image:
    art = Image.open(path).convert("RGB").crop(tuple(crop_box))
    return ImageOps.fit(art, target_size, method=Image.Resampling.LANCZOS, centering=(0.5, 0.5)).convert("RGBA")


def make_card_canvas(theme: str) -> Image.Image:
    canvas = Image.new("RGBA", CARD_SIZE, (0, 0, 0, 0))
    card_box = (40, 40, CARD_SIZE[0] - 40, CARD_SIZE[1] - 40)
    add_shadow(canvas, card_box)
    card = Image.new("RGBA", (card_box[2] - card_box[0], card_box[3] - card_box[1]), "#FFFFFF")
    draw = ImageDraw.Draw(card)
    draw.rounded_rectangle((0, 0, card.size[0] - 1, card.size[1] - 1), radius=52, fill="#FFFFFF", outline="#D5DEE8", width=3)
    header = vertical_gradient((card.size[0], 160), theme, lighten(theme, 0.24))
    paste_rounded(card, header, (0, 0), 52)
    canvas.alpha_composite(card, (40, 40))
    return canvas


def render_card_front(card: dict) -> Image.Image:
    canvas = make_card_canvas(card["theme"])
    draw = ImageDraw.Draw(canvas)
    theme = card["theme"]
    ink = "#111827"
    accent_dark = darken(theme, 0.22)

    id_font = load_font(56, bold=True)
    tag_font = load_font(48, bold=True)
    draw.text((94, 84), card["card_id"], font=id_font, fill="#FFFFFF")
    rw, _ = text_size(draw, card["risk"], tag_font)
    draw.text((CARD_SIZE[0] - 92 - rw, 88), card["risk"], font=tag_font, fill="#FFFFFF")

    title_font = fit_font(draw, card["title"], 1180, 82, min_size=54, bold=True)
    tw, th = text_size(draw, card["title"], title_font)
    draw.text(((CARD_SIZE[0] - tw) / 2, 250), card["title"], font=title_font, fill=ink)

    art_box = (110, 420, CARD_SIZE[0] - 110, 1320)
    draw_panel(canvas, art_box, "#F8FBFF", "#D7E1EC", 32, width=3)
    art = load_crop(ROOT / card["reference_image"], card["front_art_crop"], (art_box[2] - art_box[0] - 30, art_box[3] - art_box[1] - 30))
    paste_rounded(canvas, art, (art_box[0] + 15, art_box[1] + 15), 26)

    left_box = (110, 1390, 705, 1940)
    right_box = (795, 1390, 1390, 1940)
    for box in (left_box, right_box):
        draw_panel(canvas, box, "#FFFFFF", "#D7E1EC", 30, width=3)

    label_font = load_font(42, bold=True)
    body_font = load_font(36, bold=False)

    draw_icon(draw, "eye", (166, 1460), accent_dark)
    draw.text((212, 1428), "观察重点", font=label_font, fill=ink)
    draw_multiline(draw, (142, 1522), card["front_focus_short"], body_font, "#1F2937", 500, line_gap=10, max_lines=3)

    draw_icon(draw, "cross", (850, 1460), accent_dark)
    draw.text((896, 1428), "错误倾向", font=label_font, fill=ink)
    draw_multiline(draw, (826, 1522), card["front_mistake_short"], body_font, "#1F2937", 480, line_gap=10, max_lines=3)
    return canvas


def render_card_back(card: dict) -> Image.Image:
    canvas = make_card_canvas(card["theme"])
    draw = ImageDraw.Draw(canvas)
    theme = card["theme"]
    ink = "#111827"
    accent_dark = darken(theme, 0.22)

    id_font = load_font(56, bold=True)
    tag_font = load_font(48, bold=True)
    draw.text((94, 84), card["card_id"], font=id_font, fill="#FFFFFF")
    rw, _ = text_size(draw, card["risk"], tag_font)
    draw.text((CARD_SIZE[0] - 92 - rw, 88), card["risk"], font=tag_font, fill="#FFFFFF")

    title = "正确处置与知识点"
    title_font = fit_font(draw, title, 1180, 78, min_size=56, bold=True)
    tw, _ = text_size(draw, title, title_font)
    draw.text(((CARD_SIZE[0] - tw) / 2, 250), title, font=title_font, fill=ink)

    art_box = (110, 420, CARD_SIZE[0] - 110, 1210)
    draw_panel(canvas, art_box, "#F8FBFF", "#D7E1EC", 32, width=3)
    art = load_crop(ROOT / card["reference_image"], card["back_art_crop"], (art_box[2] - art_box[0] - 30, art_box[3] - art_box[1] - 30))
    paste_rounded(canvas, art, (art_box[0] + 15, art_box[1] + 15), 26)

    boxes = [
        (110, 1270, 705, 1545),
        (795, 1270, 1390, 1545),
        (110, 1600, 705, 1875),
        (795, 1600, 1390, 1875),
    ]
    labels = [
        ("check", "正确处置", card["back_action_short"]),
        ("info", "原因", card["back_reason_short"]),
        ("bulb", "知识点", card["back_knowledge_short"]),
        ("question", "复盘问题", card["back_review_short"]),
    ]
    label_font = load_font(38, bold=True)
    body_font = load_font(31, bold=False)
    for box, (icon, title_text, body_text) in zip(boxes, labels, strict=True):
        draw_panel(canvas, box, "#FFFFFF", "#D7E1EC", 26, width=3)
        draw_icon(draw, icon, (box[0] + 52, box[1] + 58), accent_dark)
        draw.text((box[0] + 100, box[1] + 26), title_text, font=label_font, fill=ink)
        draw_multiline(draw, (box[0] + 34, box[1] + 96), body_text, body_font, "#1F2937", box[2] - box[0] - 64, line_gap=6, max_lines=3)
    return canvas


def render_cover_page(data: dict, card_paths: dict[str, Path]) -> Image.Image:
    page = Image.new("RGBA", PAGE_SIZE, "#F5F8FC")
    draw = ImageDraw.Draw(page)
    theme = "#4E83D9"
    accent = darken(theme, 0.18)
    header = vertical_gradient((PAGE_SIZE[0], 420), "#FFFFFF", "#EAF3FF")
    page.alpha_composite(header, (0, 0))

    title_font = load_font(102, bold=True)
    sub_font = load_font(54, bold=False)
    body_font = load_font(38, bold=False)
    small_font = load_font(34, bold=False)

    draw.text((170, 168), data["project_title"], font=title_font, fill="#111827")
    draw.text((176, 292), data["subtitle"], font=sub_font, fill="#4B5563")

    draw_panel(page, (150, 500, 2330, 1350), "#FFFFFF", "#D9E3EE", 40, width=3)
    draw.text((220, 570), "样板目标", font=load_font(52, bold=True), fill="#111827")
    bullets = [
        "先锁事件牌正式视觉，不继续沿用旧版粗糙样式。",
        "卡面只保留短语级信息，详细解释转移到使用手册。",
        "中文全部后期排版，保证标题和正文在屏幕与打印下都清晰。",
        "当前样板只覆盖 E02 / E05，用于确认美术和版式方向。"
    ]
    y = 660
    for bullet in bullets:
        draw.ellipse((224, y + 12, 244, y + 32), fill=theme)
        y = draw_multiline(draw, (270, y), bullet, body_font, "#1F2937", 1800, line_gap=10)
        y += 22

    draw.text((180, 1470), "当前样板", font=load_font(60, bold=True), fill="#111827")
    front1 = Image.open(card_paths["E02_front"]).convert("RGBA").resize((520, 728), Image.Resampling.LANCZOS)
    back1 = Image.open(card_paths["E02_back"]).convert("RGBA").resize((520, 728), Image.Resampling.LANCZOS)
    front2 = Image.open(card_paths["E05_front"]).convert("RGBA").resize((520, 728), Image.Resampling.LANCZOS)
    back2 = Image.open(card_paths["E05_back"]).convert("RGBA").resize((520, 728), Image.Resampling.LANCZOS)
    positions = [(180, 1600), (740, 1600), (1300, 1600), (1860, 1600)]
    for img, (x, y), title in zip(
        [front1, back1, front2, back2],
        positions,
        ["E02 正面", "E02 背面", "E05 正面", "E05 背面"],
        strict=True,
    ):
        add_shadow(page, (x, y, x + 520, y + 728), radius=30)
        page.alpha_composite(img, (x, y))
        tw, _ = text_size(draw, title, small_font)
        draw.text((x + (520 - tw) / 2, y + 754), title, font=small_font, fill=accent)

    footer = "样板通过后，再扩展到整套事件牌与完整手册。"
    draw.text((180, 3340), footer, font=small_font, fill="#5B6675")
    return page


def render_detail_page(data: dict, card_paths: dict[str, Path]) -> Image.Image:
    page = Image.new("RGBA", PAGE_SIZE, "#F6F9FD")
    draw = ImageDraw.Draw(page)
    draw.text((170, 140), "样板详情页", font=load_font(92, bold=True), fill="#111827")
    draw.text((176, 260), "E02 / E05 详细说明与卡面对应关系", font=load_font(48, bold=False), fill="#4B5563")

    sections = [
        (data["cards"][0], 420, "#4E83D9"),
        (data["cards"][1], 1948, "#F0A045"),
    ]
    for card, top, theme in sections:
        accent = darken(theme, 0.18)
        draw_panel(page, (120, top, 2360, top + 1330), "#FFFFFF", "#D9E3EE", 34, width=3)
        draw.text((180, top + 56), f'{card["card_id"]}  {card["title"]}', font=load_font(62, bold=True), fill="#111827")
        draw.text((185, top + 144), f'主角：{card["protagonist"]}    风险等级：{card["risk"]}', font=load_font(36, bold=False), fill=accent)

        front = Image.open(card_paths[f'{card["card_id"]}_front']).convert("RGBA").resize((360, 504), Image.Resampling.LANCZOS)
        back = Image.open(card_paths[f'{card["card_id"]}_back']).convert("RGBA").resize((360, 504), Image.Resampling.LANCZOS)
        add_shadow(page, (180, top + 220, 540, top + 724), radius=24)
        add_shadow(page, (570, top + 220, 930, top + 724), radius=24)
        page.alpha_composite(front, (180, top + 220))
        page.alpha_composite(back, (570, top + 220))

        x = 1000
        section_title_font = load_font(40, bold=True)
        body_font = load_font(34, bold=False)
        labels = [
            ("场景说明", card["handbook_scene"]),
            ("正确处置", card["handbook_action"]),
            ("为什么这样做", card["handbook_reason"]),
            ("知识点与复盘", f'{card["handbook_knowledge"]}  {card["handbook_review"]}'),
        ]
        y = top + 234
        for label, body in labels:
            draw.rounded_rectangle((x, y, 2240, y + 200), radius=24, fill=lighten(theme, 0.89), outline=lighten(theme, 0.58), width=2)
            draw.text((x + 28, y + 20), label, font=section_title_font, fill=accent)
            draw_multiline(draw, (x + 28, y + 82), body, body_font, "#1F2937", 1180, line_gap=8, max_lines=4)
            y += 230
    return page


def render_overview(card_paths: dict[str, Path], handbook_paths: dict[str, Path]) -> Image.Image:
    board = Image.new("RGBA", (3300, 2900), "#EDF3F8")
    draw = ImageDraw.Draw(board)
    draw.text((120, 90), "样板预览总览", font=load_font(84, bold=True), fill="#111827")
    draw.text((124, 196), "4 张事件牌样板 + 2 页使用手册样板", font=load_font(42, bold=False), fill="#4B5563")

    card_names = ["E02_front", "E02_back", "E05_front", "E05_back"]
    positions = [(120, 340), (900, 340), (1680, 340), (2460, 340)]
    for name, (x, y) in zip(card_names, positions, strict=True):
        img = Image.open(card_paths[name]).convert("RGBA").resize((660, 924), Image.Resampling.LANCZOS)
        add_shadow(board, (x, y, x + 660, y + 924), radius=26)
        board.alpha_composite(img, (x, y))

    handbook_names = ["cover", "detail"]
    handbook_positions = [(420, 1400), (1710, 1400)]
    for name, (x, y) in zip(handbook_names, handbook_positions, strict=True):
        img = Image.open(handbook_paths[name]).convert("RGBA").resize((1080, 1527), Image.Resampling.LANCZOS)
        add_shadow(board, (x, y, x + 1080, y + 1527), radius=28)
        board.alpha_composite(img, (x, y))
    return board


def save_png(img: Image.Image, path: Path) -> None:
    ensure_dir(path.parent)
    img.convert("RGB").save(path, format="PNG", dpi=DPI, optimize=True)


def create_preview_html(card_paths: dict[str, Path], handbook_paths: dict[str, Path], overview_path: Path) -> None:
    ensure_dir(PREVIEW_ROOT)
    html = f"""<!doctype html>
<html lang="zh-CN">
<head>
  <meta charset="utf-8">
  <title>样板预览 v1</title>
  <style>
    body {{ font-family: 'Microsoft YaHei', sans-serif; margin: 0; padding: 24px; background: #eef3f8; color: #17202a; }}
    h1 {{ margin: 0 0 8px; font-size: 32px; }}
    p {{ margin: 0 0 20px; color: #4b5563; }}
    .grid {{ display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 18px; }}
    .card {{ background: white; padding: 16px; border-radius: 18px; box-shadow: 0 10px 30px rgba(15,23,42,.10); }}
    .row {{ display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 12px; }}
    img {{ width: 100%; display: block; border-radius: 14px; }}
  </style>
</head>
<body>
  <h1>样板预览 v1</h1>
  <p>当前展示 4 张事件牌样板、2 页使用手册样板与总览拼图。</p>
  <div class="card"><img src="../preview/sample_overview.png" alt="总览"></div>
  <div class="grid" style="margin-top:18px;">
    <div class="card"><div class="row">
      <img src="../cards/E02_front.png" alt="E02 front"><img src="../cards/E02_back.png" alt="E02 back">
    </div></div>
    <div class="card"><div class="row">
      <img src="../cards/E05_front.png" alt="E05 front"><img src="../cards/E05_back.png" alt="E05 back">
    </div></div>
    <div class="card"><img src="../handbook/handbook_cover.png" alt="handbook cover"></div>
    <div class="card"><img src="../handbook/handbook_detail.png" alt="handbook detail"></div>
  </div>
</body>
</html>"""
    (PREVIEW_ROOT / "index.html").write_text(html, encoding="utf-8")


def main() -> None:
    data = json.loads(DATA_PATH.read_text(encoding="utf-8"))
    ensure_dir(CARDS_ROOT)
    ensure_dir(HANDBOOK_ROOT)
    ensure_dir(PREVIEW_ROOT)

    card_paths: dict[str, Path] = {}
    for card in data["cards"]:
        front = render_card_front(card)
        back = render_card_back(card)
        front_path = CARDS_ROOT / f'{card["card_id"]}_front.png'
        back_path = CARDS_ROOT / f'{card["card_id"]}_back.png'
        save_png(front, front_path)
        save_png(back, back_path)
        card_paths[f'{card["card_id"]}_front'] = front_path
        card_paths[f'{card["card_id"]}_back'] = back_path

    cover = render_cover_page(data, card_paths)
    detail = render_detail_page(data, card_paths)
    cover_path = HANDBOOK_ROOT / "handbook_cover.png"
    detail_path = HANDBOOK_ROOT / "handbook_detail.png"
    save_png(cover, cover_path)
    save_png(detail, detail_path)

    handbook_paths = {"cover": cover_path, "detail": detail_path}
    overview = render_overview(card_paths, handbook_paths)
    overview_path = PREVIEW_ROOT / "sample_overview.png"
    save_png(overview, overview_path)
    create_preview_html(card_paths, handbook_paths, overview_path)


if __name__ == "__main__":
    main()
