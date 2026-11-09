# Delivery Guide

**Final Outputs:** [50-case Excel](final-outputs/LIUXU_test_results_50_FINAL.xlsx) · [Reading guide & revisions](final-outputs/README.md) · [Results](../evaluations/reports/project-results.md)

## Five-minute reading path

1. Open the final workbook's `案例与自然话术` sheet.
2. Review TC041's marked contact-boundary exception.
3. Read [results](../evaluations/reports/project-results.md) and [workflow](../docs/04_system_design.md).
4. Verify the artifacts and inspect the completion map below.

## Task-to-evidence map

| Deliverable | Evidence | Completion boundary |
| --- | --- | --- |
| A · Work log | [Work log](../docs/work_log.md), [ADRs](../docs/decisions/), Git history | Process screenshot selection remains open |
| B · Methodology | [Methodology](../docs/05_evaluation_methodology.md), rubric and comparison protocol | Controlled comparison remains planned |
| C · 50 cases | [Final workbook](final-outputs/LIUXU_test_results_50_FINAL.xlsx), [source data](final-outputs/source-data.json) | 147 client candidates + 3 no-send notes; TC041 exception disclosed |
| D · Evaluation | [Results report](../evaluations/reports/project-results.md), user review and Judge comparison | Pilot evidence available; full-set independent scoring and evaluation screenshots remain open |
| E · Defects / next steps | [Defect log](../evaluations/defects.md), [revision summary](final-outputs/README.md#本次复核与修订总结), [roadmap](../TASKS.md) | Original failures preserved; broader regression remains open |
| Demo / architecture | Runnable Studio and [workflow images](../docs/04_system_design.md) | Multi-agent is the next design direction |

## Verify

```bash
npm test
python3 deliverables/final-outputs/verify_delivery.py
```

The workbook is the current project deliverable. Historical Qwen runs remain in `evaluations/runs/`; the latest batch will be supplemented separately as `qwen-timeframexxx`.

The private repository is not a recipient-accessible submission channel on its own. Deliver selected files through the agreed channel after review. Confidential source PDFs and recruitment correspondence remain excluded.
