"""Linux und Kommandozeile, Kapitel 3 „Dateien, Verzeichnisse und Pfade“ (C:\\Bücher\\EtUndSo\\Linux\\Arbeitshefte\\Kap3_Dateien.tex,
kap3_stufen.tex, kap3_stufen_b.tex): Abbildungen, alle animiert (notizen/animationen.md §5).

Szenenname linux/k3<name> = \\label{fig:k3<name>} im Heft (\\szenenabb{k3<name>}{…}{fig:k3<name>}). Stil wie
tools/szenen/linux_teil2.py: Kästen, Pfeile, T(...) in sechs Sprachen; Terminal-Inhalte (Befehle, Ausgaben, Pfade) sind in allen
Sprachen gleich und stehen als Schreibmaschinenschrift in s.formel (\\texttt) mit unsichtbarer Stütze (gleiche Zeilenhöhe, Zeichen in
Spalten zu 0,525 em). Zeilen mit mehreren Leerzeichen hintereinander setzt ttz() stückweise an ihre Spalten. Normale Beschriftungen,
Baumknoten und Dateiinhalte mit Umlauten stehen in s.text (klein; ein $ verschwindet dort, deshalb nur in tt).
Die Koordinaten bleiben zwischen x = -3,45 und 3,45: jedes Bild höchstens 548 px breit.
Hälfte 1 (Abschnitte 1–5, 20 Szenen) baut Phase 2b-1, Hälfte 2 (Abschnitte 6–10) hängt Phase 2b-2 hinten an SZENEN an.
Bauen:  python tools/szenen/linux_teil3.py
Export: python tools/export_szenen.py <alle Namen aus SZENEN> --animiert
Rechenbild in Hälfte 1: k3einkauf (s.formel zeilenweise; Zahlen in rechnung_kap3.py); in Hälfte 2: k3du.
Zeichenreihenfolge: Ein Objekt, das per Animation erscheint, liegt über allem, was vorher erschienen ist (auch innerhalb eines
Schritts zählt die Reihenfolge der Animationen), nicht in der Reihenfolge des Anlegens. Kästen also vor ihrem Inhalt einblenden.
Seit 10.11.2026 stehen die Helfer in linux_hilfen.py (Bilder unverändert). Für neue Kapitel: s.text(..., schrift="tt") bzw.
schreibmaschine("text") statt der Formel-Stütze, Szene(..., reihenfolge="anlegen"), s.ersetzen (notizen/animationen.md).
"""
import math
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from szenen_lib import *  # noqa: E402,F403

from linux_hilfen import *  # noqa: E402,F403  (gemeinsame Helfer der Linux-Kapitel, seit 10.11.2026)

dokument = dokument_zeilen        # in diesem Kapitel: Rechteck mit linksbündigen Textzeilen


# ================================================================== Abschnitt 1: Dateien, Verzeichnisse, Baum
def k3bytes():
    """/etc/hostname als Streifen aus sechs Bytes 108 97 98 111 114 10 mit Zeichen; Namensschild daneben, nicht Teil der Bytes."""
    s = Szene("linux/k3bytes")
    werte = (108, 97, 98, 111, 114, 10)
    b, h, xl, y = 0.62, 0.52, -1.0, 0.3
    xs = [xl + (i + 0.5) * b for i in range(6)]
    xr = xl + 6 * b
    kaest = [s.box("", (x, y), breite=b, hoehe=h, form="rect", farbe=SCHWARZ, fuellung=WEISS, dicke=2.5) for x in xs]
    zahlen = [text(s, str(v), (x, y), FS, "center", ORANGE if v == 10 else SCHWARZ) for v, x in zip(werte, xs)]
    unten = [tt(s, z, x, y - 0.52, 0.26, BLAU, "m") for z, x in zip("labor", xs)]
    unten.append(text(s, T(s, "zende", "Zeilen-\nende", "line\nend", "fin de\nlínea", "换行符", "fin de\nligne", "satır\nsonu"),
                      (xs[5], y - 0.58), FM, "center", ORANGE))
    kl = klammer(s, xl + 0.02, xr - 0.02, y + h / 2 + 0.12, unten=False)
    l_inh = text(s, T(s, "inhalt", "Inhalt: 6 Bytes", "contents: 6 bytes", "contenido: 6 bytes", "内容：6 个字节",
                      "contenu : 6 octets", "içerik: 6 bayt"), ((xl + xr) / 2, y + h / 2 + 0.34), FK)
    tx = -2.45
    schild = s.box("", (tx, y), breite=1.6, hoehe=0.46, form="round", farbe=GRAU, fuellung=ORANGE_HELL, dicke=2.5)
    loch = s.kreis(None, tx + 0.66, y, 0.05, farbe=GRAU, dicke=2, fuellung=WEISS, deckung=1.0)
    name = tt(s, "/etc/hostname", tx - 0.06, y, 0.17, SCHWARZ, "m")
    faden = linie(s, (tx + 0.71, y), (xl, y), GRAU, 2, DOT)
    l_name = text(s, T(s, "schild", "Namensschild", "name tag", "etiqueta con el nombre", "名称标签", "étiquette du nom",
                       "ad etiketi"), (tx, y + 0.45), FK)
    l_nicht = text(s, T(s, "nicht", "gehört nicht\nzu den Bytes", "not part\nof the bytes", "no forma parte\nde los bytes",
                        "不属于\n这些字节", "ne fait pas partie\ndes octets", "baytlara\ndahil değil"), (tx, y - 0.58), FM,
                   "center", GRAU)
    schritt(s, WACHS(kaest, 0.6))
    s.pause(0.6)
    for i in range(6):
        schritt(s, EIN([zahlen[i], unten[i]], 0.45))
    s.pause(0.6)
    schritt(s, ZEICHNE(kl, 0.6), EIN(l_inh, 0.6))
    s.pause(0.6)
    schritt(s, WACHS(schild, 0.6), EIN([loch, name, l_name], 0.6))
    schritt(s, ZEICHNE(faden, 0.5))
    schritt(s, EIN(l_nicht, 0.6), BETONE(name, 0.8))
    s.speichern()


def k3verzeichnis():
    """/usr als Liste Name → Verweis, Zeile für Zeile; bin öffnet die Liste /usr/bin mit der Datei bash."""
    s = Szene("linux/k3verzeichnis")
    dz = 0.245

    def liste(L, titel, namen, symbol):
        y0 = 1.0
        yu = y0 - (len(namen) - 1) * dz - 0.16
        rahmen_ = s.box("", (L + 1.325, (1.46 + yu) / 2), breite=2.65, hoehe=1.46 - yu, form="rect", farbe=GRAU,
                        fuellung=WEISS, dicke=2)
        kopf = [tt(s, titel, L + 1.325, 1.66, 0.24, SCHWARZ, "m"),
                text(s, T(s, "kname", "Name", "name", "nombre", "名称", "nom", "ad"), (L + 0.18, 1.28), FM, "left", GRAU),
                text(s, T(s, "kverweis", "Verweis", "reference", "referencia", "指向", "référence", "başvuru"),
                     (L + 1.8, 1.28), FM, "center", GRAU),
                linie(s, (L, 1.15), (L + 2.65, 1.15), GRAU, 2)]
        zeilen = []
        for i, n in enumerate(namen):
            y = y0 - i * dz
            z = [text(s, n, (L + 0.18, y), FK, "left")]
            if n != "…":
                z += [pf(s, (L + 1.3, y), (L + 1.8, y), farbe=GRAU, dicke=2, spitze=0.08), symbol(s, L + 2.05, y)]
            zeilen.append(z)
        return [rahmen_] + kopf, zeilen

    links, zl = liste(-3.4, "/usr", ["bin", "games", "include", "lib", "lib64", "libexec", "local", "sbin", "share", "src"],
                      ordner_symbol)
    rechts, zr = liste(0.6, "/usr/bin", ["…", "bash", "cat", "…", "ls", "…"], datei_symbol)
    m_bin = mark(s, -3.35, -0.8, 1.0, 0.22, ORANGE, 0.25)
    verb = pf(s, (-1.17, 1.0), (0.55, 1.0), farbe=ORANGE, dicke=3)
    leg = [ordner_symbol(s, 0.75, -0.62),
           text(s, T(s, "verz", "Verzeichnis", "directory", "directorio", "目录", "répertoire", "dizin"), (0.95, -0.62), FM,
                "left"),
           datei_symbol(s, 0.75, -0.9),
           text(s, T(s, "datei", "Datei", "file", "archivo", "文件", "fichier", "dosya"), (0.95, -0.9), FM, "left")]
    schritt(s, EIN(links, 0.6))
    for z in zl:
        schritt(s, EIN(z, 0.25))
    s.pause(0.6)
    schritt(s, EIN(m_bin, 0.6), BETONE(zl[0][0], 0.8))
    schritt(s, ZEICHNE(verb, 0.7))
    schritt(s, EIN(rechts, 0.6))
    schritt(s, EIN(zr, 0.6))
    s.pause(0.4)
    schritt(s, BETONE(zr[1][0], 0.8), EIN(leg, 0.8))
    s.speichern()


def k3baum():
    """Baum Ebene für Ebene; zum Schluss /usr mit Pfeil zum übergeordneten Verzeichnis und drei Pfeilen zu Unterverzeichnissen."""
    s = Szene("linux/k3baum")
    K, E, P = baum(s, ["/", "etc", "home", "tmp", "usr", "student", "bin", "lib", "share"])
    l_w = text(s, T(s, "wurzel", "Wurzelverzeichnis", "root directory", "directorio raíz", "根目录", "répertoire racine",
                    "kök dizin"), (-0.36, 1.5), FM, "right", BLAU)
    m = rahmen(s, P["usr"], 0.8, 0.46)
    hoch = pf(s, (1.79, 1.05), (0.33, 1.43), farbe=ORANGE, dicke=3.5)
    l_hoch = text(s, T(s, "uebergeordnet", "übergeordnetes\nVerzeichnis", "parent\ndirectory", "directorio\npadre", "上级目录",
                       "répertoire\nparent", "üst\ndizin"), (1.3, 1.52), FM, "left", ORANGE)
    pu = P["usr"]
    runter = [pf(s, (pu[0], pu[1] - KH / 2), (P[n][0], P[n][1] + KH / 2), farbe=GRUEN, dicke=3.5) for n in ("bin", "lib", "share")]
    l_unter = text(s, T(s, "unterverz", "Unterverzeichnisse", "subdirectories", "subdirectorios", "子目录", "sous-répertoires",
                        "alt dizinler"), (1.9, -0.47), FM, "center", GRUEN)
    baum_auf(s, K, E, ["/"], 0.6)
    schritt(s, BETONE(K["/"][1], 0.8), EIN(l_w, 0.8))
    s.pause(0.6)
    baum_auf(s, K, E, ["etc", "home", "tmp", "usr"], 0.8)
    s.pause(0.4)
    baum_auf(s, K, E, ["student", "bin", "lib", "share"], 0.8)
    s.pause(0.6)
    schritt(s, WACHS(m, 0.6))
    schritt(s, ZEICHNE(hoch, 0.7), EIN(l_hoch, 0.7))
    schritt(s, ZEICHNE(runter, 0.8), EIN(l_unter, 0.8))
    s.speichern()


def k3laufwerke():
    """Links Windows mit den Bäumen C:\\ und D:\\, rechts ein Baum /; der Teilbaum von C: wandert unter /mnt/c."""
    s = Szene("linux/k3laufwerke")
    pos = {"C:\\": (-2.5, 1.0), "Users": (-2.95, 0.2), "Windows": (-2.05, 0.2), "D:\\": (-0.85, 1.0), "Fotos": (-0.85, 0.2),
           "/": (1.5, 1.0), "home": (0.6, 0.2), "usr": (1.5, 0.2), "mnt": (2.4, 0.2), "c": (2.4, -0.6)}
    vater = {"Users": "C:\\", "Windows": "C:\\", "Fotos": "D:\\", "home": "/", "usr": "/", "mnt": "/", "c": "mnt"}
    K, E, P = baum(s, list(pos), pos=pos, vater=vater, etiketten={"C:\\": "C:\\backslash", "D:\\": "D:\\backslash"})
    t_win = text(s, "Windows", (-1.75, 1.62), FS)
    t_lin = text(s, "Linux (WSL 2)", (1.6, 1.62), FS)
    trenn = linie(s, (-0.15, 1.8), (-0.15, -1.6), HELLGRAU, 2, DASH)
    l_c = text(s, T(s, "lwc", "Laufwerk C:", "drive C:", "unidad C:", "C: 盘", "lecteur C:", "C: sürücüsü"), (-2.5, -0.25), FM,
               "center", GRAU)
    l_d = text(s, T(s, "lwd", "Laufwerk D:", "drive D:", "unidad D:", "D: 盘", "lecteur D:", "D: sürücüsü"), (-0.85, -0.25), FM,
               "center", GRAU)
    l_mc = text(s, T(s, "lwc2", "Laufwerk C:", "drive C:", "unidad C:", "C: 盘", "lecteur C:", "C: sürücüsü"), (2.1, -0.6), FM,
                "right", ORANGE)
    d = (P["c"][0] - P["C:\\"][0], P["c"][1] - P["C:\\"][1])
    kopie = [kante(s, P["C:\\"], P[n]) for n in ("Users", "Windows")] + flach([knoten(s, n, *P[n]) for n in ("Users", "Windows")])
    schritt(s, EIN([t_win, t_lin, trenn], 0.6))
    baum_auf(s, K, E, ["C:\\", "Users", "Windows"], 0.7)
    baum_auf(s, K, E, ["D:\\", "Fotos"], 0.7)
    schritt(s, EIN([l_c, l_d], 0.5))
    s.pause(0.6)
    baum_auf(s, K, E, ["/"], 0.5)
    baum_auf(s, K, E, ["home", "usr", "mnt", "c"], 0.8)
    s.pause(0.6)
    schritt(s, EIN(kopie, 0.2))
    schritt(s, *[VER(i, d[0], d[1], 1.4) for i in kopie])
    schritt(s, BETONE(K["c"][1], 0.8), EIN(l_mc, 0.8))
    s.speichern()


# ================================================================== Abschnitt 2: Arbeitsverzeichnis und Pfade
def k3arbeitsverzeichnis():
    """Markierung „du bist hier“ in /home/student, pwd; nach cd /usr/bin springt sie, pwd nennt den neuen Weg."""
    s = Szene("linux/k3arbeitsverzeichnis")
    K, E, P = baum(s, ["/", "etc", "home", "tmp", "usr", "student", "bin", "lib", "share"])
    term = s.box("", (-1.62, -1.16), breite=3.6, hoehe=1.36, form="rect", farbe=GRAU, fuellung=TERM, dicke=2)
    x0 = -3.25
    ys = [-0.68 - 0.24 * i for i in range(5)]
    z = [tt(s, "$ pwd", x0, ys[0]), tt(s, "/home/student", x0, ys[1], farbe=ORANGE), tt(s, "$ cd /usr/bin", x0, ys[2]),
         tt(s, "$ pwd", x0, ys[3]), tt(s, "/usr/bin", x0, ys[4], farbe=ORANGE)]
    weg1 = [kante(s, P["/"], P["home"], ORANGE, 5), kante(s, P["home"], P["student"], ORANGE, 5)]
    weg2 = [kante(s, P["/"], P["usr"], ORANGE, 5), kante(s, P["usr"], P["bin"], ORANGE, 5)]
    m = rahmen(s, P["student"], 0.98, 0.46)
    l_hier = text(s, T(s, "hier", "du bist hier", "you are here", "estás aquí", "你在这里", "tu es ici", "buradasın"),
                  (P["student"][0] - 0.58, P["student"][1]), FM, "right", ORANGE)
    dx = P["bin"][0] - P["student"][0]
    schritt(s, ZEICHNE(list(E.values()), 0.8), WACHS([k[0] for k in K.values()] + [term], 0.8),
            EIN([k[1] for k in K.values()], 0.8))
    s.pause(0.6)
    schritt(s, WACHS(m, 0.6), EIN(l_hier, 0.6))
    for w in weg1:
        schritt(s, ZEICHNE(w, 0.4))
    schritt(s, EIN(z[0], 0.4))
    schritt(s, EIN(z[1], 0.5))
    s.pause(0.6)
    schritt(s, EIN(z[2], 0.5))
    schritt(s, AUS(weg1, 0.5), VER(m, dx, 0, 1.0), VER(l_hier, dx, 0, 1.0))
    for w in weg2:
        schritt(s, ZEICHNE(w, 0.4))
    schritt(s, EIN(z[3], 0.4))
    schritt(s, EIN(z[4], 0.5))
    s.speichern()


def k3pfad():
    """/usr/bin/bash oben; die Teile leuchten nacheinander, parallel wächst der Weg im Baum; Schrägstriche = Abzweigungen."""
    s = Szene("linux/k3pfad")
    K, E, P = baum(s, ["/", "etc", "home", "tmp", "usr", "student", "bin", "lib", "share", "bash"])
    e, x0, y = 0.3, -3.3, 1.95
    grau = tt(s, "/usr/bin/bash", x0, y, e, HELLGRAU)
    teile = [tt(s, "/", x0, y, e, ORANGE), tt(s, "usr", sp(x0, 1, e), y, e, ORANGE), tt(s, "/bin", sp(x0, 4, e), y, e, ORANGE),
             tt(s, "/bash", sp(x0, 8, e), y, e, ORANGE)]
    folge = ["/", "usr", "bin", "bash"]
    ringe = [rahmen(s, P[n], kb(n) + 0.16, 0.46) for n in folge]
    wege = [kante(s, P[a], P[b], ORANGE, 5) for a, b in zip(folge, folge[1:])]
    xm, yl = msp(x0, 4, 4, e), y + 0.52
    l_abz = text(s, T(s, "abzw", "Abzweigung", "branch", "bifurcación", "分岔", "embranchement", "dallanma"), (xm, yl), FM, "center",
                 ORANGE)
    faecher = [linie(s, (xm, yl - 0.1), (msp(x0, c, c, e), y + 0.2), ORANGE, 2) for c in (0, 4, 8)]
    l_datei = text(s, T(s, "datei", "Datei", "file", "archivo", "文件", "fichier", "dosya"), (P["bash"][0] + 0.45, P["bash"][1]),
                   FM, "left", GRAU)
    baum_ganz(s, K, E, [grau])
    s.pause(0.6)
    schritt(s, EIN(teile[0], 0.6), WACHS(ringe[0], 0.6))
    for i in range(1, 4):
        schritt(s, EIN(teile[i], 0.8), ZEICHNE(wege[i - 1], 0.8))
        schritt(s, WACHS(ringe[i], 0.4))
    schritt(s, EIN(l_datei, 0.5))
    s.pause(0.6)
    schritt(s, EIN(l_abz, 0.6), ZEICHNE(faecher, 0.6))
    s.speichern()


def k3absolutrelativ():
    """Absoluter Weg ab / (blau), relativer Weg bin/bash ab /usr (grün); ab /home/student führt bin/bash ins Leere (rot)."""
    s = Szene("linux/k3absolutrelativ")
    K, E, P = baum(s, ["/", "etc", "home", "tmp", "usr", "student", "bin", "lib", "share", "bash"])

    def seg(a, b, farbe, dx=0.0, spitze=False):
        p, q = (P[a][0] + dx, P[a][1] - KH / 2), (P[b][0] + dx, P[b][1] + KH / 2)
        return pf(s, p, q, farbe=farbe, dicke=4.5, spitze=0.12) if spitze else linie(s, p, q, farbe, 4.5)

    blau = [seg("/", "usr", BLAU), seg("usr", "bin", BLAU), seg("bin", "bash", BLAU, spitze=True)]
    gruen = [seg("usr", "bin", GRUEN, 0.13), seg("bin", "bash", GRUEN, 0.13, True)]
    r = [rahmen(s, P[n], kb(n) + 0.16, 0.46, f) for n, f in (("/", BLAU), ("usr", GRUEN), ("student", ROT))]
    ps = P["student"]
    rot = pf(s, (ps[0], ps[1] - KH / 2), (ps[0], ps[1] - 0.6), farbe=ROT, dash=DASH, dicke=3)
    kreuz = s.kreuzchen(None, ps[0], ps[1] - 0.78, ROT, 0.22, 4)
    l_kreuz = text(s, T(s, "keinbin", "kein Eintrag bin", "no entry bin", "no hay entrada bin", "没有 bin 这一项", "pas d'entrée bin",
                        "bin girdisi yok"), (ps[0] + 0.22, ps[1] - 0.78), FM, "left", ROT)
    e, x0 = 0.18, -3.3
    yl = [-1.42, -1.7, -1.98]
    xt = sp(x0, 14, e)
    lz = [tt(s, "/usr/bin/bash", x0, yl[0], e, BLAU), tt(s, "bin/bash", x0, yl[1], e, GRUEN), tt(s, "bin/bash", x0, yl[2], e, ROT)]
    lt = [text(s, T(s, "abs", "absolut: beginnt an der Wurzel", "absolute: starts at the root", "absoluta: empieza en la raíz",
                    "绝对路径：从根开始", "absolu : commence à la racine", "mutlak: kökten başlar"), (xt, yl[0]), FM, "left"),
          text(s, T(s, "rel1", "relativ: beginnt im Arbeitsverzeichnis /usr", "relative: starts in the working directory /usr",
                    "relativa: empieza en el directorio de trabajo /usr", "相对路径：从工作目录 /usr 开始",
                    "relatif : commence dans le répertoire de travail /usr", "göreli: çalışma dizini /usr içinde başlar"),
               (xt, yl[1]), FM, "left"),
          text(s, T(s, "rel2", "relativ ab /home/student: führt ins Leere", "relative from /home/student: leads nowhere",
                    "relativa desde /home/student: no lleva a nada", "从 /home/student 出发的相对路径：无处可去",
                    "relatif depuis /home/student : ne mène nulle part", "/home/student içinden göreli: hiçbir yere varmaz"),
               (xt, yl[2]), FM, "left")]
    baum_ganz(s, K, E)
    s.pause(0.6)
    schritt(s, WACHS(r[0], 0.6), EIN([lz[0], lt[0]], 0.6))
    for b in blau:
        schritt(s, ZEICHNE(b, 0.45))
    s.pause(0.6)
    schritt(s, WACHS(r[1], 0.6), EIN([lz[1], lt[1]], 0.6))
    for g in gruen:
        schritt(s, ZEICHNE(g, 0.45))
    s.pause(0.6)
    schritt(s, WACHS(r[2], 0.6), EIN([lz[2], lt[2]], 0.6))
    schritt(s, ZEICHNE(rot, 0.5))
    schritt(s, EIN([kreuz, l_kreuz], 0.5))
    s.speichern()


