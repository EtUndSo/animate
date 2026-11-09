"""Programmieren, Python 3 (C:\\Bücher\\EtUndSo\\Programmieren\\Arbeitshefte\\kap3_stufen.tex, kap3_stufen_b.tex): Abbildungen.

Szenenname prog/k3<name> = \\label{fig:k3<name>} im Heft. Stil wie tools/szenen/prog_teil2.py (Kästen, Pfeile, Code mit s.formel).
Bauen:  python tools/szenen/prog_teil3.py
Export: python tools/export_szenen.py prog/k3if prog/k3block prog/k3elif prog/k3while prog/k3range prog/k3rquadrate
            prog/k3rmittel prog/k3bisektion prog/k3newton prog/k3fehler prog/k3diode   (jedes Bild höchstens 548 px breit)
Rechenbilder: k3rquadrate mit s.summe ("i^2", 1 bis 5), k3rmittel mit s.formel (Messwerte mit Einheit, Index k).
Code steht in s.formel als \\texttt{...}; dort bleibt der Dezimalpunkt (5.25) in allen Sprachen erhalten.
Die Zahlen prüft C:\\Bücher\\EtUndSo\\Programmieren\\Arbeitshefte\\rechnung_kap3.py.
"""
import math
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from szenen_lib import *  # noqa: E402,F403

KLEIN = 22
MITTEL = 24
BLAU_HELL = "#e3eefb"
ORANGE_HELL = "#fdece3"
GRUEN_HELL = "#e6f3ea"
ROT_HELL = "#fbe9e9"


def kasten(s, mitte, breite, hoehe, text, groesse=KLEIN, farbe=SCHWARZ, fuellung="#ffffff"):
    """Abgerundeter Kasten (Anweisung im Flussdiagramm) mit Text."""
    s.box("", mitte, breite=breite, hoehe=hoehe, form="round", farbe=farbe, fuellung=fuellung, deckung=1, dicke=2.5)
    if text:
        s.text(None, text, mitte, groesse, "center", farbe)


def code_kasten(s, mitte, breite, hoehe, tex, h=0.18, fuellung="#ffffff"):
    """Kasten mit Code (s.formel, \\texttt)."""
    s.box("", mitte, breite=breite, hoehe=hoehe, form="round", farbe=SCHWARZ, fuellung=fuellung, deckung=1, dicke=2.5)
    s.formel(tex, mitte=mitte, hoehe=h)


def raute(s, mitte, breite, hoehe, tex, h=0.17):
    """Raute (Frage im Flussdiagramm) mit einer Bedingung in Code."""
    s.box("", mitte, breite=breite, hoehe=hoehe, form="diamond", farbe=SCHWARZ, fuellung=BLAU_HELL, deckung=1, dicke=2.5)
    s.formel(tex, mitte=mitte, hoehe=h)


def pf(s, a, b, knick="none", farbe=SCHWARZ):
    s.pfeil(a, b, knick=knick, farbe=farbe, dicke=2.5, spitze=0.12)


def ja_nein(s):
    return (s.tr("ja", "ja", "yes", "sí", "是", fr="oui", tr="evet"),
            s.tr("nein", "nein", "no", "no", "否", fr="non", tr="hayır"))


