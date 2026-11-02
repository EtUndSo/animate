"""Abbildungen zu Höhere Mathematik 3, Teil 5: Integralsätze im Raum."""
import sys
from math import cos, sin, pi, sqrt, radians
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from szenen_lib import *  # noqa: E402,F403

AZ, EL = radians(-52), radians(24)
TUERKIS = "#1f9aa8"


def proj(x, y, z, S=0.72, o=(0.0, 0.0)):
    """Parallelprojektion: Blick schräg von oben, z zeigt nach oben."""
    rx, ry = cos(AZ), sin(AZ)
    ux, uy, uz = -sin(EL) * sin(AZ), sin(EL) * cos(AZ), cos(EL)
    return (o[0] + S * (x * rx + y * ry), o[1] + S * (x * ux + y * uy + z * uz))


def blick():
    """Einheitsvektor von der Fläche zum Betrachter."""
    return (cos(EL) * sin(AZ), -cos(EL) * cos(AZ), sin(EL))


def kuppel(r, ph):
    return (r * cos(ph), r * sin(ph), 4 - r * r)


def sichtbar(r, ph):
    n = (2 * r * r * cos(ph), 2 * r * r * sin(ph), r)
    b = blick()
    return n[0] * b[0] + n[1] * b[1] + n[2] * b[2] > 0


def laeufe(pkte):
    """[(punkt, sichtbar)] -> Stücke gleicher Sichtbarkeit."""
    out, cur, st = [], [], None
    for p, v in pkte:
        if st is None or v == st:
            cur.append(p)
        else:
            out.append((st, cur + [p]))
            cur = [p]
        st = v
    if cur:
        out.append((st, cur))
    return out


def kuppelgitter(s, a, S, o, farbe="#8fb4e3", dicke=2):
    for r in (0.5, 1.0, 1.5, 2.0):
        pk = [(proj(*kuppel(r, 2 * pi * i / 80), S, o), sichtbar(r, 2 * pi * i / 80)) for i in range(81)]
        for v, p in laeufe(pk):
            s.daten(a, p, farbe=farbe if v else "#d7dde6", dicke=dicke, dash="" if v else "6,5")
    for k in range(12):
        ph = 2 * pi * k / 12
        pk = [(proj(*kuppel(0.02 + 1.98 * i / 30, ph), S, o), sichtbar(0.02 + 1.98 * i / 30, ph)) for i in range(31)]
        for v, p in laeufe(pk):
            s.daten(a, p, farbe=farbe if v else "#d7dde6", dicke=dicke, dash="" if v else "6,5")


