from __future__ import annotations

import csv
import json
import shutil
import zipfile
from datetime import datetime
from pathlib import Path
from typing import Iterable

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from PIL import Image, ImageDraw, ImageFont
from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_LEFT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import cm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import Image as RLImage
from reportlab.platypus import PageBreak, Paragraph, SimpleDocTemplate, Spacer, Table, TableStyle


ROOT = Path(__file__).resolve().parents[1]
OUTPUT_ROOT = ROOT / "output" / "v2_submission_package"
PDF_DIR = OUTPUT_ROOT / "pdf"
CHART_DIR = OUTPUT_ROOT / "charts"
TMP_DIR = OUTPUT_ROOT / "tmp"

PACKAGE_NAME = "《实验室安全值班》v2化学实验室安全情境协作桌游-2501110475-赵成博_提交版"
SUBMISSION_DIR = ROOT / "submission" / PACKAGE_NAME
ZIP_PATH = ROOT / "submission" / f"{PACKAGE_NAME}.zip"

OLD_SUBMISSION_DIR = ROOT / "submission" / "《实验室安全值班》化学实验室安全情境协作桌游-2501110475-赵成博_作者简介修订版"
OLD_PROMO_VIDEO = OLD_SUBMISSION_DIR / "02_宣传视频.mp4"
ILLUSTRATION_DIR = ROOT / "card" / "final" / "v2" / "generated_illustrations"

AUTHOR_INFO = {
    "姓名": "赵成博",
    "学号": "2501110475",
    "联系电话": "17615805216",
    "电子邮箱": "17615805216@163.com",
    "作者简介": (
        "北京大学化学与分子工程学院2025级博士研究生，严纯化老师课题组，"
        "目前的研究方向是机器学习在稀土纳米材料合成中的应用。"
    ),
}

WORK_TITLE = "《实验室安全值班》v2"
WORK_SUBTITLE = "化学实验室安全情境协作桌游"
WORK_DESCRIPTION = (
    "《实验室安全值班》v2 是一套面向化学实验室安全教育的协作式桌游。"
    "玩家在 20-30 分钟内通过岗位轮值、实验任务推进、风险事件处置和复盘知识点，"
    "模拟一次从实验准备到操作、收尾和应急判断的安全训练。"
    "作品希望把抽象安全规范转化为具体情境中的判断、沟通和处置。"
)

FONT_REGULAR_PATHS = [
    Path(r"C:\Windows\Fonts\msyh.ttc"),
    Path(r"C:\Windows\Fonts\simhei.ttf"),
    Path(r"C:\Windows\Fonts\simsun.ttc"),
]
FONT_BOLD_PATHS = [
    Path(r"C:\Windows\Fonts\msyhbd.ttc"),
    Path(r"C:\Windows\Fonts\simhei.ttf"),
    Path(r"C:\Windows\Fonts\simsunb.ttf"),
]


def register_fonts() -> dict[str, str]:
    regular_path = next(path for path in FONT_REGULAR_PATHS if path.exists())
    bold_path = next(path for path in FONT_BOLD_PATHS if path.exists())
    pdfmetrics.registerFont(TTFont("CN-Regular", str(regular_path)))
    pdfmetrics.registerFont(TTFont("CN-Bold", str(bold_path)))
    return {"regular": "CN-Regular", "bold": "CN-Bold"}


