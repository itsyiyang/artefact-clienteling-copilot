# Evaluation & Evidence

[Project results](reports/project-results.md) · [Final Outputs](../deliverables/final-outputs/README.md) · [Defects](defects.md)

## Read in this order

1. [Final workbook](../deliverables/final-outputs/README.md), including TC041.
2. [Six-case user review](runs/pilot-six-review/human-review-v1.md) and [Judge comparison](runs/pilot-judge-v1/findings.md).
3. [Methodology](../docs/05_evaluation_methodology.md), [batch guide](../docs/fifty-local-run.md), and per-run manifests.

| Directory | Role |
| --- | --- |
| `pilot-v1/` | Draft calibration inputs, reference approaches, and review keys |
| `test-set-50-v1/` | Frozen 50-case inputs and original result template |
| `runs/pilot-six-review/` | Six actual Qwen generation cases, 18 candidates, user feedback |
| `runs/pilot-judge-v1/` | Separate Judge calls and user-review comparison |
| `runs/fifty-generation-*/` | Historical batch checkpoints with requests, responses, and timing |
| `methodology/` | Rubric, data blueprint, comparison protocol |
| `customer-agent-trials/` | Synthetic data trials, including rejected and pending samples |
| `reports/` | Results interpretation and delivery gaps |

Final Outputs live in `deliverables/final-outputs/`. The latest Qwen batch will be added separately under `qwen-timeframexxx`. Read existing checkpoints through their manifests.

The 50 cases include 21 source cases plus 29 explicit synthetic branches, rather than 50 independent customers. Structure checks, user review, and model judgments answer different questions; none is automatically a quality pass rate.
