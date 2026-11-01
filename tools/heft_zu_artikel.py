"""Arbeitshefte (LaTeX) -> Website-Artikel (Markdown für build_wissen.py), in allen vier Sprachen.

Aufruf (vom Repo-Root):
    python tools/heft_zu_artikel.py et3                 alle Hefte des Moduls
    python tools/heft_zu_artikel.py et3 --kap 1 3       nur diese Hefte
    python tools/heft_zu_artikel.py et3 --pruefen       nichts schreiben, nur Meldungen
    python tools/heft_zu_artikel.py et3 --aux DIR       Nummern gegen die .aux-Dateien in DIR prüfen

Das Heft bleibt die Quelle: Kap<N>_<Name>[_en|_es|_zh].tex mit den \\input-Dateien. Der Artikel wird daraus erzeugt und
nie von Hand geändert. Nummern (Gleichungen, Sätze, Abbildungen, Aufgaben) entstehen wie in LaTeX, Verweise werden zu
Links. Aufgaben bekommen ihre Lösung direkt als aufklappbaren Block, nicht am Ende. Abbildungen werden zu
:::abbildung <szene>, die Szene heißt wie das \\label (fig:k1bode -> et3/k1bode). Texte, die nur im PDF stimmen
(„Lösungen am Ende“, „dieses Heft“), werden je Sprache angepasst (WEBTEXT).

Ziel: content/<modul>/<NN-slug>/<NN-slug>[.en|.es|.zh].md
"""
import argparse
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))
sys.stdout.reconfigure(encoding="utf-8")
from build_wissen import slugify  # noqa: E402

LANGS = ("de", "en", "es", "zh")
NBSP, THIN = "\u00a0", "\u202f"

# ------------------------------------------------------------------------------------- Module ----
MODULE = {
    "et3": {
        "quelle": Path(r"C:\Bücher\ET3\Arbeitshefte"),
        "ziel": "et3",
        "szenen": "et3",
        "pfad": {"de": "Elektrotechnik / 3. Semester / Signale und Systeme",
                 "en": "Electrical Engineering / 3rd Semester / Signals and Systems",
                 "es": "Ingeniería eléctrica / 3.er semestre / Señales y sistemas",
                 "zh": "电气工程 / 第 3 学期 / 信号与系统"},
        "basis": "elektrotechnik/3-semester/signale-und-systeme",
        "order": 3200000,
        "hefte": {
            1: ("Kap1_Faltung", "lti-systeme-und-faltung",
                {"de": "LTI-Systeme und Faltung", "en": "LTI Systems and Convolution",
                 "es": "Sistemas LTI y convolución", "zh": "LTI 系统与卷积"}),
            2: ("Kap2_Laplace", "laplace-transformation",
                {"de": "Laplace-Transformation", "en": "Laplace Transform",
                 "es": "Transformada de Laplace", "zh": "拉普拉斯变换"}),
            3: ("Kap3_Fourier", "fourier-reihe-und-transformation",
                {"de": "Fourier-Reihe und -Transformation", "en": "Fourier Series and Transform",
                 "es": "Serie y transformada de Fourier", "zh": "傅里叶级数与变换"}),
            4: ("Kap4_Diskret", "abtastung-und-zeitdiskrete-systeme",
                {"de": "Abtastung und zeitdiskrete Systeme", "en": "Sampling and Discrete-Time Systems",
                 "es": "Muestreo y sistemas en tiempo discreto", "zh": "采样与离散时间系统"}),
            5: ("Kap5_Tiefpass", "tiefpass-und-bandpasssysteme",
                {"de": "Tiefpass- und Bandpasssysteme", "en": "Lowpass and Bandpass Systems",
                 "es": "Sistemas paso bajo y paso banda", "zh": "低通与带通系统"}),
            6: ("Kap6_Korrelation", "korrelationsfunktionen",
                {"de": "Korrelationsfunktionen", "en": "Correlation Functions",
                 "es": "Funciones de correlación", "zh": "相关函数"}),
            7: ("Kap7_Statistik", "zufallssignale",
                {"de": "Zufallssignale", "en": "Random Signals", "es": "Señales aleatorias", "zh": "随机信号"}),
            8: ("Kap8_Zusatz", "orthogonalentwicklung-und-leitungen",
                {"de": "Orthogonalentwicklung und Leitungen", "en": "Orthogonal Expansion and Transmission Lines",
                 "es": "Desarrollo ortogonal y líneas de transmisión", "zh": "正交展开与传输线"}),
        },
    },
}

