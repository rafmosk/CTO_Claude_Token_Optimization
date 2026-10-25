# Contributing

Thanks for helping. This project grows on ideas from people who use Claude every day, so every contribution, big or small, is useful.

## Before you start

1. Read [PRIVACY.md](PRIVACY.md). Contributions with personal data will be closed and asked to be resubmitted.
2. Search existing [issues](../../issues) to avoid duplicates. If something similar exists, add your experience there.

## Ways to contribute

### 1. Share an idea
Open an issue with the **Idea** template. You do not need proof or measurements: describe the problem and the idea.

### 2. Propose a technique
A technique is something you have actually used and that reduced token usage.

- **Without Git:** open an issue with the **Technique proposal** template. A maintainer will turn it into a file.
- **With Git:** copy [`techniques/_TEMPLATE.md`](techniques/_TEMPLATE.md) into the right category folder, fill it in, and open a pull request.

### 3. Share a measurement
Open an issue with the **Benchmark** template, or add a file to [`benchmarks/`](benchmarks/) from [`benchmarks/_TEMPLATE.md`](benchmarks/_TEMPLATE.md). Follow the method in [`docs/measuring.md`](docs/measuring.md).

### 4. Improve what exists
Typos, clearer wording, better examples, corrections: open a pull request directly.

## Rules for techniques

- **One technique per file.** File name in lowercase with hyphens, for example `short-system-prompts.md`.
- **Label every number** as *measured*, *calculated* or *estimated*. Never mix them without saying which is which.
- **State the trade-off.** What gets worse, slower or riskier when you apply it.
- **Say where it works.** Claude app, API, Claude Code, or all of them, and with which models you tested it.
- **No invented examples presented as real.** If an example is made up for illustration, say so.

## Pull request checklist

- [ ] No personal data, credentials, company names or account identifiers
- [ ] Numbers labeled as measured, calculated or estimated
- [ ] Trade-offs stated
- [ ] File placed in the right folder and listed in that folder's `README.md`
- [ ] The privacy check passes (it runs automatically on every pull request)

You can run the privacy check locally:

```bash
python scripts/check_personal_data.py
```

## Review

A maintainer reviews every contribution. Expect questions: they are about making the technique reproducible, not about judging the idea.
