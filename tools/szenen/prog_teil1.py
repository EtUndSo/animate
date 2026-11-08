"""Programmieren, Python 1 (C:\\Bücher\\EtUndSo\\Programmieren\\Arbeitshefte\\kap1_stufen.tex, kap1_stufen_b.tex): Abbildungen.

Szenenname prog/k1<name> = \\label{fig:k1<name>} im Heft. Stil wie tools/szenen/cyber_teil1.py (Kästen, Pfeile, Texte).
Bauen:  python tools/szenen/prog_teil1.py
Export: python tools/export_szenen.py prog/k1heron prog/k1wege prog/k1modi prog/k1fehlerarten prog/k1traceback
Code in Schreibmaschinenschrift setzt s.formel mit \\texttt{...} (MathJax); Einrückungen über \\hphantom, damit die
Zeichen untereinander stehen wie im Terminal.
Rechenbilder (Summe, Produkt, Skalarprodukt mit Zahlen) kommen in diesem Heft nicht vor.
Die Zahlen prüft C:\\Bücher\\EtUndSo\\Programmieren\\Arbeitshefte\\rechnung_kap1.py.
"""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from szenen_lib import *  # noqa: E402,F403

KLEIN = 22
MITTEL = 24
GRUEN_HELL = "#e6f3ea"
ROT_HELL = "#fbe9e9"
CODE_GRAU = "#f6f6f2"


def kasten(s, mitte, breite, hoehe, text, groesse=MITTEL, farbe=SCHWARZ, textfarbe=None, fuellung="#ffffff", dash="", dicke=2.5):
    """Abgerundeter Kasten mit zentriertem Text (mehrzeilig mit \\n)."""
    s.box("", mitte, breite=breite, hoehe=hoehe, form="round", farbe=farbe, fuellung=fuellung, deckung=1, dicke=dicke, dash=dash)
    s.text(None, text, mitte, groesse, "center", textfarbe or farbe)


def tt(text, einzug=0):
    """Eine Zeile Schreibmaschinenschrift für s.formel; einzug = so viele Zeichen Leerraum davor."""
    p = r"\hphantom{\texttt{%s}}" % ("0" * einzug) if einzug else ""
    return p + r"\texttt{%s}" % text


def code(s, zeilen, mitte, hoehe, farbe=SCHWARZ):
    """Mehrere Zeilen Code linksbündig untereinander (eine Formel, damit die Zeichen genau untereinander stehen)."""
    tex = r"\begin{array}{l}" + r"\\".join(zeilen) + r"\end{array}"
    return s.formel(tex, mitte=mitte, hoehe=hoehe, farbe=farbe)


