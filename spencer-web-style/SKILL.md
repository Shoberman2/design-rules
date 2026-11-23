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
- **Gimmick motion:** bounce, typing effects, word-by-word reveals, particles, marquees, custom cursors, 3D tilt, magnetic buttons. One exception: a single showcase object Spencer asks for, like the SparkTech membership card (see 4a), may lean toward the pointer.
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

- **Accent:** default to none (ink). A brand may get **one** accent hue (e.g. UTern blue `#2563EB`, SparkTech gold `#ffd15c`), used only for links, the primary button, focus and state. Never two accents.
- **The accent is the favicon's color** (2026-11-21). The logo in the nav and footer, the accent and every button use exactly the color of the browser-tab icon. If the favicon is brighter than the site, the site moves to the favicon, not the other way round.
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
- **Buttons look finished** (2026-11-21, "make the buttons look stylish"): on a dark ground the primary pill gets a soft 1px light edge along its top and a warm glow of its own color on hover; the secondary pill is clear glass (a light blur) with a fine light edge that fills solid on hover. Weight 600. Still words only, still one component.
- **A button inside a field fills it** (2026-11-17). When a button shares a pill with an input (a search or ZIP field, a chat composer), the button is the full height of that field and sits flush in its end. Never leave a ring of the field's background around the button.
- Radius: inputs 12px, cards and media frames 16–24px, sheets/modals 24px, big hero media 28–40px.
- Shadows: soft and rare. `0 1px 2px rgba(20,20,15,.04), 0 12px 32px rgba(20,20,15,.06)`.
- Space is the separator. Section padding `clamp(96px, 12vw, 160px)`. Gaps between items 24–48px. 4px base grid. Never crowded, never touching the bottom edge of a section or viewport.
- Content width 1180px max, gutter `clamp(20px, 5vw, 56px)`. Reading columns 680–760px.
- Icons: Lucide outline, small, only when they carry meaning (never inside buttons).

### 4a. A showcase card (2026-11-21, SparkTech)

When a price or plan is shown as a card, it is an object, not a box of bullet points:
- It is a real membership card, at a high level: card proportions (1.586:1), the site's colors as its material (for SparkTech, black brushed metal with gold foil type), a real EMV chip and contactless mark, the real logo, a fine accent edge, and a visible edge with thickness when it turns. A back face (stripe, signature panel, the site's address) shows when it is clicked or tapped.
- It sits level, never rotated at rest.
- **The whole card moves, not the light** (Spencer, 2026-11-21: "I want the card to actually move, not the light or a gradient in the card. I don't like that at all"). It turns (about 18°) and drifts toward the pointer anywhere in its section, eased so it feels weighted, and its shadow on the ground moves the other way. All lighting on the card is fixed. No glare, spotlight or gradient that follows the pointer, and nothing inside the card moves on its own. A finger drag works on a phone. It settles flat when the pointer leaves, and only flips (no turning) with reduced motion.
- It carries only a name and, when Spencer wants it shown, the price (e.g. "$500 / month"). No feature list on or under it. One button below it.

## 5. Landing page shape

The landing page is **marketing only**: it explains the product and gets people to sign up. A story told top to bottom. Each section earns the next; none repeats another.

1. **Nav** (see 5a).
2. **Hero:** centered. One short Title Case statement (the promise), one supporting line at most, one primary pill CTA (optional secondary pill). Behind it, the brand's **signature background** (see 5d). No tags above it.
3. **Statement sections:** one idea each, alternating text and visual. Short centered H2, one or two short lines, then a visual that explains (section 8). Each section ends in a clear next step.
4. **Proof** only if it is real.
5. **FAQ: always a dropdown** (Spencer, 2026-11-21: "it should always be like that"). One question per row, closed by default, opening to its answer. Use native `<details>`/`<summary>` so it works without JavaScript and with a keyboard, and the answers stay in the HTML for search. Rows are separated by space (a quiet fill per row is fine), never lines. An accent plus at the row's end turns into a minus when open. Add FAQPage structured data.
6. **Closing CTA band:** one strong statement + the primary pill, centered. The one dark band, if used, usually lives here.
7. **Footer** (see 5b).

Marketing rules:
- Never show signed-in state on the landing page: no "Sign out", no account menu, no app-only features in the nav. Visiting the landing page never feels logged in.
- Audience-specific or deep content gets **its own page** ("For Businesses", "How It Works", "Pricing", "For Schools"), not crammed onto the homepage.
- An app (iOS or web app) never contains a marketing landing page; it opens to sign-in or the product.
- **Developer features get a "For Developers" page** (2026-11-17). An API, an MCP server, SDKs, open data and anything else built for developers or AI agents is explained on one "For developers" page, linked by that name in the nav and footer. It never gets a section on the landing page, which explains only the features an everyday reader uses.

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

- **No CTA button and no tagline in the footer** (Spencer, 2026-11-21: "Don't put a CTA in the footer"). The closing band above it carries the call to action.
- 4–5 link columns with plain 16px headings, grouped by intent, e.g. **Product** (Features, Pricing, How it works, Changelog), **Company** (About, Careers, Contact, Press), **Resources** (FAQ, Help center, Blog/Guides). The group of columns is centered under the page.
- **Legal is its own column** (Privacy, Terms, Sitemap, plus Cookies or Security when they exist), never a loose row of links at the bottom, where it looks out of place.
- Every page on the site appears in the footer.
- Bottom: the logo (the favicon mark, no background) beside "© year Legal Entity Name", centered, nothing else. Social accounts go in the Contact column as plain links; don't print raw emails unless the project says to.
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
- **Headlines are about four words** when they sit over a visual ("Your Career Starts Here."). If Spencer says "make this simpler", cut the headline to one short clause before touching anything else.
- **A printed number carries its source.** Any figure on a page (a cost, a count, a benchmark) shows where it came from and which parts are our own assumptions, in a quiet line or a "How we got this" fold beside it. Our own arithmetic is labelled as our estimate, never as a study. A comparison ("less than", "cheaper") needs both numbers on the page.
- **Say what the product covers, all of it.** When a product serves more than one group or season (interns and new grads, year round), copy names them all; never the narrowest one alone.
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
- **As realistic as possible** whenever depicting real things (products, places, devices). No AI-looking illustrations, stock-art people, generic maps or emoji. On product marketing sites, people appear only in the people-video form below (8a). On a client redesign or mockup, keep the business's own photos, including team photos (8b).

