# MNTD × Growth Automated · Proposal

A single-page HTML proposal for MNTD (Knix Group's menswear brand), prepared for **Kate Rothschild · GM, Emerging Brands**, with visibility for **Niki Tapscott (Brand President, Knix)**, **Cynthia Leo (CMO, Knix)**, and inside partner **Raffael Sarracini (VP eCommerce, Knix + MNTD)**.

Prepared July 2026 · Rahul Sharma · Growth Automated · Small Fidelity Services Ltd.

---

## What this repo contains

```
mntd-proposal/
├── index.html           the proposal (14 sections + sticky nav + lightbox)
├── scorecard.html       standalone 34/100 audit scorecard
├── assets/
│   ├── mntd-logo-black.svg
│   ├── ga-logo-color.svg  ga-logo-white.svg
│   ├── hero-ig.png                   Pints & Periods hero image
│   ├── sms-double-subscribe.png      MS-1 evidence
│   ├── shop2-order-confirmation.png  DS-7 evidence
│   ├── pdp-conference-slide.png      Section 08 media reference
│   ├── pp-mobile-order-details.png  · pp-popup-on-order-page.png · pp-shipment-journey.png
│   ├── pp-inbox-duplicate-notifications.jpeg  · pp-delivery-sms.png
│   ├── pp-unbox-01-received.jpeg … pp-unbox-08-mint-gift.jpeg   (unboxing gallery)
│   ├── email-01…09-*.png / .eml     transactional fulfilment sequence (Jul 9–11)
│   ├── email-w1…w5-*.png / .eml     welcome + campaign series (Jun 21 – Jul 7)
│   └── partners/
│       ├── shopify.png · klaviyo.png · klaviyo-partner.png · klaviyo-master-silver.png
│       ├── taskhusky.png · domaine.png · rewind.png · rebuy.png · retentionx.png
│       ├── triplewhale.png · loop.png · wonderment.png
│       ├── gorgias.png · yotpo.png · acceler8.png · reddit.png
│       ├── aipeekaboo.png · dataforseo.png
│       ├── newmetricmedia.png · ga-favicon.png
├── README.md            this file
├── HANDOFF.md           session state + resume protocol
├── PLAYBOOK.md          rubric for scaling this format to other mid-market DTC brands
└── BACKLOG.md           known TODOs and placeholders awaiting artefacts
```

---

## Section outline (14 + scorecard)

| # | Section | Contents |
|---|---|---|
| 01 | Story | Hero · Pints & Periods opener · Instagram photo · stakeholder map |
| 02 | In-Store · Knix Eaton Centre | IS-1 through IS-4 · retail merchandising observations |
| 03 | Shop 1 · Mobile | MS-1 through MS-5 · mobile mystery shop |
| 04 | Shop 2 · Desktop | DS-1 through DS-7 · desktop purchase experience |
| 05 | Pre-Purchase Journey Map | 7-stage flow chart · 13 clickable touchpoints across 4 channels |
| 06 | Post-Purchase · Delivery to Doorstep | PP-1 through PP-11 · 6-stage flow chart · thesis callout · unboxing gallery · fulfilment email timeline |
| 07 | The Gaps | 6-card weighted audit · big-finding callout (SMS 20% vs Email 15%) · evidence panel |
| 08 | Commercial Strategy | Value-proposition fraction diagram · 5 strategic cards · Style & Scale PDP video reference |
| 09 | Segmentation | 3 lanes · Klaviyo → ad-platform orchestration |
| 10 | The Engagement | 5 pillars · 90-day plan · investment card |
| 11 | The Team | Rahul + Raff (NMM shared origin) · 2 client references (Jeff/NMM + Brett/WBM) |
| 12 | Tools & Stack | 16 partner cards with logos |
| 13 | The Proposal | Retainer + Phase 2 AEO/SEO/Reddit tracks |
| 14 | Legal & Onboarding | 4-doc timeline (NDA → MSA → SOW → Insurance) |
| — | scorecard.html | Standalone 34/100 weighted audit · 9 dimensions · Post-Purchase supplementary finding |

---

## How to view

```bash
open /Users/rahulsharma/mntd-proposal/index.html
```

Or drag `index.html` into any modern browser. Everything is self-contained (relative asset paths, no build step, no server needed).

**Light / Dark toggle** in the top-right of the nav — choice persists across `index.html` and `scorecard.html` via `localStorage['mntd_theme']`.

---

## Design system

- **Palette**: GA Blue `#334FB4` · GA Green `#2D9C56` · Carbon `#121212` · Cloud `#F3F3F3` · Warn `#F59E0B` · Critical `#DC2626`
- **Type**: `Assistant` (body 400–800) · `DM Serif Display` (accents 400) · `DM Mono` (data 400–500)
- **Sticky topbar**: two rows (brand + scrollable nav) · height ~124px · `scroll-margin-top: 140px` applied to every section anchor so headers clear the nav on jump
- **Lightbox**: any `<img class="expandable">` opens full-screen · Escape / click-outside / × to close
- **Accordions**: native `<details>` for all IS-/MS-/DS-/PP- observations · `+` → `×` rotation on open

---

## Deployment status

**Local only.** Not pushed to GitHub as of Jul 15, 2026. To deploy:
1. Create empty public repo at `github.com/rsharma-oss/mntd-proposal`
2. Widen fine-grained PAT scope to include the new repo (Content: Read/Write · Workflow: Read/Write)
3. `git remote add origin` + `git push -u origin main` (locally staged commit `21c7cd3` needs updating first — run `git add -A && git commit`)
4. Enable Pages via GitHub Actions (source: GitHub Actions, workflow already at `.github/workflows/pages.yml`)
5. URL will be `https://rsharma-oss.github.io/mntd-proposal/`
