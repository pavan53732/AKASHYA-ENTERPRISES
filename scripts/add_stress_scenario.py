#!/usr/bin/env python3
"""Add 15-year formula-driven Scenario C to existing eight-sheet XLSX.

Uses the standard OOXML ZIP/XML parts to preserve the exact original workbook
and formatting; does NOT recreate/remove any sheet or replace the baseline.
All stress assumption rates are separate editable, source-labelled cells M43:M46.
Re-run scripts/inject_formula_caches.py after this script to calculate caches.
"""
from __future__ import annotations
from copy import deepcopy
from pathlib import Path
import os
import re
import zipfile
from xml.etree import ElementTree as ET

XLSX=Path("Anakapalli_1000MT_Briquette_Internal_Cost_Model.xlsx")
M="http://schemas.openxmlformats.org/spreadsheetml/2006/main"
R="http://schemas.openxmlformats.org/officeDocument/2006/relationships"
NS={"m":M}
ET.register_namespace("",M)
ET.register_namespace("r",R)

def q(tag): return "{"+M+"}"+tag
def col(cell): return re.match(r"[A-Z]+",cell).group()
def add_cell(row,coord,value=None,formula=None,style=None):
    at={"r":coord}
    if style is not None: at["s"]=style
    if formula is not None:
        c=ET.SubElement(row,q("c"),at)
        ET.SubElement(c,q("f")).text=formula.lstrip("=")
        ET.SubElement(c,q("v")) # formula cache injector fills it
    elif isinstance(value,(int,float)):
        c=ET.SubElement(row,q("c"),at)
        ET.SubElement(c,q("v")).text=str(value)
    else:
        at["t"]="inlineStr"
        c=ET.SubElement(row,q("c"),at)
        ins=ET.SubElement(c,q("is"))
        ET.SubElement(ins,q("t")).text=str(value)
    return c