def k5flaeche():
    s = Szene("hm3/k5flaeche")
    a = s.welt()
    x0, y0, bx, by = -3.4, -1.05, 1.7, 2.1
    for i in range(5):
        s.linie(a, (x0 + bx * i / 4, y0), (x0 + bx * i / 4, y0 + by), farbe="#8fb4e3", dicke=2)
    for j in range(7):
        s.linie(a, (x0, y0 + by * j / 6), (x0 + bx, y0 + by * j / 6), farbe="#8fb4e3", dicke=2)
    s.linie(a, (x0, y0), (x0 + bx, y0), dicke=3)
    s.linie(a, (x0, y0), (x0, y0 + by), dicke=3)
    s.linie(a, (x0, y0 + by), (x0 + bx, y0 + by), dicke=3)
    s.linie(a, (x0 + bx, y0), (x0 + bx, y0 + by), dicke=3)
    r0, ph0 = 1.25, radians(178)
    ux = x0 + bx * r0 / 2
    vy = y0 + by * ((ph0 + 2 * pi) % (2 * pi)) / (2 * pi)
    s.linie(a, (x0, vy), (x0 + bx, vy), farbe=ROT, dicke=4)
    s.linie(a, (ux, y0), (ux, y0 + by), farbe=GRUEN, dicke=4)
    s.punkt(a, ux, vy, r=0.07)
    s.text(a, "B", (x0 + 0.1, y0 + by + 0.25), groesse=26)
    s.text(a, "r", (x0 + bx + 0.18, y0 - 0.05), groesse=26)
    s.text(a, "φ", (x0 - 0.18, y0 + by - 0.05), groesse=26, ausrichtung="center")
    s.text(a, "(u,v)", (ux + 0.1, vy + 0.2), groesse=22)
    s.pfeil((-1.45, 0.05), (-0.7, 0.05), "Φ", groesse=26, spitze=0.2)
    S, o = 0.68, (1.45, -1.45)
    kuppelgitter(s, a, S, o)
    pk = [(proj(*kuppel(2 * i / 40, ph0), S, o)) for i in range(41)]
    s.daten(a, pk, farbe=ROT, dicke=4)
    pk = [(proj(*kuppel(r0, 2 * pi * i / 80), S, o), sichtbar(r0, 2 * pi * i / 80)) for i in range(81)]
    for v, p in laeufe(pk):
        if v:
            s.daten(a, p, farbe=GRUEN, dicke=4)
    P = kuppel(r0, ph0)
    xr = (cos(ph0), sin(ph0), -2 * r0)
    xp = (-r0 * sin(ph0), r0 * cos(ph0), 0.0)
    n = (2 * r0 * r0 * cos(ph0), 2 * r0 * r0 * sin(ph0), r0)
    def spitze(v, f):
        return proj(P[0] + f * v[0], P[1] + f * v[1], P[2] + f * v[2], S, o)
    q = proj(*P, S, o)
    s.pfeil(q, spitze(xr, 0.42), "", farbe=ROT, dicke=3)
    s.pfeil(q, spitze(xp, 0.75), "", farbe=GRUEN, dicke=3)
    s.pfeil(q, spitze(n, 0.3), "", farbe=SCHWARZ, dicke=3)
    s.punkt(a, q[0], q[1], r=0.07)
    t = spitze(xr, 0.42)
    s.text(a, "x_u", (t[0] - 0.1, t[1] - 0.12), groesse=24, ausrichtung="right", farbe=ROT)
    t = spitze(xp, 0.75)
    s.text(a, "x_v", (t[0] + 0.14, t[1] - 0.03), groesse=24, farbe=GRUEN)
    t = spitze(n, 0.3)
    s.text(a, "x_u × x_v", (t[0] - 0.05, t[1] + 0.2), groesse=24, ausrichtung="center")
    s.speichern()


def k5element():
    s = Szene("hm3/k5element")
    a = s.welt()
    x0, y0, w, h = -3.2, -0.55, 1.2, 0.95
    pl = "%g,%g;%g,%g;%g,%g;%g,%g" % (x0, y0, x0 + w, y0, x0 + w, y0 + h, x0, y0 + h)
    s._add("Shape", {"points": pl, "closed": True, "label": "", "material": "custom", "font_size": 24, "color": SCHWARZ, "fill_color": BLAU, "fill_opacity": 0.2, "stroke_width": 3, "dash": ""}, a)
    s.text(a, "du", (x0 + w / 2, y0 - 0.28), ausrichtung="center", groesse=26, farbe=ROT)
    s.text(a, "dv", (x0 - 0.18, y0 + h / 2), ausrichtung="right", groesse=26, farbe=GRUEN)
    s.text(a, s.tr("param", "Parameterbereich", "parameter domain", "dominio de parámetros", "参数域"), (x0 + w / 2, y0 + h + 0.4), ausrichtung="center", groesse=24)
    s.pfeil((-1.55, -0.05), (-0.55, -0.05), "Φ", groesse=26, spitze=0.2)
    o = (0.0, -0.8)
    u = (2.05, 0.45)
    v = (0.75, 1.3)
    pl = "%g,%g;%g,%g;%g,%g;%g,%g" % (o[0], o[1], o[0] + u[0], o[1] + u[1], o[0] + u[0] + v[0], o[1] + u[1] + v[1], o[0] + v[0], o[1] + v[1])
    s._add("Shape", {"points": pl, "closed": True, "label": "", "material": "custom", "font_size": 24, "color": SCHWARZ, "fill_color": BLAU, "fill_opacity": 0.2, "stroke_width": 0, "dash": ""}, a)
    s.linie(a, (o[0] + u[0], o[1] + u[1]), (o[0] + u[0] + v[0], o[1] + u[1] + v[1]), dicke=2, farbe=GRAU)
    s.linie(a, (o[0] + v[0], o[1] + v[1]), (o[0] + u[0] + v[0], o[1] + u[1] + v[1]), dicke=2, farbe=GRAU)
    s.pfeil(o, (o[0] + u[0], o[1] + u[1]), "", farbe=ROT, dicke=4)
    s.pfeil(o, (o[0] + v[0], o[1] + v[1]), "", farbe=GRUEN, dicke=4)
    s.text(a, "x_u du", (o[0] + 1.25, o[1] + 0.12), groesse=26, farbe=ROT)
    s.text(a, "x_v dv", (o[0] + 0.3, o[1] + 0.82), groesse=26, ausrichtung="right", farbe=GRUEN)
    s.text(a, "dσ = |x_u × x_v| du dv", (o[0] + 1.42, o[1] + 2.15), groesse=26, ausrichtung="center", farbe=BLAU)
    s.speichern()


