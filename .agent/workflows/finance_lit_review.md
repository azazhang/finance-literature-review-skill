---
description: Finance-first literature review workflow with dynamic venue prioritization, working paper tiering, empirical identification tracking, abstract quarantine, and 3-anchor introduction extraction.
---

# Finance Literature Review Workflow

Use this workflow when the user asks for:

- a finance literature review,
- a related literature section,
- an annotated bibliography,
- a finance reading list,
- a working-paper scan,
- a gap map across finance, economics, and accounting.

## Core Rules

- Prioritize core finance journals (JF, JFE, RFS), subfield leaders (JFQA, RCFS, RAPS, JMCB, JCF), top economics (Top 5), and top accounting (Top 5).
- **Dynamic Working Paper Integration**: Never automatically rank working papers at the bottom. Tier them into Tier 1 (NBER, CEPR, Central Banks, Top 3/5 R&Rs, AFA/WFA/NBER SI), Tier 2, and Tier 3. For frontier/emergent topics, Tier 1 working papers sit co-equal with Top 3 publications.
- **Systematic Working Paper Discovery**: Query SSRN FEN eJournals, NBER programs (`CF`, `AP`, `ME`), CEPR, Central Bank series (FEDS, NY Fed, BIS, ECB), annual conference programs (AFA, WFA, EFA, NBER SI), RePEc/IDEAS NEP reports, and finance JEL codes (`G1`, `G2`, `G3`, `M4`, `E4/E5`).
- **Abstract Quarantine & Anti-Hallucination**:
  - Never infer identification strategy, fixed effects, clustering, or numerical magnitudes from an abstract alone.
  - If only an abstract is available, tag `[Abstract-Only Provisional]`, preface statements with *"Author claims in abstract (unverified): ..."*, and mark design fields unverified.
  - Abstract-only papers **cannot** establish definitive ownership or declare research gaps settled.
- **3-Anchor Introduction Protocol**: Retrieve the Introduction (Paras 3–11) and baseline table notes to verify: (1) Setting & specific exogenous shock, (2) Quantitative magnitude, (3) Self-stated contribution relative to benchmark papers.
- **Intellectual Lineage**: Distinguish Theoretical Originator $\rightarrow$ Empirical Landmark $\rightarrow$ Causal ID Benchmark $\rightarrow$ Boundary Reassessment.
- Record both what a paper established and its boundary conditions (what it left open).
- Never fabricate citations or metadata.
- If only titles or abstracts are available, say so directly.

## Extraction Checklist (16 Columns)

For each core empirical paper, record:

1. Theme / Subtopic
2. Citation & Year
3. Venue & Status (Published vs. Series / R&R / Conference)
4. Venue Tier (`F1 Core`, `F1 Field`, `Econ Top 5`, `Acct Top 5`, `Tier 1 WP`, `Tier 2 WP`, `Tier 3 WP`)
5. Verification Level (`[Full-Text Verified]`, `[Intro / Table Verified]`, `[Abstract-Only Provisional]`)
6. Lineage & Intellectual Role (Theoretical Originator, Empirical Landmark, Causal ID Benchmark, Boundary / Reassessment)
7. Research Question
8. Setting & Primary Data Infrastructure (Compustat, CRSP, Dealscan, Call Reports, HMDA, TRACE, etc.)
9. Sample Period & Filters
10. Unit of Observation
11. Identification Strategy & Source of Exogenous Variation
12. Econometric Nuance & Fixed Effects (e.g., firm/year FE, clustering, staggered DiD diagnostics)
13. Verified Finding & Economic Magnitude
14. Mechanism / Transmission Channel
15. Boundary Condition & What It Leaves Open
16. Positioning Value & Open Gap

## Default Deliverables

- scope note and topic maturity classification,
- prioritized reading list,
- 16-column literature matrix with verification levels and lineage roles,
- synthesis by mechanism, intellectual lineage, and econometric design,
- explicit research gaps grounded in boundary conditions,
- verified citation block.
