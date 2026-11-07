---
name: spencer-web-style
description: Spencer's house design standard for every website, landing page, web app and UI Spencer builds (UTern, Leed, BallotWatch, Validate, SparkTech and anything new). Load BEFORE designing, styling, redesigning or reviewing any web page, choosing fonts/colors, writing landing-page copy, or running gstack design skills (/design-consultation, /design-html, /design-review, /design-shotgun, /plan-design-review). This standard overrides generic design-skill defaults.
---

# Spencer's Web Style

**Read [`ABOUT.md`](../ABOUT.md) first** (who Spencer is, the products, mascots and why these rules exist).

One standard, every site. A new product should look like it belongs next to UTern and Validate without anyone being told. When a gstack design skill or any other design default disagrees with this file, this file wins. A project's own DESIGN.md wins over this file only where it explicitly says so.

**The feel in one line:** mostly white, near-black ink, one clean sans, huge tight centered headlines, pill buttons, lots of space, almost no words, nothing that looks AI-made. Always a great nav, clear calls to action, a live assistant in the corner, and an in-depth footer linking to real pages.

Spencer judges by one question: *does this look like a polished, mainstream, Apple/Linear-grade product site, or does it look generic and AI-generated?*

---

## 0. Sector research first

Before any **new website** (client site, portfolio site, or greenfield concept), research the sector. Do this before choosing a creative direction, writing a `DESIGN.md`, or building options. Existing sites Spencer already designed do not need a full re-research for small tweaks; they do when the brief is a new site or a sector redesign.

1. **Pick 4–6 leading companies** in that sector whose standing you can verify from real sources (industry rankings, regulators, reputable deal databases, major press). Cite the standing source URL. **Never invent rankings** or "top firm" claims.
2. **Open each company's official site** (and the most relevant product/service page). Record concrete observations on:
   - Hierarchy (what leads the home page and why)
   - Typography
   - Nav structure and labels
   - How they explain services or product
   - Credibility signals (proof, people, data, press; only note what is actually on the page)
   - CTAs (wording, placement, hard vs soft)
3. **Decide what to adopt and what to avoid** for Spencer's project. Write it down (project `research/FINDINGS.md` or the brief). Patterns inform taste; they do not override this file's hard bans.
4. **Never clone.** Do not copy layout systems, unique visual marks, wording, testimonials, metrics, or brand assets. Do not paste a competitor's IA onto our pages. Inform, then design something that still looks like Spencer's standard (white, ink, one sans, no AI tells).
5. **Keep the research bounded.** Four to six firms is enough. Prefer official sites and cited ranking pages over secondary listicles. If standing cannot be verified, say so and pick another firm.
6. **Credentials stay in the research.** Other firms' or companies' rankings and credentials are research inputs only and must never be presented as the client's own credentials. Leave proof or recognition sections out entirely until there is real, attributable proof.

When handing off or reporting a new website, include the firm list with standing and site URLs, the adopt/avoid summary, and the path to the findings file. Confirm no borrowed credentials appear as the client's own, and that proof or recognition sections were left out unless the proof is real and attributable.

## 1. Hard bans (the "AI tells")

Never ship any of these. Check for them before calling anything done.

- **Numbered steps or labels:** no `01 / 02 / 03`, no "Step 1", no numbered section markers, no listed steps. Show a workflow as a flowing diagram instead.
- **Eyebrows / kickers:** no small tag or label above a headline, no "THE PROBLEM" uppercase line, no "New" or "Live now" chip in the hero.
- **Pill tags and badges** as content: categories, features and types are just words, not chips.
- **Lines as separators:** no horizontal rules, `<hr>`, `border-top`/`border-bottom` dividers between sections, list rows, FAQ items or footer columns. Separate with space, size and weight.
- **Boxy layouts:** no equal card grids, no 3-column icon feature grid, no icons in colored circles, no wrapping everything in `rounded + border + padding`. Boxes are a last resort.
- **Arrows or icons inside buttons.** Buttons are words only. No `→`, no chevrons, no arrow chips, on any button or CTA link.
- **Italic accent words** (`<em>` inside headings), serif flourishes, mixed display fonts.
- **Purple / violet / indigo** anywhere, gradients, glows, blobs, radial spotlights, grain, decorative waves.
- **Backgrounds behind logos, favicons or mascots** (see section 9).
- **Emoji** as design or in UI copy.
- **Gimmick motion:** bounce, typing effects, word-by-word reveals, particles, marquees, custom cursors, 3D tilt, magnetic buttons.
- **Features that do nothing for the user.** Every control, card, setting, badge and toggle must change something the user can see and cares about. If removing it would change nothing for them, it does not ship. Internal plumbing (analytics consent, feature flags, sync status, debug state) is never presented as a feature. Before adding any UI, state in one line what the user gets from it; if that line is about us, not them, cut it.
- **Orphaned controls.** When the surface that gave a control its meaning is removed, remove the control and its code in the same change. Removing a popup means removing the setting that only existed because of the popup. Search for what depended on it before calling the removal done.
- **Fake content:** invented stats, testimonials, logos, user counts, placeholder grey bars, generic AI maps or illustrations, "Acme Corp" examples.
- **Em dashes** (`—`) anywhere in copy. Use a comma, colon, period or middle dot `·`.
- **Repetition:** a statement, feature, or the *theme* of a statement must never appear twice on a page, even reworded. If two sections make the same point, cut one.

