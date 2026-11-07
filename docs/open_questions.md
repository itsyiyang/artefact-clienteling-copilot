# Open Questions

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
