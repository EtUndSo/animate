"""Cybersecurity Teil 1 (C:\\Bücher\\EtUndSo\\Cybersecurity\\Arbeitshefte\\kap1_stufen.tex, kap1_stufen_b.tex): Abbildungen.

Szenenname cyber/k1<name> = \\label{fig:k1<name>} im Heft. Stil wie tools/szenen/et3_teil2.py.
Bauen:  python tools/szenen/cyber_teil1.py
Export: python tools/export_szenen.py cyber/k1<name> ...   (jedes Bild höchstens 548 px breit)
"""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from szenen_lib import *  # noqa: E402,F403

KLEIN = 22                 # zweite Zeilen, Beispiele, Pfeiltexte (Untergrenze)
MITTEL = 24
GRUEN_HELL = "#e6f3ea"
ROT_HELL = "#fbe9e9"


def kasten(s, mitte, breite, hoehe, text, groesse=MITTEL, farbe=SCHWARZ, textfarbe=None, fuellung="#ffffff", dash="", dicke=2.5):
    """Abgerundeter Kasten mit zentriertem Text (mehrzeilig mit \\n)."""
    s.box("", mitte, breite=breite, hoehe=hoehe, form="round", farbe=farbe, fuellung=fuellung, deckung=1, dicke=dicke, dash=dash)
    s.text(None, text, mitte, groesse, "center", textfarbe or farbe)


def kasten2(s, mitte, breite, hoehe, haupt, klein, fuellung="#ffffff"):
    """Kasten mit Begriff (oben) und grauem Beispiel (unten)."""
    s.box("", mitte, breite=breite, hoehe=hoehe, form="round", fuellung=fuellung, deckung=1, dicke=2.5)
    s.text(None, haupt, (mitte[0], mitte[1] + 0.16), MITTEL, "center")
    s.text(None, klein, (mitte[0], mitte[1] - 0.17), KLEIN, "center", GRAU)


# ------------------------------------------------------------------ Abschnitt 1
def k1brief():
    """Brief vom Absender zum Empfänger; drei Störer und die drei Schutzziele."""
    s = Szene("cyber/k1brief")
    ab = s.tr("absender", "Absender", "Sender", "Remitente", "发件人")
    em = s.tr("empfaenger", "Empfänger", "Recipient", "Destinatario", "收件人")
    kasten(s, (-2.85, 0), 1.3, 0.6, ab)
    kasten(s, (2.85, 0), 1.3, 0.6, em)
    s.pfeil((-2.2, 0), (2.2, 0), dicke=3, spitze=0.18)
    # Briefumschlag
    s.box("", (-1.8, 0), breite=0.44, hoehe=0.3, form="rect", fuellung="#ffffff", deckung=1, dicke=2.5)
    s.linie(None, (-2.02, 0.15), (-1.8, -0.01), dicke=2.5)
    s.linie(None, (-1.8, -0.01), (-1.58, 0.15), dicke=2.5)
    taeter = ((-0.85, BLAU, s.tr("liest", "liest mit", "reads along", "lee", "偷看"),
               s.tr("vertr", "Vertraulichkeit", "Confidentiality", "Confidencialidad", "机密性")),
              (0.45, ROT, s.tr("aendert", "ändert ab", "alters", "modifica", "篡改"),
               s.tr("integr", "Integrität", "Integrity", "Integridad", "完整性")),
              (1.75, ORANGE, s.tr("haelt", "hält auf", "holds up", "retiene", "拦截"),
               s.tr("verfueg", "Verfügbarkeit", "Availability", "Disponibilidad", "可用性")))
    for x, farbe, tat, ziel in taeter:
        kasten(s, (x, 1.25), 1.25, 0.5, tat, MITTEL, farbe)
        s.pfeil((x, 0.99), (x, 0.08), farbe=farbe, dicke=3, spitze=0.16, dash=DASH)
        s.text(None, ziel, (x, -0.55), MITTEL, "center", farbe)
    s.speichern()


