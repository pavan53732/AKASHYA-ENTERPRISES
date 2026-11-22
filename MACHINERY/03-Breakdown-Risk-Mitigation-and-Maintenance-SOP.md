# Breakdown resilience & maintenance SOP — 1,000 MT/month
**Planning reference updated 23 Nov 2026.** Applicable to the proposed 1,000 MT/month line in Anakapalli. Source tiers in the tables are planning estimates unless a specific historical or manufacturer document is cited. Approve the final schedule through the equipment makers and competent site engineers.

| Breakdown under 25-day schedule | Finished output at risk | Gross revenue delayed at ₹8,000/MT |
|---|---|---:|
| One press stops 1 production day | ~20 MT | **₹1.60 lakh** |
| One press stops 3 days | ~60 MT | **₹4.80 lakh** |
| Both stop 3 days | ~120 MT | **₹9.60 lakh** |
| Shared dryer stops 5 days after buffers exhausted | up to 200 MT | **₹16.00 lakh** |

Revenue figures use the promoter-observed ₹8,000 per finished MT at the 1,000 MT/month planning volume, first recorded 22 Nov 2026. GST/freight basis, volume commitment and offer validity remain unverified. The 40% incoming wood baseline gives the planned schedule. The 50% case needs **1,895 wet MT/month** and **2,492 kg/h evaporation** at 340 productive h. Losses above assume no recovery or stock cover during the stated outage and represent sales timing exposure.

## Redundancy vs. spare capacity
Two presses each expected to deliver 500 MT/month **are not N+1 at full 1,000 MT target**. Failure of one leaves ~500 MT/month if the second press and upstream feed remain operational. Shared dryer, log processor, dust-safety systems, substation and utility feeders are other single-point failures. Quote separate/splittable systems to maintain 50% safe service through an upstream fault. Never bypass fire, dust or electrical interlocks for output.

## Operating controls — equipment-specific estimated check/rest/service windows
**Definitions:** “continuous industrial duty” does **not** mean workers never rotate or machines have no maintenance. Published **216, 230 and 240 machine RPM** figures apply to the supplier/model references in the [machinery price evidence](../PROCUREMENT/2026-11-22-LIVE-MACHINERY-PRICE-EVIDENCE.md). Measure *loaded ram strokes/min* separately, and no current OEM documentation verifies a universal rule “stop a 90mm press 1 hour after every 8 running hours.” Every interval below is **an initial planning allowance [EST]**, not approved OEM service instruction, compulsory legal rest cycle, exact bearing-temperature setpoint, or proof of actual availability. Apply local labour law, OEM manual, risk assessment and safe lockout/isolations.

