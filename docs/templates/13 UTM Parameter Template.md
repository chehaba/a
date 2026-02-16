# UTM Parameter Template

Standard parameters for campaign tracking. Use consistently across channels.

---

## Core parameters

| Parameter | Purpose | Example |
|-----------|---------|---------|
| utm_source | Where traffic comes from | google, linkedin, newsletter |
| utm_medium | Marketing medium | cpc, email, social |
| utm_campaign | Campaign name | q1_webinar_2025, product_launch |
| utm_content | Ad or link variant | banner_a, cta_sidebar |
| utm_term | Paid search keyword | power_bi_consulting |

---

## Naming convention

- Lowercase
- Underscores for spaces
- Consistent: source_medium_campaign
- Example: `utm_source=linkedin&utm_medium=paid&utm_campaign=it_director_q1`

---

## Template by channel

**Paid search:**
`utm_source=google&utm_medium=cpc&utm_campaign=[campaign]&utm_term=[keyword]`

**Paid social:**
`utm_source=linkedin&utm_medium=paid&utm_campaign=[campaign]&utm_content=[ad_id]`

**Email:**
`utm_source=newsletter&utm_medium=email&utm_campaign=[name]&utm_content=[cta_location]`

**Organic social:**
`utm_source=linkedin&utm_medium=social&utm_campaign=[initiative]`

---

## Checklist

- [ ] All paid links use UTM
- [ ] Naming is consistent (same campaign = same utm_campaign)
- [ ] CRM or analytics receives UTM values
- [ ] Dashboard or report shows performance by utm_campaign
