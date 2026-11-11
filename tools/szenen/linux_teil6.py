"""Linux und Kommandozeile, Kapitel 6 „Textwerkzeuge und reguläre Ausdrücke“ (C:\\Bücher\\EtUndSo\\Linux\\Arbeitshefte\\
Kap6_Textwerkzeuge.tex, kap6_stufen.tex, kap6_stufen_b.tex): 34 Abbildungen, alle animiert (notizen/animationen.md §5).

Szenenname linux/k6<name> = \\label{fig:k6<name>} im Heft (\\szenenabb{k6<name>}{…}{fig:k6<name>}); Liste in uebergabe_kap6.md,
Abschnitt „Prüfer (Phase 2a)“. Zwei Hälften: Phase 2b-1 baut die 17 Szenen der Abschnitte 1–5 (SZENEN_1), Phase 2b-2 die 17
der Abschnitte 6–10 (SZENEN_2, unten anfügen). Stil wie linux_teil5.py, Helfer aus linux_hilfen.py: schreibmaschine("text")
(Terminalzeilen als s.text in Schreibmaschinenschrift, Dezimalpunkte bleiben Punkte), Szene(..., reihenfolge="anlegen")
(Hinterlegungen vor ihrem Text anlegen), s.ersetzen nur für Texte, die nicht bewegt werden.
Bilder: Zeilen des Lauftagebuchs laeufe.csv (LAEUFE) in Schreibmaschinenschrift; farbige Hinterlegung (mark) = hervorgehoben
(grün Treffer/Ergebnis, orange Trennzeichen/Schlüssel/Unterschied, blau Datum); weißer Schleier = ausgegraut; „Kopien“ sind
deckungsgleiche Zweitexemplare einer Zeile, die mit dem Original erscheinen und dann wandern (das Original bleibt stehen).
Koordinaten zwischen x = -3,45 und 3,45 (höchstens 548 px).
Bauen:  python tools/szenen/linux_teil6.py [k6name …]
Export: python tools/export_szenen.py <alle Namen aus SZENEN> --animiert
"""
import itertools
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from szenen_lib import *  # noqa: E402,F403

from linux_hilfen import *  # noqa: E402,F403  (gemeinsame Helfer der Linux-Kapitel)

schreibmaschine("text")
EM = 0.17                         # Höhe einer Terminalzeile (1 em) in Szeneneinheiten
setze_em(EM)
C = cw()                          # Breite eines Zeichens (0,08925)
E2 = 0.15                         # kleinere Zeilen (ganze Datensätze, Listen)
C2 = cw(E2)                       # 0,07875

LAEUFE = ("datum,name,km,minuten",
          "2026-11-02,Anna,5.0,28",
          "2026-11-02,Ben,10.5,62",
          "2026-11-03,Clara,7.2,41",
          "2026-11-04,Anna,6.4,35",
          "2026-11-05,Ben,5.0,31",
          "2026-11-06,Anna,12.0,70",
          "2026-11-07,Clara,8.0,44",
          "2026-11-08,Ben,21.1,128",
          "2026-11-09,Anna,5.0,27")


def r4(v):
    return round(v, 4)


def L(s, key, w, pos, g=FM, a="center", f=SCHWARZ, roh=None):
    """Beschriftung in sechs Sprachen; w = (de, en, es, zh, fr, tr)."""
    return text(s, T(s, key, *w), pos, g, a, f, roh=roh)


def box(s, mitte, b, h, rand=GRAU, fuellung=WEISS, dicke=2, form="round", dash="", deckung=1.0):
    return s.box("", (r4(mitte[0]), r4(mitte[1])), breite=r4(b), hoehe=r4(h), form=form, farbe=rand, fuellung=fuellung,
                 deckung=deckung, dicke=dicke, dash=dash)


def ttm(s, t, x, y, em=None, farbe=SCHWARZ):
    """Terminaltext, Mitte bei (x, y)."""
    return tt(s, t, x, y, em or EM, farbe, "m")


def mitte_tt(x0, t, em=None):
    """x der Mitte eines links bei x0 beginnenden Terminaltexts (Ziel für ZU)."""
    return r4(x0 + len(t) * cw(em or EM) / 2)


def felder(zeile):
    """Felder einer CSV-Zeile [(erste Spalte, letzte Spalte, Text)] und die Spalten ihrer Kommas."""
    fl, pos = [], 0
    for f in zeile.split(","):
        fl.append((pos, pos + len(f) - 1, f))
        pos += len(f) + 1
    return fl, [i for i, ch in enumerate(zeile) if ch == ","]


def bogen(s, xa, xb, y, h, farbe=GRUEN, dash="", dicke=2.5):
    """Sprungbogen über einem Zahlenstrahl von xa nach xb (Richtungsmarke in der Mitte)."""
    return s.weg(None, "%s+%s*t" % (r4(xa), r4(xb - xa)), "%s+%s*4*t*(1-t)" % (r4(y), r4(h)), 0, 1, farbe=farbe, dicke=dicke,
                 pfeile="0.55", n=41, dash=dash, spitze=0.1)


W_AUSG = ("Ausgabe:", "output:", "salida:", "输出：", "sortie :", "çıktı:")
W_EING = ("Eingabe:", "input:", "entrada:", "输入：", "entrée :", "girdi:")


# ================================================================== Abschnitt 1: Textdaten
def k6tabelle():
    """Tabelle mit drei Läufen (Datum, Name, km, Minuten); jede Tabellenzeile wird eine Textzeile mit Kommas; die Kommas
    leuchten (Trennzeichen), die Felder von 2026-11-02,Ben,10.5,62 bekommen die Nummern 1 bis 4."""
    s = Szene("linux/k6tabelle", reihenfolge="anlegen")
    zeilen = LAEUFE[1:4]
    breiten = (1.15, 0.8, 0.62, 0.95)
    xs, xl = [], -sum(breiten) / 2
    for b in breiten:
        xs.append(r4(xl + b / 2))
        xl += b
    rh, yk, yz = 0.3, 1.5, (1.2, 0.9, 0.6)
    kopf = (("Datum", "date", "fecha", "日期", "date", "tarih"), ("Name", "name", "nombre", "姓名", "nom", "ad"),
            ("km", "km", "km", "公里", "km", "km"), ("Minuten", "minutes", "minutos", "分钟", "minutes", "dakika"))
    zellen = []
    for j, b in enumerate(breiten):
        zellen.append(box(s, (xs[j], yk), b, rh, GRAU, GRAU_HELL, 1.5, "rect"))
        zellen += [box(s, (xs[j], y), b, rh, GRAU, WEISS, 1.5, "rect") for y in yz]
    t_kopf = [L(s, "k%d" % j, w, (xs[j], yk), FM, "center", DUNKEL) for j, w in enumerate(kopf)]
    x0 = r4(-len(zeilen[1]) * C / 2)
    yl = (-0.3, -0.85, -1.4)
    mk = []
    for z, y in zip(zeilen, yl):
        mk += [mark(s, sp(x0, k) - 0.01, sp(x0, k + 1) + 0.01, y, 0.24, ORANGE, 0.4) for k in felder(z)[1]]
    werte, kopien, kommata = [], [], []
    for i, z in enumerate(zeilen):
        fl, kommas = felder(z)
        werte += [ttm(s, f, xs[j], yz[i]) for j, (a, b, f) in enumerate(fl)]
        kopien.append([(ttm(s, f, xs[j], yz[i]), r4(msp(x0, a, b)), yl[i]) for j, (a, b, f) in enumerate(fl)])
        kommata.append([tt(s, ",", sp(x0, k), yl[i]) for k in kommas])
    l_text = L(s, "text", ("als Text:", "as text:", "como texto:", "作为文本：", "en texte :", "metin olarak:"), (x0, 0.02),
               FM, "left", GRAU)
    nummern = []
    for n, (a, b, f) in enumerate(felder(zeilen[1])[0], 1):
        x = r4(msp(x0, a, b))
        nummern += [s.kreis(None, x, -0.64, 0.1, farbe=BLAU, dicke=2, fuellung=WEISS, deckung=1.0),
                    text(s, str(n), (x, -0.64), FM, "center", BLAU)]
    xr = r4(x0 + 22 * C + 0.25)
    l_komma = L(s, "komma", ("Komma = Trennzeichen", "comma = separator", "coma = separador", "逗号 = 分隔符",
                             "virgule = séparateur", "virgül = ayırıcı"), (xr, yl[0]), FM, "left", ORANGE)
    l_ds = L(s, "ds", ("ein Datensatz, 4 Felder", "one record, 4 fields", "un registro, 4 campos", "一条记录，4 个字段",
                       "un enregistrement, 4 champs", "bir kayıt, 4 alan"), (xr, yl[1]), FM, "left", BLAU)
    schritt(s, EIN(zellen + t_kopf + werte + [k[0] for r in kopien for k in r], 0.8))
    s.pause(0.6)
    schritt(s, EIN(l_text, 0.4))
    for i in range(3):
        schritt(s, *[ZU(k, x, y, 0.8) for k, x, y in kopien[i]], EIN(kommata[i], 0.8))
    s.pause(0.6)
    schritt(s, EIN(mk, 0.6), BETONE(flach(kommata), 0.8), EIN(l_komma, 0.6))
    s.pause(0.6)
    schritt(s, EIN(nummern, 0.7), EIN(l_ds, 0.7))
    s.speichern()


