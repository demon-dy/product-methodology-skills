---
name: product-stagegate
description: Use when someone is building or running a new product (C-end or small-B SaaS, 0→1 / 1→10) and needs to know which stage it is at, whether it has passed the current gate, or what to do next. Symptoms include "should I start advertising / scaling now", "users love it on first try — is this PMF", "DAU is growing so we're good", "我做了访谈接下来做什么", confusing activation with retention, jumping stages, judging progress by feelings/口头反馈 instead of behavioral data, or needing to decide whether this staged-validation framework even applies (vs contract/compliance/internal-tool/mature/creative projects). Keywords: AARRR, Demo, MVP, PMF, GTM, MTU, 激活率, 留存曲线, Sean Ellis, LTV/CAC, 通关, 阶段评审, 止损.
---

# product-stagegate

把产品按 **Demo → MVP → PMF → GTM → MTU** 五关推进:每关只回答一个核心问题、验一个核心假设、看一个核心指标;**前一关没过不许进下一关**。核心是把"感觉做对了"换成"数据证明通关了"。

## 第 0 步:适用性预检(不通过就别用本框架)

本框架只适合"面向真实用户、方向待验证、输得起小赌不输得起大赌"的新产品。先排除:

| 项目类型 | 不适用，改用 |
|---|---|
| ToG/大客户强合同定制 | 项目管理（范围/工期/验收），不验 PMF |
| 监管/合规驱动功能 | 合规检查清单 + 安全设计 |
| 内部工具/纯技术基础设施 | 需求收集→原型→内测迭代，看任务耗时/错误率 |
| 已成熟业务做精细化运营 | OKR + 分层指标 A/B 优化 |
| 创作/内容类（重主观品质） | 定性研究+同行评审+核心粉丝，数据仅辅助 |

命中任一 → **明确转向对应思路，不要硬套阶段和 AARRR**。详见 `references/applicability.md`。

## 工作流

```
1. 适用性预检（上表）→ 不适用就转向，别往下走
2. 定位当前阶段：用自检表（references/self-check.md）
3. 取该关的核心问题 / 核心指标 / 通关标准（references/stages.md）
4. 用真实数据判断通没通——不接受"我觉得 / 大家都说 / 口头愿意"
5. 通关 → 给跃迁判断 + 下一关该验什么
   未通关 → 先按「关卡没过→归因」表归到价值/共识/模式/求真某类（转 true-demand 深挖），再给该关最该做的一个动作（带数字目标和失败信号）
6. 检查止损线（references/self-check.md）：是否该停下来做方向复盘
全程套 6 原则（references/principles.md），尤其：数据说话、假设证伪、区分观察与解释、结论可操作
```

## 五关速查

| 阶段 | 核心问题 | 核心指标 | 通关标准（经验参考值） |
|---|---|---|---|
| Demo | 问题值得解决吗 | 访谈痛点确认率 | ≥60% 确认 + 找不到足够反例 |
| MVP | 最小可交付价值？愿付费吗 | 激活率 + 支付意愿转化率 | 激活 ≥30% + 支付意愿 ≥10% |
| PMF | 市场真的要吗 | 留存曲线 + Sean Ellis | 曲线趋平 + ≥40% |
| GTM | 怎么可持续获客 | LTV/CAC | ≥3 且回收期 <12 月 |
| MTU | 飞轮能自转吗 | 自然增长占比 | >30%，K-factor 上升 |

数字是讨论基准、不是机械硬门槛（不同产品/人群/市场有差异）；但"用感觉替代数字"永远不允许。操作化定义、常见错、例子见 `references/stages.md`。

## 每次输出必须包含（输出契约）

不止于"你在 X 关"。每次回答都要落到一个可执行动作，带三件套：

1. **当前阶段判定** + 一句为什么（基于自检表，不基于感觉）。
2. **最该做的一个动作**（不是一串清单，是当前杠杆最大的那一个；未通关给"补这关"的动作，通关给"下一关验什么"的动作）。
3. **数字目标 + 失败信号**：这个动作做到什么数算成、做不到什么数就触发止损/方向复盘。

> 例（未过 PMF）：「你在 PMF 关，留存还没趋平。下一步只做一件事：把 Day30 留存和 Sean Ellis 测出来（≥30 位活跃用户）。趋平且 Sean Ellis ≥40% 才进 GTM；若运营满 3 个月仍不趋平、Sean Ellis <25%，触发方向复盘。」

## 关卡没过 → 归因（与 true-demand 合成闭环，不依赖外部 Agent）

本 skill 定位"卡在哪一关"，但**为什么卡、该补哪一类**由 `true-demand` skill 回答。两者是一个闭环：定位到某关没过后，**不要止步于"去测某指标"**，先按下表把失败归到「价值/共识/模式/求真」哪一类，再转入 `true-demand` 对该类深挖，最后落到一个最小验证动作。这一步在**同一会话内**完成——你（当前模型）依次读取并应用两个 skill 即可，无需第二个 Agent。

| 卡在哪一关 | 最可能的归因类别 | 进 true-demand 读 |
|---|---|---|
| Demo 不过（问题不被确认） | 价值·真需求 / 求真（是否伪需求、是否应然想象） | `value-models` + `truth-seeking` |
| MVP 激活不够 | 价值·感知 / 共识·场景 | `value-models` + `consensus-tools` |
| MVP 不付费 | 价值（功能/情绪/资产哪类撑定价）/ 求真（口头≠付费） | `value-models` + `truth-seeking` |
| PMF 留存差 | 价值深度（功能用完即走？缺情绪/资产钩子）/ 共识（人设·场景）/ 求真（指标或应然假设读错） | `value-models` + `consensus-tools` + `truth-seeking` |
| GTM 不成立 | 模式（拿谁的钱/能力系统/安全边界） | `mode-design` |
| MTU 不转 | 模式 / 共识·关系（认同·归属才会推荐） | `mode-design` + `consensus-tools` |

**归因给的是"最可能的 1–2 类原因 + 该测什么"的假设，不是判决。** 确证哪类是真因，必须回到真实用户/数据——这正是接下来那个最小验证动作要暴露的。当 true-demand 判定"价值成立、值得做"时，反向交回本 skill 的 Demo 关开始分阶段验证。

## 三条铁律（最常被违反）

1. **不许跳关**：Demo 没过不许投放；留存没趋平不许大规模买量。跳关不是省时间，是透支未来。
2. **激活 ≠ 留存**：第一次用得爽是新奇效应，不是 PMF。PMF 必须等 Day30 留存 + Sean Ellis。
3. **行为 > 言语**：「说喜欢/说会买」不算证据，要 Fake door 点击、预付、真实复用这类行为数据。

## 何时读哪个 reference

| 你要做的事 | 读 |
|---|---|
| 判断在哪一关 / 该不该止损 | `references/self-check.md` |
| 某关的标准、操作化定义、怎么测 | `references/stages.md` |
| AARRR 与名词不懂 | `references/aarrr.md` |
| 谁来评审、交什么材料、和 OKR/敏捷的关系 | `references/review-mechanism.md` |
| 项目到底适不适用本框架 | `references/applicability.md` |
| 高频死法对照 | `references/death-traps.md` |
| 怎么想（6 原则） | `references/principles.md` |

## 反模式（必须避免）

- 对不适用项目硬套阶段和 AARRR
- 用 DAU/增长好看的数字替代留存判断
- 把"想清楚/再观察"当结论（不可操作）
- 把口头反馈、问卷好评、融资到账当通关证据
- 连续不通关还无限重试，不触发止损
