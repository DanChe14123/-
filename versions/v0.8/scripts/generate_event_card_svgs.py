from __future__ import annotations

from pathlib import Path
from textwrap import wrap
from xml.sax.saxutils import escape


ROOT = Path(__file__).resolve().parents[1]
OUTPUT_DIR = ROOT / "assets" / "events" / "fronts"
PREVIEW_DIR = ROOT / "assets" / "previews"

CARD_W = 750
CARD_H = 1050
ILLUS_X = 55
ILLUS_Y = 150
ILLUS_W = 640
ILLUS_H = 340
TEXT_X = 70

THEMES = {
    "low": {
        "label": "低危",
        "accent": "#4E83D9",
        "accent_dark": "#2D5FB3",
        "panel": "#EEF4FF",
        "bg": "#F8FBFF",
        "soft": "#DDEBFF",
    },
    "medium": {
        "label": "中危",
        "accent": "#F0A045",
        "accent_dark": "#C8741E",
        "panel": "#FFF4E7",
        "bg": "#FFF9F2",
        "soft": "#FFE2BF",
    },
    "high": {
        "label": "高危",
        "accent": "#D85A57",
        "accent_dark": "#AD3530",
        "panel": "#FFF0EF",
        "bg": "#FFF8F8",
        "soft": "#FFD7D6",
    },
}

CARDS = [
    {
        "id": "E02",
        "title": "试剂瓶标签模糊",
        "severity": "low",
        "scene": "你拿起准备使用的试剂瓶，发现标签字迹模糊，无法快速确认内容物和浓度。",
        "wrong": "不要凭记忆和瓶身颜色直接判断。",
        "focus": "无法被准确识别的试剂",
        "art": "blurred_label",
    },
    {
        "id": "E05",
        "title": "开放环境转移挥发性溶剂",
        "severity": "medium",
        "scene": "操作者在普通实验台上转移挥发性溶剂，周围没有有效局部排风。",
        "wrong": "不要认为“动作快一点”就能替代通风控制。",
        "focus": "操作地点错误，缺少局部排风",
        "art": "open_transfer",
    },
    {
        "id": "E08",
        "title": "玻璃器皿出现裂纹",
        "severity": "medium",
        "scene": "装液玻璃器皿上出现细裂纹，但当前步骤还没有结束。",
        "wrong": "不要抱着“先把这一步做完再换”的想法继续。",
        "focus": "裂纹器皿仍在待用",
        "art": "cracked_glass",
    },
    {
        "id": "E09",
        "title": "气瓶未固定",
        "severity": "medium",
        "scene": "气瓶处于可移动状态，固定链条或支架没有正确就位。",
        "wrong": "不要想着“先用一下，等会儿再固定”。",
        "focus": "钢瓶稳定性缺失",
        "art": "gas_cylinder",
    },
    {
        "id": "E13",
        "title": "皮肤接触腐蚀性液体",
        "severity": "high",
        "scene": "操作者手臂或手套被腐蚀性液体沾到，已出现明显不适反应。",
        "wrong": "不要先擦拭、忍耐或继续完成手头步骤。",
        "focus": "发生接触后需要立即冲洗",
        "art": "corrosive_contact",
    },
    {
        "id": "E15",
        "title": "实验台出现小型明火",
        "severity": "high",
        "scene": "实验台局部出现小型明火，旁边仍有电器、热源或可燃物。",
        "wrong": "不要慌乱拍打，也不要使用不合适的方法灭火。",
        "focus": "小火源已出现，周边条件不安全",
        "art": "small_fire",
    },
    {
        "id": "E21",
        "title": "旋蒸装置夹具松动",
        "severity": "medium",
        "scene": "旋蒸装置的夹具松动，或者收集瓶已经出现明显偏斜。",
        "wrong": "不要一边手扶装置一边继续转。",
        "focus": "设备姿态异常，不适合继续运行",
        "art": "rotavap",
    },
    {
        "id": "E23",
        "title": "未知粉末散落并引发不适",
        "severity": "high",
        "scene": "地面或台面散落未知粉末，附近人员已经出现刺激性不适。",
        "wrong": "不要直接扫走，也不要徒手判断是什么。",
        "focus": "未知物扩散，需要撤离警戒",
        "art": "unknown_powder",
    },
]


