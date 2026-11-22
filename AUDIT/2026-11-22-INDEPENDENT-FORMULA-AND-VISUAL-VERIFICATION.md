# Independent Mathematical Formula & PDF Visual Layout Verification Report
**Date:** 22 November 2026  
**Subject:** Full Mathematical Verification of 369 Formula Cells and 10-Page Visual Layout Inspection for Akashya Enterprises  
**Status:** Historical PASS for its existing 369 formulas and document geometry, but **NOT full numerical/model completeness verification**; later audit uncovered incorrect PDF p7 sale-price table and missing workbook Scenario C. See [follow-up repair status](2026-11-22-FOUR-FINDINGS-REPAIR-STATUS.md).  
**Reference GitHub Commit:** Resolves and Closes Issue #1 (`Kilo Code binary consistency audit`)

---

## 1. Executive Summary

Following the remediation of the seven Kilo Code discrepancies (KC-01 to KC-07) and injection of XML `<v>` caches into the Excel workbook, an independent audit was conducted across two distinct quality dimensions:
1. **Mathematical Accuracy of All 369 Formula Cells:** Verified using Python's `formulas` and `openpyxl` engines to prove not only the presence of saved caches, but the exact arithmetic correctness, cross-sheet reference integrity, and physical mass/cash balance identities across all 8 sheets.
2. **Visual Layout & Typography Inspection Across All 10 Pages:** Audited using PyMuPDF (`fitz`) geometry inspection, verifying bounding boxes, margins, font hierarchies, line wrapping, and absence of text collisions or glyph corruptions.

---

## 2. 369-Formula Mathematical Verification Audit

### 2.1 Formula Distribution by Sheet
| Sheet Name | Formula Count | Status | Key Tested Formula Cells & Logic |
|:---|:---:|:---:|:---|
| **Summary** | 16 | PASS | `B9` (Rev: ₹80.00L), `B10` (Wood: ₹31.58L), `B11` (Power: ₹12.92L), `B14` (OPEX: ₹68.50L), `B15` (EBITDA: ₹11.50L), `B18` (Fixed: ₹520.0L), `B19` (WC: ₹99.43L), `B20` (Total Outlay: ₹619.43L) |
| **Assumptions** | 1 | PASS | `B21` (`=Manpower!D19/100000`): Dynamically links 31-staff roster payroll (₹850,000) to Assumptions (8.5 Lakh) |
| **Machinery & CAPEX** | 30 | PASS | `D5:D16` (`=B*C`), `D17` (`=SUM(D5:D16)` = ₹310.0L), `D20:D26` (`=B*C`), `D27` (`=SUM(D20:D26)` = ₹210.0L), `D29` (`=D17+D27` = ₹520.0L), `D33:D38` (Working capital items), `D40` (`=SUM(D33:D38)` = ₹99.43L), `D42` (`=D29+D40` = ₹619.43L) |
| **Manpower** | 15 | PASS | `D5:D18` (`=B*C` per roster position), `D19` (`=SUM(D5:D18)` = ₹850,000 / month across 31 staff) |
| **Operating Cost** | 38 | PASS | `B5` (Rev: ₹80.00L), `B7` (Wood Cost: ₹31.58L), `B19` (Total OPEX: ₹68.50L), `B20` (EBITDA: ₹11.50L), `B23` (Wet wood required: 1,578.95 MT based on dry matter conservation) |
| **Scenarios** | 59 | PASS | 3 Sensitivity Tables: Table 1 (Selling price ₹8k-₹10k vs Wood ₹1.5k-₹3k), Table 2 (Scale 60%-100%), Table 3 (Moisture 25%-55% vs Evaporation kg/h and EBITDA) |
| **Sources & Notes** | 0 | N/A | Register sheet containing textual metadata, verified citations, and audit disclaimers |
| **15-Year Cash Flow** | 210 | PASS | Compounded escalation across 15 operating years for Scenario A (+3% sale, +6% wood) and Scenario B (+5% sale, +6% wood), capital replacement reserves (Yr 6 ₹30L, Yr 10 ₹50L, Yr 13 ₹30L), cumulative net cash position |
| **Total** | **369** | **PASS** | **Zero errors (`#REF!`, `#DIV/0!`, `#VALUE!`, `#NAME?`, `NaN`, `Inf`), Zero cache mismatches** |

### 2.2 Core Financial Identities Confirmed
1. **Operating Surplus Identity:**
   $$\text{Revenue (₹80.00L)} - \text{OPEX (₹68.50L)} = \text{EBITDA (₹11.50L)}$$
   Exact calculated: $80.0000 - 68.5013 = 11.4987$ (Tolerance $< 10^{-4}$).
2. **Capital Outlay Identity:**
   $$\text{Fixed CAPEX (₹520.00L)} + \text{Opening Working Capital (₹99.43L)} = \text{Total Cash Outlay (₹619.43L)}$$
   Exact calculated: $520.0000 + 99.4329 = 619.4329$ (Tolerance $< 10^{-4}$).
3. **Dry-Solid Conservation & Moisture Bottleneck:**
   $$W_{\text{wet}} = \frac{1000 \times (1 - 0.10)}{(1 - 0.40) \times (1 - 0.05)} = 1,578.95 \text{ MT/month}$$
   At 40% moisture, required water evaporation is 532 MT/month = 1,563 kg/hour at 340 productive hours.
   At 50% moisture, incoming logs surge to 1,895 MT/month and evaporation jumps to 2,492 kg/hour, causing a plant bottleneck on standard 1,800–2,000 kg/h flash dryers.