def styles(fonts: dict[str, str]) -> dict[str, ParagraphStyle]:
    base = getSampleStyleSheet()
    return {
        "title": ParagraphStyle(
            "title",
            parent=base["Title"],
            fontName=fonts["bold"],
            fontSize=22,
            leading=30,
            alignment=TA_CENTER,
            textColor=colors.HexColor("#163A70"),
            wordWrap="CJK",
            spaceAfter=8,
        ),
        "subtitle": ParagraphStyle(
            "subtitle",
            parent=base["Normal"],
            fontName=fonts["regular"],
            fontSize=11,
            leading=16,
            alignment=TA_CENTER,
            textColor=colors.HexColor("#43526B"),
            wordWrap="CJK",
            spaceAfter=10,
        ),
        "heading": ParagraphStyle(
            "heading",
            parent=base["Heading2"],
            fontName=fonts["bold"],
            fontSize=14,
            leading=20,
            textColor=colors.HexColor("#183A72"),
            wordWrap="CJK",
            spaceBefore=8,
            spaceAfter=6,
        ),
        "body": ParagraphStyle(
            "body",
            parent=base["BodyText"],
            fontName=fonts["regular"],
            fontSize=10.5,
            leading=15.5,
            textColor=colors.HexColor("#1E2635"),
            alignment=TA_LEFT,
            wordWrap="CJK",
        ),
        "small": ParagraphStyle(
            "small",
            parent=base["BodyText"],
            fontName=fonts["regular"],
            fontSize=9,
            leading=13,
            textColor=colors.HexColor("#455064"),
            alignment=TA_LEFT,
            wordWrap="CJK",
        ),
    }


def para(text: str, style: ParagraphStyle) -> Paragraph:
    return Paragraph(text.replace("\n", "<br/>"), style)


def safe_rmtree(path: Path) -> None:
    resolved = path.resolve()
    allowed = (ROOT / "submission").resolve()
    if not str(resolved).lower().startswith(str(allowed).lower()):
        raise RuntimeError(f"Refuse to remove outside submission directory: {resolved}")
    if resolved.exists():
        shutil.rmtree(resolved)


def ensure_dirs() -> None:
    for path in [PDF_DIR, CHART_DIR, TMP_DIR, SUBMISSION_DIR]:
        path.mkdir(parents=True, exist_ok=True)


def image_files() -> list[Path]:
    if not ILLUSTRATION_DIR.exists():
        return []
    exts = {".png", ".jpg", ".jpeg", ".webp"}
    return sorted(path for path in ILLUSTRATION_DIR.iterdir() if path.is_file() and path.suffix.lower() in exts)


def card_counts() -> dict[str, int]:
    obj = json.loads((ROOT / "content" / "v2_cards.json").read_text(encoding="utf-8"))
    cards = obj["cards"] if isinstance(obj, dict) else obj
    counts = {"task": 0, "event": 0, "action": 0, "role": 0, "post": 0, "strategy": 0, "debrief": 0}
    for card in cards:
        counts[card["card_type"]] += 1
    counts["total"] = len(cards)
    return counts


def load_longrun_stats() -> tuple[list[dict], dict[str, dict]]:
    summary_path = ROOT / "data" / "v2" / "run_009_v2_prefinal_longrun" / "summary.json"
    data = json.loads(summary_path.read_text(encoding="utf-8"))
    rows = data["scenario_stats"]
    no_strategy = {row["mode"]: row for row in rows if row["strategy_id"] == "none"}
    return rows, no_strategy


def make_winrate_chart(no_strategy: dict[str, dict]) -> Path:
    path = CHART_DIR / "v2_winrate_by_mode.png"
    modes = ["teaching", "standard", "challenge"]
    labels = ["Teaching", "Standard", "Challenge"]
    values = [no_strategy[mode]["win_rate"] * 100 for mode in modes]
    colors_ = ["#3F7FD8", "#2FA48F", "#F0A13A"]
    plt.figure(figsize=(6.4, 3.2), dpi=180)
    bars = plt.bar(labels, values, color=colors_)
    plt.ylim(0, 100)
    plt.ylabel("Win rate (%)")
    plt.title("v2 long-run baseline")
    for bar, value in zip(bars, values):
        plt.text(bar.get_x() + bar.get_width() / 2, value + 2, f"{value:.1f}%", ha="center", fontsize=9)
    plt.tight_layout()
    plt.savefig(path)
    plt.close()
    return path


def make_card_count_chart(counts: dict[str, int]) -> Path:
    path = CHART_DIR / "v2_card_counts.png"
    labels = ["Task", "Event", "Action", "Role", "Post", "Strategy", "Debrief"]
    keys = ["task", "event", "action", "role", "post", "strategy", "debrief"]
    values = [counts[key] for key in keys]
    plt.figure(figsize=(7.2, 3.2), dpi=180)
    plt.bar(labels, values, color="#5A8BD8")
    plt.ylabel("Cards")
    plt.title("v2 card pool: 120 cards")
    for idx, value in enumerate(values):
        plt.text(idx, value + 0.8, str(value), ha="center", fontsize=9)
    plt.tight_layout()
    plt.savefig(path)
    plt.close()
    return path


