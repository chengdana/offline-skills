# PDF 生成器 (PDF Generator) 使用说明

## 功能简介
从 Markdown 内容生成专业的 PDF 文档，支持中文、表格、代码块和自定义样式。

## 使用场景
- 需要创建文档或手册时
- 生成报告或摘要时
- 创建命令参考指南时
- 编写技术规格说明时
- 任何需要 PDF 输出的场景

## 快速开始
1. 准备 Markdown 文件（.md）
2. 运行生成命令：
   ```bash
   python .claude/skills/pdf-generator/scripts/generate_pdf.py input.md
   ```
3. 获得同名的 PDF 文件

## 主要特性
- ✅ 中文字体自动检测
- ✅ 表格渲染
- ✅ 代码块高亮
- ✅ 多级标题样式
- ✅ A4 页面，专业边距
- ✅ 跨平台支持（Windows/macOS/Linux）

## 支持的 Markdown 语法
- 标题（H1-H3）
- 表格
- 代码块（支持语法高亮）
- 有序/无序列表
- 粗体文本
- 水平分隔线
