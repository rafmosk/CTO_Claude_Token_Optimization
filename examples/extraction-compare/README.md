# Extraction comparison kit

Does a cheap model extract as well as a large one on **your** material? This kit lets you check it in a few steps and share only the numbers.

It is the method behind the measurement in [phase-based routing](../../techniques/model-routing/phase-based-routing.md). No sample data is included: you use your own material, on your own machine, and nothing personal leaves it.

## What you need

- Claude Code, or any Claude environment that can launch subagents with a chosen model
- Python 3.9 or later (no packages to install)
- Some material to extract from: emails, pages, documents. 10 items is a good start

## Steps

1. **Write one collection brief** from the template in [`briefs.md`](../token-budget/token-budget/briefs.md). Fix the fields to extract (for example `title`, `date`, `amount`) and ask for a JSON list saved to a file.
2. **Run it with the large model.** Ask Claude to launch a subagent with that brief on a large model at low effort, saving to `runs/large.json`.
3. **Run the same brief with the small model,** unchanged, saving to `runs/small.json`.
4. **Write down the tokens** each subagent used, where your environment shows them.
5. **Compare:**

   ```bash
   python compare.py runs/large.json runs/small.json --key title,date --names large,small
   ```

   `--key` is the field, or fields, that identify the same item in both files.

6. **Read the result:**
   - `only_in_large` / `only_in_small`: items one model found and the other missed (or invented)
   - `fields_different`: values that do not match on items both found
   - `Result: identical` means same items and same values
7. **Keep the result for yourself, or share it if you like.** If it helps answer one of the [open questions](../../docs/open-questions.md), you can post the summary with the **Try-out result** template: item counts, differences, tokens, models and effort. Never share the material or the JSON files.

## Options

| Option | Use |
|---|---|
| `--ignore` | Fields not to compare. Default: `evidence,snippet,link,url,source` |
| `--strict` | Exact comparison. By default spaces are collapsed and case is ignored |
| `--report report.json` | Save the full result to a file |
| `--names large,small` | Labels used in the output |

## Notes

- One run per model proves little. Repeat at least three times if you want a number others can trust: see [`docs/measuring.md`](../../docs/measuring.md).
- A match on extraction says nothing about judgement or writing. Do not extend the conclusion to those.
- The `runs/` folder is ignored by Git, so your outputs are not committed by mistake.