# ------------------------------------------------------------------ Abschnitt 2
def k3if():
    """Flussdiagramme: links if, rechts if mit else."""
    s = Szene("prog/k3if")
    ja, nein = ja_nein(s)
    lesen = s.tr("lesen", "u einlesen", "read u", "leer u", "读取 u", fr="lire u", tr="u'yu oku")
    warn = s.tr("warn", "Warnung\nausgeben", "print\nwarning", "mostrar\naviso", "输出\n警告", fr="afficher\nl’alerte",
                tr="uyarı\nyazdır")
    ende = s.tr("ende", "„Messung beendet“", "“measurement done”", "«medición terminada»", "“测量结束”",
                fr="« mesure terminée »", tr="„ölçüm bitti“")
    ok = s.tr("ok", "„in Ordnung“", "“OK”", "«en orden»", "“正常”", fr="« correct »", tr="„uygun“")
    s.formel(r"\texttt{if}", mitte=(-2.15, 2.65), hoehe=0.17)
    s.formel(r"\texttt{if}\ \text{+}\ \texttt{else}", mitte=(1.6, 2.65), hoehe=0.2)
    # links: if
    x = -2.15
    kasten(s, (x, 2.0), 1.6, 0.48, lesen)
    raute(s, (x, 0.85), 1.75, 0.95, r"\texttt{u > 5.25}?")
    kasten(s, (x, -0.55), 1.6, 0.72, warn)
    kasten(s, (x, -1.75), 2.2, 0.48, ende)
    pf(s, (x, 1.76), (x, 1.33))
    pf(s, (x, 0.37), (x, -0.19))
    pf(s, (x, -0.91), (x, -1.51))
    s.text(None, ja, (x + 0.12, 0.08), KLEIN, "left")
    s.linie(None, (x + 0.875, 0.85), (x + 1.45, 0.85), dicke=2.5)
    s.linie(None, (x + 1.45, 0.85), (x + 1.45, -1.75), dicke=2.5)
    pf(s, (x + 1.45, -1.75), (x + 1.1, -1.75))
    s.text(None, nein, (x + 1.0, 1.05), KLEIN, "left")
    # rechts: if und else
    x = 1.6
    kasten(s, (x, 2.0), 1.6, 0.48, lesen)
    raute(s, (x, 0.85), 1.75, 0.95, r"\texttt{u > 5.25}?")
    kasten(s, (x - 1.15, -0.55), 1.35, 0.72, warn)
    kasten(s, (x + 1.15, -0.55), 1.35, 0.72, ok)
    kasten(s, (x, -1.75), 2.2, 0.48, ende)
    pf(s, (x, 1.76), (x, 1.33))
    pf(s, (x - 0.875, 0.85), (x - 1.15, -0.19), knick="hv")
    pf(s, (x + 0.875, 0.85), (x + 1.15, -0.19), knick="hv")
    s.text(None, ja, (x - 1.25, 1.03), KLEIN, "center")
    s.text(None, nein, (x + 1.25, 1.03), KLEIN, "center")
    pf(s, (x - 1.15, -0.91), (x - 0.4, -1.51), knick="vh")
    pf(s, (x + 1.15, -0.91), (x + 0.4, -1.51), knick="vh")
    s.speichern()


def k3block():
    """Einen Block erkennt man an der Einrückung: Kopfzeile, eingerückter Block, wieder links."""
    s = Szene("prog/k3block")
    xc, yc, h = -1.65, 0.0, 1.6                     # Mitte und Höhe der Codezeilen
    zeile = h / 5                                    # Abstand der Zeilen
    s.box("", (-1.45, yc - 0.5 * zeile), breite=4.2, hoehe=2 * zeile, form="rect", farbe=BLAU, fuellung=BLAU_HELL,
          deckung=1, dicke=0)
    s.formel(r'\begin{array}{l}\texttt{u = float(input("Spannung in V: "))}\\\texttt{if u > 5.25:}\\'
             r'\hspace{2em}\texttt{zuviel = u - 5.25}\\\hspace{2em}\texttt{print(f"Achtung: ... zu hoch")}\\'
             r'\texttt{print("Messung beendet")}\end{array}', mitte=(xc, yc), hoehe=h)
    kopf = s.tr("kopf", "Kopfzeile mit Doppelpunkt", "header line with colon", "cabecera con dos puntos",
                "带冒号的首行", fr="en-tête avec deux-points", tr="iki nokta üst üsteli başlık")
    block = s.tr("block", "Block: läuft nur,\nwenn die Bedingung\nwahr ist", "block: runs only\nif the condition\nis true",
                 "bloque: solo se ejecuta\nsi la condición\nes verdadera", "代码块：仅当\n条件为真时执行",
                 fr="bloc : ne s’exécute\nque si la condition\nest vraie", tr="blok: yalnızca\nkoşul doğruysa\nçalışır")
    weiter = s.tr("weiter", "wieder links:\ngehört nicht dazu", "back to the left:\nnot part of it",
                  "de nuevo a la izquierda:\nno forma parte", "回到左侧：\n不属于该块", fr="de nouveau à gauche :\nn’en fait pas partie",
                  tr="yeniden solda:\nbloğa ait değil")
    xb = 0.9
    s.linie(None, (xb, yc + 0.05), (xb, yc - zeile * 1.05), dicke=3)
    s.linie(None, (xb, yc - 0.5 * zeile), (xb + 0.15, yc - 0.5 * zeile), dicke=3)
    s.text(None, block, (xb + 0.25, yc - 0.5 * zeile), KLEIN, "left", BLAU)
    s.text(None, kopf, (xb + 0.25, yc + zeile), KLEIN, "left")
    s.linie(None, (-2.1, yc + zeile), (xb + 0.15, yc + zeile), farbe=HELLGRAU, dicke=2)
    s.text(None, weiter, (xb + 0.25, yc - 2 * zeile - 0.1), KLEIN, "left", GRAU)
    s.linie(None, (-0.9, yc - 2 * zeile), (xb + 0.15, yc - 2 * zeile), farbe=HELLGRAU, dicke=2)
    s.speichern()


