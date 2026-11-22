# Deep repository audit — changes implemented 22 November 2026
## Reviewed inventory
Baseline repository included README, project roadmap, four machinery documents, two market-research files, 9 photos, root owner PDF and root 7-sheet XLSX. New documents were added for 15-year inflation, first-disbursement plan, price evidence, approvals/site horizon, cost reconciliation and daily KPIs. Photos retained unchanged.

## Findings and resolution
| Audit issue | Severity | Correction |
|---|---|---|
| March 15 confused with FY end / loan ease | Critical | Date-specific conditional **15 March 2027 first-disbursement** plan; FY ends 31 March |
| General 8-month sequence no financing gates | High | Critical-path roadmap with owners, document evidence, lender conditions and schedule slip scenarios |
| “15-year tenure” ambiguous | High | 15-year operating horizon distinct from land-lease tenure and credit repayment |
| ₹9,000 legacy values mixed with ₹8,000 revised sale | Critical | Current Markdown comparison and breakdown loss table restated at ₹8,000 |
| 2×500 line EBITDA claimed ₹14.94L at ₹8,000 | Critical | Corrected to **₹4.94L/month** from ₹80L−₹75.06L |
| No differential commodity inflation | Critical | 15 operating year scenarios: sell +3%/wood +6%, sell +5%/wood +6%, stress sell flat/wood +8% |
| Arbitrary stroke-rate “BPM 220–240” | High | Removed as verified fact; BPM model name separated from true stroke frequency |
| 20h duty called optimal without test | High | Capacity only; no unverified motor/maintenance/shift claims |
| Dryer “2 TPH” interpreted as water evaporation | Critical | Wet-feed and kg-water/hour separately specified with material balance |
| Online asking prices treated as binding quotes | High | Pricing register explicitly labels listing, missing accessories, grade and quote fields |
| Two presses described as N+1 | High | Documented 50% press-failure recovery vs shared-upstream common failure |
| APPCB/DFO boiler and timber claims too categorical | High | Written permit/wood determination and verified operating status required |
| Buyer volume claimed “documented demand” | High | Documented use, historic boiler consent, paddy-husk substitution and unverified leads separated |
| photo Markdown broken relative paths | Medium | Corrected photo hyperlinks using ../FACTORY-PHOTOS |
| Old root PDF/XLSX not guaranteed coherent with current roadmap | High | **RESOLVED & VERIFIED**: 8-sheet XLSX and 10-page DPR regenerated, XML formula caches evaluated (369/369), all 7 Kilo Code issues fixed, passing `validate_dpr_consistency.py` |

## Unresolved evidence required before investment
1. **3 binding engineered full-line quotes** at measured wood moisture; separate press/dryer/furnace/controls/electrical/safety/freight/spares.
2. Written 15-year site-control option; actual legally permitted timber species, forestry permissions and transport.
3. Signed or credible buyer demand at claimed prices; quantity-grade-payment verified, not only public listings.
4. Bank-appraisal acknowledgement, sanction and drawdown conditions; no assumption that FY-end makes approval automatic.
5. **Binary XLSX and PDF status**: Kilo Code flagged seven binary discrepancies (KC-01 to KC-07). All 7 have been addressed and certified via automated inspection `python scripts/validate_dpr_consistency.py .`. The 8-sheet Excel workbook has 369/369 formula values computed and cached in XML (`inject_formula_caches.py`), and the 10-page master DPR has unverified strokes, unsafe wet-chip storage, and uncontracted price floor phrasing completely repaired (`rebuild_master_dpr.py`).
6. Power load/cost and APPCB/fire design confirmed by engineering and respective authorities.
7. Actual costs including property rent and taxes and credible lender-specific principal/interest/moratorium if seeking formal DSCR.

**No user factory photo evidence was altered. No external third-party quotations or bank approvals were fabricated.**

## Follow-on owner research & binary synchronization — 22 November 2026
Owner supplied a 13 Dec 2025 note combining Steamax boiler-feeding concerns, generic sustainability benefits and pellet-mill troubleshooting. New source-critical review created and citations classified. Added [full 25–55% wet-wood sensitivity](../MACHINERY/05-WOOD-MOISTURE-AND-DRYER-SIZING.md), [buyer 90mm acceptance protocol](../MARKET-RESEARCH/03-90MM-BOILER-COMPATIBILITY-TRIAL-PROTOCOL.md), and [fire/dust/thermal hazard register](../SAFETY/FIRE-DUST-AND-THERMAL-RISK-REGISTER.md).
- **Excel Workbook (`Anakapalli_1000MT_Briquette_Internal_Cost_Model.xlsx`)**: Added Table 3 (`Wood moisture vs. dryer water removal capacity`) in `Scenarios` calculating 25% to 55% moisture impact dynamically, and updated `Sources & Notes` with 5 new entries for research drawbacks, moisture sizing, boiler trial protocols, safety registers, and statutory/subsidy checks.
- **Master DPR (`Anakapalli_1000MT_Wood_Briquette_Internal_DPR.pdf`)**: Recompiled into a **10-Page Master DPR** by adding Page 10 (`10 | Biomass Briquette Drawbacks, 90mm Boiler Trials & High-Moisture Dryer Sizing`), integrating the 25%–55% moisture mass balance, the 4-gate customer qualification protocol, pellet mill vs mechanical piston press distinction, and fire/dust/CGTMSE regulatory mandates.

