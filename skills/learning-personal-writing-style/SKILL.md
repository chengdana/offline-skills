---
name: learning-personal-writing-style
description: Use when analyzing a user's sample articles, revisions, drafts, edited-before-after pairs, voice notes, public-account posts, official materials, speeches, or long-form writing to build, update, or apply a reusable personal writing style profile.
---

# Learning Personal Writing Style

## Overview

Turn the user's real writing and edits into a reusable style profile: voice, structure, rhythm, preferred expressions, forbidden patterns, revision rules, and examples. Use the profile to draft new text, rewrite AI drafts, or continuously learn from corrections.

This is not model fine-tuning. It is a controlled skill workflow based on samples, rules, examples, and edit history.

## Workflow

1. **Collect material**
   - Prefer 5-20 strong samples from the target genre.
   - Separate genres when needed: `公众号`, `党政材料`, `讲话稿`, `调研报告`, `小红书`, `内部汇报`.
   - If the user provides before/after edits, treat those as the highest-value data.
   - Use `references/corpus-guidelines.md` when organizing files.

2. **Extract signals**
   - Read representative samples, not everything blindly.
   - If samples are local `.md` or `.txt` files, run `scripts/extract_style_signals.py <sample_dir>` for basic measurable signals.
   - Identify structure, opening habits, paragraph length, sentence rhythm, vocabulary, evidence style, stance, emotional temperature, and recurring transitions.

3. **Build or update the style profile**
   - Use `references/style-profile-template.md`.
   - Make rules specific enough to guide writing: "open with a concrete contradiction" is useful; "be thoughtful" is not.
   - Add 3-8 positive rules, 3-8 negative rules, reusable outlines, and several short phrase examples.

4. **Learn from edits**
   - Compare the AI draft and the user's edited version.
   - Extract repeatable differences: deletion habits, stronger verbs, title changes, paragraph reshaping, examples added, hedging removed, tone softened, etc.
   - Use `references/revision-learning.md` to convert edits into durable rules.

5. **Apply the style**
   - For new drafts, first decide genre and intended reader.
   - Draft for substance first, then perform a style pass.
   - Preserve factual accuracy. Style must never override truth, policy constraints, or document format.

## Style Profile Location

When the user does not specify a project path, suggest storing the profile near the user's writing corpus:

```text
writing-style/
├── samples/
├── edits/
├── style-profile.md
└── forbidden-patterns.md
```

Do not create a profile in the skill folder unless the user explicitly wants the skill itself to become personal and machine-local.

## Quick Diagnosis

| Material available | Best action |
|---|---|
| Only a topic | Ask for target genre and draft normally; mark style confidence as low |
| 3-5 samples | Build a starter profile with caveats |
| 10+ samples in same genre | Build a stable profile and reusable outlines |
| Before/after edits | Prioritize revision rules over surface style |
| Mixed genres | Split profiles by genre before summarizing shared voice |
| Official materials plus personal essays | Keep separate; they optimize for different constraints |

## Quality Rules

- Do not imitate private third-party authors without permission. For the user's own writing, build from provided samples.
- Do not overfit. A style profile should capture repeatable choices, not copy sentences.
- Keep examples short. Use phrase-level or one-sentence examples unless the user asks for longer excerpts from their own work.
- Distinguish voice from domain constraints. A public-account voice, a party/government document tone, and a Xiaohongshu note may belong to the same user but need different execution.
- Always state confidence when the sample size is small.

## Output

When building a profile, deliver:

1. `style-profile.md` content or an update patch.
2. Key findings in plain language.
3. Suggested next samples that would improve accuracy.

When applying a profile, deliver:

1. The rewritten or newly drafted text.
2. A brief change note: what style rules were applied.
3. Any facts or tone choices needing user confirmation.
