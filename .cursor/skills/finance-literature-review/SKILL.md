---
name: finance-literature-review
description: Conduct finance-first literature reviews, related-literature sections, and research synthesis. Use when the user asks for a literature review, related literature section, annotated bibliography, gap map, journal-targeted reading list, finance/macro-finance paper scan, corporate finance or asset-pricing synthesis, banking/intermediation summary, disclosure review, or working paper discovery. Prioritizes top finance journals (JF, JFE, RFS), subfield leaders, top economics (Top 5), top accounting (Top 5), and dynamically integrates elite working papers (NBER, CEPR, Central Banks, R&Rs, AFA/WFA). Enforces strict abstract quarantine and introduction/table verification to prevent hallucinated contributions.
---

# Finance Literature Review

## Purpose

Run a rigorous, PhD-level finance literature review that reflects the standards of top finance seminars, referee reports, and dissertation chapters.

Key objectives:
1. Scope the research question and identify topic maturity (frontier vs. mature paradigm).
2. Prioritize venues using a dynamic hierarchy that values elite working papers alongside top peer-reviewed journals.
3. Systematically discover working papers via SSRN FEN, NBER programs, CEPR, central bank series, and premier conference programs.
4. **Enforce the Abstract Quarantine**: Prohibit agents from inferring contributions, econometric designs, or magnitudes from abstracts alone.
5. **Execute the 3-Anchor Introduction Protocol**: Retrieve the Introduction (Paras 3–11) and baseline table notes to verify actual causal variation, quantitative magnitudes, and self-stated contributions.
6. **Map Intellectual Lineage & Ownership**: Distinguish Theoretical Originators from Empirical Landmarks, Causal Identification Benchmarks, and Boundary Reassessments. Record what previous papers established vs. what they left open.
7. Deliver actionable outputs (reading list, 16-column literature matrix, related literature section, or research gap map).

---

## Detailed References

* **Contribution Extraction & Anti-Hallucination Protocol**: [references/contribution-extraction.md](references/contribution-extraction.md)
* **Working Paper Discovery & Evaluation**: [references/working-papers.md](references/working-papers.md)
* **Venue Hierarchy & Dynamic Weighting**: [references/journal-priority.md](references/journal-priority.md)
* **Output Modes & Formats**: [references/output-modes.md](references/output-modes.md)
* **Synthesis & Delivery Checklist**: [references/synthesis-checklist.md](references/synthesis-checklist.md)
* **Literature Matrix Template**: [templates/literature-matrix.md](templates/literature-matrix.md)

---

## Hard Rules

- **Zero Citation Fabrication**: Never fabricate citations, authors, publication years, or venue tiers.
- **Abstract Quarantine & No Inferred Contributions**: Never infer identification strategies, fixed effects, clustering, or numerical magnitudes from an abstract alone. If only the abstract is accessible, tag the paper `[Abstract-Only Provisional]`, preface statements with *"Author claims in abstract (unverified): ..."*, and mark empirical design fields as unverified. Abstract-only papers **cannot** establish definitive literature ownership or declare research gaps settled.
- **Dynamic Working Paper Integration**: Never automatically dump working papers into a bottom tier. Tier working papers into Tier 1 (NBER, CEPR, Central Banks, Top 3/5 R&Rs, AFA/WFA/NBER SI), Tier 2, and Tier 3. On frontier topics, Tier 1 working papers sit co-equal with Top 3 publications for mechanisms and current evidence.
- **Publication Status Verification**: Check whether older working papers have been published in peer-reviewed journals.
- **Empirical Rigor**: Explicitly extract the specific policy shock/exogenous variation, datasets (Compustat, CRSP, Dealscan, Call Reports, etc.), fixed effects, and identification limitations.
- **Synthesize by Mechanism & Lineage**: Structure syntheses by economic transmission channel and intellectual lineage, never simple author chronologies. Record both what a paper established and its boundary conditions (what it left open).
- **State Evidence Limits Transparently**: If evidence is provisional or only abstracts/preprints are available, state that directly.

---

## 6-Step Workflow

