# CTO · Claude Token Optimization

**Let's build, together, one open skill that makes Claude spend fewer tokens without losing quality.**

Anyone can install it, anyone can propose a change, and every idea that proves useful goes into the next version with the name of whoever suggested it.

> **Status:** version 1.1 of the [token-budget skill](examples/token-budget/) is out. It is a starting point built from one person's daily use. It needs other people's experience to get better, and that is the point of this project.

## Try it now

- **Use skills?** Install the [token-budget skill](examples/token-budget/) in the Claude app or in Claude Code.
- **No skills?** Paste the [custom instructions](examples/custom-instructions.md).
- **Curious about why each rule exists?** Read the [techniques](techniques/): each rule of the skill comes from one of them.

## How you can help

- **Something in the skill does not work for you?** Open an issue with the *Improve the skill* template: tell us which rule, what you would change and why.
- **Have an idea?** Open an issue with the *Idea* template. Half-formed ideas are fine.
- **Know the answer to an [open question](docs/open-questions.md)?** That is where help is needed most.
- **Use a technique the skill does not have?** Propose it with the *Technique proposal* template.

You never need to share your prompts, files or conversations. We ask for ideas and experience, not data.

## How a suggestion becomes part of the skill

1. **Proposal.** Someone opens an issue: an idea, a rule to change, a new technique.
2. **Discussion.** We talk it through in the issue: does it help, what does it cost, where does it fail.
3. **Try-out.** Whoever wants tries it in their own work. Numbers help to decide, but they are optional: a clear description of what happened is enough to start. If you want to measure, the [comparison kit](examples/extraction-compare/) runs entirely on your own computer.
4. **Release.** If it holds up, it goes into the next version of the skill, and the [changelog](examples/token-budget/token-budget/CHANGELOG.md) credits whoever proposed it.

## What you will find here

| Folder | What goes in it |
|---|---|
| [`examples/`](examples/) | The skill, the custom instructions version and the comparison kit |
| [`techniques/`](techniques/) | The reasoning behind each rule, one file per technique |
| [`docs/`](docs/) | Open questions, how to measure, glossary |
| [`benchmarks/`](benchmarks/) | Results of try-outs that people chose to share |

## Principles

1. **Tested, not claimed.** A new rule enters the skill when someone besides its author has seen it work. The rules of version 1 come from one person's use and are open to challenge. Estimates are welcome but labeled as estimates.
2. **Quality first.** A rule that saves tokens but makes answers worse is not a saving. Every technique states its trade-offs.
3. **No personal data.** Nothing that identifies a person, a company or an account. See [PRIVACY.md](PRIVACY.md).
4. **Plain language.** Anyone using Claude, not only developers, should be able to understand and apply it.

Details in [CONTRIBUTING.md](CONTRIBUTING.md). Please read the [Code of Conduct](CODE_OF_CONDUCT.md) first. Roadmap in [ROADMAP.md](ROADMAP.md).

## License

[MIT](LICENSE). By contributing you agree that your contribution is released under the same license.

*This is an independent community project, not affiliated with or endorsed by Anthropic.*
