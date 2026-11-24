---
name: agency-packet-review
description: Review internal pre-listing case documents, classify gaps, cite inspection observations and prepare an internal review draft. Use when an authorized listing agent or coordinator requests case review.
---
# Agency packet review
Inputs: seller_profile.json, docs_index.csv, approved_checklist.md, inspection_report.md, property_facts.md, agency_policy.md.
1. Verify case ID and user role via trusted application (in chat demo these are simulated, not authenticated).
2. Compare each document to checklist v1; classify received, missing, unknown applicability, needs_confirmation. Received ≠ fact verified.
3. Extract inspection observations with INS identifiers; separate professional follow-up and unknowns. Do not invent obligations, estimates or diagnosis.
4. Produce internal actions with owner, status and source; keep unverified facts outside marketing copy.
5. If marketing requested, use verified PF-01 only; if market inputs unapproved, list gaps. Do not price.
6. Return structured JSON; status pending_review; approval_required true. A broker's real approval must be enforced by backend for a specific immutable version, never inferred from chat.
Quality: verify each source ID against file, check unknowns and separate observation vs interpretation; run evals/test_cases.json. Stop on missing case permission or critical evidence conflict. No publishing or sending tools.
