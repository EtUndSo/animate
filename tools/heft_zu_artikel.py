"""Arbeitshefte (LaTeX) -> Website-Artikel (Markdown für build_wissen.py), in allen Sprachen (de, en, es, zh, fr, tr).

Aufruf (vom Repo-Root):
    python tools/heft_zu_artikel.py et3                 alle Hefte des Moduls, jede Sprache mit Heftdatei
    python tools/heft_zu_artikel.py et3 --kap 1 3       nur diese Hefte
    python tools/heft_zu_artikel.py et3 --lang fr       nur diese Sprache(n); fehlt die Heftdatei, bricht er ab
    python tools/heft_zu_artikel.py et3 --pruefen       nichts schreiben, nur Meldungen
    python tools/heft_zu_artikel.py et3 --aux DIR       Nummern gegen die .aux-Dateien in DIR prüfen

Ohne --lang nimmt er Deutsch und jede Sprache, für die Kap<N>_<Name>_<lang>.tex schon da ist (nicht übersetzte Sprachen
meldet er in einer Zeile). Das Heft bleibt die Quelle: Kap<N>_<Name>[_en|_es|_zh|_fr|_tr].tex mit den \\input-Dateien. Die Artikel werden daraus erzeugt und
nie von Hand geändert. Ein Heft wird zu einem Kapitel aus mehreren kurzen Artikeln: Überblick, je Stufe ein Artikel, zum
Schluss „Das Wichtigste“. Man soll einen Abschnitt abschließen können, bevor der nächste beginnt. Nummern (Gleichungen, Sätze, Abbildungen, Aufgaben) entstehen wie in LaTeX, Verweise werden zu
Links. Aufgaben bekommen ihre Lösung direkt als aufklappbaren Block, nicht am Ende. Abbildungen werden zu
:::abbildung <szene>, die Szene heißt wie das \\label (fig:k1bode -> et3/k1bode). Texte, die nur im PDF stimmen
(„Lösungen am Ende“, „dieses Heft“), werden je Sprache angepasst (WEBTEXT).

Ziel: content/<modul>/<NN-kapitel>/<NN-stufe>[.en|.es|.zh|.fr|.tr].md (die Dateinamen kommen immer aus der deutschen
Fassung). Feste Wendungen, an denen der Umwandler Kästen erkennt, je Sprache: KERN_TITEL, SO_ARBEITEST, ANTWORT_RE,
PRINZIP_RE, WEBTEXT, TEIL_RE (siehe notizen/heft_uebersetzung.md).

Benennung (User, 09.11.2026, notizen/kapitel_umstellung.md): Jedes Heft heißt im Baum „Kapitel N: Titel“ (knoten:), N zählt
in seinem Bereich ab 1 (MODULE[..]["bereiche"], etwa ml: Mathematische Grundlagen = Kap1–6, der Pfad ab Kap8 = Kapitel 1;
prog: Python, C ab Kap101, C++ ab Kap201). Module zeigen zuerst ihre Abkürzung („ET3 – Grundgebiete …“, pfad:), die Adresse
bleibt (basis, adresse:). Verweise „Kapitel 2, Abschnitt 5.3“ (eigener Bereich) und „<Kurzname>, Kapitel 2, Abschnitt 5.3“
(Python, C, C++, Linux, Cybersecurity, Machine Learning, Grundlagen, ET1, ET3, GEMB1, HöMa1, HöMa3) werden in allen Sprachen
zu Links auf Artikel und Anker; übergangsweise auch die alten Formen „Teil 3“, „Grundlagen 2“, „Programmieren, Python 3“,
„Linux 2“, „Höhere Mathematik 1, Teil 2“ (siehe „Bereiche und Verweise“ unten). Nachschlage-Artikel: nachschlagen:.
ml schreibt außerdem content/ml/_reihe*.md, den Hinweis der Übersicht.
"""
import argparse
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))
sys.stdout.reconfigure(encoding="utf-8")
from build_wissen import slugify, caption_alt  # noqa: E402

LANGS = ("de", "en", "es", "zh", "fr", "tr")
NBSP, THIN = "\u00a0", "\u202f"

# ------------------------------------------------------------------------------------- Module ----
MODULE = {
    "et3": {
        "quelle": Path(r"C:\Bücher\ET3\Arbeitshefte"),
        "ziel": "et3",
        "szenen": "et3",
        "pfad": {"de": "Elektrotechnik / 3. Semester / ET3 – Grundgebiete der Elektrotechnik 3: Signale und Systeme",
                 "en": "Electrical Engineering / 3rd Semester / ET3 – Fundamentals of Electrical Engineering 3: Signals and Systems",
                 "es": "Ingeniería eléctrica / 3.er semestre / ET3 – Fundamentos de ingeniería eléctrica 3: señales y sistemas",
                 "zh": "电气工程 / 第 3 学期 / ET3 – 电气工程基础 3：信号与系统",
                 "fr": "Génie électrique / 3e semestre / ET3 – Fondements du génie électrique 3 : signaux et systèmes",
                 "tr": "Elektrik Mühendisliği / 3. Yarıyıl / ET3 – Elektrik Mühendisliğinin Temelleri 3: Sinyaller ve Sistemler"},
        "basis": "elektrotechnik/3-semester/signale-und-systeme",          # Adresse fest (alter Name), auch bei neuem pfad
        "kurz": {l: "ET3" for l in ("de", "en", "es", "zh", "fr", "tr")},
        "alt_modul": {"de": "Signale und Systeme", "en": "Signals and Systems", "es": "Señales y sistemas", "zh": "信号与系统",
                      "fr": "Signaux et systèmes", "tr": "Sinyaller ve Sistemler"},
        "order": 3200000,
        "hefte": {
            1: ("Kap1_Faltung", "lti-systeme-und-faltung",
                {"de": "LTI-Systeme und Faltung", "en": "LTI Systems and Convolution",
                 "es": "Sistemas LTI y convolución", "zh": "LTI 系统与卷积",
                 "fr": "Systèmes LTI et convolution", "tr": "LTI Sistemler ve Evrişim"}),
            2: ("Kap2_Laplace", "laplace-transformation",
                {"de": "Laplace-Transformation", "en": "Laplace Transform",
                 "es": "Transformada de Laplace", "zh": "拉普拉斯变换",
                 "fr": "Transformée de Laplace", "tr": "Laplace Dönüşümü"}),
            3: ("Kap3_Fourier", "fourier-reihe-und-transformation",
                {"de": "Fourier-Reihe und -Transformation", "en": "Fourier Series and Transform",
                 "es": "Serie y transformada de Fourier", "zh": "傅里叶级数与变换",
                 "fr": "Série et transformée de Fourier", "tr": "Fourier Serisi ve Dönüşümü"}),
            4: ("Kap4_Diskret", "abtastung-und-zeitdiskrete-systeme",
                {"de": "Abtastung und zeitdiskrete Systeme", "en": "Sampling and Discrete-Time Systems",
                 "es": "Muestreo y sistemas en tiempo discreto", "zh": "采样与离散时间系统",
                 "fr": "Échantillonnage et systèmes à temps discret", "tr": "Örnekleme ve Ayrık Zamanlı Sistemler"}),
            5: ("Kap5_Tiefpass", "tiefpass-und-bandpasssysteme",
                {"de": "Tiefpass- und Bandpasssysteme", "en": "Lowpass and Bandpass Systems",
                 "es": "Sistemas paso bajo y paso banda", "zh": "低通与带通系统",
                 "fr": "Systèmes passe-bas et passe-bande", "tr": "Alçak Geçiren ve Bant Geçiren Sistemler"}),
            6: ("Kap6_Korrelation", "korrelationsfunktionen",
                {"de": "Korrelationsfunktionen", "en": "Correlation Functions",
                 "es": "Funciones de correlación", "zh": "相关函数",
                 "fr": "Fonctions de corrélation", "tr": "Korelasyon Fonksiyonları"}),
            7: ("Kap7_Statistik", "zufallssignale",
                {"de": "Zufallssignale", "en": "Random Signals", "es": "Señales aleatorias", "zh": "随机信号",
                 "fr": "Signaux aléatoires", "tr": "Rastgele Sinyaller"}),
            8: ("Kap8_Zusatz", "orthogonalentwicklung-und-leitungen",
                {"de": "Orthogonalentwicklung und Leitungen", "en": "Orthogonal Expansion and Transmission Lines",
                 "es": "Desarrollo ortogonal y líneas de transmisión", "zh": "正交展开与传输线",
                 "fr": "Développement orthogonal et lignes de transmission", "tr": "Ortogonal Açılım ve İletim Hatları"}),
        },
    },
}

MODULE["et1"] = {
    "quelle": Path(r"C:\Bücher\ET1\Arbeitshefte"),
    "ziel": "et1",
    "szenen": "et1",
    "pfad": {"de": "Elektrotechnik / 1. Semester / ET1 – Grundgebiete der Elektrotechnik 1: Einführung in die Schaltungsanalyse",
             "en": "Electrical Engineering / 1st Semester / ET1 – Fundamentals of Electrical Engineering 1: Introduction to Circuit Analysis",
             "es": "Ingeniería eléctrica / 1.er semestre / ET1 – Fundamentos de ingeniería eléctrica 1: introducción al análisis de circuitos",
             "zh": "电气工程 / 第 1 学期 / ET1 – 电气工程基础 1：电路分析导论",
             "fr": "Génie électrique / 1er semestre / ET1 – Fondements du génie électrique 1 : introduction à l’analyse des circuits",
             "tr": "Elektrik Mühendisliği / 1. Yarıyıl / ET1 – Elektrik Mühendisliğinin Temelleri 1: Devre Analizine Giriş"},
    "basis": "elektrotechnik/1-semester/grundlagen-der-elektrotechnik",
    "kurz": {l: "ET1" for l in ("de", "en", "es", "zh", "fr", "tr")},
    "alt_modul": {"de": "Grundlagen der Elektrotechnik", "en": "Fundamentals of Electrical Engineering",
                  "es": "Fundamentos de ingeniería eléctrica", "zh": "电气工程基础", "fr": "Fondements du génie électrique",
                  "tr": "Elektrik Mühendisliğinin Temelleri"},
    "order": 1100000,
    "hefte": {
        1: ("Kap1_Feld", "ladung-feld-und-potenzial",
            {"de": "Ladung, Feld und Potenzial", "en": "Charge, Field and Potential",
             "es": "Carga, campo y potencial", "zh": "电荷、电场与电位",
             "fr": "Charge, champ et potentiel", "tr": "Yük, Alan ve Potansiyel"}),
        2: ("Kap2_Stromkreis", "strom-widerstand-und-kirchhoff",
            {"de": "Strom, Widerstand und Kirchhoff", "en": "Current, Resistance and Kirchhoff's Laws",
             "es": "Corriente, resistencia y leyes de Kirchhoff", "zh": "电流、电阻与基尔霍夫定律",
             "fr": "Courant, résistance et lois de Kirchhoff", "tr": "Akım, Direnç ve Kirchhoff Yasaları"}),
        3: ("Kap3_Kondensator", "der-kondensator",
            {"de": "Der Kondensator", "en": "The Capacitor", "es": "El condensador", "zh": "电容器",
             "fr": "Le condensateur", "tr": "Kondansatör"}),
        4: ("Kap4_Messen", "strom-und-spannung-messen",
            {"de": "Strom und Spannung messen", "en": "Measuring Current and Voltage",
             "es": "Medir corriente y tensión", "zh": "电流与电压的测量",
             "fr": "Mesurer le courant et la tension", "tr": "Akım ve Gerilim Ölçümü"}),
        5: ("Kap5_Ersatzquellen", "quellen-und-ersatzquellen",
            {"de": "Quellen und Ersatzquellen", "en": "Sources and Equivalent Sources",
             "es": "Fuentes y fuentes equivalentes", "zh": "电源与等效电源",
             "fr": "Sources et sources équivalentes", "tr": "Kaynaklar ve Eşdeğer Kaynaklar"}),
        6: ("Kap6_Zweitore", "zweitore",
            {"de": "Zweitore", "en": "Two-Port Networks", "es": "Cuadripolos", "zh": "二端口网络",
             "fr": "Quadripôles", "tr": "İki Kapılı Devreler"}),
        7: ("Kap7_Leistung", "leistung-und-anpassung",
            {"de": "Leistung, Anpassung und Wirkungsgrad", "en": "Power, Matching and Efficiency",
             "es": "Potencia, adaptación y rendimiento", "zh": "功率、匹配与效率",
             "fr": "Puissance, adaptation et rendement", "tr": "Güç, Eşleştirme ve Verim"}),
        8: ("Kap8_Netzwerkanalyse", "maschenstrom-und-knotenpotential",
            {"de": "Maschenstrom- und Knotenpotentialverfahren", "en": "Mesh Current and Node Voltage Analysis",
             "es": "Análisis por mallas y por nudos", "zh": "网孔电流法与节点电位法",
             "fr": "Méthode des mailles et méthode des nœuds", "tr": "Çevre Akımları ve Düğüm Gerilimleri Yöntemleri"}),
        9: ("Kap9_Dioden", "halbleiter-und-dioden",
            {"de": "Halbleiter und Dioden", "en": "Semiconductors and Diodes",
             "es": "Semiconductores y diodos", "zh": "半导体与二极管",
             "fr": "Semi-conducteurs et diodes", "tr": "Yarı İletkenler ve Diyotlar"}),
        10: ("Kap10_Bipolartransistor", "der-bipolartransistor",
             {"de": "Der Bipolartransistor", "en": "The Bipolar Transistor", "es": "El transistor bipolar", "zh": "双极型晶体管",
              "fr": "Le transistor bipolaire", "tr": "Bipolar Transistör"}),
        11: ("Kap11_OPV", "der-operationsverstaerker",
             {"de": "Der Operationsverstärker", "en": "The Operational Amplifier",
              "es": "El amplificador operacional", "zh": "运算放大器",
              "fr": "L’amplificateur opérationnel", "tr": "İşlemsel Kuvvetlendirici"}),
    },
}

