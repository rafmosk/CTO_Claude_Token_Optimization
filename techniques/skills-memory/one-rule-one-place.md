# One rule in one place

**Area:** skills-memory
**Works in:** all environments with skills or reusable instructions
**Tested with:** large models at low and medium effort
**Status:** tested
**Author:** @rafmosk

## Problem
As personal skills and instructions grow, the same rules get copied into several of them: writing style, output format, model choice. When two of those skills load in the same chat, the same text enters the context twice. Copies also drift apart over time and start to contradict each other.

## Technique
Organize skills in levels. Each rule lives in exactly one skill; other skills reference it instead of copying it.

| Level | What it contains | Loads |
|---|---|---|
| 0 | General rules: answer format, questions, model and budget rules, the map of all skills | nothing |
| 1 | Shared building blocks used by several tasks: writing style, personal reference data, page or code conventions | level 0 |
| 2 | Task skills: one workflow each | the level 1 blocks it needs |

Rules for the structure:
1. A task skill starts with "Load skill X first" for each building block it needs, and contains only what is specific to the task.
2. Each skill is loaded once per chat. If it is already loaded, it is not loaded again.
3. The level 0 skill keeps a **map** of all skills and their dependencies. Before adding a rule, check the map: if more than one skill needs it, it goes into a level 1 block.
4. The level 0 skill is loaded first in every chat. In practice, rules that are not loaded are not applied.

### Filter before moving a rule up a level
Move a rule into a shared block only if all four are true:
- it appears in at least two skills;
- it can be written as "do" or "don't", not as "X is important";
- ignoring it has a concrete risk you can state in one sentence;
- it is not already in the higher level, even in other words.

## Example
*Illustrative.*

**Before:** three task skills each contain the same 40-line writing style section. A task that uses two of them loads it twice.

**After:** the writing style lives in one level 1 skill. Each task skill has one line: "Load skill writing-style first."

## Saving
| Metric | Value | Type |
|---|---|---|
| Duplicated instructions in context | Removed when several skills load together | estimated, not measured |
| Contradictions between skills | Fewer, because there is one source per rule | observed, not measured |

## Trade-offs
- More skill loads per task, each with a small overhead.
- If the level 0 skill is not loaded, its rules are silently skipped. In this setup that happened once and caused an expensive session: the fix was a rule that level 0 loads first in every chat.
- Restructuring existing skills takes time.

## When not to use it
- With only one or two small skills: a single file is simpler.

## Related
- [../context/estimate-before-heavy-work.md](../context/estimate-before-heavy-work.md)
