"""Linux und Kommandozeile, Kapitel 2 „Die Shell: erste Befehle“ (C:\\Bücher\\EtUndSo\\Linux\\Arbeitshefte\\kap2_stufen.tex,
kap2_stufen_b.tex): Abbildungen, alle animiert (notizen/animationen.md §5).

Szenenname linux/k2<name> = \\label{fig:k2<name>} im Heft. Stil wie tools/szenen/linux_teil1.py (Kästen, Pfeile, T(...) in sechs
Sprachen); Terminal-Inhalte (Befehle, Ausgaben, Eingabeaufforderungen) sind in allen Sprachen gleich und stehen als
Schreibmaschinenschrift in s.formel (\\texttt). Damit alle Zeilen gleich groß sind und Zeichen genau untereinander stehen, trägt
jede Zeile vorn und hinten eine unsichtbare Stütze (\\rule, 0,001 em breit, von -0,25 em bis 0,75 em): Die Formelhöhe ist dann
genau 1 em, ein Zeichen ist 0,525 em breit (tt, sp, msp).
Die Koordinaten sind schon schmal (x zwischen -3,45 und 3,45): jedes Bild höchstens 548 px breit, keine Stauchung nötig.
Bauen:  python tools/szenen/linux_teil2.py
Export: python tools/export_szenen.py <alle Namen aus SZENEN> --animiert
Rechenbild: nur k2df (Division und Aufrunden, s.formel zeilenweise). Die Zahlen prüft rechnung_kap2.py im Heftordner.
"""
import math
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from szenen_lib import *  # noqa: E402,F403

FS, FK, FM = 22, 20, 18           # Beschriftung, klein, sehr klein (Schrift in der Artikelspalte: 0,55 px je Einheit)
EM = 0.19                         # Höhe einer Terminalzeile (1 em) in Szeneneinheiten
WEISS = "#ffffff"
BLAU_HELL = "#e3eefb"
ORANGE_HELL = "#fdece3"
GRUEN_HELL = "#e6f3ea"
GRAU_HELL = "#efefef"
TERM = "#f6f6f4"
DUNKEL = "#333333"


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
    """Ein Schritt: teile = (art, ids, dauer[, werte]); alles darin läuft gleichzeitig (ohne verschachteltes gleichzeitig)."""
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


def FORM(i, zu, d=0.9, passend=True):
    return ("TransformMatchingTex" if passend else "Transform", i, d, {"to": zu})


def LAUF(i, weg, d=0.8):
    return ("MoveAlongPath", i, d, {"path": weg})


# ------------------------------------------------------------------ Zeichnen
def text(s, t, pos, groesse=FK, ausr="center", farbe=SCHWARZ):
    return s.text(None, t, pos, groesse, ausr, farbe)


def kasten(s, mitte, b, h, t="", groesse=FK, fuellung=WEISS, form="round", farbe=SCHWARZ, textfarbe=SCHWARZ, dicke=2.5,
           dash="", ty=None, deckung=1.0):
    """Kasten mit zentriertem Text; Ergebnis [Kasten, Text] (ohne Text nur [Kasten]). Ein Kasten, der erst erscheint, wenn
    schon Text an seiner Stelle steht, liegt darüber (Reihenfolge des Erscheinens): dann deckung < 1."""
    k = s.box("", mitte, breite=b, hoehe=h, form=form, farbe=farbe, fuellung=fuellung, deckung=deckung, dicke=dicke, dash=dash)
    if not t:
        return [k]
    return [k, s.text(None, t, (mitte[0], mitte[1] if ty is None else ty), groesse, "center", textfarbe)]


def flaeche(s, x0, y0, x1, y1, fuellung, farbe=None, dicke=0, dash="", deckung=1.0):
    return s.box("", ((x0 + x1) / 2, (y0 + y1) / 2), breite=x1 - x0, hoehe=y1 - y0, form="rect", farbe=farbe or fuellung,
                 fuellung=fuellung, deckung=deckung, dicke=dicke, dash=dash)


def schleier(s, mitte, b, h, deckung=0.7):
    """Weißer, halb durchsichtiger Schleier: graut das Darunterliegende aus."""
    return s.box("", mitte, breite=b, hoehe=h, form="rect", farbe=WEISS, fuellung=WEISS, deckung=deckung, dicke=0)


def mark(s, xa, xb, y, h, farbe, deckung=0.25):
    """Farbige Hinterlegung (vor dem Text anlegen, damit sie dahinter liegt)."""
    return s.box("", ((xa + xb) / 2, y), breite=xb - xa, hoehe=h, form="rect", farbe=farbe, fuellung=farbe, deckung=deckung,
                 dicke=0)


def pf(s, a, b, knick="none", farbe=SCHWARZ, dash="", doppelt=False, dicke=2.5, spitze=0.11):
    return s.pfeil(a, b, knick=knick, farbe=farbe, dicke=dicke, spitze=spitze, dash=dash, doppelt=doppelt)


def linie(s, a, b, farbe=SCHWARZ, dicke=2.5, dash=""):
    return s.linie(None, a, b, farbe=farbe, dicke=dicke, dash=dash)


def klammer(s, xa, xb, y, unten=True, farbe=GRAU, t=0.07, dicke=2.5):
    """Eckige Klammer unter (unten=True, Schenkel nach oben) oder über einem Textstück."""
    d = t if unten else -t
    return [linie(s, (xa, y + d), (xa, y), farbe, dicke), linie(s, (xa, y), (xb, y), farbe, dicke),
            linie(s, (xb, y), (xb, y + d), farbe, dicke)]


def bogen(s, xa, xb, y, h, farbe=GRAU, dicke=2.5):
    xm, hw = (xa + xb) / 2, (xb - xa) / 2
    return s.weg(None, f"{xm:.4f}-{hw:.4f}*cos(3.141593*t)", f"{y:.4f}+{h:.4f}*sin(3.141593*t)", 0, 1, farbe=farbe,
                 dicke=dicke, n=41)


def haken(s, x, y, g=0.13, farbe=GRUEN):
    return [linie(s, (x - g, y), (x - 0.25 * g, y - 0.8 * g), farbe, 5),
            linie(s, (x - 0.25 * g, y - 0.8 * g), (x + 1.1 * g, y + g), farbe, 5)]


def taste(s, mitte, t, b=0.62, h=0.34):
    return kasten(s, mitte, b, h, t, FM, fuellung="#f1f1f1", farbe=GRAU, dicke=2)


# ------------------------------------------------------------------ Schreibmaschinenschrift
_STUETZE = r"\rule[-0.25em]{0.001em}{1em}"


def _tex(z):
    z = z.replace("\\", "").replace("$", r"\$").replace("{", r"\{").replace("}", r"\}")
    # Die Tilde der Schreibmaschinenschrift sitzt in MathJax auf Höhe der Großbuchstaben; 0,25 em tiefer steht sie wie im
    # Terminal in der Mitte (Breite bleibt 0,525 em).
    teile = [r"\texttt{" + t + "}" if t else "" for t in z.split("~")]
    return _STUETZE + r"\lower{0.25em}{\texttt{~}}".join(teile) + _STUETZE


def cw(em=EM):
    """Breite eines Zeichens."""
    return 0.525 * em


def sp(x0, i, em=EM):
    """Linke Kante der Spalte i einer Zeile, die bei x0 beginnt."""
    return x0 + i * cw(em)


def msp(x0, a, b, em=EM):
    """Mitte der Spalten a bis b (einschließlich)."""
    return x0 + (a + b + 1) / 2 * cw(em)


def tt(s, zeile, x, y, em=EM, farbe=SCHWARZ, anker="l"):
    """Eine Terminalzeile; anker l: x = linke Kante, m: x = Mitte, r: x = rechte Kante. Leerzeichen vorn verschieben."""
    vorn = len(zeile) - len(zeile.lstrip(" "))
    zeile = zeile.strip(" ")
    n, c = len(zeile), cw(em)
    cx = x + (vorn + n / 2) * c if anker == "l" else (x - n / 2 * c if anker == "r" else x)
    return s.formel(_tex(zeile), mitte=(round(cx, 4), round(y, 4)), hoehe=em, farbe=farbe)


# ================================================================== Abschnitt 1: Terminal und Shell
def k2schichten():
    """Tastatur → Terminalemulator ↔ Pseudoterminal (Kernel) ↔ Shell → Systemaufruf → Kernel → Hardware; ein Zeichen wandert."""
    s = Szene("linux/k2schichten")
    baender = [flaeche(s, -3.4, 0.45, 3.4, 1.95, GRUEN_HELL), flaeche(s, -3.4, -0.8, 3.4, 0.35, BLAU_HELL),
               flaeche(s, -3.4, -1.85, 3.4, -0.9, GRAU_HELL)]
    namen = [text(s, T(s, "prog", "Programme", "programs", "programas", "程序", "programmes", "programlar"), (-3.3, 1.78), FM,
                  "left", GRUEN),
             text(s, T(s, "kern", "Kernel", "kernel", "núcleo", "内核", "noyau", "çekirdek"), (-3.3, 0.2), FM, "left", BLAU),
             text(s, T(s, "hw", "Hardware", "hardware", "hardware", "硬件", "matériel", "donanım"), (-3.3, -1.02), FM, "left",
                  GRAU)]
    emu = kasten(s, (-1.75, 1.05), 2.5, 1.0, form="rect")
    emu_t = text(s, T(s, "emu", "Terminalemulator (Fenster)", "terminal emulator (window)", "emulador de terminal (ventana)",
                      "终端模拟器（窗口）", "émulateur de terminal (fenêtre)", "uçbirim öykünücüsü (pencere)"), (-1.75, 1.38), FM)
    sh = kasten(s, (2.05, 1.05), 1.9, 1.0, T(s, "shell", "Shell\n(bash)", "shell\n(bash)", "shell\n(bash)", "Shell\n（bash）",
                                             "shell\n(bash)", "kabuk\n(bash)"), FS)
    pty = kasten(s, (0.3, -0.2), 1.7, 0.5, T(s, "pty", "Pseudoterminal", "pseudoterminal", "pseudoterminal", "伪终端",
                                             "pseudo-terminal", "sözde uçbirim"), FM, ORANGE_HELL, form="rect")
    dienst = kasten(s, (2.3, -0.2), 1.7, 0.5, T(s, "dienste", "Dienste des Kernels", "kernel services", "servicios del núcleo",
                                                "内核服务", "services du noyau", "çekirdek hizmetleri"), FM, form="rect")
    tast = kasten(s, (-2.45, -1.4), 1.15, 0.42, T(s, "tast", "Tastatur", "keyboard", "teclado", "键盘", "clavier", "klavye"), FM,
                  form="rect")
    bild = kasten(s, (-1.05, -1.4), 1.3, 0.42, T(s, "bild", "Bildschirm", "screen", "pantalla", "屏幕", "écran", "ekran"), FM,
                  form="rect")
    cpu = kasten(s, (2.3, -1.4), 1.9, 0.42, T(s, "cpu", "Prozessor, SSD, …", "processor, SSD, …", "procesador, SSD, …",
                                              "处理器、SSD……", "processeur, SSD, …", "işlemci, SSD, …"), FM, form="rect")
    a1 = pf(s, (-2.45, -1.19), (-2.45, 0.55))
    a2 = pf(s, (-1.05, 0.55), (-1.05, -1.19))
    a3 = pf(s, (-0.5, 0.8), (0.0, 0.05), knick="hv", doppelt=True)
    a4 = pf(s, (0.6, 0.05), (1.1, 0.8), knick="vh", doppelt=True)
    a5 = pf(s, (2.3, 0.55), (2.3, 0.05))
    a6 = pf(s, (2.3, -0.45), (2.3, -1.19))
    l5 = text(s, T(s, "sysauf", "Systemaufruf", "system call", "llamada al sistema", "系统调用", "appel système",
                   "sistem çağrısı"), (2.2, 0.38), FM, "right")
    e, x0 = 0.14, -2.93
    w_pr = tt(s, "$", x0, 1.08, e)
    w_u = tt(s, "u", sp(x0, 2, e), 1.08, e)
    w_rest = tt(s, "name -r", sp(x0, 3, e), 1.08, e)
    w_ant = tt(s, "6.6.87.2-microsoft-standard-WSL2", x0, 0.8, e)
    r_u = tt(s, "u", -2.45, -0.95, 0.2, ORANGE, "m")
    r_ant = tt(s, "6.6.87.2-...", 0.3, 0.2, e, ORANGE, "m")
    schritt(s, EIN(baender + namen, 0.6))
    schritt(s, WACHS([emu, sh[0], pty[0], dienst[0], tast[0], bild[0], cpu[0]], 0.7),
            EIN([emu_t, sh[1], pty[1], dienst[1], tast[1], bild[1], cpu[1]], 0.7))
    schritt(s, ZEICHNE([a1, a2, a3, a4, a5, a6], 0.9), EIN(w_pr, 0.9))
    s.pause(0.6)
    schritt(s, EIN(r_u, 0.3))
    schritt(s, ZU(r_u, -2.45, 0.42, 0.5))
    schritt(s, ZU(r_u, 0.0, 0.2, 0.6))
    schritt(s, ZU(r_u, 0.95, 0.62, 0.5))
    schritt(s, ZU(r_u, 0.0, 0.2, 0.45))
    schritt(s, ZU(r_u, sp(x0, 2, e) + cw(e) / 2, 1.08, 0.6))
    schritt(s, AUS(r_u, 0.3), EIN(w_u, 0.3))
    s.pause(0.6)
    schritt(s, EIN(w_rest, 0.6))
    schritt(s, BETONE([a3, a4], 0.7))
    schritt(s, BETONE(a5, 0.6), EIN(l5, 0.6))
    schritt(s, BETONE(a6, 0.6))
    s.pause(0.6)
    schritt(s, EIN(r_ant, 0.3))
    schritt(s, ZU(r_ant, x0 + 16 * cw(e), 0.8, 0.7))
    schritt(s, AUS(r_ant, 0.3), EIN(w_ant, 0.3))
    s.speichern()


