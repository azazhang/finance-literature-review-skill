# Paper Contribution, Ownership, and Anti-Hallucination Protocol

A primary failure mode in AI-assisted literature reviews is the **"Abstract Trap"**: an agent reads only the abstract of a paper, hallucinates the study's empirical methodology, invents its quantitative findings, and paraphrases the abstract's marketing claims into an inflated "contribution."

This destroys literature mapping, creates false intellectual ownership, and misleads researchers who are positioning their own work. This protocol establishes strict reading, verification, and extraction standards for academic finance.

---

## 1. The "Abstract Trap" and Why It Destroys Literature Reviews

Abstracts in finance and economics are marketing instruments designed to highlight broad implications. They **never** contain the detailed proof of causal identification, the full structure of fixed effects, the validity of instruments, sample attrition filters, or economic magnitudes.

When an agent reads only an abstract:
1. **It fabricates methodology**: It assumes standard DiD or IV without knowing if the paper is a calibrated model, cross-sectional OLS, or an event study.
2. **It invents economic magnitude**: It turns vague phrases like *"we find a significant effect"* into manufactured percentage changes or statistical assertions.
3. **It muddles intellectual ownership**: It credits a modern paper with discovering a mechanism that Diamond & Dybvig (1983) or Holmström & Tirole (1997) derived theoretically, or that an earlier empirical landmark established.
4. **It ruins the researcher's differentiation**: In a related-literature section, an author must pinpoint *precisely* what prior work did and left open (e.g., *"Author (2020) examines syndicated loans in Dealscan from 2000–2012; we examine granular loan-level Call Report data post-2018..."*). If the agent guessed the prior contribution, the author's positioning is invalid.

---

## 2. Three-Tier Evidence Verification Quarantine

Every paper evaluated must carry an explicit verification tag:

### Tier A: `[Full-Text Verified]`
* The agent accessed the full publication or working paper PDF/text.
* Exact econometric specifications, table notes, and robustness sections were inspected.

### Tier B: `[Intro / Table Verified]`
* The agent retrieved the paper's Introduction (pages 1–6) and primary baseline regression tables (Table 1, 2, or 3).
* This provides ~95% of true identification, magnitude, and ownership details without needing all 60 pages.

### Tier C: `[Abstract-Only (Provisional)]` — HARD QUARANTINE
If only the abstract is accessible:
* **Strict Prohibition**: The agent is **strictly barred** from asserting specific econometric identification (e.g., "staggered DiD with firm FE"), standard error clustering, or numerical magnitudes.
* **Mandatory Framing**: All statements must be prefaced: *"Author claims in abstract (unverified): ..."*
* **Ownership Bar**: Abstract-only papers **cannot** be used to establish definitive intellectual ownership, dispute prior claims, or declare a research gap settled.
* **Flag Missing Text**: The agent must output: `[Full text unverified; methodology and boundary conditions unconfirmed]`.

---

## 3. The 3-Anchor Introduction Protocol

In top finance and economics journals (*JF*, *JFE*, *RFS*, *AER*, *QJE*, *JPE*, *Econometrica*, *ReStud*), papers adhere to a standardized Introduction structure across paragraphs 1 to 11. Agents must target three specific anchors rather than summarizing the abstract:

```
[Para 1–2] Big Picture Question & Economic Motivation
     │
     ▼
[Para 3–4] ──▶ ANCHOR 1: THE EMPIRICAL DESIGN / SHOCK ANCHOR
     │         • Exact data sources (e.g., Dealscan, TRACE, Call Reports)
     │         • Specific natural experiment / policy shock / discontinuity
     │         • Core identification strategy
     ▼
[Para 5–6] ──▶ ANCHOR 2: THE QUANTITATIVE MAGNITUDE ANCHOR
     │         • Baseline coefficient & economic significance
     │         • Real-world dollar/basis-point impact for the median firm
     │         • Primary falsification / placebo test
     ▼
[Para 7–8] Mechanism & Ruling Out Alternative Explanations
     │         • How channel A is isolated from alternative stories B and C
     ▼
[Para 9–11] ─▶ ANCHOR 3: THE SELF-STATED CONTRIBUTION & OWNERSHIP ANCHOR
               • Usually begins: "Our paper contributes to several literatures..."
               • Explicitly names 3–4 landmark papers and defines incremental boundary
```

### Table Notes Inspection
Whenever accessing tables:
* Inspect **Table 1** (Summary Statistics): Note the sample size ($N$), time window, and standard filters (e.g., excluding financials SIC 6000–6999 or share price < $5).
* Inspect **Table 2 / 3** (Baseline Regressions): Read the table footer notes to confirm:
  * Dependent variable definition.
  * Included fixed effects (e.g., `Firm FE: Yes`, `Industry × Year FE: Yes`).
  * Standard error clustering (e.g., `Clustered by Firm and Year`).

---

## 4. The 4-Stage Intellectual Lineage & Ownership Framework

To prevent misattributing ownership, agents must assign each paper to its proper role in the intellectual lineage:

1. **Theoretical Originator**:
   * The paper that first derived the mathematical or economic mechanism (e.g., Modigliani & Miller 1958; Jensen & Meckling 1976; Myers & Majluf 1984; Diamond & Dybvig 1983; Holmström & Tirole 1997).
   * *Rule*: Never credit an empirical paper with "discovering" a theoretical mechanism unless it developed a new formal model.
2. **First Empirical Landmark**:
   * The first paper to document the empirical regularity or stylized fact (often cross-sectional OLS or event study, with acknowledged endogeneity).
3. **Causal Identification Benchmark**:
   * The paper that first solved endogeneity using a credible exogenous shock, quasi-natural experiment, or clean instrument (e.g., Khwaja & Mian 2008 for credit supply; Becker, Ivashina & Raeh 2014).
4. **Boundary / Heterogeneity / Reassessment**:
   * Subsequent papers that test boundary conditions, explore heterogeneous effects across subsamples, or re-evaluate earlier findings using modern econometrics (e.g., modern staggered DiD estimators).

---

## 5. The "What It Establishes vs. What It Leaves Open" Protocol

For every core paper in the review, the agent must document two distinct elements:

1. **What It Actually Established**:
   * The verified causal effect within the specific sample and time period examined.
   * State the exact shock and mechanism tested.
2. **What It Left Open (The Boundary Condition)**:
   * What the authors themselves acknowledge they cannot observe or test:
     * Sample restrictions (e.g., only large publicly traded US firms; private firms unobserved).
     * Time horizon limits (e.g., pre-2008 financial crisis sample; post-crisis regulation unstudied).
     * Institutional limits (e.g., bank balance-sheet lending only; shadow banking / bond substitution unobserved).
     * Unresolved alternative mechanisms.

*Why this matters*: Literature gaps live exclusively inside what previous papers left open. If an agent does not record boundary conditions, it cannot formulate a credible research gap.

---

## 6. The Anti-Paraphrase Anchor Quote Rule

* **Rule**: If an agent cannot quote or directly verify the specific empirical setting, shock, or coefficient from the text, it is strictly forbidden from inferring it.
* In such cases, the agent must record `[Unverified from text]` rather than generating plausible speculation.