def svg_text(x: int, y: int, lines: list[str], size: int, fill: str, weight: str = "400", line_gap: int = 10) -> str:
    if not lines:
        return ""
    out = [
        f'<text x="{x}" y="{y}" fill="{fill}" font-size="{size}" '
        f'font-weight="{weight}" font-family="Microsoft YaHei, SimHei, sans-serif">'
    ]
    dy = 0
    for idx, line in enumerate(lines):
        if idx == 0:
            out.append(f'<tspan x="{x}" dy="0">{escape(line)}</tspan>')
            dy = size + line_gap
        else:
            out.append(f'<tspan x="{x}" dy="{dy}">{escape(line)}</tspan>')
            dy = size + line_gap
    out.append("</text>")
    return "".join(out)


def wrap_cn(text: str, width: int) -> list[str]:
    return wrap(text, width=width, break_long_words=True, replace_whitespace=False)


def shadow_defs() -> str:
    return """
    <defs>
      <filter id="cardShadow" x="-20%" y="-20%" width="140%" height="140%">
        <feDropShadow dx="0" dy="10" stdDeviation="12" flood-color="#000000" flood-opacity="0.18"/>
      </filter>
      <filter id="softShadow" x="-20%" y="-20%" width="140%" height="140%">
        <feDropShadow dx="0" dy="4" stdDeviation="6" flood-color="#000000" flood-opacity="0.12"/>
      </filter>
    </defs>
    """


def icon_pill(x: int, y: int, w: int, h: int, fill: str, stroke: str, text: str) -> str:
    return (
        f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{h/2}" fill="{fill}" stroke="{stroke}" stroke-width="2"/>'
        f'<text x="{x + w/2}" y="{y + h/2 + 9}" text-anchor="middle" fill="{stroke}" '
        f'font-size="26" font-weight="700" font-family="Microsoft YaHei, SimHei, sans-serif">{escape(text)}</text>'
    )


def draw_bench() -> str:
    return (
        '<rect x="100" y="315" width="540" height="34" rx="16" fill="#7E5B48"/>'
        '<rect x="125" y="347" width="22" height="56" rx="10" fill="#9B745F"/>'
        '<rect x="593" y="347" width="22" height="56" rx="10" fill="#9B745F"/>'
    )


def draw_person(x: int, y: int, coat: str = "#FFFFFF", skin: str = "#F6C7A5", accent: str = "#28334A", no_goggles: bool = False) -> str:
    goggles = "" if no_goggles else (
        f'<rect x="{x - 14}" y="{y + 2}" width="28" height="8" rx="4" fill="#7BC6FF" stroke="{accent}" stroke-width="2"/>'
    )
    return (
        f'<circle cx="{x}" cy="{y}" r="30" fill="{skin}" stroke="{accent}" stroke-width="4"/>'
        f'{goggles}'
        f'<rect x="{x - 32}" y="{y + 40}" width="64" height="88" rx="20" fill="{coat}" stroke="{accent}" stroke-width="4"/>'
        f'<line x1="{x - 18}" y1="{y + 58}" x2="{x - 60}" y2="{y + 110}" stroke="{accent}" stroke-width="10" stroke-linecap="round"/>'
        f'<line x1="{x + 18}" y1="{y + 58}" x2="{x + 70}" y2="{y + 120}" stroke="{accent}" stroke-width="10" stroke-linecap="round"/>'
        f'<line x1="{x - 12}" y1="{y + 128}" x2="{x - 24}" y2="{y + 200}" stroke="{accent}" stroke-width="12" stroke-linecap="round"/>'
        f'<line x1="{x + 12}" y1="{y + 128}" x2="{x + 24}" y2="{y + 200}" stroke="{accent}" stroke-width="12" stroke-linecap="round"/>'
    )


def draw_bottle(x: int, y: int, w: int = 80, h: int = 130, fill: str = "#9AD7A5", outline: str = "#28334A", label_fill: str = "#FFF7D9", cap: str = "#455A8B") -> str:
    return (
        f'<rect x="{x + 20}" y="{y}" width="{w - 40}" height="26" rx="8" fill="{cap}" stroke="{outline}" stroke-width="4"/>'
        f'<rect x="{x}" y="{y + 20}" width="{w}" height="{h}" rx="22" fill="{fill}" stroke="{outline}" stroke-width="4"/>'
        f'<rect x="{x + 14}" y="{y + 58}" width="{w - 28}" height="42" rx="12" fill="{label_fill}" stroke="{outline}" stroke-width="3"/>'
    )


