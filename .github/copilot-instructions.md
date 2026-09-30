# Finance Literature Review Instructions

Use this workflow when the user asks for a literature review, related literature section, annotated bibliography, gap analysis, or finance / economics / accounting paper scan.

## Core Defaults

- Prioritize top finance journals (JF, JFE, RFS), subfield leaders (JFQA, RCFS, RAPS, JMCB, JCF), top economics (Top 5), and top accounting (Top 5).
- **Dynamic Working Paper Integration**: Never automatically rank working papers at the bottom. Tier them into Tier 1 (NBER, CEPR, Central Banks, Top 3/5 R&Rs, AFA/WFA/NBER SI), Tier 2, and Tier 3. For frontier/emergent topics, Tier 1 working papers sit co-equal with Top 3 publications.
- **Systematic Working Paper Discovery**: Query SSRN FEN eJournals, NBER programs (`CF`, `AP`, `ME`), CEPR, Central Bank series (FEDS, NY Fed, BIS, ECB), annual conference programs (AFA, WFA, EFA, NBER SI), RePEc/IDEAS NEP reports, and finance JEL codes (`G1`, `G2`, `G3`, `M4`, `E4/E5`).
- **Abstract Quarantine & Anti-Hallucination**:
  - Never infer identification strategy, fixed effects, clustering, or numerical magnitudes from an abstract alone.
  - If only an abstract is available, tag `[Abstract-Only Provisional]`, preface statements with *"Author claims in abstract (unverified): ..."*, and mark design fields unverified.
  - Abstract-only papers **cannot** establish definitive ownership or declare research gaps settled.
- **3-Anchor Introduction Protocol**: Retrieve the Introduction (Paras 3–11) and baseline table notes to verify: (1) Setting & specific exogenous shock, (2) Quantitative magnitude, (3) Self-stated contribution relative to benchmark papers.
- **Intellectual Lineage**: Distinguish Theoretical Originator $\rightarrow$ Empirical Landmark $\rightarrow$ Causal ID Benchmark $\rightarrow$ Boundary Reassessment. Record both what a paper established and its boundary conditions (what it left open).

## Hard Rules

- Never fabricate citations, DOI values, or journal placements.
- Always separate published papers from working papers, verify if older working papers were subsequently published, and record screening signals (R&R status, conference presentation).
- For empirical papers, record:
  - research question,
  - setting and primary data infrastructure (Compustat, CRSP, Dealscan, Call Reports, HMDA, TRACE),
  - sample period and screens/filters,
  - unit of observation,
  - identification strategy and specific exogenous shock / source of variation,
  - econometric nuance (fixed effects structure, clustering, staggered DiD diagnostics),
  - verified main outcome and economic magnitude,
  - mechanism / transmission channel,
  - boundary conditions and identification threats (what the paper leaves open),
  - venue tier and verification status.
- If only metadata or abstracts are available, state that explicitly.

## Preferred Output Shape

- one-paragraph scope definition and topic maturity assessment,
- venue-prioritized reading list,
- 16-column literature matrix with verification levels and lineage roles,
- synthesis by mechanism, intellectual lineage, and research design,
- explicit research gaps and dissertation/positioning proposals grounded in boundary conditions,
- verified citation block.