def k2schleife():
    """Kreislauf der Shell mit fünf Stationen; ein Punkt läuft einmal herum, an jeder Station erscheint das Beispiel uname -r."""
    s = Szene("linux/k2schleife")
    cx, cy, r = 0.0, -0.25, 0.95
    w = [90 - 72 * i for i in range(5)]
    boegen = []
    for i in range(5):
        a0, da = math.radians(w[i]), math.radians(72)
        boegen.append(s.weg(None, f"{cx}+{r}*cos({a0:.6f}-{da:.6f}*t)", f"{cy}+{r}*sin({a0:.6f}-{da:.6f}*t)", 0, 1, farbe=GRAU,
                            dicke=3, pfeile="0.55", n=41))
    mitte = text(s, T(s, "shell", "Shell", "shell", "shell", "Shell", "shell", "kabuk"), (cx, cy), FS, "center", GRAU)
    punkte = [s.punkt(None, cx + r * math.cos(math.radians(a)), cy + r * math.sin(math.radians(a)), farbe=SCHWARZ, r=0.06)
              for a in w]
    labels = [
        text(s, T(s, "st1", "1  Eingabeaufforderung zeigen", "1  show the prompt", "1  mostrar el indicador", "1  显示提示符",
                  "1  afficher l’invite", "1  istemi göster"), (0.0, 1.38), FK),
        text(s, T(s, "st2", "2  Zeile lesen", "2  read a line", "2  leer una línea", "2  读取一行", "2  lire une ligne",
                  "2  satırı oku"), (1.08, 0.13), FK, "left"),
        text(s, T(s, "st3", "3  Befehl suchen", "3  find the command", "3  buscar el comando", "3  查找命令",
                  "3  chercher la commande", "3  komutu ara"), (0.72, -1.0), FK, "left"),
        text(s, T(s, "st4", "4  ausführen (lassen)", "4  run it (or have it run)", "4  ejecutarlo (o hacerlo ejecutar)",
                  "4  执行（或让其执行）", "4  l’exécuter (ou le faire exécuter)", "4  çalıştır (ya da çalıştırt)"),
             (-0.72, -1.0), FK, "right"),
        text(s, T(s, "st5", "5  auf das Ende warten", "5  wait for the end", "5  esperar a que termine", "5  等待结束",
                  "5  attendre la fin", "5  bitmesini bekle"), (-1.08, 0.13), FK, "right")]
    bsp = [tt(s, "student@labor:~$", 0.0, 1.08, 0.15, DUNKEL, "m"),
           tt(s, "uname -r", 1.08, -0.12, 0.15, DUNKEL),
           tt(s, "/usr/bin/uname", 0.72, -1.26, 0.15, DUNKEL),
           text(s, T(s, "bsp4", "uname läuft", "uname runs", "uname se ejecuta", "uname 运行", "uname s’exécute",
                     "uname çalışır"), (-0.72, -1.27), FM, "right", GRAU),
           text(s, T(s, "bsp5", "bis uname endet", "until uname ends", "hasta que uname termina", "直到 uname 结束",
                     "jusqu’à la fin de uname", "uname bitene kadar"), (-1.08, -0.13), FM, "right", GRAU)]
    lauf = s.punkt(None, 0.0, cy + r, farbe=ORANGE, r=0.09)
    schritt(s, ZEICHNE(boegen, 1.2), EIN(mitte, 1.2))
    schritt(s, EIN(punkte + labels, 0.6))
    s.pause(0.6)
    schritt(s, EIN([lauf, bsp[0]], 0.5))
    for i in range(4):
        schritt(s, LAUF(lauf, boegen[i], 0.8))
        schritt(s, EIN(bsp[i + 1], 0.5))
    schritt(s, LAUF(lauf, boegen[4], 0.8))
    schritt(s, AUS(lauf, 0.4))
    s.speichern()


def k2prompt():
    """student@labor:~$ zerlegt; darunter root@labor:~# mit rotem #."""
    s = Szene("linux/k2prompt")
    e, x0, y = 0.32, -1.345, 0.85
    zeile = tt(s, "student@labor:~$", x0, y, e)
    k_user = klammer(s, sp(x0, 0, e) + 0.03, sp(x0, 7, e) - 0.03, 0.6)
    t_user = text(s, T(s, "user", "Benutzer", "user", "usuario", "用户", "utilisateur", "kullanıcı"), (msp(x0, 0, 6, e), 0.42), FK)
    k_host = klammer(s, sp(x0, 8, e) + 0.03, sp(x0, 13, e) - 0.03, 0.6)
    t_host = text(s, T(s, "host", "Rechner", "computer", "equipo", "计算机", "machine", "bilgisayar"), (msp(x0, 8, 12, e), 0.42),
                  FK)
    k_dir = klammer(s, sp(x0, 14, e) + 0.02, sp(x0, 15, e) - 0.02, 1.12, unten=False)
    t_dir = text(s, T(s, "dir", "aktueller Ordner\n~ = /home/student", "current folder\n~ = /home/student",
                      "carpeta actual\n~ = /home/student", "当前文件夹\n~ = /home/student", "dossier courant\n~ = /home/student",
                      "geçerli klasör\n~ = /home/student"), (msp(x0, 14, 14, e), 1.42), FM)
    k_end = klammer(s, sp(x0, 15, e) + 0.02, sp(x0, 16, e) - 0.02, 0.6)
    t_end = text(s, T(s, "ende", "Schlusszeichen:\ngewöhnlicher Benutzer", "end character:\nordinary user",
                      "carácter final:\nusuario normal", "结尾符号：\n普通用户", "caractère final :\nutilisateur ordinaire",
                      "son karakter:\nsıradan kullanıcı"), (sp(x0, 15, e), 0.36), FM, "left")
    l_stud = text(s, T(s, "konto1", "Konto student:", "account student:", "cuenta student:", "student 账户：", "compte student :",
                       "student hesabı:"), (-1.5, y), FK, "right", GRAU)
    root = tt(s, "root@labor:~", x0, -0.25, e)
    raute = tt(s, "#", sp(x0, 12, e), -0.25, e, ROT)
    l_root = text(s, T(s, "konto2", "Konto root:", "account root:", "cuenta root:", "root 账户：", "compte root :", "root hesabı:"),
                  (-1.5, -0.25), FK, "right", GRAU)
    t_root = text(s, T(s, "darf", "# = root, darf alles", "# = root, may do anything", "# = root, puede hacerlo todo",
                       "# = root，可以做任何事", "# = root, a tous les droits", "# = root, her şeyi yapabilir"),
                  (sp(x0, 13, e) + 0.12, -0.25), FK, "left", ROT)
    schritt(s, EIN([zeile, l_stud], 0.6))
    s.pause(0.6)
    for k, t in ((k_user, t_user), (k_host, t_host), (k_dir, t_dir), (k_end, t_end)):
        schritt(s, ZEICHNE(k, 0.5), EIN(t, 0.5))
        s.pause(0.3)
    s.pause(0.3)
    schritt(s, EIN([root, l_root], 0.6))
    schritt(s, EIN([raute, t_root], 0.6))
    schritt(s, BETONE(raute, 0.8))
    s.speichern()


def k2sitzungen():
    """Zwei Fenster, zwei Shells: links cd /etc und exit, rechts bleibt alles, wie es war."""
    s = Szene("linux/k2sitzungen")
    e = 0.15
    links = kasten(s, (-1.72, 0.0), 3.2, 1.5, fuellung=TERM, form="rect", farbe=GRAU)
    rechts = kasten(s, (1.72, 0.0), 3.2, 1.5, fuellung=TERM, form="rect", farbe=GRAU)
    t1 = text(s, T(s, "f1", "Fenster 1: Sitzung 1", "window 1: session 1", "ventana 1: sesión 1", "窗口 1：会话 1",
                   "fenêtre 1 : session 1", "pencere 1: oturum 1"), (-1.72, 0.98), FK)
    t2 = text(s, T(s, "f2", "Fenster 2: Sitzung 2", "window 2: session 2", "ventana 2: sesión 2", "窗口 2：会话 2",
                   "fenêtre 2 : session 2", "pencere 2: oturum 2"), (1.72, 0.98), FK)
    xl, xr = -3.2, 0.24
    l1 = tt(s, "student@labor:~$", xl, 0.5, e)
    l1b = tt(s, " cd /etc", sp(xl, 16, e), 0.5, e)
    l2 = tt(s, "student@labor:/etc$", xl, 0.25, e)
    l2b = tt(s, " exit", sp(xl, 19, e), 0.25, e)
    r1 = tt(s, "student@labor:~$", xr, 0.5, e)
    bleibt = text(s, T(s, "bleibt", "bleibt in ~", "stays in ~", "sigue en ~", "仍在 ~", "reste dans ~", "~ içinde kalır"),
                  (1.72, -0.12), FK, "center", GRUEN)
    weiter = text(s, T(s, "weiter", "läuft weiter", "keeps running", "sigue en marcha", "继续运行", "continue de tourner",
                       "çalışmaya devam eder"), (1.72, -0.45), FK, "center", GRUEN)
    schl = schleier(s, (-1.72, 0.0), 3.2, 1.5, 0.65)
    ende = text(s, T(s, "beendet", "Shell beendet", "shell has ended", "la shell terminó", "Shell 已结束", "shell terminé",
                     "kabuk sona erdi"), (-1.72, -0.35), FK, "center", ROT)
    schritt(s, WACHS([links, rechts], 0.7), EIN([t1, t2], 0.7))
    schritt(s, EIN([l1, r1], 0.6))
    s.pause(0.6)
    schritt(s, EIN(l1b, 0.6))
    schritt(s, EIN(l2, 0.6))
    schritt(s, BETONE(r1, 0.8), EIN(bleibt, 0.8))
    s.pause(0.6)
    schritt(s, EIN(l2b, 0.5))
    schritt(s, EIN([schl, ende], 0.8))
    schritt(s, EIN(weiter, 0.6))
    s.speichern()


# ================================================================== Abschnitt 2: Aufbau einer Befehlszeile
def k2woerter():
    """uname -r wird am Leerzeichen geschnitten; die Wörter rücken in eigene Kästen."""
    s = Szene("linux/k2woerter")
    e, y = 0.36, 0.75
    x0 = -4 * cw(e)
    kaesten = [kasten(s, (-1.15, -0.5), 5 * cw(e) + 0.3, 0.55, fuellung=BLAU, farbe=BLAU, deckung=0.12),
               kasten(s, (1.15, -0.5), 2 * cw(e) + 0.3, 0.55, fuellung=BLAU, farbe=BLAU, deckung=0.12)]
    grau = tt(s, "uname -r", x0, y, e, HELLGRAU)
    w1 = tt(s, "uname", x0, y, e)
    w2 = tt(s, "-r", sp(x0, 6, e), y, e)
    xs = sp(x0, 5, e) + cw(e) / 2
    schnitt = linie(s, (xs, 1.1), (xs, 0.4), ROT, 3, DASH)
    l_schnitt = text(s, T(s, "leer", "Leerzeichen", "space", "espacio", "空格", "espace", "boşluk"), (xs, 1.3), FM, "center", ROT)
    l1 = text(s, T(s, "wort1", "Wort 1", "word 1", "palabra 1", "第 1 个词", "mot 1", "sözcük 1"), (-1.15, -0.98), FK)
    l2 = text(s, T(s, "wort2", "Wort 2", "word 2", "palabra 2", "第 2 个词", "mot 2", "sözcük 2"), (1.15, -0.98), FK)
    schritt(s, EIN([grau, w1, w2], 0.6))
    s.pause(0.6)
    schritt(s, ZEICHNE(schnitt, 0.7), EIN(l_schnitt, 0.7))
    s.pause(0.4)
    schritt(s, ZU(w1, -1.15, -0.5, 1.0), ZU(w2, 1.15, -0.5, 1.0))
    schritt(s, WACHS([k[0] for k in kaesten], 0.6), EIN([l1, l2], 0.6))
    s.speichern()


def k2argumente():
    """echo Hallo     Welt: drei Wörter, echo bekommt zwei Argumente und schreibt sie mit einem Leerzeichen."""
    s = Szene("linux/k2argumente")
    e, y = 0.26, 1.05
    x0 = -19 * cw(e) / 2
    ziele = ((-1.6, 4), (0.0, 5), (1.6, 4))
    kaesten = [kasten(s, (x, 0.0), n * cw(e) + 0.3, 0.48, fuellung=BLAU, farbe=BLAU, deckung=0.12)[0] for x, n in ziele]
    grau = tt(s, "echo Hallo     Welt", x0, y, e, HELLGRAU)
    woerter = [tt(s, "echo", x0, y, e), tt(s, "Hallo", sp(x0, 5, e), y, e), tt(s, "Welt", sp(x0, 15, e), y, e)]
    striche = [linie(s, (sp(x0, i, e) + 0.025, y - 0.2), (sp(x0, i + 1, e) - 0.025, y - 0.2), ORANGE, 3) for i in
               (4, 10, 11, 12, 13, 14)]
    l_gap = text(s, T(s, "fuenf", "5 Leerzeichen", "5 spaces", "5 espacios", "5 个空格", "5 espaces", "5 boşluk"),
                 (msp(x0, 10, 14, e), y + 0.32), FM, "center", ORANGE)
    labels = [text(s, T(s, "befehl", "Befehl", "command", "comando", "命令", "commande", "komut"), (-1.6, -0.42), FK),
              text(s, T(s, "arg1", "Argument 1", "argument 1", "argumento 1", "参数 1", "argument 1", "argüman 1"), (0.0, -0.42),
                   FK),
              text(s, T(s, "arg2", "Argument 2", "argument 2", "argumento 2", "参数 2", "argument 2", "argüman 2"), (1.6, -0.42),
                   FK)]
    l_aus = text(s, T(s, "ausgabe", "Ausgabe:", "output:", "salida:", "输出：", "sortie :", "çıktı:"), (-0.85, -1.05), FK,
                 "right", GRAU)
    aus = tt(s, "Hallo Welt", -0.7, -1.05, e)
    schritt(s, EIN([grau] + woerter + striche + [l_gap], 0.6))
    s.pause(0.6)
    schritt(s, *[ZU(wo, x, 0.0, 1.0) for wo, (x, n) in zip(woerter, ziele)])
    schritt(s, WACHS(kaesten, 0.6), EIN(labels, 0.6))
    s.pause(0.6)
    schritt(s, EIN([l_aus, aus], 0.7))
    s.speichern()


