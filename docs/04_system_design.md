# System Design Baseline

**Status:** Logical architecture confirmed; engineering topology open.

## Logical flow

1. **Input Context** — client, scenario, conversation, product/event facts
2. **Scenario-aware Client Understanding** — relevant facts, intent, relationship, preferences, boundaries, uncertainty
3. **Explicit Communication Planning** — eligibility, shared objective, relationship priority, selected facts, guardrails, engagement goal, three dynamic approaches
4. **Message Generation** — one Chinese WeChat candidate per approach
5. **Validation & CA Review** — grounding, brand, context, naturalness, and candidate diversity

## Client Understanding boundary

Understanding describes the client and situation. It does not choose the communication strategy and must not infer wealth, psychology, or purchase readiness without evidence.

Important judgments remain separated as:

- **Observed facts:** directly supported by the input
- **Supported interpretations:** reasoned but still interpretive
- **Unknowns:** insufficient or conflicting evidence

## Communication Planning baseline

All candidates share one communication objective and consistent facts/guardrails. Their dynamic approaches differ in a meaningful communication emphasis, not merely tone or wording.

Each approach must be relevant, distinct, brand-consistent, and appropriate.

## Communication Eligibility

The proposed states are `appropriate`, `caution`, and `not_recommended`. Eligibility belongs in Planning, but the exact behavior for `not_recommended` remains open.

## Explicit non-decisions

Design v0.1 does not determine the number of LLM calls, whether agents are used, the model/provider, the framework, the programming language, or the deployment architecture.
