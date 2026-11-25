# Machinery cost-rebasing decision note — published 22 Nov 2026
**Use for owner/internal lender pre-application planning only.** This is **not a new sanctioned CAPEX, nor bank-certified project cost**. Data from [public seller price register](../PROCUREMENT/2026-11-22-LIVE-MACHINERY-PRICE-EVIDENCE.md) and existing [₹520L installed owner BOM](../PROCUREMENT/COMPLETE-1000MT-TURNKEY-BILL-OF-MATERIALS.md).

## Old baseline retained until written technical bids
- Plant/machinery/handling planning allowance: **₹310 lakh**; civil/utility/erection allowance: **₹210 lakh**; **fixed total ₹520 lakh excluding land**.
- Opening working capital estimate **₹99.43 lakh** → total initial owner cash plan **₹619.43 lakh** excluding land and several cash contingencies. One partial Ex-Works vendor quotation received; complete comparable installed quotes not obtained. Never treat marketplace prices as binding.
- Existing Excel and 10-page DPR are *previous owner modelling snapshots*. This live-price research does **not** overwrite them or prove existing figures are exact. Cashflow sensitivity still assumes owner prices and unverified power/drying fuel.

**25 Nov quote reconciliation:** [EcoStan ES/26-27/08526](../PROCUREMENT/2026-11-22-MACHINERY-PRICE-AND-RFQ-REGISTER.md) totals **₹82.65L + ₹14.877L IGST = ₹97.527L Ex-Works** for one each of five machines. At 40% advance on gross (if vendor confirms tax basis), cash ₹39.0108L; remaining ₹58.5162L before delivery; advance nonrefundable under stated terms. Delivery/offload, site costs and full integrated equipment extra/unknown; quoted capacities fail 340h and 35% dryer ceiling excludes 40/50% scenarios. **Do not subtract ₹82.65L from ₹520L or scale this partial line blindly.** Bank CAPEX/working capital remain unchanged pending comparable complete scope, moisture trial and acceptance guarantees.

## Counterfactual buyer options to price separately
| Technical option | Line design | Public machinery evidence | Important cost risk |
|---|---|---|---|
| **A: controlled ≤40% wetwood** | Two presses proven at ≥1.6 TPH each, wet prep sized above 4.64 wet TPH, dryer at 1.8–2.0 TPH water with required dried flow | **IFD3000 ₹42L**, dried flow needs reconciliation. **RFD2000 ₹32L**, 1,250 kg/h evaporation falls short. Press public samples and asks by seller in the [machinery price evidence](../PROCUREMENT/2026-11-22-LIVE-MACHINERY-PRICE-EVIDENCE.md). | Seasonally wetter feed can change fuel, storage, prep and available hours |
| **B: robust 50% wetwood** | 1,895 wet MT/month, 5.57 wet TPH with reserve, 2,492 kg/h water removal and ~3.08 TPH dry flow at 340 h | **IFD5000 ₹68L**, exact 50% test required. **RFD5000** asks for price and has 3.0 TPH dry claim at <60%. **RFD7500 ₹99L**, subject to site and wood trial. | IFD equipment asks differ by **₹26L**. Installed increment, furnace fuel, HT and wet milling remain unknown. |
| **C: longer legal shifts and smaller dryer** | 20h×25d at 85% uptime = 425 productive h | IFD3000 1.8 TPH water/h needs **~471 productive hours** at 50%, so insufficient; a true **2.0 TPH** dryer needs ~424 hours, essentially **zero buffer** | Night shifts, electrical ToD and personnel costs rise, and 1 outage can wipe 1,000-MT target |
| **D: redundancy** | Separate dryer/press modules and engineered wood feeding | Not enough comparable quotes | Often higher capex but better uptime during common equipment faults |

**Owner's illustrative 50%-wood EBITDA ₹5.18L/month holds all nonwood costs unchanged.** It excludes higher thermal-fuel costs, additional power, extra labour, quality rejects, new equipment capex and finance costs. **May be substantially overstated** if 50% duty is normal. Thermal fuel manufacturer's *maximum* consumption is not a normal load forecast; require guaranteed actual kg/MT.

## Revised 23 Nov machine price/bottleneck implications (ROUGH ESTIMATES only)
The 12 machinery/handling packages sum **₹250–444 lakh** of indicative engineering allowances; seven building/HT/installation/soft-cost packages **₹175–352 lakh**; total **₹425–796 lakh fixed excluding land**. These broad bounds highlight **quotation uncertainty**, not an equiprobable range. They cannot be entered automatically as 2026 invoice costs in the root XLSX/PDF. Original fixed **₹520L** and WC **₹99.43L** remain owner placeholders.

Three high-risk intersections control whether budget is feasible:
1. **Wet fine sizing:** Incoming 40–50% wood **4.64–5.57 wet TPH**, dryer wants **<8mm** feed (Infinite IFD), EcoStan ESM150 advertises 2–10mm and a conventional dry hammer mill permits **≤15%** feed moisture. Fine wet crusher/screens or rotary pre-dryer can add previously unpriced machinery and electricity.
2. **Dryer two simultaneous duties:** ~**1.56TPH water** *and* ~**3.08TPH dried product** at 40%; IFD3000 advertised **1.8 water / 3.0 dried** (<45% inlet), so one nominal check passes while other is marginal. At 50% 2.49TPH water means IFD5000 3.0 water/4.0 dry is closer, but the OEM page says **<50% feed**, not exactly 50% guaranteed.
3. **HT/electricity:** example 595HP ≈444kW main motors **before auxiliaries**. Owner 150kWh/finished MT at 1,000MT gives **150,000kWh/month**, equivalent to **~441kW averaged over 340 productive h**. These must be reconciled with starts, power factor, actual operating hours and 630/800/1000kVA HT proposals; **₹38L electrical allowance is unverified**.

