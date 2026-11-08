# Brief: Übersetzung ML-Arbeitsheft Grundlagen 2 („Projektion, Eigenwerte und Zerlegungen“)

**Seit 06.11.2026:** Die ML-Hefte T01–T06 heißen „Grundlagen 1–6“ (Nachschlagebereich), der ML-Pfad zählt ab T08 als „Teil 1“. Für jedes weitere Heft gelten die Verweis- und Titelwendungen in der Tabelle „Feste Wendungen“ unten und in `heft_uebersetzung.md`, Abschnitt „Verweise auf andere Hefte“. Dateinamen (Kap2_Eigenwerte …) bleiben.

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
- Abschnittsnummern wie „Grundlagen~1, Abschnitt~13.5“ sind KEINE Dezimalzahlen: `13.5` bleibt mit Punkt in allen Sprachen.
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
| Grundlagen~1 (ML-Grundlagen-Heft; früher „Teil~1“) | Foundations~1 | Fundamentos~1 (ohne Artikel: „de Fundamentos~1“) | 基础篇~1 | Fondements~1 (ohne Artikel: „dans Fondements~1“) | Temeller~1 (Endung: `Temeller~1'de`) |
| Grundlagen~1, Abschnitt~13.5 | Foundations~1, Section~13.5 | Fundamentos~1, sección~13.5 | 基础篇~1~第~13.5~节 | Fondements~1, section~13.5 | Temeller~1, Kesim~13.5 |
| Teil~1 (nur ML-Pfad ab T08, Teil N = T(N+7)) | Part~1 | Parte~1 | 第~1~部分 | Partie~1 | Kısım~1 |
| Programmieren, Python~2, Abschnitt~3 | Programming, Python~2, Section~3 | Programación, Python~2, sección~3 | 编程，Python~2~第~3~节 | Programmation, Python~2, section~3 | Programlama, Python~2, Kesim~3 |
| Linux~2, Abschnitt~3 | Linux~2, Section~3 | Linux~2, sección~3 | Linux~2~第~3~节 | Linux~2, section~3 | Linux~2, Kesim~3 |
| Abschnitt~X / Unterabschnitt | Section / subsection | sección / subsección (Sección am Satzanfang) | 第~X~节 / 小节 | section / sous-section | Kesim / alt kesim |
| Abb.~\ref | Fig.~\ref | Fig.~\ref (wie ET3 es) | 图~\ref | Fig.~\ref | Şekil~\ref |
| Aufgabe~\ref | Exercise~\ref | Ejercicio~\ref / ejercicio | 练习~\ref | exercice~\ref (Exercice am Satzanfang) | Alıştırma~\ref |
| Rechenbeispiel: / Rechenbeispiel 1: | Worked example: / Worked example 1: | Ejemplo numérico: | 算例： / 算例 1： | Exemple de calcul : | Sayısal örnek: |
| Kurz gesagt: | In short: | wie ET3 es | wie ET3 zh | En bref : | Kısacası: |
| Kästen im Einleitungstext: „Hintergrund“, „Beweis“, „Herleitung“ | Background, Proof, Derivation | Contexto, Demostración, Deducción | 背景, 证明, 推导 | Contexte, Preuve, Démonstration | Arka plan, İspat, Türetme |
| Unterabschnitt „Was du dafür brauchst: …“ | What you need for this: … | Lo que necesitas: … | 所需知识：… | Ce dont vous avez besoin : … | Bunun için gerekenler: … |
(Die Kastenwörter „Definition“, „Satz“, „Aufgabe“, „Beweis:“, „Herleitung:“, „Hintergrund:“, „Achtung:“, „Worum es geht:“ setzt die Präambel selbst; die Titel in den geschweiften Klammern werden übersetzt.)

