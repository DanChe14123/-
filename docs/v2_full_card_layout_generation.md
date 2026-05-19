# v2 全 120 张卡牌版面生成说明

## 1. 生成范围

本轮生成的是《实验室安全值班》v2 的完整卡牌版面预览集，范围来自 `content/v2_cards.json`，不改规则、不改数值、不改牌池内容。

生成结果：

- 任务牌：18 张
- 事件牌：36 张
- 行动牌：24 张
- 角色牌：6 张
- 岗位牌：4 张
- 策略牌：8 张
- 复盘牌：24 张
- 合计：120 张卡，正反面共 240 张 PNG

## 2. 生成命令

默认命令：

```powershell
python scripts\generate_full_card_set_v2.py
```

如果以后要换一组样板插图，可以指定新的图片目录：

```powershell
python scripts\generate_full_card_set_v2.py --generated-image-dir "C:\path\to\generated_images"
```

脚本入口：

- `scripts/generate_full_card_set_v2.py`

数据来源：

- `content/v2_cards.json`

输出目录：

- `card/final/v2/`

## 3. 样板插图映射

本轮只使用 8 张已认可样板图作为正式风格样板，其余卡牌使用统一抽象实验室占位插图，避免在规则和版式仍可能调整时为 120 张卡逐张生成高成本插画。

样板图映射：

| 卡牌 | 用途 |
| --- | --- |
| `E02` | 低危事件样板 |
| `E05` | 中危事件样板 |
| `E15` | 高危事件样板 |
| `T03` | 任务牌样板 |
| `A01` | 行动牌样板 |
| `A08` | 行动牌样板 |
| `P01` | 岗位牌样板 |
| `R02` | 角色牌样板 |

样板插图会被复制到：

- `card/final/v2/illustrations/samples/`

## 4. 版式系统

所有卡牌共享同一套基础组件：

- 顶部色带：左侧编号，右侧风险等级或类别标签
- 白底标题区：大标题，黑色高字重
- 插图区：只放无中文插图或抽象图形
- 信息模块区：浅色信息块，承载所有中文正文
- 外轮廓：圆角、浅投影、细边框
- 安全区：文字远离边缘，避免裁切压字

卡牌类型规则：

- 事件牌正面：编号、风险等级、标题、插图、风险摘要、关键行动
- 事件牌背面：知识点、正确处置、错误倾向、复盘问题
- 任务牌正面：编号、阶段、标题、插图、任务目标、推荐行动
- 任务牌背面：完成奖励、风险标签、教学知识点
- 行动牌正面：编号、行动名、插图、用途、行动强度
- 行动牌背面：行动标签、适用岗位、限制边界、协同建议
- 角色牌/岗位牌正面：名称、身份或职责、插图、能力摘要
- 角色牌/岗位牌背面：能力、节奏、风险或贡献规则
- 策略牌/复盘牌正面：名称、路线或知识主题
- 策略牌/复盘牌背面：效果、代价、适合打法，或正确行动、原因、复盘问题

## 5. 输出文件

核心索引：

- `card/final/v2/manifest.json`
- `card/final/v2/validation_report.json`

浏览预览：

- `card/final/v2/preview/index.html`
- `card/final/v2/preview/contact_sheet.png`

印刷拼版预览：

- `card/final/v2/print/front_sheets.png`
- `card/final/v2/print/back_sheets.png`

各类型卡牌：

- `card/final/v2/events/`
- `card/final/v2/tasks/`
- `card/final/v2/actions/`
- `card/final/v2/roles/`
- `card/final/v2/posts/`
- `card/final/v2/strategies/`
- `card/final/v2/debriefs/`

## 6. 当前验证结果

本轮生成后已完成以下验证：

- `content/v2_cards.json` 可解析
- 卡牌总数为 120
- 正反面输出总数为 240
- `manifest.json` 中所有正反面路径均存在
- 8 张样板图已映射到指定卡牌
- `validation_report.json` 中 `issues` 数量为 0
- 已抽查 `E02`、`E05`、`A01`、`P01`、`D02`、`S02` 原尺寸 PNG，标题和正文清晰，文字未压在插图上

## 7. 已知边界

当前版本是全卡版式系统，不是全卡最终美术成品。

- 只有 8 张卡使用正式样板插图，其余卡使用统一占位插图
- 个别样板图可能存在构图裁切问题，后续可替换同名插图后重新运行脚本
- 中文全部由 Pillow 后期排版，未让图像生成模型直接生成中文
- HTML 预览用于审阅，不作为正式源文件
- 拼版图用于快速检查统一性，正式印刷前仍建议单独做出血、裁切线和纸张尺寸确认
