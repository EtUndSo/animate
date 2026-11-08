"""Programmieren, Python 2 (C:\\Bücher\\EtUndSo\\Programmieren\\Arbeitshefte\\kap2_stufen.tex, kap2_stufen_b.tex): Abbildungen.

Szenenname prog/k2<name> = \\label{fig:k2<name>} im Heft. Stil wie tools/szenen/prog_teil1.py (Kästen, Pfeile, Code mit s.formel).
Bauen:  python tools/szenen/prog_teil2.py
Export: python tools/export_szenen.py prog/k2objekt prog/k2rest prog/k2rbinaer prog/k2rbyte prog/k2rnull prog/k2zahlenstrahl
            prog/k2bitfelder prog/k2rfloat prog/k2etikett prog/k2zeiger prog/k2rc
Rechenbilder (Summe Schritt für Schritt): k2rbyte mit s.summe; k2rbinaer und k2rfloat mit s.formel, weil die Summanden dort
Ziffern eines Bitmusters bzw. Felder eines float sind und keine Formel im Laufindex; k2rnull mit s.formel, weil s.summe den
Summanden 3/131072 nur als Dezimalzahl zeigt und das Heft den Laufindex k benutzt.
Code mit Dezimalpunkt in s.formel als 4{.}0 schreiben, sonst macht die deutsche Fassung daraus 4,0.
Die Zahlen prüft C:\\Bücher\\EtUndSo\\Programmieren\\Arbeitshefte\\rechnung_kap2.py.
"""
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


def kasten(s, mitte, breite, hoehe, text, groesse=MITTEL, farbe=SCHWARZ, textfarbe=None, fuellung="#ffffff", dash="", dicke=2.5):
    """Abgerundeter Kasten mit zentriertem Text (mehrzeilig mit \\n)."""
    s.box("", mitte, breite=breite, hoehe=hoehe, form="round", farbe=farbe, fuellung=fuellung, deckung=1, dicke=dicke, dash=dash)
    if text:
        s.text(None, text, mitte, groesse, "center", textfarbe or farbe)


def tt(text):
    return r"\texttt{%s}" % text


# ------------------------------------------------------------------ Abschnitt 1
def k2objekt():
    """Drei Objekte als Kästen: Aufschrift (Art des Werts), Wert, Platznummer."""
    s = Szene("prog/k2objekt")
    art = [s.tr("a1", "Art: ganze Zahl", "kind: integer", "tipo: entero", "种类：整数", fr="type : entier", tr="tür: tam sayı"),
           s.tr("a2", "Art: Zahl mit Komma", "kind: decimal number", "tipo: número decimal", "种类：小数", fr="type : nombre décimal",
                tr="tür: ondalık sayı"),
           s.tr("a3", "Art: Text", "kind: text", "tipo: texto", "种类：文本", fr="type : texte", tr="tür: metin")]
    s.tr("platz", "Platz Nr.", "place no.", "lugar n.º", "位置编号", fr="place n°", tr="yer no.")
    for k, (x, wert, nr) in enumerate(((-2.35, "42", 1000), (0.0, "4.0", 1032), (2.35, '"42"', 1064))):
        s.box("", (x, 0), breite=2.15, hoehe=1.5, form="round", farbe=SCHWARZ, fuellung="#ffffff", deckung=1, dicke=2.5)
        s.box("", (x, 0.5), breite=2.15, hoehe=0.5, form="rect", farbe=SCHWARZ, fuellung=BLAU_HELL, deckung=1, dicke=2)
        s.text(None, art[k], (x, 0.5), KLEIN, "center")
        s.formel(tt(wert.replace(".", r".}\texttt{")), mitte=(x, -0.25), hoehe=0.32)   # 4.}\texttt{0: Code bleibt mit Punkt
        s.text(None, "@{platz} %d" % nr, (x, -1.05), KLEIN, "center", GRAU)
    s.speichern()


