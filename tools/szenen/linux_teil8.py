"""Linux und Kommandozeile, Kapitel 8 „Prozesse, Signale und Dienste“ (C:\\Bücher\\EtUndSo\\Linux\\Arbeitshefte\\Kap8_Prozesse.tex,
kap8_stufen.tex, kap8_stufen_b.tex): Abbildungen, alle animiert (notizen/animationen.md §5, §11).

Szenenname linux/k8<name> = \\label{fig:k8<name>} im Heft (\\szenenabb{k8<name>}{…}{fig:k8<name>}); Liste in uebergabe_kap8.md,
Abschnitt „Prüfer (Phase 2a)“. Phase 2b-1 (12.11.2026): Abschnitte 1–4 (16 Szenen) und die Bildschirm-Szene k8topbild
(Unterabschnitt 2.7); Phase 2b-2 ergänzt die Abschnitte 5–8 in dieser Datei.
Stil: F1. Zeilen mit Spalten, Feldern und Klammern (ps aux, ps -ef, jobs -l, /proc/<PID>/status) sind s.raster,
Terminalfenster s.terminal, top s.top (dunkel). Übrige Schemata aus Kästen und Pfeilen mit den Helfern aus linux_hilfen.py.
Inhalte (Zeilen, Nummern, Befehle) wörtlich aus dem Heft; Nummern, die das Heft nicht kennt, stehen als „…“.
Farben: blau = Prozess, orange = hervorgehoben/Signal, grün = erlaubt/läuft, rot = verboten/verloren, grau = bekannt oder
nicht beteiligt. Koordinaten zwischen x = -3,45 und 3,45 (höchstens 548 px).
Bauen:  python tools/szenen/linux_teil8.py [k8name …]
Export: python tools/export_szenen.py --animiert <alle Namen aus SZENEN>
"""
import math
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from szenen_lib import *  # noqa: E402,F403
from szenen_lib import farbig, tt_breite  # noqa: E402,F401

from linux_hilfen import *  # noqa: E402,F403  (gemeinsame Helfer der Linux-Kapitel)

schreibmaschine("text")
TT = 18                           # Schreibmaschinenschrift für Zeilen (9,9 px im Artikel)
TK = 17                           # kleinste Schreibmaschinenschrift (Etiketten, Prozessnamen)
P8 = "student@labor:~/linuxk8$ "    # Prompt im Arbeitsverzeichnis des Kapitels (Abschnitt 1.1: cd ~/linuxk8)
PFAD = "~/linuxk8"


def r4(v):
    return round(v, 4)


def L(s, key, w, pos, g=FM, a="center", f=SCHWARZ):
    """Beschriftung in sechs Sprachen; w = (de, en, es, zh, fr, tr)."""
    return text(s, T(s, key, *w), (r4(pos[0]), r4(pos[1])), g, a, f)


def tx(s, t, pos, g=TT, a="center", f=SCHWARZ):
    """Schreibmaschinenschrift (Code, Ausgabezeilen, Nummern); in allen Sprachen gleich."""
    return s.text(None, t, (r4(pos[0]), r4(pos[1])), g, a, f, schrift="tt")


def box(s, mitte, b, h, rand=GRAU, fuellung=WEISS, dicke=2, form="round", dash="", deckung=1.0):
    return s.box("", (r4(mitte[0]), r4(mitte[1])), breite=r4(b), hoehe=r4(h), form=form, farbe=rand, fuellung=fuellung,
                 deckung=deckung, dicke=dicke, dash=dash)


def chip(s, mitte, t, rand=BLAU, fuellung=BLAU_HELL, g=TK, h=0.3, b=None, dicke=2, textfarbe=SCHWARZ):
    """Kärtchen mit Schreibmaschinenschrift (Prozess, Signal, Job); Ergebnis [Kasten, Text]."""
    b = b if b is not None else len(t) * tt_breite(g, 1) + 0.24
    return [box(s, mitte, b, h, rand, fuellung, dicke), tx(s, t, mitte, g, "center", textfarbe)]


def wchip(s, mitte, key, w, b, rand=BLAU, fuellung=BLAU_HELL, g=FM, h=0.3, dicke=2, textfarbe=SCHWARZ):
    """Kärtchen mit Beschriftung in sechs Sprachen; Ergebnis [Kasten, Text]."""
    return [box(s, mitte, b, h, rand, fuellung, dicke), L(s, key, w, mitte, g, "center", textfarbe)]


def bogen_pf(s, a, b, h, farbe=SCHWARZ, dicke=2.5, dash="", marke="0.55"):
    """Bogen von a nach b, h über der Verbindungslinie (h < 0: darunter), Richtungsmarke bei marke."""
    fx = "%s+%s*t" % (r4(a[0]), r4(b[0] - a[0]))
    fy = "%s+%s*t+%s*4*t*(1-t)" % (r4(a[1]), r4(b[1] - a[1]), r4(h))
    return s.weg(None, fx, fy, 0, 1, farbe=farbe, dicke=dicke, pfeile=marke, n=41, dash=dash, spitze=0.12)


def kreuz(s, x, y, g=0.24, farbe=ROT):
    return s.kreuzchen(None, r4(x), r4(y), farbe, g, 4)


def pause_zeichen(s, x, y, farbe=ORANGE, h=0.2):
    """Pausenzeichen (zwei Balken): angehalten."""
    return [s.box("", (r4(x - 0.045), r4(y)), breite=0.05, hoehe=h, form="rect", farbe=farbe, fuellung=farbe, dicke=0),
            s.box("", (r4(x + 0.045), r4(y)), breite=0.05, hoehe=h, form="rect", farbe=farbe, fuellung=farbe, dicke=0)]


W_SHELL = ("Shell", "shell", "shell", "Shell", "shell", "kabuk")
W_KERNEL = ("Kernel", "kernel", "kernel", "内核", "noyau", "çekirdek")
W_VG = ("Vordergrund", "foreground", "primer plano", "前台", "premier plan", "ön plan")
W_HG = ("Hintergrund", "background", "segundo plano", "后台", "arrière-plan", "arka plan")
W_TASTATUR = ("Tastatur", "keyboard", "teclado", "键盘", "clavier", "klavye")
W_STRGC = ("Strg+C", "Ctrl+C", "Ctrl+C", "Ctrl+C", "Ctrl+C", "Ctrl+C")
W_STRGZ = ("Strg+Z", "Ctrl+Z", "Ctrl+Z", "Ctrl+Z", "Ctrl+Z", "Ctrl+Z")
W_BEENDEN = ("beenden", "terminate", "terminar", "终止", "terminer", "sonlandır")
W_BEENDET = ("beendet", "ended", "terminado", "已结束", "terminé", "sona erdi")
W_WARTET = ("wartet", "waits", "espera", "等待", "attend", "bekler")
W_ANGEH = ("angehalten", "stopped", "detenido", "已暂停", "arrêté", "durduruldu")
W_REAL = ("real", "real", "real", "实际", "réel", "gerçek")
W_EFF = ("effektiv", "effective", "efectivo", "有效", "effectif", "etkin")
W_GESP = ("gespeichert", "saved", "guardado", "保存", "sauvegardé", "kaydedilmiş")


# ================================================================== Abschnitt 1: Prozesse und ihre Verwandtschaft
W_KERN = ("Rechenkern", "CPU core", "núcleo", "CPU 核心", "cœur", "işlemci çekirdeği")
W_STAND = ("Stand", "state", "estado", "状态", "état", "durum")
W_FORT = ("Fortschritt", "progress", "progreso", "进度", "progression", "ilerleme")
W_ZEIT = ("Zeit", "time", "tiempo", "时间", "temps", "zaman")
W_KW = ("Kontextwechsel: ", "context switches: ", "cambios de contexto: ", "上下文切换：", "changements de contexte : ",
        "bağlam değişimi: ")
W_TASTE = ("wartet auf eine Taste", "waits for a key", "espera una tecla", "等待按键", "attend une touche",
           "bir tuşu bekliyor")
W_TASTE_DA = ("Taste da: bereit", "key arrived: ready", "llegó la tecla: listo", "按键已到：就绪", "touche reçue : prêt",
              "tuş geldi: hazır")


def k8zeitteilung():
    """Ein Rechenkern, drei Prozesse A, B, C mit Stand und Fortschrittsbalken. Der Stand des laufenden Prozesses liegt im
    Kern; bei jedem Kontextwechsel wandert er zurück und der nächste hinein (Zähler +1). Die Zeitleiste zeigt, wer rechnet;
    B gibt den Kern beim Warten auf eine Taste früh ab und kommt erst wieder dran, als die Taste da ist."""
    s = Szene("linux/k8zeitteilung", reihenfolge="anlegen")
    farbe = {"A": (BLAU, BLAU_HELL), "B": (GRUEN, GRUEN_HELL), "C": (ORANGE, ORANGE_HELL)}
    ys = {"A": 1.75, "B": 1.2, "C": 0.65}
    xn, xs, xb0, lb = -3.1, -2.35, -1.7, 1.4         # Name, Platz des Stands, Balkenanfang, Balkenlänge
    km, kc = (2.6, 1.2), (2.6, 1.02)                 # Rechenkern, Platz des Stands darin
    yt, X0, K = -0.1, -3.0, 1.2                      # Zeitleiste: x = X0 + K * t

    def xt(t):
        return r4(X0 + K * t)

    stat = [L(s, "fort", W_FORT, (xb0 + lb / 2, 2.15), FM, "center", GRAU),
            box(s, km, 1.4, 1.0, DUNKEL, WEISS, 2.5), L(s, "kern", W_KERN, (km[0], 1.5), FM, "center", DUNKEL),
            pf(s, (X0 - 0.05, yt), (3.35, yt), farbe=GRAU, dicke=2), L(s, "zeit", W_ZEIT, (3.35, yt - 0.27), FM, "right", GRAU)]
    for p, y in ys.items():
        f, fh = farbe[p]
        stat += [box(s, (xn, y), 0.42, 0.36, f, fh, 2.5), text(s, p, (xn, y), FK, "center", SCHWARZ),
                 box(s, (xs, y), 0.82, 0.3, HELLGRAU, WEISS, 1.5, dash=DASH),
                 linie(s, (xb0, y), (xb0 + lb, y), "#dddddd", 12)]
    chips = {}
    for p, y in ys.items():                          # die Stände liegen über ihren Plätzen
        f, fh = farbe[p]
        chips[p] = [box(s, (xs, y), 0.82, 0.3, f, fh, 2), L(s, "stand", W_STAND, (xs, y), FM)]
    s.parameter("n", 0, ganzzahlig=True)
    zaehler = s.zahl(None, "n", (X0 - 0.05, -0.8), stellen=0, vor=T(s, "kw", *W_KW), groesse=FK, ausrichtung="left",
                     farbe=DUNKEL)
    wartet = L(s, "taste", W_TASTE, (xb0 + lb + 0.15, ys["B"]), FM, "left", GRAU)
    schritt(s, EIN(stat + flach(list(chips.values())) + [zaehler], 0.7))
    s.pause(0.4)
    slots = [("A", 0.0, 1.0), ("B", 1.0, 1.4), ("C", 1.4, 2.4), ("A", 2.4, 3.4), ("B", 3.4, 4.4)]
    stand = {"A": 0.0, "B": 0.0, "C": 0.0}
    aktuell, n = None, 0
    for i, (p, t0, t1) in enumerate(slots):
        f = farbe[p][0]
        teile = VERS(chips[p], kc[0] - xs, kc[1] - ys[p], 0.7)                 # Stand laden
        if aktuell:
            teile += VERS(chips[aktuell], xs - kc[0], ys[aktuell] - kc[1], 0.7)  # vorigen Stand sichern
        with s.gleichzeitig():
            schritt(s, *teile)
            if aktuell:
                n += 1
                s.verstellen("n", n, dauer=0.7)
        aktuell = p
        seg = linie(s, (xt(t0), yt), (xt(t1), yt), f, 12)
        lt = text(s, p, (r4((xt(t0) + xt(t1)) / 2), yt - 0.27), FM, "center", f)
        bar = linie(s, (r4(xb0 + 0.6 * stand[p]), ys[p]), (r4(xb0 + 0.6 * (stand[p] + t1 - t0)), ys[p]), f, 12)
        stand[p] += t1 - t0
        d = round(max(0.5, t1 - t0), 2)
        with s.gleichzeitig():
            schritt(s, ZEICHNE([seg, bar], d), EIN(lt, d))
            if i == 3:
                s.ersetzen(wartet, T(s, "tasteda", *W_TASTE_DA), farbe=GRUEN, dauer=d)
        if i == 1:
            schritt(s, EIN(wartet, 0.5))
    s.speichern()


W_NAECHSTE = ("nächste PID", "next PID", "siguiente PID", "下一个 PID", "PID suivant", "sonraki PID")
W_FREI = ("frei", "free", "libre", "空闲", "libre", "boş")
W_NEU = ("neuer Prozess", "new process", "proceso nuevo", "新进程", "nouveau processus", "yeni süreç")
W_UMLAUF = ("Umlauf: wieder ab 300", "wrap-around: again from 300", "vuelta: de nuevo desde 300", "回绕：从 300 重新开始",
            "bouclage : reprise à 300", "başa dönüş: yeniden 300'den")
W_RAFFER = ("Zeitraffer", "fast forward", "avance rápido", "快进", "accéléré", "hızlı ileri")


def k8pidvergabe():
    """Zähler „nächste PID“ (550) und ein Streifen der Nummern. 550, 551, 552 werden vergeben, der Zähler läuft mit; 551
    endet und wird grau (frei, aber übersprungen). Zeitraffer bis 4 194 303, Umlauf auf 300; die Suche überspringt die
    vergebenen 535 (Shell) und 550 und vergibt die freie 551 neu."""
    s = Szene("linux/k8pidvergabe", reihenfolge="anlegen")
    zellen = [("300", -2.75), ("…", -2.2), ("535", -1.62), ("…", -1.07), ("550", -0.5), ("551", 0.1), ("552", 0.7),
              ("553", 1.3), ("…", 1.87), ("4 194 303", 2.78)]
    yz, hz, yp = 0.6, 0.4, 0.1
    X = {n: x for n, x in zellen if n != "…"}
    zellen_ids, nummer = [], {}
    for n, x in zellen:
        b = 0.42 if n == "…" else (0.98 if len(n) > 3 else 0.56)
        zellen_ids.append(box(s, (x, yz), b, hz, GRAU if n == "…" else DUNKEL, WEISS, 1.5, "rect"))
        nummer[n] = tx(s, n, (x, yz), TK, "center", GRAU if n == "…" else SCHWARZ)
        zellen_ids.append(nummer[n])

    def proc(x, f=BLAU, fh=BLAU_HELL):
        return box(s, (x, yp), 0.36, 0.26, f, fh, 2)

    p535 = proc(X["535"])
    l535 = L(s, "shell", W_SHELL, (X["535"], yp - 0.3), FM, "center", GRAU)
    l_n = L(s, "naechste", W_NAECHSTE, (-2.45, 2.05), FM, "center", DUNKEL)
    kz = box(s, (-2.45, 1.6), 1.5, 0.42, ORANGE, ORANGE_HELL, 2.5)
    wert = tx(s, "550", (-2.45, 1.6), 22)
    zeiger = pf(s, (X["550"], 1.22), (X["550"], 0.84), farbe=ORANGE, dicke=3, spitze=0.12)
    schritt(s, EIN(zellen_ids + [p535, l535, l_n, kz, wert, zeiger], 0.7))
    s.pause(0.4)
    pos = X["550"]
    neu = {}

    def weiter(ziel, d, *mehr):
        with s.gleichzeitig():
            schritt(s, VER(zeiger, r4(X[ziel] - pos), 0, d), *mehr)
            s.ersetzen(wert, ziel, dauer=d)
        return X[ziel]

    for alt, naechst in (("550", "551"), ("551", "552"), ("552", "553")):
        neu[alt] = proc(X[alt])
        pos = weiter(naechst, 0.6, WACHS(neu[alt], 0.6))
    s.pause(0.5)
    grau = box(s, (X["551"], yz), 0.56, hz, GRAU, GRAU, 0, "rect", deckung=0.35)
    l_frei = L(s, "frei", W_FREI, (X["551"], yp - 0.3), FM, "center", GRAU)
    schritt(s, AUS(neu["551"], 0.6), EIN([grau, l_frei], 0.6))
    s.pause(0.5)
    l_raffer = L(s, "raffer", W_RAFFER, (1.87, 1.05), FM, "center", GRAU)
    pos = weiter("4 194 303", 1.2, EIN(l_raffer, 0.5))
    s.pause(0.4)
    umlauf = bogen_pf(s, (X["4 194 303"], 0.38), (X["300"], 0.38), -1.3, ORANGE, 2.5, DASH, "0.5")
    l_um = L(s, "umlauf", W_UMLAUF, (0, -1.15), FM, "center", ORANGE)
    pos = weiter("300", 0.9, ZEICHNE(umlauf, 0.9), EIN(l_um, 0.9))
    s.pause(0.5)
    pos = weiter("535", 0.7)                          # vergeben (Shell): übersprungen
    schritt(s, BETONE([p535, nummer["535"]], 0.6))
    pos = weiter("550", 0.6)                          # vergeben: übersprungen
    schritt(s, BETONE([neu["550"], nummer["550"]], 0.6))
    pos = weiter("551", 0.6)                          # frei: wird vergeben
    p_neu = proc(X["551"], GRUEN, GRUEN_HELL)
    with s.gleichzeitig():
        schritt(s, AUS(grau, 0.6), WACHS(p_neu, 0.6))
        s.ersetzen(l_frei, T(s, "neu", *W_NEU), farbe=GRUEN, dauer=0.6)
    pos = weiter("552", 0.6)
    s.speichern()


W_UMLEIT = ("Umleitung", "redirection", "redirección", "重定向", "redirection", "yönlendirme")
W_WAIT = ("wartet (wait)", "waits (wait)", "espera (wait)", "等待（wait）", "attend (wait)", "bekler (wait)")
W_KIND = ("Kindprozess", "child process", "proceso hijo", "子进程", "processus enfant", "alt süreç")
W_EXIT0 = ("Exit-Status 0", "exit status 0", "estado de salida 0", "退出状态 0", "code de sortie 0", "çıkış durumu 0")
W_PROMPT = ("nächste Eingabeaufforderung", "next prompt", "siguiente prompt", "下一个提示符", "invite suivante",
            "sonraki istem")


def k8forkexec():
    """Zwei Spuren: oben die Shell 535 (bash), unten nach fork die Kopie 558 (bash, PPID 535). Umleitung: liste.txt auf
    Deskriptor 1. exec: Programmschild bash -> ls, PID 558 bleibt (Rahmen). Die Shell wartet (wait); der Exit-Status 0
    wandert zu ihr, dann kommt die nächste Eingabeaufforderung."""
    s = Szene("linux/k8forkexec", reihenfolge="anlegen")
    yS, yK, xb = 1.35, 0.0, -2.8
    xf, xu, xe, xende = -1.45, -0.45, 0.6, 2.0
    l_shell = L(s, "shell", W_SHELL, (xb, 1.78), FM, "center", GRAU)
    spur_s = linie(s, (-2.25, yS), (2.7, yS), GRAU, 2.5)
    wait_seg = linie(s, (xf + 0.2, yS), (xende + 0.1, yS), ORANGE, 6, DASH)
    l_wait = L(s, "wait", W_WAIT, ((xf + xende) / 2 + 0.2, yS + 0.22), FM, "center", ORANGE)
    shell = chip(s, (xb, yS), "bash", b=0.9, h=0.38)
    pid_s = chip(s, (xb, 0.93), "PID 535", GRAU, GELB, h=0.28, dicke=1.5)
    kind = chip(s, (xb, yS), "bash", b=0.9, h=0.38)            # Kopie: spaltet sich ab und wandert nach unten
    l_kind = L(s, "kind", W_KIND, (xb, 0.4), FM, "center", GRAU)
    pid_k = [box(s, (xb, -0.52), 0.95, 0.48, GRAU, GELB, 1.5, "rect"), tx(s, "PID 558", (xb, -0.41), TK),
             tx(s, "PPID 535", (xb, -0.63), TK)]
    rahmen_pid = rahmen(s, (xb, -0.52), 1.07, 0.6, ORANGE, 3)
    fork_pf = pf(s, (xf, yS - 0.04), (xf, yK + 0.06), farbe=BLAU)
    l_fork = tx(s, "fork", (xf + 0.13, 0.68), TK, "left", BLAU)
    k1 = linie(s, (xf, yK), (xe, yK), BLAU, 3)
    k2 = linie(s, (xe, yK), (xende, yK), GRUEN, 3)
    tick_u = linie(s, (xu, yK - 0.09), (xu, yK + 0.09), DUNKEL, 2.5)
    umleit = chip(s, (xu, 0.33), "1 → liste.txt", ORANGE, ORANGE_HELL, h=0.28, dicke=1.5)
    l_umleit = L(s, "umleit", W_UMLEIT, (xu, 0.63), FM, "center", ORANGE)
    tick_e = linie(s, (xe, yK - 0.09), (xe, yK + 0.09), DUNKEL, 2.5)
    l_exec = tx(s, "exec", (xe + 0.1, 0.3), TK, "left", GRUEN)
    ende_k = linie(s, (xende, yK - 0.12), (xende, yK + 0.12), DUNKEL, 3)
    exitc = wchip(s, (xende, -0.38), "exit0", W_EXIT0, 1.55, GRAU, GELB, h=0.3, dicke=1.5)
    prompt = tx(s, "$", (2.95, yS), 22, "center")
    l_prompt = L(s, "prompt", W_PROMPT, (3.4, 1.72), FM, "right", DUNKEL)
    schritt(s, EIN(shell + kind + pid_s + [l_shell, spur_s], 0.7))
    s.pause(0.5)
    schritt(s, ZEICHNE(fork_pf, 0.8), EIN(l_fork, 0.8), *VERS(kind, 0, yK - yS, 0.8))
    schritt(s, EIN(pid_k + [l_kind, l_wait], 0.6), ZEICHNE([k1, wait_seg], 0.6))
    s.pause(0.5)
    schritt(s, ZEICHNE(tick_u, 0.4), EIN(umleit + [l_umleit], 0.6))
    s.pause(0.4)
    ls_vorlage = tx(s, "ls", (xb, yK), TK)                     # Vorlage am Ziel (ersetzen nähme die alte Lage)
    with s.gleichzeitig():
        schritt(s, ZEICHNE(tick_e, 0.4), EIN([l_exec, rahmen_pid], 0.8), BETONE(pid_k[1], 0.8))
        s.umformen(kind[1], ls_vorlage, dauer=0.8)
    schritt(s, ZEICHNE(k2, 0.9))
    schritt(s, ZEICHNE(ende_k, 0.3), EIN(exitc, 0.5))
    schritt(s, *VERS(exitc, 0.4, 0.92 + 0.38, 0.9))
    schritt(s, EIN([prompt, l_prompt], 0.6))
    s.speichern()


