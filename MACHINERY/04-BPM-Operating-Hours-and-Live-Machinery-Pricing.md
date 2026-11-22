# BPM 90 mm machinery, 16/20/24-hour duty and quote status
**Re-audit:** 22 Nov 2026. Reference pages: https://www.ecostan.com/products/briquetting-machine ; https://www.ecostan.com/products/sawdust-machine ; https://www.infinitedryer.com/ifd.html ; https://www.infinitedryer.com/rfd.html .

## Terminology
**BPM** here is part of some maker's *briquette press machine* model family; it does **not** establish the ram's blows-per-minute (stroke count). Previous documentation's **220–240 strokes/min, 180–220°C, pressure 1,200–1,500 kg/cm², longer die life on 20-hour shifts** were not supported by a verified nameplate/test and **must not be represented as factory facts**. Request stroke rate, ram travel, die temperatures and guaranteed output by exact model number.

## Nameplate / public catalogue reference, NOT guaranteed continuous output
| Exact model | OEM nameplate finished output (90mm where applicable) | Connected / published motor | Model inputs | Stroke/RPM evidence and qualification |
|---|---|---|---|---|
| **EcoStan 90 HD** | 1.3–2.0 TPH briquettes | **89.5 HP** | **8–12% moisture, ≤15×8mm particles** | **True strokes/min unknown**. Older EcoStan 90-sheet **216 machine RPM** applies only after exact machine identity is reconciled |
| **Lehra LBP90 / Fuel Tech 90mm** | Up to **2.0 TPH** | **87.5 HP** general 90mm, variant **69/86 HP** | Dried graded biomass; specific feed size and wood guarantee unknown | Actual strokes/min unknown |
| **Ronak Jumbo90** | **1.0–1.5 TPH**, official | **91 HP** | ≤20–25mm biomass, species and feed moisture to verify | Maker states **230 RPM, stock/stroke length 200mm**; 230 RPM is **not certified 230 punches/min** |
| **Radhe Jumbo90** | **~1.5 TPH** marketplace | Specific listing exact motor list not verified | Dried biomass; hardwood sample needed | Unknown |
| **Jay Khodiyar JK90** | **1.0–2.0 TPH** official broad range | **91 HP** | **8–12%**, 1×5×12mm reference | Unknown |
| **EcoStan ESM150 log sawdust** | **3–5 wet TPH** (not saleable briquettes) | **159 HP** | Logs ≤12-inch; output ~2–10mm | Chipper rotor RPM not press BPM, cannot infer press strokes |
| **Infinite IFD3000 / IFD5000 dryer** | **1,800 / 3,000 kg WATER/h** (not finished briquettes) | **67 / 136 HP** | **<8mm**, inlet moisture best <45% / table <50% | Dryer airflow/fan RPM not press BPM |