def k2buendeln():
    """uname -s -r -m, -srm und -mrs: die Buchstaben wandern, die Ausgabe bleibt dieselbe."""
    s = Szene("linux/k2buendeln")
    e, eo, x0 = 0.21, 0.16, -3.0
    ys, yo = (1.35, 0.45, -0.45), (1.08, 0.18, -0.72)
    r1 = tt(s, "$ uname -s -r -m", x0, ys[0], e)
    # Ausgabe gekürzt wie in der Übergabe (Linux 6.6.87.2-… x86_64): dreimal die ganze Zeile wäre über 300 KB
    o = [[tt(s, "Linux 6.6.87.2-", x0, y, eo, DUNKEL), text(s, "…", (sp(x0, 15, eo) + 0.02, y), FM, "left", DUNKEL),
          tt(s, "x86_64", sp(x0, 18, eo), y, eo, DUNKEL)] for y in yo]
    b2 = tt(s, "$ uname -", x0, ys[1], e)
    b3 = tt(s, "$ uname -", x0, ys[2], e)
    # Buchstaben der zweiten Zeile beginnen an ihrem Platz in Zeile 1, die der dritten an ihrem Platz in Zeile 2
    z2 = (("s", 9, 9), ("r", 12, 10), ("m", 15, 11))
    z3 = (("m", 11, 9), ("r", 10, 10), ("s", 9, 11))
    b_z2 = [tt(s, ch, sp(x0, von, e), ys[0], e) for ch, von, nach in z2]
    b_z3 = [tt(s, ch, sp(x0, von, e), ys[1], e) for ch, von, nach in z3]
    labs = [text(s, T(s, "einzeln", "einzeln", "separate", "por separado", "分开写", "séparées", "ayrı ayrı"), (-0.95, ys[0]), FK,
                 "left", GRAU),
            text(s, T(s, "gebuendelt", "gebündelt", "bundled", "agrupadas", "合并写", "regroupées", "birleşik"), (-0.95, ys[1]), FK,
                 "left", GRAU),
            text(s, T(s, "andere", "gebündelt, andere Reihenfolge", "bundled, other order", "agrupadas, otro orden",
                      "合并写，顺序不同", "regroupées, autre ordre", "birleşik, başka sırada"), (-0.95, ys[2]), FK, "left", GRAU)]
    kl = [linie(s, (1.12, 1.13), (1.2, 1.13), GRAU), linie(s, (1.2, 1.13), (1.2, -0.77), GRAU),
          linie(s, (1.12, -0.77), (1.2, -0.77), GRAU)]
    l_kl = text(s, T(s, "gleich", "dreimal dieselbe\nAusgabe", "the same output\nthree times", "la misma salida\ntres veces",
                     "三次输出\n完全相同", "trois fois\nla même sortie", "üç kez\naynı çıktı"), (1.35, 0.18), FK, "left")
    schritt(s, EIN(r1, 0.5))
    schritt(s, EIN([o[0], labs[0]], 0.5))
    s.pause(0.6)
    schritt(s, EIN([b2] + b_z2, 0.4))
    schritt(s, *[ZU(b, sp(x0, nach, e) + cw(e) / 2, ys[1], 1.0) for b, (ch, von, nach) in zip(b_z2, z2)])
    schritt(s, EIN([o[1], labs[1]], 0.5))
    s.pause(0.6)
    schritt(s, EIN([b3] + b_z3, 0.4))
    schritt(s, *[ZU(b, sp(x0, nach, e) + cw(e) / 2, ys[2], 1.0) for b, (ch, von, nach) in zip(b_z3, z3)])
    schritt(s, EIN([o[2], labs[2]], 0.5))
    s.pause(0.6)
    schritt(s, ZEICHNE(kl, 0.6), EIN(l_kl, 0.6))
    s.speichern()


def k2zerlegt():
    """head -n 2 /etc/os-release: Befehl, Option mit Wert (Bogen), Argument; darunter die zwei Zeilen der Ausgabe."""
    s = Szene("linux/k2zerlegt")
    e, y = 0.30, 0.95
    x0 = -25 * cw(e) / 2
    zeile = tt(s, "head -n 2 /etc/os-release", x0, y, e)
    k_b = klammer(s, sp(x0, 0, e) + 0.03, sp(x0, 4, e) - 0.03, 0.68)
    t_b = text(s, T(s, "befehl", "Befehl", "command", "comando", "命令", "commande", "komut"), (msp(x0, 0, 3, e), 0.48), FK)
    k_o = klammer(s, sp(x0, 5, e) + 0.03, sp(x0, 9, e) - 0.03, 0.68)
    t_o = text(s, T(s, "optwert", "Option\nmit Wert", "option\nwith value", "opción\ncon valor", "带值的\n选项", "option\navec valeur",
                    "değerli\nseçenek"), (msp(x0, 5, 8, e), 0.38), FK)
    k_a = klammer(s, sp(x0, 10, e) + 0.03, sp(x0, 25, e) - 0.03, 0.68)
    t_a = text(s, T(s, "argdatei", "Argument:\ndie Datei", "argument:\nthe file", "argumento:\nel archivo", "参数：\n文件",
                    "argument :\nle fichier", "argüman:\ndosya"), (msp(x0, 10, 24, e), 0.38), FK)
    bg = bogen(s, msp(x0, 5, 6, e), msp(x0, 8, 8, e), y + 0.22, 0.2, ORANGE)
    t_bg = text(s, T(s, "zusammen", "gehört zusammen", "belong together", "van juntos", "属于一体", "vont ensemble",
                     "birbirine ait"), (msp(x0, 5, 8, e), y + 0.6), FM, "center", ORANGE)
    l_aus = text(s, T(s, "zweizeilen", "Ausgabe: die ersten 2 Zeilen", "output: the first 2 lines", "salida: las 2 primeras líneas",
                      "输出：前 2 行", "sortie : les 2 premières lignes", "çıktı: ilk 2 satır"), (x0, -0.15), FK, "left", GRAU)
    o1 = tt(s, 'PRETTY_NAME="Ubuntu 26.04.1 LTS"', x0, -0.42, 0.17, DUNKEL)
    o2 = tt(s, 'NAME="Ubuntu"', x0, -0.67, 0.17, DUNKEL)
    schritt(s, EIN(zeile, 0.6))
    s.pause(0.6)
    schritt(s, ZEICHNE(k_b, 0.6), EIN(t_b, 0.6))
    s.pause(0.4)
    schritt(s, ZEICHNE(k_o, 0.6), EIN(t_o, 0.6))
    schritt(s, ZEICHNE(bg, 0.7), EIN(t_bg, 0.7))
    s.pause(0.4)
    schritt(s, ZEICHNE(k_a, 0.6), EIN(t_a, 0.6))
    s.pause(0.6)
    schritt(s, EIN([l_aus, o1, o2], 0.7))
    s.speichern()


def k2ende():
    """ls -- -l: Schranke hinter --; links werden Optionen erkannt, rechts ist alles ein gewöhnliches Argument."""
    s = Szene("linux/k2ende")
    e, y = 0.36, 0.55
    x0 = -4 * cw(e)
    xb = sp(x0, 5, e) + cw(e) / 2
    f_l = flaeche(s, -3.0, -1.0, xb - 0.03, 1.2, GRUEN_HELL)
    f_r = flaeche(s, xb + 0.03, -1.0, 3.0, 1.2, BLAU_HELL)
    vorn = tt(s, "ls --", x0, y, e)
    hinten = tt(s, "-l", sp(x0, 6, e), y, e)
    schranke = linie(s, (xb, 1.3), (xb, -1.0), ORANGE, 6)
    t_s = text(s, T(s, "ende", "Ende der Optionen", "end of options", "fin de las opciones", "选项结束", "fin des options",
                    "seçeneklerin sonu"), (xb, 1.48), FK, "center", ORANGE)
    t_l = text(s, T(s, "erkannt", "Optionen werden\nerkannt", "options are\nrecognized", "las opciones\nse reconocen",
                    "识别\n选项", "les options\nsont reconnues", "seçenekler\ntanınır"), (-1.5, -0.45), FK)
    t_r = text(s, T(s, "nurarg", "nur gewöhnliche\nArgumente", "ordinary arguments\nonly", "solo argumentos\nnormales",
                    "只是普通\n参数", "seulement des\narguments ordinaires", "yalnızca sıradan\nargümanlar"), (1.65, -0.45), FK)
    t_d = text(s, T(s, "dateiname", "ein Dateiname", "a file name", "un nombre de archivo", "一个文件名", "un nom de fichier",
                    "bir dosya adı"), (xb + 0.12, y - 0.42), FK, "left", BLAU)
    schritt(s, EIN([f_l, f_r], 0.5))
    schritt(s, EIN([vorn, hinten], 0.6))
    s.pause(0.6)
    schritt(s, ZEICHNE(schranke, 0.8), EIN(t_s, 0.8))
    s.pause(0.6)
    schritt(s, EIN(t_l, 0.6))
    schritt(s, EIN(t_r, 0.6))
    s.pause(0.6)
    schritt(s, BETONE(hinten, 0.8), EIN(t_d, 0.8))
    s.speichern()


# ================================================================== Abschnitt 3: Arten von Befehlen
def k2suche():
    """Die Shell prüft die Ordner des Suchpfads der Reihe nach; in /usr/bin findet sie uname, der Rest bleibt ungeprüft."""
    s = Szene("linux/k2suche")
    x0 = -2.4
    ordner = ("/usr/local/sbin", "/usr/local/bin", "/usr/sbin", "/usr/bin", "/sbin", "/bin")
    ys = (1.15, 0.8, 0.45, 0.1, -0.25, -0.6)
    titel = text(s, T(s, "titel", "Suche nach uname im Suchpfad", "searching the search path for uname",
                      "búsqueda de uname en la ruta de búsqueda", "在搜索路径中查找 uname", "recherche de uname dans le chemin",
                      "arama yolunda uname aranıyor"), (x0, 1.55), FK, "left")
    zeilen = [tt(s, o, x0, y) for o, y in zip(ordner, ys)]
    rest = text(s, "…", (x0, -0.92), FS, "left", GRAU)
    rahmen = s.box("", (-1.6, ys[0]), breite=1.76, hoehe=0.3, form="rect", farbe=ORANGE, fuellung=WEISS, deckung=0, dicke=2.5)
    frage = tt(s, "uname?", -0.6, ys[0], 0.17, ORANGE)
    kreuze = [s.kreuzchen(None, 0.55, y, farbe=ROT, groesse=0.2) for y in ys[:3]]
    ok = haken(s, 0.55, ys[3])
    pfeil = pf(s, (0.85, ys[3]), (1.3, ys[3]))
    box = kasten(s, (2.3, ys[3]), 1.9, 0.62, fuellung=GRUEN_HELL, farbe=GRUEN)
    b1 = tt(s, "/usr/bin/uname", 2.3, ys[3] + 0.12, 0.15, anker="m")
    b2 = text(s, T(s, "start", "wird gestartet", "is started", "se inicia", "被启动", "est lancé", "başlatılır"), (2.3, ys[3] - 0.15),
              FM)
    schl = schleier(s, (-1.2, -0.58), 2.7, 0.85, 0.72)
    t_rest = text(s, T(s, "ungesehen", "nicht mehr angesehen", "no longer looked at", "ya no se miran", "不再查看",
                       "plus examinés", "artık bakılmaz"), (0.4, -0.58), FK, "left", GRAU)
    schritt(s, EIN([titel, rest] + zeilen, 0.7))
    s.pause(0.6)
    schritt(s, EIN([rahmen, frage], 0.4))
    for i in range(3):
        schritt(s, EIN(kreuze[i], 0.4))
        schritt(s, ZU(rahmen, -1.6, ys[i + 1], 0.4), ZU(frage, -0.6 + 3 * cw(0.17), ys[i + 1], 0.4))
    schritt(s, ZEICHNE(ok, 0.5))
    s.pause(0.6)
    schritt(s, ZEICHNE(pfeil, 0.7), WACHS(box, 0.7), EIN([b1, b2], 0.7))
    schritt(s, EIN([schl, t_rest], 0.7))
    schritt(s, AUS([rahmen, frage], 0.4))
    s.speichern()


def k2cd():
    """Links ein gedachtes Programm cd (wechselt nur seine Kopie), rechts der eingebaute Befehl (die Shell wechselt selbst)."""
    s = Szene("linux/k2cd")
    pl = flaeche(s, -3.42, -0.95, -0.08, 1.35, "#f4f4f4")
    pr = flaeche(s, 0.08, -0.95, 3.42, 1.35, "#f4f4f4")
    tl = text(s, T(s, "gedacht", "gedachtes Programm /usr/bin/cd", "imagined program /usr/bin/cd",
                   "programa imaginario /usr/bin/cd", "设想的程序 /usr/bin/cd", "programme imaginaire /usr/bin/cd",
                   "varsayımsal program /usr/bin/cd"), (-1.75, 1.6), FK)
    tr_ = text(s, T(s, "eingebaut", "eingebauter Befehl cd", "builtin command cd", "comando interno cd", "内置命令 cd",
                    "commande intégrée cd", "yerleşik komut cd"), (1.75, 1.6), FK)
    shell = T(s, "shell", "Shell", "shell", "shell", "Shell", "shell", "kabuk")
    ordner = T(s, "ordner", "Ordner:", "folder:", "carpeta:", "文件夹：", "dossier :", "klasör:")
    # links: Shell und Programm
    sh_l = kasten(s, (-2.55, 0.6), 1.2, 0.85, fuellung=WEISS)
    sh_l_t = [text(s, shell, (-2.55, 0.85), FK), text(s, ordner, (-2.55, 0.6), FM, "center", GRAU)]
    sh_l_o = tt(s, "~", -2.55, 0.36, 0.2, anker="m")
    pg = kasten(s, (-0.75, 0.6), 1.2, 0.85, fuellung=ORANGE_HELL, farbe=ORANGE)
    pg_t = [text(s, T(s, "prog", "Programm cd", "program cd", "programa cd", "程序 cd", "programme cd", "cd programı"), (-0.75, 0.85),
                 FM),
            text(s, T(s, "kopie", "Kopie:", "copy:", "copia:", "副本：", "copie :", "kopya:"), (-0.75, 0.6), FM, "center", GRAU)]
    pg_o = tt(s, "~", -0.75, 0.36, 0.2, anker="m")
    pg_etc = tt(s, "/etc", -0.75, 0.36, 0.2, anker="m")
    a = pf(s, (-1.95, 0.6), (-1.35, 0.6))
    a_t = text(s, T(s, "startet", "startet", "starts", "inicia", "启动", "lance", "başlatır"), (-1.65, 0.78), FM)
    schl = schleier(s, (-0.75, 0.6), 1.26, 0.9, 0.7)
    endet = text(s, T(s, "endet", "endet:\nKopie verloren", "ends:\ncopy is lost", "termina:\nla copia se pierde",
                      "结束：\n副本丢失", "se termine :\ncopie perdue", "biter:\nkopya kaybolur"), (-0.75, -0.05), FM, "center", ROT)
    bleibt = text(s, T(s, "bleibt", "Shell bleibt in ~", "shell stays in ~", "la shell sigue en ~", "Shell 仍在 ~",
                       "la shell reste dans ~", "kabuk ~ içinde kalır"), (-2.55, -0.05), FM, "center", GRUEN)
    pr_l = tt(s, "student@labor:~$", -1.75, -0.6, 0.15, anker="m")
    # rechts: die Shell selbst
    sh_r = kasten(s, (1.75, 0.6), 1.6, 0.85, fuellung=WEISS)
    sh_r_t = [text(s, shell, (1.75, 0.85), FK), text(s, ordner, (1.75, 0.6), FM, "center", GRAU)]
    sh_r_o = tt(s, "~", 1.75, 0.36, 0.2, anker="m")
    sh_r_etc = tt(s, "/etc", 1.75, 0.36, 0.2, anker="m")
    selbst = text(s, T(s, "selbst", "Shell wechselt selbst", "the shell changes itself", "la shell cambia ella misma",
                       "Shell 自己切换", "la shell change elle-même", "kabuk kendisi değiştirir"), (1.75, -0.05), FM, "center",
                  GRUEN)
    pr_r = tt(s, "student@labor:/etc$", 1.75, -0.6, 0.15, anker="m")
    schritt(s, EIN([pl, pr, tl, tr_], 0.6))
    schritt(s, WACHS(sh_l, 0.6), EIN(sh_l_t + [sh_l_o], 0.6))
    s.pause(0.6)
    schritt(s, ZEICHNE(a, 0.7), EIN(a_t, 0.7), WACHS(pg, 0.7), EIN(pg_t + [pg_o], 0.7))
    schritt(s, FORM(pg_o, pg_etc, 0.8))
    s.pause(0.6)
    schritt(s, EIN([schl, endet], 0.7))
    schritt(s, EIN([bleibt, pr_l], 0.7))
    schritt(s, BETONE(sh_l_o, 0.6))
    s.pause(0.6)
    schritt(s, WACHS(sh_r, 0.6), EIN(sh_r_t + [sh_r_o], 0.6))
    schritt(s, FORM(sh_r_o, sh_r_etc, 0.8))
    schritt(s, EIN([selbst, pr_r], 0.7))
    s.speichern()


