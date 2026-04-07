# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this repository is

Two things in one:

1. **Original work** — Claude Code extensions I've authored: skills, subagents, and slash commands. These live at the top level of `skills/`, `agents/`, and `commands/` and are installed by copying a single file or folder into `~/.claude/` (or a project's `.claude/`).
2. **A curated index** — a section of `README.md` that links to third-party Claude Code extensions I use and recommend. These are **not** vendored into this repo; they remain in their upstream repositories.

If you are editing files here, you are editing my own work. If a user needs a third-party extension from the curated list, follow its link in `README.md` to the upstream source.

## Directory layout

```
<repo-root>/
├── skills/              one subdirectory per skill, each containing SKILL.md
│   └── <skill-name>/SKILL.md
├── agents/              one markdown file per subagent
│   └── <agent-name>.md
├── commands/            one markdown file per slash command
│   └── <command-name>.md
├── LICENSE              Apache-2.0 — covers every file in this repo
├── CLAUDE.md            this file
├── README.md            overview + curated index of third-party extensions I use
└── .gitignore
```

There is no `mine/` vs `third-party/` split — everything under `skills/`, `agents/`, and `commands/` is my original work.

## File conventions per type

### Skills

Follow the Agent Skills open standard (https://agentskills.io/specification). Each skill is a folder at `skills/<skill-name>/` containing a `SKILL.md`. The folder name must equal the `name` frontmatter field. Required frontmatter: `name`, `description`. Optional portable fields: `license`, `compatibility`, `metadata`, `allowed-tools`. Claude Code also recognises `argument-hint`, `disable-model-invocation`, `user-invocable`, `model`, `effort`, `context`, `agent`, `hooks`, `paths`, `shell`. See https://code.claude.com/docs/en/skills.md.

Install:

    cp -r skills/<skill-name> ~/.claude/skills/<skill-name>

### Subagents

A single markdown file at `agents/<agent-name>.md`. The file name (without `.md`) must equal the agent's `name`. Typical frontmatter: `name`, `description`, optional `model`, `tools`. See https://code.claude.com/docs/en/sub-agents.md.

Install:

    cp agents/<agent-name>.md ~/.claude/agents/<agent-name>.md

### Slash commands

A single markdown file at `commands/<command-name>.md`. The file name becomes the slash command (`my-command.md` → `/my-command`). Optional frontmatter: `description`, `allowed-tools`, `argument-hint`, `disable-model-invocation`. See https://code.claude.com/docs/en/slash-commands.md.

Install:

    cp commands/<command-name>.md ~/.claude/commands/<command-name>.md

## Adding an extension I authored

1. Create the file or folder at its canonical location with valid frontmatter.
2. Ensure the file or folder name matches the `name` frontmatter field.
3. Do **not** add a per-file SPDX header — the root `LICENSE` covers every file in the repo.

## Adding to the curated list in `README.md`

The `## Extensions I use` section of `README.md` links to third-party extensions I've personally vetted. To add a new one:

1. **Do not copy the file into this repo.** Vendoring is deliberately not done — it creates licensing-compliance overhead and a drift problem that isn't worth solving for a personal library.
2. Add a bullet under the appropriate subsection (`### Skills`, `### Subagents`, or `### Slash commands`) with:
   - Extension name in bold, followed by author and SPDX license ID (informational only — not a redistribution claim).
   - A one-line description, ideally taken from the extension's upstream `description` frontmatter.
   - A **pinned** upstream URL using a commit SHA, not `main`, so the link reflects the version I actually vetted. Format: `https://github.com/<owner>/<repo>/blob/<sha>/<path>`.
   - An install pointer — a link to the plugin's marketplace page, or a short "copy this file from `<repo>`" note if the extension isn't distributed as a plugin.
3. If the upstream repo ever moves, goes private, renames the file, or deletes the extension, update or remove the bullet.

## License

This repository is licensed under Apache-2.0. See `LICENSE` for the full text. All files in this repo are my own original work, so a single top-level `LICENSE` covers everything — there is no layered scheme, no third-party notices file, and no per-file SPDX headers.
