# How To Use This Skill

## The Short Version

Give the agent:

- the topic and mechanism,
- the scope (period, geography, subfield),
- whether the topic is frontier/emergent or mature,
- the output mode you want.

The formula is:

> topic + empirical setting + source preference + output format

---

## Good Prompt Shapes

### 1. Frontier Scan with Dynamic Working Paper Hierarchy

```text
Do a finance literature review on private credit growth and corporate borrowing.
Treat this as a frontier topic: prioritize Tier 1 working papers (NBER, CEPR, Central Banks, Top 3 R&Rs, AFA/WFA presentations) alongside top finance journal publications.
Deliver a 14-column literature matrix and identify 3 key identification gaps.
```

### 2. Standard Review with Published Anchors

```text
Do a finance literature review on bank competition and financial stability.
Start with core finance journals (JF, JFE, RFS) and adjacent Top 5 economics journals.
Search recent NBER/CEPR papers and top conference programs for modern reassessments.
Give me a prioritized reading list, a literature matrix, and 5 research gaps.
```

### 3. Published-Only Review with Methodological Focus

```text
Review the published empirical literature on shareholder payouts following corporate tax shocks.
Use top finance and top accounting journals, and focus on quasi-natural experiments and staggered DiD designs.
I want a related-literature section draft and a matrix detailing the exogenous shocks and clustering methods.
```

### 4. Accounting-Adjacent Disclosure Topic

```text
Map the disclosure literature relevant to the cost of capital.
Include top accounting journals (JAR, JAE, TAR, RAST, CAR) and top finance journals.
For each core paper, capture the primary dataset (e.g., Compustat, I/B/E/S, SEC filings), the identification shock, mechanism, and endogeneity threats.
```

### 5. Dissertation Chapter / Grant Proposal Positioning

```text
I am planning a dissertation second chapter on climate transition risk and municipal bond pricing.
Search SSRN FEN and recent AFA/WFA/NBER programs for frontier working papers, plus published foundations in JF/JFE/RFS.
Give me a Gap Map detailing settled facts vs. contested empirical questions, and propose 3 viable empirical designs.
```

---

## What The Skill Returns

- **Scoped Question & Topic Maturity Classification**: Explicitly flags whether the topic is frontier/emergent (Tier 1 working papers co-equal) or mature (peer-reviewed anchors).
- **Search Grid & Discovery Log**: Demonstrates queries across SSRN FEN, NBER programs, CEPR, central banks, top conferences, and JEL codes.
- **Venue-Prioritized Reading List**: Categorized by Core Finance, Subfield Leaders, Top Econ/Accounting, and Tiered Working Papers.
- **16-Column Literature Matrix**: Complete table capturing data infrastructure, exogenous shocks, fixed effects, clustering, mechanisms, verification levels (`[Full-Text]`, `[Intro/Table]`, `[Abstract-Only]`), and boundary conditions (what it leaves open).
- **Abstract Quarantine & Lineage Mapping**: Prevents hallucinated contributions by quarantining abstract-only papers and distinguishing theoretical originators from causal identification benchmarks.
- **Synthesis by Mechanism & Design**: Contrasts causal designs and theoretical transmission channels.
- **Explicit Research Gaps**: Concrete identification or institutional opportunities for new research.
- **Verified Citation Block**: Real author names, publication years, and screening signals.

---

## Key Parameters You Can Specify

- **Subfield**: `Asset Pricing`, `Corporate Finance`, `Banking & Financial Intermediation`, `Accounting & Disclosure`, `Macro-Finance`.
- **Topic Maturity**: `Frontier / Rapidly Evolving` (e.g., FinTech, SVB/banking crisis, ESG) vs. `Mature Paradigm` (e.g., pecking order, CAPM anomalies).
- **Data Infrastructure**: `Compustat/CRSP`, `Dealscan`, `TRACE`, `Call Reports (FFIEC)`, `HMDA`, `TAQ`, `SEC EDGAR`.
- **Methodology Focus**: `Staggered DiD (Callaway-Sant'Anna/Sun-Abraham)`, `Instrumental Variables / Bartik`, `Fuzzy RDD`, `Khwaja-Mian FE`, `Structural Estimation`.
- **Output Mode**: `Reading List`, `Literature Matrix`, `Related Literature Section`, `Gap Map`.

---

## Output Modes

### 1. Reading List Mode
Best when you want fast orientation, syllabus building, or PhD exam preparation with explicit Tier 1 working paper signals.

### 2. Literature Matrix Mode
Best when you want to compare empirical strategies, datasets, fixed effects structures, and causal shocks across papers.

### 3. Related Literature Mode
Best when you are writing a paper and need publication-ready prose organized by theoretical channel and causal design.

### 4. Gap Map Mode
Best when choosing a research topic, evaluating dissertation ideas, or pitching a new project to an advisor or coauthor.
