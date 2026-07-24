# MNTD × Growth Automated · Proposal

**🟢 Live:** https://rsharma-oss.github.io/mntd-proposal/
**Shipped to:** Kate Rothschild (GM, Emerging Brands · Knix) · sent from HubSpot 2026-07-15
**Visibility:** Niki Tapscott (Brand President, Knix) · Cynthia Leo (CMO, Knix) · Raffael Sarracini (VP eCommerce, Knix + MNTD)

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
│   ├── hero-ig.png                          Pints & Periods hero image
│   ├── sms-double-subscribe.png             MS-1 evidence
│   ├── dscart-01…04-*.png                   coupon-conflict story (Section 04 evidence)
│   ├── shop2-order-confirmation.png         DS-7 evidence
│   ├── pdp-conference-slide.png             Section 08 media reference
│   ├── pp-mobile-order-details.png  · pp-popup-on-order-page.png · pp-shipment-journey.png
│   ├── pp-inbox-duplicate-notifications.jpeg  · pp-delivery-sms.png
│   ├── pp-unbox-01-received.jpeg … pp-unbox-08-mint-gift.jpeg   (unboxing gallery)
│   ├── email-01…09-*.png / .eml             transactional fulfilment sequence (Jul 9–11)
│   ├── email-w1…w5-*.png / .eml             welcome + campaign series (Jun 21 – Jul 7)
│   └── partners/                            16 vendor logos (Shopify, Klaviyo, Loop, etc.)
├── .github/workflows/
│   └── pages.yml                            Actions deploy to GitHub Pages
├── README.md            this file
├── HANDOFF.md           session state · resume protocol · post-send watchlist
├── PLAYBOOK.md          framework for scaling this format to other mid-market DTC brands
├── TEMPLATE-BUILD.md    concrete work required to extract MNTD into a reusable template
└── BACKLOG.md           known TODOs and placeholders awaiting artefacts
```

---

## Section outline (14 + scorecard)

| # | Section | Contents |
|---|---|---|
| 01 | Story | Hero · Pints & Periods opener · Instagram photo · stakeholder map |
| 02 | In-Store · Knix Eaton Centre | IS-1 through IS-4 · retail merchandising observations |
| 03 | Shop 1 · Mobile | MS-1 through MS-5 · mobile mystery shop |
| 04 | Shop 2 · Desktop | DS-1 through DS-7 · desktop purchase experience · 4-PNG coupon-conflict evidence card |
| 05 | Pre-Purchase Journey Map | 7-stage flow chart · 13 clickable touchpoints across 4 channels |
| 06 | Post-Purchase · Delivery to Doorstep | PP-1 through PP-11 · 6-stage flow chart · thesis callout · unboxing gallery · fulfilment email timeline · chronological `data-seq` numbering |
| 07 | The Gaps | 6-card weighted audit · big-finding callout (SMS 20% vs Email 15%) · evidence panel |
| 08 | Commercial Strategy | Value-proposition fraction diagram · 5 strategic cards · Style & Scale PDP video reference |
| 09 | Segmentation | 3 lanes · Klaviyo → ad-platform orchestration |
| 10 | The Engagement | 5 pillars · 90-day plan · investment card |
| 11 | The Team | Rahul + Raff (NMM shared origin) · Founder card GA-blue border · 2 client references (Jeff/NMM + Brett/WBM) |
| 12 | Tools & Stack | 16 partner cards with logos · Klaviyo Master Silver badge |
| 13 | The Proposal | Retainer + Phase 2 AEO/SEO/Reddit tracks |
| 14 | Legal & Onboarding | 4-doc timeline (NDA → MSA → SOW → Insurance) |
| — | scorecard.html | Standalone 34/100 weighted audit · 9 dimensions · Post-Purchase supplementary finding |

---

## How to view

**Live:** https://rsharma-oss.github.io/mntd-proposal/

**Local:**
```bash
open /Users/rahulsharma/mntd-proposal/index.html
```

Everything is self-contained (relative asset paths, no build step, no server needed).

**Light / Dark toggle** in the top-right of the nav — choice persists across `index.html` and `scorecard.html` via `localStorage['mntd_theme']`. Dark palette lifted from the WBM proposal work (`--bg:#121212`, `--surface-1:#1B1B26`, `--ink-3:#C1CEE0`).

---

## Design system

- **Palette:** GA Blue `#334FB4` · GA Green `#2D9C56` · Carbon `#121212` · Cloud `#F3F3F3` · Warn `#F59E0B` · Critical `#DC2626`
- **Type:** `Assistant` (body 400–800) · `DM Serif Display` (accents 400) · `DM Mono` (data 400–500)
- **Sticky topbar:** two rows (brand + scrollable nav) · height ~124px · `scroll-margin-top: 140px` applied to every section anchor
- **Lightbox:** any `<img class="expandable">` opens full-screen · Escape / click-outside / × to close
- **Accordions:** native `<details>` for all IS-/MS-/DS-/PP- observations · `+` → `×` rotation on open · deep-linkable via `#ms3`, `#pp7`, etc.

---

## Deployment

**Live** at https://rsharma-oss.github.io/mntd-proposal/ · every push to `main` auto-deploys via `.github/workflows/pages.yml`.

Repo: [github.com/rsharma-oss/mntd-proposal](https://github.com/rsharma-oss/mntd-proposal)
Actions: [github.com/rsharma-oss/mntd-proposal/actions](https://github.com/rsharma-oss/mntd-proposal/actions)

For the deploy history / recovery procedure, see `HANDOFF.md`.
For extracting this into a reusable template for brand #2, see `TEMPLATE-BUILD.md`.
