# v2 full 120-card no-text illustration prompt guide

This file is for generating the illustration layer of all 120 cards in the v2 laboratory safety board game. It does not ask the image model to generate card titles, rules text, card IDs, or readable labels. All Chinese card text should be added later in the layout stage.

## How to use

- Use the sample images provided by the user as style reference images.
- Copy only one card prompt at a time into the image generator.
- Recommended aspect ratio: vertical 2:3, such as 1024x1536 or 1536x2304.
- If the image generator has a negative prompt field, move the final Strict negative prompt paragraph into that field.
- Do not ask the image model to generate Chinese text. Text will be added later by the card layout template.
- The goal is one high-quality no-text illustration per card. If a front/back pair is needed later, reuse the same illustration or generate a back-side detail crop from the same scene.

## Unified visual style

Clean academic watercolor card art; modern chemistry laboratory; blue-white palette; soft daylight; transparent glassware; white lab coats; blue goggles or blue nitrile gloves; delicate anime-inspired but natural human proportions; credible lab equipment; rounded card-frame feeling; calm safety education tone.

## Card counts

- Task card: 18
- Event card: 36
- Action card: 24
- Role card: 6
- Post card: 4
- Strategy card: 8
- Debrief card: 24
- Total: 120

## Prompts

### E01 Event card | 未佩戴护目镜开始操作

```text
Create ONE vertical no-text illustration for a laboratory safety board-game card.

Reference style: use the uploaded sample images as the main style reference. Match their clean academic watercolor look, blue-white palette, soft natural window light, transparent glassware, delicate anime-inspired characters, realistic chemistry lab equipment, rounded card-frame feeling, and calm educational tone.

Card ID: E01
Card type: Event card
Chinese card name: 未佩戴护目镜开始操作
Visual goal: Show the safety event "未佩戴护目镜开始操作" being noticed or about to be handled. low-risk mood: calm, clear risk source, no accident consequence. The visual risk should match this Chinese description: 防护不到位导致暴露风险。
Main character: Lin Cheng; young Chinese female graduate student, short black bob hair, clear goggles, white lab coat, blue inner shirt, often holding a notebook, careful and detail-oriented.
Scene environment: preparation area of a modern chemistry lab, clean bench, reagent shelves, inventory notebook, PPE on the table.
Required visual elements: safety goggles, blue nitrile gloves, white lab coat, visible PPE checking or wearing action; potential exposure risk shown by distance, vapor, or an uncapped container, without injury; checking clamps, valves, labels, airflow, or equipment connections; two lab members confirming a risk with calm gestures.
Additional card context from the rules: knowledge: 进入实验操作前应确认基础防护。.
Composition: vertical 2:3 card illustration; risk source in foreground or lower-left third; character in mid-ground observing or responding; rounded-card safe margins.
Extra production rule: The risk must be visually obvious, but the image must not show injury, disaster aftermath, or panic. Leave visual space for later card text layout.
Color and material: pale blue, white, gray-blue, transparent glass, soft reflections on the lab bench, small amount of orange/yellow only for safety warning symbols or flame.
Border and crop: the image may include a thin rounded rectangle card border and warm off-white paper margin; keep all important subjects away from the edge.

Strict negative prompt: no readable Chinese text, no readable English text, no readable numbers, no logo, no watermark, no brand name, no school emblem, no UI text, no readable bottle labels, no readable notebook content, no readable clipboard content, no title, no card frame text. Labels, forms, badges and screens must be blank, blurred, or meaningless lines only. No photorealistic style, no 3D render, no chibi style, no horror style, no gore, no injured people, no large explosion, no chaotic disaster, no distorted face, no extra fingers, no missing hands, no duplicated faces, no cluttered composition.
```

### E02 Event card | 试剂瓶标签模糊

```text
Create ONE vertical no-text illustration for a laboratory safety board-game card.

Reference style: use the uploaded sample images as the main style reference. Match their clean academic watercolor look, blue-white palette, soft natural window light, transparent glassware, delicate anime-inspired characters, realistic chemistry lab equipment, rounded card-frame feeling, and calm educational tone.

Card ID: E02
Card type: Event card
Chinese card name: 试剂瓶标签模糊
Visual goal: Show the safety event "试剂瓶标签模糊" being noticed or about to be handled. low-risk mood: calm, clear risk source, no accident consequence. The visual risk should match this Chinese description: 物质身份无法确认。
Main character: Zhou Heng; young Chinese male graduate student, short black hair, clear goggles, white lab coat, blue inner shirt, blue nitrile gloves, skilled at hands-on experiments.
Scene environment: preparation area of a modern chemistry lab, clean bench, reagent shelves, inventory notebook, PPE on the table.
Required visual elements: reagent bottle with blank or blurred label, absolutely no readable text; unknown transparent reagent bottle and cautious inspection gesture; open lab notebook, blank grid sheet, pen, inventory ledger with no readable characters; phone or radio reporting gesture, screen blank, no readable UI; comparing bottle, blank notebook, and inventory sheet.
Additional card context from the rules: knowledge: 不能凭记忆或瓶身颜色判断试剂。.
Composition: vertical 2:3 card illustration; risk source in foreground or lower-left third; character in mid-ground observing or responding; rounded-card safe margins.
Extra production rule: The risk must be visually obvious, but the image must not show injury, disaster aftermath, or panic. Leave visual space for later card text layout.
Color and material: pale blue, white, gray-blue, transparent glass, soft reflections on the lab bench, small amount of orange/yellow only for safety warning symbols or flame.
Border and crop: the image may include a thin rounded rectangle card border and warm off-white paper margin; keep all important subjects away from the edge.

Strict negative prompt: no readable Chinese text, no readable English text, no readable numbers, no logo, no watermark, no brand name, no school emblem, no UI text, no readable bottle labels, no readable notebook content, no readable clipboard content, no title, no card frame text. Labels, forms, badges and screens must be blank, blurred, or meaningless lines only. No photorealistic style, no 3D render, no chibi style, no horror style, no gore, no injured people, no large explosion, no chaotic disaster, no distorted face, no extra fingers, no missing hands, no duplicated faces, no cluttered composition.
```

### E03 Event card | 废液桶标签缺失

```text
Create ONE vertical no-text illustration for a laboratory safety board-game card.

Reference style: use the uploaded sample images as the main style reference. Match their clean academic watercolor look, blue-white palette, soft natural window light, transparent glassware, delicate anime-inspired characters, realistic chemistry lab equipment, rounded card-frame feeling, and calm educational tone.

Card ID: E03
Card type: Event card
Chinese card name: 废液桶标签缺失
Visual goal: Show the safety event "废液桶标签缺失" being noticed or about to be handled. low-risk mood: calm, clear risk source, no accident consequence. The visual risk should match this Chinese description: 废液去向无法追溯。
Main character: Gu Ning; young Chinese female doctoral student, low ponytail or short hair, goggles, lab coat, calm posture, good at recording and verification.
Scene environment: general modern chemistry lab operation scene, clean bench, glassware, safety equipment, bright window light.
Required visual elements: waste bottle, sorted waste container, cleanup action, blank label only; reagent bottle with blank or blurred label, absolutely no readable text; open lab notebook, blank grid sheet, pen, inventory ledger with no readable characters; phone or radio reporting gesture, screen blank, no readable UI.
Additional card context from the rules: knowledge: 废液容器必须标明类别和日期。.
Composition: vertical 2:3 card illustration; risk source in foreground or lower-left third; character in mid-ground observing or responding; rounded-card safe margins.
Extra production rule: The risk must be visually obvious, but the image must not show injury, disaster aftermath, or panic. Leave visual space for later card text layout.
Color and material: pale blue, white, gray-blue, transparent glass, soft reflections on the lab bench, small amount of orange/yellow only for safety warning symbols or flame.
Border and crop: the image may include a thin rounded rectangle card border and warm off-white paper margin; keep all important subjects away from the edge.

Strict negative prompt: no readable Chinese text, no readable English text, no readable numbers, no logo, no watermark, no brand name, no school emblem, no UI text, no readable bottle labels, no readable notebook content, no readable clipboard content, no title, no card frame text. Labels, forms, badges and screens must be blank, blurred, or meaningless lines only. No photorealistic style, no 3D render, no chibi style, no horror style, no gore, no injured people, no large explosion, no chaotic disaster, no distorted face, no extra fingers, no missing hands, no duplicated faces, no cluttered composition.
```

### E04 Event card | 手套污染后继续接触门把手

```text
Create ONE vertical no-text illustration for a laboratory safety board-game card.

Reference style: use the uploaded sample images as the main style reference. Match their clean academic watercolor look, blue-white palette, soft natural window light, transparent glassware, delicate anime-inspired characters, realistic chemistry lab equipment, rounded card-frame feeling, and calm educational tone.

Card ID: E04
Card type: Event card
Chinese card name: 手套污染后继续接触门把手
Visual goal: Show the safety event "手套污染后继续接触门把手" being noticed or about to be handled. medium-risk mood: serious expression, operation needs correction soon. The visual risk should match this Chinese description: 污染扩散到公共区域。
Main character: Cheng Yan; mature Chinese male doctoral student or teaching assistant, white lab coat, blue shirt, steady posture, coordinates laboratory safety.
Scene environment: active experiment area of a modern chemistry lab, fume hood, glassware, clamps, heating or transfer setup.
Required visual elements: safety goggles, blue nitrile gloves, white lab coat, visible PPE checking or wearing action; two containers or pipettes too close, cross-contamination risk; tidy bench, wiping action, cleaning tools, organized glassware; barrier tape, safe perimeter, clear risk boundary; two lab members confirming a risk with calm gestures.
Additional card context from the rules: knowledge: 污染手套不得接触公共设施。.
Composition: vertical 2:3 card illustration; risk source in foreground or lower-left third; character in mid-ground observing or responding; rounded-card safe margins.
Extra production rule: The risk must be visually obvious, but the image must not show injury, disaster aftermath, or panic. Leave visual space for later card text layout.
Color and material: pale blue, white, gray-blue, transparent glass, soft reflections on the lab bench, small amount of orange/yellow only for safety warning symbols or flame.
Border and crop: the image may include a thin rounded rectangle card border and warm off-white paper margin; keep all important subjects away from the edge.

Strict negative prompt: no readable Chinese text, no readable English text, no readable numbers, no logo, no watermark, no brand name, no school emblem, no UI text, no readable bottle labels, no readable notebook content, no readable clipboard content, no title, no card frame text. Labels, forms, badges and screens must be blank, blurred, or meaningless lines only. No photorealistic style, no 3D render, no chibi style, no horror style, no gore, no injured people, no large explosion, no chaotic disaster, no distorted face, no extra fingers, no missing hands, no duplicated faces, no cluttered composition.
```

### E05 Event card | 开放环境转移挥发性溶剂

```text
Create ONE vertical no-text illustration for a laboratory safety board-game card.

Reference style: use the uploaded sample images as the main style reference. Match their clean academic watercolor look, blue-white palette, soft natural window light, transparent glassware, delicate anime-inspired characters, realistic chemistry lab equipment, rounded card-frame feeling, and calm educational tone.

Card ID: E05
Card type: Event card
Chinese card name: 开放环境转移挥发性溶剂
Visual goal: Show the safety event "开放环境转移挥发性溶剂" being noticed or about to be handled. medium-risk mood: serious expression, operation needs correction soon. The visual risk should match this Chinese description: 挥发暴露和火灾风险上升。
Main character: Lin Cheng; young Chinese female graduate student, short black bob hair, clear goggles, white lab coat, blue inner shirt, often holding a notebook, careful and detail-oriented.
Scene environment: active experiment area of a modern chemistry lab, fume hood, glassware, clamps, heating or transfer setup.
Required visual elements: clear solvent bottle, beaker, volatile liquid transfer setup; fume hood, airflow arrows as simple graphic marks, operation moved toward the hood; potential exposure risk shown by distance, vapor, or an uncapped container, without injury; reagent bottle with blank or blurred label, absolutely no readable text; secondary tray, absorbent pad, container boundary preventing spread.
Additional card context from the rules: knowledge: 挥发性溶剂应优先在通风橱中操作。.
Composition: vertical 2:3 card illustration; risk source in foreground or lower-left third; character in mid-ground observing or responding; rounded-card safe margins.
Extra production rule: The risk must be visually obvious, but the image must not show injury, disaster aftermath, or panic. Leave visual space for later card text layout.
Color and material: pale blue, white, gray-blue, transparent glass, soft reflections on the lab bench, small amount of orange/yellow only for safety warning symbols or flame.
Border and crop: the image may include a thin rounded rectangle card border and warm off-white paper margin; keep all important subjects away from the edge.

Strict negative prompt: no readable Chinese text, no readable English text, no readable numbers, no logo, no watermark, no brand name, no school emblem, no UI text, no readable bottle labels, no readable notebook content, no readable clipboard content, no title, no card frame text. Labels, forms, badges and screens must be blank, blurred, or meaningless lines only. No photorealistic style, no 3D render, no chibi style, no horror style, no gore, no injured people, no large explosion, no chaotic disaster, no distorted face, no extra fingers, no missing hands, no duplicated faces, no cluttered composition.
```

### E06 Event card | 易燃溶剂靠近热源

```text
Create ONE vertical no-text illustration for a laboratory safety board-game card.

Reference style: use the uploaded sample images as the main style reference. Match their clean academic watercolor look, blue-white palette, soft natural window light, transparent glassware, delicate anime-inspired characters, realistic chemistry lab equipment, rounded card-frame feeling, and calm educational tone.

Card ID: E06
Card type: Event card
Chinese card name: 易燃溶剂靠近热源
Visual goal: Show the safety event "易燃溶剂靠近热源" being noticed or about to be handled. high-risk mood: urgent but educational, no injury, no explosion, no horror. The visual risk should match this Chinese description: 火源和可燃物距离过近。
Main character: Zhou Heng; young Chinese male graduate student, short black hair, clear goggles, white lab coat, blue inner shirt, blue nitrile gloves, skilled at hands-on experiments.
Scene environment: active experiment area of a modern chemistry lab, fume hood, glassware, clamps, heating or transfer setup.
Required visual elements: small controlled flame, heat source, flammable pictogram only, no explosion; clear solvent bottle, beaker, volatile liquid transfer setup; turning off heat, power, or valve, clear switch action; barrier tape, safe perimeter, clear risk boundary; fume hood, airflow arrows as simple graphic marks, operation moved toward the hood; phone or radio reporting gesture, screen blank, no readable UI.
Additional card context from the rules: knowledge: 易燃物应远离热源并控制蒸气积聚。.
Composition: vertical 2:3 card illustration; risk source in foreground or lower-left third; character in mid-ground observing or responding; rounded-card safe margins.
Extra production rule: The risk must be visually obvious, but the image must not show injury, disaster aftermath, or panic. Leave visual space for later card text layout.
Color and material: pale blue, white, gray-blue, transparent glass, soft reflections on the lab bench, small amount of orange/yellow only for safety warning symbols or flame.
Border and crop: the image may include a thin rounded rectangle card border and warm off-white paper margin; keep all important subjects away from the edge.

Strict negative prompt: no readable Chinese text, no readable English text, no readable numbers, no logo, no watermark, no brand name, no school emblem, no UI text, no readable bottle labels, no readable notebook content, no readable clipboard content, no title, no card frame text. Labels, forms, badges and screens must be blank, blurred, or meaningless lines only. No photorealistic style, no 3D render, no chibi style, no horror style, no gore, no injured people, no large explosion, no chaotic disaster, no distorted face, no extra fingers, no missing hands, no duplicated faces, no cluttered composition.
```

### E07 Event card | 酸液转移出现飞溅

```text
Create ONE vertical no-text illustration for a laboratory safety board-game card.

Reference style: use the uploaded sample images as the main style reference. Match their clean academic watercolor look, blue-white palette, soft natural window light, transparent glassware, delicate anime-inspired characters, realistic chemistry lab equipment, rounded card-frame feeling, and calm educational tone.

Card ID: E07
Card type: Event card
Chinese card name: 酸液转移出现飞溅
Visual goal: Show the safety event "酸液转移出现飞溅" being noticed or about to be handled. medium-risk mood: serious expression, operation needs correction soon. The visual risk should match this Chinese description: 腐蚀性液体飞溅风险。
Main character: Gu Ning; young Chinese female doctoral student, low ponytail or short hair, goggles, lab coat, calm posture, good at recording and verification.
Scene environment: active experiment area of a modern chemistry lab, fume hood, glassware, clamps, heating or transfer setup.
Required visual elements: acid/base bottle, splash control, secondary tray, simple hazard pictogram with no text; minor splash risk shown with shield, distance, or careful pouring, no injury; safety goggles, blue nitrile gloves, white lab coat, visible PPE checking or wearing action; secondary tray, absorbent pad, container boundary preventing spread; eyewash, safety shower, first aid box, emergency button as background shapes; phone or radio reporting gesture, screen blank, no readable UI.
Additional card context from the rules: knowledge: 腐蚀性液体应缓慢转移并做好防护。.
Composition: vertical 2:3 card illustration; risk source in foreground or lower-left third; character in mid-ground observing or responding; rounded-card safe margins.
Extra production rule: The risk must be visually obvious, but the image must not show injury, disaster aftermath, or panic. Leave visual space for later card text layout.
Color and material: pale blue, white, gray-blue, transparent glass, soft reflections on the lab bench, small amount of orange/yellow only for safety warning symbols or flame.
Border and crop: the image may include a thin rounded rectangle card border and warm off-white paper margin; keep all important subjects away from the edge.

Strict negative prompt: no readable Chinese text, no readable English text, no readable numbers, no logo, no watermark, no brand name, no school emblem, no UI text, no readable bottle labels, no readable notebook content, no readable clipboard content, no title, no card frame text. Labels, forms, badges and screens must be blank, blurred, or meaningless lines only. No photorealistic style, no 3D render, no chibi style, no horror style, no gore, no injured people, no large explosion, no chaotic disaster, no distorted face, no extra fingers, no missing hands, no duplicated faces, no cluttered composition.
```

### E08 Event card | 玻璃器皿出现裂纹

```text
Create ONE vertical no-text illustration for a laboratory safety board-game card.

Reference style: use the uploaded sample images as the main style reference. Match their clean academic watercolor look, blue-white palette, soft natural window light, transparent glassware, delicate anime-inspired characters, realistic chemistry lab equipment, rounded card-frame feeling, and calm educational tone.

Card ID: E08
Card type: Event card
Chinese card name: 玻璃器皿出现裂纹
Visual goal: Show the safety event "玻璃器皿出现裂纹" being noticed or about to be handled. low-risk mood: calm, clear risk source, no accident consequence. The visual risk should match this Chinese description: 继续使用可能破裂。
Main character: Cheng Yan; mature Chinese male doctoral student or teaching assistant, white lab coat, blue shirt, steady posture, coordinates laboratory safety.
Scene environment: preparation area of a modern chemistry lab, clean bench, reagent shelves, inventory notebook, PPE on the table.
Required visual elements: cracked glassware or glass shards contained in a tray, no blood; checking clamps, valves, labels, airflow, or equipment connections; changing gloves, goggles, or protective clothing; tidy bench, wiping action, cleaning tools, organized glassware; open lab notebook, blank grid sheet, pen, inventory ledger with no readable characters.
Additional card context from the rules: knowledge: 裂纹玻璃器皿应停止使用。.
Composition: vertical 2:3 card illustration; risk source in foreground or lower-left third; character in mid-ground observing or responding; rounded-card safe margins.
Extra production rule: The risk must be visually obvious, but the image must not show injury, disaster aftermath, or panic. Leave visual space for later card text layout.
Color and material: pale blue, white, gray-blue, transparent glass, soft reflections on the lab bench, small amount of orange/yellow only for safety warning symbols or flame.
Border and crop: the image may include a thin rounded rectangle card border and warm off-white paper margin; keep all important subjects away from the edge.

Strict negative prompt: no readable Chinese text, no readable English text, no readable numbers, no logo, no watermark, no brand name, no school emblem, no UI text, no readable bottle labels, no readable notebook content, no readable clipboard content, no title, no card frame text. Labels, forms, badges and screens must be blank, blurred, or meaningless lines only. No photorealistic style, no 3D render, no chibi style, no horror style, no gore, no injured people, no large explosion, no chaotic disaster, no distorted face, no extra fingers, no missing hands, no duplicated faces, no cluttered composition.
```

### E09 Event card | 气瓶未固定

```text
Create ONE vertical no-text illustration for a laboratory safety board-game card.

Reference style: use the uploaded sample images as the main style reference. Match their clean academic watercolor look, blue-white palette, soft natural window light, transparent glassware, delicate anime-inspired characters, realistic chemistry lab equipment, rounded card-frame feeling, and calm educational tone.

Card ID: E09
Card type: Event card
Chinese card name: 气瓶未固定
Visual goal: Show the safety event "气瓶未固定" being noticed or about to be handled. high-risk mood: urgent but educational, no injury, no explosion, no horror. The visual risk should match this Chinese description: 气瓶倾倒可能造成高压风险。
Main character: Lin Cheng; young Chinese female graduate student, short black bob hair, clear goggles, white lab coat, blue inner shirt, often holding a notebook, careful and detail-oriented.
Scene environment: preparation area of a modern chemistry lab, clean bench, reagent shelves, inventory notebook, PPE on the table.
Required visual elements: gas cylinder, regulator, chain, hose connection; tightening clamp, stabilizing stand, securing tubing or vessel; sealed vessel, pressure gauge, slightly tense hose or cap, no rupture; checking clamps, valves, labels, airflow, or equipment connections; phone or radio reporting gesture, screen blank, no readable UI.
Additional card context from the rules: knowledge: 气瓶必须用链条或支架固定。.
Composition: vertical 2:3 card illustration; risk source in foreground or lower-left third; character in mid-ground observing or responding; rounded-card safe margins.
Extra production rule: The risk must be visually obvious, but the image must not show injury, disaster aftermath, or panic. Leave visual space for later card text layout.
Color and material: pale blue, white, gray-blue, transparent glass, soft reflections on the lab bench, small amount of orange/yellow only for safety warning symbols or flame.
Border and crop: the image may include a thin rounded rectangle card border and warm off-white paper margin; keep all important subjects away from the edge.

Strict negative prompt: no readable Chinese text, no readable English text, no readable numbers, no logo, no watermark, no brand name, no school emblem, no UI text, no readable bottle labels, no readable notebook content, no readable clipboard content, no title, no card frame text. Labels, forms, badges and screens must be blank, blurred, or meaningless lines only. No photorealistic style, no 3D render, no chibi style, no horror style, no gore, no injured people, no large explosion, no chaotic disaster, no distorted face, no extra fingers, no missing hands, no duplicated faces, no cluttered composition.
```

### E10 Event card | 通风橱门开度过高

```text
Create ONE vertical no-text illustration for a laboratory safety board-game card.

Reference style: use the uploaded sample images as the main style reference. Match their clean academic watercolor look, blue-white palette, soft natural window light, transparent glassware, delicate anime-inspired characters, realistic chemistry lab equipment, rounded card-frame feeling, and calm educational tone.

Card ID: E10
Card type: Event card
Chinese card name: 通风橱门开度过高
Visual goal: Show the safety event "通风橱门开度过高" being noticed or about to be handled. low-risk mood: calm, clear risk source, no accident consequence. The visual risk should match this Chinese description: 气流控制不足。
Main character: Zhou Heng; young Chinese male graduate student, short black hair, clear goggles, white lab coat, blue inner shirt, blue nitrile gloves, skilled at hands-on experiments.
Scene environment: active experiment area of a modern chemistry lab, fume hood, glassware, clamps, heating or transfer setup.
Required visual elements: fume hood, airflow arrows as simple graphic marks, operation moved toward the hood; two lab members confirming a risk with calm gestures.
Additional card context from the rules: knowledge: 通风橱门应保持合适高度。.
Composition: vertical 2:3 card illustration; risk source in foreground or lower-left third; character in mid-ground observing or responding; rounded-card safe margins.
Extra production rule: The risk must be visually obvious, but the image must not show injury, disaster aftermath, or panic. Leave visual space for later card text layout.
Color and material: pale blue, white, gray-blue, transparent glass, soft reflections on the lab bench, small amount of orange/yellow only for safety warning symbols or flame.
Border and crop: the image may include a thin rounded rectangle card border and warm off-white paper margin; keep all important subjects away from the edge.

Strict negative prompt: no readable Chinese text, no readable English text, no readable numbers, no logo, no watermark, no brand name, no school emblem, no UI text, no readable bottle labels, no readable notebook content, no readable clipboard content, no title, no card frame text. Labels, forms, badges and screens must be blank, blurred, or meaningless lines only. No photorealistic style, no 3D render, no chibi style, no horror style, no gore, no injured people, no large explosion, no chaotic disaster, no distorted face, no extra fingers, no missing hands, no duplicated faces, no cluttered composition.
```

### E11 Event card | 废液混放风险

```text
Create ONE vertical no-text illustration for a laboratory safety board-game card.

Reference style: use the uploaded sample images as the main style reference. Match their clean academic watercolor look, blue-white palette, soft natural window light, transparent glassware, delicate anime-inspired characters, realistic chemistry lab equipment, rounded card-frame feeling, and calm educational tone.

Card ID: E11
Card type: Event card
Chinese card name: 废液混放风险
Visual goal: Show the safety event "废液混放风险" being noticed or about to be handled. high-risk mood: urgent but educational, no injury, no explosion, no horror. The visual risk should match this Chinese description: 不相容废液可能反应。
Main character: Gu Ning; young Chinese female doctoral student, low ponytail or short hair, goggles, lab coat, calm posture, good at recording and verification.
Scene environment: general modern chemistry lab operation scene, clean bench, glassware, safety equipment, bright window light.
Required visual elements: waste bottle, sorted waste container, cleanup action, blank label only; reagent bottle with blank or blurred label, absolutely no readable text; barrier tape, safe perimeter, clear risk boundary; phone or radio reporting gesture, screen blank, no readable UI.
Additional card context from the rules: knowledge: 废液分类应先确认相容性。.
Composition: vertical 2:3 card illustration; risk source in foreground or lower-left third; character in mid-ground observing or responding; rounded-card safe margins.
Extra production rule: The risk must be visually obvious, but the image must not show injury, disaster aftermath, or panic. Leave visual space for later card text layout.
Color and material: pale blue, white, gray-blue, transparent glass, soft reflections on the lab bench, small amount of orange/yellow only for safety warning symbols or flame.
Border and crop: the image may include a thin rounded rectangle card border and warm off-white paper margin; keep all important subjects away from the edge.

Strict negative prompt: no readable Chinese text, no readable English text, no readable numbers, no logo, no watermark, no brand name, no school emblem, no UI text, no readable bottle labels, no readable notebook content, no readable clipboard content, no title, no card frame text. Labels, forms, badges and screens must be blank, blurred, or meaningless lines only. No photorealistic style, no 3D render, no chibi style, no horror style, no gore, no injured people, no large explosion, no chaotic disaster, no distorted face, no extra fingers, no missing hands, no duplicated faces, no cluttered composition.
```

### E12 Event card | 实验无人值守

```text
Create ONE vertical no-text illustration for a laboratory safety board-game card.

Reference style: use the uploaded sample images as the main style reference. Match their clean academic watercolor look, blue-white palette, soft natural window light, transparent glassware, delicate anime-inspired characters, realistic chemistry lab equipment, rounded card-frame feeling, and calm educational tone.

Card ID: E12
Card type: Event card
Chinese card name: 实验无人值守
Visual goal: Show the safety event "实验无人值守" being noticed or about to be handled. medium-risk mood: serious expression, operation needs correction soon. The visual risk should match this Chinese description: 反应异常无法及时发现。
Main character: Cheng Yan; mature Chinese male doctoral student or teaching assistant, white lab coat, blue shirt, steady posture, coordinates laboratory safety.
Scene environment: active experiment area of a modern chemistry lab, fume hood, glassware, clamps, heating or transfer setup.
Required visual elements: heating mantle, hot plate, warm glassware, heat source control; turning off heat, power, or valve, clear switch action; open lab notebook, blank grid sheet, pen, inventory ledger with no readable characters; phone or radio reporting gesture, screen blank, no readable UI.
Additional card context from the rules: knowledge: 持续反应应安排值守或明确监控。.
Composition: vertical 2:3 card illustration; risk source in foreground or lower-left third; character in mid-ground observing or responding; rounded-card safe margins.
Extra production rule: The risk must be visually obvious, but the image must not show injury, disaster aftermath, or panic. Leave visual space for later card text layout.
Color and material: pale blue, white, gray-blue, transparent glass, soft reflections on the lab bench, small amount of orange/yellow only for safety warning symbols or flame.
Border and crop: the image may include a thin rounded rectangle card border and warm off-white paper margin; keep all important subjects away from the edge.

Strict negative prompt: no readable Chinese text, no readable English text, no readable numbers, no logo, no watermark, no brand name, no school emblem, no UI text, no readable bottle labels, no readable notebook content, no readable clipboard content, no title, no card frame text. Labels, forms, badges and screens must be blank, blurred, or meaningless lines only. No photorealistic style, no 3D render, no chibi style, no horror style, no gore, no injured people, no large explosion, no chaotic disaster, no distorted face, no extra fingers, no missing hands, no duplicated faces, no cluttered composition.
```

### E13 Event card | 皮肤接触腐蚀性液体

```text
Create ONE vertical no-text illustration for a laboratory safety board-game card.

Reference style: use the uploaded sample images as the main style reference. Match their clean academic watercolor look, blue-white palette, soft natural window light, transparent glassware, delicate anime-inspired characters, realistic chemistry lab equipment, rounded card-frame feeling, and calm educational tone.

Card ID: E13
Card type: Event card
Chinese card name: 皮肤接触腐蚀性液体
Visual goal: Show the safety event "皮肤接触腐蚀性液体" being noticed or about to be handled. high-risk mood: urgent but educational, no injury, no explosion, no horror. The visual risk should match this Chinese description: 人员暴露需要立即处置。
Main character: Lin Cheng; young Chinese female graduate student, short black bob hair, clear goggles, white lab coat, blue inner shirt, often holding a notebook, careful and detail-oriented.
Scene environment: educational emergency response scene in a lab, clear evacuation path, barrier tape, emergency equipment, no graphic injury.
Required visual elements: acid/base bottle, splash control, secondary tray, simple hazard pictogram with no text; potential exposure risk shown by distance, vapor, or an uncapped container, without injury; eyewash, safety shower, first aid box, emergency button as background shapes; phone or radio reporting gesture, screen blank, no readable UI; guiding people away, setting a barrier, maintaining distance.
Additional card context from the rules: knowledge: 人员暴露应优先冲洗并报告。.
Composition: vertical 2:3 card illustration; risk source in foreground or lower-left third; character in mid-ground observing or responding; rounded-card safe margins.
Extra production rule: The risk must be visually obvious, but the image must not show injury, disaster aftermath, or panic. Leave visual space for later card text layout.
Color and material: pale blue, white, gray-blue, transparent glass, soft reflections on the lab bench, small amount of orange/yellow only for safety warning symbols or flame.
Border and crop: the image may include a thin rounded rectangle card border and warm off-white paper margin; keep all important subjects away from the edge.

Strict negative prompt: no readable Chinese text, no readable English text, no readable numbers, no logo, no watermark, no brand name, no school emblem, no UI text, no readable bottle labels, no readable notebook content, no readable clipboard content, no title, no card frame text. Labels, forms, badges and screens must be blank, blurred, or meaningless lines only. No photorealistic style, no 3D render, no chibi style, no horror style, no gore, no injured people, no large explosion, no chaotic disaster, no distorted face, no extra fingers, no missing hands, no duplicated faces, no cluttered composition.
```

### E14 Event card | 闻嗅未知气味