def make_contact_sheet(images: list[Path]) -> Path | None:
    if not images:
        return None
    thumb_w, thumb_h = 160, 240
    label_h = 28
    cols = 8
    rows = (len(images) + cols - 1) // cols
    sheet = Image.new("RGB", (cols * thumb_w, rows * (thumb_h + label_h)), "#F4F6F8")
    draw = ImageDraw.Draw(sheet)
    font_path = next((path for path in FONT_BOLD_PATHS if path.exists()), None)
    font = ImageFont.truetype(str(font_path), 18) if font_path else ImageFont.load_default()
    for idx, path in enumerate(images):
        image = Image.open(path).convert("RGB")
        image.thumbnail((thumb_w, thumb_h), Image.Resampling.LANCZOS)
        col = idx % cols
        row = idx // cols
        x = col * thumb_w + (thumb_w - image.width) // 2
        y = row * (thumb_h + label_h)
        sheet.paste(image, (x, y))
        label = path.stem
        bbox = draw.textbbox((0, 0), label, font=font)
        draw.text((col * thumb_w + (thumb_w - (bbox[2] - bbox[0])) / 2, y + thumb_h + 4), label, fill="#26313F", font=font)
    out = TMP_DIR / "generated_illustrations_contact_sheet.jpg"
    sheet.save(out, quality=92)
    return out


def build_pdf(path: Path, story: list, title: str) -> None:
    doc = SimpleDocTemplate(
        str(path),
        pagesize=A4,
        rightMargin=1.6 * cm,
        leftMargin=1.6 * cm,
        topMargin=1.5 * cm,
        bottomMargin=1.5 * cm,
        title=title,
        author="赵成博",
    )
    doc.build(story)


def fit_image(path: Path, *, max_width: float, max_height: float) -> RLImage:
    with Image.open(path) as image:
        width, height = image.size
    scale = min(max_width / width, max_height / height)
    return RLImage(str(path), width=width * scale, height=height * scale)


def info_table(rows: Iterable[tuple[str, str]], style: dict[str, ParagraphStyle]) -> Table:
    data = [[para(k, style["small"]), para(v, style["small"])] for k, v in rows]
    table = Table(data, colWidths=[3.0 * cm, 13.0 * cm])
    table.setStyle(
        TableStyle(
            [
                ("GRID", (0, 0), (-1, -1), 0.35, colors.HexColor("#CAD4E2")),
                ("BACKGROUND", (0, 0), (0, -1), colors.HexColor("#EAF2FF")),
                ("VALIGN", (0, 0), (-1, -1), "TOP"),
                ("LEFTPADDING", (0, 0), (-1, -1), 6),
                ("RIGHTPADDING", (0, 0), (-1, -1), 6),
                ("TOPPADDING", (0, 0), (-1, -1), 5),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
            ]
        )
    )
    return table


def build_author_pdf(style: dict[str, ParagraphStyle]) -> Path:
    path = PDF_DIR / "00a_作者信息与作品文字说明.pdf"
    story = [
        para("作者信息与作品文字说明", style["title"]),
        para(f"{WORK_TITLE}：{WORK_SUBTITLE}", style["subtitle"]),
        para("一、作者信息", style["heading"]),
        info_table(AUTHOR_INFO.items(), style),
        Spacer(1, 0.35 * cm),
        para("二、作品文字说明", style["heading"]),
        para(WORK_DESCRIPTION, style["body"]),
        Spacer(1, 0.2 * cm),
        para(
            "v2 版本在 v1.0 初赛原型基础上进行成熟化重构：卡牌数量扩展为 120 张，核心循环改为实验任务层、风险处置层和岗位协作层，"
            "并加入风险状态、岗位轮值、交接链、个人贡献分和复盘牌。当前提交包暂使用已生成的无文字插画样张，未等待全部 120 张插画完成。",
            style["body"],
        ),
        Spacer(1, 0.2 * cm),
        para("三、比赛提交说明", style["heading"]),
        para(
            "提交包文件名已按“作品名称-学号-姓名”组织；本页包含作者姓名、学号、联系电话、电子邮箱、作者简介和作品文字说明。",
            style["body"],
        ),
    ]
    build_pdf(path, story, "作者信息与作品文字说明")
    return path


