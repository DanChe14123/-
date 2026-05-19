# v2 评审材料阅读入口

## 1. 推荐阅读顺序

### Writing Guidance

如果评委或老师只有 10 分钟，建议按以下顺序阅读：

1. `manual/quick_reference_v2.md`
2. `docs/v2_sample_playthrough_standard.md`
3. `card/final/v2/preview/index.html`
4. `manual/judge_brief_v2.md`
5. `docs/v2_balance_report.md`
6. `docs/v2_ai_agent_playtest_findings.md`
7. `docs/v2_full_card_layout_generation.md`
8. `docs/v2_card_art_direction.md`
9. `docs/v2_gptimage2_prompt_pack.md`

这个顺序先回答“怎么玩”，再回答“一局是什么样”，再展示“卡牌长什么样”，最后说明“为什么可信、后续怎么继续做图”。

## 2. 材料分工

| 材料 | 面向对象 | 解决的问题 |
| --- | --- | --- |
| `manual/quick_reference_v2.md` | 第一次接触的人 | 3 分钟理解流程 |
| `manual/player_rulebook_v2.md` | 玩家 | 能按规则开局和完成一局 |
| `docs/v2_sample_playthrough_standard.md` | 评委、老师、AI 工具 | 看懂一局游戏体验 |
| `card/final/v2/preview/index.html` | 评委、老师、制卡人员 | 浏览全 120 张卡正反面 |
| `card/final/v2/preview/contact_sheet.png` | 评委、老师 | 快速查看全套卡面统一性 |
| `card/final/v2/manifest.json` | 开发者、制卡工具 | 检查 120 张卡与 240 个输出面 |
| `manual/teaching_guide_v2.md` | 教师 | 如何课堂带玩和复盘 |
| `manual/judge_brief_v2.md` | 评委 | 作品定位、创新点和数据摘要 |
| `docs/v2_balance_report.md` | 评委、开发者 | 数值稳定性和平衡测试证据 |
| `content/v2_cards.json` | 开发者、制卡工具 | 全部卡牌结构化数据 |
| `docs/v2_ai_agent_playtest_protocol.md` | 后续 AI 测试 | 无真人试玩阶段的替代验证流程 |
| `data/v2/ai_agent_playtests/agent_playtest_20260428_round01.md` | 开发者、评委 | 首轮 AI 代理试玩原始记录 |
| `docs/v2_ai_agent_playtest_findings.md` | 评委、老师 | AI 代理试玩汇总结论 |
| `docs/v2_full_card_layout_generation.md` | 开发者、制卡人员 | 全卡版面生成流程和验证结果 |
| `docs/v2_card_art_direction.md` | 美术制作 | 卡面风格和版式原则 |
| `docs/v2_gptimage2_prompt_pack.md` | 图像生成 | 8 张首批样板图提示词 |

## 3. 当前证据边界

### Model Inference

当前已经完成：

- v2 规则重构
- 120 张结构化卡牌
- v2 独立模拟器
- 270000 局长跑平衡数据
- 标准模式示例战报
- 教师、玩家、评委三类说明文档
- AI 代理试玩测试 round01
- 全 120 张卡牌版面预览生成

### Experiment Hypothesis

AI 代理测试已经完成一轮，但当前尚未完成真人试玩。因此以下内容不能写成事实：

- 真实玩家觉得游戏好玩
- 新手一定能在 10 分钟内独立开局
- 教师实际课堂使用成本已经被验证
- 岗位轮值一定能提升真实参与感

## 4. 下一步建议

优先级从高到低：

1. 让另一个低成本 AI 工具复核 `data/v2/ai_agent_playtests/agent_playtest_20260428_round01.md`。
2. 打开 `card/final/v2/preview/index.html`，检查全卡版式是否存在明显拥挤或缺字段。
3. 根据 `docs/v2_full_card_layout_generation.md` 替换个别被裁切的样板图并重新生成。
4. 条件允许后，做一次 2-4 人真人试玩并补充真实记录。

## 5. 对外说明建议

### Writing Guidance

对评委或老师建议这样表述：

> v2 版本已经完成规则、牌池、模拟器、长跑平衡测试、一轮 AI 代理试玩测试，以及全 120 张卡牌的程序化版面预览。由于当前暂时没有真人试玩条件，我们没有把玩家体验写成既成事实，而是用 AI 代理测试、标准模式示例战报和全卡版面预览提前发现理解障碍，并为后续真人试玩保留记录入口。
