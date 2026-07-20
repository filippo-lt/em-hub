# Cowork Projects — Setup Guide

Four Cowork Projects sitting on top of your existing EM Hub. This does **not**
restructure the hub — the hub stays one integrated system. Each work project is
a *lens*: same folder, focused instructions.

## The 4 projects

| Project | Attach this folder | Instructions file |
| ------- | ------------------ | ----------------- |
| **EM Hub / Team** | `~/Projects/em-hub` | `projects/01-team.md` |
| **Q3 Launches & M&A** | `~/Projects/em-hub` | `projects/02-q3-launches-m-and-a.md` |
| **Hiring** | `~/Projects/em-hub` | `projects/03-hiring.md` |
| **Personal / Home** | `~/Projects/personal-home` | `personal-home/PROJECT.md` |

The three work projects share **one folder** and one `CLAUDE.md` (your master
context-loading protocol). The only thing that differs between them is the
custom instructions you paste in.

## How each instructions file is laid out

Every file has exactly two parts:

- **① CUSTOM INSTRUCTIONS** — a single fenced ```text block. Copy **only this
  block** into the project's *custom instructions* field. Nothing above or below it.
- **② SETUP** — a checklist for you (folder to attach, connectors to authorize).
  Do **not** paste this into Cowork.

## Do I upload files, or point to the folder?

**Point to the folder — do not upload files.** A Cowork project reads the whole
attached folder live every session, including the `CLAUDE.md` at its root.
Uploading individual files would only create stale copies that drift from the
real hub. Reserve uploads for genuine one-offs that don't live in a connected
folder.

## Wiring each one up

For each project: create it in Cowork → attach the folder from the table →
paste the **① block** from its instructions file → authorize the connectors its
**② section** lists. (Several connectors currently need re-authorization.)

## Maintenance

The **① blocks** are the only thing Claude reads each chat — keep them tight and
edit them as your focus shifts. Master conventions (naming, context-loading
protocol, behavioral standards) live once in `em-hub/CLAUDE.md` and are inherited
by all three work projects; don't duplicate them into the blocks.
