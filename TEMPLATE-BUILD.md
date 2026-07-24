# TEMPLATE-BUILD · Extracting MNTD into a reusable pitch tool

**Goal:** Turn the shipped MNTD proposal into a reusable template so brand #2 (retail or DTC, US$5M – US$100M, Shopify-native) can be scaffolded in ≤1 day of writing after Phase 1 discovery.

**Total effort estimate:** ~2 days of focused work · one-time cost that amortises across every future proposal.

**Success test:** Brand #2 proposal shipped in ≤1 day of writing time (down from ~1 week for MNTD).

For the theoretical framework — the *how* and *why* — see `PLAYBOOK.md`. This file is the concrete work-required list.

---

## Current state vs. target state

| Layer | Current (MNTD) | Target (Template) |
|---|---|---|
| **HTML shell** | Baked with MNTD-specific copy | `template-index.html` with `{{TOKEN}}` placeholders |
| **Scorecard** | Baked with MNTD-specific numbers | `template-scorecard.html` with `{{TOKEN}}` placeholders |
| **CSS palette** | GA Blue / Green hardcoded | `:root` variable block editable in one place |
| **Partner logos** | Duplicated per proposal (`assets/partners/`) | Shared `~/growth-automated-pitch-toolkit/partner-logos/` |
| **Legal timeline** | 4-step SVG per proposal | Shared toolkit copy |
| **Email .eml → .png pipeline** | Ad-hoc Python in scratchpad | `render-emails.py` in toolkit |
| **Deploy workflow** | Per-repo `.github/workflows/pages.yml` | Templated with `{{BRAND_SLUG}}` |
| **Build script** | Manual copy-paste-edit | `build-proposal.py --brand <slug> --config brand.yaml` |
| **Voice + brand memory** | Two memory files (`growth-automated-voice.md`, `growth-automated-brand.md`) | Same — already reusable |

---

## Phase A · Toolkit repo scaffolding · ~2 hours

**Deliverable:** `~/growth-automated-pitch-toolkit/` exists with a documented structure.

- [ ] Create `~/growth-automated-pitch-toolkit/` directory
- [ ] `git init` · initial commit · push to `github.com/rsharma-oss/growth-automated-pitch-toolkit` (private)
- [ ] Directory layout:
  ```
  growth-automated-pitch-toolkit/
  ├── README.md                       what this toolkit does + how to use it
  ├── templates/
  │   ├── template-index.html         14-section proposal skeleton
  │   ├── template-scorecard.html     9-dimension audit skeleton
  │   ├── template-README.md          per-brand README stub
  │   ├── template-HANDOFF.md         per-brand handoff stub
  │   └── template-BACKLOG.md         per-brand backlog stub
  ├── partner-logos/                  16 vendor logos from MNTD + growth room for more
  ├── scripts/
  │   ├── build-proposal.py           CLI: scaffolds a new brand from a config
  │   └── render-emails.py            .eml → .png pipeline via Chrome headless
  ├── configs/
  │   └── brand.example.yaml          all tokens documented with examples
  ├── legal/                          shared NDA/MSA/SOW/Insurance references (Drive IDs only)
  └── BACKLOG.md                      cross-proposal template polish
  ```

---

## Phase B · Extract `template-index.html` · ~4 hours

**Deliverable:** `templates/template-index.html` renders as an empty proposal shell when opened, ready for `{{TOKEN}}` replacement.

The largest single task. Start from `index.html` (current MNTD) and identify every string that varies by brand. Replace with a `{{TOKEN}}` marker.

**Token catalog to build** (documented in `configs/brand.example.yaml`):

### Brand identity
- `{{BRAND_NAME}}` — e.g. "MNTD"
- `{{BRAND_TAGLINE}}` — e.g. "menswear from Knix"
- `{{BRAND_URL}}` — e.g. "wearmntd.ca"
- `{{BRAND_LOGO_PATH}}` — e.g. "assets/mntd-logo-black.svg"
- `{{BRAND_PALETTE_ACCENT}}` — e.g. "#000000" for MNTD, could be pink for a lingerie brand

### Stakeholders (Section 01)
- `{{STAKEHOLDER_PRIMARY_NAME}}` — Kate Rothschild
- `{{STAKEHOLDER_PRIMARY_ROLE}}` — GM · Emerging Brands
- `{{STAKEHOLDER_2/3/4_NAME/ROLE}}` — for the map cards
- `{{HERO_QUOTE}}` — e.g. "We met briefly at Pints & Periods…"
- `{{HERO_IMAGE_PATH}}` — e.g. "assets/hero-ig.png"

