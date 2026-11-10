"""Gemeinsame Helfer der Linux-Abbildungen (linux_teil3.py, linux_teil4.py und folgende), 10.11.2026 aus beiden Dateien
zusammengeführt. Die Szenen exportieren damit byte-gleich wie vorher.

    from szenen_lib import *          # noqa: F403
    from linux_hilfen import *        # noqa: F403
    setze_em(0.17)                    # nur wenn eine Terminalzeile nicht 0,19 Einheiten hoch sein soll (Kapitel 4)
    schreibmaschine("text")           # NEUE Dateien: tt/ttz/prozess in echter Schreibmaschinenschrift (siehe unten)

Inhalt:
- Zeitachse: schritt(s, *teile) mit EIN, WACHS, ZEICHNE, AUS, BETONE, ZU, VER, VERS, DREH, flach.
- Zeichnen: text, kasten, flaeche, schleier, mark, rahmen, pf, linie, klammer, vklammer, haken, strich, term_kasten,
  ordner_symbol, datei_symbol, uhr, dokument_zeilen (Kapitel 3: Rechteck mit Zeilen), datei_rechteck (Kapitel 4).
- Terminalzeilen: tt (eine Zeile), ttz (Zeile mit mehreren Leerzeichen, Stücke an ihren Spalten), cw/sp/msp (Spalten),
  zeilenende.
- Verzeichnisbaum (Kapitel 3): POS, VATER, DATEIEN, KH, kb, knoten, kante, baum, baum_auf, baum_ganz, zeilenbaum.
- Prozesse und Ströme (Kapitel 4): prozess, geist, rohr, nummer, bildschirm, tastatur, zettel, marke, karte, kernel,
  w_shell, w_schirm, w_term, w_beendet; Farben C0, C1, C2 der Ströme 0, 1, 2.

Schreibmaschinenschrift: Bis Kapitel 4 setzt tt() die Zeile als Formel (\\texttt in s.formel mit unsichtbarer \\rule-Stütze,
Zeichenbreite 0,525 em, Tilde abgesenkt). Jede Glyphe kostet dort 1,5–2 KB, ' und ` werden typografisch, \\ verschwindet.
Seit 10.11.2026 kann s.text das selbst: s.text(..., schrift="tt") (echte Zeichen, feste Zellen, roh). schreibmaschine("text")
stellt tt(), ttz() und prozess() darauf um, mit derselben Lage und Spaltenbreite (Schriftgröße so, dass eine Zelle
wieder 0,525 em breit ist), sodass sp(), msp() und cw() weiter stimmen. linux_teil3.py und linux_teil4.py rufen es NICHT
auf: Ihre Bilder bleiben, wie sie sind. Neue Kapitel rufen es am Anfang auf.
"""
import math
import re

from szenen_lib import *  # noqa: F403
from szenen_lib import PX, TT_ZELLE, SCHWARZ, GRAU, HELLGRAU, BLAU, GRUEN, ORANGE, DASH  # noqa: F401  (für Linter)

FS, FK, FM, FX = 22, 20, 18, 16   # Beschriftung, klein, sehr klein, winzig
EM = 0.19                         # Höhe einer Terminalzeile (1 em) in Szeneneinheiten (Kapitel 3; Kapitel 4: setze_em(0.17))
WEISS = "#ffffff"
BLAU_HELL = "#e3eefb"
ORANGE_HELL = "#fdece3"
GRUEN_HELL = "#e6f3ea"
ROT_HELL = "#f9e1e1"
GRAU_HELL = "#efefef"
GELB = "#fff3c4"
TERM = "#f6f6f4"
DUNKEL = "#333333"
C0, C1, C2 = BLAU, GRUEN, ORANGE  # Standardeingabe, Standardausgabe, Standardfehlerausgabe

_EINSTELLUNG = {"em": EM, "schrift": "formel"}


def setze_em(em):
    """Höhe einer Terminalzeile in Szeneneinheiten für alle Helfer dieser Datei (Standard 0,19)."""
    _EINSTELLUNG["em"] = em


def schreibmaschine(art):
    """art = "formel" (bis Kapitel 4: \\texttt in s.formel) oder "text" (s.text in Schreibmaschinenschrift, empfohlen)."""
    if art not in ("formel", "text"):
        raise ValueError('schreibmaschine: "formel" oder "text"')
    _EINSTELLUNG["schrift"] = art


