# Glossary

Short definitions of the terms used in this repository. Add a term when a technique needs it.

| Term | Meaning |
|---|---|
| **Token** | The unit Claude reads and writes. Usage limits and API costs are counted in tokens. |
| **Input tokens** | Everything Claude reads for a request: instructions, conversation history, attachments, tool results. |
| **Output tokens** | Everything Claude writes in its answer, including any visible reasoning. |
| **Context** | The full set of input Claude sees for one request. |
| **Effort** | How much reasoning a model is asked to put into a task, where the interface or API lets you choose. |
| **Model routing** | Sending each part of a task to the model and effort level that fits it. |
| **Caching** | Reusing a part of the input that does not change, so it is not processed in full every time. |
| **Skill** | A packaged set of instructions Claude loads only when a task needs it. |
| **Subagent** | A separate Claude instance that handles one part of a task and returns only the result. |