### In-store / Mobile / Desktop (Sections 02–04)
- `{{HAS_RETAIL}}` — boolean; if false, Section 02 is stripped
- `{{IS_ITEMS[]}}` · array of `{id, title, body, evidence_image}` for accordion observations
- `{{MS_ITEMS[]}}` · array of `{id, title, body, evidence_image}`
- `{{DS_ITEMS[]}}` · array of `{id, title, body, evidence_image}`

### Flow charts (Sections 05, 06)
- `{{PRE_PURCHASE_LANES[]}}` — 4 lanes (Physical / Email-SMS / Mobile / Desktop) with `nodes[]`
- `{{POST_PURCHASE_LANES[]}}` — 4 lanes (MNTD / Carrier / Web / Physical) with `nodes[]` + `data-seq`
- `{{EMAIL_TIMELINE[]}}` — array of `{seq, sender, time, subject, image_path}`

### Gaps + strategy (Sections 07, 08)
- `{{GAP_CARDS[]}}` — 6 cards with `{tier, title, body}`
- `{{BIG_FINDING}}` — the callout string (e.g. "SMS opens 20% vs Email 15%")
- `{{VALUE_PROP_LEADS_WITH}}` — which of {Brand, RTB, Offer, Why Now} is highlighted

### Segmentation + engagement (Sections 09, 10)
- `{{SEGMENTATION_LANES[]}}` — 2 or 3 lanes depending on parent Group presence
- `{{ENGAGEMENT_PILLARS[]}}` — usually 5
- `{{TIMELINE_LANES[]}}` — 3 lanes (Stop the Leak · Build · Compound)
- `{{INVESTMENT_AMOUNT}}` — retainer number

### Team + references (Section 11)
- `{{TEAM_MEMBERS[]}}` — usually 2, one is always Rahul
- `{{CLIENT_REFERENCES[]}}` — 2, with `{name, role, company, quote, url}`
- `{{SHARED_ORIGIN_STORY}}` — optional; skip if cold intro

### Tools (Section 12)
- `{{PARTNER_CARDS[]}}` — usually 14–18 from a canonical list, with per-brand badges

### Proposal + legal (Sections 13, 14)
- `{{PROPOSAL_TRACKS[]}}` — usually 3 MRR tracks
- `{{LEGAL_TIMELINE_STEPS[]}}` — 4 fixed steps
- `{{PRICING_DISPLAY_MODE}}` — `hidden` (default) or `visible`

**Sub-tasks:**
- [ ] Do a systematic pass through `index.html` and replace each brand-specific string
- [ ] Extract inline SVG (MNTD wordmark) into an asset reference
- [ ] Wrap Section 02 in an `{% if HAS_RETAIL %}` block (Jinja2 or similar)
- [ ] Wrap Section 09 Lane C in an `{% if PARENT_GROUP %}` block
- [ ] Verify the template still lints/renders when opened raw (tokens visible but structure intact)

---

## Phase C · Extract `template-scorecard.html` · ~1 hour

**Deliverable:** `templates/template-scorecard.html` ready for `{{TOKEN}}` replacement.

- [ ] Copy `scorecard.html` → `templates/template-scorecard.html`
- [ ] Replace `{{OVERALL_SCORE}}` (e.g. 34)
- [ ] Replace `{{DIMENSION_SCORES[]}}` — array of 9 with `{name, score, weight, evidence}`
- [ ] Replace `{{SUPPLEMENTARY_FINDING}}` — the "Post-Purchase Journey" callout for MNTD
- [ ] Verify localStorage theme key uses `{{BRAND_SLUG}}_theme` not `mntd_theme`

---

## Phase D · Extract shared assets · ~1 hour

**Deliverable:** `partner-logos/` and reusable asset packs in the toolkit.

- [ ] Copy `assets/partners/*` → `~/growth-automated-pitch-toolkit/partner-logos/`
- [ ] Copy `assets/ga-logo-color.svg`, `assets/ga-logo-white.svg`, `assets/ga-favicon.png` → toolkit root `brand/`
- [ ] Create a `partner-logos/README.md` mapping each logo file to its vendor + source (Shopify Files / vendor site / Google favicon)
- [ ] Symlink or copy-in during `build-proposal.py` execution

---

## Phase E · Extract email pipeline · ~2 hours

**Deliverable:** `scripts/render-emails.py` — takes a directory of `.eml` files, produces PNGs at correct dimensions.

The MNTD execution had this pipeline embedded in scratchpad Python. Extract it.

- [ ] Locate the Chrome-headless invocation used during MNTD build (search scratchpad)
- [ ] Wrap in a CLI: `python render-emails.py --input assets/emails/ --output assets/`
- [ ] Handle both text/html and text/plain bodies
- [ ] Auto-crop to email dimensions (Chrome headless `--window-size` + `--hide-scrollbars`)
- [ ] Optional: batch rename to `email-01-*.png`, `email-02-*.png`… by mtime
- [ ] Document usage in `scripts/README.md`

---

