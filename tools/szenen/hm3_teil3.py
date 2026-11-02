"""Abbildungen zu Höhere Mathematik 3, Teil 3: Kurvenintegrale."""
import sys
from math import cos, sin, pi, sqrt, radians
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from szenen_lib import *  # noqa: E402,F403

AZ, EL = radians(-52), radians(24)
BLASS = "#d8e6f6"


def proj(x, y, z, S=1.0, o=(0.0, 0.0)):
    """Parallelprojektion: Blick schräg von oben, z zeigt nach oben."""
    rx, ry = cos(AZ), sin(AZ)
    ux, uy, uz = -sin(EL) * sin(AZ), sin(EL) * cos(AZ), cos(EL)
    return (o[0] + S * (x * rx + y * ry), o[1] + S * (x * ux + y * uy + z * uz))


def vieleck(s, a, pkte, farbe=BLAU, deckung=0.15, rand=None, dicke=0):
    s._add("Shape", {"points": ";".join("%.4f,%.4f" % p for p in pkte), "closed": True, "label": "", "material": "custom", "font_size": 24,
                     "color": rand or farbe, "fill_color": farbe, "fill_opacity": deckung, "stroke_width": dicke, "dash": ""}, a)


def k3kurven():
    s = Szene("hm3/k3kurven")
    a = s.welt()
    xs = (-2.75, -0.9, 0.95, 2.8)
    r = 0.7
    ty, py, zy = 1.12, -0.98, -1.36
    # Kreis
    c = xs[0]
    s.weg(a, f"{c}+{r}*cos(t)", f"{r}*sin(t)", 0, 2 * pi, farbe=BLAU, dicke=4, pfeile="0.2")
    s.punkt(a, c + r, 0, r=0.07)
    s.text(a, s.tr("kr", "Kreis", "circle", "círculo", "圆"), (c, ty), ausrichtung="center", groesse=24)
    s.text(a, "t = 0, 2π", (c, py), ausrichtung="center", groesse=22)
    s.text(a, s.tr("ei", "einfach", "simple", "simple", "简单"), (c, zy), ausrichtung="center", groesse=24, farbe=GRUEN)
    # Kreis zweimal
    c = xs[1]
    s.weg(a, f"{c}+{r}*cos(t)", f"{r}*sin(t)", 0, 2 * pi, farbe=BLAU, dicke=4, pfeile="0.2;0.7")
    s.punkt(a, c + r, 0, farbe=ROT, r=0.09)
    s.text(a, s.tr("kz", "Kreis, zweimal", "circle, twice", "círculo, dos veces", "圆，两圈"), (c, ty), ausrichtung="center", groesse=24)
    s.text(a, "t = 0, 2π, 4π", (c, py), ausrichtung="center", groesse=22, farbe=ROT)
    s.text(a, s.tr("ne", "nicht einfach", "not simple", "no simple", "不简单"), (c, zy), ausrichtung="center", groesse=24, farbe=ROT)
    # Acht
    c = xs[2]
    s.weg(a, f"{c}+0.72*sin(t)", "0.72*sin(2*t)", 0, 2 * pi, farbe=BLAU, dicke=4, pfeile="0.1;0.62", n=241)
    s.punkt(a, c, 0, farbe=ROT, r=0.09)
    s.text(a, s.tr("ac", "Acht", "figure eight", "ocho", "八字形"), (c, ty), ausrichtung="center", groesse=24)
    s.text(a, "t = 0, π, 2π", (c, py), ausrichtung="center", groesse=22, farbe=ROT)
    s.text(a, "@ne", (c, zy), ausrichtung="center", groesse=24, farbe=ROT)
    # Spitze
    c = xs[3]
    s.weg(a, f"{c}-0.35+0.9*t*t", "0.75*t*t*t", -1, 1, farbe=BLAU, dicke=4, pfeile="0.1;0.9")
    s.punkt(a, c - 0.35, 0, farbe=ROT, r=0.09)
    s.text(a, s.tr("sp", "Spitze", "cusp", "cúspide", "尖点"), (c, ty), ausrichtung="center", groesse=24)
    s.text(a, s.tr("st", "steht still", "stops", "se detiene", "停住"), (c, py), ausrichtung="center", groesse=22, farbe=ROT)
    s.text(a, s.tr("nr", "nicht regulär", "not regular", "no regular", "非正则"), (c, zy), ausrichtung="center", groesse=24, farbe=ROT)
    s.speichern()


