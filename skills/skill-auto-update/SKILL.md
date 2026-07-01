---
name: skill-auto-update
description: Use when improving an existing skill based on user feedback, usage friction, missing triggers, outdated instructions, or Codex compatibility issues.
---

# Skill Auto Update

Revise an existing skill based on real feedback and observable failures.

## Start Here

- Inspect the target skill folder first.
- Read any bundled `reference/` or `examples/` files only if they are relevant to the requested change.

## Workflow

1. Identify the concrete complaint or failure mode.
2. Check whether the issue is in:
   - trigger description
   - workflow ordering
   - missing local resource references
   - outdated tool or path assumptions
3. Update the skill with the smallest change that fixes the issue.
4. Keep `SKILL.md` concise and Codex-compatible:
   - frontmatter should contain only `name` and `description`
   - prefer relative references to local bundled resources
5. Summarize what changed and what user behavior the revision is meant to improve.

## Rules

- Do not add speculative complexity.
- Prefer fixing concrete trigger words and execution steps over adding long explanations.
- Preserve useful scripts, references, and examples already in the skill.