def k3elif():
    """Flussdiagramm von if, elif und else."""
    s = Szene("prog/k3elif")
    ja, nein = ja_nein(s)
    lesen = s.tr("lesen", "u einlesen", "read u", "leer u", "读取 u", fr="lire u", tr="u'yu oku")
    niedrig = s.tr("niedrig", "„zu niedrig“", "“too low”", "«demasiado baja»", "“过低”", fr="« trop basse »", tr="„çok düşük“")
    ok = s.tr("ok", "„in Ordnung“", "“OK”", "«en orden»", "“正常”", fr="« correct »", tr="„uygun“")
    hoch = s.tr("hoch", "„zu hoch“", "“too high”", "«demasiado alta»", "“过高”", fr="« trop haute »", tr="„çok yüksek“")
    weiter = s.tr("weiter", "weiter nach dem letzten Block", "continue after the last block", "seguir tras el último bloque",
                  "在最后一个代码块之后继续", fr="suite après le dernier bloc", tr="son bloktan sonra devam")
    x, xr, xj = -1.4, 1.75, 3.05
    kasten(s, (x, 2.55), 1.6, 0.46, lesen)
    raute(s, (x, 1.4), 1.9, 0.95, r"\texttt{u < 4.75}?")
    raute(s, (x, -0.1), 1.9, 0.95, r"\texttt{u <= 5.25}?")
    kasten(s, (xr, 1.4), 1.9, 0.46, niedrig)
    kasten(s, (xr, -0.1), 1.9, 0.46, ok)
    kasten(s, (x, -1.35), 1.6, 0.46, hoch)
    kasten(s, (x + 0.6, -2.5), 3.9, 0.46, weiter)
    pf(s, (x, 2.32), (x, 1.88))
    pf(s, (x + 0.95, 1.4), (xr - 0.95, 1.4))
    pf(s, (x + 0.95, -0.1), (xr - 0.95, -0.1))
    pf(s, (x, 0.92), (x, 0.38))
    pf(s, (x, -0.58), (x, -1.12))
    pf(s, (x, -1.58), (x, -2.27))
    s.text(None, ja, (x + 1.25, 1.6), KLEIN, "center")
    s.text(None, ja, (x + 1.25, 0.1), KLEIN, "center")
    s.text(None, nein, (x + 0.12, 0.65), KLEIN, "left")
    s.text(None, nein, (x + 0.12, -0.85), KLEIN, "left")
    s.linie(None, (xr + 0.95, 1.4), (xj, 1.4), dicke=2.5)
    s.linie(None, (xr + 0.95, -0.1), (xj, -0.1), dicke=2.5)
    s.linie(None, (xj, 1.4), (xj, -2.5), dicke=2.5)
    pf(s, (xj, -2.5), (x + 2.55, -2.5))
    for y, t in ((1.4, "if"), (-0.1, "elif"), (-1.35, "else")):
        s.formel(r"\texttt{%s}" % t, mitte=(-3.4, y), hoehe=0.15, farbe=GRAU)
    s.speichern()


