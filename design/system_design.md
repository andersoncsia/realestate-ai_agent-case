# Internal Agency Copilot design — teaching blueprint
UI: assigned cases, document checklist, inspection review, listing package, market data gaps, approval queue. Seller is not a login role.
API: authenticate user; check assigned case; select workflow; load current versions; return structured drafts and citations.
Runtime: select Skill → retrieve allowed docs → model reasons / requests typed tools → backend validates scope and parameters → tool executes read only → result returns to model → validate schema/source IDs → persist pending_review. Limit steps/time/cost; if no evidence, mark blocked or pending_review. Tool failure is never treated as successful data.
Storage: Case, Document, Fact(verified/status/source), Finding, Draft(version/source_revision/policy_version), Approval(version/source_revision), Trace (redacted). RBAC and tenant/case isolation at every tool call. Never include unnecessary PII in trace.
Approval: draft → pending_review → approved/rejected. Revision or source changes invalidate old approval. Approved means internal review only; no publishing API in MVP.
Orchestration: deterministic checklist plus single model-driven agent with packet review and listing skills; optional isolated market-report worker only after tests justify it. Structured handoff source_ref, verified_fact, unknown, version, review_status.
Tests: schema, rule checks, role isolation, adversarial docs, regression evals, human domain review; observe latency, tool failures, cost and review changes. Deploy only after gate. No actual integrations in demo.
