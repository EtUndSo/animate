"""Hefte auf die einheitliche Benennung „Kapitel N“ umstellen (Wunsch des Users, 09.11.2026; notizen/kapitel_umstellung.md).

Wirkt auf alle .tex aller Module (MODULE in tools/heft_zu_artikel.py) und Sprachen (Kap<N>_<Name>[_<lang>].tex, kap<N>_*.tex):
  * Titelzeile „{\\small Arbeitsheft …, Teil~N. Stand: …}“ -> „Arbeitsheft <Bereich>, Kapitel~N. Stand: …“ (TITELZEILE im
    Umwandler), dazu der Kopfkommentar „%  Arbeitsheft …, Teil N: Titel“ in der Hauptdatei;
  * Verweise „Teil~N“, „Grundlagen~N“, „Programmieren, Python~N“, „Python~N“ (in prog), „Linux~N“, „Höhere Mathematik~1, Teil~N“
    (und die Formen der Übersetzungen) -> „Kapitel~N“ im eigenen Bereich, sonst „<Kurzname>, Kapitel~N“ (zh „<Kurzname>~第~N~章“);
    es/fr mit passendem Artikel („de la Parte~2“ -> „del capítulo~2“, „de Fondements~1“ -> „du chapitre~1“).
Nicht angefasst: Formeln, Code-Umgebungen, \\verb, \\texttt, \\label/\\ref, Kommentare (außer dem Kopfkommentar),
Versionsnummern („Python 3.13“, „Linux 6.8“; „Python 3“ und „Linux 2“ mit gewöhnlichem Leerzeichen gelten als Version und
werden nur gemeldet), Aufgabenteile („…, Teil 1: …“ in Aufgabentiteln), „Teile 2 durch …“ (Rechenanweisung).

Aufruf (vom Repo-Root):
    python tools/kapitel_umstellung.py                       Probelauf, alle Module: jeder Treffer mit Datei, Zeile, Kontext
    python tools/kapitel_umstellung.py --modul et3 ml        nur diese Module
    python tools/kapitel_umstellung.py --aus liste.txt       Treffer in eine Datei, auf der Konsole nur die Zählung
    python tools/kapitel_umstellung.py --anwenden            Dateien schreiben (vorher sichern!)
    python tools/kapitel_umstellung.py --md content/hm3/03-kurvenintegrale [--anwenden]
          dasselbe im Text von Artikeln, die nicht aus dem Heft entstehen (alter Stand, veraltete Übersetzungen)
    python tools/kapitel_umstellung.py --kopf content/et3/02-laplace-transformation [--anwenden]
          Kopfzeilen solcher Artikel (pfad:, adresse:, knoten:) so setzen, wie der Umwandler sie schreibt
Ein zweiter Lauf findet nichts mehr (die neuen Formen erkennt er nicht als alt).
"""
import argparse
import collections
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import heft_zu_artikel as H  # noqa: E402

ROOT = H.ROOT
LANGS = H.LANGS
NB = "\u00a0"

# ---------------------------------------------------------------------------------- alte Formen ----
# en nur groß: „polynomial part 0“, „part 1: when …“ sind keine Heftverweise (der Umwandler verlinkte auch nur „Part N“)
TEIL_W = {"de": r"Teil(?:e|en|s)?", "en": r"Parts?", "es": r"[Pp]artes?", "fr": r"[Pp]arties?", "tr": r"[Kk]ısım(?:lar)?"}
GRUND_W = {"de": "Grundlagen", "en": "Foundations", "es": "Fundamentos", "fr": "Fondements", "tr": "Temeller", "zh": "基础篇"}
# neues Wort je Sprache; es/fr klein (Großschreibung am Satzanfang regelt grammatik())
KAP_W = {"de": "Kapitel", "en": "Chapter", "es": "capítulo", "fr": "chapitre", "tr": "Bölüm"}
KAP_PL = {"de": "Kapitel", "en": "Chapters", "es": "capítulos", "fr": "chapitres", "tr": "Bölümler"}
DE_FORM = {"Teil": "Kapitel", "Teile": "Kapitel", "Teilen": "Kapiteln", "Teils": "Kapitels"}
STAND = r"(?:\.|。)\s*(?:Stand|Version|Versión|版本|Sürüm)\b"
ALT_WORT = r"Teil|Part|[Pp]arte|部分|Grundlagen|Foundations|Fundamentos|Fondements|Temeller|基础篇|Python|Linux|C\+\+|\bC\b|Kısım|Partie"

