"""Themenkarte erzeugen: notizen/themenkarte.md = jedes Thema -> Bereich, Heft, Abschnitt, in dem es vollständig erklärt ist.

Aufruf (vom Repo-Root):  python tools/themenkarte.py            schreibt notizen/themenkarte.md neu
                         python tools/themenkarte.py --pruefen  zeigt nur die Zahlen

Quelle sind die deutschen Hefte aller Module aus tools/heft_zu_artikel.py (MODULE[...]): je Heft die nummerierten
\\section- und \\subsection-Titel, nummeriert wie im PDF und auf der Website. Ungeschriebene Hefte fehlen. Der Teil
zwischen den Markierungen „von Hand“ bleibt beim Neuerzeugen erhalten (geplante Themen, Zuständigkeiten, die noch kein
Heft haben). Grund (User, 06.11.2026): „Inhalte nicht mehrfach auf der Webseite vollständig erklären“.
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "tools"))
import heft_zu_artikel as H  # noqa: E402

ZIEL = ROOT / "notizen" / "themenkarte.md"
HAND_AUF, HAND_ZU = "<!-- von Hand: Anfang -->", "<!-- von Hand: Ende -->"

KOPF = """# Themenkarte: Wo ist welches Thema vollständig erklärt?

Regel des Users (06.11.2026): „Inhalte nicht mehrfach auf der Webseite vollständig erklären“. Jedes Thema hat genau einen
Ort, an dem es vollständig erklärt wird. Andere Hefte setzen es voraus, fassen es höchstens in ein bis drei Sätzen zusammen
und verweisen mit Link darauf.

## So benutzt du die Karte (Schreib-Agenten)
1. **Vor dem Schreiben nachsehen:** Für jeden Begriff deines Lernpfad-Eintrags mit Grep in dieser Datei suchen (Wortstamm,
   auch englisch), nicht die ganze Datei lesen. Jede Zeile beginnt mit der Verweis-Wendung des Abschnitts.
2. **Gefunden:** nicht neu erklären. Im Heft steht dann „Was du dafür brauchst“ mit einer kurzen, selbsttragenden
   Zusammenfassung (Definition, eine Formel, ein Mini-Beispiel) und dem Verweis in genau dieser Form; auf der Website wird er
   zum Link auf Artikel und Abschnitt:
   - ML-Grundlagen: „Grundlagen 1, Abschnitt 13.5“, ML-Pfad: „Teil 2, Abschnitt 3.1“ (Teil N = Lernpfad-Heft T(N+7));
   - Programmieren: „Programmieren, Python 2, Abschnitt 3.1“ (später „Programmieren, C 1, …“, „Programmieren, C++ 1, …“);
   - Linux und Kommandozeile: „Linux 2, Abschnitt 3.1“;
   - mehrere: „Grundlagen 1, Abschnitte 10.1 und 11.4“; das ganze Heft: „Grundlagen 1“.
   Übersetzungen: notizen/heft_uebersetzung.md, Abschnitt „Verweise auf andere Hefte“. Für die Uni-Module (Elektrotechnik,
   Höhere Mathematik) gibt es noch keine automatische Link-Wendung über Modulgrenzen; dort den Abschnitt im Bericht nennen.
3. **Nicht gefunden:** Du erklärst es vollständig, wenn es zu deinem Heft gehört (siehe „Zuständigkeiten“ unten). Gehört es in
   einen anderen Bereich, der noch kein Heft dazu hat, trägst du es unten unter „Geplant“ mit dem vorgesehenen Ort ein und
   fragst im Bericht nach.
4. **Nach dem Heft:** `python tools/themenkarte.py` im Repo ausführen. Das Skript erzeugt alles unterhalb von „Erklärt in“
   neu aus den Heften; nur der Teil zwischen den Markierungen „von Hand“ bleibt stehen.

"""

HAND_VORLAGE = """## Zuständigkeiten und geplante Themen (von Hand)
- **Programmieren** (Informatik / Programmieren, noch ohne Heft): Python als Sprache, Datenstrukturen, Funktionen, Module,
  venv, NumPy-Grundlagen; später C und C++. ML und Cybersecurity setzen das voraus.
- **Linux und Kommandozeile** (Informatik / Linux und Kommandozeile, noch ohne Heft): Shell, Dateien, Rechte, Prozesse.
  Cybersecurity Teil 3 bis 5 werden nach der Recherche cyber-spezifisch oder entfallen.
- **ML-Grundlagen gegen Höhere Mathematik:** Was ein HöMa-Heft vollständig erklärt (Beweise, Herleitungen), steht in den
  Grundlagen nur als Kurzfassung mit Verweis. Prüfen bei der nächsten Überarbeitung der Grundlagen.
