"""Arbeitshefte (LaTeX) -> Website-Artikel (Markdown für build_wissen.py), in allen vier Sprachen.

Aufruf (vom Repo-Root):
    python tools/heft_zu_artikel.py et3                 alle Hefte des Moduls
    python tools/heft_zu_artikel.py et3 --kap 1 3       nur diese Hefte
    python tools/heft_zu_artikel.py et3 --pruefen       nichts schreiben, nur Meldungen
    python tools/heft_zu_artikel.py et3 --aux DIR       Nummern gegen die .aux-Dateien in DIR prüfen

Das Heft bleibt die Quelle: Kap<N>_<Name>[_en|_es|_zh].tex mit den \\input-Dateien. Die Artikel werden daraus erzeugt und
nie von Hand geändert. Ein Heft wird zu einem Kapitel aus mehreren kurzen Artikeln: Überblick, je Stufe ein Artikel, zum
Schluss „Das Wichtigste“. Man soll einen Abschnitt abschließen können, bevor der nächste beginnt. Nummern (Gleichungen, Sätze, Abbildungen, Aufgaben) entstehen wie in LaTeX, Verweise werden zu
Links. Aufgaben bekommen ihre Lösung direkt als aufklappbaren Block, nicht am Ende. Abbildungen werden zu
:::abbildung <szene>, die Szene heißt wie das \\label (fig:k1bode -> et3/k1bode). Texte, die nur im PDF stimmen
(„Lösungen am Ende“, „dieses Heft“), werden je Sprache angepasst (WEBTEXT).

Ziel: content/<modul>/<NN-kapitel>/<NN-stufe>[.en|.es|.zh].md (die Dateinamen kommen immer aus der deutschen Fassung).
"""
import argparse
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))
sys.stdout.reconfigure(encoding="utf-8")
from build_wissen import slugify, caption_alt  # noqa: E402

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

MODULE["hm1"] = {
    "quelle": Path(r"C:\Bücher\HöMa1\Arbeitshefte"),
    "ziel": "hm1",
    "szenen": "hm1",
    "pfad": {"de": "Elektrotechnik / 1. Semester / Höhere Mathematik 1",
             "en": "Electrical Engineering / 1st Semester / Higher Mathematics 1",
             "es": "Ingeniería eléctrica / 1.er semestre / Matemáticas superiores 1",
             "zh": "电气工程 / 第 1 学期 / 高等数学 1"},
    "basis": "elektrotechnik/1-semester/hohere-mathematik-1",
    "order": 1200000,
    "hefte": {
        1: ("Kap1_Zahlen", "mengen-logik-und-reelle-zahlen",
            {"de": "Mengen, Logik und reelle Zahlen", "en": "Sets, Logic and Real Numbers",
             "es": "Conjuntos, lógica y números reales", "zh": "集合、逻辑与实数"}),
        2: ("Kap2_Komplex", "komplexe-zahlen",
            {"de": "Komplexe Zahlen", "en": "Complex Numbers", "es": "Números complejos", "zh": "复数"}),
        3: ("Kap3_Funktionen", "funktionen-und-polynome",
            {"de": "Funktionen und Polynome", "en": "Functions and Polynomials",
             "es": "Funciones y polinomios", "zh": "函数与多项式"}),
        4: ("Kap4_Folgen", "folgen-und-grenzwerte",
            {"de": "Folgen und Grenzwerte", "en": "Sequences and Limits", "es": "Sucesiones y límites", "zh": "数列与极限"}),
        5: ("Kap5_Stetigkeit", "exponentialfunktion-und-stetigkeit",
            {"de": "Exponentialfunktion und Stetigkeit", "en": "Exponential Function and Continuity",
             "es": "Función exponencial y continuidad", "zh": "指数函数与连续性"}),
        6: ("Kap6_Reihen", "unendliche-reihen",
            {"de": "Unendliche Reihen", "en": "Infinite Series", "es": "Series infinitas", "zh": "无穷级数"}),
        7: ("Kap7_Potenzreihen", "potenzreihen-und-eulersche-formel",
            {"de": "Potenzreihen und Eulersche Formel", "en": "Power Series and Euler's Formula",
             "es": "Series de potencias y fórmula de Euler", "zh": "幂级数与欧拉公式"}),
        8: ("Kap8_Vektoren", "vektoren-und-skalarprodukt",
            {"de": "Vektoren und Skalarprodukt", "en": "Vectors and the Dot Product",
             "es": "Vectores y producto escalar", "zh": "向量与内积"}),
        9: ("Kap9_Basen", "vektorprodukt-und-basen",
            {"de": "Vektorprodukt und Basen", "en": "Cross Product and Bases",
             "es": "Producto vectorial y bases", "zh": "向量积与基"}),
        10: ("Kap10_Matrizen", "matrizen-und-gleichungssysteme",
             {"de": "Matrizen und lineare Gleichungssysteme", "en": "Matrices and Linear Systems",
              "es": "Matrices y sistemas lineales", "zh": "矩阵与线性方程组"}),
    },
}