# ------------------------------------------------------------------------------ geschützte Stellen ----
_CODE = "|".join(sorted(H.CODE_ENVS, key=len, reverse=True)) + "|verbatim|lstlisting"
SCHUTZ_TEX = re.compile(
    r"(?<!\\)%[^\n]*"
    r"|\\begin\{(?P<env>" + _CODE + r"|equation\*?|align\*?|gather\*?|multline\*?|eqnarray\*?)\}.*?\\end\{(?P=env)\}"
    r"|\\(?:verb|lstinline)\*?(?P<d>[^A-Za-z\s{])[^\n]*?(?P=d)"
    r"|\\(?:texttt|url|href|label|ref|eqref|cref|Cref|pageref|input|include|szene|szenenabb|includegraphics|lstinline)\{[^{}]*\}"
    r"|\$\$.*?\$\$|\\\[.*?\\\]|\\\(.*?\\\)|(?<!\\)\$(?:\\.|[^$\\])*\$", re.S)
SCHUTZ_MD = re.compile(r"\A---\n.*?\n---\n|^```.*?^```|`[^`\n]*`|\$\$.*?\$\$|(?<!\\)\$[^$\n]*\$|\]\([^)]*\)|<[^>\n]*>",
                       re.S | re.M)


def aufgaben_titel(text, art):
    """Bereiche der Aufgabentitel: dort sind „…, Teil 1: …“ Teile einer Aufgabenreihe, keine Heftverweise."""
    out = []
    if art == "md":
        for m in re.finditer(r"(?m)^:::aufgabe\b.*$", text):
            out.append((m.start(), m.end()))
        return out
    for m in re.finditer(r"\\begin\{aufgabe\}(?:\[[^\]]*\])?\{", text):
        i, d = m.end() - 1, 0
        for j in range(i, min(len(text), i + 600)):
            if text[j] == "{" and text[j - 1] != "\\":
                d += 1
            elif text[j] == "}" and text[j - 1] != "\\":
                d -= 1
                if d == 0:
                    out.append((i, j))
                    break
    return out


def drin(spans, pos):
    return any(a <= pos < b for a, b in spans)


# ---------------------------------------------------------------------------------- Grammatik ----
ES_ART = {"la": "el", "La": "El", "las": "los", "Las": "Los"}
FR_ART = {"la": "le", "La": "Le", "les": "les", "Les": "Les", "le": "le", "Le": "Le"}
SCHON = {"es": {"el", "El", "del", "Del", "al", "Al", "los", "Los", "este", "Este", "ese", "cada", "su", "nuestro"},
         "fr": {"le", "Le", "du", "Du", "au", "Au", "des", "aux", "ce", "Ce", "chaque", "son", "notre"}}
VOR_RE = re.compile(r"(?:(?P<w2>[^\s~\u00a0(\[{]+)(?P<g2>[\s~\u00a0]+))?(?P<w1>[^\s~\u00a0(\[{]+)(?P<g1>[\s~\u00a0]+\[?|\[)$")


