# Evaluation Methodology — Direction

最新进度（2026-11-09）：六案例校准包已准备，等待用户审核案例及成功条件后再运行。可先用Qwen内部Judge与人工比较，不强制另一模型；旧的“必须分模型”约束已取代。见 [校准包](../evaluations/pilot-v1/review-pack.md) 与 [闭环协议](../evaluations/pilot-v1/README.md)。

## 最新方法补充（2026-11-09）

用户确认底线、价值、单条和整组质量必须同时满足；要求丰富客户档案及长短不一的真实感合成聊天，充分测试历史证据。正式生成与Judge不得同模型；用户提供人工审议作为校准。现有同Qwen自评仅为原型，尚未切换。

评审草案：[评分锚点](../evaluations/methodology/01-quality-rubric.md)、[50例与历史数据](../evaluations/methodology/02-testset-blueprint.md)、[三方案实验协议](../evaluations/methodology/03-comparison-protocol.md)。数量配额、评分阈值、独立Judge型号仍待批准/校准；未生成完整数据或执行新实验。

## 最新确认（2026-11-09）

运行时Judge与独立evaluation分开，不增加串行Evaluation Agent。固定案例对比直接生成、独立策略生成、策略+Judge+修订；保存失败草稿、首次/最终结果和修订链，再人工校准Judge。单条与整组分别评估，记录重试、耗时、未通过展示、误报漏报；失败展示不计为通过。收藏/喜欢不是质量标签。已有一个本地实测小样，正式50例与人工校准尚未完成。详见[ADR-013](decisions/ADR-013-workflow-quality-gate.md)，下文为历史方法草案。

**Status:** Evaluation dimensions confirmed; instruments, weights, and results not yet defined.

## Quality layers

1. **Technical correctness:** three Chinese messages, complete and valid output structure
2. **Factual and brand reliability:** grounded claims, policy compliance, no unauthorized promises
3. **Clienteling quality:** personalization, contextual appropriateness, relationship sensitivity, service value, and naturalness
4. **Candidate diversity:** meaningful choice without sacrificing suitability

## Planned comparison

Compare a Direct Generation baseline with the Explicit Strategy pipeline to test whether Client Understanding and Communication Planning improve:

- personalization
- contextual appropriateness
- brand consistency
- factual reliability
- candidate diversity
- error traceability

Latency and cost should be reported as trade-offs. No experimental result exists yet.
