# v0.6 备份说明

## 版本定位

`v0.6` 是“行动层扩容版”。

本轮核心目标是把行动牌从 `8` 类扩到 `12` 类，并验证新行动能否真正进入局内决策，而不是只停留在规则文本里。

## 归档文件

- 规则归档：`C:\PKU\Term2\实验室安全作品大赛\versions\v0.6\boardgame_rules.md`
- 模拟器归档：`C:\PKU\Term2\实验室安全作品大赛\versions\v0.6\run_balance_sim.py`

## 源文件

- 当前规则：`C:\PKU\Term2\实验室安全作品大赛\boardgame_v0.6.md`
- 当前模拟器：`C:\PKU\Term2\实验室安全作品大赛\simulation\run_v0_6_balance.py`

## 数据备份

- 烟测数据：`C:\PKU\Term2\实验室安全作品大赛\data\v0.6\smoke_test_v0_6_actions_hand8_redrawfix`
- 正式数据：`C:\PKU\Term2\实验室安全作品大赛\data\v0.6\run_001_v0_6_action_expansion`

## 关联文档

- 版本日志：`C:\PKU\Term2\实验室安全作品大赛\CHANGELOG.md`
- 版本速记：`C:\PKU\Term2\实验室安全作品大赛\docs\version_memory.md`
- 测试规程：`C:\PKU\Term2\实验室安全作品大赛\docs\ai_balance_test_protocol_v0.6.md`
- 评估结论：`C:\PKU\Term2\实验室安全作品大赛\docs\v0.6_action_expansion_assessment.md`

## 本轮结论

- `balanced+balanced` 无策略标准模式胜率 `52.07%`
- `stop + report` 合计选取率从 `39.82%` 降到 `26.12%`
- 新增 4 类行动合计选取率 `34.10%`
- 行动层扩容成功，`v0.6` 可作为后续扩事件池的新稳定基线
