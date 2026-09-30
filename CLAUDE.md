# Finance Literature Review Context

Use the finance literature review workflow when the user asks for:

- a literature review,
- related literature section,
- annotated bibliography,
- gap map,
- journal-targeted reading list,
- working-paper scan,
- finance / economics / accounting research synthesis.

## Dynamic Priorities & Venue Hierarchy

- **Core Finance**: `Journal of Finance`, `Journal of Financial Economics`, `Review of Financial Studies`.
- **Subfield Leading Finance**: `JFQA`, `Review of Finance`, `Management Science` (finance), `RCFS`, `RAPS`, `JMCB`, `JCF`, `JBF`.
- **Adjacent Top Economics**: `AER`, `QJE`, `JPE`, `Econometrica`, `ReStud` when mechanisms, macro transmission, or identification strategies overlap.
- **Top Accounting**: `TAR`, `JAR`, `JAE`, `RAST`, `CAR` when overlapping disclosure, earnings, auditing, or information environment.
- **Dynamic Working Paper Integration**: Never automatically rank working papers at the bottom. Tier them into Tier 1 (NBER, CEPR, Central Banks, Top 3/5 R&Rs, AFA/WFA/NBER SI), Tier 2, and Tier 3. For frontier/emergent topics, Tier 1 working papers sit co-equal with Top 3 publications.
- **Systematic Discovery**: Search SSRN FEN eJournals, NBER programs (`CF`, `AP`, `ME`), CEPR, Central Banks (FEDS, NY Fed, BIS, ECB), conference programs (AFA, WFA, EFA, NBER SI), RePEc/IDEAS NEP reports, and finance JEL codes (`G1`, `G2`, `G3`, `M4`, `E4/E5`).

## Hard Rules & Abstract Quarantine

- Never hallucinate citations or metadata.
- **Abstract Quarantine**: Never infer identification strategies, fixed effects, clustering, or economic magnitudes from an abstract alone. If only the abstract is accessible, tag `[Abstract-Only Provisional]`, preface statements with *"Author claims in abstract (unverified): ..."*, and mark design fields unverified. Abstract-only papers **cannot** establish definitive intellectual ownership or settle research gaps.
- **3-Anchor Introduction Protocol**: Retrieve the Introduction (Paras 3–11) and baseline table notes to verify: (1) Setting & specific exogenous shock, (2) Quantitative magnitude, (3) Self-stated contribution relative to benchmark papers.
- **Intellectual Lineage**: Distinguish Theoretical Originator $\rightarrow$ Empirical Landmark $\rightarrow$ Causal ID Benchmark $\rightarrow$ Boundary Reassessment.
- Record both what a paper established and its boundary conditions (what it left open).
- Prefer synthesis by mechanism, intellectual lineage, and identification strategy, not paper-by-paper summaries.
- Capture granular empirical attributes: research question, primary dataset/infrastructure, sample period & filters, unit of observation, specific exogenous shock, fixed effects, clustering, main finding, mechanism, and limitations.
- If only titles or abstracts are available, say so explicitly.

## Preferred Outputs

- Scoped question, topic maturity assessment, and search grid.
- Venue-prioritized reading list.
- 16-column literature matrix with verification levels and lineage roles.
- Thematic mechanism synthesis.
- Explicit research gaps and dissertation/positioning proposals grounded in boundary conditions.

Use `/finance-lit-review` for the explicit guided workflow.
