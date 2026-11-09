"""Lese-Nachweis aus einem Agenten-Protokoll: welche Zeilen jeder Datei per Read gelesen wurden.
Aufruf: python lese_nachweis.py <agent.jsonl> [filter-teilstring ...]
"""
import json
import sys
from pathlib import Path

log = Path(sys.argv[1])
filter_ = sys.argv[2:]
gelesen = {}
for zeile in log.read_text(encoding="utf-8").splitlines():
    try:
        d = json.loads(zeile)
    except Exception:
        continue
    msg = d.get("message") or {}
    inhalt = msg.get("content")
    if not isinstance(inhalt, list):
        continue
    for teil in inhalt:
        if teil.get("type") == "tool_use" and teil.get("name") == "Read":
            inp = teil.get("input", {})
            p = inp.get("file_path", "")
            off = inp.get("offset") or 1
            lim = inp.get("limit") or 2000
            gelesen.setdefault(p, []).append((max(off, 1), max(off, 1) + lim - 1))

for p, bereiche in sorted(gelesen.items()):
    if filter_ and not any(f.lower() in p.lower() for f in filter_):
        continue
    try:
        n = len(Path(p).read_text(encoding="utf-8", errors="replace").splitlines())
    except Exception:
        n = None
    if p.lower().endswith((".png", ".jpg", ".pdf")):
        print(f"BILD  {p}")
        continue
    gedeckt = set()
    for a, b in bereiche:
        gedeckt.update(range(a, b + 1))
    if n is None:
        print(f"?     {p}  (nicht lesbar)")
        continue
    fehlen = [i for i in range(1, n + 1) if i not in gedeckt]
    marke = "GANZ " if not fehlen else "TEIL "
    zusatz = ""
    if fehlen:
        # Lücken zusammenfassen
        luecken, start, vor = [], fehlen[0], fehlen[0]
        for i in fehlen[1:]:
            if i != vor + 1:
                luecken.append((start, vor))
                start = i
            vor = i
        luecken.append((start, vor))
        zusatz = "  fehlt: " + ", ".join(f"{a}-{b}" for a, b in luecken[:8]) + (" …" if len(luecken) > 8 else "")
    print(f"{marke} {n:5d} Z.  {p}{zusatz}")
