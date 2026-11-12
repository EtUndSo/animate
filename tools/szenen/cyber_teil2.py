"""Cybersecurity, Kapitel 2 „Schutzgrenzen in Hardware und Betriebssystem“ (C:\\Bücher\\EtUndSo\\Cybersecurity\\Arbeitshefte\\
Kap2_Schutzgrenzen.tex, kap2_stufen.tex, kap2_stufen_b.tex): Abbildungen, alle animiert (notizen/animationen.md §5, §11).

Szenenname cyber/k2<name> = \\label{fig:k2<name>} im Heft (\\szenenabb{k2<name>}{…}{fig:k2<name>}); Liste in uebergabe_kap2.md,
Abschnitt „Endgültige Abbildungsliste“. Phase 2b-1 (12.11.2026): Abschnitte 1–6 (26 Szenen). Phase 2b-2 ergänzt die
Abschnitte 7–10 in dieser Datei und benutzt die Helfer und Wortlisten unten.
Stil: F1 für echte Ausgaben (s.terminal dunkel, Prompt student@labor:~/cyberk2$ wie nach `cd ~/cyberk2` in 1.1;
s.raster für Ausgabezeilen ohne Fenster). Übrige Schemata aus Kästen und Pfeilen (Helfer unten).
Inhalte (Befehle, Ausgaben, Adressen, Zähler) wörtlich aus dem Heft bzw. code\\kap2\\mitschrift_kap2*.txt; Rechenbilder
mit den Zahlen aus rechnung_kap2.py. Wo das Heft keinen Wert nennt (Bytes eines Befehls, Kerneladresse in IA32_LSTAR),
steht ein Wort statt einer erfundenen Zahl.
Farben: blau = Programm/Stufe 3, orange = Kernel/Stufe 0 und Hervorhebung, grün = erlaubt/läuft/Daten, rot = verboten,
grau/dunkel = Hardware oder unbeteiligt. Koordinaten zwischen x = -3,45 und 3,45 (höchstens 548 px).
Wörter: Tupel (de, en, es, zh, fr, tr); W(s, wort) legt den Schlüssel selbst an (gleicher deutscher Text = gleicher
Schlüssel). Kleinste Schrift 17 Szenenpixel (GK = 18, TK = 18).
Bauen:  python tools/szenen/cyber_teil2.py [k2name …]
Export: python tools/export_szenen.py --animiert <alle Namen aus SZENEN>
"""
import hashlib
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from szenen_lib import *  # noqa: E402,F403
from szenen_lib import farbig, tt_breite  # noqa: E402,F401
from linux_hilfen import (schritt, EIN, WACHS, ZEICHNE, AUS, BETONE, VER, VERS, DREH, ZU, flach,  # noqa: E402,F401
                          WEISS, BLAU_HELL, ORANGE_HELL, GRUEN_HELL, ROT_HELL, GRAU_HELL, GELB, DUNKEL)

GT, GN, GK = 22, 20, 18           # Beschriftung: Titel, normal, klein (18 = 9,9 px im Artikel)
TT, TK = 20, 18                   # Schreibmaschinenschrift: normal, klein
P2 = "student@labor:~/cyberk2$ "      # Prompt im Übungsverzeichnis des Kapitels (Abschnitt 1.1: cd ~/cyberk2)
PFAD2 = "~/cyberk2"                   # für t.befehl(..., pfad=PFAD2) und t.prompt(PFAD2): sonst kommt "~" zurück
LILA, TUERKIS = "#8b3aa0", "#16768a"
LILA_HELL, TUERKIS_HELL = "#f3e8f6", "#e1f1f4"


# ================================================================== Helfer
def r4(v):
    return round(v, 4)


def W(s, w):
    """Wort in sechs Sprachen (de, en, es, zh, fr, tr); der Schlüssel folgt aus dem deutschen Text."""
    slug = re.sub(r"[^a-z0-9]", "", w[0].lower().replace("ä", "ae").replace("ö", "oe").replace("ü", "ue"))[:14]
    key = "%s_%s" % (slug or "w", hashlib.md5(w[0].encode("utf-8")).hexdigest()[:4])
    return s.tr(key, w[0], w[1], w[2], w[3], fr=w[4], tr=w[5])


def lab(s, w, pos, g=GN, a="center", f=SCHWARZ, roh=None):
    """Beschriftung in sechs Sprachen (w = Tupel) oder sprachfrei (w = str)."""
    t = w if isinstance(w, str) else W(s, w)
    if roh is None:
        return s.text(None, t, (r4(pos[0]), r4(pos[1])), g, a, f)
    return s.text(None, t, (r4(pos[0]), r4(pos[1])), g, a, f, roh=roh)


def tt(s, t, pos, g=TT, a="center", f=SCHWARZ):
    """Schreibmaschinenschrift (Code, Register, Adressen, Ausgaben); in allen Sprachen gleich."""
    return s.text(None, t, (r4(pos[0]), r4(pos[1])), g, a, f, schrift="tt")


def box(s, mitte, b, h, rand=GRAU, fuellung=WEISS, dicke=2, form="round", dash="", deckung=1.0):
    """Kasten; große Flächen (beide Seiten über 1,35) eckig, weil der Eckradius 0,3 · min(b, h) beträgt."""
    if form == "round" and min(b, h) > 1.35:
        form = "rect"
    return s.box("", (r4(mitte[0]), r4(mitte[1])), breite=r4(b), hoehe=r4(h), form=form, farbe=rand, fuellung=fuellung,
                 deckung=deckung, dicke=dicke, dash=dash)


def kasten(s, mitte, b, h, w, rand=GRAU, fuellung=WEISS, g=GK, tf=SCHWARZ, dicke=2, form="round", dash=""):
    """Kasten mit Beschriftung (Tupel oder str); Ergebnis [Kasten, Text]."""
    return [box(s, mitte, b, h, rand, fuellung, dicke, form, dash), lab(s, w, mitte, g, "center", tf)]


def ttkasten(s, mitte, b, h, t, rand=GRAU, fuellung=WEISS, g=TK, tf=SCHWARZ, dicke=2, form="round", dash=""):
    """Kasten mit Schreibmaschinenschrift; Ergebnis [Kasten, Text]."""
    return [box(s, mitte, b, h, rand, fuellung, dicke, form, dash), tt(s, t, mitte, g, "center", tf)]


def pf(s, a, b, farbe=SCHWARZ, dicke=2.5, spitze=0.12, dash="", knick="none", doppelt=False):
    return s.pfeil((r4(a[0]), r4(a[1])), (r4(b[0]), r4(b[1])), knick=knick, farbe=farbe, dicke=dicke, spitze=spitze,
                   dash=dash, doppelt=doppelt)


def linie(s, a, b, farbe=SCHWARZ, dicke=2.5, dash=""):
    return s.linie(None, (r4(a[0]), r4(a[1])), (r4(b[0]), r4(b[1])), farbe=farbe, dicke=dicke, dash=dash)


def haken(s, x, y, g=0.24, farbe=GRUEN, dicke=4):
    """Häkchen (Objekt Mark, kind check)."""
    return s._add("Mark", {"center": [r4(x), r4(y), 0], "kind": "check", "size": g, "color": farbe, "stroke_width": dicke})


def kreuz(s, x, y, g=0.24, farbe=ROT, dicke=4):
    return s.kreuzchen(None, r4(x), r4(y), farbe, g, dicke)


def nummer(s, x, y, n, farbe=DUNKEL, r=0.13):
    """Nummer im gefüllten Kreis (Schritt 1, 2, 5 …); Ergebnis [Kreis, Zahl]."""
    return [s.kreis(None, r4(x), r4(y), r, farbe=farbe, dicke=0, fuellung=farbe, deckung=1.0),
            s.text(None, str(n), (r4(x), r4(y)), 17, "center", WEISS)]


def wand_v(s, x, y_oben, y_unten, luecken=(), farbe=DUNKEL, dicke=9):
    """Senkrechte Grenze von y_oben bis y_unten mit Lücken [(y_a, y_b)] (Türen, y_a > y_b); Ergebnis: Liste."""
    ids, y = [], y_oben
    for ya, yb in sorted(luecken, reverse=True):
        ids.append(linie(s, (x, y), (x, ya), farbe, dicke))
        y = yb
    ids.append(linie(s, (x, y), (x, y_unten), farbe, dicke))
    return ids


def wand_h(s, y, x_links, x_rechts, luecken=(), farbe=DUNKEL, dicke=9):
    """Waagerechte Grenze mit Lücken [(x_a, x_b)] (x_a < x_b); Ergebnis: Liste."""
    ids, x = [], x_links
    for xa, xb in sorted(luecken):
        ids.append(linie(s, (x, y), (xa, y), farbe, dicke))
        x = xb
    ids.append(linie(s, (x, y), (x_rechts, y), farbe, dicke))
    return ids


def schleier(s, mitte, b, h, deckung=0.7):
    """Weißer, halb durchsichtiger Schleier über einem Kasten (beendet, nicht beteiligt)."""
    return s.box("", (r4(mitte[0]), r4(mitte[1])), breite=r4(b), hoehe=r4(h), form="round", farbe=WEISS, fuellung=WEISS,
                 deckung=deckung, dicke=0)


def bogen(s, a, b, h, farbe=SCHWARZ, dicke=2.5, dash="", marke="0.55", spitze=0.12):
    """Bogen von a nach b, h über der Verbindungslinie (h < 0: darunter), Richtungsmarke bei marke."""
    fx = "%s+%s*t" % (r4(a[0]), r4(b[0] - a[0]))
    fy = "%s+%s*t+%s*4*t*(1-t)" % (r4(a[1]), r4(b[1] - a[1]), r4(h))
    return s.weg(None, fx, fy, 0, 1, farbe=farbe, dicke=dicke, pfeile=marke, n=41, dash=dash, spitze=spitze)


def klammer_v(s, x, y_unten, y_oben, farbe=GRAU, t=0.1, dicke=2.5):
    """Senkrechte eckige Klammer, Schenkel nach links (zum Inhalt hin)."""
    return [linie(s, (x - t, y_unten), (x, y_unten), farbe, dicke), linie(s, (x, y_unten), (x, y_oben), farbe, dicke),
            linie(s, (x, y_oben), (x - t, y_oben), farbe, dicke)]


def klammer_h(s, xa, xb, y, unten=True, farbe=GRAU, t=0.07, dicke=2.5):
    """Waagerechte eckige Klammer: unten=True = Schenkel nach oben (Klammer unter dem Inhalt)."""
    d = t if unten else -t
    return [linie(s, (xa, y + d), (xa, y), farbe, dicke), linie(s, (xa, y), (xb, y), farbe, dicke),
            linie(s, (xb, y), (xb, y + d), farbe, dicke)]


# Rechenbilder: Formelhöhe aus den Maßen der gesetzten Formel (Glyphen-Cache des Exports), wie cyber_teil1.py. Beim
# ersten Bauen gilt die Schätzung; nach dem Export ergibt ein zweiter Lauf die richtige Höhe.
_CACHE = Path(__file__).resolve().parent.parent / "tex_glyphen_cache.json"


def _masse(tex):
    """(Breite, Höhe) der gesetzten Formel in Glyph-Einheiten (1000 je em) oder None."""
    de = re.sub(r"(\d)\.(\d+)(?!\d)(?!\s*(?:em|ex|pt|cm|mm|in|mu|px|pc|bp|dd|cc|sp)\b)", r"\1{,}\2", tex)
    try:
        cache = json.loads(_CACHE.read_text(encoding="utf-8"))["glyphs"]
        glyphen = cache.get(de) or cache.get(tex)
    except (OSError, ValueError, KeyError):
        glyphen = None
    if not glyphen:
        return None
    xs, ys = [], []
    for g in glyphen:
        a, b, c, d, e, f = g["m"]
        zahlen = [float(z) for z in re.findall(r"-?\d+(?:\.\d+)?", g["d"])]
        for x, y in zip(zahlen[0::2], zahlen[1::2]):
            xs.append(a * x + c * y + e)
            ys.append(b * x + d * y + f)
    return max(xs) - min(xs), max(ys) - min(ys)


def formel_hoehe(tex, em, schaetzung, spalte=6.8):
    """Höhe der Formel in Szeneneinheiten bei em (Szeneneinheiten je em), höchstens so breit wie spalte."""
    m = _masse(tex)
    if not m:
        return schaetzung
    e = min(em, spalte * 1000 / m[0])
    return round(e * m[1] / 1000, 3)


# ================================================================== Wörter, die mehrere Szenen brauchen
W_PROGRAMM = ("Programm", "program", "programa", "程序", "programme", "program")
W_PROGRAMME = ("Programme", "programs", "programas", "程序", "programmes", "programlar")
W_KERNEL = ("Kernel", "kernel", "kernel", "内核", "noyau", "çekirdek")
W_PROZESSOR = ("Prozessor", "processor", "procesador", "处理器", "processeur", "işlemci")
W_KERN = ("Kern", "core", "núcleo", "核心", "cœur", "işlemci çekirdeği")
W_PROG3 = ("Programm (Stufe 3)", "program (level 3)", "programa (nivel 3)", "程序（第 3 级）", "programme (niveau 3)",
           "program (seviye 3)")
W_KERN0 = ("Kernel (Stufe 0)", "kernel (level 0)", "kernel (nivel 0)", "内核（第 0 级）", "noyau (niveau 0)",
           "çekirdek (seviye 0)")
W_STUFE3 = ("Stufe 3", "level 3", "nivel 3", "第 3 级", "niveau 3", "seviye 3")
W_STUFE0 = ("Stufe 0", "level 0", "nivel 0", "第 0 级", "niveau 0", "seviye 0")
W_BEFEHL = ("Befehl", "instruction", "instrucción", "指令", "instruction", "komut")
W_DATEN = ("Daten", "data", "datos", "数据", "données", "veri")
W_ZEITGEBER = ("Zeitgeber", "timer", "temporizador", "定时器", "temporisateur", "zamanlayıcı")
W_ZGUNTERBR = ("Zeitgeber-Unterbrechung", "timer interrupt", "interrupción del temporizador", "定时器中断",
               "interruption du temporisateur", "zamanlayıcı kesmesi")
W_PRUEFUNG = ("Prüfung", "check", "comprobación", "检查", "contrôle", "denetim")
W_SYSTEMAUFRUF = ("Systemaufruf", "system call", "llamada al sistema", "系统调用", "appel système", "sistem çağrısı")
W_AUSNAHME = ("Ausnahme", "exception", "excepción", "异常", "exception", "istisna")
W_UNTERBRECHUNG = ("Unterbrechung", "interrupt", "interrupción", "中断", "interruption", "kesme")
W_EINSPRUNGSTELLE = ("Einsprungstelle", "entry point", "punto de entrada", "入口点", "point d'entrée", "giriş noktası")
W_EINSPRUNGTABELLE = ("Einsprungtabelle", "entry table", "tabla de entrada", "入口表", "table d'entrée", "giriş tablosu")
W_SCHUTZVERLETZUNG = ("Schutzverletzung", "protection fault", "fallo de protección", "保护错误", "violation de protection",
                      "koruma ihlali")
W_ADRESSE = ("Adresse", "address", "dirección", "地址", "adresse", "adres")
W_ZEIT = ("Zeit", "time", "tiempo", "时间", "temps", "zaman")
W_PA = ("Prozess A", "process A", "proceso A", "进程 A", "processus A", "süreç A")
W_PB = ("Prozess B", "process B", "proceso B", "进程 B", "processus B", "süreç B")
W_STUDENTIN = ("Benutzerin student", "user student", "usuaria student", "用户 student", "utilisatrice student",
               "kullanıcı student")
W_RUECKKEHR = ("Rückkehr", "return", "retorno", "返回", "retour", "geri dönüş")


# ================================================================== Abschnitt 1: Schutzgrenzen und der Referenzmonitor
W_WENIG = ("wenig Rechte", "few rights", "pocos derechos", "权限很少", "peu de droits", "az yetki")
W_KG = ("Kernel und Geräte", "kernel and devices", "kernel y dispositivos", "内核与设备", "noyau et périphériques",
        "çekirdek ve aygıtlar")
W_ALLE = ("alle Rechte", "all rights", "todos los derechos", "全部权限", "tous les droits", "tüm yetkiler")
W_TUER = ("Tür mit Prüfstelle", "door with a checkpoint", "puerta con control", "带检查点的门", "porte avec contrôle",
          "denetim noktalı kapı")
W_DURCH = ("durch die Tür", "through the door", "por la puerta", "穿过门", "par la porte", "kapıdan")
W_VORBEI = ("an der Tür vorbei", "around the door", "evitando la puerta", "绕过门", "en contournant la porte",
            "kapıyı atlayarak")


def k2grenze():
    """Zwei Bereiche (Programm, wenig Rechte | Kernel und Geräte, alle Rechte), dazwischen eine dicke Grenze mit genau
    einer Tür samt Prüfstelle (Häkchen und Kreuz). Pfeil A geht durch die Tür und wird geprüft (Häkchen), Pfeil B
    versucht es an anderer Stelle und prallt ab."""
    s = Szene("cyber/k2grenze", reihenfolge="anlegen")
    bl = box(s, (-1.8, 0), 3.3, 2.6, BLAU, BLAU_HELL, 2)
    br = box(s, (1.8, 0), 3.3, 2.6, ORANGE, ORANGE_HELL, 2)
    titel = [lab(s, W_PROGRAMM, (-3.3, 1.0), GT, "left", BLAU), lab(s, W_WENIG, (-3.3, 0.7), GK, "left", DUNKEL),
             lab(s, W_KG, (3.3, 1.0), GT, "right", ORANGE), lab(s, W_ALLE, (3.3, 0.7), GK, "right", DUNKEL)]
    wand = wand_v(s, 0, 1.3, -1.3, [(0.55, -0.05)])
    tuer = box(s, (0, 0.25), 0.34, 0.6, ORANGE, WEISS, 2.5, "rect")
    h_k, k_k = haken(s, 0, 0.37, 0.13, GRUEN, 3), kreuz(s, 0, 0.12, 0.11, ROT, 3)
    l_tuer = lab(s, W_TUER, (0.28, -0.22), GK, "left", DUNKEL)
    a1 = pf(s, (-2.9, 0.25), (-0.22, 0.25), BLAU, 3, 0.15)
    l_a = lab(s, W_DURCH, (-1.55, 0.44), GK, "center", BLAU)
    a2 = pf(s, (0.22, 0.25), (2.9, 0.25), GRUEN, 3, 0.15)
    hk = haken(s, 0.55, 0.55, 0.26)
    b = pf(s, (-2.9, -0.7), (-0.12, -0.7), ROT, 3, 0.15, DASH)
    l_b = lab(s, W_VORBEI, (-1.55, -0.51), GK, "center", ROT)
    kb = kreuz(s, 0, -0.7, 0.28)
    zur = pf(s, (-0.16, -0.84), (-0.85, -1.1), ROT, 2.5, 0.11)
    schritt(s, EIN([bl, br] + titel + wand + [tuer, h_k, k_k, l_tuer], 0.8))
    s.pause(0.4)
    schritt(s, ZEICHNE(a1, 0.8), EIN(l_a, 0.8))
    schritt(s, BETONE([tuer, h_k], 0.8))
    schritt(s, ZEICHNE(a2, 0.7), WACHS(hk, 0.5))
    s.pause(0.5)
    schritt(s, ZEICHNE(b, 0.8), EIN(l_b, 0.8))
    schritt(s, WACHS(kb, 0.5), ZEICHNE(zur, 0.5))
    s.speichern()


W_OEFFNEN = ("öffnen", "open", "abrir", "打开", "ouvrir", "aç")
W_ABGELEHNT = ("abgelehnt", "denied", "denegado", "被拒绝", "refusé", "reddedildi")
W_KPRUEF = ("Kernel: Rechteprüfung", "kernel: permission check", "kernel: comprobación de permisos", "内核：权限检查",
            "noyau : contrôle des droits", "çekirdek: izin denetimi")
W_SH1 = ("student: nicht Besitzer,", "student: not the owner,", "student: no es la propietaria,", "student：不是所有者，",
         "student : pas propriétaire,", "student: sahibi değil,")
W_SH2 = ("nicht in der Gruppe shadow,", "not in the group shadow,", "no está en el grupo shadow,", "也不在 shadow 组中，",
         "pas dans le groupe shadow,", "shadow grubunda da değil,")
W_SH3 = ("also gelten die letzten drei Zeichen ---", "so the last three characters apply: ---",
         "así que valen los tres últimos caracteres: ---", "所以适用最后三个字符 ---",
         "donc les trois derniers caractères s'appliquent : ---", "bu yüzden son üç karakter geçerli: ---")


def k2shadow():
    """Oben das Terminal (cat /etc/shadow wird getippt). Darunter wandert die Anfrage von cat (student) als Pfeil
    „öffnen“ durch die Tür in den Kernel; dort die Rechte -rw-r----- root shadow, die letzten drei Zeichen --- markiert,
    Erklärung, Kreuz. Der Pfeil kehrt mit „abgelehnt“ zurück; im Terminal Permission denied, dann echo $? -> 1
    (Heftblock 1.3, mitschrift_kap2_b.txt; Rechte aus mitschrift_kap2_c.txt)."""
    s = Szene("cyber/k2shadow", reihenfolge="anlegen")
    t = s.terminal(pos=(-1.955, 2.6), spalten=42, zeilen=5, prompt=P2, groesse=20)
    bl = box(s, (-2.275, 0.0), 2.35, 1.7, BLAU, BLAU_HELL, 2)
    br = box(s, (1.375, 0.0), 4.15, 1.7, ORANGE, ORANGE_HELL, 2)
    l_p = lab(s, W_PROGRAMM, (-3.35, 0.66), GK, "left", BLAU)
    l_k = lab(s, W_KPRUEF, (3.35, 0.66), GK, "right", ORANGE)
    wand = wand_v(s, -0.9, 0.85, -0.85, [(0.57, -0.02)])
    tuer = box(s, (-0.9, 0.275), 0.3, 0.59, ORANGE, WEISS, 2.5, "rect")
    cat = ttkasten(s, (-2.5, 0.32), 0.9, 0.38, "cat", BLAU, WEISS, TT)
    l_st = lab(s, W_STUDENTIN, (-2.5, -0.42), GK, "center", DUNKEL)
    hin = pf(s, (-2.03, 0.36), (-0.6, 0.36), BLAU, 3, 0.13)
    l_hin = lab(s, W_OEFFNEN, (-1.55, 0.52), GK, "center", BLAU)
    g = s.raster("-rw-r----- root shadow", (-0.5, 0.36), groesse=20)
    mk = g.markieren(0, 7, 9, ORANGE, 0.4)
    erkl = [lab(s, W_SH1, (-0.5, 0.0), GK, "left", DUNKEL, roh=True), lab(s, W_SH2, (-0.5, -0.25), GK, "left", DUNKEL, roh=True),
            lab(s, W_SH3, (-0.5, -0.5), GK, "left", DUNKEL, roh=True)]
    kr = kreuz(s, g.xr(21) + 0.3, 0.36, 0.26)
    zurueck = pf(s, (-0.6, 0.12), (-2.03, 0.12), ROT, 3, 0.13)
    l_ab = lab(s, W_ABGELEHNT, (-1.55, -0.06), GK, "center", ROT)
    schritt(s, EIN([t.id, bl, br, l_p, l_k] + wand + [tuer] + cat + [l_st], 0.7))
    s.pause(0.3)
    t.eingabe("cat /etc/shadow")
    schritt(s, ZEICHNE(hin, 0.8), EIN(l_hin, 0.8))
    schritt(s, EIN(g.ids, 0.5))
    schritt(s, EIN([mk] + erkl, 0.7))
    schritt(s, WACHS(kr, 0.5))
    s.pause(0.3)
    schritt(s, ZEICHNE(zurueck, 0.8), EIN(l_ab, 0.8))
    t.schritt("cat: /etc/shadow: Permission denied\n" + P2, dauer=0.6)
    s.pause(0.3)
    t.befehl("echo $?", "1", pfad=PFAD2)
    s.speichern()


W_SUBJ = ("Handelnde", "subjects", "sujetos", "主体", "sujets", "özneler")
W_OBJ = ("Schutzgüter", "protected objects", "objetos protegidos", "受保护对象", "objets protégés", "korunan nesneler")
W_PROZESS = ("Prozess", "process", "proceso", "进程", "processus", "süreç")
W_DATEIEN = ("Dateien", "files", "archivos", "文件", "fichiers", "dosyalar")
W_SPEICHER = ("Speicher", "memory", "memoria", "内存", "mémoire", "bellek")
W_GERAETE = ("Geräte", "devices", "dispositivos", "设备", "périphériques", "aygıtlar")
W_PRUEFER = ("Prüfer", "checker", "verificador", "检查者", "contrôleur", "denetleyici")
W_FALSCH = ("falscher Prüfer", "fake checker", "verificador falso", "冒牌检查者", "faux contrôleur", "sahte denetleyici")
W_SCHILD1 = ("immer aufgerufen:\nkein Weg daran vorbei", "always invoked:\nno way around it",
             "siempre invocado:\nno hay forma de evitarlo", "始终被调用：\n无法绕过", "toujours appelé :\nimpossible à contourner",
             "her zaman çağrılır:\natlatmanın yolu yok")
W_SCHILD2 = ("manipulationssicher:\nniemand tauscht\nden Prüfer aus", "tamper-proof:\nno one can swap\nthe checker",
             "a prueba de manipulación:\nnadie sustituye\nal verificador", "防篡改：\n没有人能\n替换检查者",
             "inviolable :\npersonne ne remplace\nle contrôleur", "kurcalanamaz:\nkimse denetleyiciyi\ndeğiştiremez")
W_SCHILD3 = ("klein genug\nzum Prüfen", "small enough\nto verify", "lo bastante pequeño\npara verificarlo",
             "足够小，\n可以完整检查", "assez petit\npour être vérifié", "doğrulanabilecek\nkadar küçük")


def _zettel(s, x, y):
    """Kurzer Regelzettel: Blatt mit drei Zeilen."""
    return [box(s, (x, y), 0.3, 0.38, GRAU, WEISS, 1.5, "rect")] + \
        [linie(s, (x - 0.09, y + d), (x + 0.09, y + d), GRAU, 1.5) for d in (0.09, 0.0, -0.09)]


def _ordner(s, x, y):
    """Dicker Ordner: breiter Block mit vielen Blattkanten."""
    return [box(s, (x, y), 0.55, 0.42, DUNKEL, GRAU_HELL, 2, "rect")] + \
        [linie(s, (x - 0.2 + 0.05 * k, y - 0.17), (x - 0.2 + 0.05 * k, y + 0.17), GRAU, 1.2) for k in range(9)]


def k2monitor():
    """Tür mit Prüfstelle zwischen Handelnden und Schutzgütern; nacheinander drei Schilder: 1 immer aufgerufen (eine
    Hintertür wird zugemauert), 2 manipulationssicher (ein falscher Prüfer prallt ab), 3 klein genug zum Prüfen
    (kurzer Regelzettel statt dickem Ordner)."""
    s = Szene("cyber/k2monitor", reihenfolge="anlegen")
    bl = box(s, (-1.8, 1.45), 3.3, 2.0, BLAU, BLAU_HELL, 2)
    br = box(s, (1.8, 1.45), 3.3, 2.0, GRAU, GELB, 2)
    titel = [lab(s, W_SUBJ, (-3.3, 2.25), GN, "left", BLAU), lab(s, W_OBJ, (3.3, 2.25), GN, "right", DUNKEL)]
    proz = kasten(s, (-2.6, 1.7), 1.2, 0.34, W_PROZESS, BLAU, WEISS)
    gueter = [kasten(s, (2.45, y), 1.4, 0.32, w, GRAU, WEISS) for y, w in ((1.7, W_DATEIEN), (1.25, W_SPEICHER),
                                                                       (0.8, W_GERAETE))]
    wand = wand_v(s, 0, 2.45, 0.45, [(1.95, 1.45), (1.05, 0.7)])
    pruefer = kasten(s, (0, 1.7), 0.98, 0.44, W_PRUEFER, ORANGE, WEISS, GK, SCHWARZ, 2.5)
    hinter = box(s, (0, 0.875), 0.3, 0.35, GRAU, WEISS, 1.5, "rect", DASH)
    a_in = pf(s, (-2.0, 1.7), (-0.52, 1.7), BLAU, 2.5)
    a_out = pf(s, (0.52, 1.7), (1.73, 1.7), GRUEN, 2.5)
    # 1: Hintertür zugemauert
    weg1 = pf(s, (-1.6, 0.875), (-0.2, 0.875), ROT, 2.5, 0.11, DASH)
    mauer = [box(s, (0, 0.875), 0.26, 0.35, DUNKEL, GRAU, 2, "rect"),
             linie(s, (-0.12, 0.93), (0.12, 0.93), WEISS, 1.5), linie(s, (-0.12, 0.82), (0.12, 0.82), WEISS, 1.5)]
    k1 = kreuz(s, -0.33, 0.875, 0.2)
    n1 = nummer(s, 0.4, 0.875, 1)
    # 2: falscher Prüfer prallt ab
    falsch = kasten(s, (-1.4, 2.18), 1.45, 0.34, W_FALSCH, ROT, WEISS, GK, ROT, 2, "round", DASH)
    a_f = pf(s, (-0.68, 2.12), (-0.42, 1.98), ROT, 2.5, 0.1)
    k2 = kreuz(s, -0.36, 2.07, 0.18)
    n2 = nummer(s, -2.35, 2.18, 2)
    # Schilder
    schilder = []
    for i, (x, w) in enumerate(((-2.3, W_SCHILD1), (0.0, W_SCHILD2), (2.3, W_SCHILD3))):
        rahmen = box(s, (x, -0.4), 2.2, 1.3, ORANGE, WEISS, 2.5)
        ty = -0.15 if i == 2 else -0.4
        schilder.append([rahmen] + nummer(s, x - 0.92, 0.08, i + 1, ORANGE) + [lab(s, w, (x, ty), GK, "center", DUNKEL)])
    zettel, ordner = _zettel(s, 1.9, -0.72), _ordner(s, 2.65, -0.72)
    hz = haken(s, 2.18, -0.72, 0.2)
    ko = kreuz(s, 2.65, -0.72, 0.42, ROT, 3.5)
    schritt(s, EIN([bl, br] + titel + proz + flach(gueter) + wand + pruefer + [hinter], 0.8))
    schritt(s, ZEICHNE([a_in, a_out], 0.8))
    s.pause(0.4)
    schritt(s, EIN(schilder[0], 0.6))
    schritt(s, ZEICHNE(weg1, 0.6))
    schritt(s, WACHS(mauer, 0.6), WACHS(k1, 0.5), EIN(n1, 0.5))
    s.pause(0.5)
    schritt(s, EIN(schilder[1], 0.6))
    schritt(s, EIN(falsch + n2, 0.5))
    schritt(s, ZEICHNE(a_f, 0.4), WACHS(k2, 0.5))
    s.pause(0.5)
    schritt(s, EIN(schilder[2] + zettel + ordner, 0.6))
    schritt(s, WACHS([hz, ko], 0.5))
    s.speichern()


W_START = ("Startkette (Firmware, Bootloader)", "boot chain (firmware, boot loader)", "cadena de arranque (firmware, bootloader)",
           "启动链（固件、引导加载程序）", "chaîne de démarrage (firmware, bootloader)",
           "başlatma zinciri (ürün yazılımı, önyükleyici)")
W_RICHTET = ("richtet ein und schützt", "sets up and protects", "configura y protege", "设置并保护", "configure et protège",
             "kurar ve korur")
W_TCB = ("vertrauenswürdige\nBasis", "trusted\ncomputing base", "base de cómputo\nconfiable", "可信\n计算基",
         "base informatique\nde confiance", "güvenilir\nhesaplama tabanı")
