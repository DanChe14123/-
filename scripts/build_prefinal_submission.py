from __future__ import annotations

import csv
import json
import shutil
import textwrap
import zipfile
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, Iterable, List, Optional

import imageio.v2 as imageio
import matplotlib
import numpy as np
from PIL import Image, ImageDraw, ImageFilter, ImageFont
from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_LEFT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import cm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import (
    Image as RLImage,
    PageBreak,
    Paragraph,
    SimpleDocTemplate,
    Spacer,
    Table,
    TableStyle,
)

matplotlib.use("Agg")
import matplotlib.pyplot as plt


ROOT = Path(__file__).resolve().parents[1]
OUTPUT_PDF = ROOT / "output" / "pdf" / "prefinal_20260414"
OUTPUT_VIDEO = ROOT / "output" / "video" / "prefinal_20260414"
OUTPUT_CHARTS = ROOT / "output" / "charts" / "prefinal_20260414"
SUBMISSION_ROOT = ROOT / "submission" / "初赛参赛作品_v0.8_prefinal_20260414"
ZIP_PATH = ROOT / "submission" / "初赛参赛作品_v0.8_prefinal_20260414.zip"

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

CARD_SAMPLE_IDS = [f"E{i:02d}" for i in range(1, 14)]
NEW_ACTIONS = {"shutdown", "inspect", "secure", "evacuate"}
STOP_REPORT = {"stop", "report"}

AUTHOR_INFO = {
    "name": "赵成博",
    "student_id": "2501110475",
    "phone": "17615805216",
    "email": "17615805216@163.com",
    "bio": "北京大学化学与分子工程学院2025级博士研究生，严纯化老师课题组，研究方向为机器学习在稀土纳米材料合成中的应用。",
}

WORK_TITLE = "《实验室安全值班》"
WORK_SUBTITLE = "化学实验室安全情境协作桌游"
WORK_WRITTEN_DESCRIPTION = (
    "《实验室安全值班》是一套面向化学实验室安全教育的轻量协作桌游。"
    "作品围绕真实实验室场景构建任务牌、事件牌和行动牌，让玩家在有限回合内面对实验目标与安全风险的双重压力，"
    "通过讨论、判断和行动选择完成风险识别、处置决策与复盘学习。"
    "作品既强调实验流程中的任务推进，也强调实验室规范和应急处置，适合用于新生入组培训、课堂安全讨论和比赛展示。"
)


@dataclass
class VersionConfig:
    label: str
    summary_path: Path
    note: str
    task_count: int
    event_count: int
    action_count: int


VERSION_CONFIGS: List[VersionConfig] = [
    VersionConfig("v0.1", ROOT / "data" / "v0.1" / "run_003_v0_1_prefinal_baseline" / "summary.json", "最小原型，标准模式明显过难", 8, 16, 8),
    VersionConfig("v0.2", ROOT / "data" / "v0.2" / "run_002_candidate_v0_2_fullstats" / "summary.json", "通过基础平衡调整进入可试玩区间", 8, 16, 8),
    VersionConfig("v0.3", ROOT / "data" / "v0.3" / "run_001_v0_3_fullstats" / "summary.json", "加入任务绑定、隐患值和任务奖励，形成教学闭环", 8, 16, 8),
    VersionConfig("v0.4", ROOT / "data" / "v0.4" / "run_001_v0_4_strategy_launch" / "summary.json", "加入策略牌，形成赛前流派起点", 8, 16, 8),
    VersionConfig("v0.5", ROOT / "data" / "v0.5" / "run_001_v0_5_task_expansion" / "summary.json", "任务牌扩充到 12 张，内容体量成型", 12, 16, 8),
    VersionConfig("v0.6", ROOT / "data" / "v0.6" / "run_001_v0_6_action_expansion" / "summary.json", "行动扩充到 12 类，打法不再单一", 12, 16, 12),
    VersionConfig("v0.7", ROOT / "data" / "v0.7" / "run_001_v0_7_event_expansion" / "summary.json", "事件牌扩充到 24 张，玩法厚度成型", 12, 24, 12),
    VersionConfig("v0.8", ROOT / "data" / "v0.8" / "run_002_v0_8_refinement_teaching3" / "summary.json", "精修弱项并把教学模式拉回真正的入门版本", 12, 24, 12),
    VersionConfig("v0.8-final", ROOT / "data" / "v0.8" / "run_003_v0_8_prefinal_longrun" / "summary.json", "初赛前 10000 局长跑封版", 12, 24, 12),
]

SORA_PROMPT = """# 初赛宣传视频 Sora 提示词

Use case: competition teaser for chemistry faculty judges
Primary request: create a 20-second promo video for a lightweight cooperative tabletop game about chemical laboratory safety training
Scene/background: bright university chemistry laboratory, clean benches, fume hood, waste containers, standard glassware, modern but realistic academic environment
Subject: four fictional student researchers learning to identify hazards, choose actions, and complete tasks safely
Action: show a clear sequence of laboratory risk appearing, players discussing a response, correct handling stabilizing the scene, and the game being used in training
Camera: medium cinematic shots, slow push-ins, clean cuts, occasional top-down glimpse of cards on a table, no frantic motion
Lighting/mood: clear, calm, trustworthy, educational, professional
Color palette: lab blue, clean white, safety orange, soft gray, restrained red accents
Style/format: polished animation with card-game presentation, suitable for faculty judges, easy to understand without gaming background
Timing/beats: 4 short beats across 20 seconds; risk appears -> decision -> correct handling -> training value
Audio: light instrumental underscore only, no dramatic trailer style
Text (verbatim): "实验室安全值班" / "轻量协作式实验室安全培训桌游" / "风险识别 处置决策 复盘学习"
Constraints: no real people, no copyrighted characters, no dense on-screen text, no flashy game UI, no fantasy or sci-fi elements
Avoid: dark thriller style, noisy editing, exaggerated fire/explosions, overly childish cartoon style
"""


def ensure_dirs() -> None:
    for path in [OUTPUT_PDF, OUTPUT_VIDEO, OUTPUT_CHARTS, SUBMISSION_ROOT, SUBMISSION_ROOT / "05_样板卡图", SUBMISSION_ROOT / "06_版本数据附录"]:
        path.mkdir(parents=True, exist_ok=True)


def register_fonts() -> Dict[str, str]:
    regular_name = "CN-Regular"
    bold_name = "CN-Bold"
    regular_path = next(path for path in FONT_REGULAR_PATHS if path.exists())
    bold_path = next(path for path in FONT_BOLD_PATHS if path.exists())
    pdfmetrics.registerFont(TTFont(regular_name, str(regular_path)))
    pdfmetrics.registerFont(TTFont(bold_name, str(bold_path)))
    return {"regular": regular_name, "bold": bold_name, "regular_path": str(regular_path), "bold_path": str(bold_path)}


def build_styles(fonts: Dict[str, str]) -> Dict[str, ParagraphStyle]:
    base = getSampleStyleSheet()
    return {
        "title": ParagraphStyle("title", parent=base["Title"], fontName=fonts["bold"], fontSize=22, leading=28, alignment=TA_CENTER, textColor=colors.HexColor("#163A70"), wordWrap="CJK", spaceAfter=10),
        "subtitle": ParagraphStyle("subtitle", parent=base["Normal"], fontName=fonts["regular"], fontSize=11, leading=16, alignment=TA_CENTER, textColor=colors.HexColor("#43526B"), wordWrap="CJK", spaceAfter=10),
        "heading": ParagraphStyle("heading", parent=base["Heading2"], fontName=fonts["bold"], fontSize=14, leading=20, textColor=colors.HexColor("#183A72"), wordWrap="CJK", spaceBefore=6, spaceAfter=6),
        "body": ParagraphStyle("body", parent=base["BodyText"], fontName=fonts["regular"], fontSize=10.5, leading=15, textColor=colors.HexColor("#1E2635"), wordWrap="CJK", alignment=TA_LEFT),
        "small": ParagraphStyle("small", parent=base["BodyText"], fontName=fonts["regular"], fontSize=9, leading=13, textColor=colors.HexColor("#364256"), wordWrap="CJK"),
        "bullet": ParagraphStyle("bullet", parent=base["BodyText"], fontName=fonts["regular"], fontSize=10.5, leading=15, leftIndent=14, firstLineIndent=-8, bulletIndent=0, wordWrap="CJK", textColor=colors.HexColor("#1E2635")),
    }


