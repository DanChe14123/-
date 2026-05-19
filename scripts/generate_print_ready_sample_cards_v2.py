from __future__ import annotations

import math
import shutil
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont, ImageOps, ImageFilter


ROOT = Path(__file__).resolve().parents[1]
ILLUSTRATIONS = ROOT / "card" / "final" / "v2" / "generated_illustrations"
OUT = ROOT / "card" / "final" / "v2" / "print_ready_samples"
CARD_DIR = OUT / "cards"
SHEET_DIR = OUT / "sheets"
MATERIAL_DIR = ROOT / "card" / "final" / "v2" / "参赛文件" / "08_现场可用材料"

CARD_W, CARD_H = 1050, 1470
A4_W, A4_H = 2480, 3508

COLORS = {
    "low": (64, 127, 216),
    "medium": (240, 160, 58),
    "high": (206, 86, 78),
    "task": (47, 164, 143),
    "action": (126, 91, 216),
    "post": (35, 122, 160),
    "debrief": (85, 105, 130),
    "dark": (28, 38, 54),
    "gray": (86, 98, 116),
    "light": (245, 249, 254),
    "panel": (248, 251, 255),
    "border": (200, 214, 232),
}


def font(size: int, bold: bool = False) -> ImageFont.FreeTypeFont:
    candidates = [
        Path(r"C:\Windows\Fonts\msyhbd.ttc" if bold else r"C:\Windows\Fonts\msyh.ttc"),
        Path(r"C:\Windows\Fonts\simhei.ttf"),
        Path(r"C:\Windows\Fonts\simsun.ttc"),
    ]
    for p in candidates:
        if p.exists():
            return ImageFont.truetype(str(p), size)
    return ImageFont.load_default()


F_ID = font(44, True)
F_TAG = font(30, True)
F_TITLE = font(48, True)
F_SUBTITLE = font(31, True)
F_BODY = font(28)
F_SMALL = font(23)
F_TINY = font(19)


def wrap_text(text: str, draw: ImageDraw.ImageDraw, fnt: ImageFont.FreeTypeFont, max_w: int) -> list[str]:
    lines: list[str] = []
    current = ""
    for ch in text:
        test = current + ch
        if draw.textlength(test, font=fnt) <= max_w or not current:
            current = test
        else:
            lines.append(current)
            current = ch
    if current:
        lines.append(current)
    return lines


def text_box(
    draw: ImageDraw.ImageDraw,
    xy: tuple[int, int],
    wh: tuple[int, int],
    text: str,
    fnt: ImageFont.FreeTypeFont,
    fill=COLORS["dark"],
    line_gap: int = 8,
    max_lines: int | None = None,
    align: str = "left",
) -> int:
    x, y = xy
    w, h = wh
    lines = wrap_text(text, draw, fnt, w)
    if max_lines is not None:
        lines = lines[:max_lines]
    line_h = fnt.size + line_gap
    for i, line in enumerate(lines):
        yy = y + i * line_h
        if yy + fnt.size > y + h:
            break
        xx = x
        if align == "center":
            xx = x + int((w - draw.textlength(line, font=fnt)) / 2)
        draw.text((xx, yy), line, font=fnt, fill=fill)
    return y + min(len(lines), max_lines or len(lines)) * line_h


def rounded_mask(size: tuple[int, int], radius: int) -> Image.Image:
    mask = Image.new("L", size, 0)
    d = ImageDraw.Draw(mask)
    d.rounded_rectangle((0, 0, size[0] - 1, size[1] - 1), radius=radius, fill=255)
    return mask


