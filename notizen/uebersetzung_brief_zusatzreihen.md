# Brief: Übersetzung ML-Arbeitsheft Grundlagen 2 („Projektion, Eigenwerte und Zerlegungen“)

**Seit 09.11.2026 (Benennung „Kapitel N“, `notizen/kapitel_umstellung.md`):** Jedes Heft heißt „Kapitel N“, gezählt im Bereich; die ML-Hefte T01–T06 sind Kapitel 1–6 der „Mathematischen Grundlagen“, der ML-Pfad zählt ab T08 als Kapitel 1. Es gelten die Verweis- und Titelwendungen der Tabelle „Feste Wendungen“ unten, in `heft_uebersetzung.md` (Abschnitt „Verweise auf andere Hefte“) und die Formentabelle in `kapitel_umstellung.md`. Wo weiter unten in den Einzelbriefen noch „Foundations~N“, „Fundamentos~N“, „基础篇~N“, „Temeller~N“ oder die alten Titelblock-Zeilen stehen, gilt die neue Form („Chapter~N“ usw., Titelzeile „Workbook Machine Learning, Mathematical Foundations, Chapter~N“). Dateinamen (Kap2_Eigenwerte …) bleiben.

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
- Abschnittsnummern wie „Kapitel~1, Abschnitt~13.5“ sind KEINE Dezimalzahlen: `13.5` bleibt mit Punkt in allen Sprachen.
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
- tr-Typografie: `:` und `!` ohne Leerzeichen davor; İ/ı genau; Endungen nach Zahlen/Verweisen mit Apostroph (`Bölüm~1'de`, `Alıştırma~\ref{a:k2onb}'deki`). Anrede „siz“.
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
| Kapitel~1 (Heft im selben Bereich, seit 09.11.2026; früher „Grundlagen~1“, „Teil~1“) | Chapter~1 | capítulo~1 („el capítulo~1“, „del capítulo~1“, Satzanfang „El capítulo~1“) | 第~1~章 | chapitre~1 („le chapitre~1“, „du chapitre~1“, Satzanfang „Le chapitre~1“) | Bölüm~1 (Endung: `Bölüm~1'de`) |
| Kapitel~1, Abschnitt~13.5 | Chapter~1, Section~13.5 | capítulo~1, sección~13.5 | 第~1~章第~13.5~节 | chapitre~1, section~13.5 | Bölüm~1, Kesim~13.5 |
| Grundlagen, Kapitel~1 (ML-Grundlagen aus dem ML-Pfad) | Foundations, Chapter~1 | Fundamentos, capítulo~1 | 数学基础第~1~章 | Fondements, chapitre~1 | Temeller, Bölüm~1 |
| Python, Kapitel~2, Abschnitt~3 | Python, Chapter~2, Section~3 | Python, capítulo~2, sección~3 | Python~第~2~章第~3~节 | Python, chapitre~2, section~3 | Python, Bölüm~2, Kesim~3 |
| Linux, Kapitel~2, Abschnitt~3 | Linux, Chapter~2, Section~3 | Linux, capítulo~2, sección~3 | Linux~第~2~章第~3~节 | Linux, chapitre~2, section~3 | Linux, Bölüm~2, Kesim~3 |
| Abschnitt~X / Unterabschnitt | Section / subsection | sección / subsección (Sección am Satzanfang) | 第~X~节 / 小节 | section / sous-section | Kesim / alt kesim |
| Abb.~\ref | Fig.~\ref | Fig.~\ref (wie ET3 es) | 图~\ref | Fig.~\ref | Şekil~\ref |
| Aufgabe~\ref | Exercise~\ref | Ejercicio~\ref / ejercicio | 练习~\ref | exercice~\ref (Exercice am Satzanfang) | Alıştırma~\ref |
| `\begin{beispiel}[Rechenbeispiel]{…}` / `[Rechenbeispiel 1]` | `[Worked example]` / `[Worked example 1]` | `[Ejemplo numérico]` | `[算例]` / `[算例 1]` | `[Exemple de calcul]` | `[Sayısal örnek]` |
| `\begin{beispiel}{Titel}` / `\begin{beispiel}{}` | Umgebungsname bleibt `beispiel`, nur der Titel wird übersetzt (ohne das Wort „Beispiel“ und ohne Schlusspunkt; das Wort setzt die Präambel: Example, Ejemplo, 例, Exemple, Örnek) | | | | |
| Kurz gesagt: | In short: | wie ET3 es | wie ET3 zh | En bref : | Kısacası: |
| Kästen im Einleitungstext: „Hintergrund“, „Beweis“, „Herleitung“ | Background, Proof, Derivation | Contexto, Demostración, Deducción | 背景, 证明, 推导 | Contexte, Preuve, Démonstration | Arka plan, İspat, Türetme |
| Unterabschnitt „Was du dafür brauchst: …“ | What you need for this: … | Lo que necesitas: … | 所需知识：… | Ce dont vous avez besoin : … | Bunun için gerekenler: … |
(Die Kastenwörter „Definition“, „Satz“, „Aufgabe“, „Beweis:“, „Herleitung:“, „Hintergrund:“, „Achtung:“, „Worum es geht:“ und „Beispiel:“ setzt die Präambel selbst; die Titel in den geschweiften Klammern und das optionale Wort von `beispiel` werden übersetzt. Anfang und Ende jedes `beispiel`-Kastens stehen an derselben Stelle wie im Deutschen.)

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