# ------------------------------------------------------------------ Abschnitt 3
def k3while():
    """Flussdiagramm der while-Schleife aus zaehlen.py."""
    s = Szene("prog/k3while")
    ja, nein = ja_nein(s)
    zurueck = s.tr("zurueck", "zurück\nzur Frage", "back to\nthe question", "vuelta a\nla pregunta", "回到\n判断", fr="retour à\nla question",
                   tr="soruya\ngeri dön")
    x = -0.6
    code_kasten(s, (x, 2.3), 1.9, 0.46, r"\texttt{zaehler = 1}")
    raute(s, (x, 1.0), 2.3, 1.0, r"\texttt{zaehler <= 3}?")
    code_kasten(s, (x, -0.65), 3.4, 0.85, r'\begin{array}{l}\texttt{print("Durchlauf", zaehler)}\\'
                                            r'\texttt{zaehler = zaehler + 1}\end{array}', h=0.4)
    code_kasten(s, (2.55, 1.0), 2.05, 0.46, r'\texttt{print("fertig, ...")}', h=0.16)
    pf(s, (x, 2.07), (x, 1.5))
    pf(s, (x, 0.5), (x, -0.22))
    s.text(None, ja, (x + 0.12, 0.15), KLEIN, "left")
    pf(s, (x + 1.15, 1.0), (1.52, 1.0))
    s.text(None, nein, (x + 1.5, 1.2), KLEIN, "center")
    s.linie(None, (x, -1.08), (x, -1.55), dicke=2.5)
    s.linie(None, (x, -1.55), (-2.65, -1.55), dicke=2.5)
    s.linie(None, (-2.65, -1.55), (-2.65, 1.0), dicke=2.5)
    pf(s, (-2.65, 1.0), (x - 1.15, 1.0))
    s.text(None, zurueck, (-1.6, -2.0), KLEIN, "center", GRAU)
    s.speichern()


# ------------------------------------------------------------------ Abschnitt 4
def k3range():
    """range(2, 11, 3) auf dem Zahlenstrahl: 2, 5, 8; der Stopp 11 gehört nicht dazu."""
    s = Szene("prog/k3range")
    k, x0 = 0.56, -3.1

    def x(v):
        return x0 + v * k
    s.pfeil((x(-0.4), 0), (x(11.7), 0), farbe=GRAU, dicke=2.5, spitze=0.12)
    for v in range(12):
        s.linie(None, (x(v), 0.06), (x(v), -0.06), farbe=GRAU, dicke=2)
        s.text(None, str(v), (x(v), -0.3), KLEIN, "center", GRAU)
    for v in (2, 5, 8):
        s.punkt(None, x(v), 0, farbe=BLAU, r=0.1)
    s.kreis(None, x(11), 0, 0.1, farbe=ROT, dicke=3, fuellung="#ffffff", deckung=1)
    for a in (2, 5, 8):
        m = x(a + 1.5)
        s.weg(None, "%g + %g*cos(t)" % (m, 1.5 * k), "0.18 + 0.45*sin(t)", 0, math.pi, farbe=ORANGE, dicke=3)
        s.pfeil((m + 1.5 * k - 0.02, 0.32), (m + 1.5 * k, 0.17), farbe=ORANGE, dicke=3, spitze=0.1)
        s.text(None, "+3", (m, 0.85), KLEIN, "center", ORANGE)
    s.formel(r"\texttt{range(2, 11, 3)}\ \to\ 2,\ 5,\ 8", mitte=(0, 1.55), hoehe=0.24)
    s.text(None, "start", (x(2), -0.75), KLEIN, "center", BLAU)
    s.text(None, "stop", (x(11), -0.75), KLEIN, "center", ROT)
    s.speichern()


# ------------------------------------------------------------------ Abschnitt 5 (Rechenbilder)
def k3rquadrate():
    """Summe der Quadrate von 1 bis 5 Schritt für Schritt."""
    s = Szene("prog/k3rquadrate")
    s.summe("i^2", von=1, bis=5)
    s.speichern()


def k3rmittel():
    """Mittelwert der vier Messwerte aus mittelwert.py."""
    s = Szene("prog/k3rmittel")
    s.formel(r"\begin{aligned}\bar U=\frac14\sum_{k=1}^{4}U_k&=\frac14\,(U_1+U_2+U_3+U_4)\\"
             r"&=\frac14\,(4.98\,\mathrm V+5.02\,\mathrm V+5.01\,\mathrm V+4.99\,\mathrm V)\\"
             r"&=\frac14\cdot 20.00\,\mathrm V\\&=5.00\,\mathrm V\end{aligned}", mitte=(0, 0), hoehe=2.2)
    s.speichern()


