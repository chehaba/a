# Inbound Analysis Report — Why Qualified Leads Come In

**Data:** data/Inbound/Inbound.xlsx (550 qualified leads)  
**Source:** commit 7397323

---

## Summary

Inbound qualified leads come to Affirma primarily for **SharePoint**, **Power Platform**, **Migration**, and **Support**. They use language like "looking for," "migrate," "build," and "partner."

---

## Why They Come In (Category Distribution)

| Category | Count | % |
|----------|-------|---|
| Other* | 231 | 42 |
| Power Platform (Power BI, Dynamics, Power Automate) | 95 | 17 |
| SharePoint / Intranet | 59 | 11 |
| Support / Maintenance | 56 | 10 |
| Migration | 53 | 10 |
| Marketing / SEO | 21 | 4 |
| Analytics / Dashboard | 13 | 2 |
| Training | 12 | 2 |
| AI / Copilot | 6 | 1 |
| Compliance / Data (Purview, CMMC, HIPAA) | 4 | 1 |

\*Other includes 74 SharePoint-related (general), 16 Consulting, 8 RFP, 4 Integration.

**Combined SharePoint-related:** 59 + 74 = **133** (24% of total).

---

## Theme Frequency (Keyword Scan)

| Theme | Count |
|-------|-------|
| SharePoint | 178 |
| Help / Support | 189 (help + support) |
| Data | 65 |
| Intranet | 54 |
| Power BI | 42 |
| Migration / Migrate | 71 (combined) |
| Microsoft 365 | 48 |
| Dynamics / CRM | 45 |
| Training | 27 |
| AI | 28 |
| Dashboard | 15 |
| Workflow | 10 |
| Compliance | 9 |

---

## Language They Use (Self-Reported)

| Phrase | Count |
|--------|-------|
| "looking for" | 144 |
| "migrate" | 89 |
| "build" | 59 |
| "partner" | 51 |
| "consultant" | 38 |
| "assistance" | 25 |
| "need help" | 23 |
| "vendor" | 17 |
| "guidance" | 15 |

**Messaging insight:** They frame the ask as "looking for a partner" or "need help with" — not "we want to buy." Lead with partnership, assistance, guidance.

---

## Source Campaign

| Source | Count | % |
|--------|-------|---|
| Marketing – PPC | 434 | 79 |
| Marketing - SEO | 83 | 15 |
| Marketing - Lazlo - Websights | 6 | 1 |
| Marketing - Email | 4 | 1 |
| Marketing - Referral | 4 | 1 |
| Marketing - Clutch | 4 | 1 |
| Other | 15 | 3 |

**PPC and SEO drive 94% of inbound.**

---

## Top Inbound Reasons (Thematic)

1. **SharePoint** — Intranet, migration, build, restructure, page setup
2. **Migration** — Exchange, SharePoint, M365 tenant, Google Workspace, on-prem
3. **Power Platform** — Power BI deployment, Dynamics configuration, Power Automate flows
4. **Support / Maintenance** — Ongoing support, end-of-life upgrades
5. **Guidance** — "Information overload," "need guidance," "learn the art of the possible"
6. **Compliance** — Purview, CMMC, HIPAA, data governance
7. **Training** — New hire, adoption
8. **Analytics / Dashboard** — Report replacement, operational dashboards
9. **Marketing / SEO** — HubSpot, SEO, marketing agency
10. **AI / Copilot** — AI solution evaluation, Copilot deployment

---

## Pain Points (Triggers)

- **Migration need** — 72 references (mandate, upgrade, move off legacy)
- **Need guidance** — 13 ("information overload," "so many options")
- **Compliance requirement** — 10 (CMMC, HIPAA, Purview)
- **Scaling need** — 9 (scalable deployment)
- **End of life** — 2 (SharePoint 2013, legacy systems)

---

## Messaging Insights for Frameworks

### 1. Mirror Their Language
- Use "looking for a partner" / "need help with" / "assistance" / "guidance"
- Avoid "we sell" or "our product" — lead with partnership

### 2. Lead With Top Categories
- **SharePoint:** Intranet, migration, build, restructure
- **Power Platform:** Power BI, Dynamics, Power Automate
- **Migration:** Exchange, tenant, Google, on-prem
- **Support:** Ongoing, maintenance, EOL upgrade

### 3. Pain-Aware Hooks
- "Information overload with the M365 stack"
- "Migration mandate" / "need to move off [X]"
- "Looking for a partner to guide us"
- "End-of-life system" / "legacy upgrade"

### 4. Source Alignment
- PPC/SEO traffic → they found you via search (problem-aware)
- Messaging should match what they searched for: SharePoint help, migration, Power BI, etc.

### 5. Decision Maker
- 7 NaN, rest "No" for Decision Maker column — may indicate form field; assume mixed buyer levels

---

*Run analysis: `python3 scripts/analyze_inbound.py` (if script created)*