W_PPID_KANTE = ("Zahl an der Kante: PPID", "number on an edge: PPID", "número en la arista: PPID", "边上的数字：PPID",
                "nombre sur l'arête : PPID", "kenardaki sayı: PPID")


def k8baum():
    """Prozessbaum von oben: systemd(1), graue Sammelknoten (cron, rsyslogd, systemd-journal, …), der Zweig von WSL
    (init-systemd, SessionLeader, Relay), darunter bash(535) und die Kette bash(560) -> bash(561) -> pstree(562). Kanten
    tragen die PPID (… = im Heft nicht gezeigt); zum Schluss leuchtet der Weg von pstree(562) bis zur Wurzel."""
    s = Szene("linux/k8baum", reihenfolge="anlegen")

    def knoten(x, y, name, grau=False):
        b = len(name) * tt_breite(TK, 1) + 0.22
        f, fh = (GRAU, GRAU_HELL) if grau else (BLAU, BLAU_HELL)
        return [box(s, (x, y), b, 0.3, f, fh, 2), tx(s, name, (x, y), TK, "center", DUNKEL if grau else SCHWARZ)]

    xr, yr, yg, xw = -1.0, 2.15, 1.45, 1.4
    wsl_box = box(s, (xw, 0.95), 2.0, 1.45, HELLGRAU, WEISS, 1.5, dash=DASH, deckung=0.0)
    l_wsl = text(s, "WSL", (2.5, 0.95), FM, "left", GRAU)
    wurzel = knoten(xr, yr, "systemd(1)")
    grau = []
    for name, x in (("cron", -3.1), ("rsyslogd", -2.32), ("systemd-journal", -1.12), ("…", -0.1)):
        a, b = (xr, yr - 0.15), (x, yg + 0.15)
        grau += [linie(s, a, b, HELLGRAU, 2)] + knoten(x, yg, name, True)
        grau.append(text(s, "1", (r4((a[0] + b[0]) / 2 + 0.1), r4((a[1] + b[1]) / 2 + 0.04)), FM, "center", GRAU))
    kette = [("init-systemd(Ub(2)", 1.45, "1"), ("SessionLeader", 0.95, "2"), ("Relay", 0.45, "…"), ("bash(535)", -0.05, "…"),
             ("bash(560)", -0.55, "535"), ("bash(561)", -1.05, "560"), ("pstree(562)", -1.55, "561")]
    stufen, wege = [], []
    oben = (xr, yr - 0.15)
    for name, y, ppid in kette:
        a, b = oben, (xw, y + 0.15)
        k = linie(s, a, b, GRAU, 2)
        if a[0] == b[0]:
            lp = text(s, ppid, (xw + 0.1, r4((a[1] + b[1]) / 2)), FM, "left", DUNKEL)
        else:
            lp = text(s, ppid, (r4((a[0] + b[0]) / 2 + 0.05), r4((a[1] + b[1]) / 2 + 0.12)), FM, "center", DUNKEL)
        stufen.append([k, lp] + knoten(xw, y, name))
        wege.append(linie(s, b, a, ORANGE, 4))
        oben = (xw, y - 0.15)
    l_shell = L(s, "shell", W_SHELL, (xw - 0.6, -0.05), FM, "right", GRAU)
    l_ppid = L(s, "ppid", W_PPID_KANTE, (-3.4, -1.55), FM, "left", GRAU)
    rahmen_w = rahmen(s, (xr, yr), 1.1, 0.42, ORANGE, 3)
    schritt(s, WACHS(wurzel[0], 0.5), EIN(wurzel[1], 0.5))
    schritt(s, EIN(grau + [l_ppid], 0.7))
    schritt(s, EIN(flach(stufen[:3]) + [wsl_box, l_wsl], 0.8))
    schritt(s, EIN(stufen[3] + [l_shell], 0.6))
    s.pause(0.5)
    for st in stufen[4:]:
        schritt(s, EIN(st, 0.45))
    s.pause(0.5)
    schritt(s, ZEICHNE(list(reversed(wege)), 1.2), EIN(rahmen_w, 1.2))
    s.speichern()


# ================================================================== Abschnitt 2: Prozesse beobachten
AUX_K = "USER         PID %CPU %MEM    VSZ   RSS TTY      STAT START   TIME COMMAND"
AUX_1 = "root           1  5.1  0.0  24332 14060 ?        Ss   15:24   0:01 /sbin/init"
EF_K = "UID          PID    PPID  C STIME TTY          TIME CMD"
EF_1 = "root           1       0  5 15:24 ?        00:00:01 /sbin/init"
W_PS = [("Besitzer", "owner", "propietario", "所有者", "propriétaire", "sahip"),
        ("PID", "PID", "PID", "PID", "PID", "PID"),
        ("Anteil der Rechenzeit seit dem Start", "share of CPU time since the start", "parte del tiempo de CPU desde el inicio",
         "自启动以来的 CPU 时间占比", "part du temps CPU depuis le démarrage", "başlangıçtan beri CPU süresi payı"),
        ("Anteil am Arbeitsspeicher", "share of main memory", "parte de la memoria principal", "内存占比",
         "part de la mémoire vive", "ana bellek payı"),
        ("angeforderter Speicher (KiB)", "requested memory (KiB)", "memoria solicitada (KiB)", "申请的内存（KiB）",
         "mémoire demandée (Kio)", "istenen bellek (KiB)"),
        ("belegter Speicher (KiB)", "memory in use (KiB)", "memoria ocupada (KiB)", "实际占用的内存（KiB）",
         "mémoire occupée (Kio)", "kullanılan bellek (KiB)"),
        ("kein Terminal", "no terminal", "sin terminal", "无终端", "pas de terminal", "terminal yok"),
        ("Zustand", "state", "estado", "状态", "état", "durum"),
        ("Startzeit", "start time", "hora de inicio", "启动时间", "heure de démarrage", "başlama zamanı"),
        ("verbrauchte Rechenzeit", "CPU time used", "tiempo de CPU consumido", "已用 CPU 时间", "temps CPU consommé",
         "kullanılan CPU süresi"),
        ("Befehlszeile", "command line", "línea de órdenes", "命令行", "ligne de commande", "komut satırı")]
W_PPID_NUR = ("nur bei ps -ef: PPID", "only in ps -ef: PPID", "solo en ps -ef: PPID", "仅 ps -ef 有：PPID",
              "seulement dans ps -ef : PPID", "yalnızca ps -ef'te: PPID")


def k8psspalten():
    """Kopf und erste Zeile von ps aux in elf Spalten zerlegt (Klammern mit Nummern, Bedeutungen als Liste); dann ps -ef
    darunter, Pfeile zu den Spalten, die es ebenfalls hat; PPID steht nur dort (orange)."""
    s = Szene("linux/k8psspalten", reihenfolge="anlegen")
    x0 = -3.4
    g = s.raster([AUX_K, AUX_1], (x0, 2.0), groesse=TT)
    e = s.raster([EF_K, EF_1], (x0, 0.62), groesse=TT)
    l_g = tx(s, "ps aux", (x0, 2.28), TK, "left", GRAU)
    l_e = tx(s, "ps -ef", (-2.76, 0.93), TK, "center", GRAU)   # zwischen den Pfeilen 1 und 2

    def spalten(r):
        return [(min(a.a, b.a), max(a.b, b.b)) for a, b in zip(r.felder(0), r.felder(1))]

    sg, se = spalten(g), spalten(e)
    kl, leg = [], []
    for i, (a, b) in enumerate(sg):
        kl.append(g.klammer(1, a, b, str(i + 1), seite="unten", farbe=BLAU, groesse=FM))
        xl, yl = (-3.4, 0.12 - 0.26 * i) if i < 6 else (0.15, 0.12 - 0.26 * (i - 6))
        leg.append([text(s, str(i + 1), (r4(xl + 0.18), r4(yl)), FM, "right", BLAU),
                    L(s, "ps%d" % i, W_PS[i], (xl + 0.27, yl), FM, "left")])
    paare = [(0, 0), (1, 1), (8, 4), (6, 5), (9, 6), (10, 7)]
    y_von = r4(g.unten(1) - 0.36)
    pfeile = [pf(s, (g.xm(*sg[a]), y_von), (e.xm(*se[b]), r4(e.oben(0) + 0.03)), farbe=BLAU, dicke=2, spitze=0.08)
              for a, b in paare]
    m_ppid = e.markieren(0, se[2][0], se[2][1], ORANGE, 0.35, bis=1)
    l_ppid = L(s, "ppid", W_PPID_NUR, (e.xr(len(EF_1) - 1) + 0.2, e.y(0)), FM, "left", ORANGE)
    schritt(s, EIN(g.ids + [l_g], 0.6))
    s.pause(0.4)
    for (k, t), (nr, bed) in zip(kl, leg):
        schritt(s, ZEICHNE(k, 0.35), EIN([t, nr, bed], 0.35))
    s.pause(0.6)
    schritt(s, EIN(e.ids + [l_e], 0.6))
    schritt(s, ZEICHNE(pfeile, 0.9))
    schritt(s, EIN([m_ppid, l_ppid], 0.6))
    s.speichern()


W_ZUST = {"R1": ("rechnet", "running", "ejecutando", "正在运行", "calcule", "çalışıyor"),
          "R2": ("wartet auf einen Kern", "waits for a core", "espera un núcleo", "等待 CPU 核心", "attend un cœur",
                 "çekirdek bekliyor"),
          "R": ("beides ist R", "both are R", "ambos son R", "两者都是 R", "les deux sont R", "ikisi de R"),
          "S": ("wartet", "sleeping", "espera", "等待", "attend", "bekliyor"),
          "T": ("angehalten", "stopped", "detenido", "已暂停", "arrêté", "durduruldu"),
          "D": ("wartet auf ein Gerät", "waits for a device", "espera un dispositivo", "等待设备", "attend un périphérique",
                "aygıt bekliyor"),
          "Z1": ("beendet,", "ended,", "terminado,", "已结束，", "terminé,", "sona erdi,"),
          "Z2": ("Status nicht abgeholt", "status not collected", "estado no recogido", "状态未取走", "statut non récupéré",
                 "durum alınmadı"),
          "RS": ("wartet auf eine Taste", "waits for a key", "espera una tecla", "等待按键", "attend une touche",
                 "bir tuş bekler"),
          "SR": ("Taste kommt", "key arrives", "llega la tecla", "按键到达", "la touche arrive", "tuş gelir"),
          "RD": ("liest vom Datenträger", "reads from a disk", "lee del disco", "读取磁盘", "lit sur le disque",
                 "diskten okur"),
          "RT": ("wird angehalten", "is stopped", "se detiene", "被暂停", "est arrêté", "durdurulur"),
          "TR": ("weiter", "continues", "continúa", "继续", "continue", "devam eder"),
          "RZ": ("Programm endet", "program ends", "el programa termina", "程序结束", "le programme se termine", "program biter"),
          "ZX": ("Elternprozess holt den Status ab", "parent collects the status", "el padre recoge el estado", "父进程取走状态",
                 "le parent récupère le statut", "üst süreç durumu alır"),
          "P": ("Prozess", "process", "proceso", "进程", "processus", "süreç")}


def k8zustaende():
    """Fünf Kreise R, S, D, T, Z. Ein Punkt „Prozess“ entsteht in R, pendelt dort zwischen „rechnet“ und „wartet auf einen
    Kern“ (beides R) und wandert mit beschrifteten Übergängen: R <-> S, R <-> D, R <-> T, R -> Z und aus Z ins Leere."""
    s = Szene("linux/k8zustaende", reihenfolge="anlegen")
    pos = {"R": (0.0, 0.45), "S": (-2.45, 0.45), "T": (2.45, 0.45), "D": (-1.25, -1.0), "Z": (1.25, -1.0)}
    farbe = {"R": (GRUEN, GRUEN_HELL), "S": (BLAU, BLAU_HELL), "D": (BLAU, BLAU_HELL), "T": (ORANGE, ORANGE_HELL),
             "Z": (GRAU, GRAU_HELL)}
    rad = {"R": 0.45}
    kreise = []
    for k, (x, y) in pos.items():
        f, fh = farbe[k]
        kreise += [s.kreis(None, x, y, rad.get(k, 0.36), farbe=f, dicke=3, fuellung=fh, deckung=1.0),
                   tx(s, k, (x, y + (0.18 if k == "R" else 0.0)), 28)]
    w = W_ZUST
    lab = {"R1": L(s, "zr1", w["R1"], (-0.1, 1.1), FM, "right", GRUEN),
           "R2": L(s, "zr2", w["R2"], (0.1, 1.1), FM, "left", GRUEN),
           "S": L(s, "zs", w["S"], (-2.45, 0.98), FM, "center", BLAU),
           "T": L(s, "zt", w["T"], (2.45, 0.98), FM, "center", ORANGE),
           "D": L(s, "zd", w["D"], (-1.7, -1.0), FM, "right", BLAU),
           "Z1": L(s, "zz1", w["Z1"], (1.7, -0.88), FM, "left", GRAU),
           "Z2": L(s, "zz2", w["Z2"], (1.7, -1.12), FM, "left", GRAU)}
    l_beides = L(s, "zbeides", w["R"], (0, 1.38), FM, "center", GRAU)
    trenn = text(s, "|", (0, 1.1), FM, "center", GRAU)
    punkt = s.punkt(None, -0.17, 0.3, ORANGE, 0.09)
    l_p = L(s, "zp", w["P"], (0, 0.12), FM, "center", DUNKEL)

    def pfeil(a, b, key, lpos, ausr="center"):
        return [pf(s, a, b, farbe=DUNKEL, dicke=2.5, spitze=0.1), L(s, "z" + key.lower(), w[key], lpos, FM, ausr, DUNKEL)]

    rs = pfeil((-0.47, 0.57), (-2.07, 0.57), "RS", (-1.27, 0.73))
    sr = pfeil((-2.07, 0.33), (-0.47, 0.33), "SR", (-1.27, 0.17))
    rt = pfeil((0.47, 0.57), (2.07, 0.57), "RT", (1.27, 0.73))
    tr_ = pfeil((2.07, 0.33), (0.47, 0.33), "TR", (1.27, 0.17))
    n = (0.0606, -0.0522)                             # senkrecht zu R-D, 0,08 lang
    rd = [pf(s, (-0.294 + n[0], 0.109 + n[1]), (-1.015 + n[0], -0.727 + n[1]), farbe=DUNKEL, dicke=2.5, spitze=0.1),
          L(s, "zrd", w["RD"], (-0.84, -0.17), FM, "right", DUNKEL)]
    dr = [pf(s, (-1.015 - n[0], -0.727 - n[1]), (-0.294 - n[0], 0.109 - n[1]), farbe=DUNKEL, dicke=2.5, spitze=0.1)]
    rz = pfeil((0.294, 0.109), (1.015, -0.727), "RZ", (0.84, -0.15), "left")
    zx = pfeil((1.25, -1.36), (1.25, -1.85), "ZX", (1.1, -1.62), "right")
    schritt(s, EIN(kreise + list(lab.values()) + [trenn], 0.7))
    schritt(s, WACHS(punkt, 0.5), EIN(l_p, 0.5))
    schritt(s, ZU(punkt, 0.17, 0.3, 0.5), BETONE(lab["R2"], 0.5))
    schritt(s, ZU(punkt, -0.17, 0.3, 0.5), BETONE(lab["R1"], 0.5), EIN(l_beides, 0.5))
    s.pause(0.5)

    def gang(teile, ziel, d=0.8, extra=()):
        schritt(s, ZEICHNE(teile[0], d), EIN(teile[1:], d), ZU(punkt, ziel[0], ziel[1], d), *extra)

    gang(rs, pos["S"], extra=(AUS(l_p, 0.5),))
    gang(sr, (0.0, 0.3))
    gang(rd, pos["D"], 0.7)
    gang(dr, (0.0, 0.3), 0.7)
    gang(rt, pos["T"])
    gang(tr_, (0.0, 0.3))
    gang(rz, pos["Z"])
    s.pause(0.4)
    schritt(s, ZEICHNE(zx[0], 0.8), EIN(zx[1], 0.8), ZU(punkt, 1.25, -1.9, 0.8))
    schritt(s, AUS(punkt, 0.4))
    s.speichern()


W_GEW = ("gewöhnlich", "the usual case", "el caso habitual", "通常情况", "le cas habituel", "olağan durum")
W_ELTERN = ("Elternprozess", "parent process", "proceso padre", "父进程", "processus parent", "üst süreç")
W_KIND2 = ("Kind", "child", "hijo", "子进程", "enfant", "alt süreç")
W_ENDET = ("endet", "ends", "termina", "结束", "se termine", "sona erer")
W_NIEWAIT = ("ruft nie wait auf", "never calls wait", "nunca llama a wait", "从不调用 wait", "n'appelle jamais wait",
             "wait'i hiç çağırmaz")
W_AUFR = ("Prozess 1 oder Aufräumer", "process 1 or a subreaper", "proceso 1 o un recolector", "进程 1 或收养进程",
          "processus 1 ou récupérateur", "süreç 1 veya toplayıcı")
W_ZOMBIE = ("Zombie (Z)", "zombie (Z)", "zombi (Z)", "僵尸（Z）", "zombie (Z)", "zombi (Z)")
W_STATUS0 = ("Status 0", "status 0", "estado 0", "状态 0", "statut 0", "durum 0")


