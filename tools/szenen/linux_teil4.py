"""Linux und Kommandozeile, Kapitel 4 „Ströme, Umleitung, Pipes und Exit-Status“ (C:\\Bücher\\EtUndSo\\Linux\\Arbeitshefte\\
Kap4_Stroeme.tex, kap4_stufen.tex, kap4_stufen_b.tex): Abbildungen, alle animiert (notizen/animationen.md §5).

Szenenname linux/k4<name> = \\label{fig:k4<name>} im Heft (\\szenenabb{k4<name>}{…}{fig:k4<name>}). Stil wie linux_teil3.py:
Kästen, Pfeile, T(...) in sechs Sprachen; Terminal-Inhalte (Befehle, Ausgaben, Pfade) sind in allen Sprachen gleich und stehen als
Schreibmaschinenschrift in s.formel (\\texttt) mit unsichtbarer Stütze. In \\texttt dürfen & und _ roh stehen, $ { } werden maskiert.
Normale Beschriftungen stehen in s.text (Rich-Text: $ { } _ ^ \\ sind Sonderzeichen; \\$ schreibt ein Dollarzeichen).
Farben der drei Standardströme: 0 blau, 1 grün, 2 orange. Prozesse sind blaue Kästen, Dateien schwarze Rechtecke.
Die Koordinaten bleiben zwischen x = -3,45 und 3,45: jedes Bild höchstens 548 px breit.
Zeichenreihenfolge: Ein Objekt, das per Animation erscheint, liegt über allem, was vorher erschienen ist. Kästen also vor ihrem Inhalt
einblenden. Transform (s.umformen) auf s.text änderte das Endbild nicht; Texte deshalb aus- und einblenden.
Seit 10.11.2026 (für neue Kapitel, diese Szenen bleiben, wie sie sind): Helfer in linux_hilfen.py, s.text(..., schrift="tt") bzw.
schreibmaschine("text") statt der Formel-Stütze, Szene(..., reihenfolge="anlegen"), s.ersetzen für Texte (notizen/animationen.md).
Bauen:  python tools/szenen/linux_teil4.py
Export: python tools/export_szenen.py <alle Namen aus SZENEN> --animiert
"""
import math
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from szenen_lib import *  # noqa: E402,F403

from linux_hilfen import *  # noqa: E402,F403  (gemeinsame Helfer der Linux-Kapitel, seit 10.11.2026)

EM = 0.17                         # Höhe einer Terminalzeile (1 em) in Szeneneinheiten
setze_em(EM)                      # ... auch für tt, ttz, cw, sp, prozess aus linux_hilfen
text = text_gerundet              # in diesem Kapitel: Lage der Beschriftungen auf 4 Stellen gerundet
dokument = datei_rechteck         # in diesem Kapitel: Datei = schwarzes Rechteck


# ================================================================== Abschnitt 1: Prozesse und ihre drei Ströme
def k4prozess():
    """Programmdatei /usr/bin/nano, daraus zwei Prozesse (443, 444) mit eigenem Speicher, eigener Datei, eigenem Verzeichnis;
    Prozess 443 endet, die Datei bleibt."""
    s = Szene("linux/k4prozess")
    dx = -2.5
    disk = s.box("", (dx, 0.0), breite=1.8, hoehe=1.9, form="round", farbe=GRAU, fuellung=GRAU_HELL, dicke=2.5)
    l_disk = text(s, T(s, "disk", "Datenträger", "storage device", "disco", "存储设备", "support de données", "depolama aygıtı"),
                  (dx, 0.68), FK, "center", GRAU)
    datei = dokument(s, (dx, 0.05), 1.5, 0.42)
    d_name = tt(s, "/usr/bin/nano", dx, 0.05, 0.15, SCHWARZ, "m")
    l_prog = text(s, T(s, "prog", "Programmdatei", "program file", "archivo de programa", "程序文件", "fichier programme",
                       "program dosyası"), (dx, -0.4), FM, "center", GRAU)
    l_bleibt = text(s, T(s, "bleibt", "bleibt", "remains", "permanece", "仍然保留", "reste", "kalır"), (dx, -0.68), FM, "center",
                    GRUEN)
    px, pb, ph = 1.72, 3.3, 1.42
    karten = [("mem", "Speicher", "memory", "memoria", "内存", "mémoire", "bellek"),
              ("offen", "geöffnete Datei", "open file", "archivo abierto", "打开的文件", "fichier ouvert", "açık dosya"),
              ("wd", "Arbeitsverzeichnis", "working directory", "directorio de trabajo", "工作目录", "répertoire de travail",
               "çalışma dizini")]

    def proz(y, nr, datei_name, verz):
        k = s.box("", (px, y), breite=pb, hoehe=ph, form="round", farbe=BLAU, fuellung=BLAU_HELL, dicke=2.5)
        kopf = text(s, T(s, "p%d" % nr, "Prozess %d" % nr, "process %d" % nr, "proceso %d" % nr, "进程 %d" % nr,
                         "processus %d" % nr, "süreç %d" % nr), (px, y + 0.5), FK, "center", BLAU)
        x0, x1 = px - pb / 2 + 0.25, px + pb / 2 - 0.25
        teile = []
        for i, kt in enumerate(karten):
            yy = round(y + 0.17 - 0.3 * i, 4)
            teile.append(s.box("", (px, yy), breite=pb - 0.3, hoehe=0.26, form="round", farbe=GRAU, fuellung=WEISS, dicke=1.5))
            teile.append(text(s, T(s, *kt), (x0, yy), FM, "left", DUNKEL))
        teile.append(s.box("", (round(x1 - 0.3, 4), round(y + 0.17, 4)), breite=0.6, hoehe=0.12, form="rect", farbe=BLAU,
                           fuellung=BLAU, deckung=0.45, dicke=1))
        teile.append(text(s, datei_name, (x1, y - 0.13), FM, "right"))
        teile.append(text(s, verz, (x1, y - 0.43), FM, "right"))
        return [k, kopf], teile

    p1k, p1t = proz(0.88, 443, "einkauf.txt", "~")
    p2k, p2t = proz(-0.88, 444, "obst.txt", "/tmp")
    a1 = pf(s, (-1.58, 0.25), (0.02, 0.85), farbe=DUNKEL, dicke=3)
    a2 = pf(s, (-1.58, -0.15), (0.02, -0.85), farbe=DUNKEL, dicke=3)
    a1g = pf(s, (-1.58, 0.25), (0.02, 0.85), farbe=HELLGRAU, dicke=2.5, dash=DASH)
    st = T(s, "start", "starten", "start", "iniciar", "启动", "démarrer", "başlat")
    l_s1 = text(s, st, (-0.8, 0.86), FM, "center", DUNKEL)
    l_s2 = text(s, st, (-0.8, -0.86), FM, "center", DUNKEL)
    gh = geist(s, (px, 0.88), pb, ph)
    gh_t = text(s, T(s, "p443aus", "Prozess 443 beendet", "process 443 ended", "proceso 443 terminado", "进程 443 已结束",
                     "processus 443 terminé", "süreç 443 sona erdi"), (px, 0.88), FK, "center", GRAU)
    schritt(s, WACHS(disk, 0.6), EIN([l_disk, datei, d_name, l_prog], 0.6))
    s.pause(0.6)
    schritt(s, ZEICHNE(a1, 0.6), EIN(l_s1, 0.6))
    schritt(s, WACHS(p1k[0], 0.6), EIN(p1k[1], 0.6))
    schritt(s, EIN(p1t, 0.6))
    s.pause(0.6)
    schritt(s, ZEICHNE(a2, 0.6), EIN(l_s2, 0.6))
    schritt(s, WACHS(p2k[0], 0.6), EIN(p2k[1:] + p2t, 0.6))
    s.pause(0.6)
    schritt(s, AUS(p1k + p1t + [a1, l_s1], 0.7), EIN([gh, gh_t, a1g], 0.7))
    schritt(s, EIN(l_bleibt, 0.5), BETONE([datei, d_name], 0.8))
    s.speichern()


def k4strom():
    """Sechs Bytes 108 97 98 111 114 10 („labor“ + Zeilenende) laufen einzeln vom Schreiber zum Leser und reihen sich dort auf;
    dann liefert eine Leseanfrage 0 Bytes: Ende des Stroms. Zum Schluss verdeckt eine Wolke den Schreiber."""
    s = Szene("linux/k4strom")
    y = 0.35
    wx = -2.85
    w_k = s.box("", (wx, y), breite=1.1, hoehe=0.8, form="round", farbe=BLAU, fuellung=BLAU_HELL, dicke=2.5)
    w_t = text(s, T(s, "schreiber", "Schreiber", "writer", "escritor", "写入者", "rédacteur", "yazan"), (wx, y), FM)
    rx, rb = 2.2, 2.5
    r_k = s.box("", (rx, y), breite=rb, hoehe=1.35, form="round", farbe=BLAU, fuellung=BLAU_HELL, dicke=2.5)
    r_t = text(s, T(s, "leser", "Leser", "reader", "lector", "读取者", "lecteur", "okuyan"), (rx, y + 0.47), FK, "center", BLAU)
    bx0, bx1 = -2.3, 0.95
    band = [linie(s, (bx0, y + 0.26), (bx1, y + 0.26), GRAU, 2.5), linie(s, (bx0, y - 0.26), (bx1, y - 0.26), GRAU, 2.5)]
    werte = (108, 97, 98, 111, 114, 10)
    b = 0.38
    x_start = bx0 + 0.3
    slots = [round(rx - rb / 2 + 0.13 + b / 2 + i * b, 4) for i in range(6)]
    bytes_ = []
    for v in werte:
        k = s.box("", (x_start, y), breite=b, hoehe=b, form="rect", farbe=SCHWARZ, fuellung=WEISS, dicke=2)
        z = text(s, str(v), (x_start, y), FX, "center", ORANGE if v == 10 else SCHWARZ)
        u = zeilenende(s, x_start, y - 0.36, 0.15) if v == 10 else tt(s, chr(v), x_start, y - 0.36, 0.2, BLAU, "m")
        bytes_.append([k, z, u])
    leer = s.box("", (x_start, y), breite=b, hoehe=b, form="rect", farbe=GRAU, fuellung=WEISS, dicke=2, dash=DASH)
    xl = bx1 - 0.3
    l_leer = text(s, T(s, "nullb", "0 Bytes", "0 bytes", "0 bytes", "0 字节", "0 octet", "0 bayt"), (xl, y + 0.47), FM, "center",
                  GRAU)
    schild = karte(s, rx, y - 1.0, T(s, "ende", "Ende des Stroms", "end of the stream", "fin del flujo", "流结束", "fin du flux",
                                     "akışın sonu"), 2.2, ORANGE, ORANGE_HELL, FK, ORANGE, h=0.4)
    wolke = [s.kreis(None, round(wx + dx, 4), round(y + dy, 4), 0.34, farbe=GRAU_HELL, dicke=0, fuellung=GRAU_HELL, deckung=1.0)
             for dx, dy in ((-0.3, 0.0), (0.0, 0.16), (0.3, 0.0), (0.0, -0.14))]
    wolke.append(text(s, "?", (wx, y), 30, "center", GRAU))
    l_quelle = text(s, T(s, "quelle", "der Leser sieht\ndie Quelle nicht", "the reader cannot\nsee the source",
                         "el lector no\nve el origen", "读取者看不到\n来源", "le lecteur ne voit\npas la source",
                         "okuyan kaynağı\ngöremez"), (wx + 0.25, y - 0.95), FM, "center", GRAU)
    schritt(s, WACHS([w_k, r_k], 0.6), EIN([w_t, r_t], 0.6), ZEICHNE(band, 0.6))
    s.pause(0.6)
    schritt(s, EIN(bytes_[0], 0.3))
    for i in range(6):
        teile = VERS(bytes_[i], slots[i] - x_start, -0.05, 0.75)
        if i < 5:
            teile.append(EIN(bytes_[i + 1], 0.3))
        schritt(s, *teile)
    s.pause(0.4)
    schritt(s, EIN(leer, 0.3))
    schritt(s, VER(leer, xl - x_start, 0, 0.8))
    schritt(s, EIN(l_leer, 0.5))
    schritt(s, WACHS(schild[0], 0.5), EIN(schild[1], 0.5))
    s.pause(0.6)
    schritt(s, EIN(wolke, 0.8))
    schritt(s, EIN(l_quelle, 0.5))
    s.speichern()


def k4cateingabe():
    """cat ohne Argument: Das Terminal zeigt „Hallo“ beim Tippen, schickt die Zeile nach der Eingabetaste über 0 an cat, cat schreibt
    sie über 1 zurück; Strg+D beendet den Strom, cat endet."""
    s = Szene("linux/k4cateingabe")
    tx = -2.0
    rahmen_t = s.box("", (tx, 0.1), breite=2.8, hoehe=2.5, form="round", farbe=GRAU, fuellung=WEISS, dicke=2)
    l_term = text(s, w_term(s), (tx, 1.53), FK, "center", GRAU)
    schirm = bildschirm(s, (tx, 0.62), 2.5, 1.2)
    x0 = tx - 1.1
    zl = [tt(s, "$ cat", x0, 1.0), tt(s, "Hallo", x0, 0.74), tt(s, "Hallo", x0, 0.48), tt(s, "$", x0, 0.22)]
    tast = tastatur(s, tx, -0.62)
    cat = prozess(s, (2.45, 0.0), 1.3, 1.7, "cat")
    r1 = rohr(s, (1.8, 0.6), (-0.75, 0.6), C1)
    r0 = rohr(s, (-1.57, -0.62), (1.8, -0.62), C0)
    n1 = nummer(s, 1.55, 0.83, 1, C1)
    n0 = nummer(s, 1.55, -0.39, 0, C0)
    l_zeigt = text(s, T(s, "zeigt", "das Terminal zeigt das Getippte an", "the terminal shows what is typed",
                        "el terminal muestra lo tecleado", "终端显示所输入的内容", "le terminal affiche ce qui est tapé",
                        "terminal yazılanı gösterir"), (tx, -1.38), FM, "center", GRAU)
    l_enter = text(s, T(s, "enter", "Eingabetaste", "Enter key", "tecla Intro", "回车键", "touche Entrée", "Enter tuşu"), (0.1, -0.4),
                   FM, "center", C0)
    strgd = text(s, T(s, "strgd", "Strg+D", "Ctrl+D", "Ctrl+D", "Ctrl+D", "Ctrl+D", "Ctrl+D"), (tx, -0.95), FM, "center", ORANGE)
    ende = karte(s, 0.1, -0.88, T(s, "ende", "Ende des Stroms", "end of the stream", "fin del flujo", "流结束", "fin du flux",
                                  "akışın sonu"), 1.6, ORANGE, ORANGE_HELL, FM, ORANGE)

    def fracht(x, y):
        return [s.box("", (x, y), breite=0.72, hoehe=0.26, form="round", farbe=GRAU, fuellung=WEISS, dicke=1.5),
                tt(s, "Hallo", x, y, 0.15, SCHWARZ, "m")]

    f0 = fracht(-1.1, -0.62)
    f1 = fracht(1.4, 0.6)
    g = geist(s, (2.45, 0.0), 1.3, 1.7)
    g_name = tt(s, "cat", 2.45, 0.0, EM, HELLGRAU, "m")
    g_t = text(s, w_beendet(s), (2.45, -0.4), FM, "center", GRAU)
    schritt(s, WACHS(rahmen_t, 0.6), EIN([l_term, schirm] + tast, 0.6))
    schritt(s, EIN(zl[0], 0.4), WACHS(cat[0], 0.5), EIN(cat[1], 0.5))
    schritt(s, ZEICHNE([r1, r0], 0.6), EIN(n1 + n0, 0.6))
    s.pause(0.6)
    schritt(s, EIN([zl[1], l_zeigt], 0.6))
    s.pause(0.6)
    schritt(s, EIN([l_enter] + f0, 0.4))
    schritt(s, *VERS(f0, 2.5, 0, 0.9))
    schritt(s, AUS(f0, 0.3), EIN(f1, 0.3))
    schritt(s, *VERS(f1, -2.5, 0, 0.9))
    schritt(s, AUS(f1, 0.3), EIN(zl[2], 0.3))
    s.pause(0.6)
    schritt(s, EIN(strgd, 0.5))
    schritt(s, WACHS(ende[0], 0.5), EIN(ende[1], 0.5))
    schritt(s, AUS(cat, 0.6), EIN([g, g_name, g_t], 0.6))
    schritt(s, EIN(zl[3], 0.4))
    s.speichern()


