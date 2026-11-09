# Artefact Luxury Clienteling Copilot Challenge

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

- Phase: requirements and conceptual design
- Design baseline: v0.1
- Implementation: not started
- Next design topic: Brand Identity & Policy

This repository currently contains documentation, decision records, trackers, and an empty development skeleton only. It does **not** contain product implementation code.

## Confirmed design baseline

The product is a human-in-the-loop, luxury-clienteling-aware copilot for Client Advisors. Its logical flow is:

`Input Context → Scenario-aware Client Understanding → Explicit Communication Planning → Three Chinese WeChat Candidates → Validation & CA Review`

The three candidates share one communication objective and use three dynamic, context-appropriate approaches. Facts, supported interpretations, and unknowns must remain distinguishable.

## Repository map

- `docs/`: project baseline, business understanding, system design, evaluation direction, ADRs, work log, changelog, and open questions
- `TASKS.md`: project tracker
- `config/`: future brand-policy configuration; no policy has been implemented
- `src/`: planned module boundaries; no implementation code
- `tests/`: planned test-case and expected-check structure; no challenge data
- `evaluations/`: future baselines, experiments, reports, and defects
- `evidence/`: references to evidence kept outside Git where appropriate
- `deliverables/`: future submission assembly notes

## Confidentiality

The challenge PDF and any confidential recruitment materials must not be committed. The repository is intended to remain private.
