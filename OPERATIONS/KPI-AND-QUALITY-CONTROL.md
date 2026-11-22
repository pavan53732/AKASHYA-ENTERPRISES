# Operations, wood quality and 15-year management KPIs
## Daily production and cash margin dashboard
| KPI | Unit | Starting target / rule |
|---|---|---|
| Finished briquettes dispatched | MT/day | 40 at 25 days/month full rate |
| Wet logs received | MT/day | ~63.16 at 40% moisture |
| Saleable yield | Finished MT/wet incoming MT | ~0.633 at reference moisture; re-compute by actual batch |
| Wood moisture | wet basis % | Measured every load, not assumed 40% |
| Dryer evaporation | kg water/hour | actual meter/balance vs guarantee, 1,563 kg/h two-shift requirement |
| Output per press | MT/productive hour | ≥1.471 each at 340 productive hours/month |
| Press availability | uptime % | 85% is modelling allowance, not a warranty; record **scheduled vs productive** hours and all line stops separately |
| Press strokes vs shaft RPM | actual strokes/min and motor RPM per model | **UNVERIFIED** until timed/physical OEM test; avoid treating BPM model name or 216/230 RPM as strokes |
| Dry screw/press feed | moisture % / particle size | OEM target typically **8–12% moisture**; EcoStan 90HD ≤15×8mm feed; record sieved >size fraction |
| Dryer inlet fine-particle fraction | % passing <8mm | If Infinite IFD selected, verify **<8mm** requirement on incoming 40/50%-moisture wood |
| Stage capacity — actual running | wet kg/h → dryer dry kg/h → saleable kg/h | At 40%: **4,640 wetkg/h**, roughly **3,080 driedkg/h**, **2,941 finishedkg/h**, with measured loss allocations |
| OEM downtime by component | planned/unplanned min | Log per machine; general 85% allows **60 lost h per 400 scheduled h**, not a separate extra penalty |
| kWh per finished tonne | kWh/MT | 150 provisional, verify under real throughput |
| Dryer fuel used | kg/MT finished | Vendor guaranteed and daily measured; existing ₹600 cost needs fuel type and quantity proof |
| Briquette moisture/ash/GCV | % / kcal/kg | 3rd-party lab tests, buyer-specific specification |
| Unit selling realised | ex-GST ₹/MT | ₹8,000 observed starting assumption; **measure weighted realised** |
| Wet wood weighted landed cost | ex-GST ₹/wet MT | ₹2,000 observed, supplier contracts needed |
| EBITDA cash margin | ₹/MT | ₹1,150 initial full-rate estimate; not PAT |
| Customer outstanding | days | target 20 operating days; monitor defaults |
| Downtime by machine | minutes | record common chipper/dryer/safe baghouse stops and press stops separately |
| Near misses / fire dust | incident | stop unsafe operations and preserve evidence |

## Per-shift machine log requirements
Use a separate row for **log machine/wet grinder, conveyors, furnace/dryer, dry hammer, Press A, Press B, cooling, baghouse/fire protection, MCC/HT, weighbridge**. For every unit write opening/closing motor-meter hours, instantaneous input and output kg/h, moisture (before/after), actual current/kW, material jams, alarm-trip timestamp, scheduled stop minutes, emergency downtime minutes, repaired spare parts, and operator handover. **Do not invent an 8-hour compulsory cooling break**: if the precise OEM manual requires cooling, log its duration; otherwise measure natural equipment temperatures and safety interlocks.

Under 16h/day and 25 days, 85% modeled availability = **340 useful / 400 scheduled hours**. Trial example of 30min/d cleanup, 2h/week planned service and 4h/mo deep check uses **24.5h** from the 60h monthly downtime allowance, leaving **35.5h** for breakdown, shortages and startup. If the OEM requires more, revise TPH target or shift plan. All inspections inside active rotating equipment require proper isolation and permit.

**Monthly monitoring:** maintenance rupees per finished tonne; wood knife changes by wet tonne, press ram/die life by tested dry tonne, baghouse filter DP and change hours; **actual dryer fuel kilograms per kilogram of water evaporated**; compare the total site electric meter kWh and plant effective operating hours. Flag whether existing **150kWh/MT** assumption is consistent with equipment load and startup/standby readings. [SOP](../MACHINERY/03-Breakdown-Risk-Mitigation-and-Maintenance-SOP.md) · [OEM machine price/spec dossier](../PROCUREMENT/2026-11-22-LIVE-MACHINERY-PRICE-EVIDENCE.md).

## Wood acceptance process
Weigh in gross/tare, photo and species/source/legal transit documents, sample moisture at multiple locations per load, reject treated/painted/metal/stone-contaminated wood, record delivered truck freight and measure chips output. **Do not pay wet wood as if all wet tonnes convert one-to-one into briquettes.**

## Briquette product QC
Caliper diameter/length, fracture/abrasion, batch moisture, ash, GCV tested by certified laboratory, trace batch to raw wood supplier, inspect cool-down and safe covered storage. Do not guarantee <2% ash, 4,200 GCV or zero sulfur until actual tests show it and a buyer contract accepts the spec.

## Weekly controls before loan disbursement and commissioning
Every Friday until 12 March 2027: lender progress and missing KYC, permit filings, source quotations, quantity-priced timber and buyer letters, CAPEX drift and committed supplier deposits. After commissioning: 90-day real cost benchmarking then updated 15-year model/forward sales contracts.

See [breakdown SOP](../MACHINERY/03-Breakdown-Risk-Mitigation-and-Maintenance-SOP.md) and [project roadmap](../PROJECT-ROADMAP.md).

## Additional measured KPI and stop rules (new)
Per wood truck measure **moisture range and wood species**, not just average; track **actual kg water removed/hr**, **thermal fuel kg per 1,000 kg water evaporated**, **rejected-fuel MT**, **fines/fragmentation %,** cooling discharge temperature and **buyer boiler trial pass/fail**. Record at 40/45/50% wood conditions and track safe stockpile residence/temperature. When feed moisture exceeds the press's **written OEM limit**, divert to re-drying or stop the press per approved SOP; never force wet stock to preserve shipment numbers. Every customer must approve feeding, grate compatibility and combustion trial before sale claims. See [technical note](../MACHINERY/05-WOOD-MOISTURE-AND-DRYER-SIZING.md) and [buyer protocol](../MARKET-RESEARCH/03-90MM-BOILER-COMPATIBILITY-TRIAL-PROTOCOL.md).