def k2alias():
    """ls wird beim Einlesen durch ls --color=auto ersetzt; danach findet die Suche /usr/bin/ls."""
    s = Szene("linux/k2alias")
    e, x0 = 0.22, -1.75
    xl = sp(x0, 2, e)
    ys = (1.25, 0.35, -0.55)
    l1 = text(s, T(s, "getippt", "getippt:", "typed:", "tecleado:", "输入：", "tapé :", "yazılan:"), (-3.35, ys[0]), FK, "left",
              GRAU)
    z1 = tt(s, "$ ls", x0, ys[0], e)
    l2 = text(s, T(s, "eingelesen", "nach dem Einlesen:", "after reading:", "tras la lectura:", "读入之后：", "après la lecture :",
                   "okunduktan sonra:"), (-3.35, ys[1]), FK, "left", GRAU)
    kopie = tt(s, "ls", xl, ys[0], e, ORANGE)
    vorlage = tt(s, "ls --color=auto", xl, ys[1], e, ORANGE)
    a1 = pf(s, (-1.3, 1.05), (-1.3, 0.55), farbe=ORANGE)
    a1_t = text(s, T(s, "ersetzt", "Alias ersetzt den Text", "alias replaces the text", "el alias sustituye el texto",
                     "别名替换文本", "l’alias remplace le texte", "takma ad metni değiştirir"), (-1.15, 0.8), FM, "left", ORANGE)
    l3 = text(s, T(s, "findet", "Suche findet:", "search finds:", "la búsqueda halla:", "查找到：", "la recherche trouve :",
                   "arama bulur:"), (-3.35, ys[2]), FK, "left", GRAU)
    z3 = tt(s, "/usr/bin/ls", xl, ys[2], e)
    a2 = pf(s, (-1.3, 0.15), (-1.3, -0.35))
    a2_t = text(s, T(s, "imsuchpfad", "Suche im Suchpfad", "search in the search path", "búsqueda en la ruta",
                     "在搜索路径中查找", "recherche dans le chemin", "arama yolunda arama"), (-1.15, -0.1), FM, "left")
    tab = kasten(s, (2.3, 0.75), 2.15, 1.05, fuellung=TERM, form="rect", farbe=GRAU)
    tab_t = text(s, T(s, "aliase", "hinterlegte Aliase", "stored aliases", "alias guardados", "已存的别名", "alias enregistrés",
                      "kayıtlı takma adlar"), (2.3, 1.1), FM, "center", GRAU)
    al1 = tt(s, "ls='ls --color=auto'", 1.33, 0.8, 0.14)
    al2 = tt(s, "ll='ls -alF'", 1.33, 0.53, 0.14)
    schritt(s, EIN([l1, z1], 0.6))
    schritt(s, WACHS(tab, 0.7), EIN([tab_t, al1, al2], 0.7))
    s.pause(0.6)
    schritt(s, EIN(kopie, 0.3))
    schritt(s, ZU(kopie, xl + cw(e), ys[1], 0.7), ZEICHNE(a1, 0.7), EIN(l2, 0.7))
    schritt(s, FORM(kopie, vorlage, 0.9), BETONE(al1, 0.9), EIN(a1_t, 0.9))
    s.pause(0.6)
    schritt(s, ZEICHNE(a2, 0.7), EIN([a2_t, l3, z3], 0.7))
    s.speichern()


def k2arten():
    """Weiche der Namensauflösung; ls endet beim Alias, cd beim eingebauten Befehl, uname im Suchpfad; type und which."""
    s = Szene("linux/k2arten")
    c, ys = -0.55, (1.4, 0.8, 0.2, -0.4, -1.0)
    rand = s.box("", (0.435, 0.265), breite=5.97, hoehe=3.23, form="rect", farbe=GRAU, fuellung=WEISS, deckung=0, dicke=2,
                 dash=DASH)
    l_rand = text(s, T(s, "inshell", "in der Shell", "inside the shell", "dentro de la shell", "在 Shell 内部", "dans la shell",
                       "kabuğun içinde"), (3.32, 1.72), FM, "right", GRAU)
    name = text(s, T(s, "name", "Name", "name", "nombre", "名称", "nom", "ad"), (c, 2.15), FK)
    a_name = pf(s, (c, 2.02), (c, 1.6))
    fragen = (T(s, "f_alias", "Alias?", "alias?", "¿Alias?", "别名？", "alias ?", "takma ad mı?"),
              T(s, "f_kw", "Schlüsselwort?", "keyword?", "¿Palabra clave?", "关键字？", "mot-clé ?", "anahtar sözcük mü?"),
              T(s, "f_fn", "Funktion?", "function?", "¿Función?", "函数？", "fonction ?", "işlev mi?"),
              T(s, "f_bi", "eingebaut?", "builtin?", "¿Interno?", "内置？", "intégré ?", "yerleşik mi?"),
              T(s, "f_pf", "Datei im Suchpfad?", "file in search path?", "¿Archivo en la ruta?", "搜索路径中的文件？",
                "fichier dans le chemin ?", "arama yolunda dosya mı?"))
    st = [kasten(s, (c, y), 1.9, 0.36, f, FK, fuellung=GRAU_HELL, farbe=GRAU, dicke=2) for f, y in zip(fragen, ys)]
    runter = [pf(s, (c, ys[i] - 0.18), (c, ys[i + 1] + 0.18)) for i in range(4)]
    nein = text(s, T(s, "nein", "nein", "no", "no", "否", "non", "hayır"), (c + 0.1, 1.1), FM, "left", GRAU)
    raus = [pf(s, (0.4, y), (0.75, y)) for y in ys]
    ja = text(s, T(s, "ja", "ja", "yes", "sí", "是", "oui", "evet"), (0.57, 1.55), FM, "center", GRAU)
    erg = [text(s, T(s, "e1", "Text einsetzen", "insert the text", "insertar el texto", "插入文本", "insérer le texte",
                     "metni yerleştir"), (1.35, ys[0]), FM, "left"),
           text(s, T(s, "e2", "Teil der Sprache (if, for, …)", "part of the language (if, for, …)",
                     "parte del lenguaje (if, for, …)", "语言的一部分（if、for……）", "élément du langage (if, for, …)",
                     "dilin parçası (if, for, …)"), (1.35, ys[1]), FM, "left"),
           text(s, T(s, "e3", "Funktion ausführen", "run the function", "ejecutar la función", "执行函数", "exécuter la fonction",
                     "işlevi çalıştır"), (1.35, ys[2]), FM, "left"),
           text(s, T(s, "e4", "Shell führt ihn selbst aus", "the shell runs it itself", "la shell lo ejecuta ella misma",
                     "Shell 自己执行", "la shell l’exécute elle-même", "kabuk kendisi çalıştırır"), (1.35, ys[3]), FM, "left"),
           text(s, T(s, "e5", "Programmdatei starten", "start the program file", "iniciar el archivo de programa", "启动程序文件",
                     "lancer le fichier programme", "program dosyasını başlat"), (1.35, ys[4] + 0.12), FM, "left"),
           text(s, T(s, "e5n", "sonst: command not found", "otherwise: command not found", "si no: command not found",
                     "否则：command not found", "sinon : command not found", "yoksa: command not found"), (1.35, ys[4] - 0.12),
                FM, "left", ROT)]
    typ = kasten(s, (-2.0, 0.2), 0.75, 2.9, fuellung=BLAU_HELL, farbe=BLAU, dicke=2, form="rect")
    typ_tt = tt(s, "type", -2.0, 1.45, 0.17, BLAU, "m")
    typ_t = text(s, T(s, "alles", "sieht\nalles", "sees\nall", "lo ve\ntodo", "全都\n看到", "voit\ntout", "her şeyi\ngörür"),
                 (-2.0, 0.95), FM, "center", BLAU)
    wh = kasten(s, (-2.95, -1.72), 0.85, 0.34, fuellung=ORANGE_HELL, farbe=ORANGE, dicke=2)
    wh_tt = tt(s, "which", -2.95, -1.72, 0.17, anker="m")
    a_wh = pf(s, (-2.52, -1.72), (-1.0, -1.18), knick="hv", farbe=ORANGE)
    wh_t = text(s, T(s, "nurpfad", "nur Suchpfad", "search path only", "solo la ruta", "仅搜索路径", "chemin seul",
                     "yalnız arama yolu"), (-1.75, -1.57), FM, "center", ORANGE)
    chips = [tt(s, n, c, 1.82, 0.17, f, "m") for n, f in (("ls", BLAU), ("cd", ORANGE), ("uname", GRUEN))]
    schritt(s, EIN([rand, l_rand, name, a_name], 0.6))
    schritt(s, WACHS([k[0] for k in st], 0.7), EIN([k[1] for k in st] + [nein], 0.7), ZEICHNE(runter, 0.7))
    schritt(s, ZEICHNE(raus, 0.6), EIN(erg + [ja], 0.6))
    s.pause(0.6)
    for chip, halt, dt in ((chips[0], 0, 0.4), (chips[1], 3, 0.35), (chips[2], 4, 0.3)):
        schritt(s, EIN(chip, 0.3))
        for y in ys[:halt + 1]:
            schritt(s, ZU(chip, c, y, dt))
        schritt(s, ZU(chip, 1.05, ys[halt], 0.5))
        s.pause(0.4)
    s.pause(0.2)
    schritt(s, WACHS(typ, 0.7), EIN([typ_tt, typ_t], 0.7))
    schritt(s, WACHS(wh, 0.8), EIN([wh_tt, wh_t], 0.8), ZEICHNE(a_wh, 0.8))
    s.speichern()


# ================================================================== Abschnitt 4: Hilfe finden
def k2manpage():
    """Nachgebildete Handbuchseite uname(1) mit den Teilen in fester Reihenfolge, rechts erklärt."""
    s = Szene("linux/k2manpage")
    e, x0, xe = 0.135, -3.27, 0.9
    seite = kasten(s, (-1.33, 0.3), 4.15, 3.0, fuellung=WEISS, form="rect", farbe=GRAU, dicke=2)
    teile = [
        ([tt(s, "UNAME(1)     General Commands Manual     UNAME(1)", x0, 1.6, e)],
         T(s, "x0", "Name und Abschnitt", "name and section", "nombre y sección", "名称和节号", "nom et section",
           "ad ve bölüm"), 1.6),
        ([tt(s, "NAME", x0, 1.3, e, BLAU), tt(s, "    uname - Print certain system information.", x0, 1.1, e)],
         T(s, "x1", "Name und Kurzbeschreibung", "name and short description", "nombre y descripción breve",
           "名称和简短说明", "nom et brève description", "ad ve kısa açıklama"), 1.2),
        ([tt(s, "SYNOPSIS", x0, 0.8, e, BLAU), tt(s, "    uname [-a|--all] [-s|--kernel-name]", x0, 0.6, e)],
         T(s, "x2", "Aufrufform", "usage", "forma de uso", "用法", "forme d’appel", "kullanım biçimi"), 0.7),
        ([tt(s, "DESCRIPTION", x0, 0.3, e, BLAU), linie(s, (sp(x0, 4, e), 0.12), (sp(x0, 36, e), 0.12), HELLGRAU, 5)],
         T(s, "x3", "was der Befehl tut", "what the command does", "qué hace el comando", "命令做什么", "ce que fait la commande",
           "komutun ne yaptığı"), 0.2),
        ([tt(s, "OPTIONS", x0, -0.2, e, BLAU), tt(s, "    -a, --all", x0, -0.4, e),
          linie(s, (sp(x0, 4, e), -0.58), (sp(x0, 21, e), -0.58), HELLGRAU, 5)],
         T(s, "x4", "jede Option einzeln", "each option in turn", "cada opción por separado", "逐个说明选项",
           "chaque option à part", "her seçenek tek tek"), -0.4),
        ([text(s, T(s, "rest", "EXIT STATUS, FILES, SEE ALSO, …\n(bei anderen Seiten)", "EXIT STATUS, FILES, SEE ALSO, …\n(on other pages)",
                    "EXIT STATUS, FILES, SEE ALSO, …\n(en otras páginas)", "EXIT STATUS、FILES、SEE ALSO……\n（其他页面中）",
                    "EXIT STATUS, FILES, SEE ALSO, …\n(sur d’autres pages)", "EXIT STATUS, FILES, SEE ALSO, …\n(başka sayfalarda)"),
               (x0, -0.95), FM, "left", GRAU)],
         T(s, "x5", "weitere Teile, je nach Seite", "more parts, depending on the page", "más partes, según la página",
           "更多部分，视页面而定", "autres parties selon la page", "sayfaya göre başka bölümler"), -0.95)]
    schritt(s, WACHS(seite, 0.6))
    for i, (objs, erkl, y) in enumerate(teile):
        t = text(s, erkl, (xe, y), FM, "left", GRAU)
        schritt(s, EIN(objs + [t], 0.6))
        if i < len(teile) - 1:
            s.pause(0.4)
    s.speichern()


