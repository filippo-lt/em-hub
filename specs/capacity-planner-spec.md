# Capacity Planner — Product Specification

**Version:** 1.0  
**Status:** Implemented  

---

## Overview

A browser-based capacity planning tool visualised as a Gantt chart. Users can organise work items under named sections (people, teams, workstreams), schedule them on a scrollable day-level timeline, and track their progress through states. Data can be exported and re-imported as JSON.

---

## Layout

The interface is divided into two panels, rendered side by side and sharing a vertical scroll axis.

### Left Panel — Labels

- Fixed width, non-horizontally-scrollable.
- Contains a header row labelled **TEAM / TASKS**.
- Displays the list of sections and their items in the same vertical order and row heights as the timeline panel, so rows stay perfectly aligned.
- Scrolls vertically in sync with the timeline panel.

### Right Panel — Timeline

- Horizontally scrollable; stretches to accommodate the full planning horizon.
- Contains a sticky header (month row + day row) that remains visible during vertical scroll.
- Rows align with the left panel.
- Supports free horizontal scrolling (mouse wheel, trackpad, or drag).

### Toolbar

- Persistent bar at the top of the full viewport.
- Contains: app title, **+ Section**, **⬦ Milestone**, state legend, **↓ Export**, **↑ Import**.

---

## Timeline

### Horizon

- Total rendered span: approximately 10 months (~300 days).
- Start: 30 days before today's date.
- End: ~270 days after today.
- On load, the timeline scrolls to centre on today.

### Header

Two rows, sticky at the top of the timeline panel:

1. **Month row** — displays month + year labels, each spanning the width of days in that month.
2. **Day row** — displays the day-of-month number for each day. Today's date is highlighted with a distinct background and bold weight.

### Grid

- Each day occupies a fixed-width column (34px).
- Vertical grid lines separate each day.
- Weekend columns (Saturday + Sunday) have a subtly different background colour.

### Today Marker

- A vertical line spanning the full timeline height, positioned at the centre of today's column.
- A **TODAY** label floats near the top of the line.
- Rendered above the grid lines and task bars.

---

## Sections

Sections are the primary grouping unit. They can represent people, teams, workflows, or any other logical grouping.

### Behaviour

- Each section renders as a row in both panels — a header band in the left panel and a matching band in the timeline.
- Sections can be **collapsed** to hide their items, reducing visual clutter. The collapse state is toggled by an arrow icon (▶/▼).
- Sections can be **reordered** up or down via arrow buttons.
- Sections can be **renamed** by double-clicking the name (inline edit).
- Sections can be **deleted** (with immediate removal of all contained items).
- New sections are added via the toolbar button and appear at the bottom of the list.

---

## Items (Tasks)

Items represent individual work tasks within a section.

### Properties

| Property | Type | Description |
|----------|------|-------------|
| `name` | string | Display label for the task |
| `startDay` | integer | Start date expressed as days since Unix epoch |
| `endDay` | integer | End date (exclusive), same unit |
| `color` | hex string | Base color for the task bar |
| `state` | enum | `planned`, `running`, or `completed` |

### Duration

Duration in days is derived as `endDay − startDay`. A duration badge (e.g. `14d`) is displayed inside the bar when the bar is wide enough.

### Left Panel Controls (per item)

- Color dot — reflects current state color.
- Inline-editable name (double-click to edit).
- State icon — cycles through states on click: `○ planned → ◉ running → ✓ completed → ○ planned`.
- Color picker — native browser color input to override the auto-assigned color.
- Up/Down arrows — reorder the item within its section, or across sections when at the boundary.
- Delete button.

### Item Bar (in timeline)

- Rendered as a colored rectangle spanning `startDay` to `endDay` within the row.
- Item name is displayed inside the bar (truncated with ellipsis if the bar is too narrow).
- Duration badge displayed on the right when bar width allows.
- Two resize handles (darker 5px strips) on the left and right edges for resizing.

### Dragging

