#!/usr/bin/env python3
"""Regenerate a clean, correct page 7 (Rs. 8,000 scale + payback) of the *current*
10-page DPR, preserving every other page.

The previous coordinate-patch approach assumed a pristine Rs. 9,000 page, but the
checked-in PDF (rebuilt in commit de943d8) carries a half-migrated page 7: the
600/750/850 MT rows still hold Rs. 9,000 figures, the 1000-MT row was already set
to Rs. 8,000 at shifted x-coordinates, and the payback paragraph is scrambled.
Patching coordinates cannot reconcile that, so this module clears page 7 and
redraws it deterministically with Rs. 8,000 economics and a 4.49-year simple
payback.

Public entry point used by scripts/rebuild_master_dpr.py:
    fix_page(page) -> bool   # True if the page was (re)drawn, False if already correct

Standalone (used by scripts/run_binary_repairs.py):
    python scripts/repair_page7_scale.py
"""
from __future__ import annotations
import os
from pathlib import Path
import fitz

PDF = Path("Anakapalli_1000MT_Wood_Briquette_Internal_DPR.pdf")

# Monthly revenue and operating surplus (Rs. lakh) at Rs. 8,000/MT, holding the
# original PDF's non-sales operating costs. Ref: FINANCE/OWNER-COST-RECONCILIATION.md.
VOLUME_ROWS = [
    ("600 MT", "Rs. 48.00 lakh", "Rs. 0.23 lakh"),
    ("750 MT", "Rs. 60.00 lakh", "Rs. 4.46 lakh"),
    ("850 MT", "Rs. 68.00 lakh", "Rs. 7.27 lakh"),
    ("1000 MT", "Rs. 80.00 lakh", "Rs. 11.50 lakh"),
]
# Price x wet-wood-cost EBITDA grid (Rs. lakh/month). Columns: sale 8000/9000/10000.
GRID_ROWS = [
    ("Rs. 1,500 / wet MT", "19.39", "29.39", "39.39"),
    ("Rs. 2,000 / wet MT", "11.50", "21.50", "31.50"),
    ("Rs. 2,500 / wet MT", "3.60", "13.60", "23.60"),
    ("Rs. 3,000 / wet MT", "-4.29", "5.71", "15.71"),
]

NAVY = (0.12, 0.29, 0.49)
CHARCOAL = (0.15, 0.15, 0.15)
GREY = (0.35, 0.35, 0.35)
LINE = (0.8, 0.8, 0.8)
HEAD_BG = (0.86, 0.90, 0.95)
ALT_BG = (0.96, 0.97, 0.98)
GREEN_BG = (0.90, 0.95, 0.90)

LEFT, RIGHT = 48.2, 547.0
CORRECT = ("48.00", "60.00", "68.00", "80.00", "0.23", "4.46", "7.27", "11.50", "4.49")
OBSOLETE = ("54.00 lakh", "67.50 lakh", "76.50 lakh", "90.00 lakh",
            "2.43 years", "627.43 lakh", "257.98 lakh")


def _is_correct(text: str) -> bool:
    return all(x in text for x in CORRECT) and not any(x in text for x in OBSOLETE)


def _section(page, y, text):
    page.insert_text(fitz.Point(LEFT, y), text, fontsize=8.2, fontname="hebo", color=NAVY)


def _table(page, top, cols, header, rows, row_h=15.0, last_row_green=False):
    page.draw_rect(fitz.Rect(LEFT, top, RIGHT, top + 15), fill=HEAD_BG, color=LINE, width=0.5)
    for x, name in zip(cols, header):
        page.insert_text(fitz.Point(x + 4, top + 10.5), name, fontsize=7.2, fontname="hebo", color=NAVY)
    y = top + 15
    for i, row in enumerate(rows):
        if last_row_green and i == len(rows) - 1:
            bg = GREEN_BG
        else:
            bg = ALT_BG if i % 2 else (1, 1, 1)
        page.draw_rect(fitz.Rect(LEFT, y, RIGHT, y + row_h), fill=bg, color=LINE, width=0.5)
        for x, val in zip(cols, row):
            page.insert_text(fitz.Point(x + 4, y + row_h - 4.5), val, fontsize=7.4,
                             fontname="helv", color=CHARCOAL)
        y += row_h
    return y


