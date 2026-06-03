# Changelog

本项目遵循 [语义化版本](https://semver.org/lang/zh-CN/)。

## [1.1.0] - 2026-06-03

### 新增

- **自包含闭环接缝**：把两个 skill 的衔接逻辑内置进各自的 `SKILL.md`，无需外部 orchestrator。
  - `product-stagegate` 增「关卡没过 → 归因」映射：定位某关失败后，按表归到价值/共识/模式/求真某类，转 `true-demand` 深挖，再落到最小验证动作。
  - `true-demand` 增「与阶段定位」节：对已在运营的产品，诊断卡点后桥接到 `product-stagegate` 定位当前关与通关标准；判定"值得做"时交回 Demo 关。
  - 闭环由同一会话内的模型依次应用两个 skill 完成。

### 验证

- 各加一道闭环用例后用双 Agent 隔离方法重评：两个 skill 均 pass_rate 1.0（stagegate 9/9、true-demand 8/8），闭环用例通过，无原有用例回退。

## [1.0.0] - 2026-06-03

首个发布版本。

### 新增

- **true-demand** skill：诊断罗盘——自动判断商业卡点在「价值/共识/模式/求真」哪一环，给出带量化成败信号的最小验证动作，不要求用户先把问题分类。提炼自梁宁《真需求》。
- **product-stagegate** skill：推进关卡——按 Demo→MVP→PMF→GTM→MTU 五关推进，用真实数据判断是否通关、给下一步或止损，并先判断项目是否适用本框架。
- Claude Code 插件市场结构（`.claude-plugin/marketplace.json` + 两个插件的 `plugin.json`），支持 `/plugin marketplace add demon-dy/product-methodology-skills` 一键接入。
- CI：push/PR 时自动校验市场与插件结构（`scripts/validate-marketplace.py` + GitHub Actions）。

### 说明

两个 skill 均经双 Agent 隔离的 eval 驱动方法迭代到收敛（Optimizer 改、独立 Evaluator 打分，优化者不给自己打分）。评分为 LLM 评估者的相对趋势参考，非绝对真值；skill 为判断脚手架，输出建议人工 review。

[1.1.0]: https://github.com/demon-dy/product-methodology-skills/releases/tag/v1.1.0
[1.0.0]: https://github.com/demon-dy/product-methodology-skills/releases/tag/v1.0.0