# ------------------------------------------------------------------ Abschnitt 2
def k2rest():
    """Ganzzahldivision durch 2 auf dem Zahlenstrahl: nächstes Vielfaches links von a, Abstand = Rest."""
    s = Szene("prog/k2rest")
    k = 0.34                                                # eine Einheit des Zahlenstrahls in Szeneneinheiten

    def x(v):
        return v * k
    s.pfeil((x(-9.6), 0), (x(9.6), 0), farbe=GRAU, dicke=2.5, spitze=0.13)
    for v in range(-9, 10):
        s.linie(None, (x(v), 0.06), (x(v), -0.06), farbe=GRAU, dicke=2)
    for v in range(-8, 9, 2):
        s.punkt(None, x(v), 0, farbe=BLAU, r=0.06)
        s.text(None, str(v), (x(v), -0.3), KLEIN, "center", BLAU)
    for v in (-7, 7):
        s.linie(None, (x(v), 0.17), (x(v), -0.17), farbe=ROT, dicke=4)
        s.text(None, str(v), (x(v), -0.3), KLEIN, "center", ROT)
    rest = s.tr("rest", "Rest 1", "remainder 1", "resto 1", "余数 1", fr="reste 1", tr="kalan 1")
    for a, q in ((-7, -4), (7, 3)):
        links = q * 2
        s.linie(None, (x(links), 0.28), (x(a), 0.28), farbe=ROT, dicke=5)
        s.text(None, rest, (x(links + 0.5), 0.55), KLEIN, "center", ROT)
        tex = r"a=%d:\ (%d)\cdot 2=%d" % (a, q, links) if q < 0 else r"a=%d:\ %d\cdot 2=%d" % (a, q, links)
        s.formel(tex, mitte=(x(links + 0.5) + (0.45 if q < 0 else -0.2), 1.05), hoehe=0.3 if q < 0 else 0.24)
    blau = s.tr("blau", "blau: Vielfache von 2", "blue: multiples of 2", "azul: múltiplos de 2", "蓝色：2 的倍数",
                fr="bleu : multiples de 2", tr="mavi: 2'nin katları")
    s.text(None, blau, (x(-9.6), -0.75), KLEIN, "left", BLAU)
    s.speichern()


# ------------------------------------------------------------------ Abschnitt 3 (Rechenbilder)
def k2rbinaer():
    """Wert der Binärzahl 10011_2 Schritt für Schritt."""
    s = Szene("prog/k2rbinaer")
    s.formel(r"\begin{aligned}10011_2=\sum_{i=0}^{4}b_i\,2^i&=b_4\cdot2^4+b_3\cdot2^3+b_2\cdot2^2+b_1\cdot2^1+b_0\cdot2^0\\"
             r"&=1\cdot16+0\cdot8+0\cdot4+1\cdot2+1\cdot1\\&=16+0+0+2+1=19\end{aligned}", mitte=(0, 0), hoehe=1.38)
    s.speichern()


def k2rbyte():
    """Größter Wert eines Bytes: Summe der Stellenwerte 2^0 bis 2^7."""
    s = Szene("prog/k2rbyte")
    s.summe("2^i", von=0, bis=7, summanden=8)
    s.speichern()


def k2rnull():
    """Die ersten vier Paare von Einsen im Binärbruch von 0,1."""
    s = Szene("prog/k2rnull")                             # s.formel: s.summe zeigt 3/131072 nur als Dezimalzahl
    s.formel(r"\begin{aligned}\sum_{k=1}^{4}\frac{3}{2^{4k+1}}&=\frac{3}{2^{5}}+\frac{3}{2^{9}}+\frac{3}{2^{13}}+\frac{3}{2^{17}}\\"
             r"&=\frac{3}{32}+\frac{3}{512}+\frac{3}{8192}+\frac{3}{131072}=\frac{13107}{131072}\approx0.0999985\end{aligned}",
             mitte=(0, 0), hoehe=1.24)
    s.speichern()


# ------------------------------------------------------------------ Abschnitt 4
def k2zahlenstrahl():
    """Die 16 Zahlen eines Gleitkommaformats mit 3 Binärstellen, Exponenten -1 bis 2: Abstände verdoppeln sich."""
    s = Szene("prog/k2zahlenstrahl")
    k, x0 = 0.86, -3.25

    def x(v):
        return x0 + v * k
    s.pfeil((x(-0.15), 0), (x(7.7), 0), farbe=GRAU, dicke=2.5, spitze=0.13)
    s.linie(None, (x(0), 0.07), (x(0), -0.07), farbe=GRAU, dicke=2)
    gruppen = ((-1, BLAU, "1/8"), (0, GRUEN, "1/4"), (1, ORANGE, "1/2"), (2, ROT, "1"))
    s.tr("abst", "Abstand", "spacing", "separación", "间距", fr="écart", tr="aralık")
    for E, farbe, a in gruppen:
        werte = [m * 2.0 ** E for m in (1, 1.25, 1.5, 1.75)]
        for v in werte:
            s.linie(None, (x(v), 0.17), (x(v), -0.17), farbe=farbe, dicke=4)
        y = 0.95 if E in (-1, 1) else 0.5
        mitte = x((werte[0] + werte[-1]) / 2)
        s.linie(None, (x(werte[0]), 0.27), (x(werte[-1]), 0.27), farbe=farbe, dicke=3)
        tx = mitte - 0.35 if E == -1 else mitte
        if E == -1:
            s.linie(None, (mitte, 0.3), (tx, y - 0.14), farbe=farbe, dicke=2)
        s.text(None, "E = %d" % E, (tx, y + 0.27), KLEIN, "center", farbe)
        s.text(None, "@{abst} %s" % a, (tx, y), KLEIN, "center", farbe)
    for v in range(0, 8):
        s.text(None, str(v), (x(v), -0.4), KLEIN, "center", GRAU)
    s.text(None, "0.5", (x(0.5), -0.4), KLEIN, "center", GRAU)
    fehlt = s.tr("fehlt", "6.5 fehlt:\nrunden auf 6 oder 7", "6.5 is missing:\nround to 6 or 7", "falta 6.5:\nredondear a 6 o 7",
                 "没有 6.5：\n舍入为 6 或 7", fr="6.5 manque :\narrondir à 6 ou 7", tr="6.5 yok:\n6 veya 7'ye yuvarla")
    s.pfeil((x(6.5), -0.85), (x(6.5), -0.2), farbe=GRAU, dicke=2.5, spitze=0.12)
    s.text(None, fehlt, (x(6.5), -1.25), KLEIN, "center", GRAU)
    s.speichern()