def k8zombie():
    """Zwei Zeitleisten. Oben gewöhnlich: Kind endet, Grabstein 629/Status 0, der Elternprozess ruft wait auf, der
    Grabstein verschwindet. Unten der Versuch: 628 ruft nie wait auf, der Grabstein bleibt; 628 endet, der Grabstein wandert
    zu „Prozess 1 oder Aufräumer“, wait, weg. Ein grauer Streifen zeigt, wie lange das Kind Zombie war."""
    s = Szene("linux/k8zombie", reihenfolge="anlegen")
    BAND = "#d9d9d9"

    def grabstein(x, y, key):
        return [box(s, (x, y), 0.8, 0.48, GRAU, GRAU_HELL, 2), tx(s, "629", (x, y + 0.1), TK),
                L(s, key, W_STATUS0, (x, y - 0.11), FM, "center", DUNKEL)]

    # oben: gewöhnlich
    yE, yK, xa = 1.8, 1.3, -2.0
    t_o = L(s, "gew", W_GEW, (-3.4, 2.2), FM, "left", DUNKEL)
    lo = [L(s, "eltern", W_ELTERN, (-3.4, yE), FM, "left"), L(s, "kind", W_KIND2, (-3.4, yK), FM, "left")]
    e_o = linie(s, (xa, yE), (3.3, yE), BLAU, 3)
    f_o = pf(s, (-1.6, yE - 0.04), (-1.6, yK + 0.05), farbe=BLAU, dicke=2, spitze=0.08)
    k_o = linie(s, (-1.6, yK), (-0.2, yK), BLAU, 3)
    end_o = linie(s, (-0.2, yK - 0.1), (-0.2, yK + 0.1), DUNKEL, 3)
    band_o = linie(s, (-0.2, yK), (0.85, yK), BAND, 10)
    g_o = grabstein(0.33, yK, "st_o")
    w_o = pf(s, (0.85, yK + 0.06), (0.85, yE - 0.04), farbe=GRUEN, dicke=2.5, spitze=0.09)
    lw_o = tx(s, "wait", (0.97, (yK + yE) / 2), TK, "left", GRUEN)
    lz_o = L(s, "zomb_o", W_ZOMBIE, (0.33, yK - 0.2), FM, "center", GRAU)
    # unten: der Versuch
    yE2, yK2 = 0.3, -0.2
    t_u = tx(s, "$ bash -c 'sleep 1 & exec sleep 30'", (-3.4, 0.75), TK, "left", DUNKEL)
    lu = [tx(s, "628 sleep 30", (-3.4, yE2), TK, "left"), tx(s, "629 sleep 1", (-3.4, yK2), TK, "left")]
    e_u1 = linie(s, (xa, yE2), (-0.9, yE2), BLAU, 3)
    e_u2 = linie(s, (-0.9, yE2), (1.4, yE2), BLAU, 3)
    f_u = pf(s, (-1.6, yE2 - 0.04), (-1.6, yK2 + 0.05), farbe=BLAU, dicke=2, spitze=0.08)
    k_u = linie(s, (-1.6, yK2), (-0.9, yK2), BLAU, 3)
    end_k = linie(s, (-0.9, yK2 - 0.1), (-0.9, yK2 + 0.1), DUNKEL, 3)
    band_u1 = linie(s, (-0.9, yK2), (1.4, yK2), BAND, 10)
    band_u2 = linie(s, (1.4, yK2), (2.45, yK2), BAND, 10)
    l_nie = L(s, "niewait", W_NIEWAIT, (0.25, yE2 + 0.18), FM, "center", GRAU)
    end_e = linie(s, (1.4, yE2 - 0.1), (1.4, yE2 + 0.1), DUNKEL, 3)
    l_end = L(s, "endet", W_ENDET, (1.52, yE2), FM, "left", DUNKEL)
    neu = wchip(s, (2.45, -1.05), "aufr", W_AUFR, 2.0, GRUEN, GRUEN_HELL, h=0.4)
    g_u = grabstein(-0.45, yK2, "st_u")
    w_u = pf(s, (2.45, -0.84), (2.45, yK2 - 0.27), farbe=GRUEN, dicke=2.5, spitze=0.09)
    lw_u = tx(s, "wait", (2.57, -0.62), TK, "left", GRUEN)
    lz_u = L(s, "zomb_u", W_ZOMBIE, (0.75, yK2 - 0.2), FM, "center", GRAU)
    schritt(s, EIN([t_o] + lo, 0.6), ZEICHNE(e_o, 0.8))
    schritt(s, ZEICHNE([f_o, k_o], 0.7))
    schritt(s, ZEICHNE(end_o, 0.3), EIN(g_o, 0.5))
    schritt(s, ZEICHNE(band_o, 0.6))
    schritt(s, ZEICHNE(w_o, 0.6), EIN(lw_o, 0.6))
    schritt(s, AUS(g_o, 0.6), EIN(lz_o, 0.6))
    s.pause(0.6)
    schritt(s, EIN([t_u] + lu, 0.6), ZEICHNE(e_u1, 0.8))
    schritt(s, ZEICHNE([f_u, k_u], 0.6))
    schritt(s, ZEICHNE(end_k, 0.3), EIN(g_u, 0.5))
    schritt(s, ZEICHNE([e_u2, band_u1], 1.2), EIN(l_nie, 0.8))
    schritt(s, ZEICHNE(end_e, 0.3), EIN(l_end, 0.5))
    schritt(s, WACHS(neu[0], 0.5), EIN(neu[1], 0.5))
    schritt(s, ZEICHNE(band_u2, 1.0), *VERS(g_u, 2.9, 0, 1.0))
    schritt(s, ZEICHNE(w_u, 0.6), EIN(lw_u, 0.6))
    schritt(s, AUS(g_u, 0.6), EIN(lz_u, 0.6))
    s.speichern()


W_KOPIE = ("Kopie vom Start, für den Rückweg", "copy from the start, for the way back", "copia del inicio, para volver",
           "启动时的副本，用于切换回来", "copie du démarrage, pour le retour", "başlangıçtaki kopya, geri dönüş için")
W_FS1 = ("folgt der effektiven Nummer:", "follows the effective ID:", "sigue al número efectivo:", "跟随有效用户号：",
         "suit le numéro effectif :", "etkin numarayı izler:")
W_FS2 = ("mit ihr prüft der Kernel Dateizugriffe", "the kernel checks file access with it",
         "con él el kernel comprueba los accesos a archivos", "内核用它检查文件访问",
         "le noyau contrôle avec lui les accès aux fichiers", "çekirdek dosya erişimini onunla denetler")
W_DATEISYS = ("Dateisystem", "file system", "sistema de archivos", "文件系统", "système de fichiers", "dosya sistemi")


def k8procstatus():
    """Zwei Zeilen Uid: (bash 1000 1000 1000 1000, sudo 1000 0 0 0). Über den Spalten real, effektiv (grau, bekannt),
    gespeichert, Dateisystem. Eine Kopie der effektiven 0 wandert in „gespeichert“; „Dateisystem“ folgt der effektiven."""
    s = Szene("linux/k8procstatus", reihenfolge="anlegen")
    x0, y1, y2, G = -2.45, 1.05, 0.2, 26
    g = s.raster(["Uid:    1000    1000    1000    1000"], (x0, y1), groesse=G)
    h = s.raster(["Uid:    1000    0"], (x0, y2), groesse=G)
    namen = [tx(s, "bash", (-3.4, y1), TK, "left", GRAU), tx(s, "sudo", (-3.4, y2), TK, "left", GRAU)]
    kopf = [g.klammer(0, 8, 11, T(s, "real", *W_REAL), farbe=GRAU, groesse=FM, abstand=0.32),
            g.klammer(0, 16, 19, T(s, "eff", *W_EFF), farbe=GRAU, groesse=FM, abstand=0.05),
            g.klammer(0, 24, 27, T(s, "gesp", *W_GESP), farbe=BLAU, groesse=FM, abstand=0.32),
            g.klammer(0, 32, 35, T(s, "dsys", *W_DATEISYS), farbe=ORANGE, groesse=FM, abstand=0.05)]
    kopie = h.teil(0, 16, 16, farbe=BLAU)
    fs0 = h.teil(0, 32, 32, text="0")
    b1 = bogen_pf(s, (h.xm(16), h.oben(0) + 0.02), (h.xm(24), h.oben(0) + 0.02), 0.18, BLAU, 2.5)
    l1 = L(s, "kopie", W_KOPIE, (h.xm(20), h.oben(0) + 0.42), FM, "center", BLAU)
    b2 = bogen_pf(s, (h.xm(16), h.unten(0) - 0.02), (h.xm(32), h.unten(0) - 0.02), -0.22, ORANGE, 2.5)
    l2 = [L(s, "fs1", W_FS1, (h.xm(24), h.unten(0) - 0.42), FM, "center", ORANGE),
          L(s, "fs2", W_FS2, (h.xm(24), h.unten(0) - 0.66), FM, "center", DUNKEL)]
    schritt(s, EIN(g.ids + h.ids + namen, 0.7))
    s.pause(0.4)
    for k, t in kopf:
        schritt(s, ZEICHNE(k, 0.45), EIN(t, 0.45))
    s.pause(0.6)
    schritt(s, EIN(kopie, 0.3))
    schritt(s, ZU(kopie, h.x(24), h.y(0), 0.9), ZEICHNE(b1, 0.9))
    schritt(s, EIN(l1, 0.6))
    s.pause(0.6)
    schritt(s, ZEICHNE(b2, 0.8), EIN(fs0, 0.8))
    schritt(s, EIN(l2, 0.6), BETONE(fs0, 0.8))
    s.speichern()


# ================================================================== Abschnitt 3: Vordergrund, Hintergrund und Jobs
W_PROMPT_JETZT = ("Eingabeaufforderung erst jetzt", "prompt only now", "prompt solo ahora", "此时才出现提示符",
                  "invite seulement maintenant", "istem ancak şimdi")
W_LAEUFT_WEITER = ("läuft weiter", "keeps running", "sigue en marcha", "继续运行", "continue de tourner",
                   "çalışmaya devam eder")


def k8vordergrund():
    """Zwei Zeitleisten (Shell, sleep) unter einer Uhr. Oben sleep 3: fork, die Shell wartet, ihr Prompt ist grau, die
    Tastatur zeigt auf sleep; nach 3 s kommt die Eingabeaufforderung. Unten sleep 300 &: die Shell nimmt sofort Befehle
    an (echo $!, ps …), die Tastatur zeigt auf die Shell, sleep läuft weiter."""
    s = Szene("linux/k8vordergrund", reihenfolge="anlegen")
    X0, K = -1.45, 1.15

    def xt(t):
        return r4(X0 + K * t)

    yS1, yP1, yS2, yP2, ya = 1.85, 1.25, 0.3, -0.3, -0.75
    stat = [tx(s, "$ sleep 3", (-3.4, 2.25), TT, "left"), tx(s, "$ sleep 300 &", (-3.4, 0.7), TT, "left")]
    for y, art in ((yS1, "s"), (yP1, "p"), (yS2, "s"), (yP2, "p")):
        stat.append(L(s, "shell", W_SHELL, (-3.4, y), FM, "left") if art == "s" else tx(s, "sleep", (-3.4, y), TK, "left"))
    stat += tastatur(s, -2.1, (yS1 + yP1) / 2) + tastatur(s, -2.1, (yS2 + yP2) / 2)
    pk1 = pf(s, (-1.64, (yS1 + yP1) / 2), (-1.36, yP1 + 0.05), farbe=ORANGE, dicke=2.5, spitze=0.09)
    pk2 = pf(s, (-1.64, (yS2 + yP2) / 2), (-1.36, yS2 - 0.05), farbe=ORANGE, dicke=2.5, spitze=0.09)
    stat.append(pf(s, (X0 - 0.05, ya), (3.35, ya), farbe=GRAU, dicke=2))
    for t in range(5):
        stat += [linie(s, (xt(t), ya - 0.05), (xt(t), ya + 0.05), GRAU, 2),
                 text(s, "%d s" % t, (xt(t), ya - 0.22), FM, "center", GRAU)]
    s.parameter("uhr", 0)
    marke = s.linie(None, ("%s+%s*uhr" % (X0, K), ya), ("%s+%s*uhr" % (X0, K), 2.05), farbe=DUNKEL, dicke=1.5, dash=DASH)
    uhr_z = s.zahl(None, "uhr", (3.35, 2.25), stellen=1, vor="t = ", nach=" s", groesse=FK, ausrichtung="right",
                   farbe=DUNKEL)
    fork1 = pf(s, (xt(0.1), yS1 - 0.04), (xt(0.1), yP1 + 0.06), farbe=BLAU, dicke=2, spitze=0.08)
    fork2 = pf(s, (xt(0.1), yS2 - 0.04), (xt(0.1), yP2 + 0.06), farbe=BLAU, dicke=2, spitze=0.08)
    stuecke = [(0.1, 1.0), (1.0, 2.0), (2.0, 3.1)]
    o_sleep = [linie(s, (xt(a), yP1), (xt(b), yP1), BLAU, 6) for a, b in stuecke]
    o_wait = [linie(s, (xt(a), yS1), (xt(b), yS1), GRAU, 2.5, DASH) for a, b in stuecke]
    u_sleep = [linie(s, (xt(a), yP2), (xt(b), yP2), BLAU, 6) for a, b in stuecke]
    u_shell = [linie(s, (xt(max(a, 0.25)), yS2), (xt(b), yS2), SCHWARZ, 3) for a, b in stuecke]
    l_wartet = L(s, "wartet", W_WARTET, (xt(1.6), yS1 + 0.18), FM, "center", GRAU)
    prompt1 = tx(s, "$", (xt(3.25), yS1), TT, "center", HELLGRAU)
    dollar = tx(s, "$", (xt(0.15), yS2 + 0.2), TK, "left")
    echo = tx(s, "$ echo $!", (xt(1.0), yS2 + 0.2), TK, "left")
    ps_ = tx(s, "$ ps …", (xt(2.1), yS2 + 0.2), TK, "left")
    end1 = linie(s, (xt(3.1), yP1 - 0.1), (xt(3.1), yP1 + 0.1), DUNKEL, 3)
    l_jetzt = L(s, "jetzt", W_PROMPT_JETZT, (2.95, (yS1 + yP1) / 2), FM, "right", DUNKEL)
    o_shell = linie(s, (xt(3.4), yS1), (xt(4.0), yS1), SCHWARZ, 3)
    u_sleep4 = pf(s, (xt(3.1), yP2), (xt(4.0) + 0.12, yP2), farbe=BLAU, dicke=6, spitze=0.12)
    u_shell4 = linie(s, (xt(3.1), yS2), (xt(4.0), yS2), SCHWARZ, 3)
    l_weiter = L(s, "weiter", W_LAEUFT_WEITER, (2.95, yP2 - 0.2), FM, "right", BLAU)
    schritt(s, EIN(stat + [marke, uhr_z], 0.7))
    s.pause(0.4)
    with s.gleichzeitig():
        s.verstellen("uhr", 0.1, dauer=0.4)
        schritt(s, ZEICHNE([fork1, fork2], 0.4), EIN([pk1, pk2], 0.4))
    extra = [[l_wartet, prompt1, dollar], [echo], [ps_]]
    for i, (a, b) in enumerate(stuecke):
        d = round(0.9 * (b - a) + 0.1, 2)
        with s.gleichzeitig():
            s.verstellen("uhr", b, dauer=d)
            schritt(s, ZEICHNE([o_sleep[i], o_wait[i], u_sleep[i], u_shell[i]], d), EIN(extra[i], 0.4))
    with s.gleichzeitig():
        schritt(s, ZEICHNE(end1, 0.4), EIN(l_jetzt, 0.6))
        s.ersetzen(prompt1, "$", farbe=SCHWARZ, dauer=0.6)
    with s.gleichzeitig():
        s.verstellen("uhr", 4.0, dauer=0.9)
        schritt(s, ZEICHNE([o_shell, u_sleep4, u_shell4], 0.9))
    schritt(s, EIN(l_weiter, 0.5))
    s.speichern()


J2 = "[2]+   656 Running                    sleep 301 &"
J1 = "[1]-   654 Running                    sleep 300 &"
W_JOB = [("Jobnummer (nur in dieser Shell gültig)", "job number (valid only in this shell)",
          "número de trabajo (solo válido en esta shell)", "作业号（仅在此 Shell 中有效）",
          "numéro de tâche (valable seulement dans ce shell)", "iş numarası (yalnızca bu kabukta geçerli)"),
         ("Marke: aktueller Job", "marker: current job", "marca: trabajo actual", "标记：当前作业", "marque : tâche courante",
          "işaret: geçerli iş"),
         ("PID (im ganzen System gültig)", "PID (valid in the whole system)", "PID (válido en todo el sistema)",
          "PID（在整个系统中有效）", "PID (valable dans tout le système)", "PID (tüm sistemde geçerli)"),
         ("Zustand des Jobs", "state of the job", "estado del trabajo", "作业状态", "état de la tâche", "işin durumu"),
         ("Befehl", "command", "orden", "命令", "commande", "komut"),
         ("läuft im Hintergrund", "runs in the background", "se ejecuta en segundo plano", "在后台运行",
          "s'exécute en arrière-plan", "arka planda çalışır"),
         ("Marke: voriger Job", "marker: previous job", "marca: trabajo anterior", "标记：上一个作业",
          "marque : tâche précédente", "işaret: önceki iş")]


def k8jobliste():
    """Die Zeile [2]+ 656 Running sleep 301 & aus jobs -l in sechs Teile zerlegt (Klammern mit Nummern, Bedeutungen als
    Liste); darunter die Zeile von Job 1 mit der Marke - (7); zum Schluss zeigen %+ und %- auf ihre Zeilen."""
    s = Szene("linux/k8jobliste", reihenfolge="anlegen")
    x0 = -2.3
    g = s.raster([J2, J1], (x0, 1.55), groesse=20, zeilenabstand=2.4)
    teile = [(0, 2), (3, 3), g.finde(0, "656"), g.finde(0, "Running"), g.finde(0, "sleep 301"), g.finde(0, "&")]
    cw = g.zelle[0]                                   # nur das Zeichen hinterlegen, nicht die ganze Zeilenhöhe
    m_plus = box(s, (g.xm(3), g.y(0)), cw + 0.02, 0.22, ORANGE, ORANGE, 0, "rect", deckung=0.35)
    m_minus = box(s, (g.xm(3), g.y(1)), cw + 0.02, 0.22, ORANGE, ORANGE, 0, "rect", deckung=0.35)
    kl = [g.klammer(0, a, b, str(i + 1), seite="oben", farbe=BLAU, groesse=FM) for i, (a, b) in enumerate(teile)]
    kl.append(g.klammer(1, 3, 3, "7", seite="unten", farbe=BLAU, groesse=FM))
    leg = []
    for i, w in enumerate(W_JOB):
        y = r4(0.55 - 0.27 * i)
        leg.append([text(s, str(i + 1), (-3.1, y), FM, "right", BLAU), L(s, "job%d" % i, w, (-3.0, y), FM, "left")])
    jp = [tx(s, "%+", (-3.4, g.y(0)), TT, "left", ORANGE), pf(s, (-2.95, g.y(0)), (x0 - 0.06, g.y(0)), farbe=ORANGE,
                                                                 dicke=2.5, spitze=0.1)]
    jm = [tx(s, "%-", (-3.4, g.y(1)), TT, "left", ORANGE), pf(s, (-2.95, g.y(1)), (x0 - 0.06, g.y(1)), farbe=ORANGE,
                                                                 dicke=2.5, spitze=0.1)]
    schritt(s, EIN(g.zeile(0), 0.6))
    s.pause(0.4)
    for i in range(6):
        teile_i = [kl[i][1]] + leg[i] + ([m_plus] if i == 1 else [])
        schritt(s, ZEICHNE(kl[i][0], 0.4), EIN(teile_i, 0.4))
    s.pause(0.6)
    schritt(s, EIN(g.zeile(1), 0.5))
    schritt(s, ZEICHNE(kl[6][0], 0.4), EIN([kl[6][1], m_minus] + leg[6], 0.4))
    s.pause(0.6)
    schritt(s, EIN(jp, 0.6))
    schritt(s, EIN(jm, 0.6))
    s.speichern()


JOBS4 = ["[1]   Running                    sleep 300 &",
         "[2]   Running                    sleep 301 &",
         "[3]-  Stopped                    sleep 302",
         "[4]+  Stopped                    cat"]
W_HAELT = ("Kernel hält es an", "kernel stops it", "el kernel lo detiene", "内核将其暂停", "le noyau l'arrête",
           "çekirdek onu durdurur")
W_ANGEH_T = ("angehalten (T)", "stopped (T)", "detenido (T)", "已暂停（T）", "arrêté (T)", "durduruldu (T)")