MODULE["hm1"] = {
    "quelle": Path(r"C:\Bücher\HöMa1\Arbeitshefte"),
    "ziel": "hm1",
    "szenen": "hm1",
    "pfad": {"de": "Elektrotechnik / 1. Semester / HöMa1 – Höhere Mathematik 1",
             "en": "Electrical Engineering / 1st Semester / HöMa1 – Higher Mathematics 1",
             "es": "Ingeniería eléctrica / 1.er semestre / HöMa1 – Matemáticas superiores 1",
             "zh": "电气工程 / 第 1 学期 / HöMa1 – 高等数学 1",
             "fr": "Génie électrique / 1er semestre / HöMa1 – Mathématiques supérieures 1",
             "tr": "Elektrik Mühendisliği / 1. Yarıyıl / HöMa1 – Yüksek Matematik 1"},
    "basis": "elektrotechnik/1-semester/hohere-mathematik-1",
    "kurz": {l: "HöMa1" for l in ("de", "en", "es", "zh", "fr", "tr")},
    "alt_modul": {"de": "Höhere Mathematik 1", "en": "Higher Mathematics 1", "es": "Matemáticas superiores 1", "zh": "高等数学 1",
                  "fr": "Mathématiques supérieures 1", "tr": "Yüksek Matematik 1"},
    "order": 1200000,
    "hefte": {
        1: ("Kap1_Zahlen", "mengen-logik-und-reelle-zahlen",
            {"de": "Mengen, Logik und reelle Zahlen", "en": "Sets, Logic and Real Numbers",
             "es": "Conjuntos, lógica y números reales", "zh": "集合、逻辑与实数",
             "fr": "Ensembles, logique et nombres réels", "tr": "Kümeler, Mantık ve Gerçel Sayılar"}),
        2: ("Kap2_Komplex", "komplexe-zahlen",
            {"de": "Komplexe Zahlen", "en": "Complex Numbers", "es": "Números complejos", "zh": "复数",
             "fr": "Nombres complexes", "tr": "Karmaşık Sayılar"}),
        3: ("Kap3_Funktionen", "funktionen-und-polynome",
            {"de": "Funktionen und Polynome", "en": "Functions and Polynomials",
             "es": "Funciones y polinomios", "zh": "函数与多项式",
             "fr": "Fonctions et polynômes", "tr": "Fonksiyonlar ve Polinomlar"}),
        4: ("Kap4_Folgen", "folgen-und-grenzwerte",
            {"de": "Folgen und Grenzwerte", "en": "Sequences and Limits", "es": "Sucesiones y límites", "zh": "数列与极限",
             "fr": "Suites et limites", "tr": "Diziler ve Limitler"}),
        5: ("Kap5_Stetigkeit", "exponentialfunktion-und-stetigkeit",
            {"de": "Exponentialfunktion und Stetigkeit", "en": "Exponential Function and Continuity",
             "es": "Función exponencial y continuidad", "zh": "指数函数与连续性",
             "fr": "Fonction exponentielle et continuité", "tr": "Üstel Fonksiyon ve Süreklilik"}),
        6: ("Kap6_Reihen", "unendliche-reihen",
            {"de": "Unendliche Reihen", "en": "Infinite Series", "es": "Series infinitas", "zh": "无穷级数",
             "fr": "Séries numériques", "tr": "Sonsuz Seriler"}),
        7: ("Kap7_Potenzreihen", "potenzreihen-und-eulersche-formel",
            {"de": "Potenzreihen und Eulersche Formel", "en": "Power Series and Euler's Formula",
             "es": "Series de potencias y fórmula de Euler", "zh": "幂级数与欧拉公式",
             "fr": "Séries entières et formule d’Euler", "tr": "Kuvvet Serileri ve Euler Formülü"}),
        8: ("Kap8_Vektoren", "vektoren-und-skalarprodukt",
            {"de": "Vektoren und Skalarprodukt", "en": "Vectors and the Dot Product",
             "es": "Vectores y producto escalar", "zh": "向量与内积",
             "fr": "Vecteurs et produit scalaire", "tr": "Vektörler ve Skaler Çarpım"}),
        9: ("Kap9_Basen", "vektorprodukt-und-basen",
            {"de": "Vektorprodukt und Basen", "en": "Cross Product and Bases",
             "es": "Producto vectorial y bases", "zh": "向量积与基",
             "fr": "Produit vectoriel et bases", "tr": "Vektörel Çarpım ve Bazlar"}),
        10: ("Kap10_Matrizen", "matrizen-und-gleichungssysteme",
             {"de": "Matrizen und lineare Gleichungssysteme", "en": "Matrices and Linear Systems",
              "es": "Matrices y sistemas lineales", "zh": "矩阵与线性方程组",
              "fr": "Matrices et systèmes linéaires", "tr": "Matrisler ve Doğrusal Denklem Sistemleri"}),
    },
}

MODULE["gemb1"] = {
    "quelle": Path(r"C:\Bücher\GEMB\Arbeitshefte"),
    "ziel": "gemb1",
    "szenen": "gemb1",
    "pfad": {"de": "Elektrotechnik / 4. Semester / GEMB1 – Grundlagen elektronischer Materialien und Bauelemente 1",
             "en": "Electrical Engineering / 4th Semester / GEMB1 – Fundamentals of Electronic Materials and Devices 1",
             "es": "Ingeniería eléctrica / 4.º semestre / GEMB1 – Fundamentos de materiales y dispositivos electrónicos 1",
             "zh": "电气工程 / 第 4 学期 / GEMB1 – 电子材料与器件基础 1",
             "fr": "Génie électrique / 4e semestre / GEMB1 – Fondements des matériaux et composants électroniques 1",
             "tr": "Elektrik Mühendisliği / 4. Yarıyıl / GEMB1 – Elektronik Malzemeler ve Elemanların Temelleri 1"},
    "basis": "elektrotechnik/4-semester/elektronische-materialien-und-bauelemente-1",
    "kurz": {l: "GEMB1" for l in ("de", "en", "es", "zh", "fr", "tr")},
    "alt_modul": {"de": "Elektronische Materialien und Bauelemente 1", "en": "Electronic Materials and Devices 1",
                  "es": "Materiales y dispositivos electrónicos 1", "zh": "电子材料与器件 1",
                  "fr": "Matériaux et composants électroniques 1", "tr": "Elektronik Malzemeler ve Elemanlar 1"},
    "order": 4100000,
    "hefte": {
        1: ("Kap1_Schroedinger", "welle-teilchen-und-schroedinger-gleichung",
            {"de": "Welle, Teilchen und Schrödinger-Gleichung", "en": "Waves, Particles and the Schrödinger Equation",
             "es": "Ondas, partículas y ecuación de Schrödinger", "zh": "波、粒子与薛定谔方程",
             "fr": "Onde, particule et équation de Schrödinger", "tr": "Dalga, Parçacık ve Schrödinger Denklemi"}),
        2: ("Kap2_Box", "das-teilchen-in-der-box",
            {"de": "Das Teilchen in der Box", "en": "The Particle in a Box",
             "es": "La partícula en una caja", "zh": "箱中粒子",
             "fr": "La particule dans une boîte", "tr": "Kutudaki Parçacık"}),
        3: ("Kap3_Tunnel", "stufe-barriere-und-tunneleffekt",
            {"de": "Stufe, Barriere und Tunneleffekt", "en": "Step, Barrier and Tunnelling",
             "es": "Escalón, barrera y efecto túnel", "zh": "势阶、势垒与隧穿效应",
             "fr": "Marche, barrière et effet tunnel", "tr": "Basamak, Engel ve Tünel Etkisi"}),
        4: ("Kap4_Atome", "atome-und-orbitale",
            {"de": "Atome und Orbitale", "en": "Atoms and Orbitals",
             "es": "Átomos y orbitales", "zh": "原子与轨道",
             "fr": "Atomes et orbitales", "tr": "Atomlar ve Orbitaller"}),
        5: ("Kap5_Bindung", "chemische-bindung",
            {"de": "Chemische Bindung", "en": "Chemical Bonding",
             "es": "Enlace químico", "zh": "化学键",
             "fr": "Liaison chimique", "tr": "Kimyasal Bağ"}),
        6: ("Kap6_Kristall", "kristallgitter",
            {"de": "Kristallgitter", "en": "Crystal Lattices",
             "es": "Redes cristalinas", "zh": "晶格",
             "fr": "Réseaux cristallins", "tr": "Kristal Örgüler"}),
        7: ("Kap7_Reziprok", "kristallwachstum-und-reziprokes-gitter",
            {"de": "Kristallwachstum und reziprokes Gitter", "en": "Crystal Growth and the Reciprocal Lattice",
             "es": "Crecimiento cristalino y red recíproca", "zh": "晶体生长与倒易点阵",
             "fr": "Croissance cristalline et réseau réciproque", "tr": "Kristal Büyütme ve Ters Örgü"}),
        8: ("Kap8_TightBinding", "vom-atom-zum-band",
            {"de": "Vom Atom zum Band", "en": "From Atom to Band",
             "es": "Del átomo a la banda", "zh": "从原子到能带",
             "fr": "De l’atome à la bande", "tr": "Atomdan Banda"}),
        9: ("Kap9_Bandstruktur", "bandstrukturen-lesen",
            {"de": "Bandstrukturen lesen", "en": "Reading Band Structures",
             "es": "Leer estructuras de bandas", "zh": "读懂能带结构",
             "fr": "Lire une structure de bandes", "tr": "Bant Yapılarını Okumak"}),
        10: ("Kap10_Fermi", "zustandsdichte-und-fermi-verteilung",
            {"de": "Zustandsdichte und Fermi-Verteilung", "en": "Density of States and Fermi Distribution",
             "es": "Densidad de estados y distribución de Fermi", "zh": "态密度与费米分布",
             "fr": "Densité d’états et distribution de Fermi", "tr": "Durum Yoğunluğu ve Fermi Dağılımı"}),
        11: ("Kap11_Halbleiter", "eigenhalbleiter-und-dotierung",
            {"de": "Eigenhalbleiter und Dotierung", "en": "Intrinsic Semiconductors and Doping",
             "es": "Semiconductores intrínsecos y dopado", "zh": "本征半导体与掺杂",
             "fr": "Semi-conducteurs intrinsèques et dopage", "tr": "Saf Yarı İletkenler ve Katkılama"}),
        12: ("Kap12_Transport", "strom-im-halbleiter",
            {"de": "Strom im Halbleiter", "en": "Current in Semiconductors",
             "es": "Corriente en el semiconductor", "zh": "半导体中的电流",
             "fr": "Le courant dans le semi-conducteur", "tr": "Yarı İletkende Akım"}),
        13: ("Kap13_Diffusion", "diffusion-rekombination-grundgleichungen",
            {"de": "Diffusion, Rekombination und Grundgleichungen", "en": "Diffusion, Recombination and Basic Equations",
             "es": "Difusión, recombinación y ecuaciones básicas", "zh": "扩散、复合与基本方程",
             "fr": "Diffusion, recombinaison et équations fondamentales", "tr": "Difüzyon, Rekombinasyon ve Temel Denklemler"}),
        14: ("Kap14_pn", "der-p-n-uebergang",
            {"de": "Der p-n-Übergang", "en": "The p-n Junction",
             "es": "La unión p-n", "zh": "p-n 结",
             "fr": "La jonction p-n", "tr": "p-n Eklemi"}),
        15: ("Kap15_MOS", "die-mos-kapazitaet",
            {"de": "Die MOS-Kapazität", "en": "The MOS Capacitor",
             "es": "El condensador MOS", "zh": "MOS 电容",
             "fr": "La capacité MOS", "tr": "MOS Kapasitörü"}),
        16: ("Kap16_MOSreal", "realer-mos-kondensator",
            {"de": "Der reale MOS-Kondensator", "en": "The Real MOS Capacitor",
             "es": "El condensador MOS real", "zh": "实际 MOS 电容",
             "fr": "La capacité MOS réelle", "tr": "Gerçek MOS Kapasitörü"}),
        17: ("Kap17_MOSFET", "der-mosfet",
            {"de": "Der MOSFET", "en": "The MOSFET",
             "es": "El MOSFET", "zh": "MOSFET",
             "fr": "Le MOSFET", "tr": "MOSFET"}),
        18: ("Kap18_Kurzkanal", "skalierung-und-kurzkanaleffekte",
            {"de": "Skalierung und Kurzkanaleffekte", "en": "Scaling and Short-Channel Effects",
             "es": "Escalado y efectos de canal corto", "zh": "按比例缩小与短沟道效应",
             "fr": "Miniaturisation et effets de canal court", "tr": "Ölçekleme ve Kısa Kanal Etkileri"}),
        19: ("Kap19_Licht", "ergaenzung-licht-und-laser",
            {"de": "Licht und Laser (Ergänzung)", "en": "Light and Lasers (Supplement)",
             "es": "Luz y láser (complemento)", "zh": "光与激光（补充）",
             "fr": "Lumière et laser (complément)", "tr": "Işık ve Lazer (Ek)"}),
        20: ("Kap20_Realkristall", "ergaenzung-reale-kristalle",
            {"de": "Reale Kristalle und amorphe Stoffe (Ergänzung)", "en": "Real Crystals and Amorphous Solids (Supplement)",
             "es": "Cristales reales y sólidos amorfos (complemento)", "zh": "实际晶体与非晶固体（补充）",
             "fr": "Cristaux réels et solides amorphes (complément)", "tr": "Gerçek Kristaller ve Amorf Katılar (Ek)"}),
        21: ("Kap21_Zustandsdiagramme", "ergaenzung-zustandsdiagramme",
            {"de": "Zustandsdiagramme (Ergänzung)", "en": "Phase Diagrams (Supplement)",
             "es": "Diagramas de fases (complemento)", "zh": "相图（补充）",
             "fr": "Diagrammes de phases (complément)", "tr": "Faz Diyagramları (Ek)"}),
        22: ("Kap22_Vielteilchen", "ergaenzung-vielteilchensysteme",
            {"de": "Vielteilchensysteme (Ergänzung)", "en": "Many-Particle Systems (Supplement)",
             "es": "Sistemas de muchas partículas (complemento)", "zh": "多粒子系统（补充）",
             "fr": "Systèmes à plusieurs particules (complément)", "tr": "Çok Parçacıklı Sistemler (Ek)"}),
        23: ("Kap23_Entropie", "ergaenzung-entropie-und-gleichgewicht",
            {"de": "Entropie und Gleichgewicht (Ergänzung)", "en": "Entropy and Equilibrium (Supplement)",
             "es": "Entropía y equilibrio (complemento)", "zh": "熵与平衡（补充）",
             "fr": "Entropie et équilibre (complément)", "tr": "Entropi ve Denge (Ek)"}),
        24: ("Kap24_Gitterschwingungen", "ergaenzung-gitterschwingungen",
            {"de": "Gitterschwingungen (Ergänzung)", "en": "Lattice Vibrations (Supplement)",
             "es": "Vibraciones de la red (complemento)", "zh": "晶格振动（补充）",
             "fr": "Vibrations du réseau (complément)", "tr": "Örgü Titreşimleri (Ek)"}),
        25: ("Kap25_Metalle", "ergaenzung-metalle",
            {"de": "Metalle (Ergänzung)", "en": "Metals (Supplement)",
             "es": "Metales (complemento)", "zh": "金属（补充）",
             "fr": "Métaux (complément)", "tr": "Metaller (Ek)"}),
        26: ("Kap26_Schottky", "ergaenzung-metall-halbleiter-uebergang",
            {"de": "Metall-Halbleiter-Übergang (Ergänzung)", "en": "Metal-Semiconductor Junction (Supplement)",
             "es": "Unión metal-semiconductor (complemento)", "zh": "金属-半导体结（补充）",
             "fr": "Jonction métal-semi-conducteur (complément)", "tr": "Metal-Yarı İletken Eklemi (Ek)"}),
        27: ("Kap27_Feldeffekt", "ergaenzung-weitere-feldeffekt-bauelemente",
            {"de": "Weitere Feldeffekt-Bauelemente (Ergänzung)", "en": "Other Field-Effect Devices (Supplement)",
             "es": "Otros dispositivos de efecto de campo (complemento)", "zh": "其他场效应器件（补充）",
             "fr": "Autres composants à effet de champ (complément)", "tr": "Diğer Alan Etkili Elemanlar (Ek)"}),
        28: ("Kap28_Prozess", "ergaenzung-halbleitertechnologie",
            {"de": "Halbleitertechnologie (Ergänzung)", "en": "Semiconductor Technology (Supplement)",
             "es": "Tecnología de semiconductores (complemento)", "zh": "半导体工艺（补充）",
             "fr": "Technologie des semi-conducteurs (complément)", "tr": "Yarı İletken Teknolojisi (Ek)"}),
    },
}