def draw_lab_bg(theme: dict) -> str:
    return (
        f'<circle cx="130" cy="90" r="58" fill="{theme["soft"]}" opacity="0.6"/>'
        f'<circle cx="600" cy="110" r="72" fill="{theme["soft"]}" opacity="0.45"/>'
        '<rect x="58" y="58" width="44" height="88" rx="16" fill="#FFFFFF" opacity="0.55"/>'
        '<rect x="640" y="74" width="34" height="74" rx="12" fill="#FFFFFF" opacity="0.45"/>'
    )


def draw_blurred_label() -> str:
    return (
        draw_lab_bg(THEMES["low"])
        + draw_bench()
        + draw_person(180, 185, no_goggles=False)
        + draw_bottle(338, 160, w=106, h=154, fill="#8AD0B8")
        + '<rect x="364" y="230" width="56" height="18" rx="9" fill="#EAD9B8" opacity="0.75"/>'
        + '<rect x="360" y="256" width="64" height="16" rx="8" fill="#EAD9B8" opacity="0.5"/>'
        + '<rect x="498" y="202" width="118" height="95" rx="18" fill="#FFFDF6" stroke="#28334A" stroke-width="4"/>'
        + '<line x1="522" y1="226" x2="592" y2="226" stroke="#8EA0B4" stroke-width="5" stroke-linecap="round"/>'
        + '<line x1="522" y1="250" x2="590" y2="250" stroke="#8EA0B4" stroke-width="5" stroke-linecap="round"/>'
        + '<line x1="522" y1="274" x2="572" y2="274" stroke="#8EA0B4" stroke-width="5" stroke-linecap="round"/>'
        + '<circle cx="452" cy="242" r="20" fill="#FFD36F" stroke="#28334A" stroke-width="4"/>'
        + '<text x="452" y="249" text-anchor="middle" fill="#28334A" font-size="28" font-weight="700" font-family="Arial">?</text>'
    )


def draw_open_transfer() -> str:
    return (
        draw_lab_bg(THEMES["medium"])
        + draw_bench()
        + draw_person(185, 180)
        + draw_bottle(312, 168, w=88, h=126, fill="#9FD2F5", label_fill="#FFFFFF")
        + '<path d="M420 205 Q455 188 482 212 L510 236 Q525 250 521 270 Q516 292 492 298 Q468 304 454 284 L430 248 Q420 232 420 205 Z" fill="#78B4F5" opacity="0.72" stroke="#28334A" stroke-width="4"/>'
        + '<path d="M402 212 L438 235" stroke="#28334A" stroke-width="8" stroke-linecap="round"/>'
        + '<rect x="515" y="150" width="112" height="126" rx="24" fill="#FFF3D3" stroke="#28334A" stroke-width="4"/>'
        + '<path d="M565 168 L565 248" stroke="#C8741E" stroke-width="8" stroke-linecap="round"/>'
        + '<path d="M545 210 L585 210" stroke="#C8741E" stroke-width="8" stroke-linecap="round"/>'
        + '<path d="M548 185 Q566 168 582 186" fill="none" stroke="#F0A045" stroke-width="6" stroke-linecap="round"/>'
    )


def draw_cracked_glass() -> str:
    return (
        draw_lab_bg(THEMES["medium"])
        + draw_bench()
        + '<path d="M350 125 L398 125 L410 182 L452 275 Q468 310 444 330 Q424 348 374 348 Q324 348 304 330 Q280 310 296 275 L338 182 Z" fill="#CDE8FF" stroke="#28334A" stroke-width="5"/>'
        + '<path d="M372 172 L390 216 L364 240 L392 274 L358 314" fill="none" stroke="#D85A57" stroke-width="6" stroke-linecap="round" stroke-linejoin="round"/>'
        + '<circle cx="520" cy="190" r="30" fill="#FFFFFF" stroke="#28334A" stroke-width="4"/>'
        + '<line x1="505" y1="176" x2="535" y2="206" stroke="#28334A" stroke-width="6" stroke-linecap="round"/>'
        + '<line x1="535" y1="176" x2="505" y2="206" stroke="#28334A" stroke-width="6" stroke-linecap="round"/>'
        + '<path d="M160 226 Q186 188 232 196 Q284 208 276 258 Q270 298 230 310 Q190 320 162 292 Q144 272 146 248 Q148 236 160 226 Z" fill="#FFFFFF" stroke="#28334A" stroke-width="4"/>'
        + '<text x="212" y="262" text-anchor="middle" fill="#D85A57" font-size="44" font-weight="800" font-family="Arial">!</text>'
    )


