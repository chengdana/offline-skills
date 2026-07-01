---
name: personal-official-writing-workflow
description: Use when the user wants to train a personalized Chinese official-material writing style from their own drafts, revisions, communications, summaries, reports, notices, speeches, or government/enterprise materials, then draft or revise new materials with both personal voice and formal document standards.
---

# Personal Official Writing Workflow

## Overview

Build a reusable writing workflow for Chinese official materials by combining two separate capabilities:

- `learning-personal-writing-style`: learn how the user writes and revises from their own samples.
- `drafting-official-materials`: enforce document type, official structure, institutional tone, and quality checks.

This is not model fine-tuning. It is a local skill workflow based on samples, style profiles, revision rules, and official-material writing patterns.

## When To Use

Use this skill for:

- training a personal style profile from communications, summaries, reports, notices, speeches, research reports, briefings, or before/after edits
- drafting a new official material in the user's learned style
- revising an AI draft so it is both more like the user and more compliant with official-material conventions
- teaching a beginner how to set up a local writing project and use skills for office writing

Do not use this skill to imitate third-party authors without permission, fabricate policy basis, invent leaders' names, invent data, or replace human review for sensitive official documents.

## Required Sub-Skills

Load these only when the task reaches the matching stage:

| Stage | Required skill | Purpose |
|-|-|-|
| Train or update style | `learning-personal-writing-style` | Extract reusable style rules from user-owned samples and edits |
| Draft or revise official materials | `drafting-official-materials` | Identify document type, structure the material, and check official tone/format |

## Recommended Project Folder

When the user has no existing folder, suggest a beginner-friendly Chinese folder setup instead of an English technical tree:

```text
D盘 / 程大拿写作
```

Inside the project folder, create genre folders such as:

```text
活动通讯稿
年度工作总结
向上级汇报材料
工作通知
领导讲话稿
调研报告
```

Inside each genre folder, suggest four simple subfolders:

```text
我写过的定稿
AI原始初稿
AI规范修订稿
我最终修改稿
```

For AI draft vs user-edited groups, keep matching sequence numbers or titles:

```text
001-支行客户活动通讯稿-AI原始初稿.docx
001-支行客户活动通讯稿-AI规范修订稿.docx
001-支行客户活动通讯稿-AI规范修订稿（拟定）.docx
001-支行客户活动通讯稿-我最终修改稿.docx
```

Same number means the files belong to the same writing task. The archived `AI规范修订稿` must not be edited directly; it is the AI official-standard trace version. Create an editable working copy named `AI规范修订稿（拟定）` in the material-type folder root. The user edits that working copy. When the user says a short confirmation such as `已定稿，请帮我归档`, infer the matching working copy from the current task, same sequence number, material type folder, or most recent unarchived `（拟定）` file. Save or move it into `我最终修改稿` with the standard final filename. Ask the user to choose only if multiple candidate `（拟定）` files exist or the current task cannot be inferred. Do not make the user retype the full source path or target path. The `AI规范修订稿` vs `我最终修改稿` pair is the highest-value training material because it reveals what the user changed after the official-material pass. The `AI原始初稿` vs `AI规范修订稿` pair is mainly for checking what the official-material sub-skill changed, not for personal-style learning. Keep genres separate. Do not mix a newsletter-style communication, a work summary, a formal report, and a speech into one undifferentiated profile unless the user explicitly wants a rough starter profile.

## Workflow

1. **Set up samples**
   - Ask the user to place their own completed materials into the matching genre folder, then into `我写过的定稿`.
   - Prefer 5-20 samples per genre. With 3-5 samples, mark confidence as starter-level.
   - Put AI-generated and user-edited files into `AI原始初稿`, `AI规范修订稿`, and `我最终修改稿`, using the same sequence number or title for related files. Editable `AI规范修订稿（拟定）` working copies should stay outside the archive subfolders until the user confirms finalization.
   - When grouped files exist, compare `AI原始初稿` against `AI规范修订稿` to summarize official-material fixes; compare `AI规范修订稿` against `我最终修改稿` to summarize personal style preferences.

2. **Train style by scenario**
   - If the user only says something like `请使用 personal-official-writing-workflow，帮我训练一个写作场景的个人风格。`, do not ask them to write a full prompt. Guide them step by step.
   - Ask only for missing items: material type, completed-sample folder path or pasted samples, whether grouped draft records exist, paths for `AI原始初稿` / `AI规范修订稿` / `我最终修改稿` if available, and whether to create a new style note or update an existing one.
   - If the material type or folder path already implies the scenario, infer it and ask for confirmation instead of asking the user to restate it.
   - Use `learning-personal-writing-style`.
   - Build one style note per scenario when possible: communications, summaries/reports, speeches, research reports, notices.
   - Output beginner-facing files such as `通讯稿风格说明.md`, forbidden patterns, reusable outlines, and confidence.