4. **15-Year Long-Term Solvency Dynamics:**
   - **Scenario A (Base Case: Sale +3%/yr, Wood +6%/yr):** EBITDA turns negative in Year 7 (-₹19.52L) and cumulates to a deficit of -₹19.37 Crore by Year 15, proving that un-indexed long-term off-take contracts fail under commodity inflation.
   - **Scenario B (Indexed Offtake: Sale +5%/yr, Wood +6%/yr):** Recovers entire initial capital cash (₹619.43L) by Year 8 (+₹40.34L net surplus) and generates a cumulative net cash position of +₹6.34 Crore by Year 15 after absorbing ₹1.10 Crore in scheduled equipment replacement reserves.

---

## 3. 10-Page Visual Layout & Typography Inspection

Automated block geometry extraction via PyMuPDF ([`scripts/inspect_pdf_layout.py`](file:///c:/Users/pavan/PROJECTS/AKASHYA-ENTERPRISES/scripts/inspect_pdf_layout.py)) yielded the following certified results:

| Page # | Page Section & Core Topic | Text Blocks | Geometry & Margins | Layout & Typography Verdict |
|:---:|:---|:---:|:---:|:---:|
| **Page 1** | Executive Cover, Promoter Identity & Key Metrics | 28 | Margins: 48.2 -> 547.0 pt | **PASS:** 0 overlaps, 0 clipping, "promoter-observed scenario" clean |
| **Page 2** | Section 1: Output, Shifts & Process Design | 34 | Margins: 48.2 -> 547.0 pt | **PASS:** Clean process flow, 340h duty, uptime balance |
| **Page 3** | Section 2: Fixed Investment Budget (₹520L BOM) | 36 | Margins: 48.2 -> 547.0 pt | **PASS:** 12-item BOM table aligned, PEB shed & foundations |
| **Page 4** | Section 3: Monthly OPEX & Owner Margin | 36 | Margins: 48.2 -> 547.0 pt | **PASS:** APEPDCL HT III(A) power math, breakeven analysis |
| **Page 5** | Section 4 & 5: Manpower (31 Staff) & Statutory Permits | 36 | Margins: 48.2 -> 547.0 pt | **PASS:** 31-staff roster, shifts, Single Desk regulatory gates |
| **Page 6** | Section 6: Working Capital (₹99.43L) & Cash Outlay | 32 | Margins: 48.2 -> 547.0 pt | **PASS:** Inventory days, receivables, total ₹619.43L cash |
| **Page 7** | Section 7: Sensitivity Analysis & Payback Scenarios | 34 | Margins: 48.2 -> 547.0 pt | **PASS:** "Planning baseline" clean, 4.49-yr payback matrix |
| **Page 8** | Section 8: Approvals Checklist & Summary Judgment | 36 | Margins: 48.2 -> 547.0 pt | **PASS:** 0 overlaps, clean block 8.2, forward link to Page 9 |
| **Page 9** | Section 9: 15-Yr Model, BOM & March 15 Critical Path | 32 | Margins: 48.2 -> 547.0 pt | **PASS:** 0 out-of-bounds, 2-3 day safe buffer, candidate OEM |
| **Page 10** | Section 10: Research Critical Review & Boiler Trials | 31 | Margins: 48.2 -> 547.0 pt | **PASS:** 25-55% moisture table, 4-gate protocol, ATEX safety |

**Key Layout Improvements Achieved:**
1. **Page 8 Clean Redaction:** Replaced previous patchwork text overlays with a unified, professional `8.2 | Summary Judgment & Critical Investment Variables` block, eliminating all text collision artifacts.
2. **Page 9 Text Containment:** Reformatted 15-Year Scenario table and Financing Critical Path table so all text columns terminate inside $x = 544\text{ pt}$ (within printable boundary $x = 547\text{ pt}$), resolving all horizontal overflow.
3. **Page 10 Column Geometry:** Adjusted Table 1 column widths and engineering verdict strings, ensuring all rows are completely bounded inside the table borders.

---

## 4. GitHub Issue #1 Closure Statement

**Issue #1 Title:** Kilo Code binary consistency audit  
**Resolution Status:** **CLOSED / RESOLVED**  
**Resolution Summary:**
All seven binary defects (KC-01 to KC-07) identified in Issue #1 have been remediated, verified, and audited:
- Excel workbook formula caches saved across all 369 cells (exit code 0 on `validate_dpr_consistency.py`).
- Mathematical correctness of all 369 formula cells verified with zero errors or deviations (`audit_369_formulas.py`).
- 10-page master DPR visually inspected with zero text collisions and zero out-of-bounds clipping (`inspect_pdf_layout.py`).
- SHA256 hashes recorded:
  - Excel: `1DFE1F864D2A1D7A63C4B1C73468F4DCA8978FA5164E565ADA65EF07AA465F39`
  - PDF: `80DFE025FFB653E2B08E182ECC8959163FC2AE4513866FC904D6C0B025B883BB`

## Follow-up audit limitation — 22 Nov 2026
Even an exact formula-cache recomputation can pass when an entire documented Scenario C is absent from Excel. Text-block geometry can pass while a PDF table carries stale prices. The current report documents previous limited tests, not proof the follow-up PDF page7/Stress C checks have passed. Those need the latest binary artefacts to be actually regenerated and re-tested before bank delivery.