Titel des Hefts (aus tools/heft_zu_artikel.py, verbindlich): en „Projection, Eigenvalues and Decompositions“, es „Proyección, valores propios y descomposiciones“, zh „投影、特征值与矩阵分解“, fr „Projection, valeurs propres et décompositions“, tr „İzdüşüm, Özdeğerler ve Ayrışımlar“.
Titelblock-Zeile (seit 06.11.2026, Grundlagen-Hefte): de `Mathematische Grundlagen für Machine Learning, Grundlagen~2. Stand: …`; en `Mathematical Foundations for Machine Learning, Foundations~2. Version: 4~November 2026`; es `Fundamentos matemáticos para el aprendizaje automático, Fundamentos~2. Versión: 4~de noviembre de 2026`; zh `机器学习数学基础，基础篇~2。版本：2026~年~11~月~4~日`; fr `Fondements mathématiques pour l’apprentissage automatique, Fondements~2. Version : 4~novembre 2026`; tr `Makine Öğrenmesi için Matematiksel Temeller, Temeller~2. Sürüm: 4~Kasım 2026`. ML-Pfad-Hefte behalten die alte Form mit Teil/Part/parte/部分/partie/Kısım (`Workbook Machine Learning, Part~1` usw.).
Bereichsnamen auf der Website: Mathematische Grundlagen = Mathematical Foundations | Fundamentos matemáticos | 数学基础 | Fondements mathématiques | Matematiksel Temeller.

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
- Schatten (Bild aus Grundlagen 1) = shadow | sombra | 影子 | ombre | gölge
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

