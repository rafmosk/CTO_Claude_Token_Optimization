# Changelog

Every version lists what changed and who proposed it. This file is not linked from `SKILL.md`, so Claude does not read it during a chat and it costs no tokens.

To propose a change, open an issue with the **Improve the skill** template.

## 1.1 · 2026-10-25

- Budget limit works for API users too: `USAGE_STOP` became `BUDGET_STOP`, with a subscription value and an API value. Proposed by @rafmosk.
- Fallback when subagents are not available: every phase stays in the chat, the other rules still apply. Proposed by @rafmosk.
- Version line and link to the project, to invite changes. Proposed by @rafmosk.
- Install guide: a line for personal instructions so the skill loads in every chat. Proposed by @rafmosk.

## 1.0 · 2026-10-25

- First version: estimate before heavy work, minimal scope, phase-based routing with subagents and fixed briefs, when to start a new chat, lean instructions. Proposed by @rafmosk.

## Contributors

@rafmosk
