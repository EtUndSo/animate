"""Linux und Kommandozeile, Kapitel 10 „Shell-Skripte“ (C:\\Bücher\\EtUndSo\\Linux\\Arbeitshefte\\Kap10_Skripte.tex,
kap10_stufen.tex, kap10_stufen_b.tex): Abbildungen, alle animiert (notizen/animationen.md §5, §11).

Szenenname linux/k10<name> = \\label{fig:k10<name>} im Heft (\\szenenabb{k10<name>}{…}{fig:k10<name>}); Liste in
uebergabe_kap10.md, Abschnitt „Endgültige Abbildungsliste“. Phase 2b-1 (13.11.2026): Abschnitte 1–5 (23 Szenen); Phase
2b-2 ergänzt die Abschnitte 6–10 in dieser Datei.
Stil: F1. Das Terminal (k10skript) ist s.terminal (dunkel, wie Ubuntu, Prompt student@labor:~/linuxk10$, 72 Spalten
wie das Pseudoterminal der Mitschrift), Skriptdateien sind s.datei (hell), Zeilen zum Zerlegen s.raster. Die übrigen
Bilder sind Schemata aus Kästen und Pfeilen mit den Helfern unten und aus linux_hilfen.py. Inhalte (Befehle, Ausgaben,
Skriptzeilen) wörtlich aus dem Heft bzw. den Mitschriften code/kap10/sitzung_kap10*.txt und code/kap10/skripte/.
Wiederkehrende Bildsprache: Fächer $0 … $9 für Positionsparameter, Schublade = Variable (wie Kapitel 5), Schild mit dem
Exit-Status (grün 0, rot sonst), blauer Kasten „Shell“ mit Kindprozess als Kopie (wie k5kind).
Farben: grün = Erfolg/passt, rot = Fehler/falsch, orange = hervorgehoben/Weg, blau = Shell/Prozess, grau = unbeteiligt.
Koordinaten zwischen x = -3,45 und 3,45 (höchstens 548 px).
Bauen:  python tools/szenen/linux_teil10.py [k10name …]
Export: python tools/export_szenen.py --animiert <alle Namen aus SZENEN>
"""
import math
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from szenen_lib import *  # noqa: E402,F403
from szenen_lib import farbig, fett, tt_breite  # noqa: E402,F401

from linux_hilfen import *  # noqa: E402,F403  (gemeinsame Helfer der Linux-Kapitel)

schreibmaschine("text")
TT = 18                           # Schreibmaschinenschrift für Zeilen (9,9 px im Artikel)
TK = 17                           # kleinste Schreibmaschinenschrift (Kärtchen, Pfade)
P10 = "student@labor:~/linuxk10$ "  # Prompt im Übungsverzeichnis des Kapitels (Abschnitt 1.1: cd ~/linuxk10)
PFAD = "~/linuxk10"
TITEL = "student@labor: ~/linuxk10"
PUNKTE = farbig("...", "grau")    # ausgelassene Zeilen


def r4(v):
    return round(v, 4)


def ttb(t, g=TK):
    """Breite eines Texts in Schreibmaschinenschrift."""
    return len(t) * tt_breite(g, 1)


def L(s, key, w, pos, g=FM, a="center", f=SCHWARZ):
    """Beschriftung in sechs Sprachen; w = (de, en, es, zh, fr, tr)."""
    return text(s, T(s, key, *w), (r4(pos[0]), r4(pos[1])), g, a, f)


def Lr(s, key, w, pos, g=FM, a="center", f=SCHWARZ):
    """Wie L, aber roh: Punkte in Zahlen bleiben Punkte."""
    return text(s, T(s, key, *w), (r4(pos[0]), r4(pos[1])), g, a, f, roh=True)


def tx(s, t, pos, g=TT, a="center", f=SCHWARZ):
    """Schreibmaschinenschrift (Befehle, Namen, Ausgaben); in allen Sprachen gleich."""
    return s.text(None, t, (r4(pos[0]), r4(pos[1])), g, a, f, schrift="tt")


def txa(s, t, pos, g=TK, a="center", f=SCHWARZ):
    """Schreibmaschinenschrift mit ANSI-Farben (farbig) auf der weißen Seite."""
    return s.text(None, t, (r4(pos[0]), r4(pos[1])), g, a, f, schrift="tt", ansi=True)


def box(s, mitte, b, h, rand=GRAU, fuellung=WEISS, dicke=2, form="round", dash="", deckung=1.0):
    return s.box("", (r4(mitte[0]), r4(mitte[1])), breite=r4(b), hoehe=r4(h), form=form, farbe=rand, fuellung=fuellung,
                 deckung=deckung, dicke=dicke, dash=dash)


def chip(s, mitte, t, rand=BLAU, fuellung=BLAU_HELL, g=TK, h=0.28, b=None, dicke=2, textfarbe=SCHWARZ, dash=""):
    """Kärtchen mit Schreibmaschinenschrift (Wort, Datei); Ergebnis [Kasten, Text]."""
    b = b if b is not None else ttb(t, g) + 0.24
    return [box(s, mitte, b, h, rand, fuellung, dicke, dash=dash), tx(s, t, mitte, g, "center", textfarbe)]


def chipb(t, g=TK):
    return ttb(t, g) + 0.24


def reihe(texte, x0=None, mitte=None, g=TK, luecke=0.1):
    """Mitten und Breiten einer Reihe von Kärtchen (links ab x0 oder um mitte zentriert)."""
    bs = [chipb(t, g) for t in texte]
    gesamt = sum(bs) + luecke * (len(bs) - 1)
    x = x0 if x0 is not None else mitte - gesamt / 2
    ms = []
    for b in bs:
        ms.append(r4(x + b / 2))
        x += b + luecke
    return ms, bs


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


def nr(s, x, y, n, farbe=ORANGE, r=0.11):
    """Nummer im Kreis (Ergebnis [Kreis, Zahl])."""
    return [s.kreis(None, r4(x), r4(y), r, farbe=farbe, dicke=2, fuellung=WEISS, deckung=1.0),
            text(s, str(n), (r4(x), r4(y)), FM, "center", farbe)]


def schild(s, x, y, n, g=TT, b=0.34, h=0.3):
    """Schild mit einem Exit-Status: grün bei 0, rot sonst (Ergebnis [Kasten, Zahl])."""
    f = GRUEN if str(n) == "0" else ROT
    return [box(s, (x, y), max(b, ttb(str(n), g) + 0.16), h, f, GRUEN_HELL if f == GRUEN else ROT_HELL, 2.5),
            tx(s, str(n), (x, y), g, "center", f)]


def pbox(s, mitte, b, h):
    """Prozess (Shell, Kindprozess): blauer Kasten."""
    return box(s, mitte, b, h, BLAU, BLAU_HELL, 2.5, "rect")


def schublade(s, x, y, name, slot=8, g=TK):
    """Variable als Schublade (wie Kapitel 5): grauer Kasten, weißes Etikett mit dem Namen, daneben der gestrichelte
    Platz für den Wert. Ergebnis dict: alle, zx (Mitte des Platzes), bw (Breite des Platzes), b (Breite)."""
    c = tt_breite(g, 1)
    bn = len(name) * c + 0.14
    bw = slot * c + 0.14
    b = bn + bw + 0.2
    x0 = x - b / 2
    k = box(s, (x, y), b, 0.4, GRAU, GRAU_HELL, 2, "rect")
    nx = r4(x0 + 0.07 + bn / 2)
    ek = box(s, (nx, y), bn, 0.28, GRAU, WEISS, 1.5, "rect")
    et = tx(s, name, (nx, y), g)
    zx = r4(x0 + 0.13 + bn + bw / 2)
    pl = box(s, (zx, y), bw, 0.28, HELLGRAU, WEISS, 1.5, "rect", "4,4")
    return {"alle": [k, ek, et, pl], "zx": zx, "bw": r4(bw), "b": r4(b), "y": y}


def wert(s, sb, t, g=TK, farbe=SCHWARZ):
    """Gelber Zettel mit dem Wert im Platz einer Schublade (Ergebnis [Kasten, Text])."""
    return [box(s, (sb["zx"], sb["y"]), sb["bw"], 0.28, GRAU, GELB, 1.5, "rect"), tx(s, t, (sb["zx"], sb["y"]), g, "center", farbe)]


W_SHELL = ("Shell", "shell", "shell", "Shell", "shell", "kabuk")
W_KERNEL = ("Kernel", "kernel", "kernel", "内核", "noyau", "çekirdek")
W_EXIT = ("Exit-Status", "exit status", "estado de salida", "退出状态", "code de sortie", "çıkış durumu")
W_JA = ("ja", "yes", "sí", "是", "oui", "evet")
W_NEIN = ("nein", "no", "no", "否", "non", "hayır")
W_FALSCH = ("falsch", "false", "falso", "假", "faux", "yanlış")
W_WAHR = ("wahr", "true", "verdadero", "真", "vrai", "doğru")
W_AUSGABE = ("Ausgabe", "output", "salida", "输出", "sortie", "çıktı")
W_AUSG = ("Ausgabe:", "output:", "salida:", "输出：", "sortie :", "çıktı:")
W_WORTTRENNUNG = ("Worttrennung", "word splitting", "división en palabras", "分词", "découpage en mots", "sözcük bölme")
W_PFADNAMEN = ("Pfadnamen-Erweiterung", "pathname expansion", "expansión de nombres de ruta", "路径名扩展",
               "développement des chemins", "yol adı genişletme")


# ================================================================== Abschnitt 1: Vom Befehl zum Skript
UEBERBLICK = ['echo "Benutzer: $USER"', 'echo "Verzeichnis: $PWD"', 'echo "Inhalt:"', 'ls']
AUS_ERSTES = ["Benutzer: student", "Verzeichnis: /home/student/linuxk10", "Inhalt:",
              " einkauf.txt  'mein einkauf.txt'   ueberblick.sh"]
W_SK = {"liest": ("bash liest die Datei Zeile für Zeile", "bash reads the file line by line", "bash lee el archivo línea a línea",
                  "bash 逐行读取这个文件", "bash lit le fichier ligne par ligne", "bash dosyayı satır satır okur")}


def k10skript():
    """Oben die Datei ueberblick.sh (s.datei, skripte/ueberblick_v1.sh) mit den Zeilennummern 1–4 links, darunter das
    Terminal (Block s1_erstes). Nach bash ueberblick.sh springt ein Lesezeichen von Zeile zu Zeile, und zu jeder Zeile
    erscheint unten ihre Ausgabe mit derselben Nummer; zuletzt die neue Eingabeaufforderung."""
    s = Szene("linux/k10skript", reihenfolge="anlegen")
    d = s.datei("ueberblick.sh", "\n".join(UEBERBLICK), pos=(-3.0, 2.95), spalten=26, groesse=TT)
    xn = r4(d.links - 0.17)
    nums = [text(s, str(i + 1), (xn, d.y(i)), FM, "center", GRAU) for i in range(4)]
    lab = L(s, "liest", W_SK["liest"], (d.links, r4(d.oben_kante + 0.2)), FM, "left", ORANGE)
    lz = d.markieren(0, 0, 25, ORANGE, 0.3)
    t = s.terminal(pos=(-3.0, r4(d.unten_kante - 0.3)), spalten=72, zeilen=6, prompt=P10, titel=TITEL, groesse=18)
    nt = [text(s, str(i + 1), (r4(t.links - 0.17), t.y(i + 1)), FM, "center", ORANGE) for i in range(4)]
    dy = d.zelle[1]
    schritt(s, EIN([d.id] + nums, 0.7))
    schritt(s, EIN(lab, 0.5))
    s.pause(0.4)
    schritt(s, EIN(t.id, 0.6))
    s.pause(0.3)
    t.eingabe("bash ueberblick.sh")
    for k in range(4):
        with s.gleichzeitig():
            if k == 0:
                schritt(s, EIN([lz, nt[0]], 0.5))
            else:
                schritt(s, VER(lz, 0, -dy, 0.5), EIN(nt[k], 0.5))
            t.ausgabe(AUS_ERSTES[k], dauer=0.5)
        s.pause(0.4)
    t.prompt(pfad=PFAD)
    s.speichern()


W_ES = {"verz": ("Verzeichnis:", "directory:", "directorio:", "目录：", "répertoire :", "dizin:"),
        "kind": ("Kindprozess, Kopie der Shell", "child process, copy of the shell", "proceso hijo, copia de la shell",
                 "子进程，shell 的副本", "processus enfant, copie du shell", "alt süreç, kabuğun kopyası"),
        "beendet": ("beendet, Kopie verworfen", "ended, copy discarded", "terminado, copia descartada", "已结束，副本被丢弃",
                    "terminé, copie jetée", "bitti, kopya atıldı"),
        "unv": ("unverändert", "unchanged", "sin cambios", "未改变", "inchangé", "değişmedi"),
        "keinkind": ("kein Kindprozess", "no child process", "sin proceso hijo", "没有子进程", "pas de processus enfant",
                     "alt süreç yok"),
        "bleibt": ("Änderungen bleiben", "changes remain", "los cambios se quedan", "更改保留下来", "les changements restent",
                   "değişiklikler kalır")}


def k10eigeneshell():
    """Links bash wechsle.sh: Aus der Shell (Verzeichnis ~/linuxk10, Schublade ziel leer) wächst ein Kindprozess als
    Kopie; darin springt das Verzeichnis auf /tmp und ziel bekommt erreicht. Der Kindprozess endet, die Shell ist
    unverändert (Block s1_eigeneshell). Rechts source wechsle.sh: kein Kindprozess, die Shell selbst wechselt nach /tmp
    und behält ziel=erreicht (Block s1_source)."""
    s = Szene("linux/k10eigeneshell", reihenfolge="anlegen")
    w = W_ES
    trenn = lin(s, (0, 2.8), (0, -1.6), HELLGRAU, 2, "6,5")

    def kasten(cx, y, key, wl):
        k = pbox(s, (cx, y), 3.1, 1.1)
        lab = L(s, key, wl, (cx - 1.45, y + 0.36), FM, "left", BLAU)
        lv = L(s, "verz", w["verz"], (cx - 1.45, y + 0.06), FM, "left", GRAU)
        v = tx(s, PFAD, (cx - 0.2, y + 0.06), TK, "left")
        sb = schublade(s, cx - 0.76, y - 0.28, "ziel")
        return {"teile": [k, lab, lv, v] + sb["alle"], "v": v, "sb": sb, "k": k}

    xl, xr = -1.75, 1.75
    h_l = tx(s, "bash wechsle.sh", (xl, 2.62), TT, "center", DUNKEL)
    h_r = tx(s, "source wechsle.sh", (xr, 2.62), TT, "center", DUNKEL)
    sl = kasten(xl, 1.85, "shell", W_SHELL)
    pf_k = pfk(s, (xl, 1.3), (xl, 0.92), BLAU, 2.5)
    kd = kasten(xl, 0.35, "kind", w["kind"])
    z_k = wert(s, kd["sb"], "erreicht")
    g_k = geist(s, (xl, 0.35), 3.1, 1.1)
    l_end = L(s, "beendet", w["beendet"], (xl, 0.35), FM, "center", GRAU)
    l_unv = L(s, "unv", w["unv"], (xl + 1.45, 1.57), FM, "right", GRUEN)
    out_l = s.raster(["Im Skript: /tmp, ziel=erreicht", "$ pwd", "/home/student/linuxk10", '$ echo "ziel=$ziel"', "ziel="],
                     (-3.3, -0.5), groesse=TK)
    sr = kasten(xr, 1.85, "shell", W_SHELL)
    z_r = wert(s, sr["sb"], "erreicht")
    l_kein = L(s, "keinkind", w["keinkind"], (xr, 0.95), FM, "center", GRAU)
    l_bleibt = L(s, "bleibt", w["bleibt"], (xr + 1.45, 1.57), FM, "right", ORANGE)
    out_r = s.raster(["Im Skript: /tmp, ziel=erreicht", "$ pwd", "/tmp"], (0.2, -0.5), groesse=TK)
    # links: bash wechsle.sh
    schritt(s, EIN([trenn, h_l] + sl["teile"], 0.7))
    s.pause(0.4)
    schritt(s, ZEICHNE(pf_k, 0.5), WACHS(kd["k"], 0.6), EIN(kd["teile"][1:], 0.6))
    s.pause(0.3)
    s.ersetzen(kd["v"], "/tmp", farbe=ORANGE, dauer=0.6)
    schritt(s, EIN(z_k, 0.5), EIN(out_l.ids[0], 0.5))
    s.pause(0.5)
    schritt(s, AUS(kd["teile"] + z_k, 0.7), EIN([g_k, l_end], 0.7))
    schritt(s, EIN(out_l.ids[1:], 0.6))
    schritt(s, BETONE(sl["v"], 0.7), EIN(l_unv, 0.6))
    s.pause(0.6)
    # rechts: source wechsle.sh
    schritt(s, EIN([h_r] + sr["teile"] + [l_kein], 0.7))
    s.pause(0.3)
    s.ersetzen(sr["v"], "/tmp", farbe=ORANGE, dauer=0.6)
    schritt(s, EIN(z_r, 0.5), EIN(out_r.ids[0], 0.5))
    schritt(s, EIN(out_r.ids[1:] + [l_bleibt], 0.6))
    s.speichern()


WER = ["#!/bin/bash", PUNKTE]
W_AB = {"rechte": ("Rechte", "permissions", "permisos", "权限", "droits", "izinler"),
        "skript": ("kein Maschinenprogramm,\nsondern ein Skript", "not a machine program\nbut a script",
                   "no es un programa máquina,\nsino un script", "不是机器程序，\n而是脚本", "pas un programme machine,\nmais un script",
                   "makine programı değil,\nbir betik"),
        "neu": ("neuer Prozess", "new process", "proceso nuevo", "新进程", "nouveau processus", "yeni süreç"),
        "eingef": ("neu eingefügt", "newly inserted", "insertado", "新插入", "inséré", "yeni eklendi"),
        "l1": ("Die Shell bittet den Kernel, ./wer.sh zu starten.", "The shell asks the kernel to start ./wer.sh.",
               "La shell pide al kernel que inicie ./wer.sh.", "shell 请求内核启动 ./wer.sh。", "Le shell demande au noyau de lancer ./wer.sh.",
               "Kabuk çekirdekten ./wer.sh'yi başlatmasını ister."),
        "l2": ("Der Kernel prüft das Ausführungsrecht x.", "The kernel checks the execute permission x.",
               "El kernel comprueba el permiso de ejecución x.", "内核检查执行权限 x。", "Le noyau vérifie le droit d'exécution x.",
               "Çekirdek çalıştırma iznini (x) denetler."),
        "l3": ("Er liest die ersten Bytes der Datei: #!/bin/bash.", "It reads the first bytes of the file: #!/bin/bash.",
               "Lee los primeros bytes del archivo: #!/bin/bash.", "它读取文件开头的字节：#!/bin/bash。",
               "Il lit les premiers octets du fichier : #!/bin/bash.", "Dosyanın ilk baytlarını okur: #!/bin/bash."),
        "l4": ("Er startet stattdessen /bin/bash mit dieser Argumentliste.", "Instead it starts /bin/bash with this argument list.",
               "En su lugar inicia /bin/bash con esta lista de argumentos.", "它改为用这个参数列表启动 /bin/bash。",
               "À la place, il lance /bin/bash avec cette liste d'arguments.", "Bunun yerine /bin/bash'i bu argüman listesiyle başlatır."),
        "l5": ("Die bash öffnet ./wer.sh zum Lesen (Leserecht r).", "bash opens ./wer.sh for reading (read permission r).",
               "bash abre ./wer.sh para leerlo (permiso de lectura r).", "bash 打开 ./wer.sh 来读取（读权限 r）。",
               "bash ouvre ./wer.sh en lecture (droit de lecture r).", "bash, ./wer.sh'yi okumak için açar (okuma izni r)."),
        "ps": ("ps zeigt:", "ps shows:", "ps muestra:", "ps 显示：", "ps affiche :", "ps gösterir:")}


def k10ablauf():
    """Pflichtbild: Was bei ./wer.sh eins zwei geschieht, fünf nummerierte Schritte mit Legende. (1) Shell → Kernel;
    (2) Ausführungsrecht x (Haken am x von -rwxr-xr-x); (3) erste Bytes #!/bin/bash (Datei-Ansicht), Schild „kein
    Maschinenprogramm, sondern ein Skript“; (4) neuer Prozess /bin/bash mit den Kärtchen /bin/bash ./wer.sh eins zwei,
    ./wer.sh als neu eingefügt; (5) die bash liest die Datei (Haken am r). Ergebnis: ps zeigt /bin/bash ./wer.sh eins
    zwei (Block s1_wer)."""
    s = Szene("linux/k10ablauf", reihenfolge="anlegen")
    w = W_AB
    sh = [pbox(s, (-2.05, 2.35), 2.5, 0.62), L(s, "shell", W_SHELL, (-3.22, 2.53), FM, "left", BLAU),
          tx(s, "./wer.sh eins zwei", (-1.95, 2.25), TT)]
    ke = [box(s, (-1.68, 1.25), 3.25, 0.62, GRAU, GRAU_HELL, 2, "rect"), L(s, "kernel", W_KERNEL, (-3.22, 1.43), FM, "left", GRAU)]
    d = s.datei("wer.sh", "\n".join(WER), pos=(0.25, 2.7), spalten=13, groesse=TK)
    g = s.raster("-rwxr-xr-x", (1.78, d.y(0)), groesse=22)
    l_re = L(s, "rechte", w["rechte"], (1.78, r4(d.y(0) - 0.27)), FM, "left", GRAU)
    p1 = pfk(s, (-2.6, 2.04), (-2.6, 1.56), DUNKEL, 2.5)
    n1 = nr(s, -2.84, 1.8, 1)
    pk = pfk(s, (-0.03, 1.4), (0.25, r4(d.unten_kante + 0.1)), GRAU, 2, "5,4")
    r_x = g.rahmen(0, 3, 3, GRUEN, 2.5, rand=0.0)
    h_x = haken(s, g.xm(3), r4(g.oben(0) + 0.14), GRUEN, 0.06, 3)
    n2 = nr(s, r4(g.rechts + 0.2), g.y(0), 2)
    r_s = d.rahmen(0, 0, 10, ORANGE, 2.5, rand=0.0)
    n3 = nr(s, r4(d.links - 0.15), d.y(0), 3)
    schild3 = [box(s, (-1.0, 1.25), 1.75, 0.5, ORANGE, WEISS, 2), L(s, "skript", w["skript"], (-1.0, 1.25), FM, "center", ORANGE)]
    p4 = pfk(s, (-2.6, 0.94), (-2.6, 0.47), DUNKEL, 2.5)
    n4 = nr(s, -2.84, 0.7, 4)
    xs, bs = reihe(["/bin/bash", "./wer.sh", "eins", "zwei"], x0=-3.15, g=TK, luecke=0.12)
    pr = [pbox(s, (-1.5, 0.05), 3.6, 0.78), L(s, "neu", w["neu"], (-3.22, 0.3), FM, "left", BLAU)]
    karten = [chip(s, (xs[0], -0.08), "/bin/bash", BLAU, WEISS),
              chip(s, (xs[1], -0.08), "./wer.sh", ORANGE, ORANGE_HELL, dicke=2.5),
              chip(s, (xs[2], -0.08), "eins", GRAU, WEISS), chip(s, (xs[3], -0.08), "zwei", GRAU, WEISS)]
    l_ein = L(s, "eingef", w["eingef"], (xs[1], -0.53), FM, "center", ORANGE)
    xr = 0.75
    p5 = pfk(s, (0.3, 0.05), (xr, r4(d.unten_kante + 0.02)), DUNKEL, 2.5, knick="hv")
    n5 = nr(s, xr + 0.22, 0.7, 5)
    r_r = g.rahmen(0, 1, 1, GRUEN, 2.5, rand=0.0)
    h_r = haken(s, g.xm(1), r4(g.oben(0) + 0.14), GRUEN, 0.06, 3)
    yl = [-0.9, -1.2, -1.5, -1.8, -2.1]
    leg = [nr(s, -3.2, y, i + 1) + [L(s, "l%d" % (i + 1), w["l%d" % (i + 1)], (-3.0, y), FM, "left")] for i, y in enumerate(yl)]
    erg = [L(s, "ps", w["ps"], (-3.3, -2.48), FM, "left", GRAU), tx(s, "/bin/bash ./wer.sh eins zwei", (-2.15, -2.48), TT, "left", GRUEN)]
    schritt(s, EIN(sh, 0.6), EIN([d.id] + g.ids + [l_re], 0.6))
    s.pause(0.5)
    schritt(s, ZEICHNE(p1, 0.5), EIN(ke + n1 + leg[0], 0.6))
    s.pause(0.4)
    schritt(s, ZEICHNE(pk, 0.5), EIN([r_x] + h_x + n2 + leg[1], 0.6))
    s.pause(0.4)
    schritt(s, EIN([r_s] + n3 + leg[2], 0.6))
    schritt(s, WACHS(schild3[0], 0.5), EIN(schild3[1], 0.5))
    s.pause(0.4)
    schritt(s, ZEICHNE(p4, 0.5), WACHS(pr[0], 0.6), EIN([pr[1]] + n4 + leg[3], 0.6))
    schritt(s, EIN(flach(karten), 0.6))
    schritt(s, BETONE(karten[1][1], 0.7), EIN(l_ein, 0.6))
    s.pause(0.4)
    schritt(s, ZEICHNE(p5, 0.7), EIN([r_r] + h_r + n5 + leg[4], 0.7))
    s.pause(0.4)
    schritt(s, EIN(erg, 0.6))
    s.speichern()


BYTES = ["#", "!", "/", "b", "i", "n", "/", "b", "a", "s", "h", "\\r", "\\n"]
OD = ["$ head -n 1 windows.sh | od -c", "0000000   #   !   /   b   i   n   /   b   a   s   h  \\r  \\n", "0000015"]
W_CR = {"name": ("Name des Interpreters", "name of the interpreter", "nombre del intérprete", "解释器的名称", "nom de l'interpréteur",
                 "yorumlayıcının adı"),
        "gesucht": ("gesucht:", "looked for:", "se busca:", "查找：", "cherché :", "aranan:"),
        "passt": ("passt", "matches", "coincide", "匹配", "correspond", "eşleşir")}


def k10crlf():
    """Oben die Ausgabe von od -c (Block s1_crlffile); darunter die erste Zeile von windows.sh als 13 Byte-Kästchen,
    \\r rot. Die Klammer „Name des Interpreters“ reicht von / bis \\r; gesucht wird /bin/bash\\r, im Verzeichnis /bin
    steht nur bash: No such file or directory. Darunter dieselbe Zeile nach sed: ohne \\r, die Klammer endet bei h,
    der Name passt."""
    s = Szene("linux/k10crlf", reihenfolge="anlegen")
    w = W_CR
    g = s.raster(OD, (-3.3, 2.6), groesse=TK)
    xs = []
    for k, ch in enumerate(BYTES):
        b = 10 + 4 * k
        xs.append(g.xm(b - len(ch) + 1, b))

    def zeile(y, liste, rot=None):
        teile = []
        for k, ch in enumerate(liste):
            f = ROT if k == rot else GRAU
            teile.append(chip(s, (xs[k], y), ch, f, ROT_HELL if k == rot else WEISS, b=0.27, h=0.3, dicke=2 if k != rot else 2.5,
                              textfarbe=ROT if k == rot else SCHWARZ))
        return teile

    y1, y2 = 1.75, -0.4
    z1 = zeile(y1, BYTES, rot=11)
    k1 = klammer(s, r4(xs[2] - 0.14), r4(xs[11] + 0.14), r4(y1 - 0.25), True, ORANGE, 0.07, 2.5)
    l1 = L(s, "name", w["name"], ((xs[2] + xs[11]) / 2, y1 - 0.45), FM, "center", ORANGE)
    yg = 1.0
    l_g = L(s, "gesucht", w["gesucht"], (-1.85, yg), FM, "right", GRAU)
    such = txa(s, "/bin/bash" + farbig("\\r", ROT), (-1.7, yg), TT, "left")
    xd = 2.45
    dir1 = [box(s, (xd, 1.25), 1.5, 0.95, BLAU, WEISS, 2, "rect"), tx(s, "/bin", (xd, 1.55), TT, "center", BLAU),
            chip(s, (xd, 1.15), "bash", GRAU, WEISS), txa(s, PUNKTE, (xd, 0.92), TK)]
    pf1 = pfk(s, (-0.6, yg), (1.65, yg), DUNKEL, 2.5)
    x1 = kreuz(s, 0.55, yg, 0.22)
    msg = tx(s, "No such file or directory", (-0.95, 0.62), TK, "left", ROT)
    # nach sed
    sed = tx(s, "$ sed -i 's/\\r$//' windows.sh", (-3.3, 0.25), TK, "left", GRAU)
    ohne = BYTES[:11] + ["\\n"]
    z2 = zeile(y2, ohne)
    k2 = klammer(s, r4(xs[2] - 0.14), r4(xs[10] + 0.14), r4(y2 - 0.25), True, GRUEN, 0.07, 2.5)
    l2 = L(s, "name", w["name"], ((xs[2] + xs[10]) / 2, y2 - 0.45), FM, "center", GRUEN)
    yg2 = -1.15
    l_g2 = L(s, "gesucht", w["gesucht"], (-1.85, yg2), FM, "right", GRAU)
    such2 = tx(s, "/bin/bash", (-1.7, yg2), TT, "left")
    dir2 = [box(s, (xd, -0.9), 1.5, 0.95, BLAU, WEISS, 2, "rect"), tx(s, "/bin", (xd, -0.6), TT, "center", BLAU),
            chip(s, (xd, -1.0), "bash", GRUEN, GRUEN_HELL, dicke=2.5), txa(s, PUNKTE, (xd, -1.23), TK)]
    pf2 = pfk(s, (-0.6, yg2), (1.65, yg2), DUNKEL, 2.5)
    ok = haken(s, 0.55, r4(yg2 + 0.02), GRUEN, 0.1, 4)
    l_ok = L(s, "passt", w["passt"], (0.75, r4(yg2 + 0.22)), FM, "left", GRUEN)
    schritt(s, EIN(g.ids, 0.6))
    s.pause(0.4)
    schritt(s, EIN(flach(z1), 0.7))
    schritt(s, BETONE(z1[11][1], 0.7))
    s.pause(0.3)
    schritt(s, ZEICHNE(k1, 0.6), EIN(l1, 0.6))
    s.pause(0.4)
    schritt(s, EIN([l_g, such] + flach(dir1), 0.6))
    schritt(s, ZEICHNE(pf1, 0.6))
    schritt(s, EIN([x1, msg], 0.5))
    s.pause(0.8)
    schritt(s, EIN(sed, 0.5))
    schritt(s, EIN(flach(z2), 0.7))
    schritt(s, ZEICHNE(k2, 0.6), EIN(l2, 0.6))
    schritt(s, EIN([l_g2, such2] + flach(dir2), 0.6))
    schritt(s, ZEICHNE(pf2, 0.6))
    schritt(s, EIN(ok + [l_ok], 0.5))
    s.speichern()


# ================================================================== Abschnitt 2: Positionsparameter
FB = [0.95, 1.36, 0.5, 0.5] + [0.4] * 6     # Breiten der Fächer $0 … $9 (Fach 1 fasst „Milch und Brot“)


def faecher(s, x0, y, breiten, h=0.36, luecke=0.04):
    """Nummerierte Fächer $0, $1, … nebeneinander ab x0; Ergebnis (Kästen, Nummern, Mitten)."""
    k, n, m = [], [], []
    x = x0
    for i, b in enumerate(breiten):
        cx = r4(x + b / 2)
        k.append(box(s, (cx, y), b, h, GRAU, GRAU_HELL, 2, "rect"))
        n.append(tx(s, "$%d" % i, (cx, r4(y - h / 2 - 0.15)), TK, "center", GRAU))
        m.append(cx)
        x += b + luecke
    return k, n, m


