# agent.md

本仓库（personal_skills）是个人知识库，沉淀在 vibe coding 与 AI 协作开发过程中积累的方法、判断框架与反思文章。Agent 在本仓库操作时，请先阅读本文件了解结构与约定。

## 目录结构

```text
personal_skills/
├── agent.md                        # 本文件：结构与约定（供 Agent 阅读）
├── README.md                       # 总索引（供人阅读）
├── skills/                         # 可安装的 Agent 技能（SKILL.md 格式）
│   ├── attention-safe-orchestration/
│   │   ├── SKILL.md                # 技能入口（front matter 含 name/description）
│   │   ├── README.md
│   │   ├── docs/                   # 设计/计划/验证 历史文档
│   │   ├── references/             # 模板、示例、安装与回滚说明
│   │   └── scripts/                # 配套脚本（如 taskctl.py）
│   ├── architecture-first-design/
│   │   ├── SKILL.md
│   │   └── agents/                 # 平台适配配置（如 openai.yaml）
│   └── vibe-debug-with-evidence/
│       ├── SKILL.md
│       └── references/             # 调试手册
├── methods/                        # 方法卡 & 规则卡（单文件，可复制到项目 AGENT.md/CLAUDE.md）
│   ├── agent-execution-budget.md
│   ├── keep-system-simple.md
│   └── system-architecture-review.md
└── blog/                           # 反思文章（中文，命名：YYYY-MM-DD-英文-slug.md）
    └── YYYY-MM-DD-slug.md
```

## 三类内容

- **skills/** — 可安装/可引用的 Agent 技能。每个技能一个目录，目录名 = SKILL.md front matter 里的 `name`。除 SKILL.md 外，可含 references/、scripts/、agents/、docs/ 等配套目录。
- **methods/** — 方法卡与规则卡。单文件 markdown，内容可直接复制进项目指令，或作为方法参考长期查阅。
- **blog/** — 中文反思文章。文件名用「日期-英文-slug」命名，内容与方法卡可互相链接。

## 约定

- 新增内容按类型放入对应顶层目录，不要混放。
- 优先沉淀可复用的方法，而非一次性任务记录。
- 方法卡与反思文章之间的引用使用相对路径链接。
- 技能目录命名与 SKILL.md 的 `name` 保持一致（如 `vibe-debug-with-evidence`，不带 `-skill` 后缀）。
- 改动或新增文件后，同步更新根目录 README.md 的索引。
- 本仓库是 git 仓库；移动文件请用 `git mv` 保留历史。