MODULE["et1"] = {
    "quelle": Path(r"C:\Bücher\ET1\Arbeitshefte"),
    "ziel": "et1",
    "szenen": "et1",
    "pfad": {"de": "Elektrotechnik / 1. Semester / Grundlagen der Elektrotechnik",
             "en": "Electrical Engineering / 1st Semester / Fundamentals of Electrical Engineering",
             "es": "Ingeniería eléctrica / 1.er semestre / Fundamentos de ingeniería eléctrica",
             "zh": "电气工程 / 第 1 学期 / 电气工程基础"},
    "basis": "elektrotechnik/1-semester/grundlagen-der-elektrotechnik",
    "order": 1100000,
    "hefte": {
        1: ("Kap1_Feld", "ladung-feld-und-potenzial",
            {"de": "Ladung, Feld und Potenzial", "en": "Charge, Field and Potential",
             "es": "Carga, campo y potencial", "zh": "电荷、电场与电位"}),
        2: ("Kap2_Stromkreis", "strom-widerstand-und-kirchhoff",
            {"de": "Strom, Widerstand und Kirchhoff", "en": "Current, Resistance and Kirchhoff's Laws",
             "es": "Corriente, resistencia y leyes de Kirchhoff", "zh": "电流、电阻与基尔霍夫定律"}),
        3: ("Kap3_Kondensator", "der-kondensator",
            {"de": "Der Kondensator", "en": "The Capacitor", "es": "El condensador", "zh": "电容器"}),
        4: ("Kap4_Messen", "strom-und-spannung-messen",
            {"de": "Strom und Spannung messen", "en": "Measuring Current and Voltage",
             "es": "Medir corriente y tensión", "zh": "电流与电压的测量"}),
        5: ("Kap5_Ersatzquellen", "quellen-und-ersatzquellen",
            {"de": "Quellen und Ersatzquellen", "en": "Sources and Equivalent Sources",
             "es": "Fuentes y fuentes equivalentes", "zh": "电源与等效电源"}),
        6: ("Kap6_Zweitore", "zweitore",
            {"de": "Zweitore", "en": "Two-Port Networks", "es": "Cuadripolos", "zh": "二端口网络"}),
        7: ("Kap7_Leistung", "leistung-und-anpassung",
            {"de": "Leistung, Anpassung und Wirkungsgrad", "en": "Power, Matching and Efficiency",
             "es": "Potencia, adaptación y rendimiento", "zh": "功率、匹配与效率"}),
        8: ("Kap8_Netzwerkanalyse", "maschenstrom-und-knotenpotential",
            {"de": "Maschenstrom- und Knotenpotentialverfahren", "en": "Mesh Current and Node Voltage Analysis",
             "es": "Análisis por mallas y por nudos", "zh": "网孔电流法与节点电位法"}),
        9: ("Kap9_Dioden", "halbleiter-und-dioden",
            {"de": "Halbleiter und Dioden", "en": "Semiconductors and Diodes",
             "es": "Semiconductores y diodos", "zh": "半导体与二极管"}),
        10: ("Kap10_Bipolartransistor", "der-bipolartransistor",
             {"de": "Der Bipolartransistor", "en": "The Bipolar Transistor", "es": "El transistor bipolar", "zh": "双极型晶体管"}),
        11: ("Kap11_OPV", "der-operationsverstaerker",
             {"de": "Der Operationsverstärker", "en": "The Operational Amplifier",
              "es": "El amplificador operacional", "zh": "运算放大器"}),
    },
}

# Wörter, die in den Präambeln der Hefte stehen
WORT = {
    "de": {"aufgabe": "Aufgabe", "satz": "Satz", "definition": "Definition"},
    "en": {"aufgabe": "Exercise", "satz": "Theorem", "definition": "Definition"},
    "es": {"aufgabe": "Ejercicio", "satz": "Teorema", "definition": "Definición"},
    "zh": {"aufgabe": "练习", "satz": "定理", "definition": "定义"},
}
KERN_TITEL = ("Das Wichtigste", "Key points", "Lo esencial", "要点", "本册要点")
SO_ARBEITEST = re.compile(r"^(So arbeitest du|How to work with|Cómo trabajar con|如何使用)")
HINWEIS = {
    "de": "**So arbeitest du mit dem Artikel.** Jede Stufe hat die Idee, typische Fragen mit aufklappbaren Antworten und "
          "Aufgaben (★ bis ★★★). Versuche die Aufgaben zuerst selbst, die Lösung klappst du direkt unter der Aufgabe auf.",
    "en": "**How to work with this article.** Each stage has the idea, typical questions with answers you can expand, and "
          "exercises (★ to ★★★). Try the exercises yourself first; the solution expands right below each exercise.",
    "es": "**Cómo trabajar con este artículo.** Cada etapa tiene la idea, preguntas típicas con respuestas desplegables y "
          "ejercicios (de ★ a ★★★). Intenta resolverlos primero por tu cuenta; la solución se despliega justo debajo de cada ejercicio.",
    "zh": "**如何使用本文。**每个阶段包括基本思路、可展开解答的典型问题以及练习（★ 到 ★★★）。请先自己尝试，解答可在每道练习下方展开。",
}
# Was nur im PDF stimmt. Reihenfolge: längere Wendungen zuerst.
WEBTEXT = {
    "de": [("Dieses Heft", "Dieser Artikel"), ("für dieses Heft", "für diesen Artikel"), ("für dieses Hefts", "für diesen Artikel"),
           ("dieses Hefts", "dieses Artikels"), ("dieses Heft", "dieser Artikel"), ("diesem Heft", "diesem Artikel"),
           ("des Hefts", "des Artikels"), ("im Heft", "im Artikel"), ("dem Heft", "dem Artikel"), ("das Heft", "der Artikel"),
           ("Das Heft", "Der Artikel"), ("Heft ", "Artikel "), ("Heft:", "Artikel:"), ("Heft.", "Artikel."), ("Heft,", "Artikel,"),
           ("Hefte", "Artikel")],
    "en": [("this workbook", "this article"), ("This workbook", "This article"), ("the workbook", "the article"),
           ("The workbook", "The article"), ("workbook", "article")],
    "es": [("este cuaderno", "este artículo"), ("Este cuaderno", "Este artículo"), ("del cuaderno", "del artículo"),
           ("el cuaderno", "el artículo"), ("El cuaderno", "El artículo"), ("cuaderno", "artículo")],
    "zh": [("本册", "本文")],
}
TEIL_RE = {"de": r"\bTeil(?:e|en)?[ \u00a0](\d+)\b", "en": r"\bPart[ \u00a0](\d+)\b", "es": r"\b[Pp]arte[ \u00a0](\d+)\b",
           "zh": r"第[ \u00a0]?(\d+)[ \u00a0]?部分"}