def paste_illustration(
    card: Image.Image,
    path: Path,
    box: tuple[int, int, int, int],
    radius: int = 28,
    mode: str = "contain",
) -> None:
    x1, y1, x2, y2 = box
    size = (x2 - x1, y2 - y1)
    if path.exists():
        img = Image.open(path).convert("RGB")
        if mode == "cover":
            fitted = ImageOps.fit(img, size, method=Image.Resampling.LANCZOS, centering=(0.5, 0.35))
        else:
            bg = ImageOps.fit(img, size, method=Image.Resampling.LANCZOS, centering=(0.5, 0.35))
            bg = bg.filter(ImageFilter.GaussianBlur(18))
            overlay = Image.new("RGB", size, (245, 249, 254))
            fitted = Image.blend(bg, overlay, 0.46)
            contained = ImageOps.contain(img, (size[0] - 34, size[1] - 28), method=Image.Resampling.LANCZOS)
            px = (size[0] - contained.width) // 2
            py = (size[1] - contained.height) // 2
            fitted.paste(contained, (px, py))
    else:
        fitted = Image.new("RGB", size, (226, 238, 250))
    mask = rounded_mask(fitted.size, radius)
    card.paste(fitted, (x1, y1), mask)


def draw_panel(draw: ImageDraw.ImageDraw, box: tuple[int, int, int, int], title: str, body: str, accent, title_fnt=F_SUBTITLE, body_fnt=F_BODY):
    x1, y1, x2, y2 = box
    draw.rounded_rectangle(box, radius=28, fill=COLORS["panel"], outline=COLORS["border"], width=2)
    draw.rounded_rectangle((x1, y1, x1 + 16, y2), radius=8, fill=accent)
    draw.text((x1 + 34, y1 + 26), title, font=title_fnt, fill=COLORS["dark"])
    text_box(draw, (x1 + 34, y1 + 78), (x2 - x1 - 60, y2 - y1 - 94), body, body_fnt, fill=COLORS["dark"], line_gap=7, max_lines=4)


def base_card(spec: dict, side: str) -> tuple[Image.Image, ImageDraw.ImageDraw, tuple[int, int, int]]:
    accent = spec["color"]
    card = Image.new("RGB", (CARD_W, CARD_H), (255, 255, 255))
    d = ImageDraw.Draw(card)
    d.rounded_rectangle((18, 18, CARD_W - 18, CARD_H - 18), radius=64, fill=(255, 255, 255), outline=(167, 183, 204), width=4)
    d.rounded_rectangle((18, 18, CARD_W - 18, 118), radius=50, fill=accent)
    d.rectangle((18, 70, CARD_W - 18, 118), fill=accent)
    d.text((64, 45), spec["id"], font=F_ID, fill=(255, 255, 255))
    tag = spec["tag"] if side == "front" else spec.get("back_tag", "背面")
    tag_w = d.textlength(tag, font=F_TAG)
    d.text((CARD_W - 64 - tag_w, 50), tag, font=F_TAG, fill=(255, 255, 255))
    return card, d, accent


def draw_front(spec: dict) -> Image.Image:
    card, d, accent = base_card(spec, "front")
    title = spec["title"]
    d.text((64, 160), title, font=F_TITLE, fill=COLORS["dark"])
    text_box(d, (66, 224), (900, 58), spec["subtitle"], F_SMALL, fill=COLORS["gray"], max_lines=1)
    paste_illustration(card, ILLUSTRATIONS / f"{spec['id']}.png", (58, 292, CARD_W - 58, 1116), radius=36)
    modules = spec["front"]
    if len(modules) == 2:
        draw_panel(d, (58, 1152, 502, 1392), modules[0][0], modules[0][1], accent, F_SUBTITLE, F_SMALL)
        draw_panel(d, (548, 1152, 992, 1392), modules[1][0], modules[1][1], accent, F_SUBTITLE, F_SMALL)
    else:
        y = 1152
        for title_, body_ in modules[:3]:
            draw_panel(d, (58, y, 992, y + 118), title_, body_, accent, F_SMALL, F_SMALL)
            y += 132
    return card