def k2bitfelder():
    """Die drei Felder eines float für 6,5 und für 0,1: Vorzeichen, Exponentenfeld, Mantissenfeld."""
    s = Szene("prog/k2bitfelder")
    xs, xc, xt = -2.85, -1.35, 1.65                        # Mitten der drei Felder
    bs, bc, bt = 0.45, 2.45, 3.45                          # Breiten
    zeilen = ((0.55, "6.5", "0", "10000000001", "1010 0000 0000 … 0000"),
              (-0.35, "0.1", "0", "01111111011", "1001 1001 1001 … 1010"))
    for y, name, sbit, cbits, tbits in zeilen:
        s.text(None, name, (-3.25, y), MITTEL, "right")
        s.box("", (xs, y), breite=bs, hoehe=0.6, form="rect", farbe=ROT, fuellung=ROT_HELL, deckung=1, dicke=2)
        s.box("", (xc, y), breite=bc, hoehe=0.6, form="rect", farbe=BLAU, fuellung=BLAU_HELL, deckung=1, dicke=2)
        s.box("", (xt, y), breite=bt, hoehe=0.6, form="rect", farbe=GRUEN, fuellung=GRUEN_HELL, deckung=1, dicke=2)
        s.formel(tt(sbit), mitte=(xs, y), hoehe=0.2)
        s.formel(tt(cbits), mitte=(xc, y), hoehe=0.2)
        s.formel(r"\texttt{%s}" % tbits, mitte=(xt, y), hoehe=0.16)
    vz = s.tr("vz", "Vorzeichen s\n1 Bit", "sign s\n1 bit", "signo s\n1 bit", "符号 s\n1 位", fr="signe s\n1 bit", tr="işaret s\n1 bit")
    ef = s.tr("ef", "Exponentenfeld c\n11 Bit", "exponent field c\n11 bits", "campo del exponente c\n11 bits", "指数字段 c\n11 位",
              fr="champ d’exposant c\n11 bits", tr="üs alanı c\n11 bit")
    mf = s.tr("mf", "Mantissenfeld t\n52 Bit", "significand field t\n52 bits", "campo de la mantisa t\n52 bits", "尾数字段 t\n52 位",
              fr="champ de mantisse t\n52 bits", tr="mantis alanı t\n52 bit")
    s.text(None, vz, (xs - 0.05, -1.15), KLEIN, "center", ROT)
    s.text(None, ef, (xc, -1.15), KLEIN, "center", BLAU)
    s.text(None, mf, (xt, -1.15), KLEIN, "center", GRUEN)
    s.speichern()


def k2rfloat():
    """Wert des float für 0.1 aus seinen drei Feldern."""
    s = Szene("prog/k2rfloat")
    s.formel(r"\begin{aligned}x&=(-1)^s\cdot\Bigl(1+\frac{t}{2^{52}}\Bigr)\cdot2^{\,c-1023}\\"
             r"&=(-1)^0\cdot\Bigl(1+\frac{2702159776422298}{4503599627370496}\Bigr)\cdot2^{\,1019-1023}\\"
             r"&=1\cdot\frac{7205759403792794}{4503599627370496}\cdot\frac{1}{16}\\"
             r"&=\frac{3602879701896397}{36028797018963968}\\"
             r"&=0.1000000000000000055511151231257827\ldots\end{aligned}",
             mitte=(0, 0), hoehe=2.75)
    s.speichern()


