# Evaluation Methodology

## Current evidence

[Final Outputs](../deliverables/final-outputs/README.md) contain 50 cases prepared through AI-assisted drafting and revision. Full independent business scoring remains pending.

Actual local evidence comprises six Qwen generation cases, prior user review, separate Judge calls, and historical batch checkpoints. See [results](../evaluations/reports/project-results.md).

## Four quality layers

| Layer | Question |
| --- | --- |
| Technical correctness | Are outputs present, structured, and complete? |
| Factual and brand reliability | Are claims grounded and promises authorized? |
| Clienteling quality | Is the message relevant, timely, natural, and respectful of boundaries? |
| Candidate diversity | Do alternatives offer useful choices without sacrificing suitability? |

Hard failures cannot be offset by aggregate scores. TC041 is explicitly no-send rather than counted as three sendable messages.

## Review protocol

1. Freeze inputs, prompt, model settings, and rubric; preserve source / branch IDs.
2. Retain original outputs, errors, timing, and versions.
3. Record user judgments before showing Judge results.
4. Run Judge in a separate call without user labels.
5. Validate quotes and record false positives, missed issues, and disagreements.
6. Revise and recheck while retaining the before / after chain.

A separate call to the same Qwen model is permitted for prototype calibration; it is not an independent gold standard. A different grader may be considered after examining disagreements.

The six-case pilot followed this user-first comparison. [Findings](../evaluations/runs/pilot-judge-v1/findings.md) record missed personalization, generic reactivation, salutation issues, and invalid evidence.

## Data and comparison limits

The 50 cases comprise 21 source cases and 29 synthetic branches, with repeated customers and related history. Reactivation is concentrated on one customer. Rows are not independent observations.

Controlled comparison of direct generation, independent planning, and planning + Judge + revision remains planned. Studio strategy mode combines understanding, planning, and generation, so it cannot establish the effect of an independent planner.

Instruments: [rubric](../evaluations/methodology/01-quality-rubric.md), [data blueprint](../evaluations/methodology/02-testset-blueprint.md), [comparison protocol](../evaluations/methodology/03-comparison-protocol.md).

## Reporting

Separate structure, semantic quality, refusals, failures, first / final outputs, retries, and latency. Keep qualitative labels qualitative; do not infer pass rates from “还可以,” one reviewer, or model self-scores. Sales impact has not been measured.