# ------------------------------------------------------------------ Abschnitt 2
def k1kette():
    """Schwachstelle und Bedrohung -> Angriff (mit Exploit) -> Schaden, am Beispiel eines Hauses."""
    s = Szene("cyber/k1kette")
    kasten2(s, (-2.4, 0.75), 2.15, 0.85, s.tr("schw", "Schwachstelle", "Vulnerability", "Vulnerabilidad", "漏洞"),
            s.tr("schw2", "Kellerfenster schließt nicht", "basement window won't close", "ventana que no cierra", "地下室窗户关不严"))
    kasten2(s, (-2.4, -0.75), 2.15, 0.85, s.tr("bedr", "Bedrohung", "Threat", "Amenaza", "威胁"),
            s.tr("bedr2", "Einbrecher in der Gegend", "burglars in the area", "ladrones en la zona", "附近有窃贼"))
    kasten2(s, (0.5, 0), 1.95, 0.85, s.tr("angr", "Angriff", "Attack", "Ataque", "攻击"),
            s.tr("angr2", "steigt durchs Fenster ein", "climbs in through the window", "entra por la ventana", "从窗户爬入"), fuellung=ROT_HELL)
    kasten2(s, (2.7, 0), 1.55, 0.85, s.tr("schad", "Schaden", "Damage", "Daño", "损害"),
            s.tr("schad2", "Laptop gestohlen", "laptop stolen", "portátil robado", "笔记本被盗"))
    s.pfeil((-1.325, 0.75), (-0.475, 0.08), dicke=3, spitze=0.16)
    s.pfeil((-1.325, -0.75), (-0.475, -0.08), dicke=3, spitze=0.16)
    s.pfeil((1.475, 0), (1.925, 0), dicke=3, spitze=0.14)
    ex = s.tr("exploit", "Exploit: Fenster mit\nSchraubenzieher aufhebeln", "Exploit: lever the window\nopen with a screwdriver",
              "Exploit: forzar la ventana\ncon un destornillador", "漏洞利用：用螺丝刀\n撬开窗户")
    s.text(None, ex, (0.5, 0.85), KLEIN, "center")
    s.speichern()


# ------------------------------------------------------------------ Abschnitt 3
def k1risiko():
    """Häufigkeit und Schaden doppelt logarithmisch; Linien gleichen Risikos; Ereignisse A und B."""
    s = Szene("cyber/k1risiko")
    xl = s.tr("xl", "Eintrittshäufigkeit H in 1/Jahr", "Frequency H in 1/year", "Frecuencia H en 1/año", "发生频率 H（1/年）")
    yl = s.tr("yl", "Schaden S je Ereignis in €", "Damage S per event in €", "Daño S por evento en €", "每次损失 S（欧元）")
    a = s.achsen((0.01, 100), (10, 1e6), breite=5.0, hoehe=3.4, mitte=(0.35, 0.05), xl=xl, yl=yl, xlog=True, ylog=True, gitter=True,
                 xticks="0.01;0.1;1;10;100", yticks="10;100;1000;10000;100000;1000000")
    s.daten(a, [(0.01, 500000), (100, 50)], farbe=ROT, dicke=3, dash=DASH)
    s.daten(a, [(0.01, 100000), (100, 10)], farbe=BLAU, dicke=3, dash=DASH)
    s.tr("projahr", "€/Jahr", "€/year", "€/año", "欧元/年")
    s.punkt(a, 0.1, 50000, farbe=ROT, r=0.08)
    s.text(a, "A: R = 5 000 @{projahr}", (0.14, 50000), MITTEL, "left", ROT)
    s.punkt(a, 10, 100, farbe=BLAU, r=0.08)
    s.text(a, "B: R = 1 000 @{projahr}", (6.5, 62), MITTEL, "right", BLAU)
    s.pfeil((0.7, 3000), (4, 20000), farbe=GRAU, dicke=3, spitze=0.16, on=a)
    s.text(a, s.tr("steigt", "Risiko steigt", "risk increases", "el riesgo aumenta", "风险增加"), (4.6, 24000), KLEIN, "left", GRAU)
    s.speichern()


