"""
文字转卡片样式定义
参考 frontend-design 美学指南，避免陈词滥调的配色方案
"""

# 样式配置
STYLES = {
    # === 野兽派极简主义 ===
    "brutalist": {
        "background": "#000000",
        "text_color": "#FFFFFF",
        "accent_color": "#FF0000",
        "font_size_title": 52,
        "font_size_author": 20,
        "padding": 60,
        "shadow": False,
        "gradient": None,
    },

    # === 复古未来主义 ===
    "sunset": {
        "gradient": ("#FF6B35", "#F7C59F"),
        "text_color": "#2D132C",
        "accent_color": "#2D132C",
        "font_size_title": 48,
        "font_size_author": 22,
        "padding": 80,
        "shadow": False,
    },

    # === 有机自然 ===
    "forest": {
        "background": "#2D4A3E",
        "text_color": "#E8F5E9",
        "accent_color": "#A5D6A7",
        "font_size_title": 46,
        "font_size_author": 20,
        "padding": 70,
        "shadow": False,
        "gradient": None,
    },

    # === 柔和粉彩 ===
    "pastel": {
        "background": "#FFF0F5",
        "text_color": "#4A4A4A",
        "accent_color": "#DDA0DD",
        "font_size_title": 44,
        "font_size_author": 20,
        "padding": 75,
        "shadow": False,
        "gradient": None,
    },

    # === 工业实用主义 ===
    "industrial": {
        "background": "#1E3A5F",
        "text_color": "#E8E8E8",
        "accent_color": "#FF6B35",
        "font_size_title": 48,
        "font_size_author": 20,
        "padding": 70,
        "shadow": False,
        "gradient": None,
    },

    # === 极简白 ===
    "minimal": {
        "background": "#FFFFFF",
        "text_color": "#1A1A1A",
        "accent_color": "#666666",
        "font_size_title": 48,
        "font_size_author": 24,
        "padding": 80,
        "shadow": False,
        "gradient": None,
    },

    # === 深海 ===
    "ocean": {
        "gradient": ("#0EA5E9", "#0284C7"),
        "text_color": "#FFFFFF",
        "accent_color": "#BAE6FD",
        "font_size_title": 48,
        "font_size_author": 22,
        "padding": 80,
        "shadow": False,
    },

    # === 芥末暖色 ===
    "warm": {
        "background": "#F5E6D3",
        "text_color": "#3D2914",
        "accent_color": "#C9A66B",
        "font_size_title": 50,
        "font_size_author": 22,
        "padding": 70,
        "shadow": False,
        "gradient": None,
    },

    # === 薄荷清新 ===
    "mint": {
        "background": "#ECFDF5",
        "text_color": "#064E3B",
        "accent_color": "#6EE7B7",
        "font_size_title": 46,
        "font_size_author": 20,
        "padding": 75,
        "shadow": False,
        "gradient": None,
    },

    # === 深色模式 ===
    "dark": {
        "background": "#0F0F0F",
        "text_color": "#E5E5E5",
        "accent_color": "#404040",
        "font_size_title": 48,
        "font_size_author": 24,
        "padding": 80,
        "shadow": False,
        "gradient": None,
    },
}

DEFAULT_STYLE = "minimal"

# 样式说明
STYLE_DESCRIPTIONS = {
    "brutalist": "野兽派极简 - 黑白高对比，大胆强烈",
    "sunset": "复古未来 - 日落橙黄渐变，温暖怀旧",
    "forest": "有机自然 - 森林深绿，自然宁静",
    "pastel": "柔和粉彩 - 淡粉糖果色，温柔可爱",
    "industrial": "工业实用 - 深蓝金属风，专业冷静",
    "minimal": "极简白 - 纯白极简，经典永恒",
    "ocean": "深海 - 蓝色渐变，清新辽阔",
    "warm": "芥末暖色 - 米黄大地，温暖舒适",
    "mint": "薄荷清新 - 清新薄荷，清爽自然",
    "dark": "深色模式 - 纯黑深色，护眼舒适",
}