### Ergänzt bei Grundlagen 3 (Ableitung, Gradient, Kettenregel, 09.11.2026)
Schon oben und hier genauso: Höhenlinien, Schüssel/Rinne/Sattel, quadratische Form, gemischtes Glied, Eigenwert/Eigenvektor, Spur, Spektralsatz, Hauptachsen, positiv definit/indefinit, Residuum, beste Näherungslösung, Normalgleichungen, Ausgleichsgerade, Achsenabschnitt/Steigung, äußeres Produkt, Frobeniusnorm, Baustein, elementweise, Matrix-Vektor-Produkt, Zeilensicht, Hintereinanderausführung, lineare Stufe, Grundrechenarten, Einheitsvektor, Cauchy-Schwarz-Ungleichung, Schattenlänge, Determinante/Flächenfaktor, Gewicht/Merkmal/Vorhersage, Tausend Euro, Einheitskreis, Einheits-/Diagonalmatrix, Doppelsumme, Komponente, Transponierte, symmetrische Matrix, affine Abbildung, Gitter, Form (shape), Rang, Gegenbeispiel.
Ableitung einer Variablen
- Änderungsrate = rate of change | tasa de variación | 变化率 | taux de variation | değişim hızı
- Differenzenquotient = difference quotient | cociente incremental (cociente de diferencias) | 差商 | taux d’accroissement | fark bölümü
- Sekante, Sekantensteigung = secant line (im Bild: secant), slope of the secant | recta secante (en figuras: secante), pendiente de la secante | 割线, 割线斜率 | sécante, pente de la sécante | kesen (kesen doğru), kesenin eğimi
- Schrittweite = step size | paso (tamaño de paso) | 步长 | pas | adım büyüklüğü
- Grenzwert, beliebig nah = limit, arbitrarily close | límite, arbitrariamente cerca | 极限, 任意接近 | limite, arbitrairement proche | limit, istenildiği kadar yakın
- differenzierbar, Differenzierbarkeit = differentiable, differentiability | derivable (eine Variable), diferenciable (mehrere Variablen, ab Abschnitt 3); diferenciabilidad | 可导（一元）, 可微（多元，第 3 节起）; 可微性 | dérivable (une variable), différentiable (plusieurs variables, dès la section 3) ; différentiabilité | türevlenebilir, türevlenebilirlik
- Ableitung, Ableitungsfunktion = derivative, derivative (function) | derivada, función derivada | 导数, 导函数 | dérivée, fonction dérivée | türev, türev fonksiyonu
- Tangente = tangent line (im Bild: tangent) | recta tangente (en figuras: tangente) | 切线 | tangente | teğet (teğet doğru)
- Knick = kink (corner) | punto anguloso (pico) | 折点（尖点） | point anguleux | köşe noktası (kırılma)
- Betragsfunktion = absolute value function | función valor absoluto | 绝对值函数 | fonction valeur absolue | mutlak değer fonksiyonu
- lineare Näherung = linear approximation | aproximación lineal | 线性近似 | approximation linéaire (approximation affine) | doğrusal yaklaşım
- Empfindlichkeit, (kleine Änderungen) weitergeben = sensitivity, pass on | sensibilidad, transmitir | 灵敏度, 传递 | sensibilité, transmettre | duyarlılık, iletmek
- Lupe, Ausschnitt (Teilbild) = magnifying glass, window | lupa, ventana | 放大镜, 局部窗口 | loupe, fenêtre | büyüteç, pencere
- Grundableitungen = basic derivatives | derivadas elementales | 基本导数公式 | dérivées usuelles | temel türevler
- Ableitungsregeln: Summen-, Faktor-, Produkt-, Quotienten-, Potenzregel = differentiation rules: sum rule, constant multiple rule, product rule, quotient rule, power rule | reglas de derivación: regla de la suma, del factor constante, del producto, del cociente, de la potencia | 求导法则：和法则、常数倍法则、乘积法则、商法则、幂法则 | règles de dérivation : règle de la somme, du facteur constant, du produit, du quotient, des puissances | türev kuralları: toplam, sabit çarpan, çarpım, bölüm, kuvvet kuralı
- Streifen, Eckstück (Rechteckbild der Produktregel) = strip, corner piece | franja, pieza de la esquina | 长条, 角上的小块 | bande, petit carré du coin | şerit, köşe parçası
- binomischer Lehrsatz, Hochzahl, Bogenmaß = binomial theorem, exponent, radians | teorema del binomio (binomio de Newton), exponente, radianes | 二项式定理, 指数, 弧度 | formule du binôme (de Newton), exposant, radians | binom teoremi, üs, radyan
- e-Funktion, Eulersche Zahl, Logarithmus, Basis (einer Potenz) = exponential function, Euler’s number, natural logarithm, base | función exponencial, número e (número de Euler), logaritmo neperiano, base | 指数函数, 自然常数 e, 自然对数, 底数 | fonction exponentielle, nombre e (nombre d’Euler), logarithme népérien, base | üstel fonksiyon, e sayısı (Euler sayısı), doğal logaritma, taban
- zweite / dritte / k-te Ableitung, höhere Ableitungen = second / third / k-th derivative, higher derivatives | segunda / tercera / k-ésima derivada, derivadas de orden superior | 二阶 / 三阶 / k 阶导数, 高阶导数 | dérivée seconde / troisième / k-ième, dérivées d’ordre supérieur | ikinci / üçüncü / k. türev, yüksek mertebeden türevler
- Krümmung (des Graphen), sich nach oben / unten (von der Tangente) wegbiegen = curvature, bend upward / downward (away from the tangent) | curvatura, curvarse hacia arriba / abajo | 曲率（弯曲程度）, 向上 / 向下弯离（切线） | courbure, s’incurver vers le haut / le bas | eğrilik, yukarı / aşağı doğru bükülmek
- quadratische Näherung, Parabel = quadratic approximation, parabola | aproximación cuadrática, parábola | 二次近似, 抛物线 | approximation quadratique, parabole | ikinci dereceden yaklaşım, parabol
- stetig, Stetigkeit, Sprung = continuous, continuity, jump | continua, continuidad, salto | 连续, 连续性, 跳跃 | continue, continuité, saut | sürekli, süreklilik, sıçrama
- Satz von Taylor, Taylorpolynom k-ter Ordnung = Taylor’s theorem, Taylor polynomial of order k | teorema de Taylor, polinomio de Taylor de orden k | 泰勒定理, k 阶泰勒多项式 | formule de Taylor, polynôme de Taylor d’ordre k | Taylor teoremi, k. mertebeden Taylor polinomu
- Glied (einer Summe/Näherung), Glied zweiter Ordnung, Steigungsglied, Krümmungsglied = term, second-order term, slope term, curvature term | término, término de segundo orden, término de pendiente, término de curvatura | 项, 二阶项, 斜率项, 曲率项 | terme, terme d’ordre deux, terme de pente, terme de courbure | terim, ikinci mertebe terim, eğim terimi, eğrilik terimi
- Mittelwertsatz = mean value theorem | teorema del valor medio | 中值定理 | théorème des accroissements finis | ortalama değer teoremi
Kettenregel
- Verkettung, innere / äußere Funktion = composition (composite function), inner / outer function | composición (función compuesta), función interior / exterior | 复合（复合函数）, 内层函数 / 外层函数 | composition (fonction composée), fonction intérieure / extérieure | bileşke (bileşke fonksiyon), iç / dış fonksiyon
- Kettenregel = chain rule | regla de la cadena | 链式法则 | règle de dérivation en chaîne | zincir kuralı
- Kette, Glied (einer Kette) = chain, link | cadena, eslabón | 链, 环节 | chaîne, maillon | zincir, halka
- Stufe (einer Rechnung), Faktor einer Stufe = stage, factor | etapa, factor | 级, 因子 | étage (nicht « étape », das ist die Heft-Stufe), facteur | aşama, çarpan
- Zwischenwert, Zwischenvariable, Zwischenergebnis, Zwischenprodukt = intermediate value, intermediate variable, intermediate result, partial product | valor intermedio, variable intermedia, resultado intermedio, producto parcial | 中间值, 中间变量, 中间结果, 部分积 | valeur intermédiaire, variable intermédiaire, résultat intermédiaire, produit partiel | ara değer, ara değişken, ara sonuç, kısmi çarpım
- Getriebe, Übersetzungsstufe, Zahlenstrahl = gear train, gear stage, number line | tren de engranajes, etapa de engranajes, recta numérica | 齿轮传动, 传动级, 数轴 | train d’engrenages, étage d’engrenages, droite graduée | dişli takımı, dişli kademesi, sayı doğrusu
- logistische Funktion = logistic function | función logística | 逻辑斯谛函数（logistic 函数） | fonction logistique | lojistik fonksiyon
- Wachstum mit Sättigung, Obergrenze, Anteil = growth with saturation, upper limit, proportion | crecimiento con saturación, cota superior, proporción | 饱和增长, 上限, 比例 | croissance avec saturation, plafond, proportion | doygunluklu büyüme, üst sınır, oran
- punktsymmetrisch zum Punkt P, spiegelsymmetrisch zur senkrechten Achse = symmetric about the point P, symmetric about the vertical axis | simétrica respecto del punto P, simétrica respecto del eje vertical | 关于点 P 中心对称, 关于纵轴对称 | symétrique par rapport au point P, symétrique par rapport à l’axe vertical | P noktasına göre simetrik, düşey eksene göre simetrik
- Umkehrfunktion = inverse function | función inversa | 反函数 | fonction réciproque | ters fonksiyon
- Glockenkurve, Gipfel = bell curve, peak | curva de campana, cima | 钟形曲线, 峰顶 | courbe en cloche, sommet | çan eğrisi, tepe
Mehrere Variablen und Gradient
- Funktion von d Variablen = function of d variables | función de d variables | d 元函数 | fonction de d variables | d değişkenli fonksiyon
- Niveaumenge = level set | conjunto de nivel | 水平集（等值集） | ensemble de niveau | düzey kümesi
- Landschaft, Gelände, Landkarte, Wanderkarte, Ort, Höhe = landscape, terrain, map, hiking map, location, height | paisaje, terreno, mapa, mapa de senderismo, lugar, altura | 地形, 地面, 地图, 登山地图, 位置, 高度 | paysage, terrain, carte, carte de randonnée, lieu, altitude | arazi, arazi yüzeyi, harita, yürüyüş haritası, konum, yükseklik
- Schnitt, Schnittkurve, Schnittgerade = cross section (im Bildtitel: section), cross-section curve, cutting line | corte, curva de corte, recta de corte | 截面（im Bildtitel: 截线）, 截线, 截取直线 | coupe, courbe de coupe, droite de coupe | kesit, kesit eğrisi, kesit doğrusu
- partielle Ableitung, nach x_j ableiten, festhalten = partial derivative, differentiate with respect to x_j, hold fixed | derivada parcial, derivar respecto de x_j, mantener fija | 偏导数, 对 x_j 求导, 固定 | dérivée partielle, dériver par rapport à x_j, fixer | kısmi türev, x_j'ye göre türev almak, sabit tutmak
- Gradient, Nabla = gradient, nabla (del) | gradiente, nabla | 梯度, nabla 算子 | gradient, nabla | gradyan, nabla
- Feld von Pfeilen = field of arrows | campo de flechas | 箭头场 | champ de flèches | ok alanı
- Tangentialebene, schräg gestellte Platte, Neigung = tangent plane, tilted plate, tilt | plano tangente, placa inclinada, inclinación | 切平面, 倾斜的平板, 倾斜度 | plan tangent, plaque inclinée, inclinaison | teğet düzlem, eğik levha, eğiklik (nicht „eğim“, das ist Steigung)
- Verschiebung (Schritt h auf der Landkarte) = displacement | desplazamiento | 位移 | déplacement | yer değiştirme (nicht die Signal-Verschiebung aus Grundlagen 1: shift, décalage, kaydırma)
- Wirkung, Wechselwirkung = effect, interaction | efecto, interacción | 作用, 交互作用 | effet, interaction | etki, etkileşim
- Nullpunkt, Diagonale (x₁ = x₂), Falte = origin, diagonal, crease | origen, diagonal, pliegue | 原点, 对角线, 折痕 | origine, diagonale, pli | orijin, köşegen, kıvrım
Richtungsableitung und steilster Anstieg
- Richtungsableitung, zweite Richtungsableitung = directional derivative, second directional derivative | derivada direccional, segunda derivada direccional | 方向导数, 二阶方向导数 | dérivée directionnelle, dérivée directionnelle seconde | yönlü türev, ikinci yönlü türev
- steilster Anstieg / Abstieg, steilste Richtung = steepest ascent / descent, steepest direction | máximo ascenso / máximo descenso, dirección de máxima pendiente | 最速上升 / 最速下降, 最陡方向 | plus forte montée / plus forte descente, direction de plus grande pente | en dik çıkış / en dik iniş, en dik doğrultu
- bergauf, bergab, tiefster Punkt = uphill, downhill, lowest point | cuesta arriba, cuesta abajo, punto más bajo | 上坡, 下坡, 最低点 | en montée, en descente, point le plus bas | yokuş yukarı, yokuş aşağı, en alçak nokta
- runde / gestreckte Schüssel, Wände = round / elongated bowl, walls | cuenco redondo / alargado, paredes | 圆碗 / 拉长的碗, 碗壁 | cuvette ronde / allongée, parois | yuvarlak / uzamış çanak, çeperler
- Fußpunkt (eines Gradientenpfeils) = base point | punto de partida | 起点 | point de départ | başlangıç noktası
- Ellipse, Hyperbel, Winkelhalbierende = ellipse, hyperbola, angle bisector | elipse, hipérbola, bisectriz | 椭圆, 双曲线, 角平分线 | ellipse, hyperbole, bissectrice | elips, hiperbol, açıortay
- Tangentenrichtung, komponentenweise, Budget = tangent direction, componentwise, budget | dirección tangente, componente a componente, presupuesto | 切线方向, 逐分量, 预算 | direction tangente, composante par composante, budget | teğet doğrultusu, bileşen bileşen, bütçe
Jacobi-Matrix und Kettenregel mehrerer Variablen
- vektorwertig, Komponenten (einer Funktion) = vector-valued, components | vectorial (con valores vectoriales), componentes | 向量值, 分量函数 | à valeurs vectorielles, composantes | vektör değerli, bileşenler
- Eingang, Ausgang = input, output | entrada, salida | 输入, 输出 | entrée, sortie | girdi, çıktı
- Jacobi-Matrix = Jacobian matrix (Jacobian) | matriz jacobiana | 雅可比矩阵 | matrice jacobienne | Jacobi matrisi
- fett, mager (Schrift) = bold, non-bold | en negrita, en letra normal | 粗体, 非粗体 | en gras, en maigre | kalın, normal yazı
- Polarkoordinaten, Kreisring, Bogen = polar coordinates, annulus, arc | coordenadas polares, corona circular, arco | 极坐标, 圆环, 弧 | coordonnées polaires, couronne, arc | kutupsal koordinatlar, halka, yay
- Einheitsgitter = unit grid | cuadrícula unidad | 单位网格 | quadrillage unité | birim ızgara
- Weg, Summe über alle Wege, Netz von Wegen = path, sum over all paths, network of paths | camino, suma sobre todos los caminos, red de caminos | 路径, 对所有路径求和, 路径网络 | chemin, somme sur tous les chemins, réseau de chemins | yol, tüm yollar üzerinden toplam, yol ağı
- Knoten, Kante, Kantenfaktor (im Graphen) = node, edge, edge factor | nodo (nicht „nudo“ wie im Stromkreis), arista, factor de la arista | 节点, 边, 边上的因子 | nœud, arête, facteur de l’arête | düğüm, kenar, kenar çarpanı
- Rohrnetz, Ströme (im Rohrnetz) = pipe network, flows | red de tuberías, caudales | 管网, 水流 | réseau de canalisations, débits | boru ağı, akışlar (nicht „akım“)
- Kurve, Geschwindigkeitsvektor, Tempo = curve, velocity vector, speed | curva, vector velocidad, rapidez | 曲线, 速度向量, 速率 | courbe, vecteur vitesse, vitesse (norme du vecteur vitesse) | eğri, hız vektörü, sürat
- Buchführung = bookkeeping | contabilidad | 记账 | comptabilité | muhasebe
Ableiten nach Vektoren und Matrizen
- Layout-Konvention, Zähler-Layout, Nenner-Layout, Mischform = layout convention, numerator layout, denominator layout, mixed layout | convención de disposición, disposición de numerador, disposición de denominador, forma mixta | 布局约定, 分子布局, 分母布局, 混合布局 | convention de disposition, disposition numérateur, disposition dénominateur, forme mixte | düzen kuralı, pay düzeni, payda düzeni, karma biçim
- Formprobe, Merkhilfe = shape check, mnemonic | comprobación de la forma, regla mnemotécnica | 形状检查, 助记方法 | vérification des formes, moyen mnémotechnique | şekil kontrolü, akılda tutma yolu
- Quadratsumme, symmetrischer Anteil = sum of squares, symmetric part | suma de cuadrados, parte simétrica | 平方和, 对称部分 | somme des carrés, partie symétrique | kareler toplamı, simetrik kısım
- Ableitung nach einer Matrix = derivative with respect to a matrix | derivada respecto de una matriz | 对矩阵的导数 | dérivée par rapport à une matrice | bir matrise göre türev
- Rückwärtsregel (des Matrixprodukts) = backward rule (of the matrix product) | regla hacia atrás (del producto de matrices) | （矩阵乘积的）反向法则 | règle arrière (du produit matriciel) | (matris çarpımının) geri kuralı
Hesse-Matrix
- zweite partielle Ableitungen, gemischte Ableitungen = second partial derivatives, mixed partial derivatives | derivadas parciales segundas, derivadas cruzadas | 二阶偏导数, 混合偏导数 | dérivées partielles secondes, dérivées croisées | ikinci kısmi türevler, karma kısmi türevler
- Hesse-Matrix = Hessian matrix (Hessian) | matriz hessiana | 黑塞矩阵 | matrice hessienne | Hesse matrisi
- Satz von Schwarz = Schwarz’s theorem (Clairaut’s theorem) | teorema de Schwarz | 施瓦茨定理 | théorème de Schwarz | Schwarz teoremi
- gemischte Differenz, Grenzübergang = mixed difference, passage to the limit | diferencia mixta, paso al límite | 混合差分, 取极限 | différence croisée, passage à la limite | karma fark, limite geçiş
- gewölbte Fläche, Wölbung = curved surface, curvature | superficie curvada, curvatura | 弯曲的曲面, 弯曲 | surface bombée, bombement | kavisli yüzey, kavis
- Krümmung in einer Richtung = curvature in a direction | curvatura en una dirección | 沿某方向的曲率 | courbure dans une direction | bir doğrultudaki eğrilik
- Hesse-Matrix mal Vektor = Hessian-vector product | producto hessiana-vector | 黑塞矩阵与向量的乘积 | produit hessienne-vecteur | Hesse matrisi-vektör çarpımı
Rechengraph und automatische Differentiation
- Rechengraph, gerichtete Kante, kreisfrei = computational graph, directed edge, acyclic | grafo computacional, arista dirigida, acíclico | 计算图, 有向边, 无环 | graphe de calcul, arête orientée, acyclique | hesaplama grafiği, yönlü kenar, döngüsüz
- Eingangsknoten, Vorgänger, Nachfolger, Ergebnis = input node, predecessor, successor, result | nodo de entrada, predecesor, sucesor, resultado | 输入节点, 前驱, 后继, 结果 | nœud d’entrée, prédécesseur, successeur, résultat | girdi düğümü, öncül, ardıl, sonuç
- Grundoperation; Additions-, Multiplikations-, Quadrat-, Maximum-Knoten = elementary operation; addition, multiplication, square, max node | operación elemental; nodo de suma, de producto, de cuadrado, de máximo | 基本运算; 加法、乘法、平方、最大值节点 | opération de base ; nœud d’addition, de multiplication, carré, maximum | temel işlem; toplama, çarpma, kare, maksimum düğümü
- Vorwärtsrechnung = forward evaluation | evaluación hacia adelante | 前向计算 | évaluation avant | ileri hesaplama
- lokale Ableitung = local derivative | derivada local | 局部导数 | dérivée locale | yerel türev
- Schleife, Verzweigung, Programm = loop, branch, program | bucle, bifurcación, programa | 循环, 分支, 程序 | boucle, branchement, programme | döngü, dallanma, program
- automatische Differentiation, symbolisches / numerisches Ableiten = automatic differentiation, symbolic / numerical differentiation | diferenciación automática, derivación simbólica / numérica | 自动微分, 符号求导 / 数值求导 | différentiation automatique, dérivation symbolique / numérique | otomatik türev alma, sembolik / sayısal türev alma
- Vorwärtsmodus, Rückwärtsmodus = forward mode, reverse mode | modo directo, modo inverso | 前向模式, 反向模式 | mode direct, mode inverse | ileri mod, ters mod
- Tangentenwert = tangent value | valor tangente | 切线值 | valeur tangente | teğet değeri
- Adjungierte = adjoint | adjunto | 伴随值 | adjoint | eşlenik (adjoint)
- Durchlauf, Vorwärts- / Rückwärtsdurchlauf = pass, forward / backward pass | pasada, pasada hacia adelante / hacia atrás | 一遍, 前向 / 反向传递 | passe, passe avant / arrière | geçiş, ileri / geri geçiş
- rückwärts rechnen, Rückwärtsfluss = compute backward, backward flow | calcular hacia atrás, flujo hacia atrás | 反向计算, 反向流动 | calculer à rebours, flux arrière | geriye doğru hesaplamak, geri akış
- duale Zahlen = dual numbers | números duales | 对偶数 | nombres duaux | dual sayılar
- Aufwand, Auswertung, Speicher = cost, evaluation, memory | coste, evaluación, memoria | 计算量, 求值, 内存 | coût, évaluation, mémoire | maliyet, değerlendirme, bellek
- Klammerung von links / rechts = parenthesization from the left / right | asociación por la izquierda / derecha | 从左 / 从右结合 | parenthésage par la gauche / la droite | soldan / sağdan parantezleme
- Zwischensumme = partial sum | suma parcial | 部分和 | somme partielle | ara toplam
- Faustregel, Stellschraube = rule of thumb, adjustable knob | regla práctica, perilla de ajuste | 经验法则, 调节旋钮 | règle empirique, bouton de réglage | pratik kural, ayar düğmesi
- Abschlussarbeit (Linnainmaa 1970) = master’s thesis | tesis de maestría | 硕士论文 | mémoire de master | yüksek lisans tezi
Numerische Ableitung
- numerische Ableitung = numerical differentiation | derivación numérica | 数值微分 | dérivation numérique | sayısal türev
- Vorwärtsdifferenz, zentrale Differenz = forward difference, central difference | diferencia progresiva, diferencia central | 前向差分, 中心差分 | différence avant, différence centrée | ileri fark, merkezi fark
- Abschneidefehler, Rundungsfehler, Gesamtfehler = truncation error, rounding error, total error | error de truncamiento, error de redondeo, error total | 截断误差, 舍入误差, 总误差 | erreur de troncature, erreur d’arrondi, erreur totale | kesme hatası, yuvarlama hatası, toplam hata
- Gleitkommazahl, Kommazahl = floating-point number, non-integer (decimal) number | número en coma flotante, número decimal | 浮点数, 小数 | nombre à virgule flottante (flottant), nombre à virgule | kayan noktalı sayı, ondalıklı sayı
- Binärziffer, Zweiersystem, Zweierpotenz, Dezimalstelle = binary digit, binary system, power of two, decimal digit | dígito binario, sistema binario, potencia de dos, cifra decimal | 二进制位, 二进制, 2 的幂, 十进制位 | chiffre binaire, système binaire, puissance de deux, chiffre décimal | ikili basamak, ikili sistem, ikinin kuvveti, ondalık basamak
- doppelte / einfache Genauigkeit, Norm IEEE 754 = double / single precision, IEEE 754 standard | doble / simple precisión, norma IEEE 754 | 双精度 / 单精度, IEEE 754 标准 | double / simple précision, norme IEEE 754 | çift / tek duyarlık, IEEE 754 standardı
- Maschinengenauigkeit = machine epsilon | épsilon de máquina | 机器精度（machine epsilon） | epsilon machine | makine epsilonu
- Auslöschung = cancellation (catastrophic cancellation) | cancelación catastrófica | 相消（灾难性抵消） | annulation catastrophique | anlamlı basamak kaybı (yıkıcı sadeleşme)
- richtige Stellen = correct digits | cifras correctas | 正确的位数 | chiffres exacts | doğru basamaklar
- Fehlerkurve, V-Kurve, doppelt logarithmisch = error curve, V-shaped curve, on log-log axes | curva de error, curva en V, en escala doble logarítmica | 误差曲线, V 形曲线, 双对数坐标 | courbe d’erreur, courbe en V, en échelle log-log | hata eğrisi, V eğrisi, log-log ölçekte
- Gradientenprüfung, numerischer / berechneter Gradient = gradient check, numerical / computed gradient | comprobación del gradiente, gradiente numérico / calculado | 梯度检验, 数值梯度 / 计算得到的梯度 | vérification du gradient, gradient numérique / calculé | gradyan kontrolü, sayısal / hesaplanan gradyan
- relativer / absoluter Fehler, Schwelle, Erfahrungswert = relative / absolute error, threshold, empirical value | error relativo / absoluto, umbral, valor empírico | 相对 / 绝对误差, 阈值, 经验值 | erreur relative / absolue, seuil, valeur empirique | bağıl / mutlak hata, eşik, deneyim değeri
- Fallstrick, einseitige Steigung, Gleichstand = pitfall, one-sided slope, tie | trampa, pendiente lateral, empate | 陷阱, 单侧斜率, 相等（并列） | piège, pente à gauche / à droite, égalité | tuzak, tek taraflı eğim, eşitlik
- Taschenrechner, Rechenprogramme = calculator, numerical software | calculadora, programas de cálculo | 计算器, 数值软件 | calculatrice, logiciels de calcul | hesap makinesi, hesaplama programları