# ------------------------------------------------------------------ Abschnitt 1
def k1heron():
    """Heron-Verfahren für Wurzel 2 auf dem Zahlenstrahl: g und 2/g auf beiden Seiten, Mittelwert wird das neue g."""
    s = Szene("prog/k1heron")
    x0, k = -2.0, 5.3                                     # Zahl v liegt bei x0 + (v - 1) * k

    def x(v):
        return x0 + (v - 1) * k

    wz = 2 ** 0.5
    s.linie(None, (x(wz), 1.75), (x(wz), -1.75), farbe=GRAU, dicke=2, dash=DASH)
    s.text(None, "√2 ≈ 1.4142", (x(wz), 2.0), MITTEL, "center")
    s.tr("dg", "Durchgang", "Pass", "Pasada", "第", fr="Passage", tr="Adım")
    mw = s.tr("mw", "Mittelwert wird\ndas neue g", "the mean becomes\nthe new g", "la media es\nel nuevo g", "平均值成为\n新的 g",
              fr="la moyenne devient\nle nouveau g", tr="ortalama yeni\ng olur")
    zeilen = [(1.2, 1.0, 2.0), (0.1, 1.5, 4 / 3), (-1.0, 17 / 12, 24 / 17)]
    for n, (y, g, h) in enumerate(zeilen, start=1):
        s.text(None, "@{dg} %d" % n, (x0 - 0.2, y), MITTEL, "right")
        if n < 3:
            s.linie(None, (x(min(g, h)), y), (x(max(g, h)), y), farbe="#9cc3ee", dicke=8)
        s.punkt(None, x(h), y, farbe=ORANGE, r=0.075)
        s.punkt(None, x(g), y, farbe=BLAU, r=0.075)
        if n < 3:
            m = (g + h) / 2
            s.linie(None, (x(m), y + 0.12), (x(m), y - 0.12), farbe=SCHWARZ, dicke=3)
            s.pfeil((x(m), y - 0.17), (x(m), zeilen[n][0] + 0.3), farbe=GRAU, dicke=2.5, spitze=0.14)
    s.text(None, "g = 1", (x(1.0), 1.47), KLEIN, "center", BLAU)
    s.text(None, "2/g = 2", (x(2.0) + 0.05, 1.47), KLEIN, "right", ORANGE)
    s.text(None, mw, (x(1.5) + 0.12, 0.72), KLEIN, "left", GRAU)
    s.text(None, "g = 1.5", (x(1.5) + 0.15, -0.15), KLEIN, "left", BLAU)
    s.text(None, "2/g ≈ 1.333", (x(4 / 3) - 0.1, -0.2), KLEIN, "right", ORANGE)
    s.text(None, "g ≈ 1.4167", (x(17 / 12) + 0.15, -0.88), KLEIN, "left", BLAU)
    s.text(None, "2/g ≈ 1.4118", (x(24 / 17) - 0.15, -1.18), KLEIN, "right", ORANGE)
    s.linie(None, (x(1.0), -1.75), (x(2.0), -1.75), farbe=GRAU, dicke=2.5)
    for v in (1.0, 1.2, 1.4, 1.6, 1.8, 2.0):
        s.linie(None, (x(v), -1.7), (x(v), -1.8), farbe=GRAU, dicke=2.5)
        s.text(None, "%g" % v, (x(v), -2.02), KLEIN, "center", GRAU)
    s.speichern()