def k10parameter():
    """Die Befehlszeile ./zeige.sh Milch Brot Käse als vier Wort-Kärtchen; sie fallen nacheinander in die Fächer $0 bis
    $3, der Zähler $# springt von 0 auf 1, 2, 3 (Fach 0 zählt nicht). Zweiter Durchgang ./zeige.sh "Milch und Brot":
    Die Anführungszeichen fallen weg, das ganze Wort landet in Fach 1, $# = 1 (Block s2_zeige)."""
    s = Szene("linux/k10parameter", reihenfolge="anlegen")
    x0 = -3.3
    y1w, y1f, y2w, y2f = 2.2, 1.4, 0.4, -0.4

    def woerter(g, y_w, y_f, m, spalten):
        """Kopien der Wörter (Spalten a..b) wandern in die Fächer 0, 1, …; Ergebnis (Kopien, Schiebe-Teile)."""
        kopien, schiebe = [], []
        for i, (a, b) in enumerate(spalten):
            kp = g.teil(0, a, b, farbe=DUNKEL if i == 0 else BLAU)
            kopien.append(kp)
            schiebe.append(VER(kp, m[i] - (b - a + 1) * g.zelle[0] / 2 - g.x(a), y_f - y_w, 0.7))
        return kopien, schiebe

    k1, n1, m1 = faecher(s, x0, y1f, FB)
    g1 = s.raster("$ ./zeige.sh Milch Brot Käse", (x0, y1w), groesse=TT)
    ko1, sch1 = woerter(g1, y1w, y1f, m1, [(f.a, f.b) for f in g1.felder(0)[1:]])
    z1 = tx(s, "$# = 0", (2.2, y1w), TT, "left", ORANGE)
    k2, n2, m2 = faecher(s, x0, y2f, FB)
    g2 = s.raster('$ ./zeige.sh "Milch und Brot"', (x0, y2w), groesse=TT)
    ko2, sch2 = woerter(g2, y2w, y2f, m2, [(2, 11), (14, 27)])
    kq, _ = g2.klammer(0, 13, 28, "", seite="oben", farbe=ORANGE, dicke=2.5)
    q2 = [kq, L(s, "einarg", ("ein Argument", "one argument", "un argumento", "一个参数", "un argument", "tek argüman"),
                (g2.xm(13, 28), r4(g2.oben(0) + 0.27)), FM, "center", ORANGE)]
    z2 = tx(s, "$# = 0", (2.2, y2w), TT, "left", ORANGE)
    schritt(s, EIN(k1 + n1, 0.6))
    schritt(s, EIN(g1.ids + [z1], 0.6))
    s.pause(0.5)
    schritt(s, EIN(ko1, 0.2))
    for i in range(4):
        with s.gleichzeitig():
            schritt(s, sch1[i])
            if i:
                s.ersetzen(z1, "$# = %d" % i, dauer=0.7)
        s.pause(0.25)
    s.pause(0.6)
    schritt(s, EIN(k2 + n2, 0.6))
    schritt(s, EIN(g2.ids + [z2], 0.6))
    s.pause(0.4)
    schritt(s, EIN(q2 + ko2, 0.5))
    schritt(s, sch2[0])
    with s.gleichzeitig():
        schritt(s, sch2[1])
        s.ersetzen(z2, "$# = 1", dauer=0.7)
    s.speichern()


W_NU = {"aufruf": ("Aufruf", "call", "llamada", "调用", "appel", "çağrı"),
        "inhalt": ("Inhalt von", "content of", "contenido de", "内容：", "contenu de", "içeriği:"),
        "gleich": ("dreimal derselbe Name", "the same name three times", "tres veces el mismo nombre", "三次都是同一个名字",
                   "trois fois le même nom", "üç kez aynı ad")}


def k10null():
    """Drei Aufrufe von zeige.sh untereinander (./zeige.sh, bash zeige.sh, ~/linuxk10/zeige.sh); daneben Fach $0 mit
    ./zeige.sh, zeige.sh, /home/student/linuxk10/zeige.sh (Blöcke s2_zeige, s2_null). Ein Trichter basename macht aus
    allen drei dasselbe zeige.sh; der Dateiname ist in jedem Inhalt orange hervorgehoben."""
    s = Szene("linux/k10null", reihenfolge="anlegen")
    w = W_NU
    auf = ["./zeige.sh", "bash zeige.sh", "~/linuxk10/zeige.sh"]
    inh = ["./zeige.sh", "zeige.sh", "/home/student/linuxk10/zeige.sh"]
    ys = [1.75, 1.05, 0.35]
    xf, bf = -0.3, 2.55
    kopf = [L(s, "aufruf", w["aufruf"], (-3.3, 2.35), FM, "left", GRAU),
            L(s, "inhalt", w["inhalt"], (xf - 0.12, 2.35), FM, "right", GRAU), tx(s, "$0", (xf - 0.05, 2.35), TT, "left", GRAU)]
    c_auf, faech, inhalte, pfe = [], [], [], []
    for a, i, y in zip(auf, inh, ys):
        c_auf.append(tx(s, a, (-3.3, y), TT, "left"))
        faech.append(box(s, (xf, y), bf, 0.36, GRAU, GRAU_HELL, 2, "rect"))
        inhalte.append(txa(s, i, (xf, y), TK))
        pfe.append(pfk(s, (-3.3 + ttb(a, TT) + 0.08, y), (r4(xf - bf / 2 - 0.05), y), GRAU, 2))
    # Trichter
    xt, yt = 1.85, 1.05
    tr_ = [lin(s, (xt - 0.42, yt + 0.55), (xt - 0.1, yt - 0.05), DUNKEL, 2.5), lin(s, (xt + 0.42, yt + 0.55), (xt + 0.1, yt - 0.05), DUNKEL, 2.5),
           lin(s, (xt - 0.1, yt - 0.05), (xt - 0.1, yt - 0.35), DUNKEL, 2.5), lin(s, (xt + 0.1, yt - 0.05), (xt + 0.1, yt - 0.35), DUNKEL, 2.5),
           tx(s, "basename", (xt, yt + 0.72), TT, "center", DUNKEL)]
    zu = [pfk(s, (xf + bf / 2 + 0.05, y), (xt - 0.3, yt + 0.4 + (y - ys[1]) * 0.1), GRAU, 2) for y in ys]
    erg = chip(s, (xt, -0.15), "zeige.sh", ORANGE, ORANGE_HELL, g=TT, dicke=2.5)
    p_e = pfk(s, (xt, yt - 0.38), (xt, 0.02), DUNKEL, 2.5)
    l_gl = L(s, "gleich", w["gleich"], (xt, -0.55), FM, "center", GRAU)
    schritt(s, EIN(kopf, 0.6))
    for k in range(3):
        schritt(s, EIN(c_auf[k], 0.5))
        schritt(s, ZEICHNE(pfe[k], 0.5), EIN([faech[k], inhalte[k]], 0.6))
        s.pause(0.3)
    s.pause(0.4)
    schritt(s, ZEICHNE(tr_[:4], 0.6), EIN(tr_[4], 0.6))
    with s.gleichzeitig():
        schritt(s, ZEICHNE(zu, 0.7))
        for i, t in zip(inhalte, inh):
            s.ersetzen(i, farbig(t[:-8], "grau") + farbig("zeige.sh", ORANGE) if len(t) > 8 else farbig(t, ORANGE), dauer=0.7)
    schritt(s, ZEICHNE(p_e, 0.5), EIN(erg, 0.6))
    schritt(s, EIN(l_gl, 0.5))
    s.speichern()


W_AT = {"args": ("drei Argumente", "three arguments", "tres argumentos", "三个参数", "trois arguments", "üç argüman"),
        "w3": ("3 Wörter, unverändert", "3 words, unchanged", "3 palabras, sin cambios", "3 个词，原样不变", "3 mots, inchangés",
               "3 sözcük, değişmeden"),
        "w6": ("6 Wörter", "6 words", "6 palabras", "6 个词", "6 mots", "6 sözcük"),
        "w1": ("1 Wort", "1 word", "1 palabra", "1 个词", "1 mot", "1 sözcük"),
        "kleb": ("mit Leerzeichen\nverklebt", "glued together\nwith spaces", "pegados\ncon espacios", "用空格\n粘在一起",
                 "collés avec\ndes espaces", "boşluklarla\nyapıştırılmış")}


def k10at():
    """Drei Argumente als Kärtchen (Milch, Äpfel und Birnen, *.txt). Drei Bahnen: "$@" gibt sie unverändert weiter;
    $* zerlegt Äpfel und Birnen in drei Wörter (Worttrennung) und ersetzt *.txt durch einkauf.txt und mein einkauf.txt
    (Pfadnamen-Erweiterung), sechs Wörter; "$*" verklebt alles zu einem Wort. Werte aus Block s2_alle."""
    s = Szene("linux/k10at", reihenfolge="anlegen")
    w = W_AT
    args = ["Milch", "Äpfel und Birnen", "*.txt"]
    xa, _ = reihe(args, mitte=0.0, luecke=0.3)
    ya = 2.45
    l_args = L(s, "args", w["args"], (xa[0] - 0.55, ya), FM, "right", GRAU)
    quelle = [chip(s, (x, ya), t, BLAU, BLAU_HELL) for x, t in zip(xa, args)]
    xb = [-2.55, -0.6, 1.95]
    yk = 1.9
    kopf = [tx(s, '"$@"', (xb[0], yk), TT, "center", ORANGE), tx(s, "$*", (xb[1], yk), TT, "center", ORANGE),
            tx(s, '"$*"', (xb[2], yk), TT, "center", ORANGE)]
    tr_ = [lin(s, (-1.6, 2.05), (-1.6, -1.25), HELLGRAU, 2, "6,5"), lin(s, (0.4, 2.05), (0.4, 1.0), HELLGRAU, 2, "6,5")]
    dz = 0.36
    ys = [r4(1.45 - i * dz) for i in range(6)]
    # Bahn "$@"
    b1 = [chip(s, (xa[i], ya), t, BLAU, BLAU_HELL) for i, t in enumerate(args)]
    l_w3 = L(s, "w3", w["w3"], (xb[0], -0.95), FM, "center", GRUEN)
    # Bahn $*
    b2 = [chip(s, (xa[i], ya), t, BLAU, BLAU_HELL) for i, t in enumerate(args)]
    teile = [chip(s, (xb[1], ys[k]), t, BLAU, WEISS) for k, t in enumerate(["Äpfel", "und", "Birnen"], 1)]
    namen = [chip(s, (xb[1], ys[k]), t, GRUEN, GRUEN_HELL) for k, t in ((4, "einkauf.txt"), (5, "mein einkauf.txt"))]
    kl_w = vklammer(s, r4(xb[1] + 0.48), r4(ys[1] + 0.12), r4(ys[3] - 0.12), ORANGE, 0.07, 2.5)
    kl_p = vklammer(s, r4(xb[1] + 0.82), r4(ys[4] + 0.12), r4(ys[5] - 0.12), ORANGE, 0.07, 2.5)
    l_wt = L(s, "wt", W_WORTTRENNUNG, (xb[1] + 0.58, ys[2]), FM, "left", ORANGE)
    l_pn = L(s, "pn", W_PFADNAMEN, (xb[1] + 0.92, (ys[4] + ys[5]) / 2), FM, "left", ORANGE)
    l_w6 = L(s, "w6", w["w6"], (xb[1], -0.95), FM, "center", ORANGE)
    # Bahn "$*"
    b3 = [chip(s, (xa[i], ya), t, BLAU, BLAU_HELL) for i, t in enumerate(args)]
    lang = chip(s, (xb[2], ys[0]), "Milch Äpfel und Birnen *.txt", BLAU, BLAU_HELL)
    l_kl = L(s, "kleb", w["kleb"], (xb[2], ys[1] - 0.05), FM, "center", GRAU)
    l_w1 = L(s, "w1", w["w1"], (xb[2], -0.95), FM, "center", GRAU)
    schritt(s, EIN(flach(quelle) + [l_args], 0.6))
    schritt(s, EIN(kopf + tr_, 0.6))
    s.pause(0.5)
    schritt(s, EIN(flach(b1), 0.3))
    schritt(s, *[v for i, c in enumerate(b1) for v in VERS(c, xb[0] - xa[i], ys[i] - ya, 0.9)])
    schritt(s, EIN(l_w3, 0.5))
    s.pause(0.6)
    schritt(s, EIN(flach(b2), 0.3))
    schritt(s, *[v for i, c in enumerate(b2) for v in VERS(c, xb[1] - xa[i], ys[[0, 1, 4][i]] - ya, 0.9)])
    schritt(s, AUS(b2[1], 0.6), EIN(flach(teile), 0.6), ZEICHNE(kl_w, 0.6), EIN(l_wt, 0.6))
    schritt(s, AUS(b2[2], 0.6), EIN(flach(namen), 0.6), ZEICHNE(kl_p, 0.6), EIN(l_pn, 0.6))
    schritt(s, EIN(l_w6, 0.5))
    s.pause(0.6)
    schritt(s, EIN(flach(b3), 0.3))
    schritt(s, *[v for i, c in enumerate(b3) for v in VERS(c, xb[2] - xa[i], ys[0] - ya, 0.9)])
    schritt(s, AUS(flach(b3), 0.6), WACHS(lang[0], 0.6), EIN([lang[1], l_kl], 0.6))
    schritt(s, EIN(l_w1, 0.5))
    s.speichern()


W_SH = {"weg": ("entfernt", "removed", "eliminado", "已移除", "retiré", "kaldırıldı"),
        "ruecken": ("rücken nach vorn", "move forward", "avanzan", "向前移", "avancent", "öne kayar"),
        "bleibt": ("bleibt", "stays", "se queda", "不变", "reste", "kalır")}


def k10shift():
    """Fächer $0 bis $3 mit ./schiebe.sh, Milch, Brot, Käse, Zähler $# = 3 und die Zeile Vorher: … (Block s2_shift).
    Bei shift fällt Milch aus Fach 1 heraus, Brot und Käse rücken je ein Fach nach vorn, Fach 3 wird leer, $# = 2;
    Fach 0 bleibt. Zuletzt die Zeile Nachher: …"""
    s = Szene("linux/k10shift", reihenfolge="anlegen")
    w = W_SH
    x0, yf = -2.25, 1.15
    k, n, m = faecher(s, x0, yf, [1.15, 0.7, 0.7, 0.7], luecke=0.06)
    inh = ["./schiebe.sh", "Milch", "Brot", "Käse"]
    c = [chip(s, (m[i], yf), t, DUNKEL if i == 0 else BLAU, WEISS if i == 0 else BLAU_HELL) for i, t in enumerate(inh)]
    z = tx(s, "$# = 3", (1.6, yf), TT, "left", ORANGE)
    cmd = tx(s, "shift", (m[1], 2.05), TT, "center", ORANGE)
    p_cmd = pfk(s, (m[1], 1.88), (m[1], 1.45), ORANGE, 2.5)
    g = s.raster(["Vorher:  3 Argumente, das erste ist Milch", "Nachher: 2 Argumente, das erste ist Brot"], (-2.25, -0.4),
                 groesse=TK, zeilenabstand=1.5)
    geist_m = chip(s, (m[1], 0.15), "Milch", HELLGRAU, WEISS, dash="4,4", textfarbe=GRAU)
    l_weg = L(s, "weg", w["weg"], (m[1] + 0.5, 0.15), FM, "left", GRAU)
    l_rueck = L(s, "ruecken", w["ruecken"], ((m[2] + m[3]) / 2, r4(yf + 0.38)), FM, "center", BLAU)
    l_bl = L(s, "bleibt", w["bleibt"], (m[0], r4(yf + 0.38)), FM, "center", GRAU)
    schritt(s, EIN(k + n + flach(c) + [z], 0.7))
    schritt(s, EIN(g.ids[0], 0.5))
    s.pause(0.6)
    schritt(s, EIN(cmd, 0.5), ZEICHNE(p_cmd, 0.5))
    schritt(s, *VERS(c[1], 0, 0.15 - yf, 0.8))
    schritt(s, AUS(c[1], 0.5), EIN([*geist_m, l_weg], 0.5))
    with s.gleichzeitig():
        schritt(s, *(VERS(c[2], m[1] - m[2], 0, 0.8) + VERS(c[3], m[2] - m[3], 0, 0.8)), EIN(l_rueck, 0.8))
        s.ersetzen(z, "$# = 2", dauer=0.8)
    s.pause(0.3)
    schritt(s, BETONE(c[0][1], 0.7), EIN(l_bl, 0.6))
    schritt(s, EIN(g.ids[1], 0.5))
    s.speichern()


# ================================================================== Abschnitt 3: Verzweigen mit if und test
W_IF = {"weiter": ("weiter hinter fi", "continues after fi", "sigue tras fi", "在 fi 之后继续", "suite après fi", "fi'den sonra devam"),
        "keine": ("keine Ausgabe", "no output", "sin salida", "无输出", "aucune sortie", "çıktı yok")}


def k10if():
    """Zwei Weichen nebeneinander. Links grep -q Kaffee einkauf.txt: Schild 0, der Weg führt über das Gleis then
    (echo "Kaffee steht drauf"), Ausgabe Kaffee steht drauf, weiter hinter fi. Rechts grep -q Butter einkauf.txt:
    Schild 1, der Weg führt am then-Gleis vorbei direkt hinter fi, keine Ausgabe (Block s3_if)."""
    s = Szene("linux/k10if", reihenfolge="anlegen")
    w = W_IF
    trenn = lin(s, (0, 2.75), (0, -1.15), HELLGRAU, 2, "6,5")

    def weiche(cx, wort, status, ausgabe):
        o = {}
        y_c, y_w, y_g, y_s, y_fi, y_e = 2.3, 1.75, 1.4, 0.85, -0.05, -0.45
        xt, xb = cx - 0.6, cx + 1.05
        o["cmd"] = chip(s, (cx, y_c), "grep -q %s einkauf.txt" % wort, DUNKEL, WEISS)
        o["if"] = tx(s, "if", (cx - chipb("grep -q %s einkauf.txt" % wort) / 2 - 0.12, y_c), TT, "right", GRAU)
        xs = cx + chipb("grep -q %s einkauf.txt" % wort) / 2 + 0.3
        o["schild"] = schild(s, xs, y_c, status)
        o["l_exit"] = L(s, "exit", W_EXIT, (xs + 0.17, y_c + 0.3), FM, "right", GRAU)
        gl = [lin(s, (cx, y_c - 0.14), (cx, y_w), GRAU, 3), lin(s, (cx, y_w), (xt, y_g), GRAU, 3), lin(s, (xt, y_g), (xt, y_s + 0.16), GRAU, 3),
              lin(s, (cx, y_w), (xb, y_g), GRAU, 3), lin(s, (xb, y_g), (xb, y_fi), GRAU, 3), lin(s, (xb, y_fi), (cx + 0.2, y_fi), GRAU, 3),
              lin(s, (xt, y_s - 0.16), (xt, y_fi), GRAU, 3), lin(s, (xt, y_fi), (cx - 0.2, y_fi), GRAU, 3)]
        o["gleise"] = gl + [s.punkt(None, cx, y_w, DUNKEL, 0.06)]
        o["then"] = tx(s, "then", (r4(xt - 0.08), r4((y_w + y_g) / 2 - 0.05)), TK, "right", DUNKEL)
        o["station"] = chip(s, (xt, y_s), 'echo "%s steht drauf"' % wort, DUNKEL, WEISS)
        o["fi"] = chip(s, (cx, y_fi), "fi", DUNKEL, WEISS, g=TT)
        o["ende"] = [pfk(s, (cx, y_fi - 0.15), (cx, y_e), GRAU, 3)]
        o["l_weiter"] = L(s, "weiter", w["weiter"], (cx, y_e - 0.2), FM, "center", GRAU)
        if status == 0:
            o["weg1"] = [lin(s, (cx, y_c - 0.14), (cx, y_w), ORANGE, 5), lin(s, (cx, y_w), (xt, y_g), ORANGE, 5),
                         lin(s, (xt, y_g), (xt, y_s + 0.16), ORANGE, 5)]
            o["weg2"] = [lin(s, (xt, y_s - 0.16), (xt, y_fi), ORANGE, 5), lin(s, (xt, y_fi), (cx - 0.2, y_fi), ORANGE, 5),
                         pfk(s, (cx, y_fi - 0.15), (cx, y_e), ORANGE, 4)]
        else:
            o["weg1"] = [lin(s, (cx, y_c - 0.14), (cx, y_w), ORANGE, 5), lin(s, (cx, y_w), (xb, y_g), ORANGE, 5),
                         lin(s, (xb, y_g), (xb, y_fi), ORANGE, 5), lin(s, (xb, y_fi), (cx + 0.2, y_fi), ORANGE, 5)]
            o["weg2"] = [pfk(s, (cx, y_fi - 0.15), (cx, y_e), ORANGE, 4)]
        if ausgabe:
            o["aus"] = [L(s, "ausg", W_AUSG, (cx - 1.5, -1.0), FM, "left", GRAU),
                        tx(s, ausgabe, (r4(cx - 1.5 + 0.75), -1.0), TK, "left", GRUEN)]
        else:
            o["aus"] = [L(s, "keine", w["keine"], (cx, -1.0), FM, "center", GRAU)]
        return o

    a = weiche(-1.75, "Kaffee", 0, "Kaffee steht drauf")
    b = weiche(1.75, "Butter", 1, "")
    for o in (a, b):
        statisch = flach(o["cmd"]) + [o["if"]] + o["gleise"] + [o["then"]] + flach(o["station"]) + flach(o["fi"]) + o["ende"] + [o["l_weiter"]]
        schritt(s, EIN(statisch + ([trenn] if o is a else []), 0.7))
        s.pause(0.3)
        schritt(s, BETONE(o["cmd"][1], 0.7))
        schritt(s, EIN(o["schild"] + [o["l_exit"]], 0.5))
        s.pause(0.3)
        schritt(s, ZEICHNE(o["weg1"], 0.9))
        if o is a:
            schritt(s, BETONE(o["station"][1], 0.7), EIN(o["aus"], 0.6))
        schritt(s, ZEICHNE(o["weg2"], 0.6))
        if o is b:
            schritt(s, EIN(o["aus"], 0.5))
        s.pause(0.6)
    s.speichern()


W_KL = {"befehl": ("Befehl", "command", "orden", "命令", "commande", "komut"),
        "frage": ("Frage", "question", "pregunta", "问题", "question", "soru"),
        "gegen": ("Gegenstand", "subject", "objeto", "对象", "objet", "nesne"),
        "schluss": ("Schlusszeichen,\nmuss das letzte\nArgument sein", "closing sign,\nmust be the last\nargument",
                    "cierre,\ndebe ser el\núltimo argumento", "结束符，\n必须是\n最后一个参数", "signe de fin,\ndoit être le\ndernier argument",
                    "kapanış işareti,\nson argüman\nolmalı"),
        "gibts": ("Befehl gibt es nicht", "no such command", "esa orden no existe", "没有这个命令", "cette commande n'existe pas",
                  "böyle bir komut yok")}


def k10klammer():
    """Die Zeile [ -f einkauf.txt ] wird in vier Wort-Kärtchen zerlegt: [ Befehl, -f Frage, einkauf.txt Gegenstand,
    ] Schlusszeichen. Der Befehl [ hält das Schild 0 hoch. Darunter [-f einkauf.txt ]: Das erste Kärtchen heißt [-f, ein
    rotes Fragezeichen, „Befehl gibt es nicht“, die Meldung [-f: command not found (Block s3_klammerfehler)."""
    s = Szene("linux/k10klammer", reihenfolge="anlegen")
    w = W_KL

    def zerlege(zeile, y_z, y_k, xs, rot0=False):
        g = s.raster(zeile, (0, y_z), groesse=22, ausrichtung="mitte")
        felder = g.felder(0)
        kisten, kopien, schiebe = [], [], []
        for f, x in zip(felder, xs):
            b = chipb(f.text, 22)
            rot = rot0 and f is felder[0]
            kisten.append(box(s, (x, y_k), b, 0.32, ROT if rot else BLAU, ROT_HELL if rot else BLAU_HELL, 2.5 if rot else 2))
        for f, x in zip(felder, xs):
            kp = g.teil(0, f.a, f.b, farbe=ROT if (rot0 and f is felder[0]) else SCHWARZ)
            kopien.append(kp)
            breite = len(f.text) * g.zelle[0]
            schiebe.append(VER(kp, x - breite / 2 - g.x(f.a), y_k - g.y(0), 0.8))
        return g, kisten, kopien, schiebe

    xs1 = [-2.55, -1.4, 0.2, 2.1]
    g1, ki1, ko1, sch1 = zerlege("[ -f einkauf.txt ]", 2.45, 1.55, xs1)
    rollen = [L(s, k, w[k], (x, 1.12 if k != "schluss" else 0.93), FM, "center", BLAU)
              for k, x in zip(("befehl", "frage", "gegen", "schluss"), xs1)]
    st = schild(s, xs1[0], 2.1, 0)
    stiel = lin(s, (xs1[0], 1.95), (xs1[0], 1.71), GRUEN, 2.5)
    l_ex = L(s, "exit", W_EXIT, (xs1[0] + 0.3, 2.1), FM, "left", GRAU)
    trenn = lin(s, (-3.3, 0.45), (3.3, 0.45), HELLGRAU, 2, "6,5")
    xs2 = [-2.55, -0.8, 1.0]
    g2, ki2, ko2, sch2 = zerlege("[-f einkauf.txt ]", 0.05, -0.75, xs2, rot0=True)
    frage = text(s, "?", (xs2[0] + 0.42, -0.72), 30, "center", ROT)
    l_gibts = L(s, "gibts", w["gibts"], (xs2[0] - 0.33, -1.15), FM, "left", ROT)
    msg = tx(s, "[-f: command not found", (xs2[0] - 0.33, -1.5), TK, "left", ROT)
    schritt(s, EIN(g1.ids, 0.6))
    s.pause(0.4)
    schritt(s, EIN(ko1, 0.3))
    schritt(s, *sch1)
    schritt(s, EIN(ki1, 0.5))
    schritt(s, EIN(rollen, 0.7))
    s.pause(0.4)
    schritt(s, EIN(st + [stiel, l_ex], 0.6))
    s.pause(0.8)
    schritt(s, EIN([trenn] + g2.ids, 0.6))
    schritt(s, EIN(ko2, 0.3))
    schritt(s, *sch2)
    schritt(s, EIN(ki2, 0.5))
    schritt(s, EIN([frage, l_gibts], 0.6))
    schritt(s, EIN(msg, 0.5))
    s.speichern()


DI_AUS = {"fotos": "fotos: ein Verzeichnis", "einkauf.txt": "einkauf.txt: eine Datei mit Inhalt", "leer.txt": "leer.txt: eine leere Datei",
          "/dev/null": "/dev/null: weder Datei noch Verzeichnis", "gibtsnicht.txt": "gibtsnicht.txt: gibt es nicht"}


def k10dateiinfo():
    """Die Kette aus dateiinfo.sh als vier Tore -d?, -f? (darin -s?), -e?, else untereinander; „nein“ führt zum nächsten
    Tor, „ja“ nach rechts zur Ausgabe. Fünf Namen laufen nacheinander hinein (fotos, einkauf.txt, leer.txt, /dev/null,
    gibtsnicht.txt) und erzeugen je genau eine Ausgabezeile (Block s3_dateiinfo)."""
    s = Szene("linux/k10dateiinfo", reihenfolge="anlegen")
    xm, ys = -2.75, {"d": 1.75, "f": 1.0, "e": 0.05, "else": -0.65}
    xi = -1.55
    ein = tx(s, "name=$1", (xm, 2.6), TK, "center", GRAU)
    tore = {k: chip(s, (xm, y), "-%s?" % k if k != "else" else "else", BLAU if k != "else" else GRAU,
                    BLAU_HELL if k != "else" else WEISS, g=TT, b=0.62, h=0.32) for k, y in ys.items()}
    s_tor = chip(s, (xi, ys["f"]), "-s?", BLAU, BLAU_HELL, g=TT, b=0.62, h=0.32)
    neins = []
    folge = ["d", "f", "e", "else"]
    linien = [pfk(s, (xm, 2.45), (xm, ys["d"] + 0.17), GRAU, 2)]
    for a, b in zip(folge, folge[1:]):
        linien.append(pfk(s, (xm, ys[a] - 0.17), (xm, ys[b] + 0.17), GRAU, 2))
        neins.append(L(s, "nein", W_NEIN, (xm + 0.1, (ys[a] + ys[b]) / 2), FM, "left", GRAU))
    xa = -1.85
    ja = []
    for k in ("d", "e", "else"):
        linien.append(pfk(s, (xm + 0.32, ys[k]), (xa, ys[k]), GRAU, 2))
        if k != "else":
            ja.append(L(s, "ja", W_JA, ((xm + xa) / 2, ys[k] + 0.15), FM, "center", GRAU))
    linien.append(pfk(s, (xm + 0.32, ys["f"]), (xi - 0.32, ys["f"]), GRAU, 2))
    ja.append(L(s, "ja", W_JA, ((xm + xi) / 2 + 0.1, ys["f"] + 0.15), FM, "center", GRAU))
    ya, yn = 1.33, 0.67
    xs_ = -1.0
    linien += [pfk(s, (xi, ys["f"] + 0.16), (xs_, ya), GRAU, 2, knick="vh"), pfk(s, (xi, ys["f"] - 0.16), (xs_, yn), GRAU, 2, knick="vh")]
    ja += [L(s, "ja", W_JA, ((xi + xs_) / 2, ya + 0.13), FM, "center", GRAU),
           L(s, "nein", W_NEIN, ((xi + xs_) / 2, yn - 0.13), FM, "center", GRAU)]
    ziele = {"fotos": (xa + 0.08, ys["d"]), "einkauf.txt": (xs_ + 0.08, ya), "leer.txt": (xs_ + 0.08, yn),
             "/dev/null": (xa + 0.08, ys["e"]), "gibtsnicht.txt": (xa + 0.08, ys["else"])}
    wege = {"fotos": ["d"], "einkauf.txt": ["d", "f", "s"], "leer.txt": ["d", "f", "s"], "/dev/null": ["d", "f", "e"],
            "gibtsnicht.txt": ["d", "f", "e", "else"]}
    schritt(s, EIN([ein] + flach(list(tore.values())) + flach(s_tor) + linien + neins + ja, 0.8))
    s.pause(0.6)
    for name in ("fotos", "einkauf.txt", "leer.txt", "/dev/null", "gibtsnicht.txt"):
        x0, y0 = xm - 0.95, 2.3
        c = chip(s, (x0, y0), name, ORANGE, ORANGE_HELL)
        weg = wege[name]
        letztes = weg[-1]
        if letztes == "s":
            zw = (xi, ys["f"] + (0.42 if name == "einkauf.txt" else -0.42))
        else:
            zw = (xm - 0.95, ys[letztes])
        aus = tx(s, DI_AUS[name], ziele[name], TK, "left", DUNKEL)
        schritt(s, EIN(c, 0.4))
        schritt(s, *VERS(c, zw[0] - x0, zw[1] - y0, 0.8))
        schritt(s, AUS(c, 0.5), EIN(aus, 0.5))
        s.pause(0.25)
    s.speichern()


W_LF = {"weg": ("verschwindet", "disappears", "desaparece", "消失了", "disparaît", "kaybolur"),
        "bleibt": ("leeres Wort bleibt", "empty word stays", "la palabra vacía se queda", "空词保留", "le mot vide reste",
                   "boş sözcük kalır"),
        "w2": ("2 Wörter", "2 words", "2 palabras", "2 个词", "2 mots", "2 sözcük"),
        "w1": ("1 Wort", "1 word", "1 palabra", "1 个词", "1 mot", "1 sözcük")}


