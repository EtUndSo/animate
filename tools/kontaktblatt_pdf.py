"""Kontaktblatt aus den Vektor-PDFs der Szenen eines Hefts (ohne neu zu exportieren): so, wie die Bilder im Heft stehen.

    python tools/kontaktblatt_pdf.py <heftordner>/abb/<sprache> <ausgabeordner> [<praefix>|<name1,name2,…>]

Ohne drittes Argument alle *.pdf des Ordners (bis 10.11.2026: nur k2*); sonst alle <praefix>*.pdf (z. B. k3) oder genau
die genannten Namen. Schreibt kontakt_1.png, kontakt_2.png … (16 Bilder je Blatt, Name rot darüber; braucht PyMuPDF).
Für die SVGs der Website (wahlweise mit Export vorher) gibt es tools/szenen_ansehen.py.
"""
import sys
from pathlib import Path
import fitz

ordner = Path(sys.argv[1])
aus = Path(sys.argv[2])
aus.mkdir(parents=True, exist_ok=True)
auswahl = sys.argv[3] if len(sys.argv) > 3 else ""
if "," in auswahl:
    pdfs = [ordner / f"{n.strip()}.pdf" for n in auswahl.split(",") if n.strip()]
else:
    pdfs = sorted(ordner.glob(f"{auswahl}*.pdf"))
spalten, zeilen = 4, 4
breite = 420
pro_blatt = spalten * zeilen
for b in range(0, len(pdfs), pro_blatt):
    gruppe = pdfs[b:b + pro_blatt]
    bilder = []
    for p in gruppe:
        doc = fitz.open(p)
        seite = doc[0]
        z = breite / seite.rect.width
        pix = seite.get_pixmap(matrix=fitz.Matrix(z, z), alpha=False)
        bilder.append((p.stem, pix))
    hoehe = max(pix.height for _, pix in bilder) + 18
    ziel = fitz.Pixmap(fitz.csRGB, fitz.IRect(0, 0, spalten * (breite + 10), zeilen * hoehe), False)
    ziel.clear_with(200)
    for m, (name, pix) in enumerate(bilder):
        pix.set_origin((m % spalten) * (breite + 10), (m // spalten) * hoehe + 18)
        ziel.copy(pix, pix.irect)
    datei = aus / f"kontakt_{b // pro_blatt + 1}.png"
    ziel.save(datei)
    # Namen dazuschreiben
    d = fitz.open()
    s = d.new_page(width=ziel.width, height=ziel.height)
    s.insert_image(s.rect, filename=str(datei))
    for m, (name, _) in enumerate(bilder):
        s.insert_text(((m % spalten) * (breite + 10) + 4, (m // spalten) * hoehe + 13), name, fontsize=12, color=(0.6, 0, 0))
    s.get_pixmap(alpha=False).save(datei)
    print(datei, [n for n, _ in bilder])
