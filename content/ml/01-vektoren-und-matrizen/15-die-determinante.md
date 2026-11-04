---
title: Die Determinante
pfad: Informatik / Machine Learning / Vektoren und Matrizen
order: 6211500
summary: Eine lineare Abbildung verformt das Gitter der Ebene, und dabei werden Flächen größer oder kleiner.
tags: Determinante, Orientierung, Laplace-Entwicklung
lang: de
---

<span class="anker" id="stufe-14"></span>

:::zweck
Eine lineare Abbildung verformt das Gitter der Ebene, und dabei werden Flächen größer oder kleiner. Dieser Abschnitt bestimmt den Faktor, um den sie sich ändern. Dieser Faktor ist eine einzige Zahl, die Determinante, und an ihr erkennt man auch, ob eine Matrix invertierbar ist.
:::

### Die Determinante einer $2\times2$-Matrix

<span class="anker" id="stufe-14-1"></span>

Das Einheitsquadrat hat die Fläche $1$. Eine Matrix $\mathbf{A}$ bildet es auf das Parallelogramm ab, das ihre beiden Spalten aufspannen (Unterabschnitt [8.3](lineare-abbildungen.html#stufe-8-3)). Wie groß ist dessen Fläche? Abbildung [14](#abb-14) zeigt es für $\mathbf{A}=\bigl(\begin{smallmatrix}3&1\\1&2\end{smallmatrix}\bigr)$.

:::abbildung ml/k1det 14
Links das Einheitsquadrat mit der Fläche $1$, rechts sein Bild unter $\mathbf{A}=\bigl(\begin{smallmatrix}3&1\\1&2\end{smallmatrix}\bigr)$: das Parallelogramm aus den Spalten $\mathbf{a}_1$ und $\mathbf{a}_2$. Es hat die Fläche $5=3\cdot2-1\cdot1$. Gestrichelt das umschließende Rechteck, aus dem sich die Fläche berechnen lässt.
:::

:::herleitung Die Fläche des Parallelogramms
Die Spalten seien $\mathbf{a}_1=(a,\,c)^{\top}$ und $\mathbf{a}_2=(b,\,d)^{\top}$ mit lauter positiven Zahlen, und $\mathbf{a}_2$ liege links oberhalb von $\mathbf{a}_1$ wie in Abb. [14](#abb-14). Das Parallelogramm mit den Ecken $\mathbf{0}$, $\mathbf{a}_1$, $\mathbf{a}_1+\mathbf{a}_2$, $\mathbf{a}_2$ passt in das Rechteck mit den Seiten $a+b$ und $c+d$. Um es übrig zu lassen, schneidet man aus dem Rechteck zwei Dreiecke mit den Katheten $a$ und $c$ heraus, zwei Dreiecke mit den Katheten $b$ und $d$ und zwei Rechtecke mit den Seiten $b$ und $c$:

$$(a+b)(c+d)-2\cdot\tfrac12ac-2\cdot\tfrac12bd-2\,bc=ac+ad+bc+bd-ac-bd-2bc=ad-bc .$$

Für $\mathbf{A}=\bigl(\begin{smallmatrix}3&1\\1&2\end{smallmatrix}\bigr)$: $4\cdot3-3-2-2=5$.
:::

:::definition Definition 14.1 (Determinante einer $2\times2$-Matrix)
<span class="anker" id="satz-14-1"></span>

Die __Determinante__ der Matrix $\mathbf{A}=\bigl(\begin{smallmatrix}a&b\\c&d\end{smallmatrix}\bigr)$ ist die Zahl

<span class="anker" id="gl-14-1"></span>
$$\det\mathbf{A}=ad-bc . \tag{14.1}$$
:::

Ihr Betrag ist die Fläche des Parallelogramms, das die Spalten aufspannen, also der Faktor, um den $\mathbf{A}$ die Fläche des Einheitsquadrats ändert. Es ist dieselbe Zahl, die in der Inversen [(11.2)](einheitsmatrix-und-inverse.html#gl-11-2) im Nenner steht.

⁠**Rechenbeispiel:** $\det\bigl(\begin{smallmatrix}3&1\\1&2\end{smallmatrix}\bigr)=6-1=5$, $\det\bigl(\begin{smallmatrix}2&1\\1&1\end{smallmatrix}\bigr)=2-1=1$, $\det\operatorname{diag}(2;\,0{,}5)=1$ und $\det\bigl(\begin{smallmatrix}1&2\\2&4\end{smallmatrix}\bigr)=0$. Die Streckung verändert die Form des Quadrats, aber nicht seine Fläche: Was sie in die Breite zieht, nimmt sie in der Höhe weg.

⁠**Kurz gesagt:** Die Determinante $ad-bc$ einer $2\times2$-Matrix ist dem Betrag nach der Faktor, um den die Abbildung die Fläche des Einheitsquadrats ändert.

### Das Vorzeichen der Determinante

<span class="anker" id="stufe-14-2"></span>

Eine Fläche ist nie negativ, die Determinante kann es sein. Das Vorzeichen trägt eine zusätzliche Information: ob die Abbildung die Ebene spiegelt.

Im Einheitsquadrat liegt $\mathbf{e}_2$ von $\mathbf{e}_1$ aus gegen den Uhrzeigersinn. Bleibt das bei den Bildern so, liegt also $\mathbf{a}_2$ von $\mathbf{a}_1$ aus ebenfalls gegen den Uhrzeigersinn, so ist $\det\mathbf{A}>0$. Liegt $\mathbf{a}_2$ im Uhrzeigersinn von $\mathbf{a}_1$, ist die Ebene gespiegelt worden, und $\det\mathbf{A}<0$. Diese Eigenschaft heißt __Orientierung__: Eine positive Determinante erhält die Orientierung, eine negative kehrt sie um.

⁠**Rechenbeispiel:** Die Spiegelung an der $x_1$-Achse, $\operatorname{diag}(1;\,-1)$, hat die Determinante $-1$: Die Fläche bleibt gleich, die Orientierung kehrt sich um. Vertauscht man die Spalten einer Matrix, wechselt die Determinante ihr Vorzeichen: $\det\bigl(\begin{smallmatrix}1&3\\2&1\end{smallmatrix}\bigr)=1-6=-5$. Die Drehung um $90^\circ$ hat $\det=0\cdot0-(-1)\cdot1=1$, die Scherung $\det=1\cdot1-1\cdot0=1$, das Plattdrücken $\operatorname{diag}(1;\,0)$ die Determinante $0$.

⁠**Kurz gesagt:** Der Betrag der Determinante ist der Flächenfaktor, ihr Vorzeichen sagt, ob die Abbildung spiegelt.

### Der Flächenfaktor gilt für jede Figur

<span class="anker" id="stufe-14-3"></span>

Bisher ging es um das Einheitsquadrat. Eine lineare Abbildung behandelt aber jede Stelle der Ebene gleich, und deshalb ändert sie die Fläche jeder Figur um denselben Faktor.

:::satz Satz 14.2 (Flächenfaktor)
<span class="anker" id="satz-14-2"></span>

Bildet $\mathbf{A}\in\mathbb{R}^{2\times2}$ eine Figur der Fläche $F$ ab, so hat das Bild die Fläche $|\det\mathbf{A}|\cdot F$.
:::

:::herleitung Flächenfaktor
Man legt ein feines Gitter aus kleinen Quadraten der Seitenlänge $h$ über die Figur. Ein Quadrat mit der Ecke $\mathbf{q}$ hat die Ecken $\mathbf{q}$, $\mathbf{q}+h\mathbf{e}_1$, $\mathbf{q}+h\mathbf{e}_1+h\mathbf{e}_2$ und $\mathbf{q}+h\mathbf{e}_2$. Sein Bild hat die Ecken $\mathbf{A}\mathbf{q}$, $\mathbf{A}\mathbf{q}+h\mathbf{a}_1$, $\mathbf{A}\mathbf{q}+h\mathbf{a}_1+h\mathbf{a}_2$ und $\mathbf{A}\mathbf{q}+h\mathbf{a}_2$: Es ist das Parallelogramm aus $h\mathbf{a}_1$ und $h\mathbf{a}_2$, verschoben nach $\mathbf{A}\mathbf{q}$. Seine Fläche ist $h^2\,|\det\mathbf{A}|$, unabhängig davon, wo das Quadrat lag. Jedes kleine Quadrat wird also um denselben Faktor $|\det\mathbf{A}|$ größer oder kleiner. Die Figur besteht näherungsweise aus solchen Quadraten, und je feiner das Gitter, desto genauer. Deshalb gilt der Faktor für die ganze Figur.
:::

⁠**Rechenbeispiel:** Der Kreis mit dem Radius $1$ hat die Fläche $\pi$. Die Streckung $\operatorname{diag}(3;\,2)$ macht daraus eine Ellipse mit den Halbachsen $3$ und $2$. Deren Fläche ist $\pi\cdot3\cdot2=6\pi$, also genau $|\det\mathbf{A}|=6$-mal die Kreisfläche. Das Dreieck mit den Ecken $\mathbf{0}$, $\mathbf{e}_1$, $\mathbf{e}_2$ hat die Fläche $\tfrac12$; unter $\bigl(\begin{smallmatrix}3&1\\1&2\end{smallmatrix}\bigr)$ wird es zum Dreieck mit den Ecken $\mathbf{0}$, $(3,1)^{\top}$, $(1,2)^{\top}$ und der Fläche $\tfrac52$.

⁠**Kurz gesagt:** Eine lineare Abbildung ändert die Fläche jeder Figur um denselben Faktor $|\det\mathbf{A}|$, weil sie jedes kleine Kästchen des Gitters gleich behandelt.

### Determinanten größerer Matrizen

<span class="anker" id="stufe-14-4"></span>

Im Raum wird aus dem Einheitswürfel der Spat, den die drei Spalten der Matrix aufspannen, ein schräg verzogener Quader. Sein Volumen ist der Faktor, um den die Abbildung Volumina ändert. Auch für größere Matrizen gibt es eine solche Zahl. Man berechnet sie, indem man sie auf Determinanten kleinerer Matrizen zurückführt.

:::definition Definition 14.3 (Determinante)
<span class="anker" id="satz-14-3"></span>

Für $\mathbf{A}\in\mathbb{R}^{1\times1}$ ist $\det\mathbf{A}=a_{11}$. Für $\mathbf{A}\in\mathbb{R}^{n\times n}$ mit $n\ge2$ ist

<span class="anker" id="gl-14-2"></span>
$$\det\mathbf{A}=\sum_{j=1}^n(-1)^{1+j}\,a_{1j}\,\det\mathbf{A}_{1j} , \tag{14.2}$$

wobei $\mathbf{A}_{1j}$ die $(n-1)\times(n-1)$-Matrix ist, die aus $\mathbf{A}$ durch Streichen der ersten Zeile und der Spalte $j$ entsteht. Diese Rechenvorschrift heißt __Laplace-Entwicklung__ nach der ersten Zeile.
:::

Für $n=2$ ergibt [(14.2)](#gl-14-2) wieder $a_{11}a_{22}-a_{12}a_{21}$. Man darf ebenso nach jeder anderen Zeile oder Spalte entwickeln, mit dem Vorzeichen $(-1)^{i+j}$ für den Eintrag $a_{ij}$; das Ergebnis ist immer dasselbe. Für $n=3$ ist $|\det\mathbf{A}|$ das Volumen des Spats aus den drei Spalten, und das Vorzeichen sagt, ob die Spalten in derselben Drehrichtung angeordnet sind wie $\mathbf{e}_1,\mathbf{e}_2,\mathbf{e}_3$ (Rechte-Hand-Regel) oder gespiegelt.

⁠**Rechenbeispiel:** Für die Koeffizientenmatrix aus Unterabschnitt [12.3](lineare-gleichungssysteme.html#stufe-12-3) ist

$$\det\begin{pmatrix}1&2&1\\2&1&1\\1&1&2\end{pmatrix}=1\cdot\det\begin{pmatrix}1&1\\1&2\end{pmatrix}-2\cdot\det\begin{pmatrix}2&1\\1&2\end{pmatrix}+1\cdot\det\begin{pmatrix}2&1\\1&1\end{pmatrix}=1\cdot1-2\cdot3+1\cdot1=-4 .$$

Für eine obere Dreiecksmatrix, unter deren Diagonale nur Nullen stehen, entwickelt man immer wieder nach der ersten Spalte und erhält das Produkt der Diagonaleinträge, etwa $\det\Bigl(\begin{smallmatrix}2&1&3\\0&3&1\\0&0&4\end{smallmatrix}\Bigr)=2\cdot3\cdot4=24$.

⁠**Kurz gesagt:** Die Determinante einer $n\times n$-Matrix wird mit der Laplace-Entwicklung auf kleinere Determinanten zurückgeführt; ihr Betrag ist der Faktor, um den die Abbildung Volumina ändert.

### Rechenregeln für Determinanten

<span class="anker" id="stufe-14-5"></span>

Die wichtigste Regel folgt direkt aus der Anschauung. Führt man zwei Abbildungen hintereinander aus, so ändert die erste das Volumen um ihren Faktor und die zweite das Ergebnis noch einmal um ihren. Die Faktoren multiplizieren sich.

:::satz Satz 14.4 (Rechenregeln der Determinante)
<span class="anker" id="satz-14-4"></span>

Für $\mathbf{A},\mathbf{B}\in\mathbb{R}^{n\times n}$ und eine Zahl $c$ gilt:

<ol class="rm">

<li>

$\det(\mathbf{A}\mathbf{B})=\det\mathbf{A}\cdot\det\mathbf{B}$;

</li>

<li>

$\det\mathbf{A}^{\top}=\det\mathbf{A}$;

</li>

<li>

$\det\mathbf{A}^{-1}=1/\det\mathbf{A}$, wenn $\mathbf{A}$ invertierbar ist;

</li>

<li>

$\det(c\,\mathbf{A})=c^n\det\mathbf{A}$;

</li>

<li>

Addiert man ein Vielfaches einer Zeile zu einer anderen, ändert sich die Determinante nicht; vertauscht man zwei Zeilen, wechselt sie das Vorzeichen; multipliziert man eine Zeile mit $c$, wird sie mit $c$ multipliziert.

</li>

</ol>
:::

Regel (iii) folgt aus (i) mit $\mathbf{A}\mathbf{A}^{-1}=\mathbf{I}$ und $\det\mathbf{I}=1$. Regel (iv) sagt: Streckt man alle $n$ Kanten des Einheitswürfels um $c$, wächst sein Volumen um $c^n$. Regel (v) macht das Gauß-Verfahren zum praktischen Weg, Determinanten zu berechnen: Man bringt die Matrix auf Zeilenstufenform, merkt sich die Zahl der Vertauschungen und multipliziert die Diagonaleinträge.

⁠**Rechenbeispiel 1:** Mit $\det\bigl(\begin{smallmatrix}2&1\\1&1\end{smallmatrix}\bigr)=1$ und $\det\bigl(\begin{smallmatrix}3&1\\1&2\end{smallmatrix}\bigr)=5$ muss das Produkt $\bigl(\begin{smallmatrix}7&4\\4&3\end{smallmatrix}\bigr)$ die Determinante $5$ haben: $21-16=5$.

⁠**Rechenbeispiel 2:** Im Gauß-Verfahren aus Unterabschnitt [12.3](lineare-gleichungssysteme.html#stufe-12-3) wurde die Koeffizientenmatrix mit Additionen von Vielfachen und einer Vertauschung auf die Stufenform mit der Diagonale $1$, $-1$, $-4$ gebracht. Also ist ihre Determinante $(-1)\cdot\bigl(1\cdot(-1)\cdot(-4)\bigr)=-4$, wie mit der Laplace-Entwicklung.

⁠**Kurz gesagt:** Die Determinante eines Produkts ist das Produkt der Determinanten, weil sich die Volumenfaktoren hintereinander multiplizieren; praktisch berechnet man sie mit dem Gauß-Verfahren.

:::hintergrund Warum man Determinanten nicht mit der Laplace-Entwicklung berechnet
Die Laplace-Entwicklung einer $n\times n$-Matrix ruft $n$ Determinanten der Größe $n-1$ auf, jede von ihnen $n-1$ der Größe $n-2$ und so weiter. Ausgeschrieben entstehen $n!$ Produkte. Für $n=20$ sind das mehr als $2\cdot10^{18}$, für einen Rechner unbezahlbar. Das Gauß-Verfahren braucht dagegen nur etwa $\tfrac23n^3$ Grundrechenarten, für $n=20$ also wenige Tausend. Die Laplace-Entwicklung ist deshalb eine Definition und ein Werkzeug für kleine Matrizen und für Herleitungen, kein Rechenverfahren.
:::

### Determinante und Invertierbarkeit

<span class="anker" id="stufe-14-6"></span>

Ist die Determinante null, so wird das Einheitsquadrat zu einer Fläche ohne Inhalt, also zu einer Strecke oder einem Punkt. Die Abbildung drückt die Ebene platt, und was plattgedrückt ist, lässt sich nicht wiederherstellen.

:::satz Satz 14.5 (Determinante und Invertierbarkeit)
<span class="anker" id="satz-14-5"></span>

Eine quadratische Matrix $\mathbf{A}$ ist genau dann invertierbar, wenn $\det\mathbf{A}\ne0$ ist.
:::

:::beweis Determinante und Invertierbarkeit
Ist $\mathbf{A}$ invertierbar, so ist nach Regel (i) $\det\mathbf{A}\cdot\det\mathbf{A}^{-1}=\det\mathbf{I}=1$, also $\det\mathbf{A}\ne0$. Ist umgekehrt $\det\mathbf{A}\ne0$, so bringt man $\mathbf{A}$ mit dem Gauß-Verfahren auf Zeilenstufenform. Nach Regel (v) ändert sich die Determinante dabei höchstens um Faktoren ungleich null, die Determinante der Stufenform ist also ebenfalls nicht null. Sie ist das Produkt ihrer Diagonaleinträge, also ist keiner von ihnen null, und es gibt $n$ Stufen. Damit ist $\operatorname{rang}\mathbf{A}=n$, und nach dem Satz in Unterabschnitt [13.5](unabhangigkeit-basis-und-rang.html#stufe-13-5) ist $\mathbf{A}$ invertierbar.
:::

Zusammen mit dem Satz aus Unterabschnitt [13.5](unabhangigkeit-basis-und-rang.html#stufe-13-5) sind für eine quadratische Matrix also gleichwertig: $\det\mathbf{A}\ne0$, $\mathbf{A}$ invertierbar, $\operatorname{rang}\mathbf{A}=n$, $\ker\mathbf{A}=\{\mathbf{0}\}$, Spalten linear unabhängig.

⁠**Rechenbeispiel:** Die Matrix $\mathbf K$ aus Unterabschnitt [13.4](unabhangigkeit-basis-und-rang.html#stufe-13-4) hat $\det\mathbf K=1\cdot(2-1)-0+1\cdot(0-1)=0$, passend zu $\operatorname{rang}\mathbf K=2$. Die Koeffizientenmatrix aus dem Gauß-Beispiel hat $\det=-4\ne0$ und ist invertierbar; deshalb hatte das System genau eine Lösung.

⁠**Kurz gesagt:** Eine quadratische Matrix ist genau dann invertierbar, wenn ihre Determinante nicht null ist, also wenn sie den Raum nicht plattdrückt.

:::hintergrund Eine kleine Determinante heißt nicht „fast nicht invertierbar“
Man könnte meinen, eine Matrix mit sehr kleiner Determinante sei beinahe singulär. Das stimmt nicht. Die Matrix $0{,}1\,\mathbf{I}_{10}$ hat die Determinante $0{,}1^{10}=10^{-10}$, aber sie ist bestens invertierbar: Ihre Inverse ist $10\,\mathbf{I}_{10}$, und sie macht nichts weiter, als alle Längen auf ein Zehntel zu verkürzen. Die winzige Determinante kommt nur daher, dass sich der Faktor $0{,}1$ in zehn Richtungen multipliziert. Umgekehrt hat $\operatorname{diag}(1000;\,0{,}001)$ die Determinante $1$, obwohl sie die Ebene in einer Richtung fast plattdrückt. Die Determinante misst das Volumen, und das Volumen hängt vom Maßstab ab. Ob eine Matrix „beinahe“ Information vernichtet, sieht man an ihr nicht zuverlässig.
:::

:::aufgabe Aufgabe 34 ★ Determinanten rechnen
<span class="anker" id="aufg-34"></span>

<ol class="al">

<li>

Berechne die Determinanten von $\bigl(\begin{smallmatrix}2&4\\1&2\end{smallmatrix}\bigr)$ und $\Bigl(\begin{smallmatrix}1&2&0\\3&1&2\\0&1&1\end{smallmatrix}\Bigr)$. Welche der beiden Matrizen ist invertierbar?

</li>

<li>

Welche Fläche hat das Dreieck mit den Ecken $(0,\,0)$, $(3,\,1)$ und $(1,\,2)$?

</li>

<li>

Welches Volumen hat der Spat aus den Vektoren $(1,\,0,\,0)^{\top}$, $(1,\,2,\,0)^{\top}$ und $(0,\,1,\,3)^{\top}$?

</li>

</ol>

:::loesung
(a) $\det\bigl(\begin{smallmatrix}2&4\\1&2\end{smallmatrix}\bigr)=4-4=0$: nicht invertierbar, die zweite Spalte ist das Doppelte der ersten. Für die $3\times3$-Matrix nach der ersten Zeile entwickelt:

$$1\cdot\det\begin{pmatrix}1&2\\1&1\end{pmatrix}-2\cdot\det\begin{pmatrix}3&2\\0&1\end{pmatrix}+0=1\cdot(1-2)-2\cdot3=-7 .$$

Sie ist invertierbar.

(b) Das Dreieck ist die Hälfte des Parallelogramms aus $(3,1)^{\top}$ und $(1,2)^{\top}$ mit der Fläche $|\det\bigl(\begin{smallmatrix}3&1\\1&2\end{smallmatrix}\bigr)|=5$, hat also die Fläche $2{,}5$. Ebenso folgt es aus dem Flächenfaktor: Das Dreieck aus $\mathbf{0}$, $\mathbf{e}_1$, $\mathbf{e}_2$ mit der Fläche $\tfrac12$ wird auf dieses Dreieck abgebildet.

(c) Die Vektoren als Spalten ergeben $\Bigl(\begin{smallmatrix}1&1&0\\0&2&1\\0&0&3\end{smallmatrix}\Bigr)$, eine obere Dreiecksmatrix mit der Determinante $1\cdot2\cdot3=6$. Das Volumen ist $6$.
:::
:::

:::aufgabe Aufgabe 35 ★★ Rechenregeln nachprüfen
<span class="anker" id="aufg-35"></span>

<ol class="al">

<li>

Prüfe $\det(\mathbf{C}\mathbf{D})=\det\mathbf{C}\cdot\det\mathbf{D}$ für $\mathbf{C}=\bigl(\begin{smallmatrix}1&2\\3&4\end{smallmatrix}\bigr)$ und $\mathbf{D}=\bigl(\begin{smallmatrix}0&1\\1&1\end{smallmatrix}\bigr)$ und berechne $\det(3\,\mathbf{C})$.

</li>

<li>

Zeige, dass jede Drehmatrix $\mathbf R_\alpha$ die Determinante $1$ hat. Was bedeutet das geometrisch?

</li>

<li>

Begründe ohne Rechnung, warum eine Matrix mit zwei gleichen Spalten die Determinante $0$ hat.

</li>

</ol>

:::loesung
(a) $\det\mathbf{C}=4-6=-2$, $\det\mathbf{D}=0-1=-1$ und $\mathbf{C}\mathbf{D}=\bigl(\begin{smallmatrix}2&3\\4&7\end{smallmatrix}\bigr)$ mit $\det=14-12=2=(-2)\cdot(-1)$. Ferner $3\mathbf{C}=\bigl(\begin{smallmatrix}3&6\\9&12\end{smallmatrix}\bigr)$ mit $\det=36-54=-18=3^2\cdot(-2)$, wie Regel (iv) mit $n=2$ sagt.

(b) $\det\mathbf R_\alpha=\cos\alpha\cdot\cos\alpha-(-\sin\alpha)\cdot\sin\alpha=\cos^2\alpha+\sin^2\alpha=1$. Eine Drehung ändert keine Fläche und spiegelt nicht.

(c) Zwei gleiche Spalten sind linear abhängig. Das Parallelogramm oder der Spat, den die Spalten aufspannen, ist flach und hat den Inhalt null. Dasselbe folgt aus Regel (v), übertragen auf Spalten mit $\det\mathbf{A}^{\top}=\det\mathbf{A}$: Vertauscht man die beiden gleichen Spalten, bleibt die Matrix dieselbe, aber die Determinante müsste ihr Vorzeichen wechseln. Also ist $\det\mathbf{A}=-\det\mathbf{A}$ und damit $\det\mathbf{A}=0$.
:::
:::
