# Fixed briefs for subagents

**Area:** model-routing
**Works in:** any Claude environment with subagents (for example Claude Code)
**Tested with:** small and large models at low effort for collection
**Status:** tested
**Author:** @rafmosk

## Problem
When work is split between a main chat and subagents, the hand-off is where quality and tokens are lost. A brief written on the fly changes every time: the subagent asks for clarification, returns too much text, or makes choices it should not make. A long reply from a subagent also fills the main conversation.

## Technique
Write each brief from a fixed template, the same every time. Two rules matter most:

- **The full result goes to a file, not to the chat.** The main chat receives only counts and the file path.
- **The collector never chooses.** It takes everything in scope and leaves judgement to the main chat.

### Collection brief

```
Effort: low

Goal: <one sentence>
Scope: <exact list: email IDs, search queries, sites, files>
Extract for each item: <field 1>, <field 2>, <field 3>
Rules:
- Take every item in scope, even if it looks irrelevant.
- Do not invent anything. If a field is missing, leave it empty.
- Do not filter, rank or choose.
Output:
- Save a JSON file at <path>, one entry per item, each with a short
  verbatim snippet as evidence and the source link.
- Reply only with: number of sources read, number of items, file path.
```

### Reasoning brief (when reasoning is also delegated)

```
Effort: high

Question: <the question to answer>
Input: <path of the collection file>
Constraints: <rules that apply>
Output: an analysis with the conclusion, the assumptions used and
what is missing. No final text for the reader.
```

## Example
*Illustrative.*

**Before:** "Look through these emails and tell me what's interesting." The subagent returns three paragraphs of prose with its own selection, and the main chat cannot tell what was skipped.

**After:** the collection brief above. The subagent replies "12 emails, 31 items, file: items.json", and every item has evidence and a link.

## Saving
| Metric | Value | Type |
|---|---|---|
| Main chat input | Only counts and a path instead of the full extraction | estimated, not measured |
| Retries | Fewer, because scope and output are fixed | estimated, not measured |

In the test described in [phase-based-routing.md](phase-based-routing.md), this brief gave identical results from a small and a large model: 45 items each, 0 differing fields out of 180 (measured).

## Trade-offs
- Writing the scope exactly takes a minute more than a vague request.
- The "evidence snippet" per item makes the file bigger. It is what lets you check for invented items.

## When not to use it
- Single quick lookups: no subagent is needed.
- Exploratory research where the scope cannot be fixed in advance.

## Related
- [phase-based-routing.md](phase-based-routing.md)