def k6zeilenende():
    """Ende der Zeile 2026-11-02,Anna,5.0,28 als Bytes: Linux …8, 10; Windows …8, 13, 10. Die 13 leuchtet auf; Klammer: das
    letzte Feld ist 28 plus ein unsichtbares Zeichen."""
    s = Szene("linux/k6zeilenende", reihenfolge="anlegen")
    em = 0.19
    l_z = L(s, "zeile", ("Zeile:", "line:", "línea:", "行：", "ligne :", "satır:"), (-1.2, 1.45), FM, "right", GRAU)
    t_z = tt(s, "2026-11-02,Anna,5.0,28", -1.08, 1.45)
    yL, yW, d = 0.75, -0.35, 0.42
    xs = [r4(-1.3 + 0.47 * i) for i in range(8)]
    zeichen = ("5", ".", "0", ",", "2", "8")
    l_lin = L(s, "lin", ("Linux-Datei", "Linux file", "archivo Linux", "Linux 文件", "fichier Linux", "Linux dosyası"),
              (-3.35, yL), FK, "left")
    l_win = L(s, "win", ("Windows-Datei", "Windows file", "archivo Windows", "Windows 文件", "fichier Windows",
                         "Windows dosyası"), (-3.35, yW), FK, "left")
    gleich = []
    for y in (yL, yW):
        gleich.append(ttm(s, "…", -1.76, y, em, GRAU))
        for c, x in zip(zeichen, xs):
            gleich += [box(s, (x, y), d, d, HELLGRAU, WEISS, 1.5, "rect"), ttm(s, c, x, y, em, GRAU)]
    b10L = [box(s, (xs[6], yL), d, d, BLAU, BLAU_HELL, 2, "rect"), ttm(s, "10", xs[6], yL, em)]
    b13 = box(s, (xs[6], yW), d, d, BLAU, BLAU_HELL, 2, "rect")
    hl13 = box(s, (xs[6], yW), d, d, ORANGE, ORANGE_HELL, 2.5, "rect")
    t13 = ttm(s, "13", xs[6], yW, em)
    b10W = [box(s, (xs[7], yW), d, d, BLAU, BLAU_HELL, 2, "rect"), ttm(s, "10", xs[7], yW, em)]
    w_ze = ("Zeilenende", "newline", "fin de línea", "换行", "fin de ligne", "satır sonu")
    l_zeL = L(s, "zeL", w_ze, (xs[6] + 0.32, yL), FM, "left", BLAU)
    l_zeW = L(s, "zeW", w_ze, (xs[7] + 0.32, yW), FM, "left", BLAU)
    l_wr = L(s, "wr", ("Wagenrücklauf", "carriage return", "retorno de carro", "回车", "retour chariot", "satır başı karakteri"),
             (xs[6], 0.2), FM, "center", ORANGE)
    kl = klammer(s, xs[4] - d / 2, xs[6] + d / 2, yW - 0.32, unten=True, farbe=ORANGE, t=0.07)
    l_kl = L(s, "feld", ("letztes Feld: 28 + unsichtbares Zeichen", "last field: 28 + invisible character",
                         "último campo: 28 + carácter invisible", "最后一个字段：28 + 不可见字符",
                         "dernier champ : 28 + caractère invisible", "son alan: 28 + görünmez karakter"),
             (r4((xs[4] + xs[6]) / 2), yW - 0.58), FM, "center", ORANGE)
    schritt(s, EIN([l_z, t_z, l_lin, l_win] + gleich, 0.7))
    s.pause(0.6)
    schritt(s, EIN(b10L + [l_zeL], 0.6))
    schritt(s, EIN([b13, t13] + b10W + [l_zeW], 0.6))
    s.pause(0.6)
    schritt(s, EIN(hl13, 0.5), BETONE(t13, 0.8), EIN(l_wr, 0.6))
    s.pause(0.6)
    schritt(s, ZEICHNE(kl, 0.6), EIN(l_kl, 0.7))
    s.speichern()


def k6ausschnitt():
    """Die zehn Zeilen zweimal: tail -n +8 zählt bis Zeile 8 und nimmt den Rest (8–10); head -n -7 zählt 7 vom Ende und nimmt
    alles davor (1–3)."""
    s = Szene("linux/k6ausschnitt", reihenfolge="anlegen")
    y0, dz = 1.2, 0.21
    ys = [r4(y0 - i * dz) for i in range(10)]
    xl, xr = -2.95, 0.55
    bz = 23 * C2

    def gruen(x0, idx):
        return [mark(s, x0 - 0.04, x0 + bz + 0.04, ys[i], 0.2, GRUEN, 0.28) for i in idx]
    gL, gR = gruen(xl, range(7, 10)), gruen(xr, range(3))
    stapel = []
    for x0 in (xl, xr):
        stapel += [tt(s, str(i + 1), x0 - 0.07, y, E2, GRAU, "r") for i, y in enumerate(ys)]
        stapel += [tt(s, z, x0, y, E2) for z, y in zip(LAEUFE, ys)]

    def schl(x0, i, j):
        return schleier(s, (r4(x0 + 0.8), r4((ys[i] + ys[j]) / 2)), 2.25, r4(ys[i] - ys[j] + 0.22))
    sL, sR = schl(xl, 0, 6), schl(xr, 3, 9)
    c_l = tt(s, "tail -n +8", xl, 1.58)
    c_r = tt(s, "head -n -7", xr, 1.58)
    xa_l, xa_r = r4(xl + bz + 0.17), r4(xr + bz + 0.17)
    a_l = pf(s, (xa_l, ys[0] + 0.05), (xa_l, ys[7]), farbe=ORANGE, spitze=0.1)
    a_r = pf(s, (xa_r, ys[9] - 0.05), (xa_r, ys[3]), farbe=ORANGE, spitze=0.1)
    l_al = L(s, "bis8", ("bis\nZeile 8", "up to\nline 8", "hasta la\nlínea 8", "数到\n第 8 行", "jusqu'à\nla ligne 8",
                         "8. satıra\nkadar"), (xa_l + 0.12, r4((ys[0] + ys[7]) / 2)), FM, "left", ORANGE)
    l_ar = L(s, "vom7", ("7 vom\nEnde", "7 from\nthe end", "7 desde\nel final", "从末尾\n数 7 行", "7 depuis\nla fin",
                         "sondan\n7 satır"), (xa_r + 0.12, r4((ys[3] + ys[9]) / 2)), FM, "left", ORANGE)
    r_l = L(s, "z810", ("Zeilen 8 bis 10", "lines 8 to 10", "líneas 8 a 10", "第 8 到 10 行", "lignes 8 à 10",
                        "8. ile 10. satırlar"), (r4(xl + bz / 2), -1.02), FK, "center", GRUEN)
    r_r = L(s, "z13", ("Zeilen 1 bis 3", "lines 1 to 3", "líneas 1 a 3", "第 1 到 3 行", "lignes 1 à 3",
                       "1. ile 3. satırlar"), (r4(xr + bz / 2), -1.02), FK, "center", GRUEN)
    schritt(s, EIN(stapel, 0.6))
    s.pause(0.6)
    schritt(s, EIN(c_l, 0.4))
    schritt(s, ZEICHNE(a_l, 1.0), EIN(l_al, 0.6))
    schritt(s, EIN([sL] + gL + [r_l], 0.6))
    s.pause(0.6)
    schritt(s, EIN(c_r, 0.4))
    schritt(s, ZEICHNE(a_r, 1.0), EIN(l_ar, 0.6))
    schritt(s, EIN([sR] + gR + [r_r], 0.6))
    s.speichern()


