# App Portfolio Spreadsheet — Setup & Usage

Starter files for the App Portfolio Investment Framework spreadsheet (see `context/app-portfolio-framework.md` for the framework itself).

The live working file is a Google Sheet, not version-controlled. These CSVs are the canonical starter structure — when the Sheet structure changes meaningfully, update the CSVs in this folder.

---

## Files

| File | Purpose | Becomes which tab |
|---|---|---|
| `portfolio-dashboard.csv` | At-a-glance view, 1 row per app | **Portfolio Dashboard** (Tab 1) |
| `app-template.csv` | P&L per app — rows = lines, columns = months. Populated with AI Design as the worked example | **AI Design** (Tab 2), then duplicate + clear for each new app |
| `kill-triggers.csv` | Pre-agreed triggers across portfolio | **Kill Triggers** (final tab) |

---

## Setup (one-time, ~20 min)

### 1. Create the Sheet
- New Google Sheet → name it `App Portfolio — 2026`
- Share with David (Editor)

### 2. Import the three tabs
For each CSV:
- `File → Import → Upload → [file]`
- Import location: **Insert new sheet**
- Separator: Comma
- Convert text to numbers: **Yes** (important — otherwise formulas break)

Rename the resulting tabs to `Portfolio Dashboard`, `AI Design`, `Kill Triggers`.

### 3. Wire up the dashboard formulas
On the **Portfolio Dashboard** tab, replace the static numbers in the AI Design row with references to the AI Design tab. Example formulas (adjust cell refs to match your import):

| Dashboard column | Formula |
|---|---|
| Monthly burn (€) | `='AI Design'!G16` *(or whichever column is current month)* |
| Monthly revenue (€) | `='AI Design'!G18` |
| Net (€) | `='AI Design'!G24` |
| CAC (€) | `='AI Design'!G20` |
| LTV (€) | `='AI Design'!G21` |
| LTV/CAC | `='AI Design'!G22` |

Use a named range (e.g. `current_month_col`) if you want to roll forward monthly without editing each formula.

### 4. Conditional formatting

**LTV/CAC column (Dashboard):**
- Red if `<1`
- Amber if `>=1 and <3`
- Green if `>=3`

**Trigger status column (Dashboard + each App tab):**
- Red = trigger fired or imminent
- Amber = on watch
- Green = healthy
- "Pending sign-off" → grey background

**Net (€) column (Dashboard + each App tab):**
- Negative → red text
- Positive → green text

### 5. Lock the structure of the App template tab
Once `AI Design` is shaped the way you want it:
- Note the exact row numbers for `Total monthly burn`, `MRR`, `Net`, `CAC`, `LTV` — those are the rows the Dashboard pulls from
- Never reorder or delete rows in any App tab — only blank values out
- For each new app: duplicate the AI Design tab → rename → clear the data cells (keep the row structure)

---

## Monthly workflow (~30 min, last Friday of the month)

1. Update each App tab — current month column only:
   - Engineering / infra / AI tooling costs (yours)
   - Marketing + revenue numbers (from PMs — request 5 working days ahead)
2. Dashboard auto-updates via formulas
3. Check kill triggers — any fired? Any imminent?
4. Spot-check 2×2 position — has any app moved cell?
5. Add row to the App tab's bottom notes block if anything changed
6. Bring to next 1:1

---

## Quarterly workflow (last week of the quarter)

1. Full portfolio review with David
2. Tier reassignment per app
3. Re-set kill triggers — sign-off dated in `Kill Triggers` tab
4. Budget reallocation discussion
5. Update the framework doc if scope / inputs have shifted

---

## Gotchas

- **CSV import strips formulas.** The `=SUM(...)` and `=G21/G20` cells in `app-template.csv` will import as text. Re-type them after import, or paste each formula manually. Annoying but one-time.
- **Row numbers shift if you reorder anything.** Lock the row order in App tabs before wiring Dashboard formulas.
- **Currency formatting:** apply to cost / revenue columns after import (`Format → Number → Currency`).
- **Don't delete the [INVESTMENT] / [RETURN] / [NET] / [STATUS] section header rows** — they're load-bearing for visual scanning and for the dashboard's row-reference logic.
- **Built-but-not-updated is worse than not built.** Monthly fill-in is non-optional once this exists — if the cadence slips, David sees a rotting tool every 1:1.
