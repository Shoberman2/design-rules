# Spencer's Design Rules

The house design standard for every website and app Spencer builds (UTern, Leed, BallotWatch, Validate, SparkTech and everything new). Any AI agent (Claude, Codex, Grok Bot) designing, styling or reviewing Spencer's work follows these.

| File | Covers |
| --- | --- |
| [`ABOUT.md`](ABOUT.md) | **Start here.** Who Spencer is, the products and mascots, and why the rules exist. |
| [`spencer-web-style/SKILL.md`](spencer-web-style/SKILL.md) | Websites, landing pages, web UI. The base rules. |
| [`spencer-app-style/SKILL.md`](spencer-app-style/SKILL.md) | Apps (iOS, Expo, logged-in web apps, dashboards). Builds on the web rules. |
| [`GROKBOT.md`](GROKBOT.md) | Grok Bot's weekly rules-review job. |
| [`feedback/`](feedback/) | Weekly digests of Spencer's design feedback from Claude and Codex chats. |
| [`CHANGELOG.md`](CHANGELOG.md) | Every approved rule change. |

A project's own `DESIGN.md` wins only where it explicitly differs.

## Self-updating

The rules update themselves weekly, but only with Spencer's approval:

1. **Sunday 6pm:** a launchd job on Spencer's Mac (`scripts/weekly_digest.py`, plist in `scripts/`) collects Spencer's design-related messages from the past week of Claude Code and Codex sessions, redacts secrets, writes `feedback/YYYY-Www.md`, and pushes it here.
2. **Monday:** Grok Bot reads the new digest, compares it to the rules, and asks Spencer: *"Hey, here are some common themes of what you implemented in designs. Do you want these added to the rules?"*
3. **On approval:** Grok Bot edits the rule files, logs the change in `CHANGELOG.md`, and pushes. Claude and Codex pick it up automatically, since `~/.claude/skills/spencer-*` and `~/.codex/skills/spencer-*` are symlinks into the local clone at `~/design-rules` (pull to sync).

Run a digest by hand: `python3 scripts/weekly_digest.py [days]`.