def k8hintergrundlesen():
    """Terminal (wörtlich aus dem Heft) mit Tastatur; rechts die Felder Hintergrund und Vordergrund. cat & landet im
    Hintergrund, will von der Tastatur lesen, der Kernel hält es an (T); jobs zeigt es als Stopped. fg holt cat nach vorn,
    die Shell wartet; „Hallo“ wandert zu cat und kommt als Ausgabe zurück."""
    s = Szene("linux/k8hintergrundlesen", reihenfolge="anlegen")
    t = s.terminal(pos=(-3.45, 2.3), spalten=44, zeilen=12, prompt=P8, groesse=17)
    hg = [box(s, (1.85, 1.825), 2.9, 1.05, GRAU, GRAU_HELL, 1.5), L(s, "hg", W_HG, (0.52, 2.2), FM, "left", DUNKEL)]
    vg = [box(s, (1.85, 0.6), 2.9, 1.0, GRAU, GRAU_HELL, 1.5), L(s, "vg", W_VG, (0.52, 0.95), FM, "left", DUNKEL)]
    kb = tastatur(s, -1.7, -0.45)
    l_kb = L(s, "tastatur", W_TASTATUR, (-1.7, -0.82), FM, "center", GRAU)
    pk = pf(s, (-1.25, -0.45), (1.85, 0.08), knick="hv", farbe=ORANGE, dicke=2.5, spitze=0.1)
    shell = chip(s, (1.85, 0.55), "bash", b=0.9)
    cat = chip(s, (1.5, 1.8), "cat 659", b=1.0)
    versuch = pf(s, (1.5, 1.64), (1.5, 1.18), farbe=ORANGE, dicke=2.5, dash=DASH, spitze=0.09)
    stopp = kreuz(s, 1.5, 1.2, 0.18)
    l_stopp = L(s, "haelt", W_HAELT, (1.7, 1.2), FM, "left", ROT)
    pz = pause_zeichen(s, 2.25, 1.8, ORANGE)
    l_t = L(s, "angeh", W_ANGEH_T, (2.42, 1.8), FM, "left", ORANGE)
    schl = schleier(s, (1.1, 0.55), 0.95, 0.35, 0.55)
    l_w = L(s, "wartet", W_WARTET, (1.1, 0.25), FM, "center", GRAU)
    schritt(s, EIN([t.id] + hg + vg + kb + [l_kb, pk] + shell, 0.7))
    s.pause(0.4)
    t.eingabe("cat &")
    with s.gleichzeitig():
        t.schritt("[4] 659\n" + P8, dauer=0.6)
        s.einblenden(*cat, dauer=0.6)
    s.pause(0.4)
    schritt(s, ZEICHNE(versuch, 0.6))
    schritt(s, EIN([stopp, l_stopp] + pz + [l_t], 0.7))
    s.pause(0.5)
    t.befehl("jobs", "\n".join(JOBS4), pfad=PFAD)
    r_job = t.rahmen(6, 0, len(JOBS4[3]) - 1, ORANGE, 2.5)
    schritt(s, EIN(r_job, 0.5))
    s.pause(0.6)
    t.eingabe("fg")
    with s.gleichzeitig():
        t.ausgabe("cat", dauer=0.9)
        schritt(s, *VERS(cat, 2.55 - 1.5, 0.55 - 1.8, 0.9), *VERS(shell, 1.1 - 1.85, 0, 0.9),
                AUS([versuch, stopp, l_stopp, l_t, r_job] + pz, 0.5), EIN([schl, l_w], 0.9))
    schritt(s, BETONE(kb[0], 0.7))
    t.tippen("Hallo")
    xm, ya = t.xm(0, 4), t.y(9)
    karte_b, karte_h = t.xr(4) - t.x(0) + 0.14, t.zelle[1] + 0.08
    f0 = [box(s, (xm, ya), karte_b, karte_h, GRAU, WEISS, 1.5), t.teil(9, 0, 4, farbe=SCHWARZ)]
    with s.gleichzeitig():
        t.schritt("\n", dauer=0.4)
        s.einblenden(*f0, dauer=0.4)
    schritt(s, *VERS(f0, 2.55 - xm, 0.9 - ya, 0.9))
    schritt(s, *VERS(f0, xm - 2.55, t.y(10) - 0.9, 0.9))
    with s.gleichzeitig():
        s.ausblenden(*f0, dauer=0.4)
        t.ausgabe("Hallo", dauer=0.4)
    s.speichern()


W_HGL = ("Hintergrund (läuft)", "background (running)", "segundo plano (en ejecución)", "后台（运行中）",
         "arrière-plan (en cours)", "arka plan (çalışıyor)")
W_ENDE = ("Ende", "end", "fin", "结束", "fin", "son")
W_ENDE_PFEIL = ("Strg+C, Programmende", "Ctrl+C, program ends", "Ctrl+C, fin del programa", "Ctrl+C、程序结束",
                "Ctrl+C, fin du programme", "Ctrl+C, program biter")


def k8jobzustaende():
    """Felder Vordergrund (mit Tastatur), Hintergrund (läuft), angehalten. Das Kärtchen [3] sleep 302 startet vorn, wandert
    mit Strg+Z nach „angehalten“, mit bg in den Hintergrund und mit fg zurück; die Tastatur leuchtet, wenn es vorn ist.
    Dann die übrigen Übergänge: Start mit &, fg aus „angehalten“, Strg+C/Ende ins Aus."""
    s = Szene("linux/k8jobzustaende", reihenfolge="anlegen")
    VG, HG, AN = (-2.15, 0.55), (2.0, 1.5), (2.0, -0.45)
    felder = [box(s, VG, 2.4, 1.4, DUNKEL, WEISS, 2.5), L(s, "vg", W_VG, (VG[0], 1.07), FM, "center", DUNKEL),
              box(s, HG, 2.6, 0.9, DUNKEL, WEISS, 2.5), L(s, "hgl", W_HGL, (HG[0], 1.78), FM, "center", DUNKEL),
              box(s, AN, 2.6, 0.9, DUNKEL, WEISS, 2.5), L(s, "an", W_ANGEH, (AN[0], -0.17), FM, "center", DUNKEL)]
    kb = tastatur(s, VG[0], 0.2)
    aus = [box(s, (VG[0], -1.2), 1.4, 0.38, HELLGRAU, WEISS, 2, dash=DASH), L(s, "ende", W_ENDE, (VG[0], -1.2), FM, "center",
                                                                                 GRAU)]
    start = [tx(s, "$ sleep 302", (VG[0], 1.75), TK), pf(s, (VG[0], 1.6), (VG[0], 1.28), farbe=DUNKEL, dicke=2.5,
                                                         spitze=0.1)]
    karte = chip(s, (VG[0], 0.62), "[3] sleep 302", ORANGE, ORANGE_HELL, b=1.45)
    c_vg, c_hg, c_an = (VG[0], 0.62), (HG[0], 1.4), (AN[0], -0.55)

    def pfeil(a, b, t, lpos, ausr="center", tt=True, key=None):
        lt = tx(s, t, lpos, TK, ausr, BLAU) if tt else L(s, key, t, lpos, FM, ausr, BLAU)
        return [pf(s, a, b, farbe=BLAU, dicke=2.5, spitze=0.1), lt]

    p_z = pfeil((-0.93, 0.32), (0.68, -0.28), W_STRGZ, (-0.02, 0.2), tt=False, key="strgz")
    p_bg = pfeil((2.0, 0.02), (2.0, 1.03), "bg", (2.12, 0.52), "left")
    p_fg = pfeil((0.68, 1.4), (-0.93, 0.95), "fg", (-0.12, 1.36))
    p_amp = [tx(s, "$ sleep 300 &", (HG[0], 2.4), TK), pf(s, (HG[0], 2.27), (HG[0], 1.97), farbe=DUNKEL, dicke=2.5,
                                                          spitze=0.1)]
    p_fg2 = pfeil((0.68, -0.62), (-0.93, -0.02), "fg", (-0.17, -0.5))
    p_ende = pfeil((VG[0], -0.17), (VG[0], -0.99), W_ENDE_PFEIL, (VG[0] + 0.12, -0.58), "left", tt=False, key="endepf")
    schritt(s, EIN(felder + kb + aus, 0.7))
    schritt(s, EIN(start[0], 0.5), ZEICHNE(start[1], 0.5), WACHS(karte[0], 0.5), EIN(karte[1], 0.5))
    schritt(s, BETONE(kb[0], 0.7))
    s.pause(0.5)

    def zug(p, von, nach, extra=()):
        schritt(s, ZEICHNE(p[0], 0.8), EIN(p[1], 0.8), *VERS(karte, nach[0] - von[0], nach[1] - von[1], 0.9), *extra)

    zug(p_z, c_vg, c_an)
    zug(p_bg, c_an, c_hg)
    zug(p_fg, c_hg, c_vg)
    schritt(s, BETONE(kb[0], 0.7))
    s.pause(0.6)
    schritt(s, EIN(p_amp[0], 0.6), ZEICHNE(p_amp[1], 0.6))
    schritt(s, ZEICHNE(p_fg2[0], 0.6), EIN(p_fg2[1], 0.6))
    schritt(s, ZEICHNE(p_ende[0], 0.6), EIN(p_ende[1], 0.6))
    s.speichern()


# ================================================================== Abschnitt 4: Signale
W_REAKTIONEN = ("Reaktionen", "reactions", "reacciones", "响应方式", "réactions", "tepkiler")
W_IGNOR = ("ignorieren", "ignore", "ignorar", "忽略", "ignorer", "yok say")
W_UNTERBR = ("unterbrochen", "interrupted", "interrumpido", "被中断", "interrompu", "kesildi")


def k8signal():
    """Links zwei Absender: Tastatur mit Strg+C (grau, bekannt) und der Prozess kill 665. Das Kärtchen 15 SIGTERM geht über
    den Kernel zu sleep 400 (PID 665); dessen Spur bricht ab, er schaut in seiner Reaktionstabelle nach (SIGTERM: beenden)
    und endet."""
    s = Szene("linux/k8signal", reihenfolge="anlegen")
    kern = [flaeche(s, -1.55, -0.55, -0.25, 2.05, GRAU_HELL), L(s, "kernel", W_KERNEL, (-0.9, 1.88), FM, "center", GRAU)]
    kb = tastatur(s, -2.75, 1.55)
    l_kb = L(s, "strgc", W_STRGC, (-2.75, 1.2), FM, "center", GRAU)
    sint = chip(s, (-0.9, 1.55), "2 SIGINT", GRAU, WEISS, b=1.05, textfarbe=GRAU)
    grau_pf = [pf(s, (-2.3, 1.55), (-1.45, 1.55), farbe=HELLGRAU, dicke=2, spitze=0.08),
               pf(s, (-0.35, 1.55), (1.15, 1.55), farbe=HELLGRAU, dicke=2, dash=DASH, spitze=0.08)]
    kill = chip(s, (-2.75, 0.05), "kill 665", b=1.15, h=0.36)
    ziel = chip(s, (1.95, 1.5), "sleep 400", b=1.3, h=0.38)
    l_pid = tx(s, "PID 665", (2.72, 1.5), TK, "left", GRAU)
    spur = linie(s, (1.3, 1.12), (2.3, 1.12), GRUEN, 4)
    bruch = linie(s, (2.3, 1.02), (2.3, 1.22), ROT, 3)
    l_unt = L(s, "unterbr", W_UNTERBR, (2.42, 1.12), FM, "left", ROT)
    tab = [box(s, (2.15, 0.07), 2.5, 0.92, GRAU, WEISS, 1.5, "rect"),
           L(s, "reakt", W_REAKTIONEN, (2.15, 0.7), FM, "center", GRAU)]
    zeilen = [("2 SIGINT", W_BEENDEN, "be1"), ("15 SIGTERM", W_BEENDEN, "be2"), ("17 SIGCHLD", W_IGNOR, "ign")]
    tz = []
    for i, (sig, w, key) in enumerate(zeilen):
        y = r4(0.35 - 0.28 * i)
        tz.append([tx(s, sig, (0.98, y), TK, "left"), L(s, key, w, (2.4, y), FM, "left")])
    r_term = box(s, (2.15, 0.07), 2.4, 0.26, ORANGE, ORANGE, 0, "rect", deckung=0.25)
    karte = chip(s, (-2.75, 0.5), "15 SIGTERM", ORANGE, ORANGE_HELL, b=1.25)
    p1 = pf(s, (-2.1, 0.05), (-1.6, 0.05), farbe=ORANGE, dicke=2.5, spitze=0.1)
    p2 = pf(s, (-0.25, 0.45), (1.2, 1.35), farbe=ORANGE, dicke=2.5, spitze=0.1)
    schl = schleier(s, (1.95, 1.5), 1.4, 0.46, 0.6)
    schritt(s, EIN(kern + kb + [l_kb] + sint + grau_pf + kill + ziel + [l_pid] + tab + flach(tz), 0.7), ZEICHNE(spur, 1.2))
    s.pause(0.5)
    schritt(s, EIN(karte, 0.5))
    schritt(s, ZEICHNE(p1, 0.6), *VERS(karte, -0.9 + 2.75, 0.05 - 0.5 + 0.4, 0.8))
    schritt(s, ZEICHNE(p2, 0.6), *VERS(karte, 1.95 + 0.9, 1.92 - 0.45, 0.9))
    schritt(s, ZEICHNE(bruch, 0.3), EIN(l_unt, 0.5))
    s.pause(0.4)
    schritt(s, EIN(r_term, 0.5), BETONE(tz[1], 0.8))
    with s.gleichzeitig():
        schritt(s, EIN(schl, 0.7))
        s.ersetzen(l_unt, T(s, "beendet", *W_BEENDET), farbe=ROT, dauer=0.7)
    s.speichern()


W_PROZESS = ("Prozess", "process", "proceso", "进程", "processus", "süreç")
W_REAKTION = ("Reaktion", "reaction", "reacción", "响应", "réaction", "tepki")
W_SPEICHER = ("Speicher", "memory", "memoria", "内存", "mémoire", "bellek")
W_SATZ = ("„Heute regnet es, d…“", "\"It is raining, so…\"", "«Hoy llueve, así…»", "“今天下雨，所…”", "« Il pleut, donc… »",
          "\"Bugün yağmur var, b…\"")
W_GESPEICHERT = ("Satz gespeichert", "sentence saved", "frase guardada", "句子已保存", "phrase enregistrée", "cümle kaydedildi")
W_GELOESCHT = ("gelöscht", "deleted", "borrado", "已删除", "supprimé", "silindi")
W_AUFGERAEUMT = ("aufgeräumt", "cleaned up", "ordenado", "已清理", "rangé", "toparlandı")
W_SOFORT = ("sofort entfernt", "removed at once", "eliminado al instante", "立即被移除", "supprimé aussitôt", "hemen kaldırıldı")
W_VERLOREN = ("Satz verloren", "sentence lost", "frase perdida", "句子丢失", "phrase perdue", "cümle kayboldu")
W_LIEGEN = ("bleibt liegen", "is left behind", "queda ahí", "仍然留着", "reste sur place", "geride kalır")


def k8termkill():
    """Zwei Prozesse mit entwurf.tmp und einem halben Satz im Speicher. Links SIGTERM: der Prozess speichert den Satz,
    löscht entwurf.tmp und endet (aufgeräumt). Rechts SIGKILL: Schloss an der Reaktion, der Kernel entfernt den Prozess
    sofort; entwurf.tmp bleibt liegen, der Satz ist verloren."""
    s = Szene("linux/k8termkill", reihenfolge="anlegen")
    trenn = linie(s, (0, 2.45), (0, -1.35), HELLGRAU, 2, DASH)
    seiten = {}
    for seite, cx in (("L", -1.75), ("R", 1.75)):
        pr = wchip(s, (cx - 0.45, 1.4), "proz" + seite, W_PROZESS, 1.5, BLAU, BLAU_HELL, h=0.4)
        re_ = wchip(s, (cx + 0.95, 1.4), "reakt" + seite, W_REAKTION, 1.0, GRAU, WEISS, h=0.4, textfarbe=DUNKEL)
        sp = [L(s, "sp" + seite, W_SPEICHER, (cx - 1.5, 0.98), FM, "left", GRAU), box(s, (cx, 0.65), 3.0, 0.38, GRAU, GELB, 1.5,
                                                                                    "rect")]
        satz = L(s, "satz" + seite, W_SATZ, (cx, 0.65), FM, "center")
        ent = [datei_symbol(s, cx - 1.3, 0.05), tx(s, "entwurf.tmp", (cx - 1.12, 0.05), TK, "left")]
        seiten[seite] = (cx, pr, re_, sp, satz, ent)
    # links: SIGTERM
    cx, pr, re_, sp, satz, ent = seiten["L"]
    k_t = chip(s, (cx, 2.25), "15 SIGTERM", ORANGE, ORANGE_HELL, b=1.25)
    datei = [box(s, (cx, -0.55), 3.0, 0.38, GRUEN, WEISS, 1.5, "rect"), datei_symbol(s, cx - 1.3, -0.55)]
    kopie = L(s, "satzk", W_SATZ, (cx, 0.65), FM, "center")
    l_gesp = L(s, "gesp", W_GESPEICHERT, (cx, -0.88), FM, "center", GRUEN)
    strich_l = linie(s, (cx - 1.14, 0.05), (cx - 0.26, 0.05), GRAU, 2)
    l_gel = L(s, "gel", W_GELOESCHT, (cx - 0.1, 0.05), FM, "left", GRAU)
    schl_e = schleier(s, (cx - 0.72, 0.05), 1.3, 0.28, 0.6)
    geist_l = geist(s, (cx - 0.45, 1.4), 1.5, 0.4)
    schl_l = schleier(s, (cx - 0.45, 1.4), 1.6, 0.5, 0.65)
    schl_sp = schleier(s, (cx, 0.65), 3.1, 0.46, 0.6)          # mit dem Prozess endet auch sein Speicher
    l_bl = L(s, "beendetL", W_BEENDET, (cx - 0.45, 1.4), FM, "center", GRAU)
    l_auf = L(s, "aufger", W_AUFGERAEUMT, (cx, -1.2), FS, "center", GRUEN)
    # rechts: SIGKILL
    cxr, prr, rer, spr, satzr, entr = seiten["R"]
    k_k = chip(s, (cxr, 2.25), "9 SIGKILL", ROT, ROT_HELL, b=1.15)
    schloss = s.schloss((r4(cxr + 1.5), 1.62), 0.28, farbe=ROT)
    geist_r = geist(s, (cxr - 0.45, 1.4), 1.5, 0.4)
    l_sof = L(s, "sofort", W_SOFORT, (cxr - 0.45, 1.4), FM, "center", ROT)
    kz = kreuz(s, cxr, 0.65, 0.3)
    l_verl = L(s, "verl", W_VERLOREN, (cxr, 0.3), FM, "center", ROT)
    m_ent = box(s, (cxr - 0.72, 0.05), 1.3, 0.28, ORANGE, ORANGE, 0, "rect", deckung=0.3)
    l_lieg = L(s, "liegen", W_LIEGEN, (cxr + 0.1, 0.05), FM, "left", ORANGE)
    alles = [trenn]
    for c, p, r, spi, sa, e in seiten.values():
        alles += p + r + spi + [sa] + e
    schritt(s, EIN(alles, 0.7))
    s.pause(0.5)
    schritt(s, EIN(k_t, 0.4))
    schritt(s, *VERS(k_t, -0.45, -0.4, 0.7))
    schritt(s, EIN(datei, 0.5), EIN(kopie, 0.3))
    schritt(s, VER(kopie, 0, -1.2, 0.9))
    schritt(s, EIN(l_gesp, 0.4))
    schritt(s, EIN([schl_e, strich_l, l_gel], 0.6))
    schritt(s, AUS(pr, 0.6), EIN([geist_l, schl_l, l_bl, schl_sp], 0.6))
    schritt(s, EIN(l_auf, 0.5))
    s.pause(0.6)
    schritt(s, EIN(k_k, 0.4))
    schritt(s, *VERS(k_k, -0.45, -0.4, 0.7))
    schritt(s, WACHS(schloss, 0.5), BETONE(rer, 0.6))
    schritt(s, AUS(prr, 0.4), EIN([geist_r, l_sof], 0.4))
    schritt(s, EIN([kz, l_verl], 0.6))
    schritt(s, EIN([m_ent, l_lieg], 0.6))
    s.speichern()


W_STATUS = ("Status", "status", "estado", "状态", "statut", "durum")
W_NUMMER = ("Nummer", "number", "número", "编号", "numéro", "numara")
W_SIGNAL = ("Signal", "signal", "señal", "信号", "signal", "sinyal")
W_DURCH = ("ausgelöst durch", "caused by", "causado por", "触发方式", "déclenché par", "tetikleyen")


def k8exitrechnung():
    """Rechenbild, Zeile für Zeile: Status − 128 = Nummer, dann der Name und der Auslöser (kill, Strg+C, kill -9,
    kill -STOP, Strg+Z). In jeder Zeile erscheinen Status, Subtraktion, Nummer und Name nacheinander."""
    s = Szene("linux/k8exitrechnung", reihenfolge="anlegen")
    xs, xo, xn, xname, xw = -2.15, -1.45, -0.55, -0.25, 1.25
    kopf = [L(s, "status", W_STATUS, (-2.45, 1.85), FM, "center", GRAU),
            L(s, "nummer", W_NUMMER, (-0.8, 1.85), FM, "center", GRAU),
            L(s, "signal", W_SIGNAL, (xname, 1.85), FM, "left", GRAU),
            L(s, "durch", W_DURCH, (xw, 1.85), FM, "left", GRAU),
            linie(s, (-3.0, 1.66), (3.2, 1.66), HELLGRAU, 2)]
    faelle = [(143, 15, "SIGTERM", "kill"), (130, 2, "SIGINT", W_STRGC), (137, 9, "SIGKILL", "kill -9"),
              (147, 19, "SIGSTOP", "kill -STOP"), (148, 20, "SIGTSTP", W_STRGZ)]
    schritt(s, EIN(kopf, 0.6))
    s.pause(0.4)
    for i, (st, n, name, wer) in enumerate(faelle):
        y = r4(1.42 - 0.4 * i)
        t_s = text(s, str(st), (xs, y), FS, "right")
        t_o = text(s, "− 128 =", (xo, y), FS, "center", DUNKEL)
        t_n = text(s, str(n), (xn, y), FS, "right", ORANGE)
        t_name = tx(s, name, (xname, y), 20, "left", ORANGE)
        t_wer = tx(s, wer, (xw, y), TK, "left", GRAU) if isinstance(wer, str) else L(s, "wer%d" % i, wer, (xw, y), FM,
                                                                                      "left", GRAU)
        schritt(s, EIN(t_s, 0.35))
        schritt(s, EIN(t_o, 0.35))
        schritt(s, EIN(t_n, 0.35))
        schritt(s, EIN([t_name, t_wer], 0.4))
        s.pause(0.3)
    s.speichern()


