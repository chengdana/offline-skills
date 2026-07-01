---
name: pdf
description: Use when reading, extracting, splitting, merging, filling, creating, or programmatically modifying PDF files, including form handling, text extraction, and bulk PDF processing tasks.
---

# PDF

Work with PDFs using the local references and scripts bundled with this skill.

## Start Here

- For general PDF workflows, read `reference.md` when needed.
- For form filling, read `forms.md` first.
- Prefer `scripts/` helpers if one matches the task.

## Workflow

1. Identify the task type:
   - read or extract
   - fill a form
   - merge or split
   - generate a new PDF
   - edit an existing PDF
2. Choose the simplest local toolchain that can complete the task reliably.
3. Preserve the original file unless the user explicitly asks for in-place replacement.
4. Verify the output PDF opens and has the expected page count or extracted content.

## Rules

- Do not claim success without checking the produced PDF.
- Call out OCR limitations if text is image-based.
- Preserve form fields and page order unless the task requires changing them.
