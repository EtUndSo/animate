"""Linux und Kommandozeile, Kapitel 5 „Expansion, Quoting, Variablen und Umgebung“ (C:\\Bücher\\EtUndSo\\Linux\\Arbeitshefte\\
Kap5_Expansion.tex, kap5_stufen.tex, kap5_stufen_b.tex): 27 Abbildungen, alle animiert (notizen/animationen.md §5).

Szenenname linux/k5<name> = \\label{fig:k5<name>} im Heft (\\szenenabb{k5<name>}{…}{fig:k5<name>}); Liste in uebergabe_kap5.md,
Abschnitt „Prüfer (Phase 2a)“. Stil wie linux_teil3.py/linux_teil4.py, Helfer aus linux_hilfen.py. Neu gegenüber Kapitel 4:
schreibmaschine("text") (Terminalzeilen als s.text in Schreibmaschinenschrift, roh: $ { } ~ _ ohne Maskierung),
Szene(..., reihenfolge="anlegen") (was später angelegt wird, liegt oben: Kästen vor ihrem Inhalt anlegen), s.ersetzen für Texte
(nur für Texte, die nicht bewegt wurden: die Vorlage übernimmt die Lage beim Anlegen).
Bilder: Wortkasten = blau umrandetes Wort (ein Argument), Schublade = Shell-Variable (Etikett mit Namen, gelber Zettel mit Wert),
Prozess = blauer Kasten, Datei = weißes Rechteck. Koordinaten zwischen x = -3,45 und 3,45 (höchstens 548 px).
Bauen:  python tools/szenen/linux_teil5.py
Export: python tools/export_szenen.py <alle Namen aus SZENEN> --animiert
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from szenen_lib import *  # noqa: E402,F403

from linux_hilfen import *  # noqa: E402,F403  (gemeinsame Helfer der Linux-Kapitel)

schreibmaschine("text")
EM = 0.17                         # Höhe einer Terminalzeile (1 em) in Szeneneinheiten
setze_em(EM)
C = cw()                          # Breite eines Zeichens (0,08925)
E2 = 0.15                         # kleinere Terminalzeilen (Listen, Zettel)
E3 = 0.14


def r4(v):
    return round(v, 4)


def L(s, key, w, pos, g=FM, a="center", f=SCHWARZ, roh=None):
    """Beschriftung in sechs Sprachen; w = (de, en, es, zh, fr, tr)."""
    return text(s, T(s, key, *w), pos, g, a, f, roh=roh)


def box(s, mitte, b, h, rand=GRAU, fuellung=WEISS, dicke=2, form="round", dash="", deckung=1.0):
    return s.box("", (r4(mitte[0]), r4(mitte[1])), breite=r4(b), hoehe=r4(h), form=form, farbe=rand, fuellung=fuellung,
                 deckung=deckung, dicke=dicke, dash=dash)


def pbox(s, mitte, b, h):
    """Prozess: blauer Kasten (große Kästen eckig, damit Beschriftungen in den Ecken Platz haben)."""
    return box(s, mitte, b, h, BLAU, BLAU_HELL, 2.5, "round" if min(b, h) <= 0.9 else "rect")


def wb(w, em=None):
    """Breite eines Wortkastens."""
    return len(w) * cw(em) + 0.16


def wkasten(s, x, y, w, em=None, rand=BLAU, fuellung=BLAU_HELL):
    em = em or EM
    return box(s, (x, y), wb(w, em), em * 1.75, rand, fuellung, 2)


def wort(s, x, y, w, em=None, rand=BLAU, fuellung=BLAU_HELL, farbe=SCHWARZ):
    """Wortkasten (Mitte x, y): erst der Kasten, dann das Wort (Ergebnis [Kasten, Text])."""
    k = wkasten(s, x, y, w, em, rand, fuellung)
    return [k, tt(s, w, x, y, em or EM, farbe, "m")]


def mitten(x0, woerter, em=None, luecke=0.08):
    xs, x = [], x0
    for w in woerter:
        b = wb(w, em)
        xs.append(r4(x + b / 2))
        x += b + luecke
    return xs


def wortreihe(s, x0, y, woerter, em=None, **kw):
    return [wort(s, x, y, w, em, **kw) for x, w in zip(mitten(x0, woerter, em), woerter)]


def notiz_z(s, x, y, wert, em=None, farbe=SCHWARZ, breite=None):
    """Gelber Zettel mit einem Wert (Ergebnis [Kasten, Text])."""
    em = em or EM
    b = breite or len(wert) * cw(em) + 0.14
    return [box(s, (x, y), b, 0.28, GRAU, GELB, 1.5, "rect"), tt(s, wert, x, y, em, farbe, "m")]


def schublade(s, x, y, name, wert, em=None, anker="m", slot=None):
    """Shell-Variable als Schublade: grauer Kasten, weißes Etikett mit dem Namen, gelber Zettel mit dem Wert
    (wert=None: leerer, gestrichelter Platz für slot Zeichen). Ergebnis dict: k (Kasten, Etikett, Name), z (Zettel),
    zx (Mitte des Zettels), alle."""
    em = em or EM
    c = cw(em)
    bn = len(name) * c + 0.14
    nz = slot if slot is not None else (len(wert) if wert else 5)
    bw = nz * c + 0.14
    b = bn + bw + 0.2
    if anker == "l":
        x += b / 2
    x0 = x - b / 2
    k = box(s, (x, y), b, 0.4, GRAU, GRAU_HELL, 2, "rect")
    nx = x0 + 0.07 + bn / 2
    ek = box(s, (nx, y), bn, 0.28, GRAU, WEISS, 1.5, "rect")
    et = tt(s, name, nx, y, em, SCHWARZ, "m")
    zx = r4(x0 + 0.13 + bn + bw / 2)
    if wert is None:
        z = [box(s, (zx, y), bw, 0.28, HELLGRAU, WEISS, 1.5, "rect", DASH)]
    else:
        z = notiz_z(s, zx, y, wert, em, breite=bw)
    return {"k": [k, ek, et], "z": z, "zx": zx, "bw": bw, "b": b, "x": x, "alle": [k, ek, et] + z}


def stuecke(s, x0, y, teile, em=None):
    """Zeile aus farbigen Stücken [(text, farbe), …], Spalte für Spalte (Leerzeichen zählen mit). Ergebnis: Liste."""
    em = em or EM
    objs, col = [], 0
    for t, f in teile:
        if t.strip():
            objs.append(tt(s, t, sp(x0, col, em), y, em, f))
        col += len(t)
    return objs


W_SHELL = ("Shell", "shell", "shell", "Shell", "shell", "kabuk")
W_VERZ = ("Verzeichnis", "directory", "directorio", "目录", "répertoire", "dizin")
W_KIND = ("Kindprozess", "child process", "proceso hijo", "子进程", "processus enfant", "alt süreç")
W_KSHELL = ("Kind-Shell", "child shell", "shell hija", "子 shell", "shell enfant", "alt kabuk")
W_AUSG = ("Ausgabe:", "output:", "salida:", "输出：", "sortie :", "çıktı:")
W_GETIPPT = ("getippt:", "typed:", "escrito:", "输入：", "tapé :", "yazılan:")
W_UMG = ("Umgebung:", "environment:", "entorno:", "环境：", "environnement :", "ortam:")


# ================================================================== Abschnitt 1: Expansion, Muster, Klammern
def k5expansion():
    """ls *.txt: zwei Wörter; das Muster wird mit den Namen verglichen und durch die zwei Treffer ersetzt; erst dann startet
    ls mit diesen Argumenten."""
    s = Szene("linux/k5expansion", reihenfolge="anlegen")
    vb = box(s, (2.3, 0.45), 2.1, 2.3, form="rect")
    l_v = L(s, "verz", W_VERZ, (2.3, 1.38), FM, "center", GRAU)
    namen = (".einstellungen", "einkauf.txt", "foto1.jpg", "foto10.jpg", "foto2.jpg", "notiz.txt")
    ys = [r4(1.05 - 0.27 * i) for i in range(6)]
    mk = [mark(s, 1.35, 3.25, ys[i], 0.24, GRUEN, 0.3) for i in (1, 5)]
    nt = [tt(s, n, 1.45, y) for n, y in zip(namen, ys)]
    x0, y0, yw = -1.7, 1.35, 0.6
    l_get = L(s, "getippt", W_GETIPPT, (x0 - 0.15, y0), FM, "right", GRAU)
    zeile = tt(s, "ls *.txt", x0, y0)
    pk = pbox(s, (-1.55, -0.85), 3.6, 0.8)
    l_p = L(s, "proz", ("neuer Prozess ls, seine Argumente:", "new process ls, its arguments:", "nuevo proceso ls, sus argumentos:",
                        "新进程 ls，它的参数：", "nouveau processus ls, ses arguments :", "yeni süreç ls, argümanları:"),
            (-3.25, -0.6), FM, "left", BLAU)
    xr = {"ls": -2.4, "*.txt": -1.2, "einkauf.txt": -1.45, "notiz.txt": -0.25}
    xp = {"ls": -2.95, "einkauf.txt": -2.05, "notiz.txt": -0.85}
    yp = -0.95
    kb = {w: wkasten(s, xr[w], yw, w) for w in xr}
    t_ls = tt(s, "ls", x0, y0)
    t_m = tt(s, "*.txt", sp(x0, 3), y0)
    rh = rahmen(s, (xr["*.txt"], yw), wb("*.txt") + 0.14, 0.44)
    a_cmp = pf(s, (-0.62, yw), (1.2, yw), farbe=ORANGE, dash=DASH)
    l_cmp = L(s, "vergl", ("mit jedem Namen\nvergleichen", "compare with\nevery name", "comparar con\ncada nombre",
                           "与每个名称比较", "comparer à\nchaque nom", "her adla\nkarşılaştır"), (0.3, 0.98), FM, "center", ORANGE)
    t_e = tt(s, "einkauf.txt", 1.45, ys[1])
    t_n = tt(s, "notiz.txt", 1.45, ys[5])
    a_st = pf(s, (-1.55, 1.15), (-1.55, -0.42), farbe=DUNKEL)
    l_st = L(s, "start", ("Expansion,\ndann Start", "expansion,\nthen start", "expansión,\nluego inicio", "展开，\n然后启动",
                          "expansion,\npuis démarrage", "genişletme,\nsonra başlatma"), (-1.4, 0.35), FM, "left", DUNKEL)
    l_nie = L(s, "nie", ("Das Programm sieht das Muster nie.", "The program never sees the pattern.",
                         "El programa nunca ve el patrón.", "程序永远看不到模式。", "Le programme ne voit jamais le motif.",
                         "Program deseni hiç görmez."), (0.0, -1.55), FK, "center", ORANGE)
    schritt(s, EIN([l_get, zeile, t_ls, t_m], 0.6), WACHS(vb, 0.6), EIN([l_v] + nt, 0.6))
    s.pause(0.6)
    schritt(s, ZU(t_ls, xr["ls"], yw, 0.9), ZU(t_m, xr["*.txt"], yw, 0.9))
    schritt(s, WACHS([kb["ls"], kb["*.txt"]], 0.5))
    s.pause(0.6)
    schritt(s, EIN(rh, 0.5), ZEICHNE(a_cmp, 0.7), EIN(l_cmp, 0.7))
    schritt(s, EIN(mk, 0.6), BETONE([nt[1], nt[5]], 0.8))
    s.pause(0.6)
    schritt(s, AUS([kb["*.txt"], t_m, rh, a_cmp, l_cmp], 0.5), EIN([t_e, t_n], 0.3))
    schritt(s, ZU(t_e, xr["einkauf.txt"], yw, 1.0), ZU(t_n, xr["notiz.txt"], yw, 1.0))
    schritt(s, WACHS([kb["einkauf.txt"], kb["notiz.txt"]], 0.5))
    s.pause(0.6)
    schritt(s, WACHS(pk, 0.6), EIN(l_p, 0.6))
    teile = [ZEICHNE(a_st, 0.9), EIN(l_st, 0.9)]
    for w, t in (("ls", t_ls), ("einkauf.txt", t_e), ("notiz.txt", t_n)):
        teile += [ZU(kb[w], xp[w], yp, 1.0), ZU(t, xp[w], yp, 1.0)]
    schritt(s, *teile)
    schritt(s, EIN(l_nie, 0.6))
    s.speichern()


def k5versteckt():
    """Muster * und .* auf dieselben acht Namen (mit . und ..): links fünf Treffer, rechts einer; . und .. übersprungen."""
    s = Szene("linux/k5versteckt", reihenfolge="anlegen")
    namen = (".", "..", ".einstellungen", "einkauf.txt", "foto1.jpg", "foto10.jpg", "foto2.jpg", "notiz.txt")
    ys = [r4(0.95 - 0.27 * i) for i in range(8)]
    xl, xr = -3.0, 0.45
    mL = [mark(s, xl - 0.1, xl + 1.4, ys[i], 0.24, GRUEN, 0.3) for i in range(3, 8)]
    mR = mark(s, xr - 0.1, xr + 1.4, ys[2], 0.24, GRUEN, 0.3)
    gelb = [mark(s, xr - 0.1, xr + 0.3, ys[i], 0.24, ORANGE, 0.35) for i in (0, 1)]
    nL = [tt(s, n, xl, y, farbe=HELLGRAU if i < 2 else SCHWARZ) for i, (n, y) in enumerate(zip(namen, ys))]
    nR = [tt(s, n, xr, y, farbe=HELLGRAU if i < 2 else SCHWARZ) for i, (n, y) in enumerate(zip(namen, ys))]
    wm = ("Muster", "pattern", "patrón", "模式", "motif", "desen")
    hL = [L(s, "muster", wm, (xl + 0.6, 1.62), FM, "center", GRAU), tt(s, "*", xl + 0.6, 1.33, 0.24, ORANGE, "m")]
    hR = [L(s, "muster", wm, (xr + 0.6, 1.62), FM, "center", GRAU), tt(s, ".*", xr + 0.6, 1.33, 0.24, ORANGE, "m")]
    striche = [linie(s, (xr - 0.07, y), (xr + 0.26, y), ROT, 3) for y in ys[:2]]
    l_ueb = L(s, "ueb", ("übersprungen", "skipped", "omitidos", "被跳过", "ignorés", "atlanır"),
              (xr + 0.45, (ys[0] + ys[1]) / 2), FM, "left", ROT)
    rL = L(s, "t5", ("5 Treffer", "5 matches", "5 coincidencias", "5 个匹配", "5 correspondances", "5 eşleşme"),
           (xl + 0.6, -1.3), FK, "center", GRUEN)
    rR = L(s, "t1", ("1 Treffer", "1 match", "1 coincidencia", "1 个匹配", "1 correspondance", "1 eşleşme"),
           (xr + 0.6, -1.3), FK, "center", GRUEN)
    schritt(s, EIN(nL, 0.6))
    s.pause(0.6)
    schritt(s, EIN(hL, 0.5))
    with s.gleichzeitig():
        schritt(s, EIN(mL, 0.6))
        s.ersetzen(nL[2], namen[2], farbe=GRAU, dauer=0.6)
    schritt(s, EIN(rL, 0.5))
    s.pause(0.6)
    schritt(s, EIN(nR, 0.6))
    schritt(s, EIN(hR, 0.5))
    with s.gleichzeitig():
        schritt(s, EIN(mR, 0.6))
        for i in range(3, 8):
            s.ersetzen(nR[i], namen[i], farbe=GRAU, dauer=0.6)
    s.pause(0.4)
    schritt(s, EIN(gelb, 0.5))
    schritt(s, ZEICHNE(striche, 0.5), EIN(l_ueb, 0.5))
    schritt(s, AUS(gelb, 0.4), EIN(rR, 0.5))
    s.speichern()


def k5ohnetreffer():
    """rm *.bak: das Muster wird mit jedem Namen verglichen (✗), kein Treffer, das Wort bleibt; rm sucht eine Datei *.bak."""
    s = Szene("linux/k5ohnetreffer", reihenfolge="anlegen")
    x0, y0 = -3.3, 1.6
    zeile = tt(s, "rm *.bak", x0, y0)
    l_get = L(s, "getippt", ("getippt", "typed", "escrito", "输入", "tapé", "yazılan"), (x0 + 0.9, y0), FM, "left", GRAU)
    vb = box(s, (-2.5, 0.42), 1.7, 1.95, form="rect")
    l_v = L(s, "verz", W_VERZ, (-2.5, 1.27), FM, "center", GRAU)
    namen = (".einstellungen", "einkauf.txt", "foto1.jpg", "foto10.jpg", "foto2.jpg", "notiz.txt")
    ys = [r4(1.0 - 0.27 * i) for i in range(6)]
    nt = [tt(s, n, -3.2, y) for n, y in zip(namen, ys)]
    kreuze = [s.kreuzchen(None, -0.4, y, farbe=ROT, groesse=0.16, dicke=3) for y in ys]
    pk = pbox(s, (2.05, 0.35), 2.6, 1.2)
    l_pk = L(s, "rmbek", ("rm bekommt:", "rm receives:", "rm recibe:", "rm 收到：", "rm reçoit :", "rm şunları alır:"),
             (0.9, 0.75), FM, "left", BLAU)
    zellen = wortreihe(s, 0.95, 0.42, ("rm", "*.bak"))
    l_sucht = L(s, "sucht", ("sucht eine Datei\nnamens *.bak", "looks for a file\nnamed *.bak", "busca un archivo\nllamado *.bak",
                             "查找名为 *.bak\n的文件", "cherche un fichier\nnommé *.bak", "*.bak adlı bir\ndosya arar"),
                (2.05, 0.03), FM, "center", DUNKEL, roh=True)
    probe = wort(s, -1.05, ys[0], "*.bak", rand=ORANGE, fuellung=ORANGE_HELL)
    a = pf(s, (-0.2, ys[5]), (0.73, 0.1), farbe=DUNKEL)
    l_kein = L(s, "kein", ("kein Treffer: das Wort bleibt", "no match: the word stays", "ninguna coincidencia: la palabra queda",
                           "没有匹配：词保持不变", "aucune correspondance : le mot reste", "eşleşme yok: sözcük kalır"),
               (-3.3, -0.82), FM, "left", ORANGE)
    meld = tt(s, "rm: cannot remove '*.bak': No such file or directory", -3.3, -1.22, farbe=ROT)
    schritt(s, EIN([zeile, l_get], 0.6), WACHS(vb, 0.6), EIN([l_v] + nt, 0.6))
    s.pause(0.6)
    schritt(s, EIN(probe, 0.4))
    for i in range(6):
        schritt(s, EIN(kreuze[i], 0.25))
        if i < 5:
            schritt(s, *VERS(probe, 0, ys[i + 1] - ys[i], 0.3))
    s.pause(0.4)
    schritt(s, EIN(l_kein, 0.6), BETONE(probe, 0.8))
    s.pause(0.6)
    schritt(s, ZEICHNE(a, 0.6), WACHS(pk, 0.6), EIN(l_pk, 0.6))
    schritt(s, EIN(zellen, 0.6))
    schritt(s, EIN(l_sucht, 0.6))
    s.pause(0.4)
    schritt(s, EIN(meld, 0.7))
    s.speichern()


def k5klammer():
    """urlaub/{2025,2026}/{sommer,winter}: erst die erste Klammer (zwei Zeilen), dann in jeder die zweite (vier Wörter)."""
    s = Szene("linux/k5klammer", reihenfolge="anlegen")
    x0, y0 = -17 * C, 1.5
    top = stuecke(s, x0, y0, (("urlaub/", SCHWARZ), ("{2025,2026}", BLAU), ("/", SCHWARZ), ("{sommer,winter}", ORANGE)))
    y1 = 0.75
    xa, xb = -2.95, 0.55
    kmitte = msp(x0, 7, 17)
    k1 = [linie(s, (kmitte, 1.36), (xa + 13.5 * C, y1 + 0.13), BLAU, 2.5),
          linie(s, (kmitte, 1.36), (xb + 13.5 * C, y1 + 0.13), BLAU, 2.5)]
    L1 = [stuecke(s, x, y1, (("urlaub/", SCHWARZ), (j, BLAU), ("/", SCHWARZ), ("{sommer,winter}", ORANGE)))
          for x, j in ((xa, "2025"), (xb, "2026"))]
    ys = (0.05, -0.3)
    con, leaves, nums = [], [], []
    n = 0
    for x, j in ((xa, "2025"), (xb, "2026")):
        xv = x + 0.1
        con.append(linie(s, (xv, y1 - 0.12), (xv, ys[1]), ORANGE, 2))
        for y, w in zip(ys, ("sommer", "winter")):
            con.append(linie(s, (xv, y), (xv + 0.12, y), ORANGE, 2))
            leaves += stuecke(s, x + 0.25, y, (("urlaub/", SCHWARZ), (j, BLAU), ("/", SCHWARZ), (w, ORANGE)))
            n += 1
            nums.append(nummer(s, x + 0.25 + 18 * C + 0.25, y, n, GRAU, 0.11))
    l_z = L(s, "vier", ("2 · 2 = 4 Wörter, keine Datei nötig", "2 · 2 = 4 words, no file needed", "2 · 2 = 4 palabras, sin archivos",
                        "2 · 2 = 4 个词，无需任何文件", "2 · 2 = 4 mots, aucun fichier requis", "2 · 2 = 4 sözcük, dosya gerekmez"),
            (0.0, -0.8), FK, "center", DUNKEL)
    schritt(s, EIN(top, 0.6))
    s.pause(0.6)
    schritt(s, BETONE(top[1], 0.8))
    schritt(s, ZEICHNE(k1, 0.6), EIN(L1[0] + L1[1], 0.7))
    s.pause(0.6)
    schritt(s, BETONE([L1[0][3], L1[1][3]], 0.8))
    schritt(s, ZEICHNE(con, 0.6), EIN(leaves, 0.7))
    s.pause(0.6)
    for nm in nums:
        schritt(s, EIN(nm, 0.3))
    schritt(s, EIN(l_z, 0.6))
    s.speichern()


def k5pfadmuster():
    """urlaub/*/* Ebene für Ebene: urlaub wörtlich, erstes * trifft 2025, 2026, zweites * je sommer, winter; Ergebnis sortiert."""
    s = Szene("linux/k5pfadmuster", reihenfolge="anlegen")
    P = {"u": (0.0, 0.85), "a": (-1.55, 0.15), "b": (1.55, 0.15), "as": (-2.3, -0.55), "aw": (-0.8, -0.55),
         "bs": (0.8, -0.55), "bw": (2.3, -0.55)}
    N = {"u": "urlaub", "a": "2025", "b": "2026", "as": "sommer", "aw": "winter", "bs": "sommer", "bw": "winter"}
    V = {"a": "u", "b": "u", "as": "a", "aw": "a", "bs": "b", "bw": "b"}
    kanten = [kante(s, P[V[k]], P[k]) for k in V]
    K = {k: knoten(s, N[k], *P[k], b=kb(N[k])) for k in P}
    farben = {"u": ORANGE, "a": BLAU, "b": BLAU, "as": GRUEN, "aw": GRUEN, "bs": GRUEN, "bw": GRUEN}
    R = {k: rahmen(s, P[k], kb(N[k]) + 0.12, KH + 0.12, farben[k], 3) for k in P}
    e = 0.22
    xm = -3.3
    pat = stuecke(s, xm, 1.55, (("urlaub", ORANGE), ("/", DUNKEL), ("*", BLAU), ("/", DUNKEL), ("*", GRUEN)), e)
    leg = [L(s, "leg1", ("urlaub: kein Musterzeichen", "urlaub: no pattern character", "urlaub: sin carácter de patrón",
                         "urlaub：没有模式字符", "urlaub : aucun caractère de motif", "urlaub: desen karakteri yok"),
             (0.75, 1.62), FM, "left", ORANGE),
           L(s, "leg2", ("1. *: Namen in urlaub", "1st *: names in urlaub", "1.er *: nombres en urlaub", "第 1 个 *：urlaub 中的名称",
                         "1er * : noms dans urlaub", "1. *: urlaub içindeki adlar"), (0.75, 1.38), FM, "left", BLAU),
           L(s, "leg3", ("2. *: Namen in 2025 und 2026", "2nd *: names in 2025 and 2026", "2.º *: nombres en 2025 y 2026",
                         "第 2 个 *：2025 和 2026 中的名称", "2e * : noms dans 2025 et 2026", "2. *: 2025 ve 2026 içindeki adlar"),
             (0.75, 1.14), FM, "left", GRUEN)]
    l_erg = L(s, "erg", ("Ergebnis, sortiert:", "result, sorted:", "resultado, ordenado:", "结果（已排序）：", "résultat, trié :",
                         "sonuç, sıralı:"), (-3.3, -1.05), FM, "left", GRAU)
    erg = tt(s, "urlaub/2025/sommer urlaub/2025/winter urlaub/2026/sommer urlaub/2026/winter", -3.3, -1.35, E2)
    schritt(s, ZEICHNE(kanten, 0.7), WACHS([k[0] for k in K.values()], 0.7), EIN([k[1] for k in K.values()] + pat, 0.7))
    s.pause(0.6)
    schritt(s, BETONE(pat[0], 0.7), EIN([R["u"], leg[0]], 0.7))
    s.pause(0.5)
    schritt(s, BETONE(pat[2], 0.7), EIN([R["a"], R["b"], leg[1]], 0.7))
    s.pause(0.5)
    schritt(s, BETONE(pat[4], 0.7), EIN([R["as"], R["aw"], R["bs"], R["bw"], leg[2]], 0.7))
    s.pause(0.6)
    schritt(s, EIN([l_erg, erg], 0.7))
    s.speichern()


# ================================================================== Abschnitt 2: Variablen, Befehlsersetzung, Arithmetik
def k5variable():
    """Schublade wohnort: Zuweisung legt den Zettel Hamburg hinein; in echo Ich wohne in $wohnort wird der Zettel gelesen,
    die Zeile nach dem Einsetzen geht als Argumente an echo."""
    s = Szene("linux/k5variable", reihenfolge="anlegen")
    xa, ya = -3.3, 1.45
    z1 = tt(s, "wohnort=Hamburg", xa, ya)
    l_var = L(s, "var", ("Shell-Variable", "shell variable", "variable de shell", "Shell 变量", "variable de shell",
                         "kabuk değişkeni"), (-3.35, 0.95), FM, "left", GRAU)
    sb = schublade(s, -3.35, 0.6, "wohnort", None, anker="l", slot=7)
    yd = 0.6
    zt = notiz_z(s, msp(xa, 8, 14), ya, "Hamburg", breite=sb["bw"])
    x2, y2, y3 = -0.75, 1.3, 0.6
    l_get = L(s, "getippt", W_GETIPPT, (x2, 1.57), FM, "left", GRAU)
    l2 = [tt(s, "echo Ich wohne in", x2, y2), tt(s, "$wohnort", sp(x2, 18), y2)]
    xw = msp(x2, 18, 25)
    rh = rahmen(s, (xw, y2), 8 * C + 0.14, 0.3)
    l_nach = L(s, "nach", ("nach dem Einsetzen:", "after substitution:", "tras la sustitución:", "替换之后：", "après substitution :",
                           "yerine koymadan sonra:"), (x2, 0.87), FM, "left", GRAU)
    l3 = [tt(s, "echo Ich wohne in", x2, y3), tt(s, "Hamburg", sp(x2, 18), y3, farbe=GRUEN)]
    pk = pbox(s, (1.3, -0.55), 4.1, 0.85)
    l_pk = L(s, "pecho", ("neuer Prozess echo, Argumente:", "new process echo, arguments:", "nuevo proceso echo, argumentos:",
                          "新进程 echo，参数：", "nouveau processus echo, arguments :", "yeni süreç echo, argümanlar:"),
             (-0.65, -0.3), FM, "left", BLAU)
    zellen = wortreihe(s, -0.6, -0.67, ("echo", "Ich", "wohne", "in", "Hamburg"))
    a = pf(s, (1.0, 0.45), (1.0, -0.11), farbe=DUNKEL)
    l_st = L(s, "start", ("Start", "start", "inicio", "启动", "démarrage", "başlatma"), (1.12, 0.17), FM, "left", DUNKEL)
    z2 = notiz_z(s, sb["zx"], yd, "Hamburg", breite=sb["bw"])
    schritt(s, WACHS(sb["k"][0], 0.6), EIN(sb["k"][1:] + sb["z"] + [l_var], 0.6))
    s.pause(0.6)
    schritt(s, EIN(z1, 0.6))
    schritt(s, EIN(zt, 0.3))
    schritt(s, ZU(zt[0], sb["zx"], yd, 1.0), ZU(zt[1], sb["zx"], yd, 1.0))
    s.pause(0.6)
    schritt(s, EIN([l_get] + l2, 0.6))
    schritt(s, EIN(rh, 0.4), BETONE(l2[1], 0.7))
    schritt(s, EIN(z2, 0.3))
    schritt(s, ZU(z2[0], xw, y2, 0.9), ZU(z2[1], xw, y2, 0.9))
    schritt(s, AUS(z2 + [rh], 0.5), EIN([l_nach] + l3, 0.6))
    s.pause(0.6)
    schritt(s, WACHS(pk, 0.6), EIN(l_pk, 0.6), ZEICHNE(a, 0.6), EIN(l_st, 0.6))
    schritt(s, EIN(zellen, 0.7))
    s.speichern()


def k5zuweisung():
    """wohnort=Hamburg ist ein Wort (Zuweisung); wohnort = Hamburg sind drei Wörter: Befehl wohnort mit zwei Argumenten."""
    s = Szene("linux/k5zuweisung", reihenfolge="anlegen")
    x0, yo, yu = -3.3, 1.0, -0.15
    l_o = L(s, "ohne", ("ohne Leerzeichen", "without spaces", "sin espacios", "没有空格", "sans espaces", "boşluksuz"),
            (x0, yo + 0.4), FM, "left", GRAU)
    l_u = L(s, "mit", ("mit Leerzeichen", "with spaces", "con espacios", "有空格", "avec espaces", "boşluklu"),
            (x0, yu + 0.4), FM, "left", GRAU)
    k_o = box(s, (msp(x0, 0, 14), yo), 15 * C + 0.16, EM * 1.75, BLAU, BLAU_HELL)
    m_eq = mark(s, sp(x0, 7), sp(x0, 8), yo, 0.26, ORANGE, 0.45)
    t_o = tt(s, "wohnort=Hamburg", x0, yo)
    l_zw = L(s, "zuw", ("ein Wort mit =:\neine Zuweisung", "one word with =:\nan assignment", "una palabra con =:\nuna asignación",
                        "一个含 = 的词：\n赋值", "un mot avec = :\nune affectation", "= içeren tek sözcük:\nbir atama"),
             (-1.6, yo), FM, "left", GRUEN)
    ziele = ((-2.9, "wohnort"), (-2.2, "="), (-1.5, "Hamburg"))
    ku = [wkasten(s, x, yu, w) for x, w in ziele]
    tu = [tt(s, "wohnort", x0, yu), tt(s, "=", sp(x0, 8), yu), tt(s, "Hamburg", sp(x0, 10), yu)]
    cuts = [linie(s, (sp(x0, c) + C / 2, yu + 0.2), (sp(x0, c) + C / 2, yu - 0.2), ROT, 2.5, DASH) for c in (7, 9)]
    l_bef = L(s, "bef", ("Befehl", "command", "comando", "命令", "commande", "komut"), (-2.9, yu - 0.42), FM, "center", BLAU)
    kl = klammer(s, -2.35, -1.06, yu - 0.25, unten=False, farbe=BLAU, t=0.06, dicke=2)
    l_arg = L(s, "arg", ("Argumente", "arguments", "argumentos", "参数", "arguments", "argümanlar"), (-1.7, yu - 0.45), FX,
              "center", BLAU)
    meld = tt(s, "wohnort: command not found", -0.75, yu, farbe=ROT)
    l_ex = L(s, "exit", ("Exit-Status 127", "exit status 127", "estado de salida 127", "退出状态 127", "code de retour 127",
                         "çıkış durumu 127"), (-0.75, yu - 0.4), FM, "left", GRAU)
    schritt(s, EIN([l_o, t_o, l_u] + tu, 0.6))
    s.pause(0.6)
    schritt(s, WACHS(k_o, 0.6))
    schritt(s, EIN(m_eq, 0.5), EIN(l_zw, 0.6))
    s.pause(0.6)
    schritt(s, ZEICHNE(cuts, 0.5))
    schritt(s, AUS(cuts, 0.3), *[ZU(t, x, yu, 0.8) for t, (x, w) in zip(tu, ziele)])
    schritt(s, WACHS(ku, 0.5), EIN([l_bef, l_arg] + kl, 0.6))
    s.pause(0.6)
    schritt(s, EIN([meld, l_ex], 0.7))
    s.speichern()


def k5befehlsersetzung():
    """echo Angemeldet ist $(whoami): whoami läuft als eigener Prozess, seine Ausgabe student⏎ wird aufgefangen, das Zeilenende
    fällt weg, student wird Argument von echo."""
    s = Szene("linux/k5befehlsersetzung", reihenfolge="anlegen")
    x0, y0 = -3.3, 1.45
    xm = msp(x0, 20, 28)
    pke = pbox(s, (-1.5, -0.95), 3.8, 0.8)
    l_echo = L(s, "pecho", ("neuer Prozess echo, Argumente:", "new process echo, arguments:", "nuevo proceso echo, argumentos:",
                            "新进程 echo，参数：", "nouveau processus echo, arguments :", "yeni süreç echo, argümanlar:"),
               (-3.3, -0.7), FM, "left", BLAU)
    xs = mitten(-3.25, ("echo", "Angemeldet", "ist", "student"))
    zellen = [wort(s, x, -1.05, w) for x, w in zip(xs[:3], ("echo", "Angemeldet", "ist"))]
    k_st = wkasten(s, xs[3], -1.05, "student")
    zeile = [tt(s, "echo Angemeldet ist", x0, y0), tt(s, "$(whoami)", sp(x0, 20), y0)]
    rh = rahmen(s, (xm, y0), 9 * C + 0.14, 0.3)
    a1 = pf(s, (xm, 1.28), (xm, 0.75), farbe=ORANGE)
    l_eig = L(s, "eig", ("eigener Prozess", "separate process", "proceso propio", "独立进程", "processus à part", "ayrı süreç"),
              (xm + 0.12, 1.02), FM, "left", ORANGE)
    gh = geist(s, (xm, 0.5), 1.25, 0.45)
    t_wg = tt(s, "whoami", xm, 0.5, farbe=HELLGRAU, anker="m")
    l_end = L(s, "beendet", ("beendet", "ended", "terminado", "已结束", "terminé", "sona erdi"), (xm, 0.15), FM, "center", GRAU)
    pkw = pbox(s, (xm, 0.5), 1.25, 0.45)
    t_w = tt(s, "whoami", xm, 0.5, anker="m")
    fang = box(s, (1.85, 0.5), 1.6, 0.5, GRAU, WEISS, 2, "round", DASH)
    l_fang = L(s, "fang", ("aufgefangene Ausgabe", "captured output", "salida capturada", "捕获的输出", "sortie capturée",
                           "yakalanan çıktı"), (1.85, 0.9), FM, "center", GRAU)
    a2 = pf(s, (xm + 0.65, 0.5), (1.03, 0.5), farbe=GRUEN)
    l_nl = L(s, "nl", ("Zeilenende am Schluss\nfällt weg", "line end at the end\nis removed", "el fin de línea final\nse elimina",
                       "末尾的换行符\n被删除", "la fin de ligne finale\nest supprimée", "sondaki satır sonu\nkaldırılır"),
             (1.85, -0.02), FM, "center", ORANGE)
    a3 = pf(s, (-3.0, 1.28), (-3.0, -0.53), farbe=DUNKEL)
    l_st = L(s, "erst", ("erst dann\nStart", "only then\nstart", "solo entonces\ninicio", "然后才\n启动", "seulement alors\ndémarrage",
                         "ancak sonra\nbaşlatma"), (-2.88, 0.45), FM, "left", DUNKEL)
    st = tt(s, "student", xm + 0.75, 0.5, anker="m")
    nl = zeilenende(s, xm + 0.75 + 0.42, 0.5)
    st2 = tt(s, "student", 1.65, 0.5, farbe=GRUEN, anker="m")
    schritt(s, EIN(zeile, 0.6))
    s.pause(0.6)
    schritt(s, EIN(rh, 0.5), ZEICHNE(a1, 0.6), EIN(l_eig, 0.6))
    schritt(s, WACHS(pkw, 0.6), EIN(t_w, 0.6))
    s.pause(0.6)
    schritt(s, ZEICHNE(a2, 0.5), WACHS(fang, 0.5), EIN(l_fang, 0.5))
    schritt(s, EIN([st, nl], 0.3))
    schritt(s, ZU(st, 1.65, 0.5, 0.9), ZU(nl, 2.25, 0.5, 0.9))
    s.pause(0.6)
    schritt(s, BETONE(nl, 0.6))
    schritt(s, AUS(nl, 0.5), EIN(l_nl, 0.5))
    s.pause(0.6)
    schritt(s, AUS([pkw, t_w], 0.5), EIN([gh, t_wg, l_end], 0.5))
    schritt(s, ZEICHNE(a3, 0.7), EIN(l_st, 0.6), WACHS(pke, 0.6), EIN([l_echo] + zellen, 0.6))
    schritt(s, EIN(st2, 0.3))
    schritt(s, ZU(st2, xs[3], -1.05, 0.9), WACHS(k_st, 0.6))
    s.speichern()


def k5rechnung():
    """Rechenbild: 3·45 + 2·119 = 373 Cent; 373 / 100 = 3 Euro, 373 % 100 = 73 Cent; Probe."""
    s = Szene("linux/k5rechnung", reihenfolge="anlegen")
    tex = (r"\begin{aligned}"
           r"3 \cdot 45 + 2 \cdot 119 &= 135 + 238 = 373\\"
           r"\mathtt{373\ /\ 100} &= 3\\"
           r"\mathtt{373\ \%\ 100} &= 73\\[4pt]"
           r"3 \cdot 100 + 73 &= 373"
           r"\end{aligned}")
    s.formel(tex, mitte=(-1.05, 0.0), hoehe=1.3, zeilenweise=True, dauer=4.8)
    xa = 1.15
    labs = [L(s, "cent", ("Cent", "cents", "céntimos", "分", "centimes", "sent"), (xa, 0.5), FM, "left", GRAU),
            L(s, "euro", ("Euro: ganzzahlig geteilt", "euros: whole-number division", "euros: división entera", "欧元：整数除法",
                          "euros : division entière", "avro: tam sayı bölmesi"), (xa, 0.16), FM, "left", GRAU),
            L(s, "rest", ("Cent: der Rest", "cents: the remainder", "céntimos: el resto", "分：余数", "centimes : le reste",
                          "sent: kalan"), (xa, -0.17), FM, "left", GRAU),
            L(s, "probe", ("Probe", "check", "comprobación", "验算", "vérification", "sağlama"), (xa, -0.53), FM, "left", GRUEN)]
    s.pause(0.6)
    for lb in labs:
        schritt(s, EIN(lb, 0.4))
    s.speichern()


# ================================================================== Abschnitt 3: Worttrennung und Quoting
def k5printf():
    """printf "[%s]\\n" eins zwei: die Vorlage wird einmal je Argument angewandt; je Durchgang eine Zeile."""
    s = Szene("linux/k5printf", reihenfolge="anlegen")
    zeile = tt(s, 'printf "[%s]\\n" eins zwei', -3.3, 1.55)
    yv = 0.9
    vk = box(s, (-2.35, yv), 1.05, 0.38, ORANGE, ORANGE_HELL, 2, "round", DASH)
    vt = tt(s, "[%s]\\n", -2.35, yv, anker="m")
    l_vorl = L(s, "vorlage", ("Vorlage", "format", "plantilla", "格式模板", "modèle", "şablon"), (-3.0, yv), FM, "right", ORANGE)
    args = [wort(s, -0.1, yv, "eins"), wort(s, 0.9, yv, "zwei")]
    l_args = L(s, "args", ("übrige Argumente", "remaining arguments", "argumentos restantes", "其余参数", "arguments restants",
                           "kalan argümanlar"), (1.45, yv), FM, "left", GRAU)
    term = term_kasten(s, (1.2, -0.15), 1.6, 0.95)
    l_aus = L(s, "aus", W_AUSG, (1.2, 0.47), FM, "center", GRAU)
    rows = (0.15, -0.45)
    ds = [L(s, "d%d" % (i + 1), ("Durchgang %d" % (i + 1), "pass %d" % (i + 1), "pasada %d" % (i + 1), "第 %d 遍" % (i + 1),
                                  "passage %d" % (i + 1), "%d. geçiş" % (i + 1)), (-3.35, y), FM, "left", GRAU)
          for i, y in enumerate(rows)]
    ck = [box(s, (-1.85, y), 1.05, 0.38, ORANGE, ORANGE_HELL, 2, "round", DASH) for y in rows]
    ct = [tt(s, "[%s]\\n", -1.85, y, anker="m") for y in rows]
    ar = [pf(s, (-1.3, y), (0.38, y), farbe=GRUEN) for y in rows]
    out = [tt(s, "[eins]", 0.6, rows[0]), tt(s, "[zwei]", 0.6, rows[1])]
    l_rest = L(s, "rest", ("noch ein Argument übrig: Vorlage noch einmal", "one argument left: the format again",
                           "queda un argumento: otra vez la plantilla", "还剩一个参数：再用一次模板",
                           "il reste un argument : encore le modèle", "bir argüman kaldı: şablon yeniden"),
                (-3.35, -0.15), FM, "left", ORANGE)
    l_jede = L(s, "jede", ("eine Zeile je Argument", "one line per argument", "una línea por argumento", "每个参数一行",
                           "une ligne par argument", "argüman başına bir satır"), (1.2, -0.85), FM, "center", GRUEN)
    fl = [[box(s, (x, yv), wb(w), EM * 1.75, BLAU, BLAU_HELL, 2), tt(s, w, x, yv, anker="m")]
          for x, w in ((-0.1, "eins"), (0.9, "zwei"))]
    schritt(s, EIN(zeile, 0.6))
    s.pause(0.6)
    schritt(s, WACHS(vk, 0.5), EIN([vt, l_vorl], 0.5))
    schritt(s, EIN(args + [l_args], 0.6))
    schritt(s, WACHS(term, 0.5), EIN(l_aus, 0.5))
    s.pause(0.6)
    for i, w in enumerate(("eins", "zwei")):
        if i == 1:
            schritt(s, EIN(l_rest, 0.5))
        schritt(s, EIN(ds[i], 0.4), WACHS(ck[i], 0.5), EIN(ct[i], 0.5))
        schritt(s, EIN(fl[i], 0.2))
        schritt(s, ZU(fl[i][0], -1.85, rows[i], 0.8), ZU(fl[i][1], -1.85, rows[i], 0.8))
        with s.gleichzeitig():
            schritt(s, AUS(fl[i], 0.5))
            s.ersetzen(ct[i], "[%s]\\n" % w, dauer=0.6)
        schritt(s, ZEICHNE(ar[i], 0.6), EIN(out[i], 0.6))
        s.pause(0.4)
    schritt(s, AUS(l_rest, 0.4), EIN(l_jede, 0.6))
    s.speichern()


def k5worttrennung():
    """ls $datei: der Wert wird als ein Wort eingesetzt und dann am Leerzeichen zerlegt (zwei Argumente);
    ls "$datei": der Schnitt prallt an den Anführungszeichen ab (ein Argument)."""
    s = Szene("linux/k5worttrennung", reihenfolge="anlegen")
    sb = schublade(s, -3.35, 1.55, "datei", "mein bericht.txt", anker="l")
    wert = "mein bericht.txt"
    xv0 = -1.05 - 8 * C
    xcut = sp(xv0, 4) + C / 2
    W_PE = ("Parametererweiterung", "parameter expansion", "expansión de parámetros", "参数扩展", "développement de paramètre",
            "parametre genişletmesi")

    def reihe(y, getippt, quote):
        typ = [tt(s, getippt[:3], -3.3, y), tt(s, getippt[3:], sp(-3.3, 3), y)]
        a = pf(s, (-3.3 + len(getippt) * C + 0.1, y), (-2.08, y), farbe=DUNKEL)
        vk = wkasten(s, -1.05, y, wert)
        ul = linie(s, (sp(xv0, 4) + 0.015, y - 0.12), (sp(xv0, 5) - 0.015, y - 0.12), ORANGE, 3)
        lpe = L(s, "pe", W_PE, (-1.05, y + 0.3), FM, "center", GRAU)
        q = [tt(s, '"', -1.05 - wb(wert) / 2 - 0.07, y, farbe=ORANGE, anker="m"),
             tt(s, '"', -1.05 + wb(wert) / 2 + 0.07, y, farbe=ORANGE, anker="m")] if quote else []
        return typ, a, vk, ul, lpe, q

    y1, y2 = 0.7, -0.75
    typ1, a1, vk1, ul1, lpe1, _ = reihe(y1, "ls $datei", False)
    km = [wkasten(s, -1.6, y1, "mein"), wkasten(s, -0.45, y1, "bericht.txt")]
    v1 = [tt(s, "mein", xv0, y1), tt(s, "bericht.txt", sp(xv0, 5), y1)]
    cut1 = linie(s, (xcut, y1 + 0.24), (xcut, y1 - 0.24), ROT, 2.5, DASH)
    l_wt = L(s, "wt", ("Worttrennung", "word splitting", "división en palabras", "分词", "découpage en mots", "sözcük bölme"),
             (-1.05, y1 - 0.33), FM, "center", ROT)
    r1 = [L(s, "zwei", ("ls bekommt 2 Argumente", "ls receives 2 arguments", "ls recibe 2 argumentos", "ls 得到 2 个参数",
                        "ls reçoit 2 arguments", "ls 2 argüman alır"), (0.35, y1 + 0.13), FM, "left", DUNKEL),
          L(s, "kein", ("keins davon gibt es", "neither of them exists", "ninguno de los dos existe", "两个都不存在", "aucun n'existe",
                        "hiçbiri yok"), (0.35, y1 - 0.13), FM, "left", ROT)]
    typ2, a2, vk2, ul2, lpe2, q2 = reihe(y2, 'ls "$datei"', True)
    v2 = tt(s, wert, xv0, y2)
    cut2 = linie(s, (xcut, y2 + 0.24), (xcut, y2 - 0.24), ROT, 2.5, DASH)
    l_kwt = L(s, "kwt", ("keine Worttrennung", "no word splitting", "sin división en palabras", "不分词", "pas de découpage",
                         "sözcük bölme yok"), (-1.05, y2 - 0.33), FM, "center", GRUEN)
    hk = haken(s, 0.47, y2)
    r2 = L(s, "eins", ("ls bekommt 1 Argument", "ls receives 1 argument", "ls recibe 1 argumento", "ls 得到 1 个参数",
                       "ls reçoit 1 argument", "ls 1 argüman alır"), (0.7, y2), FM, "left", GRUEN)
    zk = notiz_z(s, sb["zx"], 1.55, wert, breite=sb["bw"])
    schritt(s, WACHS(sb["k"][0], 0.6), EIN(sb["k"][1:] + sb["z"], 0.6))
    s.pause(0.6)
    schritt(s, EIN(typ1, 0.5))
    schritt(s, BETONE(typ1[1], 0.6))
    schritt(s, ZEICHNE(a1, 0.5), WACHS(vk1, 0.5), EIN(v1 + [ul1, lpe1], 0.5))
    s.pause(0.6)
    schritt(s, ZEICHNE(cut1, 0.5), EIN(l_wt, 0.5))
    schritt(s, AUS([vk1, cut1, ul1], 0.4), ZU(v1[0], -1.6, y1, 0.8), ZU(v1[1], -0.45, y1, 0.8), WACHS(km, 0.8))
    schritt(s, EIN(r1, 0.6))
    s.pause(0.6)
    schritt(s, EIN(typ2, 0.5))
    schritt(s, EIN(zk, 0.2))
    schritt(s, ZU(zk[0], -1.05, y2, 0.8), ZU(zk[1], -1.05, y2, 0.8), ZEICHNE(a2, 0.5))
    schritt(s, AUS(zk, 0.4), WACHS(vk2, 0.4), EIN([v2, ul2, lpe2] + q2, 0.5))
    schritt(s, ZEICHNE(cut2, 0.4))
    schritt(s, VER(cut2, 0, 0.3, 0.4))
    schritt(s, AUS(cut2, 0.3), EIN(l_kwt, 0.5))
    schritt(s, EIN(hk + [r2], 0.6))
    s.speichern()


def k5entfernen():
    """"mein "'bericht'.txt: drei Stücke; die vier Anführungszeichen fallen weg, die Stücke rücken zu einem Argument zusammen."""
    s = Szene("linux/k5entfernen", reihenfolge="anlegen")
    e = 0.22
    c = cw(e)
    x0, y0 = -10 * c, 1.0
    marken = [mark(s, sp(x0, a, e), sp(x0, b, e), y0, 0.34, f, 0.18) for a, b, f in ((0, 7, BLAU), (7, 16, GRUEN), (16, 20, GRAU))]
    stk = (('"', 0, SCHWARZ), ("mein", 1, BLAU), ('"', 6, SCHWARZ), ("'", 7, SCHWARZ), ("bericht", 8, GRUEN), ("'", 15, SCHWARZ),
           (".txt", 16, SCHWARZ))
    top = [tt(s, t, sp(x0, col, e), y0, e, f) for t, col, f in stk]
    l_get = L(s, "getippt", W_GETIPPT, (x0 - 0.15, y0), FM, "right", GRAU)
    kl = (klammer(s, sp(x0, 0, e) + 0.03, sp(x0, 7, e) - 0.03, y0 - 0.22, unten=False, farbe=BLAU, t=0.06, dicke=2) +
          klammer(s, sp(x0, 7, e) + 0.03, sp(x0, 16, e) - 0.03, y0 - 0.22, unten=False, farbe=GRUEN, t=0.06, dicke=2) +
          klammer(s, sp(x0, 16, e) + 0.03, sp(x0, 20, e) - 0.03, y0 - 0.22, unten=False, farbe=GRAU, t=0.06, dicke=2))
    labs = [tt(s, '"..."', msp(x0, 0, 6, e), y0 - 0.45, farbe=BLAU, anker="m"),
            tt(s, "'...'", msp(x0, 7, 15, e), y0 - 0.45, farbe=GRUEN, anker="m"),
            L(s, "ohne", ("ohne", "none", "sin comillas", "无", "sans", "tırnaksız"), (msp(x0, 16, 19, e), y0 - 0.45), FM, "center", GRAU)]
    yb = -0.4
    x1 = -8 * c
    ak = box(s, (0, yb), 16 * c + 0.22, 0.42, BLAU, BLAU_HELL, 2)
    l_ent = L(s, "entf", ("Entfernen der Anführungszeichen", "quote removal", "eliminación de comillas", "删除引号",
                          "suppression des guillemets", "tırnak işaretlerinin kaldırılması"), (0, 0.13), FM, "center", ORANGE)
    l_arg = L(s, "arg", ("ein Argument", "one argument", "un argumento", "一个参数", "un argument", "tek argüman"),
              (0, yb - 0.42), FM, "center", BLAU)
    kop = [tt(s, t, sp(x0, col, e), y0, e, ORANGE if t in ('"', "'") else f) for t, col, f in stk]
    quotes = [kop[i] for i in (0, 2, 3, 5)]
    inhalt = {1: (0, 4), 4: (5, 7), 6: (12, 4)}
    dy = yb - y0
    schritt(s, EIN(top + [l_get], 0.6))
    schritt(s, EIN(marken, 0.5))
    schritt(s, EIN(kl + labs, 0.6))
    s.pause(0.6)
    schritt(s, EIN(kop, 0.2))
    schritt(s, *VERS(kop, 0, dy, 0.9))
    s.pause(0.4)
    schritt(s, BETONE(quotes, 0.7))
    schritt(s, AUS(quotes, 0.5), EIN(l_ent, 0.5))
    schritt(s, *[ZU(kop[i], sp(x1, col, e) + n / 2 * c, yb, 0.9) for i, (col, n) in inhalt.items()])
    schritt(s, WACHS(ak, 0.5), EIN(l_arg, 0.5))
    s.speichern()


def k5datensteuerung():
    """rm $datei: die zwei Argumente mein und bericht.txt treffen zwei andere Dateien; die gemeinte bleibt liegen."""
    s = Szene("linux/k5datensteuerung", reihenfolge="anlegen")
    zeile = tt(s, "rm $datei", -3.3, 1.6)
    sb = schublade(s, -3.35, 1.15, "datei", "mein bericht.txt", anker="l")
    pk = pbox(s, (-1.75, 0.45), 3.25, 0.7)
    l_pk = L(s, "rmbek", ("rm bekommt:", "rm receives:", "rm recibe:", "rm 收到：", "rm reçoit :", "rm şunları alır:"),
             (-3.25, 0.66), FM, "left", BLAU)
    xs = mitten(-3.25, ("rm", "mein", "bericht.txt"))
    zellen = wortreihe(s, -3.25, 0.38, ("rm", "mein", "bericht.txt"))
    l_v = L(s, "verz", W_VERZ, (1.85, 1.6), FM, "center", GRAU)
    eintraege = ("bericht.txt", "einkauf.txt", "foto1.jpg", "foto10.jpg", "foto2.jpg", "mein", "mein bericht.txt", "notiz.txt",
                 "urlaub")
    ys = [r4(1.3 - 0.27 * i) for i in range(9)]
    m6 = mark(s, 0.55, 0.88 + 16 * C + 0.08, ys[6], 0.24, GRUEN, 0.3)
    sym = [ordner_symbol(s, 0.7, y) if n == "urlaub" else datei_symbol(s, 0.7, y) for n, y in zip(eintraege, ys)]
    nt = [tt(s, n, 0.88, y) for n, y in zip(eintraege, ys)]
    a1 = pf(s, (xs[2] + wb("bericht.txt") / 2 + 0.02, 0.38), (0.55, ys[0]), farbe=ROT)
    a2 = pf(s, (xs[1], 0.23), (0.55, ys[5]), knick="vh", farbe=ROT)
    striche = [linie(s, (0.58, ys[i]), (0.88 + len(eintraege[i]) * C + 0.05, ys[i]), ROT, 3) for i in (0, 5)]
    W_DEL = ("gelöscht", "deleted", "borrado", "已删除", "supprimé", "silindi")
    l_del = [L(s, "del", W_DEL, (2.1, ys[i]), FM, "left", ROT) for i in (0, 5)]
    l_gem = L(s, "gem", ("gemeint", "intended", "la deseada", "本意", "visé", "hedeflenen"), (2.5, ys[6]), FM, "left", GRUEN)
    schritt(s, EIN([zeile] + sb["alle"], 0.6), WACHS(pk, 0.6), EIN([l_pk] + zellen, 0.6))
    schritt(s, EIN([l_v] + sym + nt, 0.6))
    s.pause(0.6)
    schritt(s, ZEICHNE([a1, a2], 0.8))
    schritt(s, BETONE([nt[0], nt[5]], 0.7))
    with s.gleichzeitig():
        schritt(s, ZEICHNE(striche, 0.5), EIN(l_del, 0.5), AUS([sym[0], sym[5]], 0.5))
        for i in (0, 5):
            s.ersetzen(nt[i], eintraege[i], farbe=HELLGRAU, dauer=0.5)
    s.pause(0.6)
    schritt(s, EIN([m6, l_gem], 0.6))
    s.speichern()


def k5werkstatt():
    """Die Werkstatt: ls -l {foto,notiz}* "$HOME" läuft durch die sechs Schritte; Ergebnis die Argumentliste von ls."""
    s = Szene("linux/k5werkstatt", reihenfolge="anlegen")
    x0 = -3.3
    st = [("st0", ("getippt", "typed", "escrito", "输入", "tapé", "yazılan")),
          ("st1", ("1  Zerlegen in Wörter", "1  split into words", "1  dividir en palabras", "1  拆分为词", "1  découpage en mots",
                   "1  sözcüklere ayırma")),
          ("st2", ("2  Klammererweiterung", "2  brace expansion", "2  expansión de llaves", "2  花括号扩展",
                   "2  développement des accolades", "2  küme parantezi genişletmesi")),
          ("st3", ("3  Tilde-, Parametererweiterung, Arithmetik, Befehlsersetzung",
                   "3  tilde and parameter expansion, arithmetic, command substitution",
                   "3  expansión de tilde y de parámetros, aritmética, sustitución de órdenes", "3  波浪号扩展、参数扩展、算术、命令替换",
                   "3  développement du tilde et des paramètres, arithmétique, substitution de commande",
                   "3  tilde ve parametre genişletmesi, aritmetik, komut ikamesi")),
          ("st4", ("4  Worttrennung: ändert hier nichts", "4  word splitting: changes nothing here",
                   "4  división en palabras: aquí no cambia nada", "4  分词：这里没有变化", "4  découpage en mots : rien ne change ici",
                   "4  sözcük bölme: burada hiçbir şey değişmez")),
          ("st5", ("5  Pfadnamen-Erweiterung", "5  pathname expansion", "5  expansión de nombres de ruta", "5  路径名扩展",
                   "5  développement des chemins", "5  yol adı genişletmesi")),
          ("st6", ("6  Entfernen der Anführungszeichen", "6  quote removal", "6  eliminación de comillas", "6  删除引号",
                   "6  suppression des guillemets", "6  tırnak işaretlerinin kaldırılması")),
          ("st7", ("Start: ls bekommt diese sechs Argumente", "start: ls receives these six arguments",
                   "inicio: ls recibe estos seis argumentos", "启动：ls 得到这六个参数", "démarrage : ls reçoit ces six arguments",
                   "başlatma: ls bu altı argümanı alır"))]
    ly = (1.8, 1.25, 0.7, 0.15, -0.4, -0.7, -1.25, -1.9)
    zy = {0: 1.55, 1: 1.0, 2: 0.45, 3: -0.1, 5: -0.95, 6: -1.5}
    labs = [L(s, k, w, (x0, y), FM, "left", GRAU if i == 0 else DUNKEL) for i, ((k, w), y) in enumerate(zip(st[:7], ly[:7]))]
    labs.append(L(s, st[7][0], st[7][1], (x0, ly[7]), FM, "left", GRUEN))
    z0 = tt(s, 'ls -l {foto,notiz}* "$HOME"', x0, zy[0])
    z1 = tt(s, 'ls -l {foto,notiz}* "$HOME"', x0, zy[1])
    u1 = [linie(s, (sp(x0, a) + 0.01, zy[1] - 0.13), (sp(x0, b + 1) - 0.01, zy[1] - 0.13), BLAU, 2.5)
          for a, b in ((0, 1), (3, 4), (6, 18), (20, 26))]
    z2 = stuecke(s, x0, zy[2], (("ls -l ", SCHWARZ), ("foto* notiz*", BLAU), (' "$HOME"', SCHWARZ)))
    z3 = stuecke(s, x0, zy[3], (('ls -l foto* notiz* "', SCHWARZ), ("/home/student", BLAU), ('"', SCHWARZ)))
    z5 = stuecke(s, x0, zy[5], (("ls -l ", SCHWARZ), ("foto1.jpg foto10.jpg foto2.jpg notiz.txt", BLAU),
                                (' "/home/student"', SCHWARZ)))
    z6 = tt(s, "ls -l foto1.jpg foto10.jpg foto2.jpg notiz.txt /home/student", x0, zy[6])
    u6 = [linie(s, (sp(x0, a) + 0.01, zy[6] - 0.13), (sp(x0, b + 1) - 0.01, zy[6] - 0.13), GRUEN, 2.5)
          for a, b in ((0, 1), (3, 4), (6, 14), (16, 25), (27, 35), (37, 45), (47, 59))]
    schritt(s, EIN([labs[0], z0], 0.6))
    s.pause(0.6)
    schritt(s, EIN([labs[1], z1], 0.6))
    schritt(s, ZEICHNE(u1, 0.6))
    s.pause(0.3)
    schritt(s, EIN([labs[2]] + z2, 0.6))
    schritt(s, BETONE(z2[1], 0.6))
    s.pause(0.3)
    schritt(s, EIN([labs[3]] + z3, 0.6))
    schritt(s, BETONE(z3[1], 0.6))
    s.pause(0.3)
    schritt(s, EIN(labs[4], 0.6))
    s.pause(0.3)
    schritt(s, EIN([labs[5]] + z5, 0.6))
    schritt(s, BETONE(z5[1], 0.6))
    s.pause(0.3)
    schritt(s, EIN([labs[6], z6], 0.6))
    s.pause(0.3)
    schritt(s, ZEICHNE(u6, 0.6), EIN(labs[7], 0.6))
    s.speichern()


# ================================================================== Abschnitt 4: Umgebung und Vererbung
def k5kind():
    """obst=Apfel in der Shell; bash -c '…' gibt den Text unverändert weiter (Kind findet nichts), bash -c "…" setzt den Wert
    vorher ein (Kind bekommt Apfel)."""
    s = Szene("linux/k5kind", reihenfolge="anlegen")
    sh = pbox(s, (-2.62, -0.05), 1.6, 2.9)
    l_sh = L(s, "shell", W_SHELL, (-2.62, 1.15), FM, "center", BLAU)
    sb = schublade(s, -2.62, 0.0, "obst", "Apfel")
    xc = -1.65
    l_h1 = L(s, "h1", ("einfache Anführungszeichen", "single quotes", "comillas simples", "单引号", "guillemets simples",
                       "tek tırnak"), (xc, 1.42), FM, "left", GRAU)
    l_h2 = L(s, "h2", ("doppelte Anführungszeichen", "double quotes", "comillas dobles", "双引号", "guillemets doubles",
                       "çift tırnak"), (xc, -0.22), FM, "left", GRAU)
    c1 = tt(s, "bash -c 'echo Obst: $obst'", xc, 1.17)
    c2 = [tt(s, 'bash -c "echo Obst:', xc, -0.47), tt(s, '$obst"', sp(xc, 20), -0.47)]
    k1 = pbox(s, (2.2, 0.62), 2.4, 1.2)
    k2 = pbox(s, (2.2, -1.0), 2.4, 1.0)
    l_k1 = L(s, "kind", W_KSHELL, (1.1, 1.07), FM, "left", BLAU)
    l_k2 = L(s, "kind", W_KSHELL, (1.1, -0.65), FM, "left", BLAU)
    l_leer = L(s, "leer", ("obst: hier nicht gesetzt", "obst: not set here", "obst: aquí no definida", "obst：这里未设置",
                           "obst : non définie ici", "obst: burada tanımlı değil"), (1.12, 0.55), FM, "left", GRAU)
    l_a1 = L(s, "aus", W_AUSG, (1.12, 0.27), FM, "left", GRAU)
    o1 = tt(s, "Obst:", 1.95, 0.27)
    l_a2 = L(s, "aus", W_AUSG, (1.12, -1.25), FM, "left", GRAU)
    o2 = tt(s, "Obst: Apfel", 1.95, -1.25)
    a1 = pf(s, (-1.82, 0.62), (1.0, 0.62), farbe=DUNKEL)
    a2 = pf(s, (-1.82, -1.0), (1.0, -1.0), farbe=DUNKEL)
    rh2 = rahmen(s, (msp(xc, 20, 24), -0.47), 5 * C + 0.14, 0.3)
    xm, ym1, ym2 = sp(xc, 9), 0.88, -0.74
    m1 = [tt(s, "echo Obst:", xm, ym1), tt(s, "$obst", sp(xm, 11), ym1)]
    m2 = [tt(s, "echo Obst:", xm, ym2), tt(s, "Apfel", sp(xm, 11), ym2, farbe=GRUEN)]
    zc = notiz_z(s, sb["zx"], 0.0, "Apfel")
    dx = 1.12 - xm
    schritt(s, WACHS(sh, 0.6), EIN([l_sh] + sb["alle"], 0.6))
    s.pause(0.6)
    schritt(s, EIN([l_h1, c1], 0.6))
    schritt(s, ZEICHNE(a1, 0.6), WACHS(k1, 0.6), EIN(l_k1, 0.6))
    schritt(s, EIN(m1, 0.3))
    schritt(s, *VERS(m1, dx, 0.82 - ym1, 0.9))
    schritt(s, BETONE(m1[1], 0.6), EIN(l_leer, 0.6))
    schritt(s, EIN([l_a1, o1], 0.6))
    s.pause(0.6)
    schritt(s, EIN([l_h2] + c2, 0.6))
    schritt(s, EIN(rh2, 0.4), EIN(zc, 0.3))
    schritt(s, ZU(zc[0], msp(xc, 20, 24), -0.47, 0.8), ZU(zc[1], msp(xc, 20, 24), -0.47, 0.8))
    schritt(s, AUS(zc, 0.4), EIN(m2, 0.5))
    schritt(s, ZEICHNE(a2, 0.6), WACHS(k2, 0.6), EIN(l_k2, 0.6))
    schritt(s, *VERS(m2, dx, -0.88 - ym2, 0.9))
    schritt(s, EIN([l_a2, o2], 0.6))
    s.speichern()


def k5umgebung():
    """Beim Start bekommt printenv zwei Zettel: die Argumente und die Umgebung; es sucht HOME und USER heraus."""
    s = Szene("linux/k5umgebung", reihenfolge="anlegen")
    cmd = tt(s, "printenv HOME USER", -3.3, 1.55)
    sh = pbox(s, (-2.55, 0.15), 1.7, 2.1)
    l_sh = L(s, "shell", W_SHELL, (-2.55, 1.0), FM, "center", BLAU)
    pk = pbox(s, (1.01, -0.075), 4.82, 2.55)
    l_pk = L(s, "neu", ("neuer Prozess printenv", "new process printenv", "nuevo proceso printenv", "新进程 printenv",
                        "nouveau processus printenv", "yeni süreç printenv"), (-1.3, 1.02), FM, "left", BLAU)
    ax, ay, bx, by = -0.55, 0.3, 2.1, 0.2
    sx, sy = -2.55, 0.15
    za = box(s, (sx, sy), 1.2, 1.0, GRAU, GELB, 1.5, "rect")
    mA = [mark(s, ax - 0.35, ax + 0.35, ay + d, 0.2, ORANGE, 0.35) for d in (-0.13, -0.36)]
    ta = [L(s, "args", ("Argumente", "arguments", "argumentos", "参数", "arguments", "argümanlar"), (sx, sy + 0.35), FM, "center",
            GRAU)] + [tt(s, w, sx, sy + d, E2, anker="m") for w, d in (("printenv", 0.1), ("HOME", -0.13), ("USER", -0.36))]
    zb = box(s, (sx, sy), 2.2, 1.4, GRAU, GELB, 1.5, "rect")
    mB = [mark(s, bx - 1.0, bx - 1.0 + 0.1 + n * cw(E2), by + d, 0.2, ORANGE, 0.35) for n, d in ((18, 0.3), (12, 0.08))]
    zeilen = ("HOME=/home/student", "USER=student", "SHELL=/bin/bash", "LANG=C.UTF-8", "…")
    tb = [L(s, "umg", ("Umgebung", "environment", "entorno", "环境", "environnement", "ortam"), (sx, sy + 0.55), FM, "center",
            GRAU)] + [tt(s, z, sx - 0.95, sy + 0.3 - 0.22 * i, E2) for i, z in enumerate(zeilen)]
    l_aus = L(s, "aus", W_AUSG, (-1.3, -0.72), FM, "left", GRAU)
    out = [tt(s, "/home/student", -0.35, -0.72), tt(s, "student", -0.35, -0.98)]
    schritt(s, EIN(cmd, 0.5), WACHS(sh, 0.6), EIN(l_sh, 0.6))
    s.pause(0.6)
    schritt(s, WACHS(pk, 0.6), EIN(l_pk, 0.6))
    schritt(s, EIN([za] + ta, 0.4))
    schritt(s, *VERS([za] + ta, ax - sx, ay - sy, 0.9))
    schritt(s, EIN([zb] + tb, 0.4))
    schritt(s, *VERS([zb] + tb, bx - sx, by - sy, 0.9))
    s.pause(0.6)
    schritt(s, EIN(mA, 0.5))
    schritt(s, EIN(mB, 0.5))
    schritt(s, EIN([l_aus] + out, 0.6))
    s.speichern()


def k5export():
    """Drei Schubladen; export obst setzt die Markierung; beim Start kommen genau die markierten in die Umgebung des Kindes."""
    s = Szene("linux/k5export", reihenfolge="anlegen")
    cmd = tt(s, "export obst", -3.3, 1.6)
    sh = pbox(s, (-1.88, 0.0), 3.04, 2.5)
    l_sh = L(s, "shell", W_SHELL, (-3.3, 1.02), FM, "left", BLAU)
    ys = (0.55, -0.05, -0.65)
    sbs = [schublade(s, -3.3, y, n, w, anker="l") for y, (n, w) in zip(ys, (("HOME", "/home/student"), ("wohnort", "Hamburg"),
                                                                          ("obst", "Apfel")))]

    def fahne(y):
        return [box(s, (-0.82, y), 0.66, 0.28, ORANGE, ORANGE_HELL, 1.5), tt(s, "export", -0.82, y, 0.15, ORANGE, "m")]
    f_home, f_obst = fahne(ys[0]), fahne(ys[2])
    kd = pbox(s, (1.95, 0.0), 2.9, 2.5)
    l_kd = L(s, "kind", W_KIND, (0.6, 1.02), FM, "left", BLAU)
    l_umg = L(s, "umg", W_UMG, (0.6, 0.72), FM, "left", GRAU)
    a = pf(s, (-0.36, 0.95), (0.5, 0.95), farbe=DUNKEL)
    l_st = L(s, "start", ("Start", "start", "inicio", "启动", "démarrage", "başlatma"), (0.07, 1.12), FM, "center", DUNKEL)
    rw = rahmen(s, (sbs[1]["x"], ys[1]), sbs[1]["b"] + 0.12, 0.52, ROT, 3)
    l_bl = L(s, "bleibt", ("nicht markiert: bleibt in der Shell", "not marked: stays in the shell",
                           "sin marcar: se queda en la shell", "未标记：留在 Shell 中", "non marquée : reste dans le shell",
                           "işaretsiz: kabukta kalır"), (-1.88, -1.05), FM, "center", ROT)
    kh = tt(s, "HOME=/home/student", -3.3 + 0.07, ys[0], E2)
    ko = tt(s, "obst=Apfel", -3.3 + 0.07, ys[2], E2)
    schritt(s, WACHS(sh, 0.6), EIN([l_sh] + sbs[0]["alle"] + sbs[1]["alle"] + sbs[2]["alle"] + f_home, 0.6))
    s.pause(0.6)
    schritt(s, EIN(cmd, 0.6))
    schritt(s, EIN(f_obst, 0.5))
    schritt(s, BETONE(f_obst, 0.7))
    s.pause(0.6)
    schritt(s, ZEICHNE(a, 0.6), EIN(l_st, 0.6), WACHS(kd, 0.6), EIN([l_kd, l_umg], 0.6))
    schritt(s, EIN([kh, ko], 0.3))
    schritt(s, ZU(kh, 0.65 + 9 * cw(E2), 0.4, 1.0), ZU(ko, 0.65 + 5 * cw(E2), 0.12, 1.0))
    s.pause(0.4)
    schritt(s, EIN([rw, l_bl], 0.6))
    s.speichern()


def k5vererbung():
    """Zeitleiste: Kind bekommt beim Start eine Kopie (obst=Apfel), ändert sie in Birne; kein Weg zurück; Kind endet,
    die Shell hat weiter Apfel."""
    s = Szene("linux/k5vererbung", reihenfolge="anlegen")
    lane = flaeche(s, -3.4, 0.6, 3.4, 1.1, BLAU_HELL)
    l_sh = L(s, "shell", W_SHELL, (-3.35, 1.3), FM, "left", BLAU)
    s1 = schublade(s, -2.4, 0.85, "obst", "Apfel")
    s2 = schublade(s, 2.5, 0.85, "obst", "Apfel")
    l_unv = L(s, "unv", ("unverändert", "unchanged", "sin cambios", "未改变", "inchangé", "değişmedi"), (2.5, 0.42), FM, "center",
              GRUEN)
    kd = pbox(s, (0.0, -0.65), 3.5, 0.9)
    l_kd = L(s, "kind", W_KIND, (-1.65, -0.33), FM, "left", BLAU)
    k1 = schublade(s, -0.85, -0.72, "obst", "Apfel")
    k2 = schublade(s, 0.85, -0.72, "obst", "Apfel")
    a12 = pf(s, (-0.17, -0.72), (0.13, -0.72), farbe=GRAU)
    a_k = pf(s, (-2.4, 0.62), (-0.95, -0.47), farbe=BLAU)
    l_k = L(s, "kopie", ("Kopie beim Start", "copy at start", "copia al inicio", "启动时的副本", "copie au démarrage",
                         "başlangıçta kopya"), (-1.75, 0.02), FM, "right", BLAU)
    l_ae = L(s, "aend", ("ändert seine Kopie", "changes its copy", "cambia su copia", "修改自己的副本", "modifie sa copie",
                         "kendi kopyasını değiştirir"), (0.85, -1.27), FM, "center", ORANGE)
    a_b = pf(s, (0.95, -0.5), (1.5, 0.58), farbe=ORANGE, dash=DASH)
    x_b = s.kreuzchen(None, 1.22, 0.04, farbe=ROT, groesse=0.2, dicke=4)
    l_kein = L(s, "zurueck", ("kein Weg zurück", "no way back", "sin camino de vuelta", "无法传回", "pas de retour", "geri dönüş yok"),
               (1.42, 0.04), FM, "left", ROT)
    schl = schleier(s, (0.0, -0.65), 3.56, 0.96, 0.6)
    l_end = L(s, "ende", ("Kind beendet:\nKopie verschwunden", "child ended:\ncopy gone", "hijo terminado:\ncopia desaparecida",
                          "子进程已结束：\n副本消失", "enfant terminé :\ncopie disparue", "alt süreç bitti:\nkopya yok"),
              (-1.85, -0.85), FM, "right", DUNKEL)
    zeit = pf(s, (-3.3, -1.62), (3.3, -1.62), farbe=GRAU)
    l_zeit = L(s, "zeit", ("Zeit", "time", "tiempo", "时间", "temps", "zaman"), (3.3, -1.45), FM, "right", GRAU)
    schritt(s, EIN([lane, l_sh, zeit, l_zeit] + s1["alle"], 0.6))
    s.pause(0.6)
    schritt(s, ZEICHNE(a_k, 0.7), EIN(l_k, 0.7), WACHS(kd, 0.7), EIN(l_kd, 0.7))
    schritt(s, EIN(k1["alle"], 0.6))
    s.pause(0.6)
    schritt(s, ZEICHNE(a12, 0.4), EIN(k2["alle"], 0.6))
    with s.gleichzeitig():
        s.ersetzen(k2["z"][1], "Birne", farbe=ORANGE, dauer=0.8)
        schritt(s, EIN(l_ae, 0.8))
    s.pause(0.6)
    schritt(s, ZEICHNE(a_b, 0.7))
    schritt(s, EIN([x_b, l_kein], 0.6))
    s.pause(0.6)
    schritt(s, EIN([schl, l_end], 0.7))
    schritt(s, EIN(s2["alle"] + [l_unv], 0.7))
    s.speichern()


def k5einbefehl():
    """TZ=Asia/Tokyo date: Kopie der Umgebung plus TZ, Uhr 15:26; date: Kopie ohne TZ, Uhr 07:26; die Shell bleibt ohne TZ."""
    s = Szene("linux/k5einbefehl", reihenfolge="anlegen")
    sh = pbox(s, (-2.3, 0.0), 2.24, 2.9)
    l_sh = L(s, "shell", W_SHELL, (-3.3, 1.25), FM, "left", BLAU)
    l_umg = L(s, "umg", W_UMG, (-3.3, 0.98), FM, "left", GRAU)
    env = [tt(s, z, -3.3, 0.72 - 0.22 * i, E3) for i, z in enumerate(("HOME=/home/student", "LANG=C.UTF-8", "USER=student", "…"))]
    l_kein = L(s, "keintz", ("kein TZ", "no TZ", "sin TZ", "没有 TZ", "pas de TZ", "TZ yok"), (-3.3, -0.25), FM, "left", GRAU)
    hk = haken(s, -3.15, -0.9)
    l_unv = L(s, "unv", ("unverändert", "unchanged", "sin cambios", "未改变", "inchangé", "değişmedi"), (-2.95, -0.9), FM, "left",
              GRUEN)
    kopie = "HOME=… LANG=… USER=… …"
    zx, zy0 = -2.3, 0.4

    def reihe(yc, cmd_teile, mit_tz, std, minute, ort, okey):
        cm = stuecke(s, -0.9, yc + 0.72, cmd_teile)
        kd = pbox(s, (0.35, yc), 2.5, 0.85)
        dn = tt(s, "date", -0.8, yc + 0.27, E2)
        hz = 0.5 if mit_tz else 0.3
        z = [box(s, (zx, zy0), 2.2, hz, GRAU, GELB, 1.5, "rect"),
             tt(s, kopie, zx - 1.0, zy0 + (0.1 if mit_tz else 0.0), E3)]
        tz = tt(s, "TZ=Asia/Tokyo", -0.9, yc + 0.72, E3, GRUEN) if mit_tz else None
        u = uhr(s, 2.45, yc + 0.05, std, minute, 0.3)
        zeit = tt(s, "%02d:%02d" % (std, minute), 2.45, yc - 0.42, E2, anker="m")
        o = L(s, okey, ort, (2.45, yc + 0.5), FM, "center", GRAU)
        return cm, kd, dn, z, tz, list(u) + [zeit, o]

    cm1, kd1, dn1, z1, tz1, u1 = reihe(0.6, (("TZ=Asia/Tokyo", GRUEN), (" date", SCHWARZ)), True, 15, 26,
                                       ("Tokio", "Tokyo", "Tokio", "东京", "Tokyo", "Tokyo"), "tokio")
    cm2, kd2, dn2, z2, _, u2 = reihe(-0.98, (("date", SCHWARZ),), False, 7, 26,
                                     ("Berlin", "Berlin", "Berlín", "柏林", "Berlin", "Berlin"), "berlin")
    schritt(s, WACHS(sh, 0.6), EIN([l_sh, l_umg, l_kein] + env, 0.6))
    s.pause(0.6)
    schritt(s, EIN(cm1, 0.5))
    schritt(s, WACHS(kd1, 0.5), EIN(dn1, 0.5))
    schritt(s, EIN(z1, 0.3))
    schritt(s, *VERS(z1, 0.35 - zx, 0.52 - zy0, 0.9))
    schritt(s, EIN(tz1, 0.2))
    schritt(s, ZU(tz1, 0.35 - 1.0 + 6.5 * cw(E3), 0.42, 0.8))
    schritt(s, EIN(u1, 0.6))
    s.pause(0.6)
    schritt(s, EIN(cm2, 0.5))
    schritt(s, WACHS(kd2, 0.5), EIN(dn2, 0.5))
    schritt(s, EIN(z2, 0.3))
    schritt(s, *VERS(z2, 0.35 - zx, -1.03 - zy0, 0.9))
    schritt(s, EIN(u2, 0.6))
    s.pause(0.6)
    schritt(s, EIN(hk + [l_unv], 0.6))
    s.speichern()


# ================================================================== Abschnitt 5: PATH
PFADE = ("/usr/local/sbin", "/usr/local/bin", "/usr/sbin", "/usr/bin", "/sbin", "/bin", "…")


def k5path():
    """Der Wert von PATH ist ein Text; die Doppelpunkte trennen; die Stücke ergeben die nummerierte Suchreihenfolge."""
    s = Szene("linux/k5path", reihenfolge="anlegen")
    wert = ":".join(PFADE)
    x0, y0 = -len(wert) / 2 * C, 1.45
    l_w = L(s, "wert", ("Wert von PATH: ein einziger Text", "value of PATH: one single text", "valor de PATH: un único texto",
                        "PATH 的值：一个文本", "valeur de PATH : un seul texte", "PATH değeri: tek bir metin"),
            (0.0, 1.78), FM, "center", GRAU)
    cols = [i for i, ch in enumerate(wert) if ch == ":"]
    mk = [mark(s, sp(x0, c), sp(x0, c + 1), y0, 0.27, ORANGE, 0.5) for c in cols]
    strip = tt(s, wert, x0, y0)
    starts = [0] + [c + 1 for c in cols]
    xl = -1.8
    ys = [r4(0.85 - 0.28 * i) for i in range(len(PFADE))]
    nums = [text(s, "%d." % (i + 1), (xl - 0.12, y), FM, "right", GRAU) for i, y in enumerate(ys)]
    kop = [tt(s, p, sp(x0, a), y0) for p, a in zip(PFADE, starts)]
    pfeil = pf(s, (0.3, ys[0]), (0.3, ys[-1]), farbe=ORANGE, dicke=4, spitze=0.14)
    l_r = L(s, "reihe", ("Suchreihenfolge", "search order", "orden de búsqueda", "搜索顺序", "ordre de recherche", "arama sırası"),
            (0.45, (ys[0] + ys[-1]) / 2), FM, "left", ORANGE)
    schritt(s, EIN([l_w, strip, *kop], 0.6))
    s.pause(0.6)
    schritt(s, EIN(mk, 0.5))
    schritt(s, BETONE(mk, 0.7))
    s.pause(0.6)
    schritt(s, *[ZU(k, xl + len(p) / 2 * C, y, 1.2) for k, p, y in zip(kop, PFADE, ys)])
    schritt(s, EIN(nums, 0.5))
    s.pause(0.6)
    schritt(s, ZEICHNE(pfeil, 0.8), EIN(l_r, 0.8))
    s.speichern()


def k5befehlssuche():
    """Entscheidungsbaum der Befehlssuche; der bekannte Teil (Alias … eingebaut) grau; Beispiele /usr/bin/echo und tree."""
    s = Szene("linux/k5befehlssuche", reihenfolge="anlegen")

    def knot(mitte, b, h, key, w, rand, fuell, tf):
        return [box(s, mitte, b, h, rand, fuell, 2.5), L(s, key, w, mitte, FM, "center", tf)]
    xq = -1.0
    Q1 = knot((xq, 1.45), 2.4, 0.45, "q1", ("Schrägstrich im Namen?", "slash in the name?", "¿barra en el nombre?", "名称中有斜杠吗？",
                                              "barre oblique dans le nom ?", "adda eğik çizgi var mı?"), DUNKEL, WEISS, SCHWARZ)
    A = knot((2.25, 1.45), 2.2, 0.55, "a", ("genau diese Datei\nstarten", "start exactly\nthis file", "iniciar exactamente\neste archivo",
                                            "启动的正是\n这个文件", "démarrer exactement\nce fichier", "tam olarak bu\ndosyayı başlat"),
             GRUEN, GRUEN_HELL, SCHWARZ)
    Q2 = knot((xq, 0.5), 2.4, 0.6, "q2", ("Alias, Schlüsselwort,\nFunktion, eingebaut?", "alias, keyword,\nfunction, builtin?",
                                          "¿alias, palabra clave,\nfunción, interna?", "别名、关键字、\n函数、内置命令？",
                                          "alias, mot-clé,\nfonction, intégrée ?", "takma ad, anahtar sözcük,\nişlev, yerleşik?"),
              HELLGRAU, GRAU_HELL, GRAU)
    B = knot((2.25, 0.5), 2.2, 0.55, "b", ("Shell erledigt\nes selbst", "the shell handles\nit itself", "la shell lo hace\nella misma",
                                           "Shell 自己\n处理", "le shell s'en\ncharge lui-même", "kabuk kendisi\nhalleder"),
             HELLGRAU, GRAU_HELL, GRAU)
    P = knot((xq, -0.45), 2.4, 0.6, "p", ("PATH von links\nnach rechts durchsuchen", "search PATH from\nleft to right",
                                          "recorrer PATH de\nizquierda a derecha", "从左到右\n搜索 PATH",
                                          "parcourir PATH de\ngauche à droite", "PATH'i soldan\nsağa ara"), ORANGE, WEISS, SCHWARZ)
    Cc = knot((-2.2, -1.45), 2.3, 0.55, "c", ("Treffer: starten\nund Pfad merken", "found: start it and\nremember the path",
                                              "encontrado: iniciar y\nrecordar la ruta", "找到：启动\n并记住路径",
                                              "trouvé : démarrer et\nretenir le chemin", "bulundu: başlat ve\nyolu hatırla"),
              GRUEN, GRUEN_HELL, SCHWARZ)
    D = knot((1.05, -1.45), 2.6, 0.55, "d", ("kein Treffer: command\nnot found, 127", "not found: command\nnot found, 127",
                                             "no encontrado: command\nnot found, 127", "未找到：command\nnot found，127",
                                             "pas trouvé : command\nnot found, 127", "bulunamadı: command\nnot found, 127"),
              ROT, ROT_HELL, SCHWARZ)
    W_JA = ("ja", "yes", "sí", "是", "oui", "evet")
    W_NEIN = ("nein", "no", "no", "否", "non", "hayır")
    a_q1a = pf(s, (0.2, 1.45), (1.15, 1.45), farbe=DUNKEL)
    l_j1 = L(s, "ja", W_JA, (0.67, 1.6), FM, "center", DUNKEL)
    a_q1q2 = pf(s, (xq, 1.22), (xq, 0.8), farbe=DUNKEL)
    l_n1 = L(s, "nein", W_NEIN, (xq - 0.12, 1.01), FM, "right", DUNKEL)
    a_q2b = pf(s, (0.2, 0.5), (1.15, 0.5), farbe=HELLGRAU)
    l_j2 = L(s, "ja", W_JA, (0.67, 0.65), FM, "center", GRAU)
    a_q2p = pf(s, (xq, 0.2), (xq, -0.15), farbe=DUNKEL)
    l_n2 = L(s, "nein", W_NEIN, (xq - 0.12, 0.03), FM, "right", DUNKEL)
    a_pc = pf(s, (-1.6, -0.75), (-2.2, -1.17), farbe=GRUEN)
    a_pd = pf(s, (-0.4, -0.75), (0.5, -1.17), farbe=ROT)
    ce = wort(s, -2.85, 1.45, "/usr/bin/echo", E3, ORANGE, ORANGE_HELL)
    ctr = wort(s, -2.85, 0.95, "tree", E3, BLAU, BLAU_HELL)
    schritt(s, WACHS([Q2[0], B[0]], 0.6), EIN([Q2[1], B[1], l_j2], 0.6), ZEICHNE(a_q2b, 0.6))
    s.pause(0.6)
    schritt(s, WACHS(Q1[0], 0.6), EIN(Q1[1], 0.6), ZEICHNE(a_q1q2, 0.6), EIN(l_n1, 0.6))
    schritt(s, ZEICHNE(a_q1a, 0.6), EIN(l_j1, 0.6), WACHS(A[0], 0.6), EIN(A[1], 0.6))
    s.pause(0.4)
    schritt(s, ZEICHNE(a_q2p, 0.6), EIN(l_n2, 0.6), WACHS(P[0], 0.6), EIN(P[1], 0.6))
    schritt(s, ZEICHNE([a_pc, a_pd], 0.7), WACHS([Cc[0], D[0]], 0.7), EIN([Cc[1], D[1]], 0.7))
    s.pause(0.6)
    schritt(s, EIN(ce, 0.4))
    schritt(s, ZU(ce[0], 0.67, 1.45, 0.7), ZU(ce[1], 0.67, 1.45, 0.7))
    schritt(s, ZU(ce[0], 2.25, 1.0, 0.7), ZU(ce[1], 2.25, 1.0, 0.7))
    s.pause(0.4)
    schritt(s, EIN(ctr, 0.4))
    for x, y in ((xq, 1.01), (xq, 0.03), (-2.9, -0.98)):
        schritt(s, ZU(ctr[0], x, y, 0.6), ZU(ctr[1], x, y, 0.6))
    s.speichern()


def k5punktslash():
    """meinbaum: Suche nur in PATH, das Arbeitsverzeichnis gehört nicht dazu, 127; ./meinbaum: Schrägstrich, direkter Start."""
    s = Szene("linux/k5punktslash", reihenfolge="anlegen")
    pb = box(s, (-2.48, 0.2), 1.88, 2.25, GRAU, GRAU_HELL, form="rect")
    l_p = L(s, "such", ("Suchpfad (PATH)", "search path (PATH)", "ruta de búsqueda (PATH)", "搜索路径（PATH）",
                        "chemin de recherche (PATH)", "arama yolu (PATH)"), (-2.48, 1.15), FM, "center", GRAU)
    ein = [tt(s, p, -3.3, 0.88 - 0.25 * i, E3, GRAU) for i, p in enumerate(PFADE)]
    wd = box(s, (2.25, 0.75), 2.3, 1.15, form="rect")
    l_wd = L(s, "arb", ("Arbeitsverzeichnis", "working directory", "directorio de trabajo", "工作目录", "répertoire de travail",
                        "çalışma dizini"), (2.25, 1.47), FM, "center", GRAU)
    h_wd = tt(s, "/home/student/linuxk5", 2.25, 1.15, E3, anker="m")
    ds = datei_symbol(s, 1.3, 0.8)
    t_mb = tt(s, "meinbaum", 1.45, 0.8, E2)
    os_ = ordner_symbol(s, 1.3, 0.46)
    t_ur = tt(s, "urlaub", 1.5, 0.46, E2)
    l_nicht = L(s, "nicht", ("nicht im Suchpfad", "not in the search path", "no está en la ruta de búsqueda", "不在搜索路径中",
                             "pas dans le chemin de recherche", "arama yolunda değil"), (2.25, -0.03), FM, "center", ORANGE)
    c1 = tt(s, "meinbaum", -0.22, 0.85, anker="m")
    a1 = pf(s, (-0.62, 0.85), (-1.5, 0.85), farbe=ROT)
    x1 = s.kreuzchen(None, -1.54, 0.85, farbe=ROT, groesse=0.22, dicke=4)
    l_127 = L(s, "nf", ("nicht gefunden: 127", "not found: 127", "no encontrado: 127", "未找到：127", "introuvable : 127",
                        "bulunamadı: 127"), (-0.22, 0.55), FM, "center", ROT)
    xc0 = -0.22 - 5 * C
    m_sl = mark(s, sp(xc0, 1), sp(xc0, 2), -0.45, 0.28, ORANGE, 0.5)
    c2 = tt(s, "./meinbaum", xc0, -0.45)
    a2 = pf(s, (0.3, -0.38), (1.18, 0.7), farbe=GRUEN)
    l_kein = L(s, "keine", ("Schrägstrich: keine Suche", "slash: no search", "barra: sin búsqueda", "斜杠：不搜索",
                            "barre oblique : pas de recherche", "eğik çizgi: arama yok"), (-0.22, -0.75), FM, "center", GRUEN)
    term = term_kasten(s, (2.35, -1.0), 1.6, 1.12)
    baum_z = ("urlaub", "├── 2025", "│   ├── sommer", "│   └── winter", "└── 2026", "    ├── sommer", "    └── winter")
    bz = [tt(s, z, 1.62, -0.55 - 0.15 * i, 0.13) for i, z in enumerate(baum_z)]
    l_aus = L(s, "aus", W_AUSG, (1.45, -1.0), FM, "right", GRAU)
    schritt(s, WACHS(pb, 0.6), EIN([l_p] + ein, 0.6), WACHS(wd, 0.6), EIN([l_wd, h_wd, ds, t_mb, os_, t_ur, l_nicht], 0.6))
    s.pause(0.6)
    schritt(s, EIN(c1, 0.5))
    schritt(s, ZEICHNE(a1, 0.6))
    schritt(s, EIN([x1, l_127], 0.6))
    s.pause(0.6)
    schritt(s, EIN(c2, 0.5))
    schritt(s, EIN(m_sl, 0.4), BETONE(c2, 0.7))
    schritt(s, ZEICHNE(a2, 0.7), EIN(l_kein, 0.7))
    schritt(s, BETONE([ds, t_mb], 0.6))
    schritt(s, WACHS(term, 0.5), EIN(bz + [l_aus], 0.6))
    s.speichern()


def k5pathneu():
    """PATH="$HOME/linuxk5/bin:$PATH": alter Text bleibt, neues Verzeichnis vorn (Nr. 1); PATH=/gibtsnicht: nur ein Eintrag."""
    s = Szene("linux/k5pathneu", reihenfolge="anlegen")
    x0, y1, y2 = -3.3, 1.6, 1.18
    zu = stuecke(s, x0, y1, (('PATH="', SCHWARZ), ("$HOME/linuxk5/bin:", GRUEN), ("$PATH", ORANGE), ('"', SCHWARZ)))
    rh = rahmen(s, (msp(x0, 24, 28), y1), 5 * C + 0.14, 0.3)
    neu, alt = "/home/student/linuxk5/bin:", "/usr/local/sbin:/usr/local/bin:…"
    v_neu = tt(s, neu, x0, y2, farbe=GRUEN)
    v_alt = tt(s, alt, sp(x0, 26), y2)
    a_alt = pf(s, (msp(x0, 24, 28), y1 - 0.13), (msp(x0, 26, 57), y2 + 0.13), farbe=ORANGE)
    kl_alt = klammer(s, sp(x0, 26), sp(x0, 58), y2 - 0.15, unten=False, farbe=ORANGE, t=0.06, dicke=2)
    l_alt = L(s, "alt", ("alter Wert von $PATH", "old value of $PATH", "valor anterior de $PATH", "$PATH 的旧值",
                         "ancienne valeur de $PATH", "$PATH'in eski değeri"), (msp(x0, 26, 57), y2 - 0.36), FM, "center", ORANGE,
              roh=True)
    kl_neu = klammer(s, sp(x0, 0), sp(x0, 26), y2 - 0.15, unten=False, farbe=GRUEN, t=0.06, dicke=2)
    l_neu = L(s, "neu", ("neues Verzeichnis + :", "new directory + :", "directorio nuevo + :", "新目录 + :", "nouveau répertoire + :",
                         "yeni dizin + :"), (msp(x0, 0, 25), y2 - 0.36), FM, "center", GRUEN)
    xl = -2.9
    rows = [r4(0.5 - 0.28 * i) for i in range(4)]
    nums = [text(s, "%d." % (i + 1), (xl - 0.12, y), FM, "right", GRAU) for i, y in enumerate(rows)]
    alte = ("/usr/local/sbin", "/usr/local/bin", "…")
    ac = [sp(x0, 26), sp(x0, 42), sp(x0, 57)]
    k_alt = [tt(s, p, a, y2) for p, a in zip(alte, ac)]
    k_neu = tt(s, "/home/student/linuxk5/bin", x0, y2, farbe=GRUEN)
    l_vorn = L(s, "vorn", ("vorn = Vorrang", "in front = priority", "delante = prioridad", "在前 = 优先", "devant = priorité",
                           "önde = öncelik"), (-0.4, rows[0]), FM, "left", GRUEN)
    sep = linie(s, (-3.4, -0.55), (3.4, -0.55), HELLGRAU, 1.5, DASH)
    y3 = -0.82
    z2 = tt(s, "PATH=/gibtsnicht", x0, y3)
    l_kein = L(s, "kein", ("kein $PATH in der Zuweisung", "no $PATH in the assignment", "sin $PATH en la asignación",
                           "赋值中没有 $PATH", "pas de $PATH dans l'affectation", "atamada $PATH yok"), (-1.65, y3), FM, "left", GRAU,
               roh=True)
    rows2 = [r4(-1.17 - 0.28 * i) for i in range(3)]
    n2 = text(s, "1.", (xl - 0.12, rows2[0]), FM, "right", GRAU)
    grau = [tt(s, p, xl, y, farbe=HELLGRAU) for p, y in zip(alte, rows2)]
    g_str = [linie(s, (xl - 0.03, y), (xl + len(p) * C + 0.03, y), ROT, 2.5) for p, y in zip(alte, rows2)]
    n_g = tt(s, "/gibtsnicht", xl, rows2[0])
    ls_ = tt(s, "ls", 0.2, rows2[0])
    a_ls = pf(s, (0.45, rows2[0]), (0.85, rows2[0]), farbe=ROT)
    l_nf = L(s, "nf", ("nicht gefunden", "not found", "no encontrado", "未找到", "introuvable", "bulunamadı"), (0.95, rows2[0]), FM,
             "left", ROT)
    schritt(s, EIN(zu, 0.6))
    s.pause(0.6)
    schritt(s, EIN(rh, 0.4), BETONE(zu[2], 0.7))
    schritt(s, ZEICHNE(a_alt, 0.6), EIN([v_alt, l_alt] + kl_alt, 0.6))
    s.pause(0.4)
    schritt(s, BETONE(zu[1], 0.7))
    schritt(s, EIN([v_neu, l_neu] + kl_neu, 0.6))
    s.pause(0.6)
    schritt(s, EIN(k_alt, 0.2))
    schritt(s, *[ZU(k, xl + len(p) / 2 * C, y, 0.9) for k, p, y in zip(k_alt, alte, rows)], EIN(nums[:3], 0.6))
    schritt(s, *VERS(k_alt, 0, rows[1] - rows[0], 0.7), EIN(nums[3], 0.6), EIN(k_neu, 0.3))
    schritt(s, ZU(k_neu, xl + 12.5 * C, rows[0], 0.9))
    schritt(s, EIN(l_vorn, 0.6))
    s.pause(0.6)
    schritt(s, ZEICHNE(sep, 0.5), EIN([z2, l_kein], 0.6))
    schritt(s, EIN(grau, 0.5))
    schritt(s, ZEICHNE(g_str, 0.4))
    schritt(s, AUS(grau + g_str, 0.5), EIN([n2, n_g], 0.6))
    s.pause(0.4)
    schritt(s, EIN([ls_, a_ls, l_nf], 0.6))
    s.speichern()


# ================================================================== Abschnitt 6: Startdateien und Aliase
def k5startdatei():
    """Start einer interaktiven bash: ~/.bashrc wird Zeile für Zeile ausgeführt, die Aliase entstehen; erst dann die
    Eingabeaufforderung."""
    s = Szene("linux/k5startdatei", reihenfolge="anlegen")
    bs = bildschirm(s, (-1.95, 0.95), 2.9, 0.95)
    l_t = L(s, "term", ("Terminal", "terminal", "terminal", "终端", "terminal", "terminal"), (-1.95, 1.58), FM, "center", GRAU)
    l_bs = L(s, "bst", ("bash startet …", "bash is starting …", "bash se inicia …", "bash 正在启动 …", "bash démarre …",
                        "bash başlıyor …"), (-1.95, 0.95), FM, "center", GRAU)
    prompt = tt(s, "student@labor:~$", -3.25, 1.2)
    cursor = box(s, (sp(-3.25, 17) + C / 2, 1.2), C, 0.17, DUNKEL, DUNKEL, 1, "rect")
    ab = pbox(s, (-1.95, -0.6), 2.9, 1.65)
    l_ab = L(s, "aliase", ("Aliase der Shell", "aliases of the shell", "alias de la shell", "Shell 的别名", "alias du shell",
                           "kabuğun takma adları"), (-1.95, 0.02), FM, "center", BLAU)
    fb = box(s, (1.75, 0.0), 3.2, 2.85, GRAU, WEISS, 2, "rect")
    hdr = tt(s, "~/.bashrc", 0.3, 1.22, E2, ORANGE)
    sepl = linie(s, (0.2, 1.07), (3.3, 1.07), HELLGRAU, 1.5)
    zeilen = ("…", "HISTSIZE=1000", "…", "alias ll='ls -alF'", "alias la='ls -A'", "alias l='ls -CF'", "…")
    ys = [r4(0.85 - 0.3 * i) for i in range(len(zeilen))]
    zt = [tt(s, z, 0.3, y, E2) for z, y in zip(zeilen, ys)]
    mrk = rahmen(s, (1.75, ys[0]), 3.0, 0.26, ORANGE, 2.5)
    aliase = {3: "ll='ls -alF'", 4: "la='ls -A'", 5: "l='ls -CF'"}
    ay = {3: -0.32, 4: -0.62, 5: -0.92}
    kop = {i: tt(s, a, sp(0.3, 6, E2), ys[i], E2) for i, a in aliase.items()}
    schritt(s, EIN([bs, l_t, l_bs], 0.6))
    s.pause(0.6)
    schritt(s, WACHS(fb, 0.6), EIN([hdr, sepl] + zt, 0.6))
    schritt(s, WACHS(ab, 0.5), EIN(l_ab, 0.5))
    s.pause(0.4)
    schritt(s, EIN(mrk, 0.3))
    for i in range(1, len(zeilen)):
        schritt(s, ZU(mrk, 1.75, ys[i], 0.35))
        if i in aliase:
            schritt(s, EIN(kop[i], 0.2))
            schritt(s, ZU(kop[i], -3.2 + len(aliase[i]) / 2 * cw(E2), ay[i], 0.7))
    s.pause(0.4)
    schritt(s, AUS([mrk, l_bs], 0.5), EIN([prompt, cursor], 0.6))
    s.speichern()


def k5source():
    """farbe.txt (farbe=blau): oben in einer Kind-Shell gelesen (Variable verschwindet mit dem Kind), unten mit source in der
    Shell selbst (bleibt)."""
    s = Szene("linux/k5source", reihenfolge="anlegen")
    fb = box(s, (-2.75, -0.2), 1.25, 0.6, GRAU, WEISS, 2, "rect")
    f_n = tt(s, "farbe.txt", -2.75, 0.28, E2, anker="m")
    f_i = tt(s, "farbe=blau", -2.75, -0.2, E2, anker="m")
    sh = pbox(s, (2.3, -0.45), 2.1, 1.6)
    l_sh = L(s, "shell", W_SHELL, (1.4, 0.17), FM, "left", BLAU)
    leer = schublade(s, 2.3, -0.42, "farbe", None, slot=4)
    l_ng = L(s, "ng", ("nicht gesetzt", "not set", "no definida", "未设置", "non définie", "tanımlı değil"), (2.3, -0.9), FX,
             "center", GRAU)
    kd = pbox(s, (-0.25, 0.85), 2.4, 1.0)
    l_kd = L(s, "kind", W_KSHELL, (-1.35, 1.2), FM, "left", BLAU)
    sk = schublade(s, -0.25, 0.75, "farbe", "blau")
    a1 = pf(s, (-2.1, 0.12), (-1.47, 0.62), farbe=DUNKEL)
    schl = schleier(s, (-0.25, 0.85), 2.46, 1.06, 0.72)
    l_end = L(s, "ende", ("beendet: farbe weg", "ended: farbe gone", "terminado: farbe desaparece", "已结束：farbe 消失",
                          "terminé : farbe disparue", "bitti: farbe yok"), (-0.25, 0.85), FM, "center", DUNKEL)
    a2 = pf(s, (-2.1, -0.4), (1.23, -0.4), farbe=GRUEN)
    l_src = tt(s, "source ./farbe.txt", -0.42, -0.23, E3, GRUEN, "m")
    ss = schublade(s, 2.3, -0.42, "farbe", "blau")
    schritt(s, WACHS(fb, 0.6), EIN([f_n, f_i], 0.6), WACHS(sh, 0.6), EIN([l_sh, l_ng] + leer["alle"], 0.6))
    s.pause(0.6)
    schritt(s, ZEICHNE(a1, 0.6), WACHS(kd, 0.6), EIN(l_kd, 0.6))
    schritt(s, BETONE(f_i, 0.6), EIN(sk["alle"], 0.6))
    s.pause(0.6)
    schritt(s, AUS(sk["alle"], 0.5), EIN([schl, l_end], 0.6))
    s.pause(0.6)
    schritt(s, ZEICHNE(a2, 0.7), EIN(l_src, 0.7))
    with s.gleichzeitig():
        schritt(s, EIN(ss["alle"], 0.6), AUS(leer["alle"], 0.4))
        s.ersetzen(l_ng, T(s, "bleibt", "bleibt gesetzt", "stays set", "sigue definida", "保持设置", "reste définie",
                           "tanımlı kalır"), farbe=GRUEN, dauer=0.6)
    s.speichern()


def k5startdateien():
    """Drei Fälle: Anmelde-Shell (/etc/profile → ~/.profile → ~/.bashrc), interaktiv ohne Anmeldung (/etc/bash.bashrc →
    ~/.bashrc), bash -c (keine Startdatei)."""
    s = Szene("linux/k5startdateien", reihenfolge="anlegen")
    xs = (-2.3, 0.0, 2.3)
    yb = (0.6, -0.15, -0.9)
    e = 0.16
    h1 = L(s, "h1", ("Anmelde-Shell\n(z. B. Terminal von WSL)", "login shell\n(e.g. WSL terminal)",
                     "shell de inicio de sesión\n(p. ej., terminal de WSL)", "登录 shell\n（例如 WSL 终端）",
                     "shell de connexion\n(p. ex. terminal de WSL)", "oturum açma kabuğu\n(ör. WSL terminali)"),
           (xs[0], 1.4), FM, "center", DUNKEL)
    h2 = L(s, "h2", ("interaktiv, ohne Anmeldung\n(z. B. neue bash)", "interactive, no login\n(e.g. new bash)",
                     "interactiva, sin inicio\n(p. ej., nueva bash)", "交互式，无登录\n（例如新的 bash）",
                     "interactif, sans connexion\n(p. ex. nouvelle bash)", "etkileşimli, oturumsuz\n(ör. yeni bash)"),
           (xs[1], 1.4), FM, "center", DUNKEL)
    h3 = tt(s, "bash -c '…'", xs[2], 1.4, e, anker="m")

    def datei(x, y, n):
        return wort(s, x, y, n, e, GRAU, WEISS)
    c1 = [datei(xs[0], y, n) for y, n in zip(yb, ("/etc/profile", "~/.profile", "~/.bashrc"))]
    c2 = [datei(xs[1], y, n) for y, n in zip(yb[:2], ("/etc/bash.bashrc", "~/.bashrc"))]
    c3 = [box(s, (xs[2], yb[0]), 1.7, 0.36, HELLGRAU, WEISS, 2, "round", DASH),
          L(s, "keine", ("keine Startdatei", "no startup file", "ningún archivo de inicio", "没有启动文件", "aucun fichier de démarrage",
                         "başlangıç dosyası yok"), (xs[2], yb[0]), FM, "center", GRAU)]
    pa = [pf(s, (xs[0], yb[i] - 0.18), (xs[0], yb[i + 1] + 0.18), farbe=DUNKEL) for i in range(2)]
    pb_ = pf(s, (xs[1], yb[0] - 0.18), (xs[1], yb[1] + 0.18), farbe=DUNKEL)
    l_holt = L(s, "holt", ("holt nach", "reads it in", "lo carga", "读入", "le charge", "okutur"), (xs[0] + 0.12, (yb[1] + yb[2]) / 2),
               FX, "left", GRAU)
    schritt(s, EIN(h1, 0.5), WACHS(c1[0][0], 0.5), EIN(c1[0][1], 0.5))
    schritt(s, ZEICHNE(pa[0], 0.5), WACHS(c1[1][0], 0.5), EIN(c1[1][1], 0.5))
    schritt(s, ZEICHNE(pa[1], 0.5), WACHS(c1[2][0], 0.5), EIN([c1[2][1], l_holt], 0.5))
    s.pause(0.6)
    schritt(s, EIN(h2, 0.5), WACHS(c2[0][0], 0.5), EIN(c2[0][1], 0.5))
    schritt(s, ZEICHNE(pb_, 0.5), WACHS(c2[1][0], 0.5), EIN(c2[1][1], 0.5))
    s.pause(0.6)
    schritt(s, EIN(h3, 0.5), WACHS(c3[0], 0.5), EIN(c3[1], 0.5))
    s.speichern()


def k5dauerhaft():
    """1: export EDITOR=nano ans Ende von ~/.bashrc, laufende Shell unverändert; 2: neue Shell liest die Datei; 3: source."""
    s = Szene("linux/k5dauerhaft", reihenfolge="anlegen")
    fb = box(s, (0.0, 0.85), 3.0, 1.15, GRAU, WEISS, 2, "rect")
    hdr = tt(s, "~/.bashrc", -1.38, 1.25, E2, ORANGE)
    zl = [tt(s, "…", -1.38, 1.0, E2), tt(s, "alias l='ls -CF'", -1.38, 0.76, E2)]
    nz = tt(s, "export EDITOR=nano", -1.38, 0.52, E2, GRUEN)
    n1 = nummer(s, 1.75, 0.52, 1, ORANGE)
    run = pbox(s, (-2.15, -0.9), 2.5, 1.1)
    l_run = L(s, "lauf", ("laufende Shell", "running shell", "shell en ejecución", "正在运行的 Shell", "shell en cours",
                          "çalışan kabuk"), (-3.3, -0.5), FM, "left", BLAU)
    leer = schublade(s, -2.15, -0.92, "EDITOR", None, slot=4)
    l_ohne = L(s, "ohne", ("noch ohne EDITOR", "no EDITOR yet", "aún sin EDITOR", "还没有 EDITOR", "pas encore d'EDITOR",
                           "henüz EDITOR yok"), (-2.15, -1.28), FM, "center", GRAU)
    nsh = pbox(s, (2.15, -0.9), 2.5, 1.1)
    l_nsh = L(s, "neu", ("neue Shell", "new shell", "shell nueva", "新的 Shell", "nouveau shell", "yeni kabuk"), (1.0, -0.5), FX,
              "left", BLAU)
    d_neu = schublade(s, 2.15, -0.92, "EDITOR", "nano")
    a2 = pf(s, (0.9, 0.27), (1.75, -0.33), farbe=DUNKEL)
    l_liest = L(s, "liest", ("liest beim Start", "reads it at start", "lo lee al iniciar", "启动时读取", "la lit au démarrage",
                             "başlarken okur"), (1.55, 0.05), FM, "left", DUNKEL)
    n2 = nummer(s, 1.05, -0.12, 2, ORANGE)
    a3 = pf(s, (-0.9, 0.27), (-1.75, -0.33), farbe=GRUEN)
    l_src = tt(s, "source ~/.bashrc", -1.55, 0.05, E3, GRUEN, "r")
    n3 = nummer(s, -1.05, -0.12, 3, ORANGE)
    d_run = schublade(s, -2.15, -0.92, "EDITOR", "nano")
    schritt(s, WACHS(fb, 0.6), EIN([hdr] + zl, 0.6), WACHS(run, 0.6), EIN([l_run, l_ohne] + leer["alle"], 0.6))
    s.pause(0.6)
    schritt(s, EIN([nz] + n1, 0.6))
    schritt(s, BETONE(nz, 0.7))
    s.pause(0.6)
    schritt(s, WACHS(nsh, 0.6), EIN(l_nsh, 0.6))
    schritt(s, ZEICHNE(a2, 0.6), EIN([l_liest] + n2, 0.6))
    schritt(s, EIN(d_neu["alle"], 0.6))
    s.pause(0.6)
    schritt(s, ZEICHNE(a3, 0.6), EIN([l_src] + n3, 0.6))
    with s.gleichzeitig():
        schritt(s, EIN(d_run["alle"], 0.6), AUS(leer["alle"], 0.4))
        s.ersetzen(l_ohne, T(s, "mit", "jetzt mit EDITOR", "now with EDITOR", "ahora con EDITOR", "现在有 EDITOR",
                             "maintenant avec EDITOR", "artık EDITOR var"), farbe=GRUEN, dauer=0.6)
    s.speichern()


SZENEN = (k5expansion, k5versteckt, k5ohnetreffer, k5klammer, k5pfadmuster,
          k5variable, k5zuweisung, k5befehlsersetzung, k5rechnung,
          k5printf, k5worttrennung, k5entfernen, k5datensteuerung, k5werkstatt,
          k5kind, k5umgebung, k5export, k5vererbung, k5einbefehl,
          k5path, k5befehlssuche, k5punktslash, k5pathneu,
          k5startdatei, k5source, k5startdateien, k5dauerhaft)

if __name__ == "__main__":
    for f in SZENEN:
        f()