def k3integral():
    s = Szene("hm3/k3integral")
    a = s.welt()

    def f(x):
        return 0.42 * sin(0.8 * x)

    def df(x):
        return 0.42 * 0.8 * cos(0.8 * x)

    s.weg(a, "t", "0.42*sin(0.8*t)", -3.45, 3.45, farbe=SCHWARZ, dicke=3, pfeile="0.98")
    fall = ((-2.8, 0, s.tr("v", "parallel: voll", "parallel: full", "paralelo: completo", "平行：全计")),
            (-1.0, 58, s.tr("sc", "schräg: Anteil", "oblique: part", "oblicuo: parte", "斜向：部分")),
            (0.8, 90, s.tr("q", "quer: null", "across: zero", "transversal: cero", "垂直：零")),
            (2.35, 180, s.tr("e", "entgegen: negativ", "against: negative", "opuesto: negativo", "反向：负")))
    for x, w, wort in fall:
        n = sqrt(1 + df(x) ** 2)
        e = (1 / n, df(x) / n)
        no = (-e[1], e[0])
        p = (x, f(x))
        L = 1.05
        d = (e[0] * cos(radians(w)) + no[0] * sin(radians(w)), e[1] * cos(radians(w)) + no[1] * sin(radians(w)))
        s.pfeil(p, (p[0] + 0.62 * e[0], p[1] + 0.62 * e[1]), "", farbe=GRUEN, dicke=5, spitze=0.17)
        v = 0.09 if w == 0 else 0.0
        q = (p[0] + v * no[0], p[1] + v * no[1])
        z = (q[0] + L * d[0], q[1] + L * d[1])
        s.pfeil(q, z, "", farbe=BLAU, dicke=3, spitze=0.17)
        if w == 58:
            fu = L * cos(radians(w))
            t = (p[0] + fu * e[0], p[1] + fu * e[1])
            s.linie(a, z, t, farbe=GRAU, dicke=2, dash=DASH)
            s.pfeil((p[0] - 0.09 * no[0], p[1] - 0.09 * no[1]), (t[0] - 0.09 * no[0], t[1] - 0.09 * no[1]), "", farbe=ROT, dicke=4, spitze=0.14)
            s.text(a, "ϑ", (p[0] + 0.3, p[1] + 0.3), groesse=24)
        s.text(a, wort, (x, -1.25), ausrichtung="center", groesse=22)
        s.punkt(a, p[0], p[1], r=0.06)
    s.text(a, "F", (-2.2, -0.12), groesse=26, farbe=BLAU)
    s.text(a, "Δx", (-2.7, -0.76), groesse=26, farbe=GRUEN)
    s.speichern()


