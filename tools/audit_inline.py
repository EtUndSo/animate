"""Findet Zeilen im Fließtext (auch in :::herleitung), in denen Gleichungen inline stehen.
Ausgenommen: Frontmatter, $$-Zeilen, :::quiz, :::grafik, :::kern.
Markiert: >= 2 inline-Gleichungen in einer Zeile oder eine lange inline-Gleichung."""
import re
import sys
import pathlib

sys.stdout.reconfigure(encoding="utf-8")   # python -I ignoriert PYTHONIOENCODING
REL =re.compile(r'(=|\\le\b|\\ge\b|\\leq|\\geq|\\approx|\\Rightarrow|\\Longrightarrow)')
SKIP_BLOCKS = (':::quiz', ':::grafik', ':::kern')


def visual_len(tex):
    """Ungefähre sichtbare Länge: jeder LaTeX-Befehl (\\vec, \\lvert, \\nabla …) zählt als 1 Zeichen,
    Klammern { } und Leerzeichen zählen nicht. So verlängert die Pfeil-Notation die Messung nicht künstlich."""
    return len(re.sub(r'[{}\s]', '', re.sub(r'\\[A-Za-z]+', '#', tex)))


def audit(path):
    lines = pathlib.Path(path).read_text(encoding='utf-8').splitlines()
    fm = 0
    skip = False
    flagged = []
    for no, ln in enumerate(lines, 1):
        s = ln.strip()
        if fm < 2:
            if s == '---':
                fm += 1
            continue
        if skip:
            if s == ':::':
                skip = False
            continue
        if s.startswith(SKIP_BLOCKS):
            skip = True
            continue
        if s.startswith('$$'):
            continue
        segs = re.findall(r'(?<!\$)\$([^$]+)\$(?!\$)', ln)
        eqs = [g for g in segs if REL.search(g)]
        if len(eqs) >= 2 or any(visual_len(g) > 16 for g in eqs):
            flagged.append((no, len(eqs), s[:105]))
    return flagged


total = 0
for p in sys.argv[1:]:
    f = audit(p)
    total += len(f)
    print(f"{len(f):3d}  {pathlib.Path(p).parent.name}/{pathlib.Path(p).name}")
    for no, n, txt in f[:15]:
        print(f"        L{no} ({n} Gl.): {txt}")
print(f"\nSumme markierter Zeilen: {total}")