```text
Create ONE vertical no-text illustration for a laboratory safety board-game card.

Reference style: use the uploaded sample images as the main style reference. Match their clean academic watercolor look, blue-white palette, soft natural window light, transparent glassware, delicate anime-inspired characters, realistic chemistry lab equipment, rounded card-frame feeling, and calm educational tone.

Card ID: E14
Card type: Event card
Chinese card name: 闻嗅未知气味
Visual goal: Show the safety event "闻嗅未知气味" being noticed or about to be handled. medium-risk mood: serious expression, operation needs correction soon. The visual risk should match this Chinese description: 未知挥发物暴露。
Main character: Zhou Heng; young Chinese male graduate student, short black hair, clear goggles, white lab coat, blue inner shirt, blue nitrile gloves, skilled at hands-on experiments.
Scene environment: active experiment area of a modern chemistry lab, fume hood, glassware, clamps, heating or transfer setup.
Required visual elements: unknown transparent reagent bottle and cautious inspection gesture; potential exposure risk shown by distance, vapor, or an uncapped container, without injury; fume hood, airflow arrows as simple graphic marks, operation moved toward the hood; guiding people away, setting a barrier, maintaining distance; phone or radio reporting gesture, screen blank, no readable UI.
Additional card context from the rules: knowledge: 未知气味不应直接闻嗅判断。.
Composition: vertical 2:3 card illustration; risk source in foreground or lower-left third; character in mid-ground observing or responding; rounded-card safe margins.
Extra production rule: The risk must be visually obvious, but the image must not show injury, disaster aftermath, or panic. Leave visual space for later card text layout.
Color and material: pale blue, white, gray-blue, transparent glass, soft reflections on the lab bench, small amount of orange/yellow only for safety warning symbols or flame.
Border and crop: the image may include a thin rounded rectangle card border and warm off-white paper margin; keep all important subjects away from the edge.

Strict negative prompt: no readable Chinese text, no readable English text, no readable numbers, no logo, no watermark, no brand name, no school emblem, no UI text, no readable bottle labels, no readable notebook content, no readable clipboard content, no title, no card frame text. Labels, forms, badges and screens must be blank, blurred, or meaningless lines only. No photorealistic style, no 3D render, no chibi style, no horror style, no gore, no injured people, no large explosion, no chaotic disaster, no distorted face, no extra fingers, no missing hands, no duplicated faces, no cluttered composition.
```

### E15 Event card | 实验台出现小型明火

```text
Create ONE vertical no-text illustration for a laboratory safety board-game card.

Reference style: use the uploaded sample images as the main style reference. Match their clean academic watercolor look, blue-white palette, soft natural window light, transparent glassware, delicate anime-inspired characters, realistic chemistry lab equipment, rounded card-frame feeling, and calm educational tone.

Card ID: E15
Card type: Event card
Chinese card name: 实验台出现小型明火
Visual goal: Show the safety event "实验台出现小型明火" being noticed or about to be handled. high-risk mood: urgent but educational, no injury, no explosion, no horror. The visual risk should match this Chinese description: 火情初期处置窗口有限。
Main character: Gu Ning; young Chinese female doctoral student, low ponytail or short hair, goggles, lab coat, calm posture, good at recording and verification.
Scene environment: educational emergency response scene in a lab, clear evacuation path, barrier tape, emergency equipment, no graphic injury.
Required visual elements: small controlled flame, heat source, flammable pictogram only, no explosion; eyewash, safety shower, first aid box, emergency button as background shapes; turning off heat, power, or valve, clear switch action; guiding people away, setting a barrier, maintaining distance; phone or radio reporting gesture, screen blank, no readable UI.
Additional card context from the rules: knowledge: 小型明火需先判断火源和灭火方式。.
Composition: vertical 2:3 card illustration; risk source in foreground or lower-left third; character in mid-ground observing or responding; rounded-card safe margins.
Extra production rule: The risk must be visually obvious, but the image must not show injury, disaster aftermath, or panic. Leave visual space for later card text layout.
Color and material: pale blue, white, gray-blue, transparent glass, soft reflections on the lab bench, small amount of orange/yellow only for safety warning symbols or flame.
Border and crop: the image may include a thin rounded rectangle card border and warm off-white paper margin; keep all important subjects away from the edge.

Strict negative prompt: no readable Chinese text, no readable English text, no readable numbers, no logo, no watermark, no brand name, no school emblem, no UI text, no readable bottle labels, no readable notebook content, no readable clipboard content, no title, no card frame text. Labels, forms, badges and screens must be blank, blurred, or meaningless lines only. No photorealistic style, no 3D render, no chibi style, no horror style, no gore, no injured people, no large explosion, no chaotic disaster, no distorted face, no extra fingers, no missing hands, no duplicated faces, no cluttered composition.
```

### E16 Event card | 锐器混入普通垃圾

```text
Create ONE vertical no-text illustration for a laboratory safety board-game card.

Reference style: use the uploaded sample images as the main style reference. Match their clean academic watercolor look, blue-white palette, soft natural window light, transparent glassware, delicate anime-inspired characters, realistic chemistry lab equipment, rounded card-frame feeling, and calm educational tone.

Card ID: E16
Card type: Event card
Chinese card name: 锐器混入普通垃圾
Visual goal: Show the safety event "锐器混入普通垃圾" being noticed or about to be handled. medium-risk mood: serious expression, operation needs correction soon. The visual risk should match this Chinese description: 后续人员割伤风险。
Main character: Cheng Yan; mature Chinese male doctoral student or teaching assistant, white lab coat, blue shirt, steady posture, coordinates laboratory safety.
Scene environment: general modern chemistry lab operation scene, clean bench, glassware, safety equipment, bright window light.
Required visual elements: sharp object or broken glass in a dedicated container, no injury; waste bottle, sorted waste container, cleanup action, blank label only; barrier tape, safe perimeter, clear risk boundary; open lab notebook, blank grid sheet, pen, inventory ledger with no readable characters; two lab members confirming a risk with calm gestures.
Additional card context from the rules: knowledge: 锐器应进入专用容器。.
Composition: vertical 2:3 card illustration; risk source in foreground or lower-left third; character in mid-ground observing or responding; rounded-card safe margins.
Extra production rule: The risk must be visually obvious, but the image must not show injury, disaster aftermath, or panic. Leave visual space for later card text layout.
Color and material: pale blue, white, gray-blue, transparent glass, soft reflections on the lab bench, small amount of orange/yellow only for safety warning symbols or flame.
Border and crop: the image may include a thin rounded rectangle card border and warm off-white paper margin; keep all important subjects away from the edge.

Strict negative prompt: no readable Chinese text, no readable English text, no readable numbers, no logo, no watermark, no brand name, no school emblem, no UI text, no readable bottle labels, no readable notebook content, no readable clipboard content, no title, no card frame text. Labels, forms, badges and screens must be blank, blurred, or meaningless lines only. No photorealistic style, no 3D render, no chibi style, no horror style, no gore, no injured people, no large explosion, no chaotic disaster, no distorted face, no extra fingers, no missing hands, no duplicated faces, no cluttered composition.
```

### E17 Event card | 加热装置温度异常升高

```text
Create ONE vertical no-text illustration for a laboratory safety board-game card.

Reference style: use the uploaded sample images as the main style reference. Match their clean academic watercolor look, blue-white palette, soft natural window light, transparent glassware, delicate anime-inspired characters, realistic chemistry lab equipment, rounded card-frame feeling, and calm educational tone.

Card ID: E17
Card type: Event card
Chinese card name: 加热装置温度异常升高
Visual goal: Show the safety event "加热装置温度异常升高" being noticed or about to be handled. high-risk mood: urgent but educational, no injury, no explosion, no horror. The visual risk should match this Chinese description: 反应温度偏离预期。
Main character: Lin Cheng; young Chinese female graduate student, short black bob hair, clear goggles, white lab coat, blue inner shirt, often holding a notebook, careful and detail-oriented.
Scene environment: active experiment area of a modern chemistry lab, fume hood, glassware, clamps, heating or transfer setup.
Required visual elements: heating mantle, hot plate, warm glassware, heat source control; turning off heat, power, or valve, clear switch action; phone or radio reporting gesture, screen blank, no readable UI; cooling water hose, ice bath, condenser, cooling control.
Additional card context from the rules: knowledge: 温度异常应先控制能量输入。.
Composition: vertical 2:3 card illustration; risk source in foreground or lower-left third; character in mid-ground observing or responding; rounded-card safe margins.
Extra production rule: The risk must be visually obvious, but the image must not show injury, disaster aftermath, or panic. Leave visual space for later card text layout.
Color and material: pale blue, white, gray-blue, transparent glass, soft reflections on the lab bench, small amount of orange/yellow only for safety warning symbols or flame.
Border and crop: the image may include a thin rounded rectangle card border and warm off-white paper margin; keep all important subjects away from the edge.

Strict negative prompt: no readable Chinese text, no readable English text, no readable numbers, no logo, no watermark, no brand name, no school emblem, no UI text, no readable bottle labels, no readable notebook content, no readable clipboard content, no title, no card frame text. Labels, forms, badges and screens must be blank, blurred, or meaningless lines only. No photorealistic style, no 3D render, no chibi style, no horror style, no gore, no injured people, no large explosion, no chaotic disaster, no distorted face, no extra fingers, no missing hands, no duplicated faces, no cluttered composition.
```

### E18 Event card | 设备未断电且记录缺失

```text
Create ONE vertical no-text illustration for a laboratory safety board-game card.

Reference style: use the uploaded sample images as the main style reference. Match their clean academic watercolor look, blue-white palette, soft natural window light, transparent glassware, delicate anime-inspired characters, realistic chemistry lab equipment, rounded card-frame feeling, and calm educational tone.

Card ID: E18
Card type: Event card
Chinese card name: 设备未断电且记录缺失
Visual goal: Show the safety event "设备未断电且记录缺失" being noticed or about to be handled. medium-risk mood: serious expression, operation needs correction soon. The visual risk should match this Chinese description: 收尾遗漏影响后续安全。
Main character: Zhou Heng; young Chinese male graduate student, short black hair, clear goggles, white lab coat, blue inner shirt, blue nitrile gloves, skilled at hands-on experiments.
Scene environment: general modern chemistry lab operation scene, clean bench, glassware, safety equipment, bright window light.
Required visual elements: clamps, stands, condenser, heating mantle, instrument panel, physically plausible equipment; open lab notebook, blank grid sheet, pen, inventory ledger with no readable characters; turning off heat, power, or valve, clear switch action; checking clamps, valves, labels, airflow, or equipment connections; two lab members confirming a risk with calm gestures.
Additional card context from the rules: knowledge: 设备收尾必须断电并记录状态。.
Composition: vertical 2:3 card illustration; risk source in foreground or lower-left third; character in mid-ground observing or responding; rounded-card safe margins.
Extra production rule: The risk must be visually obvious, but the image must not show injury, disaster aftermath, or panic. Leave visual space for later card text layout.
Color and material: pale blue, white, gray-blue, transparent glass, soft reflections on the lab bench, small amount of orange/yellow only for safety warning symbols or flame.
Border and crop: the image may include a thin rounded rectangle card border and warm off-white paper margin; keep all important subjects away from the edge.

Strict negative prompt: no readable Chinese text, no readable English text, no readable numbers, no logo, no watermark, no brand name, no school emblem, no UI text, no readable bottle labels, no readable notebook content, no readable clipboard content, no title, no card frame text. Labels, forms, badges and screens must be blank, blurred, or meaningless lines only. No photorealistic style, no 3D render, no chibi style, no horror style, no gore, no injured people, no large explosion, no chaotic disaster, no distorted face, no extra fingers, no missing hands, no duplicated faces, no cluttered composition.
```

### E19 Event card | 样品瓶盖未拧紧

```text
Create ONE vertical no-text illustration for a laboratory safety board-game card.

Reference style: use the uploaded sample images as the main style reference. Match their clean academic watercolor look, blue-white palette, soft natural window light, transparent glassware, delicate anime-inspired characters, realistic chemistry lab equipment, rounded card-frame feeling, and calm educational tone.

Card ID: E19
Card type: Event card
Chinese card name: 样品瓶盖未拧紧
Visual goal: Show the safety event "样品瓶盖未拧紧" being noticed or about to be handled. low-risk mood: calm, clear risk source, no accident consequence. The visual risk should match this Chinese description: 泄漏和挥发风险。
Main character: Gu Ning; young Chinese female doctoral student, low ponytail or short hair, goggles, lab coat, calm posture, good at recording and verification.
Scene environment: active experiment area of a modern chemistry lab, fume hood, glassware, clamps, heating or transfer setup.
Required visual elements: secondary tray, absorbent pad, container boundary preventing spread; reagent bottle with blank or blurred label, absolutely no readable text; checking clamps, valves, labels, airflow, or equipment connections.
Additional card context from the rules: knowledge: 容器密封是防泄漏的基础。.
Composition: vertical 2:3 card illustration; risk source in foreground or lower-left third; character in mid-ground observing or responding; rounded-card safe margins.
Extra production rule: The risk must be visually obvious, but the image must not show injury, disaster aftermath, or panic. Leave visual space for later card text layout.
Color and material: pale blue, white, gray-blue, transparent glass, soft reflections on the lab bench, small amount of orange/yellow only for safety warning symbols or flame.
Border and crop: the image may include a thin rounded rectangle card border and warm off-white paper margin; keep all important subjects away from the edge.

Strict negative prompt: no readable Chinese text, no readable English text, no readable numbers, no logo, no watermark, no brand name, no school emblem, no UI text, no readable bottle labels, no readable notebook content, no readable clipboard content, no title, no card frame text. Labels, forms, badges and screens must be blank, blurred, or meaningless lines only. No photorealistic style, no 3D render, no chibi style, no horror style, no gore, no injured people, no large explosion, no chaotic disaster, no distorted face, no extra fingers, no missing hands, no duplicated faces, no cluttered composition.
```

### E20 Event card | 离心样品配平异常

```text
Create ONE vertical no-text illustration for a laboratory safety board-game card.

Reference style: use the uploaded sample images as the main style reference. Match their clean academic watercolor look, blue-white palette, soft natural window light, transparent glassware, delicate anime-inspired characters, realistic chemistry lab equipment, rounded card-frame feeling, and calm educational tone.

Card ID: E20
Card type: Event card
Chinese card name: 离心样品配平异常
Visual goal: Show the safety event "离心样品配平异常" being noticed or about to be handled. medium-risk mood: serious expression, operation needs correction soon. The visual risk should match this Chinese description: 设备震动和损坏风险。
Main character: Cheng Yan; mature Chinese male doctoral student or teaching assistant, white lab coat, blue shirt, steady posture, coordinates laboratory safety.
Scene environment: active experiment area of a modern chemistry lab, fume hood, glassware, clamps, heating or transfer setup.
Required visual elements: clamps, stands, condenser, heating mantle, instrument panel, physically plausible equipment; team balancing safety and efficiency, two visible decision paths; unstable bench arrangement or glassware too close to edge; checking clamps, valves, labels, airflow, or equipment connections; tightening clamp, stabilizing stand, securing tubing or vessel; turning off heat, power, or valve, clear switch action; open lab notebook, blank grid sheet, pen, inventory ledger with no readable characters.
Additional card context from the rules: knowledge: 离心前必须重新确认配平。.
Composition: vertical 2:3 card illustration; risk source in foreground or lower-left third; character in mid-ground observing or responding; rounded-card safe margins.
Extra production rule: The risk must be visually obvious, but the image must not show injury, disaster aftermath, or panic. Leave visual space for later card text layout.
Color and material: pale blue, white, gray-blue, transparent glass, soft reflections on the lab bench, small amount of orange/yellow only for safety warning symbols or flame.
Border and crop: the image may include a thin rounded rectangle card border and warm off-white paper margin; keep all important subjects away from the edge.

Strict negative prompt: no readable Chinese text, no readable English text, no readable numbers, no logo, no watermark, no brand name, no school emblem, no UI text, no readable bottle labels, no readable notebook content, no readable clipboard content, no title, no card frame text. Labels, forms, badges and screens must be blank, blurred, or meaningless lines only. No photorealistic style, no 3D render, no chibi style, no horror style, no gore, no injured people, no large explosion, no chaotic disaster, no distorted face, no extra fingers, no missing hands, no duplicated faces, no cluttered composition.
```

### E21 Event card | 旋蒸夹具松动

```text
Create ONE vertical no-text illustration for a laboratory safety board-game card.

Reference style: use the uploaded sample images as the main style reference. Match their clean academic watercolor look, blue-white palette, soft natural window light, transparent glassware, delicate anime-inspired characters, realistic chemistry lab equipment, rounded card-frame feeling, and calm educational tone.

Card ID: E21
Card type: Event card
Chinese card name: 旋蒸夹具松动
Visual goal: Show the safety event "旋蒸夹具松动" being noticed or about to be handled. medium-risk mood: serious expression, operation needs correction soon. The visual risk should match this Chinese description: 玻璃部件坠落或破裂风险。
Main character: Lin Cheng; young Chinese female graduate student, short black bob hair, clear goggles, white lab coat, blue inner shirt, often holding a notebook, careful and detail-oriented.
Scene environment: active experiment area of a modern chemistry lab, fume hood, glassware, clamps, heating or transfer setup.
Required visual elements: clamps, stands, condenser, heating mantle, instrument panel, physically plausible equipment; cracked glassware or glass shards contained in a tray, no blood; tightening clamp, stabilizing stand, securing tubing or vessel; checking clamps, valves, labels, airflow, or equipment connections; turning off heat, power, or valve, clear switch action; tidy bench, wiping action, cleaning tools, organized glassware.
Additional card context from the rules: knowledge: 旋蒸前后都要检查夹具和收集瓶。.
Composition: vertical 2:3 card illustration; risk source in foreground or lower-left third; character in mid-ground observing or responding; rounded-card safe margins.
Extra production rule: The risk must be visually obvious, but the image must not show injury, disaster aftermath, or panic. Leave visual space for later card text layout.
Color and material: pale blue, white, gray-blue, transparent glass, soft reflections on the lab bench, small amount of orange/yellow only for safety warning symbols or flame.
Border and crop: the image may include a thin rounded rectangle card border and warm off-white paper margin; keep all important subjects away from the edge.

Strict negative prompt: no readable Chinese text, no readable English text, no readable numbers, no logo, no watermark, no brand name, no school emblem, no UI text, no readable bottle labels, no readable notebook content, no readable clipboard content, no title, no card frame text. Labels, forms, badges and screens must be blank, blurred, or meaningless lines only. No photorealistic style, no 3D render, no chibi style, no horror style, no gore, no injured people, no large explosion, no chaotic disaster, no distorted face, no extra fingers, no missing hands, no duplicated faces, no cluttered composition.
```

### E22 Event card | 废液桶接近满载

```text
Create ONE vertical no-text illustration for a laboratory safety board-game card.

Reference style: use the uploaded sample images as the main style reference. Match their clean academic watercolor look, blue-white palette, soft natural window light, transparent glassware, delicate anime-inspired characters, realistic chemistry lab equipment, rounded card-frame feeling, and calm educational tone.

Card ID: E22
Card type: Event card
Chinese card name: 废液桶接近满载
Visual goal: Show the safety event "废液桶接近满载" being noticed or about to be handled. medium-risk mood: serious expression, operation needs correction soon. The visual risk should match this Chinese description: 溢出和混放风险上升。
Main character: Zhou Heng; young Chinese male graduate student, short black hair, clear goggles, white lab coat, blue inner shirt, blue nitrile gloves, skilled at hands-on experiments.
Scene environment: general modern chemistry lab operation scene, clean bench, glassware, safety equipment, bright window light.
Required visual elements: waste bottle, sorted waste container, cleanup action, blank label only; secondary tray, absorbent pad, container boundary preventing spread; phone or radio reporting gesture, screen blank, no readable UI; open lab notebook, blank grid sheet, pen, inventory ledger with no readable characters.
Additional card context from the rules: knowledge: 废液桶不应装得过满。.
Composition: vertical 2:3 card illustration; risk source in foreground or lower-left third; character in mid-ground observing or responding; rounded-card safe margins.
Extra production rule: The risk must be visually obvious, but the image must not show injury, disaster aftermath, or panic. Leave visual space for later card text layout.
Color and material: pale blue, white, gray-blue, transparent glass, soft reflections on the lab bench, small amount of orange/yellow only for safety warning symbols or flame.
Border and crop: the image may include a thin rounded rectangle card border and warm off-white paper margin; keep all important subjects away from the edge.

Strict negative prompt: no readable Chinese text, no readable English text, no readable numbers, no logo, no watermark, no brand name, no school emblem, no UI text, no readable bottle labels, no readable notebook content, no readable clipboard content, no title, no card frame text. Labels, forms, badges and screens must be blank, blurred, or meaningless lines only. No photorealistic style, no 3D render, no chibi style, no horror style, no gore, no injured people, no large explosion, no chaotic disaster, no distorted face, no extra fingers, no missing hands, no duplicated faces, no cluttered composition.
```

### E23 Event card | 未知粉末散落并引发不适

```text
Create ONE vertical no-text illustration for a laboratory safety board-game card.

Reference style: use the uploaded sample images as the main style reference. Match their clean academic watercolor look, blue-white palette, soft natural window light, transparent glassware, delicate anime-inspired characters, realistic chemistry lab equipment, rounded card-frame feeling, and calm educational tone.

Card ID: E23
Card type: Event card
Chinese card name: 未知粉末散落并引发不适
Visual goal: Show the safety event "未知粉末散落并引发不适" being noticed or about to be handled. high-risk mood: urgent but educational, no injury, no explosion, no horror. The visual risk should match this Chinese description: 未知暴露和吸入风险。
Main character: Gu Ning; young Chinese female doctoral student, low ponytail or short hair, goggles, lab coat, calm posture, good at recording and verification.
Scene environment: educational emergency response scene in a lab, clear evacuation path, barrier tape, emergency equipment, no graphic injury.
Required visual elements: unknown transparent reagent bottle and cautious inspection gesture; small liquid spill, absorbent pad, tray boundary, contained spread; potential exposure risk shown by distance, vapor, or an uncapped container, without injury; barrier tape, safe perimeter, clear risk boundary; guiding people away, setting a barrier, maintaining distance; phone or radio reporting gesture, screen blank, no readable UI; safety goggles, blue nitrile gloves, white lab coat, visible PPE checking or wearing action.
Additional card context from the rules: knowledge: 未知粉末应先隔离和上报，不应直接清扫。.
Composition: vertical 2:3 card illustration; risk source in foreground or lower-left third; character in mid-ground observing or responding; rounded-card safe margins.
Extra production rule: The risk must be visually obvious, but the image must not show injury, disaster aftermath, or panic. Leave visual space for later card text layout.
Color and material: pale blue, white, gray-blue, transparent glass, soft reflections on the lab bench, small amount of orange/yellow only for safety warning symbols or flame.
Border and crop: the image may include a thin rounded rectangle card border and warm off-white paper margin; keep all important subjects away from the edge.

Strict negative prompt: no readable Chinese text, no readable English text, no readable numbers, no logo, no watermark, no brand name, no school emblem, no UI text, no readable bottle labels, no readable notebook content, no readable clipboard content, no title, no card frame text. Labels, forms, badges and screens must be blank, blurred, or meaningless lines only. No photorealistic style, no 3D render, no chibi style, no horror style, no gore, no injured people, no large explosion, no chaotic disaster, no distorted face, no extra fingers, no missing hands, no duplicated faces, no cluttered composition.
```

### E24 Event card | 临时容器无二次标签

```text
Create ONE vertical no-text illustration for a laboratory safety board-game card.

Reference style: use the uploaded sample images as the main style reference. Match their clean academic watercolor look, blue-white palette, soft natural window light, transparent glassware, delicate anime-inspired characters, realistic chemistry lab equipment, rounded card-frame feeling, and calm educational tone.

Card ID: E24
Card type: Event card
Chinese card name: 临时容器无二次标签
Visual goal: Show the safety event "临时容器无二次标签" being noticed or about to be handled. low-risk mood: calm, clear risk source, no accident consequence. The visual risk should match this Chinese description: 中间样品身份不清。
Main character: Cheng Yan; mature Chinese male doctoral student or teaching assistant, white lab coat, blue shirt, steady posture, coordinates laboratory safety.
Scene environment: active experiment area of a modern chemistry lab, fume hood, glassware, clamps, heating or transfer setup.
Required visual elements: reagent bottle with blank or blurred label, absolutely no readable text; open lab notebook, blank grid sheet, pen, inventory ledger with no readable characters; comparing bottle, blank notebook, and inventory sheet; two lab members confirming a risk with calm gestures.
Additional card context from the rules: knowledge: 临时容器也需要清晰标识。.
Composition: vertical 2:3 card illustration; risk source in foreground or lower-left third; character in mid-ground observing or responding; rounded-card safe margins.
Extra production rule: The risk must be visually obvious, but the image must not show injury, disaster aftermath, or panic. Leave visual space for later card text layout.
Color and material: pale blue, white, gray-blue, transparent glass, soft reflections on the lab bench, small amount of orange/yellow only for safety warning symbols or flame.
Border and crop: the image may include a thin rounded rectangle card border and warm off-white paper margin; keep all important subjects away from the edge.

Strict negative prompt: no readable Chinese text, no readable English text, no readable numbers, no logo, no watermark, no brand name, no school emblem, no UI text, no readable bottle labels, no readable notebook content, no readable clipboard content, no title, no card frame text. Labels, forms, badges and screens must be blank, blurred, or meaningless lines only. No photorealistic style, no 3D render, no chibi style, no horror style, no gore, no injured people, no large explosion, no chaotic disaster, no distorted face, no extra fingers, no missing hands, no duplicated faces, no cluttered composition.
```

### E25 Event card | 冷凝水管连接松动

```text
Create ONE vertical no-text illustration for a laboratory safety board-game card.

Reference style: use the uploaded sample images as the main style reference. Match their clean academic watercolor look, blue-white palette, soft natural window light, transparent glassware, delicate anime-inspired characters, realistic chemistry lab equipment, rounded card-frame feeling, and calm educational tone.

Card ID: E25
Card type: Event card
Chinese card name: 冷凝水管连接松动
Visual goal: Show the safety event "冷凝水管连接松动" being noticed or about to be handled. medium-risk mood: serious expression, operation needs correction soon. The visual risk should match this Chinese description: 漏水和冷凝失效风险。
Main character: Lin Cheng; young Chinese female graduate student, short black bob hair, clear goggles, white lab coat, blue inner shirt, often holding a notebook, careful and detail-oriented.
Scene environment: active experiment area of a modern chemistry lab, fume hood, glassware, clamps, heating or transfer setup.
Required visual elements: clamps, stands, condenser, heating mantle, instrument panel, physically plausible equipment; tightening clamp, stabilizing stand, securing tubing or vessel; checking clamps, valves, labels, airflow, or equipment connections; turning off heat, power, or valve, clear switch action; tidy bench, wiping action, cleaning tools, organized glassware.
Additional card context from the rules: knowledge: 冷凝水连接应固定并检查流向。.
Composition: vertical 2:3 card illustration; risk source in foreground or lower-left third; character in mid-ground observing or responding; rounded-card safe margins.
Extra production rule: The risk must be visually obvious, but the image must not show injury, disaster aftermath, or panic. Leave visual space for later card text layout.
Color and material: pale blue, white, gray-blue, transparent glass, soft reflections on the lab bench, small amount of orange/yellow only for safety warning symbols or flame.
Border and crop: the image may include a thin rounded rectangle card border and warm off-white paper margin; keep all important subjects away from the edge.

Strict negative prompt: no readable Chinese text, no readable English text, no readable numbers, no logo, no watermark, no brand name, no school emblem, no UI text, no readable bottle labels, no readable notebook content, no readable clipboard content, no title, no card frame text. Labels, forms, badges and screens must be blank, blurred, or meaningless lines only. No photorealistic style, no 3D render, no chibi style, no horror style, no gore, no injured people, no large explosion, no chaotic disaster, no distorted face, no extra fingers, no missing hands, no duplicated faces, no cluttered composition.
```

### E26 Event card | 样品记录与瓶身不一致

```text
Create ONE vertical no-text illustration for a laboratory safety board-game card.

Reference style: use the uploaded sample images as the main style reference. Match their clean academic watercolor look, blue-white palette, soft natural window light, transparent glassware, delicate anime-inspired characters, realistic chemistry lab equipment, rounded card-frame feeling, and calm educational tone.

Card ID: E26
Card type: Event card
Chinese card name: 样品记录与瓶身不一致
Visual goal: Show the safety event "样品记录与瓶身不一致" being noticed or about to be handled. medium-risk mood: serious expression, operation needs correction soon. The visual risk should match this Chinese description: 记录错误影响后续判断。
Main character: Zhou Heng; young Chinese male graduate student, short black hair, clear goggles, white lab coat, blue inner shirt, blue nitrile gloves, skilled at hands-on experiments.
Scene environment: preparation area of a modern chemistry lab, clean bench, reagent shelves, inventory notebook, PPE on the table.
Required visual elements: open lab notebook, blank grid sheet, pen, inventory ledger with no readable characters; reagent bottle with blank or blurred label, absolutely no readable text; comparing bottle, blank notebook, and inventory sheet; phone or radio reporting gesture, screen blank, no readable UI.
Additional card context from the rules: knowledge: 记录和实物不一致时必须暂停确认。.
Composition: vertical 2:3 card illustration; risk source in foreground or lower-left third; character in mid-ground observing or responding; rounded-card safe margins.
Extra production rule: The risk must be visually obvious, but the image must not show injury, disaster aftermath, or panic. Leave visual space for later card text layout.
Color and material: pale blue, white, gray-blue, transparent glass, soft reflections on the lab bench, small amount of orange/yellow only for safety warning symbols or flame.
Border and crop: the image may include a thin rounded rectangle card border and warm off-white paper margin; keep all important subjects away from the edge.

Strict negative prompt: no readable Chinese text, no readable English text, no readable numbers, no logo, no watermark, no brand name, no school emblem, no UI text, no readable bottle labels, no readable notebook content, no readable clipboard content, no title, no card frame text. Labels, forms, badges and screens must be blank, blurred, or meaningless lines only. No photorealistic style, no 3D render, no chibi style, no horror style, no gore, no injured people, no large explosion, no chaotic disaster, no distorted face, no extra fingers, no missing hands, no duplicated faces, no cluttered composition.
```

### E27 Event card | PPE 尺寸不合适

```text
Create ONE vertical no-text illustration for a laboratory safety board-game card.

Reference style: use the uploaded sample images as the main style reference. Match their clean academic watercolor look, blue-white palette, soft natural window light, transparent glassware, delicate anime-inspired characters, realistic chemistry lab equipment, rounded card-frame feeling, and calm educational tone.

Card ID: E27
Card type: Event card
Chinese card name: PPE 尺寸不合适
Visual goal: Show the safety event "PPE 尺寸不合适" being noticed or about to be handled. low-risk mood: calm, clear risk source, no accident consequence. The visual risk should match this Chinese description: 防护有效性下降。
Main character: Gu Ning; young Chinese female doctoral student, low ponytail or short hair, goggles, lab coat, calm posture, good at recording and verification.
Scene environment: preparation area of a modern chemistry lab, clean bench, reagent shelves, inventory notebook, PPE on the table.
Required visual elements: safety goggles, blue nitrile gloves, white lab coat, visible PPE checking or wearing action; changing gloves, goggles, or protective clothing; checking clamps, valves, labels, airflow, or equipment connections.
Additional card context from the rules: knowledge: PPE 必须适合当前操作和个人尺寸。.
Composition: vertical 2:3 card illustration; risk source in foreground or lower-left third; character in mid-ground observing or responding; rounded-card safe margins.
Extra production rule: The risk must be visually obvious, but the image must not show injury, disaster aftermath, or panic. Leave visual space for later card text layout.
Color and material: pale blue, white, gray-blue, transparent glass, soft reflections on the lab bench, small amount of orange/yellow only for safety warning symbols or flame.
Border and crop: the image may include a thin rounded rectangle card border and warm off-white paper margin; keep all important subjects away from the edge.

Strict negative prompt: no readable Chinese text, no readable English text, no readable numbers, no logo, no watermark, no brand name, no school emblem, no UI text, no readable bottle labels, no readable notebook content, no readable clipboard content, no title, no card frame text. Labels, forms, badges and screens must be blank, blurred, or meaningless lines only. No photorealistic style, no 3D render, no chibi style, no horror style, no gore, no injured people, no large explosion, no chaotic disaster, no distorted face, no extra fingers, no missing hands, no duplicated faces, no cluttered composition.
```