def k3punkte():
    """Von /usr/share/doc mit .. nach /usr/share, mit ../.. bis /, ein weiteres .. kreist auf / zurück."""
    s = Szene("linux/k3punkte")
    K, E, P = baum(s, ["/", "etc", "home", "tmp", "usr", "bin", "lib", "share", "doc"], dx=-0.4)
    a1 = pf(s, (2.92, -0.85), (2.92, -0.12), farbe=ORANGE, dicke=3.5)
    a2 = pf(s, (2.62, 0.22), (1.86, 0.6), farbe=ORANGE, dicke=3.5)
    a3 = pf(s, (1.45, 1.05), (-0.05, 1.45), farbe=ORANGE, dicke=3.5)
    cx, cy, rr = -0.88, 1.5, 0.18
    t1 = 5.0
    a4 = [s.weg(None, f"{cx}+{rr}*cos(t)", f"{cy}+{rr}*sin(t)", 0.7, t1, farbe=ORANGE, dicke=3.5, n=61),
          pf(s, (cx + rr * math.cos(t1), cy + rr * math.sin(t1)), (-0.665, 1.43), farbe=ORANGE, dicke=3.5, spitze=0.09)]
    la1 = tt(s, "..", 3.02, -0.48, 0.2, ORANGE)
    la23 = tt(s, "../..", 2.0, 1.1, 0.2, ORANGE)
    la4 = tt(s, "..", cx - rr - 0.08, cy, 0.2, ORANGE, "r")
    l_bleibt = text(s, T(s, "bleibt", "bleibt in /", "stays in /", "se queda en /", "仍在 /", "reste dans /", "/ içinde kalır"),
                    (cx - 0.15, cy + 0.42), FM, "center", ORANGE)
    pd = P["doc"]
    start = rahmen(s, pd, 1.0, 0.56, GRAU, 2, DASH)
    l_start = text(s, "Start", (pd[0] - 0.56, pd[1]), FM, "right", GRAU)
    m = rahmen(s, pd, 0.85, 0.44)
    leg = [rahmen(s, (-3.15, -0.9), 0.36, 0.24, ORANGE, 3),
           text(s, T(s, "arbv", "Arbeitsverzeichnis", "working directory", "directorio de trabajo", "工作目录",
                     "répertoire de travail", "çalışma dizini"), (-2.88, -0.9), FM, "left")]
    baum_ganz(s, K, E, leg)
    schritt(s, WACHS([start, m], 0.6), EIN(l_start, 0.6))
    s.pause(0.6)
    schritt(s, ZEICHNE(a1, 0.6), EIN(la1, 0.6))
    schritt(s, VER(m, 0, 0.8, 0.6))
    s.pause(0.6)
    schritt(s, EIN(la23, 0.4))
    schritt(s, ZEICHNE(a2, 0.5))
    schritt(s, VER(m, -0.95, 0.8, 0.6))
    schritt(s, ZEICHNE(a3, 0.5))
    schritt(s, VER(m, -1.9, 0.8, 0.6))
    s.pause(0.6)
    schritt(s, ZEICHNE(a4, 0.8), EIN([la4, l_bleibt], 0.8))
    schritt(s, BETONE(m, 0.6))
    s.speichern()


# ================================================================== Abschnitt 3: ls
def k3versteckt():
    """ls /etc/skel bleibt leer; ls -a zeigt ., .. und drei Dateien mit Punkt am Namensanfang."""
    s = Szene("linux/k3versteckt")
    e, x0 = 0.19, -3.15
    p1 = s.box("", (0, 1.0), breite=6.7, hoehe=0.78, form="rect", farbe=GRAU, fuellung=TERM, dicke=2)
    p2 = s.box("", (0, -0.45), breite=6.7, hoehe=1.5, form="rect", farbe=GRAU, fuellung=TERM, dicke=2)
    z1 = tt(s, "$ ls /etc/skel", x0, 1.17, e)
    l_leer = text(s, T(s, "leer", "keine Ausgabe: das Verzeichnis scheint leer", "no output: the directory looks empty",
                       "sin salida: el directorio parece vacío", "没有输出：目录看起来是空的", "aucune sortie : le répertoire semble vide",
                       "çıktı yok: dizin boş görünüyor"), (x0, 0.86), FM, "left", GRAU)
    z2 = tt(s, "$ ls -a /etc/skel", x0, 0.0, e)
    aus = ttz(s, ".  ..  .bash_logout  .bashrc  .profile", x0, -0.27, e)
    punkte = [tt(s, ".", sp(x0, c, e), -0.27, e, ORANGE) for c in (0, 3, 4, 7, 21, 30)] + \
             [linie(s, (sp(x0, c, e) + 0.01, -0.36), (sp(x0, c + 1, e) - 0.01, -0.36), ORANGE, 3.5) for c in (0, 3, 4, 7, 21, 30)]
    l_punkt = text(s, T(s, "punkt", "Punkt am Namensanfang:\nversteckt", "dot at the start of the name:\nhidden",
                        "punto al inicio del nombre:\noculto", "名称以点开头：\n隐藏", "point au début du nom :\ncaché",
                        "adın başında nokta:\ngizli"), (sp(x0, 40.5, e), -0.27), FM, "left", ORANGE)
    kl1 = klammer(s, sp(x0, 0, e) + 0.02, sp(x0, 5, e) - 0.02, -0.43)
    lk1 = text(s, T(s, "sonder", "Sondernamen", "special names", "nombres especiales", "特殊名称", "noms spéciaux", "özel adlar"),
               (x0, -0.62), FM, "left", GRAU)
    kl2 = klammer(s, sp(x0, 7, e) + 0.02, sp(x0, 38, e) - 0.02, -0.43)
    lk2 = text(s, T(s, "dreiv", "drei versteckte Dateien", "three hidden files", "tres archivos ocultos", "三个隐藏文件",
                    "trois fichiers cachés", "üç gizli dosya"), (msp(x0, 7, 37, e), -0.62), FM, "center", GRAU)
    l_da = text(s, T(s, "da", "Die Dateien waren die ganze Zeit da.", "The files were there all along.",
                     "Los archivos estaban ahí todo el tiempo.", "这些文件一直都在。", "Les fichiers étaient là depuis le début.",
                     "Dosyalar baştan beri oradaydı."), (x0, -0.97), FM, "left")
    schritt(s, WACHS([p1, p2], 0.5))
    schritt(s, EIN(z1, 0.5))
    schritt(s, EIN(l_leer, 0.5))
    s.pause(0.6)
    schritt(s, EIN(z2, 0.5))
    schritt(s, EIN(aus, 0.6))
    s.pause(0.4)
    schritt(s, EIN(punkte, 0.5), EIN(l_punkt, 0.5))
    schritt(s, BETONE(punkte, 0.7))
    schritt(s, ZEICHNE(kl1, 0.5), EIN(lk1, 0.5))
    schritt(s, ZEICHNE(kl2, 0.5), EIN(lk2, 0.5))
    s.pause(0.4)
    schritt(s, EIN(l_da, 0.6))
    s.speichern()


def k3lsl():
    """Eine Zeile von ls -l zerfällt in ihre Felder; Klammern mit Beschriftung; Rechte und Zahl zum Schluss grau."""
    s = Szene("linux/k3lsl")
    e, y = 0.18, 0.2
    c = cw(e)
    zeile = "-rw-r--r-- 1 root root 3771 Feb 13  2026 .bashrc"
    x0 = -len(zeile) * c / 2
    # (Text, Spalte); das Zeitfeld hat zwei Leerzeichen und besteht deshalb aus zwei Stücken
    stuecke = [[("-", 0)], [("rw-r--r--", 1)], [("1", 11)], [("root", 13)], [("root", 18)], [("3771", 23)],
               [("Feb 13", 28), ("2026", 36)], [(".bashrc", 41)]]
    g = 0.22
    x0n = -(len(zeile) * c + 7 * g) / 2
    namen = [T(s, "art", "Art", "type", "tipo", "类型", "type", "tür"),
             T(s, "rechte", "Zugriffsrechte", "permissions", "permisos", "访问权限", "droits d'accès", "erişim hakları"),
             T(s, "zahl", "Zahl", "number", "número", "数字", "nombre", "sayı"),
             T(s, "besitzer", "Besitzer", "owner", "propietario", "所有者", "propriétaire", "sahip"),
             T(s, "gruppe", "Gruppe", "group", "grupo", "组", "groupe", "grup"),
             T(s, "groesse", "Größe in Bytes", "size in bytes", "tamaño en bytes", "大小（字节）", "taille en octets",
               "bayt cinsinden boyut"),
             T(s, "zeit", "letzte Änderung", "last modified", "última modificación", "最后修改时间", "dernière modification",
               "son değişiklik"),
             T(s, "name", "Name", "name", "nombre", "名称", "nom", "ad")]
    ids, schieb, kl, lab, schl = [], [], [], [], []
    for k, st in enumerate(stuecke):
        dx = x0n - x0 + k * g
        ids.append([tt(s, t, sp(x0, col, e), y, e) for t, col in st])
        schieb.append(dx)
        a = sp(x0, st[0][1], e) + dx
        b = sp(x0, st[-1][1] + len(st[-1][0]), e) + dx
        grau = k in (1, 2)
        unten = k % 2 == 0
        kl.append(klammer(s, a + 0.01, b - 0.01, y - 0.16 if unten else y + 0.16, unten=unten,
                          farbe=HELLGRAU if grau else GRAU))
        lab.append(text(s, namen[k], ((a + b) / 2, y - 0.33 if unten else y + 0.33), FM, "center", GRAU if grau else SCHWARZ))
        if grau:
            schl.append(schleier(s, ((a + b) / 2, y), b - a + 0.04, 0.22, 0.6))
    note = text(s, T(s, "nichterkl", "grau: in diesem Abschnitt nicht erklärt", "gray: not explained in this section",
                     "gris: no se explica en esta sección", "灰色：本节不作解释", "gris : non expliqué dans cette section",
                     "gri: bu bölümde açıklanmıyor"), (0, -0.72), FM, "center", GRAU)
    schritt(s, EIN(ids, 0.6))
    s.pause(0.6)
    schritt(s, *[VER(i, dx, 0, 1.0) for st, dx in zip(ids, schieb) for i in st])
    s.pause(0.4)
    for k in range(8):
        schritt(s, ZEICHNE(kl[k], 0.45), EIN(lab[k], 0.45))
    s.pause(0.6)
    schritt(s, EIN(schl + [note], 0.7))
    s.speichern()


def k3sortieren():
    """Vier Karten nach Namen; mit -S, -t und -tr wandern sie in die nächste Spalte und ordnen sich um."""
    s = Szene("linux/k3sortieren")
    dateien = [("bericht.txt", "3812", "09:00"), ("foto.jpg", "2183544", "10:30"), ("liste.txt", "120", "08:15"),
               ("notiz.txt", "0", "11:00")]
    reihen = [[0, 1, 2, 3], [1, 0, 2, 3], [3, 1, 0, 2], [2, 0, 1, 3]]
    xs = [-2.55, -0.85, 0.85, 2.55]
    ys = [0.8, 0.25, -0.3, -0.85]
    befehle = ["ls", "ls -S", "ls -t", "ls -tr"]
    unter = [T(s, "nnamen", "nach Namen", "by name", "por nombre", "按名称", "par nom", "ada göre"),
             T(s, "ngroesse", "größte zuerst", "largest first", "más grandes primero", "最大的在前", "plus gros d'abord",
               "en büyük önce"),
             T(s, "nzeit", "neueste zuerst", "newest first", "más recientes primero", "最新的在前", "plus récents d'abord",
               "en yeni önce"),
             T(s, "nalt", "älteste zuerst", "oldest first", "más antiguos primero", "最旧的在前", "plus anciens d'abord",
               "en eski önce")]

    def karte(f, x, y):
        n, g, z = dateien[f]
        return [s.box("", (x, y), breite=1.55, hoehe=0.48, form="round", farbe=GRAU, fuellung=WEISS, dicke=2),
                s.text(None, n, (x - 0.68, y + 0.1), FK, "left"),
                s.text(None, f"{g} B · {z}", (x - 0.68, y - 0.12), FM, "left", GRAU)]

    koepfe = [tt(s, b, x, 1.58, 0.2, SCHWARZ, "m") for b, x in zip(befehle, xs)]
    unterk = [text(s, u, (x, 1.28), FM, "center", GRAU) for u, x in zip(unter, xs)]
    karten = []
    for c in range(4):
        q = max(c - 1, 0)
        karten.append({f: karte(f, xs[q], ys[reihen[q].index(f)]) for f in range(4)})
    schritt(s, EIN([koepfe[0], unterk[0]] + [karten[0][f] for f in range(4)], 0.6))
    for c in range(1, 4):
        s.pause(0.6)
        schritt(s, EIN([koepfe[c], unterk[c]], 0.5))
        schritt(s, EIN([karten[c][f] for f in range(4)], 0.2))
        schritt(s, *[VER(i, xs[c] - xs[c - 1], ys[reihen[c].index(f)] - ys[reihen[c - 1].index(f)], 1.0)
                     for f in range(4) for i in karten[c][f]])
        schritt(s, BETONE([karten[c][f][2] for f in range(4)], 0.7))
    s.speichern()


def k3namen():
    """ls -d /mnt/c/Program Files: Schnitt an jedem Leerzeichen, zwei Argumente (rot); mit Anführungszeichen eines (grün)."""
    s = Szene("linux/k3namen")
    e = 0.21
    c = cw(e)
    z1, y1 = "$ ls -d /mnt/c/Program Files", 1.05
    z2, y2 = '$ ls -d "/mnt/c/Program Files"', -0.4
    x1, x2 = -len(z1) * c / 2, -len(z2) * c / 2

    def wkasten(x0, y, a, b, farbe, deckung=0.12):
        return kasten(s, (msp(x0, a, b, e), y), (b - a + 1) * c + 0.12, 0.36, fuellung=farbe, farbe=farbe, dicke=2,
                      deckung=deckung)[0]

    def schnitt(x0, y, col, farbe=ROT):
        xs_ = sp(x0, col, e) + c / 2
        return linie(s, (xs_, y + 0.26), (xs_, y - 0.26), farbe, 2.5, DASH)

    zeile1 = tt(s, z1, x1, y1, e)
    l_cut = text(s, T(s, "cut", "Schnitt an jedem Leerzeichen", "cut at every space", "corte en cada espacio", "在每个空格处切开",
                      "coupure à chaque espace", "her boşlukta kesilir"), (0, y1 + 0.44), FM, "center", ROT)
    cuts1 = [schnitt(x1, y1, k) for k in (4, 7, 22)]
    box1 = [wkasten(x1, y1, 2, 3, GRAU, 0.1), wkasten(x1, y1, 5, 6, GRAU, 0.1), wkasten(x1, y1, 8, 21, ROT),
            wkasten(x1, y1, 23, 27, ROT)]
    la1 = [text(s, T(s, "arg1", "Argument 1", "argument 1", "argumento 1", "参数 1", "argument 1", "argüman 1"),
                (msp(x1, 8, 21, e), y1 - 0.38), FM, "center", ROT),
           text(s, T(s, "arg2", "Argument 2", "argument 2", "argumento 2", "参数 2", "argument 2", "argüman 2"),
                (msp(x1, 23, 27, e), y1 - 0.38), FM, "center", ROT)]
    l_zwei = text(s, T(s, "zwei", "zwei Argumente, keins davon gibt es", "two arguments, neither exists",
                       "dos argumentos, no existe ninguno", "两个参数，都不存在", "deux arguments, aucun n'existe",
                       "iki argüman, ikisi de yok"), (0, y1 - 0.64), FM, "center", ROT)
    zeile2 = tt(s, z2, x2, y2, e)
    cuts2 = [schnitt(x2, y2, k) for k in (4, 7)]
    xi = sp(x2, 22, e) + c / 2
    kein = [linie(s, (xi, y2 + 0.32), (xi, y2 + 0.16), GRUEN, 2.5),
            text(s, T(s, "kein", "kein Schnitt", "no cut", "sin corte", "不切开", "pas de coupure", "kesilmez"),
                 (xi, y2 + 0.44), FM, "center", GRUEN)]
    box2 = [wkasten(x2, y2, 2, 3, GRAU, 0.1), wkasten(x2, y2, 5, 6, GRAU, 0.1), wkasten(x2, y2, 8, 29, GRUEN)]
    la2 = text(s, T(s, "einarg", "ein Argument", "one argument", "un argumento", "一个参数", "un seul argument", "tek argüman"),
               (msp(x2, 8, 29, e), y2 - 0.38), FM, "center", GRUEN)
    l_bek = text(s, T(s, "bekommt", "ls bekommt:", "ls receives:", "ls recibe:", "ls 收到：", "ls reçoit :", "ls şunu alır:"),
                 (-1.2, y2 - 0.86), FM, "right")
    erg = tt(s, "/mnt/c/Program Files", -1.08, y2 - 0.86, 0.19, GRUEN)
    schritt(s, EIN(zeile1, 0.6))
    s.pause(0.6)
    schritt(s, ZEICHNE(cuts1, 0.7), EIN(l_cut, 0.7))
    schritt(s, WACHS(box1, 0.5), EIN(la1, 0.5))
    schritt(s, EIN(l_zwei, 0.5))
    s.pause(0.6)
    schritt(s, EIN(zeile2, 0.6))
    schritt(s, ZEICHNE(cuts2, 0.6), EIN(kein, 0.6))
    schritt(s, WACHS(box2, 0.6), EIN(la2, 0.6))
    s.pause(0.4)
    schritt(s, EIN([l_bek, erg], 0.7))
    s.speichern()


