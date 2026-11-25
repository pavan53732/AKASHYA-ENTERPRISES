# Radhe Industrial Corporation (RICO) — manufacturer-specific technical investigation

**INTERNAL ONLY — 25 November 2026.** Sequential public-source review: full official website (`radheindcorp.com`, `wp-sitemap.xml` / 59 discovered URLs, 56 live pages including portfolio/product pages, WooCommerce `/shop/` storefront and all category/policy/company pages) AND official 4-page downloadable PDF brochure ([67d545e7c2486.pdf](https://radheindcorp.com/wp-content/uploads/2025/04/67d545e7c2486.pdf)) examined. **New finding:** RICO operates an active WooCommerce `/shop/` publishing direct `₹` asking prices (`₹15.50L–₹60.00L`) for 6 SKUs (`RICO-1`, `RICO-6` to `RICO-10`), whereas multi-model pages (`Rotary Drum Dryer`, `Hammer Mill Machine`, `Biomass Pellets Machine`) quote one unallocated headline price without GST, freight, exclusions, or sub-model scope. No written quotation addressed to AKASHYA ENTERPRISES; the secondary RICO catalogue adds two drum chippers; actual local hardwood tests and loaded strokes/min remain open. [Shared master](../MACHINERY-MASTER.csv) tracks **24 RICO catalogue/webshop entries** (`Jumbo 90`, `Super 70`, `Hammer 1500/3000/5000`, `Flash Air Dryer (Tornado)`, `ROTARY 3000/4000/5000/7000`, plus pellet-only comparison `Pellet 16`, `RICO 460/560A/560B/560C/700/850A/850B`, and `2 TPH Automatic Pellet Line`, plus two drum chippers and three straw shredder comparators). Do not send this file externally. [External draft](../SUPPLIER-ENQUIRIES/08-RADHE-INDUSTRIAL-CORPORATION-RICO.md).

## 1. Supplier identity, contacts and website integrity check

- **Legal entity conflict:** Official 4-page brochure PDF (pp. 1–2) names **`RADHE INDUSTRIAL CORPORATION LLP`** (*Established 1991*, *R&D centre Pioneer Fuel operational 28 years*, *1,800+ installations globally* self-reported, pellet line *launched in 2024*), whereas website pages, footer, and `/terms-conditions/` name **`Radhe Industrial Corporation`** (founder Mr. Prakash A. Patel, homepage). Group-company portfolio lists 7 entities (*Pausons Food, Pioneer Fuel Industries, Radhe Equipments India, Radhe Hi-tech Engineering, Radhe Polymers Industries, White Field Spintex Pvt Ltd, White Gold Bio Energy*); five pages repeat identical *"hydraulic biomass briquette machine"* boilerplate text. Verify exact legal seller name and GSTIN before any RFQ/PO.
- **Address:** Plot No. 122–123, Vavdi Survey No. 43, Gondal Road Circle, 150 Ft. Ring Road, Behind Perfect True Value Showroom, Rajkot – 360004, Gujarat, India.
- **Verified public contacts:**
  - **Sales & Customer Success (`/contact-us/`, `/contact-us-2/`, Brochure p. 1):** `info@radheindcorp.com`, `+91 98252 22072`, `+91 99798 52250`, Toll Free `1800 300 21222`, Telephone `+91 281 2373700 / +91 281 2373750` (note `/all-products/` footer link contains typo `tel:919825202272`; `/refund_returns/` also lists `+91 89808 55255`).
  - **Technical Support (`/contact-us/` & `/contact-us-2/`):** `support@radheindcorp.com`, `+91 99099 23243` (Weekdays **10:00 AM–6:00 PM IST**).
- **Facilities, warranty & website audit (25 Nov 2026):**
  - `/infrastructure/` claims in-house Assembly, Boring, CNC-VMC, Fabrication, Machining, Testing, VTL Machining, and Wear & Tear Parts Store (third-party verification absent).
  - `/our-certifications/` states **`Coming soon...`** — zero ISO/CE/test certificates published.
  - `/contact-us/` states a **12-month warranty** on materials/workmanship; `/refund_returns/` states **"We are not accepting Refund"**; `/services/` claims **"24/7"** maintenance/repair availability, conflicting with `/contact-us/` weekday **10:00 AM–6:00 PM IST** support hours.
  - Homepage HTML `.w-counter` displays `1 Years of Experience / 1 Total Installations / 1 Customers Globally` (frontend JS counter bug) alongside `34+ Years` prose; test pages `/test/` and `/test-2/` remain live in the sitemap; YouTube handle linked is `@radhepelletmachine`.

## 2. Mechanical briquetting presses (`Jumbo 90`, `Super 70`)

Sources: [Jumbo 90 product](https://radheindcorp.com/product/jumbo-90/), [Jumbo 90 shop](https://radheindcorp.com/shop/jumbo-90/), [Super 70 product](https://radheindcorp.com/product/super-70/), [Super 70 shop](https://radheindcorp.com/shop/super-70/). Neither press appears in the 4-page 2024/2025 PDF brochure (which covers biomass pellets only).

| Parameter | **Jumbo 90** (`SKU: RICO-1`) | **Super 70** (`SKU: RICO-6`) | Discrepancy / verification note |
|---|---|---|---|
| **Published output** | `1,500 kg/h ±20%` (`1,200–1,800 kg/h`) prose; `1,500* kg/h` table | `750 kg/h ±20%` (`600–900 kg/h`) prose; `750* kg/h` table | Footnote `*` is undefined on both pages; material-dependent envelope, not guaranteed hardwood output |
| **Motor HP breakdown** | **91 HP** (`75` main + `10` feeding cuppy + `3` screw conveyor + `3` lubrication) | **49 HP** prose vs **50 HP** table (`40` main + `5` feeder + `3` screw + `2` lube) | 49 vs 50 HP internal mismatch on Super 70; motor make, kW/IE efficiency, and RPM omitted |
| **Amp & kWh/MT claim** | `80–100 A`; `35–40 Units (kWh) / MT` | `40–65 A`; `35–40 Units (kWh) / MT` | Manufacturer claims only; not metered hardwood data |
| **Machine RPM & stroke** | `240 RPM`; `200 mm stroke` | `240 RPM`; `200 mm stroke` | **240 RPM is flywheel/machine speed, NOT proven loaded ram strokes/min** |
| **Feed size & moisture** | `≤25 mm`; `12%` max moisture | `≤10 mm` prose vs `≤25 mm` table; `12%` max | Internal feed-size contradiction on Super 70; `≤25 mm` wood feeding without fines check unverified |
| **Briquette size** | `90 mm` Ø; `150–400 mm` prose vs `~1 ft (~305 mm)` table | `70 mm` Ø; `150–400 mm` prose vs `~1 ft` table | Length inconsistency across prose vs spec table |
| **Foundation / Room / Area** | Foundation `16×5 ft`; Room `25×15 ft`; Area `1,000 m³` | Foundation `16×5 ft`; **Room `12×4 ft`**; Area `500 m³` | **Physical impossibility on Super 70:** `12×4 ft` room (`48 sq ft`) is smaller than its `16×5 ft` foundation (`80 sq ft`)! Both pages cite project area in `m³` volume instead of `m²`/`sq ft` |
| **Webshop asking price** | **`₹22,00,000.00` (`₹22.00L`)** | **`₹15,50,000.00` (`₹15.50L`)** | `PUBLIC ASKING PRICE` (`SKU: RICO-1 / RICO-6`). GST, cooling conveyor, panel, freight, installation & spares exclusions unstated |

- **Additional press gaps:** `Jumbo 90` prose claims *"ability to grind and mix any type of raw material"* (physically false for a briquetting press). Zero published data on total weight, cooling-track length, oil grade/change hours, die/punch metallurgy or life, continuous-duty cooling stops, or spare-part numbers/prices.

## 3. Wood preparation and hammer mills (`Hammer 1500 / 3000 / 5000`)

- **Drum chippers found on the secondary RICO catalogue:** [RICO-DWC-30 and DWC-60](https://radherico.com/product/drum-wood-chipper) are listed at up to 3 and 6 TPH, maximum log Ø200 and Ø300 mm, and 70 kW/95 HP and 130 kW/175 HP, respectively. OEM states ±20% depending on material. The page names Radhe Industrial Corporation LLP and matches the address and published sales phones on [the earlier site](https://radheindcorp.com/contact-us/). Confirm seller/GSTIN, chip size and actual wet wood duty. The [same catalogue](https://radherico.com/product/dual-shaft-shredder-machine) lists SH-200/300/500 for straw square bales at <15% moisture, outside the two wet wood cases.
- **Hammer mill range ([Hammer Mill](https://radheindcorp.com/product/hammer-mill-machine/), [Shop `SKU: RICO-10`](https://radheindcorp.com/shop/hammer-mill-machine/), Brochure p. 2):**
  - Models: **`Hammer 1500`** (`1,500 kg/h`), **`Hammer 3000`** (`3,000 kg/h`), **`Hammer 5000`** (`5,000 kg/h`).
  - Input size: **`Max 100 mm length / 20 mm diameter`** (cannot accept whole round logs >20 mm diameter); output size: **`1–15 mm` adjustable** semi-powdery/powdery. Features described: heavy-duty MOC, automatic load sensing/feed control, big-stone removal, and post-cyclone dust collector.
  - **Missing technical specs:** **Zero motor HP/kW** published, **zero rotor RPM**, **zero maximum inlet moisture limit** (critical: cannot assume wet `40–50%` duty without testing, as comparable hammer mills are dry-side `≤15–20%`), and **zero screen/hammer wear life or sieve curves**.
  - **Webshop price ambiguity:** `/shop/hammer-mill-machine/` (`SKU: RICO-10`) displays one price **`₹15,50,000.00` (`₹15.50L`)** without stating which model (`1500`, `3000`, or `5000`) or which auxiliaries (stone separator, cyclone, baghouse, feeder) are included.

## 4. Drying systems (`Tornado` Flash & `ROTARY 3000 / 4000 / 5000 / 7000`)

Sources: [Flash Air Dryer (Tornado)](https://radheindcorp.com/product/flash-air-dryer-tornado/), [Shop Tornado](https://radheindcorp.com/shop/flash-air-dryer-tornado/), [Rotary Drum Dryer](https://radheindcorp.com/product/rotary-drum-dryer/), [Shop Rotary](https://radheindcorp.com/shop/rotary-drum-dryer/). Dryers do not appear in the 4-page pellet brochure.

| Series / Models | Published capacity & moisture | Listed motors & footprint | Scopes & fuel | Webshop price & critical gaps |
|---|---|---|---|---|
| **Flash Air Dryer (Tornado)** (`SKU: RICO-8`) | **Up to `1,500 kg/h`** output (`30%` max inlet → `10%` outlet); **up to `450 kg/h` water evaporation** *(separate ceilings; `1.5 TPH` at `30→10%` implies `428.6 kg/h`)* | Blower `25 HP` + Airlock `1 HP` + Screw `3 HP` = **`29 HP` listed**; footprint **`~20×15×20 ft`** | Suction hot-air flash; VFD feeder controlled by cyclone outlet temp; servo fresh-air valve; solid coal/briquettes/firewood furnace; dust collector | **`₹18,50,000.00` (`₹18.50L`)**. Max `30%` moisture excludes `40–50%` green wood; `450 kg/h` evaporation is ~18–29% of AKASHYA need; input particle size, fuel `kg/h`, and GST/furnace/baghouse scope unverified |
| **ROTARY 3000 / 4000 / 5000 / 7000** (`SKU: RICO-9`) | *"Output drying capacity"*: **`3,000 / 4,000 / 5,000 / 7,000 kg/h`**; **max `50%` inlet**, **`10%` target outlet** | **No motor HP/kW** published; **no drum dimensions** published | Suction hot-air rotary drum; hot-air generator, **twin spark cyclones**, RAVs, heavy-duty blower, **3 multi-cyclones** (ash), **wet scrubber** in chimney; briquette/firewood/coal fuel | **`₹60,00,000.00` (`₹60.00L`)** listed under one generic SKU **`RICO-9`** without identifying which of the 4 sizes (`3000–7000`) it prices! **Zero evaporation `kg/h`**, zero fuel `kg/h`, zero inlet particle size, zero simultaneous `50%→10%` proof |

## 5. Pellet mills, copy-paste `Pellet 16` anomaly & uncoded brochure ancillaries

- **Copy-paste `Pellet 16` anomaly on [Biomass Pellets Machine (`RICO 560`)](https://radheindcorp.com/product/biomass-pellets-machine/):** Page title is `RICO 560`, yet the opening three paragraphs describe **"The Pellet 16"** with **`200 mm stroke`**, **`1,100 kg/h ±20%`**, **`240 RPM`**, **`~91 HP`**, **`16 mm` Ø × `10–100 mm`**, and **`≤6 mm` feed** (clearly adapted from the mechanical Jumbo 90 piston press!), followed by specs for **`6/8/10 mm`** vertical ring-die pellet mills (`≤6 mm` web vs `≤8 mm` Brochure p. 4, `<12%` moisture) and a 7-model table (`06 to 12 mm` pellets): **`RICO 460`** (`55 kW/74 HP`, `0.6–0.8 TPH`), **`RICO 560 A`** (`90/121`, `1.2–1.5`), **`RICO 560 B`** (`110/148`, `1.4–1.7`), **`RICO 560 C`** (`132/177`, `1.7–2.5`), **`RICO 700`** (`160/215`, `2.5–3.0`), **`RICO 850 A`** (`220/295`, `2.5–3.5`), **`RICO 850 B`** (`250/335`, `4.0–5.0`), dimensions `1700×1000×1580` to `2630×1300×2200 mm`. Shop listing (`SKU: RICO-7`, **`₹22,00,000.00`**) does not state which model/variant it prices.
- **[Fully Automatic Biomass Pellet Production Line](https://radheindcorp.com/product/fully-automatic-biomass-pellet-production-line/):** `2 TPH` customizable line, `190–225 kW`, `≤15%` input moisture (dryer extra), `6–12 mm`, PLC control, `2,200 sq ft (100×22×18 ft)`, `1.1–1.3 g/cm³`, counter-flow cooler, cyclone/pulse-jet filter, `50 kg / 750 kg` packing, `1 operator + 1 loader + 2 labour/shift`, 1-year warranty. Kept strictly separate as **pellet-only** comparison.
- **Brochure pp. 2–3 uncoded ancillaries (pellet context):** `Automatic Feeder Machine`, `Pellet Screener` (vibro motor), and `Pellet Cooler With Packing Unit` (jumbo bags) have zero published model codes, dimensions, throughput ratings, or motor HP.

## 6. Price and commercial evidence

- **Six live WooCommerce webshop asking prices (`/shop/` & `/all-products/`, observed 25 Nov 2026 — `PUBLIC ASKING PRICE`, NOT binding quotes):** `JUMBO 90` (`RICO-1`) **`₹22.00L`**, `SUPER 70` (`RICO-6`) **`₹15.50L`**, `Biomass Pellets Machine` (`RICO-7`) **`₹22.00L`** *(model unspecified)*, `Flash Air Dryer (Tornado)` (`RICO-8`) **`₹18.50L`**, `Rotary Drum Dryer` (`RICO-9`) **`₹60.00L`** *(capacity 3000–7000 unspecified)*, `Hammer Mill Machine` (`RICO-10`) **`₹15.50L`** *(capacity 1500–5000 unspecified)*.
- All six omit GST (`18%`?), HSN, freight to Anakapalli, unloading/installation, cooling tracks, foundation bolts, panels/cables, spares, and validity; `/refund_returns/` states no refunds. Owner's `₹52L` twin-press / `₹520L` fixed CAPEX allowances remain unchanged.

## 7. Internal project-fit screening — never disclose

For 1,000 MT/month over 340 productive hours (`≥4.64 / 5.57 wet TPH`, `1,563 / 2,492 kg/h` water evaporation, `~3.08 dry TPH`, `2.941` combined / `≥1.60 TPH` per press target):
- **Presses (`Jumbo 90` at `₹22.00L` web ask):** `1,500 kg/h ±20%` implies `1,200–1,800 kg/h` depending on material; the `1,200 kg/h` lower end fails `1.471 / 1.60 TPH` per press, and `1,500` nominal leaves only 2% theoretical headroom. Twin presses (`₹44.00L` ex-GST/ex-scope before cooling/freight) require witnessed hardwood output `≥1.60 TPH` each and verified loaded BPM.
- **Whole-log preparation:** DWC-60 is a trial lead for the coarse-chip route. A 20% downward sensitivity gives 4.8 TPH, short of the 5.57 wet TPH case. Confirm screen/cutter output and companion dryer before ranking. Hammer 1500–5000 receive pre-sized material only in the reviewed catalogue.
- **Dryers (`ROTARY 3000–7000` vs `Tornado`):** `Tornado` (`30%` max, `450 kg/h` evaporation, `₹18.50L`) is disqualified for `40–50%` green wood. `ROTARY 3000` (`3 TPH` dry target at `50→10%` requires `~5.4 wet TPH` & `~2.4 TPH` evaporation before losses, borderline at `~3.08 TPH` dry line duty) and `ROTARY 4000/5000` (`≤50%` inlet claim) could cover `40–50%` if proven, **only** after RICO states which model `₹60.00L` represents and supplies **evaporation kg/h, motor HP, fuel kg/h, and particle-size tolerances**.

## 8. What to obtain directly from RICO

| ID | Deliverable | Status |
|---|---|---|
| R01 | Exact legal seller name (`Radhe Industrial Corporation` vs `LLP`), GSTIN, ISO/CE certs (`/our-certifications/` blank) & written letterhead offer | Pending |
| R02 | Reconcile all 6 `/shop/` WooCommerce prices (`RICO-1 ₹22L`, `RICO-6 ₹15.5L`, `RICO-7 ₹22L`, `RICO-8 ₹18.5L`, `RICO-9 ₹60L`, `RICO-10 ₹15.5L`) — exact model covered, GST, included auxiliaries, freight & exclusions | Pending |
| R03 | `Jumbo 90` & `Super 70` motor make/kW/efficiency, flywheel RPM vs **loaded physical piston strokes/min**, stroke, weight, cooling-track length, lube & stops | Pending |
| R04 | Reconcile `Jumbo 90` undefined `*`, `150–400` vs `~1 ft` length, *"grind & mix"* claim, and `Super 70` `49/50 HP`, `10/25 mm` & **`16×5 ft` foundation vs `12×4 ft` room** | Pending |
| R05 | Confirm DWC-30/60 OEM scope, log length, wet hardwood capacity, chip cut, drive split, knife schedule, model prices and availability of a direct log-to-sawdust machine | Pending |
| R06 | `Hammer 1500/3000/5000` motor HP/kW, rotor RPM, **maximum wet moisture ceiling**, fine-screen TPH/kWh/t (`≤6–8 mm` vs `1–15 mm`) & stone/dust scope | Pending |
| R07 | `ROTARY 3000/4000/5000/7000` **motor schedule**, drum dimensions, wet-vs-dry basis, **water evaporation kg/h** at `30/40/45/50%`, fuel kg/h & scrubber/spark BOM | Pending |
| R08 | `Flash Air Dryer (Tornado)` furnace/cyclone/baghouse/panel scope within `₹18.50L`, inlet particle-size limit, fuel kg/h & max moisture limit | Pending |
| R09 | Reconcile `Pellet 16` (`91 HP / 200 mm / 16 mm`) copy on `RICO 560` page & `RICO 460–850 B` / `2 TPH Pellet Line` (`pellet only` comparator) | Pending |
| R10 | Measured local hardwood (`Eucalyptus`, `Casuarina`, `Subabul`) briquette output, rejects, density, metered `kWh/t` (`35–40 kWh/t` claim vs auxiliaries) | Pending |
| R11 | Complete wear-parts list with part numbers, metallurgy, hours/tonnes life, prices & replacement time (`Wear & Tear Parts Store` unpublished) | Pending |
| R12 | Reconcile `24/7` service claim (`/services/`) vs `10:00 AM–6:00 PM` weekday support (`/contact-us/`); confirm 12-month warranty exclusions & AP SLA | Pending |
| R13 | Integrated turnkey BOM, electrical SLD (`3-phase`, starting currents, PLC/VFD) & fire/dust/explosion protections (`spark cyclones` vs baghouse vents) | Pending |
| R14 | Group-company *"hydraulic briquette"* clarification (verify purely mechanical vs hydraulic presses) & non-refundable shop terms override for industrial PO | Pending |
| R15 | O&M manuals, foundation drawings, test reports & consented South India operating wood-briquette plant references | Pending |

## 9. Review gate

Main-site and brochure audit complete. The secondary RICO catalogue adds two drum chippers and three straw shredders, for 24 master records. Six earlier webshop asks retain their evidence status. Wet-duty performance, DWC installed pricing and final process fit are pending. See the [cross-supplier comparison](../../MACHINERY/06-PRIMARY-WOOD-PREPARATION-COMPARISON.md).
