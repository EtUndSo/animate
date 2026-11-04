---
title: Lineare Gleichungssysteme
pfad: Informatik / Machine Learning / Vektoren und Matrizen
order: 6211300
summary: Bisher war der Eingang x gegeben und der Ausgang Ax gesucht.
tags: lineares Gleichungssystem, Koeffizientenmatrix, rechte Seite, Lösung, erweiterte Koeffizientenmatrix, Gauß-Verfahren, Zeilenstufenform, homogen
lang: de
---

<span class="anker" id="stufe-12"></span>

:::zweck
Bisher war der Eingang $\mathbf{x}$ gegeben und der Ausgang $\mathbf{A}\mathbf{x}$ gesucht. Dieser Abschnitt stellt die umgekehrte Frage: Welcher Eingang liefert einen vorgegebenen Ausgang? Das ist ein lineares Gleichungssystem. Er zeigt, wie man es löst und wann es keine, genau eine oder unendlich viele Lösungen hat.
:::

### Gleichungssysteme in Matrixform

<span class="anker" id="stufe-12-1"></span>

Aus der Schule kennt man Aufgaben wie: Zwei Zahlen $x_1$ und $x_2$ erfüllen $2x_1+x_2=5$ und $x_1+x_2=3$; wie heißen sie? Die linken Seiten sind die Komponenten eines Matrix-Vektor-Produkts. Die Aufgabe fragt also: Welcher Vektor $\mathbf{x}$ wird von der Matrix $\bigl(\begin{smallmatrix}2&1\\1&1\end{smallmatrix}\bigr)$ auf $(5,\,3)^{\top}$ abgebildet?

:::definition Definition 12.1 (Lineares Gleichungssystem)
<span class="anker" id="satz-12-1"></span>

Für eine Matrix $\mathbf{A}\in\mathbb{R}^{m\times n}$ und einen Vektor $\mathbf{y}\in\mathbb{R}^m$ heißt

<span class="anker" id="gl-12-1"></span>
$$\mathbf{A}\mathbf{x}=\mathbf{y} \tag{12.1}$$

