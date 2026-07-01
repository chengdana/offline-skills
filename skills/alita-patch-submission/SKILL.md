---
name: alita-patch-submission
description: Solve Alita-style coding challenges where the user must upload a submission.json containing a unified diff. Use when a workspace has challenge files such as submission.json, CHAL-* directories, hidden tests, platform logs like apply_model_patch, or the user asks to complete/debug a patch-submission coding problem.
---

# Alita Patch Submission

## Overview

Produce a valid `submission.json` for code challenges that grade by applying a model patch. Prioritize a clean, minimal unified diff that `git apply` accepts.

## Workflow

1. Read the prompt, screenshot, README, existing `submission.json`, and nearby tests before editing.
2. Identify the smallest source-file behavior change required by the challenge.
3. Reproduce with the narrowest possible command. If the local environment blocks execution, separate environment failures from challenge logic and continue with static/diff validation.
4. Inspect nearby existing tests for both accepted and rejected behavior, especially when changing parsers, validators, type systems, or compatibility code. Run the narrow new/regression case plus the closest existing negative tests when feasible.
   - For parser or grammar fixes, distinguish changing associativity/precedence from broadening accepted syntax. Do not replace a narrow grammar term such as a single expression item with a wider term such as a product/group unless the prompt explicitly requires accepting that wider syntax.
5. Edit only relevant source files. Avoid committing local build artifacts, generated binaries, dependency changes, or exploratory tests into `submission.json` unless the challenge explicitly requires tests.
6. Build the submission diff from a known original file state, not from memory. If no `.git` exists, construct the unified diff carefully from original content or the supplied baseline diff.
7. Validate `submission.json` and the extracted patch before telling the user to upload.

## Diff Rules

- `submission.json` must contain at least:

```json
{
  "challenge_id": "CHAL-...",
  "diff": "diff --git ..."
}
```

- The `diff` value must be a standard unified diff with `diff --git`, `---`, `+++`, and `@@` hunk headers.
- Hunk line counts must be exact. For `@@ -a,b +c,d @@`, count every context line plus every added line in the new side as `d`, and every context line plus every removed line in the old side as `b`.
- A `corrupt patch at line N` error usually means malformed hunk counts, missing/extra hunk lines, or broken escaping in the JSON string.
- Escape double quotes inside the JSON string as `\"`; keep newlines as `\n`.
- Prefer one focused file patch when possible. Do not include local environment setup changes.

## Required Validation

Always run these checks before final response:

```powershell
python -m json.tool submission.json > $null
@'
import json
from pathlib import Path
p = json.loads(Path("submission.json").read_text())["diff"]
Path("model.patch").write_text(p, newline="")
for i, line in enumerate(p.splitlines(), 1):
    print(f"{i:02d}: {line}")
'@ | python -
git apply --check --verbose model.patch
```

If the working tree already contains the patch, forward `git apply --check` may fail with "patch does not apply". In that case run:

```powershell
git apply --reverse --check --verbose model.patch
```

Interpretation:

- `corrupt patch` means the submission diff is invalid; fix `submission.json`.
- `patch does not apply` on a clean baseline means the context or target file is wrong; regenerate against the baseline.
- reverse check passing means the patch matches the current already-modified files.

## Handling Platform Logs

When the user shows grading logs:

- `apply_test_patch rc=0` means hidden or supplied tests were installed successfully.
- `apply_model_patch rc=128` with `corrupt patch` means submission formatting failed before tests ran.
- `apply_model_patch` with `patch does not apply` means the diff context does not match the grader baseline.
- Test failures after model patch application mean the code behavior is wrong; debug the implementation, not JSON formatting.
- If a hidden or supplied test shows a behavioral regression, identify the closest invariant that was accidentally loosened or tightened. Preserve pre-existing valid/invalid boundaries instead of only satisfying the prompt's positive example, then regenerate and revalidate `submission.json`.
- For failures like `DID NOT RAISE`, look for over-acceptance: a patch may have made invalid input valid by using a broader parser rule, looser validator condition, or more permissive fallback than intended.

## Parser Regression Triage

When a parser/grammar patch fails existing negative tests:

1. Extract the submitted diff from `submission.json` and inspect the grammar change itself, not only the edited working tree.
2. Classify each failure:
   - `DID NOT RAISE` means the patch over-accepted invalid syntax.
   - an unexpected parse error means the patch over-rejected valid syntax.
3. Compare the old and new grammar nonterminals. If the bug is about associativity or precedence, change recursion direction or grouping while keeping each operator's operands at the same narrow level.
4. Avoid replacing a narrow operand such as `unit_expression`, `factor`, or `term` with a wider operand such as `product_of_units`, `combined_units`, or `expression` unless the prompt explicitly says that wider syntax must now be valid.
5. For repeated operator bugs, validate both directions:
   - the intended repeated form parses, e.g. `a/b/c`.
   - a nearby grouped or mixed form remains invalid when existing tests expect it invalid, e.g. `/b.c` or `a/b.c`.
6. If generated parser tables exist, update them from the final grammar and confirm `submission.json` contains both the source grammar change and the generated table change.

### Repeated Division Pitfall

If a challenge says `a/b/c` should parse left-to-right, do not fix it by allowing `/` to take a whole product/group on the right.

Bad pattern:

```text
division : DIVISION product
         | division DIVISION product
```

This accepts invalid mixed forms such as `/b.c` or `a/b.c` when `product` can parse `b.c`.

Prefer preserving the original operand width:

```text
division : DIVISION item
         | division DIVISION item
         | product DIVISION item
```

Here `item` means the same narrow operand level that `/` accepted before the fix, such as `unit_expression`, `term`, or `factor`.

## Final Response

Tell the user exactly which file to upload and summarize the validation evidence. Mention any test commands that could not run and why.