Nachtrag aus der Übersetzung von Grundlagen 3 (Wahl der Übersetzer, so in den Heften verwendet)
- Knick (als \fb) = kink | punto anguloso | 折点 | point anguleux | köşe noktası
- Etappe (Teilstück eines Wegs) = leg | tramo | 段 | tronçon (« étape » ist die Heft-Stufe) | etap
- Verschiebung b einer affinen Abbildung = shift | desplazamiento | 平移 | translation | öteleme (Verschiebung h auf der Landkarte: displacement | desplazamiento | 位移 | déplacement | yer değiştirme)
- Vereinbarung, Layout-Konvention = convention, layout convention | convención, convención de disposición | 约定, 布局约定 | convention, convention de disposition | uzlaşım, düzen kuralı
- Probe: (Kontrollrechnung) = Check: | Comprobación: | 验算： | Vérification : | Sağlama:
- vollbesetzte Matrix = dense matrix | matriz densa | 稠密矩阵 | matrice pleine | tam dolu matris
- schiefe Schüssel = skewed bowl | cuenco oblicuo | 斜置碗形 | cuvette oblique | eğik çanak
- Klammerung (Reihenfolge der Produkte) = parenthesization | asociación | 结合方式 | parenthésage | parantezleme
- Matrixidentitäten = matrix identities | identidades matriciales | 矩阵恒等式 | identités matricielles | matris özdeşlikleri
- hintereinandergeschaltet (zwei Stufen) = connected in series | conectadas una tras otra | 前后串联 | montés en série | art arda bağlanmış
- Mischform (Layout) = mixed layout | forma mixta | 混合布局 | forme mixte | karma biçim
- Auslöschung beim ersten \fb: zh 相消（灾难性抵消）, tr anlamlı basamak kaybı (yıkıcı sadeleşme); Adjungierte tr eşlenik (adjoint) mit Klammerzusatz beim ersten \fb

