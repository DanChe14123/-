# v0.8 备份说明

## 版本定位

`v0.8` 是“精修版”。

本轮核心目标是在不新增系统的前提下，修正 `v0.7` 的明显弱项，并把教学模式调回真正的入门训练模式。

## 归档文件

- 规则归档：`C:\PKU\Term2\实验室安全作品大赛\versions\v0.8\boardgame_rules.md`
- 模拟器归档：`C:\PKU\Term2\实验室安全作品大赛\versions\v0.8\run_balance_sim.py`
- 卡牌模板归档：`C:\PKU\Term2\实验室安全作品大赛\versions\v0.8\card_information_template.md`
- 事件牌文本库归档：`C:\PKU\Term2\实验室安全作品大赛\versions\v0.8\event_cards.md`
- Gemini 提示词包归档：`C:\PKU\Term2\实验室安全作品大赛\versions\v0.8\gemini_image_prompt_pack.md`
- A4 打样规范归档：`C:\PKU\Term2\实验室安全作品大赛\versions\v0.8\a4_print_prototype_spec.md`
- 事件牌图文交接归档：`C:\PKU\Term2\实验室安全作品大赛\versions\v0.8\event_card_visual_handoff.md`
- 卡通事件牌生成脚本归档：`C:\PKU\Term2\实验室安全作品大赛\versions\v0.8\scripts\generate_event_card_svgs.py`
- 卡通事件牌正面归档：`C:\PKU\Term2\实验室安全作品大赛\versions\v0.8\assets\events\fronts\`
- 卡通事件牌清单归档：`C:\PKU\Term2\实验室安全作品大赛\versions\v0.8\assets\previews\event_batch1_manifest.md`
- 卡通事件牌预览页归档：`C:\PKU\Term2\实验室安全作品大赛\versions\v0.8\assets\previews\event_batch1_preview.html`
- 全卡视觉圣经归档：`C:\PKU\Term2\实验室安全作品大赛\versions\v0.8\full_card_visual_bible.md`
- 全卡文案底稿归档：`C:\PKU\Term2\实验室安全作品大赛\versions\v0.8\all_cards_copy_spec.md`

## 源文件

- 当前规则：`C:\PKU\Term2\实验室安全作品大赛\boardgame_v0.8.md`
- 当前模拟器：`C:\PKU\Term2\实验室安全作品大赛\simulation\run_v0_8_balance.py`

## 数据备份

- 烟测数据：`C:\PKU\Term2\实验室安全作品大赛\data\v0.8\smoke_test_v0_8_teaching_target3`
- 当前有效正式数据：`C:\PKU\Term2\实验室安全作品大赛\data\v0.8\run_002_v0_8_refinement_teaching3`
- 早期正式数据：`C:\PKU\Term2\实验室安全作品大赛\data\v0.8\run_001_v0_8_refinement`

## 关联文档

- 版本日志：`C:\PKU\Term2\实验室安全作品大赛\CHANGELOG.md`
- 版本速记：`C:\PKU\Term2\实验室安全作品大赛\docs\version_memory.md`
- 测试规程：`C:\PKU\Term2\实验室安全作品大赛\docs\ai_balance_test_protocol_v0.8.md`
- 评估结论：`C:\PKU\Term2\实验室安全作品大赛\docs\v0.8_refinement_assessment.md`
- 卡牌模板：`C:\PKU\Term2\实验室安全作品大赛\docs\card_information_template_v0.8.md`
- 事件牌文本库：`C:\PKU\Term2\实验室安全作品大赛\content\event_cards_v0.8.md`
- 事件牌图文交接稿：`C:\PKU\Term2\实验室安全作品大赛\content\event_card_visual_handoff_v0.8.md`
- Gemini 提示词包：`C:\PKU\Term2\实验室安全作品大赛\docs\gemini_image_prompt_pack_v0.8.md`
- A4 打样规范：`C:\PKU\Term2\实验室安全作品大赛\docs\a4_print_prototype_spec_v0.8.md`
- 卡通事件牌生成脚本：`C:\PKU\Term2\实验室安全作品大赛\scripts\generate_event_card_svgs_v0_8.py`
- 卡通事件牌正面：`C:\PKU\Term2\实验室安全作品大赛\assets\events\fronts\`
- 卡通事件牌清单：`C:\PKU\Term2\实验室安全作品大赛\assets\previews\event_batch1_manifest.md`
- 卡通事件牌预览页：`C:\PKU\Term2\实验室安全作品大赛\assets\previews\event_batch1_preview.html`
- 全卡视觉圣经：`C:\PKU\Term2\实验室安全作品大赛\docs\full_card_visual_bible_v0.8.md`
- 全卡文案底稿：`C:\PKU\Term2\实验室安全作品大赛\content\all_cards_copy_spec_v0.8.md`

## 补充说明

- 上述内容资产属于 `v0.8` 的成品化支持文件
- 本轮未新增规则版本号，也未生成新的模拟数据目录
- 当前有效玩法数据仍以 `run_002_v0_8_refinement_teaching3` 为准

## 本轮结论

- `balanced+balanced` 无策略标准模式胜率 `53.10%`
- 教学模式胜率 `81.10%`
- `T07` 完成率回升到 `58.80%`
- 行动结构保持稳定，没有回退到旧的保守解
- `v0.8` 可以作为后续成品化准备的新稳定基线
- `v0.8` 已有首批可编辑卡通事件牌正面，可直接用于原型展示
- `v0.8` 已补齐正式成品所需的视觉标准和全卡文案底稿