# ----------------------------------------------------------------------------- LaTeX lesen -------
# Mathe-Umgebungen stehen auch in $...$ im Fließtext (pmatrix, cases): Sie sind keine Blöcke.
TOK = re.compile(r"\\begin\{(?!pmatrix|bmatrix|vmatrix|matrix|smallmatrix|cases|aligned|array|gathered|split)([A-Za-z]+\*?)\}|\\(section|subsection)(\*?)\{|\\paragraph\{|\\\[|\\loesung\{|\\captionof\{|\\caption\{|\\par\b")
TEXT_IGNORE = {"bigskip", "medskip", "smallskip", "noindent", "clearpage", "newpage", "centering", "small", "footnotesize",
               "large", "Large", "LARGE", "normalsize", "bfseries", "itshape", "raggedright", "thispagestyle", "tableofcontents",
               "ignorespaces", "protect", "sloppy", "linebreak", "pagebreak", "nopagebreak", "allowbreak", "scriptsize", "newline"}
TEXT_IGNORE_ARG = {"vspace", "hspace", "addcontentsline3", "pagestyle", "setcounter2", "thispagestyle"}
SIMPLE_TEXT = {"ldots": "…", "dots": "…", "textmu": "µ", "S": "§", "textendash": "–", "textemdash": "—", "quad": " ", "qquad": "  ",
               "degree": "°", "textdegree": "°", "stern": "★"}


def strip_comments(s):
    return re.sub(r"(?<!\\)%.*", "", s)


def group(s, i):
    """s[i] == '{': (Inhalt, Position hinter der schließenden Klammer)."""
    assert s[i] == "{", s[i:i + 40]
    d, j = 0, i
    while j < len(s):
        c = s[j]
        if c == "\\":
            j += 2
            continue
        if c == "{":
            d += 1
        elif c == "}":
            d -= 1
            if d == 0:
                return s[i + 1:j], j + 1
        j += 1
    raise ValueError("Klammer offen: " + s[i:i + 60])


def bracket(s, i):
    """Optionales [..] ab i: (Inhalt oder None, neue Position)."""
    j = i
    while j < len(s) and s[j] in " \n":
        j += 1
    if j < len(s) and s[j] == "[":
        d, k = 0, j
        while k < len(s):
            if s[k] == "{":
                d += 1
            elif s[k] == "}":
                d -= 1
            elif s[k] == "]" and d == 0:
                return s[j + 1:k], k + 1
            k += 1
    return None, i


def env_end(s, name, i):
    """i hinter \\begin{name}: (Inhalt, Position hinter \\end{name}), verschachtelt gleichnamige richtig."""
    rx = re.compile(r"\\(begin|end)\{" + re.escape(name) + r"\}")
    d, j = 1, i
    while True:
        m = rx.search(s, j)
        if not m:
            raise ValueError("\\end{%s} fehlt: %s" % (name, s[i:i + 60]))
        d += 1 if m.group(1) == "begin" else -1
        j = m.end()
        if d == 0:
            return s[i:m.start()], j


