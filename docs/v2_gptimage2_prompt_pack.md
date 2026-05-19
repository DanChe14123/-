# v2 gptimage2 无文字插画提示词包

## 1. 使用规则

### Writing Guidance

每次只生成一张插画。提示词只要求画面，不要求模型生成中文。生成后把中文标题、编号和说明全部放到后期模板中。

统一负面要求：

```text
No Chinese text, no English text, no readable labels, no watermark, no logo, no distorted hands, no extra fingers, no horror style, no photorealistic accident injury, no cluttered composition.
```

统一风格句：

```text
Clean educational cartoon illustration, modern chemistry laboratory, soft natural lighting, semi-realistic anime-inspired characters, clear safety training scene, high-quality board game card art, neat composition, large central subject, no readable text.
```

## 2. E02 试剂瓶标签模糊

```text
Create a vertical board game card illustration only, without any text. Scene: a young Chinese graduate student in a white lab coat stands at a clean chemistry lab bench, holding a reagent bottle with a visibly blurred blank label and a small notebook in the other hand. The character looks cautious and uncertain, not panicked. Background: shelves with glassware, test tubes, and a tidy laboratory bench. Key visual risk: the bottle identity cannot be confirmed because the label is smudged, but the label must contain no readable words. Style: clean educational cartoon illustration, modern chemistry laboratory, soft natural lighting, semi-realistic anime-inspired character, high-quality board game card art, neat composition, large central subject, no readable text.
Negative: No Chinese text, no English text, no readable labels, no watermark, no logo, no distorted hands, no extra fingers, no horror style, no cluttered composition.
```

## 3. E05 开放环境转移挥发性溶剂

```text
Create a vertical board game card illustration only, without any text. Scene: a young Chinese male graduate student is transferring a clear volatile solvent from one bottle into a beaker on an open lab bench instead of inside a fume hood. He wears goggles and gloves, but the setup is visibly not ideal. A fume hood is visible in the background, unused. Key visual risk: open-air solvent transfer, possible vapor exposure and fire risk. Use blank hazard pictograms only, no readable labels. Style: clean educational cartoon illustration, modern chemistry laboratory, soft natural lighting, semi-realistic anime-inspired character, high-quality board game card art, neat composition, large central subject, no readable text.
Negative: No Chinese text, no English text, no readable labels, no watermark, no logo, no distorted hands, no extra fingers, no fire explosion, no horror style, no cluttered composition.
```

## 4. E15 实验台出现小型明火

```text
Create a vertical board game card illustration only, without any text. Scene: a chemistry lab bench with a small controlled flame appearing near a heating device and a solvent container placed too close. A lab student in goggles and lab coat is stepping back and preparing to cut off the heat source. The scene should feel urgent but safe for education, not disastrous. Key visual risk: early-stage small flame, nearby flammable material, need to shut down heat and respond correctly. Style: clean educational cartoon illustration, modern chemistry laboratory, soft natural lighting, semi-realistic anime-inspired character, high-quality board game card art, neat composition, large central subject, no readable text.
Negative: No Chinese text, no English text, no readable labels, no watermark, no logo, no distorted hands, no extra fingers, no large explosion, no injured people, no horror style, no cluttered composition.
```

## 5. T03 加热回流装置搭建

```text
Create a vertical board game card illustration only, without any text. Scene: a student carefully assembling a reflux setup in a chemistry lab, checking clamps, condenser tubing, round-bottom flask, and heating mantle. The setup looks mostly correct and educational. The student is focused and calm. Key visual theme: safe preparation and equipment inspection before heating. Style: clean educational cartoon illustration, modern chemistry laboratory, soft natural lighting, semi-realistic anime-inspired character, high-quality board game card art, neat composition, large central subject, no readable text.
Negative: No Chinese text, no English text, no readable labels, no watermark, no logo, no distorted glassware, no impossible tubing, no extra fingers, no cluttered composition.
```

## 6. A01 核对标签

```text
Create a vertical board game card illustration only, without any text. Scene: close-up action demonstration of gloved hands comparing a reagent bottle with a laboratory notebook and a blank inventory sheet. The focus is on careful verification. The bottle label is blank or blurred with no readable characters. Key visual theme: verify identity before use. Style: clean educational cartoon illustration, modern chemistry laboratory, soft natural lighting, high-quality board game card art, neat composition, large central subject, no readable text.
Negative: No Chinese text, no English text, no readable labels, no watermark, no logo, no distorted hands, no extra fingers, no cluttered composition.
```

## 7. A08 撤离与警戒

```text
Create a vertical board game card illustration only, without any text. Scene: a safety officer in lab coat and goggles calmly guiding two people away from a lab bench while placing a simple warning stand or barrier tape near the risk area. The risk area is visible but not graphic, with a small spill or suspicious container in the background. Key visual theme: evacuate unrelated people and guard the area. Style: clean educational cartoon illustration, modern chemistry laboratory corridor and lab entrance, soft natural lighting, semi-realistic anime-inspired characters, high-quality board game card art, neat composition, no readable text.
Negative: No Chinese text, no English text, no readable signs, no watermark, no logo, no panic crowd, no injury, no horror style, no cluttered composition.
```

## 8. P01 安全员

```text
Create a vertical board game card illustration only, without any text. Scene: a confident lab safety officer standing in a modern chemistry lab, wearing lab coat, goggles, gloves, and holding a clipboard with blank sheets. The character is pointing toward a risk area while calmly coordinating teammates. Key visual theme: risk judgment and team coordination. Style: clean educational cartoon illustration, modern chemistry laboratory, soft natural lighting, semi-realistic anime-inspired character, high-quality board game card art, neat composition, large central subject, no readable text.
Negative: No Chinese text, no English text, no readable clipboard content, no watermark, no logo, no distorted hands, no extra fingers, no cluttered composition.
```

## 9. R02 实验操作者

```text
Create a vertical board game card illustration only, without any text. Scene: a young Chinese graduate student as the experiment operator, wearing lab coat, goggles, and gloves, standing beside a clean bench with glassware and instruments. The character looks focused and reliable, holding a small tool or adjusting a clamp. Key visual theme: precise experimental operation with safety awareness. Style: clean educational cartoon illustration, modern chemistry laboratory, soft natural lighting, semi-realistic anime-inspired character, high-quality board game card art, neat composition, full-body or half-body portrait, no readable text.
Negative: No Chinese text, no English text, no readable labels, no watermark, no logo, no distorted hands, no extra fingers, no cluttered composition.
```

