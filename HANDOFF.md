# HANDOFF · MNTD × Growth Automated Proposal

**Status:** Local · not deployed · content complete pending 4 placeholder artefacts
**Last worked:** Jul 15, 2026
**Owner:** Rahul Sharma · Growth Automated
**Working directory:** `/Users/rahulsharma/mntd-proposal/`

---

## Resume protocol · run this first on any new session

Before making any change, do these three checks:

1. **Verify assets are current.** Run `ls -lt /Users/rahulsharma/mntd-proposal/assets/ | head -6` — any new file (screenshot, forwarded email) since the last change means content has drifted and BACKLOG.md may need updating.
2. **Grep for stale numbers.** `grep -nE "Section 0[0-9]|Sections 0[0-9] |four emails|3 of 4" index.html` — any hit outside the CSS/comments needs the fix from the "Full-doc QA" pattern in this file.
3. **Open in browser.** `open index.html` and skim top-to-bottom before writing new copy. Nav labels + section numbers are the fastest way to spot drift.

Then re-read BACKLOG.md and the "Open placeholders" list below to know what's genuinely unfinished vs stylistic polish.

---

## What's done

### Structure
- 14 sections + separate `scorecard.html` page (all cross-linked)
- Two-row sticky topbar · MNTD mark left · GA logo right · scrollable nav (14 anchors + Scorecard external link)
- Light/dark theme toggle · persists via `localStorage`
- Lightbox system for all `.expandable` images (native `<details>` accordions for observations)
- Anchor scroll-offset (140px) so headers land below the sticky nav

### Content
- Hero with real Pints & Periods Instagram photo · stakeholder map (Kate/Raff/Niki/Cynthia + 2 TBD)
- Value-proposition fraction diagram in Section 08 · MNTD flagged as leading with "Why Buy Now"
- Interactive pre-purchase flow chart (Section 05) · 7 stages · 13 nodes · emails and SMS open in lightbox
- Interactive post-purchase flow chart (Section 06) · 6 stages · 15 nodes · MNTD + FleetOptics + Web + Physical lanes
- Full fulfilment email timeline · 9 emails rendered as PNG screenshots, all clickable
- 5 welcome/campaign email screenshots (Jun 21 – Jul 7) with lightbox
- Full unboxing gallery (8 photos)
- Section 11 Team · Raff's NMM shared-origin corrected · NMM connection chip · 2 client references (Jeff / Brett)
- 16 tool cards with real vendor logos (Shopify Files MCP + Google favicons) · Klaviyo Master Silver + Partner badges

### Numbers verified accurate
- 5 marketing emails · 9 transactional emails · 2 SMS threads
- 3× same code repeated · 7/14 DMARC fails
- 6 gap cards · 5 Commercial cards · 3 Segmentation lanes · 5 Engagement pillars
- 16 Tools & Stack items · 4 Legal timeline steps

---

## Open placeholders · what's genuinely missing

Everything below is intentionally left as a placeholder in the doc. Ship-blocking = 0. Nice-to-have when the artefact arrives.

| Placeholder | Where | What to drop in |
|---|---|---|
| Checkout coupon-rejected screenshot | Section 06 · evidence card 2 | The 4:48 PM Shop Pay page showing `WELCOMEMNTD1557TPTGFM couldn't be used` — lost in an earlier file rename mishap, needs re-forward from Downloads. Save as `assets/shop2-checkout-coupon-rejected.png`. |
| Side-cart busy screenshot | Section 06 · evidence card 3 | A frame of the wearmntd.ca cart drawer with upsells + free-shipping + GWP + discount status all firing at once. Evidence for DS-4. |
| Repeat-visit receipt | Section 06 · evidence card 4 | Order confirmation from the second desktop-shop session. |
| Klaviyo post-purchase marketing flow | Section 06 · evidence card 5 | Marketing re-engagement flow export (distinct from the 9 transactional emails already in the timeline). |
| AEO 9-page deck | Section 13 · Proposal appendix | Referenced but not built. Follow-on content once Track A is on the table. |
| Bespoke Raff one-pager (optional) | Section 11 · Raff card | The current card is now solid with NMM shared-origin. A separate 1-pager is no longer strictly needed but was originally planned. |

---

## Not deployed

Repo `rsharma-oss/mntd-proposal` does not yet exist on GitHub. Actions workflow is pre-committed at `.github/workflows/pages.yml`. To deploy:

1. Create empty public repo at github.com/new (owner `rsharma-oss`, name `mntd-proposal`, no README/gitignore/license).
2. Widen your fine-grained PAT to include `mntd-proposal` (Content + Workflow scopes).
3. Locally: commit current state (`git add -A && git commit -m "MNTD proposal · Jul 15 build"`), then `git remote add origin https://github.com/rsharma-oss/mntd-proposal.git && git push -u origin main`.
4. In GitHub UI: Settings → Pages → Source: **GitHub Actions**.
5. URL: `https://rsharma-oss.github.io/mntd-proposal/` (auto-deploys on push after step 4).

---

## Related sessions / prior work

- **WBM Technologies proposal** (`~/wbm-ai-dashboard/`) — same template lineage · Brett Bailey testimonial in Section 11 comes from this engagement
- **Hockeystickman.com proposal** (`~/hockeystickman-ai-visibility/`) — original template for the "founder-to-founder mystery-shop" format
- **Growth Automated pitch toolkit** (`~/growth-automated-pitch-toolkit/`) — shared BACKLOG.md tracks WCAG + template polish work
- **Telus AI visibility report** (via `~/.claude/scripts/telus-rebuild.py`) — reporting-side scripts, not proposal-side

---

## Voice + tone reference

Follows the "Growth Automated voice" memory: founder-to-founder · first-person · concrete detail over abstract claim · one number per sentence maximum · never "leverage" or "synergy" · em-dash for pivots · avoids consulting-speak. See `PLAYBOOK.md` for the fuller voice spec.

---

## What I'd tell the next session

- **The evidence-first structure is the whole point.** Every Section 07 (Gaps) claim ties back to a specific mystery-shop observation. Never add a "gap" without evidence upstream.
- **Section numbers drift when sections are added.** Every insert has cost — 8–10 cross-refs elsewhere. Grep after every insert.
- **Kate is the primary recipient.** Niki/Cynthia are audience but should never be addressed directly. Joanna is out entirely.
- **The Klaviyo Master Silver badge in Section 12 is real proof — don't move it into a footer, keep it card-adjacent.**
- **The Ted Baker anecdote in PP-11 is Rahul's real voice** — don't sanitise it.
- **Loop bought Wonderment** (consolidated to one card in Section 12). Don't split them back apart.
- If pricing needs to be reintroduced, `grep '\*\.\*'` finds all 4 spots that currently read "Pricing TBD."
