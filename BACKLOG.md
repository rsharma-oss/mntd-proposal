# BACKLOG · MNTD Proposal

Everything below is acknowledged-and-deferred. Nothing here is ship-blocking. Prioritised top-to-bottom within each block.

*Last updated: Jul 15, 2026*

---

## Placeholder artefacts awaiting drop-in

Save each into `/Users/rahulsharma/mntd-proposal/assets/` with the filename in the right column. HTML is already wired to display them — no code changes needed.

| Item | Where in doc | Filename to drop |
|---|---|---|
| Shop Pay checkout · WELCOMEMNTD1557TPTGFM rejection | Section 06 · evidence card 2 | `shop2-checkout-coupon-rejected.png` |
| Side-cart drawer at a busy moment (upsells + shipping bar + GWP + discount all firing) | Section 06 · evidence card 3 | `shop2-sidecart-busy.png` |
| Repeat-visit receipt (second desktop shop session) | Section 06 · evidence card 4 | `shop2-repeat-receipt.png` |
| Klaviyo post-purchase MARKETING flow export (distinct from the 9 transactional emails already shown) | Section 06 · evidence card 5 | `shop2-marketing-flow.png` |

---

## Missing content

- **AEO 9-page deck** (Section 13 · Proposal appendix) — referenced as follow-on content but not yet built. Only needed if Track A goes live.
- **Bespoke Raff one-pager** — the current Section 11 card now tells the NMM shared-origin story properly; separate 1-pager was originally planned but is no longer required.

---

## Cosmetic / polish

- **Klaviyo Master Silver badge in dark mode** looks slightly muted (dark bg on dark theme). Consider swapping to `klaviyo-master-silver-badge-light.png` variant (already in Shopify Files) when theme is dark.
- **Partner logos with small source resolution** (Gorgias, Loop, Task Husky came in as 16×16 favicons that Google upscaled to 256). Not urgent — they render OK at 32px corner — but could be swapped for vendor-provided assets when available.
- **Section 05 pre-purchase chart** wraps horizontally at narrow widths (min-width 1030px). Native horizontal scroll handles it; consider adding a fade-right indicator like the top nav has if it feels non-obvious.
- **Legal timeline** in Section 14 stacks vertically below 800px with arrow rotation — works, but arrows look slightly odd rotated. Low priority.

---

## Cross-reference to shared toolkit

The following items were originally logged in `~/growth-automated-pitch-toolkit/BACKLOG.md` and apply to this template lineage:

- WCAG · Talon-mode contrast (only affects WBM styling, not MNTD, but same base template) — WBM-specific, deferred.
- `open-proposal` builder `<input type="url">` truncation on large base64 logos — fixed for MNTD via direct file paths in `assets/`.
- `build_fast.py` hardcoded `time_range: 90d` — Peekaboo API limitation, not MNTD-specific.

---

## Deployment / repo

- Repo `rsharma-oss/mntd-proposal` doesn't exist on GitHub yet. Needs create + PAT-scope widening + push. See HANDOFF.md for the 5-step recipe.
- Actions workflow (`.github/workflows/pages.yml`) is pre-committed and ready.

---

## Ideas parked · not doing unless asked

- **Video walkthrough** of the proposal (Loom-style) as an additional artefact for the HubSpot send.
- **PDF export** via Chrome print-to-PDF. Currently no styles for print media.
- **A/B version** with pricing exposed vs pricing-TBD. Would need a config toggle.
- **Auto-refresh scorecard** from AI Peekaboo API results. Currently manual; would need a build script.