# ------------------------------------------------------------------ Abschnitt 2
def k1wege():
    """Zwei Wege vom Quelltext zur Ausführung: Python (CPython) links, C mit Compiler rechts."""
    s = Szene("prog/k1wege")
    xl, xr, b, ys = -1.8, 1.8, 3.15, (2.75, 1.7, 0.65, -0.4, -1.45)
    py = s.tr("py", "Python (CPython)", "Python (CPython)", "Python (CPython)", "Python（CPython）", fr="Python (CPython)", tr="Python (CPython)")
    cc = s.tr("cc", "C (Compiler)", "C (compiler)", "C (compilador)", "C（编译器）", fr="C (compilateur)", tr="C (derleyici)")
    s.text(None, py, (xl, 3.45), 26, "center")
    s.text(None, cc, (xr, 3.45), 26, "center")
    links = [s.tr("l1", "hallo.py: Quelltext", "hallo.py: source code", "hallo.py: código fuente", "hallo.py：源代码",
                  fr="hallo.py : code source", tr="hallo.py: kaynak kod"),
             s.tr("l2", "Übersetzen: Syntax prüfen,\nBytecode erzeugen", "Translate: check syntax,\ngenerate bytecode",
                  "Traducir: comprobar sintaxis,\ngenerar bytecode", "翻译：检查语法，\n生成字节码",
                  fr="Traduire : vérifier la syntaxe,\nproduire le bytecode", tr="Çevir: sözdizimini denetle,\nbayt kodu üret"),
             s.tr("l3", "Bytecode\n(im Arbeitsspeicher)", "Bytecode\n(in main memory)", "Bytecode\n(en la memoria)", "字节码\n（在内存中）",
                  fr="Bytecode\n(en mémoire vive)", tr="Bayt kodu\n(ana bellekte)"),
             s.tr("l4", "Interpreterschleife:\nein Befehl nach dem anderen", "Interpreter loop:\none instruction after another",
                  "Bucle del intérprete:\nuna instrucción tras otra", "解释器循环：\n一条接一条执行",
                  fr="Boucle de l'interpréteur :\nune instruction après l'autre", tr="Yorumlayıcı döngüsü:\nkomutlar sırayla"),
             s.tr("aus", "Ausgabe", "Output", "Salida", "输出", fr="Sortie", tr="Çıktı")]
    rechts = [s.tr("r1", "hallo.c: Quelltext", "hallo.c: source code", "hallo.c: código fuente", "hallo.c：源代码",
                   fr="hallo.c : code source", tr="hallo.c: kaynak kod"),
              s.tr("r2", "Compiler gcc:\neinmal vorab übersetzen", "Compiler gcc:\ntranslate once in advance",
                   "Compilador gcc:\ntraducir una vez antes", "编译器 gcc：\n预先翻译一次",
                   fr="Compilateur gcc :\ntraduire une fois avant", tr="Derleyici gcc:\nönceden bir kez çevir"),
              s.tr("r3", "hallo.exe bzw. hallo:\nMaschinencode (Datei)", "hallo.exe or hallo:\nmachine code (file)",
                   "hallo.exe o hallo:\ncódigo máquina (archivo)", "hallo.exe 或 hallo：\n机器码（文件）",
                   fr="hallo.exe ou hallo :\ncode machine (fichier)", tr="hallo.exe veya hallo:\nmakine kodu (dosya)"),
              s.tr("r4", "Prozessor führt den\nMaschinencode direkt aus", "Processor runs the\nmachine code directly",
                   "El procesador ejecuta\nel código máquina", "处理器直接执行\n机器码",
                   fr="Le processeur exécute\nle code machine", tr="İşlemci makine kodunu\ndoğrudan çalıştırır"),
              "@aus"]
    for k, (y, tl, tr_) in enumerate(zip(ys, links, rechts)):
        h = 0.72 if k in (1, 2, 3) else 0.52
        grau = "#f2f2f2" if k in (0, 4) else "#ffffff"
        kasten(s, (xl, y), b, h, tl, MITTEL, fuellung=grau)
        kasten(s, (xr, y), b, h, tr_, MITTEL, fuellung=grau)
        if k < 4:
            h2 = 0.72 if k + 1 in (1, 2, 3) else 0.52
            for xx in (xl, xr):
                s.pfeil((xx, y - h / 2 - 0.02), (xx, ys[k + 1] + h2 / 2 + 0.02), dicke=2.5, spitze=0.13)
    s.box("", (xl, 0.65), breite=b + 0.24, hoehe=3.45, form="round", farbe=BLAU, fuellung="#ffffff", deckung=0, dicke=2.5, dash=DASH)
    rahmen = s.tr("rahmen", "gestrichelt: Programm python,\nläuft bei jedem Start mit",
                  "dashed: the program python,\nruns along at every start", "discontinuo: el programa python,\nse ejecuta en cada inicio",
                  "虚线框：程序 python，\n每次启动都要运行", fr="en tirets : le programme python,\ns'exécute à chaque lancement",
                  tr="kesik çizgi: python programı,\nher başlatmada çalışır")
    s.text(None, rahmen, (xl, -2.15), KLEIN, "center", BLAU)
    jedes = s.tr("jedes", "bei jedem Start", "at every start", "en cada inicio", "每次启动", fr="à chaque lancement", tr="her başlatmada")
    s.text(None, jedes, (xr + 0.1, 0.12), KLEIN, "left", GRAU)
    s.speichern()


