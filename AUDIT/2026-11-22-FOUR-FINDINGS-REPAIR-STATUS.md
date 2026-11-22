# Four follow-up numerical QA findings after KC-01..KC-07
**Status: OPEN pending actual binary regeneration.** 22 November 2026. Previous seven Kilo Code repairs remain documented as fixed; these are additional findings beyond original checks.

| ID | Confirmed issue | Source fix in repository | Actual binary verification |
|---|---|---|---|
| FQ-01 | PDF page7 scale table still ₹9,000/MT despite ₹8,000 current scenario | `scripts/repair_page7_scale.py`, integrated into PDF builder | **PENDING**. Correct revenue ₹48/60/68/80L at 600/750/850/1000 MT; EBITDA ₹0.23/4.46/7.27/11.50L and ~4.49 years simple payback |
| FQ-02 | Excel 15-Year Cash Flow sheet includes A and B only; no stress C | `scripts/add_stress_scenario.py` adds 15-year rows 43–57 with sale 0%, wood +8%, other OPEX +7%, plus formula-based totals | **PENDING**. Must retain 8 tabs, recalc all caches and compare Scenario C to Markdown cashflows |
| FQ-03 | JSON ensure_ascii=False may crash Windows cp1252 terminal | `scripts/validate_dpr_consistency.py` now ASCII-safe and adds page7 + stress C gates | **SOURCE FIX COMMITTED**; run on default Windows console to confirm |
| FQ-04 | Owner-cost doc carries old incomplete verification and 9-page claims | Updated FINANCE/OWNER-COST-RECONCILIATION.md | **MARKDOWN FIX COMMITTED** |

Additional defect: `scripts/audit_369_formulas.py` previously printed PASS with mismatch/error arrays nonempty; updated to assert both lists empty, check Stress C rows, and allow greater than 369 formulas after Scenario C insertion.

**Runner:** `python -m pip install formulas pymupdf pypdf` then `python scripts/run_binary_repairs.py` on latest main. The script preserves original copies and rolls back both binaries if any validation fails. Re-run checks, inspect PDF p7 raster and record fresh hashes after changes.

**Automation status:** GitHub Actions run [45054319247](https://github.com/pavan53732/AKASHYA-ENTERPRISES/actions/runs/45054319247) failed twice, without recorded job steps or accessible logs. Neither XLSX nor PDF should be claimed corrected from that run.

**Do not close this new QA register or claim bank-ready status** until the binary commit exists and the expanded validator passes in its own environment. Equipment RFQs, buyers, site tenure and lender credit conditions remain outstanding.
