# LIUXU — Project Results & Findings

2026-11-09 · Current final messaging deliverable and recorded prototype evidence.

## Final Outputs

The [final workbook](../../deliverables/final-outputs/LIUXU_test_results_50_FINAL.xlsx) contains 50 cases, two worksheets, and the original eight columns. The readable sheet presents client facts, history, and product information in Chinese sections; the original-data sheet preserves source JSON.

| Scenario | Cases |
| --- | ---: |
| Birthday / festive greetings | 8 |
| Product recommendation | 10 |
| Post-purchase care | 8 |
| Reactivation | 8 |
| Event invitation | 8 |
| Price objection | 8 |
| **Total** | **50** |

**150 output cells = 147 client-message candidates + 3 no-send handling notes.** TC041 limits contact to craft information; event-list membership alone does not authorize a new invitation. TC042, where the client asks about the event, remains a normal reply case.

The collection was prepared through AI-assisted drafting and revision using scenario inputs and the messaging reference. It is the project's current final writing deliverable, separate from local Qwen raw generation. Full independent business scoring remains pending.

Final review changed 10 output cells. The [revision table](../../deliverables/final-outputs/README.md#本次复核与修订总结) records each case and reason.

## Actual prototype evidence

The Studio implements editable inputs, direct / strategy modes, three-candidate previews, separate Judge calls, one AI edit with re-evaluation, selection/copy, and JSON export. Understanding, planning, and generation share one call. Judge uses the same local Qwen model with a separate prompt.

The [generation pilot](../runs/pilot-six-review/review.md) produced 18 messages across six scenarios. The first product-recommendation request failed and was rerun successfully; the failure remains recorded.

| Observed issue | Evidence | Consequence |
| --- | --- | --- |
| Irrelevant birthday personalization | User rejected S1 candidates 2 and 3 | Historical truth alone does not establish relevance or timeliness |
| Generic reactivation | User found S4 too general | Recontact needs concrete new value |
| Salutation | User required correction in S6 | Use a confirmed surname and title |
| Judge misses and false positives | S1, S4, S6 and other disagreements | Model grading needs human calibration |
| Invalid Judge evidence | Three S5 quotes could not be located | Validate quotes before accepting findings |

Sources: [user review](../runs/pilot-six-review/human-review-v1.md), [Judge findings](../runs/pilot-judge-v1/findings.md). “还可以” is qualitative feedback, not a numeric score or certification of every fact.

Six Judge calls took 225.7–349.8 seconds each. The early Studio generation sample took 133.363 seconds. These are observations from different runs, not a controlled speed benchmark.

## Validation

```bash
npm test
python3 deliverables/final-outputs/verify_delivery.py
```

Workbook checks cover both sheets, 50 IDs, original columns, JSON parsing, retained dialogue, 150 distinct outputs, cross-sheet agreement, TC041 labels, and the archived hash. Source-data JSON is compared with the original-data worksheet.

App tests cover generation / Judge contracts, quote handling, customer profiles, and input assembly. They do not measure message usefulness.

Historical runs preserve model metadata, snapshots, requests, responses, and timing. See the [batch guide](../../docs/fifty-local-run.md). Latest Qwen results will be supplemented separately as `qwen-timeframexxx`.

## Interpretation and limits

The completed result is a reviewable end-to-end artifact: explicit business rules, six scenarios, a runnable workspace, final case collection, and traceable revision decisions.

Current evidence does not establish a quality pass rate, sales improvement, or multi-agent superiority. Synthetic branches share customers and history. Pilot review comes from one user; the final workbook is not an independent gold standard.

TC041 is an explicit exception to “three sendable messages per case.” Its handling preserves the client's contact boundary and must remain disclosed in the final delivery.

## Next steps

Independent final-set review; process and evaluation screenshots; separate latest-Qwen archive; Judge calibration; controlled baseline comparison; then multi-agent implementation and evaluation. See the [delivery map](../../deliverables/README.md).