W_KOMMT = ("Signal kommt an", "signal is delivered", "la señal llega", "信号送达", "le signal arrive", "sinyal ulaşır")
W_SUDO_KOMMT = ("mit sudo kill: kommt an", "with sudo kill: delivered", "con sudo kill: llega", "用 sudo kill：送达",
                "avec sudo kill : arrive", "sudo kill ile: ulaşır")
W_PRUEFT = ("Kernel vergleicht", "kernel compares", "el kernel compara", "内核比较", "le noyau compare", "çekirdek karşılaştırır")


def k8wer():
    """Absender kill (real 1000, effektiv 1000), Ziele sleep 600 (student: real 1000, gespeichert 1000) und sleep 700
    (root: 0, 0). Linien von real/effektiv zu real/gespeichert: oben gleich (grün), das Signal kommt an; unten keine
    Gleichheit (rot), Operation not permitted. Zuletzt sudo kill (real 0, effektiv 0): auch unten grün."""
    s = Szene("linux/k8wer", reihenfolge="anlegen")
    kern = [flaeche(s, -0.85, -1.65, 0.7, 2.15, GRAU_HELL), L(s, "prueft", W_PRUEFT, (-0.075, 1.98), FM, "center", GRAU)]

    def karte(mitte, name, zeilen, key, rand=BLAU, fuellung=BLAU_HELL, wer=None):
        x, y = mitte
        teile = [box(s, mitte, 1.75, 0.92, rand, fuellung, 2)]
        if wer:                                       # Ziel: Programm links, Besitzer rechts
            teile += [tx(s, name, (x - 0.78, y + 0.28), TK, "left"), tx(s, wer, (x + 0.78, y + 0.28), TK, "right", GRAU)]
        else:
            teile.append(tx(s, name, (x, y + 0.28), TK, "center"))
        ys = []
        for j, (w, wert) in enumerate(zeilen):
            yy = r4(y + 0.0 - 0.27 * j)
            teile += [L(s, "%s%d" % (key, j), w, (x - 0.78, yy), FM, "left", DUNKEL), tx(s, wert, (x + 0.78, yy), TK, "right")]
            ys.append(yy)
        return teile, ys

    k1, yk1 = karte((-2.45, 0.55), "kill", [(W_REAL, "1000"), (W_EFF, "1000")], "k")
    z1, yz1 = karte((2.45, 1.55), "sleep 600", [(W_REAL, "1000"), (W_GESP, "1000")], "z1", wer="student")
    z2, yz2 = karte((2.45, -0.25), "sleep 700", [(W_REAL, "0"), (W_GESP, "0")], "z2", GRAU, GRAU_HELL, wer="root")
    k2, yk2 = karte((-2.45, -1.15), "sudo kill", [(W_REAL, "0"), (W_EFF, "0")], "s", ORANGE, ORANGE_HELL)

    def linien(ya, yb, farbe, dash=""):
        return [linie(s, (-1.57, a), (1.57, b), farbe, 2, dash) for a in ya for b in yb]

    l1 = linien(yk1, yz1, GRUEN)
    l2 = linien(yk1, yz2, ROT, DASH)
    l3 = linien(yk2, yz2, GRUEN)
    ok1 = [L(s, "kommt", W_KOMMT, (1.6, 0.9), FM, "left", GRUEN)]
    nein = tx(s, "Operation not permitted", (1.6, -0.88), TK, "left", ROT)
    ok2 = L(s, "sudokommt", W_SUDO_KOMMT, (1.6, -1.15), FM, "left", GRUEN)
    schritt(s, EIN(kern + k1 + z1 + z2, 0.7))
    s.pause(0.5)
    schritt(s, ZEICHNE(l1, 0.9))
    schritt(s, EIN(ok1, 0.5))
    s.pause(0.6)
    schritt(s, ZEICHNE(l2, 0.9))
    schritt(s, EIN(nein, 0.5))
    s.pause(0.6)
    schritt(s, EIN(k2, 0.6))
    schritt(s, ZEICHNE(l3, 0.9))
    schritt(s, EIN(ok2, 0.5))
    s.speichern()


# ================================================================== Bildschirm: top (Unterabschnitt 2.7)
TOP_KOPF = ["top - 15:25:53 up 1 min,  1 user,  load average: 0.20, 0.08, 0.03",
            "Tasks:  29 total,   1 running,  28 sleeping,   0 stopped,   0 zombie",
            "%Cpu(s):  0.0 us,  0.7 sy,  0.0 ni, 98.7 id,  0.7 wa,  0.0 hi,  0.0 si,  0.0 st",
            "MiB Mem :  31846.7 total,  30985.9 free,    736.2 used,    433.1 buff/cache",
            "MiB Swap:   8192.0 total,   8192.0 free,      0.0 used.  31110.5 avail Mem"]
TOP_TAB = ["    PID USER      PR  NI    VIRT    RES    SHR S  %CPU  %MEM     TIME+ COMMAND",
           "      1 root      20   0   24332  14060  10860 S   0.0   0.0   0:01.06 systemd",
           "      2 root      20   0    3120   2048   1920 S   0.0   0.0   0:00.02 init-sy+",
           "      6 root      20   0    3120   1792   1792 S   0.0   0.0   0:00.00 init",
           "     49 root      19  -1   42192  15744  14720 S   0.0   0.0   0:00.24 systemd+",
           "     83 systemd+  20   0   22412  14080  11648 S   0.0   0.0   0:00.11 systemd+"]
W_TOP = [("Zeit, Laufzeit, Last (wie uptime)", "time, uptime, load (as uptime)", "hora, tiempo activo, carga (como uptime)",
          "时间、运行时长、负载（同 uptime）", "heure, durée, charge (comme uptime)", "saat, çalışma süresi, yük (uptime gibi)"),
         ("Prozesse nach Zuständen", "processes by state", "procesos por estado", "按状态统计的进程", "processus par état",
          "duruma göre süreçler"),
         ("Aufteilung der Rechenzeit", "split of CPU time", "reparto del tiempo de CPU", "CPU 时间的分配",
          "répartition du temps CPU", "CPU süresinin dağılımı"),
         ("Speicher (wie free)", "memory (as free)", "memoria (como free)", "内存（同 free）", "mémoire (comme free)",
          "bellek (free gibi)"),
         ("Spaltenzeile (invers)", "column header (inverse)", "fila de columnas (invertida)", "列标题行（反色）",
          "ligne d'en-tête (inversée)", "sütun başlığı (ters renkli)"),
         ("sortiert: hier nach PID (-o -PID)", "sorted: here by PID (-o -PID)", "orden: aquí por PID (-o -PID)",
          "排序：此处按 PID（-o -PID）", "tri : ici par PID (-o -PID)", "sıralama: burada PID'ye göre (-o -PID)")]


def k8topbild():
    """top als Bildschirm mit der Momentaufnahme aus dem Heft (top -b -n 1 -o -PID, 2.7); kein Wertwechsel, weil es nur
    diese eine Momentaufnahme gibt. Nacheinander leuchten die Kopfzeilen (Zeit/Last, Aufgaben, CPU, Speicher), dann die
    inverse Spaltenzeile, zuletzt die oberste Prozesszeile (Sortierung). Nummern links, Liste darunter."""
    s = Szene("linux/k8topbild", reihenfolge="anlegen")
    t = s.top(TOP_KOPF, TOP_TAB, pos=(-3.11, 1.95), spalten=80, titel="student@labor: ~/linuxk8", groesse=18)
    teile = [(0, None, None, None), (1, None, None, None), (2, None, None, None), (3, None, None, 4), (6, 0, 79, None),
             (7, None, None, None)]
    xn = -3.28
    y_leg = (-0.62, -0.89, -1.16)
    schritte = []
    for k, (z, a, b, bis) in enumerate(teile):
        fr = t.rahmen(z, a, b, farbe=ORANGE, dicke=2.5, bis=bis, rand=0.02)
        y = t.y(z) if bis is None else r4((t.y(z) + t.y(bis)) / 2)
        nr = text(s, str(k + 1), (xn, y), FM, "center", ORANGE)
        xl, yl = (-3.35, y_leg[k]) if k < 3 else (0.15, y_leg[k - 3])
        leg = [text(s, str(k + 1), (xl, yl), FM, "left", ORANGE), L(s, "top%d" % k, W_TOP[k], (xl + 0.2, yl), FM, "left")]
        schritte.append((fr, [nr] + leg))
    schritt(s, EIN(t.id, 0.7))
    s.pause(0.6)
    vorher = None
    for k, (fr, rest) in enumerate(schritte):
        teile_k = [EIN([fr] + rest, 0.6)]
        if vorher is not None:
            teile_k.append(AUS(vorher, 0.5))
        if k in (4, 5):
            s.pause(0.4)
        schritt(s, *teile_k)
        s.pause(0.5)
        vorher = fr
    s.speichern()


# ================================================================== Abschnitt 5: Mit Signalen arbeiten (Phase 2b-2)
W_STD_BEENDEN = ("Standard: beenden", "default: terminate", "por defecto: terminar", "默认：终止", "par défaut : terminer",
                 "varsayılan: sonlandır")
W_ANHALTEN = ("anhalten", "stop", "detener", "暂停", "arrêter", "durdur")
W_EIGENE = ("eigene Reaktion: Aufräumen", "own reaction: clean up", "reacción propia: limpiar", "自定义响应：清理",
            "réaction propre : nettoyer", "kendi tepkisi: temizlik")
W_ABGEWIESEN = ("abgewiesen", "rejected", "rechazada", "被拒绝", "refusé", "reddedildi")
W_IGNORIERT = ("ignoriert", "ignored", "ignorada", "被忽略", "ignoré", "yok sayıldı")


def hoerer(s, cx, cy, r=0.13, farbe=DUNKEL):
    """Kleiner Telefonhörer: Bogen mit zwei Muscheln (Ergebnis: Liste)."""
    bogen = s.weg(None, "%s+%s*cos(pi*(0.12+0.76*t))" % (r4(cx), r4(r)), "%s+%s*sin(pi*(0.12+0.76*t))" % (r4(cy), r4(r)),
                  0, 1, farbe=farbe, dicke=6, n=25)
    teile = [bogen]
    for sx in (1, -1):
        x0, y0 = cx + sx * 0.93 * r, cy + 0.37 * r
        teile.append(linie(s, (r4(x0 - sx * 0.05 * r), r4(y0 + 0.1 * r)), (r4(x0 + sx * 0.3 * r), r4(y0 - 0.45 * r)), farbe, 9))
    return teile


def k8trap():
    """Reaktionstabelle der bash: SIGINT, SIGTERM (Standard: beenden), SIGKILL, SIGSTOP (Schloss). trap "…" TERM legt sich
    an die Zeile SIGTERM (eigene Reaktion: Aufräumen), trap "" TERM ersetzt es (ignorieren); trap "…" KILL prallt am
    Schloss ab. Zuletzt trifft 9 SIGKILL ein: Zeile KILL leuchtet, der Prozess endet."""
    s = Szene("linux/k8trap", reihenfolge="anlegen")
    rahmen_ = box(s, (1.3, 1.1), 4.1, 2.4, BLAU, WEISS, 2.5, "rect")
    kopf = [tx(s, "bash", (-0.55, 2.05), TT, "left"), L(s, "reakt", W_REAKTIONEN, (3.2, 2.05), FM, "right", GRAU),
            linie(s, (-0.65, 1.86), (3.25, 1.86), HELLGRAU, 1.5)]
    ys = {"INT": 1.6, "TERM": 1.2, "KILL": 0.8, "STOP": 0.4}
    zeilen = [("INT", "2 SIGINT", W_STD_BEENDEN), ("TERM", "15 SIGTERM", W_STD_BEENDEN), ("KILL", "9 SIGKILL", W_BEENDEN),
              ("STOP", "19 SIGSTOP", W_ANHALTEN)]
    tab, reakt = [], {}
    for k, sig, w in zeilen:
        tab.append(tx(s, sig, (-0.15, ys[k]), TK, "left"))
        reakt[k] = L(s, "r" + k, w, (1.0, ys[k]), FM, "left")
    schl = {k: s.schloss((-0.46, ys[k]), 0.22, farbe=GRAU) for k in ("KILL", "STOP")}
    k1 = chip(s, (-2.5, ys["TERM"]), 'trap "…" TERM', ORANGE, ORANGE_HELL, b=1.3)
    k2 = chip(s, (-2.45, 1.75), 'trap "" TERM', ORANGE, ORANGE_HELL, b=1.15)
    k3 = chip(s, (-2.5, ys["KILL"]), 'trap "…" KILL', ORANGE, ORANGE_HELL, b=1.3)
    kz3 = kreuz(s, -1.02, ys["KILL"], 0.18)
    l_ab = L(s, "abgew", W_ABGEWIESEN, (-1.9, 0.5), FM, "center", ROT)
    m_kill = box(s, (1.55, ys["KILL"]), 3.6, 0.3, ROT, ROT, 0, "rect", deckung=0.18)
    kk = chip(s, (1.3, -0.75), "9 SIGKILL", ROT, ROT_HELL, b=1.0)
    schl_ende = schleier(s, (1.3, 1.1), 4.2, 2.5, 0.6)
    l_ende = L(s, "beendet", W_BEENDET, (0.0, 2.05), FM, "left", ROT)
    schritt(s, EIN([rahmen_] + kopf + tab + list(reakt.values()) + list(schl.values()), 0.7))
    s.pause(0.5)
    schritt(s, EIN(k1, 0.4))
    schritt(s, *VERS(k1, 1.0, 0, 0.7))
    with s.gleichzeitig():
        s.ersetzen(reakt["TERM"], T(s, "eigene", *W_EIGENE), farbe=ORANGE, dauer=0.6)
    s.pause(0.5)
    schritt(s, EIN(k2, 0.4))
    with s.gleichzeitig():
        schritt(s, *VERS(k2, -1.43 + 2.45, ys["TERM"] - 1.75, 0.7), AUS(k1, 0.5))
        s.ersetzen(reakt["TERM"], T(s, "ignor", *W_IGNOR), farbe=ORANGE, dauer=0.7)
    s.pause(0.5)
    schritt(s, EIN(k3, 0.4))
    schritt(s, *VERS(k3, 1.26, 0, 0.5))
    schritt(s, *VERS(k3, -0.66, 0, 0.4), BETONE(schl["KILL"], 0.6))
    schritt(s, EIN([kz3, l_ab], 0.4))
    s.pause(0.5)
    schritt(s, EIN(kk, 0.4))
    schritt(s, *VERS(kk, 0, 0.4, 0.5))
    schritt(s, EIN(m_kill, 0.4), BETONE(reakt["KILL"], 0.6))
    schritt(s, EIN([schl_ende, l_ende], 0.6))
    s.speichern()


def k8timeout():
    """Stoppuhr und Zeitleiste 0–3 s (Parameter uhr). Grau oben: timeout 2 sleep 20 endet bei 2 s mit 124. Darunter
    timeout -k 1 2 bash -c 'trap "" TERM; sleep 20': bei 2 s prallt 15 SIGTERM ab (ignoriert), die Leiste läuft weiter;
    bei 3 s beendet 9 SIGKILL den Prozess, Status 137 = 128 + 9."""
    s = Szene("linux/k8timeout", reihenfolge="anlegen")
    X0, K = -1.9, 1.25

    def xt(t):
        return r4(X0 + K * t)

    yg, ygb, ym, yk, yb, ya = 2.35, 2.05, 1.55, 1.1, 0.62, -0.05
    stat = [tx(s, "$ timeout 2 sleep 20", (X0, yg), TK, "left", GRAU),
            tx(s, "$ timeout -k 1 2 bash -c 'trap \"\" TERM; sleep 20'", (X0, ym), TK, "left"),
            pf(s, (X0 - 0.05, ya), (2.25, ya), farbe=GRAU, dicke=2)]
    for t in range(4):
        stat += [linie(s, (xt(t), ya - 0.05), (xt(t), ya + 0.05), GRAU, 2),
                 text(s, "%d s" % t, (xt(t), ya - 0.22), FM, "center", GRAU)]
    cx, cy, r = -2.85, 1.0, 0.42
    uhr_ = [s.kreis(None, cx, cy, r, farbe=DUNKEL, dicke=2.5, fuellung=WEISS, deckung=1.0),
            box(s, (cx, r4(cy + r + 0.06)), 0.14, 0.1, DUNKEL, DUNKEL, 1, "rect")]
    for t in range(4):
        a = math.pi / 2 * t
        uhr_.append(linie(s, (r4(cx + 0.8 * r * math.sin(a)), r4(cy + 0.8 * r * math.cos(a))),
                          (r4(cx + r * math.sin(a)), r4(cy + r * math.cos(a))), GRAU, 2))
    s.parameter("uhr", 0)
    zeiger = s.linie(None, (cx, cy), ("%s+%s*sin(pi/2*uhr)" % (cx, 0.75 * r), "%s+%s*cos(pi/2*uhr)" % (cy, 0.75 * r)),
                     farbe=ORANGE, dicke=3)
    uhr_z = s.zahl(None, "uhr", (cx, 0.3), stellen=1, vor="t = ", nach=" s", groesse=FK, ausrichtung="center",
                   farbe=DUNKEL)
    marke_ = s.linie(None, ("%s+%s*uhr" % (X0, K), ya), ("%s+%s*uhr" % (X0, K), 2.5), farbe=DUNKEL, dicke=1.5, dash=DASH)
    g_bar = linie(s, (xt(0), ygb), (xt(2), ygb), HELLGRAU, 6)
    g_end = [linie(s, (xt(2), ygb - 0.1), (xt(2), ygb + 0.1), GRAU, 3), tx(s, "124", (2.42, ygb), TT, "left", GRAU)]
    b1 = linie(s, (xt(0), yb), (xt(2), yb), BLAU, 10)
    b2 = linie(s, (xt(2), yb), (xt(3), yb), BLAU, 10)
    k_t = chip(s, (xt(2), yk), "15 SIGTERM", ORANGE, ORANGE_HELL, b=1.0)
    l_ign = L(s, "ign", W_IGNORIERT, (xt(2), 0.33), FM, "center", ORANGE)
    k_k = chip(s, (xt(3), yk), "9 SIGKILL", ROT, ROT_HELL, b=0.92)
    ende = [linie(s, (xt(3), yb - 0.13), (xt(3), yb + 0.13), ROT, 4), tx(s, "137 = 128 + 9", (2.42, yb), TT, "left", ROT)]
    schritt(s, EIN(stat + uhr_ + [zeiger, uhr_z, marke_], 0.7))
    s.pause(0.4)
    with s.gleichzeitig():
        s.verstellen("uhr", 2, dauer=2.0, rate="linear")
        schritt(s, ZEICHNE([g_bar, b1], 2.0))
    schritt(s, EIN(g_end, 0.5), EIN(k_t, 0.5))
    s.pause(0.3)
    schritt(s, *VERS(k_t, 0, 0.82 - yk, 0.4))
    schritt(s, *VERS(k_t, 0, yk - 0.82, 0.4), EIN(l_ign, 0.5))
    s.pause(0.4)
    with s.gleichzeitig():
        s.verstellen("uhr", 3, dauer=1.0, rate="linear")
        schritt(s, ZEICHNE(b2, 1.0))
    schritt(s, EIN(k_k, 0.4))
    schritt(s, *VERS(k_k, 0, 0.82 - yk, 0.4))
    schritt(s, EIN(ende, 0.6))
    s.speichern()


W_AUFLEGEN = ("Auflegen", "hang up", "colgar", "挂断", "raccrocher", "telefonu kapatmak")
W_WEITERER = ("weiterer Job", "another job", "otro trabajo", "另一个作业", "autre tâche", "başka bir iş")
W_LAEUFT = ("läuft", "running", "en ejecución", "运行中", "en cours", "çalışıyor")