def draw_back(spec: dict) -> Image.Image:
    card, d, accent = base_card(spec, "back")
    d.text((64, 150), spec["back_title"], font=F_TITLE, fill=COLORS["dark"])
    text_box(d, (66, 214), (900, 64), spec["back_subtitle"], F_SMALL, fill=COLORS["gray"], max_lines=2)
    paste_illustration(card, ILLUSTRATIONS / f"{spec['id']}.png", (58, 292, CARD_W - 58, 665), radius=32, mode="cover")
    modules = spec["back"]
    positions = [
        (58, 704, 502, 958),
        (548, 704, 992, 958),
        (58, 990, 502, 1244),
        (548, 990, 992, 1244),
    ]
    for pos, (title_, body_) in zip(positions, modules):
        draw_panel(d, pos, title_, body_, accent, F_SMALL, F_SMALL)
    return card


CARDS = [
    {
        "id": "E02",
        "tag": "低危事件",
        "back_tag": "复盘",
        "color": COLORS["low"],
        "title": "试剂瓶标签模糊",
        "subtitle": "物质身份无法确认，必须暂停核对。",
        "front": [
            ("风险摘要", "瓶签无法清楚识别，不能凭记忆、颜色或瓶身形状判断内容物。"),
            ("关键行动", "暂停使用；核对瓶签、台账、领用记录和负责人信息。"),
        ],
        "back_title": "正确处置与知识点",
        "back_subtitle": "标签不清不是小问题，而是未知物质风险。",
        "back": [
            ("正确处置", "先暂停，核对标签、记录和来源；无法确认时隔离并上报。"),
            ("原因", "名称、浓度、危险性或配制日期不清，都会导致误用。"),
            ("知识点", "不能用经验判断试剂身份；可追溯记录是安全底线。"),
            ("复盘问题", "如果你认为这是昨天配好的那瓶，是否可以直接使用？"),
        ],
    },
    {
        "id": "E05",
        "tag": "中危事件",
        "back_tag": "复盘",
        "color": COLORS["medium"],
        "title": "开放环境转移挥发性溶剂",
        "subtitle": "挥发暴露和火灾风险同时上升。",
        "front": [
            ("风险摘要", "在开放台面转移挥发性溶剂，蒸气可能积聚并被吸入。"),
            ("关键行动", "移入通风橱；控制暴露面积；远离热源和明火。"),
        ],
        "back_title": "正确处置与知识点",
        "back_subtitle": "通风控制优先于操作速度。",
        "back": [
            ("正确处置", "暂停转移，将操作移入通风橱，减少开口暴露时间。"),
            ("原因", "挥发性溶剂易形成吸入暴露，也可能造成可燃蒸气积聚。"),
            ("知识点", "通风橱是工程控制，不应被当作普通储物台使用。"),
            ("复盘问题", "如果只想快速倒完，是否可以不移入通风橱？"),
        ],
    },
    {
        "id": "E15",
        "tag": "高危事件",
        "back_tag": "复盘",
        "color": COLORS["high"],
        "title": "实验台出现小型明火",
        "subtitle": "人员安全优先，立即控制火源与暴露。",
        "front": [
            ("风险摘要", "明火已出现，继续操作或错误灭火都可能扩大事故。"),
            ("关键行动", "切断热源电源；撤离无关人员；按火源类型选择应急设施。"),
        ],
        "back_title": "正确处置与知识点",
        "back_subtitle": "高危事件中，停止推进任务是正确选择。",
        "back": [
            ("正确处置", "先判断火源和人员暴露，切断能量输入，必要时撤离上报。"),
            ("原因", "不明火源不能盲目用水；错误处置可能造成扩散或触电。"),
            ("知识点", "应急处置顺序是人员安全、控制能源、隔离风险、报告复盘。"),
            ("复盘问题", "什么时候可以自行处理，什么时候必须撤离并上报？"),
        ],
    },
    {
        "id": "T03",
        "tag": "任务牌",
        "back_tag": "任务说明",
        "color": COLORS["task"],
        "title": "加热回流装置搭建",
        "subtitle": "搭建并检查加热回流体系。",
        "front": [
            ("任务目标", "确认冷凝、夹具、热源和连接稳定，准备进入反应操作。"),
            ("推荐行动", "检查器材、固定连接、切断或调整热源。"),
        ],
        "back_title": "任务奖励与风险",
        "back_subtitle": "完成任务前先确认装置稳定。",
        "back": [
            ("完成奖励", "完整处置本轮风险后，实验进度 +1；装置稳定时额外贡献 +1。"),
            ("常见风险", "冷凝水管松动、夹具不稳、热源异常、玻璃器皿裂纹。"),
            ("教学提醒", "加热体系的风险来自热源、压力、玻璃和冷凝失效。"),
            ("复盘问题", "如果出现明火，本轮还应继续推进加热回流任务吗？"),
        ],
    },
    {
        "id": "A02",
        "tag": "行动牌",
        "back_tag": "行动边界",
        "color": COLORS["action"],
        "title": "核对标签",
        "subtitle": "确认瓶签、临时标签和记录一致。",
        "front": [
            ("用途", "用于处理标签不清、未知样品、记录不一致等风险。"),
            ("效果", "命中标签或未知物质风险时，可作为关键行动。"),
        ],
        "back_title": "适用场景与限制",
        "back_subtitle": "核对是安全判断的起点，不是所有风险的终点。",
        "back": [
            ("适用场景", "试剂瓶标签模糊、临时容器无标识、台账与实物不一致。"),
            ("岗位配合", "记录员使用时效果最佳，可引导补全台账。"),
            ("限制边界", "不能直接处理明火、泄漏、人员暴露或通风不足。"),
            ("协同行动", "可与记录台账、上报负责人、隔离现场组合使用。"),
        ],
    },
    {
        "id": "A08",
        "tag": "行动牌",
        "back_tag": "行动边界",
        "color": COLORS["action"],
        "title": "撤离与警戒",
        "subtitle": "撤离无关人员，限制进入风险区域。",
        "front": [
            ("用途", "用于高危事件、未知暴露、明火、泄漏或人员受伤风险。"),
            ("效果", "降低人员暴露；高危事件中常作为关键辅助行动。"),
        ],
        "back_title": "适用场景与限制",
        "back_subtitle": "撤离能保护人员，但不能单独清除风险源。",
        "back": [
            ("适用场景", "明火、未知粉末、强刺激气味、腐蚀性液体接触。"),
            ("岗位配合", "安全员使用时优先级最高，适合组织现场秩序。"),
            ("限制边界", "撤离后仍需要切断热源、围堵泄漏、上报或应急处理。"),
            ("协同行动", "常与切断热源电源、上报负责人、使用应急设施配合。"),
        ],
    },
    {
        "id": "P01",
        "tag": "岗位牌",
        "back_tag": "岗位能力",
        "color": COLORS["post"],
        "title": "安全员",
        "subtitle": "先判断人员安全，再决定是否推进任务。",
        "front": [
            ("岗位职责", "识别高危风险，组织隔离、撤离、上报和应急处置。"),
            ("发言优先级", "出现人员暴露、明火、未知气味或失控风险时，安全员先发言。"),
        ],
        "back_title": "能力与贡献",
        "back_subtitle": "安全员负责把风险控制放在任务进度之前。",
        "back": [
            ("岗位能力", "使用隔离、撤离、应急或上报类行动并控制风险时，贡献 +1。"),
            ("使用节奏", "高危事件先由安全员判断；低危事件不必过度上报。"),
            ("贡献规则", "完整处置高危事件时，安全员可额外贡献 +1。"),
            ("复盘问题", "本轮是否因为追求进度而忽略了人员安全？"),
        ],
    },
    {
        "id": "D02",
        "tag": "复盘牌",
        "back_tag": "知识点",
        "color": COLORS["debrief"],
        "title": "标签核对复盘",
        "subtitle": "未知物质不能凭经验使用。",
        "front": [
            ("知识主题", "试剂身份、浓度、危险性和配制日期必须可追溯。"),
            ("讨论提示", "标签不清时，正确动作是暂停、核对、隔离和上报。"),
        ],
        "back_title": "复盘提问",
        "back_subtitle": "把一次处置转化为下一次会做对的经验。",
        "back": [
            ("正确行动", "核对瓶签、台账、领用记录；不能确认则隔离并报告。"),
            ("原因", "错误识别试剂可能造成反应失控、暴露、污染或错误废液处理。"),
            ("延伸知识", "临时容器也需要二次标签，不能只靠操作者记忆。"),
            ("提问", "如果标签只剩一半，但你大概知道是什么，可以继续用吗？"),
        ],
    },
]