W_GEPRUEFT = ("wird geprüft", "is checked", "se comprueba", "受到检查", "est contrôlé", "denetlenir")


def k2schichten():
    """Vier Schichten von unten: Startkette, Prozessor, Kernel, Programme; Pfeile „richtet ein und schützt“ nach oben;
    Klammer „vertrauenswürdige Basis“ über die unteren drei; Programm -> Kernel „wird geprüft“."""
    s = Szene("cyber/k2schichten", reihenfolge="anlegen")
    xc, b, h = -0.8, 3.9, 0.5
    lagen = ((-1.35, W_START, GRAU, GRAU_HELL, GK), (-0.45, W_PROZESSOR, DUNKEL, GRAU_HELL, GN),
             (0.45, W_KERNEL, ORANGE, ORANGE_HELL, GN), (1.35, W_PROGRAMME, BLAU, BLAU_HELL, GN))
    kaesten = [kasten(s, (xc, y), b, h, w, rand, fill, g, SCHWARZ, 2.5) for y, w, rand, fill, g in lagen]
    pfeile = []
    for i in range(3):
        y0, y1 = lagen[i][0] + h / 2, lagen[i + 1][0] - h / 2
        pfeile.append([pf(s, (-2.35, y0 + 0.02), (-2.35, y1 - 0.02), DUNKEL, 2.5, 0.1),
                       lab(s, W_RICHTET, (-2.2, (y0 + y1) / 2), GK, "left", DUNKEL)])
    kl = klammer_v(s, 1.35, -1.6, 0.7, ORANGE, 0.1, 3)
    l_kl = lab(s, W_TCB, (1.5, -0.45), GN, "left", ORANGE)
    pg = pf(s, (0.6, 1.1), (0.6, 0.72), ORANGE, 3, 0.11)
    l_pg = lab(s, W_GEPRUEFT, (0.75, 0.91), GK, "left", ORANGE)
    schritt(s, EIN(kaesten[0], 0.6))
    for i in range(3):
        schritt(s, ZEICHNE(pfeile[i][0], 0.5), EIN(pfeile[i][1], 0.5), EIN(kaesten[i + 1], 0.6))
    s.pause(0.5)
    schritt(s, ZEICHNE(kl, 0.7), EIN(l_kl, 0.7))
    s.pause(0.4)
    schritt(s, ZEICHNE(pg, 0.6), EIN(l_pg, 0.6))
    s.speichern()


# ================================================================== Abschnitt 2: Code und Daten im selben Speicher
W_VIER = ("ein Wert aus vier Bytes\nbelegt vier Adressen", "a value of four bytes\noccupies four addresses",
          "un valor de cuatro bytes\nocupa cuatro direcciones", "一个四字节的值\n占用四个地址",
          "une valeur de quatre octets\noccupe quatre adresses", "dört baytlık bir değer\ndört adres kaplar")


def k2adressen():
    """Acht Häuser mit den Bytes 2a c3 00 00 2c 01 00 00, darunter die Hausnummern 0x1000 … 0x1007. Ein Zeiger springt
    auf 0x1000 (2a = 2·16 + 10 = 42), dann auf 0x1001 (c3 = 12·16 + 3 = 195); zum Schluss eine Klammer über
    0x1004 … 0x1007: ein Wert aus vier Bytes belegt vier Adressen."""
    s = Szene("cyber/k2adressen", reihenfolge="anlegen")
    bytes_ = ["2a", "c3", "00", "00", "2c", "01", "00", "00"]
    xs = [-2.1 + 0.7 * k for k in range(8)]
    haeuser, werte, adr = [], [], []
    for k, x in enumerate(xs):
        haeuser.append(s.vieleck(None, [(r4(x - 0.29), 0.1), (r4(x + 0.29), 0.1), (r4(x + 0.29), 0.55), (r4(x), 0.8),
                                        (r4(x - 0.29), 0.55)], farbe=WEISS, deckung=1.0, dicke=2, randfarbe=DUNKEL))
        werte.append(tt(s, bytes_[k], (x, 0.32), TT))
        adr.append(tt(s, "0x%x" % (0x1000 + k), (x, -0.12), TK, "center", GRAU))
    zeiger = pf(s, (xs[0], 1.45), (xs[0], 0.9), ORANGE, 3, 0.14)
    z1 = lab(s, "0x1000:   2a = 2·16 + 10 = 42", (-2.4, -0.55), GN, "left", SCHWARZ, roh=True)
    z2 = lab(s, "0x1001:   c3 = 12·16 + 3 = 195", (-2.4, -0.85), GN, "left", SCHWARZ, roh=True)
    kl = klammer_h(s, xs[4] - 0.3, xs[7] + 0.3, 1.0, unten=False, farbe=BLAU)
    l_kl = lab(s, W_VIER, (r4((xs[4] + xs[7]) / 2), 1.33), GK, "center", BLAU)
    schritt(s, EIN(haeuser + werte, 0.7))
    schritt(s, EIN(adr, 0.7))
    s.pause(0.4)
    schritt(s, ZEICHNE(zeiger, 0.5))
    schritt(s, BETONE(werte[0], 0.7), EIN(z1, 0.7))
    s.pause(0.5)
    schritt(s, VER(zeiger, 0.7, 0, 0.6))
    schritt(s, BETONE(werte[1], 0.7), EIN(z2, 0.7))
    s.pause(0.5)
    schritt(s, ZEICHNE(kl, 0.7), EIN(l_kl, 0.7))
    s.speichern()


W_HOLEN = ("holen", "fetch", "buscar", "取出", "charger", "getir")
W_WEITER = ("weitersetzen", "advance", "avanzar", "前移", "avancer", "ilerlet")
W_AUSF = ("ausführen", "execute", "ejecutar", "执行", "exécuter", "yürüt")
W_SPRUNG = ("C: springe nach 0x401000", "C: jump to 0x401000", "C: salta a 0x401000", "C：跳转到 0x401000",
            "C : saute à 0x401000", "C: 0x401000 adresine atla")
W_BEF_A = ("A (5 Byte)", "A (5 bytes)", "A (5 bytes)", "A（5 字节）", "A (5 octets)", "A (5 bayt)")
W_BEF_B = ("B (3 Byte)", "B (3 bytes)", "B (3 bytes)", "B（3 字节）", "B (3 octets)", "B (3 bayt)")
W_BEF_C = ("C (2 Byte)", "C (2 bytes)", "C (2 bytes)", "C（2 字节）", "C (2 octets)", "C (2 bayt)")


def k2zyklus():
    """Speicherstreifen 0x401000 … 0x40100a mit A (5 Byte), B (3), C (2, springt nach 0x401000). Das Register rip zeigt
    0x401000, 0x401005, 0x401008, nach dem Holen von C kurz 0x40100a, dann wieder 0x401000; der Pfeil darunter wandert
    mit. Rechts dreht sich der Kreis holen -> weitersetzen -> ausführen (je Schritt 120°)."""
    s = Szene("cyber/k2zyklus", reihenfolge="anlegen")
    x0, cw, ys, hs = -3.3, 0.6, -0.2, 0.5

    def xc(i):
        return x0 + cw * i
    zellen = [box(s, (xc(i) + cw / 2, ys), cw, hs, HELLGRAU, WEISS, 1.5, "rect") for i in range(10)]
    z10 = box(s, (xc(10) + cw / 2, ys), cw, hs, HELLGRAU, WEISS, 1.5, "rect", DASH)
    befehle = (("A", 0, 5, BLAU, BLAU_HELL, W_BEF_A), ("B", 5, 3, GRUEN, GRUEN_HELL, W_BEF_B),
               ("C", 8, 2, ORANGE, ORANGE_HELL, W_BEF_C))
    kaesten, texte = {}, []
    for n, a, laenge, rand, fill, w in befehle:
        m = (xc(a) + cw * laenge / 2, ys)
        kaesten[n] = box(s, m, cw * laenge - 0.06, hs - 0.06, rand, fill, 2.5)
        texte.append(lab(s, w, m, GK, "center", SCHWARZ))
    ticks = [linie(s, (xc(i), ys - hs / 2 - 0.02), (xc(i), ys - hs / 2 - 0.1), GRAU, 1.5) for i in range(12)]
    adressen = [tt(s, a, (xc(i), -0.66), TK, "left", GRAU) for i, a in ((0, "0x401000"), (5, "0x401005"),
                                                                       (8, "0x401008"), (10, "0x40100a"))]
    sprung = bogen(s, (xc(9), -0.9), (xc(0) + 0.3, -0.9), -0.32, ORANGE, 2.5, DASH, "0.5")
    l_sprung = lab(s, W_SPRUNG, (-0.45, -1.42), GK, "center", ORANGE)
    rip_l = tt(s, "rip", (-3.4, 1.5), TT, "left", ORANGE)
    reg = box(s, (-2.35, 1.5), 1.45, 0.42, ORANGE, ORANGE_HELL, 2.5)
    wert = tt(s, "0x401000", (-2.35, 1.5), TT)
    ziel_x = {"A": xc(0) + 0.3, "B": xc(5) + 0.3, "C": xc(8) + 0.3, "rest": xc(10) + 0.3}

    def zeiger_auf(z):                                     # Pfeil vom Register auf das erste Byte des Ziels
        return pf(s, (-2.35, 1.27), (ziel_x[z], ys + hs / 2 + 0.04), ORANGE, 3, 0.14)
    zeiger = {z: zeiger_auf(z) for z in ("A", "B", "C", "rest")}
    zeiger["A2"] = zeiger_auf("A")
    cx, cy, r = 2.3, 1.45, 0.28
    ring = s.weg(None, "%s+%s*cos(1.5708-t)" % (cx, r), "%s+%s*sin(1.5708-t)" % (cy, r), 0, 6.2832, farbe=DUNKEL,
                 dicke=2.5, pfeile="0.17;0.5;0.83", n=97, spitze=0.09)
    w_h = lab(s, W_HOLEN, (cx, cy + 0.53), GK, "center", DUNKEL)
    w_w = lab(s, W_WEITER, (cx + 0.32, cy - 0.33), GK, "left", DUNKEL)
    w_a = lab(s, W_AUSF, (cx - 0.32, cy - 0.33), GK, "right", DUNKEL)
    schritt(s, EIN(zellen + [z10] + list(kaesten.values()) + texte + ticks + adressen + [rip_l, reg, wert, zeiger["A"],
                                                                                        ring, w_h, w_w, w_a], 0.8))
    s.pause(0.4)

    def drehung():
        return DREH(ring, -120, (cx, cy), 0.6)

    def weiter(neu, alt, ziel, d=0.6, *mehr):
        with s.gleichzeitig():
            schritt(s, BETONE(w_w if ziel != "A2" else w_a, d), drehung(), AUS(zeiger[alt], d * 0.6),
                    ZEICHNE(zeiger[ziel], d), *mehr)
            s.ersetzen(wert, neu, dauer=d)
    schritt(s, BETONE([w_h, kaesten["A"]], 0.6))
    weiter("0x401005", "A", "B")
    schritt(s, BETONE(w_a, 0.6), drehung())
    schritt(s, BETONE([w_h, kaesten["B"]], 0.6), drehung())
    weiter("0x401008", "B", "C")
    schritt(s, BETONE(w_a, 0.6), drehung())
    schritt(s, BETONE([w_h, kaesten["C"]], 0.6), drehung())
    weiter("0x40100a", "C", "rest")
    weiter("0x401000", "rest", "A2", 0.8, ZEICHNE(sprung, 0.8), EIN(l_sprung, 0.8))
    schritt(s, BETONE([w_h, kaesten["A"]], 0.6), drehung())
    s.speichern()


W_LS = ("lesen/schreiben", "read/write", "leer/escribir", "读/写", "lire/écrire", "oku/yaz")
W_C3 = ("dasselbe Byte c3, zwei Rollen", "the same byte c3, two roles", "el mismo byte c3, dos papeles",
        "同一个字节 c3，两种角色", "le même octet c3, deux rôles", "aynı bayt c3, iki rol")


def k2vonneumann():
    """Prozessor mit rip, darunter ein Speicherstreifen b8 2a 00 00 00 c3 | 0a c3 2a 64 (Befehle, als Zahlen gelesen
    Punktestände). Zuerst ohne Farbe; rip zeigt auf die linken Bytes (blau: Befehl), „lesen/schreiben“ auf die rechten
    (grün: Daten); c3 steht in beiden Teilen."""
    s = Szene("cyber/k2vonneumann", reihenfolge="anlegen")
    proz = box(s, (0, 1.55), 3.4, 0.85, DUNKEL, GRAU_HELL, 2.5)
    l_p = lab(s, W_PROZESSOR, (-1.55, 1.78), GN, "left", DUNKEL)
    rip = ttkasten(s, (-0.9, 1.4), 0.75, 0.34, "rip", ORANGE, WEISS, TK)
    x0, cw, y = -3.0, 0.6, 0.0
    bytes_ = ["b8", "2a", "00", "00", "00", "c3", "0a", "c3", "2a", "64"]
    zellen = [box(s, (x0 + cw * (i + 0.5), y), cw, 0.5, HELLGRAU, WEISS, 1.5, "rect") for i in range(10)]
    ov_b = box(s, (-1.2, y), 3.6, 0.5, BLAU, BLAU_HELL, 0, "rect")
    ov_d = box(s, (1.8, y), 2.4, 0.5, GRUEN, GRUEN_HELL, 0, "rect")
    trenn = [linie(s, (x0 + cw * i, y - 0.25), (x0 + cw * i, y + 0.25), HELLGRAU, 1.5) for i in range(1, 10)]
    umriss = box(s, (0, y), 6.0, 0.5, DUNKEL, WEISS, 2, "rect", deckung=0.0)
    texte = [tt(s, b_, (x0 + cw * (i + 0.5), y), TT) for i, b_ in enumerate(bytes_)]
    a_rip = pf(s, (-0.9, 1.22), (-2.7, 0.28), ORANGE, 3, 0.13)
    kl_b = klammer_h(s, -2.97, 0.57, -0.33, unten=True, farbe=BLAU)
    l_b = lab(s, W_BEFEHL, (-1.2, -0.53), GN, "center", BLAU)
    a_rw = pf(s, (0.9, 1.12), (1.8, 0.28), GRUEN, 3, 0.13, doppelt=True)
    l_rw = lab(s, W_LS, (1.48, 0.76), GK, "left", GRUEN)
    kl_d = klammer_h(s, 0.63, 2.97, -0.33, unten=True, farbe=GRUEN)
    l_d = lab(s, W_DATEN, (1.8, -0.53), GN, "center", GRUEN)
    rahmen = [box(s, (x0 + cw * (i + 0.5), y), 0.56, 0.46, ORANGE, WEISS, 3, "round", deckung=0.0) for i in (5, 7)]
    l_c3 = lab(s, W_C3, (0.9, -0.92), GK, "center", ORANGE)
    schritt(s, EIN([proz, l_p] + rip + zellen + trenn + [umriss] + texte, 0.8))
    s.pause(0.5)
    schritt(s, ZEICHNE(a_rip, 0.6))
    schritt(s, EIN([ov_b, l_b], 0.6), ZEICHNE(kl_b, 0.6))
    s.pause(0.4)
    schritt(s, ZEICHNE(a_rw, 0.6), EIN(l_rw, 0.6))
    schritt(s, EIN([ov_d, l_d], 0.6), ZEICHNE(kl_d, 0.6))
    s.pause(0.5)
    schritt(s, EIN(rahmen + [l_c3], 0.6), BETONE([texte[5], texte[7]], 0.8))
    s.speichern()


W_STUECK = ("Speicherstück vom Kernel (4096 Byte)", "piece of memory from the kernel (4096 bytes)",
            "trozo de memoria del kernel (4096 bytes)", "来自内核的一块内存（4096 字节）",
            "morceau de mémoire du noyau (4096 octets)", "çekirdekten bellek parçası (4096 bayt)")
W_SCHREIBEN = ("schreiben (als Daten)", "write (as data)", "escribir (como datos)", "写入（作为数据）",
               "écrire (comme données)", "yaz (veri olarak)")
W_RIPZEIGT = ("rip zeigt auf das Stück", "rip points to the piece", "rip apunta al trozo", "rip 指向这块内存",
              "rip pointe sur le morceau", "rip parçayı gösterir")


def k2datenbefehle():
    """Schritte 1, 2 und 5 von befehl.py: 1 leeres Speicherstück (00), 2 „schreiben (als Daten)“ füllt B8 2A 00 00 00 C3,
    5 rip zeigt auf das erste Byte, die sechs Bytes werden „Befehl“, der Prozessor rechnet: Ergebnis: 42."""
    s = Szene("cyber/k2datenbefehle", reihenfolge="anlegen")
    prog = ttkasten(s, (-2.35, 1.65), 1.7, 0.42, "befehl.py", BLAU, WEISS, TT)
    x0, cw, y = -3.0, 0.55, 0.25
    zellen = [box(s, (x0 + cw * (i + 0.5), y), cw, 0.46, HELLGRAU, WEISS, 1.5, "rect") for i in range(8)]
    rest = box(s, (x0 + cw * 8.5, y), cw, 0.46, HELLGRAU, WEISS, 1.5, "rect", DASH)
    ov = box(s, (x0 + cw * 3, y), cw * 6, 0.46, BLAU, BLAU_HELL, 0, "rect")
    trenn = [linie(s, (x0 + cw * i, y - 0.23), (x0 + cw * i, y + 0.23), HELLGRAU, 1.5) for i in range(1, 8)]
    texte = [tt(s, "00", (x0 + cw * (i + 0.5), y), TT) for i in range(8)]
    punkte = lab(s, "…", (x0 + cw * 8.5, y), GN, "center", GRAU)
    n1, l1 = nummer(s, -0.25, 0.78, 1), lab(s, W_STUECK, (-0.07, 0.78), GK, "left", DUNKEL)
    a_w = pf(s, (-2.35, 1.43), (-1.62, 0.5), BLAU, 3, 0.13)
    n2, l2 = nummer(s, -1.55, 1.1, 2), lab(s, W_SCHREIBEN, (-1.37, 1.1), GK, "left", BLAU)
    proz = kasten(s, (-2.35, -1.15), 1.6, 0.5, W_PROZESSOR, DUNKEL, GRAU_HELL, GK)
    a_rip = pf(s, (x0 + cw / 2, -0.9), (x0 + cw / 2, 0.0), ORANGE, 3, 0.13)
    n5, l5 = nummer(s, -3.22, -0.45, 5), lab(s, W_RIPZEIGT, (-2.6, -0.45), GK, "left", ORANGE)
    l_bef = lab(s, W_BEFEHL, (-0.6, -0.17), GK, "center", BLAU)
    a_erg = pf(s, (-1.53, -1.15), (-0.68, -1.15), GRUEN, 3, 0.12)
    erg = tt(s, "Ergebnis: 42", (-0.58, -1.15), TT, "left", GRUEN)
    schritt(s, EIN(prog, 0.5))
    schritt(s, EIN(zellen + [rest] + trenn + texte + [punkte] + n1 + [l1], 0.7))
    s.pause(0.5)
    schritt(s, ZEICHNE(a_w, 0.7), EIN(n2 + [l2], 0.7))
    with s.gleichzeitig():
        for i, neu in ((0, "B8"), (1, "2A"), (5, "C3")):
            s.ersetzen(texte[i], neu, dauer=0.8)
        schritt(s, BETONE(texte[2:5], 0.8))
    s.pause(0.5)
    schritt(s, EIN(proz, 0.5))
    schritt(s, ZEICHNE(a_rip, 0.7), EIN(n5 + [l5], 0.7))
    schritt(s, EIN([ov, l_bef], 0.6))
    schritt(s, ZEICHNE(a_erg, 0.6), EIN(erg, 0.6))
    s.speichern()


# ================================================================== Abschnitt 3: Privilegstufen und Schutzringe
W_SETZE0 = ("setze Stufe 0", "set level 0", "pon nivel 0", "设为第 0 级", "passe au niveau 0", "seviye 0 yap")
W_UEBERGANG = ("kontrollierter Übergang", "controlled transition", "transición controlada", "受控切换", "passage contrôlé",
               "denetimli geçiş")
W_ST3 = ("Stufe 3: Benutzermodus", "level 3: user mode", "nivel 3: modo usuario", "第 3 级：用户态",
         "niveau 3 : mode utilisateur", "seviye 3: kullanıcı kipi")
W_ST0 = ("Stufe 0: Kernel", "level 0: kernel", "nivel 0: kernel", "第 0 级：内核", "niveau 0 : noyau", "seviye 0: çekirdek")
W_UNTERSTE = ("unterste Bits", "lowest bits", "bits más bajos", "最低两位", "bits de poids faible", "en düşük bitler")


def k2cpl():
    """Prozessor mit dem Register CS, die beiden untersten Bits hervorgehoben: 11 = „Stufe 3: Benutzermodus“. Ein Befehl
    „setze Stufe 0“ prallt ab. Durch die Tür „kontrollierter Übergang“: Bits 00, „Stufe 0: Kernel“, rip zeigt in den
    Kernel; der zweite Übergang führt zurück zu 11."""
    s = Szene("cyber/k2cpl", reihenfolge="anlegen")
    prog = kasten(s, (-2.25, 1.6), 2.2, 0.5, W_PROGRAMM, BLAU, BLAU_HELL, GN)
    kern = kasten(s, (-2.25, -0.95), 2.2, 0.5, W_KERNEL, ORANGE, ORANGE_HELL, GN)
    wand = wand_h(s, 0.33, -3.4, -1.15, [(-3.15, -2.65)])
    tuer = box(s, (-2.9, 0.33), 0.5, 0.2, ORANGE, WEISS, 2, "rect")
    l_tuer = lab(s, W_UEBERGANG, (-2.55, 0.5), GK, "left", DUNKEL)
    proz = box(s, (1.45, 0.3), 3.9, 2.3, DUNKEL, GRAU_HELL, 2.5)
    l_proz = lab(s, W_PROZESSOR, (-0.38, 1.22), GN, "left", DUNKEL)
    cs = tt(s, "CS", (-0.3, 0.7), TT, "left", DUNKEL)
    rest = box(s, (0.75, 0.7), 1.6, 0.42, HELLGRAU, WEISS, 1.5, "rect")
    l_rest = lab(s, "…", (0.75, 0.7), GN, "center", GRAU)
    bitbox = [box(s, (x, 0.7), 0.42, 0.42, ORANGE, ORANGE_HELL, 2, "rect") for x in (1.76, 2.18)]
    bits = [tt(s, "1", (x, 0.7), TT) for x in (1.76, 2.18)]
    l_unt = lab(s, W_UNTERSTE, (1.97, 1.07), GK, "center", ORANGE)
    anzeige = lab(s, W_ST3, (1.45, 0.08), GN, "center", BLAU)
    rip = ttkasten(s, (0.1, -0.5), 0.7, 0.36, "rip", ORANGE, WEISS, TK)
    rip_p = pf(s, (-0.25, -0.4), (-1.12, 1.38), ORANGE, 2.5, 0.11)
    rip_k = pf(s, (-0.25, -0.55), (-1.12, -0.9), ORANGE, 2.5, 0.11)
    rip_p2 = pf(s, (-0.25, -0.4), (-1.12, 1.38), ORANGE, 2.5, 0.11)
    versuch = pf(s, (-1.12, 1.72), (0.48, 1.48), ROT, 2.5, 0.11, DASH)
    l_vers = lab(s, W_SETZE0, (-0.3, 1.88), GK, "center", ROT)
    kr = kreuz(s, 0.55, 1.46, 0.24)
    hin = pf(s, (-3.02, 1.33), (-3.02, -0.68), ORANGE, 3, 0.13)
    zur = pf(s, (-2.78, -0.68), (-2.78, 1.33), BLAU, 3, 0.13)
    schritt(s, EIN(prog + kern + wand + [tuer, l_tuer, proz, l_proz, cs, rest, l_rest] + bitbox + bits +
                   [l_unt, anzeige] + rip + [rip_p], 0.8))
    s.pause(0.5)
    schritt(s, ZEICHNE(versuch, 0.6), EIN(l_vers, 0.6))
    schritt(s, WACHS(kr, 0.4))
    s.pause(0.5)
    with s.gleichzeitig():
        schritt(s, ZEICHNE(hin, 0.9), BETONE(tuer, 0.9), AUS(rip_p, 0.5), ZEICHNE(rip_k, 0.9))
        for b_ in bits:
            s.ersetzen(b_, "0", dauer=0.9)
        s.ersetzen(anzeige, W(s, W_ST0), farbe=ORANGE, dauer=0.9)
    s.pause(0.6)
    with s.gleichzeitig():
        schritt(s, ZEICHNE(zur, 0.9), BETONE(tuer, 0.9), AUS(rip_k, 0.5), ZEICHNE(rip_p2, 0.9))
        for b_ in bits:
            s.ersetzen(b_, "1", dauer=0.9)
        s.ersetzen(anzeige, W(s, W_ST3), farbe=BLAU, dauer=0.9)
    s.speichern()


W_ROOTRECHTE = ("Rechte von root", "root's rights", "derechos de root", "root 权限", "droits de root", "root yetkileri")
W_CS11 = ("CS, unterste Bits: 11 = Stufe 3", "CS, lowest bits: 11 = level 3", "CS, bits más bajos: 11 = nivel 3",
          "CS 最低两位：11 = 第 3 级", "CS, bits de poids faible : 11 = niveau 3", "CS, en düşük bitler: 11 = seviye 3")
W_KCS = ("Kernel: CS 00 = Stufe 0", "kernel: CS 00 = level 0", "kernel: CS 00 = nivel 0", "内核：CS 00 = 第 0 级",
         "noyau : CS 00 = niveau 0", "çekirdek: CS 00 = seviye 0")
W_SHOEFF = ("/etc/shadow öffnen", "open /etc/shadow", "abrir /etc/shadow", "打开 /etc/shadow", "ouvrir /etc/shadow",
            "/etc/shadow aç")
W_ROOTOK = ("root: Prüfung fast\nganz übersprungen", "root: check almost\nentirely skipped",
            "root: comprobación casi\ntotalmente omitida", "root：几乎\n跳过全部检查", "root : contrôle presque\nentièrement sauté",
            "root: denetim neredeyse\ntamamen atlanır")
W_RPRUEF = ("Rechteprüfung", "permission check", "comprobación de permisos", "权限检查", "contrôle des droits",
            "izin denetimi")
W_FUSS1 = ("Benutzer und root: Sache des Kernels", "user and root: the kernel's business", "usuario y root: asunto del kernel",
           "普通用户与 root：由内核决定", "utilisateur et root : affaire du noyau", "kullanıcı ve root: çekirdeğin işi")
W_FUSS2 = ("Stufe 3 und Stufe 0: Sache des Prozessors", "level 3 and level 0: the processor's business",
           "nivel 3 y nivel 0: asunto del procesador", "第 3 级与第 0 级：由处理器决定",
           "niveau 3 et niveau 0 : affaire du processeur", "seviye 3 ve seviye 0: işlemcinin işi")


def k2root():
    """Links cat (student), rechts sudo cat (Rechte von root), beide „CS, unterste Bits: 11 = Stufe 3“; dazwischen der
    Prozessor, unten der Kernel (CS 00 = Stufe 0). Beide fragen „/etc/shadow öffnen“: links Kreuz, rechts Häkchen
    („root: Prüfung fast ganz übersprungen“). Beide versuchen HLT und prallen am Prozessor ab. Fußzeilen: Benutzer und
    root = Sache des Kernels, Stufe 3 und 0 = Sache des Prozessors."""
    s = Szene("cyber/k2root", reihenfolge="anlegen")
    progs = []
    for x, name, w2 in ((-1.75, "cat", W_STUDENTIN), (1.75, "sudo cat", W_ROOTRECHTE)):
        progs += [box(s, (x, 1.65), 3.2, 1.0, BLAU, BLAU_HELL, 2), tt(s, name, (x, 1.95), TT),
                  lab(s, w2, (x, 1.67), GK, "center", DUNKEL), lab(s, W_CS11, (x, 1.38), GK, "center", BLAU)]
    bar = [box(s, ((xa + xb) / 2, 0.55), xb - xa, 0.3, DUNKEL, GRAU_HELL, 2, "rect")
           for xa, xb in ((-3.35, -2.55), (-2.05, 0.95), (1.45, 3.35))]
    tueren = [box(s, (x, 0.55), 0.5, 0.3, ORANGE, WEISS, 2, "rect", deckung=0.0) for x in (-2.3, 1.2)]
    l_proz = lab(s, W_PROZESSOR, (-1.45, 0.55), GK, "center", DUNKEL)
    kern = [box(s, (0, -0.72), 6.7, 1.0, ORANGE, ORANGE_HELL, 2), lab(s, W_KCS, (-3.2, -1.05), GK, "left", ORANGE),
            lab(s, W_RPRUEF, (-0.55, -0.55), GK, "center", DUNKEL)]
    anfr = [pf(s, (x, 1.15), (x, -0.22), BLAU, 3, 0.12) for x in (-2.3, 1.2)]
    l_anfr = [lab(s, W_SHOEFF, (x + 0.15, 0.92), GK, "left", BLAU) for x in (-2.3, 1.2)]
    kr = kreuz(s, -2.3, -0.55, 0.26)
    hk = haken(s, 1.2, -0.55, 0.26)
    l_ok = lab(s, W_ROOTOK, (1.45, -0.55), GK, "left", GRUEN)
    hlt = [pf(s, (x, 1.15), (x, 0.74), ROT, 2.5, 0.1, DASH) for x in (-0.6, 2.9)]
    l_hlt = [tt(s, "HLT", (x + 0.12, 0.95), TK, "left", ROT) for x in (-0.6, 2.9)]
    k_hlt = [kreuz(s, x, 0.76, 0.22) for x in (-0.6, 2.9)]
    fuss = [lab(s, W_FUSS1, (0, -1.55), GN, "center", DUNKEL), lab(s, W_FUSS2, (0, -1.85), GN, "center", DUNKEL)]
    schritt(s, EIN(progs + bar + tueren + [l_proz] + kern, 0.8))
    s.pause(0.5)
    schritt(s, ZEICHNE(anfr, 0.8), EIN(l_anfr, 0.8))
    schritt(s, WACHS([kr, hk], 0.5), EIN(l_ok, 0.5))
    s.pause(0.6)
    schritt(s, ZEICHNE(hlt, 0.6), EIN(l_hlt, 0.6))
    schritt(s, WACHS(k_hlt, 0.5))
    s.pause(0.5)
    schritt(s, EIN(fuss[0], 0.6))
    schritt(s, EIN(fuss[1], 0.6))
    s.speichern()


W_RING3A = ("3: Programme:", "3: programs:", "3: programas:", "3：程序：", "3 : programmes :", "3: programlar:")
W_RING3B = ("Shell, Browser,", "shell, browser,", "shell, navegador,", "shell、浏览器，", "shell, navigateur,",
            "kabuk, tarayıcı,")
W_RING3C = ("auch Programme von root", "also programs run by root", "también programas de root", "以及 root 运行的程序",
            "aussi les programmes de root", "root'un programları da")
W_UNGENUTZT = ("1 und 2: ungenutzt", "1 and 2: unused", "1 y 2: sin usar", "1 和 2：未使用", "1 et 2 : inutilisés",
               "1 ve 2: kullanılmıyor")
W_NURDURCH = ("nur durch kontrollierte\nÜbergänge", "only through controlled\ntransitions",
              "solo mediante transiciones\ncontroladas", "只能通过\n受控切换", "uniquement par des\npassages contrôlés",
              "yalnızca denetimli\ngeçişlerle")