def grammatik(text, start, lang, plural, grenze):
    """es/fr ohne Kurznamen: Artikel und Großschreibung vor dem neuen Wort. -> (neuer Anfang, Text vor dem Wort, Wort, Notiz)."""
    nomen = KAP_PL[lang] if plural else KAP_W[lang]
    vor = text[max(grenze, start - 160):start]
    m = VOR_RE.search(vor)
    if not m:                                           # direkt nach „(“ usw. oder am Anfang
        if not vor.strip():
            return start, "", nomen[0].upper() + nomen[1:], "Satzanfang"
        return start, "", nomen, ""
    w1, w2, g1 = m.group("w1"), m.group("w2"), m.group("g1")
    a1 = start - len(vor) + m.start("w1")
    a2 = start - len(vor) + m.start("w2") if w2 else None
    gross = lambda w: w[0].upper() + w[1:]
    if w1[-1] in ",;:(—–":
        return start, "", nomen, ""
    if w1[-1] in ".!?}]" or w1.startswith("\\"):
        art = {"es": "Los" if plural else "El", "fr": "Les" if plural else "Le"}[lang]
        return start, "", art + " " + nomen, "Satzanfang: Artikel ergänzt"
    if lang == "es":
        if w1 in ES_ART:
            neu = ES_ART[w1]
            if w2 in ("de", "De", "a", "A") and neu == "el":
                kurz = {"de": "del", "De": "Del", "a": "al", "A": "Al"}[w2]
                return a2, kurz + g1, nomen, "Artikel: %s %s -> %s" % (w2, w1, kurz)
            return a1, neu + g1, nomen, "Artikel: %s -> %s" % (w1, neu)
        if w1 in ("de", "De", "a", "A") and not plural:
            kurz = {"de": "del", "De": "Del", "a": "al", "A": "Al"}[w1]
            return a1, kurz + g1, nomen, "Artikel: %s -> %s" % (w1, kurz)
        if w1 in ("de", "De", "a", "A"):
            return start, "los ", nomen, "Artikel ergänzt"
    else:
        if w1 in FR_ART:
            neu = FR_ART[w1]
            if w2 in ("de", "De", "à", "À") and neu in ("le", "les"):
                kurz = {("de", "le"): "du", ("De", "le"): "Du", ("à", "le"): "au", ("À", "le"): "Au", ("de", "les"): "des",
                        ("De", "les"): "Des", ("à", "les"): "aux", ("À", "les"): "Aux"}[(w2, neu)]
                return a2, kurz + g1, nomen, "Artikel: %s %s -> %s" % (w2, w1, kurz)
            return a1, neu + g1, nomen, "Artikel: %s -> %s" % (w1, neu)
        if w1 in ("de", "De", "à", "À"):
            kurz = {("de", False): "du", ("De", False): "Du", ("à", False): "au", ("À", False): "Au",
                    ("de", True): "des", ("De", True): "Des", ("à", True): "aux", ("À", True): "Aux"}[(w1, plural)]
            return a1, kurz + g1, nomen, "Artikel: %s -> %s" % (w1, kurz)
    if w1 in SCHON[lang]:
        return start, "", nomen, ""
    if re.fullmatch(r"[^\W\d_][\w’']*", w1):          # Präposition, Konjunktion, Verb: Artikel ergänzen
        art = {"es": "los" if plural else "el", "fr": "les" if plural else "le"}[lang]
        return start, art + " ", nomen, "Artikel ergänzt nach „%s“" % w1
    return start, "", nomen, ""


# ------------------------------------------------------------------------------------- Regeln ----
def _wort(t, sp):
    """Feste Wendung mit Leerzeichen als Muster (~, Leerzeichen, geschütztes Leerzeichen)."""
    return "".join(sp if c == " " else r"[，,]%s?" % sp if c == "，" else re.escape(c) for c in t)


def regeln(lang, art, cfg):
    """[(Name, Muster, Ziel(m) -> (Modul, Bereich, Wort))]. Gruppen: w (altes Wort), sp (Abstand), n (Nummer),
    zh: s1, s2 (Abstände um die Nummer), tr (verschluckter Abstand vor „第“)."""
    sp = r"[~ \u00a0]" if art == "tex" else r"[ \u00a0]"
    tilde = "~" if art == "tex" else NB                 # Python~N, Linux~N: nur mit geschütztem Abstand (sonst Version)
    N = r"(?P<n>\d+)(?![.,]?\d)"
    zhend = r"(?P<tr>%s?(?=第))?" % sp if lang == "zh" else ""
    out = []
    prog, linux, ml = H.MODULE["prog"], H.MODULE["linux"], H.MODULE["ml"]
    for z in H.MODULE.values():                         # „Höhere Mathematik~1, Teil~2“
        if z.get("alt_modul"):
            name = _wort(z["alt_modul"][lang], sp)
            if lang == "zh":
                rx = r"(?<!\w)%s[，,]?%s?第(?P<s1>%s?)%s(?P<s2>%s?)部分" % (name, sp, sp, N, sp)
            else:
                rx = r"(?<!\w)%s,%s(?P<w>%s)(?P<sp>%s)%s" % (name, sp, TEIL_W[lang], sp, N)
            out.append(("alter Modulname", re.compile(rx), lambda m, z=z: (z, z["bereiche"][0])))
    prae = _wort(prog["praefix"][lang].strip(), sp)
    if lang == "zh":
        prae = prae.rstrip()
    rx = r"%s%s?(?P<w>Python|C\+\+|C|%s)(?P<sp>%s)%s%s" % (prae, sp, "Kapitel" if lang == "de" else "Python", sp, N, zhend)
    out.append(("Programmieren, …", re.compile(rx),
                lambda m: (prog, prog["bereiche"][{"C": 1, "C++": 2}.get(m.group("w"), 0)])))
    rx = r"(?<![\w./+-])(?P<w>Linux)(?P<sp>%s)%s%s" % (tilde, N, zhend)
    out.append(("Linux N", re.compile(rx), lambda m: (linux, linux["bereiche"][0])))
    if cfg is prog:
        rx = r"(?<![\w./+-])(?P<w>Python)(?P<sp>%s)%s%s" % (tilde, N, zhend)
        out.append(("Python N (in prog)", re.compile(rx), lambda m: (prog, prog["bereiche"][0])))
    if lang == "zh":
        rx = r"(?P<w>基础篇)(?P<s1>%s?)%s%s" % (sp, N, zhend)
    else:
        rx = r"(?<![\w-])(?P<w>%s)(?P<sp>%s)%s" % (GRUND_W[lang], sp, N)
    out.append(("Grundlagen N", re.compile(rx), lambda m: (ml, ml["bereiche"][0])))
    if lang == "zh":
        rx = r"第(?P<s1>%s?)%s(?P<s2>%s?)部分" % (sp, N, sp)
    else:
        rx = r"\b(?P<w>%s)(?P<sp>%s)%s" % (TEIL_W[lang], sp, N)
    out.append(("Teil N", re.compile(rx), None))        # Ziel: eigener Bereich („Teile 2 durch …“ überspringt bearbeite)
    return out


