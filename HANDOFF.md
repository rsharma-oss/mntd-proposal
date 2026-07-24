# HANDOFF · MNTD × Growth Automated Proposal

**Status:** SHIPPED · deployed · sent to Kate
**Live URL:** https://rsharma-oss.github.io/mntd-proposal/
**Last worked:** Jul 15, 2026
**Owner:** Rahul Sharma · Growth Automated · Small Fidelity Services Ltd.
**Working directory:** `/Users/rahulsharma/mntd-proposal/`

---

## Resume protocol · run this first on any new session

Before making any change, do these three checks:

1. **Verify the URL is still live.** `curl -s -o /dev/null -w "%{http_code}" https://rsharma-oss.github.io/mntd-proposal/` — must return `200`. If not, check the last Actions run at `github.com/rsharma-oss/mntd-proposal/actions`.
2. **Check git state.** `git status && git log --oneline -5` from `/Users/rahulsharma/mntd-proposal/`. Uncommitted changes locally = drift from live. Every push auto-deploys via `.github/workflows/pages.yml`.
3. **Verify no reply activity.** Open Kate's HubSpot record ([id 266995962817](https://app.hubspot.com/contacts/49095182/record/0-1/266995962817)) before doing any follow-up work — she may have already replied, changed the ask, or looped in Cynthia/Niki.

Then re-read BACKLOG.md for open items and the "Post-send follow-up" section below for what's live.

---

## What's done (as of ship)

### Deployment
- Repo `github.com/rsharma-oss/mntd-proposal` public · GitHub Pages via Actions
- URL live at https://rsharma-oss.github.io/mntd-proposal/ (verified 200)
- Local git identity set (`rahul@growthautomated.ai` / `Rahul Sharma`)
- PAT bound to macOS Keychain — silent pushes going forward
- `.github/workflows/pages.yml` = `actions/configure-pages@v5` + `actions/deploy-pages@v4`, triggers on push to `main`