def k2ringe():
    """Vier Ringe 0 (innen) bis 3; Ring 0 „Kernel“ (orange), Ring 3 Programme (blau, auch Programme von root), Ringe 1
    und 2 werden grau („ungenutzt“); Pfeil von außen nach innen „nur durch kontrollierte Übergänge“."""
    s = Szene("cyber/k2ringe", reihenfolge="anlegen")
    cx, cy = -1.55, 0.0
    radien = (1.65, 1.25, 0.88, 0.52)
    farben = (BLAU_HELL, GRAU_HELL, GRAU_HELL, ORANGE_HELL)
    basis, ueber = [], []
    for r, f in zip(radien, farben):
        basis.append(s.kreis(None, cx, cy, r, farbe=DUNKEL, dicke=2, fuellung=WEISS, deckung=1.0))
        ueber.append(s.kreis(None, cx, cy, r, farbe=DUNKEL, dicke=2, fuellung=f, deckung=1.0))
    zahlen = [lab(s, str(n), (cx, cy + y), GN, "center", DUNKEL) for n, y in ((3, 1.45), (2, 1.065), (1, 0.7), (0, 0.27))]
    l_kern = lab(s, W_KERNEL, (cx, cy - 0.08), GK, "center", ORANGE)
    f3 = [linie(s, (cx + 1.188, 0.832), (0.35, 1.0), GRAU, 1.5)] + \
        [lab(s, w, (0.45, y), GK if i else GN, "left", BLAU) for i, (w, y) in enumerate(((W_RING3A, 1.25), (W_RING3B, 1.0),
                                                                                         (W_RING3C, 0.77)))]
    f12 = [linie(s, (cx + 1.055, -0.148), (0.35, -0.05), GRAU, 1.5), linie(s, (cx + 0.685, -0.146), (0.35, -0.05), GRAU, 1.5),
           lab(s, W_UNGENUTZT, (0.45, -0.05), GK, "left", GRAU)]
    pfeil = pf(s, (0.75, -1.45), (cx + 0.426, cy - 0.298), ORANGE, 3, 0.13)
    l_pf = lab(s, W_NURDURCH, (0.85, -1.5), GK, "left", ORANGE)
    schritt(s, EIN(basis + zahlen, 0.8))
    s.pause(0.4)
    schritt(s, EIN([ueber[3], l_kern], 0.6))
    schritt(s, EIN([ueber[0]] + f3, 0.7))
    schritt(s, EIN([ueber[1], ueber[2]] + f12, 0.7))
    s.pause(0.4)
    schritt(s, ZEICHNE(pfeil, 0.8), EIN(l_pf, 0.8))
    s.speichern()


W_SCHICKT = ("schickt SIGSEGV", "sends SIGSEGV", "envía SIGSEGV", "发送 SIGSEGV", "envoie SIGSEGV", "SIGSEGV gönderir")
W_BEENDET = ("Prozess beendet", "process ended", "proceso terminado", "进程已结束", "processus terminé", "süreç sonlandı")


def k2ausnahme():
    """Programm auf Stufe 3 als Befehlsfolge; rip wandert über zwei Befehle zu HLT, HLT wird rot, Pfeil
    „Schutzverletzung“ in den Kernel (Stufe 0), der Kernel schickt SIGSEGV, der Prozess endet. Unten das Terminal mit den
    echten Zeilen (Heftblock 3.5, mitschrift_kap2.txt)."""
    s = Szene("cyber/k2ausnahme", reihenfolge="anlegen")
    t = s.terminal(pos=(-2.49, 0.55), spalten=54, zeilen=5, prompt=P2, groesse=20)
    prog = [box(s, (-2.15, 1.5), 2.5, 1.6, BLAU, BLAU_HELL, 2), lab(s, W_PROG3, (-3.3, 2.12), GK, "left", BLAU)]
    zeilen = []
    for y, w in ((1.78, W_BEFEHL), (1.44, W_BEFEHL), (1.1, None)):
        zeilen.append(box(s, (-1.95, y), 1.6, 0.28, GRAU, WEISS, 1.5, "rect"))
        zeilen.append(lab(s, w, (-1.95, y), GK, "center", DUNKEL) if w else tt(s, "HLT", (-1.95, y), TK))
    rip = [pf(s, (-3.3, 1.78), (-2.8, 1.78), ORANGE, 3, 0.1), tt(s, "rip", (-3.05, 1.93), TK, "center", ORANGE)]
    kern = [box(s, (2.2, 1.5), 2.4, 1.6, ORANGE, ORANGE_HELL, 2), lab(s, W_KERN0, (1.1, 2.12), GK, "left", ORANGE)]
    schickt = lab(s, W_SCHICKT, (2.2, 1.4), GK, "center", DUNKEL)
    rot = box(s, (-1.95, 1.1), 1.72, 0.38, ROT, WEISS, 3, "round", deckung=0.0)
    sv = pf(s, (-1.13, 1.1), (0.98, 1.1), ROT, 3, 0.13)
    l_sv = lab(s, W_SCHUTZVERLETZUNG, (-0.06, 1.26), GK, "center", ROT)
    sig = pf(s, (1.0, 1.75), (-0.88, 1.75), ORANGE, 3, 0.13)
    l_sig = tt(s, "SIGSEGV", (0.06, 1.9), TK, "center", ORANGE)
    veil = schleier(s, (-2.15, 1.5), 2.5, 1.6, 0.72)
    l_end = lab(s, W_BEENDET, (-2.15, 0.82), GN, "center", ROT)          # unter der Befehlsfolge, nicht darüber
    schritt(s, EIN([t.id] + prog + zeilen + rip + kern, 0.8))
    s.pause(0.3)
    t.eingabe("python3 befehl.py anhalten")
    schritt(s, *VERS(rip, 0, -0.34, 0.5))
    schritt(s, *VERS(rip, 0, -0.34, 0.5))
    schritt(s, EIN(rot, 0.6), BETONE(zeilen[5], 0.8))
    schritt(s, ZEICHNE(sv, 0.8), EIN(l_sv, 0.8))
    schritt(s, EIN(schickt, 0.5))
    schritt(s, ZEICHNE(sig, 0.7), EIN(l_sig, 0.7))
    schritt(s, EIN([veil, l_end], 0.6))
    t.schritt("Segmentation fault         python3 befehl.py anhalten\n" + P2, dauer=0.6)
    s.pause(0.3)
    t.befehl("echo $?", "139", pfad=PFAD2)
    s.speichern()


# ================================================================== Abschnitt 4: Der Eintritt in den Kernel
W_LSTARADR = ("Kerneladresse", "kernel address", "dirección del kernel", "内核地址", "adresse du noyau", "çekirdek adresi")
W_BEIMSTART = ("beim Start vom Kernel\neingetragen", "entered by the kernel\nat startup", "registrada por el kernel\nal arrancar",
               "启动时由\n内核写入", "inscrite par le noyau\nau démarrage", "başlangıçta çekirdek\ntarafından yazılır")
W_DIENSTE = ("Tabelle der Dienste", "table of services", "tabla de servicios", "服务表", "table des services",
             "hizmet tablosu")
W_IDT = ("Einsprungtabelle (IDT)", "entry table (IDT)", "tabla de entrada (IDT)", "入口表（IDT）", "table d'entrée (IDT)",
         "giriş tablosu (IDT)")
W_DIV0 = ("Division durch null", "division by zero", "división por cero", "除以零", "division par zéro", "sıfıra bölme")
W_GERAET_MELDET = ("Gerät meldet sich", "a device signals", "un dispositivo avisa", "设备发出信号", "un périphérique signale",
                   "aygıt sinyal verir")
W_ESSC = ("Einsprungstelle für syscall", "entry point for syscall", "punto de entrada de syscall", "syscall 的入口点",
          "point d'entrée de syscall", "syscall giriş noktası")


def k2einsprung():
    """Programm (Stufe 3) legt rax <- 1 und führt syscall aus; der Prozessor springt an die Kerneladresse aus IA32_LSTAR
    („beim Start vom Kernel eingetragen“) auf Stufe 0; dort liest der Kernel rax und schlägt in seiner Tabelle der
    Dienste nach (0 read, 1 write, 2 open, …, 60 exit; Zeile 1 leuchtet). Darunter die Einsprungtabelle IDT."""
    s = Szene("cyber/k2einsprung", reihenfolge="anlegen")
    prog = [box(s, (-2.725, 1.0), 1.45, 1.3, BLAU, BLAU_HELL, 2), lab(s, W_PROGRAMM, (-2.725, 1.45), GK, "center", BLAU),
            lab(s, W_STUFE3, (-2.725, 1.2), GK, "center", GRAU)]
    rax = tt(s, "rax ← 1", (-2.725, 0.85), TK)
    sysc = tt(s, "syscall", (-2.725, 0.56), TK)
    proz = [box(s, (-0.75, 1.0), 1.8, 1.3, DUNKEL, GRAU_HELL, 2), lab(s, W_PROZESSOR, (-0.75, 1.45), GK, "center", DUNKEL)]
    lstar = ttkasten(s, (-0.75, 1.05), 1.5, 0.34, "IA32_LSTAR", DUNKEL, WEISS, TK)
    l_adr = lab(s, W_LSTARADR, (-0.75, 0.7), GK, "center", GRAU)
    notiz = lab(s, W_BEIMSTART, (-0.75, -0.02), GK, "center", GRAU)
    a_sys = pf(s, (-2.0, 0.56), (-1.65, 0.56), BLAU, 2.5, 0.1)
    kern = [box(s, (1.975, 0.25), 2.95, 3.2, ORANGE, ORANGE_HELL, 2), lab(s, W_KERN0, (0.62, 1.68), GK, "left", ORANGE)]
    es = kasten(s, (1.975, 1.33), 2.6, 0.32, W_ESSC, ORANGE, WEISS, GK)
    a_sprung = pf(s, (0.0, 1.05), (0.66, 1.3), ORANGE, 3, 0.11)
    l_rip = tt(s, "rip", (0.33, 1.38), TK, "center", ORANGE)
    l_dienste = lab(s, W_DIENSTE, (0.62, 0.93), GK, "left", DUNKEL)
    g = s.raster(["0   read", "1   write", "2   open", "…", "60  exit"], (0.75, 0.68), groesse=TK, zeilenabstand=1.3)
    mk = g.markieren(1, 0, 8, ORANGE, 0.4)
    a_zeile = pf(s, (2.6, 1.17), (g.xr(8) + 0.06, g.y(1)), ORANGE, 2.5, 0.1)
    l_rax = tt(s, "rax = 1", (2.3, 0.78), TK, "left", DUNKEL)
    idt = [lab(s, W_IDT, (0.62, -0.33), GK, "left", DUNKEL)]
    for y, w in ((-0.63, W_DIV0), (-0.9, W_SCHUTZVERLETZUNG), (-1.17, W_GERAET_MELDET)):
        idt += kasten(s, (1.975, y), 2.6, 0.24, w, GRAU, WEISS, GK, SCHWARZ, 1.5, "rect")
    schritt(s, EIN(prog + [rax, sysc] + proz + lstar + [l_adr] + kern + [l_dienste] + g.ids, 0.8))
    s.pause(0.4)
    schritt(s, BETONE([rax, sysc], 0.7))
    schritt(s, ZEICHNE(a_sys, 0.5))
    schritt(s, BETONE(lstar, 0.7), EIN(notiz, 0.7))
    schritt(s, ZEICHNE(a_sprung, 0.6), EIN([l_rip] + es, 0.6))
    schritt(s, ZEICHNE(a_zeile, 0.6), EIN(l_rax, 0.6))
    schritt(s, EIN(mk, 0.5), BETONE(g.zeile(1), 0.8))
    s.pause(0.5)
    schritt(s, EIN(idt, 0.7))
    s.speichern()


W_NICHTAUSF = ("Befehl nicht ausführbar", "instruction cannot run", "instrucción no ejecutable", "指令无法执行",
               "instruction non exécutable", "komut yürütülemez")
W_TASTATUR = ("Tastatur", "keyboard", "teclado", "键盘", "clavier", "klavye")


def k2dreiwege():
    """Oben das Programm (Stufe 3) und am Rand eine Tastatur, unten der Kernel (Stufe 0). Nacheinander drei Wege durch die
    Einsprungtabelle an eingetragene Stellen: Systemaufruf (syscall), Ausnahme (Befehl nicht ausführbar), Unterbrechung
    (Gerät meldet sich); zum Schluss ein gemeinsamer Pfeil „Rückkehr“."""
    s = Szene("cyber/k2dreiwege", reihenfolge="anlegen")
    prog = [box(s, (-1.1, 1.85), 4.6, 0.8, BLAU, BLAU_HELL, 2), lab(s, W_PROG3, (-3.3, 2.1), GK, "left", BLAU)]
    c_sys = ttkasten(s, (-2.0, 1.68), 1.1, 0.3, "syscall", BLAU, WEISS, TK)
    c_aus = kasten(s, (0.0, 1.68), 2.2, 0.3, W_NICHTAUSF, ROT, WEISS, GK)
    tast = [box(s, (2.425, 1.85), 1.95, 0.8, DUNKEL, GRAU_HELL, 2), lab(s, W_TASTATUR, (2.425, 2.02), GK, "center", DUNKEL),
            lab(s, W_GERAET_MELDET, (2.425, 1.72), GK, "center", GRAU)]
    grenze = linie(s, (-3.4, 1.25), (3.4, 1.25), GRAU, 2, DASH)
    kern = [box(s, (0, -0.17), 6.8, 2.36, ORANGE, ORANGE_HELL, 2), lab(s, W_KERN0, (-3.3, -1.18), GK, "left", ORANGE),
            lab(s, W_EINSPRUNGTABELLE, (-3.3, 0.86), GK, "left", DUNKEL)]
    wege = ((-2.0, 1.8, W_SYSTEMAUFRUF, BLAU, 1.53), (0.0, 2.0, W_AUSNAHME, ROT, 1.53),
            (2.425, 1.95, W_UNTERBRECHUNG, DUNKEL, 1.45))
    zellen, stellen, pfeile = [], [], []
    for x, b, w, f, y0 in wege:
        zellen.append(kasten(s, (x, 0.48), b, 0.4, w, ORANGE, WEISS, GK))
        stellen.append(kasten(s, (x, -0.4), 1.6, 0.32, W_EINSPRUNGSTELLE, ORANGE, WEISS, GK))
        pfeile.append((pf(s, (x, y0), (x, 0.7), f, 3, 0.12), pf(s, (x, 0.27), (x, -0.23), ORANGE, 2.5, 0.1)))
    rueck = pf(s, (1.12, -0.6), (1.12, 1.45), BLAU, 3, 0.13)
    l_rueck = lab(s, W_RUECKKEHR, (1.22, 0.02), GK, "left", BLAU)
    schritt(s, EIN(prog + c_sys + c_aus + tast + [grenze] + kern + flach(zellen), 0.8))
    s.pause(0.4)
    for i in range(3):
        schritt(s, ZEICHNE(pfeile[i][0], 0.6))
        schritt(s, BETONE(zellen[i][0], 0.5))
        schritt(s, ZEICHNE(pfeile[i][1], 0.4), EIN(stellen[i], 0.5))
        s.pause(0.3)
    s.pause(0.3)
    schritt(s, ZEICHNE(rueck, 0.8), EIN(l_rueck, 0.8))
    s.speichern()


W_NAECHSTER = ("nächster Befehl", "next instruction", "siguiente instrucción", "下一条指令", "instruction suivante",
               "sonraki komut")
W_EINTRITT_S = ("Eintritt (syscall)", "entry (syscall)", "entrada (syscall)", "进入（syscall）", "entrée (syscall)",
                "giriş (syscall)")
W_RUECK_S = ("Rückkehr (sysret)", "return (sysret)", "retorno (sysret)", "返回（sysret）", "retour (sysret)",
             "dönüş (sysret)")
W_ADRNAECHST = ("Adresse des nächsten Befehls", "address of the next instruction", "dirección de la siguiente instrucción",
                "下一条指令的地址", "adresse de l'instruction suivante", "sonraki komutun adresi")
W_ZUSTAND = ("Zustandsbits des Programms", "the program's status bits", "bits de estado del programa", "程序的状态位",
             "bits d'état du programme", "programın durum bitleri")
W_STUFE = ("Stufe", "level", "nivel", "级别", "niveau", "seviye")
W_LEGT6 = ("legt 6 in rax", "puts 6 in rax", "pone 6 en rax", "把 6 放入 rax", "met 6 dans rax", "rax'e 6 koyar")
W_ZBR11 = ("Zustandsbits ← r11", "status bits ← r11", "bits de estado ← r11", "状态位 ← r11", "bits d'état ← r11",
           "durum bitleri ← r11")


def k2rueckkehr():
    """Oben das Programm (Stufe 3), rip an syscall; unten der Kernel (Stufe 0); rechts die Register. Eintritt:
    „Adresse des nächsten Befehls“ -> rcx, „Zustandsbits des Programms“ -> r11, Stufe 0. Der Kernel arbeitet (grauer
    Balken), legt 6 in rax. Rückkehr mit sysret: rip <- rcx, Zustandsbits <- r11, Stufe 3, weiter hinter syscall; am Rand
    write(1, …, 6) = 6 wie bei strace."""
    s = Szene("cyber/k2rueckkehr", reihenfolge="anlegen")
    prog = [box(s, (-1.75, 1.6), 3.3, 1.1, BLAU, BLAU_HELL, 2), lab(s, W_PROG3, (-3.3, 1.98), GK, "left", BLAU)]
    zeile_sys = ttkasten(s, (-1.35, 1.6), 2.3, 0.28, "syscall", GRAU, WEISS, TK, SCHWARZ, 1.5, "rect")
    zeile_n = kasten(s, (-1.35, 1.27), 2.3, 0.28, W_NAECHSTER, GRAU, WEISS, GK, SCHWARZ, 1.5, "rect")
    rip = [pf(s, (-3.25, 1.6), (-2.55, 1.6), ORANGE, 3, 0.1), tt(s, "rip", (-2.9, 1.74), TK, "center", ORANGE)]
    kern = [box(s, (-1.75, -0.85), 3.3, 1.05, ORANGE, ORANGE_HELL, 2), lab(s, W_KERN0, (-3.3, -0.5), GK, "left", ORANGE)]
    balken = linie(s, (-3.1, -0.85), (-0.4, -0.85), GRAU, 14)
    l_legt = lab(s, W_LEGT6, (-1.75, -1.15), GK, "center", DUNKEL)
    hin = pf(s, (-2.9, 1.05), (-2.9, -0.325), ORANGE, 3, 0.13)
    l_hin = lab(s, W_EINTRITT_S, (-2.78, 0.52), GK, "left", ORANGE)
    zur = pf(s, (-0.6, -0.325), (-0.6, 1.05), BLAU, 3, 0.13)
    l_zur = lab(s, W_RUECK_S, (-0.72, 0.2), GK, "right", BLAU)
    panel = [box(s, (1.75, 0.35), 3.3, 3.6, DUNKEL, GRAU_HELL, 2), lab(s, W_PROZESSOR, (0.22, 1.98), GN, "left", DUNKEL)]
    werte = {}
    for y, name, wert, f in ((1.5, W_STUFE, "3", BLAU), (1.0, "rcx", "–", GRAU), (0.5, "r11", "–", GRAU),
                             (0.0, "rax", "1", SCHWARZ)):
        schluessel = name if isinstance(name, str) else "stufe"
        panel.append(tt(s, name, (0.2, y), TK, "left", DUNKEL) if isinstance(name, str) else
                     lab(s, name, (0.2, y), GK, "left", DUNKEL))
        panel.append(box(s, (2.04, y), 2.68, 0.36, GRAU, WEISS, 1.5, "rect"))
        werte[schluessel] = lab(s, wert, (0.78, y), GN, "left", f)
        panel.append(werte[schluessel])
    n1 = tt(s, "rip ← rcx", (0.2, -0.55), TK, "left", BLAU)
    n2 = lab(s, W_ZBR11, (0.2, -0.82), GK, "left", BLAU)
    strace = tt(s, "write(1, …, 6) = 6", (0.2, -1.2), TK, "left", DUNKEL)
    schritt(s, EIN(prog + zeile_sys + zeile_n + rip + kern + panel, 0.8))
    s.pause(0.5)
    with s.gleichzeitig():
        schritt(s, ZEICHNE(hin, 0.9), EIN(l_hin, 0.9), BETONE(zeile_n[1], 0.9))
        s.ersetzen(werte["rcx"], W(s, W_ADRNAECHST), farbe=SCHWARZ, dauer=0.9, groesse=GK)
        s.ersetzen(werte["r11"], W(s, W_ZUSTAND), farbe=SCHWARZ, dauer=0.9, groesse=GK)
        s.ersetzen(werte["stufe"], "0", farbe=ORANGE, dauer=0.9)
    schritt(s, ZEICHNE(balken, 1.0))
    with s.gleichzeitig():
        schritt(s, EIN(l_legt, 0.7))
        s.ersetzen(werte["rax"], "6", dauer=0.7)
    s.pause(0.6)
    with s.gleichzeitig():
        schritt(s, ZEICHNE(zur, 0.9), EIN(l_zur, 0.9), *VERS(rip, 0, -0.33, 0.9), EIN([n1, n2], 0.9))
        s.ersetzen(werte["stufe"], "3", farbe=BLAU, dauer=0.9)
    schritt(s, EIN(strace, 0.6))
    s.speichern()


W_TITEL_ARG = ("Der Systemaufruf write(1, Adresse, 6), dreimal gestellt", "The system call write(1, address, 6), made three times",
               "La llamada al sistema write(1, dirección, 6), tres veces", "系统调用 write(1, 地址, 6)，调用三次",
               "L'appel système write(1, adresse, 6), trois fois", "write(1, adres, 6) sistem çağrısı, üç kez")
W_BEREICH = ("Bereichsprüfung", "range check", "comprobación de rango", "范围检查", "contrôle de plage", "aralık denetimi")
W_KOPIEREN = ("Kopieren", "copying", "copia", "复制", "copie", "kopyalama")
W_ERGEBNIS = ("Ergebnis", "result", "resultado", "结果", "résultat", "sonuç")
W_AUSGABE_TUER = ("Ausgabe von tuer.py", "output of tuer.py", "salida de tuer.py", "tuer.py 的输出", "sortie de tuer.py",
                  "tuer.py çıktısı")


def k2argumente():
    """Adressleiste (untere Hälfte Programm bis 0x0000800000000000, obere Hälfte Kernel ab 0xffff800000000000) mit den
    drei Adressen 1, 2, 3. Tabelle der drei Aufrufe write(1, Adresse, 6): eigener Text -> Bereichsprüfung ✓, Kopieren ✓,
    Hallo; Adresse 0 -> ✓, beim Kopieren kein Speicher, EFAULT; 0xffffffff81000000 -> Bereichsprüfung weist ab, EFAULT.
    Darunter die drei echten Ausgabezeilen von tuer.py (Heftblock 4.4, mitschrift_kap2_b.txt)."""
    s = Szene("cyber/k2argumente", reihenfolge="anlegen")
    titel = lab(s, W_TITEL_ARG, (0, 2.45), GK, "center", DUNKEL)
    leiste = [box(s, (-1.775, 1.75), 3.15, 0.36, BLAU, BLAU_HELL, 2, "rect"), lab(s, W_PROGRAMM, (-1.775, 1.75), GK, "center", BLAU),
              box(s, (0, 1.75), 0.4, 0.36, GRAU, WEISS, 1.5, "rect", DASH),
              box(s, (1.775, 1.75), 3.15, 0.36, ORANGE, ORANGE_HELL, 2, "rect"), lab(s, W_KERNEL, (1.775, 1.75), GK, "center", ORANGE),
              tt(s, "0", (-3.35, 1.42), TK, "left", GRAU), tt(s, "0x0000800000000000", (-0.22, 1.42), TK, "right", GRAU),
              tt(s, "0xffff800000000000", (0.22, 1.42), TK, "left", GRAU)]
    kopf = [lab(s, W_ADRESSE, (-3.05, 1.0), GK, "left", GRAU), lab(s, W_BEREICH, (0.65, 1.0), GK, "center", GRAU),
            lab(s, W_KOPIEREN, (1.85, 1.0), GK, "center", GRAU), lab(s, W_ERGEBNIS, (2.9, 1.0), GK, "center", GRAU)]
    faelle = (("0x00007e284d0e27a0", -0.3, True, True, "Hallo"), ("0x0000000000000000", -3.3, True, False, "EFAULT"),
              ("0xffffffff81000000", 3.28, False, None, "EFAULT"))
    reihen = []
    for i, (adr, xm, ber, kop, erg) in enumerate(faelle):
        y = 0.62 - 0.35 * i
        marke = [linie(s, (xm, 1.93), (xm, 2.03), DUNKEL, 2)] + nummer(s, xm, 2.15, i + 1, DUNKEL, 0.11)
        teil = nummer(s, -3.25, y, i + 1, DUNKEL, 0.11) + [tt(s, adr, (-3.05, y), TK, "left")]
        m_ber = haken(s, 0.65, y, 0.2) if ber else kreuz(s, 0.65, y, 0.2)
        m_kop = (haken(s, 1.85, y, 0.2) if kop else kreuz(s, 1.85, y, 0.2)) if kop is not None else \
            lab(s, "–", (1.85, y), GN, "center", GRAU)
        t_erg = tt(s, erg, (2.9, y), TK, "center", GRUEN if erg == "Hallo" else ROT)
        reihen.append((marke + teil, m_ber, [m_kop, t_erg]))
    l_aus = lab(s, W_AUSGABE_TUER, (-3.4, -0.52), GK, "left", GRAU)
    zeilen = ["eigener Text   0x00007e284d0e27a0: Hallo", "Adresse 0      0x0000000000000000: abgelehnt: Bad address",
              "Kerneladresse  0xffffffff81000000: abgelehnt: Bad address"]
    g = s.raster(zeilen, (-3.4, -0.8), groesse=17, zeilenabstand=1.45)
    mk = [g.markieren(0, *g.finde(0, "Hallo"), farbe=GRUEN, deckung=0.3)] + \
        [g.markieren(z, *g.finde(z, "abgelehnt: Bad address"), farbe=ROT, deckung=0.2) for z in (1, 2)]
    schritt(s, EIN([titel] + leiste + kopf, 0.8))
    s.pause(0.4)
    for teil, m_ber, rest in reihen:
        schritt(s, EIN(teil, 0.5))
        schritt(s, WACHS(m_ber, 0.4))
        schritt(s, WACHS(rest, 0.5))
        s.pause(0.3)
    s.pause(0.3)
    schritt(s, EIN([l_aus] + g.ids + mk, 0.7))
    s.speichern()


W_PROGS3 = ("Programme (Stufe 3)", "programs (level 3)", "programas (nivel 3)", "程序（第 3 级）", "programmes (niveau 3)",
            "programlar (seviye 3)")
W_KG0 = ("Kernel und Geräte (Stufe 0)", "kernel and devices (level 0)", "kernel y dispositivos (nivel 0)",
         "内核与设备（第 0 级）", "noyau et périphériques (niveau 0)", "çekirdek ve aygıtlar (seviye 0)")
W_V1 = ("direkt auf\ndas Gerät", "straight to\nthe device", "directo al\ndispositivo", "直接访问\n设备",
        "directement\nau périphérique", "doğrudan\naygıta")
W_V2 = ("mitten in eine\nKernel-Funktion springen", "jump into the middle\nof a kernel function",
        "saltar al medio de\nuna función del kernel", "跳进内核函数\n的中间", "sauter au milieu d'une\nfonction du noyau",
        "bir çekirdek işlevinin\nortasına atla")
W_V3 = ("Einsprungtabelle\numschreiben", "rewrite the\nentry table", "reescribir la\ntabla de entrada", "改写\n入口表",
        "réécrire la\ntable d'entrée", "giriş tablosunu\nyeniden yaz")
W_R1 = ("privilegiert", "privileged", "privilegiado", "特权操作", "privilégié", "ayrıcalıklı")
W_R2 = ("keine eingetragene\nStelle", "not a registered\nentry point", "no es un punto\nregistrado", "不是登记的\n入口点",
        "pas un point\nd'entrée inscrit", "kayıtlı giriş\nnoktası değil")
W_R3 = ("nur Stufe 0", "level 0 only", "solo nivel 0", "仅限第 0 级", "niveau 0 seulement", "yalnızca seviye 0")
W_GERAET = ("Gerät", "device", "dispositivo", "设备", "périphérique", "aygıt")
W_KFUNK = ("Kernel-Funktion", "kernel function", "función del kernel", "内核函数", "fonction du noyau", "çekirdek işlevi")


def k2einzigetuer():
    """Oben Programme (Stufe 3), unten Kernel und Geräte (Stufe 0). Vier Versuche nacheinander: direkt auf das Gerät
    (privilegiert), mitten in eine Kernel-Funktion (keine eingetragene Stelle), Einsprungtabelle umschreiben (nur
    Stufe 0) prallen ab; der Systemaufruf geht durch die Tür und trifft auf die Prüfung. Zum Schluss leuchtet die Tür."""
    s = Szene("cyber/k2einzigetuer", reihenfolge="anlegen")
    xs = (-2.55, -0.85, 0.85, 2.55)
    prog = [box(s, (0, 1.9), 6.8, 1.0, BLAU, BLAU_HELL, 2), lab(s, W_PROGS3, (-3.3, 2.25), GK, "left", BLAU)]
    kern = [box(s, (0, -0.2875), 6.8, 2.075, ORANGE, ORANGE_HELL, 2), lab(s, W_KG0, (-3.3, -1.15), GK, "left", ORANGE)]
    wand = wand_h(s, 0.85, -3.4, 3.4, [(2.2, 2.9)])
    tuer = box(s, (2.55, 0.85), 0.7, 0.18, ORANGE, WEISS, 2.5, "rect")
    ziele = [kasten(s, (x, -0.3), 1.5, 0.42, w, rand, fill, GK) for x, w, rand, fill in
             ((xs[0], W_GERAET, DUNKEL, GRAU_HELL), (xs[1], W_KFUNK, ORANGE, WEISS), (xs[2], W_EINSPRUNGTABELLE, ORANGE, WEISS),
              (xs[3], W_PRUEFUNG, GRUEN, GRUEN_HELL))]
    versuche = []
    for x, w, grund in zip(xs, (W_V1, W_V2, W_V3, W_SYSTEMAUFRUF), (W_R1, W_R2, W_R3, None)):
        l_v = lab(s, w, (x, 1.75), GK, "center", DUNKEL)
        if grund:
            versuche.append((l_v, pf(s, (x, 1.4), (x, 0.95), ROT, 2.5, 0.11, DASH), kreuz(s, x, 0.86, 0.24),
                             lab(s, grund, (x, 0.5), GK, "center", ROT)))
        else:
            versuche.append((l_v, pf(s, (x, 1.4), (x, -0.08), GRUEN, 3, 0.13), None, None))
    schleier_ = [schleier(s, (x, -0.3), 1.56, 0.48, 0.6) for x in xs[:3]]
    glanz = box(s, (2.55, 0.85), 0.95, 0.4, ORANGE, WEISS, 4.5, "round", deckung=0.0)
    schritt(s, EIN(prog + kern + wand + [tuer] + flach(ziele), 0.8))
    s.pause(0.4)
    for l_v, a, k, g_ in versuche[:3]:
        schritt(s, EIN(l_v, 0.5), ZEICHNE(a, 0.6))
        schritt(s, WACHS(k, 0.4), EIN(g_, 0.5))
        s.pause(0.3)
    l_v, a, _, _ = versuche[3]
    schritt(s, EIN(l_v, 0.5), ZEICHNE(a, 0.9))
    schritt(s, BETONE(ziele[3], 0.7))
    s.pause(0.5)
    schritt(s, EIN(schleier_ + [glanz], 0.7), BETONE(tuer, 0.9))
    s.speichern()


