# Factory inspection photo evidence — AKASHYA ENTERPRISES
**Audit: 22 Nov 2026.** The nine photographs were taken at the same reference briquette factory. These are **field observations**, not a manufacturer performance certificate or a measurement survey.

| Photo | Directly visible | Interpretation requiring verification |
|---|---|---|
| [01: dryer/cyclone/MCC](../FACTORY-PHOTOS/01-drying-tower-cyclone-mcc-panel.jpg) | Tall vessels, ducts and electrical control panel | Cyclone/drying system likely; exact configuration, safe emissions and evaporation rate unknown |
| [02: factory wide shot](../FACTORY-PHOTOS/02-factory-interior-briquette-heap.jpg) | Covered shed, finished briquette heap, two reddish press structures | Two mechanical piston presses likely; press model, rated tonnage and availability not visible |
| [03: EcoStan close-up](../FACTORY-PHOTOS/03-ecostan-wood-chipper-close.jpg) | Yellow EcoStan-branded machine and log/branch feed | Model *not read* from nameplate; cannot claim ESM100/150 directly |
| [04: raw wood](../FACTORY-PHOTOS/04-raw-wood-logs-yard-chipper.jpg) | Mixed logs/branches beside machine | Species, legal source, diameter spread, received moisture and delivered wet-MT price need documents |
| [05: press/flywheel](../FACTORY-PHOTOS/05-mechanical-piston-press-flywheel.jpg) | Mechanical drive/flywheel and steep material feeder | Stroke rate, force, die temperature, wear life not measurable from photo |
| [06: belt transfer](../FACTORY-PHOTOS/06-inclined-conveyor-sawdust-discharge.jpg) | Inclined conveyor and wood particles | Actual belt capacity, metal separation and blockage monitoring unknown |
| [07: loader and dust](../FACTORY-PHOTOS/07-tractor-loader-sawdust-handling.jpg) | Tractor loader and airborne dust | Existence/performance of dust fire protection unverified; replication must improve on visible dust |
| [08: U-ducts](../FACTORY-PHOTOS/08-pneumatic-flash-dryer-u-tubes.jpg) | Tall U-shaped ducts, cyclonic equipment | Consistent with pneumatic flash separation; no proof that rotary drum dryer is present |
| [09: briquettes](../FACTORY-PHOTOS/09-90mm-finished-briquettes-cooling-track.jpg) | Brown cylindrical briquettes, some cracked/ridged | Diameter **appears ~90mm** but requires caliper; no GCV, ash, moisture or compression measurement |

## Reference plant visual hardware mapping
From the promoter's inspection photographs of the benchmark operating facility, nine primary hardware subsystems are identified and mapped into the proposed commercial plant layout:

| Observed factory equipment | Visual description in reference photos | Functional purpose in production line |
| :--- | :--- | :--- |
| **EcoStan wood-processing machine** | Yellow machine receiving logs and branches | Primary size reduction: converts incoming timber logs into coarse wood particles |
| **Log feeding conveyor** | Yellow-and-black heavy-duty conveyor | Transports raw logs and cut timber into the primary chipper infeed chute |
| **Sawdust transfer conveyors** | Inclined belt/screw conveyors inside factory | Moves chipped wood particles to drying columns and dry storage bins |
| **Two mechanical briquette presses** | Two large reddish machines in the wide factory photograph | Compresses prepared wood particles into dense cylindrical biomass briquettes |
| **Large drive flywheel** | Prominent flywheel visible on at least one mechanical press | Stores rotational kinetic energy to deliver high-force mechanical compaction strokes |
| **Drying / air-handling arrangement** | Vertical columns, U-ducts, and hot air handling | Removes moisture from wet wood particles using hot furnace gases |
| **Cyclone separation equipment** | Tall conical vessels and connected duct piping | Separates dried wood dust from humid exhaust airstream using cyclonic vortex |
| **Electrical control panels** | Multiple industrial floor-mounted cabinets (MCC) | Houses motor starters, VFDs, safety interlocks, and thermal monitoring |
| **Material handling equipment** | Tractor loader moving bulk sawdust piles | Transports bulk wood chips/sawdust from receiving yard into plant hopper |
| **Finished cylindrical briquettes** | Large piles of brown compressed cylindrical blocks | Saleable 90 mm biomass fuel for industrial boiler and furnace offtakers |

---

## Manufacturing process flow

