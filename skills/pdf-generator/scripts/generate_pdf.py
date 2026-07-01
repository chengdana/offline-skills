"""
PDF Generator - Convert Markdown to PDF
Requires: pip install reportlab
Usage: python generate_pdf.py <input.md> [output.pdf]
"""

import os
import re
import sys
import argparse
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import cm
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak
from reportlab.lib.enums import TA_LEFT, TA_CENTER
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.fonts import addMapping

# 尝试注册中文字体
def register_chinese_font():
    """注册系统中文字体"""
    font_paths = [
        # Windows 常见中文字体
        ("C:/Windows/Fonts/msyh.ttc", "Microsoft YaHei"),
        ("C:/Windows/Fonts/simsun.ttc", "SimSun"),
        ("C:/Windows/Fonts/simhei.ttf", "SimHei"),
        # macOS 常见中文字体
        ("/System/Library/Fonts/PingFang.ttc", "PingFang SC"),
        ("/Library/Fonts/Arial Unicode.ttf", "Arial Unicode"),
        # Linux 常见中文字体
        ("/usr/share/fonts/truetype/wqy/wqy-zenhei.ttc", "WenQuanYi Zen Hei"),
        ("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", "DejaVu"),
    ]

    for path, name in font_paths:
        if os.path.exists(path):
            try:
                pdfmetrics.registerFont(TTFont(name, path, subfontIndex=0))
                addMapping(name, 0, 0, name)
                print(f"使用字体: {name}")
                return name
            except Exception as e:
                continue

    # 如果都没有找到，使用默认字体（中文可能显示不正常）
    print("警告: 未找到中文字体，使用默认字体")
    return "Helvetica"

# Markdown 解析器
def parse_markdown_to_elements(content, font_name):
    """将 Markdown 内容转换为 ReportLab 元素列表"""
    elements = []
    lines = content.split('\n')
    styles = getSampleStyleSheet()

    # 自定义样式
    styles.add(ParagraphStyle(
        name='ChineseTitle',
        parent=styles['Heading1'],
        fontName=font_name,
        fontSize=24,
        textColor=colors.HexColor('#2563eb'),
        spaceAfter=12,
        alignment=TA_CENTER
    ))

    styles.add(ParagraphStyle(
        name='ChineseHeading1',
        parent=styles['Heading1'],
        fontName=font_name,
        fontSize=18,
        textColor=colors.HexColor('#1e40af'),
        spaceAfter=10,
        spaceBefore=15
    ))

    styles.add(ParagraphStyle(
        name='ChineseHeading2',
        parent=styles['Heading2'],
        fontName=font_name,
        fontSize=14,
        textColor=colors.HexColor('#1e3a8a'),
        spaceAfter=8,
        spaceBefore=10
    ))

    styles.add(ParagraphStyle(
        name='ChineseHeading3',
        parent=styles['Heading3'],
        fontName=font_name,
        fontSize=12,
        textColor=colors.HexColor('#1e40af'),
        spaceAfter=6,
        spaceBefore=8
    ))

    styles.add(ParagraphStyle(
        name='ChineseNormal',
        parent=styles['Normal'],
        fontName=font_name,
        fontSize=10,
        leading=14,
        spaceAfter=6
    ))

    styles.add(ParagraphStyle(
        name='ChineseCode',
        parent=styles['Code'],
        fontName='Courier',
        fontSize=9,
        leading=12,
        spaceAfter=6,
        backColor=colors.HexColor('#f1f5f9')
    ))

    i = 0
    in_code_block = False
    code_lines = []

    while i < len(lines):
        line = lines[i].rstrip()

        # 处理代码块
        if line.startswith('```'):
            if in_code_block:
                # 结束代码块
                code_text = '\n'.join(code_lines)
                elements.append(Paragraph(code_text.replace('<', '&lt;').replace('>', '&gt;'), styles['ChineseCode']))
                elements.append(Spacer(1, 0.3*cm))
                code_lines = []
                in_code_block = False
            else:
                in_code_block = True
            i += 1
            continue

        if in_code_block:
            code_lines.append(line)
            i += 1
            continue

        # 跳过空行
        if not line:
            i += 1
            continue

        # 处理一级标题
        if line.startswith('# '):
            text = line[2:].strip()
            elements.append(Paragraph(text, styles['ChineseTitle']))
            elements.append(Spacer(1, 0.5*cm))

        # 处理二级标题
        elif line.startswith('## '):
            text = line[3:].strip()
            elements.append(Paragraph(text, styles['ChineseHeading1']))
            elements.append(Spacer(1, 0.3*cm))

        # 处理三级标题
        elif line.startswith('### '):
            text = line[4:].strip()
            elements.append(Paragraph(text, styles['ChineseHeading2']))

        # 处理表格（Markdown 格式）
        elif line.startswith('|'):
            table_lines = [line]
            i += 1
            # 检查是否有分隔线
            if i < len(lines) and lines[i].startswith('|--'):
                i += 1
                # 收集所有表格行
                while i < len(lines) and lines[i].startswith('|'):
                    table_lines.append(lines[i])
                    i += 1

                # 解析表格
                table_data = []
                for tline in table_lines:
                    cells = [cell.strip() for cell in tline.split('|')[1:-1]]
                    table_data.append(cells)

                # 创建表格
                if table_data:
                    col_widths = [A4[0] / len(table_data[0]) * 0.9] * len(table_data[0])
                    table = Table(table_data, colWidths=col_widths)
                    table.setStyle(TableStyle([
                        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#dbeafe')),
                        ('TEXTCOLOR', (0, 0), (-1, 0), colors.HexColor('#1e40af')),
                        ('FONTNAME', (0, 0), (-1, -1), font_name),
                        ('FONTSIZE', (0, 0), (-1, -1), 9),
                        ('BOTTOMPADDING', (0, 0), (-1, 0), 8),
                        ('TOPPADDING', (0, 0), (-1, -1), 4),
                        ('BOTTOMPADDING', (0, 1), (-1, -1), 4),
                        ('GRID', (0, 0), (-1, -1), 0.5, colors.grey),
                        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
                    ]))
                    elements.append(table)
                    elements.append(Spacer(1, 0.3*cm))
                continue

        # 处理列表项
        elif re.match(r'^\d+\.\s', line):
            text = re.sub(r'^\d+\.\s', '', line)
            elements.append(Paragraph(f"{text}", styles['ChineseNormal']))

        elif line.startswith('- ') or line.startswith('* '):
            text = line[2:].strip()
            elements.append(Paragraph(f"• {text}", styles['ChineseNormal']))

        # 处理分隔线
        elif line.startswith('---'):
            elements.append(Spacer(1, 0.3*cm))

        # 处理代码行（以反引号开头）
        elif line.startswith('```') or line.strip().startswith('`'):
            elements.append(Paragraph(line.replace('`', ''), styles['ChineseCode']))

        # 普通段落
        else:
            # 处理行内代码和粗体
            processed = line
            processed = re.sub(r'\*\*(.+?)\*\*', r'<b>\1</b>', processed)
            processed = re.sub(r'`(.+?)`', r'<font face="Courier">\1</font>', processed)
            elements.append(Paragraph(processed, styles['ChineseNormal']))

        i += 1

    return elements