# ================================================================== Abschnitt 5: Die Zeitgeber-Unterbrechung
W_ARECHNET = ("A rechnet, ohne Systemaufruf", "A computes, no system call", "A calcula, sin llamada al sistema",
              "A 在计算，不做系统调用", "A calcule, sans appel système", "A hesaplar, sistem çağrısı yok")
W_BRECHNET = ("B rechnet", "B computes", "B calcula", "B 在计算", "B calcule", "B hesaplar")
W_CALL1 = ("Zeit zählen,\nAnteil von A verbraucht?\nnein", "count time,\nA's share used up?\nno",
           "contar el tiempo,\n¿cuota de A agotada?\nno", "计时，\nA 的份额用完了吗？\n没有", "compter le temps,\npart de A épuisée ?\nnon",
           "zamanı say,\nA'nın payı bitti mi?\nhayır")
W_CALL2 = ("ja: Planer wählt B,\nStand von A sichern,\nStand von B laden", "yes: scheduler picks B,\nsave A's state,\nload B's state",
           "sí: el planificador elige B,\nguardar el estado de A,\ncargar el de B", "是：调度器选择 B，\n保存 A 的状态，\n载入 B 的状态",
           "oui : l'ordonnanceur choisit B,\nsauver l'état de A,\ncharger celui de B",
           "evet: planlayıcı B'yi seçer,\nA'nın durumunu kaydet,\nB'ninkini yükle")


def k2zeitleiste():
    """Zeitleiste mit Marken alle 4 ms: A rechnet (blau, ohne Systemaufruf); an der ersten Marke Zeitgeber, kurzer
    Kernel-Abschnitt „Zeit zählen, Anteil von A verbraucht? nein“; an der zweiten „ja“: Planer wählt B, Stand von A
    sichern, B laden, B rechnet (grün). Darunter die Stufe 3, 0, 3, 0, 3."""
    s = Szene("cyber/k2zeitleiste", reihenfolge="anlegen")

    def x(t_ms):
        return r4(-3.0 + 0.57 * t_ms)
    yb = 0.3
    achse = [pf(s, (-3.05, 0), (3.4, 0), GRAU, 2, 0.1), lab(s, W_ZEIT, (3.4, -0.22), GK, "right", GRAU),
             lab(s, W_STUFE, (-3.4, -0.85), GK, "left", DUNKEL)]
    for t_ms, txt_ in ((0, "0"), (4, "4 ms"), (8, "8 ms")):
        achse.append(linie(s, (x(t_ms), 0.07), (x(t_ms), -0.07), GRAU, 2))
        achse.append(lab(s, txt_, (x(t_ms) + 0.06, -0.2), GK, "left", GRAU, roh=True))
    stuecke = [(-3.0, x(4), BLAU), (x(4), x(4) + 0.25, GRAU), (x(4) + 0.25, x(8), BLAU), (x(8), x(8) + 0.5, GRAU),
               (x(8) + 0.5, 3.3, GRUEN)]
    balken = [linie(s, (a, yb), (b, yb), f, 16) for a, b, f in stuecke]
    stufen = [lab(s, "3" if f != GRAU else "0", ((a + b) / 2, -0.85), GN, "center", BLAU if f != GRAU else ORANGE)
              for a, b, f in stuecke]
    l_a1 = lab(s, W_ARECHNET, ((stuecke[0][0] + stuecke[0][1]) / 2, 0.55), GK, "center", BLAU)
    l_a2 = lab(s, "A", ((stuecke[2][0] + stuecke[2][1]) / 2, 0.55), GK, "center", BLAU)
    l_b = lab(s, W_BRECHNET, ((stuecke[4][0] + stuecke[4][1]) / 2, 0.55), GK, "center", GRUEN)
    blitze = [[linie(s, (x(t_ms), -0.38), (x(t_ms), 0.44), ORANGE, 2.5, DASH),
               lab(s, W_ZEITGEBER, (x(t_ms), -0.52), GK, "center", ORANGE)] for t_ms in (4, 8)]
    mitte1, mitte2 = (stuecke[1][0] + stuecke[1][1]) / 2, (stuecke[3][0] + stuecke[3][1]) / 2
    call1 = [lab(s, W_CALL1, (mitte1, 1.42), GK, "center", DUNKEL), linie(s, (mitte1, 1.12), (mitte1, 0.42), GRAU, 1.5)]
    call2 = [lab(s, W_CALL2, (mitte2 + 0.1, 1.42), GK, "center", DUNKEL), linie(s, (mitte2, 1.12), (mitte2, 0.42), GRAU, 1.5)]
    schritt(s, EIN(achse, 0.6))
    s.pause(0.3)
    schritt(s, ZEICHNE(balken[0], 1.0), EIN([l_a1, stufen[0]], 1.0))
    schritt(s, EIN(blitze[0], 0.4))                  # Einblenden und Betonen nie im selben Schritt (fehlt sonst im Endbild)
    schritt(s, ZEICHNE(balken[1], 0.4), EIN(call1 + [stufen[1]], 0.7), BETONE(blitze[0][1], 0.7))
    s.pause(0.6)
    schritt(s, ZEICHNE(balken[2], 0.9), EIN([l_a2, stufen[2]], 0.9))
    schritt(s, EIN(blitze[1], 0.4))
    schritt(s, ZEICHNE(balken[3], 0.5), EIN(call2 + [stufen[3]], 0.7), BETONE(blitze[1][1], 0.7))
    s.pause(0.6)
    schritt(s, ZEICHNE(balken[4], 0.8), EIN([l_b, stufen[4]], 0.8))
    s.speichern()


W_KOOP = ("kooperativ", "cooperative", "cooperativo", "协作式", "coopératif", "işbirlikçi")
W_ERZW = ("erzwungen", "preemptive", "forzado", "抢占式", "préemptif", "zorlamalı")
W_WARTET_IMMER = ("B wartet für immer", "B waits forever", "B espera para siempre", "B 永远在等待", "B attend indéfiniment",
                  "B sonsuza dek bekler")
W_ENDLOS = ("A: Endlosschleife ohne Systemaufruf, B: wartet", "A: endless loop without a system call, B: waiting",
            "A: bucle infinito sin llamada al sistema, B: espera", "A：没有系统调用的死循环，B：等待",
            "A : boucle infinie sans appel système, B : attend", "A: sistem çağrısız sonsuz döngü, B: bekliyor")


def k2kooperativ():
    """Zwei Zeitleisten: oben kooperativ (A läuft bis zum Rand, B grau „wartet für immer“), unten erzwungen (alle 4 ms
    Zeitgeber, A und B wechseln sich ab, beide Balken wachsen)."""
    s = Szene("cyber/k2kooperativ", reihenfolge="anlegen")

    def x(t_ms):
        return r4(-2.6 + 0.369 * t_ms)
    kopf = lab(s, W_ENDLOS, (0, 2.35), GK, "center", DUNKEL)
    oben = [lab(s, W_KOOP, (-3.4, 1.95), GN, "left", DUNKEL), lab(s, "A", (-2.85, 1.6), GN, "center", BLAU),
            lab(s, "B", (-2.85, 1.25), GN, "center", GRUEN)]
    a_oben = linie(s, (-2.6, 1.6), (3.3, 1.6), BLAU, 14)
    b_oben = linie(s, (-2.6, 1.25), (3.3, 1.25), GRAU, 2.5, DASH)
    l_warte = lab(s, W_WARTET_IMMER, (0.35, 1.02), GK, "center", GRAU)
    unten = [lab(s, W_ERZW, (-3.4, 0.6), GN, "left", DUNKEL), lab(s, "A", (-2.85, 0.2), GN, "center", BLAU),
             lab(s, "B", (-2.85, -0.15), GN, "center", GRUEN), pf(s, (-2.6, -0.55), (3.4, -0.55), GRAU, 2, 0.1),
             lab(s, W_ZEIT, (3.4, -0.75), GK, "right", GRAU)]
    for t_ms in (0, 4, 8, 12):
        unten.append(linie(s, (x(t_ms), -0.49), (x(t_ms), -0.61), GRAU, 2))
        unten.append(lab(s, "%d ms" % t_ms if t_ms else "0", (x(t_ms), -0.75), GK, "center", GRAU, roh=True))
    segmente = []
    for k in range(4):
        y, f = (0.2, BLAU) if k % 2 == 0 else (-0.15, GRUEN)
        segmente.append(linie(s, (x(4 * k) + (0.06 if k else 0), y), (x(4 * k + 4) - (0.06 if k < 3 else 0), y), f, 14))
    blitze = [[linie(s, (x(t_ms), 0.4), (x(t_ms), -0.35), ORANGE, 2.5, DASH),
               lab(s, W_ZEITGEBER, (x(t_ms), 0.55), GK, "center", ORANGE)] for t_ms in (4, 8, 12)]
    schritt(s, EIN([kopf] + oben + unten, 0.7))
    s.pause(0.3)
    schritt(s, ZEICHNE(a_oben, 2.0), ZEICHNE(b_oben, 2.0))
    schritt(s, EIN(l_warte, 0.6))
    s.pause(0.5)
    for k in range(4):
        schritt(s, ZEICHNE(segmente[k], 0.7))
        if k < 3:
            schritt(s, EIN(blitze[k], 0.35))
    s.speichern()


W_SCHR1 = ("Zeitgeber stellen/abschalten", "set/switch off the timer", "ajustar/apagar el temporizador", "设置/关闭定时器",
           "régler/arrêter le temporisateur", "zamanlayıcıyı ayarla/kapat")
W_SCHR2 = ("Einsprungstelle für den Zeitgeber", "entry point for the timer", "punto de entrada del temporizador",
           "定时器的入口点", "point d'entrée du temporisateur", "zamanlayıcının giriş noktası")
W_SCHR3 = ("Unterbrechungen sperren (CLI)", "block interrupts (CLI)", "bloquear interrupciones (CLI)", "屏蔽中断（CLI）",
           "bloquer les interruptions (CLI)", "kesmeleri engelle (CLI)")
W_NICHTERLAUBT = ("auf Stufe 3\nnicht erlaubt", "not allowed\nat level 3", "no permitido\nen el nivel 3", "第 3 级\n不允许",
                  "interdit\nau niveau 3", "seviye 3'te\nizin yok")
W_NURSTUFE0 = ("= nur Stufe 0", "= level 0 only", "= solo nivel 0", "= 仅限第 0 级", "= niveau 0 seulement",
               "= yalnızca seviye 0")
W_AUFKERN = ("auf dem Kern läuft:", "running on the core:", "en el núcleo se ejecuta:", "核心上运行的是：",
             "sur le cœur tourne :", "işlemci çekirdeğinde çalışan:")


def k2wecker():
    """Ein Kern mit drei Stellschrauben hinter je einem Schloss (= nur Stufe 0): Zeitgeber stellen/abschalten,
    Einsprungstelle für den Zeitgeber, Unterbrechungen sperren (CLI). Das Programm (Stufe 3) greift nacheinander danach
    und prallt ab. Zum Schluss Zeitgeber-Unterbrechung: auf dem Kern läuft jetzt der Kernel."""
    s = Szene("cyber/k2wecker", reihenfolge="anlegen")
    prog = [box(s, (-2.45, 0.55), 1.8, 0.9, BLAU, BLAU_HELL, 2), lab(s, W_PROGRAMM, (-2.45, 0.7), GN, "center", BLAU),
            lab(s, W_STUFE3, (-2.45, 0.42), GK, "center", GRAU)]
    kern = [box(s, (1.65, 0.3), 3.6, 3.0, DUNKEL, GRAU_HELL, 2), lab(s, W_KERN, (0.0, 1.62), GN, "left", DUNKEL)]
    reihen, schloesser = [], []
    for y, w in ((1.15, W_SCHR1), (0.45, W_SCHR2), (-0.25, W_SCHR3)):
        reihen.append([box(s, (1.95, y), 2.8, 0.5, DUNKEL, WEISS, 2),
                       s.kreis(None, 0.8, y, 0.11, farbe=DUNKEL, dicke=2, fuellung=WEISS, deckung=1.0),
                       linie(s, (0.73, y - 0.06), (0.87, y + 0.06), DUNKEL, 2), lab(s, w, (1.0, y), GK, "left", DUNKEL)])
        schloesser.append(s.schloss((0.27, y), 0.3, False, DUNKEL))
    griffe = [pf(s, (-1.55, y0), (-0.05, y1), ROT, 2.5, 0.11, DASH) for y0, y1 in ((0.8, 1.15), (0.55, 0.45), (0.3, -0.25))]
    kreuze = [kreuz(s, -0.03, y, 0.22) for y in (1.15, 0.45, -0.25)]
    l_nicht = lab(s, W_NICHTERLAUBT, (-2.45, -0.3), GK, "center", ROT)
    legende = [s.schloss((-3.25, -1.0), 0.28, False, DUNKEL), lab(s, W_NURSTUFE0, (-3.05, -1.0), GK, "left", DUNKEL)]
    l_zg = lab(s, W_ZGUNTERBR, (1.65, -0.62), GK, "center", ORANGE)
    l_auf = lab(s, W_AUFKERN, (0.0, -0.95), GK, "left", DUNKEL)
    chip_p = box(s, (2.75, -0.95), 1.2, 0.34, BLAU, BLAU_HELL, 2)
    chip_k = box(s, (2.75, -0.95), 1.2, 0.34, ORANGE, ORANGE_HELL, 2)
    chip_t = lab(s, W_PROGRAMM, (2.75, -0.95), GK, "center", BLAU)
    schritt(s, EIN(prog + kern + flach(reihen) + schloesser + legende + [l_auf, chip_p, chip_t], 0.8))
    s.pause(0.5)
    for i in range(3):
        schritt(s, ZEICHNE(griffe[i], 0.5))
        schritt(s, WACHS(kreuze[i], 0.4), BETONE(schloesser[i], 0.6), *([EIN(l_nicht, 0.5)] if i == 0 else []))
    s.pause(0.6)
    schritt(s, EIN(l_zg, 0.5), BETONE(reihen[0][0], 0.8))
    with s.gleichzeitig():
        schritt(s, EIN(chip_k, 0.7), BETONE(l_zg, 0.7))
        s.ersetzen(chip_t, W(s, W_KERNEL), farbe=ORANGE, dauer=0.7)
    s.speichern()


W_VORHER = ("vorher", "before", "antes", "之前", "avant", "önce")
W_NACHHER = ("nachher", "after", "después", "之后", "après", "sonra")
W_KERN0K = ("Kern 0", "core 0", "núcleo 0", "核心 0", "cœur 0", "çekirdek 0")
W_KERN3K = ("Kern 3", "core 3", "núcleo 3", "核心 3", "cœur 3", "çekirdek 3")
W_RT1 = ("Kern 3 (Endlosschleife), Unterbrechungen je Sekunde:", "core 3 (endless loop), interrupts per second:",
         "núcleo 3 (bucle infinito), interrupciones por segundo:", "核心 3（死循环），每秒中断次数：",
         "cœur 3 (boucle infinie), interruptions par seconde :", "çekirdek 3 (sonsuz döngü), saniyedeki kesme sayısı:")
W_RT2 = ("Kern 0 (fast untätig), Unterbrechungen je Sekunde:", "core 0 (almost idle), interrupts per second:",
         "núcleo 0 (casi inactivo), interrupciones por segundo:", "核心 0（几乎空闲），每秒中断次数：",
         "cœur 0 (presque inactif), interruptions par seconde :", "çekirdek 0 (neredeyse boşta), saniyedeki kesme sayısı:")
W_EINGESTELLT = ("eingestellt: 250 je Sekunde, alle 4 ms", "configured: 250 per second, every 4 ms",
                 "configurado: 250 por segundo, cada 4 ms", "设定值：每秒 250 次，每 4 ms 一次",
                 "réglé : 250 par seconde, toutes les 4 ms", "ayarlı: saniyede 250, her 4 ms'de bir")
F_RT1 = r"\frac{3447-938}{10\,\mathrm{s}}=\frac{2509}{10\,\mathrm{s}}=250.9\,\frac{1}{\mathrm{s}}"
F_RT2 = r"\frac{1570-1447}{10\,\mathrm{s}}=\frac{123}{10\,\mathrm{s}}=12.3\,\frac{1}{\mathrm{s}}"


def k2rtakt():
    """Rechenbild: oben die Zähler vorher (1447 938) und nachher (1570 3447) von Kern 0 und Kern 3 (Heftblock 5.6,
    mitschrift_kap2.txt); dann Kern 3: (3447 − 938)/10 s = 2509/10 s = 250,9 je Sekunde (eingestellt 250, alle 4 ms),
    Kern 0: (1570 − 1447)/10 s = 123/10 s = 12,3 je Sekunde (rechnung_kap2.py)."""
    s = Szene("cyber/k2rtakt", reihenfolge="anlegen")
    g = s.raster(["1447 938", "1570 3447"], (-0.4, 2.0), groesse=28, zeilenabstand=1.5)
    tab = [lab(s, W_VORHER, (-0.55, g.y(0)), GK, "right", GRAU), lab(s, W_NACHHER, (-0.55, g.y(1)), GK, "right", GRAU)]
    k0, _ = g.klammer(0, 0, 3, seite="oben", farbe=BLAU)
    k3, _ = g.klammer(0, 5, 8, seite="oben", farbe=ORANGE)
    yk = r4(g.oben(0) + 0.27)
    tab += [k0, k3, lab(s, W_KERN0K, (g.xr(3), yk), GK, "right", BLAU), lab(s, W_KERN3K, (g.x(5), yk), GK, "left", ORANGE)]
    h1, h2 = formel_hoehe(F_RT1, 0.24, 0.55), formel_hoehe(F_RT2, 0.24, 0.55)
    l1 = lab(s, W_RT1, (-3.4, 1.12), GK, "left", DUNKEL)
    l2 = lab(s, W_RT2, (-3.4, -0.4), GK, "left", DUNKEL)
    notiz = lab(s, W_EINGESTELLT, (0, 0.05), GK, "center", GRAU)
    schritt(s, EIN(g.ids + tab, 0.7))
    s.pause(0.5)
    schritt(s, EIN(l1, 0.5))
    s.formel(F_RT1, mitte=(0, 0.6), hoehe=h1, zeilenweise=True, dauer=1.0)
    schritt(s, EIN(notiz, 0.6))
    s.pause(0.6)
    schritt(s, EIN(l2, 0.5))
    s.formel(F_RT2, mitte=(0, -0.92), hoehe=h2, zeilenweise=True, dauer=1.0)
    s.speichern()


# ================================================================== Abschnitt 6: Der virtuelle Adressraum
W_VIRT = ("virtuelle Adressen", "virtual addresses", "direcciones virtuales", "虚拟地址", "adresses virtuelles", "sanal adresler")
W_PHYS = ("physischer Arbeitsspeicher", "physical main memory", "memoria principal física", "物理内存", "mémoire vive physique",
          "fiziksel ana bellek")
W_OHNE = ("für A und B\nohne Adresse", "no address\nfor A or B", "sin dirección\npara A ni B", "A 和 B\n都没有地址",
          "sans adresse\npour A et B", "A ve B için\nadresi yok")


def k2stadtplan():
    """Prozess A und B, je ein Streifen virtueller Adressen, beide mit 0x7ffd3c2a1f48 markiert (A: 1, B: 2). Rechts der
    physische Arbeitsspeicher: A -> 0x3a1f48, B -> 0x9c0f48; ein drittes Feld ohne Pfeil „für A und B ohne Adresse“."""
    s = Szene("cyber/k2stadtplan", reihenfolge="anlegen")
    kopf = [lab(s, W_VIRT, (-3.4, 2.15), GK, "left", GRAU), lab(s, W_PHYS, (2.25, 2.15), GK, "center", GRAU)]
    streifen, marken, pfeile, phys = [], [], [], []
    speicher = box(s, (2.25, 0.3), 0.6, 3.1, HELLGRAU, WEISS, 1.5, "rect")       # zuerst: liegt unter den Feldern
    for y, w, f, fh, wert, padr, py in ((1.25, W_PA, BLAU, BLAU_HELL, "1", "0x3a1f48", 1.25),
                                        (-0.05, W_PB, GRUEN, GRUEN_HELL, "2", "0x9c0f48", -0.05)):
        streifen += [lab(s, w, (-3.4, y + 0.37), GN, "left", f)] + \
            [box(s, (-3.2 + 0.4 * i, y), 0.4, 0.4, HELLGRAU, WEISS, 1.5, "rect") for i in range(6)]
        marken.append([box(s, (-0.8, y), 0.4, 0.4, f, fh, 2, "rect"), lab(s, wert, (-0.8, y), GN, "center", SCHWARZ),
                       tt(s, "0x7ffd3c2a1f48", (-0.8, y + 0.35), TK, "center", f)])
        pfeile.append(pf(s, (-0.58, y), (1.93, py), f, 3, 0.13))
        phys.append([box(s, (2.25, py), 0.6, 0.4, f, fh, 2, "rect"), lab(s, wert, (2.25, py), GN, "center", SCHWARZ),
                     tt(s, padr, (2.65, py), TK, "left", f)])
    drittes = [box(s, (2.25, -0.85), 0.6, 0.4, GRAU, GRAU_HELL, 2, "rect"), lab(s, W_OHNE, (1.85, -0.85), GK, "right", GRAU)]
    schritt(s, EIN(kopf + streifen + [speicher], 0.7))
    schritt(s, EIN(flach(marken), 0.6))
    s.pause(0.4)
    schritt(s, ZEICHNE(pfeile[0], 0.7), EIN(phys[0], 0.7))
    schritt(s, ZEICHNE(pfeile[1], 0.7), EIN(phys[1], 0.7))
    s.pause(0.5)
    schritt(s, EIN(drittes, 0.6))
    s.speichern()


W_VADR = ("virtuelle Adresse", "virtual address", "dirección virtual", "虚拟地址", "adresse virtuelle", "sanal adres")
W_SNR = ("Seitennummer 0x402", "page number 0x402", "número de página 0x402", "页号 0x402", "numéro de page 0x402",
         "sayfa numarası 0x402")
W_VERS = ("Versatz 0xabc", "offset 0xabc", "desplazamiento 0xabc", "偏移 0xabc", "décalage 0xabc", "ofset 0xabc")
W_STAB = ("Seitentabelle", "page table", "tabla de páginas", "页表", "table des pages", "sayfa tablosu")
W_SEITE = ("Seite", "page", "página", "页", "page", "sayfa")
W_RAHMEN = ("Rahmen", "frame", "marco", "页框", "cadre", "çerçeve")
W_PADR = ("physische Adresse", "physical address", "dirección física", "物理地址", "adresse physique", "fiziksel adres")
W_S403 = ("Seitennummer 0x403", "page number 0x403", "número de página 0x403", "页号 0x403", "numéro de page 0x403",
          "sayfa numarası 0x403")
W_KEINEZEILE = ("keine Zeile", "no row", "ninguna fila", "没有这一行", "aucune ligne", "satır yok")


def k2seitentabelle():
    """0x00402abc zerfällt in Seitennummer 0x402 und Versatz 0xabc; Seitentabelle 0x400 -> 0x1a7, 0x401 -> 0x033,
    0x402 -> 0x2f0; Zeile 0x402 leuchtet, Rahmen 0x2f0 und Versatz ergeben 0x2f0abc. Seitennummer 0x403 findet keine
    Zeile."""
    s = Szene("cyber/k2seitentabelle", reihenfolge="anlegen")
    l_va = lab(s, W_VADR, (-3.4, 2.22), GK, "left", GRAU)
    va = s.raster("0x00402abc", (-3.2, 1.85), groesse=26)
    m_s, m_v = va.markieren(0, 2, 6, BLAU, 0.25), va.markieren(0, 7, 9, ORANGE, 0.3)
    k_s, _ = va.klammer(0, 2, 6, seite="unten", farbe=BLAU)
    k_v, _ = va.klammer(0, 7, 9, seite="unten", farbe=ORANGE)
    l_s = lab(s, W_SNR, (va.xm(2, 6), 1.4), GK, "center", BLAU)
    l_v = lab(s, W_VERS, (va.xr(9) + 0.17, 1.85), GK, "left", ORANGE)
    tb = s.raster(["0x400 → 0x1a7", "0x401 → 0x033", "0x402 → 0x2f0"], (0.95, 1.62), groesse=22, zeilenabstand=1.6)
    m_z = tb.markieren(2, 0, 12, GRUEN, 0.3)
    rahmen_tab = box(s, (1.585, 1.36), 1.51, 0.82, GRAU, WEISS, 2, "rect", deckung=0.0)
    kopf = [lab(s, W_STAB, (1.585, 2.22), GK, "center", DUNKEL), lab(s, W_SEITE, (tb.xm(0, 4), 1.93), GK, "center", GRAU),
            lab(s, W_RAHMEN, (tb.xm(8, 12), 1.93), GK, "center", GRAU)]
    such = pf(s, (-1.88, 1.4), (0.8, tb.y(2) + 0.03), BLAU, 2.5, 0.11)
    a_r = pf(s, (tb.xm(8, 12), 0.97), (tb.xm(8, 12), 0.42), GRUEN, 2.5, 0.11)
    pa = s.raster("0x2f0abc", (tb.x(8), 0.28), groesse=22)
    m_pr, m_pv = pa.markieren(0, 0, 4, GRUEN, 0.3), pa.markieren(0, 5, 7, ORANGE, 0.3)
    l_pa = lab(s, W_PADR, (tb.x(8) - 0.13, 0.28), GK, "right", GRAU)
    anfrage = lab(s, W_S403, (-2.68, 0.6), GK, "center", ROT)
    a_q = pf(s, (-1.88, 0.6), (0.78, 0.78), ROT, 2.5, 0.11, DASH)      # zielt unter die letzte Zeile: dort wäre 0x403
    k_q = kreuz(s, 0.95, 0.8, 0.22)
    l_q = lab(s, W_KEINEZEILE, (-2.68, 0.33), GK, "center", ROT)
    schritt(s, EIN([l_va] + va.ids, 0.6))
    schritt(s, EIN([m_s, m_v, l_s, l_v], 0.7), ZEICHNE([k_s, k_v], 0.7))
    s.pause(0.4)
    schritt(s, EIN(tb.ids + [rahmen_tab] + kopf, 0.6))
    schritt(s, ZEICHNE(such, 0.7))
    schritt(s, EIN(m_z, 0.4), BETONE(tb.zeile(2), 0.8))
    schritt(s, ZEICHNE(a_r, 0.6), EIN(pa.ids + [m_pr, m_pv, l_pa], 0.8))
    s.pause(0.6)
    schritt(s, EIN(anfrage, 0.5))
    schritt(s, ZEICHNE(a_q, 0.7))
    schritt(s, WACHS(k_q, 0.4), EIN(l_q, 0.5))
    s.speichern()


W_TABA = ("Tabelle A", "table A", "tabla A", "页表 A", "table A", "tablo A")
W_TABB = ("Tabelle B", "table B", "tabla B", "页表 B", "table B", "tablo B")
W_SPKERN = ("Speicher des Kernels", "kernel memory", "memoria del kernel", "内核内存", "mémoire du noyau", "çekirdek belleği")
W_PHYS2 = ("physischer Speicher", "physical memory", "memoria física", "物理内存", "mémoire physique", "fiziksel bellek")
W_SDATEN = ("Seite mit Daten", "data page", "página de datos", "数据页", "page de données", "veri sayfası")
W_SCODE = ("Seite mit Code", "code page", "página de código", "代码页", "page de code", "kod sayfası")
W_RA = ("Rahmen von A", "frame of A", "marco de A", "A 的页框", "cadre de A", "A'nın çerçevesi")
W_RB = ("Rahmen von B", "frame of B", "marco de B", "B 的页框", "cadre de B", "B'nin çerçevesi")
W_PCODE = ("Programmcode", "program code", "código del\nprograma", "程序代码", "code du\nprogramme", "program kodu")
W_LAEDT = ("Kernel lädt CR3 neu", "kernel reloads CR3", "el kernel recarga CR3", "内核重新载入 CR3", "le noyau recharge CR3",
           "çekirdek CR3'ü yeniden yükler")
W_NUR0K = ("(nur Stufe 0)", "(level 0 only)", "(solo nivel 0)", "（仅限第 0 级）", "(niveau 0 seulement)", "(yalnızca seviye 0)")
W_BEIDE = ("in beiden Tabellen", "in both tables", "en ambas tablas", "在两个页表中", "dans les deux tables", "iki tabloda da")


def k2mmu():
    """Kern mit MMU und CR3; Seitentabellen A und B im Speicher des Kernels; rechts der physische Speicher. CR3 -> A,
    Zugriff von A landet im Rahmen von A. Zeitgeber, der Kernel lädt CR3 neu (nur Stufe 0) -> B; Zugriff von B an
    derselben Adresse landet im Rahmen von B. Der Rahmen mit Programmcode steht in beiden Tabellen."""
    s = Szene("cyber/k2mmu", reihenfolge="anlegen")
    chip_b = box(s, (-2.4, 1.85), 1.5, 0.38, GRAU, WEISS, 2)
    chip_t = lab(s, W_PA, (-2.4, 1.85), GN, "center", BLAU)
    adr = tt(s, "0x7ffd3c2a1f48", (-2.4, 1.48), TK, "center", DUNKEL)
    kern = [box(s, (-2.4, 0.35), 2.0, 1.4, DUNKEL, GRAU_HELL, 2, "rect"), lab(s, W_KERN, (-3.3, -0.22), GK, "left", DUNKEL)]
    mmu = ttkasten(s, (-2.4, 0.58), 1.1, 0.34, "MMU", DUNKEL, WEISS, TK)
    cr3 = ttkasten(s, (-2.4, 0.08), 1.1, 0.34, "CR3", ORANGE, WEISS, TK)
    zugriff = pf(s, (-2.4, 1.36), (-2.4, 0.77), DUNKEL, 2.5, 0.1)
    region = [box(s, (0.125, -0.1), 2.35, 2.9, GRAU, GRAU_HELL, 1.5), lab(s, W_SPKERN, (0.125, 1.18), GK, "center", GRAU)]
    tabellen = {}
    for name, y, f, w, reihen in (("A", 0.52, BLAU, W_TABA, ((0.5, W_SDATEN), (0.25, W_SCODE))),
                                  ("B", -0.78, GRUEN, W_TABB, ((-0.78, W_SCODE), (-1.03, W_SDATEN)))):
        teile = [box(s, (0.125, y), 2.05, 0.85, f, WEISS, 2), lab(s, w, (0.125, y + 0.28), GK, "center", f)]
        zeilen = {}
        for yz, wz in reihen:
            zeilen[wz[0]] = kasten(s, (0.125, yz), 1.85, 0.22, wz, HELLGRAU, WEISS, GK, SCHWARZ, 1.2, "rect")
            teile += zeilen[wz[0]]
        tabellen[name] = (teile, zeilen)
    phys = [box(s, (2.65, 0.0), 1.35, 2.6, HELLGRAU, WEISS, 1.5, "rect"), lab(s, W_PHYS2, (2.65, 1.5), GK, "center", GRAU),
            kasten(s, (2.65, 0.8), 1.25, 0.42, W_RA, BLAU, BLAU_HELL, GK),
            kasten(s, (2.65, 0.0), 1.25, 0.42, W_PCODE, GRAU, GRAU_HELL, GK),
            kasten(s, (2.65, -0.8), 1.25, 0.42, W_RB, GRUEN, GRUEN_HELL, GK)]
    l_beide = lab(s, W_BEIDE, (2.65, -1.5), GK, "center", GRAU)
    cr3_a = pf(s, (-1.83, 0.12), (-0.93, 0.45), ORANGE, 2.5, 0.1)
    cr3_b = pf(s, (-1.83, 0.04), (-0.93, -0.7), ORANGE, 2.5, 0.1)
    a_daten = pf(s, (1.07, 0.5), (2.0, 0.8), BLAU, 2.5, 0.1)
    a_code = pf(s, (1.07, 0.25), (2.0, 0.06), GRAU, 2.5, 0.1)
    b_code = pf(s, (1.07, -0.78), (2.0, -0.06), GRAU, 2.5, 0.1)
    b_daten = pf(s, (1.07, -1.03), (2.0, -0.8), GRUEN, 2.5, 0.1)
    zg = [lab(s, W_ZGUNTERBR, (-2.4, -0.5), GK, "center", ORANGE), lab(s, W_LAEDT, (-2.4, -0.78), GK, "center", DUNKEL),
          lab(s, W_NUR0K, (-2.4, -1.03), GK, "center", GRAU)]
    schritt(s, EIN([chip_b, chip_t, adr] + kern + mmu + cr3 + region + tabellen["A"][0] + tabellen["B"][0] + flach(phys), 0.8))
    s.pause(0.4)
    schritt(s, ZEICHNE(cr3_a, 0.6))
    schritt(s, ZEICHNE(zugriff, 0.5), BETONE(mmu[0], 0.7))
    schritt(s, BETONE(tabellen["A"][1]["Seite mit Daten"], 0.6), ZEICHNE(a_daten, 0.6))
    schritt(s, BETONE(phys[2], 0.6))
    s.pause(0.6)
    schritt(s, EIN(zg[0], 0.5))
    with s.gleichzeitig():
        schritt(s, AUS(cr3_a, 0.5), ZEICHNE(cr3_b, 0.8), EIN(zg[1:], 0.8), BETONE([cr3[0], zg[0]], 0.8))
        s.ersetzen(chip_t, W(s, W_PB), farbe=GRUEN, dauer=0.8)
    s.pause(0.4)
    schritt(s, BETONE([zugriff, mmu[0]], 0.6))
    schritt(s, BETONE(tabellen["B"][1]["Seite mit Daten"], 0.6), ZEICHNE(b_daten, 0.6))
    schritt(s, BETONE(phys[4], 0.6))
    s.pause(0.6)
    schritt(s, ZEICHNE([a_code, b_code], 0.7), EIN(l_beide, 0.7), BETONE(phys[3], 0.8))
    s.speichern()