def _em(em):
    return _EINSTELLUNG["em"] if em is None else em


def T(s, key, de, en, es, zh, fr, tr):
    return s.tr(key, de, en, es, zh, fr=fr, tr=tr)


# ------------------------------------------------------------------ Zeitachse
def flach(x):
    if x is None:
        return []
    if isinstance(x, (list, tuple)):
        return [i for e in x for i in flach(e)]
    return [x]


def schritt(s, *teile):
    """Ein Schritt: teile = (art, ids, dauer[, werte]); alles darin läuft gleichzeitig."""
    with s.gleichzeitig():
        for t in teile:
            werte = t[3] if len(t) > 3 else {}
            for i in flach(t[1]):
                s.animation(t[0], i, t[2], **werte)


def EIN(ids, d=0.6):
    return ("FadeIn", ids, d)


def WACHS(ids, d=0.6):
    return ("GrowFromCenter", ids, d)


def ZEICHNE(ids, d=0.8):
    return ("Create", ids, d)


def AUS(ids, d=0.5):
    return ("FadeOut", ids, d)


def BETONE(ids, d=0.8):
    return ("Indicate", ids, d)


def ZU(i, x, y, d=0.8):
    return ("MoveTo", i, d, {"point": [round(x, 4), round(y, 4), 0]})


def VER(i, dx, dy, d=0.8):
    """Verschieben um (dx, dy); auch für Texte, deren Breite je Sprache anders ist."""
    return ("Shift", i, d, {"vector": [round(dx, 4), round(dy, 4), 0]})


def VERS(ids, dx, dy, d=0.8):
    """Mehrere Objekte gemeinsam verschieben (Ergebnis: Liste von Teilen, mit * an schritt übergeben)."""
    return [VER(i, dx, dy, d) for i in flach(ids)]


def DREH(i, grad, um, d=1.0):
    return ("Rotate", i, d, {"angle": grad, "around": [round(um[0], 4), round(um[1], 4), 0]})


# ------------------------------------------------------------------ Zeichnen
def text(s, t, pos, groesse=FK, ausr="center", farbe=SCHWARZ, runden=False, roh=None):
    """s.text in Szeneneinheiten. runden=True rundet die Lage auf 4 Stellen (so in Kapitel 4); roh=True: Text wörtlich."""
    if runden:
        pos = (round(pos[0], 4), round(pos[1], 4))
    if roh is None:
        return s.text(None, t, pos, groesse, ausr, farbe)
    return s.text(None, t, pos, groesse, ausr, farbe, roh=roh)


def text_gerundet(s, t, pos, groesse=FK, ausr="center", farbe=SCHWARZ):
    """text() wie in Kapitel 4 (Lage auf 4 Stellen gerundet; linux_teil4.py: text = text_gerundet)."""
    return text(s, t, pos, groesse, ausr, farbe, runden=True)


def kasten(s, mitte, b, h, t="", groesse=FK, fuellung=WEISS, form="round", farbe=SCHWARZ, textfarbe=SCHWARZ, dicke=2.5,
           dash="", deckung=1.0):
    k = s.box("", mitte, breite=b, hoehe=h, form=form, farbe=farbe, fuellung=fuellung, deckung=deckung, dicke=dicke, dash=dash)
    if not t:
        return [k]
    return [k, s.text(None, t, mitte, groesse, "center", textfarbe)]


def flaeche(s, x0, y0, x1, y1, fuellung, farbe=None, dicke=0, dash="", deckung=1.0):
    return s.box("", ((x0 + x1) / 2, (y0 + y1) / 2), breite=x1 - x0, hoehe=y1 - y0, form="rect", farbe=farbe or fuellung,
                 fuellung=fuellung, deckung=deckung, dicke=dicke, dash=dash)


def schleier(s, mitte, b, h, deckung=0.65):
    """Weißer, halb durchsichtiger Schleier: graut das Darunterliegende aus."""
    return s.box("", mitte, breite=b, hoehe=h, form="rect", farbe=WEISS, fuellung=WEISS, deckung=deckung, dicke=0)


def mark(s, xa, xb, y, h, farbe, deckung=0.25):
    """Farbige, durchscheinende Hinterlegung (erscheint sie später, liegt sie über dem Text)."""
    return s.box("", ((xa + xb) / 2, y), breite=xb - xa, hoehe=h, form="rect", farbe=farbe, fuellung=farbe, deckung=deckung,
                 dicke=0)