### E28 Event card | 吸液管污染交叉使用

```text
Create ONE vertical no-text illustration for a laboratory safety board-game card.

Reference style: use the uploaded sample images as the main style reference. Match their clean academic watercolor look, blue-white palette, soft natural window light, transparent glassware, delicate anime-inspired characters, realistic chemistry lab equipment, rounded card-frame feeling, and calm educational tone.

Card ID: E28
Card type: Event card
Chinese card name: 吸液管污染交叉使用
Visual goal: Show the safety event "吸液管污染交叉使用" being noticed or about to be handled. medium-risk mood: serious expression, operation needs correction soon. The visual risk should match this Chinese description: 交叉污染影响结果和安全。
Main character: Cheng Yan; mature Chinese male doctoral student or teaching assistant, white lab coat, blue shirt, steady posture, coordinates laboratory safety.
Scene environment: active experiment area of a modern chemistry lab, fume hood, glassware, clamps, heating or transfer setup.
Required visual elements: two containers or pipettes too close, cross-contamination risk; clamps, stands, condenser, heating mantle, instrument panel, physically plausible equipment; changing gloves, goggles, or protective clothing; tidy bench, wiping action, cleaning tools, organized glassware; open lab notebook, blank grid sheet, pen, inventory ledger with no readable characters; two lab members confirming a risk with calm gestures.
Additional card context from the rules: knowledge: 污染耗材不应跨样品继续使用。.
Composition: vertical 2:3 card illustration; risk source in foreground or lower-left third; character in mid-ground observing or responding; rounded-card safe margins.
Extra production rule: The risk must be visually obvious, but the image must not show injury, disaster aftermath, or panic. Leave visual space for later card text layout.
Color and material: pale blue, white, gray-blue, transparent glass, soft reflections on the lab bench, small amount of orange/yellow only for safety warning symbols or flame.
Border and crop: the image may include a thin rounded rectangle card border and warm off-white paper margin; keep all important subjects away from the edge.

Strict negative prompt: no readable Chinese text, no readable English text, no readable numbers, no logo, no watermark, no brand name, no school emblem, no UI text, no readable bottle labels, no readable notebook content, no readable clipboard content, no title, no card frame text. Labels, forms, badges and screens must be blank, blurred, or meaningless lines only. No photorealistic style, no 3D render, no chibi style, no horror style, no gore, no injured people, no large explosion, no chaotic disaster, no distorted face, no extra fingers, no missing hands, no duplicated faces, no cluttered composition.
```

### E29 Event card | 反应瓶压力异常

```text
Create ONE vertical no-text illustration for a laboratory safety board-game card.

Reference style: use the uploaded sample images as the main style reference. Match their clean academic watercolor look, blue-white palette, soft natural window light, transparent glassware, delicate anime-inspired characters, realistic chemistry lab equipment, rounded card-frame feeling, and calm educational tone.

Card ID: E29
Card type: Event card
Chinese card name: 反应瓶压力异常
Visual goal: Show the safety event "反应瓶压力异常" being noticed or about to be handled. high-risk mood: urgent but educational, no injury, no explosion, no horror. The visual risk should match this Chinese description: 体系压力上升。
Main character: Lin Cheng; young Chinese female graduate student, short black bob hair, clear goggles, white lab coat, blue inner shirt, often holding a notebook, careful and detail-oriented.
Scene environment: active experiment area of a modern chemistry lab, fume hood, glassware, clamps, heating or transfer setup.
Required visual elements: sealed vessel, pressure gauge, slightly tense hose or cap, no rupture; clamps, stands, condenser, heating mantle, instrument panel, physically plausible equipment; turning off heat, power, or valve, clear switch action; phone or radio reporting gesture, screen blank, no readable UI; guiding people away, setting a barrier, maintaining distance.
Additional card context from the rules: knowledge: 压力异常不可贸然打开体系。.
Composition: vertical 2:3 card illustration; risk source in foreground or lower-left third; character in mid-ground observing or responding; rounded-card safe margins.
Extra production rule: The risk must be visually obvious, but the image must not show injury, disaster aftermath, or panic. Leave visual space for later card text layout.
Color and material: pale blue, white, gray-blue, transparent glass, soft reflections on the lab bench, small amount of orange/yellow only for safety warning symbols or flame.
Border and crop: the image may include a thin rounded rectangle card border and warm off-white paper margin; keep all important subjects away from the edge.

Strict negative prompt: no readable Chinese text, no readable English text, no readable numbers, no logo, no watermark, no brand name, no school emblem, no UI text, no readable bottle labels, no readable notebook content, no readable clipboard content, no title, no card frame text. Labels, forms, badges and screens must be blank, blurred, or meaningless lines only. No photorealistic style, no 3D render, no chibi style, no horror style, no gore, no injured people, no large explosion, no chaotic disaster, no distorted face, no extra fingers, no missing hands, no duplicated faces, no cluttered composition.
```

### E30 Event card | 强氧化剂靠近有机物

```text
Create ONE vertical no-text illustration for a laboratory safety board-game card.

Reference style: use the uploaded sample images as the main style reference. Match their clean academic watercolor look, blue-white palette, soft natural window light, transparent glassware, delicate anime-inspired characters, realistic chemistry lab equipment, rounded card-frame feeling, and calm educational tone.

Card ID: E30
Card type: Event card
Chinese card name: 强氧化剂靠近有机物
Visual goal: Show the safety event "强氧化剂靠近有机物" being noticed or about to be handled. high-risk mood: urgent but educational, no injury, no explosion, no horror. The visual risk should match this Chinese description: 不相容储存风险。
Main character: Zhou Heng; young Chinese male graduate student, short black hair, clear goggles, white lab coat, blue inner shirt, blue nitrile gloves, skilled at hands-on experiments.
Scene environment: preparation area of a modern chemistry lab, clean bench, reagent shelves, inventory notebook, PPE on the table.
Required visual elements: barrier tape, safe perimeter, clear risk boundary; reagent bottle with blank or blurred label, absolutely no readable text; open lab notebook, blank grid sheet, pen, inventory ledger with no readable characters; phone or radio reporting gesture, screen blank, no readable UI.
Additional card context from the rules: knowledge: 不相容化学品必须分开存放。.
Composition: vertical 2:3 card illustration; risk source in foreground or lower-left third; character in mid-ground observing or responding; rounded-card safe margins.
Extra production rule: The risk must be visually obvious, but the image must not show injury, disaster aftermath, or panic. Leave visual space for later card text layout.
Color and material: pale blue, white, gray-blue, transparent glass, soft reflections on the lab bench, small amount of orange/yellow only for safety warning symbols or flame.
Border and crop: the image may include a thin rounded rectangle card border and warm off-white paper margin; keep all important subjects away from the edge.

Strict negative prompt: no readable Chinese text, no readable English text, no readable numbers, no logo, no watermark, no brand name, no school emblem, no UI text, no readable bottle labels, no readable notebook content, no readable clipboard content, no title, no card frame text. Labels, forms, badges and screens must be blank, blurred, or meaningless lines only. No photorealistic style, no 3D render, no chibi style, no horror style, no gore, no injured people, no large explosion, no chaotic disaster, no distorted face, no extra fingers, no missing hands, no duplicated faces, no cluttered composition.
```

### E31 Event card | 实验室通道被纸箱占用

```text
Create ONE vertical no-text illustration for a laboratory safety board-game card.

Reference style: use the uploaded sample images as the main style reference. Match their clean academic watercolor look, blue-white palette, soft natural window light, transparent glassware, delicate anime-inspired characters, realistic chemistry lab equipment, rounded card-frame feeling, and calm educational tone.

Card ID: E31
Card type: Event card
Chinese card name: 实验室通道被纸箱占用
Visual goal: Show the safety event "实验室通道被纸箱占用" being noticed or about to be handled. medium-risk mood: serious expression, operation needs correction soon. The visual risk should match this Chinese description: 应急通道受阻。
Main character: Gu Ning; young Chinese female doctoral student, low ponytail or short hair, goggles, lab coat, calm posture, good at recording and verification.
Scene environment: preparation area of a modern chemistry lab, clean bench, reagent shelves, inventory notebook, PPE on the table.
Required visual elements: guiding people away, setting a barrier, maintaining distance; tidy bench, wiping action, cleaning tools, organized glassware; barrier tape, safe perimeter, clear risk boundary; two lab members confirming a risk with calm gestures; open lab notebook, blank grid sheet, pen, inventory ledger with no readable characters.
Additional card context from the rules: knowledge: 疏散通道必须保持畅通。.
Composition: vertical 2:3 card illustration; risk source in foreground or lower-left third; character in mid-ground observing or responding; rounded-card safe margins.
Extra production rule: The risk must be visually obvious, but the image must not show injury, disaster aftermath, or panic. Leave visual space for later card text layout.
Color and material: pale blue, white, gray-blue, transparent glass, soft reflections on the lab bench, small amount of orange/yellow only for safety warning symbols or flame.
Border and crop: the image may include a thin rounded rectangle card border and warm off-white paper margin; keep all important subjects away from the edge.

Strict negative prompt: no readable Chinese text, no readable English text, no readable numbers, no logo, no watermark, no brand name, no school emblem, no UI text, no readable bottle labels, no readable notebook content, no readable clipboard content, no title, no card frame text. Labels, forms, badges and screens must be blank, blurred, or meaningless lines only. No photorealistic style, no 3D render, no chibi style, no horror style, no gore, no injured people, no large explosion, no chaotic disaster, no distorted face, no extra fingers, no missing hands, no duplicated faces, no cluttered composition.
```

### E32 Event card | 洗眼器前堆放杂物

```text
Create ONE vertical no-text illustration for a laboratory safety board-game card.

Reference style: use the uploaded sample images as the main style reference. Match their clean academic watercolor look, blue-white palette, soft natural window light, transparent glassware, delicate anime-inspired characters, realistic chemistry lab equipment, rounded card-frame feeling, and calm educational tone.

Card ID: E32
Card type: Event card
Chinese card name: 洗眼器前堆放杂物
Visual goal: Show the safety event "洗眼器前堆放杂物" being noticed or about to be handled. medium-risk mood: serious expression, operation needs correction soon. The visual risk should match this Chinese description: 应急设施不可及。
Main character: Cheng Yan; mature Chinese male doctoral student or teaching assistant, white lab coat, blue shirt, steady posture, coordinates laboratory safety.
Scene environment: preparation area of a modern chemistry lab, clean bench, reagent shelves, inventory notebook, PPE on the table.
Required visual elements: eyewash, safety shower, first aid box, emergency button as background shapes; tidy bench, wiping action, cleaning tools, organized glassware; checking clamps, valves, labels, airflow, or equipment connections; two lab members confirming a risk with calm gestures; open lab notebook, blank grid sheet, pen, inventory ledger with no readable characters.
Additional card context from the rules: knowledge: 应急设施周围必须保持可达。.
Composition: vertical 2:3 card illustration; risk source in foreground or lower-left third; character in mid-ground observing or responding; rounded-card safe margins.
Extra production rule: The risk must be visually obvious, but the image must not show injury, disaster aftermath, or panic. Leave visual space for later card text layout.
Color and material: pale blue, white, gray-blue, transparent glass, soft reflections on the lab bench, small amount of orange/yellow only for safety warning symbols or flame.
Border and crop: the image may include a thin rounded rectangle card border and warm off-white paper margin; keep all important subjects away from the edge.

Strict negative prompt: no readable Chinese text, no readable English text, no readable numbers, no logo, no watermark, no brand name, no school emblem, no UI text, no readable bottle labels, no readable notebook content, no readable clipboard content, no title, no card frame text. Labels, forms, badges and screens must be blank, blurred, or meaningless lines only. No photorealistic style, no 3D render, no chibi style, no horror style, no gore, no injured people, no large explosion, no chaotic disaster, no distorted face, no extra fingers, no missing hands, no duplicated faces, no cluttered composition.
```

### E33 Event card | 试剂架放置过高过满

```text
Create ONE vertical no-text illustration for a laboratory safety board-game card.

Reference style: use the uploaded sample images as the main style reference. Match their clean academic watercolor look, blue-white palette, soft natural window light, transparent glassware, delicate anime-inspired characters, realistic chemistry lab equipment, rounded card-frame feeling, and calm educational tone.

Card ID: E33
Card type: Event card
Chinese card name: 试剂架放置过高过满
Visual goal: Show the safety event "试剂架放置过高过满" being noticed or about to be handled. medium-risk mood: serious expression, operation needs correction soon. The visual risk should match this Chinese description: 坠落和破裂风险。
Main character: Lin Cheng; young Chinese female graduate student, short black bob hair, clear goggles, white lab coat, blue inner shirt, often holding a notebook, careful and detail-oriented.
Scene environment: preparation area of a modern chemistry lab, clean bench, reagent shelves, inventory notebook, PPE on the table.
Required visual elements: tightening clamp, stabilizing stand, securing tubing or vessel; cracked glassware or glass shards contained in a tray, no blood; barrier tape, safe perimeter, clear risk boundary; checking clamps, valves, labels, airflow, or equipment connections; tidy bench, wiping action, cleaning tools, organized glassware.
Additional card context from the rules: knowledge: 试剂存放要稳定、分类、不过量。.
Composition: vertical 2:3 card illustration; risk source in foreground or lower-left third; character in mid-ground observing or responding; rounded-card safe margins.
Extra production rule: The risk must be visually obvious, but the image must not show injury, disaster aftermath, or panic. Leave visual space for later card text layout.
Color and material: pale blue, white, gray-blue, transparent glass, soft reflections on the lab bench, small amount of orange/yellow only for safety warning symbols or flame.
Border and crop: the image may include a thin rounded rectangle card border and warm off-white paper margin; keep all important subjects away from the edge.

Strict negative prompt: no readable Chinese text, no readable English text, no readable numbers, no logo, no watermark, no brand name, no school emblem, no UI text, no readable bottle labels, no readable notebook content, no readable clipboard content, no title, no card frame text. Labels, forms, badges and screens must be blank, blurred, or meaningless lines only. No photorealistic style, no 3D render, no chibi style, no horror style, no gore, no injured people, no large explosion, no chaotic disaster, no distorted face, no extra fingers, no missing hands, no duplicated faces, no cluttered composition.
```

### E34 Event card | 低温样品结霜难以辨认

```text
Create ONE vertical no-text illustration for a laboratory safety board-game card.

Reference style: use the uploaded sample images as the main style reference. Match their clean academic watercolor look, blue-white palette, soft natural window light, transparent glassware, delicate anime-inspired characters, realistic chemistry lab equipment, rounded card-frame feeling, and calm educational tone.

Card ID: E34
Card type: Event card
Chinese card name: 低温样品结霜难以辨认
Visual goal: Show the safety event "低温样品结霜难以辨认" being noticed or about to be handled. low-risk mood: calm, clear risk source, no accident consequence. The visual risk should match this Chinese description: 低温条件导致标签识别困难。
Main character: Zhou Heng; young Chinese male graduate student, short black hair, clear goggles, white lab coat, blue inner shirt, blue nitrile gloves, skilled at hands-on experiments.
Scene environment: active experiment area of a modern chemistry lab, fume hood, glassware, clamps, heating or transfer setup.
Required visual elements: reagent bottle with blank or blurred label, absolutely no readable text; comparing bottle, blank notebook, and inventory sheet; open lab notebook, blank grid sheet, pen, inventory ledger with no readable characters; safety goggles, blue nitrile gloves, white lab coat, visible PPE checking or wearing action.
Additional card context from the rules: knowledge: 低温样品也要保证标识可读。.
Composition: vertical 2:3 card illustration; risk source in foreground or lower-left third; character in mid-ground observing or responding; rounded-card safe margins.
Extra production rule: The risk must be visually obvious, but the image must not show injury, disaster aftermath, or panic. Leave visual space for later card text layout.
Color and material: pale blue, white, gray-blue, transparent glass, soft reflections on the lab bench, small amount of orange/yellow only for safety warning symbols or flame.
Border and crop: the image may include a thin rounded rectangle card border and warm off-white paper margin; keep all important subjects away from the edge.

Strict negative prompt: no readable Chinese text, no readable English text, no readable numbers, no logo, no watermark, no brand name, no school emblem, no UI text, no readable bottle labels, no readable notebook content, no readable clipboard content, no title, no card frame text. Labels, forms, badges and screens must be blank, blurred, or meaningless lines only. No photorealistic style, no 3D render, no chibi style, no horror style, no gore, no injured people, no large explosion, no chaotic disaster, no distorted face, no extra fingers, no missing hands, no duplicated faces, no cluttered composition.
```

### E35 Event card | 学生独自处理高危事件

```text
Create ONE vertical no-text illustration for a laboratory safety board-game card.

Reference style: use the uploaded sample images as the main style reference. Match their clean academic watercolor look, blue-white palette, soft natural window light, transparent glassware, delicate anime-inspired characters, realistic chemistry lab equipment, rounded card-frame feeling, and calm educational tone.

Card ID: E35
Card type: Event card
Chinese card name: 学生独自处理高危事件
Visual goal: Show the safety event "学生独自处理高危事件" being noticed or about to be handled. high-risk mood: urgent but educational, no injury, no explosion, no horror. The visual risk should match this Chinese description: 超出个人处置能力。
Main character: Gu Ning; young Chinese female doctoral student, low ponytail or short hair, goggles, lab coat, calm posture, good at recording and verification.
Scene environment: educational emergency response scene in a lab, clear evacuation path, barrier tape, emergency equipment, no graphic injury.
Required visual elements: phone or radio reporting gesture, screen blank, no readable UI; eyewash, safety shower, first aid box, emergency button as background shapes; guiding people away, setting a barrier, maintaining distance; barrier tape, safe perimeter, clear risk boundary; two lab members confirming a risk with calm gestures.
Additional card context from the rules: knowledge: 超出处置能力时应立即上报和撤离。.
Composition: vertical 2:3 card illustration; risk source in foreground or lower-left third; character in mid-ground observing or responding; rounded-card safe margins.
Extra production rule: The risk must be visually obvious, but the image must not show injury, disaster aftermath, or panic. Leave visual space for later card text layout.
Color and material: pale blue, white, gray-blue, transparent glass, soft reflections on the lab bench, small amount of orange/yellow only for safety warning symbols or flame.
Border and crop: the image may include a thin rounded rectangle card border and warm off-white paper margin; keep all important subjects away from the edge.

Strict negative prompt: no readable Chinese text, no readable English text, no readable numbers, no logo, no watermark, no brand name, no school emblem, no UI text, no readable bottle labels, no readable notebook content, no readable clipboard content, no title, no card frame text. Labels, forms, badges and screens must be blank, blurred, or meaningless lines only. No photorealistic style, no 3D render, no chibi style, no horror style, no gore, no injured people, no large explosion, no chaotic disaster, no distorted face, no extra fingers, no missing hands, no duplicated faces, no cluttered composition.
```

### E36 Event card | 复盘记录遗漏改进措施

```text
Create ONE vertical no-text illustration for a laboratory safety board-game card.

Reference style: use the uploaded sample images as the main style reference. Match their clean academic watercolor look, blue-white palette, soft natural window light, transparent glassware, delicate anime-inspired characters, realistic chemistry lab equipment, rounded card-frame feeling, and calm educational tone.

Card ID: E36
Card type: Event card
Chinese card name: 复盘记录遗漏改进措施
Visual goal: Show the safety event "复盘记录遗漏改进措施" being noticed or about to be handled. low-risk mood: calm, clear risk source, no accident consequence. The visual risk should match this Chinese description: 同类问题可能重复出现。
Main character: Cheng Yan; mature Chinese male doctoral student or teaching assistant, white lab coat, blue shirt, steady posture, coordinates laboratory safety.
Scene environment: general modern chemistry lab operation scene, clean bench, glassware, safety equipment, bright window light.
Required visual elements: open lab notebook, blank grid sheet, pen, inventory ledger with no readable characters; two lab members confirming a risk with calm gestures.
Additional card context from the rules: knowledge: 复盘要记录原因、措施和责任岗位。.
Composition: vertical 2:3 card illustration; risk source in foreground or lower-left third; character in mid-ground observing or responding; rounded-card safe margins.
Extra production rule: The risk must be visually obvious, but the image must not show injury, disaster aftermath, or panic. Leave visual space for later card text layout.
Color and material: pale blue, white, gray-blue, transparent glass, soft reflections on the lab bench, small amount of orange/yellow only for safety warning symbols or flame.
Border and crop: the image may include a thin rounded rectangle card border and warm off-white paper margin; keep all important subjects away from the edge.

Strict negative prompt: no readable Chinese text, no readable English text, no readable numbers, no logo, no watermark, no brand name, no school emblem, no UI text, no readable bottle labels, no readable notebook content, no readable clipboard content, no title, no card frame text. Labels, forms, badges and screens must be blank, blurred, or meaningless lines only. No photorealistic style, no 3D render, no chibi style, no horror style, no gore, no injured people, no large explosion, no chaotic disaster, no distorted face, no extra fingers, no missing hands, no duplicated faces, no cluttered composition.
```

### T01 Task card | 危险化学品领取与登记

```text
Create ONE vertical no-text illustration for a laboratory safety board-game card.

Reference style: use the uploaded sample images as the main style reference. Match their clean academic watercolor look, blue-white palette, soft natural window light, transparent glassware, delicate anime-inspired characters, realistic chemistry lab equipment, rounded card-frame feeling, and calm educational tone.

Card ID: T01
Card type: Task card
Chinese card name: 危险化学品领取与登记
Visual goal: Show a positive execution scene for the lab task "危险化学品领取与登记". The task objective is: 确认试剂来源、标签和台账。
Main character: Zhou Heng; young Chinese male graduate student, short black hair, clear goggles, white lab coat, blue inner shirt, blue nitrile gloves, skilled at hands-on experiments.
Scene environment: preparation area of a modern chemistry lab, clean bench, reagent shelves, inventory notebook, PPE on the table.
Required visual elements: reagent bottle with blank or blurred label, absolutely no readable text; open lab notebook, blank grid sheet, pen, inventory ledger with no readable characters; comparing bottle, blank notebook, and inventory sheet.
Additional card context from the rules: knowledge: 危险化学品领用必须可追溯。.
Composition: vertical 2:3; person and experiment setup centered; layered foreground glassware; clean fume hood or window in background.
Extra production rule: This should look like a correct or nearly correct laboratory operation, not an accident scene. Preferred action cues: label, record, verify.
Color and material: pale blue, white, gray-blue, transparent glass, soft reflections on the lab bench, small amount of orange/yellow only for safety warning symbols or flame.
Border and crop: the image may include a thin rounded rectangle card border and warm off-white paper margin; keep all important subjects away from the edge.

Strict negative prompt: no readable Chinese text, no readable English text, no readable numbers, no logo, no watermark, no brand name, no school emblem, no UI text, no readable bottle labels, no readable notebook content, no readable clipboard content, no title, no card frame text. Labels, forms, badges and screens must be blank, blurred, or meaningless lines only. No photorealistic style, no 3D render, no chibi style, no horror style, no gore, no injured people, no large explosion, no chaotic disaster, no distorted face, no extra fingers, no missing hands, no duplicated faces, no cluttered composition.
```

### T02 Task card | 通风橱准备与气流确认

```text
Create ONE vertical no-text illustration for a laboratory safety board-game card.

Reference style: use the uploaded sample images as the main style reference. Match their clean academic watercolor look, blue-white palette, soft natural window light, transparent glassware, delicate anime-inspired characters, realistic chemistry lab equipment, rounded card-frame feeling, and calm educational tone.

Card ID: T02
Card type: Task card
Chinese card name: 通风橱准备与气流确认
Visual goal: Show a positive execution scene for the lab task "通风橱准备与气流确认". The task objective is: 确认通风橱状态并整理操作空间。
Main character: Gu Ning; young Chinese female doctoral student, low ponytail or short hair, goggles, lab coat, calm posture, good at recording and verification.
Scene environment: preparation area of a modern chemistry lab, clean bench, reagent shelves, inventory notebook, PPE on the table.
Required visual elements: fume hood, airflow arrows as simple graphic marks, operation moved toward the hood; checking clamps, valves, labels, airflow, or equipment connections; clamps, stands, condenser, heating mantle, instrument panel, physically plausible equipment; tidy bench, wiping action, cleaning tools, organized glassware.
Additional card context from the rules: knowledge: 通风橱不是储物柜，操作前要确认气流。.
Composition: vertical 2:3; person and experiment setup centered; layered foreground glassware; clean fume hood or window in background.
Extra production rule: This should look like a correct or nearly correct laboratory operation, not an accident scene. Preferred action cues: ventilation, inspect, clean.
Color and material: pale blue, white, gray-blue, transparent glass, soft reflections on the lab bench, small amount of orange/yellow only for safety warning symbols or flame.
Border and crop: the image may include a thin rounded rectangle card border and warm off-white paper margin; keep all important subjects away from the edge.

Strict negative prompt: no readable Chinese text, no readable English text, no readable numbers, no logo, no watermark, no brand name, no school emblem, no UI text, no readable bottle labels, no readable notebook content, no readable clipboard content, no title, no card frame text. Labels, forms, badges and screens must be blank, blurred, or meaningless lines only. No photorealistic style, no 3D render, no chibi style, no horror style, no gore, no injured people, no large explosion, no chaotic disaster, no distorted face, no extra fingers, no missing hands, no duplicated faces, no cluttered composition.
```

### T03 Task card | 加热回流装置搭建

```text
Create ONE vertical no-text illustration for a laboratory safety board-game card.

Reference style: use the uploaded sample images as the main style reference. Match their clean academic watercolor look, blue-white palette, soft natural window light, transparent glassware, delicate anime-inspired characters, realistic chemistry lab equipment, rounded card-frame feeling, and calm educational tone.

Card ID: T03
Card type: Task card
Chinese card name: 加热回流装置搭建
Visual goal: Show a positive execution scene for the lab task "加热回流装置搭建". The task objective is: 搭建并检查加热回流系统。
Main character: Cheng Yan; mature Chinese male doctoral student or teaching assistant, white lab coat, blue shirt, steady posture, coordinates laboratory safety.
Scene environment: active experiment area of a modern chemistry lab, fume hood, glassware, clamps, heating or transfer setup.
Required visual elements: heating mantle, hot plate, warm glassware, heat source control; clamps, stands, condenser, heating mantle, instrument panel, physically plausible equipment; small controlled flame, heat source, flammable pictogram only, no explosion; checking clamps, valves, labels, airflow, or equipment connections; tightening clamp, stabilizing stand, securing tubing or vessel; turning off heat, power, or valve, clear switch action.
Additional card context from the rules: knowledge: 加热体系必须关注冷凝、夹具和热源。.
Composition: vertical 2:3; person and experiment setup centered; layered foreground glassware; clean fume hood or window in background.
Extra production rule: This should look like a correct or nearly correct laboratory operation, not an accident scene. Preferred action cues: inspect, secure, shutdown.
Color and material: pale blue, white, gray-blue, transparent glass, soft reflections on the lab bench, small amount of orange/yellow only for safety warning symbols or flame.
Border and crop: the image may include a thin rounded rectangle card border and warm off-white paper margin; keep all important subjects away from the edge.

Strict negative prompt: no readable Chinese text, no readable English text, no readable numbers, no logo, no watermark, no brand name, no school emblem, no UI text, no readable bottle labels, no readable notebook content, no readable clipboard content, no title, no card frame text. Labels, forms, badges and screens must be blank, blurred, or meaningless lines only. No photorealistic style, no 3D render, no chibi style, no horror style, no gore, no injured people, no large explosion, no chaotic disaster, no distorted face, no extra fingers, no missing hands, no duplicated faces, no cluttered composition.
```

### T04 Task card | 有机溶剂转移

```text
Create ONE vertical no-text illustration for a laboratory safety board-game card.

Reference style: use the uploaded sample images as the main style reference. Match their clean academic watercolor look, blue-white palette, soft natural window light, transparent glassware, delicate anime-inspired characters, realistic chemistry lab equipment, rounded card-frame feeling, and calm educational tone.

Card ID: T04
Card type: Task card
Chinese card name: 有机溶剂转移
Visual goal: Show a positive execution scene for the lab task "有机溶剂转移". The task objective is: 在合适环境中转移挥发性溶剂。
Main character: Lin Cheng; young Chinese female graduate student, short black bob hair, clear goggles, white lab coat, blue inner shirt, often holding a notebook, careful and detail-oriented.
Scene environment: active experiment area of a modern chemistry lab, fume hood, glassware, clamps, heating or transfer setup.
Required visual elements: clear solvent bottle, beaker, volatile liquid transfer setup; fume hood, airflow arrows as simple graphic marks, operation moved toward the hood; small controlled flame, heat source, flammable pictogram only, no explosion; potential exposure risk shown by distance, vapor, or an uncapped container, without injury; reagent bottle with blank or blurred label, absolutely no readable text; secondary tray, absorbent pad, container boundary preventing spread.
Additional card context from the rules: knowledge: 挥发性溶剂操作优先进入通风橱。.
Composition: vertical 2:3; person and experiment setup centered; layered foreground glassware; clean fume hood or window in background.
Extra production rule: This should look like a correct or nearly correct laboratory operation, not an accident scene. Preferred action cues: ventilation, label, contain.
Color and material: pale blue, white, gray-blue, transparent glass, soft reflections on the lab bench, small amount of orange/yellow only for safety warning symbols or flame.
Border and crop: the image may include a thin rounded rectangle card border and warm off-white paper margin; keep all important subjects away from the edge.

Strict negative prompt: no readable Chinese text, no readable English text, no readable numbers, no logo, no watermark, no brand name, no school emblem, no UI text, no readable bottle labels, no readable notebook content, no readable clipboard content, no title, no card frame text. Labels, forms, badges and screens must be blank, blurred, or meaningless lines only. No photorealistic style, no 3D render, no chibi style, no horror style, no gore, no injured people, no large explosion, no chaotic disaster, no distorted face, no extra fingers, no missing hands, no duplicated faces, no cluttered composition.
```

### T05 Task card | 酸碱溶液配制

```text
Create ONE vertical no-text illustration for a laboratory safety board-game card.

Reference style: use the uploaded sample images as the main style reference. Match their clean academic watercolor look, blue-white palette, soft natural window light, transparent glassware, delicate anime-inspired characters, realistic chemistry lab equipment, rounded card-frame feeling, and calm educational tone.

Card ID: T05
Card type: Task card
Chinese card name: 酸碱溶液配制
Visual goal: Show a positive execution scene for the lab task "酸碱溶液配制". The task objective is: 按顺序配制并控制飞溅风险。
Main character: Zhou Heng; young Chinese male graduate student, short black hair, clear goggles, white lab coat, blue inner shirt, blue nitrile gloves, skilled at hands-on experiments.
Scene environment: active experiment area of a modern chemistry lab, fume hood, glassware, clamps, heating or transfer setup.
Required visual elements: acid/base bottle, splash control, secondary tray, simple hazard pictogram with no text; safety goggles, blue nitrile gloves, white lab coat, visible PPE checking or wearing action; minor splash risk shown with shield, distance, or careful pouring, no injury; reagent bottle with blank or blurred label, absolutely no readable text; careful acid/base containment or absorbent material, no violent reaction.
Additional card context from the rules: knowledge: 腐蚀性试剂操作必须优先防护和缓慢加入。.
Composition: vertical 2:3; person and experiment setup centered; layered foreground glassware; clean fume hood or window in background.
Extra production rule: This should look like a correct or nearly correct laboratory operation, not an accident scene. Preferred action cues: ppe, label, neutralize.
Color and material: pale blue, white, gray-blue, transparent glass, soft reflections on the lab bench, small amount of orange/yellow only for safety warning symbols or flame.
Border and crop: the image may include a thin rounded rectangle card border and warm off-white paper margin; keep all important subjects away from the edge.

Strict negative prompt: no readable Chinese text, no readable English text, no readable numbers, no logo, no watermark, no brand name, no school emblem, no UI text, no readable bottle labels, no readable notebook content, no readable clipboard content, no title, no card frame text. Labels, forms, badges and screens must be blank, blurred, or meaningless lines only. No photorealistic style, no 3D render, no chibi style, no horror style, no gore, no injured people, no large explosion, no chaotic disaster, no distorted face, no extra fingers, no missing hands, no duplicated faces, no cluttered composition.
```

