#!/usr/bin/env python3
"""Weekly design-feedback digest for GrokBot.

Reads Spencer's own messages from local Claude Code, Codex and Grok chats,
keeps the design-related ones, and writes feedback/<ISO year>-W<week>.md for
GrokBot's Monday review (see GROKBOT.md).

  python3 -I scripts/weekly_digest.py            # the last full week, Mon to Sun, local time
  python3 -I scripts/weekly_digest.py --days 7   # a rolling window ending now
  add --stdout to print instead of writing the file

Exit codes: 0 ok · 2 a source had recent chat files but none could be read,
so the digest may be wrong (GrokBot reports "digest broken", never "no feedback").

Privacy: read-only, sends nothing anywhere. Secrets, emails and phone numbers are
redacted, health projects are skipped, and feedback/ is gitignored so digests stay
on this Mac. Streams files line by line, so memory stays small.
"""

from __future__ import annotations

import datetime as dt
import difflib
import json
import re
import subprocess
import sys
import tomllib
from pathlib import Path

HOME = Path.home()
REPO = Path(__file__).resolve().parent.parent
CLAUDE_DIR = HOME / ".claude" / "projects"
CODEX_DIRS = [HOME / ".codex" / "sessions", HOME / ".codex" / "archived_sessions"]
CODEX_AUTOMATIONS = HOME / ".codex" / "automations"
GROK_DIR = HOME / ".grok" / "sessions"
PORTFOLIO = HOME / "studio-ops" / "portfolio.toml"

# Health data never goes into a digest that Grok reads.
EXCLUDE_IDS = {"spacial", "perch"}
EXCLUDE_NAME_HINTS = ("spacial", "allergy", "perch")

MAX_CHARS = 3000
QUOTE_CHARS = 700
LOOP_MARKER = "[studio-ops loop]"   # first line of every scheduled-loop prompt

DESIGN = re.compile(
    r"\b(design|designs|redesign|style|stylish|styling|colou?rs?|font|fonts|typograph\w*|"
    r"buttons?|spacing|padding|margins?|align\w*|cent(er|re)(ed)?|hero|layout|logo|favicon|"
    r"icons?|nav|navbar|footer|header|cards?|white|black|gold|accent|gradient|glow|shadows?|"
    r"borders?|rounded|pills?|animation|animate|motion|mockups?|screenshots?|whitespace|"
    r"bigger|smaller|ugly|generic|clean(er)?|minimal|sleek|modern|premium|tacky|cluttered|"
    r"less ai|looks? (ai|off|bad|weird|good|great|cheap)|dark mode|light mode|landing|"
    r"ui|ux|onboarding|tab bar|modal|popup|em dash|emoji|serif|sans|italic|"
    r"design rules?|spencer-(web|app)-style)\b",
    re.I,
)
BRIEF_START = re.compile(
    r"^(you are |your (task|job|brief)|task:|context:|brief:|#{1,3} |\*\*task|"
    r"implement |review the |audit |this is a (task|brief)|caveat:)",
    re.I,
)
# A session whose first prompt looks like this was started by another agent (a T3 child or loop).
SESSION_BRIEF = re.compile(r"^(you are |your (task|job|brief)\b|task:|brief:|\*\*task)", re.I)
# Text the harness or another agent injected as a "user" message.
HARNESS_MARKERS = (
    "<task-notification", "<task_notification", "<subagent", "tool-use-id", "tool_use_id",
    "<user_request>", "[Artifact comment", "This is how Claude Code surfaces", LOOP_MARKER,
)
HARNESS_ID = re.compile(r"\bcall_[0-9a-f]{6,}|\b[0-9a-f]{16,}\b")
STRIP_BLOCKS = [
    (re.compile(r"<system-reminder>.*?</system-reminder>", re.S), " "),
    (re.compile(r"<t3_code_instructions>.*?</t3_code_instructions>", re.S), " "),
    (re.compile(r"<recommended_plugins>.*?</recommended_plugins>", re.S), " "),
    (re.compile(r"<pasted_content[^>]*>.*?</pasted_content[^>]*>", re.S), " [pasted] "),
    (re.compile(r"<command-(message|args|stdout|stderr)>.*?</command-\1>", re.S), " "),
    (re.compile(r"<local-command-[a-z]+>.*?</local-command-[a-z]+>", re.S), " "),
    (re.compile(r"\[?Attached (image|file) \"[^\"]*\" is saved at: \S+\]?", re.I), " [image] "),
]
TAG = re.compile(r"</?[a-z_][a-z0-9_-]*(\s[^>]*)?>", re.I)
AGENT_REPORT = re.compile(r"(/Users/|~/|/tmp/|\bPR #\d+|\bpass(es)? (lint|build)|\bworktree\b|\bcommit [0-9a-f]{7})")
REDACT = [
    re.compile(r"\bsk-[A-Za-z0-9_-]{16,}"),
    re.compile(r"\b(ghp|gho|ghs|ghu|github_pat)_[A-Za-z0-9_]{20,}"),
    re.compile(r"\bxox[abprs]-[A-Za-z0-9-]{10,}"),
    re.compile(r"\bAKIA[0-9A-Z]{16}\b"),
    re.compile(r"\beyJ[A-Za-z0-9_-]{8,}\.[A-Za-z0-9_-]{8,}\.[A-Za-z0-9_-]{4,}"),
    re.compile(r"(?i)\bbearer\s+[A-Za-z0-9._~+/-]{16,}"),
    re.compile(r"(?i)\b[A-Z0-9_]*(KEY|TOKEN|SECRET|PASSWORD|PASSWD)[A-Z0-9_]*\s*[=:]\s*\S+"),
    re.compile(r"[\w.+-]+@[\w-]+(\.[\w-]+)+"),
    re.compile(r"(?<!\w)(\+?1[\s.-]?)?\(?\d{3}\)?[\s.-]\d{3}[\s.-]\d{4}(?!\w)"),   # phone numbers
    re.compile(r"\b[A-Za-z0-9+/_-]{40,}\b"),
]


