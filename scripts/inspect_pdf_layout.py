import sys
from pathlib import Path

import fitz


EXPECTED_PAGES = 10
DPR_PATH = Path(__file__).resolve().parents[1] / "Anakapalli_1000MT_Wood_Briquette_Internal_DPR.pdf"


def text_lines(page):
    flags = fitz.TEXTFLAGS_DICT & ~fitz.TEXT_PRESERVE_IMAGES
    for block in page.get_text("dict", flags=flags)["blocks"]:
        for line in block["lines"]:
            text = "".join(span["text"] for span in line["spans"]).strip()
            if text:
                yield fitz.Rect(line["bbox"]), text


def inspect_layout(pdf_path):
    """Return a failing exit status for missing pages or detected layout defects."""
    failed_pages = 0
    with fitz.open(pdf_path) as doc:
        page_count = len(doc)
        print(f"Total pages: {page_count} (expected {EXPECTED_PAGES})")
        for page_number, page in enumerate(doc, start=1):
            rect = page.rect
            lines = list(text_lines(page))
            outside = [
                text for bounds, text in lines
                if bounds.x0 < 30 or bounds.x1 > rect.width - 20
                or bounds.y0 < 20 or bounds.y1 > rect.height - 15
            ]
            overlaps = []
            for index, (first_bounds, first_text) in enumerate(lines):
                for second_bounds, second_text in lines[index + 1:]:
                    intersection = first_bounds & second_bounds
                    if intersection.width > 5 and intersection.height > 5:
                        overlaps.append((first_text, second_text))

            failed = not lines or bool(outside or overlaps)
            failed_pages += failed
            status = "FAIL" if failed else "PASS"
            print(
                f"Page {page_number:2d}: {status} | {rect.width:.1f} x {rect.height:.1f} pt"
                f" | Text lines: {len(lines)} | Overlaps: {len(overlaps)}"
                f" | Out of bounds: {len(outside)}"
            )
            for text in outside:
                print(f"  Outside layout margins: {text[:70]!r}")
            for first, second in overlaps:
                print(f"  Overlap: {first[:40]!r} / {second[:40]!r}")

    failed = page_count != EXPECTED_PAGES or failed_pages > 0
    status = "FAIL" if failed else "PASS"
    print(f"\n=== LAYOUT INSPECTION: {status} ({page_count - failed_pages}/{page_count} pages passed) ===")
    return int(failed)


if __name__ == "__main__":
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    raise SystemExit(inspect_layout(DPR_PATH))