class Heft:
    def __init__(self, lang, kap, szenen, labels=None, basis=None):
        self.lang, self.kap, self.szenen = lang, kap, szenen
        self.labels = labels or {}
        self.neu = {}                                # label -> (Nummer, Anker), in diesem Durchlauf vergeben
        self.fehlt = set()
        self.unbekannt = {}
        self.basis = basis or {}
        self.sec = self.eq = self.thm = self.sub = self.fig = self.aufg = 0
        self.last = ("", "")
        self.sol = {}
        self.fb = []
        self.h2 = 0

    # ------------------------------------------------------------------ Verweise ----
    def setlabel(self, name):
        self.neu[name] = self.last

    def ref(self, name, paren=False, link=True):
        num, anchor = self.labels.get(name, ("?", ""))
        if name not in self.labels:
            self.fehlt.add(name)
        txt = "(%s)" % num if paren else str(num)
        return "[%s](#%s)" % (txt, anchor) if link and anchor else txt

    # --------------------------------------------------------------------- Formeln ----
    def math(self, m):
        m = m.replace("\n", " ")
        m = re.sub(r"\\label\{[^{}]*\}", "", m)
        m = re.sub(r"\\eqref\{([^{}]*)\}", lambda x: self.ref(x.group(1), paren=True, link=False), m)
        m = re.sub(r"\\ref\{([^{}]*)\}", lambda x: self.ref(x.group(1), link=False), m)
        m = re.sub(r"\\nonumber\b", r"\\notag", m)
        while True:                                     # \un{...}, auch mit Klammern darin: \un{\frac{m}{s}}
            k = re.search(r"\\un\s*\{", m)
            if not k:
                break
            inner, e = group(m, k.end() - 1)
            m = m[:k.start()] + r"\,\mathrm{" + inner + "}" + m[e:]
        m = re.sub(r"\\un\s+(\\?[A-Za-z]+)", r"\\,\\mathrm{\1}", m)
        m = re.sub(r"\\text\{\\textmu\s*([^{}]*)\}", r"\\mu\\text{\1}", m)
        for a, b in ((r"\dd", r"\mathrm{d}"), (r"\ee", r"\mathrm{e}"), (r"\jj", r"\mathrm{j}"), (r"\Lap", r"\mathcal{L}"),
                     (r"\Four", r"\mathcal{F}"), (r"\Re", r"\operatorname{Re}"), (r"\Im", r"\operatorname{Im}"),
                     (r"\Res", r"\operatorname*{Res}"), (r"\eps", r"\varepsilon"), (r"\textmu", r"\mu ")):
            m = re.sub(re.escape(a) + r"(?![a-zA-Z])", lambda _: b, m)
        return re.sub(r" {2,}", " ", m).strip()

    def display(self, inner, labels=(), tag=None):
        anchors = ""
        if tag:
            anchors = '<span class="anker" id="gl-%s"></span>\n' % tag.replace(".", "-")
        return anchors + "$$" + self.math(inner) + ((r" \tag{%s}" % tag) if tag else "") + "$$"

    def equation(self, body):
        self.eq += 1
        num = "%d.%d" % (self.sec, self.eq)
        self.last = (num, "gl-" + num.replace(".", "-"))
        for lb in re.findall(r"\\label\{([^{}]*)\}", body):
            self.setlabel(lb)
        return self.display(body, tag=num)

    def align(self, body):
        """Jede Zeile hat ihre Nummer wie in LaTeX; auf der Website stehen sie gemeinsam neben dem Block (\tag{2.3|2.4})."""
        rows = re.split(r"(?<=\\\\)", body)
        anchors, nums, out = [], [], []
        for r in rows:
            if not r.strip():
                continue
            if re.search(r"\\nonumber|\\notag", r):
                out.append(re.sub(r"\\nonumber|\\notag", "", r))
                continue
            self.eq += 1
            num = "%d.%d" % (self.sec, self.eq)
            self.last = (num, "gl-" + num.replace(".", "-"))
            for lb in re.findall(r"\\label\{([^{}]*)\}", r):
                self.setlabel(lb)
            anchors.append('<span class="anker" id="%s"></span>' % self.last[1])
            nums.append(num)
            out.append(r)
        return "\n".join(anchors) + "\n$$" + self.math(r"\begin{aligned}" + "".join(out) + r"\end{aligned}") + r" \tag{%s}$$" % "|".join(nums)

    # ----------------------------------------------------------------- Fließtext ----
    def text(self, s):
        out, i, n = [], 0, len(s)
        while i < n:
            c = s[i]
            if c == "$":
                j = i + 1
                while j < n and s[j] != "$":
                    j += 2 if s[j] == "\\" else 1
                out.append("$" + self.math(s[i + 1:j]) + "$")
                i = j + 1
            elif c == "\\":
                m = re.match(r"\\([a-zA-Z]+)(\*?)|\\(.)", s[i:], re.S)
                if m.group(3) is not None:
                    ch = m.group(3)
                    i += 2
                    out.append({" ": " ", ",": THIN, ";": " ", "\n": " ", "\\": " ", "-": "", "/": ""}.get(ch, ch))
                    continue
                name = m.group(1)
                i += len(m.group(0))
                r, i = self.macro(name, s, i)
                out.append(r)
            elif c in "{}":
                i += 1
            elif c == "~":
                out.append(NBSP); i += 1
            elif s.startswith("---", i):
                out.append("—"); i += 3
            elif s.startswith("--", i):
                out.append("–"); i += 2
            elif s.startswith("``", i):
                out.append("“"); i += 2
            elif s.startswith("''", i):
                out.append("”"); i += 2
            elif c == "\n":
                out.append(" "); i += 1
            else:
                out.append(c); i += 1
        return re.sub(r" {2,}", " ", "".join(out)).strip()

    def macro(self, name, s, i):
        def arg(k=i):
            while s[k] in " \n":
                k += 1
            return group(s, k)
        if name == "textbf":
            a, j = arg()
            return "**" + self.text(a) + "**", j
        if name in ("emph", "textit"):
            a, j = arg()
            return "*" + self.text(a) + "*", j
        if name == "fb":
            a, j = arg()
            t = self.text(a)
            if "$" not in t:
                self.fb.append(t)
            return "__" + t + "__", j
        if name == "texttt":
            a, j = arg()
            a = re.sub(r"\\([{}_%&#$])", r"\1", a).replace("\\textbackslash", "\\").replace("~", " ")
            return "`" + a + "`", j
        if name == "uline":
            a, j = arg()
            return self.text(a), j
        if name == "texorpdfstring":
            a, j = arg()
            _, j = arg(j)
            return self.text(a), j
        if name == "url":
            a, j = arg()
            return "[%s](%s)" % (a, a), j
        if name == "href":
            a, j = arg()
            b, j = arg(j)
            return "[%s](%s)" % (self.text(b), a), j
        if name == "label":
            a, j = arg()
            self.setlabel(a)
            return "", j
        if name in ("ref", "eqref"):
            a, j = arg()
            return self.ref(a, paren=name == "eqref"), j
        if name in TEXT_IGNORE_ARG:
            a, j = arg()
            return "", j
        if name == "addcontentsline":
            _, j = arg()
            _, j = arg(j)
            _, j = arg(j)
            return "", j
        if name in SIMPLE_TEXT:
            if s[i:i + 2] == "{}":
                i += 2
            return SIMPLE_TEXT[name], i
        if name in TEXT_IGNORE:
            return "", i
        self.unbekannt[name] = self.unbekannt.get(name, 0) + 1
        return "", i

    def para(self, s):
        """Fließtext zwischen zwei Blöcken -> Absätze, je eine Zeile."""
        out = []
        for p in re.split(r"\n\s*\n", s):
            t = self.text(p)
            if t:
                if re.match(r"(\d+\.\s|[-*>|#]|<|:::)", t):     # liefe sonst als Markdown-Block
                    t = "\u2060" + t
                out.append(t)
        return out

    # ---------------------------------------------------------------------- Blöcke ----
    def block(self, s):
        out, i = [], 0
        pending = ""                                    # \paragraph{..}: fett vor den nächsten Absatz
        def add_text(t):
            nonlocal pending
            ps = self.para(t)
            if pending and ps:
                ps[0] = pending + " " + ps[0]
                pending = ""
            elif pending and not ps:
                return
            out.extend(ps)
        while True:
            m = TOK.search(s, i)
            if not m:
                add_text(s[i:])
                break
            add_text(s[i:m.start()])
            if pending:
                out.append(pending)
                pending = ""
            tok = m.group(0)
            if tok.startswith("\\begin"):
                name = m.group(1)
                body, j = env_end(s, name, m.end())
                out.append(self.environment(name, body))
                i = j
            elif tok.startswith(("\\section", "\\subsection")):
                title, j = group(s, m.end() - 1)
                out.append(self.heading(m.group(2), bool(m.group(3)), title))
                i = j
            elif tok == "\\paragraph{":
                title, j = group(s, m.end() - 1)
                t = self.text(title)
                i = j
                if SO_ARBEITEST.match(t):                    # gilt nur fürs PDF: durch den Website-Hinweis ersetzen
                    e = re.search(r"\n\s*\n", s[i:])
                    i = i + e.end() if e else len(s)
                    out.append(HINWEIS[self.lang])
                    continue
                pending = "**" + t + "**"
            elif tok == "\\[":
                j = s.index("\\]", m.end())
                out.append(self.display(s[m.end():j]))
                i = j + 2
            elif tok == "\\loesung{":
                name, j = group(s, m.end() - 1)
                e = re.compile(r"\\loesung\{|\\section").search(s, j)
                end = e.start() if e else len(s)
                self.sol[name] = self.block(s[j:end])
                i = end
            elif tok.startswith("\\caption"):            # nur außerhalb von abb: \captionof in center
                j = m.end() - 1
                if tok == "\\captionof{":
                    _, j = group(s, j)
                cap, j = group(s, j)
                out.append(self.figure(cap, s[j:j + 80]))
                i = j
                lm = re.match(r"\s*\\label\{[^{}]*\}", s[i:])
                if lm:
                    i += lm.end()
            else:                                        # \par
                i = m.end()
        return "\n\n".join(x for x in out if x)

    def heading(self, kind, star, title):
        t = self.text(title)
        if kind == "section" and not star:
            self.sec += 1
            self.eq = self.thm = self.sub = 0
            self.last = (str(self.sec), "stufe-%d" % self.sec)
            if re.match(r"(Lösungen|Solutions|Soluciones|解答)\s*$", t):
                return ""                                # stehen direkt bei den Aufgaben
            return "## %s\n\n<span class=\"anker\" id=\"stufe-%d\"></span>" % (t, self.sec)
        if kind == "section":
            return "## " + t
        self.sub += 1
        self.last = ("%d.%d" % (self.sec, self.sub), "stufe-%d-%d" % (self.sec, self.sub))
        return '### %s\n\n<span class="anker" id="%s"></span>' % (t, self.last[1])

    def figure(self, cap, after):
        self.fig += 1
        self.last = (str(self.fig), "abb-%d" % self.fig)
        lm = re.match(r"\s*\\label\{([^{}]*)\}", after)
        name = lm.group(1) if lm else "abb%d" % self.fig
        if lm:
            self.setlabel(lm.group(1))
        return self._abb(name, cap)

    def _abb(self, label, cap):
        n = re.sub(r"^fig:", "", label)
        if not re.match(r"k\d", n):
            n = "k%d%s" % (self.kap, n)
        return ":::abbildung %s/%s\n%s\n:::" % (self.szenen, n, self.text(cap))

    def environment(self, name, body):
        if name == "equation":
            return self.equation(body)
        if name == "align":
            return self.align(body)
        if name in ("equation*", "align*", "gather*", "gather"):
            inner = "aligned" if name.startswith("align") else "gathered" if name.startswith("gather") else None
            b = body if inner is None else r"\begin{%s}%s\end{%s}" % (inner, body, inner)
            return self.display(b)
        if name in ("itemize", "enumerate"):
            return self.lst(name, body)
        if name == "center":
            return self.block(body)
        if name == "tikzpicture":                        # Bild aus dem Editor, siehe :::abbildung
            return ""
        if name in ("tabularx", "tabular"):
            return self.table(name, body)
        if name == "abb":
            return self.abb(body)
        if name == "zweck":
            return ":::zweck\n%s\n:::" % self.block(body)
        if name == "analogie":
            return ":::analogie\n%s\n:::" % self.block(body)
        if name in ("merkbox", "kernbox", "herleitung", "vertiefung", "frage", "qa", "ltspice"):
            t, j = group(body, body.index("{"))
            title = self.text(t)
            inner = self.block(body[j:])
            kind = {"merkbox": "merke", "kernbox": "kern" if title in KERN_TITEL else "merke", "herleitung": "herleitung",
                    "vertiefung": "zusatz", "frage": "frage", "qa": "frage", "ltspice": "ltspice"}[name]
            return ":::%s %s\n%s\n:::" % (kind, title, inner)
        if name in ("satz", "definition"):
            opt, j = bracket(body, 0)
            self.thm += 1
            num = "%d.%d" % (self.sec, self.thm)
            self.last = (num, "satz-" + num.replace(".", "-"))
            anchor = '<span class="anker" id="%s"></span>' % self.last[1]
            head = "%s %s" % (WORT[self.lang][name], num)
            if opt:
                head += " (" + self.text(opt) + ")"
            return ":::%s %s\n%s\n\n%s\n:::" % (name, head, anchor, self.block(body[j:]))
        if name in ("aufgabe", "aufgabeplus"):
            j = 0
            plus = "a"
            if name == "aufgabeplus":
                opt, j = bracket(body, 0)
                plus = opt or "a"
            t, j = group(body, body.index("{", j))
            if name == "aufgabe":
                self.aufg += 1
                num = str(self.aufg)
            else:
                num = "%d%s" % (self.aufg, plus)
            self.last = (num, "aufg-" + num)
            lm = re.match(r"\s*\\label\{([^{}]*)\}", body[j:])
            lab = None
            if lm:
                lab = lm.group(1)
                self.setlabel(lab)
                j += lm.end()
            head = "%s %s %s" % (WORT[self.lang]["aufgabe"], num, self.text(t))
            return ':::aufgabe %s\n<span class="anker" id="aufg-%s"></span>\n\n%s\n\n@@LOESUNG:%s@@\n:::' % (head, num, self.block(body[j:]), lab)
        self.unbekannt["env:" + name] = self.unbekannt.get("env:" + name, 0) + 1
        return ""

    def abb(self, body):
        m = re.search(r"\\caption\{", body)
        cap, j = group(body, m.end() - 1)
        self.fig += 1
        self.last = (str(self.fig), "abb-%d" % self.fig)
        lm = re.search(r"\\label\{([^{}]*)\}", body[j:])
        label = lm.group(1) if lm else "abb%d" % self.fig
        if lm:
            self.setlabel(label)
        return self._abb(label, cap)

    def lst(self, name, body):
        opt, st = bracket(body, 0)
        cls = ' class="al"' if name == "enumerate" and opt and "alph" in opt else ""
        tag = "ol" if name == "enumerate" else "ul"
        pos, d = [], 0
        for m in re.finditer(r"\\begin\{(itemize|enumerate)\}|\\end\{(itemize|enumerate)\}|\\item\b", body):
            if m.group(1):
                d += 1
            elif m.group(2):
                d -= 1
            elif d == 0:
                pos.append(m)
        out = ["<%s%s>" % (tag, cls)]
        for k, m in enumerate(pos):
            end = pos[k + 1].start() if k + 1 < len(pos) else len(body)
            item = body[m.end():end]
            lab, sk = bracket(item, 0)
            if lab is not None and lab.strip():
                item = "\\textbf{" + lab + "} " + item[sk:]
            out += ["<li>", self.block(item), "</li>"]
        out.append("</%s>" % tag)
        return "\n\n".join(out)

    def table(self, name, body):
        i = 0
        if name == "tabularx":
            _, i = group(body, body.index("{"))
        _, i = group(body, body.index("{", i))
        b = body[i:]
        parts = re.split(r"\\midrule", b)
        head = parts[0] if len(parts) > 1 else ""
        rest = "\\midrule".join(parts[1:]) if len(parts) > 1 else b
        rest = re.sub(r"\\(toprule|bottomrule|midrule|hline)\b", "", rest)
        head = re.sub(r"\\(toprule|bottomrule|hline)\b", "", head)

        def rows(t):
            r = []
            for row in re.split(r"\\\\", t):
                if row.strip():
                    r.append([self.cell(c) for c in re.split(r"(?<!\\)&", row)])
            return r
        hr, br = rows(head), rows(rest)
        ncol = max(len(x) for x in hr + br)
        hdr = hr[0] if hr else [""] * ncol
        lines = ["| " + " | ".join(hdr) + " |", "|" + "---|" * ncol]
        lines += ["| " + " | ".join(r + [""] * (ncol - len(r))) + " |" for r in br]
        return "\n".join(lines)

    def cell(self, c):
        t = self.text(c)
        def bar(m):
            return re.sub(r"\\\|", r"\\Vert ", m.group(0)).replace("|", r"\vert ")
        return re.sub(r"\$[^$]*\$", bar, t)