### Ergänzt bei Python 1 (en, 11.11.2026)
Nur Englisch (Format Deutsch = en); die Übersetzer der anderen Sprachen ergänzen ihre Wörter hier. Gilt für Python 2 und 3, Linux 1–6 und Cybersecurity 1 genauso. Die Wörter der Szenen (`tools/szenen/prog_teil1.py`, `s.tr`) sind dieselben.
Programm und Rechner
- Rechner, Taschenrechner = computer, calculator; Programm, Anweisung, Arbeitsschritt = program, statement, step; Rezept, Verfahren = recipe, method
- Prozessor, Rechenwerk, Steuerwerk, Prozessorfamilie = processor, arithmetic unit, control unit, processor family; holen/entschlüsseln/ausführen = fetch/decode/execute
- Speicher, Arbeitsspeicher, Speicherplatz 12 = memory, main memory, memory cell 12; Betriebssystem = operating system
- Maschinenbefehl, Maschinencode = machine instruction, machine code; Programmiersprache, Alltagssprache, Grammatik = programming language, everyday language, grammar
- Syntax (Form), Semantik (Bedeutung) = syntax (form), semantics (meaning); Sprachreferenz, Sprachmittel = Python Language Reference, language features
- Quelltext = source code; zerlegen (Quelltext) = split up (into tokens)
Übersetzen und Ausführen
- Compiler, ausführbare Datei = compiler, executable file; übersetzen, Übersetzung (Compiler und CPython) = translate, translation (wie in den Szenen); Übersetzer (der Teil von CPython) = translator; ausführen = run (execute)
- Interpreter, Interpreterschleife = interpreter, interpreter loop; Dolmetscher (Bild) = human interpreter; Dolmetscher-Interpreter = line-by-line interpreter
- „übersetzt“ vs. „interpretiert“ als Eigenschaft einer Sprache = ``compiled'' vs. ``interpreted''
- Bytecode, gedachte Maschine, Phase, Startbefehl (RESUME) = bytecode, virtual machine, phase, start instruction
Einrichten
- Terminal, Eingabeaufforderung, Befehl (im Terminal) = terminal, prompt, command; Ordner, persönlicher Ordner = folder, home folder
- Python install manager (bleibt); Starter (`py`), Installationsprogramm, Standardversion = launcher, installer, default version; System-Python, Paketverwaltung = system Python, package manager; Verwalterrechte = administrator privileges
- Versionsnummer; Haupt-, Unterversion, Fehlerbehebungsnummer = version number; major version, minor version, bugfix number; Fehlerbehebungen, Sicherheitskorrekturen, Sicherheitslücken = bug fixes, security fixes, security vulnerabilities; „wurde eingestellt“ = reached its end of life; „ab Python 3.12“ = ``Python 3.12 or later''
- Oberflächen (englische Namen): Strg = Ctrl; Startsymbol = Start button; Ubuntu „Aktivitäten“ = Activities; „Installierte Apps“ = Installed apps; „App-Ausführungsaliase verwalten“ = Manage app execution aliases; Explorer „Anzeigen › Einblenden › Dateinamenerweiterungen“ = View › Show › File name extensions; VS Code „Datei › Ordner öffnen“ = File › Open Folder (das Deutsche nennt beide Menünamen, das Englische nur den englischen); Benutzername, Rechnername = user name, computer name; Testrechner (des Hefts) = test computers
Werte und Ausdrücke
- interaktiver Modus = interactive mode; Wert, Ausdruck, auswerten = value, expression, evaluate; Ausgabe = output
- Rechenzeichen = operator; Punkt-/Strichrechnung = multiplication and division / addition and subtraction; Potenz, Zehnerpotenz = power, power of ten; „hoch“ = ``to the power of''; runde Klammern = parentheses
- Nachkommastellen, gültige Stellen, Zwischenergebnis = decimal places, significant digits, intermediate result
- Zeichenkette = string; gerade / typografische Anführungszeichen = straight / typographic (curly) quotes; Textverarbeitung = word processor; Leerzeichen, Unterstrich = space, underscore
- Funktion, Funktionsaufruf, Teilprogramm = function, function call, subprogram
Skripte und Fehler
- Editor, Erweiterung (VS Code), Skript, Kommentar = editor, extension, script, comment; Dateiendung/Dateinamenerweiterung = file name extension
- Syntaxfehler, Laufzeitfehler, Logikfehler, Fehlermeldung = syntax error, runtime error, logic error, error message; „ist ein Syntaxfehler“ (Programm) = ``has a syntax error''
- Ausnahme, Traceback = exception, traceback; Kopfzeile, Ortszeile, Markierung = header, location line, marker; Art und Beschreibung (der Ausnahme) = type and description; oberste Ebene = top level
- Satz von Rice = Rice's theorem; Überschlagsrechnung = rough estimate
Alltagsbeispiele
- Heron-Verfahren, Durchgang, Schätzung, Mittelwert, Zahlenstrahl = Heron's method, pass, estimate, mean, number line
- Durchschnittstempo, Tempo/Fahrzeit/Strecke = average speed, speed/travel time/distance; Lotterielos, Einsatz/Gewinn, Anteil = lottery ticket, stake/prize, share; Fliesen zuschneiden = cut tiles to size
- Beträge im englischen Fließtext amerikanisch: „4,49 Euro“ = €4.49, „1000 Euro“ = €1000; in Code-Kommentaren ASCII „1.80 euros“