# ================================================================== Abschnitt 4: Dateien ansehen
def k3text():
    """Äpfel⏎Brot⏎ als zwölf Bytes; Ä belegt zwei, die Zeilenenden sind 10; darunter dieselben Bytes als zwei Zeilen Text."""
    s = Szene("linux/k3text")
    werte = (195, 132, 112, 102, 101, 108, 10, 66, 114, 111, 116, 10)
    b, h, y = 0.52, 0.42, 0.55
    xl = -6 * b
    xs = [xl + (i + 0.5) * b for i in range(12)]
    kaest = [s.box("", (x, y), breite=b, hoehe=h, form="rect", farbe=SCHWARZ, fuellung=WEISS, dicke=2.5) for x in xs]
    zahlen = [text(s, str(v), (x, y), FK, "center", ORANGE if v == 10 else SCHWARZ) for v, x in zip(werte, xs)]
    yz = 0.08
    zl = T(s, "zende", "Zeilen-\nende", "line\nend", "fin de\nlínea", "换行符", "fin de\nligne", "satır\nsonu")
    zeichen = {0: text(s, "Ä", ((xs[0] + xs[1]) / 2, yz), FS, "center", BLAU)}
    for i, ch in zip((2, 3, 4, 5, 7, 8, 9, 10), "pfelBrot"):
        zeichen[i] = text(s, ch, (xs[i], yz), FS, "center", BLAU)
    for i in (6, 11):
        zeichen[i] = text(s, zl, (xs[i], yz - 0.04), FM, "center", ORANGE)
    gruppen = [[0, 1], [2], [3], [4], [5], [6], [7], [8], [9], [10], [11]]
    kl = klammer(s, xs[0] - b / 2 + 0.03, xs[1] + b / 2 - 0.03, y + h / 2 + 0.1, unten=False)
    l_ae = text(s, T(s, "ae2", "Ä: 2 Bytes", "Ä: 2 bytes", "Ä: 2 bytes", "Ä：2 个字节", "Ä : 2 octets", "Ä: 2 bayt"),
                ((xs[0] + xs[1]) / 2, y + h / 2 + 0.3), FM)
    pfeil = pf(s, (0, -0.3), (0, -0.56), farbe=GRAU)
    anz = s.box("", (0, -0.95), breite=1.6, hoehe=0.7, form="rect", farbe=GRAU, fuellung=TERM, dicke=2)
    zeilen = [text(s, "Äpfel", (-0.55, -0.82), FS, "left"), text(s, "Brot", (-0.55, -1.09), FS, "left")]
    l_anz = text(s, T(s, "alstext", "als Text angezeigt", "shown as text", "mostrado como texto", "显示为文本", "affiché comme texte",
                      "metin olarak gösterilir"), (-0.95, -0.95), FM, "right", GRAU)
    schritt(s, WACHS(kaest, 0.6))
    s.pause(0.4)
    for gr in gruppen:
        schritt(s, EIN([zahlen[i] for i in gr] + [zeichen[gr[0]]], 0.5 if gr[0] in (0, 6, 11) else 0.3))
    s.pause(0.6)
    schritt(s, ZEICHNE(kl, 0.6), EIN(l_ae, 0.6))
    s.pause(0.4)
    schritt(s, BETONE([zahlen[6], zahlen[11]], 0.7))
    schritt(s, ZEICHNE(pfeil, 0.5), WACHS(anz, 0.5))
    schritt(s, EIN(zeilen + [l_anz], 0.6))
    s.speichern()


def k3headtail():
    """Stapel aus zwölf Zeilen; head -n 3 hebt die ersten drei hervor, tail -n 2 die letzten zwei, der Rest wird grau."""
    s = Szene("linux/k3headtail")
    n, dz, hz, xa, xb = 12, 0.22, 0.19, -2.1, 0.0
    ys = [1.25 - dz * i for i in range(n)]
    balken = [flaeche(s, xa, y - hz / 2, xb, y + hz / 2, GRAU_HELL) for y in ys]
    zeilen = [text(s, T(s, f"z{i + 1}", f"Zeile {i + 1}", f"line {i + 1}", f"línea {i + 1}", f"第 {i + 1} 行", f"ligne {i + 1}",
                        f"{i + 1}. satır"), (xa + 0.12, y), FM, "left") for i, y in enumerate(ys)]
    blau = [mark(s, xa, xb, ys[i], hz, BLAU, 0.3) for i in range(3)]
    gruen = [mark(s, xa, xb, ys[i], hz, GRUEN, 0.3) for i in (10, 11)]
    grau = schleier(s, ((xa + xb) / 2, (ys[3] + ys[9]) / 2), xb - xa + 0.02, ys[3] - ys[9] + hz + 0.01, 0.6)
    xk, xt = xb + 0.14, xb + 0.3
    k_head = vklammer(s, xk, ys[0] + hz / 2, ys[2] - hz / 2, BLAU)
    l_head = [tt(s, "head -n 3", xt, ys[1] + 0.11, 0.19, BLAU),
              text(s, T(s, "erste3", "die ersten 3 Zeilen", "the first 3 lines", "las 3 primeras líneas", "前 3 行",
                        "les 3 premières lignes", "ilk 3 satır"), (xt, ys[1] - 0.13), FM, "left", BLAU)]
    yt = (ys[10] + ys[11]) / 2
    k_tail = vklammer(s, xk, ys[10] + hz / 2, ys[11] - hz / 2, GRUEN)
    l_tail = [tt(s, "tail -n 2", xt, yt + 0.11, 0.19, GRUEN),
              text(s, T(s, "letzte2", "die letzten 2 Zeilen", "the last 2 lines", "las 2 últimas líneas", "最后 2 行",
                        "les 2 dernières lignes", "son 2 satır"), (xt, yt - 0.13), FM, "left", GRUEN)]
    l_rest = text(s, T(s, "rest", "dazwischen: nicht ausgegeben", "in between: not printed", "en medio: no se muestran",
                       "中间：不输出", "entre les deux : non affichées", "aradakiler: yazdırılmaz"), (xt, (ys[3] + ys[9]) / 2), FM,
                  "left", GRAU)
    schritt(s, EIN(balken + zeilen, 0.8))
    s.pause(0.6)
    schritt(s, EIN(blau, 0.6), ZEICHNE(k_head, 0.6), EIN(l_head, 0.6))
    s.pause(0.6)
    schritt(s, EIN(gruen, 0.6), ZEICHNE(k_tail, 0.6), EIN(l_tail, 0.6))
    s.pause(0.6)
    schritt(s, EIN([grau, l_rest], 0.7))
    s.speichern()


def k3wc():
    """wc an gruss.txt: erst Zeilenenden, dann Wörter, dann Bytes gezählt; die drei Summen wandern in die Spalten der Ausgabe."""
    s = Szene("linux/k3wc")
    e, x0 = 0.22, -3.0
    zeilen = ["Guten Morgen", "ein Test", "fertig"]
    ys = [1.15, 0.85, 0.55]
    papier = s.box("", (-2.1, 0.85), breite=2.1, hoehe=1.05, form="rect", farbe=GRAU, fuellung=WEISS, dicke=2)
    l_datei = text(s, T(s, "dname", "Datei gruss.txt", "file gruss.txt", "archivo gruss.txt", "文件 gruss.txt", "fichier gruss.txt",
                        "dosya gruss.txt"), (-3.15, 1.53), FM, "left", GRAU)
    tz = [tt(s, z, x0, y, e) for z, y in zip(zeilen, ys)]
    ende = [s.formel(r"\hookleftarrow", mitte=(round(sp(x0, len(z), e) + 0.14, 4), y), hoehe=0.15, farbe=ORANGE)
            for z, y in zip(zeilen, ys)]
    worte = [(0, 0, 4), (0, 6, 11), (1, 0, 2), (1, 4, 7), (2, 0, 5)]
    wboxen = [kasten(s, (msp(x0, a, b, e), ys[z]), (b - a + 1) * cw(e) + 0.08, 0.27, fuellung=BLAU, farbe=BLAU, dicke=1.5,
                     deckung=0.12)[0] for z, a, b in worte]
    xc = [-0.35, 0.85, 2.05]
    koepfe = [text(s, T(s, "kzeilen", "Zeilenenden", "line ends", "finales de línea", "换行符", "fins de ligne", "satır sonları"),
                   (xc[0], 1.53), FM, "center", ORANGE),
              text(s, T(s, "kwoerter", "Wörter", "words", "palabras", "单词", "mots", "sözcükler"), (xc[1], 1.53), FM, "center",
                   BLAU),
              text(s, "Bytes", (xc[2], 1.53), FM, "center", GRUEN)]
    werte = [("1", "1", "1"), ("2", "2", "1"), ("13", "9", "7")]
    spalten = [[text(s, w, (xc[k], y), FK) for w, y in zip(werte[k], ys)] for k in range(3)]
    strich = linie(s, (-0.85, 0.38), (2.5, 0.38), GRAU, 2)
    summen = ["3", "5", "29"]
    ysum = 0.2
    sums = [tt(s, t, xc[k], ysum, e, SCHWARZ, "m") for k, t in enumerate(summen)]
    note = text(s, T(s, "zbyte", "das Zeilenende zählt als 1 Byte", "the line end counts as 1 byte",
                     "el fin de línea cuenta como 1 byte", "换行符算作 1 个字节", "la fin de ligne compte pour 1 octet",
                     "satır sonu 1 bayt sayılır"), (xc[1], -0.06), FM, "center", GRAU)
    yb, yo = -0.45, -0.72
    befehl = tt(s, "$ wc gruss.txt", x0, yb, e)
    flug = [tt(s, t, xc[k], ysum, e, SCHWARZ, "m") for k, t in enumerate(summen)]
    ziele = [msp(x0, 1, 1, e), msp(x0, 4, 4, e), msp(x0, 6, 7, e)]
    dname = tt(s, "gruss.txt", sp(x0, 9, e), yo, e)
    schritt(s, WACHS(papier, 0.6), EIN(tz + [l_datei], 0.6))
    s.pause(0.6)
    schritt(s, EIN(koepfe, 0.5))
    for i in range(3):
        schritt(s, EIN([ende[i], spalten[0][i]], 0.4))
    schritt(s, EIN([strich, sums[0]], 0.4))
    s.pause(0.5)
    schritt(s, WACHS(wboxen, 0.6), EIN(spalten[1], 0.6))
    schritt(s, EIN(sums[1], 0.4))
    s.pause(0.5)
    schritt(s, EIN(spalten[2] + [note], 0.6))
    schritt(s, EIN(sums[2], 0.4))
    s.pause(0.6)
    schritt(s, EIN(befehl, 0.5))
    schritt(s, EIN(flug, 0.2))
    schritt(s, *[ZU(f, x, yo, 0.9) for f, x in zip(flug, ziele)], EIN(dname, 0.9))
    s.speichern()


def k3magie():
    """file liest die ersten Bytes und vergleicht sie mit Kennungen: 127 E L F → Programm, 137 P N G → Bild; der Name zählt nicht."""
    s = Szene("linux/k3magie")
    eb, hb = 0.42, 0.36

    def streifen(werte, x0, y, b, h, groesse):
        ids = []
        for i, w in enumerate(werte):
            x = x0 + (i + 0.5) * b
            ids += [s.box("", (x, y), breite=b, hoehe=h, form="rect", farbe=SCHWARZ, fuellung=WEISS, dicke=2),
                    text(s, w, (x, y), groesse)]
        return ids

    nA = tt(s, "/usr/bin/bash", -3.3, 1.3, 0.17)
    bA = streifen(("127", "E", "L", "F"), -3.3, 0.92, eb, hb, FK) + [text(s, "…", (-1.5, 0.92), FK)]
    nB = tt(s, "ubuntu-logo-text.png", -3.3, -0.2, 0.17)
    bB = streifen(("137", "P", "N", "G"), -3.3, -0.58, eb, hb, FK) + [text(s, "…", (-1.5, -0.58), FK)]
    typen = [T(s, "elf", "ELF-Programm", "ELF program", "programa ELF", "ELF 程序", "programme ELF", "ELF programı"),
             T(s, "png", "PNG-Bild", "PNG image", "imagen PNG", "PNG 图像", "image PNG", "PNG resmi"),
             T(s, "jpeg", "JPEG-Bild", "JPEG image", "imagen JPEG", "JPEG 图像", "image JPEG", "JPEG resmi"),
             T(s, "pdf", "PDF-Dokument", "PDF document", "documento PDF", "PDF 文档", "document PDF", "PDF belgesi")]
    kennung = [("127", "E", "L", "F"), ("137", "P", "N", "G"), ("255", "216", "255"), ("%", "P", "D", "F")]
    ry = [1.08, 0.6, 0.12, -0.36]
    liste = [s.box("", (1.425, 0.39), breite=3.75, hoehe=1.98, form="rect", farbe=GRAU, fuellung=WEISS, dicke=2),
             text(s, T(s, "kenn", "Kennungen (Auszug)", "signatures (excerpt)", "firmas (extracto)", "文件标识（节选）",
                       "signatures (extrait)", "imzalar (alıntı)"), (1.425, 1.56), FK)]
    for kw, y, t in zip(kennung, ry, typen):
        liste += streifen(kw, -0.2, y, 0.38, 0.32, FM)
        liste += [pf(s, (1.4, y), (1.72, y), farbe=GRAU, dicke=2, spitze=0.08), text(s, t, (1.82, y), FK, "left")]
    mA = mark(s, -0.4, 3.25, ry[0], 0.42, GRUEN, 0.18)
    mB = mark(s, -0.4, 3.25, ry[1], 0.42, GRUEN, 0.18)
    rA = rahmen(s, (-3.3 + 2 * eb, 0.92), 4 * eb + 0.1, hb + 0.12, ORANGE, 3)
    rB = rahmen(s, (-3.3 + 2 * eb, -0.58), 4 * eb + 0.1, hb + 0.12, ORANGE, 3)
    vA = linie(s, (-3.3 + 4 * eb + 0.05, 1.1), (-0.24, ry[0]), ORANGE, 2.5)
    vB = linie(s, (-3.3 + 4 * eb + 0.05, -0.4), (-0.24, ry[1]), ORANGE, 2.5)
    eA = text(s, T(s, "eelf", "→ ELF-Programm", "→ ELF program", "→ programa ELF", "→ ELF 程序", "→ programme ELF",
                   "→ ELF programı"), (-3.3, 0.52), FK, "left", GRUEN)
    eB = text(s, T(s, "epng", "→ PNG-Bild", "→ PNG image", "→ imagen PNG", "→ PNG 图像", "→ image PNG", "→ PNG resmi"),
              (-3.3, -0.98), FK, "left", GRUEN)
    strA = linie(s, (-3.33, 1.3), (-3.3 + 13 * cw(0.17) + 0.03, 1.3), GRAU, 2.5)
    strB = linie(s, (-3.33, -0.2), (-3.3 + 20 * cw(0.17) + 0.03, -0.2), GRAU, 2.5)
    l_name = text(s, T(s, "egal", "Der Dateiname spielt keine Rolle.", "The file name does not matter.",
                       "El nombre del archivo no importa.", "文件名无关紧要。", "Le nom du fichier ne compte pas.",
                       "Dosya adının önemi yok."), (-3.3, -1.38), FM, "left", GRAU)
    schritt(s, EIN(liste, 0.7))
    s.pause(0.6)
    schritt(s, EIN([nA] + bA, 0.6))
    schritt(s, WACHS(rA, 0.5))
    schritt(s, ZEICHNE(vA, 0.6))
    schritt(s, EIN(mA, 0.6))
    schritt(s, EIN(eA, 0.5))
    s.pause(0.6)
    schritt(s, EIN([nB] + bB, 0.6))
    schritt(s, WACHS(rB, 0.5))
    schritt(s, ZEICHNE(vB, 0.6))
    schritt(s, EIN(mB, 0.6))
    schritt(s, EIN(eB, 0.5))
    s.pause(0.6)
    schritt(s, ZEICHNE([strA, strB], 0.6), EIN(l_name, 0.6))
    s.speichern()


# ================================================================== Abschnitt 5: Anlegen
def k3mkdirp():
    """mkdir fotos/urlaub/2026 scheitert an urlaub; mkdir -p legt urlaub und 2026 nacheinander an."""
    s = Szene("linux/k3mkdirp")
    pos = {"linuxk3": (1.85, 1.55), "fotos": (1.15, 0.75), "rezepte": (2.6, 0.75), "urlaub": (1.15, -0.05),
           "2026": (1.15, -0.85)}
    vater = {"fotos": "linuxk3", "rezepte": "linuxk3", "urlaub": "fotos", "2026": "urlaub"}
    alt = ["linuxk3", "fotos", "rezepte"]
    K, E, P = baum(s, alt, pos=pos, vater=vater)
    term = s.box("", (-1.785, 1.5), breite=3.27, hoehe=0.9, form="rect", farbe=GRAU, fuellung=TERM, dicke=2)
    e, x0 = 0.18, -3.3
    z1 = tt(s, "$ mkdir fotos/urlaub/2026", x0, 1.75, e)
    z2 = tt(s, "mkdir: No such file or directory", x0, 1.5, e, ROT)
    z3 = tt(s, "$ mkdir -p fotos/urlaub/2026", x0, 1.25, e)
    pu = pos["urlaub"]
    geist_k = kante(s, pos["fotos"], pu, GRAU, 2, DASH)
    geist = knoten(s, "urlaub", *pu, art="geist", textfarbe=GRAU)
    kreuz = s.kreuzchen(None, pu[0] + 0.58, pu[1], ROT, 0.22, 4)
    l_fehlt = text(s, T(s, "fehlt", "fehlt", "missing", "falta", "不存在", "manquant", "yok"), (pu[0] + 0.78, pu[1]), FM, "left", ROT)
    neu_k = [kante(s, pos["fotos"], pu), kante(s, pu, pos["2026"])]
    neu = [knoten(s, "urlaub", *pu, art="neu"), knoten(s, "2026", *pos["2026"], art="neu")]
    leg = [s.box("", (-3.15, 0.55), breite=0.32, hoehe=0.2, form="round", farbe=GRUEN, fuellung=GRUEN_HELL, dicke=2.5),
           text(s, T(s, "neu", "neu angelegt", "newly created", "recién creado", "新建", "nouvellement créé", "yeni oluşturuldu"),
                (-2.9, 0.55), FM, "left"),
           s.box("", (-3.15, 0.25), breite=0.32, hoehe=0.2, form="round", farbe=BLAU, fuellung=BLAU_HELL, dicke=2),
           text(s, T(s, "alt", "schon vorhanden, bleibt unberührt", "already there, left untouched", "ya existía, no se toca",
                     "已存在，保持不变", "existait déjà, reste intact", "zaten vardı, dokunulmaz"), (-2.9, 0.25), FM, "left")]
    schritt(s, WACHS([term] + [K[n][0] for n in alt], 0.7), EIN([K[n][1] for n in alt], 0.7), ZEICHNE(list(E.values()), 0.7))
    s.pause(0.6)
    schritt(s, EIN(z1, 0.5))
    schritt(s, BETONE(K["fotos"][1], 0.6))
    schritt(s, ZEICHNE(geist_k, 0.4), EIN(geist, 0.4))
    schritt(s, EIN([kreuz, l_fehlt], 0.5))
    schritt(s, EIN(z2, 0.5))
    s.pause(0.6)
    schritt(s, AUS([geist_k, kreuz, l_fehlt] + geist, 0.4), EIN(z3, 0.5))
    schritt(s, ZEICHNE(neu_k[0], 0.4), WACHS(neu[0][0], 0.6), EIN(neu[0][1], 0.6))
    schritt(s, ZEICHNE(neu_k[1], 0.4), WACHS(neu[1][0], 0.6), EIN(neu[1][1], 0.6))
    s.pause(0.4)
    schritt(s, EIN(leg, 0.6))
    s.speichern()


