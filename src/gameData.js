import rawCardData from "../content/v2_cards.json";

export const cards = rawCardData.cards;

export const TYPE_LABELS = {
  task: "任务",
  event: "事件",
  action: "行动",
  role: "角色",
  post: "岗位",
  strategy: "策略",
  debrief: "复盘",
};

export const PHASE_LABELS = {
  prepare: "准备",
  operate: "操作",
  close: "收尾",
  emergency: "应急",
  any: "通用",
  setup: "开局",
  round: "回合",
  debrief: "复盘",
};

export const RISK_LABELS = {
  hint: "苗头",
  exposed: "暴露",
  critical: "失控",
};

export const RISK_ORDER = ["hint", "exposed", "critical"];

export const SEVERITY_LABELS = {
  low: "低危",
  medium: "中危",
  high: "高危",
};

export const DIFFICULTIES = {
  teaching: {
    key: "teaching",
    label: "教学模式",
    safety: 12,
    targetProgress: 5,
    maxRounds: 8,
    handLimit: 8,
    redraws: 3,
    summary: "容错更高，适合第一次讲解规则。",
  },
  standard: {
    key: "standard",
    label: "标准模式",
    safety: 10,
    targetProgress: 5,
    maxRounds: 8,
    handLimit: 7,
    redraws: 2,
    summary: "接近 v2.0 平衡基准的推荐模式。",
  },
  challenge: {
    key: "challenge",
    label: "挑战模式",
    safety: 10,
    targetProgress: 6,
    maxRounds: 8,
    handLimit: 6,
    redraws: 1,
    initialHazard: 1,
    summary: "风险压力更高，第 4 轮进入应急节奏。",
  },
};

export const POST_KEYS = {
  P01: "safety_officer",
  P02: "operator",
  P03: "recorder",
  P04: "resource_manager",
};

export const POST_ACCENTS = {
  P01: "green",
  P02: "amber",
  P03: "blue",
  P04: "teal",
};

export const CARD_FOLDERS = {
  event: "events",
  task: "tasks",
  action: "actions",
  role: "roles",
  post: "posts",
  strategy: "strategies",
  debrief: "debriefs",
};

export const cardsByType = cards.reduce((acc, card) => {
  if (!acc[card.card_type]) acc[card.card_type] = [];
  acc[card.card_type].push(card);
  return acc;
}, {});

export const cardsById = Object.fromEntries(cards.map((card) => [card.id, card]));

export function cardImagePath(card, side = "front") {
  if (!card) return "";
  const folder = CARD_FOLDERS[card.card_type];
  return `/card/final/v2/${folder}/${card.id}_${side}.png`;
}

export function formatTag(tag) {
  const labels = {
    ppe: "PPE",
    label: "标签",
    record: "记录",
    verify: "核对",
    inspect: "检查",
    ventilation: "通风",
    clean: "清洁",
    waste: "废液",
    isolate: "隔离",
    contain: "围堵",
    report: "上报",
    emergency: "应急",
    evacuate: "撤离",
    shutdown: "断电",
    secure: "固定",
    replace: "更换",
    monitor: "监测",
    communicate: "交接",
    review: "复盘",
    resource: "资源",
    guard: "警戒",
    heat: "热源",
    fire: "火情",
    solvent: "溶剂",
    corrosive: "腐蚀",
    exposure: "暴露",
    unknown: "未知物",
    equipment: "设备",
  };
  return labels[tag] ?? tag;
}