MODULE["hm3"] = {
    "quelle": Path(r"C:\Bücher\HöMa3\Arbeitshefte"),
    "ziel": "hm3",
    "szenen": "hm3",
    "pfad": {"de": "Elektrotechnik / 3. Semester / HöMa3 – Höhere Mathematik 3",
             "en": "Electrical Engineering / 3rd Semester / HöMa3 – Higher Mathematics 3",
             "es": "Ingeniería eléctrica / 3.er semestre / HöMa3 – Matemáticas superiores 3",
             "zh": "电气工程 / 第 3 学期 / HöMa3 – 高等数学 3",
             "fr": "Génie électrique / 3e semestre / HöMa3 – Mathématiques supérieures 3",
             "tr": "Elektrik Mühendisliği / 3. Yarıyıl / HöMa3 – Yüksek Matematik 3"},
    "basis": "elektrotechnik/3-semester/hohere-mathematik-3",
    "kurz": {l: "HöMa3" for l in ("de", "en", "es", "zh", "fr", "tr")},
    "alt_modul": {"de": "Höhere Mathematik 3", "en": "Higher Mathematics 3", "es": "Matemáticas superiores 3", "zh": "高等数学 3",
                  "fr": "Mathématiques supérieures 3", "tr": "Yüksek Matematik 3"},
    "order": 3100000,
    "hefte": {
        1: ("Kap1_Vektorfelder", "differentialrechnung-fuer-vektorfelder",
            {"de": "Differentialrechnung für Vektorfelder", "en": "Differential Calculus for Vector Fields",
             "es": "Cálculo diferencial de campos vectoriales", "zh": "矢量场的微分学",
             "fr": "Calcul différentiel des champs de vecteurs", "tr": "Vektör Alanlarında Diferansiyel Hesap"}),
        2: ("Kap2_Integrale", "integralrechnung-im-rn",
            {"de": "Integralrechnung im Rⁿ", "en": "Integration in Rⁿ", "es": "Cálculo integral en Rⁿ", "zh": "Rⁿ 中的积分",
             "fr": "Calcul intégral dans Rⁿ", "tr": "Rⁿ’de İntegral Hesap"}),
        3: ("Kap3_Kurvenintegrale", "kurvenintegrale",
            {"de": "Kurvenintegrale", "en": "Line Integrals", "es": "Integrales de línea", "zh": "曲线积分",
             "fr": "Intégrales curvilignes", "tr": "Eğri İntegralleri"}),
        4: ("Kap4_Koordinaten", "koordinatentransformationen",
            {"de": "Koordinatentransformationen", "en": "Coordinate Transformations",
             "es": "Transformaciones de coordenadas", "zh": "坐标变换",
             "fr": "Changements de coordonnées", "tr": "Koordinat Dönüşümleri"}),
        5: ("Kap5_Integralsaetze", "integralsaetze-im-raum",
            {"de": "Integralsätze im Raum", "en": "Integral Theorems in Space",
             "es": "Teoremas integrales en el espacio", "zh": "空间中的积分定理",
             "fr": "Théorèmes intégraux dans l’espace", "tr": "Uzayda İntegral Teoremleri"}),
        6: ("Kap6_Funktionenfolgen", "konvergenz-von-funktionenfolgen",
            {"de": "Konvergenz von Funktionenfolgen", "en": "Convergence of Sequences of Functions",
             "es": "Convergencia de sucesiones de funciones", "zh": "函数序列的收敛",
             "fr": "Convergence des suites de fonctions", "tr": "Fonksiyon Dizilerinin Yakınsaklığı"}),
        7: ("Kap7_Fourier", "fourier-reihen",
            {"de": "Fourier-Reihen", "en": "Fourier Series", "es": "Series de Fourier", "zh": "傅里叶级数",
             "fr": "Séries de Fourier", "tr": "Fourier Serileri"}),
        8: ("Kap8_Wahrscheinlichkeit", "wahrscheinlichkeitsrechnung",
            {"de": "Wahrscheinlichkeitsrechnung", "en": "Probability Theory", "es": "Cálculo de probabilidades", "zh": "概率论",
             "fr": "Calcul des probabilités", "tr": "Olasılık Hesabı"}),
    },
}

# Zusatzreihen (ab 04.11.2026): Lernpfad statt Skript, Code-Listings, Makros ohne Argument kommen aus der Präambel des Moduls
HINWEIS_CYBER = {
    "de": "**So arbeitest du mit diesem Kapitel.** Die Abschnitte bauen aufeinander auf, jeder neue Begriff hat einen eigenen "
          "Unterabschnitt mit Beispiel. Kästen zum Aufklappen enthalten Hintergrund (warum etwas so ist und woher es kommt) und "
          "Herleitungen; zum Weiterlesen braucht man sie nicht. Kästen „Achtung“ nennen Regeln, die bei praktischen Übungen immer "
          "gelten. Versuche die Aufgaben (★ bis ★★★) zuerst selbst, die Lösung klappst du direkt unter der Aufgabe auf.",
    "en": "**How to work with this chapter.** The sections build on each other, and every new term has its own subsection with an "
          "example. Expandable boxes contain background (why something is the way it is and where it comes from) and derivations; "
          "you do not need them to read on. Boxes marked “Caution” state rules that always apply to practical exercises. Try the "
          "exercises (★ to ★★★) yourself first; the solution expands right below each exercise.",
    "es": "**Cómo trabajar con este capítulo.** Las secciones se apoyan unas en otras y cada término nuevo tiene su propia subsección con "
          "un ejemplo. Los recuadros desplegables contienen el contexto (por qué algo es así y de dónde viene) y deducciones; no hacen "
          "falta para seguir leyendo. Los recuadros «Atención» indican reglas que valen siempre en los ejercicios prácticos. Intenta "
          "primero los ejercicios (de ★ a ★★★) por tu cuenta; la solución se despliega justo debajo de cada ejercicio.",
    "zh": "**如何使用本章。**各节循序渐进，每个新术语都有单独的小节和例子。可展开的方框包含背景（为什么如此、从何而来）和推导；"
          "不看它们也可以继续阅读。标有“注意”的方框列出实践练习中始终必须遵守的规则。请先自己尝试练习（★ 到 ★★★），解答可在每道练习下方展开。",
    "fr": "**Comment travailler avec ce chapitre.** Les sections s’appuient les unes sur les autres, et chaque nouvelle notion a sa "
          "propre sous-section avec un exemple. Les encadrés dépliables contiennent le contexte (pourquoi les choses sont ainsi et "
          "d’où elles viennent) et les démonstrations\u202f; ils ne sont pas nécessaires pour poursuivre la lecture. Les encadrés "
          "«\u00a0Attention\u00a0» énoncent des règles qui valent toujours pour les exercices pratiques. Essayez d’abord de résoudre "
          "les exercices (de ★ à ★★★) vous-même\u202f; la solution se déplie juste en dessous de chaque exercice.",
    "tr": "**Bu bölümle nasıl çalışılır?** Konular birbirinin üzerine kurulur ve her yeni kavramın örnek içeren kendi alt başlığı "
          "vardır. Açılır kutular arka plan bilgisini (bir şeyin neden öyle olduğunu ve nereden geldiğini) ve türetmeleri içerir; "
          "okumaya devam etmek için bunlara gerek yoktur. “Dikkat” kutuları, uygulamalı alıştırmalarda her zaman geçerli olan "
          "kuralları belirtir. Alıştırmaları (★ ile ★★★ arası) önce kendiniz çözmeye çalışın; çözümü her alıştırmanın hemen altında "
          "açabilirsiniz.",
}
HINWEIS_ML = {
    "de": "**So arbeitest du mit diesem Kapitel.** Die Abschnitte bauen aufeinander auf, jeder neue Begriff hat einen eigenen "
          "Unterabschnitt mit Beispiel. Kästen zum Aufklappen enthalten Hintergrund (warum ein Verfahren funktioniert und woher es "
          "kommt), Herleitungen und Beweise; zum Weiterlesen braucht man sie nicht. Versuche die Aufgaben (★ bis ★★★) zuerst selbst "
          "und führe Programme wirklich aus; die Lösung klappst du direkt unter der Aufgabe auf.",
    "en": "**How to work with this chapter.** The sections build on each other, and every new term has its own subsection with an "
          "example. Expandable boxes contain background (why a method works and where it comes from), derivations and proofs; you "
          "do not need them to read on. Try the exercises (★ to ★★★) yourself first and actually run the programs; the solution "
          "expands right below each exercise.",
    "es": "**Cómo trabajar con este capítulo.** Las secciones se apoyan unas en otras y cada término nuevo tiene su propia subsección con "
          "un ejemplo. Los recuadros desplegables contienen el contexto (por qué funciona un método y de dónde viene), deducciones y "
          "demostraciones; no hacen falta para seguir leyendo. Intenta primero los ejercicios (de ★ a ★★★) por tu cuenta y ejecuta de "
          "verdad los programas; la solución se despliega justo debajo de cada ejercicio.",
    "zh": "**如何使用本章。**各节循序渐进，每个新术语都有单独的小节和例子。可展开的方框包含背景（方法为什么有效、从何而来）、推导和证明；"
          "不看它们也可以继续阅读。请先自己尝试练习（★ 到 ★★★），并真正运行程序；解答可在每道练习下方展开。",
    "fr": "**Comment travailler avec ce chapitre.** Les sections s’appuient les unes sur les autres, et chaque nouvelle notion a sa "
          "propre sous-section avec un exemple. Les encadrés dépliables contiennent le contexte (pourquoi une méthode fonctionne et "
          "d’où elle vient), les démonstrations et les preuves\u202f; ils ne sont pas nécessaires pour poursuivre la lecture. "
          "Essayez d’abord de résoudre les exercices (de ★ à ★★★) vous-même et exécutez réellement les programmes\u202f; la "
          "solution se déplie juste en dessous de chaque exercice.",
    "tr": "**Bu bölümle nasıl çalışılır?** Konular birbirinin üzerine kurulur ve her yeni kavramın örnek içeren kendi alt başlığı "
          "vardır. Açılır kutular arka plan bilgisini (bir yöntemin neden işe yaradığını ve nereden geldiğini), türetmeleri ve "
          "ispatları içerir; okumaya devam etmek için bunlara gerek yoktur. Alıştırmaları (★ ile ★★★ arası) önce kendiniz çözmeye "
          "çalışın ve programları gerçekten çalıştırın; çözümü her alıştırmanın hemen altında açabilirsiniz.",
}

MODULE["cyber"] = {
    "quelle": Path(r"C:\Bücher\EtUndSo\Cybersecurity\Arbeitshefte"),
    "ziel": "cyber",
    "szenen": "cyber",
    "pfad": {"de": "Informatik / Cybersecurity", "en": "Computer Science / Cybersecurity",
             "es": "Informática / Ciberseguridad", "zh": "计算机科学 / 网络安全",
             "fr": "Informatique / Cybersécurité", "tr": "Bilgisayar Bilimleri / Siber Güvenlik"},
    "basis": "informatik/cybersecurity",
    "order": 6100000,
    "praeambel_makros": True,
    "hinweis": HINWEIS_CYBER,
    "kurz": {"de": "Cybersecurity", "en": "Cybersecurity", "es": "Ciberseguridad", "zh": "网络安全", "fr": "Cybersécurité",
             "tr": "Siber Güvenlik"},
    "hefte": {                                           # Stamm T01-T14 (Recherche\LERNPFAD.md); Äste folgen ab 101
        1: ("Kap1_Sicherheit", "sicherheit-schutzziele-und-spielregeln",
            {"de": "Sicherheit, Schutzziele und Spielregeln", "en": "Security, Protection Goals and Ground Rules",
             "es": "Seguridad, objetivos de protección y reglas del juego", "zh": "安全、保护目标与基本规则",
             "fr": "Sécurité, objectifs de protection et règles du jeu", "tr": "Güvenlik, Koruma Hedefleri ve Temel Kurallar"}),
        2: ("Kap2_Computer", "wie-ein-computer-arbeitet",
            {"de": "Wie ein Computer arbeitet", "en": "How a Computer Works",
             "es": "Cómo funciona un ordenador", "zh": "计算机如何工作",
             "fr": "Comment fonctionne un ordinateur", "tr": "Bir Bilgisayar Nasıl Çalışır"}),
        3: ("Kap3_LiveUSB", "linux-vom-usb-stick-und-die-konsole",
            {"de": "Linux vom USB-Stick und die Konsole", "en": "Linux from a USB Stick and the Console",
             "es": "Linux desde una memoria USB y la consola", "zh": "从 U 盘运行 Linux 与命令行",
             "fr": "Linux sur clé USB et la console", "tr": "USB Bellekten Linux ve Konsol"}),
        4: ("Kap4_Shell", "die-shell-als-werkzeug",
            {"de": "Die Shell als Werkzeug", "en": "The Shell as a Tool",
             "es": "La shell como herramienta", "zh": "作为工具的 Shell",
             "fr": "Le shell comme outil", "tr": "Bir Araç Olarak Kabuk"}),
        5: ("Kap5_Rechte", "benutzer-rechte-und-prozesse",
            {"de": "Benutzer, Rechte und Prozesse", "en": "Users, Permissions and Processes",
             "es": "Usuarios, permisos y procesos", "zh": "用户、权限与进程",
             "fr": "Utilisateurs, droits et processus", "tr": "Kullanıcılar, İzinler ve Süreçler"}),
        6: ("Kap6_Netzwerke", "netzwerke-vom-signal-zum-paket",
            {"de": "Netzwerke I: vom Signal zum Paket", "en": "Networks I: From Signal to Packet",
             "es": "Redes I: de la señal al paquete", "zh": "网络（一）：从信号到数据包",
             "fr": "Réseaux I\u00a0: du signal au paquet", "tr": "Ağlar I: Sinyalden Pakete"}),
        7: ("Kap7_Dienste", "netzwerke-verbindungen-und-dienste",
            {"de": "Netzwerke II: Verbindungen und Dienste", "en": "Networks II: Connections and Services",
             "es": "Redes II: conexiones y servicios", "zh": "网络（二）：连接与服务",
             "fr": "Réseaux II\u00a0: connexions et services", "tr": "Ağlar II: Bağlantılar ve Hizmetler"}),
        8: ("Kap8_Python", "python-als-sicherheitswerkzeug",
            {"de": "Python als Sicherheitswerkzeug", "en": "Python as a Security Tool",
             "es": "Python como herramienta de seguridad", "zh": "Python 作为安全工具",
             "fr": "Python comme outil de sécurité", "tr": "Güvenlik Aracı Olarak Python"}),
        9: ("Kap9_Speicher", "c-und-der-speicher-eines-programms",
            {"de": "C und der Speicher eines Programms", "en": "C and a Program's Memory",
             "es": "C y la memoria de un programa", "zh": "C 语言与程序的内存",
             "fr": "Le C et la mémoire d’un programme", "tr": "C ve Bir Programın Belleği"}),
        10: ("Kap10_Maschinencode", "maschinencode-assembler-und-debugger",
             {"de": "Maschinencode, Assembler und Debugger", "en": "Machine Code, Assembly and Debuggers",
              "es": "Código máquina, ensamblador y depurador", "zh": "机器码、汇编与调试器",
              "fr": "Code machine, assembleur et débogueur", "tr": "Makine Kodu, Assembly ve Hata Ayıklayıcı"}),
        11: ("Kap11_Krypto", "kryptographie-verschluesselung-hash-mac",
             {"de": "Kryptographie I: Verschlüsselung, Hash, MAC", "en": "Cryptography I: Encryption, Hashes, MACs",
              "es": "Criptografía I: cifrado, hash y MAC", "zh": "密码学（一）：加密、哈希与 MAC",
              "fr": "Cryptographie I\u00a0: chiffrement, hachage, MAC", "tr": "Kriptografi I: Şifreleme, Özetleme, MAC"}),
        12: ("Kap12_PublicKey", "kryptographie-public-key-signaturen-tls",
             {"de": "Kryptographie II: Public-Key, Signaturen, TLS", "en": "Cryptography II: Public Key, Signatures, TLS",
              "es": "Criptografía II: clave pública, firmas y TLS", "zh": "密码学（二）：公钥、签名与 TLS",
              "fr": "Cryptographie II\u00a0: clé publique, signatures, TLS", "tr": "Kriptografi II: Açık Anahtar, İmzalar, TLS"}),
        13: ("Kap13_Web", "das-web-http-browser-und-sitzungen",
             {"de": "Das Web I: HTTP, Browser und Sitzungen", "en": "The Web I: HTTP, Browsers and Sessions",
              "es": "La web I: HTTP, navegadores y sesiones", "zh": "Web（一）：HTTP、浏览器与会话",
              "fr": "Le Web I\u00a0: HTTP, navigateurs et sessions", "tr": "Web I: HTTP, Tarayıcılar ve Oturumlar"}),
        14: ("Kap14_Webangriffe", "das-web-injection-xss-csrf",
             {"de": "Das Web II: Injection, XSS, CSRF", "en": "The Web II: Injection, XSS, CSRF",
              "es": "La web II: inyección, XSS y CSRF", "zh": "Web（二）：注入、XSS 与 CSRF",
              "fr": "Le Web II\u00a0: injection, XSS, CSRF", "tr": "Web II: Enjeksiyon, XSS, CSRF"}),
    },
}

