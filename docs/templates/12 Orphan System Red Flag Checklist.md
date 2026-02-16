# Orphan System Red Flag Checklist

Signals that a system or app has no clear owner. Use for drift audits.

---

## Red flags (any 2+ = investigate)

- [ ] No clear owner for 6+ months
- [ ] Multiple people "own" it but no single point of contact
- [ ] No one has logged in or made changes in 90+ days
- [ ] Documentation is outdated or missing
- [ ] Integrations or dependencies are unclear
- [ ] Runbook for outages doesn't exist or is stale
- [ ] License or cost not tracked
- [ ] Access list hasn't been reviewed in 12+ months
- [ ] Critical for business but no backup or disaster recovery plan

---

## Quick action

1. List all systems with 2+ red flags.
2. For each: assign interim owner, document purpose, set review date.
3. For systems with 4+ flags: evaluate retire, replace, or formalize.

---

## Template for each orphan

| Field | Value |
|-------|-------|
| System name | |
| Purpose | |
| Last known owner | |
| Last activity | |
| Risk if down | |
| Next step | |