def p(text: str, style: ParagraphStyle) -> Paragraph:
    return Paragraph(text.replace("\n", "<br/>"), style)


def load_json(path: Path) -> Dict:
    with path.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def load_csv_rows(path: Path) -> List[Dict[str, str]]:
    if not path.exists():
        return []
    with path.open("r", encoding="utf-8-sig", newline="") as handle:
        return list(csv.DictReader(handle))


def row_is_none_strategy(row: Dict[str, str]) -> bool:
    return "strategy_id" not in row or row.get("strategy_id") in {"", "none"}


def get_row(rows: Iterable[Dict[str, str]], *, mode: str, team: str) -> Optional[Dict[str, str]]:
    filtered = [row for row in rows if row.get("mode") == mode and row.get("team") == team and row_is_none_strategy(row)]
    return filtered[0] if filtered else None


def safe_float(row: Optional[Dict[str, str]], key: str) -> Optional[float]:
    if not row:
        return None
    value = row.get(key)
    if value in {None, ""}:
        return None
    return float(value)


def compute_action_rates(rows: List[Dict[str, str]]) -> Dict[str, float]:
    filtered = [row for row in rows if row.get("mode") == "standard" and row.get("team") == "balanced+balanced" and row_is_none_strategy(row)]
    if not filtered:
        return {"stop_report": 0.0, "new_actions": 0.0}
    rates = {row["action_id"]: float(row["pick_rate"]) for row in filtered}
    return {
        "stop_report": sum(rates.get(action, 0.0) for action in STOP_REPORT),
        "new_actions": sum(rates.get(action, 0.0) for action in NEW_ACTIONS),
    }


def compute_task_bottom(rows: List[Dict[str, str]], n: int = 3) -> List[Dict[str, float]]:
    filtered = [row for row in rows if row.get("mode") == "standard" and row.get("team") == "balanced+balanced" and row_is_none_strategy(row)]
    for row in filtered:
        key = "completion_rate" if "completion_rate" in row else "task_success_rate"
        row["_rate"] = float(row[key])
    filtered.sort(key=lambda row: row["_rate"])
    return filtered[:n]


def compute_tough_event_rows(rows: List[Dict[str, str]], n: int = 5) -> List[Dict[str, float]]:
    filtered = [row for row in rows if row.get("mode") == "standard" and row.get("team") == "balanced+balanced" and row_is_none_strategy(row)]
    for row in filtered:
        if "success_rate" in row and row["success_rate"]:
            row["_success"] = float(row["success_rate"])
        else:
            row["_success"] = float(row.get("full_rate", 0.0)) + float(row.get("partial_rate", 0.0)) + float(row.get("contained_rate", 0.0))
    filtered.sort(key=lambda row: row["_success"])
    return filtered[:n]


def collect_version_stats() -> List[Dict[str, object]]:
    version_rows: List[Dict[str, object]] = []
    for config in VERSION_CONFIGS:
        summary = load_json(config.summary_path)
        base_dir = config.summary_path.parent
        team_rows = load_csv_rows(base_dir / "team_stats.csv")
        action_rows = load_csv_rows(base_dir / "action_stats.csv")
        teaching_row = get_row(team_rows, mode="teaching", team="balanced+balanced")
        challenge_row = get_row(team_rows, mode="challenge", team="balanced+balanced")
        action_metrics = compute_action_rates(action_rows)
        version_rows.append(
            {
                "version": config.label,
                "note": config.note,
                "task_count": config.task_count,
                "event_count": config.event_count,
                "action_count": config.action_count,
                "summary_path": str(config.summary_path),
                "balanced_standard_win_rate": summary["balanced_standard_team"]["win_rate"],
                "balanced_standard_progress": summary["balanced_standard_team"]["avg_progress"],
                "balanced_standard_safety": summary["balanced_standard_team"]["avg_safety"],
                "balanced_standard_upgrade": summary["balanced_standard_team"]["avg_upgrade"],
                "balanced_standard_hazards": summary["balanced_standard_team"].get("avg_hazards"),
                "teaching_win_rate": safe_float(teaching_row, "win_rate"),
                "challenge_win_rate": safe_float(challenge_row, "win_rate"),
                "stop_report_rate": action_metrics["stop_report"],
                "new_action_rate": action_metrics["new_actions"],
            }
        )
    return version_rows


def save_csv(path: Path, rows: List[Dict[str, object]]) -> None:
    if not rows:
        return
    with path.open("w", encoding="utf-8-sig", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)


def plot_chart_standard(version_rows: List[Dict[str, object]], out_path: Path) -> None:
    labels = [row["version"] for row in version_rows]
    values = [row["balanced_standard_win_rate"] * 100 for row in version_rows]
    plt.figure(figsize=(8, 4.2))
    plt.rcParams["font.sans-serif"] = ["SimHei", "Microsoft YaHei", "Arial Unicode MS"]
    plt.rcParams["axes.unicode_minus"] = False
    plt.plot(labels, values, marker="o", linewidth=2.4, color="#1D4ED8")
    plt.ylim(0, 65)
    plt.grid(alpha=0.25, linestyle="--", axis="y")
    plt.ylabel("胜率 (%)")
    plt.title("标准模式 balanced+balanced 胜率趋势")
    for label, value in zip(labels, values):
        plt.text(label, value + 1.1, f"{value:.1f}", ha="center", fontsize=9)
    plt.tight_layout()
    plt.savefig(out_path, dpi=220)
    plt.close()


def plot_chart_scale(version_rows: List[Dict[str, object]], out_path: Path) -> None:
    labels = [row["version"] for row in version_rows]
    task_values = [row["task_count"] for row in version_rows]
    event_values = [row["event_count"] for row in version_rows]
    action_values = [row["action_count"] for row in version_rows]
    plt.figure(figsize=(8, 4.2))
    plt.rcParams["font.sans-serif"] = ["SimHei", "Microsoft YaHei", "Arial Unicode MS"]
    plt.plot(labels, task_values, marker="o", linewidth=2.2, color="#2563EB", label="任务牌")
    plt.plot(labels, event_values, marker="o", linewidth=2.2, color="#F97316", label="事件牌")
    plt.plot(labels, action_values, marker="o", linewidth=2.2, color="#16A34A", label="行动牌")
    plt.grid(alpha=0.25, linestyle="--", axis="y")
    plt.ylabel("数量")
    plt.title("内容规模扩充趋势")
    plt.legend()
    plt.tight_layout()
    plt.savefig(out_path, dpi=220)
    plt.close()


def plot_chart_action(version_rows: List[Dict[str, object]], out_path: Path) -> None:
    labels = [row["version"] for row in version_rows]
    stop_report = [row["stop_report_rate"] * 100 for row in version_rows]
    new_actions = [row["new_action_rate"] * 100 for row in version_rows]
    x = range(len(labels))
    width = 0.38
    plt.figure(figsize=(8, 4.2))
    plt.rcParams["font.sans-serif"] = ["SimHei", "Microsoft YaHei", "Arial Unicode MS"]
    plt.bar([i - width / 2 for i in x], stop_report, width=width, color="#334155", label="stop + report")
    plt.bar([i + width / 2 for i in x], new_actions, width=width, color="#0EA5E9", label="新增四类行动")
    plt.xticks(list(x), labels)
    plt.ylabel("占比 (%)")
    plt.title("行动结构优化趋势")
    plt.legend()
    plt.grid(alpha=0.2, linestyle="--", axis="y")
    plt.tight_layout()
    plt.savefig(out_path, dpi=220)
    plt.close()