### Ergänzt bei Grundlagen 1 (Vektoren und Matrizen, 06.11.2026)
Daten und Modelle
- Merkmal, Merkmalsvektor, Merkmalsspalte = feature, feature vector, feature column | característica, vector de características, columna de la característica | 特征, 特征向量（feature vector）, 特征列 | caractéristique, vecteur de caractéristiques, colonne de la caractéristique | öznitelik, öznitelik vektörü, öznitelik sütunu
- Beispiel (Datenbeispiel), Datensatz, Datenmatrix = example, dataset, data matrix | ejemplo, conjunto de datos, matriz de datos | 样本, 数据集, 数据矩阵 | exemple, jeu de données, matrice de données | örnek, veri kümesi, veri matrisi
- Wohnungsdatensatz, Fläche, Zimmer, Entfernung zum Zentrum, Stadtteil = apartment dataset, floor area, rooms, distance to the center, district | conjunto de datos de viviendas, superficie, habitaciones, distancia al centro, barrio | 公寓数据集, 面积, 房间, 到市中心的距离, 城区 | jeu de données des appartements, surface, pièces, distance au centre, quartier | daire veri kümesi, alan, oda, merkeze uzaklık, semt
- Gewicht, gewichtete Summe, Modell, Vorhersage = weight, weighted sum, model, prediction | peso, suma ponderada, modelo, predicción | 权重, 加权和, 模型, 预测值 | poids, somme pondérée, modèle, prédiction | ağırlık, ağırlıklı toplam, model, tahmin
- Maklerin, Gutachter A/B, Mietspiegel, Monatsmiete = real estate agent (she), appraiser A/B, rent index, monthly rent | la agente inmobiliaria, tasador A/B, índice de alquileres, alquiler mensual | 房产经纪人, 评估师 A/B, 租金参考表, 月租金 | l’agente immobilière, expert A/B, grille de référence des loyers, loyer mensuel | emlakçı, eksper A/B, kira endeksi, aylık kira
- Fehlervektor, tatsächlicher Wert, Ausreißer = error vector, actual value, outlier | vector de error, valor real, valor atípico | 误差向量, 实际值, 离群值 | vecteur d’erreur, valeur réelle, valeur aberrante | hata vektörü, gerçek değer, aykırı değer
Summen und Vektoren
- Summenzeichen, Index, Laufindex, Doppelsumme = summation sign, index, summation index, double sum | signo de sumatorio, índice, índice de sumación, suma doble | 求和符号, 下标, 求和指标, 双重求和 | symbole somme, indice, indice de sommation, somme double | toplam sembolü, indis, toplam indisi, çift toplam
- Komponente, Skalar, transponiert, Nullvektor, Vielfaches = component, scalar, transposed, zero vector, multiple | componente, escalar, traspuesto, vector nulo, múltiplo | 分量, 标量, 转置, 零向量, 倍数 | composante, scalaire, transposé, vecteur nul, multiple | bileşen, skaler, devrik, sıfır vektörü, kat
- Linearkombination, Koeffizient, Mittelwert der Beispiele, Einheitsvektor = linear combination, coefficient, mean of the examples, unit vector | combinación lineal, coeficiente, media de los ejemplos, vector unitario | 线性组合, 系数, 样本均值, 单位向量 | combinaison linéaire, coefficient, moyenne des exemples, vecteur unitaire | doğrusal bileşim, katsayı, örneklerin ortalaması, birim vektör
- Mittelwert, Muster, Mustervergleich = mean, pattern, comparison with a pattern | media, patrón, comparación con un patrón | 均值, 模式, 模式比对 | moyenne, motif, comparaison avec un motif | ortalama, örüntü, örüntü karşılaştırması
- Abtastwert, Takt, Verschiebung, Energie, Korrelator = sample, (time) step, shift, energy, correlator | muestra, paso, desplazamiento, energía, correlador | 采样值, 采样点（步）, 移位, 能量, 相关器 | échantillon, pas, décalage, énergie, corrélateur | örnek değer, adım, kaydırma, enerji, korelatör
- Korrelationsempfänger, signalangepasstes Filter, Verhältnis von Signal zu Rauschen = correlation receiver, matched filter, signal-to-noise ratio | receptor de correlación, filtro adaptado (matched filter), relación señal-ruido | 相关接收机, 匹配滤波器（matched filter）, 信噪比 | récepteur à corrélation, filtre adapté (matched filter), rapport signal sur bruit | korelasyon alıcısı, uyumlu süzgeç (matched filter), sinyal-gürültü oranı
Normen und Abstände
- euklidische Norm, normiert, normieren = Euclidean norm, normalized, normalize | norma euclídea, normalizado, normalizar | 欧几里得范数, 归一化的, 归一化 | norme euclidienne, normé, normer | Öklid normu, normlanmış, normlamak
- Betragssummennorm, Maximumnorm, p-Norm, Manhattan-Norm = 1-norm, maximum norm, p-norm, Manhattan norm | norma 1, norma del máximo, norma p, norma Manhattan | 1-范数, 最大范数, p-范数, 曼哈顿范数 | norme 1, norme du maximum, norme p, norme de Manhattan | mutlak değerler toplamı normu (1-normu), maksimum normu, p-normu, Manhattan normu
- Dreiecksungleichung, Raute, Parallelogrammgleichung = triangle inequality, diamond (rhombus), parallelogram law | desigualdad triangular, rombo, ley del paralelogramo | 三角不等式, 菱形, 平行四边形恒等式 | inégalité triangulaire, losange, identité du parallélogramme | üçgen eşitsizliği, eşkenar dörtgen, paralelkenar özdeşliği
- Effektivwert = RMS value (root mean square) | valor eficaz | 有效值（均方根值） | valeur efficace | etkin değer (RMS)
- Tschebyscheff-Ungleichung = Chebyshev’s inequality | desigualdad de Chebyshov | 切比雪夫不等式 | inégalité de Bienaymé-Tchebychev | Çebişev eşitsizliği
- Abstand, Einheit, Gewichtung = distance, unit, weighting | distancia, unidad, ponderación | 距离, 单位, 加权 | distance, unité, pondération | uzaklık, birim, ağırlıklandırma
- zentriert, zentrieren, Abweichung vom Mittelwert = centered, center, deviation from the mean | centrado, centrar, desviación respecto de la media | 中心化的, 中心化, 与均值的偏差 | centré, centrer, écart à la moyenne | merkezlenmiş, merkezlemek, ortalamadan sapma
- Gleichanteil, Wechselanteil, Mischstrom = DC component, AC component, current with DC and AC components | componente continua, componente alterna, corriente mixta | 直流分量, 交流分量, 交直流混合电流 | composante continue, composante alternative, courant mixte | sabit (DC) bileşen, değişken (AC) bileşen, karma akım
- Standardabweichung, standardisieren, standardisierte Werte, Spannweite = standard deviation, standardize, standardized values, range | desviación típica, estandarizar, valores estandarizados, recorrido | 标准差, 标准化, 标准化值, 极差 | écart type, standardiser (centrer-réduire), valeurs standardisées, étendue | standart sapma, standartlaştırmak, standartlaştırılmış değerler, değişim aralığı
Winkel
- Cauchy-Schwarz-Ungleichung, Kosinussatz, Geodreieck = Cauchy–Schwarz inequality, law of cosines, protractor | desigualdad de Cauchy-Schwarz, teorema del coseno, transportador | 柯西-施瓦茨不等式, 余弦定理, 量角器 | inégalité de Cauchy-Schwarz, loi des cosinus (théorème d’Al-Kashi), rapporteur | Cauchy-Schwarz eşitsizliği, kosinüs teoremi, iletki
- Winkel spitz/recht/stumpf, orthogonal, Satz des Pythagoras = acute/right/obtuse angle, orthogonal, Pythagorean theorem | ángulo agudo/recto/obtuso, ortogonal, teorema de Pitágoras | 锐角/直角/钝角, 正交, 勾股定理 | angle aigu/droit/obtus, orthogonal, théorème de Pythagore | dar/dik/geniş açı, ortogonal, Pisagor teoremi
- Kosinus-Ähnlichkeit, Korrelationskoeffizient = cosine similarity, correlation coefficient | similitud coseno, coeficiente de correlación | 余弦相似度, 相关系数 | similarité cosinus, coefficient de corrélation | kosinüs benzerliği, korelasyon katsayısı
- Wörter „Tor“, „Ball“, „Wahl“ = “goal”, “ball”, “election” | «gol», «balón», «elección» | “进球”、“球”、“选举” | « but », « ballon », « élection » | “gol”, “top”, “seçim”
- Schattenlänge, vorzeichenbehaftet, Schattenpunkt, Verbindungspfeil = shadow length, signed, shadow point, connecting arrow | longitud de la sombra, con signo, punto de la sombra, flecha de unión | 影长, 带符号的, 影子端点, 连接箭头 | longueur de l’ombre, algébrique, point d’ombre, flèche de liaison | gölge uzunluğu, işaretli, gölge noktası, bağlantı oku
- Fourier-Reihe, Fourier-Koeffizient = Fourier series, Fourier coefficient | serie de Fourier, coeficiente de Fourier | 傅里叶级数, 傅里叶系数 | série de Fourier, coefficient de Fourier | Fourier serisi, Fourier katsayısı
Matrizen
- Eintrag, Format (m×n), quadratisch, Diagonale = entry, size, square, diagonal | entrada, tamaño, cuadrada, diagonal | 元素, 型（m×n；同型矩阵）, 方阵, 对角线 | coefficient, taille, carrée, diagonale | eleman, tip (m×n tipinde; „boyut“ ist schon Dimension), kare, köşegen
- Matrix-Vektor-Produkt, Zeilensicht, Spaltensicht, Spaltenraum = matrix–vector product, row view, column view, column space | producto matriz-vector, visión por filas, visión por columnas, espacio columna | 矩阵-向量乘积, 行视角, 列视角, 列空间 | produit matrice-vecteur, vue par lignes, vue par colonnes, espace des colonnes | matris-vektör çarpımı, satır bakışı, sütun bakışı, sütun uzayı
- Grundrechenarten = basic arithmetic operations | operaciones aritméticas básicas | 基本算术运算 | opérations élémentaires | temel aritmetik işlemler
- (lineare) Abbildung, Bild = (linear) map, image | aplicación (lineal), imagen | （线性）映射, 像 | application (linéaire), image | (doğrusal) dönüşüm, görüntü
- Überlagerungsprinzip, LTI-System, zeitdiskretes Filter, Einheitsimpuls = superposition principle, LTI system, discrete-time filter, unit impulse | principio de superposición, sistema LTI, filtro de tiempo discreto, impulso unitario | 叠加原理, LTI 系统, 离散时间滤波器, 单位冲激 | principe de superposition, système LTI, filtre à temps discret, impulsion unité | süperpozisyon ilkesi, LTI sistem, ayrık zamanlı süzgeç, birim dürtü
- Streckung, Plattdrücken, Einheitsquadrat, Gitter, Drehmatrix = stretch, flattening, unit square, grid, rotation matrix | estiramiento, aplastamiento, cuadrado unidad, cuadrícula, matriz de rotación | 拉伸, 压扁, 单位正方形, 网格, 旋转矩阵 | étirement, aplatissement, carré unité, quadrillage, matrice de rotation | germe, yassılaştırma, birim kare, ızgara, dönme matrisi
- affine Abbildung, Grundbetrag, erweiterte Datenmatrix, Differenzierer = affine map, base amount, augmented data matrix, differencer | aplicación afín, importe base, matriz de datos ampliada, diferenciador | 仿射映射, 基础金额, 增广数据矩阵, 差分器 | application affine, montant de base, matrice de données augmentée, différentiateur | afin dönüşüm, taban tutar, genişletilmiş veri matrisi, fark alıcı
- Matrixprodukt, Hintereinanderausführung, lineare Stufe = matrix product, composition, linear stage | producto de matrices, composición, etapa lineal | 矩阵乘积, 复合, 线性级 | produit matriciel, composition, étage linéaire | matris çarpımı, bileşke, doğrusal aşama
- Transponierte, symmetrische Matrix, Gram-Matrix der Beispiele/Merkmale = transpose, symmetric matrix, Gram matrix of the examples/features | traspuesta, matriz simétrica, matriz de Gram de los ejemplos/las características | 转置, 对称矩阵, 样本/特征的格拉姆矩阵 | transposée, matrice symétrique, matrice de Gram des exemples/caractéristiques | devrik, simetrik matris, örneklerin/özniteliklerin Gram matrisi
Gleichungssysteme, Rang, Determinante
- lineares Gleichungssystem, Unbekannte, Koeffizientenmatrix, rechte Seite = system of linear equations, unknowns, coefficient matrix, right-hand side | sistema de ecuaciones lineales, incógnitas, matriz de coeficientes, lado derecho | 线性方程组, 未知数, 系数矩阵, 右端项 | système d’équations linéaires, inconnues, matrice des coefficients, second membre | doğrusal denklem sistemi, bilinmeyenler, katsayı matrisi, sağ taraf
- Zeilenbild, Spaltenbild = row picture, column picture | imagen por filas, imagen por columnas | 行图, 列图 | image en lignes, image en colonnes | satır resmi, sütun resmi
- erweiterte Koeffizientenmatrix, Zeilenumformung, Zeilenstufenform, Stufe = augmented matrix, row operation, row echelon form, pivot | matriz ampliada, operación de filas, forma escalonada, pivote | 增广矩阵, 初等行变换, 行阶梯形, 主元 | matrice augmentée, opération sur les lignes, forme échelonnée, pivot | genişletilmiş katsayı matrisi, satır işlemi, satır basamak biçimi, pivot
- homogen, überbestimmt, unterbestimmt = homogeneous, overdetermined, underdetermined | homogéneo, sobredeterminado, infradeterminado | 齐次, 超定, 欠定 | homogène, surdéterminé, sous-déterminé | homojen, aşırı belirlenmiş, eksik belirlenmiş
- Basis, Dimension, Koordinaten, voller Rang, Spaltenrang/Zeilenrang = basis, dimension, coordinates, full rank, column rank/row rank | base, dimensión, coordenadas, rango completo, rango por columnas/por filas | 基, 维数, 坐标, 满秩, 列秩/行秩 | base, dimension, coordonnées, rang maximal, rang des colonnes/des lignes | taban, boyut, koordinatlar, tam rank, sütun rankı/satır rankı
- Erdgeschoss, Obergeschoss, Gesamtfläche, Pfund = ground floor, upper floor, total floor area, pound | planta baja, planta superior, superficie total, libra | 一楼, 二楼, 总面积, 磅 | rez-de-chaussée, étage, surface totale, livre | zemin kat, üst kat, toplam alan, libre
- Determinante, Orientierung, Flächenfaktor, Volumenfaktor = determinant, orientation, area factor, volume factor | determinante, orientación, factor de área, factor de volumen | 行列式, 定向, 面积因子, 体积因子 | déterminant, orientation, facteur d’aire, facteur de volume | determinant, yönelim, alan çarpanı, hacim çarpanı
- Spat, Einheitswürfel, Quader, Laplace-Entwicklung, Rechte-Hand-Regel, Prinzip von Cavalieri = parallelepiped, unit cube, box (cuboid), Laplace expansion, right-hand rule, Cavalieri’s principle | paralelepípedo, cubo unidad, ortoedro, desarrollo de Laplace, regla de la mano derecha, principio de Cavalieri | 平行六面体, 单位立方体, 长方体, 拉普拉斯展开, 右手定则, 祖暅原理（卡瓦列里原理） | parallélépipède, cube unité, pavé droit, développement de Laplace, règle de la main droite, principe de Cavalieri | paralelyüz, birim küp, dikdörtgenler prizması, Laplace açılımı, sağ el kuralı, Cavalieri ilkesi
Elementweise und Tensoren
- Hadamard-Produkt, elementweise = Hadamard product, elementwise | producto de Hadamard, elemento a elemento | 哈达玛积, 逐元素 | produit de Hadamard, terme à terme | Hadamard çarpımı, eleman eleman
- Tensor, Achse, Form, Farbbild, Farbkanal, Bildstapel = tensor, axis, shape, color image, color channel, image stack | tensor, eje, forma, imagen en color, canal de color, pila de imágenes | 张量, 轴, 形状, 彩色图像, 颜色通道, 图像堆叠 | tenseur, axe, forme, image couleur, canal de couleur, pile d’images | tensör, eksen, şekil, renkli görüntü, renk kanalı, görüntü yığını
- Spannungstensor (Werkstoff), Permittivitätstensor = stress tensor, permittivity tensor | tensor de tensiones, tensor de permitividad | 应力张量, 介电常数张量 | tenseur des contraintes, tenseur de permittivité | gerilme tensörü, dielektrik geçirgenlik tensörü

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

