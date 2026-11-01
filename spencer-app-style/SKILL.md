---
name: spencer-app-style
description: Spencer's house design standard for every app Spencer builds (iOS/SwiftUI, Expo/React Native, and logged-in web apps/dashboards such as UTern, Perch, Budtender, ThreadFit, BallotWatch iOS, openStudy, voiceTrivia). Load BEFORE designing, styling, redesigning or reviewing any app screen, onboarding, chat UI, tab bar, app icon or dashboard. Builds on spencer-web-style, which must be loaded too.
---

# Spencer's App Style

**Read [`ABOUT.md`](../ABOUT.md) first** (who Spencer is, the products, mascots and why these rules exist).

**Load `spencer-web-style` first. Every rule there applies to apps too** (bans, color, type, pills, Title Case, 16px minimum, no lines as separators, no arrows in buttons, transparent logos, assistant, consistency, preview-first, check-before-showing). This file adds the app-specific rules and wins where the two differ (notably: apps always get dark mode).

**The feel in one line:** a polished, native-feeling app with the website's brand: as few screens as possible, a named character to talk to, one clear action per screen, instant feedback on every tap, and a dark mode that looks as good as light.

Quality bar, in Spencer's words: *"like Triumph or any other app that's been designed and looks really good."*

---

## 1. Structure

- **As few screens as possible.** Fold features into the chat or the main screen before adding a page. Cut any page that isn't clearly useful ("The nav pages aren't very useful... keep it to chat features"). Each feature gets one or two buttons or a chat entry point, not a new section.
- **Navigation depends on the concept.** Decide per app and say why:
  - Assistant-led apps (Perch, ThreadFit): the chat is the home screen; secondary actions live in the chat's `+` menu or as starter prompts. No tab bar.
  - Content/social apps (Budtender): a tab bar of 3–5 tabs, each earning its place, in a locked order (e.g. Feed, Strains, My list, Search, Profile).
  - Never more than 5 tabs. Tab labels are plain words with outline icons.
- **Settings and profile open as a sheet** (pop-up over the current screen), never a separate full page. Sheets over stacked pages everywhere.
- **No marketing landing page inside an app.** The app opens to sign-in (or onboarding), then straight into the product.
- **App-native feel, website brand.** Same colors, font, mascot and voice as the website, but native patterns: sheets, tab bars, swipe gestures, pull to refresh, haptics, system share sheet. It should not look like the website squeezed onto a phone.

## 2. Onboarding and sign-up

- **Fewest fields possible.** Sign-up is email + password (add name or birthday only when the product truly needs it, e.g. age-gated). Google/Apple sign-in above email. No extra profile questions at sign-up.
- **Onboarding is a conversation with the character.** One question at a time; the user types or taps a quick answer (Yes / No, or 2–4 choices). Tap-only where possible, 5 steps max.
- Ask each personal preference once here (style goals, allergy profile, voice on/off, price range), then never ask again; it's editable in the settings sheet.
- Every step is skippable only if the app works without it. No "Skip this step" buttons on core steps; offer a better action instead ("Show me another").

## 3. The character (assistant)

