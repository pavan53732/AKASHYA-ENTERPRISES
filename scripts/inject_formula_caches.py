#!/usr/bin/env python3
"""Evaluate formulas and inject XML <v> value caches into XLSX workbook.

Usage:
    python scripts/inject_formula_caches.py [path_to_xlsx]

Ensures:
- All 369 formula cells across all 8 sheets have evaluated numerical values saved in XML.
- Preserves all formulas, worksheet structure, cell formatting, and relationships.
- Resolves KC-07 binary QA check for validate_dpr_consistency.py.
"""
import sys
import zipfile
from pathlib import Path
from xml.etree import ElementTree as ET
import formulas

def inject_caches(xlsx_path: Path):
    print(f"Loading formulas model from {xlsx_path}...")
    xl_model = formulas.ExcelModel().loads(str(xlsx_path)).finish()
    print("Calculating cell values...")
    res = xl_model.calculate()

    lookup = {}
    for k, v in res.items():
        s = k.strip("'")
        if '!' in s:
            sheet_part, cell_ref = s.split('!', 1)
            sheet_name = sheet_part.split(']', 1)[1] if ']' in sheet_part else sheet_part
            val = v.value[0, 0] if hasattr(v, 'value') else v
            lookup[(sheet_name.strip("'").upper(), cell_ref.upper())] = val

    M = 'http://schemas.openxmlformats.org/spreadsheetml/2006/main'
    R = 'http://schemas.openxmlformats.org/officeDocument/2006/relationships'
    NS = {'m': M}

    ET.register_namespace('', M)
    ET.register_namespace('r', R)

    with zipfile.ZipFile(xlsx_path, 'r') as zip_in:
        parts = {name: zip_in.read(name) for name in zip_in.namelist()}

    wb = ET.fromstring(parts['xl/workbook.xml'])
    relroot = ET.fromstring(parts['xl/_rels/workbook.xml.rels'])
    relationships = {r.attrib['Id']: r.attrib['Target'] for r in relroot}

    injected_count = 0

    for element in wb.findall('m:sheets/m:sheet', NS):
        name = element.attrib['name']
        rid = element.attrib.get('{' + R + '}id')
        part = relationships.get(rid, '').lstrip('/')
        if not part.startswith('xl/'):
            part = 'xl/' + part

        xml_data = parts[part]
        root = ET.fromstring(xml_data)
        sheet_injected = 0
        for cell in root.findall('.//m:sheetData/m:row/m:c', NS):
            f = cell.find('m:f', NS)
            if f is not None:
                addr = cell.attrib.get('r', '').upper()
                val = lookup.get((name.upper(), addr))
                if val is not None:
                    val_str = str(int(val)) if isinstance(val, (int, float)) and val == int(val) else str(val)
                    v = cell.find('m:v', NS)
                    if v is None:
                        v = ET.Element(f'{{{M}}}v')
                        cell.append(v)
                    v.text = val_str
                    sheet_injected += 1
                    injected_count += 1

        parts[part] = b'<?xml version="1.0" encoding="UTF-8" standalone="yes"?>\r\n' + ET.tostring(root, encoding='utf-8')
        print(f"Sheet '{name}': cached {sheet_injected} formula values")

    temp_xlsx = xlsx_path.with_name(xlsx_path.stem + '_temp.xlsx')
    with zipfile.ZipFile(temp_xlsx, 'w', compression=zipfile.ZIP_DEFLATED) as zip_out:
        for name, data in parts.items():
            zip_out.writestr(name, data)

    temp_xlsx.replace(xlsx_path)
    print(f"Successfully injected {injected_count} formula caches into {xlsx_path}!")

if __name__ == '__main__':
    target = Path(sys.argv[1] if len(sys.argv) > 1 else 'Anakapalli_1000MT_Briquette_Internal_Cost_Model.xlsx').resolve()
    inject_caches(target)
