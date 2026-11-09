# Defect Log

## Prototype v0.1 / local Qwen3:8b, 2026-11-09

- D001: First product recommendation run took 133.363 seconds (cold/warm conditions not controlled). Do not extrapolate throughput. Shortened runtime policy input and enabled 30-minute model retention for follow-up trials.
- D002: Candidate 1 and 3 were near paraphrases; Judge assigned diversity 4/5. Human assistant inspection disagrees; user calibration pending.
- D003: Judge treated normal color/size clarification as potentially inappropriate and cited product-input text rather than candidate text. Prompt v0.2 explicitly counters these errors; quote validation now marks invalid citations as requiring human review instead of passing. This structural check does not prove semantic correctness.
- D004: No formal 50-case run, calibrated grader, or independent grading model exists yet. Initial grader is the same Qwen model with a separate prompt.
- D005: Refusal conflicts currently produce a visible blocked state with zero candidates, not a compliant three-output formal test result. Final contract remains open.

Re-test evidence: `samples/local-product-review.json` contains actual local generation, v0.2 Judge, one edit and regrading. Diversity decreased to 2/5 but edit only expanded candidate 2; the repeated approaches remain. D002 is not resolved; improved grading does not establish improved generation. Candidate attribution and advice still need human calibration.

All defects are open pending regression and user review unless explicitly marked resolved. No conversion or sales claims are inferred.

Future entries should include case ID, observed failure, expected behavior, suspected stage, root-cause hypothesis, fix/version, and re-test result.