def k8sighup():
    """Terminal mit sleep 901 & ([1] 732, wörtlich aus dem Heft), Kernel, Shell bash, zwei Jobs (sleep 901 läuft, ein
    weiterer Job angehalten). Fenster zu (Kreuz), Kernel → Shell 1 SIGHUP; Shell → angehaltener Job 18 SIGCONT, dann
    an beide 1 SIGHUP; Shell und Jobs enden. Oben „Auflegen“ mit Telefonhörer."""
    s = Szene("linux/k8sighup", reihenfolge="anlegen")
    t = s.terminal(pos=(-3.45, 2.3), spalten=28, zeilen=3, groesse=17)
    kern = [flaeche(s, -0.6, 1.45, 0.6, 2.3, GRAU_HELL), L(s, "kernel", W_KERNEL, (0.0, 2.15), FM, "center", GRAU)]
    titel = hoerer(s, -0.95, 2.62) + [L(s, "aufl", W_AUFLEGEN, (-0.7, 2.62), FM, "left", DUNKEL)]
    sh = chip(s, (1.75, 1.85), "bash", b=0.85, h=0.36)
    l_sh = L(s, "shell", W_SHELL, (1.75, 2.2), FM, "center", GRAU)
    J1, J2 = (0.55, 0.3), (2.45, 0.3)
    j1 = chip(s, J1, "sleep 901", b=1.15, h=0.36)
    j2 = wchip(s, J2, "weiter", W_WEITERER, 1.55, h=0.36)
    l1 = L(s, "laeuft1", W_LAEUFT, (J1[0], -0.05), FM, "center", GRUEN)
    pz = pause_zeichen(s, 1.88, -0.05, ORANGE, 0.16)
    l2 = L(s, "angeh", W_ANGEH, (2.0, -0.05), FM, "left", ORANGE)
    verb = [linie(s, (1.75, 1.66), (J1[0], 0.49), HELLGRAU, 2), linie(s, (1.75, 1.66), (J2[0], 0.49), HELLGRAU, 2)]
    zu = [schleier(s, t.mitte, *t.groesse, 0.6), kreuz(s, t.mitte[0], t.mitte[1], 0.3)]
    p_k = pf(s, (-1.12, 1.85), (-0.66, 1.85), farbe=ORANGE, dicke=2.5, spitze=0.1)
    k_hup = chip(s, (0.0, 1.72), "1 SIGHUP", ORANGE, ORANGE_HELL, b=0.85)
    k_cont = chip(s, (1.75, 1.3), "18 SIGCONT", BLAU, BLAU_HELL, b=1.0)
    k_h1 = chip(s, (1.75, 1.3), "1 SIGHUP", ORANGE, ORANGE_HELL, b=0.85)
    k_h2 = chip(s, (1.75, 1.3), "1 SIGHUP", ORANGE, ORANGE_HELL, b=0.85)
    g_sh = [geist(s, (1.75, 1.85), 0.85, 0.36), schleier(s, (1.75, 1.85), 0.95, 0.46, 0.65)]
    g_j = [schleier(s, J1, 1.25, 0.46, 0.65), schleier(s, J2, 1.65, 0.46, 0.65)]
    schritt(s, EIN([t.id] + kern + sh + [l_sh] + verb + j1 + j2 + [l1, l2] + pz, 0.7))
    t.befehl("sleep 901 &", "[1] 732")
    s.pause(0.5)
    schritt(s, EIN(titel + zu, 0.7))
    schritt(s, ZEICHNE(p_k, 0.5), EIN(k_hup, 0.5))
    schritt(s, *VERS(k_hup, 0.85, 0.13, 0.8))
    s.pause(0.4)
    schritt(s, EIN(k_cont, 0.4))
    with s.gleichzeitig():
        schritt(s, *VERS(k_cont, J2[0] - 1.75, 0.75 - 1.3, 0.8))
    with s.gleichzeitig():
        schritt(s, AUS(pz, 0.5))
        s.ersetzen(l2, T(s, "laeuft2", *W_LAEUFT), farbe=GRUEN, dauer=0.5)
    schritt(s, AUS(k_cont, 0.3), EIN([k_h1, k_h2], 0.4))
    schritt(s, *VERS(k_h1, J1[0] - 1.75, 0.75 - 1.3, 0.8), *VERS(k_h2, J2[0] - 1.75, 0.75 - 1.3, 0.8))
    s.pause(0.3)
    with s.gleichzeitig():
        schritt(s, EIN(g_sh + g_j, 0.7))
        s.ersetzen(l1, T(s, "beendet1", *W_BEENDET), farbe=ROT, dauer=0.7)
        s.ersetzen(l2, T(s, "beendet2", *W_BEENDET), farbe=ROT, dauer=0.7)
    s.speichern()


W_JOBLISTE = ("Jobliste der Shell", "job list of the shell", "lista de trabajos de la shell", "Shell 的作业列表",
              "liste des tâches du shell", "kabuğun iş listesi")
W_GEWOEHNLICH = ("gewöhnlich", "ordinary", "normal", "普通", "ordinaire", "sıradan")
W_KEIN_SIGNAL = ("bekommt keines", "gets none", "no recibe ninguna", "收不到", "n'en reçoit aucun", "hiç almaz")
W_BZW_SYSTEMD = ("unter WSL; sonst meist systemd", "WSL; otherwise usually systemd", "WSL; si no, suele ser systemd",
                 "WSL 下；否则通常为 systemd", "WSL ; sinon souvent systemd", "WSL'de; yoksa genelde systemd")
W_NEUE_ELTERN = ("neuer Elternprozess", "new parent process", "nuevo proceso padre", "新的父进程", "nouveau processus parent",
                 "yeni üst süreç")


def k8nohup():
    """Shell im Fenster, Jobliste mit sleep 901 &, sleep 903 & (disown: gestrichen) und nohup sleep 902 (Reaktion auf
    SIGHUP: ignorieren). Fenster zu: SIGHUP an 901 (endet) und 902 (abgewiesen), 903 bekommt keines. Die Überlebenden
    hängen danach an /init (315), auf gewöhnlichem Linux meist systemd."""
    s = Szene("linux/k8nohup", reihenfolge="anlegen")
    t = s.terminal(pos=(-3.45, 2.45), spalten=34, zeilen=1, groesse=17, prompt=P8)
    sh = chip(s, (-2.4, 1.52), "bash", b=0.85, h=0.34)
    lb = [box(s, (0.35, 1.9), 1.9, 1.1, GRAU, WEISS, 1.5, "rect"), L(s, "jobliste", W_JOBLISTE, (0.35, 2.27), FM, "center", GRAU)]
    ry = (1.98, 1.72, 1.46)
    rz = [tx(s, z, (-0.45, y), TK, "left") for z, y in zip(("sleep 901 &", "sleep 903 &", "nohup sleep 902"), ry)]
    strich_ = linie(s, (-0.5, ry[1]), (0.47, ry[1]), ROT, 2.5)
    schl_r = schleier(s, (0.0, ry[1]), 1.05, 0.22, 0.55)
    J = {901: (-2.3, 0.35), 903: (0.0, 0.35), 902: (2.3, 0.35)}
    jc = {n: chip(s, J[n], "sleep %d" % n, b=1.1, h=0.34) for n in J}
    lin = {n: linie(s, (-2.4, 1.35), (J[n][0], 0.52), HELLGRAU, 2) for n in J}
    l901 = L(s, "gew", W_GEWOEHNLICH, (J[901][0], 0.0), FM, "center", GRAU)
    l903 = tx(s, "disown", (J[903][0], 0.0), TK, "center", GRAU)
    tab = [box(s, (J[902][0], -0.05), 2.1, 0.32, GRAU, WEISS, 1.5, "rect"), tx(s, "1 SIGHUP", (1.35, -0.05), TK, "left"),
           L(s, "ign", W_IGNOR, (2.2, -0.05), FM, "left", ORANGE)]
    zu = [schleier(s, t.mitte, *t.groesse, 0.6), kreuz(s, t.mitte[0], t.mitte[1], 0.25),
          geist(s, (-2.4, 1.52), 0.85, 0.34), schleier(s, (-2.4, 1.52), 0.95, 0.44, 0.65)]
    kh1 = chip(s, (-0.2, 1.15), "1 SIGHUP", ORANGE, ORANGE_HELL, b=0.85)
    kh2 = chip(s, (1.0, 1.15), "1 SIGHUP", ORANGE, ORANGE_HELL, b=0.85)
    g901 = [geist(s, J[901], 1.1, 0.34), schleier(s, J[901], 1.2, 0.44, 0.65)]
    l_ab = L(s, "abgew", W_ABGEWIESEN, (J[902][0], -0.38), FM, "center", ORANGE)
    l_kein = L(s, "kein", W_KEIN_SIGNAL, (J[903][0], -0.3), FM, "center", GRAU)
    eltern = [L(s, "neueltern", W_NEUE_ELTERN, (3.4, 2.78), FM, "right", GRAU),
              chip(s, (2.75, 2.15), "/init (315)", GRUEN, GRUEN_HELL, b=1.1, h=0.34),
              L(s, "bzw", W_BZW_SYSTEMD, (3.4, 2.52), FM, "right", GRAU)]
    neu = [linie(s, (2.45, 1.98), (J[903][0] + 0.2, 0.52), GRUEN, 2.5), linie(s, (3.0, 1.98), (J[902][0] + 0.48, 0.52), GRUEN, 2.5)]
    schritt(s, EIN([t.id] + sh + lb, 0.7))
    s.pause(0.3)
    schritt(s, EIN([rz[0], lin[901], l901] + jc[901], 0.5))
    schritt(s, EIN([rz[1], lin[903]] + jc[903], 0.5))
    schritt(s, ZEICHNE(strich_, 0.4), EIN([schl_r, l903], 0.5))
    schritt(s, EIN([rz[2], lin[902]] + jc[902] + tab, 0.5))
    s.pause(0.6)
    schritt(s, EIN(zu, 0.7))
    schritt(s, EIN([kh1, kh2], 0.4))
    schritt(s, *VERS(kh1, J[901][0] + 0.2, 0.82 - 1.15, 0.8), *VERS(kh2, J[902][0] - 1.0, 0.82 - 1.15, 0.8))
    with s.gleichzeitig():
        schritt(s, AUS(jc[901], 0.6), EIN(g901, 0.6))
        s.ersetzen(l901, T(s, "beendet", *W_BEENDET), farbe=ROT, dauer=0.6)
    schritt(s, *VERS(kh2, 0, -0.1, 0.25))
    schritt(s, *VERS(kh2, 0, 0.1, 0.3), BETONE(tab[2], 0.6), EIN(l_ab, 0.5))
    schritt(s, EIN(l_kein, 0.5))
    s.pause(0.5)
    schritt(s, AUS([lin[901], lin[903], lin[902]], 0.6), EIN(flach(eltern), 0.6))
    schritt(s, ZEICHNE(neu, 0.8))
    s.speichern()


# ================================================================== Abschnitt 6: Last und Priorität
W_LAST = ("Last", "load", "carga", "负载", "charge", "yük")
W_TMIN = ("Zeit in min", "time in min", "tiempo en min", "时间（分钟）", "temps en min", "zaman (dk)")
W_W1 = ("1-Minuten-Wert", "1-minute value", "valor de 1 minuto", "1 分钟值", "valeur sur 1 min", "1 dakikalık değer")
W_W5 = ("5-Minuten-Wert", "5-minute value", "valor de 5 minutos", "5 分钟值", "valeur sur 5 min", "5 dakikalık değer")
W_W15 = ("15-Minuten-Wert", "15-minute value", "valor de 15 minutos", "15 分钟值", "valeur sur 15 min", "15 dakikalık değer")
W_RECHNEND = ("rechnende Prozesse", "running processes", "procesos que calculan", "正在运行的进程", "processus qui calculent",
              "çalışan süreçler")
W_KERNE = ("14 Kerne: Linie bei 14, weit oben", "14 cores: line at 14, far above", "14 núcleos: línea en 14, muy arriba",
           "14 个核心：14 处的线远在上方", "14 cœurs : ligne à 14, bien plus haut", "14 çekirdek: 14'teki çizgi çok yukarıda")
W_160 = ("1,60", "1.60", "1,60", "1.60", "1,60", "1,60")
W_254 = ("2,54", "2.54", "2,54", "2.54", "2,54", "2,54")


def k8last():
    """Diagramm 0–4 min, Last 0–4: graue Treppe (vier Prozesse 60 s lang). Parameter tz läuft; die Kurven
    L = 4(1 − e^(−t/τ)) bis 1 min, danach Abklingen, für τ = 1, 5, 15 min wachsen mit. Bei 30 s und 61 s leuchten die
    Messpunkte 1,60 und 2,54 auf der 1-Minuten-Kurve. Oben angedeutet: die Linie der 14 Kerne liegt weit darüber."""
    s = Szene("linux/k8last", reihenfolge="anlegen")
    s.welt()
    a = s.achsen((0, 4, 1), (0, 4, 1), breite=4.4, hoehe=2.4, mitte=(-0.75, 0.9), xl=T(s, "tmin", *W_TMIN),
                 yl=T(s, "last", *W_LAST))
    treppe = s.daten(a, [(0, 0), (0, 4), (1, 4), (1, 0), (4, 0)], farbe=HELLGRAU, dicke=4)
    s.parameter("tz", 0)
    t61 = round(61 / 60, 4)
    stuecke = ((0, 0.5), (0.5, t61), (t61, 4))       # Kurven stückweise zeichnen: kleine Datei, Zeiger läuft mit
    kurven = [[], [], []]
    for tau, f in ((1, BLAU), (5, GRUEN), (15, ORANGE)):
        for k, (x0, x1) in enumerate(stuecke):
            kurven[k].append(s.kurve(a, "4*(1-exp(-min(x,1)/%d))*exp(-max(x-1,0)/%d)" % (tau, tau), x=(x0, x1), farbe=f,
                                     dicke=4, punkte=25 if k < 2 else 61))
    zeiger = s.linie(a, ("tz", 0), ("tz", 4), farbe=DUNKEL, dicke=1.5, dash=DASH)
    leg = []
    for i, (w, f, key) in enumerate(((W_W1, BLAU, "w1"), (W_W5, GRUEN, "w5"), (W_W15, ORANGE, "w15"),
                                     (W_RECHNEND, HELLGRAU, "rech"))):
        y = r4(1.95 - 0.3 * i)
        leg += [linie(s, (1.75, y), (2.05, y), f, 4), L(s, key, w, (2.13, y), FM, "left")]
    kerne = [pf(s, (1.05, 1.68), (1.05, 2.25), farbe=ROT, dicke=2, spitze=0.09),
             L(s, "kerne", W_KERNE, (0.95, 2.4), FM, "right", ROT)]
    p1 = s.kreis(None, -2.4, 0.66, 0.065, farbe=BLAU, dicke=2.5, fuellung=WEISS, deckung=1.0)       # (30 s, 1,60)
    p2 = s.kreis(None, -1.8317, 1.224, 0.065, farbe=BLAU, dicke=2.5, fuellung=WEISS, deckung=1.0)   # (61 s, 2,54)
    l1 = L(s, "m160", W_160, (-2.47, 0.72), FM, "right", BLAU)
    l2 = L(s, "m254", W_254, (-1.72, 1.36), FM, "left", BLAU)
    schritt(s, EIN([a, treppe, zeiger] + leg + kerne, 0.7))
    s.pause(0.5)
    for k, (ziel, d) in enumerate(((0.5, 1.2), (t61, 1.0), (4, 3.0))):
        with s.gleichzeitig():
            s.verstellen("tz", ziel, dauer=d)
            schritt(s, ZEICHNE(kurven[k], d))
        if k == 0:
            schritt(s, EIN([p1, l1], 0.4), BETONE(p1, 0.6))
        elif k == 1:
            schritt(s, EIN([p2, l2], 0.4), BETONE(p2, 0.6))
            s.pause(0.4)
    s.speichern()


W_GEMESSEN_160 = ("gemessen: 1,60", "measured: 1.60", "medido: 1,60", "实测：1.60", "mesuré : 1,60", "ölçülen: 1,60")
W_GEMESSEN_254 = ("gemessen: 2,54", "measured: 2.54", "medido: 2,54", "实测：2.54", "mesuré : 2,54", "ölçülen: 2,54")


def k8lastrechnung():
    """Rechenbild in zwei Blöcken, Zeile für Zeile: L(30 s) = 4·(1 − e^(−30/60)) = 4·(1 − 0,607) = 4·0,393 = 1,57 und
    L(60 s) = 4·(1 − e^(−1)) = 4·(1 − 0,368) = 4·0,632 = 2,53; daneben die gemessenen Werte 1,60 und 2,54."""
    s = Szene("linux/k8lastrechnung", reihenfolge="anlegen")
    t1 = (r"\begin{aligned} L(30\,\mathrm{s}) &= 4 \cdot \left(1 - \mathrm{e}^{-30/60}\right)\\ &= 4 \cdot (1 - 0.607)\\"
          r" &= 4 \cdot 0.393\\ &= 1.57 \end{aligned}")
    t2 = (r"\begin{aligned} L(60\,\mathrm{s}) &= 4 \cdot \left(1 - \mathrm{e}^{-1}\right)\\ &= 4 \cdot (1 - 0.368)\\"
          r" &= 4 \cdot 0.632\\ &= 2.53 \end{aligned}")
    m1 = L(s, "g160", W_GEMESSEN_160, (0.75, 0.88), FK, "left", BLAU)
    m2 = L(s, "g254", W_GEMESSEN_254, (0.75, -0.72), FK, "left", BLAU)
    s.formel(t1, mitte=(-1.0, 1.35), hoehe=1.15, zeilenweise=True, dauer=4.0)
    schritt(s, EIN(m1, 0.5))
    s.pause(0.6)
    s.formel(t2, mitte=(-1.0, -0.25), hoehe=1.15, zeilenweise=True, dauer=4.0)
    schritt(s, EIN(m2, 0.5))
    s.speichern()


W_ANTEIL0 = ("Anteil bei Nice 0:", "share at nice 0:", "parte con nice 0:", "nice 0 的份额：", "part avec nice 0 :",
             "nice 0 payı:")
W_ANTEIL10 = ("Anteil bei Nice 10:", "share at nice 10:", "parte con nice 10:", "nice 10 的份额：", "part avec nice 10 :",
              "nice 10 payı:")
W_BALKEN0 = ("90,3 % (gemessen 90,1)", "90.3 % (measured 90.1)", "90,3 % (medido 90,1)", "90.3 %（实测 90.1）",
             "90,3 % (mesuré 90,1)", "%90,3 (ölçülen 90,1)")
W_BALKEN10 = ("9,7 % (gemessen 9,6)", "9.7 % (measured 9.6)", "9,7 % (medido 9,6)", "9.7 %（实测 9.6）",
              "9,7 % (mesuré 9,6)", "%9,7 (ölçülen 9,6)")


def k8niceanteil():
    """Rechenbild: 1,25^10 ≈ 9,31 ≈ 1024/110; Anteil Nice 0 = 1024/(1024 + 110) = 1024/1134 = 0,903 = 90,3 %;
    Anteil Nice 10 = 110/1134 = 0,097 = 9,7 %. Darunter zwei Balken, die auf 90,3 und 9,7 % wachsen, daneben die
    gemessenen Werte 90,1 und 9,6."""
    s = Szene("linux/k8niceanteil", reihenfolge="anlegen")
    f0 = s.formel(r"1.25^{10} \approx 9.31 \approx 1024/110", mitte=(0.17, 2.05), hoehe=0.3)
    la = L(s, "a0", W_ANTEIL0, (-3.4, 1.5), FM, "left", DUNKEL)
    f1 = s.formel(r"1024/(1024 + 110) = 1024/1134 = 0.903", mitte=(0.95, 1.5), hoehe=0.25)
    lb = L(s, "a10", W_ANTEIL10, (-3.4, 1.0), FM, "left", DUNKEL)
    f2 = s.formel(r"110/1134 = 0.097", mitte=(-0.06, 1.0), hoehe=0.25)
    X0, LEN = -1.6, 3.0
    zeilen = []
    for i, (name, ant, w, key) in enumerate((("Nice 0", 0.903, W_BALKEN0, "b0"), ("Nice 10", 0.097, W_BALKEN10, "b10"))):
        y = r4(0.35 - 0.45 * i)
        zeilen.append(([linie(s, (X0, y), (X0 + LEN, y), "#e6e6e6", 14), text(s, name, (X0 - 0.12, y), FM, "right", DUNKEL)],
                       linie(s, (X0, y), (r4(X0 + LEN * ant), y), BLAU if i == 0 else ORANGE, 14),
                       L(s, key, w, (X0 + LEN + 0.12, y), FM, "left")))
    schritt(s, EIN(f0, 0.8))
    s.pause(0.6)
    schritt(s, EIN([la, f1], 0.8))
    s.pause(0.5)
    schritt(s, EIN([lb, f2], 0.8))
    s.pause(0.6)
    schritt(s, EIN(zeilen[0][0] + zeilen[1][0], 0.5))
    schritt(s, ZEICHNE([zeilen[0][1], zeilen[1][1]], 1.2))
    schritt(s, EIN([zeilen[0][2], zeilen[1][2]], 0.5))
    s.speichern()