- **Move:** drag the bar body to shift the entire item. Start and end dates both shift by the same delta.
- **Resize left edge:** drag to change the start date without affecting the end date.
- **Resize right edge:** drag to change the end date without affecting the start date.
- All dragging snaps to day boundaries (integer days only).
- Minimum duration: 1 day.

---

## States

Each item has one of three states. The state affects the visual rendering of the bar color.

| State | Icon | Color treatment | Opacity |
|-------|------|-----------------|---------|
| `planned` | ○ | Desaturated, lightened | 48% |
| `running` | ◉ | Full base color | 100% |
| `completed` | ✓ | Darkened, reduced saturation | 72% |

State color transformations are computed from the item's base color using HSL manipulation:

- **Planned:** saturation × 0.28, lightness × 1.22 (capped at 88%)
- **Completed:** saturation × 0.55, lightness × 0.62
- **Running:** base color unchanged

---

## Colors

- When a new item is created, a color is auto-assigned from a fixed 10-color palette.
- The user can override the color at any time via the color picker input in the left panel.
- The color picker is the browser's native `<input type="color">` element.

**Default palette:**

`#5B8EF7` · `#F7724F` · `#4FD6A6` · `#B47BFA` · `#F7C34F` · `#4FC9F7` · `#F74F8E` · `#8CF74F` · `#FA9E4F` · `#4FF7D6`

---

## Milestones

Milestones are global date markers that span the full height of the timeline.

### Properties

| Property | Type | Description |
|----------|------|-------------|
| `label` | string | Short descriptive name |
| `day` | integer | Date expressed as days since Unix epoch |

### Rendering

- A vertical amber line spans the full timeline height at the milestone date.
- A label tag (⬦ + text) floats at the top of the line.
- Milestones appear above all section/item rows.

### Interactions

- **Add:** click the **⬦ Milestone** toolbar button → modal appears with date picker and label field. Confirm with the **Add Milestone** button or by pressing Enter.
- **Edit/Delete:** click a milestone label tag on the timeline → modal appears with editable date and label fields, plus a **Delete** button.

---

## Data Persistence

Data is **not** auto-saved. All state exists in memory during the session.

### Export

- Clicking **↓ Export** downloads a `capacity-plan.json` file.
- The JSON contains the full application state: sections (with items) and milestones.

### Import

- Clicking **↑ Import** opens a file picker filtered to `.json`.
- A valid file replaces the current state (sections and milestones) entirely.
- Invalid JSON shows a browser alert.

### File Format

```json
{
  "sections": [
    {
      "id": "abc123",
      "name": "Alice Chen",
      "collapsed": false,
      "items": [
        {
          "id": "def456",
          "name": "UI Design",
          "startDay": 20150,
          "endDay": 20168,
          "color": "#5B8EF7",
          "state": "running"
        }
      ]
    }
  ],
  "milestones": [
    {
      "id": "ghi789",
      "day": 20180,
      "label": "Beta Launch"
    }
  ]
}
```

All dates are stored as integer day offsets from the Unix epoch (UTC midnight), computed as `Math.floor(Date.UTC(...) / 86400000)`.

---

## Inline Editing

Names for sections and items are editable in-place:

- Double-click the name to enter edit mode.
- Press **Enter** or click outside to confirm.
- Press **Escape** to cancel and revert.
- Edit renders as a single-line text input replacing the label span.

---

## Scroll Synchronisation

- The left panel and timeline panel share a synchronised vertical scroll position.
- Scrolling either panel updates the other via a `ref`-based sync with a reentrancy guard (`requestAnimationFrame`).

---

## Constraints & Limits

- Timeline horizon is fixed at 300 days from the start date. Scroll beyond this range is not supported.
- Minimum item duration is 1 day.
- No undo/redo support.
- No multi-select or bulk operations.
- Items cannot span across sections; each item belongs to exactly one section.
- No dependency arrows between items.

---

## Future Considerations

- Undo/redo stack
- Drag items between sections directly on the timeline
- Dependency links between items
- Week/month zoom levels for the x-axis
- Auto-save to `localStorage`
- Multi-user / shared state via backend sync
- Resource utilisation heatmap overlay