| Hardware / operating hazard | Online/live monitoring during operation | Provisional planned safe-stop / inspections [EST] | Spare and downtime logging requirement |
|---|---|---|---|
| **01 Log yard loader/unloader** | Before-use brake/hydraulic/tyre checks; daily tonnes, route segregation, trained driver | **10–20 min/day** pre-start, service based on actual engine hours per maker | Tyres, hydraulic hoses/filters, bucket pin, hydraulic oil leaks |
| **02 Log-to-sawdust / wet-rated 6+TPH shredder/chipper** | Every **1–2h** feed/particle/motor-current sample; chipper jam/metal sensor and knife-temperature observation | **10–20 min/shift**, **1–3h/week** guarded blade/screen inspection, major service only per OEM | Matched knife/sharpening set, bearings, rotor, cleaning of wetwood/resin, recorded 40/50% TPH and all jam minutes |
| **03 Material conveyors, magnets and screens** | Each shift belt tracking, magnet contamination collection, screw load, bunker high/low sensors | **10–20 min/day** safe clean (some checks online), **1–2h/week** bearings/belt & guard check | Belt/splices, roller/chain, magnet/screen size, blocked transfer/bridging |
| **04 Wet grinder if required before flash dryer** | Every **1–2h** output sieve (<8mm if IFD), plugging/moisture, motor current, wet-wood blade fouling | **15–30 min/shift**, **2–4h/week** OEM lockout and tooling cleaning | Wet-rated machine only; conventional **≤15%-moisture HM cannot be assumed** to run on 40–50% wood |
| **05 Furnace/HAG, dryer, ID fans, cyclones/airlocks** | Continuous feed+exit temp, gas O₂ where specified, spark, fan vibration, ΔP, hourly inlet/outlet moisture and fuel | **10–30 min/shift** approved inspection; **2–4h/week** burner ash, airlock/duct/cyclone clean; **4–8h/month** deeper maintenance | Burner grate/ash, fans/belts, high-temperature seals, airlock, monitored fuel **kg/kg water**, stop safely before any inspection inside duct/furnace |
| **06 Dry hammer mill / separator** | Every **1–2h** dry-feed moisture (must meet OEM), particle oversize, screening, motor current, dust/metal alarms | **10–20 min/shift**, **2–4h/week** approved hammer, sieve, guard/bearing service | Hammer/screen inventory; log rework % and whether grinder caps ~3.08 dry TPH |
| **07 2 × mechanical 90mm presses** | Each **hour** finished MT/press, fines, feed moisture; every **2–4h** accessible bearing/lube/current/temp/noise checks without guard removal | **10–20 min per press/shift** sample checks, **2–4h/week** coordinated safe ram/die inspection, **4–8h/month** agreed detailed preventive tasks | Separate actual stroke sensor vs motor RPM, die/ram tonnes before wear, vibration, oil filters, alarm bypass attempts, 72h production test |
| **08 Cooling tracks, packaging and finished stock** | Each shift cooled product temp, damage/shatter, moisture, dust accumulation | **10–20 min/shift** approved clean; **1–2h/week** conveyor/cooling fan checks | Broken output rate, motor drive belts, safe storage residence and heat/cold emissions |
| **09 Dust collector, baghouse, spark/fire/isolation systems** | **Continuous** differential pressure, spark/explosion protection state, alarm trips, blocked ducts and pressure | Engineer/OEM mandatory daily visual checks and **weekly documented** protective-device check; formal safety equipment service per manufacturer | Replacement filters, leakage, grounding, vent integrity, no restart until safety interlocks reset/approved |
| **10 MCC/PLC/VFD, substation/earthing** | Live voltage/current/kVA/kWh/power factor, transformer temp, trips, start/stop provenance | Qualified electrical technician per-shift checks and **monthly scheduled** insulation/thermal review as appropriate; high-voltage testing only by authorised team | Critical VFD/contactor/relay, lockout, mains blackout and generator plan |
| **11 Weighbridge, moisture/QC laboratory** | Every truck gross/tare, calibrated reference checks, sample chain-of-custody | **Daily verification**; statutory weighbridge calibration per authority, moisture-lab standards; monthly tool review | Recalibration certificate, rejections, legal wood transport |
| **12 Emergency spares/repair workshop** | Running replacement inventory by machine model | **Weekly** check stock and delivery promise, **monthly** bin audit | OEM 2-year wear consumption, minimum machine-specific critical assemblies |

### Running hours, operator relief and reserved outage time

| Plan [EST] | Staffed schedule and relief | Productive h/month | Nonproductive allowance within schedule | Use in maintenance planning |
|---|---|---:|---:|---|
| **16 h/day × 25** | Two 8 h shifts with trained relief, logged handover and continuous hot-dryer supervision | 340 at 85% | 60 h | Schedule major stops in off-shift windows where cooling and supervision permit. Track production-time losses separately. |
| **20 h/day × 25** | Staffed roster with relief and supervised heat-system shutdown/restart | 425 at 85% | 75 h | Up to 4 h/day outside production schedule. Actual work window is reduced by safe shutdown, cooling and startup. |
| **24 h/day × 26** | Rotating staffed shifts with qualified relief, maintenance coverage and separate plant stops | 499.2 at 80% | 124.8 h | Use coordinated stop blocks for common chipper/dryer, press work and protective systems. |

