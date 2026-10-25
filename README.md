# CTO · Claude Token Optimization

An open, community-driven collection of techniques to get the same results from Claude while spending fewer tokens.

The goal is simple: every technique here should be **described clearly, measured honestly, and reusable by anyone**.

> **Status:** early setup. The structure is in place; the first techniques will be published after a privacy review. Ideas are welcome right now.

## What you will find here

| Folder | What goes in it |
|---|---|
| [`techniques/`](techniques/) | One file per technique, grouped by area (prompting, context, model routing, caching, skills and memory) |
| [`benchmarks/`](benchmarks/) | Measured before/after results, with the method used to obtain them |
| [`examples/`](examples/) | Ready-to-use, anonymized prompts, skills and configurations |
| [`docs/`](docs/) | How to measure savings, glossary, project principles |

## Principles

1. **Measured, not claimed.** A saving counts only if it comes with a reproducible measurement. Estimates are welcome but must be labeled as estimates.
2. **Quality first.** A technique that saves tokens but makes answers worse is not a saving. Every technique states its trade-offs.
3. **No personal data.** Nothing that identifies a person, a company or an account. See [PRIVACY.md](PRIVACY.md).
4. **Plain language.** Anyone using Claude, not only developers, should be able to understand and apply a technique.

## How to contribute

- **Have an idea?** Open an issue with the *Idea* template. Half-formed ideas are fine.
- **Have a technique that works?** Open an issue with the *Technique proposal* template, or send a pull request using [`techniques/_TEMPLATE.md`](techniques/_TEMPLATE.md).
- **Measured something?** Share it with the *Benchmark* template.

Details in [CONTRIBUTING.md](CONTRIBUTING.md). Please read the [Code of Conduct](CODE_OF_CONDUCT.md) first.

## Roadmap

See [ROADMAP.md](ROADMAP.md).

## License

[MIT](LICENSE). By contributing you agree that your contribution is released under the same license.

*This is an independent community project, not affiliated with or endorsed by Anthropic.*
