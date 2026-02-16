#!/usr/bin/env python3
"""
Generate 31-day value-first cadence templates for each of the 10 campaigns.
Each day offers free value. Same format. Persona-specific.
Folder names: Title Case with spaces (no hyphens or underscores).
Every 5th day (5, 10, 15, 20, 25, 30) includes a soft CTA.
"""

from pathlib import Path

BASE = Path(__file__).resolve().parent.parent / "outbound" / "value-first-campaigns"
DOCS_BASE = Path(__file__).resolve().parent.parent / "docs" / "templates"

# Campaign id (for logic) -> folder name (clean, Title Case)
CAMPAIGN_FOLDERS = {
    "01-marketing-creative-conversion": "01 Marketing Creative Conversion",
    "02-marketing-creative-attribution": "02 Marketing Creative Attribution",
    "03-it-director-ownership": "03 IT Director Ownership",
    "04-it-director-drift": "04 IT Director Drift",
    "05-director-decision-latency": "05 Director Decision Latency",
    "06-marketing-vp-spend": "06 Marketing VP Spend",
    "07-finance-director-ownership": "07 Finance Director Ownership",
    "08-it-director-backlog": "08 IT Director Backlog",
    "09-marketing-manager-fixes": "09 Marketing Manager Fixes",
    "10-c-level-kpi-latency": "10 C Level KPI Latency",
}

CAMPAIGNS = [
    {
        "id": "01-marketing-creative-conversion",
        "name": "Marketing Director × Creative — Conversion",
        "persona": "Marketing Director, VP, or Manager",
        "focus": "Conversion leaks, landing pages, creative performance",
        "days": {},  # filled below
    },
    {
        "id": "02-marketing-creative-attribution",
        "name": "Marketing Director × Creative — Attribution",
        "persona": "Marketing Director, VP",
        "focus": "Attribution, spend allocation, channel performance",
        "days": {},
    },
    {
        "id": "03-it-director-ownership",
        "name": "IT Director — Ownership & Checklist",
        "persona": "IT Director, Director of IT, CIO",
        "focus": "Systems ownership, drift, governance",
        "days": {},
    },
    {
        "id": "04-it-director-drift",
        "name": "IT Director — Drift Audit",
        "persona": "IT Director, Infrastructure lead",
        "focus": "Systems drift, orphan systems, documentation",
        "days": {},
    },
    {
        "id": "05-director-decision-latency",
        "name": "Director — Decision Latency",
        "persona": "Director, VP (Ops, Finance, IT)",
        "focus": "Time-to-answer, KPI reporting, decision speed",
        "days": {},
    },
    {
        "id": "06-marketing-vp-spend",
        "name": "Marketing VP — Spend Reallocation",
        "persona": "Marketing VP, CMO",
        "focus": "Spend efficiency, channel allocation, reallocation",
        "days": {},
    },
    {
        "id": "07-finance-director-ownership",
        "name": "Finance Director — System Ownership",
        "persona": "Finance Director, VP Finance, Controller",
        "focus": "Critical systems, ownership maps, review cadence",
        "days": {},
    },
    {
        "id": "08-it-director-backlog",
        "name": "IT Director — Backlog Prioritization",
        "persona": "IT Director, Dev lead",
        "focus": "Backlog, prioritization, partner vs in-house",
        "days": {},
    },
    {
        "id": "09-marketing-manager-fixes",
        "name": "Marketing Manager × Creative — 3 Fixes",
        "persona": "Marketing Manager",
        "focus": "Quick fixes, ads, landing pages, execution",
        "days": {},
    },
    {
        "id": "10-c-level-kpi-latency",
        "name": "C-level / VP — KPI Latency",
        "persona": "C-level, VP, Senior Director",
        "focus": "Decision latency, executive KPIs, time-to-answer",
        "days": {},
    },
]