def build_overview_pdf(style: dict[str, ParagraphStyle], contact_sheet: Path | None, no_strategy: dict[str, dict], image_count: int) -> Path:
    path = PDF_DIR / "00_请先看这里_作品总览.pdf"
    standard = no_strategy["standard"]
    story = [
        para(f"{WORK_TITLE}", style["title"]),
        para(WORK_SUBTITLE, style["subtitle"]),
        para("作品一句话定义", style["heading"]),
        para(
            "一套面向化学实验室安全教育的中量协作桌游，通过任务推进、风险事件、岗位协作和知识复盘，把安全规范转化为可讨论、可演练的情境决策。",
            style["body"],
        ),
        para("先看什么", style["heading"]),
        info_table(
            [
                ("00a", "作者信息与作品文字说明：满足比赛提交要求。"),
                ("01", "一页玩法速览：评委可快速理解一局怎么进行。"),
                ("02", "宣传视频：沿用前版短片，用于快速理解主题。"),
                ("03", "版本迭代与关键数据：展示 v2 规则、规模和平衡结果。"),
                ("04", "使用手册：面向玩家和老师的规则说明。"),
                ("05", "已生成卡牌插画：当前已生成的无文字水彩卡图样张。"),
                ("06", "版本数据附录：结构化牌池、长跑摘要、AI 代理试玩记录等。"),
            ],
            style,
        ),
        Spacer(1, 0.3 * cm),
        para("当前 v2 状态", style["heading"]),
        para(
            f"v2 结构化牌池共 120 张卡；本提交包已纳入当前生成目录中的 {image_count} 张无文字插画。"
            f"最终长跑模拟共 270000 局；无策略标准模式胜率为 {standard['win_rate'] * 100:.2f}%，平均知识点触发数为 {standard['avg_knowledge_count']:.2f}。",
            style["body"],
        ),
    ]
    if contact_sheet and contact_sheet.exists():
        story.append(Spacer(1, 0.25 * cm))
        story.append(para("当前已生成插画总览", style["heading"]))
        story.append(fit_image(contact_sheet, max_width=17.0 * cm, max_height=20.0 * cm))
    build_pdf(path, story, "作品总览")
    return path


def build_quickstart_pdf(style: dict[str, ParagraphStyle]) -> Path:
    path = PDF_DIR / "01_一页玩法速览.pdf"
    story = [
        para("一页玩法速览", style["title"]),
        para("给不熟悉桌游的评委和老师看的 3 分钟说明", style["subtitle"]),
        para("基本信息", style["heading"]),
        info_table(
            [
                ("人数", "建议 2-4 人协作游玩。"),
                ("时长", "单局约 20-30 分钟。"),
                ("定位", "化学实验室安全培训桌游，不是知识问答卡。"),
                ("目标", "在安全值没有归零、事故等级没有失控、隐患没有溢出的前提下完成实验进度。"),
            ],
            style,
        ),
        para("每轮 6 步", style["heading"]),
        para("1. 岗位轮值：玩家分别承担安全员、操作者、记录员、资源管理员等职责。", style["body"]),
        para("2. 翻开任务：决定本轮实验推进目标。", style["body"]),
        para("3. 触发事件：出现标签、通风、加热、废液、泄漏等实验室安全情境。", style["body"]),
        para("4. 选择行动：玩家根据岗位和风险状态选择防护、核对、通风、停机、隔离、上报等行动。", style["body"]),
        para("5. 结算状态：风险可能被控制、勉强维持、恶化或进入交接链。", style["body"]),
        para("6. 复盘知识点：对应复盘牌解释正确处置、原因和反思问题。", style["body"]),
        para("为什么适合实验室安全教育", style["heading"]),
        para(
            "它把“记住规范”变成“面对具体情境做选择”：学生需要判断优先级，说明为什么这么做，并在复盘中把操作选择和安全知识点对应起来。",
            style["body"],
        ),
    ]
    build_pdf(path, story, "一页玩法速览")
    return path


