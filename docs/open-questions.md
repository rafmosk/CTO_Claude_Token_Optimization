# Open questions

What we do not know yet. These are the places where other people's experience can improve the skill the most. Ideas and first-hand observations are welcome; you do not need to measure anything to answer.

To answer one, open an issue with the **Idea** or **Improve the skill** template and mention the question number.

## About splitting work across models

1. **Where is the right threshold?** The skill splits work only above 3 web searches or 5 long documents. That value comes from one setup. Is it too low, too high, or different by kind of task?
2. **Does the small model hold up beyond extraction?** It matched the large model on structured extraction. What about classification, summaries or filtering? Where does it start to fail?
3. **How big is a subagent's start-up cost in a lighter setup?** It was 90,000 to 150,000 tokens in a setup with many instructions loaded. With few or no custom instructions, is it much lower? If so, the threshold in question 1 should drop.

## About usage and cost

4. **How do subscription usage indicators weigh different models?** Two models with the same token count may consume the allowance very differently. This is not documented. Has anyone observed it?
5. **Which effort level is enough for which task?** The skill uses low effort for collection and medium for research that judges sources. Has anyone found tasks where a lower level works just as well?

## About conversations and skills

6. **How expensive are long threads in practice?** Earlier messages are processed again at each turn, but some environments reuse unchanged content more cheaply. How much does starting a new chat really save?
7. **How do you make a skill load in every chat in the Claude app** without adding a line to personal instructions? Is there a better way?
8. **What is the right size for a skill?** Every line of `SKILL.md` is read whenever it loads. Which rules are worth their cost, and which could move to a separate file read only when needed?

## Have a question of your own?

Open an issue with the **Idea** template. Good questions get added here.