def k6tailf():
    """Datei neu.csv als Zeilenstapel, Terminal mit tail -n 2 -f: die letzten zwei Zeilen erscheinen, tail wartet, eine neue
    Zeile wird angehängt und erscheint sofort im Terminal; Strg+C beendet."""
    s = Szene("linux/k6tailf", reihenfolge="anlegen")
    x0 = -3.25
    yd = (1.0, 0.75, 0.5, 0.25, 0.0)
    neu = "2026-11-10,Clara,6.0,33"
    fbox = box(s, (-2.3, 0.45), 2.1, 1.5, GRAU, WEISS, 2, "rect")
    l_f = tt(s, "neu.csv", -2.3, 1.42, E2, GRAU, "m")
    mk_neu = mark(s, x0 - 0.04, x0 + len(neu) * C2 + 0.04, yd[4], 0.21, GRUEN, 0.3)
    alt = [tt(s, "…", x0, yd[0], E2, GRAU)] + [tt(s, z, x0, y, E2) for z, y in zip(LAEUFE[7:10], yd[1:4])]
    t_neu = tt(s, neu, x0, yd[4], E2)
    tk = term_kasten(s, (1.95, 0.3), 2.7, 1.9)
    xt, yt = 0.72, (1.0, 0.75, 0.5, 0.25, 0.0)
    t_cmd = tt(s, "$ tail -n 2 -f neu.csv", xt, yt[0], E2)
    kop = [tt(s, z, x0, y, E2) for z, y in zip(LAEUFE[8:10], yd[2:4])]
    kop_neu = tt(s, neu, x0, yd[4], E2)
    cursor = box(s, (xt + 0.04, yt[3]), 0.08, 0.16, DUNKEL, DUNKEL, 0, "rect")
    t_c = tt(s, "^C", xt, yt[4], E2, ORANGE)
    a = pf(s, (-1.18, 0.45), (0.52, 0.45), farbe=GRAU, spitze=0.1)
    l_wait = L(s, "wartet", ("tail wartet auf neue Zeilen", "tail waits for new lines", "tail espera líneas nuevas",
                             "tail 等待新行", "tail attend de nouvelles lignes", "tail yeni satırları bekler"),
               (1.95, -0.86), FM, "center", GRAU)
    l_strg = L(s, "strgc", ("Strg+C beendet tail", "Ctrl+C ends tail", "Ctrl+C termina tail", "Ctrl+C 结束 tail",
                            "Ctrl+C arrête tail", "Ctrl+C tail'i sonlandırır"), (1.95, -0.86), FM, "center", ORANGE)
    l_neu = L(s, "angeh", ("angehängt (zweites Terminal)", "appended (second terminal)", "añadida (segundo terminal)",
                           "追加（第二个终端）", "ajoutée (second terminal)", "eklendi (ikinci terminal)"),
              (-2.3, -0.5), FM, "center", GRUEN)
    schritt(s, EIN([fbox, l_f] + alt + kop + [tk, t_cmd], 0.7))
    s.pause(0.6)
    schritt(s, ZEICHNE(a, 0.6), *[ZU(k, mitte_tt(xt, z, E2), y, 0.9) for k, z, y in zip(kop, LAEUFE[8:10], yt[1:3])])
    s.pause(0.6)
    schritt(s, EIN([cursor, l_wait], 0.5))
    schritt(s, BETONE(cursor, 0.6))
    schritt(s, BETONE(cursor, 0.6))
    s.pause(0.4)
    schritt(s, EIN([mk_neu, t_neu, kop_neu, l_neu], 0.6))
    schritt(s, ZU(kop_neu, mitte_tt(xt, neu, E2), yt[3], 0.8), AUS(cursor, 0.4))
    s.pause(0.6)
    schritt(s, EIN([t_c, l_strg], 0.6), AUS(l_wait, 0.4))
    s.speichern()


# ================================================================== Abschnitt 2: cut, tr, paste
def k6cut():
    """cut -d, -f2: Zeilen an den Kommas zerlegt, Feld 2 leuchtet und rückt als Spalte nach rechts; der Rest wird grau."""
    s = Szene("linux/k6cut", reihenfolge="anlegen")
    x0, y0, dz = -3.3, 1.05, 0.22
    ys = [r4(y0 - i * dz) for i in range(10)]
    xo = 0.6
    info = [felder(z) for z in LAEUFE]
    mk = []
    for (fl, _), y in zip(info, ys):
        a, b, _t = fl[1]
        mk.append(mark(s, sp(x0, a, E2) - 0.03, sp(x0, b + 1, E2) + 0.03, y, 0.2, GRUEN, 0.3))
    t_cmd = tt(s, "$ cut -d, -f2 laeufe.csv", x0, 1.48, E2)
    f2, rest, kom = [], [], []
    for (fl, kommas), y in zip(info, ys):
        for j, (a, b, t) in enumerate(fl):
            (f2 if j == 1 else rest).append(tt(s, t, sp(x0, a, E2), y, E2))
        kom += [tt(s, ",", sp(x0, k, E2), y, E2) for k in kommas]
    sch = schleier(s, (-2.39, 0.06), 1.98, 2.22)
    a = pf(s, (-1.25, 1.48), (0.45, 1.48), farbe=GRUEN, spitze=0.1)
    l_aus = L(s, "aus", ("Ausgabe: Feld 2", "output: field 2", "salida: campo 2", "输出：第 2 个字段", "sortie : champ 2",
                         "çıktı: 2. alan"), (0.55, 1.48), FM, "left", GRUEN)
    ziele = []
    for (fl, _), y, t, m in zip(info, ys, f2, mk):
        xm = mitte_tt(xo, fl[1][2], E2)
        ziele += [ZU(t, xm, y, 1.0), ZU(m, xm, y, 1.0)]
    schritt(s, EIN([t_cmd] + f2 + rest + kom, 0.6))
    s.pause(0.6)
    schritt(s, BETONE(kom, 0.8))
    s.pause(0.6)
    schritt(s, EIN(mk, 0.6), BETONE(f2, 0.8))
    s.pause(0.6)
    schritt(s, *ziele)
    schritt(s, EIN(sch, 0.6), ZEICHNE(a, 0.6), EIN(l_aus, 0.6))
    s.speichern()


def k6tr():
    """tr a-z A-Z als Zuordnung a b c … z → A B C … Z; die Zeile 2026-11-02,Anna,5.0,28 läuft Stück für Stück hindurch:
    n, n, a werden N, N, A, alles andere bleibt."""
    s = Szene("linux/k6tr", reihenfolge="anlegen")
    em = 0.19
    oben = ("a", "b", "c", "…", "n", "…", "z")
    unten = ("A", "B", "C", "…", "N", "…", "Z")
    xm = [r4(0.35 + 0.43 * i) for i in range(7)]
    yo, yu = 0.55, -0.3
    t_cmd = ttm(s, "tr a-z A-Z", 1.64, 1.4)
    l_m1 = L(s, "m1", ("erste Menge", "first set", "primer conjunto", "第一个集合", "premier ensemble", "birinci küme"),
             (1.64, 0.95), FM, "center", GRAU)
    l_m2 = L(s, "m2", ("zweite Menge", "second set", "segundo conjunto", "第二个集合", "second ensemble", "ikinci küme"),
             (1.64, -0.72), FM, "center", GRAU)
    to = [ttm(s, c, x, yo, em, GRAU if c == "…" else SCHWARZ) for c, x in zip(oben, xm)]
    tu = [ttm(s, c, x, yu, em, GRAU if c == "…" else SCHWARZ) for c, x in zip(unten, xm)]
    pfe = {i: pf(s, (x, yo - 0.15), (x, yu + 0.16), farbe=GRAU, dicke=2, spitze=0.08)
           for i, (c, x) in enumerate(zip(oben, xm)) if c != "…"}
    x0, yi, ya = -3.3, 0.95, -0.72
    stuecke_ = (("2026-11-02,", None), ("A", None), ("n", 4), ("n", 4), ("a", 0), (",5.0,28", None))
    l_ein = L(s, "ein", W_EING, (x0, 1.3), FM, "left", GRAU)
    l_aus = L(s, "aus", W_AUSG, (x0, -1.05), FM, "left", GRAU)
    ein, aus, col = [], [], 0
    for t, idx in stuecke_:
        ein.append(tt(s, t, sp(x0, col), yi))
        aus.append(tt(s, t.upper() if idx is not None else t, sp(x0, col), ya, farbe=ORANGE if idx is not None else SCHWARZ))
        col += len(t)
    a = pf(s, (-2.35, 0.75), (-2.35, -0.5), farbe=GRAU, spitze=0.12)
    l_zfz = L(s, "zfz", ("Zeichen für Zeichen", "character by character", "carácter a carácter", "逐个字符",
                         "caractère par caractère", "karakter karakter"), (-2.2, 0.13), FM, "left", GRAU)
    l_leg = L(s, "leg", ("orange: ersetzt", "orange: replaced", "naranja: sustituido", "橙色：已替换", "orange : remplacé",
                         "turuncu: değiştirildi"), (x0, -1.35), FM, "left", ORANGE)
    schritt(s, EIN([t_cmd, l_m1] + to, 0.6))
    schritt(s, EIN([l_m2] + tu, 0.6), ZEICHNE(list(pfe.values()), 0.6))
    s.pause(0.6)
    schritt(s, EIN([l_ein, l_aus] + ein, 0.6), ZEICHNE(a, 0.6), EIN(l_zfz, 0.6))
    s.pause(0.4)
    for k, (t, idx) in enumerate(stuecke_):
        teile = [BETONE(ein[k], 0.6), EIN(aus[k], 0.6)]
        if idx is not None:
            teile.append(BETONE([to[idx], tu[idx], pfe[idx]], 0.6))
        schritt(s, *teile)
    schritt(s, EIN(l_leg, 0.5))
    s.speichern()


