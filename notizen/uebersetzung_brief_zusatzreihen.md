# Brief: Übersetzung ML-Arbeitsheft Teil 2 („Projektion, Eigenwerte und Zerlegungen“)

Ordner der Hefte: `C:\Bücher\EtUndSo\MachineLearning\Arbeitshefte\`
Deutsche Quelle (endgültig): `Kap2_Eigenwerte.tex` (Hauptdatei), `kap2_stufen.tex` (Abschnitte 1-6), `kap2_stufen_b.tex` (Abschnitte 7-12 + Abschluss), `kap2_loesungen.tex`.
Ziel je Sprache L: `Kap2_Eigenwerte_L.tex`, `kap2_stufen_L.tex`, `kap2_stufen_b_L.tex`, `kap2_loesungen_L.tex`.
Verbindliche Regeln: `C:\Users\info\PycharmProjects\pythonanimation\notizen\heft_uebersetzung.md` (lesen!).
Stilvorbild en/es/zh: `C:\Bücher\ET3\Arbeitshefte\kap2_stufen_en.tex`, `kap2_stufen_es.tex`, `kap2_stufen_zh.tex`, `kap2_loesungen_*.tex`, `Kap2_Laplace_*.tex`.

## Grundsätze
- Fachlich exakt, gut lesbar, seriös und professionell, aber nicht steif (wie das Original: kurze, klare Sätze). Qualität vor Tempo.
- Strukturgleich: jede Umgebung, jedes \label, jede Formel, jede Aufgabe/Lösung, jedes \item, jede Tabellenzeile, jede TikZ-Abbildung bleibt an ihrer Stelle. Nichts weglassen, nichts hinzufügen. Kommentarzeilen (`% ---`) dürfen übersetzt oder beibehalten werden.
- Formeln unverändert (Notation A = UDVᵀ mit d_j, r = y − Ax̂, κ = d₁/d_n, \vq, \mA, \T usw.). Übersetzt wird nur Text in Formeln (`\text{...}`, `\quad\text{für alle}` usw.).
- Dezimaltrennzeichen: en und zh Punkt (`0.6`), es, fr, tr Komma (`0{,}6`). Gilt auch in TikZ-Knotentexten (`{$2{,}6\,\vq_1$}` → en `{$2.6\,\vq_1$}`) und in `\foreach`-Beschriftungen wie `{0.5/0{,}5}` → en `{0.5/0.5}`. TikZ-Koordinaten (immer Punkt) NICHT anfassen.
- Listen mit Semikolon: Das Deutsche trennt Komponenten mit Dezimalzahlen durch `;` (`(0{,}6;\ 0{,}8)\T`, `\diag(1;\,-1)`, `(198{,}47;\ 132{,}60;\ \dots)`). en/zh: Komma statt Semikolon (`(0.6,\ 0.8)\T`, `\diag(1,\,-1)`). es/fr/tr: Semikolon wie im Deutschen.
- Abschnittsnummern wie „Teil~1, Abschnitt~13.5“ sind KEINE Dezimalzahlen: `13.5` bleibt mit Punkt in allen Sprachen.
- Tausendertrennung `18\,200`, `60\,100`, `100\,050`: in allen Sprachen unverändert `\,` lassen. Prozent `20\,\%` bleibt.
- Zahlwörter: Tausend = thousand / mil / 千 / mille / bin.
- Die Operatoren `\spur` und `\rang` der Präambel geben im PDF und auf der Website die deutschen Wörter „spur“/„rang“ aus. In den Übersetzungen deshalb ersetzen:
  - `\spur` → en, es, zh, fr: `\operatorname{tr}`; tr: `\operatorname{iz}`.
  - `\rang` → en, zh: `\operatorname{rank}`; es: `\operatorname{rango}`; fr: `\operatorname{rg}`; tr: `\operatorname{rank}`.
  - Im Text heißt die Spur trace / traza / 迹 / trace / iz.
  - `\diag`, `\sign`, `\argmin` bleiben.
- `\fb{...}` (Fachbegriff bei erster Nennung) übernehmen, um das übersetzte Wort.
- zh: `\emph{...}` und `\textit{...}` im Fließtext → `\textbf{...}` (SimSun hat keine Kursive).
- Anführungszeichen: en ``...'' (wie ET3 en), es «...» oder wie ET3 es, zh “...”, fr « ... » direkt getippt (mit Leerzeichen innen), tr “...”.
- fr-Typografie: vor `:` `;` `!` `?` ein normales Leerzeichen tippen (babel-french macht daraus das richtige), Apostroph typografisch ’. Anrede „vous“.
- tr-Typografie: `:` und `!` ohne Leerzeichen davor; İ/ı genau; Endungen nach Zahlen/Verweisen mit Apostroph (`Kısım~1'de`, `Alıştırma~\ref{a:k2onb}'deki`). Anrede „siz“.
- es: Anrede „tú“ wie in ET3 es. zh: wie ET3 zh (你).
- `\section*{...}` am Anfang: danach `\markboth{...}{...}` (in Großbuchstaben, wie im Deutschen) und `\addcontentsline` übersetzen. Deutsche `\pagebreak`/`\newpage` NICHT übernehmen (der Hauptagent setzt nötige Umbrüche nach dem Bauen).
- Code/Dateinamen (`rechnung\_kap2.py`) unverändert.

## Feste Wendungen (der Website-Umwandler erkennt Kästen nur daran)
| Deutsch | en | es | zh | fr | tr |
|---|---|---|---|---|---|
| \section*{Worum es geht} | What this is about | De qué se trata (oder wie ET3 es) | 本册内容 (oder wie ET3 zh) | De quoi il s’agit | Konunun özü |
| \paragraph{So arbeitest du mit dem Heft.} | How to work with this workbook. | Cómo trabajar con el cuaderno. | 如何使用本册。 | Comment travailler avec ce cahier. | Bu çalışma kitabıyla nasıl çalışılır? |
| \paragraph{Ein Prinzip hinter allen Ergebnissen.} | One principle behind all the results. | Un principio detrás de todos los resultados. | 一个原理贯穿所有结果。 | Un principe derrière tous les résultats. | Tüm sonuçların ardındaki tek ilke. |
| kernbox „Das Wichtigste bis hier“ | Key points so far | Lo esencial hasta aquí | 本册要点 | L’essentiel jusqu’ici | Buraya kadarki temel noktalar |
| kernbox „Die Antwort in drei Sätzen“ | The answer in three sentences | La respuesta en tres frases | 三句话的答案 | La réponse en trois phrases | Üç cümlede cevap |
| \section{Lösungen} | Solutions | Soluciones | 解答 | Solutions | Çözümler |
| Arbeitsheft/Heft im Fließtext | workbook | cuaderno | 本册 | cahier | çalışma kitabı (+Endungen: kitabında, kitabının, kitabına, kitabını, kitabından, kitabıyla; keine Possessivformen) |
| Teil~1 | Part~1 | Parte~1 | 第~1~部分 | Partie~1 | Kısım~1 |
| Abschnitt~X / Unterabschnitt | Section / subsection | sección / subsección (Sección am Satzanfang) | 第~X~节 / 小节 | section / sous-section | Kesim / alt kesim |
| Abb.~\ref | Fig.~\ref | Fig.~\ref (wie ET3 es) | 图~\ref | Fig.~\ref | Şekil~\ref |
| Aufgabe~\ref | Exercise~\ref | Ejercicio~\ref / ejercicio | 练习~\ref | exercice~\ref (Exercice am Satzanfang) | Alıştırma~\ref |
| Rechenbeispiel: / Rechenbeispiel 1: | Worked example: / Worked example 1: | Ejemplo numérico: | 算例： / 算例 1： | Exemple de calcul : | Sayısal örnek: |
| Kurz gesagt: | In short: | wie ET3 es | wie ET3 zh | En bref : | Kısacası: |
| Kästen im Einleitungstext: „Hintergrund“, „Beweis“, „Herleitung“ | Background, Proof, Derivation | Contexto, Demostración, Deducción | 背景, 证明, 推导 | Contexte, Preuve, Démonstration | Arka plan, İspat, Türetme |
| Unterabschnitt „Was du dafür brauchst: …“ | What you need for this: … | Lo que necesitas: … | 所需知识：… | Ce dont vous avez besoin : … | Bunun için gerekenler: … |
(Die Kastenwörter „Definition“, „Satz“, „Aufgabe“, „Beweis:“, „Herleitung:“, „Hintergrund:“, „Achtung:“, „Worum es geht:“ setzt die Präambel selbst; die Titel in den geschweiften Klammern werden übersetzt.)

Titel des Hefts (aus tools/heft_zu_artikel.py, verbindlich): en „Projection, Eigenvalues and Decompositions“, es „Proyección, valores propios y descomposiciones“, zh „投影、特征值与矩阵分解“, fr „Projection, valeurs propres et décompositions“, tr „İzdüşüm, Özdeğerler ve Ayrışımlar“.
Titelblock-Zeile: en `Workbook Machine Learning, Part~2. Version: 4~November 2026`; es `Cuaderno de trabajo Aprendizaje automático, parte~2. Versión: 4~de noviembre de 2026`; zh `机器学习练习册，第~2~部分。版本：2026~年~11~月~4~日`; fr `Cahier d’exercices Apprentissage automatique, partie~2. Version : 4~novembre 2026`; tr `Makine Öğrenmesi Çalışma Kitabı, Kısım~2. Sürüm: 4~Kasım 2026`.

## Wörter in den Abbildungen (Szenen, ml_teil2.py; in den TikZ-Bildern genauso verwenden)
Spaltenraum = column space / espacio columna / 列空间 / espace des colonnes / sütun uzayı; Schüssel, Rinne, Sattel = bowl, trough, saddle / cuenco, canal, silla / 碗形, 槽形, 鞍形 / cuvette, gouttière, selle / çanak, oluk, eyer; drehen/strecken = rotate/stretch / girar/estirar / 旋转/拉伸 / tourner/étirer / döndürme/germe; „C₁ (Rang 1)“ = rank / rango / 秩 / rang / rank; „Geraden senkrecht“ = lines perpendicular / rectas perpendiculares / 两直线垂直 / droites perpendiculaires / dik doğrular; „Geraden unter 8°“ = lines at 8° / rectas a 8° / 两直线夹角 8° / droites à 8° / 8° açılı doğrular; „Schnittpunkt wandert um 0,2“ = intersection moves by 0.2 / el punto de corte se mueve 0,2 / 交点移动 0.2 / l’intersection se déplace de 0,2 / kesişim noktası 0,2 kayar.

## Glossar (verbindlich, damit alle Dateien gleich heißen)
Format: Deutsch = en | es | zh | fr | tr
- Orthonormal, orthonormale Vektoren = orthonormal | ortonormales | 标准正交 | orthonormés | ortonormal
- Orthonormalbasis = orthonormal basis | base ortonormal | 标准正交基 | base orthonormée | ortonormal taban
- Standardbasis = standard basis | base canónica | 标准基 | base canonique | standart taban
- orthogonale Matrix = orthogonal matrix | matriz ortogonal | 正交矩阵 | matrice orthogonale | ortogonal matris
- Drehung, Spiegelung, Scherung = rotation, reflection, shear | rotación (giro), reflexión, cizalladura | 旋转, 反射, 剪切 | rotation, réflexion (symétrie), cisaillement | dönme, yansıma, kayma
- Skalarprodukt = dot product | producto escalar | 点积 | produit scalaire | iç çarpım
- Länge (Norm), Längenquadrat = length, squared length | longitud, cuadrado de la longitud | 长度, 长度的平方 | longueur, carré de la longueur | uzunluk, uzunluğun karesi
- Schatten (Bild aus Teil 1) = shadow | sombra | 影子 | ombre | gölge
- Fußpunkt des Lots = foot of the perpendicular | pie de la perpendicular | 垂足 | pied de la perpendiculaire | dikme ayağı
- (orthogonale) Projektion = (orthogonal) projection | proyección (ortogonal) | （正交）投影 | projection (orthogonale) | (dik) izdüşüm
- Projektionsmatrix = projection matrix | matriz de proyección | 投影矩阵 | matrice de projection | izdüşüm matrisi
- äußeres Produkt = outer product | producto exterior | 外积 | produit extérieur (produit tensoriel uᵥᵀ: „produit extérieur“) | dış çarpım
- Residuum = residual | residuo | 残差 | résidu | artık
- beste Näherungslösung = best approximate solution | mejor solución aproximada | 最佳近似解 | meilleure solution approchée | en iyi yaklaşık çözüm
- Methode der kleinsten Quadrate = method of least squares | método de mínimos cuadrados | 最小二乘法 | méthode des moindres carrés | en küçük kareler yöntemi
- Normalgleichungen = normal equations | ecuaciones normales | 正规方程 | équations normales | normal denklemler
- Ausgleichsgerade = least-squares line | recta de ajuste | 最小二乘直线 | droite des moindres carrés | en küçük kareler doğrusu
- Einsenspalte, Einsvektor = column of ones, all-ones vector | columna de unos, vector de unos | 全 1 列, 全 1 向量 | colonne de uns, vecteur de uns | birler sütunu, birler vektörü
- Spaltenraum = column space | espacio columna | 列空间 | espace des colonnes | sütun uzayı
- Kern = null space | núcleo | 零空间 | noyau | çekirdek
- Rang, Rangsatz = rank, rank–nullity theorem | rango, teorema del rango | 秩, 秩-零化度定理 | rang, théorème du rang | rank, rank-sıfırlık teoremi
- Spann = span | espacio generado | 张成的空间 (span) | sous-espace engendré | gerilen alt uzay (span)
- linear (un)abhängig = linearly (in)dependent | linealmente (in)dependientes | 线性无关/相关 | linéairement (in)dépendants | doğrusal (bağımsız/bağımlı)
- Gram-Matrix = Gram matrix | matriz de Gram | 格拉姆矩阵 | matrice de Gram | Gram matrisi
- Unterraum = subspace | subespacio | 子空间 | sous-espace | alt uzay
- orthogonales Komplement = orthogonal complement | complemento ortogonal | 正交补 | supplémentaire orthogonal | ortogonal tümleyen
- Normalenvektor = normal vector | vector normal | 法向量 | vecteur normal | normal vektör
- Gram-Schmidt-Verfahren (modifiziertes) = Gram–Schmidt process (modified) | proceso de Gram-Schmidt (modificado) | 格拉姆-施密特正交化（修正） | procédé de Gram-Schmidt (modifié) | Gram-Schmidt yöntemi (değiştirilmiş)
- QR-Zerlegung = QR decomposition | descomposición QR | QR 分解 | décomposition QR | QR ayrışımı
- obere/untere Dreiecksmatrix = upper/lower triangular matrix | matriz triangular superior/inferior | 上/下三角矩阵 | matrice triangulaire supérieure/inférieure | üst/alt üçgen matris
- Rückwärtseinsetzen = back substitution | sustitución regresiva | 回代 | remontée | geriye doğru yerine koyma
- Gauß-Verfahren = Gaussian elimination | eliminación gaussiana | 高斯消元法 | méthode du pivot de Gauss | Gauss eleme yöntemi
- Pivot(s), Stufenform = pivot(s), echelon form | pivote(s), forma escalonada | 主元, 阶梯形 | pivot(s), forme échelonnée | pivot(lar), basamak biçimi
- quadratische Form = quadratic form | forma cuadrática | 二次型 | forme quadratique | kuadratik form
- gemischtes Glied = cross term | término cruzado | 交叉项 | terme croisé (terme rectangle) | karma terim
- Schüssel, Rinne, Sattel, Kuppel, Kamm = bowl, trough, saddle, dome, ridge | cuenco, canal, silla, cúpula, cresta | 碗形, 槽形, 鞍形, 穹顶形, 脊形 | cuvette, gouttière, selle, dôme, crête | çanak, oluk, eyer, kubbe, sırt
- Talboden = valley floor | fondo del valle | 谷底 | fond de vallée | vadi tabanı
- Höhenlinien = contour lines | curvas de nivel | 等高线 | lignes de niveau | eş yükselti eğrileri
- quadratisch ergänzen = complete the square / completing the square | completar cuadrados | 配方 | compléter le carré | tam kareye tamamlamak
- Eigenwert, Eigenvektor, Eigenraum, Eigenrichtung, Eigenbasis = eigenvalue, eigenvector, eigenspace, eigendirection, eigenbasis | valor propio, vector propio, espacio propio, dirección propia, base propia | 特征值, 特征向量, 特征空间, 特征方向, 特征基 | valeur propre, vecteur propre, sous-espace propre, direction propre, base propre | özdeğer, özvektör, özuzay, öz doğrultu, öz taban
- Eigenfunktion = eigenfunction | función propia | 特征函数 | fonction propre | özfonksiyon
- charakteristisches Polynom = characteristic polynomial | polinomio característico | 特征多项式 | polynôme caractéristique | karakteristik polinom
- Spur = trace | traza | 迹 | trace | iz
- algebraische / geometrische Vielfachheit = algebraic / geometric multiplicity | multiplicidad algebraica / geométrica | 代数重数 / 几何重数 | multiplicité algébrique / géométrique | cebirsel / geometrik katlılık
- konjugiert komplex, Betrag, Realteil, Imaginärteil = complex conjugate, magnitude (absolute value), real part, imaginary part | conjugado complejo, módulo, parte real, parte imaginaria | 共轭复数, 模, 实部, 虚部 | conjugué, module, partie réelle, partie imaginaire | karmaşık eşlenik, mutlak değer (modül), gerçel kısım, sanal kısım
- Eulersche Formel = Euler’s formula | fórmula de Euler | 欧拉公式 | formule d’Euler | Euler formülü
- Basiswechsel, ähnlich = change of basis, similar | cambio de base, semejantes | 基变换, 相似 | changement de base, semblables | taban değişimi, benzer
- diagonalisierbar, Diagonalisierung = diagonalizable, diagonalization | diagonalizable, diagonalización | 可对角化, 对角化 | diagonalisable, diagonalisation | köşegenleştirilebilir, köşegenleştirme
- entkoppeln = decouple | desacoplar | 解耦 | découpler | ayrıştırmak (birbirinden bağımsız hale getirmek)
- Spektrum, Spektralsatz, Spektralzerlegung = spectrum, spectral theorem, spectral decomposition | espectro, teorema espectral, descomposición espectral | 谱, 谱定理, 谱分解 | spectre, théorème spectral, décomposition spectrale | spektrum, spektral teorem, spektral ayrışım
- Hauptachsen, Halbachsen = principal axes, semi-axes | ejes principales, semiejes | 主轴, 半轴 | axes principaux, demi-axes | asal eksenler, yarı eksenler
- Trägheitssatz von Sylvester = Sylvester’s law of inertia | ley de inercia de Sylvester | 西尔维斯特惯性定律 | loi d’inertie de Sylvester | Sylvester eylemsizlik yasası
- positiv definit / positiv semidefinit / negativ definit / indefinit = positive definite / positive semidefinite / negative definite / indefinite | definida positiva / semidefinida positiva / definida negativa / indefinida | 正定 / 半正定 / 负定 / 不定 | définie positive / semi-définie positive / définie négative / indéfinie | pozitif tanımlı / pozitif yarı tanımlı / negatif tanımlı / belirsiz
- Definitheit = definiteness | definición (carácter definido) | 定性 | caractère défini (signature) | tanımlılık
- Eigenwerttest = eigenvalue test | criterio de los valores propios | 特征值判别法 | critère des valeurs propres | özdeğer testi
- führende Hauptminoren, Kriterium von Sylvester = leading principal minors, Sylvester’s criterion | menores principales dominantes, criterio de Sylvester | 顺序主子式, 西尔维斯特判据 | mineurs principaux dominants, critère de Sylvester | baş asal minörler, Sylvester ölçütü
- Rayleigh-Quotient = Rayleigh quotient | cociente de Rayleigh | 瑞利商 | quotient de Rayleigh | Rayleigh bölümü
- Cholesky-Zerlegung, Cholesky-Faktor = Cholesky decomposition, Cholesky factor | descomposición de Cholesky, factor de Cholesky | Cholesky 分解, Cholesky 因子 | décomposition de Cholesky, facteur de Cholesky | Cholesky ayrışımı, Cholesky çarpanı
- Singulärwertzerlegung (SVD) = singular value decomposition (SVD) | descomposición en valores singulares (SVD) | 奇异值分解（SVD） | décomposition en valeurs singulières (SVD) | tekil değer ayrışımı (SVD)
- Singulärwert, rechter/linker Singulärvektor = singular value, right/left singular vector | valor singular, vector singular derecho/izquierdo | 奇异值, 右/左奇异向量 | valeur singulière, vecteur singulier à droite/à gauche | tekil değer, sağ/sol tekil vektör
- Baustein (vom Rang 1) = building block (of rank 1) | bloque (de rango 1) | （秩 1 的）构件 | brique (de rang 1) | (rank 1) yapı taşı
- Spektralnorm, Frobeniusnorm = spectral norm, Frobenius norm | norma espectral, norma de Frobenius | 谱范数, Frobenius 范数 | norme spectrale, norme de Frobenius | spektral norm, Frobenius normu
- abgeschnittene Singulärwertzerlegung = truncated singular value decomposition | descomposición en valores singulares truncada | 截断奇异值分解 | décomposition en valeurs singulières tronquée | kesilmiş tekil değer ayrışımı
- Satz von Eckart und Young = Eckart–Young theorem | teorema de Eckart-Young | Eckart–Young 定理 | théorème d’Eckart-Young | Eckart-Young teoremi
- Graustufenbild, Bildpunkt = grayscale image, pixel | imagen en escala de grises, píxel | 灰度图像, 像素 | image en niveaux de gris, pixel | gri tonlamalı görüntü, piksel
- Linksinverse, Rechtsinverse, Pseudoinverse = left inverse, right inverse, pseudoinverse | inversa por la izquierda, inversa por la derecha, pseudoinversa | 左逆, 右逆, 伪逆 | inverse à gauche, inverse à droite, pseudo-inverse | sol ters, sağ ters, sözde ters
- hohe/breite Matrix = tall/wide matrix | matriz alta/ancha | 高矩阵/宽矩阵 | matrice haute/large | uzun/geniş matris
- kürzeste Lösung = shortest solution (minimum-norm solution) | solución más corta | 最短解 | solution la plus courte | en kısa çözüm
- Konditionszahl, schlecht/gut konditioniert = condition number, ill-/well-conditioned | número de condición, mal/bien condicionada | 条件数, 病态/良态 | conditionnement (nombre de conditionnement), mal/bien conditionnée | koşul sayısı, kötü/iyi koşullu
- rückwärtsstabil = backward stable | estable hacia atrás | 后向稳定 | stable au sens rétrograde (backward stable) | geriye doğru kararlı
- singulär (Matrix) = singular | singular | 奇异 | singulière | tekil
- invertierbar, Inverse = invertible, inverse | invertible, inversa | 可逆, 逆矩阵 | inversible, inverse | tersinir, ters
- Einheitsmatrix, Diagonalmatrix, Nullmatrix = identity matrix, diagonal matrix, zero matrix | matriz identidad, matriz diagonal, matriz nula | 单位矩阵, 对角矩阵, 零矩阵 | matrice identité, matrice diagonale, matrice nulle | birim matris, köşegen matris, sıfır matris
- Einheitskreis, Einheitskugel = unit circle, unit sphere | circunferencia unidad, esfera unidad | 单位圆, 单位球 | cercle unité, sphère unité | birim çember, birim küre
- Wohnung, Fläche, Zimmerzahl, Preis, Tausend Euro = apartment, floor area, number of rooms, price, thousand euros | vivienda, superficie, número de habitaciones, precio, miles de euros | 公寓, 面积, 房间数, 价格, 千欧元 | appartement, surface, nombre de pièces, prix, milliers d’euros | daire, alan, oda sayısı, fiyat, bin avro
- Grundpreis = base price | precio base | 基础价格 | prix de base | taban fiyat
- Messpunkt, Messwert = data point, measured value | punto de medida, valor medido | 测量点, 测量值 | point de mesure, valeur mesurée | ölçüm noktası, ölçüm değeri
- Schwerpunkt (der Punkte) = centroid | centroide | 质心 | barycentre | ağırlık merkezi
- Achsenabschnitt, Steigung = intercept, slope | ordenada en el origen, pendiente | 截距, 斜率 | ordonnée à l’origine, pente | eksen kesişimi (sabit terim), eğim
- Kanalmatrix, Sende-/Empfangsantenne, Rauschen = channel matrix, transmit/receive antenna, noise | matriz de canal, antena transmisora/receptora, ruido | 信道矩阵, 发射/接收天线, 噪声 | matrice de canal, antenne d’émission/de réception, bruit | kanal matrisi, verici/alıcı anten, gürültü
- Impulsantwort, Übertragungsfunktion, Faltung, Autokorrelation, Kreuzkorrelation = impulse response, transfer function, convolution, autocorrelation, cross-correlation | respuesta al impulso, función de transferencia, convolución, autocorrelación, correlación cruzada | 冲激响应, 传递函数, 卷积, 自相关, 互相关 | réponse impulsionnelle, fonction de transfert, convolution, autocorrélation, intercorrélation | dürtü yanıtı, aktarım fonksiyonu, evrişim, özilinti, çapraz ilinti
- Induktivität, Gegeninduktivität, Kopplungsfaktor, Spule = inductance, mutual inductance, coupling coefficient, coil | inductancia, inductancia mutua, coeficiente de acoplamiento, bobina | 电感, 互感, 耦合系数, 线圈 | inductance, inductance mutuelle, coefficient de couplage, bobine | endüktans, karşılıklı endüktans, kuplaj katsayısı, bobin
- Fibonacci-Zahlen, goldener Schnitt = Fibonacci numbers, golden ratio | números de Fibonacci, razón áurea | 斐波那契数, 黄金比 | nombres de Fibonacci, nombre d’or | Fibonacci sayıları, altın oran

## Arbeitsweise für einen Übersetzungs-Agenten
1. Lies `notizen\heft_uebersetzung.md`, diesen Brief, deine Quelldatei GANZ (große Dateien in Teilen bis zum Ende) und die passende Präambel `praeambel_L.tex` (nur die Kastenwörter). en/es/zh: lies zusätzlich ein Stück des ET3-Vorbilds der Sprache (z. B. die ersten 250 Zeilen von `C:\Bücher\ET3\Arbeitshefte\kap2_stufen_L.tex`) für Ton und Wendungen.
2. Schreibe die Übersetzung mit dem Write-Tool (nie per Bash-Heredoc: Backslash-Falle). Große Dateien in Stücken von höchstens etwa 35 KB in den Ordner `C:\Users\info\AppData\Local\Temp\claude\C--B-cher\c5e68cc8-baf1-4782-9760-867850fb6615\scratchpad\mlk2_uebersetzung\teile\` schreiben (z. B. `stufen_en_1.tex`, `_2`, `_3`, Grenzen an Abschnittsgrenzen) und dann mit Bash zusammenfügen: `cat teil1 teil2 teil3 > Zieldatei` (cat ändert keine Backslashes).
3. Prüfe danach mit `python "C:\Users\info\AppData\Local\Temp\claude\C--B-cher\c5e68cc8-baf1-4782-9760-867850fb6615\scratchpad\mlk2_uebersetzung\struktur_check.py" <deutsche Datei> <übersetzte Datei> <L>` und behebe jede echte Abweichung mit dem Edit-Tool (fehlende Formel, Label, Umgebung, falsches Dezimalzeichen). Lies anschließend die eigene Datei einmal ganz gegen (Tippfehler, Grammatik, fehlende Sätze).
4. Nichts bauen, keine anderen Dateien ändern (insbesondere nicht die deutschen Dateien, Präambeln, kap1_*, Szenen, Werkzeuge). Kein git.
5. Fehler im deutschen Original (falsche Zahl, falscher Verweis, falsche Aussage): in der Übersetzung richtig schreiben und im Bericht genau nennen (Datei, Zeile, alt, neu, Begründung). Nur bei echten, nachgerechneten Fehlern.
6. Bericht (knapp): geschriebene Datei(en) mit Größe, Ergebnis von struktur_check, gefundene Fehler im Original, Zweifelsfälle bei Begriffen, Stellen, die ein Muttersprachler gegenlesen sollte.

## Korrekturen am Original (bereits in der deutschen Datei eingetragen)
- kap2_stufen.tex Z. 1085: „Ein negativer und ein verschwindender Eintrag geben eine umgedrehte Rinne, einen Kamm.“ (vorher fälschlich „einen umgedrehten Kamm“).
- kap2_stufen_b.tex Z. 85: $\mathbf M\mathbf s_1=(2{,}4+0{,}6;\ 0{,}6+1{,}4)\T$ (vorher 1{,}6+1{,}4).
- kap2_stufen_b.tex Z. 1181: $\lambda_1\approx2{,}005012$ (vorher 2{,}005013).
- kap2_stufen_b.tex Z. 1012: „Die Richtungen $\vu_j$ mit $j>r$, die $\mA$ nicht erreicht, bildet $\mA^+$ auf null ab, statt durch null zu teilen.“ (vorher falsch: „Richtungen, die $\mA$ auf null abbildet, bildet auch $\mA^+$ auf null ab …“).
- kap2_stufen_b.tex Z. 824 (Bildunterschrift fig:k2rfehler): „…: Sein Quadrat ist $d_2^2=1$.“ (vorher ungenau „Er ist $d_2^2=1$“).
- kap2_stufen_b.tex Z. 201: „… $\vx\T\mA\vx=\lambda_it^2=1$ genau bei $t=\pm1/\sqrt{\lambda_i}$.“ (vorher ohne ±).
- kap2_stufen.tex Z. 1262: „Nach dem Unterabschnitt über komplexe Zahlen hat es …“ (vorher falsch „Nach dem vorigen Unterabschnitt“).
Die deutschen Dateien enthalten diese Korrekturen bereits; einfach die aktuelle deutsche Fassung übersetzen.

## Wortwahl der englischen Fassung (zur Orientierung für andere Sprachen)
Betragssummennorm = 1-norm; Gleichmuster/Wechselmuster = constant/alternating pattern; Gleichanteil = DC component; Takt = sample/time step; Achsenkreuz = set of axes; Mulde = hollow; Zeiger = phasor; zyklische Faltung = cyclic convolution; Rechenprogramme = numerical software; Aufgabentitel „Große Determinante, schlechte Kondition“ wörtlich übersetzen.
