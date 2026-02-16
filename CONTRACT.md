# Agent Contract — Messaging Motion Construction

**Purpose:** Define inputs, required intermediate artifacts, outputs, and schemas for the messaging/targeting agent.

---

## Inputs

| Input | Type | Required | Description |
|-------|------|----------|-------------|
| **Trigger** | string | Yes | "Find companies to target for cloud migration [region/industry]" or "Create messaging motion for [ICP/industry/service]" |
| **Region / Industry** | string | No | Filter scope (e.g., "Austin", "Healthcare") |
| **Repository assets** | paths | Implicit | Agent reads from repo; see Asset table in AGENTS.md |

---

## Required Intermediate Artifacts

### Artifact 1: Extracted Entities

Produced after Step 2 (Extract).

| Field | Type | Source | Example |
|-------|------|--------|---------|
| companies | string[] | Market tables, vendor lists | ["Company A", "Company B"] |
| personas | string[] | Messaging Framework, Oops | ["IT Director", "VP IT", "CIO"] |
| triggers | string[] | Targeting Strategy | ["AI initiatives", "end-of-life", "compliance"] |
| pain_language | string[] | Inbound, market tables | ["data silos", "AI-ready architecture", "TCO"] |
| service_mapping | object | Company Type Target Matrix | { "SharePoint": "Modern Workplace", "Power BI": "Data & Analytics" } |

### Artifact 2: Filtered Target Candidates

Produced after Step 3 (Cross-Reference & Filter).

| Field | Type | Description |
|-------|------|-------------|
| vendor_list_match | string[] | Companies from vendor lists that appear in CRM |
| microsoft_workload | boolean | Filter: Microsoft collaboration stack only |
| exclude | string[] | Mainframe, SAP RISE-only, Oracle-only |
| priority_signals | string[] | Dynamics, Copilot, Azure adopters |

### Artifact 3: Ask → Service Mapping

Produced when building messaging motion.

| Field | Type | Description |
|-------|------|-------------|
| ask | string | What they want (SharePoint, Power BI, Dynamics, etc.) |
| service | string | Affirma service |
| phrase | string | Copy phrase (e.g., "this SharePoint migration") |

---

## Outputs

### Output 1: Target List (Cloud Migration)

| Column | Type | Required |
|--------|------|----------|
| Company | string | Yes |
| Industry | string | Yes |
| Signal | string | Yes (trigger or fit reason) |
| Priority tier | string | Yes (Tier 1, Tier 2, etc.) |
| Source | string | Yes (cite: market table, CRM, report) |

### Output 2: Role-Based Messaging

| Field | Type | Required |
|-------|------|----------|
| role | string | Champion, Influencer, DM, Stakeholder |
| service_phrase | string | Service-specific (no generic "this investment") |
| financial_lever | string | revenue, cost, protect, or capacity |
| hook | string | Campaign-aligned opener |
| cta | string | Low-pressure call to action |

### Output 3: Citations & Regen

| Field | Type | Required |
|-------|------|----------|
| sources | string[] | Paths/files used |
| regen_commands | string[] | Scripts to reproduce (e.g., `python3 scripts/company_target_matrix.py`) |

---

## Schemas

### Oops.csv (Input Data)

```
Status, Source_Campaign, Primary_Service, Contact, Account, Industry, Job_Title,
Account_Engaged_Count, Is_Multi_Opp, Title_Industry_Engaged, Title_Industry_Won,
Title_Industry_WinRate_Pct, Pattern_Count, Source_Engaged_Count
```

### company_type_service.json (Pattern Output)

```json
{
  "company_type": "string",
  "service": "string",
  "n": 0,
  "won": 0,
  "win_rate": 0.0
}
```

### Target List Table (Output)

```
| Company | Industry | Signal | Priority | Source |
|---------|----------|--------|----------|--------|
```

### Messaging Record (Output)

```
Role: string
Service phrase: string
Financial lever: string
Hook: string
CTA: string
```

---

## Fallback Rules (Missing Data)

| Missing | Fallback | Label |
|---------|----------|-------|
| No Email | Industry from description | "Add Email for domain inference" |
| No Title | Infer from description | "Inferred" |
| No Win Rates | Inbound volume + Company Type × Ask | "Directional" |
| Small N | Report counts | "Exploratory" |
| No Ask | Use description fallback | "Inferred" |

---

## Validation Checklist

- [ ] All outputs use bullet points, tables, short sentences
- [ ] Service phrase specified (no generic "this investment")
- [ ] Sources cited for each claim
- [ ] Regen commands documented
- [ ] Fallback rules applied and labeled when used
