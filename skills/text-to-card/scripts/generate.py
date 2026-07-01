#!/usr/bin/env python3
"""
文字转卡片生成器
将文字内容转换为精美的卡片或海报图片
"""

import argparse
import os
import sys

# 添加 styles.py 路径
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from styles import STYLES, DEFAULT_STYLE

try:
    from PIL import Image, ImageDraw, ImageFont
except ImportError:
    print("错误: 需要安装 Pillow 库")
    print("请运行: pip install Pillow")
    sys.exit(1)


def get_font(size, bold=False):
    """获取字体"""
    # 尝试使用系统字体
    font_names = [
        "msyhbd.ttc" if bold else "msyh.ttc",  # 微软雅黑
        "SimHei.ttf",  # 黑体
        "Arial.ttf" if not bold else "Arial Bold.ttf",
        "DejaVuSans.ttf",
    ]

    for font_name in font_names:
        try:
            # Windows 字体路径
            windows_fonts = [
                f"C:/Windows/Fonts/{font_name}",
                f"C:/Windows/Fonts/{font_name.lower()}",
            ]
            for path in windows_fonts:
                if os.path.exists(path):
                    return ImageFont.truetype(path, size)
        except:
            continue

    # 如果都找不到，使用默认字体
    return ImageFont.load_default()


def wrap_text(text, font, max_width):
    """将文字自动换行 - 支持中文和英文"""
    lines = []
    current_line = ""

    for char in text:
        test_line = current_line + char

        # 处理换行符
        if char == '\n':
            lines.append(current_line)
            current_line = ""
            continue

        # 获取文本边界
        bbox = font.getbbox(test_line)
        width = bbox[2] - bbox[0]

        if width <= max_width:
            current_line = test_line
        else:
            # 当前行已满，开始新行
            if current_line:
                lines.append(current_line)
            current_line = char

    # 添加最后一行
    if current_line:
        lines.append(current_line)

    return lines if lines else [text]


def draw_gradient(image, start_color, end_color, direction="vertical"):
    """绘制渐变背景"""
    width, height = image.size
    draw = ImageDraw.Draw(image)

    # 解析颜色
    r1, g1, b1 = int(start_color[1:3], 16), int(start_color[3:5], 16), int(start_color[5:7], 16)
    r2, g2, b2 = int(end_color[1:3], 16), int(end_color[3:5], 16), int(end_color[5:7], 16)

    for i in range(height):
        ratio = i / height
        r = int(r1 + (r2 - r1) * ratio)
        g = int(g1 + (g2 - g1) * ratio)
        b = int(b1 + (b2 - b1) * ratio)
        draw.rectangle([(0, i), (width, i + 1)], fill=(r, g, b))

    return image


def create_card(text, style_name="minimal", width=800, author=None):
    """创建文字卡片"""
    # 获取样式配置
    style = STYLES.get(style_name, STYLES[DEFAULT_STYLE])

    # 计算尺寸
    padding = style["padding"]
    content_width = width - 2 * padding

    # 获取字体
    title_font = get_font(style["font_size_title"], bold=True)
    author_font = get_font(style["font_size_author"])

    # 文字换行
    lines = wrap_text(text, title_font, content_width)

    # 计算高度
    total_text_height = 0
    for line in lines:
        bbox = title_font.getbbox(line)
        total_text_height += bbox[3] - bbox[1] + 10  # 行间距

    author_height = 0
    if author:
        bbox = author_font.getbbox(author)
        author_height = bbox[3] - bbox[1] + 40  # 作者上边距

    height = total_text_height + author_height + 2 * padding

    # 创建图片
    if style.get("gradient"):
        # 渐变背景
        image = Image.new("RGB", (width, height), style["gradient"][0])
        image = draw_gradient(image, style["gradient"][0], style["gradient"][1])
    else:
        # 纯色背景
        bg_color = style.get("background", "#FFFFFF")
        image = Image.new("RGB", (width, height), bg_color)

    draw = ImageDraw.Draw(image)

    # 卡片样式 - 绘制内卡片
    if style.get("shadow"):
        card_bg = style.get("card_bg", "#FFFFFF")
        card_padding = 30
        card_rect = [
            padding - card_padding,
            padding - card_padding,
            width - padding + card_padding,
            height - padding + card_padding
        ]

        # 绘制阴影
        shadow_offset = 10
        shadow_color = (200, 200, 200)
        draw.rectangle(
            [
                card_rect[0] + shadow_offset,
                card_rect[1] + shadow_offset,
                card_rect[2] + shadow_offset,
                card_rect[3] + shadow_offset
            ],
            fill=shadow_color,
            radius=20
        )

        # 绘制卡片背景
        draw.rectangle(card_rect, fill=card_bg, radius=20)

    # 绘制文字
    text_color = style.get("text_color", "#333333")
    r, g, b = int(text_color[1:3], 16), int(text_color[3:5], 16), int(text_color[5:7], 16)
    text_color_rgb = (r, g, b)

    y_offset = padding
    if style.get("shadow"):
        y_offset = padding - 15

    for line in lines:
        draw.text((padding, y_offset), line, font=title_font, fill=text_color_rgb)
        bbox = title_font.getbbox(line)
        y_offset += bbox[3] - bbox[1] + 15

    # 绘制作者
    if author:
        accent_color = style.get("accent_color", "#666666")
        r, g, b = int(accent_color[1:3], 16), int(accent_color[3:5], 16), int(accent_color[5:7], 16)
        accent_color_rgb = (r, g, b)
        draw.text((padding, y_offset + 20), f"— {author}", font=author_font, fill=accent_color_rgb)

    return image


def main():
    parser = argparse.ArgumentParser(
        description="文字转卡片生成器 - 将文字内容转换为精美的卡片图片"
    )
    parser.add_argument("text", help="要转换的文字内容")
    parser.add_argument("--style", "-s", default=DEFAULT_STYLE,
                        choices=list(STYLES.keys()),
                        help=f"样式模板 (默认: {DEFAULT_STYLE})")
    parser.add_argument("--width", "-w", type=int, default=800,
                        help="图片宽度 (默认: 800)")
    parser.add_argument("--output", "-o", help="输出文件路径")
    parser.add_argument("--format", "-f", default="png", choices=["png", "jpg", "jpeg"],
                        help="输出格式: png 或 jpg (默认: png)")
    parser.add_argument("--author", "-a", help="作者署名（可选）")

    args = parser.parse_args()

    # 确定输出路径
    if args.output:
        output_path = args.output
    else:
        ext = args.format.lower()
        if ext == "jpg":
            ext = "jpeg"
        output_path = f"card.{ext}"

    # 生成卡片
    print(f"正在生成卡片...")
    print(f"文字: {args.text}")
    print(f"样式: {args.style}")
    print(f"尺寸: {args.width}px 宽")

    image = create_card(args.text, args.style, args.width, args.author)

    # 保存图片
    if args.format.lower() in ["jpg", "jpeg"]:
        image.save(output_path, "JPEG", quality=95, optimize=True)
    else:
        image.save(output_path, "PNG", optimize=True)

    print(f"\n[OK] 卡片已保存到: {output_path}")
    print(f"     尺寸: {image.size[0]} x {image.size[1]} 像素")


if __name__ == "__main__":
    main()
