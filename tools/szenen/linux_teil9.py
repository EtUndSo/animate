"""Linux und Kommandozeile, Kapitel 9 „Software installieren: Paketverwaltung“ (C:\\Bücher\\EtUndSo\\Linux\\Arbeitshefte\\
Kap9_Pakete.tex, kap9_stufen.tex, kap9_stufen_b.tex): Abbildungen, alle animiert (notizen/animationen.md §5, §11).

Szenenname linux/k9<name> = \\label{fig:k9<name>} im Heft (\\szenenabb{k9<name>}{…}{fig:k9<name>}); Liste in uebergabe_kap9.md,
Abschnitt „Endgültige Abbildungsliste“. Phase 2b-1 (12.11.2026): Abschnitte 1–5 (24 Szenen); Phase 2b-2 ergänzt die
Abschnitte 6–10 in dieser Datei.
Stil: F1. Terminalbilder (apt search, apt show, apt list, dpkg-deb -I) sind s.terminal (dunkel, wie Ubuntu, echte Farben
von apt: Paketname grün, bei apt show Feldnamen fett), Zeilen mit Spalten (dpkg -l, Versionen, Adressen) s.raster,
Datei-Ansichten (ubuntu.sources, control, md5sums) s.datei (hell). Übrige Schemata aus Kästen und Pfeilen mit den Helfern
unten und aus linux_hilfen.py. Inhalte (Zeilen, Versionen, Zahlen) wörtlich aus dem Heft bzw. den Mitschriften
code/kap9/sitzung_kap9*.txt; ausgelassene Zeilen stehen wie im Heft als „...“ (grau).
Farben: grün = installiert/stimmt, orange = neu/hervorgehoben, blau = Paket/Verzeichnis, rot = Fehler/fehlt,
grau = nicht beteiligt. Koordinaten zwischen x = -3,45 und 3,45 (höchstens 548 px).
Bauen:  python tools/szenen/linux_teil9.py [k9name …]
Export: python tools/export_szenen.py --animiert <alle Namen aus SZENEN>
"""
import math
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from szenen_lib import *  # noqa: E402,F403
from szenen_lib import farbig, fett, tt_breite  # noqa: E402,F401

from linux_hilfen import *  # noqa: E402,F403  (gemeinsame Helfer der Linux-Kapitel)

schreibmaschine("text")
TT = 18                           # Schreibmaschinenschrift für Zeilen (9,9 px im Artikel)
TK = 17                           # kleinste Schreibmaschinenschrift (Paketnamen, Pfade)
P9 = "student@labor:~/linuxk9$ "    # Prompt im Arbeitsverzeichnis des Kapitels (Abschnitt 1.1: cd ~/linuxk9)
PFAD = "~/linuxk9"
TITEL = "student@labor: ~/linuxk9"
HELLO_DEB = "hello_2.10-5build1_amd64.deb"
PUNKTE = farbig("...", "grau")    # ausgelassene Zeilen (im Heft „...“)


def r4(v):
    return round(v, 4)


def ttb(t, g=TK):
    """Breite eines Texts in Schreibmaschinenschrift."""
    return len(t) * tt_breite(g, 1)


def L(s, key, w, pos, g=FM, a="center", f=SCHWARZ):
    """Beschriftung in sechs Sprachen; w = (de, en, es, zh, fr, tr)."""
    return text(s, T(s, key, *w), (r4(pos[0]), r4(pos[1])), g, a, f)


def Lr(s, key, w, pos, g=FM, a="center", f=SCHWARZ):
    """Wie L, aber roh: Punkte in Zahlen bleiben Punkte („2.0“, türkisch „26.068“)."""
    return text(s, T(s, key, *w), (r4(pos[0]), r4(pos[1])), g, a, f, roh=True)


def tx(s, t, pos, g=TT, a="center", f=SCHWARZ):
    """Schreibmaschinenschrift (Paketnamen, Pfade, Befehle); in allen Sprachen gleich."""
    return s.text(None, t, (r4(pos[0]), r4(pos[1])), g, a, f, schrift="tt")


def txa(s, t, pos, g=TK, a="center", f=SCHWARZ):
    """Schreibmaschinenschrift mit ANSI-Farben (farbig) auf der weißen Seite."""
    return s.text(None, t, (r4(pos[0]), r4(pos[1])), g, a, f, schrift="tt", ansi=True)


def box(s, mitte, b, h, rand=GRAU, fuellung=WEISS, dicke=2, form="round", dash="", deckung=1.0):
    return s.box("", (r4(mitte[0]), r4(mitte[1])), breite=r4(b), hoehe=r4(h), form=form, farbe=rand, fuellung=fuellung,
                 deckung=deckung, dicke=dicke, dash=dash)


def chip(s, mitte, t, rand=BLAU, fuellung=BLAU_HELL, g=TK, h=0.28, b=None, dicke=2, textfarbe=SCHWARZ, dash=""):
    """Kärtchen mit Schreibmaschinenschrift (Paket, Datei); Ergebnis [Kasten, Text]."""
    b = b if b is not None else ttb(t, g) + 0.24
    return [box(s, mitte, b, h, rand, fuellung, dicke, dash=dash), tx(s, t, mitte, g, "center", textfarbe)]


def chipb(t, g=TK):
    return ttb(t, g) + 0.24


def wchip(s, mitte, key, w, b, rand=BLAU, fuellung=BLAU_HELL, g=FM, h=0.3, dicke=2, textfarbe=SCHWARZ):
    """Kärtchen mit Beschriftung in sechs Sprachen; Ergebnis [Kasten, Text]."""
    return [box(s, mitte, b, h, rand, fuellung, dicke), L(s, key, w, mitte, g, "center", textfarbe)]


def kreuz(s, x, y, g=0.2, farbe=ROT):
    return s.kreuzchen(None, r4(x), r4(y), farbe, g, 4)


def pfk(s, a, b, farbe=DUNKEL, dicke=2, dash="", knick="none", spitze=0.09, doppelt=False):
    """Dünner Pfeil (gerundete Koordinaten)."""
    return pf(s, (r4(a[0]), r4(a[1])), (r4(b[0]), r4(b[1])), knick=knick, farbe=farbe, dash=dash, doppelt=doppelt,
              dicke=dicke, spitze=spitze)


def lin(s, a, b, farbe=GRAU, dicke=2, dash=""):
    return linie(s, (r4(a[0]), r4(a[1])), (r4(b[0]), r4(b[1])), farbe, dicke, dash)


def bogen_x(s, a, b, hx, farbe=DUNKEL, dicke=2, dash="", marke="0.55"):
    """Bogen von a nach b, seitlich um hx ausgewölbt (hx > 0: nach rechts), Richtungsmarke bei marke."""
    fx = "%s+%s*t+%s*4*t*(1-t)" % (r4(a[0]), r4(b[0] - a[0]), r4(hx))
    fy = "%s+%s*t" % (r4(a[1]), r4(b[1] - a[1]))
    return s.weg(None, fx, fy, 0, 1, farbe=farbe, dicke=dicke, pfeile=marke, n=41, dash=dash, spitze=0.11)


def zbaum(s, x0, y0, eintraege, dz=0.3, einzug=0.3, g=TK, farbe=SCHWARZ, linien=GRAU):
    """Verzeichnisbaum als eingerückte Liste: eintraege = [(name, ebene, "dir"|"datei")], Namen in
    Schreibmaschinenschrift. Ergebnis (Z, P): Z[i] = [Verbinder…, Symbol, Text] (Text zuletzt), P[i] = (x Symbol, y)."""
    Z, P, letzte = [], [], {}
    for i, e in enumerate(eintraege):
        name, eb, art = e[:3]
        x, y = r4(x0 + eb * einzug), r4(y0 - i * dz)
        teile = []
        if eb > 0:
            px, py = letzte[eb - 1]
            teile += [lin(s, (px, py - 0.09), (px, y), linien, 2),
                      lin(s, (px, y), (x - (0.14 if art == "dir" else 0.09), y), linien, 2)]
        teile.append(ordner_symbol(s, x, y) if art == "dir" else datei_symbol(s, x, y))
        teile.append(tx(s, name, (x + 0.2, y), g, "left", e[3] if len(e) > 3 else farbe))
        Z.append(teile)
        P.append((x, y))
        if art == "dir":
            letzte[eb] = (x, y)
    return Z, P


W_INST = ("schon installiert", "already installed", "ya instalado", "已安装", "déjà installé", "zaten kurulu")
W_NEU = ("neu", "new", "nuevo", "新", "nouveau", "yeni")
W_PAKETDATEI = ("Paketdatei", "package file", "archivo de paquete", "软件包文件", "fichier de paquet", "paket dosyası")
W_BAUM = ("Verzeichnisbaum", "directory tree", "árbol de directorios", "目录树", "arborescence", "dizin ağacı")
W_DB = ("Paketdatenbank", "package database", "base de datos de paquetes", "软件包数据库", "base de données des paquets",
        "paket veritabanı")
W_PAKET = ("Paket", "package", "paquete", "软件包", "paquet", "paket")
W_DATEIEN = ("Dateien", "files", "archivos", "文件", "fichiers", "dosyalar")


# ================================================================== Abschnitt 1: Pakete und ihre Beziehungen
HELLO_PFADE = ["usr/bin/hello", "usr/share/doc/hello/NEWS.gz", "usr/share/doc/hello/changelog.Debian.gz",
               "usr/share/doc/hello/copyright", "usr/share/info/hello.info.gz", "usr/share/man/man1/hello.1.gz"]
W_DATEIEN_ZIEL = ("Dateien mit Zielort", "files with their destination", "archivos con su destino", "文件及其目标位置",
                  "fichiers et leur destination", "hedef konumlu dosyalar")
W_ETIKETT = ("Etikett", "label", "etiqueta", "标签", "étiquette", "etiket")
W_SKRIPTE = ("Skripte", "scripts", "scripts", "脚本", "scripts", "betikler")
W_LEER_HELLO = ("bei hello\nleer", "empty\nfor hello", "vacío\nen hello", "hello 中\n为空", "vide\npour hello",
                "hello'da\nboş")
W_BRAUCHT = ("braucht: libc6", "needs: libc6", "necesita: libc6", "需要：libc6", "requiert : libc6", "gerektirir: libc6")
W_INSTALLIERTE = ("installierte Pakete", "installed packages", "paquetes instalados", "已安装的软件包", "paquets installés",
                  "kurulu paketler")


def k9paket():
    """Paketdatei hello als Karton mit drei Fächern: Dateien mit Zielort (Inhalt von dpkg-deb -c), Etikett (Name,
    Version, Architektur, braucht libc6), Skripte (bei hello leer). Darunter der Verzeichnisbaum; beim Installieren
    wandern die Dateien an ihre Plätze, das Etikett in die Liste „installierte Pakete“."""
    s = Szene("linux/k9paket", reihenfolge="anlegen")
    karton = [box(s, (0, 1.93), 6.8, 1.7, ORANGE, ORANGE_HELL, 2.5, "rect"),
              tx(s, HELLO_DEB, (-3.4, 2.95), TK, "left"),
              L(s, "pd", W_PAKETDATEI, (-3.4 + ttb(HELLO_DEB) + 0.15, 2.95), FM, "left", GRAU),
              lin(s, (-0.08, 1.15), (-0.08, 2.71), ORANGE, 2), lin(s, (1.95, 1.15), (1.95, 2.71), ORANGE, 2)]
    h1 = L(s, "f1", W_DATEIEN_ZIEL, (-3.3, 2.58), FM, "left", DUNKEL)
    g = s.raster(HELLO_PFADE, (-3.3, 2.3), groesse=TK, zeilenabstand=1.3)
    h2 = L(s, "f2", W_ETIKETT, (0.05, 2.58), FM, "left", DUNKEL)
    etikett = [box(s, (0.95, 1.78), 1.75, 1.0, GRAU, GELB, 1.5, "rect"),
               tx(s, "hello", (0.95, 2.13), TK), tx(s, "2.10-5build1", (0.95, 1.93), TK), tx(s, "amd64", (0.95, 1.73), TK),
               L(s, "braucht", W_BRAUCHT, (0.95, 1.48), FM)]
    h3 = L(s, "f3", W_SKRIPTE, (2.05, 2.58), FM, "left", DUNKEL)
    skripte = [box(s, (2.7, 1.78), 1.2, 1.0, GRAU, WEISS, 1.5, "rect", DASH), L(s, "leer", W_LEER_HELLO, (2.7, 1.78), FM,
                                                                                 "center", GRAU)]
    # Verzeichnisbaum und Liste der installierten Pakete
    xf = -1.2
    dirs = [("/", 0), ("usr", 1), ("bin", 2), ("share", 2), ("doc/hello", 3), ("info", 3), ("man/man1", 3)]
    Z, P = zbaum(s, -3.3, 0.55, [(n, e, "dir") for n, e in dirs], dz=0.34)
    l_baum = L(s, "baum", W_BAUM, (-3.4, 0.86), FM, "left", GRAU)
    ziel_zeile = {"usr/bin/": 2, "usr/share/doc/hello/": 4, "usr/share/info/": 5, "usr/share/man/man1/": 6}
    naechstes_x = {}
    kopien, symbole, schiebe = [], [], []
    for z, pfad in enumerate(HELLO_PFADE):
        name = pfad.rsplit("/", 1)[1]
        ordner = pfad[:len(pfad) - len(name)]
        zz = ziel_zeile[ordner]
        x = naechstes_x.get(zz, xf)
        naechstes_x[zz] = x + ttb(name) + 0.3
        y = P[zz][1]
        a = len(pfad) - len(name)
        k = g.teil(z, a, len(pfad) - 1)
        kopien.append(k)
        symbole.append(datei_symbol(s, r4(x - 0.14), y))
        schiebe.append(VER(k, x - g.x(a), y - g.y(z), 1.3))
    liste = [box(s, (2.835, -0.55), 1.15, 1.75, DUNKEL, WEISS, 2, "rect"),
             L(s, "inst", W_INSTALLIERTE, (2.835, 0.5), FM, "center", DUNKEL)]
    alt = [tx(s, n, (2.835, y), TK, "center", GRAU) for n, y in (("bash", 0.12), ("grep", -0.13), ("tree", -0.38))] + \
          [txa(s, PUNKTE, (2.835, -0.63), TK)]
    et_chip = chip(s, (0.95, 2.13), "hello", GRAU, GELB, h=0.24, dicke=1.5)
    schritt(s, EIN(karton, 0.7))
    schritt(s, EIN([h1] + g.ids + kopien, 0.6))
    schritt(s, EIN([h2] + etikett, 0.6))
    schritt(s, EIN([h3] + skripte, 0.6))
    s.pause(0.6)
    schritt(s, EIN(flach(Z) + [l_baum] + liste + alt, 0.8))
    s.pause(0.4)
    schritt(s, EIN(symbole, 1.3), *schiebe)
    s.pause(0.4)
    schritt(s, EIN(et_chip, 0.4))
    schritt(s, *VERS(et_chip, 2.835 - 0.95, -0.92 - 2.13, 1.1))
    s.speichern()


VERSION_FARBIG = farbig("1", ORANGE) + ":" + farbig("2.41.3", BLAU) + "-" + farbig("3ubuntu2.2", GRUEN)
W_VERS = {"ep": ("Epoche", "epoch", "época", "纪元", "époque", "dönem"),
          "ep2": ("„Zählweise geändert“", "“numbering changed”", "«cambió la numeración»", "“编号方式变了”",
                  "« numérotation changée »", "“numaralama değişti”"),
          "pv": ("Programmversion", "program version", "versión del programa", "程序版本", "version du programme",
                 "program sürümü"),
          "pv2": ("„vom Projekt“", "“from the project”", "«del proyecto»", "“来自项目”", "« du projet »", "“projeden”"),
          "rv": ("Revision", "revision", "revisión", "修订号", "révision", "revizyon"),
          "rv2": ("„von der Distribution“", "“from the distribution”", "«de la distribución»", "“来自发行版”",
                  "« de la distribution »", "“dağıtımdan”"),
          "r1": ("von Debian", "from Debian", "de Debian", "来自 Debian", "de Debian", "Debian'dan"),
          "r2": ("zwei Änderungen durch Ubuntu", "two changes by Ubuntu", "dos cambios de Ubuntu", "Ubuntu 的两次修改",
                 "deux modifications par Ubuntu", "Ubuntu'nun iki değişikliği"),
          "r3": ("zwei spätere Korrekturen", "two later fixes", "dos correcciones posteriores", "两次后续修正",
                 "deux corrections ultérieures", "iki sonraki düzeltme"),
          "folge": ("Reihenfolge der Versionen", "order of versions", "orden de las versiones", "版本的先后顺序",
                    "ordre des versions", "sürümlerin sırası"),
          "alt": ("älter", "older", "más antigua", "更旧", "plus ancienne", "daha eski"),
          "neu": ("neuer", "newer", "más nueva", "更新", "plus récente", "daha yeni"),
          "tilde": ("~: etwas älter", "~: slightly older", "~: algo más antigua", "~：稍旧一些", "~ : un peu plus ancienne",
                    "~: biraz daha eski")}


def k9version():
    """Version 1:2.41.3-3ubuntu2.2 groß in Epoche (orange), Programmversion (blau), Revision (grün) zerlegt; die Revision
    klappt auf in 3 (Debian), ubuntu2, .2. Darunter ein Zahlenstrahl: 0.10.0-1ubuntu2~26.04.1 knapp links von
    0.10.0-1ubuntu2, die Tilde als kleiner Pfeil nach links."""
    s = Szene("linux/k9version", reihenfolge="anlegen")
    w = W_VERS
    g = s.raster(VERSION_FARBIG, (0, 2.0), groesse=34, ausrichtung="mitte")
    k_ep = g.klammer(0, 0, 0, "", seite="oben", farbe=ORANGE, dicke=2.5)[0]
    k_pv = g.klammer(0, 2, 7, "", seite="oben", farbe=BLAU, dicke=2.5)[0]
    k_rv = g.klammer(0, 9, 18, "", seite="oben", farbe=GRUEN, dicke=2.5)[0]
    yk = r4(g.oben(0) + 0.17)
    namen = [L(s, "ep", w["ep"], (g.x(0) - 0.12, yk), FM, "right", ORANGE),
             L(s, "pv", w["pv"], (g.xm(2, 7), yk + 0.22), FM, "center", BLAU),
             L(s, "rv", w["rv"], (g.xr(18) + 0.12, yk), FM, "left", GRUEN)]
    beschr = [L(s, "ep2", w["ep2"], (g.x(0) - 0.12, yk - 0.25), FM, "right", GRAU),
              L(s, "pv2", w["pv2"], (g.xm(2, 7), yk + 0.47), FM, "center", GRAU),
              L(s, "rv2", w["rv2"], (g.xr(18) + 0.12, yk - 0.25), FM, "left", GRAU)]
    # Revision aufklappen
    yr = 0.95
    teile = [(9, 9, -2.2), (10, 16, 0.0), (17, 18, 2.2)]
    kopien, schiebe, lab = [], [], []
    for i, (a, b, xm) in enumerate(teile):
        k = g.teil(0, a, b, farbe=GRUEN)
        kopien.append(k)
        breite = (b - a + 1) * g.zelle[0]
        schiebe.append(VER(k, xm - breite / 2 - g.x(a), yr - g.y(0), 1.1))
        lab.append(L(s, "r%d" % (i + 1), w["r%d" % (i + 1)], (xm, yr - 0.33), FM, "center", DUNKEL))
    # Zahlenstrahl
    ya = -0.6
    achse = [pfk(s, (-3.25, ya), (3.25, ya), GRAU, 2.5, spitze=0.12), L(s, "folge", w["folge"], (-3.25, ya + 0.3), FM, "left",
                                                                       GRAU),
             L(s, "alt", w["alt"], (-3.25, ya - 0.25), FM, "left", GRAU), L(s, "neu", w["neu"], (3.25, ya - 0.25), FM,
                                                                            "right", GRAU)]
    xb, xa = 1.45, 0.8
    pb = [s.punkt(None, xb, ya, BLAU, 0.06), tx(s, "0.10.0-1ubuntu2", (xb, ya - 0.27), TK)]
    pa = [s.punkt(None, xa, ya, ORANGE, 0.06),
          txa(s, "0.10.0-1ubuntu2" + farbig("~", ORANGE) + "26.04.1", (xa, ya + 0.29), TK)]
    tilde = [pfk(s, (xb - 0.08, ya + 0.12), (xa + 0.08, ya + 0.12), ORANGE, 2.5, spitze=0.08),
             L(s, "tilde", w["tilde"], (xa + 0.95, ya + 0.29), FM, "left", ORANGE)]
    schritt(s, EIN(g.ids, 0.7))
    schritt(s, ZEICHNE([k_ep, k_pv, k_rv], 0.6), EIN(namen + kopien, 0.6))
    schritt(s, EIN(beschr, 0.6))
    s.pause(0.6)
    schritt(s, *schiebe)
    schritt(s, EIN(lab, 0.6))
    s.pause(0.6)
    schritt(s, EIN(achse, 0.6))
    schritt(s, WACHS(pb[0], 0.5), EIN(pb[1], 0.5))
    schritt(s, WACHS(pa[0], 0.6), EIN(pa[1], 0.6), ZEICHNE(tilde[0], 0.6))
    schritt(s, EIN(tilde[1], 0.5))
    s.speichern()


W_ABH = {"neu3": ("neu zu installieren: ", "to be installed: ", "por instalar: ", "需要新安装：", "à installer : ",
                  "kurulacak: "),
         "grau": ("braucht libc6 selbst (schon da)", "needed by libc6 (already there)", "los necesita libc6 (ya están)",
                  "libc6 自身的依赖（已有）", "requis par libc6 (déjà là)", "libc6'nın ihtiyacı (zaten var)")}


def k9abhaengigkeit():
    """Abhängigkeitsgraph von jq: jq → libjq1, libonig5, libc6; libjq1 → libonig5, libc6; libonig5 → libc6. Unter libc6
    grau libgcc-s1 (→ gcc-16-base) und libc-gconv-modules-extra. Installierte grün umrandet, neue orange; Zähler 3."""
    s = Szene("linux/k9abhaengigkeit", reihenfolge="anlegen")
    pos = {"jq": (-1.2, 2.35), "libjq1": (-2.4, 1.25), "libonig5": (0.0, 1.25), "libc6": (-1.2, 0.1),
           "libgcc-s1": (-2.4, -0.9), "gcc-16-base": (-2.4, -1.7), "libc-gconv-modules-extra": (0.15, -0.9)}
    neu = {n: chip(s, pos[n], n, ORANGE, ORANGE_HELL, dicke=2.5) for n in ("jq", "libjq1", "libonig5")}
    libc = chip(s, pos["libc6"], "libc6", GRUEN, GRUEN_HELL, dicke=2.5)
    grau = {n: chip(s, pos[n], n, GRUEN, WEISS, dicke=1.5, textfarbe=GRAU)
            for n in ("libgcc-s1", "gcc-16-base", "libc-gconv-modules-extra")}
    a1 = [pfk(s, (-1.33, 2.2), (-2.25, 1.4), DUNKEL, 2.5), pfk(s, (-1.07, 2.2), (-0.15, 1.4), DUNKEL, 2.5),
          bogen_x(s, (-0.99, 2.35), (-0.88, 0.1), 1.6, DUNKEL, 2.5)]
    a2 = [pfk(s, (-2.03, 1.25), (-0.45, 1.25), DUNKEL, 2.5), pfk(s, (-2.3, 1.1), (-1.42, 0.25), DUNKEL, 2.5),
          pfk(s, (-0.1, 1.1), (-0.98, 0.25), DUNKEL, 2.5)]
    a3 = [pfk(s, (-1.45, -0.05), (-2.25, -0.75), GRAU, 2), pfk(s, (-2.4, -1.05), (-2.4, -1.55), GRAU, 2),
          pfk(s, (-0.95, -0.05), (-0.25, -0.75), GRAU, 2)]
    l_grau = L(s, "grau", W_ABH["grau"], (-3.4, -2.2), FM, "left", GRAU)
    leg = [box(s, (1.82, 2.35), 0.3, 0.2, GRUEN, GRUEN_HELL, 2.5), L(s, "inst", W_INST, (2.05, 2.35), FM, "left"),
           box(s, (1.82, 2.05), 0.3, 0.2, ORANGE, ORANGE_HELL, 2.5), L(s, "neu", W_NEU, (2.05, 2.05), FM, "left")]
    s.parameter("n", 0, ganzzahlig=True)
    zaehler = s.zahl(None, "n", (1.62, 1.6), stellen=0, vor=T(s, "neu3", *W_ABH["neu3"]), groesse=FK, ausrichtung="left",
                     farbe=ORANGE)
    schritt(s, EIN(leg + [zaehler], 0.6))
    with s.gleichzeitig():
        schritt(s, WACHS(neu["jq"][0], 0.6), EIN(neu["jq"][1], 0.6))
        s.verstellen("n", 1, dauer=0.6)
    s.pause(0.5)
    with s.gleichzeitig():
        schritt(s, ZEICHNE(a1, 0.9), EIN(neu["libjq1"] + neu["libonig5"] + libc, 0.9))
        s.verstellen("n", 3, dauer=0.9)
    s.pause(0.5)
    schritt(s, ZEICHNE(a2, 0.9))
    schritt(s, BETONE(neu["libonig5"][1], 0.7))
    s.pause(0.5)
    schritt(s, ZEICHNE(a3, 0.7), EIN(flach(list(grau.values())) + [l_grau], 0.7))
    s.speichern()


W_BEZ = {"dep": ("Abhängigkeit", "dependency", "dependencia", "依赖", "dépendance", "bağımlılık"),
         "rec": ("Empfehlung", "recommendation", "recomendación", "推荐", "recommandation", "öneri"),
         "sug": ("Vorschlag", "suggestion", "sugerencia", "建议", "suggestion", "tavsiye"),
         "schalter": ("Empfehlungen mitinstallieren:", "install recommendations:", "instalar recomendados:",
                      "同时安装推荐的软件包：", "installer les recommandations :", "önerilenleri de kur:"),
         "an": ("an", "on", "sí", "开", "oui", "açık"),
         "aus": ("aus", "off", "no", "关", "non", "kapalı"),
         "zahl": ("neu installiert: ", "newly installed: ", "instalados nuevos: ", "新安装：", "nouveaux paquets : ",
                  "yeni kurulan: ")}


def k9beziehungen():
    """fortune-mod mit drei Pfeilarten: Depends durchgezogen (libc6, librecode3), Recommends gestrichelt (fortunes-min),
    Suggests gepunktet (fortunes, x11-utils, bsdextrautils). Schalter „Empfehlungen mitinstallieren: an“: fortune-mod,
    librecode3, fortunes-min werden grün (libc6 war schon da), Zähler 3; Schalter „aus“: fortunes-min grau, Zähler 2."""
    s = Szene("linux/k9beziehungen", reihenfolge="anlegen")
    w = W_BEZ
    ziele = [("libc6", "dep"), ("librecode3", "dep"), ("fortunes-min", "rec"), ("fortunes", "sug"), ("x11-utils", "sug"),
             ("bsdextrautils", "sug")]
    x, yz, xs = -3.25, 1.0, {}
    for n, _ in ziele:
        b = chipb(n)
        xs[n] = r4(x + b / 2)
        x += b + 0.14
    stil = {"dep": "", "rec": DASH, "sug": "3,5"}
    fm = chip(s, (0, 2.4), "fortune-mod", GRAU, WEISS)
    knoten = {n: chip(s, (xs[n], yz), n, GRUEN if n == "libc6" else GRAU, GRUEN_HELL if n == "libc6" else WEISS) for n, _ in ziele}
    pfeile = {n: pfk(s, (xs[n] * 0.12, 2.25), (xs[n], yz + 0.15), DUNKEL, 2.5, stil[k]) for n, k in ziele}
    gruen = {n: chip(s, p, n, GRUEN, GRUEN_HELL) for n, p in (("fortune-mod", (0, 2.4)), ("librecode3", (xs["librecode3"], yz)),
                                                             ("fortunes-min", (xs["fortunes-min"], yz)))}
    yl = 0.42
    leg = {"dep": [lin(s, (-3.25, yl), (-2.8, yl), DUNKEL, 2.5), tx(s, "Depends", (-2.7, yl), TK, "left"),
                   L(s, "dep", w["dep"], (-2.7, yl - 0.23), FM, "left", GRAU)],
           "rec": [lin(s, (-1.0, yl), (-0.55, yl), DUNKEL, 2.5, DASH), tx(s, "Recommends", (-0.45, yl), TK, "left"),
                   L(s, "rec", w["rec"], (-0.45, yl - 0.23), FM, "left", GRAU)],
           "sug": [lin(s, (1.35, yl), (1.8, yl), DUNKEL, 2.5, "3,5"), tx(s, "Suggests", (1.9, yl), TK, "left"),
                   L(s, "sug", w["sug"], (1.9, yl - 0.23), FM, "left", GRAU)]}
    ys = -0.45
    l_sch = L(s, "schalter", w["schalter"], (-3.25, ys), FM, "left")
    pill_g = box(s, (-0.6, ys), 0.5, 0.26, GRUEN, GRUEN, 1.5)
    pill_x = box(s, (-0.6, ys), 0.5, 0.26, GRAU, HELLGRAU, 1.5)
    knopf = s.kreis(None, -0.47, ys, 0.1, farbe=GRAU, dicke=1.5, fuellung=WEISS, deckung=1.0)
    t_an = L(s, "an", w["an"], (-0.25, ys), FM, "left", GRUEN)
    s.parameter("n", 3, ganzzahlig=True)
    zaehler = s.zahl(None, "n", (0.75, ys), stellen=0, vor=T(s, "zahl", *w["zahl"]), groesse=FM, ausrichtung="left",
                     farbe=GRUEN)
    schritt(s, WACHS(fm[0], 0.5), EIN(fm[1], 0.5))
    for art in ("dep", "rec", "sug"):
        namen = [n for n, k in ziele if k == art]
        schritt(s, ZEICHNE([pfeile[n] for n in namen], 0.7), EIN(flach([knoten[n] for n in namen]) + leg[art], 0.7))
    s.pause(0.6)
    schritt(s, EIN([l_sch, pill_g, knopf, t_an], 0.6))
    schritt(s, EIN(flach(list(gruen.values())) + [zaehler], 0.7), AUS(fm + knoten["librecode3"], 0.7))
    s.pause(0.8)
    with s.gleichzeitig():
        schritt(s, VER(knopf, -0.26, 0, 0.7), EIN(pill_x, 0.7), AUS(gruen["fortunes-min"], 0.7))
        s.ersetzen(t_an, T(s, "aus", *w["aus"]), farbe=GRAU, dauer=0.7)
        s.verstellen("n", 2, dauer=0.7)
    s.speichern()


W_VIRT = {"virt": ("virtueller Name, keine eigene Datei", "virtual name, no file of its own", "nombre virtual, sin archivo propio",
                   "虚拟名称，没有自己的文件", "nom virtuel, sans fichier propre", "sanal ad, kendi dosyası yok"),
          "einpaket": ("ein Paket", "a package", "un paquete", "某个软件包", "un paquet", "bir paket"),
          "zufrieden": ("zufrieden", "satisfied", "satisfecho", "已满足", "satisfait", "karşılandı"),
          "platz": ("nur Platz für eines", "room for one only", "solo cabe uno", "只容得下一个", "place pour un seul",
                    "yalnızca birine yer var"),
          "wartet": ("wartet, bis postfix weicht", "waits until postfix leaves", "espera a que salga postfix",
                     "等 postfix 让位", "attend que postfix parte", "postfix çıkana kadar bekler"),
          "beide": ("beide installiert", "both installed", "ambos instalados", "两者都已安装", "tous deux installés",
                    "ikisi de kurulu")}


def k9virtuell():
    """Links der virtuelle Name awk (gestrichelter Rahmen): gawk und mawk mit Provides: awk; ein Paket mit Depends: awk ist
    zufrieden, sobald eines grün ist. Rechts mail-transport-agent mit Schild Conflicts: nur Platz für eines; postfix
    steckt darin, exim4-daemon-light wartet davor (Versuch hineinzukommen, abgewiesen)."""
    s = Szene("linux/k9virtuell", reihenfolge="anlegen")
    w = W_VIRT
    xl, xr, yr = -1.75, 1.75, 0.95
    rahmen_l = [box(s, (xl, yr), 3.0, 1.3, BLAU, WEISS, 2.5, "round", DASH), tx(s, "awk", (xl, yr + 0.43), TT, "center", BLAU)]
    l_virt = L(s, "virt", w["virt"], (xl, yr - 1.13), FM, "center", GRAU)
    gm = {"gawk": chip(s, (xl - 0.75, yr - 0.12), "gawk", GRAU, WEISS), "mawk": chip(s, (xl + 0.75, yr - 0.12), "mawk", GRAU, WEISS)}
    prov = [tx(s, "Provides: awk", (xl - 0.75, yr - 0.42), TK, "center", DUNKEL),
            tx(s, "Provides: awk", (xl + 0.75, yr - 0.42), TK, "center", DUNKEL),
            pfk(s, (xl - 0.62, yr + 0.03), (xl - 0.22, yr + 0.33), BLAU, 2), pfk(s, (xl + 0.62, yr + 0.03), (xl + 0.22, yr + 0.33), BLAU, 2)]
    g_gr = chip(s, (xl - 0.75, yr - 0.12), "gawk", GRUEN, GRUEN_HELL, dicke=2.5)
    m_gr = chip(s, (xl + 0.75, yr - 0.12), "mawk", GRUEN, GRUEN_HELL, dicke=2.5)
    dep = wchip(s, (xl - 0.55, 2.45), "einpaket", w["einpaket"], 1.1, GRAU, WEISS) + \
        [tx(s, "Depends: awk", (xl + 0.1, 2.45), TK, "left", DUNKEL)]
    p_dep = pfk(s, (xl, 2.3), (xl, yr + 0.67), DUNKEL, 2.5)
    ok = haken(s, xl + 1.35, 2.47, GRUEN, 0.1, 4) + [L(s, "zufrieden", w["zufrieden"], (xl + 1.5, 2.45), FM, "left", GRUEN)]
    beide = L(s, "beide", w["beide"], (xl, yr - 0.86), FM, "center", GRUEN)
    # rechts: Konflikt
    rahmen_r = [box(s, (xr, yr), 3.0, 1.3, BLAU, WEISS, 2.5, "round", DASH),
                tx(s, "mail-transport-agent", (xr, yr + 0.43), TK, "center", BLAU)]
    schild = chip(s, (xr + 0.95, yr + 0.85), "Conflicts", ROT, ROT_HELL, h=0.26, dicke=2)
    platz = [box(s, (xr, yr - 0.15), 2.0, 0.5, GRAU, WEISS, 1.5, "rect", "4,4"),
             L(s, "platz", w["platz"], (xr, yr - 0.85), FM, "center", GRAU)]
    postfix = chip(s, (xr, yr - 0.15), "postfix", GRUEN, GRUEN_HELL, dicke=2.5)
    ye = -0.45
    exim = chip(s, (xr, ye), "exim4-daemon-light", GRAU, WEISS)
    l_wartet = L(s, "wartet", w["wartet"], (xr, ye - 0.3), FM, "center", GRAU)
    nein = kreuz(s, xr + 0.95, ye + 0.32, 0.18)
    schritt(s, EIN(rahmen_l + [l_virt], 0.6))
    schritt(s, EIN(flach(list(gm.values())) + prov, 0.7))
    schritt(s, EIN(dep, 0.5), ZEICHNE(p_dep, 0.5))
    schritt(s, EIN(g_gr, 0.6), AUS(gm["gawk"], 0.6))
    schritt(s, EIN(ok, 0.5))
    schritt(s, EIN(m_gr + [beide], 0.5), AUS(gm["mawk"], 0.5))
    s.pause(0.6)
    schritt(s, EIN(rahmen_r + platz, 0.6), WACHS(schild, 0.6))
    schritt(s, EIN(postfix, 0.6))
    schritt(s, EIN(exim + [l_wartet], 0.6))
    schritt(s, *VERS(exim, 0, 0.3, 0.5))
    schritt(s, BETONE(schild[0], 0.6), WACHS(nein, 0.6))
    schritt(s, *VERS(exim, 0, -0.3, 0.5))
    s.speichern()