def k6paste():
    """paste namen.txt minuten.txt: je eine Zeile links und rechts werden eine Zeile mit Tabulator dazwischen; darunter
    tail -n +2 namen.txt | paste -s -d,: die Spalte der neun Namen wird zu einer Zeile."""
    s = Szene("linux/k6paste", reihenfolge="anlegen")
    xa, xb, xo = -3.3, -2.2, -0.55
    xo2 = r4(xo + 8 * C2)
    t_c1 = tt(s, "$ paste namen.txt minuten.txt", xa, 1.75, E2)
    l_a = tt(s, "namen.txt", xa, 1.47, E2, GRAU)
    l_b = tt(s, "minuten.txt", xb, 1.47, E2, GRAU)
    l_aus = L(s, "aus", W_AUSG, (xo, 1.47), FM, "left", GRAU)
    links = ("name", "Anna", "Ben", "Clara", "…")
    rechts = ("minuten", "28", "62", "41", "…")
    yr = (1.22, 1.0, 0.78, 0.56, 0.34)
    ta = [tt(s, w, xa, y, E2) for w, y in zip(links, yr)]
    tb = [tt(s, w, xb, y, E2) for w, y in zip(rechts, yr)]
    ka = [tt(s, w, xa, y, E2) for w, y in zip(links, yr)]
    kb = [tt(s, w, xb, y, E2) for w, y in zip(rechts, yr)]
    tabs = [pf(s, (r4(xo + len(w) * C2 + 0.05), y), (r4(xo2 - 0.04), y), farbe=ORANGE, dicke=2.5, spitze=0.07)
            for w, y in zip(links[:4], yr[:4])]
    l_tab = L(s, "tab", ("Tabulator", "tab", "tabulador", "制表符", "tabulation", "sekme"), (r4(xo2 + 7 * C2 + 0.2), yr[0]),
              FM, "left", ORANGE)
    namen = [z.split(",")[1] for z in LAEUFE[1:]]
    zeile = ",".join(namen)
    t_c2 = tt(s, "$ tail -n +2 namen.txt | paste -s -d,", xa, -0.05, E2)
    yc = [r4(-0.33 - i * 0.19) for i in range(9)]
    tc = [tt(s, n, xa, y, E2) for n, y in zip(namen, yc)]
    kc = [tt(s, n, xa, y, E2) for n, y in zip(namen, yc)]
    xr0, yrow = -2.45, -1.1
    l_aus2 = L(s, "aus2", W_AUSG, (xr0, -0.83), FM, "left", GRAU)
    ziele, col = [], 0
    for n in namen:
        ziele.append(r4(sp(xr0, col, E2) + len(n) * C2 / 2))
        col += len(n) + 1
    kom = [tt(s, ",", sp(xr0, k, E2), yrow, E2, ORANGE) for k, ch in enumerate(zeile) if ch == ","]
    schritt(s, EIN([t_c1, l_a, l_b] + ta + tb + ka + kb, 0.6))
    s.pause(0.6)
    schritt(s, EIN(l_aus, 0.4))
    for r in range(5):
        teile = [ZU(ka[r], mitte_tt(xo, links[r], E2), yr[r], 0.55), ZU(kb[r], mitte_tt(xo2, rechts[r], E2), yr[r], 0.55)]
        if r < 4:
            teile.append(ZEICHNE(tabs[r], 0.55))
        schritt(s, *teile)
    schritt(s, EIN(l_tab, 0.5))
    s.pause(0.6)
    schritt(s, EIN([t_c2] + tc + kc, 0.6))
    s.pause(0.6)
    schritt(s, *[ZU(k, x, yrow, 1.2) for k, x in zip(kc, ziele)], EIN([l_aus2] + kom, 1.2))
    s.speichern()


def k6minuten():
    """Rechenbild: 28 + 62 + 41 + 35 + 31 + 70 + 44 + 128 + 27; unter jedem Summanden die Zwischensumme 28, 90, …, 466."""
    s = Szene("linux/k6minuten", reihenfolge="anlegen")
    werte = (28, 62, 41, 35, 31, 70, 44, 128, 27)
    summen = list(itertools.accumulate(werte))
    xs = [r4(-2.95 + 0.74 * i) for i in range(9)]
    y1, y2 = 0.45, -0.35
    l1 = L(s, "min", ("Minuten", "minutes", "minutos", "分钟", "minutes", "dakika"), (-3.3, 0.9), FM, "left", GRAU)
    l2 = L(s, "zw", ("Zwischensummen", "running totals", "sumas parciales", "部分和", "sommes partielles", "ara toplamlar"),
           (-3.3, -0.78), FM, "left", GRUEN)
    rb = box(s, (xs[8], y2), 0.62, 0.38, BLAU, BLAU_HELL, 2.5)
    tw = [text(s, str(w), (x, y1), FS) for w, x in zip(werte, xs)]
    tp = [text(s, "+", (r4(x + 0.37), y1), FS, "center", GRAU) for x in xs[:-1]]
    vp = [pf(s, (x, y1 - 0.16), (x, y2 + 0.17), farbe=HELLGRAU, dicke=2, spitze=0.08) for x in xs]
    hp = [pf(s, (r4(xs[i - 1] + 0.22), y2), (r4(xs[i] - 0.22), y2), farbe=HELLGRAU, dicke=2, spitze=0.08) for i in range(1, 9)]
    ts = [text(s, str(v), (x, y2), FS, "center", GRUEN if i < 8 else BLAU) for i, (v, x) in enumerate(zip(summen, xs))]
    l_end = L(s, "end", ("466 Minuten = 7 Stunden 46 Minuten", "466 minutes = 7 hours 46 minutes",
                         "466 minutos = 7 horas 46 minutos", "466 分钟 = 7 小时 46 分钟", "466 minutes = 7 heures 46 minutes",
                         "466 dakika = 7 saat 46 dakika"), (3.3, -0.95), FK, "right", BLAU)
    schritt(s, EIN(tw + tp + [l1], 0.8))
    s.pause(0.6)
    schritt(s, ZEICHNE(vp[0], 0.5), EIN([ts[0], l2], 0.5), BETONE(tw[0], 0.6))
    for i in range(1, 9):
        schritt(s, ZEICHNE([vp[i], hp[i - 1]], 0.5), EIN(ts[i], 0.5), BETONE([tw[i], ts[i - 1]], 0.6))
    s.pause(0.6)
    schritt(s, EIN([rb, l_end], 0.7))
    s.speichern()


