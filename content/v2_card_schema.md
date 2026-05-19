# v2 卡牌数据结构

## 1. 总体原则

`v2` 不再用散文档维护卡牌，而使用结构化 JSON 作为卡牌真源。

卡牌文本、模拟器、说明书和后续卡面制作都应尽量从 `content/v2_cards.json` 派生。

## 2. card_type

允许的卡牌类型：

- `task`
- `event`
- `action`
- `role`
- `post`
- `strategy`
- `debrief`

## 3. 通用字段

每张牌至少包含：

- `id`：唯一编号
- `card_type`：卡牌类型
- `name`：名称
- `phase`：所属阶段或适用阶段
- `tags`：标签数组
- `summary`：一句话说明

## 4. task 字段

任务牌字段：

- `stage`：`prepare / operate / close / emergency`
- `progress`：完成后进度
- `preferred_actions`：优先行动标签
- `risk_tags`：关联风险标签
- `reward`：任务奖励类型
- `knowledge`：对应教学点

## 5. event 字段

事件牌字段：

- `severity`：`low / medium / high`
- `initial_state`：`hint / exposed / critical`
- `risk_tags`
- `key_actions`
- `support_actions`
- `conflict_actions`
- `knowledge`
- `debrief_id`

## 6. action 字段

行动牌字段：

- `action_tags`
- `post_bonus`：适配岗位
- `strength`：`basic / strong / emergency`
- `limits`：边界说明

## 7. role 字段

角色牌字段：

- `ability_timing`
- `ability`
- `preferred_posts`
- `risk`

## 8. post 字段

岗位牌字段：

- `responsibility`
- `bonus_condition`
- `contribution_rule`

## 9. strategy 字段

策略牌字段：

- `effect`
- `cost`
- `playstyle`

## 10. debrief 字段

复盘牌字段：

- `knowledge_point`
- `correct_action`
- `why`
- `review_question`

