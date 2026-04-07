# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this repository is

A personal library of Claude Code extensions — **skills**, **subagents**, and **slash commands**. It is not a plugin, not an installable package, and has no build system. Each artifact is installed by copying a single file or folder into the user's Claude Code config directory (`~/.claude/`) or a project's `.claude/` directory.

## Ownership and disclaimer

Nothing under any `third-party/` directory was authored by the repo owner. Credit for those files belongs to the upstream authors recorded in `ATTRIBUTIONS.md`. Everything in this repository is provided as-is with no warranty; anyone installing from `third-party/` is expected to review the file first and is responsible for its behavior on their machine.

Third-party files are point-in-time snapshots and will drift behind upstream. When the user (or you, acting on their behalf) is about to install or rely on a `third-party/` artifact, prefer the latest upstream version: check the `Upstream commit` in `ATTRIBUTIONS.md` against the upstream `HEAD` and re-sync if they differ. The full user-facing disclaimer lives in `README.md`.

## Directory layout

```
<repo-root>/
├── skills/
│   ├── mine/              skills authored in this repo
│   └── third-party/       skills copied from external sources
├── agents/
│   ├── mine/              subagents authored in this repo
│   └── third-party/       subagents copied from external sources
├── commands/
│   ├── mine/              slash commands authored in this repo
│   └── third-party/       slash commands copied from external sources
├── ATTRIBUTIONS.md         upstream source, commit, sync date, license for every third-party item
├── CLAUDE.md
└── README.md
```

Each `mine/` and `third-party/` subdirectory holds its artifacts **flat** — no category nesting. Categorisation is expressed through each artifact's `description` field, not the filesystem.

## File conventions per type

### Skills

Skills follow the Agent Skills open standard (https://agentskills.io/specification). Each skill is a **folder**:

    skills/{mine,third-party}/<skill-name>/SKILL.md

The leaf folder name must equal the skill's `name` frontmatter field. Required frontmatter: `name`, `description`. Optional portable fields: `license`, `compatibility`, `metadata`, `allowed-tools`. Claude Code recognises additional optional fields (`model`, `effort`, `context`, `agent`, `hooks`, `paths`, `shell`, `argument-hint`, `disable-model-invocation`, `user-invocable`) documented at https://code.claude.com/docs/en/skills.md.

Install:

    cp -r skills/third-party/<skill-name> ~/.claude/skills/<skill-name>

### Subagents

Subagents are **single markdown files** at the root of `agents/{mine,third-party}/`:

    agents/{mine,third-party}/<agent-name>.md

The file name (without `.md`) must equal the agent's `name` frontmatter field. Typical frontmatter: `name`, `description`, optionally `model`, `tools`. See https://code.claude.com/docs/en/sub-agents.md.

Install:

    cp agents/third-party/<agent-name>.md ~/.claude/agents/<agent-name>.md

### Slash commands

Slash commands are **single markdown files** at the root of `commands/{mine,third-party}/`:

    commands/{mine,third-party}/<command-name>.md

The file name (without `.md`) becomes the slash command — `code-review.md` → `/code-review`. Frontmatter is optional; common fields are `description`, `allowed-tools`, `argument-hint`, `disable-model-invocation`. See https://code.claude.com/docs/en/slash-commands.md.

Install:

    cp commands/third-party/<command-name>.md ~/.claude/commands/<command-name>.md

## Non-negotiable rules

1. **Install gesture stays trivial.** One `cp` (or `cp -r` for skills) deposits one artifact at its canonical `~/.claude/` location. The file or folder name must match the artifact's identity.
2. **No category nesting** under any `mine/` or `third-party/` directory. Flat only.
3. **No per-artifact attribution files** inside the artifact itself. All attribution lives in `ATTRIBUTIONS.md`.
4. **Provenance is encoded by bucket.** Anything under a `third-party/` directory must have an `ATTRIBUTIONS.md` entry.

## Attribution format

Every third-party artifact gets one `ATTRIBUTIONS.md` entry:

    ### <type>/<name>
    - Source: <upstream URL>
    - Upstream path: <file path within the source repo>
    - Upstream commit: <SHA>
    - Synced: <YYYY-MM-DD>
    - License: <SPDX id or license name>
    - Notes: <optional local modifications or usage notes>

`<type>` is `skills`, `agents`, or `commands`. `Upstream path:` is the path of the file (or the canonical file of a multi-file skill) within the upstream repository — this is what the weekly drift check uses to compare against upstream.

## Adding a new artifact

For something you author yourself: place it under the matching `mine/` directory following the file convention above. No attribution entry needed.

For something copied from upstream:
1. Copy verbatim into the matching `third-party/` directory. Ensure the file or folder name matches the artifact's identity (skill `name`, agent file stem, command file stem).
2. Add an entry to `ATTRIBUTIONS.md` with source URL, upstream commit SHA, sync date, and license.
3. Avoid modifying the upstream content. If you must, record the change in the `Notes:` field of the attribution entry.