### HubSpot stakeholder sync
| Contact | Action | HubSpot ID |
|---|---|---|
| **Kate Rothschild** (GM · Emerging Brands) | Created | [266995962817](https://app.hubspot.com/contacts/49095182/record/0-1/266995962817) |
| **Cynthia Leo** (CMO · ex-Nike) | Created | [267007157215](https://app.hubspot.com/contacts/49095182/record/0-1/267007157215) |
| **Raffael Sarracini** (VP eCommerce · Knix + MNTD) | Updated (title + company; NMM email left as-is) | [86019110882](https://app.hubspot.com/contacts/49095182/record/0-1/86019110882) |
| **Niki Tapscott** (Brand President) | Updated (CCO → Brand President) | [127089683436](https://app.hubspot.com/contacts/49095182/record/0-1/127089683436) |

### Delivery
- Intro email **sent from inside HubSpot** to Kate on 2026-07-15 · auto-logged to her contact timeline · thread will reply-track natively
- Subject line: *MNTD · what I saw as a customer*
- Body: P&P shared context · 4-touchpoint customer story · live URL · guided entry points (Sections 05 + 06) · 30-min co-working ask
- Gmail draft (`r-828445312429453265`) can be deleted or kept as backup

### Structure
- 14 sections + separate `scorecard.html` page (all cross-linked)
- Two-row sticky topbar · MNTD mark left · GA logo right · scrollable nav (14 anchors + Scorecard external link)
- Light/dark theme toggle · persists via `localStorage['mntd_theme']` · WBM palette
- Lightbox system for all `.expandable` images (native `<details>` accordions for observations)
- Anchor scroll-offset (140px) so headers land below the sticky nav
- Deep-linked accordions via `#ms3`, `#ms4`, `#pp1–11`, `#ds1–7`, `#is1–4` — JS handler auto-opens on hash

### Content
- Hero with real Pints & Periods Instagram photo · stakeholder map (Kate/Raff/Niki/Cynthia + 2 TBD)
- Value-proposition fraction diagram in Section 08 · MNTD flagged as leading with "Why Buy Now" · new/returning campaign note
- Interactive pre-purchase flow chart (Section 05) · 7 stages · 13 nodes · emails and SMS open in lightbox · deep-links to `#ms3`/`#ms4`
- Interactive post-purchase flow chart (Section 06) · 6 stages · 15 nodes · `data-seq` chronological numbering · MNTD + FleetOptics + Web + Physical lanes
- Full fulfilment email timeline · 9 emails rendered as PNG screenshots, all clickable
- 5 welcome/campaign email screenshots (Jun 21 – Jul 7) with lightbox
- Full unboxing gallery (8 photos)
- Section 04 (Desktop) evidence panel · 4 dscart PNGs telling the coupon-conflict story
- Section 11 Team · Rahul + Raff (NMM shared-origin) · Founder card has GA-blue border · 2 client references (Jeff/NMM Trustpilot + Brett/WBM)
- 16 tool cards with real vendor logos (Shopify Files MCP + Google favicons) · Klaviyo Master Silver + Partner badges · Loop + Wonderment consolidated

### Copy passes done
- Full Knix-culture QA sweep (IS-1/IS-2/IS-3/IS-4 · PP-3 · Card 5 hedged with DTC benchmarks · IS-4 as testable hypothesis)
- False claim fixed ("You don't pay for a licence stack" → licence fees stay on client side)
- Legal rate-card bullet removed from Section 14
- Section 08 Task Husky closing line removed
- IS-4 "Kate + Niki conversation" line removed
- Numbers verified: 5 marketing emails · 9 transactional emails · 2 SMS threads · 3× same code repeated · 7/14 DMARC fails · 6 gap cards · 5 Commercial cards · 3 Segmentation lanes · 5 Engagement pillars · 16 Tools & Stack items · 4 Legal timeline steps

---

## Post-send follow-up · what to watch

| Signal | Where | If it fires |
|---|---|---|
| Kate opens the URL | HubSpot contact timeline (if tracking pixel was on) or GA analytics if instrumented | Wait 24h before nudge |
| Kate replies | HubSpot thread (auto-logged since sent from HubSpot) | Respond within 4 business hours |
| Kate forwards to Niki/Cynthia | Watch for their contact records showing activity | Prep bespoke follow-ups (drafts already scoped) |
| No response after 5 business days | — | One-nudge rule: one short reference to Section 06 as a hook, then let it breathe |
| Raff surfaces first | Likely — we have history via NMM | Route through him; he's the technical validator |

Cynthia and Niki intros are **queued but not sent** — waiting on Kate's signal before opening more fronts.

---

## Open placeholders · still not blocking

Everything below is intentionally left as a placeholder. Ship-blocking = 0. Nice-to-have when the artefact arrives.

| Placeholder | Where | What to drop in |
|---|---|---|
| Checkout coupon-rejected screenshot | Section 06 · evidence card 2 | The 4:48 PM Shop Pay page showing `WELCOMEMNTD1557TPTGFM couldn't be used` — needs re-forward from Downloads. Save as `assets/shop2-checkout-coupon-rejected.png`. |
| Side-cart busy screenshot | Section 06 · evidence card 3 | A frame of the wearmntd.ca cart drawer with upsells + free-shipping + GWP + discount status all firing at once. |
| Repeat-visit receipt | Section 06 · evidence card 4 | Order confirmation from the second desktop-shop session. |
| Klaviyo post-purchase marketing flow | Section 06 · evidence card 5 | Marketing re-engagement flow export. |
| AEO 9-page deck | Section 13 · Proposal appendix | Only needed if Track A goes live. |

Drop any of these into `assets/`, commit, push — Actions auto-deploys within ~90 seconds.

---

## Related sessions / prior work

- **WBM Technologies proposal** (`~/wbm-ai-dashboard/`) — same template lineage · Brett Bailey testimonial in Section 11 comes from this engagement
- **Hockeystickman.com proposal** (`~/hockeystickman-ai-visibility/`) — original template for the "founder-to-founder mystery-shop" format
- **Growth Automated pitch toolkit** (`~/growth-automated-pitch-toolkit/`) — shared BACKLOG.md tracks WCAG + template polish work
- **This project's template extraction** — see `TEMPLATE-BUILD.md` for the full work list to make MNTD reusable for brand #2

---

## Voice + tone reference

Follows the "Growth Automated voice" memory: founder-to-founder · first-person · concrete detail over abstract claim · one number per sentence maximum · never "leverage" or "synergy" · em-dash for pivots · avoids consulting-speak. See `PLAYBOOK.md` for the fuller voice spec.

---

## What I'd tell the next session

- **Kate is the primary recipient and the email is sent.** Do not send a follow-up before checking HubSpot for reply activity.
- **The evidence-first structure is the whole point.** Every Section 07 (Gaps) claim ties back to a specific mystery-shop observation. Never add a "gap" without evidence upstream.
- **Section numbers drift when sections are added.** Every insert has cost — 8–10 cross-refs elsewhere. Grep after every insert.
- **Niki/Cynthia are audience but should never be addressed directly** unless Kate loops them in. Joanna is out entirely.
- **The Klaviyo Master Silver badge in Section 12 is real proof** — don't move it into a footer, keep it card-adjacent.
- **The Ted Baker anecdote in PP-11 is Rahul's real voice** — don't sanitise it.
- **Loop bought Wonderment** (consolidated to one card in Section 12). Don't split them back apart.
- **Push = deploy.** Every commit to `main` auto-triggers the Actions workflow. Watch `github.com/rsharma-oss/mntd-proposal/actions` after any push.
- **The PAT is in Keychain.** Rahul was reminded to revoke the plain-text one from chat and issue a fresh one. If pushes fail with 401, that's likely why — re-add via `git credential approve` piped input.
- If pricing needs to be reintroduced, `grep '\*\.\*'` finds all 4 spots that currently read "Pricing TBD."