# ---------- text ----------

def clean(text: str) -> str:
    m = re.search(r"<input>(.*?)</input>", text, re.S)
    if m and "<realtime_delegation>" in text:   # Codex voice: keep only the spoken words
        text = m.group(1)
    for rx, repl in STRIP_BLOCKS:
        text = rx.sub(repl, text)
    text = TAG.sub(" ", text)
    for rx in REDACT:
        text = rx.sub("[redacted]", text)
    return re.sub(r"\s+", " ", text).strip()


def injected(raw: str) -> bool:
    return any(m in raw for m in HARNESS_MARKERS) or len(HARNESS_ID.findall(raw)) >= 2


def human(text: str) -> bool:
    if not text or len(text) < 8 or len(text) > MAX_CHARS:
        return False
    if BRIEF_START.match(text) or "(Recommended)" in text:   # briefs and answered question cards
        return False
    if text.count(" - ") + text.count("##") > 12:
        return False
    if len(text) > 250 and len(AGENT_REPORT.findall(text)) >= 2:   # a relayed agent report
        return False
    return True


# ---------- projects ----------

def load_portfolio() -> list[dict]:
    try:
        return tomllib.loads(PORTFOLIO.read_text())["project"]
    except (OSError, KeyError, tomllib.TOMLDecodeError):
        return []


PROJECTS = load_portfolio()
_cache: dict[str, tuple[str, str]] = {}


def project_of(cwd: str) -> tuple[str, str]:
    """(id, display name) for a chat's working directory."""
    if cwd in _cache:
        return _cache[cwd]
    result = None
    p = Path(cwd) if cwd else None
    if p and p.is_dir():
        try:
            r = subprocess.run(["git", "-C", cwd, "remote", "get-url", "origin"],
                               capture_output=True, text=True, timeout=5)
            remote = re.sub(r"(\.git)?$", "", r.stdout.strip()).split("github.com")[-1].strip(":/").lower()
        except (OSError, subprocess.TimeoutExpired):
            remote = ""
        for proj in PROJECTS:
            if remote and proj.get("repo", "").lower() == remote:
                result = (proj["id"], proj["name"])
                break
    if not result and p:
        best = None
        for proj in PROJECTS:
            root = Path(proj["path"]).expanduser()
            if p == root or root in p.parents:
                if not best or len(str(root)) > len(str(Path(best["path"]).expanduser())):
                    best = proj
        if best:
            result = (best["id"], best["name"])
    if not result:
        name = p.name if p else "unknown"
        parts = p.parts if p else ()
        if ".sshcode" in parts and "worktrees" in parts:
            i = parts.index("worktrees")
            name = re.sub(r"-t3-[0-9a-f]+$", "", parts[i + 1]) if i + 1 < len(parts) else name
        if ".sshcode" in parts and "scratch" in parts:
            name = "scratch chats"
        for proj in PROJECTS:
            if Path(proj["path"]).expanduser().name == name:
                result = (proj["id"], proj["name"])
                break
        if not result and name.startswith(("internidea", "utern")):
            result = ("utern", "UTern")
        result = result or (name.lower(), name)
    _cache[cwd] = result
    return result