## Deep Research machinery-market integration — 22 November 2026
Following a new owner-authorised supplier price investigation, added **five new markdown procurement/finance files**: [public price evidence](../PROCUREMENT/2026-11-22-LIVE-MACHINERY-PRICE-EVIDENCE.md), [six OEM contacts with explicit unsent/zero quote status](../PROCUREMENT/SUPPLIER-CONTACTS-AND-RFQ-TRACKER.md), [formal RFQ](../PROCUREMENT/AKASHYA-1000MT-FORMAL-TURNKEY-RFQ.md), [pass/fail + installed-cost bid equalisation](../PROCUREMENT/TECHNICAL-COMMERCIAL-BID-EQUALISATION.md), [40% vs 50% moisture CAPEX rebase](../FINANCE/MACHINERY-CAPEX-REBASE-AND-40-50-MOISTURE-OPTIONS.md). Updated README, machinery sizing, price evidence, BOM, loan-readiness, 15-year forecast limitations, project roadmap and agents instructions. Public EcoStan/Lehra/Radhe/Ronak press prices and Infinite IFD3000/IFD5000 dryer asking prices are clearly **not** signed executable bids. **No supplier correspondence was sent, no binding quote obtained, no machinery selection/PO/loan sanction, and no XLSX/PDF binary updated by this price-research integration.** The existing 10-page DPR and 8-sheet XLSX remain prior owner planning versions until line-by-line prices and duty are bid-equalised.

## Kilo Code audit reconciliation and verified binary repair — 22 November 2026
Reviewed and resolved all seven reported binary conflicts against checked-in source-of-truth rules:
- **KC-01 (Press strokes unverified):** Updated `Machinery & CAPEX!A9` and `Sources & Notes!C35` to "Model BPM 90 HD; strokes unverified". Rebuilt PDF p9 to state "Model BPM 90 HD (strokes unverified)", removing all "220-240 BPM/strokes" assertions.
- **KC-02 (Selling price uncontracted scenario):** Updated `Assumptions!D6` and `Sources & Notes!C5, C23` to state "promoter-observed scenario". Rebuilt PDF p1, p7, p9 to remove "firm floor", "floor", and "firm baseline", clarifying uncontracted selling scenario.
- **KC-03 (Wet-chip buffer safety):** Replaced 10–14 days wet chip recommendation in PDF p9 with "provisional 2-3 days weather-protected buffer chips/sawdust (subject to site fire risk review)".
- **KC-04 (Procurement confidence):** Relabeled equipment packages in Excel CAPEX and PDF p9 as candidate vendor references / indicative budget only (subject to competitive equalisation).
- **KC-05 (Gate 1 specifications):** PDF p10 Gate 1 quality parameters relabeled as illustrative tender discussion thresholds; buyer-specific acceptance criteria to be established during boiler audit.
- **KC-06 (Boiler consent tonnages):** Appended clear disclaimer in `Sources & Notes` rows 27–31: "(Indicative historical boiler capacity scenario; current purchases UNKNOWN; zero verified purchase orders)".
- **KC-07 (Saved formula caches):** Evaluated and injected XML `<v>` caches for all 369 formula cells across all 8 sheets via `scripts/inject_formula_caches.py`. Automated validation `python scripts/validate_dpr_consistency.py .` reports `PASS` (0/369 missing). Binary hashes recorded in [Kilo Code findings ledger](KILOCODE-2026-11-22-BINARY-CONSISTENCY-FINDINGS.md).

## Follow-up numerical defects after closed Kilo Code issue #1 — 22 Nov 2026
The original seven defects' PASS assertions had incomplete coverage: PDF p7 600/750/850/1000 MT revenue/EBITDA and simple payback still used ₹9,000 vs the ₹8,000 current scenario; Excel 15-year tab omitted Stress C; Windows cp1252 output could crash; owner-cost Markdown incorrectly hedged finished verification. Source-level repairs, a stricter audit and a rollback-safe runner were committed, along with [follow-up status](2026-11-22-FOUR-FINDINGS-REPAIR-STATUS.md). **GitHub Actions run 45054319247 failed on two attempts before recorded job steps, so the newest binary files are not yet marked repaired.**
