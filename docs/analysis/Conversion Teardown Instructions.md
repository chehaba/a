# Conversion Teardown + 3 Fixes — Instructions

**Covers:** Messages #1 (Conversion Teardown) and #9 (3 Fixes One-Pager)

These require analyzing a prospect's landing page or ads to find conversion leaks and recommend 3 fixes.

---

## Step-by-Step: Do It Yourself

### Step 1 — Get the asset
- Visit their website or the landing page they use for paid traffic.
- If they run ads (Google, LinkedIn, etc.), click through to see the destination page.
- Take a screenshot or save the URL.

### Step 2 — Run through the checklist

For each item, note Pass / Fail / N/A:

| Check | What to look for |
|-------|------------------|
| **Clear value prop** | Can you tell what they offer in &lt;5 seconds? |
| **Single primary CTA** | One main button/link, not 5 competing asks |
| **Above-the-fold CTA** | Main action visible without scrolling |
| **Form length** | Fewer fields = higher conversion (3–5 ideal for lead gen) |
| **Trust signals** | Logos, testimonials, security badges near form |
| **Mobile-friendly** | Page works on phone; CTA tappable |
| **Page speed** | Loads in &lt;3 sec? (Use PageSpeed Insights) |
| **Headline match** | If from ad, does headline match page message? |

### Step 3 — Identify the 3 biggest leaks

From your checklist, pick the 3 items that failed and would have the biggest impact:

1. **Fix 1:** [Issue] → [Recommended change] → [Expected impact]
2. **Fix 2:** [Issue] → [Recommended change] → [Expected impact]
3. **Fix 3:** [Issue] → [Recommended change] → [Expected impact]

### Step 4 — Write the one-pager

Use this structure:

```
CONVERSION TEARDOWN — [Company/Page Name]
Date: [Date]

QUICK TAKE
[1–2 sentences on overall impression]

3 FIXES
1. [Fix name]
   - Current: [what’s wrong]
   - Change: [what to do]
   - Why: [impact]

2. [Fix name]
   - Current: [what’s wrong]
   - Change: [what to do]
   - Why: [impact]

3. [Fix name]
   - Current: [what’s wrong]
   - Change: [what to do]
   - Why: [impact]

No call required — use however you want.
```

### Step 5 — Send
Attach the one-pager (PDF or doc) to your outreach message.

---

## Script: Semi-Automated Analysis

The script `run_conversion_teardown.py` (see below) fetches a URL, extracts structure (forms, CTAs, headings), and outputs a checklist result. You still add the 3 fixes and one-pager copy.

**Usage:** (run from repo root)
```bash
python3 scripts/run_conversion_teardown.py "https://example.com/landing-page"
```

---

## AI Prompt: Have AI Do the Analysis

Copy the prompt below and paste into ChatGPT, Claude, or similar. Include the URL or paste the page HTML.

**Prompt:**

```
I need a conversion teardown of a landing page for outbound prospecting. I'll provide a URL or the page content.

Your task:
1. Review the page for conversion best practices.
2. Identify the top 3 conversion leaks (things that likely hurt lead gen or signup rate).
3. For each fix: (a) what's wrong, (b) what to change, (c) expected impact in 1 sentence.

Format your output like this:

CONVERSION TEARDOWN — [Page/Company]
QUICK TAKE: [1–2 sentences]

FIX 1: [Name]
- Current: [issue]
- Change: [recommendation]
- Why: [impact]

FIX 2: [Name]
- Current: [issue]
- Change: [recommendation]
- Why: [impact]

FIX 3: [Name]
- Current: [issue]
- Change: [recommendation]
- Why: [impact]

Be specific and actionable. Assume the reader will implement changes themselves.

[PASTE URL HERE, or: Here's the page HTML: [paste]]
```

Then paste the URL or HTML and send.