### T06 Task card | 气瓶连接与检漏

```text
Create ONE vertical no-text illustration for a laboratory safety board-game card.

Reference style: use the uploaded sample images as the main style reference. Match their clean academic watercolor look, blue-white palette, soft natural window light, transparent glassware, delicate anime-inspired characters, realistic chemistry lab equipment, rounded card-frame feeling, and calm educational tone.

Card ID: T06
Card type: Task card
Chinese card name: 气瓶连接与检漏
Visual goal: Show a positive execution scene for the lab task "气瓶连接与检漏". The task objective is: 固定气瓶并检查阀门、接头和泄漏。
Main character: Gu Ning; young Chinese female doctoral student, low ponytail or short hair, goggles, lab coat, calm posture, good at recording and verification.
Scene environment: preparation area of a modern chemistry lab, clean bench, reagent shelves, inventory notebook, PPE on the table.
Required visual elements: gas cylinder, regulator, chain, hose connection; clamps, stands, condenser, heating mantle, instrument panel, physically plausible equipment; sealed vessel, pressure gauge, slightly tense hose or cap, no rupture; tightening clamp, stabilizing stand, securing tubing or vessel; checking clamps, valves, labels, airflow, or equipment connections; phone or radio reporting gesture, screen blank, no readable UI.
Additional card context from the rules: knowledge: 气瓶必须固定，连接后应检漏。.
Composition: vertical 2:3; person and experiment setup centered; layered foreground glassware; clean fume hood or window in background.
Extra production rule: This should look like a correct or nearly correct laboratory operation, not an accident scene. Preferred action cues: secure, inspect, report.
Color and material: pale blue, white, gray-blue, transparent glass, soft reflections on the lab bench, small amount of orange/yellow only for safety warning symbols or flame.
Border and crop: the image may include a thin rounded rectangle card border and warm off-white paper margin; keep all important subjects away from the edge.

Strict negative prompt: no readable Chinese text, no readable English text, no readable numbers, no logo, no watermark, no brand name, no school emblem, no UI text, no readable bottle labels, no readable notebook content, no readable clipboard content, no title, no card frame text. Labels, forms, badges and screens must be blank, blurred, or meaningless lines only. No photorealistic style, no 3D render, no chibi style, no horror style, no gore, no injured people, no large explosion, no chaotic disaster, no distorted face, no extra fingers, no missing hands, no duplicated faces, no cluttered composition.
```

### T07 Task card | 反应过程记录

```text
Create ONE vertical no-text illustration for a laboratory safety board-game card.

Reference style: use the uploaded sample images as the main style reference. Match their clean academic watercolor look, blue-white palette, soft natural window light, transparent glassware, delicate anime-inspired characters, realistic chemistry lab equipment, rounded card-frame feeling, and calm educational tone.

Card ID: T07
Card type: Task card
Chinese card name: 反应过程记录
Visual goal: Show a positive execution scene for the lab task "反应过程记录". The task objective is: 记录温度、时间和异常现象。
Main character: Cheng Yan; mature Chinese male doctoral student or teaching assistant, white lab coat, blue shirt, steady posture, coordinates laboratory safety.
Scene environment: active experiment area of a modern chemistry lab, fume hood, glassware, clamps, heating or transfer setup.
Required visual elements: open lab notebook, blank grid sheet, pen, inventory ledger with no readable characters; comparing bottle, blank notebook, and inventory sheet.
Additional card context from the rules: knowledge: 完整记录有助于发现异常趋势。.
Composition: vertical 2:3; person and experiment setup centered; layered foreground glassware; clean fume hood or window in background.
Extra production rule: This should look like a correct or nearly correct laboratory operation, not an accident scene. Preferred action cues: record, monitor, verify.
Color and material: pale blue, white, gray-blue, transparent glass, soft reflections on the lab bench, small amount of orange/yellow only for safety warning symbols or flame.
Border and crop: the image may include a thin rounded rectangle card border and warm off-white paper margin; keep all important subjects away from the edge.

Strict negative prompt: no readable Chinese text, no readable English text, no readable numbers, no logo, no watermark, no brand name, no school emblem, no UI text, no readable bottle labels, no readable notebook content, no readable clipboard content, no title, no card frame text. Labels, forms, badges and screens must be blank, blurred, or meaningless lines only. No photorealistic style, no 3D render, no chibi style, no horror style, no gore, no injured people, no large explosion, no chaotic disaster, no distorted face, no extra fingers, no missing hands, no duplicated faces, no cluttered composition.
```

### T08 Task card | 废液分类收集

```text
Create ONE vertical no-text illustration for a laboratory safety board-game card.

Reference style: use the uploaded sample images as the main style reference. Match their clean academic watercolor look, blue-white palette, soft natural window light, transparent glassware, delicate anime-inspired characters, realistic chemistry lab equipment, rounded card-frame feeling, and calm educational tone.

Card ID: T08
Card type: Task card
Chinese card name: 废液分类收集
Visual goal: Show a positive execution scene for the lab task "废液分类收集". The task objective is: 按类别处理废液并确认容器标签。
Main character: Lin Cheng; young Chinese female graduate student, short black bob hair, clear goggles, white lab coat, blue inner shirt, often holding a notebook, careful and detail-oriented.
Scene environment: general modern chemistry lab operation scene, clean bench, glassware, safety equipment, bright window light.
Required visual elements: waste bottle, sorted waste container, cleanup action, blank label only; reagent bottle with blank or blurred label, absolutely no readable text; secondary tray, absorbent pad, container boundary preventing spread.
Additional card context from the rules: knowledge: 废液混放可能产生放热、气体或毒性风险。.
Composition: vertical 2:3; person and experiment setup centered; layered foreground glassware; clean fume hood or window in background.
Extra production rule: This should look like a correct or nearly correct laboratory operation, not an accident scene. Preferred action cues: waste, label, contain.
Color and material: pale blue, white, gray-blue, transparent glass, soft reflections on the lab bench, small amount of orange/yellow only for safety warning symbols or flame.
Border and crop: the image may include a thin rounded rectangle card border and warm off-white paper margin; keep all important subjects away from the edge.

Strict negative prompt: no readable Chinese text, no readable English text, no readable numbers, no logo, no watermark, no brand name, no school emblem, no UI text, no readable bottle labels, no readable notebook content, no readable clipboard content, no title, no card frame text. Labels, forms, badges and screens must be blank, blurred, or meaningless lines only. No photorealistic style, no 3D render, no chibi style, no horror style, no gore, no injured people, no large explosion, no chaotic disaster, no distorted face, no extra fingers, no missing hands, no duplicated faces, no cluttered composition.
```

### T09 Task card | 玻璃器皿检查

```text
Create ONE vertical no-text illustration for a laboratory safety board-game card.

Reference style: use the uploaded sample images as the main style reference. Match their clean academic watercolor look, blue-white palette, soft natural window light, transparent glassware, delicate anime-inspired characters, realistic chemistry lab equipment, rounded card-frame feeling, and calm educational tone.

Card ID: T09
Card type: Task card
Chinese card name: 玻璃器皿检查
Visual goal: Show a positive execution scene for the lab task "玻璃器皿检查". The task objective is: 检查裂纹、缺口和污染残留。
Main character: Zhou Heng; young Chinese male graduate student, short black hair, clear goggles, white lab coat, blue inner shirt, blue nitrile gloves, skilled at hands-on experiments.
Scene environment: preparation area of a modern chemistry lab, clean bench, reagent shelves, inventory notebook, PPE on the table.
Required visual elements: cracked glassware or glass shards contained in a tray, no blood; checking clamps, valves, labels, airflow, or equipment connections; sharp object or broken glass in a dedicated container, no injury; tidy bench, wiping action, cleaning tools, organized glassware; changing gloves, goggles, or protective clothing.
Additional card context from the rules: knowledge: 有裂纹的玻璃器皿不应继续使用。.
Composition: vertical 2:3; person and experiment setup centered; layered foreground glassware; clean fume hood or window in background.
Extra production rule: This should look like a correct or nearly correct laboratory operation, not an accident scene. Preferred action cues: inspect, clean, replace.
Color and material: pale blue, white, gray-blue, transparent glass, soft reflections on the lab bench, small amount of orange/yellow only for safety warning symbols or flame.
Border and crop: the image may include a thin rounded rectangle card border and warm off-white paper margin; keep all important subjects away from the edge.

Strict negative prompt: no readable Chinese text, no readable English text, no readable numbers, no logo, no watermark, no brand name, no school emblem, no UI text, no readable bottle labels, no readable notebook content, no readable clipboard content, no title, no card frame text. Labels, forms, badges and screens must be blank, blurred, or meaningless lines only. No photorealistic style, no 3D render, no chibi style, no horror style, no gore, no injured people, no large explosion, no chaotic disaster, no distorted face, no extra fingers, no missing hands, no duplicated faces, no cluttered composition.
```

### T10 Task card | 离心样品配平

```text
Create ONE vertical no-text illustration for a laboratory safety board-game card.

Reference style: use the uploaded sample images as the main style reference. Match their clean academic watercolor look, blue-white palette, soft natural window light, transparent glassware, delicate anime-inspired characters, realistic chemistry lab equipment, rounded card-frame feeling, and calm educational tone.

Card ID: T10
Card type: Task card
Chinese card name: 离心样品配平
Visual goal: Show a positive execution scene for the lab task "离心样品配平". The task objective is: 确认样品配平并检查转子状态。
Main character: Gu Ning; young Chinese female doctoral student, low ponytail or short hair, goggles, lab coat, calm posture, good at recording and verification.
Scene environment: active experiment area of a modern chemistry lab, fume hood, glassware, clamps, heating or transfer setup.
Required visual elements: clamps, stands, condenser, heating mantle, instrument panel, physically plausible equipment; team balancing safety and efficiency, two visible decision paths; unstable bench arrangement or glassware too close to edge; checking clamps, valves, labels, airflow, or equipment connections; tightening clamp, stabilizing stand, securing tubing or vessel; open lab notebook, blank grid sheet, pen, inventory ledger with no readable characters.
Additional card context from the rules: knowledge: 离心前必须确认配平和转子状态。.
Composition: vertical 2:3; person and experiment setup centered; layered foreground glassware; clean fume hood or window in background.
Extra production rule: This should look like a correct or nearly correct laboratory operation, not an accident scene. Preferred action cues: inspect, secure, record.
Color and material: pale blue, white, gray-blue, transparent glass, soft reflections on the lab bench, small amount of orange/yellow only for safety warning symbols or flame.
Border and crop: the image may include a thin rounded rectangle card border and warm off-white paper margin; keep all important subjects away from the edge.

Strict negative prompt: no readable Chinese text, no readable English text, no readable numbers, no logo, no watermark, no brand name, no school emblem, no UI text, no readable bottle labels, no readable notebook content, no readable clipboard content, no title, no card frame text. Labels, forms, badges and screens must be blank, blurred, or meaningless lines only. No photorealistic style, no 3D render, no chibi style, no horror style, no gore, no injured people, no large explosion, no chaotic disaster, no distorted face, no extra fingers, no missing hands, no duplicated faces, no cluttered composition.
```

### T11 Task card | 旋蒸装置检查

```text
Create ONE vertical no-text illustration for a laboratory safety board-game card.

Reference style: use the uploaded sample images as the main style reference. Match their clean academic watercolor look, blue-white palette, soft natural window light, transparent glassware, delicate anime-inspired characters, realistic chemistry lab equipment, rounded card-frame feeling, and calm educational tone.

Card ID: T11
Card type: Task card
Chinese card name: 旋蒸装置检查
Visual goal: Show a positive execution scene for the lab task "旋蒸装置检查". The task objective is: 确认夹具、收集瓶和水浴设置。
Main character: Cheng Yan; mature Chinese male doctoral student or teaching assistant, white lab coat, blue shirt, steady posture, coordinates laboratory safety.
Scene environment: active experiment area of a modern chemistry lab, fume hood, glassware, clamps, heating or transfer setup.
Required visual elements: clamps, stands, condenser, heating mantle, instrument panel, physically plausible equipment; cracked glassware or glass shards contained in a tray, no blood; heating mantle, hot plate, warm glassware, heat source control; checking clamps, valves, labels, airflow, or equipment connections; tightening clamp, stabilizing stand, securing tubing or vessel; turning off heat, power, or valve, clear switch action.
Additional card context from the rules: knowledge: 旋蒸装置松动会导致破裂和样品损失。.
Composition: vertical 2:3; person and experiment setup centered; layered foreground glassware; clean fume hood or window in background.
Extra production rule: This should look like a correct or nearly correct laboratory operation, not an accident scene. Preferred action cues: inspect, secure, shutdown.
Color and material: pale blue, white, gray-blue, transparent glass, soft reflections on the lab bench, small amount of orange/yellow only for safety warning symbols or flame.
Border and crop: the image may include a thin rounded rectangle card border and warm off-white paper margin; keep all important subjects away from the edge.

Strict negative prompt: no readable Chinese text, no readable English text, no readable numbers, no logo, no watermark, no brand name, no school emblem, no UI text, no readable bottle labels, no readable notebook content, no readable clipboard content, no title, no card frame text. Labels, forms, badges and screens must be blank, blurred, or meaningless lines only. No photorealistic style, no 3D render, no chibi style, no horror style, no gore, no injured people, no large explosion, no chaotic disaster, no distorted face, no extra fingers, no missing hands, no duplicated faces, no cluttered composition.
```

### T12 Task card | 实验台收尾清理

```text
Create ONE vertical no-text illustration for a laboratory safety board-game card.

Reference style: use the uploaded sample images as the main style reference. Match their clean academic watercolor look, blue-white palette, soft natural window light, transparent glassware, delicate anime-inspired characters, realistic chemistry lab equipment, rounded card-frame feeling, and calm educational tone.

Card ID: T12
Card type: Task card
Chinese card name: 实验台收尾清理
Visual goal: Show a positive execution scene for the lab task "实验台收尾清理". The task objective is: 清理残液、锐器、污染物和公共台面。
Main character: Lin Cheng; young Chinese female graduate student, short black bob hair, clear goggles, white lab coat, blue inner shirt, often holding a notebook, careful and detail-oriented.
Scene environment: general modern chemistry lab operation scene, clean bench, glassware, safety equipment, bright window light.
Required visual elements: tidy bench, wiping action, cleaning tools, organized glassware; waste bottle, sorted waste container, cleanup action, blank label only; sharp object or broken glass in a dedicated container, no injury; two containers or pipettes too close, cross-contamination risk; checking clamps, valves, labels, airflow, or equipment connections.
Additional card context from the rules: knowledge: 收尾清理是防止后续人员暴露的关键环节。.
Composition: vertical 2:3; person and experiment setup centered; layered foreground glassware; clean fume hood or window in background.
Extra production rule: This should look like a correct or nearly correct laboratory operation, not an accident scene. Preferred action cues: clean, waste, inspect.
Color and material: pale blue, white, gray-blue, transparent glass, soft reflections on the lab bench, small amount of orange/yellow only for safety warning symbols or flame.
Border and crop: the image may include a thin rounded rectangle card border and warm off-white paper margin; keep all important subjects away from the edge.

Strict negative prompt: no readable Chinese text, no readable English text, no readable numbers, no logo, no watermark, no brand name, no school emblem, no UI text, no readable bottle labels, no readable notebook content, no readable clipboard content, no title, no card frame text. Labels, forms, badges and screens must be blank, blurred, or meaningless lines only. No photorealistic style, no 3D render, no chibi style, no horror style, no gore, no injured people, no large explosion, no chaotic disaster, no distorted face, no extra fingers, no missing hands, no duplicated faces, no cluttered composition.
```

### T13 Task card | PPE 检查与更换

```text
Create ONE vertical no-text illustration for a laboratory safety board-game card.

Reference style: use the uploaded sample images as the main style reference. Match their clean academic watercolor look, blue-white palette, soft natural window light, transparent glassware, delicate anime-inspired characters, realistic chemistry lab equipment, rounded card-frame feeling, and calm educational tone.

Card ID: T13
Card type: Task card
Chinese card name: PPE 检查与更换
Visual goal: Show a positive execution scene for the lab task "PPE 检查与更换". The task objective is: 确认护目镜、手套和实验服状态。
Main character: Zhou Heng; young Chinese male graduate student, short black hair, clear goggles, white lab coat, blue inner shirt, blue nitrile gloves, skilled at hands-on experiments.
Scene environment: preparation area of a modern chemistry lab, clean bench, reagent shelves, inventory notebook, PPE on the table.
Required visual elements: safety goggles, blue nitrile gloves, white lab coat, visible PPE checking or wearing action; potential exposure risk shown by distance, vapor, or an uncapped container, without injury; checking clamps, valves, labels, airflow, or equipment connections; changing gloves, goggles, or protective clothing.
Additional card context from the rules: knowledge: PPE 失效时应立即更换。.
Composition: vertical 2:3; person and experiment setup centered; layered foreground glassware; clean fume hood or window in background.
Extra production rule: This should look like a correct or nearly correct laboratory operation, not an accident scene. Preferred action cues: ppe, inspect, replace.
Color and material: pale blue, white, gray-blue, transparent glass, soft reflections on the lab bench, small amount of orange/yellow only for safety warning symbols or flame.
Border and crop: the image may include a thin rounded rectangle card border and warm off-white paper margin; keep all important subjects away from the edge.

Strict negative prompt: no readable Chinese text, no readable English text, no readable numbers, no logo, no watermark, no brand name, no school emblem, no UI text, no readable bottle labels, no readable notebook content, no readable clipboard content, no title, no card frame text. Labels, forms, badges and screens must be blank, blurred, or meaningless lines only. No photorealistic style, no 3D render, no chibi style, no horror style, no gore, no injured people, no large explosion, no chaotic disaster, no distorted face, no extra fingers, no missing hands, no duplicated faces, no cluttered composition.
```

### T14 Task card | 未知样品初步确认

```text
Create ONE vertical no-text illustration for a laboratory safety board-game card.

Reference style: use the uploaded sample images as the main style reference. Match their clean academic watercolor look, blue-white palette, soft natural window light, transparent glassware, delicate anime-inspired characters, realistic chemistry lab equipment, rounded card-frame feeling, and calm educational tone.

Card ID: T14
Card type: Task card
Chinese card name: 未知样品初步确认
Visual goal: Show a positive execution scene for the lab task "未知样品初步确认". The task objective is: 通过记录和负责人确认样品身份。
Main character: Gu Ning; young Chinese female doctoral student, low ponytail or short hair, goggles, lab coat, calm posture, good at recording and verification.
Scene environment: preparation area of a modern chemistry lab, clean bench, reagent shelves, inventory notebook, PPE on the table.
Required visual elements: unknown transparent reagent bottle and cautious inspection gesture; reagent bottle with blank or blurred label, absolutely no readable text; open lab notebook, blank grid sheet, pen, inventory ledger with no readable characters; phone or radio reporting gesture, screen blank, no readable UI.
Additional card context from the rules: knowledge: 未知物质不得凭经验直接使用。.
Composition: vertical 2:3; person and experiment setup centered; layered foreground glassware; clean fume hood or window in background.
Extra production rule: This should look like a correct or nearly correct laboratory operation, not an accident scene. Preferred action cues: label, record, report.
Color and material: pale blue, white, gray-blue, transparent glass, soft reflections on the lab bench, small amount of orange/yellow only for safety warning symbols or flame.
Border and crop: the image may include a thin rounded rectangle card border and warm off-white paper margin; keep all important subjects away from the edge.

Strict negative prompt: no readable Chinese text, no readable English text, no readable numbers, no logo, no watermark, no brand name, no school emblem, no UI text, no readable bottle labels, no readable notebook content, no readable clipboard content, no title, no card frame text. Labels, forms, badges and screens must be blank, blurred, or meaningless lines only. No photorealistic style, no 3D render, no chibi style, no horror style, no gore, no injured people, no large explosion, no chaotic disaster, no distorted face, no extra fingers, no missing hands, no duplicated faces, no cluttered composition.
```

### T15 Task card | 小型泄漏围堵

```text
Create ONE vertical no-text illustration for a laboratory safety board-game card.

Reference style: use the uploaded sample images as the main style reference. Match their clean academic watercolor look, blue-white palette, soft natural window light, transparent glassware, delicate anime-inspired characters, realistic chemistry lab equipment, rounded card-frame feeling, and calm educational tone.

Card ID: T15
Card type: Task card
Chinese card name: 小型泄漏围堵
Visual goal: Show a positive execution scene for the lab task "小型泄漏围堵". The task objective is: 限制泄漏扩散并选择正确清理方式。
Main character: Cheng Yan; mature Chinese male doctoral student or teaching assistant, white lab coat, blue shirt, steady posture, coordinates laboratory safety.
Scene environment: educational emergency response scene in a lab, clear evacuation path, barrier tape, emergency equipment, no graphic injury.
Required visual elements: small liquid spill, absorbent pad, tray boundary, contained spread; secondary tray, absorbent pad, container boundary preventing spread; potential exposure risk shown by distance, vapor, or an uncapped container, without injury; barrier tape, safe perimeter, clear risk boundary; phone or radio reporting gesture, screen blank, no readable UI.
Additional card context from the rules: knowledge: 泄漏处理先隔离，再判断是否可自行清理。.
Composition: vertical 2:3; person and experiment setup centered; layered foreground glassware; clean fume hood or window in background.
Extra production rule: This should look like a correct or nearly correct laboratory operation, not an accident scene. Preferred action cues: isolate, contain, report.
Color and material: pale blue, white, gray-blue, transparent glass, soft reflections on the lab bench, small amount of orange/yellow only for safety warning symbols or flame.
Border and crop: the image may include a thin rounded rectangle card border and warm off-white paper margin; keep all important subjects away from the edge.

Strict negative prompt: no readable Chinese text, no readable English text, no readable numbers, no logo, no watermark, no brand name, no school emblem, no UI text, no readable bottle labels, no readable notebook content, no readable clipboard content, no title, no card frame text. Labels, forms, badges and screens must be blank, blurred, or meaningless lines only. No photorealistic style, no 3D render, no chibi style, no horror style, no gore, no injured people, no large explosion, no chaotic disaster, no distorted face, no extra fingers, no missing hands, no duplicated faces, no cluttered composition.
```

### T16 Task card | 火源风险排查

```text
Create ONE vertical no-text illustration for a laboratory safety board-game card.

Reference style: use the uploaded sample images as the main style reference. Match their clean academic watercolor look, blue-white palette, soft natural window light, transparent glassware, delicate anime-inspired characters, realistic chemistry lab equipment, rounded card-frame feeling, and calm educational tone.

Card ID: T16
Card type: Task card
Chinese card name: 火源风险排查
Visual goal: Show a positive execution scene for the lab task "火源风险排查". The task objective is: 确认热源、电源和易燃物距离。
Main character: Lin Cheng; young Chinese female graduate student, short black bob hair, clear goggles, white lab coat, blue inner shirt, often holding a notebook, careful and detail-oriented.
Scene environment: educational emergency response scene in a lab, clear evacuation path, barrier tape, emergency equipment, no graphic injury.
Required visual elements: small controlled flame, heat source, flammable pictogram only, no explosion; turning off heat, power, or valve, clear switch action; heating mantle, hot plate, warm glassware, heat source control; barrier tape, safe perimeter, clear risk boundary; phone or radio reporting gesture, screen blank, no readable UI.
Additional card context from the rules: knowledge: 火源控制要先切断能量输入。.
Composition: vertical 2:3; person and experiment setup centered; layered foreground glassware; clean fume hood or window in background.
Extra production rule: This should look like a correct or nearly correct laboratory operation, not an accident scene. Preferred action cues: shutdown, isolate, report.
Color and material: pale blue, white, gray-blue, transparent glass, soft reflections on the lab bench, small amount of orange/yellow only for safety warning symbols or flame.
Border and crop: the image may include a thin rounded rectangle card border and warm off-white paper margin; keep all important subjects away from the edge.

Strict negative prompt: no readable Chinese text, no readable English text, no readable numbers, no logo, no watermark, no brand name, no school emblem, no UI text, no readable bottle labels, no readable notebook content, no readable clipboard content, no title, no card frame text. Labels, forms, badges and screens must be blank, blurred, or meaningless lines only. No photorealistic style, no 3D render, no chibi style, no horror style, no gore, no injured people, no large explosion, no chaotic disaster, no distorted face, no extra fingers, no missing hands, no duplicated faces, no cluttered composition.
```

### T17 Task card | 人员暴露初期处置

```text
Create ONE vertical no-text illustration for a laboratory safety board-game card.

Reference style: use the uploaded sample images as the main style reference. Match their clean academic watercolor look, blue-white palette, soft natural window light, transparent glassware, delicate anime-inspired characters, realistic chemistry lab equipment, rounded card-frame feeling, and calm educational tone.

Card ID: T17
Card type: Task card
Chinese card name: 人员暴露初期处置
Visual goal: Show a positive execution scene for the lab task "人员暴露初期处置". The task objective is: 识别接触、冲洗和上报需求。
Main character: Zhou Heng; young Chinese male graduate student, short black hair, clear goggles, white lab coat, blue inner shirt, blue nitrile gloves, skilled at hands-on experiments.
Scene environment: educational emergency response scene in a lab, clear evacuation path, barrier tape, emergency equipment, no graphic injury.
Required visual elements: potential exposure risk shown by distance, vapor, or an uncapped container, without injury; eyewash, safety shower, first aid box, emergency button as background shapes; acid/base bottle, splash control, secondary tray, simple hazard pictogram with no text; phone or radio reporting gesture, screen blank, no readable UI; guiding people away, setting a barrier, maintaining distance.
Additional card context from the rules: knowledge: 人员暴露优先处理人身安全。.
Composition: vertical 2:3; person and experiment setup centered; layered foreground glassware; clean fume hood or window in background.
Extra production rule: This should look like a correct or nearly correct laboratory operation, not an accident scene. Preferred action cues: emergency, report, evacuate.
Color and material: pale blue, white, gray-blue, transparent glass, soft reflections on the lab bench, small amount of orange/yellow only for safety warning symbols or flame.
Border and crop: the image may include a thin rounded rectangle card border and warm off-white paper margin; keep all important subjects away from the edge.

Strict negative prompt: no readable Chinese text, no readable English text, no readable numbers, no logo, no watermark, no brand name, no school emblem, no UI text, no readable bottle labels, no readable notebook content, no readable clipboard content, no title, no card frame text. Labels, forms, badges and screens must be blank, blurred, or meaningless lines only. No photorealistic style, no 3D render, no chibi style, no horror style, no gore, no injured people, no large explosion, no chaotic disaster, no distorted face, no extra fingers, no missing hands, no duplicated faces, no cluttered composition.
```

### T18 Task card | 异常情况复盘记录

```text
Create ONE vertical no-text illustration for a laboratory safety board-game card.

Reference style: use the uploaded sample images as the main style reference. Match their clean academic watercolor look, blue-white palette, soft natural window light, transparent glassware, delicate anime-inspired characters, realistic chemistry lab equipment, rounded card-frame feeling, and calm educational tone.

Card ID: T18
Card type: Task card
Chinese card name: 异常情况复盘记录
Visual goal: Show a positive execution scene for the lab task "异常情况复盘记录". The task objective is: 记录风险原因和后续改进措施。
Main character: Gu Ning; young Chinese female doctoral student, low ponytail or short hair, goggles, lab coat, calm posture, good at recording and verification.
Scene environment: general modern chemistry lab operation scene, clean bench, glassware, safety equipment, bright window light.
Required visual elements: open lab notebook, blank grid sheet, pen, inventory ledger with no readable characters; two lab members confirming a risk with calm gestures.
Additional card context from the rules: knowledge: 复盘记录能避免同类问题重复发生。.
Composition: vertical 2:3; person and experiment setup centered; layered foreground glassware; clean fume hood or window in background.
Extra production rule: This should look like a correct or nearly correct laboratory operation, not an accident scene. Preferred action cues: review, record, communicate.
Color and material: pale blue, white, gray-blue, transparent glass, soft reflections on the lab bench, small amount of orange/yellow only for safety warning symbols or flame.
Border and crop: the image may include a thin rounded rectangle card border and warm off-white paper margin; keep all important subjects away from the edge.

Strict negative prompt: no readable Chinese text, no readable English text, no readable numbers, no logo, no watermark, no brand name, no school emblem, no UI text, no readable bottle labels, no readable notebook content, no readable clipboard content, no title, no card frame text. Labels, forms, badges and screens must be blank, blurred, or meaningless lines only. No photorealistic style, no 3D render, no chibi style, no horror style, no gore, no injured people, no large explosion, no chaotic disaster, no distorted face, no extra fingers, no missing hands, no duplicated faces, no cluttered composition.
```

### A01 Action card | 补全 PPE

```text
Create ONE vertical no-text illustration for a laboratory safety board-game card.

Reference style: use the uploaded sample images as the main style reference. Match their clean academic watercolor look, blue-white palette, soft natural window light, transparent glassware, delicate anime-inspired characters, realistic chemistry lab equipment, rounded card-frame feeling, and calm educational tone.

Card ID: A01
Card type: Action card
Chinese card name: 补全 PPE
Visual goal: Show one clear safety action demonstration for "补全 PPE". The action purpose is: 补齐或更换护目镜、手套、实验服。
Main character: Gu Ning; young Chinese female doctoral student, low ponytail or short hair, goggles, lab coat, calm posture, good at recording and verification.
Scene environment: general modern chemistry lab operation scene, clean bench, glassware, safety equipment, bright window light.
Required visual elements: safety goggles, blue nitrile gloves, white lab coat, visible PPE checking or wearing action; changing gloves, goggles, or protective clothing.
Additional card context from the rules: limits: 不能替代应急处置。.
Composition: vertical 2:3; close-up or half-body action demonstration; hands and safety action very clear; background recognizable but not busy.
Extra production rule: Only one main action should dominate the image. Do not combine several unrelated safety events.
Color and material: pale blue, white, gray-blue, transparent glass, soft reflections on the lab bench, small amount of orange/yellow only for safety warning symbols or flame.
Border and crop: the image may include a thin rounded rectangle card border and warm off-white paper margin; keep all important subjects away from the edge.

Strict negative prompt: no readable Chinese text, no readable English text, no readable numbers, no logo, no watermark, no brand name, no school emblem, no UI text, no readable bottle labels, no readable notebook content, no readable clipboard content, no title, no card frame text. Labels, forms, badges and screens must be blank, blurred, or meaningless lines only. No photorealistic style, no 3D render, no chibi style, no horror style, no gore, no injured people, no large explosion, no chaotic disaster, no distorted face, no extra fingers, no missing hands, no duplicated faces, no cluttered composition.
```

### A02 Action card | 核对标签

```text
Create ONE vertical no-text illustration for a laboratory safety board-game card.

Reference style: use the uploaded sample images as the main style reference. Match their clean academic watercolor look, blue-white palette, soft natural window light, transparent glassware, delicate anime-inspired characters, realistic chemistry lab equipment, rounded card-frame feeling, and calm educational tone.

Card ID: A02
Card type: Action card
Chinese card name: 核对标签
Visual goal: Show one clear safety action demonstration for "核对标签". The action purpose is: 核对瓶签、临时标签和试剂身份。
Main character: Cheng Yan; mature Chinese male doctoral student or teaching assistant, white lab coat, blue shirt, steady posture, coordinates laboratory safety.
Scene environment: general modern chemistry lab operation scene, clean bench, glassware, safety equipment, bright window light.
Required visual elements: reagent bottle with blank or blurred label, absolutely no readable text; comparing bottle, blank notebook, and inventory sheet.
Additional card context from the rules: limits: 无法直接处理泄漏或火源。.
Composition: vertical 2:3; close-up or half-body action demonstration; hands and safety action very clear; background recognizable but not busy.
Extra production rule: Only one main action should dominate the image. Do not combine several unrelated safety events.
Color and material: pale blue, white, gray-blue, transparent glass, soft reflections on the lab bench, small amount of orange/yellow only for safety warning symbols or flame.
Border and crop: the image may include a thin rounded rectangle card border and warm off-white paper margin; keep all important subjects away from the edge.

Strict negative prompt: no readable Chinese text, no readable English text, no readable numbers, no logo, no watermark, no brand name, no school emblem, no UI text, no readable bottle labels, no readable notebook content, no readable clipboard content, no title, no card frame text. Labels, forms, badges and screens must be blank, blurred, or meaningless lines only. No photorealistic style, no 3D render, no chibi style, no horror style, no gore, no injured people, no large explosion, no chaotic disaster, no distorted face, no extra fingers, no missing hands, no duplicated faces, no cluttered composition.
```