# ================================================================== Abschnitt 2: Die Paketverwaltung und ihre Datenbank
W_KEINEM = ("gehört keinem Paket", "belongs to no package", "no pertenece a ningún paquete", "不属于任何软件包",
            "n'appartient à aucun paquet", "hiçbir pakete ait değil")
W_VERSCHWINDET = ("verschwindet beim Entfernen von tree", "removed with the package tree", "desaparece al quitar tree",
                  "删除 tree 时一并删除", "disparaît quand on retire tree", "tree kaldırılınca silinir")


def tabelle_dateien(s, x0, y0, zeilen, bd=2.6, bp=0.85, zh=0.2, rand=GRAU):
    """Tabelle Dateien | Paket: zeilen = [(paket, [datei, …])]; Ergebnis (Kopf, Reihen, Lagen) mit Reihen[i] = Liste
    der Teile und Lagen[i] = {"paket": (x, y), "dateien": [(x_links, y)], "oben": y, "unten": y, "mitte": y}."""
    kopf_h = 0.3
    xd, xp = x0 + bd / 2, x0 + bd + bp / 2
    kopf = [box(s, (xd, y0), bd, kopf_h, rand, GRAU_HELL, 1.5, "rect"), box(s, (xp, y0), bp, kopf_h, rand, GRAU_HELL, 1.5, "rect"),
            L(s, "tk_d", W_DATEIEN, (xd, y0), FM, "center", DUNKEL), L(s, "tk_p", W_PAKET, (xp, y0), FM, "center", DUNKEL)]
    reihen, lagen = [], []
    y = y0 - kopf_h / 2
    for paket, dateien in zeilen:
        h = len(dateien) * zh + 0.1
        ym = y - h / 2
        teile = [box(s, (xd, ym), bd, h, rand, WEISS, 1.5, "rect"), box(s, (xp, ym), bp, h, rand, WEISS, 1.5, "rect"),
                 tx(s, paket, (xp, ym), TK)]
        lg = {"paket": (r4(xp), r4(ym)), "dateien": [], "oben": r4(y), "unten": r4(y - h), "mitte": r4(ym)}
        for k, d in enumerate(dateien):
            yd = r4(y - 0.05 - zh / 2 - k * zh)
            teile.append(txa(s, d, (x0 + 0.1, yd), TK, "left") if "\\e[" in d else tx(s, d, (x0 + 0.1, yd), TK, "left"))
            lg["dateien"].append((r4(x0 + 0.1), yd))
        reihen.append(teile)
        lagen.append(lg)
        y -= h
    return kopf, reihen, lagen


def k9datenbank():
    """Paketdatenbank als Tabelle Dateien | Paket (bash, grep, tree mit ihren Dateien) rechts, Verzeichnisbaum links;
    dünne Linien verbinden jede Datei mit ihrer Zeile. /etc/hostname bleibt grau ohne Linie. Zum Schluss wird die Zeile
    tree markiert, die verbundene Datei leuchtet: das verschwindet beim Entfernen."""
    s = Szene("linux/k9datenbank", reihenfolge="anlegen")
    eintraege = [("/", 0, "dir"), ("etc", 1, "dir"), ("hostname", 2, "datei", GRAU), ("usr", 1, "dir"), ("bin", 2, "dir"),
                 ("bash", 3, "datei"), ("grep", 3, "datei"), ("tree", 3, "datei"), ("share/man/man1", 2, "dir"),
                 ("grep.1.gz", 3, "datei")]
    Z, P = zbaum(s, -3.35, 2.45, eintraege, dz=0.27)
    l_baum = L(s, "baum", W_BAUM, (-3.4, 2.78), FM, "left", GRAU)
    l_db = L(s, "db", W_DB, (1.62, 2.78), FM, "center", GRAU)
    kopf, reihen, lagen = tabelle_dateien(s, 0.0, 2.45, [("bash", ["/usr/bin/bash", PUNKTE]),
                                                         ("grep", ["/usr/bin/grep", "/usr/share/man/man1/grep.1.gz", PUNKTE]),
                                                         ("tree", ["/usr/bin/tree", PUNKTE])])
    l_host = L(s, "keinem", W_KEINEM, (P[2][0] + 0.35 + ttb("hostname"), P[2][1]), FM, "left", GRAU)

    def ende(i):
        return (r4(P[i][0] + 0.25 + ttb(eintraege[i][0])), P[i][1])

    verb = [(lagen[0]["dateien"][0], 5), (lagen[1]["dateien"][0], 6), (lagen[1]["dateien"][1], 9), (lagen[2]["dateien"][0], 7)]
    linien = [lin(s, ende(i), (d[0] - 0.06, d[1]), BLAU, 1.5) for d, i in verb]
    m_tree = box(s, ((0.0 + 3.45) / 2, lagen[2]["mitte"]), 3.45, lagen[2]["oben"] - lagen[2]["unten"], ORANGE, ORANGE, 0, "rect",
                 deckung=0.25)
    tree_l = lin(s, ende(7), (lagen[2]["dateien"][0][0] - 0.06, lagen[2]["dateien"][0][1]), ORANGE, 2.5)
    tree_r = box(s, (P[7][0] + 0.2 + ttb("tree") / 2 - 0.05, P[7][1]), ttb("tree") + 0.42, 0.26, ORANGE, WEISS, 2.5,
                 deckung=0.0)
    l_weg = L(s, "weg", W_VERSCHWINDET, (1.72, lagen[2]["unten"] - 0.25), FM, "center", ORANGE)
    baum_teile = flach(Z)
    schritt(s, EIN(kopf + flach(reihen) + [l_db], 0.7))
    schritt(s, EIN(baum_teile + [l_baum], 0.7))
    s.pause(0.4)
    schritt(s, ZEICHNE(linien, 1.0))
    schritt(s, EIN(l_host, 0.5))
    s.pause(0.6)
    schritt(s, EIN([m_tree, tree_l, tree_r, l_weg], 0.6))
    schritt(s, BETONE([tree_r, Z[7][-1]], 0.8))
    s.speichern()


W_EB = {"a1": ("Pakete im Netz finden", "find packages on the network", "buscar paquetes en la red", "在网络上查找软件包",
               "trouver les paquets sur le réseau", "ağda paketleri bulmak"),
        "a2": ("Abhängigkeiten auflösen", "resolve dependencies", "resolver dependencias", "解析依赖关系",
               "résoudre les dépendances", "bağımlılıkları çözmek"),
        "a3": ("herunterladen und prüfen", "download and verify", "descargar y verificar", "下载并校验",
               "télécharger et vérifier", "indirmek ve doğrulamak"),
        "d1": ("Paketdatei auspacken", "unpack the package file", "desempaquetar el archivo", "解包软件包文件",
               "dépaqueter le fichier", "paket dosyasını açmak"),
        "d2": ("Skripte ausführen", "run scripts", "ejecutar scripts", "运行脚本", "exécuter les scripts",
               "betikleri çalıştırmak"),
        "d3": ("Buch führen", "keep the records", "llevar el registro", "登记记录", "tenir le registre", "kayıt tutmak"),
        "server": ("Server der\nDistribution", "distribution\nserver", "servidor de la\ndistribución", "发行版的\n服务器",
                   "serveur de la\ndistribution", "dağıtımın\nsunucusu"),
        "auftrag": ("installiere jq", "install jq", "instala jq", "安装 jq", "installe jq", "jq'yu kur"),
        "db2": ("Paket-\ndatenbank", "package\ndatabase", "base de datos\nde paquetes", "软件包\n数据库", "base de données\ndes paquets",
                "paket\nveritabanı"),
        "oben": ("obere\nEbene", "upper\nlevel", "nivel\nsuperior", "上层", "niveau\nsupérieur", "üst\nkatman"),
        "unten": ("untere\nEbene", "lower\nlevel", "nivel\ninferior", "下层", "niveau\ninférieur", "alt\nkatman")}


def k9ebenen():
    """Zwei Stockwerke: oben apt (Pakete im Netz finden, Abhängigkeiten auflösen, herunterladen und prüfen; Pfeil zum
    Server), unten dpkg (Paketdatei auspacken, Skripte ausführen, Buch führen; Pfeile zu Paketdatenbank und
    Verzeichnisbaum). Der Auftrag „installiere jq“ geht oben hinein und wird zu drei Paketdateien, die nach unten gehen."""
    s = Szene("linux/k9ebenen", reihenfolge="anlegen")
    w = W_EB
    yo, yu, bx, hb = 1.65, -0.45, -0.55, 1.4
    oben = [box(s, (bx, yo), 3.6, hb, BLAU, BLAU_HELL, 2.5, "rect"), tx(s, "apt", (-1.95, yo + 0.25), 28, "center", BLAU),
            L(s, "oben", w["oben"], (-1.95, yo - 0.15), FM, "center", GRAU)]
    oben += [L(s, k, w[k], (-1.35, yo + 0.43 - i * 0.26), FM, "left") for i, k in enumerate(("a1", "a2", "a3"))]
    unten = [box(s, (bx, yu), 3.6, hb, DUNKEL, GRAU_HELL, 2.5, "rect"), tx(s, "dpkg", (-1.95, yu + 0.25), 28, "center", DUNKEL),
             L(s, "unten", w["unten"], (-1.95, yu - 0.15), FM, "center", GRAU)]
    unten += [L(s, k, w[k], (-1.35, yu + 0.43 - i * 0.26), FM, "left") for i, k in enumerate(("d1", "d2", "d3"))]
    server = wchip(s, (2.65, yo + 0.3), "server", w["server"], 1.55, GRAU, WEISS, h=0.62)
    p_srv = pfk(s, (1.28, yo + 0.3), (1.85, yo + 0.3), DUNKEL, 2.5, doppelt=True)
    db = wchip(s, (2.65, yu + 0.25), "db2", w["db2"], 1.55, GRAU, WEISS, h=0.5)
    baum = wchip(s, (2.65, yu - 0.42), "baum", W_BAUM, 1.55, GRAU, WEISS, h=0.36)
    p_db = [pfk(s, (1.28, yu + 0.25), (1.85, yu + 0.25), DUNKEL, 2.5), pfk(s, (1.28, yu - 0.42), (1.85, yu - 0.42), DUNKEL, 2.5)]
    auftrag = wchip(s, (bx, 2.85), "auftrag", w["auftrag"], 1.6, ORANGE, ORANGE_HELL, h=0.32)
    p_auf = pfk(s, (bx, 2.68), (bx, yo + hb / 2 + 0.02), ORANGE, 2.5)
    namen = ["jq_….deb", "libjq1_….deb", "libonig5_….deb"]
    x, dateien, schiebe = -2.27, [], []
    for n in namen:
        b = chipb(n)
        c = chip(s, (r4(x + b / 2), yo - 0.52), n, ORANGE, ORANGE_HELL, h=0.26)
        dateien.append(c)
        schiebe += VERS(c, 0, yu - 0.52 - (yo - 0.52), 1.1)
        x += b + 0.1
    p_ab = pfk(s, (0.85, yo - hb / 2 - 0.03), (0.85, yu + hb / 2 + 0.03), ORANGE, 2.5)
    schritt(s, EIN(oben + server + [p_srv], 0.7))
    schritt(s, EIN(unten + db + baum + p_db, 0.7))
    s.pause(0.6)
    schritt(s, EIN(auftrag, 0.5), ZEICHNE(p_auf, 0.5))
    schritt(s, WACHS([c[0] for c in dateien], 0.7), EIN([c[1] for c in dateien], 0.7))
    s.pause(0.4)
    schritt(s, ZEICHNE(p_ab, 1.1), *schiebe)
    schritt(s, BETONE([db[0], baum[0]], 0.7))
    s.speichern()


DPKG_L = ["+-- Desired=Unknown/Install/Remove/Purge/Hold",
          "|+- Status=Not/Inst/Conf-files/Unpacked/halF-conf/Half-inst/trig-aWait/Trig-pend",
          "||+ Err?=(none)/Reinst-required (Status,Err: uppercase=bad)",
          "||| Name           Version      Architecture Description",
          "+++-==============-============-============-=============================================",
          "ii  grep           3.12-1       amd64        GNU grep, egrep and fgrep"]
W_DL = [("gewünscht: installieren (Install)", "desired: install (Install)", "deseado: instalar (Install)",
         "期望：安装（Install）", "souhaité : installer (Install)", "istenen: kur (Install)"),
        ("Zustand: installiert (Inst)", "status: installed (Inst)", "estado: instalado (Inst)", "状态：已安装（Inst）",
         "état : installé (Inst)", "durum: kurulu (Inst)"),
        ("Fehler: keiner, leer ((none))", "error: none, blank ((none))", "error: ninguno, vacío ((none))",
         "错误：无，空白（(none)）", "erreur : aucune, vide ((none))", "hata: yok, boş ((none))"),
        ("Name", "name", "nombre", "名称", "nom", "ad"),
        ("Programmversion", "program version", "versión del programa", "程序版本", "version du programme", "program sürümü"),
        ("Revision", "revision", "revisión", "修订号", "révision", "revizyon"),
        ("Architektur", "architecture", "arquitectura", "架构", "architecture", "mimari"),
        ("Kurzbeschreibung", "short description", "descripción breve", "简短描述", "description courte", "kısa açıklama")]


def k9dpkgl():
    """Ausgabe von dpkg -l mit den drei Kopfzeilen, der Spaltenzeile und der Zeile ii grep (Block s2_liste). Die
    Kopfzeilen werden nacheinander mit den Spalten 1, 2, 3 verbunden (Install, Inst, (none) und die senkrechten
    Striche in derselben Farbe), dann Klammern mit Nummern unter Name, Programmversion, Revision, Architektur und
    Beschreibung; Liste darunter."""
    s = Szene("linux/k9dpkgl", reihenfolge="anlegen")
    g = s.raster(DPKG_L, (-3.4, 2.45), groesse=TK, zeilenabstand=1.45)
    farben = [ORANGE, BLAU, GRUEN]
    woerter = [g.finde(0, "Install"), g.finde(1, "Inst"), g.finde(2, "(none)")]
    spalte, wort = [], []
    for k in range(3):
        spalte.append(g.markieren(k, k, k, farben[k], 0.35, bis=5))
        wort.append(g.markieren(k, woerter[k][0], woerter[k][1], farben[k], 0.35))
    leg_l = []
    for k in range(3):
        y = r4(0.75 - k * 0.3)
        leg_l.append([box(s, (-3.28, y), 0.24, 0.17, farben[k], farben[k], 1, "rect", deckung=0.45),
                      L(s, "dl%d" % k, W_DL[k], (-3.08, y), FM, "left")])
    felder = [(4, 7), (19, 22), (24, 24), (32, 36), (45, 69)]
    kl, leg_r = [], []
    for i, (a, b) in enumerate(felder):
        kl.append(g.klammer(5, a, b, str(i + 1), seite="unten", farbe=BLAU, groesse=FM))
        y = r4(0.75 - i * 0.3) if i < 3 else r4(0.75 - (i - 3) * 0.3)
        xl = 0.0 if i < 3 else 1.85
        leg_r.append([text(s, str(i + 1), (xl, y), FM, "center", BLAU),
                      L(s, "dr%d" % i, W_DL[3 + i], (r4(xl + 0.15), y), FM, "left")])
    schritt(s, EIN(g.ids, 0.7))
    s.pause(0.6)
    for k in range(3):
        schritt(s, EIN([spalte[k], wort[k]] + leg_l[k], 0.7))
        s.pause(0.3)
    s.pause(0.3)
    for (k, t), lg in zip(kl, leg_r):
        schritt(s, ZEICHNE(k, 0.4), EIN([t] + lg, 0.4))
    s.speichern()


W_ZR = {"nicht": ("nicht gefunden", "not found", "no encontrado", "未找到", "introuvable", "bulunamadı"),
        "vonpaket": ("Frage vom Paket aus", "question from the package", "pregunta desde el paquete", "从软件包出发提问",
                     "question depuis le paquet", "paketten soru"),
        "vondatei": ("Frage von der Datei aus", "question from the file", "pregunta desde el archivo", "从文件出发提问",
                     "question depuis le fichier", "dosyadan soru")}


def k9zweirichtungen():
    """Dieselbe Tabelle Dateien | Paket in zwei Richtungen: oben dpkg -L grep von der Spalte Paket aus (Zeile grep
    leuchtet, ihre Dateien werden aufgezählt, Block s2_dateien); unten dpkg -S /usr/bin/ls von der Spalte Dateien aus
    (die Suche läuft durch die Zeilen und hält bei coreutils-from-uutils, Block s2_suchen) und dpkg -S /etc/hostname
    (läuft durch alle Zeilen, nicht gefunden, Block s2_nichtpaket)."""
    s = Szene("linux/k9zweirichtungen", reihenfolge="anlegen")
    w = W_ZR
    x0, y0 = -3.4, 1.85
    kopf, reihen, lagen = tabelle_dateien(s, x0, y0, [("bash", ["/usr/bin/bash ..."]), ("coreutils-from-uutils", ["/usr/bin/ls ..."]),
                                                      ("grep", ["/usr/bin/grep ..."]), ("tree", ["/usr/bin/tree ..."])],
                                          bd=1.55, bp=1.95, zh=0.24)
    xd, xp = x0 + 1.55 / 2, x0 + 1.55 + 1.95 / 2
    # oben: dpkg -L grep
    q1 = tx(s, "$ dpkg -L grep", (xp, 2.6), TK, "center", DUNKEL)
    l_q1 = L(s, "vonpaket", w["vonpaket"], (xp, 2.37), FM, "center", GRAU)
    p_q1 = pfk(s, (xp, 2.22), (xp, y0 + 0.17), ORANGE, 2.5)
    m_grep = box(s, (x0 + 1.75, lagen[2]["mitte"]), 3.5, lagen[2]["oben"] - lagen[2]["unten"], ORANGE, ORANGE, 0,
                 "rect", deckung=0.25)
    liste = ["/.", "/usr", "/usr/bin", "/usr/bin/egrep", "/usr/bin/fgrep", "/usr/bin/grep", "/usr/bin/rgrep"]
    xl, yl = 1.15, 2.6
    aus1 = [tx(s, z, (xl, r4(yl - i * 0.2)), TK, "left") for i, z in enumerate(liste)] + \
        [txa(s, PUNKTE, (xl, r4(yl - len(liste) * 0.2)), TK, "left")]
    p_aus1 = pfk(s, (0.15, lagen[2]["mitte"]), (xl - 0.12, r4(yl - 4 * 0.2)), ORANGE, 2.5)
    # unten: dpkg -S
    yq = -0.15
    q2 = tx(s, "$ dpkg -S /usr/bin/ls", (x0, yq), TK, "left", DUNKEL)
    l_q2 = L(s, "vondatei", w["vondatei"], (x0 + ttb("$ dpkg -S /usr/bin/ls") + 0.15, yq), FM, "left", GRAU)
    p_q2 = pfk(s, (xd, yq + 0.13), (xd, lagen[3]["unten"] - 0.03), BLAU, 2.5)
    hz = lagen[0]["oben"] - lagen[0]["unten"]
    such = box(s, (xd, lagen[0]["mitte"]), 1.5, hz - 0.04, BLAU, WEISS, 3, deckung=0.0)
    treffer = [box(s, (xd, lagen[1]["mitte"]), 1.5, hz - 0.04, GRUEN, WEISS, 3, deckung=0.0),
               box(s, (xp, lagen[1]["mitte"]), 1.9, hz - 0.04, GRUEN, WEISS, 3, deckung=0.0)]
    aus2 = tx(s, "coreutils-from-uutils: /usr/bin/ls", (x0, yq - 0.27), TK, "left", GRUEN)
    yq3 = yq - 0.7
    q3 = tx(s, "$ dpkg -S /etc/hostname", (x0, yq3), TK, "left", DUNKEL)
    such3 = box(s, (xd, lagen[0]["mitte"]), 1.5, hz - 0.04, ROT, WEISS, 3, deckung=0.0)
    aus3 = tx(s, "dpkg-query: no path found matching pattern /etc/hostname", (x0, yq3 - 0.27), TK, "left", ROT)
    l_nicht = L(s, "nicht", w["nicht"], (x0 + ttb("$ dpkg -S /etc/hostname") + 0.15, yq3), FM, "left", ROT)
    schritt(s, EIN(kopf + flach(reihen), 0.7))
    s.pause(0.4)
    schritt(s, EIN([q1, l_q1], 0.5), ZEICHNE(p_q1, 0.5))
    schritt(s, EIN(m_grep, 0.5))
    schritt(s, ZEICHNE(p_aus1, 0.5), EIN(aus1, 0.7))
    s.pause(0.6)
    schritt(s, EIN([q2, l_q2], 0.5), ZEICHNE(p_q2, 0.5))
    schritt(s, EIN(such, 0.3))
    schritt(s, VER(such, 0, -hz, 0.5))
    schritt(s, EIN(treffer + [aus2], 0.5), AUS(such, 0.4))
    s.pause(0.6)
    schritt(s, EIN(q3, 0.5))
    schritt(s, EIN(such3, 0.3))
    schritt(s, VER(such3, 0, -3 * hz, 1.2))
    schritt(s, VER(such3, 0, -hz, 0.3), AUS(such3, 0.3))
    schritt(s, EIN([aus3, l_nicht], 0.5))
    s.speichern()


W_SK = {"inst": ("Installieren", "installing", "instalar", "安装", "installation", "kurma"),
        "entf": ("Entfernen", "removing", "quitar", "删除", "suppression", "kaldırma"),
        "b1": ("vor dem Auspacken", "before unpacking", "antes de desempaquetar", "解包之前", "avant le dépaquetage",
               "açmadan önce"),
        "b2": ("Dateien auspacken,\nin paket.list\neintragen", "unpack files,\nrecord in\npackage.list",
               "desempaquetar,\nanotar en\npaquete.list", "解包文件，\n记入 软件包.list", "dépaqueter,\nnoter dans\npaquet.list",
               "dosyaları aç,\npaket.list'e\nyaz"),
        "b3": ("einrichten, etwa einen\nDienst anmelden", "set up, e.g. register\na service", "configurar, p. ej.\nregistrar un servicio",
               "进行设置，\n例如注册服务", "configurer, p. ex.\ninscrire un service", "kurulum, ör. bir\nhizmeti kaydetmek"),
        "b4": ("etwa den Dienst\nanhalten", "e.g. stop\nthe service", "p. ej. detener\nel servicio", "例如停止服务",
               "p. ex. arrêter\nle service", "ör. hizmeti\ndurdurmak"),
        "b5": ("Dateien aus\npaket.list löschen;\nKonfigurations-\ndateien bleiben",
               "delete files in\npackage.list;\nconfiguration\nfiles stay",
               "borrar archivos\nde paquete.list;\nla configuración\nqueda", "删除 软件包.list\n中的文件；\n配置文件保留",
               "supprimer les\nfichiers de\npaquet.list ; la\nconfiguration reste", "paket.list'teki\ndosyaları sil;\nyapılandırma\ndosyaları kalır"),
        "b6": ("nach dem Löschen", "after deleting", "después de borrar", "删除之后", "après la suppression", "sildikten sonra")}


def k9skripte():
    """Zwei Zeitleisten: Installieren (preinst als root → auspacken und in paket.list eintragen → postinst) und Entfernen
    (prerm → Dateien aus paket.list löschen, Konfigurationsdateien bleiben → postrm). Rechts die Dateien von cron in
    /var/lib/dpkg/info (Block s2_info); beim jeweiligen Schritt leuchten sie auf und bekommen dessen Nummer."""
    s = Szene("linux/k9skripte", reihenfolge="anlegen")
    w = W_SK
    xs, bb, hb = (-2.55, -0.93, 0.69), 1.45, 0.9
    y1, y2 = 1.85, 0.05
    kopf = [L(s, "inst", w["inst"], (-3.35, y1 + 0.72), FM, "left", DUNKEL), L(s, "entf", w["entf"], (-3.35, y2 + 0.72), FM,
                                                                                "left", DUNKEL)]
    kaesten, rahmen_ = [], []
    inhalt = [("preinst", "b1"), (None, "b2"), ("postinst", "b3"), ("prerm", "b4"), (None, "b5"), ("postrm", "b6")]
    for k, (skript, key) in enumerate(inhalt):
        x, y = xs[k % 3], (y1 if k < 3 else y2)
        teile = [box(s, (x, y), bb, hb, BLAU if skript else DUNKEL, BLAU_HELL if skript else WEISS, 2, "rect"),
                 text(s, str(k + 1), (r4(x - bb / 2 + 0.12), r4(y + hb / 2 - 0.13)), FM, "center", ORANGE)]
        if skript:
            teile.append(tx(s, skript, (x - (0.22 if k == 0 else 0), y + 0.2), TT, "center", BLAU))
            teile.append(L(s, key, w[key], (x, y - 0.14), FM, "center"))
        else:
            teile.append(L(s, key, w[key], (x, y), FM, "center"))
        if k == 0:
            teile += chip(s, (x + 0.42, y + 0.2), "root", ORANGE, ORANGE_HELL, h=0.22, dicke=1.5)
        kaesten.append(teile)
        rahmen_.append(box(s, (x, y), bb + 0.1, hb + 0.1, ORANGE, WEISS, 3.5, deckung=0.0))
    pfeile = [pfk(s, (xs[i] + bb / 2 + 0.01, y), (xs[i + 1] - bb / 2 - 0.01, y), DUNKEL, 2.5, spitze=0.08)
              for y in (y1, y2) for i in range(2)]
    dateien = ["cron.conffiles", "cron.list", "cron.md5sums", "cron.postinst", "cron.postrm", "cron.preinst", "cron.prerm"]
    xf, yf = 1.6, 2.2
    kopf_f = tx(s, "/var/lib/dpkg/info", (xf, 2.55), TK, "left", GRAU)
    d_ids = {d: tx(s, d, (xf, r4(yf - i * 0.29)), TK, "left") for i, d in enumerate(dateien)}
    zu = {1: ["cron.preinst"], 2: ["cron.list", "cron.md5sums", "cron.conffiles"], 3: ["cron.postinst"], 4: ["cron.prerm"],
          5: ["cron.list", "cron.conffiles"], 6: ["cron.postrm"]}
    zaehler = {d: 0 for d in dateien}
    marken = {}
    for k, ds in zu.items():
        marken[k] = []
        for d in ds:
            i = dateien.index(d)
            marken[k].append(text(s, str(k), (r4(xf + 1.25 + 0.2 * zaehler[d]), r4(yf - i * 0.29)), FM, "center", ORANGE))
            zaehler[d] += 1
    schritt(s, EIN(kopf[:1] + flach(kaesten[:3]) + pfeile[:2], 0.7))
    schritt(s, EIN(kopf[1:] + flach(kaesten[3:]) + pfeile[2:], 0.7))
    schritt(s, EIN([kopf_f] + list(d_ids.values()), 0.6))
    s.pause(0.6)
    vorher = None
    for k in range(1, 7):
        teile = [EIN([rahmen_[k - 1]] + marken[k], 0.5), BETONE([d_ids[d] for d in zu[k]], 0.7)]
        if vorher is not None:
            teile.append(AUS(vorher, 0.4))
        schritt(s, *teile)
        s.pause(0.4)
        vorher = rahmen_[k - 1]
    s.speichern()


# ================================================================== Abschnitt 3: Paketquellen und Paketlisten
W_QU = {"lager": ("Paketquelle", "repository", "repositorio", "软件源", "dépôt", "paket deposu"),
        "regale": ("Paketdateien, nach Anfangsbuchstaben", "package files, by first letter", "archivos, por letra inicial",
                   "软件包文件，按首字母", "fichiers, par première lettre", "paket dosyaları, baş harfe göre"),
        "kataloge": ("Listen, je Ausgabe", "lists, per suite", "listas, por versión", "列表，按发行套件", "listes, par version",
                     "listeler, sürüme göre"),
        "eintrag": ("Eintrag in der Liste", "entry in the list", "entrada de la lista", "列表中的条目", "entrée de la liste",
                    "listedeki kayıt")}


def regal(s, x, y, buchstabe, b=0.46, h=0.5, farbe=GRAU, fuellung=WEISS):
    """Regal: Kasten mit zwei Brettern und dem Anfangsbuchstaben darüber."""
    return [box(s, (x, y), b, h, farbe, fuellung, 2, "rect"), lin(s, (x - b / 2, y + h / 6), (x + b / 2, y + h / 6), farbe, 1.5),
            lin(s, (x - b / 2, y - h / 6), (x + b / 2, y - h / 6), farbe, 1.5), tx(s, buchstabe, (x, y + h / 2 + 0.13), TK)]


def k9quelle():
    """Paketquelle als Lagerhaus: links pool/main mit Regalen nach Anfangsbuchstaben, im Fach h/hello die Paketdatei;
    rechts dists mit den Listen je Ausgabe (resolute, -updates, -security), darin je Bereich und Architektur. Der Eintrag
    von hello (Package, Version, Filename) leuchtet, ein Pfeil führt ins Regal h."""
    s = Szene("linux/k9quelle", reihenfolge="anlegen")
    w = W_QU
    haus = [box(s, (0, 0.6), 6.9, 3.1, DUNKEL, WEISS, 2.5, "rect"),
            s.vieleck(None, [(-3.45, 2.15), (0.0, 2.85), (3.45, 2.15)], farbe=GRAU_HELL, deckung=1.0, dicke=2.5, randfarbe=DUNKEL),
            tx(s, "http://archive.ubuntu.com/ubuntu/", (0, 2.38), TK), L(s, "lager", w["lager"], (2.2, 2.62), FM, "left", GRAU)]
    links = [tx(s, "pool/main/", (-3.3, 1.92), TT, "left", BLAU), L(s, "regale", w["regale"], (-3.3, 1.67), FM, "left", GRAU)]
    bs = ["a", "b", "…", "h", "…", "z"]
    xr0, yr = -3.0, 1.0
    regale = [regal(s, r4(xr0 + i * 0.55), yr, c) for i, c in enumerate(bs)]
    xh = r4(xr0 + 3 * 0.55)
    h_gross = [box(s, (-1.85, 0.0), 3.0, 0.62, BLAU, BLAU_HELL, 2.5, "rect"), tx(s, "h/hello/", (-3.25, 0.15), TK, "left", BLAU),
               tx(s, HELLO_DEB, (-1.75, -0.12), TK, "center")]
    zoom = [lin(s, (xh - 0.23, yr - 0.25), (-3.35, 0.31), BLAU, 1.5, "4,4"), lin(s, (xh + 0.23, yr - 0.25), (-0.35, 0.31), BLAU, 1.5, "4,4")]
    h_mark = box(s, (xh, yr), 0.5, 0.54, BLAU, BLAU, 0, "rect", deckung=0.3)
    rechts = [tx(s, "dists/", (0.2, 1.92), TT, "left", BLAU), L(s, "kataloge", w["kataloge"], (0.2, 1.67), FM, "left", GRAU)]
    kat = []
    for i, (n, y) in enumerate((("resolute", 1.32), ("resolute-updates", 0.47), ("resolute-security", 0.17))):
        kat += chip(s, (r4(0.25 + chipb(n) / 2), y), n, DUNKEL, GRAU_HELL, h=0.26)
    unter = [tx(s, "main/binary-amd64/Packages", (0.45, 1.08), TK, "left"), tx(s, "universe/binary-amd64/Packages", (0.45, 0.88), TK, "left"),
             txa(s, PUNKTE, (0.45, 0.68), TK, "left")]
    yk = -0.45
    karte = [box(s, (1.8, yk - 0.05), 3.05, 0.78, ORANGE, ORANGE_HELL, 2, "rect"),
             tx(s, "Package: hello", (0.4, yk + 0.2), TK, "left"), tx(s, "Version: 2.10-5build1", (0.4, yk - 0.02), TK, "left"),
             tx(s, "Filename: pool/main/h/hello/…", (0.4, yk - 0.24), TK, "left"),
             L(s, "eintrag", w["eintrag"], (3.25, yk + 0.2), FM, "right", GRAU)]
    zoom2 = lin(s, (0.45 + ttb("main/binary-amd64/Packages") + 0.05, 1.08), (3.1, yk + 0.33), ORANGE, 1.5, "4,4")
    m_fn = box(s, (0.4 + ttb("Filename: pool/main/h/hello/…") / 2, yk - 0.24), ttb("Filename: pool/main/h/hello/…") + 0.08, 0.2,
               ORANGE, ORANGE, 0, "rect", deckung=0.35)
    p_fn = pfk(s, (0.33, yk - 0.24), (-0.3, -0.12), ORANGE, 2.5, spitze=0.1)
    schritt(s, EIN(haus, 0.7))
    schritt(s, EIN(links + flach(regale), 0.6))
    schritt(s, EIN(rechts + kat + unter, 0.6))
    s.pause(0.6)
    schritt(s, ZEICHNE(zoom2, 0.5), EIN(karte, 0.6))
    schritt(s, EIN(m_fn, 0.5))
    schritt(s, ZEICHNE(p_fn, 0.6), EIN(h_mark, 0.6))
    schritt(s, ZEICHNE(zoom, 0.5), EIN(h_gross, 0.6))
    s.speichern()