Regeln aus Python 1 (en), für alle Programmier- und Linux-Hefte
- Code-Blöcke (`python`, `konsole`, `ausgabe`), `\texttt`, `\verb`: Code, Ausgaben, Fehlermeldungen, Pfade (`/home/student/python-kurs/…`), Dateinamen (auch Platzhalter wie `datei.py`), Befehle (`echo Hallo`) und die Titel `[Linux]`, `[hallo.py]` bleiben Zeichen für Zeichen. **Zeichenketten bleiben deutsch** („Zeile 1“, „Mehl in g:“), weil ihre Ausgaben im Heft und in den Szenen stehen; **Kommentare werden übersetzt** (nur ASCII, gleiche Zeilenzahl, keine Kommentarzeile dazu oder weg: Tracebacks nennen Zeilennummern). Beim ersten Vorkommen darf der Fließtext eine kurze Glosse geben: ``Zeile 1'' (German for ``line 1'').
- Prüfskripte (im Scratchpad der Sitzung vom 11.11.2026, bei Bedarf nach `tools/` übernehmen): `C:\Users\info\AppData\Local\Temp\claude\d2b859977628cb1f\c5e68cc8-baf1-4782-9760-867850fb6615\scratchpad\en_prog1\code_vergleich.py <de.tex> <L.tex>` vergleicht die Code-Blöcke Block für Block (Kommentare ausgenommen) und `\texttt`/`\verb`; `…\en_prog1\formeln_b.py <de.tex> <L.tex>` vergleicht die echten Formeln (`$…$` außerhalb von Code).
- `uebersetzung_struktur_check.py` meldet bei Linux-Prompts (`$` in `konsole`/`\verb`) eine Formel-Abweichung als Artefakt, weil es den Text zwischen zwei `$` für eine Formel hält (Python 1: stufen 3/3, stufen_b 18/18, loesungen 15/15). Dann die echten Formeln mit `formeln_b.py` prüfen.
- Sprachgebunden: Python-Meldungen, die das Deutsche für deutsche Leser übersetzt („die Klammer wurde nie geschlossen“), nicht doppeln; „Auf Englisch heißt …“ entfällt im Englischen; Dezimalkomma-Warnungen („Vorsicht, Komma“) bleiben, begründet für Leser, die ein Dezimalkomma gewohnt sind; der Satz „Im Fließtext stehen Zahlen mit Komma“ wird sinngemäß „numbers in running text also use a decimal point“; typografische Anführungszeichen: Code mit „ (U+201E) bleibt, im Text “ ” (en) und „ “ (de) nennen; mehrdeutige Beispielsätze durch englische mit derselben Mehrdeutigkeit ersetzen (``I saw the man with the binoculars.'', ``Photograph the woman with the camera.''), Unsinnssätze durch englische (``The wulp blinks the graffel.'').
- Verweis auf ein Heft, das es in der Sprache noch nicht gibt (Python 1 en → „Linux, Chapter~2“): Der Umwandler lässt ihn als Text ohne Link. Nach der Übersetzung des Ziels das verweisende Heft neu umwandeln, dann entsteht der Link.

### Ergänzt bei Python 2 (en, 11.11.2026)
Nur Englisch (Deutsch = en). Szenenwörter in `tools/szenen/prog_teil2.py` (`s.tr`) sind dieselben.
Objekte, Typen, ganze Zahlen
- Objekt, Typ, Identität, Methode, Attribut = object, type, identity, method, attribute; Art (Aufschrift im Kasten-Bild) = kind; Aufschrift = label; Platz, Platznummer = place, place number (Bild „place no.“); Fach = compartment
- Typentabelle „Typ & englisch & Bedeutung & Beispiele“ = `Type & short for & meaning & examples` (whole number / number with decimal places / sequence of characters); „nach dem englischen binary digit“ = short for binary digit; „englisch not a number“ = short for not a number
- ganze Zahl = integer (whole number); Rechenzeichen (vor der Definition von Operator) = symbol; Operator, Operand = operator, operand; zweistellig/einstellig = binary/unary; Ganzzahldivision, Rest = floor division, remainder; Vielfache = multiples; Rangfolge, Rang = precedence, rank; Potenzturm = tower of powers; Punkt beim Methodenaufruf = dot
Binärsystem
- Stellenwertsystem, Stellenwert, Basis, Ziffer = positional numeral system, place value, base, digit; Stelle (Position) = position, Stellen/Binärstellen (Ziffern) = digits/binary digits; Bitfolge, Bitmuster, Vierergruppe = bit sequence, bit pattern, group of four; Präfix, führende Nullen = prefix, leading zeros; Angabe bei `format` = specifier
- Binärbruch, endlich, „endet (nicht)“ = binary fraction, finite, terminates (does not terminate); Periode = period; Verdopplungsverfahren = doubling method; ganzzahliger Teil, Nachkommaanteil = integer part, fractional part; Zähler, Nenner, gekürzter Bruch = numerator, denominator, fraction in lowest terms; Primfaktor = prime factor; Zweierpotenz = power of two
- **„Komma“ als Trennstelle einer Zahl = point** (decimal point, binary point; „Stellen rechts vom Komma“ = digits to the right of the point; Beweistitel „Komma verschieben“ = Shifting the point; „das Komma gleitet“ = the point floats). Nur wo das Zeichen gemeint ist (Eingabe `2,5`, Tausendertrennung), bleibt comma.
Gleitkommazahlen
- Gleitkommazahl, Gleitkommadarstellung, wissenschaftliche Schreibweise = floating-point number, floating-point representation, scientific notation; Plural im Fließtext „\texttt{float} values“, nie „floats“
- Mantisse = significand (Szene „significand field“); Exponentenfeld, Mantissenfeld, Vorzeichenbit = exponent field, significand field, sign bit; verborgenes Bit = hidden bit; Verschiebung 1023 = bias of the exponent; doppelte Genauigkeit = double precision; Norm IEEE~754 = the IEEE~754 standard; Spielzeugformat = toy format; Abstand (Bild) = spacing
- Darstellungsfehler, kürzeste Darstellung, Etikett (angezeigte kürzeste Zahl) = representation error, shortest representation, label; Rundungsfehler, Rundungsrest = rounding error, rounding residue; Runden zur geraden Mantisse = round half to even (im Satz: to the even significand in a tie); korrekt gerundet = correctly rounded; kompensierte Summation = compensated summation
- Maschinengenauigkeit = machine epsilon; „Einheit der letzten Stelle“ (ulp) = unit in the last place; Absorption, Auslöschung = absorption, cancellation; Überlauf, Unterlauf = overflow, underflow; ungültiges Ergebnis = invalid result; gewöhnliche float = ordinary float values; US-Rechnungshof (Patriot) = U.S. General Accounting Office
Variablen, Vergleiche, Module
- Variable, Zuweisung, binden, neu binden = variable, assignment, bind, rebind; Zustandsdiagramm = state diagram; Etikett (Name an einem Objekt) = tag (anheften/umhängen = attach/move the tag); Kästchen (C-Variable) = (small) box; erweiterte Zuweisung = augmented assignment; Namensregeln, Schlüsselwort = naming rules, keyword; eingebaute Funktion/Namen = built-in function/names; verdeckt = hidden
- Platzhalter in Definitionen: `\textit{ausdruck}` = `\textit{expression}`; `\verb|name = ausdruck|`, `\verb|import modul|` bleiben (Code-Regel)
- Wahrheitswert = truth value; Vergleichsoperator = comparison operator; (relative/absolute) Toleranz = (relative/absolute) tolerance; Identitätsvergleich = identity comparison
- Modul, Modulobjekt, Standardbibliothek = module, module object, standard library; Absatztitel „Erst von Hand“/„Fertig“/„Vergleich“ = First by hand / Ready-made / Comparison; Unterabschnittstitel „…: erst von Hand, dann fertig“ = „…: first by hand, then ready-made“
- Winkelfunktionen, Bogenmaß, Grad = trigonometric functions, radians, degrees; natürlicher/Zehnerlogarithmus = natural/base-10 logarithm; Schalldruck, Pegel = sound pressure, sound level
- Formel-Indizes werden übersetzt: $g_\mathrm{alt}, g_\mathrm{neu}$ = $g_\mathrm{old}, g_\mathrm{new}$; $z_\mathrm{neu}$ = $z_\mathrm{new}$; $p_\mathrm{laut}, p_\mathrm{leise}$ = $p_\mathrm{loud}, p_\mathrm{quiet}$; $t_\mathrm{abs}$ bleibt
Komplexe Zahlen, Text, Ein- und Ausgabe
- Realteil, Imaginärteil, imaginäre Einheit, komplexe Ebene = real part, imaginary part, imaginary unit, complex plane; Betrag, Phase = absolute value (magnitude), phase; konjugiert komplex = complex conjugate; Eulersche Formel, Polarform, Argument = Euler's formula, polar form, argument; Nullpunkt, Mittelpunkt, Drehwinkel = origin, center, angle of rotation; Minutenzeiger, Zifferblatt = minute hand, dial; im/gegen den Uhrzeigersinn = clockwise/counterclockwise; Lösungsformel = quadratic formula; Satz von Vieta = Vieta's formulas
- Zeichenkette verketten / vervielfachen, das Verketten = concatenate / repeat a string, concatenation; leere Zeichenkette = empty string; f-String, Formatangabe = f-string, format specifier; geschweifte Klammern = curly braces; Tausendertrennung = thousands separator; Typumwandlung = type conversion; runden = round; Lauftempo, Temporechner = running pace, pace calculator
- Probe, Vorhersage = check, prediction; Fallunterscheidung = case distinction; Hefte (Schulhefte im Preisbeispiel) = notebooks (nie workbook)
Hilfsmittel (Python 2): `…\scratchpad\en_prog2\formeln_b.py` überspringt jetzt `\%` (kein Kommentar) und `\\[-1pt]` (keine Display-Formel); Hilfsagenten legten neue Wörter fortlaufend in einer gemeinsamen Datei `teile\glossar_neu.md` ab, damit die Hälften einer Datei gleich übersetzen.