MODULE["gemb1"] = {
    "quelle": Path(r"C:\Bücher\GEMB\Arbeitshefte"),
    "ziel": "gemb1",
    "szenen": "gemb1",
    "pfad": {"de": "Elektrotechnik / 4. Semester / Elektronische Materialien und Bauelemente 1",
             "en": "Electrical Engineering / 4th Semester / Electronic Materials and Devices 1",
             "es": "Ingeniería eléctrica / 4.º semestre / Materiales y dispositivos electrónicos 1",
             "zh": "电气工程 / 第 4 学期 / 电子材料与器件 1"},
    "basis": "elektrotechnik/4-semester/elektronische-materialien-und-bauelemente-1",
    "order": 4100000,
    "hefte": {
        1: ("Kap1_Schroedinger", "welle-teilchen-und-schroedinger-gleichung",
            {"de": "Welle, Teilchen und Schrödinger-Gleichung", "en": "Waves, Particles and the Schrödinger Equation",
             "es": "Ondas, partículas y ecuación de Schrödinger", "zh": "波、粒子与薛定谔方程"}),
        2: ("Kap2_Box", "das-teilchen-in-der-box",
            {"de": "Das Teilchen in der Box", "en": "The Particle in a Box",
             "es": "La partícula en una caja", "zh": "箱中粒子"}),
        3: ("Kap3_Tunnel", "stufe-barriere-und-tunneleffekt",
            {"de": "Stufe, Barriere und Tunneleffekt", "en": "Step, Barrier and Tunnelling",
             "es": "Escalón, barrera y efecto túnel", "zh": "势阶、势垒与隧穿效应"}),
        4: ("Kap4_Atome", "atome-und-orbitale",
            {"de": "Atome und Orbitale", "en": "Atoms and Orbitals",
             "es": "Átomos y orbitales", "zh": "原子与轨道"}),
        5: ("Kap5_Bindung", "chemische-bindung",
            {"de": "Chemische Bindung", "en": "Chemical Bonding",
             "es": "Enlace químico", "zh": "化学键"}),
        6: ("Kap6_Kristall", "kristallgitter",
            {"de": "Kristallgitter", "en": "Crystal Lattices",
             "es": "Redes cristalinas", "zh": "晶格"}),
        7: ("Kap7_Reziprok", "kristallwachstum-und-reziprokes-gitter",
            {"de": "Kristallwachstum und reziprokes Gitter", "en": "Crystal Growth and the Reciprocal Lattice",
             "es": "Crecimiento cristalino y red recíproca", "zh": "晶体生长与倒易点阵"}),
        8: ("Kap8_TightBinding", "vom-atom-zum-band",
            {"de": "Vom Atom zum Band", "en": "From Atom to Band",
             "es": "Del átomo a la banda", "zh": "从原子到能带"}),
        9: ("Kap9_Bandstruktur", "bandstrukturen-lesen",
            {"de": "Bandstrukturen lesen", "en": "Reading Band Structures",
             "es": "Leer estructuras de bandas", "zh": "读懂能带结构"}),
        10: ("Kap10_Fermi", "zustandsdichte-und-fermi-verteilung",
            {"de": "Zustandsdichte und Fermi-Verteilung", "en": "Density of States and Fermi Distribution",
             "es": "Densidad de estados y distribución de Fermi", "zh": "态密度与费米分布"}),
        11: ("Kap11_Halbleiter", "eigenhalbleiter-und-dotierung",
            {"de": "Eigenhalbleiter und Dotierung", "en": "Intrinsic Semiconductors and Doping",
             "es": "Semiconductores intrínsecos y dopado", "zh": "本征半导体与掺杂"}),
        12: ("Kap12_Transport", "strom-im-halbleiter",
            {"de": "Strom im Halbleiter", "en": "Current in Semiconductors",
             "es": "Corriente en el semiconductor", "zh": "半导体中的电流"}),
        13: ("Kap13_Diffusion", "diffusion-rekombination-grundgleichungen",
            {"de": "Diffusion, Rekombination und Grundgleichungen", "en": "Diffusion, Recombination and Basic Equations",
             "es": "Difusión, recombinación y ecuaciones básicas", "zh": "扩散、复合与基本方程"}),
        14: ("Kap14_pn", "der-p-n-uebergang",
            {"de": "Der p-n-Übergang", "en": "The p-n Junction",
             "es": "La unión p-n", "zh": "p-n 结"}),
        15: ("Kap15_MOS", "die-mos-kapazitaet",
            {"de": "Die MOS-Kapazität", "en": "The MOS Capacitor",
             "es": "El condensador MOS", "zh": "MOS 电容"}),
        16: ("Kap16_MOSreal", "realer-mos-kondensator",
            {"de": "Der reale MOS-Kondensator", "en": "The Real MOS Capacitor",
             "es": "El condensador MOS real", "zh": "实际 MOS 电容"}),
        17: ("Kap17_MOSFET", "der-mosfet",
            {"de": "Der MOSFET", "en": "The MOSFET",
             "es": "El MOSFET", "zh": "MOSFET"}),
        18: ("Kap18_Kurzkanal", "skalierung-und-kurzkanaleffekte",
            {"de": "Skalierung und Kurzkanaleffekte", "en": "Scaling and Short-Channel Effects",
             "es": "Escalado y efectos de canal corto", "zh": "按比例缩小与短沟道效应"}),
        19: ("Kap19_Licht", "ergaenzung-licht-und-laser",
            {"de": "Ergänzung: Licht und Laser", "en": "Supplement: Light and Lasers",
             "es": "Complemento: luz y láser", "zh": "补充：光与激光"}),
        20: ("Kap20_Realkristall", "ergaenzung-reale-kristalle",
            {"de": "Ergänzung: Reale Kristalle und amorphe Stoffe", "en": "Supplement: Real Crystals and Amorphous Solids",
             "es": "Complemento: cristales reales y sólidos amorfos", "zh": "补充：实际晶体与非晶固体"}),
        21: ("Kap21_Zustandsdiagramme", "ergaenzung-zustandsdiagramme",
            {"de": "Ergänzung: Zustandsdiagramme", "en": "Supplement: Phase Diagrams",
             "es": "Complemento: diagramas de fases", "zh": "补充：相图"}),
        22: ("Kap22_Vielteilchen", "ergaenzung-vielteilchensysteme",
            {"de": "Ergänzung: Vielteilchensysteme", "en": "Supplement: Many-Particle Systems",
             "es": "Complemento: sistemas de muchas partículas", "zh": "补充：多粒子系统"}),
        23: ("Kap23_Entropie", "ergaenzung-entropie-und-gleichgewicht",
            {"de": "Ergänzung: Entropie und Gleichgewicht", "en": "Supplement: Entropy and Equilibrium",
             "es": "Complemento: entropía y equilibrio", "zh": "补充：熵与平衡"}),
        24: ("Kap24_Gitterschwingungen", "ergaenzung-gitterschwingungen",
            {"de": "Ergänzung: Gitterschwingungen", "en": "Supplement: Lattice Vibrations",
             "es": "Complemento: vibraciones de la red", "zh": "补充：晶格振动"}),
        25: ("Kap25_Metalle", "ergaenzung-metalle",
            {"de": "Ergänzung: Metalle", "en": "Supplement: Metals",
             "es": "Complemento: metales", "zh": "补充：金属"}),
        26: ("Kap26_Schottky", "ergaenzung-metall-halbleiter-uebergang",
            {"de": "Ergänzung: Metall-Halbleiter-Übergang", "en": "Supplement: Metal-Semiconductor Junction",
             "es": "Complemento: unión metal-semiconductor", "zh": "补充：金属-半导体结"}),
        27: ("Kap27_Feldeffekt", "ergaenzung-weitere-feldeffekt-bauelemente",
            {"de": "Ergänzung: Weitere Feldeffekt-Bauelemente", "en": "Supplement: Other Field-Effect Devices",
             "es": "Complemento: otros dispositivos de efecto de campo", "zh": "补充：其他场效应器件"}),
        28: ("Kap28_Prozess", "ergaenzung-halbleitertechnologie",
            {"de": "Ergänzung: Halbleitertechnologie", "en": "Supplement: Semiconductor Technology",
             "es": "Complemento: tecnología de semiconductores", "zh": "补充：半导体工艺"}),
    },
}