def k4rohre():
    """ls /etc/hostname /gibtsnicht: Rohr 0 von der Tastatur, 1 und 2 zum Bildschirm; die Meldung läuft durch 2 (orange), das
    Ergebnis durch 1 (grün); am Bildschirm stehen beide Zeilen in derselben Farbe."""
    s = Szene("linux/k4rohre")
    yp = 0.2
    tast = tastatur(s, -3.0, yp)
    l_tast = text(s, T(s, "tast", "Tastatur", "keyboard", "teclado", "键盘", "clavier", "klavye"), (-3.0, yp - 0.34), FM, "center",
                  GRAU)
    ls = prozess(s, (-1.55, yp), 0.9, 0.75, "ls")
    sx, sb = 1.8, 3.2
    schirm = bildschirm(s, (sx, 0.45), sb, 1.2)
    l_schirm = text(s, w_schirm(s), (sx, 1.25), FM, "center", GRAU)
    e, x0 = 0.15, 0.32
    z_cmd = tt(s, "$ ls /etc/hostname /gibtsnicht", x0, 0.82, e)
    z_err = tt(s, "ls: cannot access '/gibtsnicht': ...", x0, 0.52, e)
    z_out = tt(s, "/etc/hostname", x0, 0.22, e)
    r0 = rohr(s, (-2.55, yp), (-2.0, yp), C0)
    r1 = rohr(s, (-1.1, 0.35), (0.2, 0.35), C1)
    r2 = [linie(s, (-1.55, -0.175), (-1.55, -0.6), C2, 4.5), linie(s, (-1.55, -0.6), (sx, -0.6), C2, 4.5),
          rohr(s, (sx, -0.6), (sx, -0.15), C2)]
    n0 = nummer(s, -2.28, yp + 0.25, 0, C0)
    n1 = nummer(s, -0.8, 0.58, 1, C1)
    n2 = nummer(s, -1.3, -0.4, 2, C2)
    namen = [(0, C0, ("sin", "Standardeingabe", "standard input", "entrada estándar", "标准输入", "entrée standard",
                      "standart girdi")),
             (1, C1, ("sout", "Standardausgabe", "standard output", "salida estándar", "标准输出", "sortie standard",
                      "standart çıktı")),
             (2, C2, ("serr", "Standardfehlerausgabe", "standard error", "salida de error estándar", "标准错误输出",
                      "sortie d'erreur standard", "standart hata çıktısı"))]
    leg = []
    for i, (n, f, kt) in enumerate(namen):
        yy = -1.0 - 0.29 * i
        leg.append(nummer(s, -3.25, yy, n, f) + [text(s, T(s, *kt), (-3.05, yy), FM, "left", f)])
    note = text(s, T(s, "gleich", "am Bildschirm sehen beide\nZeilen gleich aus", "on the screen both lines\nlook the same",
                     "en la pantalla ambas líneas\nse ven iguales", "在屏幕上两行\n看起来一样", "à l'écran, les deux lignes\nse ressemblent",
                     "ekranda iki satır\naynı görünür"), (sx, -1.1), FM, "center", GRAU)
    m2 = marke(s, -1.55, -0.32, C2)
    m1 = marke(s, -0.95, 0.35, C1)
    schritt(s, WACHS(ls[0], 0.6), EIN([ls[1], l_tast] + tast, 0.6))
    schritt(s, WACHS(schirm, 0.6), EIN([l_schirm, z_cmd], 0.6))
    s.pause(0.5)
    schritt(s, ZEICHNE(r0, 0.5), EIN(n0 + leg[0], 0.5))
    schritt(s, ZEICHNE(r1, 0.5), EIN(n1 + leg[1], 0.5))
    schritt(s, ZEICHNE(r2, 0.7), EIN(n2 + leg[2], 0.7))
    s.pause(0.6)
    schritt(s, EIN(m2, 0.25))
    schritt(s, VER(m2, 0, -0.28, 0.35))
    schritt(s, VER(m2, sx + 1.55, 0, 1.0))
    schritt(s, VER(m2, 0, 0.35, 0.35))
    schritt(s, AUS(m2, 0.3), EIN(z_err, 0.4))
    schritt(s, EIN(m1, 0.25))
    schritt(s, VER(m1, 1.0, 0, 0.6))
    schritt(s, AUS(m1, 0.3), EIN(z_out, 0.4))
    s.pause(0.5)
    schritt(s, EIN(note, 0.6))
    s.speichern()


def k4deskriptoren():
    """Liste der Deskriptoren von ls im Kernel: 0, 1, 2 zum Terminal /dev/pts/2, 3 (kleinste freie Nummer) zum Verzeichnis
    /proc/454/fd; ls sagt nur „schreibe in 1“, der Kernel folgt dem Eintrag."""
    s = Szene("linux/k4deskriptoren")
    ls = prozess(s, (-2.85, 0.1), 0.9, 0.7, "ls")
    kern = kernel(s, -2.05, -1.45, 0.75, 1.45, (-1.95, 1.27))
    h_nr = text(s, T(s, "nr", "Nr.", "no.", "n.º", "编号", "n°", "no."), (-1.6, 0.95), FM, "center", GRAU)
    h_zu = text(s, T(s, "fuehrt", "führt zu", "leads to", "lleva a", "指向", "mène à", "gider"), (-0.95, 0.95), FM, "left", GRAU)
    ys = [0.6, 0.25, -0.1, -0.45]
    zellen = [[s.box("", (-1.6, y), breite=0.36, hoehe=0.28, form="rect", farbe=DUNKEL, fuellung=WEISS, dicke=2),
               text(s, str(i), (-1.6, y), FK)] for i, y in enumerate(ys)]
    tx = 2.3
    term = s.box("", (tx, 0.45), breite=2.0, hoehe=0.55, form="round", farbe=DUNKEL, fuellung=TERM, dicke=2.5)
    term_t = tt(s, "/dev/pts/2", tx, 0.45, 0.16, SCHWARZ, "m")
    l_term = text(s, w_term(s), (tx, 0.9), FM, "center", GRAU)
    verz = s.box("", (tx, -0.8), breite=2.0, hoehe=0.55, form="round", farbe=BLAU, fuellung=BLAU_HELL, dicke=2.5)
    verz_t = tt(s, "/proc/454/fd", tx, -0.8, 0.16, SCHWARZ, "m")
    l_verz = text(s, T(s, "verz", "Verzeichnis", "directory", "directorio", "目录", "répertoire", "dizin"), (tx, -1.25), FM,
                  "center", GRAU)
    ziele = [(1.3, 0.57), (1.3, 0.45), (1.3, 0.33), (1.3, -0.8)]
    pfeile = [pf(s, (-1.4, y), z, farbe=DUNKEL, dicke=2.5) for y, z in zip(ys, ziele)]
    l_frei = text(s, T(s, "frei", "kleinste freie Nummer", "lowest free number", "el número libre más bajo", "最小的空闲编号",
                       "plus petit numéro libre", "en küçük boş numara"), (-1.95, -0.85), FM, "left", ORANGE)
    blase = s.box("", (-2.85, 0.95), breite=1.2, hoehe=0.4, form="round", farbe=DUNKEL, fuellung=WEISS, dicke=2)
    blase_t = text(s, T(s, "blase", "schreibe in 1", "write to 1", "escribe en 1", "写入 1", "écris dans 1", "1'e yaz"),
                   (-2.85, 0.95), FM)
    zeig = pf(s, (-2.4, 0.2), (-1.8, 0.25), farbe=ORANGE, dicke=3)
    schritt(s, EIN(kern, 0.6), WACHS(ls[0], 0.6), EIN(ls[1], 0.6))
    schritt(s, EIN([h_nr, h_zu], 0.4))
    schritt(s, EIN(zellen[:3], 0.6), WACHS(term, 0.6), EIN([term_t, l_term], 0.6))
    schritt(s, ZEICHNE(pfeile[:3], 0.7))
    s.pause(0.6)
    schritt(s, WACHS(verz, 0.5), EIN([verz_t, l_verz], 0.5))
    schritt(s, EIN(zellen[3], 0.5), ZEICHNE(pfeile[3], 0.6))
    schritt(s, EIN(l_frei, 0.5), BETONE(zellen[3], 0.8))
    s.pause(0.6)
    schritt(s, WACHS(blase, 0.5), EIN(blase_t, 0.5))
    schritt(s, ZEICHNE(zeig, 0.6))
    schritt(s, BETONE([pfeile[1], term], 0.9))
    s.speichern()


# ================================================================== Abschnitt 2: Ausgaben umleiten
def k4umleitung():
    """ls /usr > inhalt.txt: Die Shell dreht Rohr 1 vom Bildschirm zur (leeren) Datei, erst dann startet ls; die Namen fließen in die
    Datei, der Bildschirm bleibt leer."""
    s = Szene("linux/k4umleitung")
    term = term_kasten(s, (0, 1.78), 3.0, 0.4)
    cmd = tt(s, "$ ls /usr > inhalt.txt", 0, 1.78, EM, SCHWARZ, "m")
    ls = prozess(s, (-2.4, 0.2), 1.0, 0.75, "ls")
    n1 = nummer(s, -1.7, 0.47, 1, C1)
    schirm = bildschirm(s, (2.15, 0.8), 2.2, 0.75)
    l_schirm = text(s, w_schirm(s), (2.15, 1.33), FM, "center", GRAU)
    start = (-1.9, 0.2)
    rohr1 = rohr(s, start, (1.05, 0.8), C1)
    winkel = -2 * math.degrees(math.atan2(0.6, 2.95))
    doc = dokument(s, (1.9, -0.8), 1.6, 1.3)
    d_name = text(s, "inhalt.txt", (1.1, 0.0), FK, "left")
    d_groesse = text(s, T(s, "nullb", "0 Bytes", "0 bytes", "0 bytes", "0 字节", "0 octet", "0 bayt"), (2.7, 0.0), FM, "right", GRAU)
    flug = [text(s, n, (-1.8, 0.05), FM, "left") for n in ("bin", "games", "include", "lib")]
    punkte = text(s, "…", (1.25, -1.27), FM, "left")
    l_wie = text(s, T(s, "wieimmer", "schreibt wie\nimmer in 1", "writes to 1\nas always", "escribe en 1\ncomo siempre", "照常写入 1",
                      "écrit dans 1\ncomme toujours", "her zamanki\ngibi 1'e yazar"), (-2.4, -0.55), FM, "center", GRAU)
    l_s1 = text(s, T(s, "schritt1", "1  Die Shell verbindet 1 mit der Datei.", "1  The shell connects 1 to the file.",
                     "1  La shell conecta 1 con el archivo.", "1  Shell 把 1 连接到文件。", "1  Le shell relie 1 au fichier.",
                     "1  Kabuk 1'i dosyaya bağlar."), (-3.4, -1.05), FM, "left", ORANGE)
    l_s2 = text(s, T(s, "schritt2", "2  Erst dann startet ls.", "2  Only then does ls start.", "2  Solo entonces arranca ls.",
                     "2  然后才启动 ls。", "2  Ensuite seulement, ls démarre.", "2  Ancak sonra ls başlar."), (-3.4, -1.35), FM,
                "left", ORANGE)
    l_leer = text(s, T(s, "leer", "bleibt leer", "stays empty", "queda vacía", "保持空白", "reste vide", "boş kalır"), (2.15, 0.8),
                  FM, "center", GRAU)
    schritt(s, WACHS(term, 0.5), EIN(cmd, 0.5))
    schritt(s, WACHS([ls[0], schirm], 0.6), EIN([ls[1], l_schirm], 0.6))
    schritt(s, ZEICHNE(rohr1, 0.6), EIN(n1, 0.6))
    s.pause(0.6)
    schritt(s, EIN(l_s1, 0.5))
    schritt(s, WACHS(doc, 0.5), EIN([d_name, d_groesse], 0.5))
    schritt(s, DREH(rohr1, winkel, start, 1.0))
    s.pause(0.6)
    schritt(s, EIN(l_s2, 0.5))
    for i, f in enumerate(flug):
        schritt(s, EIN(f, 0.2))
        schritt(s, VER(f, 3.05, -0.4 - 0.23 * i, 0.5))
    schritt(s, EIN(punkte, 0.3), AUS(d_groesse, 0.3))
    s.pause(0.4)
    schritt(s, EIN([l_wie, l_leer], 0.6))
    s.speichern()


def k4anhaengen():
    """einkauf.txt mit vier Zeilen, zweimal beschrieben: oben mit > (alte Zeilen weg, dann Butter), unten mit >> (Butter kommt dazu)."""
    s = Szene("linux/k4anhaengen")
    alt = ["Milch", "Brot", "Äpfel", "Kaffee"]
    R = []
    for y, op in ((0.85, ">"), (-0.95, ">>")):
        r = {"y": y}
        r["cmd"] = tt(s, "$ echo Butter %s einkauf.txt" % op, -3.4, y, 0.15)
        r["a"] = pf(s, (-1.05, y), (-0.3, y), farbe=GRAU, dicke=2.5)
        r["doc"] = dokument(s, (0.45, y), 1.3, 1.45)
        r["name"] = text(s, "einkauf.txt", (0.45, y + 0.88), FM, "center", GRAU)
        r["z"] = [text(s, w, (-0.05, y + 0.5 - 0.24 * i), FM, "left") for i, w in enumerate(alt)]
        R.append(r)
    b_o = text(s, "Butter", (-0.05, 0.85 + 0.5), FM, "left", ORANGE)
    b_u = text(s, "Butter", (-0.05, -0.95 + 0.5 - 0.96), FM, "left", GRUEN)
    n_o = text(s, T(s, "weg", "alte Zeilen weg,\ndann Butter", "old lines gone,\nthen Butter", "líneas viejas borradas,\nluego Butter",
                    "旧行被清除，\n然后写入 Butter", "anciennes lignes effacées,\npuis Butter", "eski satırlar silinir,\nsonra Butter"),
               (1.3, 0.85), FM, "left", ORANGE)
    n_u = text(s, T(s, "bleiben", "alte Zeilen bleiben,\nButter kommt dazu", "old lines stay,\nButter is added",
                    "las líneas viejas quedan,\nse añade Butter", "旧行保留，\n追加 Butter", "anciennes lignes gardées,\nButter ajouté",
                    "eski satırlar kalır,\nButter eklenir"), (1.3, -0.95), FM, "left", GRUEN)
    schritt(s, WACHS([R[0]["doc"], R[1]["doc"]], 0.6), EIN([R[0]["name"], R[1]["name"]] + R[0]["z"] + R[1]["z"], 0.6))
    s.pause(0.6)
    schritt(s, EIN(R[0]["cmd"], 0.5), ZEICHNE(R[0]["a"], 0.5))
    schritt(s, AUS(R[0]["z"], 0.6))
    schritt(s, EIN([b_o, n_o], 0.6))
    s.pause(0.6)
    schritt(s, EIN(R[1]["cmd"], 0.5), ZEICHNE(R[1]["a"], 0.5))
    schritt(s, EIN([b_u, n_u], 0.6))
    s.speichern()


