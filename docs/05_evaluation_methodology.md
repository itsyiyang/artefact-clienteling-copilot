# Evaluation Methodology — Direction

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