def draw_gas_cylinder() -> str:
    return (
        draw_lab_bg(THEMES["medium"])
        + '<rect x="330" y="88" width="120" height="268" rx="56" fill="#69B6A3" stroke="#28334A" stroke-width="5"/>'
        + '<rect x="368" y="60" width="44" height="34" rx="12" fill="#455A8B" stroke="#28334A" stroke-width="4"/>'
        + '<circle cx="390" cy="206" r="22" fill="#FFFFFF" stroke="#28334A" stroke-width="4"/>'
        + '<path d="M286 150 L316 175 L316 278" fill="none" stroke="#B1B8C7" stroke-width="10" stroke-linecap="round"/>'
        + '<path d="M494 150 L468 175 L468 278" fill="none" stroke="#B1B8C7" stroke-width="10" stroke-linecap="round"/>'
        + '<path d="M270 178 Q314 204 332 214" fill="none" stroke="#D85A57" stroke-width="8" stroke-dasharray="16 12" stroke-linecap="round"/>'
        + '<path d="M510 178 Q468 204 448 214" fill="none" stroke="#D85A57" stroke-width="8" stroke-dasharray="16 12" stroke-linecap="round"/>'
        + '<rect x="290" y="308" width="200" height="38" rx="16" fill="#7E5B48"/>'
        + '<circle cx="544" cy="126" r="26" fill="#FFF3D3" stroke="#28334A" stroke-width="4"/>'
        + '<text x="544" y="136" text-anchor="middle" fill="#C8741E" font-size="34" font-weight="800" font-family="Arial">!</text>'
    )


def draw_corrosive_contact() -> str:
    return (
        draw_lab_bg(THEMES["high"])
        + draw_person(182, 182)
        + '<line x1="250" y1="245" x2="382" y2="245" stroke="#28334A" stroke-width="8" stroke-linecap="round"/>'
        + '<path d="M368 206 Q418 180 460 212 Q488 236 484 276 Q480 322 432 334 Q394 342 370 316 Q344 288 350 250 Q352 220 368 206 Z" fill="#D85A57" opacity="0.16" stroke="#D85A57" stroke-width="6"/>'
        + '<path d="M402 198 C392 222 402 236 408 250 C414 238 430 228 422 205 C418 193 408 190 402 198 Z" fill="#D85A57" stroke="#28334A" stroke-width="4"/>'
        + '<rect x="520" y="124" width="110" height="190" rx="30" fill="#E1F4FF" stroke="#28334A" stroke-width="4"/>'
        + '<path d="M575 140 L575 194" stroke="#4E83D9" stroke-width="10" stroke-linecap="round"/>'
        + '<path d="M550 170 L600 170" stroke="#4E83D9" stroke-width="10" stroke-linecap="round"/>'
        + '<path d="M540 214 Q575 242 610 214" fill="none" stroke="#4E83D9" stroke-width="8" stroke-linecap="round"/>'
        + '<circle cx="575" cy="250" r="8" fill="#5BC4FF"/>'
        + '<circle cx="558" cy="276" r="8" fill="#5BC4FF"/>'
        + '<circle cx="592" cy="278" r="8" fill="#5BC4FF"/>'
    )


def draw_flame(x: int, y: int, scale: float = 1.0) -> str:
    outer = f'M{x} {y+78*scale} C{x-44*scale} {y+26*scale} {x-6*scale} {y-14*scale} {x+6*scale} {y-56*scale} C{x+14*scale} {y-22*scale} {x+60*scale} {y+2*scale} {x+54*scale} {y+58*scale} C{x+48*scale} {y+108*scale} {x+8*scale} {y+126*scale} {x} {y+78*scale} Z'
    inner = f'M{x+4*scale} {y+74*scale} C{x-18*scale} {y+38*scale} {x+8*scale} {y+4*scale} {x+12*scale} {y-24*scale} C{x+22*scale} {y+8*scale} {x+40*scale} {y+24*scale} {x+32*scale} {y+64*scale} C{x+26*scale} {y+92*scale} {x+6*scale} {y+94*scale} {x+4*scale} {y+74*scale} Z'
    return (
        f'<path d="{outer}" fill="#FF8B3D" stroke="#28334A" stroke-width="5"/>'
        f'<path d="{inner}" fill="#FFD363" stroke="#28334A" stroke-width="4"/>'
    )