W_ZUGRIFF = ("Programm (Stufe 3): Zugriff an einer Adresse", "program (level 3): access to an address",
             "programa (nivel 3): acceso a una dirección", "程序（第 3 级）：访问某个地址",
             "programme (niveau 3) : accès à une adresse", "program (seviye 3): bir adrese erişim")
W_SF = ("Seitenfehler", "page fault", "fallo de página", "缺页异常", "défaut de page", "sayfa hatası")
W_ART = ("Art des Zugriffs", "type of access", "tipo de acceso", "访问类型", "type d'accès", "erişim türü")
W_FRAGE = ("Gehört die Adresse zum Adressraum\nund ist der Zugriff erlaubt?",
           "Does the address belong to the address space,\nand is the access allowed?",
           "¿Pertenece la dirección al espacio de direcciones\ny está permitido el acceso?", "该地址属于地址空间吗？\n这种访问被允许吗？",
           "L'adresse appartient-elle à l'espace d'adressage\net l'accès est-il autorisé ?",
           "Adres, adres alanına ait mi\nve erişime izin var mı?")
W_JA = ("ja, Seite nur\nnicht geladen", "yes, page just\nnot loaded", "sí, la página solo\nno está cargada",
        "是，只是页面\n尚未载入", "oui, page juste\nnon chargée", "evet, sayfa yalnızca\nyüklenmemiş")
W_NEIN = ("nein", "no", "no", "否", "non", "hayır")
W_JA3 = ("Seite holen\nEintrag setzen\nBefehl wiederholen", "fetch the page\nset the entry\nrepeat the instruction",
         "traer la página\nescribir la entrada\nrepetir la instrucción", "取回页面\n写入表项\n重新执行指令",
         "charger la page\nécrire l'entrée\nrépéter l'instruction", "sayfayı getir\ngirdiyi yaz\nkomutu yinele")
W_WEITER2 = ("Programm läuft weiter", "program keeps running", "el programa sigue", "程序继续运行", "le programme continue",
             "program çalışmaya devam eder")
W_ENDE139 = ("Prozess endet, Status 139", "process ends, status 139", "el proceso termina, estado 139", "进程结束，状态 139",
             "le processus se termine, statut 139", "süreç biter, durum 139")


def k2seitenfehler():
    """Zugriff -> Seitenfehler (mit Adresse und Art des Zugriffs) auf Stufe 0 in den Kernel; Frage „Gehört die Adresse
    zum Adressraum und ist der Zugriff erlaubt?“; ja (Seite nur nicht geladen): holen, eintragen, wiederholen, Programm
    läuft weiter; nein: SIGSEGV, Prozess endet, Status 139."""
    s = Szene("cyber/k2seitenfehler", reihenfolge="anlegen")
    prog = kasten(s, (0, 2.15), 4.6, 0.42, W_ZUGRIFF, BLAU, BLAU_HELL, GK)
    sf = pf(s, (0, 1.93), (0, 1.2), ROT, 3, 0.13)
    l_sf = lab(s, W_SF, (0.15, 1.6), GN, "left", ROT)
    angaben = kasten(s, (-1.25, 1.72), 1.75, 0.28, W_ADRESSE, GRAU, WEISS) + kasten(s, (-1.25, 1.41), 1.75, 0.28, W_ART,
                                                                                    GRAU, WEISS)
    kern = [box(s, (0, -0.04), 6.8, 2.42, ORANGE, ORANGE_HELL, 2), lab(s, W_KERN0, (-3.3, -1.1), GK, "left", ORANGE)]
    frage = kasten(s, (0, 0.75), 4.0, 0.62, W_FRAGE, ORANGE, WEISS, GK)
    a_ja = pf(s, (-1.0, 0.44), (-1.6, -0.08), GRUEN, 2.5, 0.11)
    l_ja = lab(s, W_JA, (-1.55, 0.25), GK, "right", GRUEN)
    ja_box = kasten(s, (-1.85, -0.5), 2.6, 0.8, W_JA3, GRUEN, WEISS, GK)
    a_ja2 = pf(s, (-1.85, -0.9), (-1.85, -1.48), GRUEN, 2.5, 0.11)
    l_ja2 = lab(s, W_WEITER2, (-1.85, -1.68), GN, "center", GRUEN)
    a_nein = pf(s, (1.0, 0.44), (1.6, -0.12), ROT, 2.5, 0.11)
    l_nein = lab(s, W_NEIN, (1.5, 0.25), GK, "left", ROT)
    sig = ttkasten(s, (1.85, -0.3), 1.3, 0.34, "SIGSEGV", ROT, ROT_HELL, TK)
    a_nein2 = pf(s, (1.85, -0.47), (1.85, -1.48), ROT, 2.5, 0.11)
    l_nein2 = lab(s, W_ENDE139, (1.85, -1.68), GN, "center", ROT)
    schritt(s, EIN(prog, 0.5))
    schritt(s, ZEICHNE(sf, 0.7), EIN([l_sf] + angaben, 0.7))
    schritt(s, EIN(kern + frage, 0.6))
    s.pause(0.6)
    schritt(s, ZEICHNE(a_ja, 0.5), EIN(l_ja, 0.5))
    schritt(s, EIN(ja_box, 0.7))
    schritt(s, ZEICHNE(a_ja2, 0.5), EIN(l_ja2, 0.5))
    s.pause(0.6)
    schritt(s, ZEICHNE(a_nein, 0.5), EIN(l_nein, 0.5))
    schritt(s, EIN(sig, 0.5))
    schritt(s, ZEICHNE(a_nein2, 0.5), EIN(l_nein2, 0.5))
    s.speichern()


W_STUFEN = (("Stufe 4", "level 4", "nivel 4", "第 4 级", "niveau 4", "seviye 4"),
            ("Stufe 3", "level 3", "nivel 3", "第 3 级", "niveau 3", "seviye 3"),
            ("Stufe 2", "level 2", "nivel 2", "第 2 级", "niveau 2", "seviye 2"),
            ("Stufe 1", "level 1", "nivel 1", "第 1 级", "niveau 1", "seviye 1"))
W_VERSATZ = ("Versatz", "offset", "desplazamiento", "偏移", "décalage", "ofset")
W_EINTRAG = ("Eintrag", "entry", "entrada", "表项", "entrée", "girdi")
W_SRAHMEN = ("Seitenrahmen", "page\nframe", "marco de\npágina", "页框", "cadre de\npage", "sayfa\nçerçevesi")
F_RADR = (r"\begin{aligned}"
          r"255\cdot2^{39}&={}&140\,187\,732\,541\,440\\"
          r"+\;500\cdot2^{30}&={}&536\,870\,912\,000\\"
          r"+\;481\cdot2^{21}&={}&1\,008\,730\,112\\"
          r"+\;161\cdot2^{12}&={}&659\,456\\"
          r"+\;3912&={}&3\,912\\"
          r"&={}&140\,725\,612\,846\,920\\"
          r"&={}&\mathtt{0x7ffd3c2a1f48}"
          r"\end{aligned}")


def k2radresse():
    """Rechenbild: 0x00007ffd3c2a1f48, die 48 Bit in fünf farbigen Gruppen 9|9|9|9|12 mit den Werten 255, 500, 481, 161,
    3912; Rückrechnung Zeile für Zeile (Summanden aus rechnung_kap2.py) bis 140 725 612 846 920 = 0x7ffd3c2a1f48; zum
    Schluss der Weg CR3 -> Eintrag 255 -> 500 -> 481 -> 161 -> Seitenrahmen, plus Versatz."""
    s = Szene("cyber/k2radresse", reihenfolge="anlegen")
    adr = s.raster("0x00007ffd3c2a1f48", (0, 2.5), groesse=24, ausrichtung="mitte")
    bits = s.raster("011111111 111110100 111100001 010100001 111101001000", (0, 2.08), groesse=20, ausrichtung="mitte")
    gruppen = ((0, 8, BLAU, BLAU_HELL, "255"), (10, 18, GRUEN, GRUEN_HELL, "500"), (20, 28, ORANGE, ORANGE_HELL, "481"),
               (30, 38, LILA, LILA_HELL, "161"), (40, 51, TUERKIS, TUERKIS_HELL, "3912"))
    teile = []
    for i, (a, b, f, fh, wert) in enumerate(gruppen):
        mk = bits.markieren(0, a, b, f, 0.22)
        k, t = bits.klammer(0, a, b, wert, seite="unten", farbe=f, groesse=GK, schrift="tt")
        w = W_STUFEN[i] if i < 4 else W_VERSATZ
        teile.append([mk, k, t, lab(s, w, (bits.xm(a, b), 1.5), GK, "center", f)])
    h = formel_hoehe(F_RADR, 0.2, 1.9)
    ym = r4(1.3 - h / 2)
    yk = -1.25 if ym - h / 2 > -0.8 else r4(ym - h / 2 - 0.45)
    xs = [-2.875 + 1.15 * k for k in range(6)]
    kette = [ttkasten(s, (xs[0], yk), 0.9, 0.55, "CR3", ORANGE, ORANGE_HELL, TT)]
    for k, (a, b, f, fh, wert) in enumerate(gruppen[:4]):
        kette.append([box(s, (xs[k + 1], yk), 0.9, 0.55, f, fh, 2), lab(s, W_EINTRAG, (xs[k + 1], yk + 0.12), GK, "center", DUNKEL),
                      tt(s, wert, (xs[k + 1], yk - 0.13), TK, "center", f)])
    kette.append(kasten(s, (xs[5], yk), 0.95, 0.55, W_SRAHMEN, TUERKIS, TUERKIS_HELL, GK))
    unter = [lab(s, W_STUFEN[k], (xs[k + 1], yk - 0.45), GK, "center", gruppen[k][2]) for k in range(4)] + \
        [lab(s, "+ 3912", (xs[5], yk - 0.45), GK, "center", TUERKIS)]
    pfeile = [pf(s, (xs[k] + 0.46, yk), (xs[k + 1] - 0.46, yk), DUNKEL, 2.5, 0.09) for k in range(5)]
    schritt(s, EIN(adr.ids, 0.6))
    schritt(s, EIN(bits.ids, 0.6))
    for tl in teile:
        schritt(s, EIN([tl[0], tl[2], tl[3]], 0.5), ZEICHNE(tl[1], 0.5))
    s.pause(0.5)
    s.formel(F_RADR, mitte=(0.2, ym), hoehe=h, zeilenweise=True, dauer=4.9)
    s.pause(0.5)
    schritt(s, EIN(kette[0], 0.4))
    for k in range(5):
        schritt(s, ZEICHNE(pfeile[k], 0.3), EIN(kette[k + 1] + [unter[k]], 0.4))
    s.speichern()


# ================================================================== Phase 2b-2: Helfer für die Abschnitte 7–10
def schalter(s, x, y, an, b=0.4, h=0.2):
    """Kippschalter: graue Bahn, darüber grüne Bahn (sichtbar = an), weißer Knopf (links aus, rechts an).
    Ergebnis (grau, gruen, knopf, weg): umschalten = grüne Bahn ein-/ausblenden und Knopf um ±weg verschieben."""
    grau = box(s, (x, y), b, h, GRAU, GRAU_HELL, 1.5)
    gruen = box(s, (x, y), b, h, GRUEN, GRUEN, 1.5)
    weg = r4(b - h)
    knopf = s.kreis(None, r4(x + (weg / 2 if an else -weg / 2)), r4(y), r4(h / 2 - 0.035), farbe=DUNKEL, dicke=1.5,
                    fuellung=WEISS, deckung=1.0)
    return grau, gruen, knopf, weg


def stift(s, spitze, laenge=0.55, breite=0.11, winkel=150):
    """Bleistift als Vieleck: Spitze bei spitze, Schaft in Richtung winkel (Grad)."""
    import math
    ux, uy = math.cos(math.radians(winkel)), math.sin(math.radians(winkel))
    nx, ny = -uy * breite / 2, ux * breite / 2
    x, y = spitze
    p = [(x, y), (x + 0.14 * ux + nx, y + 0.14 * uy + ny), (x + laenge * ux + nx, y + laenge * uy + ny),
         (x + laenge * ux - nx, y + laenge * uy - ny), (x + 0.14 * ux - nx, y + 0.14 * uy - ny)]
    return s.vieleck(None, [(r4(a), r4(b)) for a, b in p], GELB, 1.0, 2, DUNKEL)


def schluessel_bild(s, x, y, farbe=ORANGE, g=1.0):
    """Kleiner Schlüssel (Ring links, Bart rechts) um (x, y); Ergebnis: Liste der ids."""
    return [s.kreis(None, r4(x - 0.16 * g), r4(y), r4(0.08 * g), farbe=farbe, dicke=3, fuellung=WEISS, deckung=1.0),
            linie(s, (x - 0.08 * g, y), (x + 0.2 * g, y), farbe, 3),
            linie(s, (x + 0.12 * g, y), (x + 0.12 * g, y - 0.07 * g), farbe, 3),
            linie(s, (x + 0.19 * g, y), (x + 0.19 * g, y - 0.07 * g), farbe, 3)]


def siegel(s, x, y, t="KEK", r=0.17, farbe=ORANGE):
    """Rundes Siegel mit kurzer Aufschrift (Schreibmaschinenschrift); Ergebnis [Kreis, Text]."""
    return [s.kreis(None, r4(x), r4(y), r, farbe=farbe, dicke=2, fuellung=ORANGE_HELL, deckung=1.0),
            tt(s, t, (x, y), 17, "center", farbe)]


# ================================================================== Abschnitt 7: Seitenrechte
W_BIT0 = ("Bit 0, P: vorhanden", "bit 0, P: present", "bit 0, P: presente", "第 0 位，P：存在", "bit 0, P : présente",
          "bit 0, P: mevcut")
W_BIT1 = ("Bit 1, R/W: schreibbar", "bit 1, R/W: writable", "bit 1, R/W: escribible", "第 1 位，R/W：可写",
          "bit 1, R/W : inscriptible", "bit 1, R/W: yazılabilir")
W_BIT2 = ("Bit 2, U/S: für Programme zugänglich", "bit 2, U/S: accessible to programs",
          "bit 2, U/S: accesible a los programas", "第 2 位，U/S：程序可访问", "bit 2, U/S : accessible aux programmes",
          "bit 2, U/S: programlara açık")
W_BIT63 = ("Bit 63, XD: nicht ausführbar", "bit 63, XD: not executable", "bit 63, XD: no ejecutable", "第 63 位，XD：不可执行",
           "bit 63, XD : non exécutable", "bit 63, XD: çalıştırılamaz")
W_NRAHMEN = ("Nummer des Seitenrahmens", "number of the page frame", "número del marco de página", "页框号",
             "numéro du cadre de page", "sayfa çerçevesinin numarası")
W_DEUTUNG = ("Daten eines Programms:\nvorhanden, schreibbar, für Programme, nicht ausführbar",
             "data of a program:\npresent, writable, accessible to programs, not executable",
             "datos de un programa:\npresente, escribible, accesible a los programas, no ejecutable",
             "程序的数据：\n存在、可写、程序可访问、不可执行",
             "données d'un programme :\nprésente, inscriptible, accessible aux programmes, non exécutable",
             "bir programın verisi:\nmevcut, yazılabilir, programlara açık, çalıştırılamaz")


def k2eintrag():
    """Ein Seitentabelleneintrag als Leiste mit 64 Feldern (Bit 63 links, Bit 0 rechts). Nacheinander leuchten Bit 0 (P),
    Bit 1 (R/W), Bit 2 (U/S) und Bit 63 (XD) mit Beschriftung auf, dann der Bereich der Rahmennummer (Bits 12–51).
    Dann der Beispielwert 0x800000000a3b5067: Die Bits füllen die Felder, die Hexziffern stehen unter ihren vier Bits,
    die Rahmennummer 0xa3b5 und die Deutung erscheinen (Beispiel in 7.1)."""
    s = Szene("cyber/k2eintrag", reihenfolge="anlegen")
    wert = 0x800000000a3b5067
    z = tt_breite(TT, 1)
    x0 = -32 * z
    yb, hb = 1.0, 0.3
    leiste = box(s, (0, yb), 64 * z, hb, DUNKEL, WEISS, 1.8, "rect")
    trenn = [linie(s, (x0 + k * z, yb - hb / 2), (x0 + k * z, yb + hb / 2), DUNKEL if k % 4 == 0 else HELLGRAU,
                   1.6 if k % 4 == 0 else 1) for k in range(1, 64)]
    farben = {0: GRUEN, 1: TUERKIS, 2: BLAU, 63: ROT}
    g = s.raster(format(wert, "064b"), (0, yb), groesse=TT, ausrichtung="mitte")
    assert abs(g.x(0) - x0) < 1e-3, (g.x(0), x0)
    mk = {b: g.markieren(0, 63 - b, 63 - b, f, 0.35) for b, f in farben.items()}
    yo = yb + hb / 2
    zeiger, texte = {}, {}
    for b, w, y in ((0, W_BIT0, 2.05), (1, W_BIT1, 1.77), (2, W_BIT2, 1.49)):
        x = g.xm(63 - b)
        zeiger[b] = linie(s, (x, yo), (x, y), farben[b], 2)
        texte[b] = lab(s, w, (x - 0.08, y), GK, "right", farben[b])
    x = g.xm(0)
    zeiger[63] = linie(s, (x, yo), (x, 2.05), ROT, 2)
    texte[63] = lab(s, W_BIT63, (x + 0.08, 2.05), GK, "left", ROT)
    yh = yb - hb / 2 - 0.2
    ziffern = "%016x" % wert
    hexe = [tt(s, ziffern[i], (g.xm(4 * i, 4 * i + 3), yh), TT, "center", ORANGE) for i in range(16)]
    l0x = tt(s, "0x", (x0 - 0.06, yh), TT, "right", ORANGE)
    kl = klammer_h(s, g.x(12), g.xr(51), yh - 0.2, True, DUNKEL)
    l_rahmen = lab(s, W_NRAHMEN, (0, yh - 0.38), GK, "center", DUNKEL)
    rw = tt(s, "0xa3b5", (0, yh - 0.62), TT, "center", ORANGE)
    deut = kasten(s, (0, -0.55), 6.6, 0.55, W_DEUTUNG, BLAU, BLAU_HELL, GK)
    schritt(s, EIN([leiste] + trenn, 0.6))
    s.pause(0.3)
    for b in (0, 1, 2, 63):
        schritt(s, EIN(mk[b], 0.5), ZEICHNE(zeiger[b], 0.5), EIN(texte[b], 0.5))
    schritt(s, ZEICHNE(kl, 0.6), EIN(l_rahmen, 0.6))
    s.pause(0.5)
    schritt(s, EIN(g.ids + hexe + [l0x], 0.7))
    schritt(s, BETONE([mk[b] for b in (0, 1, 2, 63)], 0.8), EIN(rw, 0.6))
    schritt(s, EIN(deut, 0.6))
    s.speichern()


W_GLEICH = ("gleiche Bytes, anderes Bit", "same bytes, different bit", "mismos bytes, otro bit", "相同的字节，不同的位",
            "mêmes octets, autre bit", "aynı baytlar, farklı bit")
W_NXGES = ("Seite rw-p, NX gesetzt", "page rw-p, NX set", "página rw-p, NX activado", "页 rw-p，NX 已置位",
           "page rw-p, NX activé", "sayfa rw-p, NX ayarlı")
W_RXP = ("Seite r-xp", "page r-xp", "página r-xp", "页 r-xp", "page r-xp", "sayfa r-xp")
W_HOLENVERB = ("Befehl holen verboten", "instruction fetch forbidden", "prohibido buscar instrucciones", "禁止取指令",
               "lecture d'instruction interdite", "komut getirmek yasak")


def k2nx():
    """Oben das Terminal mit den echten Läufen von befehl.py rechnen rw und rechnen rx (Heftblock 7.3,
    mitschrift_kap2_b.txt). Darunter zwei Spalten mit derselben Seite (B8 2A 00 00 00 C3): links rw-p, NX gesetzt –
    rip -> MMU, rotes Kreuz „Befehl holen verboten“, Seitenfehler -> SIGSEGV; rechts r-xp – rip -> MMU -> Seite,
    Häkchen, Ergebnis: 42. Zum Schluss über beiden Spalten „gleiche Bytes, anderes Bit“."""
    s = Szene("cyber/k2nx", reihenfolge="anlegen")
    t = s.terminal(pos=(-2.58, 2.8), spalten=56, zeilen=7, prompt=P2, groesse=20)
    spalten = {}
    for seite, cx in (("l", -1.75), ("r", 1.75)):
        rip = ttkasten(s, (cx - 1.3, -0.1), 0.6, 0.36, "rip", ORANGE, ORANGE_HELL, TT)
        mmu = kasten(s, (cx - 0.38, -0.1), 0.62, 0.36, "MMU", DUNKEL, GRAU_HELL, GK)
        seite_k = ttkasten(s, (cx + 0.95, -0.1), 1.5, 0.36, "B8 2A 00 00 00 C3", DUNKEL, WEISS, TK)
        kopf = lab(s, W_NXGES if seite == "l" else W_RXP, (cx + 0.95, 0.3), GK, "center", ROT if seite == "l" else GRUEN)
        a1 = pf(s, (cx - 1.0, -0.1), (cx - 0.69, -0.1), DUNKEL, 2.5, 0.09)
        spalten[seite] = dict(rahmen=rip + mmu + seite_k, kopf=kopf, a1=a1)
    l, r = spalten["l"], spalten["r"]
    kr = kreuz(s, -1.75 - 0.38, 0.25, 0.17)
    l_verb = lab(s, W_HOLENVERB, (-1.75 - 0.38, -0.5), GK, "center", ROT)
    sf = [lab(s, W_SF, (-2.55, -0.88), GK, "center", ROT), pf(s, (-1.85, -0.88), (-1.45, -0.88), ROT, 2.5, 0.09),
          tt(s, "SIGSEGV", (-0.95, -0.88), TK, "center", ROT)]
    hk = haken(s, 1.75 - 0.38, 0.25, 0.17)
    a2 = pf(s, (1.75 - 0.07, -0.1), (1.75 + 0.2, -0.1), DUNKEL, 2.5, 0.09)
    erg = tt(s, "Ergebnis: 42", (1.75 + 0.95, -0.55), TT, "center", GRUEN)
    titel = lab(s, W_GLEICH, (0, 0.75), GT, "center", DUNKEL)
    trennl = linie(s, (0, 0.5), (0, -1.05), HELLGRAU, 1.5, DASH)
    schritt(s, EIN([t.id, trennl] + l["rahmen"] + r["rahmen"], 0.7))
    s.pause(0.3)
    t.eingabe("python3 befehl.py rechnen rw")
    with s.gleichzeitig():
        t.ausgabe("Stück 0x70a25bc8c000: Rechte rw-p")
        schritt(s, EIN(l["kopf"], 0.6))
    schritt(s, ZEICHNE(l["a1"], 0.5))
    schritt(s, WACHS(kr, 0.4), EIN(l_verb, 0.5))
    with s.gleichzeitig():
        t.schritt("Segmentation fault         python3 befehl.py rechnen rw\n" + P2, dauer=0.6)
        schritt(s, EIN(sf, 0.6))
    s.pause(0.5)
    t.eingabe("python3 befehl.py rechnen rx")
    with s.gleichzeitig():
        t.ausgabe("Stück 0x787bad623000: Rechte r-xp")
        schritt(s, EIN(r["kopf"], 0.6))
    schritt(s, ZEICHNE(r["a1"], 0.5))
    schritt(s, WACHS(hk, 0.4), ZEICHNE(a2, 0.5))
    with s.gleichzeitig():
        t.schritt("Ergebnis: 42\n" + P2, dauer=0.6)
        schritt(s, EIN(erg, 0.6))
    s.pause(0.4)
    schritt(s, EIN(titel, 0.6))
    s.speichern()


W_SCHREIBEN_K = ("schreiben", "write", "escribir", "写入", "écrire", "yazma")
W_HOLEN_K = ("Befehl holen", "fetch instruction", "buscar instrucción", "取指令", "lire une instruction", "komut getirme")
W_MPROT = ("mprotect, beim Kernel beantragt", "mprotect, requested from the kernel", "mprotect, solicitado al kernel",
           "mprotect，向内核申请", "mprotect, demandé au noyau", "mprotect, çekirdekten istendi")
W_RWXVERB = ("rwx: verboten nach W^X", "rwx: forbidden by W^X", "rwx: prohibido por W^X", "rwx：W^X 禁止",
             "rwx : interdit par W^X", "rwx: W^X'e göre yasak")


def k2wx():
    """Eine Seite mit drei Schaltern r, w, x. Schritt 1 (r, w an): ein Stift schreibt B8 2A 00 00 00 C3 hinein (Häkchen
    bei „schreiben“), Befehl holen prallt ab (Kreuz). Schritt 2: Pfeil „mprotect, beim Kernel beantragt“ legt w aus und
    x an. Schritt 3: rip holt den Befehl (Häkchen, Ergebnis: 42), Schreiben prallt ab (Kreuz). Rechts ein
    durchgestrichener Kasten mit allen drei Schaltern an: „rwx: verboten nach W^X“. Die Marken tragen die Nummer ihres
    Schritts, damit das Endbild beide Zustände zeigt."""
    s = Szene("cyber/k2wx", reihenfolge="anlegen")
    seite = box(s, (-0.6, 0.0), 2.4, 1.8, DUNKEL, WEISS, 2.5)
    l_seite = lab(s, W_SEITE, (-1.7, 0.72), GK, "left", DUNKEL)
    sch, buchst = {}, []
    for b, xb, an in (("r", -1.5, True), ("w", -0.75, True), ("x", 0.0, False)):
        buchst.append(tt(s, b, (xb, 0.4), TT, "center", DUNKEL))
        sch[b] = schalter(s, xb + 0.36, 0.4, an)
    bytes_t = tt(s, "B8 2A 00 00 00 C3", (-0.6, -0.15), TK, "center", SCHWARZ)
    kern = kasten(s, (-0.6, 1.6), 2.4, 0.38, W_KERN0, ORANGE, ORANGE_HELL, GK)
    a_mp = pf(s, (-0.05, 1.41), (-0.05, 0.56), ORANGE, 2.5, 0.11)
    l_mp = lab(s, W_MPROT, (0.07, 1.13), GK, "left", ORANGE)
    n2 = nummer(s, -0.25, 1.13, 2)
    st = stift(s, (-2.98, 0.38))
    a_w = pf(s, (-2.95, 0.35), (-1.85, 0.35), DUNKEL, 2.5, 0.11)
    l_w = lab(s, W_SCHREIBEN_K, (-2.4, 0.53), GK, "center", DUNKEL)
    rip = ttkasten(s, (-3.1, -0.45), 0.55, 0.3, "rip", ORANGE, ORANGE_HELL, TT)
    a_f = pf(s, (-2.8, -0.45), (-1.85, -0.45), DUNKEL, 2.5, 0.11)
    l_f = lab(s, W_HOLEN_K, (-2.32, -0.21), GK, "center", DUNKEL)
    m = {}
    for k, (y, n, art) in enumerate(((0.12, 1, "h"), (0.12, 3, "k"), (-0.68, 1, "k"), (-0.68, 3, "h"))):
        xn = -2.7 if n == 1 else -2.2
        m[k] = nummer(s, xn, y, n, DUNKEL, 0.1) + [haken(s, xn + 0.22, y, 0.16) if art == "h" else kreuz(s, xn + 0.22, y, 0.14)]
    erg = tt(s, "Ergebnis: 42", (-0.6, -1.15), TT, "center", GRUEN)
    rechts = [box(s, (2.3, 0.0), 2.1, 1.3, DUNKEL, WEISS, 2.5, "rect"), lab(s, W_SEITE, (2.3, 0.82), GK, "center", DUNKEL)]
    for b, xb in (("r", 1.75), ("w", 2.4), ("x", 3.05)):
        rechts.append(tt(s, b, (xb - 0.3, 0.0), TT, "center", DUNKEL))
        g_, gr, kn, _ = schalter(s, xb, 0.0, True, 0.36, 0.2)
        rechts += [g_, gr, kn]
    durch = [linie(s, (1.3, 0.6), (3.3, -0.6), ROT, 4), linie(s, (1.3, -0.6), (3.3, 0.6), ROT, 4)]
    l_rwx = lab(s, W_RWXVERB, (2.3, -0.9), GK, "center", ROT, roh=True)
    an_r, an_w = [sch["r"][0], sch["r"][1], sch["r"][2]], [sch["w"][0], sch["w"][1], sch["w"][2]]
    schritt(s, EIN([seite, l_seite, kern[0], kern[1], st, rip[0], rip[1]] + buchst + an_r + an_w + [sch["x"][0], sch["x"][2]],
                   0.7))
    s.pause(0.4)
    schritt(s, ZEICHNE(a_w, 0.6), EIN(l_w, 0.6))
    schritt(s, EIN(bytes_t, 0.7), EIN(m[0], 0.5))
    schritt(s, ZEICHNE(a_f, 0.6), EIN(l_f, 0.6))
    schritt(s, EIN(m[2][:2], 0.4), WACHS(m[2][2], 0.4))
    s.pause(0.6)
    schritt(s, ZEICHNE(a_mp, 0.6), EIN([l_mp] + n2, 0.6))
    schritt(s, AUS(sch["w"][1], 0.6), VER(sch["w"][2], -sch["w"][3], 0, 0.6), EIN(sch["x"][1], 0.6),
            VER(sch["x"][2], sch["x"][3], 0, 0.6))
    s.pause(0.6)
    schritt(s, BETONE(a_f, 0.6), EIN(m[3][:2], 0.4), WACHS(m[3][2], 0.4), EIN(erg, 0.6))
    schritt(s, BETONE(a_w, 0.6), EIN(m[1][:2], 0.4), WACHS(m[1][2], 0.4))
    s.pause(0.5)
    schritt(s, EIN(rechts, 0.6))
    schritt(s, ZEICHNE(durch, 0.6), EIN(l_rwx, 0.6))
    s.speichern()


