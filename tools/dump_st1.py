"""Volltext des Skripts zu Schaltungstechnik 1 seitenweise in eine Textdatei (für grep); NUL-Zeichen entfernt.
Die Ausgabe liegt bewusst außerhalb des Repos, weil sie den Skripttext enthält. Muster: dump_get1.py."""
import sys
import pathlib
import fitz

sys.stdout.reconfigure(encoding="utf-8")
src = pathlib.Path(r"C:\Bücher\EtUndSo\3.Semester\ST1\Vorlesung\Skript.pdf")
out = pathlib.Path(r"C:\Bücher\EtUndSo\_volltext\st1_clean.txt")
out.parent.mkdir(parents=True, exist_ok=True)
doc = fitz.open(src)
parts = []
for i, page in enumerate(doc, 1):
    txt = page.get_text("text").replace("\x00", "")
    parts.append(f"=== Seite {i} ({len(txt)} chars) ===\n{txt}")
out.write_text("\n".join(parts), encoding="utf-8")
print("Seiten:", doc.page_count, "->", out)
toc = doc.get_toc()
for lvl, title, page in toc:
    if lvl <= 2:
        print("  " * (lvl - 1) + f"{title}  (S. {page})")
