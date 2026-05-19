# 桌游版本与测试日志

## v0.1 基线版

- 规则归档：`versions/v0.1/boardgame_rules.md`
- 模拟器归档：`versions/v0.1/run_v0_1_balance_baseline.py`
- 版本特征：
  - 公共手牌 5 张
  - 标准模式通关目标为 5 点进度
  - 关键行动缺失时，事件结算偏硬
  - `E14` 曾可能直接触发重大事故
- 基线结果：
  - 数据目录：`data/v0.1/smoke_test`
  - `balanced+balanced` 标准模式胜率约 `6%`
- 结论：
  - 难度明显过高，只能作为最早期原型参考

## v0.2 可试玩 Demo 版

- 规则归档：`versions/v0.2/boardgame_rules.md`
- 模拟器归档：`versions/v0.2/run_balance_sim.py`
- 主要改动：
  - 公共手牌 `5 -> 6`
  - 各模式通关目标统一调整为 `4` 点进度
  - 辅助行动在部分场景下可提供“风险控制成功但任务未推进”的保底价值
  - 低危事件在“基本正确”下不再额外扣除安全值
  - 移除 `E14` 的直接重大事故判定
  - `balanced` 机器人在中危事件下也会主动换牌
- 正式结果：
  - 数据目录：`data/v0.2/run_002_candidate_v0_2_fullstats`
  - `balanced+balanced` 标准模式胜率 `56.27%`
  - `balanced+balanced` 教学模式胜率 `63.60%`
  - `balanced+balanced` 挑战模式胜率 `19.87%`
- 结论：
  - 标准模式进入可试玩区间
  - 高危事件和 `stop/report` 偏强的问题仍待处理

## v0.3 完整度增强版

- 规则归档：`versions/v0.3/boardgame_rules.md`
- 模拟器归档：`versions/v0.3/run_balance_sim.py`
- 主要改动：
  - 引入任务与事件绑定机制
  - 引入 `隐患值`
  - 引入任务奖励：清隐患、回血、降升级、额外换牌
  - 修正挑战模式的附加事件结算
  - 统一隐患高压阈值为 `3`
- 正式结果：
  - 数据目录：`data/v0.3/run_001_v0_3_fullstats`
  - `balanced+balanced` 标准模式胜率 `53.83%`
  - `balanced+balanced` 教学模式胜率 `57.30%`
  - `balanced+balanced` 挑战模式胜率 `25.67%`
- 结论：
  - 决策层次明显增加，已经更像桌游
  - 系统稳定，但流派差异仍主要体现在结果结构，不够体现在出牌行为

## v0.4 流派起点版

- 规则归档：`versions/v0.4/boardgame_rules.md`
- 模拟器归档：`versions/v0.4/run_balance_sim.py`
- 主要改动：
  - 在 `v0.3` 基础上加入首发 4 张实验室策略牌
  - 策略牌正式接入模拟器与统计输出
  - 保留无策略基线矩阵用于横向比较
- 正式结果：
  - 数据目录：`data/v0.4/run_001_v0_4_strategy_launch`
  - `balanced+balanced` 无策略标准模式胜率 `53.83%`
  - `风险隔离` 胜率 `54.97%`
  - `稳健管理` 胜率 `53.50%`
  - `规范先行` 胜率 `52.17%`
  - `效率优先` 胜率 `49.20%`
- 结论：
  - 已形成明确的赛前流派起点
  - 不同策略会改变胜负结构与失败原因
  - 但对行动牌选取行为的影响仍不够大

## v0.5 任务扩容版

- 规则归档：`versions/v0.5/boardgame_rules.md`
- 模拟器归档：`versions/v0.5/run_balance_sim.py`
- 主要改动：
  - 任务牌 `8 -> 12`
  - 新增 `T09` 到 `T12`
  - 模拟器新增 `task_stats.csv`
  - 保持 `v0.4` 的隐患、奖励、策略牌框架不变，只验证内容扩容本身
- 新增任务：
  - `T09` 危险化学品领用与登记
  - `T10` 低温/高温设备使用
  - `T11` 旋蒸或离心设备操作
  - `T12` 实验结束后的交接检查
- 测试结果：
  - 烟测目录：`data/v0.5/smoke_test_v0_5_tasks`
  - 正式目录：`data/v0.5/run_001_v0_5_task_expansion`
  - `balanced+balanced` 无策略标准模式胜率 `51.33%`
  - `balanced+balanced` 教学模式胜率 `55.87%`
  - `balanced+balanced` 挑战模式胜率 `26.13%`
  - `balanced+balanced` 标准模式下 12 张任务全部稳定出现，出现次数约 `1436` 到 `1485`
  - 12 张任务完成率分布约 `50.34%` 到 `70.82%`
