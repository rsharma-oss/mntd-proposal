#!/usr/bin/env python3
"""Generate per-recipient microsite variants from the shipped Kate index.html."""
import os
import re

REPO = '/Users/rahulsharma/mntd-proposal'
SRC = f'{REPO}/index.html'

with open(SRC) as f:
    kate = f.read()

# --- The block we replace per recipient (eyebrow + headline + full hero body).
# Kate's block (exact, from the shipped file):
KATE_HERO_BLOCK = '''      <div class="hero-eyebrow">01 · The Story · Pints &amp; Periods</div>
      <h1 class="hero-headline">Kate — we met briefly at <em>Pints &amp; Periods</em>, and I have a confession to make.</h1>
    </div>
    <div class="hero-top-main">
  <div class="hero-body">
    <p>I've actually been using MNTD since the end of January — I got your boxers and socks from Knix — but I was always too skeptical to treat myself to a $50 T-shirt. That changed at the event, when I finally picked up a black Tee (and some more boxers and socks — thank you!).</p>
    <p><strong>Long story short: the claim holds. It is the best tee.</strong> I love how it looks at the gym. In fact, ten days ago I literally stripped naked in my laundry room just so I could wash it and immediately wear it again. A bit TMI, maybe — but that's how hooked I am.</p>
    <p>Since then, three more things have happened. I want you to know I'm writing you as a customer first, not a consultant. <strong>I brought my 12-year-old son to Knix Eaton Centre for a daddy-son day.</strong> <strong>I opened wearmntd.ca on my phone to buy more.</strong> And <strong>I placed a real order.</strong> Three customer stories, same protagonist — me — trying to give MNTD my money.</p>
    <p>I'd love to hop into a co-working session with you to walk you through what I saw across all three, and pick the quick wins together. Let me know if you're open to it.</p>
  </div>'''

def hero(eyebrow, headline, body_paragraphs):
    body = '\n    '.join(body_paragraphs)
    return f'''      <div class="hero-eyebrow">{eyebrow}</div>
      <h1 class="hero-headline">{headline}</h1>
    </div>
    <div class="hero-top-main">
  <div class="hero-body">
    {body}
  </div>'''

RAFF_HERO = hero(
    '01 · The Story · From the NMM stack forward',
    'Raff — you inherited the stack I designed at <em>New Metric Media</em>. This one comes at MNTD from the other side of the counter.',
    [
        "<p>We haven't worked directly. But you built on the operating stack I laid down at New Metric Media — Jeff hired you into the role, and the org chart you inherited was mine. I've watched the Knix Group multi-brand build from the outside. It's sharp.</p>",
        "<p>This proposal lands on Kate's desk for MNTD. I'm not writing you as the pitchee — I'm writing you as the technical validator. <strong>The bulk of the eComm story lives in Section 06 (Post-Purchase).</strong> Nine transactional emails, FleetOptics timing gaps, a 40-hour Toronto-to-Toronto ship. If the framing is fair, great. If anything lands wrong technically, tell me before it goes further.</p>",
        "<p>The three customer touchpoints — Eaton Centre visit, mobile shop, desktop shop — are Sections 02, 03, and 04. Section 05 maps the pre-purchase arc, Section 06 maps the post-purchase arc. Everything ties back to a screenshot or a real email.</p>",
        "<p>If Kate brings me in for the co-working session I proposed, I want you in the room.</p>",
    ],
)

JOANNA_HERO = hero(
    '01 · The Story · Pints &amp; Periods',
    'Joanna — <em>Pints &amp; Periods</em> was your event. Here\'s what happened when I walked in as a customer and stayed one.',
    [
        "<p>You built Knix from scratch. MNTD is what happens when a brand family grows a new generation — and the product is genuinely good. I've been using MNTD since end of January (boxers and socks from Knix originally), but was too skeptical to spring for a $50 T-shirt until Pints &amp; Periods pushed me over the edge.</p>",
        "<p><strong>The claim holds. It is the best tee.</strong> Ten days ago I literally stripped naked in my laundry room just so I could wash it and immediately wear it again. TMI — but that's how hooked I am.</p>",
        "<p>Since then, three things have happened. I brought my 12-year-old son to Knix Eaton Centre. I opened wearmntd.ca on my phone. I placed a real desktop order. This site is what I saw across all three — every observation tied to a screenshot or a real fulfillment email.</p>",
        "<p>The primary conversation is with Kate. You'll see her named throughout as the operator sponsor. But your read on the customer experience of the brand family you built matters, and I wanted you to see this before it moves further inside the org.</p>",
    ],
)