### A03 Action card | 记录台账

```text
Create ONE vertical no-text illustration for a laboratory safety board-game card.

Reference style: use the uploaded sample images as the main style reference. Match their clean academic watercolor look, blue-white palette, soft natural window light, transparent glassware, delicate anime-inspired characters, realistic chemistry lab equipment, rounded card-frame feeling, and calm educational tone.

Card ID: A03
Card type: Action card
Chinese card name: 记录台账
Visual goal: Show one clear safety action demonstration for "记录台账". The action purpose is: 补全领用、操作和异常记录。
Main character: Lin Cheng; young Chinese female graduate student, short black bob hair, clear goggles, white lab coat, blue inner shirt, often holding a notebook, careful and detail-oriented.
Scene environment: general modern chemistry lab operation scene, clean bench, glassware, safety equipment, bright window light.
Required visual elements: open lab notebook, blank grid sheet, pen, inventory ledger with no readable characters.
Additional card context from the rules: limits: 记录不能代替现场控制。.
Composition: vertical 2:3; close-up or half-body action demonstration; hands and safety action very clear; background recognizable but not busy.
Extra production rule: Only one main action should dominate the image. Do not combine several unrelated safety events.
Color and material: pale blue, white, gray-blue, transparent glass, soft reflections on the lab bench, small amount of orange/yellow only for safety warning symbols or flame.
Border and crop: the image may include a thin rounded rectangle card border and warm off-white paper margin; keep all important subjects away from the edge.

Strict negative prompt: no readable Chinese text, no readable English text, no readable numbers, no logo, no watermark, no brand name, no school emblem, no UI text, no readable bottle labels, no readable notebook content, no readable clipboard content, no title, no card frame text. Labels, forms, badges and screens must be blank, blurred, or meaningless lines only. No photorealistic style, no 3D render, no chibi style, no horror style, no gore, no injured people, no large explosion, no chaotic disaster, no distorted face, no extra fingers, no missing hands, no duplicated faces, no cluttered composition.
```

### A04 Action card | 移入通风橱

```text
Create ONE vertical no-text illustration for a laboratory safety board-game card.

Reference style: use the uploaded sample images as the main style reference. Match their clean academic watercolor look, blue-white palette, soft natural window light, transparent glassware, delicate anime-inspired characters, realistic chemistry lab equipment, rounded card-frame feeling, and calm educational tone.

Card ID: A04
Card type: Action card
Chinese card name: 移入通风橱
Visual goal: Show one clear safety action demonstration for "移入通风橱". The action purpose is: 将挥发性或刺激性操作移入通风橱。
Main character: Zhou Heng; young Chinese male graduate student, short black hair, clear goggles, white lab coat, blue inner shirt, blue nitrile gloves, skilled at hands-on experiments.
Scene environment: active experiment area of a modern chemistry lab, fume hood, glassware, clamps, heating or transfer setup.
Required visual elements: fume hood, airflow arrows as simple graphic marks, operation moved toward the hood; potential exposure risk shown by distance, vapor, or an uncapped container, without injury.
Additional card context from the rules: limits: 不适用于已经失控的火情。.
Composition: vertical 2:3; close-up or half-body action demonstration; hands and safety action very clear; background recognizable but not busy.
Extra production rule: Only one main action should dominate the image. Do not combine several unrelated safety events.
Color and material: pale blue, white, gray-blue, transparent glass, soft reflections on the lab bench, small amount of orange/yellow only for safety warning symbols or flame.
Border and crop: the image may include a thin rounded rectangle card border and warm off-white paper margin; keep all important subjects away from the edge.

Strict negative prompt: no readable Chinese text, no readable English text, no readable numbers, no logo, no watermark, no brand name, no school emblem, no UI text, no readable bottle labels, no readable notebook content, no readable clipboard content, no title, no card frame text. Labels, forms, badges and screens must be blank, blurred, or meaningless lines only. No photorealistic style, no 3D render, no chibi style, no horror style, no gore, no injured people, no large explosion, no chaotic disaster, no distorted face, no extra fingers, no missing hands, no duplicated faces, no cluttered composition.
```

### A05 Action card | 分类回收

```text
Create ONE vertical no-text illustration for a laboratory safety board-game card.

Reference style: use the uploaded sample images as the main style reference. Match their clean academic watercolor look, blue-white palette, soft natural window light, transparent glassware, delicate anime-inspired characters, realistic chemistry lab equipment, rounded card-frame feeling, and calm educational tone.

Card ID: A05
Card type: Action card
Chinese card name: 分类回收
Visual goal: Show one clear safety action demonstration for "分类回收". The action purpose is: 按类别收集废液、锐器和污染物。
Main character: Gu Ning; young Chinese female doctoral student, low ponytail or short hair, goggles, lab coat, calm posture, good at recording and verification.
Scene environment: general modern chemistry lab operation scene, clean bench, glassware, safety equipment, bright window light.
Required visual elements: waste bottle, sorted waste container, cleanup action, blank label only; reagent bottle with blank or blurred label, absolutely no readable text.
Additional card context from the rules: limits: 未知废液需先确认。.
Composition: vertical 2:3; close-up or half-body action demonstration; hands and safety action very clear; background recognizable but not busy.
Extra production rule: Only one main action should dominate the image. Do not combine several unrelated safety events.
Color and material: pale blue, white, gray-blue, transparent glass, soft reflections on the lab bench, small amount of orange/yellow only for safety warning symbols or flame.
Border and crop: the image may include a thin rounded rectangle card border and warm off-white paper margin; keep all important subjects away from the edge.

Strict negative prompt: no readable Chinese text, no readable English text, no readable numbers, no logo, no watermark, no brand name, no school emblem, no UI text, no readable bottle labels, no readable notebook content, no readable clipboard content, no title, no card frame text. Labels, forms, badges and screens must be blank, blurred, or meaningless lines only. No photorealistic style, no 3D render, no chibi style, no horror style, no gore, no injured people, no large explosion, no chaotic disaster, no distorted face, no extra fingers, no missing hands, no duplicated faces, no cluttered composition.
```

### A06 Action card | 隔离现场

```text
Create ONE vertical no-text illustration for a laboratory safety board-game card.

Reference style: use the uploaded sample images as the main style reference. Match their clean academic watercolor look, blue-white palette, soft natural window light, transparent glassware, delicate anime-inspired characters, realistic chemistry lab equipment, rounded card-frame feeling, and calm educational tone.

Card ID: A06
Card type: Action card
Chinese card name: 隔离现场
Visual goal: Show one clear safety action demonstration for "隔离现场". The action purpose is: 限制人员接触风险区域。
Main character: Cheng Yan; mature Chinese male doctoral student or teaching assistant, white lab coat, blue shirt, steady posture, coordinates laboratory safety.
Scene environment: general modern chemistry lab operation scene, clean bench, glassware, safety equipment, bright window light.
Required visual elements: barrier tape, safe perimeter, clear risk boundary; person guarding a risk zone and stopping bystanders calmly.
Additional card context from the rules: limits: 隔离后仍需后续处置。.
Composition: vertical 2:3; close-up or half-body action demonstration; hands and safety action very clear; background recognizable but not busy.
Extra production rule: Only one main action should dominate the image. Do not combine several unrelated safety events.
Color and material: pale blue, white, gray-blue, transparent glass, soft reflections on the lab bench, small amount of orange/yellow only for safety warning symbols or flame.
Border and crop: the image may include a thin rounded rectangle card border and warm off-white paper margin; keep all important subjects away from the edge.

Strict negative prompt: no readable Chinese text, no readable English text, no readable numbers, no logo, no watermark, no brand name, no school emblem, no UI text, no readable bottle labels, no readable notebook content, no readable clipboard content, no title, no card frame text. Labels, forms, badges and screens must be blank, blurred, or meaningless lines only. No photorealistic style, no 3D render, no chibi style, no horror style, no gore, no injured people, no large explosion, no chaotic disaster, no distorted face, no extra fingers, no missing hands, no duplicated faces, no cluttered composition.
```

### A07 Action card | 使用应急设施

```text
Create ONE vertical no-text illustration for a laboratory safety board-game card.

Reference style: use the uploaded sample images as the main style reference. Match their clean academic watercolor look, blue-white palette, soft natural window light, transparent glassware, delicate anime-inspired characters, realistic chemistry lab equipment, rounded card-frame feeling, and calm educational tone.

Card ID: A07
Card type: Action card
Chinese card name: 使用应急设施
Visual goal: Show one clear safety action demonstration for "使用应急设施". The action purpose is: 使用洗眼器、喷淋或合适灭火器。
Main character: Lin Cheng; young Chinese female graduate student, short black bob hair, clear goggles, white lab coat, blue inner shirt, often holding a notebook, careful and detail-oriented.
Scene environment: educational emergency response scene in a lab, clear evacuation path, barrier tape, emergency equipment, no graphic injury.
Required visual elements: eyewash, safety shower, first aid box, emergency button as background shapes; potential exposure risk shown by distance, vapor, or an uncapped container, without injury.
Additional card context from the rules: limits: 必须匹配事件类型。.
Composition: vertical 2:3; close-up or half-body action demonstration; hands and safety action very clear; background recognizable but not busy.
Extra production rule: Only one main action should dominate the image. Do not combine several unrelated safety events.
Color and material: pale blue, white, gray-blue, transparent glass, soft reflections on the lab bench, small amount of orange/yellow only for safety warning symbols or flame.
Border and crop: the image may include a thin rounded rectangle card border and warm off-white paper margin; keep all important subjects away from the edge.

Strict negative prompt: no readable Chinese text, no readable English text, no readable numbers, no logo, no watermark, no brand name, no school emblem, no UI text, no readable bottle labels, no readable notebook content, no readable clipboard content, no title, no card frame text. Labels, forms, badges and screens must be blank, blurred, or meaningless lines only. No photorealistic style, no 3D render, no chibi style, no horror style, no gore, no injured people, no large explosion, no chaotic disaster, no distorted face, no extra fingers, no missing hands, no duplicated faces, no cluttered composition.
```

### A08 Action card | 撤离与警戒

```text
Create ONE vertical no-text illustration for a laboratory safety board-game card.

Reference style: use the uploaded sample images as the main style reference. Match their clean academic watercolor look, blue-white palette, soft natural window light, transparent glassware, delicate anime-inspired characters, realistic chemistry lab equipment, rounded card-frame feeling, and calm educational tone.

Card ID: A08
Card type: Action card
Chinese card name: 撤离与警戒
Visual goal: Show one clear safety action demonstration for "撤离与警戒". The action purpose is: 撤离无关人员并设置警戒。
Main character: Zhou Heng; young Chinese male graduate student, short black hair, clear goggles, white lab coat, blue inner shirt, blue nitrile gloves, skilled at hands-on experiments.
Scene environment: educational emergency response scene in a lab, clear evacuation path, barrier tape, emergency equipment, no graphic injury.
Required visual elements: guiding people away, setting a barrier, maintaining distance; person guarding a risk zone and stopping bystanders calmly.
Additional card context from the rules: limits: 不能单独推进任务。.
Composition: vertical 2:3; close-up or half-body action demonstration; hands and safety action very clear; background recognizable but not busy.
Extra production rule: Only one main action should dominate the image. Do not combine several unrelated safety events.
Color and material: pale blue, white, gray-blue, transparent glass, soft reflections on the lab bench, small amount of orange/yellow only for safety warning symbols or flame.
Border and crop: the image may include a thin rounded rectangle card border and warm off-white paper margin; keep all important subjects away from the edge.

Strict negative prompt: no readable Chinese text, no readable English text, no readable numbers, no logo, no watermark, no brand name, no school emblem, no UI text, no readable bottle labels, no readable notebook content, no readable clipboard content, no title, no card frame text. Labels, forms, badges and screens must be blank, blurred, or meaningless lines only. No photorealistic style, no 3D render, no chibi style, no horror style, no gore, no injured people, no large explosion, no chaotic disaster, no distorted face, no extra fingers, no missing hands, no duplicated faces, no cluttered composition.
```

### A09 Action card | 上报负责人

```text
Create ONE vertical no-text illustration for a laboratory safety board-game card.

Reference style: use the uploaded sample images as the main style reference. Match their clean academic watercolor look, blue-white palette, soft natural window light, transparent glassware, delicate anime-inspired characters, realistic chemistry lab equipment, rounded card-frame feeling, and calm educational tone.

Card ID: A09
Card type: Action card
Chinese card name: 上报负责人
Visual goal: Show one clear safety action demonstration for "上报负责人". The action purpose is: 联系导师、管理员或安全负责人。
Main character: Gu Ning; young Chinese female doctoral student, low ponytail or short hair, goggles, lab coat, calm posture, good at recording and verification.
Scene environment: general modern chemistry lab operation scene, clean bench, glassware, safety equipment, bright window light.
Required visual elements: phone or radio reporting gesture, screen blank, no readable UI; two lab members confirming a risk with calm gestures.
Additional card context from the rules: limits: 低危事件中过度上报会拖慢进度。.
Composition: vertical 2:3; close-up or half-body action demonstration; hands and safety action very clear; background recognizable but not busy.
Extra production rule: Only one main action should dominate the image. Do not combine several unrelated safety events.
Color and material: pale blue, white, gray-blue, transparent glass, soft reflections on the lab bench, small amount of orange/yellow only for safety warning symbols or flame.
Border and crop: the image may include a thin rounded rectangle card border and warm off-white paper margin; keep all important subjects away from the edge.

Strict negative prompt: no readable Chinese text, no readable English text, no readable numbers, no logo, no watermark, no brand name, no school emblem, no UI text, no readable bottle labels, no readable notebook content, no readable clipboard content, no title, no card frame text. Labels, forms, badges and screens must be blank, blurred, or meaningless lines only. No photorealistic style, no 3D render, no chibi style, no horror style, no gore, no injured people, no large explosion, no chaotic disaster, no distorted face, no extra fingers, no missing hands, no duplicated faces, no cluttered composition.
```

### A10 Action card | 切断热源电源

```text
Create ONE vertical no-text illustration for a laboratory safety board-game card.

Reference style: use the uploaded sample images as the main style reference. Match their clean academic watercolor look, blue-white palette, soft natural window light, transparent glassware, delicate anime-inspired characters, realistic chemistry lab equipment, rounded card-frame feeling, and calm educational tone.

Card ID: A10
Card type: Action card
Chinese card name: 切断热源电源
Visual goal: Show one clear safety action demonstration for "切断热源电源". The action purpose is: 停止加热、断电或关闭设备。
Main character: Cheng Yan; mature Chinese male doctoral student or teaching assistant, white lab coat, blue shirt, steady posture, coordinates laboratory safety.
Scene environment: active experiment area of a modern chemistry lab, fume hood, glassware, clamps, heating or transfer setup.
Required visual elements: turning off heat, power, or valve, clear switch action; heating mantle, hot plate, warm glassware, heat source control.
Additional card context from the rules: limits: 不等同于完成清理。.
Composition: vertical 2:3; close-up or half-body action demonstration; hands and safety action very clear; background recognizable but not busy.
Extra production rule: Only one main action should dominate the image. Do not combine several unrelated safety events.
Color and material: pale blue, white, gray-blue, transparent glass, soft reflections on the lab bench, small amount of orange/yellow only for safety warning symbols or flame.
Border and crop: the image may include a thin rounded rectangle card border and warm off-white paper margin; keep all important subjects away from the edge.

Strict negative prompt: no readable Chinese text, no readable English text, no readable numbers, no logo, no watermark, no brand name, no school emblem, no UI text, no readable bottle labels, no readable notebook content, no readable clipboard content, no title, no card frame text. Labels, forms, badges and screens must be blank, blurred, or meaningless lines only. No photorealistic style, no 3D render, no chibi style, no horror style, no gore, no injured people, no large explosion, no chaotic disaster, no distorted face, no extra fingers, no missing hands, no duplicated faces, no cluttered composition.
```

### A11 Action card | 检查并更换器材

```text
Create ONE vertical no-text illustration for a laboratory safety board-game card.

Reference style: use the uploaded sample images as the main style reference. Match their clean academic watercolor look, blue-white palette, soft natural window light, transparent glassware, delicate anime-inspired characters, realistic chemistry lab equipment, rounded card-frame feeling, and calm educational tone.

Card ID: A11
Card type: Action card
Chinese card name: 检查并更换器材
Visual goal: Show one clear safety action demonstration for "检查并更换器材". The action purpose is: 检查裂纹、夹具、耗材和设备状态。
Main character: Lin Cheng; young Chinese female graduate student, short black bob hair, clear goggles, white lab coat, blue inner shirt, often holding a notebook, careful and detail-oriented.
Scene environment: general modern chemistry lab operation scene, clean bench, glassware, safety equipment, bright window light.
Required visual elements: checking clamps, valves, labels, airflow, or equipment connections; changing gloves, goggles, or protective clothing.
Additional card context from the rules: limits: 不能处理人员暴露。.
Composition: vertical 2:3; close-up or half-body action demonstration; hands and safety action very clear; background recognizable but not busy.
Extra production rule: Only one main action should dominate the image. Do not combine several unrelated safety events.
Color and material: pale blue, white, gray-blue, transparent glass, soft reflections on the lab bench, small amount of orange/yellow only for safety warning symbols or flame.
Border and crop: the image may include a thin rounded rectangle card border and warm off-white paper margin; keep all important subjects away from the edge.

Strict negative prompt: no readable Chinese text, no readable English text, no readable numbers, no logo, no watermark, no brand name, no school emblem, no UI text, no readable bottle labels, no readable notebook content, no readable clipboard content, no title, no card frame text. Labels, forms, badges and screens must be blank, blurred, or meaningless lines only. No photorealistic style, no 3D render, no chibi style, no horror style, no gore, no injured people, no large explosion, no chaotic disaster, no distorted face, no extra fingers, no missing hands, no duplicated faces, no cluttered composition.
```

### A12 Action card | 固定与规范连接

```text
Create ONE vertical no-text illustration for a laboratory safety board-game card.

Reference style: use the uploaded sample images as the main style reference. Match their clean academic watercolor look, blue-white palette, soft natural window light, transparent glassware, delicate anime-inspired characters, realistic chemistry lab equipment, rounded card-frame feeling, and calm educational tone.

Card ID: A12
Card type: Action card
Chinese card name: 固定与规范连接
Visual goal: Show one clear safety action demonstration for "固定与规范连接". The action purpose is: 固定气瓶、夹具、冷凝管和收集瓶。
Main character: Zhou Heng; young Chinese male graduate student, short black hair, clear goggles, white lab coat, blue inner shirt, blue nitrile gloves, skilled at hands-on experiments.
Scene environment: preparation area of a modern chemistry lab, clean bench, reagent shelves, inventory notebook, PPE on the table.
Required visual elements: tightening clamp, stabilizing stand, securing tubing or vessel; clamps, stands, condenser, heating mantle, instrument panel, physically plausible equipment.
Additional card context from the rules: limits: 不能代替检漏和记录。.
Composition: vertical 2:3; close-up or half-body action demonstration; hands and safety action very clear; background recognizable but not busy.
Extra production rule: Only one main action should dominate the image. Do not combine several unrelated safety events.
Color and material: pale blue, white, gray-blue, transparent glass, soft reflections on the lab bench, small amount of orange/yellow only for safety warning symbols or flame.
Border and crop: the image may include a thin rounded rectangle card border and warm off-white paper margin; keep all important subjects away from the edge.

Strict negative prompt: no readable Chinese text, no readable English text, no readable numbers, no logo, no watermark, no brand name, no school emblem, no UI text, no readable bottle labels, no readable notebook content, no readable clipboard content, no title, no card frame text. Labels, forms, badges and screens must be blank, blurred, or meaningless lines only. No photorealistic style, no 3D render, no chibi style, no horror style, no gore, no injured people, no large explosion, no chaotic disaster, no distorted face, no extra fingers, no missing hands, no duplicated faces, no cluttered composition.
```

### A13 Action card | 围堵泄漏

```text
Create ONE vertical no-text illustration for a laboratory safety board-game card.

Reference style: use the uploaded sample images as the main style reference. Match their clean academic watercolor look, blue-white palette, soft natural window light, transparent glassware, delicate anime-inspired characters, realistic chemistry lab equipment, rounded card-frame feeling, and calm educational tone.

Card ID: A13
Card type: Action card
Chinese card name: 围堵泄漏
Visual goal: Show one clear safety action demonstration for "围堵泄漏". The action purpose is: 用合适材料限制液体扩散。
Main character: Gu Ning; young Chinese female doctoral student, low ponytail or short hair, goggles, lab coat, calm posture, good at recording and verification.
Scene environment: educational emergency response scene in a lab, clear evacuation path, barrier tape, emergency equipment, no graphic injury.
Required visual elements: secondary tray, absorbent pad, container boundary preventing spread; small liquid spill, absorbent pad, tray boundary, contained spread.
Additional card context from the rules: limits: 未知物质需先隔离上报。.
Composition: vertical 2:3; close-up or half-body action demonstration; hands and safety action very clear; background recognizable but not busy.
Extra production rule: Only one main action should dominate the image. Do not combine several unrelated safety events.
Color and material: pale blue, white, gray-blue, transparent glass, soft reflections on the lab bench, small amount of orange/yellow only for safety warning symbols or flame.
Border and crop: the image may include a thin rounded rectangle card border and warm off-white paper margin; keep all important subjects away from the edge.

Strict negative prompt: no readable Chinese text, no readable English text, no readable numbers, no logo, no watermark, no brand name, no school emblem, no UI text, no readable bottle labels, no readable notebook content, no readable clipboard content, no title, no card frame text. Labels, forms, badges and screens must be blank, blurred, or meaningless lines only. No photorealistic style, no 3D render, no chibi style, no horror style, no gore, no injured people, no large explosion, no chaotic disaster, no distorted face, no extra fingers, no missing hands, no duplicated faces, no cluttered composition.
```

### A14 Action card | 降温与稳定

```text
Create ONE vertical no-text illustration for a laboratory safety board-game card.

Reference style: use the uploaded sample images as the main style reference. Match their clean academic watercolor look, blue-white palette, soft natural window light, transparent glassware, delicate anime-inspired characters, realistic chemistry lab equipment, rounded card-frame feeling, and calm educational tone.

Card ID: A14
Card type: Action card
Chinese card name: 降温与稳定
Visual goal: Show one clear safety action demonstration for "降温与稳定". The action purpose is: 降低温度并稳定反应体系。
Main character: Cheng Yan; mature Chinese male doctoral student or teaching assistant, white lab coat, blue shirt, steady posture, coordinates laboratory safety.
Scene environment: active experiment area of a modern chemistry lab, fume hood, glassware, clamps, heating or transfer setup.
Required visual elements: cooling water hose, ice bath, condenser, cooling control.
Additional card context from the rules: limits: 压力异常时不可贸然打开体系。.
Composition: vertical 2:3; close-up or half-body action demonstration; hands and safety action very clear; background recognizable but not busy.
Extra production rule: Only one main action should dominate the image. Do not combine several unrelated safety events.
Color and material: pale blue, white, gray-blue, transparent glass, soft reflections on the lab bench, small amount of orange/yellow only for safety warning symbols or flame.
Border and crop: the image may include a thin rounded rectangle card border and warm off-white paper margin; keep all important subjects away from the edge.

Strict negative prompt: no readable Chinese text, no readable English text, no readable numbers, no logo, no watermark, no brand name, no school emblem, no UI text, no readable bottle labels, no readable notebook content, no readable clipboard content, no title, no card frame text. Labels, forms, badges and screens must be blank, blurred, or meaningless lines only. No photorealistic style, no 3D render, no chibi style, no horror style, no gore, no injured people, no large explosion, no chaotic disaster, no distorted face, no extra fingers, no missing hands, no duplicated faces, no cluttered composition.
```

### A15 Action card | 中和处理

```text
Create ONE vertical no-text illustration for a laboratory safety board-game card.

Reference style: use the uploaded sample images as the main style reference. Match their clean academic watercolor look, blue-white palette, soft natural window light, transparent glassware, delicate anime-inspired characters, realistic chemistry lab equipment, rounded card-frame feeling, and calm educational tone.

Card ID: A15
Card type: Action card
Chinese card name: 中和处理
Visual goal: Show one clear safety action demonstration for "中和处理". The action purpose is: 在确认条件下进行酸碱中和。
Main character: Lin Cheng; young Chinese female graduate student, short black bob hair, clear goggles, white lab coat, blue inner shirt, often holding a notebook, careful and detail-oriented.
Scene environment: educational emergency response scene in a lab, clear evacuation path, barrier tape, emergency equipment, no graphic injury.
Required visual elements: careful acid/base containment or absorbent material, no violent reaction; acid/base bottle, splash control, secondary tray, simple hazard pictogram with no text.
Additional card context from the rules: limits: 人员接触时先冲洗，不先中和皮肤。.
Composition: vertical 2:3; close-up or half-body action demonstration; hands and safety action very clear; background recognizable but not busy.
Extra production rule: Only one main action should dominate the image. Do not combine several unrelated safety events.
Color and material: pale blue, white, gray-blue, transparent glass, soft reflections on the lab bench, small amount of orange/yellow only for safety warning symbols or flame.
Border and crop: the image may include a thin rounded rectangle card border and warm off-white paper margin; keep all important subjects away from the edge.

Strict negative prompt: no readable Chinese text, no readable English text, no readable numbers, no logo, no watermark, no brand name, no school emblem, no UI text, no readable bottle labels, no readable notebook content, no readable clipboard content, no title, no card frame text. Labels, forms, badges and screens must be blank, blurred, or meaningless lines only. No photorealistic style, no 3D render, no chibi style, no horror style, no gore, no injured people, no large explosion, no chaotic disaster, no distorted face, no extra fingers, no missing hands, no duplicated faces, no cluttered composition.
```

### A16 Action card | 清洁去污

```text
Create ONE vertical no-text illustration for a laboratory safety board-game card.

Reference style: use the uploaded sample images as the main style reference. Match their clean academic watercolor look, blue-white palette, soft natural window light, transparent glassware, delicate anime-inspired characters, realistic chemistry lab equipment, rounded card-frame feeling, and calm educational tone.

Card ID: A16
Card type: Action card
Chinese card name: 清洁去污
Visual goal: Show one clear safety action demonstration for "清洁去污". The action purpose is: 清理污染台面和公共区域。
Main character: Zhou Heng; young Chinese male graduate student, short black hair, clear goggles, white lab coat, blue inner shirt, blue nitrile gloves, skilled at hands-on experiments.
Scene environment: general modern chemistry lab operation scene, clean bench, glassware, safety equipment, bright window light.
Required visual elements: tidy bench, wiping action, cleaning tools, organized glassware; two containers or pipettes too close, cross-contamination risk.
Additional card context from the rules: limits: 不适用于未知粉末直接清扫。.
Composition: vertical 2:3; close-up or half-body action demonstration; hands and safety action very clear; background recognizable but not busy.
Extra production rule: Only one main action should dominate the image. Do not combine several unrelated safety events.
Color and material: pale blue, white, gray-blue, transparent glass, soft reflections on the lab bench, small amount of orange/yellow only for safety warning symbols or flame.
Border and crop: the image may include a thin rounded rectangle card border and warm off-white paper margin; keep all important subjects away from the edge.

Strict negative prompt: no readable Chinese text, no readable English text, no readable numbers, no logo, no watermark, no brand name, no school emblem, no UI text, no readable bottle labels, no readable notebook content, no readable clipboard content, no title, no card frame text. Labels, forms, badges and screens must be blank, blurred, or meaningless lines only. No photorealistic style, no 3D render, no chibi style, no horror style, no gore, no injured people, no large explosion, no chaotic disaster, no distorted face, no extra fingers, no missing hands, no duplicated faces, no cluttered composition.
```

### A17 Action card | 持续监测

```text
Create ONE vertical no-text illustration for a laboratory safety board-game card.

Reference style: use the uploaded sample images as the main style reference. Match their clean academic watercolor look, blue-white palette, soft natural window light, transparent glassware, delicate anime-inspired characters, realistic chemistry lab equipment, rounded card-frame feeling, and calm educational tone.

Card ID: A17
Card type: Action card
Chinese card name: 持续监测
Visual goal: Show one clear safety action demonstration for "持续监测". The action purpose is: 监测温度、压力、气味和设备状态。
Main character: Gu Ning; young Chinese female doctoral student, low ponytail or short hair, goggles, lab coat, calm posture, good at recording and verification.
Scene environment: active experiment area of a modern chemistry lab, fume hood, glassware, clamps, heating or transfer setup.
Required visual elements: open lab notebook, blank grid sheet, pen, inventory ledger with no readable characters.
Additional card context from the rules: limits: 发现异常后仍需处置。.
Composition: vertical 2:3; close-up or half-body action demonstration; hands and safety action very clear; background recognizable but not busy.
Extra production rule: Only one main action should dominate the image. Do not combine several unrelated safety events.
Color and material: pale blue, white, gray-blue, transparent glass, soft reflections on the lab bench, small amount of orange/yellow only for safety warning symbols or flame.
Border and crop: the image may include a thin rounded rectangle card border and warm off-white paper margin; keep all important subjects away from the edge.

Strict negative prompt: no readable Chinese text, no readable English text, no readable numbers, no logo, no watermark, no brand name, no school emblem, no UI text, no readable bottle labels, no readable notebook content, no readable clipboard content, no title, no card frame text. Labels, forms, badges and screens must be blank, blurred, or meaningless lines only. No photorealistic style, no 3D render, no chibi style, no horror style, no gore, no injured people, no large explosion, no chaotic disaster, no distorted face, no extra fingers, no missing hands, no duplicated faces, no cluttered composition.
```

### A18 Action card | 暂停操作

```text
Create ONE vertical no-text illustration for a laboratory safety board-game card.

Reference style: use the uploaded sample images as the main style reference. Match their clean academic watercolor look, blue-white palette, soft natural window light, transparent glassware, delicate anime-inspired characters, realistic chemistry lab equipment, rounded card-frame feeling, and calm educational tone.

Card ID: A18
Card type: Action card
Chinese card name: 暂停操作
Visual goal: Show one clear safety action demonstration for "暂停操作". The action purpose is: 暂停当前步骤，避免风险继续扩大。
Main character: Cheng Yan; mature Chinese male doctoral student or teaching assistant, white lab coat, blue shirt, steady posture, coordinates laboratory safety.
Scene environment: general modern chemistry lab operation scene, clean bench, glassware, safety equipment, bright window light.
Required visual elements: two lab members confirming a risk with calm gestures.
Additional card context from the rules: limits: 暂停不是最终处置。.
Composition: vertical 2:3; close-up or half-body action demonstration; hands and safety action very clear; background recognizable but not busy.
Extra production rule: Only one main action should dominate the image. Do not combine several unrelated safety events.
Color and material: pale blue, white, gray-blue, transparent glass, soft reflections on the lab bench, small amount of orange/yellow only for safety warning symbols or flame.
Border and crop: the image may include a thin rounded rectangle card border and warm off-white paper margin; keep all important subjects away from the edge.

Strict negative prompt: no readable Chinese text, no readable English text, no readable numbers, no logo, no watermark, no brand name, no school emblem, no UI text, no readable bottle labels, no readable notebook content, no readable clipboard content, no title, no card frame text. Labels, forms, badges and screens must be blank, blurred, or meaningless lines only. No photorealistic style, no 3D render, no chibi style, no horror style, no gore, no injured people, no large explosion, no chaotic disaster, no distorted face, no extra fingers, no missing hands, no duplicated faces, no cluttered composition.
```

