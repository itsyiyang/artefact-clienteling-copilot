# LIUXU Synthetic Reference Data

Last updated: 2026-11-09

This folder stores **synthetic test fixtures**, not real customer or brand information. Treat these versioned JSON files as shared reference inputs for scenario assembly, CA message generation, and independent judging. Do not copy product facts into separate prompts or judge rubrics.

| File | Version | Contents | Intended use |
| --- | --- | --- | --- |
| `client-database-v1.1.json` | 1.1 | 16 fictional clients; identity, relationships, historical transactions, service cases, raw CRM notes | CRM grounding and client-specific context |
| `conversation-history-v1.1.json` | 1.1 | 16 client threads, 185 historical WeChat messages | Timestamp-filtered conversation context and preference evidence |
| `product-catalog-v1.2.json` | 1.2 | 30 historical product records / transactions; 20 active product models with 38 variants; 3 documented derived comparisons | Historical purchase lookup, current product facts, price comparisons, claim evidence |

## Data boundaries and usage

- Join clients and chat threads using `client_id`. CRM transactions use historical `sku` references. Current products use `product_id` (model identity) and `variants[].variant_id` (sellable variants). **Do not equate historical paid price with current retail price.**
- Assemble context **as of each scenario's timestamp**: include only older chat messages, transactions, service updates and CRM notes; do not leak future facts. Preserve raw messages, including previous advisor errors, as conversation history—not as authoritative product or policy claims.
- Product `price` is variant-specific and effective-date bounded. `availability.status: unknown` does not imply stock. Missing/null attributes are unknown, not a license to invent details.
- The catalog's `claim_evidence`, `comparison_evidence` and `global_claim_rules` define the bounds of supported product claims. Comparisons of material, size, weight or construction must not become unsupported claims about superiority, lifespan, labor hours or manufacturing costs.
- Fine jewelry models `LX-JW-401` through `LX-JW-404` require jewelry-specific specifications and evidence; do not treat jewelry as a handbag or infer gemstone grading, precious-metal purity, or service terms not stated.
- Event invitations require a separately verified event reference; none of these three files establishes event capacity, booking status or entitlement.
- These are **test fixtures, not real-world verified merchandise claims**. `verified_in_synthetic_dataset` means internally documented in the fictional dataset only.

## Scenario integration

Scenario draft: [`evaluations/scenarios/scenario-dataset-v1.0.json`](../../evaluations/scenarios/scenario-dataset-v1.0.json), 24 scenarios (four per scenario type), targeting four CRM/history ablation conditions = 96 assembled inputs. The scenario draft is **not accepted as validated**.

Known review items:
1. `S1-001` targets C01 at 2026-11-12, but CRM birth date is 1988-11-09. Birthday trigger must be corrected or reframed.
2. `S3-003` uses C14, although the earlier scenario allocation targeted C09. Confirm intended post-purchase care coverage rather than silently changing the dataset.
3. `S6-001` names `LX-BG-401` from a ¥6,800 mention; historical conversation implies the structured model but the explicit product identity must be confirmed before treating this as a verified link.
4. `LX-BG-406` is the v1.2 `叠序翻盖手袋`; earlier draft alternative references using the same ID for a ¥6,900 crossbody are obsolete. Check all downstream references.
5. Recheck scenario recency, opt-outs, unresolved service cases, event eligibility and each `reference_ids` link against the source datasets and event reference.
6. This dataset has 24 distinct scenario instances, but only 15 unique clients; C09 currently has no scenario. It does not by itself satisfy the 50-case deliverable.

## Acceptance gate (not yet passed)

Before declaring these fixtures frozen: validate JSON/schema, IDs and referential integrity, counts, dates and as-of filtering, product evidence paths, price/variant scope, comparison arithmetic, and policy compatibility. Record failures and remediation; only then pin immutable hashes and mark an accepted ground-truth version. No validation pass is implied by uploading or committing these files.
