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

## Formula and binary-file verification completed
The root Excel model and Master PDF DPR were **fully regenerated, formula-verified, and reconciled** on 22 Nov 2026:
1. **Dynamic Formula Links Verified**: Summary fixed cost (`=Machinery & CAPEX!D29`), Working capital (`=Machinery & CAPEX!D40`), Total project cash (`=Machinery & CAPEX!D42`), Assumptions payroll (`=Manpower!D19/100000`), and all 15-year cashflow escalation formulas were verified with 0 formula errors.
2. **8th Sheet Added**: The Excel model now contains a dedicated `15-Year Cash Flow` sheet modeling Base, Indexed, and Stress scenarios with replacement CAPEX and cumulative cash indicators.
3. **9-Page Master DPR PDF**: Page 9 was added integrating the 15-year inflation matrix, the turnkey BOM capital schedule (₹520L fixed + ₹99.43L WC = ₹619.43L), and the critical path to the **15 March 2027 first eligible loan disbursement**. Broken character glyphs were eliminated.