### A19 Action card | 确认相容性

```text
Create ONE vertical no-text illustration for a laboratory safety board-game card.

Reference style: use the uploaded sample images as the main style reference. Match their clean academic watercolor look, blue-white palette, soft natural window light, transparent glassware, delicate anime-inspired characters, realistic chemistry lab equipment, rounded card-frame feeling, and calm educational tone.

Card ID: A19
Card type: Action card
Chinese card name: 确认相容性
Visual goal: Show one clear safety action demonstration for "确认相容性". The action purpose is: 确认试剂、废液和储存相容性。
Main character: Lin Cheng; young Chinese female graduate student, short black bob hair, clear goggles, white lab coat, blue inner shirt, often holding a notebook, careful and detail-oriented.
Scene environment: preparation area of a modern chemistry lab, clean bench, reagent shelves, inventory notebook, PPE on the table.
Required visual elements: comparing bottle, blank notebook, and inventory sheet; reagent bottle with blank or blurred label, absolutely no readable text.
Additional card context from the rules: limits: 需要配合标签或记录。.
Composition: vertical 2:3; close-up or half-body action demonstration; hands and safety action very clear; background recognizable but not busy.
Extra production rule: Only one main action should dominate the image. Do not combine several unrelated safety events.
Color and material: pale blue, white, gray-blue, transparent glass, soft reflections on the lab bench, small amount of orange/yellow only for safety warning symbols or flame.
Border and crop: the image may include a thin rounded rectangle card border and warm off-white paper margin; keep all important subjects away from the edge.

Strict negative prompt: no readable Chinese text, no readable English text, no readable numbers, no logo, no watermark, no brand name, no school emblem, no UI text, no readable bottle labels, no readable notebook content, no readable clipboard content, no title, no card frame text. Labels, forms, badges and screens must be blank, blurred, or meaningless lines only. No photorealistic style, no 3D render, no chibi style, no horror style, no gore, no injured people, no large explosion, no chaotic disaster, no distorted face, no extra fingers, no missing hands, no duplicated faces, no cluttered composition.
```

### A20 Action card | 沟通交接

```text
Create ONE vertical no-text illustration for a laboratory safety board-game card.

Reference style: use the uploaded sample images as the main style reference. Match their clean academic watercolor look, blue-white palette, soft natural window light, transparent glassware, delicate anime-inspired characters, realistic chemistry lab equipment, rounded card-frame feeling, and calm educational tone.

Card ID: A20
Card type: Action card
Chinese card name: 沟通交接
Visual goal: Show one clear safety action demonstration for "沟通交接". The action purpose is: 向下一岗位说明遗留风险和处理状态。
Main character: Zhou Heng; young Chinese male graduate student, short black hair, clear goggles, white lab coat, blue inner shirt, blue nitrile gloves, skilled at hands-on experiments.
Scene environment: general modern chemistry lab operation scene, clean bench, glassware, safety equipment, bright window light.
Required visual elements: two lab members confirming a risk with calm gestures.
Additional card context from the rules: limits: 不能替代实际控制。.
Composition: vertical 2:3; close-up or half-body action demonstration; hands and safety action very clear; background recognizable but not busy.
Extra production rule: Only one main action should dominate the image. Do not combine several unrelated safety events.
Color and material: pale blue, white, gray-blue, transparent glass, soft reflections on the lab bench, small amount of orange/yellow only for safety warning symbols or flame.
Border and crop: the image may include a thin rounded rectangle card border and warm off-white paper margin; keep all important subjects away from the edge.

Strict negative prompt: no readable Chinese text, no readable English text, no readable numbers, no logo, no watermark, no brand name, no school emblem, no UI text, no readable bottle labels, no readable notebook content, no readable clipboard content, no title, no card frame text. Labels, forms, badges and screens must be blank, blurred, or meaningless lines only. No photorealistic style, no 3D render, no chibi style, no horror style, no gore, no injured people, no large explosion, no chaotic disaster, no distorted face, no extra fingers, no missing hands, no duplicated faces, no cluttered composition.
```

### A21 Action card | 资源调度

```text
Create ONE vertical no-text illustration for a laboratory safety board-game card.

Reference style: use the uploaded sample images as the main style reference. Match their clean academic watercolor look, blue-white palette, soft natural window light, transparent glassware, delicate anime-inspired characters, realistic chemistry lab equipment, rounded card-frame feeling, and calm educational tone.

Card ID: A21
Card type: Action card
Chinese card name: 资源调度
Visual goal: Show one clear safety action demonstration for "资源调度". The action purpose is: 调整公共手牌和可用工具。
Main character: Gu Ning; young Chinese female doctoral student, low ponytail or short hair, goggles, lab coat, calm posture, good at recording and verification.
Scene environment: general modern chemistry lab operation scene, clean bench, glassware, safety equipment, bright window light.
Required visual elements: clean modern chemistry laboratory bench, glassware, safety equipment, bright natural light.
Additional card context from the rules: limits: 不能直接解决事件。.
Composition: vertical 2:3; close-up or half-body action demonstration; hands and safety action very clear; background recognizable but not busy.
Extra production rule: Only one main action should dominate the image. Do not combine several unrelated safety events.
Color and material: pale blue, white, gray-blue, transparent glass, soft reflections on the lab bench, small amount of orange/yellow only for safety warning symbols or flame.
Border and crop: the image may include a thin rounded rectangle card border and warm off-white paper margin; keep all important subjects away from the edge.

Strict negative prompt: no readable Chinese text, no readable English text, no readable numbers, no logo, no watermark, no brand name, no school emblem, no UI text, no readable bottle labels, no readable notebook content, no readable clipboard content, no title, no card frame text. Labels, forms, badges and screens must be blank, blurred, or meaningless lines only. No photorealistic style, no 3D render, no chibi style, no horror style, no gore, no injured people, no large explosion, no chaotic disaster, no distorted face, no extra fingers, no missing hands, no duplicated faces, no cluttered composition.
```

### A22 Action card | 复盘原因

```text
Create ONE vertical no-text illustration for a laboratory safety board-game card.

Reference style: use the uploaded sample images as the main style reference. Match their clean academic watercolor look, blue-white palette, soft natural window light, transparent glassware, delicate anime-inspired characters, realistic chemistry lab equipment, rounded card-frame feeling, and calm educational tone.

Card ID: A22
Card type: Action card
Chinese card name: 复盘原因
Visual goal: Show one clear safety action demonstration for "复盘原因". The action purpose is: 梳理风险原因和改进措施。
Main character: Cheng Yan; mature Chinese male doctoral student or teaching assistant, white lab coat, blue shirt, steady posture, coordinates laboratory safety.
Scene environment: general modern chemistry lab operation scene, clean bench, glassware, safety equipment, bright window light.
Required visual elements: open lab notebook, blank grid sheet, pen, inventory ledger with no readable characters.
Additional card context from the rules: limits: 通常在风险受控后使用。.
Composition: vertical 2:3; close-up or half-body action demonstration; hands and safety action very clear; background recognizable but not busy.
Extra production rule: Only one main action should dominate the image. Do not combine several unrelated safety events.
Color and material: pale blue, white, gray-blue, transparent glass, soft reflections on the lab bench, small amount of orange/yellow only for safety warning symbols or flame.
Border and crop: the image may include a thin rounded rectangle card border and warm off-white paper margin; keep all important subjects away from the edge.

Strict negative prompt: no readable Chinese text, no readable English text, no readable numbers, no logo, no watermark, no brand name, no school emblem, no UI text, no readable bottle labels, no readable notebook content, no readable clipboard content, no title, no card frame text. Labels, forms, badges and screens must be blank, blurred, or meaningless lines only. No photorealistic style, no 3D render, no chibi style, no horror style, no gore, no injured people, no large explosion, no chaotic disaster, no distorted face, no extra fingers, no missing hands, no duplicated faces, no cluttered composition.
```

### A23 Action card | 设置警戒标识

```text
Create ONE vertical no-text illustration for a laboratory safety board-game card.

Reference style: use the uploaded sample images as the main style reference. Match their clean academic watercolor look, blue-white palette, soft natural window light, transparent glassware, delicate anime-inspired characters, realistic chemistry lab equipment, rounded card-frame feeling, and calm educational tone.

Card ID: A23
Card type: Action card
Chinese card name: 设置警戒标识
Visual goal: Show one clear safety action demonstration for "设置警戒标识". The action purpose is: 标出风险区域和不可触碰对象。
Main character: Lin Cheng; young Chinese female graduate student, short black bob hair, clear goggles, white lab coat, blue inner shirt, often holding a notebook, careful and detail-oriented.
Scene environment: educational emergency response scene in a lab, clear evacuation path, barrier tape, emergency equipment, no graphic injury.
Required visual elements: person guarding a risk zone and stopping bystanders calmly; barrier tape, safe perimeter, clear risk boundary.
Additional card context from the rules: limits: 需要后续处置。.
Composition: vertical 2:3; close-up or half-body action demonstration; hands and safety action very clear; background recognizable but not busy.
Extra production rule: Only one main action should dominate the image. Do not combine several unrelated safety events.
Color and material: pale blue, white, gray-blue, transparent glass, soft reflections on the lab bench, small amount of orange/yellow only for safety warning symbols or flame.
Border and crop: the image may include a thin rounded rectangle card border and warm off-white paper margin; keep all important subjects away from the edge.

Strict negative prompt: no readable Chinese text, no readable English text, no readable numbers, no logo, no watermark, no brand name, no school emblem, no UI text, no readable bottle labels, no readable notebook content, no readable clipboard content, no title, no card frame text. Labels, forms, badges and screens must be blank, blurred, or meaningless lines only. No photorealistic style, no 3D render, no chibi style, no horror style, no gore, no injured people, no large explosion, no chaotic disaster, no distorted face, no extra fingers, no missing hands, no duplicated faces, no cluttered composition.
```

### A24 Action card | 替换耗材

```text
Create ONE vertical no-text illustration for a laboratory safety board-game card.

Reference style: use the uploaded sample images as the main style reference. Match their clean academic watercolor look, blue-white palette, soft natural window light, transparent glassware, delicate anime-inspired characters, realistic chemistry lab equipment, rounded card-frame feeling, and calm educational tone.

Card ID: A24
Card type: Action card
Chinese card name: 替换耗材
Visual goal: Show one clear safety action demonstration for "替换耗材". The action purpose is: 替换污染、破损或不合适耗材。
Main character: Zhou Heng; young Chinese male graduate student, short black hair, clear goggles, white lab coat, blue inner shirt, blue nitrile gloves, skilled at hands-on experiments.
Scene environment: general modern chemistry lab operation scene, clean bench, glassware, safety equipment, bright window light.
Required visual elements: changing gloves, goggles, or protective clothing; checking clamps, valves, labels, airflow, or equipment connections.
Additional card context from the rules: limits: 不能单独确认化学品身份。.
Composition: vertical 2:3; close-up or half-body action demonstration; hands and safety action very clear; background recognizable but not busy.
Extra production rule: Only one main action should dominate the image. Do not combine several unrelated safety events.
Color and material: pale blue, white, gray-blue, transparent glass, soft reflections on the lab bench, small amount of orange/yellow only for safety warning symbols or flame.
Border and crop: the image may include a thin rounded rectangle card border and warm off-white paper margin; keep all important subjects away from the edge.

Strict negative prompt: no readable Chinese text, no readable English text, no readable numbers, no logo, no watermark, no brand name, no school emblem, no UI text, no readable bottle labels, no readable notebook content, no readable clipboard content, no title, no card frame text. Labels, forms, badges and screens must be blank, blurred, or meaningless lines only. No photorealistic style, no 3D render, no chibi style, no horror style, no gore, no injured people, no large explosion, no chaotic disaster, no distorted face, no extra fingers, no missing hands, no duplicated faces, no cluttered composition.
```

### R01 Role card | 新入组本科生

```text
Create ONE vertical no-text illustration for a laboratory safety board-game card.

Reference style: use the uploaded sample images as the main style reference. Match their clean academic watercolor look, blue-white palette, soft natural window light, transparent glassware, delicate anime-inspired characters, realistic chemistry lab equipment, rounded card-frame feeling, and calm educational tone.

Card ID: R01
Card type: Role card
Chinese card name: 新入组本科生
Visual goal: Show a character portrait for the role "新入组本科生". Role concept: 学习能力强，但需要岗位支持。. Communicate the ability through pose and props, not text.
Main character: New student; young Chinese undergraduate student, careful but slightly inexperienced, wearing lab coat and goggles, focused expression.
Scene environment: character introduction scene in a bright modern laboratory with representative equipment.
Required visual elements: character portrait with equipment related to their ability.
Additional card context from the rules: ability: 复盘后将一次勉强维持改为控制风险。.
Composition: vertical 2:3; half-body or full-body portrait; character front or three-quarter view; minimal background props; safe cropping margins.
Extra production rule: Character is the main subject. Avoid multiple competing faces. Badge and papers must remain blank.
Color and material: pale blue, white, gray-blue, transparent glass, soft reflections on the lab bench, small amount of orange/yellow only for safety warning symbols or flame.
Border and crop: the image may include a thin rounded rectangle card border and warm off-white paper margin; keep all important subjects away from the edge.

Strict negative prompt: no readable Chinese text, no readable English text, no readable numbers, no logo, no watermark, no brand name, no school emblem, no UI text, no readable bottle labels, no readable notebook content, no readable clipboard content, no title, no card frame text. Labels, forms, badges and screens must be blank, blurred, or meaningless lines only. No photorealistic style, no 3D render, no chibi style, no horror style, no gore, no injured people, no large explosion, no chaotic disaster, no distorted face, no extra fingers, no missing hands, no duplicated faces, no cluttered composition.
```

### R02 Role card | 实验操作者

```text
Create ONE vertical no-text illustration for a laboratory safety board-game card.

Reference style: use the uploaded sample images as the main style reference. Match their clean academic watercolor look, blue-white palette, soft natural window light, transparent glassware, delicate anime-inspired characters, realistic chemistry lab equipment, rounded card-frame feeling, and calm educational tone.

Card ID: R02
Card type: Role card
Chinese card name: 实验操作者
Visual goal: Show a character portrait for the role "实验操作者". Role concept: 擅长推进操作任务。. Communicate the ability through pose and props, not text.
Main character: Zhou Heng; young Chinese male graduate student, short black hair, clear goggles, white lab coat, blue inner shirt, blue nitrile gloves, skilled at hands-on experiments.
Scene environment: character introduction scene in a bright modern laboratory with representative equipment.
Required visual elements: character portrait with equipment related to their ability.
Additional card context from the rules: ability: 若本轮任务完成，额外获得 1 贡献分。.
Composition: vertical 2:3; half-body or full-body portrait; character front or three-quarter view; minimal background props; safe cropping margins.
Extra production rule: Character is the main subject. Avoid multiple competing faces. Badge and papers must remain blank.
Color and material: pale blue, white, gray-blue, transparent glass, soft reflections on the lab bench, small amount of orange/yellow only for safety warning symbols or flame.
Border and crop: the image may include a thin rounded rectangle card border and warm off-white paper margin; keep all important subjects away from the edge.

Strict negative prompt: no readable Chinese text, no readable English text, no readable numbers, no logo, no watermark, no brand name, no school emblem, no UI text, no readable bottle labels, no readable notebook content, no readable clipboard content, no title, no card frame text. Labels, forms, badges and screens must be blank, blurred, or meaningless lines only. No photorealistic style, no 3D render, no chibi style, no horror style, no gore, no injured people, no large explosion, no chaotic disaster, no distorted face, no extra fingers, no missing hands, no duplicated faces, no cluttered composition.
```

### R03 Role card | 安全培训员

```text
Create ONE vertical no-text illustration for a laboratory safety board-game card.

Reference style: use the uploaded sample images as the main style reference. Match their clean academic watercolor look, blue-white palette, soft natural window light, transparent glassware, delicate anime-inspired characters, realistic chemistry lab equipment, rounded card-frame feeling, and calm educational tone.

Card ID: R03
Card type: Role card
Chinese card name: 安全培训员
Visual goal: Show a character portrait for the role "安全培训员". Role concept: 擅长控制风险和解释复盘。. Communicate the ability through pose and props, not text.
Main character: Cheng Yan; mature Chinese male doctoral student or teaching assistant, white lab coat, blue shirt, steady posture, coordinates laboratory safety.
Scene environment: character introduction scene in a bright modern laboratory with representative equipment.
Required visual elements: character portrait with equipment related to their ability.
Additional card context from the rules: ability: 将一次处置错误降低为勉强维持。.
Composition: vertical 2:3; half-body or full-body portrait; character front or three-quarter view; minimal background props; safe cropping margins.
Extra production rule: Character is the main subject. Avoid multiple competing faces. Badge and papers must remain blank.
Color and material: pale blue, white, gray-blue, transparent glass, soft reflections on the lab bench, small amount of orange/yellow only for safety warning symbols or flame.
Border and crop: the image may include a thin rounded rectangle card border and warm off-white paper margin; keep all important subjects away from the edge.

Strict negative prompt: no readable Chinese text, no readable English text, no readable numbers, no logo, no watermark, no brand name, no school emblem, no UI text, no readable bottle labels, no readable notebook content, no readable clipboard content, no title, no card frame text. Labels, forms, badges and screens must be blank, blurred, or meaningless lines only. No photorealistic style, no 3D render, no chibi style, no horror style, no gore, no injured people, no large explosion, no chaotic disaster, no distorted face, no extra fingers, no missing hands, no duplicated faces, no cluttered composition.
```

### R04 Role card | 仪器管理员

```text
Create ONE vertical no-text illustration for a laboratory safety board-game card.

Reference style: use the uploaded sample images as the main style reference. Match their clean academic watercolor look, blue-white palette, soft natural window light, transparent glassware, delicate anime-inspired characters, realistic chemistry lab equipment, rounded card-frame feeling, and calm educational tone.

Card ID: R04
Card type: Role card
Chinese card name: 仪器管理员
Visual goal: Show a character portrait for the role "仪器管理员". Role concept: 擅长设备、夹具和耗材管理。. Communicate the ability through pose and props, not text.
Main character: Equipment manager; young Chinese researcher, lab coat, goggles and gloves, checking instruments, clamps or gas cylinders.
Scene environment: character introduction scene in a bright modern laboratory with representative equipment.
Required visual elements: character portrait with equipment related to their ability.
Additional card context from the rules: ability: 设备类事件中减少 1 点安全值损失。.
Composition: vertical 2:3; half-body or full-body portrait; character front or three-quarter view; minimal background props; safe cropping margins.
Extra production rule: Character is the main subject. Avoid multiple competing faces. Badge and papers must remain blank.
Color and material: pale blue, white, gray-blue, transparent glass, soft reflections on the lab bench, small amount of orange/yellow only for safety warning symbols or flame.
Border and crop: the image may include a thin rounded rectangle card border and warm off-white paper margin; keep all important subjects away from the edge.

Strict negative prompt: no readable Chinese text, no readable English text, no readable numbers, no logo, no watermark, no brand name, no school emblem, no UI text, no readable bottle labels, no readable notebook content, no readable clipboard content, no title, no card frame text. Labels, forms, badges and screens must be blank, blurred, or meaningless lines only. No photorealistic style, no 3D render, no chibi style, no horror style, no gore, no injured people, no large explosion, no chaotic disaster, no distorted face, no extra fingers, no missing hands, no duplicated faces, no cluttered composition.
```

### R05 Role card | 记录负责人

```text
Create ONE vertical no-text illustration for a laboratory safety board-game card.

Reference style: use the uploaded sample images as the main style reference. Match their clean academic watercolor look, blue-white palette, soft natural window light, transparent glassware, delicate anime-inspired characters, realistic chemistry lab equipment, rounded card-frame feeling, and calm educational tone.

Card ID: R05
Card type: Role card
Chinese card name: 记录负责人
Visual goal: Show a character portrait for the role "记录负责人". Role concept: 擅长标签、台账和交接。. Communicate the ability through pose and props, not text.
Main character: Lin Cheng; young Chinese female graduate student, short black bob hair, clear goggles, white lab coat, blue inner shirt, often holding a notebook, careful and detail-oriented.
Scene environment: character introduction scene in a bright modern laboratory with representative equipment.
Required visual elements: character portrait with equipment related to their ability.
Additional card context from the rules: ability: 交接链触发时可取消 1 点隐患增加。.
Composition: vertical 2:3; half-body or full-body portrait; character front or three-quarter view; minimal background props; safe cropping margins.
Extra production rule: Character is the main subject. Avoid multiple competing faces. Badge and papers must remain blank.
Color and material: pale blue, white, gray-blue, transparent glass, soft reflections on the lab bench, small amount of orange/yellow only for safety warning symbols or flame.
Border and crop: the image may include a thin rounded rectangle card border and warm off-white paper margin; keep all important subjects away from the edge.

Strict negative prompt: no readable Chinese text, no readable English text, no readable numbers, no logo, no watermark, no brand name, no school emblem, no UI text, no readable bottle labels, no readable notebook content, no readable clipboard content, no title, no card frame text. Labels, forms, badges and screens must be blank, blurred, or meaningless lines only. No photorealistic style, no 3D render, no chibi style, no horror style, no gore, no injured people, no large explosion, no chaotic disaster, no distorted face, no extra fingers, no missing hands, no duplicated faces, no cluttered composition.
```

### R06 Role card | 应急响应员

```text
Create ONE vertical no-text illustration for a laboratory safety board-game card.

Reference style: use the uploaded sample images as the main style reference. Match their clean academic watercolor look, blue-white palette, soft natural window light, transparent glassware, delicate anime-inspired characters, realistic chemistry lab equipment, rounded card-frame feeling, and calm educational tone.

Card ID: R06
Card type: Role card
Chinese card name: 应急响应员
Visual goal: Show a character portrait for the role "应急响应员". Role concept: 擅长高危事件初期处置。. Communicate the ability through pose and props, not text.
Main character: Gu Ning; young Chinese female doctoral student, low ponytail or short hair, goggles, lab coat, calm posture, good at recording and verification.
Scene environment: character introduction scene in a bright modern laboratory with representative equipment.
Required visual elements: character portrait with equipment related to their ability.
Additional card context from the rules: ability: 高危事件中打出应急或撤离时额外降低 1 事故等级压力。.
Composition: vertical 2:3; half-body or full-body portrait; character front or three-quarter view; minimal background props; safe cropping margins.
Extra production rule: Character is the main subject. Avoid multiple competing faces. Badge and papers must remain blank.
Color and material: pale blue, white, gray-blue, transparent glass, soft reflections on the lab bench, small amount of orange/yellow only for safety warning symbols or flame.
Border and crop: the image may include a thin rounded rectangle card border and warm off-white paper margin; keep all important subjects away from the edge.

Strict negative prompt: no readable Chinese text, no readable English text, no readable numbers, no logo, no watermark, no brand name, no school emblem, no UI text, no readable bottle labels, no readable notebook content, no readable clipboard content, no title, no card frame text. Labels, forms, badges and screens must be blank, blurred, or meaningless lines only. No photorealistic style, no 3D render, no chibi style, no horror style, no gore, no injured people, no large explosion, no chaotic disaster, no distorted face, no extra fingers, no missing hands, no duplicated faces, no cluttered composition.
```

### P01 Post card | 安全员

```text
Create ONE vertical no-text illustration for a laboratory safety board-game card.

Reference style: use the uploaded sample images as the main style reference. Match their clean academic watercolor look, blue-white palette, soft natural window light, transparent glassware, delicate anime-inspired characters, realistic chemistry lab equipment, rounded card-frame feeling, and calm educational tone.

Card ID: P01
Card type: Post card
Chinese card name: 安全员
Visual goal: Show the duty scene for the post "安全员". Post concept: 负责风险控制和高危事件判断。. Emphasize coordination, judgment and responsibility.
Main character: Cheng Yan; mature Chinese male doctoral student or teaching assistant, white lab coat, blue shirt, steady posture, coordinates laboratory safety.
Scene environment: team coordination scene around a laboratory bench, clear role division and visible safety workflow.
Required visual elements: role-duty scene with a clear main coordinator and teammates.
Additional card context from the rules: responsibility: 优先判断风险状态。.
Composition: vertical 2:3; main post holder centered; teammates and risk source placed to the sides; clear collaboration relationship.
Extra production rule: Two or three teammates may appear, but the post holder must be largest and clearest. Show responsibility through gesture and positioning.
Color and material: pale blue, white, gray-blue, transparent glass, soft reflections on the lab bench, small amount of orange/yellow only for safety warning symbols or flame.
Border and crop: the image may include a thin rounded rectangle card border and warm off-white paper margin; keep all important subjects away from the edge.

Strict negative prompt: no readable Chinese text, no readable English text, no readable numbers, no logo, no watermark, no brand name, no school emblem, no UI text, no readable bottle labels, no readable notebook content, no readable clipboard content, no title, no card frame text. Labels, forms, badges and screens must be blank, blurred, or meaningless lines only. No photorealistic style, no 3D render, no chibi style, no horror style, no gore, no injured people, no large explosion, no chaotic disaster, no distorted face, no extra fingers, no missing hands, no duplicated faces, no cluttered composition.
```

### P02 Post card | 操作者

```text
Create ONE vertical no-text illustration for a laboratory safety board-game card.

Reference style: use the uploaded sample images as the main style reference. Match their clean academic watercolor look, blue-white palette, soft natural window light, transparent glassware, delicate anime-inspired characters, realistic chemistry lab equipment, rounded card-frame feeling, and calm educational tone.

Card ID: P02
Card type: Post card
Chinese card name: 操作者
Visual goal: Show the duty scene for the post "操作者". Post concept: 负责推进实验任务。. Emphasize coordination, judgment and responsibility.
Main character: Zhou Heng; young Chinese male graduate student, short black hair, clear goggles, white lab coat, blue inner shirt, blue nitrile gloves, skilled at hands-on experiments.
Scene environment: team coordination scene around a laboratory bench, clear role division and visible safety workflow.
Required visual elements: role-duty scene with a clear main coordinator and teammates.
Additional card context from the rules: responsibility: 确认任务行动是否匹配。.
Composition: vertical 2:3; main post holder centered; teammates and risk source placed to the sides; clear collaboration relationship.
Extra production rule: Two or three teammates may appear, but the post holder must be largest and clearest. Show responsibility through gesture and positioning.
Color and material: pale blue, white, gray-blue, transparent glass, soft reflections on the lab bench, small amount of orange/yellow only for safety warning symbols or flame.
Border and crop: the image may include a thin rounded rectangle card border and warm off-white paper margin; keep all important subjects away from the edge.

Strict negative prompt: no readable Chinese text, no readable English text, no readable numbers, no logo, no watermark, no brand name, no school emblem, no UI text, no readable bottle labels, no readable notebook content, no readable clipboard content, no title, no card frame text. Labels, forms, badges and screens must be blank, blurred, or meaningless lines only. No photorealistic style, no 3D render, no chibi style, no horror style, no gore, no injured people, no large explosion, no chaotic disaster, no distorted face, no extra fingers, no missing hands, no duplicated faces, no cluttered composition.
```

### P03 Post card | 记录员

```text
Create ONE vertical no-text illustration for a laboratory safety board-game card.

Reference style: use the uploaded sample images as the main style reference. Match their clean academic watercolor look, blue-white palette, soft natural window light, transparent glassware, delicate anime-inspired characters, realistic chemistry lab equipment, rounded card-frame feeling, and calm educational tone.

Card ID: P03
Card type: Post card
Chinese card name: 记录员
Visual goal: Show the duty scene for the post "记录员". Post concept: 负责标签、记录和复盘。. Emphasize coordination, judgment and responsibility.
Main character: Lin Cheng; young Chinese female graduate student, short black bob hair, clear goggles, white lab coat, blue inner shirt, often holding a notebook, careful and detail-oriented.
Scene environment: team coordination scene around a laboratory bench, clear role division and visible safety workflow.
Required visual elements: role-duty scene with a clear main coordinator and teammates.
Additional card context from the rules: responsibility: 维护交接链信息。.
Composition: vertical 2:3; main post holder centered; teammates and risk source placed to the sides; clear collaboration relationship.
Extra production rule: Two or three teammates may appear, but the post holder must be largest and clearest. Show responsibility through gesture and positioning.
Color and material: pale blue, white, gray-blue, transparent glass, soft reflections on the lab bench, small amount of orange/yellow only for safety warning symbols or flame.
Border and crop: the image may include a thin rounded rectangle card border and warm off-white paper margin; keep all important subjects away from the edge.

Strict negative prompt: no readable Chinese text, no readable English text, no readable numbers, no logo, no watermark, no brand name, no school emblem, no UI text, no readable bottle labels, no readable notebook content, no readable clipboard content, no title, no card frame text. Labels, forms, badges and screens must be blank, blurred, or meaningless lines only. No photorealistic style, no 3D render, no chibi style, no horror style, no gore, no injured people, no large explosion, no chaotic disaster, no distorted face, no extra fingers, no missing hands, no duplicated faces, no cluttered composition.
```

### P04 Post card | 资源管理员

```text
Create ONE vertical no-text illustration for a laboratory safety board-game card.

Reference style: use the uploaded sample images as the main style reference. Match their clean academic watercolor look, blue-white palette, soft natural window light, transparent glassware, delicate anime-inspired characters, realistic chemistry lab equipment, rounded card-frame feeling, and calm educational tone.

Card ID: P04
Card type: Post card
Chinese card name: 资源管理员
Visual goal: Show the duty scene for the post "资源管理员". Post concept: 负责手牌、设备和耗材。. Emphasize coordination, judgment and responsibility.
Main character: Gu Ning; young Chinese female doctoral student, low ponytail or short hair, goggles, lab coat, calm posture, good at recording and verification.
Scene environment: team coordination scene around a laboratory bench, clear role division and visible safety workflow.
Required visual elements: role-duty scene with a clear main coordinator and teammates.
Additional card context from the rules: responsibility: 管理公共行动资源。.
Composition: vertical 2:3; main post holder centered; teammates and risk source placed to the sides; clear collaboration relationship.
Extra production rule: Two or three teammates may appear, but the post holder must be largest and clearest. Show responsibility through gesture and positioning.
Color and material: pale blue, white, gray-blue, transparent glass, soft reflections on the lab bench, small amount of orange/yellow only for safety warning symbols or flame.
Border and crop: the image may include a thin rounded rectangle card border and warm off-white paper margin; keep all important subjects away from the edge.

Strict negative prompt: no readable Chinese text, no readable English text, no readable numbers, no logo, no watermark, no brand name, no school emblem, no UI text, no readable bottle labels, no readable notebook content, no readable clipboard content, no title, no card frame text. Labels, forms, badges and screens must be blank, blurred, or meaningless lines only. No photorealistic style, no 3D render, no chibi style, no horror style, no gore, no injured people, no large explosion, no chaotic disaster, no distorted face, no extra fingers, no missing hands, no duplicated faces, no cluttered composition.
```

### S01 Strategy card | 稳健管理

