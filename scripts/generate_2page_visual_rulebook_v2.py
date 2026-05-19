from __future__ import annotations

import shutil
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont, ImageOps


ROOT = Path(__file__).resolve().parents[1]
ILLUSTRATIONS = ROOT / "card" / "final" / "v2" / "generated_illustrations"
OUT = ROOT / "manual" / "visual_rulebook_v2"
MATERIAL_DIR = ROOT / "card" / "final" / "v2" / "参赛文件" / "08_现场可用材料"
W, H = 2480, 3508

BLUE = (22, 58, 112)
MID = (64, 127, 216)
GREEN = (47, 164, 143)
ORANGE = (240, 160, 58)
RED = (206, 86, 78)
DARK = (28, 38, 54)
GRAY = (86, 98, 116)
PANEL = (247, 250, 255)
BG = (248, 251, 255)


def font(size: int, bold: bool = False) -> ImageFont.FreeTypeFont:
    for p in [
        Path(r"C:\Windows\Fonts\msyhbd.ttc" if bold else r"C:\Windows\Fonts\msyh.ttc"),
        Path(r"C:\Windows\Fonts\simhei.ttf"),
        Path(r"C:\Windows\Fonts\simsun.ttc"),
    ]:
        if p.exists():
            return ImageFont.truetype(str(p), size)
    return ImageFont.load_default()


F_TITLE = font(88, True)
F_HEAD = font(52, True)
F_BODY = font(38)
F_SMALL = font(30)
F_NUM = font(64, True)


def wrap(text: str, draw: ImageDraw.ImageDraw, fnt: ImageFont.FreeTypeFont, max_w: int) -> list[str]:
    lines, cur = [], ""
    for ch in text:
        test = cur + ch
        if draw.textlength(test, font=fnt) <= max_w or not cur:
            cur = test
        else:
            lines.append(cur)
            cur = ch
    if cur:
        lines.append(cur)
    return lines


def draw_text(draw: ImageDraw.ImageDraw, text: str, x: int, y: int, max_w: int, fnt, fill=DARK, gap=12) -> int:
    for line in wrap(text, draw, fnt, max_w):
        draw.text((x, y), line, font=fnt, fill=fill)
        y += fnt.size + gap
    return y


def paste_img(page: Image.Image, cid: str, box: tuple[int, int, int, int]) -> None:
    x1, y1, x2, y2 = box
    p = ILLUSTRATIONS / f"{cid}.png"
    img = Image.open(p).convert("RGB") if p.exists() else Image.new("RGB", (800, 1200), (230, 240, 250))
    fitted = ImageOps.fit(img, (x2 - x1, y2 - y1), method=Image.Resampling.LANCZOS, centering=(0.5, 0.36))
    mask = Image.new("L", fitted.size, 0)
    ImageDraw.Draw(mask).rounded_rectangle((0, 0, fitted.width - 1, fitted.height - 1), radius=46, fill=255)
    page.paste(fitted, (x1, y1), mask)


def panel(draw: ImageDraw.ImageDraw, box, title, body, color):
    x1, y1, x2, y2 = box
    draw.rounded_rectangle(box, radius=42, fill=PANEL, outline=(210, 224, 240), width=3)
    draw.rounded_rectangle((x1, y1, x1 + 24, y2), radius=12, fill=color)
    draw.text((x1 + 55, y1 + 38), title, font=F_HEAD, fill=color)
    draw_text(draw, body, x1 + 55, y1 + 112, x2 - x1 - 100, F_BODY, DARK)


def step(draw: ImageDraw.ImageDraw, n: str, title: str, body: str, x: int, y: int, color):
    draw.ellipse((x, y, x + 95, y + 95), fill=color)
    draw.text((x + 31, y + 14), n, font=F_NUM, fill=(255, 255, 255))
    draw.text((x + 125, y + 3), title, font=F_HEAD, fill=BLUE)
    draw_text(draw, body, x + 125, y + 68, 850, F_SMALL, GRAY, gap=8)