```
[Raw Timber Logs & Branches]
             │
             ▼
[Log Receiving Conveyor]
             │
             ▼
[EcoStan Wood-to-Sawdust Machine] ──► Converts logs into small particles (2–10 mm)
             │
             ▼
[Sawdust Collection & Transfer Conveyors]
             │
             ▼
[Drying, Cyclone Separation & Dust Handling] ──► Reduces moisture from 40–50% to 8–12%
             │
             ▼
[Dried Sawdust Screening / Hammer Mill] ──► Ensures uniform particle size (≤15×8 mm)
             │
             ▼
[Dried Sawdust Distribution Bunker]
             │
      ┌──────┴──────┐
      ▼             ▼
[Briquette Press 1] [Briquette Press 2] ──► Twin mechanical piston presses (90 mm)
      │             │
      └──────┬──────┘
             ▼
[Cooling Tracks & Conveyors] ──► Cools and stabilizes hot briquettes to ambient
             │
             ▼
[Finished Cylindrical Briquette Storage & Weighbridge Dispatch]
```

---

## Equipment capacity & purpose specification matrix

| Equipment package | Required capacity / specification | Functional purpose & engineering battery limit |
| :--- | :--- | :--- |
| **Log receiving conveyor** | **$\ge 6.0\text{ wet TPH}$** heavy-duty belt/apron conveyor | Continuous feeding of raw logs, branches, and cut timber into primary chipper |
| **Wood-to-sawdust machine** | **$\ge 5.0\text{--}6.0\text{ wet TPH}$** (EcoStan ESM150 / Jay Khodiyar 5TPH) | Cuts and shreds raw timber logs ($\le 12$ inches) into small wood particles |
| **Dryer with heating system** | **$\ge 1,800\text{--}2,000\text{ kg/h}$** water evaporation (40% baseline)<br>*(Stressed to 2,492 kg/h at 50% moisture)* | Reduces excess moisture from wet wood ($40\text{--}50\%$) down to press-ready $8\text{--}12\%$ |
| **Screening / hammer mill** | **$3.0\text{--}4.0\text{ dry TPH}$** (EcoStan HM150, post-dryer) | Controls final particle size ($\le 15\times 8\text{ mm}$) and screens out tramp debris |
| **Briquette presses (twin)** | **$\ge 1.471\text{ TPH}$ per press** sustained (total $\ge 2.941\text{ TPH}$) | High-pressure mechanical piston compaction into 90 mm solid cylindrical briquettes |
| **Cooling conveyor / tracks** | Match press output ($2.94\text{ TPH}$), dual 30–40 ft lines | Dissipates compression heat, cools briquettes to ambient, and prevents breakage |
| **Cyclone & dust filters** | $15,000\text{--}25,000\text{ CFM}$ pulse-jet baghouse + cyclones | Collects fugitive wood dust, ensures environmental compliance, and isolates explosion risk |
| **Electrical control panels** | 630 kVA HT substation + centralized MCC / PLC | Distributes power, manages motor starters/VFDs, emergency stops, and automation interlocks |
| **Loader & weighbridge** | 1.5–2T loader + 50–60 MT pitless electronic scale | Inbound timber weighing, log yard manipulation, and outbound finished product dispatch |

---

## Evidence hierarchy
- **Observed:** wood logs, chipper, conveyors, visible dust, ducts/cyclones, heavy press drive and finished cylindrical briquettes.
- **Plausible but unproven:** 90mm product, two operating briquetting lines, pneumatic multi-pass flash drying, EcoStan ESM family.
- **Not observable:** 1,000 MT/month actual output, safe press continuous hours, 220–240 ram strokes/min, 1,200–1,500 kg/cm² pressure, binding temperature, annual maintenance, mineral ash, GCV, legally sourced wood and commercial cost.
- **Do not duplicate hazardous practice:** open dust clouds around mobile loaders can present combustible-dust/explosion risks. Design protected bins/conveyors, extraction and safe electrical separation with a competent specialist.

## Field data missing from reference factory
Obtain photo of press and chipper nameplates; live kW and kWh readings; dryer fuel inlet and gas handling; wet-wood to output mass balance; 16h actual shift register; product caliper; supplier quotes and spares record. Only documented results should enter the financial baseline.

For proposed plant engineering, see [BPM & hours](04-BPM-Operating-Hours-and-Live-Machinery-Pricing.md) and [RFQ register](../PROCUREMENT/2026-11-22-MACHINERY-PRICE-AND-RFQ-REGISTER.md).