# ------------------------------------------------------------------ Abschnitt 6
def k2etikett():
    """Zustandsdiagramme: nach y = x hängen zwei Namen an einem Objekt; x = x + 1 bindet x an ein neues Objekt."""
    s = Szene("prog/k2etikett")
    namen = s.tr("namen", "Namen", "names", "nombres", "名称", fr="noms", tr="adlar")
    objekte = s.tr("objekte", "Objekte", "objects", "objetos", "对象", fr="objets", tr="nesneler")
    neu = s.tr("neu", "neues Objekt", "new object", "objeto nuevo", "新对象", fr="nouvel objet", tr="yeni nesne")
    s.formel(r"\texttt{x = 5; y = x}", mitte=(-1.95, 1.75), hoehe=0.25)
    s.formel(r"\texttt{x = x + 1}", mitte=(1.85, 1.75), hoehe=0.2)
    s.linie(None, (0.05, 1.95), (0.05, -1.3), farbe=HELLGRAU, dicke=2)
    for x0 in (-3.4, 0.45):
        s.text(None, namen, (x0 + 0.3, 1.25), KLEIN, "center", GRAU)
        s.text(None, objekte, (x0 + 2.2, 1.25), KLEIN, "center", GRAU)
        for y, n in ((0.6, "x"), (-0.6, "y")):
            s.box("", (x0 + 0.3, y), breite=0.6, hoehe=0.42, form="round", fuellung="#ffffff", deckung=1, dicke=2.5)
            s.formel(tt(n), mitte=(x0 + 0.3, y), hoehe=0.17)
    # links: ein Objekt 5
    kasten(s, (-1.2, 0.0), 1.1, 0.75, "", fuellung=BLAU_HELL)
    s.text(None, "int", (-1.2, 0.17), KLEIN, "center", GRAU)
    s.formel(tt("5"), mitte=(-1.2, -0.13), hoehe=0.2)
    s.pfeil((-2.8, 0.6), (-1.77, 0.12), dicke=3, spitze=0.14)
    s.pfeil((-2.8, -0.6), (-1.77, -0.12), dicke=3, spitze=0.14)
    # rechts: x am neuen Objekt 6, y am alten 5
    kasten(s, (2.65, 0.6), 1.1, 0.75, "", farbe=ORANGE, fuellung=ORANGE_HELL)
    s.text(None, "int", (2.65, 0.77), KLEIN, "center", GRAU)
    s.formel(tt("6"), mitte=(2.65, 0.47), hoehe=0.2)
    kasten(s, (2.65, -0.6), 1.1, 0.75, "", fuellung=BLAU_HELL)
    s.text(None, "int", (2.65, -0.43), KLEIN, "center", GRAU)
    s.formel(tt("5"), mitte=(2.65, -0.73), hoehe=0.2)
    s.pfeil((1.05, 0.6), (2.08, 0.6), farbe=ORANGE, dicke=3, spitze=0.14)
    s.pfeil((1.05, -0.6), (2.08, -0.6), dicke=3, spitze=0.14)
    s.text(None, neu, (2.65, 0.0), KLEIN, "center", ORANGE)
    s.speichern()