W_SP = {"haupt": ("Hauptquelle von Ubuntu", "Ubuntu's main repository", "repositorio principal de Ubuntu", "Ubuntu 主软件源",
                  "dépôt principal d'Ubuntu", "Ubuntu ana deposu"),
        "s1": ("Spiegel\nUniversität", "mirror\nuniversity", "espejo\nuniversidad", "镜像\n大学", "miroir\nuniversité",
               "yansı\nüniversite"),
        "s2": ("Spiegel\nFirma", "mirror\ncompany", "espejo\nempresa", "镜像\n公司", "miroir\nentreprise", "yansı\nşirket"),
        "s3": ("Spiegel\nVerein", "mirror\nassociation", "espejo\nasociación", "镜像\n协会", "miroir\nassociation",
               "yansı\ndernek"),
        "kopie": ("Uhr: letzte Kopie", "clock: last copy", "reloj: última copia", "时钟：上次复制", "horloge : dernière copie",
                  "saat: son kopya"),
        "rechner": ("Rechner", "computers", "ordenadores", "计算机", "ordinateurs", "bilgisayarlar"),
        "update": ("neues Sicherheitsupdate", "new security update", "nueva actualización de seguridad", "新的安全更新",
                   "nouvelle mise à jour de sécurité", "yeni güvenlik güncellemesi"),
        "sofort": ("sofort an alle Rechner", "to all computers at once", "a todos los ordenadores enseguida",
                   "立即发往所有计算机", "tout de suite à tous les ordinateurs", "hemen tüm bilgisayarlara"),
        "spaeter": ("Spiegel: erst bei der nächsten Kopie", "mirrors: only at their next copy", "espejos: solo en la próxima copia",
                    "镜像：下次复制时才有", "miroirs : seulement à la prochaine copie", "yansılar: ancak bir sonraki kopyada")}


def rechner(s, x, y):
    """Kleiner Rechner: Bildschirm und Fuß (Ergebnis: Liste)."""
    return [box(s, (x, y + 0.04), 0.42, 0.28, DUNKEL, WEISS, 2, "rect"), lin(s, (x, y - 0.1), (x, y - 0.17), DUNKEL, 2.5),
            lin(s, (x - 0.12, y - 0.17), (x + 0.12, y - 0.17), DUNKEL, 2.5)]


def k9spiegel():
    """Oben die Hauptquelle von Ubuntu (archive.ubuntu.com, security.ubuntu.com), darunter drei Spiegel (Universität,
    Firma, Verein) mit Uhr „letzte Kopie“, darunter Rechner, die beim nächsten Spiegel holen. Ein neues
    Sicherheitsupdate erscheint bei security.ubuntu.com und erreicht über den direkten Weg sofort alle Rechner; die
    Spiegel bekommen es erst bei ihrer nächsten Kopie (Uhr dreht weiter)."""
    s = Szene("linux/k9spiegel", reihenfolge="anlegen")
    w = W_SP
    haupt = [box(s, (0, 2.3), 3.9, 0.62, BLAU, BLAU_HELL, 2.5, "rect"), L(s, "haupt", w["haupt"], (0, 2.8), FM, "center", BLAU)]
    arch = chip(s, (-0.92, 2.3), "archive.ubuntu.com", BLAU, WEISS)
    sec = chip(s, (0.92, 2.3), "security.ubuntu.com", BLAU, WEISS)
    xs, ym, yc = (-2.35, 0.0, 2.35), 1.05, -0.35
    spiegel, uhren, kopien, rech, zu_r = [], [], [], [], []
    for i, x in enumerate(xs):
        spiegel += [box(s, (x, ym), 1.7, 0.6, GRAU, WEISS, 2, "rect"), L(s, "s%d" % (i + 1), w["s%d" % (i + 1)], (x + 0.18, ym), FM)]
        uhren.append(uhr(s, r4(x - 0.58), ym, (3, 7, 10)[i], 0, r=0.17))
        kopien.append(pfk(s, (-0.92 + (x + 0.92) * 0.15, 2.15), (x, ym + 0.32), GRAU, 2, "6,4"))
        for dx in (-0.4, 0.4):
            rech += rechner(s, r4(x + dx), yc)
            zu_r.append(pfk(s, (x + dx * 0.4, ym - 0.31), (x + dx, yc + 0.2), GRAU, 1.5))
    l_kopie = L(s, "kopie", w["kopie"], (-3.4, ym + 0.48), FM, "left", GRAU)
    # Sicherheitsupdate: direkter Weg über security.ubuntu.com
    upd = s.punkt(None, 1.72, 2.48, ORANGE, 0.09)
    l_upd = L(s, "update", w["update"], (3.42, 2.8), FM, "right", ORANGE)
    yb = yc - 0.62
    l_rech = L(s, "rechner", w["rechner"], (-3.4, yb - 0.22), FM, "left", GRAU)
    weg = [lin(s, (1.81, 2.3), (3.38, 2.3), ORANGE, 3), lin(s, (3.38, 2.3), (3.38, yb), ORANGE, 3),
           lin(s, (3.38, yb), (-2.75, yb), ORANGE, 3)]
    hoch = [pfk(s, (x + dx, yb), (x + dx, yc - 0.21), ORANGE, 2.5, spitze=0.07) for x in xs for dx in (-0.4, 0.4)]
    an_r = [s.punkt(None, r4(x + dx), r4(yc + 0.04), ORANGE, 0.07) for x in xs for dx in (-0.4, 0.4)]
    l_sofort = L(s, "sofort", w["sofort"], (0.6, yb - 0.22), FM, "center", ORANGE)
    an_s = [s.punkt(None, r4(x + 0.7), r4(ym + 0.18), ORANGE, 0.07) for x in xs]
    l_spaeter = L(s, "spaeter", w["spaeter"], (0.6, yb - 0.46), FM, "center", GRAU)
    schritt(s, EIN(haupt + arch + sec, 0.7))
    schritt(s, ZEICHNE(kopien, 0.7), EIN(spiegel + flach(uhren) + [l_kopie], 0.7))
    schritt(s, ZEICHNE(zu_r, 0.6), EIN(rech + [l_rech], 0.6))
    s.pause(0.6)
    schritt(s, WACHS(upd, 0.5), EIN(l_upd, 0.5))
    schritt(s, ZEICHNE(weg, 1.0))
    schritt(s, ZEICHNE(hoch, 0.5), WACHS(an_r, 0.5), EIN(l_sofort, 0.5))
    s.pause(0.5)
    for i, x in enumerate(xs):
        k, zh, zm = uhren[i]
        schritt(s, DREH(zm, -360, (x - 0.58, ym), 0.6), WACHS(an_s[i], 0.6), *([EIN(l_spaeter, 0.6)] if i == 0 else []))
    s.speichern()


W_AU = {"start": ("23.04.2026", "23 Apr 2026", "23/04/2026", "2026-04-23", "23/04/2026", "23.04.2026"),
        "heute": ("12.11.2026", "12 Nov 2026", "12/11/2026", "2026-11-12", "12/11/2026", "12.11.2026"),
        "fest": ("fester Stand vom Erscheinungstag", "fixed state of the release day", "estado fijo del día de publicación",
                 "发布当天的固定状态", "état figé du jour de sortie", "çıkış günündeki sabit durum"),
        "neue": ("neue Version", "new version", "nueva versión", "新版本", "nouvelle version", "yeni sürüm"),
        "blass": ("neuere Programme, wenig geprüft", "newer programs, little tested", "programas más nuevos, poco probados",
                  "较新的程序，测试较少", "programmes plus récents, peu testés", "daha yeni programlar, az test edilmiş"),
        "bereiche": ("in jeder Ausgabe\nvier Bereiche", "four components\nin every suite", "cuatro componentes\nen cada versión",
                     "每个发行套件\n都有四个组件", "quatre sections\ndans chaque version", "her sürümde\ndört bileşen"),
        "zeit": ("Zeit", "time", "tiempo", "时间", "temps", "zaman")}


def k9ausgaben():
    """Zeitachse vom 23.04.2026 bis heute: resolute ist ein fester Block am Anfang (danach unverändert);
    resolute-updates und resolute-security wachsen, sudo-rs bekommt darin eine neue Version; resolute-backports blass.
    Rechts die vier Bereiche main, restricted, universe, multiverse als Schichten jeder Ausgabe."""
    s = Szene("linux/k9ausgaben", reihenfolge="anlegen")
    w = W_AU
    x0, x1 = -1.45, 1.55
    reihen = {"resolute-backports": 2.0, "resolute-security": 1.4, "resolute-updates": 0.8, "resolute": 0.2}
    namen = [tx(s, n, (-1.62, y), TK, "right", GRAU if n.endswith("backports") else SCHWARZ) for n, y in reihen.items()]
    ya = -0.3
    achse = [pfk(s, (x0, ya), (x1 + 0.2, ya), GRAU, 2.5, spitze=0.1), lin(s, (x0, ya - 0.06), (x0, ya + 0.06), GRAU, 2),
             lin(s, (x1, ya - 0.06), (x1, ya + 0.06), GRAU, 2),
             L(s, "start", w["start"], (x0, ya - 0.25), FM, "center", DUNKEL), L(s, "heute", w["heute"], (x1, ya - 0.25), FM, "center",
                                                                                 DUNKEL),
             L(s, "zeit", w["zeit"], (x1 + 0.2, ya + 0.22), FM, "right", GRAU)]
    yr = reihen["resolute"]
    block = box(s, (x0 + 0.17, yr), 0.34, 0.3, BLAU, BLAU, 0, "rect")
    rest = lin(s, (x0 + 0.34, yr), (x1, yr), BLAU, 2, "3,5")
    l_fest = L(s, "fest", w["fest"], (x0 + 0.45, yr - 0.27), FM, "left", BLAU)
    spur = {"resolute-updates": (GRUEN, GRUEN_HELL), "resolute-security": (ORANGE, ORANGE_HELL),
            "resolute-backports": (HELLGRAU, GRAU_HELL)}
    balken, punkte = [], []
    for n, (f, fh) in spur.items():
        y = reihen[n]
        balken.append(lin(s, (x0 + 0.34, y), (x1, y), f, 14))
        if n != "resolute-backports":
            punkte += [s.punkt(None, r4(x0 + 0.34 + k * 0.38 + (0.12 if n.endswith("security") else 0)), y, WEISS, 0.045)
                       for k in range(1, 8)]
    xs = r4(x1 - 0.2)
    sudo = [s.punkt(None, xs, reihen["resolute-security"], DUNKEL, 0.07), tx(s, "sudo-rs", (xs, reihen["resolute-security"] + 0.25),
                                                                             TK, "center", DUNKEL),
            L(s, "neue", w["neue"], (xs - 0.45, reihen["resolute-security"] + 0.25), FM, "right", GRAU)]
    l_blass = L(s, "blass", w["blass"], (x0 + 0.4, reihen["resolute-backports"] + 0.27), FM, "left", GRAU)
    kl = vklammer(s, 1.92, 2.15, 0.05, GRAU, 0.08, 2)
    p_kl = pfk(s, (1.95, 1.1), (2.18, 1.1), GRAU, 2, spitze=0.07)
    schichten = []
    for i, (n, f) in enumerate((("main", BLAU_HELL), ("restricted", GRAU_HELL), ("universe", GRUEN_HELL), ("multiverse", GELB))):
        y = r4(1.55 - i * 0.3)
        schichten += [box(s, (2.85, y), 1.25, 0.3, GRAU, f, 1.5, "rect"), tx(s, n, (2.85, y), TK)]
    l_ber = L(s, "bereiche", w["bereiche"], (2.85, 2.0), FM, "center", GRAU)
    schritt(s, EIN(namen + achse, 0.7))
    schritt(s, WACHS(block, 0.5), EIN(l_fest, 0.5))
    schritt(s, ZEICHNE(rest, 0.6))
    s.pause(0.4)
    schritt(s, ZEICHNE(balken[:2], 1.8), EIN(punkte, 1.8))
    schritt(s, EIN(sudo, 0.6))
    schritt(s, ZEICHNE(balken[2:], 1.0), EIN(l_blass, 1.0))
    s.pause(0.6)
    schritt(s, ZEICHNE(kl, 0.5), ZEICHNE(p_kl, 0.5), EIN(schichten + [l_ber], 0.6))
    s.speichern()


QUELLEN = ["Types: deb", "URIs: http://archive.ubuntu.com/ubuntu/", "Suites: resolute resolute-updates resolute-backports",
           "Components: main universe restricted multiverse", "Signed-By: /usr/share/keyrings/ubuntu-archive-keyring.gpg", "",
           "Types: deb", "URIs: http://security.ubuntu.com/ubuntu/", "Suites: resolute-security",
           "Components: main universe restricted multiverse", "Signed-By: /usr/share/keyrings/ubuntu-archive-keyring.gpg"]
W_QL = {"adresse": ("Adresse einer Paketliste:", "address of one package list:", "dirección de una lista de paquetes:",
                    "一个软件包列表的地址：", "adresse d'une liste de paquets :", "bir paket listesinin adresi:"),
        "uris": ("aus URIs", "from URIs", "de URIs", "来自 URIs", "de URIs", "URIs'ten"),
        "fest": ("fest", "fixed", "fijo", "固定", "fixe", "sabit"),
        "suites": ("aus Suites", "from Suites", "de Suites", "来自 Suites", "de Suites", "Suites'ten"),
        "comp": ("aus Components", "from Components", "de Components", "来自 Components", "de Components", "Components'ten"),
        "arch": ("Architektur", "architecture", "arquitectura", "架构", "architecture", "mimari"),
        "e1": ("3 × 4 = 12 Listen", "3 × 4 = 12 lists", "3 × 4 = 12 listas", "3 × 4 = 12 个列表", "3 × 4 = 12 listes",
               "3 × 4 = 12 liste"),
        "e1b": ("Ausgaben × Bereiche", "suites × components", "versiones × componentes", "套件 × 组件", "versions × sections",
                "sürümler × bileşenler"),
        "e2": ("1 × 4 = 4 Listen", "1 × 4 = 4 lists", "1 × 4 = 4 listas", "1 × 4 = 4 个列表", "1 × 4 = 4 listes", "1 × 4 = 4 liste"),
        "summe": ("zusammen 16 Listen", "16 lists in total", "16 listas en total", "共 16 个列表", "16 listes en tout",
                  "toplam 16 liste"),
        "schl": ("Signed-By: Schlüssel", "Signed-By: key", "Signed-By: clave", "Signed-By：密钥", "Signed-By : clé",
                 "Signed-By: anahtar")}


def k9quellenliste():
    """ubuntu.sources (Datei-Ansicht, hell, beide Einträge aus Block s3_quellen). Aus dem ersten Eintrag entsteht Stück
    für Stück die Adresse http://archive.ubuntu.com/ubuntu/dists/resolute/main/binary-amd64/ (URIs, dists, Suites,
    Components, Architektur). Rechts: 3 Ausgaben × 4 Bereiche = 12 Listen, der zweite Eintrag 4 weitere, zusammen 16;
    Signed-By als Schloss an beiden Einträgen."""
    s = Szene("linux/k9quellenliste", reihenfolge="anlegen")
    w = W_QL
    d = s.datei("/etc/apt/sources.list.d/ubuntu.sources", "\n".join(QUELLEN), pos=(-3.45, 2.8), groesse=TK)
    xu, yu = -3.3, 0.05
    cw = tt_breite(TK, 1)
    l_adr = L(s, "adresse", w["adresse"], (xu, yu + 0.3), FM, "left", GRAU)
    # Stücke: (Zeile, Muster, Farbe, Spalte in der Adresse, Beschriftung, Ebene der Beschriftung)
    a1, b1 = d.finde(1, "http://archive.ubuntu.com/ubuntu/")
    a2, b2 = d.finde(2, "resolute")
    a3, b3 = d.finde(3, "main")
    stuecke = [(1, a1, b1, BLAU, 0, "uris", 0), (2, a2, b2, ORANGE, 39, "suites", 0), (3, a3, b3, GRUEN, 48, "comp", 1)]
    schritte_ = []
    for z, a, b, f, sp, key, eb in stuecke:
        m = d.markieren(z, a, b, f, 0.3)
        k = d.teil(z, a, b, farbe=f)
        ziel_x = xu + sp * cw
        lab = L(s, key, w[key], (ziel_x + (b - a + 1) * cw / 2, yu - 0.25 - 0.24 * eb), FM, "center", f)
        schritte_.append((m, k, VER(k, ziel_x - d.x(a), yu - d.y(z), 0.9), lab))
    fest = [tx(s, "dists/", (xu + 33 * cw, yu), TK, "left"), L(s, "fest", w["fest"], (xu + 36 * cw, yu - 0.49), FM, "center", GRAU)]
    sl1 = tx(s, "/", (xu + 47 * cw, yu), TK, "left", ORANGE)
    sl2 = tx(s, "/", (xu + 52 * cw, yu), TK, "left", GRUEN)
    arch = [tx(s, "binary-amd64/", (xu + 53 * cw, yu), TK, "left"), L(s, "arch", w["arch"], (xu + 59.5 * cw, yu - 0.25), FM,
                                                                     "center", GRAU)]
    # Zählung rechts und Schlösser
    xz = d.rechts + 0.45
    m_su = d.markieren(2, 8, len(QUELLEN[2]) - 1, ORANGE, 0.18)
    m_co = d.markieren(3, 12, len(QUELLEN[3]) - 1, GRUEN, 0.18)
    m_su2 = d.markieren(8, 8, len(QUELLEN[8]) - 1, ORANGE, 0.18)
    m_co2 = d.markieren(9, 12, len(QUELLEN[9]) - 1, GRUEN, 0.18)
    e1 = [L(s, "e1", w["e1"], (xz, d.y(2)), FM, "left"), L(s, "e1b", w["e1b"], (xz, d.y(3)), FM, "left", GRAU)]
    e2 = L(s, "e2", w["e2"], (xz, d.y(8) - 0.08), FM, "left")
    summe = L(s, "summe", w["summe"], (xz, d.y(10) - 0.12), FM, "left", DUNKEL)
    schl = [s.schloss((r4(d.rechts + 0.2), d.y(4)), 0.24, farbe=DUNKEL), s.schloss((r4(d.rechts + 0.2), d.y(10)), 0.24, farbe=DUNKEL)]
    l_schl = L(s, "schl", w["schl"], (xz, d.y(5)), FM, "left", GRAU)
    schritt(s, EIN(d.id, 0.7))
    schritt(s, EIN(l_adr, 0.4))
    for i, (m, k, ver, lab) in enumerate(schritte_):
        schritt(s, EIN([m, k], 0.5))
        schritt(s, ver)
        extra = [fest] if i == 0 else ([sl1] if i == 1 else [sl2])
        schritt(s, EIN(flach(extra) + [lab], 0.5))
    schritt(s, EIN(arch, 0.5))
    s.pause(0.6)
    schritt(s, EIN([m_su, m_co] + e1, 0.7))
    schritt(s, EIN([m_su2, m_co2, e2], 0.6))
    schritt(s, EIN(summe, 0.5))
    s.pause(0.4)
    schritt(s, WACHS(schl, 0.6), EIN(l_schl, 0.6))
    s.speichern()


W_UP = {"rechner": ("dein Rechner", "your computer", "tu ordenador", "你的计算机", "ton ordinateur", "bilgisayarın"),
        "progs": ("installierte\nProgramme", "installed\nprograms", "programas\ninstalados", "已安装的\n程序", "programmes\ninstallés",
                  "kurulu\nprogramlar"),
        "bleibt": ("unverändert", "unchanged", "sin cambios", "不变", "inchangés", "değişmez"),
        "hit": ("Hit: unverändert, behalten", "Hit: unchanged, kept", "Hit: sin cambios, se conserva", "Hit：未变，保留",
                "Hit : inchangée, gardée", "Hit: değişmedi, tutulur"),
        "get": ("Get: neu, ersetzt", "Get: new, replaced", "Get: nueva, se reemplaza", "Get：新的，替换", "Get : nouvelle, remplacée",
                "Get: yeni, değiştirilir")}


def k9update():
    """Links die Server archive.ubuntu.com und security.ubuntu.com mit ihren Listen, rechts der Rechner mit
    /var/lib/apt/lists und den installierten Programmen. apt update: resolute bleibt (Hit, Haken), resolute-security,
    -updates und -backports werden ersetzt (Get); die Programme bleiben grau und unverändert. Darunter Zeilen aus
    Block s3_update bis „126 packages can be upgraded“."""
    s = Szene("linux/k9update", reihenfolge="anlegen")
    w = W_UP
    srv_a = [box(s, (-2.3, 1.9), 2.2, 1.3, DUNKEL, WEISS, 2, "rect"), tx(s, "archive.ubuntu.com", (-2.3, 2.37), TK, "center", DUNKEL)]
    srv_s = [box(s, (-2.3, 0.65), 2.2, 0.72, DUNKEL, WEISS, 2, "rect"), tx(s, "security.ubuntu.com", (-2.3, 0.85), TK, "center", DUNKEL)]
    ys_a = {"resolute": 2.08, "resolute-updates": 1.78, "resolute-backports": 1.48}
    ys_s = {"resolute-security": 0.53}
    karten_srv = []
    for n, y in list(ys_a.items()) + list(ys_s.items()):
        karten_srv += chip(s, (-2.3, y), n, GRUEN if n != "resolute" else GRAU, WEISS, h=0.25, b=1.7)
    rech = [box(s, (1.75, 1.3), 3.35, 2.25, DUNKEL, WEISS, 2.5, "round"), L(s, "rechner", w["rechner"], (1.75, 2.62), FM, "center",
                                                                            DUNKEL),
            tx(s, "/var/lib/apt/lists", (0.32, 2.22), TK, "left", BLAU)]
    xl = 1.15
    ys_l = {"resolute": 1.95, "resolute-updates": 1.65, "resolute-backports": 1.35, "resolute-security": 1.05}
    alt = {n: chip(s, (xl, y), n, GRAU, WEISS, h=0.25, b=1.7, textfarbe=GRAU) for n, y in ys_l.items()}
    progs = [L(s, "progs", w["progs"], (2.85, 2.05), FM, "center", GRAU)]
    Z, _ = zbaum(s, 2.35, 1.6, [("/usr/bin", 0, "dir", GRAU), ("bash", 1, "datei", GRAU), ("grep", 1, "datei", GRAU),
                                ("tree", 1, "datei", GRAU)], dz=0.25, einzug=0.25, linien=HELLGRAU)
    progs += flach(Z) + [L(s, "bleibt", w["bleibt"], (2.85, 0.45), FM, "center", GRAU)]
    ok = haken(s, xl + 1.0, 1.97, GRUEN, 0.08, 3.5)
    neu, schiebe, weg_alt = [], [], []
    for n in ("resolute-security", "resolute-updates", "resolute-backports"):
        y0 = ys_a.get(n, ys_s.get(n))
        c = chip(s, (-2.3, y0), n, GRUEN, GRUEN_HELL, h=0.25, b=1.7)
        neu += c
        schiebe += VERS(c, xl + 2.3, ys_l[n] - y0, 1.2)
        weg_alt += alt[n]
    l_hit = L(s, "hit", w["hit"], (0.32, 0.66), FM, "left", GRUEN)
    l_get = L(s, "get", w["get"], (0.32, 0.42), FM, "left", GRUEN)
    zeilen = ["Hit:1 http://archive.ubuntu.com/ubuntu resolute InRelease",
              "Get:2 http://security.ubuntu.com/ubuntu resolute-security InRelease [137 kB]", PUNKTE,
              "126 packages can be upgraded. Run 'apt list --upgradable' to see them."]
    g = s.raster(zeilen, (-3.4, -0.25), groesse=TK, zeilenabstand=1.4)
    schritt(s, EIN(srv_a + srv_s + karten_srv, 0.7))
    schritt(s, EIN(rech + flach(list(alt.values())) + progs, 0.7))
    s.pause(0.6)
    schritt(s, EIN(ok + [g.ids[0], l_hit], 0.6))
    schritt(s, EIN(neu, 0.4))
    schritt(s, *schiebe, AUS(weg_alt, 1.2), EIN([g.ids[1], l_get], 1.2))
    s.pause(0.5)
    schritt(s, EIN(g.ids[2:], 0.6))
    s.speichern()


# ================================================================== Abschnitt 4: Pakete suchen und ansehen
def gr(t):
    return farbig(t, "gruen")


W_SU = {"name": ("Paketname", "package name", "nombre del paquete", "软件包名", "nom du paquet", "paket adı"),
        "ausg": ("Ausgaben, aus denen die Version stammt", "suites the version comes from", "versiones de las que viene",
                 "该版本所在的发行套件", "versions d'où vient la version", "sürümün geldiği dağıtım sürümleri"),
        "version": ("Version", "version", "versión", "版本", "version", "sürüm"),
        "arch": ("Architektur", "architecture", "arquitectura", "架构", "architecture", "mimari"),
        "treffer": ("Treffer,\negal ob groß\noder klein", "matches,\nupper or\nlower case", "coincidencias,\nmayúsculas o\nminúsculas",
                    "命中，\n不区分\n大小写", "trouvés,\nmajuscules ou\nminuscules", "eşleşmeler,\nbüyük ya da\nküçük harf")}


def k9suche():
    """Terminal: apt search 'json processor', die ersten zwei Treffer (Block s4_suchen2, Paketnamen grün), Rest „...“.
    Die Zeile von jq erscheint darunter groß und wird in Paketname, Ausgaben, Version, Architektur zerlegt; in den
    Kurzbeschreibungen werden die gefundenen Wörter markiert (JSON processor / json processor)."""
    s = Szene("linux/k9suche", reihenfolge="anlegen")
    w = W_SU
    t = s.terminal(pos=(-3.45, 2.8), spalten=70, zeilen=8, prompt=P9, titel=TITEL, groesse=18)
    schritt(s, EIN(t.id, 0.6))
    s.pause(0.3)
    t.eingabe("apt search 'json processor'")
    t.ausgabe("\n".join([gr("jq") + "/resolute-updates,resolute-security 1.8.1-4ubuntu2 amd64",
                         "  lightweight and flexible command-line JSON processor", "",
                         gr("libjackson-json-java") + "/resolute 1.9.13-2 all",
                         "  streaming fast powerful standard conformant json processor in java", PUNKTE]), dauer=0.6)
    zeile = "jq/resolute-updates,resolute-security 1.8.1-4ubuntu2 amd64"
    r_t = t.rahmen(1, 0, len(zeile) - 1, farbe=ORANGE, dicke=2.5, rand=0.0)
    xg, yg = -3.3, t.unten_kante - 0.45
    g = s.raster([farbig("jq", GRUEN) + zeile[2:]], (xg, yg), groesse=TT)
    p_g = pfk(s, (xg + 0.3, t.y(1) - 0.09), (xg + 0.3, yg + 0.14), ORANGE, 2, "4,4")
    teile = [(0, 1, "name", 0, "left"), (3, 36, "ausg", 1, "center"), (38, 51, "version", 0, "center"), (53, 57, "arch", 0, "center")]
    zerl = []
    for a, b, key, eb, ausr in teile:
        k, _ = g.klammer(0, a, b, "", seite="unten", farbe=BLAU)
        x = g.x(a) if ausr == "left" else g.xm(a, b)
        zerl.append([k, L(s, "s_" + key, w[key], (x, g.unten(0) - 0.26 - 0.25 * eb), FM, ausr, BLAU)])
    a1, b1 = t.finde(2, "JSON processor")
    a2, b2 = t.finde(5, "json processor")
    marken = [t.markieren(2, a1, b1, ORANGE, 0.45), t.markieren(5, a2, b2, ORANGE, 0.45)]
    l_tr = L(s, "treffer", w["treffer"], (t.rechts + 0.1, t.y(3)), FM, "left", ORANGE)
    s.pause(0.6)
    schritt(s, EIN(r_t, 0.5))
    schritt(s, ZEICHNE(p_g, 0.5), EIN(g.ids, 0.6))
    for k, lab in zerl:
        schritt(s, ZEICHNE(k, 0.4), EIN(lab, 0.4))
    s.pause(0.5)
    schritt(s, EIN(marken + [l_tr], 0.7))
    s.speichern()


def feld(name, wert=""):
    return fett(name + ":") + (" " + wert if wert else "")


APT_SHOW = [feld("Package", gr("hello")), feld("Version", "2.10-5build1"), feld("Priority", "optional"), feld("Section", "devel"),
            feld("Origin", "Ubuntu"), feld("Maintainer", "Ubuntu Developers <ubuntu-devel-discuss@lists.ubuntu.com>"),
            feld("Original-Maintainer", "Santiago Vila <sanvila@debian.org>"),
            feld("Bugs", "https://bugs.launchpad.net/ubuntu/+filebug"), feld("Installed-Size", "106 kB"),
            feld("Depends", "libc6 (>= 2.38)"), feld("Conflicts", "hello-traditional"), feld("Breaks", "hello-debhelper (<< 2.9)"),
            feld("Replaces", "hello-debhelper (<< 2.9), hello-traditional"), feld("Homepage", "https://www.gnu.org/software/hello/"),
            feld("Download-Size", "26.1 kB"), feld("APT-Sources", "http://archive.ubuntu.com/ubuntu resolute/main amd64 Packages"),
            feld("Description", "example package based on GNU hello"), PUNKTE]
W_SH = [("so viel Platz nach dem Installieren: 104 KiB", "space used after installing: 104 KiB",
         "espacio ocupado tras instalar: 104 KiB", "安装后占用的空间：104 KiB", "place occupée après l'installation : 104 Kio",
         "kurulumdan sonra kapladığı yer: 104 KiB"),
        ("so groß ist die Paketdatei", "size of the package file", "tamaño del archivo de paquete", "软件包文件的大小",
         "taille du fichier de paquet", "paket dosyasının boyutu"),
        ("aus dieser Paketliste: resolute/main", "from this package list: resolute/main", "de esta lista: resolute/main",
         "来自这个软件包列表：resolute/main", "de cette liste : resolute/main", "bu paket listesinden: resolute/main"),
        ("schon installiert", "already installed", "ya instalado", "已安装", "déjà installé", "zaten kurulu")]


def k9show():
    """Terminal: apt show hello (Block s4_zeigen bis zur Kopfzeile Description, Feldnamen fett, hello grün). Nacheinander
    werden Installed-Size (1), Download-Size (2) und APT-Sources (3) gerahmt und links nummeriert, die Erklärungen stehen
    darunter; zuletzt Depends: libc6 (>= 2.38) mit grünem Haken „schon installiert“."""
    s = Szene("linux/k9show", reihenfolge="anlegen")
    t = s.terminal(pos=(-3.11, 2.85), spalten=80, prompt=P9, titel=TITEL, groesse=18)
    schritt(s, EIN(t.id, 0.6))
    s.pause(0.3)
    t.eingabe("apt show hello")
    t.ausgabe("\n".join(APT_SHOW), dauer=0.7)
    zeilen = [9, 15, 16, 10]
    xn = -3.28
    yl = (r4(t.unten_kante - 0.27), r4(t.unten_kante - 0.54))
    schritte_ = []
    for k, z in enumerate(zeilen):
        n = len(t.zeilen()[z].rstrip())
        fr = t.rahmen(z, 0, n - 1, farbe=ORANGE if k < 3 else "#33da7a", dicke=2.5, rand=0.0)
        zeichen = text(s, str(k + 1), (xn, t.y(z)), FM, "center", ORANGE) if k < 3 else None
        xl, y = (-3.35, yl[k]) if k < 2 else (0.35, yl[k - 2])
        if k < 3:
            leg = [text(s, str(k + 1), (xl, y), FM, "left", ORANGE), L(s, "sh%d" % k, W_SH[k], (r4(xl + 0.2), y), FM, "left")]
        else:
            leg = haken(s, xl + 0.08, y, GRUEN, 0.08, 3.5) + [L(s, "sh3", W_SH[3], (r4(xl + 0.24), y), FM, "left", GRUEN)]
            zeichen = haken(s, t.xr(n) + 0.18, t.y(z), "#33da7a", 0.07, 3.5)
        schritte_.append(([fr] + flach(zeichen), leg))
    s.pause(0.8)
    for teile, leg in schritte_:
        schritt(s, EIN(teile + leg, 0.6))
        s.pause(0.5)
    s.speichern()


W_LI = {"name": ("Name", "name", "nombre", "名称", "nom", "ad"),
        "ausg": ("Ausgaben", "suites", "versiones", "发行套件", "versions", "sürümler"),
        "version": ("Version", "version", "versión", "版本", "version", "sürüm"),
        "arch": ("Architektur", "architecture", "arquitectura", "架构", "architecture", "mimari"),
        "zustand": ("Zustand", "state", "estado", "状态", "état", "durum"),
        "now": ("now und [installed]: auf diesem Rechner", "now and [installed]: on this computer", "now y [installed]: en este equipo",
                "now 与 [installed]：在本机上", "now et [installed] : sur cette machine", "now ve [installed]: bu bilgisayarda"),
        "leer": ("leer: nicht installiert", "empty: not installed", "vacío: no instalado", "空：未安装", "vide : non installé",
                 "boş: kurulu değil"),
        "ii": ("Pakete mit ii", "packages with ii", "paquetes con ii", "带 ii 的软件包", "paquets avec ii", "ii olan paketler"),
        "plus": ("+ 629 Pakete = 630 Zeilen", "+ 629 packages = 630 lines", "+ 629 paquetes = 630 líneas", "+ 629 个软件包 = 630 行",
                 "+ 629 paquets = 630 lignes", "+ 629 paket = 630 satır")}