### Ergänzt bei Python 3 (en, 11.11.2026)
Nur Englisch (Deutsch = en). Szenenwörter in `tools/szenen/prog_teil3.py` (`s.tr`) sind dieselben. Vollständige Liste der Hilfsagenten: Scratchpad `…\en_prog3\teile\glossar_neu.md`.
Bedingungen und Entscheidungen
- Bedingung = condition; logischer Operator = logical operator; verketteter Vergleich = chained comparison; Größenvergleich = order comparison; Nummer eines Zeichens = code point; Kurzschlussauswertung = short-circuit evaluation; Wahrheitswert von Objekten, „gilt als wahr/falsch“ = truth value of objects, counts as true/false; schützende Bedingung = protecting condition; Teilbedingung = partial condition; De Morgansche Regeln = De Morgan's laws
- bedingte Anweisung = conditional statement; Kopfzeile = header line; Block, Einrückung, einrücken = block, indentation, indent; Tokens „Einrücken“/„Ausrücken“ = ``indent''/``dedent''; Stilleitfaden = style guide; Fortsetzung `...` = continuation prompt; Flussdiagramm, Raute, Kasten = flowchart, diamond, box; Weiche (im Ablauf) = fork; ja/nein (Bild) = yes/no
- Küchenwaage, Rohwert, Stufe (Quantisierung), Unter-/Überlauf = kitchen scale, raw value, step, underflow/overflow; Ganzzahlumwandlung, abrunden = integer conversion, round down; Schaltjahr = leap year; Klausur, Punktzahl = exam, score; Uhrzeiten „8 und 20~Uhr“ = 8:00 and 20:00
Schleifen
- Schleife, Schleifenkopf, Schleifenkörper, Schleifenvariable = loop, loop header, loop body, loop variable; Durchlauf (einer Schleife) = iteration (``pass'' nur für den Durchgang eines Verfahrens); Zähler = counter; Endlosschleife = infinite loop; Gleitkomma-Falle = floating-point trap; „ganzzahlig zählen“ = count with integers; Strg+C, Steuerungstaste = Ctrl+C, Control key
- `range`: Zahlenfolge, Start, Stopp, Schrittweite = sequence of numbers, start, stop, step; „liefert“ = yields; Marke = mark
- abbrechen mit `break` = break out of the loop; überspringen mit `continue` = skip; verschachtelt, äußere/innere Schleife = nested, outer/inner loop; regulär enden, `else` an der Schleife = end regularly, else on a loop; Teiler, Primzahl, zusammengesetzte Zahl = divisor, prime number, composite number
- Akkumulator, Akkumulator-Muster = accumulator, accumulator pattern; Schleifeninvariante = loop invariant; leere Summe/leeres Produkt = empty sum/empty product; Höchsttemperaturen = daily highs
- Tee: Zeitkonstante, Zeitschritt, Zimmer-/Anfangstemperatur = time constant, time step, room/initial temperature; Formel-Indizes $T_\mathrm{neu}, T_\mathrm{alt}$ = $T_\mathrm{new}, T_\mathrm{old}$, $T_\mathrm Z$ bleibt (im Text als room temperature eingeführt)
Näherungsverfahren
- Raten und Prüfen = guess and check; erschöpfende Suche = exhaustive search; Näherung, Toleranz = approximation, tolerance; Schrittverfahren = stepping method (Bild: stepping); Abbruchbedingung = stopping condition; Zahlenschloss = combination lock
- Zwischenwertsatz = intermediate value theorem; stetig = continuous; Vorzeichenwechsel = sign change; Nullstelle = zero (einer Funktion; root nur für die Wurzel); Intervallschachtelung, Teilintervall = nested intervals, subinterval; Bisektion(sverfahren) = bisection (method); Schranke = bound
- Newton-Verfahren = Newton's method; Tangente = tangent line; Startwert = starting value; Konvergenzgeschwindigkeit = speed of convergence; quadratische/lineare Konvergenz = quadratic/linear convergence; gültige/richtige Stellen = significant/correct digits; pendeln, kriechen = oscillate, crawl; Taylorformel mit Restglied = Taylor's formula with remainder
- Intervalle in Formeln: `[1;\,2]` = `[1,\,2]` (Semikolon-Regel)
Kredit
- Ratenkredit, Kredit, Kreditbetrag = installment loan, loan, loan amount; Monatsrate = monthly payment; Monatszins = monthly interest rate (Bild-Achse: monthly rate r in %); Restschuld = remaining balance; Zinseszins = compound interest; Annuitätenformel = annuity formula; effektiver Jahreszins = effective annual interest rate (NICHT APR: die US-APR ist nominal 12r); Tabellenkalkulation, Funktion ZINS = spreadsheet, RATE; Satz von Abel und Ruffini = Abel–Ruffini theorem
- Beträge an Formeln: `$K=20\,000$~euros`, `$\approx386.66$~euros`; im Fließtext €400
Flussdiagramme: Zitierte Programmausgaben in Kästen („fertig“, „in Ordnung“, „zu kalt“, „zu warm“) bleiben deutsch wie die Zeichenketten im Code, mit englischen Anführungszeichen (“fertig”); seit Python 3 in TikZ und Szenen (`prog_teil3.py`, en= angeglichen). Anweisungen in Kästen werden übersetzt (``read temp'', ``print warning'').

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

## Grundlagen 3 („Ableitung, Gradient und Kettenregel“), Übersetzung seit 09.11.2026
Die Abschnitte oben zu Grundlagen 2 (Titel, Korrekturen, Szenenwörter aus ml_teil2.py) und zu Grundlagen 1 (Titel, sprachgebundene Stellen, Bildwörter, Korrekturen) gelten hier nicht; Grundsätze, feste Wendungen und Glossar (samt Blöcken „Ergänzt bei Grundlagen 1“ und „Ergänzt bei Grundlagen 3“) gelten.

Deutsche Quelle (endgültig, Stand 5. November 2026): `Kap3_Ableitung.tex` (Hauptdatei mit Titelblock), `kap3_stufen.tex` (Abschnitte 1–6), `kap3_stufen_b.tex` (Abschnitte 7–11 und Abschluss), `kap3_loesungen.tex`. Ziel je Sprache L: `Kap3_Ableitung_L.tex`, `kap3_stufen_L.tex`, `kap3_stufen_b_L.tex`, `kap3_loesungen_L.tex`. Reihenfolge: en zuerst, zh aus dem fertigen Englisch (mit dem Deutschen daneben), dann es, fr, tr aus dem Deutschen. Teile in den Scratchpad-Ordner schreiben, den der Auftrag nennt; Strukturprüfung mit `python tools/uebersetzung_struktur_check.py <de.tex> <L.tex> <L>` vom Repo-Root.

Titel (verbindlich, aus heft_zu_artikel.py): en „Derivative, Gradient and Chain Rule“, es „Derivada, gradiente y regla de la cadena“, zh „导数、梯度与链式法则“, fr „Dérivée, gradient et règle de dérivation en chaîne“, tr „Türev, Gradyan ve Zincir Kuralı“.
Untertitel (de „Wie eine Zahl auf ihre Eingänge reagiert:\\ von der Tangente bis zum Rückwärtsmodus“): en `How a number responds to its inputs:\\ from the tangent line to reverse mode`; es `Cómo responde un número a sus entradas:\\ de la recta tangente al modo inverso`; zh `一个数如何响应它的输入：\\ 从切线到反向模式`; fr `Comment un nombre réagit à ses entrées :\\ de la tangente au mode inverse`; tr `Bir sayı girdilerine nasıl tepki verir:\\ teğetten ters moda`.
Titelblock-Zeile: en `Mathematical Foundations for Machine Learning, Foundations~3. Version: 5~November 2026`; es `Fundamentos matemáticos para el aprendizaje automático, Fundamentos~3. Versión: 5~de noviembre de 2026`; zh `机器学习数学基础，基础篇~3。版本：2026~年~11~月~5~日`; fr `Fondements mathématiques pour l’apprentissage automatique, Fondements~3. Version : 5~novembre 2026`; tr `Makine Öğrenmesi için Matematiksel Temeller, Temeller~3. Sürüm: 5~Kasım 2026`.