def plot_chart_teaching(version_rows: List[Dict[str, object]], out_path: Path) -> None:
    labels = [row["version"] for row in version_rows]
    values = [(row["teaching_win_rate"] or 0.0) * 100 for row in version_rows]
    plt.figure(figsize=(8, 4.2))
    plt.rcParams["font.sans-serif"] = ["SimHei", "Microsoft YaHei", "Arial Unicode MS"]
    plt.plot(labels, values, marker="o", linewidth=2.4, color="#7C3AED")
    plt.ylim(0, 100)
    plt.grid(alpha=0.25, linestyle="--", axis="y")
    plt.ylabel("胜率 (%)")
    plt.title("教学模式可用性趋势")
    for label, value in zip(labels, values):
        plt.text(label, value + 1.5, f"{value:.1f}", ha="center", fontsize=9)
    plt.tight_layout()
    plt.savefig(out_path, dpi=220)
    plt.close()


def create_story_header(title: str, subtitle: str, styles: Dict[str, ParagraphStyle]) -> List:
    return [p(title, styles["title"]), p(subtitle, styles["subtitle"]), Spacer(1, 0.25 * cm)]


def append_author_info(story: List, fonts: Dict[str, str], styles: Dict[str, ParagraphStyle], *, include_work_description: bool = False) -> None:
    story.append(p("作者信息", styles["heading"]))
    author_rows = [
        [p("字段", styles["small"]), p("内容", styles["small"])],
        [p("作者姓名", styles["small"]), p(AUTHOR_INFO["name"], styles["body"])],
        [p("学号", styles["small"]), p(AUTHOR_INFO["student_id"], styles["body"])],
        [p("联系电话", styles["small"]), p(AUTHOR_INFO["phone"], styles["body"])],
        [p("电子邮箱", styles["small"]), p(AUTHOR_INFO["email"], styles["body"])],
        [p("作者简介", styles["small"]), p(AUTHOR_INFO["bio"], styles["body"])],
    ]
    story.append(table_from_rows(author_rows, fonts, [3.0 * cm, 12.6 * cm]))
    if include_work_description:
        story.append(Spacer(1, 0.18 * cm))
        story.append(p("作品文字说明", styles["heading"]))
        story.append(p(WORK_WRITTEN_DESCRIPTION, styles["body"]))


def table_from_rows(rows: List[List[object]], fonts: Dict[str, str], col_widths: List[float]) -> Table:
    table = Table(rows, colWidths=col_widths, repeatRows=1)
    table.setStyle(
        TableStyle(
            [
                ("FONTNAME", (0, 0), (-1, 0), fonts["bold"]),
                ("FONTNAME", (0, 1), (-1, -1), fonts["regular"]),
                ("FONTSIZE", (0, 0), (-1, -1), 9),
                ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#E7EEF9")),
                ("TEXTCOLOR", (0, 0), (-1, 0), colors.HexColor("#163A70")),
                ("GRID", (0, 0), (-1, -1), 0.5, colors.HexColor("#C7D2E5")),
                ("VALIGN", (0, 0), (-1, -1), "TOP"),
                ("LEADING", (0, 0), (-1, -1), 12),
                ("TOPPADDING", (0, 0), (-1, -1), 5),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
            ]
        )
    )
    return table


def build_overview_pdf(path: Path, fonts: Dict[str, str], styles: Dict[str, ParagraphStyle], final_stats: Dict[str, object], cover_image: Path) -> None:
    doc = SimpleDocTemplate(str(path), pagesize=A4, leftMargin=1.7 * cm, rightMargin=1.7 * cm, topMargin=1.6 * cm, bottomMargin=1.6 * cm)
    story: List = []
    story.extend(create_story_header("《实验室安全值班》作品总览", "面向化学院老师的初赛阅读入口", styles))

    intro_text = (
        "这是一套轻量协作式化学实验室安全培训桌游。"
        "玩家在 15 到 20 分钟内，通过“任务推进 + 风险事件处置 + 复盘知识点”完成一局实验室安全训练。"
    )
    story.append(p(intro_text, styles["body"]))
    story.append(Spacer(1, 0.2 * cm))
    story.append(RLImage(str(cover_image), width=15.5 * cm, height=11.3 * cm))
    story.append(Spacer(1, 0.2 * cm))

    story.append(p("核心玩法四步", styles["heading"]))
    for item in [
        "1. 抽取 1 张实验任务牌，确定本轮实验目标。",
        "2. 从关联风险池中翻开 1 张事件牌，暴露实验室隐患。",
        "3. 团队从公共行动牌中选择应对措施，判断是否既控制风险又推进任务。",
        "4. 回合结算后复盘正确处置与知识点，形成训练闭环。",
    ]:
        story.append(p(item, styles["bullet"]))

    story.append(Spacer(1, 0.18 * cm))
    story.append(p("这套作品适合：新生入组培训、实验室安全教育、课堂安全讨论、答辩现场演示。", styles["body"]))
    story.append(Spacer(1, 0.16 * cm))
    story.append(
        p(
            f"同目录建议先看：02_宣传视频.mp4。当前最终长跑数据显示，标准模式 balanced+balanced 胜率为 {final_stats['balanced_standard_win_rate'] * 100:.2f}%，"
            f"教学模式胜率为 {final_stats['teaching_win_rate'] * 100:.2f}%。",
            styles["body"],
        )
    )

    story.append(Spacer(1, 0.25 * cm))
    story.append(p("压缩包阅读顺序", styles["heading"]))
    for item in [
        "00_请先看这里_作品总览.pdf：先认识作品和核心价值",
        "01_一页玩法速览.pdf：快速理解一局怎么进行",
        "02_宣传视频.mp4：不懂桌游也能先看懂作品要点",
        "03_版本迭代与关键数据.pdf：看版本演化和最终封版数据",
        "04_使用手册.pdf：详细规则与教学使用建议",
    ]:
        story.append(p(item, styles["bullet"]))
    doc.build(story)


def build_onepager_pdf(path: Path, fonts: Dict[str, str], styles: Dict[str, ParagraphStyle]) -> None:
    doc = SimpleDocTemplate(str(path), pagesize=A4, leftMargin=1.7 * cm, rightMargin=1.7 * cm, topMargin=1.5 * cm, bottomMargin=1.5 * cm)
    story: List = []
    story.extend(create_story_header("一页玩法速览", "给不熟悉桌游的评委老师看的简明版说明", styles))
    story.append(p("作品定位", styles["heading"]))
    story.append(p("1 到 4 人，推荐 2 到 3 人，单局约 15 到 20 分钟。它不是竞技对抗桌游，而是以化学实验室风险识别和处置决策为核心的协作训练工具。", styles["body"]))
    story.append(p("一局怎么进行", styles["heading"]))
    for item in [
        "每轮先抽实验任务，再翻开与该任务相关的安全事件。",
        "团队从公共行动牌中选择 1 到 2 个动作，讨论如何应对。",
        "如果动作既解决事件又符合任务要求，就推进进度并触发奖励。",
        "如果处理错误，安全值下降、升级标记增加，隐患也可能累积。",
    ]:
        story.append(p(item, styles["bullet"]))

    story.append(p("怎么赢 / 怎么输", styles["heading"]))
    story.append(p("标准模式下，团队需要在 6 轮内完成至少 4 点进度，并保持安全值大于 0、升级标记未爆表、隐患值未失控。", styles["body"]))
    story.append(Spacer(1, 0.12 * cm))
    story.append(p("失败通常来自三类原因：安全值归零、隐患失控、进度不足。这样的设计会自然逼迫玩家在“做实验”和“守规范”之间做出判断。", styles["body"]))

    story.append(p("为什么适合化学实验室安全培训", styles["heading"]))
    for item in [
        "风险事件全部来自典型化学实验室场景，而不是抽象口号。",
        "每张事件牌背后都对应“正确处置 + 原因 + 知识点 + 复盘问题”。",
        "规则足够轻，适合课堂、培训或比赛答辩现场快速演示。",
    ]:
        story.append(p(item, styles["bullet"]))
    doc.build(story)