# ================================================================== Abschnitt 3: sort und uniq
def k6lexnum():
    """sort vergleicht 10.5 und 5.0 Zeichen für Zeichen (1 < 5: 10.5 zuerst); sort -n vergleicht die Werte (5,0 < 10,5)."""
    s = Szene("linux/k6lexnum", reihenfolge="anlegen")
    em = 0.19
    xo = 1.75
    t_s = tt(s, "sort", -3.3, 1.55)
    l_s = L(s, "zz", ("vergleicht Zeichen für Zeichen", "compares character by character", "compara carácter a carácter",
                      "逐个字符比较", "compare caractère par caractère", "karakter karakter karşılaştırır"),
            (-2.8, 1.55), FM, "left", GRAU)
    xc = [r4(-3.1 + 0.38 * i) for i in range(4)]
    ya, yb = 1.08, 0.66
    zellen = [box(s, (x, ya), 0.32, 0.32, GRAU, WEISS, 1.5, "rect") for x in xc]
    zellen += [box(s, (x, yb), 0.32, 0.32, GRAU, WEISS, 1.5, "rect") for x in xc[:3]]
    ta = [ttm(s, c, x, ya, em) for c, x in zip("10.5", xc)]
    tb = [ttm(s, c, x, yb, em) for c, x in zip("5.0", xc)]
    rh = rahmen(s, (xc[0], r4((ya + yb) / 2)), 0.46, 0.84)
    l_1 = L(s, "erst", ("erstes Zeichen: 1 < 5", "first character: 1 < 5", "primer carácter: 1 < 5", "第一个字符：1 < 5",
                        "premier caractère : 1 < 5", "ilk karakter: 1 < 5"), (-1.35, r4((ya + yb) / 2)), FM, "left", ORANGE)
    l_o1 = L(s, "aus1", W_AUSG, (xo, 1.25), FM, "left", GRAU)
    o1 = [tt(s, "10.5", xo, 0.98), tt(s, "5.0", xo, 0.73)]
    sep = linie(s, (-3.3, 0.25), (3.3, 0.25), HELLGRAU, 1.5)
    t_n = tt(s, "sort -n", -3.3, -0.08)
    l_n = L(s, "wert", ("vergleicht Zahlenwerte", "compares numeric values", "compara valores numéricos", "比较数值",
                        "compare des valeurs numériques", "sayısal değerleri karşılaştırır"), (-2.55, -0.08), FM, "left", GRAU)
    ya2 = -0.95

    def X(v):
        return r4(-3.0 + v * 0.32)
    achse = [pf(s, (X(0) - 0.08, ya2), (X(11) + 0.1, ya2), farbe=GRAU, dicke=2, spitze=0.1)]
    achse += [linie(s, (X(v), ya2 - 0.05), (X(v), ya2 + 0.05), GRAU, 2) for v in (0, 5, 10)]
    achse += [text(s, str(v), (X(v), ya2 - 0.22), FM, "center", GRAU) for v in (0, 5, 10)]
    pkt = [s.punkt(None, X(5.0), ya2, BLAU, 0.06), s.punkt(None, X(10.5), ya2, BLAU, 0.06)]
    vw = [text(s, "5.0", (X(5.0), ya2 + 0.22), FK, "center", BLAU), text(s, "10.5", (X(10.5), ya2 + 0.22), FK, "center", BLAU)]
    l_kl = L(s, "kl", ("5.0 < 10.5",) * 6, (X(5.5), -1.52), FM, "center", ORANGE)
    l_o2 = L(s, "aus2", W_AUSG, (xo, -0.33), FM, "left", GRAU)
    o2 = [tt(s, "5.0", xo, -0.6), tt(s, "10.5", xo, -0.85)]
    schritt(s, EIN([t_s, l_s] + zellen + ta + tb, 0.7))
    s.pause(0.6)
    schritt(s, EIN([rh, l_1], 0.6), BETONE([ta[0], tb[0]], 0.8))
    schritt(s, EIN([l_o1] + o1, 0.6))
    s.pause(0.6)
    schritt(s, EIN([sep, t_n, l_n] + achse, 0.7))
    schritt(s, WACHS(pkt, 0.6), EIN(vw, 0.6))
    schritt(s, EIN([l_kl, l_o2] + o2, 0.6))
    s.speichern()


def k6schluessel():
    """sort -t, -k3,3n: Feld 3 jedes Datensatzes ist hinterlegt (Schlüssel); die ganzen Zeilen wandern an ihre Plätze, bei
    den drei Läufen über 5.0 km entscheidet die ganze Zeile (Datum hervorgehoben)."""
    s = Szene("linux/k6schluessel", reihenfolge="anlegen")
    daten = LAEUFE[1:]
    sortiert = sorted(daten, key=lambda z: (float(z.split(",")[2]), z))
    xl, xr = -3.35, 0.2
    ys = [r4(1.0 - i * 0.24) for i in range(9)]

    def schl(z, x0, y):
        a, b, _t = felder(z)[0][2]
        return mark(s, sp(x0, a, E2) - 0.02, sp(x0, b + 1, E2) + 0.02, y, 0.21, ORANGE, 0.4)
    mL = [schl(z, xl, y) for z, y in zip(daten, ys)]
    mK = [schl(z, xl, y) for z, y in zip(daten, ys)]
    dat = [mark(s, xr - 0.02, sp(xr, 10, E2) + 0.02, ys[k], 0.21, BLAU, 0.3) for k in range(3)]
    tL = [tt(s, z, xl, y, E2) for z, y in zip(daten, ys)]
    tK = [tt(s, z, xl, y, E2) for z, y in zip(daten, ys)]
    l_ds = L(s, "ds", ("Datensätze", "records", "registros", "记录", "enregistrements", "kayıtlar"), (xl, 1.4), FM, "left", GRAU)
    l_key = L(s, "key", ("Schlüssel: Feld 3", "key: field 3", "clave: campo 3", "键：第 3 个字段", "clé : champ 3",
                         "anahtar: 3. alan"), (-1.4, 1.4), FM, "right", ORANGE)
    t_sort = tt(s, "sort -t, -k3,3n", xr, 1.4)
    a = pf(s, (-1.25, 1.4), (0.08, 1.4), farbe=GRAU, spitze=0.1)
    xk = r4(xr + 22 * C2 + 0.12)
    kl = vklammer(s, xk, ys[0] + 0.1, ys[2] - 0.1, farbe=BLAU)
    l_gl = L(s, "gleich", ("gleiche Strecke:\nganze Zeile\nentscheidet", "same distance:\nthe whole line\ndecides",
                           "misma distancia:\ndecide la\nlínea entera", "距离相同：\n由整行\n决定",
                           "même distance :\nla ligne\nentière décide", "aynı mesafe:\ntüm satır\nbelirler"),
             (r4(xk + 0.1), ys[1]), FM, "left", BLAU)
    ziele = []
    for z, t, m in zip(daten, tK, mK):
        k = sortiert.index(z)
        a3, b3, _t = felder(z)[0][2]
        ziele += [ZU(t, mitte_tt(xr, z, E2), ys[k], 1.4), ZU(m, r4((sp(xr, a3, E2) + sp(xr, b3 + 1, E2)) / 2), ys[k], 1.4)]
    schritt(s, EIN([l_ds] + tL + tK, 0.6))
    s.pause(0.6)
    schritt(s, EIN(mL + mK + [l_key], 0.7))
    s.pause(0.6)
    schritt(s, EIN(t_sort, 0.5), ZEICHNE(a, 0.5))
    schritt(s, *ziele)
    s.pause(0.6)
    schritt(s, EIN(dat, 0.6), ZEICHNE(kl, 0.6), EIN(l_gl, 0.7))
    s.speichern()