def draw_small_fire() -> str:
    return (
        draw_lab_bg(THEMES["high"])
        + draw_bench()
        + '<rect x="460" y="154" width="118" height="72" rx="18" fill="#E3E8F3" stroke="#28334A" stroke-width="4"/>'
        + '<circle cx="488" cy="190" r="8" fill="#455A8B"/>'
        + '<circle cx="520" cy="190" r="8" fill="#455A8B"/>'
        + draw_flame(356, 208, 1.0)
        + '<path d="M302 130 Q335 112 366 130" fill="none" stroke="#D85A57" stroke-width="7" stroke-linecap="round"/>'
        + '<path d="M284 112 Q332 86 386 108" fill="none" stroke="#D85A57" stroke-width="5" stroke-linecap="round" opacity="0.7"/>'
        + '<rect x="162" y="176" width="84" height="130" rx="18" fill="#FFFFFF" stroke="#28334A" stroke-width="4"/>'
        + '<line x1="204" y1="176" x2="204" y2="306" stroke="#28334A" stroke-width="4"/>'
    )


def draw_rotavap() -> str:
    return (
        draw_lab_bg(THEMES["medium"])
        + '<rect x="148" y="310" width="470" height="36" rx="16" fill="#7E5B48"/>'
        + '<rect x="188" y="172" width="110" height="112" rx="24" fill="#E2E8F2" stroke="#28334A" stroke-width="4"/>'
        + '<circle cx="242" cy="228" r="34" fill="#C8D4E6" stroke="#28334A" stroke-width="4"/>'
        + '<rect x="356" y="120" width="18" height="138" rx="9" fill="#8897B0"/>'
        + '<path d="M364 202 L452 178" stroke="#8897B0" stroke-width="10" stroke-linecap="round"/>'
        + '<path d="M452 178 L516 222" stroke="#8897B0" stroke-width="10" stroke-linecap="round"/>'
        + '<rect x="514" y="220" width="68" height="106" rx="22" transform="rotate(14 548 273)" fill="#D3EDFF" stroke="#28334A" stroke-width="4"/>'
        + '<path d="M418 160 L448 146" stroke="#D85A57" stroke-width="8" stroke-linecap="round"/>'
        + '<path d="M452 144 L480 164" stroke="#D85A57" stroke-width="8" stroke-linecap="round"/>'
        + '<circle cx="554" cy="148" r="28" fill="#FFF3D3" stroke="#28334A" stroke-width="4"/>'
        + '<text x="554" y="158" text-anchor="middle" fill="#C8741E" font-size="36" font-weight="800" font-family="Arial">!</text>'
    )


def draw_unknown_powder() -> str:
    return (
        draw_lab_bg(THEMES["high"])
        + '<rect x="100" y="312" width="540" height="34" rx="16" fill="#CBD4E2"/>'
        + '<path d="M250 312 Q278 286 320 304 Q352 318 380 302 Q420 280 452 312 Z" fill="#E8E0BE" stroke="#28334A" stroke-width="4"/>'
        + '<circle cx="302" cy="286" r="6" fill="#E8E0BE"/>'
        + '<circle cx="338" cy="282" r="5" fill="#E8E0BE"/>'
        + '<circle cx="360" cy="292" r="7" fill="#E8E0BE"/>'
        + draw_person(160, 184)
        + '<path d="M218 246 L286 222" stroke="#28334A" stroke-width="10" stroke-linecap="round"/>'
        + '<path d="M548 188 Q506 150 470 188 Q438 220 452 268 Q466 316 520 318 Q566 318 590 280" fill="none" stroke="#28334A" stroke-width="10" stroke-linecap="round"/>'
        + '<circle cx="518" cy="180" r="28" fill="#F6C7A5" stroke="#28334A" stroke-width="4"/>'
        + '<path d="M504 184 Q518 198 532 184" fill="none" stroke="#D85A57" stroke-width="5" stroke-linecap="round"/>'
        + '<path d="M132 110 Q152 88 184 102" fill="none" stroke="#D85A57" stroke-width="7" stroke-linecap="round"/>'
        + '<path d="M542 102 Q566 86 592 108" fill="none" stroke="#D85A57" stroke-width="7" stroke-linecap="round"/>'
    )


ART = {
    "blurred_label": draw_blurred_label,
    "open_transfer": draw_open_transfer,
    "cracked_glass": draw_cracked_glass,
    "gas_cylinder": draw_gas_cylinder,
    "corrosive_contact": draw_corrosive_contact,
    "small_fire": draw_small_fire,
    "rotavap": draw_rotavap,
    "unknown_powder": draw_unknown_powder,
}