## 2. Color

Mostly white. Color carries meaning, never decoration.

```css
:root {
  /* ground: pick ONE per project. Pure white is the default; a barely-warm off-white is allowed when the brand wants it. */
  --bg: #FFFFFF;            /* or #F7F6F3 */
  --surface: #FFFFFF;
  --surface-dim: #F4F4F2;   /* quiet fills: inputs, hover, segmented controls */
  --card-edge: #ECEEF1;     /* a raised surface's own outline only, never a divider */

  --ink: #1A1A18;           /* text + primary buttons. never pure #000 */
  --ink-2: #5A574F;         /* secondary text */
  --ink-3: #6D6B63;         /* lightest grey allowed to carry text (AA 4.5:1) */

  --accent: var(--ink);     /* default: black IS the accent */
  --accent-on: #FFFFFF;

  --ok: #1F7A4D; --warn: #B45309; --bad: #B4372F;   /* status only */
}
```

- **Accent:** default to none (ink). A brand may get **one** accent hue (e.g. UTern blue `#2563EB`, SparkTech gold `#b8860b`), used only for links, the primary button, focus and state. Never two accents.
- **White is the standard background, never black** (Spencer, 2026-11-07: "keep the standard background white not black"). Every page, app screen, mockup and preview renders on white by default, even when the viewer's device is in dark mode: do not switch to dark from `prefers-color-scheme` alone.
- **Dark:** marketing pages stay light. One dark band (footer CTA or a photo hero) is allowed when it clearly helps; use your judgment and keep it to one. Apps and logged-in products still ship a well-designed dark mode (see `spencer-app-style`), same token names under `:root[data-theme="dark"]`, but only when the person picks it in settings.
- **Images bring the color.** Photos, product screens and real content are where color lives.
- All tokens in one theme file. Never hardcode hex in components.

## 3. Typography

One clean sans for everything. Mono only for numbers and data.

- **Default:** Geist (400/500/600/700) + Geist Mono. Satoshi or Instrument Sans are fine as the single face; Inter is acceptable. Self-host or `next/font`, never a system-ui stack.
- No serif, no italics for emphasis. **Emphasize with weight**, not italic, not color.
- **Headlines and statements are Title Case** ("We Build The Things Others Only Talk About", "More Coming"). Buttons, body and labels stay sentence case.
- **Brand and product names spelled exactly**, every time, everywhere (SparkTech, UTern, Leed, BallotWatch, Validate-s). Check meta tags and alt text too.
- Headlines are large and tight:

```css
h1 { font-size: clamp(44px, 7.5vw, 112px); font-weight: 600; line-height: .95; letter-spacing: -0.05em; }
h2 { font-size: clamp(32px, 4.8vw, 72px);  font-weight: 600; line-height: 1;   letter-spacing: -0.04em; }
h3 { font-size: clamp(20px, 2vw, 26px);    font-weight: 600; line-height: 1.2; letter-spacing: -0.02em; }
body { font-size: 17px; line-height: 1.6; color: var(--ink-2); }
.num { font-family: var(--mono); font-variant-numeric: tabular-nums; }
```

- **Minimum 16px** for all body text, fine print, captions, footer links and form text. Only dense app chrome (table meta, timestamps) may go to 13px. When in doubt go bigger; Spencer regularly says things are too small.
- Line length about 70ch max.

## 4. Alignment, shape, space, depth

