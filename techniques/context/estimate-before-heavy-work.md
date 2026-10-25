# Estimate before heavy work

**Area:** context
**Works in:** all
**Tested with:** large models at low and medium effort
**Status:** tested
**Author:** @rafmosk

## Problem
A few kinds of work can consume a large share of a usage allowance in one go: several subagents, many web searches, a full review of a long document. They often start without anyone checking the cost, and the damage is visible only afterwards.

**Observed case (one occurrence):** five subagents launched in parallel, without an estimate and with the weekly allowance already almost used, consumed about 880,000 tokens and roughly a third of a weekly allowance.

## Technique
Put these rules in your custom instructions, project instructions or a skill.

1. **Define "heavy".** Subagents, more than 3 web searches, a full review of a long document, or the analysis of many files at once.
2. **Estimate first.** Before heavy work, Claude states how many subagents or searches it needs and roughly what share of the usage allowance it expects to use.
3. **Always offer a light version** and an option to wait, and start only after an explicit yes. An approval that does not mention cost is not an informed yes.
4. **Check the allowance.** Ask the user where their usage stands. Above a high threshold (85% was used here), no heavy work: only light tasks until the reset.
5. **Minimal scope.** Research starts from the smallest scope that answers the question and goes deeper only on request.
6. **Sequence, do not parallelize.** Speed is rarely the goal. Run at most two subagents, preferably one after the other, and check the first result before launching more.
7. **Never pay to watch.** No repeated status checks or polling of a running job. State the expected end time and stop; check only when the user asks.

### Text to paste

```
Before any heavy work (subagents, more than 3 web searches, a full
review of a long document, many files at once): state how many
subagents or searches you need and the estimated share of my usage,
offer a lighter version and an option to wait, and start only after
my explicit yes. Ask me where my usage stands first; above 85%, do
only light work. Start research from the minimal scope. Never spend
tokens monitoring a running job: give the expected end time and stop.
```

## Example
*Illustrative.*

**Before:** "Compare these seven options in depth." Claude launches seven research subagents at once.

**After:** "This needs about 7 searches with one subagent, roughly a few percent of your weekly usage (estimated). Light version: 3 searches on the top options only. Go, light version, or wait?"

## Saving
| Metric | Value | Type |
|---|---|---|
| Worst case avoided | About 880,000 tokens in the observed case above | measured, one occurrence |
| Typical effect | Fewer large unplanned runs | estimated |

## Trade-offs
- One extra exchange before heavy work starts.
- Estimates made in advance can be wrong. In this setup, one estimate was several times higher than the real cost: record real values and use them as the reference for later estimates.

## When not to use it
- Small tasks: the estimate costs more attention than it saves.
- A single cheap collection subagent on a small, fixed scope can be exempted, as long as it is declared.

## Related
- [../model-routing/phase-based-routing.md](../model-routing/phase-based-routing.md)
- [when-to-start-a-new-chat.md](when-to-start-a-new-chat.md)