NIKI_HERO = hero(
    '01 · The Story · MNTD from the customer side',
    "Niki — you're stepping into a brand family with a real customer under it. Here's what I found when that customer was me.",
    [
        "<p>You've just moved from Chief Commercial Officer to Brand President, and the Knix Group you're inheriting includes MNTD — the emerging brand Kate stewards. I wanted you to see this before it moves through the org.</p>",
        "<p>I've been using MNTD since end of January — a customer, not a consultant. In the last two weeks I've added three touchpoints: Knix Eaton Centre with my 12-year-old son, wearmntd.ca on my phone, and a real desktop order. Every observation across those three ties back to a screenshot or a real fulfillment email in the sections below.</p>",
        "<p><strong>The claim holds. It is the best tee.</strong> MNTD has real product-market fit. What this proposal argues is that the customer experience around it hasn't caught up with the product yet — and the gap is fixable in weeks, not quarters.</p>",
        "<p>The primary conversation is with Kate. You'll see her named throughout as the operator sponsor for the engagement. This version is for your visibility — no ask attached.</p>",
    ],
)

def build(slug, name, hero_block, scrub_raff_finalist=False):
    html = kate

    # 1) Replace the hero block
    if KATE_HERO_BLOCK not in html:
        raise SystemExit(f'FATAL: Kate hero block not found — file drifted, script needs update')
    html = html.replace(KATE_HERO_BLOCK, hero_block, 1)

    # 2) <title> tag
    html = html.replace(
        '<title>MNTD × Growth Automated · Proposal for Kate Rothschild</title>',
        f'<title>MNTD × Growth Automated · Proposal for {name}</title>',
        1,
    )

    # 3) tb-sub
    html = html.replace(
        '<div class="tb-sub">Proposal · Kate Rothschild</div>',
        f'<div class="tb-sub">Proposal · {name}</div>',
        1,
    )

    # 4) Footer "Prepared for"
    html = html.replace(
        '<div><strong>Prepared for Kate Rothschild</strong> · MNTD · Toronto ON · July 2026</div>',
        f'<div><strong>Prepared for {name}</strong> · MNTD · Toronto ON · July 2026</div>',
        1,
    )

    # 5) Raff-only: scrub the "Kate was one of the finalists" line
    if scrub_raff_finalist:
        html = html.replace(
            'New Metric Media then hired Raff into that role — a role Kate was one of the finalists for. Raff built on the stack I laid down.',
            'New Metric Media then hired Raff into that role. Raff built on the stack I laid down.',
            1,
        )

    # 6) Rewrite asset + scorecard paths for subdir (../ prefix)
    html = re.sub(r'src="assets/', 'src="../assets/', html)
    html = re.sub(r'href="assets/', 'href="../assets/', html)
    html = re.sub(r'href="scorecard\.html"', 'href="../scorecard.html"', html)

    # 7) Write to subdir
    out_dir = f'{REPO}/{slug}'
    os.makedirs(out_dir, exist_ok=True)
    with open(f'{out_dir}/index.html', 'w') as f:
        f.write(html)
    print(f'  {slug}/index.html · {len(html):,} bytes')

print('Building recipient variants:')
build('raff', 'Raffael Sarracini', RAFF_HERO, scrub_raff_finalist=True)
build('joanna', 'Joanna Griffiths', JOANNA_HERO)
build('niki', 'Niki Tapscott', NIKI_HERO)
print('Done.')