# ================================================================== Abschnitt 7: Dienste und systemd
W_IM_TERMINAL = ("im Terminal gestartet", "started in a terminal", "iniciado en un terminal", "在终端中启动",
                 "lancé dans un terminal", "terminalde başlatıldı")
W_DIENST = ("Dienst", "service", "servicio", "服务", "service", "hizmet")
W_ZEILEN_DIENST = [("Elternprozess", "parent process", "proceso padre", "父进程", "processus parent", "üst süreç"),
                   ("Terminal", "terminal", "terminal", "终端", "terminal", "terminal"),
                   ("Besitzer", "owner", "propietario", "所有者", "propriétaire", "sahip"),
                   ("Eingabe", "input", "entrada", "输入", "entrée", "girdi"),
                   ("Ausgabe", "output", "salida", "输出", "sortie", "çıktı")]
W_BILDSCHIRM = ("Bildschirm", "screen", "pantalla", "屏幕", "écran", "ekran")
W_PROTOKOLL = ("Protokoll", "log", "registro", "日志", "journal", "günlük")
W_WEITERER_DIENST = ("weiterer Dienst", "another service", "otro servicio", "另一个服务", "autre service", "başka bir hizmet")
W_EIGENER_BEN = ("eigener Benutzer:", "own user:", "usuario propio:", "专用用户：", "utilisateur propre :", "kendi kullanıcısı:")


def k8dienst():
    """Vergleichstabelle sleep 600 (PID 596, im Terminal gestartet) gegen cron (PID 160, Dienst): Elternprozess
    bash (587) / systemd (1), Terminal pts/3 / ?, Besitzer student / root, Eingabe Tastatur / /dev/null, Ausgabe
    Bildschirm / Protokoll. Darunter systemd-resolved mit eigenem Benutzer systemd-resolve. Die Unterschiede leuchten
    nacheinander auf (Elternprozess, Terminal, Besitzer, Ein- und Ausgabe)."""
    s = Szene("linux/k8dienst", reihenfolge="anlegen")
    X1, X2, XL = -0.55, 2.15, -3.4
    kopf = [L(s, "imterm", W_IM_TERMINAL, (X1, 2.4), FM, "center", GRAU), L(s, "dienst", W_DIENST, (X2, 2.4), FM, "center", GRAU)]
    kopf += chip(s, (X1, 2.08), "sleep 600", b=1.15, h=0.34) + chip(s, (X2, 2.08), "cron", b=0.8, h=0.34)
    ys = [1.7, 1.4, 1.1, 0.8, 0.5, 0.2]
    pid = [tx(s, "PID", (XL, ys[0]), TK, "left", GRAU), tx(s, "596", (X1, ys[0]), TK), tx(s, "160", (X2, ys[0]), TK)]
    werte = [("bash (587)", "systemd (1)"), ("pts/3", "?"), ("student", "root"), (W_TASTATUR, "/dev/null"),
             (W_BILDSCHIRM, W_PROTOKOLL)]
    zeilen = []
    for i, (w, (a, b)) in enumerate(zip(W_ZEILEN_DIENST, werte)):
        y = ys[i + 1]
        za = tx(s, a, (X1, y), TK) if isinstance(a, str) else L(s, "a%d" % i, a, (X1, y), FM)
        zb = tx(s, b, (X2, y), TK) if isinstance(b, str) else L(s, "b%d" % i, b, (X2, y), FM)
        zeilen.append([L(s, "z%d" % i, w, (XL, y), FM, "left", DUNKEL), za, zb])
    trenn = [linie(s, (XL, 1.88), (3.4, 1.88), HELLGRAU, 1.5), linie(s, (XL, 0.02), (3.4, 0.02), HELLGRAU, 1.5)]
    band = [box(s, (r4((-1.75 + 3.4) / 2), ys[1]), 5.15, 0.27, ORANGE, ORANGE, 0, "rect", deckung=0.2),
            box(s, (r4((-1.75 + 3.4) / 2), ys[2]), 5.15, 0.27, ORANGE, ORANGE, 0, "rect", deckung=0.2),
            box(s, (r4((-1.75 + 3.4) / 2), ys[3]), 5.15, 0.27, ORANGE, ORANGE, 0, "rect", deckung=0.2),
            box(s, (r4((-1.75 + 3.4) / 2), (ys[4] + ys[5]) / 2), 5.15, 0.57, ORANGE, ORANGE, 0, "rect", deckung=0.2)]
    resolved = [L(s, "weiter", W_WEITERER_DIENST, (XL, -0.3), FM, "left", DUNKEL)]
    resolved += chip(s, (X1, -0.3), "systemd-resolved", b=1.5, h=0.32)
    resolved += [L(s, "eigben", W_EIGENER_BEN, (X2, -0.17), FM, "center", GRAU), tx(s, "systemd-resolve", (X2, -0.43), TK)]
    schritt(s, EIN(kopf + pid + trenn + flach(zeilen), 0.7))
    s.pause(0.6)
    gruppen = [zeilen[0], zeilen[1], zeilen[2], zeilen[3] + zeilen[4]]
    vorher = None
    for k, g in enumerate(gruppen):
        teile_k = [EIN(band[k], 0.5), BETONE(g[1:3] + (g[4:6] if k == 3 else []), 0.8)]
        if vorher is not None:
            teile_k.append(AUS(vorher, 0.4))
        schritt(s, *teile_k)
        if k == 2:
            schritt(s, EIN(resolved, 0.6))
        s.pause(0.5)
        vorher = band[k]
    schritt(s, AUS(vorher, 0.4))
    s.speichern()


UNIT_CRON = ["[Unit]", "Description=Regular background program processing daemon", "Documentation=man:cron(8)",
             "After=remote-fs.target nss-user-lookup.target", "", "[Service]", "EnvironmentFile=-/etc/default/cron",
             "ExecStart=/usr/sbin/cron -f -P $EXTRA_OPTS", "IgnoreSIGPIPE=false", "KillMode=process", "Restart=on-failure",
             "SyslogFacility=cron", "", "[Install]", "WantedBy=multi-user.target"]
W_ROLLE = [("was ist das, und nach wem\nstarte ich", "what is this, and after\nwhat do I start",
            "qué es esto y después de\nqué arranco", "这是什么，\n我在谁之后启动", "qu'est-ce que c'est, et après\nquoi je démarre",
            "bu nedir ve neyin\nardından başlarım"),
           ("welches Programm, und was tun,\nwenn es endet", "which program, and what to do\nwhen it ends",
            "qué programa y qué hacer\ncuando termina", "运行哪个程序，\n结束时怎么办", "quel programme, et que faire\nquand il se termine",
            "hangi program ve bittiğinde\nne yapılacak"),
           ("zu welchem Zustand des Systems\ngehöre ich", "which state of the system\ndo I belong to",
            "a qué estado del sistema\npertenezco", "我属于系统的\n哪个状态", "à quel état du système\nj'appartiens",
            "sistemin hangi durumuna\naitim")]


def k8unitdatei():
    """Unit-Datei von cron als Datei-Ansicht (hell, wörtlich aus systemctl cat). [Unit], [Service], [Install] leuchten
    nacheinander, rechts daneben ihre Rolle. Dann Pfeile: ExecStart= → Prozess /usr/sbin/cron -f -P (PID 160),
    WantedBy= → Kasten multi-user.target."""
    s = Szene("linux/k8unitdatei", reihenfolge="anlegen")
    d = s.datei("/usr/lib/systemd/system/cron.service", "\n".join(UNIT_CRON), pos=(-3.45, 2.45), groesse=17)
    bloecke = [(0, 3), (5, 11), (13, 14)]
    marken, rollen = [], []
    xr = 1.12
    for k, (z0, z1) in enumerate(bloecke):
        breit = max(len(UNIT_CRON[z]) for z in range(z0, z1 + 1)) - 1
        marken.append(d.markieren(z0, 0, breit, ORANGE, 0.22, bis=z1))
        y = d.y(z0) if k == 2 else r4((d.y(z0) + d.y(z0 + 2)) / 2)
        rollen.append([tx(s, UNIT_CRON[z0], (xr, r4(y + 0.2)), TK, "left", ORANGE),
                       L(s, "rolle%d" % k, W_ROLLE[k], (xr, r4(y - 0.1)), FM, "left")])
    a, b = d.finde(7, "/usr/sbin/cron -f -P")
    r_exec = d.markieren(7, 0, len(UNIT_CRON[7]) - 1, BLAU, 0.2)
    proz = chip(s, (2.3, d.y(9)), "/usr/sbin/cron -f -P", b=1.75, h=0.32) + [tx(s, "PID 160", (2.3, r4(d.y(9) - 0.27)), TK,
                                                                                "center", GRAU)]
    p_exec = pf(s, (d.xr(len(UNIT_CRON[7]) - 1) + 0.06, d.y(7)), (1.4, d.y(9)), farbe=BLAU, dicke=2.5, spitze=0.1)
    a2, b2 = d.finde(14, "multi-user.target")
    r_want = d.markieren(14, 0, len(UNIT_CRON[14]) - 1, BLAU, 0.2)
    ziel_y = r4(d.unten_kante - 0.38)
    ziel = chip(s, (d.xm(a2, b2), ziel_y), "multi-user.target", GRUEN, GRUEN_HELL, b=1.55, h=0.32)
    p_want = pf(s, d.anker(14, a2, b2, "unten"), (d.xm(a2, b2), r4(ziel_y + 0.17)), farbe=BLAU, dicke=2.5, spitze=0.1)
    schritt(s, EIN(d.id, 0.7))
    s.pause(0.5)
    vorher = None
    for k in range(3):
        teile_k = [EIN([marken[k]] + rollen[k], 0.6)]
        if vorher is not None:
            teile_k.append(AUS(vorher, 0.4))
        schritt(s, *teile_k)
        s.pause(0.6)
        vorher = marken[k]
    schritt(s, AUS(vorher, 0.4), EIN(r_exec, 0.5))
    schritt(s, ZEICHNE(p_exec, 0.6), EIN(proz, 0.6))
    s.pause(0.4)
    schritt(s, EIN(r_want, 0.5))
    schritt(s, ZEICHNE(p_want, 0.5), EIN(ziel, 0.6))
    s.speichern()


W_KIND_KILL = ("Kind beendet: SIGKILL", "child ended: SIGKILL", "hijo terminado: SIGKILL", "子进程结束：SIGKILL",
               "enfant terminé : SIGKILL", "alt süreç bitti: SIGKILL")
W_KIND_TERM = ("SIGTERM: gewolltes Ende", "SIGTERM: intended end", "SIGTERM: fin deseado", "SIGTERM：有意结束",
               "SIGTERM : fin voulue", "SIGTERM: istenen son")
W_NEUSTARTS0 = ("Neustarts: 0", "restarts: 0", "reinicios: 0", "重启次数：0", "redémarrages : 0", "yeniden başlatma: 0")
W_NEUSTARTS1 = ("Neustarts: 1", "restarts: 1", "reinicios: 1", "重启次数：1", "redémarrages : 1", "yeniden başlatma: 1")
W_BLEIBT_AUS = ("Dienst bleibt aus", "service stays off", "el servicio queda parado", "服务保持停止",
                "le service reste arrêté", "hizmet kapalı kalır")
W_GREIFT_NICHT = ("greift nicht", "does not apply", "no se aplica", "不适用", "ne s'applique pas", "uygulanmaz")


def k8neustart():
    """systemd --user (383) oben, Regel Restart=on-failure und Zähler Neustarts. Im Dienst k8eieruhr: sleep 600 (829).
    9 SIGKILL trifft 829 → Pfeil „Kind beendet: SIGKILL“ zu systemd, Regel leuchtet, Zähler 1, neuer Prozess 833.
    15 SIGTERM trifft 833 → „SIGTERM: gewolltes Ende“, Regel greift nicht, der Dienst bleibt aus."""
    s = Szene("linux/k8neustart", reihenfolge="anlegen")
    sysd = chip(s, (-1.55, 2.1), "systemd --user", b=1.35, h=0.36) + [tx(s, "PID 383", (-0.75, 2.1), TK, "left", GRAU)]
    regel = chip(s, (2.25, 2.1), "Restart=on-failure", GRAU, WEISS, b=1.6, h=0.34)
    zaehler = L(s, "n0", W_NEUSTARTS0, (2.25, 1.74), FM, "center", DUNKEL)
    rahmen_d = [box(s, (0.0, 0.55), 5.7, 1.1, GRAU, WEISS, 1.5, dash=DASH), tx(s, "k8eieruhr.service", (-2.7, 0.94), TK, "left", GRAU)]
    A, B = (-1.3, 0.42), (1.2, 0.42)
    pa = chip(s, A, "sleep 600", b=1.1, h=0.34) + [tx(s, "PID 829", (-0.65, A[1]), TK, "left", GRAU)]
    pb = chip(s, B, "sleep 600", GRUEN, GRUEN_HELL, b=1.1, h=0.34) + [tx(s, "PID 833", (1.85, B[1]), TK, "left", GRAU)]
    kk = chip(s, (A[0], -0.55), "9 SIGKILL", ROT, ROT_HELL, b=0.92)
    kt = chip(s, (B[0], -0.55), "15 SIGTERM", ORANGE, ORANGE_HELL, b=1.0)
    ga = [schleier(s, A, 1.2, 0.44, 0.65), geist(s, A, 1.1, 0.34)]
    gb = [schleier(s, B, 1.2, 0.44, 0.65), geist(s, B, 1.1, 0.34)]
    pfa = [pf(s, (A[0], 0.62), (-1.55, 1.9), farbe=ROT, dicke=2.5, spitze=0.1),
           L(s, "kindkill", W_KIND_KILL, (-1.55, 1.3), FM, "right", ROT)]
    p_neu = pf(s, (1.75, 1.6), (1.35, 0.62), farbe=GRUEN, dicke=2.5, spitze=0.1)
    pfb = [pf(s, (0.85, 0.62), (-0.8, 1.9), farbe=ORANGE, dicke=2.5, spitze=0.1),
           L(s, "kindterm", W_KIND_TERM, (-0.02, 1.47), FM, "left", ORANGE)]
    kz = kreuz(s, 3.2, 2.1, 0.16, GRAU)
    l_gn = L(s, "greift", W_GREIFT_NICHT, (2.75, 1.42), FM, "center", GRAU)
    l_aus = L(s, "aus", W_BLEIBT_AUS, (2.6, -0.55), FM, "center", GRAU)
    schritt(s, EIN(sysd + regel + [zaehler] + rahmen_d + pa, 0.7))
    s.pause(0.5)
    schritt(s, EIN(kk, 0.4))
    schritt(s, *VERS(kk, 0, 0.55, 0.5))
    schritt(s, EIN(ga, 0.4))
    schritt(s, ZEICHNE(pfa[0], 0.7), EIN(pfa[1], 0.7))
    with s.gleichzeitig():
        schritt(s, BETONE(regel, 0.8))
        s.ersetzen(zaehler, T(s, "n1", *W_NEUSTARTS1), farbe=GRUEN, dauer=0.8)
    schritt(s, ZEICHNE(p_neu, 0.5), WACHS(pb[:2], 0.6), EIN(pb[2], 0.6))
    s.pause(0.6)
    schritt(s, EIN(kt, 0.4))
    schritt(s, *VERS(kt, 0, 0.55, 0.5))
    schritt(s, EIN(gb, 0.4))
    schritt(s, ZEICHNE(pfb[0], 0.7), EIN(pfb[1], 0.7))
    schritt(s, EIN([kz, l_gn], 0.5))
    schritt(s, EIN(l_aus, 0.5))
    s.speichern()


W_JETZT = ("jetzt", "now", "ahora", "现在", "maintenant", "şimdi")
W_NAECHSTER_START = ("beim nächsten Start", "at the next start", "en el próximo arranque", "下次启动时", "au prochain démarrage",
                     "bir sonraki başlangıçta")
W_AUS_INACTIVE = ("aus (inactive)", "off (inactive)", "parado (inactive)", "停止（inactive）", "arrêté (inactive)",
                  "kapalı (inactive)")
W_LAEUFT_ACTIVE = ("läuft (active)", "running (active)", "en marcha (active)", "运行中（active）", "en marche (active)",
                   "çalışıyor (active)")
W_LINK = ("Link", "link", "enlace", "链接", "lien", "bağlantı")
W_ZEITSPRUNG = ("Zeitsprung: nächste Anmeldung", "time jump: next login", "salto en el tiempo: próximo inicio de sesión",
                "时间跳转：下次登录", "saut dans le temps : prochaine connexion", "zaman atlaması: bir sonraki oturum açma")
W_ERREICHT = ("erreicht default.target", "reaches default.target", "alcanza default.target", "到达 default.target",
              "atteint default.target", "default.target'a ulaşır")


def schalter(s, x, y):
    """Schalter (aus): Spur, grüne Spur (für „an“, zunächst unsichtbar), Knopf. Ergebnis (spur, gruen, knopf)."""
    spur = box(s, (x, y), 0.62, 0.3, GRAU, GRAU_HELL, 2)
    gruen = box(s, (x, y), 0.62, 0.3, GRUEN, GRUEN, 2)
    knopf = s.kreis(None, r4(x - 0.15), y, 0.11, farbe=GRAU, dicke=2, fuellung=WEISS, deckung=1.0)
    return spur, gruen, knopf


def k8enable():
    """Zwei Schalter: „jetzt“ (start/stop) und „beim nächsten Start“ (enable/disable). enable legt in
    default.target.wants einen Link auf k8eieruhr.service an, der Dienst bleibt aus. Zeitsprung „nächste Anmeldung“:
    systemd --user erreicht default.target, folgt dem Link, startet den Dienst. disable entfernt den Link."""
    s = Szene("linux/k8enable", reihenfolge="anlegen")
    XJ, XN = -1.9, 1.5
    kopf = [L(s, "jetzt", W_JETZT, (XJ, 2.42), FM, "center", DUNKEL),
            L(s, "naechster", W_NAECHSTER_START, (XN, 2.42), FM, "center", DUNKEL),
            tx(s, "start / stop", (XJ, 1.72), TK, "center", GRAU), tx(s, "enable / disable", (XN, 1.72), TK, "center", GRAU)]
    sj, gj, kj = schalter(s, XJ, 2.05)
    sn, gn, kn = schalter(s, XN, 2.05)
    dienst = chip(s, (XJ, 0.85), "k8eieruhr.service", b=1.55, h=0.34)
    zustand = L(s, "zust", W_AUS_INACTIVE, (XJ, 0.5), FM, "center", GRAU)
    ordner = [box(s, (XN, 0.75), 2.6, 0.8, GRAU, WEISS, 1.5, "rect"), ordner_symbol(s, XN - 1.08, 1.0),
              tx(s, "default.target.wants/", (r4(XN - 0.9), 1.0), TK, "left")]
    eintrag = tx(s, "k8eieruhr.service", (r4(XN - 0.9), 0.62), TK, "left", BLAU)
    link = [pf(s, (r4(XN - 0.98), 0.62), (r4(XJ + 0.82), 0.78), farbe=BLAU, dicke=2, dash=DASH, spitze=0.09),
            L(s, "link", W_LINK, (-0.3, 0.88), FM, "center", BLAU)]
    sprung = [L(s, "sprung", W_ZEITSPRUNG, (-3.4, -0.35), FM, "left", ORANGE)]
    sysd = chip(s, (XN, -0.35), "systemd --user", b=1.35, h=0.34)
    l_err = L(s, "erreicht", W_ERREICHT, (XN, -0.7), FM, "center", GRAU)
    p_sys = pf(s, (XN, -0.17), (XN, 0.33), farbe=DUNKEL, dicke=2.5, spitze=0.1)
    schritt(s, EIN(kopf + [sj, kj, sn, kn] + dienst + [zustand] + ordner, 0.7))
    s.pause(0.5)
    schritt(s, EIN(gn, 0.5), VER(kn, 0.3, 0, 0.5))
    schritt(s, EIN(eintrag, 0.5), ZEICHNE(link[0], 0.6), EIN(link[1], 0.6))
    schritt(s, BETONE(zustand, 0.7))
    s.pause(0.6)
    schritt(s, EIN(sprung + sysd + [l_err], 0.7))
    schritt(s, ZEICHNE(p_sys, 0.5), BETONE(eintrag, 0.6))
    with s.gleichzeitig():
        schritt(s, BETONE(link[0], 0.6), EIN(gj, 0.6), VER(kj, 0.3, 0, 0.6))
        s.ersetzen(zustand, T(s, "laeuft", *W_LAEUFT_ACTIVE), farbe=GRUEN, dauer=0.6)
    s.pause(0.6)
    schritt(s, AUS([gn, eintrag] + link, 0.6), VER(kn, -0.3, 0, 0.6))
    s.speichern()


