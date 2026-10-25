---
name: token-budget
description: Rules to spend fewer tokens with no loss of quality. Estimate before heavy work, route phases to cheaper models via subagents, switch chats at the right time. Load at the start of every chat.
---

# Token budget

Version 1.1 · community skill · propose changes at github.com/rafmosk/CTO_Claude_Token_Optimization

Apply these rules in every chat, before any substantial work.

## Settings

Adjust these values to your plan and habits. The rules below refer to them by name.

| Setting | Default |
|---|---|
| HEAVY_SEARCHES | more than 3 web searches |
| HEAVY_DOCS | more than 5 long documents, emails or pages |
| BUDGET_STOP | subscription: 85% of the weekly usage allowance · API: the monthly amount or token budget the user set |
| MAX_SUBAGENTS | 2, preferably in sequence |
| CHEAP_MODEL | the smallest available model, low effort |
| JUDGE_MODEL | a large model, medium effort |

## 1. Heavy work needs an estimate

Work is **heavy** when it involves subagents, more than HEAVY_SEARCHES, more than HEAVY_DOCS, a full review of a long document, or the analysis of many files at once.

Before heavy work:
1. State how many subagents and searches you plan, and the estimated share of the usage allowance or budget. Label it as an estimate.
2. Ask the user where their usage or spending stands. Above BUDGET_STOP, do only light work until the reset or the next budget period.
3. Offer a lighter version and an option to wait. Start only after an explicit yes that came after the cost was stated.

Exemption: a single collection subagent on CHEAP_MODEL with a small, fixed scope (up to about 20 items) can start without an estimate, as long as it is declared in one line.

## 2. Minimal scope

- Start research from the smallest scope that answers the question. Go deeper only when asked.
- Never spend tokens watching a running job: no polling, no repeated status checks. State the expected end time and stop. Check only when the user asks.
- Speed is not a reason to parallelize. Run at most MAX_SUBAGENTS, and check the first result before launching more.

## 3. Split phases across models

A task that **collects**, **reasons** and **writes** can hand each phase to a different model through subagents, in the same chat.

If subagents are not available in this environment, do every phase in the chat and skip this section: sections 1, 2 and 4 still apply.

Split only above the threshold: more than HEAVY_SEARCHES or more than HEAVY_DOCS. Below it, do everything in the chat, because a subagent has a fixed start-up cost that can exceed the saving. Propose the split yourself when the threshold is crossed.

| Phase | Who does it |
|---|---|
| Collection and extraction | subagent on CHEAP_MODEL |
| Research that must judge or choose sources | subagent on JUDGE_MODEL |
| Reasoning | the main chat |
| Writing | the main chat |

- Always specify model **and** effort for each subagent. Never let it inherit the main chat's settings silently. Where effort cannot be set, write it at the top of the brief.
- Write every brief from the fixed templates in [briefs.md](briefs.md). The full result goes to a file; only counts and the file path come back to the chat.
- Never use CHEAP_MODEL for judgement, choices, final text or sensitive areas.
- If CHEAP_MODEL invents even one item in real use, stop using it for that kind of task.

## 4. Switch chats at the right moment

At the end of each step, say whether to continue in this chat or open a new one, and with which model and effort.

Recommend a new chat when:
- a new block of work starts;
- the next step needs a different model or effort;
- the chat was summarized or compacted, or changed topic more than twice;
- an independent check is needed (the reviewer must not be the chat that did the work);
- an attempt failed and a different approach is next.

Do not switch in the middle of an implementation or while correcting the work in progress.

Before any switch, write the current state (done, decided, next) to a document the user keeps, and give the opening prompt for the new chat, pointing to that document instead of repeating it.

## 5. Keep instructions lean

- If a rule from another skill or instruction is already here, do not repeat it there: reference this skill.
- Answers start with the result. Explain only what is needed.