ein __lineares Gleichungssystem__ mit $m$ Gleichungen und den $n$ Unbekannten $x_1,\dots,x_n$. Die Matrix $\mathbf{A}$ heißt __Koeffizientenmatrix__, der Vektor $\mathbf{y}$ die __rechte Seite__. Jeder Vektor $\mathbf{x}\in\mathbb{R}^n$, der [(12.1)](#gl-12-1) erfüllt, heißt eine __Lösung__.
:::

Ausgeschrieben steht in Zeile $i$ die Gleichung $a_{i1}x_1+\dots+a_{in}x_n=y_i$.

⁠**Rechenbeispiel:** Das System

$$\begin{pmatrix}2&1\\1&1\end{pmatrix}\begin{pmatrix}x_1\\x_2\end{pmatrix}=\begin{pmatrix}5\\3\end{pmatrix}$$

hat die Lösung $\mathbf{x}=(2,\,1)^{\top}$: $2\cdot2+1=5$ und $2+1=3$. Die Koeffizientenmatrix ist aus Unterabschnitt [11.2](einheitsmatrix-und-inverse.html#stufe-11-2) bekannt, mit der Inversen $\bigl(\begin{smallmatrix}1&-1\\-1&2\end{smallmatrix}\bigr)$. Multipliziert man das System von links mit ihr, steht die Lösung sofort da: $\mathbf{x}=\mathbf{A}^{-1}\mathbf{y}=(5-3,\ -5+6)^{\top}=(2,\,1)^{\top}$.

⁠**Kurz gesagt:** Ein lineares Gleichungssystem $\mathbf{A}\mathbf{x}=\mathbf{y}$ fragt, welcher Eingang $\mathbf{x}$ den Ausgang $\mathbf{y}$ liefert.

### Zeilenbild und Spaltenbild

<span class="anker" id="stufe-12-2"></span>

Wie beim Matrix-Vektor-Produkt gibt es zwei Arten, ein Gleichungssystem zu lesen.

**Zeilenbild.** Jede Gleichung für sich beschreibt eine Menge von Punkten. Bei zwei Unbekannten ist $2x_1+x_2=5$ eine Gerade in der Ebene, ebenso $x_1+x_2=3$. Eine Lösung muss beide Gleichungen erfüllen, also auf beiden Geraden liegen: Sie ist ihr Schnittpunkt (Abb. [12](#abb-12), links). Bei drei Unbekannten ist jede Gleichung eine Ebene im Raum.

**Spaltenbild.** Nach der Spaltensicht [(7.3)](das-matrix-vektor-produkt.html#gl-7-3) ist $\mathbf{A}\mathbf{x}=x_1\mathbf{a}_1+\dots+x_n\mathbf{a}_n$. Die Gleichung fragt also: Mit welchen Koeffizienten ergibt die Linearkombination der Spalten die rechte Seite? Im Beispiel: $x_1\,(2,\,1)^{\top}+x_2\,(1,\,1)^{\top}=(5,\,3)^{\top}$, gelöst von $x_1=2$ und $x_2=1$. Das ist genau das Bild rechts in Abb. [8](das-matrix-vektor-produkt.html#abb-8).

:::abbildung ml/k1lgs 12
Das Zeilenbild dreier Gleichungssysteme mit zwei Unbekannten. Jede Gleichung ist eine Gerade, eine Lösung liegt auf allen Geraden. (a) Die Geraden schneiden sich in einem Punkt. (b) Die Geraden sind parallel und haben keinen gemeinsamen Punkt. (c) Beide Gleichungen beschreiben dieselbe Gerade, und jeder ihrer Punkte ist eine Lösung.
:::

Das Spaltenbild beantwortet sofort, wann es überhaupt eine Lösung gibt. Die Vektoren $\mathbf{A}\mathbf{x}$ bilden den Spaltenraum (Unterabschnitt [7.4](das-matrix-vektor-produkt.html#stufe-7-4)).

:::satz Satz 12.2 (Lösbarkeit)
<span class="anker" id="satz-12-2"></span>

Das System $\mathbf{A}\mathbf{x}=\mathbf{y}$ hat genau dann eine Lösung, wenn $\mathbf{y}$ im Spaltenraum von $\mathbf{A}$ liegt.
:::

⁠**Rechenbeispiel:** Das System $\bigl(\begin{smallmatrix}1&2\\2&4\end{smallmatrix}\bigr)\mathbf{x}=\mathbf{y}$ ist für $\mathbf{y}=(3,\,6)^{\top}$ lösbar, etwa mit $\mathbf{x}=(1,\,1)^{\top}$, aber für $\mathbf{y}=(1,\,1)^{\top}$ nicht: Der Spaltenraum ist nach Unterabschnitt [7.4](das-matrix-vektor-produkt.html#stufe-7-4) nur die Gerade in Richtung $(1,\,2)^{\top}$.

⁠**Kurz gesagt:** Im Zeilenbild ist eine Lösung ein gemeinsamer Punkt aller Gleichungen, im Spaltenbild die Wahl der Koeffizienten, mit der die Spalten die rechte Seite ergeben.

### Das Gauß-Verfahren

<span class="anker" id="stufe-12-3"></span>

Bei zwei Unbekannten findet man die Lösung durch Hinsehen. Bei drei oder mehr braucht man ein Verfahren, das immer funktioniert. Die Idee ist dieselbe wie in der Schule: Man zieht ein Vielfaches einer Gleichung von einer anderen ab, sodass eine Unbekannte verschwindet. Das wiederholt man, bis die letzte Gleichung nur noch eine Unbekannte enthält.

Man schreibt dafür nur die Zahlen auf: die Koeffizientenmatrix und, durch einen Strich getrennt, die rechte Seite. Diese Tabelle heißt die __erweiterte Koeffizientenmatrix__ $(\mathbf{A}\,|\,\mathbf{y})$.

:::definition Definition 12.3 (Gauß-Verfahren)
<span class="anker" id="satz-12-3"></span>

Das __Gauß-Verfahren__ formt die erweiterte Koeffizientenmatrix mit drei Zeilenumformungen um:

<ol>

<li>

ein Vielfaches einer Zeile zu einer anderen Zeile addieren;

</li>

<li>

zwei Zeilen vertauschen;

</li>

<li>

eine Zeile mit einer Zahl ungleich null multiplizieren.

</li>

</ol>

Ziel ist die __Zeilenstufenform__: In jeder Zeile steht vor dem ersten Eintrag ungleich null mindestens eine Null mehr als in der Zeile darüber. Danach bestimmt man die Unbekannten von unten nach oben (Rückwärtseinsetzen).
:::

:::satz Satz 12.4 (Zeilenumformungen ändern die Lösungen nicht)
<span class="anker" id="satz-12-4"></span>

Ein System und das durch Zeilenumformungen daraus entstandene System haben dieselben Lösungen.
:::

:::beweis Zeilenumformungen
Jede Lösung des alten Systems erfüllt auch die neuen Gleichungen, denn diese sind Summen und Vielfache der alten. Jede der drei Umformungen lässt sich aber auch rückgängig machen: das Vielfache wieder abziehen, die Zeilen zurücktauschen, durch die Zahl teilen. Also erfüllt umgekehrt jede Lösung des neuen Systems auch das alte.
:::

⁠**Rechenbeispiel:** Das System

$$\begin{aligned} x_1+2x_2+x_3&=8\\ 2x_1+x_2+x_3&=7\\ x_1+x_2+2x_3&=9 \end{aligned} \qquad\text{hat die erweiterte Koeffizientenmatrix}\qquad \left(\begin{array}{ccc|c}1&2&1&8\\2&1&1&7\\1&1&2&9\end{array}\right).$$

Zieht man die erste Zeile zweimal von der zweiten und einmal von der dritten ab, so verschwindet $x_1$ aus beiden. Vertauscht man danach die neue zweite und dritte Zeile und zieht die neue zweite dreimal von der dritten ab, verschwindet auch $x_2$ aus der letzten Zeile:

$$\left(\begin{array}{ccc|c}1&2&1&8\\0&-3&-1&-9\\0&-1&1&1\end{array}\right) \;\longrightarrow\; \left(\begin{array}{ccc|c}1&2&1&8\\0&-1&1&1\\0&-3&-1&-9\end{array}\right) \;\longrightarrow\; \left(\begin{array}{ccc|c}1&2&1&8\\0&-1&1&1\\0&0&-4&-12\end{array}\right).$$

Von unten nach oben: $-4x_3=-12$, also $x_3=3$; dann $-x_2+3=1$, also $x_2=2$; dann $x_1+4+3=8$, also $x_1=1$. Die Lösung ist $\mathbf{x}=(1,\,2,\,3)^{\top}$, und Einsetzen in alle drei Gleichungen bestätigt sie.

⁠**Kurz gesagt:** Das Gauß-Verfahren eliminiert die Unbekannten Schritt für Schritt durch Zeilenumformungen, die die Lösungen nicht ändern, und setzt dann von unten nach oben ein.

:::hintergrund Warum man zum Lösen keine Inverse berechnet
Ist $\mathbf{A}$ invertierbar, so ist die Lösung $\mathbf{x}=\mathbf{A}^{-1}\mathbf{y}$. Das ist für Überlegungen nützlich, als Rechenweg aber ungünstig. Das Gauß-Verfahren braucht für ein System mit $n$ Gleichungen und $n$ Unbekannten etwa $\tfrac23n^3$ Grundrechenarten; die Inverse zu berechnen kostet etwa $2n^3$, dreimal so viel, und danach kommt noch das Produkt $\mathbf{A}^{-1}\mathbf{y}$ hinzu. Außerdem rechnet ein Rechner mit endlich vielen Stellen. Die Inverse lässt sich dann nur gerundet darstellen, und das direkte Eliminieren liefert in der Regel genauere Ergebnisse. Die Inverse ist deshalb vor allem ein Werkzeug zum Denken und Herleiten, nicht zum Rechnen.
:::

### Keine, eine oder unendlich viele Lösungen

<span class="anker" id="stufe-12-4"></span>

Zwei Geraden in der Ebene schneiden sich in einem Punkt, sind parallel oder fallen zusammen (Abb. [12](#abb-12)). Genau zwei Schnittpunkte gibt es nicht. Dasselbe gilt für jedes lineare Gleichungssystem, gleichgültig wie groß.

:::satz Satz 12.5 (Anzahl der Lösungen)
<span class="anker" id="satz-12-5"></span>

Ein lineares Gleichungssystem hat entweder keine Lösung, genau eine Lösung oder unendlich viele Lösungen.
:::

:::beweis Anzahl der Lösungen
Es genügt zu zeigen: Hat das System zwei verschiedene Lösungen $\mathbf{x}\ne\mathbf{x}'$, so hat es unendlich viele. Für jede Zahl $t$ ist

$$\mathbf{A}\bigl(\mathbf{x}+t\,(\mathbf{x}'-\mathbf{x})\bigr)=\mathbf{A}\mathbf{x}+t\,(\mathbf{A}\mathbf{x}'-\mathbf{A}\mathbf{x})=\mathbf{y}+t\,(\mathbf{y}-\mathbf{y})=\mathbf{y} ,$$

also ist jeder Punkt $\mathbf{x}+t\,(\mathbf{x}'-\mathbf{x})$ der Geraden durch $\mathbf{x}$ und $\mathbf{x}'$ eine Lösung, und verschiedene $t$ geben verschiedene Punkte.
:::

Das System $\mathbf{A}\mathbf{x}=\mathbf{0}$ mit der rechten Seite null heißt __homogen__. Es hat immer die Lösung $\mathbf{x}=\mathbf{0}$. Kennt man eine einzige Lösung $\mathbf{x}_{\mathrm s}$ des Systems $\mathbf{A}\mathbf{x}=\mathbf{y}$, so erhält man alle anderen, indem man die Lösungen des homogenen Systems dazuaddiert: $\mathbf{A}\mathbf{x}=\mathbf{y}$ gilt genau dann, wenn $\mathbf{A}(\mathbf{x}-\mathbf{x}_{\mathrm s})=\mathbf{y}-\mathbf{y}=\mathbf{0}$ ist.

⁠**Rechenbeispiel:** Die drei Systeme in Abb. [12](#abb-12):

<ol class="al">

<li>

$2x_1+x_2=5$, $x_1+x_2=3$: genau eine Lösung $(2,\,1)^{\top}$.

</li>

<li>

$x_1+x_2=3$, $x_1+x_2=1$: keine Lösung, denn dieselbe Summe kann nicht zugleich $3$ und $1$ sein.

</li>

<li>

$x_1+x_2=3$, $2x_1+2x_2=6$: Die zweite Gleichung ist das Doppelte der ersten. Eine Lösung ist $\mathbf{x}_{\mathrm s}=(3,\,0)^{\top}$, und das homogene System $x_1+x_2=0$ wird von allen Vielfachen von $(-1,\,1)^{\top}$ gelöst. Alle Lösungen sind also $\mathbf{x}=(3,\,0)^{\top}+t\,(-1,\,1)^{\top}$ mit beliebigem $t$.

</li>

</ol>

⁠**Kurz gesagt:** Ein lineares Gleichungssystem hat keine, genau eine oder unendlich viele Lösungen; alle Lösungen sind eine Lösung plus die Lösungen des homogenen Systems.

### Mehr Gleichungen als Unbekannte

<span class="anker" id="stufe-12-5"></span>

Bei Daten ist die Lage oft ungleich verteilt. Angenommen, man sucht Gewichte $w_1$ für die Fläche und $w_2$ für die Zimmer, sodass die gewichtete Summe bei drei Wohnungen genau den tatsächlichen Preis trifft. Das sind drei Gleichungen für zwei Unbekannte.

:::definition Definition 12.6 (Überbestimmt, unterbestimmt)
<span class="anker" id="satz-12-6"></span>

Ein lineares Gleichungssystem mit mehr Gleichungen als Unbekannten ($m>n$) heißt __überbestimmt__, eines mit weniger Gleichungen als Unbekannten ($m<n$) __unterbestimmt__.
:::

Ein überbestimmtes System hat meist keine Lösung: Schon zwei Gleichungen legen zwei Unbekannte fest, und die dritte Gleichung müsste zufällig ebenfalls stimmen. Im Spaltenbild: Der Spaltenraum von $n$ Spalten im $\mathbb{R}^m$ ist für $n<m$ nur ein kleiner Teil des $\mathbb{R}^m$, und die rechte Seite liegt fast nie darin. Ein unterbestimmtes System hat dagegen, wenn es überhaupt lösbar ist, unendlich viele Lösungen: In der Zeilenstufenform bleibt mindestens eine Unbekannte ohne eigene Stufe, und sie ist frei wählbar.

⁠**Rechenbeispiel:** Für die Wohnungen 1 bis 3 mit den Preisen $200$, $130$ und $290$ Tausend Euro lautet das System

$$60\,w_1+2\,w_2=200,\qquad 40\,w_1+w_2=130,\qquad 90\,w_1+4\,w_2=290 .$$

Aus den ersten beiden Gleichungen folgt $w_1=3$ und $w_2=10$: Zieht man die zweite zweimal von der ersten ab, bleibt $-20\,w_1=-60$. In die dritte eingesetzt, ergibt das aber $270+40=310\ne290$. Das System hat keine Lösung. Kein Paar von Gewichten trifft alle drei Preise genau. Was man in einem solchen Fall stattdessen sucht, ist eine eigene Frage.

⁠**Kurz gesagt:** Ein überbestimmtes System hat mehr Gleichungen als Unbekannte und ist meist unlösbar, ein unterbestimmtes hat weniger und, wenn lösbar, unendlich viele Lösungen.

:::aufgabe Aufgabe 28 ★★ Das Gauß-Verfahren
<span class="anker" id="aufg-28"></span>

Löse mit dem Gauß-Verfahren und mache die Probe:

$$x_1+x_2+x_3=6,\qquad 2x_1+3x_2+x_3=11,\qquad x_1-x_2+2x_3=5 .$$

:::loesung
Die erweiterte Koeffizientenmatrix ist $\Bigl(\begin{smallmatrix}1&1&1&|&6\\2&3&1&|&11\\1&-1&2&|&5\end{smallmatrix}\Bigr)$. Zieht man die erste Zeile zweimal von der zweiten und einmal von der dritten ab, entstehen die Zeilen $(0,\,1,\,-1\,|\,-1)$ und $(0,\,-2,\,1\,|\,-1)$. Addiert man dann die neue zweite Zeile zweimal zur dritten, wird diese zu $(0,\,0,\,-1\,|\,-3)$. Die Stufenform lautet

$$x_1+x_2+x_3=6,\qquad x_2-x_3=-1,\qquad -x_3=-3 .$$

Von unten: $x_3=3$, $x_2=-1+3=2$, $x_1=6-2-3=1$. Probe: $1+2+3=6$, $2+6+3=11$, $1-2+6=5$. Die Lösung ist $\mathbf{x}=(1,\,2,\,3)^{\top}$.
:::
:::

:::aufgabe Aufgabe 29 ★★ Wie viele Lösungen?
<span class="anker" id="aufg-29"></span>

Bestimme für jedes System die Lösungsmenge und zeichne das Zeilenbild:

<ol class="al">

<li>

$x_1+2x_2=3$, $2x_1+4x_2=6$;

</li>

<li>

$x_1+2x_2=3$, $2x_1+4x_2=5$;

</li>

<li>

$x_1+2x_2=3$, $x_1-x_2=0$.

</li>

</ol>

:::loesung
(a) Die zweite Gleichung ist das Doppelte der ersten; beide beschreiben dieselbe Gerade. Unendlich viele Lösungen: Mit $x_2=t$ ist $x_1=3-2t$, also $\mathbf{x}=(3,\,0)^{\top}+t\,(-2,\,1)^{\top}$.

(b) Verdoppelt man die erste Gleichung, erhält man $2x_1+4x_2=6$, im Widerspruch zu $2x_1+4x_2=5$. Die Geraden sind parallel; es gibt keine Lösung.

(c) Aus der zweiten Gleichung ist $x_1=x_2$, in die erste eingesetzt $3x_2=3$. Genau eine Lösung: $\mathbf{x}=(1,\,1)^{\top}$, der Schnittpunkt zweier nicht paralleler Geraden.
:::
:::

:::aufgabe Aufgabe 30 ★★ Gewichte, die passen
<span class="anker" id="aufg-30"></span>

Nimm zu dem überbestimmten System aus Unterabschnitt [12.5](#stufe-12-5) noch Wohnung 4 mit dem Preis $240$ Tausend Euro hinzu.

<ol class="al">

<li>

Welche der vier Wohnungen werden mit $w_1=3$, $w_2=10$ genau getroffen?

</li>

<li>

Schreibe das System mit vier Gleichungen als $\mathbf{A}\mathbf{w}=\mathbf{y}$. Welche Formate haben $\mathbf{A}$, $\mathbf{w}$ und $\mathbf{y}$? Was bedeutet „keine Lösung“ im Spaltenbild?

</li>

</ol>

:::loesung
(a) Mit $w_1=3$, $w_2=10$: Wohnung 1: $180+20=200$ (getroffen), Wohnung 2: $120+10=130$ (getroffen), Wohnung 3: $270+40=310$ statt $290$ (nicht getroffen), Wohnung 4: $210+30=240$ (getroffen). Drei der vier Preise stimmen, aber nicht alle.

(b) $\mathbf{A}=\Biggl(\begin{smallmatrix}60&2\\40&1\\90&4\\70&3\end{smallmatrix}\Biggr)\in\mathbb{R}^{4\times2}$, $\mathbf{w}\in\mathbb{R}^2$, $\mathbf{y}=(200,\,130,\,290,\,240)^{\top}\in\mathbb{R}^4$. Der Spaltenraum von $\mathbf{A}$ besteht aus allen Kombinationen $w_1\mathbf{a}_1+w_2\mathbf{a}_2$ der Flächenspalte und der Zimmerspalte; er ist eine Ebene durch den Nullpunkt im $\mathbb{R}^4$. „Keine Lösung“ heißt: Der Preisvektor $\mathbf{y}$ liegt nicht in dieser Ebene. Keine Wahl der beiden Gewichte erzeugt genau diese vier Preise.
:::
:::
