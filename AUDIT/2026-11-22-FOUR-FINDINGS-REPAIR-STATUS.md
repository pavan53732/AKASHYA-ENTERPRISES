# Four follow-up numerical QA findings after KC-01..KC-07
**Status: ALL 4 FINDINGS (FQ-01 TO FQ-04) FULLY RESOLVED, REGENERATED AND VERIFIED.** Executed via rollback-safe runner `python scripts/run_binary_repairs.py`. All integrity gates (`validate_dpr_consistency.py`, `audit_369_formulas.py`, `inspect_pdf_layout.py`) report `PASS` (exit code 0). Validated 23 November 2026.

| ID | Confirmed issue | Source fix in repository | Actual binary verification | Status |
|---|---|---|---|---|
| FQ-01 | PDF page 7 scale table still ₹9,000/MT despite ₹8,000 current scenario | `scripts/repair_page7_scale.py`, integrated into PDF builder | **RESOLVED / VERIFIED**. Page 7 regenerated cleanly: shows 600/750/850/1000 MT revenues ₹48.00/60.00/68.00/80.00L; EBITDA ₹0.23/4.46/7.27/11.50L; simple payback 4.49 years on ₹619.43L outlay / ₹137.98L annual EBITDA. Stale ₹9,000 values completely eliminated. | **FIXED** |
| FQ-02 | Excel 15-Year Cash Flow sheet includes A and B only; no stress C | `scripts/add_stress_scenario.py` adds 15-year rows 43–57 with sale 0%, wood +8%, other OPEX +7%, plus formula-based totals | **RESOLVED / VERIFIED**. Added Scenario C at rows 43–57; relocated owner key findings to rows 59–62. All 521 formulas across 8 sheets evaluated and cached in XML via `inject_formula_caches.py`. Scenario C matches markdown stress table exactly: Y1 ₹8.8L, Y5 -₹147.0L, Y10 -₹584.9L, Y15 -₹1,213.7L, cumulative -₹7,664.6L (-₹76.65 Cr). | **FIXED** |
| FQ-03 | JSON ensure_ascii=False may crash Windows cp1252 terminal | `scripts/validate_dpr_consistency.py`, `audit_369_formulas.py`, `inspect_pdf_layout.py` now ASCII/UTF-8 safe | **RESOLVED / VERIFIED**. Terminal encoding hardened with UTF-8 stdout reconfiguration and `run_binary_repairs.py` environment flags. Verified on Windows shell with 0 crashes. | **FIXED** |
| FQ-04 | Owner-cost doc carries old incomplete verification and 9-page claims | Updated `FINANCE/OWNER-COST-RECONCILIATION.md` | **RESOLVED / VERIFIED**. Reconciled with 10-page DPR, ₹8,000 baseline, ₹520L fixed + ₹99.43L WC = ₹619.43L outlay, and verified status. | **FIXED** |

## Binary Verification Hash Register
- `Anakapalli_1000MT_Briquette_Internal_Cost_Model.xlsx`: SHA256 `70B94733D32567FF8A264ADCB48031415F4BE683D58DAFAF106D8862EB8EE512`
- `Anakapalli_1000MT_Wood_Briquette_Internal_DPR.pdf`: SHA256 `0BF59C82986488F2D89CC54522E5603E62C4694741DF7A69B47F975BD40F7075`

## Audit Pipeline Results
- `validate_dpr_consistency.py`: **PASS** (8 sheets, 521/521 formula caches, Scenario C verified in rows 43–57, Page 7 verified, 0 unverified strokes, 0 unsafe buffers, 0 price floor claims).
- `audit_369_formulas.py`: **PASS** (521 formula cells, 0 calculation errors, 0 cache mismatches, all 3 fifteen-year scenarios verified).
- `inspect_pdf_layout.py`: **PASS** (10/10 pages pass layout check; 0 text block collisions/overlaps, 0 out-of-bounds text).
- CI workflow: Hardened with UTF-8 encoding and script fixes for reproducible builds.
