# product-methodology-skills

两个用于 AI Agent 的**产品方法论 skill**，把"判断方向"和"推进阶段"两件事分别封装成可直接加载的能力。适用于 Claude Code 及兼容 [Agent Skills 规范](https://agentskills.io/specification) 的运行时。

> Two product-methodology skills for AI agents — one diagnoses *whether a direction is worth doing*, the other drives a product *through validated lifecycle stages*. Built for Claude Code and Agent-Skills-compatible runtimes.

**快速安装（Claude Code 插件市场）：**

```text
/plugin marketplace add demon-dy/product-methodology-skills
/plugin install true-demand@product-methodology
/plugin install product-stagegate@product-methodology
```

详见 [安装](#安装)（含手动复制方式）。

## 两个 skill（不同维度，互锁不合并）

| skill | 角色 | 回答什么 | 何时触发 |
|---|---|---|---|
| [`true-demand`](skills/true-demand/SKILL.md) | **诊断罗盘** | 这方向**该不该做**、卡在哪、是不是自嗨 | 模糊的想法 / 卖不动 / 没人用 / 商业模式 / 复盘 |
| [`product-stagegate`](skills/product-stagegate/SKILL.md) | **推进关卡** | 我**走到哪一关**、通没通、下一步 / 该不该止损 | 已在做的项目，问"该投放了吗 / 这是 PMF 吗 / 下一步" |

- **true-demand**：用商业闭环方法，自动判断卡点在「价值 / 共识 / 模式 / 求真」哪一环，给出带量化成败信号的最小验证动作——**不要求用户先把问题分类**。
- **product-stagegate**：按 `Demo → MVP → PMF → GTM → MTU` 五关推进，用真实数据（拒绝"感觉 / 口头反馈 / DAU"）判断是否通关，给下一步动作或止损决定，并先判断项目**是否适用**本框架（合同 / 合规 / 内部工具 / 成熟业务 / 创作类会主动转向）。

**接缝**：true-demand 判完"值得做" → 进 product-stagegate 的 Demo 关；product-stagegate 某一关数字难看 → 回到 true-demand 做"为什么卡"的深度归因。一个是仪表盘和关卡，一个是修理工。

## 安装

本仓库同时是一个 **Claude Code 插件市场**，提供两种安装方式。

### 方式 A：插件市场（推荐，Claude Code）

在 Claude Code 里依次执行：

```text
/plugin marketplace add demon-dy/product-methodology-skills
/plugin install true-demand@product-methodology
/plugin install product-stagegate@product-methodology
```

也可以只 `/plugin marketplace add` 后，在 `/plugin` 面板里浏览这两个插件、按需安装。安装后 skill 即可用，可显式调用 `/true-demand:true-demand`、`/product-stagegate:product-stagegate`，或自然描述产品问题让它按 description 自动触发。更新：`/plugin marketplace update product-methodology`。

### 方式 B：手动复制（任意兼容运行时）

每个 skill 是一个自包含文件夹（`SKILL.md` + `references/`），无外部依赖：

```bash
git clone https://github.com/demon-dy/product-methodology-skills.git
cp -r product-methodology-skills/plugins/true-demand/skills/true-demand             ~/.claude/skills/
cp -r product-methodology-skills/plugins/product-stagegate/skills/product-stagegate ~/.claude/skills/
# 或只在某个项目里用：cp 到该项目的 .claude/skills/ 下
```

重开一个会话即可被发现。其他兼容运行时按各自的 skill 安装方式放入对应目录即可，`SKILL.md` frontmatter 遵循通用 Agent Skills 规范。

## 这两个 skill 是怎么打磨的

不是一次写成，而是用**双 Agent 隔离的 eval 驱动方法**迭代出来的：一个 Agent 负责改（Optimizer），另一个全新上下文的 Agent 只负责按冻结的评分规范独立打分（Evaluator），**优化者不给自己打分**。每个 skill 用 7–8 个覆盖典型场景与失败模式的测试用例多轮迭代到收敛（主指标稳定、用例全过、无回退）。

需要说明：评分由 LLM 评估者给出，是**相对趋势参考，不是绝对真值**。

## 使用须知

- 这两个 skill 是**判断脚手架**，不替代你去接触真实用户、拿真实数据。它们能拦住常见自嗨（把口头反馈 / 问卷 / DAU / 融资当验证），但核查不了你提供信息的真假。
- 输出建议**人工 review** 后再据以决策。
- 数字门槛（60% / 30% / LTV-CAC≥3 等）是业界经验参考值，请结合自己产品形态校准。

## 出处与致谢

- `true-demand` 的方法论提炼自梁宁《真需求》（商业闭环：价值 / 共识 / 模式 / 求真）。本仓库仅是方法论的二次提炼与工程封装，不复制原书内容；建议配合原书阅读。
- `product-stagegate` 来自"科学做产品 × AARRR × 产品生命周期"的团队实践方法论。

## License

[MIT](LICENSE) © 2026 duyu (@demon-dy)
