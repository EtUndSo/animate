---
title: Die Konditionszahl
pfad: Informatik / Machine Learning / Projektion, Eigenwerte und Zerlegungen
order: 6221300
summary: Messdaten sind nie exakt, und ein Rechner rundet bei jedem Schritt.
tags: Konditionszahl
lang: de
---

<span class="anker" id="stufe-12"></span>

:::zweck
Messdaten sind nie exakt, und ein Rechner rundet bei jedem Schritt. Wie stark ändert sich die Lösung eines Gleichungssystems, wenn die rechte Seite ein wenig falsch ist? Dieser Abschnitt zeigt, dass eine einzige Zahl aus den Singulärwerten die Antwort gibt, und was sie für die Normalgleichungen bedeutet.
:::

### Ein empfindliches Gleichungssystem

<span class="anker" id="stufe-12-1"></span>

Das Gleichungssystem

$$x_1+x_2=2,\qquad x_1+1{,}01\,x_2=2{,}01$$

hat die Lösung $\mathbf{x}=(1,\,1)^{\top}$. Ändert man die rechte Seite der zweiten Gleichung um $0{,}01$ auf $2{,}02$, so ergibt die Differenz der Gleichungen $0{,}01\,x_2=0{,}02$, also $x_2=2$ und $x_1=0$. Eine Änderung der Daten in der dritten Stelle verschiebt die Lösung um ihre eigene Größe.

