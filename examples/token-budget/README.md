# token-budget skill

A ready-to-install skill that applies the techniques of this project in every chat:

- [Estimate before heavy work](../../techniques/context/estimate-before-heavy-work.md)
- [Phase-based routing with subagents](../../techniques/model-routing/phase-based-routing.md)
- [Fixed briefs for subagents](../../techniques/model-routing/subagent-briefs.md)
- [When to start a new chat](../../techniques/context/when-to-start-a-new-chat.md)
- [One rule in one place](../../techniques/skills-memory/one-rule-one-place.md)

| File | Content |
|---|---|
| [`token-budget/SKILL.md`](token-budget/SKILL.md) | The rules, with a settings table at the top |
| [`token-budget/briefs.md`](token-budget/briefs.md) | Subagent brief templates, read only when needed |
| [`token-budget.zip`](token-budget.zip) | The same folder, packed for upload to the Claude app |

## Install in the Claude app (claude.ai)

Skills require code execution to be enabled in your settings.

1. Download [`token-budget.zip`](token-budget.zip) (on the file page, use the download button).
2. Open **Customize > Skills** ([claude.ai/customize/skills](https://claude.ai/customize/skills)).
3. Add the skill by uploading the ZIP, then make sure it is enabled.

Official guide: [How to create custom skills](https://support.claude.com/en/articles/12512198-how-to-create-custom-skills) and [Use skills in Claude](https://support.claude.com/en/articles/12512180-use-skills-in-claude).

## Install in Claude Code

Copy the `token-budget` folder (the one containing `SKILL.md`) to one of these places:

| Scope | Path |
|---|---|
| All your projects | `~/.claude/skills/token-budget/` |
| One repository | `.claude/skills/token-budget/` |

Invoke it with `/token-budget`, or let Claude load it automatically.

Official guide: [Extend Claude with skills](https://code.claude.com/docs/en/skills).

## Customize

Change the values in the **Settings** table at the top of `SKILL.md` (thresholds, models, usage limit). If you edit the files and want to upload them to the Claude app, rebuild the ZIP:

```bash
python scripts/build_skill_zips.py
```

## Test it and share results

1. Use it for a week on your normal work.
2. Measure a task with and without it, following [`docs/measuring.md`](../../docs/measuring.md).
3. To compare a cheap and a large model on the same extraction, use the [extraction comparison kit](../extraction-compare/).
4. Share your numbers with the **Benchmark** issue template.
