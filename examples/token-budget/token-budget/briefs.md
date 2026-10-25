# Subagent brief templates

Use these templates exactly. The hand-off between phases is where quality is lost, so the brief is always written the same way.

## Collection brief

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

## Research brief (when sources must be judged)

```
Effort: medium

Question: <what must be answered>
Scope: <where to look, what to exclude>
Rules:
- Prefer primary sources. Record the date of each source.
- Separate facts from interpretation.
Output:
- Save findings to <path>, each with source link and date.
- Reply only with: number of sources kept, number discarded and why,
  file path.
```

## Reasoning brief (only when reasoning is delegated)

```
Effort: high

Question: <the question to answer>
Input: <path of the collection or research file>
Constraints: <rules that apply>
Output: an analysis with the conclusion, the assumptions used and
what is missing. No final text for the reader.
```