def excluded(pid: str, name: str) -> bool:
    low = f"{pid} {name}".lower()
    return pid in EXCLUDE_IDS or any(h in low for h in EXCLUDE_NAME_HINTS)


# ---------- time ----------

def parse_ts(ts) -> dt.datetime | None:
    try:
        t = dt.datetime.fromisoformat(str(ts).replace("Z", "+00:00"))
    except (ValueError, TypeError):
        return None
    return t if t.tzinfo else t.replace(tzinfo=dt.timezone.utc)


def window(argv: list[str]) -> tuple[dt.datetime, dt.datetime, str]:
    now = dt.datetime.now().astimezone()
    if "--days" in argv:
        days = int(argv[argv.index("--days") + 1])
        return now - dt.timedelta(days=days), now, f"last-{days}-days-{now:%Y-%m-%d}"
    monday = (now - dt.timedelta(days=now.weekday())).replace(hour=0, minute=0, second=0, microsecond=0)
    start = monday - dt.timedelta(days=7)
    y, w, _ = start.isocalendar()
    return start, monday, f"{y}-W{w:02d}"


# ---------- sources ----------

class Stats:
    def __init__(self):
        self.files = self.user_lines = self.errors = self.kept = 0


def recent(root: Path, pattern: str, start: dt.datetime):
    if not root.exists():
        return
    for f in root.rglob(pattern):
        try:
            if f.stat().st_mtime >= start.timestamp():
                yield f
        except OSError:
            continue


def lines(f: Path, st: Stats):
    try:
        with f.open("r", encoding="utf-8", errors="replace") as fh:
            st.files += 1
            for line in fh:
                yield line
    except OSError:
        st.errors += 1


def from_claude(start, end, st):
    for f in recent(CLAUDE_DIR, "*.jsonl", start):
        if "/subagents/" in str(f):
            continue
        first = True
        for line in lines(f, st):
            if ('"type":"user"' not in line and '"type": "user"' not in line) or "tool_result" in line:
                continue
            try:
                o = json.loads(line)
                if o.get("type") != "user" or o.get("isSidechain") or o.get("isMeta"):
                    continue
                c = (o.get("message") or {}).get("content")
                if isinstance(c, list):
                    c = " ".join(x.get("text", "") for x in c if isinstance(x, dict) and x.get("type") == "text")
                if not isinstance(c, str) or not c.strip():
                    continue
            except (json.JSONDecodeError, AttributeError, TypeError):
                st.errors += 1
                continue
            st.user_lines += 1
            if injected(c):
                continue
            text = clean(c)
            if first:
                first = False
                if SESSION_BRIEF.match(text):   # the session was started by another agent
                    break
            t = parse_ts(o.get("timestamp"))
            if t and start <= t < end and human(text):
                yield t, "claude", o.get("cwd", ""), text


def codex_automation_prompts() -> list[str]:
    out = []
    for f in CODEX_AUTOMATIONS.glob("*/automation.toml"):
        try:
            p = tomllib.loads(f.read_text()).get("prompt", "")
            if p:
                out.append(clean(p)[:120])
        except (OSError, tomllib.TOMLDecodeError):
            continue
    return out


def from_codex(start, end, st):
    autos = codex_automation_prompts()
    for root in CODEX_DIRS:
        for f in recent(root, "*.jsonl", start):
            cwd = ""
            for line in lines(f, st):
                try:
                    if '"session_meta"' in line and not cwd:
                        p = json.loads(line).get("payload") or {}
                        cwd = p.get("cwd", "") or ""
                        # Subagents and guardian reviews are not Spencer.
                        if p.get("thread_source") not in (None, "user", "realtime_voice"):
                            break
                        continue
                    if '"role":"user"' not in line and '"role": "user"' not in line:
                        continue
                    o = json.loads(line)
                    p = o.get("payload") or {}
                    if not isinstance(p, dict) or p.get("type") != "message" or p.get("role") != "user":
                        continue
                    raw = " ".join(x.get("text", "") for x in p.get("content", []) if isinstance(x, dict))
                except (json.JSONDecodeError, AttributeError, TypeError):
                    st.errors += 1
                    continue
                st.user_lines += 1
                if raw.lstrip().startswith(("<recommended_plugins>", "<environment_context>", "# AGENTS.md",
                                            "<user_instructions>", "<permissions")) or injected(raw):
                    continue
                text = clean(raw)
                if any(a[:80] in text for a in autos):   # an automation run: "<id> <time> <prompt>"
                    continue
                t = parse_ts(o.get("timestamp"))
                if t and start <= t < end and human(text):
                    yield t, "codex", cwd, text