# ------------------------------------------------------------------ Abschnitt 5
def k1toctou():
    """Zwei Geldautomaten: Prüfen zu t1/t2, Auszahlen zu t3/t4; Kontostand 100, 100, 0, -100."""
    s = Szene("cyber/k1toctou")
    y1, y2, yk, yt = 1.15, -0.15, -1.35, -1.85
    x0, x1 = -2.35, 3.55
    ts = (-1.3, 0.1, 1.5, 2.9)
    s.box("", ((ts[0] + ts[2]) / 2, y1), breite=ts[2] - ts[0], hoehe=0.62, form="rect", farbe=ROT_HELL, fuellung=ROT_HELL, deckung=1, dicke=0)
    s.text(None, s.tr("luecke", "Lücke zwischen Prüfen und Handeln", "gap between check and use", "hueco entre comprobar y actuar", "检查与使用之间的空隙"),
           ((ts[0] + ts[2]) / 2, y1 + 0.47), KLEIN, "center", ROT)
    for y, key, de, en, es, zh in ((y1, "a1", "Automat 1", "ATM 1", "Cajero 1", "取款机 1"), (y2, "a2", "Automat 2", "ATM 2", "Cajero 2", "取款机 2")):
        s.text(None, s.tr(key, de, en, es, zh), (x0 - 0.1, y), MITTEL, "right")
        s.linie(None, (x0, y), (x1, y), farbe=HELLGRAU, dicke=2)
    s.text(None, s.tr("stand", "Kontostand", "balance", "saldo", "余额"), (x0 - 0.1, yk), MITTEL, "right", GRAU)
    pr = s.tr("prueft", "prüft: 100 ≥ 100 ✓", "checks: 100 ≥ 100 ✓", "comprueba: 100 ≥ 100 ✓", "检查：100 ≥ 100 ✓")
    za = s.tr("zahlt", "zahlt 100 € aus,\nbucht ab", "pays out 100 €,\ndebits", "entrega 100 €,\ncarga", "支付 100 欧元，\n扣款")
    for (x, y, t) in ((ts[0], y1, pr), (ts[1], y2, pr), (ts[2], y1, za), (ts[3], y2, za)):
        s.punkt(None, x, y, r=0.07)
        s.text(None, t, (x, y - 0.38), KLEIN, "center")
    for x, k, farbe in ((ts[0], "100 €", GRAU), (ts[1], "100 €", GRAU), (ts[2], "0 €", GRAU), (ts[3], "−100 €", ROT)):
        s.text(None, k, (x, yk), MITTEL, "center", farbe)
    s.pfeil((x0, yt), (x1 + 0.1, yt), farbe=GRAU, dicke=2.5, spitze=0.15)
    s.text(None, s.tr("zeit", "Zeit", "time", "tiempo", "时间"), (x1 + 0.1, yt - 0.28), KLEIN, "right", GRAU)
    for x, t in zip(ts, ("t₁", "t₂", "t₃", "t₄")):
        s.linie(None, (x, yt + 0.07), (x, yt - 0.07), farbe=GRAU, dicke=2.5)
        s.text(None, t, (x, yt - 0.28), KLEIN, "center", GRAU)
    s.speichern()


# ------------------------------------------------------------------ Abschnitt 6
def k1schichten():
    """Drei Verteidigungslinien um den Schatz; Durchbruchswahrscheinlichkeiten multiplizieren sich."""
    s = Szene("cyber/k1schichten")
    cx, cy = 0.35, 0.3
    for b, h, deck in ((4.6, 2.7, 0.06), (3.2, 1.85, 0.13), (1.75, 0.95, 0.22)):
        s.box("", (cx, cy), breite=b, hoehe=h, form="round", farbe=BLAU, fuellung=BLAU, deckung=deck, dicke=2.5)
    s.text(None, s.tr("graben", "Graben: 30 % kommen durch", "moat: 30 % get through", "foso: pasa el 30 %", "护城河：30% 能通过"),
           (cx, cy + 1.13), KLEIN, "center")
    s.text(None, s.tr("mauer", "Mauer: 10 %", "wall: 10 %", "muralla: 10 %", "城墙：10%"), (cx, cy + 0.7), KLEIN, "center")
    s.text(None, s.tr("schatz", "Schatz", "treasure", "tesoro", "宝藏"), (cx, cy + 0.15), MITTEL, "center")
    s.text(None, s.tr("wache", "Wache: 5 %", "guard: 5 %", "guardia: 5 %", "守卫：5%"), (cx, cy - 0.2), KLEIN, "center")
    s.pfeil((-3.3, cy), (cx - 0.9, cy), farbe=ROT, dicke=4, spitze=0.2)
    s.text(None, s.tr("angreifer", "Angreifer", "attacker", "atacante", "攻击者"), (-2.75, cy + 0.22), KLEIN, "center", ROT)
    s.text(None, s.tr("alle", "alle drei überwinden:  0.3 · 0.1 · 0.05 = 0.0015", "get past all three:  0.3 · 0.1 · 0.05 = 0.0015",
                      "superar las tres:  0.3 · 0.1 · 0.05 = 0.0015", "突破全部三道：0.3 · 0.1 · 0.05 = 0.0015"), (cx, cy - 1.75), MITTEL, "center")
    s.speichern()