def build_data_pdf(style: dict[str, ParagraphStyle], counts: dict[str, int], no_strategy: dict[str, dict], win_chart: Path, count_chart: Path, image_count: int) -> Path:
    path = PDF_DIR / "03_v2版本迭代与关键数据.pdf"
    rows, _ = load_longrun_stats()
    total_games = sum(row["games"] for row in rows)
    strategy_rates = [row["win_rate"] for row in rows if row["mode"] == "standard"]
    story = [
        para("v2 版本迭代与关键数据", style["title"]),
        para("只展示评委最需要看的关键指标，完整数据见附录。", style["subtitle"]),
        para("v2 相比 v1.0 的主要变化", style["heading"]),
        info_table(
            [
                ("规则结构", "从单回合事件响应升级为任务层、风险层、岗位层三层循环。"),
                ("风险表现", "从一次性成功/失败升级为苗头、暴露、失控等状态。"),
                ("协作方式", "加入岗位轮值、交接链和个人贡献分。"),
                ("内容规模", "v2 结构化牌池扩展为 120 张。"),
                ("美术状态", f"当前提交包纳入 {image_count} 张已生成无文字插画，其余可继续按提示词批量补齐。"),
            ],
            style,
        ),
        para("牌池规模", style["heading"]),
        info_table(
            [
                ("任务牌", str(counts["task"])),
                ("事件牌", str(counts["event"])),
                ("行动牌", str(counts["action"])),
                ("角色牌", str(counts["role"])),
                ("岗位牌", str(counts["post"])),
                ("策略牌", str(counts["strategy"])),
                ("复盘牌", str(counts["debrief"])),
                ("合计", str(counts["total"])),
            ],
            style,
        ),
        Spacer(1, 0.2 * cm),
        RLImage(str(count_chart), width=15.5 * cm, height=6.9 * cm),
        PageBreak(),
        para("最终长跑平衡数据", style["heading"]),
        para(f"最终长跑目录：data/v2/run_009_v2_prefinal_longrun/。共 {total_games} 局模拟。", style["body"]),
        info_table(
            [
                ("教学模式", f"{no_strategy['teaching']['win_rate'] * 100:.2f}%"),
                ("标准模式", f"{no_strategy['standard']['win_rate'] * 100:.2f}%"),
                ("挑战模式", f"{no_strategy['challenge']['win_rate'] * 100:.2f}%"),
                ("标准模式策略范围", f"{min(strategy_rates) * 100:.2f}%-{max(strategy_rates) * 100:.2f}%"),
                ("标准模式平均知识点", f"{no_strategy['standard']['avg_knowledge_count']:.2f} 个/局"),
            ],
            style,
        ),
        Spacer(1, 0.25 * cm),
        RLImage(str(win_chart), width=15.5 * cm, height=7.6 * cm),
        para("数据解释", style["heading"]),
        para(
            "教学模式胜率较高，适合新手入门；标准模式保留压力但多数情况下可通过协作获胜；挑战模式胜率下降，适合作为熟悉规则后的提高难度。",
            style["body"],
        ),
    ]
    build_pdf(path, story, "v2 版本迭代与关键数据")
    return path