def k10leerfalle():
    """Oben leer= und zwei Zeilen: [ $leer = Anna ] (das Kärtchen $leer verschwindet, es bleiben =, Anna, ]; Schild 2,
    unary operator expected) und [ "$leer" = Anna ] (ein leeres Kärtchen bleibt, Schild 1, falsch). Darunter
    datei="mein einkauf.txt": [ -f $datei ] zerfällt in zwei Kärtchen (Schild 2, binary operator expected),
    [ -f "$datei" ] bleibt eines (Schild 0). Werte aus Block s3_leerfalle."""
    s = Szene("linux/k10leerfalle", reihenfolge="anlegen")
    w = W_LF
    trenn = [lin(s, (0, 2.6), (0, 0.7), HELLGRAU, 2, "6,5"), lin(s, (-3.3, 0.62), (3.3, 0.62), HELLGRAU, 2, "6,5"),
             lin(s, (0, 0.2), (0, -1.6), HELLGRAU, 2, "6,5")]
    # oben
    a1 = tx(s, "leer=", (0, 2.85), TK, "center", GRAU)
    t_l = tx(s, "[ $leer = Anna ]", (-1.75, 2.42), TT)
    t_r = tx(s, '[ "$leer" = Anna ]', (1.75, 2.42), TT)
    yk = 1.87
    wl = ["[", "$leer", "=", "Anna", "]"]
    xl, bl = reihe(wl, mitte=-1.75, luecke=0.12)
    kl = [chip(s, (x, yk), t, BLAU if i else DUNKEL, BLAU_HELL if i else WEISS) for i, (x, t) in enumerate(zip(xl, wl))]
    l_weg = L(s, "weg", w["weg"], (xl[1], yk - 0.33), FM, "center", GRAU)
    dx = -(bl[1] + 0.12)
    wr = ["[", '"$leer"', "=", "Anna", "]"]
    xr, br = reihe(wr, mitte=1.75, luecke=0.12)
    kr = [chip(s, (x, yk), t, BLAU if i else DUNKEL, BLAU_HELL if i else WEISS) for i, (x, t) in enumerate(zip(xr, wr))]
    l_bl = L(s, "bleibt", w["bleibt"], (xr[1], yk - 0.33), FM, "center", BLAU)
    s_l = schild(s, -3.05, 1.18, 2)
    m_l = tx(s, "bash: [: =: unary operator expected", (-2.8, 1.18), TK, "left", ROT)
    s_r = schild(s, 0.55, 1.18, 1)
    m_r = L(s, "falsch", W_FALSCH, (0.82, 1.18), FM, "left", ROT)
    # unten
    a2 = tx(s, 'datei="mein einkauf.txt"', (0, 0.4), TK, "center", GRAU)
    u_l = tx(s, "[ -f $datei ]", (-1.75, 0.0), TT)
    u_r = tx(s, '[ -f "$datei" ]', (1.75, 0.0), TT)
    yu = -0.55
    wu = ["[", "-f", "mein", "einkauf.txt", "]"]
    xu, bu = reihe(wu, mitte=-1.75, luecke=0.12)
    vor = ["[", "-f", "$datei", "]"]
    xv, _ = reihe(vor, mitte=-1.75, luecke=0.12)
    kv = [chip(s, (x, yu), t, BLAU if i else DUNKEL, BLAU_HELL if i else WEISS) for i, (x, t) in enumerate(zip(xv, vor))]
    kn = [chip(s, (xu[k], yu), wu[k], ORANGE, ORANGE_HELL) for k in (2, 3)]
    wr2 = ["[", "-f", '"$datei"', "]"]
    xr2, _ = reihe(["[", "-f", "mein einkauf.txt", "]"], mitte=1.75, luecke=0.12)
    kr2 = [chip(s, (x, yu), t, BLAU if i else DUNKEL, BLAU_HELL if i else WEISS, b=(chipb("mein einkauf.txt") if i == 2 else None))
           for i, (x, t) in enumerate(zip(xr2, wr2))]
    l_w2 = L(s, "w2", w["w2"], ((xu[2] + xu[3]) / 2, yu - 0.33), FM, "center", ORANGE)
    l_w1 = L(s, "w1", w["w1"], (xr2[2], yu - 0.33), FM, "center", BLAU)
    s_u = schild(s, -3.05, -1.2, 2)
    m_u = tx(s, "bash: [: mein: binary operator expected", (-3.3, -1.55), TK, "left", ROT)
    s_u2 = schild(s, 0.55, -1.2, 0)
    schritt(s, EIN(trenn[:2] + [a1, t_l], 0.6))
    schritt(s, EIN(flach(kl), 0.6))
    s.pause(0.3)
    schritt(s, AUS(kl[1], 0.7), EIN(l_weg, 0.7))
    schritt(s, *[v for c in kl[2:] for v in VERS(c, dx, 0, 0.7)])
    schritt(s, EIN(s_l + [m_l], 0.6))
    s.pause(0.6)
    schritt(s, EIN([t_r] + flach(kr), 0.6))
    s.ersetzen(kr[1][1], '""', dauer=0.7)
    schritt(s, EIN(l_bl, 0.5))
    schritt(s, EIN(s_r + [m_r], 0.6))
    s.pause(0.8)
    schritt(s, EIN([trenn[2], a2, u_l] + flach(kv), 0.6))
    s.pause(0.3)
    schritt(s, AUS(kv[2], 0.6), EIN(flach(kn), 0.6), *(VERS(kv[0], xu[0] - xv[0], 0, 0.6) + VERS(kv[1], xu[1] - xv[1], 0, 0.6) +
                                                        VERS(kv[3], xu[4] - xv[3], 0, 0.6)))
    schritt(s, EIN(l_w2, 0.5))
    schritt(s, EIN(s_u + [m_u], 0.6))
    s.pause(0.6)
    schritt(s, EIN([u_r] + flach(kr2), 0.6))
    s.ersetzen(kr2[2][1], "mein einkauf.txt", dauer=0.7)
    schritt(s, EIN(l_w1, 0.5))
    schritt(s, EIN(s_u2, 0.5))
    s.speichern()


W_ZT = {"zahlen": ("als Zahlen", "as numbers", "como números", "作为数字", "comme nombres", "sayı olarak"),
        "texte": ("als Texte", "as text", "como textos", "作为文本", "comme textes", "metin olarak"),
        "links": ("liegt 10 links von 9?", "is 10 left of 9?", "¿está 10 a la izquierda de 9?", "10 在 9 的左边吗？",
                  "10 est-il à gauche de 9 ?", "10, 9'un solunda mı?"),
        "vor": ("steht 10 vor 9?", "does 10 come before 9?", "¿va 10 antes que 9?", "10 排在 9 前面吗？", "10 vient-il avant 9 ?",
                "10, 9'dan önce mi gelir?"),
        "wb": ("Wörterbuch-Reihenfolge", "dictionary order", "orden de diccionario", "词典顺序", "ordre du dictionnaire", "sözlük sırası"),
        "erstes": ("das erste Zeichen\nentscheidet", "the first character\ndecides", "decide el\nprimer carácter", "由第一个字符\n决定",
                   "le premier caractère\ndécide", "ilk karakter\nbelirler")}


def k10zahltext():
    """Links „als Zahlen“: Zahlenstrahl 0 bis 12, Marken 9 und 10; [ 10 -lt 9 ] fragt „liegt 10 links von 9?“: nein,
    Schild 1. Rechts „als Texte“: die Liste 007, 10, 7, 9 in Wörterbuch-Reihenfolge, das erste Zeichen orange;
    [ 10 \\< 9 ] fragt „steht 10 vor 9?“: ja, Schild 0 (Blöcke s3_zahlen, s3_textordnung)."""
    s = Szene("linux/k10zahltext", reihenfolge="anlegen")
    w = W_ZT
    trenn = lin(s, (0.15, 2.7), (0.15, -0.1), HELLGRAU, 2, "6,5")
    h_l = [L(s, "zahlen", w["zahlen"], (-1.6, 2.55), FS, "center", DUNKEL), tx(s, "[ 10 -lt 9 ]", (-1.6, 2.15), TT)]
    x0, x1, ya = -3.2, -0.25, 1.1
    u = (x1 - x0) / 12
    achse = [lin(s, (x0, ya), (x1, ya), DUNKEL, 2.5)] + [lin(s, (x0 + k * u, ya - 0.05), (x0 + k * u, ya + 0.05), DUNKEL, 2) for k in range(13)]
    zahlen = [text(s, str(k), (r4(x0 + k * u), ya - 0.22), FM, "center", GRAU) for k in (0, 5, 9, 10, 12)]
    p9 = s.punkt(None, r4(x0 + 9 * u), ya, BLAU, 0.07)
    p10 = s.punkt(None, r4(x0 + 10 * u), ya, ORANGE, 0.07)
    q_l = L(s, "links", w["links"], (-1.6, 1.62), FM, "center", DUNKEL)
    a_l = [L(s, "nein", W_NEIN, (-1.75, 0.35), FM, "right", ROT)] + schild(s, -1.45, 0.35, 1)
    h_r = [L(s, "texte", w["texte"], (1.75, 2.55), FS, "center", DUNKEL), tx(s, "[ 10 \\< 9 ]", (1.75, 2.15), TT)]
    l_wb = L(s, "wb", w["wb"], (0.55, 1.8), FM, "left", GRAU)
    liste = ["007", "10", "7", "9"]
    xl = 0.85
    yl = [1.45, 1.13, 0.81, 0.49]
    karten = [[box(s, (xl, y), 0.6, 0.28, GRAU, WEISS, 2), txa(s, farbig(t[0], ORANGE) + t[1:], (xl, y), TT)] for t, y in zip(liste, yl)]
    r10 = box(s, (xl, yl[1]), 0.68, 0.34, ORANGE, WEISS, 2.5, deckung=0.0)
    r9 = box(s, (xl, yl[3]), 0.68, 0.34, ORANGE, WEISS, 2.5, deckung=0.0)
    p_v = bogen_x(s, (xl + 0.36, yl[1]), (xl + 0.36, yl[3]), 0.22, ORANGE, 2.5)
    l_er = L(s, "erstes", w["erstes"], (1.75, 1.38), FM, "left", ORANGE)
    q_r = L(s, "vor", w["vor"], (1.75, 0.81), FM, "left", DUNKEL)
    a_r = [L(s, "ja", W_JA, (1.85, 0.35), FM, "right", GRUEN)] + schild(s, 2.15, 0.35, 0)
    schritt(s, EIN(h_l + [trenn], 0.6))
    schritt(s, EIN(achse + zahlen, 0.7))
    schritt(s, WACHS([p9, p10], 0.5))
    schritt(s, EIN(q_l, 0.5))
    schritt(s, BETONE(p10, 0.6))
    schritt(s, EIN(a_l, 0.5))
    s.pause(0.8)
    schritt(s, EIN(h_r + [l_wb], 0.6))
    schritt(s, EIN(flach(karten), 0.7))
    schritt(s, EIN(l_er, 0.5))
    schritt(s, EIN([r10, r9, q_r], 0.6), ZEICHNE(p_v, 0.6))
    schritt(s, EIN(a_r, 0.5))
    s.speichern()


# ================================================================== Abschnitt 4: [[ ]], (( )) und case
W_DK = {"station": ("Worttrennung\nder Shell", "word splitting\nby the shell", "división en palabras\nde la shell", "shell 的\n分词",
                    "découpage en mots\npar le shell", "kabuğun\nsözcük bölmesi"),
        "faellt": ("leeres Wort\nfällt heraus", "empty word\ndrops out", "la palabra vacía\nse pierde", "空词\n被丢掉",
                   "le mot vide\ndisparaît", "boş sözcük\ndüşer"),
        "bash": ("bash prüft selbst", "bash checks itself", "bash comprueba por sí misma", "bash 自己检查", "bash vérifie lui-même",
                 "bash kendisi denetler"),
        "vorbei": ("an der Station\nvorbei", "past the\nstation", "sin pasar por\nla estación", "绕过\n这一站", "sans passer\npar l'étape",
                   "istasyonun\nyanından"),
        "muster": ("Muster passt", "pattern matches", "el patrón coincide", "模式匹配", "le motif correspond", "desen eşleşir")}


def k10doppelklammer():
    """Links [ $leer = Anna ]: Die Zeile läuft durch die Station „Worttrennung“ der Shell, das leere Wort fällt heraus,
    beim Befehl [ kommen nur =, Anna, ] an: Schild 2. Rechts [[ $leer = Anna ]]: an der Station vorbei in die bash, das
    leere Wort bleibt: Schild 1. Darunter [[ $datei == *.txt ]]: Das Muster legt sich über mein einkauf.txt, Schild 0
    (Blöcke s4_doppel, s4_muster)."""
    s = Szene("linux/k10doppelklammer", reihenfolge="anlegen")
    w = W_DK
    t_l = tx(s, "[ $leer = Anna ]", (-1.85, 2.5), TT)
    t_r = tx(s, "[[ $leer = Anna ]]", (1.85, 2.5), TT)
    st = [box(s, (-0.25, 1.85), 1.6, 0.55, ORANGE, ORANGE_HELL, 2.5, "rect"), L(s, "station", w["station"], (-0.25, 1.85), FM, "center", ORANGE)]
    p_l1 = pfk(s, (-1.85, 2.35), (-1.05, 1.95), DUNKEL, 2.5)
    p_l2 = pfk(s, (-1.05, 1.75), (-1.85, 1.3), DUNKEL, 2.5)
    p_r = pfk(s, (1.85, 2.35), (1.85, 1.45), DUNKEL, 2.5)
    l_vb = L(s, "vorbei", w["vorbei"], (1.95, 1.9), FM, "left", GRAU)
    yk = 1.07
    wl = ["[", "=", "Anna", "]"]
    xl, _ = reihe(wl, mitte=-1.95, luecke=0.12)
    kl = [chip(s, (x, yk), t, BLAU if i else DUNKEL, BLAU_HELL if i else WEISS) for i, (x, t) in enumerate(zip(xl, wl))]
    leer_l = chip(s, (-0.25, 1.45), "", HELLGRAU, WEISS, b=0.4, dash="4,4")
    l_f = L(s, "faellt", w["faellt"], (-0.25, 0.85), FM, "center", GRAU)
    s_l = schild(s, -1.95, 0.45, 2)
    bx = [box(s, (1.85, 0.95), 2.55, 0.75, BLAU, WEISS, 2, "rect"), L(s, "bash", w["bash"], (0.65, 1.2), FM, "left", BLAU)]
    wr = ['""', "=", "Anna"]
    xr, _ = reihe(wr, mitte=1.85, luecke=0.12)
    kr = [chip(s, (x, 0.85), t, BLAU, BLAU_HELL, textfarbe=GRAU if i == 0 else SCHWARZ) for i, (x, t) in enumerate(zip(xr, wr))]
    s_r = schild(s, 1.85, 0.3, 1)
    trenn = lin(s, (-3.3, -0.05), (3.3, -0.05), HELLGRAU, 2, "6,5")
    t_u = tx(s, "[[ $datei == *.txt ]]", (0, -0.35), TT)
    g = s.raster("mein einkauf.txt", (-0.4, -1.25), groesse=22, ausrichtung="mitte")
    k_st, l_st = g.klammer(0, 0, 11, "*", seite="oben", farbe=ORANGE, groesse=22, schrift="tt")
    k_tx, l_tx = g.klammer(0, 12, 15, ".txt", seite="oben", farbe=ORANGE, groesse=22, schrift="tt")
    s_u = schild(s, 1.55, -1.25, 0)
    l_m = L(s, "muster", w["muster"], (1.85, -1.25), FM, "left", GRUEN)
    schritt(s, EIN(t_l, 0.5))
    schritt(s, ZEICHNE(p_l1, 0.5), EIN(st, 0.6))
    schritt(s, EIN(leer_l, 0.4))
    schritt(s, *VERS(leer_l, 0, 1.1 - 1.45, 0.6), EIN(l_f, 0.6))
    schritt(s, AUS(leer_l, 0.4), ZEICHNE(p_l2, 0.5), EIN(flach(kl), 0.6))
    schritt(s, EIN(s_l, 0.5))
    s.pause(0.7)
    schritt(s, EIN(t_r, 0.5))
    schritt(s, ZEICHNE(p_r, 0.6), EIN(l_vb, 0.6))
    schritt(s, EIN(bx + flach(kr), 0.6))
    schritt(s, EIN(s_r, 0.5))
    s.pause(0.7)
    schritt(s, EIN([trenn, t_u] + g.ids, 0.6))
    schritt(s, ZEICHNE([k_st, k_tx], 0.6), EIN([l_st, l_tx], 0.6))
    schritt(s, EIN(s_u + [l_m], 0.5))
    s.speichern()


W_RX = {"anf": ("Anfang", "start", "inicio", "开头", "début", "başlangıç"),
        "ende": ("Ende", "end", "fin", "结尾", "fin", "son"),
        "mehr": ("eine oder mehr Ziffern", "one or more digits", "uno o más dígitos", "一个或多个数字", "un ou plusieurs chiffres",
                 "bir ya da daha çok rakam"),
        "ganz": ("passt ganz", "matches fully", "coincide entero", "完全匹配", "correspond en entier", "tamamen eşleşir"),
        "haengt": ("hängt am x", "stuck at x", "se atasca en la x", "卡在 x", "bloqué sur x", "x'te takılır"),
        "keine": ("keine Ziffer", "no digit", "ningún dígito", "没有数字", "aucun chiffre", "rakam yok")}


def k10regex():
    """Der Ausdruck ^[0-9]+$ groß als Schablone mit drei Teilen: Anfang, eine oder mehr Ziffern, Ende. Drei Eingaben
    werden nacheinander daruntergeschoben: 42 füllt sie ganz (grün, Schild 0), 4x2 hängt am x (Schild 1), die leere
    Eingabe hat keine Ziffer (Schild 1) (Block s4_regex)."""
    s = Szene("linux/k10regex", reihenfolge="anlegen")
    w = W_RX
    g = s.raster(farbig("^", BLAU) + farbig("[0-9]+", ORANGE) + farbig("$", BLAU), (0.3, 2.0), groesse=36, ausrichtung="mitte")
    k_m, _ = g.klammer(0, 1, 6, "", seite="oben", farbe=ORANGE, dicke=2.5)
    l_m = L(s, "mehr", w["mehr"], (g.xm(1, 6), r4(g.oben(0) + 0.32)), FM, "center", ORANGE)
    l_a = L(s, "anf", w["anf"], (r4(g.x(0) - 0.12), g.y(0)), FM, "right", BLAU)
    l_e = L(s, "ende", w["ende"], (r4(g.xr(7) + 0.12), g.y(0)), FM, "left", BLAU)
    xm = g.xm(1, 6)
    zeilen = [("42", 0, "ganz"), ("4x2", 1, "haengt"), ("", 1, "keine")]
    ys = [1.1, 0.35, -0.4]
    objs = []
    for (eing, st, key), y in zip(zeilen, ys):
        o = {"zuw": tx(s, "eingabe=" + eing, (-3.3, y), TK, "left", GRAU)}
        x_start = -1.15
        if eing:
            o["chip"] = [box(s, (x_start, y), chipb(eing, TT), 0.28, GRAU, WEISS, 2), txa(s, eing, (x_start, y), TT)]
        else:
            o["chip"] = chip(s, (x_start, y), "", ROT, WEISS, g=TT, b=0.5, dash="4,4")
        o["schieben"] = VERS(o["chip"], xm - x_start, 0, 0.7)
        o["farbe"] = None                     # gefärbte Fassung an der Endlage (ersetzt den verschobenen Text)
        if eing == "42":
            o["mark"] = [box(s, (g.xm(0, 7), y), r4(g.xr(7) - g.x(0)), 0.4, GRUEN, WEISS, 2.5, deckung=0.0)]
            o["farbe"] = txa(s, farbig("42", GRUEN), (xm, y), TT)
        elif eing == "4x2":
            o["mark"] = [box(s, (xm, y), 0.11, 0.3, ROT, WEISS, 2, deckung=0.0)]
            o["farbe"] = txa(s, farbig("4", GRUEN) + farbig("x", ROT) + farbig("2", "grau"), (xm, y), TT)
        else:
            o["mark"] = [box(s, (xm, y), 0.6, 0.4, ROT, WEISS, 2.5, deckung=0.0)]
        o["schild"] = schild(s, 1.75, y, st)
        o["lab"] = L(s, key, w[key], (2.05, y), FM, "left", GRUEN if st == 0 else ROT)
        objs.append(o)
    schritt(s, EIN(g.ids, 0.6))
    schritt(s, EIN([l_a, l_e], 0.6), ZEICHNE(k_m, 0.6), EIN(l_m, 0.6))
    s.pause(0.6)
    for o in objs:
        schritt(s, EIN([o["zuw"]] + o["chip"], 0.5))
        schritt(s, *o["schieben"])
        if o["farbe"]:
            schritt(s, EIN(o["mark"] + [o["farbe"]], 0.5), AUS(o["chip"][1], 0.5))
        else:
            schritt(s, EIN(o["mark"], 0.5))
        schritt(s, EIN(o["schild"] + [o["lab"]], 0.5))
        s.pause(0.4)
    s.speichern()


W_DR = {"arith": ("Arithmetik", "arithmetic", "aritmética", "算术", "arithmétique", "aritmetik"),
        "wert": ("Wert", "value", "valor", "值", "valeur", "değer"),
        "regel": ("Wert 0 → Status 1, jeder andere Wert → Status 0", "value 0 → status 1, any other value → status 0",
                  "valor 0 → estado 1, cualquier otro valor → estado 0", "值 0 → 状态 1，其他任何值 → 状态 0",
                  "valeur 0 → code 1, toute autre valeur → code 0", "değer 0 → durum 1, başka her değer → durum 0")}


def k10doppelrund():
    """Ein Übersetzer zwischen zwei Welten: links „Arithmetik“ mit 10 < 9 (Wert 0), 3 + 4 (Wert 7) und
    n > 3 && n < 10 mit n=5 (Wert 1); durch das Tor (( )) nach rechts „Exit-Status“: Wert 0 wird Status 1 (falsch),
    jeder andere Wert Status 0 (wahr) (Block s4_arith)."""
    s = Szene("linux/k10doppelrund", reihenfolge="anlegen")
    w = W_DR
    kopf = [L(s, "arith", w["arith"], (-2.2, 2.5), FS, "center", DUNKEL), L(s, "exit", W_EXIT, (2.2, 2.5), FS, "center", DUNKEL),
            L(s, "wert", w["wert"], (-0.95, 2.1), FM, "center", GRAU)]
    tor = [box(s, (0.3, 1.0), 0.75, 2.05, GRAU, GRAU_HELL, 2, "rect"), tx(s, "(( ))", (0.3, 2.2), TT, "center", DUNKEL)]
    zeilen = [("10 < 9", "0", 1), ("3 + 4", "7", 0), ("n > 3 && n < 10", "1", 0)]
    ys = [1.65, 1.0, 0.35]
    n5 = tx(s, "n=5", (-3.3, 0.62), TK, "left", GRAU)
    reihen = []
    for (aus, wv, st), y in zip(zeilen, ys):
        e = tx(s, aus, (-3.3, y), TT, "left")
        p1 = pfk(s, (-3.3 + ttb(aus, TT) + 0.1, y), (-1.22, y), GRAU, 2)
        wc = chip(s, (-0.95, y), wv, GRAU, GELB, g=TT, b=0.42)
        p2 = pfk(s, (-0.7, y), (1.3, y), DUNKEL, 2.5)
        sc = schild(s, 1.55, y, st)
        lab = L(s, "f%d" % st, W_FALSCH if st else W_WAHR, (1.85, y), FM, "left", ROT if st else GRUEN)
        reihen.append((e, p1, wc, p2, sc, lab))
    regel = L(s, "regel", w["regel"], (0, -0.35), FM, "center", DUNKEL)
    schritt(s, EIN(kopf, 0.6))
    schritt(s, EIN(tor, 0.6))
    s.pause(0.4)
    for k, (e, p1, wc, p2, sc, lab) in enumerate(reihen):
        schritt(s, EIN([e] + ([n5] if k == 2 else []), 0.5))
        schritt(s, ZEICHNE(p1, 0.4), EIN(wc, 0.5))
        schritt(s, ZEICHNE(p2, 0.6))
        schritt(s, EIN(sc + [lab], 0.5))
        s.pause(0.3)
    schritt(s, EIN(regel, 0.6))
    s.speichern()


W_VK = {"dreht": ("! dreht den Status um", "! reverses the status", "! invierte el estado", "! 把状态反过来", "! inverse le code",
                  "! durumu tersine çevirir"),
        "nur0": ("zweite Prüfung nur nach 0", "second check only after 0", "segunda prueba solo tras 0", "只有得到 0 才做第二个检查",
                 "second test seulement après 0", "ikinci denetim yalnızca 0'dan sonra"),
        "ein": ("ein Befehl, zwei Teile", "one command, two parts", "una orden, dos partes", "一个命令，两部分", "une commande, deux parties",
                "tek komut, iki kısım"),
        "leer": ("leer", "empty", "vacío", "空", "vide", "boş"),
        "erg": ("Ergebnis", "result", "resultado", "结果", "résultat", "sonuç")}


def k10verknuepfen():
    """Drei Reihen (Block s4_verkn). Oben ! grep -q Butter einkauf.txt: grep hält 1 hoch, ! dreht es zu 0. Mitte
    [ -f einkauf.txt ] && [ -s einkauf.txt ]: zwei Prüfungen, die zweite nur, weil die erste 0 meldet; Ergebnis 0.
    Unten [[ -f einkauf.txt && -s leer.txt ]]: beide Teile in einem Befehl, der zweite liefert „leer“; Ergebnis 1."""
    s = Szene("linux/k10verknuepfen", reihenfolge="anlegen")
    w = W_VK
    y1, y2, y3 = 1.95, 0.75, -0.3
    g0 = s.raster("!", (-3.3, y1), groesse=TT, farbe=ORANGE)                    # das ! als eigener Text (betonen)
    g1 = s.raster("grep -q Butter einkauf.txt", (r4(-3.3 + 2 * tt_breite(TT, 1)), y1), groesse=TT)
    g2 = s.raster("[ -f einkauf.txt ] && [ -s einkauf.txt ]", (-3.3, y2), groesse=TT)
    g3 = s.raster("[[ -f einkauf.txt && -s leer.txt ]]", (-3.3, y3), groesse=TT)
    xe = r4(g2.rechts + 0.75)                 # Spalte der Ergebnisse

    def ergebnis(g, y, n):
        return [pfk(s, (g.rechts + 0.12, y), (xe - 0.2, y), DUNKEL, 2.5)] + schild(s, xe, y, n)

    r1 = [g0.rahmen(0, 0, 0, ORANGE, 2.5), g1.rahmen(0, 0, 25, DUNKEL, 2)]
    s1 = schild(s, g1.xm(0, 25), r4(y1 + 0.42), 1)
    e1 = ergebnis(g1, y1, 0)
    l1 = L(s, "dreht", w["dreht"], (xe + 0.3, y1), FM, "left", ORANGE)
    r2a, r2b = g2.rahmen(0, 0, 17, DUNKEL, 2), g2.rahmen(0, 22, 39, DUNKEL, 2)
    s2a = schild(s, g2.xm(0, 17), r4(y2 + 0.42), 0)
    s2b = schild(s, g2.xm(22, 39), r4(y2 + 0.42), 0)
    p2 = pfk(s, (g2.xm(0, 17) + 0.22, r4(y2 + 0.42)), (g2.xm(22, 39) - 0.22, r4(y2 + 0.42)), GRUEN, 2.5)
    l2 = L(s, "nur0", w["nur0"], (g2.xm(19, 20), r4(y2 + 0.68)), FM, "center", GRUEN)
    e2 = ergebnis(g2, y2, 0)
    r3 = g3.rahmen(0, 0, 34, DUNKEL, 2)
    m3a = g3.markieren(0, 3, 16, GRUEN, 0.25)
    m3b = g3.markieren(0, 21, 31, ROT, 0.25)
    h3 = haken(s, g3.xm(3, 16), r4(y3 - 0.33), GRUEN, 0.08, 3.5)
    l3b = L(s, "leer", w["leer"], (g3.xm(21, 31), r4(y3 - 0.33)), FM, "center", ROT)
    e3 = ergebnis(g3, y3, 1)
    l3 = L(s, "ein", w["ein"], (xe + 0.3, y3), FM, "left", GRAU)
    l_erg = L(s, "erg", w["erg"], (xe, r4(y1 + 0.42)), FM, "center", GRAU)
    ausr = g0.ids[0]
    schritt(s, EIN(g0.ids + g1.ids + r1, 0.6))
    schritt(s, EIN(s1, 0.5))
    schritt(s, BETONE(ausr, 0.6))
    schritt(s, EIN(e1 + [l1, l_erg], 0.6))
    s.pause(0.7)
    schritt(s, EIN(g2.ids + [r2a, r2b], 0.6))
    schritt(s, EIN(s2a, 0.5))
    schritt(s, ZEICHNE(p2, 0.5), EIN(l2, 0.5))
    schritt(s, EIN(s2b, 0.5))
    schritt(s, EIN(e2, 0.5))
    s.pause(0.7)
    schritt(s, EIN(g3.ids + [r3], 0.6))
    schritt(s, EIN([m3a] + h3, 0.5))
    schritt(s, EIN([m3b, l3b], 0.5))
    schritt(s, EIN(e3 + [l3], 0.5))
    s.speichern()


W_CA = {"stopp": ("nach dem ersten\nTreffer weiter\nhinter esac", "after the first\nmatch, go on\nafter esac",
                  "tras la primera\ncoincidencia,\nsigue tras esac", "第一次匹配后\n跳到 esac\n之后继续",
                  "après la première\ncorrespondance,\nsuite après esac", "ilk eşleşmeden\nsonra esac'tan\nsonra devam"),
        "auff": ("Auffangfall", "catch-all", "caso por defecto", "兜底", "cas par défaut", "genel durum")}
CASE_AUS = ["strand 1.jpg: ein Bild", "einkauf.txt: ein Text", "notiz.TXT: unbekannte Art"]


def k10case():
    """Sortieranlage aus art.sh: ein senkrechtes Band mit vier Fächern *.jpg | *.jpeg | *.png, *.txt, *.csv und *.
    strand 1.jpg fällt ins erste Fach, einkauf.txt rollt am ersten vorbei ins zweite, notiz.TXT an allen vorbei ins
    Auffangfach *. Hinter jedem Fach ein Stopper ;; mit dem Weg zu esac: Nach dem ersten Treffer wird nichts weiter
    geprüft. Unten die Ausgaben (Block s4_case)."""
    s = Szene("linux/k10case", reihenfolge="anlegen")
    w = W_CA
    xb, xp = -0.7, -1.35
    ys = [1.6, 0.85, 0.1, -0.65]
    muster = ["*.jpg | *.jpeg | *.png", "*.txt", "*.csv", "*"]
    kopf = tx(s, 'case "$1" in', (-3.3, 2.35), TT, "left", DUNKEL)
    band = lin(s, (xb, 2.15), (xb, ys[3]), GRAU, 4)
    mus = [chip(s, (r4(xp - chipb(m) / 2), y), m, BLAU, BLAU_HELL) for m, y in zip(muster, ys)]
    xf, bf, xs_, xe = 0.45, 1.2, 1.3, 1.68
    faecher_ = []
    for y in ys:
        faecher_ += [pfk(s, (xb, y), (r4(xf - bf / 2 - 0.03), y), GRAU, 2),
                     box(s, (xf, y), bf, 0.34, GRAU, GRAU_HELL, 2, "rect"),
                     tx(s, ";;", (xs_, y), TT, "center", ROT), pfk(s, (xs_ + 0.15, y), (xe, y), GRAU, 2)]
    esac = [lin(s, (xe, ys[0] + 0.15), (xe, -1.05), GRAU, 3), tx(s, "esac", (xe, -1.2), TT, "center", DUNKEL)]
    l_st = L(s, "stopp", w["stopp"], (1.85, 0.5), FM, "left", ROT)
    l_auf = L(s, "auff", w["auff"], (r4(xp - chipb("*") - 0.12), ys[3]), FM, "right", GRAU)
    g = s.raster(CASE_AUS, (-3.3, -1.65), groesse=TK, zeilenabstand=1.45)
    schritt(s, EIN([kopf, band] + flach(mus) + faecher_ + esac + [l_auf], 0.8))
    schritt(s, EIN(l_st, 0.5))
    s.pause(0.6)
    namen = [("strand 1.jpg", 0), ("einkauf.txt", 1), ("notiz.TXT", 3)]
    for k, (name, ziel) in enumerate(namen):
        c = chip(s, (xb, 2.35), name, ORANGE, ORANGE_HELL)
        schritt(s, EIN(c, 0.4))
        schritt(s, *VERS(c, 0, ys[ziel] - 2.35, 0.5 + 0.25 * ziel))
        schritt(s, *VERS(c, xf - xb, 0, 0.5))
        schritt(s, BETONE(faecher_[4 * ziel + 2], 0.6), EIN(g.ids[k], 0.6))
        s.pause(0.3)
    s.speichern()