def k6uniq():
    """uniq -c mit einem Merkzettel (vorige Zeile, Zähler): ungeordnet Anna Ben Clara Anna → jede Zeile 1; geordnet
    Anna×4 Ben×3 Clara×2 → 4, 3, 2."""
    s = Szene("linux/k6uniq", reihenfolge="anlegen")
    t_cmd = ttm(s, "uniq -c", 0.1, 1.88)
    trenn = linie(s, (0.12, 1.6), (0.12, -0.85), HELLGRAU, 1.5)
    dz = 0.21
    tafeln = []
    for key, ox, folge, titel in (
            ("u", -3.1, ("Anna", "Ben", "Clara", "Anna"),
             ("ungeordnet", "unsorted", "desordenado", "未排序", "non trié", "sırasız")),
            ("g", 0.45, ("Anna",) * 4 + ("Ben",) * 3 + ("Clara",) * 2,
             ("geordnet", "sorted", "ordenado", "已排序", "trié", "sıralı"))):
        xz = r4(ox + 1.4)
        yi = [r4(0.95 - i * dz) for i in range(len(folge))]
        gruppen = [(len(list(g)), n) for n, g in itertools.groupby(folge)]
        tafeln.append({
            "rahmen": [L(s, key + "t", titel, (xz, 1.52), FK, "center", DUNKEL),
                       L(s, key + "e", W_EING, (ox, 1.22), FM, "left", GRAU),
                       L(s, key + "a", W_AUSG, (r4(ox + 2.15), 1.22), FM, "left", GRAU),
                       L(s, key + "m", ("Merkzettel", "note", "nota", "便签", "pense-bête", "not"), (xz, 0.92), FM, "center",
                         GRAU),
                       box(s, (xz, 0.55), 1.05, 0.4, GRAU, GELB, 1.5, "rect"),
                       L(s, key + "lz", ("Zeile", "line", "línea", "行", "ligne", "satır"), (r4(xz - 0.2), 0.21), FM, "center",
                         GRAU),
                       L(s, key + "lc", ("Zähler", "counter", "contador", "计数", "compteur", "sayaç"), (r4(xz + 0.33), 0.21),
                         FM, "center", GRAU)],
            "inp": [tt(s, n, ox, y) for n, y in zip(folge, yi)],
            "ptr": pf(s, (r4(ox - 0.3), yi[0]), (r4(ox - 0.07), yi[0]), farbe=ORANGE, dicke=3, spitze=0.08),
            "name": ttm(s, folge[0], r4(xz - 0.2), 0.55),
            "cnt": ttm(s, "1", r4(xz + 0.33), 0.55, farbe=ORANGE),
            "out": [tt(s, "%d %s" % g, r4(ox + 2.15), r4(0.95 - k * dz)) for k, g in enumerate(gruppen)],
            "folge": folge})
    schritt(s, EIN(t_cmd, 0.5))
    for T_ in tafeln:
        folge = T_["folge"]
        s.pause(0.6)
        schritt(s, EIN(T_["rahmen"] + T_["inp"], 0.6))
        schritt(s, EIN([T_["ptr"], T_["name"], T_["cnt"]], 0.45), BETONE(T_["inp"][0], 0.5))
        prev, n, k = folge[0], 1, 0
        for i in range(1, len(folge)):
            with s.gleichzeitig():
                schritt(s, VER(T_["ptr"], 0, -dz, 0.45), BETONE(T_["inp"][i], 0.5))
                if folge[i] == prev:
                    n += 1
                    s.ersetzen(T_["cnt"], str(n), dauer=0.45)
                else:
                    schritt(s, EIN(T_["out"][k], 0.45))
                    k += 1
                    s.ersetzen(T_["name"], folge[i], dauer=0.45)
                    s.ersetzen(T_["cnt"], "1", dauer=0.45)
                    prev, n = folge[i], 1
        schritt(s, EIN(T_["out"][k], 0.45), AUS(T_["ptr"], 0.45))
    schritt(s, EIN(trenn, 0.4))
    s.speichern()


def k6haeufigkeit():
    """Häufigkeitstabelle der Strecken: ungeordnet → sort (Block 5.0) → uniq -c (Block wird 3 5.0) → sort -rn (3 5.0 an die
    Spitze)."""
    s = Szene("linux/k6haeufigkeit", reihenfolge="anlegen")
    werte = [z.split(",")[2] for z in LAEUFE[1:]]
    folge = sorted(range(9), key=lambda i: (werte[i], i))           # Zeile r von sort enthält werte[folge[r]]
    gruppen, r = [], 0
    for v, g in itertools.groupby(werte[i] for i in folge):
        n = len(list(g))
        gruppen.append(("%d %s" % (n, v), r + (n - 1) / 2))
        r += n
    rn = sorted((g[0] for g in gruppen), key=lambda t: (int(t.split()[0]), t), reverse=True)
    ys = [r4(0.95 - k * 0.24) for k in range(9)]
    R = (-2.75, -1.2, 0.75, 2.95)

    def mx(Rk, t):
        return r4(Rk - len(t) * C / 2)

    def yv(rr):
        return r4(0.95 - rr * 0.24)
    l_st = L(s, "str", ("Strecken", "distances", "distancias", "距离", "distances", "mesafeler"), (r4(R[0] - 0.2), 1.47), FM,
             "center", GRAU)
    c1 = [tt(s, v, R[0], y, EM, SCHWARZ, "r") for v, y in zip(werte, ys)]
    k12 = [tt(s, v, R[0], y, EM, SCHWARZ, "r") for v, y in zip(werte, ys)]
    rb = rahmen(s, (mx(R[1], "5.0"), ys[4]), 0.5, 0.78)
    l_bl = L(s, "block", ("Block", "block", "bloque", "相同值成块", "bloc", "blok"), (-2.12, ys[4]), FM, "center", ORANGE)
    c3 = [tt(s, t, R[2], yv(rr), EM, ORANGE if t.startswith("3") else SCHWARZ, "r") for t, rr in gruppen]
    k34 = [tt(s, t, R[2], yv(rr), EM, ORANGE if t.startswith("3") else SCHWARZ, "r") for t, rr in gruppen]
    drei = [g for g, (t, rr) in enumerate(gruppen) if t.startswith("3")]
    pfe, labs = [], []
    for (xa, xb), w in zip(((-2.6, -1.68), (-1.08, 0.1), (0.87, 2.3)), ("sort", "uniq -c", "sort -rn")):
        pfe.append(pf(s, (xa, 1.22), (xb, 1.22), farbe=GRAU, spitze=0.1))
        labs.append(ttm(s, w, r4((xa + xb) / 2), 1.47))
    l_top = L(s, "top", ("häufigster Wert\nzuerst", "most frequent\nvalue first", "valor más\nfrecuente primero",
                         "最常见的值\n排在最前", "valeur la plus\nfréquente d'abord", "en sık değer\nbaşta"),
              (r4(R[3] - 0.3), -0.88), FM, "center", ORANGE)
    schritt(s, EIN([l_st] + c1 + k12, 0.6))
    s.pause(0.6)
    schritt(s, EIN(labs[0], 0.5), ZEICHNE(pfe[0], 0.5))
    schritt(s, *[ZU(k12[i], mx(R[1], werte[i]), ys[folge.index(i)], 1.2) for i in range(9)])
    schritt(s, EIN([rb, l_bl], 0.5))
    s.pause(0.6)
    schritt(s, EIN(labs[1], 0.5), ZEICHNE(pfe[1], 0.5))
    schritt(s, EIN(c3 + k34, 0.6))
    schritt(s, BETONE([c3[g] for g in drei], 0.8))      # nicht im selben Schritt wie EIN (sonst bleibt es unsichtbar)
    s.pause(0.6)
    schritt(s, EIN(labs[2], 0.5), ZEICHNE(pfe[2], 0.5))
    schritt(s, *[ZU(k34[g], mx(R[3], t), ys[rn.index(t)], 1.2) for g, (t, rr) in enumerate(gruppen)])
    schritt(s, EIN(l_top, 0.6), BETONE([k34[g] for g in drei], 0.8))
    s.speichern()


# ================================================================== Abschnitt 4: seq und diff
def k6seq():
    """Zahlenstrahl: seq 1 4 10 setzt Marken bei 1, 5, 9; der Sprung zu 13 liegt jenseits der 10 (grau). Darunter
    seq 0 0.5 2 mit Marken im Abstand 0,5."""
    s = Szene("linux/k6seq", reihenfolge="anlegen")
    ya = 0.7

    def X(v):
        return r4(-3.0 + v * 0.44)
    t1 = tt(s, "seq 1 4 10", -3.3, 1.55)
    ax1 = [linie(s, (X(0) - 0.1, ya), (X(10), ya), GRAU, 2), linie(s, (X(10), ya), (X(13) + 0.25, ya), HELLGRAU, 2, DASH)]
    ax1 += [linie(s, (X(v), ya - 0.05), (X(v), ya + 0.05), GRAU if v <= 10 else HELLGRAU, 1.5) for v in range(14)]
    tl1 = {v: text(s, str(v), (X(v), ya - 0.22), FM, "center", GRAU if v <= 10 else HELLGRAU) for v in range(14)}
    ende = linie(s, (X(10), ya - 0.12), (X(10), ya + 0.12), ORANGE, 3)
    l_ende = L(s, "ende", ("Ende", "end", "fin", "终点", "fin", "son"), (X(10), ya - 0.46), FM, "center", ORANGE)
    h = 0.42
    p1 = {v: s.punkt(None, X(v), ya, GRUEN, 0.07) for v in (1, 5, 9)}
    k13 = s.kreis(None, X(13), ya, 0.07, farbe=HELLGRAU, dicke=2, fuellung=WEISS, deckung=1.0)
    b1 = [bogen(s, X(a), X(b), ya, h, GRUEN if b <= 10 else HELLGRAU, "" if b <= 10 else DASH)
          for a, b in ((1, 5), (5, 9), (9, 13))]
    lb1 = [text(s, "+4", (X(a + 2), ya + h + 0.13), FM, "center", GRUEN if a < 9 else HELLGRAU) for a in (1, 5, 9)]
    yb = -0.95

    def Xb(v):
        return r4(-3.0 + v * 1.6)
    t2 = tt(s, "seq 0 0.5 2", -3.3, -0.1)
    stellen = (0, 0.5, 1, 1.5, 2)
    ax2 = [pf(s, (Xb(0) - 0.1, yb), (Xb(2) + 0.35, yb), farbe=GRAU, dicke=2, spitze=0.1)]
    ax2 += [linie(s, (Xb(v), yb - 0.05), (Xb(v), yb + 0.05), GRAU, 1.5) for v in stellen]
    ax2 += [text(s, ("%g" % v), (Xb(v), yb - 0.22), FM, "center", GRAU) for v in stellen]
    p2 = [s.punkt(None, Xb(v), yb, GRUEN, 0.07) for v in stellen]
    b2 = [bogen(s, Xb(a), Xb(a + 0.5), yb, 0.3) for a in stellen[:-1]]
    lb2 = [text(s, "+0.5", (Xb(a + 0.25), yb + 0.43), FM, "center", GRUEN) for a in stellen[:-1]]
    schritt(s, EIN([t1] + ax1 + list(tl1.values()), 0.7))
    s.pause(0.6)
    with s.gleichzeitig():
        schritt(s, WACHS(p1[1], 0.5))
        s.ersetzen(tl1[1], "1", farbe=GRUEN, dauer=0.5)
    for i, b in enumerate((5, 9)):
        with s.gleichzeitig():
            schritt(s, ZEICHNE(b1[i], 0.7), EIN(lb1[i], 0.7), WACHS(p1[b], 0.7))
            s.ersetzen(tl1[b], str(b), farbe=GRUEN, dauer=0.7)
    s.pause(0.4)
    schritt(s, ZEICHNE(b1[2], 0.7), EIN([lb1[2], k13], 0.7))
    schritt(s, EIN([ende, l_ende], 0.6))
    s.pause(0.6)
    schritt(s, EIN([t2] + ax2, 0.7))
    schritt(s, WACHS(p2[0], 0.4))
    for i in range(4):
        schritt(s, ZEICHNE(b2[i], 0.5), EIN(lb2[i], 0.5), WACHS(p2[i + 1], 0.5))
    s.speichern()


