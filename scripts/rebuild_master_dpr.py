#!/usr/bin/env python3
"""Rebuild 10-page Master DPR PDF with full Kilo Code binary consistency.

Ensures:
- Exact 10 pages total (KC-01..07 compliant).
- Page 9: Dual briquetting press labeled 'Model BPM 90 HD (strokes unverified)' - NO '220-240 BPM/strokes'.
- Page 9: Buffer storage labeled 'provisional 2-3 days weather-protected buffer chips/sawdust (subject to site fire risk review)' - NO '10-14 days wet chips'.
- Page 9: Bill of materials packages labeled as candidate vendor references / indicative budget only.
- Page 9: Offtake labeled as uncontracted promoter-observed scenario.
- Page 10: Gate 1 targets labeled as illustrative tender discussion thresholds; buyer-specific acceptance criteria to be established during boiler audit.
- Pages 1 & 7: 'floor' and 'firm baseline' replaced with promoter-observed scenario / planning baseline.
- Clean standard PDF fonts with zero missing glyphs.
"""
import os
import sys
import fitz

def rebuild_pdf():
    pdf_path = 'Anakapalli_1000MT_Wood_Briquette_Internal_DPR.pdf'
    doc = fitz.open(pdf_path)
    print(f'Initial page count: {len(doc)}')

    # 1. Truncate pages back to base 8 pages
    while len(doc) > 8:
        doc.delete_page(len(doc) - 1)
    print(f'Base page count after reset: {len(doc)}')

    # 2. Text cleanups on Page 1 (index 0) and Page 7 (index 6)
    # Page 1 (0): Remove 'floor'
    p1 = doc[0]
    p1_redactions = [
        (fitz.Rect(248, 258, 540, 275), 'Rs. 8,000 per finished metric tonne (promoter-observed scenario)', 7.5, (0.05, 0.05, 0.05)),
        (fitz.Rect(48, 488, 540, 505), 'Promoter commercial observation: Rs. 8,000/MT sales (Pajson Cashew scenario)', 7.5, (0.05, 0.05, 0.05)),
    ]
    for rbox, rtext, rsize, rcolor in p1_redactions:
        p1.add_redact_annot(rbox, fill=(1, 1, 1))
    p1.apply_redactions()
    for rbox, rtext, rsize, rcolor in p1_redactions:
        p1.insert_text(fitz.Point(rbox.x0 + 2, rbox.y0 + rsize + 1.5), rtext, fontsize=rsize, fontname='helv', color=rcolor)

    # Page 7 (6): Remove 'firm baseline'
    p7 = doc[6]
    p7_redactions = [
        (fitz.Rect(48, 562, 350, 578), 'Rs. 8,000 planning baseline throughout the year', 8.0, (0.05, 0.05, 0.05)),
    ]
    for rbox, rtext, rsize, rcolor in p7_redactions:
        p7.add_redact_annot(rbox, fill=(1, 1, 1))
    p7.apply_redactions()
    for rbox, rtext, rsize, rcolor in p7_redactions:
        p7.insert_text(fitz.Point(rbox.x0 + 2, rbox.y0 + rsize + 1.5), rtext, fontsize=rsize, fontname='helv', color=rcolor)

    # Styling constants
    navy = (0.12, 0.29, 0.49)
    charcoal = (0.15, 0.15, 0.15)
    grey_text = (0.35, 0.35, 0.35)
    line_color = (0.8, 0.8, 0.8)
    table_head_bg = (0.86, 0.90, 0.95)
    table_alt_bg = (0.96, 0.97, 0.98)
    alert_bg = (0.99, 0.92, 0.90)
    green_bg = (0.90, 0.95, 0.90)

    # 3. Create Page 9
    p9 = doc.new_page(width=595.28, height=841.89)

    # Running Header
    p9.draw_line(fitz.Point(48.2, 38), fitz.Point(547.0, 38), color=line_color, width=0.5)
    p9.insert_text(fitz.Point(48.2, 30), 'AKASHYA ENTERPRISES | 1,000 MT/MONTH WOOD BIOMASS BRIQUETTES', fontsize=8, fontname='hebo', color=navy)
    p9.insert_text(fitz.Point(515.0, 30), 'Page 9', fontsize=8, fontname='helv', color=grey_text)

    # Title
    p9.insert_text(fitz.Point(48.2, 56), '9 | 15-Year Horizon, Inflation Controls & March 15, 2027 Financing Critical Path', fontsize=11.5, fontname='hebo', color=navy)

    # Scope paragraph
    scope_txt = (
        'Scope: 15-year operating horizon after commissioning (not a bank loan tenure guarantee). Nominal INR. Excludes land '
        'acquisition, lease rent, bank loan interest/principal, and corporate income taxes. A static Rs. 8,000/MT price structure '
        'without escalation leads to negative EBITDA by Year 7 under 6% wet-wood inflation. Long-term corporate boiler supply '
        'agreements must include annual contract price indexation (+4% to +5%/year) to preserve project solvency.'
    )
    p9.insert_textbox(fitz.Rect(48.2, 63, 547.0, 102), scope_txt, fontsize=7.0, fontname='helv', color=charcoal)

    # Section A: 15-Year Inflation Scenarios Table
    p9.insert_text(fitz.Point(48.2, 110), 'A | 15-YEAR COMMODITY INFLATION & OPERATING MARGIN SCENARIOS', fontsize=8.2, fontname='hebo', color=navy)

    t1_top = 116
    p9.draw_rect(fitz.Rect(48.2, t1_top, 547.0, t1_top + 15), fill=table_head_bg, color=line_color, width=0.5)
    p9.insert_text(fitz.Point(52, t1_top + 10.5), 'Scenario', fontsize=7.0, fontname='hebo', color=navy)
    p9.insert_text(fitz.Point(125, t1_top + 10.5), 'Escalation Rates', fontsize=7.0, fontname='hebo', color=navy)
    p9.insert_text(fitz.Point(235, t1_top + 10.5), 'Yr 1 EBITDA', fontsize=7.0, fontname='hebo', color=navy)
    p9.insert_text(fitz.Point(295, t1_top + 10.5), 'Yr 5 EBITDA', fontsize=7.0, fontname='hebo', color=navy)
    p9.insert_text(fitz.Point(355, t1_top + 10.5), 'Yr 10 EBITDA', fontsize=7.0, fontname='hebo', color=navy)
    p9.insert_text(fitz.Point(420, t1_top + 10.5), 'Yr 15 EBITDA', fontsize=7.0, fontname='hebo', color=navy)
    p9.insert_text(fitz.Point(480, t1_top + 10.5), '15-Yr Cumul. Cash', fontsize=7.0, fontname='hebo', color=navy)

    rows_t1 = [
        ('Scenario A (Base Case)', 'Sale +3%/yr, Wood +6%/yr, Power +5%/yr', 'Rs. 8.8 L', 'Rs. 29.9 L', '-Rs. 110.3 L', '-Rs. 319.0 L', '-Rs. 19.35 Cr (Alert: Neg. Yr 7)', alert_bg),
        ('Scenario B (Indexed Offtake)', 'Sale +5%/yr, Wood +6%/yr, Power +5%/yr', 'Rs. 8.8 L', 'Rs. 107.6 L', 'Rs. 102.7 L', 'Rs. 84.7 L', '+Rs. 6.34 Cr (Recovers capital Yr 8)', green_bg),
        ('Scenario C (Downside Stress)', 'Sale 0%/yr, Wood +8%/yr, Power +7%/yr', 'Rs. 8.8 L', '-Rs. 147.0 L', '-Rs. 584.9 L', '-Rs. 1,213.7 L', '-Rs. 76.65 Cr (Severe deficit)', (1, 0.95, 0.95))
    ]

    curr_y = t1_top + 15
    for r_name, r_esc, y1, y5, y10, y15, cum, bg in rows_t1:
        p9.draw_rect(fitz.Rect(48.2, curr_y, 547.0, curr_y + 13), fill=bg, color=line_color, width=0.5)
        p9.insert_text(fitz.Point(52, curr_y + 9.5), r_name, fontsize=6.8, fontname='hebo', color=charcoal)
        p9.insert_text(fitz.Point(125, curr_y + 9.5), r_esc, fontsize=6.5, fontname='helv', color=charcoal)
        p9.insert_text(fitz.Point(235, curr_y + 9.5), y1, fontsize=6.8, fontname='helv', color=charcoal)
        p9.insert_text(fitz.Point(295, curr_y + 9.5), y5, fontsize=6.8, fontname='helv', color=charcoal)
        p9.insert_text(fitz.Point(355, curr_y + 9.5), y10, fontsize=6.8, fontname='helv', color=charcoal)
        p9.insert_text(fitz.Point(420, curr_y + 9.5), y15, fontsize=6.8, fontname='helv', color=charcoal)
        p9.insert_text(fitz.Point(480, curr_y + 9.5), cum, fontsize=6.5, fontname='hebo', color=navy if '+' in cum else (0.7, 0.1, 0.1))
        curr_y += 13

    note_t1 = 'Notes: Scheduled replacement reserves: Yr 6 (Rs. 30L), Yr 10 (Rs. 50L), Yr 13 (Rs. 30L). Initial cash base starts at -Rs. 6.19 Cr (Fixed Rs. 5.20 Cr + WC Rs. 99.43L).'
    p9.insert_text(fitz.Point(48.2, curr_y + 8), note_t1, fontsize=6.0, fontname='heit', color=grey_text)

    # Section B: Critical Path to 15 March 2027 Milestone
    curr_y += 17
    p9.insert_text(fitz.Point(48.2, curr_y), 'B | CRITICAL PATH TO 15 MARCH 2027 FINANCING TARGET & FIRST DISBURSEMENT', fontsize=8.2, fontname='hebo', color=navy)

    curr_y += 6
    p9.draw_rect(fitz.Rect(48.2, curr_y, 547.0, curr_y + 15), fill=table_head_bg, color=line_color, width=0.5)
    p9.insert_text(fitz.Point(52, curr_y + 10.5), 'Target Window', fontsize=7.0, fontname='hebo', color=navy)
    p9.insert_text(fitz.Point(155, curr_y + 10.5), 'Milestone & Regulatory Gate', fontsize=7.0, fontname='hebo', color=navy)
    p9.insert_text(fitz.Point(320, curr_y + 10.5), 'Key Deliverable & Bank Readiness Evidence', fontsize=7.0, fontname='hebo', color=navy)

    rows_t2 = [
        ('22 Nov - 15 Dec 2026', 'Bank DPR, TEV Study & Vendor RFQs', '3 binding turnkey OEM quotes; DFO written wood species determination; site soil test.'),
        ('16 Dec 2026 - 15 Jan 2027', 'Loan Application & Statutory Filings', 'Formal loan filing with lender/SIDBI; APPCB CTE filing; APEPDCL 11 kV HT power feasibility.'),
        ('16 Jan - 28 Feb 2027', 'Appraisal, Sanction & Equity Escrow', 'Lender site audit, title legal clearance, promoter equity commitment (Rs. 1.55 Cr), sanction letter.'),
        ('01 Mar - 15 Mar 2027', 'CP Compliance & First Disbursement', 'TARGET: First eligible loan drawdown released for long-lead equipment orders (candidate OEM press & dryer).'),
        ('16 Mar - 31 Oct 2027', 'Civil Shed Construction & Erection', 'Pre-engineered industrial shed, machine foundations, 500 kVA substation, conveyor integration.'),
        ('01 Nov - 30 Nov 2027', 'Trial Runs & Commercial Production', 'Wet-wood commissioning, APPCB CTO inspection, boiler client deliveries ramp to 1,000 MT/month.')
    ]

    curr_y += 15
    for idx, (p_win, p_mile, p_deliv) in enumerate(rows_t2):
        bg = table_alt_bg if idx % 2 == 1 else (1, 1, 1)
        if 'TARGET' in p_deliv:
            bg = green_bg
        p9.draw_rect(fitz.Rect(48.2, curr_y, 547.0, curr_y + 13), fill=bg, color=line_color, width=0.5)
        p9.insert_text(fitz.Point(52, curr_y + 9), p_win, fontsize=6.8, fontname='hebo', color=charcoal)
        p9.insert_text(fitz.Point(155, curr_y + 9), p_mile, fontsize=6.8, fontname='helv', color=charcoal)
        p9.insert_text(fitz.Point(320, curr_y + 9), p_deliv, fontsize=6.5, fontname='helv', color=navy if 'TARGET' in p_deliv else charcoal)
        curr_y += 13

    note_t2 = 'Note: Fiscal year ends 31 March 2027. Sanction is subject to lender credit committee; milestone ensures readiness before year-end rush.'
    p9.insert_text(fitz.Point(48.2, curr_y + 8), note_t2, fontsize=6.0, fontname='heit', color=grey_text)

    # Section C: Turnkey Plant BOM & Capital Structure Table (KC-01 & KC-04 compliant)
    curr_y += 17
    p9.insert_text(fitz.Point(48.2, curr_y), 'C | TURNKEY BILL OF MATERIALS & CAPITAL STRUCTURE (EXCLUDING LAND)', fontsize=8.2, fontname='hebo', color=navy)

    curr_y += 6
    p9.draw_rect(fitz.Rect(48.2, curr_y, 547.0, curr_y + 15), fill=table_head_bg, color=line_color, width=0.5)
    p9.insert_text(fitz.Point(52, curr_y + 10.5), 'Major Package (Candidate Reference)', fontsize=7.0, fontname='hebo', color=navy)
    p9.insert_text(fitz.Point(175, curr_y + 10.5), 'Indicative Specification & Scope (Budget Only)', fontsize=7.0, fontname='hebo', color=navy)
    p9.insert_text(fitz.Point(430, curr_y + 10.5), 'Power (HP)', fontsize=7.0, fontname='hebo', color=navy)
    p9.insert_text(fitz.Point(495, curr_y + 10.5), 'Budget (Rs. L)', fontsize=7.0, fontname='hebo', color=navy)

    bom_rows = [
        ('Log Shredder (EcoStan ESM 150 ref)', 'Heavy rotor drum with multi-knives, handles up to 12-inch logs and branches', '159 HP', 'Rs. 34.00 L'),
        ('Hammer Mill & Screening', 'Secondary size reduction to under 5mm, magnetic separator, vibrating screen', '50 HP', 'Rs. 18.00 L'),
        ('Flash Dryer Train (Infinite/EcoStan ref)', 'Double-pass pneumatic U-ducts, >=1,800 kg/hr evap, furnace and cyclone', '93 HP', 'Rs. 75.00 L'),
        ('Dual Briquetting Presses (BPM 90 HD)', 'Two 90mm piston presses, Model BPM 90 HD (strokes unverified), 1.3-2.0 TPH each', '179 HP', 'Rs. 52.00 L'),
        ('Material Handling & Logistics', 'Log intake tables, screw/belt conveyors, 4WD Tractor Loader, Weighbridge', '45 HP', 'Rs. 47.00 L'),
        ('Electricals, Air & Spares', 'Central MCC panel, cabling, dust extraction cyclone, workshop spares, freight', '35 HP', 'Rs. 84.00 L'),
        ('Civil Works & 11 kV Substation', 'PEB factory shed (15,000 sq ft), heavy machine foundations, 500 kVA substation', 'N/A', 'Rs. 210.00 L'),
    ]

    curr_y += 15
    for idx, (pkg, spec, hp, bgt) in enumerate(bom_rows):
        bg = table_alt_bg if idx % 2 == 1 else (1, 1, 1)
        p9.draw_rect(fitz.Rect(48.2, curr_y, 547.0, curr_y + 12), fill=bg, color=line_color, width=0.5)
        p9.insert_text(fitz.Point(52, curr_y + 8.5), pkg, fontsize=6.5, fontname='hebo', color=charcoal)
        p9.insert_text(fitz.Point(175, curr_y + 8.5), spec, fontsize=6.2, fontname='helv', color=charcoal)
        p9.insert_text(fitz.Point(435, curr_y + 8.5), hp, fontsize=6.5, fontname='helv', color=charcoal)
        p9.insert_text(fitz.Point(498, curr_y + 8.5), bgt, fontsize=6.5, fontname='hebo', color=navy)
        curr_y += 12

    # Subtotal row for BOM
    p9.draw_rect(fitz.Rect(48.2, curr_y, 547.0, curr_y + 13), fill=green_bg, color=line_color, width=0.5)
    p9.insert_text(fitz.Point(52, curr_y + 9), 'TOTAL CAPITAL REQUIREMENT', fontsize=6.8, fontname='hebo', color=navy)
    p9.insert_text(fitz.Point(175, curr_y + 9), 'Fixed Capital: Rs. 520.00 L | Opening Working Capital: Rs. 99.43 L (Total cash required)', fontsize=6.5, fontname='hebo', color=navy)
    p9.insert_text(fitz.Point(430, curr_y + 9), '561 HP', fontsize=6.8, fontname='hebo', color=navy)
    p9.insert_text(fitz.Point(495, curr_y + 9), 'Rs. 619.43 L', fontsize=7.0, fontname='hebo', color=navy)
    curr_y += 13

    # Section D: Governing Policies & Risk Controls (KC-02 & KC-03 compliant)
    curr_y += 17
    p9.insert_text(fitz.Point(48.2, curr_y), 'D | GOVERNING QUALITY, FEEDSTOCK & OPERATING POLICIES', fontsize=8.2, fontname='hebo', color=navy)

    policies = [
        ('Feedstock Indexation & Commercial Offtake Terms: ', 'Corporate boiler agreements (Cohance, Torrent, Toyotsu) must feature annual price indexation (min +4% to +5%/year) tied to raw timber rates. Baseline rate of Rs. 8,000/MT is an uncontracted promoter-observed scenario.'),
        ('Incoming Log Moisture Control: ', 'Daily weighbridge moisture testing. Base economics assume 40% moisture. Moisture between 40-50% triggers proportional weight deductions (payment on dry-basis equivalent). Batches with >50% moisture are rejected.'),
        ('Dual 50% Capacity Sharing: ', 'Two candidate EcoStan BPM 90 HD presses provide dual 50% capacity sharing. Breakdown of 1 press preserves 50% production (20 MT/day). Raw logs sourced on demand; wet-chip buffer to be approved after site fire risk review; provisional 2-3 days weather-protected buffer chips/sawdust (subject to site fire risk review).'),
        ('Statutory Clearances: ', 'APPCB Orange Category consent via Single Desk; AP Forest Dept written determination under 2018 Wood-Based Industry Rules; APEPDCL 11 kV HT connection under Category III(A) industrial tariff.')
    ]

    curr_y += 8
    policy_heights = [24, 24, 34, 24]
    for (p_title, p_desc), box_h in zip(policies, policy_heights):
        tb_rect = fitz.Rect(52, curr_y, 547.0, curr_y + box_h)
        bullet_text = f"- {p_title}{p_desc}"
        p9.insert_textbox(tb_rect, bullet_text, fontsize=6.7, fontname='helv', color=charcoal)
        curr_y += box_h + 3

    # Running Footer on Page 9
    p9.draw_line(fitz.Point(48.2, 805), fitz.Point(547.0, 805), color=line_color, width=0.5)
    p9.insert_text(fitz.Point(48.2, 818), 'Akashya Enterprises · Owner Planning Master DPR · 22 Nov 2026 · Anakapalli, AP', fontsize=8, fontname='helv', color=grey_text)
    p9.insert_text(fitz.Point(460.0, 818), 'Continued to Page 10 ->', fontsize=7.5, fontname='hebo', color=navy)

    # 4. Create Page 10 (KC-05 compliant)
    p10 = doc.new_page(width=595.28, height=841.89)

    # Running Header
    p10.draw_line(fitz.Point(48.2, 38), fitz.Point(547.0, 38), color=line_color, width=0.5)
    p10.insert_text(fitz.Point(48.2, 30), 'AKASHYA ENTERPRISES | 1,000 MT/MONTH WOOD BIOMASS BRIQUETTES', fontsize=8, fontname='hebo', color=navy)
    p10.insert_text(fitz.Point(510.0, 30), 'Page 10', fontsize=8, fontname='helv', color=grey_text)

    # Title
    p10.insert_text(fitz.Point(48.2, 56), '10 | Biomass Briquette Drawbacks, 90mm Boiler Trials & High-Moisture Dryer Sizing', fontsize=11.2, fontname='hebo', color=navy)

    # Scope paragraph
    scope_txt_10 = (
        'Scope: Critical engineering evaluation based on promoter-supplied research (December 2025) and updated technical '
        'guidelines (22 Nov 2026). Sizing analysis contrasts 40% base-case wood moisture with 50% high-wet conditions, establishes '
        'the 4-gate customer boiler qualification protocol, and specifies fire/dust safety standards.'
    )
    p10.insert_textbox(fitz.Rect(48.2, 63, 547.0, 100), scope_txt_10, fontsize=6.8, fontname='helv', color=charcoal)

    # Section A: Wood Moisture Sensitivity & Dryer Water Removal Capacity Table
    p10.insert_text(fitz.Point(48.2, 108), 'A | WOOD MOISTURE SENSITIVITY & DRYER EVAPORATION BOTTLENECK (340 PRODUCTIVE HOURS/MONTH)', fontsize=8.0, fontname='hebo', color=navy)

    t1_top = 114
    p10.draw_rect(fitz.Rect(48.2, t1_top, 547.0, t1_top + 15), fill=table_head_bg, color=line_color, width=0.5)
    p10.insert_text(fitz.Point(52, t1_top + 10.5), 'Moisture', fontsize=7.0, fontname='hebo', color=navy)
    p10.insert_text(fitz.Point(100, t1_top + 10.5), 'Wet Wood (MT)', fontsize=7.0, fontname='hebo', color=navy)
    p10.insert_text(fitz.Point(170, t1_top + 10.5), 'Wood Cost (Rs. L)', fontsize=7.0, fontname='hebo', color=navy)
    p10.insert_text(fitz.Point(250, t1_top + 10.5), 'Water Evap. (MT)', fontsize=7.0, fontname='hebo', color=navy)
    p10.insert_text(fitz.Point(325, t1_top + 10.5), 'Evap. Rate (kg/h)', fontsize=7.0, fontname='hebo', color=navy)
    p10.insert_text(fitz.Point(405, t1_top + 10.5), 'EBITDA (Rs. L)', fontsize=7.0, fontname='hebo', color=navy)
    p10.insert_text(fitz.Point(475, t1_top + 10.5), 'Dryer Engineering Verdict', fontsize=7.0, fontname='hebo', color=navy)

    moisture_data = [
        ('25%', '1,263 MT', 'Rs. 25.26 L', '216 MT', '635 kg/h', 'Rs. 17.82 L', 'Well within 1,800 kg/h dryer rating', (1, 1, 1)),
        ('30%', '1,353 MT', 'Rs. 27.07 L', '306 MT', '900 kg/h', 'Rs. 16.01 L', 'Well within 1,800 kg/h dryer rating', table_alt_bg),
        ('35%', '1,458 MT', 'Rs. 29.15 L', '410 MT', '1,206 kg/h', 'Rs. 13.93 L', 'Comfortable operating margin (33% reserve)', (1, 1, 1)),
        ('40% BASE', '1,579 MT', 'Rs. 31.58 L', '532 MT', '1,563 kg/h', 'Rs. 11.50 L', 'BASE DESIGN: 15% reserve on 1,800 kg/h dryer', green_bg),
        ('45%', '1,723 MT', 'Rs. 34.45 L', '675 MT', '1,986 kg/h', 'Rs. 8.63 L', 'Zero margin on 2,000 kg/h; needs 20h schedule', (1, 0.98, 0.94)),
        ('50% HIGH', '1,895 MT', 'Rs. 37.89 L', '847 MT', '2,492 kg/h', 'Rs. 5.18 L', 'BOTTLENECK: Exceeds 2,000 kg/h; needs 3,000 kg/h unit', alert_bg),
        ('55%', '2,105 MT', 'Rs. 42.11 L', '1,058 MT', '3,111 kg/h', 'Rs. 0.97 L', 'SEVERE DEFICIT: Unviable without log seasoning', (1, 0.92, 0.92))
    ]

    curr_y = t1_top + 15
    for m_label, logs, cost, wtr, rate, ebitda, verdict, bg in moisture_data:
        p10.draw_rect(fitz.Rect(48.2, curr_y, 547.0, curr_y + 12.5), fill=bg, color=line_color, width=0.5)
        p10.insert_text(fitz.Point(52, curr_y + 9), m_label, fontsize=6.7, fontname='hebo', color=charcoal)
        p10.insert_text(fitz.Point(100, curr_y + 9), logs, fontsize=6.7, fontname='helv', color=charcoal)
        p10.insert_text(fitz.Point(170, curr_y + 9), cost, fontsize=6.7, fontname='helv', color=charcoal)
        p10.insert_text(fitz.Point(250, curr_y + 9), wtr, fontsize=6.7, fontname='helv', color=charcoal)
        p10.insert_text(fitz.Point(325, curr_y + 9), rate, fontsize=6.7, fontname='hebo' if 'BASE' in m_label or 'HIGH' in m_label else 'helv', color=navy if 'BASE' in m_label else (0.7, 0.1, 0.1) if 'HIGH' in m_label else charcoal)
        p10.insert_text(fitz.Point(405, curr_y + 9), ebitda, fontsize=6.7, fontname='hebo', color=navy if 'BASE' in m_label else charcoal)
        p10.insert_text(fitz.Point(475, curr_y + 9), verdict, fontsize=6.0, fontname='hebo' if 'BASE' in m_label or 'HIGH' in m_label else 'helv', color=navy if 'BASE' in m_label else (0.7, 0.1, 0.1) if 'HIGH' in m_label else charcoal)
        curr_y += 12.5

    note_m = 'Note: EBITDA reflects feedstock variance only. At 50% moisture, added furnace fuel, power, and 3,000 kg/h dryer capex reduce surplus below Rs. 5.18L.'
    p10.insert_text(fitz.Point(48.2, curr_y + 8), note_m, fontsize=6.0, fontname='heit', color=grey_text)

    # Section B: Customer Boiler Qualification & 4-Gate Trial Protocol (KC-05 & KC-06 compliant)
    curr_y += 17
    p10.insert_text(fitz.Point(48.2, curr_y), 'B | INDUSTRIAL BOILER COMPATIBILITY & 4-GATE CUSTOMER TRIAL PROTOCOL', fontsize=8.0, fontname='hebo', color=navy)

    curr_y += 6
    p10.draw_rect(fitz.Rect(48.2, curr_y, 547.0, curr_y + 15), fill=table_head_bg, color=line_color, width=0.5)
    p10.insert_text(fitz.Point(52, curr_y + 10.5), 'Trial Stage', fontsize=7.0, fontname='hebo', color=navy)
    p10.insert_text(fitz.Point(125, curr_y + 10.5), 'Qualification Scope & Safety Verification', fontsize=7.0, fontname='hebo', color=navy)
    p10.insert_text(fitz.Point(365, curr_y + 10.5), 'Target Industrial Boiler Clients', fontsize=7.0, fontname='hebo', color=navy)

    gates = [
        ('Gate 0: Safety & Grate', 'Audit boiler firing doors, stoker interlocks & grate type. Do not mandate manual feeding if automated stoker cannot accept 90mm without crushing.', 'Cohance Lifesciences (Atchutapuram SEZ)\nTeejay India (Brandix Apparel City)'),
        ('Gate 1: Lab Analysis', 'Accredited testing: Illustrative tender discussion thresholds (moisture <=10%, ash <=3%, GCV >=3,800 kcal/kg, density >=1.15 g/cm3, shatter >=95%; buyer-specific acceptance criteria to be established during boiler audit; zero buyer-approved grades on file).', 'Torrent Pharmaceuticals (JNPC Parawada)\nVisakha Solvents (APSEZ Rambilli)'),
        ('Gate 2: Steam Trial', '48-hour continuous firing trial logging steam output (t/h), thermal efficiency, air-fuel ratio, flue gas opacity, and grate clinkering.', 'Toyotsu Rare Earths (12 TPH boiler consent)\nLaurus Labs / Local Pharma Units'),
        ('Gate 3: Purchase PO', 'Execution of binding monthly offtake contract with minimum volume commitment and annual price escalation clause (min +4% to +5%/yr).', 'Commercial requirement before commitment;\nNo uncontracted volume assumed.')
    ]

    curr_y += 15
    for idx, (g_title, g_scope, g_clients) in enumerate(gates):
        bg = table_alt_bg if idx % 2 == 1 else (1, 1, 1)
        g_h = 24
        p10.draw_rect(fitz.Rect(48.2, curr_y, 547.0, curr_y + g_h), fill=bg, color=line_color, width=0.5)
        p10.insert_text(fitz.Point(52, curr_y + 10), g_title, fontsize=6.7, fontname='hebo', color=navy)
        
        p10.insert_textbox(fitz.Rect(125, curr_y + 2, 360, curr_y + g_h - 1), g_scope, fontsize=6.0, fontname='helv', color=charcoal)
        p10.insert_textbox(fitz.Rect(365, curr_y + 2, 544, curr_y + g_h - 1), g_clients, fontsize=6.0, fontname='hebo', color=charcoal)
        curr_y += g_h

    # Section C: Technical Drawbacks Synthesis (Pellet Mill vs Piston Press)
    curr_y += 18
    p10.insert_text(fitz.Point(48.2, curr_y), 'C | TECHNICAL DRAWBACKS SYNTHESIS: PELLET MILL VS MECHANICAL PISTON PRESS', fontsize=8.0, fontname='hebo', color=navy)

    drawback_points = [
        ('Manual Feeding Hazards in Boilers: ', 'Manual feeding causes heat loss, air infiltration, and worker backfire risks. Akashya Enterprises 90mm briquettes target industrial boilers designed for lump solid fuel or retrofitted with hydraulic pushers. Customers requiring small fuel (<25mm) must not be sold intact 90mm briquettes.'),
        ('Pellet Mill vs Piston Press Mechanics: ', 'Pellet mill failures in research (roller wear, clogged die holes, high power) relate to rotary extrusion through perforated dies. Akashya Enterprises plans candidate mechanical piston presses (e.g. EcoStan BPM 90 HD reference), which compress wood chips in a single continuous reciprocating stroke, eliminating roller-jam failure modes.'),
        ('Combustion Characteristics: ', 'Pure hardwood sawdust briquettes deliver volatile matter of 65-70% and fixed carbon ~30%. High density ensures prolonged burning without premature disintegration, provided incoming log moisture is rigorously controlled <=40%.')
    ]

    curr_y += 8
    for title, desc in drawback_points:
        tb_rect = fitz.Rect(52, curr_y, 547.0, curr_y + 30)
        p10.insert_textbox(tb_rect, f"- {title}{desc}", fontsize=6.6, fontname='helv', color=charcoal)
        curr_y += 30

    # Section D: Statutory, Credit Guarantee & Safety Mandates
    curr_y += 10
    p10.insert_text(fitz.Point(48.2, curr_y), 'D | STATUTORY, CREDIT GUARANTEE & SAFETY MANDATES', fontsize=8.0, fontname='hebo', color=navy)

    statutory_points = [
        ('CGTMSE Credit Guarantee Ceiling: ', 'Effective 1 April 2025, CGTMSE coverage extends up to Rs. 10 Crore facility limit. This represents maximum guarantee eligibility, NOT an automatic loan approval. Bank appraisal, DSCR covenants, and promoter equity (Rs. 1.55 Cr) remain mandatory.'),
        ('BioURJA Subsidy Precaution: ', 'MNRE BioURJA Phase II budget approval is pending for applications post 10 Oct 2024. Model retains Rs. 0 subsidy to protect project viability against sovereign subsidy disbursement delays.'),
        ('Fire, Dust & Safety Compliance: ', 'Pneumatic drying and size reduction generate combustible wood dust. Erection must incorporate ATEX/OSHA-aligned spark detection, explosion venting on cyclones, grounded ducts, and strict storage pile height limits.')
    ]

    curr_y += 8
    for title, desc in statutory_points:
        tb_rect = fitz.Rect(52, curr_y, 547.0, curr_y + 30)
        p10.insert_textbox(tb_rect, f"- {title}{desc}", fontsize=6.6, fontname='helv', color=charcoal)
        curr_y += 30

    # Running Footer on Page 10
    p10.draw_line(fitz.Point(48.2, 805), fitz.Point(547.0, 805), color=line_color, width=0.5)
    p10.insert_text(fitz.Point(48.2, 818), 'Akashya Enterprises · Owner Planning Master DPR · 22 Nov 2026 · Anakapalli, AP', fontsize=8, fontname='helv', color=grey_text)
    p10.insert_text(fitz.Point(410.0, 818), 'End of 10-Page Master DPR', fontsize=8, fontname='hebo', color=navy)

    # Save to temp file then replace
    temp_pdf = 'temp_rebuilt_dpr.pdf'
    doc.save(temp_pdf)
    doc.close()

    os.replace(temp_pdf, pdf_path)
    print(f'Successfully rebuilt 10-page master DPR: {pdf_path}')

if __name__ == '__main__':
    rebuild_pdf()