MODULE["hm3"] = {
    "quelle": Path(r"C:\Bücher\HöMa3\Arbeitshefte"),
    "ziel": "hm3",
    "szenen": "hm3",
    "pfad": {"de": "Elektrotechnik / 3. Semester / Höhere Mathematik 3",
             "en": "Electrical Engineering / 3rd Semester / Higher Mathematics 3",
             "es": "Ingeniería eléctrica / 3.er semestre / Matemáticas superiores 3",
             "zh": "电气工程 / 第 3 学期 / 高等数学 3"},
    "basis": "elektrotechnik/3-semester/hohere-mathematik-3",
    "order": 3100000,
    "hefte": {
        1: ("Kap1_Vektorfelder", "differentialrechnung-fuer-vektorfelder",
            {"de": "Differentialrechnung für Vektorfelder", "en": "Differential Calculus for Vector Fields",
             "es": "Cálculo diferencial de campos vectoriales", "zh": "矢量场的微分学"}),
        2: ("Kap2_Integrale", "integralrechnung-im-rn",
            {"de": "Integralrechnung im Rⁿ", "en": "Integration in Rⁿ", "es": "Cálculo integral en Rⁿ", "zh": "Rⁿ 中的积分"}),
        3: ("Kap3_Kurvenintegrale", "kurvenintegrale",
            {"de": "Kurvenintegrale", "en": "Line Integrals", "es": "Integrales de línea", "zh": "曲线积分"}),
        4: ("Kap4_Koordinaten", "koordinatentransformationen",
            {"de": "Koordinatentransformationen", "en": "Coordinate Transformations",
             "es": "Transformaciones de coordenadas", "zh": "坐标变换"}),
        5: ("Kap5_Integralsaetze", "integralsaetze-im-raum",
            {"de": "Integralsätze im Raum", "en": "Integral Theorems in Space",
             "es": "Teoremas integrales en el espacio", "zh": "空间中的积分定理"}),
        6: ("Kap6_Funktionenfolgen", "konvergenz-von-funktionenfolgen",
            {"de": "Konvergenz von Funktionenfolgen", "en": "Convergence of Sequences of Functions",
             "es": "Convergencia de sucesiones de funciones", "zh": "函数序列的收敛"}),
        7: ("Kap7_Fourier", "fourier-reihen",
            {"de": "Fourier-Reihen", "en": "Fourier Series", "es": "Series de Fourier", "zh": "傅里叶级数"}),
        8: ("Kap8_Wahrscheinlichkeit", "wahrscheinlichkeitsrechnung",
            {"de": "Wahrscheinlichkeitsrechnung", "en": "Probability Theory", "es": "Cálculo de probabilidades", "zh": "概率论"}),
    },
}

