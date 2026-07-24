# BACKLOG · MNTD Proposal

Everything below is acknowledged-and-deferred. Nothing here is ship-blocking. The proposal is live at https://rsharma-oss.github.io/mntd-proposal/ and has been sent to Kate — the queue below is post-send polish, follow-through, and template extraction.

*Last updated: Jul 15, 2026*

---

## Post-send follow-through

| Task | Trigger | Effort |
|---|---|---|
| Watch Kate's HubSpot contact for open/click/reply activity | Passive — check daily until reply | 2 min/day |
| Draft Cynthia intro | After Kate opens or on day 5 with no reply | 20 min |
| Draft Niki intro | Only if Kate loops her in OR after week 2 with no reply | 20 min |
| Draft Raff back-channel note | Anytime — separate track since we have NMM history | 15 min |
| Follow-up nudge to Kate | Day 5 with no response · reference Section 06 as hook · one nudge only | 10 min |
| Update `HANDOFF.md` with reply signal + next step | On any inbound signal | 5 min |

---

## Placeholder artefacts awaiting drop-in

Save each into `/Users/rahulsharma/mntd-proposal/assets/` with the filename in the right column. HTML is already wired to display them — no code changes needed. Push after drop = auto-deploy.

| Item | Where in doc | Filename to drop |
|---|---|---|
| Shop Pay checkout · WELCOMEMNTD1557TPTGFM rejection | Section 06 · evidence card 2 | `shop2-checkout-coupon-rejected.png` |
| Side-cart drawer at a busy moment (upsells + shipping bar + GWP + discount all firing) | Section 06 · evidence card 3 | `shop2-sidecart-busy.png` |
| Repeat-visit receipt (second desktop shop session) | Section 06 · evidence card 4 | `shop2-repeat-receipt.png` |
| Klaviyo post-purchase MARKETING flow export (distinct from the 9 transactional emails already shown) | Section 06 · evidence card 5 | `shop2-marketing-flow.png` |

---

## Missing content

- **AEO 9-page deck** (Section 13 · Proposal appendix) — referenced as follow-on content but not yet built. Only needed if Track A goes live.
- **Bespoke Raff one-pager** — the current Section 11 card now tells the NMM shared-origin story properly; separate 1-pager is no longer required.

---

## Cosmetic / polish

- **Klaviyo Master Silver badge in dark mode** looks slightly muted (dark bg on dark theme). Consider swapping to `klaviyo-master-silver-badge-light.png` variant (already in Shopify Files) when theme is dark.
- **Partner logos with small source resolution** (Gorgias, Loop, Task Husky came in as 16×16 favicons that Google upscaled to 256). Not urgent — they render OK at 32px corner — but could be swapped for vendor-provided assets when available.
- **Section 05 pre-purchase chart** wraps horizontally at narrow widths (min-width 1030px). Native horizontal scroll handles it; consider adding a fade-right indicator like the top nav has if it feels non-obvious.
- **Legal timeline** in Section 14 stacks vertically below 800px with arrow rotation — works, but arrows look slightly odd rotated. Low priority.

---

## Template extraction · to make this reusable for brand #2

See `TEMPLATE-BUILD.md` for the full work list. Summary of what's still to do:

- Create `~/growth-automated-pitch-toolkit/` repo (does not yet exist)
- Extract `template-index.html` with `{{TOKEN}}` placeholders (~4 hours)
- Extract `template-scorecard.html` (~1 hour)
- Move 16 partner logos to shared `partner-logos/` directory (~30 min)
- Extract `.eml → .png` render script as `render-emails.py` (~2 hours)
- Build `build-proposal.py` scaffolding CLI (~4 hours)
- Document the token catalog (~2 hours)
- First-run validation on brand #2 (~1 day)

**Total estimated effort:** ~2 days of focused work to make brand #2 execute in ≤1 day.

---

## Cross-reference to shared toolkit

The following items were originally logged in `~/growth-automated-pitch-toolkit/BACKLOG.md` — but that repo does not exist yet. Move these when the toolkit is created:

- WCAG · Talon-mode contrast (only affects WBM styling, not MNTD, but same base template) — WBM-specific, deferred.
- `open-proposal` builder `<input type="url">` truncation on large base64 logos — fixed for MNTD via direct file paths in `assets/`.
- `build_fast.py` hardcoded `time_range: 90d` — Peekaboo API limitation, not MNTD-specific.

---

## Deployment / repo

**Done.** Repo `rsharma-oss/mntd-proposal` live. Actions workflow deploying on push. URL live at https://rsharma-oss.github.io/mntd-proposal/.

Only thing pending: revoke the plain-text PAT that was pasted in chat during the initial push, and generate a fresh one when convenient. The current PAT is bound to macOS Keychain and works for silent pushes — no urgency, but hygiene.

---

## Ideas parked · not doing unless asked

- **Video walkthrough** of the proposal (Loom-style) as an additional artefact for the HubSpot send. Could be a strong differentiator for brand #2.
- **PDF export** via Chrome print-to-PDF. Currently no styles for print media.
- **A/B version** with pricing exposed vs pricing-TBD. Would need a config toggle.
- **Auto-refresh scorecard** from AI Peekaboo API results. Currently manual; would need a build script.
- **Retention-focused variant** for brands where post-purchase is the primary opportunity (invert Sections 03/04 emphasis to 05/06).
- **B2B/wholesale variant** for brands with dual DTC + wholesale motion.