def k3invarianz():
    s = Szene("hm3/k3invarianz")
    a = s.welt()
    rad, oy = 1.6, -1.05
    panels = ((-3.4, [pi / 2 * k / 8 for k in range(9)], "γ(t)", s.tr("gl", "gleichmäßig", "evenly spaced", "uniforme", "均匀"), BLAU, False),
              (-0.95, [pi / 2 * (k / 8) ** 2 for k in range(9)], "γ∘τ(u)", s.tr("sc", "erst langsam, dann schnell", "slow, then fast", "lento, luego rápido", "先慢后快"), ROT, False),
              (1.6, [pi / 2 * k / 8 for k in range(9)], s.tr("rw", "rückwärts", "backwards", "hacia atrás", "反向"), s.tr("sv", "Vorzeichen kippt", "sign flips", "cambia el signo", "符号翻转"), GRUEN, True))
    for ox, punkte, titel, wort, farbe, zurueck in panels:
        if zurueck:
            s.weg(a, f"{ox}+{rad}*cos({pi / 2}-t)", f"{oy}+{rad}*sin({pi / 2}-t)", 0, pi / 2, farbe=farbe, dicke=4, pfeile="0.6")
        else:
            s.weg(a, f"{ox}+{rad}*cos(t)", f"{oy}+{rad}*sin(t)", 0, pi / 2, farbe=farbe, dicke=4, pfeile="0.6")
        for w in punkte:
            s.punkt(a, ox + rad * cos(w), oy + rad * sin(w), farbe=farbe, r=0.07)
        s.text(a, titel, (ox + 0.8, 0.95), groesse=26, ausrichtung="center", farbe=farbe)
        s.text(a, wort, (ox + 0.8, -1.42), groesse=22, ausrichtung="center", farbe=farbe)
    s.speichern()


def k3wege():
    s = Szene("hm3/k3wege")
    a = s.welt()
    S, y0 = 2.15, -1.2

    def panel(x0, fx, fy, g, titel, w1, w2):
        def m(x, y):
            return (x0 + S * x, y0 + S * y)
        for i in range(6):
            for j in range(6):
                x, y = 0.08 + 0.2 * i, 0.08 + 0.2 * j
                u, v = fx(x, y), fy(x, y)
                p = m(x, y)
                s.pfeil((p[0] - g * u, p[1] - g * v), (p[0] + g * u, p[1] + g * v), "", farbe=HELLGRAU, dicke=2, spitze=0.08)
        s.weg(a, f"{x0}+{S}*cos(t)", f"{y0}+{S}*sin(t)", 0, pi / 2, farbe=BLAU, dicke=4, pfeile="0.55")
        s.weg(a, f"{x0}+{S}*(1-t)", f"{y0}+{S}*t", 0, 1, farbe=ROT, dicke=4, pfeile="0.55")
        A, B = m(1, 0), m(0, 1)
        s.punkt(a, A[0], A[1], r=0.08)
        s.punkt(a, B[0], B[1], r=0.08)
        s.text(a, "A", (A[0] + 0.1, A[1] - 0.3), groesse=26)
        s.text(a, "B", (B[0] - 0.32, B[1] + 0.05), groesse=26)
        s.text(a, titel, (x0 + 1.2, 1.42), groesse=26, ausrichtung="center")
        s.text(a, w1, (x0 + 1.2, -1.6), groesse=24, ausrichtung="center", farbe=BLAU)
        s.text(a, w2, (x0 + 1.2, -1.95), groesse=24, ausrichtung="center", farbe=ROT)

    panel(-3.4, lambda x, y: -y, lambda x, y: x, 0.09, "V = (−y, x)",
          s.tr("a1", "Viertelkreis: π/2", "quarter circle: π/2", "cuarto de círculo: π/2", "四分之一圆：π/2"),
          s.tr("a2", "Strecke: 1", "segment: 1", "segmento: 1", "线段：1"))
    panel(0.65, lambda x, y: 2 * x, lambda x, y: 2 * y, 0.05, "G = ∇(x² + y²)",
          s.tr("b1", "Viertelkreis: 0", "quarter circle: 0", "cuarto de círculo: 0", "四分之一圆：0"),
          s.tr("b2", "Strecke: 0", "segment: 0", "segmento: 0", "线段：0"))
    s.speichern()


