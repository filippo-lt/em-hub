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
