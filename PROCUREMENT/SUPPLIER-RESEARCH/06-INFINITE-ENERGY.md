# Infinite Energy Pvt Ltd (`Infinite Dryer`) — manufacturer-specific technical investigation

**INTERNAL ONLY — 25 November 2026.** Sequential public-source review (supplier **6 of 6**, dryer specialist): full official website (`www.infinitedryer.com`, all 15 non-image HTML pages including `ifd.html`, `rfd.html`, `isd.html`, `technology.html`, `about-us.html`, `faqs.html`, `flash-dryer-blog.html`, `flash-dryer-rotary.html`, `pp.html`, `tc.html`) AND complete IndiaMART TrustSEAL mini-site (`www.infinitedryer.in`, all 22 HTML pages including `sitemap.html`, `profile.html`, `quality.html`, `testimonial.html`, `photos.html` and 14 product-category pages; **zero downloadable PDFs** linked on either domain) audited. **No written quotation addressed to AKASHYA ENTERPRISES; zero `infinitedryer.com` catalogue prices published** (`₹12.00L–₹99.00L` asks exist exclusively on `infinitedryer.in` storefront listings loaded with copy-paste model/capacity/moisture errors and unconfirmed exclusions). **`infinitedryer.com` contains restroom hand-dryer template copy on `/about-us.html` and `/faqs.html`**, and **`RFD` feed particle-size ceilings conflict three ways (`<12 mm` vs `<15 mm` vs `<16 mm`)**. [Shared master](../MACHINERY-MASTER.csv) tracks **26 Infinite Energy records** (**14** existing `IFD750–10000` & `RFD750–10000` updated, **4** newly documented `ISD750–6000` comparator units, plus **8** distinct priced/unreconciled `infinitedryer.in` storefront & gasifier comparator records). Do not send this file externally. [External draft](../SUPPLIER-ENQUIRIES/07-INFINITE-ENERGY-DRYER.md).

## 1. Supplier identity, contacts and website integrity check

