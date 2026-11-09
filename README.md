# Artefact Luxury Clienteling Copilot Challenge

## 本地Qwen 50例原始结果（待评审）

[八列结果CSV](evaluations/test-set-50-v1/test-results-50.csv) · [耗时、版本与原始证据](evaluations/runs/fifty-generation-v0.3-8k/README.md)。50例150条真实本地生成，技术失败0；存在已记录的业务缺陷，未运行本轮Judge，不等于质量通过。与下方Codex编写版分开保留。

## Codex 50例交付文件（2026-11-09）

新增[最终Excel、交付描述与复核总结](deliverables/clienteling-50-codex-final/README.md)，保留原8列及50例，包含阅读页和原始数据核对页。150个输出单元中，147条为客户话术，TC041的3条明确为不发送客户的处理建议。该内容是Codex编写与复核的独立交付稿，不代表本地Qwen运行完成或独立评测通过。

## 客户模拟 Agent（2026-11-09）

本地离线测试数据工具已加入，使用 `npm run simulate:customer` 创建一个新的待审客户案例。先生成档案，再生成场景、商品事实与历史；必填姓名/生日/年龄/购物历史，其他信息允许缺失。详情见 [使用说明](docs/customer-agent.md)。它未接入网页，不替换已有人工评审案例，也不自动运行50例。

## Local prototype v0.1 (2026-11-09)

Implementation has now started with the user's approval; older Design v0.1 statements below describe the initial baseline.

Requirements: Node.js 22+ and Ollama running locally with `qwen3:8b` downloaded. Run `npm start`, then open http://127.0.0.1:3210 . No npm dependencies or cloud inference keys are required. Run `npm test` for contract checks. Both app and model stay local; do not expose their ports publicly.

Six editable fictional seed cases, direct/explicit generation modes, three candidate previews, separate Judge scoring, one AI Edit with re-evaluation, CA selection/copy, session history and JSON export are available. Rules come from rules.md. Generation/analysis/planning are currently combined in one structured model call; Judge is a separate call to the same local model, not independent ground truth. Promptfoo-style grading is implemented directly; Promptfoo itself is not integrated.

Runs are saved under ignored `work/runs/` and restored into the history list on reload. Intermediate UI snapshots remain in browser memory. Selection is retained in the browser/export. Explicit marketing-refusal conflicts may block generation with zero candidates: these cases do not satisfy the brief's three-output requirement and must not be counted as completed formal cases.

This is an initial reviewable prototype, not the final 50-case submission. Synthetic input generation is available for the selected scenario/direction and requires human review. Calibrated scoring, a side-by-side experiment table and final evaluation report remain future work. The first live run took 133 seconds for generation and exposed Judge false positives and overly generous diversity scores. Judge prompt v0.2 adds calibration examples and quote validation; quality remains unverified until human review.

Private project record for the Artefact Applied AI Engineer written challenge.

## Current status

- Local prototype exists; generation/planning remain a combined call.
- 50 local Qwen cases (150 raw candidates) completed; human review and calibrated evaluation remain pending.
- Independent planning, automatic quality gate/revision and final A/B/C comparison remain unfinished.
- The older design baseline below is historical; task.md and HANDOFF.md describe current progress.

## Confirmed design baseline

The product is a human-in-the-loop, luxury-clienteling-aware copilot for Client Advisors. Its logical flow is:

`Input Context → Scenario-aware Client Understanding → Explicit Communication Planning → Three Chinese WeChat Candidates → Validation & CA Review`

The three candidates share one communication objective and use three dynamic, context-appropriate approaches. Facts, supported interpretations, and unknowns must remain distinguishable.

## Repository map

- `docs/`: project baseline, business understanding, system design, evaluation direction, ADRs, work log, changelog, and open questions
- `docs/clienteling_messaging_reference.md`: LIUXU 六场景 CA 话术策略、模板、回复分支、事实边界与工具字段参考
- `TASKS.md`: project tracker
- `config/`: future brand-policy configuration; no policy has been implemented
- `src/`: planned module boundaries; no implementation code
- `tests/`: planned test-case and expected-check structure; no challenge data
- `evaluations/`: future baselines, experiments, reports, and defects
- `evidence/`: references to evidence kept outside Git where appropriate
- `deliverables/`: future submission assembly notes

## Confidentiality

The challenge PDF and any confidential recruitment materials must not be committed. The repository is intended to remain private.
