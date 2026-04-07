# Attributions

This file records the upstream source, commit, sync date, and license for every third-party artifact in this repo. See `CLAUDE.md` for the required format.

### skills/frontend-design

- Source: https://github.com/anthropics/claude-plugins-official/tree/main/plugins/frontend-design
- Upstream commit: 104d39be10b7b1380b2ae23a387a11a297b599c3
- Synced: 2026-04-07
- License: Apache-2.0
- Notes: File copied verbatim from `plugins/frontend-design/skills/frontend-design/SKILL.md`. The skill's own frontmatter references `LICENSE.txt`, which does not ship inside the skill folder upstream — the plugin's license lives at the plugin root. The actual license is Apache-2.0 as recorded above.

### agents/code-simplifier

- Source: https://github.com/anthropics/claude-plugins-official/tree/main/plugins/code-simplifier
- Upstream commit: 104d39be10b7b1380b2ae23a387a11a297b599c3
- Synced: 2026-04-07
- License: Apache-2.0
- Notes: File copied verbatim from `plugins/code-simplifier/agents/code-simplifier.md`. Part of Anthropic's official Claude Code plugin marketplace.

### commands/code-review

- Source: https://github.com/anthropics/claude-plugins-official/tree/main/plugins/code-review
- Upstream commit: 104d39be10b7b1380b2ae23a387a11a297b599c3
- Synced: 2026-04-07
- License: Apache-2.0
- Notes: File copied verbatim from `plugins/code-review/commands/code-review.md`. Part of Anthropic's official Claude Code plugin marketplace.

### commands/security-review

- Source: https://github.com/anthropics/claude-code-security-review
- Upstream commit: 0c6a49f1fa56a1d472575da86a94dbc1edb78eda
- Synced: 2026-04-07
- License: MIT
- Notes: File copied verbatim from `.claude/commands/security-review.md`. The upstream repository also ships a GitHub Action (`action.yml`) which is intentionally not mirrored here — only the slash command.