### 8a. People video ("A Person And A Message", 2026-11-11)

The one sanctioned way to show people. Spencer on UTern: "I love the style of video you made." Use it to explain a feature without showing the product's screen.

- **What it is:** a short clip of one person in their own day (on their phone on campus, behind a counter, at a desk), and the assistant's messages arriving over the footage. The person carries the feeling; the messages say what the product did.
- **The footage:** one continuous shot, 6 seconds, looping, silent. Photoreal, warm natural light (golden hour, a window), shallow depth of field, gentle or no camera move. The person sits on one third of the frame; the other half is soft background, left free for the messages. A different person in every clip, same grade across the set.
- **Never in the footage:** product screens, text, captions, logos, readable signs. Phone and laptop screens face away.
- **The messages:** real HTML over the video, never baked in. Three lines per clip: the assistant, the person's short reply, the assistant again. The assistant's bubble is dark glass (blur) with the mascot's head and name; the person's reply is the brand accent, on the right. Lines arrive one at a time, the newest two stay (the older one dimmed), then the conversation rests and starts again.
- **Every line is true:** it says only what the product does. No invented numbers, companies or outcomes.
- **Generated people are not customers.** Clips may be AI-generated; say so in the code, and never present the person as a user, a testimonial or a real student.
- **Sizes:** one wide clip (16:9, the hero's corner radius) under a short Title Case headline of about four words; then one clip per feature, filling that feature's frame (16:9, 4:3 on a phone). The first clip may be higher quality than the rest.
- **Build:** H.264 mp4 with faststart, no audio track, a JPEG poster, `muted playsInline loop preload="none"`. Play only while in view. Rows at 1280px wide, about 400 to 600 KB each. With reduced motion: the poster and all three lines, no animation. One hidden line of text gives a screen reader the whole exchange once.
- **Take the idea, not the site.** When another site inspires this, bring over only the people-and-message idea: not its nav, layout, colors, type or cast.
- **Prompt recipe:** "Photoreal cinematic lifestyle footage, one continuous shot, natural skin and motion. [Who, age, clothes] [where] [one small action ending in a smile or nod]. Medium shot, [light], shallow depth of field. They are on the right side of the frame; the left half is soft out of focus background. Phone screen not visible. No text, no captions, no logos, no readable signage, no on-screen graphics."

### 8b. Redesigns: keep and upgrade the client's real media (2026-11-15)

Spencer, on SparkTech mockups: keep the images and videos in the new version; it shouldn't look bare, and it should look even better.

- **Keep their media, and make it look better.** Every redesign or mockup keeps the business's own images and videos from the current site: logo, storefront or interior, team, work and gallery photos, and any embedded video. The new version must never look bare, and must look clearly better than the original.
- **Fill the page with their photos.** Use a full-bleed real photo hero with a dark scrim (a gradient overlay on the photo only, so text stays AA-readable; this is not a decorative page gradient). Add photo sections or galleries. Design mobile-first, and check at 390px and 1440px.
- **Upgrade low-res originals.** Upscale or sharpen weak photos (Higgsfield upscale using existing credits only, never buy more; or a local sharpen). Crop out baked-in dated banners, borders and text.
- **Skip junk media.** Leave out tiny icons, spacers, dated banner GIFs and typography collages. Don't mix stock or model shots next to real interiors.
- **Never invent the business.** Do not create fake photos of the shop, its staff or its work. Generic textures or quiet fills are fine when you need a ground. If a site has under about 4 usable photos, flag it as thin.
- **Don't guess names.** Don't caption staff photos with names unless the name is confirmed, so no one is misidentified.
- **Pre-ship for redesigns and mockups:** every image loads; no text runs edge to edge (keep at least 20px side padding on mobile); real services, hours, phone and address are kept.

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
- [ ] Full multi-column footer, centered, with Legal as its own column, no CTA button, and only the logo with © at the bottom; every footer link opens a real, themed page (no `#`, no 404s).
- [ ] Every FAQ is a dropdown (`<details>`), separated by space, with FAQPage structured data.
- [ ] Logo, accent and buttons are the favicon's exact color.
- [ ] Sections separated by space, not lines or boxes.
- [ ] Every visual is real, explains something, and device frames look real.
- [ ] Client redesign or mockup (8b): the business's own photos and videos are kept and upgraded; the page does not look bare and looks clearly better than the original; no invented photos of the business, staff or work; every image loads; at least 20px side padding on mobile; real services, hours, phone and address are kept. Flag the brief if there are under about 4 usable photos.
- [ ] Logos, favicon and mascot have no background or padding.
- [ ] Bottom-right assistant is a round face only and actually answers questions about the product.
- [ ] Loading states appear instantly, show checkmarked steps, appear once.
- [ ] App pages match the landing page's tokens, fonts and buttons.
- [ ] Copy is the fewest words that still say it clearly; examples use the real brand.
- [ ] Screenshotted at 390px and 1440px: no overlap, crowding, off-center or edge-hugging elements; reduced motion works.
