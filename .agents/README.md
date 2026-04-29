# em-hub/.agents

Single source of truth for em-hub's skills, subagents, and rules. Both Claude Code (`.claude/`) and Cursor (`.cursor/`) consume these via symlinks.

## Layout

```
.agents/
├── skills/<name>/SKILL.md   # SKILL.md format, works in both tools
├── agents/<name>.md          # Claude Code subagents
└── rules/<name>.mdc          # Cursor rules
```

## Symlink convention

```
.claude/skills/<name>     → ../../.agents/skills/<name>
.cursor/skills/<name>     → ../../.agents/skills/<name>
.claude/agents/<x>.md     → ../../.agents/agents/<x>.md
.cursor/rules/<x>.mdc     → ../../.agents/rules/<x>.mdc
```

## Adding a new skill

```bash
mkdir -p .agents/skills/<name>
# write SKILL.md with YAML frontmatter (name, description)
ln -s ../../.agents/skills/<name> .claude/skills/<name>
ln -s ../../.agents/skills/<name> .cursor/skills/<name>
```

## Scope

This is **EM tooling** that depends on this repo's `people/`, `teams/`, `context/`, `metrics/` directories. For machine-wide / cross-project tooling (mostly SE work), see `~/Projects/ai-toolkit/`.