# Free value items by campaign type (31 per campaign)
VALUE_ITEMS = {
    "marketing-creative": [
        ("Conversion leak checklist (5 items)", "doc"),
        ("Landing page CTA audit criteria", "doc"),
        ("3 headline formulas that convert", "snippet"),
        ("Form length best practices (1-pager)", "doc"),
        ("Trust signal placement checklist", "doc"),
        ("Above-the-fold audit template", "doc"),
        ("Mobile CTA tap-target checklist", "doc"),
        ("A/B test priority matrix", "doc"),
        ("Landing-to-nurture handoff checklist", "doc"),
        ("Conversion funnel stage definitions", "snippet"),
        ("2-minute page speed fix list", "snippet"),
        ("Top 3 attribution blind spots", "snippet"),
        ("Channel scoring framework (4 questions)", "doc"),
        ("Reallocation cadence template", "doc"),
        ("Spend vs outcome tracking worksheet", "doc"),
        ("Before/after fix example (format)", "doc"),
        ("Creative brief for high-converting ads", "doc"),
        ("Audience match vs creative match checklist", "doc"),
        ("Remarketing list health check", "snippet"),
        ("Lead quality signal checklist", "doc"),
        ("Campaign naming convention for attribution", "snippet"),
        ("UTM parameter template", "doc"),
        ("First-touch vs last-touch comparison", "snippet"),
        ("3 fixes framework (issue → change → impact)", "doc"),
        ("Conversion rate benchmark by industry", "snippet"),
        ("Exit-intent trigger checklist", "doc"),
        ("Thank-you page optimization checklist", "doc"),
        ("Nurture email sequence timing guide", "snippet"),
        ("Lead scoring quick-start (5 signals)", "doc"),
        ("Pipeline contribution by channel template", "doc"),
        ("Monthly conversion review agenda", "doc"),
    ],
    "it-director": [
        ("Systems ownership checklist", "doc"),
        ("Drift audit one-page template", "doc"),
        ("Owner + backup assignment template", "doc"),
        ("Review cadence matrix (weekly/monthly/quarterly)", "doc"),
        ("Orphan system red-flag checklist", "doc"),
        ("Vendor handoff checklist", "doc"),
        ("Runbook template (1-page)", "doc"),
        ("Escalation path template", "doc"),
        ("System dependency map (blank)", "doc"),
        ("Documentation health score (5 questions)", "doc"),
        ("Backlog prioritization matrix", "doc"),
        ("Effort vs impact scoring guide", "doc"),
        ("Partner vs in-house decision tree", "doc"),
        ("Sprint planning priority template", "doc"),
        ("Tech debt vs feature trade-off framework", "doc"),
        ("System retirement checklist", "doc"),
        ("Integration ownership template", "doc"),
        ("Disaster recovery runbook template", "doc"),
        ("Change log template", "doc"),
        ("Stakeholder notification template", "doc"),
        ("Quarterly systems review agenda", "doc"),
        ("Access audit template", "doc"),
        ("License and cost tracking worksheet", "doc"),
        ("Capacity planning 4-question framework", "doc"),
        ("Incident post-mortem template", "doc"),
        ("On-call rotation checklist", "doc"),
        ("Backup verification checklist", "doc"),
        ("Security patch cadence template", "doc"),
        ("Cloud cost allocation template", "doc"),
        ("Application inventory template", "doc"),
        ("Year-end systems review checklist", "doc"),
    ],
    "director-data": [
        ("Decision latency worksheet (5 questions)", "doc"),
        ("KPI latency snapshot (5-question audit)", "doc"),
        ("Report prioritization matrix", "doc"),
        ("Data quality checklist", "doc"),
        ("Owner-based alert template", "doc"),
        ("Time-to-answer tracking worksheet", "doc"),
        ("Bottleneck identification guide", "doc"),
        ("Executive KPI one-pager template", "doc"),
        ("Weekly vs monthly vs quarterly report guide", "doc"),
        ("Data source ownership map", "doc"),
        ("Report retirement criteria", "doc"),
        ("Single source of truth checklist", "doc"),
        ("Dashboard health score (5 items)", "doc"),
        ("Refresh cadence decision guide", "doc"),
        ("Export vs live report trade-off", "doc"),
        ("Alert fatigue reduction checklist", "doc"),
        ("Action-loop template (alert → owner → close)", "doc"),
        ("Cross-functional KPI alignment guide", "doc"),
        ("Report request intake form", "doc"),
        ("Data governance quick-reference", "doc"),
        ("Sensitive data handling checklist", "doc"),
        ("Report usage tracking template", "doc"),
        ("Stale report identification guide", "doc"),
        ("Self-serve vs requested report matrix", "doc"),
        ("ROI of reporting (time-saved calc)", "doc"),
        ("Decision journal template", "doc"),
        ("SLA for report delivery template", "doc"),
        ("Monthly data review agenda", "doc"),
        ("Report consolidation checklist", "doc"),
        ("Executive summary format", "doc"),
        ("Quarterly analytics review agenda", "doc"),
    ],
    "marketing-vp": [
        ("Spend reallocation framework (4 questions)", "doc"),
        ("Channel scoring template", "doc"),
        ("Attribution model comparison (1-pager)", "doc"),
        ("Budget reallocation cadence template", "doc"),
        ("Cost-per-outcome tracking worksheet", "doc"),
        ("Underperforming channel exit criteria", "doc"),
        ("Pilot budget allocation guide", "doc"),
        ("ROAS vs pipeline contribution matrix", "doc"),
        ("Quarterly spend review agenda", "doc"),
        ("Channel mix optimization checklist", "doc"),
        ("Incrementality test design (simple)", "doc"),
        ("Multi-touch attribution quick-start", "doc"),
        ("Spend pacing checklist", "doc"),
        ("Campaign sunset criteria", "doc"),
        ("Creative refresh cadence guide", "doc"),
        ("Audience overlap audit template", "doc"),
        ("Competitive spend benchmarks (sources)", "snippet"),
        ("Vendor consolidation checklist", "doc"),
        ("Contract renewal negotiation points", "doc"),
        ("Marketing tech stack audit", "doc"),
        ("Team capacity vs spend alignment", "doc"),
        ("Approval workflow optimization", "doc"),
        ("Finance handoff template", "doc"),
        ("Forecast vs actual template", "doc"),
        ("Annual planning timeline", "doc"),
        ("Board presentation summary format", "doc"),
        ("Executive briefing one-pager", "doc"),
        ("Stakeholder update template", "doc"),
        ("Win/loss integration guide", "doc"),
        ("Monthly marketing review agenda", "doc"),
        ("Year-end spend analysis template", "doc"),
    ],
    "finance-director": [
        ("System ownership map (blank)", "doc"),
        ("Critical systems inventory template", "doc"),
        ("Review cadence matrix", "doc"),
        ("Audit trail checklist", "doc"),
        ("Cost allocation template", "doc"),
        ("Finance system dependency map", "doc"),
        ("Month-end close checklist", "doc"),
        ("Reconciliation review template", "doc"),
        ("Access control audit template", "doc"),
        ("Vendor management checklist", "doc"),
        ("Compliance documentation template", "doc"),
        ("Exception handling workflow", "doc"),
        ("Approval hierarchy template", "doc"),
        ("Finance runbook template", "doc"),
        ("Disaster recovery for finance systems", "doc"),
        ("Backup verification schedule", "doc"),
        ("Data retention policy checklist", "doc"),
        ("SOX-relevant control checklist", "doc"),
        ("Quarterly finance systems review", "doc"),
        ("Integration ownership (AP, AR, GL)", "doc"),
        ("Report ownership for finance", "doc"),
        ("Close timeline optimization guide", "doc"),
        ("Variance review template", "doc"),
        ("Forecast accuracy tracking", "doc"),
        ("Budget vs actual template", "doc"),
        ("Cash flow visibility checklist", "doc"),
        ("Treasury system handoff template", "doc"),
        ("Audit prep checklist", "doc"),
        ("Year-end close checklist", "doc"),
        ("Finance tech stack inventory", "doc"),
        ("Monthly finance systems health check", "doc"),
    ],
    "c-level": [
        ("KPI latency snapshot (5 questions)", "doc"),
        ("Executive decision-speed diagnostic", "doc"),
        ("Board-level KPI one-pager format", "doc"),
        ("Strategic vs operational KPI split", "doc"),
        ("Time-to-insight tracking worksheet", "doc"),
        ("Cross-functional alignment checklist", "doc"),
        ("Executive summary template", "doc"),
        ("Deck-to-dashboard migration guide", "doc"),
        ("Leading vs lagging indicator guide", "doc"),
        ("Monthly business review agenda", "doc"),
        ("Quarterly planning alignment template", "doc"),
        ("Stakeholder communication cadence", "doc"),
        ("Decision-making latency audit", "doc"),
        ("Initiative prioritization matrix", "doc"),
        ("Resource allocation framework", "doc"),
        ("Risk visibility checklist", "doc"),
        ("Compliance status one-pager", "doc"),
        ("Org health metrics template", "doc"),
        ("Customer health score summary", "doc"),
        ("Revenue attribution at exec level", "doc"),
        ("Cost reduction opportunity matrix", "doc"),
        ("Transformation tracking template", "doc"),
        ("Change readiness checklist", "doc"),
        ("Executive dashboard principles", "doc"),
        ("Meeting effectiveness checklist", "doc"),
        ("Delegation of authority template", "doc"),
        ("Escalation criteria for executives", "doc"),
        ("Board prep checklist", "doc"),
        ("Investor communication template", "doc"),
        ("Annual strategic review agenda", "doc"),
        ("Executive operating rhythm template", "doc"),
    ],
}