def k3touch():
    """Links: touch auf einen neuen Namen → leere Datei, 0 Bytes. Rechts: touch auf die Einkaufsliste → Inhalt bleibt, Uhr auf jetzt."""
    s = Szene("linux/k3touch")
    trenn = linie(s, (0.0, 1.9), (0.0, -1.15), HELLGRAU, 2, DASH)
    t_l = text(s, T(s, "neuname", "neuer Name", "new name", "nombre nuevo", "新名称", "nouveau nom", "yeni ad"), (-1.75, 1.72), FK)
    t_r = text(s, T(s, "vorh", "vorhandene Datei", "existing file", "archivo existente", "已有文件", "fichier existant", "var olan dosya"),
               (1.75, 1.72), FK)
    cmd_l = tt(s, "$ touch einkauf.txt", -1.75, 1.38, 0.17, SCHWARZ, "m")
    cmd_r = tt(s, "$ touch einkauf.txt", 1.75, 1.38, 0.17, SCHWARZ, "m")
    l_aend = T(s, "aend", "letzte Änderung", "last modified", "última modificación", "最后修改", "dernière modification",
               "son değişiklik")
    jetzt = T(s, "jetzt", "Nov 10 02:41 (jetzt)", "Nov 10 02:41 (now)", "Nov 10 02:41 (ahora)", "Nov 10 02:41（现在）",
              "Nov 10 02:41 (maintenant)", "Nov 10 02:41 (şimdi)")
    # links: neue, leere Datei
    doc_l = s.box("", (-2.45, 0.4), breite=0.9, hoehe=1.15, form="rect", farbe=SCHWARZ, fuellung=WEISS, dicke=2.5)
    nl = [text(s, "einkauf.txt", (-2.45, -0.37), FM),
          text(s, T(s, "b0", "0 Bytes", "0 bytes", "0 bytes", "0 字节", "0 octet", "0 bayt"), (-2.45, -0.62), FM, "center", GRAU)]
    ul = list(uhr(s, -0.95, 0.55, 2, 41))
    zl = [text(s, jetzt, (-0.95, 0.08), FM, "center", ORANGE), text(s, l_aend, (-0.95, -0.17), FM, "center", GRAU)]
    neu_l = text(s, T(s, "neuleer", "neu angelegt, leer", "newly created, empty", "recién creado, vacío", "新建，空文件",
                      "créé, vide", "yeni oluşturuldu, boş"), (-2.45, -0.92), FM, "center", GRUEN)
    # rechts: vorhandene Datei mit vier Zeilen
    doc_r = s.box("", (1.05, 0.4), breite=0.9, hoehe=1.15, form="rect", farbe=SCHWARZ, fuellung=WEISS, dicke=2.5)
    inhalt = [text(s, w, (0.72, y), FM, "left") for w, y in zip(("Milch", "Brot", "Äpfel", "Kaffee"), (0.8, 0.57, 0.34, 0.11))]
    nr = [text(s, "einkauf.txt", (1.05, -0.37), FM),
          text(s, T(s, "b25", "25 Bytes", "25 bytes", "25 bytes", "25 字节", "25 octets", "25 bayt"), (1.05, -0.62), FM, "center",
               GRAU)]
    kr, zh_r, zm_r = uhr(s, 2.55, 0.55, 18, 30)
    alt = text(s, "Nov 9 18:30", (2.55, 0.08), FM)
    neu = text(s, jetzt, (2.55, 0.08), FM, "center", ORANGE)
    l_r = text(s, l_aend, (2.55, -0.17), FM, "center", GRAU)
    bleibt = text(s, T(s, "bleibt", "Inhalt bleibt", "contents unchanged", "el contenido no cambia", "内容不变", "contenu inchangé",
                       "içerik aynı kalır"), (1.05, -0.92), FM, "center", GRUEN)
    schritt(s, EIN([t_l, t_r, trenn], 0.5))
    schritt(s, EIN(cmd_l, 0.5))
    schritt(s, WACHS(doc_l, 0.6), EIN(nl, 0.6))
    schritt(s, EIN(ul + zl, 0.6))
    schritt(s, EIN(neu_l, 0.5))
    s.pause(0.6)
    schritt(s, WACHS(doc_r, 0.7), EIN(inhalt + nr + [kr, zh_r, zm_r, alt, l_r], 0.7))
    s.pause(0.4)
    schritt(s, EIN(cmd_r, 0.5))
    schritt(s, DREH(zm_r, -426, (2.55, 0.55), 1.2), DREH(zh_r, -245.5, (2.55, 0.55), 1.2))
    schritt(s, AUS(alt, 0.3), EIN(neu, 0.3))
    schritt(s, EIN(bleibt, 0.6), BETONE(inhalt, 0.7))
    s.speichern()


def k3nano():
    """Schema des nano-Fensters; ^O leuchtet, Statuszeile [ Wrote 4 lines ], der Stern verschwindet; dann ^X."""
    s = Szene("linux/k3nano")
    L, R, O, U = -3.4, 1.5, 1.7, -1.55
    fenster = s.box("", ((L + R) / 2, (O + U) / 2), breite=R - L, hoehe=O - U, form="rect", farbe=GRAU, fuellung=TERM, dicke=2)
    balken = flaeche(s, L, O - 0.24, R, O, DUNKEL)
    yt = O - 0.12
    t_nano = text(s, "GNU nano 8.7.1", (L + 0.12, yt), FM, "left", WEISS)
    t_stern = text(s, "einkauf.txt *", (-0.7, yt), FM, "center", WEISS)
    t_name = text(s, "einkauf.txt", (-0.7, yt), FM, "center", WEISS)
    zeilen = [text(s, w, (L + 0.12, y), FK, "left") for w, y in zip(("Milch", "Brot", "Äpfel", "Kaffee"), (1.28, 1.04, 0.8, 0.56))]
    cursor = flaeche(s, L + 0.1, 0.24, L + 0.2, 0.4, DUNKEL)
    ys_ = -0.75
    st_b = flaeche(s, -1.75, ys_ - 0.11, -0.15, ys_ + 0.11, DUNKEL)
    st_t = text(s, "[ Wrote 4 lines ]", (-0.95, ys_), FM, "center", WEISS)
    # in s.text: \^ = ^ (sonst hochgestellt), \backslash = \
    reihe1 = ["\\^G Help", "\\^O Write Out", "\\^F Where Is", "\\^K Cut", "\\^T Execute"]
    reihe2 = ["\\^X Exit", "\\^R Read File", "\\^\\backslash Replace", "\\^U Paste", "\\^J Justify"]
    y1, y2 = -1.07, -1.35
    xk = [L + 0.12 + 0.95 * k for k in range(5)]
    kuerzel = [text(s, t, (x, y1), FM, "left", DUNKEL) for t, x in zip(reihe1, xk)] + \
              [text(s, t, (x, y2), FM, "left", DUNKEL) for t, x in zip(reihe2, xk)]
    m_o = mark(s, xk[1] - 0.05, xk[1] + 0.9, y1, 0.22, ORANGE, 0.3)
    m_x = mark(s, xk[0] - 0.05, xk[0] + 0.62, y2, 0.22, ORANGE, 0.3)
    xa = R + 0.12
    anm = [text(s, T(s, "titel", "Titelzeile\n* = ungespeichert", "title bar\n* = unsaved", "barra de título\n* = sin guardar",
                     "标题栏\n* = 未保存", "barre de titre\n* = non enregistré", "başlık satırı\n* = kaydedilmedi"),
                (xa, yt - 0.06), FM, "left"),
           text(s, T(s, "textc", "Text mit Cursor", "text with cursor", "texto con el cursor", "带光标的文本",
                     "texte avec le curseur", "imleçli metin"), (xa, 0.9), FM, "left"),
           text(s, T(s, "status", "Statuszeile", "status bar", "línea de estado", "状态栏", "ligne d'état", "durum satırı"),
                (xa, ys_), FM, "left"),
           text(s, T(s, "kuerzel", "Tastenkürzel\n\\^ = Strg", "shortcuts\n\\^ = Ctrl", "atajos\n\\^ = Ctrl",
                     "快捷键\n\\^ = Ctrl", "raccourcis\n\\^ = Ctrl", "kısayollar\n\\^ = Ctrl"), (xa, (y1 + y2) / 2), FM, "left")]
    note = text(s, T(s, "nnote", "Strg+O speichert (den Namen mit der Eingabetaste bestätigen),\nStrg+X beendet nano.",
                     "Ctrl+O saves (confirm the name with Enter),\nCtrl+X quits nano.",
                     "Ctrl+O guarda (confirma el nombre con Intro),\nCtrl+X sale de nano.",
                     "Ctrl+O 保存（按回车确认文件名），\nCtrl+X 退出 nano。",
                     "Ctrl+O enregistre (valider le nom avec Entrée),\nCtrl+X quitte nano.",
                     "Ctrl+O kaydeder (adı Enter ile onayla),\nCtrl+X nano'dan çıkar."), (L, U - 0.32), FM, "left", GRAU)
    schritt(s, WACHS(fenster, 0.6), EIN([balken, t_nano, t_stern], 0.6))
    schritt(s, EIN(zeilen + [cursor], 0.6))
    schritt(s, EIN(kuerzel, 0.6))
    s.pause(0.4)
    for a in anm:
        schritt(s, EIN(a, 0.4))
    s.pause(0.6)
    schritt(s, EIN(m_o, 0.5), BETONE(kuerzel[1], 0.8))
    schritt(s, EIN([st_b, st_t], 0.6))
    schritt(s, AUS(t_stern, 0.4), EIN(t_name, 0.4))
    s.pause(0.6)
    schritt(s, EIN(m_x, 0.5), BETONE(kuerzel[5], 0.8))
    schritt(s, EIN(note, 0.6))
    s.speichern()


def k3einkauf():
    """Rechenbild: Bytes der Einkaufsliste zeilenweise (Wort + Zeilenende, Ä = 2 Bytes), Summe 25 wie bei wc."""
    s = Szene("linux/k3einkauf")
    tex = (r"\begin{aligned}"
           r"\mathtt{Milch} &:\; 5 + 1 = 6\\"
           r"\mathtt{Brot} &:\; 4 + 1 = 5\\"
           r"\mathtt{\ddot{A}pfel} &:\; 2 + 4 + 1 = 7\\"
           r"\mathtt{Kaffee} &:\; 6 + 1 = 7\\[4pt]"
           r"\texttt{einkauf.txt} &:\; 6 + 5 + 7 + 7 = 25"      # \texttt: kein Abstand nach dem Punkt (2b-2)
           r"\end{aligned}")
    s.formel(tex, mitte=(-1.1, 0.1), hoehe=1.55, zeilenweise=True, dauer=5.0)
    xa = 1.25
    l1 = text(s, T(s, "plus1", "+ 1: das Zeilenende", "+ 1: the line end", "+ 1: el fin de línea", "+ 1：换行符",
                   "+ 1 : la fin de ligne", "+ 1: satır sonu"), (xa, 0.72), FM, "left", ORANGE)
    l2 = text(s, T(s, "ae", "Ä belegt 2 Bytes", "Ä takes 2 bytes", "Ä ocupa 2 bytes", "Ä 占 2 个字节", "Ä occupe 2 octets",
                   "Ä 2 bayt tutar"), (xa, 0.12), FM, "left", ORANGE)
    l3 = text(s, T(s, "wiewc", "wie wc meldet", "as wc reports", "como indica wc", "与 wc 的结果相同", "comme l'indique wc",
                   "wc'nin bildirdiği gibi"), (xa, -0.55), FM, "left", GRAU)
    s.pause(0.6)
    schritt(s, EIN(l1, 0.5))
    schritt(s, EIN(l2, 0.5))
    schritt(s, EIN(l3, 0.5))
    s.speichern()


# ================================================================== Hälfte 2 (Phase 2b-2)
# Die Helfer haken, strich, zeilenbaum, dokument (= dokument_zeilen) und term_kasten stehen in linux_hilfen.py.
# Seit 10.11.2026 ändert s.umformen auf einen s.text Inhalt und Farbe (bequemer: s.ersetzen); die Szenen hier blenden
# Texte noch aus und ein (unverändert).


# ================================================================== Abschnitt 6: Kopieren, verschieben, löschen
def k3cp():
    """cp einkauf.txt einkauf_alt.txt: eine zweite Datei mit eigenem Inhalt; danach wird einkauf.txt geändert, die Kopie bleibt."""
    s = Szene("linux/k3cp")
    xl, xr, y, b, h = -1.65, 1.65, 0.2, 1.3, 1.5
    term = term_kasten(s, (0, 1.78), 3.6, 0.42)
    cmd = tt(s, "$ cp einkauf.txt einkauf_alt.txt", 0, 1.78, 0.18, SCHWARZ, "m")
    inhalt = ("Milch", "Brot", "Äpfel", "Kaffee")

    def dok(x):
        k = s.box("", (x, y), breite=b, hoehe=h, form="rect", farbe=SCHWARZ, fuellung=WEISS, dicke=2.5)
        return [k] + [text(s, w, (x - 0.45, y + 0.48 - 0.24 * i), FM, "left") for i, w in enumerate(inhalt)]

    links = dok(xl)
    kopie = dok(xl)
    n_l = text(s, "einkauf.txt", (xl, 1.15), FK)
    n_r = text(s, r"einkauf\_alt.txt", (xr, 1.15), FK)
    pfeil = pf(s, (xl + b / 2 + 0.08, y), (xr - b / 2 - 0.08, y), farbe=GRAU, dicke=2.5)
    l_cp = tt(s, "cp", 0, y + 0.2, 0.17, GRAU, "m")
    m_b = mark(s, xl - 0.6, xl + 0.6, y - 0.48, 0.21, ORANGE, 0.2)
    butter = text(s, "Butter", (xl - 0.45, y - 0.48), FM, "left", ORANGE)
    l_g = text(s, T(s, "geaendert", "danach geändert", "changed afterwards", "modificado después", "随后被修改", "modifié ensuite",
                    "sonra değiştirildi"), (xl, -0.8), FM, "center", ORANGE)
    l_b = text(s, T(s, "bleibt", "bleibt, wie sie war", "stays as it was", "se queda como estaba", "保持原样", "reste comme avant",
                    "olduğu gibi kalır"), (xr, -0.8), FM, "center", GRUEN)
    fazit = text(s, T(s, "eigen", "zwei eigenständige Dateien", "two independent files", "dos archivos independientes",
                      "两个独立的文件", "deux fichiers indépendants", "iki bağımsız dosya"), (0, -1.3), FK)
    schritt(s, WACHS(links[0], 0.6), EIN(links[1:] + [n_l], 0.6))
    s.pause(0.6)
    schritt(s, WACHS(term, 0.5), EIN(cmd, 0.5))
    schritt(s, EIN(kopie, 0.2))
    schritt(s, *[VER(i, xr - xl, 0, 1.2) for i in kopie], ZEICHNE(pfeil, 1.2))
    schritt(s, EIN([n_r, l_cp], 0.5))
    s.pause(0.6)
    schritt(s, EIN([m_b, butter], 0.6))
    schritt(s, EIN(l_g, 0.5))
    schritt(s, EIN(l_b, 0.5), BETONE(kopie[1:], 0.8))
    s.pause(0.4)
    schritt(s, EIN(fazit, 0.6))
    s.speichern()


def k3cpr():
    """cp -r rezepte sicherung zweimal: erst entsteht sicherung als Kopie, dann landet die Kopie als sicherung/rezepte darin."""
    s = Szene("linux/k3cpr")
    zeilen = [("rezepte", 0, "dir"), ("einkauf.txt", 1, "datei"), ("kuchen", 1, "dir"), ("suppen", 1, "dir")]
    x0, y0, dz, ez = -3.2, 0.85, 0.38, 0.34
    Z, _ = zeilenbaum(s, x0, y0, zeilen, dz, ez)
    term = term_kasten(s, (-1.95, 1.72), 2.7, 0.62)
    xt = -3.2
    z1 = tt(s, "$ cp -r rezepte sicherung", xt, 1.84, 0.17)
    z2 = tt(s, "$ cp -r rezepte sicherung", xt, 1.6, 0.17)
    n1 = [s.kreis(None, -0.42, 1.84, 0.1, GRUEN, 2.5, WEISS, 1.0), text(s, "1", (-0.42, 1.84), FM, "center", GRUEN)]
    n2 = [s.kreis(None, -0.42, 1.6, 0.1, ORANGE, 2.5, WEISS, 1.0), text(s, "2", (-0.42, 1.6), FM, "center", ORANGE)]
    dx1 = 3.5
    C1, _ = zeilenbaum(s, x0, y0, zeilen, dz, ez, textfarbe=GRUEN)
    xs = x0 + dx1
    n_sich = text(s, "sicherung", (xs + 0.2, y0), FK, "left", GRUEN)
    l1 = text(s, T(s, "mal1", "1. Mal: neu als Kopie", "1st time: new copy", "1.ª vez: copia nueva", "第 1 次：新建为副本",
                   "1re fois : nouvelle copie", "1. kez: yeni kopya"), (xs + 1.1, y0), FM, "left", GRUEN)
    dx2, dy2 = xs + ez - x0, -4 * dz
    C2, _ = zeilenbaum(s, x0, y0, zeilen, dz, ez, textfarbe=ORANGE)
    yr = y0 + dy2
    verb = [linie(s, (xs, y0 - 3 * dz), (xs, yr), GRAU, 2), linie(s, (xs, yr), (xs + ez - 0.14, yr), GRAU, 2)]
    l2 = text(s, T(s, "mal2", "2. Mal: landet darin,\nals sicherung/rezepte", "2nd time: lands inside,\nas sicherung/rezepte",
                   "2.ª vez: va dentro,\ncomo sicherung/rezepte", "第 2 次：放进里面，\n成为 sicherung/rezepte",
                   "2e fois : atterrit dedans,\nen sicherung/rezepte", "2. kez: içine gider,\nsicherung/rezepte olarak"),
              (xs + ez + 0.95, yr), FM, "left", ORANGE)
    schritt(s, EIN(flach(Z), 0.7), WACHS(term, 0.7))
    s.pause(0.6)
    schritt(s, EIN([z1] + n1, 0.5))
    schritt(s, EIN(flach(C1), 0.2))
    schritt(s, *[VER(i, dx1, 0, 1.2) for i in flach(C1)])
    schritt(s, AUS(C1[0][-1], 0.4), EIN(n_sich, 0.4))
    schritt(s, EIN(l1, 0.5))
    s.pause(0.6)
    schritt(s, EIN([z2] + n2, 0.5))
    schritt(s, EIN(flach(C2), 0.2))
    schritt(s, *[VER(i, dx2, dy2, 1.3) for i in flach(C2)])
    schritt(s, ZEICHNE(verb, 0.5), EIN(l2, 0.5))
    s.speichern()


def k3mv():
    """Zwei Verzeichnistabellen: Umbenennen ändert nur den Namen im Eintrag, Verschieben trägt den Eintrag in die andere Tabelle;
    die Daten der Datei bleiben unbewegt."""
    s = Szene("linux/k3mv")
    dz, b, LL, LR, y1 = 0.28, 2.5, -3.35, 0.85, 1.05
    term = term_kasten(s, (0, 1.98), 3.9, 0.56)
    z1 = tt(s, "$ mv einkauf_alt.txt einkauf_montag.txt", -1.64, 2.09, 0.16)
    z2 = tt(s, "$ mv einkauf_montag.txt sicherung", -1.64, 1.87, 0.16)
    ys = [y1 - i * dz for i in range(5)]
    oben, unten = y1 + 0.2, ys[-1] - 0.18

    def tabelle(L, titel, namen):
        r = s.box("", (L + b / 2, (oben + unten) / 2), breite=b, hoehe=oben - unten, form="rect", farbe=GRAU, fuellung=WEISS,
                  dicke=2)
        return [r, tt(s, titel, L + b / 2, oben + 0.17, 0.17, SCHWARZ, "m")], \
            [text(s, n, (L + 0.18, y), FK, "left") for n, y in zip(namen, ys)]

    tl, zl = tabelle(LL, "~/linuxk3", ["einkauf.txt", r"einkauf\_alt.txt", "fotos", "rezepte", "sicherung"])
    tr_, zr = tabelle(LR, "sicherung", ["einkauf.txt", "kuchen", "rezepte", "suppen"])
    daten = dokument(s, (0, -1.25), 1.55, 0.62, ["Milch, Brot,", "Äpfel, Kaffee"], dz=0.22)
    l_daten = text(s, T(s, "daten", "Daten bleiben, wo sie sind", "the data stay where they are", "los datos se quedan donde están",
                        "数据留在原处", "les données restent où elles sont", "veriler yerinde kalır"), (0, -1.78), FM, "center", GRUEN)
    p_alt = pf(s, (LL + b, ys[1]), (-0.3, -0.92), farbe=GRAU)
    p_neu = pf(s, (LR, ys[4]), (0.3, -0.92), farbe=ORANGE)
    m = mark(s, LL + 0.05, LL + b - 0.05, ys[1], 0.25, ORANGE, 0.2)
    t_mon = text(s, r"einkauf\_montag.txt", (LL + 0.18, ys[1]), FK, "left")
    l_um = text(s, T(s, "um", "Umbenennen:\nnur der Name ändert sich", "Renaming:\nonly the name changes", "Renombrar:\nsolo cambia el nombre",
                     "重命名：\n只有名称改变", "Renommer :\nseul le nom change", "Yeniden adlandırma:\nyalnızca ad değişir"),
                (LL + b / 2, -0.62), FM, "center", ORANGE)
    l_ver = text(s, T(s, "ver", "Verschieben:\nder Eintrag wandert", "Moving:\nthe entry moves", "Mover:\nla entrada se traslada",
                      "移动：\n条目换了位置", "Déplacer :\nl'entrée se déplace", "Taşıma:\ngirdi yer değiştirir"),
                 (LR + b / 2, -0.62), FM, "center", ORANGE)
    schritt(s, EIN(tl + zl + tr_ + zr, 0.7), WACHS(daten[0], 0.7), EIN(daten[1:], 0.7))
    schritt(s, ZEICHNE(p_alt, 0.6))
    s.pause(0.6)
    schritt(s, WACHS(term, 0.4), EIN(z1, 0.5))
    schritt(s, EIN(m, 0.5), AUS(zl[1], 0.5), EIN(t_mon, 0.5))
    schritt(s, EIN(l_um, 0.5))
    s.pause(0.6)
    schritt(s, EIN(z2, 0.5))
    schritt(s, AUS(p_alt, 0.4))
    schritt(s, VER(t_mon, LR - LL, ys[4] - ys[1], 1.2), VER(m, LR - LL, ys[4] - ys[1], 1.2),
            *[VER(t, 0, dz, 1.0) for t in zl[2:]])
    schritt(s, ZEICHNE(p_neu, 0.6), EIN(l_ver, 0.6))
    s.pause(0.4)
    schritt(s, EIN(l_daten, 0.6), BETONE(daten, 0.8))
    s.speichern()