MELDEN = {                                              # nur melden: sieht aus wie ein Heftname, wird aber nicht geändert
    "Python/Linux mit Leerzeichen (Version?)": r"(?<![\w./+-])(?:Python|Linux) \d+(?![.,]?\d)",
    "Teile N durch (Rechenanweisung)": r"\bTeile[~ \u00a0]\d+[~ \u00a0]+durch\b",
}


# ----------------------------------------------------------------------------------- Bearbeiten ----
def sprache(stem):
    m = re.search(r"[._](en|es|zh|fr|tr)$", stem)
    return m.group(1) if m else "de"


def neu_verweis(lang, cfg, kap, z, b, m, text, grenze):
    """Ersatz für einen Treffer: (Anfang, Ende, neuer Text, Notiz)."""
    eigen = H.bereich(cfg, kap)
    gleich = z is cfg and b is eigen
    n = m.group("n")
    w = m.groupdict().get("w") or ""
    start, ende = m.start(), m.end()
    if lang == "zh":
        s1 = m.groupdict().get("s1")
        s1 = s1 if s1 is not None else (m.groupdict().get("sp") or "")
        s2 = m.groupdict().get("s2")
        s2 = s2 if s2 is not None else s1
        kern = "第%s%s%s章" % (s1, n, s2)
        if gleich:
            return start, ende, kern, ""
        k = b["kurz"]["zh"]
        return start, ende, k + ("~" if k[-1].isascii() and s1 else "") + kern, "Kurzname"
    sp = m.groupdict().get("sp") or "~"
    plural = (lang in ("en", "fr", "es") and w.lower().endswith(("parts", "partes", "parties"))) or w in ("Kısımlar",)
    if lang == "de":
        wort = DE_FORM.get(w, "Kapitel")
    elif lang in ("es", "fr"):
        wort = KAP_PL[lang] if plural else KAP_W[lang]
    elif lang == "en":
        wort = ("Chapters" if plural else "Chapter") if w[:1] != "p" else ("chapters" if plural else "chapter")
    else:
        wort = KAP_PL[lang] if plural else KAP_W[lang]
    if not gleich:
        return start, ende, "%s, %s%s%s" % (b["kurz"][lang], wort, sp, n), "Kurzname"
    notiz = ""
    if lang in ("es", "fr"):
        start, vor, wort, notiz = grammatik(text, start, lang, plural, grenze)
        return start, ende, vor + wort + sp + n, notiz
    return start, ende, wort + sp + n, notiz


def titel_und_kopf(text, lang, cfg, kap, hauptdatei):
    """Titelzeile und Kopfkommentar der Hauptdatei: [(Anfang, Ende, neu, Kategorie)]."""
    if not hauptdatei:
        return []
    out = []
    neu = H.titelzeile(cfg, kap, lang)
    m = re.search(r"(\{\\small\s+)(?P<alt>[^\n]*?)(?=%s)" % STAND, text)
    if m and m.group("alt") != neu:
        out.append((m.start("alt"), m.end("alt"), neu, "Titelzeile"))
    nr = str(H.kapitel_nr(cfg, kap))
    for k in re.finditer(r"(?m)^%[ \t]+(?P<alt>[^\n:：]*?)(?=[ \t]?[:：])", text[:600]):
        alt = k.group("alt")
        if text.startswith(neu.replace("~", " "), k.start("alt")):
            break                                       # schon neu (der Modulname enthält selbst einen Doppelpunkt)
        if re.search(r"(?<!\d)%s(?!\d)" % nr, alt) and re.search(ALT_WORT, alt) and alt != neu.replace("~", " "):
            out.append((k.start("alt"), k.end("alt"), neu.replace("~", " "), "Kopfkommentar"))
            break
    return out


