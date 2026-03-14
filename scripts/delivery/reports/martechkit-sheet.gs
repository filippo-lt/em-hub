/**
 * MarTechKit Roadmap — Google Sheets Generator (Interactive + Extensible)
 *
 * HOW TO USE:
 * 1. Go to https://sheets.new — creates a blank spreadsheet
 * 2. Click Extensions → Apps Script
 * 3. Delete all existing code, paste this entire script
 * 4. Save (Cmd+S), then Run ▶ → select buildMarTechKitRoadmap
 * 5. Approve permissions when prompted
 *
 * TO ADD A NEW PHASE:
 * 1. Right-click a phase row → Insert row above/below
 * 2. In column A, type  v10  or  v11  (sets the version + colour)
 * 3. In column B, type the phase name
 * 4. In column E, type the number of days
 * → Dates and bars update automatically
 *
 * TO EDIT DURATION: change any value in the yellow Days column (E).
 * All subsequent phase dates and bars cascade immediately.
 */

// ─── CONSTANTS ────────────────────────────────────────────────────────────────

const SHEET_NAME     = 'MarTechKit Roadmap';
const TAG_COL        = 1;   // A — 'v10' or 'v11' tag (white text, invisible)
const NAME_COL       = 2;   // B — phase name
const START_COL      = 3;   // C — start date (written by script)
const END_COL        = 4;   // D — end date (written by script)
const DAYS_COL       = 5;   // E — days (editable, yellow)
const GANTT_COL      = 7;   // G — first week bar column
const TOTAL_WEEKS    = 16;
const DATA_START_ROW = 11;  // first row the script scans for phase tags

const GANTT_WEEK_START = new Date(2026, 2, 16); // March 16, 2026 (Monday)

const C = {
  bg:          '#ffffff',
  surface:     '#f8f9fa',
  teal:        '#0f766e',
  tealBar:     '#14b8a6',
  tealSection: '#f0fdfa',
  purple:      '#6d28d9',
  purpleBar:   '#8b5cf6',
  purpleSection:'#f5f3ff',
  amber:       '#b45309',
  ink:         '#111827',
  muted:       '#9ca3af',
  dim:         '#4b5563',
  headerBg:    '#f1f3f5',
  border:      '#e5e7eb',
  editable:    '#fefce8',   // yellow — signals editable cell
};

// ─── onEdit TRIGGER ───────────────────────────────────────────────────────────
// Fires on any edit. Refreshes phases when Days (col E) or Tag (col A) changes.

function onEdit(e) {
  const sh = e.source.getActiveSheet();
  if (sh.getName() !== SHEET_NAME) return;

  const col = e.range.getColumn();
  const row = e.range.getRow();
  if (row < DATA_START_ROW) return;
  if (col !== DAYS_COL && col !== TAG_COL) return;

  // When a tag is set, also apply row styling
  if (col === TAG_COL) applyPhaseRowStyle(sh, row, e.range.getValue().toString().trim());

  SpreadsheetApp.flush();
  refreshPhases(sh);
}

// ─── CORE: scan sheet, recompute dates, redraw bars ───────────────────────────

function refreshPhases(sh) {
  const phases = scanPhaseRows(sh);
  if (phases.length === 0) return;

  const START = new Date(2026, 2, 16);
  let cursor  = new Date(START.getTime());

  phases.forEach(p => {
    const days = parseInt(sh.getRange(p.row, DAYS_COL).getValue(), 10) || 1;

    // Write start date
    sh.getRange(p.row, START_COL)
      .setValue(new Date(cursor.getTime()))
      .setNumberFormat('d MMM');

    // Compute and write end date
    const endDate = addWorkdays(cursor, days - 1);
    sh.getRange(p.row, END_COL)
      .setValue(new Date(endDate.getTime()))
      .setNumberFormat('d MMM');

    // Advance cursor to next workday
    cursor = nextWorkday(endDate);

    // Redraw Gantt bars for this row
    const barColor = p.version === 'v10' ? C.tealBar      : C.purpleBar;
    const rowBg    = p.version === 'v10' ? C.tealSection  : C.purpleSection;
    const start    = sh.getRange(p.row, START_COL).getValue();
    const end      = sh.getRange(p.row, END_COL).getValue();
    const barBgs   = [];
    for (let w = 0; w < TOTAL_WEEKS; w++) {
      const ws = weekStartDate(w);
      const we = new Date(ws.getTime()); we.setDate(we.getDate() + 6);
      barBgs.push(start <= we && end >= ws ? barColor : rowBg);
    }
    sh.getRange(p.row, GANTT_COL, 1, TOTAL_WEEKS).setBackgrounds([barBgs]);
  });

  // Update summary rows
  updateSummary(sh, phases);
}