- **Legal entity & brand:** **Infinite Energy Private Limited (`IEPL` / brand `Infinite Dryer`)**. Registered GSTIN **`06AABCI4249M1ZD`** (GST Reg. `01-07-2017`), CIN **`U29299DL2005PTC140055`** (Delhi MCA incorporation in **2005**), IEC **`0507050118`**, TAN `DELI0*****`, Banker: Canara Bank, Annual Turnover `5–25 Cr`, 26–50 employees, 40–60% exports self-reported ([Profile](https://www.infinitedryer.in/profile.html)). Note conflicting age wording: `infinitedryer.in` prints *"Established in the year of 2017"* (GST migration date) while `infinitedryer.com` states *"20+ years of experience, founded by an IITian"* (aligning with 2005 CIN).
- **Leadership & partners:** **Mr. Shivanand Ramachandran** (CEO / Mentor) and **Mr. Naval Kishore Aggarwal** (GST Partner / Nashik branch contact) ([Enquiry](https://www.infinitedryer.in/enquiry.html), [Profile](https://www.infinitedryer.in/profile.html)).
- **Works & offices:**
  - Works / NIT Faridabad: **Plot No. 25/2, Opp. Peer Baba, Dabua Pali Road, NIT, Faridabad – 121001, Haryana**.
  - Branch office: **Naval Kishore Aggarwal, 212/2, Plot No. 20, Shree Neelkamal Industrial Area, Khatwad, Nashik, Maharashtra**.
  - **Registered-address mashup:** `profile.html` prints *"1107, Arunachal Building 19, Barakhamaba Road, Near Metro Station, Connaught Place,, Faridabad- 121001, Haryana, India"* (Barakhamba Road / Connaught Place is New Delhi-110001 matching the `DL2005` CIN, spliced with the Faridabad PIN).
- **Verified public contacts:** `sales@infinitedryer.com` and **`naval.infenergy@gmail.com`** (newly discovered on every `infinitedryer.com` header/footer); `+91 92120 84932`, `+91 92120 84933` (`infinitedryer.in` IndiaMART virtual number `07942672132`, `75%` response rate).
- **Quality, testing & review audit (25 Nov 2026):**
  - `quality.html` cites **ISO 9001:2008** (superseded standard; certificate number/validity unpublished) from UKAS, claims `Quality Measures / Testing Facilities: Yes` and **`Sampling Policy: Paid`** (feedstock trials are chargeable). Client list names NTPC Ltd (Dadri), Rubber Wood India (Kerala), CIAE (Bhopal), Hindustan Pencils (Jammu), Sanghvi Woods (Jammu), and food/biscuit units.
  - [TrustSEAL Testimonials](https://www.infinitedryer.in/testimonial.html): **`3.9 / 5`** across 8 users (`5×5★`, `1×4★`, `2×1★` = **25% 1-star ratings**; **Response `80%`**, **Quality `75%`**, **Delivery `50%`**). Listed product reviews include Flash Dryers (`09-Apr-23`, Cuttack), Wooden Pellet (`08-May-22`), DDGS Dryer (`28-Mar-23`), Gasifiers (`08-Jan-20`), Cat Litter (`2021`).
  - **Severe `infinitedryer.com` website contamination:** `about-us.html` and `faqs.html` carry pasted **commercial restroom hand-dryer copy** (*"Revolutionizing Hand Drying, Sustainably — public restrooms"*, *"sensor-based hand dryer system connected to the cloud... Wi-Fi... Android and iOS mobile app"*!), homepage displays generic counters (`7500 kWh / 3206 Installation / 458k Total Projects`) and a stray competitor/template name **`"Geotech redefines your relationship with energy"`**, `tc.html` leaves literal brackets **`[India/Delhi]`**, and blog articles carry future dates **`Aug 01–30, 2026`**.
  - **Does NOT sell briquetting presses:** `infinitedryer.in/briquetting-machines.html` actually lists a **`5000 kg/hr` Wood-Fired Sawdust Flash Dryer (`₹22.00L`)**, not a briquette press.

## 2. Pneumatic flash dryers (`IFD 750` to `IFD 10000`) & process architecture (`technology.html`)

Sources: [IFD Series (`ifd.html`)](https://www.infinitedryer.com/ifd.html), [Technology (`technology.html`)](https://www.infinitedryer.com/technology.html), [Blog (`flash-dryer-blog.html`)](https://www.infinitedryer.com/flash-dryer-blog.html).

### 2.1 Official `IFD` specification table & moisture/feed contradictions

| Model | Evap. `kg/h` | Dry o/p `<30%` `(kg/h)` | Dry o/p `<45%` `(kg/h)` | Dry o/p `<50%` `(kg/h)` | Fuel cap `<kg/h>` *(Note #)* | Connected HP | `infinitedryer.in` listing & conflict |
|---|---:|---:|---:|---:|---:|---:|---|
| **IFD 750** | `450` | `1,100` | `750` | `600` | `<115` | `21` | `sawdust-dryer.html`: **`₹15.00L`** (`1,500 kg/hr`, `45%` — **2×** `<45%` table!) |
| **IFD 1500** | `900` | `2,200` | `1,500` | `1,200` | `<225` | `31` | **`₹22.00L`** mislabeled on **`biomass-gasifier.html` (`250 kWth`)** & **`biomass-plant.html` (`250 kW, 14 Bar`)** |
| **IFD 2000** | `1,100` | `2,500` | `2,000` | `1,500` | `<250` | `41` | Absent from `infinitedryer.in` (separate generic `Saw Dust Flash 2 MT/H` asks **`₹25.00L`**) |
| **IFD 3000** | `1,800` | `4,400` | `3,000` | `2,400` | `<440` | `67` | `biomass-dryer.html`: **`₹42.00L`**, mislabeled **`Fluid Bed Dryer`**, **`2,000 kg/hr`**, `45%` |
| **IFD 5000** | `3,000` | `7,000` | `5,000` | `4,000` | `<700` | `136` | `biomass-dryer.html`: **`₹68.00L`**, mislabeled **`Fluid Bed Dryer`**, `5,000 kg/hr`, `45%` |
| **IFD 7500** | `4,500` | `10,000` | `7,500` | `6,000` | `<950` | `174` | Unpublished price |
| **IFD 10000** | `6,000` | `14,000` | `10,000` | `8,000` | `<1,250` | `225` | Unpublished price |

- **Moisture ceiling contradiction (`<45%` vs `<50%`):** `ifd.html` hero banner and body text twice restrict IFD to **`initial moisture content of less than 45%`**, whereas the bottom box and homepage say **`moisture < 50%`** (`<50%` strictly excludes **`50.0%`**, and IFD dry output drops `-20%` between `<45%` and `<50%`).
- **Missing fields across ALL 7 IFD models:** zero **input wet-feed rate (`kg/h`)**, zero **guaranteed outlet moisture %** (no `10%` or `12%` stated on `ifd.html`), zero **model dimensions/footprint `(L×B×H)`**, zero **motor-by-motor kW breakdown**, and zero **measured kWh/h**.
- **Reference fuel caveat (`Note #`):** `<115` to `<1,250 kg/h` explicitly assumes **`Briquettes or wood blocks of moisture < 20% & C.V. > 3,800 Kcal/kg`** — wet wood fuel will increase required kg/h and grate sizing.

### 2.2 Upstream preparation, furnace & blower mechanics (`technology.html` & homepage)

- **`technology.html` process train:** Belt conveyor with **magnetic separator** → **8 mm hexagonal-opening rotary screen** (auger-assisted oversize rejection) → screw conveyor → **"stone catcher box"** → **cage mill** (secondary wet/pre-mix breakdown + turbulence) → pneumatic vertical drying columns (`350–400°C` flue gas mixed with ambient air after refractory-lined circular HAG) → cyclone separator → rotary airlock (**"Flexi Seal airlock technology"** on homepage) → **backward-curved radial ID fan** exhausting to atmosphere via **`20 ft` stack**.
- **Major scope / safety ambiguity (`*` footnote vs `technology.html`):** `ifd.html`/`rfd.html`/`isd.html` footnote `*` reads: **`Exclusive of Dust Collector, Chimney (if more than 30 ft), Civil Work, Foundations, Electrical caballing, GST & Transport.`** `technology.html` mentions a `20 ft` stack (likely violating APPCB stack norms if taller chimney needed), explicitly excludes any **dust collector / baghouse** (cyclone-only exhaust poses combustible fines & particulate hazard!), and never clarifies whether the **belt conveyor, magnet, 8 mm hex screen, stone catcher box, cage mill, furnace & MCC/VFD** are inside or outside the `₹15L–₹68L` storefront prices.

## 3. Two-stage rotary flash dryers (`RFD 750` to `RFD 10000`) & recirculation `ISD` family

Sources: [RFD Series (`rfd.html`)](https://www.infinitedryer.com/rfd.html), [ISD Series (`isd.html`)](https://www.infinitedryer.com/isd.html), [Flash vs Rotary Blog](https://www.infinitedryer.com/flash-dryer-rotary.html).

| Model | Evap. `kg/h` | Dry o/p `<50%` `(kg/h)` | Dry o/p `<60%` `(kg/h)` | Fuel cap `<kg/h>` *(Note #)* | Connected HP | Feed size conflict | `infinitedryer.in` storefront listing |
|---|---:|---:|---:|---:|---:|---|---|
| **RFD 750** | `500` | `750` | `400` | `<125` | `24` | `<12` vs `<15` vs `<16 mm` | **`₹18.00L`** mislabeled **`Biomass Gasifier` (`Model No: RFD1500`, `500 kWth`)**! |
| **RFD 1500** | `1,000` | `1,500` | `850` | `<230` | `34` | Same triple conflict | `sawdust-dryer.html`: **`₹27.00L`** (`3,000 kg/hr`, `Semi Automatic` — **2×** rating!) |
| **RFD 2000** | `1,250` | `2,000` | `1,200` | `<275` | `45` | Same triple conflict | `biomass-dryer.html`: **`₹32.00L`** (`Fluid Bed Dryer`, **`1,000 kg/hr`**, `45%`) |
| **RFD 3000** | `2,000` | `3,000` | `1,800` | `<450` | `93` | Same triple conflict | `ddgs-dryer.html`: **`₹51.00L`** (`RFD 3000 DDGS`, `Model No: RFD1500`, **`500 TPD`**!) |
| **RFD 5000** | `3,200` | `5,000` | `3,000` | `<750` | `173` | Same triple conflict | `biomass-dryer.html`: **`Ask for Price`** (`Fluid Bed Dryer`, `3,000 kg/hr`, `45%`) |
| **RFD 7500** | `4,700` | `7,500` | `4,000` | `<1,050` | `235` | Same triple conflict | `biomass-dryer.html`: **`₹99.00L`** (`Fluid Bed Dryer`, **`10,000 kg/hr`**, `45%`) |
| **RFD 10000** | `6,500` | `10,000` | `6,000` | `<1,250` | `325` | Same triple conflict | Unpublished price |

- **Critical design clarification:** `RFD` is **NOT** a standalone slow-speed rotary drum dryer. `rfd.html` specifies a sloped liftered **rotary pre-dryer/heater** (cooling flue gas to `200–250°C`) discharging by gravity into a **standard `IFD` pneumatic flash column** (`4–6 s` total residence). Therefore flash-stage velocity/screen/airlock sensitivity still applies!
- **Three-way particle-size contradiction on `RFD`:** Homepage card states **`Size <12mm`**, `rfd.html` wood bullet specifies **`less than 15 mm`**, and `rfd.html` Techno Commercial table specifies **`size < 16mm`**.
- **Newly captured `ISD` 6th Gen Series (`isd.html` — comparator only):** Twin-shaft back-mixing blender mixes wet slurry/sludge (`<80%`, `<5 mm`) with recirculated dry product to make `~50%` granular feed entering an RFD system. Models: **`ISD 750 / 1500 / 3000 / 6000`** → Evap `750 / 1,500 / 3,000 / 6,000 kg/h`; Feed `<850 / <1,700 / <3,500 / <7,000 kg/h`; Dry o/p `<15%` (`100–150 / 200–300 / 500–600 / 1,000–1,200 kg/h`; prose says `<10%`); Fuel `<150 / <300 / <600 / <1,200 kg/h`; Connected HP `47 / 87 / 186 / 298 HP`; Area `(L×B×H)` **`9×9×9 / 12×12×10 / 20×20×12 / 25×25×15 m`**. While aimed at ETP sludge/poultry litter/pressmud rather than chipped logs, **`isd.html` reveals two crucial engineering clues:** (1) typical **footprint envelope (`12–25 m` length/width and `10–15 m` shed clearance)** likely needed for comparable RFD/IFD multi-stage units, and (2) even Infinite's 6th Gen system blends down to `~50%` before feeding its RFD stage!

## 4. Additional `infinitedryer.in` storefront listings (prices & template anomalies)

All prices on [Sitemap](https://www.infinitedryer.in/sitemap.html) / [Photos](https://www.infinitedryer.in/photos.html) are `PUBLIC ASKING PRICE` entries managed on an IndiaMART TrustSEAL storefront — **NOT formal quotes** — and display severe cross-SKU pasting:
- **`Saw Dust Flash Dryer 2 MT/H` (`spin-flash-dryer.html`):** **`₹25.00L`**, `40 × 20 ft` space, `9 MT` weight, max `400°C`, `WOOD / BRIQUETTES`, `PELLET MANUFACTURING`. Unclear how this differs from `IFD2000`.
- **`Sawdust Dryer 5000 kg/hr` (`briquetting-machines.html`):** **`₹22.00L`**, `Wood Fired`, table says `50 To 12%`, prose says `UPTO 60% INPUT MOISTURE` — wildly below `IFD5000` (`₹68L`) or `RFD5000`.
- **`Infinite Flash Dryer` (`spin-flash-dryer.html`):** **`₹12.00L`**, `1–30 Lakh kcal`, errantly states `"INDIAS MOST EFFICIENT OIL HEATING TECHNOLOGY -BOILER"`. Also `500Kg/Hr Spin Flash Dryer` (`₹15.00L`, `200°C`, `Side Rotor`, `Crystal Slurry`) and `500Kg/Hr Flash Dryer` (`₹22.00L`, `200°C`, `Multi Cyclone`, `Crystal Slurry`).
- **`Sludge Paddle Dryers` (`sludge-dryer.html`) & `Sludge Rotary Dryers` (`rotary-dryers.html`):** `500/1000/1500 kg/h` Paddle at **`₹40.00L / ₹55.00L / ₹75.00L`** (`60–80% → 15–30%`) and Rotary at **`₹55.00L`**.
- **Feedstock-specific listings:** `Coir Pith Dryer 500 kg/h` (`₹27.00L`, `35 HP`), `Bagasse Fluid Bed Dryer 10 TPH` (`₹35.00L`, `35%`), `RFD 3000 DDGS` (`₹51.00L`, `RFD1500 / 500 TPD` error).
- **Gasifiers / Power (`biomass-gasifier.html`, `biomass-plant.html`, `rice-husk-gasifier.html`):** `IFD1500` (`₹22.00L`, `250 kWth` gasifier / `14 Bar` plant), `RFD 750` (`₹18.00L`, `500 kWth` with `Model No: RFD1500`), `Automatic Rice Husk Gasifier` (`₹60.00L`, `20 kW`).

## 5. Cross-OEM interface compatibility matrix (Infinite Dryer vs 5 Briquette OEMs)

| Upstream / Downstream OEM Stage | Catalogue Particle / Moisture Profile | Interface vs **`IFD`** (`<8 mm`, `<45%` / `<50%`) | Interface vs **`RFD`** (`<12 / 15 / 16 mm`, `<50%` / `<60%`) | Engineering Action Required |
|---|---|---|---|---|
| **EcoStan `ESM 100 / 150`** | `2–10 mm` sawdust (logs `≤10–12 in`); dry `HM` strictly `≤15%` | **Partial mismatch:** `8–10 mm` fraction exceeds `<8 mm` (requires `technology.html` `8 mm` hex screen + wet recycle/cage mill) | **Nominal pass** (`10 mm < 12–16 mm`), subject to sliver/bark distribution check | Specify wet screen cut + wet wood trial; place `HM` post-dryer unless wet-rated |
| **Lehra `Log Eater` vs `CG`** | `Log Eater 5/10`: direct sawdust (sieve unconfirmed); `CG-10`: screened wood chips (screen mm open) | **`CG` needs secondary wet milling** if screen >8 mm; `Log Eater` needs sieve curve <8 mm | **`CG` screen ≤12–15 mm potentially compatible**; confirm oversized slivers | Obtain sieve curves from Lehra before sizing `IFD` vs `RFD` |
| **Jay Khodiyar `WC-75/100/150`** | Drum chippers `≤15 mm` customizable (`25–50%` claim); `SH-50` 1–1.2 TPH `≤10 mm` | **Direct chips ≤15 mm EXCEED IFD `<8 mm`** — mandatory secondary wet hammer/cage mill or screen | **Fits `RFD <15–16 mm` prose/table, BUT fails `<12 mm` homepage card** if chips reach 12–15 mm | Reconcile `RFD` `<12` vs `<16 mm`; avoid `IFD` unless paired with wet fine-milling |
| **RICO DWC-30/60 and HM** | DWC catalogue lists 3/6 TPH, chip geometry and wet duty unknown. Hammer mills accept pre-sized feed. | Needs demonstrated <8 mm accepted sawdust with compatible moisture and throughput | Test the actual cut against the confirmed RFD limit | See [primary wood comparison](../../MACHINERY/06-PRIMARY-WOOD-PREPARATION-COMPARISON.md). |
| **Ronak `64 HP Chipper / HDWC-30`** | `64 HP`: `≤10 mm` at `0.8–1.0 TPH` (undersized); `HDWC-30`: `12/15 mm` screens at `1–1.5 TPH` | **Too coarse (`10–15 mm`) & ~4–5× undersized** | Multiple units still undersized; `15 mm` exceeds `<12 mm` homepage card | Not viable as primary wet line for IFD/RFD |
| **Downstream 90 mm Presses (All 5 OEMs)** | Require **`8–12%`** (EcoStan/Lehra/JK/RICO) or **`10–15%`** (Ronak) feed; mostly `≤15–25 mm` | **UNCONFIRMED:** `ifd.html` omits outlet moisture guarantee (`<10%` vs `<12%` vs `<15%`) | **UNCONFIRMED:** `rfd.html` omits outlet moisture guarantee | Demand guaranteed `≤10%` (or press-matched `8–12%`) outlet moisture + post-dryer cooler/buffer |

## 6. Internal project-fit screening — never disclose

For `1,000 MT/month` over `340` productive hours (`10%` finished moisture, `5%` dry-solids loss) requiring **`4.64 wet TPH / 1,563 kg/h water` at `40%`** and **`5.57 wet TPH / 2,492 kg/h water` (`~2,750–3,000 kg/h` reserve) at `50%`**, plus **`~3.08 dry TPH` dryer outlet** (`2.941` finished TPH):
- **At `40%` moisture baseline:**
  - **`IFD 3000`** (`1,800 kg/h` water, `3,000 kg/h` dry at `<45%`, `67 HP`, `₹42.00L` storefront ask) clears `1,563 kg/h` water (~15% margin), **BUT `3.00 TPH` dry at `<45%` sits marginally below `~3.08 TPH`**, leaving **zero reserve** if losses exceed 5% or inlet fluctuates between `40–45%`. Also requires `<8 mm` screened sawdust!
  - **`RFD 3000`** (`2,000 kg/h` water, `3,000 kg/h` dry at `<50%`, `93 HP`, **no wood price**; DDGS storefront `₹51.00L` invalid) clears `1,563 kg/h` water (+28% margin) and accepts coarser chips (`<12–16 mm` to verify), with same `~3.00 TPH` dry-out check vs `~3.08 TPH`. (`RFD 2000` at `1,250 kg/h` **fails** 40% water duty.)
- **At `50%` moisture sensitivity:**
  - **`IFD 5000`** (`3,000 kg/h` water, `4,000 kg/h` dry at `<50%`, `136 HP`, `₹68.00L` storefront ask) meets water/dry numbers numerically, **HOWEVER both `IFD3000` and `IFD5000` explicitly state `<50%` and `<45%` prose limits**, legally **excluding exact `50.0%`** wood without written vendor re-rating!
  - **`RFD 5000`** (`3,200 kg/h` water, **`5,000 kg/h` dry at `<50%` vs `3,000 kg/h` dry at `<60%`**, `173 HP`, `Ask for Price`) clears `50%` on `<60%` rating (`3,200 > 2,492 kg/h`), **BUT its `<60%` band only delivers `3,000 kg/h` dry** (slightly shy of `~3.08 TPH`, and exact `50.0%` performance is unknown). `RFD 7500` (`4,700 kg/h` water, `4,000–7,500 kg/h` dry, `235 HP`, `₹99.00L` ask) provides headroom at nearly double capex/HP — before furnace, dust collector, chimney, electrical, civil, GST & Anakapalli freight!
- **Thermal fuel impact (`Note #`):** Burning `₹8,000/MT` finished briquettes vs `₹2,000/wet MT` wood blocks/residues `<20%` moisture substantially changes OPEX; obtain tested fuel curves (`<440 / <700 / <750 kg/h` reference caps are dry-fuel ceilings only).

## 7. What to obtain directly from Infinite Energy (`IE01–IE15`)

| ID | Deliverable | Status |
|---|---|---|
| IE01 | Formal letterhead quote (`GSTIN 06AABCI4249M1ZD`, CIN `U29299DL2005PTC140055`), clarify Delhi/Faridabad registered address & Nashik branch support | Pending |
| IE02 | Individual Ex-Works/delivered unit & complete-package wood prices for **`IFD 3000/5000`** & **`RFD 2000/3000/5000/7500`** (plus `ISD` & `2 MT/H` flash status) | Pending |
| IE03 | Reconcile `infinitedryer.in` storefront errors (`Fluid Bed` label, `45%` everywhere, `IFD750`/`RFD1500` 2× rates, `RFD7500 10k kg/h`, `500 TPD` DDGS, gasifier IDs, `briquetting-machines.html`) | Pending |
| IE04 | Confirm **`<45%` vs `<50%` IFD ceiling** and exact boundary behavior at **`45.0%` & `50.0%`** hardwood sawdust; confirm `RFD <50%` vs `<60%` curve at `40/45/50%` | Pending |
| IE05 | Reconcile **3-way `RFD` particle-size limit (`<12 mm` homepage vs `<15 mm` bullet vs `<16 mm` table)** and **`IFD <8 mm`** tolerance/rework rules | Pending |
| IE06 | Complete **simultaneous 10-point curve** (`15–60%`): wet feed kg/h, water evap kg/h, dry output kg/h, **guaranteed outlet moisture (`8–12%`)**, discharge temp, fines/solids loss | Pending |
| IE07 | Confirm exact **standard inclusions vs `*` exclusions**: are belt + magnet + `8 mm` hex rotary screen + stone catcher + cage mill + HAG included or extra? | Pending |
| IE08 | Resolve **chimney/dust safety**: `20 ft` stack (`technology.html`) vs `>30 ft` exclusion (`ifd/rfd.html`), **baghouse/wet-scrubber**, spark detection, explosion vents & fire deluge | Pending |
| IE09 | Thermal furnace & fuel guarantee: actual kcal/h, refractory grade/life, ash removal, fuel kg/h & ₹ cost when firing **wet wood chips/bark** vs `<20%` briquettes/blocks | Pending |
| IE10 | Motor-by-motor HP/kW list (ID fan, cage mill, rotary drum drive, screws, Flexi Seal airlocks, furnace blower), VFD/soft-starter panel & metered `kWh/h` | Pending |
| IE11 | Dimensions, static/dynamic loads, shed height (`10–15 m`?), clearances (`isd.html` gives `9–25 m`; `IFD/RFD` unpublished) & civil foundation drawings | Pending |
| IE12 | Operating schedule limits (`16/20/24 h`), cold/warm startup fuel & minutes, cooldown before cleanout, ash/chute cleaning downtime | Pending |
| IE13 | Part-numbered wear spares & prices (Flexi Seal blades, radial impeller/liner, cage-mill hammers, rotary lifters/tyres/rollers, `8 mm` screen, refractory) + 2-yr kit | Pending |
| IE14 | Clarify **UKAS ISO 9001:2008** currency (9001:2015 cert number?), **paid wood trial (`Sampling Policy: Paid`)** fee/duration, and `50% Delivery` review issues | Pending |
| IE15 | Written warranty, Anakapalli/AP service SLA, FAT/SAT witnessed tests & consented South India wood-dryer references (`Rubber Wood India` etc.) | Pending |

## 8. Review gate

Complete official website (`infinitedryer.com` — 15 pages) and IndiaMART TrustSEAL mini-site (`infinitedryer.in` — 22 pages, 0 PDFs) audit finished for **Infinite Energy Pvt Ltd** (**26 master records**). **All 6 sequential public manufacturer/specialist reviews (`EcoStan`, `Lehra`, `Jay Khodiyar`, `RICO`, `Ronak`, `Infinite Energy`) are now complete.** Public evidence alone qualifies neither `IFD` (`<8 mm`, `<45% / <50%` exclusions) nor unpriced `RFD` packages without simultaneous mass/thermal balance, battery-limit pricing (`technology.html` prep/cage mill/dust collector/chimney), and paid/witnessed hardwood trials. Use [updated Infinite Energy draft](../SUPPLIER-ENQUIRIES/07-INFINITE-ENERGY-DRYER.md) for outreach (do not send this dossier). **Next procurement stage: owner review of drafts, authorised RFQ collection, and cross-OEM equalisation in [Bid Equalisation](../TECHNICAL-COMMERCIAL-BID-EQUALISATION.md).** No outreach sent.