def k2synopsis():
    """Zwei Aufrufformen; farbige Marken für [ ], |, ... und Platzhalter, mit Legende."""
    s = Szene("linux/k2synopsis")
    e, x0, y1, y2 = 0.2, -3.0, 1.05, 0.35
    h = 0.27

    def m(cols, y, farbe):
        return [mark(s, sp(x0, a, e) - 0.005, sp(x0, b + 1, e) + 0.005, y, h, farbe, 0.28) for a, b in cols]
    m_kl = m([(6, 6), (15, 15), (17, 17), (34, 34)], y1, BLAU) + m([(4, 4), (11, 11), (16, 16), (21, 21)], y2, BLAU)
    m_st = m([(9, 9), (20, 20)], y1, ORANGE)
    m_pk = m([(12, 14), (22, 24)], y2, GRUEN)
    m_ph = m([(5, 10), (17, 20)], y2, ROT)
    z1 = tt(s, "uname [-a|--all] [-s|--kernel-name]", x0, y1, e)
    weiter = text(s, "…", (sp(x0, 35, e) + 0.12, y1), FS, "left", GRAU)
    z2 = tt(s, "cat [OPTION]... [FILE]...", x0, y2, e)
    leg = []
    for (x, y, sym, farbe, b, erkl) in (
            (-3.0, -0.45, "[ ]", BLAU, 0.5, T(s, "l1", "darf fehlen", "may be left out", "se puede omitir", "可以省略", "facultatif",
                                              "yazılmayabilir")),
            (0.25, -0.45, "|", ORANGE, 0.5, T(s, "l2", "eines davon wählen", "choose one of them", "elegir una de ellas", "选其中之一",
                                              "en choisir une", "birini seç")),
            (-3.0, -0.9, "...", GRUEN, 0.5, T(s, "l3", "darf sich wiederholen", "may be repeated", "se puede repetir",
                                              "可以重复", "peut se répéter", "tekrarlanabilir")),
            (0.25, -0.9, "FILE", ROT, 0.62, T(s, "l4", "Platzhalter: Passendes einsetzen", "placeholder: put in something suitable",
                                              "marcador: poner algo adecuado", "占位符：填入合适的内容",
                                              "à remplacer par une valeur adaptée", "yer tutucu: uygun bir şey yaz"))):
        leg.append([mark(s, x, x + b, y, 0.3, farbe, 0.28), tt(s, sym, x + b / 2, y, e, anker="m"),
                    text(s, erkl, (x + b + 0.15, y), FK, "left")])
    schritt(s, EIN([z1, weiter, z2], 0.6))
    for marken, eintrag in ((m_kl, leg[0]), (m_st, leg[1]), (m_pk, leg[2]), (m_ph, leg[3])):
        s.pause(0.5)
        schritt(s, EIN(marken + eintrag, 0.8))
    s.speichern()


