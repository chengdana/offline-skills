#!/usr/bin/env python3
"""
文字转卡片生成器 - HTML渲染版本
使用HTML+CSS渲染，完美支持中文换行和排版
"""

import argparse
import os
import sys
import subprocess

# 添加 styles.py 路径
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from styles import STYLES, DEFAULT_STYLE

# 样式对应的CSS配色
CSS_COLORS = {
    "brutalist": {
        "bg": "#000000",
        "text": "#FFFFFF",
        "accent": "#FF0000",
    },
    "sunset": {
        "bg": "linear-gradient(135deg, #FF6B35 0%, #F7C59F 100%)",
        "text": "#2D132C",
        "accent": "#2D132C",
    },
    "forest": {
        "bg": "#2D4A3E",
        "text": "#E8F5E9",
        "accent": "#A5D6A7",
    },
    "pastel": {
        "bg": "#FFF0F5",
        "text": "#4A4A4A",
        "accent": "#DDA0DD",
    },
    "industrial": {
        "bg": "#1E3A5F",
        "text": "#E8E8E8",
        "accent": "#FF6B35",
    },
    "minimal": {
        "bg": "#FFFFFF",
        "text": "#1A1A1A",
        "accent": "#666666",
    },
    "ocean": {
        "bg": "linear-gradient(135deg, #0EA5E9 0%, #0284C7 100%)",
        "text": "#FFFFFF",
        "accent": "#BAE6FD",
    },
    "warm": {
        "bg": "#F5E6D3",
        "text": "#3D2914",
        "accent": "#C9A66B",
    },
    "mint": {
        "bg": "#ECFDF5",
        "text": "#064E3B",
        "accent": "#6EE7B7",
    },
    "dark": {
        "bg": "#0F0F0F",
        "text": "#E5E5E5",
        "accent": "#404040",
    },
}


def create_html(text, style_name="minimal", width=800, author=None):
    """创建HTML文件"""
    colors = CSS_COLORS.get(style_name, CSS_COLORS["minimal"])

    html = f"""<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <style>
        * {{
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }}
        body {{
            width: {width}px;
            min-height: 200px;
            padding: 60px;
            background: {colors['bg']};
            font-family: "Microsoft YaHei", "PingFang SC", -apple-system, BlinkMacSystemFont, sans-serif;
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
        }}
        .content {{
            width: 100%;
        }}
        .text {{
            color: {colors['text']};
            font-size: 42px;
            font-weight: bold;
            line-height: 1.6;
            text-align: center;
            white-space: pre-wrap;
            word-break: break-word;
        }}
        .author {{
            margin-top: 40px;
            color: {colors['accent']};
            font-size: 24px;
            text-align: center;
        }}
    </style>
</head>
<body>
    <div class="content">
        <div class="text">{text}</div>
        {f'<div class="author">— {author}</div>' if author else ''}
    </div>
</body>
</html>"""
    return html


def html_to_image(html_path, output_path, width=800):
    """使用playwright将HTML转换为图片"""
    try:
        from playwright.sync_api import sync_playwright
        with sync_playwright() as p:
            browser = p.chromium.launch()
            page = browser.new_page(viewport={'width': width, 'height': 1000})
            page.goto(f'file:///{html_path.replace("\\", "/")}')
            # 等待页面加载完成
            page.wait_for_load_state('networkidle')

            # 获取实际内容高度
            body_height = page.evaluate('document.body.scrollHeight')
            page.set_viewport_size({'width': width, 'height': body_height})

            # 截图
            page.screenshot(path=output_path, full_page=True)
            browser.close()
        return True
    except ImportError:
        return False
    except Exception as e:
        print(f"Playwright error: {e}")
        return False


def main():
    parser = argparse.ArgumentParser(
        description="文字转卡片生成器 - HTML渲染版本"
    )
    parser.add_argument("text", help="要转换的文字内容")
    parser.add_argument("--style", "-s", default=DEFAULT_STYLE,
                        choices=list(CSS_COLORS.keys()),
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
        output_path = f"card.{args.format}"

    # 创建HTML
    html = create_html(args.text, args.style, args.width, args.author)

    # 保存HTML文件
    html_path = output_path.replace('.png', '.html').replace('.jpg', '.html').replace('.jpeg', '.html')
    with open(html_path, 'w', encoding='utf-8') as f:
        f.write(html)

    print(f"正在生成卡片...")
    print(f"文字: {args.text[:50]}...")
    print(f"样式: {args.style}")
    print(f"尺寸: {args.width}px 宽")

    # 尝试使用playwright
    if html_to_image(html_path, output_path, args.width):
        print(f"\n[OK] 卡片已保存到: {output_path}")
        os.remove(html_path)  # 删除临时HTML文件
    else:
        print(f"\n[INFO] 未安装 playwright，请手动操作：")
        print(f"1. 安装 playwright: pip install playwright && playwright install chromium")
        print(f"2. 或者用浏览器打开: {html_path}")
        print(f"3. 然后截图保存为: {output_path}")


if __name__ == "__main__":
    main()