# ------------------------------------------------------------------ Abschnitt 7
def k3bisektion():
    """Bisektion für die Wurzel aus 2 als Intervallschachtelung, Schritt 0 bis 5."""
    s = Szene("prog/k3bisektion")
    k, x0 = 2.95, -2.65

    def x(v):
        return x0 + v * k
    zeilen = ((0, 2), (1, 2), (1, 1.5), (1.25, 1.5), (1.375, 1.5), (1.375, 1.4375))
    s.tr("schritt", "Schritt", "step", "paso", "步骤", fr="étape", tr="adım")
    for n, (lo, hi) in enumerate(zeilen):
        y = 1.9 - 0.62 * n
        s.linie(None, (x(lo), y), (x(hi), y), farbe=BLAU, dicke=9)
        m = (lo + hi) / 2
        s.linie(None, (x(m), y + 0.17), (x(m), y - 0.17), farbe=SCHWARZ, dicke=3)
        s.text(None, "@{schritt} %d" % n, (x(0) - 0.15, y), KLEIN, "right")
    s.linie(None, (x(-0.03), -1.95), (x(2.05), -1.95), farbe=GRAU, dicke=2.5)
    for v, t in ((0, "0"), (0.5, "0.5"), (1, "1"), (1.5, "1.5"), (2, "2")):
        s.linie(None, (x(v), -1.89), (x(v), -2.01), farbe=GRAU, dicke=2)
        s.text(None, t, (x(v), -2.25), KLEIN, "center", GRAU)
    w = x(math.sqrt(2))
    s.linie(None, (w, -1.95), (w, 2.25), farbe=ROT, dicke=2.5, dash=DASH)
    s.formel(r"\sqrt2", mitte=(w, 2.5), hoehe=0.24, farbe=ROT)
    s.speichern()


# ------------------------------------------------------------------ Abschnitt 8
def k3newton():
    """Zwei Newton-Schritte für f(x) = x^2 - 2: Tangenten bei 2 und bei 1,5."""
    s = Szene("prog/k3newton")
    a = s.achsen((1.2, 2.1, 0.25), (-0.6, 2.3, 0.5), breite=5.6, hoehe=3.8, mitte=(0.2, 0), xl="x", yl="f(x)",
                 kreuz=True, xticks="1.25;1.75;2", yticks="-0.5;0.5;1;1.5;2")
    s.kurve(a, "x^2-2", x=(1.2, 2.08), farbe=BLAU, dicke=5)
    s.kurve(a, "2+4*(x-2)", x=(1.38, 2.05), farbe=ORANGE, dicke=4)
    s.kurve(a, "0.25+3*(x-1.5)", x=(1.36, 1.62), farbe=GRUEN, dicke=4)
    s.linie(a, (2, 0), (2, 2), farbe=GRAU, dicke=2, dash=DASH)
    s.linie(a, (1.5, 0), (1.5, 0.25), farbe=GRAU, dicke=2, dash=DASH)
    s.punkt(a, 2, 2, r=0.07)
    s.punkt(a, 1.5, 0.25, r=0.07)
    s.punkt(a, 1.5, 0, farbe=ORANGE, r=0.07)
    s.punkt(a, 1.41667, 0, farbe=GRUEN, r=0.07)
    s.text(a, "g₀ = 2", (1.97, 2.15), KLEIN, "right")
    s.text(a, "g₁ = 1.5", (1.47, 0.42), KLEIN, "right")
    s.text(a, "g₁", (1.5, -0.25), KLEIN, "center", ORANGE)
    s.text(a, "g₂", (1.39, -0.25), KLEIN, "right", GRUEN)
    s.speichern()


