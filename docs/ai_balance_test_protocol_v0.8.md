# 桌游平衡性测试规程 v0.8

## 1. 目标

本规程用于让任何后续 AI 或人工测试者，在不重新理解全部上下文的前提下，重复运行《实验室安全值班》`v0.8` 的平衡性测试，并把数据记录到统一格式。

当前有效版本为 `v0.8`。

## 2. 关键文件

- 当前规则：`C:\PKU\Term2\实验室安全作品大赛\boardgame_v0.8.md`
- 规则归档：`C:\PKU\Term2\实验室安全作品大赛\versions\v0.8\boardgame_rules.md`
- 当前模拟器：`C:\PKU\Term2\实验室安全作品大赛\simulation\run_v0_8_balance.py`
- 模拟器归档：`C:\PKU\Term2\实验室安全作品大赛\versions\v0.8\run_balance_sim.py`
- 版本日志：`C:\PKU\Term2\实验室安全作品大赛\CHANGELOG.md`
- 版本速记：`C:\PKU\Term2\实验室安全作品大赛\docs\version_memory.md`

## 3. 当前测试假设

若未明确提出新版本，不要改动以下假设：

- 公共手牌大小：`8`
- 每回合行动上限：`2`
- 标准 / 挑战模式通关目标为 `4` 点进度
- 教学模式通关目标为 `3` 点进度
- 首发 4 张策略牌继续沿用
- 任务与事件绑定：主事件必须从当前任务的关联事件池中抽取
- 存在“辅助行动保底结算”
- 隐患值达到 `3` 时，轮初安全值 `-1`
- 隐患值达到 `4` 时，立即失败
- 教学模式下，低危事件若结果为 `contained`，不增加隐患值
- 当前任务总数为 `12`
- 当前行动总类数为 `12`
- 当前事件总数为 `24`

## 4. 机器人与矩阵

当前模拟器内置 5 类机器人：

- `expert`
- `balanced`
- `safe`
- `learner`
- `reckless`

默认测试矩阵：

- 标准模式无策略：所有双人组合
- 教学模式无策略：只跑 `balanced+balanced`
- 挑战模式无策略：只跑 `balanced+balanced`
- 策略牌测试：`balanced+balanced` 在标准模式下分别测试四张首发策略牌

## 5. 标准执行方式

如工具能运行 Python，优先直接执行模拟器，不要手动逐局推演。

命令模板：

```powershell
python "C:\PKU\Term2\实验室安全作品大赛\simulation\run_v0_8_balance.py" `
  --games-per-team 3000 `
  --run-id run_XXX_description `
  --output-root "C:\PKU\Term2\实验室安全作品大赛\data\v0.8"
```

要求：

- `run_id` 必须唯一
- 当前有效正式基线为：`run_002_v0_8_refinement_teaching3`
- 正式跑数建议 `games-per-team >= 3000`
- 烟测可用 `50`、`100`、`200`

## 6. 输出文件要求

每次运行后，输出目录必须包含：

- `summary.json`
- `team_stats.csv`
- `action_stats.csv`
- `event_stats.csv`
- `task_stats.csv`
- `game_results.csv`
- `sample_turn_logs.jsonl`

## 7. 通过标准

当前以“精修完成并进入成品化准备”为目标，优先看以下指标：

- `balanced+balanced` 标准模式胜率：目标 `52%` 到 `56%`
- `balanced+balanced` 教学模式胜率：应明显高于标准模式
- `balanced+balanced` 挑战模式胜率：允许明显偏低，但不应低到接近 `0`
- `reckless+reckless` 标准模式胜率：应明显低于 `balanced+balanced`
- `T07` 完成率：不应继续位于极低区间
- `E18`：可继续优化，但不应导致系统性崩坏
- `stop + report` 合计选取率：不应回升到 `30%` 以上
- 新增 4 类行动合计选取率：最好保持在 `35%` 左右或更高

## 8. 问题处理顺序

如果结果不理想，不要一次改很多参数，按以下顺序处理：

1. 先判断是单卡问题，还是模式问题。
2. 若标准模式胜率波动过大，优先检查：
   - 任务与事件是否再次错位
   - 低危事件是否拖慢整体推进
3. 若教学模式失真，优先检查：
   - 通关目标是否过高或过低
   - 低危 contained 的隐患保护是否仍合理
   - 教学模式换牌次数和初始安全值是否需要微调
4. 若单张任务或事件异常，优先改单卡，不要先改全局。

## 9. 数据记录要求

每次跑新版本或新参数后，必须做 3 件事：

1. 新建独立数据目录，不要覆盖旧目录。
2. 在 `CHANGELOG.md` 记录版本或测试结果。
3. 若规则改动，先复制规则和模拟器到新版本目录，再继续迭代。

## 10. 如果只能用低成本 AI 手动模拟

若后续工具不能直接运行 Python，但能读写文件，按以下方式操作：

1. 最低限度测试 `balanced+balanced`、`balanced+learner`、`reckless+reckless`
2. 每组至少模拟 `100` 局
3. 每局记录：
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
4. 每回合记录：
   - `task_id`
   - `event_id`
   - `chosen_actions`
   - `outcome`
   - `task_completed`
   - `reward_applied`
   - `strategy_effects`
5. 汇总输出：
   - 胜率
   - 平均进度
   - 平均安全值
   - 平均隐患值
   - 各行动被选次数
   - 各任务出现次数与完成率
   - 各事件的 `full / partial / contained / error / blatant`

## 11. 禁止事项

- 不要覆盖历史 `run_id`
- 不要直接改 `versions/v0.1` 到 `versions/v0.8` 中的归档文件
- 不要在未留档的情况下直接覆盖当前规则
- 不要只写结论而不保留原始数据