def k4zweidateien():
    """ls /etc/hostname /gibtsnicht mit zwei Zielen: links 1 → aus.txt, 2 → fehler.txt; rechts 2 → /dev/null (Loch), die Meldung
    verschwindet."""
    s = Szene("linux/k4zweidateien")
    kopf = tt(s, "$ ls /etc/hostname /gibtsnicht ...", 0, 2.0, 0.16, SCHWARZ, "m")
    trenn = linie(s, (0, 1.75), (0, -1.4), HELLGRAU, 2, DASH)
    weg_t = T(s, "weg", "verworfen", "discarded", "descartado", "被丢弃", "jeté", "atıldı")

    def panel(px, rechts):
        r = {}
        r["titel"] = tt(s, "... > aus.txt 2> " + ("/dev/null" if rechts else "fehler.txt"), px, 1.55, 0.14, SCHWARZ, "m")
        r["ls"] = prozess(s, (px - 1.0, 0.25), 0.8, 0.7, "ls")
        r["aus"] = dokument(s, (px + 0.8, 0.85), 1.5, 0.5)
        r["l_aus"] = text(s, "aus.txt", (px + 0.8, 1.24), FM, "center", GRAU)
        r["r1"] = rohr(s, (px - 0.6, 0.4), (px + 0.05, 0.8), C1)
        r["n1"] = nummer(s, px - 0.42, 0.72, 1, C1)
        if rechts:
            r["ziel"] = [s.kreis(None, px + 0.8, -0.45, 0.3, farbe=DUNKEL, dicke=2, fuellung=DUNKEL, deckung=1.0)]
            r["l_ziel"] = tt(s, "/dev/null", px + 0.8, -0.95, 0.14, SCHWARZ, "m")
            r["r2"] = rohr(s, (px - 0.6, 0.1), (px + 0.48, -0.36), C2)
            r["weg"] = text(s, weg_t, (px + 0.8, -1.22), FM, "center", GRAU)
        else:
            r["ziel"] = [dokument(s, (px + 0.8, -0.45), 1.5, 0.5)]
            r["l_ziel"] = text(s, "fehler.txt", (px + 0.8, -0.86), FM, "center", GRAU)
            r["r2"] = rohr(s, (px - 0.6, 0.1), (px + 0.05, -0.4), C2)
        r["n2"] = nummer(s, px - 0.42, -0.16, 2, C2)
        r["out"] = text(s, "/etc/hostname", (px - 0.3, 0.6), FM, "center", GRUEN)
        r["err"] = text(s, "ls: cannot access …", (px - 0.3, -0.05), FX, "center", ORANGE)
        return r

    for px, rechts in ((-1.75, False), (1.75, True)):
        r = panel(px, rechts)
        if not rechts:
            schritt(s, EIN(kopf, 0.5), ZEICHNE(trenn, 0.5))
        else:
            s.pause(0.6)
        schritt(s, WACHS([r["ls"][0], r["aus"]] + r["ziel"], 0.6), EIN([r["titel"], r["ls"][1], r["l_aus"], r["l_ziel"]], 0.6))
        schritt(s, ZEICHNE([r["r1"], r["r2"]], 0.6), EIN(r["n1"] + r["n2"], 0.6))
        schritt(s, EIN([r["out"], r["err"]], 0.3))
        schritt(s, ZU(r["out"], px + 0.8, 0.85, 0.8), ZU(r["err"], px + 0.8, -0.45, 0.8))
        if rechts:
            schritt(s, AUS(r["err"], 0.4))
            schritt(s, EIN(r["weg"], 0.5))
    s.speichern()


def k4reihenfolge():
    """Zwei Tafeln „Schritt | 1 → | 2 →“: > alles.txt 2>&1 (2 übernimmt die Datei) und 2>&1 > nur.txt (2 bleibt beim Terminal);
    Karten gleiten als Kopie in die nächste Zeile bzw. Spalte; das Endbild zeigt alle Schritte."""
    s = Szene("linux/k4reihenfolge")
    xs, x1, x2 = -2.15, 0.15, 2.3
    cb = 1.55
    t_term = w_term(s)
    t_anf = T(s, "anfang", "am Anfang", "at the start", "al principio", "开始时", "au début", "başta")
    t_schr = T(s, "schritt", "Schritt", "step", "paso", "步骤", "étape", "adım")

    def k_t(x, y):
        return karte(s, x, y, t_term, cb)

    def k_d(x, y, name):
        return karte(s, x, y, name, cb, ORANGE, ORANGE_HELL)

    def tafel(y0, titel):
        t = tt(s, titel, -3.3, y0, EM, BLAU)
        hk = [text(s, t_schr, (xs, y0 - 0.4), FM, "center", GRAU), text(s, r"1 \rightarrow", (x1, y0 - 0.4), FM, "center", GRAU),
              text(s, r"2 \rightarrow", (x2, y0 - 0.4), FM, "center", GRAU), linie(s, (-3.3, y0 - 0.58), (3.3, y0 - 0.58), HELLGRAU, 2)]
        return t, hk, [round(y0 - 0.8 - 0.37 * i, 4) for i in range(3)]

    tA, hA, yA = tafel(1.95, "> alles.txt 2>&1")
    a_s = [text(s, t_anf, (xs, yA[0]), FM), tt(s, "> alles.txt", xs, yA[1], 0.15, SCHWARZ, "m"), tt(s, "2>&1", xs, yA[2], 0.15, SCHWARZ, "m")]
    a00, a01 = k_t(x1, yA[0]), k_t(x2, yA[0])
    a11k = k_t(x2, yA[0])
    a10 = k_d(x1, yA[1], "alles.txt")
    a20k, a21k = k_d(x1, yA[1], "alles.txt"), k_d(x1, yA[1], "alles.txt")
    tB, hB, yB = tafel(-0.1, "2>&1 > nur.txt")
    b_s = [text(s, t_anf, (xs, yB[0]), FM), tt(s, "2>&1", xs, yB[1], 0.15, SCHWARZ, "m"), tt(s, "> nur.txt", xs, yB[2], 0.15, SCHWARZ, "m")]
    b00, b01 = k_t(x1, yB[0]), k_t(x2, yB[0])
    b10k, b11k = k_t(x1, yB[0]), k_t(x1, yB[0])
    b21k = k_t(x2, yB[1])
    b20 = k_d(x1, yB[2], "nur.txt")
    hervor = rahmen(s, (x2, yB[2]), cb + 0.16, 0.42, ORANGE, 3.5)
    note = text(s, T(s, "bleibt", "bleibt beim Terminal", "stays with the terminal", "se queda en el terminal", "仍指向终端",
                     "reste sur le terminal", "terminalde kalır"), (x2, yB[2] - 0.4), FM, "center", ORANGE)
    d = yA[1] - yA[0]
    schritt(s, EIN([tA] + hA, 0.5))
    schritt(s, EIN(a_s[0], 0.5), WACHS([a00[0], a01[0]], 0.5), EIN([a00[1], a01[1]], 0.5))
    s.pause(0.5)
    schritt(s, EIN(a_s[1], 0.4), EIN(a11k, 0.2))
    schritt(s, *VERS(a11k, 0, d, 0.6), WACHS(a10[0], 0.6), EIN(a10[1], 0.6))
    s.pause(0.4)
    schritt(s, EIN(a_s[2], 0.4), EIN(a20k + a21k, 0.2))
    schritt(s, *VERS(a20k, 0, d, 0.8), *VERS(a21k, x2 - x1, d, 0.8))
    s.pause(0.6)
    schritt(s, EIN([tB] + hB, 0.5))
    schritt(s, EIN(b_s[0], 0.5), WACHS([b00[0], b01[0]], 0.5), EIN([b00[1], b01[1]], 0.5))
    s.pause(0.5)
    schritt(s, EIN(b_s[1], 0.4), EIN(b10k + b11k, 0.2))
    schritt(s, *VERS(b10k, 0, d, 0.8), *VERS(b11k, x2 - x1, d, 0.8))
    s.pause(0.4)
    schritt(s, EIN(b_s[2], 0.4), EIN(b21k, 0.2))
    schritt(s, *VERS(b21k, 0, d, 0.6), WACHS(b20[0], 0.6), EIN(b20[1], 0.6))
    s.pause(0.4)
    schritt(s, ZEICHNE(hervor, 0.6), EIN(note, 0.6))
    s.speichern()


def k4kuerzung():
    """sort probe.txt > probe.txt als Zeitleiste: (1) die Shell öffnet probe.txt für > und leert sie (32 → 0 Bytes), (2) sort liest
    0 Bytes, (3) sort schreibt nichts; Liste verloren."""
    s = Szene("linux/k4kuerzung")
    term = term_kasten(s, (0, 1.85), 3.6, 0.4)
    cmd = tt(s, "$ sort probe.txt > probe.txt", 0, 1.85, EM, SCHWARZ, "m")
    achse = pf(s, (-3.35, 1.3), (3.35, 1.3), farbe=GRAU, dicke=2.5)
    l_zeit = text(s, T(s, "zeit", "Zeit", "time", "tiempo", "时间", "temps", "zaman"), (3.35, 1.47), FX, "right", GRAU)
    sx = [-2.2, 0.0, 2.2]
    punkte = [s.kreis(None, x, 1.3, 0.08, farbe=DUNKEL, dicke=2, fuellung=DUNKEL, deckung=1.0) for x in sx]
    st = [("st1", "1  Shell öffnet\nprobe.txt für >", "1  shell opens\nprobe.txt for >", "1  la shell abre\nprobe.txt para >",
           "1  Shell 为 >\n打开 probe.txt", "1  le shell ouvre\nprobe.txt pour >", "1  kabuk > için\nprobe.txt'yi açar"),
          ("st2", "2  sort startet\nund liest", "2  sort starts\nand reads", "2  sort arranca\ny lee", "2  sort 启动\n并读取",
           "2  sort démarre\net lit", "2  sort başlar\nve okur"),
          ("st3", "3  sort schreibt", "3  sort writes", "3  sort escribe", "3  sort 写入", "3  sort écrit", "3  sort yazar")]
    l_st = [text(s, T(s, *t), (x, 0.92), FM, "center") for t, x in zip(st, sx)]
    dx = -2.2
    doc = dokument(s, (dx, -0.5), 1.3, 1.4)
    zeilen = [text(s, w, (dx - 0.45, 0.02 - 0.24 * i), FM, "left") for i, w in enumerate(("Milch", "Brot", "Äpfel", "Kaffee", "Butter"))]
    name = text(s, "probe.txt", (dx, 0.38), FM, "center")
    g32 = text(s, T(s, "b32", "32 Bytes", "32 bytes", "32 bytes", "32 字节", "32 octets", "32 bayt"), (dx, -1.42), FM, "center", GRAU)
    t0 = T(s, "nullb", "0 Bytes", "0 bytes", "0 bytes", "0 字节", "0 octet", "0 bayt")
    g0 = text(s, t0, (dx, -1.42), FM, "center", ROT)
    sort = prozess(s, (0.0, -0.5), 1.0, 0.6, "sort")
    lese = rohr(s, (-1.55, -0.35), (-0.5, -0.35), C0)
    l_lese = text(s, t0, (-1.02, -0.15), FX, "center", C0)
    schreib = [linie(s, (0.0, -0.8), (0.0, -1.1), C1, 4.5), rohr(s, (0.0, -1.1), (-1.55, -1.1), C1)]
    l_nichts = text(s, T(s, "nichts", "nichts", "nothing", "nada", "什么也没有", "rien", "hiçbir şey"), (-0.78, -1.3), FX, "center", C1)
    schild = karte(s, 2.2, -0.5, T(s, "verloren", "Liste verloren", "list lost", "lista perdida", "列表丢失", "liste perdue",
                                   "liste kayboldu"), 1.9, ROT, ROT_HELL, FK, ROT, h=0.45)
    schritt(s, WACHS(term, 0.5), EIN(cmd, 0.5))
    schritt(s, WACHS(doc, 0.6), EIN(zeilen + [name, g32], 0.6))
    schritt(s, ZEICHNE(achse, 0.6), EIN(l_zeit, 0.6))
    s.pause(0.6)
    schritt(s, WACHS(punkte[0], 0.4), EIN(l_st[0], 0.5))
    schritt(s, AUS(zeilen + [g32], 0.7), EIN(g0, 0.7))
    schritt(s, BETONE(g0, 0.7))
    s.pause(0.6)
    schritt(s, WACHS(punkte[1], 0.4), EIN(l_st[1], 0.5), WACHS(sort[0], 0.5), EIN(sort[1], 0.5))
    schritt(s, ZEICHNE(lese, 0.6), EIN(l_lese, 0.6))
    s.pause(0.6)
    schritt(s, WACHS(punkte[2], 0.4), EIN(l_st[2], 0.5))
    schritt(s, ZEICHNE(schreib, 0.7), EIN(l_nichts, 0.7))
    s.pause(0.4)
    schritt(s, WACHS(schild[0], 0.6), EIN(schild[1], 0.6))
    s.speichern()