// ─── Scan rows for phase tags ─────────────────────────────────────────────────

function scanPhaseRows(sh) {
  const lastRow = sh.getLastRow();
  const phases  = [];
  for (let r = DATA_START_ROW; r <= lastRow; r++) {
    const tag = sh.getRange(r, TAG_COL).getValue().toString().trim().toLowerCase();
    if (tag === 'v10' || tag === 'v11') {
      phases.push({ row: r, version: tag });
    }
  }
  return phases;
}

// ─── Apply styling when a tag is typed into col A ────────────────────────────

function applyPhaseRowStyle(sh, row, tag) {
  const v = tag.toLowerCase();
  if (v !== 'v10' && v !== 'v11') return;

  const rowBg    = v === 'v10' ? C.tealSection  : C.purpleSection;
  const color    = v === 'v10' ? C.teal         : C.purple;
  const barColor = v === 'v10' ? C.tealBar      : C.purpleBar;

  sh.setRowHeight(row, 28);
  sh.getRange(row, 1, 1, 6 + TOTAL_WEEKS).setBackground(rowBg);

  // Tag cell: coloured accent, white text (effectively hidden)
  sh.getRange(row, TAG_COL)
    .setBackground(color).setFontColor(color).setFontSize(8);

  // Name cell styling (if empty, leave placeholder)
  sh.getRange(row, NAME_COL)
    .setFontFamily('Arial').setFontSize(11).setFontColor(C.ink)
    .setVerticalAlignment('middle').setBackground(rowBg);

  // Date cells
  [START_COL, END_COL].forEach(col => {
    sh.getRange(row, col)
      .setFontFamily('Arial').setFontSize(10).setFontColor(C.dim)
      .setVerticalAlignment('middle').setBackground(rowBg)
      .setNumberFormat('d MMM');
  });

  // Days cell (yellow, editable)
  sh.getRange(row, DAYS_COL)
    .setFontFamily('Arial').setFontSize(11).setFontColor(color).setFontWeight('bold')
    .setHorizontalAlignment('center').setVerticalAlignment('middle')
    .setBackground(C.editable);

  // Spacer col
  sh.getRange(row, 6).setBackground(rowBg);

  // Gantt zone — empty until refreshPhases runs
  sh.getRange(row, GANTT_COL, 1, TOTAL_WEEKS).setBackground(rowBg);

  // Bottom border
  sh.getRange(row, 2, 1, 4 + TOTAL_WEEKS)
    .setBorder(null, null, true, null, null, null, C.bg, SpreadsheetApp.BorderStyle.SOLID);
}

// ─── Summary rows ────────────────────────────────────────────────────────────

function updateSummary(sh, phases) {
  const v10 = phases.filter(p => p.version === 'v10');
  const v11 = phases.filter(p => p.version === 'v11');

  // Find or create summary rows (we write them 2 rows below last phase)
  const lastPhaseRow = phases[phases.length - 1].row;
  const sumRow1 = lastPhaseRow + 2;
  const sumRow2 = lastPhaseRow + 3;

  // Ensure enough rows exist
  if (sh.getMaxRows() < sumRow2 + 5) sh.insertRowsAfter(sh.getMaxRows(), 10);

  const writeSumRow = (row, label, phasesArr, color) => {
    if (phasesArr.length === 0) return;
    const totalDays = phasesArr.reduce((s, p) => s + (parseInt(sh.getRange(p.row, DAYS_COL).getValue(), 10) || 0), 0);
    const endDate   = sh.getRange(phasesArr[phasesArr.length - 1].row, END_COL).getValue();

    sh.setRowHeight(row, 24);
    sh.getRange(row, 1, 1, 6 + TOTAL_WEEKS).setBackground(C.headerBg);
    sh.getRange(row, TAG_COL).setBackground(color);
    sh.getRange(row, NAME_COL).setValue(label)
      .setFontFamily('Arial').setFontSize(10).setFontColor(color).setFontWeight('bold')
      .setVerticalAlignment('middle').setBackground(C.headerBg);
    sh.getRange(row, START_COL).setValue('End:')
      .setFontFamily('Arial').setFontSize(9).setFontColor(C.muted).setVerticalAlignment('middle')
      .setBackground(C.headerBg);
    sh.getRange(row, END_COL).setValue(endDate)
      .setNumberFormat('d MMM yyyy')
      .setFontFamily('Arial').setFontSize(10).setFontColor(color).setFontWeight('bold')
      .setVerticalAlignment('middle').setBackground(C.headerBg);
    sh.getRange(row, DAYS_COL).setValue(totalDays + 'd total')
      .setFontFamily('Arial').setFontSize(9).setFontColor(C.dim).setVerticalAlignment('middle')
      .setBackground(C.headerBg);
  };

  // Thin divider above summary
  const divRow = lastPhaseRow + 1;
  sh.setRowHeight(divRow, 2);
  sh.getRange(divRow, 1, 1, 6 + TOTAL_WEEKS).setBackground(C.border);

  if (v10.length) writeSumRow(sumRow1, 'v1.0 — Face AI Pilot',          v10, C.teal);
  if (v11.length) writeSumRow(sumRow2, 'v1.1 — Typed Events & Rollout',  v11, C.purple);
}