- **Centered:** the hero, every big statement, and every CTA group. **Left-aligned:** body paragraphs, lists, forms and app content.
- **Buttons are pills** (`border-radius: 999px`), like live UTern. Solid ink (or the one accent) for primary, outlined/ghost pill for secondary. Padding about `14px 26px`, weight 500, words only (no arrows, no icons), a `translateY(-1px)` lift on hover, no shadow at rest. Every button on the site, landing and app, uses the same button component.
- Radius: inputs 12px, cards and media frames 16–24px, sheets/modals 24px, big hero media 28–40px.
- Shadows: soft and rare. `0 1px 2px rgba(20,20,15,.04), 0 12px 32px rgba(20,20,15,.06)`.
- Space is the separator. Section padding `clamp(96px, 12vw, 160px)`. Gaps between items 24–48px. 4px base grid. Never crowded, never touching the bottom edge of a section or viewport.
- Content width 1180px max, gutter `clamp(20px, 5vw, 56px)`. Reading columns 680–760px.
- Icons: Lucide outline, small, only when they carry meaning (never inside buttons).

## 5. Landing page shape

The landing page is **marketing only**: it explains the product and gets people to sign up. A story told top to bottom. Each section earns the next; none repeats another.

1. **Nav** (see 5a).
2. **Hero:** centered. One short Title Case statement (the promise), one supporting line at most, one primary pill CTA (optional secondary pill). Behind it, the brand's **signature background** (see 5d). No tags above it.
3. **Statement sections:** one idea each, alternating text and visual. Short centered H2, one or two short lines, then a visual that explains (section 8). Each section ends in a clear next step.
4. **Proof** only if it is real.
5. **FAQ:** plain question/answer pairs separated by space, no cards, no lines.
6. **Closing CTA band:** one strong statement + the primary pill, centered. The one dark band, if used, usually lives here.
7. **Footer** (see 5b).

Marketing rules:
- Never show signed-in state on the landing page: no "Sign out", no account menu, no app-only features in the nav. Visiting the landing page never feels logged in.
- Audience-specific or deep content gets **its own page** ("For Businesses", "How It Works", "Pricing", "For Schools"), not crammed onto the homepage.
- An app (iOS or web app) never contains a marketing landing page; it opens to sign-in or the product.

### 5a. Nav: always good, always easy

- **Glued to the top** (sticky), 64–72px tall, spanning the full page width. White, or transparent over a photo hero, turning white with a soft blur on scroll.
- Wordmark left (links home, no background behind it). 3–5 plain-word links named for what's there ("How it works", "For businesses", "Pricing"), never clever labels.
- **Top right: "Sign in" (ghost) + "Sign up" (solid pill), side by side**, or the single primary CTA if the product has no accounts.
- Active page shown by ink weight/color, not underlines or boxes. Hover darkens text.
- Mobile: wordmark + primary CTA + a menu button; the menu opens a full-screen white sheet with big tappable links (min 44px) and Sign in / Sign up at the bottom. Closes on link tap and Escape.
- Dropdowns only when there are genuinely many pages; keep them simple lists with a one-line description each.
- Keyboard and screen-reader usable (`<nav>`, `aria-current`, focus ring, `aria-expanded` on the menu button).

### 5b. Footer: always in-depth

Every site gets a full, real footer, not a single copyright line.