# ------------------------------------------------------------------ Abschnitt 5
def k1modi():
    """Interaktiver Modus (Kreislauf) gegen Skript (ganze Datei übersetzen, Zeilen nacheinander, nur print-Ausgaben)."""
    s = Szene("prog/k1modi")
    im = s.tr("im", "Interaktiver Modus", "Interactive mode", "Modo interactivo", "交互模式", fr="Mode interactif", tr="Etkileşimli kip")
    sk = s.tr("sk", "Skript", "Script", "Script", "脚本", fr="Script", tr="Betik")
    s.text(None, im, (-1.8, 2.45), 26, "center")
    s.text(None, sk, (2.0, 2.45), 26, "center")
    lesen = s.tr("lesen", "Lesen: >>> 2 + 3", "Read: >>> 2 + 3", "Leer: >>> 2 + 3", "读入：>>> 2 + 3", fr="Lire : >>> 2 + 3", tr="Oku: >>> 2 + 3")
    ausw = s.tr("ausw", "Auswerten", "Evaluate", "Evaluar", "求值", fr="Évaluer", tr="Değerlendir")
    anz = s.tr("anz", "Anzeigen: 5", "Display: 5", "Mostrar: 5", "显示：5", fr="Afficher : 5", tr="Göster: 5")
    kasten(s, (-1.8, 1.55), 2.25, 0.55, lesen)
    kasten(s, (-0.88, 0.05), 1.5, 0.55, ausw)
    kasten(s, (-2.72, 0.05), 1.5, 0.55, anz)
    s.pfeil((-1.1, 1.27), (-0.88, 0.33), dicke=2.5, spitze=0.14)
    s.pfeil((-1.63, 0.05), (-1.97, 0.05), dicke=2.5, spitze=0.14)
    s.pfeil((-2.72, 0.33), (-2.5, 1.27), dicke=2.5, spitze=0.14)
    s.text(None, s.tr("wert", "Wert 5", "value 5", "valor 5", "值 5", fr="valeur 5", tr="değer 5"), (-1.8, -0.32), KLEIN, "center", GRAU)
    jede = s.tr("jede", "jede Eingabe einzeln;\nder Wert jedes Ausdrucks\nwird angezeigt", "each input on its own;\nthe value of every\nexpression is displayed",
                "cada entrada por separado;\nse muestra el valor\nde cada expresión", "每次一条输入；\n每个表达式的值\n都会显示",
                fr="chaque saisie séparément ;\nla valeur de chaque\nexpression s'affiche", tr="her girdi ayrı ayrı;\nher ifadenin değeri\ngösterilir")
    s.text(None, jede, (-1.8, -1.15), KLEIN, "center")
    s.box("", (2.0, 1.6), breite=2.6, hoehe=0.95, form="round", fuellung=CODE_GRAU, deckung=1, dicke=2)
    code(s, [tt('print("Vorher")'), tt("2 + 3"), tt('print("Nachher")')], (2.0, 1.6), 0.78)
    s.text(None, "ausdruck.py", (0.75, 2.21), KLEIN, "left", GRAU)
    ue = s.tr("ue", "ganze Datei übersetzen", "translate the whole file", "traducir todo el archivo", "翻译整个文件",
              fr="traduire tout le fichier", tr="tüm dosyayı çevir")
    zl = s.tr("zl", "Zeilen von oben nach\nunten ausführen", "run the lines from\ntop to bottom", "ejecutar las líneas\nde arriba abajo",
              "从上到下\n执行各行", fr="exécuter les lignes\nde haut en bas", tr="satırları yukarıdan\naşağıya çalıştır")
    kasten(s, (2.0, 0.55), 2.8, 0.5, ue)
    kasten(s, (2.0, -0.4), 2.8, 0.72, zl)
    s.pfeil((2.0, 1.12), (2.0, 0.81), dicke=2.5, spitze=0.13)
    s.pfeil((2.0, 0.29), (2.0, -0.03), dicke=2.5, spitze=0.13)
    s.pfeil((2.0, -0.77), (2.0, -1.08), dicke=2.5, spitze=0.13)
    s.box("", (2.0, -1.43), breite=1.5, hoehe=0.68, form="round", fuellung="#ffffff", deckung=1, dicke=2)
    code(s, [tt("Vorher"), tt("Nachher")], (2.0, -1.43), 0.5)
    nur = s.tr("nur", "sichtbar: nur die Ausgaben\nvon print; 2 + 3 zeigt nichts", "visible: only the output\nof print; 2 + 3 shows nothing",
               "visible: solo la salida\nde print; 2 + 3 no muestra nada", "可见的只有 print 的输出；\n2 + 3 什么也不显示",
               fr="visible : seulement la sortie\nde print ; 2 + 3 n'affiche rien", tr="görünen: yalnızca print\nçıktısı; 2 + 3 bir şey göstermez")
    s.text(None, nur, (2.0, -2.2), KLEIN, "center", GRAU)
    s.speichern()


