# Kilo Code binary inconsistency audit and corrective decisions
**Status:** Open binary-remediation findings; current source of truth is checked-in Markdown technical and commercial controls, pending inspection and regeneration of the latest root XLSX and PDF. Logged 22 November 2026. Kilo Code's audit described GitHub HEAD \`37e280b\`, while later procurement/research commits exist. This report distinguishes *reported XLSX/PDF observations* from *directly verified Markdown policies*. No claim is made here that the newest binary cells were independently inspected.

## Decision matrix: seven Kilo Code findings

| ID | Kilo Code binary observation to check in the most recent checkout | Independent established source and correction | Classification / signoff |
|---|---|---|---|
| KC-01 | Excel \`Machinery & CAPEX!A9\`, \`Sources & Notes!A35\`, PDF p9 claim **220–240 BPM as piston strokes/min** | \`MACHINERY/04\` and \`AGENTS.md\` say **BPM/BM refers to model designation**. Exact strokes/min **UNKNOWN pending OEM datasheet/trial**. Replace with "Unverified; OEM to confirm". | **High — engineering contradiction if present; must correct** |
| KC-02 | Excel \`Assumptions!D6\`, \`Sources & Notes!A5/C23\` label selling **₹8,000/MT as firm/confirmed floor** | \`README.md\` and \`FINANCE/OWNER-COST-RECONCILIATION.md\`: ₹8,000/MT **promoter-observed ex-GST scenario, no confirmed buyer contract**. Remove "confirmed", "firm", "floor"; retain numeric scenario. | **Critical — financial evidence misstatement if present** |
| KC-03 | PDF p9 recommends **10–14 days of wet chipped wood** | \`MACHINERY/03\`: **2–3 days provisional weather-protected inventory only subject to site fire/EHS engineering**. Replace 10–14 days wet chips recommendation with "raw-log inventory based on sourcing; wet-chip buffer to be approved after self-heating/fire assessment; provisional 2–3 days". Do NOT represent 2–3 days as universal legal max. | **High — process/storage risk** |
| KC-04 | PDF p9 and CAPEX workbook imply EcoStan ESM150/BPM90HD and Infinite dryers already *selected* | Machinery list is **candidate vendor references**, not an award, binding quote or installed configuration. Change headings/notes to "indicative model reference / budget only". Preserve model names as references where useful. | **High — procurement confidence misstatement** |
| KC-05 | PDF p10 states Gate 1 ash ≤3%, GCV ≥3,800 kcal/kg, density ≥1.15, shatter ≥95% as though approved product specifications | \`MARKET-RESEARCH/03\` and \`OPERATIONS/KPI\` require **buyer-specific, test-backed acceptance criteria**. Values may remain only as explicitly illustrative tender discussion thresholds, not contractual minimums, industry standards, or achieved results. No buyer-approved grade on file. | **High — commercial quality promise** |
| KC-06 | Excel \`Sources & Notes\` has Toyotsu/Cohance per-company tonnes that can look like confirmed 2026 procurement | \`MARKET-RESEARCH/02\` records **current tonne purchases UNKNOWN**. Keep hypothetical examples only with clear *historic/conditional scenario, zero verified purchase orders* note. Do not aggregate into contracted offtake. | **Critical — unsupported demand certainty** |
| KC-07 | Kilo Code says all formula cells read with \`data_only\` as \`None\` | If correct in latest workbook, formulas **exist** but saved formula-result caches are missing. Recalculate and save using an appropriate capable spreadsheet engine; verify Summary/Assumptions/CAPEX/Manpower/Operating Cost/Scenarios/15-Year values with *cached numeric outputs*. Do not claim recalculated until demonstrated. | **Critical — computational deliverable integrity** |

## Subtleties: what Kilo Code did not prove
1. **Outdated checkout:** Kilo reported 25 Markdown documents and HEAD \`37e280b\`; the project has newer commits containing priced supplier research. First \`git fetch && git pull --ff-only\`.
2. **Blank caches ≠ formula errors:** \`data_only=None\` may indicate *absence of saved cached results*, not wrong mathematical formulas. Perform an independent cell/formula check rather than declaring every formula wrong.
3. **"Firm floor" is not a contract:** selling assumptions must be on explicitly hypothetical basis, including the 15-year indexed scenario.
4. **No exact machine selection:** even a manufacturer model code on a rough engineering budget is not a supplier quote, nor does a photo prove capacity.
5. **Wet-chip storage:** the 2–3-day provisional guidance in the safety SOP is *not a fire engineer's signoff*; determine safe volume, turn-over, pile dimensions and monitoring for the actual site.
6. **Threshold provenance:** whether 3% ash etc. are sensible *indicative* targets is a buyer/OEM/independent lab question; mark source/grade rather than silently deleting technical placeholders.

## Acceptance criteria for repaired binary versions
- Open **current newest main** (not obsolete commit) and preserve **8 sheets and 10 pages**.
- Compare and correct exactly the cells/sections above *only after verifying they exist*; preserve formula references, layouts, model structure, 15-year scenario and 25–55% moisture sensitivity.
- Formula checks must test \`'Machinery & CAPEX'!D29/D40/D42\`, \`'Manpower'!D19\`, Summary linked totals, assumptions payroll, scenario 40% vs 50% wood and all 15-year cashflow arithmetic and cash signs; no \`#REF!\`, \`#VALUE!\`, \`#DIV/0!\`.
- Recompute and ensure Excel has **saved formula caches**. External viewers must be able to open formula values without their own recalculation. Any formula evaluator limitation must be documented; do **not** claim complete formula-cache validity if untested.
- PDF p9 and p10 corrected; verify PDF text extraction and visual page renders, 10-page count, font support for ₹, no spill/crop. Compare loan numbers and plant moisture entries against XLSX *after* recalculation.
- Store a new audit note documenting exact modified cell addresses, PDF pages, formula-cache inspection output, before/after hashes, commit SHA and reviewer. Only then mark \`KC-01..07 FIXED\`.
- **Do not overwrite root XLSX/PDF with older local mounted attachments.** They predate newer 8-sheet and 10-page GitHub binaries. Preserve latest binary version, byte-for-byte where not modified.

## Current implementation status
**Markdown claims corrected and validation gate prepared. Original binary issues require in-place regeneration of their latest version and remain OPEN until resulting GitHub file SHA changes and validations pass.** This document is a tracked repair spec and is not itself an edited XLSX/PDF.
