---
name: text-to-card
description: 文字转卡片/海报生成器。将文字内容转换为精美的卡片或海报图片，适合社交媒体分享。支持 PNG 和 JPG 输出格式，10 种预设样式模板（参考 frontend-design 美学指南）。当用户请求：将文字转为图片、生成卡片、制作海报、文字转图、分享卡片时使用此技能。
---

# Text to Card

将文字内容转换为精美的卡片或海报图片。

## 设计理念

参考 frontend-design 美学指南，避免陈词滥调的配色方案（如紫色渐变），提供多种独特的美学风格。

## 快速开始

### 基础用法

```bash
python scripts/generate.py "你的文字内容"
```

### 指定样式

```bash
python scripts/generate.py "你的文字内容" --style brutalist --author "@作者"
```

## 可用样式模板

| 样式名 | 美学风格 | 适用场景 |
|--------|----------|----------|
| `brutalist` | 野兽派极简 - 黑白高对比，大胆强烈 | 艺术语录、强烈表达 |
| `sunset` | 复古未来 - 日落橙黄渐变，温暖怀旧 | 复古主题、温暖内容 |
| `forest` | 有机自然 - 森林深绿，自然宁静 | 自然主题、环保内容 |
| `pastel` | 柔和粉彩 - 淡粉糖果色，温柔可爱 | 可爱内容、少女心 |
| `industrial` | 工业实用 - 深蓝金属风，专业冷静 | 科技主题、商务内容 |
| `minimal` | 极简白 - 纯白极简，经典永恒 | 日记、名言、简洁内容 |
| `ocean` | 深海 - 蓝色渐变，清新辽阔 | 清新主题、夏日内容 |
| `warm` | 芥末暖色 - 米黄大地，温暖舒适 | 温暖主题、治愈内容 |
| `mint` | 薄荷清新 - 清新薄荷，清爽自然 | 清新主题、健康内容 |
| `dark` | 深色模式 - 纯黑深色，护眼舒适 | 夜间阅读、深色偏好 |

## 参数说明

```
usage: generate.py [-h] [--style STYLE] [--width WIDTH] [--output OUTPUT]
                   [--format FORMAT] [--author AUTHOR]
                   text

positional arguments:
  text                  要转换的文字内容

options:
  -h, --help            显示帮助信息
  --style STYLE         样式模板 (默认: minimal)
  --width WIDTH         图片宽度 (默认: 800)
  --output OUTPUT       输出文件路径
  --format FORMAT       输出格式: png 或 jpg (默认: png)
  --author AUTHOR       作者署名（可选）
```

## 输出格式支持

- **PNG**: 支持透明背景，高质量
- **JPG**: 文件较小，兼容性好

## 样式自定义

每种样式的配色方案可在 `scripts/styles.py` 中修改。

## 示例

```bash
# 野兽派风格 - 大胆强烈
python scripts/generate.py "Stay Hungry, Stay Foolish" --style brutalist

# 复古日落 - 温暖怀旧
python scripts/generate.py "那些年我们一起追过的梦" --style sunset --author "@青春"

# 森林自然 - 宁静绿色
python scripts/generate.py "大自然是最好的治愈师" --style forest

# 工业科技 - 专业冷静
python scripts/generate.py "Code is Poetry" --style industrial --author "@Dev"

# 深海清新 - 蓝色渐变
python scripts/generate.py "海阔凭鱼跃，天高任鸟飞" --style ocean --format jpg
```
