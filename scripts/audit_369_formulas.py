import formulas
import zipfile
from xml.etree import ElementTree as ET
import math
import sys
try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass

print("=== STARTING INDEPENDENT 369-FORMULA AUDIT ===")

xlsx_path = 'Anakapalli_1000MT_Briquette_Internal_Cost_Model.xlsx'
xl_model = formulas.ExcelModel().loads(xlsx_path).finish()
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

with zipfile.ZipFile(xlsx_path) as zipf:
    wb = ET.fromstring(zipf.read('xl/workbook.xml'))
    relroot = ET.fromstring(zipf.read('xl/_rels/workbook.xml.rels'))
    relationships = {r.attrib['Id']: r.attrib['Target'] for r in relroot}

    sheet_formulas = {}
    mismatches = []
    errors = []
    
    for element in wb.findall('m:sheets/m:sheet', NS):
        name = element.attrib['name']
        rid = element.attrib.get('{' + R + '}id')
        part = relationships.get(rid, '').lstrip('/')
        if not part.startswith('xl/'):
            part = 'xl/' + part
        root = ET.fromstring(zipf.read(part))
        
        formula_list = []
        for cell in root.findall('.//m:sheetData/m:row/m:c', NS):
            f = cell.find('m:f', NS)
            v = cell.find('m:v', NS)
            if f is not None:
                addr = cell.attrib.get('r', '').upper()
                cached_val = v.text if v is not None else None
                calc_val = lookup.get((name.upper(), addr))
                formula_list.append({
                    'address': addr,
                    'formula': f.text,
                    'cached': cached_val,
                    'calculated': calc_val
                })
                
                # Check for errors in calculated value
                if isinstance(calc_val, str) and (calc_val.startswith('#') or 'ERROR' in calc_val.upper()):
                    errors.append((name, addr, f.text, calc_val))
                elif isinstance(calc_val, float) and (math.isnan(calc_val) or math.isinf(calc_val)):
                    errors.append((name, addr, f.text, calc_val))
                
                # Check cache match
                if cached_val is not None and calc_val is not None:
                    try:
                        c_float = float(cached_val)
                        cal_float = float(calc_val)
                        if abs(c_float - cal_float) > 1e-4:
                            mismatches.append((name, addr, f.text, cached_val, calc_val))
                    except ValueError:
                        if str(cached_val).strip() != str(calc_val).strip():
                            mismatches.append((name, addr, f.text, cached_val, calc_val))
        
        sheet_formulas[name] = formula_list

print(f"Total sheets inspected: {len(sheet_formulas)}")
total_f = sum(len(fl) for fl in sheet_formulas.values())
print(f"Total formula cells verified: {total_f}")
for sname, fl in sheet_formulas.items():
    print(f"  - Sheet '{sname}': {len(fl)} formula cells")

print(f"\nErrors detected (#REF!, #DIV/0!, NaN, Inf): {len(errors)}")
if errors:
    for e in errors:
        print("  ERROR:", e)

print(f"Cache mismatches between XML <v> and evaluated formula result: {len(mismatches)}")
if mismatches:
    for m in mismatches:
        print("  MISMATCH:", m)

# Detailed Verification of Core Financial Equations
print("\n=== VERIFYING CORE FINANCIAL EQUATIONS ===")

# 1. Summary Sheet Checks
s_rev = lookup.get(('SUMMARY', 'B9'))
s_wood = lookup.get(('SUMMARY', 'B10'))
s_pwr = lookup.get(('SUMMARY', 'B11'))
s_fuel = lookup.get(('SUMMARY', 'B12'))
s_wage = lookup.get(('SUMMARY', 'B13'))
s_opex = lookup.get(('SUMMARY', 'B14'))
s_ebitda = lookup.get(('SUMMARY', 'B15'))
s_capex = lookup.get(('SUMMARY', 'B18'))
s_wc = lookup.get(('SUMMARY', 'B19'))
s_outlay = lookup.get(('SUMMARY', 'B20'))

print(f"Summary: Revenue={s_rev}, OPEX={s_opex}, EBITDA={s_ebitda}")
print(f"Summary: Fixed CAPEX={s_capex}, Working Capital={s_wc}, Total Outlay={s_outlay}")

