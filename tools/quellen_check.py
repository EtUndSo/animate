"""Prüft Artikel auf Hinweise auf Vorlagen und Lehrveranstaltungen (ERKLAER_PROMPT §5.7, Vorgabe des Users vom 22.10.2026:
keine Verweise auf Skript, Vorlesung, Übung, Praktikum, Tutorium, Klausur, Folien, Seiten-, Bild-, Tabellen-, Kapitel-,
Abschnitts- oder Gleichungsnummern einer Vorlage, Lehrveranstaltungs- oder Hochschulnamen, Modulkürzel und interne
Werkzeuge wie das Zahlenwerk).
Gibt jede Fundstelle aus und endet mit Code 1, wenn es welche gibt. Ohne Argumente prüft es alle Dateien in content/.
Aufruf: python -I tools/quellen_check.py [<artikel.md> …]"""
import re
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")
REPO = Path(__file__).resolve().parent.parent
MUSTER = {
    "Skript": r"[Ss]kript",
    "Vorlesung": r"[Vv]orlesung",
    "Übung": r"\bÜbung|übungs|Uebung",
    "Praktikum": r"[Pp]raktik",
    "Tutorium": r"[Tt]utori",
    "Klausur": r"[Kk]lausur",
    "Folie": r"\bFolie",
    "Seite": r"\bS\.\s?\d|\bSeite\s\d",
    "Bild-Nr": r"\bBild(er)?\s\d+\.\d+|\bAbb\.\s?\d+\.\d+",
    "Tabelle-Nr": r"\bTabelle\s\d+\.\d+",
    "Abschnitt-Nr": r"\bAbschnitt\s\d+(\.\d+)+",
    "Kapitel": r"\bKapitel|\bKap\.\s?\d",
    "Gleichung-Nr": r"\b(Gl\.|Gleichung(en)?)\s\(?\d+\.\d+",
    "Kurs": r"GET-?1|\bMiNa\b|RWTH|Lehrstuhl|Formelsammlung|KGÜ|Hilfsfolie|\bProf\.|Dozent",
    "Modulkürzel": r"\bET\s?[1-4]\b|\bGEMB\b|\bHöMa\b|\bHM\s?[1-4]\b|Höhere(n)? Mathematik\s(I{1,3}|[1-4])\b",
    "Veranstaltung": r"\bKurs(es|e)?\b|Schaltungstechnik\s?\d|\bModul(e|en|s)?\b|\b(späteren|nächsten|vorigen|früheren|zweiten|dritten|vierten|fünften|sechsten) Semester",
    "Satz-Nr": r"\b(Satz|Definition|Lemma|Korollar|Bemerkung|Formel)\s\(?([A-Z]\d+|\d+\.\d+)(\.\d+)*\)?",
    "Seitenbezug": r"derselben Seite|Seite später|eine Seite (früher|vorher|davor)",
    "intern": r"Zahlenwerk",
}

dateien = [Path(a) for a in sys.argv[1:]] or sorted((REPO / "content").rglob("*.md"))
n = 0
for p in dateien:
    for nr, zeile in enumerate(p.read_text(encoding="utf-8").split("\n"), 1):
        if zeile.startswith(("pfad:", "order:")):                # Gliederung der Website, kein Quellenbezug
            continue
        zeile = re.sub(r"\]\([^)]*\)|https?://\S+", "]", zeile)   # Linkziele und Adressen nicht prüfen
        for name, rx in MUSTER.items():
            for m in re.finditer(rx, zeile):
                a, b = max(0, m.start() - 50), min(len(zeile), m.end() + 50)
                print(f"{p.as_posix()}:{nr}: [{name}] …{zeile[a:b]}…")
                n += 1
sys.exit(1 if n else 0)