# Wörter, die in den Präambeln der Hefte stehen
WORT = {
    "de": {"aufgabe": "Aufgabe", "satz": "Satz", "definition": "Definition"},
    "en": {"aufgabe": "Exercise", "satz": "Theorem", "definition": "Definition"},
    "es": {"aufgabe": "Ejercicio", "satz": "Teorema", "definition": "Definición"},
    "zh": {"aufgabe": "练习", "satz": "定理", "definition": "定义"},
}
KERN_TITEL = ("Das Wichtigste", "Das Wichtigste bis hier", "Key points", "Key points so far", "Lo esencial", "Lo esencial hasta aquí", "要点", "本册要点")
SO_ARBEITEST = re.compile(r"^(So arbeitest du|How to work with|Cómo trabajar con|如何使用)")
HINWEIS = {
    "de": "**So arbeitest du mit diesem Kapitel.** Die Abschnitte bauen aufeinander auf, jeder neue Begriff hat einen eigenen "
          "Unterabschnitt mit Beispiel. Kästen zum Aufklappen enthalten Hintergrund (warum etwas so ist und woher es kommt), Herleitungen "
          "und Hinweise zur Simulation; zum Weiterlesen braucht man sie nicht. Versuche die Aufgaben (★ bis ★★★) zuerst selbst, die Lösung "
          "klappst du direkt unter der Aufgabe auf.",
    "en": "**How to work with this chapter.** The sections build on each other, and every new term has its own subsection with an "
          "example. Expandable boxes contain background (why something is the way it is and where it comes from), derivations and "
          "simulation hints; you do not need them to read on. Try the exercises (★ to ★★★) yourself first; the solution expands right "
          "below each exercise.",
    "es": "**Cómo trabajar con este capítulo.** Las secciones se apoyan unas en otras y cada término nuevo tiene su propia subsección con "
          "un ejemplo. Los recuadros desplegables contienen el contexto (por qué algo es así y de dónde viene), deducciones e indicaciones "
          "para la simulación; no hacen falta para seguir leyendo. Intenta primero los ejercicios (de ★ a ★★★) por tu cuenta; la solución "
          "se despliega justo debajo de cada ejercicio.",
    "zh": "**如何使用本章。**各节循序渐进，每个新术语都有单独的小节和例子。可展开的方框包含背景（为什么如此、从何而来）、推导和仿真提示；"
          "不看它们也可以继续阅读。请先自己尝试练习（★ 到 ★★★），解答可在每道练习下方展开。",
}
# Was nur im PDF stimmt. Reihenfolge: längere Wendungen zuerst.
WEBTEXT = {
    "de": [("Hefts", "Kapitels"), ("Hefte", "Kapitel"), ("Heft", "Kapitel")],
    "en": [("workbook", "chapter"), ("Workbook", "Chapter")],
    "es": [("cuaderno", "capítulo"), ("Cuaderno", "Capítulo")],
    "zh": [("本册", "本章")],
}
UEBERBLICK = {"de": "Überblick", "en": "Overview", "es": "Visión general", "zh": "概览"}
ZU_GROSS = 12000                                         # Zeichen: längere Stufen werden an ihren Unterabschnitten geteilt
ZU_GROSS_NEU = 10 ** 9                                   # überarbeitete Hefte (Gliederung wie das Skript): immer ein Artikel je Abschnitt
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


