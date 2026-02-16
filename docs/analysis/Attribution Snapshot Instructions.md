# Attribution Snapshot — Instructions

**Covers:** Message #2 (Attribution Snapshot)

This requires inferring where attribution might break down based on what you can see (website structure, ad destinations, public info). You don't have access to their analytics.

---

## Step-by-Step: Do It Yourself

### Step 1 — Map their traffic sources

From their website and any ads you can find:
- Do they run paid search (Google Ads)?
- Do they run paid social (LinkedIn, Meta)?
- Do they have organic/blog/SEO content?
- Do they run webinars, events, or email campaigns?
- Check: Do their ads link to dedicated landing pages or the homepage?

### Step 2 — Common attribution gaps (use this checklist)

| Gap | How to infer | Typical fix |
|-----|--------------|-------------|
| **Last-click only** | Can't verify; assume common. | Multi-touch or first-touch + last-touch |
| **No UTM on ads** | Ad links may lack UTM params. | Add campaign/source/medium to all links |
| **Homepage as destination** | Ads point to homepage, not dedicated page. | Create campaign-specific landing pages |
| **Form without source field** | Forms don't capture where lead came from. | Hidden field or dropdown: How did you hear about us? |
| **No cross-channel view** | Single-channel reporting only. | Unified dashboard or simple consolidation |
| **Long delay between touch and conversion** | B2B has long cycles. | Extend attribution window; use pipeline attribution |

### Step 3 — Write the snapshot

Use this structure:

```
ATTRIBUTION SNAPSHOT — [Company]
Based on: [website review / ad scan] — no analytics access

OBSERVED
- Traffic sources: [list what you see]
- Ad destinations: [homepage vs landing pages]
- Form capture: [any visible source tracking?]

LIKELY GAPS (where attribution often breaks)
1. [Gap] — [why it matters] — [one change that would help]
2. [Gap] — [why it matters] — [one change that would help]
3. [Gap] — [why it matters] — [one change that would help]

ONE CHANGE THAT WOULD SURFACE IT
[Single most impactful fix, e.g., "Add UTM parameters to all paid links and a hidden form field to capture first-touch source."]

No call required — use or ignore as you like.
```

### Step 4 — Send
Attach as PDF or paste into email.

---

## Script: Lightweight Structure Check

The script `run_attribution_check.py` (see below) fetches a URL and looks for:
- UTM parameters in links
- Forms and whether they might capture source
- Number of distinct landing URLs (homepage vs dedicated)

It outputs a short report. You add the narrative.

**Usage:** (run from repo root)
```bash
python3 scripts/run_attribution_check.py "https://example.com"
```

---

## AI Prompt: Have AI Do the Snapshot

**Prompt:**

```
I need an attribution snapshot for outbound prospecting. I'll provide a company's website URL (or describe what I see).

Your task:
1. Assume we DON'T have access to their analytics.
2. Based on typical B2B setups, list 3–4 common attribution gaps that could apply.
3. For each: (a) what the gap is, (b) why it matters, (c) one change that would help surface it.
4. End with: "One change that would surface it" — the single highest-impact fix.

Format:

ATTRIBUTION SNAPSHOT — [Company]
OBSERVED: [What we can infer from the site]

LIKELY GAPS:
1. [Gap] — [Why it matters] — [One change]
2. [Gap] — [Why it matters] — [One change]
3. [Gap] — [Why it matters] — [One change]

ONE CHANGE THAT WOULD SURFACE IT:
[Single recommendation]

No call required.

[PASTE URL or describe the site]
```

Then paste the URL or a short description and send.