# ================================================================== Abschnitt 5: Schleifen
FOR_ZEILEN = ["for tag in Montag Mittwoch Freitag", "do", '    echo "Training am $tag"', "done"]
W_FO = {"stapel": ("Stapel", "stack", "pila", "一叠卡片", "pile", "deste"),
        "leer": ("Stapel leer: Schleife endet", "stack empty: loop ends", "pila vacía: el bucle termina", "卡片用完：循环结束",
                 "pile vide : la boucle se termine", "deste boş: döngü biter"),
        "bleibt": ("bleibt nach der Schleife", "kept after the loop", "se conserva tras el bucle", "循环之后仍保留",
                   "reste après la boucle", "döngüden sonra kalır")}


def k10for():
    """Die Schleife for tag in Montag Mittwoch Freitag (Block s5_forzeilen) als Code oben links; drei Karteikarten auf
    einem Stapel. Je Durchgang wandert die oberste Karte in die Schublade tag, die Zeile echo "Training am $tag"
    leuchtet, rechts erscheint die Ausgabe. Danach ist der Stapel leer, done endet die Schleife, in tag liegt Freitag."""
    s = Szene("linux/k10for", reihenfolge="anlegen")
    w = W_FO
    g = s.raster(FOR_ZEILEN, (-3.3, 2.5), groesse=TK)
    m_done = g.markieren(3, 0, 3, ORANGE, 0.3)
    l_done = L(s, "leer", w["leer"], (r4(g.xr(3) + 0.2), g.y(3)), FM, "left", ORANGE)
    xs, ys = -2.45, 0.85
    l_st = L(s, "stapel", w["stapel"], (xs, ys + 0.5), FM, "center", GRAU)
    platz = box(s, (xs, ys), 0.98, 0.34, HELLGRAU, WEISS, 1.5, "rect", "4,4")
    sb = schublade(s, 0.0, ys, "tag", slot=10)
    p_sb = pfk(s, (xs + 0.58, ys), (r4(-sb["b"] / 2 - 0.02), ys), GRAU, 2)
    tage = ["Freitag", "Mittwoch", "Montag"]
    karten = {}
    for i, t in enumerate(tage):
        karten[t] = chip(s, (r4(xs + 0.08 * (1 - i)), r4(ys - 0.06 * (1 - i))), t, GRAU, GELB, b=0.9)
    l_bl = L(s, "bleibt", w["bleibt"], (0.0, ys - 0.38), FM, "center", GRAU)
    l_aus = L(s, "ausg", W_AUSGABE, (1.35, 2.5), FM, "left", GRAU)
    aus = [tx(s, "Training am " + t, (1.35, r4(2.2 - 0.3 * i)), TK, "left", GRUEN) for i, t in enumerate(reversed(tage))]
    schritt(s, EIN(g.ids, 0.6))
    schritt(s, EIN([l_st, platz] + flach(list(karten.values())) + sb["alle"] + [p_sb, l_aus], 0.7))
    s.pause(0.6)
    vorher = None
    for i, t in enumerate(reversed(tage)):
        c = karten[t]
        j = tage.index(t)
        x0 = r4(xs + 0.08 * (1 - j))
        y0 = r4(ys - 0.06 * (1 - j))
        teile = VERS(c, sb["zx"] - x0, ys - y0, 0.8)
        if vorher:
            schritt(s, *teile, AUS(vorher, 0.5))
        else:
            schritt(s, *teile)
        schritt(s, BETONE(g.ids[2], 0.6), EIN(aus[i], 0.6))
        s.pause(0.35)
        vorher = c
    schritt(s, EIN([m_done, l_done], 0.6))
    schritt(s, EIN(l_bl, 0.5))
    s.speichern()


W_LS = {"ganz": ("ganze Namen", "whole names", "nombres completos", "完整的文件名", "noms entiers", "tam adlar"),
        "lsaus": ("Ausgabe von ls:", "output of ls:", "salida de ls:", "ls 的输出：", "sortie de ls :", "ls çıktısı:"),
        "schnitt": ("Worttrennung an Leerzeichen\nund Zeilenenden", "word splitting at spaces\nand line ends",
                    "división en palabras en espacios\ny finales de línea", "在空格和行尾处\n分词",
                    "découpage en mots aux espaces\net aux fins de ligne", "boşluklarda ve satır sonlarında\nsözcük bölme"),
        "bruch": ("Bruchstücke\nvon Namen", "pieces\nof names", "trozos\nde nombres", "文件名的\n碎片", "morceaux\nde noms", "ad\nparçaları"),
        "d2": ("2 Durchgänge", "2 iterations", "2 iteraciones", "2 次循环", "2 itérations", "2 tur"),
        "d5": ("5 Durchgänge", "5 iterations", "5 iteraciones", "5 次循环", "5 itérations", "5 tur")}


def k10lsfalle():
    """Links for foto in fotos/*.jpg: Die Pfadnamen-Erweiterung legt zwei ganze Namen in die Schleife (Block s5_fotos).
    Rechts for foto in $(ls fotos): ls liefert einen Text mit Zeilenenden \\n; die Worttrennung schneidet an jedem
    Leerzeichen und Zeilenende, fünf Stücke kommen an, vier davon sind Bruchstücke von Namen (Block s5_lsfalle)."""
    s = Szene("linux/k10lsfalle", reihenfolge="anlegen")
    w = W_LS
    trenn = lin(s, (0.05, 2.7), (0.05, -1.1), HELLGRAU, 2, "6,5")
    xl, xr = -1.7, 1.75
    h_l = tx(s, "for foto in fotos/*.jpg", (xl, 2.5), TT, "center", DUNKEL)
    h_r = tx(s, "for foto in $(ls fotos)", (xr, 2.5), TT, "center", DUNKEL)
    mu = chip(s, (xl, 1.95), "fotos/*.jpg", BLAU, BLAU_HELL)
    p_l = pfk(s, (xl, 1.78), (xl, 1.3), ORANGE, 2.5)
    l_pn = L(s, "pn2", ("Pfadnamen-\nErweiterung", "pathname\nexpansion", "expansión de\nnombres de ruta", "路径名\n扩展",
                        "développement\ndes chemins", "yol adı\ngenişletme"), (xl + 0.1, 1.55), FM, "left", ORANGE)
    ganz =[chip(s, (xl, 1.05), "fotos/strand 1.jpg", GRUEN, GRUEN_HELL), chip(s, (xl, 0.7), "fotos/strand 2.jpg", GRUEN, GRUEN_HELL)]
    l_ganz = L(s, "ganz", w["ganz"], (xl, 0.35), FM, "center", GRUEN)
    l_d2 = L(s, "d2", w["d2"], (xl, -0.85), FM, "center", DUNKEL)
    nl = farbig("\\n", ORANGE)
    streifen = "berg.png" + nl + "strand 1.jpg" + nl + "strand 2.jpg" + nl
    l_ls = L(s, "lsaus", w["lsaus"], (0.3, 2.2), FM, "left", GRAU)
    g = s.raster(streifen, (xr, 1.9), groesse=TK, ausrichtung="mitte")
    schnitte = [g.xm(8, 9), g.xm(16), g.xm(22, 23), g.xm(30), g.xm(36, 37)]
    cuts = [lin(s, (x, a), (x, b), ORANGE, 2.5) for x in schnitte for a, b in ((2.1, 1.99), (1.81, 1.7))]
    l_sch = L(s, "schnitt", w["schnitt"], (xr, 1.45), FM, "center", ORANGE)
    stuecke = [(0, 7, "berg.png"), (10, 15, "strand"), (17, 21, "1.jpg"), (24, 29, "strand"), (31, 35, "2.jpg")]
    yk = [0.98, 0.64, 0.3, -0.04, -0.38]
    xk = 1.35
    kisten, kopien, schiebe = [], [], []
    for (a, b, t), y in zip(stuecke, yk):
        rot = t != "berg.png"
        kisten.append(box(s, (xk, y), 0.88, 0.28, ROT if rot else GRAU, ROT_HELL if rot else WEISS, 2.5 if rot else 2))
    for (a, b, t), y in zip(stuecke, yk):
        kp = g.teil(0, a, b, farbe=SCHWARZ)
        kopien.append(kp)
        schiebe.append(VER(kp, xk - len(t) * g.zelle[0] / 2 - g.x(a), y - g.y(0), 0.9))
    kl = vklammer(s, xk + 0.55, r4(yk[1] + 0.12), r4(yk[4] - 0.12), ROT, 0.07, 2.5)
    l_br = L(s, "bruch", w["bruch"], (xk + 0.68, (yk[1] + yk[4]) / 2), FM, "left", ROT)
    l_d5 = L(s, "d5", w["d5"], (xr, -0.85), FM, "center", DUNKEL)
    schritt(s, EIN([trenn, h_l] + mu, 0.6))
    schritt(s, ZEICHNE(p_l, 0.5), EIN(l_pn, 0.5))
    schritt(s, EIN(flach(ganz), 0.6))
    schritt(s, EIN([l_ganz, l_d2], 0.5))
    s.pause(0.8)
    schritt(s, EIN([h_r, l_ls] + g.ids, 0.6))
    schritt(s, EIN(cuts + [l_sch], 0.6))
    schritt(s, EIN(kopien, 0.3))
    schritt(s, *schiebe)
    schritt(s, EIN(kisten, 0.5))
    schritt(s, ZEICHNE(kl, 0.5), EIN(l_br, 0.5))
    schritt(s, EIN(l_d5, 0.5))
    s.speichern()


W_FC = {"anfang": ("einmal am Anfang", "once at the start", "una vez al inicio", "开始时执行一次", "une fois au début", "başta bir kez"),
        "vor": ("vor jedem Durchgang", "before each iteration", "antes de cada iteración", "每次循环之前", "avant chaque itération",
                "her turdan önce"),
        "nach": ("nach jedem Durchgang", "after each iteration", "después de cada iteración", "每次循环之后", "après chaque itération",
                 "her turdan sonra"),
        "ende": ("Schleife endet", "loop ends", "el bucle termina", "循环结束", "la boucle se termine", "döngü biter")}


def k10forc():
    """Die Zeile for (( i = 1; i <= 3; i++ )) in drei farbige Teile zerlegt (einmal am Anfang / vor jedem Durchgang /
    nach jedem Durchgang). Darunter der Kreislauf: Start i = 1, Prüfung i <= 3 (grün), Körper echo "Runde $i" mit
    Ausgabe, Schritt i++; bei i = 4 wird die Prüfung rot, der Pfeil führt hinaus (Block s5_forc)."""
    s = Szene("linux/k10forc", reihenfolge="anlegen")
    w = W_FC
    zeile = "for (( " + farbig("i = 1", BLAU) + "; " + farbig("i <= 3", GRUEN) + "; " + farbig("i++", ORANGE) + " ))"
    g = s.raster(zeile, (0.0, 2.25), groesse=20, ausrichtung="mitte")
    ka, _ = g.klammer(0, 7, 11, "", seite="oben", farbe=BLAU, dicke=2.5)
    kv, _ = g.klammer(0, 14, 19, "", seite="unten", farbe=GRUEN, dicke=2.5)
    kn, _ = g.klammer(0, 22, 24, "", seite="oben", farbe=ORANGE, dicke=2.5)
    la = L(s, "anfang", w["anfang"], (r4(g.xr(11) + 0.05), r4(g.oben(0) + 0.3)), FM, "right", BLAU)
    lv = L(s, "vor", w["vor"], (g.xm(14, 19), r4(g.unten(0) - 0.3)), FM, "center", GRUEN)
    ln = L(s, "nach", w["nach"], (r4(g.x(22) - 0.05), r4(g.oben(0) + 0.3)), FM, "left", ORANGE)
    xc = -2.2
    yst, ypr, ykp, ysr = 1.2, 0.5, -0.2, -0.9
    start = chip(s, (xc, yst), "i = 1", BLAU, BLAU_HELL, g=TT)
    pruef = chip(s, (xc, ypr), "i <= 3 ?", GRUEN, GRUEN_HELL, g=TT)
    koerper = chip(s, (xc, ykp), 'echo "Runde $i"', DUNKEL, WEISS, g=TT)
    schr = chip(s, (xc, ysr), "i++", ORANGE, ORANGE_HELL, g=TT)
    pfe = [pfk(s, (xc, yst - 0.14), (xc, ypr + 0.14), DUNKEL, 2.5), pfk(s, (xc, ypr - 0.14), (xc, ykp + 0.14), DUNKEL, 2.5),
           pfk(s, (xc, ykp - 0.14), (xc, ysr + 0.14), DUNKEL, 2.5),
           lin(s, (xc - 0.25, ysr), (-3.3, ysr), DUNKEL, 2.5), lin(s, (-3.3, ysr), (-3.3, ypr), DUNKEL, 2.5),
           pfk(s, (-3.3, ypr), (r4(xc - chipb("i <= 3 ?", TT) / 2 - 0.02), ypr), DUNKEL, 2.5)]
    l_ja = L(s, "ja", W_JA, (xc + 0.1, (ypr + ykp) / 2), FM, "left", GRUEN)
    sb = schublade(s, 0.15, ykp, "i", slot=2, g=TT)
    wi = wert(s, sb, "1", g=TT)
    rot = box(s, (xc, ypr), r4(chipb("i <= 3 ?", TT) + 0.08), 0.36, ROT, WEISS, 3, deckung=0.0)
    p_aus = pfk(s, (r4(xc + chipb("i <= 3 ?", TT) / 2 + 0.06), ypr), (-0.75, ypr), ROT, 2.5)
    l_nein = L(s, "nein", W_NEIN, (-1.2, ypr + 0.15), FM, "center", ROT)
    l_ende = L(s, "ende", w["ende"], (-0.65, ypr), FM, "left", ROT)
    l_aus = L(s, "ausg", W_AUSGABE, (1.6, 1.2), FM, "left", GRAU)
    aus = [tx(s, "Runde %d" % k, (1.6, r4(0.9 - 0.3 * (k - 1))), TK, "left", GRUEN) for k in (1, 2, 3)]
    schritt(s, EIN(g.ids, 0.6))
    schritt(s, ZEICHNE(ka, 0.4), EIN(la, 0.5))
    schritt(s, ZEICHNE(kv, 0.4), EIN(lv, 0.5))
    schritt(s, ZEICHNE(kn, 0.4), EIN(ln, 0.5))
    s.pause(0.6)
    schritt(s, EIN(start + pruef + koerper + schr + pfe + [l_ja] + sb["alle"] + [l_aus], 0.7))
    schritt(s, BETONE(start[1], 0.5), EIN(wi, 0.5))
    for k in (1, 2, 3):
        schritt(s, BETONE(pruef[1], 0.5))
        schritt(s, BETONE(koerper[1], 0.5), EIN(aus[k - 1], 0.5))
        with s.gleichzeitig():
            schritt(s, BETONE(schr[1], 0.5))
            s.ersetzen(wi[1], str(k + 1), dauer=0.5)
    schritt(s, EIN([rot, l_nein], 0.5), ZEICHNE(p_aus, 0.5))
    schritt(s, EIN(l_ende, 0.5))
    s.speichern()


W_WH = {"ziel": ("Ziel 1000 Euro", "target 1000 euros", "objetivo 1000 euros", "目标 1000 欧元", "objectif 1000 euros", "hedef 1000 avro")}


def sparschwein(s, x, y):
    """Sparschwein aus einfachen Formen; Ergebnis (Teile, Lage des Schlitzes)."""
    t = [box(s, (x, y), 1.25, 0.8, ORANGE, ORANGE_HELL, 2.5, "round")]
    t += [lin(s, (x - 0.42, y - 0.36), (x - 0.42, y - 0.52), ORANGE, 5), lin(s, (x - 0.2, y - 0.38), (x - 0.2, y - 0.52), ORANGE, 5),
          lin(s, (x + 0.2, y - 0.38), (x + 0.2, y - 0.52), ORANGE, 5), lin(s, (x + 0.42, y - 0.36), (x + 0.42, y - 0.52), ORANGE, 5)]
    t += [box(s, (x + 0.68, y - 0.02), 0.2, 0.26, ORANGE, ORANGE_HELL, 2.5, "round"),
          s.punkt(None, r4(x + 0.38), r4(y + 0.14), DUNKEL, 0.04),
          lin(s, (x - 0.15, y + 0.4), (x + 0.15, y + 0.4), DUNKEL, 4)]
    t += [lin(s, (x + 0.15, y + 0.38), (x + 0.28, y + 0.55), ORANGE, 2.5), lin(s, (x + 0.28, y + 0.55), (x + 0.36, y + 0.35), ORANGE, 2.5)]
    return t, (x, y + 0.4)


def k10while():
    """Ein Sparschwein und ein Balken mit Zielstrich bei 1000 Euro (sparen.sh 1000 75, Block s5_while). Je Durchgang
    leuchtet die Prüfung stand < ziel ?, eine Münze +75 fällt ins Schwein, stand und monate springen weiter (75/1,
    150/2, …, 975/13, 1050/14; die Monate 3 bis 12 laufen schnell durch). Bei 1050 wird die Prüfung rot, die Schleife
    endet, unten steht die Ausgabe."""
    s = Szene("linux/k10while", reihenfolge="anlegen")
    w = W_WH
    auf = tx(s, "$ ./sparen.sh 1000 75", (-3.3, 2.6), TK, "left", GRAU)
    schwein, (xs_, ys_) = sparschwein(s, -2.4, 1.45)
    pruef = chip(s, (0.1, 2.0), "stand < ziel ?", GRUEN, GRUEN_HELL, g=TT)
    rot = box(s, (0.1, 2.0), r4(chipb("stand < ziel ?", TT) + 0.08), 0.36, ROT, WEISS, 3, deckung=0.0)
    l_nein = L(s, "nein", W_NEIN, (0.1, 1.65), FM, "center", ROT)
    s.parameter("m", 0, ganzzahlig=True)
    z_st = s.zahl(None, "75*m", (1.25, 2.15), stellen=0, vor="stand = ", groesse=FK, ausrichtung="left")
    z_mo = s.zahl(None, "m", (1.25, 1.8), stellen=0, vor="monate = ", groesse=FK, ausrichtung="left")
    x0, ya, k = -2.9, 0.45, 5.4 / 1100
    achse = [lin(s, (x0, ya), (x0 + 1100 * k, ya), GRAU, 2)] + \
            [lin(s, (x0 + v * k, ya - 0.2), (x0 + v * k, ya - 0.12), GRAU, 2) for v in (0, 500, 1000)] + \
            [text(s, str(v), (r4(x0 + v * k), ya - 0.34), FM, "center", GRAU) for v in (0, 500, 1000)]
    ziel = [lin(s, (x0 + 1000 * k, ya - 0.22), (x0 + 1000 * k, ya + 0.32), ORANGE, 2.5, "5,4"),
            L(s, "ziel", w["ziel"], (x0 + 1000 * k, ya + 0.47), FM, "center", ORANGE)]
    balken = s.linie(None, (x0, ya), ("%s+%s*m" % (x0, r4(75 * k)), ya), farbe=GRUEN, dicke=16)
    aus = tx(s, "Nach 14 Monaten sind 1050 Euro gespart.", (-3.3, -0.3), TK, "left", GRUEN)
    muenzen = []
    for _ in range(4):
        muenzen.append([s.kreis(None, xs_, r4(ys_ + 0.55), 0.21, farbe=ORANGE, dicke=2, fuellung=GELB, deckung=1.0),
                        tx(s, "+75", (xs_, r4(ys_ + 0.55)), TK, "center", DUNKEL)])
    schritt(s, EIN([auf] + schwein + pruef + [z_st, z_mo] + achse + ziel + [balken], 0.8))
    s.pause(0.6)
    folge = [1, 2, None, 13, 14]
    mi = 0
    for p in folge:
        if p is None:
            with s.gleichzeitig():
                s.verstellen("m", 12, dauer=1.6, rate="linear")
                schritt(s, BETONE(pruef[1], 1.6))
            continue
        c = muenzen[mi]
        mi += 1
        schritt(s, BETONE(pruef[1], 0.5), EIN(c, 0.4))
        with s.gleichzeitig():
            schritt(s, *VERS(c, 0, -0.5, 0.5))
            s.verstellen("m", p, dauer=0.5, rate="linear")
        schritt(s, AUS(c, 0.3))
    s.pause(0.3)
    schritt(s, EIN([rot, l_nein], 0.6))
    schritt(s, EIN(aus, 0.6))
    s.speichern()


W_BR = {"treffer": ("Treffer:\nKaffee", "match:\nKaffee", "coincidencia:\nKaffee", "命中：\nKaffee", "trouvé :\nKaffee", "eşleşme:\nKaffee"),
        "nicht": ("nicht mehr geprüft", "no longer checked", "ya no se comprueban", "不再检查", "plus vérifiés", "artık denetlenmez"),
        "datei": ("Datei: echo läuft", "file: echo runs", "archivo: se ejecuta echo", "文件：执行 echo", "fichier : echo s'exécute",
                  "dosya: echo çalışır"),
        "verz": ("Verzeichnis: gleich zum\nnächsten Durchgang", "directory: straight on\nto the next iteration",
                 "directorio: directo a\nla siguiente iteración", "目录：直接进入\n下一次循环", "répertoire : directement\nà l'itération suivante",
                 "dizin: doğrudan\nsonraki tura")}


def kreisbogen(s, cx, cy, r, w0, w1, farbe, dicke=4, marke="", dash=""):
    """Bogen auf einem Kreis von Winkel w0 nach w1 (Grad, im Uhrzeigersinn, wenn w1 < w0)."""
    a0, a1 = math.radians(w0), math.radians(w1)
    fx = "%s+%s*cos(%s+%s*t)" % (r4(cx), r4(r), r4(a0), r4(a1 - a0))
    fy = "%s+%s*sin(%s+%s*t)" % (r4(cy), r4(r), r4(a0), r4(a1 - a0))
    return s.weg(None, fx, fy, 0, 1, farbe=farbe, dicke=dicke, pfeile=marke, n=61, dash=dash, spitze=0.13)


def k10break():
    """Zwei Schleifen als Rundbahnen. Links for datei in *.txt mit break: Die Bahn läuft bis einkauf.txt, grep findet
    Kaffee, der Pfeil break führt hinaus zu done; leer.txt und mein einkauf.txt bleiben grau (Block s5_break). Rechts
    for name in * mit continue: Bei einer Datei läuft die Runde über echo, bei den Verzeichnissen bin und fotos führt die
    Abkürzung continue gleich zum Anfang des nächsten Durchgangs (Block s5_continue)."""
    s = Szene("linux/k10break", reihenfolge="anlegen")
    w = W_BR
    trenn = lin(s, (0.05, 2.7), (0.05, -1.85), HELLGRAU, 2, "6,5")
    r = 0.72
    # links: break
    cl = (-1.95, 1.05)
    h_l = tx(s, "for datei in *.txt", (cl[0], 2.5), TT, "center", DUNKEL)
    bahn_l = s.kreis(None, cl[0], cl[1], r, farbe=HELLGRAU, dicke=4)
    weg_l = kreisbogen(s, cl[0], cl[1], r, 90, 14, ORANGE, 5, "0.6")
    start_l = s.punkt(None, cl[0], r4(cl[1] + r), DUNKEL, 0.07)
    st_e = chip(s, (r4(cl[0] + r), cl[1]), "einkauf.txt", DUNKEL, WEISS)
    st_l = chip(s, (cl[0], r4(cl[1] - r)), "leer.txt", HELLGRAU, WEISS, textfarbe=GRAU)
    st_m = chip(s, (r4(cl[0] - r), cl[1]), "mein einkauf.txt", HELLGRAU, WEISS, textfarbe=GRAU)
    tr_ = L(s, "treffer", w["treffer"], (-1.15, 1.6), FM, "left", GRUEN)
    done = chip(s, (-0.55, -0.35), "done", DUNKEL, WEISS, g=TT)
    p_br = pfk(s, (r4(cl[0] + r), r4(cl[1] - 0.16)), (-0.55, -0.2), ORANGE, 3)
    l_br = tx(s, "break", (-0.45, 0.42), TT, "left", ORANGE)
    l_nicht = L(s, "nicht", w["nicht"], (cl[0], r4(cl[1] - r - 0.35)), FM, "center", GRAU)
    aus_l = tx(s, "Kaffee steht in einkauf.txt", (-3.3, -0.85), TK, "left", GRUEN)
    # rechts: continue
    cr = (1.6, 1.05)
    h_r = tx(s, "for name in *", (cr[0], 2.5), TT, "center", DUNKEL)
    bahn_r = s.kreis(None, cr[0], cr[1], r, farbe=HELLGRAU, dicke=4)
    voll = kreisbogen(s, cr[0], cr[1], r, 90, -265, GRUEN, 5, "0.35;0.8")
    abk = pfk(s, (r4(cr[0] + r - 0.12), r4(cr[1] + 0.18)), (r4(cr[0] + 0.12), r4(cr[1] + r - 0.12)), ORANGE, 3.5, "6,4", spitze=0.11)
    start_r = s.punkt(None, cr[0], r4(cr[1] + r), DUNKEL, 0.07)
    st_d = chip(s, (r4(cr[0] + r), cr[1]), "[ -d ]?", BLAU, BLAU_HELL)
    st_echo = chip(s, (cr[0], r4(cr[1] - r)), "echo", GRUEN, GRUEN_HELL)
    l_cont = tx(s, "continue", (r4(cr[0] - 0.02), r4(cr[1] + 0.22)), TK, "center", ORANGE)
    namen = [("bewertung.sh", 0), ("bin", 1), ("dateiinfo.sh", 0), ("einkauf.txt", 0), ("fotos", 1), ("leer.txt", 0)]
    xs1, _ = reihe([n for n, _ in namen[:3]], mitte=cr[0] + 0.05, luecke=0.1)
    xs2, _ = reihe([n for n, _ in namen[3:]], mitte=cr[0] + 0.05, luecke=0.1)
    pos = [(x, -0.25) for x in xs1] + [(x, -0.6) for x in xs2]
    grau = [chip(s, p, n, HELLGRAU, WEISS, textfarbe=GRAU) for (n, _), p in zip(namen, pos)]
    farbig_ = [chip(s, p, n, ORANGE if d else GRUEN, ORANGE_HELL if d else GRUEN_HELL, dicke=2.5) for (n, d), p in zip(namen, pos)]
    pkt = [txa(s, PUNKTE, (r4(xs2[2] + chipb(namen[5][0]) / 2 + 0.2), -0.6), TK)]
    leg = [box(s, (0.45, -1.15), 0.3, 0.2, GRUEN, GRUEN_HELL, 2.5), L(s, "datei", w["datei"], (0.7, -1.15), FM, "left"),
           box(s, (0.45, -1.5), 0.3, 0.2, ORANGE, ORANGE_HELL, 2.5), L(s, "verz", w["verz"], (0.7, -1.58), FM, "left")]
    schritt(s, EIN([trenn, h_l, bahn_l, start_l] + st_e + st_l + st_m, 0.7))
    s.pause(0.4)
    schritt(s, ZEICHNE(weg_l, 0.8))
    schritt(s, BETONE(st_e[1], 0.6), EIN(tr_, 0.6))
    schritt(s, ZEICHNE(p_br, 0.6), EIN([l_br, done[0], done[1]], 0.6))
    schritt(s, EIN([l_nicht, aus_l], 0.6))
    s.pause(0.8)
    schritt(s, EIN([h_r, bahn_r, start_r] + st_d + st_echo + flach(grau) + pkt, 0.7))
    s.pause(0.4)
    schritt(s, ZEICHNE(voll, 1.0), EIN(farbig_[0], 1.0), AUS(grau[0], 1.0))
    schritt(s, ZEICHNE(abk, 0.7), EIN([l_cont] + farbig_[1], 0.7), AUS(grau[1], 0.7))
    for k in range(2, 6):
        schritt(s, EIN(farbig_[k], 0.4), AUS(grau[k], 0.4))
    schritt(s, EIN(leg, 0.6))
    s.speichern()


# ================================================================== Abschnitt 6: Zeilen lesen und Listen (Phase 2b-2)
def schere(s, x, y, farbe=ORANGE):
    """Schere aus zwei Klingen und zwei Griffen, Spitze nach rechts (Ergebnis: Liste)."""
    return [lin(s, (x - 0.2, y + 0.07), (x + 0.24, y - 0.05), farbe, 3), lin(s, (x - 0.2, y - 0.07), (x + 0.24, y + 0.05), farbe, 3),
            s.kreis(None, r4(x - 0.28), r4(y + 0.09), 0.07, farbe=farbe, dicke=2.5, fuellung=WEISS, deckung=1.0),
            s.kreis(None, r4(x - 0.28), r4(y - 0.09), 0.07, farbe=farbe, dicke=2.5, fuellung=WEISS, deckung=1.0),
            s.punkt(None, r4(x), r4(y), DUNKEL, 0.025)]


def band(s, x0, x1, y):
    """Förderband: dicke graue Linie mit zwei Rollen (Ergebnis: Liste)."""
    return [lin(s, (x0, y), (x1, y), GRAU, 6)] + [s.kreis(None, r4(x), r4(y), 0.07, farbe=GRAU, dicke=2, fuellung=WEISS, deckung=1.0)
                                                for x in (x0, x1)]


def gelb(s, sb):
    """Gelber Wertzettel im Platz einer Schublade, ohne Text (der Wert kommt als wandernde Kopie)."""
    return box(s, (sb["zx"], sb["y"]), sb["bw"], 0.28, GRAU, GELB, 1.5, "rect")


W_RD = {"schnitt": ("Schnitt an jedem Leerzeichen", "cut at every space", "corte en cada espacio", "在每个空格处切开",
                    "coupé à chaque espace", "her boşlukta kesilir"),
        "drei": ("drei Wörter", "three words", "tres palabras", "三个词", "trois mots", "üç sözcük"),
        "rest": ("letzte Variable:\nder ganze Rest", "last variable:\nall the rest", "última variable:\ntodo el resto",
                 "最后一个变量：\n剩下的全部", "dernière variable :\ntout le reste", "son değişken:\nkalanın tamamı")}