- 结论：
  - 任务扩容显著提升了内容体量与任务覆盖面
  - 基线强度仅小幅回落，说明扩容健康
  - 当前仍需继续压低 `stop/report` 的泛用性，并通过行动牌细分进一步做实流派差异

## v0.6 行动层扩容版

- 规则归档：`versions/v0.6/boardgame_rules.md`
- 模拟器归档：`versions/v0.6/run_balance_sim.py`
- 主要改动：
  - 行动牌 `8 -> 12`
  - 新增 `shutdown / inspect / secure / evacuate`
  - 公共手牌 `6 -> 8`
  - 修正换牌逻辑，要求机器人更看重“事件专属关键解”
  - 保持 `v0.5` 的 12 任务框架不变，专门验证行动层扩容
- 测试结果：
  - 烟测目录：`data/v0.6/smoke_test_v0_6_actions_hand8_redrawfix`
  - 正式目录：`data/v0.6/run_001_v0_6_action_expansion`
  - `balanced+balanced` 无策略标准模式胜率 `52.07%`
  - `balanced+balanced` 教学模式胜率 `54.40%`
  - `balanced+balanced` 挑战模式胜率 `31.63%`
  - 新增 4 类行动合计选取率 `34.10%`
  - `stop + report` 合计选取率从 `v0.5` 的 `39.82%` 降到 `26.12%`
  - 行动集中度明显下降，前 4 大行动合计从 `67.63%` 降到 `51.12%`
- 结论：
  - 行动层扩容成功，新增行动已经真正进入局内决策
  - `v0.6` 在不牺牲平衡的前提下，把行动选择结构明显做开了
  - 下一步应优先扩充事件池，让 `secure` 等窄用途行动获得更多存在感

## v0.7 事件池扩容版

- 规则归档：`versions/v0.7/boardgame_rules.md`
- 模拟器归档：`versions/v0.7/run_balance_sim.py`
- 主要改动：
  - 事件牌 `16 -> 24`
  - 新增 `E17` 到 `E24`
  - 优先补 `secure / inspect / evacuate` 相关场景
  - 任务与事件映射同步扩容
  - 对 `E17 / E18 / E20 / E21` 做了轻度对齐，避免拖垮任务推进
- 测试结果：
  - 烟测目录：`data/v0.7/smoke_test_v0_7_events_tuned`
  - 正式目录：`data/v0.7/run_001_v0_7_event_expansion`
  - `balanced+balanced` 无策略标准模式胜率 `50.53%`
  - `balanced+balanced` 教学模式胜率 `50.43%`
  - `balanced+balanced` 挑战模式胜率 `33.20%`
  - 24 张事件全部稳定进入牌池，出现次数约 `320` 到 `1326`
  - `stop + report` 合计选取率进一步降到 `25.49%`
  - 新增 4 类行动合计选取率提升到 `36.57%`
  - `secure` 选取率从 `2.18%` 提升到 `4.61%`
- 结论：
  - 事件池扩容成功，没有破坏标准模式基线
  - 新行动在更丰富的事件环境下进一步站稳
  - 当前主要残留问题是教学模式相对标准模式的优势变窄，下一步应做单卡精修与模式回调

## v0.8 精修版

- 规则归档：`versions/v0.8/boardgame_rules.md`
- 模拟器归档：`versions/v0.8/run_balance_sim.py`
- 主要改动：
  - `T07` 新增 `撤离与警戒` 偏好，修正与 `E23` 的错位
  - 调整低危 `shutdown / secure` 事件的换牌判断
  - 教学模式新增“低危 contained 不加隐患”的保护
  - 教学模式参数回调：
    - 初始安全值 `10`
    - 换牌次数 `4`
    - 通关目标 `3` 点进度
- 测试结果：
  - 早期正式跑数：`data/v0.8/run_001_v0_8_refinement`
  - 当前有效正式跑数：`data/v0.8/run_002_v0_8_refinement_teaching3`
  - `balanced+balanced` 无策略标准模式胜率 `53.10%`
  - `balanced+balanced` 教学模式胜率 `81.10%`
  - `balanced+balanced` 挑战模式胜率 `33.80%`
  - `T07` 完成率提升到 `58.80%`
  - `stop + report` 合计选取率维持在 `25.56%`
  - 新增 4 类行动合计选取率 `36.33%`