# Map (val_type, day_index_0based) -> doc filename in docs/templates/
# Days without a mapping: create from description or use run_conversion_teardown/run_attribution_check
VALUE_TO_DOC = {
    ("marketing-creative", 0): "08 Conversion Leak Checklist.md",
    ("marketing-creative", 1): "10 Landing Page CTA Audit Criteria.md",
    ("marketing-creative", 4): "09 Trust Signal Placement Checklist.md",
    ("marketing-creative", 13): "11 Channel Scoring Framework.md",
    ("marketing-creative", 22): "13 UTM Parameter Template.md",
    ("it-director", 0): "01 Systems Ownership Checklist.md",
    ("it-director", 1): "02 Drift Audit Template.md",
    ("it-director", 4): "12 Orphan System Red Flag Checklist.md",
    ("it-director", 10): "06 Backlog Prioritization Matrix.md",
    ("director-data", 0): "03 Decision Latency Worksheet.md",
    ("director-data", 1): "07 KPI Latency Snapshot.md",
    ("marketing-vp", 0): "04 Spend Reallocation Framework.md",
    ("finance-director", 0): "05 System Ownership Map.md",
    ("c-level", 0): "07 KPI Latency Snapshot.md",
}

# Map campaign id to value type
CAMPAIGN_VALUE_MAP = {
    "01-marketing-creative-conversion": "marketing-creative",
    "02-marketing-creative-attribution": "marketing-creative",
    "03-it-director-ownership": "it-director",
    "04-it-director-drift": "it-director",
    "05-director-decision-latency": "director-data",
    "06-marketing-vp-spend": "marketing-vp",
    "07-finance-director-ownership": "finance-director",
    "08-it-director-backlog": "it-director",
    "09-marketing-manager-fixes": "marketing-creative",
    "10-c-level-kpi-latency": "c-level",
}