def from_grok(start, end, st):
    if not GROK_DIR.exists():
        return
    for f in GROK_DIR.glob("*/prompt_history.jsonl"):
        cwd = f.parent.name.replace("%2F", "/")
        started_by_agent: dict[str, bool] = {}
        for line in lines(f, st):
            try:
                o = json.loads(line)
                raw = o.get("prompt", "")
                sid = o.get("session_id", "")
            except (json.JSONDecodeError, AttributeError):
                st.errors += 1
                continue
            if not isinstance(raw, str):
                continue
            st.user_lines += 1
            text = clean(raw)
            if sid not in started_by_agent:   # judge each session by its first prompt
                started_by_agent[sid] = bool(SESSION_BRIEF.match(text)) or injected(raw)
            if started_by_agent[sid] or injected(raw):
                continue
            t = parse_ts(o.get("timestamp"))
            if t and start <= t < end and human(text):
                yield t, "grok", cwd, text


# ---------- digest ----------

def norm(s: str) -> str:
    return re.sub(r"\s+", " ", re.sub(r"[^a-z0-9 ]", " ", s.lower())).strip()


def main(argv: list[str]) -> int:
    start, end, title = window(argv)
    stats = {"claude": Stats(), "codex": Stats(), "grok": Stats()}
    by_proj: dict[str, list] = {}
    skipped_health = 0

    for src, fn in (("claude", from_claude), ("codex", from_codex), ("grok", from_grok)):
        for t, tool, cwd, text in fn(start, end, stats[src]):
            if not DESIGN.search(text):
                continue
            pid, name = project_of(cwd)
            if excluded(pid, name):
                skipped_health += 1
                continue
            items = by_proj.setdefault(name, [])
            n = norm(text)[:300]
            if any(difflib.SequenceMatcher(None, n, norm(q)[:300]).ratio() > 0.88 for _, _, q in items):
                continue   # the same message sent again is not a second ask
            q = text if len(text) <= QUOTE_CHARS else text[:QUOTE_CHARS].rsplit(" ", 1)[0] + " …"
            items.append((t.astimezone(), tool, q))
            stats[src].kept += 1

    broken = [s for s, st in stats.items() if st.files and not st.user_lines]
    total = sum(len(v) for v in by_proj.values())
    out = [
        f"# Design feedback digest {title}",
        "",
        f"Spencer's design-related messages from {start:%a %Y-%m-%d} to {end - dt.timedelta(seconds=1):%a %Y-%m-%d} "
        f"(local time): {total} quotes across {len(by_proj)} projects. Exact words, trimmed. Pasted text, "
        f"secrets, emails and phone numbers removed. Health projects skipped ({skipped_health} quotes).",
        "",
        "Sources: " + " · ".join(f"{s} {st.files} files, {st.user_lines} user lines, {st.kept} kept"
                                 + (f", {st.errors} unreadable" if st.errors else "") for s, st in stats.items()),
        "",
    ]
    if broken:
        out += [f"**WARNING:** {', '.join(broken)} had recent chat files but no readable user messages. "
                "The format may have changed, so this digest may be missing feedback.", ""]
    for name in sorted(by_proj, key=lambda k: -len(by_proj[k])):
        out += [f"## {name} ({len(by_proj[name])})", ""]
        out += [f"- {t:%a %b %d} · {tool}: \"{q}\"" for t, tool, q in sorted(by_proj[name])]
        out.append("")
    body = "\n".join(out)

    if "--stdout" in argv:
        print(body)
    else:
        dest = REPO / "feedback" / f"{title}.md"
        dest.parent.mkdir(exist_ok=True)
        dest.write_text(body, encoding="utf-8")
        print(f"wrote {dest} ({total} quotes, {len(by_proj)} projects)")
    if broken:
        print(f"digest may be broken: no readable user messages from {', '.join(broken)}", file=sys.stderr)
        return 2
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