def k10read():
    """Die Zeile Anna Maria Berg auf einem Förderband, Schnitte an den beiden Leerzeichen, drei Wörter. Anna wandert in die
    Schublade vorname; Maria und Berg wandern samt Leerzeichen zusammen in die letzte Schublade rest. read hält das
    Schild 0 (Block s6_readmehr, Ausgabe unten)."""
    s = Szene("linux/k10read", reihenfolge="anlegen")
    w = W_RD
    zeile = 'read -r vorname rest <<< "Anna Maria Berg"'
    cmd = tx(s, zeile, (-3.3, 2.5), TT, "left", DUNKEL)
    xs = r4(-3.3 + ttb(zeile, TT) + 0.32)
    sch = schild(s, xs, 2.5, 0)
    l_ex = L(s, "exit", W_EXIT, (r4(xs + 0.25), 2.5), FM, "left", GRAU)
    yb, yz, yv = 1.7, 1.1, 0.3
    sv = schublade(s, -1.6, yv, "vorname", slot=5, g=20)
    sr = schublade(s, 1.25, yv, "rest", slot=11, g=20)
    gv, gr = gelb(s, sv), gelb(s, sr)
    g = s.raster("Anna Maria Berg", (0.0, yb), groesse=20, ausrichtung="mitte")
    c = g.zelle[0]
    bd = band(s, -1.3, 1.3, r4(g.unten(0) - 0.17))
    cuts = [lin(s, (g.xm(k), r4(a)), (g.xm(k), r4(b)), ORANGE, 2.5) for k in (4, 10)
            for a, b in ((g.oben(0) + 0.12, g.oben(0) + 0.02), (g.unten(0) - 0.02, g.unten(0) - 0.1))]
    l_sch = L(s, "schnitt", w["schnitt"], (0.0, r4(g.oben(0) + 0.27)), FM, "center", ORANGE)
    stuecke = [(0, 3, -0.6), (5, 9, 0.0), (11, 14, 0.6)]
    kop = [g.teil(0, a, b, farbe=BLAU) for a, b, _ in stuecke]
    l_drei = L(s, "drei", w["drei"], (r4(g.xr(14) + 0.8), yz), FM, "left", GRAU)
    ziel = [sv["zx"] - 2 * c, sr["zx"] - 5 * c, sr["zx"] + c]        # linke Kante am Ziel: Anna | Maria Berg
    l_rest = L(s, "rest", w["rest"], (sr["zx"], r4(yv - 0.48)), FM, "center", ORANGE)
    aus = s.raster(['$ echo "Vorname: $vorname, Rest: $rest"', "Vorname: Anna, Rest: Maria Berg"], (-3.3, -0.75), groesse=TK)
    schritt(s, EIN(cmd, 0.6))
    schritt(s, EIN(g.ids + bd, 0.6))
    s.pause(0.4)
    schritt(s, EIN(cuts + [l_sch], 0.6))
    schritt(s, EIN(kop, 0.2))
    schritt(s, *[VER(k, dx, yz - yb, 0.7) for k, (_, _, dx) in zip(kop, stuecke)], EIN(l_drei, 0.7))
    s.pause(0.4)
    schritt(s, EIN(sv["alle"] + sr["alle"], 0.6))
    schritt(s, VER(kop[0], ziel[0] - g.x(0) + 0.6, yv - yz, 0.8), EIN(gv, 0.8), AUS(l_drei, 0.5))
    s.pause(0.3)
    schritt(s, VER(kop[1], ziel[1] - g.x(5), yv - yz, 0.8), VER(kop[2], ziel[2] - g.x(11) - 0.6, yv - yz, 0.8), EIN(gr, 0.8))
    schritt(s, EIN(l_rest, 0.6))
    s.pause(0.4)
    schritt(s, EIN(sch + [l_ex], 0.6))
    schritt(s, EIN(aus.ids, 0.6))
    s.speichern()


EINKAUF = ["Milch", "Brot", "Äpfel", "Kaffee"]
W_WR = {"lz": ("Lesezeichen", "bookmark", "marcador", "书签", "marque-page", "yer imi"),
        "ende": ("nichts mehr da: read meldet 1,\ndie Schleife endet", "nothing left: read reports 1,\nthe loop ends",
                 "no queda nada: read devuelve 1,\nel bucle termina", "没有内容了：read 返回 1，\n循环结束",
                 "plus rien : read renvoie 1,\nla boucle se termine", "bir şey kalmadı: read 1 döndürür,\ndöngü biter"),
        "kein": ("Brot: kein Zeilenende", "Brot: no line end", "Brot: sin fin de línea", "Brot：没有行尾",
                 "Brot : pas de fin de ligne", "Brot: satır sonu yok"),
        "trotz": ("Brot steht in der Variablen,\naber read meldet 1:\ndie Schleife gibt Brot nicht mehr aus",
                  "Brot is in the variable,\nbut read reports 1:\nthe loop no longer prints Brot",
                  "Brot está en la variable,\npero read devuelve 1:\nel bucle ya no imprime Brot",
                  "Brot 已在变量中，\n但 read 返回 1：\n循环不再输出 Brot",
                  "Brot est dans la variable,\nmais read renvoie 1 :\nla boucle n'affiche plus Brot",
                  "Brot değişkende,\nama read 1 döndürür:\ndöngü Brot'u artık yazdırmaz")}


def k10whileread():
    """Oben die Datei einkauf.txt (s.datei) mit Zeilenenden \\n und einem Lesezeichen; ein Rohr < einkauf.txt führt in den
    Kasten der Schleife mit der Schublade zeile. Je Durchgang wandert die Zeile am Lesezeichen in die Schublade, das
    Lesezeichen rückt weiter, rechts erscheint - Milch … - Kaffee (Block s6_whileread). Danach greift read ins Leere:
    Schild 1, die Schublade ist leer, die Schleife endet. Unten ohne_ende.txt: Brot ohne Zeilenende landet in der
    Schublade, read meldet trotzdem 1, ausgegeben wird nur - Milch (Block s6_ohneende)."""
    s = Szene("linux/k10whileread", reihenfolge="anlegen")
    w = W_WR
    c = tt_breite(TT, 1)
    xb, xo = 0.65, 2.05

    def schleife(y, h, d, quelle):
        o = {"rohr": pfk(s, (r4(d.rechts + 0.05), y), (r4(xb - 1.17), y), BLAU, 4.5),
             "r_lab": tx(s, "< " + quelle, (r4((d.rechts + xb - 1.15) / 2), r4(y + 0.2)), TK, "center", BLAU),
             "box": pbox(s, (xb, y), 2.3, h),
             "titel": tx(s, "while read -r zeile", (r4(xb - 1.07), r4(y + h / 2 - 0.22)), TK, "left", BLAU)}
        o["sb"] = schublade(s, r4(xb - 0.4), r4(y - h / 2 + 0.3), "zeile", slot=6, g=TT)
        o["gelb"] = gelb(s, o["sb"])
        o["s0"] = schild(s, r4(xb + 0.8), r4(y + h / 2 - 0.22), 0)
        o["s1"] = schild(s, r4(xb + 0.8), r4(y + h / 2 - 0.22), 1)
        return o

    def hin(d, k, z, sb):
        return VER(k, sb["zx"] - len(z) * c / 2 - d.x(0), sb["y"] - d.y(EINKAUF.index(z) if d is d1 else ["Milch", "Brot"].index(z)), 0.6)

    cmd = tx(s, 'while read -r zeile; do echo "- $zeile"; done < einkauf.txt', (-3.3, 2.65), TK, "left", DUNKEL)
    d1 = s.datei("einkauf.txt", "\n".join(EINKAUF), pos=(-3.3, 2.4), spalten=16, zeilen=5, groesse=TT)
    dy = d1.zelle[1]
    nls = [tx(s, "\\n", (r4(d1.x(len(z)) + 0.03), d1.y(i)), TK, "left", ORANGE) for i, z in enumerate(EINKAUF)]
    o1 = schleife(1.8, 1.0, d1, "einkauf.txt")
    kop = [d1.teil(i, 0, len(z) - 1, farbe=SCHWARZ) for i, z in enumerate(EINKAUF)]
    lz = d1.markieren(0, 0, 15, ORANGE, 0.3)
    l_lz = L(s, "lz", w["lz"], (d1.links, r4(d1.unten_kante - 0.17)), FM, "left", ORANGE)
    l_aus = L(s, "ausg", W_AUSGABE, (xo, 2.3), FM, "left", GRAU)
    aus = [tx(s, "- " + z, (xo, r4(2.02 - 0.26 * i)), TK, "left", GRUEN) for i, z in enumerate(EINKAUF)]
    l_ende = L(s, "ende", w["ende"], (xb, 1.0), FM, "center", ROT)
    # unten: ohne_ende.txt
    sep = lin(s, (-3.3, 0.55), (3.3, 0.55), HELLGRAU, 2, "6,5")
    cmd2 = tx(s, 'while read -r zeile; do echo "- $zeile"; done < ohne_ende.txt', (-3.3, 0.3), TK, "left", DUNKEL)
    d2 = s.datei("ohne_ende.txt", "Milch\nBrot", pos=(-3.3, 0.05), spalten=16, zeilen=2, groesse=TT)
    nl2 = tx(s, "\\n", (r4(d2.x(5) + 0.03), d2.y(0)), TK, "left", ORANGE)
    o2 = schleife(-0.3, 0.8, d2, "ohne_ende.txt")
    kop2 = [d2.teil(i, 0, len(z) - 1, farbe=SCHWARZ) for i, z in enumerate(["Milch", "Brot"])]
    lz2 = d2.markieren(0, 0, 15, ORANGE, 0.3)
    l_kein = L(s, "kein", w["kein"], (d2.links, r4(d2.unten_kante - 0.17)), FM, "left", ROT)
    aus2 = tx(s, "- Milch", (xo, -0.1), TK, "left", GRUEN)
    l_trotz = L(s, "trotz", w["trotz"], (xb, -1.12), FM, "center", ROT)
    # oben
    schritt(s, EIN(cmd, 0.5))
    schritt(s, EIN([d1.id] + nls, 0.6))
    schritt(s, ZEICHNE(o1["rohr"], 0.5), EIN([o1["r_lab"], o1["box"], o1["titel"]] + o1["sb"]["alle"] + [l_aus], 0.6))
    s.pause(0.4)
    for i, z in enumerate(EINKAUF):
        if i == 0:
            schritt(s, EIN([lz, l_lz, kop[0]], 0.4))
        else:
            schritt(s, VER(lz, 0, -dy, 0.4), EIN(kop[i], 0.4))
        teile = [hin(d1, kop[i], z, o1["sb"]), EIN(aus[i], 0.6)]
        teile += [EIN([o1["gelb"]] + o1["s0"], 0.6)] if i == 0 else [AUS(kop[i - 1], 0.4)]
        schritt(s, *teile)
        s.pause(0.2)
    schritt(s, VER(lz, 0, -dy, 0.4))
    schritt(s, AUS([kop[3], o1["gelb"]] + o1["s0"], 0.5), EIN(o1["s1"] + [l_ende], 0.5))
    s.pause(0.7)
    # unten
    schritt(s, EIN([sep, cmd2, d2.id, nl2, l_kein], 0.6))
    schritt(s, ZEICHNE(o2["rohr"], 0.5), EIN([o2["r_lab"], o2["box"], o2["titel"]] + o2["sb"]["alle"], 0.6))
    schritt(s, EIN([lz2, kop2[0]], 0.4))
    schritt(s, hin(d2, kop2[0], "Milch", o2["sb"]), EIN([o2["gelb"]] + o2["s0"] + [aus2], 0.6))
    schritt(s, VER(lz2, 0, -dy, 0.4), EIN(kop2[1], 0.4))
    schritt(s, hin(d2, kop2[1], "Brot", o2["sb"]), AUS([kop2[0]] + o2["s0"], 0.4), EIN(o2["s1"], 0.6))
    schritt(s, EIN(l_trotz, 0.6))
    s.speichern()


LAUF = "2026-11-02,Anna,5.0,28"
W_IFS = {"komma": ("schneidet nur am Komma", "cuts only at commas", "corta solo en las comas", "只在逗号处切开",
                   "coupe seulement aux virgules", "yalnızca virgülde keser"),
         "vor": ("Voreinstellung: IFS = Leerzeichen, Tabulator, Zeilenende", "default: IFS = space, tab, newline",
                 "predeterminado: IFS = espacio, tabulador, fin de línea", "默认：IFS = 空格、制表符、换行符",
                 "par défaut : IFS = espace, tabulation, fin de ligne", "varsayılan: IFS = boşluk, sekme, satır sonu"),
         "kein": ("kein Leerzeichen:\nkein Schnitt", "no space:\nno cut", "sin espacio:\nsin corte", "没有空格：\n不切开",
                  "pas d'espace :\npas de coupe", "boşluk yok:\nkesim yok")}


def k10ifs():
    """Die Zeile 2026-11-02,Anna,5.0,28 auf einem Förderband; ein Schild IFS=, über einer Schere, Schnitte an den drei
    Kommas, die vier Stücke wandern in die Schubladen datum, name, km, minuten (Block s6_ifs mit der Ausgabe
    Anna: 5.0 km). Darunter dieselbe Zeile mit der Voreinstellung von IFS: kein Leerzeichen, kein Schnitt, die ganze
    Zeile landet in datum, die übrigen Schubladen bleiben leer."""
    s = Szene("linux/k10ifs", reihenfolge="anlegen")
    w = W_IFS
    c = tt_breite(20, 1)
    namen = ["datum", "name", "km", "minuten"]

    def schubladen(y, slots, luecke):
        bs = [len(n) * c + sl * c + 0.48 for n, sl in zip(namen, slots)]
        x = -(sum(bs) + luecke * (len(bs) - 1)) / 2
        out = []
        for n, sl, b in zip(namen, slots, bs):
            out.append(schublade(s, r4(x + b / 2), y, n, slot=sl, g=20))
            x += b + luecke
        return out

    def schnitte(g, spalten):
        return [lin(s, (g.xm(k), r4(a)), (g.xm(k), r4(b)), ORANGE, 2.5) for k in spalten
                for a, b in ((g.oben(0) + 0.12, g.oben(0) + 0.02), (g.unten(0) - 0.02, g.unten(0) - 0.1))]

    cmd = tx(s, 'IFS=, read -r datum name km minuten <<< "%s"' % LAUF, (-3.3, 2.6), TK, "left", DUNKEL)
    y1, ys1 = 1.85, 1.0
    sb1 = schubladen(ys1, [10, 4, 3, 2], 0.2)
    ge1 = [gelb(s, sb) for sb in sb1]
    g1 = s.raster(LAUF, (0.0, y1), groesse=20, ausrichtung="mitte")
    bd1 = band(s, -1.15, 1.15, r4(g1.unten(0) - 0.17))
    sch1 = schere(s, -2.2, y1, ORANGE)
    ifs = chip(s, (-2.25, r4(y1 + 0.36)), "IFS=,", ORANGE, ORANGE_HELL, g=TT)
    l_k = L(s, "komma", w["komma"], (-2.35, r4(y1 - 0.33)), FM, "center", ORANGE)
    cut1 = schnitte(g1, g1.trenner(0, ","))
    felder = g1.felder(0, ",")
    kop1 = [g1.teil(0, f.a, f.b, farbe=BLAU) for f in felder]
    ver1 = [VER(k, sb["zx"] - len(f.text) * c / 2 - g1.x(f.a), ys1 - y1, 0.9) for k, f, sb in zip(kop1, felder, sb1)]
    aus = s.raster(['$ echo "$name: $km km"', "Anna: 5.0 km"], (-3.3, 0.45), groesse=TK)
    sep = lin(s, (-3.3, 0.05), (3.3, 0.05), HELLGRAU, 2, "6,5")
    l_vor = L(s, "vor", w["vor"], (-3.3, -0.17), FM, "left", GRAU)
    cmd2 = tx(s, 'read -r datum name km minuten <<< "%s"' % LAUF, (-3.3, -0.45), TK, "left", DUNKEL)
    y2, ys2 = -0.98, -1.75
    sb2 = schubladen(ys2, [22, 4, 3, 2], 0.12)
    ge2 = gelb(s, sb2[0])
    g2 = s.raster(LAUF, (0.0, y2), groesse=20, ausrichtung="mitte")
    bd2 = band(s, -1.15, 1.15, r4(g2.unten(0) - 0.17))
    sch2 = schere(s, -2.2, y2, GRAU)
    l_kein = L(s, "kein", w["kein"], (-2.25, r4(y2 - 0.4)), FM, "center", GRAU)
    kop2 = g2.teil(0, 0, len(LAUF) - 1, farbe=BLAU)
    schritt(s, EIN(cmd, 0.5))
    schritt(s, EIN(g1.ids + bd1, 0.6))
    schritt(s, EIN(sch1 + flach(ifs), 0.6))
    schritt(s, EIN(cut1 + [l_k], 0.6))
    s.pause(0.3)
    schritt(s, EIN(flach([sb["alle"] for sb in sb1]), 0.6))
    schritt(s, EIN(kop1, 0.2))
    schritt(s, *ver1, EIN(ge1, 0.9))
    schritt(s, EIN(aus.ids, 0.6))
    s.pause(0.7)
    schritt(s, EIN([sep, l_vor, cmd2], 0.6))
    schritt(s, EIN(g2.ids + bd2 + sch2 + flach([sb["alle"] for sb in sb2]), 0.6))
    schritt(s, EIN(l_kein, 0.5))
    schritt(s, EIN(kop2, 0.2))
    schritt(s, VER(kop2, sb2[0]["zx"] - len(LAUF) * c / 2 - g2.x(0), ys2 - y2, 0.9), EIN(ge2, 0.9))
    s.speichern()


MINUTEN = [28, 90, 131, 166, 197, 267, 311, 439, 466]
W_PF = {"falsch": ("mit Pipe: die Schleife läuft in einem Kindprozess", "with a pipe: the loop runs in a child process",
                   "con tubería: el bucle se ejecuta en un proceso hijo", "使用管道：循环在子进程中运行",
                   "avec un tube : la boucle tourne dans un processus enfant", "boruyla: döngü bir alt süreçte çalışır"),
        "richtig": ("mit done < laeufe.csv: die Schleife läuft in der Shell selbst",
                    "with done < laeufe.csv: the loop runs in the shell itself",
                    "con done < laeufe.csv: el bucle se ejecuta en la propia shell", "使用 done < laeufe.csv：循环在 shell 自身中运行",
                    "avec done < laeufe.csv : la boucle tourne dans le shell lui-même",
                    "done < laeufe.csv ile: döngü kabuğun kendisinde çalışır"),
        "shell": ("Shell des Skripts", "shell of the script", "shell del script", "脚本的 shell", "shell du script", "betiğin kabuğu"),
        "kopie": ("Kopie", "copy", "copia", "副本", "copie", "kopya"),
        "ende": ("Kindprozesse beendet, Kopie verworfen", "child processes ended, copy discarded",
                 "procesos hijo terminados, copia descartada", "子进程已结束，副本被丢弃", "processus enfants terminés, copie jetée",
                 "alt süreçler bitti, kopya atıldı")}


def k10pipefalle():
    """Pflichtbild. Oben (minuten.sh mit Pipe, Block s6_pipefalle): Kasten „Shell des Skripts“ mit der Schublade summe = 0;
    zwei Kindprozesse wachsen heraus, tail links, die while-Schleife rechts, verbunden durch ein Rohr. Die Schleife hat
    eine Kopie von summe und zählt sie hoch: 28, 90, 131, 166, 197, 267, 311, 439, 466 (die Zwischensummen der Läufe
    wie Kapitel 6). Die Kindprozesse verschwinden samt Kopie; echo liest das Original: Zusammen: 0 Minuten. Unten
    (done < laeufe.csv, Block s6_minuten): die Schleife läuft im Kasten der Shell, summe zeigt am Ende 466."""
    s = Szene("linux/k10pipefalle", reihenfolge="anlegen")
    w = W_PF
    l_f = L(s, "falsch", w["falsch"], (-3.3, 2.7), FM, "left", GRAU)
    sh = pbox(s, (-0.6, 2.2), 4.0, 0.6)
    l_sh = L(s, "shell", w["shell"], (-2.5, 2.2), FM, "left", BLAU)
    sb_o = schublade(s, 0.65, 2.2, "summe", slot=3)
    w_o = wert(s, sb_o, "0")
    p_echo = pfk(s, (1.45, 2.2), (1.7, 2.2), DUNKEL, 2)
    t_echo = tx(s, "echo", (1.75, 2.43), TK, "left", GRAU)
    out_f = tx(s, "Zusammen: 0 Minuten", (1.75, 2.2), TK, "left", ROT)
    p_l = pfk(s, (-2.3, 1.88), (-2.3, 1.33), BLAU, 2.5)
    p_r = pfk(s, (0.75, 1.88), (0.75, 1.38), BLAU, 2.5)
    bx_l = pbox(s, (-2.3, 1.05), 2.0, 0.5)
    t_l = tx(s, "tail -n +2 laeufe.csv", (-2.3, 1.05), TK, "center")
    bx_r = pbox(s, (0.75, 0.95), 3.4, 0.8)
    t_r = tx(s, "while IFS=, read -r _ _ _ minuten", (-0.87, 1.17), TK, "left", BLAU)
    sb_k = schublade(s, 0.2, 0.76, "summe", slot=3)
    w_k = wert(s, sb_k, "0")
    l_kop = L(s, "kopie", w["kopie"], (0.85, 0.76), FM, "left", GRAU)
    rohr = pfk(s, (-1.28, 1.05), (-0.97, 1.05), BLAU, 4)
    strich_ = tx(s, "|", (-1.12, 1.27), TT, "center", BLAU)
    g_l, g_r = geist(s, (-2.3, 1.05), 2.0, 0.5), geist(s, (0.75, 0.95), 3.4, 0.8)
    l_end = L(s, "ende", w["ende"], (-0.4, 0.38), FM, "center", GRAU)
    # unten
    sep = lin(s, (-3.3, 0.12), (3.3, 0.12), HELLGRAU, 2, "6,5")
    l_r = L(s, "richtig", w["richtig"], (-3.3, -0.1), FM, "left", GRAU)
    datei_ = chip(s, (-2.75, -0.85), "laeufe.csv", GRAU, WEISS)
    rohr2 = pfk(s, (-2.22, -0.85), (-1.62, -0.85), BLAU, 4.5)
    lt2 = tx(s, "<", (-1.92, -0.66), TT, "center", BLAU)
    sh2 = pbox(s, (-0.1, -0.85), 3.0, 1.1)
    l_sh2 = L(s, "shell", w["shell"], (-1.5, -0.47), FM, "left", BLAU)
    t_lp = tx(s, "while IFS=, read -r datum _ _ minuten", (-1.5, -0.74), TK, "left", BLAU)
    sb2 = schublade(s, -0.8, -1.1, "summe", slot=3)
    w2 = wert(s, sb2, "0")
    p_echo2 = pfk(s, (1.45, -1.1), (1.7, -1.1), DUNKEL, 2)
    t_echo2 = tx(s, "echo", (1.75, -0.87), TK, "left", GRAU)
    out_r = tx(s, "Zusammen: 466 Minuten", (1.75, -1.1), TK, "left", GRUEN)
    schritt(s, EIN([l_f, sh, l_sh] + sb_o["alle"] + w_o, 0.7))
    s.pause(0.4)
    schritt(s, ZEICHNE([p_l, p_r], 0.5), WACHS([bx_l, bx_r], 0.6), EIN([t_l, t_r], 0.6))
    schritt(s, ZEICHNE(rohr, 0.4), EIN(strich_, 0.4))
    schritt(s, EIN(sb_k["alle"] + w_k + [l_kop], 0.6))
    for v in MINUTEN:
        s.ersetzen(w_k[1], str(v), dauer=0.3)
    s.pause(0.5)
    schritt(s, AUS([p_l, p_r, bx_l, bx_r, t_l, t_r, rohr, strich_, l_kop] + sb_k["alle"] + w_k, 0.7), EIN([g_l, g_r, l_end], 0.7))
    schritt(s, BETONE(w_o[1], 0.7))
    schritt(s, ZEICHNE(p_echo, 0.4), EIN([t_echo, out_f], 0.5))
    s.pause(0.8)
    schritt(s, EIN([sep, l_r] + datei_ + [rohr2, lt2, sh2, l_sh2, t_lp] + sb2["alle"] + w2, 0.7))
    for v in MINUTEN:
        s.ersetzen(w2[1], str(v), dauer=0.22)
    schritt(s, ZEICHNE(p_echo2, 0.4), EIN([t_echo2, out_r], 0.5))
    s.speichern()


W_AR = {"vier": ("4 Elemente: 4 Wörter, 4 Durchgänge", "4 elements: 4 words, 4 iterations", "4 elementos: 4 palabras, 4 iteraciones",
                 "4 个元素：4 个词，4 次循环", "4 éléments : 4 mots, 4 itérations", "4 öğe: 4 sözcük, 4 tur")}


def k10array():
    """Ein Regal fotos mit den Fächern 0, 1, 2 (strand 1.jpg, strand 2.jpg, berg.png; Block s6_array). Ein Zeiger
    ${fotos[0]} auf Fach 0, ein Zähler ${#fotos[@]} = 3. Bei fotos+=(neu.jpg) kommt Fach 3 dazu, der Zähler springt auf
    4. Zum Schluss fließen alle Fächer über "${fotos[@]}" als vier getrennte Kärtchen in eine Schleife."""
    s = Szene("linux/k10array", reihenfolge="anlegen")
    w = W_AR
    inhalt = ["strand 1.jpg", "strand 2.jpg", "berg.png", "neu.jpg"]
    cmd1 = tx(s, 'fotos=("strand 1.jpg" "strand 2.jpg" berg.png)', (-3.3, 2.6), TK, "left", DUNKEL)
    cmd2 = tx(s, "fotos+=(neu.jpg)", (-3.3, 2.3), TK, "left", DUNKEL)
    yr = 1.6
    l_reg = tx(s, "fotos", (-3.3, yr), TT, "left", BLAU)
    xs = [r4(-1.9 + 1.36 * i) for i in range(4)]
    faecher_ = [box(s, (x, yr), 1.3, 0.42, GRAU, GRAU_HELL, 2, "rect") for x in xs]
    nummern = [tx(s, str(i), (x, r4(yr - 0.37)), TK, "center", GRAU) for i, x in enumerate(xs)]
    karten = [chip(s, (x, yr), t, GRAU, GELB) for x, t in zip(xs, inhalt)]
    zeiger = tx(s, "${fotos[0]}", (xs[0], 0.72), TT, "center", ORANGE)
    p_z = pfk(s, (xs[0], 0.86), (xs[0], r4(yr - 0.5)), ORANGE, 2.5)
    zaehler = tx(s, "${#fotos[@]} = 3", (1.5, 0.72), TT, "center", ORANGE)
    loop = tx(s, 'for f in "${fotos[@]}"; do', (-3.3, 0.15), TK, "left", DUNKEL)
    ms, _ = reihe(inhalt, mitte=0.0, luecke=0.25)
    yk = -0.35
    kopien = [chip(s, (x, yr), t, BLAU, BLAU_HELL) for x, t in zip(xs, inhalt)]
    l_vier = L(s, "vier", w["vier"], (0.0, -0.75), FM, "center", BLAU)
    schritt(s, EIN(cmd1, 0.5))
    schritt(s, EIN([l_reg] + faecher_[:3] + nummern[:3], 0.6))
    schritt(s, EIN(flach(karten[:3]), 0.6))
    s.pause(0.4)
    schritt(s, EIN(zeiger, 0.5), ZEICHNE(p_z, 0.5))
    schritt(s, BETONE(karten[0][1], 0.7))
    schritt(s, EIN(zaehler, 0.5))
    s.pause(0.5)
    schritt(s, EIN(cmd2, 0.5))
    schritt(s, WACHS(faecher_[3], 0.6), EIN([nummern[3]] + karten[3], 0.6))
    s.ersetzen(zaehler, "${#fotos[@]} = 4", dauer=0.6)
    s.pause(0.5)
    schritt(s, EIN(loop, 0.5))
    schritt(s, EIN(flach(kopien), 0.2))
    schritt(s, *[v for k, x in zip(kopien, ms) for v in VERS(k, x - xs[kopien.index(k)], yk - yr, 0.9)])
    schritt(s, EIN(l_vier, 0.5))
    s.speichern()


# ================================================================== Abschnitt 7: Funktionen
W_FU = {"bekannt": ("bekannte Funktionen", "known functions", "funciones conocidas", "已知的函数", "fonctions connues",
                    "bilinen fonksiyonlar"),
        "ablegen": ("nur ablegen, nichts ausführen", "only store it, run nothing", "solo guardar, no ejecutar nada",
                    "只存放，不执行", "seulement ranger, rien exécuter", "yalnızca sakla, hiçbir şey çalıştırma")}


def k10funktion():
    """Oben links das Skript als helle Dateiansicht (Titel gruesse.sh, nur für die Szene): die Definition
    gruesse() { echo "Hallo, $USER!"; } und zwei Zeilen gruesse (Befehle wie Block s7_funktion). Beim Lesen der
    Definition legt die Shell eine Karteikarte gruesse im Kasten „bekannte Funktionen“ ab, ohne etwas auszuführen. Bei
    jeder Zeile gruesse führt ein Pfeil zur Karte, ihr Inhalt läuft ab, die Ausgabe Hallo, student! erscheint, ein
    gestrichelter Pfeil kehrt zur nächsten Zeile zurück."""
    s = Szene("linux/k10funktion", reihenfolge="anlegen")
    w = W_FU
    zeilen = ['gruesse() { echo "Hallo, $USER!"; }', "gruesse", "gruesse"]
    d = s.datei("gruesse.sh", "\n".join(zeilen), pos=(-3.3, 2.55), spalten=36, groesse=TT)
    dy = d.zelle[1]
    lab = L(s, "liest", W_SK["liest"], (d.links, r4(d.oben_kante + 0.2)), FM, "left", ORANGE)
    lz = d.markieren(0, 0, 35, ORANGE, 0.3)
    kb = box(s, (1.85, 1.4), 2.9, 0.95, GRAU, WEISS, 2, "rect")
    l_kb = L(s, "bekannt", w["bekannt"], (0.5, 1.7), FM, "left", GRAU)
    karte_ = [box(s, (1.85, 1.25), 2.6, 0.5, GRAU, GELB, 2), tx(s, "gruesse", (0.68, 1.38), TT, "left", DUNKEL)]
    k_inh = tx(s, 'echo "Hallo, $USER!"', (0.68, 1.13), TK, "left")
    p_def = pfk(s, (r4(d.xr(34) + 0.05), d.y(0)), (0.53, 1.42), GRAU, 2, "5,4")
    l_ab = L(s, "ablegen", w["ablegen"], (0.15, 2.22), FM, "left", GRAU)
    x_ende = r4(d.xr(6) + 0.06)
    p_auf = [pfk(s, (x_ende, d.y(1)), (0.53, 1.27), ORANGE, 2.5), pfk(s, (x_ende, d.y(2)), (0.53, 1.13), ORANGE, 2.5)]
    p_zur = [pfk(s, (0.53, 1.06), (x_ende, d.y(2)), ORANGE, 2, "5,4"),
             pfk(s, (0.53, 1.03), (x_ende, r4(d.y(2) - dy)), ORANGE, 2, "5,4")]
    l_aus = L(s, "ausg", W_AUSG, (-3.3, 1.35), FM, "left", GRAU)
    aus = [tx(s, "Hallo, student!", (-3.3, r4(1.1 - 0.24 * i)), TK, "left", GRUEN) for i in range(2)]
    schritt(s, EIN([d.id, lab, kb, l_kb], 0.7))
    s.pause(0.3)
    schritt(s, EIN(lz, 0.4))
    schritt(s, ZEICHNE(p_def, 0.5), EIN(karte_ + [k_inh, l_ab], 0.6))
    s.pause(0.5)
    schritt(s, EIN(l_aus, 0.4))
    for k in (0, 1):
        schritt(s, VER(lz, 0, -dy, 0.4))
        schritt(s, ZEICHNE(p_auf[k], 0.5))
        schritt(s, BETONE(k_inh, 0.6), EIN(aus[k], 0.6))
        schritt(s, ZEICHNE(p_zur[k], 0.5))
        schritt(s, AUS(p_zur[k], 0.3))
        s.pause(0.2)
    s.speichern()