# Makros der Präambel und ihre KaTeX-Form
MAKROS = ((r"\dd", r"\mathrm{d}"), (r"\ee", r"\mathrm{e}"), (r"\jj", r"\mathrm{j}"), (r"\Lap", r"\mathcal{L}"),
          (r"\Four", r"\mathcal{F}"), (r"\Re", r"\operatorname{Re}"), (r"\Im", r"\operatorname{Im}"),
          (r"\Res", r"\operatorname*{Res}"), (r"\eps", r"\varepsilon"), (r"\textmu", r"\mu "),
          (r"\R", r"\mathbb{R}"), (r"\C", r"\mathbb{C}"), (r"\N", r"\mathbb{N}"), (r"\Z", r"\mathbb{Z}"), (r"\Q", r"\mathbb{Q}"),
          (r"\vx", r"\boldsymbol{x}"), (r"\vy", r"\boldsymbol{y}"), (r"\vF", r"\boldsymbol{F}"), (r"\vE", r"\boldsymbol{E}"),
          (r"\vH", r"\boldsymbol{H}"), (r"\vA", r"\boldsymbol{A}"), (r"\vn", r"\boldsymbol{n}"), (r"\vt", r"\boldsymbol{t}"),
          (r"\vg", r"\boldsymbol{g}"), (r"\ver", r"\hat{\boldsymbol{e}}"), (r"\rot", r"\operatorname{rot}"),
          (r"\divg", r"\operatorname{div}"), (r"\dS", r"\mathrm{d}\boldsymbol{S}"), (r"\dsg", r"\mathrm{d}\sigma"))