- 结论：
  - 精修成功，标准模式重新回到更舒适区间
  - 教学模式已被明确拉开，成为真正的入门训练模式
  - `v0.8` 可以作为下一阶段成品化准备的稳定基线

## v0.8 内容资产补完

- 本轮不新增规则系统，不改模拟器，不生成新的平衡数据目录
- 当前有效玩法基线仍以：`data/v0.8/run_002_v0_8_refinement_teaching3`
- 新增内容资产：
  - 卡牌模板：`docs/card_information_template_v0.8.md`
  - 事件牌文本库：`content/event_cards_v0.8.md`
  - Gemini 提示词包：`docs/gemini_image_prompt_pack_v0.8.md`
  - A4 打样规范：`docs/a4_print_prototype_spec_v0.8.md`
- 本轮结论：
  - `v0.8` 已从“稳定玩法基线”进入“可开始卡面化”的阶段
  - 事件牌背面教学文本已具备落版条件
  - 后续应优先补 `12` 张任务牌和 `12` 类行动牌的正式卡面文案

## v0.8 事件牌图文合并交接

- 本轮仍不改规则与数值
- 新增图文合并交接稿：`content/event_card_visual_handoff_v0.8.md`
- 处理方式：
  - 每张事件牌提供一份可直接复制的 Gemini 单图 prompt
  - 同页保留该牌正反面核心文案
  - 明确建议文件命名，方便后续排版
- 本轮结论：
  - 事件牌已经具备“逐张出图 -> 回填卡面”的执行条件
  - 下一步应转向任务牌与行动牌的同类交接稿

## v0.8 首批卡通事件牌正面

- 本轮不改玩法规则和模拟器
- 新增生成脚本：`scripts/generate_event_card_svgs_v0_8.py`
- 新增风格说明：`docs/cartoon_event_card_pipeline_v0.8.md`
- 生成输出目录：`assets/events/fronts/`
- 浏览器预览页：`assets/previews/event_batch1_preview.html`
- 首批完成 `8` 张 SVG 正面卡：
  - `E02`
  - `E05`
  - `E08`
  - `E09`
  - `E13`
  - `E15`
  - `E21`
  - `E23`
- 清单文件：`assets/previews/event_batch1_manifest.md`
- 本轮结论：
  - 已建立统一卡通风格的可编辑矢量卡面基线
  - 后续可以在同一生成器上继续扩到全部 `24` 张事件牌
  - 下一步应补任务牌与行动牌，或继续扩剩余 `16` 张事件牌

## v0.8 全卡视觉与文案定稿底稿

- 本轮不改规则和数值
- 新增视觉圣经：`docs/full_card_visual_bible_v0.8.md`
- 新增全卡文案底稿：`content/all_cards_copy_spec_v0.8.md`
- 关键新增：
  - 四名可选角色的固定视觉设定
  - `56` 张牌的主角平均分配方案
  - 五类卡牌的正式卡面标准
  - 全部事件、任务、行动、角色、策略卡的正反面文案底稿
- 本轮结论：
  - 视觉方向已从“原型试做”切换为“正式成品规范”
  - 后续所有插画和排版应以上述两份文件为主标准
  - 现有简化 SVG 只能继续作为结构原型，不能代表最终质感
# 2026-04-14 初赛前封版补充

- 玩法结论：冻结 `v0.8`，初赛前不再做结构性规则修改
- 新增长跑数据：`data/v0.8/run_003_v0_8_prefinal_longrun`
- 补跑 `v0.1` 正式基线：`data/v0.1/run_003_v0_1_prefinal_baseline`
- 新增提交构建脚本：`scripts/build_prefinal_submission.py`
- 新增玩法冻结评估：`docs/prefinal_freeze_review.md`
- 新增 Sora 宣传片提示词：`docs/sora_prefinal_video_prompt.md`
- 生成初赛文档：
  - `output/pdf/prefinal_20260414/00_请先看这里_作品总览.pdf`
  - `output/pdf/prefinal_20260414/01_一页玩法速览.pdf`
  - `output/pdf/prefinal_20260414/03_版本迭代与关键数据.pdf`
  - `output/pdf/prefinal_20260414/04_使用手册.pdf`
- 生成本地宣传视频备选：`output/video/prefinal_20260414/02_宣传视频.mp4`
- 生成初赛压缩包：
  - `submission/初赛参赛作品_v0.8_prefinal_20260414`
  - `submission/初赛参赛作品_v0.8_prefinal_20260414.zip`
- 长跑结果摘要：
  - `balanced+balanced` 标准模式胜率 `52.44%`
  - 封版阈值全部通过，初赛前不再修改核心玩法
