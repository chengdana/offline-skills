---
name: pdf-generator
description: Generate professional PDF documents from Markdown content. Use when Codex needs to create PDF documents for documentation, reports, summaries, command reference guides, technical specifications, or similar outputs. Supports Chinese fonts, tables, code blocks, and custom styling.
---

# PDF Generator

Generate professional PDF documents with Chinese language support, tables, code blocks, and custom styling.

## Quick Start

To generate a PDF:

1. Create or generate a Markdown file (`.md`)
2. Run the PDF generation script:
   ```bash
   python scripts/generate_pdf.py <input.md> [output.pdf]
   ```
3. If no output filename is specified, it defaults to the same name as the input file

## Workflow

```mermaid
graph LR
    A[User Request] --> B[Generate Markdown]
    B --> C[Write .md File]
    C --> D[Run generate_pdf.py]
    D --> E[PDF Output]
```

## Markdown Format Support

The PDF generator supports standard Markdown with extensions:

- **Headings**: `# H1`, `## H2`, `### H3`
- **Tables**: `| Header | Header |`
- **Code blocks**: ```` ```language ```` and inline `` `code` ``
- **Lists**: `- item` or `1. item`
- **Bold**: `**text**`
- **Horizontal rules**: `---`

## Styling

The PDF generator applies these default styles:

- **Page size**: A4
- **Margins**: 2cm on all sides
- **Fonts**: Auto-detects system Chinese fonts (Microsoft YaHei, PingFang SC, etc.)
- **Colors**: Professional blue theme for headings

## Script Details

See `scripts/generate_pdf.py` for the implementation. Key features:

- Automatic Chinese font detection across platforms (Windows/macOS/Linux)
- Table rendering with borders and header styling
- Code block highlighting with gray background
- Multi-level heading styles

## Example

```bash
# Generate from existing markdown
python scripts/generate_pdf.py guide.md

# Specify output name
python scripts/generate_pdf.py guide.md output.pdf
```
