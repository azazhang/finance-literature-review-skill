# Repo Context

This repository packages a finance-oriented literature review workflow for multiple coding agents.

## Working Rules

- Keep provider-native files aligned when the core workflow changes.
- Prioritize top finance journals (JF, JFE, RFS), subfield leaders, top economics (Top 5), and top accounting (Top 5).
- **Dynamic Working Paper Integration**: Never automatically rank working papers at the bottom. Tier them into Tier 1 (NBER, CEPR, Central Banks, Top 3/5 R&Rs, AFA/WFA/NBER SI), Tier 2, and Tier 3. For frontier/emergent topics, Tier 1 working papers sit co-equal with Top 3 publications.
- **Systematic Working Paper Discovery**: Search working paper channels: SSRN FEN eJournals, NBER programs (`CF`, `AP`, `ME`, `PE`), CEPR, Central Bank series (FEDS, NY Fed, BIS, ECB), conference programs (AFA, WFA, EFA, NBER SI), and finance JEL codes (`G1`, `G2`, `G3`, `M4`, `E4/E5`).
- **Abstract Quarantine & Anti-Hallucination**:
  - Never infer identification strategy, fixed effects, clustering, or quantitative magnitude from an abstract alone.
  - When only the abstract is available, tag `[Abstract-Only Provisional]`, preface statements with *"Author claims in abstract (unverified): ..."*, and mark design fields unverified.
  - Abstract-only papers **cannot** establish definitive intellectual ownership or declare research gaps settled.
- **3-Anchor Introduction Retrieval**: Retrieve the Introduction (Paras 3–11) and baseline table notes to verify:
  1. Exact setting, dataset, and specific exogenous shock / natural experiment.
  2. Quantitative findings, baseline coefficients, and economic magnitude.
  3. Self-stated contribution and incremental boundary relative to benchmark papers.
- **Intellectual Lineage & Ownership Precision**:
  - Distinguish Theoretical Originators from Empirical Landmarks, Causal ID Benchmarks, and Boundary Reassessments.
  - Record what each paper established and its boundary conditions (what it left open).
- Never fabricate citations, metadata, or journal quality signals.
- Default outputs should include:
  - scoped question and topic maturity assessment,
  - search strategy and grid,
  - prioritized reading list,
  - 16-column literature matrix,
  - synthesis by mechanism and intellectual lineage,
  - explicit research-gap statement grounded in boundary conditions.
