# BPM 90 mm machinery, 16/20/24-hour duty and quote status
**Re-audit:** 22 Nov 2026. Reference pages: https://www.ecostan.com/products/briquetting-machine ; https://www.ecostan.com/products/sawdust-machine ; https://www.infinitedryer.com/ifd.html ; https://www.infinitedryer.com/rfd.html .

## Terminology
**BPM** here is part of some maker's *briquette press machine* model family; it does **not** establish the ram's blows-per-minute (stroke count). Previous documentation's **220–240 strokes/min, 180–220°C, pressure 1,200–1,500 kg/cm², longer die life on 20-hour shifts** were not supported by a verified nameplate/test and **must not be represented as factory facts**. Request stroke rate, ram travel, die temperatures and guaranteed output by exact model number.

## Nameplate / public catalogue reference, NOT guaranteed continuous output
| Reference | Publicly claimed output | Motor | Applicability |
|---|---|---|---|
| EcoStan BPM/BM 90 HD class | 1.3–2.0 TPH | approx 89.5 HP | Two suitable candidates; exact offered model/specification must be confirmed |
| EcoStan ESM 150 log sawdust | up to 5 TPH | 159 HP | Can be a bottleneck against ≥4.64 wet TPH need |
| Infinite IFD3000 dryer reference | ~1,800 kg/h evaporation | vendor technical table | Plausible duty candidate for two shifts, not a price quote |
| Infinite RFD series | model-dependent, including 2,000 kg/h water evaporation | vendor technical table | Alternative to compare using same wet-wood feed |

## Schedule mathematics
| Schedule | Operating days/month | Scheduled hours | Availability assumption | Productive hours | Total TPH needed | Each of two presses TPH |
|---|---:|---:|---:|---:|---:|---:|
| 16 hours/day | 25 | 400 | 85% | 340 | 2.941 | 1.471 |
| 20 hours/day | 25 | 500 | 85% | 425 | 2.353 | 1.176 |
| 24 hours/day | 26 | 624 | 80% | 499.2 | 2.003 | 1.002 |

**20-hour/day duty is not automatically cheaper:** labour cover, legal shifts and rest, night power/time-of-day tariffs, heat loads, preventive maintenance windows and actual loss factor change. Never label 20 h as “2.5 shifts” without compliant roster. **Press redundancy:** with two presses each producing roughly 500 MT/month, one press stopping cuts capacity ≈50%. Shared chipping/drying/power remain common single-point failures; two presses are **N parallel**, not N+1 to deliver the full 1,000 MT target during one press failure.

## Evaporation and wood
Wet mass = 1,000×(1−0.10)/[(1−0.05)×(1−0.40)] = **1,578.95 MT/mo**. Moisture removed = 1,578.95×0.40 −100 = **531.58 MT/month**. Divide by 340 h → **1.563 MT water evaporated/hour**. Request **1.8–2.0 MT/h verified evaporation guarantee** plus test at 50% incoming wet-basis moisture. A “2 TPH feed dryer” can be insufficient.

## Prices: separate source from budget
A public EcoStan BM-90/100-family press asking price of **₹25.95 lakh** appears at https://www.indiamart.com/proddetail/white-coal-biomass-briquette-machine-21168491112.html ; another 90-mm biocoal listing asks **₹27.15 lakh** at https://www.indiamart.com/proddetail/biocoal-briquette-machine-21168481191.html . These **are not firm exact-model quotations**. The two-press owner **₹52 lakh** capex remains a preliminary allowance; its coverage of auxiliary gear is unverified. Whole plant ₹3.10 crore machinery and ₹5.20 crore fixed excluding land are **unquoted** estimates. Exact quote comparisons and RFQ mandatory conditions are in [procurement register](../PROCUREMENT/2026-11-22-MACHINERY-PRICE-AND-RFQ-REGISTER.md).

## 15-year operating support
Obtain wear part lifetime **at guaranteed feedstock and 90-mm diameter**, annual service/spares indexation, guaranteed useful machine life vs overhaul cycles, critical component lead times, and a legal warranty. Ten years of annual inflation cannot be solved by a fixed 2026 machinery asking price. Model year 6/10/13 replacement reserves as placeholders only, not proven manufacturer overhaul timings.

**Action:** do not sign full-line orders until all bidders pass same wet-wood material balance, electrical single line, 16/20/24 h productivity schedule, vendor acceptance test and quote scope.