// ─── DATE HELPERS ─────────────────────────────────────────────────────────────

function addWorkdays(date, n) {
  let d = new Date(date.getTime());
  let added = 0;
  while (added < n) {
    d.setDate(d.getDate() + 1);
    if (d.getDay() !== 0 && d.getDay() !== 6) added++;
  }
  return d;
}

function nextWorkday(date) {
  let d = new Date(date.getTime());
  d.setDate(d.getDate() + 1);
  while (d.getDay() === 0 || d.getDay() === 6) d.setDate(d.getDate() + 1);
  return d;
}

function weekStartDate(weekIndex) {
  const d = new Date(GANTT_WEEK_START.getTime());
  d.setDate(d.getDate() + weekIndex * 7);
  return d;
}

function columnLetter(col) {
  let letter = '';
  while (col > 0) {
    const rem = (col - 1) % 26;
    letter = String.fromCharCode(65 + rem) + letter;
    col = Math.floor((col - 1) / 26);
  }
  return letter;
}

// ─── BUILD FUNCTION ───────────────────────────────────────────────────────────

function buildMarTechKitRoadmap() {
  const ss = SpreadsheetApp.getActiveSpreadsheet();
  const sh = ss.getActiveSheet();
  sh.setName(SHEET_NAME);
  sh.clear();
  sh.clearConditionalFormatRules();

  const lastCol = columnLetter(6 + TOTAL_WEEKS);

  // ── Column widths ──
  sh.setColumnWidth(TAG_COL,  14);
  sh.setColumnWidth(NAME_COL, 185);
  sh.setColumnWidth(START_COL, 80);
  sh.setColumnWidth(END_COL,   80);
  sh.setColumnWidth(DAYS_COL,  52);
  sh.setColumnWidth(6, 14);
  for (let w = 0; w < TOTAL_WEEKS; w++) sh.setColumnWidth(GANTT_COL + w, 52);

  // ── Full background ──
  sh.getRange(1, 1, 60, 7 + TOTAL_WEEKS).setBackground(C.bg);

  // ── Title ──
  sh.setRowHeight(1, 8);
  sh.setRowHeight(2, 44);
  sh.setRowHeight(3, 22);
  sh.setRowHeight(4, 3);

  sh.getRange(`B2:${lastCol}2`).merge();
  sh.getRange('B2').setValue('MarTechKit — Swift Package Initiative')
    .setFontFamily('Arial').setFontSize(20).setFontWeight('bold').setFontColor(C.ink)
    .setVerticalAlignment('middle');

  sh.getRange(`B3:${lastCol}3`).merge();
  sh.getRange('B3')
    .setValue('Centralising Amplitude · RevenueCat · AppsFlyer   ·   Owner: Victor Jalencas   ·   Pilot: Face AI   ·   Kickoff: 15–16 Mar 2026')
    .setFontFamily('Arial').setFontSize(10).setFontColor(C.dim).setVerticalAlignment('middle');

  sh.getRange(`A4:${lastCol}4`).setBackground(C.teal); // accent divider

  // ── Column headers ──
  [5, 6, 7].forEach(r => sh.setRowHeight(r, 6));
  sh.setRowHeight(8, 22);
  sh.setRowHeight(9, 20);
  sh.setRowHeight(10, 6);
  sh.getRange(8, 1, 3, 6 + TOTAL_WEEKS).setBackground(C.headerBg);

  [['', 'Phase', 'Start', 'End', 'Days ✎']].forEach(row => {
    row.forEach((h, i) => {
      sh.getRange(8, 1 + i).setValue(h)
        .setFontFamily('Arial').setFontSize(9).setFontWeight('bold').setFontColor(C.muted)
        .setVerticalAlignment('middle');
    });
  });
  sh.getRange(8, DAYS_COL).setFontColor(C.amber); // highlight "Days ✎" as editable

  // ── Week date headers ──
  for (let w = 0; w < TOTAL_WEEKS; w++) {
    const d = weekStartDate(w);
    const isMonthBoundary = d.getDate() <= 7;
    sh.getRange(9, GANTT_COL + w)
      .setValue(d)
      .setNumberFormat(isMonthBoundary ? 'MMM d' : 'd')
      .setFontFamily('Arial').setFontSize(8)
      .setFontColor(isMonthBoundary ? C.dim : C.muted)
      .setFontWeight(isMonthBoundary ? 'bold' : 'normal')
      .setHorizontalAlignment('center').setVerticalAlignment('middle');
  }

  // ── Phase data ──
  const phases = [
    // v1.0
    { name: 'Setup & Design',      days: 4,  version: 'v10', desc: 'Package skeleton, key storage format, read existing SDK integrations in Face AI' },
    { name: 'Core Build',          days: 7,  version: 'v10', desc: 'Unified init, MarTechConfiguration, ID sharing, RevenueCat anonymous init' },
    { name: 'Face AI Integration', days: 7,  version: 'v10', desc: 'Replace direct SDK calls with MarTechKit, test in dev + staging' },
    { name: 'Hardening & Docs',    days: 4,  version: 'v10', desc: 'Fix integration issues, write migration guide for other apps, finalise v1.0' },
    // v1.1
    { name: 'Build Typed Events',  days: 7,  version: 'v11', desc: 'MarTechEvent enum with typed logging API — event taxonomy already defined by MarTech' },
    { name: 'Rollout Planning',    days: 7,  version: 'v11', desc: 'Align with MarTech on multi-app rollout sequence, prepare migration guide' },
  ];

  let currentRow = DATA_START_ROW;
  let prevVersion = null;

  phases.forEach(p => {
    // Section header when version changes
    if (p.version !== prevVersion) {
      const label    = p.version === 'v10' ? 'v1.0 — Face AI Pilot' : 'v1.1 — Typed Events & Multi-App Rollout';
      const color    = p.version === 'v10' ? C.teal   : C.purple;
      const sectionBg = p.version === 'v10' ? C.tealSection : C.purpleSection;
      if (prevVersion !== null) { sh.setRowHeight(currentRow, 8); currentRow++; } // spacer
      sh.setRowHeight(currentRow, 22);
      sh.getRange(currentRow, 1, 1, 6 + TOTAL_WEEKS).setBackground(sectionBg);
      sh.getRange(currentRow, TAG_COL).setBackground(color);
      sh.getRange(currentRow, NAME_COL).setValue(label)
        .setFontFamily('Arial').setFontSize(9).setFontWeight('bold').setFontColor(color)
        .setVerticalAlignment('middle').setBackground(sectionBg);
      currentRow++;
      prevVersion = p.version;
    }

    // Write tag (white-on-matching-bg — visually hidden, read by script)
    const color    = p.version === 'v10' ? C.teal        : C.purple;
    const rowBg    = p.version === 'v10' ? C.tealSection : C.purpleSection;
    const barColor = p.version === 'v10' ? C.tealBar     : C.purpleBar;

    sh.setRowHeight(currentRow, 28);
    sh.getRange(currentRow, 1, 1, 6 + TOTAL_WEEKS).setBackground(rowBg);

    sh.getRange(currentRow, TAG_COL).setValue(p.version)
      .setBackground(color).setFontColor(color).setFontSize(8); // invisible tag

    sh.getRange(currentRow, NAME_COL).setValue(p.name).setNote(p.desc)
      .setFontFamily('Arial').setFontSize(11).setFontColor(C.ink)
      .setVerticalAlignment('middle').setBackground(rowBg);

    sh.getRange(currentRow, DAYS_COL).setValue(p.days)
      .setFontFamily('Arial').setFontSize(11).setFontColor(color).setFontWeight('bold')
      .setHorizontalAlignment('center').setVerticalAlignment('middle')
      .setBackground(C.editable);

    sh.getRange(currentRow, START_COL).setNumberFormat('d MMM')
      .setFontFamily('Arial').setFontSize(10).setFontColor(C.dim)
      .setVerticalAlignment('middle').setBackground(rowBg);
    sh.getRange(currentRow, END_COL).setNumberFormat('d MMM')
      .setFontFamily('Arial').setFontSize(10).setFontColor(C.dim)
      .setVerticalAlignment('middle').setBackground(rowBg);
    sh.getRange(currentRow, 6).setBackground(rowBg);

    sh.getRange(currentRow, 2, 1, 4 + TOTAL_WEEKS)
      .setBorder(null, null, true, null, null, null, C.bg, SpreadsheetApp.BorderStyle.SOLID);

    currentRow++;
  });

  // Compute dates + draw bars for initial state
  refreshPhases(sh);

  // ── Key Decisions ──
  const decisionsStartRow = currentRow + 4;
  sh.setRowHeight(decisionsStartRow - 2, 8);
  writeSectionLabel(sh, decisionsStartRow - 1, 'KEY DESIGN DECISIONS', TOTAL_WEEKS);
  sh.setRowHeight(decisionsStartRow - 1, 20);

  [
    { icon: '👤', title: 'User Identity',  status: 'v1.0 Scoped',       body: 'RevenueCat anonymous mode for v1.0. Architecture leaves door open for identified users when auth lands. Single setUser(id:) syncs identity across all three SDKs.' },
    { icon: '⚙️', title: 'CI/CD Pipeline', status: 'Discuss w/ Victor',  body: 'GitHub Actions runs tests on PR — keep it simple. Full release automation (SPM tag publishing) is a v1.1+ concern.' },
  ].forEach((d, i) => {
    const r = decisionsStartRow + i * 2;
    sh.setRowHeight(r, 58);
    sh.getRange(r, 1, 1, 6 + TOTAL_WEEKS).setBackground(C.surface);
    sh.getRange(r, NAME_COL, 1, 4).merge();
    sh.getRange(r, NAME_COL)
      .setValue(`${d.icon}  ${d.title}  [${d.status}]\n${d.body}`)
      .setFontFamily('Arial').setFontSize(10).setFontColor(C.dim)
      .setVerticalAlignment('top').setWrap(true).setBackground(C.surface);
    sh.setRowHeight(r + 1, 5);
  });

  // ── Open Questions ──
  const qStartRow = decisionsStartRow + 6;
  writeSectionLabel(sh, qStartRow, 'OPEN QUESTIONS FOR MARTECH  (David Sanchez)', TOTAL_WEEKS);
  sh.setRowHeight(qStartRow, 20);

  [
    ['01', 'Event naming conventions',         'Does MarTech have a naming scheme for Amplitude events? Shapes the v1.1 MarTechEvent catalogue.'],
    ['02', 'SDK key ownership long-term',       'No one formally owns the API keys today. Needs a clear owner before scaling beyond Face AI.'],
    ['03', 'Rollout sequencing beyond Face AI', 'After the pilot, which app is next? Does MarTech have a priority order or does mobile decide?'],
    ['04', 'Other features',                   'Any additional capabilities MarTech wants to consolidate into the package beyond current scope?'],
  ].forEach(([num, title, body], i) => {
    const r = qStartRow + 1 + i;
    sh.setRowHeight(r, 36);
    sh.getRange(r, 1, 1, 6 + TOTAL_WEEKS).setBackground(C.surface);
    sh.getRange(r, TAG_COL).setValue(num)
      .setFontFamily('Arial').setFontSize(9).setFontColor(C.amber)
      .setVerticalAlignment('middle').setHorizontalAlignment('center')
      .setBackground(C.surface);
    sh.getRange(r, START_COL, 1, 3 + TOTAL_WEEKS).merge();
    sh.getRange(r, START_COL).setValue(`${title} — ${body}`)
      .setFontFamily('Arial').setFontSize(10).setFontColor(C.dim)
      .setVerticalAlignment('middle').setWrap(true).setBackground(C.surface);
    sh.getRange(r, NAME_COL).setBackground(C.surface);
    sh.getRange(r, TAG_COL, 1, 5 + TOTAL_WEEKS)
      .setBorder(null, null, true, null, null, null, C.bg, SpreadsheetApp.BorderStyle.SOLID);
  });

  // ── Freeze ──
  sh.setFrozenRows(9);
  sh.setFrozenColumns(2);
  sh.setTabColor(C.teal);
  ss.rename('MarTechKit Roadmap — Mar 2026');

  SpreadsheetApp.getUi().alert('✅ Done!\n\nTo add a phase: insert a row, type v10 or v11 in column A, then fill in name + days.\nTo change duration: edit any yellow Days cell.');
}

// ─── HELPERS ──────────────────────────────────────────────────────────────────

function writeSectionLabel(sh, row, label, totalWeeks) {
  sh.getRange(row, 1, 1, 6 + totalWeeks).setBackground(C.bg);
  sh.getRange(row, NAME_COL).setValue(label)
    .setFontFamily('Arial').setFontSize(9).setFontWeight('bold').setFontColor(C.muted)
    .setVerticalAlignment('middle');
  sh.getRange(row, NAME_COL, 1, 4 + totalWeeks)
    .setBorder(null, null, true, null, null, null, C.border, SpreadsheetApp.BorderStyle.SOLID_MEDIUM);
}