## Phase F · Build the scaffolding CLI · ~4 hours

**Deliverable:** `scripts/build-proposal.py --brand <slug> --config brand.yaml` produces a fully scaffolded `~/<brand>-proposal/` directory ready to edit.

- [ ] CLI parsing (argparse): `--brand`, `--config`, `--output-dir` (default `~/<brand>-proposal/`)
- [ ] YAML config parser (PyYAML)
- [ ] Jinja2 template rendering: `template-index.html` + config → `<output>/index.html`
- [ ] Same for scorecard, README, HANDOFF, BACKLOG
- [ ] Copy `partner-logos/` → `<output>/assets/partners/`
- [ ] Copy GA brand assets → `<output>/assets/`
- [ ] Write `.gitignore` (`.DS_Store`)
- [ ] Write `.github/workflows/pages.yml` with `{{BRAND_SLUG}}` substituted
- [ ] Optional Phase 2: `git init` + first commit + remote setup

**Acceptance test:**
```bash
python build-proposal.py --brand testco --config configs/testco.yaml
open ~/testco-proposal/index.html   # renders with test data · no {{TOKEN}} leaks
```

---

## Phase G · Document the token catalog · ~2 hours

**Deliverable:** `configs/brand.example.yaml` is fully documented and copy-paste-ready.

- [ ] Every token from Phase B listed with:
  - Example value
  - Type (string / boolean / array-of-object)
  - Required vs. optional
  - What section it appears in
  - Cross-references to `PLAYBOOK.md`
- [ ] Include a "minimum viable brand" example — smallest config that still produces a valid proposal
- [ ] Include a "full-featured brand" example (like MNTD would look through this system)

---

## Phase H · Validate on brand #2 · ~1 day

**Deliverable:** A second real proposal shipped using only the toolkit.

- [ ] Pick brand #2 (likely candidate: a Knix-adjacent brand or a wholly separate one from Rahul's pipeline)
- [ ] Do Phase 1 Discovery from `PLAYBOOK.md` (the 4-touchpoint customer journey)
- [ ] Write `configs/<brand>.yaml`
- [ ] Run `build-proposal.py`
- [ ] Fill in per-brand copy in the scaffolded file
- [ ] Deploy via the same GitHub Actions pattern
- [ ] Time the total effort · target ≤1 day from Discovery completion to click-ready link

**Success metrics** (from `PLAYBOOK.md`):
- Time to first draft ≤ 8 hours ✓
- Time to click-ready link ≤ 1 day ✓
- If either overruns, iterate on the template — the MNTD execution took ~1 week; the amortisation only pays off if brand #2 is dramatically faster

---

## Ordering rationale

The phases are ordered so that partial completion still yields value:
- **After Phase A alone:** a documented toolkit repo exists — future work has a home
- **After Phases A-D:** the visual template can be manually cloned (still faster than starting from scratch)
- **After Phases A-F:** true one-command scaffolding is possible
- **After Phase H:** the template is validated and the tool is genuinely reusable

Do NOT skip Phase H. Templates that haven't been used twice are theoretical.

---

## What NOT to templatise

- **The Pints & Periods opener.** Only works because Rahul was actually there. Every brand needs its own "how we met" story.
- **The Ted Baker anecdote in PP-11.** Rahul's personal voice. Would be uncanny valley if generated.
- **Specific numbers** (34/100 audit, $158.42 order, 40-hour delivery). Always earn them for the new brand.
- **The Klaviyo Master Silver badge.** GA's actual tier — not a pattern anyone else can copy.
- **Case-study references** (Jeff/NMM, Brett/WBM). Real relationships. Rotate based on what's relevant to the target brand.
- **Section 11 team story.** Rahul + one collaborator per engagement — the collaborator changes.

The template gives you the *structure*. The *evidence* still comes from real work.

---

## Estimated timeline

| Phase | Effort | Cumulative |
|---|---|---|
| A · Toolkit scaffolding | 2h | 2h |
| B · template-index.html | 4h | 6h |
| C · template-scorecard.html | 1h | 7h |
| D · Shared assets | 1h | 8h |
| E · Email pipeline | 2h | 10h |
| F · Build CLI | 4h | 14h |
| G · Token catalog docs | 2h | 16h |
| H · Brand #2 validation | 8h | 24h |

**Total:** ~3 focused workdays. Realistically over ~1 calendar week alongside other work.

**ROI break-even:** After brand #2 ships in ≤1 day of writing (vs. MNTD's ~1 week), the toolkit has paid for itself once. Every subsequent brand is pure profit on time.

---

## Owner + next action

**Owner:** Rahul.
**Next action:** Wait for Kate's response on the MNTD proposal. If she engages, execution takes priority. If quiet after a week, use the downtime to knock out Phase A (2h · low context switch cost) as a starting foothold.