## Grundlagen 1 („Vektoren und Matrizen“), Übersetzung seit 06.11.2026
Die Abschnitte oben zu Grundlagen 2 (Titel, Korrekturen, Szenenwörter aus ml_teil2.py) gelten hier nicht; Grundsätze, feste Wendungen und Glossar (samt Block „Ergänzt bei Grundlagen 1“) gelten.

Deutsche Quelle (endgültig): `Kap1_Vektoren.tex`, `kap1_stufen.tex` (Abschnitte 1–7), `kap1_stufen_b.tex` (Abschnitte 8–15 und Abschluss), `kap1_loesungen.tex`. Ziel je Sprache L: `Kap1_Vektoren_L.tex`, `kap1_stufen_L.tex`, `kap1_stufen_b_L.tex`, `kap1_loesungen_L.tex`. Reihenfolge: en zuerst, zh aus dem fertigen Englisch (mit dem Deutschen daneben), es, fr, tr aus dem Deutschen.

Titel (verbindlich, aus heft_zu_artikel.py): en „Vectors and Matrices“, es „Vectores y matrices“, zh „向量与矩阵“, fr „Vecteurs et matrices“, tr „Vektörler ve Matrisler“. Titelblock-Zeile mit `Foundations~1` usw. wie oben, Datum 4. November 2026.