```text
Create ONE vertical no-text illustration for a laboratory safety board-game card.

Reference style: use the uploaded sample images as the main style reference. Match their clean academic watercolor look, blue-white palette, soft natural window light, transparent glassware, delicate anime-inspired characters, realistic chemistry lab equipment, rounded card-frame feeling, and calm educational tone.

Card ID: S01
Card type: Strategy card
Chinese card name: 稳健管理
Visual goal: Show a team strategy scene for "稳健管理". Strategy concept: 提高安全冗余。. It should feel like a route choice inside a real lab, not a fantasy scene.
Main character: Lab team; 2 to 4 Chinese lab members in lab coats and goggles, cooperating around a bench, clear hierarchy and no crowding.
Scene environment: character introduction scene in a bright modern laboratory with representative equipment.
Required visual elements: team discussing a route around a lab bench, blank cards or diagrams only.
Additional card context from the rules: effect: 首次安全值损失减少 1。 | cost: 优秀通关要求隐患不高于 2。 | playstyle: 保守控场。.
Composition: vertical 2:3; team decision composition inside a lab; bench in foreground; fume hood or shelves in background; clear route/choice feeling.
Extra production rule: Use team movement, bench layout, or blank visual route cards to express strategy. Do not draw readable board-game cards.
Color and material: pale blue, white, gray-blue, transparent glass, soft reflections on the lab bench, small amount of orange/yellow only for safety warning symbols or flame.
Border and crop: the image may include a thin rounded rectangle card border and warm off-white paper margin; keep all important subjects away from the edge.

Strict negative prompt: no readable Chinese text, no readable English text, no readable numbers, no logo, no watermark, no brand name, no school emblem, no UI text, no readable bottle labels, no readable notebook content, no readable clipboard content, no title, no card frame text. Labels, forms, badges and screens must be blank, blurred, or meaningless lines only. No photorealistic style, no 3D render, no chibi style, no horror style, no gore, no injured people, no large explosion, no chaotic disaster, no distorted face, no extra fingers, no missing hands, no duplicated faces, no cluttered composition.
```

### S02 Strategy card | 效率优先

```text
Create ONE vertical no-text illustration for a laboratory safety board-game card.

Reference style: use the uploaded sample images as the main style reference. Match their clean academic watercolor look, blue-white palette, soft natural window light, transparent glassware, delicate anime-inspired characters, realistic chemistry lab equipment, rounded card-frame feeling, and calm educational tone.

Card ID: S02
Card type: Strategy card
Chinese card name: 效率优先
Visual goal: Show a team strategy scene for "效率优先". Strategy concept: 强化任务推进。. It should feel like a route choice inside a real lab, not a fantasy scene.
Main character: Lab team; 2 to 4 Chinese lab members in lab coats and goggles, cooperating around a bench, clear hierarchy and no crowding.
Scene environment: character introduction scene in a bright modern laboratory with representative equipment.
Required visual elements: team discussing a route around a lab bench, blank cards or diagrams only.
Additional card context from the rules: effect: 首次连续两轮完成任务时进度 +1。 | cost: 触发奖励后安全值 -2；高危错误额外增加事故等级。 | playstyle: 快速推进。.
Composition: vertical 2:3; team decision composition inside a lab; bench in foreground; fume hood or shelves in background; clear route/choice feeling.
Extra production rule: Use team movement, bench layout, or blank visual route cards to express strategy. Do not draw readable board-game cards.
Color and material: pale blue, white, gray-blue, transparent glass, soft reflections on the lab bench, small amount of orange/yellow only for safety warning symbols or flame.
Border and crop: the image may include a thin rounded rectangle card border and warm off-white paper margin; keep all important subjects away from the edge.

Strict negative prompt: no readable Chinese text, no readable English text, no readable numbers, no logo, no watermark, no brand name, no school emblem, no UI text, no readable bottle labels, no readable notebook content, no readable clipboard content, no title, no card frame text. Labels, forms, badges and screens must be blank, blurred, or meaningless lines only. No photorealistic style, no 3D render, no chibi style, no horror style, no gore, no injured people, no large explosion, no chaotic disaster, no distorted face, no extra fingers, no missing hands, no duplicated faces, no cluttered composition.
```

### S03 Strategy card | 规范先行

```text
Create ONE vertical no-text illustration for a laboratory safety board-game card.

Reference style: use the uploaded sample images as the main style reference. Match their clean academic watercolor look, blue-white palette, soft natural window light, transparent glassware, delicate anime-inspired characters, realistic chemistry lab equipment, rounded card-frame feeling, and calm educational tone.

Card ID: S03
Card type: Strategy card
Chinese card name: 规范先行
Visual goal: Show a team strategy scene for "规范先行". Strategy concept: 奖励完整处置。. It should feel like a route choice inside a real lab, not a fantasy scene.
Main character: Lab team; 2 to 4 Chinese lab members in lab coats and goggles, cooperating around a bench, clear hierarchy and no crowding.
Scene environment: character introduction scene in a bright modern laboratory with representative equipment.
Required visual elements: team discussing a route around a lab bench, blank cards or diagrams only.
Additional card context from the rules: effect: 每次完整处置额外清除 1 隐患。 | cost: 勉强维持时额外失去 1 安全值。 | playstyle: 完美处置。.
Composition: vertical 2:3; team decision composition inside a lab; bench in foreground; fume hood or shelves in background; clear route/choice feeling.
Extra production rule: Use team movement, bench layout, or blank visual route cards to express strategy. Do not draw readable board-game cards.
Color and material: pale blue, white, gray-blue, transparent glass, soft reflections on the lab bench, small amount of orange/yellow only for safety warning symbols or flame.
Border and crop: the image may include a thin rounded rectangle card border and warm off-white paper margin; keep all important subjects away from the edge.

Strict negative prompt: no readable Chinese text, no readable English text, no readable numbers, no logo, no watermark, no brand name, no school emblem, no UI text, no readable bottle labels, no readable notebook content, no readable clipboard content, no title, no card frame text. Labels, forms, badges and screens must be blank, blurred, or meaningless lines only. No photorealistic style, no 3D render, no chibi style, no horror style, no gore, no injured people, no large explosion, no chaotic disaster, no distorted face, no extra fingers, no missing hands, no duplicated faces, no cluttered composition.
```

### S04 Strategy card | 风险隔离

```text
Create ONE vertical no-text illustration for a laboratory safety board-game card.

Reference style: use the uploaded sample images as the main style reference. Match their clean academic watercolor look, blue-white palette, soft natural window light, transparent glassware, delicate anime-inspired characters, realistic chemistry lab equipment, rounded card-frame feeling, and calm educational tone.

Card ID: S04
Card type: Strategy card
Chinese card name: 风险隔离
Visual goal: Show a team strategy scene for "风险隔离". Strategy concept: 强化隔离和交接。. It should feel like a route choice inside a real lab, not a fantasy scene.
Main character: Lab team; 2 to 4 Chinese lab members in lab coats and goggles, cooperating around a bench, clear hierarchy and no crowding.
Scene environment: character introduction scene in a bright modern laboratory with representative equipment.
Required visual elements: team discussing a route around a lab bench, blank cards or diagrams only.
Additional card context from the rules: effect: 交接链首次触发时不增加隐患。 | cost: 通关时事故等级必须不高于 1。 | playstyle: 隐患管理。.
Composition: vertical 2:3; team decision composition inside a lab; bench in foreground; fume hood or shelves in background; clear route/choice feeling.
Extra production rule: Use team movement, bench layout, or blank visual route cards to express strategy. Do not draw readable board-game cards.
Color and material: pale blue, white, gray-blue, transparent glass, soft reflections on the lab bench, small amount of orange/yellow only for safety warning symbols or flame.
Border and crop: the image may include a thin rounded rectangle card border and warm off-white paper margin; keep all important subjects away from the edge.

Strict negative prompt: no readable Chinese text, no readable English text, no readable numbers, no logo, no watermark, no brand name, no school emblem, no UI text, no readable bottle labels, no readable notebook content, no readable clipboard content, no title, no card frame text. Labels, forms, badges and screens must be blank, blurred, or meaningless lines only. No photorealistic style, no 3D render, no chibi style, no horror style, no gore, no injured people, no large explosion, no chaotic disaster, no distorted face, no extra fingers, no missing hands, no duplicated faces, no cluttered composition.
```

### S05 Strategy card | 岗位训练

```text
Create ONE vertical no-text illustration for a laboratory safety board-game card.

Reference style: use the uploaded sample images as the main style reference. Match their clean academic watercolor look, blue-white palette, soft natural window light, transparent glassware, delicate anime-inspired characters, realistic chemistry lab equipment, rounded card-frame feeling, and calm educational tone.

Card ID: S05
Card type: Strategy card
Chinese card name: 岗位训练
Visual goal: Show a team strategy scene for "岗位训练". Strategy concept: 强化个人贡献。. It should feel like a route choice inside a real lab, not a fantasy scene.
Main character: Lab team; 2 to 4 Chinese lab members in lab coats and goggles, cooperating around a bench, clear hierarchy and no crowding.
Scene environment: character introduction scene in a bright modern laboratory with representative equipment.
Required visual elements: team discussing a route around a lab bench, blank cards or diagrams only.
Additional card context from the rules: effect: 每名玩家首次触发岗位奖励时额外 +1 贡献分。 | cost: 若有人贡献分低于 3，不能优秀通关。 | playstyle: 均衡参与。.
Composition: vertical 2:3; team decision composition inside a lab; bench in foreground; fume hood or shelves in background; clear route/choice feeling.
Extra production rule: Use team movement, bench layout, or blank visual route cards to express strategy. Do not draw readable board-game cards.
Color and material: pale blue, white, gray-blue, transparent glass, soft reflections on the lab bench, small amount of orange/yellow only for safety warning symbols or flame.
Border and crop: the image may include a thin rounded rectangle card border and warm off-white paper margin; keep all important subjects away from the edge.

Strict negative prompt: no readable Chinese text, no readable English text, no readable numbers, no logo, no watermark, no brand name, no school emblem, no UI text, no readable bottle labels, no readable notebook content, no readable clipboard content, no title, no card frame text. Labels, forms, badges and screens must be blank, blurred, or meaningless lines only. No photorealistic style, no 3D render, no chibi style, no horror style, no gore, no injured people, no large explosion, no chaotic disaster, no distorted face, no extra fingers, no missing hands, no duplicated faces, no cluttered composition.
```

### S06 Strategy card | 设备优先

```text
Create ONE vertical no-text illustration for a laboratory safety board-game card.

Reference style: use the uploaded sample images as the main style reference. Match their clean academic watercolor look, blue-white palette, soft natural window light, transparent glassware, delicate anime-inspired characters, realistic chemistry lab equipment, rounded card-frame feeling, and calm educational tone.

Card ID: S06
Card type: Strategy card
Chinese card name: 设备优先
Visual goal: Show a team strategy scene for "设备优先". Strategy concept: 强化设备事件处理。. It should feel like a route choice inside a real lab, not a fantasy scene.
Main character: Lab team; 2 to 4 Chinese lab members in lab coats and goggles, cooperating around a bench, clear hierarchy and no crowding.
Scene environment: character introduction scene in a bright modern laboratory with representative equipment.
Required visual elements: team discussing a route around a lab bench, blank cards or diagrams only.
Additional card context from the rules: effect: 设备类事件中检查或固定视为额外辅助行动。 | cost: 人员暴露类事件不能获得该收益。 | playstyle: 设备控制。.
Composition: vertical 2:3; team decision composition inside a lab; bench in foreground; fume hood or shelves in background; clear route/choice feeling.
Extra production rule: Use team movement, bench layout, or blank visual route cards to express strategy. Do not draw readable board-game cards.
Color and material: pale blue, white, gray-blue, transparent glass, soft reflections on the lab bench, small amount of orange/yellow only for safety warning symbols or flame.
Border and crop: the image may include a thin rounded rectangle card border and warm off-white paper margin; keep all important subjects away from the edge.

Strict negative prompt: no readable Chinese text, no readable English text, no readable numbers, no logo, no watermark, no brand name, no school emblem, no UI text, no readable bottle labels, no readable notebook content, no readable clipboard content, no title, no card frame text. Labels, forms, badges and screens must be blank, blurred, or meaningless lines only. No photorealistic style, no 3D render, no chibi style, no horror style, no gore, no injured people, no large explosion, no chaotic disaster, no distorted face, no extra fingers, no missing hands, no duplicated faces, no cluttered composition.
```

### S07 Strategy card | 复盘驱动

```text
Create ONE vertical no-text illustration for a laboratory safety board-game card.

Reference style: use the uploaded sample images as the main style reference. Match their clean academic watercolor look, blue-white palette, soft natural window light, transparent glassware, delicate anime-inspired characters, realistic chemistry lab equipment, rounded card-frame feeling, and calm educational tone.

Card ID: S07
Card type: Strategy card
Chinese card name: 复盘驱动
Visual goal: Show a team strategy scene for "复盘驱动". Strategy concept: 强化知识点收益。. It should feel like a route choice inside a real lab, not a fantasy scene.
Main character: Lab team; 2 to 4 Chinese lab members in lab coats and goggles, cooperating around a bench, clear hierarchy and no crowding.
Scene environment: character introduction scene in a bright modern laboratory with representative equipment.
Required visual elements: team discussing a route around a lab bench, blank cards or diagrams only.
Additional card context from the rules: effect: 每完成 3 个复盘知识点，团队抽 1 张行动牌。 | cost: 跳过复盘时隐患 +1。 | playstyle: 教学训练。.
Composition: vertical 2:3; team decision composition inside a lab; bench in foreground; fume hood or shelves in background; clear route/choice feeling.
Extra production rule: Use team movement, bench layout, or blank visual route cards to express strategy. Do not draw readable board-game cards.
Color and material: pale blue, white, gray-blue, transparent glass, soft reflections on the lab bench, small amount of orange/yellow only for safety warning symbols or flame.
Border and crop: the image may include a thin rounded rectangle card border and warm off-white paper margin; keep all important subjects away from the edge.

Strict negative prompt: no readable Chinese text, no readable English text, no readable numbers, no logo, no watermark, no brand name, no school emblem, no UI text, no readable bottle labels, no readable notebook content, no readable clipboard content, no title, no card frame text. Labels, forms, badges and screens must be blank, blurred, or meaningless lines only. No photorealistic style, no 3D render, no chibi style, no horror style, no gore, no injured people, no large explosion, no chaotic disaster, no distorted face, no extra fingers, no missing hands, no duplicated faces, no cluttered composition.
```

### S08 Strategy card | 应急演练

```text
Create ONE vertical no-text illustration for a laboratory safety board-game card.

Reference style: use the uploaded sample images as the main style reference. Match their clean academic watercolor look, blue-white palette, soft natural window light, transparent glassware, delicate anime-inspired characters, realistic chemistry lab equipment, rounded card-frame feeling, and calm educational tone.

Card ID: S08
Card type: Strategy card
Chinese card name: 应急演练
Visual goal: Show a team strategy scene for "应急演练". Strategy concept: 强化高危事件应对。. It should feel like a route choice inside a real lab, not a fantasy scene.
Main character: Lab team; 2 to 4 Chinese lab members in lab coats and goggles, cooperating around a bench, clear hierarchy and no crowding.
Scene environment: character introduction scene in a bright modern laboratory with representative equipment.
Required visual elements: team discussing a route around a lab bench, blank cards or diagrams only.
Additional card context from the rules: effect: 首次失控事件中事故等级增加减少 1。 | cost: 低危任务推进效率 -1 次奖励。 | playstyle: 高压应急。.
Composition: vertical 2:3; team decision composition inside a lab; bench in foreground; fume hood or shelves in background; clear route/choice feeling.
Extra production rule: Use team movement, bench layout, or blank visual route cards to express strategy. Do not draw readable board-game cards.
Color and material: pale blue, white, gray-blue, transparent glass, soft reflections on the lab bench, small amount of orange/yellow only for safety warning symbols or flame.
Border and crop: the image may include a thin rounded rectangle card border and warm off-white paper margin; keep all important subjects away from the edge.

Strict negative prompt: no readable Chinese text, no readable English text, no readable numbers, no logo, no watermark, no brand name, no school emblem, no UI text, no readable bottle labels, no readable notebook content, no readable clipboard content, no title, no card frame text. Labels, forms, badges and screens must be blank, blurred, or meaningless lines only. No photorealistic style, no 3D render, no chibi style, no horror style, no gore, no injured people, no large explosion, no chaotic disaster, no distorted face, no extra fingers, no missing hands, no duplicated faces, no cluttered composition.
```

### D01 Debrief card | PPE 基础防护

```text
Create ONE vertical no-text illustration for a laboratory safety board-game card.

Reference style: use the uploaded sample images as the main style reference. Match their clean academic watercolor look, blue-white palette, soft natural window light, transparent glassware, delicate anime-inspired characters, realistic chemistry lab equipment, rounded card-frame feeling, and calm educational tone.

Card ID: D01
Card type: Debrief card
Chinese card name: PPE 基础防护
Visual goal: Show a teaching debrief illustration for "PPE 基础防护". Knowledge topic: 基础防护. Correct action: 操作前确认护目镜、手套和实验服。
Main character: Cheng Yan; mature Chinese male doctoral student or teaching assistant, white lab coat, blue shirt, steady posture, coordinates laboratory safety.
Scene environment: teaching debrief scene, controlled risk source, blank checklist, lab notebook, calm discussion.
Required visual elements: safety goggles, blue nitrile gloves, white lab coat, visible PPE checking or wearing action.
Additional card context from the rules: why: PPE 是暴露前的第一道屏障。 | review_question: 本轮是否在操作前完成防护确认？.
Composition: vertical 2:3; stable post-response debrief scene; blank notebook or checklist foreground; controlled risk source in background.
Extra production rule: The scene should look like calm teaching review or correct post-response handling, not chaotic accident response.
Color and material: pale blue, white, gray-blue, transparent glass, soft reflections on the lab bench, small amount of orange/yellow only for safety warning symbols or flame.
Border and crop: the image may include a thin rounded rectangle card border and warm off-white paper margin; keep all important subjects away from the edge.

Strict negative prompt: no readable Chinese text, no readable English text, no readable numbers, no logo, no watermark, no brand name, no school emblem, no UI text, no readable bottle labels, no readable notebook content, no readable clipboard content, no title, no card frame text. Labels, forms, badges and screens must be blank, blurred, or meaningless lines only. No photorealistic style, no 3D render, no chibi style, no horror style, no gore, no injured people, no large explosion, no chaotic disaster, no distorted face, no extra fingers, no missing hands, no duplicated faces, no cluttered composition.
```

### D02 Debrief card | 标签与身份确认

```text
Create ONE vertical no-text illustration for a laboratory safety board-game card.

Reference style: use the uploaded sample images as the main style reference. Match their clean academic watercolor look, blue-white palette, soft natural window light, transparent glassware, delicate anime-inspired characters, realistic chemistry lab equipment, rounded card-frame feeling, and calm educational tone.

Card ID: D02
Card type: Debrief card
Chinese card name: 标签与身份确认
Visual goal: Show a teaching debrief illustration for "标签与身份确认". Knowledge topic: 标签确认. Correct action: 暂停、核对标签、记录和负责人。
Main character: Lin Cheng; young Chinese female graduate student, short black bob hair, clear goggles, white lab coat, blue inner shirt, often holding a notebook, careful and detail-oriented.
Scene environment: teaching debrief scene, controlled risk source, blank checklist, lab notebook, calm discussion.
Required visual elements: reagent bottle with blank or blurred label, absolutely no readable text.
Additional card context from the rules: why: 身份、浓度和危险信息不可靠时不能继续使用。 | review_question: 如果标签模糊，下一步应先做什么？.
Composition: vertical 2:3; stable post-response debrief scene; blank notebook or checklist foreground; controlled risk source in background.
Extra production rule: The scene should look like calm teaching review or correct post-response handling, not chaotic accident response.
Color and material: pale blue, white, gray-blue, transparent glass, soft reflections on the lab bench, small amount of orange/yellow only for safety warning symbols or flame.
Border and crop: the image may include a thin rounded rectangle card border and warm off-white paper margin; keep all important subjects away from the edge.

Strict negative prompt: no readable Chinese text, no readable English text, no readable numbers, no logo, no watermark, no brand name, no school emblem, no UI text, no readable bottle labels, no readable notebook content, no readable clipboard content, no title, no card frame text. Labels, forms, badges and screens must be blank, blurred, or meaningless lines only. No photorealistic style, no 3D render, no chibi style, no horror style, no gore, no injured people, no large explosion, no chaotic disaster, no distorted face, no extra fingers, no missing hands, no duplicated faces, no cluttered composition.
```

### D03 Debrief card | 废液可追溯

```text
Create ONE vertical no-text illustration for a laboratory safety board-game card.

Reference style: use the uploaded sample images as the main style reference. Match their clean academic watercolor look, blue-white palette, soft natural window light, transparent glassware, delicate anime-inspired characters, realistic chemistry lab equipment, rounded card-frame feeling, and calm educational tone.

Card ID: D03
Card type: Debrief card
Chinese card name: 废液可追溯
Visual goal: Show a teaching debrief illustration for "废液可追溯". Knowledge topic: 废液标签. Correct action: 分类、贴签、记录日期和类别。
Main character: Zhou Heng; young Chinese male graduate student, short black hair, clear goggles, white lab coat, blue inner shirt, blue nitrile gloves, skilled at hands-on experiments.
Scene environment: teaching debrief scene, controlled risk source, blank checklist, lab notebook, calm discussion.
Required visual elements: waste bottle, sorted waste container, cleanup action, blank label only.
Additional card context from the rules: why: 无法追溯会放大后续混放风险。 | review_question: 废液桶缺标签时能否继续倒入？.
Composition: vertical 2:3; stable post-response debrief scene; blank notebook or checklist foreground; controlled risk source in background.
Extra production rule: The scene should look like calm teaching review or correct post-response handling, not chaotic accident response.
Color and material: pale blue, white, gray-blue, transparent glass, soft reflections on the lab bench, small amount of orange/yellow only for safety warning symbols or flame.
Border and crop: the image may include a thin rounded rectangle card border and warm off-white paper margin; keep all important subjects away from the edge.

Strict negative prompt: no readable Chinese text, no readable English text, no readable numbers, no logo, no watermark, no brand name, no school emblem, no UI text, no readable bottle labels, no readable notebook content, no readable clipboard content, no title, no card frame text. Labels, forms, badges and screens must be blank, blurred, or meaningless lines only. No photorealistic style, no 3D render, no chibi style, no horror style, no gore, no injured people, no large explosion, no chaotic disaster, no distorted face, no extra fingers, no missing hands, no duplicated faces, no cluttered composition.
```

### D04 Debrief card | 污染扩散控制

```text
Create ONE vertical no-text illustration for a laboratory safety board-game card.

Reference style: use the uploaded sample images as the main style reference. Match their clean academic watercolor look, blue-white palette, soft natural window light, transparent glassware, delicate anime-inspired characters, realistic chemistry lab equipment, rounded card-frame feeling, and calm educational tone.

Card ID: D04
Card type: Debrief card
Chinese card name: 污染扩散控制
Visual goal: Show a teaching debrief illustration for "污染扩散控制". Knowledge topic: 污染控制. Correct action: 更换手套并清洁被污染区域。
Main character: Gu Ning; young Chinese female doctoral student, low ponytail or short hair, goggles, lab coat, calm posture, good at recording and verification.
Scene environment: teaching debrief scene, controlled risk source, blank checklist, lab notebook, calm discussion.
Required visual elements: two containers or pipettes too close, cross-contamination risk.
Additional card context from the rules: why: 交叉污染会影响人员和环境安全。 | review_question: 哪些动作可能把污染带出实验台？.
Composition: vertical 2:3; stable post-response debrief scene; blank notebook or checklist foreground; controlled risk source in background.
Extra production rule: The scene should look like calm teaching review or correct post-response handling, not chaotic accident response.
Color and material: pale blue, white, gray-blue, transparent glass, soft reflections on the lab bench, small amount of orange/yellow only for safety warning symbols or flame.
Border and crop: the image may include a thin rounded rectangle card border and warm off-white paper margin; keep all important subjects away from the edge.

Strict negative prompt: no readable Chinese text, no readable English text, no readable numbers, no logo, no watermark, no brand name, no school emblem, no UI text, no readable bottle labels, no readable notebook content, no readable clipboard content, no title, no card frame text. Labels, forms, badges and screens must be blank, blurred, or meaningless lines only. No photorealistic style, no 3D render, no chibi style, no horror style, no gore, no injured people, no large explosion, no chaotic disaster, no distorted face, no extra fingers, no missing hands, no duplicated faces, no cluttered composition.
```

### D05 Debrief card | 挥发性溶剂通风

```text
Create ONE vertical no-text illustration for a laboratory safety board-game card.

Reference style: use the uploaded sample images as the main style reference. Match their clean academic watercolor look, blue-white palette, soft natural window light, transparent glassware, delicate anime-inspired characters, realistic chemistry lab equipment, rounded card-frame feeling, and calm educational tone.

Card ID: D05
Card type: Debrief card
Chinese card name: 挥发性溶剂通风
Visual goal: Show a teaching debrief illustration for "挥发性溶剂通风". Knowledge topic: 通风控制. Correct action: 减少暴露面积和暴露时间。
Main character: Cheng Yan; mature Chinese male doctoral student or teaching assistant, white lab coat, blue shirt, steady posture, coordinates laboratory safety.
Scene environment: teaching debrief scene, controlled risk source, blank checklist, lab notebook, calm discussion.
Required visual elements: fume hood, airflow arrows as simple graphic marks, operation moved toward the hood.
Additional card context from the rules: why: 通风能降低吸入和火灾风险。 | review_question: 为什么不能用动作快代替通风？.
Composition: vertical 2:3; stable post-response debrief scene; blank notebook or checklist foreground; controlled risk source in background.
Extra production rule: The scene should look like calm teaching review or correct post-response handling, not chaotic accident response.
Color and material: pale blue, white, gray-blue, transparent glass, soft reflections on the lab bench, small amount of orange/yellow only for safety warning symbols or flame.
Border and crop: the image may include a thin rounded rectangle card border and warm off-white paper margin; keep all important subjects away from the edge.

Strict negative prompt: no readable Chinese text, no readable English text, no readable numbers, no logo, no watermark, no brand name, no school emblem, no UI text, no readable bottle labels, no readable notebook content, no readable clipboard content, no title, no card frame text. Labels, forms, badges and screens must be blank, blurred, or meaningless lines only. No photorealistic style, no 3D render, no chibi style, no horror style, no gore, no injured people, no large explosion, no chaotic disaster, no distorted face, no extra fingers, no missing hands, no duplicated faces, no cluttered composition.
```

### D06 Debrief card | 火源管理

```text
Create ONE vertical no-text illustration for a laboratory safety board-game card.

Reference style: use the uploaded sample images as the main style reference. Match their clean academic watercolor look, blue-white palette, soft natural window light, transparent glassware, delicate anime-inspired characters, realistic chemistry lab equipment, rounded card-frame feeling, and calm educational tone.

Card ID: D06
Card type: Debrief card
Chinese card name: 火源管理
Visual goal: Show a teaching debrief illustration for "火源管理". Knowledge topic: 火灾预防. Correct action: 移开可燃物并切断热源。
Main character: Lin Cheng; young Chinese female graduate student, short black bob hair, clear goggles, white lab coat, blue inner shirt, often holding a notebook, careful and detail-oriented.
Scene environment: teaching debrief scene, controlled risk source, blank checklist, lab notebook, calm discussion.
Required visual elements: small controlled flame, heat source, flammable pictogram only, no explosion.
Additional card context from the rules: why: 蒸气、热源和氧气组合会形成火灾条件。 | review_question: 本轮是否先控制热源？.
Composition: vertical 2:3; stable post-response debrief scene; blank notebook or checklist foreground; controlled risk source in background.
Extra production rule: The scene should look like calm teaching review or correct post-response handling, not chaotic accident response.
Color and material: pale blue, white, gray-blue, transparent glass, soft reflections on the lab bench, small amount of orange/yellow only for safety warning symbols or flame.
Border and crop: the image may include a thin rounded rectangle card border and warm off-white paper margin; keep all important subjects away from the edge.

Strict negative prompt: no readable Chinese text, no readable English text, no readable numbers, no logo, no watermark, no brand name, no school emblem, no UI text, no readable bottle labels, no readable notebook content, no readable clipboard content, no title, no card frame text. Labels, forms, badges and screens must be blank, blurred, or meaningless lines only. No photorealistic style, no 3D render, no chibi style, no horror style, no gore, no injured people, no large explosion, no chaotic disaster, no distorted face, no extra fingers, no missing hands, no duplicated faces, no cluttered composition.
```

### D07 Debrief card | 腐蚀性液体操作

```text
Create ONE vertical no-text illustration for a laboratory safety board-game card.

Reference style: use the uploaded sample images as the main style reference. Match their clean academic watercolor look, blue-white palette, soft natural window light, transparent glassware, delicate anime-inspired characters, realistic chemistry lab equipment, rounded card-frame feeling, and calm educational tone.

Card ID: D07
Card type: Debrief card
Chinese card name: 腐蚀性液体操作
Visual goal: Show a teaching debrief illustration for "腐蚀性液体操作". Knowledge topic: 腐蚀防护. Correct action: 佩戴 PPE，控制加入速度。
Main character: Zhou Heng; young Chinese male graduate student, short black hair, clear goggles, white lab coat, blue inner shirt, blue nitrile gloves, skilled at hands-on experiments.
Scene environment: teaching debrief scene, controlled risk source, blank checklist, lab notebook, calm discussion.
Required visual elements: acid/base bottle, splash control, secondary tray, simple hazard pictogram with no text.
Additional card context from the rules: why: 飞溅会导致皮肤和眼部伤害。 | review_question: 飞溅后应先保护样品还是人员？.
Composition: vertical 2:3; stable post-response debrief scene; blank notebook or checklist foreground; controlled risk source in background.
Extra production rule: The scene should look like calm teaching review or correct post-response handling, not chaotic accident response.
Color and material: pale blue, white, gray-blue, transparent glass, soft reflections on the lab bench, small amount of orange/yellow only for safety warning symbols or flame.
Border and crop: the image may include a thin rounded rectangle card border and warm off-white paper margin; keep all important subjects away from the edge.

Strict negative prompt: no readable Chinese text, no readable English text, no readable numbers, no logo, no watermark, no brand name, no school emblem, no UI text, no readable bottle labels, no readable notebook content, no readable clipboard content, no title, no card frame text. Labels, forms, badges and screens must be blank, blurred, or meaningless lines only. No photorealistic style, no 3D render, no chibi style, no horror style, no gore, no injured people, no large explosion, no chaotic disaster, no distorted face, no extra fingers, no missing hands, no duplicated faces, no cluttered composition.
```

### D08 Debrief card | 玻璃器皿状态

```text
Create ONE vertical no-text illustration for a laboratory safety board-game card.

Reference style: use the uploaded sample images as the main style reference. Match their clean academic watercolor look, blue-white palette, soft natural window light, transparent glassware, delicate anime-inspired characters, realistic chemistry lab equipment, rounded card-frame feeling, and calm educational tone.

Card ID: D08
Card type: Debrief card
Chinese card name: 玻璃器皿状态
Visual goal: Show a teaching debrief illustration for "玻璃器皿状态". Knowledge topic: 器材检查. Correct action: 停用并更换器材。
Main character: Gu Ning; young Chinese female doctoral student, low ponytail or short hair, goggles, lab coat, calm posture, good at recording and verification.
Scene environment: teaching debrief scene, controlled risk source, blank checklist, lab notebook, calm discussion.
Required visual elements: cracked glassware or glass shards contained in a tray, no blood.
Additional card context from the rules: why: 裂纹会在压力、温度或外力下扩大。 | review_question: 裂纹器皿是否能低风险使用？.
Composition: vertical 2:3; stable post-response debrief scene; blank notebook or checklist foreground; controlled risk source in background.
Extra production rule: The scene should look like calm teaching review or correct post-response handling, not chaotic accident response.
Color and material: pale blue, white, gray-blue, transparent glass, soft reflections on the lab bench, small amount of orange/yellow only for safety warning symbols or flame.
Border and crop: the image may include a thin rounded rectangle card border and warm off-white paper margin; keep all important subjects away from the edge.

Strict negative prompt: no readable Chinese text, no readable English text, no readable numbers, no logo, no watermark, no brand name, no school emblem, no UI text, no readable bottle labels, no readable notebook content, no readable clipboard content, no title, no card frame text. Labels, forms, badges and screens must be blank, blurred, or meaningless lines only. No photorealistic style, no 3D render, no chibi style, no horror style, no gore, no injured people, no large explosion, no chaotic disaster, no distorted face, no extra fingers, no missing hands, no duplicated faces, no cluttered composition.
```

### D09 Debrief card | 气瓶固定