def k6diff():
    """Links die ersten fünf Zeilen, rechts dieselben mit ben: gleiche Zeilen grau verbunden, Zeile 3 leuchtet, darunter
    die Meldung 3c3 mit <, --- und >."""
    s = Szene("linux/k6diff", reihenfolge="anlegen")
    kurz = LAEUFE[:5]
    klein = [z.replace("B", "b") for z in kurz]
    xl, xr = -3.35, 0.2
    ys = [r4(1.25 - i * 0.22) for i in range(5)]
    l_a = L(s, "a", ("erste Datei", "first file", "primer archivo", "第一个文件", "premier fichier", "birinci dosya"),
            (xl, 1.6), FM, "left", GRAU)
    l_b = L(s, "b", ("zweite Datei", "second file", "segundo archivo", "第二个文件", "second fichier", "ikinci dosya"),
            (xr, 1.6), FM, "left", GRAU)
    m3 = [mark(s, x - 0.03, x + 22 * C2 + 0.03, ys[2], 0.2, ORANGE, 0.3) for x in (xl, xr)]
    tl = [tt(s, z, xl, y, E2) for z, y in zip(kurz, ys)]
    tr_ = [tt(s, z, xr, y, E2) for z, y in zip(klein, ys)]
    rB = [rahmen(s, (r4(sp(x, 11, E2) + C2 / 2), ys[2]), r4(C2 + 0.08), 0.22, ORANGE, 2) for x in (xl, xr)]
    verb = [linie(s, (r4(xl + len(kurz[i]) * C2 + 0.08), ys[i]), (r4(xr - 0.08), ys[i]), HELLGRAU, 1.5) for i in (0, 1, 3, 4)]
    kb = term_kasten(s, (-0.95, -0.6), 2.65, 0.98)
    l_m = L(s, "meld", ("Meldung von diff:", "message from diff:", "mensaje de diff:", "diff 的输出：", "message de diff :",
                        "diff çıktısı:"), (-2.27, 0.06), FM, "left", GRAU)
    x0 = -2.15
    d = [tt(s, "3c3", x0, -0.25, E2, BLAU), tt(s, "< " + kurz[2], x0, -0.47, E2), tt(s, "---", x0, -0.69, E2),
         tt(s, "> " + klein[2], x0, -0.91, E2)]
    xa = 0.55
    an = [L(s, "c", ("Zeile 3 ändern (c)", "change line 3 (c)", "cambiar la línea 3 (c)", "修改第 3 行 (c)",
                     "modifier la ligne 3 (c)", "3. satırı değiştir (c)"), (xa, -0.25), FM, "left", BLAU),
          L(s, "lt", ("aus der ersten Datei", "from the first file", "del primer archivo", "来自第一个文件", "du premier fichier",
                      "birinci dosyadan"), (xa, -0.47), FM, "left", GRAU),
          L(s, "gt", ("aus der zweiten Datei", "from the second file", "del segundo archivo", "来自第二个文件",
                      "du second fichier", "ikinci dosyadan"), (xa, -0.91), FM, "left", GRAU)]
    schritt(s, EIN([l_a, l_b] + tl + tr_, 0.6))
    s.pause(0.6)
    schritt(s, ZEICHNE(verb, 0.7))
    s.pause(0.6)
    schritt(s, EIN(m3 + rB, 0.6), BETONE([tl[2], tr_[2]], 0.8))
    s.pause(0.6)
    schritt(s, EIN([kb, l_m], 0.4))
    schritt(s, EIN([d[0], an[0]], 0.5))
    schritt(s, EIN([d[1], an[1]], 0.5))
    schritt(s, EIN(d[2], 0.3))
    schritt(s, EIN([d[3], an[2]], 0.5))
    s.speichern()


# ================================================================== Abschnitt 5: grep
def k6grep():
    """Lauftagebuch, Suchtext Anna: ohne Option 4 Zeilen, -v die 6 anderen, -c die Anzahl 4, -n die Nummern 2, 5, 7, 10."""
    s = Szene("linux/k6grep", reihenfolge="anlegen")
    x0 = -2.95
    ys = [r4(1.15 - i * 0.23) for i in range(10)]
    anna = [i for i, z in enumerate(LAEUFE) if "Anna" in z]
    andere = [i for i in range(10) if i not in anna]

    def mk(i, f):
        return mark(s, x0 - 0.04, x0 + len(LAEUFE[i]) * C2 + 0.04, ys[i], 0.21, f, 0.3)
    gA = [mk(i, GRUEN) for i in anna]
    oV = [mk(i, ORANGE) for i in andere]
    gB = [mk(i, GRUEN) for i in anna]
    tz = [tt(s, z, x0, y, E2) for z, y in zip(LAEUFE, ys)]
    nr = [tt(s, "%d:" % (i + 1), x0, ys[i], E2, GRUEN, "r") for i in anna]
    l_such = L(s, "such", ("Suchtext:", "search text:", "texto buscado:", "搜索文本：", "texte cherché :", "arama metni:"),
               (-1.75, 1.55), FM, "right", GRAU)
    t_such = tt(s, "Anna", -1.68, 1.55)
    xc, xe = -0.75, 1.25
    yr = (1.05, 0.5, -0.05, -0.6)
    cmds = [tt(s, "grep %sAnna laeufe.csv" % o, xc, y, E2) for o, y in zip(("", "-v ", "-c ", "-n "), yr)]
    erg = [L(s, "r1", ("4 Zeilen mit Anna", "4 lines with Anna", "4 líneas con Anna", "4 行含 Anna", "4 lignes avec Anna",
                       "Anna içeren 4 satır"), (xe, yr[0]), FM, "left", GRUEN),
           L(s, "r2", ("die 6 anderen", "the other 6", "las otras 6", "其余 6 行", "les 6 autres", "diğer 6 satır"),
             (xe, yr[1]), FM, "left", ORANGE),
           L(s, "r3", ("nur die Anzahl: 4", "only the count: 4", "solo el número: 4", "只输出数量：4", "seulement le nombre : 4",
                       "yalnızca sayı: 4"), (xe, yr[2]), FM, "left", GRUEN),
           L(s, "r4", ("Nummer vor jede Zeile", "number before each line", "número delante de cada línea", "每行前加行号",
                       "numéro devant chaque ligne", "her satırın önüne numara"), (xe, yr[3]), FM, "left", GRUEN)]
    schritt(s, EIN([l_such, t_such] + tz, 0.6))
    s.pause(0.6)
    schritt(s, EIN([cmds[0]] + gA + [erg[0]], 0.7))
    s.pause(0.6)
    schritt(s, EIN(cmds[1], 0.4), AUS(gA, 0.5), EIN(oV + [erg[1]], 0.7))
    s.pause(0.6)
    schritt(s, EIN(cmds[2], 0.4), AUS(oV, 0.5), EIN(gB + [erg[2]], 0.7))
    s.pause(0.6)
    schritt(s, EIN(cmds[3], 0.4), EIN(nr + [erg[3]], 0.7))
    s.speichern()