Verweise im Heft: `Unterabschnitt~\ref{k1:…}` = en `Subsection~\ref`, es `subsección~\ref` (am Satzanfang `Subsección`), zh `第~\ref{…}~小节`, fr `sous-section~\ref`, tr `alt kesim~\ref` bzw. `Alt kesim~\ref{…}'de`. `Abschnitt~\ref{k1:…}` wie oben (Section, sección, 第~\ref{…}~节, section, Kesim). `Abbildung~\ref` am Satzanfang = Figure / La figura / 图 / La figure / Şekil. `Tabelle~\ref` = Table / tabla / 表 / tableau / Tablo. Die Grundlagen-1-Wörter, die Grundlagen 2 schon benutzt (1-Norm, Gleich-/Wechselmuster, Zeilen-/Spaltensicht, Kreuz = cross | cruz | 十字 | croix | artı işareti, Wohnungen, Einsvektor), heißen genau wie dort.

Sprachgebundene Stellen (sinngemäß anpassen, nichts weglassen):
- kap1_stufen.tex, „Spalte und Zeile“: Der Satz über Semikolons begründet sich mit dem Dezimalkomma. es/fr/tr übernehmen ihn wörtlich (Semikolon, `{,}`). en/zh schreiben sinngemäß: Die Komponenten werden durch Kommas getrennt; weil Dezimalzahlen hier einen Punkt haben, gibt es keine Verwechslung: `$(0.2,\ 0.25,\ 0.3)\T$ has three components`.
- kap1_stufen.tex, „Zwei Hinweise zu den Wörtern“: Datenbank-Zeile = record | registro | 记录 | enregistrement | kayıt; das Wort Beispiel gegen die feste Wendung für Rechenbeispiel (worked example | ejemplo numérico | 算例 | exemple de calcul | sayısal örnek) stellen.
- Hintergrund „Dieselben Dinge mit anderen Namen“: Die englischen Fachwörter bleiben (\emph). Statt der deutschen Synonyme („Datenpunkt“, „Stichprobe“) die in der Zielsprache verbreiteten nennen. en: sinngemäß „Other texts call an example a sample, an instance or a data point, a feature an attribute, …“, ohne „in English-language texts“.
- Hintergrund „Andere Schreibweisen für dasselbe“: en sinngemäß „the same number is also called the inner product or scalar product“; die anderen Sprachen behalten „auf Englisch heißt es dot product oder inner product“.
- „signalangepassten Filters (\emph{matched filter})“: en nur matched filter; andere Sprachen Wort der Sprache plus (\emph{matched filter}). „rms steht für root mean square“ bleibt in allen Sprachen.
- TikZ, Abb. fig:k1einheiten: Die deutsche Datei hat seit 06.11.2026 `\foreach \x/\t in {5.4/5{,}4,6/6,6.6/6{,}6}` (Achsenzahlen mit Komma). en/zh: `{5.4/5.4,6/6,6.6/6.6}`; es/fr/tr wie deutsch. Koordinaten nie ändern.
- Alle TikZ-Beschriftungen übersetzen und die Wörter der Szenen benutzen (unten). Längere Beschriftungen nicht kürzen, nur wenn sie über das Bild hinausragen würden, sinngemäß knapper.