def rahmen(s, mitte, b, h, farbe=ORANGE, dicke=3.5, dash=""):
    """Umriss ohne Füllung (Markierung)."""
    return s.box("", mitte, breite=b, hoehe=h, form="round", farbe=farbe, fuellung=WEISS, deckung=0.0, dicke=dicke, dash=dash)


def pf(s, a, b, knick="none", farbe=SCHWARZ, dash="", doppelt=False, dicke=2.5, spitze=0.11):
    return s.pfeil(a, b, knick=knick, farbe=farbe, dicke=dicke, spitze=spitze, dash=dash, doppelt=doppelt)


def linie(s, a, b, farbe=SCHWARZ, dicke=2.5, dash=""):
    return s.linie(None, a, b, farbe=farbe, dicke=dicke, dash=dash)


def klammer(s, xa, xb, y, unten=True, farbe=GRAU, t=0.07, dicke=2.5):
    """Eckige Klammer unter (unten=True, Schenkel nach oben) oder über einem Stück."""
    d = t if unten else -t
    return [linie(s, (xa, y + d), (xa, y), farbe, dicke), linie(s, (xa, y), (xb, y), farbe, dicke),
            linie(s, (xb, y), (xb, y + d), farbe, dicke)]


def vklammer(s, x, ya, yb, farbe=GRAU, t=0.07, dicke=2.5):
    """Senkrechte Klammer, Schenkel nach links."""
    return [linie(s, (x - t, ya), (x, ya), farbe, dicke), linie(s, (x, ya), (x, yb), farbe, dicke),
            linie(s, (x, yb), (x - t, yb), farbe, dicke)]


def haken(s, x, y, farbe=GRUEN, g=0.1, dicke=4):
    """Häkchen aus zwei Strichen (Ergebnis: Liste)."""
    return [linie(s, (x - g, y + 0.05 * g), (x - 0.25 * g, y - 0.75 * g), farbe, dicke),
            linie(s, (x - 0.25 * g, y - 0.75 * g), (x + g, y + 0.9 * g), farbe, dicke)]


def strich(s, x, y, farbe=HELLGRAU, g=0.08, dicke=3):
    """Kurzer waagrechter Strich: „trifft nicht zu“."""
    return linie(s, (x - g, y), (x + g, y), farbe, dicke)


def term_kasten(s, mitte, b, h):
    return s.box("", mitte, breite=b, hoehe=h, form="rect", farbe=GRAU, fuellung=TERM, dicke=2)


def ordner_symbol(s, x, y):
    return s.box("", (x, y), breite=0.26, hoehe=0.17, form="round", farbe=BLAU, fuellung=BLAU_HELL, dicke=1.5)


def datei_symbol(s, x, y):
    return s.box("", (x, y), breite=0.15, hoehe=0.2, form="rect", farbe=GRAU, fuellung=WEISS, dicke=1.5)


def uhr(s, x, y, std, minute, r=0.3):
    """Zifferblatt mit Stunden- und Minutenzeiger; Ergebnis (Kreis, Stundenzeiger, Minutenzeiger)."""
    k = s.kreis(None, x, y, r, farbe=SCHWARZ, dicke=2.5, fuellung=WEISS, deckung=1.0)
    wm = math.radians(90 - minute * 6)
    wh = math.radians(90 - (std % 12 + minute / 60) * 30)
    zh = linie(s, (x, y), (x + 0.5 * r * math.cos(wh), y + 0.5 * r * math.sin(wh)), SCHWARZ, 3.5)
    zm = linie(s, (x, y), (x + 0.82 * r * math.cos(wm), y + 0.82 * r * math.sin(wm)), SCHWARZ, 2.5)
    return k, zh, zm


def dokument_zeilen(s, mitte, b, h, zeilen, dz=0.22, groesse=FM, rand=SCHWARZ, fuellung=WEISS, textfarbe=SCHWARZ, dash="",
                    oben=None):
    """Rechteck mit linksbündigen Textzeilen; oben = y der ersten Zeile (sonst mittig). Ergebnis [Kasten, Text…].
    (In linux_teil3.py heißt es dokument.)"""
    x, y = mitte
    k = s.box("", mitte, breite=b, hoehe=h, form="rect", farbe=rand, fuellung=fuellung, dicke=2.5, dash=dash)
    y0 = oben if oben is not None else y + (len(zeilen) - 1) * dz / 2
    return [k] + [text(s, z, (x - b / 2 + 0.15, y0 - i * dz), groesse, "left", textfarbe) for i, z in enumerate(zeilen)]