# --------------------------------------------------------------------------------- Ein Heft ----
def read_tex(folder, name):
    s = strip_comments((folder / (name + ".tex")).read_text(encoding="utf-8"))
    s = re.sub(r"^\\(pgfmathdeclarefunction|markboth)\b.*$", "", s, flags=re.M)     # gehören zum Satz im PDF
    return re.sub(r"\\input\{([^{}]*)\}", lambda m: read_tex(folder, m.group(1)) if m.group(1) != "praeambel" and not m.group(1).startswith("praeambel") else "", s)


def titel(s):
    t = re.search(r"\{\\LARGE\\bfseries\s*(.*?)\\par\}", s, re.S)
    u = re.search(r"\{\\large\s*(.*?)\\par\}", s, re.S)
    clean = lambda x: re.sub(r"\s+", " ", x.replace("\\\\", " ").replace("~", " ")).strip()
    return clean(t.group(1)), clean(u.group(1)) if u else ""


def convert(cfg, kap, lang):
    stem, slug, thema = cfg["hefte"][kap]
    name = stem + ("" if lang == "de" else "_" + lang)
    src = read_tex(cfg["quelle"], name)
    head = re.search(r"\\begin\{document\}(.*)\\end\{document\}", src, re.S).group(1)
    tt, sub = titel(head)
    body = re.sub(r"\\begin\{center\}.*?\\end\{center\}", "", head, count=1, flags=re.S)

    def run(labels):
        h = Heft(lang, kap, cfg["szenen"], labels)
        return h, h.block(body)
    h, _ = run({})
    h, md = run(h.neu)
    for lab, sol in h.sol.items():
        md = md.replace("@@LOESUNG:%s@@" % lab, ":::loesung\n%s\n:::" % sol)
    rest = re.findall(r"@@LOESUNG:([^@]*)@@", md)
    md = re.sub(r"@@LOESUNG:[^@]*@@\n?", "", md)
    teile = "/wissen/%s%s" % ("" if lang == "de" else lang + "/", cfg["basis"])
    return h, md, tt, sub, rest, teile


