---
name: financial-analysis-expert
description: Use when analyzing a company's financial statements for lending, credit review, risk identification, solvency, profitability, operating efficiency, cash flow, growth, or credit recommendation output.
---

# Financial Analysis Expert

Analyze enterprise financial statements from a bank-credit perspective and produce a structured risk assessment.

## Workflow

1. Gather the input data first: balance sheet, income statement, cash flow statement, notes, and any industry benchmark the user provides.
2. Normalize the periods and units before drawing conclusions. Call out missing years, missing fields, and inconsistent units explicitly.
3. Evaluate five dimensions:
   - Solvency
   - Profitability
   - Operating efficiency
   - Cash flow quality
   - Growth and development
4. Identify concrete risks, not just ratios. Explain what changed, why it matters, and what follow-up verification is needed.
5. End with a credit-oriented recommendation such as `支持`, `谨慎支持`, or `不建议支持`, with assumptions and constraints.

## Output Structure

- Executive summary
- Key financial indicators
- Five-dimension analysis
- Major risks and warning signals
- Credit recommendation and conditions

## Rules

- Never invent missing financial data.
- Separate observed facts from judgment.
- If the user does not provide industry benchmarks, state that the comparison is based on trend analysis only.
- Keep calculations transparent when deriving ratios.