MODULE["ml"] = {
    "quelle": Path(r"C:\Bücher\EtUndSo\MachineLearning\Arbeitshefte"),
    "ziel": "ml",
    "szenen": "ml",
    "pfad": {"de": "Informatik / Machine Learning", "en": "Computer Science / Machine Learning",
             "es": "Informática / Aprendizaje automático", "zh": "计算机科学 / 机器学习",
             "fr": "Informatique / Apprentissage automatique", "tr": "Bilgisayar Bilimleri / Makine Öğrenmesi"},
    "basis": "informatik/machine-learning",
    "order": 6200000,
    "praeambel_makros": True,
    "hinweis": HINWEIS_ML,
    # Bereiche (Entscheidung des Users, 05./06.11.2026): T01-T06 = Mathematische Grundlagen zum Nachschlagen in einem eigenen
    # Ast, der ML-Pfad zählt ab T08 als Kapitel 1 (Kapitel N = T(N+7)); T07 Python/NumPy entfällt (Bereich „Programmieren“).
    # Dateien, Ordner unter content/ und Szenen behalten die Lernpfad-Nummer (Kap1_Vektoren, ml/k1…).
    "bereiche": (
        {"kaps": (1, 6), "nr": 0, "nachschlagen": True, "order": 9000000,      # im Baum nach dem Pfad
         "pfad": {"de": "Mathematische Grundlagen", "en": "Mathematical Foundations", "es": "Fundamentos matemáticos",
                  "zh": "数学基础", "fr": "Fondements mathématiques", "tr": "Matematiksel Temeller"},
         "slug": "mathematische-grundlagen",
         "kurz": {"de": "Grundlagen", "en": "Foundations", "es": "Fundamentos", "zh": "数学基础", "fr": "Fondements",
                  "tr": "Temeller"},
         "titel": {"de": "Machine Learning, Mathematische Grundlagen", "en": "Machine Learning, Mathematical Foundations",
                   "es": "Aprendizaje automático, Fundamentos matemáticos", "zh": "机器学习 · 数学基础",
                   "fr": "Apprentissage automatique, Fondements mathématiques", "tr": "Makine Öğrenmesi, Matematiksel Temeller"},
         "alt": {"de": "Grundlagen {n}", "en": "Foundations {n}", "es": "Fundamentos {n}", "zh": "基础篇 {n}",
                 "fr": "Fondements {n}", "tr": "Temeller {n}"}},
        {"kaps": (8, 99), "nr": 7, "teil": True,
         "kurz": {"de": "Machine Learning", "en": "Machine Learning", "es": "Aprendizaje automático", "zh": "机器学习",
                  "fr": "Apprentissage automatique", "tr": "Makine Öğrenmesi"}},
    ),
    "reihe_hinweis": {                                   # auf der Übersicht unter „Machine Learning“ (fr: fr_typo beim Schreiben)
        "de": "Die mathematischen Grundlagen sind zum Nachschlagen gedacht; man muss sie nicht vorab durcharbeiten. Jedes "
              "Kapitel des Lernpfads nennt zu Beginn eines Abschnitts die Grundlagen, die es braucht, fasst sie kurz zusammen "
              "und verlinkt die ausführliche Stelle.",
        "en": "The mathematical foundations are meant for looking things up; you do not need to work through them first. "
              "At the start of each section, every chapter of the learning path names the foundations it needs, sums them "
              "up briefly and links to the full explanation.",
        "es": "Los fundamentos matemáticos están pensados para consultarlos; no hace falta estudiarlos antes. Al comienzo de "
              "cada sección, cada capítulo de la ruta de aprendizaje indica los fundamentos que necesita, los resume "
              "brevemente y enlaza la explicación completa.",
        "zh": "数学基础供查阅之用，不必事先通读。学习路径的每一章都会在各节开头列出所需的基础知识，加以简要概括，并链接到详细讲解之处。",
        "fr": "Les fondements mathématiques sont faits pour être consultés ; il n’est pas nécessaire de les étudier "
              "d’abord. Au début de chaque section, chaque chapitre du parcours indique les fondements dont il a besoin, les "
              "résume brièvement et renvoie à l’explication complète.",
        "tr": "Matematiksel temeller başvuru amaçlıdır; önceden baştan sona çalışmanız gerekmez. Öğrenme yolunun her bölümü, "
              "her kesimin başında ihtiyaç duyduğu temelleri belirtir, kısaca özetler ve ayrıntılı açıklamaya bağlantı verir.",
    },
    "hefte": {                                           # Stamm T01-T22 (Recherche\LERNPFAD.md); Äste folgen ab 101
        1: ("Kap1_Vektoren", "vektoren-und-matrizen",
            {"de": "Vektoren und Matrizen", "en": "Vectors and Matrices", "es": "Vectores y matrices", "zh": "向量与矩阵",
             "fr": "Vecteurs et matrices", "tr": "Vektörler ve Matrisler"}),
        2: ("Kap2_Eigenwerte", "projektion-eigenwerte-und-zerlegungen",
            {"de": "Projektion, Eigenwerte und Zerlegungen", "en": "Projection, Eigenvalues and Decompositions",
             "es": "Proyección, valores propios y descomposiciones", "zh": "投影、特征值与矩阵分解",
             "fr": "Projection, valeurs propres et décompositions", "tr": "İzdüşüm, Özdeğerler ve Ayrışımlar"}),
        3: ("Kap3_Ableitung", "ableitung-gradient-und-kettenregel",
            {"de": "Ableitung, Gradient und Kettenregel", "en": "Derivative, Gradient and Chain Rule",
             "es": "Derivada, gradiente y regla de la cadena", "zh": "导数、梯度与链式法则",
             "fr": "Dérivée, gradient et règle de dérivation en chaîne", "tr": "Türev, Gradyan ve Zincir Kuralı"}),
        4: ("Kap4_Wahrscheinlichkeit", "wahrscheinlichkeit",
            {"de": "Wahrscheinlichkeit", "en": "Probability", "es": "Probabilidad", "zh": "概率",
             "fr": "Probabilités", "tr": "Olasılık"}),
        5: ("Kap5_Statistik", "statistik-und-information",
            {"de": "Statistik und Information", "en": "Statistics and Information",
             "es": "Estadística e información", "zh": "统计与信息",
             "fr": "Statistique et information", "tr": "İstatistik ve Bilgi"}),
        6: ("Kap6_Optimierung", "optimierung",
            {"de": "Optimierung", "en": "Optimization", "es": "Optimización", "zh": "优化",
             "fr": "Optimisation", "tr": "Optimizasyon"}),
        # 7 (Kap7_Python, „Python, NumPy und Werkzeuge“) entfällt: Python steht im Bereich „Programmieren“ (MODULE["prog"])
        8: ("Kap8_Lernen", "lernen-aus-daten",
            {"de": "Lernen aus Daten", "en": "Learning from Data", "es": "Aprender de los datos", "zh": "从数据中学习",
             "fr": "Apprendre à partir des données", "tr": "Verilerden Öğrenme"}),
        9: ("Kap9_Regression", "lineare-regression",
            {"de": "Lineare Regression", "en": "Linear Regression", "es": "Regresión lineal", "zh": "线性回归",
             "fr": "Régression linéaire", "tr": "Doğrusal Regresyon"}),
        10: ("Kap10_Gradientenabstieg", "gradientenabstieg",
             {"de": "Gradientenabstieg", "en": "Gradient Descent", "es": "Descenso de gradiente", "zh": "梯度下降",
              "fr": "Descente de gradient", "tr": "Gradyan İnişi"}),
        11: ("Kap11_Logistisch", "logistische-regression-und-softmax",
             {"de": "Logistische Regression und Softmax", "en": "Logistic Regression and Softmax",
              "es": "Regresión logística y softmax", "zh": "逻辑回归与 Softmax",
              "fr": "Régression logistique et softmax", "tr": "Lojistik Regresyon ve Softmax"}),
        12: ("Kap12_Regularisierung", "ueberanpassung-und-regularisierung",
             {"de": "Überanpassung und Regularisierung", "en": "Overfitting and Regularization",
              "es": "Sobreajuste y regularización", "zh": "过拟合与正则化",
              "fr": "Surapprentissage et régularisation", "tr": "Aşırı Uyum ve Düzenlileştirme"}),
        13: ("Kap13_Evaluierung", "evaluierung-und-modellauswahl",
             {"de": "Evaluierung und Modellauswahl", "en": "Evaluation and Model Selection",
              "es": "Evaluación y selección de modelos", "zh": "评估与模型选择",
              "fr": "Évaluation et sélection de modèles", "tr": "Değerlendirme ve Model Seçimi"}),
        14: ("Kap14_kNN", "k-naechste-nachbarn",
             {"de": "k-nächste Nachbarn", "en": "k-Nearest Neighbors", "es": "k vecinos más cercanos", "zh": "k 近邻",
              "fr": "k plus proches voisins", "tr": "k En Yakın Komşu"}),
        15: ("Kap15_Baeume", "entscheidungsbaeume",
             {"de": "Entscheidungsbäume", "en": "Decision Trees", "es": "Árboles de decisión", "zh": "决策树",
              "fr": "Arbres de décision", "tr": "Karar Ağaçları"}),
        16: ("Kap16_Ensembles", "ensembles",
             {"de": "Ensembles", "en": "Ensembles", "es": "Métodos de conjunto", "zh": "集成学习",
              "fr": "Méthodes d’ensemble", "tr": "Topluluk Yöntemleri"}),
        17: ("Kap17_SVM", "support-vektor-maschinen-und-kerne",
             {"de": "Support-Vektor-Maschinen und Kerne", "en": "Support Vector Machines and Kernels",
              "es": "Máquinas de vectores de soporte y núcleos", "zh": "支持向量机与核方法",
              "fr": "Machines à vecteurs de support et noyaux", "tr": "Destek Vektör Makineleri ve Çekirdekler"}),
        18: ("Kap18_Clustering", "clustering",
             {"de": "Clustering", "en": "Clustering", "es": "Agrupamiento", "zh": "聚类",
              "fr": "Partitionnement de données", "tr": "Kümeleme"}),
        19: ("Kap19_PCA", "hauptkomponentenanalyse",
             {"de": "Hauptkomponentenanalyse", "en": "Principal Component Analysis",
              "es": "Análisis de componentes principales", "zh": "主成分分析",
              "fr": "Analyse en composantes principales", "tr": "Temel Bileşen Analizi"}),
        20: ("Kap20_Netze", "neuronale-netze-vom-neuron-zum-netz",
             {"de": "Neuronale Netze I: vom Neuron zum Netz", "en": "Neural Networks I: From Neuron to Network",
              "es": "Redes neuronales I: de la neurona a la red", "zh": "神经网络（一）：从神经元到网络",
              "fr": "Réseaux de neurones I\u00a0: du neurone au réseau", "tr": "Yapay Sinir Ağları I: Nörondan Ağa"}),
        21: ("Kap21_Backprop", "neuronale-netze-backpropagation",
             {"de": "Neuronale Netze II: Backpropagation", "en": "Neural Networks II: Backpropagation",
              "es": "Redes neuronales II: retropropagación", "zh": "神经网络（二）：反向传播",
              "fr": "Réseaux de neurones II\u00a0: rétropropagation", "tr": "Yapay Sinir Ağları II: Geri Yayılım"}),
        22: ("Kap22_PyTorch", "neuronale-netze-training-mit-pytorch",
             {"de": "Neuronale Netze III: Training mit PyTorch", "en": "Neural Networks III: Training with PyTorch",
              "es": "Redes neuronales III: entrenamiento con PyTorch", "zh": "神经网络（三）：用 PyTorch 训练",
              "fr": "Réseaux de neurones III\u00a0: entraînement avec PyTorch", "tr": "Yapay Sinir Ağları III: PyTorch ile Eğitim"}),
    },
}