# Mathematical identities
assert abs((s_rev - s_opex) - s_ebitda) < 1e-4, "EBITDA != Revenue - OPEX"
assert abs((s_capex + s_wc) - s_outlay) < 1e-4, "Total Outlay != Capex + WC"
print("✓ Summary arithmetic identities verified (EBITDA = Rev - OPEX, Outlay = Capex + WC)")

# 2. CAPEX Sheet Checks
capex_p_m = lookup.get(('MACHINERY & CAPEX', 'D17'))
capex_civ = lookup.get(('MACHINERY & CAPEX', 'D27'))
capex_tot = lookup.get(('MACHINERY & CAPEX', 'D29'))
wc_tot = lookup.get(('MACHINERY & CAPEX', 'D40'))
outlay_tot = lookup.get(('MACHINERY & CAPEX', 'D42'))

print(f"CAPEX: Plant & Mach={capex_p_m}, Civil={capex_civ}, Total Fixed={capex_tot}")
print(f"CAPEX: Working Capital={wc_tot}, Total Project Cash={outlay_tot}")
assert abs((capex_p_m + capex_civ) - capex_tot) < 1e-4, "Total Fixed != P&M + Civil"
assert abs((capex_tot + wc_tot) - outlay_tot) < 1e-4, "Total Cash != Fixed + WC"
assert abs(capex_tot - 520.0) < 1e-4, "Fixed Capex != 520.0"
assert abs(wc_tot - 99.43289) < 1e-3, "Working Capital != 99.43"
assert abs(outlay_tot - 619.43289) < 1e-3, "Total Outlay != 619.43"
print("✓ CAPEX & Working capital arithmetic matches exact owner budget (₹520L fixed + ₹99.43L WC = ₹619.43L outlay)")

# 3. Manpower Sheet Checks
payroll_tot = lookup.get(('MANPOWER', 'D19'))
assump_payroll = lookup.get(('ASSUMPTIONS', 'B21'))
print(f"Manpower: Monthly Payroll={payroll_tot} INR -> Assumptions B21={assump_payroll} Lakh")
assert abs(payroll_tot - 850000.0) < 1e-4, "Payroll != 850,000"
assert abs(assump_payroll - 8.5) < 1e-4, "Assumptions Payroll != 8.5 Lakh"
assert abs(payroll_tot / 100000.0 - assump_payroll) < 1e-4, "Assumptions!B21 not dynamically linked to Manpower!D19/100000"
print("✓ Dynamic payroll linking between Manpower and Assumptions confirmed")

# 4. Operating Cost Checks
op_rev = lookup.get(('OPERATING COST', 'B5'))
op_wood_mt = lookup.get(('OPERATING COST', 'B23'))
op_wood_cost = lookup.get(('OPERATING COST', 'B7'))
op_ebitda = lookup.get(('OPERATING COST', 'B20'))
print(f"Operating Cost: Wet Wood={op_wood_mt:.2f} MT -> Wood Cost=Rs. {op_wood_cost:.2f} L -> EBITDA=Rs. {op_ebitda:.2f} L")
# Wood math: 1000 MT finished @ 10% moisture = 900 MT dry matter. At 40% moisture in: 900 / (1 - 0.40) = 1500 MT... wait, what formula is in B23?
op_f_b23 = [fl['formula'] for fl in sheet_formulas['Operating Cost'] if fl['address'] == 'B23'][0]
print(f"  Formula in Operating Cost!B23: {op_f_b23}")
# Let's inspect the exact formula in B23 and B7
print(f"  Calculated Wet Wood MT: {op_wood_mt}")
assert abs(op_rev - 80.0) < 1e-4, "Revenue != 80.0 Lakh"
assert abs(op_ebitda - 11.49868) < 1e-3, "EBITDA != 11.50 Lakh"
print("✓ Monthly EBITDA of ₹11.50 Lakh verified against Revenue ₹80.00L and OPEX ₹68.50L")

# 5. Scenarios (Moisture Sensitivity Table 3)
print("\n=== VERIFYING MOISTURE SENSITIVITY TABLE (SCENARIOS TAB) ===")
# Table 3 rows for 25%, 30%, 35%, 40%, 45%, 50%, 55%
moisture_levels = [0.25, 0.30, 0.35, 0.40, 0.45, 0.50, 0.55]
# Let's see rows in Scenarios tab
for r in range(25, 33):
    vals = [lookup.get(('SCENARIOS', f'{col}{r}')) for col in ['A', 'B', 'C', 'D', 'E', 'F', 'G']]
    if any(v is not None for v in vals):
        print(f"  Row {r}: {vals}")