def _draw(page):
    page.draw_line(fitz.Point(LEFT, 38), fitz.Point(RIGHT, 38), color=LINE, width=0.5)
    page.insert_text(fitz.Point(LEFT, 30),
                     "AKASHYA ENTERPRISES | 1,000 MT/MONTH WOOD BIOMASS BRIQUETTES",
                     fontsize=8, fontname="hebo", color=NAVY)
    page.insert_text(fitz.Point(515, 30), "Page 7", fontsize=8, fontname="helv", color=GREY)

    page.insert_text(fitz.Point(LEFT, 56), "7 | Sensitivity: Revenue and Raw Wood Cost",
                     fontsize=11.5, fontname="hebo", color=NAVY)

    intro = (
        "The baseline selling price of Rs. 8,000/MT and wet-wood purchase price of Rs. 2,000/MT are "
        "uncontracted owner-observed scenarios (Pajson Cashew reference). Every Rs. 500/MT movement in "
        "briquette selling price changes monthly surplus by about Rs. 5.00 lakh at 1,000 MT sales; every "
        "Rs. 500/MT movement in wet-wood price changes monthly surplus by about Rs. 7.89 lakh at 1,579 MT input."
    )
    page.insert_textbox(fitz.Rect(LEFT, 62, RIGHT, 104), intro, fontsize=7.6,
                        fontname="helv", color=CHARCOAL, lineheight=1.25)

    _section(page, 116, "A | PRICE x RAW-WOOD COST SENSITIVITY - MONTHLY EBITDA (Rs. LAKH)")
    _table(page, 122, [52, 250, 348, 446],
           ["Raw wood cost", "Sale Rs. 8,000", "Sale Rs. 9,000", "Sale Rs. 10,000"],
           GRID_ROWS, row_h=15)

    _section(page, 222, "B | IMPACT OF DIFFERENT MONTHLY PRODUCTION LEVELS (AT Rs. 8,000/MT)")
    end = _table(page, 228, [52, 250, 420],
                 ["Volume", "Revenue / month", "Operating surplus"],
                 VOLUME_ROWS, row_h=15, last_row_green=True)
    page.insert_textbox(fitz.Rect(LEFT, end + 4, RIGHT, end + 34),
                        "Scale assumptions hold salaries, demand charges, administrative overhead and "
                        "baseline maintenance fixed; other expenses move broadly with tonnes sold. Real "
                        "plants experience downtime and step-change expenses, so these are planning "
                        "sensitivities, not guaranteed profits.",
                        fontsize=6.4, fontname="heit", color=GREY, lineheight=1.2)

    _section(page, 345, "C | EXTRA MOISTURE EXPOSURE (40% VS 50% INCOMING WOOD)")
    moist = (
        "At 50% incoming wood moisture the same dry-mass balance requires about 1,895 MT wet wood/month "
        "- an additional 316 MT versus the 40% case. That adds about Rs. 6.32 lakh/month in wood cost alone "
        "at Rs. 2,000/MT, plus increased drying energy. Measuring moisture on each incoming load therefore "
        "protects margin."
    )
    page.insert_textbox(fitz.Rect(LEFT, 351, RIGHT, 402), moist, fontsize=7.6,
                        fontname="helv", color=CHARCOAL, lineheight=1.25)

    _section(page, 414, "D | ILLUSTRATIVE SIMPLE INVESTMENT PAYBACK")
    payback = (
        "Total provisional cash requirement of Rs. 619.43 lakh divided by full-output EBITDA of "
        "Rs. 11.499 lakh/month (about Rs. 137.98 lakh/year) gives an illustrative simple pre-tax, "
        "pre-finance payback of about 4.49 years - only if output and the uncontracted Rs. 8,000/MT "
        "selling price hold. This is NOT IRR, lender DSCR, or a contractual return; it excludes loan "
        "costs, rent, income tax, extra drying fuel, and operational disruptions."
    )
    page.insert_textbox(fitz.Rect(LEFT, 420, RIGHT, 492), payback, fontsize=7.6,
                        fontname="helv", color=CHARCOAL, lineheight=1.25)

    page.draw_line(fitz.Point(LEFT, 805), fitz.Point(RIGHT, 805), color=LINE, width=0.5)
    page.insert_text(fitz.Point(LEFT, 818),
                     "Akashya Enterprises - Owner Planning Master DPR - 22 Nov 2026 - Anakapalli, AP",
                     fontsize=8, fontname="helv", color=GREY)
    page.insert_text(fitz.Point(455, 818), "Continued to Page 8 ->",
                     fontsize=7.5, fontname="hebo", color=NAVY)


def fix_page(page) -> bool:
    """Redraw page 7 with correct Rs. 8,000 economics. Returns True if changed."""
    if page.number != 6:
        raise ValueError("Expected page 7 (0-index page 6)")
    if _is_correct(page.get_text()):
        return False
    # Clear whatever is on the page (text + line-art) and redraw from scratch.
    page.add_redact_annot(page.rect, fill=(1, 1, 1))
    page.apply_redactions()
    _draw(page)
    text = page.get_text()
    missing = [x for x in CORRECT if x not in text]
    stale = [x for x in OBSOLETE if x in text]
    if missing or stale:
        raise RuntimeError(f"Page 7 regeneration failed self-check; missing={missing} stale={stale}")
    return True


def main():
    if not PDF.is_file():
        raise FileNotFoundError(PDF)
    doc = fitz.open(PDF)
    if len(doc) != 10:
        raise RuntimeError("Refusing to replace non-10-page DPR")
    changed = fix_page(doc[6])
    if changed:
        tmp = PDF.with_name("_tmp_corrected_akashya_page7.pdf")
        doc.save(tmp, garbage=4, deflate=True)
        doc.close()
        os.replace(tmp, PDF)
        print("PDF p7 regenerated: 600/750/850/1000 MT at Rs. 8,000/MT, Rs. 8,000 price x wood grid, 4.49-year payback")
    else:
        doc.close()
        print("PDF p7 already correct; no binary changes")


if __name__ == "__main__":
    main()