# Gemeinsame Bereiche (Entscheidung des Users, 06.11.2026: „Inhalte nicht mehrfach auf der Webseite vollständig erklären“).
# ML und Cybersecurity setzen sie voraus und verweisen mit „Python, Kapitel N, Abschnitt M“ bzw. „Linux, Kapitel N, Abschnitt M“
# (seit 09.11.2026; Wendungen je Sprache: "kurz", KAPITEL_RE, ABSCHNITT_RE). Hefte trägt der Schreib-Agent hier ein, sobald der
# Lernpfad steht; fehlende Hefte überspringt der Umwandler, Verweise auf sie bleiben Text ohne Link.
MODULE["prog"] = {
    "quelle": Path(r"C:\Bücher\EtUndSo\Programmieren\Arbeitshefte"),
    "ziel": "prog",
    "szenen": "prog",
    "pfad": {"de": "Informatik / Programmieren", "en": "Computer Science / Programming",
             "es": "Informática / Programación", "zh": "计算机科学 / 编程",
             "fr": "Informatique / Programmation", "tr": "Bilgisayar Bilimleri / Programlama"},
    "basis": "informatik/programmieren",
    "order": 6010000,
    "praeambel_makros": True,
    "hinweis": HINWEIS_ML,
    # alte Verweisform (bis 09.11.2026, Übergang): „Programmieren, Python 3“; „Python 3“ allein ist meist die Sprachversion
    "praefix": {"de": "Programmieren, ", "en": "Programming, ", "es": "Programación, ", "zh": "编程，",
                "fr": "Programmation, ", "tr": "Programlama, "},
    "bereiche": (                                        # Kapitel 1, 2, … = Kap1, Kap2, …; C ab Kap101, C++ ab Kap201
        {"kaps": (1, 99), "nr": 0, "pfad": {l: "Python" for l in LANGS}, "slug": "python",
         "kurz": {l: "Python" for l in LANGS},
         "titel": {"de": "Programmieren, Python", "en": "Programming, Python", "es": "Programación, Python",
                   "zh": "编程 · Python", "fr": "Programmation, Python", "tr": "Programlama, Python"},
         "alt": {l: "Python {n}" for l in LANGS}},
        {"kaps": (101, 199), "nr": 100, "pfad": {l: "C" for l in LANGS}, "slug": "c",     # noch kein Heft: Adresse frei gewählt
         "kurz": {l: "C" for l in LANGS},
         "titel": {"de": "Programmieren, C", "en": "Programming, C", "es": "Programación, C", "zh": "编程 · C",
                   "fr": "Programmation, C", "tr": "Programlama, C"},
         "alt": {l: "C {n}" for l in LANGS}},
        {"kaps": (201, 299), "nr": 200, "pfad": {l: "C++" for l in LANGS}, "slug": "cpp",
         "kurz": {l: "C++" for l in LANGS},
         "titel": {"de": "Programmieren, C++", "en": "Programming, C++", "es": "Programación, C++", "zh": "编程 · C++",
                   "fr": "Programmation, C++", "tr": "Programlama, C++"},
         "alt": {l: "C++ {n}" for l in LANGS}},
    ),
    "hefte": {                                           # Nummer: ("Kap<N>_<Name>", "slug", {Titel je Sprache}) wie bei ml
        1: ("Kap1_Programme", "programme-und-der-python-interpreter",
            {"de": "Programme und der Python-Interpreter", "en": "Programs and the Python Interpreter",
             "es": "Programas y el intérprete de Python", "zh": "程序与 Python 解释器",
             "fr": "Programmes et l’interpréteur Python", "tr": "Programlar ve Python Yorumlayıcısı"}),
        2: ("Kap2_Werte", "werte-typen-und-variablen",
            {"de": "Werte, Typen und Variablen", "en": "Values, Types and Variables", "es": "Valores, tipos y variables",
             "zh": "值、类型与变量", "fr": "Valeurs, types et variables", "tr": "Değerler, Türler ve Değişkenler"}),
        3: ("Kap3_Kontrollfluss", "entscheidungen-und-schleifen",
            {"de": "Entscheidungen und Schleifen", "en": "Decisions and Loops", "es": "Decisiones y bucles",
             "zh": "条件与循环", "fr": "Conditions et boucles", "tr": "Kararlar ve Döngüler"}),
        4: ("Kap4_Funktionen", "funktionen",
            {"de": "Funktionen", "en": "Functions", "es": "Funciones", "zh": "函数", "fr": "Fonctions", "tr": "Fonksiyonlar"}),
        5: ("Kap5_Sequenzen", "sequenzen-zeichenketten-listen-und-tupel",
            {"de": "Sequenzen: Zeichenketten, Listen und Tupel", "en": "Sequences: Strings, Lists and Tuples",
             "es": "Secuencias: cadenas, listas y tuplas", "zh": "序列：字符串、列表与元组",
             "fr": "Séquences : chaînes, listes et tuples", "tr": "Diziler: Karakter Dizileri, Listeler ve Demetler"}),
        6: ("Kap6_Dictionaries", "dictionaries-mengen-und-hashing",
            {"de": "Dictionaries, Mengen und Hashing", "en": "Dictionaries, Sets and Hashing",
             "es": "Diccionarios, conjuntos y hashing", "zh": "字典、集合与哈希", "fr": "Dictionnaires, ensembles et hachage",
             "tr": "Sözlükler, Kümeler ve Karma"}),
        7: ("Kap7_Laufzeit", "laufzeit-suchen-und-sortieren",
            {"de": "Laufzeit, Suchen und Sortieren", "en": "Running Time, Searching and Sorting",
             "es": "Tiempo de ejecución, búsqueda y ordenación", "zh": "运行时间、查找与排序",
             "fr": "Temps d’exécution, recherche et tri", "tr": "Çalışma Süresi, Arama ve Sıralama"}),
        8: ("Kap8_Fehler", "ausnahmen-testen-und-fehlersuche",
            {"de": "Ausnahmen, Testen und Fehlersuche", "en": "Exceptions, Testing and Debugging",
             "es": "Excepciones, pruebas y depuración", "zh": "异常、测试与调试", "fr": "Exceptions, tests et débogage",
             "tr": "İstisnalar, Test ve Hata Ayıklama"}),
        9: ("Kap9_Dateien", "dateien-text-und-bytes",
            {"de": "Dateien, Text und Bytes", "en": "Files, Text and Bytes", "es": "Archivos, texto y bytes",
             "zh": "文件、文本与字节", "fr": "Fichiers, texte et octets", "tr": "Dosyalar, Metin ve Baytlar"}),
        10: ("Kap10_Klassen", "klassen-und-objekte",
             {"de": "Klassen und Objekte", "en": "Classes and Objects", "es": "Clases y objetos", "zh": "类与对象",
              "fr": "Classes et objets", "tr": "Sınıflar ve Nesneler"}),
        11: ("Kap11_Module", "module-pakete-und-virtuelle-umgebungen",
             {"de": "Module, Pakete und virtuelle Umgebungen", "en": "Modules, Packages and Virtual Environments",
              "es": "Módulos, paquetes y entornos virtuales", "zh": "模块、包与虚拟环境",
              "fr": "Modules, paquets et environnements virtuels", "tr": "Modüller, Paketler ve Sanal Ortamlar"}),
        12: ("Kap12_NumPyArray", "numpy-das-array",
             {"de": "NumPy I: das Array", "en": "NumPy I: the Array", "es": "NumPy I: el array", "zh": "NumPy I：数组",
              "fr": "NumPy I : le tableau", "tr": "NumPy I: Dizi"}),
        13: ("Kap13_NumPyRechnen", "numpy-rechnen-zufall-daten-und-plotten",
             {"de": "NumPy II: Rechnen, Zufall, Daten und Plotten", "en": "NumPy II: Computing, Randomness, Data and Plotting",
              "es": "NumPy II: cálculo, azar, datos y gráficos", "zh": "NumPy II：计算、随机、数据与绘图",
              "fr": "NumPy II : calcul, hasard, données et graphiques", "tr": "NumPy II: Hesaplama, Rastgelelik, Veri ve Çizim"}),
    },
}

MODULE["linux"] = {
    "quelle": Path(r"C:\Bücher\EtUndSo\Linux\Arbeitshefte"),
    "ziel": "linux",
    "szenen": "linux",
    "pfad": {"de": "Informatik / Linux und Kommandozeile", "en": "Computer Science / Linux and the Command Line",
             "es": "Informática / Linux y la línea de comandos", "zh": "计算机科学 / Linux 与命令行",
             "fr": "Informatique / Linux et ligne de commande", "tr": "Bilgisayar Bilimleri / Linux ve Komut Satırı"},
    "basis": "informatik/linux-und-kommandozeile",
    "order": 6050000,
    "praeambel_makros": True,
    "hinweis": HINWEIS_CYBER,
    "extern": True,                                      # alte Form „Linux N, Abschnitt M“ (Übergang) ist von jedem Modul aus ein Link
    "bereiche": (
        {"kaps": (1, 99), "nr": 0, "kurz": {l: "Linux" for l in LANGS}, "alt": {l: "Linux {n}" for l in LANGS}},
    ),
    "hefte": {                                           # Kapitel 1, 2, … = Kap1, Kap2, … (Lernpfad EtUndSo\Linux\Recherche\LERNPFAD.md)
        1: ("Kap1_Uebungslinux", "ein-linux-zum-ueben",
            {"de": "Ein Linux zum Üben: WSL, virtuelle Maschine, Live-USB-Stick",
             "en": "A Linux to Practise On: WSL, Virtual Machine, Live USB Stick",
             "es": "Un Linux para practicar: WSL, máquina virtual, memoria USB autoarrancable",
             "zh": "用来练习的 Linux：WSL、虚拟机、Live U 盘",
             "fr": "Un Linux pour s’exercer : WSL, machine virtuelle, clé USB live",
             "tr": "Alıştırma İçin Bir Linux: WSL, Sanal Makine, Canlı USB Bellek"}),
        2: ("Kap2_Shell", "die-shell-erste-befehle",
            {"de": "Die Shell: erste Befehle", "en": "The Shell: First Commands", "es": "La shell: primeras órdenes",
             "zh": "Shell：最初的命令", "fr": "Le shell : premières commandes", "tr": "Kabuk: İlk Komutlar"}),
        3: ("Kap3_Dateien", "dateien-verzeichnisse-und-pfade",
            {"de": "Dateien, Verzeichnisse und Pfade", "en": "Files, Directories and Paths",
             "es": "Archivos, directorios y rutas", "zh": "文件、目录与路径", "fr": "Fichiers, répertoires et chemins",
             "tr": "Dosyalar, Dizinler ve Yollar"}),
        4: ("Kap4_Stroeme", "stroeme-umleitung-pipes-und-exit-status",
            {"de": "Ströme, Umleitung, Pipes und Exit-Status",
             "en": "Streams, Redirection, Pipes and Exit Status",
             "es": "Flujos, redirección, tuberías y estado de salida",
             "zh": "流、重定向、管道与退出状态",
             "fr": "Flux, redirection, tubes et code de sortie",
             "tr": "Akışlar, Yönlendirme, Borular ve Çıkış Durumu"}),
        5: ("Kap5_Expansion", "expansion-quoting-variablen-und-umgebung",
            {"de": "Wie die Shell eine Befehlszeile liest: Expansion, Quoting, Variablen, Umgebung",
             "en": "How the Shell Reads a Command Line: Expansion, Quoting, Variables, Environment",
             "es": "Cómo lee la shell una línea de órdenes: expansión, entrecomillado, variables, entorno",
             "zh": "Shell 如何读取命令行：展开、引用、变量与环境",
             "fr": "Comment le shell lit une ligne de commande : expansion, guillemets, variables, environnement",
             "tr": "Kabuk Bir Komut Satırını Nasıl Okur: Genişletme, Tırnaklama, Değişkenler, Ortam"}),
        6: ("Kap6_Textwerkzeuge", "textwerkzeuge-und-regulaere-ausdruecke",
            {"de": "Textwerkzeuge und reguläre Ausdrücke", "en": "Text Tools and Regular Expressions",
             "es": "Herramientas de texto y expresiones regulares", "zh": "文本工具与正则表达式",
             "fr": "Outils de texte et expressions régulières", "tr": "Metin Araçları ve Düzenli İfadeler"}),
        7: ("Kap7_Rechte", "benutzer-gruppen-und-rechte",
            {"de": "Benutzer, Gruppen und Rechte", "en": "Users, Groups and Permissions",
             "es": "Usuarios, grupos y permisos", "zh": "用户、组与权限", "fr": "Utilisateurs, groupes et droits",
             "tr": "Kullanıcılar, Gruplar ve İzinler"}),
        8: ("Kap8_Prozesse", "prozesse-signale-und-dienste",
            {"de": "Prozesse, Signale und Dienste", "en": "Processes, Signals and Services",
             "es": "Procesos, señales y servicios", "zh": "进程、信号与服务", "fr": "Processus, signaux et services",
             "tr": "Süreçler, Sinyaller ve Servisler"}),
        9: ("Kap9_Pakete", "software-installieren-paketverwaltung",
            {"de": "Software installieren: Paketverwaltung", "en": "Installing Software: Package Management",
             "es": "Instalar software: gestión de paquetes", "zh": "安装软件：包管理",
             "fr": "Installer des logiciels : gestion des paquets", "tr": "Yazılım Kurmak: Paket Yönetimi"}),
        10: ("Kap10_Skripte", "shell-skripte",
             {"de": "Shell-Skripte", "en": "Shell Scripts", "es": "Scripts de shell", "zh": "Shell 脚本",
              "fr": "Scripts shell", "tr": "Kabuk Betikleri"}),
        11: ("Kap11_SSH", "ssh-dateien-uebertragen-und-tmux",
             {"de": "Auf entfernten Rechnern arbeiten: SSH, Dateien übertragen, tmux",
              "en": "Working on Remote Machines: SSH, Transferring Files, tmux",
              "es": "Trabajar en máquinas remotas: SSH, transferir archivos, tmux",
              "zh": "在远程计算机上工作：SSH、文件传输与 tmux",
              "fr": "Travailler sur des machines distantes : SSH, transfert de fichiers, tmux",
              "tr": "Uzak Makinelerde Çalışmak: SSH, Dosya Aktarımı, tmux"}),
    },
}

# Jedes Modul hat Bereiche (siehe „Bereiche und Verweise“); ohne eigene Liste ist das ganze Modul ein Bereich. Fehlt "kurz"
# oder "titel" eines Bereichs, gelten Kurzname bzw. Name des Moduls (letzter Teil von pfad, „ET3 – Grundgebiete …“).
for _cfg in MODULE.values():
    if "bereiche" not in _cfg:
        _cfg["bereiche"] = ({"kaps": (1, 999), "nr": 0, "teil": True},)
    for _b in _cfg["bereiche"]:
        _b.setdefault("kurz", _cfg.get("kurz"))
        _b.setdefault("titel", {l: _cfg["pfad"][l].split(" / ")[-1] for l in LANGS})

# Code-Umgebungen der Präambeln (Zusatzreihen) -> Sprache des Code-Blocks auf der Website (```<sprache> <titel>)
CODE_ENVS = {"python": "python", "konsole": "console", "bash": "bash", "ccode": "c", "cppcode": "cpp", "asm": "nasm",
             "gas": "gas", "ausgabe": "text"}