TEMPLATE_FORMAT = """---
Persona: {persona}
Campaign: {campaign_name}
Day: {day}
Channel: {channel}
---

SUBJECT: {subject}

BODY:

{body}

---

FREE VALUE:
{free_value}

ATTACH: {doc_source}

CTA:
{cta}
"""


def get_channel(day):
    """Alternate email/LinkedIn - email heavy."""
    if day in (3, 7, 14, 21, 28):
        return "LinkedIn"
    return "Email"


def build_content(campaign, day, value_item, value_type):
    cid = campaign["id"]
    val_type = CAMPAIGN_VALUE_MAP[cid]
    channel = get_channel(day)

    # Subject lines by persona type (varied)
    if "marketing" in cid and "creative" in cid:
        subjects = [
            "Quick thing I put together for you",
            "One-pager from our team",
            "No strings — use it or not",
            "Thought you might find this useful",
            "Ran this for a similar team",
            "Free resource — your call",
        ]
    elif "it-director" in cid:
        subjects = [
            "Template we use with IT teams",
            "Checklist that's helped a few directors",
            "One-pager — no call needed",
            "Something we've seen work",
            "Quick reference for your team",
            "Use it internally if helpful",
        ]
    elif "finance" in cid:
        subjects = [
            "Framework finance teams use",
            "Template — no strings",
            "Something for your review cadence",
            "Use it or adapt it",
            "Quick reference we use",
            "Thought it might help",
        ]
    elif "c-level" in cid or "10-" in cid:
        subjects = [
            "Executive-level snapshot",
            "5 questions that surface latency",
            "Framework for decision speed",
            "Quick diagnostic — your call",
            "Something for your leadership team",
            "No meeting needed",
        ]
    else:
        subjects = [
            "Quick resource for you",
            "One-pager — no strings",
            "Thought you might find this useful",
            "Use it however you want",
            "Something we've seen work",
            "Free to use or ignore",
        ]

    subject = subjects[day % len(subjects)]

    # Lead-ins by persona (adds relevance)
    lead_ins = {
        "marketing-creative": [
            "Most teams have traffic but leave conversion on the table. ",
            "We see a lot of landing pages — a few patterns stand out. ",
            "Conversion leaks are usually fixable in under a week. ",
            "Quick wins > long projects. ",
            "Your team can run this themselves. ",
        ],
        "it-director": [
            "Orphan systems and drift cost time and risk. ",
            "Clear ownership = fewer surprises. ",
            "We use this with teams managing multiple systems. ",
            "5–15 minutes usually surfaces the gaps. ",
            "No vendor lock-in — use it as-is. ",
        ],
        "director-data": [
            "Decision delay is usually fixable with 1–2 report changes. ",
            "Time-to-answer is the metric that matters. ",
            "Most teams have the data; it's just hard to get to. ",
            "Owner-based alerts beat passive dashboards. ",
            "Focus on the reports that drive actual decisions. ",
        ],
        "marketing-vp": [
            "Spend reallocation is where most teams leave money. ",
            "A few questions usually reveal the leaks. ",
            "Channel mix optimization doesn't need complex models. ",
            "Quick framework, big impact. ",
            "Your team can run this without us. ",
        ],
        "finance-director": [
            "Critical systems need clear owners and cadence. ",
            "Gaps in ownership show up at month-end. ",
            "We've seen this work for finance teams. ",
            "15 minutes to fill in, worth the visibility. ",
            "No call required — use it internally. ",
        ],
        "c-level": [
            "Decision latency is usually visible with 5 questions. ",
            "Exec teams need answers in minutes, not days. ",
            "This surfaces where time gets lost. ",
            "Simple diagnostic, high impact. ",
            "Your leadership team can run it themselves. ",
        ],
    }
    lead_in = lead_ins.get(val_type, ["Thought you might find this useful. "])[day % 5]

    body = f"""[Name] —

{lead_in}Attached: {value_item}

Sent it over. No call or follow-up from us — use it with your team, adapt it, or ignore it. Whatever's useful."""

    # Every 5th day (5, 10, 15, 20, 25, 30): soft CTA for a call
    if day in (5, 10, 15, 20, 25, 30):
        cta = "If it would help to walk through this together, we can do a 15-min call. No pressure — reply if you'd like to schedule."
    else:
        cta = "No ask. If helpful, keep it. If you have questions, reply and we can chat — but no pressure."

    # Doc to attach
    doc_key = (val_type, day - 1)
    doc_source = VALUE_TO_DOC.get(doc_key)
    if doc_source:
        doc_source = f"docs/templates/{doc_source}"
    else:
        doc_source = "Create from description above, or use scripts/run_conversion_teardown.py / run_attribution_check.py for campaigns 01, 02, 09"

    return {
        "persona": campaign["persona"],
        "campaign_name": campaign["name"],
        "day": day,
        "channel": channel,
        "subject": subject,
        "body": body,
        "free_value": value_item,
        "doc_source": doc_source,
        "cta": cta,
    }