def k3fehler():
    """Fehler über der Schrittzahl, logarithmisch: Schrittverfahren, Bisektion, Newton."""
    s = Szene("prog/k3fehler")
    s.welt()
    xl = s.tr("schritte", "Schritte n", "steps n", "pasos n", "步数 n", fr="étapes n", tr="adım n")
    yl = s.tr("fehler", "Fehler |gₙ − √2|", "error |gₙ − √2|", "error |gₙ − √2|", "误差 |gₙ − √2|", fr="erreur |gₙ − √2|",
              tr="hata |gₙ − √2|")
    a = s.achsen((0, 42, 5), (1e-16, 10), breite=5.6, hoehe=3.6, mitte=(0.35, 0.55), xl=xl, yl=yl, ylog=True,
                 yticks="1e-16;1e-12;1e-8;1e-4;1", gitter=True, rahmen=True)
    w = math.sqrt(2)
    s.daten(a, [(n, abs(n * 0.01 - w)) for n in range(0, 43)], farbe=GRAU, dicke=3)
    lo, hi = 0.0, 2.0
    bis = [(0, abs(1.0 - w))]
    for n in range(1, 42):
        m = (lo + hi) / 2
        if m * m < 2:
            lo = m
        else:
            hi = m
        bis.append((n, abs((lo + hi) / 2 - w)))
    s.daten(a, bis, farbe=BLAU, dicke=3, marker=True, marker_r=0.035)
    s.daten(a, [(n, 2.0 ** -n) for n in range(0, 42)], farbe=BLAU, dicke=2, dash=DASH)
    g = 2.0
    newt = [(0, abs(g - w))]
    for n in range(1, 5):
        g = g - (g * g - 2) / (2 * g)
        newt.append((n, abs(g - w)))
    s.daten(a, newt, farbe=ROT, dicke=4, marker=True, marker_r=0.05)
    hinweis = s.tr("hinweis", "Schritt 5: genau math.sqrt(2)", "step 5: exactly math.sqrt(2)", "paso 5: exactamente math.sqrt(2)",
                   "第 5 步：恰为 math.sqrt(2)", fr="étape 5 : exactement math.sqrt(2)", tr="5. adım: tam olarak math.sqrt(2)")
    s.text(a, hinweis, (5.5, 1e-14), KLEIN, "left", ROT)
    schritt = s.tr("l_schritt", "Schrittverfahren (h = 0.01)", "stepping (h = 0.01)", "pasos fijos (h = 0.01)", "定步法 (h = 0.01)",
                   fr="pas fixes (h = 0.01)", tr="sabit adım (h = 0.01)")
    bisek = s.tr("l_bisek", "Bisektion", "bisection", "bisección", "二分法", fr="bissection", tr="ikiye bölme")
    newton = s.tr("l_newton", "Newton", "Newton", "Newton", "牛顿法", fr="Newton", tr="Newton")
    schranke = s.tr("l_schranke", "Schranke 2/2ⁿ⁺¹", "bound 2/2ⁿ⁺¹", "cota 2/2ⁿ⁺¹", "上界 2/2ⁿ⁺¹", fr="borne 2/2ⁿ⁺¹",
                    tr="sınır 2/2ⁿ⁺¹")
    s.legende(None, [(schritt, GRAU, "-"), (bisek, BLAU, "-o"), (newton, ROT, "-o"), (schranke, BLAU, "--")],
              (-2.4, -2.5), groesse=KLEIN)
    s.speichern()


# ------------------------------------------------------------------ Abschnitt 9
def k3diode():
    """Diodenkennlinie und Arbeitsgerade, Schnittpunkt = Arbeitspunkt."""
    s = Szene("prog/k3diode")
    xl = s.tr("uachse", "U in V", "U in V", "U en V", "U / V", fr="U en V", tr="U (V)")
    yl = s.tr("iachse", "Strom in mA", "current in mA", "corriente en mA", "电流 / mA", fr="courant en mA", tr="akım (mA)")
    a = s.achsen((0.4, 0.66, 0.05), (0, 10, 2), breite=5.6, hoehe=3.4, mitte=(0.4, 0.1), xl=xl, yl=yl, gitter=True, rahmen=True)
    s.kurve(a, "1e-9*(exp(x/0.02585)-1)", x=(0.4, 0.603), farbe=BLAU, dicke=5)
    s.kurve(a, "5-x", x=(0.4, 0.66), farbe=ORANGE, dicke=5)
    s.punkt(a, 0.574147, 4.425853, r=0.08)
    ap = s.tr("ap", "Arbeitspunkt 0.574 V, 4.43 mA", "operating point 0.574 V, 4.43 mA", "punto de trabajo 0.574 V, 4.43 mA",
              "工作点 0.574 V，4.43 mA", fr="point de fonctionnement 0.574 V, 4.43 mA", tr="çalışma noktası 0.574 V, 4.43 mA")
    s.text(a, ap, (0.566, 5.4), KLEIN, "right")
    diode = s.tr("l_diode", "Diode I_D", "diode I_D", "diodo I_D", "二极管 I_D", fr="diode I_D", tr="diyot I_D")
    wid = s.tr("l_wid", "Widerstand I_R = (U₀ − U)/R", "resistor I_R = (U₀ − U)/R", "resistencia I_R = (U₀ − U)/R",
               "电阻 I_R = (U₀ − U)/R", fr="résistance I_R = (U₀ − U)/R", tr="direnç I_R = (U₀ − U)/R")
    s.legende(a, [(diode, BLAU, "-"), (wid, ORANGE, "-")], (0.41, 9.3), groesse=KLEIN)
    s.speichern()


SZENEN = (k3if, k3block, k3elif, k3while, k3range, k3rquadrate, k3rmittel, k3bisektion, k3newton, k3fehler, k3diode)

for f in SZENEN:
    f()
