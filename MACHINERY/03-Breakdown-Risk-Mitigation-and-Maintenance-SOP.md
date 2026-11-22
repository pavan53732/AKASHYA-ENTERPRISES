# Breakdown resilience & maintenance SOP — 1,000 MT/month
**Updated with machine-specific provisional intervals 23 Nov 2026; baseline 22 Nov 2026; selling price ₹8,000/MT, not ₹9,000/MT.** Documents are design targets; factory safety instructions must be approved by equipment OEM and competent EHS engineering team.

| Breakdown under 25-day schedule | Finished output at risk | **Revenue delayed**, not profit lost |
|---|---|---:|
| One press stops 1 production day | ~20 MT | **₹1.60 lakh** |
| One press stops 3 days | ~60 MT | **₹4.80 lakh** |
| Both stop 3 days | ~120 MT | **₹9.60 lakh** |
| Shared dryer stops 5 days after buffers exhausted | up to 200 MT | **₹16.00 lakh** |

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

### How many hours should machines run before a break?
- **16h/day plan:** two **8h staffed shifts** (lawful meal relief/rotation). With proper supervised relief an engineered press or dryer can run through an operator's meal break; **personnel rest is mandatory, automatic mechanical cool-down every 1/2/4/8 hours is NOT a known universal OEM requirement**. Stop when lubrication/temp/dust hazards or the signed vendor manual require it.
- **20h/day plan:** provides 4h/day scheduled off-line for cleaning/repair (subject to startup/cooldown), but shift roster and daily fatigue controls must be lawful. It does not automatically make an undersized **1.8TPH evaporation** dryer sufficient for **50%** wood (would need **~471 productive hours**).
- **24h/day plan:** multiple legally staffed rotating shifts plus planned line stop/maintenance reserve; **80% availability** already models 124.8h lost in 624h schedule. Don't claim true 24h uninterrupted availability with manual wood feeding.
- At **16h ×25d =400 scheduled hours/month**, **85% availability allows 60 nonproductive hours**. Example only: 30min/day ×25 days = **12.5h**, 2h weekly ×4 = **8h**, 4h monthly = **4h**, total **24.5h planned** and remaining **35.5h for other loss**, including faults/warmups. Do not add all per-machine weekly intervals arithmetically: many are **coordinated line stops**. If OEM requires more service or startup time, recompute productive hours and finished TPH. A separate daily 10min check is not always a stop: specify live monitoring vs isolated service.

### Machine-life and running cost estimation
Historic FAO reports for certain older piston dies: **~500–1,000 operating hours** and an instance of **~1,300h with intermediate reboring**, under specific feedstocks; this is **NOT modern 2026 maker-specific life or price**. Knife/bearing/die life for local Casuarina/Eucalyptus/Subabul is **unknown** until OEM trials. Request per **1000 finished MT**: dies, rams, blades, oil, filters, bearings, screens, electricity, dryer fuel, loss hours, labour and maintenance contractor rate. No exact hourly cooler/oil change is asserted. [FAO background](https://www.fao.org/4/t0275e/t0275e04.htm) · [EcoStan press moisture/size](https://www.ecostan.com/products/briquetting-machine) · [Ronak machine RPM](https://ronakeng.com/manual-briquetting-machine/) · [Infinite IFD duty table](https://www.infinitedryer.com/ifd.html).

### Provisional wear-part service and replacement intervals [Engineering Planning Guide]
Based on field experience with abrasive hardwood and Indian mechanical piston briquetting plants:

| Component / Subassembly | Typical service life (running hours) | Recommended maintenance action | Changeout downtime | Critical spare stock requirement |
|---|---:|---|---:|---|
| **Ram Punch Head / Tip** | **80–150 h** | Inspect for rounding/wear; swap with pre-faced spare; hardface worn tip with high-chromium carbide electrodes | 30–45 min | 4 complete spare punch heads in toolroom |
| **Taper Die / Collet Rings** | **150–300 h** | Measure internal bore diameter; re-bore to 90 mm profile or replace segmented die collets | 1.0–2.0 h | 2 complete die holder sets + collet rings |
| **Guide Sleeves / Wear Rings** | **400–800 h** | Inspect alignment and clearance; replace bronze/hardened steel wear bushes | 2.0–3.0 h | 2 sets guide sleeves |
| **Chipper Knives & Anvils** | **40–80 h (sharpen) / 400–600 h (replace)** | Rotate/re-sharpen knives to correct cutting angle; inspect anvil clearance (1.5–2.0 mm) | 30–60 min | 3 matched knife sets (one running, one ready, one at grinding workshop) |
| **Hammer Mill Hammers** | **80–120 h (turn edge) / 300–500 h (replace)** | Reverse hammers to utilize all 4 wear corners; replace entire balanced set when worn | 1.0–2.0 h | 2 complete balanced hammer sets |
| **Hammer Mill Sieve Screens** | **200–400 h** | Check perforation size and screen cracking; replace blinded or worn perforated plate | 30–45 min | 4 replacement screens (3 mm, 5 mm, 8 mm) |
| **Centralized Lube Oil & Filter** | **500 h (filter) / 1,000–1,500 h (oil flush)** | Replace 10-micron oil filter element; drain, flush, and refill ISO VG 220/320 gear oil | 1.0 h (scheduled stop) | 6 oil filter cartridges + 2 barrels (420 L) gear oil |
| **Dryer Rotary Airlock Vanes** | **1,000–1,500 h** | Inspect neoprene/EPDM flexible tips; adjust blade clearance to maintain cyclone vacuum seal | 1.0–2.0 h | 2 sets airlock rotor tips + shaft seals |
| **Conveyor Belts & Roller Bearings** | **2,500–5,000 h** | Grease weekly (NLGI 2 EP grease); replace sealed pillow block bearings upon vibration | 1.0–3.0 h | 4 spare conveyor bearings + 1 belt splice kit |

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