- **Every app has a named character** with a real personality (Birdee, Pip, Budzy, Sherlock), drawn as the brand's own mascot. Never an orb, blob, generic sparkle, or a photo-real person.
- Small personality moments are welcome and on-brand (Budzy's replies drifting off as smoke). One or two, not everywhere.
- **The app icon is the mascot**, transparent and tightly cropped in the source art, no added frame or colored square beyond what the platform requires.
- In web apps and dashboards, the character sits bottom-right as a small round face (see web rules).

## 4. Chat UI

- The chat bar looks natural and quiet: one text field, a send pill, at most one `+` for attachments/scan. No voice button unless the user turned voice on in onboarding.
- Messages are readable and consistent: 16px+ text, comfortable bubble width, nothing flattened, squished or out of proportion, the same layout every time.
- Links inside replies are plain text. Tapping one opens that exact item (job, strain, product), with similar items listed below it. Primary action on that item first (e.g. Apply), secondary after.
- Rich results (cards for jobs, products, places) use one standard card format everywhere in the chat.
- Starter prompts on an empty chat are short plain text buttons, not pill tags.
- Loading lives inline next to the message: the character's own loading animation plus short steps that get checkmarks, shown once.

## 5. Feel, motion and feedback

- **Every tap gets instant feedback.** Loading appears the moment something is tapped. Confirmations slide down as a short banner ("Moved to Saved"). Correct answers get a checkmark. Light haptic on primary actions, success and errors. No dead taps, no silent failures.
- **Great transitions everywhere:** native push/sheet transitions, smooth list insertions, shared-element or zoom transitions into detail views. Spring animations are fine in apps when they are subtle (no visible bounce overshoot).
- **One signature moment per app** that makes it memorable (Budtender's zoom from the phone into the bud as THC/CBD/terpenes light up). Polished and fast, never blocking.
- Respect Reduce Motion (cross-fade instead).

## 6. Screens and content

- **One clear primary action per screen.** Remove every option that isn't needed (an extra "Symptoms" button, a voice button, "Skip this step").
- **Images at the right size and accurate.** Thumbnails sized so several fit on screen, never oversized. Images must actually show the thing (the right product, the right style), with no text baked into images and no zooming in on the wrong detail. As realistic as possible.
- **Never show the same thing twice:** no repeated items in a feed or recommendations, and vary formats (openStudy questions mix concepts, not always fill-in-the-blank).
- **Feeds look like real posts** in one standard format (who, what, the item, the reaction). When the feed is empty, show clearly labeled preview posts, never fake ones presented as real.
- Lists use settings-style rows: small label over a 16px+ value, separated by space, not lines.
- Empty states are specific to the screen and point to the one next action.

## 7. Gamification: per app

Decide per app and state the choice in the project's DESIGN.md. When an app uses it (Budtender, voiceTrivia), keep it simple: checkmarks, rankings, lists that fill up, satisfying feedback. When it doesn't (UTern, BookSaver), no streaks, points, badges, confetti or party emoji. Never gamify by default.

## 8. Dark mode: always, and it must look good

Every app ships light and dark, following the system setting with an override in the settings sheet. Dark is designed, not inverted.

```css
/* light: use the spencer-web-style tokens */
:root[data-theme="dark"], .dark {
  --bg: #0E0E10;
  --surface: #17171A;       /* cards, sheets */
  --surface-dim: #1F1F23;   /* inputs, hover, segmented controls */
  --card-edge: #2A2A2F;     /* a raised surface's own outline only */

  --ink: #F2F2EF;           /* text + primary buttons (button text is --bg) */
  --ink-2: #B4B2AC;
  --ink-3: #8C8A84;         /* lightest text grey, AA on --bg */

  --accent: var(--ink);     /* or the brand accent, lifted for dark (e.g. blue #2563EB -> #60A5FA, gold #b8860b -> #d4b46a) */
  --ok: #4CC38A; --warn: #F5A524; --bad: #F2555A;
}
```

- Same token names in both themes; components never hardcode colors. In SwiftUI, every color lives in the asset catalog with Any + Dark appearances (or one `Theme.swift`), never inline `Color(red:...)`.
- Depth in dark comes from lighter surfaces, not shadows. No pure `#000` backgrounds, no pure `#FFF` text.
- Check every screen in both themes: AA contrast, mascot and images readable, no invisible borders or icons, accent still legible.

## 9. Platform specifics

- **iOS/SwiftUI:** use the project font (Geist/Satoshi bundled) with Dynamic Type support; SF Symbols in regular/outline weights; 44pt minimum tap targets; respect safe areas; native sheets with `.presentationDetents`; haptics via `sensoryFeedback`.
- **Expo/React Native:** same tokens in one theme file, `useColorScheme` for dark mode, native stack and sheet navigation, expo-haptics.
- **Web apps and dashboards:** follow spencer-web-style fully, plus this file's structure, chat, feedback and dark-mode rules.

## 10. Business / enterprise apps

Professional and minimal. Pipelines (candidates, tips, orders) use a board with columns (e.g. Sourced, Interviewing, Offer) that open into detail sheets. Information as settings-style rows, not boxes. Same brand, calmer: no signature animations, no gamification.

## 11. Shipping

- When a build is ready, open it in the iOS Simulator for Spencer, then offer TestFlight to Spencer's phone (team ID in global CLAUDE.md).
- Screenshot every changed screen in light and dark at iPhone SE and iPhone Pro Max sizes before reporting done; fix overlap, crowding, clipping and off-center items first.

## 12. App pre-ship checklist

All of the spencer-web-style checklist that applies, plus:

- [ ] Fewest screens; every tab/page clearly useful; nav choice (chat-only vs tabs) justified by the concept.
- [ ] Settings and profile are sheets; no marketing landing page in the app.
- [ ] Sign-up is minimal; onboarding is a one-question-at-a-time chat, 5 steps max.
- [ ] Named character present; app icon is the mascot with no added background.
- [ ] Chat bar quiet; messages consistent and unsquished; links open the exact item.
- [ ] Every tap has instant visual (and haptic) feedback; loading shows checkmarked steps once.
- [ ] One primary action per screen; no unneeded options.
- [ ] Images correctly sized, accurate, realistic; nothing repeated in feeds/recommendations.
- [ ] Gamification choice recorded in DESIGN.md and followed.
- [ ] Dark mode designed and checked on every screen; light mode too.
- [ ] Opened in the simulator for Spencer.