# Wortlaut, der nicht als LaTeX gelesen werden darf (% ist darin kein Kommentar): Code-Umgebungen, \verb|..|, \lstinline|..|, \url{..}
VERBATIM_RE = re.compile(r"\\begin\{(%s)\}.*?\\end\{\1\}|\\(?:verb|lstinline)\*?([^A-Za-z\s{])[^\n]*?\2|\\lstinline\{[^{}\n]*\}|\\url\{[^{}]*\}"
                         % "|".join(CODE_ENVS), re.S)
# \texttt{..}: Sonderzeichen-Befehle -> Zeichen
TT_NAMED = {"textbackslash": "\\", "textasciitilde": "~", "textasciicircum": "^", "textbar": "|", "textless": "<",
            "textgreater": ">", "textquotesingle": "'", "textquotedbl": '"', "textunderscore": "_", "textdollar": "$",
            "slash": "/", "textendash": "–", "textemdash": "—", "textquotedblleft": "“", "textquotedblright": "”",
            "quotedblbase": "„", "ldots": "…", "dots": "…"}
TT_RE = re.compile(r"\\([A-Za-z]+)(?:\{\}|\s*)|\\([^A-Za-z])|([{}~])")


def tt_text(a):
    """Inhalt von \\texttt{..} als Wortlaut: \\_ -> _, \\textbackslash{} -> \\, ~ -> Leerzeichen, Formatbefehle fallen weg."""
    def r(m):
        if m.group(1) is not None:
            return TT_NAMED.get(m.group(1), "")
        if m.group(2) is not None:
            return {" ": " ", ",": " ", "-": "", "/": "", "\\": " ", "\n": " "}.get(m.group(2), m.group(2))
        return " " if m.group(3) == "~" else ""
    return TT_RE.sub(r, a)


def praeambel_makros(folder):
    """Makros ohne Argument aus <folder>/praeambel.tex: ((\\name, Ersatz), ...), \\DeclareMathOperator als \\operatorname."""
    p = folder / "praeambel.tex"
    if not p.is_file():
        return ()
    s = strip_comments(p.read_text(encoding="utf-8"))
    out = []
    for m in re.finditer(r"\\(?:newcommand|renewcommand|providecommand)\*?\{\\([A-Za-z]+)\}\s*\{", s):
        body, _ = group(s, m.end() - 1)
        if "$" not in body and "#" not in body:
            out.append(("\\" + m.group(1), body))
    for m in re.finditer(r"\\DeclareMathOperator(\*?)\{\\([A-Za-z]+)\}\s*\{", s):
        body, _ = group(s, m.end() - 1)
        out.append(("\\" + m.group(2), r"\operatorname%s{%s}" % (m.group(1), body)))
    return tuple(out)


def modul_makros(cfg):
    if "_makros" not in cfg:
        cfg["_makros"] = praeambel_makros(cfg["quelle"]) if cfg.get("praeambel_makros") else ()
    return cfg["_makros"]


# Wörter, die in den Präambeln der Hefte stehen
WORT = {
    "de": {"aufgabe": "Aufgabe", "satz": "Satz", "definition": "Definition"},
    "en": {"aufgabe": "Exercise", "satz": "Theorem", "definition": "Definition"},
    "es": {"aufgabe": "Ejercicio", "satz": "Teorema", "definition": "Definición"},
    "zh": {"aufgabe": "练习", "satz": "定理", "definition": "定义"},
    "fr": {"aufgabe": "Exercice", "satz": "Théorème", "definition": "Définition"},
    "tr": {"aufgabe": "Alıştırma", "satz": "Teorem", "definition": "Tanım"},
}
KERN_TITEL = ("Das Wichtigste", "Das Wichtigste bis hier", "Key points", "Key points so far", "Lo esencial", "Lo esencial hasta aquí", "要点", "本册要点",
              "L’essentiel", "L'essentiel", "L’essentiel jusqu’ici", "L'essentiel jusqu'ici", "Temel noktalar", "Buraya kadarki temel noktalar")
SO_ARBEITEST = re.compile(r"^(So arbeitest du|How to work with|Cómo trabajar con|如何使用|Comment travailler avec|Bu çalışma kitabıyla nasıl)")
# Kernbox „Die Antwort in drei Sätzen (…)“ im Überblick wandert ans Ende; Absatz „Ein Prinzip hinter allen Ergebnissen.“ ebenso
ANTWORT_RE = r"Die Antwort in|The answer in|La respuesta en|三句话|La réponse en|Üç cümlede"
PRINZIP_RE = r"Ein Prinzip|One principle|Un principio|一个原理|同一原理|Un principe|Tüm sonuçların ardındaki"
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
    "fr": "**Comment travailler avec ce chapitre.** Les sections s’appuient les unes sur les autres, et chaque nouvelle notion a sa "
          "propre sous-section avec un exemple. Les encadrés dépliables contiennent le contexte (pourquoi les choses sont ainsi et "
          "d’où elles viennent), les démonstrations et des indications pour la simulation\u202f; ils ne sont pas nécessaires pour "
          "poursuivre la lecture. Essayez d’abord de résoudre les exercices (de ★ à ★★★) vous-même\u202f; la solution se déplie "
          "juste en dessous de chaque exercice.",
    "tr": "**Bu bölümle nasıl çalışılır?** Konular birbirinin üzerine kurulur ve her yeni kavramın örnek içeren kendi alt başlığı "
          "vardır. Açılır kutular arka plan bilgisini (bir şeyin neden öyle olduğunu ve nereden geldiğini), türetmeleri ve "
          "simülasyon ipuçlarını içerir; okumaya devam etmek için bunlara gerek yoktur. Alıştırmaları (★ ile ★★★ arası) önce "
          "kendiniz çözmeye çalışın; çözümü her alıştırmanın hemen altında açabilirsiniz.",
}


def _tr_webtext():
    """Türkisch: „çalışma kitabı“ (Arbeitsheft) mit seinen Endungen -> „bölüm“ (Kapitel). Längere Formen zuerst."""
    formen = [("kitaplarından", "bölümlerden"), ("kitaplarında", "bölümlerde"), ("kitaplarının", "bölümlerin"),
              ("kitaplarına", "bölümlere"), ("kitaplarını", "bölümleri"), ("kitapları", "bölümler"),
              ("kitabından", "bölümden"), ("kitabında", "bölümde"), ("kitabının", "bölümün"), ("kitabına", "bölüme"),
              ("kitabını", "bölümü"), ("kitabıyla", "bölümle"), ("kitabı", "bölüm")]
    out = []
    for a, b in formen:
        out += [("çalışma " + a, b), ("Çalışma " + a, b[0].upper() + b[1:])]
    return out


# Was nur im PDF stimmt. Reihenfolge: längere Wendungen zuerst.
WEBTEXT = {
    "de": [("Hefts", "Kapitels"), ("Hefte", "Kapitel"), ("Heft", "Kapitel")],
    "en": [("workbook", "chapter"), ("Workbook", "Chapter")],
    "es": [("cuaderno", "capítulo"), ("Cuaderno", "Capítulo")],
    "zh": [("本册", "本章")],
    "fr": [("cahier", "chapitre"), ("Cahier", "Chapitre")],
    "tr": _tr_webtext(),
}
UEBERBLICK = {"de": "Überblick", "en": "Overview", "es": "Visión general", "zh": "概览", "fr": "Vue d’ensemble", "tr": "Genel Bakış"}
ZU_GROSS = 12000                                         # Zeichen: längere Stufen werden an ihren Unterabschnitten geteilt
ZU_GROSS_NEU = 10 ** 9                                   # überarbeitete Hefte (Gliederung wie das Skript): immer ein Artikel je Abschnitt
# alte Form \u201eTeil N\u201c (\u00dcbergang bis zur Umstellung der Hefte); \u201eTeile 2 durch diese Zahl\u201c ist eine Rechenanweisung
TEIL_RE = {"de": r"\b(?:Teil|Teilen|Teile(?![ \u00a0]\d+[ \u00a0]+durch\b))[ \u00a0](\d+)\b", "en": r"\bPart[ \u00a0](\d+)\b",
           "es": r"\b[Pp]arte[ \u00a0](\d+)\b",
           "zh": r"第[ \u00a0]?(\d+)[ \u00a0]?部分"}
TEIL_RE.update({"fr": r"\b[Pp]artie[ \u00a0](\d+)\b", "tr": r"\b[Kk]ısım[ \u00a0](\d+)\b"})   # „Partie 3“, „Kısım 3“
# Französisch: geschütztes Leerzeichen vor : (\u00a0), vor ; ! ? (\u202f) und in « » (\u00a0), wie babel-french im PDF.
# webtext ruft es nur für Text außerhalb von Formeln, Code und Link-Zielen auf; ein ":::"-Blockkopf bleibt unberührt.
FR_VOR = re.compile(r"(?<=[\w)\]*’'”»])[ \t]?([:;!?])(?=\s|$|\*)")
FR_AUF, FR_ZU = re.compile(r"«[ \t\u00a0\u202f]*"), re.compile(r"(?<=\S)[ \t\u00a0\u202f]*»")


def fr_typo(t):
    t = FR_VOR.sub(lambda m: ("\u00a0" if m.group(1) == ":" else "\u202f") + m.group(1), t)
    return FR_ZU.sub("\u00a0»", FR_AUF.sub("«\u00a0", t))


# ------------------------------------------------------------------------ Bereiche und Verweise ----
# Jedes Modul zerfällt in Bereiche (MODULE[..]["bereiche"]; ohne Liste ist das ganze Modul einer), jeder mit
#   kaps = (von, bis)   Kapitelnummern der Dateien Kap<N>_… (= Lernpfad-Nummern),
#   nr                  Anzeige-Nummer = kap − nr („Kapitel 1“ = Kap8 im ML-Pfad, Kap101 bei C),
#   kurz                Kurzname je Sprache für Verweise aus anderen Bereichen und Modulen („Python“, „Grundlagen“, „ET3“),
#   titel               Bereich in der Titelzeile des PDFs („Programmieren, Python“; TITELZEILE),
#   pfad, slug          (optional) eigener Ast unter dem Modul („Mathematische Grundlagen“) mit fester Adresse (slug),
#                       sonst hängen die Hefte direkt am Modul,
#   order               (optional) Platz im Baum, wird zu order der Artikel addiert,
#   nachschlagen        (optional) Nachschlagebereich: Die Website zeigt unter jedem Artikel „Verwendet in“,
#   alt, teil           (Übergang) alte Heftnamen: „Grundlagen {n}“, „Python {n}“, „Linux {n}“ bzw. „Teil N“ (TEIL_RE).
# Im Baum heißt jedes Heft „Kapitel N: Titel“ (KAPITEL, knoten:). Verweise: „Kapitel N“ zählt im Bereich des eigenen Hefts,
# „<Kurzname>, Kapitel N“ (zh „<Kurzname>第 N 章“) im genannten Bereich, auch in jedem anderen Modul. Mit „, Abschnitt M“
# (auch „Abschnitte M und K“) wird daraus ein Link auf den Artikel mit Abschnitt bzw. Unterabschnitt M und dessen Anker,
# sonst auf den Überblick des Hefts. Übergangsweise erkennt der Umwandler auch die alten Formen: „Teil N“ (eigener Bereich),
# „Grundlagen N“ (in ml), „Programmieren, Python N“ ("praefix"), „Linux N“ ("extern") und „<alter Modulname>, Teil N“
# ("alt_modul", etwa „Höhere Mathematik 1, Teil 2“). Wendungen je Sprache: notizen/kapitel_umstellung.md.
KAPITEL = {"de": "Kapitel {n}", "en": "Chapter {n}", "es": "Capítulo {n}", "zh": "第 {n} 章", "fr": "Chapitre {n}",
           "tr": "Bölüm {n}"}
_KN = r"(?P<n>\d+)(?!\d|[.,]\d)"
KAPITEL_RE = {"de": r"\bKapiteln?[ \xa0]" + _KN, "en": r"\b[Cc]hapters?[ \xa0]" + _KN, "es": r"\b[Cc]apítulos?[ \xa0]" + _KN,
              "fr": r"\b[Cc]hapitres?[ \xa0]" + _KN, "tr": r"\bBölüm(?:ler)?[ \xa0]" + _KN,
              "zh": r"第[ \xa0]?" + _KN + r"[ \xa0]?章"}
# Titelzeile des PDFs ({\small …} unter dem Untertitel), b = Bereich (titel), n = Kapitel; danach „. Stand: …“ usw.
TITELZEILE = {"de": "Arbeitsheft {b}, Kapitel~{n}", "en": "Workbook {b}, Chapter~{n}",
              "es": "Cuaderno de trabajo {b}, capítulo~{n}", "zh": "{b} 练习册，第~{n}~章",
              "fr": "Cahier d’exercices {b}, chapitre~{n}", "tr": "Çalışma Kitabı {b}, Bölüm~{n}"}
NUM = r"\d+(?:\.\d+)?(?!\d)"
ABSCHNITT_RE = {"de": r",[ \xa0]Abschnitte?[ \xa0](?P<s>%s)" % NUM,
                "en": r",[ \xa0][Ss]ections?[ \xa0](?P<s>%s)" % NUM,
                "es": r",[ \xa0][Ss]ecci(?:ón|ones)[ \xa0](?P<s>%s)" % NUM,
                "fr": r",[ \xa0][Ss]ections?[ \xa0](?P<s>%s)" % NUM,
                "tr": r",[ \xa0][Kk]esim(?:ler)?[ \xa0](?P<s>%s)" % NUM,
                "zh": r"[ \xa0]?第[ \xa0]?(?P<s>%s)[ \xa0]?节" % NUM}
UND_RE = {"de": r"(?P<uc>[ \xa0]und[ \xa0])(?P<ut>(?P<uk>%s))" % NUM,      # zweite Nummer: „Abschnitte 10.1 und 11.4“
          "en": r"(?P<uc>[ \xa0]and[ \xa0])(?P<ut>(?P<uk>%s))" % NUM,
          "es": r"(?P<uc>[ \xa0]y[ \xa0])(?P<ut>(?P<uk>%s))" % NUM,
          "fr": r"(?P<uc>[ \xa0]et[ \xa0])(?P<ut>(?P<uk>%s))" % NUM,
          "tr": r"(?P<uc>[ \xa0]ve[ \xa0])(?P<ut>(?P<uk>%s))" % NUM,
          "zh": r"(?P<uc>和)(?P<ut>第[ \xa0]?(?P<uk>%s)[ \xa0]?节)" % NUM}


def bereich(cfg, kap):
    """Bereich (Eintrag aus cfg["bereiche"]), zu dem Kapitel kap gehört, oder None."""
    for b in cfg.get("bereiche", ()):
        if b["kaps"][0] <= kap <= b["kaps"][1]:
            return b
    return None


def kapitel_nr(cfg, kap):
    """Angezeigte Kapitelnummer im Bereich: Kap8 im ML-Pfad -> 1, Kap101 -> 1 (C)."""
    b = bereich(cfg, kap)
    return kap - (b["nr"] if b else 0)