# ------------------------------------------------------------------ Abschnitt 9
def k2zeiger():
    """z = 3 + 4j als Zeiger, dazu z* gestrichelt; rechts die Python-Ausdrücke."""
    s = Szene("prog/k2zeiger")
    k, x0 = 0.48, -3.2

    def p(re, im):
        return (x0 + re * k, im * k)
    s.pfeil(p(-0.6, 0), p(4.8, 0), farbe=GRAU, dicke=2.5, spitze=0.12)
    s.pfeil(p(0, -4.8), p(0, 4.8), farbe=GRAU, dicke=2.5, spitze=0.12)
    s.text(None, "Re", (p(4.8, 0)[0] + 0.08, -0.22), KLEIN, "left", GRAU)
    s.text(None, "Im", (p(0, 4.8)[0] + 0.12, p(0, 4.8)[1]), KLEIN, "left", GRAU)
    for v in (1, 2, 3, 4):
        s.linie(None, (p(v, 0)[0], 0.05), (p(v, 0)[0], -0.05), farbe=GRAU, dicke=2)
    for v in (-4, -2, 2, 4):
        s.linie(None, (x0 - 0.05, v * k), (x0 + 0.05, v * k), farbe=GRAU, dicke=2)
        s.text(None, str(v), (x0 - 0.12, v * k), KLEIN, "right", GRAU)
    s.linie(None, p(3, 4), p(3, 0), farbe=HELLGRAU, dicke=2, dash=DASH)
    s.linie(None, p(3, 4), p(0, 4), farbe=HELLGRAU, dicke=2, dash=DASH)
    s.pfeil(p(0, 0), p(3, 4), farbe=BLAU, dicke=5, spitze=0.16)
    s.pfeil(p(0, 0), p(3, -4), farbe=GRAU, dicke=3, spitze=0.14, dash=DASH)
    s.formel(r"z=3+4\mathrm j", mitte=(p(3, 4)[0] + 0.6, p(3, 4)[1] + 0.2), hoehe=0.22, farbe=BLAU)
    s.formel(r"z^*=3-4\mathrm j", mitte=(p(3, -4)[0] + 0.65, p(3, -4)[1] - 0.2), hoehe=0.24, farbe=GRAU)
    s.formel(r"|z|=5", mitte=(p(1.1, 2.4)[0] - 0.05, p(1.1, 2.4)[1] + 0.12), hoehe=0.22, farbe=BLAU)
    s.weg(None, "%g + 0.5*cos(t)" % x0, "0.5*sin(t)", 0, 0.9273, farbe=ORANGE, dicke=3)
    s.text(None, "φ", (x0 + 0.7, 0.3), KLEIN, "center", ORANGE)
    zeilen = ["Re z = 3:  z.real", "Im z = 4:  z.imag", "|z| = 5:  abs(z)",
              "φ ≈ 0.9273:  cmath.phase(z)", "z*:  z.conjugate()"]
    for j, z in enumerate(zeilen):
        y = 1.4 - 0.45 * j if j < 3 else -0.6 - 0.45 * (j - 3)
        s.text(None, z, (0.75, y), KLEIN, "left")
    s.speichern()


def k2rc():
    """Zeigerdiagramm der Impedanz des RC-Glieds: R, 1/(jωC), Z mit Betrag und Phase."""
    s = Szene("prog/k2rc")
    k, x0, y0 = 1 / 500, -2.2, 1.4                        # 1 Szeneneinheit = 500 Ohm

    def p(re, im):
        return (x0 + re * k, y0 + im * k)
    s.pfeil(p(-200, 0), p(1700, 0), farbe=GRAU, dicke=2.5, spitze=0.12)
    s.pfeil(p(0, -2150), p(0, 350), farbe=GRAU, dicke=2.5, spitze=0.12)
    s.text(None, "Re Z", (p(1700, 0)[0] + 0.08, y0), KLEIN, "left", GRAU)
    s.text(None, "Im Z", (p(0, 350)[0] + 0.12, p(0, 350)[1]), KLEIN, "left", GRAU)
    for v in (-500, -1000, -1500):
        s.linie(None, (x0 - 0.05, p(0, v)[1]), (x0 + 0.05, p(0, v)[1]), farbe=GRAU, dicke=2)
        s.text(None, "%d Ω" % v, (x0 - 0.12, p(0, v)[1]), KLEIN, "right", GRAU)
    zr = (1000, -1591.5494309189537)
    s.pfeil(p(0, 0), p(1000, 0), farbe=BLAU, dicke=5, spitze=0.15)
    s.pfeil(p(1000, 0), p(*zr), farbe=ORANGE, dicke=5, spitze=0.15)
    s.pfeil(p(0, 0), p(*zr), farbe=ROT, dicke=5, spitze=0.15)
    s.formel(r"R=1000\,\Omega", mitte=(p(500, 0)[0], y0 + 0.25), hoehe=0.2, farbe=BLAU)
    s.formel(r"\frac{1}{\mathrm j\omega C}=-\mathrm j\,1591.5\,\Omega", mitte=(p(1000, -800)[0] + 1.45, p(0, -800)[1]), hoehe=0.42,
             farbe=ORANGE)
    s.formel(r"Z", mitte=(p(450, -900)[0] - 0.2, p(0, -900)[1]), hoehe=0.18, farbe=ROT)
    s.formel(r"|Z|=1879.6\,\Omega", mitte=(p(*zr)[0], p(*zr)[1] - 0.3), hoehe=0.2, farbe=ROT)
    s.weg(None, "%g + 0.55*cos(t)" % x0, "%g + 0.55*sin(t)" % y0, 0, -1.0098, farbe=SCHWARZ, dicke=3)
    s.formel(r"\varphi=-57.86^\circ", mitte=(x0 + 1.35, y0 - 0.32), hoehe=0.2)
    s.speichern()


SZENEN = (k2objekt, k2rest, k2rbinaer, k2rbyte, k2rnull, k2zahlenstrahl, k2bitfelder, k2rfloat, k2etikett, k2zeiger, k2rc)

for f in SZENEN:
    f()
