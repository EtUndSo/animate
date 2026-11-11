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


# ================================================================== Abschnitt 6: reguläre Ausdrücke
W_AUSDR = ("Ausdruck", "expression", "expresión", "表达式", "expression", "ifade")
W_AUSDR2 = ("Ausdruck:", "expression:", "expresión:", "表达式：", "expression :", "ifade:")


def k6menge():
    """Der Ausdruck 5.0 beschreibt die Menge aller Zeichenketten aus 5, einem beliebigen Zeichen und 0. Von den Zeilen 5.0,
    5x0, 520 und 50 enthalten die ersten drei ein Stück der Menge (grün, das Element der Menge umrandet); 50 bleibt grau."""
    s = Szene("linux/k6menge", reihenfolge="anlegen")
    em = 0.24
    xa, ya = -2.55, 1.0
    l_a = L(s, "ausdr", W_AUSDR, (xa, 1.45), FM, "center", GRAU)
    mk_p = mark(s, xa - cw(em) / 2, xa + cw(em) / 2, ya, 0.36, BLAU, 0.25)
    t_a = ttm(s, "5.0", xa, ya, em)
    l_p = L(s, "punkt", ("Punkt = ein beliebiges Zeichen", "dot = any single character", "punto = un carácter cualquiera",
                         "点 = 任意一个字符", "point = un caractère quelconque", "nokta = herhangi bir karakter"),
            (-3.4, 0.55), FM, "left", BLAU)
    a = pf(s, (-2.05, ya), (-0.6, ya), farbe=GRAU, spitze=0.1)
    l_b = L(s, "beschr", ("beschreibt", "describes", "describe", "描述", "décrit", "tanımlar"), (-1.32, 1.17), FM, "center", GRAU)
    xm = 1.45
    k_m = box(s, (xm, 0.95), 3.8, 1.0, BLAU, BLAU_HELL, 2, "rect")
    l_m = L(s, "menge", ("Menge: 5, ein beliebiges Zeichen, 0", "set: 5, any character, 0", "conjunto: 5, un carácter cualquiera, 0",
                         "集合：5、任意一个字符、0", "ensemble : 5, un caractère quelconque, 0", "küme: 5, herhangi bir karakter, 0"),
            (xm, 1.67), FM, "center", BLAU)
    elem = ("5.0", "5x0", "520", "5,0", "5a0", "500", "5-0", "…")
    pos = [((0.0, 0.95, 1.9, 2.85)[i % 4], (1.18, 0.72)[i // 4]) for i in range(8)]
    rh = [rahmen(s, pos[i], 0.55, 0.34, GRUEN, 2.5) for i in range(3)]
    te = [ttm(s, e, x, y, 0.19, GRAU if e == "…" else SCHWARZ) for e, (x, y) in zip(elem, pos)]
    l_z = L(s, "zeilen", ("Zeilen:", "lines:", "líneas:", "行：", "lignes :", "satırlar:"), (-3.4, -0.45), FM, "left", GRAU)
    lx, yl = (-2.1, -0.95, 0.2, 1.35), -0.45
    zl = ("5.0", "5x0", "520", "50")
    mk_l = [mark(s, x - 0.25, x + 0.25, yl, 0.36, GRUEN, 0.3) for x in lx[:3]]
    tl = [ttm(s, z, x, yl, 0.22, GRAU) for z, x in zip(zl, lx)]
    hk = [haken(s, x, -0.85) for x in lx[:3]]
    l_kein = L(s, "kein", ("kein Stück aus der Menge", "no piece from the set", "ningún trozo del conjunto", "没有属于集合的片段",
                           "aucun morceau de l'ensemble", "kümeden parça yok"), (lx[3], -0.85), FM, "center", GRAU)
    schritt(s, EIN([l_a, t_a], 0.6))
    schritt(s, EIN([mk_p, l_p], 0.6))
    s.pause(0.6)
    schritt(s, ZEICHNE(a, 0.6), EIN([l_b, k_m, l_m], 0.6))
    schritt(s, EIN(te[:4], 0.6))
    schritt(s, EIN(te[4:], 0.6))
    s.pause(0.6)
    schritt(s, EIN([l_z] + tl, 0.6))
    for i in range(3):
        with s.gleichzeitig():
            schritt(s, EIN([mk_l[i], rh[i]] + hk[i], 0.6), BETONE(te[i], 0.7))
            s.ersetzen(tl[i], zl[i], farbe=SCHWARZ, dauer=0.6)
    s.pause(0.4)
    schritt(s, EIN(l_kein, 0.6))
    s.speichern()


def k6klammer():
    """2026-11-0[2-4] Stelle für Stelle: über 2026-11-03 stimmen die festen Zeichen, die 3 liegt im Kästchen {2, 3, 4}
    (Treffer); über 2026-11-07 liegt die 7 nicht im Kästchen (kein Treffer)."""
    s = Szene("linux/k6klammer", reihenfolge="anlegen")
    em, hc = 0.22, 0.34
    xs = [r4(-3.0 + 0.3 * i) for i in range(9)]
    xk = 0.1
    xd = xs + [xk]
    yE, y1, y2 = 0.95, 0.1, -0.8
    zE = [box(s, (x, yE), 0.28, hc, GRAU, WEISS, 1.5, "rect") for x in xs]
    kk = box(s, (xk, yE), 0.86, 0.42, ORANGE, ORANGE_HELL, 2.5, "rect")
    mk3 = mark(s, xk - 0.11, xk + 0.11, yE, 0.32, GRUEN, 0.45)
    tE = [ttm(s, c, x, yE, em) for c, x in zip("2026-11-0", xs)]
    tk = [ttm(s, c, x, yE, em) for c, x in zip("234", (xk - 0.25, xk, xk + 0.25))]
    t_kl = ttm(s, "[2-4]", xk, yE + 0.38, 0.17, ORANGE)
    l_fest = L(s, "fest", ("feste Zeichen", "fixed characters", "caracteres fijos", "固定字符", "caractères fixes",
                           "sabit karakterler"), (r4((xs[0] + xs[8]) / 2), yE + 0.38), FM, "center", GRAU)
    l_E = L(s, "ausdr", W_AUSDR, (0.65, yE + 0.14), FM, "left", GRAU)
    t_E = tt(s, "2026-11-0[2-4]", 0.65, yE - 0.14, 0.17)

    def datum(d, y, f_letzt):
        zellen = [box(s, (x, y), 0.28, hc, GRAU, WEISS, 1.5, "rect") for x in xd]
        m_fest = mark(s, xs[0] - 0.14, xs[8] + 0.14, y, hc, GRUEN, 0.3)
        m_letzt = mark(s, xk - 0.14, xk + 0.14, y, hc, f_letzt, 0.3)
        return zellen, m_fest, m_letzt, [ttm(s, c, x, y, em) for c, x in zip(d, xd)]
    z1, mf1, ml1, t1 = datum("2026-11-03", y1, GRUEN)
    z2, mf2, ml2, t2 = datum("2026-11-07", y2, ROT)
    a3 = pf(s, (xk, y1 + 0.2), (xk, yE - 0.23), farbe=GRUEN, spitze=0.08)
    kz = s.kreuzchen(None, 0.42, y2, ROT, 0.16, 3)
    l_ok = L(s, "ok", ("3 im Kästchen: Treffer", "3 is in the box: match", "3 está en la caja: coincide", "3 在方框中：匹配",
                       "3 dans la case : correspondance", "3 kutuda: eşleşme"), (0.65, y1), FM, "left", GRUEN)
    l_no = L(s, "no", ("7 nicht im Kästchen: kein Treffer", "7 is not in the box: no match", "7 no está en la caja: no coincide",
                       "7 不在方框中：不匹配", "7 hors de la case : échec", "7 kutuda değil: eşleşme yok"), (0.65, y2), FM, "left", ROT)
    schritt(s, EIN(zE + [kk] + tE + tk + [t_kl, l_fest, l_E, t_E], 0.7))
    s.pause(0.6)
    schritt(s, EIN(z1 + t1, 0.6))
    schritt(s, EIN(mf1, 0.6), BETONE(tE, 0.7))
    s.pause(0.4)
    schritt(s, EIN([ml1, mk3], 0.6), ZEICHNE(a3, 0.6), BETONE(tk[1], 0.8), EIN(l_ok, 0.6))
    s.pause(0.6)
    schritt(s, EIN(z2 + t2, 0.6))
    schritt(s, EIN(mf2, 0.6))
    schritt(s, EIN([ml2, kz, l_no], 0.6), BETONE(tk, 0.8))
    s.speichern()


def k6klassen():
    """Die Zeile 2026-11-03,Clara,7.2,41 Zeichen für Zeichen: nacheinander [[:digit:]] (12 Ziffern, blau), [[:alpha:]]
    (5 Buchstaben, grün), [[:punct:]] (6 Satzzeichen, orange); jedes Zeichen gehört zu genau einer Klasse."""
    s = Szene("linux/k6klassen", reihenfolge="anlegen")
    em = 0.24
    z = "2026-11-03,Clara,7.2,41"
    x0, y0 = r4(-len(z) * cw(em) / 2), 1.1
    klassen = (("digit", "[[:digit:]]", BLAU, str.isdigit,
                ("12 Ziffern", "12 digits", "12 dígitos", "12 个数字", "12 chiffres", "12 rakam")),
               ("alpha", "[[:alpha:]]", GRUEN, str.isalpha,
                ("5 Buchstaben", "5 letters", "5 letras", "5 个字母", "5 lettres", "5 harf")),
               ("punct", "[[:punct:]]", ORANGE, lambda ch: ch in "-,.",
                ("6 Satzzeichen", "6 punctuation marks", "6 signos de puntuación", "6 个标点符号", "6 signes de ponctuation",
                 "6 noktalama işareti")))
    mk, idx = [], []
    for _k, _n, f, test, _w in klassen:
        ii = [i for i, ch in enumerate(z) if test(ch)]
        idx.append(ii)
        mk.append([mark(s, sp(x0, i, em) + 0.008, sp(x0, i + 1, em) - 0.008, y0, 0.4, f, 0.3) for i in ii])
    tz = [tt(s, ch, sp(x0, i, em), y0, em) for i, ch in enumerate(z)]
    zeilen = [[tt(s, name, -1.6, y, 0.19, f), L(s, key, w, (-0.25, y), FM, "left", f)]
              for (key, name, f, _t, w), y in zip(klassen, (0.35, -0.2, -0.75))]
    l_g = L(s, "genau", ("Jedes Zeichen gehört zu genau einer der drei Klassen.",
                         "Each character belongs to exactly one of the three classes.",
                         "Cada carácter pertenece a exactamente una de las tres clases.", "每个字符恰好属于三个类中的一个。",
                         "Chaque caractère appartient à exactement une des trois classes.",
                         "Her karakter üç sınıftan tam olarak birine aittir."), (0, -1.3), FM, "center", GRAU)
    schritt(s, EIN(tz, 0.6))
    for k in range(3):
        s.pause(0.5)
        schritt(s, EIN(zeilen[k], 0.5))
        schritt(s, EIN(mk[k], 0.6), BETONE([tz[i] for i in idx[k]], 0.8))
    s.pause(0.6)
    schritt(s, EIN(l_g, 0.6))
    s.speichern()


def k6anker():
    """2026-11-08,Ben,21.1,128 als Zeichen mit Stellen (Striche) dazwischen; der erste Strich ist die Stelle von ^, der letzte
    die von $. ,2[0-9] trifft ,21; ,2[0-9]$ müsste am letzten Strich enden und findet nichts."""
    s = Szene("linux/k6anker", reihenfolge="anlegen")
    z = LAEUFE[8]
    n, d, y0, em = len(z), 0.2, 1.0, 0.21
    xl = r4(-n * d / 2)
    xs = [r4(xl + d * k) for k in range(n + 1)]
    xc = [r4(xl + d * (i + 0.5)) for i in range(n)]
    mk = mark(s, xs[14], xs[17], y0, 0.38, GRUEN, 0.3)
    st = [linie(s, (x, y0 - 0.2), (x, y0 + 0.2), HELLGRAU, 1.5) for x in xs[1:-1]]
    sa = [linie(s, (x, y0 - 0.24), (x, y0 + 0.24), BLAU, 3) for x in (xs[0], xs[-1])]
    tz = [ttm(s, ch, x, y0, em) for ch, x in zip(z, xc)]
    t_hut = ttm(s, "^", xs[0], y0 + 0.42, 0.19, BLAU)
    t_dol = ttm(s, "$", xs[-1], y0 + 0.42, 0.19, BLAU)
    l_st = L(s, "stellen", ("Stellen zwischen den Zeichen", "positions between the characters", "posiciones entre los caracteres",
                            "字符之间的位置", "positions entre les caractères", "karakterler arasındaki konumlar"),
             (0, y0 + 0.45), FM, "center", GRAU)
    a = pf(s, (xs[17], y0 - 0.33), (xs[23], y0 - 0.33), farbe=ORANGE, dash=DASH, spitze=0.09)
    y1, y2 = 0.2, -0.45
    t_r1 = tt(s, ",2[0-9]", -3.35, y1, 0.19)
    hk = haken(s, -2.33, y1)
    l_r1 = L(s, "r1", ("Treffer: ,21", "match: ,21", "coincidencia: ,21", "匹配：,21", "correspondance : ,21", "eşleşme: ,21"),
             (-2.1, y1), FM, "left", GRUEN)
    t_r2 = tt(s, ",2[0-9]$", -3.35, y2, 0.19)
    kz = s.kreuzchen(None, -2.33, y2, ROT, 0.16, 3)
    l_r2 = L(s, "r2", ("müsste am letzten Strich enden: kein Treffer", "would have to end at the last stroke: no match",
                       "tendría que terminar en el último trazo: sin coincidencia", "必须在最后一条竖线处结束：无匹配",
                       "devrait finir au dernier trait : pas de correspondance", "son çizgide bitmeli: eşleşme yok"),
             (-2.1, y2), FM, "left", ROT)
    schritt(s, EIN(tz, 0.6))
    s.pause(0.6)
    schritt(s, ZEICHNE(st + sa, 0.7), EIN(l_st, 0.6))
    schritt(s, EIN([t_hut, t_dol], 0.5), BETONE(sa, 0.8))
    s.pause(0.6)
    schritt(s, EIN(t_r1, 0.5))
    schritt(s, EIN([mk, l_r1] + hk, 0.6), BETONE(tz[14:17], 0.8))
    s.pause(0.6)
    schritt(s, EIN(t_r2, 0.5))
    schritt(s, ZEICHNE(a, 0.7), BETONE(sa[1], 0.8))
    schritt(s, EIN([kz, l_r2], 0.6))
    s.speichern()


# ================================================================== Abschnitt 7: Wiederholungen, zwei Formen
def k6grundform():
    """,[0-9]{3}$ zweimal: oben (Grundform) sind {, 3, } gewöhnliche Zeichen, der Vergleich mit ,128 scheitert an der 2 unter {;
    unten (-E) heißt {3} „die Ziffer davor dreimal“, ,128 ist ein Treffer."""
    s = Szene("linux/k6grundform", reihenfolge="anlegen")
    z, em_z, xz = LAEUFE[8], 0.17, -1.3
    l_z = L(s, "zeile", ("Zeile:", "line:", "línea:", "行：", "ligne :", "satır:"), (xz - 0.12, 1.65), FM, "right", GRAU)
    mz = mark(s, sp(xz, 19, em_z) - 0.02, sp(xz, 23, em_z) + 0.02, 1.65, 0.24, GRUEN, 0.3)
    t_z = tt(s, z, xz, 1.65, em_z)

    def kacheln(teile, y, x=-3.2, gap=0.08):
        objs, mitten = [], []
        for t, b in teile:
            m = r4(x + b / 2)
            objs += [box(s, (m, y), b, 0.36, GRAU, WEISS, 1.5, "rect"), ttm(s, t, m, y, 0.19)]
            mitten.append(m)
            x += b + gap
        return objs, mitten
    y1k, y1z = 0.75, 0.3
    l_p1 = L(s, "p1", ("ohne Option: Grundform", "without option: basic form", "sin opción: forma básica", "无选项：基本形式",
                       "sans option : forme de base", "seçeneksiz: temel biçim"), (-3.35, 1.17), FM, "left", DUNKEL)
    k1, m1 = kacheln(((",", 0.36), ("[0-9]", 0.72), ("{", 0.36), ("3", 0.36), ("}", 0.36), ("$", 0.36)), y1k)
    g1 = [mark(s, m1[i] - 0.16, m1[i] + 0.16, y1z, 0.34, f, 0.3) for i, f in ((0, GRUEN), (1, GRUEN), (2, ROT))]
    c1 = [ttm(s, ch, m1[i], y1z, 0.22) for i, ch in enumerate(",128")]
    hk = [haken(s, m1[i], y1z - 0.33, GRUEN, 0.08, 3) for i in (0, 1)]
    kz = s.kreuzchen(None, m1[2], y1z - 0.33, ROT, 0.14, 3)
    l_g = L(s, "gew", ("{, 3 und } sind gewöhnliche Zeichen", "{, 3 and } are ordinary characters",
                       "{, 3 y } son caracteres normales", "{、3 和 } 是普通字符", "{, 3 et } sont des caractères ordinaires",
                       "{, 3 ve } sıradan karakterlerdir"), (0.1, y1k), FM, "left", GRAU, roh=True)
    l_n = L(s, "nein", ("2 ist nicht {: kein Treffer", "2 is not {: no match", "2 no es {: sin coincidencia", "2 不是 {：无匹配",
                        "2 n'est pas { : pas de correspondance", "2, { ile aynı değil: eşleşme yok"), (0.1, y1z), FM, "left", ROT, roh=True)
    y2k, y2z = -0.7, -1.15
    l_p2 = L(s, "p2", ("mit -E: erweiterte Form", "with -E: extended form", "con -E: forma extendida", "使用 -E：扩展形式",
                       "avec -E : forme étendue", "-E ile: genişletilmiş biçim"), (-3.35, -0.28), FM, "left", DUNKEL)
    k2, m2 = kacheln(((",", 0.36), ("[0-9]{3}", 1.2), ("$", 0.36)), y2k)
    g2 = [mark(s, m2[0] - 0.16, m2[0] + 0.16, y2z, 0.34, GRUEN, 0.3), mark(s, m2[1] - 0.45, m2[1] + 0.45, y2z, 0.34, GRUEN, 0.3)]
    c2 = [ttm(s, ",", m2[0], y2z, 0.22)] + [ttm(s, ch, r4(m2[1] + dx), y2z, 0.22) for ch, dx in zip("128", (-0.28, 0, 0.28))]
    ende = linie(s, (m2[2], y2z - 0.2), (m2[2], y2z + 0.2), BLAU, 3)
    l_3 = L(s, "drei", ("{3}: die Ziffer davor dreimal", "{3}: the digit before it three times", "{3}: el dígito anterior tres veces",
                        "{3}：前面的数字出现三次", "{3} : le chiffre précédent trois fois", "{3}: önceki rakam üç kez"),
            (0.1, y2k), FM, "left", BLAU, roh=True)
    l_t = L(s, "treffer", ("Treffer: ,128", "match: ,128", "coincidencia: ,128", "匹配：,128", "correspondance : ,128", "eşleşme: ,128"),
            (0.1, y2z), FM, "left", GRUEN)
    schritt(s, EIN([l_z, t_z], 0.6))
    s.pause(0.6)
    schritt(s, EIN([l_p1] + k1, 0.6))
    schritt(s, EIN(c1 + [l_g], 0.6))
    s.pause(0.4)
    schritt(s, EIN([g1[0]] + hk[0], 0.45))
    schritt(s, EIN([g1[1]] + hk[1], 0.45))
    schritt(s, EIN([g1[2], kz, l_n], 0.6), BETONE(k1[5], 0.8))
    s.pause(0.6)
    schritt(s, EIN([l_p2] + k2, 0.6))
    schritt(s, EIN(l_3, 0.5), BETONE(k2[3], 0.8))
    schritt(s, EIN(c2 + [ende], 0.6))
    schritt(s, EIN(g2 + [l_t, mz], 0.6), BETONE(c2[1:], 0.8))
    s.speichern()


def k6quantor():
    """^a*b$, ^a+b$, ^a?b$, ^a{2,3}b$ gegen b, ab, aab, aaab: passende Zeichenketten leuchten auf (4, 3, 2, 2), die übrigen
    bleiben grau."""
    s = Szene("linux/k6quantor", reihenfolge="anlegen")
    ketten = ("b", "ab", "aab", "aaab")
    xk = (-0.2, 0.75, 1.8, 2.95)
    reihen = (("^a*b$", "stern", ("beliebig oft, auch null", "zero or more times", "cero o más veces", "任意次，也可以是零次",
                                  "zéro fois ou plus", "sıfır veya daha çok kez"), (1, 1, 1, 1)),
              ("^a+b$", "plus", ("mindestens einmal", "at least once", "al menos una vez", "至少一次", "au moins une fois",
                                 "en az bir kez"), (0, 1, 1, 1)),
              ("^a?b$", "frage", ("keinmal oder einmal", "zero times or once", "cero o una vez", "零次或一次", "zéro ou une fois",
                                  "sıfır ya da bir kez"), (1, 1, 0, 0)),
              ("^a{2,3}b$", "nm", ("zwei- bis dreimal", "two to three times", "de dos a tres veces", "两到三次", "deux à trois fois",
                                   "iki ila üç kez"), (0, 0, 1, 1)))
    ys = (0.8, 0.3, -0.2, -0.7)
    l_a = L(s, "ausdr", W_AUSDR, (-3.35, 1.3), FM, "left", GRAU)
    l_k = L(s, "ketten", ("Zeichenketten", "strings", "cadenas", "字符串", "chaînes", "dizgiler"), (r4((xk[0] + xk[3]) / 2), 1.3),
            FM, "center", GRAU)
    grau, neu, hell, kopf = [], [], [], []
    for (ausdr, key, w, passt), y in zip(reihen, ys):
        neu.append([mark(s, x - 0.33, x + 0.33, y, 0.32, GRUEN, 0.3) for x, p in zip(xk, passt) if p])
        g = [ttm(s, k, x, y, 0.19, GRAU) for k, x in zip(ketten, xk)]
        grau += g
        hell.append([(t, k) for t, k, p in zip(g, ketten, passt) if p])
        kopf.append([tt(s, ausdr, -3.35, y, 0.19, BLAU), L(s, key, w, (-2.3, y), FM, "left", GRAU)])
    l_anker = L(s, "anker", ("^ und $: die ganze Zeichenkette muss passen", "^ and $: the whole string must match",
                             "^ y $: toda la cadena debe coincidir", "^ 和 $：整个字符串必须匹配",
                             "^ et $ : toute la chaîne doit correspondre", "^ ve $: dizginin tamamı eşleşmeli"),
                (0, -1.15), FM, "center", GRAU, roh=True)
    schritt(s, EIN([l_a, l_k] + grau, 0.7))
    for r in range(4):
        s.pause(0.4)
        schritt(s, EIN(kopf[r], 0.5))
        with s.gleichzeitig():
            schritt(s, EIN(neu[r], 0.6))
            for t, k in hell[r]:
                s.ersetzen(t, k, farbe=SCHWARZ, dauer=0.6)
    s.pause(0.4)
    schritt(s, EIN(l_anker, 0.5))
    s.speichern()


def k6gierig():
    """A.*km im Satz Anna lief 5 km, Ben lief 10 km: Beginn beim A ganz links, ein kurzer Bogen bis zum ersten km, ein langer
    bis zum letzten, der längere gewinnt; darunter A[^,]*km: das Komma ist verboten, der Bogen endet beim ersten km."""
    s = Szene("linux/k6gierig", reihenfolge="anlegen")
    satz = "Anna lief 5 km, Ben lief 10 km"
    em, x0 = 0.2, -2.3
    y1, y2 = 0.55, -0.85
    xe = r4(sp(x0, 14, em))
    xz = r4(sp(x0, len(satz), em))
    mA = mark(s, x0 - 0.01, sp(x0, 1, em), y1, 0.3, BLAU, 0.3)
    m1 = mark(s, x0 - 0.02, xz + 0.02, y1, 0.3, GRUEN, 0.3)
    m2 = mark(s, x0 - 0.02, xe, y2, 0.3, GRUEN, 0.3)
    mk = mark(s, xe, sp(x0, 15, em), y2, 0.3, ORANGE, 0.45)
    a1 = tt(s, "A.*km", -3.35, y1, 0.19, BLAU)
    t1 = tt(s, satz, x0, y1, em)
    a2 = tt(s, "A[^,]*km", -3.35, y2, 0.19, BLAU)
    t2 = tt(s, satz, x0, y2, em)
    b_kurz = bogen(s, x0, xe, y1 + 0.18, 0.4, GRAU, DASH, 2.5)
    b_lang = bogen(s, x0, xz, y1 + 0.18, 0.75, GRUEN, "", 3)
    b2 = bogen(s, x0, xe, y2 + 0.18, 0.4, GRUEN, "", 3)
    l_beg = L(s, "beg", ("Beginn: das A ganz links", "start: the A on the far left", "inicio: la A más a la izquierda",
                         "起点：最左边的 A", "début : le A tout à gauche", "başlangıç: en soldaki A"), (x0, y1 - 0.33), FM, "left", BLAU)
    l_kurz = L(s, "kurz", ("erstes km", "first km", "primer km", "第一个 km", "premier km", "ilk km"), (xe + 0.08, y1 + 0.37),
               FM, "left", GRAU)
    l_lang = L(s, "lang", ("letztes km: gewinnt", "last km: wins", "último km: gana", "最后一个 km：胜出", "dernier km : l'emporte",
                           "son km: kazanır"), (xz + 0.1, y1 + 0.37), FM, "left", GRUEN)
    l_e2 = L(s, "e2", ("endet beim ersten km", "ends at the first km", "termina en el primer km", "在第一个 km 处结束",
                       "finit au premier km", "ilk km'de biter"), (xe + 0.08, y2 + 0.37), FM, "left", GRUEN)
    l_k = L(s, "komma", ("kein Komma erlaubt", "no comma allowed", "no se permite coma", "不允许逗号", "virgule interdite",
                         "virgüle izin yok"), (r4(sp(x0, 14.5, em)), y2 - 0.33), FM, "center", ORANGE)
    schritt(s, EIN([a1, t1], 0.6))
    s.pause(0.6)
    schritt(s, EIN([mA, l_beg], 0.6))
    s.pause(0.6)
    schritt(s, ZEICHNE(b_kurz, 0.8), EIN(l_kurz, 0.6))
    schritt(s, ZEICHNE(b_lang, 1.0), EIN(l_lang, 0.6))
    s.pause(0.4)
    schritt(s, EIN(m1, 0.6), BETONE(l_lang, 0.8))
    s.pause(0.6)
    schritt(s, EIN([a2, t2], 0.6))
    schritt(s, EIN([mk, l_k], 0.6))
    schritt(s, ZEICHNE(b2, 0.8), EIN([m2, l_e2], 0.6))
    s.speichern()


def k6automat():
    """[0-9]+\\.[0-9]+ als Maschine mit vier Kreisen (Start, in der Zahl, nach dem Punkt, Ziel); 10.5 wandert Zeichen für Zeichen
    hindurch, der leuchtende Kreis ist der Zustand; bei der 5 ist das Ziel erreicht."""
    s = Szene("linux/k6automat", reihenfolge="anlegen")
    cy, r = 0.25, 0.36
    xs = (-2.55, -0.85, 0.85, 2.55)
    l_aus = L(s, "ausdr", W_AUSDR2, (-0.52, 1.6), FM, "right", GRAU)
    t_aus = ttm(s, "[0-9]+\\.[0-9]+", 0.3, 1.6, 0.19)
    kr = [s.kreis(None, x, cy, r, farbe=DUNKEL, dicke=2.5, fuellung=WEISS, deckung=1.0) for x in xs]
    innen = s.kreis(None, xs[3], cy, 0.29, farbe=DUNKEL, dicke=2, fuellung=WEISS, deckung=0.0)
    ziel_g = s.kreis(None, xs[3], cy, r, farbe=GRUEN, dicke=4, fuellung=GRUEN, deckung=0.0)
    tok = s.kreis(None, xs[0], cy, 0.27, farbe=ORANGE, dicke=0, fuellung=ORANGE, deckung=0.35)
    namen = (("start", ("Start", "start", "inicio", "开始", "départ", "başlangıç")),
             ("zahl", ("in der Zahl", "in the number", "en el número", "在数字中", "dans le nombre", "sayının içinde")),
             ("punkt", ("nach dem Punkt", "after the dot", "tras el punto", "在点之后", "après le point", "noktadan sonra")),
             ("ziel", ("Ziel", "goal", "meta", "终点", "but", "hedef")))
    ln = [L(s, k, w, (x, r4(cy - r - 0.2)), FM, "center", DUNKEL) for (k, w), x in zip(namen, xs)]
    a_in = pf(s, (-3.42, cy), (r4(xs[0] - r - 0.02), cy), farbe=DUNKEL, spitze=0.1)
    ab = [pf(s, (r4(xs[i] + r + 0.03), cy), (r4(xs[i + 1] - r - 0.03), cy), farbe=DUNKEL, spitze=0.1) for i in range(3)]
    w_z = ("Ziffer", "digit", "dígito", "数字", "chiffre", "rakam")
    w_p = ("Punkt", "dot", "punto", "点", "point", "nokta")
    la = [L(s, "a%d" % i, w, (r4((xs[i] + xs[i + 1]) / 2), cy + 0.17), FM, "center", BLAU) for i, w in enumerate((w_z, w_p, w_z))]
    cyl = r4(cy + 0.477)
    sl = [s.weg(None, "%s+0.2*cos(pi/180*(220-260*t))" % x, "%s+0.2*sin(pi/180*(220-260*t))" % cyl, 0, 1, farbe=DUNKEL,
                dicke=2.5, pfeile="0.5", n=41, spitze=0.1) for x in (xs[1], xs[3])]
    ls = [L(s, "s%d" % i, w_z, (x, r4(cyl + 0.36)), FM, "center", BLAU) for i, x in enumerate((xs[1], xs[3]))]
    yz = -0.95
    l_zk = L(s, "zk", ("Zeichenkette:", "string:", "cadena:", "字符串：", "chaîne :", "dizgi:"), (-1.3, yz), FM, "right", GRAU)
    xz = (-1.1, -0.85, -0.6, -0.35)
    mz = [mark(s, x - 0.12, x + 0.12, yz, 0.34, GRUEN, 0.3) for x in xz]
    tz = [ttm(s, ch, x, yz, 0.24) for ch, x in zip("10.5", xz)]
    l_ok = L(s, "ok", ("bei der 5: Ziel erreicht", "at the 5: goal reached", "en el 5: meta alcanzada", "读到 5：到达终点",
                       "après le 5 : but atteint", "5'te: hedefe ulaşıldı"), (0.1, yz), FM, "left", GRUEN)
    l_m = L(s, "merk", ("Die Maschine merkt sich nur den Kreis, in dem sie steht.",
                        "The machine remembers only the circle it is in.", "La máquina solo recuerda el círculo en el que está.",
                        "机器只记住自己所在的圆圈。", "La machine ne retient que le cercle où elle se trouve.",
                        "Makine yalnızca bulunduğu daireyi hatırlar."), (0, -1.45), FM, "center", GRAU)
    schritt(s, EIN([l_aus, t_aus], 0.6))
    s.pause(0.6)
    schritt(s, WACHS(kr, 0.7), EIN([innen] + ln, 0.7), ZEICHNE(a_in, 0.6))
    schritt(s, ZEICHNE(ab + sl, 0.8), EIN(la + ls, 0.8))
    s.pause(0.6)
    schritt(s, EIN([l_zk] + tz + [tok], 0.6))
    s.pause(0.4)
    schritt(s, EIN(mz[0], 0.5), ZU(tok, xs[1], cy, 0.8), BETONE(ab[0], 0.8))
    s.pause(0.2)
    schritt(s, EIN(mz[1], 0.5), BETONE(sl[0], 0.8))
    s.pause(0.2)
    schritt(s, EIN(mz[2], 0.5), ZU(tok, xs[2], cy, 0.8), BETONE(ab[1], 0.8))
    s.pause(0.2)
    schritt(s, EIN(mz[3], 0.5), ZU(tok, xs[3], cy, 0.8), BETONE(ab[2], 0.8))
    s.pause(0.4)
    schritt(s, EIN([ziel_g, l_ok], 0.6))
    schritt(s, EIN(l_m, 0.6))
    s.speichern()


# ================================================================== Abschnitt 8: sed
def k6sed():
    """Kreislauf von sed: Zeile aus laeufe.csv in den Zwischenspeicher, s/,/;/ ändert das erste Komma, Ausgabe, nächste Zeile;
    die Datei bleibt grau und unverändert."""
    s = Szene("linux/k6sed", reihenfolge="anlegen")
    zeilen = LAEUFE[:3]
    neu = [z.replace(",", ";", 1) for z in zeilen]
    yz = (0.65, 0.43, 0.21, -0.01)
    fb = box(s, (-2.4, 0.25), 2.0, 1.2, GRAU, WEISS, 2, "rect")
    f_t = tt(s, "laeufe.csv", -2.4, 1.05, E2, GRAU, "m")
    fl = [tt(s, z, -3.3, y, E2, GRAU) for z, y in zip(zeilen, yz)] + [tt(s, "…", -3.3, yz[3], E2, GRAU)]
    l_unv = L(s, "unv", ("bleibt unverändert", "stays unchanged", "no cambia", "保持不变", "reste inchangé", "değişmeden kalır"),
              (-2.4, -0.55), FM, "center", GRAU)
    yb = 1.2
    bb = box(s, (0, yb), 2.0, 0.36, GRAU, GELB, 2, "rect")
    l_b = L(s, "zw", ("Zwischenspeicher", "buffer", "búfer", "缓冲区", "tampon", "ara bellek"), (0, 1.6), FM, "center", DUNKEL)
    sm = []
    for z in zeilen:
        xl, k = -len(z) * C2 / 2, z.index(",")
        sm.append(mark(s, sp(xl, k, E2) - 0.01, sp(xl, k + 1, E2) + 0.01, yb, 0.24, ORANGE, 0.5))
    ob = term_kasten(s, (2.4, 0.25), 2.0, 1.2)
    l_o = L(s, "aus", ("Ausgabe", "output", "salida", "输出", "sortie", "çıktı"), (2.4, 1.05), FM, "center", GRAU)
    o_dots = tt(s, "…", 1.48, yz[3], E2)
    kb = box(s, (0, 0.4), 1.05, 0.36, BLAU, BLAU_HELL, 2, "round")
    t_cmd = ttm(s, "s/,/;/", 0, 0.4)
    a_cmd = pf(s, (0, 0.6), (0, 1.0), farbe=BLAU, spitze=0.09)
    l_cmd = L(s, "befehl", ("Befehl", "command", "comando", "命令", "commande", "komut"), (0, 0.05), FM, "center", BLAU)
    a1 = pf(s, (-1.36, 0.92), (-1.04, 1.13), farbe=GRAU, spitze=0.08)
    a2 = pf(s, (1.04, 1.13), (1.36, 0.92), farbe=GRAU, spitze=0.08)
    lp = s.weg(None, "1.4-2.8*t", "-0.3-0.45*4*t*(1-t)", 0, 1, farbe=GRAU, dicke=2.5, pfeile="0.5", n=41, spitze=0.1)
    l_lp = L(s, "naechste", ("nächste Zeile", "next line", "siguiente línea", "下一行", "ligne suivante", "sonraki satır"),
             (0, -0.95), FM, "center", GRAU)
    inn = [ttm(s, z, 0, yb, E2) for z in zeilen]
    out = [ttm(s, z, 0, yb, E2) for z in neu]
    schritt(s, EIN([fb, f_t] + fl + [bb, l_b, ob, l_o, kb, t_cmd, l_cmd], 0.8), ZEICHNE([a1, a2, a_cmd], 0.8))
    s.pause(0.6)
    for i in range(3):
        teile = [EIN(inn[i], 0.6), BETONE(fl[i], 0.7)]
        if i:
            teile.append(BETONE(lp, 0.7))
        schritt(s, *teile)
        schritt(s, BETONE(t_cmd, 0.7), AUS(inn[i], 0.5), EIN([out[i], sm[i]], 0.6))
        schritt(s, ZU(out[i], mitte_tt(1.48, neu[i], E2), yz[i], 0.8), AUS(sm[i], 0.4))
        if i == 0:
            schritt(s, ZEICHNE(lp, 0.6), EIN(l_lp, 0.6))
        s.pause(0.3)
    schritt(s, EIN([o_dots, l_unv], 0.6))
    s.speichern()


def k6zeilenadressen():
    """Die zehn Zeilen viermal (gekürzt auf den Namen): 2,4 → Zeilen 2 bis 4, $ → letzte, /Clara/ → 4 und 8, 1 → Kopfzeile."""
    s = Szene("linux/k6zeilenadressen", reihenfolge="anlegen")
    kurz = ["datum,name,…"] + ["…,%s,…" % z.split(",")[1] for z in LAEUFE[1:]]
    ys = [r4(1.0 - 0.21 * i) for i in range(10)]
    spalten = (("2,4", (1, 2, 3), "z24", ("Zeilen 2 bis 4", "lines 2 to 4", "líneas 2 a 4", "第 2 至 4 行", "lignes 2 à 4",
                                          "2. ile 4. satırlar")),
               ("$", (9,), "zl", ("letzte Zeile", "last line", "última línea", "最后一行", "dernière ligne", "son satır")),
               ("/Clara/", (3, 7), "zc", ("Zeilen mit Clara", "lines with Clara", "líneas con Clara", "含 Clara 的行",
                                          "lignes avec Clara", "Clara içeren satırlar")),
               ("1", (0,), "zk", ("Kopfzeile", "header line", "línea de cabecera", "表头行", "ligne d'en-tête", "başlık satırı")))
    l_h = L(s, "kopf", ("Zeilenadressen", "line addresses", "direcciones de línea", "行地址", "adresses de ligne", "satır adresleri"),
            (0.03, 1.75), FM, "center", GRAU)
    basis, adr, erg = [], [], []
    for (a, idx, key, w), x in zip(spalten, (-3.05, -1.4, 0.25, 1.9)):
        xc = r4(x + 0.6)
        mk = [mark(s, x - 0.03, x + 1.2, ys[i], 0.19, GRUEN, 0.3) for i in idx]
        nr = [tt(s, str(i + 1), x + 0.16, y, E2, GRAU, "r") for i, y in enumerate(ys)]
        tx = [tt(s, k, x + 0.22, y, E2) for k, y in zip(kurz, ys)]
        basis += nr + tx
        adr.append(ttm(s, a, xc, 1.4, 0.19, ORANGE))
        erg.append((mk + [L(s, key, w, (xc, -1.25), FM, "center", GRUEN)], [tx[i] for i in idx]))
    schritt(s, EIN(basis + [l_h], 0.7))
    for k in range(4):
        s.pause(0.5)
        schritt(s, EIN(adr[k], 0.5))
        schritt(s, EIN(erg[k][0], 0.6), BETONE(erg[k][1], 0.7))
    s.speichern()


def k6gruppen():
    """2026-11-02 und ^([0-9]{4})-([0-9]{2})-([0-9]{2}): die Gruppen färben 2026 (1), 11 (2), 02 (3); der Ersatz \\3.\\2.\\1
    holt die Stücke in neuer Reihenfolge: 02.11.2026."""
    s = Szene("linux/k6gruppen", reihenfolge="anlegen")
    farb = (BLAU, GRUEN, ORANGE)

    def marke(x, y, n, f):
        return [s.kreis(None, r4(x), r4(y), 0.12, farbe=f, dicke=2, fuellung=WEISS, deckung=1.0),
                text(s, str(n), (r4(x), r4(y)), FM, "center", f)]
    emA, xA, yA = 0.17, -1.2, 1.5
    gA = ((1, 10), (12, 21), (23, 32))
    mA = [mark(s, sp(xA, a, emA) - 0.005, sp(xA, b + 1, emA) + 0.005, yA, 0.26, f, 0.3) for (a, b), f in zip(gA, farb)]
    l_A = L(s, "ausdr", W_AUSDR2, (xA - 0.12, yA), FM, "right", GRAU)
    tA = tt(s, "^([0-9]{4})-([0-9]{2})-([0-9]{2})", xA, yA, emA)
    nA = [marke(msp(xA, a, b, emA), yA + 0.3, g + 1, f) for g, ((a, b), f) in enumerate(zip(gA, farb))]
    em = 0.26
    datum, yD = "2026-11-02", 0.75
    xD = r4(-len(datum) * cw(em) / 2)
    stD = ((0, 3), (5, 6), (8, 9))
    erg_st = ((6, 9), (3, 4), (0, 1))                  # Platz der Gruppe 1, 2, 3 im Ergebnis 02.11.2026
    yE, yR = -0.25, -1.05
    mR = [mark(s, sp(xD, a, em) - 0.01, sp(xD, b + 1, em) + 0.01, yR, 0.38, f, 0.3) for (a, b), f in zip(erg_st, farb)]
    mD = [mark(s, sp(xD, a, em) - 0.01, sp(xD, b + 1, em) + 0.01, yD, 0.38, f, 0.3) for (a, b), f in zip(stD, farb)]
    l_D = L(s, "datum", ("Datum:", "date:", "fecha:", "日期：", "date :", "tarih:"), (xD - 0.15, yD), FM, "right", GRAU)
    tD = [tt(s, datum[a:b + 1], sp(xD, a, em), yD, em) for a, b in stD] + [tt(s, "-", sp(xD, k, em), yD, em) for k in (4, 7)]
    kop = [tt(s, datum[a:b + 1], sp(xD, a, em), yD, em) for a, b in stD]
    nD = [marke(msp(xD, a, b, em), yD - 0.36, g + 1, f) for g, ((a, b), f) in enumerate(zip(stD, farb))]
    ers = "\\3.\\2.\\1"
    xE = r4(-len(ers) * cw(em) / 2)
    stE = ((0, 1, 2), (3, 4, 1), (6, 7, 0))
    mE = [mark(s, sp(xE, a, em) - 0.01, sp(xE, b + 1, em) + 0.01, yE, 0.38, farb[g], 0.3) for a, b, g in stE]
    l_E = L(s, "ersatz", ("Ersatz:", "replacement:", "reemplazo:", "替换：", "remplacement :", "değiştirme metni:"), (xE - 0.15, yE),
            FM, "right", GRAU)
    tE = [tt(s, ers[a:b + 1], sp(xE, a, em), yE, em) for a, b, _g in stE] + [tt(s, ".", sp(xE, k, em), yE, em) for k in (2, 5)]
    l_R = L(s, "erg", ("Ergebnis:", "result:", "resultado:", "结果：", "résultat :", "sonuç:"), (xD - 0.15, yR), FM, "right", GRAU)
    tRp = [tt(s, ".", sp(xD, k, em), yR, em) for k in (2, 5)]
    schritt(s, EIN([l_A, tA, l_D] + tD + kop, 0.7))
    s.pause(0.6)
    for g in range(3):
        schritt(s, EIN([mA[g], mD[g]] + nA[g] + nD[g], 0.6), BETONE(kop[g], 0.7))
    s.pause(0.6)
    schritt(s, EIN([l_E] + mE + tE, 0.6))
    s.pause(0.4)
    schritt(s, EIN(l_R, 0.4))
    for k, g in enumerate((2, 1, 0)):
        a, b = erg_st[g]
        schritt(s, ZU(kop[g], msp(xD, a, b, em), yR, 0.9), EIN(mR[g], 0.6), BETONE(tE[k], 0.8))
        if k < 2:
            schritt(s, EIN(tRp[k], 0.3))
    s.speichern()


def k6sedi():
    """sed -i 's/Ben/Benjamin/' kopie.csv: sed liest die alte Datei und schreibt jede Zeile in eine neue Datei daneben; am Ende
    übernimmt die neue Datei den Namen kopie.csv, die alte verschwindet (gestrichelter Umriss)."""
    s = Szene("linux/k6sedi", reihenfolge="anlegen")
    alt = LAEUFE[:3]
    neu = [z.replace("Ben", "Benjamin") for z in alt]
    yz = (0.7, 0.48, 0.26, 0.04)
    xa, xn, xs_, ys_ = -3.27, 0.87, -0.55, 0.3
    t_cmd = tt(s, "$ sed -i 's/Ben/Benjamin/' kopie.csv", -3.3, 1.65, E2)
    geist_ = box(s, (-2.35, 0.3), 2.0, 1.15, HELLGRAU, WEISS, 2, "rect", DASH, 0.0)
    ab = box(s, (-2.35, 0.3), 2.0, 1.15, GRAU, WEISS, 2, "rect")
    a_name = tt(s, "kopie.csv", -2.35, 1.07, E2, SCHWARZ, "m")
    al = [tt(s, z, xa, y, E2) for z, y in zip(alt, yz)] + [tt(s, "…", xa, yz[3], E2)]
    sb = box(s, (xs_, ys_), 0.7, 0.45, BLAU, BLAU_HELL, 2.5, "round")
    s_t = ttm(s, "sed", xs_, ys_)
    nb = box(s, (2.0, 0.3), 2.45, 1.15, GRAU, WEISS, 2, "rect")
    mben = mark(s, sp(xn, 11, E2) - 0.01, sp(xn, 19, E2) + 0.01, yz[2], 0.2, ORANGE, 0.35)
    n_dots = tt(s, "…", xn, yz[3], E2)
    l_neu = L(s, "neu", ("neue Datei", "new file", "archivo nuevo", "新文件", "nouveau fichier", "yeni dosya"), (2.0, 1.07), FM,
              "center", GRAU)
    pa = [pf(s, (-1.32, ys_), (-0.93, ys_), farbe=GRAU, spitze=0.08), pf(s, (-0.17, ys_), (0.72, ys_), farbe=GRAU, spitze=0.08)]
    l_alt = L(s, "alt", ("alte Datei: bleibt unverändert", "old file: stays unchanged", "archivo viejo: no cambia", "旧文件：保持不变",
                         "ancien fichier : inchangé", "eski dosya: değişmez"), (-2.35, -0.5), FM, "center", GRAU)
    l_alt2 = L(s, "alt2", ("alte Datei: am Ende entfernt", "old file: removed at the end", "archivo viejo: borrado al final",
                           "旧文件：最后被删除", "ancien fichier : supprimé à la fin", "eski dosya: sonunda silinir"),
               (-2.35, -0.5), FM, "center", GRAU)
    l_neu2 = L(s, "neu2", ("neue Datei daneben", "new file next to it", "archivo nuevo al lado", "旁边的新文件",
                           "nouveau fichier à côté", "yanında yeni dosya"), (2.0, -0.5), FM, "center", GRAU)
    l_neu3 = L(s, "neu3", ("übernimmt den Namen", "takes over the name", "toma el nombre", "获得这个名字", "reprend le nom",
                           "adı devralır"), (2.0, -0.5), FM, "center", ORANGE)
    kop = [tt(s, z, xa, y, E2) for z, y in zip(alt, yz)]
    ben = ttm(s, neu[2], xs_, ys_, E2)
    schritt(s, EIN([t_cmd, geist_, ab, a_name] + al + kop + [sb, s_t], 0.7))
    s.pause(0.6)
    schritt(s, EIN([nb, l_neu, l_neu2, l_alt], 0.6), ZEICHNE(pa, 0.6))
    s.pause(0.4)
    for i in range(2):
        schritt(s, ZU(kop[i], xs_, ys_, 0.6))
        schritt(s, ZU(kop[i], mitte_tt(xn, alt[i], E2), yz[i], 0.6))
    schritt(s, ZU(kop[2], xs_, ys_, 0.6))
    schritt(s, AUS(kop[2], 0.4), EIN(ben, 0.5), BETONE(s_t, 0.7))
    schritt(s, ZU(ben, mitte_tt(xn, neu[2], E2), yz[2], 0.7))
    schritt(s, EIN([mben, n_dots], 0.5))
    s.pause(0.6)
    schritt(s, AUS([ab] + al + [l_alt, l_neu, l_neu2], 0.7), ZU(a_name, 2.0, 1.07, 0.9), EIN([l_alt2, l_neu3], 0.7))
    s.speichern()


# ================================================================== Abschnitt 9: awk
def k6regeln():
    """awk-Programm aus zwei Regeln; die Zeilen Anna, Ben, Clara kommen nacheinander, beide Regeln werden von oben geprüft:
    bei Clara leuchten beide und schreiben, sonst nur die zweite (ohne Bedingung)."""
    s = Szene("linux/k6regeln", reihenfolge="anlegen")
    r1 = '/Clara/ {print "Clara ist gelaufen"}'
    r2 = '{print "Zeile gelesen"}'
    xr, y1, y2 = -3.3, 1.2, 0.45
    x2 = r4(sp(xr, 8, E2))
    l_p = L(s, "prog", ("awk-Programm", "awk program", "programa awk", "awk 程序", "programme awk", "awk programı"), (-3.35, 1.65),
            FM, "left", GRAU)
    b1 = box(s, (-1.85, y1), 3.1, 0.38, GRAU, WEISS, 2, "rect")
    g1 = box(s, (-1.85, y1), 3.1, 0.38, GRUEN, GRUEN_HELL, 2.5, "rect")
    rot = [mark(s, xr - 0.02, sp(xr, 7, E2) + 0.02, y1, 0.26, ROT, 0.25) for _ in range(2)]
    t1 = tt(s, r1, xr, y1, E2)
    b2 = box(s, (-1.85, y2), 3.1, 0.38, GRAU, WEISS, 2, "rect")
    g2 = [box(s, (-1.85, y2), 3.1, 0.38, GRUEN, GRUEN_HELL, 2.5, "rect") for _ in range(3)]
    t2 = tt(s, r2, x2, y2, E2)
    w_b = ("Bedingung", "condition", "condición", "条件", "condition", "koşul")
    w_a = ("Aktion", "action", "acción", "动作", "action", "eylem")
    lab = [L(s, "b1", w_b, (msp(xr, 0, 6, E2), y1 - 0.32), FM, "center", GRAU),
           L(s, "a1", w_a, (msp(xr, 8, 35, E2), y1 - 0.32), FM, "center", GRAU),
           L(s, "b2", ("keine Bedingung", "no condition", "sin condición", "无条件", "pas de condition", "koşul yok"),
             (xr, y2 - 0.32), FM, "left", GRAU),
           L(s, "a2", w_a, (msp(x2, 0, 22, E2), y2 - 0.32), FM, "center", GRAU)]
    zl = LAEUFE[1:4]
    xi, yi = 0.95, (1.4, 1.18, 0.96)
    l_e = L(s, "ein", W_EING, (xi, 1.68), FM, "left", GRAU)
    cur = mark(s, xi - 0.04, xi + 23 * C2 + 0.04, yi[0], 0.2, ORANGE, 0.3)
    ti = [tt(s, z, xi, y, E2) for z, y in zip(zl, yi)]
    ptr = pf(s, (0.45, y1), (-0.22, y1), farbe=ORANGE, dicke=3, spitze=0.09)
    ob = term_kasten(s, (2.15, -0.45), 2.4, 1.1)
    l_o = L(s, "aus", W_AUSG, (xi, 0.3), FM, "left", GRAU)
    yo = (-0.07, -0.29, -0.51, -0.73)
    ausg = ("Zeile gelesen", "Zeile gelesen", "Clara ist gelaufen", "Zeile gelesen")
    mo = mark(s, 1.02, 1.08 + 18 * C2, yo[2], 0.2, GRUEN, 0.3)
    to = [tt(s, a, 1.05, y, E2) for a, y in zip(ausg, yo)]
    schritt(s, EIN([l_p, b1, t1, b2, t2] + lab, 0.7))
    s.pause(0.6)
    schritt(s, EIN([l_e] + ti + [ob, l_o], 0.6))
    s.pause(0.6)
    k, vorher = 0, []
    for i, z in enumerate(zl):
        if i == 0:
            schritt(s, EIN([cur, ptr], 0.5))
        else:
            schritt(s, VER(cur, 0, yi[i] - yi[i - 1], 0.5), VER(ptr, 0, y1 - y2, 0.5), AUS(vorher, 0.4))
        if "Clara" in z:
            schritt(s, EIN([g1, to[k]], 0.6))
            vorher = [g2[i]]
            k += 1
        else:
            schritt(s, EIN(rot[i], 0.5))
            vorher = [rot[i], g2[i]]
        schritt(s, VER(ptr, 0, y2 - y1, 0.5), EIN([g2[i], to[k]], 0.6))
        k += 1
        s.pause(0.3)
    schritt(s, AUS(ptr, 0.4), EIN(mo, 0.6))
    s.speichern()


def k6awkfelder():
    """2026-11-08,Ben,21.1,128 mit -F,: $1 bis $4 über den Feldern, ein Bogen $0 über der ganzen Zeile; rechts NF = 4, $NF zeigt
    auf das letzte Feld; links NR = 9."""
    s = Szene("linux/k6awkfelder", reihenfolge="anlegen")
    z = LAEUFE[8]
    em, y0 = 0.22, -0.05
    x0 = r4(-len(z) * cw(em) / 2)
    fl, kommas = felder(z)
    mk = [mark(s, sp(x0, k, em) + 0.005, sp(x0, k + 1, em) - 0.005, y0, 0.36, ORANGE, 0.4) for k in kommas]
    tf = [tt(s, f, sp(x0, a, em), y0, em) for a, b, f in fl]
    tk = [tt(s, ",", sp(x0, k, em), y0, em) for k in kommas]
    t_F = tt(s, "-F,", -3.3, 1.55, 0.19)
    l_F = L(s, "F", ("Trennzeichen: Komma", "separator: comma", "separador: coma", "分隔符：逗号", "séparateur : virgule",
                     "ayırıcı: virgül"), (-2.9, 1.55), FM, "left", ORANGE)
    kl = [klammer(s, sp(x0, a, em) + 0.02, sp(x0, b + 1, em) - 0.02, y0 + 0.24, unten=False, farbe=BLAU, t=0.06, dicke=2)
          for a, b, f in fl]
    tn = [ttm(s, "$%d" % (j + 1), msp(x0, a, b, em), y0 + 0.45, 0.19, BLAU) for j, (a, b, f) in enumerate(fl)]
    breite = r4(len(z) * cw(em) + 0.08)
    arc = s.weg(None, "%s+%s*t" % (r4(x0 - 0.04), breite), "%s+0.32*4*t*(1-t)" % r4(y0 + 0.66), 0, 1, farbe=BLAU, dicke=2.5, n=41)
    t0 = ttm(s, "$0", 0, r4(y0 + 1.15), 0.19, BLAU)
    xr = r4(sp(x0, len(z), em) + 0.25)
    t_nf = tt(s, "NF = 4", xr, y0, 0.19)
    l_nf = L(s, "nf", ("Zahl der Felder", "number of fields", "número de campos", "字段数", "nombre de champs", "alan sayısı"),
             (xr, r4(y0 - 0.32)), FM, "left", GRAU)
    x4 = r4(msp(x0, fl[3][0], fl[3][1], em))
    a_nf = pf(s, (x4, r4(y0 - 0.68)), (x4, r4(y0 - 0.24)), farbe=BLAU, spitze=0.08)
    t_dnf = ttm(s, "$NF", x4, r4(y0 - 0.83), 0.19, BLAU)
    l_dnf = L(s, "dnf", ("das letzte Feld", "the last field", "el último campo", "最后一个字段", "le dernier champ", "son alan"),
              (r4(x4 + 0.3), r4(y0 - 0.83)), FM, "left", GRAU)
    xl = r4(x0 - 0.25)
    t_nr = tt(s, "NR = 9", xl, y0, 0.19, SCHWARZ, "r")
    l_nr = L(s, "nr", ("Zeilennummer", "line number", "número de línea", "行号", "numéro de ligne", "satır numarası"),
             (xl, r4(y0 - 0.32)), FM, "right", GRAU)
    schritt(s, EIN(tf + tk + [t_F, l_F], 0.6))
    schritt(s, EIN(mk, 0.6), BETONE(tk, 0.7))
    s.pause(0.6)
    for j in range(4):
        schritt(s, ZEICHNE(kl[j], 0.45), EIN(tn[j], 0.45))
    s.pause(0.6)
    schritt(s, ZEICHNE(arc, 0.7), EIN(t0, 0.6))
    s.pause(0.6)
    schritt(s, EIN([t_nf, l_nf], 0.5))
    schritt(s, ZEICHNE(a_nf, 0.6), EIN([t_dnf, l_dnf], 0.6), BETONE(tn[3], 0.8))
    s.pause(0.6)
    schritt(s, EIN([t_nr, l_nr], 0.5))
    s.speichern()


def k6mittel():
    """Rechenbild: Annas Strecken 5,0 + 6,4 + 12,0 + 5,0, Zwischensummen 5,0, 11,4, 23,4, 28,4, dann ÷ 4 = 7,1."""
    s = Szene("linux/k6mittel", reihenfolge="anlegen")
    werte = (5.0, 6.4, 12.0, 5.0)
    summen = [round(v, 1) for v in itertools.accumulate(werte)]
    xs = [r4(-2.5 + 1.0 * i) for i in range(4)]
    y1, y2 = 0.45, -0.35
    xr = 2.25
    rb = box(s, (xr, y2), 0.75, 0.4, BLAU, BLAU_HELL, 2.5)
    l1 = L(s, "km", ("Annas Strecken in km", "Anna's distances in km", "distancias de Anna en km", "Anna 的距离（公里）",
                     "distances d'Anna en km", "Anna'nın mesafeleri (km)"), (-3.3, 0.9), FM, "left", GRAU)
    l2 = L(s, "zw", ("Zwischensummen", "running totals", "sumas parciales", "部分和", "sommes partielles", "ara toplamlar"),
           (-3.3, -0.78), FM, "left", GRUEN)
    tw = [text(s, "%.1f" % w, (x, y1), FS) for w, x in zip(werte, xs)]
    tp = [text(s, "+", (r4(x + 0.5), y1), FS, "center", GRAU) for x in xs[:-1]]
    vp = [pf(s, (x, y1 - 0.16), (x, y2 + 0.17), farbe=HELLGRAU, dicke=2, spitze=0.08) for x in xs]
    hp = [pf(s, (r4(xs[i - 1] + 0.3), y2), (r4(xs[i] - 0.3), y2), farbe=HELLGRAU, dicke=2, spitze=0.08) for i in range(1, 4)]
    ts = [text(s, "%.1f" % v, (x, y2), FS, "center", GRUEN) for v, x in zip(summen, xs)]
    xa, xb = r4(xs[3] + 0.35), r4(xr - 0.42)
    pd = pf(s, (xa, y2), (xb, y2), farbe=BLAU, dicke=2.5, spitze=0.09)
    t_d = text(s, "÷ 4", (r4((xa + xb) / 2), y2 + 0.22), FS, "center", BLAU)
    l_n = L(s, "laeufe", ("4 Läufe", "4 runs", "4 carreras", "4 次跑步", "4 courses", "4 koşu"), (r4((xa + xb) / 2), y2 - 0.22),
            FM, "center", GRAU)
    t_r = text(s, "7.1", (xr, y2), FS, "center", BLAU)
    l_end = L(s, "end", ("mittlere Strecke: 7.1 km", "mean distance: 7.1 km", "distancia media: 7.1 km", "平均距离：7.1 公里",
                         "distance moyenne : 7.1 km", "ortalama mesafe: 7.1 km"), (3.3, -1.0), FK, "right", BLAU)
    schritt(s, EIN(tw + tp + [l1], 0.8))
    s.pause(0.6)
    schritt(s, ZEICHNE(vp[0], 0.5), EIN([ts[0], l2], 0.5), BETONE(tw[0], 0.6))
    for i in range(1, 4):
        schritt(s, ZEICHNE([vp[i], hp[i - 1]], 0.5), EIN(ts[i], 0.5), BETONE([tw[i], ts[i - 1]], 0.6))
    s.pause(0.6)
    schritt(s, ZEICHNE(pd, 0.6), EIN([t_d, l_n], 0.6), BETONE(ts[3], 0.7))
    schritt(s, EIN([rb, t_r], 0.6))
    s.pause(0.4)
    schritt(s, EIN(l_end, 0.6))
    s.speichern()


def k6array():
    """Die neun Datensätze laufen ein; rechts die Tabelle Schlüssel / s / n: neue Namen legen eine Zeile an, weitere Läufe erhöhen
    sie; am Ende Anna 28,4 / 4, Ben 36,6 / 3, Clara 15,2 / 2."""
    s = Szene("linux/k6array", reihenfolge="anlegen")
    zl = LAEUFE[1:]
    x0 = -3.35
    ys = [r4(1.0 - 0.22 * i) for i in range(9)]
    cur = mark(s, x0 - 0.04, x0 + 23 * C2 + 0.04, ys[0], 0.2, ORANGE, 0.3)
    tz = [tt(s, z, x0, y, E2) for z, y in zip(zl, ys)]
    l_akt = L(s, "akt", ("für jede Zeile:", "for each line:", "para cada línea:", "对每一行：", "pour chaque ligne :",
                         "her satır için:"), (0.75, 1.5), FM, "right", GRAU)
    t_akt = tt(s, "{s[$2] += $3; n[$2]++}", 0.84, 1.5, 0.17)
    xk, xsv, xn = 1.0, 2.15, 2.95
    l_k = L(s, "schl", ("Schlüssel", "key", "clave", "键", "clé", "anahtar"), (xk, 1.0), FM, "center", DUNKEL)
    t_sh = ttm(s, "s", xsv, 1.0, 0.19)
    t_nh = ttm(s, "n", xn, 1.0, 0.19)
    hl = linie(s, (0.35, 0.83), (3.3, 0.83), HELLGRAU, 1.5)
    a = pf(s, (-1.35, 0.15), (0.25, 0.15), farbe=GRAU, spitze=0.1)
    ry = {"Anna": 0.6, "Ben": 0.3, "Clara": 0.0}
    erst = {}
    for z in zl:
        n, km = z.split(",")[1], z.split(",")[2]
        erst.setdefault(n, km)
    rows = {n: [ttm(s, n, xk, y, 0.19), text(s, erst[n], (xsv, y), FK), text(s, "1", (xn, y), FK)] for n, y in ry.items()}
    schritt(s, EIN(tz + [l_akt, t_akt], 0.6))
    schritt(s, EIN([l_k, t_sh, t_nh, hl], 0.6), ZEICHNE(a, 0.6))
    s.pause(0.6)
    summe, anz = {}, {}
    for i, z in enumerate(zl):
        n, km = z.split(",")[1], float(z.split(",")[2])
        with s.gleichzeitig():
            if i == 0:
                schritt(s, EIN(cur, 0.4))
            else:
                schritt(s, VER(cur, 0, ys[i] - ys[i - 1], 0.4))
            if n not in summe:
                summe[n], anz[n] = km, 1
                schritt(s, EIN(rows[n], 0.5))
            else:
                summe[n], anz[n] = round(summe[n] + km, 1), anz[n] + 1
                s.ersetzen(rows[n][1], "%.1f" % summe[n], dauer=0.5)
                s.ersetzen(rows[n][2], str(anz[n]), dauer=0.5)
                schritt(s, BETONE(rows[n][0], 0.6))
        s.pause(0.15)
    schritt(s, AUS(cur, 0.4))
    s.speichern()


# ================================================================== Abschnitt 10: Werkzeuge zusammen
def k6werkzeuge():
    """Das Lauftagebuch als Tabelle (Raster), fünfmal: grep/sed -n ganze Zeilen, cut eine Spalte, sort neue Reihenfolge (Balken
    der Schlüsselspalte ordnen sich), tr/sed Zeichen in Zellen, uniq -c/awk: viele Zeilen werden wenige Ergebniszeilen."""
    s = Szene("linux/k6werkzeuge", reihenfolge="anlegen")
    zb, zh = 0.24, 0.14

    def kopf(xm, top, spalten=4):
        return box(s, (xm, r4(top - zh / 2)), spalten * zb, zh, GRAU_HELL, GRAU_HELL, 0, "rect")

    def linien(xm, top, spalten=4, zeilen=6):
        le, re, un = r4(xm - spalten * zb / 2), r4(xm + spalten * zb / 2), r4(top - zeilen * zh)
        return ([linie(s, (le, r4(top - k * zh)), (re, r4(top - k * zh)), GRAU, 1.2) for k in range(zeilen + 1)] +
                [linie(s, (r4(le + j * zb), top), (r4(le + j * zb), un), GRAU, 1.2) for j in range(spalten + 1)])

    def zelle(xm, top, z, sp_, farbe, spalten=4):
        le = xm - spalten * zb / 2
        return mark(s, r4(le + sp_ * zb), r4(le + (sp_ + 1) * zb), r4(top - (z + 0.5) * zh), zh, farbe, 0.4)

    def zeile_(xm, top, z, farbe, spalten=4):
        return mark(s, r4(xm - spalten * zb / 2), r4(xm + spalten * zb / 2), r4(top - (z + 0.5) * zh), zh, farbe, 0.4)
    tA, tB = 1.15, -0.4
    xA = (-2.3, 0.0, 2.3)
    l_t = L(s, "titel", ("das Lauftagebuch als Tabelle: Zeile = Datensatz, Spalte = Feld",
                         "the running log as a table: line = record, column = field",
                         "el diario de carreras como tabla: línea = registro, columna = campo", "跑步记录作为表格：行 = 记录，列 = 字段",
                         "le journal de course en tableau : ligne = enregistrement, colonne = champ",
                         "tablo olarak koşu günlüğü: satır = kayıt, sütun = alan"), (0, 1.75), FM, "center", GRAU)
    raster = []
    # grep, sed -n
    raster.append(kopf(xA[0], tA))
    e1 = [zeile_(xA[0], tA, z, GRUEN) for z in (2, 4)]
    raster += linien(xA[0], tA)
    # cut
    raster.append(kopf(xA[1], tA))
    le = xA[1] - 2 * zb
    e2 = mark(s, r4(le + zb), r4(le + 2 * zb), r4(tA - 3 * zh), 6 * zh, GRUEN, 0.4)
    raster += linien(xA[1], tA)
    # sort
    raster.append(kopf(xA[2], tA))
    werte = (0.55, 0.2, 0.85, 0.35, 0.7)
    rang = {v: i for i, v in enumerate(sorted(werte))}
    le = xA[2] - 2 * zb
    balken, ziele = [], []
    for z, v in enumerate(werte, 1):
        xm = r4(le + 2 * zb + 0.02 + v * 0.1)
        balken.append(box(s, (xm, r4(tA - (z + 0.5) * zh)), r4(v * 0.2), 0.08, BLAU, BLAU, 0, "rect"))
        ziele.append((xm, r4(tA - (rang[v] + 1.5) * zh)))
    raster += linien(xA[2], tA)
    a_s = pf(s, (r4(xA[2] + 0.62), r4(tA - 0.2)), (r4(xA[2] + 0.62), r4(tA - 0.78)), farbe=BLAU, dicke=2.5, spitze=0.07)
    # tr, sed
    raster.append(kopf(xA[0], tB))
    e4 = [zelle(xA[0], tB, z, sp_, ORANGE) for z, sp_ in ((1, 1), (3, 1), (5, 1), (2, 3))]
    raster += linien(xA[0], tB)
    # uniq -c, awk
    raster.append(kopf(xA[1], tB))
    gruppen = (GRUEN, BLAU, ORANGE, GRUEN, BLAU)
    e5 = [zelle(xA[1], tB, z, 1, f) for z, f in enumerate(gruppen, 1)]
    raster += linien(xA[1], tB)
    erg = [kopf(xA[2], tB, 2)] + [zeile_(xA[2], tB, z, f, 2) for z, f in enumerate((GRUEN, BLAU, ORANGE), 1)]
    erg += linien(xA[2], tB, 2, 4)
    a_u = pf(s, (0.6, r4(tB - 3 * zh)), (r4(xA[2] - 0.38), r4(tB - 3 * zh)), farbe=GRAU, spitze=0.09)
    namen = [ttm(s, n, x, r4(t + 0.22), E2) for n, x, t in (("grep, sed -n", xA[0], tA), ("cut", xA[1], tA), ("sort", xA[2], tA),
                                                           ("tr, sed", xA[0], tB), ("uniq -c, awk", xA[1], tB))]
    w = ((("ganze Zeilen", "whole lines", "líneas enteras", "整行", "lignes entières", "satırların tamamı"), xA[0], tA),
         (("eine Spalte", "one column", "una columna", "一列", "une colonne", "bir sütun"), xA[1], tA),
         (("neue Reihenfolge", "new order", "nuevo orden", "新顺序", "nouvel ordre", "yeni sıra"), xA[2], tA),
         (("Zeichen in Zellen", "characters in cells", "caracteres en celdas", "单元格中的字符", "caractères dans les cellules",
           "hücrelerdeki karakterler"), xA[0], tB),
         (("viele Zeilen werden wenige Ergebniszeilen", "many lines become a few result lines",
           "muchas líneas se convierten en pocas líneas de resultado", "多行变成少量结果行",
           "beaucoup de lignes deviennent quelques lignes de résultat", "çok satır, birkaç sonuç satırına iner"),
          r4((xA[1] + xA[2]) / 2), tB))
    lab = [L(s, "w%d" % k, ww, (x, r4(t - 6 * zh - 0.21)), FM, "center", GRUEN if k < 2 else (BLAU if k == 2 else
                                                                                           (ORANGE if k == 3 else DUNKEL)))
           for k, (ww, x, t) in enumerate(w)]
    schritt(s, EIN([l_t] + raster, 0.8))
    s.pause(0.4)
    schritt(s, EIN(namen[0], 0.4))
    schritt(s, EIN(e1 + [lab[0]], 0.6))
    s.pause(0.4)
    schritt(s, EIN(namen[1], 0.4))
    schritt(s, EIN([e2, lab[1]], 0.6))
    s.pause(0.4)
    schritt(s, EIN([namen[2]] + balken, 0.5))
    schritt(s, *[ZU(b, x, y, 0.9) for b, (x, y) in zip(balken, ziele)], ZEICHNE(a_s, 0.9), EIN(lab[2], 0.6))
    s.pause(0.4)
    schritt(s, EIN(namen[3], 0.4))
    schritt(s, EIN(e4 + [lab[3]], 0.6))
    s.pause(0.4)
    schritt(s, EIN(namen[4], 0.4))
    schritt(s, EIN(e5, 0.5))
    schritt(s, ZEICHNE(a_u, 0.6), EIN(erg + [lab[4]], 0.7))
    s.speichern()


SZENEN_1 = (k6tabelle, k6zeilenende, k6ausschnitt, k6tailf,            # Abschnitte 1–5 (Phase 2b-1)
            k6cut, k6tr, k6paste, k6minuten,
            k6lexnum, k6schluessel, k6uniq, k6haeufigkeit,
            k6seq, k6diff,
            k6grep, k6grepo, k6grepr)
SZENEN_2 = (k6menge, k6klammer, k6klassen, k6anker,                    # Abschnitte 6–10 (Phase 2b-2)
            k6grundform, k6quantor, k6gierig, k6automat,
            k6sed, k6zeilenadressen, k6gruppen, k6sedi,
            k6regeln, k6awkfelder, k6mittel, k6array,
            k6werkzeuge)
SZENEN = SZENEN_1 + SZENEN_2

if __name__ == "__main__":
    wahl = set(sys.argv[1:])
    for f in SZENEN:
        if not wahl or f.__name__ in wahl:
            f()