def zellen(s, a, x0, y0, m, n, c):
    for i in range(m):
        for j in range(n):
            x, y = x0 + i * c, y0 + j * c
            s._add("Shape", {"points": "%g,%g;%g,%g;%g,%g;%g,%g" % (x, y, x + c, y, x + c, y + c, x, y + c), "closed": True, "label": "", "material": "custom", "font_size": 24,
                             "color": HELLGRAU, "fill_color": BLAU, "fill_opacity": 0.08, "stroke_width": 2, "dash": ""}, a)


def k5zellen():
    s = Szene("hm3/k5zellen")
    a = s.welt()
    c, m, n = 0.82, 3, 3
    x0, y0 = -3.3, -1.25
    zellen(s, a, x0, y0, m, n, c)
    e = 0.16
    for i in range(m):
        for j in range(n):
            x, y = x0 + i * c, y0 + j * c
            k = [((x + e, y + e), (x + c - e, y + e)), ((x + c - e, y + e), (x + c - e, y + c - e)), ((x + c - e, y + c - e), (x + e, y + c - e)), ((x + e, y + c - e), (x + e, y + e))]
            aussen = [j == 0, i == m - 1, j == n - 1, i == 0]
            for (p, q), au in zip(k, aussen):
                s.pfeil(p, q, "", farbe=ROT if au else GRAU, dicke=3 if au else 2, spitze=0.13)
    s.text(a, s.tr("innen", "innen: gegenläufig", "inside: opposite", "dentro: opuestas", "内部：方向相反"), (x0 + 1.5 * c, y0 + 3 * c + 0.3), groesse=24, ausrichtung="center", farbe=GRAU)
    s.pfeil((-0.5, 0), (0.25, 0), "", spitze=0.2)
    x1, y1 = 0.75, -1.25
    zellen(s, a, x1, y1, m, n, c)
    w = m * c
    for p, q in (((x1, y1), (x1 + w, y1)), ((x1 + w, y1), (x1 + w, y1 + w)), ((x1 + w, y1 + w), (x1, y1 + w)), ((x1, y1 + w), (x1, y1))):
        s.pfeil(p, q, "", farbe=ROT, dicke=4, spitze=0.2)
    s.text(a, s.tr("rand", "nur der Rand bleibt", "only the boundary remains", "solo queda el borde", "只剩边界"), (x1 + w / 2, y1 + w + 0.3), groesse=24, ausrichtung="center", farbe=ROT)
    s.speichern()


