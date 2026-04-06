# How To Use This Skill

## The Short Version

Give the agent:

- the topic,
- the scope,
- the venue preference,
- the output you want.

The more precise version is:

> topic + boundaries + source preference + output format

## Good Prompt Shapes

### 1. Standard Literature Review

```text
Do a finance literature review on bank competition and financial stability.
Start with top finance journals, then top economics journals if needed.
Give me a prioritized reading list, a literature matrix, and 5 research gaps.
```

### 2. Published-Only Review

```text
Review the published literature on payout policy after tax changes.
Use top finance journals first and exclude working papers unless they are essential for context.
I want a related-literature section outline and a matrix by identification strategy.
```

### 3. Frontier Scan

```text
Scan the frontier literature on AI and bank lending.
Separate published papers from NBER, CEPR, SSRN, and RePEc working papers.
Highlight what is still provisional.
```

### 4. Accounting-Adjacent Topic

```text
Map the disclosure literature relevant to the cost of capital.
Use top accounting journals and top finance journals.
For each core paper, capture the mechanism, identification strategy, and limitation.
```

### 5. Dissertation-Oriented Use

```text
I am planning a dissertation chapter on climate risk and asset pricing.
Give me a literature review structured into theory, measurement, identification, and frontier open questions.
Prioritize papers that would matter for top finance journals.
```

## What The Skill Will Usually Return

- a scoped review question,
- a venue-prioritized reading list,
- a literature matrix,
- a synthesis by theme and design,
- explicit research gaps,
- a citation block.

## Best Optional Constraints To Add

- geography: `US only`, `cross-country`, `emerging markets`
- period: `post-2000`, `pre-GFC vs post-GFC`, `recent 5 years`
- source mix: `published only`, `include frontier working papers`
- output type: `matrix`, `narrative synthesis`, `related literature section`, `reading list`, `dissertation memo`
- method focus: `difference-in-differences`, `event studies`, `structural`, `textual analysis`

## Output Modes

### Reading List Mode

Best when you want fast orientation.

Ask for:

```text
Give me a prioritized reading list on ...
```

### Matrix Mode

Best when you want to compare empirical strategies.

Ask for:

```text
Build a literature matrix on ...
```

### Related Literature Mode

Best when you want draft-ready prose.

Ask for:

```text
Write a related literature section on ...
```

### Gap Map Mode

Best when you are choosing a project.

Ask for:

```text
Identify research gaps in ...
```

## What To Expect On Weak Evidence

If the literature is mostly recent working papers, the skill should tell you that directly.

If only titles and abstracts are available, the skill should say that directly instead of pretending the full papers were reviewed.

If a topic is mature in economics but thin in finance, the skill should widen to economics and say why.