def k9liste():
    """Terminal: apt list hello grep jq (Block s4_liste, Namen grün). Die Zeilen von grep und hello erscheinen darunter
    groß; bei grep werden Name, Ausgaben, Version, Architektur, Zustand beschriftet, now und [installed] leuchten, bei hello
    bleibt die Stelle leer. Darunter die Zählung 629 (dpkg -l | grep -c '^ii') gegen 630 (apt list --installed | wc -l),
    die zusätzliche Zeile Listing... rot."""
    s = Szene("linux/k9liste", reihenfolge="anlegen")
    w = W_LI
    t = s.terminal(pos=(-3.45, 2.85), spalten=60, zeilen=5, prompt=P9, titel=TITEL, groesse=18)
    schritt(s, EIN(t.id, 0.6))
    s.pause(0.3)
    t.befehl("apt list hello grep jq", "\n".join([gr("grep") + "/resolute,now 3.12-1 amd64 [installed]",
                                                    gr("hello") + "/resolute 2.10-5build1 amd64",
                                                    gr("jq") + "/resolute-updates,resolute-security 1.8.1-4ubuntu2 amd64"]), pfad=PFAD)
    z_grep = "grep/resolute,now 3.12-1 amd64 [installed]"
    z_hello = "hello/resolute 2.10-5build1 amd64"
    xg = -3.3
    yg1, yg2 = 0.88, 0.38
    g1 = s.raster([farbig("grep", GRUEN) + z_grep[4:]], (xg, yg1), groesse=TT)
    g2 = s.raster([farbig("hello", GRUEN) + z_hello[5:]], (xg, yg2), groesse=TT)
    teile = [(0, 3, "name", 0), (5, 16, "ausg", 1), (18, 23, "version", 0), (25, 29, "arch", 1), (31, 41, "zustand", 0)]
    zerl = []
    for a, b, key, eb in teile:
        k, _ = g1.klammer(0, a, b, "", seite="oben", farbe=BLAU)
        zerl.append([k, L(s, "l_" + key, w[key], (g1.xm(a, b), g1.oben(0) + 0.24 + 0.24 * eb), FM, "center", BLAU)])
    a_now, b_now = g1.finde(0, "now")
    m_now = [g1.markieren(0, a_now, b_now, ORANGE, 0.4), g1.markieren(0, 31, 41, ORANGE, 0.4)]
    l_now = L(s, "now", w["now"], (g1.xr(41) + 0.15, yg1), FM, "left", ORANGE)
    leer = [box(s, (g2.xm(34, 44), yg2), (11 * g2.zelle[0]), 0.22, GRAU, WEISS, 1.5, "rect", "4,4", 0.0),
            L(s, "leer", w["leer"], (g2.xr(44) + 0.15, yg2), FM, "left", GRAU)]
    # Zählung
    yz = -0.3
    c1 = s.raster(["$ dpkg -l | grep -c '^ii'", "629"], (xg, yz), groesse=TK, zeilenabstand=1.4)
    c2 = s.raster(["$ apt list --installed | wc -l", "630"], (0.1, yz), groesse=TK, zeilenabstand=1.4)
    l_ii = L(s, "ii", w["ii"], (xg + 0.4, c1.y(1)), FM, "left", GRAU)
    listing = chip(s, (0.1 + chipb("Listing...") / 2, r4(c2.y(1) - 0.32)), "Listing...", ROT, ROT_HELL, h=0.24)
    l_plus = L(s, "plus", w["plus"], (0.1 + chipb("Listing...") + 0.12, r4(c2.y(1) - 0.32)), FM, "left")
    s.pause(0.6)
    schritt(s, EIN(g1.ids + g2.ids, 0.6))
    for k, lab in zerl:
        schritt(s, ZEICHNE(k, 0.35), EIN(lab, 0.35))
    s.pause(0.4)
    schritt(s, EIN(m_now + [l_now], 0.6))
    schritt(s, EIN(leer, 0.6))
    s.pause(0.6)
    schritt(s, EIN(c1.ids + [l_ii], 0.6))
    schritt(s, EIN(c2.ids, 0.6))
    schritt(s, EIN(listing + [l_plus], 0.6))
    s.speichern()


W_PO = {"prio": ("1. höchste Priorität: 500 = 500, Gleichstand", "1. highest priority: 500 = 500, a tie",
                 "1. prioridad más alta: 500 = 500, empate", "1. 最高优先级：500 = 500，平局", "1. priorité la plus haute : 500 = 500, égalité",
                 "1. en yüksek öncelik: 500 = 500, eşit"),
        "vers": ("2. Version: 0.10.0 ist neuer als 0.8.0", "2. version: 0.10.0 is newer than 0.8.0",
                 "2. versión: 0.10.0 es más nueva que 0.8.0", "2. 版本：0.10.0 比 0.8.0 新", "2. version : 0.10.0 est plus récente que 0.8.0",
                 "2. sürüm: 0.10.0, 0.8.0'dan yeni")}


def k9policy():
    """Versionstabelle von rust-coreutils (Block s4_policyrust) als Siegertreppchen: 0.10.0-1ubuntu2~26.04.1 (resolute-updates
    500, resolute-security 500) gegen 0.8.0-0ubuntu3 (*** installiert; resolute 500, /var/lib/dpkg/status 100). Erst die
    höchste Priorität (Gleichstand 500), dann die Version: 0.10.0 steigt aufs Treppchen und wird Candidate, 0.8.0 behält
    Installed und die drei Sterne."""
    s = Szene("linux/k9policy", reihenfolge="anlegen")
    w = W_PO
    titel = tx(s, "$ apt policy rust-coreutils", (0, 2.85), TK, "center", DUNKEL)
    xa, xb, yc, hc = -1.72, 1.72, 1.45, 1.05
    karte_a = [box(s, (xa, yc), 3.2, hc, BLAU, WEISS, 2.5, "rect"), tx(s, "0.10.0-1ubuntu2~26.04.1", (xa, yc + 0.3), TT)]
    pa = [tx(s, "500", (xa - 1.35, yc - 0.03), TK, "left"), tx(s, "500", (xa - 1.35, yc - 0.28), TK, "left")]
    karte_a += pa + [tx(s, "resolute-updates", (xa - 0.95, yc - 0.03), TK, "left", GRAU),
                     tx(s, "resolute-security", (xa - 0.95, yc - 0.28), TK, "left", GRAU)]
    karte_b = [box(s, (xb, yc), 3.2, hc, BLAU, WEISS, 2.5, "rect"), tx(s, "***", (xb - 0.6, yc + 0.3), TT, "right"),
               tx(s, "0.8.0-0ubuntu3", (xb + 0.16, yc + 0.3), TT)]
    pb = [tx(s, "500", (xb - 1.35, yc - 0.03), TK, "left"), tx(s, "100", (xb - 1.35, yc - 0.28), TK, "left")]
    karte_b += pb + [tx(s, "resolute", (xb - 0.95, yc - 0.03), TK, "left", GRAU),
                     tx(s, "/var/lib/dpkg/status", (xb - 0.95, yc - 0.28), TK, "left", GRAU)]
    ys = yc - hc / 2
    sockel_a = box(s, (xa, ys - 0.2), 2.2, 0.4, GRAU, GRAU_HELL, 2, "rect")
    sockel_b = box(s, (xb, ys - 0.2), 2.2, 0.4, GRAU, GRAU_HELL, 2, "rect")
    hoch = 0.35
    sockel_a2 = box(s, (xa, ys - 0.2 + hoch / 2), 2.2, 0.4 + hoch, GRUEN, GRUEN_HELL, 2.5, "rect")
    inst = chip(s, (xb, ys - 0.2), "Installed", BLAU, BLAU_HELL, h=0.26)
    cand = chip(s, (xa, ys - 0.2), "Candidate", GRUEN, WEISS, h=0.26)
    mk = [box(s, (r4(p_x), r4(p_y)), 0.34, 0.2, ORANGE, ORANGE, 0, "rect", deckung=0.35)
          for p_x, p_y in ((xa - 1.35 + 0.113, yc - 0.03), (xa - 1.35 + 0.113, yc - 0.28), (xb - 1.35 + 0.113, yc - 0.03))]
    l_prio = L(s, "prio", w["prio"], (0, ys - 0.75), FM, "center", ORANGE)
    l_vers = L(s, "vers", w["vers"], (0, ys - 1.02), FM, "center", GRUEN)
    vb = [box(s, (xa, yc + 0.3), ttb("0.10.0-1ubuntu2~26.04.1", TT) + 0.1, 0.24, GRUEN, WEISS, 2.5, deckung=0.0),
          box(s, (xb + 0.16, yc + 0.3), ttb("0.8.0-0ubuntu3", TT) + 0.1, 0.24, GRAU, WEISS, 2.5, deckung=0.0)]
    schritt(s, EIN([titel], 0.5))
    schritt(s, EIN(karte_a + karte_b + [sockel_a, sockel_b] + inst, 0.7))
    s.pause(0.6)
    schritt(s, EIN(mk + [l_prio], 0.7))
    s.pause(0.5)
    schritt(s, EIN(vb + [l_vers], 0.7))
    s.pause(0.4)
    schritt(s, EIN(sockel_a2, 0.8), AUS(sockel_a, 0.8), *VERS(karte_a + [mk[0], mk[1], vb[0]], 0, hoch, 0.8))
    schritt(s, WACHS(cand[0], 0.5), EIN(cand[1], 0.5))
    s.speichern()


W_RD = {"runter": ("wovon jq abhängt", "what jq depends on", "de qué depende jq", "jq 依赖什么", "ce dont jq dépend",
                   "jq neye bağlı"),
        "hoch": ("wer libonig5 braucht", "who needs libonig5", "quién necesita libonig5", "谁需要 libonig5", "qui a besoin de libonig5",
                 "libonig5'e kim ihtiyaç duyar"),
        "422": ("422 installierte Pakete brauchen libc6", "422 installed packages need libc6", "422 paquetes instalados necesitan libc6",
                "422 个已安装的软件包需要 libc6", "422 paquets installés ont besoin de libc6", "422 kurulu paket libc6'ya ihtiyaç duyar")}


def k9rdepends():
    """Derselbe Graph in zwei Richtungen: links apt-cache depends jq (Pfeile nach unten zu libjq1, libc6, libonig5),
    rechts apt-cache rdepends libonig5 (Block s4_rdepends, Pfeile von oben hinein: libevhtp0t64, php8.5-mbstring, libjq1,
    jq, xh, rust-findutils, …). Zum Schluss ein Fächer von Pfeilen in libc6 mit 422."""
    s = Szene("linux/k9rdepends", reihenfolge="anlegen")
    w = W_RD
    xl = -1.85
    links = [tx(s, "$ apt-cache depends jq", (xl, 2.75), TK, "center", DUNKEL)] + chip(s, (xl, 2.3), "jq")
    ziele = [("libjq1", -2.85), ("libc6", -1.85), ("libonig5", -0.85)]
    zk, zp = [], []
    for n, x in ziele:
        zk += chip(s, (x, 1.3), n, BLAU, BLAU_HELL if n != "libonig5" else ORANGE_HELL)
        zp.append(pfk(s, (xl + (x - xl) * 0.15, 2.15), (x, 1.45), DUNKEL, 2.5))
    l_runter = L(s, "runter", w["runter"], (xl, 0.88), FM, "center", GRAU)
    xr = 1.75
    rechts = [tx(s, "$ apt-cache rdepends libonig5", (xr, 2.75), TK, "center", DUNKEL)]
    on = chip(s, (xr, 0.75), "libonig5", BLAU, ORANGE_HELL)
    quellen = [("libevhtp0t64", 0, 2.32), ("php8.5-mbstring", 1, 2.32), ("libjq1", 0, 1.94), ("jq", 1, 1.94), ("xh", 0, 1.56),
               ("rust-findutils", 1, 1.56)]
    qk, qp = [], []
    for i, (n, sp, y) in enumerate(quellen):
        b = chipb(n)
        x = r4(xr - 0.3 - b / 2) if sp == 0 else r4(xr + 0.3 + b / 2)
        qk.append(chip(s, (x, y), n, BLAU, WEISS))
        xs = xr - 0.3 if sp == 0 else xr + 0.3
        reihe = round((2.32 - y) / 0.38)
        qp.append(pfk(s, (xs, y), (xr + (-1 if sp == 0 else 1) * (0.1 + 0.1 * reihe), 0.9), DUNKEL, 2))
    mehr = txa(s, PUNKTE, (xr + 0.35, 1.25), TK, "left")
    l_hoch = L(s, "hoch", w["hoch"], (xr, 0.38), FM, "center", GRAU)
    # Fächer in libc6
    yc = -1.55
    libc = chip(s, (0, yc), "libc6", BLAU, BLAU_HELL, dicke=2.5)
    faecher = []
    for i in range(21):
        x = -3.0 + i * 0.3
        y0 = -0.35 - 0.18 * (1 - (x / 3.0) ** 2)
        faecher.append(pfk(s, (x, y0), (x * 0.08, yc + 0.16), GRAU, 1.2, spitze=0.05))
    l_422 = L(s, "422", w["422"], (0.45, yc), FM, "left", ORANGE)
    rohr = tx(s, "$ apt-cache rdepends --installed libc6 | tail -n +3 | sort -u | wc -l", (0, yc - 0.42), TK, "center", GRAU)
    schritt(s, EIN(links, 0.6))
    schritt(s, ZEICHNE(zp, 0.7), EIN(zk + [l_runter], 0.7))
    s.pause(0.6)
    schritt(s, EIN(rechts + on, 0.6))
    schritt(s, EIN(flach(qk) + [mehr], 0.7), ZEICHNE(qp, 0.9))
    schritt(s, EIN(l_hoch, 0.5))
    s.pause(0.6)
    schritt(s, WACHS(libc[0], 0.5), EIN(libc[1], 0.5))
    schritt(s, ZEICHNE(faecher, 1.0), EIN([l_422, rohr], 1.0))
    s.speichern()


# ================================================================== Abschnitt 5: Ein Paket von innen
W_DO = {"server": ("Server", "server", "servidor", "服务器", "serveur", "sunucu"),
        "nur": ("nur geladen, nichts installiert,\nkein root nötig", "only downloaded, nothing installed,\nno root needed",
                "solo descargado, nada instalado,\nsin root", "只是下载，没有安装，\n不需要 root", "seulement téléchargé, rien d'installé,\nsans root",
                "yalnızca indirildi, kurulmadı,\nroot gerekmez"),
        "inst": ("installiert", "installed", "instalado", "已安装", "installé", "kuruldu"),
        "geloescht": ("nach dem Installieren gelöscht", "deleted after installing", "borrado tras instalar", "安装后被删除",
                      "supprimé après l'installation", "kurulumdan sonra silindi"),
        "groesse": ("Größe der Datei", "size of the file", "tamaño del archivo", "文件大小", "taille du fichier", "dosyanın boyutu"),
        "lsl": ("laut ls -l", "from ls -l", "según ls -l", "来自 ls -l", "d'après ls -l", "ls -l'ye göre"),
        "liste": ("Feld der Paketliste", "field of the package list", "campo de la lista", "软件包列表中的字段", "champ de la liste",
                  "paket listesindeki alan")}


def k9download():
    """Zwei Wege einer Paketdatei vom Server: oben apt download hello → ~/linuxk9 („nur geladen, nichts installiert, kein
    root“); unten sudo apt install hello → /var/cache/apt/archives → dpkg, danach dort gelöscht. Am Rand: 26068 Byte
    (ls -l) = Size: 26068 aus der Paketliste (grünes Gleichheitszeichen)."""
    s = Szene("linux/k9download", reihenfolge="anlegen")
    w = W_DO
    srv = [box(s, (-2.75, 0.85), 1.4, 2.5, DUNKEL, GRAU_HELL, 2.5, "rect"), tx(s, "archive.ubuntu.com", (-2.75, 2.3), TK, "center", DUNKEL),
           L(s, "server", w["server"], (-2.75, 1.8), FM, "center", GRAU)]
    srv += [box(s, (-2.75, 0.9), 0.42, 0.55, GRAU, WEISS, 2, "rect"), tx(s, ".deb", (-2.75, 0.9), TK, "center", GRAU)]
    bc = ttb(HELLO_DEB) + 0.14
    y1, y2 = 1.55, -0.05
    oben = [tx(s, "$ apt download hello", (-1.9, y1 + 0.62), TK, "left", DUNKEL), pfk(s, (-2.0, y1), (0.93, y1), DUNKEL, 2.5),
            box(s, (2.2, y1), 2.45, 0.72, BLAU, BLAU_HELL, 2, "rect"), tx(s, "~/linuxk9", (1.08, y1 + 0.2), TK, "left", BLAU)]
    l_nur = L(s, "nur", w["nur"], (-0.55, y1 - 0.42), FM, "center", GRUEN)
    d1 = chip(s, (-2.75, 0.9), HELLO_DEB, GRAU, WEISS, h=0.24, b=bc)
    unten = [tx(s, "$ sudo apt install hello", (-1.9, y2 + 0.62), TK, "left", DUNKEL), pfk(s, (-2.0, y2), (-0.82, y2), DUNKEL, 2.5),
             box(s, (0.45, y2), 2.45, 0.72, BLAU, BLAU_HELL, 2, "rect"), tx(s, "/var/cache/apt/archives", (-0.68, y2 + 0.2), TK, "left", BLAU)]
    weiter = [pfk(s, (1.72, y2), (2.15, y2), DUNKEL, 2.5), box(s, (2.8, y2), 1.2, 0.72, DUNKEL, WEISS, 2, "rect"),
              tx(s, "dpkg", (2.8, y2 + 0.15), TT, "center", DUNKEL)]
    ok = haken(s, 2.55, y2 - 0.15, GRUEN, 0.07, 3.5) + [L(s, "inst", w["inst"], (2.68, y2 - 0.15), FM, "left", GRUEN)]
    d2 = chip(s, (-2.75, 0.9), HELLO_DEB, GRAU, WEISS, h=0.24, b=bc)
    l_weg = L(s, "geloescht", w["geloescht"], (0.45, y2 - 0.12), FM, "center", ROT)
    # Größe am Rand
    yg = -0.95
    groesse = [L(s, "groesse", w["groesse"], (-3.4, yg + 0.27), FM, "left", GRAU), tx(s, "26068", (-3.4, yg), TT, "left"),
               L(s, "lsl", w["lsl"], (-3.4, yg - 0.25), FM, "left", GRAU),
               text(s, "=", (-2.55, yg), 30, "center", GRUEN),
               tx(s, "Size: 26068", (-2.25, yg), TT, "left"), L(s, "liste", w["liste"], (-2.25, yg - 0.25), FM, "left", GRAU)]
    schritt(s, EIN(srv, 0.7))
    s.pause(0.4)
    schritt(s, EIN(oben, 0.6))
    schritt(s, EIN(d1, 0.3))
    schritt(s, *VERS(d1, 2.2 + 2.75, y1 - 0.12 - 0.9, 1.2))
    schritt(s, EIN(l_nur, 0.6))
    s.pause(0.6)
    schritt(s, EIN(unten + weiter, 0.6))
    schritt(s, EIN(d2, 0.3))
    schritt(s, *VERS(d2, 0.45 + 2.75, y2 - 0.12 - 0.9 + 0.0, 1.0))
    schritt(s, BETONE(weiter[0], 0.6), EIN(ok, 0.6))
    schritt(s, AUS(d2, 0.6), EIN(l_weg, 0.6))
    s.pause(0.5)
    schritt(s, EIN(groesse, 0.7))
    s.speichern()


W_DEB = {"ganz": ("Paketdatei: 26 068 Byte", "package file: 26,068 bytes", "archivo de paquete: 26 068 bytes", "软件包文件：26,068 字节",
                  "fichier de paquet : 26 068 octets", "paket dosyası: 26.068 bayt"),
         "db": ("debian-binary: „2.0“, 4 Byte", "debian-binary: “2.0”, 4 bytes", "debian-binary: «2.0», 4 bytes",
                "debian-binary：“2.0”，4 字节", "debian-binary : « 2.0 », 4 octets", "debian-binary: “2.0”, 4 bayt"),
         "ct": ("control.tar.zst: 856 Byte", "control.tar.zst: 856 bytes", "control.tar.zst: 856 bytes", "control.tar.zst：856 字节",
                "control.tar.zst : 856 octets", "control.tar.zst: 856 bayt"),
         "dt": ("data.tar.zst: 25 019 Byte", "data.tar.zst: 25,019 bytes", "data.tar.zst: 25 019 bytes", "data.tar.zst：25,019 字节",
                "data.tar.zst : 25 019 octets", "data.tar.zst: 25.019 bayt"),
         "steuer": ("Steuerteil", "control part", "parte de control", "控制部分", "partie de contrôle", "denetim kısmı"),
         "daten": ("Datenteil", "data part", "parte de datos", "数据部分", "partie de données", "veri kısmı"),
         "rest": ("dazu 8 + 3 × 60 Byte Verwaltungsangaben des Archivs und 1 Füllbyte",
                  "plus 8 + 3 × 60 bytes of archive headers and 1 padding byte",
                  "más 8 + 3 × 60 bytes de cabeceras del archivo y 1 byte de relleno", "另有 8 + 3 × 60 字节的归档头信息和 1 个填充字节",
                  "plus 8 + 3 × 60 octets d'en-têtes de l'archive et 1 octet de remplissage",
                  "ayrıca 8 + 3 × 60 bayt arşiv başlığı ve 1 dolgu baytı"),
         "massstab": ("(nicht maßstäblich)", "(not to scale)", "(no a escala)", "（未按比例）", "(pas à l'échelle)", "(ölçekli değil)")}


def k9deb():
    """hello_2.10-5build1_amd64.deb als Streifen von 26 068 Byte: schmaler Kopf debian-binary („2.0“), kleiner Block
    control.tar.zst (856 Byte), großer data.tar.zst (25 019 Byte; ar tv). Der Steuerteil klappt auf zu control und md5sums,
    der Datenteil zu usr/bin/hello, usr/share/doc/hello/…, usr/share/info/…, usr/share/man/man1/hello.1.gz."""
    s = Szene("linux/k9deb", reihenfolge="anlegen")
    w = W_DEB
    x0, x1, ys, hs = -3.25, 3.25, 1.45, 0.42
    b_db, b_ct = 0.12, 0.26
    xa, xb = x0 + b_db, x0 + b_db + b_ct
    kopf = [tx(s, HELLO_DEB, (0, 2.85), TK, "center"), klammer(s, x0, x1, 2.28, unten=False, farbe=DUNKEL, t=0.08, dicke=2),
            Lr(s, "ganz", w["ganz"], (0, 2.5), FM, "center", DUNKEL)]
    teile = [box(s, ((x0 + xa) / 2, ys), b_db, hs, DUNKEL, GELB, 1.5, "rect"),
             box(s, ((xa + xb) / 2, ys), b_ct, hs, ORANGE, ORANGE_HELL, 1.5, "rect"),
             box(s, ((xb + x1) / 2, ys), x1 - xb, hs, BLAU, BLAU_HELL, 1.5, "rect")]
    l_dt = Lr(s, "dt", w["dt"], ((xb + x1) / 2, ys), FM, "center", BLAU)
    yk = -0.45
    l_db = [lin(s, ((x0 + xa) / 2, ys + hs / 2), ((x0 + xa) / 2, ys + 0.48), DUNKEL, 1.5),
            Lr(s, "db", w["db"], ((x0 + xa) / 2 + 0.1, ys + 0.48), FM, "left", DUNKEL)]
    l_ct = [lin(s, ((xa + xb) / 2, ys - hs / 2), ((xa + xb) / 2, yk + 0.48), ORANGE, 1.5),
            L(s, "ct", w["ct"], ((xa + xb) / 2 + 0.1, ys - 0.6), FM, "left", ORANGE)]
    l_ms = L(s, "massstab", w["massstab"], (-0.55, ys + 0.48), FM, "left", GRAU)
    # Steuerteil aufgeklappt
    steuer = [box(s, (-2.35, yk), 1.8, 0.95, ORANGE, WEISS, 2, "rect"), L(s, "steuer", w["steuer"], (-2.35, yk + 0.3), FM, "center", ORANGE)]
    steuer += chip(s, (-2.35, yk - 0.02), "control", ORANGE, ORANGE_HELL, h=0.24) + chip(s, (-2.35, yk - 0.3), "md5sums", ORANGE,
                                                                                          ORANGE_HELL, h=0.24)
    daten = [box(s, (1.5, yk - 0.05), 3.7, 1.25, BLAU, WEISS, 2, "rect"), L(s, "daten", w["daten"], (1.5, yk + 0.4), FM, "center", BLAU)]
    for i, p in enumerate(["usr/bin/hello", "usr/share/doc/hello/…", "usr/share/info/…", "usr/share/man/man1/hello.1.gz"]):
        y = r4(yk + 0.13 - i * 0.22)
        daten += [datei_symbol(s, 0.0, y), tx(s, p, (0.18, y), TK, "left")]
    zoom_d = [lin(s, (-0.2, ys - hs / 2), (-0.35, yk + 0.58), BLAU, 1.5, "4,4"), lin(s, (x1, ys - hs / 2), (3.35, yk + 0.58), BLAU, 1.5,
                                                                                         "4,4")]
    l_rest = L(s, "rest", w["rest"], (0, -1.35), FM, "center", GRAU)
    schritt(s, EIN(kopf, 0.6))
    schritt(s, WACHS(teile, 0.8), EIN(l_dt, 0.8))
    schritt(s, ZEICHNE(l_db[0], 0.5), EIN([l_db[1], l_ms], 0.5))
    s.pause(0.6)
    schritt(s, ZEICHNE(l_ct[0], 0.6), EIN([l_ct[1]] + steuer, 0.7))
    schritt(s, ZEICHNE(zoom_d, 0.5), EIN(daten, 0.7))
    s.pause(0.4)
    schritt(s, EIN(l_rest, 0.6))
    s.speichern()


DEB_I = [" new Debian package, version 2.0.", " size 26068 bytes: control archive=856 bytes.",
         "     842 bytes,    21 lines      control", "     375 bytes,     6 lines      md5sums", " Package: hello",
         " Version: 2.10-5build1", " Architecture: amd64", PUNKTE]
CONTROL = ["Package: hello", "Version: 2.10-5build1", "Architecture: amd64", PUNKTE, "Installed-Size: 104", "Depends: libc6 (>= 2.38)",
           PUNKTE]
MD5 = ["744cd4018e23f9e830ffd19d602311cd  usr/bin/hello", "9dbc678a728a0936b503c0aef4507f5d  usr/share/doc/hello/NEWS.gz",
       "dc449c753669eece697ea37a617f2c0e  usr/share/doc/hello/changelog.Debian.gz",
       "bf4bad78d5cf6787c6512b69f29be7fa  usr/share/doc/hello/copyright",
       "957220d1bec8cda9312bba43783e62cc  usr/share/info/hello.info.gz",
       "29b51e7fcc9c18e989a69e7870af6ba2  usr/share/man/man1/hello.1.gz"]
W_ST = {"keine": ("bei hello keine Skripte", "no scripts in hello", "hello no tiene scripts", "hello 没有脚本", "pas de scripts dans hello",
                  "hello'da betik yok"),
        "pruef": ("Prüfsumme – Pfad", "checksum – path", "suma de comprobación – ruta", "校验和 – 路径", "somme de contrôle – chemin",
                  "sağlama toplamı – yol")}