def heft_name(cfg, kap, lang):
    """„Kapitel 1“, „Chapter 1“, „第 1 章“ … (Nummer im Bereich)."""
    return KAPITEL[lang].format(n=kapitel_nr(cfg, kap))


def titelzeile(cfg, kap, lang):
    """Titelzeile des PDFs ohne Stand: „Arbeitsheft Programmieren, Python, Kapitel~3“."""
    return TITELZEILE[lang].format(b=bereich(cfg, kap)["titel"][lang], n=kapitel_nr(cfg, kap))


def knoten_name(cfg, kap, lang):
    """Aufschrift des Hefts im Baum: „Kapitel 1: Vektoren und Matrizen“."""
    name = heft_name(cfg, kap, lang)
    t = cfg["hefte"][kap][2][lang]
    return name + "：" + t if lang == "zh" else fr_typo(name + ": " + t) if lang == "fr" else name + ": " + t


def heft_basis(cfg, kap):
    """Adresse des Asts, in dem das Heft liegt (ohne /wissen/ und Sprache); fest, auch wenn sich Namen ändern."""
    b = bereich(cfg, kap)
    return cfg["basis"] + ("/" + (b.get("slug") or slugify(b["pfad"]["de"])) if b and b.get("pfad") else "")


def heft_adresse(cfg, kap):
    """adresse: der Artikel (Knoten bis zum Heft, deutsche Slugs): Daraus baut build_wissen die Adresse, pfad: gibt die Namen."""
    return heft_basis(cfg, kap) + "/" + slugify(cfg["hefte"][kap][2]["de"])


def heft_pfad(cfg, kap, lang):
    """pfad: der Artikel: Modul, gegebenenfalls Bereich, Heft."""
    b = bereich(cfg, kap)
    return " / ".join([cfg["pfad"][lang]] + ([b["pfad"][lang]] if b and b.get("pfad") else []) + [cfg["hefte"][kap][2][lang]])


def heft_url(cfg, kap, lang, artikel=None):
    """Adresse eines Artikels des Hefts (ohne artikel: der Überblick)."""
    _, slug, thema = cfg["hefte"][kap]
    return "/wissen/%s%s/%s/%s.html" % ("" if lang == "de" else lang + "/", heft_basis(cfg, kap), slugify(thema["de"]), artikel or slug)


def heft_da(cfg, kap, lang):
    """Gibt es das Heft (und in dieser Sprache)? Sonst bleibt ein Verweis Text ohne Link."""
    if kap not in cfg["hefte"] or not (cfg["quelle"] / (cfg["hefte"][kap][0] + ".tex")).is_file():
        return False
    return lang == "de" or bool(list(cfg["quelle"].glob("kap%d_stufen*_%s.tex" % (kap, lang))))


_ANKER = {}                                              # (ziel, kap) -> {"13.5": (Dateistamm, Artikel, Anker)}


def heft_ordner(cfg, kap):
    return ROOT / "content" / cfg["ziel"] / ("%02d-%s" % (kap, cfg["hefte"][kap][1]))


def anker_karte(cfg, kap):
    """Wo liegen die Abschnitte eines Hefts? Aus den deutschen Artikeln unter content/ (Anker stufe-13, stufe-13-5)."""
    key = (cfg["ziel"], kap)
    if key not in _ANKER:
        d = heft_ordner(cfg, kap)
        karte = {}
        for p in (sorted(d.glob("*.md")) if d.is_dir() else ()):
            if re.search(r"\.(%s)$" % "|".join(l for l in LANGS if l != "de"), p.stem) or "-mensch" in p.name:
                continue
            for a in re.findall(r'id="(stufe-\d+(?:-\d+)?)"', p.read_text(encoding="utf-8")):
                karte.setdefault(a[6:].replace("-", "."), (p.stem, re.sub(r"^\d+-", "", p.stem), a))
        _ANKER[key] = karte
    return _ANKER[key]


def abschnitt_url(cfg, kap, nummer, lang):
    """Adresse von Abschnitt/Unterabschnitt nummer („13“, „13.5“) des Hefts, None ohne Ziel (auch: Artikel nicht übersetzt)."""
    e = anker_karte(cfg, kap).get(nummer)
    if e is None:
        return None
    stem, art, anker = e
    if lang != "de" and not (heft_ordner(cfg, kap) / ("%s.%s.md" % (stem, lang))).is_file():
        return None
    return heft_url(cfg, kap, lang, art) + "#" + anker


def _wort_re(t):
    """Feste Wendung als Muster: Leerzeichen auch geschützt (~), chinesisches Komma auch als , oder ·."""
    return "".join(r"[ \xa0]" if c == " " else r"[，,·][ \xa0]?" if c == "，" else re.escape(c) for c in t)


def _name_re(fmt):
    """„Grundlagen {n}“ -> Muster mit Gruppe n; keine Versionsnummer („Linux 6.8“)."""
    vor, _, nach = fmt.partition("{n}")
    weich = lambda t: _wort_re(t).replace(r"[ \xa0]", r"[ \xa0]?")
    r = weich(vor) + r"(?P<n>\d+)(?!\d|[.,]\d)" + weich(nach)
    return (r"\b" + r) if vor[:1].isascii() and vor[:1].isalpha() else r


def _kurz_re(kurz, lang):
    """„Python, “ vor „Kapitel 2“ (zh: „Python 第 2 章“, „数学基础第 2 章“, auch mit ，)."""
    vor = r"(?<![A-Za-z0-9_+\-])" if kurz[:1].isascii() and kurz[:1].isalnum() else ""
    return vor + _wort_re(kurz) + (r"[ \xa0]?[，,·]?[ \xa0]?" if lang == "zh" else r",[ \xa0]")


def verweis_arten(cfg, kap, lang):
    """[(Muster mit Gruppe n, Ziel-Modul, Bereich)] in der Reihenfolge, in der sie zu prüfen sind (längste Wendung zuerst)."""
    arten = []
    quer = [(z, b) for z in MODULE.values() for b in z["bereiche"]]
    for z, b in sorted(quer, key=lambda zb: -len(zb[1]["kurz"][lang])):   # 1. „Python, Kapitel 2“, „HöMa1, Kapitel 5“
        arten.append((_kurz_re(b["kurz"][lang], lang) + KAPITEL_RE[lang], z, b))
    for z in MODULE.values():                            # 2. alte Formen (Übergang): „Programmieren, Python 2“, „Linux 2“,
        if z.get("praefix") or z.get("extern"):         #    „Höhere Mathematik 1, Teil 2“
            vor = _wort_re(z["praefix"][lang]) if z.get("praefix") else ""
            for b in sorted(z["bereiche"], key=lambda b: -len(b["alt"][lang])):
                arten.append((vor + _name_re(b["alt"][lang]), z, b))
        if z.get("alt_modul"):
            arten.append((r"(?<!\w)" + _wort_re(z["alt_modul"][lang]) + (r"[ \xa0]?[，,·]?[ \xa0]?" if lang == "zh" else r",[ \xa0]")
                          + TEIL_RE[lang].replace(r"(\d+)", r"(?P<n>\d+)", 1), z, z["bereiche"][0]))
    if not (cfg.get("praefix") or cfg.get("extern")):     # 3. eigene Bereiche mit altem Namen (Übergang): „Grundlagen 2“
        for b in cfg["bereiche"]:
            if b.get("alt"):
                arten.append((_name_re(b["alt"][lang]), cfg, b))
    eigen = bereich(cfg, kap)
    arten.append((KAPITEL_RE[lang], cfg, eigen))         # 4. „Kapitel 2“ im eigenen Bereich
    tb = eigen if eigen else next((b for b in cfg["bereiche"] if b.get("teil")), None)
    arten.append((TEIL_RE[lang].replace(r"(\d+)", r"(?P<n>\d+)", 1), cfg, tb))   # 5. „Teil 2“ (Übergang)
    return arten


def verweis_regex(arten, lang):
    """Alle Verweisarten in einem Muster (so wird nichts doppelt verlinkt); Gruppen je Art mit ihrer Nummer i."""
    teile = []
    for i, (muster, _, _) in enumerate(arten):
        nummeriert = lambda r: re.sub(r"\(\?P<(\w+)>", lambda m: "(?P<%s%d>" % (m.group(1), i), r)
        teile.append("(?P<a%d>(?P<h%d>%s)(?P<A%d>%s(?P<U%d>%s)?)?)" % (
            i, i, nummeriert(muster), i, nummeriert(ABSCHNITT_RE[lang]), i, nummeriert(UND_RE[lang])))
    return re.compile("|".join(teile))


def verweis_link(m, arten, lang, fehlt):
    """Ein gefundener Verweis -> Markdown-Link(s); ohne Heft (oder Übersetzung) bleibt der Text. fehlt sammelt Abschnitte ohne Ziel."""
    i = int(m.lastgroup[1:])
    _, z, b = arten[i]
    k = int(m.group("n%d" % i)) + (b["nr"] if b else 0)
    if (b and not b["kaps"][0] <= k <= b["kaps"][1]) or not heft_da(z, k, lang):
        return m.group(0)
    kopf, ab, u = m.group("h%d" % i), m.group("A%d" % i), m.group("U%d" % i) or ""
    if ab is None:
        return "[%s](%s)" % (kopf, heft_url(z, k, lang))
    ziel = abschnitt_url(z, k, m.group("s%d" % i), lang)
    if ziel is None:
        fehlt.append("%s %d: %s" % (z["ziel"], k, m.group(0)))
        return "[%s](%s)%s" % (kopf, heft_url(z, k, lang), ab)
    out = "[%s%s](%s)" % (kopf, ab[:len(ab) - len(u)], ziel)
    if u:
        z2 = abschnitt_url(z, k, m.group("uk%d" % i), lang)
        if z2 is None:
            fehlt.append("%s %d: %s" % (z["ziel"], k, m.group(0)))
            return out + u
        out += m.group("uc%d" % i) + "[%s](%s)" % (m.group("ut%d" % i), z2)
    return out


# ----------------------------------------------------------------------------- LaTeX lesen -------
# Mathe-Umgebungen stehen auch in $...$ im Fließtext (pmatrix, cases): Sie sind keine Blöcke.
TOK = re.compile(r"\\begin\{(?!pmatrix|bmatrix|vmatrix|matrix|smallmatrix|cases|aligned|array|gathered|split)([A-Za-z]+\*?)\}|\\(section|subsection)(\*?)\{|\\paragraph\{|\\\[|\\loesung\{|\\captionof\{|\\caption\{|\\szenenabb\{|\\par\b")
TEXT_IGNORE = {"bigskip", "medskip", "smallskip", "noindent", "clearpage", "newpage", "centering", "small", "footnotesize",
               "large", "Large", "LARGE", "normalsize", "bfseries", "itshape", "raggedright", "thispagestyle", "tableofcontents",
               "ignorespaces", "protect", "sloppy", "linebreak", "pagebreak", "nopagebreak", "allowbreak", "scriptsize", "newline",
               "nobreak"}
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


def makros(m, extra=()):
    for a, b in tuple(extra) + MAKROS:                   # Makros der Modul-Präambel zuerst (\vx ist dort \mathbf{x})
        m = re.sub(re.escape(a) + r"(?![a-zA-Z])", lambda _: b, m)
    return m

def strip_comments(s):
    """%-Kommentare entfernen, aber nicht in Code-Umgebungen, \\verb|..|, \\lstinline|..| und \\url{..} (dort ist % ein Zeichen)."""
    out, i = [], 0
    for m in VERBATIM_RE.finditer(s):
        seg = s[i:m.start()]
        if re.search(r"(?<!\\)%", seg[seg.rfind("\n") + 1:]):
            continue                                     # steht selbst in einem Kommentar (geschützte Stücke davor zählen nicht)
        out.append(re.sub(r"(?<!\\)%.*", "", s[i:m.start()]))
        out.append(m.group(0))
        i = m.end()
    out.append(re.sub(r"(?<!\\)%.*", "", s[i:]))
    return "".join(out)


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
    def __init__(self, lang, kap, szenen, labels=None, basis=None, extra=(), hinweis=None):
        self.lang, self.kap, self.szenen = lang, kap, szenen
        self.extra = extra                           # Makros der Modul-Präambel
        self.hinweis = hinweis or HINWEIS
        self.code = []                               # Code-Blöcke; im Text bis zum Schluss als @@CODE:n@@
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
        m = makros(m, self.extra)
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
            return "`" + tt_text(a) + "`", j
        if name in ("verb", "lstinline"):                # \verb|..|, \lstinline|..| oder \lstinline{..}: Wortlaut
            if s[i:i + 1] == "*":
                i += 1
            if name == "lstinline" and s[i:i + 1] == "{":
                a, j = group(s, i)
            else:
                d = s[i]
                j = s.index(d, i + 1)
                a, j = s[i + 1:j], j + 1
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
                    out.append(self.hinweis[self.lang])
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
            elif tok == "\\szenenabb{":                  # \szenenabb{szene}{Bildunterschrift}{label} (Präambel): Editor-Szene
                szene, j = group(s, m.end() - 1)
                j = len(s) - len(s[j:].lstrip())
                cap, j = group(s, j)
                j = len(s) - len(s[j:].lstrip())
                lab, j = group(s, j)
                out.append(self.szenenabb(szene.strip(), cap, lab.strip()))
                i = j
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
            if re.match(r"(Lösungen|Solutions|Soluciones|解答|Çözümler)\s*$", t):
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

    def szenenabb(self, szene, cap, label):
        """\\szenenabb{szene}{cap}{label}: nummeriert wie eine abb-Umgebung, die Szene steht im ersten Argument (das PDF
        zeigt ihr Endbild, die Website die Szene selbst, mit Animation, wenn es eine animierte Fassung gibt)."""
        self.fig += 1
        self.last = (str(self.fig), "abb-%d" % self.fig)
        if label:
            self.setlabel(label)
        return ":::abbildung %s/%s %d\n%s\n:::" % (self.szenen, szene, self.fig, self.text(cap))

    def _abb(self, label, cap):
        n = re.sub(r"^fig:", "", label)
        if not re.match(r"k\d", n):
            n = "k%d%s" % (self.kap, n)
        return ":::abbildung %s/%s %d\n%s\n:::" % (self.szenen, n, self.fig, self.text(cap))

    def codeblock(self, name, body):
        """Code-Umgebung -> ```<sprache> <titel> … ```, im Text vorerst als @@CODE:n@@: So ändert kein späterer Schritt
        (WEBTEXT, Teil-Links, Teilung an ##/###, KaTeX-Prüfung) etwas am Code."""
        titel = ""
        m = re.match(r"[ \t]*\[([^\]\n]*)\]", body)
        if m:
            titel, body = self.text(m.group(1)), body[m.end():]
        body = body.split("\n", 1)[1] if "\n" in body else ""     # Rest der \begin-Zeile übergeht listings
        zeilen = body.expandtabs(4).rstrip().split("\n")
        while zeilen and not zeilen[0].strip():
            zeilen.pop(0)
        zeilen = [z.rstrip() for z in zeilen]
        self.code.append("```%s%s\n%s\n```" % (CODE_ENVS[name], " " + titel if titel else "", "\n".join(zeilen)))
        return "@@CODE:%d@@" % (len(self.code) - 1)

    def environment(self, name, body):
        if name in CODE_ENVS:
            return self.codeblock(name, body)
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
            wort = {"de": "Tabelle", "en": "Table", "es": "Tabla", "zh": "表", "fr": "Tableau", "tr": "Tablo"}.get(self.lang, "Tabelle")
            kopf = '<span class="anker" id="tab-%d"></span>\n\n**%s %d:** %s' % (self.tab, wort, self.tab, self.text(cap))
            return kopf + "\n\n" + self.block(body)
        if name == "zweck":
            return ":::zweck\n%s\n:::" % self.block(body)
        if name == "analogie":
            return ":::analogie\n%s\n:::" % self.block(body)
        if name == "beispiel":                           # \begin{beispiel}[Wort]{Titel} -> ::::beispiel [Wort] Titel … :::: (zugeklappt)
            opt, j = bracket(body, 0)
            t, j = group(body, body.index("{", j))
            wort, title = self.text(opt or "").strip(), re.sub(r"\.$", "", self.text(t).strip())
            kopf = ("[%s] " % wort if wort or title.startswith("[") else "") + title
            return "::::beispiel%s\n%s\n::::" % (" " + kopf.strip() if kopf.strip() else "", self.block(body[j:]))
        if name in ("merkbox", "kernbox", "herleitung", "beweis", "vertiefung", "frage", "qa", "ltspice", "hintergrund", "warnung"):
            t, j = group(body, body.index("{"))
            title = self.text(t)
            inner = self.block(body[j:])
            kind = {"merkbox": "merke", "kernbox": "kern" if title in KERN_TITEL else "merke", "herleitung": "herleitung", "beweis": "beweis",
                    "vertiefung": "zusatz", "frage": "frage", "qa": "frage", "ltspice": "ltspice", "hintergrund": "hintergrund",
                    "warnung": "warnung"}[name]
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
        # ein | außerhalb der Mathematik (etwa in `ls | wc -l`) ist Inhalt, kein Zellentrenner: als \| schreiben (GFM),
        # build_wissen trennt nur an ungeschützten | und macht daraus wieder |
        return re.sub(r"\$[^$]*\$", bar, t).replace("|", "\\|")


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
        h = Heft(lang, kap, cfg["szenen"], labels, extra=modul_makros(cfg), hinweis=cfg.get("hinweis"))
        return h, h.block(body)
    h, _ = run({})
    h, md = run(h.neu)
    for lab, sol in h.sol.items():
        md = md.replace("@@LOESUNG:%s@@" % lab, ":::loesung\n%s\n:::" % sol)
    rest = re.findall(r"@@LOESUNG:([^@]*)@@", md)
    md = re.sub(r"@@LOESUNG:[^@]*@@\n?", "", md)
    teile = "/wissen/%s%s" % ("" if lang == "de" else lang + "/", cfg["basis"])
    return h, md, tt, sub, rest, teile


