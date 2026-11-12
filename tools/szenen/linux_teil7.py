"""Linux und Kommandozeile, Kapitel 7 „Benutzer, Gruppen und Rechte“ (C:\\Bücher\\EtUndSo\\Linux\\Arbeitshefte\\Kap7_Rechte.tex,
kap7_stufen.tex, kap7_stufen_b.tex): 28 Abbildungen, alle animiert (notizen/animationen.md §5, §11).

Szenenname linux/k7<name> = \\label{fig:k7<name>} im Heft (\\szenenabb{k7<name>}{…}{fig:k7<name>}); Liste in uebergabe_kap7.md,
Abschnitt „Prüfer (Phase 2a)“. Phase 2b (12.11.2026), ein Agent für alle 28.
Stil: F1 (12.11.2026). Zeilen in Schreibmaschinenschrift mit Spalten, Feldern und Klammern (passwd, group, ls -l, sudoers,
id, Rechenbilder) sind s.raster; Datei-Ansichten (hell) sind s.datei; Schlösser s.schloss. Übrige Schemata aus Kästen und
Pfeilen wie linux_teil6.py (Helfer aus linux_hilfen.py). Inhalte (Zeilen, Nummern, Befehle) wörtlich aus dem Heft bzw. der
Mitschrift code/kap7/sitzung_kap7.txt; Inode-Nummern, die das Heft nicht zeigt, stehen als „…“.
Farben: blau = Hauptgruppe/Prozess, orange = Zusatzgruppe/hervorgehoben, grün = erlaubt, rot = verboten, grau = nicht beteiligt;
gelbe Etiketten = Nummern eines Prozesses. Koordinaten zwischen x = -3,45 und 3,45 (höchstens 548 px).
Bauen:  python tools/szenen/linux_teil7.py [k7name …]
Export: python tools/export_szenen.py --animiert <alle Namen aus SZENEN>
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from szenen_lib import *  # noqa: E402,F403
from szenen_lib import farbig  # noqa: E402

from linux_hilfen import *  # noqa: E402,F403  (gemeinsame Helfer der Linux-Kapitel)

schreibmaschine("text")
TT = 18                           # Schreibmaschinenschrift für Zeilen (9,9 px im Artikel)
TK = 17                           # kleinste Schreibmaschinenschrift (Etiketten, Dateinamen)

PASSWD = "student:x:1000:1000::/home/student:/bin/bash"
GROUP3 = ("sudo:x:27:student", "users:x:100:", "student:x:1000:")
ID_ZEILE = "uid=1000(student) gid=1000(student) groups=1000(student),27(sudo)"
LSL = "-rw-r--r-- 1 student student 25 Nov 10 12:32 einkauf.txt"
LSN = "-rw-r--r-- 1 1000 1000 25 Nov 10 12:32 einkauf.txt"


def r4(v):
    return round(v, 4)


def L(s, key, w, pos, g=FM, a="center", f=SCHWARZ):
    """Beschriftung in sechs Sprachen; w = (de, en, es, zh, fr, tr)."""
    return text(s, T(s, key, *w), (r4(pos[0]), r4(pos[1])), g, a, f)


def tx(s, t, pos, g=TT, a="center", f=SCHWARZ):
    """Schreibmaschinenschrift (Code, Dateizeilen, Nummern); in allen Sprachen gleich."""
    return s.text(None, t, (r4(pos[0]), r4(pos[1])), g, a, f, schrift="tt")


def box(s, mitte, b, h, rand=GRAU, fuellung=WEISS, dicke=2, form="round", dash="", deckung=1.0):
    return s.box("", (r4(mitte[0]), r4(mitte[1])), breite=r4(b), hoehe=r4(h), form=form, farbe=rand, fuellung=fuellung,
                 deckung=deckung, dicke=dicke, dash=dash)


def proz(s, mitte, b, name, h=0.4, tt_name=True, g=FK, farbe=BLAU, fuellung=BLAU_HELL, key=None):
    """Prozess = blauer Kasten mit Programmnamen (tt) oder Beschriftung (name = Wortliste, key nötig)."""
    k = box(s, mitte, b, h, farbe, fuellung, 2.5)
    t = tx(s, name, mitte, g) if tt_name else L(s, key, name, mitte, g)
    return [k, t]


def etikett(s, mitte, zeilen, b, zh=0.21, rand=GRAU, fuellung=GELB, key="et"):
    """Etikett (gelber Zettel) mit Zeilen: str = Schreibmaschinenschrift, (Wortliste) = Beschriftung in sechs Sprachen."""
    h = len(zeilen) * zh + 0.12
    teile = [box(s, mitte, b, h, rand, fuellung, 1.5, "rect")]
    y0 = mitte[1] + (len(zeilen) - 1) * zh / 2
    for i, z in enumerate(zeilen):
        p = (mitte[0], y0 - i * zh)
        teile.append(tx(s, z, p, TK) if isinstance(z, str) else L(s, "%s%d" % (key, i), z, p, FM))
    return teile


def kreuz(s, x, y, g=0.24, farbe=ROT):
    return s.kreuzchen(None, r4(x), r4(y), farbe, g, 4)


def bogen_pf(s, a, b, h, farbe=SCHWARZ, dicke=2.5, dash="", marke="0.55"):
    """Bogen von a nach b, h über der Verbindungslinie, Richtungsmarke bei marke."""
    fx = "%s+%s*t" % (r4(a[0]), r4(b[0] - a[0]))
    fy = "%s+%s*t+%s*4*t*(1-t)" % (r4(a[1]), r4(b[1] - a[1]), r4(h))
    return s.weg(None, fx, fy, 0, 1, farbe=farbe, dicke=dicke, pfeile=marke, n=41, dash=dash, spitze=0.12)


def auge(s, x, y, w=0.2, h=0.1, farbe=SCHWARZ):
    """Auge: zwei Bögen und eine Pupille (Ergebnis: Liste)."""
    fx = "%s+%s*(2*t-1)" % (r4(x), w)
    o = s.weg(None, fx, "%s+%s*(1-(2*t-1)*(2*t-1))" % (r4(y), h), 0, 1, farbe=farbe, dicke=2.5, n=25)
    u = s.weg(None, fx, "%s-%s*(1-(2*t-1)*(2*t-1))" % (r4(y), h), 0, 1, farbe=farbe, dicke=2.5, n=25)
    p = s.kreis(None, r4(x), r4(y), r4(h * 0.6), farbe=farbe, dicke=1.5, fuellung=farbe, deckung=1.0)
    return [o, u, p]


def stift(s, x, y, lang=0.42, breit=0.1, farbe=DUNKEL, fuellung=GELB):
    """Stift, schräg (Spitze unten links bei x, y)."""
    import math
    ux, uy = math.cos(math.radians(45)), math.sin(math.radians(45))
    nx, ny = -uy, ux
    sp = 0.12
    pb = (x + ux * sp, y + uy * sp)
    pe = (x + ux * (sp + lang), y + uy * (sp + lang))
    pk = [(x, y), (pb[0] + nx * breit / 2, pb[1] + ny * breit / 2), (pe[0] + nx * breit / 2, pe[1] + ny * breit / 2),
          (pe[0] - nx * breit / 2, pe[1] - ny * breit / 2), (pb[0] - nx * breit / 2, pb[1] - ny * breit / 2)]
    return [s.vieleck(None, [(r4(a), r4(b)) for a, b in pk], farbe=fuellung, deckung=1.0, dicke=2, randfarbe=farbe)]


def startknopf(s, x, y, r=0.14, farbe=GRUEN):
    """Startknopf: Kreis mit Dreieck."""
    k = s.kreis(None, r4(x), r4(y), r, farbe=farbe, dicke=2.5, fuellung=GRUEN_HELL, deckung=1.0)
    d = s.vieleck(None, [(r4(x - 0.04), r4(y + 0.07)), (r4(x - 0.04), r4(y - 0.07)), (r4(x + 0.07), r4(y))], farbe=farbe,
                  deckung=1.0, dicke=1, randfarbe=farbe)
    return [k, d]


def tabelle_verz(s, x0, y0, zeilen, bn=1.35, bi=0.75, rh=0.3, rand=GRAU, textfarbe=SCHWARZ, key="tv"):
    """Verzeichnis als Tabelle Name | Inode (Kopf grau); zeilen = [(name, inode)]. Ergebnis: (Kopf, [Zeile …], Mitten)
    mit Zeile = [Kasten Name, Kasten Inode, Text Name, Text Inode]; Mitten[i] = (x Name, x Inode, y)."""
    xn, xi = x0 + bn / 2, x0 + bn + bi / 2
    kopf = [box(s, (xn, y0), bn, rh, rand, GRAU_HELL, 1.5, "rect"), box(s, (xi, y0), bi, rh, rand, GRAU_HELL, 1.5, "rect"),
            L(s, key + "n", ("Name", "name", "nombre", "名称", "nom", "ad"), (xn, y0), FM, "center", DUNKEL),
            L(s, key + "i", ("Inode", "inode", "inodo", "inode", "inode", "inode"), (xi, y0), FM, "center", DUNKEL)]
    reihen, mitten = [], []
    for i, (n, ino) in enumerate(zeilen):
        y = y0 - (i + 1) * rh
        reihen.append([box(s, (xn, y), bn, rh, rand, WEISS, 1.5, "rect"), box(s, (xi, y), bi, rh, rand, WEISS, 1.5, "rect"),
                       tx(s, n, (x0 + 0.1, y), TK, "left", textfarbe), tx(s, ino, (xi, y), TK, "center", textfarbe)])
        mitten.append((r4(xn), r4(xi), r4(y)))
    return kopf, reihen, mitten


W_PASSWD = ("Name", "user name", "nombre de usuario", "用户名", "nom d'utilisateur", "kullanıcı adı"), \
    ("Platzhalter für den Passwort-Prüfwert", "placeholder for the password hash", "marcador del hash de la contraseña",
     "密码校验值的占位符", "emplacement du hachage du mot de passe", "parola özeti için yer tutucu"), \
    ("Benutzernummer (UID)", "user ID (UID)", "número de usuario (UID)", "用户号（UID）", "numéro d'utilisateur (UID)",
     "kullanıcı numarası (UID)"), \
    ("Nummer der Hauptgruppe", "primary group ID", "número del grupo principal", "主组号", "numéro du groupe principal",
     "birincil grup numarası"), \
    ("Kommentar (hier leer)", "comment (empty here)", "comentario (aquí vacío)", "注释（此处为空）", "commentaire (vide ici)",
     "açıklama (burada boş)"), \
    ("Heimatverzeichnis", "home directory", "directorio personal", "主目录", "répertoire personnel", "ev dizini"), \
    ("Programm nach der Anmeldung", "program started at login", "programa al iniciar sesión", "登录后启动的程序",
     "programme lancé à la connexion", "oturum açılınca başlayan program")


# ================================================================== Abschnitt 1: Benutzer und Gruppen
def k7passwd():
    """passwd-Zeile von student: die sechs Doppelpunkte leuchten, die sieben Felder bekommen nacheinander Nummer und
    Bedeutung; zum Schluss Pfeil von der Hauptgruppe 1000 zur Zeile student:x:1000: in /etc/group."""
    s = Szene("linux/k7passwd", reihenfolge="anlegen")
    g = s.raster(PASSWD, (0, 1.5), groesse=24, ausrichtung="mitte")
    l_datei = tx(s, "/etc/passwd", (g.links, 1.88), TK, "left", GRAU)
    kol = g.trenner(0, ":")
    mk = [g.markieren(0, k, k, ORANGE, 0.4) for k in kol]
    leucht = [g.teil(0, k, k) for k in kol]
    yn = r4(g.unten(0) - 0.24)
    x0, dy = -2.75, 0.3
    felder = []
    for j, f in enumerate(g.felder(0, ":")):
        if f.b >= f.a:
            kl, kt = g.klammer(0, f.a, f.b, str(j + 1), seite="unten", farbe=BLAU, groesse=FM)
            teile = [kl, kt]
        else:                                        # leeres Feld zwischen zwei Doppelpunkten: nur die Nummer
            teile = [None, text(s, str(j + 1), (g.x(f.a), yn), FM, "center", BLAU)]
        y = r4(0.12 - j * dy)
        nr = text(s, str(j + 1), (x0, y), FM, "center", BLAU)
        bed = L(s, "f%d" % j, W_PASSWD[j], (x0 + 0.22, y), FM, "left")
        felder.append((teile, [nr, bed], f))
    f4 = felder[3][2]
    d = s.datei("/etc/group", "student:x:1000:", pos=(1.0, 0.98), groesse=20)
    a4, b4 = d.finde(0, "1000")
    m_gid = d.markieren(0, a4, b4, BLAU, 0.25)
    pf4 = pf(s, (g.xm(f4.a, f4.b), r4(yn - 0.12)), (r4(d.links - 0.04), d.y(0)), knick="vh", farbe=BLAU)
    schritt(s, EIN(g.ids + leucht + [l_datei], 0.7))
    schritt(s, EIN(mk, 0.6), BETONE(leucht, 0.8))
    s.pause(0.6)
    for teile, leg, f in felder:
        if teile[0] is not None:
            schritt(s, ZEICHNE(teile[0], 0.4), EIN([teile[1]] + leg, 0.4))
        else:
            schritt(s, EIN([teile[1]] + leg, 0.4))
    s.pause(0.6)
    schritt(s, EIN(d.id, 0.6))
    schritt(s, ZEICHNE(pf4, 0.8), EIN(m_gid, 0.8))
    s.speichern()


def k7gruppen():
    """Links die passwd-Zeile, rechts drei Zeilen aus /etc/group. Pfeil Feld 4 → Gruppe student (Hauptgruppe), Bogen
    vom Mitglied student in sudo zurück zum Benutzer (Zusatzgruppe), users grau, unten die Zeile von id."""
    s = Szene("linux/k7gruppen", reihenfolge="anlegen")
    p = s.raster(PASSWD, (-3.4, 1.25), groesse=TT)
    gr = s.raster(list(GROUP3), (1.6, 1.25), groesse=TT, zeilenabstand=1.75)
    l_p = tx(s, "/etc/passwd", (-3.4, 1.0), TK, "left", GRAU)
    l_g = tx(s, "/etc/group", (1.6, gr.y(2) - 0.27), TK, "left", GRAU)
    f4 = p.felder(0, ":")[3]
    m_f4 = p.markieren(0, f4.a, f4.b, BLAU, 0.25)
    a, b = gr.finde(2, "1000")
    m_g = gr.markieren(2, a, b, BLAU, 0.25)
    pf1 = pf(s, (p.xm(f4.a, f4.b), r4(p.unten(0) - 0.02)), (r4(gr.links - 0.06), gr.y(2)), knick="vh", farbe=BLAU)
    l1 = L(s, "haupt", ("Hauptgruppe", "primary group", "grupo principal", "主组", "groupe principal", "birincil grup"),
           (-0.7, gr.y(2) - 0.2), FM, "center", BLAU)
    a2, b2 = gr.finde(0, "student")
    m_s = gr.markieren(0, a2, b2, ORANGE, 0.3)
    m_n = p.markieren(0, 0, 6, ORANGE, 0.3)
    bg = bogen_pf(s, (gr.xm(a2, b2), r4(gr.oben(0) + 0.02)), (p.xm(0, 6), r4(p.oben(0) + 0.02)), 0.55, ORANGE)
    l2 = L(s, "zusatz", ("Zusatzgruppe", "supplementary group", "grupo suplementario", "附加组", "groupe supplémentaire",
                         "ek grup"), (-0.35, 2.17), FM, "center", ORANGE)
    idr = s.raster(["$ id", ID_ZEILE], (0, -0.2), groesse=TT, ausrichtung="mitte", zeilenabstand=1.5)
    a3, b3 = idr.finde(1, "1000(student)", n=3)
    a4, b4 = idr.finde(1, "27(sudo)")
    m_i1 = idr.markieren(1, a3, b3, BLAU, 0.25)
    m_i2 = idr.markieren(1, a4, b4, ORANGE, 0.3)
    schritt(s, EIN(p.ids + gr.ids + [l_p, l_g], 0.7))
    s.pause(0.5)
    schritt(s, EIN(m_f4, 0.4))
    schritt(s, ZEICHNE(pf1, 0.9), EIN([m_g, l1], 0.9))
    s.pause(0.6)
    schritt(s, EIN(m_s, 0.4))
    schritt(s, ZEICHNE(bg, 1.0), EIN([m_n, l2], 1.0))
    s.pause(0.6)
    gr.faerben(1, [], rest=GRAU, dauer=0.7)
    s.pause(0.6)
    schritt(s, EIN(idr.ids, 0.7))
    schritt(s, EIN([m_i1, m_i2], 0.7))
    s.speichern()


W_GRUPPEN = ("Gruppen: 1000, 27", "groups: 1000, 27", "grupos: 1000, 27", "组：1000, 27", "groupes : 1000, 27",
             "gruplar: 1000, 27")


def k7prozess():
    """Kette Anmeldeprogramm → Shell → bash -c → id. Das Anmeldeprogramm liest /etc/passwd und /etc/group und klebt der
    Shell ein Etikett auf; eine Kopie geht in einem Schritt an die beiden neuen Prozesse; die Dateien werden grau."""
    s = Szene("linux/k7prozess", reihenfolge="anlegen")
    xc, ys = -0.55, (1.65, 0.75, -0.15, -1.05)
    xe, be = 1.62, 1.75
    w_login = ("Anmeldeprogramm", "login program", "programa de inicio de sesión", "登录程序", "programme de connexion",
               "oturum açma programı")
    login = proz(s, (xc, ys[0]), 2.15, w_login, 0.42, tt_name=False, g=FM, key="login")
    shell = proz(s, (xc, ys[1]), 2.15, ("Shell (bash)", "shell (bash)", "shell (bash)", "Shell（bash）", "shell (bash)",
                                         "kabuk (bash)"), 0.42, tt_name=False, g=FM, key="shell")
    bashc = proz(s, (xc, ys[2]), 2.15, "bash -c id", 0.42)
    pid = proz(s, (xc, ys[3]), 2.15, "id", 0.42)
    xd = -2.62
    dateien = []
    for i, (n, y) in enumerate((("/etc/passwd", 1.95), ("/etc/group", 1.35))):
        dateien.append([box(s, (xd, y), 1.25, 0.32, GRAU, WEISS, 1.5, "rect"), tx(s, n, (xd, y), TK)])
    pfd = [pf(s, (xd + 0.65, 1.95), (xc - 1.1, ys[0] + 0.08), farbe=GRAU, dicke=2),
           pf(s, (xd + 0.65, 1.35), (xc - 1.1, ys[0] - 0.08), farbe=GRAU, dicke=2)]
    pk = [pf(s, (xc, r4(ys[i] - 0.22)), (xc, r4(ys[i + 1] + 0.22)), farbe=BLAU) for i in range(3)]
    zeilen = ["uid=1000 gid=1000", W_GRUPPEN]
    et = etikett(s, (xe, ys[0]), zeilen, be, key="e0")
    k1 = etikett(s, (xe, ys[1]), zeilen, be, key="e1")
    k2 = etikett(s, (xe, ys[1]), zeilen, be, key="e2")
    schl = [schleier(s, (xd, y), 1.35, 0.4, 0.6) for y in (1.95, 1.35)]
    l_grau = L(s, "grau", ("nicht mehr gelesen", "no longer read", "ya no se leen", "不再读取", "plus relus", "artık okunmaz"),
               (xd, 0.95), FM, "center", GRAU)
    schritt(s, EIN(login + flach(dateien), 0.7))
    schritt(s, ZEICHNE(pfd, 0.8))
    schritt(s, BETONE([d[1] for d in dateien], 0.8))
    s.pause(0.6)
    schritt(s, ZEICHNE(pk[0], 0.5), WACHS(shell[0], 0.5), EIN(shell[1], 0.5), EIN(et, 0.5))
    schritt(s, *VERS(et, 0, ys[1] - ys[0], 0.9))
    s.pause(0.6)
    schritt(s, ZEICHNE(pk[1:], 0.6), WACHS([bashc[0], pid[0]], 0.6), EIN([bashc[1], pid[1]], 0.6), EIN(k1 + k2, 0.3))
    schritt(s, *(VERS(k1, 0, ys[2] - ys[1], 0.9) + VERS(k2, 0, ys[3] - ys[1], 0.9)))
    s.pause(0.6)
    schritt(s, EIN(schl + [l_grau], 0.8))
    s.speichern()


def k7pruefwert():
    """Oben: Passwort → Rechenweg → Prüfwert → Zeile in /etc/shadow; Rückweg rot durchgestrichen. Unten: eingegebenes
    Passwort → derselbe Rechenweg → Vergleich mit dem gespeicherten Prüfwert, grün."""
    s = Szene("linux/k7pruefwert", reihenfolge="anlegen")
    ya, yb = 1.4, -0.4
    xp, xr, xw = -2.62, -0.72, 1.02
    w_rw = ("Rechenweg", "calculation", "cálculo", "计算方法", "calcul", "hesaplama")
    t_a = L(s, "fest", ("Passwort festlegen", "setting the password", "fijar la contraseña", "设置密码", "définir le mot de passe",
                        "parolayı belirleme"), (-3.4, 2.2), FM, "left", GRAU)
    pw = [box(s, (xp, ya), 1.45, 0.38, DUNKEL, WEISS, 2), L(s, "pw", ("Passwort", "password", "contraseña", "密码",
                                                                      "mot de passe", "parola"), (xp, ya), FM)]
    rw = [box(s, (xr, ya), 1.3, 0.42, BLAU, BLAU_HELL, 2.5), L(s, "rw", w_rw, (xr, ya), FM)]
    chip = [box(s, (xw, ya), 0.85, 0.36, ORANGE, ORANGE_HELL, 2), tx(s, "$y$…", (xw, ya), TT)]
    l_pw = L(s, "pruef", ("Prüfwert", "hash", "hash", "校验值", "empreinte", "özet"), (xw, ya - 0.33), FM, "center", ORANGE)
    pa = [pf(s, (xp + 0.75, ya), (xr - 0.68, ya)), pf(s, (xr + 0.68, ya), (xw - 0.45, ya))]
    d = s.datei("/etc/shadow", "student:", pos=(1.82, 1.08), spalten=13, zeilen=1, groesse=TT)
    ziel = (d.xm(8, 11), d.y(0))
    kopie = tx(s, "$y$…", (xw, ya), TT)
    rueck = bogen_pf(s, (xw, ya + 0.22), (xp + 0.2, ya + 0.22), 0.36, ROT, 2.5, DASH, "0.9")
    xk = r4((xw + xp + 0.2) / 2)
    kz = kreuz(s, xk, ya + 0.22 + 0.36, 0.26)
    l_kz = L(s, "rueck", ("kein Rückweg", "no way back", "sin camino de vuelta", "无法反推", "pas de retour", "geri dönüş yok"),
             (xk + 0.28, ya + 0.8), FM, "left", ROT)
    t_b = L(s, "anm", ("Anmeldung", "login", "inicio de sesión", "登录", "connexion", "oturum açma"), (-3.4, 0.3), FM, "left",
            GRAU)
    ein = [box(s, (xp, yb), 1.55, 0.38, DUNKEL, WEISS, 2), L(s, "ein", ("eingegebenes Passwort", "entered password",
                                                                        "contraseña introducida", "输入的密码",
                                                                        "mot de passe saisi", "girilen parola"), (xp, yb), FM)]
    rw2 = [box(s, (xr, yb), 1.3, 0.42, BLAU, BLAU_HELL, 2.5), L(s, "rw2", w_rw, (xr, yb), FM)]
    chip2 = [box(s, (xw, yb), 0.85, 0.36, ORANGE, ORANGE_HELL, 2), tx(s, "$y$…", (xw, yb), TT)]
    pb = [pf(s, (xp + 0.8, yb), (xr - 0.68, yb)), pf(s, (xr + 0.68, yb), (xw - 0.45, yb))]
    xv = r4(d.xm(8, 11))
    ver = [s.kreis(None, xv, yb, 0.2, farbe=DUNKEL, dicke=2.5, fuellung=WEISS, deckung=1.0), text(s, "=", (xv, yb), FK)]
    pv = [pf(s, (xw + 0.45, yb), (xv - 0.22, yb)), pf(s, (xv, r4(d.unten_kante - 0.04)), (xv, yb + 0.22))]
    gruen = s.kreis(None, xv, yb, 0.2, farbe=GRUEN, dicke=4, fuellung=GRUEN_HELL, deckung=0.0)
    gl = text(s, "=", (xv, yb), FK, "center", GRUEN)
    hk = haken(s, xv + 0.38, yb + 0.02)
    l_gl = L(s, "gleich", ("gleich: Passwort richtig", "equal: password correct", "igual: contraseña correcta", "相同：密码正确",
                           "égal : mot de passe correct", "eşit: parola doğru"), (xv - 0.2, yb - 0.4), FM, "center", GRUEN)
    schritt(s, EIN([t_a] + pw, 0.6))
    schritt(s, ZEICHNE(pa[0], 0.5), WACHS(rw[0], 0.5), EIN(rw[1], 0.5))
    schritt(s, ZEICHNE(pa[1], 0.5), WACHS(chip[0], 0.5), EIN([chip[1], l_pw], 0.5))
    s.pause(0.4)
    schritt(s, EIN(d.id, 0.5), EIN(kopie, 0.5))
    schritt(s, ZU(kopie, ziel[0], ziel[1], 0.9))
    s.pause(0.6)
    schritt(s, ZEICHNE(rueck, 0.8))
    schritt(s, EIN([kz, l_kz], 0.5))
    s.pause(0.6)
    schritt(s, EIN([t_b] + ein, 0.6))
    schritt(s, ZEICHNE(pb[0], 0.5), WACHS(rw2[0], 0.5), EIN(rw2[1], 0.5))
    schritt(s, ZEICHNE(pb[1], 0.5), WACHS(chip2[0], 0.5), EIN(chip2[1], 0.5))
    schritt(s, ZEICHNE(pv, 0.6), EIN(ver, 0.6))
    schritt(s, EIN([gruen, gl] + hk + [l_gl], 0.6))
    s.speichern()


# ================================================================== Abschnitt 2: Die Rechte einer Datei
def k7besitz():
    """Inode von einkauf.txt (Besitzer 1000, Gruppe 1000, übrige Felder grau); ls -l schlägt die erste 1000 in /etc/passwd
    nach und schreibt student, dann die zweite in /etc/group; darunter ls -n mit den Zahlen."""
    s = Szene("linux/k7besitz", reihenfolge="anlegen")
    xi, xl, xr = -2.55, -3.27, -1.85
    ib = box(s, (xi, 1.27), 1.62, 1.55, DUNKEL, WEISS, 2, "rect")
    i_k = L(s, "inode", ("Inode von einkauf.txt", "inode of einkauf.txt", "inodo de einkauf.txt", "einkauf.txt 的 inode",
                         "inode de einkauf.txt", "einkauf.txt inode'u"), (xi, 2.3), FM, "center", DUNKEL)
    zeilen = [(("groesse", ("Größe:", "size:", "tamaño:", "大小：", "taille :", "boyut:")), "25", 1.85, GRAU),
              (("besitzer", ("Besitzer:", "owner:", "propietario:", "所有者：", "propriétaire :", "sahip:")), "1000", 1.55,
               SCHWARZ),
              (("gruppe", ("Gruppe:", "group:", "grupo:", "组：", "groupe :", "grup:")), "1000", 1.25, SCHWARZ),
              (("rechte", ("Rechte:", "mode:", "permisos:", "权限：", "droits :", "izinler:")), "rw-r--r--", 0.95, GRAU),
              (("zeiten", ("Zeitstempel …", "timestamps …", "marcas de tiempo …", "时间戳 …", "horodatages …",
                           "zaman damgaları …")), "", 0.65, GRAU)]
    inode = [ib, i_k]
    werte = {}
    for (key, w), wert, y, f in zeilen:
        inode.append(L(s, key, w, (xl, y), FM, "left", f))
        if wert:
            werte[key] = tx(s, wert, (xr, y), TK, "right", f)
            inode.append(werte[key])
    p = s.raster(PASSWD, (-1.3, 1.85), groesse=TT)
    l_p = tx(s, "/etc/passwd", (-1.3, 2.15), TK, "left", GRAU)
    gr = s.raster(["student:x:1000:"], (-1.3, 0.62), groesse=TT)
    l_g = tx(s, "/etc/group", (gr.rechts + 0.15, 0.62), TK, "left", GRAU)
    lsl = s.raster(["$ ls -l einkauf.txt", LSL[:12]], (-2.28, -0.05), groesse=TT, zeilenabstand=1.5)
    rest = lsl.teil(1, 29, len(LSL) - 1, text=LSL[29:])   # Lücke für Besitzer und Gruppe (Spalten 13–27) ohne Leerzeichen
    lsn = s.raster(["$ ls -n einkauf.txt", LSN], (-2.28, -0.85), groesse=TT, zeilenabstand=1.5)
    f3 = p.felder(0, ":")[2]
    g3 = gr.felder(0, ":")[2]
    m_p = p.markieren(0, f3.a, f3.b, ORANGE, 0.35)
    m_g = gr.markieren(0, g3.a, g3.b, ORANGE, 0.35)
    pf1 = pf(s, (xi + 0.82, 1.55), (p.xm(f3.a, f3.b), r4(p.unten(0) - 0.02)), knick="hv", farbe=ORANGE)
    pf2 = pf(s, (xi + 0.82, 1.25), (gr.xm(g3.a, g3.b), r4(gr.oben(0) + 0.02)), knick="hv", farbe=ORANGE)
    n1 = p.teil(0, 0, 6, farbe=BLAU)
    n2 = gr.teil(0, 0, 6, farbe=BLAU)
    z1 = (lsl.x(13), lsl.y(1))                       # MoveTo setzt den Anker: bei linksbündigem Text die linke Kante
    z2 = (lsl.x(21), lsl.y(1))
    an1, bn1 = 13, 16
    m_n = [lsn.markieren(1, an1, bn1, ORANGE, 0.35), lsn.markieren(1, 18, 21, ORANGE, 0.35)]
    schritt(s, EIN(inode + p.ids + gr.ids + [l_p, l_g], 0.7))
    s.pause(0.5)
    schritt(s, EIN(lsl.ids + [rest], 0.6))
    schritt(s, BETONE(werte["besitzer"], 0.6))
    schritt(s, ZEICHNE(pf1, 0.8), EIN(m_p, 0.8))
    schritt(s, EIN(n1, 0.4))
    schritt(s, ZU(n1, z1[0], z1[1], 1.0))
    s.pause(0.6)
    schritt(s, BETONE(werte["gruppe"], 0.6))
    schritt(s, ZEICHNE(pf2, 0.8), EIN(m_g, 0.8))
    schritt(s, EIN(n2, 0.4))
    schritt(s, ZU(n2, z2[0], z2[1], 1.0))
    s.pause(0.6)
    schritt(s, EIN(lsn.ids, 0.6))
    schritt(s, EIN(m_n, 0.6))
    s.speichern()


def k7klassen():
    """Datei einkauf.txt (Besitzer student, Gruppe student); drei Benutzer kommen von links und landen in u, g, o."""
    s = Szene("linux/k7klassen", reihenfolge="anlegen")
    datei = [box(s, (0, 1.72), 3.1, 0.66, DUNKEL, WEISS, 2, "rect"), tx(s, "einkauf.txt", (0, 1.88), TT),
             L(s, "bes", ("Besitzer: student · Gruppe: student", "owner: student · group: student",
                          "propietario: student · grupo: student", "所有者：student · 组：student",
                          "propriétaire : student · groupe : student", "sahip: student · grup: student"), (0, 1.58), FM)]
    ys = (0.82, 0.07, -0.68)
    xu, xf = -2.32, 2.5
    w_user = ("student", ("Mitglied der Gruppe student", "member of group student", "miembro del grupo student",
                          "student 组的成员", "membre du groupe student", "student grubunun üyesi"),
              ("weder Besitzer noch Mitglied", "neither owner nor member", "ni propietario ni miembro", "既非所有者也非成员",
               "ni propriétaire ni membre", "ne sahip ne üye"))
    w_feld = (("u · Besitzer", "u · owner", "u · propietario", "u · 所有者", "u · propriétaire", "u · sahip"),
              ("g · Gruppe", "g · group", "g · grupo", "g · 组", "g · groupe", "g · grup"),
              ("o · andere", "o · others", "o · otros", "o · 其他人", "o · autres", "o · diğerleri"))
    farben = ((BLAU, BLAU_HELL), (GRUEN, GRUEN_HELL), (ORANGE, ORANGE_HELL))
    nutzer, felder, fuell, pfeile = [], [], [], []
    for i, y in enumerate(ys):
        k = box(s, (xu, y), 2.15, 0.4, DUNKEL, WEISS, 2)
        t = tx(s, w_user[i], (xu, y), TT) if i == 0 else L(s, "u%d" % i, w_user[i], (xu, y), FM)
        nutzer += [k, t]
        f = box(s, (xf, y), 1.75, 0.46, GRAU, WEISS, 2)
        fuell.append(box(s, (xf, y), 1.75, 0.46, farben[i][0], farben[i][1], 3))
        felder += [f]
        felder.append(L(s, "f%d" % i, w_feld[i], (xf, y), FM))
        pfeile.append(pf(s, (xu + 1.12, y), (xf - 0.92, y), farbe=farben[i][0]))
    l_end = L(s, "genau", ("Jeder Benutzer landet in genau einer Klasse.", "Every user lands in exactly one class.",
                           "Cada usuario cae en exactamente una clase.", "每个用户恰好落入一个类别。",
                           "Chaque utilisateur tombe dans exactement une classe.", "Her kullanıcı tam olarak bir sınıfa düşer."),
              (0, -1.25), FM, "center", DUNKEL)
    schritt(s, EIN(datei + nutzer + felder, 0.7))
    s.pause(0.6)
    for i in range(3):
        schritt(s, ZEICHNE(pfeile[i], 0.8), EIN(fuell[i], 0.8))
        s.pause(0.4)
    schritt(s, EIN(l_end, 0.6))
    s.speichern()


def k7rwx():
    """Links die Zeile von einkauf.txt in der Tabelle des Verzeichnisses (grau), rechts die Datei mit Inhalt; Auge (r),
    Stift (w), Startknopf (x) erscheinen; zuletzt leuchtet der Name, ein Pfeil von w dorthin wird durchgestrichen."""
    s = Szene("linux/k7rwx", reihenfolge="anlegen")
    l_t = L(s, "tab", ("Tabelle des Verzeichnisses", "directory table", "tabla del directorio", "目录表", "table du répertoire",
                       "dizin tablosu"), (-2.32, 1.3), FM, "center", GRAU)
    kopf, reihen, mitten = tabelle_verz(s, -3.35, 0.95, [("einkauf.txt", "…")], rand=HELLGRAU, textfarbe=GRAU)
    m_name = box(s, (-2.675, 0.65), 1.35, 0.3, ORANGE, ORANGE, 0, "rect", deckung=0.35)
    xb, yb = 0.32, 0.62
    dbox = box(s, (xb, yb), 2.0, 1.55, DUNKEL, WEISS, 2, "rect")
    d_t = tx(s, "einkauf.txt", (xb, yb + 0.95), TT)
    inhalt = [tx(s, z, (xb - 0.82, 1.07 - i * 0.25), TK, "left") for i, z in enumerate(("Milch", "Brot", "Äpfel", "Kaffee"))]
    xs = 0.95
    a_r = auge(s, xs, 1.07)
    a_w = stift(s, xs - 0.18, 0.47)
    a_x = startknopf(s, xs, 0.02)
    xl = 1.55
    l_r = L(s, "r", ("r: lesen", "r: read", "r: leer", "r：读取", "r : lire", "r: okuma"), (xl, 1.07), FM, "left")
    l_w = L(s, "w", ("w: verändern", "w: modify", "w: modificar", "w：修改", "w : modifier", "w: değiştirme"), (xl, 0.57), FM,
            "left")
    l_x = L(s, "x", ("x: starten", "x: run", "x: ejecutar", "x：运行", "x : exécuter", "x: çalıştırma"), (xl, 0.02), FM, "left")
    yp = mitten[0][2]
    w_tt = tx(s, "w", (xb - 1.12, yp + 0.17), TT, "center", ORANGE)
    pw = pf(s, (xb - 1.04, yp), (-1.2, yp), farbe=ORANGE)
    kz = kreuz(s, r4((xb - 1.04 - 1.2) / 2), yp, 0.2)
    l_end = L(s, "ende", ("Umbenennen und Löschen ändern die Tabelle, nicht die Datei.",
                          "Renaming and deleting change the table, not the file.",
                          "Renombrar y borrar cambian la tabla, no el archivo.", "重命名和删除改变的是目录表，而不是文件。",
                          "Renommer et supprimer modifient la table, pas le fichier.",
                          "Yeniden adlandırma ve silme dosyayı değil tabloyu değiştirir."), (0, -0.55), FM, "center", DUNKEL)
    schritt(s, EIN(kopf + flach(reihen) + [l_t, dbox, d_t] + inhalt, 0.7))
    s.pause(0.6)
    schritt(s, EIN(a_r + [l_r], 0.6))
    schritt(s, EIN(a_w + [l_w], 0.6))
    schritt(s, EIN(a_x + [l_x], 0.6))
    s.pause(0.6)
    schritt(s, EIN(m_name, 0.5))
    schritt(s, BETONE(reihen[0][2], 0.7))
    schritt(s, EIN(w_tt, 0.4), ZEICHNE(pw, 0.7))
    schritt(s, EIN([kz, l_end], 0.6))
    s.speichern()


def k7spalte():
    """ls -l-Zeile von einkauf.txt: Rest grau außer Besitzer und Gruppe; Klammern u/g/o über den neun Zeichen, r/w/x
    darunter beschriftet; Bögen u → Besitzer, g → Gruppe."""
    s = Szene("linux/k7spalte", reihenfolge="anlegen")
    g = s.raster(LSL, (0, 0.2), groesse=22, ausrichtung="mitte")
    kl = [g.klammer(0, a, a + 2, k, seite="oben", farbe=BLAU, groesse=FK, schrift="tt") for a, k in ((1, "u"), (4, "g"),
                                                                                                    (7, "o"))]
    buch = [text(s, "rwx"[i % 3], (g.xm(1 + i), r4(g.unten(0) - 0.14)), TK, "center", BLAU) for i in range(9)]
    l_rwx = L(s, "stelle", ("Stelle: r w x je Klasse", "position: r w x per class", "posición: r w x por clase",
                            "位置：每类 r w x", "position : r w x par classe", "konum: her sınıf için r w x"),
              (g.links, r4(g.unten(0) - 0.45)), FM, "left", BLAU)
    l_strich = L(s, "strich", ("„-“ = Recht fehlt", "“-” = right missing", "«-» = falta el permiso", "“-” = 没有该权限",
                               "« - » = droit absent", "„-“ = izin yok"), (g.links, r4(g.unten(0) - 0.75)), FM, "left")
    yb = r4(g.oben(0) + 0.42)
    b1 = bogen_pf(s, (g.xm(1, 3) - 0.04, yb + 0.02), (g.xm(13, 19), r4(g.oben(0) + 0.04)), 0.45, BLAU, 2.5, "", "0.97")
    b2 = bogen_pf(s, (g.xm(4, 6) + 0.04, yb + 0.02), (g.xm(21, 27), r4(g.oben(0) + 0.04)), 0.62, GRUEN, 2.5, "", "0.97")
    l_b = L(s, "bes", ("Besitzer", "owner", "propietario", "所有者", "propriétaire", "sahip"), (g.xm(13, 19), r4(g.unten(0) - 0.2)),
            FM, "center", BLAU)
    l_g = L(s, "grp", ("Gruppe", "group", "grupo", "组", "groupe", "grup"), (g.xm(21, 27), r4(g.unten(0) - 0.45)), FM, "center",
            GRUEN)
    schritt(s, EIN(g.ids, 0.6))
    s.pause(0.4)
    g.faerben(0, [(1, 9, SCHWARZ), (13, 19, SCHWARZ), (21, 27, SCHWARZ)], rest=GRAU, dauer=0.7)
    s.pause(0.5)
    for k, t in kl:
        schritt(s, ZEICHNE(k, 0.45), EIN(t, 0.45))
    s.pause(0.5)
    schritt(s, EIN(buch + [l_rwx], 0.7))
    schritt(s, EIN(l_strich, 0.5))
    s.pause(0.6)
    schritt(s, ZEICHNE(b1, 0.8), EIN(l_b, 0.8))
    schritt(s, ZEICHNE(b2, 0.8), EIN(l_g, 0.8))
    s.speichern()


# ================================================================== Abschnitt 3: chmod
def k7symbolisch():
    """Raster u/g/o × r/w/x (gefüllt = gesetzt); g+w, o-r, u=rw,go=r ändern die Felder; darunter die Buchstabenfolge."""
    s = Szene("linux/k7symbolisch", reihenfolge="anlegen")
    xs, ys = (-0.55, 0.0, 0.55), (0.95, 0.4, -0.15)
    kopf = [tx(s, c, (x, 1.45), FK, "center", BLAU) for c, x in zip("rwx", xs)]
    seite = [tx(s, c, (-1.05, y), FK, "center", BLAU) for c, y in zip("ugo", ys)]
    zellen = [box(s, (x, y), 0.5, 0.5, HELLGRAU, WEISS, 1.5, "rect") for y in ys for x in xs]
    ringe = [s.kreis(None, x, y, 0.15, farbe=GRAU, dicke=2) for y in ys for x in xs]

    def punkt(i, j):
        return s.kreis(None, xs[j], ys[i], 0.15, farbe=BLAU, dicke=2, fuellung=BLAU, deckung=1.0)
    da = [punkt(0, 0), punkt(0, 1), punkt(1, 0)]
    o_r = punkt(2, 0)                                # gesetzt am Anfang, o-r nimmt es weg
    g_w = punkt(1, 1)                                # g+w setzt es, u=rw,go=r nimmt es wieder weg
    o_r2 = punkt(2, 0)                               # u=rw,go=r setzt o/r wieder
    rahmen_ = [box(s, (xs[j], ys[i]), 0.5, 0.5, ORANGE, WEISS, 3.5, "rect", deckung=0.0) for i, j in ((1, 1), (2, 0))]
    l_start = L(s, "start", ("Ausgangszustand", "starting state", "estado inicial", "初始状态", "état initial", "başlangıç durumu"),
                (0, 2.0), FM, "center", GRAU)
    befehl = tx(s, "chmod g+w einkauf.txt", (0, 2.0), TT)
    folge = tx(s, "rw-r--r--", (0, -0.72), 22)
    l_folge = L(s, "folge", ("wie ls -l es zeigt", "as ls -l shows it", "como lo muestra ls -l", "ls -l 的显示方式",
                             "comme ls -l l'affiche", "ls -l'nin gösterdiği gibi"), (0, -1.05), FM, "center", GRAU)
    schritt(s, EIN(kopf + seite + zellen + ringe + [l_start, folge, l_folge], 0.7))
    s.pause(0.8)
    schritt(s, AUS(l_start, 0.4), EIN(befehl, 0.4))
    schritt(s, EIN([g_w, rahmen_[0]], 0.6))
    s.ersetzen(folge, "rw-rw-r--", dauer=0.6)
    s.pause(0.8)
    s.ersetzen(befehl, "chmod o-r einkauf.txt", dauer=0.5)
    schritt(s, AUS(o_r, 0.6), AUS(rahmen_[0], 0.6), EIN(rahmen_[1], 0.6))
    s.ersetzen(folge, "rw-rw----", dauer=0.6)
    s.pause(0.8)
    s.ersetzen(befehl, "chmod u=rw,go=r einkauf.txt", dauer=0.5)
    schritt(s, AUS(g_w, 0.6), EIN(o_r2, 0.6), AUS(rahmen_[1], 0.6))
    s.ersetzen(folge, "rw-r--r--", dauer=0.6)
    s.speichern()


def k7oktal():
    """Rechenbild rwx r-x --- → Bits 111 101 000 → Stellenwerte 4 2 1 → Summen 7, 5, 0 → 750."""
    s = Szene("linux/k7oktal", reihenfolge="anlegen")
    b = (2, 13, 24)

    def zeile(teile):
        z = [" "] * 35
        for a, t in zip(b, teile):
            for k, ch in enumerate(t):
                z[a + k] = ch
        return "".join(z).rstrip()
    zeilen = [zeile(("  u", "  g", "  o")), zeile(("r w x", "r - x", "- - -")), zeile(("1 1 1", "1 0 1", "0 0 0")),
              zeile(("4 2 1", "4 2 1", "4 2 1")), "", ""]
    g = s.raster(zeilen, (-1.35, 1.75), groesse=24, zeilenabstand=1.7)
    summen = [g.teil(4, a, a + 8, text=t) for a, t in zip(b, ("4+2+1 = 7", "4+0+1 = 5", "0+0+0 = 0"))]
    xl = r4(g.links - 0.2)
    lab = [L(s, "l%d" % i, w, (xl, g.y(i + 1)), FM, "right", GRAU) for i, w in enumerate((
        ("Rechte", "permissions", "permisos", "权限", "droits", "izinler"),
        ("Bits", "bits", "bits", "位", "bits", "bitler"),
        ("Stellenwerte", "place values", "valores posicionales", "位权", "poids", "basamak değerleri"),
        ("Summen", "sums", "sumas", "和", "sommes", "toplamlar")))]
    l_ok = L(s, "okt", ("oktal", "octal", "octal", "八进制", "octal", "sekizlik"), (xl, g.y(5)), FM, "right", GRAU)
    ziffern = [g.teil(4, a + 8, a + 8, text=t) for a, t in zip(b, "750")]
    ende = [(g.x(16 + i), g.y(5)) for i in range(3)]
    rahm = g.rahmen(5, 16, 18, ORANGE, 3)
    schritt(s, EIN([g.zeile(0), g.zeile(1), lab[0]], 0.7))
    s.pause(0.6)
    schritt(s, EIN([g.zeile(2), lab[1]], 0.7))
    s.pause(0.4)
    schritt(s, EIN([g.zeile(3), lab[2]], 0.7))
    s.pause(0.6)
    schritt(s, EIN([summen[0], lab[3]], 0.8))
    schritt(s, EIN(summen[1], 0.8))
    schritt(s, EIN(summen[2], 0.8))
    s.pause(0.6)
    schritt(s, EIN(ziffern, 0.3))
    schritt(s, *[ZU(z, x, y, 0.9) for z, (x, y) in zip(ziffern, ende)], EIN(l_ok, 0.9))
    schritt(s, ZEICHNE(rahm, 0.6))
    s.speichern()


# ================================================================== Abschnitt 4: Rechte bei Verzeichnissen
W_VERZ_FACH = ("Verzeichnis fach", "directory fach", "directorio fach", "目录 fach", "répertoire fach", "fach dizini")
W_DATEI = ("Datei brief.txt", "file brief.txt", "archivo brief.txt", "文件 brief.txt", "fichier brief.txt", "brief.txt dosyası")


def k7verzrechte():
    """Verzeichnis fach als Tabelle Name | Inode mit brief.txt, rechts die Datei. r: ein Auge liest die Namen (Inode
    verdeckt); x: Pfeil vom Namen über die Inode-Nummer zur Datei; w + x: ein Stift fügt neu.txt hinzu."""
    s = Szene("linux/k7verzrechte", reihenfolge="anlegen")
    x0, y0 = -3.3, 0.85
    l_v = L(s, "verz", W_VERZ_FACH, (x0, 1.7), FM, "left", DUNKEL)
    kopf, reihen, mitten = tabelle_verz(s, x0, y0, [("brief.txt", "…"), ("neu.txt", "…")])
    xn, xi, yr = mitten[0]
    neu = reihen[1]
    deck = box(s, (xi, yr), 0.79, 0.34, GRAU, GRAU_HELL, 1.5, "rect", deckung=0.85)
    a_r = auge(s, xn, r4(y0 + 0.42))
    xb = 1.95
    dbox = [box(s, (xb, yr), 2.1, 0.62, DUNKEL, WEISS, 2, "rect"), tx(s, "Treffen am Freitag", (xb, yr), TK)]
    l_d = L(s, "datei", W_DATEI, (xb, yr + 0.5), FM, "center", DUNKEL)
    p1 = pf(s, (r4(x0 + 1.05), yr), (r4(xi - 0.2), yr), farbe=GRUEN, spitze=0.1)
    p2 = pf(s, (r4(xi + 0.25), yr), (r4(xb - 1.1), yr), farbe=GRUEN)
    a_w = stift(s, r4(xi + 0.45), r4(mitten[1][2] - 0.1), lang=0.3)
    yl, dy = -0.25, 0.32
    l_r = L(s, "r", ("r: die Namen lesen (auflisten)", "r: read the names (list)", "r: leer los nombres (listar)",
                     "r：读取名称（列出）", "r : lire les noms (lister)", "r: adları okuma (listeleme)"), (x0, yl), FM, "left")
    l_x = L(s, "x", ("x: über einen Namen zur Datei gelangen", "x: reach the file through a name",
                     "x: llegar al archivo a través de un nombre", "x：通过名称到达文件",
                     "x : atteindre le fichier par un nom", "x: bir ad üzerinden dosyaya ulaşma"), (x0, yl - dy), FM, "left")
    l_w = L(s, "w", ("w + x: Einträge anlegen, löschen, umbenennen", "w + x: create, delete, rename entries",
                     "w + x: crear, borrar, renombrar entradas", "w + x：创建、删除、重命名条目",
                     "w + x : créer, supprimer, renommer des entrées", "w + x: girdi oluşturma, silme, yeniden adlandırma"),
            (x0, yl - 2 * dy), FM, "left")
    l_un = L(s, "unver", ("unverändert", "unchanged", "sin cambios", "未改变", "inchangé", "değişmedi"), (xb, yr - 0.5), FM,
             "center", GRAU)
    schritt(s, EIN(kopf + reihen[0] + [l_v] + dbox + [l_d], 0.7))
    s.pause(0.6)
    schritt(s, EIN(a_r + [deck, l_r], 0.7))
    s.pause(0.8)
    schritt(s, AUS(deck, 0.5), EIN(l_x, 0.5))
    schritt(s, ZEICHNE(p1, 0.6))
    schritt(s, ZEICHNE(p2, 0.7))
    s.pause(0.8)
    schritt(s, EIN(a_w + [l_w], 0.6))
    schritt(s, EIN(neu, 0.7))
    schritt(s, EIN(l_un, 0.5))
    s.speichern()


def k7loeschen():
    """Tabelle fach (Schloss w) und Datei brief.txt (Schloss, r--r--r--). rm streicht den Namen; nur das Schloss der
    Tabelle öffnet sich; danach zeigt kein Name mehr auf die Inode, sie wird grau (frei)."""
    s = Szene("linux/k7loeschen", reihenfolge="anlegen")
    x0, y0 = -3.3, 0.85
    cmd = tx(s, "rm fach/brief.txt", (0, 1.95), TT)
    l_v = L(s, "verz", W_VERZ_FACH, (x0, 1.45), FM, "left", DUNKEL)
    kopf, reihen, mitten = tabelle_verz(s, x0, y0, [("brief.txt", "…"), ("neu.txt", "…")])
    xn, xi, yr = mitten[0]
    xs_ = r4(xi + 0.65)
    zu1 = s.schloss((xs_, r4(y0 + 0.05)), 0.36, False, DUNKEL)
    auf1 = s.schloss((xs_, r4(y0 + 0.05)), 0.36, True, GRUEN)
    l_s1 = tx(s, "w", (xs_ + 0.3, r4(y0 + 0.05)), TT, "center", DUNKEL)
    xb = 1.85
    dbox = [box(s, (xb, yr), 2.1, 0.62, DUNKEL, WEISS, 2, "rect"), tx(s, "Treffen am Freitag", (xb, yr), TK)]
    l_d = L(s, "datei", W_DATEI, (xb, yr + 0.55), FM, "center", DUNKEL)
    zu2 = s.schloss((r4(xb + 1.25), yr), 0.36, False, DUNKEL)
    l_s2 = tx(s, "r--r--r--", (xb, r4(yr - 0.48)), TK, "center", DUNKEL)
    link = pf(s, (r4(xi + 0.3), yr), (r4(xb - 1.1), yr), farbe=GRAU, dash=DASH)
    strich = linie(s, (r4(x0 + 0.05), yr), (r4(xi + 0.35), yr), ROT, 3)
    l_nicht = L(s, "nicht", ("nicht gebraucht", "not needed", "no se necesita", "不需要", "pas nécessaire", "gerekmez"),
                (r4(xb + 1.25), r4(yr - 0.48)), FM, "center", GRAU)
    schl = schleier(s, (xb, yr), 2.2, 0.72, 0.65)
    l_frei = L(s, "frei", ("freigegeben: kein Name zeigt mehr darauf", "freed: no name points to it any more",
                           "liberado: ya ningún nombre apunta a él", "已释放：不再有名称指向它",
                           "libéré : plus aucun nom ne le désigne", "serbest: artık hiçbir ad onu göstermiyor"),
                (0.3, r4(yr - 0.95)), FM, "center", GRAU)
    l_w = L(s, "wtab", ("w am Verzeichnis: Tabelle ändern", "w on the directory: change the table",
                        "w en el directorio: cambiar la tabla", "目录的 w：修改目录表", "w sur le répertoire : modifier la table",
                        "dizinde w: tabloyu değiştirme"), (x0, r4(yr - 0.95 - 0.35)), FM, "left", GRUEN)
    schritt(s, EIN([cmd, l_v] + kopf + flach(reihen) + [zu1, l_s1] + dbox + [l_d, zu2, l_s2, link], 0.7))
    s.pause(0.8)
    schritt(s, BETONE(cmd, 0.6))
    schritt(s, AUS(zu1, 0.5), EIN(auf1, 0.5))
    schritt(s, ZEICHNE(strich, 0.7), AUS(link, 0.7), EIN(l_w, 0.7))
    s.pause(0.6)
    schritt(s, BETONE(zu2, 0.7), EIN(l_nicht, 0.7))
    s.pause(0.6)
    schritt(s, EIN([schl, l_frei], 0.8))
    s.speichern()


# ================================================================== Abschnitt 5: Wie der Kernel Rechte prüft
def k7pfad():
    """Pfad weg/innen/zettel.txt als Kette linuxk7 (rwx), weg (rw-), innen (rwx), zettel.txt (rw-r--r--); ein Punkt
    wandert, x wird geprüft: grün bei linuxk7, rot bei weg; der Rest bleibt grau."""
    s = Szene("linux/k7pfad", reihenfolge="anlegen")
    cmd = tx(s, "cat weg/innen/zettel.txt", (0, 1.75), TT)
    namen = (("linuxk7", "rwx", True), ("weg", "rw-", True), ("innen", "rwx", True), ("zettel.txt", "rw-r--r--", False))
    breiten = (1.3, 0.95, 1.05, 1.45)
    gap, y = 0.42, 0.65
    x = -sum(breiten) / 2 - 1.5 * gap + 0.25
    teile, rechte, mitten = [], [], []
    for (n, r, verz), b in zip(namen, breiten):
        m = x + b / 2
        if verz:
            teile += [box(s, (m, y), b, 0.38, BLAU, BLAU_HELL, 2), tx(s, n, (m, y), TT)]
        else:
            teile += [box(s, (m, y), b, 0.38, GRAU, WEISS, 2, "rect"), tx(s, n, (m, y), TT)]
        rechte.append(s.raster([r], (m, r4(y - 0.42)), groesse=TT, ausrichtung="mitte"))
        mitten.append(r4(m))
        x += b + gap
    sl = [pf(s, (r4(mitten[i] + breiten[i] / 2 + 0.04), y), (r4(mitten[i + 1] - breiten[i + 1] / 2 - 0.04), y), farbe=GRAU,
             spitze=0.1) for i in range(3)]
    xp0 = r4(mitten[0] - breiten[0] / 2 - 0.35)
    dot = s.punkt(None, xp0, r4(y + 0.36), ORANGE, 0.09)
    m1 = rechte[0].rahmen(0, 2, 2, GRUEN, 3)
    m2 = rechte[1].rahmen(0, 2, 2, ROT, 3)
    hk = haken(s, mitten[0], r4(y - 0.85))
    kz = kreuz(s, mitten[1], r4(y - 0.85), 0.22)
    schl = [schleier(s, (mitten[i], r4(y - 0.2)), breiten[i] + 0.12, 0.95, 0.65) for i in (2, 3)]
    l_x = L(s, "x", ("An jedem Verzeichnis prüft der Kernel x.", "At every directory the kernel checks x.",
                     "En cada directorio el núcleo comprueba x.", "内核在每个目录检查 x。",
                     "À chaque répertoire, le noyau vérifie x.", "Çekirdek her dizinde x'i denetler."), (0, -0.75), FM)
    l_grau = L(s, "grau", ("nicht erreicht", "not reached", "no alcanzado", "未到达", "non atteint", "ulaşılmadı"),
               (r4((mitten[2] + mitten[3]) / 2), r4(y - 0.85)), FM, "center", GRAU)
    schritt(s, EIN([cmd] + teile + flach([r.ids for r in rechte]) + sl, 0.7))
    s.pause(0.6)
    schritt(s, EIN(dot, 0.4), EIN(l_x, 0.4))
    schritt(s, ZU(dot, mitten[0], r4(y + 0.36), 0.7))
    schritt(s, ZEICHNE(m1, 0.5), EIN(hk, 0.5))
    s.pause(0.4)
    schritt(s, ZU(dot, mitten[1], r4(y + 0.36), 0.7))
    schritt(s, ZEICHNE(m2, 0.5), EIN(kz, 0.5))
    s.pause(0.6)
    schritt(s, EIN(schl + [l_grau], 0.7))
    s.speichern()


def k7entscheidung():
    """Entscheidungsbaum UID 0? → Besitzer? → Gruppe? → andere; zum Schluss leuchtet der Weg für student und
    ----r--r--: zweite Frage ja, u-Bits ---, verboten."""
    s = Szene("linux/k7entscheidung", reihenfolge="anlegen")
    xq, xo, bq, bo = -1.5, 1.88, 2.8, 2.6
    yq = (1.9, 0.8, -0.4)
    w_q = ((("q1", ("Benutzernummer des Prozesses = 0?", "process user ID = 0?", "¿número de usuario del proceso = 0?",
                    "进程的用户号 = 0？", "numéro d'utilisateur du processus = 0 ?", "sürecin kullanıcı numarası = 0?")),),
           (("q2", ("Ist sie die des Besitzers?", "Is it the owner's?", "¿Es la del propietario?", "是所有者的吗？",
                    "Est-ce celui du propriétaire ?", "Sahibinki mi?")),),
           (("q3a", ("Ist die Gruppe der Datei", "Is the file's group", "¿Es el grupo del archivo", "文件的组是否为",
                     "Le groupe du fichier est-il", "Dosyanın grubu")),
            ("q3b", ("eine Gruppe des Prozesses?", "a group of the process?", "un grupo del proceso?", "进程的某个组？",
                     "un groupe du processus ?", "sürecin bir grubu mu?"))))
    w_o = ((("o1a", ("erlaubt", "allowed", "permitido", "允许", "autorisé", "izin verilir")),
            ("o1b", ("(Starten nur mit einem x)", "(running only with an x)", "(ejecutar solo con una x)", "（运行需有一个 x）",
                     "(exécuter seulement avec un x)", "(çalıştırma yalnızca bir x ile)"))),
           (("o2", ("nur die u-Bits zählen", "only the u bits count", "solo cuentan los bits u", "只看 u 位",
                    "seuls les bits u comptent", "yalnızca u bitleri sayılır")),),
           (("o3", ("nur die g-Bits zählen", "only the g bits count", "solo cuentan los bits g", "只看 g 位",
                    "seuls les bits g comptent", "yalnızca g bitleri sayılır")),))
    w_ja = ("ja", "yes", "sí", "是", "oui", "evet")
    w_nein = ("nein", "no", "no", "否", "non", "hayır")
    fragen, ausg, pfeile, wort = [], [], [], []
    for i, y in enumerate(yq):
        h = 0.62 if len(w_q[i]) == 2 else 0.42
        fragen.append([box(s, (xq, y), bq, h, BLAU, BLAU_HELL, 2)] +
                      [L(s, k, w, (xq, r4(y + (0.12 if len(w_q[i]) == 2 else 0) - 0.24 * j)), FM)
                       for j, (k, w) in enumerate(w_q[i])])
        ho = 0.62 if len(w_o[i]) == 2 else 0.42
        ausg.append([box(s, (xo, y), bo, ho, GRAU, WEISS, 2)] +
                    [L(s, k, w, (xo, r4(y + (0.12 if len(w_o[i]) == 2 else 0) - 0.24 * j)), FM)
                     for j, (k, w) in enumerate(w_o[i])])
        pfeile.append(pf(s, (r4(xq + bq / 2), y), (r4(xo - bo / 2), y)))
        wort.append(L(s, "ja%d" % i, w_ja, (r4((xq + bq / 2 + xo - bo / 2) / 2), r4(y + 0.15)), FM, "center", GRUEN))
    yo = -1.45
    ausg_o = [box(s, (xq, yo), bq, 0.42, GRAU, WEISS, 2), L(s, "o4", ("die o-Bits zählen", "the o bits count",
                                                                      "cuentan los bits o", "看 o 位", "les bits o comptent",
                                                                      "o bitleri sayılır"), (xq, yo), FM)]
    runter = [pf(s, (xq, r4(yq[0] - 0.22)), (xq, r4(yq[1] + 0.22))), pf(s, (xq, r4(yq[1] - 0.22)), (xq, r4(yq[2] + 0.32))),
              pf(s, (xq, r4(yq[2] - 0.32)), (xq, r4(yo + 0.22)))]
    nein = [L(s, "n%d" % i, w_nein, (r4(xq + 0.12), r4(m)), FM, "left", ROT) for i, m in
            enumerate(((yq[0] + yq[1]) / 2, (yq[1] + yq[2]) / 2 + 0.05, (yq[2] + yo) / 2 - 0.05))]
    bsp = [L(s, "bsp", ("Beispiel: student liest", "example: student reads", "ejemplo: student lee", "例：student 读取",
                        "exemple : student lit", "örnek: student okur"), (xo, r4(yo + 0.12)), FM, "center", ORANGE),
           tx(s, "----r--r-- student student einkauf.txt", (xo, r4(yo - 0.14)), 17, "center", DUNKEL)]
    hl = [box(s, (xq, yq[0]), bq + 0.1, 0.52, ORANGE, WEISS, 3.5, deckung=0.0),
          box(s, (xq, yq[1]), bq + 0.1, 0.52, ORANGE, WEISS, 3.5, deckung=0.0),
          box(s, (xo, yq[1]), bo + 0.1, 0.52, ORANGE, WEISS, 3.5, deckung=0.0)]
    hp = [pf(s, (xq, r4(yq[0] - 0.22)), (xq, r4(yq[1] + 0.22)), farbe=ORANGE, dicke=4),
          pf(s, (r4(xq + bq / 2), yq[1]), (r4(xo - bo / 2), yq[1]), farbe=ORANGE, dicke=4)]
    erg = [tx(s, "u: ---", (r4(xo - 0.75), r4(yq[1] - 0.45)), TT, "center", ROT),
           L(s, "verb", ("verboten", "denied", "denegado", "禁止", "refusé", "reddedilir"), (r4(xo + 0.1), r4(yq[1] - 0.45)),
             FM, "left", ROT)]
    l_ob = L(s, "obwohl", ("obwohl g und o lesen dürften", "although g and o may read", "aunque g y o podrían leer",
                           "尽管 g 和 o 可以读取", "bien que g et o puissent lire", "g ve o okuyabilse de"),
             (xo, r4(yq[1] - 0.75)), FM, "center", GRAU)
    schritt(s, EIN(fragen[0], 0.6))
    schritt(s, ZEICHNE(pfeile[0], 0.5), EIN(wort[0], 0.5), WACHS(ausg[0][0], 0.5), EIN(ausg[0][1:], 0.5))
    schritt(s, ZEICHNE(runter[0], 0.5), EIN(nein[0], 0.5), WACHS(fragen[1][0], 0.5), EIN(fragen[1][1:], 0.5))
    schritt(s, ZEICHNE(pfeile[1], 0.5), EIN(wort[1], 0.5), WACHS(ausg[1][0], 0.5), EIN(ausg[1][1:], 0.5))
    schritt(s, ZEICHNE(runter[1], 0.5), EIN(nein[1], 0.5), WACHS(fragen[2][0], 0.5), EIN(fragen[2][1:], 0.5))
    schritt(s, ZEICHNE(pfeile[2], 0.5), EIN(wort[2], 0.5), WACHS(ausg[2][0], 0.5), EIN(ausg[2][1:], 0.5))
    schritt(s, ZEICHNE(runter[2], 0.5), EIN(nein[2], 0.5), WACHS(ausg_o[0], 0.5), EIN(ausg_o[1], 0.5))
    s.pause(0.8)
    schritt(s, EIN(bsp, 0.6))
    schritt(s, EIN(hl[0], 0.4))
    schritt(s, ZEICHNE(hp[0], 0.5), EIN(hl[1], 0.5))
    schritt(s, ZEICHNE(hp[1], 0.5), EIN(hl[2], 0.5))
    schritt(s, EIN(erg, 0.6))
    schritt(s, EIN(l_ob, 0.5))
    s.speichern()


def k7oeffnen():
    """Zeitachse: tail -f öffnet tagebuch.txt (r geprüft, Deskriptor als Eintrittskarte); zweites Terminal setzt
    -w-------; tail liest mit seiner Karte weiter; cat öffnet neu und scheitert."""
    s = Szene("linux/k7oeffnen", reihenfolge="anlegen")
    xs = (-2.55, -0.72, 1.02, 2.62)
    yc, yp, yk, ya_, yt = 1.5, 0.95, 0.35, -0.25, -0.9
    w_t1 = ("Terminal 1", "terminal 1", "terminal 1", "终端 1", "terminal 1", "terminal 1")
    w_t2 = ("Terminal 2", "terminal 2", "terminal 2", "终端 2", "terminal 2", "terminal 2")
    achse = pf(s, (-3.35, yt), (3.35, yt), farbe=GRAU, spitze=0.13)
    l_zeit = L(s, "zeit", ("Zeit", "time", "tiempo", "时间", "temps", "zaman"), (3.3, r4(yt + 0.2)), FM, "right", GRAU)
    ticks = [linie(s, (x, r4(yt - 0.07)), (x, r4(yt + 0.07)), GRAU, 2.5) for x in xs]
    w_ev = (("oeffnen", ("öffnen", "open", "abrir", "打开", "ouvrir", "açma")),
            ("aendern", ("Rechte ändern", "change permissions", "cambiar permisos", "修改权限", "changer les droits",
                         "izinleri değiştirme")),
            ("lesen", ("lesen", "read", "leer", "读取", "lire", "okuma")),
            ("neu", ("neu öffnen", "open again", "abrir de nuevo", "重新打开", "rouvrir", "yeniden açma")))
    ev = [L(s, k, w, (x, r4(yt - 0.27)), FM, "center", GRAU) for (k, w), x in zip(w_ev, xs)]
    c1 = [L(s, "t1", w_t1, (xs[0], r4(yc + 0.3)), FM, "center", GRAU), tx(s, "tail -f tagebuch.txt", (xs[0], yc), TK)]
    c2 = [L(s, "t2a", w_t2, (xs[1], r4(yc + 0.3)), FM, "center", GRAU), tx(s, "chmod 200 tagebuch.txt", (xs[1], yc), TK)]
    c4 = [L(s, "t2b", w_t2, (xs[3], r4(yc + 0.3)), FM, "center", GRAU), tx(s, "cat tagebuch.txt", (xs[3], yc), TK)]
    p1 = [tx(s, "r", (r4(xs[0] - 0.12), yp), TT), haken(s, r4(xs[0] + 0.15), yp)]
    p4 = [tx(s, "r", (r4(xs[3] - 0.12), yp), TT), kreuz(s, r4(xs[3] + 0.15), yp, 0.22)]
    l_p = L(s, "keine", ("keine Prüfung", "no check", "sin comprobación", "不检查", "pas de contrôle", "denetim yok"),
            (xs[2], yp), FM, "center", GRAU)
    rechte = tx(s, "rw-r--r--", (xs[1], yp), TT)

    def karte_(x):
        return [box(s, (x, yk), 1.3, 0.38, ORANGE, ORANGE_HELL, 2, "rect", DASH),
                L(s, "k%d" % int(10 * x + 40), ("Deskriptor", "descriptor", "descriptor", "描述符", "descripteur",
                                                  "tanımlayıcı"), (x, yk), FM)]
    k1 = karte_(xs[0])
    k3 = karte_(xs[0])
    z1 = tx(s, "Montag: 5 km", (xs[0], ya_), TK)
    z3 = tx(s, "Dienstag: 7 km", (xs[2], ya_), TK, "center", GRUEN)
    schritt(s, ZEICHNE(achse, 0.6), EIN(ticks + [l_zeit], 0.6))
    s.pause(0.4)
    schritt(s, EIN(c1 + [ev[0]], 0.6))
    schritt(s, EIN(p1[0], 0.4))
    schritt(s, EIN(p1[1], 0.4))
    schritt(s, WACHS(k1[0], 0.5), EIN(k1[1], 0.5))
    schritt(s, EIN(z1, 0.5))
    s.pause(0.6)
    schritt(s, EIN(c2 + [ev[1], rechte], 0.6))
    s.ersetzen(rechte, "-w-------", farbe=ORANGE, dauer=0.7)
    s.pause(0.6)
    schritt(s, EIN(k3, 0.3))
    schritt(s, *VERS(k3, xs[2] - xs[0], 0, 1.0), EIN([ev[2], l_p], 1.0))
    schritt(s, EIN(z3, 0.6))
    s.pause(0.6)
    schritt(s, EIN(c4 + [ev[3]], 0.6))
    schritt(s, EIN(p4[0], 0.4))
    schritt(s, EIN(p4[1], 0.5))
    s.speichern()


# ================================================================== Abschnitt 6: sudo und su
W_BEENDET = ("beendet", "ended", "terminado", "已结束", "terminé", "sona erdi")


def k7sudo():
    """Shell (uid=1000) → sudo hakt Erlaubnis, Passwort, Protokoll ab → whoami mit uid=0; danach ist whoami beendet,
    die Shell läuft unverändert mit uid=1000."""
    s = Szene("linux/k7sudo", reihenfolge="anlegen")
    y = 1.3
    xsh, xsu, xw = -2.62, 0.0, 2.62
    shell = proz(s, (xsh, y), 1.3, "bash", 0.42)
    e_sh = etikett(s, (xsh, r4(y - 0.5)), ["uid=1000"], 1.1)
    sudo = proz(s, (xsu, y), 1.3, "sudo", 0.42, farbe=ORANGE, fuellung=ORANGE_HELL)
    who = proz(s, (xw, y), 1.3, "whoami", 0.42)
    e_w = etikett(s, (xw, r4(y - 0.5)), ["uid=0"], 1.1, rand=ORANGE, fuellung=ORANGE_HELL)
    geist_ = geist(s, (xw, y), 1.3, 0.42)
    l_end = L(s, "end", W_BEENDET, (xw, r4(y - 0.5)), FM, "center", GRAU)
    p1 = pf(s, (r4(xsh + 0.7), y), (r4(xsu - 0.7), y))
    p2 = pf(s, (r4(xsu + 0.7), y), (r4(xw - 0.7), y))
    w_st = (("st1", ("Erlaubnis in /etc/sudoers nachsehen", "look up permission in /etc/sudoers",
                     "consultar el permiso en /etc/sudoers", "在 /etc/sudoers 中查找许可",
                     "vérifier l'autorisation dans /etc/sudoers", "/etc/sudoers içinde izne bakma")),
            ("st2", ("Passwort von student prüfen", "check the password of student", "comprobar la contraseña de student",
                     "检查 student 的密码", "vérifier le mot de passe de student", "student'ın parolasını denetleme")),
            ("st3", ("Eintrag ins Protokoll schreiben", "write an entry to the log", "escribir una entrada en el registro",
                     "向日志写入一条记录", "écrire une entrée dans le journal", "günlüğe kayıt yazma")))
    xk, ys = -1.5, (0.5, 0.15, -0.2)
    kaestchen, texte, haken_ = [], [], []
    for (k, w), yy in zip(w_st, ys):
        kaestchen.append(box(s, (xk, yy), 0.2, 0.2, DUNKEL, WEISS, 1.5, "rect"))
        texte.append(L(s, k, w, (xk + 0.2, yy), FM, "left"))
        haken_.append(haken(s, xk + 0.01, yy + 0.02, g=0.09, dicke=3.5))
    l_un = L(s, "unver", ("Shell unverändert", "shell unchanged", "shell sin cambios", "Shell 未改变", "shell inchangé",
                          "kabuk değişmedi"), (xsh, r4(y - 0.88)), FM, "center", BLAU)
    schritt(s, EIN(shell + e_sh, 0.6))
    s.pause(0.4)
    schritt(s, ZEICHNE(p1, 0.5), WACHS(sudo[0], 0.5), EIN(sudo[1], 0.5))
    schritt(s, EIN(kaestchen + texte, 0.6))
    for h in haken_:
        schritt(s, EIN(h, 0.45))
    s.pause(0.5)
    schritt(s, ZEICHNE(p2, 0.5), WACHS(who[0], 0.5), EIN(who[1:] + e_w, 0.5))
    s.pause(0.8)
    schritt(s, AUS(who + e_w, 0.7), EIN([geist_, l_end], 0.7))
    schritt(s, BETONE(e_sh[1], 0.8), EIN(l_un, 0.8))
    s.speichern()


REGEL = "%sudo   ALL=(ALL:ALL) ALL"


def k7sudoers():
    """Regel %sudo ALL=(ALL:ALL) ALL; die vier Teile leuchten nacheinander mit ihrer Bedeutung; Pfeil von %sudo zur
    Zeile sudo:x:27:student in /etc/group."""
    s = Szene("linux/k7sudoers", reihenfolge="anlegen")
    g = s.raster(REGEL, (0, 0.95), groesse=26, ausrichtung="mitte")
    l_s = tx(s, "/etc/sudoers", (r4(g.rechts + 0.2), 0.95), TK, "left", GRAU)
    teile = ((0, 4, BLAU, "wer", ("wer: alle Mitglieder der Gruppe sudo", "who: all members of group sudo",
                                  "quién: todos los miembros del grupo sudo", "谁：sudo 组的所有成员",
                                  "qui : tous les membres du groupe sudo", "kim: sudo grubunun tüm üyeleri")),
             (8, 10, GRUEN, "wo", ("wo: auf jedem Rechner", "where: on every host", "dónde: en cualquier equipo",
                                   "在哪里：在每台主机上", "où : sur chaque machine", "nerede: her bilgisayarda")),
             (12, 20, ORANGE, "alswer", ("als wer: als jeder Benutzer und mit jeder Gruppe", "as whom: as any user, with any group",
                                         "como quién: como cualquier usuario y con cualquier grupo",
                                         "以谁的身份：任何用户、任何组", "en tant que qui : tout utilisateur, tout groupe",
                                         "kim olarak: her kullanıcı ve her grup olarak")),
             (22, 24, DUNKEL, "was", ("was: jeder Befehl", "what: any command", "qué: cualquier orden", "做什么：任何命令",
                                      "quoi : toute commande", "ne: her komut")))
    mk, lt, kl, zeilen = [], [], [], []
    x0, y0, dy = -3.2, 0.25, 0.32
    for i, (a, b, f, k, w) in enumerate(teile):
        mk.append(g.markieren(0, a, b, f, 0.22))
        lt.append(g.teil(0, a, b))
        kl.append(g.klammer(0, a, b, "", seite="unten", farbe=f)[0])
        yy = r4(y0 - i * dy)
        zeilen.append([tx(s, REGEL[a:b + 1], (x0, yy), TT, "left", f), L(s, k, w, (x0 + 1.15, yy), FM, "left", f)])
    d = s.datei("/etc/group", "sudo:x:27:student", pos=(-3.35, 2.4), groesse=TT)
    m_g = d.markieren(0, 0, 3, BLAU, 0.25)
    pg = pf(s, (g.xm(0, 4), r4(g.oben(0) + 0.03)), (r4(d.rechts + 0.04), d.y(0)), knick="vh", farbe=BLAU)
    schritt(s, EIN(g.ids + lt + [l_s], 0.7))
    s.pause(0.5)
    for i in range(4):
        schritt(s, EIN(mk[i], 0.4))
        schritt(s, BETONE(lt[i], 0.6), ZEICHNE(kl[i], 0.6), EIN(zeilen[i], 0.6))
        s.pause(0.3)
    s.pause(0.4)
    schritt(s, EIN(d.id, 0.5), AUS(lt, 0.5))          # Leucht-Kopien ausblenden (deckungsgleich, im Endbild doppelt)
    schritt(s, ZEICHNE(pg, 0.8), EIN(m_g, 0.8))
    s.speichern()


def k7sudofalle():
    """Oben sudo echo Hallo > nurroot.txt: die Shell (uid=1000) öffnet zuerst, der Kernel lehnt ab, sudo und echo starten
    nicht. Unten echo Hallo | sudo tee nurroot.txt: tee läuft mit uid=0 und öffnet selbst."""
    s = Szene("linux/k7sudofalle", reihenfolge="anlegen")
    xa, xd = -2.6, 2.45

    def datei_(y):
        return [box(s, (xd, y), 1.6, 0.42, GRAU, WEISS, 2, "rect"), tx(s, "nurroot.txt", (xd, y), TT),
                tx(s, "root root rw-r--r--", (xd, r4(y - 0.38)), TK, "center", DUNKEL)]
    y1 = 1.3
    c1 = tx(s, "$ sudo echo Hallo > nurroot.txt", (0, 2.0), TT)
    sh = proz(s, (xa, y1), 1.2, "bash", 0.42)
    e1 = etikett(s, (xa, r4(y1 - 0.48)), ["uid=1000"], 1.1)
    d1 = datei_(y1)
    p1 = pf(s, (r4(xa + 0.64), y1), (r4(xd - 0.84), y1), farbe=ROT)
    l1 = L(s, "zuerst", ("öffnet zuerst für >", "opens first for >", "abre primero para >", "先为 > 打开",
                         "ouvre d'abord pour >", "önce > için açar"), (0.0, r4(y1 + 0.2)), FM, "center")
    kz = kreuz(s, 1.2, y1, 0.26)
    l_k = L(s, "pruef", ("Kernel prüft 1000: abgelehnt", "kernel checks 1000: denied", "el núcleo comprueba 1000: denegado",
                         "内核用 1000 检查：拒绝", "le noyau vérifie 1000 : refusé", "çekirdek 1000'i denetler: reddedildi"),
              (0.35, r4(y1 - 0.25)), FM, "center", ROT)
    gs = [box(s, (x, r4(y1 - 0.72)), 0.85, 0.36, HELLGRAU, WEISS, 2, dash=DASH) for x in (-0.95, 0.05)]
    gt = [tx(s, n, (x, r4(y1 - 0.72)), TK, "center", GRAU) for n, x in (("sudo", -0.95), ("echo", 0.05))]
    l_g = L(s, "nicht", ("starten nicht", "never start", "no se inician", "不会启动", "ne démarrent pas", "başlamaz"),
            (0.62, r4(y1 - 0.72)), FM, "left", GRAU)
    y2 = -0.85
    c2 = tx(s, "$ echo Hallo | sudo tee nurroot.txt", (0, -0.15), TT)
    ec = proz(s, (xa, y2), 1.2, "echo", 0.42)
    te = proz(s, (-0.25, y2), 1.2, "tee", 0.42, farbe=ORANGE, fuellung=ORANGE_HELL)
    e2 = etikett(s, (-0.25, r4(y2 - 0.48)), ["uid=0"], 1.1, rand=ORANGE, fuellung=ORANGE_HELL)
    l_su = L(s, "unter", ("unter sudo", "under sudo", "bajo sudo", "在 sudo 下", "sous sudo", "sudo altında"),
             (-0.25, r4(y2 + 0.36)), FM, "center", ORANGE)
    pp = pf(s, (r4(xa + 0.64), y2), (-0.89, y2), farbe=BLAU)
    l_pp = L(s, "pipe", ("Pipe", "pipe", "tubería", "管道", "tube", "boru"), (-1.47, r4(y2 + 0.2)), FM, "center", BLAU)
    d2 = datei_(y2)
    p2 = pf(s, (0.39, y2), (r4(xd - 0.84), y2), farbe=GRUEN)
    l2 = L(s, "selbst", ("öffnet selbst", "opens itself", "abre por sí mismo", "自己打开", "ouvre lui-même", "kendisi açar"),
           (1.0, r4(y2 + 0.2)), FM, "center", GRUEN)
    hk = haken(s, 1.0, r4(y2 - 0.22))
    schritt(s, EIN([c1] + sh + e1 + d1, 0.6))
    s.pause(0.4)
    schritt(s, ZEICHNE(p1, 0.7), EIN(l1, 0.7))
    schritt(s, BETONE(e1[1], 0.7))
    schritt(s, EIN([kz, l_k], 0.5))
    schritt(s, EIN(gs + gt + [l_g], 0.5))
    s.pause(0.8)
    schritt(s, EIN([c2] + ec + d2, 0.6))
    schritt(s, ZEICHNE(pp, 0.6), EIN(l_pp, 0.6), WACHS(te[0], 0.6), EIN([te[1], l_su] + e2, 0.6))
    schritt(s, ZEICHNE(p2, 0.7), EIN(l2, 0.7))
    schritt(s, EIN(hk, 0.5))
    s.speichern()


def k7susudo():
    """Links su - (Passwort von root, Shell mit uid=0 bis exit, Protokoll „root“), rechts sudo befehl (eigenes Passwort,
    ein Befehl mit uid=0, Name und Befehl im Protokoll); zuletzt wird das root-Passwort durchgestrichen."""
    s = Szene("linux/k7susudo", reihenfolge="anlegen")
    xl, xr = -1.75, 1.75
    kopf = [tx(s, "su -", (xl, 2.05), 22), tx(s, "sudo befehl", (xr, 2.05), 22)]
    trenn = linie(s, (0, 2.2), (0, -1.0), HELLGRAU, 2)
    pw_l = [L(s, "pwl", ("Passwort von root", "password of root", "contraseña de root", "root 的密码", "mot de passe de root",
                         "root'un parolası"), (xl, 1.6), FM, "center"),
            box(s, (xl, 1.3), 1.9, 0.34, DUNKEL, WEISS, 1.5, "rect"), tx(s, "••••••", (xl, 1.3), TT)]
    pw_r = [L(s, "pwr", ("eigenes Passwort", "your own password", "tu propia contraseña", "自己的密码", "son propre mot de passe",
                         "kendi parolası"), (xr, 1.6), FM, "center"),
            box(s, (xr, 1.3), 1.9, 0.34, DUNKEL, WEISS, 1.5, "rect"), tx(s, "••••••", (xr, 1.3), TT)]
    sh = [box(s, (xl, 0.35), 2.6, 1.05, BLAU, BLAU_HELL, 2.5),
          L(s, "shell0", ("Shell mit uid=0", "shell with uid=0", "shell con uid=0", "uid=0 的 Shell", "shell avec uid=0",
                          "uid=0 olan kabuk"), (xl, 0.7), FM, "center")] + \
         [tx(s, z, (r4(xl - 0.9), r4(0.43 - 0.22 * i)), TK, "left") for i, z in enumerate(("# befehl", "# befehl", "# exit"))]
    l_viele = L(s, "viele", ("beliebig viele Befehle", "any number of commands", "cualquier número de órdenes", "任意多条命令",
                             "autant de commandes que voulu", "istenen sayıda komut"), (xl, -0.4), FM, "center", BLAU)
    ein = [box(s, (xr, 0.6), 2.0, 0.4, ORANGE, ORANGE_HELL, 2.5), tx(s, "befehl  uid=0", (xr, 0.6), TK)]
    p_r = pf(s, (xr, 0.38), (xr, 0.08), farbe=GRAU)
    zur = [L(s, "zurueck", ("danach sofort wieder uid=1000", "then immediately uid=1000 again", "luego enseguida uid=1000 otra vez",
                            "随后立即恢复 uid=1000", "puis aussitôt de nouveau uid=1000", "sonra hemen yine uid=1000"),
             (xr, -0.08), FM, "center", BLAU)]
    l_ein = L(s, "ein", ("genau ein Befehl", "exactly one command", "exactamente una orden", "恰好一条命令", "exactement une commande",
                         "tam olarak bir komut"), (xr, -0.4), FM, "center", ORANGE)
    w_pr = ("im Protokoll:", "in the log:", "en el registro:", "日志中：", "dans le journal :", "günlükte:")
    prot = [L(s, "prl", w_pr, (xl, -0.75), FM, "center", GRAU), tx(s, "root", (xl, -1.0), TK),
            L(s, "prr", w_pr, (xr, -0.75), FM, "center", GRAU), tx(s, "student : … COMMAND=befehl", (xr, -1.0), TK)]
    strich = linie(s, (r4(xl - 1.05), 1.18), (r4(xl + 1.05), 1.42), ROT, 3.5)
    l_kein = L(s, "kein", ("Unter Ubuntu hat root kein Passwort.", "On Ubuntu, root has no password.",
                           "En Ubuntu, root no tiene contraseña.", "在 Ubuntu 上 root 没有密码。",
                           "Sous Ubuntu, root n'a pas de mot de passe.", "Ubuntu'da root'un parolası yoktur."),
              (0, -1.45), FM, "center", ROT)
    schritt(s, EIN(kopf + [trenn], 0.6))
    schritt(s, EIN(pw_l, 0.6))
    schritt(s, WACHS(sh[0], 0.6), EIN(sh[1:], 0.6))
    schritt(s, EIN(l_viele, 0.5))
    schritt(s, EIN(prot[:2], 0.5))
    s.pause(0.8)
    schritt(s, EIN(pw_r, 0.6))
    schritt(s, WACHS(ein[0], 0.6), EIN(ein[1:], 0.6))
    schritt(s, ZEICHNE(p_r, 0.5), EIN(zur + [l_ein], 0.5))
    schritt(s, EIN(prot[2:], 0.5))
    s.pause(0.8)
    schritt(s, ZEICHNE(strich, 0.6), EIN(l_kein, 0.6))
    s.speichern()


# ================================================================== Abschnitt 7: Benutzer und Gruppen anlegen
def k7adduser():
    """In der Mitte adduser; nacheinander Pfeile zu /etc/passwd (neue Zeile), /etc/group (anna, users), /etc/shadow
    (anna:!:…, ohne Passwort) und /home/anna (aus /etc/skel)."""
    s = Szene("linux/k7adduser", reihenfolge="anlegen")
    cmd_t = 'sudo adduser --disabled-password --comment "Anna Berg" anna'
    kc = box(s, (0, 0.38), 4.65, 0.42, DUNKEL, GRAU_HELL, 2)
    cmd = tx(s, cmd_t, (0, 0.38), TK)
    gruen = lambda t: farbig(t, "gruen")
    pw = s.datei("/etc/passwd", farbig("…", "grau"), pos=(-3.42, 2.3), spalten=47, zeilen=2, groesse=TK)
    gr = s.datei("/etc/group", "users:x:100:\n" + farbig("…", "grau"), pos=(0.95, 2.3), spalten=16, zeilen=3, groesse=TK)
    sh = s.datei("/etc/shadow", farbig("…", "grau"), pos=(-2.75, -0.15), spalten=15, zeilen=2, groesse=TK)
    l_sh = L(s, "ohne", ("ohne Passwort", "no password", "sin contraseña", "无密码", "sans mot de passe", "parolasız"),
             (r4(sh.rechts + 0.15), r4(sh.y(1))), FM, "left", GRAU)
    xh, yh = 1.35, -0.42
    home = [box(s, (xh, yh), 1.55, 0.4, BLAU, BLAU_HELL, 2), tx(s, "/home/anna", (xh, yh), TT)]
    l_home = tx(s, "drwxr-x--- anna anna", (xh, r4(yh - 0.36)), TK, "center", DUNKEL)
    skel = [box(s, (2.85, r4(yh - 0.95)), 1.1, 0.36, GRAU, WEISS, 1.5, "rect"), tx(s, "/etc/skel", (2.85, r4(yh - 0.95)), TK,
                                                                                   "center", GRAU)]
    p_sk = pf(s, (2.85, r4(yh - 0.75)), (r4(xh + 0.6), r4(yh - 0.2)), farbe=GRAU, dicke=2)
    l_sk = L(s, "vorl", ("Vorlagen", "templates", "plantillas", "模板", "modèles", "şablonlar"), (2.5, r4(yh - 0.36)), FM,
             "left", GRAU)
    pfeile = [pf(s, (-1.6, 0.6), (-1.6, r4(pw.unten_kante - 0.04)), farbe=GRUEN),
              pf(s, (1.6, 0.6), (1.6, r4(gr.unten_kante - 0.04)), farbe=GRUEN),
              pf(s, (-2.15, 0.16), (-2.15, r4(sh.oben_kante + 0.04)), farbe=GRUEN),
              pf(s, (xh, 0.16), (xh, r4(yh + 0.22)), farbe=GRUEN)]
    schritt(s, EIN([kc, cmd], 0.6))
    s.pause(0.5)
    schritt(s, EIN(pw.id, 0.5))
    schritt(s, ZEICHNE(pfeile[0], 0.6))
    pw.zeile_dazu(gruen("anna:x:1001:1001:Anna Berg:/home/anna:/bin/bash"), dauer=0.7)
    s.pause(0.4)
    schritt(s, EIN(gr.id, 0.5))
    schritt(s, ZEICHNE(pfeile[1], 0.6))
    gr.schritt("\\e[s\\e[1;13H" + gruen("anna") + "\\e[u\n" + gruen("anna:x:1001:"), dauer=0.7)
    s.pause(0.4)
    schritt(s, EIN(sh.id, 0.5))
    schritt(s, ZEICHNE(pfeile[2], 0.6))
    sh.zeile_dazu(gruen("anna:!:…"), dauer=0.7)
    schritt(s, EIN(l_sh, 0.4))
    s.pause(0.4)
    schritt(s, ZEICHNE(pfeile[3], 0.6), WACHS(home[0], 0.6), EIN(home[1:] + [l_home], 0.6))
    schritt(s, EIN(skel, 0.5))
    schritt(s, ZEICHNE(p_sk, 0.6), EIN(l_sk, 0.6))
    s.speichern()


def k7usermod():
    """Zusatzgruppen von anna: users, student. Links -aG kochclub: kommt hinzu; rechts -G kochclub: users und student
    rot gestrichen und verschwinden; darunter ein Schloss vor /home/student."""
    s = Szene("linux/k7usermod", reihenfolge="anlegen")
    xl, xr = -1.75, 1.75
    kopf = L(s, "kopf", ("Zusatzgruppen von anna", "supplementary groups of anna", "grupos suplementarios de anna",
                         "anna 的附加组", "groupes supplémentaires d'anna", "anna'nın ek grupları"), (0, 2.1), FM, "center",
             DUNKEL)
    cmds = [tx(s, "sudo usermod -aG kochclub anna", (xl, 1.65), TK), tx(s, "sudo usermod -G kochclub anna", (xr, 1.65), TK)]
    trenn = linie(s, (0, 1.85), (0, -1.15), HELLGRAU, 2)
    ys = (1.1, 0.68, 0.26)

    def karte_(x, y, n, rand=DUNKEL, f=WEISS):
        return [box(s, (x, y), 1.6, 0.34, rand, f, 2), tx(s, n, (x, y), TT)]
    li = karte_(xl, ys[0], "users") + karte_(xl, ys[1], "student")
    re_ = karte_(xr, ys[0], "users") + karte_(xr, ys[1], "student")
    neu_l = karte_(xl, ys[2], "kochclub", GRUEN, GRUEN_HELL)
    neu_r = karte_(xr, ys[2], "kochclub", GRUEN, GRUEN_HELL)
    schl = [schleier(s, (xr, y), 1.7, 0.4, 0.7) for y in ys[:2]]
    striche = [linie(s, (r4(xr - 0.85), y), (r4(xr + 0.85), y), ROT, 3.5) for y in ys[:2]]
    l_bl = L(s, "bleiben", ("alte Gruppen bleiben", "old groups stay", "los grupos antiguos se quedan", "原有的组保留",
                            "les anciens groupes restent", "eski gruplar kalır"), (xl, -0.15), FM, "center", GRUEN)
    l_er = L(s, "ersetzt", ("ganze Liste ersetzt", "whole list replaced", "lista entera reemplazada", "整个列表被替换",
                            "liste entière remplacée", "tüm liste değiştirildi"), (xr, -0.15), FM, "center", ROT)
    lock = s.schloss((r4(xr - 0.95), -0.68), 0.34, False, DUNKEL)
    l_lock = tx(s, "/home/student", (r4(xr - 0.7), -0.68), TT, "left")
    l_zu = L(s, "zu", ("anna kommt nicht mehr hinein", "anna can no longer get in", "anna ya no puede entrar",
                       "anna 再也进不去", "anna ne peut plus y entrer", "anna artık giremez"), (xr, -1.0), FM, "center", ROT)
    schritt(s, EIN([kopf, trenn] + cmds + li + re_, 0.7))
    s.pause(0.8)
    schritt(s, WACHS(neu_l[0], 0.6), EIN(neu_l[1], 0.6), EIN(l_bl, 0.6))
    s.pause(0.8)
    schritt(s, WACHS(neu_r[0], 0.6), EIN(neu_r[1], 0.6))
    schritt(s, ZEICHNE(striche, 0.6))
    schritt(s, EIN(schl + [l_er], 0.7))
    s.pause(0.6)
    schritt(s, EIN([lock, l_lock], 0.6))
    schritt(s, EIN(l_zu, 0.5))
    s.speichern()


def k7zweiquellen():
    """Links /etc/group bekommt eine neue Mitgliedschaft; rechts die laufende Shell mit altem Etikett. id "$USER" findet
    die Gruppe in der Datei, id fragt den eigenen Prozess und findet sie nicht; unten ein neuer Prozess mit frischem
    Etikett."""
    s = Szene("linux/k7zweiquellen", reihenfolge="anlegen")
    d = s.datei("/etc/group", "sudo:x:27:student\nkochclub:x:1002:anna", pos=(-3.42, 2.25), spalten=28, zeilen=2,
                groesse=TK)
    m_neu = d.markieren(1, 0, 27, ORANGE, 0.22)
    xs_, ys_ = 2.3, 1.75
    l_sh = L(s, "lauf", ("laufende Shell", "running shell", "shell en marcha", "正在运行的 Shell", "shell en cours", "çalışan kabuk"),
             (xs_, r4(ys_ + 0.38)), FM, "center", GRAU)
    sh = proz(s, (xs_, ys_), 1.3, "bash", 0.4)
    et = etikett(s, (xs_, r4(ys_ - 0.62)), ["uid=1000 gid=1000", W_GRUPPEN], 1.9, key="ea")
    q1 = tx(s, 'id "$USER"', (-0.35, 0.55), TT)
    q2 = tx(s, "id", (0.45, -0.05), TT)
    p1 = pf(s, (-0.8, 0.62), (r4(d.rechts - 0.4), r4(d.unten_kante - 0.04)), farbe=GRUEN)
    p2 = pf(s, (0.65, 0.0), (r4(xs_ - 0.6), r4(ys_ - 0.95)), farbe=ROT)
    r1 = [haken(s, -0.7, 0.25), tx(s, "1002(kochclub)", (-0.48, 0.25), TK, "left", GRUEN)]
    r2 = [kreuz(s, 0.45, -0.32, 0.22), L(s, "fehlt", ("1002 fehlt", "1002 missing", "falta 1002", "缺少 1002", "1002 absent",
                                                      "1002 yok"), (0.7, -0.32), FM, "left", ROT)]
    yn = -1.1
    l_np = L(s, "neu", ("neuer Prozess: Anmeldung oder sudo -u", "new process: login or sudo -u",
                        "proceso nuevo: inicio de sesión o sudo -u", "新进程：登录或 sudo -u",
                        "nouveau processus : connexion ou sudo -u", "yeni süreç: oturum açma veya sudo -u"),
             (-0.75, r4(yn + 0.42)), FM, "center", GRAU)
    np_ = proz(s, (-0.75, yn), 2.5, 'sudo -u "$USER" id', 0.4, g=TK)
    et2 = etikett(s, (2.3, yn), ["uid=1000 gid=1000", ("Gruppen: 1000, 27, 1002", "groups: 1000, 27, 1002",
                                                      "grupos: 1000, 27, 1002", "组：1000, 27, 1002",
                                                      "groupes : 1000, 27, 1002", "gruplar: 1000, 27, 1002")], 2.0,
                  rand=GRUEN, key="eb")
    pn = pf(s, (-2.9, r4(d.unten_kante - 0.04)), (-2.02, yn), knick="vh", farbe=GRUEN)
    l_fr = L(s, "frisch", ("frisch gelesen", "read fresh", "leído de nuevo", "重新读取", "lu à nouveau", "yeniden okunur"),
             (-2.82, -0.3), FM, "left", GRUEN)
    pe = pf(s, (0.53, yn), (1.28, yn), farbe=GRUEN)
    schritt(s, EIN([d.id, l_sh] + sh + et, 0.7))
    s.pause(0.5)
    d.setze(1, 20, farbig(",student", ORANGE), dauer=0.7)
    schritt(s, EIN(m_neu, 0.5))
    s.pause(0.6)
    schritt(s, EIN(q1, 0.4))
    schritt(s, ZEICHNE(p1, 0.6))
    schritt(s, EIN(flach(r1), 0.5))
    s.pause(0.4)
    schritt(s, EIN(q2, 0.4))
    schritt(s, ZEICHNE(p2, 0.6))
    schritt(s, EIN(flach(r2), 0.5))
    s.pause(0.6)
    schritt(s, EIN([l_np] + np_, 0.6))
    schritt(s, ZEICHNE(pn, 0.7), EIN(l_fr, 0.7))
    schritt(s, ZEICHNE(pe, 0.4), EIN(et2, 0.6))
    s.speichern()


# ================================================================== Abschnitt 8: chown, chgrp, umask
def k7umask():
    """Rechenbild: verlangt 666 / 777, umask 022, umgekehrt, Bit für Bit UND → 644 = rw-r--r-- und 755 = rwxr-xr-x."""
    s = Szene("linux/k7umask", reihenfolge="anlegen")
    def z(links, okt_l, rechts, okt_r):              # Bits Spalten 0-10, Oktal 13-15, Bits 18-28, Oktal 31-33
        return (links.ljust(13) + okt_l.ljust(5) + rechts.ljust(13) + okt_r).rstrip()
    zeilen = [z("touch", "", "mkdir", ""), z(" u   g   o", "", " u   g   o", ""),
              z("110 110 110", "666", "111 111 111", "777"), z("000 010 010", "022", "000 010 010", "022"),
              z("111 101 101", "", "111 101 101", ""), z("110 100 100", "644", "111 101 101", "755"),
              z("rw- r-- r--", "", "rwx r-x r-x", "")]
    g = s.raster(zeilen, (-1.25, 1.85), groesse=20, zeilenabstand=1.6)
    xl = r4(g.links - 0.2)
    w = (("verl", ("verlangt", "requested", "solicitado", "请求的", "demandé", "istenen")),
         ("um", ("umask", "umask", "umask", "umask", "umask", "umask")),
         ("umg", ("umask umgekehrt", "umask inverted", "umask invertida", "umask 取反", "umask inversé", "ters umask")),
         ("erg", ("Ergebnis", "result", "resultado", "结果", "résultat", "sonuç")),
         ("rech", ("Rechte", "permissions", "permisos", "权限", "droits", "izinler")))
    lab = [L(s, k, ww, (xl, g.y(i + 2)), FM, "right", GRAU) for i, (k, ww) in enumerate(w)]
    einsen = (5, 9, 23, 27)
    m3 = [g.markieren(3, c, c, ORANGE, 0.4) for c in einsen]
    m4 = [g.markieren(4, c, c, ORANGE, 0.4) for c in einsen]
    m5 = [g.markieren(5, c, c, ORANGE, 0.4) for c in einsen]
    y_l = r4((g.unten(4) + g.oben(5)) / 2)
    strich = linie(s, (r4(g.x(0) - 0.05), y_l), (r4(g.xr(33) + 0.05), y_l), DUNKEL, 2)
    r644 = g.rahmen(5, 13, 15, BLAU, 2.5)
    r755 = g.rahmen(5, 31, 33, BLAU, 2.5)
    l_und = L(s, "und", ("Ergebnis = verlangt UND umgekehrte umask (Bit für Bit)", "result = requested AND inverted umask (bit by bit)",
                         "resultado = solicitado Y umask invertida (bit a bit)", "结果 = 请求的 与 取反的 umask（逐位）",
                         "résultat = demandé ET umask inversé (bit à bit)", "sonuç = istenen VE ters umask (bit bit)"),
              (0.25, r4(g.y(6) - 0.45)), FM, "center", DUNKEL)
    schritt(s, EIN([g.zeile(0), g.zeile(1), g.zeile(2), lab[0]], 0.7))
    s.pause(0.6)
    schritt(s, EIN([g.zeile(3), lab[1]], 0.6))
    schritt(s, EIN(m3, 0.5))
    s.pause(0.5)
    schritt(s, EIN([g.zeile(4), lab[2]] + m4, 0.7))
    s.pause(0.6)
    schritt(s, ZEICHNE(strich, 0.4))
    schritt(s, EIN([g.zeile(5), lab[3]] + m5, 0.8))
    schritt(s, ZEICHNE([r644, r755], 0.5))
    s.pause(0.4)
    schritt(s, EIN([g.zeile(6), lab[4]], 0.6))
    schritt(s, EIN(l_und, 0.5))
    s.speichern()


def k7undnicht():
    """Zwei Spalten: wegnehmen (666 UND NICHT 033 = 644 = rw-r--r--) gegen abziehen (666 − 033 = 633 = rw--wx-wx);
    die Unterschiede in Gruppe und andere leuchten rot."""
    s = Szene("linux/k7undnicht", reihenfolge="anlegen")
    li = s.raster(["666 = 110 110 110", "033 = 000 011 011", "644 = 110 100 100", ""], (-3.15, 1.25),
                  groesse=20, zeilenabstand=1.6)
    re_ = s.raster(["  666", "- 033", "= 633 = 110 011 011", ""], (0.75, 1.25), groesse=20, zeilenabstand=1.6)
    rwx_l = li.teil(3, 6, 16, text="rw- r-- r--")     # ohne führende Leerzeichen (beginnt unter den Bits)
    rwx_r = re_.teil(3, 8, 18, text="rw- -wx -wx")
    k_l = L(s, "weg", ("wegnehmen (Bit für Bit)", "taking away (bit by bit)", "quitar (bit a bit)", "去掉（逐位）",
                       "retirer (bit à bit)", "çıkarıp atma (bit bit)"), (li.xm(0, 16), 1.75), FM, "center", GRUEN)
    k_r = L(s, "ab", ("abziehen (Ziffer für Ziffer)", "subtracting (digit by digit)", "restar (cifra a cifra)", "相减（逐位数字）",
                      "soustraire (chiffre par chiffre)", "çıkarma (basamak basamak)"), (re_.xm(0, 18), 1.75), FM, "center",
              ROT)
    y_l = r4((li.unten(1) + li.oben(2)) / 2)
    s_l = linie(s, (r4(li.x(0) - 0.05), y_l), (r4(li.xr(16) + 0.05), y_l), DUNKEL, 2)
    s_r = linie(s, (r4(re_.x(0) - 0.05), y_l), (r4(re_.xr(4) + 0.05), y_l), DUNKEL, 2)
    m_l = [li.markieren(2, 10, 16, ROT, 0.25), li.markieren(3, 10, 16, ROT, 0.25)]
    m_r = [re_.markieren(2, 12, 18, ROT, 0.25), re_.markieren(3, 12, 18, ROT, 0.25)]
    r_l = li.rahmen(2, 0, 2, GRUEN, 2.5)
    r_r = re_.rahmen(2, 2, 4, ROT, 2.5)
    l_ok = L(s, "ok", ("richtig", "correct", "correcto", "正确", "correct", "doğru"), (li.xm(0, 2), r4(li.y(3) - 0.05)), FM,
             "center", GRUEN)
    l_falsch = L(s, "falsch", ("falsch", "wrong", "incorrecto", "错误", "faux", "yanlış"), (re_.xm(0, 4), r4(re_.y(3) - 0.05)), FM,
                 "center", ROT)
    l_g = L(s, "grp", ("Gruppe: links r ohne x, rechts x ohne r", "group: left r without x, right x without r",
                       "grupo: a la izquierda r sin x, a la derecha x sin r", "组：左边有 r 无 x，右边有 x 无 r",
                       "groupe : à gauche r sans x, à droite x sans r", "grup: solda x'siz r, sağda r'siz x"),
            (0, r4(li.y(3) - 0.5)), FM, "center", ROT)
    schritt(s, EIN([k_l, li.zeile(0), li.zeile(1)], 0.7))
    schritt(s, ZEICHNE(s_l, 0.4))
    schritt(s, EIN([li.zeile(2), li.zeile(3), rwx_l], 0.7))
    schritt(s, ZEICHNE(r_l, 0.4), EIN(l_ok, 0.4))
    s.pause(0.8)
    schritt(s, EIN([k_r, re_.zeile(0), re_.zeile(1)], 0.7))
    schritt(s, ZEICHNE(s_r, 0.4))
    schritt(s, EIN([re_.zeile(2), re_.zeile(3), rwx_r], 0.7))
    schritt(s, ZEICHNE(r_r, 0.4), EIN(l_falsch, 0.4))
    s.pause(0.6)
    schritt(s, EIN(m_l + m_r, 0.7))
    schritt(s, EIN(l_g, 0.5))
    s.speichern()


# ================================================================== Abschnitt 9: besondere Rechte
W_REAL = ("real", "real", "real", "实际", "réel", "gerçek")
W_EFF = ("effektiv", "effective", "efectivo", "有效", "effectif", "etkin")


def re_karte(s, mitte, real, eff, key, rand=GRAU, fuellung=GELB, sichtbar=(True, True)):
    """Etikett „real …, effektiv …“; Ergebnis (Teile, Wert real, Wert effektiv, (x, y) real, (x, y) effektiv)."""
    x, y = mitte
    k = box(s, mitte, 1.6, 0.56, rand, fuellung, 1.5, "rect")
    lr = L(s, key + "r", W_REAL, (r4(x - 0.7), r4(y + 0.13)), FM, "left")
    le = L(s, key + "e", W_EFF, (r4(x - 0.7), r4(y - 0.13)), FM, "left")
    pr, pe = (r4(x + 0.7), r4(y + 0.13)), (r4(x + 0.7), r4(y - 0.13))
    vr = tx(s, real, pr, TK, "right") if sichtbar[0] else None
    ve = tx(s, eff, pe, TK, "right") if sichtbar[1] else None
    return [k, lr, le] + [v for v in (vr, ve) if v], vr, ve, pr, pe


def k7suid():
    """Shell (real 1000, effektiv 1000) startet meinid (Besitzer 0 = root, rwsr-xr-x, s leuchtet): neuer Prozess real
    1000 (kopiert), effektiv 0 (vom Besitzerfeld); darunter derselbe Start ohne s: real 1000, effektiv 1000."""
    s = Szene("linux/k7suid", reihenfolge="anlegen")
    xsh, xf, xp = -2.55, -0.2, 2.45
    shell = proz(s, (xsh, 0.55), 1.4, "bash", 0.42)
    k_sh, v_r, v_e, _, _ = re_karte(s, (xsh, 0.0), "1000", "1000", "sh")

    def datei_(y, rechte, key):
        k = box(s, (xf, y), 1.85, 1.0, DUNKEL, WEISS, 2, "rect")
        n = tx(s, "meinid", (xf, r4(y + 0.3)), TT)
        lb = L(s, key, ("Besitzer:", "owner:", "propietario:", "所有者：", "propriétaire :", "sahip:"), (r4(xf - 0.8), y), FM,
               "left")
        vb = tx(s, "0 (root)", (r4(xf + 0.8), y), TK, "right")
        g = s.raster([rechte], (xf, r4(y - 0.3)), groesse=TT, ausrichtung="mitte")
        return [k, n, lb, vb] + g.ids, g, (r4(xf + 0.8 - tt_breite(TK, 8)), y)
    d1, g1, p_null = datei_(1.35, "rwsr-xr-x", "b1")
    d2, g2, _ = datei_(-0.95, "rwxr-xr-x", "b2")
    m_s = g1.markieren(0, 2, 2, ORANGE, 0.4)
    s_teil = g1.teil(0, 2, 2)
    l_mit = L(s, "mit", ("mit SUID-Bit", "with SUID bit", "con bit SUID", "带 SUID 位", "avec bit SUID", "SUID bitiyle"),
              (xf, 2.05), FM, "center", ORANGE)
    l_ohne = L(s, "ohne", ("ohne s", "without s", "sin s", "没有 s", "sans s", "s olmadan"), (xf, -0.25), FM, "center", GRAU)
    p1 = proz(s, (xp, 1.65), 1.4, "meinid", 0.4)
    k1, _, _, pr1, pe1 = re_karte(s, (xp, 1.05), "", "", "p1", sichtbar=(False, False))
    p2 = proz(s, (xp, -0.65), 1.4, "meinid", 0.4)
    k2, _, _, pr2, pe2 = re_karte(s, (xp, -1.25), "", "", "p2", sichtbar=(False, False))
    a1 = [pf(s, (r4(xsh + 0.72), 0.65), (r4(xf - 0.95), 1.35)), pf(s, (r4(xf + 0.95), 1.55), (r4(xp - 0.72), 1.65))]
    a2 = [pf(s, (r4(xsh + 0.72), 0.45), (r4(xf - 0.95), -0.95)), pf(s, (r4(xf + 0.95), -0.75), (r4(xp - 0.72), -0.65))]
    c_r1 = tx(s, "1000", (r4(xsh + 0.7), r4(0.13)), TK, "right")
    c_e1 = tx(s, "0", (r4(p_null[0] + tt_breite(TK, 1) / 2), p_null[1]), TK, "center", ORANGE)
    c_r2 = tx(s, "1000", (r4(xsh + 0.7), r4(0.13)), TK, "right")
    c_e2 = tx(s, "1000", (r4(xsh + 0.7), r4(-0.13)), TK, "right")
    ziel_r1 = pr1                                    # MoveTo setzt den Anker: rechtsbündig = rechte Kante
    schritt(s, EIN(shell + k_sh, 0.6))
    s.pause(0.4)
    schritt(s, EIN(d1 + [l_mit, s_teil], 0.6))
    schritt(s, EIN(m_s, 0.4))
    schritt(s, BETONE(s_teil, 0.8))
    schritt(s, ZEICHNE(a1, 0.7), WACHS(p1[0], 0.7), EIN([p1[1]] + k1, 0.7))
    schritt(s, EIN([c_r1, c_e1], 0.3))
    schritt(s, ZU(c_r1, ziel_r1[0], ziel_r1[1], 0.9), ZU(c_e1, r4(pe1[0] - tt_breite(TK, 1) / 2), pe1[1], 0.9))
    s.pause(0.8)
    schritt(s, EIN(d2 + [l_ohne], 0.6))
    schritt(s, ZEICHNE(a2, 0.7), WACHS(p2[0], 0.7), EIN([p2[1]] + k2, 0.7))
    schritt(s, EIN([c_r2, c_e2], 0.3))
    schritt(s, ZU(c_r2, ziel_r1[0], pr2[1], 0.9), ZU(c_e2, ziel_r1[0], pe2[1], 0.9))
    s.speichern()


def k7sgid():
    """Verzeichnisse ohne (rwxrwxr-x) und gemeinsam (rwxrwsr-x, s leuchtet), beide Gruppe student; anna legt in beiden
    an: links anna anna, rechts anna student mit Pfeil Gruppe Verzeichnis → Datei."""
    s = Szene("linux/k7sgid", reihenfolge="anlegen")
    xl, xr = -1.72, 1.72
    w_grp = ("Gruppe: student", "group: student", "grupo: student", "组：student", "groupe : student", "grup: student")
    an = [box(s, (0, 2.0), 2.3, 0.62, DUNKEL, WEISS, 2), tx(s, "anna", (0, 2.13), TT),
          L(s, "ha", ("Hauptgruppe: anna", "primary group: anna", "grupo principal: anna", "主组：anna", "groupe principal : anna",
                      "birincil grup: anna"), (0, 1.88), FM)]

    def verz(x, name, rechte, key):
        k = box(s, (x, 0.85), 2.4, 0.9, BLAU, BLAU_HELL, 2)
        n = tx(s, name, (x, 1.12), TT)
        g = s.raster([rechte], (x, 0.85), groesse=TT, ausrichtung="mitte")
        lg = L(s, key, w_grp, (x, 0.58), FM)
        return [k, n] + g.ids + [lg], g
    v1, g1 = verz(xl, "ohne/", "rwxrwxr-x", "g1")
    v2, g2 = verz(xr, "gemeinsam/", "rwxrwsr-x", "g2")
    m_s = g2.markieren(0, 5, 5, ORANGE, 0.4)
    s_t = g2.teil(0, 5, 5)

    def datei_(x, gruppe):
        k = box(s, (x, -0.65), 2.4, 0.62, DUNKEL, WEISS, 2, "rect")
        n = tx(s, "von_anna.txt", (x, -0.52), TT)
        g = s.raster(["anna " + gruppe], (x, -0.78), groesse=TT, ausrichtung="mitte")
        return [k, n] + g.ids, g
    f1, h1 = datei_(xl, "anna")
    f2, h2 = datei_(xr, "student")
    m1 = h1.markieren(0, 5, 8, ORANGE, 0.35)
    m2 = h2.markieren(0, 5, 11, BLAU, 0.25)
    pa = [pf(s, (-0.9, 1.68), (r4(xl + 0.3), 1.32), farbe=GRAU, dicke=2), pf(s, (0.9, 1.68), (r4(xr - 0.3), 1.32), farbe=GRAU,
                                                                           dicke=2)]
    pd = [pf(s, (x, 0.38), (x, -0.32), farbe=GRAU, dicke=2) for x in (xl, xr)]
    xw = r4(xr + 1.42)                               # Weg rechts außen: Verzeichnis-Gruppe → Gruppe der Datei
    pg = [linie(s, (r4(xr + 1.22), 0.58), (xw, 0.58), BLAU, 2.5), linie(s, (xw, 0.58), (xw, -0.78), BLAU, 2.5),
          pf(s, (xw, -0.78), (r4(h2.xr(11) + 0.08), -0.78), farbe=BLAU)]
    l1 = L(s, "von_anna", ("Gruppe von anna", "group from anna", "grupo de anna", "组来自 anna", "groupe d'anna",
                           "grup anna'dan"), (xl, -1.18), FM, "center", ORANGE)
    l2 = L(s, "von_verz", ("Gruppe vom Verzeichnis", "group from the directory", "grupo del directorio", "组来自目录",
                           "groupe du répertoire", "grup dizinden"), (xr, -1.18), FM, "center", BLAU)
    schritt(s, EIN(v1 + v2 + [s_t], 0.7))
    schritt(s, EIN(m_s, 0.4))
    schritt(s, BETONE(s_t, 0.8))
    s.pause(0.5)
    schritt(s, EIN(an, 0.6))
    schritt(s, ZEICHNE(pa, 0.6))
    schritt(s, ZEICHNE(pd, 0.5), WACHS(f1[0], 0.6), WACHS(f2[0], 0.6), EIN(f1[1:] + f2[1:], 0.6))
    s.pause(0.6)
    schritt(s, EIN([m1, l1], 0.6))
    s.pause(0.4)
    schritt(s, ZEICHNE(pg, 0.8), EIN([m2, l2], 0.8))
    s.speichern()


def k7sticky():
    """ablage (rwxrwxr-t, Besitzer student) mit von_student.txt und von_anna.txt: anna streicht ihren eigenen Eintrag
    (grün), den von student nicht (rot); student streicht den von anna (grün, Besitzer des Verzeichnisses)."""
    s = Szene("linux/k7sticky", reihenfolge="anlegen")
    x0, y0 = -3.3, 0.75
    bn, bb, rh = 1.85, 1.05, 0.32
    titel = tx(s, "ablage/", (x0, 1.62), TT, "left")
    g = s.raster(["rwxrwxr-t"], (r4(x0 + 0.85), 1.62), groesse=TT)
    m_t = g.markieren(0, 8, 8, ORANGE, 0.4)
    t_t = g.teil(0, 8, 8)
    l_b = L(s, "bes", ("Besitzer: student", "owner: student", "propietario: student", "所有者：student", "propriétaire : student",
                       "sahip: student"), (x0, 1.3), FM, "left")
    xn, xb = r4(x0 + bn / 2), r4(x0 + bn + bb / 2)
    kopf = [box(s, (xn, y0), bn, rh, GRAU, GRAU_HELL, 1.5, "rect"), box(s, (xb, y0), bb, rh, GRAU, GRAU_HELL, 1.5, "rect"),
            L(s, "n", ("Name", "name", "nombre", "名称", "nom", "ad"), (xn, y0), FM, "center", DUNKEL),
            L(s, "b", ("Besitzer", "owner", "propietario", "所有者", "propriétaire", "sahip"), (xb, y0), FM, "center", DUNKEL)]
    reihen, yr = [], []
    for i, (n, b) in enumerate((("von_student.txt", "student"), ("von_anna.txt", "anna"))):
        y = r4(y0 - (i + 1) * rh)
        yr.append(y)
        reihen += [box(s, (xn, y), bn, rh, GRAU, WEISS, 1.5, "rect"), box(s, (xb, y), bb, rh, GRAU, WEISS, 1.5, "rect"),
                   tx(s, n, (r4(x0 + 0.1), y), TK, "left"), tx(s, b, (xb, y), TK)]
    xr_ = r4(x0 + bn + bb)
    xa = 2.4
    anna = [box(s, (xa, 1.0), 1.2, 0.4, DUNKEL, WEISS, 2), tx(s, "anna", (xa, 1.0), TT)]
    stud = [box(s, (xa, -0.75), 1.2, 0.4, DUNKEL, WEISS, 2), tx(s, "student", (xa, -0.75), TT)]
    a1 = pf(s, (r4(xa - 0.62), 0.92), (r4(xr_ + 0.05), r4(yr[1] + 0.05)), farbe=GRUEN)
    a2 = pf(s, (r4(xa - 0.62), 1.08), (r4(xr_ + 0.05), yr[0]), farbe=ROT)
    a3 = pf(s, (r4(xa - 0.62), -0.67), (r4(xr_ + 0.05), r4(yr[1] - 0.05)), farbe=GRUEN)

    def auf(p, q, t=0.8):
        return r4(p[0] + (q[0] - p[0]) * t), r4(p[1] + (q[1] - p[1]) * t)
    h1 = haken(s, *auf((xa - 0.62, 0.92), (xr_, yr[1]), 0.62))
    k2 = kreuz(s, *auf((xa - 0.62, 1.08), (xr_, yr[0]), 0.62), 0.22)
    h3 = haken(s, *auf((xa - 0.62, -0.67), (xr_, yr[1]), 0.62))
    l3 = L(s, "verzb", ("Besitzer des Verzeichnisses", "owner of the directory", "propietario del directorio", "目录的所有者",
                        "propriétaire du répertoire", "dizinin sahibi"), (r4(xa - 0.3), -1.12), FM, "center", GRUEN)
    schritt(s, EIN([titel, l_b] + g.ids + [t_t] + kopf + reihen, 0.7))
    schritt(s, EIN(m_t, 0.4))
    schritt(s, BETONE(t_t, 0.8))
    s.pause(0.5)
    schritt(s, EIN(anna, 0.5))
    schritt(s, ZEICHNE(a1, 0.7))
    schritt(s, EIN(h1, 0.4))
    schritt(s, ZEICHNE(a2, 0.7))
    schritt(s, EIN(k2, 0.4))
    s.pause(0.6)
    schritt(s, EIN(stud, 0.5))
    schritt(s, ZEICHNE(a3, 0.7))
    schritt(s, EIN(h3 + [l3], 0.5))
    s.speichern()


def k7vierziffern():
    """Rechenbild 2775: die 2 zerfällt in die Bits 0 1 0 (SUID, SGID, Sticky; nur SGID), der Rest wird rwx rwx r-x; das
    SGID-Bit macht aus dem x der Gruppe ein s: rwxrwsr-x. Darunter 4755 und 1777."""
    s = Szene("linux/k7vierziffern", reihenfolge="anlegen")
    xd = (-2.2, -0.35, 0.85, 2.05)
    yd, yz = 1.85, 1.05
    ziff = []
    for x, z in zip(xd, "2775"):
        ziff += [box(s, (x, yd), 0.48, 0.48, DUNKEL, WEISS, 2, "rect"), tx(s, z, (x, yd), 26)]
    xb = (-2.85, -2.2, -1.55)
    bits = [tx(s, b, (x, yz), 24) for b, x in zip("010", xb)]
    namen = [text(s, n, (x, r4(yz - 0.3)), FM, "center", GRAU) for n, x in zip(("SUID", "SGID", "Sticky"), xb)]
    l_bits = [linie(s, (xd[0], r4(yd - 0.26)), (x, r4(yz + 0.16)), GRAU, 1.5) for x in xb]
    m_sg = box(s, (xb[1], r4(yz - 0.14)), 0.62, 0.62, ORANGE, ORANGE_HELL, 2.5, deckung=0.0)
    grp = [tx(s, t, (x, yz), 24) for t, x in zip(("rwx", "rwx", "r-x"), xd[1:])]
    l_grp = [linie(s, (x, r4(yd - 0.26)), (x, r4(yz + 0.16)), GRAU, 1.5) for x in xd[1:]]
    ye = 0.2
    erg = s.raster(["rwxrw r-x"], (0.85, ye), groesse=24, ausrichtung="mitte")
    xpos = erg.teil(0, 5, 5, text="x")
    ziele = [erg.xm(0, 2), erg.xm(3, 5), erg.xm(6, 8)]
    kop = [tx(s, t, (x, yz), 24) for t, x in zip(("rwx", "rwx", "r-x"), xd[1:])]
    k_bit = tx(s, "1", (xb[1], yz), 24, "center", ORANGE)
    l_erg = L(s, "erg", ("ls -l zeigt:", "ls -l shows:", "ls -l muestra:", "ls -l 显示：", "ls -l affiche :", "ls -l gösterir:"),
              (r4(erg.links - 0.2), ye), FM, "right", GRAU)
    unten = s.raster(["rwsr-xr-x", "rwxrwxrwt"], (0.3, -0.65), groesse=TT, zeilenabstand=1.8)
    nums = [tx(s, n, (-0.6, unten.y(i)), TT, "right") for i, n in enumerate(("4755", "1777"))]
    pfs = [pf(s, (-0.48, unten.y(i)), (0.2, unten.y(i)), farbe=GRAU, dicke=2, spitze=0.1) for i in range(2)]
    r_u = [unten.rahmen(0, 2, 2, ORANGE, 2.5), unten.rahmen(1, 8, 8, ORANGE, 2.5)]
    schritt(s, EIN(ziff, 0.6))
    s.pause(0.5)
    schritt(s, ZEICHNE(l_bits, 0.5), EIN(bits + namen, 0.6))
    schritt(s, ZEICHNE(m_sg, 0.6))
    schritt(s, BETONE(bits[1], 0.7))
    s.pause(0.4)
    schritt(s, ZEICHNE(l_grp, 0.5), EIN(grp, 0.6))
    s.pause(0.5)
    schritt(s, EIN(kop, 0.3))
    schritt(s, *[ZU(k, x, ye, 0.9) for k, x in zip(kop, ziele)], EIN(l_erg, 0.9))
    schritt(s, EIN(erg.ids + [xpos], 0.2), AUS(kop, 0.2))
    schritt(s, EIN(k_bit, 0.3))
    schritt(s, ZU(k_bit, erg.xm(5, 5), ye, 0.9))
    with s.gleichzeitig():
        s.ausblenden(k_bit, dauer=0.6)
        s.ersetzen(xpos, "s", farbe=ORANGE, dauer=0.6)
    s.pause(0.6)
    schritt(s, EIN(unten.ids + nums + pfs, 0.6))
    schritt(s, ZEICHNE(r_u, 0.5))
    s.speichern()


SZENEN = (k7passwd, k7gruppen, k7prozess, k7pruefwert, k7besitz, k7klassen, k7rwx, k7spalte, k7symbolisch, k7oktal,
          k7verzrechte, k7loeschen, k7pfad, k7entscheidung, k7oeffnen, k7sudo, k7sudoers, k7sudofalle, k7susudo, k7adduser,
          k7usermod, k7zweiquellen, k7umask, k7undnicht, k7suid, k7sgid, k7sticky, k7vierziffern)

if __name__ == "__main__":
    wahl = set(sys.argv[1:])
    for f in SZENEN:
        if not wahl or f.__name__ in wahl:
            f()
            print("gebaut:", f.__name__)