def webtext(md, lang, cfg, teile):
    """Texte anpassen, die nur im PDF stimmen; „Teil 3“ wird zum Link. Formeln, Code, Überschriften und Blockköpfe bleiben."""
    def subs(t):
        for a, b in WEBTEXT[lang]:
            t = t.replace(a, b)
        return t
    def link(m):
        k = int(m.group(1))
        if k not in cfg["hefte"]:
            return m.group(0)
        _, slug, thema = cfg["hefte"][k]
        return "[%s](%s/%s/%s.html)" % (m.group(0), teile, slugify(thema["de"]), slug)
    out = []
    for line in md.split("\n"):
        plain = line.startswith(("#", ":::", "<", "|", "$$"))
        pieces = re.split(r"(\$\$.*?\$\$|\$[^$]*\$|`[^`]*`|\]\([^)]*\))", line)
        for i in range(0, len(pieces), 2):
            pieces[i] = subs(pieces[i])
            if not plain:
                pieces[i] = re.sub(TEIL_RE[lang], link, pieces[i])
        out.append("".join(pieces))
    return "\n".join(out)


def tags(h):
    seen = []
    for t in h.fb:
        t = re.sub(r"[*_`]", "", t)
        if t and t not in seen and "," not in t:
            seen.append(t)
    return ", ".join(seen[:8])


