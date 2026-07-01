---
name: docx
description: "全面的文档创建、编辑和分析，支持跟踪更改、注释、格式保留和文本提取。当 Claude 需要处理专业文档（.docx 文件）时用于：（1）创建新文档，（2）修改或编辑内容，（3）处理跟踪更改，（4）添加注释或任何其他文档任务"
license: 专有。完整条款见 LICENSE.txt
---

# DOCX 创建、编辑和分析

## 概述

用户可能要求您创建、编辑或分析 .docx 文件的内容。.docx 文件本质上是一个包含 XML 文件和其他可以读取或编辑的资源的 ZIP 存档。您针对不同的任务有不同的工具和工作流程可用。

## 工作流程决策树

### 读取/分析内容
使用下面的"文本提取"或"原始 XML 访问"部分

### 创建新文档
使用"创建新的 Word 文档"工作流程

### 编辑现有文档
- **您自己的文档 + 简单更改**
  使用"基本 OOXML 编辑"工作流程

- **其他人的文档**
  使用**"修订工作流程"**（推荐默认）

- **法律、学术、商业或政府文档**
  使用**"修订工作流程"**（必需）

## 读取和分析内容

### 文本提取
如果只需要读取文档的文本内容，应该使用 pandoc 将文档转换为 markdown。Pandoc 提供了对保留文档结构的出色支持，可以显示跟踪更改：

```bash
# 使用跟踪更改将文档转换为 markdown
pandoc --track-changes=all path-to-file.docx -o output.md
# 选项：--track-changes=accept/reject/all
```

### 原始 XML 访问
您需要原始 XML 访问来处理：注释、复杂格式、文档结构、嵌入的媒体和元数据。对于这些功能中的任何一个，您需要解包文档并读取其原始 XML 内容。

#### 解包文件
`python ooxml/scripts/unpack.py <office_file> <output_directory>`

#### 关键文件结构
* `word/document.xml` - 主文档内容
* `word/comments.xml` - 在 document.xml 中引用的注释
* `word/media/` - 嵌入的图像和媒体文件
* 跟踪的更改使用 `<w:ins>`（插入）和 `<w:del>`（删除）标签

## 创建新的 Word 文档

从 scratch 创建新的 Word 文档时，请使用 **docx-js**，它允许您使用 JavaScript/TypeScript 创建 Word 文档。

### 工作流程
1. **强制 - 阅读整个文件**：从头到尾完全阅读 [`docx-js.md`](docx-js.md)（约 500 行）。**在阅读此文件时切勿设置任何范围限制。** 在继续创建文档之前，阅读完整的文件内容以获取详细的语法、关键的格式规则和最佳实践。
2. 使用 Document、Paragraph、TextRun 组件创建 JavaScript/TypeScript 文件（您可以假设所有依赖项都已安装，但如果没有，请参阅下面的依赖项部分）
3. 使用 Packer.toBuffer() 导出为 .docx

## 编辑现有的 Word 文档

编辑现有的 Word 文档时，请使用 **Document 库**（一个用于 OOXML 操作的 Python 库）。该库自动处理基础架构设置并提供文档操作方法。对于复杂场景，您可以通过该库直接访问底层 DOM。

### 工作流程
1. **强制 - 阅读整个文件**：从头到尾完全阅读 [`ooxml.md`](ooxml.md)（约 600 行）。**在阅读此文件时切勿设置任何范围限制。** 阅读完整的文件内容以获取 Document 库 API 和用于直接编辑文档文件的 XML 模式。
2. 解包文档：`python ooxml/scripts/unpack.py <office_file> <output_directory>`
3. 使用 Document 库创建并运行 Python 脚本（请参阅 ooxml.md 中的"Document Library"部分）
4. 打包最终文档：`python ooxml/scripts/pack.py <input_directory> <office_file>`

Document 库为常见操作提供高级方法，并为复杂场景提供直接 DOM 访问。

## 文档审查的修订工作流程

此工作流程允许您在使用 OOXML 实现它们之前计划全面的跟踪更改。**关键**：对于完整的跟踪更改，您必须系统地实施所有更改。

**批处理策略**：将相关更改分组为 3-10 个更改的批次。这使得调试可管理，同时保持效率。在移动到下一个之前测试每个批次。

**原则：最少、精确的编辑**
实施跟踪更改时，仅标记实际更改的文本。重复未更改的文本使编辑更难审查，并且看起来不专业。将替换分解为：[未更改的文本] + [删除] + [插入] + [未更改的文本]。通过从原始提取 `<w:r>` 元素并重新使用它来保留未更改文本的原始运行的 RSID。

示例 - 将句子中的"30 天"更改为"60 天"：
```python
# 坏 - 替换整个句子
'<w:del><w:r><w:delText>期限是 30 天。</w:delText></w:r></w:del><w:ins><w:r><w:t>期限是 60 天。</w:t></w:r></w:ins>'

# 好 - 仅标记更改的内容，为未更改的文本保留原始 <w:r>
'<w:r w:rsidR="00AB12CD"><w:t>期限是 </w:t></w:r><w:del><w:r><w:delText>30</w:delText></w:r></w:del><w:ins><w:r><w:t>60</w:t></w:r></w:ins><w:r w:rsidR="00AB12CD"><w:t> 天。</w:t></w:r>'
```

