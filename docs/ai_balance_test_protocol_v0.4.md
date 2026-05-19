# 桌游平衡性测试规程 v0.4

## 1. 目标

本规程用于让任何后续 AI 或人工测试者，在不重新理解全部上下文的前提下，重复运行《实验室安全值班》的平衡性测试，并把数据记录到统一格式。

当前有效版本为 `v0.4`。

## 2. 关键文件

- 当前规则：`C:\PKU\Term2\实验室安全作品大赛\boardgame_v0.4.md`
- 规则归档：`C:\PKU\Term2\实验室安全作品大赛\versions\v0.4\boardgame_rules.md`
- 当前模拟器：`C:\PKU\Term2\实验室安全作品大赛\simulation\run_v0_4_balance.py`
- 模拟器归档：`C:\PKU\Term2\实验室安全作品大赛\versions\v0.4\run_balance_sim.py`
- 版本日志：`C:\PKU\Term2\实验室安全作品大赛\CHANGELOG.md`

## 3. 当前测试假设

若未明确提出新版本，不要改动以下假设：

- 公共手牌大小：6
- 每回合行动上限：2
- 标准模式通关目标：4 点进度
- 教学模式通关目标：4 点进度
- 挑战模式通关目标：4 点进度
- `v0.4` 首发 4 张策略牌已经上线
- 任务与事件绑定：主事件必须从当前任务的关联事件池中抽取
- 若未打出关键行动但打出合理辅助行动，记为“风险控制成功但任务未推进”
- 隐患值达到 `3` 时，轮初安全值 -1
- 隐患值达到 `4` 时，立即失败
- 任务完成后立即触发任务奖励

## 4. 机器人策略

当前模拟器内置 5 类机器人：

- `expert`：高知识水平，积极换牌，优先关键行动和协同
- `balanced`：当前主参考机器人，用于估计普通认真玩家表现
- `safe`：偏保守，偏好 `暂停操作` / `上报负责人`
- `learner`：存在一定知识噪声，代表新手或训练不足玩家
- `reckless`：低换牌、低保守性，用于压力测试

默认测试矩阵：

- 标准模式无策略：所有无序双人组合
- 教学模式无策略：只跑 `balanced+balanced`
- 挑战模式无策略：只跑 `balanced+balanced`
- 策略牌测试：`balanced+balanced` 在标准模式下分别测试首发策略牌

## 5. 标准执行方式

如果测试工具能运行 Python，优先直接执行模拟器，不要手动逐局推演。

命令模板：

```powershell
python "C:\PKU\Term2\实验室安全作品大赛\simulation\run_v0_4_balance.py" `
  --games-per-team 3000 `
  --run-id run_XXX_description `
  --output-root "C:\PKU\Term2\实验室安全作品大赛\data\v0.4"
```

要求：

- `run-id` 必须唯一，不能覆盖历史数据
- 正式跑数建议 `games-per-team >= 3000`
- 烟测可以用 `20` 或 `50`

## 6. 输出文件要求

每次运行后，输出目录必须包含：

- `summary.json`
- `team_stats.csv`
- `action_stats.csv`
- `event_stats.csv`
- `game_results.csv`
- `sample_turn_logs.jsonl`

这些文件的作用：

- `summary.json`：快速查看本次跑数结论
- `team_stats.csv`：看不同队伍在不同模式下的胜率与平均状态
- `action_stats.csv`：看卡牌选取率
- `event_stats.csv`：看每个事件的处理结果分布
- `game_results.csv`：逐局结果，便于二次分析
- `sample_turn_logs.jsonl`：抽样回合日志，便于查异常

## 7. 通过标准

当前以“适合 Demo 和初赛提交”为目标，优先看以下指标：

- `balanced+balanced` 在标准模式胜率：目标 `50% 到 65%`
- `balanced+balanced` 在教学模式胜率：目标 `55% 以上`
- `reckless+reckless` 在标准模式胜率：应明显低于 `balanced+balanced`
- `upgrade_limit` 失败数：不应高到接近主要失败原因
- `hazard_overflow` 和 `hazard_pressure`：不应取代 `safety_zero` 成为唯一主要失败来源
- `action_stats.csv` 中 `stop` 和 `report`：可以较高，但不应压倒性垄断
- `event_stats.csv` 中单一事件的 `blatant_rate`：若持续高于 `30%`，优先检查该事件
- `avg_tasks_completed`：标准模式下应接近 `3.3` 到 `4.2`
- 策略牌场景下：同一队伍不同策略的胜率差距最好不超过 `15%`

## 8. 发现问题后的处理顺序

如果测试结果不理想，不要一次改很多参数。按以下顺序处理：

1. 先判断是“难度问题”还是“信息表达问题”
2. 若胜率过低，优先调整：
   - 手牌数量
   - 通关进度目标
   - 错误惩罚
   - 辅助行动是否有保底价值
3. 若 `stop/report` 选取率过高，优先调整：
   - 具体事件是否过度奖励保守行动
   - 任务偏好动作是否给得太弱
   - 是否缺少更细分的行动牌
4. 若单个事件异常难，优先改该事件，不要先改全局
5. 若隐患相关失败过多，优先调整：
   - 隐患加压阈值
   - 任务奖励强度
   - 完全正确时的隐患清除收益
6. 若不同策略牌的行动牌选取率差异很小，优先调整：
   - 策略牌的长期约束
   - 策略牌与任务奖励的联动
   - 行动牌的细分程度

## 9. 数据记录要求

每次跑新版本或新参数后，必须做 3 件事：

1. 新建独立数据目录，不覆盖旧目录
2. 在 `CHANGELOG.md` 增加一条版本或测试记录
3. 如果规则变动，先复制规则文件到新版本目录，再改新文件

## 10. 如果只能用低成本 AI 手动模拟

如果后续工具不能直接运行 Python，但仍能读写文件，请按以下方式操作：

1. 只测试 `balanced+balanced`、`balanced+learner`、`reckless+reckless`
2. 每组至少模拟 `100` 局
3. 每局都记录以下字段：
   - `mode`
   - `team`
   - `strategy_id`
   - `game_index`
   - `result`
   - `loss_reason`
   - `progress`
   - `safety`
   - `upgrade`
   - `hazards`
   - `redraws_used`
4. 每回合记录以下字段：
   - `task_id`
   - `event_id`
   - `chosen_actions`
   - `outcome`
   - `task_completed`
   - `reward_applied`
   - `strategy_effects`
5. 汇总出：
   - 胜率
   - 平均进度
   - 平均安全值
   - 平均隐患值
   - 各行动被选次数
   - 各事件的 `full / partial / contained / error / blatant`

## 11. 禁止事项

- 不要覆盖历史 `run_id`
- 不要直接改 `versions/v0.1`
- 不要在未留档的情况下直接改当前规则
- 不要只给结论而不保留原始数据文件
