# skills

A personal library of Claude Code extensions I use and curate — **skills**, **subagents**, and **slash commands** — both things I've authored and things I've found and like. It is not a plugin. Install an artifact by copying the matching file or folder into your `~/.claude/` (or a project's `.claude/`).

See [`CLAUDE.md`](./CLAUDE.md) for the directory layout, file conventions per type, and attribution rules. See [`ATTRIBUTIONS.md`](./ATTRIBUTIONS.md) for full provenance of third-party items (upstream URL, commit SHA, sync date, license).

## Credit & disclaimer

**I am not the author of anything in `third-party/`.** Every file under `skills/third-party/`, `agents/third-party/`, and `commands/third-party/` was written by someone else — primarily [Anthropic](https://github.com/anthropics). These files are included here only because I use them myself and want a single place to track, review, and sync the versions I run. I claim no credit for them. Full credit goes to the original authors listed in [`ATTRIBUTIONS.md`](./ATTRIBUTIONS.md), along with exact upstream URLs, commit SHAs, and licenses.

**No warranty — use at your own risk.** Everything in this repository is provided **as-is**, with no warranty of any kind, express or implied. You are solely responsible for reviewing any skill, subagent, or slash command before installing it into your Claude Code environment. Anything you install runs with your user permissions and can read, modify, or execute files on your machine; treat it accordingly.

**Always prefer the latest official source.** The copies under `third-party/` are **point-in-time snapshots** and will drift behind upstream over time. Before installing anything from this repo:
1. Open [`ATTRIBUTIONS.md`](./ATTRIBUTIONS.md) and check the `Upstream commit` field for the file you want.
2. Compare it against the upstream repository's current `HEAD`.
3. If there is drift, **re-sync from upstream** (or install the official version directly — e.g. via Claude Code's plugin marketplace) rather than using the stale copy here.

When in doubt, install from the official source, not from this repo.

## What's inside

### Subagents

- **[`agents/third-party/code-simplifier.md`](./agents/third-party/code-simplifier.md)** — Anthropic's `code-simplifier` agent. Simplifies and refines recently modified code for clarity, consistency, and maintainability while preserving behavior. Upstream: https://github.com/anthropics/claude-plugins-official/tree/main/plugins/code-simplifier

### Slash commands

- **[`commands/third-party/code-review.md`](./commands/third-party/code-review.md)** — Anthropic's `/code-review` command. Performs a multi-agent code review on a pull request with CLAUDE.md compliance checks, bug detection, git-history context, and false-positive filtering. Upstream: https://github.com/anthropics/claude-plugins-official/tree/main/plugins/code-review
- **[`commands/third-party/security-review.md`](./commands/third-party/security-review.md)** — Anthropic's `/security-review` command. Performs a focused, high-signal security review of the pending changes on the current branch, filtering out noise and low-confidence findings. Upstream: https://github.com/anthropics/claude-code-security-review

### Skills

- **[`skills/third-party/frontend-design/`](./skills/third-party/frontend-design/)** — Anthropic's `frontend-design` skill. Guides the creation of distinctive, production-grade frontend interfaces with high design quality, steering away from generic "AI slop" aesthetics. Upstream: https://github.com/anthropics/claude-plugins-official/tree/main/plugins/frontend-design

## Install

Skills:

    cp -r skills/third-party/<skill-name> ~/.claude/skills/<skill-name>

Subagents:

    cp agents/third-party/<agent-name>.md ~/.claude/agents/<agent-name>.md

Slash commands:

    cp commands/third-party/<command-name>.md ~/.claude/commands/<command-name>.md
