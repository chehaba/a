# Company Type × Ask × Service — Target Matrix

**Data:** data/Inbound/Inbound.xlsx (550 leads)  
**Regenerate:** `python3 scripts/company_target_matrix.py`  
**Note:** Add **Email** column to your next CRM export to enable domain-based company inference (e.g., .gov → Government, .edu → Education). Currently uses Industry extracted from description.

---

## Purpose

1. **Infer company type** from email domain (when available) or from description language.
2. **Connect asks to Affirma services** — what they want → which service to message.
3. **Target the right companies** with the right service-specific copy.
4. **Replace "this investment"** with the actual service phrase in messaging.

---

## Company Type × Top Asks → Service

| Company Type | Top Asks | Services to Message | Say This (not "this investment") |
|--------------|----------|---------------------|----------------------------------|
| **Government** | SharePoint, Power BI, Google→M365 | Modern Workplace, Data & Analytics | "this SharePoint migration" / "this Power BI deployment" |
| **Healthcare** | SharePoint, Compliance, Dashboard | Modern Workplace, Data & Analytics | "this SharePoint migration" / "this Power BI deployment" |
| **Non-Profit** | Dynamics, SharePoint, Migration | CRM, Modern Workplace | "this Dynamics implementation" / "this SharePoint migration" |
| **MSP** | BPO/Helpdesk, Power BI, Support | Infrastructure/BPO, Data & Analytics | "this helpdesk outsourcing" |
| **Construction** | SharePoint, Power Automate | Modern Workplace | "this SharePoint migration" |
| **Education** | Dynamics, Power BI | CRM, Data & Analytics | "this Dynamics implementation" |
| **Financial Services** | SharePoint, Dynamics | Modern Workplace, CRM | "this SharePoint migration" |
| **Manufacturing** | Dynamics, Guidance | CRM, Modern Workplace | "this Dynamics implementation" |
| **Legal** | SharePoint, Ongoing Support | Modern Workplace, Infrastructure | "this SharePoint migration" |
| **Real Estate** | BPO, Dashboard, Dynamics | Infrastructure/BPO, Data & Analytics | "this helpdesk outsourcing" |

---

## Ask → Service → Phrase (Use in Copy)

| What They Ask | Affirma Service | Replace "this investment" With |
|---------------|-----------------|--------------------------------|
| SharePoint (any) | Modern Workplace | "this SharePoint migration" or "this intranet build" |
| Power BI, Dashboards | Data & Analytics | "this Power BI deployment" |
| Dynamics, CRM | CRM | "this Dynamics implementation" |
| HubSpot, SEO | Marketing Services | "this HubSpot setup" |
| AI, Copilot | AI / Automation | "this AI rollout" |
| BPO, Helpdesk | Infrastructure / BPO | "this helpdesk outsourcing" |
| Google→M365, Tenant, Exchange | Infrastructure | "this migration" |

---

## How to Use

1. **Before writing:** Look up company type (or infer from LinkedIn/website). Match to the target matrix.
2. **Choose service:** Based on their ask + company type. Government + SharePoint → Modern Workplace.
3. **Use the phrase:** "This [SharePoint migration] will increase revenue by..." — not "This investment will..."
4. **Add Email to export:** When you add the Email column to Inbound.xlsx, re-run the script. Domain-based inference (e.g., cityof*.gov) will improve accuracy.