- Top: wordmark + one line about the product + the primary pill CTA (or an email signup if that's the conversion).
- Then 3–5 link columns with plain headings, grouped by intent, e.g. **Product** (Features, Pricing, How it works, Changelog), **Company** (About, Careers, Contact, Press), **Resources** (FAQ, Help center, Blog/Guides), **Legal** (Privacy, Terms, Cookies, Security).
- Bottom: © year + company name, every real social account linked (small outline icons), and contact (link to the contact page or "Book a call"; don't print raw emails unless the project says to).
- Columns are separated by space, never lines. Generous padding top and bottom. Same tokens as the page; may sit on `--surface-dim` or be the one dark band.
- **Every footer link goes to a real, built page.** Never `#`, never a dead link. If a linked page doesn't exist, create it in the same theme: same nav, same footer, same type and spacing, real content (legal pages get real reasonable policy text marked for review; About/Contact get honest copy, no invented team or stats). If a page truly shouldn't exist yet, drop the link instead.
- Mobile: columns stack into a 2-column grid, then 1; links stay 44px tappable.

### 5c. Calls to action: always

- Every page has a primary CTA: in the nav, in the hero, and in a closing CTA band before the footer. Every interior page (legal excepted) ends with a CTA too.
- One primary action per screen, worded as the outcome in 2–4 words ("Find my internship", "Start validating", "Book a call"). Same wording for the same action everywhere on the site, and it must not change after the page loads.
- Secondary actions are ghost pills or plain text links (no arrows), never a second solid button competing with the first.
- CTAs link to something that works (sign-up, booking, checkout, contact form). No dead buttons.

### 5d. Signature hero background

Each brand owns one recognizable hero image or video (UTern's mountain, BallotWatch's Capitol, Leed's opening doors, oasisVRX's venue footage). It sits behind the hero (and optionally the closing CTA band), with a soft scrim so centered white or ink text stays AA-readable. Everything else on the page stays white. Inside the logged-in app, backgrounds stay plain white unless the project says otherwise.

## 5e. Standard screens

Two screens look the same in every product. Build them this way unless the project's DESIGN.md says otherwise.

**Sign in and sign up ("Open Page", 2026-11-07).**
- No card and no box around the form. No Sign in / Sign up tab toggle.
- Centered column, about 380px wide: the mascot face (no background), a Title Case heading ("Welcome Back"), one short line under it.
- "Continue with Google" (and Apple when the product has it) first, as a soft-filled pill. Then "or with email" as plain small text, never between divider lines.
- Each field has a small label above it, a soft fill (`--surface-dim`), no border, 16px radius, at least 52px tall, and a focus ring in the accent.
- One primary pill with words only ("Sign in", "Create account"). Under it, plain text links: "Forgot password?" and "New here? Sign up" or "Have an account? Sign in".

**An opportunity, listing or item ("Facts First", 2026-11-07).** The same layout for every type (internship, part time, new grad, fellowship, research, a product, a place):
- Header: logo, title, the company or owner, then share and close.
- A strip of four facts, always in the same order and place. For a role that is When, Where, Pay and Closes (or Usually opens). A missing fact says "Not listed"; it never disappears.
- One line on what it is.
- "About" is open by default and easy to read: short paragraphs, bullet lists under plain headings (What you'll do, What they ask for), 16px or more, about 70ch wide. Never a wall of text.
- Everything else is folded underneath, one row each (Why it fits you, history, more details).
- Apply (primary pill) and Ask the assistant (secondary pill) stay pinned at the bottom.
- In lists, one row per item: title, then "Company · Where · When · Pay".

## 6. Copy

- Fewest words possible. If a word doesn't add value, cut it. Headlines under ~8 words, supporting lines one sentence.
- Plain, blunt, confident. Sounds like a person talking, not a pitch.
- No ambiguous terms, no internal jargon. Labels name the outcome ("Prepare application", not "Run agent").
- **Examples use the real brand and are vivid.** Demo data, sample rooms and example stories use the actual product and company (UTern, not "Acme Software") and are captivating, not bland ("a crazy story", not "the district gave a bus contract to a cousin").
- Banned words: delve, crucial, robust, comprehensive, seamless, leverage, elevate, unlock, empower, journey, landscape, cutting-edge, innovative, synergy, revolutionize, game-changer.
- No "Welcome to…", no "keep scrolling", no throat-clearing, no exclamation marks, no rule-of-three cadence.

## 7. Motion and loading

Smooth like a high-quality app, never showy.

```css
.reveal { opacity: 0; transform: translateY(16px); transition: opacity .7s cubic-bezier(.2,.6,.2,1), transform .7s cubic-bezier(.2,.6,.2,1); }
.reveal.in { opacity: 1; transform: none; }
@media (prefers-reduced-motion: reduce) { *, *::before, *::after { animation: none !important; transition: none !important; } }
```

- Fade-up on scroll, 1–2px hover lifts, 150–250ms UI transitions, ease-out in. Nothing loops or bounces.
- **Loading shows progress:** the loading state appears the instant something is clicked (no dead pause), shows what's happening as short steps that get checkmarks as they finish, sits next to the thing it's loading, and appears once (never duplicated). Use skeletons for content, not spinners.

## 8. Imagery and visuals

Every visual must explain something. If an image doesn't convey what the product does, replace it.

- **Real or nothing:** real product screens shown whole (not zoomed into a fragment), real photos, real data.
- Product screens go in a **realistic device frame** when shown as a phone or laptop (correct notch, status bar, proportions; nothing overlapping).
- A raw screenshot alone is not enough: pair it with a short statement, or use a very simple diagram with real words that shows the concept (e.g. a line sweeping a map with dots where clusters appear).
- Workflows flow horizontally or diagonally as one connected visual, never as numbered boxes or a list of steps.
- **As realistic as possible** whenever depicting real things (products, places, devices). No AI-looking illustrations, stock-art people, generic maps or emoji.

## 9. Brand assets and the live assistant

- **Logos, favicons, app icons and mascots are transparent and tightly cropped.** No white or black square, no padding ring, no colored circle, no whitespace around them, anywhere (favicon, nav, footer, share image, chat bubble).
- **Every site has a live assistant in the bottom-right corner:** the product's mascot or logo as a small round face (about 56px), nothing else. No label text like "Ask me anything", no tooltip clutter.
  - On the marketing site it is a **live question helper**: clicking it opens a small, clean chat panel that answers visitors' questions about what the product is, how it works, pricing and how to get started, grounded in the site's own content (never invents features or numbers). It should steer toward the primary CTA when relevant.
  - Inside the app it is the product's assistant (Birdee, Sherlock, Pip, etc.).
  - The panel follows this standard: white, same font, pill send button, 16px text, opens and closes smoothly, works on mobile, keyboard accessible, closes on Escape.
  - If the project has no AI backend yet, wire it to a real LLM endpoint (prefer the Vercel AI Gateway) with the site's content as context. Don't ship a fake canned-answer widget.

## 10. One look across the whole product

The logged-in app, every interior page and the landing page share the same tokens, fonts, buttons, inputs and spacing. When adding or restyling an app page, match the landing page exactly. Same colors everywhere (audit for stray hues after any change), same font everywhere, every button from the one button component.

## 11. How to work with Spencer on design

- **Change only what Spencer asked.** Keep everything else pixel-identical. Edits to an existing page are tweaks, not redesigns.
- **"Less AI" means strip the tells in section 1 inside the current design**, not invent a new identity. Ask what specifically feels off if unclear.
- **New designs and redesigns: show options first.** Make 2–3 distinct options as a preview (HTML mockup or dev server), open it for Spencer, and implement only the one Spencer picks. Small tweaks get applied directly, then shown.
- Don't propose full redesigns unprompted; they usually get reverted.
- **Check before showing.** Screenshot every changed page at 390px and 1440px and fix overlap, crowding, off-center elements, skew, items too close to edges, and unrealistic device frames before reporting done. Then open it for Spencer.
- New project: finish **§0 Sector research first** (findings saved with source URLs), then write a short `DESIGN.md` derived from this file (fonts, the one accent, ground color, signature hero background, assistant mascot, and the adopt/avoid notes from research) plus one theme file, and log rejected ideas there so they don't return.
- Ship with accessibility: AA contrast, 44px tap targets, visible focus ring, reduced motion.

## 12. Pre-ship checklist

Run this on every page before saying done:

- [ ] New site: sector research done (4–6 verified leaders, findings path, adopt/avoid); no cloned competitor UI or invented rankings. Other firms' or companies' rankings and credentials are research inputs only and are never presented as the client's own. Proof or recognition sections are left out entirely until there is real, attributable proof.
- [ ] Every control on the page does something the user can see and cares about; nothing left over from a removed feature.
- [ ] Zero items from the section 1 ban list (search for `01`, `—`, `→`, `<hr`, `border-top`, `border-bottom`, `<em`, `italic`, purple hues, emoji).
- [ ] No statement, feature or theme appears twice on the page.
- [ ] White background by default, also on a device in dark mode; sign-in and item screens follow 5e.
- [ ] Mostly white; at most one accent; at most one dark band; signature hero background in place.
- [ ] One font family (+ mono for numbers); headlines big, tight, Title Case; emphasis by weight; brand names spelled exactly.
- [ ] No text under 16px outside dense app chrome.
- [ ] Hero, statements and CTA groups centered; body left-aligned.
- [ ] All buttons are word-only pills from one component; one primary per screen.
- [ ] Sticky full-width nav with plain-word links, active state, Sign in + Sign up top right, and a working mobile menu.
- [ ] Landing page shows no signed-in state; deep or audience content lives on its own pages.
- [ ] CTA in the nav, the hero and a closing band; every interior page ends with one; all CTAs work and don't change after load.
- [ ] Full multi-column footer with socials; every footer link opens a real, themed page (no `#`, no 404s).
- [ ] Sections separated by space, not lines or boxes.
- [ ] Every visual is real, explains something, and device frames look real.
- [ ] Logos, favicon and mascot have no background or padding.
- [ ] Bottom-right assistant is a round face only and actually answers questions about the product.
- [ ] Loading states appear instantly, show checkmarked steps, appear once.
- [ ] App pages match the landing page's tokens, fonts and buttons.
- [ ] Copy is the fewest words that still say it clearly; examples use the real brand.
- [ ] Screenshotted at 390px and 1440px: no overlap, crowding, off-center or edge-hugging elements; reduced motion works.