3. **Draft from a real writing request**
   - If the user only says something like `请使用 personal-official-writing-workflow 帮我写一份材料。`, do not draft immediately. Ask them for six items: material type, use scenario, rough framework and must-keep facts, reference material path or pasted content, target length, and forbidden content.
   - Provide simple examples for each item, such as `工作总结 / 汇报材料 / 通讯稿 / 通知 / 讲话稿`, `季度工作推进情况总结`, or `不能编造数据`.
   - If the user is unsure about the document type, present a short choice list, infer the closest material type from the task, and ask the user to confirm.
   - Accept reference material either pasted in chat or provided as a local file/folder path. If the path is provided, read the file before drafting; if the current platform cannot read local paths, ask the user to paste the needed content. If the material is insufficient, ask for the missing facts.
   - Use the closest style note to draft the first version.
   - Preserve facts and mark missing information with `[待补充]`.
   - If the current AI tool can write local files, automatically save the first style-based draft into `AI原始初稿` before running the official-material pass. If file writing is unavailable, tell the user exactly what filename to use.
   - Do not stop after the style-based draft. After `AI原始初稿` is produced, immediately continue to the official-material pass as the second internal stage of the same workflow.

4. **Run the official-material pass**
   - Use `drafting-official-materials` automatically after the style-based draft. Do not require the user to trigger this sub-skill manually.
   - Confirm whether the draft is a notice, report, request, letter, meeting minutes, speech, work summary, research report, or briefing.
   - Check structure, institutional relationship, policy/fact safety, official tone, headings, and closing formula.
   - Save the post-check version into `AI规范修订稿`. Treat this as an archived AI trace version; do not ask the user to edit it directly.
   - If file writing is available, immediately create an editable working copy in the material-type folder root using the pattern `{编号}-{标题}-AI规范修订稿（拟定）.docx`. Tell the user to revise only this working copy.
   - If the platform cannot invoke sub-skills automatically, explicitly state that you are continuing with the official-material check and then apply the same rules directly.

5. **Learn from the user's edit**
   - When the user says `已定稿，请帮我归档`, `已定稿`, or otherwise confirms the working copy is final, infer the matching `{编号}-{标题}-AI规范修订稿（拟定）.docx` from the current task, same sequence number, material type folder, or most recent unarchived `（拟定）` file. Save or move it into `我最终修改稿` as `{编号}-{标题}-我最终修改稿.docx`. Ask the user to choose only if multiple candidate working copies exist. Do not ask the user to retype the full source path or target path. Do not overwrite the archived `AI规范修订稿`.
   - Then compare the AI official-standard revision vs the user final version with `learning-personal-writing-style`.
   - When the user asks briefly, such as `请帮我更新写作风格，根据刚生成的“002-季度工作总结”的几份稿件。`, do not ask them to paste all three paths. Infer the matching `AI原始初稿`, `AI规范修订稿`, and `我最终修改稿` from the current task, same sequence number/title, material type folder, or recent generated files. Ask the user to choose only if multiple candidates exist or required files are missing.
   - Use the inferred file-path group when possible, such as `年度工作总结 / AI原始初稿 / 002-季度工作总结-AI原始初稿.docx`, `年度工作总结 / AI规范修订稿 / 002-季度工作总结-AI规范修订稿.docx`, and `年度工作总结 / 我最终修改稿 / 002-季度工作总结-我最终修改稿.docx`.
   - Do not treat all differences between `AI原始初稿` and `我最终修改稿` as personal style. First separate official-format fixes from personal edits. Update personal style notes primarily from the `AI规范修订稿` vs `我最终修改稿` comparison.
   - Add durable revision rules only when the edit reveals a repeatable preference.

## Input Contract

Before drafting, collect:

```text
材料类型：
使用场景：
大致框架和必须保留的事实：
参考素材路径或粘贴内容：
篇幅：
不能写的内容：
```

If the user cannot provide all fields, continue with placeholders unless the missing field blocks the document type. Do not require the user to know the style-note filename; infer the closest style note from the material type and available style files.

## Output Contract

For training:

```text
已读取样本：
生成/更新的风格文件：
风格置信度：
最明显的 5 条写作习惯：
需要继续补充的样本：
```

For writing:

```text
一、可直接修改的正文
二、已应用的个人风格规则
三、公文规范检查结果
四、待确认事项
五、建议回流训练的修改点
```

## Quality Rules

- Personal style can shape expression, rhythm, paragraphing, and preferred structures, but must not override document type, factual accuracy, or institutional tone.
- For strict statutory documents such as `请示`, `报告`, `通知`, `函`, and `会议纪要`, the official-material pass is mandatory after style drafting.
- For communications and briefings, readability may be stronger, but claims still need concrete facts, measures, effects, or next steps.
- Do not present a starter profile as stable. State confidence based on sample count and edit quality.
- Keep beginner-facing guidance step-by-step. Avoid assuming the user understands skills, local folders, Markdown, or style profiles.

## Common Mistakes

| Mistake | Fix |
|-|-|
| Putting all sample materials into one folder | Separate by scenario before training |
| Training only from final drafts | Add AI draft vs user-edited pairs whenever possible |
| Drafting in personal style but skipping official checks | Always run `drafting-official-materials` before delivery |
| Letting the model invent policy/data | Use placeholders and ask for confirmation |
| Updating style after every tiny edit | Update only repeatable preferences; keep one-off edits as notes |
