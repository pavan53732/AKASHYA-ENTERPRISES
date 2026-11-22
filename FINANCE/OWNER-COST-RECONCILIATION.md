# Current owner-cost baseline and reconciliation requirements
**22 Nov 2026.** Full production is 1,000 saleable MT/month. **₹8,000 sell price and ₹2,000/wet MT wood** are promoter-reported assumptions, **not audited contracts**.

## Monthly arithmetic — ₹ lakh
| Row | Full-output assumption | Cost ₹L/mo |
|---|---|---:|
| Revenue | 1,000 MT × ₹8,000 | **80.00** |
| Wood | 1,578.947 wet MT × ₹2,000 | 31.579 |
| Dryer thermal fuel | ₹600/saleable MT | 6.000 |
| Power energy | 150 kWh/MT ÷ 0.95 PF × ₹6.30/kVAh | 9.947 |
| Power contract demand | 500 kVA × ₹475/month | 2.375 |
| Power ToD/duty adjustment | Budget estimate only | 0.600 |
| Payroll | 31 staff two shifts | 8.500 |
| Repairs | Preliminary | 2.500 |
| Wear, knives, lubricants | Preliminary | 1.000 |
| Packaging/QC | Preliminary | 0.800 |
| Dispatch freight | Preliminary | 2.500 |
| Insurance/administration | Preliminary | 2.700 |
| **Total OPEX** | Round sum | **68.501** |
| **EBITDA** | 80−68.501 | **11.499** |

**Important:** this is an owner-side **cash-operating margin**, not PAT, distributable promoter profit, cash flow available for debt service or an equipment quote. No lease rent included even if project rents a property; add actual rent. Power ToD surcharge/discount should be recalculated on the selected 16/20/24 h operating schedule.

## Working capital starter — ₹ lakh
| Component | Basis | Amount |
|---|---|---:|
| Wood inventory | 14 operating days of ₹31.579L monthly wood | +17.684 |
| Finished inventory | 5 operating days of ₹68.501L OPEX/month | +13.700 |
| Buyer credit | 20 operating days of ₹80L sales/month | +64.000 |
| Dryer-fuel stock | 7 operating days of ₹6L fuel/month | +1.680 |
| Cash reserve | Fixed illustrative allowance | +15.000 |
| Wood-supplier credit | 10 operating days of ₹31.579L/month | −12.632 |
| **Opening estimated WC** | Rounded | **99.432** |

This WC formula is provisional: for true cash conversion include GST timing, raw and product inventory accounting cost, actual calendar/operating days, buyer retention/overdue charges, staff pay dates, supplier credit terms, and year-by-year inflation-driven WC increases. Do **not** equate this with minimum bank cash credit sanction.

## Capital baseline — ₹ lakh, owner estimate
Machinery & handling **310** + civil/electrical/site infrastructure **210** = **520**. Include shed/floor and electrical infrastructure, exclude land acquisition; any **land lease deposit and rent are also excluded** at present. Machinery detailed estimate remains in [procurement register](../PROCUREMENT/2026-11-22-MACHINERY-PRICE-AND-RFQ-REGISTER.md); get three written binding supplier offers.

## Workbook/PDF audit status after new Kilo Code follow-up — 22 Nov 2026
The Excel workbook contains 8 sheets, and the master PDF contains 10 pages. The previous KC-01 through KC-07 wording, formula-cache and visual-layout fixes are documented. However a subsequent **numerical completeness audit has identified new defects not covered by those checks**:

- The PDF page-7 production scale table and simple payback still reflect old ₹9,000/MT economics. At the owner-observed, uncontracted **₹8,000/MT**, the 600/750/850/1000 MT monthly revenues must be ₹48/60/68/80 lakh and the original OPEX-controlled EBITDA sensitivity ₹0.23/4.46/7.27/11.50 lakh; full-run simple payback is approximately ₹619.43L ÷ (₹11.499L × 12) = **4.49 years**, not 2.43 years.
- The 15-Year Cash Flow sheet contains **Scenario A (+3% sale/+6% wood) and Scenario B (+5% sale/+6% wood)**. The stressed Scenario C (flat sale, +8% wetwood, +7% other OPEX) is published in Markdown/PDF but is **not yet in the committed Excel binary**.
- The original mathematical audit checked its existing 369 formulas, not whether all three documented scenarios were represented. A separate, strengthened audit now must fail on any formula error/cache mismatch or missing Scenario C.

Repair scripts and a rollback-safe one-command runner have been committed. **Do not represent the binaries as fully synchronized or lender-ready until the actual current files are regenerated and validated, and their new SHA256 hashes recorded.** See [four-follow-up-issue audit](../AUDIT/2026-11-22-FOUR-FINDINGS-REPAIR-STATUS.md).
## Critical 25–55% wood moisture case (new — 22 Nov 2026)
The original **₹68.50 lakh OPEX/₹11.50 lakh EBITDA** is a **40%-incoming-moisture only** assumption at 1,000 MT/month, not a moisture-independent price. At 50% moisture **purchased wood rises to 1,895 MT/month** and raw-wood expense to **₹37.89 lakh**, cutting EBITDA to ~**₹5.18 lakh/month before increased dryer fuel/power, lower throughput or larger dryer costs**. See [full moisture sensitivity](../MACHINERY/05-WOOD-MOISTURE-AND-DRYER-SIZING.md). A 1,800–2,000 kg/hr evaporative dryer cannot assure 1,000 MT/month at 50% moisture on the 340 productive-hour base schedule. Do not convert the ₹5.18L sensitivity into net profit or lender DSCR.

**Moisture-cost caution:** 25–55% moisture mass-balance sensitivity is not a full high-moisture fuel/power/capex forecast; obtain OEM duty and fuel guarantees before bank extrapolation.

**Override as of 22 Nov 2026:** KC-01 through KC-07 are closed; separate new follow-up numerical defects remain **OPEN**, documented in [follow-up audit](../AUDIT/2026-11-22-FOUR-FINDINGS-REPAIR-STATUS.md). Reference revenue ₹8,000/MT remains an assumption, not a confirmed floor. The 40–50% dryer scenario must also include any extra fuel/power and actual capacity shortfall.