# ================================================================== Abschnitt 8: Protokolle
W_QUELLEN = ("Quellen", "sources", "fuentes", "来源", "sources", "kaynaklar")
W_ZEIT_RECHNER = ("Zeit · Rechner", "time · host", "hora · equipo", "时间 · 主机", "heure · machine", "zaman · makine")
W_PROG_UNIT = ("Programm[PID] · Unit", "program[PID] · unit", "programa[PID] · unit", "程序[PID] · unit",
               "programme[PID] · unit", "program[PID] · unit")
W_ABLAGEN = ("Ablagen", "stores", "almacenes", "存储", "stockages", "depolar")
W_SYSTEM = ("System", "system", "sistema", "系统", "système", "sistem")
W_BEN1000 = ("Benutzer 1000", "user 1000", "usuario 1000", "用户 1000", "utilisateur 1000", "kullanıcı 1000")
W_FILTER = ("Filter", "filters", "filtros", "过滤器", "filtres", "filtreler")
W_KOPIE = ("Kopie", "copy", "copia", "副本", "copie", "kopya")


def k8journal():
    """Quellen (Kernel, cron, k8eieruhr, systemd) → systemd-journald mit Zettel (Zeit, Rechner, Programm[PID], Unit) →
    Ablagen System und Benutzer 1000 → Filter -u, -b, -n → journalctl; nur der passende Zettel kommt durch.
    Seitenpfeil: journald → rsyslogd → /var/log/syslog und /var/log/auth.log."""
    s = Szene("linux/k8journal", reihenfolge="anlegen")
    XQ, XJ, XA, XF, XC = -2.75, -0.55, 1.05, 2.2, 3.0
    ys = (2.0, 1.6, 1.2, 0.8)
    quellen = [L(s, "quellen", W_QUELLEN, (XQ, 2.42), FM, "center", GRAU)]
    quellen += wchip(s, (XQ, ys[0]), "kernel", W_KERNEL, 1.1, GRAU, GRAU_HELL, h=0.32)
    for name, y in zip(("cron", "k8eieruhr", "systemd"), ys[1:]):
        quellen += chip(s, (XQ, y), name, b=1.1, h=0.32)
    jd = chip(s, (XJ, 1.4), "systemd-journald", DUNKEL, WEISS, b=1.45, h=0.4)
    pq = [pf(s, (XQ + 0.6, y), (XJ - 0.78, r4(1.4 + (y - 1.4) * 0.3)), farbe=GRAU, dicke=2, spitze=0.08) for y in ys]
    zettel = [box(s, (XJ, 2.22), 1.6, 0.5, GRAU, GELB, 1.5, "rect"), L(s, "zr", W_ZEIT_RECHNER, (XJ, 2.33), FM),
              L(s, "pu", W_PROG_UNIT, (XJ, 2.11), FM), linie(s, (XJ, 1.97), (XJ, 1.6), GRAU, 1.5, DASH)]
    ablagen = [L(s, "ablagen", W_ABLAGEN, (XA, 2.42), FM, "center", GRAU),
               box(s, (XA, 1.85), 1.2, 0.5, DUNKEL, GRAU_HELL, 2, "rect"), L(s, "sys", W_SYSTEM, (XA, 1.85), FM),
               box(s, (XA, 1.0), 1.2, 0.5, DUNKEL, GRAU_HELL, 2, "rect"), L(s, "ben", W_BEN1000, (XA, 1.0), FM)]
    pa = [pf(s, (XJ + 0.75, 1.48), (XA - 0.62, 1.8), farbe=GRAU, dicke=2, spitze=0.08),
          pf(s, (XJ + 0.75, 1.32), (XA - 0.62, 1.05), farbe=GRAU, dicke=2, spitze=0.08)]
    filt = [L(s, "filter", W_FILTER, (XF, 2.42), FM, "center", GRAU), box(s, (XF, 1.4), 0.5, 1.2, GRAU, WEISS, 1.5, "rect")]
    for f, y in (("-u", 1.75), ("-b", 1.4), ("-n", 1.05)):
        filt.append(tx(s, f, (XF, y), TK, "center", BLAU))
    jc = chip(s, (XC, 1.4), "journalctl", BLAU, BLAU_HELL, b=0.9, h=0.36)
    # Zettel unterwegs: je Quelle einer, danach zwei in die Ablagen, dann durch die Filter
    unterwegs = [marke(s, XQ + 0.68, y, ORANGE, 0.2, 0.14) for y in ys]
    z_sys = marke(s, XJ, 1.4, ORANGE, 0.2, 0.14)
    z_ben = marke(s, XJ, 1.4, BLAU, 0.2, 0.14)
    kz = kreuz(s, XF - 0.3, 1.85, 0.14)
    rs = chip(s, (XJ, 0.35), "rsyslogd", GRAU, WEISS, b=0.9, h=0.32)
    p_rs = [pf(s, (XJ, 1.18), (XJ, 0.53), farbe=GRAU, dicke=2, dash=DASH, spitze=0.08),
            L(s, "kopie", W_KOPIE, (XJ + 0.08, 0.85), FM, "left", GRAU)]
    dateien = [tx(s, "/var/log/syslog", (0.45, 0.48), TK, "left"), tx(s, "/var/log/auth.log", (0.45, 0.2), TK, "left")]
    p_dat = [pf(s, (XJ + 0.47, 0.4), (0.4, 0.48), farbe=GRAU, dicke=2, spitze=0.08),
             pf(s, (XJ + 0.47, 0.3), (0.4, 0.2), farbe=GRAU, dicke=2, spitze=0.08)]
    schritt(s, EIN(quellen, 0.7))
    schritt(s, EIN([jd[0], jd[1]], 0.5), ZEICHNE(pq, 0.6), EIN(unterwegs, 0.4))
    schritt(s, *[VER(u, r4(XJ - 0.85 - XQ - 0.68), r4((1.4 + (y - 1.4) * 0.3) - y), 0.8) for u, y in zip(unterwegs, ys)])
    schritt(s, AUS(unterwegs, 0.3), EIN(zettel, 0.6))
    s.pause(0.5)
    schritt(s, EIN(ablagen, 0.5), ZEICHNE(pa, 0.5), EIN([z_sys, z_ben], 0.3))
    schritt(s, VER(z_sys, XA - 0.35 - XJ, 1.85 - 1.4, 0.7), VER(z_ben, XA - 0.35 - XJ, 1.0 - 1.4, 0.7))
    s.pause(0.4)
    schritt(s, EIN(filt + jc, 0.6))
    schritt(s, VER(z_sys, r4(XF - 0.3 - XA + 0.35), 0, 0.6), VER(z_ben, r4(XF - 0.3 - XA + 0.35), 0.4, 0.6))
    schritt(s, EIN(kz, 0.3), VER(z_ben, r4(XC - 0.5 - XF + 0.3), 0, 0.7))
    s.pause(0.5)
    schritt(s, ZEICHNE(p_rs[0], 0.5), EIN([p_rs[1]] + rs, 0.5))
    schritt(s, ZEICHNE(p_dat, 0.5), EIN(dateien, 0.5))
    s.speichern()


J_ZEILEN = ["Nov 10 15:29:19 labor systemd[383]: Started k8eieruhr.service - Eieruhr zum Üben.",
            "Nov 10 15:29:25 labor systemd[383]: Stopping k8eieruhr.service - Eieruhr zum Üben...",
            "Nov 10 15:29:25 labor systemd[383]: Stopped k8eieruhr.service - Eieruhr zum Üben.",
            "Nov 10 15:29:25 labor systemd[383]: Started k8eieruhr.service - Eieruhr zum Üben."]
W_STOPPT_STARTET = ("stoppt und startet k8eieruhr", "stops and starts k8eieruhr", "detiene e inicia k8eieruhr",
                    "停止并启动 k8eieruhr", "arrête et démarre k8eieruhr", "k8eieruhr'u durdurur ve başlatır")
W_DREI = ("drei Meldungen", "three messages", "tres mensajes", "三条消息", "trois messages", "üç ileti")


def k8journalfolgen():
    """Zwei Terminals untereinander, voller Wortlaut aus dem Heft. Oben (~/linuxk8) journalctl --user -u k8eieruhr -f -n 1:
    die letzte alte Meldung, dann wartet es. Unten (~, neues Terminal) systemctl --user restart k8eieruhr. Der Weg:
    systemd --user stoppt und startet den Dienst, schickt drei Meldungen an systemd-journald; oben erscheinen Stopping,
    Stopped, Started mit derselben Uhrzeit. Zuletzt Strg+C (^C) und die Eingabeaufforderung."""
    s = Szene("linux/k8journalfolgen", reihenfolge="anlegen")
    t = s.terminal(pos=(-3.44, 2.5), spalten=84, zeilen=7, prompt=P8, groesse=18)
    u = s.terminal(pos=(-3.44, 0.45), spalten=52, zeilen=2, groesse=18)
    yu = u.y(0)
    sysd = chip(s, (2.3, yu), "systemd --user", b=1.36, h=0.32)
    l_ss = L(s, "stoppt", W_STOPPT_STARTET, (2.3, r4(yu - 0.33)), FM, "center", GRAU)
    jd = chip(s, (2.3, 0.66), "systemd-journald", DUNKEL, WEISS, b=1.5, h=0.3)
    p1 = pf(s, (u.xr(50) + 0.08, yu), (2.3 - 0.7, yu), farbe=ORANGE, dicke=2.5, spitze=0.1)
    p2 = pf(s, (2.3, r4(yu + 0.17)), (2.3, 0.5), farbe=ORANGE, dicke=2.5, spitze=0.09)
    p3 = pf(s, (2.3, 0.82), (2.3, r4(t.unten_kante - 0.02)), farbe=ORANGE, dicke=2.5, spitze=0.09)
    l_drei = L(s, "drei", W_DREI, (2.42, r4((0.82 + t.unten_kante) / 2)), FM, "left", ORANGE)
    schritt(s, EIN([t.id, u.id], 0.7))
    s.pause(0.3)
    t.eingabe("journalctl --user -u k8eieruhr -f -n 1", dauer=1.6)
    t.ausgabe(J_ZEILEN[0], dauer=0.5)
    t.warten(1.2)
    u.eingabe("systemctl --user restart k8eieruhr", dauer=1.4)
    schritt(s, ZEICHNE(p1, 0.5), EIN(sysd + [l_ss], 0.5))
    schritt(s, ZEICHNE(p2, 0.4), EIN(jd, 0.4))
    with s.gleichzeitig():
        schritt(s, ZEICHNE(p3, 0.4), EIN(l_drei, 0.4))
        t.ausgabe(J_ZEILEN[1], dauer=0.5)
    t.ausgabe(J_ZEILEN[2], dauer=0.5)
    with s.gleichzeitig():
        t.ausgabe(J_ZEILEN[3], dauer=0.5)
        u.prompt(dauer=0.5)
    s.pause(0.6)
    t.ausgabe("^C", dauer=0.4)
    t.prompt(pfad=PFAD)
    s.speichern()


W_STUDENT_EIGENE = ("eigene Meldungen", "own messages", "mensajes propios", "自己的消息", "ses propres messages",
                    "kendi iletileri")
W_ADM_MITGLIED = ("Mitglied von adm", "member of adm", "miembro de adm", "adm 组成员", "membre de adm", "adm üyesi")
W_ROOT_SUDO = ("root (über sudo)", "root (via sudo)", "root (con sudo)", "root（通过 sudo）", "root (via sudo)",
               "root (sudo ile)")
W_INHALT_SYS = ("Kernel, cron, sudo, systemd", "kernel, cron, sudo, systemd", "kernel, cron, sudo, systemd",
                "内核、cron、sudo、systemd", "noyau, cron, sudo, systemd", "çekirdek, cron, sudo, systemd")
W_GROUP_TEST = ("/etc/group, Testsystem:", "/etc/group, test system:", "/etc/group, sistema de prueba:",
                "/etc/group，测试系统：", "/etc/group, système de test :", "/etc/group, test sistemi:")
W_GROUP_GEW = ("gewöhnliche Installation:", "usual installation:", "instalación habitual:", "常规安装：",
               "installation ordinaire :", "olağan kurulum:")
W_FEHLT = ("student fehlt", "student is missing", "falta student", "缺少 student", "student manque", "student yok")


def k8journalrechte():
    """Ablagen System (Kernel, cron, sudo, systemd) und Benutzer 1000 (k8eieruhr); Leser student (nur eigene; rotes
    Schloss am System, Hinweis „not seeing messages“), Mitglied von adm (beide), root über sudo (beide). Zum Schluss
    adm:x:4:syslog aus /etc/group: student fehlt; klein darunter die Zeile einer gewöhnlichen Installation mit student."""
    s = Szene("linux/k8journalrechte", reihenfolge="anlegen")
    XA = 2.25
    ablagen = [box(s, (XA, 1.75), 2.2, 0.62, DUNKEL, GRAU_HELL, 2, "rect"), L(s, "sys", W_SYSTEM, (XA, 1.88), FM),
               L(s, "inhalt", W_INHALT_SYS, (XA, 1.62), FM, "center", GRAU),
               box(s, (XA, 0.75), 2.2, 0.62, DUNKEL, GRAU_HELL, 2, "rect"), L(s, "ben", W_BEN1000, (XA, 0.88), FM),
               tx(s, "k8eieruhr", (XA, 0.62), TK, "center", GRAU)]
    XL = -2.6
    leser = [chip(s, (XL, 1.95), "student", b=1.0, h=0.34),
             wchip(s, (XL, 1.2), "adm", W_ADM_MITGLIED, 1.55, h=0.34),
             wchip(s, (XL, 0.45), "root", W_ROOT_SUDO, 1.55, h=0.34)]
    x0 = XL + 0.8
    xa = XA - 1.1

    def lin(y0, y1, farbe=GRUEN, dash=""):
        return linie(s, (r4(x0), y0), (r4(xa), y1), farbe, 2.5, dash)

    st_ok = lin(1.95, 0.9)
    st_nein = lin(1.95, 1.9, ROT, DASH)
    schl = s.schloss((r4((x0 + xa) / 2), 1.99), 0.24, farbe=ROT)
    hinweis = tx(s, "… not seeing messages …", (-3.4, 1.62), TK, "left", ROT)
    adm = [lin(1.2, 1.75), lin(1.2, 0.75)]
    root = [lin(0.45, 1.6), lin(0.45, 0.6)]
    g1 = s.raster(["adm:x:4:syslog"], (-0.85, -0.25), groesse=20)
    l1 = L(s, "test", W_GROUP_TEST, (-1.0, -0.25), FM, "right", GRAU)
    fehlt = L(s, "fehlt", W_FEHLT, (0.45, -0.25), FM, "left", ROT)
    g2 = s.raster(["adm:x:4:syslog,student"], (-0.85, -0.6), groesse=17)
    l2 = L(s, "gew", W_GROUP_GEW, (-1.0, -0.6), FM, "right", GRAU)
    a2, b2 = g2.finde(0, ",student")
    m2 = g2.markieren(0, a2, b2, GRUEN, 0.25)
    schritt(s, EIN(ablagen, 0.6))
    s.pause(0.4)
    schritt(s, EIN(leser[0], 0.5), ZEICHNE(st_ok, 0.7))
    schritt(s, ZEICHNE(st_nein, 0.6), WACHS(schl, 0.6))
    schritt(s, EIN(hinweis, 0.5))
    s.pause(0.5)
    schritt(s, EIN(leser[1], 0.5), ZEICHNE(adm, 0.7))
    schritt(s, EIN(leser[2], 0.5), ZEICHNE(root, 0.7))
    s.pause(0.6)
    schritt(s, EIN(g1.ids + [l1], 0.6))
    schritt(s, BETONE(g1.ids, 0.7), EIN(fehlt, 0.5))
    schritt(s, EIN(g2.ids + [l2, m2], 0.6))
    s.speichern()


# ================================================================== Bildschirm: systemctl status (Unterabschnitt 7.4)
def _gr(t):
    return farbig(t, "gruen", True)


STATUS_CRON = [_gr("●") + " cron.service - Regular background program processing daemon",
               "     Loaded: loaded (/usr/lib/systemd/system/cron.service; " + _gr("enabled") + "; preset: " + _gr("enabled")
               + ")",
               "     Active: " + _gr("active (running)") + " since Tue 2026-11-10 15:24:41 CET; 4min 23s ago",
               " Invocation: 5bebfba81d7240c09d04b95ea11dc2b4",
               "       Docs: man:cron(8)",
               "   Main PID: 160 (cron)",
               "      Tasks: 1 (limit: 38204)",
               "     Memory: 508K (peak: 2M)",
               "        CPU: 15ms",
               "     CGroup: /system.slice/cron.service",
               "             " + farbig("└─", "grau") + "160 /usr/sbin/cron -f -P"]
W_STATUSTEILE = [("Name und Beschreibung der Unit", "name and description of the unit", "nombre y descripción de la unit",
                  "unit 的名称和描述", "nom et description de l'unit", "unit'in adı ve açıklaması"),
                 ("Loaded: Datei, enabled, preset", "Loaded: file, enabled, preset", "Loaded: archivo, enabled, preset",
                  "Loaded：文件、enabled、preset", "Loaded : fichier, enabled, preset", "Loaded: dosya, enabled, preset"),
                 ("Active: Zustand, seit wann", "Active: state, since when", "Active: estado, desde cuándo",
                  "Active：状态、从何时起", "Active : état, depuis quand", "Active: durum, ne zamandan beri"),
                 ("Main PID: Hauptprozess", "Main PID: main process", "Main PID: proceso principal", "Main PID：主进程",
                  "Main PID : processus principal", "Main PID: ana süreç"),
                 ("CGroup: Gruppe der Prozesse", "CGroup: group of processes", "CGroup: grupo de procesos", "CGroup：进程组",
                  "CGroup : groupe de processus", "CGroup: süreç grubu")]


def k8statusbild():
    """systemctl status cron (Block in 7.4, wörtlich) als Seitenanzeiger in einem Terminal mit zehn Zeilen für die
    Ausgabe: ● und active (running) und enabled grün, Baumzeichen grau, Statuszeile lines 1-10/11. Erst eine Zeile weiter
    (lines 2-11/11 (END), der Prozessbaum erscheint) und zurück; dann leuchten nacheinander Name (1), Loaded (2),
    Active (3), Main PID (4) und CGroup (5), links nummeriert, Liste darunter. Journalzeilen stehen nicht im Block."""
    s = Szene("linux/k8statusbild", reihenfolge="anlegen")
    p = s.pager(STATUS_CRON, pos=(-3.05, 2.35), sichtbar=10, titel="student@labor: ~/linuxk8", groesse=17)
    teile = [0, 1, 2, 5, 9]
    xn = -3.25
    y_leg = (r4(p.unten_kante - 0.25), r4(p.unten_kante - 0.52), r4(p.unten_kante - 0.79))
    schritte = []
    for k, z in enumerate(teile):
        fr = p.rahmen(z, None, None, farbe=ORANGE, dicke=2.5, rand=0.0)
        nr = text(s, str(k + 1), (xn, p.y(z)), FM, "center", ORANGE)
        xl, yl = (-3.35, y_leg[k]) if k < 3 else (0.35, y_leg[k - 3])
        leg = [text(s, str(k + 1), (xl, yl), FM, "left", ORANGE),
               L(s, "teil%d" % k, W_STATUSTEILE[k], (r4(xl + 0.2), yl), FM, "left")]
        schritte.append((fr, [nr] + leg))
    schritt(s, EIN(p.id, 0.7))
    s.pause(0.6)
    p.weiter(1, dauer=0.6)
    s.pause(0.8)
    p.weiter(-1, dauer=0.6)
    s.pause(0.5)
    vorher = None
    for k, (fr, rest) in enumerate(schritte):
        teile_k = [EIN([fr] + rest, 0.6)]
        if vorher is not None:
            teile_k.append(AUS(vorher, 0.4))
        schritt(s, *teile_k)
        s.pause(0.5)
        vorher = fr
    s.speichern()


SZENEN = (k8zeitteilung, k8pidvergabe, k8forkexec, k8baum, k8psspalten, k8zustaende, k8zombie, k8procstatus, k8topbild,
          k8vordergrund, k8jobliste, k8hintergrundlesen, k8jobzustaende, k8signal, k8termkill, k8exitrechnung, k8wer,
          k8trap, k8timeout, k8sighup, k8nohup, k8last, k8lastrechnung, k8niceanteil, k8dienst, k8unitdatei, k8neustart,
          k8statusbild, k8enable, k8journal, k8journalfolgen, k8journalrechte)

if __name__ == "__main__":
    wahl = set(sys.argv[1:])
    for f in SZENEN:
        if not wahl or f.__name__ in wahl:
            f()
            print("gebaut:", f.__name__)
