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

## Dryer procurement consequence
- Existing shortlisted 1,800–2,000 kg-water/h dryer **has reasonable nominal margin over the 1,563 kg/h at 40%**, before engineering losses.
- At **45%** incoming moisture, required 1,986 kg/h leaves virtually no margin on a 2,000 kg/h dryer.
- At **50%**, required **2,492 kg/h**; preliminary requirement with 10–20% engineering margin = **~2,750–3,000 kg-water/h**, *not a vendor quotation*.
- If a 2,000 kg/h genuine evaporation dryer is used with 50% feedstock, time needed = 847,400/2,000 ≈ **424 productive hours/month**, nearly all the 425 productive hours in a 20h×25d at 85% model. A 1,800 kg/h dryer would need **~471 productive hours** and cannot meet two-shift 340h target.
- At 50% moisture, wet-wood log processing also needs **1,895/340 = 5.57 wet TPH** before extra margin: a published “3–5 TPH” wood machine may be insufficient. At 40% it already needs **4.64 wet TPH**.
- A larger dryer, longer operation, pre-seasoned wood or extra dryer train are mutually different options, each changing capex, staffing, thermal fuel and reliability. **No recommendation to buy a 3,000 kg/h dryer until seasonal wood-moisture distribution is sampled and a supplier guarantees energy balance.**

## Required wood moisture test and supplier RFP
1. Select at least **3 legal timber supply sources** and separate Casuarina, Eucalyptus and Subabul loads.
2. Sample **>=3 different shipments per supplier/species** as initial screening, including surface/interior pieces from the load; seasonal sampling needed to know full-year distribution. This is owner research design, not an Indian mandatory standard.
3. Record wet-basis moisture via calibrated oven-dry reference or equivalent accepted lab method, bark %, species, diameters, stones, chipped particle distribution, supplier/transport cost, moisture distribution, time since felling and storage condition.
4. Collect vendor duty curves at **30/40/45/50% incoming moisture**, dry outlet at OEM-specified 8–12% press feed, water evaporation kg/h, thermal input kg or kcal per kg evaporated, blower/furnace motors, actual electrical kWh/finished MT, particulate exhaust and dust safety.
5. Compare **16, 20, 24-hour** legal shift cases, at 80/85% genuine availability; reserve hours for cleaning, cooling, maintenance and breakdown.
6. Require testable **40 tonne/day finished output** on selected wood across the whole line; write wetwood input and product reject criteria explicitly.

## Source quality
FAO tech note: https://www.fao.org/4/t0275e/t0275e04.htm ; EcoStan model documentation: https://www.ecostan.com/products/briquetting-machine ; 2020 technical review: https://www.mdpi.com/2071-1050/12/11/4609 . The above quantitative design numbers are **derived from owner scenario assumptions** rather than manufacturer measurements.