def makros(m):
    for a, b in MAKROS:
        m = re.sub(re.escape(a) + r"(?![a-zA-Z])", lambda _: b, m)
    return m

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
        self.tab = 0
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
        m = re.sub(r"\\un(?![A-Za-z])\s*(\\?[A-Za-z]+)", r"\\,\\mathrm{\1}", m)   # \un s, \un\Omega
        m = re.sub(r"\\text\{\\textmu\s*([^{}]*)\}", r"\\mu\\text{\1}", m)
        for a, b in MAKROS:
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
        return ":::abbildung %s/%s %d\n%s\n:::" % (self.szenen, n, self.fig, self.text(cap))

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
        if name == "table":                              # Tabelle: Überschrift mit Nummer und Anker, darunter die tabular
            cap, lab = "", None
            body = re.sub(r"^\s*\[[^\]]*\]", "", body)      # Platzierung [!htbp]
            mc = re.search(r"\\caption\{", body)
            if mc:
                cap, j = group(body, mc.end() - 1)
                body = body[:mc.start()] + body[j:]
            ml = re.search(r"\\label\{([^{}]*)\}", body)
            if ml:
                lab = ml.group(1)
                body = body[:ml.start()] + body[ml.end():]
            self.tab += 1
            self.last = (str(self.tab), "tab-%d" % self.tab)
            if lab:
                self.setlabel(lab)
            wort = {"de": "Tabelle", "en": "Table", "es": "Tabla", "zh": "表"}.get(self.lang, "Tabelle")
            kopf = '<span class="anker" id="tab-%d"></span>\n\n**%s %d:** %s' % (self.tab, wort, self.tab, self.text(cap))
            return kopf + "\n\n" + self.block(body)
        if name == "zweck":
            return ":::zweck\n%s\n:::" % self.block(body)
        if name == "analogie":
            return ":::analogie\n%s\n:::" % self.block(body)
        if name in ("merkbox", "kernbox", "herleitung", "beweis", "vertiefung", "frage", "qa", "ltspice", "hintergrund"):
            t, j = group(body, body.index("{"))
            title = self.text(t)
            inner = self.block(body[j:])
            kind = {"merkbox": "merke", "kernbox": "kern" if title in KERN_TITEL else "merke", "herleitung": "herleitung", "beweis": "beweis",
                    "vertiefung": "zusatz", "frage": "frage", "qa": "frage", "ltspice": "ltspice", "hintergrund": "hintergrund"}[name]
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
        cls = ""
        if name == "enumerate" and opt:                  # (a), (b) oder (i), (ii)
            cls = ' class="al"' if "alph" in opt else ' class="rm"' if "roman" in opt else ""
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
        if lang != "de" and not list(cfg["quelle"].glob("kap%d_stufen*_%s.tex" % (k, lang))):
            return m.group(0)                            # noch nicht übersetzt: Text ohne Link, sonst läuft er ins Leere
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


