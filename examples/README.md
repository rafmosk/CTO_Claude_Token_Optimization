# Examples

Ready-to-use prompts, skills and configurations that apply one or more techniques.

Every example must be **anonymized** following [`../PRIVACY.md`](../PRIVACY.md): keep the structure, replace personal content with placeholders such as `<NAME>` or `<PROJECT>`.

Suggested layout:

```
examples/
  <example-name>/
    README.md      what it does, which techniques it uses, how to use it
    <files>        prompt, SKILL.md, configuration
```

## Available

| Example | What it is | For whom |
|---|---|---|
| [`token-budget/`](token-budget/) | Ready-to-install skill with all the techniques, for the Claude app and Claude Code | Anyone using skills |
| [`custom-instructions.md`](custom-instructions.md) | The same rules as a short text to paste into your instructions | Anyone not using skills |
| [`extraction-compare/`](extraction-compare/) | Script and steps to compare a cheap and a large model on your own material | Anyone who wants to measure |

A skill folder (one containing `SKILL.md`) gets a ZIP for upload to the Claude app. After editing a skill, rebuild it with `python scripts/build_skill_zips.py`: a check on every pull request fails if the ZIP is out of date.