def add_bleed_marks(sheet: Image.Image) -> None:
    d = ImageDraw.Draw(sheet)
    margin = 80
    d.rectangle((margin, margin, A4_W - margin, A4_H - margin), outline=(220, 225, 232), width=2)


def make_sheet(paths: list[Path], out_path: Path) -> Path:
    sheet = Image.new("RGB", (A4_W, A4_H), (255, 255, 255))
    add_bleed_marks(sheet)
    cols, rows = 2, 4
    target_w, target_h = 980, 1372
    gap_x = 150
    gap_y = 22
    start_x = int((A4_W - cols * target_w - gap_x) / 2)
    start_y = 65
    for idx, p in enumerate(paths[:8]):
        img = Image.open(p).convert("RGB")
        img = img.resize((target_w, target_h), Image.Resampling.LANCZOS)
        col = idx % cols
        row = idx // cols
        x = start_x + col * (target_w + gap_x)
        y = start_y + row * (target_h + gap_y)
        sheet.paste(img, (x, y))
    sheet.save(out_path, quality=95)
    return out_path


def main() -> dict:
    CARD_DIR.mkdir(parents=True, exist_ok=True)
    SHEET_DIR.mkdir(parents=True, exist_ok=True)
    MATERIAL_DIR.mkdir(parents=True, exist_ok=True)

    front_paths: list[Path] = []
    back_paths: list[Path] = []
    for spec in CARDS:
        front = draw_front(spec)
        back = draw_back(spec)
        front_path = CARD_DIR / f"{spec['id']}_front.png"
        back_path = CARD_DIR / f"{spec['id']}_back.png"
        front.save(front_path, quality=95)
        back.save(back_path, quality=95)
        front_paths.append(front_path)
        back_paths.append(back_path)

    front_sheet = make_sheet(front_paths, SHEET_DIR / "sample_cards_front_A4.png")
    back_sheet = make_sheet(back_paths, SHEET_DIR / "sample_cards_back_A4.png")

    pdf_path = SHEET_DIR / "sample_cards_print_sheets.pdf"
    front_img = Image.open(front_sheet).convert("RGB")
    back_img = Image.open(back_sheet).convert("RGB")
    front_img.save(pdf_path, save_all=True, append_images=[back_img], resolution=300.0)

    for src in [
        ROOT / "manual" / "实验室安全值班_v2_详细玩法说明_可直接开局.md",
        ROOT / "manual" / "实验室安全值班_v2_4分钟现场演讲稿.md",
    ]:
        if src.exists():
            shutil.copy2(src, MATERIAL_DIR / src.name)

    return {
        "cards": len(front_paths),
        "fronts": [str(p) for p in front_paths],
        "backs": [str(p) for p in back_paths],
        "front_sheet": str(front_sheet),
        "back_sheet": str(back_sheet),
        "pdf": str(pdf_path),
        "material_dir": str(MATERIAL_DIR),
    }


if __name__ == "__main__":
    import json

    print(json.dumps(main(), ensure_ascii=False, indent=2))
