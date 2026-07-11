# System Architecture Review

围绕系统架构复盘与长期可维护性设计的一张方法卡。内容整理自 Codex skill `system-architecture-review`，并转成更适合作为个人知识仓库长期查阅的形式。

## 这份内容解决什么问题

很多设计只解决“这次怎么做完”，却没有解决“以后怎么不做乱”。

`system-architecture-review` 这套方法的价值，在于把注意力从单次任务推进到系统的长期认知结构，重点检查：

- 核心概念是否稳定
- 模块边界是否清晰
- 生命周期、协议、持久化、UI、编排职责是否混杂
- 文档是在描述当前设计，还是只是在归档历史

## 适用场景

适合在下面这些时候使用：

- 项目做了一段时间，开始怀疑结构在变乱
- 某个模块越来越像“什么都能放进去”的地方
- 需要在设计文档和代码之间重新对齐概念边界
- 连续完成多个任务后，想把局部合理的修改重新收束成系统级结构
- 想把一次重构、复盘或开发经验，沉淀成更稳定的架构判断

## 核心立场

这套方法不是为了制造大重构，而是为了恢复清晰的认知边界。

做 review 时，优先看这些问题：

- 名字是否对应真实职责
- 哪些模块正在吸收不该属于自己的生命周期问题
- 协议边界是显式存在，还是被埋进实现细节
- 扩展点和持久化流程是设计出来的，还是后补进去的
- 文档是否还在教授当前系统，而不是堆积历史噪音

## 方法流程

### 1. 先建立当前上下文

优先看已有设计文档、核心模块、最近计划和用户真正担心的问题。不要只从零散代码反推架构。

### 2. 定义核心概念

为系统中的关键对象各写一句定义，并明确它“不应该拥有什么”。

例如：

- `Session` 是长期上下文，不应该顺手变成所有执行细节的容器
- `Run` 是一次输入触发的执行，不应该承担长期状态归档
- `RunStep` 是一次可审计的处理痕迹，不应该兼任高层编排

### 3. 画关系，而不是只列模块

当关系、事件流、生命周期边界是重点时，用图把它们画出来。图不是装饰，而是用来验证职责是否真的分开。

### 4. 检查耦合与漂移

重点寻找：

- 过载模块
- 隐含协议边界
- 重复状态
- 模糊命名
- 持久化副作用散落在主流程中

### 5. 区分任务级问题和系统级问题

- 任务级问题：会阻塞当前修改
- 系统级问题：会让未来的修改越来越容易做错

这两类问题不能混在一起，否则 review 很容易退化成一次普通 bug triage。

### 6. 给出目标结构

目标不是把模块越拆越多，而是找到更少、更锋利的边界。

### 7. 更新合适的产物

根据场景，输出应该落到明确载体上，例如：

- 架构评审记录
- 关系图
- 设计文档
- 重构提案
- 复盘文章

### 8. 落到下一步动作

最后必须收束成具体动作，例如：

- 哪份文档需要更新
- 哪个边界应该先收紧
- 哪些测试能守住新结构
- 哪个设计决策需要先拍板

## 常用追问

做 review 时，不需要机械回答全部问题，但这些问题很容易暴露系统真实风险：

- 系统里长期存在的上下文单元是什么？
- 一次执行实例到底是什么？
- 什么东西才算一个可审计的处理步骤？
- 谁拥有生命周期，谁只是执行者？
- 协议转换是一个真正的边界，还是正在泄漏到运行时和 UI 中？
- usage、审计、持久化应该挂在哪一层？
- 未来加一个新能力时，它会自然落到现有边界，还是逼人绕路？
- 文档是在教当前系统，还是只保存历史噪音？

## 典型输出模板

### 架构评审

```md
## Findings

- [Severity] Finding with file/doc reference and why it matters.

## Target Model

Short description of the desired concept boundaries.

## Relationship Diagram

Mermaid diagram if useful.

## Recommended Changes

Concrete changes, ordered by architectural leverage.

## Open Decisions

Only decisions that materially affect the design.
```

### 反思文章

```md
# Title

Opening insight.

## What I Used To Think

The previous working model and why it was insufficient.

## What Became Clear

The conceptual shift.

## The Method

The reusable way of working.

## What I Will Do Differently

Practical future behavior.
```

## 使用边界

这套方法有几个明确约束：

- 不要把每次 review 都导向大重构
- 不要把所有模块说明塞进一篇巨型文档
- 不要让图只是装饰
- 不要为了“模式完整”制造过多用户可见模式
- 如果结构已经过载，要直接指出问题，而不是用局部修补掩盖

## 相关内容

- [反思文章：从 Vibe Coding 到系统级设计](./blog/2026-07-11-from-vibe-coding-to-system-design.md)
