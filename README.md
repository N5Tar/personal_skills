# personal_skills

在 vibe coding 和 AI 协作开发过程中，持续沉淀的一些方法、判断框架与反思文章。

## 当前内容

### [agent-orchestration](./knowledge/agent-orchestration/)

围绕 Agent 控制权分配、验证预算、上下文边界，以及“受限推理”与“自主编排”两种模式的思考沉淀。

- [反思文章：不要把一句话，当作给 Agent 的全权委托](./knowledge/agent-orchestration/2026-07-30-agent-control-and-evaluation.md)

### [agent-execution-budget](./knowledge/agent-execution-budget/)

一份可复制到项目 Agent 指令中的短规则卡，用于约束编码 Agent 对慢构建、测试、格式化和静态检查的执行预算。

- [Agent Execution Budget](./knowledge/agent-execution-budget/agent-execution-budget.md)

### [keep-system-simple](./knowledge/keep-system-simple/)

一份可复制到项目 Agent 指令中的短规则卡，先建立可验证的最小工作闭环，再按明确的任务需要增加能力，并让协作保持可观察、可控制、可审阅与可恢复。

- [Keep System Simple](./knowledge/keep-system-simple/keep-system-simple.md)

### [system-architecture-review](./knowledge/system-architecture-review/README.md)

围绕“从任务级设计走向系统级设计”的一组知识沉淀，包含：

- 一份整理自 Codex skill `system-architecture-review` 的方法说明
- 一篇关于从 vibe coding 走向系统级设计的反思文章

具体文件：

- [方法说明](./knowledge/system-architecture-review/README.md)
- [反思文章：从 Vibe Coding 到系统级设计](./knowledge/system-architecture-review/blog/2026-07-11-from-vibe-coding-to-system-design.md)

## 维护原则

- 每个主题尽量形成独立目录，方便持续扩展
- 优先沉淀可复用的方法，而不只是一次性的任务记录
- 反思文章和方法说明分开存放，但彼此互相链接