# ================================================================== Abschnitt 3: Eingaben umleiten
def k4eingabe():
    """Links wc -l einkauf.txt (Name als Argument, wc öffnet selbst, Ausgabe mit Namen); rechts wc -l < einkauf.txt (die Shell öffnet,
    die Datei hängt an 0, wc kennt den Namen nicht, Ausgabe nur 5)."""
    s = Szene("linux/k4eingabe")
    trenn = linie(s, (0, 1.9), (0, -1.55), HELLGRAU, 2, DASH)
    arg_t = T(s, "arg", "Argumente", "arguments", "argumentos", "参数", "arguments", "argümanlar")
    aus_t = T(s, "ausgabe", "Ausgabe:", "output:", "salida:", "输出：", "sortie :", "çıktı:")

    def panel(px, rechts):
        r = {}
        r["cmd"] = tt(s, "$ wc -l < einkauf.txt" if rechts else "$ wc -l einkauf.txt", px, 1.7, 0.15, SCHWARZ, "m")
        r["wc"] = prozess(s, (px + 0.55, 0.35), 1.0, 0.6, "wc")
        r["slot"] = s.box("", (px + 0.55, 0.97), breite=1.6, hoehe=0.32, form="rect", farbe=GRAU, fuellung=WEISS, dicke=1.5, dash=DASH)
        r["opt"] = tt(s, "-l", px - 0.15, 0.97, 0.15)
        r["l_slot"] = text(s, arg_t, (px - 0.33, 0.97), FM, "right", GRAU)
        r["doc"] = [dokument(s, (px - 0.9, -0.55), 1.3, 0.45), text(s, "einkauf.txt", (px - 0.9, -0.55), FM)]
        r["l_aus"] = text(s, aus_t, (px - 1.6, -1.3), FM, "left", GRAU)
        r["out"] = tt(s, "5" if rechts else "5 einkauf.txt", px - 0.7, -1.3, 0.16)
        return r

    L, R = panel(-1.75, False), panel(1.75, True)
    px = -1.75
    karte_l = karte(s, px + 0.3, 1.4, "einkauf.txt", 1.0, BLAU, BLAU_HELL, FX)
    oeffnet_l = pf(s, (px + 0.3, 0.05), (px - 0.25, -0.38), farbe=DUNKEL, dicke=2.5)
    l_selbst = text(s, T(s, "selbst", "öffnet sie selbst", "opens it itself", "lo abre él mismo", "自己打开它", "l'ouvre lui-même",
                         "kendisi açar"), (px + 0.2, -0.42), FX, "left", DUNKEL)
    px = 1.75
    shell = kasten(s, (px - 0.9, 0.35), 0.95, 0.5, w_shell(s), FM, GRAU_HELL, farbe=GRAU)
    oeffnet_r = pf(s, (px - 0.9, 0.1), (px - 0.9, -0.32), farbe=DUNKEL, dicke=2.5)
    l_oeffnet = text(s, T(s, "oeffnet", "öffnet", "opens", "abre", "打开", "ouvre", "açar"), (px - 0.98, -0.1), FX, "right", DUNKEL)
    r0 = rohr(s, (px - 0.25, -0.5), (px + 0.2, 0.05), C0)
    n0 = nummer(s, px - 0.12, -0.12, 0, C0)
    durch = [text(s, "einkauf.txt", (px + 1.0, -0.45), FX, "center", GRAU), linie(s, (px + 0.58, -0.45), (px + 1.42, -0.45), ROT, 2.5)]
    l_unb = text(s, T(s, "unbekannt", "unbekannt", "unknown", "desconocido", "未知", "inconnu", "bilinmiyor"), (px + 1.0, -0.68), FX,
                 "center", ROT)
    for r, rechts in ((L, False), (R, True)):
        if rechts:
            s.pause(0.6)
        else:
            schritt(s, ZEICHNE(trenn, 0.4))
        schritt(s, EIN(r["cmd"], 0.5))
        schritt(s, WACHS([r["wc"][0], r["slot"], r["doc"][0]], 0.6), EIN([r["wc"][1], r["opt"], r["l_slot"], r["doc"][1]], 0.6))
        if not rechts:
            schritt(s, EIN(karte_l, 0.3))
            schritt(s, *VERS(karte_l, 0.45, 0.97 - 1.4, 0.8))
            schritt(s, ZEICHNE(oeffnet_l, 0.6), EIN(l_selbst, 0.6))
        else:
            schritt(s, WACHS(shell[0], 0.5), EIN(shell[1], 0.5))
            schritt(s, ZEICHNE(oeffnet_r, 0.5), EIN(l_oeffnet, 0.5))
            schritt(s, ZEICHNE(r0, 0.6), EIN(n0, 0.6))
            schritt(s, EIN(durch + [l_unb], 0.6))
        schritt(s, EIN([r["l_aus"], r["out"]], 0.5))
    s.speichern()


def k4heredoc():
    """cat <<ENDE: Die Shell sammelt die Zeilen Milch und Brot in einem Korb, die Zeile ENDE schließt ihn (ohne hineinzugehen); der
    Inhalt fließt über 0 in cat, cat schreibt beide Zeilen über 1 ins Terminal."""
    s = Szene("linux/k4heredoc")
    term = s.box("", (-2.45, 0.35), breite=1.9, hoehe=2.5, form="rect", farbe=GRAU, fuellung=TERM, dicke=2)
    x0, e = -3.3, 0.16
    z = [tt(s, t, x0, y, e) for t, y in (("$ cat <<ENDE", 1.35), ("> Milch", 1.07), ("> Brot", 0.79), ("> ENDE", 0.51))]
    aus = [tt(s, t, x0, y, e) for t, y in (("Milch", 0.0), ("Brot", -0.28))]
    shell = s.box("", (0.15, 0.75), breite=1.6, hoehe=1.5, form="round", farbe=GRAU, fuellung=GRAU_HELL, dicke=2.5)
    l_shell = text(s, w_shell(s), (0.15, 1.3), FK, "center", GRAU)
    korb = [linie(s, (-0.35, 1.05), (-0.35, 0.2), DUNKEL, 3), linie(s, (-0.35, 0.2), (0.65, 0.2), DUNKEL, 3),
            linie(s, (0.65, 0.2), (0.65, 1.05), DUNKEL, 3)]
    deckel = linie(s, (-0.35, 1.05), (0.65, 1.05), ORANGE, 4)
    ys = (0.75, 0.45)
    flug = [tt(s, "Milch", sp(x0, 2, e), 1.07, e), tt(s, "Brot", sp(x0, 2, e), 0.79, e)]
    m_ende = mark(s, x0 - 0.05, sp(x0, 6, e) + 0.05, 0.51, 0.26, ORANGE)
    l_ende = text(s, T(s, "endzeile", "die Endzeile kommt nicht hinein", "the end line does not go in", "la línea final no entra",
                       "结束行不放进去", "la ligne de fin n'y entre pas", "bitiş satırı içine girmez"), (0.15, 1.75), FM, "center",
                  ORANGE)
    cat = prozess(s, (2.65, 0.75), 1.0, 0.6, "cat")
    r0 = rohr(s, (0.95, 0.75), (2.15, 0.75), C0)
    n0 = nummer(s, 1.9, 0.98, 0, C0)
    kopien = [tt(s, "Milch", 0.15, ys[0], e, SCHWARZ, "m"), tt(s, "Brot", 0.15, ys[1], e, SCHWARZ, "m")]
    r1 = [linie(s, (2.65, 0.45), (2.65, -0.14), C1, 4.5), rohr(s, (2.65, -0.14), (-1.48, -0.14), C1)]
    n1 = nummer(s, 2.88, 0.2, 1, C1)
    schritt(s, WACHS(term, 0.5), EIN(z[0], 0.5))
    schritt(s, WACHS(shell, 0.6), EIN(l_shell, 0.6), ZEICHNE(korb, 0.6))
    s.pause(0.5)
    for i in range(2):
        schritt(s, EIN([z[i + 1], flug[i]], 0.4))
        schritt(s, ZU(flug[i], 0.15, ys[i], 0.7))
    s.pause(0.4)
    schritt(s, EIN(z[3], 0.4))
    schritt(s, EIN(m_ende, 0.5), ZEICHNE(deckel, 0.5), EIN(l_ende, 0.5))
    s.pause(0.6)
    schritt(s, WACHS(cat[0], 0.5), EIN(cat[1], 0.5), ZEICHNE(r0, 0.5), EIN(n0, 0.5))
    schritt(s, EIN(kopien, 0.2))
    schritt(s, ZU(kopien[0], 2.65, 0.75, 0.8), ZU(kopien[1], 2.65, 0.75, 0.8))
    schritt(s, AUS(kopien, 0.3))
    schritt(s, ZEICHNE(r1, 0.6), EIN(n1, 0.6))
    schritt(s, EIN(aus, 0.5))
    s.speichern()


def k4herestring():
    """wc -c <<< "Linux": Die Shell macht daraus fünf Bytes L i n u x und hängt ein Zeilenende an; wc -c zählt 1 … 6 und schreibt 6."""
    s = Szene("linux/k4herestring")
    term = term_kasten(s, (0, 1.75), 3.0, 0.42)
    cmd = tt(s, '$ wc -c <<< "Linux"', 0, 1.75, EM, SCHWARZ, "m")
    shell = kasten(s, (-2.8, 0.35), 1.1, 0.6, w_shell(s), FM, GRAU_HELL, farbe=GRAU)
    b, x0 = 0.42, -1.85
    xs = [round(x0 + b / 2 + i * b, 4) for i in range(6)]
    boxen = [s.box("", (x, 0.35), breite=b, hoehe=b, form="rect", farbe=SCHWARZ, fuellung=WEISS if i < 5 else ORANGE_HELL, dicke=2)
             for i, x in enumerate(xs)]
    zeichen = [tt(s, c, x, 0.35, 0.21, SCHWARZ, "m") for c, x in zip("Linux", xs)] + [zeilenende(s, xs[5], 0.35, 0.17)]
    l_ang = text(s, T(s, "angehaengt", "angehängt", "appended", "añadido", "附加的", "ajouté", "eklendi"), (xs[5], 0.82), FM, "center",
                 ORANGE)
    pfs = pf(s, (-2.25, 0.35), (x0 - 0.03, 0.35), farbe=GRAU, dicke=2.5)
    kl = klammer(s, x0 + 0.02, x0 + 6 * b - 0.02, -0.02)
    l_6b = text(s, T(s, "sechs", "6 Bytes", "6 bytes", "6 bytes", "6 字节", "6 octets", "6 bayt"), (x0 + 3 * b, -0.25), FM)
    wc = s.box("", (2.6, 0.35), breite=1.3, hoehe=0.95, form="round", farbe=BLAU, fuellung=BLAU_HELL, dicke=2.5)
    wc_t = tt(s, "wc -c", 2.6, 0.6, 0.16, SCHWARZ, "m")
    r0 = rohr(s, (x0 + 6 * b + 0.05, 0.35), (1.95, 0.35), C0)
    n0 = nummer(s, 1.7, 0.58, 0, C0)
    zaehler = [text(s, str(i + 1), (2.6, 0.13), FS, "center", BLAU) for i in range(6)]
    r1 = rohr(s, (2.6, -0.125), (2.6, -0.72), C1)
    n1 = nummer(s, 2.83, -0.42, 1, C1)
    schirm = bildschirm(s, (2.6, -0.95), 1.0, 0.45)
    out = tt(s, "6", 2.6, -0.95, EM, SCHWARZ, "m")
    schritt(s, WACHS(term, 0.5), EIN(cmd, 0.5))
    schritt(s, WACHS(shell[0], 0.5), EIN(shell[1], 0.5))
    schritt(s, ZEICHNE(pfs, 0.4))
    for i in range(5):
        schritt(s, WACHS(boxen[i], 0.25), EIN(zeichen[i], 0.25))
    s.pause(0.6)
    schritt(s, WACHS(boxen[5], 0.5), EIN([zeichen[5], l_ang], 0.5))
    s.pause(0.6)
    schritt(s, WACHS(wc, 0.5), EIN(wc_t, 0.5), ZEICHNE(r0, 0.5), EIN(n0, 0.5))
    for i in range(6):
        teile = [BETONE([boxen[i], zeichen[i]], 0.45), EIN(zaehler[i], 0.3)]
        if i:
            teile.append(AUS(zaehler[i - 1], 0.3))
        schritt(s, *teile)
    schritt(s, ZEICHNE(kl, 0.5), EIN(l_6b, 0.5))
    schritt(s, ZEICHNE(r1, 0.5), WACHS(schirm, 0.5), EIN(n1 + [out], 0.5))
    s.speichern()


# ================================================================== Abschnitt 4: Pipes und Filter
def w_sin(s):
    return T(s, "sin", "Standardeingabe", "standard input", "entrada estándar", "标准输入", "entrée standard", "standart girdi")


def k4pipe():
    """ls /usr/bin | wc -l: beide Prozesse laufen; ls schreibt über 1 in einen Puffer im Kernel, wc liest über 0 daraus, der Füllstand
    schwankt; ls endet, der Puffer leert sich, wc sieht das Ende und schreibt 1018."""
    s = Szene("linux/k4pipe")
    term = term_kasten(s, (0, 1.88), 3.0, 0.4)
    cmd = tt(s, "$ ls /usr/bin | wc -l", 0, 1.88, EM, SCHWARZ, "m")
    kern = kernel(s, -1.5, -0.75, 1.5, 1.45, (-1.4, 1.27))
    lsx, wcx, y = -2.6, 2.6, 0.45
    ls = prozess(s, (lsx, y), 1.1, 0.7, "ls")
    wc = prozess(s, (wcx, y), 1.1, 0.7, "wc -l")
    lauf = T(s, "laeuft", "läuft", "running", "en marcha", "运行中", "en cours", "çalışıyor")
    st_ls = text(s, lauf, (lsx, 1.0), FM, "center", GRUEN)
    st_wc = text(s, lauf, (wcx, 1.0), FM, "center", GRUEN)
    puffer = s.box("", (0, 0.35), breite=1.1, hoehe=1.1, form="rect", farbe=DUNKEL, fuellung=WEISS, dicke=2.5)
    l_puffer = text(s, T(s, "puffer", "Puffer", "buffer", "búfer", "缓冲区", "tampon", "tampon"), (0, -0.45), FM, "center", GRAU)
    pegel = [flaeche(s, -0.53, -0.18, 0.53, round(-0.18 + h, 4), BLAU_HELL) for h in (0.25, 0.5, 0.35, 0.65, 0.3)]
    r1 = rohr(s, (lsx + 0.55, y), (-0.55, y), C1)
    r0 = rohr(s, (0.55, y), (wcx - 0.55, y), C0)
    n1 = nummer(s, lsx + 0.8, y + 0.24, 1, C1)
    n0 = nummer(s, wcx - 0.8, y + 0.24, 0, C0)
    g = geist(s, (lsx, y), 1.1, 0.7)
    g_n = tt(s, "ls", lsx, y, EM, HELLGRAU, "m")
    st_ls2 = text(s, w_beendet(s), (lsx, 1.0), FM, "center", GRAU)
    st_wc2 = text(s, T(s, "siehtende", "sieht das Ende", "sees the end", "ve el final", "看到流结束", "voit la fin", "sonu görür"),
                  (wcx, 1.0), FM, "center", ORANGE)
    r_aus = rohr(s, (wcx, y - 0.35), (wcx, -0.8), C1)
    n_aus = nummer(s, wcx + 0.23, -0.4, 1, C1)
    schirm = bildschirm(s, (wcx, -1.05), 1.2, 0.48)
    aus = tt(s, "1018", wcx, -1.05, EM, SCHWARZ, "m")
    schritt(s, WACHS(term, 0.4), EIN(cmd, 0.4))
    schritt(s, EIN(kern, 0.5), WACHS([ls[0], wc[0]], 0.6), EIN([ls[1], wc[1]], 0.6))
    schritt(s, EIN([st_ls, st_wc], 0.5))
    s.pause(0.5)
    schritt(s, WACHS(puffer, 0.5), EIN(l_puffer, 0.5), ZEICHNE([r1, r0], 0.6), EIN(n1 + n0, 0.6))
    s.pause(0.5)
    alt_t, alt_p = [], None
    for k, (rein, raus) in enumerate(((True, False), (True, True), (True, True), (True, False), (False, True))):
        neu = ([marke(s, -1.8, y, C1)] if rein else []) + ([marke(s, 0.75, y, C0)] if raus else [])
        teile = [EIN(neu, 0.2)] + ([AUS(alt_t, 0.2)] if alt_t else [])
        schritt(s, *teile)
        teile = [VER(t, 1.05, 0, 0.6) for t in neu] + [EIN(pegel[k], 0.6)] + ([AUS(alt_p, 0.6)] if alt_p else [])
        schritt(s, *teile)
        alt_t, alt_p = neu, pegel[k]
    s.pause(0.4)
    schritt(s, AUS(alt_t + ls + [st_ls], 0.6), EIN([g, g_n, st_ls2], 0.6))
    letzt = marke(s, 0.75, y, C0)
    schritt(s, EIN(letzt, 0.2))
    schritt(s, VER(letzt, 1.05, 0, 0.6), AUS(alt_p, 0.6))
    schritt(s, AUS([letzt, st_wc], 0.4), EIN(st_wc2, 0.4))
    s.pause(0.4)
    schritt(s, ZEICHNE(r_aus, 0.5), EIN(n_aus, 0.5), WACHS(schirm, 0.5))
    schritt(s, EIN(aus, 0.5))
    s.speichern()