Geometrisch sind die beiden Gleichungen zwei Geraden, die sich im Lösungspunkt schneiden. Hier sind sie fast parallel; sie schneiden sich unter einem Winkel von nur etwa $0{,}29^\circ$. Verschiebt man eine von ihnen ein wenig, wandert der Schnittpunkt weit an der anderen entlang (Abb. [28](#abb-28)). Stehen die Geraden dagegen senkrecht, so wandert er nur so weit, wie man die Gerade verschiebt.

:::abbildung ml/k2kondition 28
Dieselbe Verschiebung der roten Geraden um den Abstand $0{,}2$ (gestrichelt), zweimal. Links schneidet sie die blaue Gerade senkrecht, und der Schnittpunkt wandert um $0{,}2$. Rechts schneiden sich die Geraden unter $8^\circ$, und der Schnittpunkt wandert um $0{,}2/\sin8^\circ\approx1{,}44$. Je flacher der Schnittwinkel, desto empfindlicher reagiert die Lösung auf Änderungen der Daten.
:::

Wie groß ist die Wirkung, gemessen an den Größen selbst? Die rechte Seite $\mathbf{y}=(2;\ 2{,}01)^{\top}$ hat die Länge $\sqrt{4+4{,}0401}\approx2{,}8355$ (Abb. [29](#abb-29)), die Änderung $\Delta\mathbf{y}=(0;\ 0{,}01)^{\top}$ die Länge $0{,}01$. Die rechte Seite ändert sich also relativ um $0{,}01/2{,}8355\approx0{,}35\,\%$. Die Lösung ändert sich um $\Delta\mathbf{x}=(-1,\,1)^{\top}$, relativ um $\lVert\Delta\mathbf{x}\rVert/\lVert\mathbf{x}\rVert=\sqrt2/\sqrt2=100\,\%$. Der relative Fehler wird etwa $284$-fach verstärkt.

:::abbildung ml/k2rnormy 29
Das Längenquadrat der rechten Seite als Skalarprodukt $\mathbf{y}^{\top}\mathbf{y}$; die Länge ist $\sqrt{8{,}0401}\approx2{,}8355$.
:::

⁠**Kurz gesagt:** Schneiden sich die Geraden eines Gleichungssystems fast parallel, so verschieben kleine Änderungen der Daten die Lösung stark.

### Die Konditionszahl

<span class="anker" id="stufe-12-2"></span>

Woher kommt der Faktor? Mit der Singulärwertzerlegung lässt sich die Verstärkung genau abschätzen.

:::definition Definition 12.1 (Konditionszahl)
<span class="anker" id="satz-12-1"></span>

Es sei $\mathbf{A}\in\mathbb{R}^{m\times n}$ mit linear unabhängigen Spalten, also $d_n>0$. Die __Konditionszahl__ von $\mathbf{A}$ ist

<span class="anker" id="gl-12-1"></span>
$$\kappa(\mathbf{A})=\frac{d_1}{d_n}, \tag{12.1}$$

das Verhältnis der größten zur kleinsten Streckung.
:::

Es ist immer $\kappa(\mathbf{A})\ge1$. Eine orthogonale Matrix hat $\kappa=1$, denn alle ihre Singulärwerte sind $1$. Eine Matrix mit großer Konditionszahl heißt schlecht konditioniert.

:::satz Satz 12.2 (Fehlerverstärkung)
<span class="anker" id="satz-12-2"></span>

Es sei $\mathbf{A}\in\mathbb{R}^{n\times n}$ invertierbar, $\mathbf{A}\mathbf{x}=\mathbf{y}$ mit $\mathbf{y}\ne\mathbf{0}$ und $\mathbf{A}(\mathbf{x}+\Delta\mathbf{x})=\mathbf{y}+\Delta\mathbf{y}$. Dann ist

<span class="anker" id="gl-12-2"></span>
$$\frac{\lVert\Delta\mathbf{x}\rVert}{\lVert\mathbf{x}\rVert}\le\kappa(\mathbf{A})\,\frac{\lVert\Delta\mathbf{y}\rVert}{\lVert\mathbf{y}\rVert} . \tag{12.2}$$

Gleichheit tritt ein, wenn $\mathbf{y}$ in Richtung $\mathbf{u}_1$ und $\Delta\mathbf{y}$ in Richtung $\mathbf{u}_n$ zeigt.
:::

:::beweis Fehlerverstärkung
Aus beiden Gleichungen folgt $\mathbf{A}\Delta\mathbf{x}=\Delta\mathbf{y}$. Nach [(9.5)](die-singularwertzerlegung.html#gl-9-5) ist $\lVert\mathbf{y}\rVert=\lVert\mathbf{A}\mathbf{x}\rVert\le d_1\lVert\mathbf{x}\rVert$, also $1/\lVert\mathbf{x}\rVert\le d_1/\lVert\mathbf{y}\rVert$, und $\lVert\Delta\mathbf{y}\rVert=\lVert\mathbf{A}\Delta\mathbf{x}\rVert\ge d_n\lVert\Delta\mathbf{x}\rVert$, also $\lVert\Delta\mathbf{x}\rVert\le\lVert\Delta\mathbf{y}\rVert/d_n$. Multipliziert ergibt das [(12.2)](#gl-12-2). Zeigt $\mathbf{y}$ in Richtung $\mathbf{u}_1$, so ist $\mathbf{x}$ ein Vielfaches von $\mathbf{v}_1$ und die erste Ungleichung eine Gleichung; zeigt $\Delta\mathbf{y}$ in Richtung $\mathbf{u}_n$, so ist $\Delta\mathbf{x}$ ein Vielfaches von $\mathbf{v}_n$ und die zweite eine Gleichung.
:::

Der schlimmste Fall ist also: Die Lösung liegt in der Richtung, die $\mathbf{A}$ am stärksten streckt, sodass $\mathbf{y}$ groß ist im Vergleich zu $\mathbf{x}$, und der Fehler liegt in der Richtung, die $\mathbf{A}$ am schwächsten streckt, sodass das Rückrechnen ihn um $1/d_n$ vergrößert.

⁠**Rechenbeispiel:** $\mathbf{A}=\bigl(\begin{smallmatrix}1&1\\1&1{,}01\end{smallmatrix}\bigr)$ ist symmetrisch mit der Spur $2{,}01$ und der Determinante $0{,}01$. Ihre Eigenwerte sind

$$\lambda_{1,2}=\frac{2{,}01\pm\sqrt{2{,}01^2-0{,}04}}2=\frac{2{,}01\pm\sqrt{4{,}0001}}2\approx\frac{2{,}01\pm2{,}000025}2,$$

also $\lambda_1\approx2{,}005012$ und $\lambda_2\approx0{,}004988$, beide positiv. Nach Abschnitt [9.7](die-singularwertzerlegung.html#stufe-9-7) sind das auch die Singulärwerte, und $\kappa(\mathbf{A})\approx402$. Die beobachtete Verstärkung $284$ liegt darunter. Sie erreicht die Schranke nicht ganz, weil $\Delta\mathbf{y}=(0;\ 0{,}01)^{\top}$ nicht genau in Richtung $\mathbf{u}_2\approx(1,\,-1)^{\top}/\sqrt2$ zeigt. Für $\mathbf{A}=\bigl(\begin{smallmatrix}2&3\\0&2\end{smallmatrix}\bigr)$ ist $\kappa=4/1=4$: Relative Fehler werden höchstens vervierfacht.

⁠**Kurz gesagt:** Die Konditionszahl $\kappa(\mathbf{A})=d_1/d_n$ ist der größte Faktor, um den $\mathbf{A}^{-1}$ einen relativen Fehler der Daten in der Lösung vergrößern kann.

### Konditionszahl und Determinante

<span class="anker" id="stufe-12-3"></span>

Im Hintergrund von [Teil 1](/wissen/informatik/machine-learning/vektoren-und-matrizen/vektoren-und-matrizen.html), Abschnitt 14.6, stand eine Warnung: Eine kleine Determinante heißt nicht, dass eine Matrix beinahe singulär ist. Die Konditionszahl misst, was dort gemeint war.

:::satz Satz 12.3 (Abstand zur nächsten singulären Matrix)
<span class="anker" id="satz-12-3"></span>

Für eine invertierbare Matrix $\mathbf{A}\in\mathbb{R}^{n\times n}$ ist der kleinste Abstand $\lVert\mathbf{A}-\mathbf{B}\rVert_2$ zu einer singulären Matrix $\mathbf{B}$ gleich $d_n$. Relativ zur Größe $\lVert\mathbf{A}\rVert_2=d_1$ ist er

<span class="anker" id="gl-12-3"></span>
$$\min_{\mathbf{B}\ \text{singulär}}\frac{\lVert\mathbf{A}-\mathbf{B}\rVert_2}{\lVert\mathbf{A}\rVert_2}=\frac1{\kappa(\mathbf{A})} . \tag{12.3}$$
:::

:::beweis Abstand
Eine singuläre Matrix hat höchstens den Rang $n-1$. Nach dem Satz von Eckart und Young mit $k=n-1$ ist $\lVert\mathbf{A}-\mathbf{B}\rVert_2\ge d_n$, und die singuläre Matrix $\mathbf{A}_{n-1}$ hat genau den Abstand $d_n$.
:::

Eine große Konditionszahl heißt also: Eine verhältnismäßig kleine Änderung macht die Matrix singulär. Die Determinante misst etwas anderes. Nach Aufgabe [29](die-singularwertzerlegung.html#aufg-29) ist $|\det\mathbf{A}|=d_1\cdots d_n$, das Produkt aller Streckungen; es hängt von der Größe der Matrix ab. Die Konditionszahl ist ein Verhältnis und ändert sich nicht, wenn man $\mathbf{A}$ mit einer Zahl multipliziert: $\kappa(c\mathbf{A})=\kappa(\mathbf{A})$ für $c\ne0$. Sie misst nur, wie flach die Ellipse ist, in die $\mathbf{A}$ den Einheitskreis verwandelt.

⁠**Rechenbeispiel:** Die beiden Matrizen aus [Teil 1](/wissen/informatik/machine-learning/vektoren-und-matrizen/vektoren-und-matrizen.html), Abschnitt 14.6: $0{,}1\cdot\mathbf{I}_{10}$ hat die Determinante $10^{-10}$, aber alle Singulärwerte $0{,}1$ und $\kappa=1$; sie ist so gut konditioniert wie möglich. $\operatorname{diag}(1000;\ 0{,}001)$ hat die Determinante $1$, aber $\kappa=1000/0{,}001=10^6$. Für $\mathbf{A}=\bigl(\begin{smallmatrix}1&1\\1&1{,}01\end{smallmatrix}\bigr)$ ist der Abstand zur nächsten singulären Matrix $d_2\approx0{,}005$: Ändert man Einträge um wenige Tausendstel, wird sie singulär. Die singuläre Matrix $\bigl(\begin{smallmatrix}1&1\\1&1\end{smallmatrix}\bigr)$ hat den Abstand $\lVert\bigl(\begin{smallmatrix}0&0\\0&0{,}01\end{smallmatrix}\bigr)\rVert_2=0{,}01$, etwas mehr als das Minimum.

⁠**Kurz gesagt:** $1/\kappa(\mathbf{A})$ ist der relative Abstand zur nächsten singulären Matrix; die Determinante sagt darüber nichts, weil sie von der Größe der Matrix abhängt.

### Normalgleichungen quadrieren die Konditionszahl

<span class="anker" id="stufe-12-4"></span>

Die beste Näherungslösung kann man über die Normalgleichungen $\mathbf{A}^{\top}\mathbf{A}\hat{\mathbf{x}}=\mathbf{A}^{\top}\mathbf{y}$ berechnen oder über die QR-Zerlegung, $\mathbf{R}\hat{\mathbf{x}}=\mathbf{Q}^{\top}\mathbf{y}$. Mathematisch liefern beide dasselbe. Mit gerundeten Zahlen nicht, und der Grund ist die Konditionszahl.

:::satz Satz 12.4 (Konditionszahl der Gram-Matrix)
<span class="anker" id="satz-12-4"></span>

Hat $\mathbf{A}$ linear unabhängige Spalten, so ist

<span class="anker" id="gl-12-4"></span>
$$\kappa(\mathbf{A}^{\top}\mathbf{A})=\kappa(\mathbf{A})^2 . \tag{12.4}$$

Für die QR-Zerlegung $\mathbf{A}=\mathbf{Q}\mathbf{R}$ dagegen ist $\kappa(\mathbf{R})=\kappa(\mathbf{A})$.
:::

:::beweis Gram-Matrix
$\mathbf{A}^{\top}\mathbf{A}$ ist symmetrisch und positiv definit mit den Eigenwerten $d_j^2$; nach Abschnitt [9.7](die-singularwertzerlegung.html#stufe-9-7) sind das auch ihre Singulärwerte, und ihr Verhältnis ist $d_1^2/d_n^2$. Wegen $\mathbf{Q}^{\top}\mathbf{Q}=\mathbf{I}$ ist $\mathbf{R}^{\top}\mathbf{R}=\mathbf{R}^{\top}\mathbf{Q}^{\top}\mathbf{Q}\mathbf{R}=\mathbf{A}^{\top}\mathbf{A}$; $\mathbf{R}$ hat also dieselben Singulärwerte wie $\mathbf{A}$.
:::

⁠**Rechenbeispiel:** Die Wohnungsmatrix aus Abschnitt [3.7](die-beste-naherungslosung.html#stufe-3-7), Fläche und Zimmerzahl, hat die Singulärwerte $d_1\approx135{,}02$ und $d_2\approx0{,}848$, also $\kappa(\mathbf{A})\approx159{,}3$ und $\kappa(\mathbf{A}^{\top}\mathbf{A})\approx25\,367$. Zwei Ursachen machen $\kappa(\mathbf{A})$ groß. Erstens die Einheiten: Die Flächen sind Zahlen um $65$, die Zimmerzahlen um $2{,}5$. Misst man die Fläche in Einheiten von $10\,\mathrm m^2$, so sinkt die Konditionszahl auf etwa $18{,}5$. Zweitens zeigen die beiden Spalten fast in dieselbe Richtung, sie schließen nur etwa $8{,}9^\circ$ ein. Auch wenn man beide Spalten auf die Länge $1$ bringt, bleibt deshalb $\kappa\approx12{,}8$. Das Umrechnen der Einheiten ändert die angepassten Werte $\hat{\mathbf{y}}$ nicht: Teilt man eine Spalte durch $10$, so wird das zugehörige Gewicht $10$-mal so groß, und die Produkte bleiben gleich.

⁠**Kurz gesagt:** Die Normalgleichungen arbeiten mit $\kappa(\mathbf{A})^2$, die QR-Zerlegung mit $\kappa(\mathbf{A})$; gut gewählte Einheiten senken die Konditionszahl.

:::hintergrund Was der Rechner mit der Konditionszahl macht
Ein Rechner speichert Zahlen üblicherweise mit etwa $16$ gültigen Dezimalstellen und rundet nach jeder Rechenoperation. Ein gutes Verfahren liefert die exakte Lösung einer Aufgabe, deren Daten nur in der Größenordnung dieser Rundung verändert sind; solche Verfahren heißen rückwärtsstabil. Nach [(12.2)](#gl-12-2) hat das Ergebnis dann einen relativen Fehler von höchstens etwa $\kappa\cdot10^{-16}$: Man verliert ungefähr $\log_{10}\kappa$ der $16$ Stellen.

Der Weg über die QR-Zerlegung (und über die Singulärwertzerlegung) ist rückwärtsstabil; bei kleinem Residuum wächst sein Fehler etwa wie $\kappa(\mathbf{A})$. Der Weg über die Normalgleichungen ist es nicht: Er arbeitet mit der Matrix $\mathbf{A}^{\top}\mathbf{A}$, und sein Fehler wächst immer wie $\kappa(\mathbf{A})^2$, auch wenn das Residuum klein ist. Bei $\kappa(\mathbf{A})=10^6$ verliert man auf diesem Weg etwa $12$ der $16$ Stellen, mit QR etwa $6$. Bei den Wohnungen mit $\kappa(\mathbf{A})^2\approx2{,}5\cdot10^4$ ist das noch harmlos; bei großen Datensätzen mit fast abhängigen Merkmalen nicht. Deshalb rechnen gute Programme die beste Näherungslösung über QR oder die Singulärwertzerlegung aus, nicht über die Normalgleichungen, obwohl diese die Theorie am kürzesten beschreiben.
:::

:::aufgabe Aufgabe 36 ★ Konditionszahlen ablesen
<span class="anker" id="aufg-36"></span>

Bestimme die Konditionszahl von

<ol class="al">

<li>

$\operatorname{diag}(2;\ 0{,}5)$ und $\operatorname{diag}(-3;\ 3)$;

</li>

<li>

der Drehmatrix um $30^\circ$;

</li>

<li>

$5\mathbf{A}$ für $\mathbf{A}=\bigl(\begin{smallmatrix}2&3\\0&2\end{smallmatrix}\bigr)$. Vergleiche die Determinanten von $\mathbf{A}$ und $5\mathbf{A}$.

</li>

</ol>

:::loesung
(a) $\operatorname{diag}(2;\,0{,}5)$ hat die Singulärwerte $2$ und $0{,}5$, also $\kappa=4$. $\operatorname{diag}(-3;\,3)$ hat nach Abschnitt [9.7](die-singularwertzerlegung.html#stufe-9-7) die Singulärwerte $3$ und $3$, also $\kappa=1$, obwohl die Eigenwerte verschiedene Vorzeichen haben.

(b) Eine Drehmatrix ist orthogonal, alle Singulärwerte sind $1$: $\kappa=1$.

(c) $5\mathbf{A}$ hat die Singulärwerte $20$ und $5$, also wieder $\kappa=4$. Die Determinante wächst dagegen von $4$ auf $\det(5\mathbf{A})=25\cdot4=100$.
:::
:::

:::aufgabe Aufgabe 37 ★★ Große Determinante, schlechte Kondition
<span class="anker" id="aufg-37"></span>

Es sei $\mathbf{A}=\bigl(\begin{smallmatrix}10&7\\7&5\end{smallmatrix}\bigr)$.

<ol class="al">

<li>

Berechne $\det\mathbf{A}$ und $\mathbf{A}^{-1}$. Löse $\mathbf{A}\mathbf{x}=(17,\,12)^{\top}$ und $\mathbf{A}\mathbf{x}=(17;\ 12{,}1)^{\top}$.

</li>

<li>

Berechne die relativen Änderungen von $\mathbf{y}$ und $\mathbf{x}$ und ihr Verhältnis.

</li>

<li>

Berechne $\kappa(\mathbf{A})$ und prüfe [(12.2)](#gl-12-2). Wie weit ist $\mathbf{A}$ von der nächsten singulären Matrix entfernt?

</li>

</ol>

:::loesung
(a) $\det\mathbf{A}=50-49=1$ und $\mathbf{A}^{-1}=\bigl(\begin{smallmatrix}5&-7\\-7&10\end{smallmatrix}\bigr)$. Damit ist $\mathbf{A}^{-1}(17,\,12)^{\top}=(85-84,\ -119+120)^{\top}=(1,\,1)^{\top}$ und $\mathbf{A}^{-1}(17;\ 12{,}1)^{\top}=(85-84{,}7;\ -119+121)^{\top}=(0{,}3;\ 2)^{\top}$.

(b) $\lVert\Delta\mathbf{y}\rVert/\lVert\mathbf{y}\rVert=0{,}1/\sqrt{433}\approx0{,}1/20{,}809\approx0{,}48\,\%$. $\Delta\mathbf{x}=(-0{,}7;\ 1)^{\top}$, also $\lVert\Delta\mathbf{x}\rVert/\lVert\mathbf{x}\rVert=\sqrt{1{,}49}/\sqrt2\approx1{,}2207/1{,}4142\approx86{,}3\,\%$. Das Verhältnis ist etwa $180$.

(c) $\mathbf{A}$ ist symmetrisch mit Spur $15$ und Determinante $1$, also $\lambda=\tfrac{15\pm\sqrt{221}}2\approx14{,}933$ und $0{,}0670$, beide positiv. Nach Abschnitt [9.7](die-singularwertzerlegung.html#stufe-9-7) sind das die Singulärwerte, und $\kappa(\mathbf{A})\approx14{,}933/0{,}0670\approx223$. Die Schranke [(12.2)](#gl-12-2) ist erfüllt: $86{,}3\,\%\le223\cdot0{,}48\,\%\approx107\,\%$. Der Abstand zur nächsten singulären Matrix ist $d_2\approx0{,}067$, relativ $1/223$. Die Determinante $1$ verrät davon nichts.
:::
:::

:::aufgabe Aufgabe 38 ★★★ Rechenregeln für die Konditionszahl
<span class="anker" id="aufg-38"></span>

Es sei $\mathbf{A}\in\mathbb{R}^{n\times n}$ invertierbar und $\mathbf{Q}$ orthogonal. Zeige:

<ol class="al">

<li>

$\kappa(\mathbf{Q}\mathbf{A})=\kappa(\mathbf{A})$ und $\kappa(\mathbf{A}^{-1})=\kappa(\mathbf{A})$;

</li>

<li>

für alle Eigenwerte $\lambda$ und $\mu$ von $\mathbf{A}$ ist $|\lambda|/|\mu|\le\kappa(\mathbf{A})$;

</li>

<li>

für symmetrisches $\mathbf{A}$ ist $\kappa(\mathbf{A})=|\lambda|_{\max}/|\lambda|_{\min}$, das Verhältnis des betragsgrößten zum betragskleinsten Eigenwert.

</li>

</ol>

:::loesung
(a) Nach Aufgabe [29](die-singularwertzerlegung.html#aufg-29) hat $\mathbf{Q}\mathbf{A}$ dieselben Singulärwerte wie $\mathbf{A}$, also dieselbe Konditionszahl. Aus $\mathbf{A}=\mathbf{U}\mathbf{D}\mathbf{V}^{\top}$ folgt $\mathbf{A}^{-1}=\mathbf{V}\mathbf{D}^{-1}\mathbf{U}^{\top}$, eine Singulärwertzerlegung mit den Singulärwerten $1/d_j$. Der größte ist $1/d_n$, der kleinste $1/d_1$, also $\kappa(\mathbf{A}^{-1})=\tfrac{1/d_n}{1/d_1}=\tfrac{d_1}{d_n}=\kappa(\mathbf{A})$.

(b) Für einen Eigenvektor $\mathbf{v}$ zu $\lambda$ gilt nach [(9.5)](die-singularwertzerlegung.html#gl-9-5) $d_n\lVert\mathbf{v}\rVert\le\lVert\mathbf{A}\mathbf{v}\rVert=|\lambda|\,\lVert\mathbf{v}\rVert\le d_1\lVert\mathbf{v}\rVert$, also $d_n\le|\lambda|\le d_1$; für komplexe Eigenvektoren gilt das ebenso, wie in Abschnitt [9.8](die-singularwertzerlegung.html#stufe-9-8) gezeigt. Dasselbe gilt für $\mu$. Also ist $|\lambda|/|\mu|\le d_1/d_n$.

(c) Für symmetrisches $\mathbf{A}$ sind die Singulärwerte nach Abschnitt [9.7](die-singularwertzerlegung.html#stufe-9-7) die Beträge $|\lambda_i|$. Der größte Singulärwert ist also $|\lambda|_{\max}$, der kleinste $|\lambda|_{\min}$.
:::
:::
