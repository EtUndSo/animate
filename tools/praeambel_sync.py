"""Überträgt Makros ohne Argument aus praeambel.tex in die Sprachpräambeln praeambel_<lang>.tex desselben Ordners.

    python tools/praeambel_sync.py <heftordner> [--nur-zeigen]

Übernommen werden Zeilen der Form \\newcommand{\\name}{...} und \\DeclareMathOperator{\\name}{...} bzw. \\DeclareMathOperator*,
deren Makroname in der Sprachpräambel noch nicht definiert ist. Sie kommen gesammelt ans Ende der Sprachpräambel.
Grund: Die Sprachpräambeln sind Kopien; ein später in praeambel.tex ergänztes Makro fehlt sonst in den Übersetzungen.
"""
import re
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")
DEF = re.compile(r"^\\(?:newcommand|DeclareMathOperator\*?)\{\\([A-Za-z]+)\}(?!\[)")


def definitionen(text):
    """Makroname -> Zeile, für Definitionen ohne Argument am Zeilenanfang."""
    erg = {}
    for zeile in text.splitlines():
        m = DEF.match(zeile.strip())
        if m:
            erg.setdefault(m.group(1), zeile.rstrip())
    return erg


def main():
    ordner = Path(sys.argv[1])
    nur_zeigen = "--nur-zeigen" in sys.argv
    haupt = definitionen((ordner / "praeambel.tex").read_text(encoding="utf-8"))
    for p in sorted(ordner.glob("praeambel_*.tex")):
        text = p.read_text(encoding="utf-8")
        vorhanden = set(definitionen(text))
        # auch Definitionen irgendwo in der Zeile zählen (z. B. eingerückt oder mit Kommentar davor)
        vorhanden |= set(re.findall(r"\\(?:newcommand|DeclareMathOperator\*?|def)\{?\\([A-Za-z]+)", text))
        fehlend = [zeile for name, zeile in haupt.items() if name not in vorhanden]
        if not fehlend:
            print(f"{p.name}: vollständig")
            continue
        print(f"{p.name}: {len(fehlend)} fehlen: " + ", ".join(DEF.match(z.strip()).group(1) for z in fehlend))
        if not nur_zeigen:
            zusatz = "\n% --- aus praeambel.tex übernommen (tools/praeambel_sync.py) ---\n" + "\n".join(fehlend) + "\n"
            p.write_text(text.rstrip("\n") + "\n" + zusatz, encoding="utf-8")


if __name__ == "__main__":
    main()