### 跟踪更改工作流程

1. **获取 markdown 表示**：将文档转换为带有保留跟踪更改的 markdown：
   ```bash
   pandoc --track-changes=all path-to-file.docx -o current.md
   ```

2. **识别和分组更改**：审查文档并识别所有需要的更改，将它们组织成逻辑批次：

   **定位方法**（用于在 XML 中查找更改）：
   - 部分/标题编号（例如，"第 3.2 节"、"第四条"）
   - 编号段落的标识符
   - 带有独特周围文本的 Grep 模式
   - 文档结构（例如，"第一段"、"签名块"）
   - **不要使用 markdown 行号** - 它们不映射到 XML 结构

   **批次组织**（每组 3-10 个相关更改）：
   - 按部分："批次 1：第 2 节修正"、"批次 2：第 5 节更新"
   - 按类型："批次 1：日期更正"、"批次 2：各方名称更改"
   - 按复杂性：从简单的文本替换开始，然后处理复杂的结构更改
   - 顺序："批次 1：第 1-3 页"、"批次 2：第 4-6 页"

3. **阅读文档并解包**：
   - **强制 - 阅读整个文件**：从头到尾完全阅读 [`ooxml.md`](ooxml.md)（约 600 行）。**在阅读此文件时切勿设置任何范围限制。** 特别注意"Document Library"和"Tracked Change Patterns"部分。
   - **解包文档**：`python ooxml/scripts/unpack.py <file.docx> <dir>`
   - **注意建议的 RSID**：解包脚本将建议一个 RSid 用于您的跟踪更改。复制此 RSid 以在步骤 4b 中使用。

4. **分批实施更改**：逻辑地分组更改（按部分、按类型或按接近程度）并在单个脚本中一起实施它们。此方法：
   - 使调试更容易（更小的批次 = 更容易隔离错误）
   - 允许增量进度
   - 保持效率（3-10 个更改的批次大小效果很好）

   **建议的批次分组**：
   - 按文档部分（例如，"第 3 节更改"、"定义"、"终止条款"）
   - 按更改类型（例如，"日期更改"、"各方名称更新"、"法律术语替换"）
   - 按接近程度（例如，"第 1-3 页的更改"、"文档上半部分的更改"）

   对于每批相关更改：

   **a. 将文本映射到 XML**：在 `word/document.xml` 中使用 Grep 查找文本以验证文本如何跨 `<w:r>` 元素分割。

   **b. 创建并运行脚本**：使用 `get_node` 查找节点，实施更改，然后 `doc.save()`。请参阅 ooxml.md 中的 **"Document Library"** 部分以获取模式。

   **注意**：在编写脚本之前始终 grep `word/document.xml` 以获取当前行号并验证文本内容。行号在每次脚本运行后都会更改。

5. **打包文档**：所有批次完成后，将解包的目录转换回 .docx：
   ```bash
   python ooxml/scripts/pack.py unpacked reviewed-document.docx
   ```

6. **最终验证**：对完整文档进行全面检查：
   - 将最终文档转换为 markdown：
     ```bash
     pandoc --track-changes=all reviewed-document.docx -o verification.md
     ```
   - 验证所有更改都正确应用：
     ```bash
     grep "原始短语" verification.md  # 应该找不到它
     grep "替换短语" verification.md  # 应该找到它
     ```
   - 检查是否引入了任何意外的更改

## 将文档转换为图像

要直观地分析 Word 文档，请使用两步过程将它们转换为图像：

1. **将 DOCX 转换为 PDF**：
   ```bash
   soffice --headless --convert-to pdf document.docx
   ```

2. **将 PDF 页面转换为 JPEG 图像**：
   ```bash
   pdftoppm -jpeg -r 150 document.pdf page
   ```
   这将创建 `page-1.jpg`、`page-2.jpg` 等文件。

选项：
- `-r 150`：将分辨率设置为 150 DPI（调整质量/大小平衡）
- `-jpeg`：输出 JPEG 格式（如果首选，使用 `-png` 表示 PNG）
- `-f N`：要转换的第一页（例如，`-f 2` 从第 2 页开始）
- `-l N`：要转换的最后一页（例如，`-l 5` 在第 5 页停止）
- `page`：输出文件的前缀

特定范围的示例：
```bash
pdftoppm -jpeg -r 150 -f 2 -l 5 document.pdf page  # 仅转换第 2-5 页
```

## 代码样式指南
**重要**：为 DOCX 操作生成代码时：
- 编写简洁的代码
- 避免冗长的变量名和冗余操作
- 避免不必要的打印语句

## 依赖项

所需的依赖项（如果不可用则安装）：

- **pandoc**：`sudo apt-get install pandoc`（用于文本提取）
- **docx**：`npm install -g docx`（用于创建新文档）
- **LibreOffice**：`sudo apt-get install libreoffice`（用于 PDF 转换）
- **Poppler**：`sudo apt-get install poppler-utils`（用于 pdftoppm 将 PDF 转换为图像）
- **defusedxml**：`pip install defusedxml`（用于安全 XML 解析）