def main():
    if not XLSX.exists(): raise FileNotFoundError(XLSX)
    with zipfile.ZipFile(XLSX) as z:
        parts={n:z.read(n) for n in z.namelist()}
    workbook=ET.fromstring(parts["xl/workbook.xml"])
    sheets=workbook.findall("m:sheets/m:sheet",NS)
    names=[e.attrib["name"] for e in sheets]
    if len(sheets)!=8 or "15-Year Cash Flow" not in names:
        raise RuntimeError("Require latest 8-sheet current GitHub workbook; aborting")
    rels=ET.fromstring(parts["xl/_rels/workbook.xml.rels"])
    relsmap={e.attrib["Id"]:e.attrib["Target"] for e in rels}
    sh=next(e for e in sheets if e.attrib["name"]=="15-Year Cash Flow")
    part=relsmap[sh.attrib["{"+R+"}id"]].lstrip("/")
    if not part.startswith("xl/"):part="xl/"+part
    root=ET.fromstring(parts[part])
    data=root.find("m:sheetData",NS)
    rows={int(e.attrib["r"]):e for e in data.findall("m:row",NS)}
    if 43 in rows and any(c.attrib.get("r")=="J57"
                           for r in rows.values() for c in r.findall("m:c",NS)):
        print("Scenario C already present, retaining source workbook")
        return
    # Never stamp over previous owner entries at the target address. The current
    # workbook carries an owner "KEY 15-YEAR STRATEGIC FINDINGS" text block in
    # A41:A44. Capture and relocate any pure column-A text out of the 41-57 band
    # (re-added below the new Scenario C table) instead of aborting or overwriting.
    relocated = []
    for n in range(41, 58):
        r = rows.get(n)
        if r is None:
            continue
        cells = r.findall("m:c", NS)
        if not cells:
            continue
        if not all(re.fullmatch(r"A\d+", c.attrib.get("r", "")) for c in cells):
            raise RuntimeError(f"Unexpected non-column-A cells in target row {n}; aborting without changes")
        for c in cells:
            tnode = c.find("m:is/m:t", NS)
            relocated.append(tnode.text if tnode is not None else None)
        data.remove(r)
    source=rows.get(25)
    if source is None: raise RuntimeError("Missing Scenario B year-one source row 25")
    original_style={col(c.attrib["r"]):c.attrib.get("s") for c in source.findall("m:c",NS)}
    def style(k):return original_style.get(k)
    def new_row(idx):
        row=ET.Element(q("row"),{"r":str(idx)})
        return row
    out=[]
    title=new_row(41)
    add_cell(title,"A41","SCENARIO C — Downside stress: sale price flat, wet wood +8%, non-wood OPEX +7% annually",style=style("A"))
    out.append(title)
    header=new_row(42)
    for c,v in zip("ABCDEFGHIJ",["Year","Util.","Finished MT","Sale INR/MT","Wetwood INR/MT","Revenue INR L","OPEX INR L","EBITDA INR L","Repl. CAPEX INR L","Cumulative INR L"]):
        add_cell(header,c+"42",v,style=style(c))
    out.append(header)
    # Parameter/source block is separate from formulas and visibly editable.
    # M46 annual fixed OPEX is derived from the owner's 15.425L/mo allocation.
    # M47 variable nonwood cost is solved from the existing Scenario B year-one
    # OPEX; same baseline and avoids independently inventing a new unit cost.
    # M48 links to the verified 40% moisture mass-balance formula.
    params={43:("Sale escalation pa",0.0),
            44:("Wet wood escalation pa",0.08),
            45:("Nonwood escalation pa",0.07),
            46:("Fixed nonwood Yr1 INR L",185.1),
            47:("Variable nonwood INR/MT",None),
            48:("Wetwood MT/finished MT",None),
            49:("Source: FINANCE/15-YEAR-INFLATION-AND-CASHFLOW-MODEL.md",None)}
    for n in range(43,58):
        row=new_row(n)
        i=n-43
        src=25+i
        expressions={
            "A":f"A{src}",
            "B":f"B{src}",
            "C":f"C{src}",
            "D":(f"D{src}" if i==0 else f"D{n-1}*(1+$M$43)"),
            "E":(f"E{src}" if i==0 else f"E{n-1}*(1+$M$44)"),
            "F":f"C{n}*D{n}/100000",
            "G":f"($M$46+C{n}*$M$47/100000)*(1+$M$45)^(A{n}-1)+C{n}*$M$48*E{n}/100000",
            "H":f"F{n}-G{n}",
            "I":f"I{src}",
            "J":(f"-'Machinery & CAPEX'!$D$42+H{n}-I{n}" if i==0 else f"J{n-1}+H{n}-I{n}")
        }
        for c in "ABCDEFGHIJ":
            add_cell(row,c+str(n),formula=expressions[c],style=style(c))
        if n in params:
            label,value=params[n]
            add_cell(row,"L"+str(n),value=label)
            if value is not None:
                add_cell(row,"M"+str(n),value=value)
            elif n==47:
                add_cell(row,"M47",formula="(G25-$M$46-C25*$M$48*E25/100000)*100000/C25")
            elif n==48:
                add_cell(row,"M48",formula="'Operating Cost'!$B$23/1000")
        out.append(row)
    # Re-add the relocated owner "KEY FINDINGS" text below the Scenario C table so
    # no owner content is lost and the layout reads A, B, C, then key findings.
    for i, text in enumerate(relocated):
        row = new_row(59 + i)
        if text is not None:
            add_cell(row, f"A{59+i}", text)
        out.append(row)
    # Append new rows in ascending numeric order; retain all prior rows.
    for row in out:
        data.append(row)
    dim=root.find("m:dimension",NS)
    if dim is not None:dim.set("ref",f"A1:M{max(57, 58+len(relocated))}")
    parts[part]=ET.tostring(root,encoding="utf-8",xml_declaration=True)
    tmp=XLSX.with_name("_tmp_akashya_stress.xlsx")
    with zipfile.ZipFile(tmp,"w",compression=zipfile.ZIP_DEFLATED) as z:
        for path,body in parts.items(): z.writestr(path,body)
    os.replace(tmp,XLSX)
    print("Added formula-driven Scenario C, rows A41:J57, inputs M43:M48 (8 sheets retained)")

if __name__=="__main__":main()