def datei_rechteck(s, mitte, b, h):
    """Datei = schwarzes Rechteck. (In linux_teil4.py heißt es dokument.)"""
    return s.box("", mitte, breite=b, hoehe=h, form="rect", farbe=SCHWARZ, fuellung=WEISS, dicke=2)


# ------------------------------------------------------------------ Schreibmaschinenschrift
_STUETZE = r"\rule[-0.25em]{0.001em}{1em}"


def _tex(z):
    z = z.replace("\\", "").replace("$", r"\$").replace("{", r"\{").replace("}", r"\}")
    # Die Tilde sitzt in MathJax auf Höhe der Großbuchstaben; 0,25 em tiefer steht sie wie im Terminal in der Mitte.
    teile = [r"\texttt{" + t + "}" if t else "" for t in z.split("~")]
    return _STUETZE + r"\lower{0.25em}{\texttt{~}}".join(teile) + _STUETZE


def cw(em=None):
    """Breite eines Zeichens."""
    return 0.525 * _em(em)


def sp(x0, i, em=None):
    """Linke Kante der Spalte i einer Zeile, die bei x0 beginnt."""
    return x0 + i * cw(em)


def msp(x0, a, b, em=None):
    """Mitte der Spalten a bis b (einschließlich)."""
    return x0 + (a + b + 1) / 2 * cw(em)


def tt_groesse(em=None):
    """Schriftgröße (Szenenpixel) der echten Schreibmaschinenschrift, bei der eine Zelle cw(em) breit ist."""
    return round(cw(em) * PX / TT_ZELLE, 3)


def tt(s, zeile, x, y, em=None, farbe=SCHWARZ, anker="l"):
    """Eine Terminalzeile; anker l: x = linke Kante, m: x = Mitte, r: x = rechte Kante. Leerzeichen vorn verschieben.
    schreibmaschine("text"): als s.text in Schreibmaschinenschrift (roh, echte Zeichen), gleiche Lage und Spalten."""
    em = _em(em)
    vorn = len(zeile) - len(zeile.lstrip(" "))
    zeile = zeile.strip(" ")
    n, c = len(zeile), cw(em)
    cx = x + (vorn + n / 2) * c if anker == "l" else (x - n / 2 * c if anker == "r" else x)
    if _EINSTELLUNG["schrift"] == "text":
        return s.text(None, zeile, (round(cx, 4), round(y, 4)), tt_groesse(em), "center", farbe, schrift="tt")
    return s.formel(_tex(zeile), mitte=(round(cx, 4), round(y, 4)), hoehe=em, farbe=farbe)


def ttz(s, zeile, x0, y, em=None, farbe=SCHWARZ):
    """Terminalzeile mit mehreren Leerzeichen hintereinander: Stücke an ihren Spalten (Ergebnis: Liste). Mit
    schreibmaschine("text") ginge auch eine einzige Zeile tt(s, zeile, x0, y) (mehrere Leerzeichen bleiben); ttz bleibt,
    wenn die Stücke einzeln animiert werden sollen."""
    em = _em(em)
    return [tt(s, m.group(), sp(x0, m.start(), em), y, em, farbe) for m in re.finditer(r"\S+(?: \S+)*", zeile)]


def zeilenende(s, x, y, h=0.15, farbe=ORANGE):
    return s.formel(r"\hookleftarrow", mitte=(round(x, 4), round(y, 4)), hoehe=h, farbe=farbe)


# ------------------------------------------------------------------ Verzeichnisbaum (Kapitel 3)
POS = {"/": (0.0, 1.5), "etc": (-2.55, 0.7), "home": (-1.2, 0.7), "tmp": (0.15, 0.7), "usr": (1.9, 0.7),
       "student": (-1.2, -0.1), "bin": (0.95, -0.1), "lib": (1.9, -0.1), "share": (2.85, -0.1),
       "bash": (0.95, -0.9), "doc": (2.85, -0.9)}