def abschnitte(md, teilen=None):
    """Heft-Text -> Artikel [{titel, art, md}]: Überblick, je Abschnitt einer, zum Schluss das letzte :::kern mit allem danach.
    teilen = Nummern der Abschnitte, die an ### geteilt werden. Das entscheidet die deutsche Fassung (None), damit jede
    Sprache dieselben Artikel hat."""
    teile = [t for t in re.split(r"(?m)^(?=## )", md) if t.strip()]
    grenze = ZU_GROSS_NEU if re.search(r"(?m)^:::hintergrund\b", md) else ZU_GROSS
    out = [{"titel": "", "art": "ueberblick", "md": teile[0]}]
    for nr, t in enumerate(teile[1:]):
        kopf, _, rumpf = t.partition("\n")
        titel = kopf[3:].strip()
        stuecke = re.split(r"(?m)^(?=### )", rumpf)
        gross = len(t) > grenze and len(stuecke) > 1 if teilen is None else nr in teilen
        if gross:                                        # große Stufe: an den Unterabschnitten teilen
            GETEILT.add(nr)
            out.append({"titel": titel, "art": "stufe", "md": stuecke[0] + stuecke[1]})
            for st in stuecke[2:]:
                k, _, r = st.partition("\n")
                out.append({"titel": k[4:].strip(), "art": "stufe", "md": r})
        else:
            out.append({"titel": titel, "art": "stufe", "md": rumpf})
    letzter = out[-1]["md"]
    m = list(re.finditer(r"(?m)^:::kern\b(.*)$", letzter))
    if m:
        k = m[-1]
        out[-1]["md"] = letzter[:k.start()]
        ende = {"titel": k.group(1).strip(), "art": "kern", "md": letzter[k.start():]}
        if not out[-1]["md"].strip():
            out.pop()
        a = re.search(r"(?ms)^:::merke ((?:Die Antwort in|The answer in|La respuesta en|三句话)[^\n(（]*)[^\n]*\n(.*?)^:::\n", out[0]["md"])
        if a:                                            # nennt Ergebnisse, die man am Anfang nicht kennt
            out[0]["md"] = out[0]["md"][:a.start()] + out[0]["md"][a.end():]
            ende["md"] = ":::merke " + a.group(1).strip() + "\n" + a.group(2) + ":::\n\n" + ende["md"]
        p = re.search(r"(?ms)^\u2060?\*\*(?:Ein Prinzip|One principle|Un principio|一个原理|同一原理)[^\n]*\n\n(?:\|[^\n]*\n)+", out[0]["md"])
        if p:
            out[0]["md"] = out[0]["md"][:p.start()] + out[0]["md"][p.end():]
            ende["md"] = ende["md"].rstrip() + "\n\n" + p.group(0)
        out.append(ende)
    return out


GETEILT = set()                                          # von abschnitte() gefüllt: geteilte Abschnitte der deutschen Fassung


def datei_stamm(cfg, kap, stuecke):
    """Dateinamen aus den deutschen Titeln: 01-<kapitel>, 02-<stufe>, ... (der erste bleibt der Name des Kapitels)."""
    _, slug, _ = cfg["hefte"][kap]
    namen = ["01-" + slug]
    for i, a in enumerate(stuecke[1:], 2):
        t = re.sub(r"^Stufe\s+\d+:\s*", "", a["titel"])
        t = re.sub(r"\$[^$]*\$", " ", t)
        namen.append("%02d-%s" % (i, slugify(t)))
    return namen


