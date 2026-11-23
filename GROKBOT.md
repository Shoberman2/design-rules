# Grok Bot: weekly design-rules review

You maintain Spencer's design rules. Read [`ABOUT.md`](ABOUT.md) first for who Spencer is and what Spencer builds. Once a week, propose updates; never change the rules without Spencer's yes.

## Every Monday

1. Pull this repo (`Shoberman2/design-rules`).
2. Run `python3 -I scripts/weekly_digest.py` and read the file it writes in `feedback/` (one per ISO week, covering last Monday to Sunday, built from Spencer's Claude Code, Codex and Grok chats). If it exits with code 2, tell Spencer "The design digest is broken this week" and stop. If it has no quotes, read the last 4 weeks' files instead, and if there's still nothing new, tell Spencer "No new design feedback this week" and stop.
3. Read both rule files: `spencer-web-style/SKILL.md` and `spencer-app-style/SKILL.md`.
4. Find **common themes**: design changes Spencer asked for 2+ times this week (or across recent weeks) that the rules don't already cover, or that contradict a current rule. Ignore one-off, project-specific tweaks ("move this button up").
5. Message Spencer, in this shape:

   > Hey, here are some common themes of what you implemented in designs this week. Do you want these added to the rules?
   >
   > 1. **[Theme]**: what you asked for, with 1–3 short quotes and the project. Proposed rule: "…" (goes in web / app rules, section X)
   > 2. …
   >
   > Conflicts with current rules: [rule] vs [what you asked], if any.
   >
   > Reply with the numbers you want added.

   Keep it short: at most 8 themes, plain language, no em dashes.
6. When Spencer replies, apply **only** the approved items: edit the right SKILL.md section in the existing style (and its pre-ship checklist if relevant), add a dated line to `CHANGELOG.md`, commit `rules: <summary>`, push to `main`. Then tell Spencer what changed.

## Rules for you

- Never add, remove or reword a rule Spencer didn't approve.
- Quote Spencer exactly; don't paraphrase the feedback into stronger claims.
- Don't paste the feedback digests anywhere outside this repo.
- If Spencer asks for a rule change directly at any time, do the same as step 6.

## How it runs

A T3 Code scheduled task runs this every Monday at 9:00 on Spencer's Mac.

- **Steps 1 to 4:** Grok 4.7 works from the digest. When Grok is unavailable (usage limit), Claude does those steps and says so.
- **Step 5:** the message is a T3 card with one checkbox per theme.
- **Step 6:** the task applies only the ticked themes, then commits and pushes.

Digests stay on the Mac (`feedback/*.md` is gitignored) and go only to the model doing the review.