def build_manual_pdf(style: dict[str, ParagraphStyle]) -> Path:
    path = PDF_DIR / "04_使用手册.pdf"
    story = [
        para("使用手册", style["title"]),
        para("玩家规则 + 教师带玩提示 + 评审说明摘要", style["subtitle"]),
        para("一、开局准备", style["heading"]),
        para("选择模式和策略，发放角色牌，准备任务牌、事件牌、行动牌、岗位牌和复盘牌。玩家明确本局胜负条件，并约定每轮按岗位顺序发言。", style["body"]),
        para("二、核心组件", style["heading"]),
        para("任务牌决定实验推进目标；事件牌制造安全情境；行动牌提供处置方式；岗位牌规定本轮职责；复盘牌把事件和安全知识点对应起来。", style["body"]),
        para("三、行动选择", style["heading"]),
        para("关键行动直接针对风险源，辅助行动提高成功率或补充证据，冲突行动可能让风险恶化。玩家应先判断风险状态，再决定是否继续推进任务。", style["body"]),
        para("四、交接链", style["heading"]),
        para("如果本轮隐患没有被处理干净，它会进入下一轮并影响岗位和任务。该机制用于模拟真实实验中“上一班留下的问题会影响下一班”的管理逻辑。", style["body"]),
        para("五、教学复盘", style["heading"]),
        para("每个事件对应复盘知识点。教师可追问：风险源是什么、为什么这个行动优先、如果现实中遇到该情况应该先报告谁、哪些信息必须记录。", style["body"]),
        para("六、当前美术说明", style["heading"]),
        para("本提交包暂收录当前已生成的无文字插画。所有中文标题和规则说明应后期排版，避免图像模型直接生成中文导致不清晰。", style["body"]),
    ]
    build_pdf(path, story, "使用手册")
    return path


def copy_appendix_files(target: Path) -> None:
    target.mkdir(parents=True, exist_ok=True)
    files = {
        ROOT / "content" / "v2_cards.json": "v2_cards.json",
        ROOT / "boardgame_v2.0.md": "boardgame_v2.0.md",
        ROOT / "manual" / "judge_brief_v2.md": "judge_brief_v2.md",
        ROOT / "manual" / "player_rulebook_v2.md": "player_rulebook_v2.md",
        ROOT / "manual" / "quick_reference_v2.md": "quick_reference_v2.md",
        ROOT / "manual" / "teaching_guide_v2.md": "teaching_guide_v2.md",
        ROOT / "docs" / "v2_balance_report.md": "v2_balance_report.md",
        ROOT / "docs" / "v2_sample_playthrough_standard.md": "v2_sample_playthrough_standard.md",
        ROOT / "docs" / "v2_ai_agent_playtest_findings.md": "v2_ai_agent_playtest_findings.md",
        ROOT / "docs" / "v2_ai_agent_playtest_protocol.md": "v2_ai_agent_playtest_protocol.md",
        ROOT / "docs" / "v2_120_card_image_generation_guide.md": "v2_120_card_image_generation_guide.md",
        ROOT / "data" / "v2" / "run_009_v2_prefinal_longrun" / "summary.json": "run_009_v2_prefinal_longrun_summary.json",
        ROOT / "data" / "v2" / "run_009_v2_prefinal_longrun" / "turn_logs.csv": "run_009_v2_prefinal_longrun_turn_logs.csv",
        ROOT / "data" / "v2" / "run_011_demo_standard_selected" / "summary.json": "run_011_demo_standard_selected_summary.json",
        ROOT / "data" / "v2" / "run_011_demo_standard_selected" / "turn_logs.csv": "run_011_demo_standard_selected_turn_logs.csv",
        ROOT / "data" / "v2" / "ai_agent_playtests" / "agent_playtest_20260428_round01.md": "agent_playtest_20260428_round01.md",
    }
    for source, name in files.items():
        if source.exists():
            shutil.copy2(source, target / name)

    # Keep a compact CSV sample so the package stays upload-friendly while retaining evidence.
    source_csv = ROOT / "data" / "v2" / "run_009_v2_prefinal_longrun" / "game_results.csv"
    sample_csv = target / "run_009_game_results_first_500_rows.csv"
    if source_csv.exists():
        with source_csv.open("r", encoding="utf-8-sig", newline="") as src, sample_csv.open("w", encoding="utf-8-sig", newline="") as dst:
            reader = csv.reader(src)
            writer = csv.writer(dst)
            for idx, row in enumerate(reader):
                writer.writerow(row)
                if idx >= 500:
                    break

    note = target / "00_数据附录说明.txt"
    note.write_text(
        "本目录保留 v2 结构化牌池、规则文档、平衡报告、最终长跑 summary、示例战报和 AI 代理试玩记录。"
        "为控制提交包大小，270000 局 game_results.csv 未全量复制，只保留前 500 行样例；完整原始文件位于项目 data/v2/run_009_v2_prefinal_longrun/。\n",
        encoding="utf-8",
    )