def k3papierkorb():
    """Oben: Papierkorb einer Oberfläche = verschieben nach ~/.local/share/Trash/files (+ info), Rückweg möglich.
    Unten: rm streicht den Eintrag, kein Rückweg."""
    s = Szene("linux/k3papierkorb")
    trenn = linie(s, (-3.4, 0.0), (3.4, 0.0), HELLGRAU, 2, DASH)

    def haelfte(dy):
        box = s.box("", (-2.45, 0.95 + dy), breite=1.7, hoehe=0.75, form="rect", farbe=GRAU, fuellung=WEISS, dicke=2)
        kopf = tt(s, "~/linuxk3", -2.45, 1.48 + dy, 0.15, SCHWARZ, "m")
        eintrag = [datei_symbol(s, -3.05, 0.95 + dy), text(s, "einkauf.txt", (-2.87, 0.95 + dy), FK, "left")]
        return [box, kopf], eintrag

    t_o = text(s, T(s, "oben", "Papierkorb einer grafischen Oberfläche", "Trash of a graphical desktop", "Papelera de un escritorio gráfico",
                    "图形界面的回收站", "Corbeille d'un bureau graphique", "Grafik masaüstünün çöp kutusu"), (-3.35, 1.8), FK, "left")
    korb = s.box("", (1.5, 0.95), breite=2.2, hoehe=0.75, form="rect", farbe=GRUEN, fuellung=GRUEN_HELL, dicke=2)
    korb_t = tt(s, "~/.local/share/Trash/files", 1.5, 1.48, 0.14, SCHWARZ, "m")
    vo, eo = haelfte(0)
    hin = pf(s, (-1.52, 1.07), (0.33, 1.07), farbe=ORANGE)
    l_hin = text(s, T(s, "versch", "verschieben", "move", "mover", "移动", "déplacer", "taşı"), (-0.6, 1.27), FM, "center", ORANGE)
    zurueck = pf(s, (0.33, 0.8), (-1.52, 0.8), farbe=GRUEN, dash=DASH)
    l_zur = text(s, T(s, "zurueck", "zurückholen möglich", "can be restored", "se puede recuperar", "可以还原", "restauration possible",
                      "geri alınabilir"), (-0.6, 0.6), FM, "center", GRUEN)
    info = [datei_symbol(s, 0.55, 0.3),
            text(s, T(s, "info", "dazu ein Zettel in Trash/info:\nalter Pfad, Zeitpunkt",
                      "plus a note in Trash/info:\nold path, time", "más una nota en Trash/info:\nruta antigua, hora",
                      "另在 Trash/info 中记下：\n原路径、时间", "plus une note dans Trash/info :\nancien chemin, heure",
                      "ayrıca Trash/info içinde not:\neski yol, zaman"), (0.72, 0.3), FM, "left", GRAU)]
    dx = 0.65 - (-3.05)
    t_u = text(s, T(s, "unten", "rm an der Kommandozeile", "rm on the command line", "rm en la línea de comandos", "命令行中的 rm",
                    "rm en ligne de commande", "komut satırında rm"), (-3.35, -0.2), FK, "left")
    vu, eu = haelfte(-2.0)
    term = term_kasten(s, (1.5, -1.05), 2.2, 0.5)
    cmd = tt(s, "$ rm einkauf.txt", 1.5, -1.05, 0.17, SCHWARZ, "m")
    geist = [s.box("", (-2.45, -1.05), breite=1.5, hoehe=0.34, form="round", farbe=GRAU, fuellung=WEISS, dicke=2, dash=DASH),
             text(s, "einkauf.txt", (-2.45, -1.05), FK, "center", HELLGRAU)]
    l_weg = text(s, T(s, "weg", "Eintrag gestrichen", "entry removed", "entrada eliminada", "条目被删除", "entrée supprimée",
                      "girdi silindi"), (-2.45, -1.6), FM, "center", ROT)
    kein = pf(s, (0.33, -1.42), (-1.52, -1.42), farbe=ROT, dash=DASH)
    kreuz = s.kreuzchen(None, -0.6, -1.42, ROT, 0.22, 4)
    l_kein = text(s, T(s, "kein", "kein Weg zurück", "no way back", "no hay vuelta atrás", "无法恢复", "aucun retour possible",
                       "geri dönüş yok"), (-0.6, -1.72), FM, "center", ROT)
    schritt(s, WACHS(korb, 0.7), EIN([t_o] + vo + eo + [korb_t], 0.7))   # Reihenfolge = Zeichenreihenfolge
    s.pause(0.6)
    schritt(s, ZEICHNE(hin, 0.6), EIN(l_hin, 0.6))
    schritt(s, *[VER(i, dx, 0, 1.0) for i in eo])
    schritt(s, EIN(info, 0.5))
    schritt(s, ZEICHNE(zurueck, 0.6), EIN(l_zur, 0.6))
    s.pause(0.6)
    schritt(s, EIN([trenn, t_u] + vu + eu, 0.7), WACHS(term, 0.7), EIN(cmd, 0.7))
    schritt(s, AUS(eu, 0.6), EIN(geist, 0.6))
    schritt(s, EIN(l_weg, 0.4))
    schritt(s, ZEICHNE(kein, 0.6))
    schritt(s, EIN([kreuz, l_kein], 0.5))
    s.speichern()


def k3muster():
    """Sechs Namen aus fotos/urlaub/2026; die Muster *.jpg, strand_?.jpg und *_[12].jpg nacheinander: Treffer leuchten, der Rest graut aus;
    am Ende steht je Muster eine Spalte mit Häkchen."""
    s = Szene("linux/k3muster")
    namen = [r"berg\_1.jpg", r"berg\_2.jpg", "notiz.txt", r"strand\_1.jpg", r"strand\_10.jpg", r"strand\_2.jpg"]
    muster = ["*.jpg", "strand_?.jpg", "*_[12].jpg"]
    treffer = [{0, 1, 3, 4, 5}, {3, 5}, {0, 1, 3, 5}]
    ys = [0.9 - 0.33 * i for i in range(6)]
    xn, cx, yk = -3.3, [-1.2, 0.55, 2.3], 1.42
    kopf_l = tt(s, "fotos/urlaub/2026", xn, yk, 0.15)
    strich_k = linie(s, (-3.35, 1.2), (3.2, 1.2), HELLGRAU, 2)
    texte = [text(s, n, (xn, y), FK, "left") for n, y in zip(namen, ys)]
    kopf = [tt(s, m, x, yk, 0.18, BLAU, "m") for m, x in zip(muster, cx)]
    marks, schl, zeichen = [], [], []
    for j in range(3):
        marks.append([mark(s, -3.35, -2.1, ys[i], 0.27, GRUEN, 0.25) for i in sorted(treffer[j])])
        schl.append([schleier(s, (-2.72, ys[i]), 1.3, 0.27, 0.7) for i in range(6) if i not in treffer[j]])
        zeichen.append([haken(s, cx[j], ys[i]) if i in treffer[j] else strich(s, cx[j], ys[i]) for i in range(6)])
    yl = [-1.2, -1.5, -1.8]
    leg = [[tt(s, "*", xn, yl[0], 0.17, BLAU),
            text(s, T(s, "stern", "beliebig viele Zeichen, auch keins", "any number of characters, even none",
                      "cualquier número de caracteres, también ninguno", "任意多个字符，也可以没有",
                      "un nombre quelconque de caractères, même aucun", "istenen sayıda karakter, hiç olmayabilir de"),
                 (-2.65, yl[0]), FM, "left")],
           [tt(s, "?", xn, yl[1], 0.17, BLAU),
            text(s, T(s, "frage", "genau ein Zeichen", "exactly one character", "exactamente un carácter", "恰好一个字符",
                      "exactement un caractère", "tam olarak bir karakter"), (-2.65, yl[1]), FM, "left")],
           [tt(s, "[12]", xn, yl[2], 0.17, BLAU),
            text(s, T(s, "klammer", "eine 1 oder eine 2", "a 1 or a 2", "un 1 o un 2", "一个 1 或一个 2", "un 1 ou un 2",
                      "bir 1 ya da bir 2"), (-2.65, yl[2]), FM, "left")]]
    schritt(s, EIN([kopf_l, strich_k] + texte, 0.7))
    s.pause(0.6)
    for j in range(3):
        schritt(s, EIN([kopf[j]] + leg[j], 0.5))
        schritt(s, EIN(marks[j] + schl[j], 0.5))
        schritt(s, ZEICHNE(flach(zeichen[j]), 0.5))
        s.pause(0.5)
        schritt(s, AUS(marks[j] + schl[j], 0.4))
    s.speichern()


# ================================================================== Abschnitt 7: Verzeichnisstruktur
def k3fhs():
    """Die oberste Ebene unter /, nach Zweck in sieben farbige Gruppen; jede Gruppe erscheint mit ihrer Beschriftung."""
    s = Szene("linux/k3fhs")
    G = [  # Verzeichnisse, Füllung, Rand, Mitte x, Mitte y, Breite, Schlüssel und Texte
        (["usr", "opt"], BLAU_HELL, BLAU, -2.575, 0.6, 1.55,
         ("prog", "Programme,\nBibliotheken", "Programs,\nlibraries", "Programas,\nbibliotecas", "程序和库", "Programmes,\nbibliothèques",
          "Programlar,\nkütüphaneler")),
        (["etc"], ORANGE_HELL, ORANGE, -0.86, 0.6, 1.55,
         ("einst", "Einstellungen", "Settings", "Configuración", "配置", "Configuration", "Ayarlar")),
        (["home", "root"], GRUEN_HELL, GRUEN, 0.855, 0.6, 1.55,
         ("benutzer", "Benutzer", "Users", "Usuarios", "用户", "Utilisateurs", "Kullanıcılar")),
        (["var", "tmp"], "#fff4cc", "#c99a00", 2.57, 0.6, 1.55,
         ("var", "veränderliche\nDaten", "Variable\ndata", "Datos\nvariables", "可变数据", "Données\nvariables", "Değişken\nveriler")),
        (["boot"], GRAU_HELL, GRAU, -2.295, -0.6, 1.55,
         ("start", "Start", "Boot", "Arranque", "启动", "Démarrage", "Önyükleme")),
        (["mnt", "media"], "#e2f3f5", "#2a8f9b", -0.475, -0.6, 1.75,
         ("einh", "Einhängepunkte", "Mount points", "Puntos de montaje", "挂载点", "Points de montage", "Bağlama noktaları")),
        (["dev", "proc", "sys", "run"], "#f8e3e3", ROT, 1.82, -0.6, 2.5,
         ("kernel", "vom Kernel erzeugt", "Created by the kernel", "Creados por el kernel", "由内核生成", "Créés par le noyau",
          "Çekirdek tarafından üretilir")),
    ]
    rahmen_ = s.box("", (0, 0.03), breite=6.85, hoehe=2.55, form="round", farbe=HELLGRAU, fuellung=WEISS, dicke=2, dash=DASH)
    wurzel = knoten(s, "/", 0.0, 1.3)
    l_w = text(s, T(s, "oben", "Verzeichnisse direkt unter /", "directories directly under /", "directorios justo bajo /",
                    "/ 下的第一层目录", "répertoires juste sous /", "/ altındaki ilk dizinler"), (0.4, 1.55), FM, "left", GRAU)
    gruppen = []
    for namen, fu, ra, x, y, b, tx in G:
        box = s.box("", (x, y), breite=b, hoehe=0.95, form="round", farbe=ra, fuellung=fu, dicke=2.5)
        breiten = [kb(n) for n in namen]
        x0 = x - (sum(breiten) + 0.08 * (len(namen) - 1)) / 2
        teile = []
        for n, w in zip(namen, breiten):
            teile += [s.box("", (x0 + w / 2, y + 0.22), breite=w, hoehe=KH, form="round", farbe=ra, fuellung=WEISS, dicke=2),
                      text(s, n, (x0 + w / 2, y + 0.22), FK)]
            x0 += w + 0.08
        teile.append(text(s, T(s, *tx), (x, y - 0.22), FM, "center", DUNKEL))
        gruppen.append((box, teile))
    schritt(s, ZEICHNE(rahmen_, 0.7), WACHS(wurzel[0], 0.7), EIN([wurzel[1], l_w], 0.7))
    s.pause(0.6)
    for box, teile in gruppen:
        schritt(s, WACHS(box, 0.6), EIN(teile, 0.6))
        s.pause(0.25)
    s.speichern()


def k3dev():
    """Drei Türen /dev/zero, /dev/urandom, /dev/sdd; od liest durch sie hindurch, dahinter antwortet je ein Treiber im Kernel."""
    s = Szene("linux/k3dev")
    cx = [-2.3, 0.0, 2.3]
    band = flaeche(s, -3.4, -1.9, 3.4, -0.3, GRAU_HELL)
    l_k = text(s, T(s, "kernel", "Kernel", "kernel", "kernel", "内核", "noyau", "çekirdek"), (-3.3, -1.72), FK, "left", GRAU)
    od = s.box("", (0, 1.82), breite=2.1, hoehe=0.42, form="round", farbe=BLAU, fuellung=BLAU_HELL, dicke=2.5)
    od_t = text(s, T(s, "prog", "Programm od", "program od", "programa od", "程序 od", "programme od", "od programı"), (0, 1.82), FK)
    l_wie = text(s, T(s, "wie", "liest wie aus einer Datei", "reads as from a file", "lee como de un archivo", "像读文件一样读取",
                      "lit comme dans un fichier", "dosyadan okur gibi okur"), (1.2, 1.82), FM, "left", GRAU)
    unten = [pf(s, (x, -0.53), (x, 0.23), farbe=ORANGE, dicke=3) for x in cx]
    oben = [pf(s, (x, 1.07), (0.3 * x, 1.6), farbe=ORANGE, dicke=3) for x in cx]
    tueren, pfade = [], []
    for x, p in zip(cx, ["/dev/zero", "/dev/urandom", "/dev/sdd"]):
        tueren += [s.box("", (x, 0.65), breite=0.55, hoehe=0.8, form="rect", farbe="#9a6b3a", fuellung="#f3e2c7", dicke=2.5),
                   s.kreis(None, x + 0.16, 0.62, 0.045, "#9a6b3a", 2, "#9a6b3a", 1.0)]
        pfade.append(tt(s, p, x - 0.38, 0.65, 0.15, SCHWARZ, "r"))
    treiber_t = [("t0", "Treiber:\nliefert Nullen", "driver:\nsupplies zeros", "controlador:\nentrega ceros", "驱动程序：\n提供零",
                  "pilote :\nfournit des zéros", "sürücü:\nsıfır verir"),
                 ("t1", "Treiber:\nliefert Zufallszahlen", "driver:\nsupplies random numbers", "controlador:\nnúmeros aleatorios",
                  "驱动程序：\n提供随机数", "pilote :\nnombres aléatoires", "sürücü:\nrastgele sayılar"),
                 ("t2", "Treiber:\nliest die Sektoren", "driver:\nreads the sectors", "controlador:\nlee los sectores", "驱动程序：\n读取扇区",
                  "pilote :\nlit les secteurs", "sürücü:\nsektörleri okur")]
    treiber = [(s.box("", (x, -0.85), breite=2.05, hoehe=0.62, form="round", farbe=GRAU, fuellung=WEISS, dicke=2),
                text(s, T(s, *t), (x, -0.85), FM)) for x, t in zip(cx, treiber_t)]
    daten = [tt(s, "0 0 0 0 0 0 0 0", cx[0] + 0.1, -0.12, 0.14, ORANGE),
             tt(s, "14 237 103 241 ...", cx[1] + 0.1, -0.12, 0.14, ORANGE),
             text(s, T(s, "sekt", "Sektoren", "sectors", "sectores", "扇区", "secteurs", "sektörler"), (cx[2] + 0.1, -0.12), FM,
                  "left", ORANGE)]
    note = text(s, T(s, "note", "hinter der Tür: kein gespeicherter Inhalt, sondern ein Treiber",
                     "behind the door: no stored contents, but a driver", "tras la puerta: ningún contenido guardado, sino un controlador",
                     "门后没有存储的内容，而是一个驱动程序", "derrière la porte : aucun contenu stocké, mais un pilote",
                     "kapının ardında saklı içerik yok, bir sürücü var"), (0.35, -1.5), FM, "center", DUNKEL)
    schritt(s, WACHS(od, 0.7), EIN([od_t] + pfade, 0.7), WACHS(tueren, 0.7))
    schritt(s, EIN(l_wie, 0.5))
    s.pause(0.6)
    schritt(s, EIN([band, l_k], 0.6))
    for i in range(3):
        schritt(s, WACHS(treiber[i][0], 0.5), EIN(treiber[i][1], 0.5))
        schritt(s, ZEICHNE([unten[i], oben[i]], 0.6))
        schritt(s, EIN(daten[i], 0.4))
    s.pause(0.6)
    schritt(s, EIN(note, 0.6))
    s.speichern()


def k3proc():
    """cat /proc/uptime fragt den Kernel; der erzeugt „46.54 642.08“ in diesem Moment und reicht es zurück; kein Datenträger beteiligt."""
    s = Szene("linux/k3proc")
    term = term_kasten(s, (-1.75, 1.45), 3.2, 0.78)
    z1 = tt(s, "$ cat /proc/uptime", -3.2, 1.6, 0.17)
    kern = s.box("", (1.95, -0.05), breite=2.6, hoehe=1.35, form="round", farbe=BLAU, fuellung=BLAU_HELL, dicke=2.5)
    k_t = text(s, T(s, "kernel", "Kernel", "kernel", "kernel", "内核", "noyau", "çekirdek"), (1.95, 0.4), FS, "center", BLAU)
    u = list(uhr(s, 1.05, -0.15, 2, 42, r=0.24))
    gen = tt(s, "46.54 642.08", 2.3, -0.15, 0.17, ORANGE, "m")
    kopie = tt(s, "46.54 642.08", 2.3, -0.15, 0.17, ORANGE, "m")
    l_gen = text(s, T(s, "erzeugt", "erzeugt die Zeile beim Lesen", "creates the line when it is read", "crea la línea al leerla",
                      "读取时才生成这一行", "crée la ligne au moment de la lecture", "satırı okuma anında üretir"), (1.95, -0.52), FM)
    anfrage = pf(s, (-0.1, 1.42), (1.25, 0.66), farbe=GRAU)
    l_anf = text(s, T(s, "anfrage", "Anfrage", "request", "petición", "请求", "requête", "istek"), (0.72, 1.22), FM, "left", GRAU)
    antwort = pf(s, (0.62, -0.05), (-1.0, 1.02), farbe=ORANGE)
    l_antw = text(s, T(s, "antwort", "Antwort", "answer", "respuesta", "回答", "réponse", "yanıt"), (-0.35, 0.42), FM, "right", ORANGE)
    disk = s.box("", (-2.1, -0.75), breite=1.6, hoehe=0.55, form="round", farbe=GRAU, fuellung=GRAU_HELL, dicke=2)
    disk_t = text(s, T(s, "disk", "Datenträger", "storage device", "disco", "存储设备", "support de données", "depolama aygıtı"),
                  (-2.1, -0.75), FM)
    kreuz = s.kreuzchen(None, -1.08, -0.75, ROT, 0.3, 4)
    l_disk = text(s, T(s, "nirgends", "/proc/uptime liegt auf\nkeinem Datenträger", "/proc/uptime is on\nno storage device",
                       "/proc/uptime no está\nen ningún disco", "/proc/uptime 不在\n任何存储设备上", "/proc/uptime ne se trouve\nsur aucun support",
                       "/proc/uptime hiçbir\naygıtta durmaz"), (-2.1, -1.32), FM, "center", ROT)
    schritt(s, WACHS([term, kern], 0.7), EIN(k_t, 0.7))
    s.pause(0.6)
    schritt(s, EIN(z1, 0.5))
    schritt(s, ZEICHNE(anfrage, 0.7), EIN(l_anf, 0.7))
    schritt(s, EIN(u, 0.4))
    schritt(s, EIN(gen, 0.5))
    schritt(s, EIN(l_gen, 0.5), BETONE(gen, 0.8))
    s.pause(0.4)
    schritt(s, ZEICHNE(antwort, 0.7), EIN(l_antw, 0.7))
    schritt(s, EIN(kopie, 0.2))
    schritt(s, ZU(kopie, -3.2 + 6 * cw(0.17), 1.33, 1.0))
    s.pause(0.6)
    schritt(s, WACHS(disk, 0.6), EIN(disk_t, 0.6))
    schritt(s, ZEICHNE(kreuz, 0.5), EIN(l_disk, 0.5))
    s.speichern()


