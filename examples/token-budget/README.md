# token-budget skill

The open skill this project builds together. Version 1.1, see the [changelog](token-budget/CHANGELOG.md).

It applies these techniques in every chat:

- [Estimate before heavy work](../../techniques/context/estimate-before-heavy-work.md)
- [Phase-based routing with subagents](../../techniques/model-routing/phase-based-routing.md)
- [Fixed briefs for subagents](../../techniques/model-routing/subagent-briefs.md)
- [When to start a new chat](../../techniques/context/when-to-start-a-new-chat.md)
- [One rule in one place](../../techniques/skills-memory/one-rule-one-place.md)

| File | Content |
|---|---|
| [`token-budget/SKILL.md`](token-budget/SKILL.md) | The rules, with a settings table at the top |
| [`token-budget/briefs.md`](token-budget/briefs.md) | Subagent brief templates, read only when needed |
| [`token-budget/CHANGELOG.md`](token-budget/CHANGELOG.md) | Versions and contributors, never read during a chat |
| [`token-budget.zip`](token-budget.zip) | The same folder, packed for upload to the Claude app |

## Install in the Claude app (claude.ai)

Skills require code execution to be enabled in your settings.

1. Download [`token-budget.zip`](token-budget.zip) (on the file page, use the download button).
2. Open **Customize > Skills** ([claude.ai/customize/skills](https://claude.ai/customize/skills)).
3. Add the skill by uploading the ZIP, then make sure it is enabled.
4. **Make it load in every chat.** Claude loads a skill only when it judges that a request needs it, so a general skill like this one may stay unused. Add this line to your personal instructions (or to a project's instructions):

   ```
   At the start of every chat, before any other work, load the token-budget skill and apply it.
   ```

**Updating:** when a new version comes out, upload the new ZIP in the same place, replacing the old skill.

Official guide: [How to create custom skills](https://support.claude.com/en/articles/12512198-how-to-create-custom-skills) and [Use skills in Claude](https://support.claude.com/en/articles/12512180-use-skills-in-claude).

## Install in Claude Code

Copy the `token-budget` folder (the one containing `SKILL.md`) to one of these places:

| Scope | Path |
|---|---|
| All your projects | `~/.claude/skills/token-budget/` |
| One repository | `.claude/skills/token-budget/` |

Invoke it with `/token-budget`, or let Claude load it automatically. To load it in every session, add the line from step 4 above to your `CLAUDE.md`.

Official guide: [Extend Claude with skills](https://code.claude.com/docs/en/skills).

## Customize

Change the values in the **Settings** table at the top of `SKILL.md`: thresholds, models, budget limit. If you edit the files and want to upload them to the Claude app, rebuild the ZIP:

```bash
python scripts/build_skill_zips.py
```

## Help improve it

- A rule gets in your way, or misses a case? Open an issue with the **Improve the skill** template.
- Have an answer to one of the [open questions](../../docs/open-questions.md)? That is where help is needed most.
- Tried a rule and want to tell how it went? Use the **Try-out result** template. Numbers are optional, and you never share your material.

Accepted changes go into the next version, and the [changelog](token-budget/CHANGELOG.md) credits whoever proposed them.