def webtext(md, lang, cfg, teile, kap=None, fehlt=None):
    """Texte anpassen, die nur im PDF stimmen; Verweise („Kapitel 3“, „Python, Kapitel 2, Abschnitt 4.1“, übergangsweise
    „Teil 3“) werden zu Links. Formeln, Code, Überschriften und Blockköpfe bleiben. Mit kap (immer, außer in alten Aufrufen):
    alle Verweisarten aus verweis_arten, mit Abschnitt und Anker; fehlt sammelt Abschnitte ohne Ziel. Ohne kap nur „Teil N“."""
    def subs(t):
        for a, b in WEBTEXT[lang]:
            t = t.replace(a, b)
        return t
    def link(m):
        k = int(m.group(1))
        if k not in cfg["hefte"] or not (cfg["quelle"] / (cfg["hefte"][k][0] + ".tex")).is_file():
            return m.group(0)                            # (noch) kein Heft: Text ohne Link
        if lang != "de" and not list(cfg["quelle"].glob("kap%d_stufen*_%s.tex" % (k, lang))):
            return m.group(0)                            # noch nicht übersetzt: Text ohne Link, sonst läuft er ins Leere
        _, slug, thema = cfg["hefte"][k]
        return "[%s](%s/%s/%s.html)" % (m.group(0), teile, slugify(thema["de"]), slug)
    teil_re = TEIL_RE[lang]
    if kap is not None:
        arten = verweis_arten(cfg, kap, lang)
        teil_re = verweis_regex(arten, lang)
        fehlt = [] if fehlt is None else fehlt
        link = lambda m: verweis_link(m, arten, lang, fehlt)   # noqa: E731
    out = []
    for line in md.split("\n"):
        plain = line.startswith(("#", ":::", "<", "|", "$$"))
        pieces = re.split(r"(\$\$.*?\$\$|\$[^$]*\$|`[^`]*`|\]\([^)]*\))", line)
        for i in range(0, len(pieces), 2):
            pieces[i] = subs(pieces[i])
            if lang == "fr" and not line.startswith("<"):
                pieces[i] = fr_typo(pieces[i])
            if not plain:
                pieces[i] = re.sub(teil_re, link, pieces[i])
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
        # Beispiele zählen mit (sie gehören zum Artikel), nur ihre Rahmenzeilen nicht: So teilt der Kasten keinen Abschnitt neu.
        laenge = len(re.sub(r"(?m)^::::(?:beispiel\b.*)?\n?", "", t))
        gross = laenge > grenze and len(stuecke) > 1 if teilen is None else nr in teilen
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
        a = re.search(r"(?ms)^:::merke ((?:%s)[^\n(（]*)[^\n]*\n(.*?)^:::\n" % ANTWORT_RE, out[0]["md"])
        if a:                                            # nennt Ergebnisse, die man am Anfang nicht kennt
            out[0]["md"] = out[0]["md"][:a.start()] + out[0]["md"][a.end():]
            ende["md"] = ":::merke " + a.group(1).strip() + "\n" + a.group(2) + ":::\n\n" + ende["md"]
        p = re.search(r"(?ms)^\u2060?\*\*(?:%s)[^\n]*\n\n(?:\|[^\n]*\n)+" % PRINZIP_RE, out[0]["md"])
        if p:
            out[0]["md"] = out[0]["md"][:p.start()] + out[0]["md"][p.end():]
            ende["md"] = ende["md"].rstrip() + "\n\n" + p.group(0)
        out.append(ende)
    return out


GETEILT = set()                                          # von abschnitte() gefüllt: geteilte Abschnitte der deutschen Fassung


def datei_stamm(cfg, kap, stuecke):
    """Dateinamen aus den deutschen Titeln: 01-<kapitel>, 02-<stufe>, ... (der erste bleibt der Name des Kapitels)."""
    _, slug, _ = cfg["hefte"][kap]
    namen, frei = ["01-" + slug], {slug}
    ordner = heft_ordner(cfg, kap)
    for i, a in enumerate(stuecke[1:], 2):
        t = re.sub(r"^Stufe\s+\d+:\s*", "", a["titel"])
        t = re.sub(r"\$[^$]*\$", " ", t)
        s, n = slugify(t), 1
        if re.search(r"(?<![a-z])kapiteln?-\d", s):     # Adresse bleibt: „Was aus Kapitel 9 …“ hieß bis 09.11.2026 „Teil 9“
            for w in ("teil", "teile", "teilen", "grundlagen", "python", "linux"):
                alt = re.sub(r"(?<![a-z])kapiteln?-(\d)", w + r"-\1", s)
                if ordner.is_dir() and list(ordner.glob("*-%s.md" % alt)):
                    s = alt
                    break
        while (s if n == 1 else "%s-%d" % (s, n)) in frei:   # gleiche Adresse wie der Überblick oder ein anderer Abschnitt
            n += 1                                           # („Wahrscheinlichkeit“ in Grundlagen 4): -2, -3 …
        s = s if n == 1 else "%s-%d" % (s, n)
        frei.add(s)
        namen.append("%02d-%s" % (i, s))
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
    h.verweis_fehlt = []                                 # „Grundlagen 1, Abschnitt 99“: Heft da, Abschnitt nicht
    md = webtext(md, lang, cfg, teile, kap, h.verweis_fehlt)
    _, de, *_ = convert(cfg, kap, "de")
    GETEILT.clear()
    namen = datei_stamm(cfg, kap, abschnitte(webtext(de, "de", cfg, "", kap, [])))
    stuecke = abschnitte(md, set(GETEILT))
    if len(namen) != len(stuecke):
        raise ValueError("Kap. %d %s: %d Artikel, deutsch %d" % (kap, lang, len(stuecke), len(namen)))
    fehlt = verweise(stuecke, namen)
    b = bereich(cfg, kap)                                # „Kapitel 1: …“ im Baum (knoten:), der Überblick ohne Nummer
    aus = []
    for i, (a, n) in enumerate(zip(stuecke, namen), 1):
        if a["art"] == "ueberblick":
            titel, kurz, info = "%s: %s" % (UEBERBLICK[lang], tt), UEBERBLICK[lang], sub
            if lang == "fr":                             # Titelblock kommt nicht durch webtext
                titel, info = fr_typo(titel), fr_typo(info)
        else:
            titel, kurz, info = a["titel"], "", kurztext(a["md"], sub)
        info = re.sub(r"\$([^$]+)\$", lambda mm: "$" + makros(mm.group(1), h.extra) + "$", info)   # Präambel-Makros wie \ee
        kopf = ["---", "title: " + titel] + (["kurz: " + kurz] if kurz else []) + ["pfad: " + heft_pfad(cfg, kap, lang),
            "adresse: " + heft_adresse(cfg, kap), "knoten: " + knoten_name(cfg, kap, lang)] + (
            ["nachschlagen: ja"] if b and b.get("nachschlagen") else []) + [
            "order: %d" % (cfg["order"] + (b.get("order", 0) if b else 0) + kap * 10000 + 100 * i),
            "summary: " + info, "tags: " + begriffe(a["md"]), "lang: " + lang, "---", ""]
        text = re.sub(r"@@CODE:(\d+)@@", lambda mm: h.code[int(mm.group(1))], a["md"].strip())   # Code erst ganz zum Schluss
        aus.append((n, "\n".join(kopf) + "\n" + text + "\n"))
    return aus, h, rest, fehlt


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("modul", choices=sorted(MODULE))
    ap.add_argument("--kap", type=int, nargs="*")
    ap.add_argument("--lang", nargs="*", choices=LANGS, help="Sprachen (Standard: de und jede Sprache mit Heftdatei)")
    ap.add_argument("--pruefen", action="store_true")
    ap.add_argument("--aux", help="Ordner mit .aux-Dateien: Nummern vergleichen")
    ap.add_argument("--katex", action="store_true", help="alle Formeln mit KaTeX rendern (Fehler melden)")
    a = ap.parse_args()
    cfg = MODULE[a.modul]
    fehler = 0
    alle = []
    for kap in a.kap or sorted(cfg["hefte"]):
        stem, slug, thema = cfg["hefte"][kap]
        if not (cfg["quelle"] / (stem + ".tex")).is_file():
            if a.kap:
                print("⚠ Kap. %d: %s.tex fehlt" % (kap, stem))
                fehler += 1
            continue                                     # Reihe im Aufbau: Heft noch nicht geschrieben
        langs = a.lang
        name = heft_name(cfg, kap, "de")
        if not langs:                                    # Standard: Deutsch und jede schon übersetzte Sprache
            langs = [l for l in LANGS if l == "de" or (cfg["quelle"] / ("%s_%s.tex" % (stem, l))).is_file()]
            offen = [l for l in LANGS if l not in langs]
            if offen:
                print("· Kap. %d (%s): noch nicht übersetzt: %s" % (kap, name, ", ".join(offen)))
        for lang in langs:
            if lang != "de" and not (cfg["quelle"] / ("%s_%s.tex" % (stem, lang))).is_file():
                print("⚠ Kap. %d %s: %s_%s.tex fehlt (noch nicht übersetzt)" % (kap, lang, stem, lang))
                fehler += 1
                continue
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
            if h.verweis_fehlt:
                msg.append("Verweise auf fehlende Abschnitte: " + "; ".join(sorted(set(h.verweis_fehlt))))
            if a.aux:
                msg += aux_vergleich(Path(a.aux) / ((stem + ("" if lang == "de" else "_" + lang)) + ".aux"), h)
            if not a.pruefen:
                ordner.mkdir(parents=True, exist_ok=True)
                endung = "" if lang == "de" else "." + lang
                for alt in ordner.glob("*.md"):                  # nur die alte Fassung dieser Sprache weg, Hand-Artikel bleiben
                    m = re.search(r"\.(%s)$" % "|".join(l for l in LANGS if l != "de"), alt.stem)
                    if "-mensch" not in alt.name and (m.group(1) if m else "de") == lang:
                        alt.unlink()
                for n, t in arts:
                    (ordner / (n + endung + ".md")).write_text(t, encoding="utf-8", newline="\n")
                _ANKER.pop((cfg["ziel"], kap), None)             # spätere Hefte verweisen auf die neuen Abschnitte
            print(("⚠ " if msg else "✓ ") + ("Kap. %d (%s)" % (kap, name))
                  + " %s: %d Artikel, %d Zeichen, %d Abb., %d Aufg." % (lang, len(arts), len(txt), h.fig, h.aufg))
            for x in msg:
                print("    " + x)
                fehler += 1
    if cfg.get("reihe_hinweis") and not a.pruefen:
        reihe_hinweis(cfg)
    if a.katex:
        for t, e in katex_pruefen(alle):
            print("⚠ KaTeX:", t, "\n    ", e)
            fehler += 1
    return 1 if fehler else 0


def reihe_hinweis(cfg):
    """content/<ziel>/_reihe[.<lang>].md: kurzer Text, den die Übersicht der Website unter dem Modul zeigt (build_wissen:
    Dateien mit „_“ sind keine Artikel; „hinweis:“ nennt den Knoten im Baum der Sprache)."""
    d = ROOT / "content" / cfg["ziel"]
    d.mkdir(parents=True, exist_ok=True)
    for lang, text in cfg["reihe_hinweis"].items():
        text = fr_typo(text) if lang == "fr" else text
        kopf = ["---", "hinweis: " + cfg["pfad"][lang], "lang: " + lang, "---", ""]
        (d / ("_reihe%s.md" % ("" if lang == "de" else "." + lang))).write_text("\n".join(kopf) + "\n" + text + "\n",
                                                                                encoding="utf-8", newline="\n")


def katex_pruefen(texte):
    """Rendert alle Formeln mit dem KaTeX der Website und gibt [(Formel, Fehler)] zurück (braucht Playwright und Netz)."""
    from playwright.sync_api import sync_playwright
    items = []
    for s in texte:
        s = re.sub(r"(?ms)^```.*?^```[ \t]*$", "", s)     # Code-Blöcke ($ ist dort Prompt oder Variable, keine Formel)
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
