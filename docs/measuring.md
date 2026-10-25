# How to measure a saving

A saving is credible only if someone else can repeat the measurement and get a similar result.

## Three kinds of numbers

| Type | Meaning | Example |
|---|---|---|
| **Measured** | Read from a real run | Token counts returned by the API for an actual request |
| **Calculated** | Derived from measured numbers with a stated formula | Average of five measured runs |
| **Estimated** | A reasoned guess, without a measurement | "Roughly half, judging from the length of the prompt" |

Always say which one you are using. Never put estimates in the same table as measurements.

## Minimum method

1. **Same task, two variants.** Keep everything identical except the technique.
2. **Same model and effort level** for both variants.
3. **At least three runs per variant.** Answers vary between runs; one run proves little.
4. **Count input and output separately.** Many techniques reduce one and increase the other.
5. **Check quality.** Compare the answers. If the "after" answer is worse, record it.
6. **Write down the limits.** One task on one model does not prove the technique works everywhere.

## Where token counts come from

- **API:** every response reports the input and output tokens used.
- **Claude Code and the Claude app:** use whatever usage information the interface shows, and describe exactly what you read and where.

If you are not sure how a number was obtained, label it as *estimated*.

## Conversations with many turns

In a multi-turn conversation the earlier messages are usually sent again at each turn, so a long thread costs more per message than a short one. When a technique affects conversation length, measure the whole conversation, not a single message.