def k3stern():
    s = Szene("hm3/k3stern")
    a = s.welt()
    c = (-2.05, -0.05)
    pk = []
    for k in range(10):
        w = pi / 2 + k * pi / 5
        r = 1.32 if k % 2 == 0 else 0.6
        pk.append((c[0] + r * cos(w), c[1] + r * sin(w)))
    vieleck(s, a, pk, BLAU, 0.16, BLAU, 3)
    for k in range(0, 10, 2):
        s.linie(a, c, pk[k], farbe=BLAU, dicke=3)
    for k in range(1, 10, 2):
        s.linie(a, c, pk[k], farbe=BLAU, dicke=2, dash=DASH)
    s.punkt(a, c[0], c[1], r=0.08)
    s.text(a, "x₀", (c[0] + 0.26, c[1] - 0.28), groesse=24)
    s.text(a, s.tr("st", "Sterngebiet", "star domain", "dominio estrellado", "星形区域"), (c[0], 1.55), groesse=26, ausrichtung="center", farbe=BLAU)
    s.text(a, s.tr("st2", "jede Strecke bleibt im Gebiet", "each segment stays inside", "cada segmento queda dentro", "线段都在区域内"), (c[0], -1.55), groesse=22, ausrichtung="center", farbe=BLAU)
    k = (1.95, -0.05)
    s.kreis(a, k[0], k[1], 1.28, farbe=BLAU, dicke=3, fuellung=BLAU, deckung=0.16)
    s.kreis(a, k[0], k[1], 0.52, farbe=BLAU, dicke=3, fuellung="#ffffff", deckung=1.0)
    p, q = (k[0] - 0.9, k[1]), (k[0] + 0.9, k[1])
    s.linie(a, p, (k[0] - 0.52, k[1]), farbe=ROT, dicke=3)
    s.linie(a, (k[0] - 0.52, k[1]), (k[0] + 0.52, k[1]), farbe=ROT, dicke=3, dash=DASH)
    s.linie(a, (k[0] + 0.52, k[1]), q, farbe=ROT, dicke=3)
    s.punkt(a, p[0], p[1], r=0.08)
    s.punkt(a, q[0], q[1], r=0.08)
    s.text(a, "x₀", (p[0] - 0.08, p[1] - 0.32), groesse=24)
    s.text(a, "x", (q[0] - 0.02, q[1] - 0.32), groesse=24)
    s.text(a, s.tr("ke", "kein Sterngebiet", "no star domain", "no estrellado", "非星形区域"), (k[0], 1.55), groesse=26, ausrichtung="center", farbe=ROT)
    s.text(a, s.tr("ke2", "die Strecke trifft das Loch", "the segment hits the hole", "el segmento cruza el agujero", "线段穿过孔"), (k[0], -1.55), groesse=22, ausrichtung="center", farbe=ROT)
    s.speichern()


def k3achsen():
    s = Szene("hm3/k3achsen")
    a = s.welt()
    o = (-2.0, -1.0)

    def q(p):
        return (o[0] + p[0] + 0.55 * p[1], o[1] + 0.4 * p[1] + p[2])

    P0, P1, P2, P3 = (0, 0, 0), (2.3, 0, 0), (2.3, 1.7, 0), (2.3, 1.7, 1.25)
    for e, nm in (((3.7, 0, 0), "x"), ((0, 2.1, 0), "y"), ((0, 0, 1.9), "z")):
        z = q(e)
        s.pfeil(q((0, 0, 0)), z, "", farbe=GRAU, dicke=2, spitze=0.15)
        s.text(a, nm, (z[0] - 0.02 if nm == "y" else z[0] + 0.1, z[1] + 0.16 if nm == "y" else z[1] + 0.02), groesse=24, farbe=GRAU)
    s.linie(a, q(P0), q(P3), farbe=GRAU, dicke=3, dash=DASH)
    s.pfeil(q(P0), q(P1), "", farbe=BLAU, dicke=5, spitze=0.2)
    s.pfeil(q(P1), q(P2), "", farbe=ROT, dicke=5, spitze=0.2)
    s.pfeil(q(P2), q(P3), "", farbe=GRUEN, dicke=5, spitze=0.2)
    for p in (P0, P3):
        z = q(p)
        s.punkt(a, z[0], z[1], r=0.08)
    z = q(P0)
    s.text(a, "(x₀, y₀, z₀)", (z[0] - 0.14, z[1] - 0.14), groesse=24, ausrichtung="right")
    z = q(P3)
    s.text(a, "(x, y, z)", (z[0] + 0.14, z[1] + 0.04), groesse=24)
    m = q((1.15, 0, 0))
    s.text(a, "F₁(t, y₀, z₀)", (m[0], m[1] - 0.36), groesse=24, ausrichtung="center", farbe=BLAU)
    m = q((2.3, 0.85, 0))
    s.text(a, "F₂(x, t, z₀)", (m[0] + 0.26, m[1] - 0.04), groesse=24, farbe=ROT)
    m = q((2.3, 1.7, 0.6))
    s.text(a, "F₃(x, y, t)", (m[0] + 0.16, m[1] - 0.05), groesse=24, farbe=GRUEN)
    s.speichern()


