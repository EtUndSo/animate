# Zusatz zur Heft-Übersetzung: Höhere Mathematik 1 (Modul hm1)

Es gilt notizen/heft_uebersetzung.md, mit diesen Abweichungen:

- Heftordner: C:\Bücher\HöMa1\Arbeitshefte. Prüfung: `python tools/heft_zu_artikel.py hm1 --kap <N> --lang <Sprachen, z. B. en es zh oder fr tr> --pruefen --katex --aux "C:/Bücher/HöMa1/Arbeitshefte"` vor dem Löschen der .aux.
- Vorbild: die fertigen Fassungen in C:\Bücher\ET1\Arbeitshefte (kap1_stufen_en.tex usw.) und die Fassungen von Teil 1 der Mathematik, sobald sie vorliegen. Bildwörter in tools/szenen/hm1_teil<N>.py (`s.tr`) sind verbindlich.
- Umgebung `beweis` bleibt `beweis`, die Präambeln liefern das Wort je Sprache (Preuve, İspat). Listen, Labels und Sätze bleiben wie im Deutschen.
- Bezeichnungen bleiben: i als imaginäre Einheit, log, Mengenschreibweise. Dezimaltrennzeichen wie im Hauptauftrag (fr und tr: Komma).
- Zahlentrennung: In Mathematik kommt die Dezimalzahl oft neben Intervallen vor. Spanische, französische und türkische Intervalle wie [0{,}5;\,1] behalten das Semikolon aus dem Original, wenn eines dasteht (in Formeln setzt babel-french kein Leerzeichen davor). Englisch und Chinesisch: [0.5, 1].
- Französisch: vollständige Induktion heißt „raisonnement par récurrence“; „Folge“ ist „suite“, „Reihe“ „série“; „Potenzreihe“ „série entière“.

Fachwörter (de | en | es | zh | fr | tr):

Menge | set | conjunto | 集合 | ensemble | küme
Aussage | statement | proposición | 命题 | proposition | önerme
Quantor | quantifier | cuantificador | 量词 | quantificateur | niceleyici
Körper | field | cuerpo | 域 | corps | cisim
Anordnung | order | orden | 序 | ordre | sıralama
vollständige Induktion | mathematical induction | inducción matemática | 数学归纳法 | raisonnement par récurrence | tümevarım
Vollständigkeit | completeness | completitud | 完备性 | complétude | tamlık
Betrag | absolute value | valor absoluto | 绝对值 | valeur absolue | mutlak değer
komplexe Zahl | complex number | número complejo | 复数 | nombre complexe | karmaşık sayı
konjugiert komplex | complex conjugate | conjugado complejo | 共轭复数 | conjugué | karmaşık eşlenik
Polynom | polynomial | polinomio | 多项式 | polynôme | polinom
rationale Funktion | rational function | función racional | 有理函数 | fonction rationnelle | rasyonel fonksiyon
Folge | sequence | sucesión | 数列 | suite | dizi
Grenzwert | limit | límite | 极限 | limite | limit
Nullfolge | null sequence | sucesión nula | 零数列 | suite de limite nulle | sıfıra yakınsayan dizi
Cauchy-Folge | Cauchy sequence | sucesión de Cauchy | 柯西数列 | suite de Cauchy | Cauchy dizisi
Häufungspunkt | accumulation point | punto de acumulación | 聚点 | point d’accumulation | yığılma noktası
Teilfolge | subsequence | subsucesión | 子数列 | sous-suite | alt dizi
stetig | continuous | continua | 连续 | continue | sürekli
Zwischenwertsatz | intermediate value theorem | teorema del valor intermedio | 介值定理 | théorème des valeurs intermédiaires | ara değer teoremi
Reihe | series | serie | 级数 | série | seri
Teilsumme | partial sum | suma parcial | 部分和 | somme partielle | kısmi toplam
absolut konvergent | absolutely convergent | absolutamente convergente | 绝对收敛 | absolument convergente | mutlak yakınsak
Potenzreihe | power series | serie de potencias | 幂级数 | série entière | kuvvet serisi
Konvergenzradius | radius of convergence | radio de convergencia | 收敛半径 | rayon de convergence | yakınsaklık yarıçapı
Vektorraum | vector space | espacio vectorial | 向量空间 | espace vectoriel | vektör uzayı
Unterraum | subspace | subespacio | 子空间 | sous-espace vectoriel | alt uzay
Skalarprodukt | dot product (inner product) | producto escalar | 内积 | produit scalaire | skaler çarpım (iç çarpım)
Norm | norm | norma | 范数 | norme | norm
linear unabhängig | linearly independent | linealmente independiente | 线性无关 | linéairement indépendant | doğrusal bağımsız
Vektorprodukt | cross product | producto vectorial | 向量积 | produit vectoriel | vektörel çarpım
Spatprodukt | scalar triple product | producto mixto | 混合积 | produit mixte | karma çarpım
Basis | basis | base | 基 | base | baz
Orthonormalbasis | orthonormal basis | base ortonormal | 标准正交基 | base orthonormée | ortonormal baz
lineare Abbildung | linear map | aplicación lineal | 线性映射 | application linéaire | doğrusal dönüşüm
Kern | kernel | núcleo | 核 | noyau | çekirdek
Bild | image | imagen | 像 | image | görüntü
Rang | rank | rango | 秩 | rang | rank
Gleichungssystem | system of equations | sistema de ecuaciones | 方程组 | système d’équations | denklem sistemi