**Do not calculate high-moisture project cash by adding IFD5000's ₹68L price to an already-included ₹75L furnace/dryer budget.** Instead replace matched dry/furnace subsystem on a quote-by-quote basis, then add tested wet-milling, safety, HT and working capital deltas. Price 16/20/24hr cases with maker-specific service stops and annual maintenance, rather than guessed universal hourly cooling gaps. Sources: [current live-price evidence](../PROCUREMENT/2026-11-22-LIVE-MACHINERY-PRICE-EVIDENCE.md), [maintenance allowances](../MACHINERY/03-Breakdown-Risk-Mitigation-and-Maintenance-SOP.md).

## Capacity-constrained scenario prototype — 25 Nov 2026

[Executable source](../scripts/plant_scenario_model.mjs) · [illustrative input values](SCENARIO-INPUTS-ILLUSTRATIVE.json). Required wet intake, dried product, evaporation and saleable press duty are separate. A missing capacity produces only a conditional upper bound and suppresses financial results; moisture outside a stated rating blocks output. The model accepts different shift durations, availability, measured energy/fuel inputs and 15 separate annual utilisation factors; separately escalates sale, wood, electricity, fuel, other variable and fixed costs. It is not an equipment selector or bank forecast.

| Calibration check @340 productive h | 40% wood | 50% wood |
|---|---:|---:|
| Raw wood MT per saleable MT | 1.579 | 1.895 |
| Wet TPH required | 4.644 | 5.573 |
| Dry TPH required | 3.080 | 3.080 |
| Evaporation TPH required | 1.563 | 2.492 |

**Mass-balance assumption made explicit:** inherited water figures assume dry-only rejected solids after the dryer, with 100 kg water retained in each tonne of finished briquettes. Dryer outlet before rejection is 1.04737 MT per saleable MT (~9.55% moisture). If rejection instead leaves at 10% moisture, dried throughput becomes 1.05263 MT and evaporation at 40% is 0.52632 rather than 0.53158 MT per saleable tonne. Both are theoretical; obtain stage-wise measured reject moisture. Do not mix assumptions across capacity checks.

Baseline monthly EBITDA calibration ~₹11.50L, not new evidence. Fuel rate and price are jointly calibrated to the original ₹600/finished MT at 40% and are not vendor estimates. Existing 15-year table is preserved, since this prototype simplifies fixed-cost escalation. At 35% quote, assuming 2.5 TPH wet dryer input yields a conditional maximum ~583 MT/month (unknown evaporation/dry/transfer capacities), not guaranteed production; 40/50% exceed the 35% offered limit.

**Binary gate:** existing root workbook and PDF are unchanged. Their validators hard-code eight sheets and ten pages. Extend and execute actual formula/cache/layout checks before publishing expanded files. Do not represent this source model as a regenerated or independently validated workbook/PDF. No supplier selection or budget rebasing.

## Finance rules
1. **Keep ₹520L as a planning placeholder** and place a visible **“quotation uncertainty / high-moisture capex TBD”** risk annotation beside it in lender planning. Do not treat the outdated broad ~₹4.0–5.5Cr internet inference as an upper bound. [Expanded 19-package owner cost estimate](../PROCUREMENT/COMPLETE-1000MT-TURNKEY-BILL-OF-MATERIALS.md) now gives a **wide internal ₹425–796L fixed-price envelope** for the 40% planning configuration (₹250–444L machinery + ₹175–352L civil/power/erection, all **[EST]**, not bids), **not** an approved revision to the ₹520L owner model.
2. Add line-by-line supplier bid equalisation, compare total cash outflow including unrecoverable GST, advances and retention timing; reconcile with civil engineer and APEPDCL actual connection quotation.
3. Request annual OEM maintenance, spares replacement and wear-life by feedstock. Include negotiated 15-year price escalation—not only one-off machine buy.
4. Add bank-specific DSCR, debt principal and tenure only after indicative finance terms arrive. The **15-year business operating horizon** is not automatically a 15-year bank loan.
5. **No irreversible purchase decision** before year-round moisture and legal timber source tests, 3 comparable complete quotes, site permissions and signed buyer fuel trial acceptance.

## Procurement timing
26–27 Nov owner sends neutral preliminary enquiries to [five primary OEMs plus Infinite dryer](../PROCUREMENT/SUPPLIER-ENQUIRIES/README.md); project-specific RFQ internal until approved; 8 Dec first bids target; 15–20 Dec technical comparison; 31 Dec bank-draft BOM target; 15 Jan lender application; 15 Mar 2027 *conditional* first-eligible-disbursement milestone. Dates are *owner targets*, not supplier commitments.

Supporting: [supplier contacts](../PROCUREMENT/SUPPLIER-CONTACTS-AND-RFQ-TRACKER.md) · [equalisation](../PROCUREMENT/TECHNICAL-COMMERCIAL-BID-EQUALISATION.md) · [15-year business scenarios](15-YEAR-INFLATION-AND-CASHFLOW-MODEL.md) · [moisture mass balance](../MACHINERY/05-WOOD-MOISTURE-AND-DRYER-SIZING.md).