# ================================================================== Abschnitt 8: Inode und Links
def k3inode():
    """Eintrag einkauf.txt → 95361, Inode-Kasten mit allen Angaben außer dem Namen, Datenblöcke; Pfeile nacheinander."""
    s = Szene("linux/k3inode")
    L, R = -3.4, -1.5
    tab = s.box("", ((L + R) / 2, 0.35), breite=R - L, hoehe=1.3, form="rect", farbe=GRAU, fuellung=WEISS, dicke=2)
    tab_t = text(s, T(s, "verz", "Verzeichnis linuxk3", "directory linuxk3", "directorio linuxk3", "目录 linuxk3", "répertoire linuxk3",
                      "linuxk3 dizini"), ((L + R) / 2, 1.22), FK)
    kopf = [text(s, T(s, "name", "Name", "name", "nombre", "名称", "nom", "ad"), (L + 0.15, 0.85), FM, "left", GRAU),
            text(s, T(s, "nummer", "Nummer", "number", "número", "编号", "numéro", "numara"), (R - 0.1, 0.85), FM, "right", GRAU),
            linie(s, (L, 0.72), (R, 0.72), GRAU, 2)]
    zeilen = [text(s, "…", (L + 0.15, 0.5), FM, "left", GRAU), text(s, "einkauf.txt", (L + 0.15, 0.2), FK, "left"),
              text(s, "95361", (R - 0.1, 0.2), FK, "right", ORANGE), text(s, "…", (L + 0.15, -0.1), FM, "left", GRAU)]
    p1 = pf(s, (R, 0.2), (-0.77, 0.2), farbe=ORANGE)
    ino = s.box("", (0.25, 0.35), breite=2.0, hoehe=2.2, form="round", farbe=BLAU, fuellung=BLAU_HELL, dicke=2.5)
    ino_t = text(s, T(s, "ititel", "Inode 95361", "inode 95361", "inodo 95361", "inode 95361", "inode 95361", "inode 95361"),
                 (0.25, 1.22), FK, "center", BLAU)
    angaben = [("art", "Art: gewöhnliche Datei", "type: regular file", "tipo: archivo regular", "类型：普通文件", "type : fichier ordinaire",
                "tür: normal dosya"),
               ("rechte", "Rechte: rw-r--r--", "permissions: rw-r--r--", "permisos: rw-r--r--", "权限：rw-r--r--", "droits : rw-r--r--",
                "izinler: rw-r--r--"),
               ("besitzer", "Besitzer: student", "owner: student", "propietario: student", "所有者：student", "propriétaire : student",
                "sahip: student"),
               ("groesse", "Größe: 25 Bytes", "size: 25 bytes", "tamaño: 25 bytes", "大小：25 字节", "taille : 25 octets", "boyut: 25 bayt"),
               ("zeiten", "Zeitstempel", "timestamps", "marcas de tiempo", "时间戳", "horodatages", "zaman damgaları"),
               ("links", "Links: 1", "links: 1", "enlaces: 1", "链接数：1", "liens : 1", "bağlantı: 1"),
               ("lage", "Lage der Blöcke", "location of the blocks", "ubicación de los bloques", "数据块的位置", "emplacement des blocs",
                "blokların yeri")]
    zl = [text(s, T(s, *a), (-0.6, 0.95 - 0.23 * i), FM, "left") for i, a in enumerate(angaben)]
    xb = 2.62
    bloecke = [s.box("", (xb, 0.95), breite=1.3, hoehe=0.4, form="rect", farbe=GRAU, fuellung=GRAU_HELL, dicke=2),
               s.box("", (xb, 0.25), breite=1.3, hoehe=0.95, form="rect", farbe=ORANGE, fuellung=ORANGE_HELL, dicke=2.5),
               s.box("", (xb, -0.47), breite=1.3, hoehe=0.4, form="rect", farbe=GRAU, fuellung=GRAU_HELL, dicke=2)]
    inhalt = [text(s, w, (xb - 0.5, 0.58 - 0.22 * i), FM, "left") for i, w in enumerate(("Milch", "Brot", "Äpfel", "Kaffee"))]
    l_b = text(s, T(s, "bloecke", "Datenblöcke", "data blocks", "bloques de datos", "数据块", "blocs de données", "veri blokları"),
               (xb, -0.9), FM, "center", GRAU)
    p2 = pf(s, (1.25, -0.43), (xb - 0.67, 0.05), farbe=ORANGE)
    note = text(s, T(s, "note", "Der Name steht nur im Verzeichnis, nicht in der Inode.",
                     "The name is only in the directory, not in the inode.", "El nombre solo está en el directorio, no en el inodo.",
                     "名称只在目录里，不在 inode 中。", "Le nom n'est que dans le répertoire, pas dans l'inode.",
                     "Ad yalnızca dizinde durur, inode'da değil."), (0, -1.3), FM, "center", DUNKEL)
    schritt(s, WACHS(tab, 0.7), EIN([tab_t] + kopf + zeilen, 0.7))
    s.pause(0.6)
    schritt(s, BETONE(zeilen[1:3], 0.7))
    schritt(s, ZEICHNE(p1, 0.6))
    schritt(s, WACHS(ino, 0.6), EIN(ino_t, 0.6))
    schritt(s, EIN(zl, 0.8))
    s.pause(0.6)
    schritt(s, ZEICHNE(p2, 0.6))
    schritt(s, WACHS(bloecke, 0.6), EIN(inhalt + [l_b], 0.6))
    s.pause(0.6)
    schritt(s, EIN(note, 0.6))
    s.speichern()


def k3tabelle():
    """Das Verzeichnis rezepte als Tabelle Name → Inode-Nummer; . zeigt auf die eigene Inode, .. nach oben, kuchen und suppen nach unten."""
    s = Szene("linux/k3tabelle")
    L, R, top, bot = -3.35, -0.85, 1.15, -0.75
    ys = [0.55, 0.2, -0.15, -0.5]
    tab = s.box("", ((L + R) / 2, (top + bot) / 2), breite=R - L, hoehe=top - bot, form="rect", farbe=GRAU, fuellung=WEISS, dicke=2)
    kopf = [text(s, T(s, "name", "Name", "name", "nombre", "名称", "nom", "ad"), (L + 0.15, 0.93), FM, "left", GRAU),
            text(s, T(s, "nummer", "Inode-Nummer", "inode number", "número de inodo", "inode 编号", "numéro d'inode", "inode numarası"),
                 (R - 0.12, 0.93), FM, "right", GRAU),
            linie(s, (L, 0.79), (R, 0.79), GRAU, 2)]
    namen = [tt(s, ".", L + 0.2, ys[0], 0.22), tt(s, "..", L + 0.2, ys[1], 0.22),
             text(s, "kuchen", (L + 0.15, ys[2]), FK, "left"), text(s, "suppen", (L + 0.15, ys[3]), FK, "left")]
    nummern = [text(s, n, (R - 0.12, y), FK, "right") for n, y in zip(("95355", "95352", "95359", "95360"), ys)]

    def ibox(x, y, nr, farbe=BLAU):
        return [s.box("", (x, y), breite=1.1, hoehe=0.36, form="round", farbe=farbe, fuellung=BLAU_HELL, dicke=2.5),
                text(s, nr, (x, y), FK)]

    i_self = ibox(-1.9, 1.75, "95355", ORANGE)
    l_self = text(s, "rezepte", (-2.55, 1.75), FK, "right")
    verb = linie(s, (-2.2, 1.57), (-2.2, top), GRAU, 2, DASH)
    l_inh = text(s, T(s, "inhalt", "Inhalt", "contents", "contenido", "内容", "contenu", "içerik"), (-2.3, 1.36), FM, "right", GRAU)
    punkt = [linie(s, (R, ys[0]), (-0.65, ys[0]), ORANGE, 3), linie(s, (-0.65, ys[0]), (-0.65, 1.75), ORANGE, 3),
             pf(s, (-0.65, 1.75), (-1.33, 1.75), farbe=ORANGE, dicke=3)]
    l_eigen = text(s, T(s, "eigen", "eigene Nummer", "own number", "número propio", "自己的编号", "son propre numéro", "kendi numarası"),
                   (-0.75, 1.36), FM, "right", ORANGE)
    i_par = ibox(1.0, 1.75, "95352")
    l_par = text(s, T(s, "par", "linuxk3 (übergeordnet)", "linuxk3 (parent)", "linuxk3 (padre)", "linuxk3（上级）", "linuxk3 (parent)",
                      "linuxk3 (üst dizin)"), (1.65, 1.75), FM, "left", BLAU)
    p_par = pf(s, (R, ys[1]), (0.43, 1.75), farbe=BLAU, dicke=3)
    i_k, i_s = ibox(1.0, -0.2, "95359", GRUEN), ibox(1.0, -0.9, "95360", GRUEN)
    l_k, l_s = text(s, "kuchen", (1.65, -0.2), FM, "left", GRUEN), text(s, "suppen", (1.65, -0.9), FM, "left", GRUEN)
    p_k, p_s = pf(s, (R, ys[2]), (0.43, -0.2), farbe=GRUEN, dicke=3), pf(s, (R, ys[3]), (0.43, -0.9), farbe=GRUEN, dicke=3)
    schritt(s, WACHS(tab, 0.7), EIN(kopf + namen + nummern, 0.7))
    s.pause(0.6)
    schritt(s, WACHS(i_self[0], 0.6), EIN([i_self[1], l_self, l_inh], 0.6), ZEICHNE(verb, 0.6))
    s.pause(0.6)
    schritt(s, BETONE(namen[0], 0.6))
    schritt(s, ZEICHNE(punkt, 0.8), EIN(l_eigen, 0.8))
    s.pause(0.4)
    schritt(s, BETONE(namen[1], 0.6))
    schritt(s, ZEICHNE(p_par, 0.7), WACHS(i_par[0], 0.7), EIN([i_par[1], l_par], 0.7))
    s.pause(0.4)
    schritt(s, ZEICHNE([p_k, p_s], 0.7), WACHS([i_k[0], i_s[0]], 0.7), EIN([i_k[1], i_s[1], l_k, l_s], 0.7))
    s.speichern()


def k3hartlink():
    """ln einkauf.txt liste.txt: zweiter Eintrag auf dieselbe Inode, Linkzähler 1 → 2; rm einkauf.txt: erster Eintrag weg, 2 → 1, Daten bleiben."""
    s = Szene("linux/k3hartlink")
    term = term_kasten(s, (-1.85, 1.75), 3.1, 0.6)
    z1 = tt(s, "$ ln einkauf.txt liste.txt", -3.3, 1.87, 0.17)
    z2 = tt(s, "$ rm einkauf.txt", -3.3, 1.63, 0.17)
    L, R, y1, y2 = -3.4, -1.15, 0.5, 0.15
    tab = s.box("", ((L + R) / 2, 0.45), breite=R - L, hoehe=1.1, form="rect", farbe=GRAU, fuellung=WEISS, dicke=2)
    tab_t = tt(s, "~/linuxk3", (L + R) / 2, 1.17, 0.15, SCHWARZ, "m")
    kopf = [text(s, T(s, "name", "Name", "name", "nombre", "名称", "nom", "ad"), (L + 0.12, 0.85), FM, "left", GRAU),
            text(s, T(s, "nummer", "Nummer", "number", "número", "编号", "numéro", "numara"), (R - 0.1, 0.85), FM, "right", GRAU),
            linie(s, (L, 0.73), (R, 0.73), GRAU, 2)]
    r1 = [text(s, "einkauf.txt", (L + 0.12, y1), FK, "left"), text(s, "95361", (R - 0.1, y1), FK, "right")]
    m2 = mark(s, L + 0.04, R - 0.04, y2, 0.27, GRUEN, 0.2)
    r2 = [text(s, "liste.txt", (L + 0.12, y2), FK, "left"), text(s, "95361", (R - 0.1, y2), FK, "right")]
    schl = schleier(s, ((L + R) / 2, y1), R - L - 0.08, 0.27, 0.6)
    weg = linie(s, (L + 0.08, y1), (R - 0.08, y1), ROT, 3)
    a1 = pf(s, (R, y1), (-0.32, 0.45), farbe=GRAU)
    a2 = pf(s, (R, y2), (-0.32, 0.25), farbe=GRUEN)
    ino = s.box("", (0.55, 0.35), breite=1.75, hoehe=1.15, form="round", farbe=BLAU, fuellung=BLAU_HELL, dicke=2.5)
    ino_t = text(s, T(s, "ititel", "Inode 95361", "inode 95361", "inodo 95361", "inode 95361", "inode 95361", "inode 95361"),
                 (0.55, 0.7), FK, "center", BLAU)
    zaehler = [text(s, T(s, k, f"Links: {n}", f"links: {n}", f"enlaces: {n}", f"链接数：{n}", f"liens : {n}", f"bağlantı: {n}"),
                    (0.55, 0.3), FS, "center", ORANGE) for k, n in (("l1", 1), ("l2", 2), ("l1", 1))]
    a3 = pf(s, (1.43, 0.35), (1.93, 0.35), farbe=GRAU)
    daten = dokument(s, (2.6, 0.35), 1.3, 1.15, ["Milch", "Brot", "Äpfel", "Kaffee"])
    l_d = text(s, T(s, "daten", "Daten", "data", "datos", "数据", "données", "veri"), (2.6, 1.1), FM, "center", GRAU)
    l_ln = text(s, T(s, "zweiter", "zweiter Name, gleiche Inode", "second name, same inode", "segundo nombre, mismo inodo",
                     "第二个名称，同一个 inode", "deuxième nom, même inode", "ikinci ad, aynı inode"), ((L + R) / 2, -0.36), FM, "center",
                GRUEN)
    l_rm = text(s, T(s, "weg", "einkauf.txt: Eintrag entfernt", "einkauf.txt: entry removed", "einkauf.txt: entrada eliminada",
                     "einkauf.txt：条目已删除", "einkauf.txt : entrée supprimée", "einkauf.txt: girdi kaldırıldı"), ((L + R) / 2, -0.66),
                FM, "center", ROT)
    note = text(s, T(s, "bleiben", "Daten bleiben: ein Name ist noch übrig", "data stay: one name is left",
                     "los datos se quedan: aún queda un nombre", "数据还在：还剩一个名称", "les données restent : il reste un nom",
                     "veri kalır: bir ad hâlâ var"), (1.45, -0.6), FM, "center", GRUEN)
    schritt(s, WACHS([tab, term], 0.8), EIN([tab_t] + kopf + r1, 0.8))
    schritt(s, ZEICHNE(a1, 0.6), WACHS(ino, 0.6), EIN([ino_t, zaehler[0]], 0.6))
    schritt(s, ZEICHNE(a3, 0.5), WACHS(daten[0], 0.5), EIN(daten[1:] + [l_d], 0.5))
    s.pause(0.6)
    schritt(s, EIN(z1, 0.5))
    schritt(s, EIN([m2] + r2, 0.6))
    schritt(s, ZEICHNE(a2, 0.5))
    schritt(s, AUS(zaehler[0], 0.4), EIN(zaehler[1], 0.4))
    schritt(s, BETONE(zaehler[1], 0.6), EIN(l_ln, 0.6))
    s.pause(0.6)
    schritt(s, EIN(z2, 0.5))
    schritt(s, AUS(a1, 0.5), EIN(schl, 0.5), ZEICHNE(weg, 0.5))
    schritt(s, EIN(l_rm, 0.4))
    schritt(s, AUS(zaehler[1], 0.4), EIN(zaehler[2], 0.4))
    schritt(s, BETONE(zaehler[2], 0.6))
    schritt(s, EIN(note, 0.6), BETONE(daten[1:], 0.8))
    s.speichern()


def k3symlink():
    """Oben: zettel.txt mit dem Inhalt „einkauf.txt“ leitet cat zur Einkaufsliste um. Unten: das Ziel ist gelöscht, der Pfad bleibt, der Link
    führt ins Leere."""
    s = Szene("linux/k3symlink")
    xz, xe, yA, yB = -1.55, 2.0, 0.75, -1.15

    def zettel(y):
        return [s.box("", (xz, y), breite=1.35, hoehe=0.55, form="rect", farbe=BLAU, fuellung=BLAU_HELL, dicke=2.5),
                tt(s, "einkauf.txt", xz, y, 0.16, SCHWARZ, "m")]

    t_a = text(s, T(s, "da", "Ziel\nvorhanden", "target\nexists", "destino\nexiste", "目标\n存在", "cible\nprésente", "hedef\nmevcut"),
               (-3.35, yA), FM, "left", GRAU)
    t_b = text(s, T(s, "geloescht", "Ziel\ngelöscht", "target\ndeleted", "destino\nborrado", "目标\n已删除", "cible\nsupprimée",
                    "hedef\nsilindi"), (-3.35, yB), FM, "left", GRAU)
    trenn = linie(s, (-3.4, -0.2), (3.4, -0.2), HELLGRAU, 2, DASH)
    ziel = dokument(s, (xe, yA), 1.3, 1.15, ["Milch", "Brot", "Äpfel", "Kaffee", "Butter"], dz=0.2)
    l_ziel = text(s, "einkauf.txt", (xe, yA + 0.78), FK)
    za = zettel(yA)
    l_za = text(s, T(s, "link", "zettel.txt: Link, 11 Bytes", "zettel.txt: link, 11 bytes", "zettel.txt: enlace, 11 bytes",
                     "zettel.txt：链接，11 字节", "zettel.txt : lien, 11 octets", "zettel.txt: bağlantı, 11 bayt"), (xz, yA - 0.48), FM,
                "center", BLAU)
    cat = tt(s, "$ cat zettel.txt", xz, yA + 0.85, 0.16, SCHWARZ, "m")
    p_cat = pf(s, (xz, yA + 0.72), (xz, yA + 0.3), farbe=GRAU)
    um = pf(s, (xz + 0.7, yA), (xe - 0.68, yA), farbe=ORANGE, dicke=3)
    l_um = text(s, T(s, "um", "umgeleitet", "redirected", "redirigido", "被转向", "redirigé", "yönlendirildi"),
                ((xz + xe) / 2 + 0.05, yA + 0.2), FM, "center", ORANGE)
    zb = zettel(yA)
    geist = s.box("", (xe, yB), breite=1.3, hoehe=1.15, form="rect", farbe=GRAU, fuellung=WEISS, dicke=2, dash=DASH)
    l_geist = text(s, T(s, "geist", "einkauf.txt (gelöscht)", "einkauf.txt (deleted)", "einkauf.txt (borrado)", "einkauf.txt（已删除）",
                        "einkauf.txt (supprimé)", "einkauf.txt (silindi)"), (xe, yB + 0.78), FM, "center", GRAU)
    leer = pf(s, (xz + 0.7, yB), (xe - 0.68, yB), farbe=GRAU, dash=DASH)
    kreuz = s.kreuzchen(None, xe, yB, ROT, 0.4, 4)
    l_leer = text(s, T(s, "leer", "führt ins Leere", "leads nowhere", "no lleva a nada", "无处可去", "ne mène nulle part",
                       "hiçbir yere varmaz"), ((xz + xe) / 2 + 0.05, yB + 0.2), FM, "center", ROT)
    l_zb = text(s, T(s, "pfad", "der Pfad steht weiter darin", "the path is still in it", "la ruta sigue dentro", "路径仍写在里面",
                     "le chemin y figure toujours", "yol hâlâ içinde yazılı"), (xz, yB - 0.48), FM, "center", BLAU)
    schritt(s, EIN([t_a, l_ziel], 0.7), WACHS(ziel[0], 0.7), EIN(ziel[1:], 0.7))
    s.pause(0.6)
    schritt(s, WACHS(za[0], 0.6), EIN([za[1], l_za], 0.6))
    schritt(s, BETONE(za[1], 0.6))
    s.pause(0.6)
    schritt(s, EIN(cat, 0.5), ZEICHNE(p_cat, 0.5))
    schritt(s, ZEICHNE(um, 0.8), EIN(l_um, 0.8))
    schritt(s, BETONE(ziel[1:], 0.6))
    s.pause(0.6)
    schritt(s, EIN([trenn, t_b], 0.5))
    schritt(s, EIN(zb, 0.2))
    schritt(s, *[VER(i, 0, yB - yA, 1.0) for i in zb])
    schritt(s, EIN([geist, l_geist], 0.6))
    schritt(s, ZEICHNE(leer, 0.6))
    schritt(s, EIN([kreuz, l_leer], 0.5))
    schritt(s, EIN(l_zb, 0.5), BETONE(zb[1], 0.6))
    s.speichern()