def k4pipefehler():
    """Oben ls /gibtsnicht | wc -l: Rohr 2 führt an der Pipe vorbei zum Bildschirm, wc zählt 0; unten |&: Rohr 2 mündet in die Pipe,
    wc zählt 1."""
    s = Szene("linux/k4pipefehler")
    t_vorbei = T(s, "vorbei", "an der Pipe vorbei", "past the pipe", "por fuera de la tubería", "绕过管道", "à côté du tube",
                 "borunun yanından")
    t_hinein = T(s, "hinein", "in die Pipe", "into the pipe", "dentro de la tubería", "进入管道", "dans le tube", "boruya")

    def reihe(y, mit):
        r = {}
        r["cmd"] = tt(s, "$ ls /gibtsnicht |& wc -l" if mit else "$ ls /gibtsnicht | wc -l", -3.4, y + 0.68, 0.15)
        r["ls"] = prozess(s, (-2.75, y), 0.8, 0.55, "ls")
        r["pipe"] = rohr(s, (-2.35, y), (-0.15, y), C1)
        r["n"] = nummer(s, -2.1, y + 0.23, 1, C1) + nummer(s, -0.4, y + 0.23, 0, C0) + nummer(s, -2.52, y - 0.44, 2, C2)
        r["wc"] = prozess(s, (0.4, y), 1.1, 0.55, "wc -l")
        r["a"] = rohr(s, (0.95, y), (1.5, y), C1)
        r["schirm"] = bildschirm(s, (2.45, y), 1.9, 0.8)
        xe = -1.5 if mit else 2.45
        r["r2"] = [linie(s, (-2.75, y - 0.275), (-2.75, y - 0.6), C2, 4.5), linie(s, (-2.75, y - 0.6), (xe, y - 0.6), C2, 4.5),
                   rohr(s, (xe, y - 0.6), (xe, y - 0.07 if mit else y - 0.4), C2)]
        r["m"] = marke(s, -2.75, y - 0.38, C2)
        r["l"] = text(s, t_hinein, (-1.35, y - 0.6), FX, "left", C2) if mit else text(s, t_vorbei, (0.4, y - 0.78), FX, "center", C2)
        return r

    for y, mit in ((0.95, False), (-1.0, True)):
        r = reihe(y, mit)
        if mit:
            s.pause(0.6)
        schritt(s, EIN(r["cmd"], 0.4))
        schritt(s, WACHS([r["ls"][0], r["wc"][0], r["schirm"]], 0.5), EIN([r["ls"][1], r["wc"][1]], 0.5))
        schritt(s, ZEICHNE([r["pipe"], r["a"]] + r["r2"], 0.6), EIN(r["n"], 0.6))
        schritt(s, EIN(r["m"], 0.2))
        schritt(s, VER(r["m"], 0, -0.22, 0.3))
        if not mit:
            schritt(s, VER(r["m"], 5.2, 0, 1.1), EIN(r["l"], 0.6))
            schritt(s, VER(r["m"], 0, 0.25, 0.3))
            meld = text(s, "ls: cannot access …", (2.45, y + 0.15), FX, "center", DUNKEL)
            schritt(s, AUS(r["m"], 0.3), EIN(meld, 0.4))
            zahl = tt(s, "0", 2.45, y - 0.15, EM, SCHWARZ, "m")
        else:
            schritt(s, VER(r["m"], 1.25, 0, 0.4), EIN(r["l"], 0.4))
            schritt(s, VER(r["m"], 0, 0.6, 0.4))
            schritt(s, VER(r["m"], 1.15, 0, 0.5))
            schritt(s, AUS(r["m"], 0.3))
            zahl = tt(s, "1", 2.45, y, EM, SCHWARZ, "m")
        schritt(s, EIN(zahl, 0.5), BETONE(r["wc"], 0.6))
    s.speichern()


def k4filter():
    """Die sieben Zeilen von obst.txt fließen nacheinander in sort, head -n 2, grep Apfel und uniq; unter jedem Filter das Ergebnis."""
    s = Szene("linux/k4filter")
    cx = [-2.75, -1.4, -0.05, 1.3, 2.65]
    obst = ["Apfel", "Birne", "Apfel", "Kiwi", "Banane", "Apfel", "Birne"]
    erg = [sorted(obst), obst[:2], [w for w in obst if w == "Apfel"], obst]
    yk, dz, y0 = 1.5, 0.26, 1.02
    doc = dokument(s, (cx[0], 0.24), 1.15, 1.95)
    l_doc = text(s, "obst.txt", (cx[0], yk), FK)
    z0 = [text(s, w, (cx[0], y0 - dz * i), FM) for i, w in enumerate(obst)]
    bus0 = linie(s, (cx[0], yk + 0.17), (cx[0], 1.88), GRAU, 2.5)
    busse = [linie(s, (cx[k], 1.88), (cx[k + 1], 1.88), GRAU, 2.5) for k in range(4)]
    tropfen = [pf(s, (cx[k + 1], 1.88), (cx[k + 1], yk + 0.2), farbe=GRAU, dicke=2.5) for k in range(4)]
    filt = [prozess(s, (cx[k + 1], yk), 1.2, 0.38, n, 0.14) for k, n in enumerate(["sort", "head -n 2", "grep Apfel", "uniq"])]
    res = [[text(s, w, (cx[k + 1], y0 - dz * i), FM) for i, w in enumerate(ws)] for k, ws in enumerate(erg)]
    note = text(s, T(s, "nachbarn", "keine zwei gleichen\nZeilen untereinander", "no two equal lines\nnext to each other",
                     "no hay dos líneas\niguales seguidas", "没有相邻的\n相同行", "pas deux lignes égales\nl'une sous l'autre",
                     "alt alta iki aynı\nsatır yok"), (cx[4], y0 - dz * 7 - 0.12), FX, "center", GRAU)
    schritt(s, WACHS(doc, 0.6), EIN([l_doc] + z0, 0.6))
    s.pause(0.6)
    for k in range(4):
        schritt(s, ZEICHNE(([bus0] if k == 0 else []) + [busse[k]], 0.4))
        schritt(s, ZEICHNE(tropfen[k], 0.3), WACHS(filt[k][0], 0.4), EIN(filt[k][1], 0.4))
        schritt(s, EIN(res[k], 0.6))
        if k < 3:
            s.pause(0.3)
    schritt(s, EIN(note, 0.5))
    s.speichern()


def k4fliessband():
    """sort obst.txt | uniq | wc -l als Fließband: unter jeder Pipe das Zwischenergebnis (7 geordnete Zeilen, 4 Sorten), am Ende 4."""
    s = Szene("linux/k4fliessband")
    term = term_kasten(s, (0, 1.9), 3.4, 0.4)
    cmd = tt(s, "$ sort obst.txt | uniq | wc -l", 0, 1.9, 0.16, SCHWARZ, "m")
    y = 1.2
    st = [prozess(s, (-2.45, y), 1.6, 0.5, "sort obst.txt", 0.15), prozess(s, (0.0, y), 0.9, 0.5, "uniq", 0.16),
          prozess(s, (2.45, y), 1.1, 0.5, "wc -l", 0.16)]
    pipes = [pf(s, (-1.65, y), (-0.45, y), farbe=DUNKEL, dicke=3), pf(s, (0.45, y), (1.9, y), farbe=DUNKEL, dicke=3)]
    mx = [-1.05, 1.17]
    stiel = [linie(s, (x, y - 0.05), (x, 0.82), GRAU, 2, DOT) for x in mx]
    dz = 0.24
    s1 = [text(s, w, (mx[0], 0.66 - dz * i), FM) for i, w in enumerate(["Apfel"] * 3 + ["Banane", "Birne", "Birne", "Kiwi"])]
    s2 = [text(s, w, (mx[1], 0.66 - dz * i), FM) for i, w in enumerate(["Apfel", "Banane", "Birne", "Kiwi"])]
    l1 = text(s, T(s, "geordnet", "7 Zeilen, geordnet", "7 lines, sorted", "7 líneas, ordenadas", "7 行，已排序", "7 lignes, triées",
                   "7 satır, sıralı"), (mx[0], 0.66 - dz * 7 - 0.03), FX, "center", GRAU)
    l2 = text(s, T(s, "sorten", "4 Sorten", "4 kinds", "4 tipos", "4 种", "4 sortes", "4 çeşit"), (mx[1], 0.66 - dz * 4 - 0.03), FX,
              "center", GRAU)
    aus = rohr(s, (2.45, y - 0.25), (2.45, 0.42), C1)
    schirm = bildschirm(s, (2.45, 0.18), 0.8, 0.45)
    vier = tt(s, "4", 2.45, 0.18, 0.2, SCHWARZ, "m")
    schritt(s, WACHS(term, 0.4), EIN(cmd, 0.4))
    schritt(s, WACHS([b[0] for b in st], 0.6), EIN([b[1] for b in st], 0.6), ZEICHNE(pipes, 0.6))
    s.pause(0.6)
    schritt(s, BETONE(st[0], 0.6))
    schritt(s, ZEICHNE(stiel[0], 0.3), EIN(s1, 0.7))
    schritt(s, EIN(l1, 0.4))
    s.pause(0.6)
    schritt(s, BETONE(st[1], 0.6))
    schritt(s, ZEICHNE(stiel[1], 0.3), EIN(s2, 0.7))
    schritt(s, EIN(l2, 0.4))
    s.pause(0.6)
    schritt(s, BETONE(st[2], 0.6))
    schritt(s, ZEICHNE(aus, 0.5), WACHS(schirm, 0.5))
    schritt(s, EIN(vier, 0.5))
    s.speichern()


def k4tee():
    """tee als T-Stück: Apfel, Banane, Birne, Kiwi kommen von links, jede Zeile geht weiter nach rechts zu wc -l und zugleich nach
    unten in sorten.txt; am Ende 4."""
    s = Szene("linux/k4tee")
    term = term_kasten(s, (0, 1.88), 3.75, 0.4)
    cmd = tt(s, "$ sort obst.txt | uniq | tee sorten.txt | wc -l", 0, 1.88, 0.14, SCHWARZ, "m")
    y, tx = 0.75, -0.2
    ein = rohr(s, (-3.35, y), (tx - 0.4, y), C1)
    l_von = text(s, T(s, "vonuniq", "von uniq", "from uniq", "de uniq", "来自 uniq", "de uniq", "uniq'ten"), (-3.35, y + 0.35), FM,
                 "left", GRAU)
    tee = prozess(s, (tx, y), 0.8, 0.5, "tee")
    l_tee = text(s, T(s, "tstueck", "T-Stück", "T-piece", "pieza en T", "三通", "raccord en T", "T parçası"), (tx, y + 0.42), FM,
                 "center", GRAU)
    rechts = rohr(s, (tx + 0.4, y), (1.95, y), C1)
    wc = prozess(s, (2.5, y), 1.1, 0.5, "wc -l")
    unten = rohr(s, (tx, y - 0.25), (tx, -0.08), C1)
    doc = dokument(s, (tx, -0.75), 1.3, 1.3)
    l_doc = text(s, "sorten.txt", (tx - 0.75, -0.25), FM, "right")
    sorten = ["Apfel", "Banane", "Birne", "Kiwi"]
    qx = [-1.0, -1.68, -2.36, -3.04]
    karten = [karte(s, x, y, w, 0.62, GRAU, WEISS, FX) for x, w in zip(qx, sorten)]
    kopien = [karte(s, tx, y, w, 0.62, GRAU, WEISS, FX) for w in sorten]
    zy = [-0.35 - 0.25 * i for i in range(4)]
    r_aus = rohr(s, (2.5, y - 0.25), (2.5, -0.15), C1)
    schirm = bildschirm(s, (2.5, -0.4), 0.8, 0.45)
    vier = tt(s, "4", 2.5, -0.4, 0.2, SCHWARZ, "m")
    schritt(s, WACHS(term, 0.4), EIN(cmd, 0.4))
    schritt(s, ZEICHNE([ein, rechts, unten], 0.6), WACHS([tee[0], wc[0], doc], 0.6), EIN([tee[1], wc[1], l_von, l_tee, l_doc], 0.6))
    schritt(s, WACHS([k[0] for k in karten], 0.5), EIN([k[1] for k in karten], 0.5))
    s.pause(0.6)
    for i in range(4):
        teile = VERS(karten[i], tx - qx[i], 0, 0.5)
        if i:
            teile.append(AUS(kopien[i - 1], 0.3))
        schritt(s, *teile)
        schritt(s, EIN(kopien[i], 0.15))
        schritt(s, *VERS(karten[i], 0, zy[i] - y, 0.6), *VERS(kopien[i], 2.7, 0, 0.6))
    schritt(s, AUS(kopien[3], 0.3))
    s.pause(0.4)
    schritt(s, ZEICHNE(r_aus, 0.5), WACHS(schirm, 0.5))
    schritt(s, EIN(vier, 0.5))
    s.speichern()


