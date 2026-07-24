# PLAYBOOK · Scaling this proposal format to other mid-market retail + DTC brands

The MNTD proposal is a template. This document is how to re-use it for the next mid-market brand — retail or DTC — without re-inventing structure, voice, or tech.

> **This file = the theory.** For the concrete extraction work list (what to copy, tokenise, and move into a shared toolkit repo), see `TEMPLATE-BUILD.md`. That file estimates ~2 focused workdays to convert MNTD into a genuinely reusable template.

Target profile: **US$5M – US$100M in annual revenue · Shopify-native · brand-led (not pure performance) · founder or brand-president level buyer.**

Not the right template for: enterprise (>$500M · needs procurement-heavy proposals), pre-revenue (needs a different discovery arc), pure-B2B (this template assumes DTC lifecycle).

---

## The framework in one line

**Live the customer journey yourself → document friction with evidence → connect gaps to strategy → propose a working engagement, not a deck.**

Everything below is scaffolding for that thesis.

---

## Phase 1 · Discovery (before writing a single line)

Every strong proposal starts with 4 customer touchpoints the founder has personally executed:

| Touchpoint | What to capture | Why |
|---|---|---|
| **1. Discovery / meet moment** (event, referral, DM) | Photo, quote, or vivid detail from the first exposure | The hero opener. Grounds the proposal in shared context. |
| **2. Mobile mystery shop** | Subscribe (email + SMS) · browse · build cart · attempt purchase · screenshot key friction | 60–75% of DTC traffic is mobile. Test the primary path. |
| **3. Desktop / follow-up shop** | Return visit · complete a real order · screenshot checkout, order confirmation, receipt | The paid moment is the pivot. Real skin in the game beats hypotheticals. |
| **4. Post-purchase** | Every fulfilment email, tracking SMS, unboxing photo, first-wear moment | Post-purchase is highest engagement and lowest-cost lift for most brands. |

Retail add-on: **in-store visit** (physical merchandising, staff pitch, checkout flow, vibe). If the brand has retail presence, include a Section 02 for in-store observations.

**Evidence hygiene rule:** every observation card in the final proposal must trace back to a screenshot, email, SMS, or physical artefact from Phase 1. No claims without evidence.

---

## Phase 2 · Structure template (14 sections + scorecard)

Copy this outline. Rename sections as brand context demands, but keep the numbering pattern.

| # | Section | What it contains | Length |
|---|---|---|---|
| **01** | Story | Personal opener · hero image (event photo / IG frame) · stakeholder map (primary + supporting audience + TBD seats) | 3–4 paragraphs + stakeholder cards |
| **02** | In-Store (if retail) | 4–6 accordion observations (IS-1…) · retail-only. Skip for pure-DTC. | ~4 items |
| **03** | Shop 1 · Mobile | 5–7 mobile mystery-shop observations (MS-1…) | ~5 items |
| **04** | Shop 2 · Desktop | 5–8 desktop observations (DS-1…) including any coupon / cart friction | ~7 items |
| **05** | Pre-Purchase Journey Map | Horizontal flow chart · 6–8 stages · lanes for Physical / Email-SMS / Mobile / Desktop · pivots to purchase | 1 visual |
| **06** | Post-Purchase | Thesis callout ("why post-purchase matters most") · flow chart · 8–12 observations (PP-1…) · unboxing gallery · fulfilment-email timeline | Deepest section |
| **07** | The Gaps | 6 weighted gap cards (Tier 1/2/3) · one big-finding callout · evidence panel with real emails/SMS | 6 cards + evidence |
| **08** | Commercial Strategy | Value-proposition fraction diagram (Brand · RTB · Offer · Why Now) · 4–6 strategic cards · optional media reference (video / case study) | Diagram + 5 cards |
| **09** | Segmentation | 3 lanes: table stakes (1st vs Nth purchase) · differentiated angle (brand-specific) · parent-brand/group-wide (if applicable) · ad-orchestration wiring | 3 lanes |
| **10** | Engagement | 5 pillars · 90-day timeline (3 lanes: Stop the Leak · Build · Compound) · investment card | Pillars + timeline |
| **11** | Team | 2 people max · include shared-origin story if relevant · 2 client references with real names and roles | 2 team cards + 2 refs |
| **12** | Tools & Stack | 14–18 partner cards with real logos · badge (Partner / New / Governance) · positioning quotes from each vendor's own website | Grid |
| **13** | Proposal | Retainer scope + Phase 2 MRR expansion tracks (AEO / SEO / Community) | Big price card + 3 MRR cards |
| **14** | Legal | 4-step timeline (NDA → MSA → SOW → Insurance) · standard across all engagements | Timeline |
| **—** | scorecard.html | Weighted 9-dimension audit as a separate page | ~1 page |

**When to skip a section:**
- Skip **02** if the brand has no retail presence.
- Skip **11** shared-origin if it's a cold intro (keep just the bio + refs).
- Section **09 Lane C** (parent-brand) only applies when there's a parent Group.
- Section **08** value-prop diagram is fine to keep even when the brand isn't over-indexed on any one lever — just don't flag one as "leading."

---

## Phase 3 · Assets checklist

For every proposal, gather these before writing:

- [ ] Brand logo (SVG preferred · vendor site or Shopify Files MCP)
- [ ] 1 hero image (event photo, founder shot, IG frame — 4:5 portrait works best)
- [ ] 4–6 in-store photos (if retail)
- [ ] 3–5 mobile mystery-shop screenshots (popup, product page, cart, checkout friction)
- [ ] 2–4 desktop screenshots (coupon rejection, side-cart busy, order confirmation)
- [ ] All welcome + campaign emails received (as .eml → render to .png via Chrome headless)
- [ ] All transactional emails post-purchase (order → shipped → delivered)
- [ ] SMS thread screenshots (subscribe + delivery)
- [ ] Unboxing photo set (received → contents → gift/insert if any)
- [ ] Partner vendor logos (Shopify Files MCP has most; Google favicon service for the rest)

**Email screenshot pipeline** (reusable script — see `~/mntd-proposal/` for reference):
```
Python: parse .eml → extract text/html body → wrap in template → Chrome headless screenshot → PNG
```

---

## Phase 4 · Design system

Copy `assets/mntd-logo-black.svg`, `assets/ga-logo-color.svg`, `assets/ga-logo-white.svg`, and the entire CSS block from `index.html` head. Only two things need editing per brand:

**A. Brand palette** — replace GA blue/green with brand accents in the `:root` CSS variable block:
```css
:root{--ga-blue:#XXXXXX;--ga-green:#XXXXXX;--ga-carbon:#XXXXXX;--ga-cloud:#XXXXXX;--critical:#DC2626;--warn:#F59E0B;--good:#10B981}
```

**B. Brand logo swap** — MNTD wordmark in the top-left needs replacing with the target brand's wordmark. Keep the 52×88 rounded-white holder for consistency.

Type stack (Assistant / DM Serif Display / DM Mono) is brand-agnostic — keep it.

---

## Phase 5 · Voice

Match the "Growth Automated voice" memory. Key rules for this template specifically:

- **First-person, always.** "I built a cart" not "we built a cart" or "the customer built."
- **Concrete detail over abstract claim.** "The Klaviyo welcome code silently dropped after three bundle iterations" beats "the cart experience needs work."
- **One number per sentence, max.** Numbers earn their place. Don't stack.
- **Em-dash for pivots, not commas.** *"The claim holds — it is the best tee."*
- **Founder-to-founder tone.** Never explain what a Shopify store is. Assume the reader knows their business.
- **No consulting-speak.** Banned: leverage, synergy, deep-dive, low-hanging fruit, actionable insights, thought leadership, best-in-class (unless the brand actually is).
- **Personal anecdote is a feature, not a bug.** The Ted Baker "have a nice day" label story in PP-11 is more memorable than any framework diagram. Include real moments.

---

## Phase 6 · Repeatability infrastructure

Files worth carrying between proposals (put in `~/growth-automated-pitch-toolkit/`):

- `template-index.html` — stripped MNTD proposal with `{{TOKEN}}` placeholders for brand-specific fields
- `template-scorecard.html` — same but for the scorecard
- `render-emails.py` — the Chrome-headless `.eml → .png` pipeline from this project
- `partner-logos/` — pre-fetched logos for the standard 12–15 partners (Shopify, Klaviyo, Rewind, ReBuy, Loop, Wonderment, Yotpo, Gorgias, Triple Whale, RetentionX, Acceler8 Labs, Reddit, DataForSEO, AI Peekaboo, Task Husky, Domaine)
- `legal/` — the 4 GA legal timeline docs (NDA / MSA / SOW / Insurance) with Drive IDs referenced

New proposal setup should take 60–90 minutes of scaffolding + 4–8 hours of writing (assuming Phase 1 discovery is already done).

---

## Phase 7 · Delivery infrastructure

Same as MNTD:

1. Local `~/{brand}-proposal/` folder · `index.html` + `scorecard.html` + `assets/` + `.github/workflows/pages.yml`
2. GitHub repo at `github.com/rsharma-oss/{brand}-proposal` (public, or private with Pages if the brand asks)
3. GitHub Actions deploy · URL `https://rsharma-oss.github.io/{brand}-proposal/`
4. HubSpot email intro with the URL · CC to `rahul@growthautomated.ai`

Time from "start writing" to "link in HubSpot" for a repeat-brand execution: **~1 day.**

---

## When to break the template

- **Multi-brand parent Groups** (like Knix Group): add Section 09 Lane C for parent-wide value.
- **Brands with a specific channel angle** (like Reddit-first brands): expand Section 13 Track C into more depth.
- **Brands with retail expansion pending**: make Section 02 the highlight; move it before Story if warranted.
- **Brands where the founder is the buyer** (not a GM): make the tone more peer-to-peer; drop the stakeholder map or keep it small.

The template is scaffolding, not scripture. Every section can be adapted, but the *evidence-first, section-numbered, cross-linked* structure should stay.

---

## What NOT to copy

- MNTD's specific numbers (34/100 audit, $158.42 order, 40-hour delivery) — always earn them for the new brand.
- The Pints & Periods reference in the opener — only works because Rahul was actually there.
- The Ted Baker anecdote in PP-11 — Rahul's personal story, not a rubric line.
- The Klaviyo Master Silver badge — that's Growth Automated's tier, not a pattern.

---

## Success metric for the pitch tool itself

- **Time to first draft** ≤ 8 hours for a repeat-brand
- **Time to click-ready link** ≤ 1 day
- **Response rate on cold intro** ≥ 40% (vs ~10% for deck-style pitches)
- **Meeting-book rate on response** ≥ 60%

If any of these drop, revisit the voice, the evidence density, or the personal-anecdote quotient — those are the three levers that make this format work.