def k3homotopie():
    s = Szene("hm3/k3homotopie")
    a = s.welt()
    # links: feste Endpunkte
    x0, w = -3.3, 2.8
    y0 = -0.75
    vieleck(s, a, [(x0 - 0.2, y0 - 0.75), (x0 + w + 0.2, y0 - 0.75), (x0 + w + 0.2, 1.3), (x0 - 0.2, 1.3)], BLAU, 0.09)
    for k, hb in enumerate((1.75, 1.15, 0.55, -0.05, -0.65)):
        farbe = BLAU if k == 0 else ROT if k == 4 else HELLGRAU
        d = 4 if k in (0, 4) else 3
        s.weg(a, f"{x0}+{w}*t", f"{y0}+({hb})*sin(3.14159*t)+0.1*sin(6.28318*t)", 0, 1, farbe=farbe, dicke=d, pfeile="0.55" if k in (0, 4) else "")
    s.punkt(a, x0, y0, r=0.08)
    s.punkt(a, x0 + w, y0, r=0.08)
    s.text(a, "γ₀", (x0 + 0.22, 0.48), groesse=24, farbe=BLAU)
    s.text(a, "γ₁", (x0 + 0.28, -1.2), groesse=24, farbe=ROT)
    s.text(a, s.tr("fe", "feste Endpunkte", "fixed endpoints", "extremos fijos", "端点固定"), (x0 + w / 2, 1.55), groesse=24, ausrichtung="center")
    # rechts: Ebene ohne Nullpunkt
    x1 = 0.25
    vieleck(s, a, [(x1, -1.5), (x1 + 3.2, -1.5), (x1 + 3.2, 1.3), (x1, 1.3)], BLAU, 0.09)
    c = (x1 + 2.15, 0.0)
    s.kreis(a, c[0], c[1], 0.1, farbe=ROT, dicke=3, fuellung="#ffffff", deckung=1.0)
    s.weg(a, f"{c[0]}+0.82*cos(t)", f"{c[1]}+0.82*sin(t)", 0, 2 * pi, farbe=ROT, dicke=4, pfeile="0.1")
    for r, far in ((0.52, GRUEN), (0.32, "#6fb38e"), (0.14, "#9dcdb2")):
        s.kreis(a, x1 + 0.72, 0.15, r, farbe=far, dicke=3 if r > 0.5 else 2)
    s.punkt(a, x1 + 0.72, 0.15, farbe=GRUEN, r=0.05)
    s.text(a, s.tr("zu", "zusammenziehbar", "contractible", "contráctil", "可收缩"), (x1 + 0.08, -0.72), groesse=22, farbe=GRUEN)
    s.text(a, s.tr("ha", "bleibt am Loch hängen", "caught on the hole", "se engancha en el agujero", "被孔卡住"), (x1 + 1.6, -1.25), groesse=22, ausrichtung="center", farbe=ROT)
    s.text(a, s.tr("oh", "Ebene ohne Nullpunkt", "plane without the origin", "plano sin el origen", "去掉原点的平面"), (x1 + 1.6, 1.55), groesse=24, ausrichtung="center")
    s.speichern()