W_FP = {"skript": ("Skript", "script", "script", "脚本", "script", "betik"),
        "waehrend": ("während des Aufrufs", "during the call", "durante la llamada", "调用期间", "pendant l'appel", "çağrı sırasında"),
        "beide": ("gilt für beide", "same for both", "igual para ambos", "两者相同", "le même pour les deux", "ikisi için aynı")}


def k10funktionsparameter():
    """Die Fächer $0 … $3 des Skripts (./gruss.sh, Milch, Brot, leer) und der Zähler $# = 2. Für gruss Anna Ben Clara
    schiebt sich ein zweiter Satz Fächer 1–3 mit Anna, Ben, Clara und $# = 3 davor und verdeckt die Fächer des Skripts;
    Fach 0 bleibt dasselbe. Danach schiebt sich der Satz zurück nach oben, die Fächer des Skripts sind wieder sichtbar.
    Unten die drei Ausgabezeilen (Block s7_argumente)."""
    s = Szene("linux/k10funktionsparameter", reihenfolge="anlegen")
    w = W_FP
    cmd = tx(s, "$ ./gruss.sh Milch Brot", (-3.3, 2.75), TK, "left", GRAU)
    ys, yp = 1.3, 2.08
    k, n, m = faecher(s, -2.45, ys, [1.15, 0.75, 0.75, 0.75], luecke=0.06)
    l_sk = L(s, "skript", w["skript"], (-3.3, ys), FM, "left", GRAU)
    c0 = chip(s, (m[0], ys), "./gruss.sh", DUNKEL, WEISS)
    cs = [chip(s, (m[i], ys), t, BLAU, BLAU_HELL) for i, t in ((1, "Milch"), (2, "Brot"))]
    z2 = chip(s, (1.85, ys), "$# = 2", GRAU, WEISS, g=TT)
    xa, xe = m[1] - 0.43, m[3] + 0.43
    panel = box(s, ((xa + xe) / 2, yp), xe - xa, 0.5, BLAU, WEISS, 2.5, "rect")
    ff = [box(s, (m[i], yp), 0.75, 0.36, GRAU, GRAU_HELL, 2, "rect") for i in (1, 2, 3)]
    fc = [chip(s, (m[i], yp), t, BLAU, BLAU_HELL) for i, t in ((1, "Anna"), (2, "Ben"), (3, "Clara"))]
    z3 = chip(s, (1.85, yp), "$# = 3", BLAU, BLAU_HELL, g=TT)
    satz = [panel] + ff + flach(fc) + flach(z3)
    l_fn = tx(s, "gruss Anna Ben Clara", (r4(xa), r4(yp + 0.42)), TK, "left", BLAU)
    l_w = L(s, "waehrend", w["waehrend"], (r4(xa + ttb("gruss Anna Ben Clara") + 0.15), r4(yp + 0.42)), FM, "left", BLAU)
    l_b = L(s, "beide", w["beide"], (m[0], r4(ys + 0.36)), FM, "center", ORANGE)
    aus = s.raster(["Im Skript: 2 Argumente, das erste ist Milch",
                    "In der Funktion: 3 Argumente, das erste ist Anna, $0 ist ./gruss.sh",
                    "Wieder im Skript: das erste ist Milch"], (-3.3, 0.45), groesse=TK)
    schritt(s, EIN([cmd, l_sk] + k + n + flach(c0) + flach(cs) + flach(z2), 0.7))
    schritt(s, EIN(aus.ids[0], 0.5))
    s.pause(0.5)
    schritt(s, EIN([l_fn, l_w] + satz, 0.6))
    schritt(s, *VERS(satz, 0, ys - yp, 0.8))
    schritt(s, BETONE(c0[1], 0.6), EIN(l_b, 0.6))
    schritt(s, EIN(aus.ids[1], 0.5))
    s.pause(0.6)
    schritt(s, *VERS(satz, 0, yp - ys, 0.8))
    schritt(s, EIN(aus.ids[2], 0.5))
    s.speichern()


W_LO = {"skript": ("Variable des Skripts", "variable of the script", "variable del script", "脚本的变量", "variable du script",
                   "betiğin değişkeni"),
        "lokal": ("lokal", "local", "local", "局部", "locale", "yerel"),
        "weg": ("nach dem Aufruf weg", "gone after the call", "eliminada tras la llamada", "调用后消失", "disparue après l'appel",
                "çağrıdan sonra yok"),
        "direkt": ("schreibt direkt\nhinein", "writes straight\ninto it", "escribe directamente\nen ella", "直接\n写入",
                   "écrit directement\ndedans", "doğrudan\niçine yazar")}


def k10local():
    """Zwei Spalten mit der Schublade anzahl = 10 des Skripts (lokal.sh, Block s7_local). Links mit_local: Eine eigene
    Schublade anzahl schiebt sich davor, die Funktion schreibt 2 hinein; nach dem Aufruf ist sie weg, dahinter steht
    unverändert 10. Rechts ohne_local: keine eigene Schublade, die Funktion schreibt 1 direkt in die Schublade des
    Skripts; danach bleibt 1. Unter jeder Spalte die beiden Ausgabezeilen."""
    s = Szene("linux/k10local", reihenfolge="anlegen")
    w = W_LO
    trenn = lin(s, (0, 2.8), (0, -0.4), HELLGRAU, 2, "6,5")
    xl, xr = -1.75, 1.75
    yk, yp, yv = 2.2, 1.6, 0.95
    h_l = tx(s, "mit_local", (xl, 2.6), TT, "center", DUNKEL)
    c_l = chip(s, (xl, yk), "local anzahl=2", ORANGE, ORANGE_HELL)
    sv_l = schublade(s, xl, yv, "anzahl", slot=3)
    w_l = wert(s, sv_l, "10")
    l_sl = L(s, "skript", w["skript"], (xl, r4(yv - 0.36)), FM, "center", GRAU)
    g_loc = geist(s, (xl, yp), 2.0, 0.46)
    l_weg = L(s, "weg", w["weg"], (xl, yp), FM, "center", GRAU)
    sloc = schublade(s, xl, yp, "anzahl", slot=3)
    l_lok = L(s, "lokal", w["lokal"], (r4(xl - sv_l["b"] / 2 - 0.1), yp), FM, "right", ORANGE)
    w_loc = wert(s, {"zx": sloc["zx"], "y": yv, "bw": sloc["bw"]}, "2", farbe=ORANGE)
    aus_l = s.raster(["In mit_local: anzahl=2", "Danach: anzahl=10"], (-3.3, 0.05), groesse=TK)
    h_r = tx(s, "ohne_local", (xr, 2.6), TT, "center", DUNKEL)
    c_r = chip(s, (xr, yk), "anzahl=1", ORANGE, ORANGE_HELL)
    sv_r = schublade(s, xr, yv, "anzahl", slot=3)
    w_r = wert(s, sv_r, "10")
    l_sr = L(s, "skript", w["skript"], (xr, r4(yv - 0.36)), FM, "center", GRAU)
    p_r = pfk(s, (sv_r["zx"], r4(yk - 0.16)), (sv_r["zx"], r4(yv + 0.17)), ORANGE, 2.5)
    l_dir = L(s, "direkt", w["direkt"], (r4(sv_r["zx"] - 0.12), yp), FM, "right", ORANGE)
    aus_r = s.raster(["In ohne_local: anzahl=1", "Danach: anzahl=1"], (0.2, 0.05), groesse=TK)
    lokal = sloc["alle"] + [l_lok]
    schritt(s, EIN([trenn, h_l, c_l] + sv_l["alle"] + w_l + [l_sl], 0.7))
    s.pause(0.4)
    schritt(s, EIN(lokal, 0.6))
    schritt(s, *VERS(lokal, 0, yv - yp, 0.8))
    schritt(s, EIN(w_loc, 0.5), EIN(aus_l.ids[0], 0.5))
    s.pause(0.4)
    schritt(s, *VERS(lokal, 0, yp - yv, 0.7), AUS(w_loc, 0.5))
    schritt(s, AUS(lokal, 0.5), EIN([g_loc, l_weg], 0.5))
    schritt(s, BETONE(w_l[1], 0.6), EIN(aus_l.ids[1], 0.6))
    s.pause(0.7)
    schritt(s, EIN([h_r, c_r] + sv_r["alle"] + w_r + [l_sr], 0.7))
    schritt(s, ZEICHNE(p_r, 0.5), EIN(l_dir, 0.5))
    with s.gleichzeitig():
        s.ersetzen(w_r[1], "1", farbe=ORANGE, dauer=0.6)
        schritt(s, EIN(aus_r.ids[0], 0.6))
    schritt(s, EIN(aus_r.ids[1], 0.5))
    s.speichern()


W_RG = {"fn": ("Funktion", "function", "función", "函数", "fonction", "fonksiyon"),
        "stdout": ("Standardausgabe", "standard output", "salida estándar", "标准输出", "sortie standard", "standart çıktı"),
        "h1": ("Status: nur 0 bis 255, für Ja und Nein", "status: only 0 to 255, for yes and no",
               "estado: solo de 0 a 255, para sí y no", "状态：只有 0 到 255，用于是与否", "code : seulement 0 à 255, pour oui et non",
               "durum: yalnızca 0 ile 255 arası, evet ve hayır için"),
        "h2": ("Ausgabe: beliebiger Text", "output: any text", "salida: cualquier texto", "输出：任意文本",
               "sortie : n'importe quel texte", "çıktı: herhangi bir metin")}


def k10rueckgabe():
    """Eine Funktion als Kasten mit zwei Ausgängen. Oben „Exit-Status“: ist_zahl 42 schiebt das Schild 0 hinaus in die
    Weiche eines if, der Weg then leuchtet (Block s7_return). Unten „Standardausgabe“: euro 373 schiebt den Text
    3,73 Euro auf ein Band, die Befehlsersetzung $( ) fängt ihn und legt ihn in die Schublade preis (Ausgabe wie Block
    s7_ausgabe). Darunter der Hinweis Status gegen Ausgabe."""
    s = Szene("linux/k10rueckgabe", reihenfolge="anlegen")
    w = W_RG
    yo, yu = 1.75, 0.85
    fb = pbox(s, (-2.45, 1.4), 1.8, 1.7)
    l_fb = L(s, "fn", w["fn"], (-2.45, 2.07), FM, "center", BLAU)
    t_o = tx(s, "ist_zahl 42", (-2.45, yo), TK, "center")
    t_u = tx(s, "euro 373", (-2.45, yu), TK, "center")
    l_ex = L(s, "exit", W_EXIT, (-1.4, r4(yo + 0.22)), FM, "left", GRAU)
    l_so = L(s, "stdout", w["stdout"], (-1.4, r4(yu + 0.25)), FM, "left", GRAU)
    xw = 0.75
    gleis = [lin(s, (-1.55, yo), (xw, yo), GRAU, 3), lin(s, (xw, yo), (1.4, r4(yo + 0.35)), GRAU, 3),
             lin(s, (xw, yo), (1.4, r4(yo - 0.35)), GRAU, 3), s.punkt(None, xw, yo, DUNKEL, 0.06)]
    t_if = tx(s, "if", (xw, r4(yo + 0.25)), TT, "center", DUNKEL)
    t_then = tx(s, "then", (1.5, r4(yo + 0.35)), TK, "left", DUNKEL)
    t_fi = tx(s, "fi", (1.5, r4(yo - 0.35)), TK, "left", DUNKEL)
    weg = lin(s, (xw, yo), (1.4, r4(yo + 0.35)), ORANGE, 5)
    sch = schild(s, -1.3, yo, 0)
    bd = band(s, -1.38, 0.1, r4(yu - 0.15))
    fang = chip(s, (0.65, yu), "$( )", ORANGE, ORANGE_HELL, g=TT)
    xsb = 2.35
    sb = schublade(s, xsb, yu, "preis", slot=9)
    ge = gelb(s, sb)
    p_sb = pfk(s, (r4(0.65 + chipb("$( )", TT) / 2 + 0.04), yu), (r4(xsb - sb["b"] / 2 - 0.04), yu), DUNKEL, 2)
    code = tx(s, "preis=$(euro 373)", (0.65, r4(yu - 0.42)), TK, "center", DUNKEL)
    breite = ttb("3,73 Euro")
    text_ = tx(s, "3,73 Euro", (-1.45, yu), TK, "left", GRUEN)
    x1 = 0.65 - chipb("$( )", TT) / 2 - breite - 0.05        # linke Kante vor dem Fänger
    h1 = L(s, "h1", w["h1"], (-3.3, -0.05), FM, "left", DUNKEL)
    h2 = L(s, "h2", w["h2"], (-3.3, -0.32), FM, "left", DUNKEL)
    schritt(s, EIN([fb, l_fb, t_o, t_u, l_ex, l_so], 0.7))
    s.pause(0.4)
    schritt(s, EIN(gleis + [t_if, t_then, t_fi], 0.6))
    schritt(s, EIN(sch, 0.4))
    schritt(s, *VERS(sch, xw - 0.3 + 1.3, 0, 0.8))
    schritt(s, ZEICHNE(weg, 0.6))
    s.pause(0.5)
    schritt(s, EIN(bd + flach(fang) + sb["alle"] + [p_sb, code], 0.6))
    schritt(s, EIN(text_, 0.4))
    schritt(s, VER(text_, x1 + 1.45, 0, 0.8))
    schritt(s, VER(text_, sb["zx"] - breite / 2 - x1, 0, 0.8), EIN(ge, 0.8))
    s.pause(0.4)
    schritt(s, EIN([h1, h2], 0.6))
    s.speichern()


W_FS = {"selbst": ("führt die Funktion selbst aus", "runs the function itself", "ejecuta la función por sí misma",
                   "自己执行这个函数", "exécute la fonction lui-même", "fonksiyonu kendisi çalıştırır")}


def k10funktionskript():
    """Zwei Spalten wie k10eigeneshell. Links mcd fotos/2026: Die Shell führt die Funktion selbst aus, ihr Verzeichnis
    springt auf ~/linuxk10/fotos/2026 und bleibt (Block s7_mcd). Rechts bash mcd.sh fotos/2027: Ein Kindprozess als
    Kopie wechselt nach ~/linuxk10/fotos/2027 und endet; die Shell bleibt in ~/linuxk10 (Block s7_mcdskript)."""
    s = Szene("linux/k10funktionskript", reihenfolge="anlegen")
    w = W_ES
    trenn = lin(s, (0, 2.8), (0, -0.95), HELLGRAU, 2, "6,5")

    def kasten(cx, y, key, wl):
        k = pbox(s, (cx, y), 3.1, 0.8)
        lab = L(s, key, wl, (cx - 1.45, y + 0.19), FM, "left", BLAU)
        lv = L(s, "verz", w["verz"], (cx - 1.45, y - 0.15), FM, "left", GRAU)
        v = tx(s, PFAD, (cx - 0.55, y - 0.15), TK, "left")
        return {"teile": [k, lab, lv, v], "v": v, "k": k}

    xl, xr = -1.75, 1.75
    h_l = tx(s, "mcd fotos/2026", (xl, 2.62), TT, "center", DUNKEL)
    h_r = tx(s, "bash mcd.sh fotos/2027", (xr, 2.62), TT, "center", DUNKEL)
    sl = kasten(xl, 1.85, "shell", W_SHELL)
    l_selbst = L(s, "selbst", W_FS["selbst"], (xl, 1.22), FM, "center", GRAU)
    l_bleibt = L(s, "bleibt", w["bleibt"], (xl + 1.5, 0.97), FM, "right", ORANGE)
    out_l = s.raster(["$ pwd", "/home/student/linuxk10/fotos/2026"], (-3.3, 0.55), groesse=TK)
    sr = kasten(xr, 1.85, "shell", W_SHELL)
    pf_k = pfk(s, (xr, 1.43), (xr, 0.8), BLAU, 2.5)
    kd = kasten(xr, 0.35, "kind", w["kind"])
    g_k = geist(s, (xr, 0.35), 3.1, 0.8)
    l_end = L(s, "beendet", w["beendet"], (xr, 0.35), FM, "center", GRAU)
    l_unv = L(s, "unv", w["unv"], (xr + 1.5, 1.18), FM, "right", GRUEN)
    out_r = s.raster(["Im Skript: /home/student/linuxk10/fotos/2027", "$ pwd", "/home/student/linuxk10"], (0.1, -0.35),
                     groesse=TK)
    schritt(s, EIN([trenn, h_l] + sl["teile"], 0.7))
    s.pause(0.3)
    schritt(s, EIN(l_selbst, 0.5))
    s.ersetzen(sl["v"], "~/linuxk10/fotos/2026", farbe=ORANGE, dauer=0.6)
    schritt(s, EIN(out_l.ids + [l_bleibt], 0.6))
    s.pause(0.7)
    schritt(s, EIN([h_r] + sr["teile"], 0.7))
    schritt(s, ZEICHNE(pf_k, 0.5), WACHS(kd["k"], 0.6), EIN(kd["teile"][1:], 0.6))
    s.pause(0.3)
    with s.gleichzeitig():
        s.ersetzen(kd["v"], "~/linuxk10/fotos/2027", farbe=ORANGE, dauer=0.6)
        schritt(s, EIN(out_r.ids[0], 0.6))
    s.pause(0.4)
    schritt(s, AUS(kd["teile"] + [pf_k], 0.7), EIN([g_k, l_end], 0.7))
    schritt(s, EIN(out_r.ids[1:], 0.6))
    schritt(s, BETONE(sr["v"], 0.7), EIN(l_unv, 0.6))
    s.speichern()


# ================================================================== Abschnitt 8: Fehler erkennen und melden
W_EX = {"args": ("Argumente da?", "arguments given?", "¿hay argumentos?", "有参数吗？", "des arguments ?", "argüman var mı?"),
        "lesbar": ("lesbare Datei?", "readable file?", "¿archivo legible?", "是可读文件吗？", "fichier lisible ?", "okunabilir dosya mı?"),
        "stderr": ("auf die Fehlerausgabe:", "to standard error:", "a la salida de errores:", "写到标准错误：",
                   "vers la sortie d'erreur :", "standart hataya:"),
        "weiter": ("nächste Datei", "next file", "siguiente archivo", "下一个文件", "fichier suivant", "sonraki dosya"),
        "alles": ("alles gezählt", "everything counted", "todo contado", "全部已计数", "tout compté", "hepsi sayıldı"),
        "fehlte": ("mindestens eine fehlte", "at least one was missing", "faltó al menos uno", "至少缺了一个", "au moins un manquait",
                   "en az biri eksikti")}


def frage(s, mitte, key, wl, b=1.9):
    """Entscheidung im Flussbild: orange umrandeter Kasten mit einer Frage (Ergebnis [Kasten, Text])."""
    return [box(s, mitte, b, 0.4, ORANGE, ORANGE_HELL, 2.5), L(s, key, wl, mitte, FM, "center", DUNKEL)]


def k10exit():
    """Flussbild der fertigen zaehle.sh (skripte/zaehle.sh, Block s8_zaehle). „Argumente da?“ nein: Aufruf: zaehle.sh
    DATEI... auf der Fehlerausgabe, exit 2. Ja: status=0, Schleife for datei in "$@" (Rahmen); darin „lesbare Datei?“
    ja: echo "$datei: $zeilen Zeilen", nein: status=1 und continue, beide Wege zur nächsten Datei. Nach der Schleife
    exit "$status" mit den Schildern 0 „alles gezählt“ und 1 „mindestens eine fehlte“."""
    s = Szene("linux/k10exit", reihenfolge="anlegen")
    w = W_EX
    xm = -1.95
    d1 = frage(s, (xm, 2.6), "args", w["args"])
    p_n1 = pfk(s, (xm + 0.95, 2.6), (-0.3, 2.6), DUNKEL, 2.5)
    l_n1 = L(s, "nein", W_NEIN, (-0.65, 2.75), FM, "center", GRAU)
    l_err = L(s, "stderr", w["stderr"], (-0.25, 2.85), FM, "left", GRAU)
    msg = tx(s, "Aufruf: zaehle.sh DATEI...", (-0.25, 2.6), TK, "left", ROT)
    p_e2 = pfk(s, (r4(-0.25 + ttb("Aufruf: zaehle.sh DATEI...") + 0.05), 2.6), (2.2, 2.6), DUNKEL, 2.5)
    ex2 = chip(s, (2.6, 2.6), "exit 2", ROT, ROT_HELL, g=TT)
    p_j1 = pfk(s, (xm, 2.4), (xm, 2.18), DUNKEL, 2.5)
    l_j1 = L(s, "ja", W_JA, (xm + 0.12, 2.29), FM, "left", GRAU)
    st0 = chip(s, (xm, 2.02), "status=0", GRAU, WEISS, g=TT)
    p_in = pfk(s, (xm, 1.86), (xm, 1.74), DUNKEL, 2.5)
    rahmen_ = box(s, (-0.45, 0.83), 5.7, 1.78, GRAU, WEISS, 2, "rect")
    kopf = tx(s, 'for datei in "$@"', (-3.2, 1.42), TT, "left", DUNKEL)
    d2 = frage(s, (xm, 0.95), "lesbar", w["lesbar"])
    p_n2 = pfk(s, (xm + 0.95, 0.95), (-0.52, 0.95), DUNKEL, 2.5)
    l_n2 = L(s, "nein", W_NEIN, (-0.75, 1.1), FM, "center", GRAU)
    st1 = chip(s, (-0.05, 0.95), "status=1", ORANGE, ORANGE_HELL, g=TT)
    p_c = pfk(s, (0.43, 0.95), (0.88, 0.95), DUNKEL, 2.5)
    cont = chip(s, (1.35, 0.95), "continue", ORANGE, ORANGE_HELL, g=TT)
    p_j2 = pfk(s, (xm, 0.75), (xm, 0.5), DUNKEL, 2.5)
    l_j2 = L(s, "ja", W_JA, (xm + 0.12, 0.62), FM, "left", GRAU)
    ech = chip(s, (xm, 0.35), 'echo "$datei: $zeilen Zeilen"', DUNKEL, WEISS)
    xz = 2.15
    l_ech = lin(s, (r4(xm + chipb('echo "$datei: $zeilen Zeilen"') / 2), 0.35), (xz, 0.35), DUNKEL, 2.5)
    l_ct = lin(s, (r4(1.35 + chipb("continue", TT) / 2), 0.95), (xz, 0.95), ORANGE, 2.5)
    p_zur = pfk(s, (xz, 0.35), (r4(-3.2 + ttb('for datei in "$@"', TT) + 0.08), 1.42), DUNKEL, 2.5, knick="vh")
    l_w = L(s, "weiter", w["weiter"], (0.3, 1.53), FM, "center", GRAU)
    p_aus = pfk(s, (xm, -0.06), (xm, -0.29), DUNKEL, 2.5)
    exs = chip(s, (xm, -0.45), 'exit "$status"', DUNKEL, WEISS, g=TT)
    xs0 = r4(xm + chipb('exit "$status"', TT) / 2)
    ast = [lin(s, (xs0, -0.45), (-0.5, -0.28), GRAU, 2), lin(s, (xs0, -0.45), (-0.5, -0.66), GRAU, 2)]
    s0 = schild(s, -0.3, -0.28, 0) + [L(s, "alles", w["alles"], (-0.05, -0.28), FM, "left", GRUEN)]
    s1 = schild(s, -0.3, -0.66, 1) + [L(s, "fehlte", w["fehlte"], (-0.05, -0.66), FM, "left", ROT)]
    schritt(s, EIN(d1, 0.6))
    schritt(s, ZEICHNE(p_n1, 0.5), EIN(l_n1, 0.5))
    schritt(s, EIN([l_err, msg], 0.6))
    schritt(s, ZEICHNE(p_e2, 0.4), EIN(ex2, 0.5))
    s.pause(0.5)
    schritt(s, ZEICHNE(p_j1, 0.4), EIN([l_j1] + st0, 0.5))
    schritt(s, ZEICHNE(p_in, 0.3), EIN([rahmen_, kopf], 0.6))
    schritt(s, EIN(d2, 0.5))
    schritt(s, ZEICHNE(p_j2, 0.4), EIN([l_j2] + ech, 0.5))
    schritt(s, ZEICHNE([l_ech, p_zur], 0.8), EIN(l_w, 0.6))
    s.pause(0.4)
    schritt(s, ZEICHNE(p_n2, 0.4), EIN([l_n2] + st1, 0.5))
    schritt(s, ZEICHNE(p_c, 0.3), EIN(cont, 0.5))
    schritt(s, ZEICHNE(l_ct, 0.5))
    s.pause(0.5)
    schritt(s, ZEICHNE(p_aus, 0.3), EIN(exs, 0.5))
    schritt(s, ZEICHNE(ast, 0.4), EIN(s0 + s1, 0.6))
    s.speichern()


W_CD = {"ohne": ("ohne Prüfung", "without a check", "sin comprobación", "不检查", "sans vérification", "denetim olmadan"),
        "mit": ("mit Prüfung", "with a check", "con comprobación", "带检查", "avec vérification", "denetimle"),
        "trotzdem": ("läuft trotzdem\nweiter", "carries on\nanyway", "sigue de\ntodos modos", "仍然\n继续", "continue\nquand même",
                     "yine de\ndevam eder"),
        "geloescht": ("gelöscht", "deleted", "borrado", "已删除", "supprimé", "silindi"),
        "bleibt": ("bleibt", "stays", "se queda", "保留", "reste", "kalır"),
        "grau": ("nicht erreicht", "not reached", "no se alcanza", "未执行", "non atteint", "ulaşılmaz")}


def k10cdfalle():
    """Zwei Läufe von ./loesche.sh gibtsnicht. Links ohne Prüfung (skripte/loesche_falsch.sh, Block s8_cdfalle): cd prallt
    am nicht vorhandenen Verzeichnis ab (rotes Kreuz), der Ablauf geht trotzdem weiter zu rm -f -- *.tmp, das im
    Arbeitsordner ~/linuxk10 zuschlägt: wichtig.tmp verschwindet. Rechts mit Prüfung (skripte/loesche.sh, Block
    s8_cdrichtig): if ! cd "$1" biegt sofort zu exit 1 ab, rm bleibt grau, wichtig.tmp bleibt."""
    s = Szene("linux/k10cdfalle", reihenfolge="anlegen")
    w = W_CD
    yc, ye, yr, yo = 2.2, 1.6, 1.05, 0.3
    kopf = tx(s, "./loesche.sh gibtsnicht", (0.0, 2.95), TT, "center", DUNKEL)
    trenn = lin(s, (0, 2.75), (0, -0.15), HELLGRAU, 2, "6,5")

    def ziel_weg(x):
        return [box(s, (x, yc), 1.1, 0.34, HELLGRAU, WEISS, 2, "rect", "5,4"), tx(s, "gibtsnicht", (x, yc), TK, "center", GRAU)]

    def ordner(x):
        return [box(s, (x, yo), 3.0, 0.7, BLAU, WEISS, 2, "rect"), tx(s, "~/linuxk10", (r4(x - 1.4), r4(yo + 0.2)), TK, "left", BLAU)]

    h_l = L(s, "ohne", w["ohne"], (-1.75, 2.62), FM, "center", GRAU)
    h_r = L(s, "mit", w["mit"], (1.75, 2.62), FM, "center", GRAU)
    # links
    cd_l = chip(s, (-2.55, yc), 'cd "$1"', DUNKEL, WEISS, g=TT)
    zw_l = ziel_weg(-0.75)
    p_cd_l = pfk(s, (r4(-2.55 + chipb('cd "$1"', TT) / 2 + 0.04), yc), (-1.55, yc), DUNKEL, 2.5)
    x_l = kreuz(s, -1.42, yc, 0.15)
    p_dn = pfk(s, (-2.55, r4(yc - 0.16)), (-2.55, r4(yr + 0.16)), DUNKEL, 2.5)
    l_tr = L(s, "trotzdem", w["trotzdem"], (-2.4, r4((yc + yr) / 2)), FM, "left", ROT)
    rm_l = chip(s, (-2.55, yr), "rm -f -- *.tmp", DUNKEL, WEISS, g=TT)
    or_l = ordner(-1.75)
    wi_l = chip(s, (-2.0, r4(yo - 0.08)), "wichtig.tmp", GRAU, GELB)
    gz_l = chip(s, (-2.0, r4(yo - 0.08)), "wichtig.tmp", HELLGRAU, WEISS, textfarbe=HELLGRAU, dash="4,4")
    l_ge = L(s, "geloescht", w["geloescht"], (-1.35, r4(yo - 0.08)), FM, "left", ROT)
    p_rm = pfk(s, (-2.45, r4(yr - 0.16)), (-2.15, r4(yo + 0.08)), ORANGE, 3)
    # rechts
    cd_r = chip(s, (0.95, yc), 'if ! cd "$1"', DUNKEL, WEISS, g=TT)
    zw_r = ziel_weg(2.75)
    p_cd_r = pfk(s, (r4(0.95 + chipb('if ! cd "$1"', TT) / 2 + 0.04), yc), (1.95, yc), DUNKEL, 2.5)
    x_r = kreuz(s, 2.08, yc, 0.15)
    p_ex = pfk(s, (0.95, r4(yc - 0.16)), (r4(2.45 - chipb("exit 1", TT) / 2 - 0.03), ye), ROT, 2.5, knick="vh")
    ex = chip(s, (2.45, ye), "exit 1", ROT, ROT_HELL, g=TT)
    p_gr = lin(s, (0.95, r4(ye - 0.06)), (0.95, r4(yr + 0.16)), HELLGRAU, 2, "4,4")
    rm_r = chip(s, (0.95, yr), "rm -f -- *.tmp", HELLGRAU, WEISS, g=TT, textfarbe=GRAU)
    l_gr = L(s, "grau", w["grau"], (1.7, yr), FM, "left", GRAU)
    or_r = ordner(1.75)
    wi_r = chip(s, (1.5, r4(yo - 0.08)), "wichtig.tmp", GRAU, GELB)
    hk = haken(s, 2.2, r4(yo - 0.08), GRUEN, 0.08, 3)
    l_bl = L(s, "bleibt", w["bleibt"], (2.35, r4(yo - 0.08)), FM, "left", GRUEN)
    schritt(s, EIN([kopf, trenn, h_l, h_r], 0.6))
    schritt(s, EIN(flach(cd_l) + zw_l + or_l + flach(wi_l), 0.6))
    s.pause(0.3)
    schritt(s, ZEICHNE(p_cd_l, 0.5))
    schritt(s, EIN(x_l, 0.4))
    schritt(s, ZEICHNE(p_dn, 0.5), EIN([l_tr] + rm_l, 0.6))
    schritt(s, ZEICHNE(p_rm, 0.5))
    schritt(s, AUS(wi_l, 0.6), EIN(gz_l + [l_ge], 0.6))
    s.pause(0.8)
    schritt(s, EIN(flach(cd_r) + zw_r + flach(rm_r) + or_r + flach(wi_r), 0.6))
    s.pause(0.3)
    schritt(s, ZEICHNE(p_cd_r, 0.5))
    schritt(s, EIN(x_r, 0.4))
    schritt(s, ZEICHNE(p_ex, 0.6), EIN(ex, 0.6))
    schritt(s, EIN([p_gr, l_gr], 0.5))
    schritt(s, EIN(hk + [l_bl], 0.5))
    s.speichern()


W_SU = {"ohne": ("ohne set -u", "without set -u", "sin set -u", "没有 set -u", "sans set -u", "set -u olmadan"),
        "mit": ("mit set -u", "with set -u", "con set -u", "有 set -u", "avec set -u", "set -u ile"),
        "nicht": ("gibt es nicht:\nliefert nichts", "does not exist:\nyields nothing", "no existe:\nno da nada", "不存在：\n什么也得不到",
                  "n'existe pas :\nne donne rien", "yok:\nhiçbir şey vermez"),
        "gemeint": ("gemeint", "meant", "la intención", "本来想要的", "voulu", "kastedilen"),
        "leer": ("leer", "empty", "vacío", "空", "vide", "boş"),
        "halt": ("Skript hält an:\nFertig. erscheint nicht", "script stops:\nFertig. never appears",
                 "el script se detiene:\nFertig. no aparece", "脚本停止：\n不会出现 Fertig.", "le script s'arrête :\nFertig. n'apparaît pas",
                 "betik durur:\nFertig. görünmez")}


