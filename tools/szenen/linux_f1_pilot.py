"""Pilot der Editor-Welle F1 „Bildschirme und Fenster“ (12.11.2026): drei vorhandene Linux-Szenen zusätzlich mit dem
neuen Terminal bzw. Raster im dunklen, an Ubuntu angelehnten Stil (Namen mit _f1; die Handfassungen bleiben, wie sie
sind) und zwei kleine Vorführszenen für Vollbild-Programme (top, Pager wie bei systemctl status).

    linux/k2sitzungen_f1   zwei Terminalfenster, Prompt wechselt mit cd, exit beendet die Shell links
    linux/k4cateingabe_f1  cat ohne Argument: „Hallo“ getippt, als Kopie zu cat und zurück, Strg+D
    linux/k6awkfelder_f1   eine CSV-Zeile als Raster: Kommas leuchten, Klammern $1..$4, $0, NF, $NF, NR
    beispiel/anim_f1_top   top: Kopf und Prozesstabelle, ein Prozess kommt hinzu, Werte ändern sich
    beispiel/anim_f1_pager systemctl status cron im Pager: ● grün, Baumzeichen, Statuszeile, eine Seite weiter

Anleitung: notizen/animationen.md §11. Die Vorführinhalte stammen aus schreibgeschützten Läufen in der WSL
(top -b -n 1, systemctl status --no-pager cron, 12.11.2026), gekürzt.
Bauen:  python tools/szenen/linux_f1_pilot.py [name …]
Export: python tools/export_szenen.py --animiert linux/k2sitzungen_f1 linux/k4cateingabe_f1 linux/k6awkfelder_f1 \\
        beispiel/anim_f1_top beispiel/anim_f1_pager
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from szenen_lib import *  # noqa: E402,F403
from szenen_lib import farbig  # noqa: E402

from linux_hilfen import *  # noqa: E402,F403

schreibmaschine("text")          # tt/prozess als s.text in Schreibmaschinenschrift
FK, FM = 20, 18


# ================================================================== Kapitel 2: zwei Sitzungen
def k2sitzungen_f1():
    """Zwei Fenster, zwei Shells: links cd /etc und exit, rechts bleibt alles, wie es war."""
    s = Szene("linux/k2sitzungen_f1", reihenfolge="anlegen")
    li = s.terminal(pos=(-3.4, 0.62), spalten=26, zeilen=3)
    re_ = s.terminal(pos=(0.1, 0.62), spalten=26, zeilen=3)
    t1 = text(s, T(s, "f1", "Fenster 1: Sitzung 1", "window 1: session 1", "ventana 1: sesión 1", "窗口 1：会话 1",
                   "fenêtre 1 : session 1", "pencere 1: oturum 1"), (li.mitte[0], 0.84), FK)
    t2 = text(s, T(s, "f2", "Fenster 2: Sitzung 2", "window 2: session 2", "ventana 2: sesión 2", "窗口 2：会话 2",
                   "fenêtre 2 : session 2", "pencere 2: oturum 2"), (re_.mitte[0], 0.84), FK)
    schl = schleier(s, li.mitte, *li.groesse, 0.6)
    ende = text(s, T(s, "beendet", "Shell beendet", "shell has ended", "la shell terminó", "Shell 已结束", "shell terminé",
                     "kabuk sona erdi"), (li.mitte[0], li.unten_kante - 0.25), FK, "center", ROT)
    bleibt = text(s, T(s, "bleibt", "bleibt in ~", "stays in ~", "sigue en ~", "仍在 ~", "reste dans ~", "~ içinde kalır"),
                  (re_.mitte[0], re_.unten_kante - 0.25), FK, "center", GRUEN)
    weiter = text(s, T(s, "weiter", "läuft weiter", "keeps running", "sigue en marcha", "继续运行", "continue de tourner",
                       "çalışmaya devam eder"), (re_.mitte[0], re_.unten_kante - 0.55), FK, "center", GRUEN)
    p_re = re_.teil(0, 0, 16)                        # Kopie des Prompts rechts (farbig, deckungsgleich) zum Betonen
    schritt(s, WACHS([li.id, re_.id], 0.7), EIN([t1, t2], 0.7))
    schritt(s, EIN(p_re, 0.01))
    s.pause(0.4)
    li.befehl("cd /etc", pfad="/etc")
    schritt(s, BETONE(p_re, 0.8), EIN(bleibt, 0.8))
    s.pause(0.6)
    li.schritt("\\e>exit\n\\e[?25l", dauer=0.5)
    schritt(s, EIN([schl, ende], 0.8))
    schritt(s, EIN(weiter, 0.6))
    s.speichern()


# ================================================================== Kapitel 4: cat liest von der Tastatur
def k4cateingabe_f1():
    """cat ohne Argument: Das Terminal zeigt „Hallo“ beim Tippen, schickt die Zeile nach der Eingabetaste über 0 an cat,
    cat schreibt sie über 1 zurück; Strg+D beendet den Strom, cat endet."""
    s = Szene("linux/k4cateingabe_f1", reihenfolge="anlegen")
    t = s.terminal(pos=(-3.4, 1.5), spalten=20, zeilen=4)
    tx = t.mitte[0]
    tast = tastatur(s, tx, -0.55)
    cat = prozess(s, (2.45, 0.0), 1.3, 1.7, "cat", 0.17)
    y1 = t.y(2)                                      # Zeile, in der cats Ausgabe erscheint
    r1 = rohr(s, (1.8, y1), (t.rechts + 0.05, y1), C1)
    r0 = rohr(s, (tx + 0.45, -0.55), (1.8, -0.55), C0)
    n1 = nummer(s, 1.55, y1 + 0.23, 1, C1)
    n0 = nummer(s, 1.55, -0.32, 0, C0)
    l_zeigt = text(s, T(s, "zeigt", "das Terminal zeigt das Getippte an", "the terminal shows what is typed",
                        "el terminal muestra lo tecleado", "终端显示所输入的内容", "le terminal affiche ce qui est tapé",
                        "terminal yazılanı gösterir"), (tx, -1.05), FM, "center", GRAU)
    l_enter = text(s, T(s, "enter", "Eingabetaste", "Enter key", "tecla Intro", "回车键", "touche Entrée", "Enter tuşu"),
                   (0.6, -0.3), FM, "center", C0)
    strgd = text(s, T(s, "strgd", "Strg+D", "Ctrl+D", "Ctrl+D", "Ctrl+D", "Ctrl+D", "Ctrl+D"), (tx, -1.38), FM, "center", ORANGE)
    ende = karte(s, 0.6, -1.0, T(s, "ende", "Ende des Stroms", "end of the stream", "fin del flujo", "流结束", "fin du flux",
                                 "akışın sonu"), 1.6, ORANGE, ORANGE_HELL, FM, ORANGE)
    xm, ya = t.xm(0, 4), t.y(1)                      # „Hallo“ in Zeile 1, Spalten 0..4
    karte_b, karte_h = t.xr(4) - t.x(0) + 0.14, t.zelle[1] + 0.08
    # f1: weiße Karte bei cat; sie landet genau über Zeile 2, wo cats Ausgabe erscheint
    f1 = [s.box("", (1.4, y1), breite=karte_b, hoehe=karte_h, form="round", farbe=GRAU, fuellung=WEISS, dicke=1.5),
          s.text(None, "Hallo", (1.4, y1), t._groesse(), "center", SCHWARZ, schrift="tt")]
    g = geist(s, (2.45, 0.0), 1.3, 1.7)
    g_name = tt(s, "cat", 2.45, 0.0, 0.17, HELLGRAU, "m")
    g_t = text(s, w_beendet(s), (2.45, -0.4), FM, "center", GRAU)
    schritt(s, WACHS(t.id, 0.6), EIN(tast, 0.6))
    t.eingabe("cat")
    schritt(s, WACHS(cat[0], 0.5), EIN(cat[1], 0.5))
    schritt(s, ZEICHNE([r1, r0], 0.6), EIN(n1 + n0, 0.6))
    with s.gleichzeitig():
        t.tippen("Hallo")
        s.einblenden(l_zeigt)
    # f0: dieselbe Karte genau über der getippten Zeile, darin die deckungsgleiche Kopie der Zeichen (Teil löst sich);
    # erst jetzt anlegen: teil liest den Bildschirm nach den bisherigen Schritten
    f0 = [s.box("", (xm, ya), breite=karte_b, hoehe=karte_h, form="round", farbe=GRAU, fuellung=WEISS, dicke=1.5),
          t.teil(1, 0, 4, farbe=SCHWARZ)]
    s.pause(0.4)
    with s.gleichzeitig():
        t.schritt("\n", dauer=0.4)                   # Eingabetaste
        s.einblenden(l_enter, *f0, dauer=0.4)
    schritt(s, *VERS(f0, 1.4 - xm, -0.55 - ya, 0.9))
    schritt(s, AUS(f0, 0.3), EIN(f1, 0.3))
    schritt(s, *VERS(f1, xm - 1.4, 0.0, 0.9))
    with s.gleichzeitig():
        s.ausblenden(*f1, dauer=0.3)
        t.ausgabe("Hallo", dauer=0.3)
    s.pause(0.5)
    schritt(s, EIN(strgd, 0.5))
    schritt(s, WACHS(ende[0], 0.5), EIN(ende[1], 0.5))
    schritt(s, AUS(cat, 0.6), EIN([g, g_name, g_t], 0.6))
    t.prompt()
    s.speichern()


# ================================================================== Kapitel 6: awk zerlegt eine Zeile in Felder
LAUF = "2026-11-08,Ben,21.1,128"


def k6awkfelder_f1():
    """2026-11-08,Ben,21.1,128 mit -F,: $1 bis $4 über den Feldern, ein Bogen $0 über der ganzen Zeile; rechts NF = 4,
    $NF zeigt auf das letzte Feld; links NR = 9."""
    s = Szene("linux/k6awkfelder_f1", reihenfolge="anlegen")
    g = s.raster(LAUF, (0, -0.05), groesse=26, ausrichtung="mitte", zeilenabstand=1.85)
    fl, kommas = g.felder(0, ","), g.trenner(0, ",")
    mk = [g.markieren(0, k, k, ORANGE, 0.4) for k in kommas]
    tk = [g.teil(0, k, k) for k in kommas]                       # Kopien der Kommas: leuchten einzeln
    t_F = s.text(None, "-F,", (-3.3, 1.55), 22.4, "left", schrift="tt")
    l_F = text(s, T(s, "F", "Trennzeichen: Komma", "separator: comma", "separador: coma", "分隔符：逗号",
                    "séparateur : virgule", "ayırıcı: virgül"), (-2.9, 1.55), FM, "left", ORANGE)
    kl = [g.klammer(0, f.a, f.b, "$%d" % (j + 1), farbe=BLAU, groesse=22.4, abstand=0.0, tiefe=0.06, schrift="tt")
          for j, f in enumerate(fl)]
    x0, x1 = g.x(0) - 0.04, g.xr(len(LAUF) - 1) + 0.04
    arc = s.weg(None, "%s+%s*t" % (round(x0, 4), round(x1 - x0, 4)), "%s+0.32*4*t*(1-t)" % round(g.y(0) + 0.66, 4), 0, 1,
                farbe=BLAU, dicke=2.5, n=41)
    t0 = s.text(None, "$0", (0, round(g.y(0) + 1.15, 4)), 22.4, "center", BLAU, schrift="tt")
    xr = g.rechts + 0.25
    t_nf = s.text(None, "NF = 4", (xr, g.y(0)), 22.4, "left", schrift="tt")
    l_nf = text(s, T(s, "nf", "Zahl der Felder", "number of fields", "número de campos", "字段数", "nombre de champs",
                     "alan sayısı"), (xr, g.y(0) - 0.32), FM, "left", GRAU)
    x4 = g.xm(fl[3].a, fl[3].b)
    a_nf = pf(s, (x4, g.unten(0) - 0.5), (x4, g.unten(0) - 0.06), farbe=BLAU, spitze=0.08)
    t_dnf = s.text(None, "$NF", (x4, g.unten(0) - 0.65), 22.4, "center", BLAU, schrift="tt")
    l_dnf = text(s, T(s, "dnf", "das letzte Feld", "the last field", "el último campo", "最后一个字段", "le dernier champ",
                      "son alan"), (x4 + 0.3, g.unten(0) - 0.65), FM, "left", GRAU)
    xl = g.links - 0.25
    t_nr = s.text(None, "NR = 9", (xl, g.y(0)), 22.4, "right", schrift="tt")
    l_nr = text(s, T(s, "nr", "Zeilennummer", "line number", "número de línea", "行号", "numéro de ligne",
                     "satır numarası"), (xl, g.y(0) - 0.32), FM, "right", GRAU)
    schritt(s, EIN(g.ids + tk + [t_F, l_F], 0.6))
    schritt(s, EIN(mk, 0.6), BETONE(tk, 0.7))
    s.pause(0.6)
    for k, t in kl:
        schritt(s, ZEICHNE(k, 0.45), EIN(t, 0.45))
    s.pause(0.6)
    schritt(s, ZEICHNE(arc, 0.7), EIN(t0, 0.6))
    s.pause(0.6)
    schritt(s, EIN([t_nf, l_nf], 0.5))
    schritt(s, ZEICHNE(a_nf, 0.6), EIN([t_dnf, l_dnf], 0.6), BETONE(kl[3][1], 0.8))
    s.pause(0.6)
    schritt(s, EIN([t_nr, l_nr], 0.5))
    s.speichern()


# ================================================================== Vorführung: top
KOPF = ["top - 00:04:48 up 0 min,  1 user,  load average: 0.24, 0.05, 0.02",
        "Tasks:  73 total,   1 running,  72 sleeping,   0 stopped,   0 zombie",
        "%Cpu(s):  0.0 us,  0.0 sy,  0.0 ni,100.0 id,  0.0 wa,  0.0 hi,  0.0 si,  0.0 st",
        "MiB Mem :  31846.7 total,  30927.2 free,    741.4 used,    486.3 buff/cache",
        "MiB Swap:   8192.0 total,   8192.0 free,      0.0 used.  31105.3 avail Mem"]
SPALTEN = "    PID USER      PR  NI    VIRT    RES    SHR S  %CPU  %MEM     TIME+ COMMAND"
PROZ = ["      1 root      20   0   24512  14592  11008 S   0.0   0.0   0:01.28 systemd",
        "     46 root      19  -1   42060  15752  14728 S   0.0   0.0   0:00.26 systemd-journal",
        "     83 systemd+  20   0   22412  13952  11520 S   0.0   0.0   0:00.13 systemd-resolve",
        "    112 root      20   0    4464   2816   2688 S   0.0   0.0   0:00.01 cron",
        "    113 message+  20   0    8784   4864   4352 S   0.0   0.0   0:00.11 dbus-daemon",
        "    245 student   20   0    9216   5376   3584 S   0.0   0.0   0:00.04 bash"]
YES = "    301 student   20   0    5616   1792   1664 R  %s   0.0   %s yes"


def anim_f1_top():
    """top im Vollbild: Kopf mit fetten Zahlen, Spaltenzeile invers; ein Prozess (yes) kommt hinzu und rechnet, Last und
    Zeit laufen weiter (drei Bilder, je ein Schritt)."""
    s = Szene("beispiel/anim_f1_top", reihenfolge="anlegen")
    top = s.top(KOPF, [SPALTEN] + PROZ, pos=(-3.45, 1.6), spalten=80)
    s.einblenden(top.id)
    s.pause(0.6)
    k2 = [KOPF[0].replace("00:04:48", "00:04:51").replace("0.24, 0.05, 0.02", "0.30, 0.07, 0.02"),
          KOPF[1].replace("  1 running,  72", "  2 running,  72").replace("73 total", "74 total"),
          KOPF[2].replace("  0.0 us,", " 99.7 us,").replace("100.0 id", "  0.3 id"), KOPF[3], KOPF[4]]
    top.bild(kopf=k2, tabelle=[SPALTEN, YES % ("99.7", "  0:02.91")] + PROZ[:-1], dauer=0.8)
    s.pause(0.6)
    k3 = [k2[0].replace("00:04:51", "00:04:54").replace("0.30, 0.07, 0.02", "0.36, 0.09, 0.03"), k2[1],
          k2[2].replace(" 99.7 us,", " 99.3 us,").replace("  0.3 id", "  0.7 id"), k2[3], k2[4]]
    top.bild(kopf=k3, tabelle=[SPALTEN, YES % ("99.3", "  0:05.89")] + PROZ[:-1], dauer=0.8)
    s.pause(0.6)
    a, b = top.finde(6, "%CPU")                      # Spalte %CPU in der Spaltenzeile (Bildschirmzeile 6)
    s.einblenden(top.rahmen(7, a, b, farbe=ORANGE))  # der Wert des neuen Prozesses darunter
    s.speichern()


# ================================================================== Vorführung: Pager (systemctl status)
def systemctl_cron():
    g = lambda t, f=True: farbig(t, "gruen", f)
    return [g("●") + " cron.service - Regular background program processing daemon",
            "     Loaded: loaded (/usr/lib/systemd/system/cron.service; " + g("enabled", False) + "; preset: "
            + g("enabled", False) + ")",
            "     Active: " + g("active (running)") + " since Thu 2026-11-12 00:04:44 CET; 8s ago",
            " Invocation: a074ad10927f48989da488ac53ddbe7a",
            "       Docs: man:cron(8)",
            "   Main PID: 112 (cron)",
            "      Tasks: 1 (limit: 38204)",
            "     Memory: 512K (peak: 2M)",
            "        CPU: 18ms",
            "     CGroup: /system.slice/cron.service",
            "             " + farbig("└─", "grau", False) + "112 /usr/sbin/cron -f -P"]


def anim_f1_pager():
    """systemctl status cron im Pager: acht von elf Zeilen, Statuszeile invers; ● und active (running) grün, Baumzeichen
    grau; eine Seite weiter (die letzten Zeilen und (END)) und zurück, dann leuchtet active (running)."""
    s = Szene("beispiel/anim_f1_pager", reihenfolge="anlegen")
    p = s.pager(systemctl_cron(), pos=(-3.45, 1.4), sichtbar=8)
    s.einblenden(p.id)
    s.pause(0.8)
    p.weiter(3, dauer=0.6)                           # eine Seite weiter: die letzten Zeilen, (END)
    s.pause(0.8)
    p.weiter(-3, dauer=0.6)                          # und zurück zum Anfang
    s.pause(0.4)
    a, b = p.finde(2, "active (running)")
    s.einblenden(p.rahmen(2, a, b, farbe=ORANGE))
    s.speichern()


SZENEN = (k2sitzungen_f1, k4cateingabe_f1, k6awkfelder_f1, anim_f1_top, anim_f1_pager)

if __name__ == "__main__":
    wahl = set(sys.argv[1:])
    for f in SZENEN:
        if not wahl or f.__name__ in wahl:
            f()
            print("gebaut:", f.__name__)