def build_card(card: dict) -> str:
    theme = THEMES[card["severity"]]
    title_lines = wrap_cn(card["title"], 12)
    scene_lines = wrap_cn(card["scene"], 18)
    wrong_lines = wrap_cn(card["wrong"], 18)
    focus_lines = wrap_cn(card["focus"], 14)

    title_y = 560
    scene_y = 670
    wrong_y = 880

    return f"""<svg xmlns="http://www.w3.org/2000/svg" width="{CARD_W}" height="{CARD_H}" viewBox="0 0 {CARD_W} {CARD_H}">
    {shadow_defs()}
    <rect x="28" y="24" width="{CARD_W - 56}" height="{CARD_H - 48}" rx="36" fill="{theme["bg"]}" filter="url(#cardShadow)"/>
    <rect x="28" y="24" width="{CARD_W - 56}" height="{CARD_H - 48}" rx="36" fill="none" stroke="#28334A" stroke-width="4"/>
    <rect x="28" y="24" width="{CARD_W - 56}" height="96" rx="36" fill="{theme["accent"]}"/>
    <rect x="28" y="84" width="{CARD_W - 56}" height="36" fill="{theme["accent"]}"/>
    {icon_pill(55, 48, 110, 46, "#FFFFFF", theme["accent_dark"], card["id"])}
    {icon_pill(178, 48, 96, 46, theme["panel"], theme["accent_dark"], theme["label"])}
    <text x="666" y="80" text-anchor="end" fill="#FFFFFF" font-size="28" font-weight="700" font-family="Microsoft YaHei, SimHei, sans-serif">事件牌</text>

    <rect x="{ILLUS_X}" y="{ILLUS_Y}" width="{ILLUS_W}" height="{ILLUS_H}" rx="30" fill="{theme["panel"]}" stroke="#28334A" stroke-width="4" filter="url(#softShadow)"/>
    <g transform="translate({ILLUS_X - 10},{ILLUS_Y - 10})">
      {ART[card["art"]]()}
    </g>

    <rect x="55" y="525" width="640" height="210" rx="28" fill="#FFFFFF" stroke="#28334A" stroke-width="4"/>
    <rect x="55" y="750" width="640" height="206" rx="28" fill="{theme["panel"]}" stroke="#28334A" stroke-width="4"/>

    {svg_text(TEXT_X, title_y, title_lines, 42, "#28334A", "700", 8)}
    <rect x="70" y="620" width="208" height="38" rx="19" fill="{theme["soft"]}" stroke="none"/>
    <text x="174" y="646" text-anchor="middle" fill="{theme["accent_dark"]}" font-size="22" font-weight="700" font-family="Microsoft YaHei, SimHei, sans-serif">观察重点</text>
    {svg_text(70, scene_y, scene_lines, 28, "#344054", "400", 6)}

    <rect x="70" y="780" width="150" height="38" rx="19" fill="{theme["accent"]}" opacity="0.18"/>
    <text x="145" y="806" text-anchor="middle" fill="{theme["accent_dark"]}" font-size="22" font-weight="700" font-family="Microsoft YaHei, SimHei, sans-serif">错误倾向</text>
    {svg_text(70, wrong_y, wrong_lines, 28, "#28334A", "500", 6)}
    {svg_text(520, 806, focus_lines, 24, theme["accent_dark"], "700", 4)}
    <circle cx="640" cy="796" r="22" fill="{theme["accent"]}"/>
    <text x="640" y="804" text-anchor="middle" fill="#FFFFFF" font-size="28" font-weight="800" font-family="Arial">!</text>
    </svg>"""


def build_manifest(cards: list[dict]) -> str:
    lines = [
        "# 首批卡通事件牌清单",
        "",
        "以下文件由 `scripts/generate_event_card_svgs_v0_8.py` 生成。",
        "",
    ]
    for card in cards:
        lines.append(f'- `{card["id"]}` {card["title"]} -> `assets/events/fronts/{card["id"]}_front.svg`')
    lines.append("")
    return "\n".join(lines)


def main() -> None:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    PREVIEW_DIR.mkdir(parents=True, exist_ok=True)
    for card in CARDS:
        (OUTPUT_DIR / f'{card["id"]}_front.svg').write_text(build_card(card), encoding="utf-8")
    (PREVIEW_DIR / "event_batch1_manifest.md").write_text(build_manifest(CARDS), encoding="utf-8")


if __name__ == "__main__":
    main()
