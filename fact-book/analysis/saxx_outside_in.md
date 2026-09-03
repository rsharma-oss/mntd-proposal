# SAXX · Outside-In Evidence · 2026-07-24

## DNS / authentication (live lookups)

| Record | Value |
|---|---|
| SPF (saxxunderwear.ca TXT) | `v=spf1 include:spf.protection.outlook.com -all` |
| DMARC (_dmarc.saxxunderwear.ca) | `v=DMARC1; p=reject; pct=100; ruf=mailto:it@saxxunderwear.com; fo=0:d:s; aspf=r; adkim=r` |
| BIMI (default._bimi.saxxunderwear.ca) | *(not published)* |
| DKIM common selectors (klaviyo1/klaviyo2/dkim/k1/k2/s1/s2/selector1/selector2) | *(none returned — Klaviyo uses their own selector, e.g. `kl2._domainkey`, which per the rubric note is expected)* |
| trk.saxxunderwear.ca CNAME | `d868twil0ijmb.cloudfront.net` (Klaviyo standard tracking hop) |
| trk.saxxunderwear.ca A | `13.227.246.108` |
| MX | `saxxunderwear-ca.mail.protection.outlook.com` (Microsoft 365 Exchange for corp mail) |

**Reads:**
- **DMARC p=reject at 100%** is best-in-class enforcement. Rare in DTC — most brands sit at `p=none` (monitor-only) or `p=quarantine`. This alone signals mature deliverability discipline.
- **SPF authorizes only Outlook.** Per the proforma-email-audit rubric note, Klaviyo authenticates the friendly-from via DKIM (`kl2._domainkey` CNAME), not an SPF include — so the SPF-only-Outlook line is NOT a failure. Corpus confirms 100% auth pass across SPF/DKIM/DMARC.
- **BIMI is not published.** The single visible gap on this dimension. Would benefit from setting up a VMC + BIMI record for the branded-mark-in-inbox surface (Gmail/Yahoo). Small lift, symbolic value.
- **Branded tracking on CloudFront** — Klaviyo standard. Confirms Klaviyo is the ESP for marketing.

---

## Storefront pull (https://saxxunderwear.ca/)

| Signal | Detected |
|---|---|
| HTML fetched | 256,812 bytes |
| Klaviyo detection (page grep) | **12 matches** — Klaviyo confirmed on-site |
| Signup incentive on homepage | "Sign Up / Sign up / newsletter / subscribe" strings present, but **no visible dollar or percentage incentive on the homepage itself** — the 15% off is delivered after signup, not baited pre-signup |
| Loyalty / rewards | **YES** — "Loyalty", "Rewards", "Points" all present on-page |
| Content library | **YES** — "Blog", "Guide" present |
| Locale / bilingual | **No hreflang, no `/fr/` path, no locale alternates** — English only despite Canadian brand |
| Currency | CAD default |

**Reads:**
- Loyalty program present but not surfaced in email personalization (0% loyalty-tier tells in subjects) — potential integration gap.
- English-only storefront is a real segmentation miss for the Canadian market (~22% of Canadians are Francophone; QC market alone is ~5M people). No French-language capture, no French-language stream.
- No pre-signup incentive on the homepage is a deliberate brand choice (vs. the popup-driven 10-15% incentives most DTC brands use) — cleaner UX, likely lower list-growth velocity.

---

## Marketplace-link spot-check (8 random emails deep-parsed)

Random sample: 8 of 155 `.eml` opened, all `href="https?://..."` extracted, hosts tallied.

**Result:** 100% of links routed through `trk.saxxunderwear.ca` (the branded Klaviyo tracker). Zero raw `myshopify.com` links, zero direct marketplace hosts (Amazon / Nordstrom / Walmart / etc.), zero marketplace mentions in the whole-corpus subject scan (155 messages, 0 hits on `amazon|nordstrom|walmart|retail partner`).

**Two possible reads:**
1. **Segmentation** — this subscriber's stream is DTC-only. SAXX may run separate marketplace/retail campaigns to different segments.
2. **Redirect masking** — every link fires through the branded tracker first, so the true destination (potentially marketplace) is only observable after following the redirect. Not resolved from static parse.

Neither read invalidates the corpus scoring — conversion tracking is still best-in-class from the branded-tracking-on-everything signal. But if the marketplace angle is important to the client-facing comparative, follow the redirect chain on a discount email to confirm.

---

## Corpus recap (from `saxx_summary.json`)

| Signal | Value |
|---|---|
| Corpus | 155 campaigns · Sep 22 2025 → Jul 30 2026 (310 days) |
| Cadence | 3.5 sends/week |
| Send-day skew | Sun 40 / Tue 25 / Fri 24 / Thu 20 / Mon 16 / Wed 15 / Sat 15 |
| Send-hour peak (msg tz) | 15:00 |
| ESP account | Klaviyo `Yuky3w` |
| Content mix | 73.5% promo · 16.8% editorial-education · 3.9% winback · 2.6% welcome · 1.9% cart/browse |
| Lifecycle emails observed | 13 |
| Discount depths | 15 / 25 / 30 / 40 (median 40, 24.5% of sends) |
| Bundle/multipack callouts | 27.7% of sends |
| Subject craft | 31-char avg · 23.9% emoji · 14.2% urgency · **1.3% personalization** |
| Image-heavy sends | 0% |
| Compliance footers | 100% unsubscribe / preferences / address |
| Branded tracking on | 100% of sends |
| Auth pass rate (in corpus) | 100% SPF / 100% DKIM / 100% DMARC |