def k5kuppel():
    s = Szene("hm3/k5kuppel")
    a = s.welt()
    S, o = 0.78, (0.0, -1.3)
    pk = [proj(2 * cos(2 * pi * i / 60), 2 * sin(2 * pi * i / 60), 0, S, o) for i in range(60)]
    s._add("Shape", {"points": ";".join("%.4f,%.4f" % p for p in pk), "closed": True, "label": "", "material": "custom", "font_size": 24, "color": BLAU, "fill_color": ORANGE, "fill_opacity": 0.22, "stroke_width": 0, "dash": ""}, a)
    kuppelgitter(s, a, S, o)
    rx, ry = cos(AZ), sin(AZ)
    ux, uy = -sin(EL) * sin(AZ), sin(EL) * cos(AZ)
    A, B = S * 2 * rx, S * 2 * ry
    C, D = S * 2 * ux, S * 2 * uy
    s.weg(a, "%.5f+(%.5f)*cos(t)+(%.5f)*sin(t)" % (o[0], A, B), "%.5f+(%.5f)*cos(t)+(%.5f)*sin(t)" % (o[1], C, D), 0, 6.28319, farbe=ROT, dicke=5, pfeile="0.08;0.6")
    t = proj(0, 0, 4, S, o)
    s.pfeil(t, (t[0], t[1] + 0.75), "", dicke=3)
    s.text(a, "n", (t[0] + 0.14, t[1] + 0.62), groesse=26)
    d = proj(0, 0, 0, S, o)
    s.pfeil(d, (d[0], d[1] + 0.6), "", farbe=ORANGE, dicke=3)
    s.text(a, "n", (d[0] + 0.14, d[1] + 0.42), groesse=26, farbe=ORANGE)
    s.text(a, s.tr("kup", "Kuppel K", "dome K", "cúpula K", "穹顶 K"), (1.45, 1.1), groesse=26, farbe=BLAU)
    s.text(a, s.tr("sch", "Bodenscheibe", "base disk", "disco base", "底面圆盘"), (1.85, -1.9), groesse=26, farbe=ORANGE)
    s.text(a, s.tr("ran", "gemeinsamer Rand", "common boundary", "borde común", "公共边界"), (-1.85, -1.95), groesse=26, ausrichtung="center", farbe=ROT)
    s.speichern()


def k5loecher():
    s = Szene("hm3/k5loecher")
    a = s.welt()
    c = (-1.95, 0.05)
    s.kreis(a, c[0], c[1], 1.25, farbe=BLAU, dicke=3, fuellung=BLAU, deckung=0.08)
    s.weg(a, "%g+1.25*cos(t)" % c[0], "%g+0.38*sin(t)" % c[1], 3.14159, 6.28319, farbe=BLAU, dicke=2)
    s.weg(a, "%g+1.25*cos(t)" % c[0], "%g+0.38*sin(t)" % c[1], 0, 3.14159, farbe=BLAU, dicke=2, dash="6,5")
    s.kreis(a, c[0], c[1], 0.08, farbe=ROT, dicke=3, fuellung="#ffffff", deckung=1.0)
    s.text(a, s.tr("pkt", "fehlt: ein Punkt", "missing: a point", "falta: un punto", "缺：一个点"), (c[0], 1.72), groesse=26, ausrichtung="center", farbe=ROT)
    s.text(a, s.tr("fl", "Kugelfläche: nicht", "sphere: cannot", "esfera: no se", "球面：不可"), (c[0], -1.55), groesse=24, ausrichtung="center")
    s.text(a, s.tr("fl2", "zusammenziehbar", "be shrunk", "puede contraer", "收缩"), (c[0], -1.9), groesse=24, ausrichtung="center")
    x = 1.95
    s.linie(a, (x, -1.25), (x, -0.02), farbe=ROT, dicke=4, dash="10,7")
    s.linie(a, (x, 0.32), (x, 1.35), farbe=ROT, dicke=4, dash="10,7")
    s.weg(a, "%g+1.05*cos(t)" % x, "0.05+0.32*sin(t)", 3.14159, 6.28319, farbe=BLAU, dicke=4, pfeile="0.55")
    s.weg(a, "%g+1.05*cos(t)" % x, "0.05+0.32*sin(t)", 0.26, 2.88, farbe=BLAU, dicke=4)
    s.text(a, s.tr("ach", "fehlt: die z-Achse", "missing: the z-axis", "falta: el eje z", "缺：z 轴"), (x, 1.72), groesse=26, ausrichtung="center", farbe=ROT)
    s.text(a, s.tr("ku", "Kreis um die Achse: nicht", "circle around the axis: cannot", "círculo alrededor: no se", "绕轴的圆：不可"), (x, -1.55), groesse=24, ausrichtung="center")
    s.text(a, "@fl2", (x, -1.9), groesse=24, ausrichtung="center")
    s.speichern()


