# Contributing

Thanks for helping. The goal is one open skill that saves tokens for everyone, and it gets better only with the experience of people who use Claude every day. Every contribution, big or small, counts.

## What we ask, and what we never ask

- We ask for **ideas and experience**: what worked, what did not, what you would change.
- We **never** ask for your prompts, files, conversations or any personal data. Numbers are optional.

## Before you start

1. Read [PRIVACY.md](PRIVACY.md). Contributions with personal data will be closed and asked to be resubmitted.
2. Search existing [issues](../../issues) to avoid duplicates. If something similar exists, add your experience there.

## Ways to contribute

### 1. Improve the skill
Open an issue with the **Improve the skill** template. Say which rule of [`SKILL.md`](examples/token-budget/token-budget/SKILL.md) you would change, how, and why. "This rule annoyed me because..." is a perfectly good start.

### 2. Share an idea
Open an issue with the **Idea** template. You do not need proof: describe the problem and the idea.

### 3. Answer an open question
The [open questions](docs/open-questions.md) list what we do not know yet. Comment on the related issue or open one.

### 4. Propose a technique
A technique is something you have actually used that reduced token usage.

- **Without Git:** open an issue with the **Technique proposal** template. A maintainer will turn it into a file.
- **With Git:** copy [`techniques/_TEMPLATE.md`](techniques/_TEMPLATE.md) into the right category folder, fill it in, and open a pull request.

### 5. Share a try-out result (optional)
If you tried a rule and want to share how it went, use the **Try-out result** template. A description is enough; numbers help if you have them. The method is in [`docs/measuring.md`](docs/measuring.md), and the [comparison kit](examples/extraction-compare/) runs only on your computer.

### 6. Fix what exists
Typos, clearer wording, better examples, corrections: open a pull request directly.

## How a suggestion becomes part of the skill

1. **Proposal** in an issue.
2. **Discussion**: does it help, what does it cost, where does it fail.
3. **Try-out** by whoever wants, in their own work.
4. **Release**: it goes into the next version of the skill, and the [changelog](examples/token-budget/token-budget/CHANGELOG.md) credits whoever proposed it.

## Rules for techniques

- **One technique per file.** File name in lowercase with hyphens, for example `short-system-prompts.md`.
- **Label every number** as *measured*, *calculated* or *estimated*. Never mix them without saying which is which.
- **State the trade-off.** What gets worse, slower or riskier when you apply it.
- **Say where it works.** Claude app, API, Claude Code, or all of them, and with which models you tested it.
- **No invented examples presented as real.** If an example is made up for illustration, say so.

## Changing the skill files

- Keep `SKILL.md` short: everything in it is read in every chat where it loads. Put long material in separate files that `SKILL.md` links to.
- Update [`CHANGELOG.md`](examples/token-budget/token-budget/CHANGELOG.md) and the version line in `SKILL.md`.
- Rebuild the ZIP for the Claude app: `python scripts/build_skill_zips.py`. A check fails on the pull request if you forget.

## Pull request checklist

- [ ] No personal data, credentials, company names or account identifiers
- [ ] Numbers labeled as measured, calculated or estimated
- [ ] Trade-offs stated
- [ ] File placed in the right folder and listed in that folder's `README.md`
- [ ] For skill changes: changelog, version line and ZIP updated
- [ ] The automatic checks pass

You can run the privacy check locally:

```bash
python scripts/check_personal_data.py
```

## Review

A maintainer reviews every contribution. Expect questions: they are about understanding where a rule helps and where it fails, not about judging the idea.