Bildwörter (ml_teil1.py = TikZ im Heft), de = en | es | zh | fr | tr:
als Punkt/als Pfeil = as a point/as an arrow | como punto/como flecha | 看作点/看作箭头 | comme point/comme flèche | nokta olarak/ok olarak;
x wechselt im Takt = x alternates | x alterna | x 交替变化 | x alterne en cadence | x işaret değiştirir; x' steigt gleichmäßig = x' rises steadily | x' sube de forma regular | x' 平稳上升 | x' croît régulièrement | x' düzgün biçimde artar; Muster w, Signal, Produkte = pattern w, signal, products | patrón w, señal, productos | 模式 w, 信号, 乘积 | motif w, signal, produits | örüntü w, sinyal, çarpımlar;
Fläche in m², Fläche in 10 m², Zimmer = area in m², area in 10 m², rooms | superficie (m²), superficie (10 m²), cuartos (nur diese Achse, aus Platzgründen; sonst habitaciones) | 面积 m², 面积 10 m², 房间数 | surface (m²), surface (10 m²), pièces | alan (m²), alan (10 m²), oda;
Schatten 2,6 = shadow 2.6 | sombra 2,6 | 影长 2.6 | ombre 2,6 | gölge 2,6;
Wohnung i, Fläche, Zimmer, Entfernung = apartment i, area, rooms, distance | vivienda i, superficie, habitaciones, distancia | 公寓 i, 面积, 房间, 距离 | appartement i, surface, pièces, distance | daire i, alan, oda, uzaklık; Zeile 2: Beispiel x₂ᵀ = row 2: example | fila 2: ejemplo | 第 2 行：样本 | ligne 2 : exemple | satır 2: örnek; Spalte 1: Merkmal Fläche = column 1: feature area | columna 1: característica superficie | 第 1 列：特征 面积 | colonne 1 : caractéristique surface | sütun 1: öznitelik alan;
Zeilensicht, Spaltensicht, Zeile 1 mal x = row view, column view, row 1 times x | visión por filas, visión por columnas, fila 1 por x | 行视角, 列视角, 第 1 行乘 x | vue par lignes, vue par colonnes, ligne 1 fois x | satır bakışı, sütun bakışı, satır 1 çarpı x;
Drehung, Streckung, Scherung, Plattdrücken = rotation, stretch, shear, flattening | rotación, estiramiento, cizalladura, aplastamiento | 旋转, 拉伸, 剪切, 压扁 | rotation, étirement, cisaillement, aplatissement | dönme, germe, kayma, yassılaştırma;
vorher, erst drehen, dann strecken / erst strecken, dann drehen = before, rotate first, then stretch / stretch first, then rotate | antes, primero girar, luego estirar / primero estirar, luego girar | 变换前, 先旋转，再拉伸 / 先拉伸，再旋转 | avant, d’abord tourner, puis étirer / d’abord étirer, puis tourner | önce, önce döndür, sonra ger / önce ger, sonra döndür;
(a) genau eine Lösung, (b) keine Lösung, (c) unendlich viele = exactly one solution, no solution, infinitely many | exactamente una solución, ninguna solución, infinitas | 唯一解, 无解, 无穷多解 | exactement une solution, aucune solution, une infinité | tek bir çözüm, çözüm yok, sonsuz sayıda;
Einheitsquadrat, Bild unter A = unit square, image under A | cuadrado unidad, imagen bajo A | 单位正方形, A 作用后的像 | carré unité, image par A | birim kare, A altındaki görüntü;
Skalar Form: keine, Vektor Form 4, Matrix Form 4×4, Farbbild Form 3×4×4, Bildstapel Form N×3×4×4 = scalar shape: none, vector shape 4, matrix shape 4×4, color image shape …, image stack shape … | escalar forma vacía, vector forma 4, matriz forma 4×4, imagen en color forma …, pila de imágenes forma … | 标量 形状：无, 向量 形状 4, 矩阵 形状 4×4, 彩色图像 形状 …, 图像堆叠 形状 … | scalaire forme vide, vecteur forme 4, matrice forme 4×4, image couleur forme …, pile d’images forme … | skaler şekil: yok, vektör şekil 4, matris şekil 4×4, renkli görüntü şekil …, görüntü yığını şekil ….

