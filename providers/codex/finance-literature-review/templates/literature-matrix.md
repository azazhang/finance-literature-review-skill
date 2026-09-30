# Finance Literature Matrix Template

Use this template to capture empirical and theoretical attributes required for rigorous PhD-level literature reviews, related-literature sections, and dissertation proposals.

---

## Column Definitions

1. **Theme / Subtopic**: The substantive mechanism or theoretical channel (e.g., *Credit Supply vs. Demand*, *Tax Incentives for Payout*, *Disclosure & Cost of Capital*).
2. **Citation & Year**: Author(s) (Year).
3. **Venue & Status**: 
   * Published: *Journal Name* (e.g., *Journal of Finance*, *AER*).
   * Working Paper: Series and vetting level (e.g., `NBER WP #31892 / R&R JF`, `CEPR DP #17890 / AFA 2025`, `Fed Board FEDS 2024-012`, `SSRN FEN`).
4. **Venue Tier**:
   * `F1 Core` (JF, JFE, RFS)
   * `F1 Field` (JFQA, RF, MS, RCFS, RAPS, JMCB, JCF)
   * `Econ Top 5` (AER, QJE, JPE, Econometrica, ReStud)
   * `Acct Top 5` (TAR, JAR, JAE, RAST, CAR)
   * `Tier 1 WP` (NBER, CEPR, Central Bank, R&R at Top 3/5, AFA/WFA/NBER SI)
   * `Tier 2 WP` (Top department series, regional workshops, high-download SSRN)
   * `Tier 3 WP` (Early unvetted preprint)
5. **Verification Level**:
   * `[Full-Text Verified]`: Inspected full manuscript/PDF text and tables.
   * `[Intro / Table Verified]`: Inspected Introduction (pages 1–6) and baseline regression tables.
   * `[Abstract-Only Provisional]`: **Quarantined**. Columns 11–15 must be marked `[Unverified from abstract]`.
6. **Lineage & Intellectual Role**:
   * `Theoretical Originator`: Derived the benchmark mathematical/economic model.
   * `First Empirical Landmark`: First documented empirical correlation/stylized fact.
   * `Causal ID Benchmark`: First established causal link via credible natural experiment / shock.
   * `Boundary / Reassessment`: Tested external validity, subsample boundary, or staggered DiD re-evaluation.
7. **Research Question**: The precise economic question investigated.
8. **Setting & Primary Data**: Databases and institutional universe (e.g., *US Compustat/CRSP*, *Dealscan syndicated loans*, *TRACE corporate bonds*, *FFIEC Call Reports*, *HMDA mortgages*, *TAQ intraday*, *SEC EDGAR 10-K text*).
9. **Sample Period & Filters**: Time window and standard screens (e.g., *1995–2022; excludes financial (SIC 6000–6999) and utilities (SIC 4900–4949); share price > $5*).
10. **Unit of Observation**: Level of analysis (e.g., *firm-year*, *loan-quarter*, *bank-firm-year*, *stock-day*).
11. **Identification Strategy & Source of Exogenous Variation**: 
    * The causal design (e.g., *Staggered DiD*, *Fuzzy RDD*, *2SLS / Instrumental Variables*, *Event Study*, *Khwaja-Mian credit supply decomposition*, *Structural estimation*).
    * The specific shock / policy / instrument (e.g., *state corporate income tax changes*, *Russell 1000/2000 reconstitution*, *Dodd-Frank asset threshold ($50B)*, *county-level weather shocks*).
12. **Econometric Nuance & Fixed Effects**: Fixed effects structure (e.g., *firm and industry $\times$ year FE*), standard error clustering (e.g., *Petersen two-way clustering by firm and year*), and modern DiD estimator if staggered (e.g., *Callaway-Sant'Anna, Sun-Abraham*).
13. **Verified Empirical Finding & Magnitude**: Quantitative primary estimate and economic significance (e.g., *34 bps spread reduction, \$12M for median borrower*).
14. **Mechanism / Channel**: The economic transmission channel verified or tested (e.g., *collateral channel*, *managerial entrenchment*, *information acquisition cost*, *regulatory capital arbitrage*).
15. **Boundary Condition & What It Leaves Open**: What the paper cannot observe, unstudied samples, or remaining identification threats.
16. **Positioning Value & Open Gap**: How this paper anchors the literature and the exact gap it leaves for new work.

---

## Markdown Matrix Table

| Theme | Citation & Year | Venue & Status | Venue Tier | Verification Level | Lineage Role | Research Question | Setting & Primary Data | Sample Period & Filters | Unit | Identification Strategy & Shock | Econometric Nuance & FE | Finding & Magnitude | Mechanism / Channel | Boundary Condition / Leaves Open | Positioning / Gap |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Credit Supply Shocks | Khwaja and Mian (2008) | AER (Published) | Econ Top 5 | [Full-Text Verified] | Causal ID Benchmark | Do liquidity shocks to banks affect credit supply to firms? | Pakistan Credit Registry (all business loans) | 1996–2000 | Bank-firm-quarter | Exogenous nuclear test liquidity shock; within-borrower multi-bank estimator | Firm FE absorbs firm borrowing demand; clusters at bank level | Affected banks reduce lending by 12%; 1-SD liquidity drop cuts borrowing by \$2.4M | Bank liquidity channel; asymmetric information prevents substitution | Examines bank loans only; cannot observe whether firms substitute into bond markets or trade credit | Established landmark within-borrower estimator for credit supply vs. demand |
| Bank Capital & Stability | Author (2024) | NBER WP #32100 / R&R JF | Tier 1 WP | [Intro / Table Verified] | Boundary / Reassessment | Does unrealized hold-to-maturity loss increase uninsured deposit run risk? | US Commercial Banks (Call Reports, Y-9C) | 2019–2023 | Bank-quarter | Post-2022 rate hike cycle $\times$ pre-existing HTM securities share | Bank & Quarter FE; clustered by bank | 10% HTM loss predicts 8.4% uninsured deposit outflow in Q1 2023 | Mark-to-market insolvency perception triggers uninsured run | Sample restricted to commercial banks; does not test shadow banks or repo runs | Extends Diamond-Dybvig to duration risk in modern uninsured deposit markets |
| AI in Credit Underwriting | Preprint Author (2025) | SSRN FEN (Working Paper) | Tier 3 WP | [Abstract-Only Provisional] | Boundary / Reassessment | Does LLM-assisted scoring reduce mortgage default rates? | US FinTech mortgage originator (Confidential) | 2021–2024 | Loan-level | [Unverified from abstract] | [Unverified from abstract] | Author claims 14% default reduction in abstract (unverified) | Algorithmic screening efficiency (unverified) | Proprietary data; external validity and demographic bias unverified | Illustrates frontier industry claim; requires full-text validation before citation |