def k9steuerteil():
    """Terminal: dpkg-deb -I hello_2.10-5build1_amd64.deb, die ersten Zeilen (Block s5_info). Die Zeilen control und
    md5sums werden hervorgehoben; Pfeile führen zu zwei Datei-Ansichten (hell): control (Felder der Paketbeschreibung,
    ausgelassene Zeilen „...“) und md5sums mit den sechs Zeilen „Prüfsumme – Pfad“. Daneben vier leere gestrichelte
    Plätze preinst, postinst, prerm, postrm: bei hello keine Skripte."""
    s = Szene("linux/k9steuerteil", reihenfolge="anlegen")
    w = W_ST
    t = s.terminal(pos=(-3.45, 2.85), spalten=66, zeilen=10, prompt=P9, titel=TITEL, groesse=18)
    schritt(s, EIN(t.id, 0.6))
    s.pause(0.3)
    t.eingabe("dpkg-deb -I " + HELLO_DEB, dauer=1.6)
    t.ausgabe("\n".join(DEB_I), dauer=0.6)
    c = s.datei("control", "\n".join(CONTROL), pos=(1.45, 0.62), groesse=TK)
    m = s.datei("md5sums", "\n".join(MD5), pos=(-3.45, -1.0), groesse=TK)
    f_c = t.rahmen(3, 33, 39, farbe=ORANGE, dicke=2.5, rand=0.0)
    f_m = t.rahmen(4, 33, 39, farbe=BLAU, dicke=2.5, rand=0.0)
    xc = r4(c.links + 0.5)
    p_c = pfk(s, (t.xr(39) + 0.07, t.y(3)), (xc, c.oben_kante + 0.02), ORANGE, 2.5, knick="hv")
    xm_ = 0.35
    p_m = pfk(s, (t.xr(39) + 0.07, t.y(4)), (xm_, m.oben_kante + 0.02), BLAU, 2.5, knick="hv")
    l_pr = L(s, "pruef", w["pruef"], (m.links + 0.05, m.unten_kante - 0.2), FM, "left", GRAU)
    plaetze = []
    for i, n in enumerate(("preinst", "postinst", "prerm", "postrm")):
        x = r4(-3.0 + (i % 2) * 1.55)
        y = r4(0.42 - (i // 2) * 0.38)
        plaetze += [box(s, (x, y), 0.85 if i % 2 == 0 else 0.95, 0.28, GRAU, WEISS, 1.5, "rect", "4,4"),
                    tx(s, n, (x, y), TK, "center", GRAU)]
    l_keine = L(s, "keine", w["keine"], (-2.25, -0.33), FM, "center", GRAU)
    s.pause(0.5)
    schritt(s, EIN(f_c, 0.5))
    schritt(s, ZEICHNE(p_c, 0.6), EIN(c.id, 0.7))
    s.pause(0.4)
    schritt(s, EIN(f_m, 0.5))
    schritt(s, ZEICHNE(p_m, 0.6), EIN([m.id, l_pr], 0.7))
    s.pause(0.5)
    schritt(s, EIN(plaetze + [l_keine], 0.7))
    s.speichern()


W_AP = {"rechts": ("Installieren", "installing", "instalar", "安装", "installer", "kurmak"),
        "z1": ("Dateien landen in", "files go to", "los archivos van a", "文件放到", "les fichiers vont dans", "dosyalar şuraya"),
        "z2": ("Besitzer", "owner", "propietario", "所有者", "propriétaire", "sahip"),
        "z3": ("Programm läuft", "program runs", "el programa funciona", "程序运行", "le programme tourne", "program çalışır"),
        "z4": ("Abhängigkeiten geprüft", "dependencies checked", "dependencias comprobadas", "检查依赖", "dépendances vérifiées",
               "bağımlılıklar denetlendi"),
        "z5": ("Wartungsskripte laufen", "maintainer scripts run", "scripts de mantenimiento", "运行维护脚本", "scripts de maintenance",
               "bakım betikleri çalışır"),
        "z6": ("Paketdatenbank", "package database", "base de datos de paquetes", "软件包数据库", "base des paquets", "paket veritabanı"),
        "falls": ("ja, falls vorhanden", "yes, if any", "sí, si los hay", "是（如果有）", "oui, s'il y en a", "evet, varsa")}


def k9auspacken():
    """Dieselbe Paketdatei oben, darunter zwei Spalten: links dpkg-deb -x (Dateien in ~/linuxk9/auspacken/usr/…, Besitzer
    student, das Programm läuft: Hello, world!, Paketdatenbank: no packages found), rechts Installieren (/usr/…, root,
    Hello, world!, dazu Abhängigkeitsprüfung, Wartungsskripte und der Eintrag ii hello in der Paketdatenbank). Die drei
    Zusatzschritte rechts leuchten nacheinander auf."""
    s = Szene("linux/k9auspacken", reihenfolge="anlegen")
    w = W_AP
    xl, xr, xz = -0.75, 2.2, -3.4
    datei = chip(s, (0.7, 2.7), HELLO_DEB, GRAU, GELB, h=0.28)
    kl = [tx(s, "dpkg-deb -x", (xl + 0.2, 2.12), TT, "center", BLAU), L(s, "rechts", w["rechts"], (xr, 2.12), FM, "center", DUNKEL)]
    pfe = [pfk(s, (0.1, 2.55), (xl + 0.35, 2.27), DUNKEL, 2.5), pfk(s, (1.3, 2.55), (xr - 0.2, 2.27), DUNKEL, 2.5)]
    trenn = lin(s, (0.72, 1.95), (0.72, -0.35), HELLGRAU, 2)
    ys = [1.7, 1.37, 1.04, 0.71, 0.38, 0.05]
    namen = [L(s, "z%d" % (i + 1), w["z%d" % (i + 1)], (xz, y), FM, "left", GRAU) for i, y in enumerate(ys)]
    links = [tx(s, "~/linuxk9/auspacken/usr/…", (xl + 0.2, ys[0]), TK), tx(s, "student", (xl + 0.2, ys[1]), TK),
             tx(s, "Hello, world!", (xl + 0.2, ys[2]), TK, "center", GRUEN), strich(s, xl + 0.2, ys[3], HELLGRAU, 0.15, 3),
             strich(s, xl + 0.2, ys[4], HELLGRAU, 0.15, 3), tx(s, "no packages found", (xl + 0.2, ys[5]), TK, "center", ROT)]
    rechts = [tx(s, "/usr/…", (xr, ys[0]), TK), tx(s, "root", (xr, ys[1]), TK), tx(s, "Hello, world!", (xr, ys[2]), TK, "center", GRUEN)]
    extra = [haken(s, xr, ys[3], GRUEN, 0.08, 3.5),
             [L(s, "falls", w["falls"], (xr, ys[4]), FM, "center", GRUEN)],
             [tx(s, "ii  hello", (xr, ys[5]), TK, "center", GRUEN)]]
    rahmen_x = [box(s, (xr, y), 2.3, 0.28, ORANGE, WEISS, 2.5, deckung=0.0) for y in ys[3:]]
    schritt(s, WACHS(datei[0], 0.5), EIN(datei[1], 0.5))
    schritt(s, ZEICHNE(pfe, 0.5), EIN(kl + [trenn] + namen, 0.6))
    s.pause(0.4)
    schritt(s, EIN(links[:3] + rechts, 0.7))
    s.pause(0.5)
    schritt(s, EIN(links[3:], 0.6))
    for k in range(3):
        schritt(s, EIN([rahmen_x[k]] + flach(extra[k]), 0.6))
        s.pause(0.3)
    s.speichern()


# ================================================================== Abschnitt 6: Installieren, entfernen, aktualisieren
# (Phase 2b-2, 12.11.2026)
def nr(s, x, y, n, farbe, r=0.11):
    """Nummer im Kreis (Ergebnis [Kreis, Zahl]); Schrift FM (nummer() aus linux_hilfen hat 16 px)."""
    return [s.kreis(None, r4(x), r4(y), r, farbe=farbe, dicke=2, fuellung=WEISS, deckung=1.0),
            text(s, str(n), (r4(x), r4(y)), FM, "center", farbe)]


def proz(s, mitte, name, rand=ORANGE, fuellung=ORANGE_HELL, unten="root", textfarbe=SCHWARZ):
    """Prozess als Kärtchen mit Name und Benutzer (Ergebnis [Kasten, Name, Benutzer])."""
    b = max(ttb(name), ttb(unten)) + 0.26
    x, y = mitte
    return [box(s, (x, y), b, 0.5, rand, fuellung, 2), tx(s, name, (x, y + 0.1), TK, "center", textfarbe),
            tx(s, unten, (x, y - 0.12), TK, "center", GRAU)]


def sanduhr(s, x, y, h=0.3, farbe=DUNKEL):
    b = h * 0.7
    return [lin(s, (x - b / 2, y + h / 2), (x + b / 2, y + h / 2), farbe, 2.5),
            lin(s, (x - b / 2, y - h / 2), (x + b / 2, y - h / 2), farbe, 2.5),
            lin(s, (x - b / 2 + 0.03, y + h / 2), (x + b / 2 - 0.03, y - h / 2), farbe, 2),
            lin(s, (x + b / 2 - 0.03, y + h / 2), (x - b / 2 + 0.03, y - h / 2), farbe, 2)]


def leer(s, mitte, b, h=0.28):
    """Leerer, gestrichelter Platz (etwas wurde gelöscht)."""
    return box(s, mitte, b, h, HELLGRAU, WEISS, 1.5, dash="4,4")


W_SP = {"kernel": ("Kernel: verwaltet die Sperren", "kernel: manages the locks", "kernel: gestiona los bloqueos", "内核：管理锁",
                   "noyau : gère les verrous", "çekirdek: kilitleri yönetir"),
        "datei": ("Sperrdatei:", "lock file:", "archivo de bloqueo:", "锁文件：", "fichier de verrou :", "kilit dosyası:"),
        "gesperrt": ("gesperrt", "locked", "bloqueado", "已锁定", "verrouillé", "kilitli"),
        "wartet": ("wartet", "waits", "espera", "等待中", "attend", "bekler"),
        "fertig": ("beendet: der Kernel\ngibt die Sperre frei", "finished: the kernel\nreleases the lock",
                   "terminado: el kernel\nlibera el bloqueo", "已结束：内核\n释放锁", "terminé : le noyau\nlibère le verrou",
                   "bitti: çekirdek\nkilidi bırakır"),
        "ohne": ("student, ohne sudo", "student, without sudo", "student, sin sudo", "student，不用 sudo", "student, sans sudo",
                 "student, sudo olmadan")}


def k9sperre():
    """Sperrdatei /var/lib/dpkg/lock-frontend als Tür mit Riegel, darüber der Kernel. unattended-upgrade (root) tritt ein,
    der Riegel schließt, Schild „gesperrt“. sudo apt install (root) wartet mit Sanduhr. Der erste endet und geht (grau,
    „beendet: der Kernel gibt die Sperre frei“), der Riegel öffnet sich, der zweite tritt ein, der Riegel schließt wieder.
    Unten student ohne sudo: scheitert am Schloss rw-r----- (Permission denied, Block s6_ohnesudo)."""
    s = Szene("linux/k9sperre", reihenfolge="anlegen")
    w = W_SP
    kern = [box(s, (0, 2.75), 6.8, 0.34, DUNKEL, GRAU_HELL, 2, "rect"), L(s, "kernel", w["kernel"], (0, 2.75), FM, "center", DUNKEL)]
    xt, yt, bt, ht = 0.45, 1.3, 2.0, 1.6
    pfad = "/var/lib/dpkg/lock-frontend"
    tuer = [box(s, (xt, yt), bt, ht, DUNKEL, BLAU_HELL, 2.5, "rect"),
            lin(s, (xt + bt / 2 + 0.07, yt - ht / 2), (xt + bt / 2 + 0.07, yt + ht / 2), DUNKEL, 6),
            tx(s, pfad, (xt, 2.33), TK), L(s, "datei", w["datei"], (xt - ttb(pfad) / 2 - 0.12, 2.33), FM, "right", GRAU)]
    yr = 1.5
    zug = [lin(s, (1.72, 2.58), (1.72, yr + 0.06), GRAU, 1.5, "4,4")]
    riegel = box(s, (1.3, yr), 0.3, 0.09, DUNKEL, DUNKEL, 1.5, "rect")
    schild1 = wchip(s, (xt, 1.88), "gesperrt", w["gesperrt"], 1.15, ROT, ROT_HELL, h=0.28)
    schild2 = wchip(s, (xt, 1.88), "gesperrt", w["gesperrt"], 1.15, ROT, ROT_HELL, h=0.28)
    p1 = proz(s, (-2.25, 1.75), "unattended-upgrade")
    p2 = proz(s, (-2.25, 0.95), "sudo apt install", BLAU, BLAU_HELL)
    uhr_ = sanduhr(s, -3.25, 0.95)
    l_wart = L(s, "wartet", w["wartet"], (-2.25, 0.55), FM, "center", GRAU)
    xa = 2.64
    p1g = proz(s, (xa, yt), "unattended-upgrade", GRAU, GRAU_HELL, textfarbe=GRAU)
    l_fertig = L(s, "fertig", w["fertig"], (xa, 0.72), FM, "center", GRAU)
    st = chip(s, (-2.25, -0.25), "apt install hello", GRAU, WEISS)
    l_ohne = L(s, "ohne", w["ohne"], (-2.25, -0.56), FM, "center", GRAU)
    p_st = pfk(s, (-1.45, -0.2), (-0.45, 0.18), DUNKEL, 2.5)
    schl = s.schloss((-0.27, 0.27), 0.28, farbe=DUNKEL)
    rw = [tx(s, "rw-r-----", (-0.05, 0.27), TK, "left"), tx(s, "Permission denied", (-0.05, -0.02), TK, "left", ROT)]
    nein = kreuz(s, -0.62, 0.08, 0.18)
    schritt(s, EIN(kern + tuer + zug + [riegel], 0.7))
    s.pause(0.3)
    schritt(s, EIN(p1, 0.5))
    schritt(s, *VERS(p1, xt + 2.25, yt - 0.25 - 1.75, 0.9))
    schritt(s, VER(riegel, 0.22, 0, 0.5), EIN(schild1, 0.5))
    s.pause(0.4)
    schritt(s, EIN(p2 + uhr_ + [l_wart], 0.6))
    s.pause(0.8)
    schritt(s, *VERS(p1, xa - xt, 0.25, 0.8))
    schritt(s, AUS(p1 + schild1, 0.6), EIN(p1g + [l_fertig], 0.6), VER(riegel, -0.22, 0, 0.6))
    schritt(s, *VERS(p2, xt + 2.25, yt - 0.25 - 0.95, 0.9), AUS(uhr_ + [l_wart], 0.9))
    schritt(s, VER(riegel, 0.22, 0, 0.5), EIN(schild2, 0.5))
    s.pause(0.6)
    schritt(s, EIN(st + [l_ohne], 0.5))
    schritt(s, ZEICHNE(p_st, 0.6))
    schritt(s, WACHS(schl, 0.5), EIN(rw[0], 0.5))
    schritt(s, WACHS(nein, 0.5), EIN(rw[1], 0.5))
    s.speichern()


SIM = ["NOTE: This is only a simulation!", "      apt needs root privileges for real execution.",
       "      Keep also in mind that locking is deactivated,",
       "      so don't depend on the relevance to the real current situation!", "", "Installing:", "  " + gr("jq"), "",
       "Installing dependencies:", "  " + gr("libjq1") + "  " + gr("libonig5"), "", "Summary:",
       "  Upgrading: 0, Installing: 3, Removing: 0, Not Upgrading: 126",
       "Inst libonig5 (6.9.10-1build1 Ubuntu:26.04/resolute [amd64])",
       "Inst libjq1 (1.8.1-4ubuntu2 Ubuntu:26.04/resolute-updates, Ubuntu:26.04/resolute-security [amd64])",
       "Inst jq (1.8.1-4ubuntu2 Ubuntu:26.04/resolute-updates, Ubuntu:26.04/resolute-security [amd64])",
       "Conf libonig5 (6.9.10-1build1 Ubuntu:26.04/resolute [amd64])",
       "Conf libjq1 (1.8.1-4ubuntu2 Ubuntu:26.04/resolute-updates, Ubuntu:26.04/resolute-security [amd64])",
       "Conf jq (1.8.1-4ubuntu2 Ubuntu:26.04/resolute-updates, Ubuntu:26.04/resolute-security [amd64])"]
W_SI = [("nur Simulation: ohne root, ohne Sperre", "only a simulation: no root, no lock", "solo simulación: sin root ni bloqueo",
         "仅为模拟：无需 root，不加锁", "simple simulation : sans root, sans verrou", "yalnızca benzetim: root yok, kilit yok"),
        ("verlangt", "requested", "pedido", "所要求的", "demandé", "istenen"),
        ("mitgebracht: Abhängigkeiten", "brought along: dependencies", "traídas: dependencias", "随之安装：依赖",
         "apportées : dépendances", "beraberinde gelen: bağımlılıklar"),
        ("Zusammenfassung in Zahlen", "summary in numbers", "resumen en cifras", "数字摘要", "résumé en chiffres", "sayılarla özet"),
        ("Inst: auspacken (dpkg)", "Inst: unpack (dpkg)", "Inst: desempaquetar (dpkg)", "Inst：解包（dpkg）",
         "Inst : dépaqueter (dpkg)", "Inst: paketi açmak (dpkg)"),
        ("Conf: einrichten (dpkg)", "Conf: configure (dpkg)", "Conf: configurar (dpkg)", "Conf：配置（dpkg）",
         "Conf : configurer (dpkg)", "Conf: yapılandırmak (dpkg)")]
W_SI_FOLGE = ("Reihenfolge libonig5, libjq1, jq: zuerst, wovon die anderen abhängen",
              "order libonig5, libjq1, jq: first what the others depend on",
              "orden libonig5, libjq1, jq: primero aquello de lo que dependen los demás",
              "顺序 libonig5、libjq1、jq：先装其他包所依赖的", "ordre libonig5, libjq1, jq : d'abord ce dont les autres dépendent",
              "sıra libonig5, libjq1, jq: önce diğerlerinin bağlı olduğu")


def k9simulation():
    """Terminal: apt -s install jq (Block s6_simulation vollständig, 84 Spalten; die Zeilen Inst/Conf brechen um wie im
    Terminal, Paketnamen unter Installing grün). Nacheinander werden NOTE, Installing, Installing dependencies, Summary
    gerahmt und nummeriert, die Blöcke Inst (orange) und Conf (grün) hinterlegt; die Liste darunter erklärt die Nummern,
    zuletzt die Reihenfolge libonig5, libjq1, jq."""
    s = Szene("linux/k9simulation", reihenfolge="anlegen")
    t = s.terminal(pos=(-3.45, 2.95), spalten=84, zeilen=25, prompt=P9, titel=TITEL, groesse=18)
    schritt(s, EIN(t.id, 0.6))
    s.pause(0.3)
    t.eingabe("apt -s install jq")
    t.ausgabe("\n".join(SIM), dauer=0.7)
    teile = []
    for z, n in ((1, 32), (6, 11), (9, 24), (12, 8)):
        teile.append(([t.rahmen(z, 0, n - 1, farbe=ORANGE, dicke=2.5, rand=0.0)], (t.xr(n - 1) + 0.2, t.y(z)), ORANGE))
    teile.append(([t.markieren(14, 0, 83, farbe=ORANGE, deckung=0.3, bis=18)], (t.xr(58) + 0.25, t.y(14)), ORANGE))
    teile.append(([t.markieren(19, 0, 83, farbe=GRUEN, deckung=0.4, bis=23)], (t.xr(58) + 0.25, t.y(19)), GRUEN))
    y0 = r4(t.unten_kante - 0.28)
    schritte_ = []
    for k, (ids, (xn, yn), f) in enumerate(teile):
        xl, yl = (-3.3, y0 - 0.28 * k) if k < 3 else (0.3, y0 - 0.28 * (k - 3))
        leg = nr(s, xl, yl, k + 1, f) + [L(s, "si%d" % k, W_SI[k], (xl + 0.2, yl), FM, "left")]
        schritte_.append((ids + nr(s, xn, yn, k + 1, f), leg))
    folge = L(s, "folge", W_SI_FOLGE, (-3.41, r4(y0 - 0.28 * 3 - 0.04)), FM, "left", DUNKEL)
    s.pause(0.6)
    for ids, leg in schritte_:
        schritt(s, EIN(ids + leg, 0.6))
        s.pause(0.3)
    schritt(s, EIN(folge, 0.6))
    s.speichern()


W_IN = {"s1": ("1 Auflösen", "1 resolve", "1 resolver", "1 解析", "1 résoudre", "1 çözmek"),
        "s2": ("2 Laden und\nprüfen", "2 download\nand verify", "2 descargar\ny verificar", "2 下载\n并校验", "2 télécharger\net vérifier",
               "2 indirmek ve\ndoğrulamak"),
        "s3": ("3 Auspacken\n(Inst)", "3 unpack\n(Inst)", "3 desempaquetar\n(Inst)", "3 解包\n（Inst）", "3 dépaqueter\n(Inst)",
               "3 açmak\n(Inst)"),
        "s4": ("4 Einrichten\n(Conf)", "4 configure\n(Conf)", "4 configurar\n(Conf)", "4 配置\n（Conf）", "4 configurer\n(Conf)",
               "4 yapılandırmak\n(Conf)"),
        "server": ("Server", "server", "servidor", "服务器", "serveur", "sunucu"),
        "pruef": ("Prüfsumme stimmt", "checksum matches", "la suma coincide", "校验和一致", "somme correcte", "sağlama tutuyor"),
        "dateien": ("Dateien", "files", "archivos", "文件", "fichiers", "dosyalar"),
        "listen": ("Dateilisten", "file lists", "listas", "文件列表", "listes", "listeler"),
        "inst": ("installiert", "installed", "instalado", "已安装", "installé", "kuruldu"),
        "aus3": ("aus jq\nwerden\n3 Pakete", "jq becomes\n3 packages", "jq se\nconvierte en\n3 paquetes", "jq 变成\n3 个软件包",
                 "jq devient\n3 paquets", "jq\n3 paket\nolur"),
        "gesperrt": ("gesperrt:", "locked:", "bloqueado:", "已锁定：", "verrouillé :", "kilitli:")}


def k9installieren():
    """sudo apt install jq als Fließband mit vier Stationen: 1 Auflösen (jq wird zu jq, libjq1, libonig5), 2 Laden und
    prüfen (Server, grüne Haken, /var/cache/apt/archives), 3 Auspacken (Inst; preinst, Dateien in den Verzeichnisbaum,
    Dateilisten in die Paketdatenbank), 4 Einrichten (Conf; postinst, grün „installiert“). Oben das Schild „gesperrt“ der
    Sperrdatei, am Ende abgenommen."""
    s = Szene("linux/k9installieren", reihenfolge="anlegen")
    w = W_IN
    st = [(-2.745, 1.35), (-0.975, 1.95), (0.995, 1.75), (2.705, 1.43)]
    yb, hb = 1.2, 1.8
    stationen = []
    for i, (x, b) in enumerate(st):
        stationen += [box(s, (x, yb), b, hb, DUNKEL, WEISS, 2, "rect"), L(s, "s%d" % (i + 1), w["s%d" % (i + 1)], (x, 1.84), FM, "center",
                                                                          DUNKEL)]
    band = [pfk(s, (st[i][0] + st[i][1] / 2 + 0.01, yb), (st[i + 1][0] - st[i + 1][1] / 2 - 0.01, yb), DUNKEL, 2.5, spitze=0.07)
            for i in range(3)]
    schild = [box(s, (0, 2.8), 6.8, 0.3, ROT, ROT_HELL, 2, "rect"), L(s, "gesperrt", w["gesperrt"], (-0.55, 2.8), FM, "right", ROT),
              tx(s, "/var/lib/dpkg/lock-frontend", (-0.45, 2.8), TK, "left")]
    namen = ["jq", "libjq1", "libonig5"]
    ys = [1.15, 0.9, 0.65]
    auftrag = chip(s, (st[0][0], ys[0]), "jq", ORANGE, ORANGE_HELL, h=0.22)
    karten = [chip(s, (st[0][0], y), n, BLAU, BLAU_HELL, h=0.22) for n, y in zip(namen, ys)]
    xs = [st[0][0], st[1][0] - 0.3, st[2][0], st[3][0] - 0.15]
    l_aus = L(s, "aus3", w["aus3"], (st[0][0], 0.9), FM, "center", GRAU)
    srv = wchip(s, (st[1][0], 2.45), "server", w["server"], 0.95, GRAU, WEISS, h=0.24)
    p_srv = pfk(s, (st[1][0], 2.33), (st[1][0], yb + hb / 2 + 0.02), DUNKEL, 2)
    ok = flach([haken(s, xs[1] + 0.68, y, GRUEN, 0.07, 3) for y in ys])
    l_ok = L(s, "pruef", w["pruef"], (st[1][0], 0.4), FM, "center", GRUEN)
    cache = tx(s, "/var/cache/apt/archives", (st[1][0], 0.12), TK)
    pre = chip(s, (st[2][0], 1.45), "preinst", GRAU, WEISS, h=0.22, dash="4,4")
    post = chip(s, (st[3][0], 1.45), "postinst", GRAU, WEISS, h=0.22, dash="4,4")
    baum = wchip(s, (0.45, -0.38), "baum", W_BAUM, 1.45, GRAU, WEISS, h=0.3)
    db = wchip(s, (2.05, -0.38), "db2", W_EB["db2"], 1.45, GRAU, WEISS, h=0.44)
    p_ab = [pfk(s, (0.6, yb - hb / 2 - 0.01), (0.45, -0.21), DUNKEL, 2), pfk(s, (1.4, yb - hb / 2 - 0.01), (1.95, -0.14), DUNKEL, 2)]
    l_ab = [L(s, "dateien", w["dateien"], (0.4, 0.02), FM, "right", GRAU), L(s, "listen", w["listen"], (1.92, 0.06), FM, "left", GRAU)]
    gruen = [chip(s, (xs[3], y), n, GRUEN, GRUEN_HELL, h=0.22) for n, y in zip(namen, ys)]
    fertig = flach([haken(s, xs[3] + 0.6, y, GRUEN, 0.07, 3) for y in ys]) + [L(s, "inst", w["inst"], (st[3][0], 0.4), FM, "center",
                                                                                   GRUEN)]
    schritt(s, EIN(stationen + band + schild, 0.8))
    schritt(s, EIN(auftrag, 0.4))
    schritt(s, AUS(auftrag, 0.7), WACHS([k[0] for k in karten], 0.7), EIN([k[1] for k in karten], 0.7))
    s.pause(0.4)
    schritt(s, EIN(srv, 0.5), ZEICHNE(p_srv, 0.5))
    schritt(s, *VERS(karten, xs[1] - xs[0], 0, 1.0), EIN(l_aus, 1.0))
    schritt(s, EIN(ok + [l_ok, cache], 0.6))
    s.pause(0.4)
    schritt(s, *VERS(karten, xs[2] - xs[1], 0, 1.0), EIN(pre, 1.0))
    schritt(s, ZEICHNE(p_ab, 0.7), EIN(baum + db + l_ab, 0.7))
    s.pause(0.4)
    schritt(s, *VERS(karten, xs[3] - xs[2], 0, 1.0), EIN(post, 1.0))
    schritt(s, EIN(flach(gruen) + fertig, 0.6), AUS(flach(karten), 0.6))
    s.pause(0.3)
    schritt(s, AUS(schild, 0.6))
    s.speichern()


W_EN = {"r1": ("Programmdateien", "program files", "archivos del\nprograma", "程序文件", "fichiers du\nprogramme", "program\ndosyaları"),
        "r2": ("Konfigurations-\ndateien", "configuration\nfiles", "archivos de\nconfiguración", "配置文件", "fichiers de\nconfiguration",
               "yapılandırma\ndosyaları"),
        "r3": ("automatisch\ninstallierte\nBibliothek", "automatically\ninstalled\nlibrary", "biblioteca\ninstalada\nautomáticamente",
               "自动安装的\n库", "bibliothèque\ninstallée\nautomatiquement", "otomatik\nkurulan\nkütüphane"),
        "r4": ("Heimat-\nverzeichnis", "home\ndirectory", "directorio\npersonal", "主目录", "répertoire\npersonnel", "ev dizini"),
        "danach": ("danach", "afterwards", "después", "之后", "ensuite", "ardından"),
        "verwaist": ("verwaist", "orphaned", "huérfana", "无人需要", "orpheline", "sahipsiz"),
        "bleibt": ("bleibt", "stays", "se queda", "保留", "reste", "kalır")}


def k9entfernen():
    """Drei Spalten remove, purge, autoremove; Zeilen Programmdateien (/usr/…), Konfigurationsdateien (/etc/…), automatisch
    installierte Bibliothek (lib…), Heimatverzeichnis (~/…). remove: /usr weg, /etc bleibt, dpkg -l: rc, Bibliothek
    verwaist; purge: auch /etc weg; autoremove (danach, Ausgangszustand nach remove): die verwaiste Bibliothek weg. Das
    Heimatverzeichnis bleibt überall (grüner Haken)."""
    s = Szene("linux/k9entfernen", reihenfolge="anlegen")
    w = W_EN
    xs, ys = [-0.9, 0.75, 2.4], [1.85, 1.2, 0.55, -0.1]
    zellen = ["/usr/…", "/etc/…", "lib…", "~/…"]
    kopf = [tx(s, n, (x, 2.6), TK, "center", DUNKEL) for n, x in zip(("apt remove", "apt purge", "apt autoremove"), xs)]
    kopf += [L(s, "danach", w["danach"], (xs[2], 2.34), FM, "center", GRAU)]
    zeilen = [L(s, "r%d" % (i + 1), w["r%d" % (i + 1)], (-3.4, y), FM, "left", DUNKEL) for i, y in enumerate(ys)]
    trenn = [lin(s, (-3.4, (ys[i] + ys[i + 1]) / 2), (3.3, (ys[i] + ys[i + 1]) / 2), HELLGRAU, 1.5) for i in range(3)]
    bc = 1.05
    cell = {}
    for j, x in enumerate(xs):
        for i, y in enumerate(ys):
            if j == 2 and i == 0:
                cell[(i, j)] = [leer(s, (x, y), bc)]
            else:
                cell[(i, j)] = chip(s, (x, y), zellen[i], ORANGE if (j == 2 and i == 2) else BLAU,
                                    ORANGE_HELL if (j == 2 and i == 2) else BLAU_HELL, b=bc)
    l_v = {j: L(s, "verwaist", w["verwaist"], (xs[j], ys[2] - 0.25), FM, "center", ORANGE) for j in range(3)}
    rc = tx(s, "dpkg -l: rc", (xs[0], -0.62), TK, "center", DUNKEL)
    weg = {(i, j): leer(s, (xs[j], ys[i]), bc) for i, j in ((0, 0), (0, 1), (1, 1), (2, 2))}
    orange = {j: chip(s, (xs[j], ys[2]), "lib…", ORANGE, ORANGE_HELL, b=bc) for j in (0, 1)}
    ok = flach([haken(s, x + 0.68, ys[3], GRUEN, 0.07, 3) for x in xs]) + [L(s, "bleibt", w["bleibt"], (3.4, ys[3] - 0.27), FM,
                                                                                 "right", GRUEN)]
    schritt(s, EIN(kopf + zeilen + trenn + flach(list(cell.values())) + [l_v[2]], 0.8))
    s.pause(0.6)
    schritt(s, AUS(cell[(0, 0)], 0.6), EIN(weg[(0, 0)], 0.6))
    schritt(s, EIN(orange[0] + [l_v[0], rc], 0.6), AUS(cell[(2, 0)], 0.6))
    s.pause(0.5)
    schritt(s, AUS(cell[(0, 1)] + cell[(1, 1)], 0.6), EIN([weg[(0, 1)], weg[(1, 1)]], 0.6))
    schritt(s, EIN(orange[1] + [l_v[1]], 0.6), AUS(cell[(2, 1)], 0.6))
    s.pause(0.5)
    schritt(s, AUS(cell[(2, 2)] + [l_v[2]], 0.6), EIN(weg[(2, 2)], 0.6))
    s.pause(0.4)
    schritt(s, EIN(ok, 0.6))
    s.speichern()


W_UG = {"alt": ("alt", "old", "antigua", "旧", "ancienne", "eski"),
        "neu": ("neu", "new", "nueva", "新", "nouvelle", "yeni"),
        "konflikt": ("Konflikt mit D", "conflicts with D", "conflicto con D", "与 D 冲突", "conflit avec D", "D ile çakışma"),
        "entfernt": ("entfernt", "removed", "eliminado", "已移除", "supprimé", "kaldırıldı"),
        "test": ("Testsystem, apt -s upgrade: 126 Pakete aktualisierbar", "test system, apt -s upgrade: 126 packages upgradable",
                 "sistema de prueba, apt -s upgrade: 126 paquetes actualizables", "测试系统，apt -s upgrade：126 个软件包可升级",
                 "système de test, apt -s upgrade : 126 paquets à mettre à jour", "test sistemi, apt -s upgrade: 126 paket güncellenebilir"),
        "jetzt": ("121 jetzt", "121 now", "121 ahora", "121 个现在升级", "121 maintenant", "121 şimdi"),
        "spaeter": ("5 gestaffelt, später", "5 phased, later", "5 escalonados, más tarde", "5 个分阶段，稍后", "5 échelonnés, plus tard",
                    "5 kademeli, sonra")}
W_PAKETE = [("Paket %s" % c, "package %s" % c, "paquete %s" % c, "软件包 %s" % c, "paquet %s" % c, "paket %s" % c) for c in "ABCD"]


def k9upgrade():
    """Zwei Reihen mit den Paketen A–D (Versionsschild „alt“, darüber gestrichelt der Kandidat „neu“). apt upgrade: A und
    B bekommen ihren Kandidaten, C bleibt stehen (kept back), weil seine neue Version mit D in Konflikt steht. apt
    full-upgrade: auch C wird aktualisiert, D weicht (rot durchgestrichen, „entfernt“). Darunter der Balken des
    Testsystems: 126 aktualisierbar = 121 jetzt (grün) + 5 gestaffelt, später (grau), Blöcke s6_upgrade, s6_phasing."""
    s = Szene("linux/k9upgrade", reihenfolge="anlegen")
    w = W_UG
    xs, bk = [-1.4, -0.2, 1.0, 2.2], 0.95
    reihen = []
    for y, befehl in ((1.95, "apt upgrade"), (0.5, "apt full-upgrade")):
        r = {"kopf": tx(s, befehl, (-3.4, y), TK, "left", DUNKEL), "karten": [], "alt": [], "neu": []}
        for i, x in enumerate(xs):
            r["karten"] += [box(s, (x, y), bk, 0.62, BLAU, WEISS, 2, "rect"), L(s, "pk%d" % i, W_PAKETE[i], (x, y + 0.14), FM)]
            if i < 3:
                r["alt"].append(wchip(s, (x, y - 0.13), "alt", w["alt"], 0.6, GRAU, GRAU_HELL, h=0.22, textfarbe=DUNKEL))
            else:
                r["alt"].append(wchip(s, (x, y - 0.13), "inst", W_IN["inst"], 0.85, GRAU, GRAU_HELL, h=0.22, textfarbe=DUNKEL))
            r["neu"].append(wchip(s, (x, y + 0.5), "neu", w["neu"], 0.6, GRUEN, GRUEN_HELL, h=0.22) if i < 3 else [])
        reihen.append(r)
    r1, r2 = reihen
    kept = tx(s, "kept back", (xs[2], 1.95 - 0.47), TK, "center", ORANGE)
    konf = [lin(s, (xs[2] + 0.31, 2.45), (xs[3] - bk / 2, 2.2), ORANGE, 2, "4,4"),
            L(s, "konflikt", w["konflikt"], (xs[3] + 0.15, 2.48), FM, "center", ORANGE)]
    dx_, dy_ = xs[3], 0.5
    durch = [lin(s, (dx_ - bk / 2, dy_ + 0.31), (dx_ + bk / 2, dy_ - 0.31), ROT, 3), lin(s, (dx_ - bk / 2, dy_ - 0.31), (dx_ + bk / 2, dy_ + 0.31), ROT, 3)]
    l_weg = L(s, "entfernt", w["entfernt"], (dx_, dy_ - 0.47), FM, "center", ROT)
    yb, x0, x1 = -0.65, -3.35, 3.35
    xg = r4(x0 + (x1 - x0) * 121 / 126)
    balken = [lin(s, (x0, yb), (xg, yb), GRUEN, 14), lin(s, (xg, yb), (x1, yb), HELLGRAU, 14)]
    l_test = L(s, "test", w["test"], (x0, yb + 0.28), FM, "left", DUNKEL)
    l_b = [L(s, "jetzt", w["jetzt"], (x0, yb - 0.28), FM, "left", GRUEN), L(s, "spaeter", w["spaeter"], (x1, yb - 0.28), FM, "right", GRAU)]

    def zeile(r):
        return [r["kopf"]] + r["karten"] + flach(r["alt"]) + flach(r["neu"])
    schritt(s, EIN(zeile(r1), 0.8))
    s.pause(0.5)
    schritt(s, *[VER(i, 0, -0.63, 1.0) for k in (0, 1) for i in r1["neu"][k]], AUS(r1["alt"][0] + r1["alt"][1], 1.0))
    schritt(s, ZEICHNE(konf[0], 0.6), EIN([konf[1], kept], 0.6))
    s.pause(0.6)
    schritt(s, EIN(zeile(r2), 0.7))
    schritt(s, *[VER(i, 0, -0.63, 1.0) for k in (0, 1, 2) for i in r2["neu"][k]], AUS(r2["alt"][0] + r2["alt"][1] + r2["alt"][2], 1.0))
    schritt(s, ZEICHNE(durch, 0.6), EIN(l_weg, 0.6))
    s.pause(0.6)
    schritt(s, EIN(l_test, 0.5))
    schritt(s, ZEICHNE(balken[0], 1.0), EIN(l_b[0], 1.0))
    schritt(s, ZEICHNE(balken[1], 0.4), EIN(l_b[1], 0.4))
    s.speichern()


# ================================================================== Abschnitt 7: Warum man den Paketen trauen kann
def schluessel(s, x, y, farbe=ORANGE, fuellung=ORANGE_HELL, g=1.0):
    """Schlüssel waagrecht, Bart rechts (Ergebnis Liste); Mitte etwa (x, y), Breite 0,56·g."""
    return [s.kreis(None, r4(x - 0.18 * g), r4(y), r4(0.1 * g), farbe=farbe, dicke=2.5, fuellung=fuellung, deckung=1.0),
            lin(s, (x - 0.08 * g, y), (x + 0.28 * g, y), farbe, 4),
            lin(s, (x + 0.17 * g, y), (x + 0.17 * g, y - 0.08 * g), farbe, 3.5),
            lin(s, (x + 0.26 * g, y), (x + 0.26 * g, y - 0.1 * g), farbe, 3.5)]


def dok(s, x, y, b=0.42, h=0.52, rand=DUNKEL, fuellung=WEISS, linien=HELLGRAU):
    """Dokument mit drei angedeuteten Zeilen (Ergebnis Liste)."""
    teile = [box(s, (x, y), b, h, rand, fuellung, 2, "rect")]
    for k in range(3):
        yy = y + h / 2 - h * 0.25 - k * h * 0.22
        teile.append(lin(s, (x - b / 2 + 0.07, yy), (x + b / 2 - 0.07 - (0.07 if k == 2 else 0), yy), linien, 2))
    return teile


def siegel(s, x, y, r=0.09, farbe=ORANGE):
    return s.kreis(None, r4(x), r4(y), r, farbe=farbe, dicke=2, fuellung=farbe, deckung=0.9)


REL = ["Suite: resolute", PUNKTE, "SHA256:", " 92eb335c…  7581722 main/binary-amd64/Packages"]
PKG = ["Package: hello", PUNKTE, "SHA256: b6e9bef3…"]
W_KE = {"gesp": ("steht darüber", "stored above", "guardada arriba", "上面记录的", "notée au-dessus", "yukarıda kayıtlı"),
        "ber": ("berechnet", "computed", "calculada", "计算得出", "calculée", "hesaplanan"),
        "signiert": ("signiert", "signed", "firmada", "已签名", "signée", "imzalı"),
        "byte": ("1 Byte geändert", "1 byte changed", "1 byte cambiado", "改了 1 个字节", "1 octet modifié", "1 bayt değişti"),
        "ab": ("abgelehnt", "rejected", "rechazado", "拒绝", "rejeté", "reddedilir")}


def k9kette():
    """Kette der Prüfsummen: Release-Datei dists/resolute/InRelease (signiert) mit der Zeile 92eb335c… main/binary-amd64/
    Packages; der Wert wandert in die Vergleichszeile neben der Paketliste und trifft die berechnete Prüfsumme 92eb335c…
    (grünes =). In der Paketliste SHA256: b6e9bef3…, Vergleich mit der Paketdatei hello (grünes =). Zum Schluss die
    Fälschung gefaelscht.deb mit 7d4be4c4…: rotes, durchgestrichenes =, abgelehnt (Blöcke s7_*)."""
    s = Szene("linux/k9kette", reihenfolge="anlegen")
    w = W_KE
    r = s.datei("dists/resolute/InRelease", "\n".join(REL), pos=(-3.45, 2.95), groesse=TK)
    p = s.datei("main/binary-amd64/Packages", "\n".join(PKG), pos=(-3.45, 1.72), spalten=28, groesse=TK)
    sg = [siegel(s, r.rechts + 0.22, r.y(0), 0.12, ROT), L(s, "signiert", w["signiert"], (r.rechts + 0.42, r.y(0)), FM, "left", ROT)]
    xa, xe, xb = 0.75, 1.5, 2.25
    y1, y2, y3 = p.y(1), 0.45, -0.12
    kopf = [L(s, "gesp", w["gesp"], (xa, 1.84), FM, "center", GRAU), L(s, "ber", w["ber"], (xb, 1.84), FM, "center", GRAU)]
    m1 = r.markieren(3, 1, 9, ORANGE, 0.3)
    k1 = r.teil(3, 1, 9)
    a1 = pfk(s, (r.xr(9) + 0.05, r.y(3) - 0.04), (xa - 0.4, y1 + 0.04), GRAU, 1.5, "4,4")
    b1 = tx(s, "92eb335c…", (xb, y1), TK)
    eq1 = text(s, "=", (xe, y1), 28, "center", GRUEN)
    deb = chip(s, (-2.0, y2), HELLO_DEB, BLAU, BLAU_HELL)
    m2 = p.markieren(2, 8, 16, ORANGE, 0.3)
    k2 = p.teil(2, 8, 16)
    a2 = pfk(s, (p.xr(16) + 0.05, p.y(2) - 0.04), (xa - 0.4, y2 + 0.04), GRAU, 1.5, "4,4")
    b2 = tx(s, "b6e9bef3…", (xb, y2), TK)
    eq2 = text(s, "=", (xe, y2), 28, "center", GRUEN)
    fake = chip(s, (-2.0, y3), "gefaelscht.deb", ROT, ROT_HELL) + [L(s, "byte", w["byte"], (-2.0, y3 - 0.3), FM, "center", ROT)]
    k3 = p.teil(2, 8, 16)
    b3 = tx(s, "7d4be4c4…", (xb, y3), TK, "center", ROT)
    ne3 = [text(s, "=", (xe, y3), 28, "center", ROT), lin(s, (xe - 0.1, y3 - 0.13), (xe + 0.1, y3 + 0.13), ROT, 3),
           L(s, "ab", w["ab"], (xb + 0.5, y3), FM, "left", ROT)]
    schritt(s, EIN(r.id, 0.6))
    schritt(s, EIN(sg, 0.5))
    schritt(s, EIN(p.id, 0.6))
    s.pause(0.4)
    schritt(s, EIN([m1, k1] + kopf, 0.5))
    schritt(s, VER(k1, xa - r.xm(1, 9), y1 - r.y(3), 0.9), ZEICHNE(a1, 0.9))
    schritt(s, EIN(b1, 0.5))
    schritt(s, EIN(eq1, 0.5))
    s.pause(0.5)
    schritt(s, EIN(deb + [m2, k2], 0.5))
    schritt(s, VER(k2, xa - p.xm(8, 16), y2 - p.y(2), 0.9), ZEICHNE(a2, 0.9))
    schritt(s, EIN(b2, 0.5))
    schritt(s, EIN(eq2, 0.5))
    s.pause(0.6)
    schritt(s, EIN(fake + [k3], 0.5))
    schritt(s, VER(k3, xa - p.xm(8, 16), y3 - p.y(2), 1.0))
    schritt(s, EIN(b3, 0.5))
    schritt(s, EIN(ne3, 0.6))
    s.speichern()


W_SL = {"zufall": ("Zufallszahl", "random number", "número aleatorio", "随机数", "nombre aléatoire", "rastgele sayı"),
        "prog": ("Programm erzeugt\nein Schlüsselpaar", "a program creates\na key pair", "un programa crea\nun par de claves",
                 "程序生成\n一对密钥", "un programme crée\nune paire de clés", "program bir\nanahtar çifti üretir"),
        "geheim": ("geheimer Schlüssel", "private key", "clave privada", "私钥", "clé privée", "gizli anahtar"),
        "oeff": ("öffentlicher Schlüssel", "public key", "clave pública", "公钥", "clé publique", "açık anahtar"),
        "hin": ("beim Erzeugen\nberechnet", "computed when\ncreated", "calculada al\ncrearlas", "生成时\n计算得出", "calculée à\nla création",
                "üretilirken\nhesaplanır"),
        "zurueck": ("zurück: praktisch\nnicht ausrechenbar", "backwards: practically\nimpossible to compute",
                    "al revés: en la práctica\nno se puede calcular", "反向：实际上\n无法计算", "à rebours : pratiquement\nimpossible à calculer",
                    "geri: pratikte\nhesaplanamaz"),
        "tresor": ("Tresor bei Ubuntu", "safe at Ubuntu", "caja fuerte de Ubuntu", "Ubuntu 的保险箱", "coffre chez Ubuntu",
                   "Ubuntu'daki kasa"),
        "jeder": ("auf jedem Ubuntu-Rechner", "on every Ubuntu computer", "en cada equipo con Ubuntu", "在每台 Ubuntu 计算机上",
                  "sur chaque machine Ubuntu", "her Ubuntu bilgisayarında")}


def k9schluesselpaar():
    """Zufallszahl → Programm → zwei gleich gefärbte Schlüssel. Grüner Pfeil geheim → öffentlich („beim Erzeugen
    berechnet“), roter Pfeil zurück durchgestrichen („praktisch nicht ausrechenbar“). Der geheime Schlüssel kommt in den
    Tresor bei Ubuntu, Kopien des öffentlichen wandern auf drei Rechner (ubuntu-archive-keyring.gpg)."""
    s = Szene("linux/k9schluesselpaar", reihenfolge="anlegen")
    w = W_SL
    zuf = wchip(s, (-2.55, 2.65), "zufall", w["zufall"], 1.45, GRAU, WEISS, h=0.3)
    prog = wchip(s, (0.35, 2.65), "prog", w["prog"], 2.3, DUNKEL, GRAU_HELL, h=0.52)
    p_z = pfk(s, (-1.8, 2.65), (-0.84, 2.65), DUNKEL, 2.5)
    xg, xo, yk = -1.9, 1.9, 1.55
    kg = schluessel(s, xg, yk, g=1.3)
    ko = schluessel(s, xo, yk, g=1.3)
    p_k = [pfk(s, (0.0, 2.38), (xg + 0.2, yk + 0.2), DUNKEL, 2), pfk(s, (0.7, 2.38), (xo - 0.2, yk + 0.2), DUNKEL, 2)]
    l_k = [L(s, "geheim", w["geheim"], (xg, 1.22), FM, "center", DUNKEL), L(s, "oeff", w["oeff"], (xo, 1.22), FM, "center", DUNKEL)]
    hin = [pfk(s, (-0.92, 1.66), (1.42, 1.66), GRUEN, 2.5), L(s, "hin", w["hin"], (0.25, 1.92), FM, "center", GRUEN)]
    zur = [pfk(s, (1.42, 1.42), (-0.92, 1.42), ROT, 2.5), L(s, "zurueck", w["zurueck"], (0.25, 1.13), FM, "center", ROT)]
    nein = kreuz(s, 0.25, 1.42, 0.2)
    tresor = [box(s, (xg, 1.42), 1.75, 0.78, DUNKEL, WEISS, 4, "rect", deckung=0.0), s.kreis(None, xg + 0.72, 1.66, 0.06, farbe=DUNKEL,
                                                                                               dicke=2.5),
              L(s, "tresor", w["tresor"], (xg, 0.86), FM, "center", DUNKEL)]
    xs = [1.0, 1.9, 2.8]
    rech = flach([rechner(s, x, -0.05) for x in xs])
    kopien = [schluessel(s, xo, yk, g=1.3) for _ in xs]
    l_r = [tx(s, "ubuntu-archive-keyring.gpg", (1.9, -0.45), TK), L(s, "jeder", w["jeder"], (1.9, -0.72), FM, "center", GRAU)]
    schritt(s, EIN(zuf, 0.5))
    schritt(s, ZEICHNE(p_z, 0.5), EIN(prog, 0.5))
    schritt(s, ZEICHNE(p_k, 0.7), EIN(kg + ko + l_k, 0.7))
    s.pause(0.5)
    schritt(s, ZEICHNE(hin[0], 0.7), EIN(hin[1], 0.7))
    schritt(s, ZEICHNE(zur[0], 0.7), EIN(zur[1], 0.7))
    schritt(s, WACHS(nein, 0.5))
    s.pause(0.6)
    schritt(s, EIN(tresor, 0.7))
    schritt(s, EIN(rech + flach(kopien), 0.4))
    schritt(s, *[v for x, k in zip(xs, kopien) for v in VERS(k, x - xo, 0.36 - yk, 1.1)])
    schritt(s, EIN(l_r, 0.5))
    s.speichern()


W_SG = {"ubuntu": ("bei Ubuntu", "at Ubuntu", "en Ubuntu", "在 Ubuntu", "chez Ubuntu", "Ubuntu'da"),
        "release": ("Release-Datei", "Release file", "archivo Release", "Release 文件", "fichier Release", "Release dosyası"),
        "signieren": ("signieren", "sign", "firmar", "签名", "signer", "imzala"),
        "pruefen": ("prüfen", "verify", "verificar", "验证", "vérifier", "doğrula"),
        "mitsig": ("mit Signatur", "with signature", "con firma", "带签名", "avec signature", "imzalı")}


def k9signatur():
    """Links bei Ubuntu: Release-Datei und geheimer Schlüssel (mit Schloss) → „signieren“ → Release-Datei mit Signatur.
    Rechts auf dem eigenen Rechner: die Datei mit Signatur und der öffentliche Schlüssel → „prüfen“ (gpgv) → Good
    signature. Zweiter Durchgang: ein Byte unterwegs geändert → BAD signature. Der geheime Schlüssel bleibt links."""
    s = Szene("linux/k9signatur", reihenfolge="anlegen")
    w = W_SG
    zonen = [L(s, "ubuntu", w["ubuntu"], (-3.4, 2.95), FM, "left", GRAU), L(s, "rechner", W_UP["rechner"], (3.4, 2.95), FM, "right", GRAU),
             lin(s, (0.1, 3.0), (0.1, -0.2), HELLGRAU, 2, "6,5")]
    d_in = dok(s, -3.0, 1.55) + [L(s, "release", w["release"], (-3.0, 1.1), FM, "center")]
    kg = schluessel(s, -1.95, 2.42) + [s.schloss((-1.48, 2.42), 0.22, farbe=DUNKEL),
                                       L(s, "geheim", W_SL["geheim"], (-1.95, 2.72), FM, "center", DUNKEL)]
    m_l = wchip(s, (-1.95, 1.55), "signieren", w["signieren"], 1.05, DUNKEL, GRAU_HELL, h=0.55)
    p_l = [pfk(s, (-2.76, 1.55), (-2.5, 1.55), DUNKEL, 2), pfk(s, (-1.95, 2.3), (-1.95, 1.85), DUNKEL, 2),
           pfk(s, (-1.4, 1.55), (-0.9, 1.55), DUNKEL, 2)]
    aus = dok(s, -0.6, 1.55) + [siegel(s, -0.46, 1.37)]
    l_aus = L(s, "mitsig", w["mitsig"], (-0.6, 1.1), FM, "center")
    ko = schluessel(s, 1.65, 2.42) + [L(s, "oeff", W_SL["oeff"], (1.65, 2.72), FM, "center", DUNKEL)]
    m_r = [box(s, (1.65, 0.95), 0.95, 1.5, DUNKEL, GRAU_HELL, 2, "round"), L(s, "pruefen", w["pruefen"], (1.65, 1.5), FM, "center"),
           tx(s, "gpgv", (1.65, 1.27), TK)]
    p_k = pfk(s, (1.65, 2.3), (1.65, 1.72), DUNKEL, 2)
    ya, yb_ = 1.3, 0.5
    kopie_a = dok(s, -0.6, 1.55) + [siegel(s, -0.46, 1.37)]
    kopie_b = dok(s, -0.6, 1.55) + [siegel(s, -0.46, 1.37)]
    p_a = pfk(s, (0.88, ya), (1.15, ya), DUNKEL, 2)
    p_b = pfk(s, (0.88, yb_), (1.15, yb_), DUNKEL, 2)
    good = tx(s, "Good signature", (2.2, ya), TK, "left", GRUEN)
    bad = tx(s, "BAD signature", (2.2, yb_), TK, "left", ROT)
    byte = [box(s, (0.62, yb_ + 0.04), 0.16, 0.07, ROT, ROT, 1, "rect"), L(s, "byte", W_KE["byte"], (0.62, 0.03), FM, "center", ROT)]
    schritt(s, EIN(zonen, 0.5))
    schritt(s, EIN(d_in + kg + m_l, 0.7))
    schritt(s, ZEICHNE(p_l[:2], 0.5))
    schritt(s, ZEICHNE(p_l[2], 0.5), EIN(aus + [l_aus], 0.6))
    s.pause(0.5)
    schritt(s, EIN(ko + m_r, 0.6), ZEICHNE(p_k, 0.6))
    schritt(s, EIN(kopie_a, 0.3))
    schritt(s, *VERS(kopie_a, 1.25, ya - 1.55, 1.0))
    schritt(s, ZEICHNE(p_a, 0.4))
    schritt(s, EIN(good, 0.6))
    s.pause(0.6)
    schritt(s, EIN(kopie_b, 0.3))
    schritt(s, *VERS(kopie_b, 1.25, yb_ - 1.55, 1.0))
    schritt(s, EIN(byte, 0.5))
    schritt(s, ZEICHNE(p_b, 0.4))
    schritt(s, EIN(bad, 0.6))
    s.speichern()


W_SB = {"heute": ("mit Signed-By: jede Quelle hat ihren Schlüsselbund", "with Signed-By: each source has its own keyring",
                  "con Signed-By: cada fuente tiene su llavero", "使用 Signed-By：每个软件源有自己的密钥环",
                  "avec Signed-By : chaque source a son trousseau", "Signed-By ile: her kaynağın kendi anahtarlığı var"),
        "frueher": ("früher, ohne Signed-By: ein Schlüsselbund für alle Quellen", "formerly, without Signed-By: one keyring for all sources",
                    "antes, sin Signed-By: un llavero para todas las fuentes", "以前没有 Signed-By：所有软件源共用一个密钥环",
                    "autrefois, sans Signed-By : un trousseau pour toutes les sources",
                    "eskiden, Signed-By olmadan: tüm kaynaklar için tek anahtarlık"),
        "zus": ("zusätzliche\nQuelle", "extra\nsource", "fuente\nadicional", "附加\n软件源", "source\najoutée", "ek\nkaynak"),
        "angeblich": ("angeblich\nUbuntu", "supposedly\nUbuntu", "dice ser\nUbuntu", "自称\nUbuntu", "soi-disant\nUbuntu",
                      "güya\nUbuntu"),
        "gemeinsam": ("gemeinsamer\nSchlüsselbund", "shared\nkeyring", "llavero\ncomún", "共用的\n密钥环", "trousseau\ncommun", "ortak\nanahtarlık"),
        "gilt": ("auch die Fälschung gilt", "the forgery is accepted too", "también se acepta la falsificación", "伪造的也被接受",
                 "la falsification passe aussi", "sahtesi de kabul edilir")}


def k9signedby():
    """Oben (mit Signed-By): ubuntu.sources → /usr/share/keyrings/ubuntu-archive-keyring.gpg (drei Schlüssel, orange),
    beispiel.sources → /etc/apt/keyrings/beispiel.gpg (ein Schlüssel, blau). Eine Release-Datei der zusätzlichen Quelle
    mit blauem Siegel wird angenommen; dieselbe Signatur auf einer Datei, die vorgibt, von Ubuntu zu kommen, prallt am
    Schlüsselbund von Ubuntu ab. Unten der alte Zustand: ein gemeinsamer Bund mit allen Schlüsseln, die Fälschung gilt."""
    s = Szene("linux/k9signedby", reihenfolge="anlegen")
    w = W_SB
    xe, xk, bk, xd = -2.6, 0.62, 2.64, 2.35
    y1, y2 = 2.3, 1.35
    kopf = L(s, "heute", w["heute"], (-3.4, 2.92), FM, "left", GRAU)
    e1 = chip(s, (xe, y1), "ubuntu.sources", BLAU, BLAU_HELL)
    e2 = chip(s, (xe, y2), "beispiel.sources", BLAU, BLAU_HELL)

    def bund(y, z1, z2, farben):
        teile = [box(s, (xk, y), bk, 0.56, DUNKEL, WEISS, 2, "round"), tx(s, z1, (xk - bk / 2 + 0.1, y + 0.11), TK, "left"),
                 tx(s, z2, (xk - bk / 2 + 0.1, y - 0.11), TK, "left")]
        for k, f in enumerate(farben):
            yy = y + 0.12 * (len(farben) - 1) / 2 - 0.12 * k
            teile += schluessel(s, xk + bk / 2 - 0.3, yy, f, WEISS, g=0.5)
        return teile
    b1 = bund(y1, "/usr/share/keyrings/", "ubuntu-archive-keyring.gpg", [ORANGE] * 3)
    b2 = bund(y2, "/etc/apt/keyrings/", "beispiel.gpg", [BLAU])
    leinen = []
    for y, e in ((y1, e1), (y2, e2)):
        leinen += [lin(s, (xe + 0.75, y), (xk - bk / 2 - 0.02, y), DUNKEL, 2), tx(s, "Signed-By", (-1.31, y + 0.14), TK, "center", GRAU)]
    d1 = dok(s, xd + 0.6, y2, 0.36, 0.44) + [siegel(s, xd + 0.72, y2 - 0.14, 0.07, BLAU)]
    d2 = dok(s, xd + 0.6, y1, 0.36, 0.44) + [siegel(s, xd + 0.72, y1 - 0.14, 0.07, BLAU)]
    l_d = [L(s, "zus", w["zus"], (xd + 0.3, y2), FM, "left"), L(s, "angeblich", w["angeblich"], (xd + 0.3, y1), FM, "left")]
    ok1 = haken(s, xd, y2, GRUEN, 0.13, 4)
    nein = kreuz(s, xd, y1, 0.36)
    # früher
    yt = 0.78
    trenn = lin(s, (-3.4, yt), (3.4, yt), HELLGRAU, 1.5)
    kopf2 = L(s, "frueher", w["frueher"], (-3.4, yt - 0.2), FM, "left", GRAU)
    y3, y4, yg = 0.05, -0.6, -0.28
    e3 = chip(s, (xe, y3), "ubuntu.sources", BLAU, BLAU_HELL)
    e4 = chip(s, (xe, y4), "beispiel.sources", BLAU, BLAU_HELL)
    gem = [box(s, (xk, yg), bk, 0.66, DUNKEL, WEISS, 2, "round"), L(s, "gemeinsam", w["gemeinsam"], (xk - 0.35, yg), FM, "center")]
    for k, (dx, dy, f) in enumerate(((0.55, 0.12, ORANGE), (0.95, 0.12, ORANGE), (0.55, -0.12, ORANGE), (0.95, -0.12, BLAU))):
        gem += schluessel(s, xk + dx, yg + dy, f, WEISS, g=0.5)
    leinen2 = [lin(s, (xe + 0.68, y3), (xk - bk / 2 - 0.02, yg + 0.15), DUNKEL, 2),
               lin(s, (xe + 0.75, y4), (xk - bk / 2 - 0.02, yg - 0.15), DUNKEL, 2)]
    d3 = dok(s, xd + 0.6, yg, 0.36, 0.44) + [siegel(s, xd + 0.72, yg - 0.14, 0.07, BLAU)]
    l_d3 = L(s, "angeblich3", w["angeblich"], (xd + 0.3, yg), FM, "left")
    ok3 = haken(s, xd, yg, ORANGE, 0.13, 4)
    l_gilt = L(s, "gilt", w["gilt"], (xk, yg - 0.5), FM, "center", ROT)
    schritt(s, EIN([kopf] + e1 + e2 + b1 + b2, 0.7))
    schritt(s, ZEICHNE([leinen[0], leinen[2]], 0.6), EIN([leinen[1], leinen[3]], 0.6))
    s.pause(0.5)
    schritt(s, EIN(d1, 0.4))
    schritt(s, *VERS(d1, -0.6, 0, 0.7))
    schritt(s, EIN([l_d[0]] + ok1, 0.5))
    s.pause(0.4)
    schritt(s, EIN(d2, 0.4))
    schritt(s, *VERS(d2, -0.75, 0, 0.6))
    schritt(s, *VERS(d2, 0.15, 0, 0.4), WACHS(nein, 0.4))
    schritt(s, EIN(l_d[1], 0.5))
    s.pause(0.6)
    schritt(s, EIN([trenn, kopf2] + e3 + e4 + gem + leinen2, 0.7))
    schritt(s, EIN(d3, 0.4))
    schritt(s, *VERS(d3, -0.6, 0, 0.7))
    schritt(s, EIN([l_d3, l_gilt] + ok3, 0.5))
    s.speichern()


def minidok(s, x, y, rand=GRAU, fuellung=WEISS):
    return [box(s, (x, y), 0.2, 0.26, rand, fuellung, 1.5, "rect"), lin(s, (x - 0.05, y + 0.04), (x + 0.05, y + 0.04), rand, 1.5),
            lin(s, (x - 0.05, y - 0.04), (x + 0.05, y - 0.04), rand, 1.5)]


W_WG = {"s1": ("1 Entwickler", "1 developer", "1 desarrollador", "1 开发者", "1 développeur", "1 geliştirici"),
        "s2": ("2 Distribution", "2 distribution", "2 distribución", "2 发行版", "2 distribution", "2 dağıtım"),
        "s3": ("3 Hauptserver", "3 main server", "3 servidor\nprincipal", "3 主服务器", "3 serveur\nprincipal", "3 ana sunucu"),
        "s4": ("4 Spiegel", "4 mirror", "4 réplica", "4 镜像", "4 miroir", "4 yansı"),
        "s5": ("5 dein Rechner", "5 your computer", "5 tu ordenador", "5 你的计算机", "5 ton ordinateur", "5 bilgisayarın"),
        "quell": ("Quelltext\nGNU hello", "source code\nGNU hello", "código fuente\nGNU hello", "源代码\nGNU hello",
                  "code source\nGNU hello", "kaynak kodu\nGNU hello"),
        "fremd": ("fremder\nBetreiber", "third-party\noperator", "operador\najeno", "第三方\n运营者", "exploitant\ntiers", "yabancı\nişletmeci"),
        "angreifer": ("Angreifer", "attacker", "atacante", "攻击者", "attaquant", "saldırgan"),
        "c1": ("Siegel prüfen", "check the seal", "comprobar el sello", "检查签名", "vérifier le sceau", "mührü doğrula"),
        "c2": ("Prüfsumme der Liste", "list checksum", "suma de la lista", "列表的校验和", "somme de la liste", "liste sağlaması"),
        "c3": ("Prüfsumme des Pakets", "package checksum", "suma del paquete", "软件包的校验和", "somme du paquet", "paket sağlaması"),
        "c4": ("dpkg packt aus", "dpkg unpacks", "dpkg desempaqueta", "dpkg 解包", "dpkg dépaquette", "dpkg açar"),
        "aus": ("aussortiert", "rejected", "descartado", "被剔除", "écarté", "ayıklandı")}


def k9weg():
    """Fünf Stationen: 1 Entwickler (Quelltext GNU hello); 2 Distribution (hello_….deb, darüber Packages und InRelease, je
    über SHA256 verbunden, Siegel mit dem geheimen Schlüssel); 3 Hauptserver archive.ubuntu.com; 4 Spiegel (fremder
    Betreiber, http, gestrichelter Pfeil); 5 dein Rechner (apt update: Siegel, Prüfsumme der Liste; apt install: Prüfsumme des
    Pakets; dpkg packt aus). Ein Angreifer tauscht beim Spiegel eine Datei; bei Station 5 wird sie rot aussortiert."""
    s = Szene("linux/k9weg", reihenfolge="anlegen")
    w = W_WG
    st = [(-2.975, 0.95), (-1.525, 1.6), (-0.075, 0.95), (1.05, 0.95), (2.575, 1.75)]
    yb, hb = 1.6, 2.1
    rahmen_ = []
    for i, (x, b) in enumerate(st):
        rahmen_ += [box(s, (x, yb), b, hb, DUNKEL, WEISS, 2, "rect"), L(s, "s%d" % (i + 1), w["s%d" % (i + 1)], (x, 2.45), FM, "center",
                                                                          DUNKEL)]
    pfe = [pfk(s, (st[i][0] + st[i][1] / 2 + 0.01, yb), (st[i + 1][0] - st[i + 1][1] / 2 - 0.01, yb), DUNKEL, 2, "4,3" if i == 3 else "",
               spitze=0.07) for i in range(4)]
    s1 = minidok(s, st[0][0], 1.75, DUNKEL) + [L(s, "quell", w["quell"], (st[0][0], 1.2), FM, "center")]
    xc = st[1][0] - 0.2
    deb = chip(s, (xc, 0.92), "hello_….deb", BLAU, BLAU_HELL, h=0.24)
    pkg = chip(s, (xc, 1.45), "Packages", GRAU, WEISS, h=0.24) + [pfk(s, (xc, 1.05), (xc, 1.32), DUNKEL, 2, spitze=0.07),
                                                                    tx(s, "SHA256", (xc + 0.12, 1.19), TK, "left", GRAU)]
    rel = chip(s, (xc, 1.98), "InRelease", GRAU, WEISS, h=0.24) + [pfk(s, (xc, 1.58), (xc, 1.85), DUNKEL, 2, spitze=0.07),
                                                                     tx(s, "SHA256", (xc + 0.12, 1.72), TK, "left", GRAU)]
    sig = [siegel(s, xc + 0.6, 1.98, 0.08, ROT)] + schluessel(s, xc + 0.62, 2.22, ORANGE, ORANGE_HELL, g=0.5)
    s3 = flach([minidok(s, st[2][0] + dx, 1.75) for dx in (-0.27, 0, 0.27)]) + [tx(s, "archive.", (st[2][0], 1.22), TK),
                                                                                 tx(s, "ubuntu.com", (st[2][0], 1.02), TK)]
    s4_docs = [minidok(s, st[3][0] + dx, 1.75) for dx in (-0.27, 0, 0.27)]
    s4 = flach(s4_docs) + [L(s, "fremd", w["fremd"], (st[3][0], 1.2), FM, "center"), tx(s, "http", (st[3][0], 0.8), TK, "center", GRAU)]
    x5 = st[4][0] - st[4][1] / 2 + 0.1
    s5 = [tx(s, "apt update", (x5, 2.1), TK, "left", DUNKEL)]
    checks = []
    for key, y in (("c1", 1.86), ("c2", 1.62), ("c3", 1.1)):
        checks.append(haken(s, x5 + 0.08, y, GRUEN, 0.07, 3) + [L(s, key, w[key], (x5 + 0.22, y), FM, "left")])
    s5b = tx(s, "apt install", (x5, 1.35), TK, "left", DUNKEL)
    c4 = L(s, "c4", w["c4"], (x5, 0.8), FM, "left", GRUEN)
    ang = wchip(s, (st[3][0], 0.15), "angreifer", w["angreifer"], 0.95, ROT, ROT_HELL, h=0.28)
    falsch = minidok(s, st[3][0], 0.15, ROT, ROT_HELL)
    xf, yf = st[4][0] - 0.55, 0.15
    weg_ = kreuz(s, xf, yf, 0.3)
    l_weg = L(s, "aus", w["aus"], (xf + 0.25, yf), FM, "left", ROT)
    p_f = [pfk(s, (st[3][0] + 0.25, 0.3), (st[3][0] + 0.27, yb - hb / 2 - 0.02), ROT, 2, "4,3", spitze=0.07),
           pfk(s, (st[3][0] + 0.4, yb - hb / 2 - 0.02), (xf - 0.15, yf + 0.1), ROT, 2, "4,3", spitze=0.07)]
    schritt(s, EIN(rahmen_ + pfe, 0.8))
    schritt(s, EIN(s1, 0.5))
    schritt(s, EIN(deb, 0.4))
    schritt(s, EIN(pkg, 0.5))
    schritt(s, EIN(rel, 0.5))
    schritt(s, EIN(sig, 0.5))
    schritt(s, EIN(s3, 0.5))
    schritt(s, EIN(s4, 0.5))
    schritt(s, EIN([s5[0]] + checks[0] + checks[1], 0.6))
    schritt(s, EIN([s5b] + checks[2], 0.5))
    schritt(s, EIN(c4, 0.5))
    s.pause(0.6)
    schritt(s, EIN(ang + falsch, 0.5))
    schritt(s, *VERS(falsch, 0.27, 1.6, 0.8), AUS(s4_docs[2], 0.8), ZEICHNE(p_f[0], 0.8))
    schritt(s, *VERS(falsch, xf - st[3][0] - 0.27, yf - 1.75, 0.9), ZEICHNE(p_f[1], 0.9))
    schritt(s, WACHS(weg_, 0.5), EIN(l_weg, 0.5))
    s.speichern()


# ================================================================== Abschnitt 8: Aktualisieren als Schutz
W_RV = {"projekt": ("Projekt: neue Programmversion", "project: new program version", "proyecto: nueva versión del programa",
                    "项目：新的程序版本", "projet : nouvelle version du programme", "proje: yeni program sürümü"),
        "korr": ("Korrektur", "fix", "corrección", "修复", "correctif", "düzeltme"),
        "funk": ("neue Funktion", "new feature", "nueva función", "新功能", "nouvelle fonction", "yeni işlev"),
        "opt": ("geänderte Option", "changed option", "opción cambiada", "更改的选项", "option modifiée", "değişen seçenek"),
        "ubuntu": ("Ubuntu: nur die Korrektur übernehmen", "Ubuntu: take only the fix", "Ubuntu: solo se toma la corrección",
                   "Ubuntu：只取修复", "Ubuntu : reprendre seulement le correctif", "Ubuntu: yalnızca düzeltmeyi almak"),
        "vorh": ("vorhandene Version", "existing version", "versión existente", "现有版本", "version existante", "mevcut sürüm"),
        "bleibt": ("Programmversion bleibt", "program version stays", "la versión del programa sigue", "程序版本不变",
                   "version du programme inchangée", "program sürümü aynı"),
        "rev": ("Revision steigt", "revision goes up", "la revisión sube", "修订号增加", "la révision augmente", "revizyon artar")}


def k9revision():
    """Oben das Projekt: neue Programmversion mit Korrektur und weiteren Änderungen (Kärtchen). Unten Ubuntu: nur das
    Kärtchen „Korrektur“ wandert in die vorhandene Version sudo-rs 0.2.13; das Versionsschild 0.2.13-0ubuntu1 wird zu
    0.2.13-0ubuntu1.2 (Programmversion bleibt, Revision steigt); das Paket erscheint in resolute-security und
    resolute-updates (Block s8_sicherheit)."""
    s = Szene("linux/k9revision", reihenfolge="anlegen")
    w = W_RV
    oben = [box(s, (0, 2.2), 6.85, 1.05, BLAU, WEISS, 2, "rect"), L(s, "projekt", w["projekt"], (-3.3, 2.55), FM, "left", BLAU)]
    karten = []
    for k, (key, f, ff) in enumerate((("korr", GRUEN, GRUEN_HELL), ("funk", BLAU, BLAU_HELL), ("opt", ORANGE, ORANGE_HELL),
                                      ("funk", BLAU, BLAU_HELL))):
        karten.append(wchip(s, (r4(-2.48 + k * 1.62), 2.05), key, w[key], 1.48, f, ff, h=0.3))
    unten_t = L(s, "ubuntu", w["ubuntu"], (-3.4, 1.2), FM, "left", DUNKEL)
    xb, yb = -1.0, 0.55
    vorh = [box(s, (xb, yb), 2.9, 0.7, GRAU, GRAU_HELL, 2, "rect"), tx(s, "sudo-rs", (xb - 1.35, yb + 0.2), TK, "left", DUNKEL),
            L(s, "vorh", w["vorh"], (xb + 1.35, yb + 0.2), FM, "right", GRAU),
            leer(s, (xb, yb - 0.1), 1.5, 0.3)]
    korr = wchip(s, (-2.48, 2.05), "korr", w["korr"], 1.48, GRUEN, GRUEN_HELL, h=0.3)
    x0, yv = xb - 1.35, -0.12
    alt = tx(s, "0.2.13-0ubuntu1", (x0, yv), TT, "left")
    g = s.raster("0.2.13-0ubuntu1.2", (x0, yv), groesse=TT)
    mk = g.markieren(0, 7, 16, ORANGE, 0.3)
    k1, l1 = g.klammer(0, 0, 5, "", seite="unten", farbe=BLAU)
    k2, l2 = g.klammer(0, 7, 16, "", seite="unten", farbe=ORANGE)
    xl_ = g.xr(16) + 0.3
    def vor(p, ww):
        return tuple(p + (" : " if i == 4 else ("：" if i == 3 else ": ")) + v for i, v in enumerate(ww))
    lab = [Lr(s, "bleibt", vor("0.2.13", w["bleibt"]), (xl_, yv + 0.13), FM, "left", BLAU),
           Lr(s, "rev", vor("0ubuntu1 → 0ubuntu1.2", w["rev"]), (xl_, yv - 0.14), FM, "left", ORANGE)]
    p_r = pfk(s, (xb + 1.47, yb), (1.25, yb), DUNKEL, 2.5)
    aus = chip(s, (2.35, yb + 0.18), "resolute-security", GRUEN, GRUEN_HELL, h=0.26) + \
        chip(s, (2.35, yb - 0.18), "resolute-updates", GRUEN, GRUEN_HELL, h=0.26)
    schritt(s, EIN(oben, 0.6))
    schritt(s, EIN(flach(karten), 0.7))
    s.pause(0.6)
    schritt(s, EIN([unten_t] + vorh + [alt], 0.7))
    schritt(s, EIN(korr, 0.3), BETONE(karten[0][0], 0.6))
    schritt(s, *VERS(korr, xb - (-2.48), yb - 0.1 - 2.05, 1.1))
    s.pause(0.3)
    schritt(s, AUS(alt, 0.7), EIN(g.ids + [mk], 0.7))
    schritt(s, ZEICHNE([k1, k2], 0.5), EIN(lab, 0.5))
    s.pause(0.4)
    schritt(s, ZEICHNE(p_r, 0.5), EIN(aus, 0.6))
    s.speichern()


W_ZF = {"fehler": ("Fehler\nentsteht", "bug is\nintroduced", "surge el\nfallo", "缺陷\n产生", "le bogue\napparaît", "hata\noluşur"),
        "update": ("Update\nveröffentlicht", "update\npublished", "actualización\npublicada", "更新\n发布", "mise à jour\npubliée",
                   "güncelleme\nyayımlanır"),
        "angriffe": ("Angriffsversuche", "attack attempts", "intentos de ataque", "攻击尝试", "tentatives d'attaque", "saldırı girişimleri"),
        "a": ("A: am selben Tag", "A: the same day", "A: el mismo día", "A：当天", "A : le jour même", "A: aynı gün"),
        "b": ("B: nach einer Woche", "B: after a week", "B: tras una semana", "B：一周后", "B : après une semaine", "B: bir hafta sonra"),
        "c": ("C: nach drei Monaten", "C: after three months", "C: tras tres meses", "C：三个月后", "C : après trois mois", "C: üç ay sonra"),
        "fenster": ("rot: Zeitfenster, angreifbar", "red: time window, vulnerable", "rojo: ventana de tiempo, vulnerable",
                    "红色：时间窗口，可被攻击", "rouge : fenêtre de temps, vulnérable", "kırmızı: zaman penceresi, saldırıya açık"),
        "geschuetzt": ("grün: geschützt", "green: protected", "verde: protegido", "绿色：已受保护", "vert : protégé", "yeşil: korunuyor")}


def k9zeitfenster():
    """Zeitachse mit den Marken „Fehler entsteht“ und „Update veröffentlicht“; ab der Veröffentlichung steigt die rote Kurve
    „Angriffsversuche“. Darunter drei Rechner: A spielt das Update am selben Tag ein, B nach einer Woche, C nach drei
    Monaten; die roten Stücke (Zeitfenster) beginnen alle bei der Veröffentlichung, danach grün (geschützt). Schematisch."""
    s = Szene("linux/k9zeitfenster", reihenfolge="anlegen")
    w = W_ZF
    x0, x1, ya = -1.9, 3.3, 1.0
    xf, xu = -1.55, -0.45
    achse = [pfk(s, (x0, ya), (x1 + 0.1, ya), DUNKEL, 2.5), L(s, "zeit", W_AU["zeit"], (x1 + 0.1, ya - 0.2), FM, "right", GRAU)]
    marken = [lin(s, (xf, ya - 0.08), (xf, ya + 0.08), DUNKEL, 2.5), L(s, "fehler", w["fehler"], (xf, ya + 0.35), FM, "center", DUNKEL)]
    m_u = [lin(s, (xu, ya + 1.0), (xu, -0.45), DUNKEL, 1.5, "5,4"), L(s, "update", w["update"], (xu - 0.08, ya + 0.85), FM, "right", DUNKEL)]
    kurve = s.weg(None, "%s+%s*t" % (xu, r4(x1 - xu)), "%s+1.6*(1-exp(-4*t))" % ya, 0, 1, farbe=ROT, dicke=3, n=81)
    l_k = L(s, "angriffe", w["angriffe"], (1.6, 2.85), FM, "center", ROT)
    ys = [0.55, 0.15, -0.25]
    dauer = [0.07, 0.35, 2.85]
    basis, rot, gruen, namen = [], [], [], []
    for k, (y, d, key) in enumerate(zip(ys, dauer, ("a", "b", "c"))):
        basis.append(lin(s, (x0, y), (xu, y), HELLGRAU, 10))
        rot.append(lin(s, (xu, y), (xu + d, y), ROT, 10))
        gruen.append(lin(s, (xu + d, y), (x1, y), GRUEN, 10))
        namen.append(L(s, key, w[key], (-3.42, y), FM, "left", DUNKEL))
    leg = [L(s, "fenster", w["fenster"], (x0, -0.62), FM, "left", ROT), L(s, "geschuetzt", w["geschuetzt"], (x1, -0.62), FM, "right", GRUEN)]
    schritt(s, ZEICHNE(achse[0], 0.6), EIN(achse[1:] + marken, 0.6))
    s.pause(0.3)
    schritt(s, EIN(m_u, 0.6))
    schritt(s, ZEICHNE(kurve, 1.4), EIN(l_k, 1.4))
    s.pause(0.5)
    schritt(s, EIN(basis + namen, 0.6))
    for k in range(3):
        schritt(s, ZEICHNE(rot[k], 0.4 + 0.4 * k), ZEICHNE(gruen[k], 0.4 + 0.4 * k))
    schritt(s, EIN(leg, 0.6))
    s.speichern()


W_NS = {"name": ("Name im Verzeichnis:", "name in the directory:", "nombre en el directorio:", "目录中的名字：", "nom dans le répertoire :",
                 "dizindeki ad:"),
        "dienst": ("Dienst", "service", "servicio", "服务", "service", "hizmet"),
        "neu": ("Dienst, neu gestartet", "service, restarted", "servicio reiniciado", "服务，已重启", "service redémarré",
                "hizmet, yeniden başladı"),
        "alt": ("alte Fassung\nmit Lücke", "old version,\nvulnerable", "versión antigua\ncon fallo", "旧版本\n有漏洞", "ancienne version\nvulnérable",
                "eski sürüm\naçıklı"),
        "neuf": ("neue Fassung", "new version", "versión nueva", "新版本", "nouvelle version", "yeni sürüm"),
        "beendet": ("beendet", "ended", "terminado", "已结束", "terminé", "sona erdi"),
        "frei": ("freigegeben", "freed", "liberado", "已释放", "libéré", "serbest bırakıldı")}


def k9neustart():
    """Prozess „Dienst“ hängt an libbeispiel (Inode 1, orange, alte Fassung mit Lücke). Das Update legt
    libbeispiel.dpkg-new (Inode 2, grün) an und benennt um: der Name wandert zu Inode 2, Inode 1 trägt „(deleted)“, der
    Dienst hängt weiter daran. systemctl restart: der alte Prozess endet, Inode 1 wird freigegeben (verblasst), der neu
    gestartete Dienst hängt an Inode 2 (Versuch Block s8_geloescht)."""
    s = Szene("linux/k9neustart", reihenfolge="anlegen")
    w = W_NS
    xi1, xi2, yi = 0.0, 2.35, 1.05
    i1 = [box(s, (xi1, yi), 1.6, 0.72, ORANGE, ORANGE_HELL, 2.5, "rect"), text(s, "Inode 1", (xi1, yi + 0.2), FM, "center", DUNKEL),
          L(s, "alt", w["alt"], (xi1, yi - 0.1), FM, "center", ORANGE)]
    i2 = [box(s, (xi2, yi), 1.6, 0.72, GRUEN, GRUEN_HELL, 2.5, "rect"), text(s, "Inode 2", (xi2, yi + 0.12), FM, "center", DUNKEL),
          L(s, "neuf", w["neuf"], (xi2, yi - 0.13), FM, "center", GRUEN)]
    yn = 2.45
    l_name = L(s, "name", w["name"], (-3.42, yn), FM, "left", GRAU)
    name = chip(s, (xi1, yn), "libbeispiel", BLAU, BLAU_HELL) + [pfk(s, (xi1, yn - 0.15), (xi1, yi + 0.38), BLAU, 2)]
    neu = chip(s, (xi2, yn), "libbeispiel.dpkg-new", GRAU, WEISS) + [pfk(s, (xi2, yn - 0.15), (xi2, yi + 0.38), GRAU, 2)]
    xp = -2.45
    alt_p = [box(s, (xp, yi), 1.3, 0.45, ORANGE, WEISS, 2), L(s, "dienst", w["dienst"], (xp, yi), FM)]
    leine = lin(s, (xp + 0.66, yi), (xi1 - 0.81, yi), ORANGE, 3)
    deleted = tx(s, "(deleted)", (xi1, yi - 0.53), TK, "center", ROT)
    restart = chip(s, (xp, 0.32), "systemctl restart", DUNKEL, WEISS)
    yq = -0.25
    neu_p = [box(s, (xp, yq), 1.9, 0.45, GRUEN, WEISS, 2), L(s, "neu", w["neu"], (xp, yq), FM)]
    leine2 = pfk(s, (xp + 0.96, yq), (xi2, yi - 0.38), GRUEN, 3, knick="hv", spitze=0.09)
    grau = [schleier(s, (xp, yi), 1.4, 0.55, 0.7), schleier(s, ((xp + xi1) / 2 - 0.08, yi), 1.45, 0.12, 0.7),
            schleier(s, (xi1, yi), 1.7, 0.8, 0.7)]
    l_grau = [L(s, "beendet", w["beendet"], (xp, yi + 0.4), FM, "center", GRAU), L(s, "frei", w["frei"], (xi1, yi - 0.78), FM, "center",
                                                                                       GRAU)]
    schritt(s, EIN([l_name] + name + i1 + alt_p + [leine], 0.8))
    s.pause(0.6)
    schritt(s, EIN(neu + i2, 0.6))
    s.pause(0.4)
    schritt(s, AUS(neu, 1.0), *VERS(name, xi2 - xi1, 0, 1.0))
    schritt(s, EIN(deleted, 0.5))
    s.pause(0.7)
    schritt(s, EIN(restart, 0.5))
    schritt(s, EIN(grau + l_grau, 0.8))
    schritt(s, EIN(neu_p, 0.6), ZEICHNE(leine2, 0.8))
    s.speichern()


W_TI = {"daily": ("6 und 18 Uhr, je bis 12 h später", "6 am and 6 pm, up to 12 h later", "6 y 18 h, hasta 12 h más tarde",
                  "6 点和 18 点，最多晚 12 小时", "6 h et 18 h, jusqu'à 12 h plus tard", "06.00 ve 18.00, en çok 12 saat sonra"),
        "upgrade": ("6 Uhr, bis 60 min später", "6 am, up to 60 min later", "6 h, hasta 60 min más tarde", "6 点，最多晚 60 分钟",
                    "6 h, jusqu'à 60 min plus tard", "06.00, en çok 60 dakika sonra"),
        "aus": ("Laptop aus", "laptop off", "portátil apagado", "笔记本关机", "portable éteint", "dizüstü kapalı"),
        "verpasst": ("verpasst, wird beim Einschalten nachgeholt", "missed, caught up after switching on",
                     "perdido, se recupera al encender", "错过了，开机后补上", "manqué, rattrapé à l'allumage",
                     "kaçırıldı, açılınca yapılır")}


def k9timer():
    """24-Stunden-Zifferblatt: apt-daily mit Startmarken 6 und 18 Uhr und je einem Bogen von 12 h (zufällige Verschiebung,
    ein Punkt springt an eine zufällige Stelle); apt-daily-upgrade mit Marke 6 Uhr und Bogen bis 7 Uhr. Darunter ein
    Tagesstreifen eines Laptops, der nachts aus ist: der Lauf um 6 Uhr wird verpasst und beim Einschalten nachgeholt
    (Persistent=true). Daten Block s8_timer."""
    s = Szene("linux/k9timer", reihenfolge="anlegen")
    w = W_TI
    cx, cy, R = -1.95, 1.62, 0.9

    def pkt(h, r):
        a = math.radians(90 - 15 * h)
        return (r4(cx + r * math.cos(a)), r4(cy + r * math.sin(a)))

    def bogen(h0, h1, r, farbe, dicke):
        return s.weg(None, "%s+%s*cos(pi/2-(%s+%s*t)*pi/12)" % (cx, r, h0, h1 - h0), "%s+%s*sin(pi/2-(%s+%s*t)*pi/12)" % (cy, r, h0, h1 - h0),
                     0, 1, farbe=farbe, dicke=dicke, n=73)
    blatt = [s.kreis(None, cx, cy, R, farbe=DUNKEL, dicke=2.5, fuellung=WEISS, deckung=1.0)]
    blatt += [lin(s, pkt(h, R - (0.12 if h % 6 == 0 else 0.06)), pkt(h, R), DUNKEL if h % 6 == 0 else GRAU, 2) for h in range(24)]
    blatt += [text(s, str(h), pkt(h, R - 0.44), FM, "center", DUNKEL) for h in (0, 6, 12, 18)]
    hb = "#9cc3f0"
    b_daily = [bogen(6, 18, R + 0.12, hb, 9), bogen(18, 30, R + 0.26, hb, 9)]
    m_daily = [lin(s, pkt(6, R + 0.02), pkt(6, R + 0.36), BLAU, 4), lin(s, pkt(18, R + 0.02), pkt(18, R + 0.36), BLAU, 4)]
    punkt = s.kreis(None, *pkt(6, R + 0.12), 0.07, farbe=BLAU, dicke=2, fuellung=BLAU, deckung=1.0)
    b_up = bogen(6, 7, R - 0.2, "#f3a983", 9)
    m_up = lin(s, pkt(6, R - 0.3), pkt(6, R - 0.1), ORANGE, 4)
    xl = 0.0
    leg = [lin(s, (xl, 2.3), (xl + 0.3, 2.3), hb, 9), tx(s, "apt-daily", (xl + 0.42, 2.3), TK, "left", BLAU),
           Lr(s, "daily", w["daily"], (xl + 0.42, 2.05), FM, "left")]
    leg2 = [lin(s, (xl, 1.6), (xl + 0.3, 1.6), "#f3a983", 9), tx(s, "apt-daily-upgrade", (xl + 0.42, 1.6), TK, "left", ORANGE),
            Lr(s, "upgrade", w["upgrade"], (xl + 0.42, 1.35), FM, "left")]
    # Tagesstreifen
    ys, x0, dh = -0.42, -2.7, 0.25
    rech = rechner(s, -3.17, ys)
    streifen = [box(s, (x0 + 12 * dh, ys), 24 * dh, 0.24, GRAU, WEISS, 1.5, "rect"),
                box(s, (x0 + 4 * dh, ys), 8 * dh, 0.24, GRAU, GRAU_HELL, 1.5, "rect"),
                box(s, (x0 + 23 * dh, ys), 2 * dh, 0.24, GRAU, GRAU_HELL, 1.5, "rect"),
                L(s, "aus", w["aus"], (x0 + 4 * dh, ys), FM, "center", GRAU)]
    streifen += [text(s, str(h), (x0 + h * dh, ys - 0.27), FM, "center", GRAU) for h in (0, 6, 12, 18, 24)]
    m6 = lin(s, (x0 + 6 * dh, ys - 0.16), (x0 + 6 * dh, ys + 0.16), ORANGE, 4)
    nach = [pfk(s, (x0 + 6 * dh, ys + 0.2), (x0 + 8 * dh + 0.03, ys + 0.2), ORANGE, 2.5, knick="none", spitze=0.08),
            lin(s, (x0 + 8 * dh, ys - 0.16), (x0 + 8 * dh, ys + 0.16), GRUEN, 4),
            L(s, "verpasst", w["verpasst"], (x0 + 8 * dh + 0.15, ys + 0.5), FM, "left", ORANGE),
            tx(s, "Persistent=true", (x0 + 8 * dh + 0.15, ys + 0.26), TK, "left", DUNKEL)]
    schritt(s, EIN(blatt, 0.7))
    schritt(s, EIN(m_daily, 0.5))
    schritt(s, ZEICHNE(b_daily, 1.0), EIN(leg, 1.0))
    schritt(s, EIN(punkt, 0.3))
    schritt(s, DREH(punkt, -112, (cx, cy), 1.0))
    s.pause(0.4)
    schritt(s, EIN(m_up, 0.4))
    schritt(s, ZEICHNE(b_up, 0.6), EIN(leg2, 0.6))
    s.pause(0.6)
    schritt(s, EIN(rech + streifen, 0.7))
    schritt(s, EIN(m6, 0.5))
    schritt(s, ZEICHNE(nach[0], 0.6), EIN(nach[1:], 0.6))
    s.speichern()


W_PF = {"main": ("main: Sicherheitsupdates", "main: security updates", "main: actualizaciones de seguridad", "main：安全更新",
                 "main : mises à jour de sécurité", "main: güvenlik güncellemeleri"),
        "universe": ("universe: Sicherheitsupdates nur mit Ubuntu Pro", "universe: security updates only with Ubuntu Pro",
                     "universe: actualizaciones de seguridad solo con Ubuntu Pro", "universe：仅在 Ubuntu Pro 下有安全更新",
                     "universe : mises à jour de sécurité seulement avec Ubuntu Pro", "universe: güvenlik güncellemeleri yalnızca Ubuntu Pro ile"),
        "start": ("23.04.2026", "23 Apr 2026", "23/04/2026", "2026-04-23", "23/04/2026", "23.04.2026"),
        "ende": ("April 2031", "April 2031", "abril de 2031", "2031 年 4 月", "avril 2031", "Nisan 2031"),
        "keine": ("keine Updates\nmehr", "no more\nupdates", "ya sin\nactualizaciones", "不再\n有更新", "plus de\nmises à jour",
                  "artık\ngüncelleme yok"),
        "naechste": ("nächste LTS-Version", "next LTS version", "siguiente versión LTS", "下一个 LTS 版本", "version LTS suivante",
                     "sonraki LTS sürümü"),
        "wechsel": ("rechtzeitig wechseln", "switch in time", "cambiar a tiempo", "及时升级", "changer à temps", "zamanında geç")}


def k9pflege():
    """Zeitachse 2026–2032: grüner Balken „main: Sicherheitsupdates“ vom 23.04.2026 bis April 2031 mit Punkten für
    einzelne Updates, danach keine; gestrichelter Balken „universe: nur mit Ubuntu Pro“. Ein Pfeil zeigt rechtzeitig vor dem
    Ende auf einen neuen Balken „nächste LTS-Version“."""
    s = Szene("linux/k9pflege", reihenfolge="anlegen")
    w = W_PF

    def x(j):
        return r4(-2.9 + (j - 2026) * 0.95)
    ya = 0.3
    achse = [pfk(s, (x(2026) - 0.2, ya), (x(2032) + 0.4, ya), DUNKEL, 2.5)]
    achse += [lin(s, (x(j), ya - 0.06), (x(j), ya + 0.06), DUNKEL, 2) for j in range(2026, 2033)]
    achse += [text(s, str(j), (x(j), ya - 0.25), FM, "center", DUNKEL) for j in range(2026, 2033)]
    xs, xe = x(2026.31), x(2031.29)
    ym, yu, yn = 1.75, 0.88, 2.65
    main = lin(s, (xs, ym), (xe, ym), GRUEN, 20)
    l_main = [L(s, "main", w["main"], (xs, ym + 0.28), FM, "left", GRUEN), Lr(s, "start", w["start"], (xs, ym - 0.28), FM, "left", DUNKEL),
              Lr(s, "ende", w["ende"], (xe, ym - 0.28), FM, "center", DUNKEL)]
    jahre = [2026.45, 2026.62, 2026.86, 2027.1, 2027.4, 2027.72, 2028.0, 2028.35, 2028.7, 2029.08, 2029.45, 2029.8, 2030.2, 2030.55,
             2030.9, 2031.15]
    punkte = [s.kreis(None, x(j), ym, 0.045, farbe=WEISS, dicke=1.5, fuellung=WEISS, deckung=1.0) for j in jahre]
    keine = L(s, "keine", w["keine"], (xe + 0.15, ym), FM, "left", GRAU)
    uni = [lin(s, (xs, yu), (x(2032), yu), "#9cc79f", 20, "10,8"), L(s, "universe", w["universe"], (xs, yu + 0.28), FM, "left", DUNKEL)]
    xw = x(2030)
    nae = [lin(s, (x(2028.3), yn), (x(2032) + 0.3, yn), "#7fc29b", 20), L(s, "naechste", w["naechste"], (x(2028.3), yn + 0.28), FM, "left",
                                                                            DUNKEL)]
    wechsel = [pfk(s, (xw, ym + 0.12), (xw, yn - 0.13), ORANGE, 3), L(s, "wechsel", w["wechsel"], (xw - 0.1, (ym + yn) / 2 + 0.05), FM,
                                                                       "right", ORANGE)]
    schritt(s, EIN(achse, 0.6))
    schritt(s, ZEICHNE(main, 1.2), EIN(l_main[:2], 1.2))
    schritt(s, EIN(punkte, 0.8), EIN(l_main[2], 0.8))
    schritt(s, EIN(keine, 0.5))
    s.pause(0.4)
    schritt(s, ZEICHNE(uni[0], 0.8), EIN(uni[1], 0.8))
    s.pause(0.5)
    schritt(s, ZEICHNE(nae[0], 0.8), EIN(nae[1], 0.8))
    schritt(s, ZEICHNE(wechsel[0], 0.6), EIN(wechsel[1], 0.6))
    s.speichern()


# ================================================================== Abschnitt 9: Alternativen
W_AL = {"allg": ("allgemeiner Name", "generic name", "nombre genérico", "通用名称", "nom générique", "genel ad"),
        "gruppe": ("Gruppe awk", "group awk", "grupo awk", "awk 组", "groupe awk", "awk grubu"),
        "p10": ("Priorität 10", "priority 10", "prioridad 10", "优先级 10", "priorité 10", "öncelik 10"),
        "p5": ("Priorität 5", "priority 5", "prioridad 5", "优先级 5", "priorité 5", "öncelik 5"),
        "auto": ("automatisch", "automatic", "automático", "自动", "automatique", "otomatik"),
        "manuell": ("manuell", "manual", "manual", "手动", "manuel", "elle"),
        "zaehlt": ("manuell: Prioritäten\nzählen nicht", "manual: priorities\ndo not count", "manual: las prioridades\nno cuentan",
                   "手动：优先级\n不起作用", "manuel : les priorités\nne comptent pas", "elle: öncelikler\nsayılmaz"),
        "folge": ("Folgelink (slave):", "follower link (slave):", "enlace dependiente (slave):", "从属链接（slave）：",
                  "lien suiveur (slave) :", "bağlı bağlantı (slave):")}


def k9alternativen():
    """/usr/bin/awk → /etc/alternatives/awk → Kandidaten auf Sockeln: /usr/bin/gawk (Priorität 10, höher) und
    /usr/bin/mawk (5). Schalter „automatisch“: der Pfeil zeigt auf den höheren Sockel; der Folgelink awk.1.gz zeigt auf
    gawk.1.gz. Zum Schluss Schalter „manuell“: der Pfeil schwenkt auf mawk, der Folgelink wechselt auf mawk.1.gz, die
    Prioritäten zählen nicht mehr (Block s9_awk)."""
    s = Szene("linux/k9alternativen", reihenfolge="anlegen")
    w = W_AL
    ya = 2.5
    a = chip(s, (-2.45, ya), "/usr/bin/awk", BLAU, BLAU_HELL)
    b = chip(s, (0.25, ya), "/etc/alternatives/awk", BLAU, BLAU_HELL)
    p_ab = pfk(s, (-2.45 + chipb("/usr/bin/awk") / 2 + 0.02, ya), (0.25 - chipb("/etc/alternatives/awk") / 2 - 0.03, ya), DUNKEL, 2.5)
    l_a = L(s, "allg", w["allg"], (-2.45, ya - 0.3), FM, "center", GRAU)
    P = (0.25, ya - 0.16)
    yb_, hs = 0.0, 0.42
    gx = -1.2
    gy, my = yb_ + 2 * hs + 0.14, yb_ + hs + 0.14
    tg = (gx, gy + 0.16)
    d = math.hypot(tg[0] - P[0], tg[1] - P[1])
    dy = P[1] - (my + 0.16)
    mx = r4(P[0] + math.sqrt(d * d - dy * dy))
    tm = (mx, my + 0.16)
    winkel = round(math.degrees(math.atan2(tm[1] - P[1], tm[0] - P[0]) - math.atan2(tg[1] - P[1], tg[0] - P[0])), 2)
    sockel = [box(s, (gx, yb_ + hs), 1.3, 2 * hs, GRAU, GRAU_HELL, 2, "rect"), L(s, "p10", w["p10"], (gx, yb_ + hs), FM, "center", DUNKEL),
              box(s, (mx, yb_ + hs / 2), 1.3, hs, GRAU, GRAU_HELL, 2, "rect"), L(s, "p5", w["p5"], (mx, yb_ + hs / 2), FM, "center", DUNKEL)]
    gawk = chip(s, (gx, gy), "/usr/bin/gawk", GRUEN, GRUEN_HELL)
    mawk = chip(s, (mx, my), "/usr/bin/mawk", GRUEN, GRUEN_HELL)
    l_gr = L(s, "gruppe", w["gruppe"], (-3.4, yb_ + 0.2), FM, "left", GRAU)
    pfeil = pfk(s, P, (tg[0], tg[1] + 0.02), DUNKEL, 2.5)
    xs_, ys_ = -2.75, 1.35
    schalter = [box(s, (xs_, ys_), 0.6, 0.26, GRAU, WEISS, 2, "round")]
    knopf = s.kreis(None, xs_ - 0.15, ys_, 0.09, farbe=BLAU, dicke=2, fuellung=BLAU, deckung=1.0)
    l_mode = L(s, "auto", w["auto"], (xs_, ys_ + 0.3), FM, "center", BLAU)
    yf = -0.42
    folge = [L(s, "folge", w["folge"], (-0.5, yf), FM, "right", GRAU), tx(s, "awk.1.gz", (-0.4, yf), TK, "left"),
             pfk(s, (0.25, yf), (0.6, yf), DUNKEL, 2, spitze=0.08)]
    ziel = tx(s, "gawk.1.gz", (0.7, yf), TK, "left", GRUEN)
    l_z = L(s, "zaehlt", w["zaehlt"], (-3.4, 0.92), FM, "left", ORANGE)
    grau = [schleier(s, (gx, yb_ + hs), 1.1, 0.26, 0.6), schleier(s, (mx, yb_ + hs / 2), 1.1, 0.26, 0.6)]
    schritt(s, EIN(a + b + [l_a], 0.6), ZEICHNE(p_ab, 0.6))
    schritt(s, EIN(sockel + gawk + mawk + [l_gr], 0.7))
    s.pause(0.4)
    schritt(s, EIN(schalter + [knopf, l_mode], 0.5))
    schritt(s, ZEICHNE(pfeil, 0.7))
    schritt(s, EIN(folge + [ziel], 0.6))
    s.pause(0.8)
    with s.gleichzeitig():
        s.ersetzen(l_mode, T(s, "manuell", *w["manuell"]), farbe=ORANGE, dauer=0.9)
        s.ersetzen(ziel, "mawk.1.gz", dauer=0.9)
        schritt(s, VER(knopf, 0.3, 0, 0.9), DREH(pfeil, winkel, P, 0.9))
    schritt(s, EIN(grau + [l_z], 0.6))
    s.speichern()


W_SD = {"kein": ("angelegt von update-alternatives, in keinem Paket", "created by update-alternatives, in no package",
                 "creados por update-alternatives, en ningún paquete", "由 update-alternatives 创建，不属于任何软件包",
                 "créés par update-alternatives, dans aucun paquet", "update-alternatives oluşturur, hiçbir pakette değil"),
        "rs": ("Paket sudo-rs\nPriorität 50", "package sudo-rs\npriority 50", "paquete sudo-rs\nprioridad 50", "软件包 sudo-rs\n优先级 50",
               "paquet sudo-rs\npriorité 50", "paket sudo-rs\nöncelik 50"),
        "ws": ("Paket sudo\nPriorität 40", "package sudo\npriority 40", "paquete sudo\nprioridad 40", "软件包 sudo\n优先级 40",
               "paquet sudo\npriorité 40", "paket sudo\nöncelik 40"),
        "auto": ("automatisch: höchste Priorität", "automatic: highest priority", "automático: prioridad más alta", "自动：最高优先级",
                 "automatique : priorité la plus haute", "otomatik: en yüksek öncelik"),
        "folge": ("Folgelinks (slave):", "follower links (slave):", "enlaces dependientes (slave):", "从属链接（slave）：",
                  "liens suiveurs (slave) :", "bağlı bağlantılar (slave):")}


def k9sudo():
    """Kette /usr/bin/sudo → /etc/alternatives/sudo (Klammer: angelegt von update-alternatives, in keinem Paket) →
    /usr/lib/cargo/bin/sudo auf dem Sockel „Paket sudo-rs, Priorität 50“; daneben /usr/bin/sudo.ws auf „Paket sudo,
    Priorität 40“. dpkg -S /usr/bin/sudo fragt beim ersten Glied an: no path found. Unten die Folgelinks sudo.8.gz →
    sudo-rs.8.gz und visudo → /usr/lib/cargo/bin/visudo (Block s9_sudo)."""
    s = Szene("linux/k9sudo", reihenfolge="anlegen")
    w = W_SD
    ya = 2.3
    na, nb = "/usr/bin/sudo", "/etc/alternatives/sudo"
    xa_, xb_ = -2.35, 0.35
    a = chip(s, (xa_, ya), na, BLAU, BLAU_HELL)
    b = chip(s, (xb_, ya), nb, BLAU, BLAU_HELL)
    p_ab = pfk(s, (xa_ + chipb(na) / 2 + 0.02, ya), (xb_ - chipb(nb) / 2 - 0.03, ya), DUNKEL, 2.5)
    kl = klammer(s, xa_ - chipb(na) / 2, xb_ + chipb(nb) / 2, ya + 0.22, unten=False, farbe=GRAU, t=0.07, dicke=2)
    l_kl = L(s, "kein", w["kein"], ((xa_ + xb_) / 2, ya + 0.42), FM, "center", GRAU)
    frage = tx(s, "dpkg -S /usr/bin/sudo", (xa_, 1.55), TK)
    p_fr = pfk(s, (xa_, 1.68), (xa_, ya - 0.16), DUNKEL, 2)
    nein = tx(s, "no path found", (xa_, 1.27), TK, "center", ROT)
    yb_ = 0.0
    nc, nw = "/usr/lib/cargo/bin/sudo", "/usr/bin/sudo.ws"
    h50, h40 = 0.75, 0.6
    xc, xw = xb_, 2.55
    soc = [box(s, (xc, yb_ + h50 / 2), 2.15, h50, GRAU, GRAU_HELL, 2, "rect"), L(s, "rs", w["rs"], (xc, yb_ + h50 / 2), FM, "center", DUNKEL),
           box(s, (xw, yb_ + h40 / 2), 1.6, h40, GRAU, GRAU_HELL, 2, "rect"), L(s, "ws", w["ws"], (xw, yb_ + h40 / 2), FM, "center", DUNKEL)]
    c = chip(s, (xc, yb_ + h50 + 0.14), nc, GRUEN, GRUEN_HELL)
    ws = chip(s, (xw, yb_ + h40 + 0.14), nw, GRAU, WEISS)
    pfeil = pfk(s, (xb_, ya - 0.16), (xc, yb_ + h50 + 0.3), DUNKEL, 2.5)
    l_auto = L(s, "auto", w["auto"], (xb_ + 0.15, 1.55), FM, "left", BLAU)
    yf = -0.38
    folge = [L(s, "folge", w["folge"], (-3.4, yf), FM, "left", GRAU), tx(s, "sudo.8.gz → sudo-rs.8.gz", (-1.0, yf), TK, "left"),
             tx(s, "visudo → /usr/lib/cargo/bin/visudo", (-1.0, yf - 0.27), TK, "left")]
    schritt(s, EIN(a + b, 0.5), ZEICHNE(p_ab, 0.6))
    schritt(s, ZEICHNE(kl, 0.5), EIN(l_kl, 0.6))
    s.pause(0.4)
    schritt(s, EIN(frage, 0.5), ZEICHNE(p_fr, 0.5))
    schritt(s, EIN(nein, 0.5))
    s.pause(0.6)
    schritt(s, EIN(soc + c + ws, 0.7))
    schritt(s, ZEICHNE(pfeil, 0.7), EIN(l_auto, 0.7))
    s.pause(0.4)
    schritt(s, EIN(folge, 0.6))
    s.speichern()


W_CU = {"virt": ("virtueller Name, Platz für genau ein Paket", "virtual name, room for exactly one package",
                 "nombre virtual, sitio para un solo paquete", "虚拟名称，只能容纳一个软件包", "nom virtuel, place pour un seul paquet",
                 "sanal ad, yalnızca bir paketlik yer"),
        "aus": ("ausgeschlossen (Conflicts)", "excluded (Conflicts)", "excluidos (Conflicts)", "被排除（Conflicts）", "exclus (Conflicts)",
                "dışlanır (Conflicts)"),
        "multi": ("Multicall-Programm", "multicall program", "programa multillamada", "多调用程序", "programme multi-appel",
                  "çok çağrılı program"),
        "tausch": ("Tausch: coreutils-from-gnu rückt in den Rahmen, alle Links zeigen auf gnu-coreutils;\n"
                   "rust-coreutils und gnu-coreutils bleiben installiert",
                   "swap: coreutils-from-gnu moves into the frame, all links point to gnu-coreutils;\n"
                   "rust-coreutils and gnu-coreutils stay installed",
                   "cambio: coreutils-from-gnu entra en el marco, todos los enlaces van a gnu-coreutils;\n"
                   "rust-coreutils y gnu-coreutils siguen instalados",
                   "互换：coreutils-from-gnu 进入框内，所有链接指向 gnu-coreutils；\nrust-coreutils 和 gnu-coreutils 仍保持安装",
                   "échange : coreutils-from-gnu entre dans le cadre, tous les liens vont vers gnu-coreutils ;\n"
                   "rust-coreutils et gnu-coreutils restent installés",
                   "değişim: coreutils-from-gnu çerçeveye girer, tüm bağlantılar gnu-coreutils'e gider;\n"
                   "rust-coreutils ve gnu-coreutils kurulu kalır")}


def k9coreutils():
    """Oben der virtuelle Name coreutils-from als gestrichelter Rahmen (Platz für ein Paket) mit coreutils-from-uutils;
    rechts grau ausgeschlossen -gnu, -busybox, -toybox (Conflicts). Links des Pakets: ls, cat, date → rust-coreutils
    (Multicall-Programm), cp, mv, rm, df, true → gnu-coreutils (gnucp, gnumv, …). Unten der gedachte Tausch als Hinweis
    (gestrichelter Pfeil von coreutils-from-gnu zum Rahmen). Blöcke s9_coreutils, s9_depends."""
    s = Szene("linux/k9coreutils", reihenfolge="anlegen")
    w = W_CU
    xr_, yr_ = -1.25, 2.4
    rahmen_ = [box(s, (xr_, yr_), 2.25, 0.44, DUNKEL, WEISS, 2, "round", dash="6,5"), tx(s, "coreutils-from", (-3.4, 2.85), TK, "left", DUNKEL),
               L(s, "virt", w["virt"], (-3.4 + ttb("coreutils-from") + 0.15, 2.85), FM, "left", GRAU)]
    uu = chip(s, (xr_, yr_), "coreutils-from-uutils", BLAU, BLAU_HELL)
    xw = 2.35
    warten = [chip(s, (xw, 2.42 - 0.31 * k), n, GRAU, WEISS, textfarbe=GRAU)
              for k, n in enumerate(("coreutils-from-gnu", "coreutils-from-busybox", "coreutils-from-toybox"))]
    l_w = L(s, "aus", w["aus"], (xw, 1.55), FM, "center", GRAU)
    yl, yp = 1.3, 0.3
    links_a = [("ls", -2.9), ("cat", -2.4), ("date", -1.85)]
    links_b = [("cp", -0.3), ("mv", 0.2), ("rm", 0.7), ("df", 1.2), ("true", 1.75)]
    ka, kb, la, lb, pa, pb = [], [], [], [], [], []
    for n, x in links_a + links_b:
        k = chip(s, (x, yl), n, BLAU, WEISS, h=0.26)
        l_ = lin(s, (xr_, yr_ - 0.23), (x, yl + 0.14), HELLGRAU, 1.5)
        rust = (n, x) in links_a
        p_ = pfk(s, (x, yl - 0.14), (-2.35 if rust else 0.73, yp + 0.33), DUNKEL, 1.5, spitze=0.07)
        (ka if rust else kb).append(k)
        (la if rust else lb).append(l_)
        (pa if rust else pb).append(p_)
    rust_b = [box(s, (-2.35, yp), 1.95, 0.62, DUNKEL, GRAU_HELL, 2, "rect"), tx(s, "rust-coreutils", (-2.35, yp + 0.13), TK),
              L(s, "multi", w["multi"], (-2.35, yp - 0.14), FM, "center", GRAU)]
    gnu_b = [box(s, (0.73, yp), 2.6, 0.62, DUNKEL, GRAU_HELL, 2, "rect"), tx(s, "gnu-coreutils", (0.73, yp + 0.13), TK),
             tx(s, "gnucp, gnumv, …", (0.73, yp - 0.14), TK, "center", GRAU)]
    p_t = pfk(s, (xw - chipb("coreutils-from-gnu") / 2 - 0.03, 2.42), (xr_ + 1.15, 2.42), ORANGE, 2, "5,4")
    l_t = L(s, "tausch", w["tausch"], (-3.4, -0.4), FM, "left", ORANGE)
    schritt(s, EIN(rahmen_, 0.6))
    schritt(s, EIN(uu, 0.5))
    schritt(s, EIN(flach(warten) + [l_w], 0.6))
    s.pause(0.5)
    schritt(s, ZEICHNE(la, 0.6), EIN(flach(ka), 0.6))
    schritt(s, EIN(rust_b, 0.5), ZEICHNE(pa, 0.6))
    s.pause(0.4)
    schritt(s, ZEICHNE(lb, 0.6), EIN(flach(kb), 0.6))
    schritt(s, EIN(gnu_b, 0.5), ZEICHNE(pb, 0.6))
    s.pause(0.6)
    schritt(s, ZEICHNE(p_t, 0.7), EIN(l_t, 0.7))
    s.speichern()


W_GS = {"befehl": ("Befehl: coreutils-from-gnu rein, coreutils-from-uutils raus", "command: coreutils-from-gnu in, coreutils-from-uutils out",
                   "orden: entra coreutils-from-gnu, sale coreutils-from-uutils", "命令：装入 coreutils-from-gnu，移除 coreutils-from-uutils",
                   "commande : coreutils-from-gnu entre, coreutils-from-uutils sort",
                   "komut: coreutils-from-gnu girer, coreutils-from-uutils çıkar"),
        "weg": ("wird entfernt", "removed", "se elimina", "将被移除", "supprimé", "kaldırılır"),
        "rein": ("wird installiert", "installed", "se instala", "将被安装", "installé", "kurulur"),
        "nicht": ("automatisch installiert, nicht mehr gebraucht", "automatically installed, no longer needed",
                  "instalados automáticamente, ya no necesarios", "自动安装，已不再需要", "installés automatiquement, plus nécessaires",
                  "otomatik kurulmuş, artık gerekmiyor")}


def k9geschuetzt():
    """Kettenreaktion beim Wechsel der Grundbefehle (Block s9_wechsel): coreutils-from-uutils (Protected: yes) wird rot
    entfernt; build-essential hängt davon ab (Depends) und wird ebenfalls rot; der Pfeil zu den Paketen, die es
    mitgebracht hat (g++, g++-15, g++-x86-64-linux-gnu, g++-15-x86-64-linux-gnu, libstdc++-15-dev, libcrypt-dev),
    verschwindet, sie werden orange „automatisch installiert, nicht mehr gebraucht“. coreutils-from-gnu wird grün. Oben
    das Warnschild von apt."""
    s = Szene("linux/k9geschuetzt", reihenfolge="anlegen")
    w = W_GS
    warn = [box(s, (0, 2.68), 5.35, 0.5, ROT, ROT_HELL, 2, "rect"),
            tx(s, "WARNING: The following essential packages will be removed.", (-2.55, 2.8), TK, "left", ROT),
            tx(s, "This should NOT be done unless you know exactly what you are doing!", (-2.55, 2.56), TK, "left", ROT)]
    befehl = L(s, "befehl", w["befehl"], (0, 2.08), FM, "center", DUNKEL)
    xu, yu = -1.35, 1.5
    uu = chip(s, (xu, yu), "coreutils-from-uutils", BLAU, BLAU_HELL)
    tag = chip(s, (xu + 1.5, yu), "Protected: yes", GRAU, GELB, textfarbe=DUNKEL)
    gnu = chip(s, (2.45, yu), "coreutils-from-gnu", GRAU, WEISS, textfarbe=GRAU)
    yb = 0.75
    be = chip(s, (xu, yb), "build-essential", BLAU, BLAU_HELL)
    p_dep = pfk(s, (xu, yb + 0.15), (xu, yu - 0.15), DUNKEL, 2)
    l_dep = tx(s, "Depends", (xu + 0.1, (yb + yu) / 2), TK, "left", GRAU)
    reihen = [["g++", "g++-15", "g++-x86-64-linux-gnu"], ["g++-15-x86-64-linux-gnu", "libstdc++-15-dev", "libcrypt-dev"]]
    yg = [-0.05, -0.4]
    rahmen_g = box(s, (0, -0.225), 5.2, 0.72, GRAU, WEISS, 1.5, "round", dash="5,4")
    gruppe, orange_ = [], []
    for r, y in zip(reihen, yg):
        breite = sum(chipb(n) for n in r) + 0.12 * (len(r) - 1)
        x = -breite / 2
        for n in r:
            bb = chipb(n)
            gruppe.append(chip(s, (r4(x + bb / 2), y), n, BLAU, BLAU_HELL, h=0.26))
            orange_.append(chip(s, (r4(x + bb / 2), y), n, ORANGE, ORANGE_HELL, h=0.26))
            x += bb + 0.12
    p_g = pfk(s, (xu, yb - 0.15), (xu, 0.15), DUNKEL, 2)
    l_nicht = L(s, "nicht", w["nicht"], (0, -0.8), FM, "center", ORANGE)
    uu_r = chip(s, (xu, yu), "coreutils-from-uutils", ROT, ROT_HELL)
    be_r = chip(s, (xu, yb), "build-essential", ROT, ROT_HELL)
    gnu_g = chip(s, (2.45, yu), "coreutils-from-gnu", GRUEN, GRUEN_HELL)
    l_weg = [L(s, "weg", w["weg"], (xu - 1.05, yu), FM, "right", ROT), L(s, "weg", w["weg"], (xu - 0.8, yb), FM, "right", ROT)]
    l_rein = L(s, "rein", w["rein"], (2.45, yu - 0.3), FM, "center", GRUEN)
    schritt(s, EIN(uu + tag + be + [l_dep, rahmen_g] + flach(gruppe), 0.8), ZEICHNE([p_dep, p_g], 0.8))
    schritt(s, EIN(gnu, 0.5))
    s.pause(0.6)
    schritt(s, EIN(befehl, 0.6))
    schritt(s, EIN(uu_r + [l_weg[0]], 0.6), AUS(uu, 0.6))
    schritt(s, EIN(be_r + [l_weg[1]], 0.6), AUS(be, 0.6))
    schritt(s, AUS([p_g] + flach(gruppe), 0.8), EIN(flach(orange_) + [l_nicht], 0.8))
    schritt(s, EIN(gnu_g + [l_rein], 0.6), AUS(gnu, 0.6))
    s.pause(0.4)
    schritt(s, EIN(warn, 0.6))
    s.speichern()


# ================================================================== Abschnitt 10: Software von außerhalb
W_FQ = {"titel": ("gedacht: eine zusätzliche Quelle bietet sudo-rs an", "imagined: an extra source offers sudo-rs",
                  "supuesto: una fuente adicional ofrece sudo-rs", "设想：一个附加软件源提供 sudo-rs",
                  "supposons : une source ajoutée propose sudo-rs", "varsayım: ek bir kaynak sudo-rs sunuyor"),
        "ubuntu": ("Ubuntu", "Ubuntu", "Ubuntu", "Ubuntu", "Ubuntu", "Ubuntu"),
        "zus": ("zusätzliche Quelle (Version erfunden)", "extra source (made-up version)", "fuente adicional (versión inventada)",
                "附加软件源（版本为虚构）", "source ajoutée (version inventée)", "ek kaynak (uydurma sürüm)"),
        "prio": ("1. höchste Priorität: 500 = 500, Gleichstand", "1. highest priority: 500 = 500, a tie",
                 "1. prioridad más alta: 500 = 500, empate", "1. 最高优先级：500 = 500，平局", "1. priorité la plus haute : 500 = 500, égalité",
                 "1. en yüksek öncelik: 500 = 500, eşit"),
        "vers": ("2. Version: 0.3.0-1 ist höher als 0.2.13-0ubuntu1.2", "2. version: 0.3.0-1 is higher than 0.2.13-0ubuntu1.2",
                 "2. versión: 0.3.0-1 es mayor que 0.2.13-0ubuntu1.2", "2. 版本：0.3.0-1 高于 0.2.13-0ubuntu1.2",
                 "2. version : 0.3.0-1 est plus haute que 0.2.13-0ubuntu1.2", "2. sürüm: 0.3.0-1, 0.2.13-0ubuntu1.2'den yüksek"),
        "schloss": ("Signed-By prüft, wer die Liste unterschrieben hat,\nnicht, welche Pakete darin stehen",
                    "Signed-By checks who signed the list,\nnot which packages it contains",
                    "Signed-By comprueba quién firmó la lista,\nno qué paquetes contiene", "Signed-By 检查谁签署了列表，\n不检查其中有哪些软件包",
                    "Signed-By vérifie qui a signé la liste,\npas quels paquets elle contient",
                    "Signed-By listeyi kimin imzaladığını denetler,\nhangi paketleri içerdiğini değil")}


def k9fremdquelle():
    """Versionstabelle von sudo-rs wie bei apt policy mit zwei Quellen: Ubuntu 0.2.13-0ubuntu1.2 (500 resolute-updates,
    500 resolute-security) und eine zusätzliche Quelle 0.3.0-1 (500 pakete.example.org, Version erfunden). Erst Priorität
    (Gleichstand), dann Version: das Schild Candidate wandert zur zusätzlichen Quelle. Schloss an ihrer Liste: Signed-By
    prüft, wer unterschrieben hat, nicht, welche Pakete darin stehen."""
    s = Szene("linux/k9fremdquelle", reihenfolge="anlegen")
    w = W_FQ
    titel = [tx(s, "$ apt policy sudo-rs", (0, 2.88), TK, "center", DUNKEL), L(s, "titel", w["titel"], (0, 2.62), FM, "center", GRAU)]
    xa, xb, yc, hc = -1.72, 1.72, 1.7, 1.08
    va, vb = "0.2.13-0ubuntu1.2", "0.3.0-1"
    karte_a = [box(s, (xa, yc), 3.2, hc, BLAU, WEISS, 2.5, "rect"), L(s, "ubuntu", w["ubuntu"], (xa, yc + 0.36), FM, "center", GRAU),
               tx(s, va, (xa, yc + 0.12), TT), tx(s, "500", (xa - 1.45, yc - 0.14), TK, "left"),
               tx(s, "resolute-updates", (xa - 1.05, yc - 0.14), TK, "left", GRAU), tx(s, "500", (xa - 1.45, yc - 0.37), TK, "left"),
               tx(s, "resolute-security", (xa - 1.05, yc - 0.37), TK, "left", GRAU)]
    karte_b = [box(s, (xb, yc), 3.2, hc, ORANGE, WEISS, 2.5, "rect"), L(s, "zus", w["zus"], (xb, yc + 0.36), FM, "center", GRAU),
               tx(s, vb, (xb, yc + 0.12), TT), tx(s, "500", (xb - 1.45, yc - 0.14), TK, "left"),
               tx(s, "pakete.example.org", (xb - 1.05, yc - 0.14), TK, "left", GRAU)]
    ys = yc - hc / 2 - 0.22
    cand = chip(s, (xa, ys), "Candidate", GRUEN, GRUEN_HELL, h=0.26)
    mk = [box(s, (r4(px + 0.113), r4(py)), 0.34, 0.2, ORANGE, ORANGE, 0, "rect", deckung=0.35)
          for px, py in ((xa - 1.45, yc - 0.14), (xa - 1.45, yc - 0.37), (xb - 1.45, yc - 0.14))]
    l_prio = L(s, "prio", w["prio"], (0, ys - 0.38), FM, "center", ORANGE)
    vb_ = [box(s, (xb, yc + 0.12), ttb(vb, TT) + 0.12, 0.25, GRUEN, WEISS, 2.5, deckung=0.0),
           box(s, (xa, yc + 0.12), ttb(va, TT) + 0.12, 0.25, GRAU, WEISS, 2.5, deckung=0.0)]
    l_vers = Lr(s, "vers", w["vers"], (0, ys - 0.64), FM, "center", GRUEN)
    schl = s.schloss((r4(xb - 1.05 + ttb("pakete.example.org") + 0.25), r4(yc - 0.14)), 0.24, farbe=DUNKEL)
    l_schl = L(s, "schloss", w["schloss"], (0, ys - 1.1), FM, "center", DUNKEL)
    schritt(s, EIN(titel, 0.5))
    schritt(s, EIN(karte_a + cand, 0.7))
    s.pause(0.6)
    schritt(s, EIN(karte_b, 0.6))
    s.pause(0.4)
    schritt(s, EIN(mk + [l_prio], 0.6))
    schritt(s, EIN(vb_ + [l_vers], 0.6))
    s.pause(0.3)
    schritt(s, *VERS(cand, xb - xa, 0, 0.9))
    s.pause(0.4)
    schritt(s, WACHS(schl, 0.6), EIN(l_schl, 0.6))
    s.speichern()


def warndreieck(s, x, y, g=0.26, farbe=ORANGE):
    h = g * 0.87
    a, b, c = (x - g / 2, y - h / 2), (x + g / 2, y - h / 2), (x, y + h / 2)
    return [lin(s, a, b, farbe, 2.5), lin(s, b, c, farbe, 2.5), lin(s, c, a, farbe, 2.5),
            text(s, "!", (r4(x), r4(y - h * 0.12)), FM, "center", farbe)]


W_EZ = {"braucht": ("braucht: libonig5", "needs: libonig5", "necesita: libonig5", "需要：libonig5", "requiert : libonig5",
                    "gerektirir: libonig5"),
        "keinhaken": ("kein Haken der Kette:\nnicht aus einer Paketliste", "no tick from the chain:\nnot from a package list",
                      "sin la marca de la cadena:\nno viene de una lista", "没有信任链的勾：\n不是来自软件包列表",
                      "pas de coche de la chaîne :\npas issu d'une liste", "zincir onayı yok:\nbir paket listesinden değil"),
        "ausgepackt": ("ausgepackt", "unpacked", "desempaquetado", "已解包", "dépaqueté", "açıldı"),
        "fehlt": ("libonig5 fehlt", "libonig5 missing", "falta libonig5", "缺少 libonig5", "libonig5 manque", "libonig5 eksik"),
        "nicht": ("nicht eingerichtet", "not configured", "no configurado", "未配置", "non configuré", "yapılandırılmadı"),
        "holt": ("libonig5 aus den Paketquellen, geprüft", "libonig5 from the repositories, verified",
                 "libonig5 de los repositorios, verificado", "libonig5 来自软件源，已校验", "libonig5 depuis les dépôts, vérifié",
                 "libonig5 paket depolarından, doğrulandı"),
        "beide": ("beide eingerichtet", "both configured", "ambos configurados", "两者都已配置", "les deux configurés",
                  "ikisi de yapılandırıldı")}


def k9einzeldatei():
    """Oben werkzeug_1.4_amd64.deb (erfunden) „braucht: libonig5“, daneben ein leerer gestrichelter Kreis: kein Haken der
    Kette, nicht aus einer Paketliste. Links sudo dpkg -i: ausgepackt, libonig5 fehlt, nicht eingerichtet (Warnzeichen),
    dpkg -l: iU. Rechts sudo apt install ./werkzeug_1.4_amd64.deb: libonig5 aus den Paketquellen (geprüft), ausgepackt,
    beide eingerichtet, dpkg -l: ii."""
    s = Szene("linux/k9einzeldatei", reihenfolge="anlegen")
    w = W_EZ
    datei = "werkzeug_1.4_amd64.deb"
    oben = chip(s, (0.2, 2.62), datei, ORANGE, ORANGE_HELL) + [L(s, "braucht", w["braucht"], (0.2 + chipb(datei) / 2 + 0.12, 2.62), FM,
                                                                     "left", DUNKEL)]
    kein = [s.kreis(None, -1.0, 2.62, 0.13, farbe=GRAU, dicke=2, dash="4,3"),
            L(s, "keinhaken", w["keinhaken"], (-1.22, 2.62), FM, "right", GRAU)]
    trenn = lin(s, (0, 2.25), (0, 0.2), HELLGRAU, 2, "6,5")
    kopf = [tx(s, "sudo dpkg -i " + datei, (-1.75, 2.0), TK, "center", DUNKEL),
            tx(s, "sudo apt install ./" + datei, (1.75, 2.0), TK, "center", DUNKEL)]
    ys = [1.55, 1.2, 0.85]
    xl, xr = -3.3, 0.25
    links = [haken(s, xl, ys[0], GRUEN, 0.07, 3) + [L(s, "ausgepackt", w["ausgepackt"], (xl + 0.17, ys[0]), FM, "left")],
             [kreuz(s, xl, ys[1], 0.16), L(s, "fehlt", w["fehlt"], (xl + 0.17, ys[1]), FM, "left", ROT)],
             warndreieck(s, xl, ys[2]) + [L(s, "nicht", w["nicht"], (xl + 0.17, ys[2]), FM, "left", ORANGE)],
             [tx(s, "dpkg -l: iU", (xl - 0.08, 0.45), TK, "left", ORANGE)]]
    rechts = [haken(s, xr, ys[0], GRUEN, 0.07, 3) + [L(s, "holt", w["holt"], (xr + 0.17, ys[0]), FM, "left")],
              haken(s, xr, ys[1], GRUEN, 0.07, 3) + [L(s, "ausgepackt", w["ausgepackt"], (xr + 0.17, ys[1]), FM, "left")],
              haken(s, xr, ys[2], GRUEN, 0.07, 3) + [L(s, "beide", w["beide"], (xr + 0.17, ys[2]), FM, "left", GRUEN)],
              [tx(s, "dpkg -l: ii", (xr - 0.08, 0.45), TK, "left", GRUEN)]]
    schritt(s, EIN(oben, 0.6))
    schritt(s, EIN(kein, 0.6))
    s.pause(0.4)
    schritt(s, EIN(kopf + [trenn], 0.5))
    for teil in links:
        schritt(s, EIN(teil, 0.45))
    s.pause(0.5)
    for teil in rechts:
        schritt(s, EIN(teil, 0.45))
    s.speichern()


W_CB = {"sieht": ("← du siehst nur eine leere Zeile", "← you see only an empty line", "← solo ves una línea vacía", "← 你只看到一行空白",
                  "← tu ne vois qu'une ligne vide", "← yalnızca boş bir satır görürsün"),
        "pipe": ("Pipe", "pipe", "tubería", "管道", "tube", "boru"),
        "fuehrt": ("bash führt jede Zeile\nsofort aus", "bash runs each line\nat once", "bash ejecuta cada línea\nen el acto",
                   "bash 立即执行\n每一行", "bash exécute chaque\nligne aussitôt", "bash her satırı\nhemen çalıştırır"),
        "z1": ("Zeile 1", "line 1", "línea 1", "第 1 行", "ligne 1", "satır 1"),
        "z2": ("Zeile 2", "line 2", "línea 2", "第 2 行", "ligne 2", "satır 2"),
        "root": ("jetzt mit root", "now as root", "ahora como root", "现在以 root 运行", "maintenant en root", "şimdi root olarak"),
        "abbruch": ("Verbindung\nbricht ab", "connection\ndrops", "se corta la\nconexión", "连接\n中断", "la connexion\ncoupe",
                    "bağlantı\nkopar"),
        "halb": ("halbe Zeile wird ausgeführt", "half a line is run", "se ejecuta media línea", "半行被执行", "une demi-ligne est exécutée",
                 "yarım satır çalıştırılır"),
        "sicher": ("sicherer Weg:", "safer way:", "camino más seguro:", "更安全的做法：", "voie plus sûre :", "daha güvenli yol:"),
        "s1": ("1 in eine Datei laden", "1 download to a file", "1 guardarlo en archivo", "1 下载到文件", "1 le télécharger",
               "1 dosyaya indir"),
        "s2": ("2 lesen: less datei", "2 read: less file", "2 leer: less archivo", "2 阅读：less 文件", "2 lire : less fichier",
               "2 oku: less dosya"),
        "s3": ("3 ausführen: bash datei", "3 run: bash file", "3 ejecutar: bash archivo", "3 运行：bash 文件", "3 lancer : bash fichier",
               "3 çalıştır: bash dosya")}


def k9curlbash():
    """Terminal: curl -fsSL https://example.org/install.sh | bash wird getippt, danach nur eine leere Zeile. Darunter
    Server (install.sh) → curl → Pipe → bash: Zeilen des Skripts laufen einzeln durch die Pipe und werden sofort
    ausgeführt (Liste unter bash); die Zeile mit sudo ist rot („jetzt mit root“). Dann bricht die Verbindung ab, und bash
    führt die halbe Zeile aus. Unten der sicherere Weg in drei Kästchen."""
    s = Szene("linux/k9curlbash", reihenfolge="anlegen")
    w = W_CB
    t = s.terminal(pos=(-3.45, 2.95), spalten=74, zeilen=2, prompt=P9, titel=TITEL, groesse=18)
    l_sieht = L(s, "sieht", w["sieht"], (t.x(2), t.y(1)), FM, "left", "#8a8990")
    yf = 1.4
    srv = [box(s, (-2.95, yf), 0.95, 0.6, DUNKEL, GRAU_HELL, 2, "rect"), L(s, "server", W_DO["server"], (-2.95, yf + 0.13), FM),
           tx(s, "install.sh", (-2.95, yf - 0.13), TK)]
    p_sc = pfk(s, (-2.46, yf), (-2.1, yf), DUNKEL, 2.5)
    curl = [box(s, (-1.7, yf), 0.75, 0.42, DUNKEL, WEISS, 2, "round"), tx(s, "curl", (-1.7, yf), TT)]
    pipe = [lin(s, (-1.32, yf), (1.12, yf), HELLGRAU, 12), L(s, "pipe", w["pipe"], (-0.1, yf + 0.24), FM, "center", GRAU)]
    xb_ = 1.75
    bash = [box(s, (xb_, yf), 1.25, 0.42, DUNKEL, WEISS, 2, "round"), tx(s, "bash", (xb_, yf), TT),
            L(s, "fuehrt", w["fuehrt"], (xb_, yf + 0.5), FM, "center", DUNKEL)]
    ys = [0.95, 0.68, 0.41, 0.14]
    karten = [wchip(s, (-1.0, yf), "z1", w["z1"], 0.8, GRAU, WEISS, h=0.24), wchip(s, (-1.0, yf), "z2", w["z2"], 0.8, GRAU, WEISS, h=0.24),
              chip(s, (-1.0, yf), "sudo …", ROT, ROT_HELL, h=0.24, b=0.8),
              [box(s, (-1.19, yf), 0.42, 0.24, ORANGE, ORANGE_HELL, 2, "rect", dash="3,3")]]
    marken = [haken(s, xb_ + 0.55, ys[0], GRUEN, 0.07, 3), haken(s, xb_ + 0.55, ys[1], GRUEN, 0.07, 3),
              [L(s, "root", w["root"], (xb_ - 0.55, ys[2]), FM, "right", ROT)],
              [L(s, "halb", w["halb"], (xb_ - 0.55, ys[3]), FM, "right", ORANGE)]]
    abbruch = [kreuz(s, -2.28, yf, 0.2), L(s, "abbruch", w["abbruch"], (-2.95, yf - 0.55), FM, "center", ROT)]
    ysi = -0.48
    sicher = [L(s, "sicher", w["sicher"], (-3.4, ysi), FM, "left", GRUEN)]
    for k, x in enumerate((-1.3, 0.45, 2.2)):
        sicher += wchip(s, (x, ysi), "s%d" % (k + 1), w["s%d" % (k + 1)], 1.65, GRUEN, GRUEN_HELL, h=0.3)
    schritt(s, EIN(t.id, 0.6))
    t.eingabe("curl -fsSL https://example.org/install.sh | bash", dauer=2.0)
    with s.gleichzeitig():
        t.warten(1.0)
        s.einblenden(l_sieht)
    schritt(s, EIN(srv + [p_sc] + curl + pipe + bash, 0.7))
    for k, (kt, mk) in enumerate(zip(karten, marken)):
        if k == 3:
            schritt(s, EIN(abbruch, 0.5))
        schritt(s, EIN(kt, 0.25))
        dx = xb_ - (-1.0)
        schritt(s, *VERS(kt, dx, 0, 0.7))
        schritt(s, *VERS(kt, 0, ys[k] - yf, 0.4), EIN(mk, 0.4))
    s.pause(0.5)
    schritt(s, EIN(sicher, 0.7))
    s.speichern()


W_SN = {"dist": ("Pakete der Distribution", "distribution packages", "paquetes de la distribución", "发行版的软件包",
                 "paquets de la distribution", "dağıtım paketleri"),
        "snaps": ("Snaps", "snaps", "snaps", "Snap 包", "snaps", "snap'ler"),
        "luecke": ("Lücke gefunden", "vulnerability found", "fallo encontrado", "发现漏洞", "faille trouvée", "açık bulundu"),
        "ein": ("ein Update genügt", "one update is enough", "basta una actualización", "一次更新就够了", "une mise à jour suffit",
                "tek güncelleme yeter"),
        "jede": ("jeder Hersteller einzeln", "each vendor separately", "cada fabricante por separado", "各厂商分别更新",
                 "chaque éditeur séparément", "her üretici ayrı ayrı")}
W_PROG = [("Programm %d" % k, "program %d" % k, "programa %d" % k, "程序 %d" % k, "programme %d" % k, "program %d" % k) for k in (1, 2, 3)]


def warnpunkt(s, x, y, r=0.1):
    return [s.kreis(None, r4(x), r4(y), r, farbe=ROT, dicke=2, fuellung=ROT, deckung=1.0), text(s, "!", (r4(x), r4(y)), FM, "center", WEISS)]


def k9snap():
    """Links „Pakete der Distribution“: drei Programme → eine gemeinsame libbeispiel. Rechts „Snaps“: drei Kapseln mit je
    Programm und eigener Kopie von libbeispiel. Eine Lücke (rotes Zeichen an allen Kopien): links ein Update, alle Pfeile
    grün; rechts wird jede Kapsel einzeln vom Hersteller erneuert, nacheinander und verschieden schnell."""
    s = Szene("linux/k9snap", reihenfolge="anlegen")
    w = W_SN
    kopf = [L(s, "dist", w["dist"], (-1.8, 2.85), FM, "center", DUNKEL), L(s, "snaps", w["snaps"], (1.8, 2.85), FM, "center", DUNKEL),
            lin(s, (0, 2.95), (0, 0.15), HELLGRAU, 2, "6,5")]
    xl, ylib = [-2.95, -1.8, -0.65], 0.95
    progs = [wchip(s, (x, 2.3), "pg%d" % k, W_PROG[k], 1.0, BLAU, BLAU_HELL, h=0.3) for k, x in enumerate(xl)]
    lib = chip(s, (-1.8, ylib), "libbeispiel", DUNKEL, GRAU_HELL)
    pf_l = [pfk(s, (x, 2.14), (-1.8 + (x + 1.8) * 0.25, ylib + 0.16), DUNKEL, 2) for x in xl]
    pf_g = [pfk(s, (x, 2.14), (-1.8 + (x + 1.8) * 0.25, ylib + 0.16), GRUEN, 2.5) for x in xl]
    lib_g = chip(s, (-1.8, ylib), "libbeispiel", GRUEN, GRUEN_HELL)
    xr_ = [0.7, 1.8, 2.9]
    kaps, kaps_g, libs, libs_g, inn = [], [], [], [], []
    for k, x in enumerate(xr_):
        kaps.append(box(s, (x, 1.62), 1.06, 1.68, DUNKEL, WEISS, 2, "round"))
        inn += wchip(s, (x, 2.2), "pg%d" % k, W_PROG[k], 0.92, BLAU, BLAU_HELL, h=0.3)
        inn.append(pfk(s, (x, 2.04), (x, ylib + 0.16), DUNKEL, 2))
        libs.append(chip(s, (x, ylib), "libbeispiel", DUNKEL, GRAU_HELL, b=0.98))
    for k, x in enumerate(xr_):
        kaps_g.append(box(s, (x, 1.62), 1.06, 1.68, GRUEN, WEISS, 3, "round", deckung=0.0))
        libs_g.append(chip(s, (x, ylib), "libbeispiel", GRUEN, GRUEN_HELL, b=0.98))
    rot = [warnpunkt(s, -1.8 + 0.62, ylib + 0.14)] + [warnpunkt(s, x + 0.44, ylib + 0.14) for x in xr_]
    l_l = L(s, "luecke", w["luecke"], (0, 0.42), FM, "center", ROT)
    l_ein = L(s, "ein", w["ein"], (-1.8, ylib - 0.4), FM, "center", GRUEN)
    l_jede = L(s, "jede", w["jede"], (1.8, ylib - 0.4), FM, "center", GRUEN)
    schritt(s, EIN(kopf, 0.5))
    schritt(s, EIN(flach(progs) + lib, 0.6), ZEICHNE(pf_l, 0.6))
    schritt(s, EIN(kaps + inn + flach(libs), 0.7))
    s.pause(0.6)
    schritt(s, WACHS(flach(rot), 0.6), EIN(l_l, 0.6))
    s.pause(0.6)
    schritt(s, EIN(lib_g + [l_ein], 0.6), AUS(lib + rot[0], 0.6), ZEICHNE(pf_g, 0.6))
    s.pause(0.3)
    for k, (dauer, warte) in enumerate(((0.5, 0.3), (0.5, 1.2), (0.5, 0.6))):
        if warte:
            s.pause(warte)
        schritt(s, EIN(libs_g[k] + [kaps_g[k]], dauer), AUS(libs[k] + rot[k + 1], dauer))
    schritt(s, EIN(l_jede, 0.5), AUS(l_l, 0.5))
    s.speichern()


SZENEN = (k9paket, k9version, k9abhaengigkeit, k9beziehungen, k9virtuell, k9datenbank, k9ebenen, k9dpkgl, k9zweirichtungen,
          k9skripte, k9quelle, k9spiegel, k9ausgaben, k9quellenliste, k9update, k9suche, k9show, k9liste, k9policy, k9rdepends,
          k9download, k9deb, k9steuerteil, k9auspacken,
          k9sperre, k9simulation, k9installieren, k9entfernen, k9upgrade,
          k9kette, k9schluesselpaar, k9signatur, k9signedby, k9weg,
          k9revision, k9zeitfenster, k9neustart, k9timer, k9pflege,
          k9alternativen, k9sudo, k9coreutils, k9geschuetzt,
          k9fremdquelle, k9einzeldatei, k9curlbash, k9snap)

if __name__ == "__main__":
    wahl = set(sys.argv[1:])
    for f in SZENEN:
        if not wahl or f.__name__ in wahl:
            f()
            print("gebaut:", f.__name__)