W_KHALB = ("Kernel (U/S = 0), läuft auf Stufe 0", "kernel (U/S = 0), runs at level 0", "kernel (U/S = 0), en el nivel 0",
           "内核（U/S = 0），运行在第 0 级", "noyau (U/S = 0), au niveau 0", "çekirdek (U/S = 0), seviye 0'da")
W_PHALB = ("Programm (U/S = 1)", "program (U/S = 1)", "programa (U/S = 1)", "程序（U/S = 1）", "programme (U/S = 1)",
           "program (U/S = 1)")
W_ZEIGER = ("Kernel folgt einem Zeiger", "kernel follows a pointer", "el kernel sigue un puntero", "内核跟随一个指针",
            "le noyau suit un pointeur", "çekirdek bir işaretçiyi izler")
W_VORB = ("vom Programm vorbereitete Bytes", "bytes prepared by the program", "bytes preparados por el programa",
          "程序事先准备的字节", "octets préparés par le programme", "programın hazırladığı baytlar")
W_HOLEN_S = ("Befehl holen", "fetch code", "buscar código", "取指令", "lire du code", "komut getir")
W_LESEN = ("lesen", "read", "leer", "读取", "lire", "okuma")
W_KURZ = ("Zugriff kurz erlaubt", "access briefly allowed", "acceso permitido un momento", "短暂允许访问",
          "accès permis un instant", "erişime kısa süre izin")
W_ARGS = ("Argumente", "arguments", "argumentos", "参数", "arguments", "argümanlar")
W_KOPIE = ("Kopie", "copy", "copia", "副本", "copie", "kopya")


def k2smap():
    """Oben die Kernelhälfte (U/S = 0, Stufe 0), unten die Hälfte der Programme (U/S = 1). Links folgt der Kernel
    fehlerhaft einem Zeiger nach unten auf vom Programm vorbereitete Bytes: Befehl holen prallt an SMEP ab, Lesen an
    SMAP. Rechts copy_from_user: Der Schalter „Zugriff kurz erlaubt“ geht an, die Argumente werden in den Kernel
    kopiert, der Schalter geht wieder aus."""
    s = Szene("cyber/k2smap", reihenfolge="anlegen")
    bk = box(s, (0, 1.1), 6.9, 1.5, ORANGE, ORANGE_HELL, 2)
    bp = box(s, (0, -0.65), 6.9, 1.5, BLAU, BLAU_HELL, 2)
    titel = [lab(s, W_KHALB, (-3.35, 1.66), GK, "left", ORANGE), lab(s, W_PHALB, (-3.35, -1.22), GK, "left", BLAU)]
    code = kasten(s, (-1.95, 1.2), 2.7, 0.42, W_ZEIGER, ORANGE, WEISS, GK)
    vorb = kasten(s, (-1.95, -0.5), 2.7, 0.42, W_VORB, BLAU, WEISS, GK)
    aa = pf(s, (-3.0, 0.99), (-3.0, 0.31), ROT, 2.5, 0.11, DASH)
    ab = pf(s, (-1.6, 0.99), (-1.6, 0.31), ROT, 2.5, 0.11, DASH)
    la = lab(s, W_HOLEN_S, (-2.92, 0.66), GK, "left", ROT)
    lb = lab(s, W_LESEN, (-1.52, 0.66), GK, "left", ROT)
    ka, kb = kreuz(s, -3.0, 0.225, 0.16), kreuz(s, -1.6, 0.225, 0.16)
    sa, sb = lab(s, "SMEP", (-2.84, 0.225), GK, "left", ROT), lab(s, "SMAP", (-1.44, 0.225), GK, "left", ROT)
    cfu = ttkasten(s, (0.75, 1.2), 1.75, 0.42, "copy_from_user", ORANGE, WEISS, TK)
    puffer = box(s, (2.75, 1.2), 1.1, 0.42, ORANGE, WEISS, 2, dash=DASH)
    l_puffer = lab(s, W_KOPIE, (2.75, 1.56), GK, "center", ORANGE)
    args = kasten(s, (2.75, -0.5), 1.1, 0.42, W_ARGS, BLAU, WEISS, GK)
    sw = schalter(s, 1.03, 0.66, False)
    l_sw = lab(s, W_KURZ, (1.3, 0.66), GK, "left", GRUEN)
    a_cfu = pf(s, (0.75, 0.99), (2.17, -0.5), GRUEN, 2.5, 0.11, knick="vh")
    chip = kasten(s, (2.75, -0.5), 0.9, 0.3, W_DATEN, BLAU, BLAU_HELL, 17)
    schritt(s, EIN([bk, bp] + titel + code + vorb + [cfu[0], cfu[1], puffer, l_puffer] + args + [sw[0], sw[2], l_sw], 0.7))
    s.pause(0.5)
    schritt(s, ZEICHNE(aa, 0.6), EIN(la, 0.6))
    schritt(s, WACHS(ka, 0.4), EIN(sa, 0.4))
    schritt(s, ZEICHNE(ab, 0.6), EIN(lb, 0.6))
    schritt(s, WACHS(kb, 0.4), EIN(sb, 0.4))
    s.pause(0.6)
    schritt(s, EIN(sw[1], 0.5), VER(sw[2], sw[3], 0, 0.5), BETONE(l_sw, 0.7))
    schritt(s, ZEICHNE(a_cfu, 0.7))
    schritt(s, EIN(chip, 0.4))
    schritt(s, *[ZU(i, 2.75, 1.2, 0.9) for i in chip])
    schritt(s, AUS(sw[1], 0.5), VER(sw[2], -sw[3], 0, 0.5))
    s.speichern()


W_CODE = ("Code", "code", "código", "代码", "code", "kod")
W_NURLESEN = ("nur lesen", "read only", "solo lectura", "只读", "lecture seule", "salt okunur")
W_DATENNX = ("Daten, nicht ausführbar", "data, not executable", "datos, no ejecutables", "数据，不可执行",
             "données, non exécutables", "veri, çalıştırılamaz")
W_LUECKE = ("Schutzlücke", "guard gap", "hueco de protección", "保护间隙", "zone de garde", "koruma boşluğu")
W_KNICHT2 = ("Kernel:\nnicht aufgelistet", "kernel:\nnot listed", "kernel:\nno listado", "内核：\n未列出", "noyau :\nnon listé",
             "çekirdek:\nlistelenmez")
L_MAPS = ["62a019dc1000-62a019eb3000 r--p … cat",
          "62a019eb3000-62a01a36b000 r-xp … cat",
          "62a01a88f000-62a01a895000 rw-p … cat",
          "62a0343be000-62a034400000 rw-p … [heap]",
          "75980fa28000-75980fbc0000 r-xp … libc.so.6",
          "75980ff3d000-75980ff3e000 ---p",
          "7ffe148ff000-7ffe14920000 rw-p … [stack]",
          "7ffe149f5000-7ffe149f9000 r--p … [vvar]",
          "7ffe149f9000-7ffe149fb000 r-xp … [vdso]"]


def k2maps():
    """Ausschnitt der Bereichsliste von cat (Heftblock 7.6, gekürzt: … für Versatz, Gerät, Inode und Pfad). Nacheinander
    werden die Rechte markiert: r-xp grün „Code“, r--p grau „nur lesen“, rw-p blau „Daten, nicht ausführbar“, ---p rot
    „Schutzlücke“. Rechts daneben eine senkrechte Leiste des Adressraums (unten 0 und die Hälfte der Programme, oben die
    Kernelhälfte, „nicht aufgelistet“), in der dieselben Farben an ihren Adressen erscheinen (0x62a0…, 0x7598…, 0x7ffe…
    im Verhältnis zu 0x0000800000000000; Streifen nicht maßstäblich)."""
    s = Szene("cyber/k2maps", reihenfolge="anlegen")
    xl, bl_, ya, ym, ye = 3.1, 0.32, -0.9, 1.1, 1.95       # senkrechte Leiste: 0 unten, Hälfte der Programme bis ym
    lp = box(s, (xl, (ya + ym) / 2), bl_, ym - ya, BLAU, WEISS, 2, "rect")
    lk = box(s, (xl, (ym + ye) / 2), bl_, ye - ym, GRAU, GRAU_HELL, 2, "rect", DASH)
    l_lp = lab(s, W_PROGRAMM, (xl - 0.24, 0.0), GK, "right", BLAU)
    l_lk = lab(s, W_KNICHT2, (xl - 0.24, 1.72), GK, "right", GRAU)
    g = s.raster(L_MAPS, (-3.4, 1.85), groesse=TK)
    gruppen = ((GRUEN, (1, 4, 8), W_CODE, 1), (GRAU, (0, 7), W_NURLESEN, 0), (BLAU, (2, 3, 6), W_DATENNX, 2),
               (ROT, (5,), W_LUECKE, 5))
    hs = 0.045                                                # Höhe eines Streifens (nicht maßstäblich)
    y_cat = ya + (ym - ya) * 0x62a0 / 0x8000                  # 0x62a0… / 0x8000… der Hälfte
    unten = {0: y_cat - 2 * hs, 4: 0.83, 6: ym - 3 * hs}      # libc (0x7598…) leicht nach unten gerückt, damit Platz bleibt
    lage = {0: 0, 1: 1, 2: 2, 3: 3, 4: 0, 5: 1, 6: 0, 7: 1, 8: 2}
    def y_streifen(z):
        basis = 0 if z < 4 else (4 if z < 6 else 6)
        return unten[basis] + hs * lage[z] + hs / 2
    adr = [tt(s, "0", (xl - 0.24, ya + 0.05), TK, "right", DUNKEL),
           tt(s, "62a0…", (xl - 0.24, y_cat), TK, "right", DUNKEL),
           tt(s, "7598…", (xl - 0.24, unten[4] + hs), TK, "right", DUNKEL),
           tt(s, "7ffe…", (xl - 0.24, ym - 1.5 * hs), TK, "right", DUNKEL)]
    teile = []
    for f, zeilen, w, z_lab in gruppen:
        mks = [g.markieren(z, 26, 29, f, 0.3) for z in zeilen]
        streifen = [box(s, (xl, y_streifen(z)), bl_ - 0.04, hs, f, f, 0, "rect") for z in zeilen]
        teile.append((mks, streifen, lab(s, w, (0.2, g.y(z_lab)), GK, "left", f)))
    schritt(s, EIN(g.ids + [lp, lk, l_lp, l_lk] + adr, 0.7))
    s.pause(0.5)
    for mks, streifen, l in teile:
        schritt(s, EIN(mks + streifen + [l], 0.6))
        s.pause(0.3)
    s.speichern()


# ================================================================== Abschnitt 8: Die Startkette als Schutzgrenze
W_FW = ("Firmware", "firmware", "firmware", "固件", "firmware", "ürün yazılımı")
W_BL = ("Bootloader", "boot loader", "bootloader", "引导加载程序", "bootloader", "önyükleyici")
W_SCANNER = ("Virenscanner", "virus scanner", "antivirus", "病毒扫描程序", "antivirus", "virüs tarayıcı")
W_VERAENDERT = ("verändert", "modified", "modificado", "已被篡改", "modifié", "değiştirilmiş")
W_STABS = ("Seitentabellen", "page tables", "tablas de páginas", "页表", "tables des pages", "sayfa tabloları")
W_ZEILE_GEAENDERT = ("eine Zeile geändert", "one row changed", "una fila cambiada", "改了一行", "une ligne modifiée",
                     "bir satır değişti")
W_BEMERKEN = ("Programme und Virenscanner sehen nur den fertigen Kernel und bemerken nichts",
              "programs and virus scanner see only the finished kernel and notice nothing",
              "los programas y el antivirus solo ven el kernel terminado y no notan nada",
              "程序和病毒扫描程序只看到已完成启动的内核，什么也察觉不到",
              "les programmes et l'antivirus ne voient que le noyau prêt et ne remarquent rien",
              "programlar ve virüs tarayıcı yalnızca hazır çekirdeği görür, hiçbir şey fark etmez")


def k2bootkit():
    """Zeitleiste des Starts: Firmware, Bootloader, Kernel (mit Tabelle der Dienste), Programme samt Virenscanner. Beim
    Kernel erscheinen nacheinander die Grenzen als Schranken (Einsprungtabelle, Zeitgeber, Seitentabellen, NX, SMEP,
    SMAP) auf der Seite zu den Programmen. Dann wird der Bootloader rot („verändert“) und greift von der frühen Seite
    her in die Tabelle der Dienste, an den Schranken vorbei; die Programme bemerken nichts."""
    s = Szene("cyber/k2bootkit", reihenfolge="anlegen")
    fw = kasten(s, (-2.95, 0.6), 0.95, 0.5, W_FW, DUNKEL, GRAU_HELL, GK)
    bl = [box(s, (-1.85, 0.6), 1.0, 0.5, DUNKEL, GRAU_HELL, 2)]
    bl_rot = box(s, (-1.85, 0.6), 1.0, 0.5, ROT, ROT_HELL, 2.5)          # liegt unter dem Text (reihenfolge="anlegen")
    bl.append(lab(s, W_BL, (-1.85, 0.6), GK, "center", SCHWARZ))
    l_ver = lab(s, W_VERAENDERT, (-1.85, 0.18), GK, "center", ROT)
    kern = [box(s, (0.65, 0.4), 3.0, 2.2, ORANGE, ORANGE_HELL, 2), lab(s, W_KERNEL, (-0.75, 1.3), GN, "left", ORANGE)]
    l_tab = lab(s, W_DIENSTE, (-0.12, 0.98), GK, "center", DUNKEL)
    tab_k = box(s, (-0.12, 0.5), 1.05, 0.66, DUNKEL, WEISS, 1.5, "rect")
    g = s.raster(["0  read", "1  write", "2  open"], (-0.55, 0.68), groesse=TK)
    mk = g.markieren(1, 0, 7, ROT, 0.35)
    l_zeile = lab(s, W_ZEILE_GEAENDERT, (-0.12, -0.05), GK, "center", ROT)
    schranken = []
    for y, w in ((1.05, W_EINSPRUNGTABELLE), (0.62, W_ZEITGEBER), (0.19, W_STABS), (-0.24, "NX, SMEP, SMAP")):
        schranken.append(kasten(s, (1.42, y), 1.3, 0.3, w, DUNKEL, DUNKEL, 17, WEISS, 2, "rect"))
    progs = kasten(s, (2.87, 0.95), 1.1, 0.4, W_PROGRAMME, BLAU, BLAU_HELL, GK)
    scan = kasten(s, (2.87, 0.35), 1.1, 0.4, W_SCANNER, BLAU, BLAU_HELL, GK)
    zeit = [pf(s, (-3.4, -1.35), (3.4, -1.35), GRAU, 2, 0.12), lab(s, W_ZEIT, (3.4, -1.17), GK, "right", GRAU)]
    l_bem = lab(s, W_BEMERKEN, (3.4, -0.95), GK, "right", BLAU)
    angriff = bogen(s, (-1.85, 0.86), (-0.68, 0.5), 0.45, ROT, 3, marke="0.95", spitze=0.13)
    schritt(s, EIN(fw + bl + kern + [l_tab, tab_k] + g.ids + progs + scan + zeit, 0.7))
    s.pause(0.4)
    for sk in schranken:
        schritt(s, EIN(sk, 0.4))
    s.pause(0.6)
    with s.gleichzeitig():
        schritt(s, EIN([bl_rot, l_ver], 0.6))
        s.ersetzen(bl[1], W(s, W_BL), farbe=ROT, dauer=0.6)
    schritt(s, ZEICHNE(angriff, 0.8))
    schritt(s, EIN([mk, l_zeile], 0.6))
    s.pause(0.4)
    schritt(s, BETONE(progs + scan, 0.8), EIN(l_bem, 0.6))
    s.speichern()


W_STARTCODE = ("unveränderlicher\nStartcode", "immutable\nstart code", "código de arranque\ninmutable", "不可更改的\n启动代码",
               "code de démarrage\nimmuable", "değiştirilemez\nbaşlangıç kodu")
W_FWSCHL = ("Firmware mit\nSchlüsseln", "firmware\nwith keys", "firmware\ncon claves", "带密钥的\n固件", "firmware\navec clés",
            "anahtarlı ürün\nyazılımı")
W_PRUEFT = ("prüft", "checks", "comprueba", "检查", "vérifie", "denetler")
W_WERPRUEFT = ("wer prüft mich?", "who checks me?", "¿quién me comprueba?", "谁来检查我？", "qui me vérifie ?",
               "beni kim denetler?")
W_NIEMAND = ("niemand: deshalb unveränderlich", "nobody: hence immutable", "nadie: por eso es inmutable",
             "没有人：所以不可更改", "personne : donc immuable", "kimse: bu yüzden değiştirilemez")
W_UEBERSCHR = ("überschreiben", "overwrite", "sobrescribir", "覆盖", "écraser", "üzerine yazma")
W_VANKER = ("Vertrauensanker", "root of trust", "raíz de confianza", "信任根", "racine de confiance", "güven kökü")


def anker_bild(s, x, y, farbe=DUNKEL):
    """Anker, Ring oben bei (x, y); Ergebnis: Liste der ids."""
    ids = [s.kreis(None, r4(x), r4(y), 0.07, farbe=farbe, dicke=3, fuellung=WEISS, deckung=1.0),
           linie(s, (x, y - 0.07), (x, y - 0.68), farbe, 3.5), linie(s, (x - 0.17, y - 0.19), (x + 0.17, y - 0.19), farbe, 3.5)]
    yb = y - 0.42
    ids.append(s.weg(None, "%s+0.28*cos(t)" % r4(x), "%s+0.28*sin(t)" % r4(yb), 3.14159, 6.28318, farbe=farbe, dicke=3.5,
                     n=41))
    for sx in (-1, 1):
        xe = x + sx * 0.28
        ids += [linie(s, (xe, yb), (xe - sx * 0.07, yb + 0.08), farbe, 3), linie(s, (xe, yb), (xe + sx * 0.09, yb + 0.04), farbe, 3)]
    return ids


def k2anker():
    """Kette aus vier Gliedern (unveränderlicher Startcode, Firmware mit Schlüsseln, Bootloader, Kernel), Pfeile „prüft“.
    Am ersten Glied hängt ein Anker (Vertrauensanker). „wer prüft mich?“ wird zu „niemand: deshalb unveränderlich“
    (Schloss am ersten Glied). Ein Versuch, das erste Glied zu überschreiben, prallt ab."""
    s = Szene("cyber/k2anker", reihenfolge="anlegen")
    xs, y = (-2.65, -0.88, 0.88, 2.65), 0.55
    glieder = [kasten(s, (xs[0], y), 1.45, 0.62, W_STARTCODE, DUNKEL, GRAU_HELL, GK, dicke=2.5),
               kasten(s, (xs[1], y), 1.45, 0.62, W_FWSCHL, DUNKEL, GRAU_HELL, GK),
               kasten(s, (xs[2], y), 1.45, 0.62, W_BL, DUNKEL, GRAU_HELL, GK),
               kasten(s, (xs[3], y), 1.45, 0.62, W_KERNEL, ORANGE, ORANGE_HELL, GK)]
    pruef = []
    for k in range(3):
        pruef.append([pf(s, (xs[k] + 0.73, y), (xs[k + 1] - 0.73, y), GRUEN, 2.5, 0.1),
                      lab(s, W_PRUEFT, ((xs[k] + xs[k + 1]) / 2, y + 0.45), GK, "center", GRUEN)])
    seil = linie(s, (xs[0], y - 0.31), (xs[0], -0.2), DUNKEL, 2)
    anker = anker_bild(s, xs[0], -0.27)
    l_anker = lab(s, W_VANKER, (xs[0] + 0.4, -0.6), GN, "left", DUNKEL)
    frage = lab(s, W_WERPRUEFT, (-3.4, 1.45), GN, "left", ORANGE)
    schloss = s.schloss((xs[0] - 0.62, y + 0.33), 0.3, False, DUNKEL)
    angriff = pf(s, (-0.35, -0.9), (-1.82, 0.13), ROT, 2.5, 0.12, DASH)
    l_ang = lab(s, W_UEBERSCHR, (-0.25, -0.9), GK, "left", ROT)
    kr = kreuz(s, -1.92, 0.2, 0.22)
    schritt(s, EIN(flach(glieder), 0.7))
    s.pause(0.3)
    for p in pruef:
        schritt(s, ZEICHNE(p[0], 0.4), EIN(p[1], 0.4))
    schritt(s, ZEICHNE(seil, 0.3), EIN(anker + [l_anker], 0.6))
    s.pause(0.4)
    schritt(s, EIN(frage, 0.6))
    s.pause(0.8)
    with s.gleichzeitig():
        s.ersetzen(frage, W(s, W_NIEMAND), dauer=0.8)
        schritt(s, WACHS(schloss, 0.6))
    s.pause(0.5)
    schritt(s, ZEICHNE(angriff, 0.7), EIN(l_ang, 0.6))
    schritt(s, WACHS(kr, 0.4))
    s.speichern()


W_PK = ("PK (Hersteller)", "PK (manufacturer)", "PK (fabricante)", "PK（制造商）", "PK (fabricant)", "PK (üretici)")
W_KEKL = ("KEK (z. B. Microsoft, Hersteller)", "KEK (e.g. Microsoft, manufacturer)", "KEK (p. ej., Microsoft, fabricante)",
          "KEK（如 Microsoft、制造商）", "KEK (p. ex. Microsoft, fabricant)", "KEK (ör. Microsoft, üretici)")
W_DB = ("db: erlaubt", "db: allowed", "db: permitido", "db：允许", "db : autorisé", "db: izinli")
W_DBX = ("dbx: gesperrt", "dbx: blocked", "dbx: bloqueado", "dbx：已禁止", "dbx : bloqué", "dbx: engellenmiş")
W_DARF = ("darf ändern", "may change", "puede cambiar", "可以修改", "peut modifier", "değiştirebilir")
W_STARTPROG = ("Startprogramm", "boot program", "programa de arranque", "启动程序", "programme de démarrage",
               "başlatma programı")
W_INDBX = ("1. in dbx?", "1. in dbx?", "1. ¿en dbx?", "1. 在 dbx 中？", "1. dans dbx ?", "1. dbx'te mi?")
W_ZUDB = ("2. passt zu db?", "2. matches db?", "2. ¿coincide con db?", "2. 与 db 匹配？", "2. correspond à db ?",
          "2. db ile eşleşiyor mu?")
W_JA1 = ("ja", "yes", "sí", "是", "oui", "evet")
W_PRUEF_FW = ("Prüfung der Firmware", "firmware check", "comprobación del firmware", "固件的检查", "contrôle du firmware",
              "ürün yazılımı denetimi")
W_STARTET = ("startet", "starts", "arranca", "启动", "démarre", "başlar")


def k2schluessel():
    """Pyramide: PK (Hersteller) -> KEK (z. B. Microsoft, Hersteller) -> db: erlaubt (grün) | dbx: gesperrt (rot), Pfeile
    „darf ändern“. Unten kommt ein Startprogramm an die Schranke; rechts die Prüfung der Firmware: 1. in dbx? nein,
    2. passt zu db? ja; dann öffnet sich die Schranke, das Startprogramm startet."""
    s = Szene("cyber/k2schluessel", reihenfolge="anlegen")
    pyr = s.vieleck(None, [(-1.3, 2.1), (-3.4, -0.4), (0.8, -0.4)], GRAU_HELL, 0.7, 0)
    pk = kasten(s, (-1.3, 1.6), 2.0, 0.4, W_PK, DUNKEL, WEISS, GK)
    kek = kasten(s, (-1.3, 0.85), 3.3, 0.4, W_KEKL, DUNKEL, WEISS, GK)
    db = kasten(s, (-2.2, 0.05), 1.6, 0.4, W_DB, GRUEN, GRUEN_HELL, GK, GRUEN)
    dbx = kasten(s, (-0.4, 0.05), 1.6, 0.4, W_DBX, ROT, ROT_HELL, GK, ROT)
    a1 = [pf(s, (-1.3, 1.4), (-1.3, 1.06), DUNKEL, 2.5, 0.1), lab(s, W_DARF, (-1.18, 1.23), GK, "left", DUNKEL)]
    a2 = [pf(s, (-2.2, 0.65), (-2.2, 0.26), DUNKEL, 2.5, 0.1), pf(s, (-0.4, 0.65), (-0.4, 0.26), DUNKEL, 2.5, 0.1),
          lab(s, W_DARF, (-1.3, 0.45), GK, "center", DUNKEL)]
    boden = linie(s, (-3.4, -1.2), (3.4, -1.2), HELLGRAU, 2)
    pfosten = box(s, (0.75, -1.15), 0.14, 0.14, DUNKEL, DUNKEL, 1, "rect")
    baum = linie(s, (0.75, -1.15), (0.75, -0.5), ROT, 7)
    prog = kasten(s, (-2.6, -0.95), 1.7, 0.4, W_STARTPROG, BLAU, BLAU_HELL, GK)
    titel = lab(s, W_PRUEF_FW, (1.1, 0.95), GN, "left", DUNKEL)
    q1, q2 = lab(s, W_INDBX, (1.1, 0.5), GK, "left", DUNKEL), lab(s, W_ZUDB, (1.1, 0.1), GK, "left", DUNKEL)
    a_q1 = [lab(s, W_NEIN, (2.95, 0.5), GK, "left", GRUEN), haken(s, 2.82, 0.5, 0.15)]
    a_q2 = [lab(s, W_JA1, (2.95, 0.1), GK, "left", GRUEN), haken(s, 2.82, 0.1, 0.15)]
    l_start = lab(s, W_STARTET, (2.4, -0.55), GK, "center", GRUEN)
    schritt(s, EIN([pyr] + pk, 0.6))
    schritt(s, ZEICHNE(a1[0], 0.4), EIN(kek + [a1[1]], 0.5))
    schritt(s, ZEICHNE(a2[:2], 0.4), EIN(db + dbx + [a2[2]], 0.5))
    s.pause(0.5)
    schritt(s, EIN([boden, pfosten, baum, titel] + prog, 0.6))
    schritt(s, *[ZU(i, -0.15, -0.95, 0.8) for i in prog])
    schritt(s, EIN(q1, 0.5), BETONE(dbx, 0.8))
    schritt(s, EIN(a_q1, 0.5))
    schritt(s, EIN(q2, 0.5), BETONE(db, 0.8))
    schritt(s, EIN(a_q2, 0.5))
    schritt(s, DREH(baum, -80, (0.75, -1.15), 0.8))
    schritt(s, *[ZU(i, 2.4, -0.95, 0.8) for i in prog], EIN(l_start, 0.6))
    s.pause(0.3)
    s.speichern()


W_NEUDBX = ("neuer Eintrag für dbx\n(aus Windows Update)", "new entry for dbx\n(from Windows Update)",
            "nueva entrada para dbx\n(de Windows Update)", "dbx 的新条目\n（来自 Windows Update）",
            "nouvelle entrée pour dbx\n(de Windows Update)", "dbx için yeni kayıt\n(Windows Update'ten)")
W_SIGKEK = ("signiert mit KEK von Microsoft", "signed with Microsoft's KEK", "firmado con la KEK de Microsoft",
            "用 Microsoft 的 KEK 签名", "signé avec la KEK de Microsoft", "Microsoft'un KEK'iyle imzalı")
W_SCHAD = ("Schadprogramm\nmit Verwalterrechten", "malware with\nadministrator rights", "programa malicioso con\nderechos de administrador",
           "具有管理员权限的\n恶意程序", "logiciel malveillant avec\ndroits d'administrateur", "yönetici haklarına sahip\nzararlı program")
W_OHNESIEGEL = ("ohne Siegel: in db eintragen", "no seal: add to db", "sin sello: añadir a db", "无签章：写入 db",
                "sans sceau : ajouter à db", "mühürsüz: db'ye ekle")
W_MENSCH = ("Mensch an der Tastatur,\nMenü der Firmware", "person at the keyboard,\nfirmware menu",
            "persona en el teclado,\nmenú del firmware", "键盘前的人，\n固件菜单", "personne au clavier,\nmenu du firmware",
            "klavye başındaki kişi,\nürün yazılımı menüsü")
W_NURAM = ("nur am Rechner", "only at the computer", "solo en el equipo", "只能在电脑前", "seulement sur place",
           "yalnızca yerinde")
W_NEU = ("neu", "new", "nuevo", "新", "nouveau", "yeni")


def mensch_bild(s, x, y, farbe=DUNKEL):
    """Mensch (Kopf und Schultern) um (x, y); Ergebnis: Liste der ids."""
    return [s.kreis(None, r4(x), r4(y + 0.17), 0.1, farbe=farbe, dicke=2.5, fuellung=WEISS, deckung=1.0),
            s.box("", (r4(x), r4(y - 0.1)), breite=0.38, hoehe=0.3, form="round", farbe=farbe, fuellung=WEISS, deckung=1.0,
                  dicke=2.5)]


def k2aendern():
    """Rechts die Firmware mit PK, KEK, db, dbx hinter einem Schloss. Von links drei Änderungen: (1) neuer dbx-Eintrag
    aus Windows Update mit Siegel „signiert mit KEK von Microsoft“: Häkchen, der Eintrag landet in dbx; (2) Schadprogramm
    mit Verwalterrechten will ohne Siegel in db: Kreuz; (3) Mensch an der Tastatur im Menü der Firmware: Häkchen,
    „nur am Rechner“."""
    s = Szene("cyber/k2aendern", reihenfolge="anlegen")
    fw = [box(s, (2.3, 0.15), 2.2, 2.9, DUNKEL, GRAU_HELL, 2.5), lab(s, W_FW, (2.3, 1.38), GN, "center", DUNKEL)]
    listen = []
    for y, t, f, fh in ((0.95, "PK", DUNKEL, WEISS), (0.45, "KEK", DUNKEL, WEISS), (-0.05, "db", GRUEN, GRUEN_HELL),
                        (-0.55, "dbx", ROT, ROT_HELL)):
        listen += [box(s, (2.45, y), 1.5, 0.36, f, fh, 2), tt(s, t, (1.88, y), TK, "center", f)]
    schloss = s.schloss((1.2, 0.2), 0.42, False, DUNKEL)
    nums = [nummer(s, -3.3, y, n) for y, n in ((1.15, 1), (0.15, 2), (-0.95, 3))]
    e1 = kasten(s, (-1.9, 1.15), 2.2, 0.55, W_NEUDBX, BLAU, BLAU_HELL, GK)
    sg = siegel(s, -0.54, 1.15, "KEK", 0.2)
    l_sg = lab(s, W_SIGKEK, (-1.9, 1.62), GK, "center", ORANGE)
    a1 = pf(s, (-0.32, 1.06), (0.98, 0.38), GRUEN, 2.5, 0.11)
    h1 = haken(s, 1.2, 0.68, 0.2)
    chip = kasten(s, (-1.9, 1.15), 0.62, 0.26, W_NEU, ROT, WEISS, 17, ROT)
    e2 = kasten(s, (-1.9, 0.15), 2.2, 0.55, W_SCHAD, ROT, ROT_HELL, GK)
    a2 = pf(s, (-0.75, 0.15), (0.92, 0.15), ROT, 2.5, 0.11, DASH)
    l_a2 = lab(s, W_OHNESIEGEL, (-0.7, 0.33), GK, "left", ROT)
    k2 = kreuz(s, 0.85, 0.15, 0.2)
    pers = mensch_bild(s, -2.85, -0.95)
    tast = [box(s, (-2.3, -1.12), 0.5, 0.2, DUNKEL, WEISS, 1.8, "rect")] + \
        [linie(s, (-2.5 + 0.1 * k, -1.17), (-2.5 + 0.1 * k + 0.05, -1.17), DUNKEL, 1.5) for k in range(5)] + \
        [linie(s, (-2.47, -1.07), (-2.13, -1.07), DUNKEL, 1.5)]
    l_m = lab(s, W_MENSCH, (-1.95, -0.95), GK, "left", DUNKEL)
    a3 = pf(s, (-0.4, -0.95), (1.18, -0.95), GRUEN, 2.5, 0.11)
    h3 = haken(s, 0.4, -0.75, 0.2)
    l_nur = lab(s, W_NURAM, (0.35, -1.18), GK, "center", GRUEN)
    schritt(s, EIN(fw + listen + [schloss], 0.7))
    s.pause(0.4)
    schritt(s, EIN(nums[0] + e1 + sg + [l_sg], 0.6))
    schritt(s, ZEICHNE(a1, 0.6))
    schritt(s, WACHS(h1, 0.4), BETONE(schloss, 0.6))
    schritt(s, EIN(chip, 0.3))
    schritt(s, *[ZU(i, 2.85, -0.55, 0.9) for i in chip])
    s.pause(0.5)
    schritt(s, EIN(nums[1] + e2, 0.6))
    schritt(s, ZEICHNE(a2, 0.6), EIN(l_a2, 0.6))
    schritt(s, WACHS(k2, 0.4), BETONE(schloss, 0.6))
    s.pause(0.5)
    schritt(s, EIN(nums[2] + pers + tast + [l_m], 0.6))
    schritt(s, ZEICHNE(a3, 0.6))
    schritt(s, WACHS(h3, 0.4), EIN(l_nur, 0.5))
    s.speichern()


