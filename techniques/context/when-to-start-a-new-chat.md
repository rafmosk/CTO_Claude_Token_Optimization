# When to start a new chat

**Area:** context
**Works in:** all
**Tested with:** large models at low and medium effort
**Status:** tested
**Author:** @rafmosk

## Problem
In a conversation the earlier messages are usually processed again at every new turn. A long thread that has covered several topics makes every message more expensive, and old reasoning (including wrong turns) keeps influencing the answers. Starting over too often has the opposite cost: context has to be rebuilt by hand.

## Technique
Switch chats at clear moments, and always write the state down before switching.

### Start a new chat when
- A new block of work begins (for example, a proposal is approved and a new piece of work starts).
- The next step needs a different model or effort level from the current chat.
- The chat has been summarized or compacted, or has changed topic more than twice.
- You need an independent check: the reviewer should not be the chat that wrote the work.
- An attempt failed and you want to try a different approach. The failed reasoning stays in context and tends to come back.
- A bug fix is closed and you move to the next piece.

### Stay in the same chat when
- You are correcting or recording the work in progress.
- You are in the middle of an implementation. Finish the current step first, or names, paths and partial state get lost.

### Before switching
1. Write the current state in a document or in the repository: what is done, what is decided, what is next.
2. The first message of the new chat **points to that document** instead of repeating its content.
3. Ask Claude to say at the end of each step whether to continue here or open a new chat, and with which model.

### Text to paste

```
At the end of each step, tell me whether to continue in this chat or
open a new one, and with which model and effort. Recommend a new chat
when a new block of work starts, the next step needs a different
model, the chat was summarized or changed topic more than twice, an
independent check is needed, or an attempt failed. Before any switch,
write the current state to <document> and give me the opening prompt
for the new chat, pointing to that document.
```

## Example
*Illustrative.*

**Before:** one chat used for design, then implementation, then a review of the same implementation, then an unrelated question.

**After:** design chat ends by writing decisions to `STATUS.md`. A new chat implements, pointing to `STATUS.md`. A third, fresh chat reviews only the change.

## Saving
| Metric | Value | Type |
|---|---|---|
| Input per message | Lower in short, focused chats than in a long mixed thread | estimated, not measured |

A benchmark comparing one long thread with the same work split into focused chats is welcome: see [../../docs/measuring.md](../../docs/measuring.md).

## Trade-offs
- Writing the state takes a few minutes.
- Anything not written down is lost in the switch.

## When not to use it
- Short conversations on a single topic.
- In the middle of a step that has not reached a stable point.

## Related
- [estimate-before-heavy-work.md](estimate-before-heavy-work.md)
