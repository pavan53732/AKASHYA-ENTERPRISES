#!/usr/bin/env python3
"""Rollback-safe repair of the latest AKASHYA 8-sheet XLSX and 10-page PDF.

Usage:
    python -m pip install formulas pymupdf pypdf
    python scripts/run_binary_repairs.py

Rolls back original binary bytes if any of the validators fails.
"""
from __future__ import annotations
import hashlib
import os
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile

ROOT = Path(__file__).resolve().parent.parent
FILES = [
    ROOT / "Anakapalli_1000MT_Briquette_Internal_Cost_Model.xlsx",
    ROOT / "Anakapalli_1000MT_Wood_Briquette_Internal_DPR.pdf",
]
STEPS = [
    "scripts/add_stress_scenario.py",
    "scripts/inject_formula_caches.py",
    "scripts/rebuild_master_dpr.py",
    "scripts/repair_page7_scale.py",
    "scripts/validate_dpr_consistency.py",
    "scripts/audit_369_formulas.py",
    "scripts/inspect_pdf_layout.py",
]


def checksum(p):
    h = hashlib.sha256()
    with p.open("rb") as fd:
        for chunk in iter(lambda: fd.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest().upper()


def main():
    for p in FILES:
        if not p.is_file():
            raise FileNotFoundError(p)
    before = {p: checksum(p) for p in FILES}
    env = dict(os.environ, PYTHONIOENCODING="utf-8", PYTHONUTF8="1")
    with tempfile.TemporaryDirectory(prefix="akashya_repair_") as directory:
        temp = Path(directory)
        for p in FILES:
            shutil.copy2(p, temp / p.name)
        try:
            for step in STEPS:
                cmd = [sys.executable, step]
                if step.endswith("validate_dpr_consistency.py"):
                    cmd.append(".")
                print("RUN", step, flush=True)
                subprocess.run(cmd, cwd=ROOT, check=True, env=env)
        except BaseException:
            for p in FILES:
                shutil.copy2(temp / p.name, p)
            for p in FILES:
                assert checksum(p) == before[p], "Rollback hash mismatch " + p.name
            print("FAIL: all original binaries restored unchanged", file=sys.stderr)
            raise
    print("SUCCESS: Excel stress C and PDF page7 repaired and tested")
    for p in FILES:
        print(p.name, checksum(p))
    return 0


if __name__ == "__main__":
    sys.exit(main())