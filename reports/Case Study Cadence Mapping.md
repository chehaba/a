# Case Study → Cadence Mapping

**Source:** assets/ (8 case study decks)  
**Purpose:** Map case studies to outbound cadences and pains for targeted proof.

---

## 1. Parsed Case Studies

| Client | Service | Pains Addressed | File |
|--------|---------|-----------------|------|
| Alorica | AI / Automation | manual processes, HR inquiry volume, support volume/resolution, lead conversion, RFP response speed | `Alorica – Website Chat Bot & RFP Assistant.pptx` |
| CoPilot Case Studies | AI / Automation | manual processes, scattered knowledge/data, HR inquiry volume, repetitive inquiries, support volume/resolution | `CoPilot Case Studies.pptx` |
| Microsoft | Creative | HR inquiry volume, support volume/resolution | `MSFT_ZeroTrust-Onepage-CS.pptx` |
| Microsoft | AI / Automation | manual processes, scattered knowledge/data, compliance/regulated workflows, support volume/resolution, time-intensive | `Microsoft - Partner Support AI Agent .pptx` |
| Microsoft | AI / Automation | manual processes, compliance/regulated workflows, repetitive inquiries, HR inquiry volume | `Microsoft - Pharmaceutical AI Agent Proof of Concept.pptx` |
| Microsoft | Data & Analytics | support volume/resolution | `Microsoft AI Platform - JFK Files AI Search.pptx` |
| Microsoft | AI / Automation | manual processes, Excel/spreadsheet dependence, event data collection/prioritization | `Microsoft Bing - Calendar AI Agent.pptx` |
| St. Luke's | AI / Automation | manual processes, duplicate data entry, HR inquiry volume | `Saint Lukes - Medical Scribing AI Agent.pptx` |

---

## 2. Case Study → Cadence Campaign Mapping

Use the case study that matches the **pain** your prospect has. Attach or link in cadence emails where CTA or proof is relevant.

| Case Study | Best Cadence(s) | Use When Prospect Says... | Cadence Days |
|------------|-----------------|---------------------------|--------------|
| Alorica (Website Chat + RFP) | 01 Marketing Creative, 02 Attribution | conversion, lead quality, RFP response, sales enablement | 5, 10, 15, 20 |
| CoPilot HR Agent | 07 Finance Director, 05 Decision Latency | HR questions, benefits, PTO, scattered policies, manual responses | 8–14 |
| CoPilot Customer Service Agent | 03 IT Director Ownership, 04 Drift | support volume, knowledge scattered, slow resolution, repetitive tickets | 5, 10, 15 |
| CoPilot Financial Analysis Agent | 05 Decision Latency, 10 C-level KPI | time-to-answer, manual reporting, decision speed | 1, 5, 15 |
| Microsoft Partner Support Agent | 08 IT Director Backlog, 03 Ownership | manual support, multiple data sources, partner/incentive questions | 11, 15 |
| Microsoft Pharmaceutical AI PoC | 05 Decision Latency, 10 C-level | compliance, regulated workflows, R&D, time-to-insight | 1–7 |
| Microsoft JFK Files / AI Search | 05 Decision Latency, Data & Analytics | search, findability, data discovery | 8–14 |
| Microsoft Bing Calendar Agent | 05 Decision Latency, 08 Backlog | manual data collection, Excel, event prioritization, scalability | 11, 20 |
| St. Luke's Medical Scribing | 05 Decision Latency, 08 Backlog | duplicate entry, manual EMR, clinical documentation, healthcare efficiency | 8–14 |
| MSFT ZeroTrust Webinar | 01 Marketing Creative (video/delivery) | webinar, demos, delivery, testimonial | N/A (Creative asset) |

---

## 3. Pain → Service → Case Study

| Pain | Affirma Service | Case Study to Use |
|------|-----------------|-------------------|
| Manual processes / duplicate data entry | AI / Automation | St. Luke's, Microsoft Partner Support, Bing Calendar |
| Repetitive inquiries (HR, Support, Partners) | AI / Automation | CoPilot HR, Customer Service, Partner Support |
| Scattered knowledge / multiple systems | AI / Automation, Modern Workplace | CoPilot agents, Alorica RFP |
| Time-to-answer / decision latency | Data & Analytics, AI / Automation | Financial Analysis, Pharmaceutical, JFK Search |
| Lead conversion / website discovery | Marketing Services, Creative | Alorica Website Chat |
| RFP response speed / sales enablement | AI / Automation, Custom Dev | Alorica RFP Assistant |
| Event/data collection, Excel dependence | AI / Automation | Microsoft Bing Calendar |
| Healthcare/clinical documentation | AI / Automation | St. Luke's Medical Scribing |
| Compliance / regulated workflows | AI / Automation | Microsoft Pharmaceutical |

---

## 4. Cadence Day Recommendations

**When to attach a case study:**
- **Days 5, 10, 15, 20, 25, 30** — Soft CTA days. Attach 1 relevant case study with the doc/checklist.
- **Days 8–14** — Deeper value phase. Use case study as 'proof' in body: 'We did X for [Client] — similar situation.'
- **Day 1** — Only if prospect already signaled the pain. Don't lead with case study; establish pattern first.

**Rule:** Match case study pain to cadence theme. IT Director Drift → use Customer Service or Partner Support (scattered knowledge). Marketing Creative → use Alorica (conversion).

---

**Regenerate:** `python3 scripts/parse_case_studies.py`