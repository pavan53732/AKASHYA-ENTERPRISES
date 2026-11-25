# Wood moisture, purchased-log yield and dryer capacity
**Engineering sensitivity dated 22 Nov 2026; NOT tested plant performance.** Product 1,000 MT/month, 10% finished moisture (wet basis), 5% input dry-solids loss, two-shift schedule 25×16h with 85% uptime = **340 productive hours/month**. Baseline wet wood price ₹2,000/MT owner-observed, NOT volume-contracted. Dryer thermal fuel/power is **NOT** included in incremental raw-wood cost calculations.

## Simplified mass balance
- Dry solids in finished 1,000 MT = 1,000×(1−0.10)=900 MT.
- Required dry wood solids = 900/(1−0.05) = **947.368 MT**.
- Incoming wet wood MT = 947.368/(1−incoming wet-basis moisture fraction).
- Indicative evaporated water = incoming wet mass×moisture fraction − 100 MT finished water.
- **Engineering limitation:** this simplification does not assign moisture to rejected material or furnace feed. Integrator must close a **measured wet/dry solids and water mass balance** for actual plant losses and rejects.
- Required dryer water removal kg/hour = monthly indicative evaporated water×1,000/340 hours.

## Required evaporation and wood cost by incoming moisture
| Incoming wet wood moisture | Purchased wet logs MT/mo | Wood cost ₹ lakh/mo | Indicative water removal MT/mo | Water evaporation kg/h at 340 h | EBITDA ₹ lakh/mo *before added drying costs* |
|---:|---:|---:|---:|---:|---:|
| 25% | 1,263 | 25.26 | 216 | 635 | 17.82 |
| 30% | 1,353 | 27.07 | 306 | 900 | 16.01 |
| 35% | 1,458 | 29.15 | 410 | 1,206 | 13.93 |
| **40% BASE** | **1,579** | **31.58** | **532** | **1,563** | **11.50** |
| 45% | 1,723 | 34.45 | 675 | 1,986 | 8.63 |
| **50% HIGH-WET** | **1,895** | **37.89** | **847** | **2,492** | **5.18** |
| 55% | 2,105 | 42.11 | 1,058 | 3,111 | 0.97 |

The EBITDA column holds all non-wood operating costs constant. **Actual high-moisture EBITDA can be lower or monthly output can fall** due to more furnace fuel, power, rejects, oversized dryer purchase and reduced chipper throughput. The 10% moisture is finished product reference, **not automatically dryer-outlet press-feed target**. Obtain exact OEM press-feed moisture and particle-size limits; typical literature describes roughly 8–12% feed moisture but material-specific optimisation is mandatory.