```text
Create ONE vertical no-text illustration for a laboratory safety board-game card.

Reference style: use the uploaded sample images as the main style reference. Match their clean academic watercolor look, blue-white palette, soft natural window light, transparent glassware, delicate anime-inspired characters, realistic chemistry lab equipment, rounded card-frame feeling, and calm educational tone.

Card ID: D09
Card type: Debrief card
Chinese card name: 气瓶固定
Visual goal: Show a teaching debrief illustration for "气瓶固定". Knowledge topic: 高压气体. Correct action: 固定气瓶，检查阀门和接头。
Main character: Cheng Yan; mature Chinese male doctoral student or teaching assistant, white lab coat, blue shirt, steady posture, coordinates laboratory safety.
Scene environment: teaching debrief scene, controlled risk source, blank checklist, lab notebook, calm discussion.
Required visual elements: gas cylinder, regulator, chain, hose connection.
Additional card context from the rules: why: 倾倒会导致高压冲击风险。 | review_question: 气瓶连接后还需要检查什么？.
Composition: vertical 2:3; stable post-response debrief scene; blank notebook or checklist foreground; controlled risk source in background.
Extra production rule: The scene should look like calm teaching review or correct post-response handling, not chaotic accident response.
Color and material: pale blue, white, gray-blue, transparent glass, soft reflections on the lab bench, small amount of orange/yellow only for safety warning symbols or flame.
Border and crop: the image may include a thin rounded rectangle card border and warm off-white paper margin; keep all important subjects away from the edge.

Strict negative prompt: no readable Chinese text, no readable English text, no readable numbers, no logo, no watermark, no brand name, no school emblem, no UI text, no readable bottle labels, no readable notebook content, no readable clipboard content, no title, no card frame text. Labels, forms, badges and screens must be blank, blurred, or meaningless lines only. No photorealistic style, no 3D render, no chibi style, no horror style, no gore, no injured people, no large explosion, no chaotic disaster, no distorted face, no extra fingers, no missing hands, no duplicated faces, no cluttered composition.
```

### D10 Debrief card | 通风橱门高度

```text
Create ONE vertical no-text illustration for a laboratory safety board-game card.

Reference style: use the uploaded sample images as the main style reference. Match their clean academic watercolor look, blue-white palette, soft natural window light, transparent glassware, delicate anime-inspired characters, realistic chemistry lab equipment, rounded card-frame feeling, and calm educational tone.

Card ID: D10
Card type: Debrief card
Chinese card name: 通风橱门高度
Visual goal: Show a teaching debrief illustration for "通风橱门高度". Knowledge topic: 通风橱使用. Correct action: 保持合适门高和工作距离。
Main character: Lin Cheng; young Chinese female graduate student, short black bob hair, clear goggles, white lab coat, blue inner shirt, often holding a notebook, careful and detail-oriented.
Scene environment: teaching debrief scene, controlled risk source, blank checklist, lab notebook, calm discussion.
Required visual elements: fume hood, airflow arrows as simple graphic marks, operation moved toward the hood.
Additional card context from the rules: why: 气流屏障依赖门高和操作位置。 | review_question: 通风橱门为什么不能一直全开？.
Composition: vertical 2:3; stable post-response debrief scene; blank notebook or checklist foreground; controlled risk source in background.
Extra production rule: The scene should look like calm teaching review or correct post-response handling, not chaotic accident response.
Color and material: pale blue, white, gray-blue, transparent glass, soft reflections on the lab bench, small amount of orange/yellow only for safety warning symbols or flame.
Border and crop: the image may include a thin rounded rectangle card border and warm off-white paper margin; keep all important subjects away from the edge.

Strict negative prompt: no readable Chinese text, no readable English text, no readable numbers, no logo, no watermark, no brand name, no school emblem, no UI text, no readable bottle labels, no readable notebook content, no readable clipboard content, no title, no card frame text. Labels, forms, badges and screens must be blank, blurred, or meaningless lines only. No photorealistic style, no 3D render, no chibi style, no horror style, no gore, no injured people, no large explosion, no chaotic disaster, no distorted face, no extra fingers, no missing hands, no duplicated faces, no cluttered composition.
```

### D11 Debrief card | 不相容物质

```text
Create ONE vertical no-text illustration for a laboratory safety board-game card.

Reference style: use the uploaded sample images as the main style reference. Match their clean academic watercolor look, blue-white palette, soft natural window light, transparent glassware, delicate anime-inspired characters, realistic chemistry lab equipment, rounded card-frame feeling, and calm educational tone.

Card ID: D11
Card type: Debrief card
Chinese card name: 不相容物质
Visual goal: Show a teaching debrief illustration for "不相容物质". Knowledge topic: 相容性. Correct action: 确认类别后分类处理。
Main character: Zhou Heng; young Chinese male graduate student, short black hair, clear goggles, white lab coat, blue inner shirt, blue nitrile gloves, skilled at hands-on experiments.
Scene environment: teaching debrief scene, controlled risk source, blank checklist, lab notebook, calm discussion.
Required visual elements: clean modern chemistry laboratory bench, glassware, safety equipment, bright natural light.
Additional card context from the rules: why: 混放可能产生热、气体或毒性产物。 | review_question: 不确定相容性时应怎么做？.
Composition: vertical 2:3; stable post-response debrief scene; blank notebook or checklist foreground; controlled risk source in background.
Extra production rule: The scene should look like calm teaching review or correct post-response handling, not chaotic accident response.
Color and material: pale blue, white, gray-blue, transparent glass, soft reflections on the lab bench, small amount of orange/yellow only for safety warning symbols or flame.
Border and crop: the image may include a thin rounded rectangle card border and warm off-white paper margin; keep all important subjects away from the edge.

Strict negative prompt: no readable Chinese text, no readable English text, no readable numbers, no logo, no watermark, no brand name, no school emblem, no UI text, no readable bottle labels, no readable notebook content, no readable clipboard content, no title, no card frame text. Labels, forms, badges and screens must be blank, blurred, or meaningless lines only. No photorealistic style, no 3D render, no chibi style, no horror style, no gore, no injured people, no large explosion, no chaotic disaster, no distorted face, no extra fingers, no missing hands, no duplicated faces, no cluttered composition.
```

### D12 Debrief card | 无人值守

```text
Create ONE vertical no-text illustration for a laboratory safety board-game card.

Reference style: use the uploaded sample images as the main style reference. Match their clean academic watercolor look, blue-white palette, soft natural window light, transparent glassware, delicate anime-inspired characters, realistic chemistry lab equipment, rounded card-frame feeling, and calm educational tone.

Card ID: D12
Card type: Debrief card
Chinese card name: 无人值守
Visual goal: Show a teaching debrief illustration for "无人值守". Knowledge topic: 值守要求. Correct action: 安排监控或暂停高风险步骤。
Main character: Gu Ning; young Chinese female doctoral student, low ponytail or short hair, goggles, lab coat, calm posture, good at recording and verification.
Scene environment: teaching debrief scene, controlled risk source, blank checklist, lab notebook, calm discussion.
Required visual elements: clean modern chemistry laboratory bench, glassware, safety equipment, bright natural light.
Additional card context from the rules: why: 异常趋势需要及时发现。 | review_question: 哪些操作不适合无人值守？.
Composition: vertical 2:3; stable post-response debrief scene; blank notebook or checklist foreground; controlled risk source in background.
Extra production rule: The scene should look like calm teaching review or correct post-response handling, not chaotic accident response.
Color and material: pale blue, white, gray-blue, transparent glass, soft reflections on the lab bench, small amount of orange/yellow only for safety warning symbols or flame.
Border and crop: the image may include a thin rounded rectangle card border and warm off-white paper margin; keep all important subjects away from the edge.

Strict negative prompt: no readable Chinese text, no readable English text, no readable numbers, no logo, no watermark, no brand name, no school emblem, no UI text, no readable bottle labels, no readable notebook content, no readable clipboard content, no title, no card frame text. Labels, forms, badges and screens must be blank, blurred, or meaningless lines only. No photorealistic style, no 3D render, no chibi style, no horror style, no gore, no injured people, no large explosion, no chaotic disaster, no distorted face, no extra fingers, no missing hands, no duplicated faces, no cluttered composition.
```

### D13 Debrief card | 人员暴露优先

```text
Create ONE vertical no-text illustration for a laboratory safety board-game card.

Reference style: use the uploaded sample images as the main style reference. Match their clean academic watercolor look, blue-white palette, soft natural window light, transparent glassware, delicate anime-inspired characters, realistic chemistry lab equipment, rounded card-frame feeling, and calm educational tone.

Card ID: D13
Card type: Debrief card
Chinese card name: 人员暴露优先
Visual goal: Show a teaching debrief illustration for "人员暴露优先". Knowledge topic: 暴露处置. Correct action: 立即冲洗、撤离或上报。
Main character: Cheng Yan; mature Chinese male doctoral student or teaching assistant, white lab coat, blue shirt, steady posture, coordinates laboratory safety.
Scene environment: teaching debrief scene, controlled risk source, blank checklist, lab notebook, calm discussion.
Required visual elements: potential exposure risk shown by distance, vapor, or an uncapped container, without injury.
Additional card context from the rules: why: 延误会扩大伤害。 | review_question: 暴露后第一优先级是什么？.
Composition: vertical 2:3; stable post-response debrief scene; blank notebook or checklist foreground; controlled risk source in background.
Extra production rule: The scene should look like calm teaching review or correct post-response handling, not chaotic accident response.
Color and material: pale blue, white, gray-blue, transparent glass, soft reflections on the lab bench, small amount of orange/yellow only for safety warning symbols or flame.
Border and crop: the image may include a thin rounded rectangle card border and warm off-white paper margin; keep all important subjects away from the edge.

Strict negative prompt: no readable Chinese text, no readable English text, no readable numbers, no logo, no watermark, no brand name, no school emblem, no UI text, no readable bottle labels, no readable notebook content, no readable clipboard content, no title, no card frame text. Labels, forms, badges and screens must be blank, blurred, or meaningless lines only. No photorealistic style, no 3D render, no chibi style, no horror style, no gore, no injured people, no large explosion, no chaotic disaster, no distorted face, no extra fingers, no missing hands, no duplicated faces, no cluttered composition.
```

### D14 Debrief card | 未知气味

```text
Create ONE vertical no-text illustration for a laboratory safety board-game card.

Reference style: use the uploaded sample images as the main style reference. Match their clean academic watercolor look, blue-white palette, soft natural window light, transparent glassware, delicate anime-inspired characters, realistic chemistry lab equipment, rounded card-frame feeling, and calm educational tone.

Card ID: D14
Card type: Debrief card
Chinese card name: 未知气味
Visual goal: Show a teaching debrief illustration for "未知气味". Knowledge topic: 吸入暴露. Correct action: 加强通风、撤离、上报。
Main character: Lin Cheng; young Chinese female graduate student, short black bob hair, clear goggles, white lab coat, blue inner shirt, often holding a notebook, careful and detail-oriented.
Scene environment: teaching debrief scene, controlled risk source, blank checklist, lab notebook, calm discussion.
Required visual elements: unknown transparent reagent bottle and cautious inspection gesture.
Additional card context from the rules: why: 未知挥发物可能有毒或刺激性。 | review_question: 闻到异常气味时应靠近确认吗？.
Composition: vertical 2:3; stable post-response debrief scene; blank notebook or checklist foreground; controlled risk source in background.
Extra production rule: The scene should look like calm teaching review or correct post-response handling, not chaotic accident response.
Color and material: pale blue, white, gray-blue, transparent glass, soft reflections on the lab bench, small amount of orange/yellow only for safety warning symbols or flame.
Border and crop: the image may include a thin rounded rectangle card border and warm off-white paper margin; keep all important subjects away from the edge.

Strict negative prompt: no readable Chinese text, no readable English text, no readable numbers, no logo, no watermark, no brand name, no school emblem, no UI text, no readable bottle labels, no readable notebook content, no readable clipboard content, no title, no card frame text. Labels, forms, badges and screens must be blank, blurred, or meaningless lines only. No photorealistic style, no 3D render, no chibi style, no horror style, no gore, no injured people, no large explosion, no chaotic disaster, no distorted face, no extra fingers, no missing hands, no duplicated faces, no cluttered composition.
```

### D15 Debrief card | 小型火情

```text
Create ONE vertical no-text illustration for a laboratory safety board-game card.

Reference style: use the uploaded sample images as the main style reference. Match their clean academic watercolor look, blue-white palette, soft natural window light, transparent glassware, delicate anime-inspired characters, realistic chemistry lab equipment, rounded card-frame feeling, and calm educational tone.

Card ID: D15
Card type: Debrief card
Chinese card name: 小型火情
Visual goal: Show a teaching debrief illustration for "小型火情". Knowledge topic: 初期火情. Correct action: 切断热源，选择合适灭火方式。
Main character: Zhou Heng; young Chinese male graduate student, short black hair, clear goggles, white lab coat, blue inner shirt, blue nitrile gloves, skilled at hands-on experiments.
Scene environment: teaching debrief scene, controlled risk source, blank checklist, lab notebook, calm discussion.
Required visual elements: small controlled flame, heat source, flammable pictogram only, no explosion.
Additional card context from the rules: why: 错误灭火可能扩大事故。 | review_question: 什么情况下应撤离而不是灭火？.
Composition: vertical 2:3; stable post-response debrief scene; blank notebook or checklist foreground; controlled risk source in background.
Extra production rule: The scene should look like calm teaching review or correct post-response handling, not chaotic accident response.
Color and material: pale blue, white, gray-blue, transparent glass, soft reflections on the lab bench, small amount of orange/yellow only for safety warning symbols or flame.
Border and crop: the image may include a thin rounded rectangle card border and warm off-white paper margin; keep all important subjects away from the edge.

Strict negative prompt: no readable Chinese text, no readable English text, no readable numbers, no logo, no watermark, no brand name, no school emblem, no UI text, no readable bottle labels, no readable notebook content, no readable clipboard content, no title, no card frame text. Labels, forms, badges and screens must be blank, blurred, or meaningless lines only. No photorealistic style, no 3D render, no chibi style, no horror style, no gore, no injured people, no large explosion, no chaotic disaster, no distorted face, no extra fingers, no missing hands, no duplicated faces, no cluttered composition.
```

### D16 Debrief card | 锐器与通道

```text
Create ONE vertical no-text illustration for a laboratory safety board-game card.

Reference style: use the uploaded sample images as the main style reference. Match their clean academic watercolor look, blue-white palette, soft natural window light, transparent glassware, delicate anime-inspired characters, realistic chemistry lab equipment, rounded card-frame feeling, and calm educational tone.

Card ID: D16
Card type: Debrief card
Chinese card name: 锐器与通道
Visual goal: Show a teaching debrief illustration for "锐器与通道". Knowledge topic: 公共安全. Correct action: 锐器专收，通道保持畅通。
Main character: Gu Ning; young Chinese female doctoral student, low ponytail or short hair, goggles, lab coat, calm posture, good at recording and verification.
Scene environment: teaching debrief scene, controlled risk source, blank checklist, lab notebook, calm discussion.
Required visual elements: sharp object or broken glass in a dedicated container, no injury.
Additional card context from the rules: why: 安全管理也包括后续人员。 | review_question: 收尾时哪些风险最容易被忽视？.
Composition: vertical 2:3; stable post-response debrief scene; blank notebook or checklist foreground; controlled risk source in background.
Extra production rule: The scene should look like calm teaching review or correct post-response handling, not chaotic accident response.
Color and material: pale blue, white, gray-blue, transparent glass, soft reflections on the lab bench, small amount of orange/yellow only for safety warning symbols or flame.
Border and crop: the image may include a thin rounded rectangle card border and warm off-white paper margin; keep all important subjects away from the edge.

Strict negative prompt: no readable Chinese text, no readable English text, no readable numbers, no logo, no watermark, no brand name, no school emblem, no UI text, no readable bottle labels, no readable notebook content, no readable clipboard content, no title, no card frame text. Labels, forms, badges and screens must be blank, blurred, or meaningless lines only. No photorealistic style, no 3D render, no chibi style, no horror style, no gore, no injured people, no large explosion, no chaotic disaster, no distorted face, no extra fingers, no missing hands, no duplicated faces, no cluttered composition.
```

### D17 Debrief card | 能量输入控制

```text
Create ONE vertical no-text illustration for a laboratory safety board-game card.

Reference style: use the uploaded sample images as the main style reference. Match their clean academic watercolor look, blue-white palette, soft natural window light, transparent glassware, delicate anime-inspired characters, realistic chemistry lab equipment, rounded card-frame feeling, and calm educational tone.

Card ID: D17
Card type: Debrief card
Chinese card name: 能量输入控制
Visual goal: Show a teaching debrief illustration for "能量输入控制". Knowledge topic: 热源控制. Correct action: 降温、断电、监测并报告。
Main character: Cheng Yan; mature Chinese male doctoral student or teaching assistant, white lab coat, blue shirt, steady posture, coordinates laboratory safety.
Scene environment: teaching debrief scene, controlled risk source, blank checklist, lab notebook, calm discussion.
Required visual elements: heating mantle, hot plate, warm glassware, heat source control.
Additional card context from the rules: why: 能量输入会推动事故升级。 | review_question: 温度异常时能否继续加热观察？.
Composition: vertical 2:3; stable post-response debrief scene; blank notebook or checklist foreground; controlled risk source in background.
Extra production rule: The scene should look like calm teaching review or correct post-response handling, not chaotic accident response.
Color and material: pale blue, white, gray-blue, transparent glass, soft reflections on the lab bench, small amount of orange/yellow only for safety warning symbols or flame.
Border and crop: the image may include a thin rounded rectangle card border and warm off-white paper margin; keep all important subjects away from the edge.

Strict negative prompt: no readable Chinese text, no readable English text, no readable numbers, no logo, no watermark, no brand name, no school emblem, no UI text, no readable bottle labels, no readable notebook content, no readable clipboard content, no title, no card frame text. Labels, forms, badges and screens must be blank, blurred, or meaningless lines only. No photorealistic style, no 3D render, no chibi style, no horror style, no gore, no injured people, no large explosion, no chaotic disaster, no distorted face, no extra fingers, no missing hands, no duplicated faces, no cluttered composition.
```

### D18 Debrief card | 设备收尾

```text
Create ONE vertical no-text illustration for a laboratory safety board-game card.

Reference style: use the uploaded sample images as the main style reference. Match their clean academic watercolor look, blue-white palette, soft natural window light, transparent glassware, delicate anime-inspired characters, realistic chemistry lab equipment, rounded card-frame feeling, and calm educational tone.

Card ID: D18
Card type: Debrief card
Chinese card name: 设备收尾
Visual goal: Show a teaching debrief illustration for "设备收尾". Knowledge topic: 断电记录. Correct action: 断电、检查、记录状态。
Main character: Lin Cheng; young Chinese female graduate student, short black bob hair, clear goggles, white lab coat, blue inner shirt, often holding a notebook, careful and detail-oriented.
Scene environment: teaching debrief scene, controlled risk source, blank checklist, lab notebook, calm discussion.
Required visual elements: clamps, stands, condenser, heating mantle, instrument panel, physically plausible equipment.
Additional card context from the rules: why: 下一位使用者需要明确信息。 | review_question: 交接时哪些设备状态必须说明？.
Composition: vertical 2:3; stable post-response debrief scene; blank notebook or checklist foreground; controlled risk source in background.
Extra production rule: The scene should look like calm teaching review or correct post-response handling, not chaotic accident response.
Color and material: pale blue, white, gray-blue, transparent glass, soft reflections on the lab bench, small amount of orange/yellow only for safety warning symbols or flame.
Border and crop: the image may include a thin rounded rectangle card border and warm off-white paper margin; keep all important subjects away from the edge.

Strict negative prompt: no readable Chinese text, no readable English text, no readable numbers, no logo, no watermark, no brand name, no school emblem, no UI text, no readable bottle labels, no readable notebook content, no readable clipboard content, no title, no card frame text. Labels, forms, badges and screens must be blank, blurred, or meaningless lines only. No photorealistic style, no 3D render, no chibi style, no horror style, no gore, no injured people, no large explosion, no chaotic disaster, no distorted face, no extra fingers, no missing hands, no duplicated faces, no cluttered composition.
```

### D19 Debrief card | 容器密封

```text
Create ONE vertical no-text illustration for a laboratory safety board-game card.

Reference style: use the uploaded sample images as the main style reference. Match their clean academic watercolor look, blue-white palette, soft natural window light, transparent glassware, delicate anime-inspired characters, realistic chemistry lab equipment, rounded card-frame feeling, and calm educational tone.

Card ID: D19
Card type: Debrief card
Chinese card name: 容器密封
Visual goal: Show a teaching debrief illustration for "容器密封". Knowledge topic: 容器管理. Correct action: 拧紧瓶盖并检查容器匹配。
Main character: Zhou Heng; young Chinese male graduate student, short black hair, clear goggles, white lab coat, blue inner shirt, blue nitrile gloves, skilled at hands-on experiments.
Scene environment: teaching debrief scene, controlled risk source, blank checklist, lab notebook, calm discussion.
Required visual elements: secondary tray, absorbent pad, container boundary preventing spread.
Additional card context from the rules: why: 泄漏常从小疏忽开始。 | review_question: 临时容器是否也需要检查密封？.
Composition: vertical 2:3; stable post-response debrief scene; blank notebook or checklist foreground; controlled risk source in background.
Extra production rule: The scene should look like calm teaching review or correct post-response handling, not chaotic accident response.
Color and material: pale blue, white, gray-blue, transparent glass, soft reflections on the lab bench, small amount of orange/yellow only for safety warning symbols or flame.
Border and crop: the image may include a thin rounded rectangle card border and warm off-white paper margin; keep all important subjects away from the edge.

Strict negative prompt: no readable Chinese text, no readable English text, no readable numbers, no logo, no watermark, no brand name, no school emblem, no UI text, no readable bottle labels, no readable notebook content, no readable clipboard content, no title, no card frame text. Labels, forms, badges and screens must be blank, blurred, or meaningless lines only. No photorealistic style, no 3D render, no chibi style, no horror style, no gore, no injured people, no large explosion, no chaotic disaster, no distorted face, no extra fingers, no missing hands, no duplicated faces, no cluttered composition.
```

### D20 Debrief card | 离心配平

```text
Create ONE vertical no-text illustration for a laboratory safety board-game card.

Reference style: use the uploaded sample images as the main style reference. Match their clean academic watercolor look, blue-white palette, soft natural window light, transparent glassware, delicate anime-inspired characters, realistic chemistry lab equipment, rounded card-frame feeling, and calm educational tone.

Card ID: D20
Card type: Debrief card
Chinese card name: 离心配平
Visual goal: Show a teaching debrief illustration for "离心配平". Knowledge topic: 离心安全. Correct action: 重新配平并检查转子。
Main character: Gu Ning; young Chinese female doctoral student, low ponytail or short hair, goggles, lab coat, calm posture, good at recording and verification.
Scene environment: teaching debrief scene, controlled risk source, blank checklist, lab notebook, calm discussion.
Required visual elements: team balancing safety and efficiency, two visible decision paths.
Additional card context from the rules: why: 不平衡会造成设备损坏和样品飞散。 | review_question: 离心机启动前要看哪两项？.
Composition: vertical 2:3; stable post-response debrief scene; blank notebook or checklist foreground; controlled risk source in background.
Extra production rule: The scene should look like calm teaching review or correct post-response handling, not chaotic accident response.
Color and material: pale blue, white, gray-blue, transparent glass, soft reflections on the lab bench, small amount of orange/yellow only for safety warning symbols or flame.
Border and crop: the image may include a thin rounded rectangle card border and warm off-white paper margin; keep all important subjects away from the edge.

Strict negative prompt: no readable Chinese text, no readable English text, no readable numbers, no logo, no watermark, no brand name, no school emblem, no UI text, no readable bottle labels, no readable notebook content, no readable clipboard content, no title, no card frame text. Labels, forms, badges and screens must be blank, blurred, or meaningless lines only. No photorealistic style, no 3D render, no chibi style, no horror style, no gore, no injured people, no large explosion, no chaotic disaster, no distorted face, no extra fingers, no missing hands, no duplicated faces, no cluttered composition.
```

### D21 Debrief card | 旋蒸夹具

```text
Create ONE vertical no-text illustration for a laboratory safety board-game card.

Reference style: use the uploaded sample images as the main style reference. Match their clean academic watercolor look, blue-white palette, soft natural window light, transparent glassware, delicate anime-inspired characters, realistic chemistry lab equipment, rounded card-frame feeling, and calm educational tone.

Card ID: D21
Card type: Debrief card
Chinese card name: 旋蒸夹具
Visual goal: Show a teaching debrief illustration for "旋蒸夹具". Knowledge topic: 夹具固定. Correct action: 检查夹具、瓶口和转速。
Main character: Cheng Yan; mature Chinese male doctoral student or teaching assistant, white lab coat, blue shirt, steady posture, coordinates laboratory safety.
Scene environment: teaching debrief scene, controlled risk source, blank checklist, lab notebook, calm discussion.
Required visual elements: tightening clamp, stabilizing stand, securing tubing or vessel.
Additional card context from the rules: why: 旋转和负压会放大松动风险。 | review_question: 旋蒸前最容易漏查什么？.
Composition: vertical 2:3; stable post-response debrief scene; blank notebook or checklist foreground; controlled risk source in background.
Extra production rule: The scene should look like calm teaching review or correct post-response handling, not chaotic accident response.
Color and material: pale blue, white, gray-blue, transparent glass, soft reflections on the lab bench, small amount of orange/yellow only for safety warning symbols or flame.
Border and crop: the image may include a thin rounded rectangle card border and warm off-white paper margin; keep all important subjects away from the edge.

Strict negative prompt: no readable Chinese text, no readable English text, no readable numbers, no logo, no watermark, no brand name, no school emblem, no UI text, no readable bottle labels, no readable notebook content, no readable clipboard content, no title, no card frame text. Labels, forms, badges and screens must be blank, blurred, or meaningless lines only. No photorealistic style, no 3D render, no chibi style, no horror style, no gore, no injured people, no large explosion, no chaotic disaster, no distorted face, no extra fingers, no missing hands, no duplicated faces, no cluttered composition.
```

### D22 Debrief card | 废液容量

```text
Create ONE vertical no-text illustration for a laboratory safety board-game card.

Reference style: use the uploaded sample images as the main style reference. Match their clean academic watercolor look, blue-white palette, soft natural window light, transparent glassware, delicate anime-inspired characters, realistic chemistry lab equipment, rounded card-frame feeling, and calm educational tone.

Card ID: D22
Card type: Debrief card
Chinese card name: 废液容量
Visual goal: Show a teaching debrief illustration for "废液容量". Knowledge topic: 容量控制. Correct action: 及时更换容器并记录。
Main character: Lin Cheng; young Chinese female graduate student, short black bob hair, clear goggles, white lab coat, blue inner shirt, often holding a notebook, careful and detail-oriented.
Scene environment: teaching debrief scene, controlled risk source, blank checklist, lab notebook, calm discussion.
Required visual elements: waste bottle, sorted waste container, cleanup action, blank label only.
Additional card context from the rules: why: 过满会增加溢出和混放风险。 | review_question: 废液桶满到什么程度应更换？.
Composition: vertical 2:3; stable post-response debrief scene; blank notebook or checklist foreground; controlled risk source in background.
Extra production rule: The scene should look like calm teaching review or correct post-response handling, not chaotic accident response.
Color and material: pale blue, white, gray-blue, transparent glass, soft reflections on the lab bench, small amount of orange/yellow only for safety warning symbols or flame.
Border and crop: the image may include a thin rounded rectangle card border and warm off-white paper margin; keep all important subjects away from the edge.

Strict negative prompt: no readable Chinese text, no readable English text, no readable numbers, no logo, no watermark, no brand name, no school emblem, no UI text, no readable bottle labels, no readable notebook content, no readable clipboard content, no title, no card frame text. Labels, forms, badges and screens must be blank, blurred, or meaningless lines only. No photorealistic style, no 3D render, no chibi style, no horror style, no gore, no injured people, no large explosion, no chaotic disaster, no distorted face, no extra fingers, no missing hands, no duplicated faces, no cluttered composition.
```

### D23 Debrief card | 未知粉末

```text
Create ONE vertical no-text illustration for a laboratory safety board-game card.

Reference style: use the uploaded sample images as the main style reference. Match their clean academic watercolor look, blue-white palette, soft natural window light, transparent glassware, delicate anime-inspired characters, realistic chemistry lab equipment, rounded card-frame feeling, and calm educational tone.

Card ID: D23
Card type: Debrief card
Chinese card name: 未知粉末
Visual goal: Show a teaching debrief illustration for "未知粉末". Knowledge topic: 未知物处置. Correct action: 隔离、撤离、上报。
Main character: Zhou Heng; young Chinese male graduate student, short black hair, clear goggles, white lab coat, blue inner shirt, blue nitrile gloves, skilled at hands-on experiments.
Scene environment: teaching debrief scene, controlled risk source, blank checklist, lab notebook, calm discussion.
Required visual elements: unknown transparent reagent bottle and cautious inspection gesture.
Additional card context from the rules: why: 吸入和接触风险无法立即判断。 | review_question: 为什么不能直接扫掉未知粉末？.
Composition: vertical 2:3; stable post-response debrief scene; blank notebook or checklist foreground; controlled risk source in background.
Extra production rule: The scene should look like calm teaching review or correct post-response handling, not chaotic accident response.
Color and material: pale blue, white, gray-blue, transparent glass, soft reflections on the lab bench, small amount of orange/yellow only for safety warning symbols or flame.
Border and crop: the image may include a thin rounded rectangle card border and warm off-white paper margin; keep all important subjects away from the edge.

Strict negative prompt: no readable Chinese text, no readable English text, no readable numbers, no logo, no watermark, no brand name, no school emblem, no UI text, no readable bottle labels, no readable notebook content, no readable clipboard content, no title, no card frame text. Labels, forms, badges and screens must be blank, blurred, or meaningless lines only. No photorealistic style, no 3D render, no chibi style, no horror style, no gore, no injured people, no large explosion, no chaotic disaster, no distorted face, no extra fingers, no missing hands, no duplicated faces, no cluttered composition.
```

### D24 Debrief card | 复盘闭环

```text
Create ONE vertical no-text illustration for a laboratory safety board-game card.

Reference style: use the uploaded sample images as the main style reference. Match their clean academic watercolor look, blue-white palette, soft natural window light, transparent glassware, delicate anime-inspired characters, realistic chemistry lab equipment, rounded card-frame feeling, and calm educational tone.

Card ID: D24
Card type: Debrief card
Chinese card name: 复盘闭环
Visual goal: Show a teaching debrief illustration for "复盘闭环". Knowledge topic: 持续改进. Correct action: 记录原因、措施和责任岗位。
Main character: Gu Ning; young Chinese female doctoral student, low ponytail or short hair, goggles, lab coat, calm posture, good at recording and verification.
Scene environment: teaching debrief scene, controlled risk source, blank checklist, lab notebook, calm discussion.
Required visual elements: clean modern chemistry laboratory bench, glassware, safety equipment, bright natural light.
Additional card context from the rules: why: 没有措施的复盘难以防止重复发生。 | review_question: 本轮风险以后如何避免？.
Composition: vertical 2:3; stable post-response debrief scene; blank notebook or checklist foreground; controlled risk source in background.
Extra production rule: The scene should look like calm teaching review or correct post-response handling, not chaotic accident response.
Color and material: pale blue, white, gray-blue, transparent glass, soft reflections on the lab bench, small amount of orange/yellow only for safety warning symbols or flame.
Border and crop: the image may include a thin rounded rectangle card border and warm off-white paper margin; keep all important subjects away from the edge.

Strict negative prompt: no readable Chinese text, no readable English text, no readable numbers, no logo, no watermark, no brand name, no school emblem, no UI text, no readable bottle labels, no readable notebook content, no readable clipboard content, no title, no card frame text. Labels, forms, badges and screens must be blank, blurred, or meaningless lines only. No photorealistic style, no 3D render, no chibi style, no horror style, no gore, no injured people, no large explosion, no chaotic disaster, no distorted face, no extra fingers, no missing hands, no duplicated faces, no cluttered composition.
```