def page1() -> Image.Image:
    page = Image.new("RGB", (W, H), BG)
    d = ImageDraw.Draw(page)
    d.text((140, 125), "《实验室安全值班》怎么玩", font=F_TITLE, fill=BLUE)
    d.text((145, 235), "2-4人｜20-30分钟｜协作完成实验并控制风险", font=F_BODY, fill=GRAY)
    paste_img(page, "E02", (145, 420, 880, 1525))
    paste_img(page, "E15", (930, 420, 1665, 1525))
    paste_img(page, "T03", (1715, 420, 2340, 1525))
    panel(d, (145, 1650, 1140, 2155), "目标", "8轮内让实验进度达标，同时保持安全值大于0、事故等级和隐患不超限。", MID)
    panel(d, (1245, 1650, 2340, 2155), "你会做什么", "翻任务、遇事件、按岗位讨论行动，最后复盘为什么这样处置。", GREEN)
    step(d, "1", "看任务", "明确本轮实验原本要推进什么。", 165, 2350, MID)
    step(d, "2", "翻事件", "判断风险等级和当前状态。", 165, 2585, ORANGE)
    step(d, "3", "打行动", "选择关键行动和辅助行动。", 1245, 2350, GREEN)
    step(d, "4", "做复盘", "读知识点，回答复盘问题。", 1245, 2585, RED)
    d.text((145, 3260), "一句话：先控风险，再推进实验；团队共同胜负。", font=F_HEAD, fill=BLUE)
    return page


def page2() -> Image.Image:
    page = Image.new("RGB", (W, H), BG)
    d = ImageDraw.Draw(page)
    d.text((140, 125), "一轮示例：小型明火", font=F_TITLE, fill=BLUE)
    d.text((145, 235), "演示时用这组牌最直观：T03 + E15 + A08 + P01", font=F_BODY, fill=GRAY)
    paste_img(page, "P01", (145, 420, 830, 1445))
    paste_img(page, "A08", (900, 420, 1585, 1445))
    paste_img(page, "D02", (1655, 420, 2340, 1445))
    panel(d, (145, 1580, 760, 2130), "岗位", "安全员先判断人员暴露，决定是否撤离、警戒和上报。", MID)
    panel(d, (930, 1580, 1545, 2130), "行动", "出现明火时，切断热源，撤离无关人员，按火源类型应急。", RED)
    panel(d, (1715, 1580, 2340, 2130), "复盘", "为什么不能盲目用水？什么时候必须撤离并上报？", GREEN)
    d.text((145, 2340), "胜利条件", font=F_HEAD, fill=BLUE)
    draw_text(d, "实验进度达标，且安全值、事故等级、隐患池都没有越线。", 145, 2425, 950, F_BODY, DARK)
    d.text((1245, 2340), "失败条件", font=F_HEAD, fill=RED)
    draw_text(d, "安全值归零、事故等级过高、隐患堆积，或8轮后进度不足。", 1245, 2425, 950, F_BODY, DARK)
    d.rounded_rectangle((145, 2900, 2340, 3260), radius=46, fill=(235, 245, 255), outline=(202, 218, 238), width=3)
    d.text((235, 2990), "主持人提示：每轮只问三件事——风险是什么？先做什么？为什么？", font=F_HEAD, fill=BLUE)
    return page


def main() -> dict:
    OUT.mkdir(parents=True, exist_ok=True)
    MATERIAL_DIR.mkdir(parents=True, exist_ok=True)
    p1 = page1()
    p2 = page2()
    p1_path = OUT / "visual_rulebook_page1.png"
    p2_path = OUT / "visual_rulebook_page2.png"
    pdf_path = OUT / "实验室安全值班_v2_2页彩图说明书.pdf"
    md_path = ROOT / "manual" / "实验室安全值班_v2_2页彩图说明书_文字源.md"
    p1.save(p1_path, quality=95)
    p2.save(p2_path, quality=95)
    p1.save(pdf_path, save_all=True, append_images=[p2], resolution=300.0)
    md_path.write_text(
        "# 《实验室安全值班》v2 2页彩图说明书文字源\n\n"
        "第1页：2-4人，20-30分钟。团队在8轮内推进实验进度，同时保持安全值大于0、事故等级和隐患不超限。每轮按“看任务、翻事件、打行动、做复盘”进行。核心原则：先控风险，再推进实验；团队共同胜负。\n\n"
        "第2页：演示组合为T03加热回流、E15小型明火、A08撤离与警戒、P01安全员。安全员先判断人员暴露，团队切断热源、撤离无关人员并按火源类型应急。复盘时回答：为什么不能盲目用水，什么时候必须撤离并上报。\n",
        encoding="utf-8",
    )
    for p in [p1_path, p2_path, pdf_path, md_path]:
        shutil.copy2(p, MATERIAL_DIR / p.name)
    return {
        "page1": str(p1_path),
        "page2": str(p2_path),
        "pdf": str(pdf_path),
        "source": str(md_path),
        "material_dir": str(MATERIAL_DIR),
    }


if __name__ == "__main__":
    import json

    print(json.dumps(main(), ensure_ascii=False, indent=2))
