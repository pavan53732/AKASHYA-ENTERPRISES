#!/usr/bin/env python3
"""Read-only AKASHYA workbook/PDF integrity gate.

Usage:
    python scripts/validate_dpr_consistency.py .
Requires pypdf for inspecting PDF content; XLSX inspection uses Python stdlib
ZIP/XML to examine saved formulas and cached results. Never edits source files.
Exit 0 only when all checks pass, exit 1 on detected defects.
"""
from __future__ import annotations
import json
import re
import sys
import zipfile
from pathlib import Path
from xml.etree import ElementTree as ET

M = "http://schemas.openxmlformats.org/spreadsheetml/2006/main"
R = "http://schemas.openxmlformats.org/officeDocument/2006/relationships"
NS = {"m": M}
PASS = "PASS"
FAIL = "FAIL"

def check(result, name, ok, explanation):
    result["checks"].append({"name": name, "status": PASS if ok else FAIL,
                             "detail": explanation})

def read_xlsx(path):
    result = {"file": str(path), "checks": [], "sheets": [],
              "formula_count": 0, "formulas_without_caches": 0}
    if not path.is_file():
        check(result, "xlsx_exists", False, "Missing latest workbook")
        return result
    with zipfile.ZipFile(path) as zipf:
        all_parts = set(zipf.namelist())
        strings = []
        if "xl/sharedStrings.xml" in all_parts:
            root = ET.fromstring(zipf.read("xl/sharedStrings.xml"))
            for si in root.findall("m:si", NS):
                strings.append("".join(t.text or "" for t in si.findall(".//m:t", NS)))
        wb = ET.fromstring(zipf.read("xl/workbook.xml"))
        relroot = ET.fromstring(zipf.read("xl/_rels/workbook.xml.rels"))
        relationships = {r.attrib["Id"]: r.attrib["Target"] for r in relroot}
        sheet_cells = {}
        for element in wb.findall("m:sheets/m:sheet", NS):
            name = element.attrib["name"]
            result["sheets"].append(name)
            rid = element.attrib.get("{" + R + "}id")
            part = relationships.get(rid, "").lstrip("/")
            if not part.startswith("xl/"):
                part = "xl/" + part
            if part not in all_parts:
                check(result, "sheet_part:" + name, False, part + " not found")
                continue
            root = ET.fromstring(zipf.read(part))
            cells = {}
            for cell in root.findall(".//m:sheetData/m:row/m:c", NS):
                address = cell.attrib.get("r", "")
                f = cell.find("m:f", NS)
                v = cell.find("m:v", NS)
                inline = cell.find("m:is", NS)
                value = v.text if v is not None else None
                if cell.attrib.get("t") == "s" and value is not None:
                    try:
                        value = strings[int(value)]
                    except (IndexError, ValueError):
                        pass
                if inline is not None:
                    value = "".join(t.text or "" for t in inline.findall(".//m:t", NS))
                if f is not None:
                    result["formula_count"] += 1
                    if v is None or not (v.text or "").strip():
                        result["formulas_without_caches"] += 1
                cells[address] = {"value": value,
                                  "formula": f.text if f is not None else None}
            sheet_cells[name] = cells
        text = " ".join(str(c["value"] or "") for cells in sheet_cells.values()
                        for c in cells.values())
        check(result, "eight_sheets", len(result["sheets"]) == 8,
              "Found " + ", ".join(result["sheets"]))
        missing = result["formulas_without_caches"]
        count = result["formula_count"]
        check(result, "saved_formula_caches", count > 0 and missing == 0,
              "%s/%s formula cells lack saved values (blank caches do not prove incorrect formulas)" %
              (missing, count))
        check(result, "strokes_not_guaranteed",
              not bool(re.search(r"220\s*[–-]\s*240\s*(?:BPM|strokes)", text, re.I)),
              "Do not assert 220–240 BPM/strokes as an OEM verified fact")
        check(result, "selling_price_not_firm_floor",
              not bool(re.search(r"(?:firm|confirmed|guaranteed)\s+(?:selling\s+)?floor", text, re.I)),
              "₹8,000/MT is an owner-observed scenario, not a signed floor")
        inspect = {
            "Machinery & CAPEX": ["A9", "D29", "D40", "D42"],
            "Assumptions": ["D6"],
            "Sources & Notes": ["A5", "A35", "C23"],
            "Summary": ["B18", "B19", "B20"],
        }
        result["key_cells"] = {
            name: {addr: cells.get(addr) for addr in addresses}
            for name, addresses in inspect.items()
            if (cells := sheet_cells.get(name)) is not None
        }
        check(result, "model_has_scenario_sheet",
              "Scenarios" in sheet_cells and "15-Year Cash Flow" in sheet_cells,
              "Both moisture sensitivity and long-term model tabs required")
    return result

def read_pdf(path):
    result = {"file": str(path), "checks": [], "pages": 0}
    if not path.is_file():
        check(result, "pdf_exists", False, "Missing latest PDF")
        return result
    try:
        from pypdf import PdfReader
        reader = PdfReader(str(path))
        pages = [(page.extract_text() or "") for page in reader.pages]
    except Exception as exc:
        check(result, "pdf_text_extraction", False, repr(exc))
        return result
    result["pages"] = len(pages)
    check(result, "ten_pages", len(pages) == 10,
          "Found %s pages" % len(pages))
    content = "\n".join(pages)
    check(result, "pdf_no_unverified_strokes",
          not bool(re.search(r"220\s*[–-]\s*240\s*(?:BPM|strokes)", content, re.I)),
          "Unverified press strokes/min in PDF")
    unsafe = re.search(
        r"10\s*[–-]\s*14\s*(?:days|day)[^\n]{0,80}(?:wet\s*chip|chip)|"
        r"wet\s*chip[^\n]{0,80}10\s*[–-]\s*14\s*days", content, re.I)
    check(result, "pdf_no_unsafe_wetchip_buffer", unsafe is None,
          "10–14 day wet-chip buffer needs explicit engineering risk review")
    check(result, "pdf_no_firm_price_floor",
          not bool(re.search(r"(?:firm|confirmed|guaranteed)\s+(?:selling\s+)?floor",
                             content, re.I)),
          "₹8,000 buyer rate must be labelled uncontracted")
    result["review_notes"] = (
        "Manually inspect PDF p9/p10 for proposed vs selected OEM equipment, "
        "buyer-specific GCV/ash/density/shatter targets, and safe site storage. "
        "Passing regex alone is NOT engineering signoff."
    )
    return result

def main():
    root = Path(sys.argv[1] if len(sys.argv) > 1 else ".").resolve()
    xlsx = read_xlsx(root / "Anakapalli_1000MT_Briquette_Internal_Cost_Model.xlsx")
    pdf = read_pdf(root / "Anakapalli_1000MT_Wood_Briquette_Internal_DPR.pdf")
    checks = xlsx["checks"] + pdf["checks"]
    passed = bool(checks) and all(item["status"] == PASS for item in checks)
    result = {"repo_root": str(root), "status": PASS if passed else FAIL,
              "xlsx": xlsx, "pdf": pdf}
    print(json.dumps(result, indent=2, ensure_ascii=False))
    return 0 if passed else 1

if __name__ == "__main__":
    sys.exit(main())