# ------------------------------------------------------------------ Abschnitt 7
def k1zyklus():
    """Lebenszyklus einer Schwachstelle im ungünstigen Fall: Zero-Day-Phase und Phase bis zum Update."""
    s = Szene("cyber/k1zyklus")
    xs = (-2.9, -1.45, 0.0, 1.45, 2.9)
    yb = 0.55
    for x0, x1, farbe, deck, key, de, en, es, zh, tf in (
            (xs[0], xs[1], GRAU, 0.12, "niemand", "niemand\nweiß davon", "nobody\nknows", "nadie\nlo sabe", "无人知晓", GRAU),
            (xs[1], xs[3], ROT, 0.14, "zero", "Zero-Day:\nausgenutzt, kein Patch", "zero-day:\nexploited, no patch", "día cero:\nexplotada, sin parche",
             "零日：\n已被利用，无补丁", ROT),
            (xs[3], xs[4], ORANGE, 0.18, "nday", "Patch da, nicht\neingespielt", "patch out,\nnot installed", "parche listo,\nno instalado",
             "补丁已发布，\n未安装", ORANGE)):
        s.box("", ((x0 + x1) / 2, yb), breite=x1 - x0, hoehe=0.7, form="rect", farbe=farbe, fuellung=farbe, deckung=deck, dicke=0)
        s.text(None, s.tr(key, de, en, es, zh), ((x0 + x1) / 2, yb), KLEIN, "center", tf)
    s.pfeil((-3.25, 0), (3.45, 0), farbe=SCHWARZ, dicke=3, spitze=0.16)
    s.text(None, s.tr("zeit", "Zeit", "time", "tiempo", "时间"), (3.45, -0.25), KLEIN, "right", GRAU)
    texte = (s.tr("e1", "Fehler entsteht,\nProgramm wird\nausgeliefert", "flaw is made,\nsoftware\nis shipped", "nace el fallo,\nse distribuye\nel programa",
                  "缺陷产生，\n程序发布"),
             s.tr("e2", "Angreifer finden\ndie Lücke und\nnutzen sie aus", "attackers find\nand exploit\nthe flaw", "atacantes\nencuentran y\nexplotan el fallo",
                  "攻击者发现\n并利用漏洞"),
             s.tr("e3", "Hersteller\nerfährt davon", "vendor\nlearns of it", "el fabricante\nse entera", "厂商\n得知漏洞"),
             s.tr("e4", "Patch und\nVeröffentlichung\n(CVE-Kennung)", "patch and\ndisclosure\n(CVE ID)", "parche y\npublicación\n(ID CVE)",
                  "补丁与公开\n（CVE 编号）"),
             s.tr("e5", "Betreiber\nspielt das\nUpdate ein", "operator\ninstalls\nthe update", "el operador\ninstala la\nactualización", "运营者\n安装更新"))
    for x, t in zip(xs, texte):
        s.linie(None, (x, 0.1), (x, -0.1), dicke=3)
        s.text(None, t, (x, -0.65), KLEIN, "center")
    s.speichern()


# ------------------------------------------------------------------ Abschnitt 10
def k1offenlegung():
    """Finder -> Hersteller -> Betreiber/Öffentlichkeit; Koordinator, wenn der Hersteller nicht reagiert."""
    s = Szene("cyber/k1offenlegung")
    y = 0.55
    kasten(s, (-2.55, y), 1.4, 0.6, s.tr("finder", "Finder", "Finder", "Descubridor", "发现者"))
    kasten(s, (0.25, y), 1.6, 0.6, s.tr("hersteller", "Hersteller", "Vendor", "Fabricante", "厂商"))
    kasten(s, (2.85, y), 1.7, 0.8, s.tr("oeff", "Betreiber und\nÖffentlichkeit", "operators and\nthe public", "operadores y\nel público", "运营者与\n公众"), KLEIN)
    kasten(s, (-1.05, -1.3), 2.1, 0.75, s.tr("koord", "Koordinator\n(z. B. BSI, CERT)", "coordinator\n(e.g. BSI, CERT)", "coordinador\n(p. ej. BSI, CERT)",
                                             "协调方\n（如 BSI、CERT）"), KLEIN, dash=DASH)
    s.pfeil((-1.85, y), (-0.55, y), dicke=3, spitze=0.16)
    s.pfeil((1.05, y), (2.0, y), dicke=3, spitze=0.16)
    s.text(None, s.tr("s1", "1. vertrauliche\nMeldung", "1. confidential\nreport", "1. aviso\nconfidencial", "1. 保密\n报告"), (-1.22, y + 0.55), KLEIN, "center")
    s.text(None, s.tr("s3", "3. Patch, danach\nVeröffentlichung", "3. patch, then\ndisclosure", "3. parche, luego\npublicación", "3. 补丁，\n然后公开"),
           (1.52, y + 0.55), KLEIN, "center")
    s.text(None, s.tr("s2", "2. entwickelt einen Patch", "2. develops a patch", "2. desarrolla un parche", "2. 开发补丁"), (0.25, y + 1.2), KLEIN, "center")
    s.pfeil((-2.55, y - 0.3), (-2.1, -1.3), knick="vh", dicke=2.5, spitze=0.15, dash=DASH)
    s.text(None, s.tr("keine", "wenn keine\nReaktion", "if no\nresponse", "si no hay\nrespuesta", "若无\n回应"), (-2.45, -0.45), KLEIN, "left")
    s.pfeil((0.0, -1.3), (0.25, y - 0.3), knick="hv", dicke=2.5, spitze=0.15, dash=DASH)
    s.text(None, s.tr("verm", "vermittelt", "mediates", "media", "居中协调"), (0.35, -0.5), KLEIN, "left")
    s.speichern()