def generate_pdf(md_file, pdf_file):
    """生成 PDF 文件"""
    # 读取 Markdown 文件
    with open(md_file, 'r', encoding='utf-8') as f:
        content = f.read()

    # 注册字体
    font_name = register_chinese_font()

    # 创建 PDF
    doc = SimpleDocTemplate(
        pdf_file,
        pagesize=A4,
        rightMargin=2*cm,
        leftMargin=2*cm,
        topMargin=2*cm,
        bottomMargin=2*cm
    )

    # 解析并生成元素
    elements = parse_markdown_to_elements(content, font_name)

    # 构建 PDF
    doc.build(elements)
    print(f"PDF 已生成: {pdf_file}")

def main():
    parser = argparse.ArgumentParser(
        description='Convert Markdown to PDF',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog='''
Examples:
  python generate_pdf.py document.md
  python generate_pdf.py document.md output.pdf
  python generate_pdf.py README.pdf -o MyDocument.pdf
        '''
    )
    parser.add_argument('input', help='Input Markdown file (.md)')
    parser.add_argument('output', nargs='?', help='Output PDF file (default: input filename with .pdf extension)')
    parser.add_argument('-o', '--output-file', dest='output_alt', help='Alternative way to specify output file')

    args = parser.parse_args()

    md_file = args.input
    pdf_file = args.output or args.output_alt

    if not os.path.exists(md_file):
        print(f"Error: Input file not found: {md_file}", file=sys.stderr)
        sys.exit(1)

    if pdf_file is None:
        pdf_file = os.path.splitext(md_file)[0] + '.pdf'

    try:
        generate_pdf(md_file, pdf_file)
    except ImportError as e:
        print("\nError: Required library not installed.", file=sys.stderr)
        print("Please install: pip install reportlab", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"Error generating PDF: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