Korrekturen am Original (in der deutschen Datei eingetragen):
- kap1_stufen.tex Z. 897 (TikZ fig:k1einheiten): Achsenzahlen 5,4 und 6,6 jetzt mit Dezimalkomma (vorher druckte `$\x$` „5.4“, „6.6“).
- kap1_stufen.tex Z. 1024 (Hintergrund „Warum gerade die Standardabweichung als Maßstab?“): „… einen Maßstab, der sich bei einem Einheitenwechsel um denselben Faktor ändert wie die Unterschiede zwischen den Werten. … Jede Größe, die aus den Unterschieden zwischen den Werten des Merkmals berechnet wird und die Einheit des Merkmals hat, leistet das“ (vorher „genauso ändert wie die Zahlen selbst“ und „aus den Daten des Merkmals berechnet“: falsch für den Mittelwert, der bei v' = αv + β nicht nur mit dem Faktor α wächst).
- kap1_stufen_b.tex Z. 17: „macht aus Geraden wieder Geraden oder einzelne Punkte … wieder parallele, gleichabständige Linien oder Punkte“ (vorher ohne „oder (einzelne) Punkte“; falsch fürs Plattdrücken).
- kap1_stufen_b.tex Z. 78: „Weil die Abbildung Linearkombinationen erhält, wird das Quadrat zu dem Parallelogramm …“ (vorher „Weil die Abbildung Geraden auf Geraden abbildet“).
- kap1_stufen_b.tex Z. 1369: „… mit einem festen Vektor ist die Multiplikation mit einer Diagonalmatrix“ (vorher „ist eine Diagonalmatrix“).
- kap1_loesungen.tex Z. 42: „obwohl ihr Gewicht dem Betrag nach das kleinste ist“ (Gewichte 3, 10, −4).
- kap1_loesungen.tex Z. 87: „jedes von null verschiedene Vielfache davon ebenso“ (die Aufgabe verlangt v ≠ 0).
- ml_teil1.py, Szenen k1ebene und k1reihenfolge: Achsen jetzt ohne Teilstriche und Zahlen wie im Heft (vorher drängten sich automatische Zahlen 0,25 … 1,5 über die Bilder, in allen Sprachen).