**Published model links:** [EcoStan press](https://www.ecostan.com/products/briquetting-machine), [older EcoStan 90 RPM brochure](https://5.imimg.com/data5/JG/VV/KA/SELLER-49897310/biomass-briquetting-plant.pdf), [Lehra official](https://lehrafuel.com/biomass-briquetting-machine.php), [Ronak 230 RPM](https://ronakeng.com/manual-briquetting-machine/), [JK90](https://jaykhodiyar.com/briquetting-machine/), [EcoStan ESM150](https://www.ecostan.com/products/sawdust-machine), [Infinite dryer size/water/fuel table](https://www.infinitedryer.com/ifd.html).

### What “BPM/hourly strokes” can and cannot tell us
- **Physical ram rate unknown:** a catalogue crank/shaft **216 RPM** (older EcoStan 90 reference) or **230 RPM** (Ronak Jumbo90) is NOT an OEM-certified **strokes/minute** for the current quote. Require ram-crank ratio, stroke length, sensor-recorded actual strokes during a load trial and exact serial/model.
- **Production from mass flow, not guessed RPM:** whole factory **2,941 kg finished/h**, each of 2 equal presses **1,471 kg/h**. At an *assumed, not measured* 216 strokes/min each, that is **~114g/stroke**; at 230 strokes/min **~107g/stroke**. Those are only demonstration ratios and cannot certify one briquette per stroke or solid density.
- **Press input:** dry graded material typically **8–12% wet-basis** per EcoStan/JK90. 1,000 MT/month finished includes **900 dry MT**. Upstream post-dryer material approximates **3.08 MT/h** at the assumed mass/loss model; verify where rejected dry matter leaves the line and don't equate 4.64 wet TPH logs with 2.94 finished TPH.
- **Real capacity at 340 productive h:** a model delivering 1.0/1.3/1.5/1.6/1.8/2.0 TPH on *each* of two presses would make **680/884/1,020/1,088/1,224/1,360 MT/month** *if all upstream equipment also performs* (no further downtime deduction; 340h already allows 15%). Need **≥1.60 TPH per press sustained, ≥3.20 combined**, not just transient surge above 2.941 combined.
- **Cooling gaps:** No published universal hourly stop or mandatory rest period for modern 90mm crank presses. They are intended as industrial continuous machines within approved bearing/die temperature/vibration and lubricant limits. A planned inspection stop is not a claimed obligatory 1-hour pause after each 8-hour shift. Negotiate an OEM written 16/20/24h duty cycle, maximum permissible continuous run, temperature alarms, lockout procedures and actual service windows.

See [line-by-line maintenance windows](03-Breakdown-Risk-Mitigation-and-Maintenance-SOP.md) and [expanded price and exact machine family register](../PROCUREMENT/2026-11-22-LIVE-MACHINERY-PRICE-EVIDENCE.md).

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

## High-moisture design correction (new — 22 Nov 2026)
**New upstream interface hold point:** Infinite IFD prefers **<8 mm particles** and **<45% inlet moisture** in its narrative, but its table also shows capacity at **<50%**, while EcoStan ESM150 output ranges **2–10mm** and its conventional HM grinder requires **≤15%-moisture material**. Pre-dryer screening/wet grinding and exactly-50% wetwood contractual performance must be resolved. **IFD3000 lists ~3,000 kg/h dry material at <45% inlet**, borderline against this plant's ~3,080kg/h nominal dryer-out balance. [IFD OEM](https://www.infinitedryer.com/ifd.html) · [ESM OEM](https://www.ecostan.com/products/sawdust-machine) · [HM OEM](https://www.ecostan.com/products/hammer-mill).

The 1.563 MT/hour water-evaporation requirement assumes **40% incoming moisture only**. At **50%** and the same output, mass balance instead requires approximately **2.492 MT/hour evaporated water** and **5.57 wet MT/hour log preparation** at 340 productive hours. An indicated 1.8–2.0 MT/h dryer and 3–5 wet TPH chipper would be bottlenecks. **Do not order these models as a guaranteed year-round 1,000-MT/month line** without wet-wood tests and a confirmed pre-drying or longer-hours strategy. For a 50%-moisture two-shift design, evaluate **~2.75–3.0 MT/hour water-evaporation** as a provisional engineering RFP with reserve, not a final price. See [wood-moisture technical note](05-WOOD-MOISTURE-AND-DRYER-SIZING.md).

## New 22 Nov comparative press/dryer evidence
| OEM reference (public) | Public price/model distinction | Continuous test requirement |
|---|---|---|
| EcoStan BM90/100 seller listing | **₹25.95L**, 117 HP, 1.5–2.5 TPH listing **vs** BPM90HD official **89.5 HP**, 1.3–2.0 TPH | Must choose exact model/90mm accessories and test on local hardwood |
| Lehra 90mm machine | ~**₹21.75L** asking, 87.5 HP/2.0 TPH official reference | Written >=1.6 saleable TPH on approved drywood and agreed upkeep |
| Radhe Jumbo90 | ~**₹22.51L**, 1.5 TPH listing | **Uncomfortably narrow** 16h duty at 340 productive hours |
| Ronak Jumbo90 | ~**₹21.75L**, 1.5 TPH | An observed 230 RPM is NOT verified 230 ram strokes/minute |
| Infinite IFD3000 | ~**₹42L** asking; **1,800 kg water evaporated/h** | Controlled <=40% moisture; 50% case fails 340h requirement |
| Infinite IFD5000 | ~**₹68L** asking; **3,000 kg water evaporated/h** | Technically promising 50% design; requires guaranteed wood/thermal-electricity and complete safe installation quote |

**Historical wear evidence, not modern warranty:** FAO's older Indian piston-press discussion quotes certain dies roughly **500–1,000 operating hours**, and another field reference **~1,300h** under particular materials and reboring schedules. This cannot be extrapolated as a replacement every 500h for EcoStan, Lehra, Radhe, Ronak or Jay Khodiyar. OEM signed wood-specific consumables and maintenance windows control. [FAO wear discussion](https://www.fao.org/4/t0275e/t0275e04.htm).

At rated 1.5 TPH per press, two presses produce **1,020 MT in 340 productive h**, just **2% theoretical margin** over 1,000. If sustainably >=1.6 TPH per press, potential is **1,088 MT** on same hours (~8.8% planning reserve), but **not a warranty**. One shared chipper and one dryer still remain common failure points. Request an OEM witnessed **72 logged production-hour test** on defined wood, including all stop time, real briquette tonnage, rejects and fuel/energy.

Latest prices and evidence: [22 Nov live-price research](../PROCUREMENT/2026-11-22-LIVE-MACHINERY-PRICE-EVIDENCE.md) · [RFQ](../PROCUREMENT/AKASHYA-1000MT-FORMAL-TURNKEY-RFQ.md).
