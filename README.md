# personal_skills

在 vibe coding 和 AI 协作开发过程中，持续沉淀的一些方法、判断框架与反思文章。

按内容类型分成三块：可安装的 Agent 技能、方法卡/规则卡、反思文章。

## Skills — 可安装的 Agent 技能

SKILL.md 格式，可安装或引用到项目中。

### [attention-safe-orchestration](./skills/attention-safe-orchestration/)

让多个 Agent 并发工作时，只在明确的决策和验收节点消耗人类注意力；把工作路由到既有技能，不重复实现。

- [技能入口](./skills/attention-safe-orchestration/SKILL.md)
- [使用说明](./skills/attention-safe-orchestration/README.md)
- [设计文档](./skills/attention-safe-orchestration/docs/)

### [architecture-first-design](./skills/architecture-first-design/)

当改动可能触及所有权边界、公共 API/协议、持久化、权限、产物、生命周期、兼容性或跨包时，先产出有证据支撑的架构文档，再进入实现。

- [技能入口](./skills/architecture-first-design/SKILL.md)

### [vibe-debug-with-evidence](./skills/vibe-debug-with-evidence/)

在 vibe coding 里排查复杂 Bug 时，先冻结症状、收集日志与可证伪证据，再动手修复，避免陷入「读代码→猜原因→打补丁」的循环。

- [技能入口](./skills/vibe-debug-with-evidence/SKILL.md)
- [调试手册](./skills/vibe-debug-with-evidence/references/ai-debugging-playbook.md)

## Methods — 方法卡 & 规则卡

可直接复制到项目的 AGENT.md / CLAUDE.md，或作为方法参考长期查阅。

- [Agent Execution Budget](./methods/agent-execution-budget.md) — 把慢构建/测试/静态检查当作有限预算，而非每次编辑后必跑的命令
- [Keep System Simple](./methods/keep-system-simple.md) — 先建立可验证的最小工作闭环，再按明确需要增加能力
- [System Architecture Review](./methods/system-architecture-review.md) — 从「任务级设计」走向「系统级设计」的检查方法

## Blog — 反思文章

- [从 Vibe Coding 到系统级设计](./blog/2026-07-11-from-vibe-coding-to-system-design.md)（2026-07-11）
- [不要把一句话，当作给 Agent 的全权委托](./blog/2026-07-30-agent-control-and-evaluation.md)（2026-07-30）
- [当 Agent 开始修改自己，它已经开始帮我干活了](./blog/2026-08-05-when-agent-starts-helping.md)（2026-08-05）
- [在 vibe coding 里，如何约束 AI 处理复杂 Bug](./blog/vibe-coding-ai-debugging-methodology.md)
- [配置不是表单状态](./blog/2026-08-13-configuration-is-a-runtime-boundary.md)（2026-08-13）
- [能完成一次任务之后，Agent 还要学会连续工作](./blog/2026-08-13-long-running-agent-tasks.md)（2026-08-13）

## 维护原则

- 三个顶层目录按内容类型区分：`skills/`（技能）、`methods/`（方法/规则卡）、`blog/`（反思文章）
- 优先沉淀可复用的方法，而不只是一次性的任务记录
- 反思文章用「日期-英文-slug」命名，方法卡与方法说明互相链接
