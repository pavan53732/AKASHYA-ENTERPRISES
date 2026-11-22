#!/usr/bin/env python3
"""Repair stale 9000-rupee scale numbers on page 7 of the *current* 10-page DPR.

Preserves every other page. Hard-fails if the known row anchors are not found
rather than claiming success after a silent missed redaction. Designed to run
AFTER scripts/rebuild_master_dpr.py, since that rebuild preserves old page 7.
"""
from __future__ import annotations
import os
from pathlib import Path
import fitz

PDF = Path("Anakapalli_1000MT_Wood_Briquette_Internal_DPR.pdf")
# Monthly revenue and EBITDA, in lakh, holding the original PDF's non-sales
# operating costs unchanged. Ref: FINANCE/OWNER-COST-RECONCILIATION.md.
ROWS = [
    (600, 54.00, 6.23, 48.00, 0.23),
    (750, 67.50, 11.96, 60.00, 4.46),
    (850, 76.50, 15.77, 68.00, 7.27),
    (1000, 90.00, 21.50, 80.00, 11.50),
]

def _row_words(page, ytop, xlo, xhi):
    return [w for w in page.get_text("words")
            if abs(w[1]-ytop) < 5 and xlo <= w[0] <= xhi]

def _text_in_row(page, ytop, xlo, xhi):
    return " ".join(str(w[4]) for w in _row_words(page, ytop, xlo, xhi))

def _fit(page, bbox, message, size=8.0):
    x0,y0,x1,y1=bbox
    while size >= 6:
        if fitz.get_text_length(message, fontname="helv", fontsize=size) <= x1-x0-1:
            page.insert_text((x0, y0+size+1), message,
                             fontsize=size, fontname="helv", color=(0.11,0.11,0.11))
            return
        size-=0.3
    raise RuntimeError("Page 7 corrected text too wide: "+message)

def fix_page(page):
    """Return True if a stale page was corrected; False if already corrected."""
    if page.number != 6:
        raise ValueError("Expected page 7 (0-index page 6)")
    words=page.get_text("words")
    pending=[]
    for volume,old_rev,old_ebitda,new_rev,new_ebitda in ROWS:
        hits=[w for w in words if w[4]==str(volume) and 50<w[0]<125 and 280<w[1]<380]
        if len(hits)!=1:
            raise RuntimeError("Could not locate exactly one scale row for %s MT" % volume)
        y=hits[0][1]
        rev=_text_in_row(page,y,180,335)
        margin=_text_in_row(page,y,365,535)
        if f"{new_rev:.2f}" in rev and f"{new_ebitda:.2f}" in margin:
            continue
        if f"{old_rev:.2f}" not in rev or f"{old_ebitda:.2f}" not in margin:
            raise RuntimeError(f"Unexpected source in {volume}-MT row: revenue={rev!r} EBITDA={margin!r}")
        # Redact only the 2 numeric cells, keeping the original MT volume and
        # all other table row content unmodified.
        page.add_redact_annot(fitz.Rect(185,y-1.5,330,y+11.5),fill=(1,1,1))
        page.add_redact_annot(fitz.Rect(374,y-1.5,535,y+11.5),fill=(1,1,1))
        pending.append((y,new_rev,new_ebitda))
    if not pending:
        # Already corrected; confirm stale 2026 payback language absent.
        content=page.get_text()
        if "627.43" in content or "257.98" in content or "2.43 years" in content:
            raise RuntimeError("Scale rows corrected but old 9000-based payback remains")
        return False

    # Intro line contains old "9,000" for the baseline, independent from the
    # genuinely legitimate 9000 column in the *selling-price sensitivity* grid.
    page.add_redact_annot(fitz.Rect(53,98,544,112.5),fill=(1,1,1))
    # Entire old payback paragraph; do not leave a patchwork old line behind.
    page.add_redact_annot(fitz.Rect(53,537,544,608),fill=(1,1,1))
    page.apply_redactions(images=0,graphics=0,text=0)

    _fit(page,(54.2,98.5,542,114),
         "Briquettes Rs. 8,000/MT and wet wood Rs. 2,000/MT are uncontracted owner scenarios. Every Rs. 500/MT movement in",7.7)
    for y,new_rev,new_ebitda in pending:
        _fit(page,(192.5,y,329,y+13),f"Rs. {new_rev:.2f} lakh",7.8)
        _fit(page,(379.6,y,531,y+13),f"Rs. {new_ebitda:.2f} lakh",7.8)

    paragraph=(
        "At 1,000 saleable MT/month, estimated total initial cash is Rs. 619.43 lakh and "
        "full-output EBITDA is Rs. 11.499 lakh/month, or about Rs. 137.98 lakh/year. "
        "Illustrative simple pre-tax, pre-finance payback is about 4.49 years only if "
        "output and uncontracted Rs. 8,000/MT selling prices hold. This is NOT "
        "IRR, lender DSCR, or a contractual return; excludes loan costs, rent, "
        "income tax, extra drying fuel, and operational disruptions."
    )
    box=fitz.Rect(54.2,538.0,542.5,608)
    leftover=page.insert_textbox(box,paragraph,fontsize=8.0,
                                  fontname="helv",lineheight=1.25,
                                  color=(0.11,0.11,0.11))
    if leftover < 0:
        raise RuntimeError("Corrected p7 payback body overflowed: %s" % leftover)

    text=page.get_text()
    for bad in ("Rs. 54.00 lakh","Rs. 90.00 lakh","627.43","257.98","2.43 years"):
        if bad in text: raise RuntimeError("Obsolete page7 claim remains: "+bad)
    for target in ("Rs. 48.00 lakh","Rs. 60.00 lakh","Rs. 68.00 lakh",
                   "Rs. 80.00 lakh","Rs. 0.23 lakh","Rs. 11.50 lakh","4.49"):
        if target not in text: raise RuntimeError("Missing corrected p7 figure: "+target)
    return True

def main():
    if not PDF.is_file(): raise FileNotFoundError(PDF)
    doc=fitz.open(PDF)
    if len(doc)!=10: raise RuntimeError("Refusing to replace non-10-page DPR")
    changed=fix_page(doc[6])
    if changed:
        temp=PDF.with_name("_tmp_corrected_akashya_page7.pdf")
        doc.save(temp,garbage=4,deflate=True)
        doc.close()
        os.replace(temp,PDF)
        print("PDF p7 repaired: 600/750/850/1000 MT revenues and EBITDA, Rs. 8,000 scenario, 4.49-year payback")
    else:
        doc.close()
        print("PDF p7 already corrected; no binary changes")

if __name__ == "__main__": main()