**Illustrative 16 h planning month.** Of the 60 h within-schedule allowance, reserve **12.5 h** for 30 minutes/day logged stop/start/cleaning, **8 h** for four coordinated two-hour weekly stops, and **4 h** for a monthly planned shutdown. That gives **24.5 planned h + 35.5 h for other losses**. If weekly/monthly jobs overlap or occur outside scheduled plant hours, count only actual minutes lost to production. Simultaneous maintenance on the chipper, dryer and one press can share a single line stop. Record isolated work minutes, cooldown/restart minutes, operator relief and any loss of saleable production as separate fields.

**Hourly monitoring** is normally visual, instrumented or from an approved protected sample point. Contact with moving parts, blade/die changes, hot-dryer access or blocked-duct entry require the OEM/approved shutdown and isolation procedure. Keep the furnace/dryer staffed through shift relief and managed shutdown. Maximum uninterrupted hot runtime and restart permissives remain **UNKNOWN** until the supplier provides the applicable manual and the site test. There is no substantiated common rest interval for the listed presses.

### Machine-life and running cost estimation
Historic FAO reports for certain older piston dies: **~500–1,000 operating hours** and an instance of **~1,300h with intermediate reboring**, under specific feedstocks; this is **NOT modern 2026 maker-specific life or price**. Knife/bearing/die life for local Casuarina/Eucalyptus/Subabul is **unknown** until OEM trials. Request per **1000 finished MT**: dies, rams, blades, oil, filters, bearings, screens, electricity, dryer fuel, loss hours, labour and maintenance contractor rate. No exact hourly cooler/oil change is asserted. [FAO background](https://www.fao.org/4/t0275e/t0275e04.htm) · [EcoStan press moisture/size](https://www.ecostan.com/products/briquetting-machine) · [Ronak machine RPM](https://ronakeng.com/manual-briquetting-machine/) · [Infinite IFD duty table](https://www.infinitedryer.com/ifd.html).

### Provisional wear-part inspection and changeout allowances

These are **first-pass maintenance and downtime estimates** for staffing/spare planning. Inspection hours are running-hour triggers to review wear logs during commissioning. Replace only against the offered machine’s limits and actual condition. Changeout windows allow for hands-on work and must be extended for any additional cooldown, isolation, reheat, testing and material dependency. Use qualified service staff and approved parts, lubricants and procedures.

| Component | Engineering review window [EST] | Indicative hands-on changeout [EST] | Measurements and spares to record |
|---|---|---|---|
| **Ram/punch** | Review wear trend at **80–150 h** | **0.5–1 h** per press | OEM alignment/wear method, a matched replacement and service hours |
| **Die / collet** | Review condition at **150–300 h** | **1–2 h** per press | Diameter, surface damage, tonnes since service, matched spare and OEM approval for rework |
| **Guides, bushings and seals** | Review wear trend at **400–800 h** | **2–3 h** work block | Loaded alignment, OEM limits and correct kit |
| **Chipper knives and anvil** | Inspect condition by shift and review sharpen/rotation need at **40–80 h** | **0.5–1 h** | Knife damage, cut-size drift, matched set, supplier-approved clearances |
| **Mill hammers / screens** | Review hammers at **80–120 h** and screens at **200–400 h**, with routine condition checks each shift | **1–2 h** for hammers, **0.5–1 h** for screens | Vibration, screen blinding/perforation, balanced approved kits |
| **Lubrication system** | Level, pressure and leaks each staffed shift; intervals per the offered OEM | **~1 h** budgeting block for routine service | Quote oil grade, filter, normal operating ranges and calendar/hour interval. **Lehra Fuel Industries** public 90 mm sample calls out **7–10 days for filter service** and **three months for oil** for its stated equipment. |
| **Airlocks, fans and cyclone outlets** | Routine weekly review, condition-based follow-up per thermal package | **1–2 h** indicative airlock work block after cooled/isolated access | Leaks, vane and seal condition, fan vibration, spare and hot-start procedure |
| **Conveyor belts, drives and rollers** | Shift observation plus weekly approved isolated inspection | **1–3 h** depending on access and duty | Tracking, tension, bearings, roller and splice kit |
| **Baghouse, sparks and fire equipment** | Review instrument readings each shift. Test protective functions at approved intervals. | OEM/EHS schedule and access scope to determine | Filters/DP trend, alarm evidence, signed test and permission to return to service |
| **MCC/PLC, transformer and weighbridge/QC** | Electrical checks and statutory/quality verification per responsible engineer or authority. | OEM/specialist schedule | Trip history, interlock verification, instrument calibration and spare component compatibility |

**Supplier-specific gap.** EcoStan, Radhe Engineering Co / RICO, Ronak and Jay Khodiyar have published performance or machine specifications, but applicable maintenance intervals, the permitted continuous loaded run and mandatory cooling time for the site offer need the offered model’s manual. Lehra’s publicly hosted intervals apply to its sample scope only. Infinite publishes dryer capacity and fuel/load figures. Cooldown, supervised restart, cleaning and protective-device test windows need the furnace/dryer package and site procedure. [Lehra sample](https://5.imimg.com/data5/SELLER/Doc/2026/4/599355057/JI/VP/UE/253839848/white-coal-making-machine.pdf) · [Infinite IFD](https://www.infinitedryer.com/ifd.html) · [Wood dust engineering reference](https://www.osha.gov/wood-dust/solutions).

## Per-shift operational data to retain
Log **time at rated output** and **time at feed/quality failure** separately; record plant production, each press discharge, dryer input wettonnes/%moisture, water removed, fuel kg, kWh, unplanned minutes by machine, labour shift, knife/die service minutes and wet/dry particle-screen oversize. A daily sheet should reconcile **wet delivered wood → cleaned feed → dryer water removed → dry press feed → finished passed/rejected product**, or else monthly 1,000 MT cannot be validated.

## Buffers (provisional, engineering signoff required)
- Wet chips: provisional **2–3 days** weather-protected and fire-engineer reviewed, not a universal legal maximum. For 40%-wood **4.64wet TPH ×340h/25d ≈63MT/day**, 2–3 days of chip stock could exceed **126–189 wet MT**, requiring engineered compartmentation, pile temperature and air movement. Do **not** design such a pile solely from this suggested day count. Rotting, self-heating and fire risk need storage design.
- Dried material: 1–2 days nominal press-feed stock *only if dust/fire engineer approves protected compartments, max pile size, ventilation and hot-particle prevention.* No unregulated open sawdust heap is acceptable.
- Finished briquettes: 2–3 days/80–120 MT protected dry stock, subject to safe fire-rated storage.
- On-site OEM-specified spares: dies, rams, knife sets, bearings, lubricating system, approved electrical parts and dryer fan/airlock components; costing ₹6–8 lakh is **preliminary**.

## Vendor contract clauses
Require acceptance test, 12-month defect warranty terms, spare price list and availability years 1–5, published repair procedures, local service response schedule, technician training, root-cause reporting, explicit wear-part and force-majeure exclusions, and safety certification. Do not promise “die change in three hours” or “48-hour engineer on-site” without signed supplier acceptance.

See [procurement RFQ](../PROCUREMENT/2026-11-22-MACHINERY-PRICE-AND-RFQ-REGISTER.md) and [15-year price risk](../FINANCE/15-YEAR-INFLATION-AND-CASHFLOW-MODEL.md).

## Product and dryer failure modes from new research
The uploaded owner document's pellet-mill list (roller dies, die-hole clogging) must **not** be described as verified failure modes of a mechanical piston ram press. Applicable checks for a piston machine are OEM-specific ram/die wear, lubricator condition, bearing/vibration, overheating, blocked feed, overload and high-moisture material **with an interlocked diversion/stop**. There is no verified universal die-life in days. Maintain separate spare-parts lead-time table for press, chipper, dryer, fans, baghouse and controls. In a 50% high-moisture case the existing 1.8–2.0 MT/h water removal can cause **chronic production loss despite zero breakdowns**. See [dryer capacity](05-WOOD-MOISTURE-AND-DRYER-SIZING.md) and [site safety register](../SAFETY/FIRE-DUST-AND-THERMAL-RISK-REGISTER.md).
