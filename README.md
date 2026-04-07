# skills

My personal library of Claude Code extensions — things I've authored myself, plus a curated list of third-party ones I use and recommend.

This is **not a plugin** and not an installable package. Extensions I've written are installed by copying a single file or folder into `~/.claude/` (or a project's `.claude/`). Third-party entries in the curated list below are **links, not copies** — follow each link to install from its upstream source.

See [`CLAUDE.md`](./CLAUDE.md) for the directory layout, file conventions per extension type, and rules for adding to the curated list.

## My extensions

*(None yet.)* When I author a skill, subagent, or slash command, it'll appear here.

## Extensions I use

I curate this list. Everything below is authored by someone else (primarily Anthropic) and lives in its own upstream repository. I am neither the author nor a redistributor — these are pointers, not mirrors. Install directly from upstream (via the plugin marketplace, `gh repo clone`, or a one-off file copy).

The "Pinned" links below point to the specific commit SHA I vetted — clicking through gives you exactly the version I'm recommending. The second link per entry (where provided) takes you to the plugin marketplace page or the current upstream default branch.

### Skills

- **`frontend-design`** — Anthropic, Apache-2.0. Guides the creation of distinctive, production-grade frontend interfaces with high design quality, explicitly steered away from generic "AI slop" aesthetics.
  - Pinned: https://github.com/anthropics/claude-plugins-official/blob/104d39be10b7b1380b2ae23a387a11a297b599c3/plugins/frontend-design/skills/frontend-design/SKILL.md
  - Plugin marketplace: https://github.com/anthropics/claude-plugins-official/tree/main/plugins/frontend-design

### Subagents

- **`code-simplifier`** — Anthropic, Apache-2.0. Simplifies and refines recently modified code for clarity, consistency, and maintainability while preserving behaviour.
  - Pinned: https://github.com/anthropics/claude-plugins-official/blob/104d39be10b7b1380b2ae23a387a11a297b599c3/plugins/code-simplifier/agents/code-simplifier.md
  - Plugin marketplace: https://github.com/anthropics/claude-plugins-official/tree/main/plugins/code-simplifier

### Slash commands

- **`/code-review`** — Anthropic, Apache-2.0. Performs a multi-agent code review on a pull request, with CLAUDE.md compliance checks, bug detection, git-history context, and false-positive filtering.
  - Pinned: https://github.com/anthropics/claude-plugins-official/blob/104d39be10b7b1380b2ae23a387a11a297b599c3/plugins/code-review/commands/code-review.md
  - Plugin marketplace: https://github.com/anthropics/claude-plugins-official/tree/main/plugins/code-review
- **`/security-review`** — Anthropic, MIT. Performs a focused, high-signal security review of the pending changes on the current branch, filtering out noise and low-confidence findings.
  - Pinned: https://github.com/anthropics/claude-code-security-review/blob/0c6a49f1fa56a1d472575da86a94dbc1edb78eda/.claude/commands/security-review.md
  - Upstream repository: https://github.com/anthropics/claude-code-security-review (the command lives at `.claude/commands/security-review.md`).

## License

This repository is licensed under the **Apache License 2.0**. See [`LICENSE`](./LICENSE) for the full text. Copyright holder: `Dor Ben Dov`.

Every file in this repo is my own original work. The "Extensions I use" section above is a list of *links* to other people's extensions — those files are not included in this repository, so their licenses do not apply to the repository's contents.

## No warranty

Everything in this repo is provided **as-is**, without warranty of any kind, express or implied. The full disclaimer lives in `LICENSE` (Apache-2.0 §§7–8). You are responsible for reviewing any file before using it, and for evaluating any third-party extension at its upstream source before installing it.