def bearbeite(text, art, lang, cfg, kap, hauptdatei=False):
    """-> (neuer Text, [Treffer]) mit Treffer = dict(start, ende, alt, neu, kat, notiz)."""
    edits = [dict(start=s, ende=e, neu=t, kat=k, notiz="") for s, e, t, k in titel_und_kopf(text, lang, cfg, kap, hauptdatei)]
    schutz = [(m.start(), m.end()) for m in (SCHUTZ_TEX if art == "tex" else SCHUTZ_MD).finditer(text)]
    schutz += [(e["start"], e["ende"]) for e in edits]
    if art == "tex":                                    # die ganze Titelzeile
        schutz += [(m.start(), m.end()) for m in re.finditer(r"\{\\small[^\n]*?%s[^\n]*" % STAND, text)]
    aufg = aufgaben_titel(text, art)
    kand = []
    for name, rx, ziel in regeln(lang, art, cfg):
        for m in rx.finditer(text):
            kand.append((m.start(), -(m.end() - m.start()), name, m, ziel))
    kand.sort(key=lambda k: (k[0], k[1]))
    gemeldet, ende_vorher = [], 0
    for start, _, name, m, ziel in kand:
        if start < ende_vorher or drin(schutz, start):
            continue
        if m.groupdict().get("w") == "Teile" and re.match(r"[~  ]+durch\b", text[m.end():]):
            continue                                    # „Teile 2 durch diese Zahl“ (Rechenanweisung), MELDEN nennt es
        if drin(aufg, start) and re.match(r"[ \t]*[:：]", text[m.end():]):
            gemeldet.append(dict(start=m.start(), ende=m.end(), kat="übersprungen: Aufgabenteil"))
            ende_vorher = m.end()
            continue
        z, b = ziel(m) if ziel else (cfg, H.bereich(cfg, kap))
        if b is None:
            gemeldet.append(dict(start=m.start(), ende=m.end(), kat="übersprungen: kein Bereich"))
            continue
        s, e, neu, notiz = neu_verweis(lang, cfg, kap, z, b, m, text, ende_vorher)
        edits.append(dict(start=s, ende=e, neu=neu, kat=name, notiz=notiz))
        ende_vorher = e
    for name, rx in MELDEN.items():
        for m in re.finditer(rx, text):
            if not drin(schutz, m.start()) and not any(x["start"] <= m.start() < x["ende"] for x in edits):
                gemeldet.append(dict(start=m.start(), ende=m.end(), kat="gemeldet: " + name))
    edits.sort(key=lambda x: x["start"])
    neu_text = text
    for x in reversed(edits):
        x["alt"] = text[x["start"]:x["ende"]]
        neu_text = neu_text[:x["start"]] + x["neu"] + neu_text[x["ende"]:]
    for g in gemeldet:
        g["alt"], g["neu"], g["notiz"] = text[g["start"]:g["ende"]], "", ""
    return neu_text, [x for x in edits if x["alt"] != x["neu"]] + gemeldet


def kontext(text, x, breite=45):
    a, e = max(0, x["start"] - breite), min(len(text), x["ende"] + breite)
    return (text[a:x["start"]] + "⟦" + text[x["start"]:x["ende"]] + "⟧" + text[x["ende"]:e]).replace("\n", "⏎")


# -------------------------------------------------------------------------------------- Dateien ----
def tex_dateien(module):
    for mod in module:
        cfg = H.MODULE[mod]
        for p in sorted(cfg["quelle"].glob("*.tex")):
            if p.name.startswith("praeambel"):
                continue
            m = re.match(r"[Kk]ap(\d+)_", p.name)
            yield mod, cfg, (int(m.group(1)) if m else None), sprache(p.stem), p, bool(re.match(r"Kap\d+_", p.name))