W_SPERRL = ("Sperrliste (dbx)", "block list (dbx)", "lista de bloqueo (dbx)", "禁止列表（dbx）", "liste de blocage (dbx)",
            "engel listesi (dbx)")
W_ZERT = ("3 Zertifikate", "3 certificates", "3 certificados", "3 个证书", "3 certificats", "3 sertifika")
W_150 = ("150 Prüfsummen", "150 checksums", "150 sumas de verificación", "150 个校验和", "150 sommes de contrôle",
         "150 sağlama toplamı")
W_FUELL = ("≈ 10 kB: fast ein Drittel", "≈ 10 kB: almost a third", "≈ 10 kB: casi un tercio", "≈ 10 kB：近三分之一",
           "≈ 10 kB : près d'un tiers", "≈ 10 kB: neredeyse üçte biri")
W_SBAT = ("GRUB: mindestens Generation 3", "GRUB: at least generation 3", "GRUB: al menos generación 3", "GRUB：至少第 3 代",
          "GRUB : au moins génération 3", "GRUB: en az 3. nesil")
W_SHIMPR = ("prüft shim, steht nicht in dbx", "checked by shim, not in dbx", "lo comprueba shim, no está en dbx",
            "由 shim 检查，不在 dbx 中", "vérifié par shim, pas dans dbx", "shim denetler, dbx'te değil")
W_GENS = [("Bootloader\nGeneration %d" % n, "boot loader\ngeneration %d" % n, "bootloader\ngeneración %d" % n,
           "引导加载程序\n第 %d 代" % n, "bootloader\ngénération %d" % n, "önyükleyici\n%d. nesil" % n) for n in (1, 2, 3)]


def k2widerruf():
    """Links die Sperrliste mit Skala 0 bis 32 kB; drei Zertifikate und ein Block aus 150 Prüfsummen fallen hinein, der
    Füllstand steigt auf ≈ 10 kB (fast ein Drittel). Rechts drei Fassungen eines Bootloaders (Generation 1, 2, 3); ein
    kurzer Eintrag „GRUB: mindestens Generation 3“ (prüft shim, steht nicht in dbx) sperrt die beiden alten auf einmal."""
    s = Szene("cyber/k2widerruf", reihenfolge="anlegen")
    beh = box(s, (-2.4, -0.2), 1.4, 2.6, ROT, WEISS, 2.5, "rect")
    l_beh = lab(s, W_SPERRL, (-2.4, 1.33), GK, "center", ROT)
    skala = [lab(s, "32 kB", (-1.6, 1.0), GK, "left", DUNKEL), lab(s, "0", (-1.6, -1.42), GK, "left", DUNKEL)]
    hub = 1.6                                     # Einträge erscheinen oben im Kasten und fallen um hub nach unten
    zert = [box(s, (-2.4, y + hub), 1.2, 0.1, ORANGE, ORANGE_HELL, 1.5, "rect") for y in (-1.44, -1.32, -1.2)]
    l_zert = lab(s, W_ZERT, (-1.6, -1.27), GK, "left", ORANGE)
    block = [box(s, (-2.4, -0.915 + hub), 1.2, 0.43, BLAU, BLAU_HELL, 1.5, "rect")] + \
        [linie(s, (-2.9, y + hub), (-1.9, y + hub), BLAU, 1) for y in (-1.06, -0.99, -0.92, -0.85, -0.78)]
    l_block = lab(s, W_150, (-1.6, -0.92), GK, "left", BLAU)
    stand = [linie(s, (-3.1, -0.69), (-1.7, -0.69), DUNKEL, 2, DASH), lab(s, W_FUELL, (-1.6, -0.6), GK, "left", DUNKEL)]
    gens = [kasten(s, (2.6, y), 1.55, 0.55, W_GENS[k], DUNKEL, GRAU_HELL, GK) for k, y in enumerate((0.85, 0.05, -0.75))]
    sbat = kasten(s, (0.15, 1.0), 2.35, 0.42, W_SBAT, GRUEN, GRUEN_HELL, GK)
    l_shim = lab(s, W_SHIMPR, (0.15, 0.6), GK, "center", DUNKEL)
    pfeile = [pf(s, (1.33, 1.0 - 0.05 * k), (1.8, y), DUNKEL, 2.5, 0.1) for k, y in enumerate((0.85, 0.05, -0.75))]
    marken = [kreuz(s, 3.2, 0.85, 0.2), kreuz(s, 3.2, 0.05, 0.2), haken(s, 3.2, -0.75, 0.2)]
    schritt(s, EIN([beh, l_beh] + skala, 0.6))
    s.pause(0.3)
    schritt(s, EIN(zert, 0.4))
    schritt(s, *VERS(zert, 0, -hub, 0.6), EIN(l_zert, 0.6))
    schritt(s, EIN(block, 0.4))
    schritt(s, *VERS(block, 0, -hub, 0.6), EIN(l_block, 0.6))
    schritt(s, ZEICHNE(stand[0], 0.5), EIN(stand[1], 0.5))
    s.pause(0.6)
    schritt(s, EIN(flach(gens), 0.6))
    schritt(s, EIN(sbat + [l_shim], 0.6))
    schritt(s, ZEICHNE(pfeile, 0.6))
    schritt(s, WACHS(marken, 0.5))
    s.speichern()


# ================================================================== Abschnitt 9: Measured Boot
W_VERHINDERT = ("Start bricht ab: verhindert", "booting stops: prevented", "el arranque se detiene: impedido",
                "启动中止：被阻止", "le démarrage s'arrête : empêché", "başlatma durur: engellendi")
W_MESSEN = ("messen", "measure", "medir", "测量", "mesurer", "ölç")
W_AUFGEZ = ("aufgezeichnet:", "recorded:", "registrado:", "已记录：", "enregistré :", "kaydedildi:")
W_MANDERS = ("Bootloader: anderer Messwert", "boot loader: different measured value", "bootloader: otro valor medido",
             "引导加载程序：测量值不同", "bootloader : autre valeur mesurée", "önyükleyici: farklı ölçüm değeri")
W_MKERNEL = ("Kernel: Messwert", "kernel: measured value", "kernel: valor medido", "内核：测量值", "noyau : valeur mesurée",
             "çekirdek: ölçüm değeri")
W_ERKENNBAR = ("erkennbar", "detectable", "detectable", "可以发现", "détectable", "tespit edilebilir")


def waage_bild(s, x, y, farbe=DUNKEL):
    """Kleine Balkenwaage, Fuß bei (x, y - 0.14); Ergebnis: Liste der ids."""
    return [s.vieleck(None, [(r4(x - 0.09), r4(y - 0.16)), (r4(x + 0.09), r4(y - 0.16)), (r4(x), r4(y - 0.05))], farbe, 1.0, 1),
            linie(s, (x, y - 0.06), (x, y + 0.12), farbe, 2.5), linie(s, (x - 0.22, y + 0.12), (x + 0.22, y + 0.12), farbe, 2.5),
            linie(s, (x - 0.22, y + 0.12), (x - 0.22, y + 0.01), farbe, 1.5), linie(s, (x + 0.22, y + 0.12), (x + 0.22, y + 0.01), farbe, 1.5),
            linie(s, (x - 0.31, y + 0.01), (x - 0.13, y + 0.01), farbe, 2.5), linie(s, (x + 0.13, y + 0.01), (x + 0.31, y + 0.01), farbe, 2.5)]


def k2zweiketten():
    """Zwei Zeilen mit derselben Kette Firmware -> Bootloader -> Kernel. Oben Secure Boot: vor jedem Pfeil eine Schranke
    mit Schloss; der Bootloader ist verändert (rot), die erste Schranke bleibt zu: „Start bricht ab: verhindert“.
    Unten Measured Boot: vor jedem Pfeil eine Waage „messen“, die Ergebnisse fallen in „aufgezeichnet“; der veränderte
    Bootloader läuft weiter, sein Messwert ist anders: „erkennbar“."""
    s = Szene("cyber/k2zweiketten", reihenfolge="anlegen")
    yt, yb = 1.0, -0.5
    titel = [lab(s, "Secure Boot", (-3.4, 1.62), GN, "left", DUNKEL), lab(s, "Measured Boot", (-3.4, 0.08), GN, "left", DUNKEL)]
    reihen = {}
    for name, y in (("t", yt), ("b", yb)):
        fw = kasten(s, (-2.65, y), 1.1, 0.45, W_FW, DUNKEL, GRAU_HELL, GK)
        bl = [box(s, (-0.05, y), 1.2, 0.45, DUNKEL, GRAU_HELL, 2)]
        bl_rot = [box(s, (-0.05, y), 1.2, 0.45, ROT, ROT_HELL, 2.5)]     # unter dem Text; der Text wird rot umgefärbt
        bl.append(lab(s, W_BL, (-0.05, y), GK, "center", SCHWARZ))
        ke = kasten(s, (2.6, y), 1.1, 0.45, W_KERNEL, ORANGE, ORANGE_HELL, GK)
        reihen[name] = dict(fw=fw, bl=bl, bl_rot=bl_rot, ke=ke)
    # oben: Schranken mit Schloss vor jedem Pfeil
    schr = []
    for xs in (-1.1, 1.45):
        schr.append([box(s, (xs, yt - 0.3), 0.12, 0.1, DUNKEL, DUNKEL, 1, "rect"), linie(s, (xs, yt - 0.3), (xs, yt + 0.3), ROT, 6),
                     s.schloss((xs, yt + 0.47), 0.26, False, DUNKEL)])
    a_t = pf(s, (-2.08, yt), (-1.2, yt), DUNKEL, 2.5, 0.1)
    kr_t = kreuz(s, -1.1, yt, 0.2)
    l_verh = lab(s, W_VERHINDERT, (-1.1, yt - 0.5), GK, "center", ROT)
    # unten: Waagen, Aufzeichnung
    waagen = [waage_bild(s, xw, yb - 0.3) for xw in (-1.35, 1.25)]
    l_mess = [lab(s, W_MESSEN, (xw, yb + 0.17), GK, "center", DUNKEL) for xw in (-1.35, 1.25)]
    a_b = [pf(s, (-2.08, yb), (-0.67, yb), DUNKEL, 2.5, 0.1), pf(s, (0.57, yb), (2.03, yb), DUNKEL, 2.5, 0.1)]
    auf = [box(s, (0, -1.45), 5.7, 0.42, DUNKEL, WEISS, 2), lab(s, W_AUFGEZ, (-2.75, -1.45), GK, "left", DUNKEL)]
    e1 = lab(s, W_MANDERS, (-0.55, -1.45), GK, "center", ROT)
    e2 = lab(s, W_MKERNEL, (1.95, -1.45), GK, "center", DUNKEL)
    fall = [pf(s, (-1.35, yb - 0.48), (-0.95, -1.22), GRAU, 2, 0.09, DASH), pf(s, (1.25, yb - 0.48), (1.7, -1.22), GRAU, 2, 0.09, DASH)]
    l_erk = lab(s, W_ERKENNBAR, (-0.55, -1.84), GN, "center", ORANGE)
    t, b = reihen["t"], reihen["b"]
    schritt(s, EIN(titel + t["fw"] + t["bl"] + t["ke"] + b["fw"] + b["bl"] + b["ke"] + flach(schr) + flach(waagen) + l_mess + auf,
                   0.7))
    s.pause(0.5)
    with s.gleichzeitig():
        schritt(s, EIN(t["bl_rot"] + b["bl_rot"], 0.6))
        s.ersetzen(t["bl"][1], W(s, W_BL), farbe=ROT, dauer=0.6)
        s.ersetzen(b["bl"][1], W(s, W_BL), farbe=ROT, dauer=0.6)
    s.pause(0.4)
    schritt(s, ZEICHNE(a_t, 0.6))
    schritt(s, WACHS(kr_t, 0.4), BETONE(schr[0][2], 0.7))
    schritt(s, EIN(l_verh, 0.5))
    s.pause(0.6)
    schritt(s, ZEICHNE(a_b[0], 0.6), BETONE(waagen[0][2], 0.6))
    schritt(s, ZEICHNE(fall[0], 0.5), EIN(e1, 0.5))
    schritt(s, ZEICHNE(a_b[1], 0.6), BETONE(waagen[1][2], 0.6))
    schritt(s, ZEICHNE(fall[1], 0.5), EIN(e2, 0.5))
    schritt(s, EIN(l_erk, 0.5), BETONE(e1, 0.7))
    s.speichern()


W_SPPL = ("Speicherplätze", "storage slots", "posiciones de memoria", "存储位置", "emplacements", "bellek yuvaları")
W_RECHENWERK = ("Rechenwerk", "arithmetic\nunit", "unidad de\ncálculo", "运算单元", "unité de\ncalcul", "hesap\nbirimi")
W_NURBEF = ("nur festgelegte Befehle", "only defined commands", "solo órdenes definidas", "只接受规定的命令",
            "seulement des ordres fixés", "yalnızca tanımlı komutlar")
W_MESSWERT = ("Messwert", "measured value", "valor medido", "测量值", "valeur mesurée", "ölçüm değeri")
W_DIREKT = ("Speicherplatz überschreiben", "overwrite a slot", "sobrescribir una posición", "覆盖存储位置",
            "écraser un emplacement", "yuvanın üzerine yaz")


def k2tpm():
    """Links die Startkette Firmware -> Bootloader -> Kernel, rechts das TPM als abgeschlossener Kasten mit
    Speicherplätzen und Rechenwerk. Jedes Glied schickt einen Messwert durch eine schmale Öffnung („nur festgelegte
    Befehle“); er wird in einem Speicherplatz abgelegt. Ein Programm will einen Speicherplatz direkt überschreiben und
    prallt an der Wand ab."""
    s = Szene("cyber/k2tpm", reihenfolge="anlegen")
    kette = []
    for y, w in ((1.2, W_FW), (0.3, W_BL), (-0.6, W_KERNEL)):
        kette.append(kasten(s, (-2.55, y), 1.5, 0.42, w, ORANGE if w is W_KERNEL else DUNKEL,
                            ORANGE_HELL if w is W_KERNEL else GRAU_HELL, GK))
    kpf = [pf(s, (-2.55, 0.98), (-2.55, 0.53), DUNKEL, 2, 0.09), pf(s, (-2.55, 0.08), (-2.55, -0.37), DUNKEL, 2, 0.09)]
    prog = kasten(s, (-2.55, -1.45), 1.5, 0.42, W_PROGRAMM, BLAU, BLAU_HELL, GK)
    innen = box(s, (1.85, 0.2), 3.1, 2.9, GRAU_HELL, GRAU_HELL, 0, "rect")
    wand = wand_v(s, 0.3, 1.65, -1.25, [(0.55, 0.15)], DUNKEL, 7) + \
        [linie(s, (0.3, 1.65), (3.4, 1.65), DUNKEL, 7), linie(s, (3.4, 1.65), (3.4, -1.25), DUNKEL, 7),
         linie(s, (3.4, -1.25), (0.3, -1.25), DUNKEL, 7)]
    l_tpm = lab(s, "TPM", (3.2, 1.4), GT, "right", DUNKEL)
    l_sppl = lab(s, W_SPPL, (1.2, 1.35), GK, "center", DUNKEL)
    plaetze = [box(s, (1.2, y), 1.3, 0.38, DUNKEL, WEISS, 2, "rect") for y in (0.95, 0.45, -0.05, -0.55)]
    rw = kasten(s, (2.65, 0.2), 1.05, 0.75, W_RECHENWERK, DUNKEL, WEISS, GK)
    wege = [pf(s, (-1.78, y0), (0.22, y1), GRAU, 2, 0.09, DASH) for y0, y1 in ((1.2, 0.47), (0.3, 0.35), (-0.6, 0.23))]
    l_off = [lab(s, W_NURBEF, (0.12, -0.78), GK, "right", DUNKEL), linie(s, (0.17, -0.68), (0.28, 0.12), HELLGRAU, 1.5)]
    chips = [kasten(s, (-1.55, y), 1.05, 0.3, W_MESSWERT, ORANGE, ORANGE_HELL, 17) for y in (1.2, 0.3, -0.6)]
    angr = pf(s, (-1.78, -1.45), (0.2, -1.02), ROT, 2.5, 0.11, DASH)
    l_angr = lab(s, W_DIREKT, (-0.75, -1.5), GK, "center", ROT)
    kr = kreuz(s, 0.3, -1.0, 0.22)
    schritt(s, EIN(flach(kette) + kpf + prog + [innen] + wand + [l_tpm, l_sppl] + plaetze + rw + wege + l_off, 0.7))
    s.pause(0.4)
    for k, c in enumerate(chips):
        schritt(s, EIN(c, 0.3))
        schritt(s, *[ZU(i, 0.3, 0.35, 0.6) for i in c])
        schritt(s, *[ZU(i, 1.2, (0.95, 0.45, -0.05)[k], 0.5) for i in c])
    s.pause(0.5)
    schritt(s, ZEICHNE(angr, 0.6), EIN(l_angr, 0.6))
    schritt(s, WACHS(kr, 0.4), BETONE(wand[3], 0.6))
    s.speichern()


F_K = {"0037": r"00\,\|\,37", "3752": r"37\,\|\,52", "0052": r"00\,\|\,52", "5237": r"52\,\|\,37"}
F_H = {"0037": r"h(00\,37)=37", "3752": r"h(37\,52)=3752-38\cdot97=66", "0052": r"h(00\,52)=52",
       "5237": r"h(52\,37)=5237-53\cdot97=96"}
W_PCR = ("PCR", "PCR", "PCR", "PCR", "PCR", "PCR")
W_MW = {n: ("Messwert %s" % n, "measured value %s" % n, "valor medido %s" % n, "测量值 %s" % n, "valeur mesurée %s" % n,
            "ölçüm değeri %s" % n) for n in ("37", "52")}
W_GLEICHMW = ("gleiche Messwerte, andere Reihenfolge, anderes Ergebnis", "same measured values, different order, different result",
              "mismos valores medidos, otro orden, otro resultado", "测量值相同，顺序不同，结果不同",
              "mêmes valeurs mesurées, autre ordre, autre résultat", "aynı ölçüm değerleri, farklı sıra, farklı sonuç")


def k2rpcr():
    """Rechenbild mit der Spiel-Prüfsumme (Rest bei Division durch 97, Beispiel in 9.5, rechnung_kap2.py): oben PCR 00,
    Messwert 37 -> h(00 37) = 37, Messwert 52 -> h(37 52) = 3752 − 38·97 = 66; unten PCR 00, Messwert 52 -> 52,
    Messwert 37 -> h(52 37) = 5237 − 53·97 = 96. Jeder Schritt als Kasten „alt ‖ neu“ mit Pfeil zum neuen PCR-Wert;
    am Ende 66 ≠ 96 und „gleiche Messwerte, andere Reihenfolge, anderes Ergebnis“."""
    s = Szene("cyber/k2rpcr", reihenfolge="anlegen")
    em = 0.17
    xs = {"p0": -3.05, "k1": -1.85, "p1": -0.6, "k2": 0.6, "p2": 1.85}
    zeilen = (("t", 1.35, ("0037", "3752"), ("00", "37", "66"), ("37", "52")),
              ("b", -0.2, ("0052", "5237"), ("00", "52", "96"), ("52", "37")))
    teile = {}
    for name, y, ks, ps, mws in zeilen:
        pcr = [ttkasten(s, (xs["p%d" % i], y), 0.6, 0.36, ps[i], ORANGE, ORANGE_HELL, TT) for i in range(3)]
        l_pcr = [lab(s, W_PCR, (xs["p%d" % i], y + 0.36), GK, "center", GRAU) for i in range(3)]
        kk = []
        for j, k in enumerate(ks):
            xk = xs["k%d" % (j + 1)]
            hk = formel_hoehe(F_K[k], em, 0.2)
            hh = formel_hoehe(F_H[k], em, 0.2)
            kk.append(dict(rahmen=box(s, (xk, y), 1.1, 0.36, DUNKEL, WEISS, 2),
                           inhalt=s.formel(F_K[k], mitte=(xk, y), hoehe=hk),
                           mw=lab(s, W_MW[mws[j]], (xk, y + 0.36), GK, "center", BLAU),
                           rein=pf(s, (xs["p%d" % j] + 0.32, y), (xk - 0.57, y), DUNKEL, 2.5, 0.09),
                           raus=pf(s, (xk + 0.57, y), (xs["p%d" % (j + 1)] - 0.32, y), DUNKEL, 2.5, 0.09),
                           f=(F_H[k], (xk, y - 0.43), hh)))
        teile[name] = (pcr, l_pcr, kk)
    ungl = lab(s, "≠", (xs["p2"], 0.58), GT, "center", ROT)
    schluss = lab(s, W_GLEICHMW, (0, -1.08), GN, "center", DUNKEL)
    for name in ("t", "b"):
        pcr, l_pcr, kk = teile[name]
        schritt(s, EIN(pcr[0] + [l_pcr[0]], 0.5))
        for j, k in enumerate(kk):
            schritt(s, ZEICHNE(k["rein"], 0.4), EIN([k["rahmen"], k["inhalt"], k["mw"]], 0.5))
            tex, mitte, hh = k["f"]
            s.formel(tex, mitte=mitte, hoehe=hh, zeilenweise=True, dauer=0.8)
            schritt(s, ZEICHNE(k["raus"], 0.4), EIN(pcr[j + 1] + [l_pcr[j + 1]], 0.5))
        s.pause(0.5)
    schritt(s, EIN([ungl, schluss], 0.6), BETONE(teile["t"][0][2] + teile["b"][0][2], 0.8))
    s.speichern()


W_64NULL = ("64 Nullen", "64 zeros", "64 ceros", "64 个零", "64 zéros", "64 sıfır")
W_PSFW = ("‖ Prüfsumme von\nfirmware.txt", "‖ checksum of\nfirmware.txt", "‖ suma de verificación\nde firmware.txt",
          "‖ firmware.txt\n的校验和", "‖ somme de contrôle\nde firmware.txt", "‖ firmware.txt\nsağlama toplamı")
W_PSBL = ("‖ Prüfsumme von\nbootloader.txt", "‖ checksum of\nbootloader.txt", "‖ suma de verificación\nde bootloader.txt",
          "‖ bootloader.txt\n的校验和", "‖ somme de contrôle\nde bootloader.txt", "‖ bootloader.txt\nsağlama toplamı")
W_GLEICHD = ("gleiche Dateien, andere Reihenfolge, anderer Wert", "same files, different order, different value",
             "mismos archivos, otro orden, otro valor", "文件相同，顺序不同，值不同",
             "mêmes fichiers, autre ordre, autre valeur", "aynı dosyalar, farklı sıra, farklı değer")
SITZUNG_SHA = ["$ printf 'firmware' > firmware.txt",
               "$ printf 'bootloader' > bootloader.txt",
               "$ m1=$(sha256sum firmware.txt | cut -c1-64)",
               "$ m2=$(sha256sum bootloader.txt | cut -c1-64)",
               "$ pcr=$(printf '%064d' 0)",
               "$ pcr=$(printf '%s%s' \"$pcr\" \"$m1\" | xxd -r -p | sha256sum | cut -c1-64)",
               "$ echo \"$pcr\"",
               "3e287e57770de15677579228044a2abe6ca7c39d61de4b8a47fd6b7209dd0bab",
               "$ pcr=$(printf '%s%s' \"$pcr\" \"$m2\" | xxd -r -p | sha256sum | cut -c1-64)",
               "$ echo \"$pcr\"",
               "dd54e062881a8ffb7249e72173ab4900d2e947002641f4bb27d9fd99939fd027"]


def k2sha():
    """Oben das Terminal mit der Sitzung aus dem Heftblock 9.5 (mitschrift_kap2.txt; Prompt $ wie im Heft, weil die
    Zeilen 72 Zeichen lang sind); die Zeilen erscheinen nacheinander, das Fenster rollt (7 Zeilen sichtbar), zum Schluss
    sind 3e287e57… und dd54e062… hinterlegt. Darunter zwei Ketten: 64 Nullen ‖ Prüfsumme von firmware.txt -> 3e287e57…
    ‖ Prüfsumme von bootloader.txt -> dd54e062…; umgekehrt 64 Nullen -> … -> e5e9b123… (rechnung_kap2.py). Am Ende
    dd54e062… ≠ e5e9b123…: „gleiche Dateien, andere Reihenfolge, anderer Wert“."""
    s = Szene("cyber/k2sha", reihenfolge="anlegen")
    t = s.terminal(text="", pos=(-3.38, 2.55), spalten=74, zeilen=7, prompt="$ ", titel="student@labor: ~/cyberk2",
                   groesse=20)
    xs, yo, yu = (-2.8, -0.05, 2.7), 0.15, -0.95
    ketten = []
    for y, werte, worte, farbe in ((yo, ("3e287e57…", "dd54e062…"), (W_PSFW, W_PSBL), BLAU),
                                   (yu, ("…", "e5e9b123…"), (W_PSBL, W_PSFW), LILA)):
        k = [kasten(s, (xs[0], y), 1.15, 0.4, W_64NULL, DUNKEL, WEISS, GK)]
        for j in range(2):
            k.append([pf(s, (xs[j] + 0.6, y), (xs[j + 1] - 0.6, y), farbe, 2.5, 0.1),
                      lab(s, worte[j], ((xs[j] + xs[j + 1]) / 2, y + 0.3), 17, "center", farbe)] +
                     ttkasten(s, (xs[j + 1], y), 1.15, 0.4, werte[j], farbe, WEISS, TK, farbe))
        ketten.append(k)
    ungl = lab(s, "≠", (xs[2], (yo + yu) / 2), GT, "center", ROT)
    schluss = lab(s, W_GLEICHD, (0, -1.45), GN, "center", DUNKEL)
    mk = [t.markieren(2, 0, 63, ORANGE, 0.35), t.markieren(5, 0, 63, ORANGE, 0.35)]
    schritt(s, EIN(t.id, 0.5))
    for z in SITZUNG_SHA[:5]:
        t.ausgabe(z, dauer=0.35)
    for z in SITZUNG_SHA[5:]:
        t.ausgabe(z, dauer=0.5)
    t.schritt("$ ", dauer=0.3)
    schritt(s, EIN(mk, 0.5))
    s.pause(0.5)
    for k in ketten:
        schritt(s, EIN(k[0], 0.4))
        for teil in k[1:]:
            schritt(s, ZEICHNE(teil[0], 0.4), EIN(teil[1:], 0.5))
        s.pause(0.3)
    schritt(s, EIN([ungl, schluss], 0.6), BETONE(ketten[0][2][2:] + ketten[1][2][2:], 0.8))
    s.speichern()


W_PROTOKOLL = ("Ereignisprotokoll", "event log", "registro de eventos", "事件日志", "journal des événements", "olay günlüğü")
W_FW37 = ("Firmware, Messwert 37", "firmware, measured value 37", "firmware, valor medido 37", "固件，测量值 37",
          "firmware, valeur mesurée 37", "ürün yazılımı, ölçüm değeri 37")
W_BL52 = ("Bootloader, Messwert 52", "boot loader, measured value 52", "bootloader, valor medido 52", "引导加载程序，测量值 52",
          "bootloader, valeur mesurée 52", "önyükleyici, ölçüm değeri 52")
W_RECHNET = ("Prüfer rechnet nach", "checker recalculates", "el verificador recalcula", "检查者重新计算",
             "le contrôleur recalcule", "denetleyici yeniden hesaplar")
W_ECHT = ("Protokoll echt", "log genuine", "registro auténtico", "日志真实", "journal authentique", "günlük gerçek")
W_PASSTNICHT = ("Protokoll passt nicht, eine Messung fehlt", "log does not match, a measurement is missing",
                "el registro no coincide, falta una medición", "日志不符，缺少一次测量",
                "le journal ne correspond pas, une mesure manque", "günlük uyuşmuyor, bir ölçüm eksik")


def k2protokoll():
    """Zwei Fassungen untereinander. Links das Ereignisprotokoll (Firmware, Messwert 37; Bootloader, Messwert 52), in
    der Mitte rechnet der Prüfer mit der Spiel-Prüfsumme nach (00 -> 37 -> 66), rechts das TPM mit dem PCR-Wert. Oben
    PCR 66: gleich, Häkchen „Protokoll echt“. Unten PCR 85 (Bootkit 81: h(66 81) = 85): ungleich, Kreuz „Protokoll passt
    nicht, eine Messung fehlt“."""
    s = Szene("cyber/k2protokoll", reihenfolge="anlegen")
    teile = []
    for y, pcr in ((0.85, "66"), (-0.75, "85")):
        prot = [box(s, (-2.35, y), 2.2, 0.78, DUNKEL, WEISS, 2), lab(s, W_PROTOKOLL, (-2.35, y + 0.22), GK, "center", DUNKEL),
                lab(s, W_FW37, (-3.35, y - 0.03), GK, "left", SCHWARZ), lab(s, W_BL52, (-3.35, y - 0.25), GK, "left", SCHWARZ)]
        tpm = [box(s, (2.65, y), 1.5, 0.78, DUNKEL, GRAU_HELL, 2), lab(s, "TPM", (2.65, y + 0.2), GK, "center", DUNKEL),
               tt(s, "PCR: " + pcr, (2.65, y - 0.13), TT, "center", ORANGE)]
        l_r = lab(s, W_RECHNET, (0.0, y + 0.33), GK, "center", DUNKEL)
        rech = [ttkasten(s, (-0.72 + 0.72 * i, y), 0.46, 0.34, v, ORANGE, ORANGE_HELL, TT) for i, v in enumerate(("00", "37", "66"))]
        rpf = [pf(s, (-0.72 + 0.72 * i + 0.24, y), (-0.72 + 0.72 * (i + 1) - 0.24, y), DUNKEL, 2.5, 0.08) for i in range(2)]
        teile.append(dict(prot=prot, tpm=tpm, l_r=l_r, rech=rech, rpf=rpf, y=y))
    ob, un = teile
    gl = lab(s, "=", (1.43, ob["y"]), GT, "center", GRUEN)
    hk = haken(s, 1.43, ob["y"] + 0.33, 0.2)
    l_echt = lab(s, W_ECHT, (1.43, ob["y"] - 0.5), GK, "center", GRUEN)
    ngl = lab(s, "≠", (1.43, un["y"]), GT, "center", ROT)
    kr = kreuz(s, 1.43, un["y"] + 0.33, 0.2)
    l_nicht = lab(s, W_PASSTNICHT, (0.4, un["y"] - 0.55), GK, "center", ROT)
    for tl in teile:
        schritt(s, EIN(tl["prot"] + tl["tpm"], 0.6))
        schritt(s, EIN([tl["l_r"]] + tl["rech"][0], 0.4))
        for i in range(2):
            schritt(s, ZEICHNE(tl["rpf"][i], 0.3), EIN(tl["rech"][i + 1], 0.4))
        if tl is ob:
            schritt(s, EIN(gl, 0.4), WACHS(hk, 0.4), EIN(l_echt, 0.5))
        else:
            schritt(s, EIN(ngl, 0.4), WACHS(kr, 0.4), EIN(l_nicht, 0.5))
        s.pause(0.6)
    s.speichern()


