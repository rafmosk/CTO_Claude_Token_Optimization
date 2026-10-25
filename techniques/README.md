# Techniques

Each technique lives in its own file, inside the folder of its area. Start from [`_TEMPLATE.md`](_TEMPLATE.md).

| Area | What it covers |
|---|---|
| [`prompting/`](prompting/) | How requests and instructions are written: length, structure, output format |
| [`context/`](context/) | What stays in the conversation: when to start a new chat, summaries, attachments, long threads |
| [`model-routing/`](model-routing/) | Which model and which effort level for which kind of work |
| [`caching/`](caching/) | Reusing content that does not change between requests |
| [`skills-memory/`](skills-memory/) | Skills, projects, memory and reusable instructions that avoid repeating context |

## Index

When you add a technique, list it here and in the folder's `README.md`.

| Technique | Area | Works in | Saving | Status |
|---|---|---|---|---|
| [Phase-based routing with subagents](model-routing/phase-based-routing.md) | model-routing | environments with subagents | Same quality on extraction from a much cheaper model | measured |
| [Fixed briefs for subagents](model-routing/subagent-briefs.md) | model-routing | environments with subagents | Only counts and a file path return to the main chat | tested |
| [Estimate before heavy work](context/estimate-before-heavy-work.md) | context | all | Avoids large unplanned runs | tested |
| [When to start a new chat](context/when-to-start-a-new-chat.md) | context | all | Shorter, focused context per message | tested |
| [One rule in one place](skills-memory/one-rule-one-place.md) | skills-memory | all with skills | No duplicated instructions in context | tested |

**Status values:** `idea` (not tested), `tested` (used, not measured), `measured` (with a benchmark).