Feste Wendungen in diesem Heft (zusätzlich zur Tabelle oben):
- Kastennamen im Absatz „So arbeitest du mit dem Heft.“ (kap3_stufen.tex Z. 17): „Hintergrund“, „Beweis“, „Herleitung“, „Achtung“ = Background, Proof, Derivation, Caution | Contexto, Demostración, Deducción, Atención | 背景, 证明, 推导, 注意 | Contexte, Preuve, Démonstration, Attention | Arka plan, İspat, Türetme, Dikkat (genau die Wörter der Präambeln); „Was du dafür brauchst“ wie in der Tabelle oben.
- `[Rechenbeispiel]`, `[Rechenbeispiel 1]`, `[Rechenbeispiel 2]` wie in der Tabelle oben; im Fließtext „im Rechenbeispiel“ = in the worked example | en el ejemplo numérico | 在算例中 | dans l’exemple de calcul | sayısal örnekte. (Die Kommentare in praeambel_es/_tr nennen „Ejemplo de cálculo“/„Hesap örneği“; maßgeblich ist die Tabelle, wie in Grundlagen 1 und 2.)
- Abschlusstabelle „Ergebnis & Woher es kommt“ wie in Grundlagen 2: Result & Where it comes from | Resultado & De dónde viene | 结果 & 来源 | Résultat & D’où il vient | Sonuç & Nereden geliyor.
- Tabellenköpfe und -wörter (tab:k3vorwaerts, tab:k3tangente, tab:k3rueckwaerts, tab:k3lokal und die Tabelle der Lösung zu a:k3rueckquadrat gleich): Knoten, Rechnung, Wert, Tangentenwert, Adjungierte, Eingang, Start = node, computation, value, tangent value, adjoint, input, start | nodo, cálculo, valor, valor tangente, adjunto, entrada, inicio | 节点, 计算, 值, 切线值, 伴随值, 输入, 起点 | nœud, calcul, valeur, valeur tangente, adjoint, entrée, départ | düğüm, hesap, değer, teğet değeri, eşlenik, girdi, başlangıç; Operation, lokale Ableitungen, benötigte Werte, keine, die Eingänge, der Eingang, der Ausgang, welcher größer ist = operation, local derivatives, values needed, none, the inputs, the input, the output, which one is larger | operación, derivadas locales, valores necesarios, ninguno, las entradas, la entrada, la salida, cuál es mayor | 运算, 局部导数, 所需的值, 无, 两个输入, 输入, 输出, 哪个更大 | opération, dérivées locales, valeurs nécessaires, aucune, les entrées, l’entrée, la sortie, laquelle est la plus grande | işlem, yerel türevler, gereken değerler, yok, girdiler, girdi, çıktı, hangisinin büyük olduğu.

Verweise im Heft (Formen der Tabelle „Verweise auf andere Hefte“ oben, dazu):
- `Grundlagen~1 und Grundlagen~2` = `Foundations~1 and Foundations~2` | `Fundamentos~1 y Fundamentos~2` | `基础篇~1 和基础篇~2` | `Fondements~1 et Fondements~2` | `Temeller~1 ve Temeller~2` (jeden Namen ausschreiben, sonst kein Link). `Grundlagen~N, Abschnitt~M` steht 37-mal im Heft, auch mit ganzzahligem M (`Abschnitt~3`, `Abschnitt~8`); M bleibt wie es ist.
- `Abschnitt~\ref{k3:…}` = `Section~\ref` | `sección~\ref` (Satzanfang `Sección`) | `第~\ref{…}~节` | `section~\ref` | `Kesim~\ref`. Zwei: `Abschnitte~\ref{a} und~\ref{b}` = `Sections~\ref{a} and~\ref{b}` | `secciones~\ref{a} y~\ref{b}` | `第~\ref{a}~节和第~\ref{b}~节` | `sections~\ref{a} et~\ref{b}` | `Kesim~\ref{a} ve~\ref{b}`. Bereich (kap3_stufen.tex Z. 541): `Abschnitte~\ref{k3:gradient} bis~\ref{k3:hesse}` = `Sections~\ref{…} through~\ref{…}` | `secciones~\ref{…} a~\ref{…}` | `第~\ref{…}~节到第~\ref{…}~节` | `sections~\ref{…} à~\ref{…}` | `Kesim~\ref{…} ile~\ref{…} arasında`.
- „im vorigen / nächsten Unterabschnitt“ (ohne \ref) = previous / next subsection | subsección anterior / siguiente | 上一小节 / 下一小节 | sous-section précédente / suivante | önceki / sonraki alt kesim.
- `Abb.~\ref` = `Fig.~\ref` | `fig.~\ref` (klein wie in Grundlagen 1/2 es) | `图~\ref` | `Fig.~\ref` | `Şekil~\ref`; „Abb.~\ref{fig:k3lupe} links“ = left panel | panel izquierdo | 左图 | panneau de gauche | sol panel. `Tabelle~\ref` = `Table~\ref` | `tabla~\ref` | `表~\ref` | `tableau~\ref` | `Tablo~\ref`. `Aufgabe~\ref` = `Exercise~\ref` | `ejercicio~\ref` | `练习~\ref` | `exercice~\ref` | `Alıştırma~\ref`.
- „das Rechenbeispiel zu Abschnitt~\ref{k3:zwischen}“ / „im Rechenbeispiel zu \eqref{…}“ = the worked example in Section~\ref / for \eqref | el ejemplo numérico de la sección~\ref / de \eqref | 第~\ref{…}~节的算例 / \eqref{…} 处的算例 | l’exemple de calcul de la section~\ref / associé à \eqref | Kesim~\ref{…}'deki sayısal örnek / \eqref{…} ile ilgili sayısal örnek.
- tr-Endungen: an `\eqref` keine Endung hängen, sondern Postpositionen wie in Grundlagen 2 tr (`\eqref{…} uyarınca`, `\eqref{…} bağıntısı`, `\eqref{…} içindeki`). Bei `Kesim~\ref` und `Alıştırma~\ref` richtet sich die Endung nach der letzten Zahl: Abschnitte 1 ableitung, 2 kette, 3 gradient, 4 richtung, 5 jacobi, 6 kettemehr, 7 matrixabl, 8 hesse, 9 graph, 10 ad, 11 numerisch, Unterabschnitte in Reihenfolge (k3:zwischen = 9.1, k3:senkrecht = 4.3); verwiesene Aufgaben a:k3gradient = 9, a:k3linear = 10, a:k3kurve = 22, a:k3taylor = 29, a:k3graphquadrat = 32.

Sprachgebundene Stellen (sinngemäß anpassen, nichts weglassen):
- Semikolon: Das Heft setzt `;` auch ohne Dezimalzahl, wenn ein Eintrag eine Rechnung ist oder die Liste sonst Dezimalzahlen hat: `\diag(2;\,8)`, `\diag(2;\,-4;\,6)`, `\diag(8;\,2)`, `\diag(\ee^0;\,\ee^1;\,\ee^{-1})`, `(8+3;\ 8+12)\T`, `(0;\ \sqrt6)\T`, `(0;\ 3;\ 2{,}000001)\T`, Funktionsargumente `f(1{,}01;\ 2{,}02)`, `\vg(1{,}1;\ 1{,}9)`. en/zh überall Komma (`\diag(2,\,8)`, `(8+3,\ 8+12)\T`, `f(1.01,\ 2.02)`); es/fr/tr wie im Deutschen. Listen mit Komma ohne Dezimalzahl (`(1,\,2)`, `f(1,2)`) bleiben in allen Sprachen.
- `\spur` (kap3_stufen_b.tex Z. 149, 237; kap3_loesungen.tex Z. 226): ersetzen wie in den Grundsätzen (`\operatorname{tr}`, tr `\operatorname{iz}`). Wort „Spur $6$“ (stufen_b Z. 414), „Spur $10$“ (loesungen Z. 267) = trace | traza | 迹 | trace | iz. „Rang“ (stufen_b Z. 444, loesungen Z. 248) steht nur als Wort: rank | rango | 秩 | rang | rank.
- `\text{…}` in Formeln (alle übersetzen): `\text{mit}` (stufen Z. 140, 246, 985; stufen_b Z. 349) = `with` | `con` | `其中` | `avec` | `burada`. `\text{(Summenregel)}` usw. (stufen Z. 195–198) nach dem Glossar. `\text{falls }v(x)\ne0` = `if` | `si` | `若` | `si` | tr `v(x)\ne0\text{ ise}`. `(\text{Summanden mit }h^2,h^3,\dots,h^n)` (stufen Z. 212) = `terms with` | `términos con` | `(\text{含 }h^2,h^3,\dots,h^n\text{ 的项})` | `termes en` | `(h^2,h^3,\dots,h^n\text{ içeren terimler})`. `a\text{ Vorgänger von }b` (stufen_b Z. 691) / `b\text{ Nachfolger von }a` (Z. 733) = `predecessor of` / `successor of` | `predecesor de` / `sucesor de` | `a\text{ 为 }b\text{ 的前驱}` / `b\text{ 为 }a\text{ 的后继}` | `prédécesseur de` / `successeur de` | `a\text{: }b\text{'nin öncülü}` / `b\text{: }a\text{'nın ardılı}`. `\text{bzw.}` (stufen_b Z. 1012) = `\text{and}` und im Satz danach „respectively“ (es `\text{y}` … respectivamente, zh `\text{和}` … 分别, fr `\text{et}` … respectivement, tr `\text{ve}` … sırasıyla). `\text{linear: }`, `\text{quadratisch: }` (loesungen Z. 33) = linear / quadratic | lineal / cuadrática | 线性 / 二次 | linéaire / quadratique | doğrusal / ikinci dereceden. Indizes `\varepsilon_{\mathrm M}`, `\vg_{\mathrm a}`, `\vg_{\mathrm n}` bleiben.
- „gelesen „$f$ nach $g$““ (stufen Z. 334): die übliche Lesart der Sprache: en ``$f$ after $g$''; es «$f$ compuesta con $g$»; zh 读作“$f$ 复合 $g$”; fr « $f$ rond $g$ »; tr “$f$ bileşke $g$”.
- „Das Zeichen $\partial$ ist ein gerundetes d“ (stufen Z. 564): fr « un d rond » (so heißt das Zeichen dort), sonst wörtlich (a rounded d | una d redondeada | 圆体的 d | kıvrık bir d). „liest man „Nabla““ (Z. 614): en ``nabla'' (or ``del''), sonst nabla in den Anführungszeichen der Sprache.
- „e-Funktion“ (stufen Z. 227 Hintergrundtitel und öfter) ist ein deutsches Kurzwort: überall exponential function | función exponencial | 指数函数 | fonction exponentielle | üstel fonksiyon, nie „e-function“.
- „Rechner speichern Kommazahlen als Gleitkommazahlen“ (stufen_b Z. 990): Das Wortspiel hängt am deutschen „Komma“. en „Computers store non-integers as floating-point numbers“; es „los números decimales como números en coma flotante“; zh „把小数存为浮点数“; fr « les nombres à virgule comme nombres à virgule flottante »; tr „ondalıklı sayıları kayan noktalı sayılar olarak“.
- „diese Zahl heißt Maschinengenauigkeit, und Rechenprogramme geben sie unter diesem Namen aus“ (stufen_b Z. 994): Der Satz muss in der Zielsprache stimmen; Programme nennen die Zahl machine epsilon bzw. eps. en „is called machine epsilon, and numerical software reports it under this name“; es, zh, fr, tr: Wort des Glossars, und „unter diesem Namen“ wird „unter dem Namen eps“ (es „con el nombre eps“, zh „以 eps 为名“, fr « sous le nom eps », tr „eps adıyla“).
- „acht Byte je Zahl … $80$ Gigabyte“ (stufen_b Z. 866): fr « huit octets … 80 gigaoctets », tr „sekiz bayt … 80 gigabayt“, zh „每个数 8 字节 … 80 GB“, es „ocho bytes … 80 gigabytes“.
- „11{,}18 Tausend Euro“ (loesungen Z. 123): thousand euros | miles de euros | 千欧元 | milliers d’euros | bin avro, Zahl mit dem Dezimalzeichen der Sprache.
- Code: Grundlagen 3 hat keine Code-Blöcke (`python`, `ausgabe`), kein `\texttt` und kein `\verb` (grep; Grundlagen 1 ebenso). Der Programmname `rechnung_kap3.py` steht nur in Kommentarzeilen und bleibt. Regel für spätere Hefte: Code und Programmausgaben bleiben Zeichen für Zeichen (Python druckt Dezimalpunkte, also auch in es/fr/tr kein Komma in `ausgabe`); Kommentare dürfen übersetzt werden, Zeichenketten nur zusammen mit der im Heft gezeigten Ausgabe; Zeichen außerhalb von ASCII nur in Kommentaren und Zeichenketten.