VATER = {"etc": "/", "home": "/", "tmp": "/", "usr": "/", "student": "home", "bin": "usr", "lib": "usr", "share": "usr",
         "bash": "bin", "doc": "share"}
DATEIEN = {"bash"}
KH = 0.32                         # Höhe eines Knotens


def kb(name):
    """Breite eines Knotens."""
    return max(0.5, 0.2 + 0.085 * len(name))


def knoten(s, name, x, y, art="dir", textfarbe=SCHWARZ, b=None):
    b = b or kb(name)
    if art == "datei":
        k = s.box("", (x, y), breite=b, hoehe=KH, form="rect", farbe=GRAU, fuellung=WEISS, dicke=2)
    elif art == "geist":
        k = s.box("", (x, y), breite=b, hoehe=KH, form="round", farbe=GRAU, fuellung=WEISS, dicke=2, dash=DASH)
    elif art == "neu":
        k = s.box("", (x, y), breite=b, hoehe=KH, form="round", farbe=GRUEN, fuellung=GRUEN_HELL, dicke=3)
    else:
        k = s.box("", (x, y), breite=b, hoehe=KH, form="round", farbe=BLAU, fuellung=BLAU_HELL, dicke=2)
    return [k, s.text(None, name, (x, y), FK, "center", textfarbe)]


def kante(s, a, b, farbe=GRAU, dicke=2.5, dash="", dx=0.0):
    """Linie von der Unterkante des Knotens a zur Oberkante des Knotens b (Mitten)."""
    return linie(s, (a[0] + dx, a[1] - KH / 2), (b[0] + dx, b[1] + KH / 2), farbe, dicke, dash)


def baum(s, namen, dx=0.0, dy=0.0, pos=None, vater=None, dateien=DATEIEN, etiketten=None):
    """Kanten und Knoten; Ergebnis K[name] = [Kasten, Text], E[name] = Kante zum Vater, P[name] = Mitte.
    etiketten: abweichende Beschriftung (z. B. C:\\backslash, denn ein einzelnes \\ verschwindet in s.text)."""
    pos, vater, etiketten = pos or POS, vater or VATER, etiketten or {}
    P = {n: (round(pos[n][0] + dx, 4), round(pos[n][1] + dy, 4)) for n in namen}
    E = {n: kante(s, P[vater[n]], P[n]) for n in namen if vater.get(n) in P}
    K = {n: knoten(s, etiketten.get(n, n), *P[n], art="datei" if n in dateien else "dir", b=kb(n)) for n in namen}
    return K, E, P


def baum_auf(s, K, E, namen, d=0.7):
    """Ein Schritt: Kanten zu diesen Knoten zeichnen, Kästen wachsen, Namen einblenden."""
    schritt(s, ZEICHNE([E[n] for n in namen if n in E], d), WACHS([K[n][0] for n in namen], d),
            EIN([K[n][1] for n in namen], d))


def baum_ganz(s, K, E, extra=(), d=0.8):
    """Ein Schritt: der ganze Baum (und extra) erscheint."""
    schritt(s, ZEICHNE(list(E.values()), d), WACHS([k[0] for k in K.values()], d), EIN([k[1] for k in K.values()] + list(extra), d))


def zeilenbaum(s, x0, y0, eintraege, dz=0.38, einzug=0.34, textfarbe=SCHWARZ, groesse=FK, linienfarbe=GRAU):
    """Baum als eingerückte Liste wie bei tree: eintraege = [(name, ebene, "dir"|"datei")].
    Ergebnis: Z = je Zeile [Verbinder…, Symbol, Text] (Text zuletzt), P = je Zeile (x des Symbols, y)."""
    Z, P, letzte = [], [], {}
    for i, (name, eb, art) in enumerate(eintraege):
        x, y = round(x0 + eb * einzug, 4), round(y0 - i * dz, 4)
        teile = []
        if eb > 0:
            px, py = letzte[eb - 1]
            teile += [linie(s, (px, py - 0.09), (px, y), linienfarbe, 2),
                      linie(s, (px, y), (x - (0.14 if art == "dir" else 0.09), y), linienfarbe, 2)]
        teile.append(ordner_symbol(s, x, y) if art == "dir" else datei_symbol(s, x, y))
        teile.append(text(s, name, (x + 0.2, y), groesse, "left", textfarbe))
        Z.append(teile)
        P.append((x, y))
        if art == "dir":
            letzte[eb] = (x, y)
    return Z, P


