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
        "pfad": {"de": "Elektrotechnik / 3. Semester / Signale und Systeme",
                 "en": "Electrical Engineering / 3rd Semester / Signals and Systems",
                 "es": "Ingeniería eléctrica / 3.er semestre / Señales y sistemas",
                 "zh": "电气工程 / 第 3 学期 / 信号与系统",
                 "fr": "Génie électrique / 3e semestre / Signaux et systèmes",
                 "tr": "Elektrik Mühendisliği / 3. Yarıyıl / Sinyaller ve Sistemler"},
        "basis": "elektrotechnik/3-semester/signale-und-systeme",
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
    "pfad": {"de": "Elektrotechnik / 1. Semester / Grundlagen der Elektrotechnik",
             "en": "Electrical Engineering / 1st Semester / Fundamentals of Electrical Engineering",
             "es": "Ingeniería eléctrica / 1.er semestre / Fundamentos de ingeniería eléctrica",
             "zh": "电气工程 / 第 1 学期 / 电气工程基础",
             "fr": "Génie électrique / 1er semestre / Fondements du génie électrique",
             "tr": "Elektrik Mühendisliği / 1. Yarıyıl / Elektrik Mühendisliğinin Temelleri"},
    "basis": "elektrotechnik/1-semester/grundlagen-der-elektrotechnik",
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
    "pfad": {"de": "Elektrotechnik / 1. Semester / Höhere Mathematik 1",
             "en": "Electrical Engineering / 1st Semester / Higher Mathematics 1",
             "es": "Ingeniería eléctrica / 1.er semestre / Matemáticas superiores 1",
             "zh": "电气工程 / 第 1 学期 / 高等数学 1",
             "fr": "Génie électrique / 1er semestre / Mathématiques supérieures 1",
             "tr": "Elektrik Mühendisliği / 1. Yarıyıl / Yüksek Matematik 1"},
    "basis": "elektrotechnik/1-semester/hohere-mathematik-1",
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
    "pfad": {"de": "Elektrotechnik / 4. Semester / Elektronische Materialien und Bauelemente 1",
             "en": "Electrical Engineering / 4th Semester / Electronic Materials and Devices 1",
             "es": "Ingeniería eléctrica / 4.º semestre / Materiales y dispositivos electrónicos 1",
             "zh": "电气工程 / 第 4 学期 / 电子材料与器件 1",
             "fr": "Génie électrique / 4e semestre / Matériaux et composants électroniques 1",
             "tr": "Elektrik Mühendisliği / 4. Yarıyıl / Elektronik Malzemeler ve Elemanlar 1"},
    "basis": "elektrotechnik/4-semester/elektronische-materialien-und-bauelemente-1",
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
            {"de": "Ergänzung: Licht und Laser", "en": "Supplement: Light and Lasers",
             "es": "Complemento: luz y láser", "zh": "补充：光与激光",
             "fr": "Complément\u00a0: lumière et laser", "tr": "Ek: Işık ve Lazer"}),
        20: ("Kap20_Realkristall", "ergaenzung-reale-kristalle",
            {"de": "Ergänzung: Reale Kristalle und amorphe Stoffe", "en": "Supplement: Real Crystals and Amorphous Solids",
             "es": "Complemento: cristales reales y sólidos amorfos", "zh": "补充：实际晶体与非晶固体",
             "fr": "Complément\u00a0: cristaux réels et solides amorphes", "tr": "Ek: Gerçek Kristaller ve Amorf Katılar"}),
        21: ("Kap21_Zustandsdiagramme", "ergaenzung-zustandsdiagramme",
            {"de": "Ergänzung: Zustandsdiagramme", "en": "Supplement: Phase Diagrams",
             "es": "Complemento: diagramas de fases", "zh": "补充：相图",
             "fr": "Complément\u00a0: diagrammes de phases", "tr": "Ek: Faz Diyagramları"}),
        22: ("Kap22_Vielteilchen", "ergaenzung-vielteilchensysteme",
            {"de": "Ergänzung: Vielteilchensysteme", "en": "Supplement: Many-Particle Systems",
             "es": "Complemento: sistemas de muchas partículas", "zh": "补充：多粒子系统",
             "fr": "Complément\u00a0: systèmes à plusieurs particules", "tr": "Ek: Çok Parçacıklı Sistemler"}),
        23: ("Kap23_Entropie", "ergaenzung-entropie-und-gleichgewicht",
            {"de": "Ergänzung: Entropie und Gleichgewicht", "en": "Supplement: Entropy and Equilibrium",
             "es": "Complemento: entropía y equilibrio", "zh": "补充：熵与平衡",
             "fr": "Complément\u00a0: entropie et équilibre", "tr": "Ek: Entropi ve Denge"}),
        24: ("Kap24_Gitterschwingungen", "ergaenzung-gitterschwingungen",
            {"de": "Ergänzung: Gitterschwingungen", "en": "Supplement: Lattice Vibrations",
             "es": "Complemento: vibraciones de la red", "zh": "补充：晶格振动",
             "fr": "Complément\u00a0: vibrations du réseau", "tr": "Ek: Örgü Titreşimleri"}),
        25: ("Kap25_Metalle", "ergaenzung-metalle",
            {"de": "Ergänzung: Metalle", "en": "Supplement: Metals",
             "es": "Complemento: metales", "zh": "补充：金属",
             "fr": "Complément\u00a0: métaux", "tr": "Ek: Metaller"}),
        26: ("Kap26_Schottky", "ergaenzung-metall-halbleiter-uebergang",
            {"de": "Ergänzung: Metall-Halbleiter-Übergang", "en": "Supplement: Metal-Semiconductor Junction",
             "es": "Complemento: unión metal-semiconductor", "zh": "补充：金属-半导体结",
             "fr": "Complément\u00a0: jonction métal-semi-conducteur", "tr": "Ek: Metal-Yarı İletken Eklemi"}),
        27: ("Kap27_Feldeffekt", "ergaenzung-weitere-feldeffekt-bauelemente",
            {"de": "Ergänzung: Weitere Feldeffekt-Bauelemente", "en": "Supplement: Other Field-Effect Devices",
             "es": "Complemento: otros dispositivos de efecto de campo", "zh": "补充：其他场效应器件",
             "fr": "Complément\u00a0: autres composants à effet de champ", "tr": "Ek: Diğer Alan Etkili Elemanlar"}),
        28: ("Kap28_Prozess", "ergaenzung-halbleitertechnologie",
            {"de": "Ergänzung: Halbleitertechnologie", "en": "Supplement: Semiconductor Technology",
             "es": "Complemento: tecnología de semiconductores", "zh": "补充：半导体工艺",
             "fr": "Complément\u00a0: technologie des semi-conducteurs", "tr": "Ek: Yarı İletken Teknolojisi"}),
    },
}

