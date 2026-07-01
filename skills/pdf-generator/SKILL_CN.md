---
name: pdf-generator
description: 从 Markdown 内容生成专业 PDF 文档。当 Claude 需要为以下用途创建 PDF 文档时使用：(1) 文档和手册，(2) 报告和摘要，(3) 命令参考指南，(4) 技术规格说明，或任何其他 PDF 生成任务。支持中文字体、表格、代码块和自定义样式。
---

# PDF 生成器

从 Markdown 内容生成支持中文、表格、代码块和自定义样式的专业 PDF 文档。

## 快速开始

要生成 PDF：

1. 创建或生成 Markdown 文件（`.md`）
2. 运行 PDF 生成脚本：
   ```bash
   python .claude/skills/pdf-generator/scripts/generate_pdf.py <input.md> [output.pdf]
   ```
3. 如果未指定输出文件名，默认使用与输入文件相同的名称

## 工作流程

```mermaid
graph LR
    A[用户请求] --> B[生成 Markdown]
    B --> C[写入 .md 文件]
    C --> D[运行 generate_pdf.py]
    D --> E[PDF 输出]
```

## Markdown 格式支持

PDF 生成器支持标准 Markdown 及扩展：

- **标题**：`# H1`、`## H2`、`### H3`
- **表格**：`| 表头 | 表头 |`
- **代码块**：```` ```语言 ```` 和行内 `` `代码` ``
- **列表**：`- 项目` 或 `1. 项目`
- **粗体**：`**文本**`
- **水平线**：`---`

## 样式

PDF 生成器应用以下默认样式：

- **页面大小**：A4
- **边距**：各边 2cm
- **字体**：自动检测系统中文字体（Microsoft YaHei、PingFang SC 等）
- **颜色**：标题使用专业蓝色主题

## 脚本详情

参见 `scripts/generate_pdf.py` 了解实现细节。主要特性：

- 跨平台自动中文字体检测（Windows/macOS/Linux）
- 带边框和标题样式的表格渲染
- 带灰色背景的代码块高亮
- 多级标题样式

## 示例

```bash
# 从现有 markdown 生成
python .claude/skills/pdf-generator/scripts/generate_pdf.py guide.md

# 指定输出名称
python .claude/skills/pdf-generator/scripts/generate_pdf.py guide.md output.pdf
```
