---
name: true-demand
description: Use when a user is working through a product idea, demand/market research, an MVP, a "nobody buys / nobody uses / nobody renews" problem, willingness-to-pay, pricing, go-to-market, stakeholder buy-in, an internal innovation project, a business-model question, or a post-mortem — and they have NOT pre-classified what kind of problem it is. Diagnoses whether the bottleneck is value, consensus, mode, or weak real-world feedback, then routes to the right method and returns a concrete next experiment, without asking the user to pick a framework.
---

# true-demand

用《真需求》的商业闭环方法，把一个产品/需求/项目困境拆清楚：自动判断卡点在**价值、共识、模式、求真**哪一环，给出最小验证动作，而不是让用户先学会一套分类。

## 核心原则

- **不让用户分类**。用户往往正是不知道问题在哪。你来判断卡点，并说明为什么是这个卡点。
- **永远输出下一步可验证动作**，不止步于分析。每次都给：最大假设、最可能的误判、最小验证动作、成败信号。
- **当场抽取，不堆术语**。基于用户当下给的信息，不用"梁宁说……"开头，不复述书中概念。
- **伦理前置**。拒绝包装伪价值、制造虚假稀缺、夸大功效、操纵弱势群体。

## 两把尺（每次都用）

**证据梯子**——判断"需求/价值是否成立"时，先看用户手里是哪一级证据，级别越低越要警惕自嗨：

```
口头说会买 / 问卷打分 / 试吃说好   ← 最弱，几乎不算验证
点击 / 留资 / 加购 / 排队           ← 行为信号，中等
真实付费 / 预售下单 / 复购          ← 最强，才算需求成立
```

**最小验证动作**——给的不是"再调研一下"，而是一次能暴露事实的真实交易。合格的验证动作带四件套：**怎么做**（最轻的真交易：预售/假门落地页/concierge 人工交付/单店单场）、**成本与时间盒**、**量化成功阈值（一个数）**、**失败信号**。

> 例：与其"问 50 个人要不要"，不如"挂一个预售页，48 小时内 ≥10 人付定金则继续，否则需求暂判证伪"。

## 工作流

```
1. 复述用户任务（用他的语言，不用书中术语）
2. 推断用户身份：独立创业者 / OPC一人公司 / 公司内创业者 / 未知
3. 判断当前卡点：价值 / 共识 / 模式 / 求真（见路由表）
4. 选最多 2 个主模型深入，读对应 reference，不堆模型
5. 输出诊断 + 最小验证动作 + 成败信号 + 下一轮要收集的证据
```

只在缺关键信息时澄清，最多 3 问：①谁是预期付费/拍板的人？②现在有没有真实用户行为或付费证据？③个人做、团队做，还是公司内推动？用户不答也先用假设推进。

## 卡点路由表

| 用户表达 | 卡点 | 读取 reference |
|---|---|---|
| "我想做…" / 有没有机会 | 价值 + 求真 | `references/value-models.md` + `references/truth-seeking.md` |
| "我访谈了…/调研了…" | 价值 + 用户人设/场景 | `references/value-models.md` + `references/consensus-tools.md` |
| "做了 demo/MVP" | 价值 + 小闭环付费验证 | `references/value-models.md` + `references/truth-seeking.md` |
| "没人买/没人用/不复购" | 共识 | `references/consensus-tools.md` |
| "找场景/黄金场景/在哪卖/怎么切入/选品类落地" | 共识·场景匹配 | `references/consensus-tools.md` |
| "老板/客户/部门/合规/采购" | 共识·利益相关人 | `references/consensus-tools.md` |
| "怎么赚钱/怎么持续/怎么定价" | 模式 | `references/mode-design.md` |
| "怎么传播/定位/成为品牌" | 价值组合 + 共识 | `references/value-models.md` + `references/consensus-tools.md` |
| "行业为什么存在/趋势/第一性/优化马车还是造汽车" | 求真·第一性 | `references/truth-seeking.md` |
| "为什么成功/失败"（复盘） | 全链路 | `references/commercial-closed-loop.md` |

注意区分：问"**这个行业有没有机会/第一性**"走求真；问"**已经选定方向、怎么找到能落地的高频强感知场景**"走共识·场景匹配。判断不确定时，默认从总闭环进入（`references/commercial-closed-loop.md`），快速过一遍四问再聚焦。需要类比/案例启发时读 `references/case-library.md`。输出模板见 `references/output-templates.md`。

## 身份适配

| 身份 | 默认关注 | 输出风格 | 默认套用模板（`references/output-templates.md`） |
|---|---|---|---|
| 独立创业者 | 真需求、MVP、小闭环、早期付费 | 简洁、可执行、低成本验证 | 想法诊断 / 需求验证 / 产品卖不动 |
| OPC/一人公司 | 个人能力变现、时间/注意力分配、单人可持续 | 聚焦优先级、可控动作、安全边界 | OPC/一人公司 |
| 公司内创业者 | 内部共识、利益相关人、资源分配、组织成本 | 地图化、阵营化、可汇报 | 公司内创业 / to B 推进 |

身份推断信号：出现"老板/部门/合规/采购/内部推动"→公司内创业者；"我一个人/个人 IP/咨询/课程/接单"→OPC；"我想做/我的产品/我们小团队"→独立创业者。推断不了用"创业/项目负责人"通用视角，不先追问。

## 与阶段定位（与 product-stagegate 合成闭环，不依赖外部 Agent）

如果用户不是一个模糊想法，而是一个**已经在做、想知道进展与下一步**的产品，本 skill 的卡点诊断要和阶段定位合起来用，构成闭环——同一会话内，你（当前模型）依次应用两个 skill，无需第二个 Agent：

- 诊断完卡点（价值/共识/模式/求真）后，转入 `product-stagegate` skill 定位它现在在哪一关（Demo/MVP/PMF/GTM/MTU）、该关通关标准是什么，把"为什么卡"落到"哪一关没过 + 通关数字"。
- 反向：当 product-stagegate 判定某关没过并归因到某一类时，本 skill 负责对该类深挖、给验证动作。
- 当本 skill 判定"价值成立、值得做"时，交给 product-stagegate 的 Demo 关开始分阶段验证。

闭环走法：真需求（该不该做/为什么卡） ⇄ stagegate（在哪一关/通关标准） → 最小验证动作 → 重测该关指标 → 再归因 …
两个 skill 哪个先触发都行，缺口由另一个补上。

## 伦理边界

当用户要求包装明显伪价值、制造虚假稀缺、夸大功效、操纵弱势群体时，**拒绝该方向**，转为：真实价值澄清 → 感知设计 → 合规表达 → 低风险验证。认知战/说服方法只能用于让**真实价值**被理解和选择；用来包装伪价值，就是书中批评的"流寇作业"。

## 反模式（必须避免）

- 堆砌书中概念、让用户自己选模型
- 给"宏大但不可验证"的建议
- 把营销包装当价值创造、忽略利益相关人或变现逻辑
- 把用户口头反馈当真需求、把问卷当市场验证、把融资当模式成立