def k2abschnitte():
    """Das Handbuch als Regal mit acht Fächern; man uname greift Fach 1, man 2 uname Fach 2."""
    s = Szene("linux/k2abschnitte")
    xs, yr = (-2.55, -0.85, 0.85, 2.55), (0.5, -0.65)
    namen = (T(s, "s1", "1 Befehle", "1 commands", "1 comandos", "1 命令", "1 commandes", "1 komutlar"),
             T(s, "s2", "2 Systemaufrufe", "2 system calls", "2 llamadas al sistema", "2 系统调用", "2 appels système",
               "2 sistem çağrıları"),
             T(s, "s3", "3 Bibliotheken", "3 libraries", "3 bibliotecas", "3 库函数", "3 bibliothèques", "3 kütüphaneler"),
             T(s, "s4", "4 Gerätedateien", "4 device files", "4 dispositivos", "4 设备文件", "4 périphériques", "4 aygıt dosyaları"),
             T(s, "s5", "5 Dateiformate", "5 file formats", "5 formatos de archivo", "5 文件格式", "5 formats de fichier",
               "5 dosya biçimleri"),
             T(s, "s6", "6 Spiele", "6 games", "6 juegos", "6 游戏", "6 jeux", "6 oyunlar"),
             T(s, "s7", "7 Übersichten", "7 overviews", "7 visiones generales", "7 概述", "7 vues d’ensemble", "7 genel bakışlar"),
             T(s, "s8", "8 Verwaltung", "8 administration", "8 administración", "8 系统管理", "8 administration",
               "8 sistem yönetimi"))
    faecher, labels = [], []
    for i, nm in enumerate(namen):
        x, y = xs[i % 4], yr[i // 4]
        faecher.append(kasten(s, (x, y), 1.62, 1.05, fuellung="#f7f3ea", form="rect", farbe=GRAU, dicke=2)[0])
        labels.append(text(s, nm, (x, y - 0.36), FM))

    def karte(x, y, name):
        return [kasten(s, (x, y), 0.95, 0.24, fuellung=WEISS, form="rect", farbe=GRAU, dicke=1.5)[0],
                tt(s, name, x, y, 0.15, anker="m")]
    k_u1 = karte(xs[0], 0.82, "uname")
    k_p1 = karte(xs[0], 0.55, "passwd")
    k_u2 = karte(xs[1], 0.82, "uname")
    k_p5 = karte(xs[0], -0.33, "passwd")
    m1 = tt(s, "man uname", xs[0], 1.45, 0.17, BLAU, "m")
    m2 = tt(s, "man 2 uname", xs[1], 1.45, 0.17, BLAU, "m")
    a1 = pf(s, (xs[0], 1.33), (xs[0], 0.96), farbe=BLAU)
    a2 = pf(s, (xs[1], 1.33), (xs[1], 0.96), farbe=BLAU)
    schritt(s, WACHS(faecher, 0.8), EIN(labels, 0.8))
    s.pause(0.6)
    schritt(s, EIN(k_u1 + k_u2 + k_p1 + k_p5, 0.7))
    s.pause(0.6)
    schritt(s, EIN(m1, 0.6), ZEICHNE(a1, 0.6))
    schritt(s, BETONE(k_u1[1], 0.8))
    s.pause(0.6)
    schritt(s, EIN(m2, 0.6), ZEICHNE(a2, 0.6))
    schritt(s, BETONE(k_u2[1], 0.8))
    s.speichern()


def k2apropos():
    """apropos durchsucht eine Datenbank der NAME-Zeilen; der Suchbalken fährt darüber, zwei Treffer leuchten."""
    s = Szene("linux/k2apropos")
    e = 0.135
    zeilen = ("free (1) - Display amount of free and used memory in the system",
              "hostname (1) - show or set the system's host name",
              "passwd (1) - change user password",
              "passwd (5) - the password file",
              "rust-hostname (1) - Display or set the system's host name.",
              "uname (1) - Print certain system information.",
              "uname (2) - get name and information about current kernel")
    ys = [1.0 - 0.26 * i for i in range(7)]
    x0 = -64 * cw(e) / 2
    befehl = tt(s, '$ apropos "host name"', 0.0, 1.78, 0.17, anker="m")
    titel = text(s, T(s, "db", "Datenbank: Name, Abschnitt und NAME-Zeile jeder Handbuchseite",
                      "database: name, section and NAME line of every manual page",
                      "base de datos: nombre, sección y línea NAME de cada página",
                      "数据库：每个手册页的名称、节号和 NAME 行", "base de données : nom, section et ligne NAME de chaque page",
                      "veritabanı: her kılavuz sayfasının adı, bölümü ve NAME satırı"), (0.0, 1.45), FM, "center", GRAU)
    box = kasten(s, (0.0, 0.22), 4.95, 1.95, fuellung=TERM, form="rect", farbe=GRAU, dicke=2)
    treffer = [mark(s, x0 - 0.08, -x0 + 0.08, ys[i], 0.24, GRUEN, 0.25) for i in (1, 4)]
    balken = mark(s, x0 - 0.08, -x0 + 0.08, ys[0], 0.24, ORANGE, 0.35)
    z = [text(s, t, (x0 + 0.05, y), FM, "left") for t, y in zip(zeilen, ys)]   # Schrift statt Glyphen: Datei bleibt klein
    erg = text(s, T(s, "treffer", "2 Treffer, je mit Seite, Abschnitt und Kurzbeschreibung",
                    "2 hits, each with page, section and short description",
                    "2 resultados, cada uno con página, sección y descripción breve", "2 个结果，各含页面、节号和简短说明",
                    "2 résultats, chacun avec page, section et brève description",
                    "2 sonuç, her biri sayfa, bölüm ve kısa açıklamayla"), (0.0, -1.0), FM, "center", GRUEN)
    schritt(s, EIN(befehl, 0.5))
    schritt(s, WACHS(box, 0.7), EIN([titel] + z, 0.7))
    s.pause(0.6)
    schritt(s, EIN(balken, 0.3))
    schritt(s, ZU(balken, 0.0, ys[1], 0.35))
    schritt(s, EIN(treffer[0], 0.4))
    schritt(s, ZU(balken, 0.0, ys[4], 0.7))
    schritt(s, EIN(treffer[1], 0.4))
    schritt(s, ZU(balken, 0.0, ys[6], 0.5))
    schritt(s, AUS(balken, 0.3))
    schritt(s, EIN(erg, 0.6))
    s.speichern()


def k2hilfeweg():
    """Entscheidungsbaum: Name bekannt? nein → apropos; ja → Art des Befehls: eingebaut → help, Datei → --help bzw. man."""
    s = Szene("linux/k2hilfeweg")
    q1 = kasten(s, (-0.9, 1.45), 2.6, 0.42, T(s, "q1", "Name des Befehls bekannt?", "Do you know the command’s name?",
                                             "¿Conoces el nombre del comando?", "知道命令的名称吗？",
                                             "Connais-tu le nom de la commande ?", "Komutun adını biliyor musun?"), FK,
                fuellung=GRAU_HELL, farbe=GRAU)
    q2 = kasten(s, (0.85, 0.35), 2.2, 0.62, fuellung=GRAU_HELL, farbe=GRAU)
    q2_t = text(s, T(s, "q2", "Art des Befehls?", "kind of command?", "¿Tipo de comando?", "命令的类型？", "type de commande ?",
                     "komutun türü?"), (0.85, 0.47), FK)
    q2_tt = tt(s, "type", 0.85, 0.2, 0.17, BLAU, "m")
    blaetter = []
    for x, cmd, erkl in ((-2.6, "apropos", T(s, "b1", "Befehl suchen", "find the command", "buscar el comando", "查找命令",
                                             "trouver la commande", "komutu bul")),
                         (-0.9, "help", T(s, "b2", "eingebaute Befehle", "builtin commands", "comandos internos", "内置命令",
                                          "commandes intégrées", "yerleşik komutlar")),
                         (0.85, "--help", T(s, "b3", "Überblick", "overview", "resumen", "概览", "aperçu", "genel bakış")),
                         (2.6, "man", T(s, "b4", "alles", "everything", "todo", "全部", "tout", "her şey"))):
        blaetter.append([kasten(s, (x, -1.15), 1.55, 0.62, fuellung=GRUEN_HELL, farbe=GRUEN)[0],
                         tt(s, cmd, x, -1.02, 0.17, anker="m"), text(s, erkl, (x, -1.3), FM)])
    a_nein = pf(s, (-2.2, 1.45), (-2.6, -0.84), knick="hv")
    t_nein = text(s, T(s, "nein", "nein", "no", "no", "否", "non", "hayır"), (-2.4, 1.6), FM, "center", GRAU)
    a_ja = pf(s, (0.4, 1.45), (0.85, 0.66), knick="hv")
    t_ja = text(s, T(s, "ja", "ja", "yes", "sí", "是", "oui", "evet"), (0.62, 1.6), FM, "center", GRAU)
    a_bi = pf(s, (-0.25, 0.35), (-0.9, -0.84), knick="hv")
    t_bi = text(s, T(s, "eingeb", "eingebaut", "builtin", "interno", "内置", "intégrée", "yerleşik"), (-0.57, 0.5), FM, "center",
                GRAU)
    datei = T(s, "datei", "Datei", "file", "archivo", "文件", "fichier", "dosya")
    a_d1 = pf(s, (0.85, 0.04), (0.85, -0.84))
    t_d1 = text(s, datei, (0.95, -0.4), FM, "left", GRAU)
    a_d2 = pf(s, (1.95, 0.35), (2.6, -0.84), knick="hv")
    t_d2 = text(s, datei, (2.27, 0.5), FM, "center", GRAU)
    schritt(s, WACHS(q1[0], 0.6), EIN(q1[1], 0.6))
    s.pause(0.6)
    schritt(s, ZEICHNE(a_nein, 0.7), EIN(t_nein, 0.7))
    schritt(s, WACHS(blaetter[0][0], 0.6), EIN(blaetter[0][1:], 0.6))
    s.pause(0.6)
    schritt(s, ZEICHNE(a_ja, 0.7), EIN(t_ja, 0.7))
    schritt(s, WACHS(q2, 0.6), EIN([q2_t, q2_tt], 0.6))
    s.pause(0.6)
    schritt(s, ZEICHNE(a_bi, 0.7), EIN(t_bi, 0.7))
    schritt(s, WACHS(blaetter[1][0], 0.6), EIN(blaetter[1][1:], 0.6))
    s.pause(0.6)
    schritt(s, ZEICHNE([a_d1, a_d2], 0.7), EIN([t_d1, t_d2], 0.7))
    schritt(s, WACHS([blaetter[2][0], blaetter[3][0]], 0.6), EIN(blaetter[2][1:] + blaetter[3][1:], 0.6))
    s.speichern()


# ================================================================== Abschnitt 5: Schneller arbeiten
def k2tab():
    """unam + Tab → uname; cat /etc/host + Tab Tab → Liste der drei passenden Dateien."""
    s = Szene("linux/k2tab")
    e, x0 = 0.22, -3.2
    ya, yb, yl, yn = 1.1, 0.15, -0.4, -0.8
    za = tt(s, "$ unam", x0, ya, e)
    ka = taste(s, (-2.1, ya), "Tab")
    aa = pf(s, (-1.7, ya), (-1.15, ya))
    ra = tt(s, "$ unam", -1.0, ya, e)
    ra_e = tt(s, "e", sp(-1.0, 6, e), ya, e, GRUEN)
    la = text(s, T(s, "eindeutig", "ein Name passt: ergänzt", "one name fits: completed", "encaja un nombre: completado",
                   "只有一个匹配：补全", "un seul nom : complété", "tek ad uyuyor: tamamlanır"), (0.05, ya), FK, "left", GRUEN)
    zb = tt(s, "$ cat /etc/host", x0, yb, e)
    kb1 = taste(s, (-1.05, yb), "Tab")
    kb2 = taste(s, (-0.35, yb), "Tab")
    liste = tt(s, "host.conf  hostname   hosts", x0, yl, e, GRUEN)
    neu = tt(s, "$ cat /etc/host", x0, yn, e)
    lb = text(s, T(s, "mehrere", "mehrere passen:\nzweimal Tab zeigt alle", "several fit:\nTab twice shows them all",
                   "encajan varios:\ndos veces Tab los muestra", "多个匹配：\n按两次 Tab 全部列出", "plusieurs conviennent :\ndeux fois Tab les montre",
                   "birkaç ad uyuyor:\niki kez Tab hepsini gösterir"), (0.3, (yl + yn) / 2), FK, "left", GRUEN)
    schritt(s, EIN(za, 0.5))
    s.pause(0.4)
    schritt(s, WACHS(ka[0], 0.5), EIN(ka[1], 0.5))
    schritt(s, ZEICHNE(aa, 0.6), EIN([ra, ra_e], 0.6))
    schritt(s, EIN(la, 0.5))
    s.pause(0.6)
    schritt(s, EIN(zb, 0.5))
    schritt(s, WACHS(kb1[0], 0.4), EIN(kb1[1], 0.4))
    schritt(s, WACHS(kb2[0], 0.4), EIN(kb2[1], 0.4))
    schritt(s, EIN([liste, neu], 0.6))
    schritt(s, EIN(lb, 0.5))
    s.speichern()


def k2verlauf():
    """Getippte Zeilen wandern in die Verlaufsliste; die Zeile mit Leerzeichen vorn prallt ab; Pfeil nach oben; exit schreibt die Datei."""
    s = Szene("linux/k2verlauf")
    e, x0 = 0.16, -3.35
    ys_in = (1.2, 0.9, 0.6, 0.3)
    ys_v = (0.85, 0.55, 0.25)
    titel = text(s, T(s, "getippt", "getippt", "typed", "tecleado", "输入", "tapé", "yazılan"), (x0, 1.5), FM, "left", GRAU)
    ein_z = [tt(s, z, x0, y, e) for z, y in zip(("$ whoami", "$ uname -m", "$  echo geheim", "$ history"), ys_in)]
    box = kasten(s, (0.0, 0.65), 2.2, 1.3, fuellung=TERM, form="rect", farbe=GRAU)
    box_t = text(s, T(s, "speicher", "Verlauf im Speicher", "history in memory", "historial en memoria", "内存中的历史记录",
                      "historique en mémoire", "bellekteki geçmiş"), (0.0, 1.13), FM, "center", GRAU)
    hl = s.box("", (0.0, ys_v[2]), breite=2.0, hoehe=0.27, form="rect", farbe=ORANGE, fuellung=WEISS, deckung=0, dicke=2.5)
    nummern = [tt(s, str(i + 1), -0.95, y, e) for i, y in enumerate(ys_v)]
    chips = [tt(s, c, sp(x0, 2, e), y, e, BLAU) for c, y in (("whoami", ys_in[0]), ("uname -m", ys_in[1]), ("history", ys_in[3]))]
    ziele = [(-0.6 + n * cw(e) / 2, y) for n, y in zip((6, 8, 7), ys_v)]
    geheim = tt(s, "echo geheim", sp(x0, 3, e), ys_in[2], e, ROT)
    xg = sp(x0, 3, e) + 11 * cw(e) / 2
    kreuz = s.kreuzchen(None, -1.9, ys_in[2], farbe=ROT, groesse=0.18)
    l_geh = text(s, T(s, "leervorn", "Leerzeichen vorn:\nnicht aufgenommen", "leading space:\nnot recorded",
                      "espacio inicial:\nno se guarda", "开头有空格：\n不记录", "espace au début :\nnon enregistré",
                      "başta boşluk:\nkaydedilmez"), (x0, -0.15), FM, "left", ROT)
    l_hoch = text(s, T(s, "hoch", "↑ holt ältere Zeilen zurück", "↑ brings back older lines", "↑ recupera líneas anteriores",
                       "↑ 取回较早的行", "↑ rappelle les lignes précédentes", "↑ eski satırları geri getirir"), (0.0, -0.2), FM,
                  "center", ORANGE)
    datei = kasten(s, (2.55, 0.65), 1.65, 1.3, fuellung=WEISS, form="rect", farbe=GRAU)
    datei_t = tt(s, "~/.bash_history", 2.55, 1.13, 0.13, anker="m")
    datei_z = [tt(s, z, 1.85, y, 0.14, DUNKEL) for z, y in zip(("whoami", "uname -m", "history"), ys_v)]
    a_exit = pf(s, (1.1, 0.65), (1.725, 0.65))
    t_exit = text(s, T(s, "beiexit", "bei exit", "on exit", "al salir", "exit 时", "à exit", "exit’te"), (1.41, 0.82), FM)
    schritt(s, EIN([titel] + ein_z, 0.6))
    schritt(s, WACHS(box[0], 0.6), EIN(box_t, 0.6))
    s.pause(0.6)
    for i in range(2):
        schritt(s, EIN(chips[i], 0.2))
        schritt(s, ZU(chips[i], *ziele[i], 0.7), EIN(nummern[i], 0.7))
    schritt(s, EIN(geheim, 0.2))
    schritt(s, ZU(geheim, -1.1 - 11 * cw(e) / 2, ys_in[2], 0.5))
    schritt(s, ZU(geheim, xg, ys_in[2], 0.4))
    schritt(s, AUS(geheim, 0.4), EIN([kreuz, l_geh], 0.4))
    schritt(s, EIN(chips[2], 0.2))
    schritt(s, ZU(chips[2], *ziele[2], 0.7), EIN(nummern[2], 0.7))
    s.pause(0.6)
    schritt(s, EIN([hl, l_hoch], 0.5))
    schritt(s, ZU(hl, 0.0, ys_v[1], 0.5))
    s.pause(0.6)
    schritt(s, ZEICHNE(a_exit, 0.6), EIN(t_exit, 0.6), WACHS(datei[0], 0.6), EIN(datei_t, 0.6))
    schritt(s, EIN(datei_z, 0.6))
    s.speichern()


def k2rsuche():
    """Rückwärtssuche: u, n grenzen ein (Treffer uname -m), ein weiteres Strg+R springt zu uname -r."""
    s = Szene("linux/k2rsuche")
    e, x0 = 0.16, -2.95
    ys = (1.17, 0.9, 0.63, 0.36)
    box = kasten(s, (-1.65, 0.85), 2.9, 1.45, fuellung=TERM, form="rect", farbe=GRAU)
    titel = text(s, T(s, "verlauf", "Verlauf", "history", "historial", "历史记录", "historique", "geçmiş"), (-1.65, 1.45), FM,
                 "center", GRAU)
    hl = s.box("", (-1.65, ys[2]), breite=2.7, hoehe=0.25, form="rect", farbe=ORANGE, fuellung=WEISS, deckung=0, dicke=2.5)
    eintr = [tt(s, z, x0, y, e) for z, y in zip(("1  uname -r", "2  whoami", "3  uname -m", "4  head -n 1 /etc/os-release"), ys)]
    a = pf(s, (0.05, ys[3]), (0.05, ys[0]), farbe=ORANGE)
    a_t = text(s, T(s, "richtung", "sucht von der jüngsten\nzur ältesten Zeile", "searches from the newest\nto the oldest line",
                    "busca de la línea más reciente\na la más antigua", "从最新的一行\n查到最旧的一行",
                    "cherche de la ligne la plus récente\nà la plus ancienne", "en yeni satırdan\nen eskiye arar"),
               (0.2, (ys[0] + ys[3]) / 2), FM, "left", ORANGE)
    # Suchzeile in Stücken, die ein- und ausblenden (Umformen ganzer Zeilen kostet je Bild alle Glyphen)
    es, ysu = 0.17, -0.35
    vorn = tt(s, "(reverse-i-search)`", x0, ysu, es)
    q = [tt(s, z, sp(x0, 19, es), ysu, es) for z in ("':", "u':", "un':")]
    r = [tt(s, "uname -m", sp(x0, 23, es), ysu, es), tt(s, "uname -m", sp(x0, 24, es), ysu, es),
         tt(s, "uname -r", sp(x0, 24, es), ysu, es)]
    strg_r = T(s, "strgr", "Strg+R", "Ctrl+R", "Ctrl+R", "Ctrl+R", "Ctrl+R", "Ctrl+R")
    k1 = taste(s, (-2.55, -0.85), strg_r, 0.85)
    ku = taste(s, (-1.75, -0.85), "u", 0.4)
    kn = taste(s, (-1.2, -0.85), "n", 0.4)
    k2 = taste(s, (-0.35, -0.85), strg_r, 0.85)
    schritt(s, WACHS(box[0], 0.6), EIN([titel] + eintr, 0.6))
    schritt(s, ZEICHNE(a, 0.6), EIN(a_t, 0.6))
    s.pause(0.6)
    schritt(s, WACHS(k1[0], 0.5), EIN([k1[1], vorn, q[0]], 0.5))
    schritt(s, WACHS(ku[0], 0.8), EIN([ku[1], q[1], r[0], hl], 0.8), AUS(q[0], 0.4))
    schritt(s, WACHS(kn[0], 0.8), EIN([kn[1], q[2], r[1]], 0.8), AUS([q[1], r[0]], 0.4))
    s.pause(0.6)
    schritt(s, WACHS(k2[0], 0.9), EIN([k2[1], r[2]], 0.9), AUS(r[1], 0.5), ZU(hl, -1.65, ys[0], 0.9))
    s.speichern()


def k2strgcd():
    """Strg+C wird im Kernel zur Unterbrechung an sleep 30; Strg+D wird zum Lesen mit 0 Zeichen an cat."""
    s = Szene("linux/k2strgcd")
    xs = (-2.65, -0.95, 0.8, 2.6)
    yl = (0.6, -0.55)
    kern = flaeche(s, 0.0, -1.1, 1.6, 1.85, BLAU_HELL)
    trenn = [linie(s, (x, 1.85), (x, -1.1), HELLGRAU, 2, DASH) for x in (-1.8, 1.7)]
    koepfe = [text(s, t, (x, 1.55), FM, "center", GRAU) for t, x in zip(
        (T(s, "tast", "Tastatur", "keyboard", "teclado", "键盘", "clavier", "klavye"),
         T(s, "emu", "Terminal-\nemulator", "terminal\nemulator", "emulador\nde terminal", "终端\n模拟器", "émulateur\nde terminal",
           "uçbirim\nöykünücüsü"),
         T(s, "kpty", "Kernel\n(Pseudoterminal)", "kernel\n(pseudoterminal)", "núcleo\n(pseudoterminal)", "内核\n（伪终端）",
           "noyau\n(pseudo-terminal)", "çekirdek\n(sözde uçbirim)"),
         T(s, "prog", "Programm", "program", "programa", "程序", "programme", "program")), xs)]
    p1 = kasten(s, (xs[3], yl[0]), 1.1, 0.36, fuellung=WEISS, form="rect", farbe=GRAU, dicke=2)
    p1_tt = tt(s, "sleep 30", xs[3], yl[0], 0.16, anker="m")
    p2 = kasten(s, (xs[3], yl[1]), 1.1, 0.36, fuellung=WEISS, form="rect", farbe=GRAU, dicke=2)
    p2_tt = tt(s, "cat", xs[3], yl[1], 0.16, anker="m")
    laeufe = []
    for y, taste_t, zeichen, mitte, ende, farbe in (
            (yl[0], T(s, "strgc", "Strg+C", "Ctrl+C", "Ctrl+C", "Ctrl+C", "Ctrl+C", "Ctrl+C"),
             T(s, "nr3", "Zeichen\nNr. 3", "character\nno. 3", "carácter\nn.º 3", "字符\n编号 3", "caractère\nn° 3", "karakter\nno. 3"),
             T(s, "unterbr", "Unterbrechung", "interrupt", "interrupción", "中断", "interruption", "kesme"),
             T(s, "brichtab", "bricht ab", "stops", "se interrumpe", "中止", "s’arrête", "durur"), ROT),
            (yl[1], T(s, "strgd", "Strg+D", "Ctrl+D", "Ctrl+D", "Ctrl+D", "Ctrl+D", "Ctrl+D"),
             T(s, "nr4", "Zeichen\nNr. 4", "character\nno. 4", "carácter\nn.º 4", "字符\n编号 4", "caractère\nn° 4", "karakter\nno. 4"),
             T(s, "null", "Lesen liefert\n0 Zeichen", "read returns\n0 characters", "la lectura da\n0 caracteres", "读取返回\n0 个字符",
               "la lecture rend\n0 caractère", "okuma\n0 karakter verir"),
             T(s, "endetselbst", "endet selbst", "ends by itself", "termina por sí solo", "自行结束", "se termine de lui-même",
               "kendisi biter"), DUNKEL)):
        k = taste(s, (xs[0], y), taste_t, 1.0, 0.36)
        a1 = pf(s, (-2.12, y), (-1.35, y))
        z = text(s, zeichen, (xs[1], y), FM)
        a2 = pf(s, (-0.55, y), (0.36, y))
        m = text(s, mitte, (xs[2], y), FM, "center", ORANGE if farbe == ROT else BLAU)
        if farbe == ROT:
            a3 = [linie(s, (1.26, y), (1.5, y + 0.12), ORANGE, 4), linie(s, (1.5, y + 0.12), (1.58, y - 0.08), ORANGE, 4),
                  pf(s, (1.58, y - 0.08), (2.02, y), farbe=ORANGE, dicke=4)]
        else:
            a3 = [pf(s, (1.26, y), (2.02, y))]
        schl = schleier(s, (xs[3], y), 1.16, 0.42, 0.6)
        e = text(s, ende, (xs[3], y - 0.34), FM, "center", farbe)
        laeufe.append((k, a1, z, a2, m, a3, schl, e))
    schritt(s, EIN([kern] + trenn + koepfe, 0.6))
    schritt(s, WACHS([p1[0], p2[0]], 0.6), EIN([p1_tt, p2_tt], 0.6))
    for k, a1, z, a2, m, a3, schl, e in laeufe:
        s.pause(0.6)
        schritt(s, WACHS(k[0], 0.4), EIN(k[1], 0.4))
        schritt(s, ZEICHNE(a1, 0.5), EIN(z, 0.5))
        schritt(s, ZEICHNE(a2, 0.5), EIN(m, 0.5))
        schritt(s, ZEICHNE(a3, 0.6))
        schritt(s, EIN([schl, e], 0.6))
    s.speichern()


def k2tasten():
    """Befehlszeile mit Cursor in der Mitte; Strg+A/E springen, Strg+U/K/W löschen, nacheinander hervorgehoben."""
    s = Szene("linux/k2tasten")
    e, y = 0.26, 0.0
    x0 = -27 * cw(e) / 2
    xs, xc, xe, xw = sp(x0, 2, e), sp(x0, 10, e), sp(x0, 27, e), sp(x0, 7, e)
    rot = [mark(s, a, b, y, 0.3, ROT, 0.25) for a, b in ((xs, xc), (xc, xe), (xw, xc))]
    pr = tt(s, "$", x0, y, e, GRAU)
    zeile = tt(s, "unme -n 2 /etc/os-release", xs, y, e)
    cursor = linie(s, (xc, y - 0.17), (xc, y + 0.19), ORANGE, 4)
    l_cur = text(s, T(s, "cursor", "Cursor", "cursor", "cursor", "光标", "curseur", "imleç"), (xc, 0.3), FM, "center", ORANGE)
    a_a = pf(s, (xc, 0.52), (xs, 0.52), farbe=BLAU)
    t_a = text(s, T(s, "anf", "Strg+A: an den Anfang", "Ctrl+A: to the start", "Ctrl+A: al principio", "Ctrl+A：到行首",
                    "Ctrl+A : au début", "Ctrl+A: başa"), ((xs + xc) / 2, 0.75), FM, "center", BLAU)
    a_e = pf(s, (xc, 0.52), (xe, 0.52), farbe=BLAU)
    t_e = text(s, T(s, "end", "Strg+E: an das Ende", "Ctrl+E: to the end", "Ctrl+E: al final", "Ctrl+E：到行尾", "Ctrl+E : à la fin",
                    "Ctrl+E: sona"), ((xc + xe) / 2, 0.75), FM, "center", BLAU)
    k_u = klammer(s, xs, xc - 0.02, -0.3, farbe=ROT)
    t_u = text(s, T(s, "u", "Strg+U:\nlinks löschen", "Ctrl+U:\ndelete left", "Ctrl+U:\nborrar a la izquierda", "Ctrl+U：\n删除左边",
                    "Ctrl+U :\neffacer à gauche", "Ctrl+U:\nsolu sil"), ((xs + xc) / 2, -0.52), FM, "center", ROT)
    k_k = klammer(s, xc + 0.02, xe, -0.3, farbe=ROT)
    t_k = text(s, T(s, "k", "Strg+K:\nrechts löschen", "Ctrl+K:\ndelete right", "Ctrl+K:\nborrar a la derecha", "Ctrl+K：\n删除右边",
                    "Ctrl+K :\neffacer à droite", "Ctrl+K:\nsağı sil"), ((xc + xe) / 2, -0.52), FM, "center", ROT)
    k_w = klammer(s, xw, xc - 0.02, -0.92, farbe=ROT)
    t_w = text(s, T(s, "w", "Strg+W: Wort davor löschen", "Ctrl+W: delete the word before", "Ctrl+W: borrar la palabra anterior",
                    "Ctrl+W：删除前一个词", "Ctrl+W : effacer le mot précédent", "Ctrl+W: önceki sözcüğü sil"),
               ((xw + xc) / 2, -1.12), FM, "center", ROT)
    schritt(s, EIN([pr, zeile, cursor, l_cur], 0.6))
    s.pause(0.6)
    schritt(s, ZEICHNE(a_a, 0.7), EIN(t_a, 0.7))
    schritt(s, ZEICHNE(a_e, 0.7), EIN(t_e, 0.7))
    for m_, k, t in ((rot[0], k_u, t_u), (rot[1], k_k, t_k), (rot[2], k_w, t_w)):
        s.pause(0.5)
        schritt(s, EIN(m_, 0.4), ZEICHNE(k, 0.7), EIN(t, 0.7))
        schritt(s, AUS(m_, 0.4))
    s.speichern()


# ================================================================== Abschnitt 6: Das System erkunden
def k2uname():
    """Ausgabe von uname -a, umbrochen und zerlegt."""
    s = Szene("linux/k2uname")
    e = 0.2
    x0 = -51 * cw(e) / 2
    cmd = tt(s, "$ uname -a", x0, 1.85, 0.17, GRAU)
    z1 = tt(s, "Linux labor 6.6.87.2-microsoft-standard-WSL2", x0, 1.45, e)
    z2 = tt(s, "#1 SMP PREEMPT_DYNAMIC Thu Jun  5 18:30:46 UTC 2025", x0, 0.5, e)
    z3 = tt(s, "x86_64 GNU/Linux", x0, -0.4, e)
    teile = []
    for (a, b, yk, yt, t) in (
            (0, 4, 1.24, 1.04, T(s, "kname", "Kernelname", "kernel name", "nombre del núcleo", "内核名称", "nom du noyau",
                                 "çekirdek adı")),
            (6, 10, 1.24, 0.8, T(s, "rname", "Rechnername", "host name", "nombre del equipo", "主机名", "nom de la machine",
                                 "bilgisayar adı")),
            (12, 43, 1.24, 1.04, T(s, "kver", "Kernelversion", "kernel version", "versión del núcleo", "内核版本",
                                   "version du noyau", "çekirdek sürümü")),
            (0, 50, 0.29, 0.09, T(s, "bau", "Angaben zum Bau des Kernels, mit Datum", "details of the kernel build, with date",
                                  "datos de la compilación del núcleo, con fecha", "内核构建信息，含日期",
                                  "informations sur la compilation du noyau, avec date", "çekirdeğin derlenme bilgileri, tarihle")),
            (0, 5, -0.61, -0.81, T(s, "cpu", "Prozessortyp", "processor type", "tipo de procesador", "处理器类型",
                                   "type de processeur", "işlemci türü")),
            (7, 15, -0.61, -1.05, T(s, "os", "Betriebssystem", "operating system", "sistema operativo", "操作系统",
                                    "système d’exploitation", "işletim sistemi"))):
        k = klammer(s, sp(x0, a, e) + 0.02, sp(x0, b + 1, e) - 0.02, yk)
        if yt < yk - 0.3:
            k.append(linie(s, (msp(x0, a, b, e), yk), (msp(x0, a, b, e), yt + 0.1), GRAU, 1.5))
        teile.append((k, text(s, t, (msp(x0, a, b, e), yt), FK)))
    schritt(s, EIN([cmd, z1, z2, z3], 0.7))
    s.pause(0.6)
    for i, (k, t) in enumerate(teile):
        schritt(s, ZEICHNE(k, 0.5), EIN(t, 0.5))
        if i in (2, 3):
            s.pause(0.4)
    s.speichern()


def k2id():
    """Ausgabe von id zerlegt; die Gruppe sudo hervorgehoben."""
    s = Szene("linux/k2id")
    e = 0.185
    z = "uid=1000(student) gid=1000(student) groups=1000(student),27(sudo)"
    x0 = -len(z) * cw(e) / 2
    m_sudo = mark(s, sp(x0, 60, e), sp(x0, 64, e), 0.2, 0.28, ORANGE, 0.35)
    cmd = tt(s, "$ id", x0, 0.65, 0.17, GRAU)
    zeile = tt(s, z, x0, 0.2, e)
    teile = []
    for a, b, t in ((0, 16, T(s, "uid", "Benutzernummer\nund Name", "user ID\nand name", "número de usuario\ny nombre",
                              "用户编号\n和名称", "numéro d’utilisateur\net nom", "kullanıcı numarası\nve adı")),
                    (18, 34, T(s, "gid", "Hauptgruppe", "primary group", "grupo principal", "主组", "groupe principal",
                               "birincil grup")),
                    (36, 64, T(s, "groups", "alle Gruppen", "all groups", "todos los grupos", "所有组", "tous les groupes",
                               "tüm gruplar"))):
        teile.append((klammer(s, sp(x0, a, e) + 0.02, sp(x0, b + 1, e) - 0.02, -0.02), text(s, t, (msp(x0, a, b, e), -0.3), FK)))
    xm = msp(x0, 60, 63, e)
    a = pf(s, (xm, 0.6), (xm, 0.36), farbe=ORANGE)
    t_s = text(s, T(s, "sudo", "Gruppe sudo: Erlaubnis für\nBefehle als root", "group sudo: permission for\ncommands as root",
                    "grupo sudo: permiso para\ncomandos como root", "sudo 组：\n允许以 root 身份执行命令",
                    "groupe sudo : droit d’exécuter\ndes commandes en root", "sudo grubu: root olarak\nkomut çalıştırma izni"),
               (3.35, 0.85), FK, "right", ORANGE)
    schritt(s, EIN([cmd, zeile], 0.6))
    s.pause(0.6)
    for k, t in teile:
        schritt(s, ZEICHNE(k, 0.5), EIN(t, 0.5))
    s.pause(0.6)
    schritt(s, EIN([m_sudo, t_s], 0.8), ZEICHNE(a, 0.8))
    s.speichern()


def k2uptime():
    """Ausgabe von uptime zerlegt; daneben die drei Lastwerte als Balken vor der Linie bei 14 Kernen."""
    s = Szene("linux/k2uptime")
    e = 0.185
    z = " 00:31:31 up 1 min,  1 user,  load average: 2.47, 0.87, 0.31"
    x0 = -len(z) * cw(e) / 2
    cmd = tt(s, "$ uptime", x0, 1.8, 0.17, GRAU)
    zeile = tt(s, z, x0, 1.4, e)
    teile = []
    for a, b, t in ((1, 8, T(s, "zeit", "Uhrzeit", "time", "hora", "时间", "heure", "saat")),
                    (10, 17, T(s, "lauf", "Laufzeit", "uptime", "tiempo activo", "运行时间", "durée", "çalışma süresi")),
                    (21, 26, T(s, "ben", "Benutzer", "users", "usuarios", "用户", "utilisateurs", "kullanıcılar")),
                    (30, 59, T(s, "last", "Last: Mittel über 1, 5, 15 Minuten", "load: average over 1, 5, 15 minutes",
                               "carga: media de 1, 5 y 15 minutos", "负载：1、5、15 分钟的平均值", "charge : moyenne sur 1, 5, 15 minutes",
                               "yük: 1, 5, 15 dakikalık ortalama"))):
        teile.append((klammer(s, sp(x0, a, e) + 0.02, sp(x0, b + 1, e) - 0.02, 1.18), text(s, t, (msp(x0, a, b, e), 0.98), FK)))
    x_null, k = -1.6, 4.6 / 14
    achse = linie(s, (x_null, 0.55), (x_null, -0.55), GRAU, 2)
    kerne = linie(s, (x_null + 14 * k, 0.55), (x_null + 14 * k, -0.55), GRUEN, 3, DASH)
    t_kerne = text(s, T(s, "kerne", "14 Kerne (nproc)", "14 cores (nproc)", "14 núcleos (nproc)", "14 个核心（nproc）",
                        "14 cœurs (nproc)", "14 çekirdek (nproc)"), (3.35, -0.75), FM, "right", GRUEN)
    t_titel = text(s, T(s, "vergleich", "Last im Vergleich zu den Kernen", "load compared with the cores",
                        "carga comparada con los núcleos", "负载与核心数对比", "charge comparée aux cœurs",
                        "çekirdeklere göre yük"), (x_null, 0.7), FM, "left", GRAU)
    balken = []
    for (wert, txt, y, lab) in ((2.47, T(s, "v1", "2,47", "2.47", "2,47", "2.47", "2,47", "2,47"), 0.35, "1 min"),
                                (0.87, T(s, "v2", "0,87", "0.87", "0,87", "0.87", "0,87", "0,87"), 0.0, "5 min"),
                                (0.31, T(s, "v3", "0,31", "0.31", "0,31", "0.31", "0,31", "0,31"), -0.35, "15 min")):
        b = linie(s, (x_null, y), (x_null + wert * k, y), BLAU, 14)
        balken.append((b, text(s, txt, (x_null + wert * k + 0.12, y), FM, "left", BLAU),
                       text(s, lab, (x_null - 0.12, y), FM, "right", GRAU)))
    schritt(s, EIN([cmd, zeile], 0.6))
    s.pause(0.6)
    for kl, t in teile:
        schritt(s, ZEICHNE(kl, 0.5), EIN(t, 0.5))
    s.pause(0.6)
    schritt(s, EIN([achse, t_titel], 0.6), ZEICHNE(kerne, 0.6), EIN(t_kerne, 0.6))
    for b, wt, lab in balken:
        schritt(s, ZEICHNE(b, 0.6), EIN([wt, lab], 0.6))
    s.speichern()


def k2free():
    """free -h als Tabelle; darunter ein schematischer Balken (belegt, Zwischenspeicher, frei) mit Klammer für available."""
    s = Szene("linux/k2free")
    e = 0.16
    kopf = "               total        used        free      shared  buff/cache   available"
    mem = "Mem:            31Gi       765Mi        30Gi       3.5Mi       429Mi        30Gi"
    swap = "Swap:          8.0Gi          0B       8.0Gi"
    x0 = -len(kopf) * cw(e) / 2
    yk, ym, ysw = 1.55, 1.3, 1.05

    def spalte(wort):
        ende = kopf.index(wort) + len(wort)
        anf = min(kopf.index(wort), ende - 6)
        return sp(x0, anf, e) - 0.03, sp(x0, ende, e) + 0.03
    hl = {w: mark(s, *spalte(w), (yk + ym) / 2, 0.5, f, 0.25) for w, f in
          (("used", ORANGE), ("buff/cache", BLAU), ("free", GRUEN))}
    xa0, xa1 = spalte("available")
    av = s.box("", ((xa0 + xa1) / 2, (yk + ym) / 2), breite=xa1 - xa0, hoehe=0.5, form="rect", farbe=GRUEN, fuellung=WEISS,
               deckung=0, dicke=2.5, dash=DASH)
    cmd = tt(s, "$ free -h", x0, 1.85, 0.17, GRAU)
    tab = [tt(s, kopf, x0, yk, e), tt(s, mem, x0, ym, e), tt(s, swap, x0, ysw, e)]
    yb, hb = -0.15, 0.42
    seg = [kasten(s, ((a + b) / 2, yb), b - a, hb, fuellung=f, form="rect", farbe=GRAU, dicke=1.5)[0] for a, b, f in
           ((-3.0, -2.0, "#f6c3a8"), (-2.0, -0.9, "#bcd6f3"), (-0.9, 3.0, "#bfe3cb"))]
    t_used = text(s, T(s, "used", "belegt (used)\n765 MiB", "used\n765 MiB", "en uso (used)\n765 MiB", "已用（used）\n765 MiB",
                       "utilisé (used)\n765 Mio", "kullanılan (used)\n765 MiB"), (-2.5, -0.65), FM)
    t_cache = text(s, T(s, "cache", "Zwischenspeicher\n(buff/cache) 429 MiB", "cache\n(buff/cache) 429 MiB",
                        "caché\n(buff/cache) 429 MiB", "缓存\n（buff/cache）429 MiB", "cache\n(buff/cache) 429 Mio",
                        "önbellek\n(buff/cache) 429 MiB"), (-1.2, -0.65), FM)
    t_free = text(s, T(s, "frei", "frei (free) 30 GiB", "free 30 GiB", "libre (free) 30 GiB", "空闲（free）30 GiB",
                       "libre (free) 30 Gio", "boş (free) 30 GiB"), (1.05, yb), FM)
    k_av = klammer(s, -1.75, 3.0, 0.22, unten=False, farbe=GRUEN)
    t_av = text(s, T(s, "avail", "verfügbar (available): 30 GiB", "available: 30 GiB", "disponible (available): 30 GiB",
                     "可用（available）：30 GiB", "disponible (available) : 30 Gio", "kullanılabilir (available): 30 GiB"),
                (0.62, 0.42), FM, "center", GRUEN)
    k_tot = klammer(s, -3.0, 3.0, -1.02, farbe=GRAU)
    t_tot = text(s, T(s, "total", "gesamt (total): 31 GiB", "total: 31 GiB", "total: 31 GiB", "总计（total）：31 GiB",
                      "total : 31 Gio", "toplam (total): 31 GiB"), (0.0, -1.22), FM, "center", GRAU)
    t_nm = text(s, T(s, "schema", "schematisch, nicht maßstäblich", "schematic, not to scale", "esquemático, sin escala",
                     "示意图，未按比例", "schématique, pas à l’échelle", "şematik, ölçekli değil"), (3.35, -1.5), 16, "right", GRAU)
    schritt(s, EIN([cmd] + tab, 0.7))
    s.pause(0.6)
    schritt(s, ZEICHNE(k_tot, 0.6), EIN(t_tot, 0.6))
    schritt(s, WACHS(seg[0], 0.7), EIN([t_used, hl["used"]], 0.7))
    schritt(s, WACHS(seg[1], 0.7), EIN([t_cache, hl["buff/cache"]], 0.7))
    schritt(s, WACHS(seg[2], 0.7), EIN([t_free, hl["free"]], 0.7))
    s.pause(0.6)
    schritt(s, ZEICHNE(k_av, 0.8), EIN([t_av, av], 0.8))
    schritt(s, EIN(t_nm, 0.4))
    s.speichern()


def k2df():
    """Rechenbild: dieselben Byte in Vielfachen von 1024 (df -h) und von 1000 (df -H), aufgerundet."""
    s = Szene("linux/k2df")
    hoehe, cx = 0.55, -0.4
    kopf = text(s, T(s, "kopf", "df -h rechnet mit 1024, df -H mit 1000", "df -h works in 1024s, df -H in 1000s",
                     "df -h calcula con 1024, df -H con 1000", "df -h 按 1024 计算，df -H 按 1000 计算",
                     "df -h compte par 1024, df -H par 1000", "df -h 1024 ile, df -H 1000 ile hesaplar"), (cx, 0.75), FK)
    auf = text(s, T(s, "auf", "aufgerundet", "rounded up", "redondeado hacia arriba", "向上取整", "arrondi au-dessus",
                    "yukarı yuvarlanmış"), (cx + 1.97, 0.43), FM, "center", GRAU)
    l1 = text(s, "df -h", (2.75, 0.143), FK, "left", BLAU)
    l2 = text(s, "df -H", (2.75, -0.198), FK, "left", BLAU)
    schritt(s, EIN([kopf, auf, l1, l2], 0.6))
    s.pause(0.6)
    s.formel(r"\begin{aligned}1\,081\,101\,176\,832\ \mathrm{B} \div 2^{30} &= 1006.85\ \mathrm{GiB} &&\longrightarrow\ "
             r"\texttt{1007G}\\1\,081\,101\,176\,832\ \mathrm{B} \div 10^{12} &= 1.081\ \mathrm{TB} &&\longrightarrow\ "
             r"\texttt{1.1T}\end{aligned}", mitte=(cx, 0.0), hoehe=hoehe, zeilenweise=True, dauer=2.6)
    s.speichern()


# ================================================================== Abschnitt 7: GNU und uutils
def k2coreutils():
    """Raster der Grundbefehle nach Aufgaben: Dateien, Text, System; insgesamt über hundert."""
    s = Szene("linux/k2coreutils")
    rahmen = kasten(s, (0.0, 0.55), 6.8, 2.3, fuellung=WEISS, form="rect", farbe=GRAU, dicke=2)
    titel = tt(s, "coreutils", 0.0, 1.92, 0.24, anker="m")
    spalten = []
    for x, kopf, f, hf, namen in (
            (-2.25, T(s, "dateien", "Dateien", "files", "archivos", "文件", "fichiers", "dosyalar"), BLAU, BLAU_HELL,
             ("ls", "cp", "mv", "rm", "mkdir", "touch")),
            (0.0, T(s, "text", "Text", "text", "texto", "文本", "texte", "metin"), ORANGE, ORANGE_HELL,
             ("cat", "head", "tail", "sort", "wc", "cut")),
            (2.25, T(s, "system", "System", "system", "sistema", "系统", "système", "sistem"), GRUEN, GRUEN_HELL,
             ("uname", "date", "df", "whoami", "id", "nproc"))):
        objs = kasten(s, (x, 1.35), 2.0, 0.36, kopf, FK, fuellung=hf, farbe=f, dicke=2)
        for i, n in enumerate(namen):
            xi, yi = x + (-0.5 if i % 2 == 0 else 0.5), 0.9 - 0.36 * (i // 2)
            objs += [kasten(s, (xi, yi), 0.85, 0.28, fuellung=WEISS, farbe=f, dicke=1.5)[0], tt(s, n, xi, yi, 0.17, anker="m")]
        objs.append(text(s, "…", (x, -0.18), FS, "center", GRAU))
        spalten.append(objs)
    unten = text(s, T(s, "hundert", "über hundert Grundbefehle in einer Sammlung", "over a hundred core commands in one collection",
                      "más de cien comandos básicos en una colección", "一个集合中的一百多个基本命令",
                      "plus de cent commandes de base dans une collection", "tek bir koleksiyonda yüzden fazla temel komut"),
                  (0.0, -0.95), FK)
    schritt(s, WACHS(rahmen, 0.6), EIN(titel, 0.6))
    s.pause(0.6)
    for objs in spalten:
        schritt(s, EIN(objs, 0.8))
    s.pause(0.6)
    schritt(s, EIN(unten, 0.7))
    s.speichern()


def k2zweifassungen():
    """Zwei Werkzeugkästen auf Ubuntu 26.04: uutils (Rust) und GNU coreutils (C); die Namen fliegen in ihre Kästen."""
    s = Szene("linux/k2zweifassungen")
    e = 0.18
    titel = text(s, T(s, "namen", "Befehlsnamen", "command names", "nombres de comandos", "命令名", "noms de commandes",
                      "komut adları"), (0.0, 1.05), FK, "center", GRAU)
    links = kasten(s, (-1.75, -0.2), 3.3, 1.55, fuellung=ORANGE_HELL, form="rect", farbe=ORANGE, dicke=2)
    rechts = kasten(s, (1.75, -0.2), 3.3, 1.55, fuellung=BLAU_HELL, form="rect", farbe=BLAU, dicke=2)
    t_l = text(s, "uutils (Rust)", (-1.75, 0.38), FK, "center", ORANGE)
    t_r = text(s, "GNU coreutils (C)", (1.75, 0.38), FK, "center", BLAU)
    l_unten = text(s, T(s, "meisten", "die meisten Grundbefehle", "most core commands", "la mayoría de los comandos básicos",
                        "大多数基本命令", "la plupart des commandes de base", "temel komutların çoğu"), (-1.75, -0.75), FM, "center",
                   GRAU)
    ziele = {"ls": (-2.9, 0.0), "cat": (-2.25, 0.0), "uname": (-1.5, 0.0), "head": (-0.7, 0.0), "date": (-2.75, -0.38),
             "cp": (0.55, 0.05), "mv": (1.05, 0.05), "rm": (1.55, 0.05), "df": (2.05, 0.05), "true": (2.6, 0.05)}
    chips = {n: tt(s, n, -2.8 + i * 0.62, 0.78, e, anker="m") for i, n in enumerate(ziele)}
    weiter = text(s, "…", (-2.05, -0.38), FS, "center", GRAU)
    trenn = linie(s, (0.25, -0.2), (3.25, -0.2), BLAU, 1.5, DASH)
    l_gnu = text(s, T(s, "vorsilbe", "alle auch mit Vorsilbe gnu:", "all also with the prefix gnu:",
                      "todos también con el prefijo gnu:", "全部也可加前缀 gnu：", "toutes aussi avec le préfixe gnu :",
                      "hepsi gnu ön ekiyle de:"), (0.25, -0.38), FM, "left", BLAU)
    gnu = [tt(s, n, x, -0.7, e, anker="m") for n, x in (("gnuls", 0.65), ("gnucat", 1.35), ("gnuuname", 2.2))]
    gnu.append(text(s, "…", (2.95, -0.7), FS, "center", GRAU))
    schritt(s, EIN(titel, 0.5))
    schritt(s, WACHS([links[0], rechts[0]], 0.7), EIN([t_l, t_r], 0.7))
    s.pause(0.6)
    schritt(s, EIN(list(chips.values()), 0.6))
    s.pause(0.6)
    schritt(s, *[ZU(chips[n], x, y, 1.2) for n, (x, y) in ziele.items()])
    schritt(s, EIN([weiter, l_unten], 0.5))
    s.pause(0.6)
    schritt(s, ZEICHNE(trenn, 0.8), EIN([l_gnu] + gnu, 0.8))
    s.speichern()


def k2fehlermeldung():
    """Dieselbe falsche Option, zwei Antworten: links uutils, rechts GNU; gemeinsame Bedeutung darunter."""
    s = Szene("linux/k2fehlermeldung")
    e = 0.145
    xl, xr = -3.35, 0.1
    pl = kasten(s, (-1.73, 0.88), 3.38, 0.92, fuellung=TERM, form="rect", farbe=GRAU, dicke=2)
    pr = kasten(s, (1.73, 0.88), 3.38, 0.92, fuellung=TERM, form="rect", farbe=GRAU, dicke=2)
    t_l = text(s, "uutils:  uname -x", (-1.73, 1.55), FK, "center", ORANGE)
    t_r = text(s, "GNU coreutils:  gnuuname -x", (1.73, 1.55), FK, "center", BLAU)
    m_l = [mark(s, sp(xl, 0, e), sp(xl, 6, e), 1.17, 0.21, ORANGE, 0.3),
           mark(s, sp(xl, 26, e), sp(xl, 34, e), 0.59, 0.21, ORANGE, 0.3)]
    m_r = [mark(s, sp(xr, 10, e), sp(xr, 24, e), 1.17, 0.21, BLAU, 0.3),
           mark(s, sp(xr, 4, e), sp(xr, 21, e), 0.94, 0.21, BLAU, 0.3)]
    zl = [tt(s, z, xl, y, e) for z, y in (("error: unexpected argument '-x' found", 1.17),
                                          ("Usage: uname [OPTION]...", 0.88), ("For more information, try '--help'.", 0.59))]
    zr = [tt(s, z, xr, y, e) for z, y in (("gnuuname: invalid option -- 'x'", 1.17),
                                          ("Try 'gnuuname --help' for more information.", 0.94))]
    unten = kasten(s, (0.0, -0.12), 5.4, 0.42, T(s, "bedeutung", "beide bedeuten: Die Option -x gibt es nicht.",
                                                 "both mean: the option -x does not exist.",
                                                 "ambos significan: la opción -x no existe.", "两者含义相同：选项 -x 不存在。",
                                                 "les deux signifient : l’option -x n’existe pas.",
                                                 "ikisinin anlamı: -x seçeneği yok."), FK, fuellung=GRUEN_HELL, farbe=GRUEN)
    a_l = pf(s, (-1.73, 0.42), (-1.0, 0.09), farbe=GRUEN)
    a_r = pf(s, (1.73, 0.42), (1.0, 0.09), farbe=GRUEN)
    schritt(s, WACHS(pl, 0.6), EIN(t_l, 0.6))
    schritt(s, EIN(zl, 0.7))
    schritt(s, EIN(m_l, 0.6))
    s.pause(0.6)
    schritt(s, WACHS(pr, 0.6), EIN(t_r, 0.6))
    schritt(s, EIN(zr, 0.7))
    schritt(s, EIN(m_r, 0.6))
    s.pause(0.6)
    schritt(s, ZEICHNE([a_l, a_r], 0.6), WACHS(unten[0], 0.7), EIN(unten[1], 0.7))
    s.speichern()


SZENEN = (k2schichten, k2schleife, k2prompt, k2sitzungen, k2woerter, k2argumente, k2buendeln, k2zerlegt, k2ende, k2suche, k2cd,
          k2alias, k2arten, k2manpage, k2synopsis, k2abschnitte, k2apropos, k2hilfeweg, k2tab, k2verlauf, k2rsuche, k2strgcd,
          k2tasten, k2uname, k2id, k2uptime, k2free, k2df, k2coreutils, k2zweifassungen, k2fehlermeldung)

if __name__ == "__main__":
    for f in SZENEN:
        f()
    print(" ".join("linux/" + f.__name__ for f in SZENEN))