def k10setu():
    """Zwei Läufe von tippfehler.sh. Oben ohne set -u (skripte/tippfehler_v1.sh, Block s8_tippfehler): echo "Ich sichere
    $odrner" greift in eine Schublade odrner, die es nicht gibt, und bekommt nichts; die Ausgabe Ich sichere endet im
    Leeren, das Skript läuft bis Fertig., Status 0. Unten mit set -u (skripte/tippfehler.sh, Block s8_setu): derselbe
    Griff löst ein rotes Signal aus, Meldung unbound variable, Halt, Status 1. Rechts oben die Schublade ordner = fotos,
    die gemeint war."""
    s = Szene("linux/k10setu", reihenfolge="anlegen")
    w = W_SU
    zeile = 'echo "Ich sichere $odrner"'
    xg = 0.2

    def geist_sb(y, farbe=HELLGRAU):
        return [box(s, (xg, y), 1.0, 0.36, farbe, WEISS, 2, "rect", "5,4"), tx(s, "odrner", (xg, y), TK, "center", GRAU)]

    # oben
    l_o = L(s, "ohne", w["ohne"], (-3.3, 2.68), FM, "left", GRAU)
    g1 = s.raster(zeile, (-3.3, 2.32), groesse=TT)
    a, b = g1.finde(0, "$odrner")
    r1 = g1.rahmen(0, a, b, ORANGE, 2.5, rand=0.0)
    p1 = pfk(s, (r4(g1.xr(25) + 0.06), 2.32), (r4(xg - 0.53), 2.32), ORANGE, 2.5)
    gs1 = geist_sb(2.32)
    l_n = L(s, "nicht", w["nicht"], (xg, 1.9), FM, "center", GRAU)
    sb = schublade(s, 2.45, 2.32, "ordner", slot=5)
    wo = wert(s, sb, "fotos")
    p_g = pfk(s, (r4(xg + 0.53), 2.32), (r4(2.45 - sb["b"] / 2 - 0.03), 2.32), GRAU, 2, "4,4")
    l_g = L(s, "gemeint", w["gemeint"], (1.25, 2.47), FM, "center", GRAU)
    g2 = s.raster(["Ich sichere ", "Fertig."], (-3.3, 1.82), groesse=TK)
    xl0 = r4(g2.xr(11) + 0.04)
    leer_ = [box(s, (r4(xl0 + 0.25), g2.y(0)), 0.5, 0.2, GRAU, WEISS, 1.5, "rect", "3,3"),
             L(s, "leer", w["leer"], (r4(xl0 + 0.62), g2.y(0)), FM, "left", GRAU)]
    st0 = schild(s, -3.1, 1.36, 0) + [L(s, "exit", W_EXIT, (-2.88, 1.36), FM, "left", GRAU)]
    # unten
    sep = lin(s, (-3.3, 1.12), (3.3, 1.12), HELLGRAU, 2, "6,5")
    l_m = L(s, "mit", w["mit"], (-3.3, 0.92), FM, "left", GRAU)
    g3 = s.raster(zeile, (-3.3, 0.6), groesse=TT)
    r3 = g3.rahmen(0, a, b, ROT, 2.5, rand=0.0)
    p3 = pfk(s, (r4(g3.xr(25) + 0.06), 0.6), (r4(xg - 0.53), 0.6), ROT, 2.5)
    gs3 = geist_sb(0.6)
    sig = box(s, (xg, 0.6), 1.12, 0.46, ROT, ROT_HELL, 3, "rect", deckung=0.0)
    l_h = L(s, "halt", w["halt"], (0.9, 0.6), FM, "left", ROT)
    msg = tx(s, "tippfehler.sh: line 5: odrner: unbound variable", (-3.3, 0.18), TK, "left", ROT)
    st1 = schild(s, -3.1, -0.16, 1) + [L(s, "exit", W_EXIT, (-2.88, -0.16), FM, "left", GRAU)]
    schritt(s, EIN([l_o] + g1.ids + sb["alle"] + wo, 0.6))
    schritt(s, EIN(r1, 0.4))
    schritt(s, ZEICHNE(p1, 0.5), EIN(gs1, 0.5))
    schritt(s, EIN(l_n, 0.5), ZEICHNE(p_g, 0.5), EIN(l_g, 0.5))
    s.pause(0.4)
    schritt(s, EIN([g2.ids[0]] + leer_, 0.6))
    schritt(s, EIN(g2.ids[1], 0.4))
    schritt(s, EIN(st0, 0.5))
    s.pause(0.8)
    schritt(s, EIN([sep, l_m] + g3.ids, 0.6))
    schritt(s, EIN(r3, 0.4))
    schritt(s, ZEICHNE(p3, 0.5), EIN(gs3, 0.5))
    schritt(s, EIN([sig, msg], 0.5))
    schritt(s, EIN(st1 + [l_h], 0.6))
    s.speichern()


W_SE = {"waechter": ("Wächter am Eingang", "guard at the entrance", "guardián en la entrada", "入口处的守卫", "gardien à l'entrée",
                     "girişteki bekçi"),
        "geprueft": ("Status geprüft: Wächter schaut weg", "status checked: guard looks away", "estado comprobado: el guardián no mira",
                     "状态被检查：守卫不管", "code testé : le gardien ignore", "durum denetlendi: bekçi bakmaz"),
        "greift": ("ungeprüft: Wächter greift, Ende mit 1", "unchecked: guard steps in, exit with 1",
                   "sin comprobar: actúa el guardián, sale con 1", "未检查：守卫出手，以 1 结束", "non testé : le gardien agit, fin avec 1",
                   "denetlenmedi: bekçi girer, 1 ile biter"),
        "titel": ("Hier schaut der Wächter weg:", "Here the guard looks away:", "Aquí el guardián no mira:", "守卫在这些地方不管：",
                  "Ici, le gardien ne regarde pas :", "Bekçi burada bakmaz:"),
        "e1": ("Bedingung von if, while, until", "condition of if, while, until", "condición de if, while, until", "if、while、until 的条件",
               "condition de if, while, until", "if, while, until koşulu"),
        "e2": ("links von && und ||", "left of && and ||", "a la izquierda de && y ||", "&& 和 || 的左边", "à gauche de && et ||",
               "&& ve ||'nin solunda"),
        "e3": ("vorn in einer Pipeline", "front part of a pipeline", "parte delantera de una tubería", "管道中靠前的命令",
               "début d'un tube", "boru hattının ön kısmı"),
        "e4": ("hinter !", "after !", "tras !", "! 之后", "après !", "! işaretinden sonra")}


def k10sete():
    """Das Skript abbruch.sh als helle Dateiansicht (skripte/abbruch.sh); am Eingang set -e als Wächter. Drei Aufrufe von
    pruefen: hinter || (Zeile 10) und als Bedingung von if (Zeile 12) wird der Status geprüft, der Wächter schaut weg;
    beim ungeprüften Aufruf (Zeile 15) greift er, das Skript endet mit 1, Zeile 16 bleibt grau. Unten die Ausgabe
    (Block s8_sete), rechts die Liste der Stellen, an denen der Wächter wegschaut."""
    s = Szene("linux/k10sete", reihenfolge="anlegen")
    w = W_SE
    zeilen =["#!/bin/bash", "# abbruch.sh: wo set -e greift und wo nicht", "set -e", "", "pruefen() {", "    false",
              '    echo "  in pruefen nach false weiter"', "}", "", 'pruefen || echo "  pruefen meldet einen Fehler"',
              "echo \"1: nach 'pruefen || ...'\"", "if pruefen; then", '    echo "2: im if-Zweig"', "fi", "pruefen",
              'echo "3: diese Zeile erscheint nie"']
    d = s.datei("abbruch.sh", "\n".join(zeilen), pos=(-3.4, 2.75), spalten=47, groesse=TK)
    xl = r4(d.rechts + 0.12)
    r_e = d.rahmen(2, 0, 5, ORANGE, 2.5, rand=0.0)
    l_e = L(s, "waechter", w["waechter"], (xl, d.y(2)), FM, "left", ORANGE)
    m1 = d.markieren(9, 0, 46, GRUEN, 0.22)
    m2 = d.markieren(11, 0, 46, GRUEN, 0.22)
    m3 = d.markieren(14, 0, 46, ROT, 0.22)
    nie = d.markieren(15, 0, 46, WEISS, 0.6)
    l1 = L(s, "geprueft", w["geprueft"], (xl, d.y(9)), FM, "left", GRUEN)
    l2 = L(s, "geprueft", w["geprueft"], (xl, d.y(11)), FM, "left", GRUEN)
    l3 = L(s, "greift", w["greift"], (xl, d.y(14)), FM, "left", ROT)
    aus = s.raster(["$ bash abbruch.sh", "  in pruefen nach false weiter", "1: nach 'pruefen || ...'",
                    "  in pruefen nach false weiter", "2: im if-Zweig", "$ echo $?", "1"], (-3.3, -0.3), groesse=TK)
    liste = [L(s, "titel", w["titel"], (0.45, -0.3), FM, "left", DUNKEL)] + \
            [L(s, k, w[k], (0.6, r4(-0.58 - 0.26 * i)), FM, "left", GRAU) for i, k in enumerate(("e1", "e2", "e3", "e4"))]
    schritt(s, EIN(d.id, 0.6))
    schritt(s, EIN([r_e, l_e], 0.6))
    s.pause(0.4)
    schritt(s, EIN(aus.ids[0], 0.4))
    schritt(s, EIN([m1, l1], 0.6))
    schritt(s, EIN(aus.ids[1:3], 0.5))
    schritt(s, EIN([m2, l2], 0.6))
    schritt(s, EIN(aus.ids[3:5], 0.5))
    s.pause(0.3)
    schritt(s, EIN([m3, l3], 0.6))
    schritt(s, EIN([nie] + aus.ids[5:], 0.5))
    s.pause(0.5)
    schritt(s, EIN(liste, 0.7))
    s.speichern()


# ================================================================== Abschnitt 9: Aufräumen
TAR_LISTE = ["./", "./strand 2.jpg", "./berg.png", "./2026/", "./strand 1.jpg", "./2027/"]
W_TA = {"hinein": ("erst hineinwechseln", "change into it first", "entrar primero", "先进入该目录", "y entrer d'abord", "önce içine gir"),
        "punkt": (".: alles darin", ".: everything in it", ".: todo lo de dentro", ".：里面的全部", ". : tout son contenu", ".: içindeki her şey"),
        "packen": ("einpacken", "pack", "empaquetar", "打包", "emballer", "paketle"),
        "pressen": ("zusammenpressen", "compress", "comprimir", "压缩", "comprimer", "sıkıştır"),
        "etikett": ("Etikett", "label", "etiqueta", "标签", "étiquette", "etiket"),
        "schauen": ("nur hineinschauen:\nalles bleibt im Archiv", "only look inside:\neverything stays in the archive",
                    "solo mirar dentro:\ntodo se queda en el archivo", "只是查看：\n内容都留在归档里",
                    "seulement regarder :\ntout reste dans l'archive", "yalnızca içine bak:\nher şey arşivde kalır")}


def k10tar():
    """tar -czf fotos.tar.gz -C fotos . (Block s9_tar): Links das Verzeichnis fotos mit strand 1.jpg, strand 2.jpg,
    berg.png, 2026/, 2027/; ein Wegweiser -C fotos „erst hineinwechseln“, „.“ nimmt alles darin mit. Kopien der
    Einträge wandern in einen Karton (-c), zwei Pfeile pressen ihn zusammen (-z), das Paket bekommt das Etikett
    fotos.tar.gz (-f). Unten tar -tzf fotos.tar.gz: die Namen mit ./ davor, in der Reihenfolge der Mitschrift."""
    s = Szene("linux/k10tar", reihenfolge="anlegen")
    w = W_TA
    cmd = tx(s, "tar -czf fotos.tar.gz -C fotos .", (-3.3, 2.75), TT, "left", DUNKEL)
    eintraege = [("strand 1.jpg", False), ("strand 2.jpg", False), ("berg.png", False), ("2026/", True), ("2027/", True)]
    yo = [1.75, 1.51, 1.27, 1.03, 0.79]
    xo, xk = -2.3, 0.45
    ordner = [box(s, (-2.35, 1.38), 1.9, 1.6, BLAU, WEISS, 2, "rect"), tx(s, "fotos", (-3.2, 2.0), TT, "left", BLAU)]
    karten = [chip(s, (xo, y), t, BLAU if d else GRAU, BLAU_HELL if d else GELB) for (t, d), y in zip(eintraege, yo)]
    weg = [chip(s, (-2.35, 2.42), "-C fotos", ORANGE, ORANGE_HELL, g=TT), L(s, "hinein", w["hinein"], (-1.65, 2.42), FM, "left", ORANGE)]
    l_pkt = L(s, "punkt", w["punkt"], (-2.35, 0.38), FM, "center", GRAU)
    karton = [box(s, (xk, 1.38), 1.5, 1.45, ORANGE, ORANGE_HELL, 2.5, "rect"), tx(s, "-c", (1.32, 1.95), TT, "left", ORANGE),
              L(s, "packen", w["packen"], (1.57, 1.95), FM, "left", ORANGE)]
    yk = [1.86, 1.64, 1.42, 1.2, 0.98]
    kopien = [chip(s, (xo, y), t, BLAU if d else GRAU, BLAU_HELL if d else GELB) for (t, d), y in zip(eintraege, yo)]
    presse = [pfk(s, (xk, 2.6), (xk, 2.15), DUNKEL, 3), pfk(s, (xk, 0.18), (xk, 0.6), DUNKEL, 3),
              tx(s, "-z", (r4(xk + 0.15), 0.35), TT, "left", DUNKEL), L(s, "pressen", w["pressen"], (r4(xk + 0.45), 0.35), FM, "left", DUNKEL)]
    paket = box(s, (xk, 1.38), 1.5, 0.55, ORANGE, ORANGE_HELL, 2.5, "rect")
    etikett = chip(s, (xk, 1.38), "fotos.tar.gz", DUNKEL, WEISS)
    l_f = [tx(s, "-f", (1.32, 1.38), TT, "left", DUNKEL), L(s, "etikett", w["etikett"], (1.57, 1.38), FM, "left", DUNKEL)]
    sep = lin(s, (-3.3, 0.12), (3.3, 0.12), HELLGRAU, 2, "6,5")
    cmd2 = tx(s, "$ tar -tzf fotos.tar.gz", (-3.3, -0.12), TT, "left", DUNKEL)
    g = s.raster(TAR_LISTE, (-3.3, -0.42), groesse=TK)
    marken = [g.markieren(z, 0, 1, ORANGE, 0.3) for z in range(len(TAR_LISTE))]
    l_sch = L(s, "schauen", w["schauen"], (-1.3, -0.85), FM, "left", GRAU)
    schritt(s, EIN(cmd, 0.5))
    schritt(s, EIN(ordner + flach(karten), 0.6))
    s.pause(0.4)
    schritt(s, EIN(flach(weg), 0.6))
    schritt(s, EIN(l_pkt, 0.5))
    s.pause(0.3)
    schritt(s, EIN(karton, 0.5))
    schritt(s, EIN(flach(kopien), 0.2))
    schritt(s, *[v for k, y0, y1 in zip(kopien, yo, yk) for v in VERS(k, xk - xo, y1 - y0, 0.9)])
    s.pause(0.3)
    schritt(s, ZEICHNE(presse[:2], 0.5), EIN(presse[2:], 0.5))
    schritt(s, AUS([karton[0]] + flach(kopien), 0.6), EIN(paket, 0.6), VER(presse[0], 0, -0.46, 0.6),
            *VERS([presse[1]] + presse[2:], 0, 0.46, 0.6))
    schritt(s, EIN(flach(etikett) + l_f, 0.6))
    s.pause(0.7)
    schritt(s, EIN([sep, cmd2], 0.5))
    schritt(s, EIN(g.ids, 0.6))
    schritt(s, EIN(marken + [l_sch], 0.6))
    s.speichern()


W_MK = {"zweiter": ("zweiter Lauf:", "second run:", "segunda ejecución:", "第二次运行：", "deuxième exécution :", "ikinci çalıştırma:"),
        "andere": ("Dateien anderer Benutzer", "other users' files", "archivos de otros usuarios", "其他用户的文件",
                   "fichiers d'autres utilisateurs", "diğer kullanıcıların dosyaları"),
        "stempel": ("neu angelegt, leer,", "newly created, empty,", "recién creado, vacío,", "新建，空，", "nouveau, vide,", "yeni, boş,"),
        "anders": ("anderer Name", "a different name", "otro nombre", "另一个名字", "un autre nom", "başka bir ad")}


def k10mktemp():
    """Links zwischen=$(mktemp) (Block s9_mktemp): Die Vorlage tmp. mit zehn leeren Feldern X; zehn Würfel fallen hinein
    und zeigen J o p P Y F g z y A. Daraus wird die Datei tmp.JopPYFgzyA im Verzeichnis /tmp, zwischen Dateien
    anderer Benutzer, mit dem Stempel „neu angelegt, leer, rw-------“ und einem Schloss. Rechts ein zweiter Lauf mit
    anderem Namen (tmp.ULJNwITrfq, ebenfalls ein Name aus dem Heft, Abschnitt 9.3)."""
    s = Szene("linux/k10mktemp", reihenfolge="anlegen")
    w = W_MK
    yv = 2.25

    def vorlage(x0, zeichen):
        felder = [box(s, (r4(x0 + 0.48 + 0.22 * k), yv), 0.19, 0.26, HELLGRAU, WEISS, 1.5, "rect", "3,3") for k in range(10)]
        xe = [tx(s, "X", (r4(x0 + 0.48 + 0.22 * k), yv), TT, "center", HELLGRAU) for k in range(10)]
        kopf = tx(s, "tmp.", (x0, yv), TT, "left", DUNKEL)
        wuerfel = [chip(s, (r4(x0 + 0.48 + 0.22 * k), r4(yv + 0.45)), z, ORANGE, WEISS, g=TT, b=0.2, h=0.26)
                   for k, z in enumerate(zeichen)]
        return [kopf] + felder, xe, wuerfel

    ordner = [box(s, (0.0, 0.5), 6.7, 1.0, BLAU, WEISS, 2, "rect"), tx(s, "/tmp", (-3.25, 0.84), TT, "left", BLAU)]
    fremd = [box(s, (r4(-0.3 + 0.52 * k), 0.2), 0.44, 0.22, HELLGRAU, GRAU_HELL, 1.5, "rect") for k in range(3)]
    l_fr = L(s, "andere", w["andere"], (1.1, 0.2), FM, "left", GRAU)
    h1 = tx(s, "$ zwischen=$(mktemp)", (-3.3, 2.75), TK, "left", DUNKEL)
    v1, x1, wf1 = vorlage(-3.2, "JopPYFgzyA")
    p1 = pfk(s, (-2.2, 2.0), (-2.2, 0.72), DUNKEL, 2.5)
    d1 = chip(s, (-2.2, 0.55), "tmp.JopPYFgzyA", GRAU, GELB)
    sl1 = s.schloss((-1.35, 0.55), 0.24)
    st = [box(s, (-1.9, 0.2), 2.5, 0.26, ROT, WEISS, 2), L(s, "stempel", w["stempel"], (-3.05, 0.2), FM, "left", ROT),
          tx(s, "rw-------", (-1.42, 0.2), TK, "left", ROT)]
    h2 = L(s, "zweiter", w["zweiter"], (0.3, 2.75), FM, "left", GRAU)
    v2, x2, wf2 = vorlage(0.3, "ULJNwITrfq")
    p2 = pfk(s, (1.3, 2.0), (1.3, 0.72), DUNKEL, 2.5)
    d2 = chip(s, (1.3, 0.55), "tmp.ULJNwITrfq", GRAU, GELB)
    sl2 = s.schloss((2.15, 0.55), 0.24)
    l_an = L(s, "anders", w["anders"], (2.38, 0.55), FM, "left", GRUEN)
    schritt(s, EIN([h1] + v1 + x1 + ordner + fremd + [l_fr], 0.6))
    s.pause(0.4)
    schritt(s, EIN(flach(wf1), 0.3))
    schritt(s, *[v for c in wf1 for v in VERS(c, 0, -0.45, 0.8)], AUS(x1, 0.8))
    schritt(s, ZEICHNE(p1, 0.5), EIN(flach(d1) + [sl1], 0.6))
    schritt(s, EIN(st, 0.6))
    s.pause(0.7)
    schritt(s, EIN([h2] + v2 + x2, 0.6))
    schritt(s, EIN(flach(wf2), 0.3))
    schritt(s, *[v for c in wf2 for v in VERS(c, 0, -0.45, 0.8)], AUS(x2, 0.8))
    schritt(s, ZEICHNE(p2, 0.5), EIN(flach(d2) + [sl2], 0.6))
    schritt(s, EIN(l_an, 0.5))
    s.speichern()


W_TR = {"start": ("Start", "start", "inicio", "开始", "début", "başlangıç"),
        "arbeit": ("Arbeitsteil: sleep 600", "main work: sleep 600", "trabajo: sleep 600", "工作部分：sleep 600", "travail : sleep 600",
                   "iş kısmı: sleep 600"),
        "schild": ("vor dem Ende: rm", "before the end: rm", "antes del final: rm", "结束前：rm", "avant la fin : rm", "bitmeden önce: rm"),
        "r1": ("läuft durch", "runs to the end", "llega al final", "运行到结束", "va jusqu'au bout", "sonuna kadar çalışır"),
        "r2": ("exit 1", "exit 1", "exit 1", "exit 1", "exit 1", "exit 1"),
        "r3": ("Strg+C (SIGINT)", "Ctrl+C (SIGINT)", "Ctrl+C (SIGINT)", "Ctrl+C (SIGINT)", "Ctrl+C (SIGINT)", "Ctrl+C (SIGINT)"),
        "r4": ("kill (SIGTERM)", "kill (SIGTERM)", "kill (SIGTERM)", "kill (SIGTERM)", "kill (SIGTERM)", "kill (SIGTERM)"),
        "r5": ("kill -9 (SIGKILL)", "kill -9 (SIGKILL)", "kill -9 (SIGKILL)", "kill -9 (SIGKILL)", "kill -9 (SIGKILL)", "kill -9 (SIGKILL)"),
        "weg": ("rm löscht\ndie Datei", "rm deletes\nthe file", "rm borra\nel archivo", "rm 删除\n这个文件", "rm supprime\nle fichier",
                "rm dosyayı\nsiler"),
        "bleibt": ("bleibt liegen", "is left behind", "se queda ahí", "留了下来", "reste là", "geride kalır")}


def k10trap():
    """Zeitleiste von zwischendatei.sh senkrecht links: Start, mktemp legt /tmp/tmp.ULJNwITrfq an (Block s9_trap im Heft),
    trap '...' EXIT hängt das Schild „vor dem Ende: rm“ an den Ausgang, dann der lange Arbeitsteil. Fünf Enden zweigen
    nach rechts ab: läuft durch, exit 1, Strg+C (SIGINT), kill (SIGTERM) führen durch den Ausgang, rm löscht die Datei;
    kill -9 (SIGKILL) führt unter dem Ausgang vorbei, die Datei tmp.occObehWXm bleibt rot liegen (Block s9_trapkill)."""
    s = Szene("linux/k10trap", reihenfolge="anlegen")
    w = W_TR
    xt, xd = -3.0, 1.65
    ys = [1.3, 0.85, 0.4, -0.05, -0.55]
    start = [s.punkt(None, xt, 2.65, DUNKEL, 0.07), L(s, "start", w["start"], (-2.85, 2.65), FM, "left", DUNKEL)]
    achse = lin(s, (xt, 2.65), (xt, 1.75), DUNKEL, 2.5)
    n_mk = [s.kreis(None, xt, 2.3, 0.06, farbe=DUNKEL, dicke=2, fuellung=WEISS, deckung=1.0), tx(s, "mktemp", (-2.85, 2.3), TK, "left")]
    p_mk = pfk(s, (-2.35, 2.3), (-1.98, 2.3), DUNKEL, 2)
    datei_ = chip(s, (-1.1, 2.3), "/tmp/tmp.ULJNwITrfq", GRAU, GELB)
    n_tr = [s.kreis(None, xt, 1.95, 0.06, farbe=DUNKEL, dicke=2, fuellung=WEISS, deckung=1.0), tx(s, "trap '...' EXIT", (-2.85, 1.95), TK, "left")]
    p_tr = pfk(s, (-1.65, 1.95), (0.73, 1.95), ORANGE, 2, "5,4")
    schild_ = [box(s, (xd, 1.95), 1.8, 0.3, ORANGE, WEISS, 2.5), L(s, "schild", w["schild"], (xd, 1.95), FM, "center", ORANGE)]
    tuer = box(s, (xd, 0.63), 0.2, 1.75, ORANGE, ORANGE_HELL, 2.5, "rect")
    arbeit = [lin(s, (xt, 1.75), (xt, -0.65), GRAU, 8), L(s, "arbeit", w["arbeit"], (-2.85, 1.62), FM, "left", GRAU)]
    zeilen_, labels, nach = [], [], []
    for k, y in enumerate(ys):
        ende = (xd - 0.12) if k < 4 else 2.0
        zeilen_.append(pfk(s, (xt, y), (ende, y), ROT if k == 4 else DUNKEL, 2.5))
        labels.append(L(s, "r%d" % (k + 1), w["r%d" % (k + 1)], (-2.85, r4(y + 0.13)), FM, "left", ROT if k == 4 else DUNKEL))
        if k < 4:
            nach.append(pfk(s, (r4(xd + 0.12), y), (2.05, y), GRUEN, 2.5))
    kl = vklammer(s, 2.2, r4(ys[0] + 0.08), r4(ys[3] - 0.08), GRUEN, 0.07, 2.5)
    l_weg = L(s, "weg", w["weg"], (2.32, r4((ys[0] + ys[3]) / 2)), FM, "left", GRUEN)
    rest = chip(s, (2.72, ys[4]), "tmp.occObehWXm", ROT, ROT_HELL, dicke=2.5)
    l_bl = L(s, "bleibt", w["bleibt"], (2.72, r4(ys[4] - 0.3)), FM, "center", ROT)
    schritt(s, EIN(start + [achse], 0.5))
    schritt(s, EIN(n_mk, 0.4), ZEICHNE(p_mk, 0.4), EIN(datei_, 0.5))
    schritt(s, EIN(n_tr, 0.4))
    schritt(s, ZEICHNE(p_tr, 0.6), EIN(schild_ + [tuer], 0.6))
    schritt(s, EIN(arbeit, 0.6))
    s.pause(0.5)
    for k in range(4):
        schritt(s, ZEICHNE(zeilen_[k], 0.5), EIN(labels[k], 0.5))
        schritt(s, ZEICHNE(nach[k], 0.3))
    schritt(s, ZEICHNE(kl, 0.4), EIN(l_weg, 0.5))
    s.pause(0.6)
    schritt(s, ZEICHNE(zeilen_[4], 0.6), EIN(labels[4], 0.6))
    schritt(s, EIN(flach(rest) + [l_bl], 0.6))
    s.speichern()


SICHERUNG = """#!/bin/bash
# sicherung.sh: packt ein Verzeichnis in ein Archiv mit dem Datum im Namen
#   Aufruf:      sicherung.sh QUELLE ZIEL
#   Beispiel:    sicherung.sh fotos sicherungen
#   Exit-Status: 0 Sicherung angelegt, 1 Fehler, 2 falscher Aufruf

# --- Einstellungen ---
set -u
set -o pipefail

programm=$(basename "$0")

# --- Funktionen ---
fehler() {
    echo "$programm: $1" >&2
    exit 1
}

# --- Argumente prüfen ---
if [ $# -ne 2 ]; then
    echo "Aufruf: $programm QUELLE ZIEL" >&2
    exit 2
fi
quelle=$1
ziel=$2
[ -d "$quelle" ] || fehler "$quelle ist kein Verzeichnis"
[ -d "$ziel" ] || fehler "$ziel ist kein Verzeichnis"
archiv="$ziel/sicherung_$(date +%F).tar.gz"
if [ -e "$archiv" ]; then
    fehler "$archiv gibt es schon"
fi

# --- Aufräumen vorbereiten ---
tmp=$(mktemp -p "$ziel" .sicherung.XXXXXX) || fehler "keine Zwischendatei in $ziel"
trap 'rm -f "$tmp"' EXIT

# --- Hauptteil ---
tar -czf "$tmp" -C "$quelle" . || fehler "tar ist gescheitert"
mv "$tmp" "$archiv" || fehler "kann $archiv nicht anlegen"
echo "Gesichert: $archiv"
exit 0"""
W_GE = {"t1": ("Shebang", "shebang", "shebang", "shebang 行", "shebang", "shebang"),
        "t2": ("Kommentar: Zweck,\nAufruf, Exit-Status", "comment: purpose,\nusage, exit status", "comentario: propósito,\nuso, estado de salida",
               "注释：用途、\n调用、退出状态", "commentaire : but,\nappel, code de sortie", "yorum: amaç,\nçağrı, çıkış durumu"),
        "t3": ("Einstellungen", "settings", "ajustes", "设置", "réglages", "ayarlar"),
        "t4": ("feste Werte\nund Funktionen", "fixed values\nand functions", "valores fijos\ny funciones", "固定值\n和函数",
               "valeurs fixes\net fonctions", "sabit değerler\nve fonksiyonlar"),
        "t5": ("Argumente prüfen", "check arguments", "comprobar argumentos", "检查参数", "vérifier les arguments", "argümanları denetle"),
        "t6": ("Aufräumen\nvorbereiten", "prepare the\nclean-up", "preparar\nla limpieza", "准备\n清理", "préparer\nle nettoyage",
               "temizliği\nhazırla"),
        "t7": ("Hauptteil", "main part", "parte principal", "主体部分", "partie principale", "ana kısım"),
        "t8": ("Ende: exit 0", "end: exit 0", "final: exit 0", "结束：exit 0", "fin : exit 0", "son: exit 0")}
GE_TEILE = [(1, 1), (2, 5), (7, 9), (11, 17), (19, 31), (33, 35), (37, 40), (41, 41)]   # Dateizeilen der acht Teile


def umbrechen(zeilen, sp):
    """Zeilen über sp Zeichen an der letzten Wortgrenze umbrechen; die Fortsetzung beginnt mit einem grauen ↪ wie in den
    Code-Kästen des Hefts. Ergebnis (Bildschirmzeilen, erste und letzte Bildschirmzeile je Dateizeile)."""
    rows, an, bis = [], [], []
    for z in zeilen:
        an.append(len(rows))
        while len(z) > sp:
            i = z.rfind(" ", 2, sp + 1)
            rows.append(z[:i])
            z = farbig("↪", "grau") + " " + z[i + 1:]
        rows.append(z)
        bis.append(len(rows) - 1)
    return rows, an, bis