def k5zellen3():
    s = Szene("hm3/k5zellen3")
    a = s.welt()
    c, m, n = 1.0, 3, 2
    x0, y0 = -1.5, -1.0
    zellen(s, a, x0, y0, m, n, c)
    d = 0.2
    for i in range(1, m):
        for j in range(n):
            x, y = x0 + i * c, y0 + (j + 0.5) * c
            s.pfeil((x - d, y + 0.1), (x + d, y + 0.1), "", farbe=GRAU, dicke=2, spitze=0.14)
            s.pfeil((x + d, y - 0.1), (x - d, y - 0.1), "", farbe=GRAU, dicke=2, spitze=0.14)
    for i in range(m):
        for j in range(1, n):
            x, y = x0 + (i + 0.5) * c, y0 + j * c
            s.pfeil((x - 0.1, y - d), (x - 0.1, y + d), "", farbe=GRAU, dicke=2, spitze=0.14)
            s.pfeil((x + 0.1, y + d), (x + 0.1, y - d), "", farbe=GRAU, dicke=2, spitze=0.14)
    for i in range(m):
        x = x0 + (i + 0.5) * c
        s.pfeil((x, y0 + n * c - 0.05), (x, y0 + n * c + 0.42), "", farbe=ROT, dicke=4, spitze=0.17)
        s.pfeil((x, y0 + 0.05), (x, y0 - 0.42), "", farbe=ROT, dicke=4, spitze=0.17)
    for j in range(n):
        y = y0 + (j + 0.5) * c
        s.pfeil((x0 + 0.05, y), (x0 - 0.42, y), "", farbe=ROT, dicke=4, spitze=0.17)
        s.pfeil((x0 + m * c - 0.05, y), (x0 + m * c + 0.42, y), "", farbe=ROT, dicke=4, spitze=0.17)
    s.text(a, s.tr("gi", "Innenwände:", "inner walls:", "paredes internas:", "内壁："), (2.15, 0.45), groesse=24, farbe=GRAU)
    s.text(a, s.tr("gi2", "heben sich auf", "cancel", "se cancelan", "相互抵消"), (2.15, 0.1), groesse=24, farbe=GRAU)
    s.text(a, s.tr("gi3", "Außenhaut: bleibt", "outer skin: remains", "piel exterior: queda", "外表面：保留"), (2.15, -0.55), groesse=24, farbe=ROT)
    s.speichern()