def k3usrmerge():
    """Früher /bin und /usr/bin mit eigenen Programmen; heute wandern alle nach /usr/bin, /bin ist ein Link mit dem Inhalt usr/bin;
    ebenso /sbin und /lib."""
    s = Szene("linux/k3usrmerge")
    trenn = linie(s, (0.05, 2.0), (0.05, -1.9), HELLGRAU, 2, DASH)
    t_f = text(s, T(s, "frueher", "früher", "earlier", "antes", "以前", "autrefois", "eskiden"), (-1.75, 1.88), FS)
    t_h = text(s, T(s, "heute", "heute", "today", "hoy", "现在", "aujourd'hui", "bugün"), (1.75, 1.88), FS)
    dz, top = 0.24, 1.3

    def kasten_p(x, n, titel):
        h = 0.3 + n * dz
        return [s.box("", (x, top - h / 2), breite=1.35, hoehe=h, form="rect", farbe=BLAU, fuellung=BLAU_HELL, dicke=2),
                tt(s, titel, x, top + 0.17, 0.16, SCHWARZ, "m")]

    pb, pu = ["bash", "cat", "ls", "cp"], ["less", "nano", "find", "du"]
    k_bin, k_usr, k_neu = kasten_p(-2.5, 4, "/bin"), kasten_p(-0.85, 4, "/usr/bin"), kasten_p(2.6, 8, "/usr/bin")

    def progs(x, namen):
        return [text(s, n, (x - 0.45, top - 0.27 - dz * i), FM, "left") for i, n in enumerate(namen)]

    t_bin, t_usr = progs(-2.5, pb), progs(-0.85, pu)
    c_bin, c_usr = progs(-2.5, pb), progs(-0.85, pu)
    l_f = text(s, T(s, "zwei", "zwei Verzeichnisse,\nje eigene Programme", "two directories,\neach with its own programs",
                    "dos directorios,\ncada uno con sus programas", "两个目录，\n各有各的程序", "deux répertoires,\nchacun ses programmes",
                    "iki dizin,\nher birinin kendi programları"), (-1.65, -0.3), FM, "center", GRAU)
    xl = 0.85
    link = [s.box("", (xl, 1.0), breite=1.2, hoehe=0.42, form="rect", farbe=ORANGE, fuellung=ORANGE_HELL, dicke=2.5),
            tt(s, "usr/bin", xl, 1.0, 0.15, SCHWARZ, "m"), tt(s, "/bin", xl, 1.38, 0.16, SCHWARZ, "m")]
    l_link = text(s, T(s, "sym", "symbolischer Link", "symbolic link", "enlace simbólico", "符号链接", "lien symbolique",
                       "sembolik bağlantı"), (xl, 0.6), FM, "center", ORANGE)
    p_link = pf(s, (xl + 0.62, 1.0), (2.6 - 0.69, 1.0), farbe=ORANGE, dicke=3)
    l_bash = text(s, T(s, "bash", "/bin/bash führt nach\n/usr/bin/bash", "/bin/bash leads to\n/usr/bin/bash", "/bin/bash lleva a\n/usr/bin/bash",
                       "/bin/bash 指向\n/usr/bin/bash", "/bin/bash mène à\n/usr/bin/bash", "/bin/bash,\n/usr/bin/bash'e çıkar"),
                  (xl, -0.2), FM, "center", DUNKEL)
    ebenso = [text(s, T(s, "ebenso", "ebenso:", "likewise:", "igual:", "同样：", "de même :", "aynı biçimde:"), (0.3, -1.12), FM, "left",
                   GRAU),
              tt(s, "/sbin -> usr/sbin", 0.3, -1.42, 0.15), tt(s, "/lib -> usr/lib", 0.3, -1.68, 0.15)]
    schritt(s, WACHS([k_bin[0], k_usr[0]], 0.8), EIN([t_f, k_bin[1], k_usr[1]] + t_bin + t_usr, 0.8))
    schritt(s, EIN(l_f, 0.5))
    s.pause(0.6)
    schritt(s, EIN([trenn, t_h, k_neu[1]], 0.6), WACHS(k_neu[0], 0.6))
    schritt(s, EIN(c_bin + c_usr, 0.2))
    schritt(s, *[VER(t, 2.6 - (-2.5), 0, 1.2) for t in c_bin],
            *[VER(t, 2.6 - (-0.85), -4 * dz, 1.2) for t in c_usr])
    s.pause(0.6)
    schritt(s, WACHS(link[0], 0.6), EIN(link[1:] + [l_link], 0.6))
    schritt(s, ZEICHNE(p_link, 0.6))
    schritt(s, EIN(l_bash, 0.5))
    s.pause(0.6)
    schritt(s, EIN(ebenso, 0.6))
    s.speichern()


# ================================================================== Abschnitt 9: Datenträger und Einhängen
# Hinweis: Die Zeichenreihenfolge folgt der Reihenfolge, in der Objekte erscheinen (nicht der Reihenfolge des Anlegens).
def k3einhaengen():
    """Drei Spalten: vorher (STICK leer, daneben der Stick mit eigener Wurzel), eingehängt (Wurzel des Sticks sitzt an STICK,
    urlaub.jpg erscheint), ausgehängt (STICK wieder leer)."""
    s = Szene("linux/k3einhaengen")
    cx = [-2.4, -0.15, 2.05]
    dz, ez, y0 = 0.38, 0.3, 1.25
    x0s = [c - 0.75 for c in cx]
    reihen = [("/", 0, "dir"), ("media", 1, "dir"), ("student", 2, "dir"), ("STICK", 3, "dir")]
    koepfe = [text(s, T(s, k, *w), (c, 1.78), FK) for c, (k, w) in zip(cx, (
        ("vorher", ("vorher", "before", "antes", "挂载前", "avant", "önce")),
        ("ein", ("eingehängt", "mounted", "montado", "已挂载", "monté", "bağlandı")),
        ("aus", ("ausgehängt", "unmounted", "desmontado", "已卸载", "démonté", "ayrıldı"))))]
    ystick = y0 - 3 * dz
    leer = T(s, "leer", "leer", "empty", "vacío", "空", "vide", "boş")
    B1, _ = zeilenbaum(s, x0s[0], y0, reihen, dz, ez)
    l1 = text(s, leer, (x0s[0] + 1.6, ystick), FM, "left", GRAU)
    box = s.box("", (-2.45, -1.0), breite=1.9, hoehe=1.0, form="round", farbe=ORANGE, fuellung=ORANGE_HELL, dicke=2.5)
    l_box = text(s, T(s, "stick", "USB-Stick (/dev/sdb1)", "USB stick (/dev/sdb1)", "memoria USB (/dev/sdb1)", "U 盘（/dev/sdb1）",
                      "clé USB (/dev/sdb1)", "USB bellek (/dev/sdb1)"), (-2.45, -0.64), FM)
    ST, _ = zeilenbaum(s, -3.15, -0.92, [("/", 0, "dir"), ("urlaub.jpg", 1, "datei")], dz, ez, textfarbe=ORANGE)
    l_wurzel = text(s, T(s, "wurzel", "Wurzel des Sticks", "root of the stick", "raíz de la memoria", "U 盘的根", "racine de la clé",
                         "belleğin kökü"), (-2.75, -0.92), FM, "left", GRAU)
    B2, _ = zeilenbaum(s, x0s[0], y0, reihen, dz, ez)
    KOP, _ = zeilenbaum(s, -3.15, -0.92, [("/", 0, "dir"), ("urlaub.jpg", 1, "datei")], dz, ez, textfarbe=ORANGE)
    dkx, dky = x0s[1] + 3 * ez + 3.15, ystick + 0.92
    ring = rahmen(s, (x0s[1] + 3 * ez + 0.27, ystick), 0.78, 0.3, ORANGE, 3)
    pfad = tt(s, "/media/student/STICK/urlaub.jpg", cx[1], -0.75, 0.13, ORANGE, "m")
    l_sitzt = text(s, T(s, "sitzt", "die Wurzel des Sticks sitzt an STICK", "the stick's root sits at STICK", "la raíz de la memoria está en STICK",
                        "U 盘的根挂在 STICK 上", "la racine de la clé se trouve à STICK", "belleğin kökü STICK'e oturur"), (cx[1], -1.05),
                   FM, "center", ORANGE)
    B3, _ = zeilenbaum(s, x0s[0], y0, reihen, dz, ez)
    l3 = text(s, leer, (x0s[2] + 1.6, ystick), FM, "left", GRAU)
    schritt(s, EIN([koepfe[0]] + flach(B1), 0.8))
    schritt(s, EIN(l1, 0.4))
    schritt(s, WACHS(box, 0.7), EIN([l_box] + flach(ST) + [l_wurzel], 0.7))
    s.pause(0.6)
    schritt(s, EIN(koepfe[1], 0.4), EIN(flach(B2), 0.2))
    schritt(s, *[VER(i, x0s[1] - x0s[0], 0, 1.0) for i in flach(B2)])
    schritt(s, EIN(flach(KOP), 0.2))
    schritt(s, *[VER(i, dkx, dky, 1.2) for i in flach(KOP)])
    schritt(s, AUS(KOP[0], 0.5), WACHS(ring, 0.5))
    schritt(s, EIN(pfad, 0.5))
    schritt(s, EIN(l_sitzt, 0.5))
    s.pause(0.6)
    schritt(s, EIN(koepfe[2], 0.4), EIN(flach(B3), 0.2))
    schritt(s, *[VER(i, x0s[2] - x0s[0], 0, 1.0) for i in flach(B3)])
    schritt(s, EIN(l3, 0.4))
    s.speichern()


def k3wslbaum():
    """Baum von WSL 2: ext4 auf /dev/sdd als Grundstock, tmpfs unter /tmp, 9p (Laufwerk C:) unter /mnt/c, je eine Farbe; Legende."""
    s = Szene("linux/k3wslbaum")
    pos = {"/": (0.0, 1.65), "etc": (-2.7, 0.9), "home": (-1.45, 0.9), "tmp": (-0.2, 0.9), "usr": (1.05, 0.9), "mnt": (2.5, 0.9),
           "student": (-1.45, 0.15), "bin": (1.05, 0.15), "c": (2.5, 0.15), "Users": (1.95, -0.6), "Windows": (2.95, -0.6)}
    vater = {"etc": "/", "home": "/", "tmp": "/", "usr": "/", "mnt": "/", "student": "home", "bin": "usr", "c": "mnt",
             "Users": "c", "Windows": "c"}

    def kn(n):
        return [s.box("", pos[n], breite=kb(n), hoehe=KH, form="round", farbe=GRAU, fuellung=WEISS, dicke=2),
                text(s, n, pos[n], FK)]

    r_ext = flaeche(s, -3.35, -0.98, 3.42, 1.98, BLAU_HELL, BLAU, 2)
    l_ext = [s.box("", (-3.15, -1.3), breite=0.32, hoehe=0.2, form="rect", farbe=BLAU, fuellung=BLAU_HELL, dicke=2),
             text(s, T(s, "ext", "ext4 auf /dev/sdd, 1007G: der Grundstock", "ext4 on /dev/sdd, 1007G: the base",
                       "ext4 en /dev/sdd, 1007G: la base", "ext4 位于 /dev/sdd，1007G：基础", "ext4 sur /dev/sdd, 1007G : la base",
                       "/dev/sdd üzerinde ext4, 1007G: temel"), (-2.9, -1.3), FM, "left")]
    E = {n: kante(s, pos[vater[n]], pos[n]) for n in vater}
    K = {n: kn(n) for n in pos}
    r_tmp = flaeche(s, -0.62, 0.62, 0.22, 1.18, GRUEN_HELL, GRUEN, 2)
    d_tmp = [E["tmp"]] + K["tmp"]             # erscheint erst mit seiner Fläche (liegt dann darüber)
    l_tmp = [s.box("", (-3.15, -1.6), breite=0.32, hoehe=0.2, form="rect", farbe=GRUEN, fuellung=GRUEN_HELL, dicke=2),
             text(s, T(s, "tmpfs", "tmpfs unter /tmp, 16G: im Arbeitsspeicher", "tmpfs at /tmp, 16G: in main memory",
                       "tmpfs en /tmp, 16G: en la memoria", "tmpfs 位于 /tmp，16G：在内存中", "tmpfs sous /tmp, 16G : en mémoire vive",
                       "/tmp altında tmpfs, 16G: bellekte"), (-2.9, -1.6), FM, "left")]
    r_c = flaeche(s, 1.45, -0.93, 3.4, 0.42, ORANGE_HELL, ORANGE, 2)
    d_c = [E["c"], E["Users"], E["Windows"]] + K["c"] + K["Users"] + K["Windows"]
    basis = [n for n in pos if n not in ("tmp", "c", "Users", "Windows")]
    l_c = [s.box("", (-3.15, -1.9), breite=0.32, hoehe=0.2, form="rect", farbe=ORANGE, fuellung=ORANGE_HELL, dicke=2),
           text(s, T(s, "9p", "9p unter /mnt/c, 475G: Laufwerk C: von Windows", "9p at /mnt/c, 475G: Windows drive C:",
                     "9p en /mnt/c, 475G: unidad C: de Windows", "9p 位于 /mnt/c，475G：Windows 的 C: 盘",
                     "9p sous /mnt/c, 475G : lecteur C: de Windows", "/mnt/c altında 9p, 475G: Windows'un C: sürücüsü"),
                (-2.9, -1.9), FM, "left")]
    schritt(s, EIN([r_ext] + l_ext, 0.7))
    s.pause(0.4)
    schritt(s, ZEICHNE([E[n] for n in basis if n in E], 0.8), WACHS([K[n][0] for n in basis], 0.8), EIN([K[n][1] for n in basis], 0.8))
    s.pause(0.6)
    schritt(s, EIN([r_tmp] + d_tmp + l_tmp, 0.7))
    schritt(s, BETONE(d_tmp[2], 0.6))
    s.pause(0.4)
    schritt(s, EIN([r_c] + d_c + l_c, 0.7))
    schritt(s, BETONE(d_c[4], 0.6))
    s.speichern()


def k3grenze():
    """Drei Felder ext4, tmpfs, 9p: der harte Link prallt an der Grenze ab, der symbolische Link (nur ein Pfad) überquert sie,
    mv über die Grenze wird zu Kopieren und Löschen."""
    s = Szene("linux/k3grenze")
    f_ext = flaeche(s, -3.4, -1.85, -0.5, 1.6, BLAU_HELL, BLAU, 2.5)
    f_tmp = flaeche(s, -0.25, 0.05, 3.4, 1.6, GRUEN_HELL, GRUEN, 2.5)
    f_9p = flaeche(s, -0.25, -1.85, 3.4, -0.2, ORANGE_HELL, ORANGE, 2.5)
    kopf = [text(s, "ext4", (-3.3, 1.42), FK, "left", BLAU), tt(s, "/home/student", -2.85, 1.42, 0.14),
            text(s, "tmpfs", (-0.15, 1.42), FK, "left", GRUEN), tt(s, "/tmp", 0.38, 1.42, 0.14),
            text(s, "9p", (-0.15, -0.38), FK, "left", ORANGE), tt(s, "/mnt/c", 0.12, -0.38, 0.14)]

    def datei(x, y, name):
        return [s.box("", (x, y), breite=0.32, hoehe=0.42, form="rect", farbe=GRAU, fuellung=WEISS, dicke=2),
                text(s, name, (x, y - 0.36), FM)]

    ek = datei(-2.4, 0.75, "einkauf.txt")
    no = datei(-2.4, -0.95, "notiz.txt")
    hart = pf(s, (-2.2, 0.95), (-0.53, 1.2), farbe=ROT, dicke=3)
    l_ln = tt(s, "ln", -1.35, 1.25, 0.15, ROT, "m")
    x_hart = s.kreuzchen(None, -0.37, 1.2, ROT, 0.22, 4)
    l_hart = text(s, T(s, "hart", "harter Link: geht nicht", "hard link: not possible", "enlace duro: imposible", "硬链接：不行",
                       "lien physique : impossible", "sabit bağlantı: olmaz"), (-0.05, 1.18), FM, "left", ROT)
    sym = [s.box("", (1.3, 0.55), breite=1.75, hoehe=0.36, form="rect", farbe=GRUEN, fuellung=WEISS, dicke=2.5),
           tt(s, "~/linuxk3/einkauf.txt", 1.3, 0.55, 0.13, SCHWARZ, "m")]
    l_sym = text(s, T(s, "sym", "symbolischer Link: nur ein Pfad", "symbolic link: just a path", "enlace simbólico: solo una ruta",
                      "符号链接：只是一个路径", "lien symbolique : juste un chemin", "sembolik bağlantı: yalnızca bir yol"), (1.3, 0.24),
                FM, "center", GRUEN)
    p_sym = pf(s, (0.4, 0.55), (-2.2, 0.68), farbe=GRUEN, dicke=3, dash=DASH)
    l_lns = tt(s, "ln -s", -1.35, 0.45, 0.15, GRUEN, "m")
    h_sym = haken(s, -0.37, 0.8)
    p_mv = pf(s, (-2.2, -0.95), (0.7, -0.95), farbe=ORANGE, dicke=3)
    l_mv = tt(s, "mv", -1.35, -0.8, 0.15, ORANGE, "m")
    kopie = datei(-2.4, -0.95, "notiz.txt")
    l_kop = text(s, T(s, "kop", "1. kopieren", "1. copy", "1. copiar", "1. 复制", "1. copier", "1. kopyala"), (1.0, -0.6), FM, "center",
                 ORANGE)
    x_mv = s.kreuzchen(None, -2.4, -0.95, ROT, 0.36, 4)
    l_loe = text(s, T(s, "loe", "2. löschen", "2. delete", "2. borrar", "2. 删除", "2. supprimer", "2. sil"), (-2.4, -1.58), FM,
                 "center", ROT)
    schritt(s, EIN([f_ext, f_tmp, f_9p] + kopf, 0.8))
    schritt(s, WACHS([ek[0], no[0]], 0.6), EIN([ek[1], no[1]], 0.6))
    s.pause(0.6)
    schritt(s, ZEICHNE(hart, 0.7), EIN(l_ln, 0.7))
    schritt(s, EIN([x_hart, l_hart], 0.5))
    s.pause(0.6)
    schritt(s, WACHS(sym[0], 0.6), EIN([sym[1], l_sym], 0.6))
    schritt(s, ZEICHNE(p_sym, 0.7), EIN(l_lns, 0.7))
    schritt(s, ZEICHNE(h_sym, 0.4))
    s.pause(0.6)
    schritt(s, ZEICHNE(p_mv, 0.6), EIN(l_mv, 0.6))
    schritt(s, EIN(kopie, 0.2))
    schritt(s, *[VER(i, 3.4, 0, 1.0) for i in kopie])
    schritt(s, EIN(l_kop, 0.4))
    schritt(s, ZEICHNE(x_mv, 0.5), EIN(l_loe, 0.5))
    s.speichern()


# ================================================================== Abschnitt 10: Finden und Platz messen
def k3find():
    """find rezepte -name "*.txt": ein Punkt besucht die Einträge in der Reihenfolge von find; je Eintrag Nummer und Häkchen/Kreuz,
    passende Pfade erscheinen in der Ausgabe."""
    s = Szene("linux/k3find")
    cmd = tt(s, '$ find rezepte -name "*.txt"', -3.3, 1.8, 0.17)
    zeilen = [("rezepte", 0, "dir"), ("kuchen", 1, "dir"), ("apfelkuchen.txt", 2, "datei"), ("kaesekuchen.txt", 2, "datei"),
              ("zettel.txt", 1, "datei"), ("suppen", 1, "dir"), ("kuerbissuppe.txt", 2, "datei")]
    Z, P = zeilenbaum(s, -3.0, 1.2, zeilen, 0.36, 0.34)
    passt = [False, False, True, True, True, False, True]
    nummern = [[s.kreis(None, -0.62, y, 0.11, GRAU, 2, WEISS, 1.0), text(s, str(i + 1), (-0.62, y), FM, "center")]
               for i, (_, y) in enumerate(P)]
    zeichen = [haken(s, -0.2, y) if ok else s.kreuzchen(None, -0.2, y, ROT, 0.16, 3.5) for ok, (_, y) in zip(passt, P)]
    term = term_kasten(s, (1.85, 0.25), 2.95, 1.45)
    l_aus = text(s, T(s, "ausgabe", "Ausgabe", "output", "salida", "输出", "sortie", "çıktı"), (1.85, 1.15), FM, "center", GRAU)
    pfade = ["rezepte/kuchen/apfelkuchen.txt", "rezepte/kuchen/kaesekuchen.txt", "rezepte/zettel.txt", "rezepte/suppen/kuerbissuppe.txt"]
    aus = [text(s, p, (0.5, 0.7 - 0.28 * i), FM, "left") for i, p in enumerate(pfade)]
    punkt = s.punkt(None, P[0][0] - 0.25, P[0][1], ORANGE, 0.07)
    leg = [[s.kreis(None, -3.2, -1.38, 0.11, GRAU, 2, WEISS, 1.0), text(s, "1", (-3.2, -1.38), FM, "center"),
            text(s, T(s, "folge", "Reihenfolge, in der find die Einträge besucht", "order in which find visits the entries",
                      "orden en que find visita las entradas", "find 访问各条目的顺序", "ordre dans lequel find visite les entrées",
                      "find'ın girdileri ziyaret sırası"), (-2.95, -1.38), FM, "left")],
           haken(s, -3.2, -1.68) + [text(s, T(s, "ja", "Test bestanden: Pfad wird ausgegeben", "test passed: path is printed",
                                             "prueba superada: se imprime la ruta", "测试通过：输出路径", "test réussi : le chemin est affiché",
                                             "test geçti: yol yazdırılır"), (-2.95, -1.68), FM, "left")],
           [s.kreuzchen(None, -3.2, -1.98, ROT, 0.16, 3.5),
            text(s, T(s, "nein", "Test nicht bestanden", "test failed", "prueba no superada", "测试未通过", "test échoué", "test geçmedi"),
                 (-2.95, -1.98), FM, "left")]]
    schritt(s, EIN([cmd] + flach(Z), 0.8), WACHS(term, 0.8), EIN(l_aus, 0.8))
    s.pause(0.6)
    k = 0
    for i, ((x, y), ok) in enumerate(zip(P, passt)):
        if i == 0:
            schritt(s, EIN(punkt, 0.35))
        else:
            schritt(s, ZU(punkt, x - 0.25, y, 0.35))
        neu = nummern[i] + flach(zeichen[i])
        if ok:
            neu.append(aus[k])
            k += 1
        schritt(s, EIN(neu, 0.35))
    schritt(s, AUS(punkt, 0.4))
    schritt(s, EIN(flach(leg), 0.6))
    s.speichern()