def main():
    BASE.mkdir(parents=True, exist_ok=True)

    # Remove old hyphenated campaign folders
    import shutil
    for item in BASE.iterdir():
        if item.is_dir() and "-" in item.name and item.name[0].isdigit():
            shutil.rmtree(item)
            print(f"Removed old folder: {item.name}")

    for campaign in CAMPAIGNS:
        cid = campaign["id"]
        folder_name = CAMPAIGN_FOLDERS.get(cid, cid.replace("-", " ").title())
        val_type = CAMPAIGN_VALUE_MAP[cid]
        values = VALUE_ITEMS[val_type]

        camp_dir = BASE / folder_name
        camp_dir.mkdir(parents=True, exist_ok=True)

        for day in range(1, 32):
            value_item, _ = values[day - 1]
            content = build_content(campaign, day, value_item, val_type)
            text = TEMPLATE_FORMAT.format(**content)

            day_file = camp_dir / f"Day {day:02d}.md"
            day_file.write_text(text, encoding="utf-8")

        print(f"Created {camp_dir} (31 templates)")

    # Write campaign index (use folder names for links)
    index = ["# Value-First Campaign Cadence (31 Days)\n\n"]
    index.append("| Campaign | Persona | Days |\n|----------|----------|------|\n")
    for c in CAMPAIGNS:
        folder = CAMPAIGN_FOLDERS.get(c["id"], c["id"])
        index.append(f"| [{c['name']}]({folder}/) | {c['persona']} | 31 |\n")
    (BASE / "README.md").write_text("".join(index), encoding="utf-8")
    print(f"Created {BASE / 'README.md'}")


if __name__ == "__main__":
    main()
