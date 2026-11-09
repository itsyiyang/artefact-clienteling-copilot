# Repository Guide & Sync Record

Updated 2026-11-09.

## Source of truth

| Purpose | Location |
| --- | --- |
| Presentation and quickstart | [Project homepage](../README.md) |
| Current project outputs | [Final Outputs](../deliverables/final-outputs/README.md) |
| Submission completion map | [Delivery guide](../deliverables/README.md) |
| Current task status | [Roadmap](../TASKS.md) |
| Product architecture | [System design](04_system_design.md) |
| Quality findings | [Results report](../evaluations/reports/project-results.md) |
| Historical decisions | [Work log](work_log.md), [ADRs](decisions/), Git history |

## Local synchronization

Three local project copies and the final-output authoring workspace were compared with the remote repository.

- Application code, prompts, customer simulation, input assembly, batch runner, and existing tests were already tracked.
- Added the selected early Studio screenshot to `docs/assets/client-studio.png`.
- Added the saved early generation / Judge / revision sample to `samples/local-product-review.json`, completing the existing defect-log reference.
- Added `deliverables/final-outputs/source-data.json`, the 51-row array (header plus 50 cases) behind the final workbook's original-data sheet.
- Retained the final workbook byte-for-byte and added a source-data equality check to its verification script.
- Older intermediate workbook / CSV exports and duplicate local document copies were not promoted over the final deliverable.
- Latest Qwen results are deferred at the user's request and will use a separate `qwen-timeframexxx` run name.

Local scratch runs and unselected drafts remain outside this curated archive. See [local Git workflow](local-github-workflow.md) for synchronization discipline.

## Naming and provenance

Final Outputs are presented as LIUXU project results. Drafting and content checking used AI assistance; independent user labels and model-generated review remain distinguished in the evidence. Tool-specific branding has been removed from the current working tree. Historical Git commits remain intact.

## Presentation references

The homepage's overview → workflow → quickstart → documentation structure draws on the clear entry points used in [NVIDIA's Retail Shopping Assistant](https://github.com/NVIDIA-AI-Blueprints/retail-shopping-assistant) and [Promptfoo](https://github.com/promptfoo/promptfoo). They are presentation references; LIUXU does not thereby claim their integrations or capabilities.