def k3quoting():
    """Oben: find . -name *.txt; die Shell ersetzt *.txt durch drei Namen, find bekommt eine falsche Bedingung (rot).
    Unten: mit Anführungszeichen kommt *.txt bei find an und gilt im ganzen Teilbaum (grün)."""
    s = Szene("linux/k3quoting")
    x0, e1, e2 = -3.3, 0.17, 0.15
    a1 = tt(s, "$ find . -name *.txt", x0, 1.75, e1)
    l_ohne = text(s, T(s, "ohne", "ohne Anführungszeichen", "without quotes", "sin comillas", "不加引号", "sans guillemets", "tırnaksız"),
                  (-1.3, 1.75), FM, "left", GRAU)
    m1 = mark(s, sp(x0, 15, e1), sp(x0, 20, e1), 1.75, 0.25, ORANGE, 0.25)
    p1 = pf(s, (msp(x0, 15, 19, e1), 1.6), (msp(x0, 15, 19, e1), 0.92), farbe=ORANGE)
    l1 = text(s, T(s, "ersetzt", "die Shell ersetzt *.txt\ndurch passende Namen", "the shell replaces *.txt\nwith matching names",
                   "la shell sustituye *.txt\npor los nombres que encajan", "shell 把 *.txt\n替换成匹配的名称",
                   "le shell remplace *.txt\npar les noms qui conviennent", "kabuk *.txt'yi\neşleşen adlarla değiştirir"),
              (-1.6, 1.26), FM, "left", ORANGE)
    wd = s.box("", (2.3, 1.075), breite=2.1, hoehe=1.35, form="rect", farbe=GRAU, fuellung=WEISS, dicke=2)
    wd_t = text(s, T(s, "wd", "Arbeitsverzeichnis", "working directory", "directorio de trabajo", "工作目录", "répertoire de travail",
                     "çalışma dizini"), (2.3, 1.58), FM, "center", GRAU)
    wd_n = [text(s, n, (1.45, 1.33 - 0.2 * i), FM, "left", ORANGE if n.endswith(".txt") else SCHWARZ)
            for i, n in enumerate(["aktuell.txt", "einkauf.txt", "fotos", "rezepte", "zettel.txt"])]
    p_wd = pf(s, (1.22, 0.93), (0.48, 0.8), farbe=ORANGE, dash=DASH)
    b1 = tt(s, "find . -name aktuell.txt einkauf.txt zettel.txt", x0, 0.75, e2)
    r1 = [rahmen(s, (msp(x0, a, b, e2), 0.75), (b - a + 1) * cw(e2) + 0.06, 0.24, ROT, 2.5) for a, b in ((13, 23), (25, 35), (37, 46))]
    l_b1 = text(s, T(s, "falsch", "falsche Bedingung: find bricht mit Fehler ab", "wrong condition: find stops with an error",
                     "condición errónea: find se detiene con un error", "条件错误：find 报错退出",
                     "mauvaise condition : find s'arrête sur une erreur", "yanlış koşul: find hatayla durur"), (x0, 0.4), FM, "left", ROT)
    trenn = linie(s, (-3.4, 0.12), (3.4, 0.12), HELLGRAU, 2, DASH)
    a2 = tt(s, '$ find . -name "*.txt"', x0, -0.35, e1)
    l_mit = text(s, T(s, "mit", "mit Anführungszeichen", "with quotes", "con comillas", "加引号", "avec guillemets", "tırnaklı"),
                 (-1.12, -0.35), FM, "left", GRAU)
    m2 = mark(s, sp(x0, 15, e1), sp(x0, 22, e1), -0.35, 0.25, GRUEN, 0.25)
    p2 = pf(s, (msp(x0, 15, 21, e1), -0.5), (msp(x0, 15, 21, e1), -1.17), farbe=GRUEN)
    l2 = text(s, T(s, "weg", "die Shell nimmt nur die\nAnführungszeichen weg", "the shell only removes\nthe quotes",
                   "la shell solo quita\nlas comillas", "shell 只去掉\n引号", "le shell enlève seulement\nles guillemets",
                   "kabuk yalnızca\ntırnakları kaldırır"), (-1.5, -0.84), FM, "left", GRUEN)
    b2 = tt(s, "find . -name *.txt", x0, -1.35, e2)
    r2 = rahmen(s, (msp(x0, 13, 17, e2), -1.35), 5 * cw(e2) + 0.06, 0.24, GRUEN, 2.5)
    l_b2 = text(s, T(s, "richtig", "find prüft *.txt an jedem Namen im ganzen Teilbaum", "find tests *.txt against every name in the subtree",
                     "find aplica *.txt a cada nombre de todo el subárbol", "find 用 *.txt 检查整个子树中的每个名称",
                     "find teste *.txt sur chaque nom de tout le sous-arbre", "find, *.txt'yi tüm alt ağaçtaki her adda dener"),
                (x0, -1.72), FM, "left", GRUEN)
    schritt(s, EIN([a1, l_ohne], 0.7), WACHS(wd, 0.7), EIN([wd_t] + wd_n, 0.7))
    s.pause(0.6)
    schritt(s, EIN(m1, 0.4))
    schritt(s, ZEICHNE(p1, 0.6), EIN(l1, 0.6))
    schritt(s, ZEICHNE(p_wd, 0.5), BETONE([wd_n[0], wd_n[1], wd_n[4]], 0.6))
    schritt(s, EIN(b1, 0.5))
    schritt(s, ZEICHNE(r1, 0.5))
    schritt(s, EIN(l_b1, 0.5))
    s.pause(0.6)
    schritt(s, EIN([trenn, a2, l_mit], 0.6))
    schritt(s, EIN(m2, 0.4))
    schritt(s, ZEICHNE(p2, 0.6), EIN(l2, 0.6))
    schritt(s, EIN(b2, 0.5))
    schritt(s, ZEICHNE(r2, 0.4))
    schritt(s, EIN(l_b2, 0.5))
    s.speichern()


def k3findsize():
    """Zahlenstrahl (nicht maßstäblich) mit Dateien von 0, 32, 1024 und 1025 Bytes, darüber ihre Größe in ganzen KiB (aufgerundet);
    -size -1k trifft nur 0, -size -2k alles bis 1024."""
    s = Szene("linux/k3findsize")
    p = {0: -2.5, 32: -1.8, 1024: 0.5, 1025: 1.2, 2048: 2.7}
    ya, yk = 0.0, 0.55
    achse = pf(s, (-2.75, ya), (3.3, ya), farbe=SCHWARZ, dicke=2.5, spitze=0.1)
    ticks = [linie(s, (p[b], ya - 0.09), (p[b], ya + 0.09), SCHWARZ, 2.5) for b in (0, 1024, 2048)]
    l_bytes = text(s, "Bytes", (-2.85, ya - 0.3), FM, "right", GRAU)
    lbl = [text(s, str(b), (p[b], ya - 0.3), FK, "center", GRAU if b == 2048 else SCHWARZ) for b in (0, 32, 1024, 1025, 2048)]
    dots = [s.punkt(None, p[b], ya, BLAU, 0.07) for b in (0, 32, 1024, 1025)]
    l_kib = text(s, "KiB", (-2.85, yk), FM, "right", ORANGE)
    stufen = [[linie(s, (p[b], ya + 0.1), (p[b], yk - 0.13), ORANGE, 1.5, DOT), text(s, str(k), (p[b], yk), FK, "center", ORANGE)]
              for b, k in ((0, 0), (32, 1), (1024, 1), (1025, 2))]
    titel = text(s, T(s, "titel", "Größe in ganzen KiB, immer aufgerundet", "size in whole KiB, always rounded up",
                      "tamaño en KiB enteros, siempre redondeado hacia arriba", "以整 KiB 计的大小，总是向上取整",
                      "taille en KiB entiers, toujours arrondie vers le haut", "tam KiB cinsinden boyut, hep yukarı yuvarlanır"),
                 (0.2, 1.2), FK)
    band1 = flaeche(s, p[0] - 0.18, -0.15, p[0] + 0.18, 0.82, GRUEN, deckung=0.22)
    band2 = flaeche(s, p[0] - 0.18, -0.15, p[1024] + 0.18, 0.82, BLAU, deckung=0.13)
    r1 = [tt(s, "-size -1k", -3.3, -0.85, 0.17, GRUEN),
          text(s, T(s, "r1", "weniger als 1 KiB, also nur die leere Datei", "less than 1 KiB, so only the empty file",
                    "menos de 1 KiB: solo el archivo vacío", "小于 1 KiB：只有空文件", "moins de 1 KiB : seulement le fichier vide",
                    "1 KiB'tan az: yalnızca boş dosya"), (-2.35, -0.85), FM, "left")]
    r2 = [tt(s, "-size -2k", -3.3, -1.2, 0.17, BLAU),
          text(s, T(s, "r2", "weniger als 2 KiB, also alle bis 1024 Bytes", "less than 2 KiB, so everything up to 1024 bytes",
                    "menos de 2 KiB: todo hasta 1024 bytes", "小于 2 KiB：不超过 1024 字节的都算", "moins de 2 KiB : tout jusqu'à 1024 octets",
                    "2 KiB'tan az: 1024 bayta kadar her şey"), (-2.35, -1.2), FM, "left")]
    schritt(s, ZEICHNE(achse, 0.7), EIN(ticks + [l_bytes], 0.7))
    schritt(s, WACHS(dots, 0.6), EIN(lbl, 0.6))
    s.pause(0.6)
    schritt(s, EIN([titel, l_kib], 0.5))
    for st in stufen:
        schritt(s, ZEICHNE(st[0], 0.4), EIN(st[1], 0.4))
    s.pause(0.6)
    schritt(s, EIN([band1] + r1, 0.7))
    s.pause(0.6)
    schritt(s, EIN([band2] + r2, 0.7))
    s.speichern()


def k3findzeit():
    """Zeitachse von jetzt nach links in ganzen Tagen; -mtime -1 = jüngster Tag (grün), -mtime +7 = ab 8 ganzen Tagen (orange);
    kaesekuchen.txt vom 1. Oktober weit links."""
    s = Szene("linux/k3findzeit")
    w, xj, ya = 0.42, 3.0, 0.2

    def xn(n):
        return xj - n * w

    achse = [linie(s, (xj, ya), (-2.1, ya), SCHWARZ, 2.5), pf(s, (-2.3, ya), (-3.35, ya), farbe=SCHWARZ, dicke=2.5, spitze=0.1)]
    bruch = [linie(s, (-2.17, ya - 0.12), (-2.07, ya + 0.12), SCHWARZ, 2.5), linie(s, (-2.33, ya - 0.12), (-2.23, ya + 0.12), SCHWARZ, 2.5)]
    ticks = [linie(s, (xn(n), ya - 0.07), (xn(n), ya + 0.07), SCHWARZ, 2) for n in range(13)]
    zahlen = [text(s, str(n), (xn(n + 0.5), ya - 0.25), FM, "center", ORANGE if n >= 8 else (GRUEN if n == 0 else SCHWARZ))
              for n in range(12)]
    jetzt = text(s, T(s, "jetzt", "jetzt", "now", "ahora", "现在", "maintenant", "şimdi"), (3.15, ya - 0.55), FM, "right")
    aelter = text(s, T(s, "aelter", "älter", "older", "más antiguo", "更早", "plus ancien", "daha eski"), (-3.3, ya - 0.3), FM, "left",
                  GRAU)
    titel = text(s, T(s, "titel", "Alter in ganzen Tagen (angebrochene Tage fallen weg)", "age in whole days (partial days are dropped)",
                      "edad en días enteros (los días empezados no cuentan)", "以整天计的时长（不足一天的部分舍去）",
                      "âge en jours entiers (les jours entamés ne comptent pas)", "tam gün olarak yaş (yarım günler sayılmaz)"),
                 (0.2, ya - 0.62), FM, "center", GRAU)
    kaese = s.punkt(None, -2.95, ya, BLAU, 0.08)
    l_kaese = text(s, T(s, "kaese", "kaesekuchen.txt, 1. Okt.", "kaesekuchen.txt, Oct 1", "kaesekuchen.txt, 1 oct.",
                        "kaesekuchen.txt，10月1日", "kaesekuchen.txt, 1er oct.", "kaesekuchen.txt, 1 Ekim"), (-3.3, ya + 0.45), FM, "left",
                   BLAU)
    apfel = s.punkt(None, 2.93, ya, BLAU, 0.08)
    l_apfel = text(s, T(s, "apfel", "apfelkuchen.txt (vor Minuten)", "apfelkuchen.txt (minutes ago)", "apfelkuchen.txt (hace minutos)",
                        "apfelkuchen.txt（几分钟前）", "apfelkuchen.txt (il y a quelques minutes)", "apfelkuchen.txt (dakikalar önce)"),
                   (2.85, ya + 0.45), FM, "right", BLAU)
    band1 = flaeche(s, xn(1), ya - 0.15, xj, ya + 0.75, GRUEN, deckung=0.22)
    band7 = flaeche(s, -3.35, ya - 0.15, xn(8), ya + 0.75, ORANGE, deckung=0.18)
    t1 = tt(s, "-mtime -1", xn(0.5), ya + 0.95, 0.16, GRUEN, "m")
    t7 = tt(s, "-mtime +7", -1.85, ya + 0.95, 0.16, ORANGE, "m")
    r1 = [tt(s, "-mtime -1", -3.3, -0.9, 0.16, GRUEN),
          text(s, T(s, "m1", "in den letzten 24 Stunden geändert", "changed in the last 24 hours", "modificado en las últimas 24 horas",
                    "最近 24 小时内修改过", "modifié au cours des dernières 24 heures", "son 24 saatte değiştirilmiş"), (-2.3, -0.9), FM,
               "left")]
    r7 = [tt(s, "-mtime +7", -3.3, -1.22, 0.16, ORANGE),
          text(s, T(s, "m7", "vor mindestens 8 ganzen Tagen geändert", "changed at least 8 whole days ago",
                    "modificado hace al menos 8 días enteros", "至少 8 整天之前修改过", "modifié il y a au moins 8 jours entiers",
                    "en az 8 tam gün önce değiştirilmiş"), (-2.3, -1.22), FM, "left")]
    sieben = text(s, T(s, "sieben", "7 Tage und einige Stunden zählen als 7, also nicht als +7",
                       "7 days and a few hours count as 7, so not as +7", "7 días y algunas horas cuentan como 7, no como +7",
                       "7 天零几小时算作 7，不算 +7", "7 jours et quelques heures comptent pour 7, donc pas pour +7",
                       "7 gün ve birkaç saat 7 sayılır, yani +7 değil"), (-3.3, -1.55), FM, "left", GRAU)
    schritt(s, ZEICHNE(achse, 0.8), EIN(bruch + ticks, 0.8))
    schritt(s, EIN(zahlen + [jetzt, aelter, titel], 0.6))
    s.pause(0.6)
    schritt(s, WACHS([kaese, apfel], 0.6), EIN([l_kaese, l_apfel], 0.6))
    s.pause(0.6)
    schritt(s, EIN([band1, t1], 0.6))
    schritt(s, EIN(r1, 0.5))
    s.pause(0.6)
    schritt(s, EIN([band7, t7], 0.6))
    schritt(s, EIN(r7, 0.5), BETONE(l_kaese, 0.7))
    s.pause(0.4)
    schritt(s, EIN(sieben, 0.5), BETONE(zahlen[7], 0.7))
    s.speichern()


def k3du():
    """Rechenbild: Platz von rezepte in KiB, ganze Blöcke zu 4 KiB: kuchen 4 + 4 + 4 = 12, suppen 4 + 4 = 8, Link 0,
    rezepte 4 + 12 + 8 + 0 = 24 wie du meldet."""
    s = Szene("linux/k3du")
    tex = (r"\begin{aligned}"
           r"\mathtt{kuchen} &:\; 4 + 4 + 4 = 12\\"
           r"\mathtt{suppen} &:\; 4 + 4 = 8\\"
           r"\texttt{zettel.txt} &:\; 0\\[4pt]"
           r"\mathtt{rezepte} &:\; 4 + 12 + 8 + 0 = 24"
           r"\end{aligned}")
    kopf = text(s, T(s, "kopf", "belegter Platz in KiB (ein Block = 4 KiB)", "space used in KiB (one block = 4 KiB)",
                     "espacio ocupado en KiB (un bloque = 4 KiB)", "占用空间，单位 KiB（一个块 = 4 KiB）",
                     "espace occupé en KiB (un bloc = 4 KiB)", "kullanılan alan, KiB (bir blok = 4 KiB)"), (-0.2, 1.05), FM, "center", GRAU)
    schritt(s, EIN(kopf, 0.5))
    s.pause(0.4)
    s.formel(tex, mitte=(-1.25, 0.05), hoehe=1.3, zeilenweise=True, dauer=4.8)    # eigener Schritt: Zeile für Zeile
    xa = 1.15
    a = [text(s, T(s, "a1", "Verzeichnis + zwei Rezepte", "directory + two recipes", "directorio + dos recetas", "目录 + 两个食谱",
                   "répertoire + deux recettes", "dizin + iki tarif"), (xa, 0.55), FM, "left", ORANGE),
         text(s, T(s, "a2", "Verzeichnis + ein Rezept", "directory + one recipe", "directorio + una receta", "目录 + 一个食谱",
                   "répertoire + une recette", "dizin + bir tarif"), (xa, 0.23), FM, "left", ORANGE),
         text(s, T(s, "a3", "symbolischer Link: kein Block", "symbolic link: no block", "enlace simbólico: ningún bloque", "符号链接：不占块",
                   "lien symbolique : aucun bloc", "sembolik bağlantı: blok yok"), (xa, -0.09), FM, "left", ORANGE),
         text(s, T(s, "a4", "eigener Block + Teilsummen,\nwie du rezepte meldet", "own block + subtotals,\nas du rezepte reports",
                   "bloque propio + subtotales,\ncomo indica du rezepte", "自身一个块 + 各部分之和，\n与 du rezepte 的结果相同",
                   "bloc propre + sous-totaux,\ncomme l'indique du rezepte", "kendi bloğu + ara toplamlar,\ndu rezepte'nin bildirdiği gibi"),
              (xa, -0.48), FM, "left", GRAU)]
    s.pause(0.4)
    for t in a:
        schritt(s, EIN(t, 0.5))
    s.speichern()


# Hälfte 1 (Abschnitte 1–5, Phase 2b-1); Phase 2b-2 hängt die Szenen der Abschnitte 6–10 hinten an.
SZENEN = (k3bytes, k3verzeichnis, k3baum, k3laufwerke,
          k3arbeitsverzeichnis, k3pfad, k3absolutrelativ, k3punkte,
          k3versteckt, k3lsl, k3sortieren, k3namen,
          k3text, k3headtail, k3wc, k3magie,
          k3mkdirp, k3touch, k3nano, k3einkauf,
          # Hälfte 2 (Abschnitte 6–10, Phase 2b-2)
          k3cp, k3cpr, k3mv, k3papierkorb, k3muster,
          k3fhs, k3dev, k3proc,
          k3inode, k3tabelle, k3hartlink, k3symlink, k3usrmerge,
          k3einhaengen, k3wslbaum, k3grenze,
          k3find, k3quoting, k3findsize, k3findzeit, k3du,
          )

if __name__ == "__main__":
    for f in SZENEN:
        f()
