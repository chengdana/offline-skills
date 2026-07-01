---
name: markdown-to-word
description: Use when converting Markdown files into Word documents (.docx), especially when the user wants headings, lists, tables, links, code blocks, or basic formatting preserved in the generated document.
---

# Markdown to Word

Convert Markdown content into a formatted Word document.

## Workflow

1. Read the source Markdown and confirm the target output path.
2. Preserve document structure in this order:
   - Headings
   - Paragraphs
   - Lists
   - Tables
   - Code blocks
   - Links and emphasis
3. Prefer deterministic conversion paths such as existing local tools or Python libraries already available in the environment.
4. After generation, verify the `.docx` exists and that the title, heading levels, and tables rendered correctly.

## Formatting Priorities

- Keep heading hierarchy intact.
- Preserve table cell structure where possible.
- Render code blocks in a visually distinct style.
- Avoid silently dropping unsupported Markdown features; mention them.

## Output

Return the generated `.docx` path and list any formatting compromises.