# ================================================================== Abschnitt 10: Das TPM
W_DISKRET = ("Diskret", "discrete", "discreto", "独立式", "discret", "ayrık")
W_INTEGRIERT = ("Integriert", "integrated", "integrado", "集成式", "intégré", "tümleşik")
W_FWTPM = ("Firmware-TPM", "firmware TPM", "TPM de firmware", "固件 TPM", "TPM firmware", "ürün yazılımı TPM")
W_SWTPM = ("Software-TPM", "software TPM", "TPM de software", "软件 TPM", "TPM logiciel", "yazılım TPM")
W_HAUPTPL = ("Hauptplatine", "mainboard", "placa base", "主板", "carte mère", "anakart")
W_ABGESCH = ("abgeschottet:\nTPM-Programm", "isolated:\nTPM program", "aislado:\nprograma TPM", "隔离区：\nTPM 程序",
             "isolé :\nprogramme TPM", "yalıtılmış:\nTPM programı")
W_TPMPROG = ("TPM-Programm", "TPM program", "programa TPM", "TPM 程序", "programme TPM", "TPM programı")
W_SCHUTZ = ("Schutz des TPM selbst", "protection of the TPM itself", "protección del propio TPM", "TPM 自身的保护",
            "protection du TPM lui-même", "TPM'in kendi korunması")
W_HOCH = ("hoch", "high", "alta", "高", "élevée", "yüksek")
W_NIEDRIG = ("niedrig", "low", "baja", "低", "faible", "düşük")


def k2bauformen():
    """Vier Kästen nebeneinander: Diskret (eigener Chip auf der Hauptplatine, sichtbare Leitung zum Prozessor),
    Integriert (Block im Prozessorchip), Firmware-TPM (Programm in einem abgeschotteten Bereich des Prozessors),
    Software-TPM (Programm neben Programmen). Darunter ein Keil „Schutz des TPM selbst“, links hoch, rechts niedrig."""
    s = Szene("cyber/k2bauformen", reihenfolge="anlegen")
    xs, yp = (-2.6, -0.87, 0.87, 2.6), 0.55
    paneele = []
    for x, w in zip(xs, (W_DISKRET, W_INTEGRIERT, W_FWTPM, W_SWTPM)):
        paneele.append([box(s, (x, yp), 1.65, 1.7, HELLGRAU, WEISS, 1.5, "rect"), lab(s, w, (x, 1.62), GN, "center", DUNKEL)])
    x = xs[0]
    paneele[0] += [box(s, (x, yp - 0.05), 1.45, 1.4, GRUEN, GRUEN_HELL, 1.5, "rect"),
                   lab(s, W_HAUPTPL, (x, yp - 0.6), 17, "center", GRUEN)]
    paneele[0] += kasten(s, (x - 0.28, yp + 0.25), 0.82, 0.55, W_PROZESSOR, DUNKEL, GRAU_HELL, 17)
    paneele[0] += [linie(s, (x + 0.13, yp + 0.12), (x + 0.42, yp + 0.12), ORANGE, 3.5),
                   linie(s, (x + 0.42, yp + 0.12), (x + 0.42, yp - 0.07), ORANGE, 3.5)]
    paneele[0] += ttkasten(s, (x + 0.42, yp - 0.22), 0.5, 0.3, "TPM", ORANGE, ORANGE_HELL, 17, ORANGE)
    x = xs[1]
    paneele[1] += [box(s, (x, yp - 0.05), 1.35, 1.3, DUNKEL, GRAU_HELL, 2, "rect"),
                   lab(s, W_PROZESSOR, (x, yp + 0.4), 17, "center", DUNKEL)]
    paneele[1] += ttkasten(s, (x + 0.3, yp - 0.3), 0.5, 0.3, "TPM", ORANGE, ORANGE_HELL, 17, ORANGE)
    x = xs[2]
    paneele[2] += [box(s, (x, yp - 0.05), 1.35, 1.3, DUNKEL, GRAU_HELL, 2, "rect"),
                   lab(s, W_PROZESSOR, (x, yp + 0.4), 17, "center", DUNKEL)]
    paneele[2] += kasten(s, (x, yp - 0.25), 1.15, 0.55, W_ABGESCH, ORANGE, WEISS, 17, ORANGE, 2, "round", DASH)
    x = xs[3]
    for k, y in enumerate((yp + 0.4, yp, yp - 0.4)):
        if k == 1:
            paneele[3] += kasten(s, (x, y), 1.4, 0.3, W_TPMPROG, ORANGE, ORANGE_HELL, 17, ORANGE)
        else:
            paneele[3] += kasten(s, (x, y), 1.4, 0.3, W_PROGRAMM, BLAU, BLAU_HELL, 17, BLAU)
    keil = s.vieleck(None, [(-3.4, -0.5), (3.4, -0.5), (3.4, -0.57), (-3.4, -0.9)], GRUEN, 0.8, 0)
    l_keil = [lab(s, W_SCHUTZ, (0, -1.1), GN, "center", DUNKEL), lab(s, W_HOCH, (-3.4, -1.1), GK, "left", GRUEN),
              lab(s, W_NIEDRIG, (3.4, -1.1), GK, "right", GRUEN)]
    for p in paneele:
        schritt(s, EIN(p, 0.5))
        s.pause(0.3)
    schritt(s, EIN([keil] + l_keil, 0.7))
    s.speichern()


W_START1 = ("Erster Start", "first boot", "primer arranque", "第一次启动", "premier démarrage", "ilk başlatma")
W_START2 = ("Zweiter Start, mit Bootkit", "second boot, with bootkit", "segundo arranque, con bootkit",
            "第二次启动，带 bootkit", "second démarrage, avec bootkit", "ikinci başlatma, bootkit ile")
W_MWERTE = ("Messwerte", "measured values", "valores medidos", "测量值", "valeurs mesurées", "ölçüm değerleri")
W_TRESOR = ("Tresor", "safe", "caja fuerte", "保险箱", "coffre", "kasa")
W_WIN = ("Windows fragt nach dem\nWiederherstellungsschlüssel", "Windows asks for\nthe recovery key",
         "Windows pide\nla clave de recuperación", "Windows 要求输入\n恢复密钥", "Windows demande\nla clé de récupération",
         "Windows kurtarma\nanahtarını ister")


def k2versiegeln():
    """Zwei Starts untereinander. Im TPM ein Tresor mit Schloss „PCR = 66“ und einem Schlüssel. Erster Start: Messwerte
    37, 52; das PCR geht 00 -> 37 -> 66, das Schloss öffnet sich, der Schlüssel kommt heraus. Zweiter Start mit Bootkit:
    37, 52, 81; das PCR geht bis 85, das Schloss bleibt zu, der Schlüssel bleibt drin, Windows fragt nach dem
    Wiederherstellungsschlüssel (Spiel-Prüfsumme aus 9.5)."""
    s = Szene("cyber/k2versiegeln", reihenfolge="anlegen")
    reihen = []
    for y, titel, mw, pcrs in ((0.85, W_START1, ("37", "52"), ("37", "66")),
                               (-0.95, W_START2, ("37", "52", "81"), ("37", "66", "85"))):
        r = dict(y=y, pcrs=pcrs)
        r["titel"] = lab(s, titel, (-3.4, y + 0.62), GN, "left", DUNKEL)
        r["l_mw"] = lab(s, W_MWERTE, (-2.8, y + 0.3), 17, "center", BLAU)
        r["chips"] = [ttkasten(s, (-3.2 + 0.45 * i, y), 0.4, 0.32, v, ROT if v == "81" else BLAU,
                               ROT_HELL if v == "81" else BLAU_HELL, TK, ROT if v == "81" else BLAU) for i, v in enumerate(mw)]
        r["tpm"] = [box(s, (-0.12, y), 2.95, 1.1, DUNKEL, GRAU_HELL, 2, "rect"), lab(s, "TPM", (-1.52, y + 0.4), GK, "left", DUNKEL)]
        r["pfeil"] = pf(s, (-1.98, y), (-1.62, y), DUNKEL, 2.5, 0.09)
        r["pcr_k"] = box(s, (-1.0, y - 0.05), 0.9, 0.36, ORANGE, WEISS, 2)
        r["pcr_t"] = tt(s, "PCR 00", (-1.0, y - 0.05), TK, "center", ORANGE)
        r["tresor"] = [box(s, (0.55, y - 0.05), 1.4, 0.82, DUNKEL, WEISS, 3, "rect"),
                       lab(s, W_TRESOR, (-0.07, y + 0.22), 17, "left", DUNKEL),
                       tt(s, "PCR = 66", (0.82, y + 0.22), 17, "center", ORANGE)]
        r["zu"] = s.schloss((1.25, y - 0.12), 0.34, False, DUNKEL)
        r["key"] = schluessel_bild(s, 0.35, y - 0.17, ORANGE)
        reihen.append(r)
    r1, r2 = reihen
    auf = s.schloss((1.25, r1["y"] - 0.12), 0.34, True, GRUEN)
    hk = haken(s, 3.0, r1["y"] - 0.17, 0.22)
    kr = kreuz(s, 0.92, r2["y"] - 0.12, 0.16)
    win = kasten(s, (2.45, r2["y"] - 0.05), 1.95, 0.62, W_WIN, BLAU, BLAU_HELL, GK)
    for r in reihen:
        schritt(s, EIN([r["titel"], r["l_mw"]] + r["tpm"] + [r["pfeil"], r["pcr_k"], r["pcr_t"]] + r["tresor"] + [r["zu"]] +
                    r["key"], 0.6))
        for i, c in enumerate(r["chips"]):
            schritt(s, EIN(c, 0.4))
            s.ersetzen(r["pcr_t"], "PCR " + r["pcrs"][i], dauer=0.5)
        if r is r1:
            schritt(s, BETONE(r["tresor"][2], 0.7))
            schritt(s, AUS(r["zu"], 0.4), EIN(auf, 0.4))
            schritt(s, *VERS(r["key"], 2.0, 0, 0.8))
            schritt(s, WACHS(hk, 0.4))
        else:
            schritt(s, BETONE(r["tresor"][2], 0.7), WACHS(kr, 0.4))
            schritt(s, EIN(win, 0.6))
        s.pause(0.6)
    s.speichern()


W_BOOTMGR = ("Bootmanager\nvon Windows", "Windows\nboot manager", "gestor de arranque\nde Windows", "Windows\n启动管理器",
             "gestionnaire de\ndémarrage Windows", "Windows\nönyükleme yöneticisi")
W_LADEPROG = ("Ladeprogramm", "loader", "cargador", "加载程序", "chargeur", "yükleyici")
W_ANFANG = ("Anfang", "start", "inicio", "起始", "début", "başlangıç")
W_GEHEIM = ("BitLocker-Geheimnis", "BitLocker secret", "secreto de BitLocker", "BitLocker 机密", "secret BitLocker",
            "BitLocker sırrı")
W_ZWEITES = ("zweites Ladeprogramm", "second loader", "segundo cargador", "第二个加载程序", "second chargeur",
             "ikinci yükleyici")
W_FRAGT = ("fragt nach dem Geheimnis", "asks for the secret", "pide el secreto", "索要机密", "demande le secret",
           "sırrı ister")
W_RUECKW = ("rückwärts:\nblockiert", "backwards:\nblocked", "hacia atrás:\nbloqueado", "反向：\n被卡住", "en arrière :\nbloqué",
            "geri:\nengelli")
W_NEUSTART = ("erst ein Neustart setzt PCR 11 zurück", "only a restart resets PCR 11", "solo un reinicio restablece PCR 11",
              "只有重新启动才会重置 PCR 11", "seul un redémarrage remet PCR 11 à zéro", "PCR 11'i yalnızca yeniden başlatma sıfırlar")


def zahnrad_bild(s, mx, my, R=0.45, r=0.34, n=10, farbe=DUNKEL):
    """Sperrrad mit n Sägezähnen um (mx, my); Ergebnis: id des Vielecks."""
    import math
    p = []
    for k in range(n):
        a = 2 * math.pi * k / n
        p.append((mx + r * math.cos(a), my + r * math.sin(a)))
        p.append((mx + R * math.cos(a + 0.02), my + R * math.sin(a + 0.02)))
    return s.vieleck(None, [(r4(a), r4(b)) for a, b in p], GRAU_HELL, 1.0, 2.5, farbe)


def k2sperrklinke():
    """Zeitleiste: Firmware, Bootmanager von Windows, Ladeprogramm, Windows. Im TPM PCR 11 als Sperrrad mit Klinke, Zeiger
    auf „Anfang“. Während der Bootmanager läuft, wandert das BitLocker-Geheimnis (Schlüssel) zu ihm. Bei der Übergabe an
    das Ladeprogramm dreht das Rad eine Raste weiter. Ein zweites Ladeprogramm fragt nach dem Geheimnis: Kreuz.
    Rückwärtsdrehen ist blockiert; erst ein Neustart setzt PCR 11 zurück."""
    s = Szene("cyber/k2sperrklinke", reihenfolge="anlegen")
    yz = 1.5
    fw = kasten(s, (-2.8, yz), 1.15, 0.55, W_FW, DUNKEL, GRAU_HELL, GK)
    bm = kasten(s, (-0.95, yz), 1.75, 0.55, W_BOOTMGR, DUNKEL, GRAU_HELL, 17)
    lp = kasten(s, (0.9, yz), 1.3, 0.55, W_LADEPROG, DUNKEL, GRAU_HELL, GK)
    wi = kasten(s, (2.75, yz), 1.15, 0.55, "Windows", BLAU, BLAU_HELL, GK)
    p1 = pf(s, (-2.21, yz), (-1.84, yz), DUNKEL, 2.5, 0.09)
    p2 = pf(s, (-0.06, yz), (0.24, yz), DUNKEL, 2.5, 0.09)
    p3 = pf(s, (1.56, yz), (2.16, yz), DUNKEL, 2.5, 0.09)
    gx, gy = -1.55, -0.55
    tpm = [box(s, (-1.15, -0.5), 2.7, 1.65, DUNKEL, WEISS, 2, "rect"), lab(s, "TPM", (-2.4, 0.15), GK, "left", DUNKEL)]
    rad = zahnrad_bild(s, gx, gy)
    zeiger = linie(s, (gx, gy), (gx, gy + 0.3), ORANGE, 4)
    nabe = s.kreis(None, gx, gy, 0.06, farbe=DUNKEL, dicke=2, fuellung=DUNKEL, deckung=1.0)
    marke = [linie(s, (gx, gy + 0.5), (gx, gy + 0.6), ORANGE, 2.5), lab(s, W_ANFANG, (gx, gy + 0.72), 17, "center", ORANGE)]
    klinke = [linie(s, (gx + 0.7, gy + 0.38), (gx + 0.27, gy + 0.27), DUNKEL, 5),
              s.kreis(None, r4(gx + 0.7), r4(gy + 0.38), 0.06, farbe=DUNKEL, dicke=2, fuellung=WEISS, deckung=1.0)]
    l_pcr = lab(s, "PCR 11", (gx, gy - 0.63), GK, "center", DUNKEL)
    key = schluessel_bild(s, -0.35, -0.75, ORANGE)
    l_key = lab(s, W_GEHEIM, (-0.35, -1.0), 17, "center", ORANGE)
    dy_k = 0.97 - (-0.75)
    zw = kasten(s, (2.35, 0.2), 1.9, 0.42, W_ZWEITES, ROT, ROT_HELL, GK, ROT)
    frage = pf(s, (1.38, 0.15), (0.2, -0.35), ROT, 2.5, 0.11, DASH)
    kr_f = kreuz(s, 0.12, -0.38, 0.2)
    l_frage = lab(s, W_FRAGT, (2.35, -0.17), GK, "center", ROT)
    rueck = s.weg(None, "%s+0.62*cos(t)" % gx, "%s+0.62*sin(t)" % gy, 2.5, 3.75, farbe=ROT, dicke=2.5, pfeile="0.97", n=31,
                  dash=DASH, spitze=0.12)
    kr_r = kreuz(s, gx - 0.62, gy + 0.03, 0.16)
    l_rueck = lab(s, W_RUECKW, (-2.95, -0.2), 17, "center", ROT)
    l_neu = lab(s, W_NEUSTART, (1.85, -1.0), GK, "center", DUNKEL)
    schritt(s, EIN(fw + bm + lp + wi + [p1] + tpm + [rad, zeiger, nabe] + marke + klinke + [l_pcr] + key + [l_key], 0.7))
    s.pause(0.4)
    schritt(s, BETONE(bm, 0.7))
    schritt(s, *VERS(key + [l_key], -0.6, dy_k, 0.9))
    s.pause(0.5)
    schritt(s, ZEICHNE(p2, 0.5), DREH(rad, -36, (gx, gy), 0.8), DREH(zeiger, -36, (gx, gy), 0.8), BETONE(klinke[0], 0.8))
    schritt(s, ZEICHNE(p3, 0.4))
    s.pause(0.4)
    schritt(s, EIN(zw, 0.5))
    schritt(s, ZEICHNE(frage, 0.6), EIN(l_frage, 0.6))
    schritt(s, WACHS(kr_f, 0.4))
    s.pause(0.4)
    schritt(s, ZEICHNE(rueck, 0.6))
    schritt(s, WACHS(kr_r, 0.4), EIN(l_rueck, 0.5))
    schritt(s, EIN(l_neu, 0.6))
    s.speichern()


W_RECHNER = ("Rechner", "computer", "equipo", "计算机", "ordinateur", "bilgisayar")
W_ZUFALL = ("Zufallszahl 4711", "random number 4711", "número aleatorio 4711", "随机数 4711", "nombre aléatoire 4711",
            "rastgele sayı 4711")
W_PCRW = ("PCR-Werte", "PCR values", "valores PCR", "PCR 值", "valeurs PCR", "PCR değerleri")
W_ASCHL = ("Attestierungsschlüssel", "attestation key", "clave de atestación", "证明密钥", "clé d'attestation",
           "tasdik anahtarı")
W_BESCH = ("Bescheinigung", "quote", "constancia", "证明", "attestation", "belge")
W_BESCH_PROT = ("Bescheinigung + Protokoll", "quote + log", "constancia + registro", "证明 + 日志", "attestation + journal",
                "belge + günlük")
W_SIEGELPR = ("Siegel prüfen", "check the seal", "comprobar el sello", "检查签章", "vérifier le sceau", "mührü denetle")
W_NACHR = ("Protokoll nachrechnen", "recalculate the log", "recalcular el registro", "重新计算日志", "recalculer le journal",
           "günlüğü yeniden hesapla")
W_GUTE = ("Liste guter Werte", "list of good values", "lista de valores buenos", "良好值列表", "liste des bonnes valeurs",
          "iyi değerler listesi")
W_ALTB = ("alte Bescheinigung: 1234", "old quote: 1234", "constancia antigua: 1234", "旧证明：1234",
          "ancienne attestation : 1234", "eski belge: 1234")
W_ODER = ("oder", "or", "o", "或", "ou", "veya")


def k2attest():
    """Links der Prüfer, rechts der Rechner mit TPM und Ereignisprotokoll. (1) Zufallszahl 4711 zum Rechner; (2) im TPM
    werden PCR-Werte und 4711 zur Bescheinigung, Siegel mit dem Attestierungsschlüssel; (3) Bescheinigung + Protokoll
    zurück, der Prüfer prüft Siegel, rechnet nach, vergleicht mit der Liste guter Werte: Häkchen oder Kreuz; (4) ein
    Bootkit schickt eine alte Bescheinigung mit 1234: 1234 ≠ 4711, abgelehnt."""
    s = Szene("cyber/k2attest", reihenfolge="anlegen")
    pr = [box(s, (-2.4, 0.1), 2.1, 3.0, DUNKEL, WEISS, 2, "rect"), lab(s, W_PRUEFER, (-2.4, 1.4), GN, "center", DUNKEL)]
    zuf = kasten(s, (-2.4, 1.02), 1.75, 0.32, W_ZUFALL, BLAU, BLAU_HELL, GK)
    liste = []
    for y, w in ((0.45, W_SIEGELPR), (0.15, W_NACHR), (-0.15, W_GUTE)):
        liste.append([lab(s, w, (-3.3, y), GK, "left", DUNKEL), haken(s, -1.55, y, 0.15)])
    ergebnis = [haken(s, -2.85, -0.5, 0.17), lab(s, W_ODER, (-2.45, -0.5), GK, "center", DUNKEL), kreuz(s, -2.05, -0.5, 0.15)]
    ungl = lab(s, "1234 ≠ 4711", (-2.4, -0.92), GN, "center", ROT)
    abgel = [kreuz(s, -3.0, -1.22, 0.15), lab(s, W_ABGELEHNT, (-2.8, -1.22), GK, "left", ROT)]
    re = [box(s, (2.4, 0.1), 2.1, 3.0, DUNKEL, WEISS, 2, "rect"), lab(s, W_RECHNER, (2.4, 1.4), GN, "center", DUNKEL)]
    tpm = [box(s, (2.4, 0.55), 1.85, 1.25, ORANGE, ORANGE_HELL, 2, "rect"), lab(s, "TPM", (1.6, 1.0), GK, "left", ORANGE)]
    pcrw = kasten(s, (2.0, 0.72), 0.95, 0.3, W_PCRW, DUNKEL, WEISS, 17)
    z4711 = ttkasten(s, (2.9, 0.72), 0.6, 0.3, "4711", BLAU, BLAU_HELL, 17, BLAU)
    besch = kasten(s, (2.25, 0.33), 1.35, 0.3, W_BESCH, DUNKEL, WEISS, 17)
    sg = s.kreis(None, 3.08, 0.33, 0.13, farbe=ORANGE, dicke=2, fuellung=ORANGE, deckung=1.0)
    l_asch = lab(s, W_ASCHL, (2.4, 0.05), 17, "center", ORANGE)
    prot = kasten(s, (2.4, -0.45), 1.85, 0.38, W_PROTOKOLL, DUNKEL, WEISS, GK)
    bk = kasten(s, (2.4, -1.1), 1.85, 0.38, "Bootkit", ROT, ROT_HELL, GK, ROT)
    n2 = nummer(s, 2.15, 1.0, 2)
    m1 = [pf(s, (-1.33, 1.02), (1.33, 1.02), BLAU, 2.5, 0.11), lab(s, "4711", (0.0, 1.2), GK, "center", BLAU)] + nummer(s, -0.5, 1.2, 1)
    m3 = [pf(s, (1.33, -0.25), (-1.33, -0.25), DUNKEL, 2.5, 0.11), lab(s, W_BESCH_PROT, (0.1, -0.07), GK, "center", DUNKEL)] + \
        nummer(s, -1.1, -0.07, 3)
    m4 = [pf(s, (1.33, -1.1), (-1.33, -1.1), ROT, 2.5, 0.11, DASH), lab(s, W_ALTB, (0.1, -0.92), GK, "center", ROT)] + \
        nummer(s, -1.1, -0.92, 4, ROT)
    schritt(s, EIN(pr + re + tpm + pcrw + prot, 0.7))
    s.pause(0.4)
    schritt(s, EIN(zuf, 0.5))
    schritt(s, ZEICHNE(m1[0], 0.6), EIN(m1[1:], 0.5))
    schritt(s, EIN(z4711, 0.4))
    s.pause(0.4)
    schritt(s, EIN(n2, 0.4), BETONE(pcrw + z4711, 0.7))
    schritt(s, EIN(besch, 0.5), WACHS(sg, 0.5), EIN(l_asch, 0.5))
    s.pause(0.4)
    schritt(s, ZEICHNE(m3[0], 0.6), EIN(m3[1:], 0.5))
    for item in liste:
        schritt(s, EIN(item[0], 0.35), WACHS(item[1], 0.35))
    schritt(s, EIN(ergebnis, 0.5))
    s.pause(0.6)
    schritt(s, EIN(bk, 0.5))
    schritt(s, ZEICHNE(m4[0], 0.6), EIN(m4[1:], 0.5))
    schritt(s, EIN(ungl, 0.5))
    schritt(s, EIN(abgel, 0.5))
    s.speichern()


W_DTPM = ("diskretes TPM", "discrete TPM", "TPM discreto", "独立式 TPM", "TPM discret", "ayrık TPM")
W_PINTPM = ("TPM mit PIN", "TPM with PIN", "TPM con PIN", "带 PIN 的 TPM", "TPM avec PIN", "PIN'li TPM")
W_ITPM = ("integriertes TPM", "integrated TPM", "TPM integrado", "集成式 TPM", "TPM intégré", "tümleşik TPM")
W_AUFZ = ("zeichnet auf", "records", "graba", "记录下来", "enregistre", "kaydeder")
W_NICHTS = ("zeichnet nichts auf", "records nothing", "no graba nada", "什么也记录不到", "n'enregistre rien", "hiçbir şey kaydetmez")
W_WARTETPIN = ("wartet auf die PIN", "waits for the PIN", "espera el PIN", "等待 PIN", "attend le PIN", "PIN'i bekler")
W_KEINANS = ("kein\nAnsatzpunkt", "nothing to\nclip onto", "ningún punto\nde acceso", "无处下手", "aucun point\nd'accès",
             "bağlanacak\nyer yok")


def klemme_bild(s, x, y, farbe=ROT):
    """Klemme (zwei Backen) mit Spitze bei (x, y), Kabel nach unten bis y - 0.2; Ergebnis: Liste der ids."""
    return [linie(s, (x - 0.09, y - 0.14), (x - 0.02, y), farbe, 3), linie(s, (x + 0.09, y - 0.14), (x + 0.02, y), farbe, 3),
            linie(s, (x - 0.09, y - 0.14), (x + 0.09, y - 0.14), farbe, 3), linie(s, (x, y - 0.14), (x, y - 0.22), farbe, 2)]


def k2bus():
    """Drei Fassungen untereinander, je eine Hauptplatine. (1) Diskretes TPM mit sichtbarer Leitung zum Prozessor: Der
    Schlüssel wandert über die Leitung, die Klemme mit Aufzeichnungsgerät zeichnet ihn auf (rot). (2) TPM mit PIN: Der
    Schlüssel bleibt im TPM, bis die PIN eingegeben ist; die Klemme zeichnet nichts auf. (3) Integriertes TPM: Die
    Leitung liegt im Prozessorchip, die Klemme findet keinen Ansatzpunkt."""
    s = Szene("cyber/k2bus", reihenfolge="anlegen")
    ys = (1.25, 0.05, -1.15)
    titel = [lab(s, w, (-3.4, y), GN, "left", DUNKEL) for w, y in zip((W_DTPM, W_PINTPM, W_ITPM), ys)]
    platinen = [box(s, (0.1, y), 4.2, 1.0, GRUEN, GRUEN_HELL, 1.5, "rect") for y in ys]
    reihe = []
    for y in ys[:2]:
        r = dict(tpm=[box(s, (-1.35, y + 0.12), 0.8, 0.6, ORANGE, ORANGE_HELL, 2), tt(s, "TPM", (-1.35, y + 0.3), TK, "center", ORANGE)],
                 cpu=kasten(s, (1.6, y + 0.12), 1.15, 0.45, W_PROZESSOR, DUNKEL, GRAU_HELL, GK),
                 leit=linie(s, (-0.95, y + 0.12), (1.02, y + 0.12), ORANGE, 3.5),
                 klemme=klemme_bild(s, 0.0, y + 0.12),
                 geraet=[box(s, (0.0, y - 0.24), 0.5, 0.24, ROT, WEISS, 2, "rect"),
                         s.kreis(None, -0.13, r4(y - 0.24), 0.045, farbe=ROT, dicke=0, fuellung=ROT, deckung=1.0)],
                 key=schluessel_bild(s, -1.33, y + 0.02, ORANGE, 0.8))
        reihe.append(r)
    r1, r2 = reihe
    kopie = schluessel_bild(s, 0.08, ys[0] - 0.24, ROT, 0.6)
    l_aufz = lab(s, W_AUFZ, (0.35, ys[0] - 0.24), GK, "left", ROT)
    l_pin = lab(s, W_WARTETPIN, (-1.35, ys[1] - 0.3), 17, "center", ORANGE)
    l_nichts = lab(s, W_NICHTS, (0.35, ys[1] - 0.24), GK, "left", DUNKEL)
    y3 = ys[2]
    cpu3 = [box(s, (0.3, y3), 2.8, 0.75, DUNKEL, GRAU_HELL, 2, "rect"), lab(s, W_PROZESSOR, (-1.0, y3 + 0.24), 17, "left", DUNKEL)]
    innen3 = ttkasten(s, (-0.6, y3 - 0.1), 0.6, 0.34, "TPM", ORANGE, ORANGE_HELL, TK, ORANGE) + \
        [linie(s, (-0.3, y3 - 0.1), (0.75, y3 - 0.1), ORANGE, 3)] + \
        kasten(s, (1.2, y3 - 0.1), 0.9, 0.34, W_KERN, DUNKEL, WEISS, 17)
    klemme3 = klemme_bild(s, 2.85, y3 + 0.2)
    kr3 = kreuz(s, 2.85, y3 + 0.37, 0.15)
    l_kein = lab(s, W_KEINANS, (2.85, y3 - 0.27), 17, "center", ROT)
    schritt(s, EIN(titel + platinen + flach([[r["tpm"], r["cpu"], r["leit"], r["klemme"], r["geraet"], r["key"]] for r in reihe]) +
                   cpu3 + innen3 + klemme3, 0.7))
    s.pause(0.5)
    schritt(s, *VERS(r1["key"], 2.0, 0, 1.2))
    schritt(s, EIN(kopie + [l_aufz], 0.5), BETONE(r1["geraet"][0], 0.6))
    s.pause(0.6)
    schritt(s, EIN(l_pin, 0.5), BETONE(r2["key"], 0.7))
    schritt(s, EIN(l_nichts, 0.5))
    s.pause(0.6)
    schritt(s, WACHS(kr3, 0.4), EIN(l_kein, 0.5))
    s.speichern()


SZENEN = (k2grenze, k2shadow, k2monitor, k2schichten, k2adressen, k2zyklus, k2vonneumann, k2datenbefehle, k2cpl, k2root,
          k2ringe, k2ausnahme, k2einsprung, k2dreiwege, k2rueckkehr, k2argumente, k2einzigetuer, k2zeitleiste, k2kooperativ,
          k2wecker, k2rtakt, k2stadtplan, k2seitentabelle, k2mmu, k2seitenfehler, k2radresse,
          k2eintrag, k2nx, k2wx, k2smap, k2maps, k2bootkit, k2anker, k2schluessel, k2aendern, k2widerruf,
          k2zweiketten, k2tpm, k2rpcr, k2sha, k2protokoll, k2bauformen, k2versiegeln, k2sperrklinke, k2attest, k2bus)

if __name__ == "__main__":
    namen = sys.argv[1:]
    for f in SZENEN:
        if not namen or f.__name__ in namen:
            f()
