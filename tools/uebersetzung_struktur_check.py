"""Strukturvergleich deutsches Heft <-> Übersetzung.

Aufruf: python struktur_check.py <deutsch.tex> <uebersetzt.tex> <lang>
Meldet: Umgebungen, Labels, Verweise, \\item, \\fb, Formeln (als Multimenge, normalisiert: Dezimalzeichen, ; -> ,,
\\text{..} leer, Leerraum weg, \\operatorname{tr|iz} -> \\spur, \\operatorname{rank|rango|rg} -> \\rang),
falsche Dezimalzeichen je Sprache und stehen gebliebene deutsche Wörter.
"""
import re
import sys
from collections import Counter

sys.stdout.reconfigure(encoding="utf-8")


def strip_comments(s):
    return "\n".join(re.sub(r"(?<!\\)%.*$", "", z) for z in s.split("\n"))


def env_counts(s):
    return Counter(re.findall(r"\\begin\{([^}]+)\}", s))


def labels(s):
    return Counter(re.findall(r"\\label\{([^}]+)\}", s))


def refs(s):
    return Counter(re.findall(r"\\(?:eq)?ref\{([^}]+)\}", s))


DISPLAY_ENVS = r"equation\*?|align\*?|gather\*?|multline\*?"


def remove_text_args(m):
    # \text{...} (eine Ebene Klammern) leeren
    out, i = [], 0
    for t in re.finditer(r"\\(?:text|textbf|textit|mbox|mathrm\{\\?[A-Za-z]*\}?)\{", m):
        pass
    res = ""
    i = 0
    pat = re.compile(r"\\(text|mbox)\s*\{")
    while True:
        mm = pat.search(m, i)
        if not mm:
            res += m[i:]
            break
        res += m[i:mm.start()] + "\\text{"
        j, depth = mm.end(), 1
        while j < len(m) and depth:
            if m[j] == "{":
                depth += 1
            elif m[j] == "}":
                depth -= 1
            j += 1
        res += "}"
        i = j
    return res


def norm(m):
    m = remove_text_args(m)
    m = re.sub(r"\\operatorname\{(tr|iz)\}", r"\\spur", m)
    m = re.sub(r"\\operatorname\{(rank|rango|rg)\}", r"\\rang", m)
    m = m.replace("{,}", ".").replace(";", ",")
    m = re.sub(r"\\[,;!: ]", "", m)
    m = re.sub(r"\\q?quad", "", m)
    m = m.replace("~", "")
    m = re.sub(r"\s+", "", m)
    return m


def maths(s):
    found = []
    rest = s
    for pat in (r"\\begin\{(" + DISPLAY_ENVS + r")\}(.+?)\\end\{\1\}", r"(?<!\\)\\\[(.+?)\\\]"):
        rx = re.compile(pat, re.S)
        for mm in rx.finditer(rest):
            found.append(mm.group(mm.lastindex))
        rest = rx.sub(" ", rest)
    for mm in re.finditer(r"(?<![\\$])\$(?!\$)(.+?)(?<!\\)\$", rest, re.S):
        found.append(mm.group(1))
    textonly = re.sub(r"(?<![\\$])\$(?!\$)(.+?)(?<!\\)\$", " ", rest, flags=re.S)
    return found, textonly


GERMAN = re.compile(r"\b(und|nicht|eine|einen|einer|wird|werden|ist|sind|mit|für|Abschnitt|Abschnitte|Teil|Aufgabe|Abb|Heft|Hefts|der|das|dem|den|auch|oder|bei|Rechenbeispiel|Kurz gesagt|Lösung|Satz|Beweis)\b")


def main():
    de_path, tr_path, lang = sys.argv[1], sys.argv[2], sys.argv[3]
    de = strip_comments(open(de_path, encoding="utf-8").read())
    tr = strip_comments(open(tr_path, encoding="utf-8").read())
    probleme = 0

    def vergleiche(name, a, b, zeige=40):
        nonlocal probleme
        if a == b:
            print(f"OK   {name}")
            return
        nur_a, nur_b = a - b, b - a
        probleme += 1
        print(f"DIFF {name}: nur deutsch {sum(nur_a.values())}, nur übersetzt {sum(nur_b.values())}")
        for k, v in list(nur_a.items())[:zeige]:
            print(f"   - de x{v}: {k[:160]}")
        for k, v in list(nur_b.items())[:zeige]:
            print(f"   + {lang} x{v}: {k[:160]}")

    vergleiche("Umgebungen", env_counts(de), env_counts(tr))
    vergleiche("Labels", labels(de), labels(tr))
    vergleiche("Verweise", refs(de), refs(tr))
    vergleiche("\\item", Counter({"item": len(re.findall(r"\\item\b", de))}), Counter({"item": len(re.findall(r"\\item\b", tr))}))
    vergleiche("\\fb", Counter({"fb": len(re.findall(r"\\fb\{", de))}), Counter({"fb": len(re.findall(r"\\fb\{", tr))}))
    vergleiche("\\section/\\subsection/\\paragraph",
               Counter(re.findall(r"\\(section|subsection|paragraph)\*?\{", de)),
               Counter(re.findall(r"\\(section|subsection|paragraph)\*?\{", tr)))
    mde, _ = maths(de)
    mtr, ttr = maths(tr)
    vergleiche("Formeln (Multimenge, normalisiert)", Counter(norm(m) for m in mde), Counter(norm(m) for m in mtr), zeige=60)

    # Dezimalzeichen in Formeln
    if lang in ("en", "zh"):
        falsch = [m for m in mtr if "{,}" in m]
        if falsch:
            probleme += 1
            print(f"DEZ  {len(falsch)} Formeln mit {{,}} (en/zh brauchen den Punkt):")
            for m in falsch[:30]:
                print("   ", m.strip()[:160])
        semi = [m for m in mtr if re.search(r"\d\s*;|;\\?\s*-?\d", m)]
        if semi:
            print(f"HINW {len(semi)} Formeln mit ';' zwischen Zahlen (en/zh: Komma statt Semikolon?):")
            for m in semi[:30]:
                print("   ", m.strip()[:160])
    else:
        falsch = [m for m in mtr if re.search(r"(?<![\w.])\d+\.\d", m)]
        if falsch:
            probleme += 1
            print(f"DEZ  {len(falsch)} Formeln mit Dezimalpunkt (es/fr/tr brauchen {{,}}):")
            for m in falsch[:30]:
                print("   ", m.strip()[:160])
    # deutsche Wörter im Text (ohne Formeln, Labels, Verweise, Befehle)
    t = re.sub(r"\\(label|ref|eqref|begin|end|input|cite)\{[^}]*\}", " ", ttr)
    t = re.sub(r"\\[A-Za-z]+", " ", t)
    treffer = Counter(m.group(1) for m in GERMAN.finditer(t))
    if lang != "de" and treffer:
        print("WORT mögliche deutsche Wörter:", dict(treffer.most_common(20)))
    print("Probleme:", probleme)


if __name__ == "__main__":
    main()