def verweise(stuecke, namen):
    """#anker, die auf einem anderen Artikel des Kapitels liegen, werden zu datei.html#anker. Liefert die Anker ohne Ziel."""
    wo = {}
    for a, n in zip(stuecke, namen):
        for i in re.findall(r'id="([^"]+)"', a["md"]):
            wo[i] = n
        for i in re.findall(r"(?m)^:::abbildung \S+ (\d+)", a["md"]):
            wo["abb-" + i] = n
    fehlt = set()
    for a, n in zip(stuecke, namen):
        def ersetze(m, eigen=n):
            ziel = wo.get(m.group(1))
            if ziel is None:
                fehlt.add(m.group(1))
                return m.group(0)
            if ziel == eigen:
                return m.group(0)
            return "](%s.html#%s)" % (re.sub(r"^\d+-", "", ziel), m.group(1))
        a["md"] = re.sub(r"\]\(#([^)]+)\)", ersetze, a["md"])
    return fehlt


def begriffe(md):
    seen = []
    for t in re.findall(r"__([^_\n]+)__", md):
        t = re.sub(r"[*`$]", "", t).strip()
        if t and t not in seen and "," not in t:
            seen.append(t)
    return ", ".join(seen[:8])


def kurztext(md, ersatz):
    m = re.search(r":::zweck\n(.*?)\n:::", md, re.S)
    if not m:
        return ersatz
    t = caption_alt(m.group(1))
    return re.split(r"(?<=[.!?。])\s", t)[0]


def artikel(cfg, kap, lang):
    """Liste [(Dateiname, Text)] der Artikel eines Hefts, dazu Heft, offene Lösungen, Anker ohne Ziel."""
    stem, slug, thema = cfg["hefte"][kap]
    h, md, tt, sub, rest, teile = convert(cfg, kap, lang)
    md = webtext(md, lang, cfg, teile)
    _, de, *_ = convert(cfg, kap, "de")
    GETEILT.clear()
    namen = datei_stamm(cfg, kap, abschnitte(webtext(de, "de", cfg, "")))
    stuecke = abschnitte(md, set(GETEILT))
    if len(namen) != len(stuecke):
        raise ValueError("Teil %d %s: %d Artikel, deutsch %d" % (kap, lang, len(stuecke), len(namen)))
    fehlt = verweise(stuecke, namen)
    aus = []
    for i, (a, n) in enumerate(zip(stuecke, namen), 1):
        if a["art"] == "ueberblick":
            titel, kurz, info = "%s: %s" % (UEBERBLICK[lang], tt), UEBERBLICK[lang], sub
        else:
            titel, kurz, info = a["titel"], "", kurztext(a["md"], sub)
        info = re.sub(r"\$([^$]+)\$", lambda mm: "$" + makros(mm.group(1)) + "$", info)   # Präambel-Makros wie \ee
        kopf = ["---", "title: " + titel] + (["kurz: " + kurz] if kurz else []) + [
            "pfad: %s / %s" % (cfg["pfad"][lang], thema[lang]), "order: %d" % (cfg["order"] + kap * 10000 + 100 * i),
            "summary: " + info, "tags: " + begriffe(a["md"]), "lang: " + lang, "---", ""]
        aus.append((n, "\n".join(kopf) + "\n" + a["md"].strip() + "\n"))
    return aus, h, rest, fehlt


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
            arts, h, rest, fehlt = artikel(cfg, kap, lang)
            txt = "\n".join(t for _, t in arts)
            alle.append(txt)
            ordner = ROOT / "content" / cfg["ziel"] / ("%02d-%s" % (kap, slug))
            msg = []
            if fehlt:
                msg.append("Anker ohne Ziel: " + ", ".join(sorted(fehlt)))
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
                endung = "" if lang == "de" else "." + lang
                for alt in ordner.glob("*.md"):                  # nur die alte Fassung dieser Sprache weg, Hand-Artikel bleiben
                    m = re.search(r"\.(en|es|zh)$", alt.stem)
                    if "-mensch" not in alt.name and (m.group(1) if m else "de") == lang:
                        alt.unlink()
                for n, t in arts:
                    (ordner / (n + endung + ".md")).write_text(t, encoding="utf-8", newline="\n")
            print(("⚠ " if msg else "✓ ") + "Teil %d %s: %d Artikel, %d Zeichen, %d Abb., %d Aufg." % (kap, lang, len(arts), len(txt), h.fig, h.aufg))
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