def copy_illustrations(target: Path, images: list[Path], contact_sheet: Path | None) -> None:
    target.mkdir(parents=True, exist_ok=True)
    for path in images:
        shutil.copy2(path, target / path.name)
    progress = ILLUSTRATION_DIR / "progress.md"
    if progress.exists():
        shutil.copy2(progress, target / "progress.md")
    if contact_sheet and contact_sheet.exists():
        shutil.copy2(contact_sheet, target / "00_当前已生成插画总览.jpg")
    ids = [path.stem for path in images]
    (target / "00_当前已生成插画清单.txt").write_text(
        "当前提交包使用已生成插画，不等待全 120 张完成。\n"
        f"已收录数量：{len(ids)}\n"
        "已收录卡牌：\n"
        + "\n".join(ids)
        + "\n",
        encoding="utf-8",
    )


def copy_video(target: Path) -> None:
    if OLD_PROMO_VIDEO.exists():
        shutil.copy2(OLD_PROMO_VIDEO, target / "02_宣传视频.mp4")
        (target / "02_宣传视频说明.txt").write_text(
            "本视频沿用前一版宣传短片，用于帮助评委快速理解作品主题。v2 的主要更新体现在规则、牌池、数据和当前已生成插画中。\n",
            encoding="utf-8",
        )
    else:
        (target / "02_宣传视频说明.txt").write_text(
            "当前环境未找到可复制的宣传视频。本提交包以 PDF 说明、数据附录和已生成插画为主。\n",
            encoding="utf-8",
        )


def make_zip(source_dir: Path, zip_path: Path) -> None:
    if zip_path.exists():
        zip_path.unlink()
    with zipfile.ZipFile(zip_path, "w", compression=zipfile.ZIP_DEFLATED) as zf:
        for path in sorted(source_dir.rglob("*")):
            if path.is_file():
                zf.write(path, path.relative_to(source_dir.parent))


def build_package() -> dict:
    safe_rmtree(SUBMISSION_DIR)
    ensure_dirs()
    fonts = register_fonts()
    style = styles(fonts)
    images = image_files()
    counts = card_counts()
    _, no_strategy = load_longrun_stats()
    win_chart = make_winrate_chart(no_strategy)
    count_chart = make_card_count_chart(counts)
    contact_sheet = make_contact_sheet(images)

    pdfs = [
        build_author_pdf(style),
        build_overview_pdf(style, contact_sheet, no_strategy, len(images)),
        build_quickstart_pdf(style),
        build_data_pdf(style, counts, no_strategy, win_chart, count_chart, len(images)),
        build_manual_pdf(style),
    ]

    for pdf in pdfs:
        shutil.copy2(pdf, SUBMISSION_DIR / pdf.name)
    copy_video(SUBMISSION_DIR)
    copy_illustrations(SUBMISSION_DIR / "05_已生成卡牌插画", images, contact_sheet)
    copy_appendix_files(SUBMISSION_DIR / "06_版本数据附录")

    readme = SUBMISSION_DIR / "00_阅读顺序.txt"
    readme.write_text(
        "建议阅读顺序：\n"
        "1. 00a_作者信息与作品文字说明.pdf\n"
        "2. 00_请先看这里_作品总览.pdf\n"
        "3. 01_一页玩法速览.pdf\n"
        "4. 02_宣传视频.mp4（如需快速感受主题）\n"
        "5. 03_v2版本迭代与关键数据.pdf\n"
        "6. 04_使用手册.pdf\n"
        "7. 05_已生成卡牌插画/\n"
        "8. 06_版本数据附录/\n",
        encoding="utf-8",
    )

    make_zip(SUBMISSION_DIR, ZIP_PATH)
    return {
        "submission_dir": str(SUBMISSION_DIR),
        "zip_path": str(ZIP_PATH),
        "image_count": len(images),
        "zip_size_mb": round(ZIP_PATH.stat().st_size / 1024 / 1024, 2),
        "created_at": datetime.now().isoformat(timespec="seconds"),
    }


if __name__ == "__main__":
    result = build_package()
    print(json.dumps(result, ensure_ascii=False, indent=2))