def k5epsilon():
    s = Szene("hm3/k5epsilon")
    a = s.welt()
    s._add("Shape", {"points": "-3,-1.75;3,-1.75;3,1.75;-3,1.75", "closed": True, "label": "", "material": "custom", "font_size": 24, "color": BLAU, "fill_color": BLAU, "fill_opacity": 0.13, "stroke_width": 0, "dash": ""}, a)
    s.kreis(a, 0, 0, 0.9, farbe=SCHWARZ, dicke=3, fuellung="#ffffff", deckung=1.0)
    s.punkt(a, 0, 0, r=0.06)
    s.text(a, "0", (0.12, -0.17), groesse=24)
    for k in range(8):
        w = pi / 8 + k * pi / 4
        s.pfeil((0.9 * cos(w), 0.9 * sin(w)), (0.45 * cos(w), 0.45 * sin(w)), "", farbe=ROT, dicke=3, spitze=0.15)
    for k in range(8):
        w = k * pi / 4
        s.pfeil((2.2 * cos(w) * 1.05, 1.5 * sin(w)), (1.25 * cos(w), 1.05 * sin(w)), "", farbe=GRUEN, dicke=2, spitze=0.14)
    s.text(a, "n", (0.48, 0.5), groesse=26, farbe=ROT, ausrichtung="center")
    s.text(a, "S_ε", (-0.56, 0.98), groesse=26)
    s.text(a, "∇φ", (2.35, 0.32), groesse=26, farbe=GRUEN)
    s.text(a, s.tr("au", "Außenraum", "exterior", "exterior", "外部区域"), (-2.8, 1.42), groesse=26, farbe=BLAU)
    s.speichern()


def feld(s, a, x0, fx, fy, titel, farbe):
    n = 5
    w = 1.75
    for i in range(n):
        for j in range(n):
            x, y = -1 + 2 * i / (n - 1), -1 + 2 * j / (n - 1)
            u, v = fx(x, y), fy(x, y)
            if abs(u) + abs(v) < 1e-9:
                continue
            px, py = x0 + x * w / 2, y * w / 2
            g = 0.105
            s.pfeil((px - g * u, py - g * v), (px + g * u, py + g * v), "", farbe=farbe, dicke=2, spitze=0.09)
    s.text(a, titel, (x0, 1.35), groesse=26, ausrichtung="center", farbe=farbe)


def k5helmholtz():
    s = Szene("hm3/k5helmholtz")
    a = s.welt()
    feld(s, a, -2.4, lambda x, y: x - y, lambda x, y: x + y, "F", SCHWARZ)
    s.text(a, "=", (-1.2, 0), groesse=34, ausrichtung="center")
    feld(s, a, 0.0, lambda x, y: x, lambda x, y: y, "∇u", ROT)
    s.text(a, "+", (1.2, 0), groesse=34, ausrichtung="center")
    feld(s, a, 2.4, lambda x, y: -y, lambda x, y: x, "rot A", BLAU)
    s.text(a, s.tr("q", "Quellen", "sources", "fuentes", "源"), (0.0, -1.35), groesse=24, ausrichtung="center", farbe=ROT)
    s.text(a, s.tr("w", "Wirbel", "vortices", "vórtices", "涡"), (2.4, -1.35), groesse=24, ausrichtung="center", farbe=BLAU)
    s.speichern()


def k5invarianz():
    s = Szene("hm3/k5invarianz")
    a = s.welt()
    rad = 1.3
    x1, x2 = -2.0, 2.0
    for mx, titel, farbe in ((x1, "(x, y)", BLAU), (x2, "(r, φ)", ROT)):
        s.kreis(a, mx, 0, rad, farbe=farbe, dicke=4)
        s.text(a, titel, (mx, 1.6), groesse=26, ausrichtung="center", farbe=farbe)
    for k in range(-3, 4):
        c = k * rad / 4
        h = sqrt(rad ** 2 - c ** 2)
        s.linie(a, (x1 + c, -h), (x1 + c, h), farbe=BLAU, dicke=2)
        s.linie(a, (x1 - h, c), (x1 + h, c), farbe=BLAU, dicke=2)
    for k in range(1, 4):
        s.kreis(a, x2, 0, k * rad / 4, farbe=ROT, dicke=2)
    for k in range(12):
        w = radians(30 * k)
        s.linie(a, (x2, 0), (x2 + rad * cos(w), rad * sin(w)), farbe=ROT, dicke=2)
    s.speichern()


for f in (k5flaeche, k5element, k5zellen, k5kuppel, k5loecher, k5zellen3, k5epsilon, k5helmholtz, k5invarianz):
    f()
