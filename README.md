# 离线 Skills

这是一份只包含本地工作流、文档处理、写作、分析和工程方法论的 skills 包。

筛选原则：

- 不包含联网搜索能力。
- 不包含浏览器、Chrome、GitHub 平台操作、云平台连接、上传下载、在线发布等外联指令。
- 不包含飞书、企业微信、Canva、NotebookLM、Vercel、YouTube、X/Twitter 等平台型 skills。
- 保留适合离线比赛环境使用的系统级、用户级和项目级 superpowers skills。

## 目录

- `skills/`：用户级通用 skills。
- `superpowers/`：项目级 superpowers 工作流 skills。
- `system-skills/`：筛选后可离线使用的系统级 skills。
- `MANIFEST.md`：完整清单和来源分组。
- `install.ps1`：Windows 本地安装脚本。
- `install.sh`：macOS/Linux 本地安装脚本。

## 安装

先拉取仓库：

```bash
git clone https://github.com/chengdana/offline-skills.git
cd offline-skills
```

Windows PowerShell:

```powershell
.\install.ps1 -Target "$env:USERPROFILE\.codex\skills"
```

macOS/Linux:

```bash
chmod +x ./install.sh
./install.sh "$HOME/.codex/skills"
```

如果你的 AI 平台使用不同的 skills 目录，把目标路径替换成对应目录即可。

## 赛前提醒

这份包只保证包内 `SKILL.md` 不含外联搜索类能力描述。比赛时还需要在运行环境层面关闭或避免使用平台自带的联网工具、浏览器工具、插件连接器和外部检索工具。
