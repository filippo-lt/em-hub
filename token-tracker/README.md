# Claude Code Token Tracker

A Mac menu bar app that shows what your Claude Code usage **would** cost on
standard token-based API pricing — even though the Max plan doesn't bill you per
token. Plus per-session, per-model, per-project, and weekly breakdowns.

## How it works

Claude Code writes a full local log of every session as JSONL under
`~/.claude/projects/**/*.jsonl`. Each assistant turn records exact token counts
(`input`, `output`, `cache_read`, `cache_creation` — with the 5-minute / 1-hour
cache-write split). No network calls, no API access, no plan-side telemetry —
it's all already on disk.

Two pieces:

- **`cc_cost.py`** — parses the logs and prices each token bucket separately
  (this matters: cache reads are ~0.1× input and dominate the token count, so a
  naïve `input+output` estimate is wildly wrong). It's the single source of
  truth for parsing + pricing, and runs standalone.
- **`app/`** — a SwiftUI `MenuBarExtra` app that shells out to
  `cc_cost.py --json` every 30s and renders the result in the menu bar.

```
menu bar:  $ 5.66          ← this week's hypothetical cost
dropdown:  Today / This week / This month / All time
           By model · By project · By week
```

## Try the script alone first

```sh
python3 token-tracker/cc_cost.py          # pretty breakdown
python3 token-tracker/cc_cost.py --json   # what the app consumes
```

## Run the menu bar app

Requirements: **macOS 13+**, a Swift toolchain (Xcode or Command Line Tools),
and `python3` (the system `/usr/bin/python3` is fine).

```sh
cd token-tracker/app
swift run
```

A `$` item appears in the menu bar. Click it for the full breakdown. `swift run`
keeps it resident; quit from the dropdown or with Ctrl-C in the terminal.

## Customizing

- **Pricing / models** — edit the `PRICING` table at the top of `cc_cost.py`.
  Families are matched by substring (`opus` / `sonnet` / `haiku`), so version
  suffixes resolve automatically.
- **Script location** — the app finds `cc_cost.py` relative to its own source;
  override with `CC_COST_SCRIPT=/path/to/cc_cost.py swift run`.
- **Refresh interval** — `refreshInterval` in `UsageStore.swift`.
- **Headline metric** — the menu bar shows `thisWeek`; change `menuTitle` in
  `UsageStore.swift` to `today` or `total` if you prefer.

## Analysis ideas

The logs carry, per turn: token counts (4 buckets), `model`, `cwd` (project),
`gitBranch`, `sessionId`, and a timestamp. That's enough for a lot of lenses.
Items marked ✅ are already emitted by `cc_cost.py --json`; the rest are small
additions.

**Time**
- ✅ **By day** — daily spend trend; 7- and 30-day rolling average; a
  GitHub-style calendar heatmap; active-day streaks.
- ✅ **By week** — week-over-week delta; is this week tracking above or below
  your running average; burn rate.
- ✅ **By day of week** — which weekdays you grind; weekday vs weekend split
  (a quiet overtime signal).
- ✅ **By hour of day** — when you actually work; peak hours; late-night /
  early-morning sessions.
- **Hour × day-of-week heatmap** — the "when do I code with CC" grid; the single
  most informative view once there's a few weeks of data.

**Work breakdown**
- ✅ **By project** (`cwd`) — which repos cost most; share of total; per-project
  trend over time.
- **By git branch** (`gitBranch`) — cost per feature/PR. Attribute spend to the
  thing you were building, not just the repo.
- ✅ **By model** — Opus/Sonnet/Haiku mix; cost share vs token share; are you
  reaching for Opus when Haiku would do?
- ✅ **By session** — cost distribution (median vs the heavy tail); a
  "most expensive sessions" leaderboard; sessions per day.

**Efficiency & economics**
- **Cache efficiency** — `cache_read / (input + cache_read)`. Claude Code leans
  hard on caching; this shows how well it's working and lets you estimate the $
  the cache *saved* vs paying full input price.
- **Output / input ratio** — how much you generate vs context you feed in.
- **Tokens per session over time** — are sessions getting heavier (context
  bloat)?
- **Break-even vs the Max plan** — compare the hypothetical monthly token cost to
  the flat subscription. Are you getting your money's worth, and at what usage
  would per-token pricing actually be cheaper? (The headline "gotcha" metric.)
- **Projected monthly run-rate** — extrapolate from the rolling daily average.
- **Web tool usage** — `server_tool_use` web_search / web_fetch counts per
  session (and their cost, if you price them).

**Signals**
- **Anomaly flags** — a session or day N× your median → catch runaway loops or
  unusually heavy work early.
- **Model-mix drift** — are you trending toward cheaper or pricier models over
  time?

## Activity states & animation

The menu bar glyph reflects what Claude Code is doing right now, inferred from
how recently any session log was written (a cheap mtime scan every 2s — no
parsing):

| State | Menu bar | Meaning |
|---|---|---|
| **Working** | green, braille spinner `⠋⠙⠹…` | a log was written in the last ~6s |
| **Waiting for input** | orange, blinking `●`/`○` | recent activity (<10 min) but not actively writing |
| **Idle** | gray, static `$` | nothing for 10+ min, or no sessions |

It's a heuristic: it can't perfectly distinguish "awaiting your message" from
"awaiting a permission prompt" (both look like *recent but not writing*). The
windows are tunable — `workingWindow`, `idleWindow`, and the animation `frame`
rate live in `UsageStore.swift`. The dropdown header shows the same state as a
colored dot + label.

## Notes & possible next steps

- **Dependency tradeoff:** the app shells out to Python so there's one place that
  owns parsing + pricing. Cost: it needs `python3` at runtime. A pure-Swift port
  (parse the JSONL natively, zero dependencies) is a clean follow-up if you want
  a fully self-contained `.app`.
- **Packaging:** `swift run` is enough for daily personal use. To ship a
  double-clickable `.app` that launches at login, wrap it in an Xcode app target
  (set `LSUIElement` / Application is agent = YES) or bundle the SwiftPM output.
- Pricing is **hypothetical** — the Max plan is a flat subscription; this is a
  "what if I were paying per token" lens, useful for spotting heavy sessions and
  comparing projects, not an actual bill.