def build_data_pdf(path: Path, fonts: Dict[str, str], styles: Dict[str, ParagraphStyle], version_rows: List[Dict[str, object]], chart_paths: Dict[str, Path], final_summary: Dict[str, object], final_tasks: List[Dict[str, object]], final_events: List[Dict[str, object]], final_action_metrics: Dict[str, float], validation: Dict[str, bool]) -> None:
    doc = SimpleDocTemplate(str(path), pagesize=A4, leftMargin=1.5 * cm, rightMargin=1.5 * cm, topMargin=1.4 * cm, bottomMargin=1.4 * cm)
    story: List = []
    story.extend(create_story_header("版本迭代与关键数据", "只展示支撑结论的关键指标，不用评委老师翻原始 CSV", styles))

    summary_rows = [["版本", "核心改动", "标准胜率", "教学胜率", "结论"]]
    for row in version_rows:
        teaching_text = "-" if row["teaching_win_rate"] is None else f"{row['teaching_win_rate'] * 100:.2f}%"
        summary_rows.append([row["version"], row["note"], f"{row['balanced_standard_win_rate'] * 100:.2f}%", teaching_text, "规则更稳定" if row["version"] != "v0.1" else "原型过难"])
    story.append(table_from_rows(summary_rows, fonts, [2.0 * cm, 7.0 * cm, 2.2 * cm, 2.2 * cm, 3.5 * cm]))
    story.append(Spacer(1, 0.25 * cm))

    chart_table = Table(
        [
            [RLImage(str(chart_paths["standard"]), width=8.0 * cm, height=4.2 * cm), RLImage(str(chart_paths["scale"]), width=8.0 * cm, height=4.2 * cm)],
            [RLImage(str(chart_paths["action"]), width=8.0 * cm, height=4.2 * cm), RLImage(str(chart_paths["teaching"]), width=8.0 * cm, height=4.2 * cm)],
        ],
        colWidths=[8.2 * cm, 8.2 * cm],
    )
    chart_table.setStyle(TableStyle([("VALIGN", (0, 0), (-1, -1), "TOP")]))
    story.append(chart_table)

    story.append(PageBreak())
    story.append(p("最终长跑封版结论", styles["heading"]))
    verdict_text = (
        f"最终长跑使用 run_003_v0_8_prefinal_longrun，共 {final_summary['games_per_team']} 局/队伍。"
        f"balanced+balanced 在标准模式下胜率 {final_summary['balanced_standard_team']['win_rate'] * 100:.2f}%，"
        f"教学模式胜率 {final_summary['teaching_win_rate'] * 100:.2f}%，"
        f"挑战模式胜率 {final_summary['challenge_win_rate'] * 100:.2f}%。"
    )
    story.append(p(verdict_text, styles["body"]))

    pass_rows = [["验收项", "结果", "是否通过"]]
    pass_rows.append(["标准模式胜率 0.50 - 0.56", f"{final_summary['balanced_standard_team']['win_rate']:.4f}", "通过" if validation["standard"] else "未通过"])
    pass_rows.append(["教学模式胜率 >= 0.75", f"{final_summary['teaching_win_rate']:.4f}", "通过" if validation["teaching"] else "未通过"])
    pass_rows.append(["挑战模式胜率 0.28 - 0.38", f"{final_summary['challenge_win_rate']:.4f}", "通过" if validation["challenge"] else "未通过"])
    pass_rows.append(["最弱任务完成率 >= 0.52", f"{min(float(row['_rate']) for row in final_tasks):.4f}", "通过" if validation["task_floor"] else "未通过"])
    pass_rows.append(["stop + report 占比 <= 0.27", f"{final_action_metrics['stop_report']:.4f}", "通过" if validation["action"] else "未通过"])
    story.append(table_from_rows(pass_rows, fonts, [5.8 * cm, 3.0 * cm, 3.0 * cm]))
    story.append(Spacer(1, 0.22 * cm))

    metric_rows = [
        ["指标", "数值"],
        ["标准模式最佳队伍", final_summary["best_standard_team"]["team"]],
        ["标准模式最弱队伍", final_summary["weakest_standard_team"]["team"]],
        ["balanced+balanced 平均进度", f"{final_summary['balanced_standard_team']['avg_progress']:.3f}"],
        ["balanced+balanced 平均安全值", f"{final_summary['balanced_standard_team']['avg_safety']:.3f}"],
        ["balanced+balanced 平均升级标记", f"{final_summary['balanced_standard_team']['avg_upgrade']:.3f}"],
        ["balanced+balanced 平均隐患值", f"{final_summary['balanced_standard_team']['avg_hazards']:.3f}"],
        ["stop + report 合计占比", f"{final_action_metrics['stop_report'] * 100:.2f}%"],
        ["shutdown / inspect / secure / evacuate 合计占比", f"{final_action_metrics['new_actions'] * 100:.2f}%"],
    ]
    story.append(table_from_rows(metric_rows, fonts, [6.0 * cm, 4.0 * cm]))

    story.append(PageBreak())
    story.append(p("最终版最弱任务与最难事件", styles["heading"]))
    task_rows = [["任务牌", "完成率", "说明"]]
    for row in final_tasks:
        task_rows.append([row["task_id"] + " " + row["task_name"], f"{float(row['_rate']) * 100:.2f}%", "仍在可接受区间，不再动规则"])
    story.append(table_from_rows(task_rows, fonts, [6.5 * cm, 2.3 * cm, 6.0 * cm]))
    story.append(Spacer(1, 0.22 * cm))

    event_rows = [["事件牌", "成功结构", "说明"]]
    for row in final_events:
        event_rows.append([row["event_id"] + " " + row["event_name"], f"{float(row['_success']) * 100:.2f}%", "作为高压教学点保留，不再改机制"])
    story.append(table_from_rows(event_rows, fonts, [6.5 * cm, 2.3 * cm, 6.0 * cm]))
    story.append(Spacer(1, 0.22 * cm))
    story.append(p("结论：v0.8 在机制上冻结，后续优化重点转为展示质量、手册表达和复赛演示材料，而不是继续重写规则。", styles["body"]))
    doc.build(story)


def build_manual_pdf(path: Path, fonts: Dict[str, str], styles: Dict[str, ParagraphStyle], sample_images: List[Path]) -> None:
    doc = SimpleDocTemplate(str(path), pagesize=A4, leftMargin=1.6 * cm, rightMargin=1.6 * cm, topMargin=1.5 * cm, bottomMargin=1.5 * cm)
    story: List = []
    story.extend(create_story_header("使用手册", "给初赛评委和后续培训老师的详细说明", styles))

    story.append(p("1. 作品定位", styles["heading"]))
    story.append(p("《实验室安全值班》是一套面向化学实验室安全教育的轻量协作桌游。它通过任务、事件、行动三类牌的互动，让玩家在短时间内练习风险识别、处置决策和复盘表达。", styles["body"]))
    story.append(Spacer(1, 0.12 * cm))
    story.append(p("推荐场景：新生入组教育、实验室安全培训、课堂讨论、小型公开展示。", styles["body"]))
    if sample_images:
        story.append(Spacer(1, 0.2 * cm))
        story.append(RLImage(str(sample_images[0]), width=15.0 * cm, height=11.0 * cm))

    story.append(PageBreak())
    story.append(p("2. 开局准备", styles["heading"]))
    for item in [
        "选择模式：教学 / 标准 / 挑战。",
        "洗混任务牌、事件牌和行动牌；将行动牌翻开 8 张组成公共手牌。",
        "如使用角色牌和策略牌，则在开局完成对应选择。",
        "初始化安全值、进度值、升级标记与隐患值。",
    ]:
        story.append(p(item, styles["bullet"]))

    story.append(p("3. 每轮流程", styles["heading"]))
    for item in [
        "先结算隐患带来的轮初压力，再翻开本轮任务牌。",
        "从该任务关联的事件池中翻开 1 张事件牌。",
        "团队从公共手牌中打出 1 到 2 张行动牌，讨论怎样处理最合适。",
        "若行动既解决事件又符合任务要求，则推进任务并触发奖励。",
        "翻看事件牌背面的正确处置与知识点，完成复盘。",
    ]:
        story.append(p(item, styles["bullet"]))

    story.append(PageBreak())
    story.append(p("4. 怎么赢，怎么输", styles["heading"]))
    story.append(p("标准模式下，团队需要在 6 轮内完成至少 4 点进度，同时保证安全值大于 0、升级标记未达到上限、隐患值未爆表。", styles["body"]))
    story.append(Spacer(1, 0.12 * cm))
    story.append(p("失败通常来自：处理错误导致安全值归零、隐患连续积压、进度不足，或者高危事件被明显错误处置。", styles["body"]))

    story.append(p("5. 三种模式", styles["heading"]))
    mode_rows = [["模式", "用途", "特点"], ["教学", "新手体验与课堂训练", "更高安全值、更多换牌机会、通关目标更低"], ["标准", "作品主展示模式", "在风险控制和任务推进之间保持平衡"], ["挑战", "高压演示或进阶体验", "初始压力更大，额外事件更多"]]
    story.append(table_from_rows(mode_rows, fonts, [2.5 * cm, 4.8 * cm, 8.2 * cm]))

    story.append(PageBreak())
    story.append(p("6. 为什么适合化学实验室培训", styles["heading"]))
    for item in [
        "风险事件全部来自实验室常见场景，例如标签模糊、废液混放、通风控制失效、玻璃器皿裂纹、气瓶异常等。",
        "每轮不只是“答题”，而是让玩家在有限行动中做选择，因此更接近真实处置思路。",
        "每张事件牌背面都保留复盘知识点，方便老师讲解，也便于课后讨论。",
    ]:
        story.append(p(item, styles["bullet"]))
    story.append(p("7. 教学使用建议", styles["heading"]))
    for item in [
        "首次培训建议直接使用教学模式，重点看“为什么这样处置”。",
        "展示时可只演示 1 到 2 轮，不必完整跑完一局。",
        "如果时间有限，建议先放宣传视频，再用一张高代表性事件牌做现场讲解。",
    ]:
        story.append(p(item, styles["bullet"]))
    doc.build(story)