def artikel(cfg, kap, lang):
    stem, slug, thema = cfg["hefte"][kap]
    h, md, tt, sub, rest, teile = convert(cfg, kap, lang)
    md = webtext(md, lang, cfg, teile)
    kopf = ["---", "title: " + tt, "pfad: %s / %s" % (cfg["pfad"][lang], thema[lang]), "order: %d" % (cfg["order"] + kap * 10000 + 100),
            "summary: " + sub, "tags: " + tags(h), "lang: " + lang, "---", ""]
    return "\n".join(kopf) + "\n" + md + "\n", h, rest


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("modul", choices=sorted(MODULE))
    ap.add_argument("--kap", type=int, nargs="*")
    ap.add_argument("--lang", nargs="*", default=list(LANGS))
    ap.add_argument("--pruefen", action="store_true")
    ap.add_argument("--aux", help="Ordner mit .aux-Dateien: Nummern vergleichen")
    ap.add_argument("--katex", action="store_true", help="alle Formeln mit KaTeX rendern (Fehler melden)")
    a = ap.parse_args()
    cfg = MODULE[a.modul]
    fehler = 0
    alle = []
    for kap in a.kap or sorted(cfg["hefte"]):
        stem, slug, thema = cfg["hefte"][kap]
        for lang in a.lang:
            txt, h, rest = artikel(cfg, kap, lang)
            alle.append(txt)
            ordner = ROOT / "content" / cfg["ziel"] / ("%02d-%s" % (kap, slug))
            datei = ordner / ("01-%s%s.md" % (slug, "" if lang == "de" else "." + lang))
            msg = []
            if h.fehlt:
                msg.append("Verweise ohne Ziel: " + ", ".join(sorted(h.fehlt)))
            if h.unbekannt:
                msg.append("unbekannt: " + ", ".join("%s×%d" % kv for kv in sorted(h.unbekannt.items())))
            if rest:
                msg.append("Aufgaben ohne Lösung: " + ", ".join(rest))
            ungenutzt = [l for l in h.sol if ("@@LOESUNG:%s@@" % l) not in txt and l not in h.neu]
            if ungenutzt:
                msg.append("Lösungen ohne Aufgabe: " + ", ".join(ungenutzt))
            if a.aux:
                msg += aux_vergleich(Path(a.aux) / ((stem + ("" if lang == "de" else "_" + lang)) + ".aux"), h)
            if not a.pruefen:
                ordner.mkdir(parents=True, exist_ok=True)
                datei.write_text(txt, encoding="utf-8", newline="\n")
            print(("⚠ " if msg else "✓ ") + "Teil %d %s: %d Zeichen, %d Abb., %d Aufg." % (kap, lang, len(txt), h.fig, h.aufg))
            for x in msg:
                print("    " + x)
                fehler += 1
    if a.katex:
        for t, e in katex_pruefen(alle):
            print("⚠ KaTeX:", t, "\n    ", e)
            fehler += 1
    return 1 if fehler else 0