MODULE["hm3"] = {
    "quelle": Path(r"C:\Bücher\HöMa3\Arbeitshefte"),
    "ziel": "hm3",
    "szenen": "hm3",
    "pfad": {"de": "Elektrotechnik / 3. Semester / Höhere Mathematik 3",
             "en": "Electrical Engineering / 3rd Semester / Higher Mathematics 3",
             "es": "Ingeniería eléctrica / 3.er semestre / Matemáticas superiores 3",
             "zh": "电气工程 / 第 3 学期 / 高等数学 3",
             "fr": "Génie électrique / 3e semestre / Mathématiques supérieures 3",
             "tr": "Elektrik Mühendisliği / 3. Yarıyıl / Yüksek Matematik 3"},
    "basis": "elektrotechnik/3-semester/hohere-mathematik-3",
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
    "abschnitt_links": True,
    "hinweis": HINWEIS_CYBER,
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
    "abschnitt_links": True,
    "hinweis": HINWEIS_ML,
    # Bereiche (Entscheidung des Users, 05./06.11.2026): T01-T06 = „Grundlagen 1-6“ zum Nachschlagen in einem eigenen
    # Ast, der ML-Pfad zählt ab T08 als „Teil 1“ (Teil N = T(N+7)); T07 Python/NumPy entfällt (Bereich „Programmieren“).
    # Dateien, Ordner unter content/ und Szenen behalten die Lernpfad-Nummer (Kap1_Vektoren, ml/k1…).
    "bereiche": (
        {"kaps": (1, 6), "nr": 0, "nachschlagen": True, "order": 9000000,      # im Baum nach dem Pfad
         "pfad": {"de": "Mathematische Grundlagen", "en": "Mathematical Foundations", "es": "Fundamentos matemáticos",
                  "zh": "数学基础", "fr": "Fondements mathématiques", "tr": "Matematiksel Temeller"},
         "name": {"de": "Grundlagen {n}", "en": "Foundations {n}", "es": "Fundamentos {n}", "zh": "基础篇 {n}",
                  "fr": "Fondements {n}", "tr": "Temeller {n}"}},
        {"kaps": (8, 99), "nr": 7, "teil": True,
         "name": {"de": "Teil {n}", "en": "Part {n}", "es": "Parte {n}", "zh": "第 {n} 部分", "fr": "Partie {n}",
                  "tr": "Kısım {n}"}},
    ),
    "reihe_hinweis": {                                   # auf der Übersicht unter „Machine Learning“
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
        "fr": "Les fondements mathématiques sont faits pour être consultés ; il n’est pas nécessaire de les étudier "
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
# ML und Cybersecurity setzen sie voraus und verweisen mit „Programmieren, Python N, Abschnitt M“ bzw. „Linux N, Abschnitt M“
# (Wendungen je Sprache: "praefix", Bereichsnamen, ABSCHNITT_RE). Hefte trägt der Schreib-Agent hier ein, sobald der
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
    "abschnitt_links": True,
    "hinweis": HINWEIS_ML,
    # Verweise von überall nur mit Bereichsnamen davor: „Python 3“ allein ist meist die Sprachversion
    "praefix": {"de": "Programmieren, ", "en": "Programming, ", "es": "Programación, ", "zh": "编程，",
                "fr": "Programmation, ", "tr": "Programlama, "},
    "bereiche": (                                        # Python 1, 2, … = Kap1, Kap2, …; C ab Kap101, C++ ab Kap201
        {"kaps": (1, 99), "nr": 0, "pfad": {l: "Python" for l in LANGS},
         "name": {l: "Python {n}" for l in LANGS}},
        {"kaps": (101, 199), "nr": 100,
         "pfad": {"de": "C und C++", "en": "C and C++", "es": "C y C++", "zh": "C 与 C++", "fr": "C et C++", "tr": "C ve C++"},
         "name": {l: "C {n}" for l in LANGS}},
        {"kaps": (201, 299), "nr": 200,
         "pfad": {"de": "C und C++", "en": "C and C++", "es": "C y C++", "zh": "C 与 C++", "fr": "C et C++", "tr": "C ve C++"},
         "name": {l: "C++ {n}" for l in LANGS}},
    ),
    "hefte": {},                                         # Nummer: ("Kap<N>_<Name>", "slug", {Titel je Sprache}) wie bei ml
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
    "abschnitt_links": True,
    "hinweis": HINWEIS_CYBER,
    "extern": True,                                      # „Linux N, Abschnitt M“ ist von jedem Modul mit abschnitt_links aus ein Link
    "bereiche": (
        {"kaps": (1, 99), "nr": 0, "name": {l: "Linux {n}" for l in LANGS}},
    ),
    "hefte": {},
}

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
TEIL_RE = {"de": r"\bTeil(?:e|en)?[ \u00a0](\d+)\b", "en": r"\bPart[ \u00a0](\d+)\b", "es": r"\b[Pp]arte[ \u00a0](\d+)\b",
           "zh": r"第[ \u00a0]?(\d+)[ \u00a0]?部分"}
TEIL_RE.update({"fr": r"\b[Pp]artie[ \u00a0](\d+)\b", "tr": r"\b[Kk]ısım[ \u00a0](\d+)\b"})   # „Partie 3“, „Kısım 3“
# Französisch: geschütztes Leerzeichen vor : (\u00a0), vor ; ! ? (\u202f) und in « » (\u00a0), wie babel-french im PDF.
# webtext ruft es nur für Text außerhalb von Formeln, Code und Link-Zielen auf; ein ":::"-Blockkopf bleibt unberührt.
FR_VOR = re.compile(r"(?<=[\w)\]*’'”»])[ \t]?([:;!?])(?=\s|$|\*)")
FR_AUF, FR_ZU = re.compile(r"«[ \t\u00a0\u202f]*"), re.compile(r"(?<=\S)[ \t\u00a0\u202f]*»")


def fr_typo(t):
    t = FR_VOR.sub(lambda m: ("\u00a0" if m.group(1) == ":" else "\u202f") + m.group(1), t)
    return FR_ZU.sub("\u00a0»", FR_AUF.sub("«\u00a0", t))


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


def webtext(md, lang, cfg, teile):
    """Texte anpassen, die nur im PDF stimmen; „Teil 3“ wird zum Link. Formeln, Code, Überschriften und Blockköpfe bleiben."""
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
    out = []
    for line in md.split("\n"):
        plain = line.startswith(("#", ":::", "<", "|", "$$"))
        pieces = re.split(r"(\$\$.*?\$\$|\$[^$]*\$|`[^`]*`|\]\([^)]*\))", line)
        for i in range(0, len(pieces), 2):
            pieces[i] = subs(pieces[i])
            if lang == "fr" and not line.startswith("<"):
                pieces[i] = fr_typo(pieces[i])
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
            if lang == "fr":                             # Titelblock kommt nicht durch webtext
                titel, info = fr_typo(titel), fr_typo(info)
        else:
            titel, kurz, info = a["titel"], "", kurztext(a["md"], sub)
        info = re.sub(r"\$([^$]+)\$", lambda mm: "$" + makros(mm.group(1), h.extra) + "$", info)   # Präambel-Makros wie \ee
        kopf = ["---", "title: " + titel] + (["kurz: " + kurz] if kurz else []) + [
            "pfad: %s / %s" % (cfg["pfad"][lang], thema[lang]), "order: %d" % (cfg["order"] + kap * 10000 + 100 * i),
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
                print("⚠ Teil %d: %s.tex fehlt" % (kap, stem))
                fehler += 1
            continue                                     # Reihe im Aufbau: Teil noch nicht geschrieben
        langs = a.lang
        if not langs:                                    # Standard: Deutsch und jede schon übersetzte Sprache
            langs = [l for l in LANGS if l == "de" or (cfg["quelle"] / ("%s_%s.tex" % (stem, l))).is_file()]
            offen = [l for l in LANGS if l not in langs]
            if offen:
                print("· Teil %d: noch nicht übersetzt: %s" % (kap, ", ".join(offen)))
        for lang in langs:
            if lang != "de" and not (cfg["quelle"] / ("%s_%s.tex" % (stem, lang))).is_file():
                print("⚠ Teil %d %s: %s_%s.tex fehlt (noch nicht übersetzt)" % (kap, lang, stem, lang))
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