# ================================================================== Abschnitt 5: Der Exit-Status
def k4exitstatus():
    """ls /gibtsnicht endet und hinterlässt den Zettel 2; der Kernel reicht ihn an die wartende Shell, die sich $? = 2 merkt;
    echo $? bekommt von der Shell die 2 eingesetzt."""
    s = Szene("linux/k4exitstatus")
    shell = s.box("", (-2.3, 0.75), breite=2.0, hoehe=1.05, form="round", farbe=GRAU, fuellung=GRAU_HELL, dicke=2.5)
    l_shell = text(s, w_shell(s), (-2.3, 1.1), FK, "center", GRAU)
    wartet = text(s, T(s, "wartet", "wartet …", "waits …", "espera …", "等待中 …", "attend …", "bekliyor …"), (-2.3, 0.65), FM,
                  "center", DUNKEL)
    merkt = text(s, T(s, "merkt", "merkt sich:", "remembers:", "recuerda:", "记住：", "retient :", "hatırlar:"), (-2.3, 0.75), FM,
                 "center", DUNKEL)
    wert = tt(s, "$? = 2", -2.3, 0.47, EM, SCHWARZ, "m")
    kern = kernel(s, -1.05, -0.1, 0.95, 1.6, (-0.05, 1.42), "center")
    weg = pf(s, (1.25, 0.6), (-1.25, 0.6), farbe=GRAU, dicke=2, dash=DASH)
    l_weg = text(s, T(s, "exit", "Exit-Status", "exit status", "estado de salida", "退出状态", "code de retour", "çıkış durumu"),
                 (-0.05, 0.85), FM, "center", DUNKEL)
    pr = prozess(s, (2.3, 0.75), 2.0, 0.6, "ls /gibtsnicht", 0.15)
    g = geist(s, (2.3, 0.75), 2.0, 0.6)
    g_t = text(s, w_beendet(s), (2.3, 1.25), FM, "center", GRAU)
    g_n = tt(s, "ls /gibtsnicht", 2.3, 0.75, 0.15, HELLGRAU, "m")
    z = zettel(s, 2.3, 0.3, "2", ORANGE)
    term = term_kasten(s, (-1.25, -0.95), 4.2, 0.8)
    e1 = tt(s, "$ echo $?", -3.2, -0.77)
    e2 = tt(s, "2", -3.2, -1.1)
    pfeil = pf(s, (-2.3, 0.22), (sp(-3.2, 7.5), -0.62), farbe=ORANGE, dicke=2.5)
    l_ein = text(s, T(s, "setztein", "die Shell setzt 2 ein", "the shell puts in 2", "la shell pone el 2", "Shell 填入 2",
                      "le shell met 2 à la place", "kabuk yerine 2 koyar"), (-1.7, -0.77), FM, "left", ORANGE)
    schritt(s, EIN(kern, 0.5), WACHS([shell, pr[0]], 0.6), EIN([l_shell, pr[1]], 0.6))
    schritt(s, EIN(wartet, 0.5))
    s.pause(0.6)
    schritt(s, AUS(pr, 0.6), EIN([g, g_n, g_t], 0.6), WACHS(z[0], 0.6), EIN(z[1], 0.6))
    schritt(s, *VERS(z, -2.35, 0.3, 0.8), ZEICHNE(weg, 0.8), EIN(l_weg, 0.8))
    schritt(s, *VERS(z, -2.25, -0.13, 0.8))
    schritt(s, AUS(z + [wartet], 0.4), EIN([merkt, wert], 0.5))
    s.pause(0.6)
    schritt(s, WACHS(term, 0.5), EIN(e1, 0.5))
    schritt(s, ZEICHNE(pfeil, 0.6), EIN(l_ein, 0.6))
    schritt(s, EIN(e2, 0.5))
    s.speichern()


def k4grepstatus():
    """grep -q in drei Fällen: Treffer → 0, kein Treffer → 1, Datei fehlt → 2 (nur hier eine Meldung)."""
    s = Szene("linux/k4grepstatus")
    cx = [-2.3, 0.0, 2.3]
    K = [tt(s, c, x, 1.6, 0.13, SCHWARZ, "m") for c, x in
         zip(["grep -q Apfel obst.txt", "grep -q Mango obst.txt", "grep -q Apfel fehlt.txt"], cx)]
    icons = [haken(s, cx[0], 0.98, GRUEN, 0.14, 5), [linie(s, (-0.15, 0.98), (0.15, 0.98), GRAU, 5)],
             [s.kreuzchen(None, cx[2], 0.98, ROT, 0.3, 5)]]
    bes = [("gefunden", "Apfel gefunden", "Apfel found", "Apfel encontrado", "找到 Apfel", "Apfel trouvé", "Apfel bulundu"),
           ("nichtgef", "Mango nicht gefunden", "Mango not found", "Mango no encontrado", "未找到 Mango", "Mango introuvable",
            "Mango bulunamadı"),
           ("fehlt", "Datei fehlt", "file missing", "falta el archivo", "文件不存在", "fichier absent", "dosya yok")]
    labs = [text(s, T(s, *b), (x, 0.6), FM, "center", f) for b, x, f in zip(bes, cx, (GRUEN, GRAU, ROT))]
    pfeile = [pf(s, (x, 0.42), (x, -0.32), farbe=GRAU, dicke=2.5) for x in cx]
    farben = [(GRUEN, GRUEN_HELL), (ORANGE, ORANGE_HELL), (ROT, ROT_HELL)]
    boxen = [s.box("", (x, -0.58), breite=1.3, hoehe=0.48, form="round", farbe=f, fuellung=h, dicke=2.5) for x, (f, h) in zip(cx, farben)]
    werte = [tt(s, "$? = %d" % i, x, -0.58, 0.19, SCHWARZ, "m") for i, x in enumerate(cx)]
    meld = text(s, "grep: fehlt.txt: No such\nfile or directory", (cx[2], -1.32), FX, "center", ORANGE)
    l_m = text(s, T(s, "meldung", "Meldung:", "message:", "mensaje:", "消息：", "message :", "mesaj:"), (cx[2], -1.0), FX, "center",
               GRAU)
    for i in range(3):
        if i:
            s.pause(0.4)
        schritt(s, EIN(K[i], 0.4))
        schritt(s, ZEICHNE(icons[i], 0.5), EIN(labs[i], 0.5))
        schritt(s, ZEICHNE(pfeile[i], 0.4))
        schritt(s, WACHS(boxen[i], 0.5), EIN(werte[i], 0.5))
        if i == 2:
            schritt(s, EIN([meld, l_m], 0.5))
    s.speichern()


def k4nummern():
    """Zahlenstrahl 0 bis 255 (senkrecht, nicht maßstäblich): 0 Erfolg, 1–125 Fehler des Programms, 126 nicht ausführbar,
    127 nicht gefunden, 129–255 Abbruch durch Nachricht n = 128 + n mit 130 (Strg+C) und 141 (13)."""
    s = Szene("linux/k4nummern")
    ax, lx = -2.3, -1.95
    Y = {0: -1.6, 1: -1.3, 125: -0.45, 126: -0.12, 127: 0.2, 129: 0.55, 130: 0.8, 141: 1.12, 255: 1.75}
    achse = linie(s, (ax, -1.8), (ax, 1.95), DUNKEL, 3)
    titel = text(s, T(s, "titel", "Exit-Status", "exit status", "estado de salida", "退出状态", "code de retour", "çıkış durumu"),
                 (ax, 2.15), FK, "center", DUNKEL)

    def nr(n):
        return [linie(s, (ax - 0.08, Y[n]), (ax + 0.08, Y[n]), DUNKEL, 2), text(s, str(n), (ax - 0.15, Y[n]), FM, "right", DUNKEL)]

    def punkt(n, f):
        return s.kreis(None, ax, Y[n], 0.075, farbe=f, dicke=2, fuellung=f, deckung=1.0)

    def lab(n, kt, f, y=None):
        return text(s, T(s, *kt), (lx, Y[n] if y is None else y), FM, "left", f)

    e0 = nr(0) + [punkt(0, GRUEN), lab(0, ("erfolg", "Erfolg", "success", "éxito", "成功", "succès", "başarı"), GRUEN)]
    b1 = [flaeche(s, ax + 0.05, Y[1], ax + 0.2, Y[125], ORANGE, deckung=0.8)] + nr(1) + nr(125)
    l1 = lab(1, ("prog", "vom Programm gemeldete Fehler\n(etwa 1 und 2)", "errors reported by the program\n(e.g. 1 and 2)",
                 "errores que informa el programa\n(p. ej., 1 y 2)", "程序自己报告的错误\n（例如 1 和 2）",
                 "erreurs signalées par le programme\n(par ex. 1 et 2)", "programın bildirdiği hatalar\n(örneğin 1 ve 2)"), ORANGE,
             (Y[1] + Y[125]) / 2)
    e126 = nr(126) + [punkt(126, ROT), lab(126, ("nausf", "nicht ausführbar", "not executable", "no ejecutable", "无法执行",
                                                 "non exécutable", "çalıştırılamaz"), ROT)]
    e127 = nr(127) + [punkt(127, ROT), lab(127, ("ngef", "nicht gefunden", "not found", "no encontrado", "未找到", "introuvable",
                                                 "bulunamadı"), ROT)]
    b2 = [flaeche(s, ax + 0.05, Y[129], ax + 0.2, Y[255], BLAU, deckung=0.8)] + nr(129) + nr(255)
    l2 = lab(255, ("abbruch", "Abbruch durch Unterbrechungsnachricht n:  128 + n", "aborted by interrupt message n:  128 + n",
                   "interrumpido por el mensaje de interrupción n:  128 + n", "被中断消息 n 终止：128 + n",
                   "interrompu par le message d'interruption n :  128 + n", "kesme mesajı n ile sonlandırma:  128 + n"), BLAU, 1.47)
    e130 = nr(130) + [punkt(130, DUNKEL), lab(130, ("n130", "= 128 + 2  (Strg+C)", "= 128 + 2  (Ctrl+C)", "= 128 + 2  (Ctrl+C)",
                                                    "= 128 + 2（Ctrl+C）", "= 128 + 2  (Ctrl+C)", "= 128 + 2  (Ctrl+C)"), DUNKEL)]
    e141 = nr(141) + [punkt(141, DUNKEL), lab(141, ("n141", "= 128 + 13  (Schreiben ohne Leser)", "= 128 + 13  (writing with no reader)",
                                                    "= 128 + 13  (escribir sin lector)", "= 128 + 13（写入时无读取方）",
                                                    "= 128 + 13  (écriture sans lecteur)", "= 128 + 13  (okuyan yokken yazma)"),
                                                DUNKEL)]
    note = text(s, T(s, "massstab", "nicht maßstäblich", "not to scale", "no a escala", "未按比例", "pas à l'échelle", "ölçekli değil"),
                (3.4, -1.75), FX, "right", GRAU)
    schritt(s, ZEICHNE(achse, 0.6), EIN(titel, 0.6))
    s.pause(0.4)
    schritt(s, EIN(e0, 0.6))
    s.pause(0.4)
    schritt(s, EIN(b1, 0.6))
    schritt(s, EIN(l1, 0.5))
    s.pause(0.5)
    schritt(s, EIN(e126, 0.5))
    schritt(s, EIN(e127, 0.5))
    s.pause(0.6)
    schritt(s, EIN(b2, 0.6), EIN(l2, 0.6))
    schritt(s, EIN(e130, 0.5))
    schritt(s, EIN(e141, 0.5))
    schritt(s, EIN(note, 0.4))
    s.speichern()


# ================================================================== Abschnitt 6: Befehle verketten
def k4weichen():
    """Zwei Weichen nach dem Exit-Status von a: links a && b (0 → b, sonst vorbei), rechts a || b (≠ 0 → b, sonst vorbei);
    je zwei Züge mit 0 und 1 fahren beide Fälle ab und bleiben am Ziel stehen."""
    s = Szene("linux/k4weichen")
    trenn = linie(s, (0, 2.0), (0, -1.0), HELLGRAU, 2, DASH)
    t0 = T(s, "st0", "Status 0", "status 0", "estado 0", "状态 0", "statut 0", "durum 0")
    tn = T(s, "stn", r"Status \neq 0", r"status \neq 0", r"estado \neq 0", r"状态 \neq 0", r"statut \neq 0", r"durum \neq 0")
    t_v = T(s, "vorbei", "vorbei", "skipped", "se salta", "跳过", "sauté", "atlanır")

    def panel(px, op, b_bei_null):
        r = {"px": px}
        r["kopf"] = tt(s, "a %s b" % op, px, 1.82, 0.2, SCHWARZ, "m")
        r["a"] = prozess(s, (px, 1.2), 0.7, 0.42, "a", 0.18)
        r["gleis"] = [linie(s, (px, 0.99), (px, 0.5), DUNKEL, 4), linie(s, (px, 0.5), (px - 0.8, -0.3), DUNKEL, 4),
                      linie(s, (px, 0.5), (px + 0.8, -0.3), DUNKEL, 4)]
        r["b"] = prozess(s, (px - 0.8, -0.58), 0.7, 0.42, "b", 0.18)
        r["v"] = text(s, t_v, (px + 0.8, -0.58), FM, "center", GRAU)
        r["lab"] = [text(s, t0 if b_bei_null else tn, (px - 0.45, 0.25), FM, "right", GRUEN if b_bei_null else ORANGE),
                    text(s, tn if b_bei_null else t0, (px + 0.45, 0.25), FM, "left", ORANGE if b_bei_null else GRUEN)]
        return r

    L, R = panel(-1.75, "&&", True), panel(1.75, "||", False)
    leg = text(s, T(s, "leg", "Zahl im Zug: Exit-Status von a", "number on the train: exit status of a",
                    "número en el tren: estado de salida de a", "列车上的数字：a 的退出状态", "nombre sur le train : code de retour de a",
                    "trendeki sayı: a'nın çıkış durumu"), (0, -1.25), FM, "center", GRAU)
    schritt(s, ZEICHNE(trenn, 0.4))
    for P in (L, R):
        schritt(s, EIN(P["kopf"], 0.4), WACHS(P["a"][0], 0.5), EIN(P["a"][1], 0.5))
        schritt(s, ZEICHNE(P["gleis"], 0.6), WACHS(P["b"][0], 0.6), EIN([P["b"][1], P["v"]] + P["lab"], 0.6))
    schritt(s, EIN(leg, 0.5))
    s.pause(0.5)
    for P, b_bei_null in ((L, True), (R, False)):
        for st in (0, 1):
            zum_b = (st == 0) == b_bei_null
            f, h = (GRUEN, GRUEN_HELL) if st == 0 else (ORANGE, ORANGE_HELL)
            zug = karte(s, P["px"], 0.85, str(st), 0.36, f, h, FM, f, h=0.26)
            schritt(s, WACHS(zug[0], 0.3), EIN(zug[1], 0.3))
            schritt(s, *VERS(zug, 0, -0.35, 0.4))
            schritt(s, *VERS(zug, -0.6 if zum_b else 0.6, -0.6, 0.6))
            schritt(s, BETONE(P["b"] if zum_b else P["v"], 0.5))
        if P is L:
            s.pause(0.5)
    s.speichern()