def k10geruest():
    """Pflichtbild: sicherung.sh (skripte/sicherung.sh, 41 Zeilen) als helle Dateiansicht mit 58 Spalten; die vier Zeilen
    über 58 Zeichen (2, 5, 34, 38) sind an einer Wortgrenze umbrochen, die Fortsetzung beginnt mit ↪ wie in den
    Code-Kästen des Hefts. Rechts färben sich nacheinander die Klammern der acht Teile des Skriptgerüsts aus Abschnitt
    9.4; zum Schluss leuchten die Prüfstellen auf: if … exit 2, || fehler, if [ -e … ]."""
    s = Szene("linux/k10geruest", reihenfolge="anlegen")
    w = W_GE
    sp = 58
    rows, zeile_an, zeile_bis = umbrechen(SICHERUNG.split("\n"), sp)
    d = s.datei("sicherung.sh", "\n".join(rows), pos=(-3.4, 3.6), spalten=sp, zeilen=len(rows), groesse=TK)
    xk = r4(d.rechts + 0.1)
    farben = [GRAU, GRAU, BLAU, BLAU, ORANGE, GRUEN, DUNKEL, DUNKEL]
    klammern = []
    for k, ((a, b), f) in enumerate(zip(GE_TEILE, farben)):
        ya, yb = d.oben(zeile_an[a - 1]), d.unten(zeile_bis[b - 1])
        klammern.append(vklammer(s, xk, r4(ya - 0.02), r4(yb + 0.02), f, 0.06, 2.5) +
                        [L(s, "t%d" % (k + 1), w["t%d" % (k + 1)], (r4(xk + 0.1), r4((ya + yb) / 2)), FM, "left", f)])
    pruef = []
    for nr_ in (26, 27, 34, 38, 39):
        zr = zeile_an[nr_ - 1]
        a, b = d.finde(zr, "|| fehler")
        pruef.append(d.markieren(zr, a, b, ORANGE, 0.35))
    a, b = d.finde(zeile_an[19], "if [ $# -ne 2 ]")
    pruef.append(d.markieren(zeile_an[19], a, b, ORANGE, 0.35))
    a, b = d.finde(zeile_an[21], "exit 2")
    pruef.append(d.markieren(zeile_an[21], a, b, ORANGE, 0.35))
    a, b = d.finde(zeile_an[28], 'if [ -e "$archiv" ]')
    pruef.append(d.markieren(zeile_an[28], a, b, ORANGE, 0.35))
    schritt(s, EIN(d.id, 0.7))
    s.pause(0.4)
    for k in klammern:
        schritt(s, ZEICHNE(k[:3], 0.4), EIN(k[3], 0.4))
    s.pause(0.5)
    schritt(s, EIN(pruef, 0.8))
    s.speichern()


W_SI = {"zweiter": ("zweiter Durchgang: Abbruch bei Schritt 2", "second run: aborted at step 2", "segunda pasada: se interrumpe en el paso 2",
                    "第二次：在第 2 步中断", "deuxième passage : interruption à l'étape 2", "ikinci tur: 2. adımda kesilir"),
        "abbruch": ("Abbruch", "aborted", "interrupción", "中断", "interruption", "kesildi"),
        "kein": ("kein Archiv", "no archive", "ningún archivo", "没有归档", "aucune archive", "arşiv yok")}


def k10sicherung():
    """./sicherung.sh fotos sicherungen (Block s9_sicherung im Heft, Datum 2026-11-12). Oben: (1) mktemp legt in
    sicherungen die graue versteckte Datei .sicherung.XXXXXX an; (2) tar füllt sie, ein Balken läuft; (3) Haken tar: 0,
    mv gibt ihr in einem Sprung den Namen sicherung_2026-11-12.tar.gz, sie wird farbig. Unten ein zweiter Durchgang,
    der bei Schritt 2 mit einem Blitz abbricht: trap räumt die graue Datei weg, es entsteht kein Archiv."""
    s = Szene("linux/k10sicherung", reihenfolge="anlegen")
    w = W_SI

    def lauf(y, key):
        o = {"fotos": [box(s, (-2.5, y), 1.4, 0.9, BLAU, WEISS, 2, "rect"), tx(s, "fotos", (-3.1, r4(y + 0.25)), TT, "left", BLAU)] +
             [box(s, (r4(-2.85 + 0.35 * k), r4(y - 0.1)), 0.24, 0.3, GRAU, GELB, 1.5, "rect") for k in range(3)],
             "ziel": [box(s, (1.55, y), 3.5, 1.15, BLAU, WEISS, 2, "rect"), tx(s, "sicherungen", (-0.1, r4(y + 0.42)), TT, "left", BLAU)],
             "grau": chip(s, (1.55, r4(y + 0.1)), ".sicherung.XXXXXX", HELLGRAU, GRAU_HELL, textfarbe=GRAU),
             "n1": nr(s, 0.02, r4(y + 0.1), 1), "n2": nr(s, 0.02, r4(y - 0.25), 2),
             "tar": [pfk(s, (-1.78, r4(y + 0.1)), (0.75, r4(y + 0.1)), ORANGE, 3), tx(s, "tar -czf", (-1.0, r4(y + 0.27)), TK, "center", ORANGE)]}
        s.parameter(key, 0)
        o["balken"] = s.linie(None, (0.79, r4(y - 0.25)), ("0.79+%s*%s" % (r4(2.31 - 0.79), key), r4(y - 0.25)), farbe=ORANGE, dicke=8)
        o["schiene"] = lin(s, (0.79, r4(y - 0.25)), (2.31, r4(y - 0.25)), HELLGRAU, 8)
        return o

    cmd = tx(s, "$ ./sicherung.sh fotos sicherungen", (-3.3, 2.75), TK, "left", DUNKEL)
    o1 = lauf(1.85, "f1")
    ok = haken(s, 2.5, 1.6, GRUEN, 0.08, 3) + [tx(s, "tar: 0", (2.65, 1.6), TK, "left", GRUEN)]
    archiv = chip(s, (1.55, 1.95), "sicherung_2026-11-12.tar.gz", GRUEN, GRUEN_HELL, dicke=2.5)
    n3 = nr(s, 2.9, 1.95, 3) + [tx(s, "mv", (3.05, 1.95), TK, "left", ORANGE)]
    sep = lin(s, (-3.3, 1.15), (3.3, 1.15), HELLGRAU, 2, "6,5")
    l_2 = L(s, "zweiter", w["zweiter"], (-3.3, 0.98), FM, "left", GRAU)
    o2 = lauf(0.2, "f2")
    blitz = [lin(s, (1.78, 0.2), (1.62, -0.05), ROT, 3.5), lin(s, (1.62, -0.05), (1.76, -0.05), ROT, 3.5),
             lin(s, (1.76, -0.05), (1.6, -0.32), ROT, 3.5), L(s, "abbruch", w["abbruch"], (2.0, -0.05), FM, "left", ROT)]
    g2 = [box(s, (1.55, 0.3), chipb(".sicherung.XXXXXX"), 0.28, HELLGRAU, WEISS, 2, dash="4,4")]
    trp = tx(s, "trap: rm -f", (1.55, 0.3), TK, "center", ORANGE)
    l_kein = L(s, "kein", w["kein"], (3.25, -0.25), FM, "right", GRAU)
    schritt(s, EIN(cmd, 0.5))
    schritt(s, EIN(o1["fotos"] + o1["ziel"], 0.6))
    s.pause(0.3)
    schritt(s, EIN(flach(o1["grau"]) + o1["n1"], 0.6))
    schritt(s, ZEICHNE(o1["tar"][0], 0.5), EIN([o1["tar"][1], o1["schiene"], o1["balken"]] + o1["n2"], 0.5))
    s.verstellen("f1", 1, dauer=1.0, rate="linear")
    schritt(s, EIN(ok, 0.5))
    schritt(s, AUS(o1["grau"], 0.6), EIN(flach(archiv) + n3, 0.6))
    s.pause(0.8)
    schritt(s, EIN([sep, l_2] + o2["fotos"] + o2["ziel"], 0.6))
    schritt(s, EIN(flach(o2["grau"]) + o2["n1"], 0.5))
    schritt(s, ZEICHNE(o2["tar"][0], 0.5), EIN([o2["tar"][1], o2["schiene"], o2["balken"]] + o2["n2"], 0.5))
    s.verstellen("f2", 0.45, dauer=0.5, rate="linear")
    schritt(s, EIN(blitz, 0.4))
    schritt(s, AUS(flach(o2["grau"]) + [o2["balken"], o2["schiene"]], 0.6), EIN(flach(g2) + [trp], 0.6))
    schritt(s, EIN(l_kein, 0.5))
    s.speichern()


# ================================================================== Abschnitt 10: Skripte prüfen
KAPUTT = ["#!/bin/bash", "# kaputt.sh: ein Skript mit einem Syntaxfehler", 'for datei in "$@"; do',
          '    if [ -f "$datei" ]; then', '        echo "$datei: eine Datei"', "done"]
W_BN = {"fehlt": ("hier fehlt fi", "fi is missing here", "aquí falta fi", "这里缺少 fi", "fi manque ici", "burada fi eksik"),
        "offen": ("bleibt offen", "stays open", "queda abierto", "没有闭合", "reste ouvert", "açık kalır")}


def k10bashn():
    """Oben das Terminal mit bash -n kaputt.sh und den beiden Meldezeilen (Block s10_bashn), darunter kaputt.sh
    (skripte/kaputt.sh) mit Zeilennummern. Ein Pfeil führt von der Meldung (line 6, `done') zu done in Zeile 6; eine
    gestrichelte rote Linie markiert die Lücke nach Zeile 5, wo fi fehlt. Links die Klammern: for … done geschlossen,
    if bleibt offen."""
    s = Szene("linux/k10bashn", reihenfolge="anlegen")
    w = W_BN
    t = s.terminal(pos=(-3.3, 2.95), spalten=72, zeilen=4, prompt=P10, titel=TITEL, groesse=18)
    d = s.datei("kaputt.sh", "\n".join(KAPUTT), pos=(-2.15, 1.55), spalten=48, groesse=TT)
    nums = [text(s, str(i + 1), (r4(d.links - 0.17), d.y(i)), FM, "center", GRAU) for i in range(6)]
    r1 = t.rahmen(1, 11, 16, ORANGE, 2.5, rand=0.0)
    r2 = t.rahmen(1, 54, 59, ORANGE, 2.5, rand=0.0)
    xa, xw, y1, y6 = r4(t.xr(59) + 0.07), 3.15, t.y(1), d.y(5)
    weg = [lin(s, (xa, y1), (xw, y1), ORANGE, 2.5), lin(s, (xw, y1), (xw, y6), ORANGE, 2.5),
           pfk(s, (xw, y6), (r4(d.xr(3) + 0.07), y6), ORANGE, 2.5)]
    rd = d.rahmen(5, 0, 3, ORANGE, 2.5, rand=0.0)
    xf, xi = -2.5, -2.68
    k_for = [lin(s, (xf + 0.07, d.oben(2)), (xf, d.oben(2)), BLAU, 2.5), lin(s, (xf, d.oben(2)), (xf, d.unten(5)), BLAU, 2.5),
             lin(s, (xf, d.unten(5)), (xf + 0.07, d.unten(5)), BLAU, 2.5)]
    l_for = tx(s, "for", (r4(xf - 0.06), d.oben(2)), TK, "right", BLAU)
    k_if = [lin(s, (xi + 0.07, d.oben(3)), (xi, d.oben(3)), ROT, 2.5), lin(s, (xi, d.oben(3)), (xi, d.unten(5)), ROT, 2.5),
            lin(s, (xi, d.unten(5)), (xi, r4(d.unten(5) - 0.3)), ROT, 2.5, "4,4")]
    l_if = tx(s, "if", (r4(xi - 0.06), d.oben(3)), TK, "right", ROT)
    l_off = L(s, "offen", w["offen"], (xi, r4(d.unten(5) - 0.45)), FM, "center", ROT)
    y_l = r4((d.y(4) + d.y(5)) / 2)
    luecke = lin(s, (d.x(4), y_l), (d.x(33), y_l), ROT, 2, "5,4")
    l_fehlt = L(s, "fehlt", w["fehlt"], (d.x(35), y_l), FM, "left", ROT)
    schritt(s, EIN(t.id, 0.6))
    t.eingabe("bash -n kaputt.sh")
    t.ausgabe("kaputt.sh: line 6: syntax error near unexpected token `done'\nkaputt.sh: line 6: `done'")
    t.prompt(pfad=PFAD)
    s.pause(0.3)
    schritt(s, EIN([d.id] + nums, 0.6))
    schritt(s, EIN([r1, r2], 0.5))
    schritt(s, ZEICHNE(weg, 0.8))
    schritt(s, EIN(rd, 0.4))
    s.pause(0.4)
    schritt(s, ZEICHNE(k_for, 0.5), EIN(l_for, 0.5))
    schritt(s, ZEICHNE(k_if, 0.5), EIN([l_if, l_off], 0.5))
    schritt(s, ZEICHNE(luecke, 0.5), EIN(l_fehlt, 0.5))
    s.speichern()


BEWERTUNG = ["#!/bin/bash", "# bewertung.sh: macht aus Punkten (0 bis 100) eine Bewertung", "ist_zahl() {",
             "    [[ $1 =~ ^[0-9]+$ ]]", "}", "", "punkte=$1", 'if ! ist_zahl "$punkte" || (( punkte > 100 )); then',
             '    echo "Aufruf: bewertung.sh PUNKTE   (eine ganze Zahl von 0 bis 100)" >&2', "    exit 2", "fi",
             "if (( punkte >= 90 )); then", '    echo "sehr gut"', "elif (( punkte >= 75 )); then", '    echo "gut"',
             "elif (( punkte >= 50 )); then", '    echo "bestanden"', "else", '    echo "nicht bestanden"', "fi"]
SPUR = ["+ punkte=80", "+ ist_zahl 80", "+ [[ 80 =~ ^[0-9]+$ ]]", "+ ((  punkte > 100  ))", "+ ((  punkte >= 90  ))",
        "+ ((  punkte >= 75  ))", "+ echo gut"]
SPUR_ZEILE = [6, 7, 3, 7, 11, 13, 14]          # Zeile der Datei (ab 0) zu jeder Spurzeile


def k10bashx():
    """Oben bewertung.sh (skripte/bewertung.sh, s.datei), darunter das Terminal mit bash -x bewertung.sh 80 (Block
    s10_bashx). Zu jeder Spurzeile leuchtet oben ihre Zeile auf; Nummern 1–7 rechts neben Spur und Datei ordnen sie
    einander zu (Zeile 8 zweimal: 2 und 4). Zum Schluss werden die übersprungenen Zeilen grau (9–10, 13, 16–19)."""
    s = Szene("linux/k10bashx", reihenfolge="anlegen")
    d = s.datei("bewertung.sh", "\n".join(BEWERTUNG), pos=(-3.4, 3.4), spalten=76, groesse=TK)
    t = s.terminal(pos=(-3.4, r4(d.unten_kante - 0.25)), spalten=72, zeilen=10, prompt=P10, titel=TITEL, groesse=TK)
    marken, nr_d, nr_t, gesehen = {}, [], [], {}
    for k, z in enumerate(SPUR_ZEILE):
        if z not in marken:
            marken[z] = d.markieren(z, 0, len(BEWERTUNG[z]) - 1, ORANGE, 0.3)
        n = gesehen.get(z, 0)
        gesehen[z] = n + 1
        nr_d.append(nr(s, r4(d.rechts + 0.17 + 0.25 * n), d.y(z), k + 1, r=0.1))
        nr_t.append(nr(s, r4(t.rechts + 0.17), t.y(k + 1), k + 1, r=0.1))
    grau = [d.markieren(z, 0, 75, WEISS, 0.62) for z in (8, 9, 12, 15, 16, 17, 18)]
    schritt(s, EIN(d.id, 0.6))
    schritt(s, EIN(t.id, 0.5))
    t.eingabe("bash -x bewertung.sh 80")
    for k, z in enumerate(SPUR_ZEILE):
        with s.gleichzeitig():
            t.ausgabe(SPUR[k], dauer=0.5)
            if SPUR_ZEILE.index(z) == k:
                schritt(s, EIN([marken[z]] + nr_d[k] + nr_t[k], 0.5))
            else:
                schritt(s, EIN(nr_d[k] + nr_t[k], 0.5))
        s.pause(0.2)
    t.ausgabe("gut", dauer=0.5)
    t.prompt(pfad=PFAD)
    s.pause(0.3)
    schritt(s, EIN(grau, 0.7))
    s.speichern()


SC_ZEILEN = ["", "In fehlerhaft.sh line 3:", "cd $1",
             "^---^ SC2164 (warning): Use 'cd ... || exit' or 'cd ... || return' in case cd fails.",
             "   ^-- SC2086 (info): Double quote to prevent globbing and word splitting.", "", "Did you mean:",
             'cd "$1" || exit', "", "", "In fehlerhaft.sh line 4:", "for datei in $(ls *.txt); do",
             "             ^---------^ SC2045 (error): Iterating over ls output is fragile. Use globs.",
             "                  ^-- SC2035 (info): Use ./*glob* or -- *glob* so names with dashes won't become options.", "", "",
             "In fehlerhaft.sh line 5:", "    woerter=$(wc -w < $datei)",
             "                      ^----^ SC2086 (info): Double quote to prevent globbing and word splitting.", "",
             "Did you mean:", '    woerter=$(wc -w < "$datei")', "", "", "In fehlerhaft.sh line 9:",
             'echo "Zusammen: $gesamt Wörter in $verzeichnis"',
             "                                  ^----------^ SC2154 (warning): verzeichnis is referenced but not assigned."]
SC_FARBE = {"warning": ("gelb", ORANGE), "info": ("gruen", GRUEN), "error": ("rot", ROT)}
W_SC = {"2164": ("cd prüfen", "check cd", "comprobar cd", "检查 cd", "vérifier cd", "cd'yi denetle"),
        "2086": ("Anführungs-\nzeichen", "quotes", "comillas", "加引号", "guillemets", "tırnak\nişareti"),
        "2045": ("keine Schleife\nüber ls", "no loop\nover ls", "sin bucle\nsobre ls", "不要遍历\nls 的输出", "pas de boucle\nsur ls",
                 "ls üzerinde\ndöngü yok"),
        "2035": ("./* vor\nMustern", "./* before\npatterns", "./* delante\nde patrones", "模式前\n加 ./*", "./* devant\nles motifs",
                 "kalıplardan\nönce ./*"),
        "2154": ("Variable\nnie belegt", "variable\nnever set", "variable\nsin asignar", "变量\n从未赋值", "variable\njamais définie",
                 "değişken\nhiç atanmadı")}


def k10shellcheck():
    """Das Terminal (72 Spalten wie die Mitschrift, lange Zeilen brechen um) mit dem Anfang der Ausgabe von
    shellcheck fehlerhaft.sh bis zur Meldung SC2154 (Block s10_shellcheck, ohne „For more information“). Die Meldungen
    sind nach Einstufung gefärbt (error rot, warning gelb, info grün). Nacheinander leuchtet jede Meldung auf, rechts
    erscheint ihr Etikett mit der Regel aus dem Heft."""
    s = Szene("linux/k10shellcheck", reihenfolge="anlegen")
    sp = 72
    start, r = [], 1
    for z in SC_ZEILEN:
        start.append(r)
        r += max(1, -(-len(z) // sp))
    inhalt = []
    for z in SC_ZEILEN:
        m = re.search(r"SC\d+ \((\w+)\)", z)
        inhalt.append(farbig(z, SC_FARBE[m.group(1)][0]) if m else z)
    t = s.terminal(pos=(-3.45, 3.0), spalten=sp, zeilen=r + 1, prompt=P10, titel=TITEL, groesse=TK, cursor=False)
    meldungen = [i for i, z in enumerate(SC_ZEILEN) if re.search(r"SC\d+ \(", z)]
    xl = r4(t.rechts + 0.14)
    teile, frei = [], -1
    for i in meldungen:
        code, stufe = re.search(r"SC(\d+) \((\w+)\)", SC_ZEILEN[i]).groups()
        f = SC_FARBE[stufe][1]
        zr = max(start[i], frei + 1)                   # Etikett darf nach unten ausweichen
        n = W_SC[code][0].count("\n") + 1
        mk = t.markieren(start[i], 0, sp - 1, f, 0.22, bis=start[i] + 1)
        et = [tx(s, "SC" + code, (xl, t.y(zr)), TK, "left", f),
              L(s, "sc" + code, W_SC[code], (xl, r4((t.y(zr + 1) + t.y(zr + n)) / 2)), FM, "left", f),
              lin(s, (r4(t.rechts + 0.02), t.y(start[i])), (r4(xl - 0.04), t.y(zr)), f, 1.5)]
        frei = zr + n
        teile.append((mk, et))
    schritt(s, EIN(t.id, 0.6))
    t.eingabe("shellcheck fehlerhaft.sh")
    t.ausgabe("\n".join(inhalt), dauer=0.8)
    s.pause(0.4)
    for k, (mk, et) in enumerate(teile):
        schritt(s, EIN(mk, 0.4))
        schritt(s, EIN(et, 0.5), AUS(mk, 0.5))
    s.speichern()


W_PL = {"probe": ("Probelauf", "dry run", "prueba en seco", "试运行", "essai à blanc", "deneme çalıştırması"),
        "echt": ("echter Lauf", "real run", "ejecución real", "真正运行", "exécution réelle", "gerçek çalıştırma"),
        "plakat": ("echo zeigt den Befehl nur an", "echo only shows the command", "echo solo muestra la orden", "echo 只显示这条命令",
                   "echo affiche seulement la commande", "echo komutu yalnızca gösterir"),
        "bleiben": ("bleiben stehen", "stay", "se quedan", "保留", "restent", "kalır"),
        "weg": ("gelöscht", "deleted", "borrados", "已删除", "supprimés", "silindi")}


def k10probelauf():
    """Oben der Probelauf (loesche.sh mit echo vor rm, Block s10_probelauf): echo rm -f -- *.tmp wird durch die
    Pfadnamen-Erweiterung zu echo rm -f -- c.tmp d.tmp; echo hält den fertigen Befehl wie ein Plakat hoch, c.tmp und
    d.tmp im Verzeichnis alt bleiben. Unten der echte Lauf ohne echo: derselbe Befehl geht an rm, die Dateien
    verschwinden."""
    s = Szene("linux/k10probelauf", reihenfolge="anlegen")
    w = W_PL

    def lauf(y, befehl, key):
        o = {"titel": L(s, key, w[key], (-3.3, r4(y + 0.32)), FM, "left", ORANGE if key == "probe" else ROT),
             "z1": s.raster(befehl + "*.tmp", (-3.3, y), groesse=TT),
             "p": pfk(s, (-2.9, r4(y - 0.13)), (-2.9, r4(y - 0.42)), DUNKEL, 2.5),
             "l_p": L(s, "pfad", W_PFADNAMEN, (-2.78, r4(y - 0.28)), FM, "left", GRAU),
             "z2": s.raster(befehl + "c.tmp d.tmp", (-3.3, r4(y - 0.55)), groesse=TT)}
        a = len(befehl)
        o["mk"] = o["z2"].markieren(0, a, a + 10, ORANGE, 0.3)
        o["ordner"] = [box(s, (2.65, r4(y - 0.25)), 1.3, 0.95, BLAU, WEISS, 2, "rect"), tx(s, "alt", (2.1, r4(y + 0.1)), TT, "left", BLAU)]
        o["dateien"] = [chip(s, (2.65, r4(y - 0.2)), "c.tmp", GRAU, GELB), chip(s, (2.65, r4(y - 0.5)), "d.tmp", GRAU, GELB)]
        return o

    o1 = lauf(2.3, "echo rm -f -- ", "probe")
    plakat = [box(s, (0.55, 2.0), 2.05, 0.4, DUNKEL, WEISS, 2, "rect"), tx(s, "rm -f -- c.tmp d.tmp", (0.55, 2.0), TK, "center", GRUEN),
              lin(s, (0.55, 1.8), (0.55, 1.55), DUNKEL, 3)]
    p_pl = pfk(s, (r4(-3.3 + ttb("echo rm -f -- c.tmp d.tmp", TT) + 0.06), 1.75), (-0.5, 1.95), DUNKEL, 2)
    l_pl = L(s, "plakat", w["plakat"], (0.55, 1.4), FM, "center", GRAU)
    ok = haken(s, 2.65, 1.3, GRUEN, 0.08, 3) + [L(s, "bleiben", w["bleiben"], (2.65, 1.12), FM, "center", GRUEN)]
    sep = lin(s, (-3.3, 0.95), (3.3, 0.95), HELLGRAU, 2, "6,5")
    o2 = lauf(0.45, "rm -f -- ", "echt")
    p_rm = pfk(s, (r4(-3.3 + ttb("rm -f -- c.tmp d.tmp", TT) + 0.06), -0.1), (r4(2.65 - 0.65 - 0.04), -0.1), ROT, 2.5)
    geister = [chip(s, (2.65, 0.25), "c.tmp", HELLGRAU, WEISS, textfarbe=HELLGRAU, dash="4,4"),
               chip(s, (2.65, -0.05), "d.tmp", HELLGRAU, WEISS, textfarbe=HELLGRAU, dash="4,4")]
    l_weg = L(s, "weg", w["weg"], (2.65, -0.47), FM, "center", ROT)
    for o in (o1, o2):
        schritt(s, EIN([o["titel"]] + o["z1"].ids + o["ordner"] + flach(o["dateien"]), 0.6))
        schritt(s, ZEICHNE(o["p"], 0.4), EIN(o["l_p"], 0.4))
        schritt(s, EIN(o["z2"].ids + [o["mk"]], 0.6))
        s.pause(0.3)
        if o is o1:
            schritt(s, ZEICHNE(p_pl, 0.5), EIN(plakat, 0.6))
            schritt(s, EIN(l_pl, 0.5))
            schritt(s, EIN(ok, 0.5))
            s.pause(0.8)
            schritt(s, EIN(sep, 0.3))
        else:
            schritt(s, ZEICHNE(p_rm, 0.6))
            schritt(s, AUS(flach(o["dateien"]), 0.6), EIN(flach(geister) + [l_weg], 0.6))
    s.speichern()


TESTS = [("100", "sehr gut", True), ("90", "sehr gut", True), ("89", "gut", True), ("75", "gut", True), ("74", "bestanden", True),
         ("50", "bestanden", True), ("49", "nicht bestanden", True), ("0", "nicht bestanden", True), ("101", "''", False),
         ("abc", "''", False), ('""', "''", False)]
W_TF = {"eingabe": ("Eingabe", "input", "entrada", "输入", "entrée", "girdi"),
        "erwartet": ("erwartet", "expected", "esperado", "期望", "attendu", "beklenen"),
        "grenze": ("Grenzen", "limits", "límites", "边界", "limites", "sınırlar"),
        "aussen": ("außerhalb: 101, abc, leer", "outside: 101, abc, empty", "fuera: 101, abc, vacío", "范围外：101、abc、空",
                   "hors limites : 101, abc, vide", "dışında: 101, abc, boş")}


def k10testfaelle():
    """Oben ein Zahlenstrahl 0–100 mit den Grenzen 50, 75, 90; die Testwerte sitzen beiderseits jeder Grenze (49/50,
    74/75, 89/90) und an den Enden (0, 100), 101, abc und leer liegen außerhalb. Darunter die Tabelle der elf Testfälle
    aus teste_bewertung.sh (Eingabe, erwartet); die Spalten bewertung_alt.sh (8 Haken, 3 Kreuze) und bewertung.sh
    (11 Haken) füllen sich nacheinander, darunter 3 Fehler und 0 Fehler (Block s10_tests)."""
    s = Szene("linux/k10testfaelle", reihenfolge="anlegen")
    w = W_TF
    x0, kx, ya = -3.0, 0.055, 2.35

    def xp(v):
        return r4(x0 + kx * v)

    achse = [lin(s, (xp(0), ya), (xp(100), ya), DUNKEL, 2.5)] + [lin(s, (xp(v), ya - 0.06), (xp(v), ya + 0.06), DUNKEL, 2) for v in (0, 100)]
    grenzen = [lin(s, (xp(v), r4(ya - 0.12)), (xp(v), r4(ya + 0.2)), ORANGE, 2.5, "4,3") for v in (50, 75, 90)] + \
              [tx(s, str(v), (xp(v), r4(ya + 0.32)), TK, "center", ORANGE) for v in (50, 75, 90)] + \
              [L(s, "grenze", w["grenze"], (r4(xp(50) - 0.2), r4(ya + 0.32)), FM, "right", ORANGE)]
    punkte = [s.punkt(None, xp(v), ya, BLAU, 0.04) for v in (0, 49, 50, 74, 75, 89, 90, 100)]
    p_lab = [tx(s, t_, (r4(xp(v)), r4(ya - 0.25)), TK, "center", BLAU) for t_, v in (("0", 0), ("49 50", 49.5), ("74 75", 74.5),
                                                                                       ("89 90", 89.5), ("100", 100))]
    aus101 = [s.punkt(None, xp(101), ya, ROT, 0.04), L(s, "aussen", w["aussen"], (3.35, r4(ya - 0.5)), FM, "right", ROT)]
    yk, dz = 1.35, 0.235
    xe, xw, xa, xn = -2.85, -2.45, 0.75, 2.5
    kopf = [L(s, "eingabe", w["eingabe"], (xe, yk), FM, "center", GRAU), L(s, "erwartet", w["erwartet"], (xw, yk), FM, "left", GRAU),
            tx(s, "bewertung_alt.sh", (xa, yk), TK, "center", GRAU), tx(s, "bewertung.sh", (xn, yk), TK, "center", GRAU),
            lin(s, (-3.3, r4(yk - 0.13)), (3.3, r4(yk - 0.13)), HELLGRAU, 2)]
    zeilen_, alt, neu = [], [], []
    for i, (e, erw, ok_alt) in enumerate(TESTS):
        y = r4(yk - 0.3 - dz * i)
        zeilen_ += [tx(s, e, (xe, y), TK, "center", ROT if not ok_alt else DUNKEL), tx(s, erw, (xw, y), TK, "left")]
        alt.append(haken(s, xa, y, GRUEN, 0.07, 3) if ok_alt else [kreuz(s, xa, y, 0.14)])
        neu.append(haken(s, xn, y, GRUEN, 0.07, 3))
    yf = r4(yk - 0.3 - dz * len(TESTS) - 0.05)
    fuss = [lin(s, (-3.3, r4(yf + 0.15)), (3.3, r4(yf + 0.15)), HELLGRAU, 2)]
    f_alt = tx(s, "3 Fehler", (xa, yf), TK, "center", ROT)
    f_neu = tx(s, "0 Fehler", (xn, yf), TK, "center", GRUEN)
    schritt(s, EIN(achse, 0.5))
    schritt(s, EIN(grenzen, 0.6))
    schritt(s, EIN(punkte + p_lab, 0.6))
    schritt(s, EIN(aus101, 0.5))
    s.pause(0.5)
    schritt(s, EIN(kopf + zeilen_ + fuss, 0.7))
    s.pause(0.3)
    for i in range(0, len(TESTS), 4):
        schritt(s, EIN(flach(alt[i:i + 4]), 0.4))
    schritt(s, EIN(f_alt, 0.5))
    s.pause(0.4)
    for i in range(0, len(TESTS), 4):
        schritt(s, EIN(flach(neu[i:i + 4]), 0.4))
    schritt(s, EIN(f_neu, 0.5))
    s.speichern()


SZENEN = (k10skript, k10eigeneshell, k10ablauf, k10crlf,
          k10parameter, k10null, k10at, k10shift,
          k10if, k10klammer, k10dateiinfo, k10leerfalle, k10zahltext,
          k10doppelklammer, k10regex, k10doppelrund, k10verknuepfen, k10case,
          k10for, k10lsfalle, k10forc, k10while, k10break,
          k10read, k10whileread, k10ifs, k10pipefalle, k10array,
          k10funktion, k10funktionsparameter, k10local, k10rueckgabe, k10funktionskript,
          k10exit, k10cdfalle, k10setu, k10sete,
          k10tar, k10mktemp, k10trap, k10geruest, k10sicherung,
          k10bashn, k10bashx, k10shellcheck, k10probelauf, k10testfaelle)

if __name__ == "__main__":
    wahl = set(sys.argv[1:])
    for f in SZENEN:
        if not wahl or f.__name__ in wahl:
            f()
            print("gebaut:", f.__name__)