TikZ-Abbildungen (Koordinaten nie ändern):
- Die Achsenzahlen von pgfplots (`xtick`, `ytick`) setzt die Präambel je Sprache mit Punkt oder Komma; nicht anfassen. Von Hand geschriebene Zahlen dagegen umstellen: stufen Z. 59 `yticklabels={…,$15{,}625$,…}` (en/zh `$15.625$`), Z. 66 Legende `$h=0{,}5$`, Z. 123/127 Titel `$1{,}9$` … `$2{,}01$`, Z. 362–364 `$1{,}01$`, `$4{,}03$`, `$16{,}2409$`, Z. 367 `24\cdot0{,}01=0{,}24`.
- `coordinates {…}`, `domain` und `legend style={at={(axis cs:3e-12,4)}…}` in fig:k3vkurve (stufen_b Z. 1024–1047) bleiben unverändert. Nach dem Bauen prüfen, dass die längeren fr/tr-Legenden keine Messpunkte verdecken.

Bildwörter (ml_teil3.py `s.tr` = TikZ im Heft), de = en | es | zh | fr | tr:
Sekante h = 1: Steigung 19 (TikZ-Legende „Sekante, $h=1$“) = secant h = 1: slope 19 (secant, $h=1$) | secante h = 1: pendiente 19 (secante, $h=1$) | 割线 h = 1：斜率 19（割线，$h=1$） | sécante h = 1 : pente 19 (sécante, $h=1$) | kesen h = 1: eğim 19 (kesen, $h=1$);
Tangente(: Steigung 12) = tangent(: slope 12) | tangente(: pendiente 12) | 切线（：斜率 12） | tangente( : pente 12) | teğet(: eğim 12);
x von 1 bis 3 = x from 1 to 3 | x de 1 a 3 | x 从 1 到 3 | x de 1 à 3 | x: 1 ile 3 arası (TikZ `$x$: $1{,}9$ ile $2{,}1$ arası`);
Stufe 1: Faktor 3 (TikZ „Stufe 1: Faktor $g'(1)=3$“) = stage 1: factor 3 | etapa 1: factor 3 | 第 1 级：因子 3 | étage 1 : facteur 3 | aşama 1: çarpan 3;
zusammen: Δy ≈ … = combined: | en total: | 合计： | au total : | toplam:;
(a) Höhenlinien = (a) contour lines | (a) curvas de nivel | (a) 等高线 | (a) lignes de niveau | (a) eş yükselti eğrileri (falls im Bild zu breit: seviye eğrileri);
(b) Schnitt x₂ = 2 = (b) section x₂ = 2 | (b) corte x₂ = 2 | (b) 截线 x₂ = 2 | (b) coupe x₂ = 2 | (b) kesit x₂ = 2;
Steigung 4 = slope 4 | pendiente 4 | 斜率 4 | pente 4 | eğim 4;
Schrittweite h, Fehler = step size h, error | paso h, error | 步长 h, 误差 | pas h, erreur | adım büyüklüğü h, hata;
Vorwärtsdifferenz(, gemessen), zentrale Differenz(, gemessen) = forward difference(, measured), central difference(, measured) | diferencia progresiva(, medida), diferencia central(, medida) | 前向差分（实测）, 中心差分（实测） | différence avant(, mesurée), différence centrée(, mesurée) | ileri fark(, ölçülen), merkezi fark(, ölçülen);
Abschätzung(en), z. B. „Abschätzung $E_+(h)$“ = estimate(s) | estimación(es) | 估计 | estimation(s) | kestirim(ler).
Farbwörter in Bildunterschriften: rot, orange, blau, grün, grau, schwarz, gestrichelt = red, orange, blue, green, gray, black, dashed | rojo, naranja, azul, verde, gris, negro, discontinua | 红色, 橙色, 蓝色, 绿色, 灰色, 黑色, 虚线 | rouge, orange, bleu, vert, gris, noir, en tirets | kırmızı, turuncu, mavi, yeşil, gri, siyah, kesikli.
Die Rechenbilder ml/k3r… (`_formel` in ml_teil3.py) enthalten kein `\text{…}`; ihre Dezimalzahlen stellt der Export je Sprache um.

Korrekturen am Original (in der deutschen Datei eingetragen, 09.11.2026):
- kap3_stufen.tex Z. 99: Der Begriff \fb{Knick} steht jetzt im Haupttext vor dem Kasten „Rechenbeispiel 2“ (eigener Absatz „Nicht jede Funktion ist überall differenzierbar. …“); im Kasten nur noch „einen Knick“ ohne \fb (vorher nur im zugeklappten Kasten erklärt, aber später sechsmal benutzt).
- kap3_loesungen.tex Z. 356–359 (Aufgabe a:k3differenzen): alle vier Werte e^{±0,1}, e^{±0,01} jetzt mit neun Nachkommastellen (1,105170918; 0,904837418; 1,010050167; 0,990049834), auch in den Brüchen; die align-Umgebung hat deshalb vier Zeilen (D_0 jeweils in eigener Zeile mit `&\quad`). Vorher sechs bzw. sieben Stellen, aus denen die angegebenen 1,001668, 1,005017 und 1,0000167 nicht folgten.
- kap3_stufen_b.tex Z. 852 (Hintergrund zum Rückwärtsmodus, Checkpointing): „… wachsen dann der Speicher und der Faktor, um den die Rechenzeit die einer einfachen Auswertung übersteigt, nur noch logarithmisch …“ (vorher „Speicher und Rechenzeit“; die Rechenzeit selbst wächst mindestens linear).
- kap3_stufen_b.tex Z. 1020 (V-Kurve): „Rechts steigt die Kurve mit der Steigung $1$ … Links fällt sie mit der Steigung $-1$ …“ (vorher „fällt“/„steigt“ vertauscht, widersprüchlich zum Vorzeichen der Steigung).
- kap3_stufen_b.tex Z. 1068 (eq:k3gradnum): Formel endet mit Punkt statt Komma, weil danach ein neuer Satz beginnt.
- kap3_loesungen.tex Z. 156 (a:k3jacobilin b): „Bei einem Schritt um genau diesen Vektor ändert sich dann der erste Ausgang um $4\cdot2-1\cdot(-1)=9$.“ (vorher „… um 9 je Einheit dieser Richtung“, mehrdeutig, weil (2, −1) nicht normiert ist; je Längeneinheit wären es 9/√5).
- Satzspiegel (nur Übersetzungen, sinngleich): kap3_loesungen Z. 33 in fr/tr `\quad` statt `\qquad`, tr `\text{kuadratik: }`; Z. 145 es « por », fr ohne « on a », tr „işler“, damit die Zeile nicht über den Rand ragt; zh `见图~\ref` statt `（图~\ref）` am Zeilenanfang (stufen Z. 770, stufen_b Z. 363); `\pagebreak` vor Kastentiteln am Seitenfuß: zh stufen vor dem Hintergrund „为什么要对路径求和“, tr stufen_b vor dem Beweis „Doğrusal fonksiyonların gradyanları“.