## Crucial size and stage interface — wet pre-grind vs dry hammer mill
A 90mm mechanical press **cannot accept unchipped green logs**. The stages must match material **size, wet-basis moisture AND tonnes/hour simultaneously**. Example: [EcoStan ESM150](https://www.ecostan.com/products/sawdust-machine) quotes **2–10mm sawdust**, while the [Infinite IFD flash dryer](https://www.infinitedryer.com/ifd.html) says incoming particles **<8mm**; screen/recycle the 8–10mm fraction or obtain a site trial. The [EcoStan HM family](https://www.ecostan.com/products/hammer-mill) is documented for **≤15% feed moisture**, so **do not assume the dry hammer mill can pre-grind wet logs at 40–50%**. Possible plant routes are *wet-rated log eater/grinder to <8mm → flash dryer → dry mill/press* or *coarser chipper → rotary pre-dryer able to accept chips → fine milling/flash finish dryer → press*. Quote both with the same mass balance, actual wet-chip blade clogging and fire controls.

| Plant interface | 40%-moisture reference per productive h | 50%-moisture reference per productive h | OEM acceptance criterion |
|---|---:|---:|---|
| Legal log receiving | **4.64 wet MT/h** | **5.57 wet MT/h** | Chipper/sawdust **actual** ≥6wet MT/h with reserve or priced longer schedule |
| Wet sawdust before dryer | ~4.64 MT/h less measured sorting/metal losses | ~5.57 MT/h less sorting/metal losses | Pass through dryer **<8mm** (IFD), validate distribution not average |
| Water evaporated | **1.563 MT/h** | **2.492 MT/h** | Real guaranteed evaporation, 10–20% sizing reserve |
| Dry material after dryer | **~3.08 MT/h** before allocation of modeled 5% solids loss | **~3.08 MT/h** | Both **dryer dry-output** and dry mill must actually support this flow |
| Finished, saleable 90mm product | **2.941 MT/h** | **2.941 MT/h** | 2 presses each ≥1.60 MT/h tested, not nameplate only |

**Caution:** The simplified 3.08 MT/h intermediate number approximates wet-mass minus evaporation and is sensitive to the stage at which dry solids are rejected; use a measured full mass balance before equipment guarantees. Infinite IFD3000 publishes **~3.0 MT/h dry product at <45% input**, already borderline relative to ~3.08 MT/h. The same table says **<50%**, which does not warrant an **exact 50.0%** inlet trial.

| Productive hours per month | 40% wet feed TPH | 40% water kg/h | 50% wet feed TPH | 50% water kg/h | Dried material TPH [approx.] | Saleable combined TPH |
|---:|---:|---:|---:|---:|---:|---:|
| 340 | 4.644 | 1563 | 5.573 | 2492 | 3.080 | 2.941 |
| 425 | 3.715 | 1251 | 4.458 | 1994 | 2.464 | 2.353 |
| 499.2 | 3.163 | 1065 | 3.796 | 1697 | 2.098 | 2.003 |

All rows are **derived** at the same 1,000 MT/month target and use the same simplified reject allocation. The 425 h and 499.2 h rows correspond to the 20 h and 24 h operating plans. Design margin, outage costs, furnace fuel, pressure losses and allowable material temperature are separate engineering inputs.

For screening/regrind loops, estimate machine circulation as **fresh feed ÷ (1 − per-pass recirculation fraction)** if all rejected oversize returns to the same unit and there are no other branches. At **10% / 20%** recirculation, wet circulation is **5.16 / 5.80 TPH at 40%** and **6.19 / 6.96 TPH at 50%**. Dry full-stream circulation is about **3.42 / 3.85 TPH** under the same assumptions. These are derived planning sensitivities. Measure actual screen rejects and adjust feeders, conveyors and motors along the recycle path. An oversize-only dry hammer mill should instead be sized from the actual oversize stream plus rework.

## Dryer procurement consequence
- At **40%**, a true 1,800 kg/h evaporation rating clears the water check. Infinite **RFD2000** is rated at **1,250 kg/h water** and falls short. Its model-number “2000” aligns with an OEM dried-output band, and the **₹32L** public listing is equipment only. [machinery price evidence](../PROCUREMENT/2026-11-22-LIVE-MACHINERY-PRICE-EVIDENCE.md).
- At **45%** incoming moisture, required 1,986 kg/h leaves virtually no margin on a 2,000 kg/h dryer.
- At **50%**, required **2,492 kg/h** water implies **~2,750–3,000 kg/h** with engineering reserve. Infinite **IFD5000** lists **3,000 kg/h**, with exact 50% feed outside its stated <50% inlet. **RFD5000** lists **3,200 kg/h** water, but **3,000 kg/h** dry output at <60% inlet falls below the ~3,080 kg/h line estimate. Verify both duties together and quote cost and thermal fuel separately.
- If a 2,000 kg/h genuine evaporation dryer is used with 50% feedstock, time needed = 847,400/2,000 ≈ **424 productive hours/month**, nearly all the 425 productive hours in a 20h×25d at 85% model. A 1,800 kg/h dryer would need **~471 productive hours** and cannot meet two-shift 340h target.
- At 50% moisture, wet-wood log processing also needs **1,895/340 = 5.57 wet TPH** before extra margin: a published “3–5 TPH” wood machine may be insufficient. At 40% it already needs **4.64 wet TPH**.
- A larger dryer, longer operation, pre-seasoned wood or extra dryer train are mutually different options, each changing capex, staffing, thermal fuel and reliability. **No recommendation to buy a 3,000 kg/h dryer until seasonal wood-moisture distribution is sampled and a supplier guarantees energy balance.**

### Quoted FDD 25 / ESM 100 combination — 25 Nov 2026

[EcoStan written quote register](../PROCUREMENT/2026-11-22-MACHINERY-PRICE-AND-RFQ-REGISTER.md): FDD 25 ₹22.85L ex GST, 41 HP, 1.5–2.5 TPH unspecified wet/dry basis, **maximum 35% incoming material moisture**. Current [OEM double-pass FD25](https://www.ecostan.com/products/flash-dryer) lists 40%, <15 mm feed, dried biomass fuel and temperature up to 150°C; these are catalogue claims, not amendments to the quotation. ESM100 ₹25.55L, 106 HP, 2–3 TPH, logs ≤10 in, quoted 4–8 mm output versus [OEM 2–10 mm](https://www.ecostan.com/products/sawdust-machine). Obtain actual size distribution and wetwood trials; no automatic elimination of screening/rework.

**[DERIVED]** At 35% wet feed and 10% dried moisture (zero solids losses), if 2.5 TPH refers to wet feed, dried output = 2.5×0.65/0.90 = **1.806 TPH**, evaporation ~694 kg/h; if 2.5 TPH refers to dry output, required wet feed = **3.462 TPH** and evaporation ~962 kg/h, above the ESM100 nameplate maximum. At 340 productive h one DFC press at max 2.3 TPH yields ≤782 MT even before line losses. Both 40/50% cases remain outside quoted moisture limit; at 340 h the line needs 4.64/5.57 wet TPH and ~3.08 dried TPH. Even 24h scheduling does not cure moisture ceiling or prove duty. Obtain alternate dryer/pre-dryer and matched line scope.

For reference only, per saleable tonne at **15/20/25/30/35% wet-basis input** using the repository's 5% dry-solids-loss assumption and 10% finished moisture: wet wood input ≈ **1.115/1.184/1.263/1.353/1.457 MT**. These are not vendor-tested yields; reject moisture and furnace fuel excluded. Keep existing 40/50% scenarios and avoid mixing with other illustrative loss assumptions.

## Required wood moisture test and supplier RFP
1. Select at least **3 legal timber supply sources** and separate Casuarina, Eucalyptus and Subabul loads.
2. Sample **>=3 different shipments per supplier/species** as initial screening, including surface/interior pieces from the load; seasonal sampling needed to know full-year distribution. This is owner research design, not an Indian mandatory standard.
3. Record wet-basis moisture via calibrated oven-dry reference or equivalent accepted lab method, bark %, species, diameters, stones, chipped particle distribution, supplier/transport cost, moisture distribution, time since felling and storage condition.
4. Collect vendor duty curves at **30/40/45/50% incoming moisture**, dry outlet at OEM-specified 8–12% press feed, water evaporation kg/h, thermal input kg or kcal per kg evaporated, blower/furnace motors, actual electrical kWh/finished MT, particulate exhaust and dust safety.
5. Compare **16, 20, 24-hour** legal shift cases, at 80/85% genuine availability; reserve hours for cleaning, cooling, maintenance and breakdown.
6. Require testable **40 tonne/day finished output** on selected wood across the whole line; write wetwood input and product reject criteria explicitly.

## Source quality
FAO tech note: https://www.fao.org/4/t0275e/t0275e04.htm ; EcoStan model documentation: https://www.ecostan.com/products/briquetting-machine ; 2020 technical review: https://www.mdpi.com/2071-1050/12/11/4609 . The above quantitative design numbers are **derived from owner scenario assumptions** rather than manufacturer measurements.
