# Phase-based routing with subagents

**Area:** model-routing
**Works in:** any Claude environment that can launch subagents with a chosen model (for example Claude Code)
**Tested with:** a large model at low effort vs a small model at low effort for collection; the main chat on a large model
**Status:** measured
**Author:** @rafmosk

## Problem
Many tasks have three phases: **collect** material (search, read, extract), **reason** about it, and **write** the result. Running all three in one chat on a strong model means the expensive model also does the mechanical part, and every page or email it reads stays in the conversation and is re-read at each following turn.

## Technique
Keep one chat, but hand the collection phase to a subagent running a cheaper model.

1. The main chat plans the work and writes a fixed brief for the collection (see [subagent-briefs.md](subagent-briefs.md)).
2. A subagent on a small, cheap model collects and extracts, saves the full result to a file, and returns only counts and the file path.
3. The main chat reasons on the file and writes the final output.

| Phase | Who does it |
|---|---|
| Collection and extraction | Subagent, small model, low effort |
| Research that must judge or choose sources | Subagent, large model, medium effort |
| Reasoning | Main chat |
| Writing | Main chat |

**Only split above a threshold.** A subagent has a fixed start-up cost, so splitting small jobs spends more than it saves. The threshold used here: more than 3 web searches, or more than 5 long documents, emails or pages to read. Below that, do everything in the main chat. The threshold is a working rule from one setup, not a universal value.

## Example
*Illustrative.*

**Before:** one chat on a large model reads 20 notification emails, extracts the relevant items, compares them and writes a summary. All 20 emails stay in the conversation for every later turn.

**After:** the main chat sends a collection brief to a small-model subagent. The subagent reads the 20 emails, writes the extracted items to `items.json` and replies "20 emails read, 38 items, file: items.json". The main chat reads the file and writes the summary.

## Saving

### Measured: quality and token volume
Same 10 notification emails, same extraction brief, structured output, one run each (October 2026).

| Metric | Large model, low effort | Small model, low effort | Type |
|---|---|---|---|
| Items extracted | 45 | 45 | measured |
| Items found by only one of the two | 0 | 0 | measured |
| Fields that differ (out of 180) | 0 | 0 | measured |
| Total subagent tokens | about 153,000 | about 160,000 | measured |

A smaller earlier run on 2 emails gave the same pattern: identical accuracy, about 89,000 vs 90,000 tokens (measured).

### What this means
- **Routing does not reduce the number of tokens.** Both models used about the same amount. The saving comes from the **price per token** of the smaller model, which is much lower: see the official [pricing page](https://platform.claude.com/docs/en/about-claude/pricing).
- **The main chat stays lighter.** The raw emails never enter the main conversation, only the counts and the file. This is a real effect but was not measured separately (estimated).
- **Subscription usage bars:** how a plan's usage indicator weighs different models is not documented, so the effect on a subscription is not proven here.

### Fixed start-up cost
Across several runs in this setup, a single subagent used **90,000 to 150,000 tokens even on very little material** (measured). Much of it is start-up: instructions and tools loaded into the subagent. A setup with fewer instructions will likely see lower values (estimated).

### External reference
Anthropic described a similar design for its own research feature: a lead agent coordinating subagents performed much better than a single agent on broad research, at the cost of many times more tokens than a normal chat, and it was a poor fit when agents need to share context or depend heavily on each other. Source: [How we built our multi-agent research system](https://www.anthropic.com/engineering/multi-agent-research-system).

## Trade-offs
- The hand-off between phases is where quality is lost. A vague brief gives a vague result.
- The subagent does not see the conversation: it knows only what the brief says.
- In some environments you can choose the subagent's model but not its effort level. Writing "Effort: low" in the brief is a request, not a guaranteed setting.
- One test with 10 emails proves the small model was enough for **structured extraction**, not for judgement or writing.

## When not to use it
- Small jobs below the threshold.
- Tasks where collection and reasoning are tightly mixed (each finding changes the next search).
- Anything that requires judgement in the collection phase: use a large model there.
- If the small model invents even one item in real use, go back to a larger model for that kind of task.

## Related
- [subagent-briefs.md](subagent-briefs.md)
- [../context/estimate-before-heavy-work.md](../context/estimate-before-heavy-work.md)
