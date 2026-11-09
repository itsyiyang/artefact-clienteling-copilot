# Task Tracker

最新详细执行计划见 [task.md](task.md)（2026-11-09，讨论稿）。本文件保留历史高层状态；优先级、依赖、验收与待确认项以 task.md 为准。

2026-11-09 实测更新：已根据话术参考优化批量提示，本地Qwen完成50例150条原始回复，并保存CSV、原始请求/返回、耗时和版本。技术失败0；人工review、Judge校准、质量修订及对比评测尚未完成，不能标记全部候选质量通过。详情见[evaluations/runs/fifty-generation-v0.3-8k/README.md](evaluations/runs/fifty-generation-v0.3-8k/README.md)。

Status meanings: **Done** means the discussion or record is complete, not that implementation exists. **Open** means no decision has been made.

## Design and records

- [x] Define the product as a luxury-clienteling-aware copilot
- [x] Establish the relationship-first business principles
- [x] Select an explicit strategy pipeline
- [x] Select Scenario-aware Client Understanding
- [x] Select one shared objective plus three Dynamic Approaches
- [x] Separate Understanding, Planning, Generation, and Validation responsibilities
- [x] Create the private repository and documentation baseline
- [ ] Define Brand Identity & Policy in executable, evaluable terms
  - 已形成 [rules.md](rules.md) 共识基线及六场景正反例；具体政策和业务校准待完成，不标记整体完成。
- [ ] Resolve Communication Eligibility behavior for `not_recommended`
- [ ] Decide implementation topology, model, framework, and number of LLM calls

## Later implementation and evaluation

- [ ] Freeze Design v0.2 after Brand Identity & Policy
- [ ] Build a direct-generation baseline
- [ ] Build the explicit strategy prototype
- [ ] Define and curate 50 test cases / 150 candidate messages
- [ ] Run evaluation and defect analysis
- [ ] Assemble final work log, methodology, results, and next steps