# ------------------------------------------------------------------ Abschnitt 6
def k1fehlerarten():
    """Syntaxfehler: Übersetzen scheitert, keine Zeile läuft. Laufzeitfehler: Zeile 1 läuft, Zeile 2 bricht ab."""
    s = Szene("prog/k1fehlerarten")
    lauf = s.tr("lauf", "läuft", "runs", "se ejecuta", "已执行", fr="s'exécute", tr="çalışır")
    nicht = s.tr("nicht", "läuft nicht", "does not run", "no se ejecuta", "未执行", fr="non exécutée", tr="çalışmaz")
    bricht = s.tr("bricht", "bricht ab", "aborts", "se interrumpe", "中止", fr="s'interrompt", tr="durur")
    fehlt = s.tr("fehlt", "hier fehlt )", ") is missing", "falta )", "缺少 )", fr=") manquante", tr=") eksik")
    us = s.tr("us", "Übersetzen scheitert", "Translation fails", "La traducción falla", "翻译失败", fr="La traduction échoue", tr="Çeviri başarısız")
    ug = s.tr("ug", "Übersetzen gelingt", "Translation succeeds", "La traducción funciona", "翻译成功", fr="La traduction réussit", tr="Çeviri başarılı")
    spalten = (
        (-3.65, "syntaxfehler.py", us, ROT, ROT_HELL,
         [('print("Zeile 1")', nicht, GRAU, "#ffffff", SCHWARZ), ('print("Zeile 2")', nicht, GRAU, "#ffffff", SCHWARZ),
          ('print("Zeile 3"', fehlt, ROT, "#ffffff", ROT)],
         s.tr("aus_s", "Ausgabe: nur die\nMeldung SyntaxError", "Output: only the\nSyntaxError message", "Salida: solo el\nmensaje SyntaxError",
              "输出：只有\nSyntaxError 信息", fr="Sortie : seulement le\nmessage SyntaxError", tr="Çıktı: yalnızca\nSyntaxError iletisi")),
        (0.15, "laufzeitfehler.py", ug, GRUEN, GRUEN_HELL,
         [('print("Zeile 1")', lauf, GRUEN, GRUEN_HELL, SCHWARZ), ("print(5 / 0)", bricht, ROT, "#ffffff", ROT),
          ('print("Zeile 3")', nicht, GRAU, "#ffffff", SCHWARZ)],
         s.tr("aus_l", "Ausgabe: Zeile 1,\ndann der Traceback", "Output: Zeile 1,\nthen the traceback", "Salida: Zeile 1,\ny luego el traceback",
              "输出：Zeile 1，\n然后是 traceback", fr="Sortie : Zeile 1,\npuis le traceback", tr="Çıktı: Zeile 1,\nsonra traceback")),
    )
    for x0, datei, phase, pfarbe, phell, zeilen, ausgabe in spalten:
        s.formel(tt(datei), mitte=(x0 + 1.2, 2.55), hoehe=0.21)
        kasten(s, (x0 + 1.2, 1.9), 2.4, 0.5, phase, MITTEL, farbe=pfarbe, textfarbe=SCHWARZ, fuellung=phell)
        for k, (zeile, status, sfarbe, fuell, rand) in enumerate(zeilen):
            y = 1.0 - 0.72 * k
            s.box("", (x0 + 1.05, y), breite=2.1, hoehe=0.5, form="round", farbe=rand, fuellung=fuell, deckung=1, dicke=2.5 if rand == ROT else 2)
            s.formel(tt(zeile), mitte=(x0 + 1.05, y), hoehe=0.2, farbe=GRAU if sfarbe == GRAU else SCHWARZ)
            s.text(None, status, (x0 + 2.2, y), KLEIN, "left", sfarbe)
        s.text(None, ausgabe, (x0 + 1.2, -1.3), KLEIN, "center")
    s.speichern()


