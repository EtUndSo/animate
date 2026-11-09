---
title: Einheitsmatrix und Inverse
pfad: Informatik / Machine Learning / Mathematische Grundlagen / Vektoren und Matrizen
knoten: Grundlagen 1: Vektoren und Matrizen
nachschlagen: ja
order: 15211200
summary: Manche linearen Abbildungen lassen sich rückgängig machen, andere nicht.
tags: Einheitsmatrix, invertierbar, Inverse, singulär
lang: de
---

<span class="anker" id="stufe-11"></span>

:::zweck
Manche linearen Abbildungen lassen sich rückgängig machen, andere nicht. Dieser Abschnitt führt die Matrix ein, die nichts verändert, und die inverse Matrix, die eine Abbildung umkehrt, und klärt, wann es sie gibt.
:::

### Die Einheitsmatrix

<span class="anker" id="stufe-11-1"></span>

Unter allen linearen Abbildungen gibt es eine, die gar nichts tut: Sie bildet jeden Vektor auf sich selbst ab. Ihre Spalten sind nach [(8.2)](lineare-abbildungen.html#gl-8-2) die Bilder der Einheitsvektoren, also die Einheitsvektoren selbst.

:::definition Definition 11.1 (Einheitsmatrix)
<span class="anker" id="satz-11-1"></span>

Die __Einheitsmatrix__ $\mathbf{I}_n\in\mathbb{R}^{n\times n}$ ist die Diagonalmatrix mit lauter Einsen auf der Diagonale. Ihre Spalten sind $\mathbf{e}_1,\dots,\mathbf{e}_n$.
:::

Wenn das Format klar ist, schreibt man kurz $\mathbf{I}$. Für jeden Vektor $\mathbf{x}\in\mathbb{R}^n$ ist $\mathbf{I}\mathbf{x}=\mathbf{x}$, und für jede Matrix $\mathbf{A}\in\mathbb{R}^{m\times n}$ ist $\mathbf{A}\mathbf{I}_n=\mathbf{A}$ und $\mathbf{I}_m\mathbf{A}=\mathbf{A}$. Die Einheitsmatrix spielt beim Matrixprodukt die Rolle der Zahl $1$.

::::beispiel [Rechenbeispiel]
$$\mathbf{I}_3=\begin{pmatrix}1&0&0\\0&1&0\\0&0&1\end{pmatrix},\qquad \mathbf{I}_3\begin{pmatrix}60\\2\\3\end{pmatrix}=\begin{pmatrix}60\\2\\3\end{pmatrix}.$$
::::

⁠**Kurz gesagt:** Die Einheitsmatrix hat Einsen auf der Diagonale und sonst Nullen; als Abbildung lässt sie jeden Vektor unverändert.

### Die inverse Matrix

<span class="anker" id="stufe-11-2"></span>

Eine Drehung um $90^\circ$ macht man rückgängig, indem man um $90^\circ$ zurückdreht. Eine Streckung auf das Doppelte macht man rückgängig, indem man auf die Hälfte staucht. In beiden Fällen gibt es eine zweite Abbildung, die die erste aufhebt: Hintereinander ausgeführt, tun beide zusammen nichts.

:::definition Definition 11.2 (Inverse Matrix)
<span class="anker" id="satz-11-2"></span>

Eine quadratische Matrix $\mathbf{A}\in\mathbb{R}^{n\times n}$ heißt __invertierbar__, wenn es eine Matrix $\mathbf{A}^{-1}\in\mathbb{R}^{n\times n}$ gibt mit

<span class="anker" id="gl-11-1"></span>
$$\mathbf{A}\mathbf{A}^{-1}=\mathbf{A}^{-1}\mathbf{A}=\mathbf{I} . \tag{11.1}$$

Die Matrix $\mathbf{A}^{-1}$ heißt die __Inverse__ von $\mathbf{A}$.
:::

Es gibt höchstens eine solche Matrix. Sind nämlich $\mathbf{B}$ und $\mathbf{C}$ beide invers zu $\mathbf{A}$, so ist $\mathbf{B}=\mathbf{B}\mathbf{I}=\mathbf{B}(\mathbf{A}\mathbf{C})=(\mathbf{B}\mathbf{A})\mathbf{C}=\mathbf{I}\mathbf{C}=\mathbf{C}$. Deshalb darf man von *der* Inversen sprechen. Kennt man sie, kann man jedes Ergebnis $\mathbf{y}=\mathbf{A}\mathbf{x}$ zurückrechnen: $\mathbf{A}^{-1}\mathbf{y}=\mathbf{A}^{-1}\mathbf{A}\mathbf{x}=\mathbf{x}$.

::::beispiel [Rechenbeispiel]
$$\begin{pmatrix}2&1\\1&1\end{pmatrix}\begin{pmatrix}1&-1\\-1&2\end{pmatrix}=\begin{pmatrix}2-1&-2+2\\1-1&-1+2\end{pmatrix}=\begin{pmatrix}1&0\\0&1\end{pmatrix},$$

und ebenso in der anderen Reihenfolge, also ist $\bigl(\begin{smallmatrix}2&1\\1&1\end{smallmatrix}\bigr)^{-1}=\bigl(\begin{smallmatrix}1&-1\\-1&2\end{smallmatrix}\bigr)$. Die Streckung hat die Inverse $\operatorname{diag}(2;\,0{,}5)^{-1}=\operatorname{diag}(0{,}5;\,2)$, die Drehung um $90^\circ$ die Drehung um $-90^\circ$, $\bigl(\begin{smallmatrix}0&-1\\1&0\end{smallmatrix}\bigr)^{-1}=\bigl(\begin{smallmatrix}0&1\\-1&0\end{smallmatrix}\bigr)$.
::::

⁠**Kurz gesagt:** Die Inverse $\mathbf{A}^{-1}$ macht die Abbildung $\mathbf{A}$ rückgängig: $\mathbf{A}^{-1}\mathbf{A}=\mathbf{A}\mathbf{A}^{-1}=\mathbf{I}$.

:::hintergrund Die Inverse einer Diagonalmatrix
Eine Diagonalmatrix $\operatorname{diag}(\mathbf{v})$ multipliziert jede Komponente mit ihrem eigenen Faktor $v_j$. Rückgängig macht man das, indem man jede Komponente durch ihren Faktor teilt: $\operatorname{diag}(\mathbf{v})^{-1}=\operatorname{diag}(1/v_1,\dots,1/v_n)$. Das geht genau dann, wenn kein Faktor null ist. Ein Faktor $v_j=0$ löscht die Komponente $j$ aus, und was gelöscht ist, kann keine Rechnung zurückholen.
:::

### Die Inverse einer $2\times2$-Matrix

<span class="anker" id="stufe-11-3"></span>

Für $2\times2$-Matrizen gibt es eine einfache Formel. Man vertauscht die beiden Diagonaleinträge, setzt vor die beiden anderen ein Minus und teilt durch eine Zahl, die man aus allen vier Einträgen bildet.

:::satz Satz 11.3 (Inverse einer $2\times2$-Matrix)
<span class="anker" id="satz-11-3"></span>

Die Matrix $\mathbf{A}=\bigl(\begin{smallmatrix}a&b\\c&d\end{smallmatrix}\bigr)$ ist genau dann invertierbar, wenn $ad-bc\ne0$ ist, und dann ist

<span class="anker" id="gl-11-2"></span>
$$\mathbf{A}^{-1}=\frac{1}{ad-bc}\begin{pmatrix}d&-b\\-c&a\end{pmatrix}. \tag{11.2}$$
:::

:::herleitung Inverse einer $2\times2$-Matrix
Ausmultipliziert ist

$$\begin{pmatrix}a&b\\c&d\end{pmatrix}\begin{pmatrix}d&-b\\-c&a\end{pmatrix}=\begin{pmatrix}ad-bc&-ab+ba\\cd-dc&-cb+da\end{pmatrix}=(ad-bc)\,\mathbf{I} ,$$

und in der anderen Reihenfolge ebenso. Ist $ad-bc\ne0$, teilt man durch diese Zahl und erhält [(11.1)](#gl-11-1). Ist $ad-bc=0$, so schickt $\mathbf{A}$ den Vektor $(d,\,-c)^{\top}$ auf $(ad-bc,\ cd-dc)^{\top}=\mathbf{0}$ und ebenso $(b,\,-a)^{\top}$ auf $\mathbf{0}$. Wenigstens einer der beiden ist nicht der Nullvektor, außer alle vier Einträge sind null, und dann ist $\mathbf{A}$ ohnehin die Nullmatrix. Eine Matrix, die einen Vektor $\mathbf{x}\ne\mathbf{0}$ auf $\mathbf{0}$ abbildet, hat aber keine Inverse: Gäbe es eine, so wäre $\mathbf{x}=\mathbf{A}^{-1}\mathbf{A}\mathbf{x}=\mathbf{A}^{-1}\mathbf{0}=\mathbf{0}$.
:::

::::beispiel [Rechenbeispiel]
Für $\bigl(\begin{smallmatrix}2&1\\1&1\end{smallmatrix}\bigr)$ ist $ad-bc=2-1=1$, also ist die Inverse $\bigl(\begin{smallmatrix}1&-1\\-1&2\end{smallmatrix}\bigr)$, wie oben. Für $\bigl(\begin{smallmatrix}3&1\\1&2\end{smallmatrix}\bigr)$ ist $ad-bc=5$ und die Inverse $\tfrac15\bigl(\begin{smallmatrix}2&-1\\-1&3\end{smallmatrix}\bigr)$.
::::

⁠**Kurz gesagt:** Eine $2\times2$-Matrix ist genau dann invertierbar, wenn $ad-bc\ne0$; die Inverse ist $\frac{1}{ad-bc}\bigl(\begin{smallmatrix}d&-b\\-c&a\end{smallmatrix}\bigr)$.

### Rechenregeln für Inverse

<span class="anker" id="stufe-11-4"></span>

Wer zwei Abbildungen hintereinander ausführt und das rückgängig machen will, muss die zweite zuerst aufheben. Deshalb kehrt sich beim Invertieren eines Produkts die Reihenfolge um.

:::satz Satz 11.4 (Rechenregeln für Inverse)
<span class="anker" id="satz-11-4"></span>

Sind $\mathbf{A},\mathbf{B}\in\mathbb{R}^{n\times n}$ invertierbar und ist $c\ne0$, so sind auch $\mathbf{A}\mathbf{B}$, $\mathbf{A}^{\top}$, $\mathbf{A}^{-1}$ und $c\,\mathbf{A}$ invertierbar, und es gilt

$$(\mathbf{A}\mathbf{B})^{-1}=\mathbf{B}^{-1}\mathbf{A}^{-1},\qquad(\mathbf{A}^{\top})^{-1}=(\mathbf{A}^{-1})^{\top},\qquad(\mathbf{A}^{-1})^{-1}=\mathbf{A},\qquad(c\,\mathbf{A})^{-1}=\tfrac1c\,\mathbf{A}^{-1}.$$
:::

:::herleitung Rechenregeln für Inverse
Man prüft jeweils, dass das Produkt mit dem Kandidaten die Einheitsmatrix ergibt. Für das Produkt: $(\mathbf{A}\mathbf{B})(\mathbf{B}^{-1}\mathbf{A}^{-1})=\mathbf{A}(\mathbf{B}\mathbf{B}^{-1})\mathbf{A}^{-1}=\mathbf{A}\mathbf{A}^{-1}=\mathbf{I}$, und ebenso $(\mathbf{B}^{-1}\mathbf{A}^{-1})(\mathbf{A}\mathbf{B})=\mathbf{I}$. Für die Transponierte: $\mathbf{A}^{\top}(\mathbf{A}^{-1})^{\top}=(\mathbf{A}^{-1}\mathbf{A})^{\top}=\mathbf{I}^{\top}=\mathbf{I}$, und in der anderen Reihenfolge ebenso. Die beiden letzten Regeln folgen direkt aus [(11.1)](#gl-11-1).
:::

Eine Regel, die man gern hätte, gilt nicht: $(\mathbf{A}+\mathbf{B})^{-1}$ ist im Allgemeinen nicht $\mathbf{A}^{-1}+\mathbf{B}^{-1}$. Schon für Zahlen ist $\frac{1}{2+4}=\frac16$, aber $\frac12+\frac14=\frac34$.

::::beispiel [Rechenbeispiel]
Für $\mathbf{A}=\bigl(\begin{smallmatrix}2&1\\1&1\end{smallmatrix}\bigr)$ und $\mathbf{B}=\bigl(\begin{smallmatrix}3&1\\1&2\end{smallmatrix}\bigr)$ ist $\mathbf{A}\mathbf{B}=\bigl(\begin{smallmatrix}7&4\\4&3\end{smallmatrix}\bigr)$ mit $ad-bc=21-16=5$, also $(\mathbf{A}\mathbf{B})^{-1}=\tfrac15\bigl(\begin{smallmatrix}3&-4\\-4&7\end{smallmatrix}\bigr)$. Dasselbe ergibt

$$\mathbf{B}^{-1}\mathbf{A}^{-1}=\tfrac15\begin{pmatrix}2&-1\\-1&3\end{pmatrix}\begin{pmatrix}1&-1\\-1&2\end{pmatrix}=\tfrac15\begin{pmatrix}3&-4\\-4&7\end{pmatrix}.$$
::::

⁠**Kurz gesagt:** Die Inverse eines Produkts ist das Produkt der Inversen in umgekehrter Reihenfolge, $(\mathbf{A}\mathbf{B})^{-1}=\mathbf{B}^{-1}\mathbf{A}^{-1}$.

:::hintergrund Ein Bild für die umgekehrte Reihenfolge
Wer morgens zuerst einen Pullover und dann eine Jacke anzieht, zieht abends zuerst die Jacke und dann den Pullover aus. Das Rückgängigmachen läuft rückwärts durch die Schritte. Die Abbildung $\mathbf{A}\mathbf{B}$ ist „erst $\mathbf{B}$, dann $\mathbf{A}$“; um sie aufzuheben, muss man zuerst $\mathbf{A}$ aufheben und dann $\mathbf{B}$, also erst $\mathbf{A}^{-1}$ und dann $\mathbf{B}^{-1}$. Als Matrix geschrieben, mit der zuerst ausgeführten rechts, ist das $\mathbf{B}^{-1}\mathbf{A}^{-1}$. Das Bild trägt nur so weit, wie es um die Reihenfolge geht; es erklärt nicht, warum eine Inverse existiert.
:::

### Wann es keine Inverse gibt

<span class="anker" id="stufe-11-5"></span>

Die Matrix $\operatorname{diag}(1;\,0)$ drückt die Ebene auf die $x_1$-Achse platt (Abb. [32](lineare-abbildungen.html#abb-32)). Die Punkte $(1,\,5)^{\top}$ und $(1,\,-2)^{\top}$ landen beide in $(1,\,0)^{\top}$. Wer nur das Ergebnis $(1,\,0)^{\top}$ sieht, kann nicht wissen, von welchem Punkt es kam. Die zweite Komponente ist verloren, und keine Rechnung bringt sie zurück.

:::satz Satz 11.5 (Ohne Inverse)
<span class="anker" id="satz-11-5"></span>

Gibt es einen Vektor $\mathbf{x}\ne\mathbf{0}$ mit $\mathbf{A}\mathbf{x}=\mathbf{0}$, so ist $\mathbf{A}$ nicht invertierbar.
:::

:::beweis Ohne Inverse
Gäbe es eine Inverse, so wäre $\mathbf{x}=\mathbf{A}^{-1}\mathbf{A}\mathbf{x}=\mathbf{A}^{-1}\mathbf{0}=\mathbf{0}$, im Widerspruch zu $\mathbf{x}\ne\mathbf{0}$.
:::

Anschaulich: Mit $\mathbf{A}\mathbf{x}=\mathbf{0}$ landen für jedes $\mathbf{u}$ die beiden verschiedenen Vektoren $\mathbf{u}$ und $\mathbf{u}+\mathbf{x}$ am selben Ort, denn $\mathbf{A}(\mathbf{u}+\mathbf{x})=\mathbf{A}\mathbf{u}+\mathbf{A}\mathbf{x}=\mathbf{A}\mathbf{u}$. Zwei Eingänge mit demselben Ausgang lassen sich nicht auseinanderhalten. Eine quadratische Matrix, die nicht invertierbar ist, heißt __singulär__.

::::beispiel [Rechenbeispiel]
Für $\bigl(\begin{smallmatrix}1&2\\2&4\end{smallmatrix}\bigr)$ ist $ad-bc=4-4=0$. Tatsächlich wird $\mathbf{x}=(2,\,-1)^{\top}$ auf $(2-2,\ 4-4)^{\top}=\mathbf{0}$ abgebildet, und die verschiedenen Vektoren $(1,\,1)^{\top}$ und $(3,\,0)^{\top}$ landen beide in $(3,\,6)^{\top}$.
::::

Für Daten heißt das: Eine Rechnung, die zum Beispiel aus Schlafzimmern und Wohnzimmern nur die Summe der Zimmer bildet, kann die beiden Zahlen nicht mehr trennen. Bei $2\times2$-Matrizen ist das genau der Fall $ad-bc=0$ aus Unterabschnitt [11.3](#stufe-11-3).

⁠**Kurz gesagt:** Bildet eine Matrix einen Vektor $\mathbf{x}\ne\mathbf{0}$ auf $\mathbf{0}$ ab, so verliert sie Information und hat keine Inverse; sie heißt dann singulär.

:::aufgabe Aufgabe 26 ★ Inverse berechnen
<span class="anker" id="aufg-26"></span>

<ol class="al">

<li>

Berechne die Inversen von $\bigl(\begin{smallmatrix}4&3\\1&1\end{smallmatrix}\bigr)$ und $\bigl(\begin{smallmatrix}1&2\\3&4\end{smallmatrix}\bigr)$ und mache jeweils die Probe.

</li>

<li>

Für welche Zahl $t$ ist $\bigl(\begin{smallmatrix}2&t\\4&6\end{smallmatrix}\bigr)$ nicht invertierbar? Gib für diesen Fall einen Vektor $\mathbf{x}\ne\mathbf{0}$ mit $\mathbf{A}\mathbf{x}=\mathbf{0}$ an.

</li>

<li>

Gib die Inverse von $\operatorname{diag}(4;\,-1;\,0{,}5)$ an.

</li>

</ol>

:::loesung
(a) Für $\bigl(\begin{smallmatrix}4&3\\1&1\end{smallmatrix}\bigr)$ ist $ad-bc=4-3=1$ und die Inverse $\bigl(\begin{smallmatrix}1&-3\\-1&4\end{smallmatrix}\bigr)$. Probe: $\bigl(\begin{smallmatrix}4&3\\1&1\end{smallmatrix}\bigr)\bigl(\begin{smallmatrix}1&-3\\-1&4\end{smallmatrix}\bigr)=\bigl(\begin{smallmatrix}4-3&-12+12\\1-1&-3+4\end{smallmatrix}\bigr)=\mathbf{I}$. Für $\bigl(\begin{smallmatrix}1&2\\3&4\end{smallmatrix}\bigr)$ ist $ad-bc=4-6=-2$ und die Inverse $-\tfrac12\bigl(\begin{smallmatrix}4&-2\\-3&1\end{smallmatrix}\bigr)=\bigl(\begin{smallmatrix}-2&1\\1{,}5&-0{,}5\end{smallmatrix}\bigr)$. Probe: $\bigl(\begin{smallmatrix}1&2\\3&4\end{smallmatrix}\bigr)\bigl(\begin{smallmatrix}-2&1\\1{,}5&-0{,}5\end{smallmatrix}\bigr)=\bigl(\begin{smallmatrix}-2+3&1-1\\-6+6&3-2\end{smallmatrix}\bigr)=\mathbf{I}$.

(b) $ad-bc=12-4t=0$ für $t=3$. Dann ist die Matrix $\bigl(\begin{smallmatrix}2&3\\4&6\end{smallmatrix}\bigr)$; ihre zweite Zeile ist das Doppelte der ersten. Der Vektor $(3,\,-2)^{\top}$ wird auf $(6-6,\ 12-12)^{\top}=\mathbf{0}$ abgebildet.

(c) $\operatorname{diag}(4;\,-1;\,0{,}5)^{-1}=\operatorname{diag}(0{,}25;\,-1;\,2)$: Jeder Diagonaleintrag wird durch seinen Kehrwert ersetzt.
:::
:::

:::aufgabe Aufgabe 27 ★★ Mit Inversen argumentieren
<span class="anker" id="aufg-27"></span>

<ol class="al">

<li>

Prüfe $(\mathbf{C}^{\top})^{-1}=(\mathbf{C}^{-1})^{\top}$ für $\mathbf{C}=\bigl(\begin{smallmatrix}1&2\\3&4\end{smallmatrix}\bigr)$.

</li>

<li>

Es sei $\mathbf{A}$ invertierbar und $\mathbf{A}\mathbf{B}=\mathbf 0$. Zeige, dass dann $\mathbf{B}=\mathbf 0$ ist.

</li>

<li>

Bei Zahlen folgt aus $ab=0$, dass $a=0$ oder $b=0$ ist. Zeige mit $\mathbf{A}=\mathbf{B}=\bigl(\begin{smallmatrix}0&1\\0&0\end{smallmatrix}\bigr)$, dass das für Matrizen nicht gilt. Warum widerspricht das nicht (b)?

</li>

</ol>

:::loesung
(a) $\mathbf{C}^{-1}=\bigl(\begin{smallmatrix}-2&1\\1{,}5&-0{,}5\end{smallmatrix}\bigr)$ aus der vorigen Aufgabe, also $(\mathbf{C}^{-1})^{\top}=\bigl(\begin{smallmatrix}-2&1{,}5\\1&-0{,}5\end{smallmatrix}\bigr)$. Andererseits ist $\mathbf{C}^{\top}=\bigl(\begin{smallmatrix}1&3\\2&4\end{smallmatrix}\bigr)$ mit $ad-bc=-2$, also $(\mathbf{C}^{\top})^{-1}=-\tfrac12\bigl(\begin{smallmatrix}4&-3\\-2&1\end{smallmatrix}\bigr)=\bigl(\begin{smallmatrix}-2&1{,}5\\1&-0{,}5\end{smallmatrix}\bigr)$. Beide stimmen überein.

(b) Man multipliziert $\mathbf{A}\mathbf{B}=\mathbf 0$ von links mit $\mathbf{A}^{-1}$: $\mathbf{B}=\mathbf{I}\mathbf{B}=\mathbf{A}^{-1}\mathbf{A}\mathbf{B}=\mathbf{A}^{-1}\mathbf 0=\mathbf 0$.

(c) $\mathbf{A}\mathbf{A}=\bigl(\begin{smallmatrix}0&1\\0&0\end{smallmatrix}\bigr)\bigl(\begin{smallmatrix}0&1\\0&0\end{smallmatrix}\bigr)=\bigl(\begin{smallmatrix}0\cdot0+1\cdot0&0\cdot1+1\cdot0\\0&0\end{smallmatrix}\bigr)=\mathbf 0$, obwohl $\mathbf{A}\ne\mathbf 0$. Geometrisch schickt $\mathbf{A}$ den Vektor $\mathbf{e}_2$ nach $\mathbf{e}_1$ und $\mathbf{e}_1$ nach $\mathbf{0}$; zweimal angewandt landet alles im Nullvektor. Das widerspricht (b) nicht, denn $\mathbf{A}$ ist nicht invertierbar: $ad-bc=0$. Die Folgerung in (b) braucht die Inverse.
:::
:::