- **Geplant (noch ohne Heft):** Grundlagen 6 Optimierung (Lernpfad T06, vor dem Gradientenabstieg); ML-Pfad ab Teil 1
  „Lernen aus Daten“ (T08).
"""


def abschnitte(cfg, kap):
    """[(Nummer, Titel, [(Nummer, Titel)])] der nummerierten Abschnitte des deutschen Hefts (ohne „Lösungen“)."""
    s = H.read_tex(cfg["quelle"], cfg["hefte"][kap][0])
    s = re.search(r"\\begin\{document\}(.*)\\end\{document\}", s, re.S).group(1)
    h = H.Heft("de", kap, cfg["szenen"], extra=H.modul_makros(cfg))
    out, sec, sub = [], 0, 0
    for m in re.finditer(r"\\(section|subsection)(\*?)\{", s):
        if m.group(2):
            continue
        titel, _ = H.group(s, m.end() - 1)
        t = re.sub(r"\s+", " ", h.text(titel)).strip()
        if m.group(1) == "section":
            sec, sub = sec + 1, 0
            if re.match(r"Lösungen\s*$", t):
                break
            out.append((str(sec), t, []))
        elif out:
            sub += 1
            out[-1][2].append(("%d.%d" % (sec, sub), t))
    return out


def wendung(cfg, mod, kap):
    """Verweis-Wendung des Hefts, so wie sie in einem Heft stehen muss („Grundlagen 1“, „Programmieren, Python 2“)."""
    name = H.heft_name(cfg, kap, "de")
    if name:
        return cfg.get("praefix", {}).get("de", "") + name
    return "%s, Teil %d" % (cfg["pfad"]["de"].split(" / ")[-1], kap)


def bereich_titel(cfg, kap):
    b = H.bereich(cfg, kap)
    return cfg["pfad"]["de"] + (" / " + b["pfad"]["de"] if b and b.get("pfad") else "")


def erzeugen():
    module = sorted(H.MODULE.items(), key=lambda kv: kv[1]["order"])
    teile, zahl = [], {"hefte": 0, "abschnitte": 0, "unter": 0}
    for mod, cfg in module:
        gruppen = {}
        for kap in sorted(cfg["hefte"]):
            if not (cfg["quelle"] / (cfg["hefte"][kap][0] + ".tex")).is_file():
                continue
            b = H.bereich(cfg, kap)
            key = ((b or {}).get("order", 0), bereich_titel(cfg, kap))
            gruppen.setdefault(key, []).append(kap)
        if not gruppen:
            teile.append("## %s\n\n(noch kein Heft; Modul `%s` in tools/heft_zu_artikel.py)\n" % (cfg["pfad"]["de"], mod))
            continue
        for (_, titel), kaps in sorted(gruppen.items()):
            zeilen = ["## %s\n" % titel]
            for kap in kaps:
                stem, _, thema = cfg["hefte"][kap]
                w = wendung(cfg, mod, kap)
                zeilen.append("### %s: %s (`%s`, Modul %s)\n" % (w, thema["de"], stem, mod))
                for nr, t, subs in abschnitte(cfg, kap):
                    unter = " · ".join("%s %s" % st for st in subs)
                    zeilen.append("- %s, Abschnitt %s „%s“%s" % (w, nr, t, (": " + unter) if unter else ""))
                    zahl["abschnitte"] += 1
                    zahl["unter"] += len(subs)
                zeilen.append("")
                zahl["hefte"] += 1
            teile.append("\n".join(zeilen))
    return "\n".join(teile), zahl


def main():
    pruefen = "--pruefen" in sys.argv
    sys.stdout.reconfigure(encoding="utf-8")
    hand = HAND_VORLAGE
    if ZIEL.is_file():
        alt = ZIEL.read_text(encoding="utf-8")
        m = re.search(re.escape(HAND_AUF) + r"\n(.*?)" + re.escape(HAND_ZU), alt, re.S)
        if m:
            hand = m.group(1)
    karte, zahl = erzeugen()
    text = (KOPF + HAND_AUF + "\n" + hand.rstrip("\n") + "\n" + HAND_ZU + "\n\n"
            + "# Erklärt in (aus den Heften erzeugt, nicht von Hand ändern)\n\n"
            + "Je Zeile ein Abschnitt: Verweis-Wendung, Abschnittstitel, dann die Unterabschnitte mit Nummer.\n\n" + karte)
    print("%d Hefte, %d Abschnitte, %d Unterabschnitte" % (zahl["hefte"], zahl["abschnitte"], zahl["unter"]))
    if not pruefen:
        ZIEL.write_text(text, encoding="utf-8", newline="\n")
        print("->", ZIEL)


if __name__ == "__main__":
    main()