def k1traceback():
    """Der Traceback von laufzeitfehler.py, in seine Teile zerlegt; gelesen wird von unten."""
    s = Szene("prog/k1traceback")
    zeilen = [tt("Traceback (most recent call last):"),
              tt('File "/home/student/python-kurs/laufzeitfehler.py",', 2),
              r"\hphantom{\texttt{00}}\hookrightarrow" + tt("line 2, in <module>", 1),
              tt("print(5 / 0)", 4),
              tt("~~^~~", 10),
              tt("ZeroDivisionError: division by zero")]
    hoehe, mitte = 1.74, (0.3, 1.55)
    s.box("", (0.32, 1.55), breite=6.4, hoehe=2.1, form="rect", farbe="#d6d8d0", fuellung=CODE_GRAU, deckung=1, dicke=2)
    code(s, zeilen, mitte, hoehe)
    zeile_h = hoehe / len(zeilen)
    oben = mitte[1] + hoehe / 2
    for nr, k in ((1, 0), (2, 1), (3, 3), (4, 4), (5, 5)):
        y = oben - (k + 0.5) * zeile_h
        s.kreis(None, -3.3, y, 0.15, farbe=ROT, dicke=2.5, fuellung="#ffffff", deckung=1)
        s.text(None, str(nr), (-3.3, y), KLEIN, "center", ROT)
    leg = [(5, s.tr("t5", "Art und Beschreibung: was passiert ist (hier anfangen)", "type and description: what happened (start here)",
                    "tipo y descripción: qué ha pasado (empieza aquí)", "类型与描述：发生了什么（从这里读起）",
                    fr="type et description : ce qui s'est passé (commencer ici)", tr="tür ve açıklama: ne oldu (buradan başla)")),
           (2, s.tr("t2", "Datei, Zeile, <module> = oberste Ebene: wo", "file, line, <module> = top level: where",
                    "archivo, línea, <module> = nivel superior: dónde", "文件、行号、<module> = 顶层：在哪里",
                    fr="fichier, ligne, <module> = niveau supérieur : où", tr="dosya, satır, <module> = en üst düzey: nerede")),
           (3, s.tr("t3", "die Zeile, wie sie in der Datei steht", "the line as written in the file", "la línea tal como está en el archivo",
                    "文件中的那一行", fr="la ligne telle qu'elle est dans le fichier", tr="dosyadaki haliyle satır")),
           (4, s.tr("t4", r"\^ zeigt auf das Rechenzeichen, ~ auf die Werte", r"\^ points to the operator, ~ to the values",
                    r"\^ señala el operador, ~ los valores", r"\^ 指向运算符，~ 指向参与的值",
                    fr=r"\^ désigne l'opérateur, ~ les valeurs", tr=r"\^ işleci, ~ değerleri gösterir")),
           (1, s.tr("t1", "Kopfzeile: der jüngste Schritt steht zuletzt", "header: the most recent step comes last",
                    "cabecera: el paso más reciente va al final", "标题行：最近的一步在最后",
                    fr="en-tête : l'étape la plus récente vient en dernier", tr="başlık: en son adım en sonda"))]
    for j, (nr, txt) in enumerate(leg):
        y = -0.15 - 0.42 * j
        s.kreis(None, -3.3, y, 0.15, farbe=ROT, dicke=2.5, fuellung="#ffffff", deckung=1)
        s.text(None, str(nr), (-3.3, y), KLEIN, "center", ROT)
        s.text(None, txt, (-3.0, y), KLEIN, "left")
    s.speichern()


SZENEN = (k1heron, k1wege, k1modi, k1fehlerarten, k1traceback)

for f in SZENEN:
    f()