def k4kette():
    """a && b || c als Entscheidungsbaum: a scheitert → c; a gelingt → b; b gelingt → fertig; b scheitert → c (roter Weg, zuletzt)."""
    s = Szene("linux/k4kette")
    kopf = tt(s, "a && b || c", 0, 1.85, 0.22, SCHWARZ, "m")
    A = prozess(s, (-2.4, 0.85), 0.75, 0.45, "a", 0.2)
    B = prozess(s, (0.0, 0.85), 0.75, 0.45, "b", 0.2)
    C = prozess(s, (0.0, -1.0), 0.75, 0.45, "c", 0.2)
    E = karte(s, 2.6, 0.85, T(s, "fertig", "fertig", "done", "fin", "结束", "fin", "bitti"), 1.0, GRAU, GRAU_HELL, FM, h=0.45)
    ab = pf(s, (-2.0, 0.85), (-0.4, 0.85), farbe=GRUEN, dicke=3)
    ac = pf(s, (-2.25, 0.6), (-0.4, -0.95), farbe=ORANGE, dicke=3)
    be = pf(s, (0.4, 0.85), (2.08, 0.85), farbe=GRUEN, dicke=3)
    bc = pf(s, (0.0, 0.6), (0.0, -0.75), farbe=ROT, dicke=4.5, spitze=0.14)
    l_ab = haken(s, -1.45, 1.07, GRUEN, 0.08, 3.5) + [text(s, "0", (-1.15, 1.07), FM, "center", GRUEN)]
    l_be = haken(s, 0.95, 1.07, GRUEN, 0.08, 3.5) + [text(s, "0", (1.25, 1.07), FM, "center", GRUEN)]
    l_ac = [s.kreuzchen(None, -1.78, -0.42, ORANGE, 0.16, 3.5), text(s, r"\neq 0", (-1.45, -0.42), FM, "center", ORANGE)]
    l_bc = [s.kreuzchen(None, 0.3, 0.0, ROT, 0.16, 3.5), text(s, r"\neq 0", (0.62, 0.0), FM, "center", ROT)]
    l_ueb = text(s, T(s, "uebersehen", "leicht übersehen", "easy to overlook", "fácil de pasar por alto", "容易被忽视",
                      "facile à manquer", "kolayca gözden kaçar"), (0.2, -0.32), FM, "left", ROT)
    schritt(s, EIN(kopf, 0.5), WACHS(A[0], 0.5), EIN(A[1], 0.5))
    s.pause(0.6)
    schritt(s, ZEICHNE(ac, 0.6), EIN(l_ac, 0.6))
    schritt(s, WACHS(C[0], 0.5), EIN(C[1], 0.5))
    s.pause(0.6)
    schritt(s, ZEICHNE(ab, 0.6), EIN(l_ab, 0.6))
    schritt(s, WACHS(B[0], 0.5), EIN(B[1], 0.5))
    schritt(s, ZEICHNE(be, 0.6), EIN(l_be, 0.6), WACHS(E[0], 0.6), EIN(E[1], 0.6))
    s.pause(0.8)
    schritt(s, ZEICHNE(bc, 0.8), EIN(l_bc, 0.8))
    schritt(s, BETONE(bc, 0.8), EIN(l_ueb, 0.6))
    s.speichern()


def k4pipestatus():
    """sort fehlt.txt | head -n 3: sort endet mit 2, head mit 0; $? bekommt nur die 0, PIPESTATUS hält 2 0 fest; mit pipefail wird
    $? zur 2."""
    s = Szene("linux/k4pipestatus")
    y = 1.3
    so = prozess(s, (-1.8, y), 2.0, 0.5, "sort fehlt.txt", 0.15)
    he = prozess(s, (1.6, y), 1.5, 0.5, "head -n 3", 0.15)
    pipe = rohr(s, (-0.8, y), (0.85, y), C1)
    z2 = zettel(s, -1.8, 0.55, "2", ORANGE)
    z0 = zettel(s, 1.6, 0.55, "0", GRUEN)
    stiele = [linie(s, (-1.8, y - 0.25), (-1.8, 0.71), GRAU, 2, DOT), linie(s, (1.6, y - 0.25), (1.6, 0.71), GRAU, 2, DOT)]
    ps = s.box("", (-0.1, -0.4), breite=2.6, hoehe=0.5, form="round", farbe=DUNKEL, fuellung=WEISS, dicke=2.5)
    ps_t = tt(s, "PIPESTATUS: 2 0", -0.1, -0.4, 0.17, SCHWARZ, "m")
    a_ps = [pf(s, (-1.7, 0.39), (-0.8, -0.15), farbe=GRAU), pf(s, (1.5, 0.39), (0.6, -0.15), farbe=GRAU)]
    v0 = pf(s, (1.6, 0.39), (1.6, -1.07), farbe=GRUEN, dicke=2.5)
    v2 = pf(s, (-1.8, 0.39), (-1.8, -1.07), farbe=ORANGE, dicke=2.5)
    q0 = s.box("", (1.6, -1.3), breite=1.4, hoehe=0.45, form="round", farbe=GRUEN, fuellung=GRUEN_HELL, dicke=2.5)
    q0_t = tt(s, "$? = 0", 1.6, -1.3, 0.18, SCHWARZ, "m")
    l_q0 = text(s, T(s, "ohnepf", "ohne pipefail", "without pipefail", "sin pipefail", "不启用 pipefail", "sans pipefail",
                     "pipefail olmadan"), (1.6, -1.72), FM, "center", GRUEN)
    q2 = s.box("", (-1.8, -1.3), breite=1.4, hoehe=0.45, form="round", farbe=ORANGE, fuellung=ORANGE_HELL, dicke=2.5)
    q2_t = tt(s, "$? = 2", -1.8, -1.3, 0.18, SCHWARZ, "m")
    l_q2 = text(s, T(s, "mitpf", "mit pipefail", "with pipefail", "con pipefail", "启用 pipefail", "avec pipefail", "pipefail ile"),
                (-1.8, -1.72), FM, "center", ORANGE)
    sx = -3.0
    schalter = s.box("", (sx, -1.3), breite=0.5, hoehe=0.24, form="round", farbe=GRAU, fuellung=WEISS, dicke=2)
    an = s.box("", (sx, -1.3), breite=0.5, hoehe=0.24, form="round", farbe=GRUEN, fuellung=GRUEN, deckung=0.7, dicke=2)
    knopf = s.kreis(None, sx - 0.12, -1.3, 0.09, farbe=DUNKEL, dicke=2, fuellung=WEISS, deckung=1.0)
    knopf2 = s.kreis(None, sx + 0.12, -1.3, 0.09, farbe=DUNKEL, dicke=2, fuellung=WEISS, deckung=1.0)
    l_pf = text(s, "pipefail", (sx, -1.02), FX, "center", DUNKEL)
    l_an = text(s, T(s, "an", "an", "on", "activado", "开", "activé", "açık"), (sx, -1.58), FX, "center", GRUEN)
    schritt(s, WACHS([so[0], he[0]], 0.6), EIN([so[1], he[1]], 0.6), ZEICHNE(pipe, 0.6))
    s.pause(0.5)
    schritt(s, ZEICHNE(stiele[0], 0.3), WACHS(z2[0], 0.5), EIN(z2[1], 0.5))
    schritt(s, ZEICHNE(stiele[1], 0.3), WACHS(z0[0], 0.5), EIN(z0[1], 0.5))
    s.pause(0.6)
    schritt(s, ZEICHNE(v0, 0.6))
    schritt(s, WACHS(q0, 0.5), EIN([q0_t, l_q0], 0.5))
    s.pause(0.6)
    schritt(s, ZEICHNE(a_ps, 0.6))
    schritt(s, WACHS(ps, 0.5), EIN(ps_t, 0.5))
    s.pause(0.6)
    schritt(s, WACHS(schalter, 0.4), EIN([knopf, l_pf], 0.4))
    schritt(s, AUS(knopf, 0.4), EIN([an, knopf2, l_an], 0.4))
    schritt(s, ZEICHNE(v2, 0.6))
    schritt(s, WACHS(q2, 0.5), EIN([q2_t, l_q2], 0.5))
    s.speichern()


def k4yeshead():
    """yes | head -n 1 als Zeitleiste: yes schreibt y in die Pipe, head liest eins, gibt es aus und endet mit 0; das Leseende ist zu,
    der nächste Schreibversuch bringt Nachricht 13, yes endet mit 141; PIPESTATUS 141 0."""
    s = Szene("linux/k4yeshead")
    y = 1.05
    yes = prozess(s, (-2.85, y), 0.8, 0.55, "yes")
    rx0, rx1 = -2.3, 0.65
    rohr_k = s.box("", ((rx0 + rx1) / 2, y), breite=rx1 - rx0, hoehe=0.42, form="rect", farbe=DUNKEL, fuellung=WEISS, dicke=2.5)
    l_pipe = text(s, T(s, "pipe", "Pipe", "pipe", "tubería", "管道", "tube", "boru"), ((rx0 + rx1) / 2, y + 0.38), FM, "center", GRAU)
    head = prozess(s, (1.6, y), 1.5, 0.55, "head -n 1", 0.15)
    a_out = rohr(s, (1.6, y - 0.275), (1.6, 0.175), C1)
    schirm = bildschirm(s, (1.6, -0.05), 1.0, 0.45)
    aus_y = tt(s, "y", 1.6, -0.05, 0.2, SCHWARZ, "m")
    xs = rx0 + 0.15
    t = [tt(s, "y", xs, y, 0.2, SCHWARZ, "m") for _ in range(4)]
    wand = linie(s, (rx1, y - 0.21), (rx1, y + 0.21), ROT, 7)
    hg, hg_n = geist(s, (1.6, y), 1.5, 0.55), tt(s, "head -n 1", 1.6, y, 0.15, HELLGRAU, "m")
    yg, yg_n = geist(s, (-2.85, y), 0.8, 0.55), tt(s, "yes", -2.85, y, EM, HELLGRAU, "m")
    z0 = zettel(s, 2.75, y, "0", GRUEN)
    z141 = zettel(s, -2.85, y - 0.62, "141", ORANGE, b=0.62)
    l_141 = text(s, "128 + 13", (-2.85, y - 0.93), FX, "center", ORANGE)
    blitz = [linie(s, (-2.95, y + 0.85), (-2.78, y + 0.62), ORANGE, 4), linie(s, (-2.78, y + 0.62), (-2.92, y + 0.6), ORANGE, 4),
             linie(s, (-2.92, y + 0.6), (-2.75, y + 0.36), ORANGE, 4)]
    l_n13 = text(s, T(s, "n13", "Nachricht 13", "message 13", "mensaje 13", "消息 13", "message 13", "mesaj 13"), (-2.6, y + 0.68), FM,
                 "left", ORANGE)
    liste = [("y1", "1  yes schreibt Zeilen in die Pipe", "1  yes writes lines into the pipe", "1  yes escribe líneas en la tubería",
              "1  yes 向管道写入行", "1  yes écrit des lignes dans le tube", "1  yes boruya satır yazar"),
             ("y2", "2  head liest eine, gibt sie aus, endet mit 0", "2  head reads one, prints it, ends with 0",
              "2  head lee una, la muestra, termina con 0", "2  head 读取一行、输出、以 0 结束", "2  head en lit une, l'affiche, finit avec 0",
              "2  head birini okur, yazar, 0 ile biter"),
             ("y3", "3  yes schreibt weiter, niemand liest", "3  yes keeps writing, nobody reads", "3  yes sigue escribiendo, nadie lee",
              "3  yes 继续写入，无人读取", "3  yes continue d'écrire, personne ne lit", "3  yes yazmaya devam eder, okuyan yok"),
             ("y4", "4  Nachricht 13 beendet yes: 141", "4  message 13 ends yes: 141", "4  el mensaje 13 termina yes: 141",
              "4  消息 13 终止 yes：141", "4  le message 13 termine yes : 141", "4  mesaj 13 yes'i sonlandırır: 141")]
    L = [text(s, T(s, *kt), (-3.35, -0.55 - 0.28 * i), FM, "left", DUNKEL) for i, kt in enumerate(liste)]
    ps = s.box("", (1.85, -1.2), breite=2.5, hoehe=0.48, form="round", farbe=DUNKEL, fuellung=WEISS, dicke=2.5)
    ps_t = tt(s, "PIPESTATUS: 141 0", 1.85, -1.2, 0.16, SCHWARZ, "m")
    schritt(s, WACHS([yes[0], head[0], rohr_k], 0.6), EIN([yes[1], head[1], l_pipe], 0.6))
    s.pause(0.5)
    schritt(s, EIN(L[0], 0.4), EIN(t[0], 0.2))
    schritt(s, VER(t[0], 0.45 - xs, 0, 0.5), EIN(t[1], 0.2))
    schritt(s, VER(t[1], 0.15 - xs, 0, 0.45), EIN(t[2], 0.2))
    schritt(s, VER(t[2], -0.15 - xs, 0, 0.4))
    s.pause(0.5)
    schritt(s, EIN(L[1], 0.4), VER(t[0], 0.55, 0, 0.5))
    schritt(s, AUS(t[0], 0.3), ZEICHNE(a_out, 0.4), WACHS(schirm, 0.4))
    schritt(s, EIN(aus_y, 0.4))
    schritt(s, AUS(head, 0.5), EIN([hg, hg_n], 0.5), WACHS(z0[0], 0.5), EIN(z0[1], 0.5))
    schritt(s, ZEICHNE(wand, 0.4), AUS([t[1], t[2]], 0.4))
    s.pause(0.5)
    schritt(s, EIN(L[2], 0.4), EIN(t[3], 0.2))
    schritt(s, VER(t[3], 0.35 - xs, 0, 0.6))
    schritt(s, ZEICHNE(blitz, 0.3), EIN(l_n13, 0.3), AUS(t[3], 0.3))
    s.pause(0.4)
    schritt(s, EIN(L[3], 0.4), AUS(yes, 0.5), EIN([yg, yg_n], 0.5), WACHS(z141[0], 0.5), EIN([z141[1], l_141], 0.5))
    s.pause(0.5)
    schritt(s, WACHS(ps, 0.5), EIN(ps_t, 0.5))
    s.speichern()


