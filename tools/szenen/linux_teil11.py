"""Linux und Kommandozeile, Kapitel 11 „SSH, Dateien übertragen und tmux“ (C:\\Bücher\\EtUndSo\\Linux\\Arbeitshefte\\
Kap11_SSH.tex, kap11_stufen.tex, kap11_stufen_b.tex): Abbildungen, alle animiert (notizen/animationen.md §5, §11).

Szenenname linux/k11<name> = \\label{fig:k11<name>} im Heft (\\szenenabb{k11<name>}{…}{fig:k11<name>}); Liste in
uebergabe_kap11.md, Abschnitt „Endgültige Abbildungsliste“. Phase 2b-1 (13.11.2026): Abschnitte 1–3 (15 Szenen); Phase
2b-2 (13.11.2026): Abschnitte 4–6 (15 Szenen, ab „Phase 2b-2: Helfer“).
Stil: F1. Terminalbilder (k11ersteverbindung, k11warnung, k11keygen, k11sftp, k11tmuxssh) sind s.terminal (dunkel, wie Ubuntu, Prompt
student@labor:~/linuxk11$), Datei-Ansichten s.datei bzw. s.terminal(rahmen="datei", stil="hell"), wenn Zeilen
verschwinden oder wechseln; Zeilen zum Zerlegen s.raster. Die übrigen Bilder sind Schemata aus Kästen und Pfeilen mit
den Helfern unten und aus linux_hilfen.py. Inhalte (Befehle, Ausgaben, Schlüssel, Fingerabdrücke) wörtlich aus dem Heft
bzw. den Mitschriften code/kap11/sitzung_kap11*.txt; die 32 Bytes in k11fingerabdruck sind der Fingerabdruck aus dem
Heft, aus Base64 zurückgerechnet (wie rechnung_kap11.py).
Wiederkehrende Bildsprache (wie Kapitel 9): Schlüssel als Schlüsselsymbol, private Schlüssel mit Schloss (s.schloss),
Signatur als Siegel; Hostschlüssel orange, Schlüsselpaar des Benutzers blau. Client und Server als zwei Blöcke
nebeneinander (links der eigene Rechner, rechts der Server).
Farben: grün = passt/erlaubt, rot = Fehler/abgelehnt, orange = hervorgehoben/Weg, blau = Programm/Prozess, grau = unbeteiligt.
Koordinaten zwischen x = -3,45 und 3,45 (höchstens 548 px).
Bauen:  python tools/szenen/linux_teil11.py [k11name …]
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
TK = 17                           # kleinste Schreibmaschinenschrift (Kärtchen, Pfade)
P11 = "student@labor:~/linuxk11$ "  # Prompt im Übungsverzeichnis des Kapitels (Abschnitt 1.1: cd ~/linuxk11)
PFAD = "~/linuxk11"
TITEL = "student@labor: ~/linuxk11"
PUNKTE = farbig("...", "grau")    # ausgelassene Zeilen (im Heft „...“)
K_HOST = ORANGE                   # Hostschlüssel des Servers
K_USER = BLAU                     # Schlüsselpaar des Benutzers
HOST_B64 = "AAAAC3NzaC1lZDI1NTE5AAAAIAo/cgLpIheFYzbh2ILLxezHxP0EQX6fpHHVx64eG9nE"   # Heft 2.5 (68 Zeichen)
HOST_FP = "SHA256:wNZ8yXKbBf8Si12Ie8pjqJdgbEqnuvLvD4qb6M7qYnw"                       # Heft 1.5, 2.3, 2.4
USER_FP = "SHA256:263611uAvZia1OHwR0Wp8jBvtQdiBkiiPZTlU1NH+L4"                       # Heft 3.2


def r4(v):
    return round(v, 4)


def ttb(t, g=TK):
    """Breite eines Texts in Schreibmaschinenschrift."""
    return len(t) * tt_breite(g, 1)


def L(s, key, w, pos, g=FM, a="center", f=SCHWARZ):
    """Beschriftung in sechs Sprachen; w = (de, en, es, zh, fr, tr)."""
    return text(s, T(s, key, *w), (r4(pos[0]), r4(pos[1])), g, a, f)


def Lr(s, key, w, pos, g=FM, a="center", f=SCHWARZ):
    """Wie L, aber roh: Punkte in Zahlen bleiben Punkte, _ bleibt _."""
    return text(s, T(s, key, *w), (r4(pos[0]), r4(pos[1])), g, a, f, roh=True)


def tx(s, t, pos, g=TT, a="center", f=SCHWARZ):
    """Schreibmaschinenschrift (Befehle, Namen, Ausgaben); in allen Sprachen gleich."""
    return s.text(None, t, (r4(pos[0]), r4(pos[1])), g, a, f, schrift="tt")


def box(s, mitte, b, h, rand=GRAU, fuellung=WEISS, dicke=2, form="round", dash="", deckung=1.0):
    return s.box("", (r4(mitte[0]), r4(mitte[1])), breite=r4(b), hoehe=r4(h), form=form, farbe=rand, fuellung=fuellung,
                 deckung=deckung, dicke=dicke, dash=dash)


def chip(s, mitte, t, rand=BLAU, fuellung=BLAU_HELL, g=TK, h=0.28, b=None, dicke=2, textfarbe=SCHWARZ, dash=""):
    """Kärtchen mit Schreibmaschinenschrift (Wort, Datei); Ergebnis [Kasten, Text]."""
    b = b if b is not None else ttb(t, g) + 0.24
    return [box(s, mitte, b, h, rand, fuellung, dicke, dash=dash), tx(s, t, mitte, g, "center", textfarbe)]


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


def nr(s, x, y, n, farbe=ORANGE, r=0.11):
    """Nummer im Kreis (Ergebnis [Kreis, Zahl])."""
    return [s.kreis(None, r4(x), r4(y), r, farbe=farbe, dicke=2, fuellung=WEISS, deckung=1.0),
            text(s, str(n), (r4(x), r4(y)), FM, "center", farbe)]


def proz(s, mitte, name, b=None, h=0.4, g=TT):
    """Programm/Prozess: blauer Kasten mit dem Namen in Schreibmaschinenschrift (Ergebnis [Kasten, Name])."""
    b = b if b is not None else ttb(name, g) + 0.3
    return [box(s, mitte, b, h, BLAU, BLAU_HELL, 2.5, "rect"), tx(s, name, mitte, g)]


def block(s, x0, x1, y0, y1, key, w):
    """Ein Rechner als Block: Rahmen und Überschrift oben links (Ergebnis [Rahmen, Überschrift])."""
    return [box(s, ((x0 + x1) / 2, (y0 + y1) / 2), x1 - x0, y1 - y0, GRAU, WEISS, 2, "rect"),
            L(s, key, w, (x0 + 0.1, y1 - 0.17), FM, "left", DUNKEL)]


def schluessel(s, x, y, farbe=ORANGE, fuellung=ORANGE_HELL, g=1.0):
    """Schlüssel waagrecht, Bart rechts (wie Kapitel 9; Ergebnis Liste); Mitte etwa (x, y), Breite 0,56·g."""
    return [s.kreis(None, r4(x - 0.18 * g), r4(y), r4(0.1 * g), farbe=farbe, dicke=2.5, fuellung=fuellung, deckung=1.0),
            lin(s, (x - 0.08 * g, y), (x + 0.28 * g, y), farbe, 4),
            lin(s, (x + 0.17 * g, y), (x + 0.17 * g, y - 0.08 * g), farbe, 3.5),
            lin(s, (x + 0.26 * g, y), (x + 0.26 * g, y - 0.1 * g), farbe, 3.5)]


def siegel(s, x, y, r=0.09, farbe=ORANGE):
    """Signatur als Siegel (wie Kapitel 9)."""
    return s.kreis(None, r4(x), r4(y), r, farbe=farbe, dicke=2, fuellung=farbe, deckung=0.9)


def dok(s, x, y, b=0.42, h=0.52, rand=DUNKEL, fuellung=WEISS, linien=HELLGRAU):
    """Dokument mit drei angedeuteten Zeilen (Ergebnis Liste)."""
    teile = [box(s, (x, y), b, h, rand, fuellung, 2, "rect")]
    for k in range(3):
        yy = y + h / 2 - h * 0.25 - k * h * 0.22
        teile.append(lin(s, (x - b / 2 + 0.07, yy), (x + b / 2 - 0.07 - (0.07 if k == 2 else 0), yy), linien, 2))
    return teile


def rechner(s, x, y, g=1.0):
    """Kleiner Rechner: Bildschirm und Fuß (Ergebnis Liste)."""
    return [box(s, (x, y + 0.04 * g), 0.42 * g, 0.28 * g, DUNKEL, WEISS, 2, "rect"),
            lin(s, (x, y - 0.1 * g), (x, y - 0.17 * g), DUNKEL, 2.5),
            lin(s, (x - 0.12 * g, y - 0.17 * g), (x + 0.12 * g, y - 0.17 * g), DUNKEL, 2.5)]


def laptop(s, x, y, g=1.0, farbe=DUNKEL):
    """Laptop: Bildschirm und flache Tastatur (Ergebnis Liste)."""
    return [box(s, (x, y + 0.08 * g), 0.5 * g, 0.32 * g, farbe, WEISS, 2, "rect"),
            box(s, (x, y - 0.12 * g), 0.66 * g, 0.07 * g, farbe, GRAU_HELL, 2, "rect")]


def person(s, x, y, farbe=ROT, g=1.0):
    """Kleine Figur aus Kopf und Schultern (Ergebnis Liste); Höhe etwa 0,32·g."""
    kopf = s.kreis(None, r4(x), r4(y + 0.08 * g), r4(0.075 * g), farbe=farbe, dicke=2.5, fuellung=WEISS, deckung=1.0)
    rumpf = s.weg(None, "%s+%s*cos(t)" % (r4(x), r4(0.14 * g)), "%s+%s*sin(t)" % (r4(y - 0.16 * g), r4(0.14 * g)),
                  0, 3.1416, farbe=farbe, dicke=2.5, n=31)
    return [kopf, rumpf]


def ohr(s, x, y, g=1.0, farbe=DUNKEL):
    """Ohr-Symbol „lauscht“ (Ergebnis Liste)."""
    rx, ry = 0.075 * g, 0.1 * g
    aussen = s.weg(None, "%s+%s*cos(t)" % (r4(x), r4(rx)), "%s+%s*sin(t)" % (r4(y + 0.02 * g), r4(ry)), -1.2, 3.6,
                   farbe=farbe, dicke=2.5, n=41)
    x1, y1 = x + rx * math.cos(3.6), y + 0.02 * g + ry * math.sin(3.6)
    x2, y2 = x + rx * math.cos(-1.2), y + 0.02 * g + ry * math.sin(-1.2)
    lappen = s.weg(None, "%s+%s*t+%s*4*t*(1-t)" % (r4(x1), r4(x2 - x1), r4(-0.03 * g)),
                   "%s+%s*t-%s*4*t*(1-t)" % (r4(y1), r4(y2 - y1), r4(0.05 * g)), 0, 1, farbe=farbe, dicke=2.5, n=21)
    innen = s.weg(None, "%s+%s*cos(t)" % (r4(x + 0.005 * g), r4(0.03 * g)), "%s+%s*sin(t)" % (r4(y + 0.02 * g), r4(0.04 * g)),
                  0.2, 3.4, farbe=farbe, dicke=2, n=21)
    return [aussen, lappen, innen]


def steckdose(s, x, y, r=0.17):
    """Steckdose (Socket): Kreis mit zwei Löchern (Ergebnis Liste)."""
    return [s.kreis(None, r4(x), r4(y), r, farbe=DUNKEL, dicke=2.5, fuellung=WEISS, deckung=1.0),
            s.kreis(None, r4(x - 0.065), r4(y), 0.03, farbe=DUNKEL, dicke=1, fuellung=DUNKEL, deckung=1.0),
            s.kreis(None, r4(x + 0.065), r4(y), 0.03, farbe=DUNKEL, dicke=1, fuellung=DUNKEL, deckung=1.0)]


def brief(s, x, y, b=1.3, h=0.52):
    """Briefumschlag mit Klappe (Ergebnis Liste)."""
    return [box(s, (x, y), b, h, DUNKEL, WEISS, 2, "rect"),
            lin(s, (x - b / 2, y + h / 2), (x, y + h / 2 - 0.17), DUNKEL, 1.5),
            lin(s, (x, y + h / 2 - 0.17), (x + b / 2, y + h / 2), DUNKEL, 1.5)]


def tresor(s, mitte, b, h):
    """Tresor: dicker Rahmen mit Drehknopf (Ergebnis Liste)."""
    return [box(s, mitte, b, h, DUNKEL, WEISS, 4, "rect"),
            s.kreis(None, r4(mitte[0] + b / 2 - 0.16), r4(mitte[1] + h / 2 - 0.2), 0.06, farbe=DUNKEL, dicke=2.5)]


def gleich_nicht(s, x, y, g=TT):
    """Durchgestrichenes Gleichheitszeichen (Ergebnis Liste)."""
    return [tx(s, "=", (x, y), g + 4, "center", ROT), lin(s, (x - 0.1, y - 0.13), (x + 0.1, y + 0.13), ROT, 3)]


W_CLIENT = ("Client", "client", "cliente", "客户端", "client", "istemci")
W_SERVER = ("Server", "server", "servidor", "服务器", "serveur", "sunucu")
W_DEIN = ("dein Rechner", "your computer", "tu ordenador", "你的计算机", "ton ordinateur", "bilgisayarın")
W_ENTF = ("entfernter Rechner", "remote computer", "ordenador remoto", "远程计算机", "ordinateur distant", "uzak bilgisayar")
W_PRIVAT = ("privater Schlüssel", "private key", "clave privada", "私钥", "clé privée", "özel anahtar")
W_STARTET = ("startet", "starts", "inicia", "启动", "lance", "başlatır")
W_SHELL = ("Shell", "shell", "shell", "Shell", "shell", "kabuk")
W_AUSGABE = ("Ausgabe", "output", "salida", "输出", "sortie", "çıktı")


# ================================================================== Abschnitt 1: Entfernte Anmeldung
W_PO = {"lh": ("localhost, auch ::1: immer der eigene Rechner", "localhost, also ::1: always your own computer",
               "localhost, también ::1: siempre el propio ordenador", "localhost，也写作 ::1：总是本机",
               "localhost, aussi ::1 : toujours ta propre machine", "localhost, ayrıca ::1: her zaman kendi bilgisayarın"),
        "ssh": ("SSH-Server", "SSH server", "servidor SSH", "SSH 服务器", "serveur SSH", "SSH sunucusu"),
        "lauscht": ("lauscht", "listens", "escucha", "监听", "écoute", "dinler"),
        "web": ("Webserver", "web server", "servidor web", "Web 服务器", "serveur web", "web sunucusu"),
        "nicht": ("nicht\ninstalliert", "not\ninstalled", "no\ninstalado", "未安装", "non\ninstallé", "kurulu\ndeğil"),
        "satz": ("Adresse wählt den Rechner, Port wählt den Dienst", "The address picks the computer, the port picks the service",
                 "La dirección elige el ordenador, el puerto elige el servicio", "地址选择计算机，端口选择服务",
                 "L'adresse choisit la machine, le port choisit le service", "Adres bilgisayarı seçer, port hizmeti seçer")}


def k11port():
    """Haus mit der Anschrift 127.0.0.1 (darunter: localhost, auch ::1), vier Wohnungstüren: 22 (SSH-Server, Ohr
    „lauscht“), 443 (gestrichelt, Webserver nicht installiert), zwei ohne Schild. Ein Brief 127.0.0.1 : 22 kommt an,
    die Anschrift passt (beide leuchten), er wird zur Tür 22 gebracht. Unten der Satz."""
    s = Szene("linux/k11port", reihenfolge="anlegen")
    w = W_PO
    xm, yb0, yb1, bb = 1.0, -0.95, 1.25, 4.5
    dach = s.vieleck(None, [(r4(xm - bb / 2 - 0.15), yb1), (r4(xm + bb / 2 + 0.15), yb1), (xm, 2.3)], farbe=GRAU_HELL,
                     deckung=1.0, dicke=2.5, randfarbe=DUNKEL)
    koerper = box(s, (xm, (yb0 + yb1) / 2), bb, yb1 - yb0, DUNKEL, WEISS, 2.5, "rect")
    schild = chip(s, (xm, 1.64), "127.0.0.1", DUNKEL, WEISS, g=TT, h=0.32)
    l_lh = Lr(s, "lh", w["lh"], (xm, 0.95), FM, "center", DUNKEL)
    xs = [xm - bb / 2 + 0.15 + 0.475 + 1.07 * k for k in range(4)]
    tb, th = 0.95, 0.95
    yt = yb0 + th / 2
    tueren = []
    for k, x in enumerate(xs):
        tueren.append(box(s, (x, yt), tb, th, DUNKEL if k != 1 else GRAU, WEISS if k else BLAU_HELL, 2.5 if k != 1 else 2,
                          "rect", dash="6,4" if k == 1 else ""))
        if k >= 2:
            tueren.append(s.kreis(None, r4(x + tb / 2 - 0.12), r4(yt), 0.035, farbe=DUNKEL, dicke=2, fuellung=DUNKEL, deckung=1.0))
    pl22 = chip(s, (xs[0], yt + th / 2 + 0.18), "22", DUNKEL, WEISS, g=TT, h=0.28)
    pl443 = chip(s, (xs[1], yt + th / 2 + 0.18), "443", GRAU, WEISS, g=TT, h=0.28, textfarbe=GRAU, dash="5,4")
    d22 = [L(s, "ssh", w["ssh"], (xs[0], yt + 0.22), FM, "center", BLAU)] + ohr(s, xs[0] - 0.28, yt - 0.2) + \
          [L(s, "lauscht", w["lauscht"], (xs[0] - 0.12, yt - 0.2), FM, "left", DUNKEL)]
    d443 = [L(s, "web", w["web"], (xs[1], yt + 0.22), FM, "center", GRAU),
            L(s, "nicht", w["nicht"], (xs[1], yt - 0.18), FM, "center", GRAU)]
    # Brief: oben links, Aufschrift in drei Stücken (Anschrift, Doppelpunkt, Port)
    bx, by = -2.55, 1.85
    cw = tt_breite(TK, 1)
    x0 = bx - 14 * cw / 2
    yb = by - 0.09
    bf = brief(s, bx, by)
    a_adr = tx(s, "127.0.0.1", (x0 + 4.5 * cw, yb), TK)
    a_dp = tx(s, ":", (x0 + 10.5 * cw, yb), TK)
    a_port = tx(s, "22", (x0 + 13 * cw, yb), TK)
    brief_alle = bf + [a_adr, a_dp, a_port]
    zx, zy = -2.45, yt
    pf_t = pfk(s, (zx + 0.67, zy), (xs[0] - tb / 2 - 0.03, zy), ORANGE, 2.5)
    satz = L(s, "satz", w["satz"], (xm - 0.6, yb0 - 0.4), FS, "center", DUNKEL)
    schritt(s, EIN([dach, koerper], 0.6))
    schritt(s, EIN(schild, 0.5))
    schritt(s, EIN(l_lh, 0.5))
    s.pause(0.3)
    schritt(s, EIN(tueren + pl22 + pl443, 0.6))
    schritt(s, EIN(d22 + d443, 0.6))
    s.pause(0.5)
    schritt(s, EIN(brief_alle, 0.5))
    schritt(s, BETONE([a_adr, schild[1]], 0.8))
    schritt(s, *VERS(brief_alle, zx - bx, zy - by, 0.9))
    schritt(s, ZEICHNE(pf_t, 0.5), BETONE([a_port, pl22[1]], 0.8))
    s.pause(0.4)
    schritt(s, EIN(satz, 0.6))
    s.speichern()


W_CS = {"auf": ("Verbindung aufbauen", "open a connection", "establecer la conexión", "建立连接", "établir la connexion",
                "bağlantı kur"),
        "seite": ("Seite", "page", "página", "网页", "page", "sayfa"),
        "antwort": ("Antwort", "reply", "respuesta", "回应", "réponse", "yanıt"),
        "browser": ("Browser", "browser", "navegador", "浏览器", "navigateur", "tarayıcı"),
        "webserver": ("Webserver", "web server", "servidor web", "Web 服务器", "serveur web", "web sunucusu"),
        "kc": ("(Client)", "(client)", "(cliente)", "（客户端）", "(client)", "(istemci)"),
        "ks": ("(Server)", "(server)", "(servidor)", "（服务器）", "(serveur)", "(sunucu)"),
        "wartet": ("wartet immer", "always waiting", "siempre espera", "一直在等待", "attend toujours", "hep bekler"),
        "ruft": ("ruft an, wenn er\netwas braucht", "calls when it\nneeds something", "llama cuando\nnecesita algo",
                 "需要时\n才打电话", "appelle quand il\na besoin de quelque chose", "bir şeye ihtiyacı\nolunca arar")}


def server_tuer(s, x, y, port):
    """Rechner mit einer Tür (Port) an der linken Seite; Ergebnis (Teile, Anker an der Tür)."""
    k = box(s, (x, y), 1.05, 0.78, DUNKEL, GRAU_HELL, 2, "rect")
    xt = x - 0.525 + 0.2
    tuer = box(s, (xt, y - 0.1), 0.26, 0.46, DUNKEL, WEISS, 2, "rect")
    nummer_ = tx(s, port, (xt, y + 0.25), TK)
    schlitze = [lin(s, (x + 0.02, y + 0.2 - 0.12 * k), (x + 0.38, y + 0.2 - 0.12 * k), GRAU, 2) for k in range(3)]
    return [k, tuer, nummer_] + schlitze, (xt - 0.13, y - 0.1)


def k11clientserver():
    """Zwei Zeilen im selben Muster: Browser (Client) → Webserver an Tür 443, Antwort „Seite“; ssh (Client) → sshd
    (Server) an Tür 22. Zuletzt die Schilder: Uhr „wartet immer“ an den Servern, „ruft an, wenn er etwas braucht“."""
    s = Szene("linux/k11clientserver", reihenfolge="anlegen")
    w = W_CS
    xl, xr = -2.55, 2.45
    zeilen_ = []
    for i, (y, prog, port, kz, ant) in enumerate(((1.7, None, "443", "browser", "seite"), (-0.05, "ssh", "22", None, "antwort"))):
        lap = laptop(s, xl, y + 0.05)
        l1 = L(s, kz, w[kz], (xl, y - 0.33), FM, "center") if kz else tx(s, prog, (xl, y - 0.33), TT)
        l2 = L(s, "kc%d" % i, w["kc"], (xl, y - 0.57), FM, "center", GRAU)
        srv, anker = server_tuer(s, xr, y + 0.02, port)
        r1 = L(s, "webserver", w["webserver"], (xr, y - 0.55), FM, "center") if kz else tx(s, "sshd", (xr, y - 0.55), TT)
        r2 = L(s, "ks%d" % i, w["ks"], (xr, y - 0.79), FM, "center", GRAU)
        auf = [pfk(s, (xl + 0.42, anker[1] + 0.07), (anker[0] - 0.03, anker[1] + 0.07), DUNKEL, 2.5),
               L(s, "auf%d" % i, w["auf"], (-0.05, anker[1] + 0.25), FM, "center", DUNKEL)]
        zur = [pfk(s, (anker[0] - 0.03, anker[1] - 0.13), (xl + 0.42, anker[1] - 0.13), GRUEN, 2.5),
               L(s, ant, w[ant], (-0.05, anker[1] - 0.31), FM, "center", GRUEN)]
        uhr_ = list(uhr(s, xr + 0.76, y + 0.3, 10, 10, 0.14))
        zeilen_.append({"links": lap + [l1, l2], "rechts": srv + [r1, r2], "auf": auf, "zur": zur, "uhr": uhr_})
    ys = -1.25
    s_r = list(uhr(s, 1.55, ys, 10, 10, 0.18)) + [L(s, "wartet", w["wartet"], (1.85, ys), FM, "left", DUNKEL)]
    s_l = [L(s, "ruft", w["ruft"], (xl + 0.2, ys), FM, "center", DUNKEL)]
    for i, z in enumerate(zeilen_):
        schritt(s, EIN(z["links"] + z["rechts"], 0.6))
        schritt(s, ZEICHNE(z["auf"][0], 0.6), EIN(z["auf"][1], 0.6))
        schritt(s, ZEICHNE(z["zur"][0], 0.6), EIN(z["zur"][1], 0.6))
        s.pause(0.5)
    schritt(s, EIN(zeilen_[0]["uhr"] + zeilen_[1]["uhr"] + s_r, 0.6))
    schritt(s, EIN(s_l, 0.6))
    s.speichern()


W_AN = {"versch": ("verschlüsselt", "encrypted", "cifrado", "加密", "chiffré", "şifreli"),
        "shellhier": ("Shell läuft hier", "the shell runs here", "la shell se ejecuta aquí", "shell 在这里运行",
                      "le shell tourne ici", "kabuk burada çalışır"),
        "fensterhier": ("Fenster ist hier", "the window is here", "la ventana está aquí", "窗口在这里", "la fenêtre est ici",
                        "pencere burada")}


def k11anmeldung():
    """Links der eigene Rechner mit Terminalfenster und ssh, rechts der Server mit sshd an Port 22. Nacheinander: Rohr
    mit Schloss (verschlüsselt), sshd startet eine Shell, das Paket ls wandert nach rechts, die Ausgabe kommt zurück und
    erscheint im Fenster. Etiketten Client, Server, „Shell läuft hier“, „Fenster ist hier“."""
    s = Szene("linux/k11anmeldung", reihenfolge="anlegen")
    w = W_AN
    bl = block(s, -3.42, -0.8, -0.75, 2.45, "dein", W_DEIN)
    br = block(s, 0.8, 3.42, -0.75, 2.45, "entf", W_ENTF)
    ys = 0.2
    rohr_ = box(s, (-0.17, ys), 3.46, 0.2, GRAU, GRAU_HELL, 2, "rect")
    t = s.terminal(pos=(-3.25, 2.12), spalten=22, zeilen=3, groesse=TK, prompt="student@labor:~$ ")
    p_ssh = proz(s, (-2.35, ys), "ssh", 0.9)
    verb = lin(s, (-2.35, t.unten_kante - 0.03), (-2.35, ys + 0.22), GRAU, 2, "4,4")
    p_sshd = proz(s, (2.35, ys), "sshd", 0.9)
    port = chip(s, (1.72, ys), "22", DUNKEL, WEISS, g=TK, h=0.26, b=0.32)
    schl = s.schloss((-0.17, ys + 0.3), 0.3, farbe=DUNKEL)
    l_v = L(s, "versch", w["versch"], (-0.17, ys - 0.28), FM, "center", DUNKEL)
    sh = [box(s, (2.1, 1.6), 1.2, 0.42, BLAU, BLAU_HELL, 2.5, "rect"), L(s, "shell", W_SHELL, (2.1, 1.6), FM, "center")]
    p_st = pfk(s, (2.35, ys + 0.2), (2.35, 1.38), BLAU, 2.5)
    l_st = L(s, "startet", W_STARTET, (2.47, 0.88), FM, "left", BLAU)
    l_client = L(s, "client", W_CLIENT, (-2.35, ys - 0.36), FM, "center", DUNKEL)
    l_server = L(s, "server", W_SERVER, (2.35, ys - 0.36), FM, "center", DUNKEL)
    l_sh = L(s, "shellhier", w["shellhier"], (2.1, 2.02), FM, "center", ORANGE)
    l_fe = L(s, "fensterhier", w["fensterhier"], (-2.25, 0.86), FM, "left", ORANGE)
    schritt(s, EIN(bl + br, 0.5))
    schritt(s, EIN([t.id, verb] + p_ssh, 0.6), EIN(p_sshd + port, 0.6))
    s.pause(0.4)
    schritt(s, WACHS(rohr_, 0.6), EIN([schl, l_v], 0.6))
    schritt(s, ZEICHNE(p_st, 0.5), WACHS(sh[0], 0.6), EIN([sh[1], l_st], 0.6))
    s.pause(0.4)
    t.eingabe("ls")
    xa, ya = t.xm(17, 18), t.y(0)
    pk = chip(s, (xa, ya), "ls", ORANGE, ORANGE_HELL, g=TK, h=0.26)
    schritt(s, EIN(pk, 0.4))
    schritt(s, *VERS(pk, -2.35 - xa, ys - ya, 0.6))
    schritt(s, *VERS(pk, 4.7 - 0.6, 0, 0.8))
    schritt(s, *VERS(pk, 2.1 - 1.75, 1.6 - ys, 0.5))
    schritt(s, AUS(pk, 0.3))
    au = wchip(s, (2.1, 1.6), "ausgabe", W_AUSGABE, 0.95, GRUEN, GRUEN_HELL, h=0.28)
    schritt(s, EIN(au, 0.4))
    schritt(s, *VERS(au, 1.75 - 2.1, ys - 1.6, 0.5))
    schritt(s, *VERS(au, -2.35 - 1.75, 0, 0.8))
    schritt(s, *VERS(au, 0, t.y(1) - ys, 0.6))
    with s.gleichzeitig():
        t.ausgabe(PUNKTE, dauer=0.5)
        schritt(s, AUS(au, 0.5))
    t.prompt()
    s.pause(0.3)
    schritt(s, EIN([l_client, l_server], 0.5))
    schritt(s, EIN([l_sh, l_fe], 0.6))
    s.speichern()


DROPIN = ["ListenAddress 127.0.0.1", "ListenAddress ::1", "PasswordAuthentication no", "KbdInteractiveAuthentication no",
          "PermitRootLogin no"]
INCLUDE = "Include /etc/ssh/sshd_config.d/*.conf"
W_DI = {"lh": ("nur über localhost erreichbar", "reachable only via localhost", "accesible solo por localhost",
               "只能通过 localhost 访问", "accessible seulement via localhost", "yalnızca localhost üzerinden erişilebilir"),
        "pw": ("keine Passwörter", "no passwords", "sin contraseñas", "不用密码", "pas de mots de passe", "parola yok"),
        "root": ("kein root", "no root", "sin root", "禁止 root", "pas de root", "root yok"),
        "ein": ("an dieser Stelle\neingelesen", "read in\nat this point", "se lee\nen este punto", "在此处\n读入",
                "lu à\ncet endroit", "bu noktada\nokunur")}


def k11dropin():
    """Oben /etc/ssh/sshd_config (hell): …, hervorgehoben Include /etc/ssh/sshd_config.d/*.conf, … (mehr steht nach dem
    Rückbau nicht fest). Darunter 10-linuxk11.conf mit den fünf Zeilen (Mitschrift s0_dropin), rechts Randetiketten mit
    Klammern. Ein Pfeil von der Include-Zeile geht zur Datei; deren Zeilen wandern (orange Kopien) an diese Stelle."""
    s = Szene("linux/k11dropin", reihenfolge="anlegen")
    w = W_DI
    t = s.terminal(text="\n".join([PUNKTE, INCLUDE, PUNKTE]), pos=(-3.42, 3.0), spalten=38, zeilen=8,
                   titel="/etc/ssh/sshd_config", groesse=TK, stil="hell", rahmen="datei", knoepfe="x", cursor=False,
                   farbprompt=False)
    mk = t.markieren(1, 0, len(INCLUDE) - 1, ORANGE, 0.25)
    b = s.datei("/etc/ssh/sshd_config.d/10-linuxk11.conf", "\n".join(DROPIN), pos=(-2.9, 1.05), spalten=38, groesse=TK)
    xk = b.rechts + 0.13
    etik = []
    for (z0, z1), key in (((0, 1), "lh"), ((2, 3), "pw"), ((4, 4), "root")):
        ya, yb = b.oben(z0) - 0.015, b.unten(z1) + 0.015
        etik += vklammer(s, r4(xk), r4(ya), r4(yb), GRAU, 0.06, 2) + [L(s, key, w[key], (xk + 0.12, (ya + yb) / 2), FM, "left", DUNKEL)]
    xa = -0.25
    pfeil_ = pfk(s, (t.xr(len(INCLUDE) - 1) + 0.06, t.y(1)), (xa, b.oben_kante + 0.03), ORANGE, 2.5, knick="hv")
    l_ein = L(s, "ein", w["ein"], (xa + 0.15, t.y(4)), FM, "left", ORANGE)
    kopien = [b.teil(k, 0, len(z) - 1, farbe=ORANGE) for k, z in enumerate(DROPIN)]
    schritt(s, EIN(t.id, 0.6))
    schritt(s, EIN(mk, 0.5))
    s.pause(0.3)
    schritt(s, EIN(b.id, 0.6))
    schritt(s, EIN(etik, 0.6))
    s.pause(0.5)
    schritt(s, ZEICHNE(pfeil_, 0.7))
    with s.gleichzeitig():
        t.schritt("\\e[3;1H\\e[K\\e[8;1H" + PUNKTE, 0.5)
        schritt(s, EIN(kopien, 0.5))
    schritt(s, *[VER(k, t.x(0) - b.x(0), t.y(2 + i) - b.y(i), 1.0) for i, k in enumerate(kopien)], EIN(l_ein, 1.0))
    s.speichern()


W_SO = {"lauscht": ("lauscht an 127.0.0.1:22 und [::1]:22", "listens on 127.0.0.1:22 and [::1]:22",
                    "escucha en 127.0.0.1:22 y [::1]:22", "监听 127.0.0.1:22 和 [::1]:22", "écoute sur 127.0.0.1:22 et [::1]:22",
                    "127.0.0.1:22 ve [::1]:22 adreslerini dinler"),
        "ueber": ("übergibt den Socket", "hands over the socket", "entrega el socket", "交出套接字", "transmet le socket",
                  "soketi devreder"),
        "satz": ("Der Dienst startet erst, wenn jemand anruft.", "The service starts only when someone calls.",
                 "El servicio solo arranca cuando alguien llama.", "有人打来时服务才启动。",
                 "Le service ne démarre que lorsque quelqu'un appelle.", "Hizmet ancak biri aradığında başlar.")}


def k11socket():
    """Kasten systemd mit der Steckdose am Port 22 (ssh.socket, lauscht an 127.0.0.1:22 und [::1]:22), darunter grau
    gestrichelt ssh.service (sshd), inactive. Die Verbindung von Client ssh kommt an der Steckdose an (oranger Ring);
    systemd startet sshd (Kasten blau, active) und reicht die Steckdose samt wartender Verbindung hinüber. Unten der
    Satz (Heft: systemctl status, is-active)."""
    s = Szene("linux/k11socket", reihenfolge="anlegen")
    w = W_SO
    xc, yc = -2.75, 0.8
    cl = proz(s, (xc, yc), "ssh", 0.9)
    l_cl = L(s, "client", W_CLIENT, (xc, yc + 0.36), FM, "center", DUNKEL)
    xb, bb = 1.05, 4.5
    xs0 = xb - bb / 2
    y1, y2 = 1.75, -0.1
    sd = [box(s, (xb, y1), bb, 1.0, GRAU, GRAU_HELL, 2, "rect"), tx(s, "systemd", (xs0 + 0.1, y1 + 0.66), TT, "left", DUNKEL)]
    so = [tx(s, "ssh.socket", (xs0 + 0.35, y1 + 0.17), TT, "left"),
          Lr(s, "lauscht", w["lauscht"], (xs0 + 0.35, y1 - 0.16), FM, "left", DUNKEL)]
    xd = xs0 - 0.17
    dose = steckdose(s, xd, y1)
    p22 = tx(s, "22", (xd, y1 - 0.31), TK, "center", DUNKEL)
    sv_grau = box(s, (xb, y2), bb, 0.95, GRAU, WEISS, 2, "rect", dash="6,4")
    sv_blau = box(s, (xb, y2), bb, 0.95, BLAU, BLAU_HELL, 2.5, "rect")
    sv_t = tx(s, "ssh.service (sshd)", (xs0 + 0.35, y2 + 0.17), TT, "left")
    st = tx(s, "inactive", (xs0 + 0.35, y2 - 0.17), TT, "left", GRAU)
    kabel1 = pfk(s, (xc + 0.45, yc + 0.08), (xd - 0.2, y1 - 0.12), DUNKEL, 2.5)
    ring = s.kreis(None, r4(xd), y1, 0.24, farbe=ORANGE, dicke=3)
    kabel2 = pfk(s, (xc + 0.45, yc - 0.08), (xd - 0.2, y2 + 0.12), DUNKEL, 2.5)
    p_st = pfk(s, (xb + 1.6, y1 - 0.5), (xb + 1.6, y2 + 0.475), BLAU, 2.5)
    l_st = L(s, "startet", W_STARTET, (xb + 1.72, (y1 + y2) / 2 + 0.05), FM, "left", BLAU)
    l_ue = L(s, "ueber", w["ueber"], (xs0 + 0.2, (y1 + y2) / 2 + 0.05), FM, "left", ORANGE)
    satz = L(s, "satz", w["satz"], (0.0, -0.95), FS, "center", DUNKEL)
    schritt(s, EIN(sd + so + dose + [p22], 0.6))
    schritt(s, EIN([sv_grau, sv_t, st], 0.6))
    s.pause(0.4)
    schritt(s, EIN(cl + [l_cl], 0.5))
    schritt(s, ZEICHNE(kabel1, 0.6), EIN(ring, 0.6))
    s.pause(0.3)
    schritt(s, ZEICHNE(p_st, 0.5), EIN([sv_blau, l_st], 0.6))
    s.ersetzen(st, "active", farbe=GRUEN, dauer=0.6)
    s.pause(0.3)
    schritt(s, *VERS(dose + [ring, p22], 0, y2 - y1, 1.0), AUS(kabel1, 0.6), EIN(l_ue, 1.0))
    schritt(s, ZEICHNE(kabel2, 0.5))
    s.pause(0.4)
    schritt(s, EIN(satz, 0.6))
    s.speichern()


# ================================================================== Abschnitt 2: Die erste Verbindung
W_HK = {"kartei": ("bekannte Rechner", "known hosts", "equipos conocidos", "已知主机", "machines connues", "bilinen makineler"),
        "daten": ("Daten nur\ndieser Verbindung", "data of this\nconnection only", "datos solo de\nesta conexión",
                  "仅属于这次\n连接的数据", "données de cette\nseule connexion", "yalnızca bu\nbağlantının verisi"),
        "signiert": ("signiert", "signs", "firma", "签名", "signe", "imzalar"),
        "nie": ("Der private Schlüssel verlässt den Tresor nie.", "The private key never leaves the safe.",
                "La clave privada nunca sale de la caja fuerte.", "私钥从不离开保险箱。", "La clé privée ne quitte jamais le coffre.",
                "Özel anahtar kasadan hiç çıkmaz.")}


def kartei(s, x, y, farbe=K_HOST):
    """Karteikasten: drei Karten ragen heraus, vorn ein kleiner Schlüssel (Ergebnis Liste)."""
    teile = [box(s, (x - 0.24 + 0.24 * k, y + 0.2), 0.36, 0.3, GRAU, WEISS, 1.5, "round") for k in range(3)]
    teile.append(box(s, (x, y), 1.0, 0.42, DUNKEL, GRAU_HELL, 2, "rect"))
    return teile + schluessel(s, x, y, farbe, WEISS, g=0.6)


def k11hostschluessel():
    """Rechts der Server mit Tresor (ssh_host_ed25519_key, Schloss, rw-------, root) und .pub, links der Client mit dem
    Karteikasten „bekannte Rechner“. (1) Kärtchen „Daten nur dieser Verbindung“, Nummer wechselt; (2) Siegel aus dem
    privaten Hostschlüssel, Kärtchen und .pub gehen nach links; (3) Haken für das Siegel, Vergleich mit dem Karteikasten.
    Schild: Der private Schlüssel verlässt den Tresor nie."""
    s = Szene("linux/k11hostschluessel", reihenfolge="anlegen")
    w = W_HK
    bl = block(s, -3.42, -1.05, -0.6, 2.5, "client", W_CLIENT)
    br = block(s, 1.05, 3.42, -0.6, 2.5, "server", W_SERVER)
    xs = 2.25
    tr_ = tresor(s, (xs, 1.62), 2.15, 1.1)
    kp = schluessel(s, xs - 0.35, 1.9, K_HOST, ORANGE_HELL)
    lk = s.schloss((xs + 0.2, 1.9), 0.24, farbe=DUNKEL)
    tr_txt = [tx(s, "ssh_host_ed25519_key", (xs - 0.05, 1.6), TK), tx(s, "rw-------  root", (xs - 0.05, 1.33), TK, "center", GRAU)]
    pub = schluessel(s, xs, 0.72, K_HOST, WEISS) + [tx(s, "ssh_host_ed25519_key.pub", (xs, 0.42), TK)]
    xk = -2.6
    ka = kartei(s, xk, 0.4)
    l_ka = L(s, "kartei", w["kartei"], (xk, -0.05), FM, "center", DUNKEL)
    xd, yd = 0.0, 1.5
    d = dok(s, xd, yd, 0.46, 0.56)
    badge = [s.kreis(None, r4(xd + 0.1), r4(yd - 0.14), 0.09, farbe=DUNKEL, dicke=2, fuellung=GELB, deckung=1.0)]
    num = text(s, "1", (r4(xd + 0.1), r4(yd - 0.14)), FM, "center", DUNKEL)
    l_d = L(s, "daten", w["daten"], (xd, 2.1), FM, "center", DUNKEL)
    sg = siegel(s, xd - 0.11, yd - 0.14, 0.08, K_HOST)
    p_sg = pfk(s, (xs - 1.1, 1.82), (xd + 0.3, yd + 0.12), ORANGE, 2, "5,4")
    l_sg = L(s, "signiert", w["signiert"], (0.7, 1.43), FM, "center", ORANGE)
    karte = d + badge + [num, sg]
    kopie = schluessel(s, xs, 0.72, K_HOST, WEISS)
    xz, yz = -2.55, 1.32
    xp, yp = -1.42, 0.4
    h1 = haken(s, xz + 0.5, yz, GRUEN, 0.1, 4)
    gl = tx(s, "=", (xk + 0.5 + 0.2, 0.4), TT + 4, "center", GRUEN)
    h2 = haken(s, xp, 0.0, GRUEN, 0.1, 4)
    nie = L(s, "nie", w["nie"], (0.0, -0.95), FS, "center", DUNKEL)
    schritt(s, EIN(bl + br, 0.5))
    schritt(s, EIN(tr_ + kp + [lk] + tr_txt, 0.7))
    schritt(s, EIN(pub, 0.5))
    schritt(s, EIN(ka + [l_ka], 0.6))
    s.pause(0.5)
    schritt(s, EIN(d + badge + [num, l_d], 0.6))
    s.ersetzen(num, "2", dauer=0.4)
    s.ersetzen(num, "3", dauer=0.4)
    s.pause(0.3)
    schritt(s, ZEICHNE(p_sg, 0.6), EIN(l_sg, 0.6))
    schritt(s, WACHS(sg, 0.4))
    schritt(s, EIN(kopie, 0.3))
    schritt(s, *VERS(karte + [l_d], xz - xd, yz - yd, 1.0), *VERS(kopie, xp - xs, yp - 0.72, 1.0), AUS([p_sg, l_sg], 0.5))
    schritt(s, EIN(h1, 0.5))
    schritt(s, EIN([gl] + h2, 0.5))
    s.pause(0.5)
    schritt(s, EIN(nie, 0.6))
    schritt(s, BETONE(kp + [lk], 0.9))
    s.speichern()


SHA_HEX = "c0 d6 7c c9 72 9b 05 ff 12 8b 5d 88 7b ca 63 a8 97 60 6c 4a a7 ba f2 ef 0f 8a 9b e8 ce ea 62 7c".split()
BITS8 = "11000000 11010110 01111100"
BITS6 = "110000 001101 011001 111100"
B64TAB = ["A–Z   0–25", "a–z  26–51", "0–9  52–61", "+       62", "/       63"]
W_FA = {"z68": ("68 Zeichen", "68 characters", "68 caracteres", "68 个字符", "68 caractères", "68 karakter"),
        "lesen": ("Base64 lesen", "decode Base64", "decodificar Base64", "Base64 解码", "décoder le Base64", "Base64 çöz"),
        "b51": ("51 Bytes", "51 bytes", "51 bytes", "51 字节", "51 octets", "51 bayt"),
        "b32": ("32 Bytes = 256 Bit", "32 bytes = 256 bits", "32 bytes = 256 bits", "32 字节 = 256 位", "32 octets = 256 bits",
                "32 bayt = 256 bit"),
        "g6": ("6-Bit-Gruppen", "6-bit groups", "grupos de 6 bits", "6 位一组", "groupes de 6 bits", "6 bitlik gruplar"),
        "rest": ("4 Bit + 00", "4 bits + 00", "4 bits + 00", "4 位 + 00", "4 bits + 00", "4 bit + 00"),
        "z43": ("43 Zeichen", "43 characters", "43 caracteres", "43 个字符", "43 caractères", "43 karakter")}


def k11fingerabdruck():
    """Oben die Zeile aus ssh_host_ed25519_key.pub (Klammer „68 Zeichen“), Base64 lesen → 51 Bytes, Trichter SHA-256 →
    32 Bytes (Kästchen mit den Bytes des Fingerabdrucks). Die ersten drei Bytes als Bits, zerlegt in 6-Bit-Gruppen, je
    Gruppe Wert und Zeichen (w N Z 8, Tabelle am Rand); das letzte Byte: 4 Bit + 00 → w. Unten der Fingerabdruck,
    Klammer „43 Zeichen“, daneben ein durchgestrichenes =."""
    s = Szene("linux/k11fingerabdruck", reihenfolge="anlegen")
    w = W_FA
    pub = "ssh-ed25519 " + HOST_B64 + " root@labor"
    g1 = s.raster(pub, (-3.43, 2.55), groesse=TK)
    k1 = g1.klammer(0, 12, 79, T(s, "z68", *w["z68"]), "oben", BLAU, FM)
    xm1 = g1.xm(12, 79)
    p1 = pfk(s, (xm1, 2.43), (xm1, 2.1), DUNKEL, 2.5)
    l1 = L(s, "lesen", w["lesen"], (xm1 + 0.12, 2.27), FM, "left", DUNKEL)
    yb = 1.95
    bytes51 = [box(s, (-3.2 + 0.128 * k, yb), 0.11, 0.15, GRAU, GRAU_HELL, 1, "rect") for k in range(51)]
    l51 = L(s, "b51", w["b51"], (3.27, yb - 0.2), FM, "right", GRAU)
    trichter = s.vieleck(None, [(-1.1, 1.8), (1.1, 1.8), (0.38, 1.38), (-0.38, 1.38)], farbe=GRAU_HELL, deckung=1.0,
                         dicke=2.5, randfarbe=DUNKEL)
    l_sha = tx(s, "SHA-256", (0, 1.6), TK)
    yc = 1.12
    xc = [-3.1 + 0.2 * k for k in range(32)]
    k32 = [box(s, (x, yc), 0.185, 0.25, BLAU, BLAU_HELL, 1.5, "rect") for x in xc]
    h32 = [tx(s, h, (x, yc), TK) for h, x in zip(SHA_HEX, xc)]
    l32 = Lr(s, "b32", w["b32"], (1.75, yc - 0.25), FM, "center", BLAU)
    # erste drei Bytes
    r3 = rahmen(s, (xc[1], yc), 0.66, 0.34, ORANGE, 2.5)
    p3 = pfk(s, (xc[1], yc - 0.19), (xc[1], 0.62), ORANGE, 2.5)
    yd, yv, yz = 0.5, 0.18, -0.12
    g4 = s.raster(BITS8, (-3.3, yd), groesse=TK)
    cw = tt_breite(TK, 1)
    x0 = -3.3
    l6 = L(s, "g6", w["g6"], (x0 + 27 * cw + 0.12, yd), FM, "left", GRAU)
    werte = [tx(s, str(v), (x0 + (7 * k + 3) * cw, yv), TK, "center", GRAU) for k, v in enumerate((48, 13, 25, 60))]
    zeichen = [tx(s, c, (x0 + (7 * k + 3) * cw, yz), 22, "center", ORANGE) for k, c in enumerate("wNZ8")]
    tab = s.raster(B64TAB, (0.25, 0.62), groesse=TK, zeilenabstand=1.25)
    # letztes Byte
    r31 = rahmen(s, (xc[31], yc), 0.24, 0.34, ORANGE, 2.5)
    p31 = pfk(s, (xc[31], yc - 0.19), (xc[31], 0.62), ORANGE, 2.5)
    xr0 = 2.6
    g5 = s.raster("01111100", (xr0, yd), groesse=TK)
    m5 = g5.markieren(0, 4, 7, ORANGE, 0.3)
    null2 = tx(s, "00", (xr0 + 8 * cw, yd), TK, "left", ORANGE)
    xw = xr0 + 7 * cw
    l_rest = L(s, "rest", w["rest"], (xw - 0.3, yv), FM, "right", GRAU)
    w48 = tx(s, "48", (xw, yv), TK, "center", GRAU)
    zw = tx(s, "w", (xw, yz), 22, "center", ORANGE)
    # Fingerabdruck
    yf = -0.85
    g7 = s.raster(HOST_FP, (-2.9, yf), groesse=20)
    m7 = [g7.markieren(0, 7, 10, ORANGE, 0.3), g7.markieren(0, 49, 49, ORANGE, 0.3)]
    k7 = g7.klammer(0, 7, 49, T(s, "z43", *w["z43"]), "unten", BLAU, FM)
    ne = gleich_nicht(s, g7.rechts + 0.35, yf, 20)
    schritt(s, EIN(g1.ids, 0.6))
    schritt(s, ZEICHNE(k1[0], 0.5), EIN(k1[1], 0.5))
    s.pause(0.4)
    schritt(s, ZEICHNE(p1, 0.5), EIN(l1, 0.5))
    schritt(s, EIN(bytes51 + [l51], 0.6))
    schritt(s, EIN([trichter, l_sha], 0.5))
    schritt(s, EIN(k32 + h32 + [l32], 0.7))
    s.pause(0.5)
    schritt(s, EIN(r3, 0.4), ZEICHNE(p3, 0.4))
    schritt(s, EIN(g4.ids, 0.5))
    s.ersetzen(g4.ids[0], BITS6, dauer=0.8)
    schritt(s, EIN(l6, 0.4))
    schritt(s, EIN(tab.ids + werte, 0.6))
    schritt(s, EIN(zeichen, 0.6))
    s.pause(0.4)
    schritt(s, EIN(r31, 0.4), ZEICHNE(p31, 0.4))
    schritt(s, EIN(g5.ids, 0.5))
    schritt(s, EIN(m5, 0.4))
    schritt(s, EIN([null2, l_rest], 0.5))
    schritt(s, EIN([w48, zw], 0.5))
    s.pause(0.5)
    schritt(s, EIN(g7.ids + m7, 0.6))
    schritt(s, ZEICHNE(k7[0], 0.5), EIN(k7[1], 0.5))
    schritt(s, EIN(ne, 0.5))
    s.speichern()


KEYGEN_L = "ssh-keygen -l -f /etc/ssh/ssh_host_ed25519_key.pub"
FP_ZEILE = "256 " + HOST_FP + " root@labor (ED25519)"
ERSTE = ["The authenticity of host 'localhost (127.0.0.1)' can't be established.",
         "ED25519 key fingerprint is: " + HOST_FP,
         "This key is not known by any other names.",
         "Are you sure you want to continue connecting (yes/no/[fingerprint])? "]
ADDED = "Warning: Permanently added 'localhost' (ED25519) to the list of known hosts."
DENIED = "student@localhost: Permission denied (publickey)."
W_EV = {"gleich": ("gleich", "identical", "idénticos", "相同", "identiques", "aynı"),
        "noch": ("Der Server hat sich ausgewiesen, du dich noch nicht.", "The server has proved its identity; you have not yet.",
                 "El servidor se ha identificado; tú todavía no.", "服务器已证明身份，你还没有。",
                 "Le serveur s'est identifié, toi pas encore.", "Sunucu kimliğini kanıtladı, sen henüz değil.")}


def k11ersteverbindung():
    """Terminal (Heft 2.3/2.4, Mitschrift s2_fingerabdruck, s2_erste): ssh-keygen -l zeigt den Fingerabdruck,
    ssh localhost fragt. Beide Fingerabdrücke lösen sich als Kärtchen, stehen untereinander, ein Lineal fährt über sie,
    sie werden grün. Dann yes, die Warning-Zeile und Permission denied (rot: der Server hat sich ausgewiesen, du nicht)."""
    s = Szene("linux/k11ersteverbindung", reihenfolge="anlegen")
    w = W_EV
    sp = max(len(P11 + KEYGEN_L), len(ERSTE[1]), len(ADDED))
    t = s.terminal(pos=(-3.25, 2.75), spalten=sp, zeilen=10, prompt=P11, titel=TITEL, groesse=TT)
    cw, lh = t.zelle
    n = len(HOST_FP)
    xT = t.x(28)
    yA = t.unten_kante - 0.32
    yB = yA - lh - 0.12
    la = [tx(s, "ssh-keygen -l", (xT - 0.2, yA), TK, "right", GRAU), tx(s, "ssh localhost", (xT - 0.2, yB), TK, "right", GRAU)]
    schritt(s, EIN(t.id, 0.6))
    t.befehl(KEYGEN_L, FP_ZEILE, pfad=PFAD, tempo=32)
    t.eingabe("ssh localhost", tempo=20)
    t.schritt("\n".join(ERSTE), 0.8)
    kA = box(s, (t.xm(4, 3 + n), t.y(1)), n * cw + 0.12, lh + 0.04, GRAU, WEISS, 1.5, "rect")
    cA = t.teil(1, 4, 3 + n, farbe=SCHWARZ)
    kB = box(s, (t.xm(28, 27 + n), t.y(4)), n * cw + 0.12, lh + 0.04, GRAU, WEISS, 1.5, "rect")
    cB = t.teil(4, 28, 27 + n, farbe=SCHWARZ)
    lineal = lin(s, (xT - 0.02, yA + lh / 2 + 0.08), (xT - 0.02, yB - lh / 2 - 0.08), ORANGE, 3)
    gA = tx(s, HOST_FP, (xT, yA), TT, "left", GRUEN)
    gB = tx(s, HOST_FP, (xT, yB), TT, "left", GRUEN)
    hk = haken(s, xT + n * cw + 0.22, (yA + yB) / 2, GRUEN, 0.1, 4)
    l_gl = L(s, "gleich", w["gleich"], (xT + n * cw + 0.22, yB - 0.3), FM, "center", GRUEN)
    s.pause(0.3)
    schritt(s, EIN([kA, cA, kB, cB], 0.5))
    schritt(s, VER(kA, xT - t.x(4), yA - t.y(1), 0.9), VER(cA, xT - t.x(4), yA - t.y(1), 0.9),
           VER(kB, 0, yB - t.y(4), 0.9), VER(cB, 0, yB - t.y(4), 0.9), EIN(la, 0.9))
    schritt(s, EIN(lineal, 0.3))
    schritt(s, VER(lineal, n * cw + 0.04, 0, 1.6))
    schritt(s, EIN([gA, gB], 0.6), AUS([cA, cB, lineal], 0.6))
    schritt(s, EIN(hk + [l_gl], 0.5))
    s.pause(0.5)
    t.eingabe("yes", tempo=8)
    t.ausgabe(ADDED, dauer=0.6)
    t.ausgabe(DENIED, dauer=0.6)
    md = t.markieren(8, 0, len(DENIED) - 1, ROT, 0.3)
    l_no = L(s, "noch", w["noch"], (t.links, yB - 0.6), FM, "left", ROT)
    schritt(s, EIN([md, l_no], 0.6))
    t.prompt(pfad=PFAD)
    s.speichern()


KH_ZEILE = "|1|plxWO27Yo4dtbmZo0bgV0WfLaHo=|1dCnqs8a0nMi7VhJCi3Ks3idVhg= ssh-ed25519 " + HOST_B64
KH_NAME = "|1|plxWO27Yo4dtbmZo0bgV0WfLaHo=|1dCnqs8a0nMi7VhJCi3Ks3idVhg="
W_KH = {"name": ("unkenntlicher Name", "unreadable name", "nombre ilegible", "不可辨认的名称", "nom illisible", "okunamaz ad"),
        "zufall": ("Zufallszahl", "random number", "número aleatorio", "随机数", "nombre aléatoire", "rastgele sayı"),
        "pruef": ("Prüfsumme aus Zufallszahl und Name", "checksum of random number and name",
                  "suma de comprobación de número y nombre", "由随机数和名称算出的校验和", "somme de contrôle du nombre et du nom",
                  "rastgele sayı ve addan sağlama"),
        "typ": ("Typ", "type", "tipo", "类型", "type", "tür"),
        "hostkey": ("öffentlicher Hostschlüssel", "public host key", "clave pública del host", "主机公钥", "clé publique de l'hôte",
                    "açık sunucu anahtarı"),
        "machine": ("Prüfsumme", "checksum", "suma de\ncomprobación", "校验和", "somme de\ncontrôle", "sağlama"),
        "zufall2": ("Zufallszahl", "random number", "número aleatorio", "随机数", "nombre aléatoire", "rastgele sayı"),
        "anders": ("anderes Ergebnis", "different result", "otro resultado", "结果不同", "autre résultat", "farklı sonuç"),
        "passt": ("passt", "matches", "coincide", "匹配", "correspond", "eşleşir"),
        "kein": ("kein Treffer", "no match", "no coincide", "不匹配", "non trouvé", "eşleşme yok")}


def k11knownhosts():
    """Oben ~/.ssh/known_hosts (hell) mit der einen Zeile (Heft 2.5), umbrochen. Darunter die drei Teile auf eigenen
    Zeilen mit Klammern: Zufallszahl / Prüfsumme aus Zufallszahl und Name (zusammen „unkenntlicher Name“), Typ,
    öffentlicher Hostschlüssel. Unten die Maschine: localhost + Zufallszahl → Prüfsumme = Datei (Haken); rechner1 →
    anderes Ergebnis (kein Treffer)."""
    s = Szene("linux/k11knownhosts", reihenfolge="anlegen")
    w = W_KH
    d = s.datei("~/.ssh/known_hosts", KH_ZEILE, pos=(-3.42, 3.05), spalten=72, groesse=TT)
    m_n = d.markieren(0, 0, 59, BLAU, 0.18)
    m_t = d.markieren(0, 61, 71, GRUEN, 0.18)
    m_k = d.markieren(1, 1, 68, ORANGE, 0.18)
    x0 = -3.3
    r0 = s.raster(KH_NAME, (x0, 1.72), groesse=TK)
    kz = r0.klammer(0, 3, 30, T(s, "zufall", *w["zufall"]), "oben", BLAU, FM)
    kp = r0.klammer(0, 32, 59, T(s, "pruef", *w["pruef"]), "oben", BLAU, FM)
    kn = r0.klammer(0, 0, 59, T(s, "name", *w["name"]), "unten", BLAU, FM)
    r1 = s.raster("ssh-ed25519", (x0, 0.98), groesse=TK)
    kt = r1.klammer(0, 0, 10, T(s, "typ", *w["typ"]), "oben", GRUEN, FM)
    r2 = s.raster(HOST_B64, (x0, 0.38), groesse=TK)
    kk = r2.klammer(0, 0, 67, T(s, "hostkey", *w["hostkey"]), "oben", ORANGE, FM)
    # Maschine
    ym1, ym2 = -0.5, -1.0
    ymm = (ym1 + ym2) / 2
    e1 = chip(s, (-2.85, ym1), "localhost", GRAU, WEISS)
    e2 = chip(s, (-2.85, ym2), "rechner1", GRAU, WEISS)
    zf = wchip(s, (-1.3, ymm), "zufall2", w["zufall2"], 1.25, BLAU, BLAU_HELL, h=0.3)
    xm_ = 0.3
    ma = [box(s, (xm_, ymm), 1.1, 0.85, DUNKEL, GRAU_HELL, 2.5, "round"), L(s, "machine", w["machine"], (xm_, ymm), FM, "center")]
    pe1 = pfk(s, (-2.3, ym1), (xm_ - 0.57, ym1 + 0.05), DUNKEL, 2)
    pe2 = pfk(s, (-2.35, ym2), (xm_ - 0.57, ym2 - 0.05), DUNKEL, 2)
    pz = pfk(s, (-0.66, ymm), (xm_ - 0.57, ymm), BLAU, 2)
    a1 = pfk(s, (xm_ + 0.57, ym1 + 0.05), (1.07, ym1), DUNKEL, 2)
    o1 = chip(s, (1.6, ym1), "1dCnqs8a…", GRUEN, GRUEN_HELL)
    h1 = haken(s, 2.4, ym1, GRUEN, 0.1, 4)
    l1 = L(s, "passt", w["passt"], (2.56, ym1), FM, "left", GRUEN)
    a2 = pfk(s, (xm_ + 0.57, ym2 - 0.05), (1.07, ym2), DUNKEL, 2)
    o2 = wchip(s, (1.72, ym2), "anders", w["anders"], 1.25, GRAU, WEISS, h=0.3)
    x2 = kreuz(s, 2.4, ym2, 0.16)
    l2 = L(s, "kein", w["kein"], (2.56, ym2), FM, "left", ROT)
    mg = r0.markieren(0, 32, 59, GRUEN, 0.3)
    schritt(s, EIN(d.id, 0.6))
    s.pause(0.4)
    schritt(s, EIN(m_n, 0.4))
    schritt(s, EIN(r0.ids, 0.5))
    schritt(s, ZEICHNE([kz[0], kp[0]], 0.5), EIN([kz[1], kp[1]], 0.5))
    schritt(s, ZEICHNE(kn[0], 0.5), EIN(kn[1], 0.5))
    schritt(s, EIN([m_t] + r1.ids, 0.5))
    schritt(s, ZEICHNE(kt[0], 0.4), EIN(kt[1], 0.4))
    schritt(s, EIN([m_k] + r2.ids, 0.5))
    schritt(s, ZEICHNE(kk[0], 0.4), EIN(kk[1], 0.4))
    s.pause(0.6)
    schritt(s, EIN(ma + zf, 0.6), ZEICHNE(pz, 0.6))
    schritt(s, EIN(e1, 0.4))
    schritt(s, ZEICHNE(pe1, 0.5))
    schritt(s, ZEICHNE(a1, 0.4), EIN(o1, 0.5))
    schritt(s, EIN(h1 + [l1, mg], 0.5))
    s.pause(0.4)
    schritt(s, EIN(e2, 0.4))
    schritt(s, ZEICHNE(pe2, 0.5))
    schritt(s, ZEICHNE(a2, 0.4), EIN(o2, 0.5))
    schritt(s, EIN([x2, l2], 0.5))
    s.speichern()


WARN_CMD = "ssh -o UserKnownHostsFile=falsch_known_hosts localhost"
WARNUNG = ["@" * 59,
           "@    WARNING: REMOTE HOST IDENTIFICATION HAS CHANGED!     @",
           "@" * 59,
           "IT IS POSSIBLE THAT SOMEONE IS DOING SOMETHING NASTY!",
           "Someone could be eavesdropping on you right now (man-in-the-middle attack)!",
           "It is also possible that a host key has just been changed.",
           "The fingerprint for the ED25519 key sent by the remote host is",
           HOST_FP + ".",
           "Please contact your system administrator.",
           "Add correct host key in falsch_known_hosts to get rid of this message.",
           "Offending ED25519 key in falsch_known_hosts:1",
           "  remove with:",
           "  ssh-keygen -f 'falsch_known_hosts' -R 'localhost'",
           "Host key for localhost has changed and you have requested strict checking."]
FAILED = "Host key verification failed."
W_WA = {"geaendert": ("Fingerabdruck\ngeändert", "fingerprint\nchanged", "huella\ncambiada", "指纹\n变了", "empreinte\nmodifiée",
                      "parmak izi\ndeğişti"),
        "neu": ("Server neu installiert, vom Betreuer bestätigt?", "Server reinstalled, confirmed by the admin?",
                "¿Servidor reinstalado, confirmado por el administrador?", "服务器重装过，并经管理员确认？",
                "Serveur réinstallé, confirmé par l'administrateur ?", "Sunucu yeniden kuruldu, yönetici onayladı mı?"),
        "dann": ("neu verbinden, neuen Fingerabdruck prüfen", "reconnect, check the new fingerprint",
                 "reconectar, comprobar la nueva huella", "重新连接，核对新指纹", "se reconnecter, vérifier la nouvelle empreinte",
                 "yeniden bağlan, yeni parmak izini denetle"),
        "unbek": ("unbekannt", "unknown", "desconocido", "不明", "inconnu", "bilinmiyor"),
        "nicht": ("nicht verbinden, nachfragen", "do not connect, ask", "no conectar, preguntar", "不要连接，先询问",
                  "ne pas se connecter, demander", "bağlanma, sor")}


def k11warnung():
    """Oben das Terminal mit der Warnung (Heft 2.6, Mitschrift s2_falsch) bis Host key verification failed. (rot),
    @-Kasten rot umrandet. Darunter das Schema: Fingerabdruck geändert → grün „Server neu installiert, vom Betreuer
    bestätigt?“ → ssh-keygen -R, neu verbinden, neuen Fingerabdruck prüfen; rot „unbekannt“ → nicht verbinden, nachfragen."""
    s = Szene("linux/k11warnung", reihenfolge="anlegen")
    w = W_WA
    t = s.terminal(pos=(-3.3, 3.1), spalten=len(P11 + WARN_CMD), zeilen=17, prompt=P11, titel=TITEL, groesse=TT)
    schritt(s, EIN(t.id, 0.6))
    t.eingabe(WARN_CMD, tempo=30)
    t.ausgabe("\n".join(WARNUNG), dauer=0.8)
    t.ausgabe(FAILED, dauer=0.5)
    t.prompt(pfad=PFAD)
    r_at = t.rahmen(1, 0, 58, ROT, 2.5, bis=3, rand=0.0)
    m_f = t.markieren(1 + len(WARNUNG), 0, len(FAILED) - 1, ROT, 0.35)
    schritt(s, EIN([r_at, m_f], 0.6))
    s.pause(0.6)
    y0 = t.unten_kante - 0.75
    st = [box(s, (-2.55, y0 - 0.35), 1.6, 0.62, DUNKEL, GELB, 2.5, "round"),
          L(s, "geaendert", w["geaendert"], (-2.55, y0 - 0.35), FM, "center", DUNKEL)]
    xg = -0.85
    gr = [box(s, (1.28, y0 + 0.05), 4.25, 0.92, GRUEN, GRUEN_HELL, 2.5, "round"),
          L(s, "neu", w["neu"], (xg + 0.1, y0 + 0.33), FM, "left", DUNKEL),
          tx(s, "ssh-keygen -R", (xg + 0.1, y0 + 0.05), TK, "left", DUNKEL),
          L(s, "dann", w["dann"], (xg + 0.1, y0 - 0.23), FM, "left", DUNKEL)]
    rt = [box(s, (1.28, y0 - 0.9), 4.25, 0.62, ROT, ROT_HELL, 2.5, "round"),
          L(s, "unbek", w["unbek"], (xg + 0.1, y0 - 0.78), FM, "left", ROT),
          L(s, "nicht", w["nicht"], (xg + 0.1, y0 - 1.02), FM, "left", DUNKEL)]
    pg = pfk(s, (-1.74, y0 - 0.2), (xg - 0.03, y0 + 0.05), GRUEN, 2.5)
    pr = pfk(s, (-1.74, y0 - 0.5), (xg - 0.03, y0 - 0.9), ROT, 2.5)
    schritt(s, EIN(st, 0.6))
    schritt(s, ZEICHNE(pg, 0.5), EIN(gr, 0.6))
    schritt(s, ZEICHNE(pr, 0.5), EIN(rt, 0.6))
    s.speichern()


# ================================================================== Abschnitt 3: Anmelden mit einem Schlüsselpaar
KEYGEN_CMD = "ssh-keygen -t ed25519 -f uebungsschluessel"
RANDOMART = ["+--[ED25519 256]--+",
             "|      o+o.o..oo o|",
             "|     +.o...... o |",
             "|    . o o  . .. .|",
             "|       . . +++oo |",
             "|        S .oOo=..|",
             "|         o * O.+.|",
             "|        . o O.o.o|",
             "|         . +..E. |",
             "|        .o=.  .. |",
             "+----[SHA256]-----+"]
W_KG = {"privat": ("privat, bleibt hier", "private, stays here", "privada, se queda aquí", "私有，留在这里", "privée, reste ici",
                   "özel, burada kalır"),
        "oeff": ("öffentlich, darf weitergegeben werden", "public, may be passed on", "pública, se puede compartir",
                 "公开，可以分发", "publique, peut être transmise", "açık, paylaşılabilir")}


def dateikarte(s, x0, y, name, key, wl, privat):
    """Dateikärtchen: Schlüssel (blau), bei privat mit Schloss, Dateiname und Beschriftung (Ergebnis Liste)."""
    b, h = 3.15, 0.62
    teile = [box(s, (x0 + b / 2, y), b, h, K_USER, WEISS, 2, "round")]
    teile += schluessel(s, x0 + 0.32, y + 0.08, K_USER, BLAU_HELL if privat else WEISS, g=0.85)
    if privat:
        teile.append(s.schloss((x0 + 0.72, y + 0.08), 0.22, farbe=DUNKEL))
    xn = x0 + (0.92 if privat else 0.68)
    teile.append(tx(s, name, (xn, y + 0.1), TK, "left"))
    teile.append(L(s, key, wl, (xn, y - 0.15), FM, "left", K_USER))
    return teile


def k11keygen():
    """Terminal (Heft 3.2, Werte des Hefts): ssh-keygen -t ed25519 -f uebungsschluessel mit zwei leeren
    Passphrase-Fragen, Speicherorten, Fingerabdruck und Bild aus Zeichen. Rechts neben dem Zeichenbild erscheinen
    nacheinander die Kärtchen uebungsschluessel (Schloss, privat, bleibt hier) und uebungsschluessel.pub (öffentlich)."""
    s = Szene("linux/k11keygen", reihenfolge="anlegen")
    w = W_KG
    t = s.terminal(pos=(-3.0, 2.9), spalten=len(P11 + KEYGEN_CMD), zeilen=21, prompt=P11, titel=TITEL, groesse=TT)
    schritt(s, EIN(t.id, 0.6))
    t.eingabe(KEYGEN_CMD, tempo=24)
    t.ausgabe("Generating public/private ed25519 key pair.", dauer=0.4)
    t.schritt('Enter passphrase for "uebungsschluessel" (empty for no passphrase): ', 0.5)
    t.warten(0.8)
    t.eingabe("", dauer=0.3)
    t.schritt("Enter same passphrase again: ", 0.4)
    t.eingabe("", dauer=0.3)
    t.ausgabe("\n".join(["Your identification has been saved in uebungsschluessel",
                         "Your public key has been saved in uebungsschluessel.pub",
                         "The key fingerprint is:",
                         USER_FP + " student@labor",
                         "The key's randomart image is:"]), dauer=0.6)
    t.ausgabe("\n".join(RANDOMART), dauer=0.6)
    t.prompt(pfad=PFAD)
    xk = t.x(23)
    k1 = dateikarte(s, xk, t.y(12), "uebungsschluessel", "privat", w["privat"], True)
    k2 = dateikarte(s, xk, t.y(16), "uebungsschluessel.pub", "oeff", w["oeff"], False)
    s.pause(0.5)
    schritt(s, EIN(k1, 0.6))
    s.pause(0.3)
    schritt(s, EIN(k2, 0.6))
    s.speichern()


AK = ["ssh-ed25519 AAAA… student@labor", "ssh-ed25519 AAAA… Laptop von Anna", "ssh-ed25519 AAAA… Arbeitsrechner"]
W_AK = {"gest": ("gestohlen", "stolen", "robado", "被盗", "volé", "çalındı")}


def k11authorizedkeys():
    """Rechts der Server mit ~/.ssh/authorized_keys (hell, Rechte rw-------): drei Zeilen (student@labor aus dem Heft,
    Laptop von Anna, Arbeitsrechner, gekürzt mit …). Links je ein Gerät mit Schloss, eine Linie zu seiner Zeile. Der
    Laptop wird rot durchgestrichen (gestohlen), seine Zeile verschwindet, die dritte rückt nach; die anderen Geräte
    kommen weiter herein (Haken)."""
    s = Szene("linux/k11authorizedkeys", reihenfolge="anlegen")
    w = W_AK
    br = block(s, -1.0, 3.42, 0.15, 2.6, "server", W_SERVER)
    rechte = tx(s, "rw-------", (3.32, 2.43), TK, "right", GRAU)
    t = s.terminal(text="\n".join(AK), pos=(-0.85, 2.18), spalten=34, zeilen=3, titel="~/.ssh/authorized_keys", groesse=20,
                   stil="hell", rahmen="datei", knoepfe="x", cursor=False, farbprompt=False)
    xd = -2.75
    yg = [2.05, 1.35, 0.65]
    geraete = [rechner(s, xd, yg[0]), laptop(s, xd, yg[1]), rechner(s, xd, yg[2])]
    schl = [s.schloss((xd + 0.42, y), 0.22, farbe=DUNKEL) for y in yg]
    xl0, xl1 = xd + 0.62, t.links - 0.04
    linien = [lin(s, (xl0, yg[k]), (xl1, t.y(k)), GRAU, 2) for k in range(3)]
    neu3 = lin(s, (xl0, yg[2]), (xl1, t.y(1)), GRAU, 2)
    x_l = kreuz(s, xd, yg[1], 0.32)
    l_g = L(s, "gest", w["gest"], (xd, yg[1] - 0.36), FM, "center", ROT)
    h = [haken(s, xd - 0.45, y, GRUEN, 0.09, 4) for y in (yg[0], yg[2])]
    schritt(s, EIN(br + [rechte, t.id], 0.6))
    s.pause(0.3)
    schritt(s, EIN(flach(geraete) + schl, 0.6))
    schritt(s, ZEICHNE(linien, 0.6))
    s.pause(0.5)
    schritt(s, WACHS(x_l, 0.5), EIN(l_g, 0.5))
    with s.gleichzeitig():
        t.schritt("\\e[2;1H\\e[K", 0.6)
        schritt(s, AUS(linien[1], 0.6))
    with s.gleichzeitig():
        t.schritt("\\e[2;1H" + AK[2] + "\\e[3;1H\\e[K", 0.7)
        schritt(s, AUS(linien[2], 0.5), ZEICHNE(neu3, 0.7))
    s.pause(0.3)
    schritt(s, EIN(flach(h), 0.5))
    s.speichern()


W_SP = {"verb": ("Verbindung", "connection", "conexión", "连接", "connexion", "bağlantı"),
        "s1": ("Server signiert mit dem Hostschlüssel, Client prüft mit known_hosts",
               "Server signs with its host key, client checks against known_hosts",
               "El servidor firma con su clave de host, el cliente comprueba con known_hosts",
               "服务器用主机密钥签名，客户端对照 known_hosts 验证",
               "Le serveur signe avec sa clé d'hôte, le client vérifie avec known_hosts",
               "Sunucu, sunucu anahtarıyla imzalar; istemci known_hosts ile doğrular"),
        "s2": ("Client bietet seinen öffentlichen Schlüssel an, Server findet ihn in authorized_keys",
               "Client offers its public key, server finds it in authorized_keys",
               "El cliente ofrece su clave pública, el servidor la encuentra en authorized_keys",
               "客户端提供公钥，服务器在 authorized_keys 中找到它",
               "Le client propose sa clé publique, le serveur la trouve dans authorized_keys",
               "İstemci açık anahtarını sunar, sunucu onu authorized_keys içinde bulur"),
        "s3": ("Client signiert mit seinem privaten Schlüssel", "Client signs with its private key",
               "El cliente firma con su clave privada", "客户端用私钥签名", "Le client signe avec sa clé privée",
               "İstemci özel anahtarıyla imzalar"),
        "s4": ("Server prüft die Signatur: angemeldet, -bash startet", "Server verifies the signature: logged in, -bash starts",
               "El servidor verifica la firma: sesión iniciada, arranca -bash", "服务器验证签名：登录成功，-bash 启动",
               "Le serveur vérifie la signature : connecté, -bash démarre", "Sunucu imzayı doğrular: oturum açıldı, -bash başlar")}


def k11schluesselpaar():
    """Pflichtbild. Links der eigene Rechner: ~/.ssh/known_hosts (mit dem Hostschlüssel), ~/linuxk11/uebungsschluessel
    (Schloss, 600), uebungsschluessel.pub; rechts der Server: /etc/ssh/ssh_host_ed25519_key (Schloss, 600 root), .pub,
    ~/.ssh/authorized_keys (mit der Kopie der .pub). Vier nummerierte Schritte über die Verbindung, Legende darunter;
    zum Schluss leuchten beide privaten Schlüssel: Sie sind an ihrem Platz geblieben."""
    s = Szene("linux/k11schluesselpaar", reihenfolge="anlegen")
    w = W_SP
    xl0, xr0, bw = -3.42, 0.95, 2.47
    bl = block(s, xl0, xl0 + bw, -0.55, 2.62, "dein", W_DEIN)
    br = block(s, xr0, xr0 + bw, -0.55, 2.62, "server", W_SERVER)
    band = [box(s, (0, 1.03), 1.7, 3.17, HELLGRAU, GRAU_HELL, 1, "rect", deckung=0.6),
            L(s, "verb", w["verb"], (0, 2.45), FM, "center", GRAU)]
    y1, y2, y3 = 2.02, 1.27, 0.55
    # links
    kh = [box(s, (xl0 + bw / 2, y1), bw - 0.2, 0.38, GRAU, WEISS, 2, "round"), tx(s, "~/.ssh/known_hosts", (xl0 + 0.2, y1), TK, "left")] + \
        schluessel(s, xl0 + bw - 0.42, y1, K_HOST, WEISS, g=0.55)
    up_k = schluessel(s, xl0 + 0.32, y2, K_USER, BLAU_HELL, g=0.9)
    up_l = s.schloss((xl0 + 0.74, y2), 0.22, farbe=DUNKEL)
    up = up_k + [up_l, tx(s, "~/linuxk11/", (xl0 + 0.93, y2 + 0.19), TK, "left", GRAU),
                 tx(s, "uebungsschluessel", (xl0 + 0.93, y2), TK, "left"), tx(s, "600", (xl0 + 0.93, y2 - 0.19), TK, "left", GRAU)]
    uo = schluessel(s, xl0 + 0.32, y3, K_USER, WEISS, g=0.9) + [tx(s, "uebungsschluessel.pub", (xl0 + 0.6, y3), TK, "left")]
    # rechts
    hp_k = schluessel(s, xr0 + 0.32, y1, K_HOST, ORANGE_HELL, g=0.9)
    hp_l = s.schloss((xr0 + 0.74, y1), 0.22, farbe=DUNKEL)
    hp = hp_k + [hp_l, tx(s, "/etc/ssh/", (xr0 + 0.9, y1 + 0.19), TK, "left", GRAU),
                 tx(s, "ssh_host_ed25519_key", (xr0 + 0.9, y1), TK, "left"), tx(s, "600 root", (xr0 + 0.9, y1 - 0.19), TK, "left", GRAU)]
    ho = schluessel(s, xr0 + 0.32, y2, K_HOST, WEISS, g=0.9) + [tx(s, "ssh_host_ed25519_key.pub", (xr0 + 0.6, y2), TK, "left")]
    ak = [box(s, (xr0 + bw / 2, y3), bw - 0.12, 0.38, GRAU, WEISS, 2, "round"), tx(s, "~/.ssh/authorized_keys", (xr0 + 0.13, y3), TK, "left")] + \
        schluessel(s, xr0 + bw - 0.3, y3, K_USER, WEISS, g=0.55)
    sh = proz(s, (xr0 + bw / 2, -0.17), "-bash", 1.0, 0.36)
    # Schritte
    xa, xb = -0.93, 0.93
    p1 = pfk(s, (xb, y1), (xa - 0.08, y1), K_HOST, 2.5)
    sg1 = siegel(s, 0.3, y1, 0.07, K_HOST)
    n1 = nr(s, -0.3, y1 + 0.2, 1)
    h1 = haken(s, -0.72, y1 - 0.24, GRUEN, 0.08, 3.5)
    p2 = pfk(s, (xa + 0.02, y3), (xb + 0.04, y3), K_USER, 2.5)
    k2 = schluessel(s, 0.0, y3 + 0.0, K_USER, WEISS, g=0.45)
    n2 = nr(s, -0.3, y3 + 0.2, 2)
    r2 = box(s, (xr0 + bw - 0.3, y3), 0.42, 0.3, ORANGE, WEISS, 2.5, "round", deckung=0.0)
    p3 = pfk(s, (xa + 0.02, y2 - 0.02), (xb + 0.04, y3 + 0.17), K_USER, 2.5)
    sg3 = siegel(s, 0.0, (y2 + y3) / 2 + 0.07, 0.07, K_USER)
    n3 = nr(s, -0.38, y2 + 0.12, 3)
    h4 = haken(s, xr0 + bw - 0.3, y3 + 0.33, GRUEN, 0.08, 3.5)
    p4 = pfk(s, (xr0 + bw / 2, y3 - 0.2), (xr0 + bw / 2, -0.17 + 0.2), BLAU, 2.5)
    n4 = nr(s, xr0 + bw / 2 + 0.25, (y3 - 0.2 - 0.17 + 0.2) / 2 + 0.02, 4)
    yl = [-0.85, -1.13, -1.41, -1.69]
    leg = [nr(s, -3.3, y, i + 1) + [Lr(s, "s%d" % (i + 1), w["s%d" % (i + 1)], (-3.1, y), FM, "left")] for i, y in enumerate(yl)]
    schritt(s, EIN(bl + br + band, 0.6))
    schritt(s, EIN(up + uo + kh, 0.7))
    schritt(s, EIN(hp + ho + ak, 0.7))
    s.pause(0.6)
    schritt(s, ZEICHNE(p1, 0.7), WACHS(sg1, 0.7), EIN(n1 + leg[0], 0.7))
    schritt(s, EIN(h1, 0.5))
    s.pause(0.5)
    schritt(s, ZEICHNE(p2, 0.7), EIN(k2 + n2 + leg[1], 0.7))
    schritt(s, EIN(r2, 0.5))
    s.pause(0.5)
    schritt(s, ZEICHNE(p3, 0.7), WACHS(sg3, 0.7), EIN(n3 + leg[2], 0.7))
    s.pause(0.3)
    schritt(s, EIN(h4, 0.5))
    schritt(s, ZEICHNE(p4, 0.5), WACHS(sh[0], 0.5), EIN([sh[1]] + n4 + leg[3], 0.6))
    s.pause(0.5)
    schritt(s, BETONE(up_k + [up_l] + hp_k + [hp_l], 1.0))
    s.speichern()


W_RE = {"datei": ("Datei", "file", "archivo", "文件", "fichier", "dosya"),
        "ueblich": ("üblich", "usual", "habitual", "通常", "habituel", "olağan"),
        "offen": ("zu offen", "too open", "demasiado abiertos", "太宽松", "trop ouverts", "fazla açık"),
        "gefahr": ("Gefahr", "danger", "peligro", "危险", "danger", "tehlike"),
        "laedt": ("ssh lädt ihn nicht", "ssh does not load it", "ssh no la carga", "ssh 不加载它", "ssh ne la charge pas",
                  "ssh onu yüklemez"),
        "verw": ("Server verweigert", "server refuses", "el servidor rechaza", "服务器拒绝", "le serveur refuse", "sunucu reddeder"),
        "kopiert": ("kopiert den\nSchlüssel", "copies\nthe key", "copia\nla clave", "复制\n密钥", "copie\nla clé", "anahtarı\nkopyalar"),
        "schreibt": ("schreibt eine\neigene Zeile", "adds a line\nof his own", "añade una\nlínea propia", "写入自己的\n一行",
                     "ajoute sa\npropre ligne", "kendi satırını\nekler"),
        "fuss": ("Ubuntu/Debian: Der Server erlaubt Schreibrecht für die Gruppe, wenn sie nur dich enthält.",
                 "Ubuntu/Debian: the server allows group write if the group contains only you.",
                 "Ubuntu/Debian: el servidor permite escritura del grupo si el grupo solo te contiene a ti.",
                 "Ubuntu/Debian：若组里只有你自己，服务器允许组写权限。",
                 "Ubuntu/Debian : le serveur permet l'écriture du groupe s'il ne contient que toi.",
                 "Ubuntu/Debian: grup yalnızca seni içeriyorsa sunucu grup yazma iznine izin verir.")}


def k11rechte():
    """Tabelle mit Ampeln (Heft 3.7): privater Schlüssel rw------- grün, rw-r--r-- rot „ssh lädt ihn nicht“; ~/.ssh
    rwx------ grün; authorized_keys rw------- grün, rw-----w- rot „Server verweigert“; .pub, known_hosts rw-r--r-- grün.
    Zu den roten Zeilen die Gefahr: ein anderer Benutzer kopiert den Schlüssel bzw. schreibt eine eigene Zeile hinein.
    Unten die Ausnahme von Ubuntu/Debian."""
    s = Szene("linux/k11rechte", reihenfolge="anlegen")
    w = W_RE
    xn, xg, xr, xx = -3.35, -1.25, 0.15, 1.9
    yk = 2.5
    kopf = [L(s, "datei", w["datei"], (xn, yk), FM, "left", GRAU), L(s, "ueblich", w["ueblich"], (xg - 0.12, yk), FM, "left", GRAU),
            L(s, "offen", w["offen"], (xr - 0.12, yk), FM, "left", GRAU), L(s, "gefahr", w["gefahr"], (xx, yk), FM, "left", GRAU)]
    ys = [2.0, 1.25, 0.5, -0.25]
    trenn = [lin(s, (-3.4, y + 0.38), (3.4, y + 0.38), HELLGRAU, 1.5) for y in ys]

    def recht(x, y, r, farbe):
        return [s.kreis(None, r4(x), r4(y), 0.075, farbe=farbe, dicke=1.5, fuellung=farbe, deckung=1.0),
                tx(s, r, (x + 0.17, y), TT, "left", farbe)]
    namen = [L(s, "privat", W_PRIVAT, (xn, ys[0]), FM, "left"), tx(s, "~/.ssh", (xn, ys[1]), TT, "left"),
             tx(s, "authorized_keys", (xn, ys[2]), TT, "left"), tx(s, ".pub, known_hosts", (xn, ys[3]), TT, "left")]
    gruen = [recht(xg, ys[0], "rw-------", GRUEN), recht(xg, ys[1], "rwx------", GRUEN), recht(xg, ys[2], "rw-------", GRUEN),
             recht(xg, ys[3], "rw-r--r--", GRUEN)]
    rot1 = recht(xr, ys[0], "rw-r--r--", ROT) + [L(s, "laedt", w["laedt"], (xr + 0.17, ys[0] - 0.25), FM, "left", ROT)]
    rot3 = recht(xr, ys[2], "rw-----w-", ROT) + [L(s, "verw", w["verw"], (xr + 0.17, ys[2] - 0.25), FM, "left", ROT)]
    xs, xp = 2.35, 3.15
    g1 = schluessel(s, xs, ys[0] + 0.05, K_USER, BLAU_HELL, g=0.8) + person(s, xp, ys[0] + 0.02) + \
        [pfk(s, (xs + 0.3, ys[0] + 0.05), (xp - 0.2, ys[0] + 0.05), ROT, 2, "4,3"),
         L(s, "kopiert", w["kopiert"], (2.75, ys[0] - 0.33), FM, "center", ROT)]
    dk = dok(s, xs, ys[2] + 0.03, 0.36, 0.44)
    g3 = dk + [lin(s, (xs - 0.11, ys[2] - 0.12), (xs + 0.11, ys[2] - 0.12), ROT, 3)] + person(s, xp, ys[2] + 0.02) + \
        [pfk(s, (xp - 0.2, ys[2] + 0.05), (xs + 0.24, ys[2] + 0.05), ROT, 2, "4,3"),
         L(s, "schreibt", w["schreibt"], (2.75, ys[2] - 0.38), FM, "center", ROT)]
    fuss = L(s, "fuss", w["fuss"], (xn, -0.85), FM, "left", GRAU)
    schritt(s, EIN(kopf + trenn, 0.5))
    for k in range(4):
        schritt(s, EIN([namen[k]] + gruen[k], 0.5))
        if k == 0:
            schritt(s, EIN(rot1, 0.5))
            schritt(s, EIN(g1, 0.6))
            s.pause(0.4)
        if k == 2:
            schritt(s, EIN(rot3, 0.5))
            schritt(s, EIN(g3, 0.6))
            s.pause(0.4)
    s.pause(0.3)
    schritt(s, EIN(fuss, 0.6))
    s.speichern()


W_AG = {"platte": ("auf der Platte: verschlüsselt", "on disk: encrypted", "en el disco: cifrada", "磁盘上：已加密",
                   "sur le disque : chiffrée", "diskte: şifreli"),
        "speicher": ("(Arbeitsspeicher)", "(memory)", "(memoria)", "（内存）", "(mémoire vive)", "(bellek)"),
        "pp": ("Passphrase, einmal", "passphrase, once", "frase de contraseña, una vez", "口令，只问一次", "phrase secrète, une fois",
               "parola cümlesi, bir kez"),
        "bitte": ("bitte\nsignieren", "please\nsign", "firma,\npor favor", "请签名", "signe,\ns'il te plaît", "lütfen\nimzala"),
        "ohne": ("ohne Frage", "no question asked", "sin preguntar", "无需询问", "sans question", "soru sorulmadan"),
        "leer": ("leer", "empty", "vacío", "空", "vide", "boş")}


def k11agent():
    """Links die Datei uebungsschluessel mit geschlossenem Schloss. ssh-add fragt einmal (Sprechblase ********), öffnet
    das Schloss, der entschlüsselte Schlüssel wandert in den Kasten ssh-agent (Arbeitsspeicher) mit SSH_AUTH_SOCK →
    ~/.ssh/agent/…. Drei ssh-Aufrufe bitten um eine Signatur und bekommen sie ohne Frage; die Datei bleibt verschlossen.
    Zum Schluss ssh-agent -k: Der Kasten leert sich."""
    s = Szene("linux/k11agent", reihenfolge="anlegen")
    w = W_AG
    xf, yf = -2.25, 2.15
    datei = [box(s, (xf, yf), 2.2, 0.42, GRAU, WEISS, 2, "rect")] + schluessel(s, xf - 0.82, yf, K_USER, BLAU_HELL, g=0.8)
    lk = s.schloss((xf - 0.45, yf), 0.24, farbe=DUNKEL)
    datei += [lk, tx(s, "uebungsschluessel", (xf - 0.27, yf), TK, "left")]
    l_pl = L(s, "platte", w["platte"], (xf - 1.1, yf + 0.38), FM, "left", GRAU)
    ya = 1.1
    add = proz(s, (xf, ya), "ssh-add", 1.1, 0.42)
    p_fa = pfk(s, (xf, yf - 0.22), (xf, ya + 0.22), DUNKEL, 2)
    blase = [box(s, (xf, 0.48), 1.1, 0.32, DUNKEL, WEISS, 2, "round"), lin(s, (xf - 0.1, 0.64), (xf - 0.18, ya - 0.21), DUNKEL, 2),
             tx(s, "********", (xf, 0.48), TK), L(s, "pp", w["pp"], (xf, 0.16), FM, "center", DUNKEL)]
    offen = s.schloss((xf + 0.85, ya + 0.02), 0.24, offen=True, farbe=DUNKEL)
    kc = schluessel(s, xf + 0.85, ya - 0.3, K_USER, BLAU_HELL, g=0.8)
    xa, yaa = 1.65, 1.6
    ag = [box(s, (xa, yaa), 3.45, 1.2, BLAU, BLAU_HELL, 2.5, "rect"), tx(s, "ssh-agent", (xa - 1.6, yaa + 0.4), TT, "left"),
          L(s, "speicher", w["speicher"], (xa - 1.6 + ttb("ssh-agent", TT) + 0.12, yaa + 0.4), FM, "left", DUNKEL)]
    sock = [s.kreis(None, xa, r4(yaa - 0.6), 0.08, farbe=DUNKEL, dicke=2, fuellung=WEISS, deckung=1.0),
            tx(s, "SSH_AUTH_SOCK → ~/.ssh/agent/…", (xa, 0.78), TK)]
    p_aa = pfk(s, (xf + 0.58, ya), (xa - 1.75, ya + 0.12), DUNKEL, 2)
    leer = L(s, "leer", w["leer"], (xa, yaa - 0.08), FM, "center", GRAU)
    ys = -0.4
    xs_ = [0.25, 1.65, 3.0]
    aufr, pfe, siegel_, haken_ = [], [], [], []
    for x in xs_:
        aufr.append(proz(s, (x, ys), "ssh", 0.75, 0.38))
        pfe.append(pfk(s, (x + (0.12 if x < xa else (-0.12 if x > xa else 0)), ys + 0.21), (xa + (x - xa) * 0.12, 0.64), DUNKEL, 2))
        siegel_.append(siegel(s, xa, 0.58, 0.07, K_USER))
        haken_.append(haken(s, x + 0.5, ys, GRUEN, 0.08, 3.5))
    l_bitte = L(s, "bitte", w["bitte"], (0.28, 0.3), FM, "center", DUNKEL)
    l_ohne = L(s, "ohne", w["ohne"], (xa, ys - 0.36), FM, "center", GRUEN)
    kill = [box(s, (xf, ys), 1.5, 0.38, GRAU, GRAU_HELL, 2, "rect"), tx(s, "ssh-agent -k", (xf, ys), TK)]
    p_k = pfk(s, (xf + 0.76, ys + 0.1), (xa - 1.75, yaa - 0.45), GRAU, 2)
    schritt(s, EIN(datei + [l_pl], 0.6))
    schritt(s, ZEICHNE(p_fa, 0.4), EIN(add, 0.5))
    schritt(s, EIN(blase, 0.6))
    schritt(s, EIN([offen] + kc, 0.5))
    schritt(s, EIN(ag + sock, 0.6), ZEICHNE(p_aa, 0.6))
    schritt(s, *VERS(kc, xa - (xf + 0.85), (yaa - 0.12) - (ya - 0.3), 0.9), AUS(offen, 0.6))
    s.pause(0.4)
    for k in range(3):
        schritt(s, EIN(aufr[k], 0.4), ZEICHNE(pfe[k], 0.5), *([EIN(l_bitte, 0.5)] if k == 0 else []))
        schritt(s, EIN(siegel_[k], 0.2))
        schritt(s, VER(siegel_[k], xs_[k] + 0.25 - xa, ys + 0.12 - 0.58, 0.5))
        schritt(s, EIN(haken_[k] + ([l_ohne] if k == 2 else []), 0.4))
    schritt(s, BETONE(lk, 0.8))
    s.pause(0.4)
    schritt(s, EIN(kill, 0.5), ZEICHNE(p_k, 0.5))
    schritt(s, AUS(kc, 0.6), EIN(leer, 0.6))
    s.speichern()


# ================================================================== Phase 2b-2: Helfer für die Abschnitte 4–6
TERM_BG, TERM_FG, TERM_GRAU = "#1e1e1e", "#d0cfcc", "#8a8990"   # dunkles Terminal (notizen/f1_terminal_palette.md)
TMUX_GRUEN = "#26a269"                                         # Statuszeile von tmux (ANSI-Grün der dunklen Palette)


def blitz(s, x, y, g=1.0, farbe=ORANGE):
    """Blitz (ein Signal wie SIGHUP oder ein Abbruch), Mitte (x, y), Höhe etwa 0,36·g (Ergebnis id)."""
    pts = [(0.035, 0.18), (-0.085, -0.015), (-0.01, -0.015), (-0.045, -0.18), (0.09, 0.035), (0.012, 0.035)]
    return s.vieleck(None, [(r4(x + g * a), r4(y + g * b)) for a, b in pts], farbe=farbe, deckung=1.0, dicke=1.5,
                     randfarbe=farbe)


def waage(s, x, y, g=1.0, farbe=GRUEN):
    """Balkenwaage im Gleichgewicht (Ergebnis Liste); Breite etwa 0,42·g."""
    b, r = 0.15 * g, 0.06 * g
    teile = [lin(s, (x, y - 0.11 * g), (x, y + 0.09 * g), farbe, 2),
             lin(s, (x - 0.07 * g, y - 0.11 * g), (x + 0.07 * g, y - 0.11 * g), farbe, 2.5),
             lin(s, (x - b, y + 0.09 * g), (x + b, y + 0.09 * g), farbe, 2.5)]
    for sx in (-1, 1):
        xs = x + sx * b
        teile.append(lin(s, (xs, y + 0.09 * g), (xs, y), farbe, 1.5))
        teile.append(s.weg(None, "%s+%s*cos(t)" % (r4(xs), r4(r)), "%s+%s*sin(t)" % (r4(y), r4(r)), 3.1416, 6.2832,
                           farbe=farbe, dicke=2, n=21))
    return teile


def grau_proz(s, mitte, name, b=None, h=0.4, g=TT):
    """Beendeter Prozess: grauer, gestrichelter Kasten mit grauem Namen (Ergebnis [Kasten, Name])."""
    b = b if b is not None else ttb(name, g) + 0.3
    return [box(s, mitte, b, h, GRAU, GRAU_HELL, 2, "rect", dash="5,4"), tx(s, name, mitte, g, "center", GRAU)]


def mk(s, x0, x1, y, h=0.2, farbe=ORANGE, deckung=0.25):
    """Hinterlegung von x0 bis x1 in Höhe h um y (Ergebnis id)."""
    return mark(s, r4(x0), r4(x1), r4(y), h, farbe, deckung)


def band(s, x0, x1, y0, y1, key="verb"):
    """Band „Verbindung“ zwischen zwei Blöcken (Ergebnis [Band, Beschriftung oben])."""
    return [box(s, ((x0 + x1) / 2, (y0 + y1) / 2), x1 - x0, y1 - y0, HELLGRAU, GRAU_HELL, 1, "rect", deckung=0.6),
            L(s, key, W_SP["verb"], ((x0 + x1) / 2, y1 - 0.17), FM, "center", GRAU)]


def ttchip(s, mitte, key, w, b, rand=ORANGE, fuellung=WEISS, g=TK, h=0.26):
    """Kärtchen mit übersetzter Schreibmaschinenschrift (Tasten wie Strg+B c); Ergebnis [Kasten, Text]."""
    return [box(s, mitte, b, h, rand, fuellung, 2),
            s.text(None, T(s, key, *w), (r4(mitte[0]), r4(mitte[1])), g, "center", SCHWARZ, schrift="tt")]


# ================================================================== Abschnitt 4: Bequemer verbinden, Befehle aus der Ferne
CONFIG = ["# Uebungsserver aus Linux, Kapitel 11", "Host uebung", "    HostName localhost", "    User student", "    Port 22",
          "    IdentityFile ~/linuxk11/uebungsschluessel"]
LANGBEFEHL = "ssh -p 22 -i ~/linuxk11/uebungsschluessel student@localhost"
W_CF = {"kurz": ("kurz", "short", "corto", "简写", "court", "kısa"),
        "lang": ("ausgeschrieben", "in full", "completo", "完整写法", "en entier", "açık hâli"),
        "gleich": ("Beides bewirkt dasselbe.", "Both do the same.", "Ambos hacen lo mismo.", "两者效果相同。",
                   "Les deux font la même chose.", "İkisi de aynı işi yapar.")}


def k11config():
    """Oben ~/.ssh/config (hell, Datei skripte/config, Heft 4.1), darunter der kurze Befehl ssh uebung. „uebung“ leuchtet
    in Befehl und Host-Zeile; ssh rückt nach unten, dann leuchten die vier eingerückten Zeilen nacheinander auf, und ihr
    Wert wandert in den langen Befehl ssh -p 22 -i ~/linuxk11/uebungsschluessel student@localhost (-p, -i und @ kommen
    dazu). Unten: Beides bewirkt dasselbe."""
    s = Szene("linux/k11config", reihenfolge="anlegen")
    w = W_CF
    d = s.datei("~/.ssh/config", "\n".join(CONFIG), pos=(-1.92, 3.0), spalten=46, groesse=TT)
    m_host = d.markieren(1, 5, 10, BLAU, 0.22)
    zl = {2: (13, 21, 50), 3: (9, 15, 42), 4: (9, 10, 7), 5: (17, 44, 13)}   # Zeile: Spalten in der Datei, Spalte im Befehl
    m_z = {z: d.markieren(z, 4, len(CONFIG[z]) - 1, ORANGE, 0.22) for z in zl}
    kop = {z: d.teil(z, a, b, farbe=SCHWARZ) for z, (a, b, _) in zl.items()}
    cw = tt_breite(TT, 1)
    x0, yk, yl = -2.36, 1.15, 0.4
    rk = s.raster("ssh uebung", (x0, yk), groesse=TT)
    m_k = rk.markieren(0, 4, 9, BLAU, 0.22)
    c_ssh = rk.teil(0, 0, 2, farbe=SCHWARZ)
    fest = {4: tx(s, "-p", (x0 + 4 * cw, yl), TT, "left"), 5: tx(s, "-i", (x0 + 10 * cw, yl), TT, "left"),
            3: tx(s, "@", (x0 + 49 * cw, yl), TT, "left")}
    l_k = L(s, "kurz", w["kurz"], (x0 - 0.12, yk), FM, "right", GRAU)
    l_l = L(s, "lang", w["lang"], (x0 - 0.12, yl), FM, "right", GRAU)
    l_g = L(s, "gleich", w["gleich"], (0, yl - 0.5), FS, "center", DUNKEL)
    schritt(s, EIN([d.id] + list(kop.values()), 0.6))
    s.pause(0.3)
    schritt(s, EIN(rk.ids + [c_ssh, l_k], 0.5))
    schritt(s, EIN([m_k, m_host], 0.5))
    s.pause(0.4)
    schritt(s, VER(c_ssh, 0, yl - yk, 0.6), EIN(l_l, 0.6))
    for z, (a, _b, ziel) in zl.items():
        schritt(s, EIN(m_z[z], 0.4))
        schritt(s, VER(kop[z], x0 + ziel * cw - d.x(a), yl - d.y(z), 0.8), *([EIN(fest[z], 0.8)] if z in fest else []))
    s.pause(0.4)
    schritt(s, EIN(l_g, 0.6))
    s.speichern()


ZS1 = "ssh uebung 'echo \"Verbindung: $SSH_CONNECTION\"'"
ZS2 = 'ssh uebung "echo \\"Verbindung: $SSH_CONNECTION\\""'
ZS_ARG = 'echo "Verbindung: $SSH_CONNECTION"'
ZS_ARG2 = 'echo "Verbindung: "'
ZS_OUT1 = "Verbindung: 127.0.0.1 57032 127.0.0.1 22"
W_ZS = {"dein": ("deine Shell", "your shell", "tu shell", "你的 shell", "ton shell", "senin kabuğun"),
        "dort": ("Shell auf dem Server (bash -c)", "shell on the server (bash -c)", "shell en el servidor (bash -c)",
                 "服务器上的 shell (bash -c)", "shell sur le serveur (bash -c)", "sunucudaki kabuk (bash -c)"),
        "nur": ("entfernt nur die beiden '", "removes only the two '", "solo quita las dos '", "只去掉两个 '",
                "retire seulement les deux '", "yalnızca iki ' kaldırılır"),
        "leer": ("hier leer", "empty here", "vacía aquí", "这里为空", "vide ici", "burada boş")}


def k11zweishells():
    """Zwei Bahnen (Heft 4.2, Mitschrift s4_befehl, Werte des Hefts), jede mit ihrem Befehl darüber und zwei Blöcken:
    links „deine Shell“, rechts „Shell auf dem Server (bash -c)“, dazwischen ssh. Bahn 1: Die ' ' leuchten rot, der Inhalt
    fällt als Kärtchen echo "Verbindung: $SSH_CONNECTION" in den linken Block und wandert unverändert nach rechts; dort
    wird die Variable ersetzt (blau), Ausgabe mit dem Wert grün. Bahn 2: Die Variable leuchtet schon im Befehl; links wird
    ihr Platz leer („hier leer“), zum Server geht echo "Verbindung: ", Ausgabe Verbindung:."""
    s = Szene("linux/k11zweishells", reihenfolge="anlegen")
    w = W_ZS
    cw = tt_breite(TK, 1)
    xc, xa, xb, xo = -3.3, -3.22, 0.5, 0.36           # Befehle, Text links, Text rechts, Ausgaben
    xl0, xl1, xr0, xr1 = -3.44, -0.47, 0.28, 3.44
    xs = (xl1 + xr0) / 2
    kb = len(ZS_ARG) * cw + 0.16
    kb2 = len(ZS_ARG2) * cw + 0.16
    dx = xb - xa
    bahnen = []
    for i, yc in enumerate((3.0, 1.0)):
        yt = yc - 0.25
        yk, yo = yt - 0.57, yt - 1.03
        b = {"yk": yk, "yo": yo}
        b["bl"] = block(s, xl0, xl1, yt - 1.32, yt, "dein", w["dein"])
        b["br"] = [box(s, ((xr0 + xr1) / 2, yt - 0.66), xr1 - xr0, 1.32, GRAU, WEISS, 2, "rect"),
                   Lr(s, "dort", w["dort"], (xr0 + 0.1, yt - 0.17), FM, "left", DUNKEL)]
        b["ssh"] = proz(s, (xs, yk), "ssh", g=TK)
        b["kl"] = box(s, (xa - 0.08 + kb / 2, yk), kb, 0.26, GRAU, WEISS, 1.5, "round")
        b["a1"] = pfk(s, (xa - 0.08 + kb + 0.02, yk), (xs - 0.28, yk), DUNKEL, 2, spitze=0.07)
        b["a2"] = pfk(s, (xs + 0.28, yk), (xb - 0.1, yk), DUNKEL, 2, spitze=0.07)
        b["a3"] = pfk(s, (1.8, yk - 0.15), (1.8, yo + 0.12), DUNKEL, 2, spitze=0.07)
        bahnen.append(b)
    b1, b2 = bahnen
    # Bahn 1
    r1 = s.raster(ZS1, (xc, 3.0), groesse=TK)
    q1 = [r1.markieren(0, 11, 11, ROT, 0.35), r1.markieren(0, 46, 46, ROT, 0.35)]
    c1 = r1.teil(0, 12, 45, farbe=SCHWARZ)
    l_nur = Lr(s, "nur", w["nur"], (xa - 0.08, b1["yo"]), FM, "left", ROT)
    k1 = [box(s, (xa - 0.08 + kb / 2, b1["yk"]), kb, 0.26, GRAU, WEISS, 1.5, "round"), tx(s, ZS_ARG, (xa, b1["yk"]), TK, "left")]
    m_v1 = mk(s, xb + 18 * cw, xb + 33 * cw, b1["yk"], 0.2, BLAU, 0.25)
    m_o1 = mk(s, xo + 12 * cw, xo + 40 * cw, b1["yo"], 0.2, GRUEN, 0.22)
    o1 = tx(s, ZS_OUT1, (xo, b1["yo"]), TK, "left")
    # Bahn 2
    r2 = s.raster(ZS2, (xc, 1.0), groesse=TK)
    q2 = r2.markieren(0, 31, 45, ROT, 0.3)
    yk2 = b2["yk"]
    p1 = tx(s, 'echo "Verbindung: ', (xa, yk2), TK, "left")
    vbox = box(s, (xa + 25.5 * cw, yk2), 15 * cw + 0.06, 0.2, GRAU, WEISS, 1.5, "rect", dash="3,3")
    vtext = tx(s, "$SSH_CONNECTION", (xa + 18 * cw, yk2), TK, "left")
    p3 = tx(s, '"', (xa + 33 * cw, yk2), TK, "left")
    m_v2 = mk(s, xa + 18 * cw, xa + 33 * cw, yk2, 0.2, ROT, 0.3)
    l_leer = Lr(s, "leer", w["leer"], (xa + 25.5 * cw, b2["yo"]), FM, "center", ROT)
    k2 = [box(s, (xa - 0.08 + kb2 / 2, yk2), kb2, 0.26, GRAU, WEISS, 1.5, "round"), tx(s, ZS_ARG2, (xa, yk2), TK, "left")]
    o2 = tx(s, "Verbindung:", (xo, b2["yo"]), TK, "left")
    schritt(s, EIN(b1["bl"] + b1["br"] + b1["ssh"] + b2["bl"] + b2["br"] + b2["ssh"], 0.6))
    s.pause(0.3)
    schritt(s, EIN(r1.ids + [c1], 0.5))
    schritt(s, EIN(q1, 0.5))
    schritt(s, VER(c1, xa - r1.x(12), b1["yk"] - 3.0, 0.9), EIN([b1["kl"], l_nur], 0.9))
    schritt(s, ZEICHNE(b1["a1"], 0.3))
    schritt(s, EIN(k1, 0.25))
    schritt(s, *VERS(k1, dx, 0, 1.0), ZEICHNE(b1["a2"], 1.0))
    schritt(s, EIN(m_v1, 0.4))
    schritt(s, ZEICHNE(b1["a3"], 0.3))
    schritt(s, EIN([m_o1, o1], 0.5))
    s.pause(0.6)
    schritt(s, EIN(r2.ids, 0.5))
    schritt(s, EIN(q2, 0.4))
    schritt(s, EIN([b2["kl"], p1, vbox, vtext, p3], 0.6))
    schritt(s, EIN(m_v2, 0.4))
    schritt(s, AUS([vtext, m_v2], 0.6), EIN(l_leer, 0.6))
    schritt(s, ZEICHNE(b2["a1"], 0.3))
    schritt(s, EIN(k2, 0.25))
    schritt(s, *VERS(k2, dx, 0, 1.0), ZEICHNE(b2["a2"], 1.0))
    schritt(s, ZEICHNE(b2["a3"], 0.3))
    schritt(s, EIN(o2, 0.5))
    s.speichern()


W_FM = {"hier": ("hier erweitert", "expanded here", "se expande aquí", "在这里展开", "développé ici", "burada genişletilir"),
        "kein": ("kein Treffer", "no match", "sin coincidencias", "没有匹配", "aucun résultat", "eşleşme yok"),
        "keine": ("keine Datei *.txt", "no *.txt file", "ningún archivo *.txt", "没有 *.txt 文件", "aucun fichier *.txt",
                  "*.txt dosyası yok"),
        "heim": ("(Heimatverzeichnis)", "(home directory)", "(directorio personal)", "（主目录）", "(répertoire personnel)",
                 "(ev dizini)"),
        "ausgabe": ("Ausgabe:", "output:", "salida:", "输出：", "sortie :", "çıktı:")}


def k11fernmuster():
    """Links dein Rechner mit ~/linuxk11 (einkauf.txt), rechts der Server mit dem Heimatverzeichnis ~ (keine Datei *.txt),
    dazwischen das Band Verbindung (Heft 4.3, Mitschrift s4_muster). Obere Bahn ssh uebung echo *.txt: Das Muster zeigt auf
    einkauf.txt, wird links zu einkauf.txt, das Kärtchen echo einkauf.txt wandert nach rechts, Ausgabe einkauf.txt. Untere
    Bahn ssh uebung 'echo *.txt': Das Kärtchen echo *.txt wandert unverändert, rechts kein Treffer, Ausgabe *.txt."""
    s = Szene("linux/k11fernmuster", reihenfolge="anlegen")
    w = W_FM
    cw = tt_breite(TT, 1)
    bl = block(s, -3.44, -0.62, -1.75, 2.55, "dein", W_DEIN)
    br = block(s, 0.62, 3.44, -1.75, 2.55, "server", W_SERVER)
    bd = band(s, -0.62, 0.62, -1.75, 2.55)
    # Verzeichnisse (Mitte)
    yd, yf = 0.55, 0.2
    dl = [box(s, (-2.03, 0.38), 2.5, 0.75, HELLGRAU, WEISS, 1.5, "round"), ordner_symbol(s, -3.08, yd),
          tx(s, "~/linuxk11", (-2.88, yd), TT, "left")]
    chip_e = chip(s, (-2.3, yf), "einkauf.txt", GRAU, WEISS, g=TT, h=0.26)
    r_e = box(s, (-2.3, yf), 1.12, 0.34, GRUEN, WEISS, 2.5, "round", deckung=0.0)
    dr = [box(s, (2.03, 0.38), 2.5, 0.75, HELLGRAU, WEISS, 1.5, "round"), ordner_symbol(s, 0.98, yd),
          tx(s, "~", (1.18, yd), TT, "left"), L(s, "heim", w["heim"], (1.36, yd), FM, "left", GRAU),
          Lr(s, "keine", w["keine"], (0.95, yf), FM, "left", GRAU)]
    # Bahn 1
    y1, yc1, yo1 = 1.95, 1.5, 1.08
    c1 = [tx(s, "ssh uebung echo ", (-3.3, y1), TT, "left")]
    stern1 = tx(s, "*.txt", (-3.3 + 16 * cw, y1), TT, "left", ORANGE)
    f1 = pfk(s, (-1.82, y1 - 0.12), (-2.15, yf + 0.15), ORANGE, 2, "4,3")
    l_hier = Lr(s, "hier", w["hier"], (-2.14, 1.0), FM, "right", ORANGE)
    k1 = chip(s, (-2.0, yc1), "echo einkauf.txt", DUNKEL, WEISS, g=TT, h=0.28)
    a1 = pfk(s, (-1.2, yc1), (1.28, yc1), DUNKEL, 2)
    o1 = [L(s, "ausgabe", w["ausgabe"], (2.0, yo1), FM, "right", GRAU), tx(s, "einkauf.txt", (2.1, yo1), TT, "left", GRUEN)]
    # Bahn 2
    y2, yc2, yo2 = -0.45, -0.9, -1.32
    c2 = [tx(s, "ssh uebung 'echo ", (-3.3, y2), TT, "left"), tx(s, "*.txt", (-3.3 + 17 * cw, y2), TT, "left", ORANGE),
          tx(s, "'", (-3.3 + 22 * cw, y2), TT, "left")]
    k2 = [box(s, (-2.0, yc2), 10 * cw + 0.24, 0.28, DUNKEL, WEISS, 2), tx(s, "echo ", (-2.0 - 5 * cw, yc2), TT, "left"),
          tx(s, "*.txt", (-2.0, yc2), TT, "left", ORANGE)]
    a2 = pfk(s, (-1.2, yc2), (1.53, yc2), DUNKEL, 2)
    xs2 = -2.0 + 4.03 + 2.5 * cw
    f2 = pfk(s, (xs2, yc2 + 0.15), (xs2, yf - 0.18), ORANGE, 2, "4,3")
    x2 = kreuz(s, xs2, -0.38, 0.14)
    l_kein = L(s, "kein", w["kein"], (xs2 - 0.18, -0.38), FM, "right", ROT)
    o2 = [L(s, "ausgabe2", w["ausgabe"], (2.0, yo2), FM, "right", GRAU), tx(s, "*.txt", (2.1, yo2), TT, "left", GRUEN)]
    schritt(s, EIN(bl + br + bd, 0.5))
    schritt(s, EIN(dl + chip_e + dr, 0.6))
    s.pause(0.4)
    schritt(s, EIN(c1 + [stern1], 0.5))
    schritt(s, ZEICHNE(f1, 0.6), EIN(l_hier, 0.6))
    schritt(s, EIN(r_e, 0.4))
    s.ersetzen(stern1, "einkauf.txt", farbe=ORANGE)
    schritt(s, EIN(k1, 0.3))
    schritt(s, *VERS(k1, 4.03, 0, 1.0), ZEICHNE(a1, 1.0))
    schritt(s, EIN(o1, 0.5))
    s.pause(0.6)
    schritt(s, EIN(c2, 0.5))
    schritt(s, EIN(k2, 0.3))
    schritt(s, *VERS(k2, 4.03, 0, 1.0), ZEICHNE(a2, 1.0))
    schritt(s, ZEICHNE(f2, 0.5))
    schritt(s, EIN([x2, l_kein], 0.5))
    schritt(s, EIN(o2, 0.5))
    s.speichern()


EINKAUF = ["Milch", "Brot", "Äpfel", "Kaffee"]
SORTIERT = ["Brot", "Kaffee", "Milch", "Äpfel"]
W_FS = {"pipe": ("Pipe", "pipe", "tubería", "管道", "tube", "boru"),
        "selbst": ("255: ssh selbst\ngescheitert", "255: ssh itself\nfailed", "255: falló\nel propio ssh", "255：ssh 本身\n失败",
                   "255 : ssh lui-même\na échoué", "255: ssh'nin\nkendisi başarısız")}


def k11fernstroeme():
    """Links dein Rechner, rechts der Server, dazwischen das Band Verbindung (Heft 4.4, Mitschrift s4_pipe, s4_status).
    Oben: cat linuxk11/einkauf.txt → Rohr 1 → sshd-session → durch die Verbindung (die vier Zeilen im Band) → ssh → Pipe
    → sort → sortierte Liste. Unten: bash -c 'exit 3' schickt den Zettel 3 zu ssh ($? = 3); darunter ein ssh, dessen
    Verbindung an einem roten Blitz endet, $? = 255, Schild „255: ssh selbst gescheitert“."""
    s = Szene("linux/k11fernstroeme", reihenfolge="anlegen")
    w = W_FS
    bl = block(s, -3.44, -0.8, -1.95, 2.5, "dein", W_DEIN)
    br = block(s, 0.8, 3.44, -1.95, 2.5, "server", W_SERVER)
    bd = band(s, -0.8, 0.8, -1.95, 2.5)
    xr, ys = 2.12, 0.95
    cat = proz(s, (xr, 1.85), "cat linuxk11/einkauf.txt", g=TK)
    r1 = pfk(s, (xr, 1.63), (xr, ys + 0.22), GRUEN, 3.5)
    n1 = nr(s, xr + 0.22, 1.42, 1, GRUEN)
    sshd = proz(s, (xr, ys), "sshd-session", g=TK)
    verb = pfk(s, (xr - 0.63, ys), (-1.06, ys), GRUEN, 3.5)
    last = [box(s, (0, 1.55), 0.74, 0.74, GRAU, WEISS, 1.5, "round")] + \
           [tx(s, z, (0, 1.79 - 0.16 * i), TK, "center") for i, z in enumerate(EINKAUF)]
    ssh = proz(s, (-1.35, ys), "ssh", g=TK)
    pipe = pfk(s, (-1.63, ys), (-2.53, ys), GRUEN, 3.5)
    l_pipe = L(s, "pipe", w["pipe"], (-2.08, ys + 0.2), FM, "center", GRUEN)
    sort = proz(s, (-2.85, ys), "sort", g=TK)
    raus = pfk(s, (-2.85, ys - 0.22), (-2.85, 0.53), GRUEN, 2.5)
    liste = [box(s, (-2.85, 0.13), 0.74, 0.74, GRUEN, GRUEN_HELL, 1.5, "round")] + \
            [tx(s, z, (-2.85, 0.37 - 0.16 * i), TK, "center") for i, z in enumerate(SORTIERT)]
    # unten: Exit-Status
    trenn = lin(s, (-3.3, -0.4), (3.3, -0.4), HELLGRAU, 1.5, "6,4")
    y3, y4 = -0.85, -1.55
    bash = proz(s, (xr, y3), "bash -c 'exit 3'", g=TK)
    ssh3 = proz(s, (-1.35, y3), "ssh", g=TK)
    a3 = pfk(s, (xr - 0.77, y3), (-1.07, y3), GRAU, 2)
    z3 = zettel(s, 1.1, y3, "3")
    l3 = tx(s, "$? =", (-2.12, y3), TK, "right")
    ssh4 = proz(s, (-1.35, y4), "ssh", g=TK)
    a4 = pfk(s, (-1.07, y4), (-0.16, y4), GRAU, 2, "5,4")
    bz = blitz(s, 0, y4, 1.0, ROT)
    l_selbst = Lr(s, "selbst", w["selbst"], (0.95, y4), FM, "left", ROT)
    z4 = zettel(s, -1.95, y4, "255", b=0.55)
    l4 = tx(s, "$? =", (-2.3, y4), TK, "right")
    schritt(s, EIN(bl + br + bd, 0.5))
    schritt(s, EIN(cat, 0.5))
    schritt(s, ZEICHNE(r1, 0.5), EIN(n1 + sshd, 0.6))
    schritt(s, ZEICHNE(verb, 0.8), EIN(last, 0.8))
    schritt(s, EIN(ssh, 0.4))
    schritt(s, ZEICHNE(pipe, 0.6), EIN([l_pipe] + sort, 0.6))
    schritt(s, ZEICHNE(raus, 0.4), EIN(liste, 0.6))
    s.pause(0.6)
    schritt(s, EIN([trenn] + bash + ssh3, 0.5))
    schritt(s, EIN(z3, 0.3))
    schritt(s, *VERS(z3, -1.95 + 0.1 - 1.1, 0, 0.9), ZEICHNE(a3, 0.9))
    schritt(s, EIN(l3, 0.4))
    s.pause(0.5)
    schritt(s, EIN(ssh4, 0.4), ZEICHNE(a4, 0.5))
    schritt(s, WACHS(bz, 0.5), EIN(l_selbst, 0.6))
    schritt(s, EIN(z4 + [l4], 0.5))
    s.speichern()


W_TY = {"pt": ("Pseudoterminal", "pseudo-terminal", "pseudoterminal", "伪终端", "pseudo-terminal", "sözde uçbirim"),
        "unv": ("unverändert", "unchanged", "sin cambios", "不变", "inchangé", "değişmeden"),
        "ver": ("vom Terminal verändert", "changed by the terminal", "cambiado por el terminal", "被终端改变",
                "modifié par le terminal", "uçbirim değiştirir"),
        "legende": ("10 = Zeilenende, 13 = Wagenrücklauf", "10 = line feed, 13 = carriage return",
                    "10 = salto de línea, 13 = retorno de carro", "10 = 换行，13 = 回车", "10 = fin de ligne, 13 = retour chariot",
                    "10 = satır sonu, 13 = satır başı"),
        "anm": ("(Anmeldung)", "(login)", "(inicio de sesión)", "（登录）", "(connexion)", "(oturum açma)")}


def k11tty():
    """Drei Zeilen (Heft 4.5, Mitschrift s4_tty): links der Befehl und die Antwort, rechts auf dem Server sshd-session,
    Pseudoterminal pts/3 und das Programm. (1) ssh uebung: pts/3 zwischen sshd-session und -bash. (2) ssh uebung tty:
    gerades Rohr, das Byte 10 kommt unverändert an, Antwort not a tty. (3) ssh -t uebung tty: das Byte 10 läuft durch pts/3
    und kommt als 13 10 heraus, Antwort /dev/pts/3. Unten die Legende 10 = Zeilenende, 13 = Wagenrücklauf."""
    s = Szene("linux/k11tty", reihenfolge="anlegen")
    w = W_TY
    bl = block(s, -3.44, -1.45, -1.55, 2.45, "dein", W_DEIN)
    br = block(s, -1.15, 3.44, -1.55, 2.45, "server", W_SERVER)
    ys = [1.65, 0.6, -0.45]
    befehle = ["ssh uebung", "ssh uebung tty", "ssh -t uebung tty"]
    progs = ["-bash", "tty", "tty"]
    xs, xp, xg = -0.45, 1.05, 2.45
    z = []
    for i, y in enumerate(ys):
        r = {"cmd": tx(s, befehle[i], (-3.3, y), TT, "left"), "a": pfk(s, (-1.88, y), (-1.08, y), DUNKEL, 2),
             "sshd": proz(s, (xs, y), "sshd-session", g=TK), "prog": proz(s, (xg, y), progs[i], g=TK)}
        bp = ttb(progs[i], TK) + 0.3
        if i != 1:
            r["pts"] = [box(s, (xp, y), 0.64, 0.34, "#0f0f0f", TERM_BG, 1.5, "rect"), tx(s, "pts/3", (xp, y), TK, "center", TERM_FG),
                        lin(s, (xs + 0.61, y), (xp - 0.32, y), GRAU, 2), lin(s, (xp + 0.32, y), (xg - bp / 2, y), GRAU, 2)]
        else:
            r["pts"] = [pfk(s, (xg - bp / 2 - 0.01, y), (xs + 0.62, y), GRUEN, 3)]
        z.append(r)
    l_pt = L(s, "pt", w["pt"], (xp, ys[0] + 0.32), FM, "center", GRAU)
    ant = [L(s, "anm", w["anm"], (-3.3, ys[0] - 0.3), FM, "left", GRAU), tx(s, "not a tty", (-3.3, ys[1] - 0.3), TT, "left"),
           tx(s, "/dev/pts/3", (-3.3, ys[2] - 0.3), TT, "left")]
    c10 = chip(s, (1.95, ys[1]), "10", GRUEN, GRUEN_HELL, g=TK, h=0.24, b=0.4)
    l_unv = L(s, "unv", w["unv"], (0.44, ys[1] - 0.33), FM, "center", GRUEN)
    c10b = chip(s, (1.75, ys[2]), "10", GRUEN, GRUEN_HELL, g=TK, h=0.24, b=0.4)
    c1310 = chip(s, (0.44, ys[2]), "13 10", ORANGE, ORANGE_HELL, g=TK, h=0.24, b=0.52)
    l_ver = L(s, "ver", w["ver"], (0.44, ys[2] - 0.33), FM, "center", ORANGE)
    leg = Lr(s, "legende", w["legende"], (-1.05, -1.22), FM, "left", GRAU)
    schritt(s, EIN(bl + br, 0.5))
    for i in range(3):
        r = z[i]
        s.pause(0.3)
        schritt(s, EIN(r["cmd"], 0.4))
        schritt(s, ZEICHNE(r["a"], 0.4), EIN(r["sshd"], 0.5))
        if i == 0:
            schritt(s, EIN(r["pts"] + r["prog"] + [l_pt], 0.6))
            schritt(s, EIN(ant[0], 0.4))
        elif i == 1:
            schritt(s, EIN(r["prog"], 0.4))
            schritt(s, ZEICHNE(r["pts"], 0.5))
            schritt(s, EIN(c10, 0.3))
            schritt(s, *VERS(c10, 0.44 - 1.95, 0, 0.8))
            schritt(s, EIN([l_unv, ant[1]], 0.5))
        else:
            schritt(s, EIN(r["pts"] + r["prog"], 0.5))
            schritt(s, EIN(c10b, 0.3))
            schritt(s, *VERS(c10b, xp - 1.75, 0, 0.6))
            schritt(s, AUS(c10b, 0.4), EIN(c1310, 0.4))
            schritt(s, EIN([l_ver, ant[2]], 0.5))
    s.pause(0.3)
    schritt(s, EIN(leg, 0.5))
    s.speichern()


# ================================================================== Abschnitt 5: Dateien übertragen
W_SC = {"hier": ("hier", "here", "aquí", "本机", "ici", "burası"),
        "kein": ("kein Doppelpunkt: lokale Kopie", "no colon: local copy", "sin dos puntos: copia local", "没有冒号：本地复制",
                 "pas de deux-points : copie locale", "iki nokta yok: yerel kopya")}


def k11scp():
    """Oben die drei Befehle (Heft 5.1, Mitschrift s5_scp, s5_doppelpunkt) mit Nummern, der Doppelpunkt rot. Darunter links
    „hier“ (~/linuxk11), rechts „uebung“ (~/linuxk11/server). (1) einkauf.txt wandert nach rechts, (2) die Kopie kommt als
    zurueck.txt zurück, (3) ohne Doppelpunkt biegt der Pfeil links in eine Datei uebung; Schild „kein Doppelpunkt: lokale
    Kopie“."""
    s = Szene("linux/k11scp", reihenfolge="anlegen")
    w = W_SC
    cw = tt_breite(TK, 1)
    xc = -3.12
    ys = [2.6, 2.27, 1.94]
    bef = []
    for i, (vor, nach) in enumerate((("scp einkauf.txt uebung", "linuxk11/server/"),
                                     ("scp uebung", "linuxk11/server/einkauf.txt zurueck.txt"))):
        sp = len(vor)
        m = mk(s, xc + sp * cw - 0.01, xc + (sp + 1) * cw + 0.01, ys[i], 0.2, ROT, 0.2)
        t = s.text(None, vor + farbig(":", ROT, fett=True) + nach, (xc, ys[i]), TK, "left", SCHWARZ, schrift="tt", ansi=True)
        bef.append([m, t])
    bef.append([tx(s, "scp einkauf.txt uebung", (xc, ys[2]), TK, "left")])
    nrn = [nr(s, -3.3, y, i + 1, [ORANGE, BLAU, ROT][i]) for i, y in enumerate(ys)]
    bl = block(s, -3.44, -0.55, -1.6, 1.6, "hier", w["hier"])
    br = [box(s, (1.995, 0), 2.89, 3.2, GRAU, WEISS, 2, "rect"), tx(s, "uebung", (0.65, 1.43), TT, "left", DUNKEL)]
    pfade = [tx(s, "~/linuxk11", (-3.34, 1.17), TK, "left", GRAU), tx(s, "~/linuxk11/server", (0.65, 1.17), TK, "left", GRAU)]
    e_l = chip(s, (-2.0, 0.6), "einkauf.txt", GRAU, WEISS, g=TT, h=0.28)
    e_r = chip(s, (2.0, 0.6), "einkauf.txt", GRAU, WEISS, g=TT, h=0.28)
    z_l = chip(s, (-2.0, -0.15), "zurueck.txt", GRAU, WEISS, g=TT, h=0.28)
    u_l = chip(s, (-2.0, -0.9), "uebung", ROT, ROT_HELL, g=TT, h=0.28)
    p1 = pfk(s, (-1.42, 0.67), (1.42, 0.67), ORANGE, 2.5)
    n1 = nr(s, 0, 0.87, 1, ORANGE)
    p2 = pfk(s, (1.42, 0.52), (-1.42, -0.1), BLAU, 2.5)
    n2 = nr(s, -0.25, -0.06, 2, BLAU)
    p3 = [lin(s, (-2.58, 0.6), (-2.85, 0.6), ROT, 2.5), pfk(s, (-2.85, 0.6), (-2.38, -0.9), ROT, 2.5, knick="vh")]
    n3 = nr(s, -3.1, -0.4, 3, ROT)
    l_kein = Lr(s, "kein", w["kein"], (-3.3, -1.3), FM, "left", ROT)
    schritt(s, EIN(bl + br + pfade + e_l, 0.6))
    s.pause(0.4)
    schritt(s, EIN(bef[0] + nrn[0], 0.5))
    schritt(s, ZEICHNE(p1, 0.7), EIN(n1, 0.7))
    schritt(s, EIN(e_r, 0.4))
    s.pause(0.4)
    schritt(s, EIN(bef[1] + nrn[1], 0.5))
    schritt(s, ZEICHNE(p2, 0.7), EIN(n2, 0.7))
    schritt(s, EIN(z_l, 0.4))
    s.pause(0.4)
    schritt(s, EIN(bef[2] + nrn[2], 0.5))
    schritt(s, ZEICHNE(p3, 0.7), EIN(n3, 0.7))
    schritt(s, EIN(u_l, 0.4))
    schritt(s, EIN(l_kein, 0.5))
    s.speichern()


SFTP_LLS = ["einkauf.txt  ssh_dateien.txt    uebungsschluessel.pub  zurueck.txt", "server       uebungsschluessel  urlaub"]
SFTP_GET = ["Fetching /home/student/linuxk11/server/einkauf.txt to aus_sftp.txt",
            "einkauf.txt                           100%   25    18.8KB/s   00:00"]
W_SF = {"dort": ("dort\n(Server)", "there\n(server)", "allí\n(servidor)", "那边\n（服务器）", "là-bas\n(serveur)", "orada\n(sunucu)"),
        "hier": ("hier\n(eigener Rechner)", "here\n(own computer)", "aquí\n(ordenador propio)", "这里\n（自己的计算机）",
                 "ici\n(ton ordinateur)", "burada\n(kendi bilgisayarın)"),
        "holt": ("holt: Server\n→ dein Rechner", "fetches: server\n→ your computer", "trae: servidor\n→ tu ordenador",
                 "取回：服务器\n→ 你的计算机", "rapatrie : serveur\n→ ton ordinateur", "getirir: sunucu\n→ bilgisayarın")}


def k11sftp():
    """Terminal (Heft 5.2, Mitschrift s5_sftp, Werte des Hefts): sftp uebung bis bye, die Eingaben hinter sftp> getippt.
    Im rechten Rand Klammern mit Etiketten: cd/ls „dort (Server)“, lls „hier (eigener Rechner)“, get „holt: Server → dein
    Rechner“ (rechtsbündig)."""
    s = Szene("linux/k11sftp", reihenfolge="anlegen")
    w = W_SF
    t = s.terminal(pos=(-3.42, 2.4), spalten=67, zeilen=13, prompt=P11, titel=TITEL, groesse=TK)
    schritt(s, EIN(t.id, 0.6))
    t.eingabe("sftp uebung", tempo=16)
    t.schritt("Connected to uebung.\nsftp> ", 0.6)
    t.eingabe("cd linuxk11/server", tempo=20)
    t.schritt("sftp> ", 0.3)
    t.eingabe("ls", tempo=10)
    t.schritt("einkauf.txt   urlaub\nsftp> ", 0.5)
    xk = t.rechts + 0.19

    def klammer_(z0, z1, key, farbe):
        ya, yb = t.oben(z0) - 0.01, t.unten(z1) + 0.01
        return vklammer(s, r4(xk), r4(ya), r4(yb), farbe, 0.07, 2) + \
            [L(s, key, w[key], (3.42, (ya + yb) / 2), FM, "right", farbe)]
    k_dort = klammer_(2, 4, "dort", DUNKEL)
    schritt(s, EIN(k_dort, 0.5))
    s.pause(0.3)
    t.eingabe("lls", tempo=10)
    t.schritt("\n".join(SFTP_LLS) + "\nsftp> ", 0.5)
    k_hier = klammer_(5, 7, "hier", BLAU)
    schritt(s, EIN(k_hier, 0.5))
    s.pause(0.3)
    t.eingabe("get einkauf.txt aus_sftp.txt", tempo=24)
    t.schritt("\n".join(SFTP_GET) + "\nsftp> ", 0.6)
    k_get = klammer_(8, 10, "holt", ORANGE)
    schritt(s, EIN(k_get, 0.5))
    s.pause(0.3)
    t.eingabe("bye", tempo=10)
    t.prompt(pfad=PFAD)
    s.speichern()


RSYNC_CMD = "rsync -av urlaub/ uebung:linuxk11/server/sicherung/"
W_RS = {"lauf1": ("Lauf 1", "run 1", "pasada 1", "第 1 次", "passage 1", "1. çalıştırma"),
        "lauf2": ("Lauf 2", "run 2", "pasada 2", "第 2 次", "passage 2", "2. çalıştırma"),
        "lauf3": ("Lauf 3", "run 3", "pasada 3", "第 3 次", "passage 3", "3. çalıştırma"),
        "hier": ("hier", "here", "aquí", "本机", "ici", "burası"),
        "leer": ("leer", "empty", "vacía", "空", "vide", "boş"),
        "gleich": ("Größe und Zeit gleich", "same size and time", "mismo tamaño y hora", "大小和时间相同", "même taille et heure",
                   "boyut ve zaman aynı"),
        "neu": ("neu", "new", "nuevo", "新", "nouveau", "yeni")}


def k11rsync():
    """Oben der Befehl (Heft 5.3, Mitschrift), darunter drei Läufe nebeneinander, je links urlaub/ (hier), rechts
    sicherung/ (Server). Lauf 1: rechts leer, tag1–tag3 wandern hinüber, sent 320 bytes. Lauf 2: Waagen „Größe und Zeit
    gleich“, nichts wandert, sent 115 bytes. Lauf 3: tag4.txt ist neu und wandert allein, sent 201 bytes."""
    s = Szene("linux/k11rsync", reihenfolge="anlegen")
    w = W_RS
    cmd = tx(s, RSYNC_CMD, (0, 2.6), TK, "center")
    cxs = [-2.3, 0.0, 2.3]
    yf = [0.98, 0.63, 0.28, -0.07]
    sent = ["sent 320 bytes", "sent 115 bytes", "sent 201 bytes"]
    laeufe = []
    for k, cx in enumerate(cxs):
        n_l = 4 if k == 2 else 3
        n_r = 0 if k == 0 else 3
        o = {"rahmen": [box(s, (cx, 0.45), 2.2, 3.5, GRAU, WEISS, 2, "rect"),
                        L(s, "lauf%d" % (k + 1), w["lauf%d" % (k + 1)], (cx, 1.98), FM, "center", DUNKEL),
                        tx(s, "urlaub/", (cx - 0.6, 1.62), TK), tx(s, "sicherung/", (cx + 0.6, 1.62), TK),
                        L(s, "hier", w["hier"], (cx - 0.6, 1.4), FM, "center", GRAU),
                        L(s, "server", W_SERVER, (cx + 0.6, 1.4), FM, "center", GRAU)]}
        o["links"] = [chip(s, (cx - 0.62, yf[j]), "tag%d.txt" % (j + 1), ORANGE if (k == 2 and j == 3) else GRAU, WEISS, g=TK,
                           h=0.26, b=0.74) for j in range(n_l)]
        o["rechts"] = [chip(s, (cx + 0.62, yf[j]), "tag%d.txt" % (j + 1), GRAU, WEISS, g=TK, h=0.26, b=0.74) for j in range(n_r)]
        o["waagen"] = [waage(s, cx, yf[j] - 0.02, 0.8) for j in range(3)] if k > 0 else []
        neu = range(3) if k == 0 else ([3] if k == 2 else [])
        o["kopien"] = [chip(s, (cx - 0.62, yf[j]), "tag%d.txt" % (j + 1), GRAU, WEISS, g=TK, h=0.26, b=0.74) for j in neu]
        o["sent"] = tx(s, sent[k], (cx, -0.55), TK)
        o["extra"] = []
        if k == 0:
            o["leer"] = L(s, "leer", w["leer"], (cx + 0.6, yf[1]), FM, "center", GRAU)
        else:
            o["extra"].append(L(s, "gleich", w["gleich"], (cx, -0.95), FM, "center", GRUEN))
        if k == 2:
            o["extra"].append(L(s, "neu", w["neu"], (cx - 0.6, yf[3] - 0.27), FM, "center", ORANGE))
        laeufe.append(o)
    schritt(s, EIN(cmd, 0.5))
    for k, o in enumerate(laeufe):
        s.pause(0.3)
        schritt(s, EIN(o["rahmen"], 0.5))
        schritt(s, EIN(flach(o["links"]) + flach(o["rechts"]) + ([o["leer"]] if k == 0 else []), 0.5))
        if k == 0:
            schritt(s, EIN(flach(o["kopien"]), 0.25))
            schritt(s, *VERS(o["kopien"], 1.24, 0, 1.0), AUS(o["leer"], 0.6))
        else:
            schritt(s, EIN(flach(o["waagen"]), 0.6))
            if k == 2:
                schritt(s, EIN(o["extra"][1], 0.4))
                schritt(s, EIN(flach(o["kopien"]), 0.25))
                schritt(s, *VERS(o["kopien"], 1.24, 0, 0.9))
        schritt(s, EIN([o["sent"]] + o["extra"][:1], 0.5))
    s.speichern()


def karton(s, x, y):
    """Karton urlaub mit vier Dateien (Mitte x, y; Breite 1,3, Höhe 1,34). Ergebnis (Teile, Deckel links, Deckel rechts)."""
    teile = [box(s, (x, y), 1.3, 1.34, DUNKEL, ORANGE_HELL, 2.5, "rect"), tx(s, "urlaub", (x, y + 0.5), TT)]
    for j in range(4):
        teile += chip(s, (x, y + 0.23 - 0.25 * j), "tag%d.txt" % (j + 1), GRAU, WEISS, g=TK, h=0.22)
    dl = lin(s, (x - 0.65, y + 0.67), (x, y + 0.67), DUNKEL, 3.5)
    dr = lin(s, (x, y + 0.67), (x + 0.65, y + 0.67), DUNKEL, 3.5)
    return teile, dl, dr


def k11schraegstrich():
    """Links dein Rechner mit dem Karton urlaub (vier Dateien), rechts der Server mit zwei Zielen (Heft 5.4). Oben
    rsync -a urlaub …/mit_ordner/: der ganze Karton wandert und steht in mit_ordner/ (also mit_ordner/urlaub/). Unten
    rsync -a urlaub/ …/nur_inhalt/: der Schrägstrich leuchtet, der Karton öffnet sich, nur die vier Dateien wandern und
    liegen direkt in nur_inhalt/."""
    s = Szene("linux/k11schraegstrich", reihenfolge="anlegen")
    cw = tt_breite(TK, 1)
    bl = block(s, -3.44, -1.0, -1.85, 2.55, "dein", W_DEIN)
    br = block(s, -0.6, 3.44, -1.85, 2.55, "server", W_SERVER)
    kx, ky = -2.22, 0.45
    src, dl, dr = karton(s, kx, ky)
    # oben: mit_ordner
    c1 = tx(s, "rsync -a urlaub …/mit_ordner/", (-0.45, 2.12), TK, "left")
    f1 = [box(s, (1.42, 0.97), 1.9, 1.9, BLAU, WEISS, 2, "rect"), tx(s, "mit_ordner/", (0.57, 1.76), TK, "left", BLAU)]
    a1 = pfk(s, (kx + 0.68, 0.75), (0.45, 0.9), DUNKEL, 2.5)
    kop, kdl, kdr = karton(s, kx, ky)
    kop += [kdl, kdr]
    # unten: nur_inhalt
    yc2 = -0.25
    c2 = [tx(s, "rsync -a urlaub", (-0.45, yc2), TK, "left"), tx(s, "/", (-0.45 + 15 * cw, yc2), TK, "left", ORANGE),
          tx(s, " …/nur_inhalt/", (-0.45 + 16 * cw, yc2), TK, "left")]
    f2 = [box(s, (1.42, -0.975), 1.9, 1.25, BLAU, WEISS, 2, "rect"), tx(s, "nur_inhalt/", (0.57, -0.52), TK, "left", BLAU)]
    a2 = pfk(s, (kx + 0.68, 0.15), (0.45, -0.95), DUNKEL, 2.5)
    ziele = [(0.95, -0.85), (1.89, -0.85), (0.95, -1.2), (1.89, -1.2)]
    dateien = [chip(s, (kx, ky + 0.23 - 0.25 * j), "tag%d.txt" % (j + 1), GRAU, WEISS, g=TK, h=0.22) for j in range(4)]
    schritt(s, EIN(bl + br, 0.5))
    schritt(s, EIN(src + [dl, dr], 0.6))
    s.pause(0.4)
    schritt(s, EIN([c1] + f1, 0.5))
    schritt(s, EIN(kop, 0.25))
    schritt(s, ZEICHNE(a1, 1.0), *VERS(kop, 1.42 - kx, 0.82 - ky, 1.0))
    s.pause(0.5)
    schritt(s, EIN(c2 + f2, 0.5))
    schritt(s, BETONE(c2[1], 0.8))
    schritt(s, DREH(dl, 115, (kx - 0.65, ky + 0.67), 0.7), DREH(dr, -115, (kx + 0.65, ky + 0.67), 0.7))
    schritt(s, EIN(flach(dateien), 0.25))
    schritt(s, ZEICHNE(a2, 1.0),
           *[v for j in range(4) for v in VERS(dateien[j], ziele[j][0] - kx, ziele[j][1] - (ky + 0.23 - 0.25 * j), 1.0)])
    s.speichern()


W_DE = {"alt": ("alte Fassung (auf dem Server)", "old version (on the server)", "versión antigua (en el servidor)", "旧版本（在服务器上）",
                "ancienne version (sur le serveur)", "eski sürüm (sunucuda)"),
        "neu": ("neue Fassung", "new version", "versión nueva", "新版本", "nouvelle version", "yeni sürüm"),
        "gleich": ("1142 Blöcke zu 1128 Bytes: wiedergefunden", "1142 blocks of 1128 bytes: found again",
                   "1142 bloques de 1128 bytes: encontrados de nuevo", "1142 个 1128 字节的块：再次找到",
                   "1142 blocs de 1128 octets : retrouvés", "1128 baytlık 1142 blok: yeniden bulundu"),
        "gesendet": ("719 + 7 Bytes: neu gesendet", "719 + 7 bytes: sent anew", "719 + 7 bytes: enviados de nuevo",
                     "719 + 7 字节：重新发送", "719 + 7 octets : envoyés", "719 + 7 bayt: yeniden gönderildi"),
        "bg": ("Blockgröße\n(Vielfaches von 8)", "block size\n(multiple of 8)", "tamaño de bloque\n(múltiplo de 8)", "块大小\n（8 的倍数）",
               "taille de bloc\n(multiple de 8)", "blok boyutu\n(8'in katı)"),
        "altz": ("alte Fassung", "old version", "versión antigua", "旧版本", "ancienne version", "eski sürüm")}
DELTA = [r"\sqrt{1\,288\,895}\approx 1135.3\;\to\;1128", r"1\,288\,895 = 1142\cdot 1128 + 719", r"1142\cdot 1128 = 1\,288\,176",
         r"719 + 7 = 726", r"1\,288\,176 + 726 = 1\,288\,902"]


def k11delta():
    """Rechenbild zum Blockvergleich (Heft 5.6, Beispiel „Woher die 726 Bytes kommen“). Oben zwei Balken: alte Fassung
    (1142 graue Blöcke, Rest 719) und neue Fassung (1142 grüne Blöcke, gelbes Endstück 719 + 7), nicht maßstäblich.
    Darunter Zeile für Zeile: Blockgröße, Zerlegung der alten Fassung, Matched data, Literal data, Total file size."""
    s = Szene("linux/k11delta", reihenfolge="anlegen")
    w = W_DE
    x0, x1, x2 = -3.3, 1.9, 2.6
    ya, yn, hb = 2.0, 1.3, 0.3

    def balken(y, rand, fuell, rest_rand, rest_fuell, x_end, txt):
        teile = [box(s, ((x0 + x1) / 2, y), x1 - x0, hb, rand, fuell, 2, "rect")]
        teile += [lin(s, (x0 + 0.2 * k, y - hb / 2), (x0 + 0.2 * k, y + hb / 2), rand, 1) for k in range(1, 26)]
        rest = [box(s, ((x1 + x_end) / 2, y), x_end - x1, hb, rest_rand, rest_fuell, 2, "rect"),
                text(s, txt, ((x1 + x_end) / 2, y), FM, "center", DUNKEL, roh=True)]
        return teile, rest
    alt, alt_r = balken(ya, GRAU, GRAU_HELL, GRAU, WEISS, x2, "719")
    neu, neu_r = balken(yn, GRUEN, GRUEN_HELL, ORANGE, GELB, 3.35, "719 + 7")
    l_alt = Lr(s, "alt", w["alt"], (x0, ya + 0.3), FM, "left", DUNKEL)
    l_neu = Lr(s, "neu", w["neu"], (x0, yn + 0.3), FM, "left", DUNKEL)
    l_gl = Lr(s, "gleich", w["gleich"], (x0, yn - 0.32), FM, "left", GRUEN)
    l_ge = Lr(s, "gesendet", w["gesendet"], (3.38, yn - 0.55), FM, "right", ORANGE)
    yz = [0.1, -0.42, -0.9, -1.38, -1.86]
    xl, xf = -0.75, 1.3
    labels = [Lr(s, "bg", w["bg"], (xl, yz[0]), FM, "right", DUNKEL), Lr(s, "altz", w["altz"], (xl, yz[1]), FM, "right", DUNKEL),
              tx(s, "Matched data", (xl, yz[2]), TK, "right", GRUEN), tx(s, "Literal data", (xl, yz[3]), TK, "right", ORANGE),
              tx(s, "Total file size", (xl, yz[4]), TK, "right")]
    formeln = [s.formel(f, mitte=(xf, y), hoehe=0.3 if i == 0 else 0.22) for i, (f, y) in enumerate(zip(DELTA, yz))]
    schritt(s, EIN(alt + alt_r + [l_alt], 0.6))
    s.pause(0.3)
    schritt(s, EIN(neu + [l_neu], 0.6))
    schritt(s, EIN(l_gl, 0.5))
    schritt(s, EIN(neu_r, 0.5))
    schritt(s, EIN(l_ge, 0.5))
    for f, l in zip(formeln, labels):
        s.pause(0.4)
        schritt(s, EIN([f, l], 0.8))
    s.speichern()


# ================================================================== Abschnitt 6: Programme weiterlaufen lassen
XS1, XPT, XBA = -0.35, 0.95, 2.25          # sshd-session, pts/3, -bash (Zeile A); Job und Datei darunter bei XBA
YA, YB, YC = 1.0, -0.1, -1.0
XSSH = -2.52                               # ssh unter dem Fenster
FENSTER = (-3.4, 2.6)                      # linke obere Ecke des Terminalfensters (22 × 4 Zeichen)
W_AB = {"zu": ("Fenster\ngeschlossen", "window\nclosed", "ventana\ncerrada", "窗口\n已关闭", "fenêtre\nfermée", "pencere\nkapandı"),
        "bleibt": ("bleibt bei 4", "stays at 4", "se queda en 4", "停在 4", "reste à 4", "4'te kalır")}


def kette(s, job, unten=-1.55, pts_offen=True):
    """Gemeinsame Teile von k11abbruch und k11nohup: Blöcke, sshd-session – pts/3 – -bash, der Job darunter, die Datei
    fortschritt.txt und der Pfeil vom Job zur Datei (Ergebnis dict mit Listen); pts_offen=False: nur das geschlossene,
    graue pts/3."""
    o = {"bl": block(s, -3.44, -1.5, unten, 2.95, "dein", W_DEIN), "br": block(s, -1.1, 3.44, unten, 2.95, "server", W_SERVER)}
    o["sshd"] = proz(s, (XS1, YA), "sshd-session", g=TK)
    o["pts"] = [box(s, (XPT, YA), 0.64, 0.34, "#0f0f0f", TERM_BG, 1.5, "rect"),
                tx(s, "pts/3", (XPT, YA), TK, "center", TERM_FG)] if pts_offen else []
    o["linien"] = [lin(s, (XS1 + 0.61, YA), (XPT - 0.32, YA), GRAU, 2), lin(s, (XPT + 0.32, YA), (XBA - 0.34, YA), GRAU, 2),
                   lin(s, (XBA, YA - 0.2), (XBA, YB + 0.2), GRAU, 2)]
    o["bash"] = proz(s, (XBA, YA), "-bash", g=TK)
    o["job"] = proz(s, (XBA, YB), job, g=TK)
    o["karte"] = [box(s, (XBA, YC), 1.85, 0.36, GRAU, WEISS, 2, "round"), tx(s, "fortschritt.txt", (XBA - 0.82, YC), TK, "left")]
    o["pfj"] = pfk(s, (XBA, YB - 0.2), (XBA, YC + 0.19), DUNKEL, 2)
    o["g_pts"] = [box(s, (XPT, YA), 0.64, 0.34, GRAU, GRAU_HELL, 2, "rect", dash="5,4"), tx(s, "pts/3", (XPT, YA), TK, "center", GRAU)]
    return o


def ssh_links(s, geschlossen):
    """ssh unter dem Fenster und die Verbindung zu sshd-session (nur ohne geschlossen); dazu die grauen Teile nach dem
    Abbruch: ssh grau, Rohr gerissen, gestrichelter Fensterrahmen (Ergebnis dict)."""
    o = {} if geschlossen else {
        "ssh": proz(s, (XSSH, YA), "ssh", g=TK),
        "rohr": box(s, ((XSSH + 0.264 + XS1 - 0.605) / 2, YA), XS1 - 0.605 - XSSH - 0.264, 0.14, GRAU, GRAU_HELL, 1.5, "rect")}
    o["g_ssh"] = grau_proz(s, (XSSH, YA), "ssh", g=TK)
    o["stuemmel"] = [box(s, ((XSSH + 0.264 - 1.45) / 2, YA), -1.45 - XSSH - 0.264, 0.14, GRAU, GRAU_HELL, 1.5, "rect"),
                     box(s, ((-1.15 + XS1 - 0.605) / 2, YA), XS1 - 0.605 + 1.15, 0.14, GRAU, GRAU_HELL, 1.5, "rect"),
                     kreuz(s, -1.3, YA, 0.16)]
    gw, gh = 22 * tt_breite(TK, 1) + 1.2 * TK / PX, (2 + 4 * 1.2 + 0.9) * TK / PX     # Fenster 22 × 4 bei TK (F1-Maße)
    gm = (FENSTER[0] + gw / 2, FENSTER[1] - gh / 2)
    o["geist"] = [box(s, gm, gw, gh, GRAU, WEISS, 2, "round", dash="5,4", deckung=0.0), L(s, "zu", W_AB["zu"], gm, FM, "center", GRAU)]
    return o


def k11abbruch():
    """Links das Terminalfenster (Schritt 1 … 4, der Zähler läuft auf dem Server) über ssh; rechts der Server mit
    sshd-session – pts/3 – -bash und dem Job ./zaehler.sh, unten fortschritt.txt (1 → 4). Das Fenster schließt (×,
    gestrichelter Rahmen „Fenster geschlossen“), Blitz SIGHUP an ssh, ssh wird grau, die Verbindung reißt (Kreuz),
    sshd-session schließt pts/3 (Kreuz), Blitz SIGHUP an -bash, von dort an den Job; beide werden grau. fortschritt.txt
    bleibt bei 4 (Heft 6.2, Mitschrift s6_abbruch)."""
    s = Szene("linux/k11abbruch", reihenfolge="anlegen")
    w = W_AB
    o = kette(s, "./zaehler.sh")
    v = tx(s, "1", (XBA + 0.72, YC), TT, "center")
    t = s.terminal(text="Schritt 1\n", pos=FENSTER, spalten=22, zeilen=4, groesse=TK)
    c = ssh_links(s, False)
    b1 = [blitz(s, XSSH, 1.42, 0.75), tx(s, "SIGHUP", (XSSH + 0.17, 1.42), TK, "left", ORANGE)]
    b2 = [blitz(s, 1.59, YA, 0.75), tx(s, "SIGHUP", (1.59, YA + 0.3), TK, "center", ORANGE)]
    b3 = [blitz(s, XBA, (YA + YB) / 2, 0.75), tx(s, "SIGHUP", (XBA + 0.17, (YA + YB) / 2), TK, "left", ORANGE)]
    g_bash = grau_proz(s, (XBA, YA), "-bash", g=TK)
    g_job = grau_proz(s, (XBA, YB), "./zaehler.sh", g=TK)
    l_bl = L(s, "bleibt", w["bleibt"], (XBA, YC - 0.34), FM, "center", GRAU)
    schritt(s, EIN(o["bl"] + o["br"], 0.5))
    schritt(s, EIN([t.id] + c["ssh"] + [c["rohr"]], 0.6))
    schritt(s, EIN(o["sshd"] + o["pts"] + o["linien"] + o["bash"] + o["job"] + o["karte"] + [o["pfj"], v], 0.6))
    s.pause(0.3)
    for k in (2, 3, 4):
        with s.gleichzeitig():
            t.ausgabe("Schritt %d" % k, dauer=0.5)
            s.ersetzen(v, str(k), dauer=0.5)
    s.pause(0.5)
    with s.gleichzeitig():
        t.schliessen(1.0)
        schritt(s, EIN(c["geist"], 1.0))
    schritt(s, WACHS(b1[0], 0.5), EIN(b1[1], 0.5))
    schritt(s, AUS(c["ssh"] + [c["rohr"]], 0.7), EIN(c["g_ssh"] + c["stuemmel"], 0.7))
    schritt(s, AUS(o["pts"], 0.6), EIN(o["g_pts"], 0.6))
    schritt(s, WACHS(b2[0], 0.5), EIN(b2[1], 0.5))
    schritt(s, WACHS(b3[0], 0.5), EIN(b3[1], 0.5))
    schritt(s, AUS(o["bash"] + o["job"], 0.6), EIN(g_bash + g_job, 0.6))
    schritt(s, EIN(l_bl, 0.5))
    s.speichern()


W_NH = {"ign": ("SIGHUP wird ignoriert", "SIGHUP is ignored", "SIGHUP se ignora", "SIGHUP 被忽略", "SIGHUP est ignoré",
                "SIGHUP yok sayılır"),
        "neu": ("neue Anmeldung", "new login", "nuevo inicio de sesión", "新的登录", "nouvelle connexion", "yeni oturum"),
        "dateien": ("liest die Dateien", "reads the files", "lee los archivos", "读取文件", "lit les fichiers", "dosyaları okur"),
        "alt": ("alter Bildschirm", "old screen", "pantalla antigua", "旧屏幕", "ancien écran", "eski ekran")}


def k11nohup():
    """Wie k11abbruch nach dem Abbruch: links der geschlossene Fensterrahmen, ssh grau, Verbindung gerissen; rechts pts/3
    geschlossen. Blitz SIGHUP an -bash (wird grau) und weiter an den Job nohup ./zaehler.sh; dort prallt er ab („SIGHUP wird
    ignoriert“). Der Zähler schreibt weiter: Ausgabe nach nohup.out, fortschritt.txt 4 → 8. Darunter links eine neue
    Anmeldung: Sie erreicht die Dateien und mit pkill den Prozess, nicht aber den alten Bildschirm (Kreuz). Heft 6.3."""
    s = Szene("linux/k11nohup", reihenfolge="anlegen")
    w = W_NH
    o = kette(s, "nohup ./zaehler.sh", unten=-1.75, pts_offen=False)
    v = tx(s, "4", (XBA + 0.72, YC), TT, "center")
    gruppe = box(s, (1.475, YC), 3.62, 0.6, GRUEN, WEISS, 2, "round", dash="5,4", deckung=0.0)
    nout = [box(s, (0.3, YC), 1.1, 0.36, GRAU, WEISS, 2, "round"), tx(s, "nohup.out", (0.3, YC), TK)]
    p_out = pfk(s, (XBA - 0.6, YB - 0.2), (0.62, YC + 0.19), DUNKEL, 2)
    l_out = L(s, "ausgabe", W_AUSGABE, (0.95, -0.5), FM, "right", GRAU)
    c = ssh_links(s, True)
    b2 = [blitz(s, 1.59, YA, 0.75), tx(s, "SIGHUP", (1.59, YA + 0.3), TK, "center", ORANGE)]
    b3 = blitz(s, XBA, 0.5, 0.75)
    schild = [lin(s, (XBA - 0.35, 0.17), (XBA + 0.35, 0.17), GRUEN, 5), pfk(s, (XBA + 0.1, 0.32), (XBA + 0.38, 0.62), ORANGE, 2,
                                                                           spitze=0.07),
              L(s, "ign", w["ign"], (XBA - 0.22, 0.5), FM, "right", GRUEN)]
    g_bash = grau_proz(s, (XBA, YA), "-bash", g=TK)
    neu = [proz(s, (-2.47, -0.55), "ssh uebung", g=TK), L(s, "neu", w["neu"], (-2.47, -0.22), FM, "center", BLAU)]
    xn = -2.47 + 0.53
    a_dat = pfk(s, (xn, -0.65), (-0.34, YC - 0.05), GRUEN, 2.5)
    l_dat = L(s, "dateien", w["dateien"], (1.475, YC - 0.45), FM, "center", GRUEN)
    a_pk = pfk(s, (xn, -0.5), (XBA - 0.85, YB - 0.05), GRUEN, 2.5)
    l_pk = tx(s, "pkill", (-0.3, -0.16), TK, "center", GRUEN)
    a_alt = pfk(s, (xn, -0.42), (XPT - 0.25, YA - 0.19), ROT, 2.5, "5,4")
    x_alt = kreuz(s, -0.6, 0.2, 0.16)
    l_alt = L(s, "alt", w["alt"], (0.08, 0.6), FM, "right", ROT)
    schritt(s, EIN(o["bl"] + o["br"], 0.5))
    schritt(s, EIN(c["geist"] + c["g_ssh"] + c["stuemmel"], 0.6))
    schritt(s, EIN(o["sshd"] + o["g_pts"] + o["linien"] + o["bash"] + o["job"] + o["karte"] + nout + [v], 0.6))
    s.pause(0.4)
    schritt(s, WACHS(b2[0], 0.5), EIN(b2[1], 0.5))
    schritt(s, WACHS(b3, 0.4))
    schritt(s, EIN(schild, 0.6))
    schritt(s, AUS(o["bash"], 0.5), EIN(g_bash, 0.5))
    s.pause(0.3)
    schritt(s, ZEICHNE([o["pfj"], p_out], 0.5), EIN(l_out, 0.5))
    for k in (5, 6, 7, 8):
        s.ersetzen(v, str(k), dauer=0.4)
    s.pause(0.5)
    schritt(s, EIN(neu, 0.5))
    schritt(s, EIN(gruppe, 0.4), ZEICHNE(a_dat, 0.6), EIN(l_dat, 0.6))
    schritt(s, ZEICHNE(a_pk, 0.6), EIN(l_pk, 0.6))
    schritt(s, ZEICHNE(a_alt, 0.6), EIN([x_alt, l_alt], 0.6))
    s.speichern()


W_TS = {"srv": ("tmux-Server", "tmux server", "servidor tmux", "tmux 服务器", "serveur tmux", "tmux sunucusu"),
        "hg": ("(läuft im Hintergrund, kein Terminal)", "(runs in the background, no terminal)",
               "(se ejecuta en segundo plano, sin terminal)", "（在后台运行，没有终端）", "(tourne en arrière-plan, sans terminal)",
               "(arka planda çalışır, uçbirimi yok)")}


def k11tmuxserver():
    """Rechts der Kasten tmux-Server (läuft im Hintergrund, kein Terminal) mit drei kleinen Bildschirmen pts/4 – pts/6, je
    mit einer Shell; auf pts/4 zählt ein Zähler. Links ein Terminalfenster mit dem Client tmux, eine Linie zu pts/4, das
    Fenster zeigt dasselbe. Das Fenster schließt: Client und Linie verschwinden, der Zähler läuft weiter. Ein neues Fenster
    mit neuem Client verbindet sich mit demselben Bildschirm und zeigt den weitergelaufenen Stand (Heft 6.4)."""
    s = Szene("linux/k11tmuxserver", reihenfolge="anlegen")
    w = W_TS
    srv = [box(s, (1.795, 0.6), 3.29, 3.7, BLAU, BLAU_HELL, 2.5, "rect"), L(s, "srv", w["srv"], (0.28, 2.25), FM, "left", DUNKEL),
           Lr(s, "hg", w["hg"], (0.28, 2.0), FM, "left", GRAU)]
    yts = [1.7, 0.85, 0.0]
    texte = ["Schritt 3\nSchritt 4", "student@labor:~$ ", "student@labor:~$ "]
    ms = [s.terminal(text=texte[i], pos=(0.32, y), spalten=18, zeilen=2, groesse=TK, rahmen="ohne", knoepfe="keine", cursor=False)
          for i, y in enumerate(yts)]
    ms_l = [tx(s, "pts/%d · bash" % (4 + i), (1.98, ms[i].mitte[1]), TK, "left") for i in range(3)]

    def client(y_oben, text, mit_geist):
        t = s.terminal(text=text, pos=(-3.4, y_oben), spalten=22, zeilen=2, groesse=TK, cursor=False)
        ym = t.mitte[1]
        teile = proz(s, (-1.0, ym), "tmux", g=TK) + [lin(s, (t.rechts, ym), (-1.3, ym), GRAU, 1.5, "3,3"),
                                                    L(s, "client%d" % len(s.objects), W_CLIENT, (-1.0, ym - 0.33), FM, "center", GRAU)]
        linie_ = lin(s, (-0.7, ym), (0.31, ms[0].mitte[1] + 0.03), ORANGE, 2.5)
        geist_ = [box(s, t.mitte, t.groesse[0], t.groesse[1], GRAU, WEISS, 2, "round", dash="5,4", deckung=0.0),
                  L(s, "zu", W_AB["zu"], t.mitte, FM, "center", GRAU)] if mit_geist else []
        return t, teile, linie_, geist_
    t1, c1, li1, g1 = client(2.3, "Schritt 3\nSchritt 4", True)
    t2, c2, li2, _ = client(0.4, "Schritt 6\nSchritt 7", False)
    schritt(s, EIN(srv, 0.6))
    schritt(s, EIN([m.id for m in ms] + ms_l, 0.6))
    s.pause(0.4)
    schritt(s, EIN([t1.id] + c1, 0.6))
    schritt(s, ZEICHNE(li1, 0.5))
    with s.gleichzeitig():
        ms[0].schritt("\nSchritt 5", 0.5)
        t1.schritt("\nSchritt 5", 0.5)
    s.pause(0.4)
    with s.gleichzeitig():
        t1.schliessen(1.0)
        schritt(s, AUS(c1 + [li1], 1.0), EIN(g1, 1.0))
    ms[0].schritt("\nSchritt 6", 0.5)
    ms[0].schritt("\nSchritt 7", 0.5)
    s.pause(0.3)
    schritt(s, EIN([t2.id] + c2, 0.6))
    schritt(s, ZEICHNE(li2, 0.5))
    for k in (8, 9):
        with s.gleichzeitig():
            ms[0].schritt("\nSchritt %d" % k, 0.5)
            t2.schritt("\nSchritt %d" % k, 0.5)
    s.speichern()


W_HI = {"sitzung": ("Sitzung probe", "session probe", "sesión probe", "会话 probe", "session probe", "oturum probe"),
        "f0": ("Fenster 0", "window 0", "ventana 0", "窗口 0", "fenêtre 0", "pencere 0"),
        "f1": ("Fenster 1", "window 1", "ventana 1", "窗口 1", "fenêtre 1", "pencere 1"),
        "status": ("Statuszeile", "status line", "línea de estado", "状态栏", "ligne d'état", "durum satırı"),
        "kc": ("Strg+B c", "Ctrl+B c", "Ctrl+B c", "Ctrl+B c", "Ctrl+B c", "Ctrl+B c"),
        "kp": ("Strg+B %", "Ctrl+B %", "Ctrl+B %", "Ctrl+B %", "Ctrl+B %", "Ctrl+B %"),
        "kq": ('Strg+B "', 'Ctrl+B "', 'Ctrl+B "', 'Ctrl+B "', 'Ctrl+B "', 'Ctrl+B "')}
ST_RECHTS = '"labor" 03:43 13-Nov-26'


def statuszeile(links, rechts=ST_RECHTS, breite=72):
    return links + " " * (breite - len(links) - len(rechts)) + rechts


def k11hierarchie():
    """Pflichtbild (Heft 6.5–6.7, Mitschrift bild_tmux, s6_ps). Rahmen „Sitzung probe“, darin die Karteikarten Fenster 0
    (ein Bereich: Zeile Fenster 0, pts/4 · bash, 72×23) und Fenster 1, das sich teilt: erst ein Bereich (pts/5), nach
    Strg+B % links 36×23 und rechts 35×23 (pts/6), nach Strg+B " rechts oben und unten je 35×11 (pts/6, pts/7). Unten die
    grüne Statuszeile [probe] 0:bash* → [probe] 0:bash- 1:bash* … "labor" 03:43 13-Nov-26. Die Tasten erscheinen mit
    ihrer Ebene in einer Reihe unter den Karten."""
    s = Szene("linux/k11hierarchie", reihenfolge="anlegen")
    w = W_HI
    rahmen_ = [box(s, (0, 0.6), 6.84, 3.9, DUNKEL, WEISS, 2.5, "rect"), Lr(s, "sitzung", w["sitzung"], (-3.3, 2.38), FM, "left", DUNKEL)]
    st_box = box(s, (0, -0.85), 5.54, 0.22, TMUX_GRUEN, TMUX_GRUEN, 1, "rect")
    st = tx(s, statuszeile("[probe] 0:bash*"), (-2.72, -0.85), TK, "left", SCHWARZ)
    l_st = L(s, "status", w["status"], (0, -1.12), FM, "center", GRAU)

    def karte_(cx, key):
        return [box(s, (cx - 0.95, 2.08), 1.2, 0.26, GRAU, GRAU_HELL, 1.5, "rect"), L(s, key, w[key], (cx - 0.95, 2.08), FM, "center"),
                box(s, (cx, 0.9), 3.1, 2.1, GRAU, GRAU_HELL, 1.5, "rect")]

    def bereich(x0, x1, y0, y1):
        return box(s, ((x0 + x1) / 2, (y0 + y1) / 2), x1 - x0, y1 - y0, "#0f0f0f", TERM_BG, 1.5, "rect")

    def info(x, y, pts, groesse_):
        return [tx(s, pts + " · bash", (x, y), TK, "center", TERM_FG), tx(s, groesse_, (x, y - 0.23), TK, "center", TERM_GRAU)]
    k0 = karte_(-1.7, "f0")
    k1 = karte_(1.7, "f1")
    yo, yu = 1.85, -0.05
    b0 = [bereich(-3.15, -0.25, yu, yo)] + info(-1.7, 0.95, "pts/4", "72×23")
    b1 = [bereich(0.25, 3.15, yu, yo)] + info(1.7, 0.95, "pts/5", "72×23")
    xm1, xm2 = 0.25 + 2.9 * 36 / 72, 0.25 + 2.9 * 37 / 72
    b1l = [bereich(0.25, xm1, yu, yo)] + info((0.25 + xm1) / 2, 0.95, "pts/5", "36×23")
    b1r = [bereich(xm2, 3.15, yu, yo)] + info((xm2 + 3.15) / 2, 0.95, "pts/6", "35×23")
    ym1, ym2 = yo - 1.9 * 11 / 23, yo - 1.9 * 12 / 23
    b1ro = [bereich(xm2, 3.15, ym1, yo)] + info((xm2 + 3.15) / 2, (ym1 + yo) / 2 + 0.1, "pts/6", "35×11")
    b1ru = [bereich(xm2, 3.15, yu, ym2)] + info((xm2 + 3.15) / 2, (yu + ym2) / 2 + 0.1, "pts/7", "35×11")
    z0 = tx(s, "Fenster 0", (-3.07, 1.72), TK, "left", TERM_FG)
    z1 = tx(s, "Fenster 1", (0.33, 1.72), TK, "left", TERM_FG)
    kn = chip(s, (-1.7, -0.45), "tmux new -s probe", ORANGE, WEISS, g=TK, h=0.26)
    kc = ttchip(s, (0.7, -0.45), "kc", w["kc"], 0.84)
    kp = ttchip(s, (1.7, -0.45), "kp", w["kp"], 0.84)
    kq = ttchip(s, (2.7, -0.45), "kq", w["kq"], 0.84)
    schritt(s, EIN(kn, 0.5))
    schritt(s, EIN(rahmen_ + [st_box, st, l_st], 0.6))
    schritt(s, EIN(k0 + b0 + [z0], 0.6))
    s.pause(0.6)
    schritt(s, EIN(kc, 0.4))
    schritt(s, EIN(k1 + b1 + [z1], 0.7))
    s.ersetzen(st, statuszeile("[probe] 0:bash- 1:bash*"), dauer=0.6)
    s.pause(0.5)
    schritt(s, EIN(kp, 0.4))
    schritt(s, AUS(b1, 0.7), EIN(b1l + b1r, 0.7))
    s.pause(0.5)
    schritt(s, EIN(kq, 0.4))
    schritt(s, AUS(b1r, 0.7), EIN(b1ro + b1ru, 0.7))
    s.speichern()


W_TM = {"laeuft": ("Zähler läuft ohne Unterbrechung", "the counter runs without a break", "el contador sigue sin interrupción",
                   "计数器不间断地运行", "le compteur tourne sans interruption", "sayaç kesintisiz çalışır"),
        "zu": ("Fenster\ngeschlossen", "window\nclosed", "ventana\ncerrada", "窗口\n已关闭", "fenêtre\nfermée", "pencere\nkapandı"),
        "anm": ("neue\nAnmeldung", "new\nlogin", "nuevo inicio\nde sesión", "新的\n登录", "nouvelle\nconnexion", "yeni\noturum")}


def tmux_status(zeit):
    """Statuszeile von tmux in Zeile 21 (ANSI, grün mit schwarzer Schrift), Cursor bleibt, wo er war."""
    return "\\e[s\\e[21;1H\\e[42;30m" + statuszeile("[rechnung] 0:bash*", '"labor" %s 13-Nov-26' % zeit) + "\\e[0m\\e[u"


def k11tmuxssh():
    """Terminal (Heft 6.10, Mitschrift bild_rechnung): die tmux-Sitzung rechnung auf dem Server, oben
    student@labor:~/linuxk11$ ./zaehler.sh und Schritt 1 … 6, unten die grüne Statuszeile [rechnung] 0:bash* … "labor"
    03:43 13-Nov-26. Der Zähler läuft weiter bis Schritt 18; darunter eine Zeitleiste, die mitläuft: „Fenster geschlossen“
    (Kreuz, das Bild wird blass), „neue Anmeldung“, tmux attach -t rechnung (das Bild ist wieder da, Uhrzeit 03:44)."""
    s = Szene("linux/k11tmuxssh", reihenfolge="anlegen")
    w = W_TM
    start = P11 + "./zaehler.sh\n" + "".join("Schritt %d\n" % k for k in range(1, 7)) + tmux_status("03:43")
    t = s.terminal(text=start, pos=(-2.8, 3.2), spalten=72, zeilen=21, prompt=P11, titel=TITEL, groesse=TK)
    xl, xr = t.links, t.rechts
    sch = schleier(s, t.mitte, t.groesse[0] + 0.02, t.groesse[1] + 0.02, 0.6)
    yb, ya = -0.75, -0.92
    n = 12
    seg = [lin(s, (xl + (xr - xl) * k / n, yb), (xl + (xr - xl) * (k + 1) / n, yb), GRUEN, 6) for k in range(n)]
    l_l = L(s, "laeuft", w["laeuft"], (xl, yb + 0.19), FM, "left", GRUEN)
    achse = lin(s, (xl, ya), (xr, ya), GRAU, 2)
    xe = [xl + (xr - xl) * k / n for k in (2, 6, 9)]
    e1 = [kreuz(s, xe[0], ya, 0.14), L(s, "zu", w["zu"], (xe[0], ya - 0.32), FM, "center", ROT)]
    e2 = [lin(s, (xe[1], ya + 0.08), (xe[1], ya - 0.08), DUNKEL, 2.5), L(s, "anm", w["anm"], (xe[1], ya - 0.32), FM, "center", DUNKEL)]
    e3 = [lin(s, (xe[2], ya + 0.08), (xe[2], ya - 0.08), DUNKEL, 2.5), tx(s, "tmux attach -t rechnung", (xe[2], ya - 0.24), TK)]
    schritt(s, EIN(t.id, 0.6))
    s.pause(0.4)
    schritt(s, EIN([achse, l_l], 0.5))
    for i, k in enumerate(range(7, 19)):
        with s.gleichzeitig():
            if k == 16:
                t.schritt("Schritt 16\n\\e[s\\e[21;58H\\e[42;30m03:44\\e[0m\\e[u", 0.35)
            else:
                t.ausgabe("Schritt %d" % k, dauer=0.35)
            schritt(s, ZEICHNE(seg[i], 0.35))
        if k == 8:
            schritt(s, EIN(e1 + [sch], 0.6))
        elif k == 12:
            schritt(s, EIN(e2, 0.5))
        elif k == 15:
            schritt(s, EIN(e3, 0.5), AUS(sch, 0.5))
    s.speichern()


SZENEN = (k11port, k11clientserver, k11anmeldung, k11dropin, k11socket,
          k11hostschluessel, k11fingerabdruck, k11ersteverbindung, k11knownhosts, k11warnung,
          k11keygen, k11authorizedkeys, k11schluesselpaar, k11rechte, k11agent,
          k11config, k11zweishells, k11fernmuster, k11fernstroeme, k11tty,
          k11scp, k11sftp, k11rsync, k11schraegstrich, k11delta,
          k11abbruch, k11nohup, k11tmuxserver, k11hierarchie, k11tmuxssh)

if __name__ == "__main__":
    wahl = set(sys.argv[1:])
    for f in SZENEN:
        if not wahl or f.__name__ in wahl:
            f()
            print("gebaut:", f.__name__)