### Step 1: Scope & Topic Maturity
Clarify the economic mechanism, institutional setting, geographic scope, sample window, and output mode. 
* **Assess topic maturity**: Is this a **frontier/emergent topic** (e.g., GenAI in finance, private credit, recent bank run mechanisms) where Tier 1 working papers lead the literature, or a **mature paradigm** (e.g., capital structure trade-off, asset pricing anomalies) where peer-reviewed top-journal papers form the bedrock?
* **Identify relevant subfields**: Asset Pricing, Corporate Finance/Governance, Banking/Financial Intermediation, Macro-Finance, or Accounting/Disclosure.

### Step 2: Build the Search Grid & Query Plan
Construct an exhaustive search grid combining:
1. **Core Concept Terms & Finance Synonyms**: (e.g., "bank capital", "regulatory arbitrage", "risk-weighted assets").
2. **Finance JEL Codes**: Guide queries using `G1` (Financial Markets), `G2` (Financial Institutions), `G3` (Corporate Finance), `M4` (Disclosure/Accounting), `E4/E5` (Monetary Transmission).
3. **Identification & Shock Keywords**: Specific policy shocks (e.g., "Dodd-Frank", "TCJA 2017", "Basel III", "Russell reconstitution"), method keywords (e.g., "staggered difference-in-differences", "fuzzy RDD", "Khwaja-Mian").
4. **Data Infrastructure Terms**: (e.g., "Compustat", "CRSP", "Dealscan", "Call Reports", "HMDA", "TRACE", "TAQ", "10-K text").
5. **Systematic Working Paper Channels**:
   * SSRN Financial Economics Network (FEN) subject eJournals.
   * NBER research programs (`CF`, `AP`, `ME`, `PE`) and CEPR discussion papers.
   * Central Bank series (Federal Reserve Board FEDS, NY Fed Staff Reports, BIS, ECB).
   * Annual conference programs (AFA, WFA, EFA, NBER Summer Institute, SFS Cavalcade).
   * RePEc/IDEAS NEP weekly reports (`nep-ban`, `nep-cfn`, `nep-fmk`, `nep-mon`).
   * arXiv `q-fin` for quantitative finance and FinTech/ML.

### Step 3: Collect & Full-Text / Introduction Retrieval
* **Do not stop at the abstract**: Retrieve the manuscript or open-access working paper PDF/HTML (via SSRN, NBER, OpenAlex, institutional repository, or publisher).
* For mature topics: collect seminal Top 3/Top 5 published papers first, follow forward citation chains, and capture modern working paper re-examinations.
* For frontier topics: capture active Tier 1 working papers, check their R&R or top conference screening status, and complement with published foundational models.
* Cross-check whether working papers have subsequently been published.

### Step 4: Extract via the 3-Anchor Protocol (16-Column Matrix)
Using [templates/literature-matrix.md](templates/literature-matrix.md), execute [references/contribution-extraction.md](references/contribution-extraction.md):
* **Target the 3 Introduction Anchors**:
  * *Anchor 1 (Paras 3–4)*: Setting, exact dataset, and specific exogenous shock.
  * *Anchor 2 (Paras 5–6)*: Baseline quantitative findings and economic magnitude.
  * *Anchor 3 (Paras 9–11)*: Self-stated contribution and incremental boundary relative to benchmark papers.
* **Inspect Table Notes**: Dependent variables, included fixed effects, and clustering level.
* **Tag Verification Level**: `[Full-Text Verified]`, `[Intro / Table Verified]`, or `[Abstract-Only Provisional]`.
* **Record Lineage Role**: Theoretical Originator, First Empirical Landmark, Causal ID Benchmark, or Boundary / Reassessment.
* **Separate Verified Claim from Boundary Condition**: Record what the paper established and what it left open.

### Step 5: Synthesize by Mechanism & Lineage
Synthesize findings along economic channels:
* Contrast differing empirical findings by their identification strategies and sample settings (e.g., why cross-sectional OLS diverges from quasi-experimental DiD estimates).
* Preserve theoretical ownership: credit theoretical originators for mechanisms, and causal benchmarks for identification.
* Delineate boundary conditions: use what previous papers left open to establish true research gaps.

### Step 6: Deliver & Verify
Produce the selected output format ([references/output-modes.md](references/output-modes.md)):
* Prioritized Reading List
* Complete Literature Matrix
* Related Literature Section (draft-ready prose)
* Gap Map & Research Proposals

Run through [references/synthesis-checklist.md](references/synthesis-checklist.md) before presenting final deliverables.
