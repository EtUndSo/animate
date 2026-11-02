# Zusatz zur Heft-Übersetzung: Höhere Mathematik 1 (Modul hm1)

Es gilt notizen/heft_uebersetzung.md, mit diesen Abweichungen:

- Heftordner: C:\Bücher\HöMa1\Arbeitshefte. Prüfung: `python tools/heft_zu_artikel.py hm1 --kap <N> --lang en es zh --pruefen --katex --aux "C:/Bücher/HöMa1/Arbeitshefte"` vor dem Löschen der .aux.
- Vorbild: die fertigen Fassungen in C:\Bücher\ET1\Arbeitshefte (kap1_stufen_en.tex usw.) und die Fassungen von Teil 1 der Mathematik, sobald sie vorliegen. Bildwörter in tools/szenen/hm1_teil<N>.py (`s.tr`) sind verbindlich.
- Umgebung `beweis` bleibt `beweis`, die Präambeln liefern das Wort je Sprache. Listen, Labels und Sätze bleiben wie im Deutschen.
- Bezeichnungen bleiben: i als imaginäre Einheit, log, Mengenschreibweise. Dezimaltrennzeichen wie im Hauptauftrag.
- Zahlentrennung: In Mathematik kommt die Dezimalzahl oft neben Intervallen vor. Spanische Intervalle wie [0{,}5;\,1] behalten das Semikolon aus dem Original, wenn eines dasteht. Englisch und Chinesisch: [0.5, 1].

Fachwörter (de | en | es | zh):

Menge | set | conjunto | 集合
Aussage | statement | proposición | 命题
Quantor | quantifier | cuantificador | 量词
Körper | field | cuerpo | 域
Anordnung | order | orden | 序
vollständige Induktion | mathematical induction | inducción matemática | 数学归纳法
Vollständigkeit | completeness | completitud | 完备性
Betrag | absolute value | valor absoluto | 绝对值
komplexe Zahl | complex number | número complejo | 复数
konjugiert komplex | complex conjugate | conjugado complejo | 共轭复数
Polynom | polynomial | polinomio | 多项式
rationale Funktion | rational function | función racional | 有理函数
Folge | sequence | sucesión | 数列
Grenzwert | limit | límite | 极限
Nullfolge | null sequence | sucesión nula | 零数列
Cauchy-Folge | Cauchy sequence | sucesión de Cauchy | 柯西数列
Häufungspunkt | accumulation point | punto de acumulación | 聚点
Teilfolge | subsequence | subsucesión | 子数列
stetig | continuous | continua | 连续
Zwischenwertsatz | intermediate value theorem | teorema del valor intermedio | 介值定理
Reihe | series | serie | 级数
Teilsumme | partial sum | suma parcial | 部分和
absolut konvergent | absolutely convergent | absolutamente convergente | 绝对收敛
Potenzreihe | power series | serie de potencias | 幂级数
Konvergenzradius | radius of convergence | radio de convergencia | 收敛半径
Vektorraum | vector space | espacio vectorial | 向量空间
Unterraum | subspace | subespacio | 子空间
Skalarprodukt | dot product (inner product) | producto escalar | 内积
Norm | norm | norma | 范数
linear unabhängig | linearly independent | linealmente independiente | 线性无关
Vektorprodukt | cross product | producto vectorial | 向量积
Spatprodukt | scalar triple product | producto mixto | 混合积
Basis | basis | base | 基
Orthonormalbasis | orthonormal basis | base ortonormal | 标准正交基
lineare Abbildung | linear map | aplicación lineal | 线性映射
Kern | kernel | núcleo | 核
Bild | image | imagen | 像
Rang | rank | rango | 秩
Gleichungssystem | system of equations | sistema de ecuaciones | 方程组