def k3rand():
    s = Szene("hm3/k3rand")
    a = s.welt()
    ox, c, d = -1.8, -1.0, 1.0
    al = "(-1.05-0.28*cos(1.5*t))"
    be = "(1.0+0.25*t*t+0.12*t)"

    def alf(y):
        return -1.05 - 0.28 * cos(1.5 * y)

    def bet(y):
        return 1.0 + 0.25 * y * y + 0.12 * y

    n = 40
    ys = [c + (d - c) * i / n for i in range(n + 1)]
    pk = [(ox + bet(y), y) for y in ys] + [(ox + alf(y), y) for y in reversed(ys)]
    vieleck(s, a, pk, BLAU, 0.14)
    s.weg(a, f"{ox}+{be}", "t", c, d, farbe=ROT, dicke=4, pfeile="0.55")
    s.weg(a, f"{ox}+({bet(d):.4f})-({bet(d) - alf(d):.4f})*t", f"{d}", 0, 1, farbe=GRUEN, dicke=4, pfeile="0.55")
    s.weg(a, f"{ox}+(-1.05-0.28*cos(1.5*({d}-{d - c}*t)))", f"{d}-{d - c}*t", 0, 1, farbe=ORANGE, dicke=4, pfeile="0.55")
    s.weg(a, f"{ox}+({alf(c):.4f})+({bet(c) - alf(c):.4f})*t", f"{c}", 0, 1, farbe=BLAU, dicke=4, pfeile="0.55")
    s.text(a, "Γ₁", (ox + bet(0) + 0.14, 0.0), groesse=24, farbe=ROT)
    s.text(a, "Γ₂", (ox - 0.1, d + 0.14), groesse=24, ausrichtung="center", farbe=GRUEN)
    s.text(a, "Γ₃", (ox + alf(0) - 0.14, 0.0), groesse=24, ausrichtung="right", farbe=ORANGE)
    s.text(a, "Γ₄", (ox - 0.1, c - 0.34), groesse=24, ausrichtung="center", farbe=BLAU)
    s.text(a, "D", (ox - 0.15, -0.1), groesse=28)
    k = (1.75, 0.0)
    ra, ri = 1.25, 0.56
    s.kreis(a, k[0], k[1], ra, farbe=BLAU, dicke=0, fuellung=BLAU, deckung=0.14)
    s.kreis(a, k[0], k[1], ri, farbe=BLAU, dicke=0, fuellung="#ffffff", deckung=1.0)
    s.weg(a, f"{k[0]}+{ra}*cos(t)", f"{k[1]}+{ra}*sin(t)", 0, 2 * pi, farbe=ROT, dicke=4, pfeile="0.08;0.33;0.58;0.83")
    s.weg(a, f"{k[0]}+{ri}*cos(t)", f"{k[1]}-{ri}*sin(t)", 0, 2 * pi, farbe=ROT, dicke=4, pfeile="0.12;0.62")
    w = radians(38)
    p = (k[0] + ra * cos(w), k[1] + ra * sin(w))
    s.pfeil(p, (p[0] + 0.62 * cos(w), p[1] + 0.62 * sin(w)), "", farbe=GRUEN, dicke=4, spitze=0.16)
    s.pfeil(p, (p[0] - 0.62 * sin(w), p[1] + 0.62 * cos(w)), "", farbe=SCHWARZ, dicke=4, spitze=0.16)
    s.text(a, "ν", (p[0] + 0.62 * cos(w) + 0.08, p[1] + 0.62 * sin(w) + 0.04), groesse=26, farbe=GRUEN)
    s.text(a, "t", (p[0] - 0.62 * sin(w) - 0.22, p[1] + 0.62 * cos(w) + 0.04), groesse=26)
    s.speichern()


for f in (k3kurven, k3integral, k3invarianz, k3wege, k3stern, k3achsen, k3homotopie, k3rand):
    f()
