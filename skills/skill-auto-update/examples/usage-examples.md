# 技能自更新使用示例

本文档包含详细的使用示例和输出格式说明。

## 使用场景

### 示例 1：指定技能更新

```
用户: /skill-auto-update wechat-article-generator
Claude: 好的，我来帮你优化 wechat-article-generator 技能。

[收集反馈...]
问题 1: 这次使用有哪些不满意的地方？
[用户选择：工作流程步骤太复杂]

问题 2: 你希望技能在哪方面改进？
[用户选择：优化工作流程和执行逻辑]

问题 3: 请具体描述你的改进建议
[用户输入：希望能自动检查即梦服务是否启动，不用每次手动确认]

[分析、更新、生成报告...]
```

### 示例 2：自动识别最近使用的技能

```
用户: /skill-auto-update
Claude: 检测到你最近使用了 ppt-designer 技能，要优化这个技能吗？

[后续流程同上...]
```

### 示例 3：批量反馈多个优化点

```
用户: /skill-auto-update markdown-to-word
我希望：
1. 支持更多 Markdown 语法（如删除线、任务列表）
2. 优化表格样式，支持合并单元格
3. 增加转换进度提示

Claude: 收到你的 3 点反馈，我来逐一优化...
[自动分类并更新对应部分...]
```

## 输出格式

### 更新成功

```
✅ 技能更新完成！

📋 更新摘要:
- 技能名称: wechat-article-generator
- 更新部分: 3 处
  • description 字段优化
  • 工作流程简化（合并步骤 6-7）
  • 新增自动服务检测功能

📄 详细报告已生成
请查看上方的完整更新报告。

💡 建议:
重新调用 /wechat-article-generator 测试新流程是否更流畅。
```

### 更新失败

```
❌ 技能更新失败

原因: 未找到技能文件 "xyz-skill"

建议:
1. 检查技能名称是否正确
2. 运行以下命令查看所有可用技能:
   find .claude/skills -name "SKILL.md"
3. 如果技能在个人目录，请检查 ~/.claude/skills/
```

### 需要拆分时

```
⚠️ 技能文件过长，建议拆分

当前状态:
- 文件: wechat-article-generator/SKILL.md
- 行数: 520 行（超过 500 行限制）

拆分建议:
1. 移动"详细配图规范" → reference/image-rules.md (约 80 行)
2. 移动"标题模板大全" → reference/title-templates.md (约 60 行)
3. 移动"完整示例" → examples/complete-example.md (约 100 行)

预计拆分后: SKILL.md 约 280 行 ✅

是否执行拆分? (y/n)
```