def k1entscheidung():
    """Entscheidungsbaum: Darf ich das testen?"""
    s = Szene("cyber/k1entscheidung")
    xq, xa = -1.2, 2.45
    fragen = ((1.7, 0.8, s.tr("q1", "Gehört das System dir, und sind\nkeine Daten anderer betroffen?",
                              "Is the system yours, and is no one\nelse's data involved?",
                              "¿Es tuyo el sistema y no afecta\na datos de otras personas?", "系统属于你，\n且不涉及他人数据？")),
              (0.35, 1.05, s.tr("q2", "Hast du eine ausdrückliche, schriftliche\nErlaubnis des Verfügungsberechtigten,\nund liegt der Test in ihrem Umfang?",
                                "Do you have explicit written permission\nfrom the person entitled to decide,\nand is the test within its scope?",
                                "¿Tienes permiso expreso y por escrito\nde quien tiene la facultad de decidir,\ny la prueba entra en su alcance?",
                                "你是否有处置权人的\n明确书面许可，\n且测试在许可范围内？")),
              (-1.0, 0.8, s.tr("q3", "Ist es eine Lernplattform, deren\nRegeln genau diesen Test erlauben?",
                               "Is it a training platform whose rules\nallow exactly this test?",
                               "¿Es una plataforma de práctica cuyas\nnormas permiten justo esta prueba?", "这是规则恰好允许\n此项测试的练习平台吗？")))
    antworten = (s.tr("j1", "erlaubt", "allowed", "permitido", "允许"),
                 s.tr("j2", "erlaubt, nur im\nvereinbarten Umfang", "allowed, only within\nthe agreed scope", "permitido, solo dentro\ndel alcance acordado",
                      "允许，仅限\n约定范围"),
                 s.tr("j3", "erlaubt, nur innerhalb\nder Regeln", "allowed, only within\nthe rules", "permitido, solo dentro\nde las normas", "允许，仅限\n规则之内"))
    ja = s.tr("ja", "ja", "yes", "sí", "是")
    nein = s.tr("nein", "nein", "no", "no", "否")
    for (y, h, t), ant in zip(fragen, antworten):
        kasten(s, (xq, y), 3.85, h, t, KLEIN)
        kasten(s, (xa, y), 2.0, 0.62, ant, KLEIN, farbe=GRUEN, textfarbe=GRUEN, fuellung=GRUEN_HELL)
        s.pfeil((xq + 1.925, y), (xa - 1.0, y), dicke=2.5, spitze=0.15)
        s.text(None, ja, ((xq + 1.925 + xa - 1.0) / 2, y + 0.18), KLEIN, "center")
    kasten(s, (xq, -2.0), 1.8, 0.5, s.tr("nicht", "nicht testen", "do not test", "no probar", "不要测试"), MITTEL, farbe=ROT, textfarbe=ROT, fuellung=ROT_HELL)
    for ya, yb in ((1.7 - 0.4, 0.35 + 0.525), (0.35 - 0.525, -1.0 + 0.4), (-1.0 - 0.4, -2.0 + 0.25)):
        s.pfeil((xq, ya), (xq, yb), dicke=2.5, spitze=0.15)
        s.text(None, nein, (xq + 0.1, (ya + yb) / 2), KLEIN, "left")
    s.speichern()


SZENEN = (k1brief, k1kette, k1risiko, k1toctou, k1schichten, k1zyklus, k1offenlegung, k1entscheidung)

for f in SZENEN:
    f()
