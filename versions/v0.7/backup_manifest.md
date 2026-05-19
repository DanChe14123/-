# v0.7 备份说明

## 版本定位

`v0.7` 是“事件池扩容版”。

本轮核心目标是把事件牌从 `16` 张扩到 `24` 张，并验证 `v0.6` 中已经展开的行动层，能否在更厚的事件环境下继续稳定运行。

## 归档文件

- 规则归档：`C:\PKU\Term2\实验室安全作品大赛\versions\v0.7\boardgame_rules.md`
- 模拟器归档：`C:\PKU\Term2\实验室安全作品大赛\versions\v0.7\run_balance_sim.py`

## 源文件

- 当前规则：`C:\PKU\Term2\实验室安全作品大赛\boardgame_v0.7.md`
- 当前模拟器：`C:\PKU\Term2\实验室安全作品大赛\simulation\run_v0_7_balance.py`

## 数据备份

- 烟测数据：`C:\PKU\Term2\实验室安全作品大赛\data\v0.7\smoke_test_v0_7_events_tuned`
- 正式数据：`C:\PKU\Term2\实验室安全作品大赛\data\v0.7\run_001_v0_7_event_expansion`

## 关联文档

- 版本日志：`C:\PKU\Term2\实验室安全作品大赛\CHANGELOG.md`
- 版本速记：`C:\PKU\Term2\实验室安全作品大赛\docs\version_memory.md`
- 测试规程：`C:\PKU\Term2\实验室安全作品大赛\docs\ai_balance_test_protocol_v0.7.md`
- 评估结论：`C:\PKU\Term2\实验室安全作品大赛\docs\v0.7_event_expansion_assessment.md`

## 本轮结论

- `balanced+balanced` 无策略标准模式胜率 `50.53%`
- 24 张事件全部稳定进入牌池
- 新增 4 类行动合计选取率 `36.57%`
- `secure` 选取率从 `2.18%` 提升到 `4.61%`
- `v0.7` 可以作为后续单卡精修与成品化准备的新稳定基线