def k6grepo():
    """Zeile Anna und Anna: grep -c zählt Zeilen (1); grep -o schreibt jeden Treffer auf eine eigene Zeile, wc -l zählt sie (2)."""
    s = Szene("linux/k6grepo", reihenfolge="anlegen")
    em = 0.19
    zeile = "Anna und Anna"
    x0, y0 = r4(-len(zeile) * cw(em) / 2), 1.35
    mk = [mark(s, sp(x0, a, em) - 0.02, sp(x0, a + 4, em) + 0.02, y0, 0.26, GRUEN, 0.3) for a in (0, 9)]
    l_z = L(s, "zeile", ("Zeile:", "line:", "línea:", "行：", "ligne :", "satır:"), (x0 - 0.15, y0), FM, "right", GRAU)
    t_z = tt(s, zeile, x0, y0, em)
    xL, xR = -1.9, 1.75
    a_l = pf(s, (-0.7, 1.12), (-1.7, 0.62), farbe=GRAU, spitze=0.1)
    t_c = ttm(s, "grep -c Anna", xL, 0.45)
    r1 = [box(s, (xL, -0.05), 0.42, 0.38, GRUEN, GRUEN_HELL, 2), ttm(s, "1", xL, -0.05, em)]
    lab1 = L(s, "zz", ("zählt Zeilen", "counts lines", "cuenta líneas", "统计行数", "compte les lignes", "satırları sayar"),
             (xL, -0.46), FM, "center", GRAU)
    a_r = pf(s, (0.7, 1.12), (1.6, 0.62), farbe=GRAU, spitze=0.1)
    t_o = ttm(s, "grep -o Anna", xR, 0.45)
    ob = term_kasten(s, (xR, -0.02), 0.8, 0.56)
    kop = [tt(s, "Anna", sp(x0, a, em), y0, em) for a in (0, 9)]
    a_w = pf(s, (xR, -0.33), (xR, -0.55), farbe=GRAU, spitze=0.08)
    t_wc = ttm(s, "wc -l", xR, -0.7)
    r2 = [box(s, (xR, -1.12), 0.42, 0.38, GRUEN, GRUEN_HELL, 2), ttm(s, "2", xR, -1.12, em)]
    lab2 = L(s, "zt", ("zählt Treffer", "counts matches", "cuenta coincidencias", "统计匹配数", "compte les correspondances",
                       "eşleşmeleri sayar"), (xR, -1.53), FM, "center", GRAU)
    schritt(s, EIN([l_z, t_z] + kop, 0.6))
    schritt(s, EIN(mk, 0.6), BETONE(kop, 0.8))
    s.pause(0.6)
    schritt(s, ZEICHNE(a_l, 0.6), EIN(t_c, 0.6))
    schritt(s, EIN(r1 + [lab1], 0.6))
    s.pause(0.6)
    schritt(s, ZEICHNE(a_r, 0.6), EIN([t_o, ob], 0.6))
    schritt(s, ZU(kop[0], xR, 0.12, 0.9), ZU(kop[1], xR, -0.16, 0.9))
    s.pause(0.6)
    schritt(s, ZEICHNE(a_w, 0.5), EIN(t_wc, 0.5))
    schritt(s, EIN(r2 + [lab2], 0.6))
    s.speichern()


def k6grepr():
    """Kleiner Baum (., archiv/november.csv, laeufe.csv, minuten.txt, namen.txt): grep -r Clara . besucht jede Datei und
    schreibt Pfad:Zeile; grep -rl Clara . eine Zeile je Datei mit Treffer."""
    s = Szene("linux/k6grepr", reihenfolge="anlegen")
    eintr = ((".", 0, "dir"), ("archiv", 1, "dir"), ("november.csv", 2, "datei"), ("laeufe.csv", 1, "datei"),
             ("minuten.txt", 1, "datei"), ("namen.txt", 1, "datei"))
    yb = [r4(1.1 - i * 0.3) for i in range(6)]
    xsym = [r4(-3.25 + eb * 0.28) for _n, eb, _a in eintr]
    xnam = [r4(x + 0.18) for x in xsym]
    treffer = {2: "./archiv/november.csv", 3: "./laeufe.csv", 5: "./namen.txt"}
    marken = {i: mark(s, xnam[i] - 0.04, xnam[i] + len(eintr[i][0]) * C2 + 0.04, yb[i], 0.21, GRUEN, 0.3) for i in treffer}
    baum_, namen_, letzte = [], {}, {}
    for i, (name, eb, art) in enumerate(eintr):
        x, y = xsym[i], yb[i]
        if eb > 0:
            px, py = letzte[eb - 1]
            baum_ += [linie(s, (px, r4(py - 0.09)), (px, y), GRAU, 2),
                      linie(s, (px, y), (r4(x - (0.14 if art == "dir" else 0.09)), y), GRAU, 2)]
        baum_.append(ordner_symbol(s, x, y) if art == "dir" else datei_symbol(s, x, y))
        namen_[i] = tt(s, name, xnam[i], y, E2)
        baum_.append(namen_[i])
        if art == "dir":
            letzte[eb] = (x, y)
    baum_.append(tt(s, "(~/linuxk6)", r4(xnam[0] + 0.2), yb[0], E2, GRAU))
    kreuz = s.kreuzchen(None, r4(xnam[4] + len("minuten.txt") * C2 + 0.15), yb[4], HELLGRAU, 0.14, 3)
    x0 = -1.3
    t_c1 = tt(s, "$ grep -r Clara .", x0, 1.45, E2)
    l_pfad = L(s, "pfad", ("Pfad der Datei vor dem :", "file path before the :", "ruta del archivo antes de :",
                           "冒号前是文件路径", "chemin du fichier avant le :", "':' öncesi dosya yolu"),
               (0.25, 1.45), FM, "left", BLAU)
    zl = ("2026-11-03,Clara,7.2,41", "2026-11-07,Clara,8.0,44")
    ausg = [(i, treffer[i], z) for i in (2, 3, 5) for z in (zl if i != 5 else ("Clara", "Clara"))]
    out = []
    for k, (i, p, z) in enumerate(ausg):
        y = r4(1.2 - k * 0.22)
        out.append((i, [tt(s, p, x0, y, E2, BLAU), tt(s, ":" + z, sp(x0, len(p), E2), y, E2)]))
    t_c2 = tt(s, "$ grep -rl Clara .", x0, -0.28, E2)
    l_je = L(s, "je", ("eine Zeile je Datei", "one line per file", "una línea por archivo", "每个文件一行", "une ligne par fichier",
                       "dosya başına bir satır"), (0.35, -0.28), FM, "left", GRAU)
    out2 = [tt(s, treffer[i], x0, r4(-0.5 - k * 0.22), E2, BLAU) for k, i in enumerate((2, 3, 5))]
    schritt(s, EIN(baum_, 0.7))
    s.pause(0.6)
    schritt(s, EIN([t_c1, l_pfad], 0.5))
    for i in (2, 3, 4, 5):
        if i == 4:
            schritt(s, EIN(kreuz, 0.5))
        else:
            schritt(s, EIN([marken[i]] + [o for j, oo in out if j == i for o in oo], 0.6))
    s.pause(0.6)
    schritt(s, EIN([t_c2, l_je], 0.5))
    schritt(s, EIN(out2, 0.6), BETONE([namen_[i] for i in treffer], 0.8))
    s.speichern()


SZENEN_1 = (k6tabelle, k6zeilenende, k6ausschnitt, k6tailf,            # Abschnitte 1–5 (Phase 2b-1)
            k6cut, k6tr, k6paste, k6minuten,
            k6lexnum, k6schluessel, k6uniq, k6haeufigkeit,
            k6seq, k6diff,
            k6grep, k6grepo, k6grepr)
SZENEN_2 = ()                                                          # Abschnitte 6–10 (Phase 2b-2): hier anfügen
SZENEN = SZENEN_1 + SZENEN_2

if __name__ == "__main__":
    wahl = set(sys.argv[1:])
    for f in SZENEN:
        if not wahl or f.__name__ in wahl:
            f()