# ------------------------------------------------------------------ Prozesse und Ströme (Kapitel 4)
def prozess(s, mitte, b, h, name, em=None, farbe=BLAU, fuellung=BLAU_HELL):
    """Prozess = blauer Kasten mit dem Programmnamen in Schreibmaschinenschrift (Ergebnis [Kasten, Name])."""
    k = s.box("", mitte, breite=b, hoehe=h, form="round", farbe=farbe, fuellung=fuellung, dicke=2.5)
    return [k, tt(s, name, mitte[0], mitte[1], _em(em), SCHWARZ, "m")]


def geist(s, mitte, b, h):
    """Blasser, gestrichelter Umriss eines beendeten Prozesses."""
    return s.box("", mitte, breite=b, hoehe=h, form="round", farbe=HELLGRAU, fuellung=WEISS, deckung=0.0, dicke=2, dash=DASH)


def rohr(s, a, b, farbe, dicke=4.5, spitze=0.13, dash=""):
    """Ein Strom als dicker Pfeil."""
    return pf(s, a, b, farbe=farbe, dash=dash, dicke=dicke, spitze=spitze)


def nummer(s, x, y, n, farbe, r=0.12):
    """Deskriptornummer im Kreis (Ergebnis [Kreis, Zahl])."""
    return [s.kreis(None, round(x, 4), round(y, 4), r, farbe=farbe, dicke=2, fuellung=WEISS, deckung=1.0),
            text_gerundet(s, str(n), (x, y), FX, "center", farbe)]


def bildschirm(s, mitte, b, h):
    return s.box("", mitte, breite=b, hoehe=h, form="rect", farbe=DUNKEL, fuellung=TERM, dicke=3)


def tastatur(s, x, y):
    teile = [s.box("", (x, y), breite=0.86, hoehe=0.36, form="round", farbe=GRAU, fuellung=GRAU_HELL, dicke=2)]
    for n, dy in ((6, 0.07), (5, -0.07)):
        for i in range(n):
            teile.append(s.box("", (round(x - (n - 1) * 0.06 + i * 0.12, 4), round(y + dy, 4)), breite=0.09, hoehe=0.09,
                               form="rect", farbe=GRAU, fuellung=WEISS, dicke=1))
    return teile


def zettel(s, x, y, t, farbe=SCHWARZ, b=0.4, h=0.32, groesse=FK):
    """Gelber Zettel mit einer Zahl (Exit-Status)."""
    return [s.box("", (x, y), breite=b, hoehe=h, form="rect", farbe=GRAU, fuellung=GELB, dicke=1.5),
            text_gerundet(s, t, (x, y), groesse, "center", farbe)]


def marke(s, x, y, farbe, b=0.34, h=0.18):
    """Farbiges Kästchen: eine Zeile unterwegs in einem Strom."""
    return s.box("", (x, y), breite=b, hoehe=h, form="round", farbe=farbe, fuellung=farbe, deckung=0.85, dicke=1.5)


def karte(s, x, y, t, b, rand=GRAU, fuellung=GRAU_HELL, groesse=FM, textfarbe=SCHWARZ, h=0.28):
    """Abgerundete Karte mit Text (Ergebnis [Kasten, Text])."""
    return [s.box("", (x, y), breite=b, hoehe=h, form="round", farbe=rand, fuellung=fuellung, dicke=2),
            text_gerundet(s, t, (x, y), groesse, "center", textfarbe)]


def kernel(s, x0, y0, x1, y1, lpos, ausr="left"):
    return [flaeche(s, x0, y0, x1, y1, GRAU_HELL),
            text_gerundet(s, T(s, "kernel", "Kernel", "kernel", "kernel", "内核", "noyau", "çekirdek"), lpos, FM, ausr, GRAU)]


def w_shell(s):
    return T(s, "shell", "Shell", "shell", "shell", "Shell", "shell", "kabuk")


def w_schirm(s):
    return T(s, "schirm", "Bildschirm", "screen", "pantalla", "屏幕", "écran", "ekran")


def w_term(s):
    return T(s, "term", "Terminal", "terminal", "terminal", "终端", "terminal", "terminal")


def w_beendet(s):
    return T(s, "beendet", "beendet", "ended", "terminado", "已结束", "terminé", "sona erdi")