# ================================================================== Abschnitt 7: Aus einer Ausgabe Argumente machen
def k4stromargument():
    """Zwei Eingänge eines Prozesses: Argumente (beim Start) und Standardeingabe (Strom). echo probe2.txt | rm: rm liest nicht, die
    Argumente sind leer → missing operand. echo einkauf.txt | wc -l: wc zählt den Namen als eine Zeile, die Datei bleibt unberührt."""
    s = Szene("linux/k4stromargument")
    arg_t = T(s, "arg", "Argumente", "arguments", "argumentos", "参数", "arguments", "argümanlar")
    sin_t = w_sin(s)

    def reihe(y, cmd, name, prog, opt):
        r = {"y": y}
        r["cmd"] = tt(s, cmd, -3.4, y + 0.85, 0.15)
        r["echo"] = prozess(s, (-2.85, y), 0.9, 0.5, "echo", 0.15)
        r["pipe"] = rohr(s, (-2.4, y), (-0.25, y), C0)
        r["l_pipe"] = text(s, sin_t, (-1.35, y - 0.22), FX, "center", C0)
        r["p"] = prozess(s, (0.4, y), 1.2, 0.55, prog, 0.16)
        r["slot"] = s.box("", (0.4, y + 0.52), breite=1.3, hoehe=0.28, form="rect", farbe=GRAU, fuellung=WEISS, dicke=1.5, dash=DASH)
        r["l_slot"] = text(s, arg_t, (-0.35, y + 0.52), FX, "right", GRAU)
        r["opt"] = tt(s, opt, 0.4, y + 0.52, 0.15, SCHWARZ, "m") if opt else \
            text(s, T(s, "leer", "leer", "empty", "vacía", "空", "vide", "boş"), (0.4, y + 0.52), FX, "center", GRAU)
        r["tok"] = text(s, name, (-1.85, y + 0.17), FM, "center", C0)
        return r

    A = reihe(0.85, "$ echo probe2.txt | rm", "probe2.txt", "rm", "")
    B = reihe(-0.95, "$ echo einkauf.txt | wc -l", "einkauf.txt", "wc", "-l")
    sperre = linie(s, (-0.33, 0.85 - 0.2), (-0.33, 0.85 + 0.2), ROT, 6)
    l_sperre = text(s, T(s, "liestnicht", "liest nicht", "does not read", "no lee", "不读取", "ne lit pas", "okumaz"), (-0.33, 0.85 - 0.4),
                    FX, "center", ROT)
    out_rm = text(s, "rm: missing operand", (1.15, 0.85), FM, "left", ROT)
    a_wc = rohr(s, (1.0, -0.95), (1.35, -0.95), C1)
    eins = tt(s, "1", 1.55, -0.95, 0.19, SCHWARZ, "m")
    l_eins = text(s, T(s, "einezeile", "eine Zeile\nDaten", "one line\nof data", "una línea\nde datos", "一行\n数据", "une ligne\nde données",
                       "bir satır\nveri"), (1.55, -1.38), FX, "center", GRAU)
    doc = dokument(s, (2.75, -0.95), 1.25, 0.75)
    d_t = [text(s, "einkauf.txt", (2.75, -0.82), FX), text(s, T(s, "fuenfz", "5 Zeilen", "5 lines", "5 líneas", "5 行", "5 lignes",
                                                              "5 satır"), (2.75, -1.08), FX, "center", GRAU)]
    l_doc = text(s, T(s, "unberuehrt", "unberührt", "untouched", "intacto", "未被触及", "intact", "dokunulmadı"), (2.75, -1.5), FX,
                 "center", GRUEN)
    for r in (A, B):
        if r is B:
            s.pause(0.6)
        schritt(s, EIN(r["cmd"], 0.4))
        schritt(s, WACHS([r["echo"][0], r["p"][0], r["slot"]], 0.6), EIN([r["echo"][1], r["p"][1], r["l_slot"], r["opt"], r["l_pipe"]], 0.6),
                ZEICHNE(r["pipe"], 0.6))
        if r is A:
            schritt(s, ZEICHNE(sperre, 0.4), EIN(l_sperre, 0.4))
        schritt(s, EIN(r["tok"], 0.3))
        if r is A:
            schritt(s, VER(r["tok"], 1.05, 0, 0.8))
            schritt(s, EIN(out_rm, 0.5), BETONE(r["opt"], 0.6))
        else:
            schritt(s, VER(r["tok"], 2.05, -0.17, 0.8))
            schritt(s, AUS(r["tok"], 0.3))
            schritt(s, ZEICHNE(a_wc, 0.4), EIN([eins, l_eins], 0.5))
            schritt(s, WACHS(doc, 0.5), EIN(d_t + [l_doc], 0.5))
    s.speichern()


def k4xargs():
    """echo einkauf.txt obst.txt | xargs wc -l: Der Strom fließt in xargs, xargs zerlegt ihn in zwei Wortkarten und hängt sie an
    wc -l an; der neue Prozess wc -l einkauf.txt obst.txt schreibt 5, 7, 12 total."""
    s = Szene("linux/k4xargs")
    term = term_kasten(s, (0, 1.88), 3.6, 0.4)
    cmd = tt(s, "$ echo einkauf.txt obst.txt | xargs wc -l", 0, 1.88, 0.15, SCHWARZ, "m")
    y = 1.1
    strom = karte(s, -2.3, y, "einkauf.txt obst.txt", 1.9, BLAU, BLAU_HELL, FM)
    strom_k = karte(s, -2.3, y, "einkauf.txt obst.txt", 1.9, BLAU, BLAU_HELL, FM)
    l_strom = text(s, w_sin(s), (-2.3, y - 0.32), FX, "center", C0)
    pipe = rohr(s, (-1.3, y), (-0.05, y), C0)
    xa = prozess(s, (0.55, y), 1.1, 0.5, "xargs", 0.16)
    l_zer = text(s, T(s, "zerlegt", "zerlegt in Wörter", "splits into words", "separa en palabras", "切分成单词", "découpe en mots",
                      "sözcüklere böler"), (1.25, y), FX, "left", GRAU)
    w1 = karte(s, 0.05, 0.45, "einkauf.txt", 1.0, ORANGE, ORANGE_HELL, FX)
    w2 = karte(s, 1.1, 0.45, "obst.txt", 0.8, ORANGE, ORANGE_HELL, FX)
    w1k = karte(s, 0.05, 0.45, "einkauf.txt", 1.0, ORANGE, ORANGE_HELL, FX)
    w2k = karte(s, 1.1, 0.45, "obst.txt", 0.8, ORANGE, ORANGE_HELL, FX)
    neu =s.box("", (-0.7, -0.35), breite=3.2, hoehe=0.55, form="round", farbe=BLAU, fuellung=BLAU_HELL, dicke=2.5)
    wc_t = tt(s, "wc -l", -2.15, -0.35, 0.17)
    l_neu = text(s, T(s, "neuproz", "neuer Prozess", "new process", "proceso nuevo", "新进程", "nouveau processus", "yeni süreç"),
                 (-2.3, 0.05), FX, "left", BLAU)
    r1 = rohr(s, (-0.7, -0.625), (-0.7, -0.83), C1)
    t2 = term_kasten(s, (-0.7, -1.25), 2.6, 0.84)
    aus = (ttz(s, " 5 einkauf.txt", -1.85, -1.0, 0.16) + ttz(s, " 7 obst.txt", -1.85, -1.25, 0.16)
           + ttz(s, "12 total", -1.85, -1.5, 0.16))
    schritt(s, WACHS(term, 0.4), EIN(cmd, 0.4))
    schritt(s, WACHS(strom[0], 0.5), EIN([strom[1], l_strom], 0.5))
    schritt(s, ZEICHNE(pipe, 0.5), WACHS(xa[0], 0.5), EIN(xa[1], 0.5))
    s.pause(0.5)
    schritt(s, EIN(strom_k, 0.2))
    schritt(s, *VERS(strom_k, 2.85, 0, 0.7))
    schritt(s, AUS(strom_k, 0.3), WACHS([w1[0], w2[0]], 0.5), EIN([w1[1], w2[1], l_zer], 0.5))
    s.pause(0.6)
    schritt(s, WACHS(neu, 0.5), EIN([wc_t, l_neu], 0.5))
    schritt(s, EIN(w1k + w2k, 0.15))
    schritt(s, *VERS(w1k, -1.05, -0.8, 0.8), *VERS(w2k, -1.1, -0.8, 0.8))
    s.pause(0.6)
    schritt(s, ZEICHNE(r1, 0.4), WACHS(t2, 0.5))
    schritt(s, EIN(aus, 0.5))
    s.speichern()


def k4portionen():
    """Drei Wörter Apfel, Birne, Kiwi: ohne -n ein Aufruf echo Obst: Apfel Birne Kiwi, mit -n 1 drei Aufrufe mit je einem Wort."""
    s = Szene("linux/k4portionen")
    woerter = ["Apfel", "Birne", "Kiwi"]
    qx, qy = [-0.85, 0.15, 1.15], 1.7
    l_q = text(s, T(s, "woerter", "Wörter in der Eingabe:", "words in the input:", "palabras de la entrada:", "输入中的单词：",
                    "mots de l'entrée :", "girdideki sözcükler:"), (-1.45, qy), FX, "right", GRAU)

    def k(x, y, w):
        return karte(s, x, y, w, 0.85, ORANGE, ORANGE_HELL, FM)

    quelle = [k(x, qy, w) for x, w in zip(qx, woerter)]
    y1 = 0.95
    l1 = [text(s, T(s, "ohne", "ohne -n", "without -n", "sin -n", "不加 -n", "sans -n", "-n olmadan"), (-3.35, y1 + 0.1), FM, "left",
               DUNKEL),
          text(s, T(s, "einaufruf", "ein Aufruf", "one call", "una llamada", "一次调用", "un appel", "tek çağrı"), (-3.35, y1 - 0.17), FX,
               "left", GRAU)]
    box1 = s.box("", (0.55, y1), breite=4.6, hoehe=0.46, form="round", farbe=BLAU, fuellung=BLAU_HELL, dicke=2.5)
    e1 = tt(s, "echo Obst:", -1.6, y1, 0.16)
    s1 = [-0.2, 0.75, 1.7]
    kop1 = [k(x, qy, w) for x, w in zip(qx, woerter)]
    y2 = [0.15, -0.5, -1.15]
    l2 = [text(s, T(s, "mit", "mit -n 1", "with -n 1", "con -n 1", "加 -n 1", "avec -n 1", "-n 1 ile"), (-3.35, y2[0] + 0.1), FM, "left",
               DUNKEL),
          text(s, T(s, "drei", "drei Aufrufe\nnacheinander", "three calls,\none after another", "tres llamadas,\nuna tras otra",
                    "三次调用，\n依次进行", "trois appels\nl'un après l'autre", "art arda\nüç çağrı"), (-3.35, y2[0] - 0.27), FX, "left",
               GRAU)]
    box2 = [s.box("", (-0.425, yy), breite=2.65, hoehe=0.46, form="round", farbe=BLAU, fuellung=BLAU_HELL, dicke=2.5) for yy in y2]
    e2 = [tt(s, "echo Obst:", -1.6, yy, 0.16) for yy in y2]
    kop2 = [k(x, qy, w) for x, w in zip(qx, woerter)]
    schritt(s, EIN(l_q, 0.5), WACHS([q[0] for q in quelle], 0.5), EIN([q[1] for q in quelle], 0.5))
    s.pause(0.6)
    schritt(s, EIN(l1, 0.5), WACHS(box1, 0.5), EIN(e1, 0.5))
    schritt(s, EIN(kop1, 0.2))
    schritt(s, *[t for i in range(3) for t in VERS(kop1[i], s1[i] - qx[i], y1 - qy, 0.8)])
    s.pause(0.6)
    schritt(s, EIN(l2, 0.5))
    for i in range(3):
        schritt(s, WACHS(box2[i], 0.4), EIN([e2[i]] + kop2[i], 0.4))
        schritt(s, *VERS(kop2[i], -0.2 - qx[i], y2[i] - qy, 0.6))
    s.speichern()


def k4leerzeichen():
    """Oben trennt xargs an Leerzeichen und Zeilenenden: aus ./mein foto.jpg werden ./mein und foto.jpg (rot); unten trennt xargs -0
    nur an den Nullbytes: zwei ganze Namen (grün)."""
    s = Szene("linux/k4leerzeichen")
    e = 0.18
    c = cw(e)
    x0 = -2.0

    def strom(y, null):
        r = {}
        n1 = tt(s, "./mein foto.jpg", x0, y, e)
        xa = x0 + 15 * c + 0.05
        w = 0.38 if null else 0.3
        sep1 = karte(s, xa + w / 2, y, r"\backslash0", 0.36, ORANGE, ORANGE_HELL, FM, ORANGE, h=0.28) if null else \
            [zeilenende(s, xa + w / 2, y, 0.16)]
        x2 = xa + w + 0.05
        n2 = tt(s, "./urlaub.jpg", x2, y, e)
        xb = x2 + 12 * c + 0.05
        sep2 = karte(s, xb + w / 2, y, r"\backslash0", 0.36, ORANGE, ORANGE_HELL, FM, ORANGE, h=0.28) if null else \
            [zeilenende(s, xb + w / 2, y, 0.16)]
        r["bg"] = s.box("", ((x0 - 0.1 + xb + w + 0.1) / 2, y), breite=xb + w + 0.2 - x0, hoehe=0.42, form="rect", farbe=GRAU,
                        fuellung=TERM, dicke=1.5)
        r["inhalt"] = [n1, n2] + sep1 + sep2
        schnitte = [xa + w / 2, xb + w / 2] if null else [x0 + 6.5 * c, xa + w / 2, xb + w / 2]
        f = GRUEN if null else ROT
        r["cuts"] = [linie(s, (x, y + a), (x, y + b), f, 3.5) for x in schnitte for a, b in ((0.16, 0.32), (-0.16, -0.32))]
        r["x2"] = x2
        return r

    def wk(x, y, t, ok):
        b = 0.075 * len(t) + 0.16
        return karte(s, x, y, t, b, GRUEN if ok else ROT, GRUEN_HELL if ok else ROT_HELL, FM, GRUEN if ok else ROT, h=0.3)

    yo, yu = 1.45, -0.35
    l_o = text(s, T(s, "ohne0", "xargs trennt an Leerzeichen und Zeilenenden", "xargs splits at spaces and line ends",
                    "xargs separa en espacios y finales de línea", "xargs 在空格和换行处切分", "xargs coupe aux espaces et aux fins de ligne",
                    "xargs boşluklarda ve satır sonlarında böler"), (-3.35, yo + 0.42), FM, "left", DUNKEL)
    l_u = text(s, T(s, "mit0", "xargs -0 trennt nur am Nullbyte", "xargs -0 splits only at the null byte",
                    "xargs -0 separa solo en el byte nulo", "xargs -0 只在空字节处切分", "xargs -0 coupe seulement à l'octet nul",
                    "xargs -0 yalnızca boş baytta böler"), (-3.35, yu + 0.42), FM, "left", DUNKEL)
    O, U = strom(yo, False), strom(yu, True)
    ko = [wk(x0 + 2.5 * c, yo - 0.6, "./mein", False), wk(x0 + 11.5 * c, yo - 0.6, "foto.jpg", False),
          wk(O["x2"] + 6 * c, yo - 0.6, "./urlaub.jpg", True)]
    ku = [wk(x0 + 7.5 * c, yu - 0.6, "./mein foto.jpg", True), wk(U["x2"] + 6 * c, yu - 0.6, "./urlaub.jpg", True)]
    l_rot = text(s, T(s, "gibtsnicht", "zwei Namen, die es nicht gibt", "two names that do not exist", "dos nombres que no existen",
                      "两个不存在的名称", "deux noms qui n'existent pas", "var olmayan iki ad"), (x0 + 7 * c, yo - 0.92), FX, "center", ROT)
    l_gr = text(s, T(s, "ganz", "beide Namen bleiben ganz", "both names stay whole", "ambos nombres quedan enteros", "两个名称都保持完整",
                     "les deux noms restent entiers", "iki ad da bütün kalır"), (0.0, yu - 0.92), FX, "center", GRUEN)
    for R, karten, lab, l_kopf in ((O, ko, l_rot, l_o), (U, ku, l_gr, l_u)):
        if R is U:
            s.pause(0.6)
        schritt(s, EIN(l_kopf, 0.5), WACHS(R["bg"], 0.5), EIN(R["inhalt"], 0.5))
        schritt(s, ZEICHNE(R["cuts"], 0.6))
        schritt(s, WACHS([k[0] for k in karten], 0.6), EIN([k[1] for k in karten], 0.6))
        schritt(s, EIN(lab, 0.5))
    s.speichern()


SZENEN = (k4prozess, k4strom, k4cateingabe, k4rohre, k4deskriptoren,
          k4umleitung, k4anhaengen, k4zweidateien, k4reihenfolge, k4kuerzung,
          k4eingabe, k4heredoc, k4herestring,
          k4pipe, k4pipefehler, k4filter, k4fliessband, k4tee,
          k4exitstatus, k4grepstatus, k4nummern,
          k4weichen, k4kette, k4pipestatus, k4yeshead,
          k4stromargument, k4xargs, k4portionen, k4leerzeichen)

if __name__ == "__main__":
    for f in SZENEN:
        f()