def fit_cover_image(img: Image.Image, size: tuple[int, int]) -> Image.Image:
    target_w, target_h = size
    src_ratio = img.width / img.height
    dst_ratio = target_w / target_h
    if src_ratio > dst_ratio:
        new_h = target_h
        new_w = int(new_h * src_ratio)
    else:
        new_w = target_w
        new_h = int(new_w / src_ratio)
    img = img.resize((new_w, new_h), Image.LANCZOS)
    left = (img.width - target_w) // 2
    top = (img.height - target_h) // 2
    return img.crop((left, top, left + target_w, top + target_h))


def draw_text_block(draw: ImageDraw.ImageDraw, xy: tuple[int, int], width: int, title: str, body_lines: List[str], title_font: ImageFont.FreeTypeFont, body_font: ImageFont.FreeTypeFont, fill: str = "#FFFFFF") -> None:
    x, y = xy
    draw.text((x, y), title, font=title_font, fill=fill)
    y += int(title_font.size * 1.55)
    wrap_chars = max(12, width // body_font.size)
    for line in body_lines:
        for wrapped in textwrap.wrap(line, width=wrap_chars):
            draw.text((x, y), wrapped, font=body_font, fill=fill)
            y += int(body_font.size * 1.6)
        y += 6


def build_scene(size: tuple[int, int], image_paths: List[Path], headline: str, sublines: List[str], body_font: ImageFont.FreeTypeFont, title_font: ImageFont.FreeTypeFont) -> Image.Image:
    canvas = Image.new("RGB", size, "#0F172A")
    background = None
    for path in image_paths:
        if path.exists():
            background = Image.open(path).convert("RGB")
            break
    if background:
        background = fit_cover_image(background, size).filter(ImageFilter.GaussianBlur(radius=8))
        background = Image.blend(background, Image.new("RGB", size, "#0B1220"), 0.45)
        canvas.paste(background, (0, 0))

    draw = ImageDraw.Draw(canvas)
    draw.rounded_rectangle((48, 48, size[0] - 48, size[1] - 48), radius=28, outline="#E2E8F0", width=2)
    card_y = 120
    card_x = size[0] - 540
    thumb_w = 220
    thumb_h = 300
    gap = 28
    for idx, path in enumerate(image_paths[:2]):
        if not path.exists():
            continue
        card = fit_cover_image(Image.open(path).convert("RGB"), (thumb_w, thumb_h))
        shadow = Image.new("RGBA", (thumb_w + 20, thumb_h + 20), (0, 0, 0, 0))
        shadow_draw = ImageDraw.Draw(shadow)
        shadow_draw.rounded_rectangle((10, 12, thumb_w + 6, thumb_h + 8), radius=20, fill=(0, 0, 0, 110))
        shadow = shadow.filter(ImageFilter.GaussianBlur(radius=10))
        pos_x = card_x + idx * (thumb_w + gap)
        canvas.paste(shadow, (pos_x - 10, card_y - 10), shadow)
        canvas.paste(card, (pos_x, card_y))

    draw_text_block(draw, (88, 120), 500, headline, sublines, title_font, body_font, fill="#FFFFFF")
    draw.rounded_rectangle((88, 520, 560, 610), radius=20, fill="#E0F2FE")
    draw.text((112, 545), "轻量协作  风险识别  处置决策  复盘学习", font=body_font, fill="#0F172A")
    return canvas


def build_video(path: Path, fonts: Dict[str, str]) -> None:
    title_font = ImageFont.truetype(fonts["bold_path"], 48)
    body_font = ImageFont.truetype(fonts["regular_path"], 24)
    size = (1280, 720)
    fps = 12
    scene_specs = [
        ("《实验室安全值班》", ["化学实验室安全培训桌游", "先看风险，再做选择。"], [ROOT / "card" / "E02.png", ROOT / "card" / "E05.png"]),
        ("典型风险会先出现", ["标签模糊、开放转移、明火、腐蚀性接触。", "事件全部来自真实实验室场景。"], [ROOT / "card" / "E08.png", ROOT / "card" / "E13.png"]),
        ("团队需要讨论行动", ["从公共行动牌中选出最合适的处置。", "不是背答案，而是在局内做判断。"], [ROOT / "card" / "E03.png", ROOT / "card" / "E06.png"]),
        ("正确处置会推进任务", ["风险被控制，任务才会真正完成。", "每轮都带有复盘知识点。"], [ROOT / "card" / "E10.png", ROOT / "card" / "E12.png"]),
        ("适用于安全培训与答辩展示", ["15 到 20 分钟一局。", "让不懂桌游的人也能快速看懂作品价值。"], [ROOT / "card" / "E01.png", ROOT / "card" / "E11.png"]),
    ]
    with imageio.get_writer(path, fps=fps, codec="libx264", quality=8) as writer:
        for headline, lines, image_paths in scene_specs:
            base = build_scene(size, image_paths, headline, lines, body_font, title_font)
            for frame_idx in range(fps * 4):
                zoom = 1.0 + (frame_idx / (fps * 4)) * 0.035
                zoomed = base.resize((int(size[0] * zoom), int(size[1] * zoom)), Image.LANCZOS)
                left = (zoomed.width - size[0]) // 2
                top = (zoomed.height - size[1]) // 2
                writer.append_data(np.asarray(zoomed.crop((left, top, left + size[0], top + size[1]))))


def copy_card_samples(dest_dir: Path) -> None:
    for card_id in CARD_SAMPLE_IDS:
        src = ROOT / "card" / f"{card_id}.png"
        if src.exists():
            shutil.copy2(src, dest_dir / src.name)


def copy_version_appendices(dest_dir: Path) -> None:
    appendix_map = {
        "v0.1": ROOT / "data" / "v0.1" / "run_003_v0_1_prefinal_baseline",
        "v0.2": ROOT / "data" / "v0.2" / "run_002_candidate_v0_2_fullstats",
        "v0.3": ROOT / "data" / "v0.3" / "run_001_v0_3_fullstats",
        "v0.4": ROOT / "data" / "v0.4" / "run_001_v0_4_strategy_launch",
        "v0.5": ROOT / "data" / "v0.5" / "run_001_v0_5_task_expansion",
        "v0.6": ROOT / "data" / "v0.6" / "run_001_v0_6_action_expansion",
        "v0.7": ROOT / "data" / "v0.7" / "run_001_v0_7_event_expansion",
        "v0.8": ROOT / "data" / "v0.8" / "run_002_v0_8_refinement_teaching3",
        "v0.8-final": ROOT / "data" / "v0.8" / "run_003_v0_8_prefinal_longrun",
    }
    wanted_files = ["summary.json", "team_stats.csv", "action_stats.csv", "event_stats.csv", "task_stats.csv", "game_results.csv", "sample_turn_logs.jsonl"]
    for label, src_dir in appendix_map.items():
        version_dir = dest_dir / label
        version_dir.mkdir(parents=True, exist_ok=True)
        for name in wanted_files:
            src = src_dir / name
            if src.exists():
                shutil.copy2(src, version_dir / name)


def make_zip(src_dir: Path, zip_path: Path) -> None:
    if zip_path.exists():
        zip_path.unlink()
    with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as zf:
        for file_path in src_dir.rglob("*"):
            if file_path.is_file():
                zf.write(file_path, file_path.relative_to(src_dir.parent))


def build_validation(final_row: Dict[str, object], final_tasks: List[Dict[str, object]], final_action: Dict[str, float]) -> Dict[str, bool]:
    return {
        "standard": 0.50 <= final_row["balanced_standard_win_rate"] <= 0.56,
        "teaching": (final_row["teaching_win_rate"] or 0.0) >= 0.75,
        "challenge": 0.28 <= (final_row["challenge_win_rate"] or 0.0) <= 0.38,
        "task_floor": min(float(row["_rate"]) for row in final_tasks) >= 0.52,
        "action": final_action["stop_report"] <= 0.27,
    }


def main() -> None:
    ensure_dirs()
    fonts = register_fonts()
    styles = build_styles(fonts)

    final_run_dir = ROOT / "data" / "v0.8" / "run_003_v0_8_prefinal_longrun"
    final_summary = load_json(final_run_dir / "summary.json")
    final_team_rows = load_csv_rows(final_run_dir / "team_stats.csv")
    final_action_rows = load_csv_rows(final_run_dir / "action_stats.csv")
    final_task_rows = load_csv_rows(final_run_dir / "task_stats.csv")
    final_event_rows = load_csv_rows(final_run_dir / "event_stats.csv")

    teaching_row = get_row(final_team_rows, mode="teaching", team="balanced+balanced")
    challenge_row = get_row(final_team_rows, mode="challenge", team="balanced+balanced")
    version_rows = collect_version_stats()
    final_action_metrics = compute_action_rates(final_action_rows)
    final_tasks = compute_task_bottom(final_task_rows, 3)
    final_events = compute_tough_event_rows(final_event_rows, 5)

    final_bundle = {
        **final_summary,
        "teaching_win_rate": float(teaching_row["win_rate"]) if teaching_row else None,
        "challenge_win_rate": float(challenge_row["win_rate"]) if challenge_row else None,
    }
    validation = build_validation(version_rows[-1], final_tasks, final_action_metrics)

    chart_paths = {
        "standard": OUTPUT_CHARTS / "chart_standard_winrate.png",
        "scale": OUTPUT_CHARTS / "chart_content_scale.png",
        "action": OUTPUT_CHARTS / "chart_action_structure.png",
        "teaching": OUTPUT_CHARTS / "chart_teaching_mode.png",
    }
    plot_chart_standard(version_rows, chart_paths["standard"])
    plot_chart_scale(version_rows, chart_paths["scale"])
    plot_chart_action(version_rows, chart_paths["action"])
    plot_chart_teaching(version_rows, chart_paths["teaching"])

    overview_pdf = OUTPUT_PDF / "00_请先看这里_作品总览.pdf"
    gameplay_pdf = OUTPUT_PDF / "01_一页玩法速览.pdf"
    data_pdf = OUTPUT_PDF / "03_版本迭代与关键数据.pdf"
    manual_pdf = OUTPUT_PDF / "04_使用手册.pdf"
    promo_video = OUTPUT_VIDEO / "02_宣传视频.mp4"

    build_overview_pdf(overview_pdf, fonts, styles, version_rows[-1], ROOT / "card" / "E02.png")
    build_onepager_pdf(gameplay_pdf, fonts, styles)
    build_data_pdf(data_pdf, fonts, styles, version_rows, chart_paths, final_bundle, final_tasks, final_events, final_action_metrics, validation)
    build_manual_pdf(manual_pdf, fonts, styles, [ROOT / "card" / "E02.png", ROOT / "card" / "E05.png"])
    build_video(promo_video, fonts)

    shutil.rmtree(SUBMISSION_ROOT, ignore_errors=True)
    ensure_dirs()
    copy_card_samples(SUBMISSION_ROOT / "05_样板卡图")
    copy_version_appendices(SUBMISSION_ROOT / "06_版本数据附录")

    shutil.copy2(overview_pdf, SUBMISSION_ROOT / overview_pdf.name)
    shutil.copy2(gameplay_pdf, SUBMISSION_ROOT / gameplay_pdf.name)
    shutil.copy2(promo_video, SUBMISSION_ROOT / promo_video.name)
    shutil.copy2(data_pdf, SUBMISSION_ROOT / data_pdf.name)
    shutil.copy2(manual_pdf, SUBMISSION_ROOT / manual_pdf.name)

    shutil.copy2(chart_paths["standard"], SUBMISSION_ROOT / "06_版本数据附录" / "chart_standard_winrate.png")
    shutil.copy2(chart_paths["scale"], SUBMISSION_ROOT / "06_版本数据附录" / "chart_content_scale.png")
    shutil.copy2(chart_paths["action"], SUBMISSION_ROOT / "06_版本数据附录" / "chart_action_structure.png")
    shutil.copy2(chart_paths["teaching"], SUBMISSION_ROOT / "06_版本数据附录" / "chart_teaching_mode.png")

    save_csv(SUBMISSION_ROOT / "06_版本数据附录" / "版本趋势摘要.csv", version_rows)
    with (SUBMISSION_ROOT / "06_版本数据附录" / "最终长跑关键指标.json").open("w", encoding="utf-8") as handle:
        json.dump({"final_summary": final_bundle, "final_action_metrics": final_action_metrics, "final_bottom_tasks": final_tasks, "final_tough_events": final_events, "validation": validation}, handle, ensure_ascii=False, indent=2)
    (SUBMISSION_ROOT / "06_版本数据附录" / "00_Sora宣传视频提示词.md").write_text(SORA_PROMPT, encoding="utf-8")

    make_zip(SUBMISSION_ROOT, ZIP_PATH)

    manifest = {
        "submission_root": str(SUBMISSION_ROOT),
        "zip_path": str(ZIP_PATH),
        "pdfs": [str(overview_pdf), str(gameplay_pdf), str(data_pdf), str(manual_pdf)],
        "video": str(promo_video),
        "charts": {key: str(value) for key, value in chart_paths.items()},
        "validation": validation,
    }
    with (ROOT / "output" / "prefinal_submission_manifest.json").open("w", encoding="utf-8") as handle:
        json.dump(manifest, handle, ensure_ascii=False, indent=2)
    print(json.dumps(manifest, ensure_ascii=False, indent=2))


def build_author_statement_pdf(path: Path, fonts: Dict[str, str], styles: Dict[str, ParagraphStyle]) -> None:
    doc = SimpleDocTemplate(str(path), pagesize=A4, leftMargin=1.7 * cm, rightMargin=1.7 * cm, topMargin=1.6 * cm, bottomMargin=1.6 * cm)
    story: List = []
    story.extend(create_story_header("作者信息与作品文字说明", "用于满足初赛提交中的作者信息与作品说明要求", styles))
    append_author_info(story, fonts, styles, include_work_description=True)
    story.append(Spacer(1, 0.18 * cm))
    story.append(p("作品定位", styles["heading"]))
    story.append(
        p(
            f"{WORK_TITLE}是一套面向化学实验室安全教育的轻量协作桌游，"
            "强调真实实验室风险情境中的判断、协作、处置和复盘。",
            styles["body"],
        )
    )
    story.append(Spacer(1, 0.12 * cm))
    story.append(p("核心玩法概述", styles["heading"]))
    for item in [
        "每轮先翻开任务牌，再出现与该任务相关的事件牌。",
        "团队从公共行动牌中选择应对措施，讨论如何兼顾安全与实验推进。",
        "处理正确时，任务推进并触发奖励；处理错误时，安全值、升级标记和隐患值会恶化。",
        "每张事件牌背面都包含正确处置、原因、知识点和复盘问题，便于教学使用。",
    ]:
        story.append(p(item, styles["bullet"]))
    story.append(Spacer(1, 0.12 * cm))
    story.append(p("作品价值", styles["heading"]))
    story.append(
        p(
            "本作品适合用于新生入组培训、实验室安全课程讨论和比赛现场展示。"
            "它的重点不是娱乐性，而是通过情境化决策训练帮助学生形成风险识别和规范处置意识。",
            styles["body"],
        )
    )
    doc.build(story)


def build_overview_pdf(path: Path, fonts: Dict[str, str], styles: Dict[str, ParagraphStyle], final_stats: Dict[str, object], cover_image: Path) -> None:
    doc = SimpleDocTemplate(str(path), pagesize=A4, leftMargin=1.7 * cm, rightMargin=1.7 * cm, topMargin=1.6 * cm, bottomMargin=1.6 * cm)
    story: List = []
    story.extend(create_story_header(f"{WORK_TITLE}作品总览", "面向化学院老师的初赛阅读入口", styles))

    intro_text = (
        f"{WORK_TITLE}是一套轻量协作式化学实验室安全培训桌游。"
        "玩家在 15 到 20 分钟内，通过“任务推进 + 风险事件处置 + 复盘知识点”完成一局实验室安全训练。"
    )
    story.append(p(intro_text, styles["body"]))
    story.append(Spacer(1, 0.16 * cm))
    append_author_info(story, fonts, styles)
    story.append(Spacer(1, 0.18 * cm))
    story.append(RLImage(str(cover_image), width=15.5 * cm, height=11.3 * cm))
    story.append(Spacer(1, 0.18 * cm))

    story.append(p("作品文字说明", styles["heading"]))
    story.append(p(WORK_WRITTEN_DESCRIPTION, styles["body"]))
    story.append(Spacer(1, 0.16 * cm))

    story.append(p("核心玩法四步", styles["heading"]))
    for item in [
        "1. 抽取 1 张实验任务牌，明确本轮实验目标。",
        "2. 从关联风险池中翻开 1 张事件牌，暴露实验室隐患。",
        "3. 团队从公共行动牌中选择应对措施，判断是否既控制风险又推进任务。",
        "4. 回合结算后复盘正确处置与知识点，形成训练闭环。",
    ]:
        story.append(p(item, styles["bullet"]))

    story.append(Spacer(1, 0.16 * cm))
    story.append(p("这套作品适合：新生入组培训、实验室安全教育、课堂安全讨论、比赛现场演示。", styles["body"]))
    story.append(Spacer(1, 0.12 * cm))
    story.append(
        p(
            f"建议先看同目录下的 02_宣传视频.mp4。当前最终长跑数据显示，标准模式 balanced+balanced 胜率为 {final_stats['balanced_standard_win_rate'] * 100:.2f}%，"
            f"教学模式胜率为 {final_stats['teaching_win_rate'] * 100:.2f}%。",
            styles["body"],
        )
    )

    story.append(Spacer(1, 0.22 * cm))
    story.append(p("压缩包阅读顺序", styles["heading"]))
    for item in [
        "00_请先看这里_作品总览.pdf：先认识作品、作者信息和核心价值。",
        "00a_作者信息与作品文字说明.pdf：查看作者简介与正式作品说明。",
        "01_一页玩法速览.pdf：快速理解一局怎么进行。",
        "02_宣传视频.mp4：不懂桌游也能先看懂作品要点。",
        "03_版本迭代与关键数据.pdf：看版本演化和最终封版数据。",
        "04_使用手册.pdf：详细规则与教学使用建议。",
    ]:
        story.append(p(item, styles["bullet"]))
    doc.build(story)


def build_onepager_pdf(path: Path, fonts: Dict[str, str], styles: Dict[str, ParagraphStyle]) -> None:
    doc = SimpleDocTemplate(str(path), pagesize=A4, leftMargin=1.7 * cm, rightMargin=1.7 * cm, topMargin=1.5 * cm, bottomMargin=1.5 * cm)
    story: List = []
    story.extend(create_story_header("一页玩法速览", "给不熟悉桌游的评委老师看的简明版说明", styles))
    story.append(p("作品定位", styles["heading"]))
    story.append(p("1 到 4 人，推荐 2 到 3 人，单局约 15 到 20 分钟。它不是竞技对抗桌游，而是以化学实验室风险识别和处置决策为核心的协作训练工具。", styles["body"]))
    story.append(p("一局怎么进行", styles["heading"]))
    for item in [
        "每轮先抽实验任务，再翻开与该任务相关的安全事件。",
        "团队从公共行动牌中选择 1 到 2 个动作，讨论怎样处理最合适。",
        "如果动作既解决事件又符合任务要求，就推进进度并触发奖励。",
        "如果处理错误，安全值下降、升级标记增加，隐患也可能积累。",
    ]:
        story.append(p(item, styles["bullet"]))

    story.append(p("怎么赢 / 怎么输", styles["heading"]))
    story.append(p("标准模式下，团队需要在 6 轮内完成至少 4 点进度，同时保持安全值大于 0、升级标记未爆表、隐患值未失控。", styles["body"]))
    story.append(Spacer(1, 0.12 * cm))
    story.append(p("失败通常来自三类原因：安全值归零、隐患失控、进度不足。这种设计会自然迫使玩家在“做实验”和“守规范”之间做出判断。", styles["body"]))

    story.append(p("为什么适合化学实验室安全培训", styles["heading"]))
    for item in [
        "风险事件全部来自典型化学实验室场景，而不是抽象口号。",
        "每张事件牌背后都对应“正确处置 + 原因 + 知识点 + 复盘问题”。",
        "规则足够轻，适合课堂、培训或比赛答辩现场快速演示。",
    ]:
        story.append(p(item, styles["bullet"]))

    story.append(Spacer(1, 0.18 * cm))
    story.append(p("作者信息", styles["heading"]))
    story.append(
        p(
            f"作者：{AUTHOR_INFO['name']}｜学号：{AUTHOR_INFO['student_id']}｜联系电话：{AUTHOR_INFO['phone']}｜电子邮箱：{AUTHOR_INFO['email']}",
            styles["small"],
        )
    )
    doc.build(story)


def build_manual_pdf(path: Path, fonts: Dict[str, str], styles: Dict[str, ParagraphStyle], sample_images: List[Path]) -> None:
    doc = SimpleDocTemplate(str(path), pagesize=A4, leftMargin=1.6 * cm, rightMargin=1.6 * cm, topMargin=1.5 * cm, bottomMargin=1.5 * cm)
    story: List = []
    story.extend(create_story_header("使用手册", "给初赛评委和后续培训老师的详细说明", styles))
    append_author_info(story, fonts, styles)
    story.append(Spacer(1, 0.14 * cm))

    story.append(p("1. 作品定位", styles["heading"]))
    story.append(p(f"{WORK_TITLE}是一套面向化学实验室安全教育的轻量协作桌游。它通过任务、事件、行动三类牌的互动，让玩家在短时间内练习风险识别、处置决策和复盘表达。", styles["body"]))
    story.append(Spacer(1, 0.12 * cm))
    story.append(p("推荐场景：新生入组教育、实验室安全培训、课堂讨论、小型公开展示。", styles["body"]))
    if sample_images:
        story.append(Spacer(1, 0.2 * cm))
        story.append(RLImage(str(sample_images[0]), width=15.0 * cm, height=11.0 * cm))

    story.append(PageBreak())
    story.append(p("2. 开局准备", styles["heading"]))
    for item in [
        "选择模式：教学 / 标准 / 挑战。",
        "洗混任务牌、事件牌和行动牌；将行动牌翻开 8 张组成公共手牌。",
        "如使用角色牌和策略牌，则在开局完成对应选择。",
        "初始化安全值、进度值、升级标记与隐患值。",
    ]:
        story.append(p(item, styles["bullet"]))

    story.append(p("3. 每轮流程", styles["heading"]))
    for item in [
        "先结算隐患带来的轮初压力，再翻开本轮任务牌。",
        "从该任务关联的事件池中翻开 1 张事件牌。",
        "团队从公共手牌中打出 1 到 2 张行动牌，讨论怎样处理最合适。",
        "若行动既解决事件又符合任务要求，则推进任务并触发奖励。",
        "翻看事件牌背面的正确处置与知识点，完成复盘。",
    ]:
        story.append(p(item, styles["bullet"]))

    story.append(PageBreak())
    story.append(p("4. 怎么赢，怎么输", styles["heading"]))
    story.append(p("标准模式下，团队需要在 6 轮内完成至少 4 点进度，同时保证安全值大于 0、升级标记未达到上限、隐患值未爆表。", styles["body"]))
    story.append(Spacer(1, 0.12 * cm))
    story.append(p("失败通常来自：处理错误导致安全值归零、隐患连续积压、进度不足，或高危事件被明显错误处置。", styles["body"]))

    story.append(p("5. 三种模式", styles["heading"]))
    mode_rows = [
        ["模式", "用途", "特点"],
        ["教学", "新手体验与课堂训练", "更高安全值、更多换牌机会、通关目标更低"],
        ["标准", "作品主展示模式", "在风险控制和任务推进之间保持平衡"],
        ["挑战", "高压演示或进阶体验", "初始压力更大，额外事件更多"],
    ]
    story.append(table_from_rows(mode_rows, fonts, [2.5 * cm, 4.8 * cm, 8.2 * cm]))

    story.append(PageBreak())
    story.append(p("6. 为什么适合化学实验室培训", styles["heading"]))
    for item in [
        "风险事件全部来自实验室常见场景，例如标签模糊、废液混放、通风控制失效、玻璃器皿裂纹、气瓶异常等。",
        "每轮不只是“答题”，而是让玩家在有限行动中做选择，因此更接近真实处置思路。",
        "每张事件牌背面都保留复盘知识点，方便老师讲解，也便于课后讨论。",
    ]:
        story.append(p(item, styles["bullet"]))
    story.append(p("7. 教学使用建议", styles["heading"]))
    for item in [
        "首次培训建议直接使用教学模式，重点看“为什么这样处置”。",
        "展示时可只演示 1 到 2 轮，不必完整跑完一局。",
        "如果时间有限，建议先放宣传视频，再用 1 张高代表性事件牌做现场讲解。",
    ]:
        story.append(p(item, styles["bullet"]))
    doc.build(story)


def main() -> None:
    ensure_dirs()
    fonts = register_fonts()
    styles = build_styles(fonts)

    final_run_dir = ROOT / "data" / "v0.8" / "run_003_v0_8_prefinal_longrun"
    final_summary = load_json(final_run_dir / "summary.json")
    final_team_rows = load_csv_rows(final_run_dir / "team_stats.csv")
    final_action_rows = load_csv_rows(final_run_dir / "action_stats.csv")
    final_task_rows = load_csv_rows(final_run_dir / "task_stats.csv")
    final_event_rows = load_csv_rows(final_run_dir / "event_stats.csv")

    teaching_row = get_row(final_team_rows, mode="teaching", team="balanced+balanced")
    challenge_row = get_row(final_team_rows, mode="challenge", team="balanced+balanced")
    version_rows = collect_version_stats()
    final_action_metrics = compute_action_rates(final_action_rows)
    final_tasks = compute_task_bottom(final_task_rows, 3)
    final_events = compute_tough_event_rows(final_event_rows, 5)

    final_bundle = {
        **final_summary,
        "teaching_win_rate": float(teaching_row["win_rate"]) if teaching_row else None,
        "challenge_win_rate": float(challenge_row["win_rate"]) if challenge_row else None,
    }
    validation = build_validation(version_rows[-1], final_tasks, final_action_metrics)

    chart_paths = {
        "standard": OUTPUT_CHARTS / "chart_standard_winrate.png",
        "scale": OUTPUT_CHARTS / "chart_content_scale.png",
        "action": OUTPUT_CHARTS / "chart_action_structure.png",
        "teaching": OUTPUT_CHARTS / "chart_teaching_mode.png",
    }
    plot_chart_standard(version_rows, chart_paths["standard"])
    plot_chart_scale(version_rows, chart_paths["scale"])
    plot_chart_action(version_rows, chart_paths["action"])
    plot_chart_teaching(version_rows, chart_paths["teaching"])

    overview_pdf = OUTPUT_PDF / "00_请先看这里_作品总览.pdf"
    author_pdf = OUTPUT_PDF / "00a_作者信息与作品文字说明.pdf"
    gameplay_pdf = OUTPUT_PDF / "01_一页玩法速览.pdf"
    data_pdf = OUTPUT_PDF / "03_版本迭代与关键数据.pdf"
    manual_pdf = OUTPUT_PDF / "04_使用手册.pdf"
    promo_video = OUTPUT_VIDEO / "02_宣传视频.mp4"

    build_overview_pdf(overview_pdf, fonts, styles, version_rows[-1], ROOT / "card" / "E02.png")
    build_author_statement_pdf(author_pdf, fonts, styles)
    build_onepager_pdf(gameplay_pdf, fonts, styles)
    build_data_pdf(data_pdf, fonts, styles, version_rows, chart_paths, final_bundle, final_tasks, final_events, final_action_metrics, validation)
    build_manual_pdf(manual_pdf, fonts, styles, [ROOT / "card" / "E02.png", ROOT / "card" / "E05.png"])
    build_video(promo_video, fonts)

    shutil.rmtree(SUBMISSION_ROOT, ignore_errors=True)
    ensure_dirs()
    copy_card_samples(SUBMISSION_ROOT / "05_样板卡图")
    copy_version_appendices(SUBMISSION_ROOT / "06_版本数据附录")

    for pdf_path in [overview_pdf, author_pdf, gameplay_pdf, data_pdf, manual_pdf]:
        shutil.copy2(pdf_path, SUBMISSION_ROOT / pdf_path.name)
    shutil.copy2(promo_video, SUBMISSION_ROOT / promo_video.name)

    shutil.copy2(chart_paths["standard"], SUBMISSION_ROOT / "06_版本数据附录" / "chart_standard_winrate.png")
    shutil.copy2(chart_paths["scale"], SUBMISSION_ROOT / "06_版本数据附录" / "chart_content_scale.png")
    shutil.copy2(chart_paths["action"], SUBMISSION_ROOT / "06_版本数据附录" / "chart_action_structure.png")
    shutil.copy2(chart_paths["teaching"], SUBMISSION_ROOT / "06_版本数据附录" / "chart_teaching_mode.png")

    save_csv(SUBMISSION_ROOT / "06_版本数据附录" / "版本趋势摘要.csv", version_rows)
    with (SUBMISSION_ROOT / "06_版本数据附录" / "最终长跑关键指标.json").open("w", encoding="utf-8") as handle:
        json.dump(
            {
                "final_summary": final_bundle,
                "final_action_metrics": final_action_metrics,
                "final_bottom_tasks": final_tasks,
                "final_tough_events": final_events,
                "validation": validation,
            },
            handle,
            ensure_ascii=False,
            indent=2,
        )
    (SUBMISSION_ROOT / "06_版本数据附录" / "00_Sora宣传视频提示词.md").write_text(SORA_PROMPT, encoding="utf-8")

    make_zip(SUBMISSION_ROOT, ZIP_PATH)

    manifest = {
        "submission_root": str(SUBMISSION_ROOT),
        "zip_path": str(ZIP_PATH),
        "pdfs": [str(overview_pdf), str(author_pdf), str(gameplay_pdf), str(data_pdf), str(manual_pdf)],
        "video": str(promo_video),
        "charts": {key: str(value) for key, value in chart_paths.items()},
        "validation": validation,
        "author": AUTHOR_INFO,
    }
    with (ROOT / "output" / "prefinal_submission_manifest.json").open("w", encoding="utf-8") as handle:
        json.dump(manifest, handle, ensure_ascii=False, indent=2)
    print(json.dumps(manifest, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
