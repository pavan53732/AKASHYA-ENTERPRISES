# Jay Khodiyar Machine Tools — manufacturer-specific technical investigation

**INTERNAL ONLY — 25 November 2026.** Sequential public-source review: full official website (`jaykhodiyar.com`, `sitemap_index.xml` / 198 discovered URLs, all product/technical/support pages, redirect checks) AND official 20-page downloadable company brochure PDF examined. No written quotation addressed to AKASHYA ENTERPRISES; zero factory/brochure prices published; actual local wood test data, motor breakdowns, and loaded strokes/min remain open. [Shared master](../MACHINERY-MASTER.csv) tracks **27 Jay Khodiyar catalogue/legacy entries** (`JK-65/75/90`, `SH-50/WC-75/WC-100`, `JKWC75/100/150`, `JKCM75/100/150`, `50 HP Chipper Grinder`, `VC-30/50/75/100`, `HM-50/75/100 (100 HP)/100 (150 HP)`, `JK-BD-2000/3000/5000`, plus `JK-VP100/175/225` pellet-only comparison). Do not send this file externally. [External draft](../SUPPLIER-ENQUIRIES/04-JAY-KHODIYAR.md).

## 1. Supplier identity, contacts and website integrity check

- **Entity & Works:** Jay Khodiyar Machine Tools (JKMT), Samrat Industrial Area, Street No. 2, Gondal Road, Rajkot 360004, Gujarat, India. Established 1994; owner/chairman Mr. Sanjay Tilala. [About](https://jaykhodiyar.com/about-us/) · [Contact](https://jaykhodiyar.com/contact/)
- **Certifications & claims:** ISO 9001:2015 self-reported (brochure p. 18); claims 20+ patents, 22,800+ clients, 28,600+ installations, 85+ countries, 30–75 day equipment dispatch (brochure pp. 3–4, 19). These are self-reported marketing claims, not third-party operational reliability or local AP SLA proof.
- **Public contacts verified on `/contact/` & brochure:** `+91 76000 00014 / 16 / 18 / 19`, `+91 98253 25361` (WhatsApp), `+91 80000 00076`; `info@jaykhodiyar.com`, `export@jaykhodiyar.com`, `sales@jaykhodiyar.com` (brochure p. 19). International offices listed in Amsterdam, Vietnam, and Kenya.
- **Official brochure PDF (retrieved):** [20-page JKMT Brochure](https://drive.google.com/file/d/1iHYtGg_Io_yRU58HfzEk_1W9zAnibblm/view) linked directly from `jaykhodiyar.com` header.
- **Website URL / redirect audit (25 Nov 2026):**
  - `https://jaykhodiyar.com/product/wood-chipper-5tph/` → **redirects** to `/wood-chipper/` (where 5 TPH is no longer listed; max current model is `WC-100` 3–4 TPH).
  - `https://jaykhodiyar.com/product/biomass-dryer-machine/` → redirects to `/biomass-dryer-machine/`.
  - `https://jaykhodiyar.com/product/sawdust-dryer-machine/` → redirects to `/sawdust-dryer-machine/`.
  - `https://jaykhodiyar.com/wood-powder-machine/` and `/wood-powder-dryer/` → redirect to `/biomass-dryer-system/`.
  - `https://jaykhodiyar.com/sawdust-machine/` and `/services/` → redirect to homepage `/`.
  - `https://jaykhodiyar.com/after-sales/` (and `/after-sale/`) → **infinite HTTP 301 redirect loop** (server misconfiguration; service page unreachable).

## 2. Mechanical briquetting presses (`JK-65`, `JK-75`, `JK-90`)

Sources: [Briquetting Machine](https://jaykhodiyar.com/briquetting-machine/), [Briquette Machine](https://jaykhodiyar.com/briquette-machine/), [Briquette Press](https://jaykhodiyar.com/briquette-press/), [Briquetting Press](https://jaykhodiyar.com/briquetting-press/), [Briquette Plant](https://jaykhodiyar.com/briquette-plant/), [Briquetting Plant](https://jaykhodiyar.com/briquetting-plant/), [Briquette Making Machine](https://jaykhodiyar.com/briquette-making-machine/), and **Brochure PDF pp. 7–9**.

| Model | Diameter | Website HP / Brochure kW | Website capacity (kg/h) | Brochure capacity (kg/h) | Feed moisture (Web vs Brochure) | Feed size & Briquette length (Web vs Brochure) |
|---|---|---|---:|---:|---|---|
| **JK-65** | 65 mm *(brochure typo prints 90MM)* | 59 HP / 43.99 kW | 500–700 | Up to 800 ±10% | 8–12% (>15% dry) vs **5–10%** | `1×5×12 mm` vs `1×5 mm`; `50–450 mm` vs `50–300 mm` |
| **JK-75** | 75 mm | 69 HP / 51.45 kW | 700–1,000 | Up to 1,000 ±10% | 8–12% (>15% dry) vs **5–10%** | `1×5×12 mm` vs `1×5 mm`; `50–450 mm` vs `50–300 mm` |
| **JK-90 (Jumbo 90)** | **90 mm** | **91 HP / 67.85 kW** | **1,000–2,000** | **900–2,000 ±10%** *(bulk 50–250 kg/m³)* | **8–12%** (>15% dry) | `1×5×12 mm`; `50–450 mm` |

- **Design parameters claimed:** High-pressure mechanical ram & die (`~2,000 kg/cm²`), heavy-duty MS fabrication, electric motor with flywheel, screw feeder with hopper, automatic/centralized lubrication, electrical control panel with overload auto cut-off sensors, binderless (`natural lignin`), `24×7` continuous operation claim.
- **Catalogue discrepancies & missing data:**
  1. Brochure p. 9 (`JK-65`) copy-pastes *"jumbo 90"* text and `90MM` diameter; Brochure p. 8 (`JK-75`) repeats *"jumbo 90"* prose.
  2. Website tables state `500–700` / `8–12%` / `50–450 mm` for `JK-65` and `700–1,000` / `8–12%` for `JK-75`, vs brochure `up to 800` / `up to 1,000` / `5–10%` / `50–300 mm`. `JK-90` ranges differ between `1,000–2,000` and `900–2,000 ±10%` (and blog `/white-coal-machine/` cites `~1,800 kg/h`, max `300 mm` length, `<20 mm` feed at `10–15%`).
  3. **Zero OEM data published** for: motor-by-motor HP breakdown (main drive vs screw feeder vs lube vs cooling conveyor), flywheel/shaft **RPM**, **loaded physical piston strokes/min (BPM)**, stroke length, total machine weight (`~8,500 kg` only in third-party IndiaMART ads, not on `jaykhodiyar.com` or brochure), cooling-line length, lubrication oil grade/change intervals, and scheduled maintenance downtime.
- **Internal fit (90 mm line):** `JK-90` (`91 HP`, `1,000–2,000 kg/h`) is a **candidate** only; its lower `900–1,000 kg/h` end fails the `≥1.471 TPH` arithmetic (`≥1.60 TPH` RFQ target). Twin presses require witnessed sustained local hardwood tests.

## 3. Wood preparation, chippers, veneer chippers and hammer mills

### 3.1 Three separate wood-chipper model series across JKMT pages & brochure

| Source | Model | Power (HP) | Capacity | Max Log Ø / Length | Moisture & Output claims |
|---|---|---:|---:|---|---|
| [Current Wood Chipper](https://jaykhodiyar.com/wood-chipper/) / [Chipper Machine](https://jaykhodiyar.com/wood-chipper-machine/) | **SH-50** | 50 | 1–1.2 TPH | ≤50 mm / 300–3,000 mm | 25–50% moisture; `≤15 mm` customizable; hydraulic feed rollers + belt |
| Current OEM site | **WC-75** | 89 | 2–3 TPH | ≤300 mm / 300–3,000 mm | Same family (`25–50%`, `≤15 mm`); `24×7` claim |
| Current OEM site | **WC-100** | 114 | 3–4 TPH | ≤400 mm / 300–3,000 mm | Same family (`25–50%`, `≤15 mm`); legacy `/product/wood-chipper-5tph/` redirects here |
| [Legacy Wood Chippers](https://jaykhodiyar.com/jay-khodiyar-wood-chippers-machine/) | **JKWC75 / JKWC100 / JKWC150** | 85 / 110 / 170 | ≤2 / ≤3 / ≤5 TPH | Not tabulated | Prose claims turning logs/wet wood into dust/chips |
| **Brochure PDF (pp. 11 & 13)** | **JKCM75 / JKCM100 / JKCM150** | **89 / 114 / 176** | ≤2 / ≤3 / ≤5 TPH | Brochure p. 6 cites chips up to `20 mm` | Brochure p. 11 labels these `Wood chipper Machine`, p. 13 repeats identical table under `Hammer Chipper grinder`! |
| **Brochure PDF (p. 12)** | **Chipper grinder (50 HP)** | 50 | ≤2 TPH | ≤50 mm Ø × ≤500 mm L | Input moisture **`Up to 30%`**; output `≤20 mm` (wood chips & agro waste) |

**Critical finding:** The `5 TPH` class (`JKWC150` `170 HP` / `JKCM150` `176 HP`) no longer appears on `/wood-chipper/` (where `/product/wood-chipper-5tph/` redirects to `WC-100` capping at `3–4 TPH`). Even at `5 TPH`, nominal output falls below `5.57 wet TPH` (50% moisture) and offers narrow margin over `4.64 wet TPH` (40% moisture). Further, `≤15–20 mm` chips cannot feed fine turbo/flash dryers (`≤3×10 mm` or `<8 mm`) without secondary size reduction.

### 3.2 Veneer chippers / crushers (4 models — new catalogue evidence)

Sources: [Veneer Chipper](https://jaykhodiyar.com/veneer-chipper/), [Veneer Chipper Machine](https://jaykhodiyar.com/veneer-chipper-machine/), [Veneer Crusher Machine](https://jaykhodiyar.com/veneer-crusher-machine/). High-speed drum chipper for plywood/veneer waste (`5 mm T × ≤300 mm W` sheets or `25×25×35 mm` chips), **input moisture `Up to 35%`**, output `Up to 16 mm (Customized)`, belt conveyor feed/discharge:
- **VC-30** (`30 HP`, max veneer `3 mm`, `1–2 TPH`) · **VC-50** (`50 HP`, `5 mm`, `2–4 TPH`) · **VC-75** (`75 HP`, `5 mm`, `4–6 TPH`) · **VC-100** (`100 HP`, `5 mm`, `6–8 TPH`). Not whole-log chippers.

### 3.3 Hammer mills (`HM-50`, `HM-75`, `HM-100` — website vs brochure conflicts)

Sources: [Hammer Mill](https://jaykhodiyar.com/hammer-mill/), [Hammer Mill Machine](https://jaykhodiyar.com/hammer-mill-machine/), [Biomass Hammer Mill](https://jaykhodiyar.com/biomass-hammer-mill/), and **Brochure p. 13**.

| Model | Power | Published capacity | Input size | Input moisture (Web vs Brochure) | Output size (Web vs Brochure) |
|---|---:|---:|---|---|---|
| **HM-50** | 60 HP | 800–1,500 kg/h | `50 × 25 × 25 mm` | **Up to 20%** vs Up to 30% (p. 13) | **Up to 8 mm** vs 2–20 mm (p. 13) |
| **HM-75** | 75 HP | 1.5–2.5 TPH | `50 × 25 × 25 mm` | Same conflict | Same conflict |
| **HM-100 (100 HP)** | 100 HP | 2.5–4 TPH | `50 × 25 × 25 mm` | Same conflict | Same conflict |
| **HM-100 (150 HP)** *(likely typo for HM-150)* | 150 HP | 4.5–6 TPH | `50 × 25 × 25 mm` | Same conflict | Same conflict |

Website prints **`HM-100`** for both the `100 HP (2.5–4 TPH)` and `150 HP (4.5–6 TPH)` rows. Integrated belt conveyor feed and pneumatic cyclone discharge described. Strictly **dry-side grinding only** (`≤20%` web moisture limit excludes 40–50% wet wood).

## 4. Drying systems (`JK-BD-2000`, `JK-BD-3000`, `JK-BD-5000`)

Sources: [Biomass Dryer Machine](https://jaykhodiyar.com/biomass-dryer-machine/), [Biomass Dryer System](https://jaykhodiyar.com/biomass-dryer-system/), [Sawdust Dryer Machine](https://jaykhodiyar.com/sawdust-dryer-machine/) (all legacy `/product/` and `/wood-powder-*` URLs redirect here), [Rotary Dryer article](https://jaykhodiyar.com/rotary-dryer-system/), **Brochure p. 10**.

| Model | Power (HP) | Published capacity (TPH) | Table 2 input moisture | Table 1 moisture across pages | Table 1 feed size | Outlet moisture |
|---|---:|---:|---|---|---|---|
| **JK-BD-2000** | 61 | 2 | Up to 40% | **35%** (Biomass Dryer) vs **45%** (Sawdust Dryer) vs **35%** (Brochure p. 10) | **Dia ≤3 mm × Length ≤10 mm** | 8–15% |
| **JK-BD-3000** | 73 | 3 | Up to 40% | Same internal conflict | **Dia ≤3 mm × Length ≤10 mm** | 8–15% |
| **JK-BD-5000** | 90 | 4 | Up to 40% | Same internal conflict | **Dia ≤3 mm × Length ≤10 mm** | 8–15% |

- **Technology & scope described:** Turbo / Flash hot-air dryer with screw/belt feeder, hot-air biomass furnace (burns briquettes, wood waste, logs), ID centrifugal blower, cyclone separator with airlock.
- **Four major technical gaps / disqualifiers without test:**
  1. **Severe moisture contradictions:** Website Table 2 cites `40%`, Table 1 cites `35%` (`Biomass Dryer`) vs `45%` (`Sawdust Dryer`), prose says `30–40%`, `30–45%`, and `30–50%`, while Brochure p. 10 states `35% to 10%`! None certifies exact `50%` inlet or matches earlier third-party references (`4000 / 91 HP / 35%` and `2000 / 62 HP / 40%`).
  2. **Very small feed size (`≤3 mm dia × 10 mm L`):** Jay Khodiyar's own wood chippers output `≤15–20 mm`, creating an unresolved pre-dryer wet-sizing bottleneck.
  3. **Zero evaporation / fuel / basis data:** `2/3/4 TPH` capacity does not state whether it is wet feed or dry product, and **kg water evaporated/hour** and **furnace fuel kg/h** are completely omitted. (And `4 TPH` wet feed at 40% falls short of `4.64 wet TPH`; at 50% it falls way short of `5.57 wet TPH`.)
  4. **Rotary dryer gap:** Generic blog articles describe rotary drum dryers, but **zero rotary dryer models, HP, or capacities** are published on the website or brochure.

## 5. Pellet mills and listed press spare parts

- **Pellet mills (outside primary briquette BOM):** Website lists vertical ring-die models **JK-VP100** (`123 HP`, `800–1,200 kg/h`), **JK-VP175** (`175 HP`, `1,500–2,000 kg/h`), **JK-VP225** (`225 HP`, `2,000–3,000 kg/h`), `8–10 mm`, `8–12%` moisture, `≤2 mm` feed ([Pellet page](https://jaykhodiyar.com/vertical-ring-die-pellet-machine/)). Brochure p. 14 lists **JK7560P** (`136.5 kW` sum, `1,500–2,000 kg/h`), **JK7700P** (`165.5 kW` sum, `2,000–2,500 kg/h`), **JK7850P** (`227.5/257.5 kW` sum, `2,500–4,000 kg/h`), `6/8/10 mm`, `≤15%` moisture. Do not mix pellet equipment into briquette budgets.
- **Press spare parts ([Spares page](https://jaykhodiyar.com/spare-parts-of-briquette-machine/)):** Lists 16 components (*Ram/Rem Punch, Screw Worm, Oil Seal, Main Belt, Crank Shaft, Taper Die, Feeder Box, Allen/L&Key Bolt, Die Holder, Brass Bush/Bus-Brass, Split Die, Collet Flange, Oil Pipe, Screw Worm Coupler, Piston, Collet Ring, Ram Holder, Oil System Parts, Main Stud, Gudgeon/Gajan Pin*) with zero part numbers, steel grades, wear-life hours, or prices.

## 6. Price and commercial evidence

- **Zero factory or brochure prices:** Neither `jaykhodiyar.com` nor the 20-page brochure PDF discloses equipment, package, or spare-part prices.
- **Existing unresolved third-party asks ([price ledger](../2026-11-22-LIVE-MACHINERY-PRICE-EVIDENCE.md)):** TradeIndia `₹5.00L` (labelled hydraulic, 90 mm), `₹8.00L` (mixed 10–90 mm), and `BRQ-9075` (`Get Latest Price`) remain unverified third-party directory entries of unknown scope. **Do not budget or contract from them.** Owner ₹52L twin-press baseline remains unchanged.

## 7. Internal project-fit screening — never disclose

For 1,000 MT/month over 340 productive hours (`≥4.64 / 5.57 wet TPH`, `1,563 / 2,492 kg/h` water evaporation, `~3.08 dry TPH`, `2.941` combined / `≥1.60 TPH` per press target):
- `JK-90` (`91 HP`, `1,000–2,000 kg/h` web / `900–2,000 ±10%` brochure) spans below and above target; requires two presses plus witnessed sustained hardwood verification (motor breakdown, RPM, loaded strokes/min, wear rate).
- `WC-100` (`114 HP`, `3–4 TPH`) is undersized as a single chipper for `4.64 / 5.57 wet TPH`; discontinued/hidden `JKWC150 / JKCM150` (`5 TPH`, `170/176 HP`) must be confirmed as available, wet-hardwood-rated, and reconciled with dryer feed size (`≤3×10 mm` on `JK-BD`!).
- `JK-BD-5000` (`90 HP`, `4 TPH`, conflicting `35%/40%/45%` moisture) lacks evaporation ratings and cannot cover `5.57 wet TPH` at `50%` moisture (nor `4.64 wet TPH` at `40%` if capacity is wet input). No rotary dryer models published.

## 8. What to obtain directly from Jay Khodiyar

| ID | Deliverable | Status |
|---|---|---|
| J01 | Dated Ex-Works & delivered/installed price list for `JK-65/75/90`, chippers, hammer mills, `JK-BD` dryers & spares | Pending |
| J02 | Reconcile `JK-65/75/90` website vs brochure capacities, `5–10%` vs `8–12%` moisture, `300` vs `450 mm` length, and Brochure `90MM` typo on JK-65 | Pending |
| J03 | Press motor-by-motor HP breakdown, weight, cooling-track scope, flywheel RPM, **loaded physical strokes/min**, stroke length & lubrication specs | Pending |
| J04 | Written continuous-duty vs mandatory rest, oil/filter schedule, wear-part metallurgy, life (hours/tonnes) & part-numbered spare prices (16 listed parts) | Pending |
| J05 | Reconcile TradeIndia `₹5L hydraulic` / `₹8L mixed-size` / `BRQ-9075` listings vs genuine mechanical `JK-90` package | Pending |
| J06 | Wood chipper lineup status: `SH-50/WC-75/WC-100` vs `JKWC75/100/150` vs `JKCM75/100/150` (`170` vs `176 HP`), 5 TPH availability, rotor RPM, knife life & wet hardwood sieve curve | Pending |
| J07 | Reconcile `HM-100` duplicate (`100 HP` vs `150 HP`), `≤20%` web vs `≤30%` brochure moisture, `≤8 mm` vs `2–20 mm` output, wet-milling exclusion & motor schedules | Pending |
| J08 | Veneer chippers (`VC-30/50/75/100`): confirm whole-wood non-suitability and any overlap with wood-chip/branch sizing | Pending |
| J09 | Reconcile `JK-BD-2000/3000/5000` (vs earlier `4000/2000` names), `35%/40%/45%/50%` moisture limits, `≤3×10 mm` size limit, wet-vs-dry TPH basis, **evaporation kg/h**, fuel kg/h & furnace BOM | Pending |
| J10 | Confirm availability, sizes, HP & evaporation ratings of Rotary Drum Dryers (described in blog prose, absent from tables) | Pending |
| J11 | Reconcile `JK-VP100/175/225` vs `JK7560P/7700P/7850P` pellet mills (separate optional comparison only) | Pending |
| J12 | Integrated standard-line BOM (feeders, screens, cyclones, baghouse/spark safety, conveyors, MCC/PLC), layout & motor load SLD | Pending |
| J13 | Measured local hardwood (`Eucalyptus`, `Casuarina`, `Subabul`) output, rejects, density, kWh/t & mass balance per tonne | Pending |
| J14 | Restore/clarify `/after-sales/` link (infinite redirect loop); confirm AP/Telangana service engineer SLA, commissioning warranty & FAT/SAT remedies | Pending |
| J15 | Model-specific manuals, electrical SLDs, test reports & consented South India operating wood-plant references | Pending |

## 9. Review gate

Complete public website (`sitemap_index.xml` / 198 URLs, all live product/redirect/support pages) and 20-page official brochure PDF audit finished for Jay Khodiyar Machine Tools (**27 master records**). Zero verified factory prices, zero loaded BPM/stroke measurements, and zero evaporation/fuel curves are published. Use [updated Jay Khodiyar draft](../SUPPLIER-ENQUIRIES/04-JAY-KHODIYAR.md) for outreach (do not send this dossier). **Next manufacturer in sequential public research: Radhe Industrial Corporation (RICO).** No outreach sent.