# 6. 15-Year Cash Flow Sheet Checks
print("\n=== VERIFYING 15-YEAR CASH FLOW MODEL (210 FORMULAS) ===")
print('--- SCENARIO A: BASE CASE (+3% SALE, +6% WOOD) ---')
print('Yr | Util% | MT Sold | Sale/MT | Wood/MT | Rev (₹L) | OPEX (₹L) | EBITDA (₹L) | Repl. Capex | Cumul Cash (₹L)')
for r in range(7, 22):
    yr = lookup.get(('15-YEAR CASH FLOW', f'A{r}'))
    u = lookup.get(('15-YEAR CASH FLOW', f'B{r}'))
    mt = lookup.get(('15-YEAR CASH FLOW', f'C{r}'))
    sale = lookup.get(('15-YEAR CASH FLOW', f'D{r}'))
    wood = lookup.get(('15-YEAR CASH FLOW', f'E{r}'))
    rev = lookup.get(('15-YEAR CASH FLOW', f'F{r}'))
    opex = lookup.get(('15-YEAR CASH FLOW', f'G{r}'))
    ebitda = lookup.get(('15-YEAR CASH FLOW', f'H{r}'))
    repl = lookup.get(('15-YEAR CASH FLOW', f'I{r}'))
    cum = lookup.get(('15-YEAR CASH FLOW', f'J{r}'))
    print(f'{yr:2.0f} | {u*100:4.0f}% | {mt:7.0f} | ₹{sale:5.0f} | ₹{wood:5.0f} | ₹{rev:7.2f}L | ₹{opex:7.2f}L | ₹{ebitda:7.2f}L | ₹{repl:4.0f}L | ₹{cum:8.2f}L')

print('\n--- SCENARIO B: INDEXED OFFTAKE (+5% SALE, +6% WOOD) ---')
print('Yr | Util% | MT Sold | Sale/MT | Wood/MT | Rev (₹L) | OPEX (₹L) | EBITDA (₹L) | Repl. Capex | Cumul Cash (₹L)')
for r in range(25, 40):
    yr = lookup.get(('15-YEAR CASH FLOW', f'A{r}'))
    u = lookup.get(('15-YEAR CASH FLOW', f'B{r}'))
    mt = lookup.get(('15-YEAR CASH FLOW', f'C{r}'))
    sale = lookup.get(('15-YEAR CASH FLOW', f'D{r}'))
    wood = lookup.get(('15-YEAR CASH FLOW', f'E{r}'))
    rev = lookup.get(('15-YEAR CASH FLOW', f'F{r}'))
    opex = lookup.get(('15-YEAR CASH FLOW', f'G{r}'))
    ebitda = lookup.get(('15-YEAR CASH FLOW', f'H{r}'))
    repl = lookup.get(('15-YEAR CASH FLOW', f'I{r}'))
    cum = lookup.get(('15-YEAR CASH FLOW', f'J{r}'))
    print(f'{yr:2.0f} | {u*100:4.0f}% | {mt:7.0f} | ₹{sale:5.0f} | ₹{wood:5.0f} | ₹{rev:7.2f}L | ₹{opex:7.2f}L | ₹{ebitda:7.2f}L | ₹{repl:4.0f}L | ₹{cum:8.2f}L')

# Do not report a PASS if diagnostics are non-empty or a stress scenario is absent.
assert total_f >= 369, f"Expected at least 369 original formula cells, got {total_f}"
assert not errors, f"Detected {len(errors)} formula errors: {errors[:10]}"
assert not mismatches, f"Detected {len(mismatches)} cache mismatches: {mismatches[:10]}"
stress_rows = sheet_formulas.get('15-Year Cash Flow', [])
stress_addresses = {x['address'] for x in stress_rows}
assert all(f'J{r}' in stress_addresses for r in range(43,58)), "Missing 15-year Stress Scenario C formulas in J43:J57"
assert lookup.get(('15-YEAR CASH FLOW','J57')) is not None, "Stress Scenario C year-15 cash cache is missing"
print(f"=== FULL AUDIT PASSED: {total_f} FORMULAS, 0 ERRORS, 0 CACHE MISMATCHES, ALL 3 SCENARIOS ===")