def katex_pruefen(texte):
    """Rendert alle Formeln mit dem KaTeX der Website und gibt [(Formel, Fehler)] zurück (braucht Playwright und Netz)."""
    from playwright.sync_api import sync_playwright
    items = []
    for s in texte:
        s = re.sub(r"`[^`]*`", "", s)
        items += [(x, True) for x in re.findall(r"\$\$(.+?)\$\$", s, re.S)]
        items += [(x, False) for x in re.findall(r"\$([^$\n]+)\$", re.sub(r"\$\$.+?\$\$", " ", s, flags=re.S))]
    js = ("(items) => { const bad = []; for (const [t, d] of items) { try { katex.renderToString(t.replace(/\\\\tag\\{[^{}]*\\}/, ''), "
          "{displayMode: d, throwOnError: true, strict: false}); } catch (e) { bad.push([t.slice(0, 120), e.message.slice(0, 160)]); } } return bad; }")
    with sync_playwright() as p:
        b = p.chromium.launch()
        pg = b.new_page()
        pg.set_content("<html><body></body></html>")
        pg.add_script_tag(url="https://cdnjs.cloudflare.com/ajax/libs/KaTeX/0.16.11/katex.min.js")
        bad = pg.evaluate(js, items)
        b.close()
    print(len(items), "Formeln mit KaTeX geprüft,", len(bad), "Fehler")
    return bad


def aux_vergleich(path, h):
    if not path.is_file():
        return ["keine aux-Datei: " + path.name]
    s = path.read_text(encoding="utf-8", errors="replace")
    diff = []
    for m in re.finditer(r"\\newlabel\{([^{}]*)\}\{\{([^{}]*)\}", s):
        name, num = m.group(1), m.group(2)
        if name.endswith("@cref") or name not in h.neu:
            continue
        if str(h.neu[name][0]) != num:
            diff.append("%s: LaTeX %s, Umwandler %s" % (name, num, h.neu[name][0]))
    return diff


if __name__ == "__main__":
    sys.exit(main())
