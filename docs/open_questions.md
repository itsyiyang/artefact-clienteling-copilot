# Open Questions

最新收敛（2026-11-09）：不强制生成/Judge分模型，先以六例人工校准衡量Qwen Judge，再决定是否替换。待用户审核六例输入与评分，尤其生日/售后/邀请的策略差异；未运行、未评分。

## Methodology最新边界（2026-11-09）

生成保持Qwen3:8b，正式Judge须不同模型；用户人工审议先作校准依据。待选独立Judge型号、待验证其中文评审能力；未授权新下载。三份评审草案位于evaluations/methodology/；50例配额、12/38分区、额外6压力例和0–2评分门槛均待校准，不视为已经执行。

## 最新收敛与待定（2026-11-09）

已确认独立策略规划、单条与整组质量门、有限自动修正、耗尽后允许明确标记的失败展示、独立evaluation及CA收藏/反馈/重生成方向，见[ADR-013](decisions/ADR-013-workflow-quality-gate.md)。本地Qwen3:8b与Node服务已运行，故下方工程问题7–8不再全部开放。

仍需讨论：通过阈值；失败草稿是否允许选择/复制；受限场景差异尺度；人工评分与50例分布；拒绝营销下正式三输出契约。两轮内部修正与一次CA修改作为首版可调整参数。

Items here are not decisions.

## Brand Identity & Policy

1. What makes the fictional luxury brand recognizably distinct beyond generic “elegant, warm, professional” language?
2. Which rules are hard constraints, soft preferences, or scenario-specific guidance?
3. How will brand compliance be evaluated consistently?

## Communication Eligibility

4. When outreach is `not_recommended` but the challenge requires three messages, should the system produce clearly flagged drafts, transform the objective into a non-promotional response, or follow another policy?
5. What evidence is sufficient to move from `caution` to `not_recommended`?

## Engineering

6. How many LLM calls should implement the logical pipeline?
7. Should intermediate outputs be generated jointly or separately?
8. Which model/provider, language, framework, interface, and deployment approach should be used?
9. Which deterministic checks belong in Validation?

## Evaluation

10. How should the 50 cases cover scenarios, relationship states, ambiguity, and adversarial boundary conditions?
11. What rubric, weights, raters, and acceptance thresholds should be used?
12. How will latency/cost trade-offs be compared with quality gains?