def md_ordner(ordner):
    """content/<ziel>/<NN-slug> -> (Modul, cfg, kap)."""
    d = Path(ordner).resolve()
    ziel, nn = d.parent.name, d.name
    for mod, cfg in H.MODULE.items():
        if cfg["ziel"] == ziel:
            return mod, cfg, int(nn.split("-", 1)[0])
    raise SystemExit("kein Modul für %s" % d)


def kopf_nachziehen(ordner, anwenden):
    """pfad:, adresse:, knoten: wie heft_zu_artikel.artikel(); Text bleibt."""
    mod, cfg, kap = md_ordner(ordner)
    n = 0
    for p in sorted(Path(ordner).glob("*.md")):
        lang = sprache(p.stem)
        s = p.read_text(encoding="utf-8")
        if not s.startswith("---"):
            continue
        kopf, rest = s.split("\n---", 1)
        neu = []
        for z in kopf.split("\n"):
            if z.startswith(("adresse:", "knoten:")):
                continue
            if z.startswith("pfad:"):
                neu += ["pfad: " + H.heft_pfad(cfg, kap, lang), "adresse: " + H.heft_adresse(cfg, kap),
                        "knoten: " + H.knoten_name(cfg, kap, lang)]
            else:
                neu.append(z)
        t = "\n".join(neu) + "\n---" + rest
        if t != s:
            n += 1
            print("Kopf:", p.relative_to(ROOT), "|", " | ".join(neu[1:6]))
            if anwenden:
                p.write_text(t, encoding="utf-8", newline="\n")
    print("%d Dateien %s" % (n, "geändert" if anwenden else "zu ändern (Probelauf)"))


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    ap = argparse.ArgumentParser()
    ap.add_argument("--modul", nargs="*", choices=sorted(H.MODULE))
    ap.add_argument("--anwenden", action="store_true")
    ap.add_argument("--aus", help="Treffer in diese Datei (sonst auf die Konsole)")
    ap.add_argument("--md", nargs="*", help="Ordner mit Artikeln (content/<modul>/<NN-kapitel>) statt der Hefte")
    ap.add_argument("--kopf", nargs="*", help="Ordner mit Artikeln: nur die Kopfzeilen nachziehen")
    a = ap.parse_args()
    if a.kopf:
        for o in a.kopf:
            kopf_nachziehen(o, a.anwenden)
        return 0
    if a.md:
        quellen = []
        for o in a.md:
            mod, cfg, kap = md_ordner(o)
            quellen += [(mod, cfg, kap, sprache(p.stem), p, False) for p in sorted(Path(o).glob("*.md"))]
        art = "md"
    else:
        quellen, art = list(tex_dateien(a.modul or sorted(H.MODULE, key=lambda m: H.MODULE[m]["order"]))), "tex"
    zeilen, zahl, dateien = [], collections.Counter(), 0
    for mod, cfg, kap, lang, p, haupt in quellen:
        if kap is None or kap not in cfg["hefte"]:
            zeilen.append("· %s: ohne bekannte Kapitelnummer, übersprungen" % p)
            continue
        text = p.read_text(encoding="utf-8")
        neu, treffer = bearbeite(text, art, lang, cfg, kap, haupt)
        for x in sorted(treffer, key=lambda x: x["start"]):
            zeile = text.count("\n", 0, x["start"]) + 1
            zahl[(mod, lang, x["kat"])] += 1
            if x["notiz"]:
                zahl[(mod, lang, "  davon " + x["notiz"].split(" nach ")[0].split(":")[0])] += 1
            pfeil = "  ->  %s" % x["neu"] if x["neu"] or not x["kat"].startswith(("gemeldet", "übersprungen")) else ""
            zeilen.append("%s:%d [%s %s] %s%s%s\n      %s" % (p.name, zeile, mod, lang, x["kat"], ("; " + x["notiz"]) if x["notiz"] else "",
                                                        "", kontext(text, x)) + ("\n      %r%s" % (x["alt"], pfeil)))
        if neu != text:
            dateien += 1
            if a.anwenden:
                p.write_text(neu, encoding="utf-8", newline="\n")
    liste = "\n".join(zeilen)
    if a.aus:
        Path(a.aus).write_text(liste + "\n", encoding="utf-8")
    else:
        print(liste)
    print("\n%s: %d Dateien %s" % ("Anwenden" if a.anwenden else "Probelauf", dateien,
                                   "geändert" if a.anwenden else "würden geändert"))
    for (mod, lang, kat), n in sorted(zahl.items()):
        print("%6d  %-6s %-3s %s" % (n, mod, lang, kat))
    return 0


if __name__ == "__main__":
    sys.exit(main())
