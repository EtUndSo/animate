---
title: Die Kettenregel für mehrere Variablen
pfad: Informatik / Machine Learning / Mathematische Grundlagen / Ableitung, Gradient und Kettenregel
adresse: informatik/machine-learning/mathematische-grundlagen/ableitung-gradient-und-kettenregel
knoten: Kapitel 3: Ableitung, Gradient und Kettenregel
nachschlagen: ja
order: 15230700
summary: Rechnungen mit vielen Variablen sind Ketten von Funktionen mit vielen Ein- und Ausgängen.
tags: Kurve, Geschwindigkeitsvektor
lang: de
---

<span class="anker" id="stufe-6"></span>

:::zweck
Rechnungen mit vielen Variablen sind Ketten von Funktionen mit vielen Ein- und Ausgängen. Die Kettenregel überträgt sich auf sie: Die Jacobi-Matrizen der Stufen werden multipliziert. Komponentenweise heißt das, dass man über alle Wege summiert, auf denen eine Änderung von einem Eingang zum Ausgang gelangt. Für den Gradienten einer Zahl tritt dabei die transponierte Jacobi-Matrix auf.
:::

### Die Kettenregel als Matrixprodukt

<span class="anker" id="stufe-6-1"></span>

Es seien zwei Stufen hintereinandergeschaltet: $\mathbf{g}:\mathbb{R}^n\to\mathbb{R}^m$ macht aus $\mathbf{x}$ den Zwischenvektor $\mathbf{u}=\mathbf{g}(\mathbf{x})$, und $\mathbf f:\mathbb{R}^m\to\mathbb{R}^p$ macht daraus $\mathbf{y}=\mathbf f(\mathbf{u})$. Man verfolgt eine kleine Änderung $\Delta\mathbf{x}$ wie in Abschnitt [2.2](die-kettenregel.html#stufe-2-2). Die erste Stufe gibt sie nach [(5.3)](die-jacobi-matrix.html#gl-5-3) als $\Delta\mathbf{u}\approx\mathbf{J}_{\mathbf{g}}\,\Delta\mathbf{x}$ weiter, die zweite als $\Delta\mathbf{y}\approx\mathbf{J}_{\mathbf f}\,\Delta\mathbf{u}\approx\mathbf{J}_{\mathbf f}\,\mathbf{J}_{\mathbf{g}}\,\Delta\mathbf{x}$. Aus dem Produkt zweier Zahlen wird das Produkt zweier Matrizen. Das passt zu [Kapitel 1, Abschnitt 9.4](/wissen/informatik/machine-learning/mathematische-grundlagen/vektoren-und-matrizen/das-matrixprodukt.html#stufe-9-4): Zwei lineare Stufen hintereinander sind eine lineare Stufe, deren Matrix das Produkt der beiden Matrizen ist.

:::satz Satz 6.1 (Kettenregel für mehrere Variablen)
<span class="anker" id="satz-6-1"></span>

Ist $\mathbf{g}$ an der Stelle $\mathbf{x}$ differenzierbar und $\mathbf f$ an der Stelle $\mathbf{g}(\mathbf{x})$ differenzierbar, so ist $\mathbf f\circ\mathbf{g}$ an der Stelle $\mathbf{x}$ differenzierbar, und

<span class="anker" id="gl-6-1"></span>
$$\mathbf{J}_{\mathbf f\circ\mathbf{g}}(\mathbf{x})=\mathbf{J}_{\mathbf f}\bigl(\mathbf{g}(\mathbf{x})\bigr)\,\mathbf{J}_{\mathbf{g}}(\mathbf{x}). \tag{6.1}$$
:::

Die Formen passen zusammen: Links steht eine $p\times n$-Matrix, rechts eine $p\times m$-Matrix mal einer $m\times n$-Matrix. Die gemeinsame Zahl $m$ ist die Zahl der Zwischenvariablen. Wie in einer Variablen wird jede Jacobi-Matrix dort ausgewertet, wo ihre Stufe arbeitet, $\mathbf{J}_{\mathbf f}$ also am Zwischenwert $\mathbf{u}=\mathbf{g}(\mathbf{x})$. Bei längeren Ketten $\mathbf f_L\circ\dots\circ\mathbf f_1$ ist die Jacobi-Matrix das Produkt $\mathbf{J}_{\mathbf f_L}\cdots\mathbf{J}_{\mathbf f_1}$, mit der zuletzt angewandten Stufe ganz links. Anders als bei Zahlen darf man die Faktoren nicht vertauschen.

:::beweis Kettenregel für mehrere Variablen
Der Beweis geht wie in Abschnitt [2.2](die-kettenregel.html#stufe-2-2), mit Längen statt Beträgen. Mit $\mathbf{u}=\mathbf{g}(\mathbf{x})$ und $\mathbf{k}=\mathbf{g}(\mathbf{x}+\mathbf{h})-\mathbf{u}=\mathbf{J}_{\mathbf{g}}\mathbf{h}+\mathbf{r}_{\mathbf{g}}(\mathbf{h})$ ist

$$\mathbf f\bigl(\mathbf{g}(\mathbf{x}+\mathbf{h})\bigr)-\mathbf f(\mathbf{u})=\mathbf{J}_{\mathbf f}\,\mathbf{k}+\mathbf{r}_{\mathbf f}(\mathbf{k})=\mathbf{J}_{\mathbf f}\mathbf{J}_{\mathbf{g}}\,\mathbf{h}+\mathbf{J}_{\mathbf f}\,\mathbf{r}_{\mathbf{g}}(\mathbf{h})+\mathbf{r}_{\mathbf f}(\mathbf{k}).$$

Der mittlere Fehler verschwindet schneller als $\lVert\mathbf{h}\rVert$, weil $\mathbf{r}_{\mathbf{g}}$ das tut und die Multiplikation mit einer festen Matrix Längen höchstens um einen festen Faktor vergrößert. Der letzte verschwindet schneller als $\lVert\mathbf{k}\rVert$, und $\lVert\mathbf{k}\rVert$ ist höchstens ein festes Vielfaches von $\lVert\mathbf{h}\rVert$, sobald $\mathbf{h}$ klein ist. Also ist $\mathbf{J}_{\mathbf f}\mathbf{J}_{\mathbf{g}}$ die Matrix der linearen Näherung von $\mathbf f\circ\mathbf{g}$.
:::

::::beispiel [Rechenbeispiel]
Es sei $\mathbf{g}$ wie in [(5.1)](die-jacobi-matrix.html#gl-5-1) und $f(\mathbf{u})=u_1^2+3u_2$, eine Funktion mit einem Ausgang ($p=1$). Ihre Verkettung ist $F(\mathbf{x})=f(\mathbf{g}(\mathbf{x}))=x_1^2x_2^2+6x_1+3x_2^2$. An der Stelle $\mathbf{x}=(1,\,2)^{\top}$ ist $\mathbf{u}=\mathbf{g}(\mathbf{x})=(2,\,6)^{\top}$ und $\mathbf{J}_f(\mathbf{u})=(2u_1\ \ 3)=(4\ \ 3)$. Nach [(6.1)](#gl-6-1) ist

$$\mathbf{J}_F(1,2)=\begin{pmatrix}4&3\end{pmatrix}\begin{pmatrix}2&1\\2&4\end{pmatrix}=\begin{pmatrix}4\cdot2+3\cdot2&\ 4\cdot1+3\cdot4\end{pmatrix}=\begin{pmatrix}14&16\end{pmatrix}.$$

Probe mit der ausgeschriebenen Funktion: $\partial_1F=2x_1x_2^2+6=8+6=14$ und $\partial_2F=2x_1^2x_2+6x_2=4+12=16$.
::::

⁠**Kurz gesagt:** Die Jacobi-Matrix einer Verkettung ist das Produkt der Jacobi-Matrizen der Stufen, die zuletzt angewandte Stufe links: $\mathbf{J}_{\mathbf f\circ\mathbf{g}}=\mathbf{J}_{\mathbf f}\,\mathbf{J}_{\mathbf{g}}$.

### Summe über alle Wege

<span class="anker" id="stufe-6-2"></span>

Schreibt man das Matrixprodukt [(6.1)](#gl-6-1) für einen Eintrag aus, so steht dort eine Summe über die Zwischenvariablen. Für eine Funktion $F=f\circ\mathbf{g}$ mit einem Ausgang ist

<span class="anker" id="gl-6-2"></span>
$$\frac{\partial F}{\partial x_j}(\mathbf{x})=\sum_{i=1}^m\frac{\partial f}{\partial u_i}(\mathbf{u})\,\frac{\partial u_i}{\partial x_j}(\mathbf{x}),\qquad \mathbf{u}=\mathbf{g}(\mathbf{x}). \tag{6.2}$$

Diese Summe hat eine anschauliche Bedeutung. Eine Änderung von $x_j$ erreicht $F$ nicht direkt, sondern über die Zwischenvariablen $u_1,\dots,u_m$. Jede Zwischenvariable ist ein Weg: Auf dem Weg über $u_i$ wird die Änderung erst mit $\partial u_i/\partial x_j$ und dann mit $\partial f/\partial u_i$ multipliziert. Am Ausgang kommen die Beiträge aller Wege an und addieren sich (Abb. [11](#abb-11)). Die Kettenregel heißt deshalb oft: Entlang eines Wegs multiplizieren, über alle Wege summieren.

:::abbildung ml/k3wege 11
Die Kettenregel als Netz von Wegen für $F=f\circ\mathbf{g}$ an der Stelle $(1,\,2)$. An jeder Kante steht die lokale Ableitung des Ziels nach dem Ausgangspunkt der Kante. Von $x_1$ führen zwei Wege zu $F$, über $u_1$ (blau) und über $u_2$ (orange). Entlang jedes Wegs werden die Faktoren multipliziert, die beiden Beiträge addiert. Man kann sich ein Rohrnetz vorstellen, in dem jedes Rohr die durchfließende Menge mit seinem Faktor vervielfacht und sich die Ströme am Ziel vereinen.
:::

::::beispiel [Rechenbeispiel 1]
Für $F=f\circ\mathbf{g}$ aus dem vorigen Unterabschnitt sind die Kantenfaktoren an der Stelle $(1,\,2)$

$$\frac{\partial u_1}{\partial x_1}=x_2=2,\quad \frac{\partial u_1}{\partial x_2}=x_1=1,\quad \frac{\partial u_2}{\partial x_1}=2,\quad \frac{\partial u_2}{\partial x_2}=2x_2=4,\quad \frac{\partial f}{\partial u_1}=2u_1=4,\quad \frac{\partial f}{\partial u_2}=3 .$$

Über beide Wege summiert ergibt das die Einträge $14$ und $16$ wie im Matrixprodukt (Abb. [12](#abb-12)).

:::abbildung ml/k3rwege 12
Die partiellen Ableitungen von $F=f\circ\mathbf{g}$ an der Stelle $(1,\,2)$ als Summen über die beiden Wege durch $u_1$ und $u_2$.
:::
::::

::::beispiel [Rechenbeispiel 2]
Ein Eingang, zwei Wege. Es sei $F(x)=g_1(x)\,g_2(x)$ mit $g_1(x)=x^2$ und $g_2(x)=3x$, also $f(\mathbf{u})=u_1u_2$. Die Wege über $u_1$ und $u_2$ liefern

$$\frac{\mathrm{d} F}{\mathrm{d} x}=\frac{\partial f}{\partial u_1}\,g_1'(x)+\frac{\partial f}{\partial u_2}\,g_2'(x)=u_2\cdot2x+u_1\cdot3=3x\cdot2x+x^2\cdot3=9x^2 .$$

Probe: $F(x)=3x^3$ hat die Ableitung $9x^2$. Wer einen Weg vergisst, erhält $6x^2$ oder $3x^2$. Nebenbei ist das genau die Produktregel [(1.5)](die-ableitung.html#gl-1-5): Sie ist die Kettenregel für zwei Wege.
::::

⁠**Kurz gesagt:** Komponentenweise ist die Kettenregel eine Summe über alle Wege vom Eingang zum Ausgang; entlang jedes Wegs werden die lokalen Ableitungen multipliziert.

:::hintergrund Warum man über die Wege summiert
Der Grund ist die Beobachtung aus Abschnitt [3.4](partielle-ableitungen-und-der-gradient.html#stufe-3-4): Bei kleinen Änderungen addieren sich die Wirkungen. Verändert man $x_j$ um $\Delta x_j$, so verändern sich alle Zwischenvariablen zugleich, jede um ungefähr $\frac{\partial u_i}{\partial x_j}\Delta x_j$. Wie diese gleichzeitigen Änderungen auf $f$ wirken, sagt die lineare Näherung von $f$ in den Variablen $u_1,\dots,u_m$: Jede trägt $\frac{\partial f}{\partial u_i}\Delta u_i$ bei, und die Beiträge addieren sich, als hätte sich jede Zwischenvariable allein verändert. Die Summe über die Wege ist also die Summe dieser Einzelbeiträge. Bei längeren Ketten setzt sich das fort: Ein Weg geht dann durch mehrere Zwischenvariablen nacheinander, entlang des Wegs multipliziert man alle Kantenfaktoren, und am Ende summiert man über alle Wege vom Eingang zum Ausgang. Die Zahl der Wege kann dabei sehr schnell wachsen; wie man sie geschickt zusammenfasst, zeigt Abschnitt [10](automatische-differentiation.html#stufe-10).
:::

### Der Gradient einer Verkettung

<span class="anker" id="stufe-6-3"></span>

Für eine Funktion $F=f\circ\mathbf{g}$ mit einem Ausgang ist die Jacobi-Matrix der Gradient als Zeile. Will man den Gradienten als Spalte haben, wie dieses Kapitel ihn vereinbart hat, muss man die Kettenregel transponieren.

:::satz Satz 6.2 (Gradient einer Verkettung)
<span class="anker" id="satz-6-2"></span>

Ist $\mathbf{g}:\mathbb{R}^n\to\mathbb{R}^m$ an der Stelle $\mathbf{x}$ differenzierbar und $f:\mathbb{R}^m\to\mathbb{R}$ an der Stelle $\mathbf{u}=\mathbf{g}(\mathbf{x})$ differenzierbar, so ist

<span class="anker" id="gl-6-3"></span>
$$\nabla(f\circ\mathbf{g})(\mathbf{x})=\mathbf{J}_{\mathbf{g}}(\mathbf{x})^{\top}\,\nabla f(\mathbf{u}). \tag{6.3}$$
:::

:::beweis Gradient einer Verkettung
Nach [(6.1)](#gl-6-1) ist $\nabla(f\circ\mathbf{g})(\mathbf{x})^{\top}=\mathbf{J}_{f\circ\mathbf{g}}(\mathbf{x})=\mathbf{J}_f(\mathbf{u})\,\mathbf{J}_{\mathbf{g}}(\mathbf{x})=\nabla f(\mathbf{u})^{\top}\,\mathbf{J}_{\mathbf{g}}(\mathbf{x})$. Transponiert man beide Seiten mit der Regel $(\mathbf{A}\mathbf{B})^{\top}=\mathbf{B}^{\top}\mathbf{A}^{\top}$ aus [Kapitel 1, Abschnitt 10.1](/wissen/informatik/machine-learning/mathematische-grundlagen/vektoren-und-matrizen/transponierte-symmetrie-und-gram-matrix.html#stufe-10-1), folgt die Behauptung.
:::

Die Transponierte ist reine Buchführung: Sie entsteht, weil der Gradient als Spalte geschrieben wird, die Zeilen der Jacobi-Matrix aber zu den Ausgängen gehören. Inhaltlich sagt [(6.3)](#gl-6-3) dasselbe wie [(6.2)](#gl-6-2): Die Komponente $j$ von $\mathbf{J}_{\mathbf{g}}^{\top}\nabla f$ ist die Spalte $j$ von $\mathbf{J}_{\mathbf{g}}$ mal $\nabla f$, also die Summe über die Wege von $x_j$ aus. Ist die innere Funktion linear, $\mathbf{g}(\mathbf{x})=\mathbf{A}\mathbf{x}$, so wird daraus nach Abschnitt [5.4](die-jacobi-matrix.html#stufe-5-4) die Regel $\nabla_{\mathbf{x}}f(\mathbf{A}\mathbf{x})=\mathbf{A}^{\top}\,\nabla f(\mathbf{A}\mathbf{x})$. Der Index $\mathbf{x}$ am Nabla sagt, nach welcher Variablen der Gradient gebildet wird.

::::beispiel [Rechenbeispiel]
Mit $\mathbf{J}_{\mathbf{g}}(1,2)$ und $\nabla f(\mathbf{u})=(4,\,3)^{\top}$ aus dem Beispiel zu [(6.1)](#gl-6-1) ist

$$\nabla F(1,2)=\begin{pmatrix}2&1\\2&4\end{pmatrix}^{\top}\begin{pmatrix}4\\3\end{pmatrix}=\begin{pmatrix}2&2\\1&4\end{pmatrix}\begin{pmatrix}4\\3\end{pmatrix}=\begin{pmatrix}8+6\\4+12\end{pmatrix}=\begin{pmatrix}14\\16\end{pmatrix}.$$

Ohne Transponieren erhielte man $\mathbf{J}_{\mathbf{g}}\,\nabla f=(8+3;\ 8+12)^{\top}=(11,\,20)^{\top}$, und das ist falsch.
::::

:::warnung Die Transponierte nicht vergessen
Ist die Jacobi-Matrix der inneren Funktion symmetrisch, so fällt ein vergessenes Transponieren nicht auf. Prüfe deshalb eine selbst hergeleitete Gradientenformel an einem Beispiel, dessen Jacobi-Matrix nicht symmetrisch ist. Hat $\mathbf{J}_{\mathbf{g}}$ nicht dieselbe Zahl von Zeilen und Spalten, verrät ein Blick auf die Formen den Fehler sofort: $\nabla f$ hat $m$ Einträge, $\mathbf{J}_{\mathbf{g}}^{\top}$ hat $m$ Spalten, und nur $\mathbf{J}_{\mathbf{g}}^{\top}\nabla f$ ergibt einen Vektor mit $n$ Einträgen.
:::

⁠**Kurz gesagt:** Der Gradient einer Verkettung ist die transponierte Jacobi-Matrix der inneren Funktion mal dem Gradienten der äußeren: $\nabla(f\circ\mathbf{g})=\mathbf{J}_{\mathbf{g}}^{\top}\nabla f$.

### Ableitung entlang einer Kurve

<span class="anker" id="stufe-6-4"></span>

Ein Spaziergang über die Landkarte ist eine Kurve: Zu jeder Zeit $t$ ist man an einem Ort $\boldsymbol{\gamma}(t)\in\mathbb{R}^d$. Wie schnell ändert sich die Höhe $f(\boldsymbol{\gamma}(t))$ unterwegs? Das ist ein Sonderfall der Kettenregel mit einer einzigen Eingangsvariablen $t$.

:::definition Definition 6.3 (Kurve und Geschwindigkeit)
<span class="anker" id="satz-6-3"></span>

Eine __Kurve__ ist eine Funktion $\boldsymbol{\gamma}:\mathbb{R}\to\mathbb{R}^d$, $t\mapsto\boldsymbol{\gamma}(t)=(\gamma_1(t),\dots,\gamma_d(t))^{\top}$. Ihre Ableitung $\boldsymbol{\gamma}'(t)=(\gamma_1'(t),\dots,\gamma_d'(t))^{\top}$ heißt __Geschwindigkeitsvektor__.
:::

Der Geschwindigkeitsvektor ist die Jacobi-Matrix von $\boldsymbol{\gamma}$, eine $d\times1$-Matrix. Er zeigt in die Richtung, in die man sich gerade bewegt, und seine Länge ist das Tempo. Nach [(6.1)](#gl-6-1) mit $n=1$ gilt für differenzierbares $f$

<span class="anker" id="gl-6-4"></span>
$$\frac{\mathrm{d}}{\mathrm{d} t}f\bigl(\boldsymbol{\gamma}(t)\bigr)=\nabla f\bigl(\boldsymbol{\gamma}(t)\bigr)^{\top}\boldsymbol{\gamma}'(t). \tag{6.4}$$

Für eine Gerade $\boldsymbol{\gamma}(t)=\mathbf{x}+t\,\mathbf{h}$ ist $\boldsymbol{\gamma}'=\mathbf{h}$ und die Rate $\nabla f(\mathbf{x})^{\top}\mathbf{h}$; hat $\mathbf{h}$ die Länge $1$, so ist das die Richtungsableitung aus Abschnitt [4.1](richtungsableitung-und-steilster-anstieg.html#stufe-4-1). Verläuft eine Kurve ganz in einer Höhenlinie, so ist $f(\boldsymbol{\gamma}(t))$ konstant, die linke Seite also null: Der Gradient steht senkrecht auf jedem Geschwindigkeitsvektor in der Höhenlinie. Das ist der Satz aus Abschnitt [4.3](richtungsableitung-und-steilster-anstieg.html#stufe-4-3), jetzt mit der Kettenregel begründet.

::::beispiel [Rechenbeispiel]
Es sei $f(\mathbf{x})=x_1^2x_2+x_2^2$ und $\boldsymbol{\gamma}(t)=(1+t,\ 2+2t)^{\top}$, eine Gerade durch $(1,\,2)$ mit $\boldsymbol{\gamma}'(t)=(1,\,2)^{\top}$. Bei $t=0$ ist

$$\frac{\mathrm{d}}{\mathrm{d} t}f\bigl(\boldsymbol{\gamma}(t)\bigr)\Big|_{t=0}=\begin{pmatrix}4&5\end{pmatrix}\begin{pmatrix}1\\2\end{pmatrix}=4+10=14 .$$

Probe: $f(\boldsymbol{\gamma}(t))=(1+t)^2(2+2t)+(2+2t)^2=2\,(1+t)^3+4\,(1+t)^2$ hat bei $t=0$ die Ableitung $6+8=14$.
::::

⁠**Kurz gesagt:** Entlang einer Kurve ändert sich $f$ mit der Rate $\nabla f^{\top}\boldsymbol{\gamma}'$; in einer Höhenlinie ist diese Rate null.

:::aufgabe Aufgabe 20 ★ Kettenregel mit Jacobi-Matrizen
<span class="anker" id="aufg-20"></span>

Es sei $\mathbf{g}(\mathbf{x})=(x_1+x_2,\ x_1x_2)^{\top}$ und $f(\mathbf{u})=u_1^2-u_2$.

<ol class="al">

<li>

Berechne an der Stelle $\mathbf{x}=(1,\,3)^{\top}$ den Zwischenwert $\mathbf{u}$, die Jacobi-Matrix $\mathbf{J}_{\mathbf{g}}(\mathbf{x})$ und $\nabla f(\mathbf{u})$.

</li>

<li>

Berechne $\nabla(f\circ\mathbf{g})(\mathbf{x})$ mit [(6.3)](#gl-6-3) und mache die Probe mit der ausgeschriebenen Funktion. Was käme ohne Transponieren heraus?

</li>

</ol>

:::loesung
(a) $\mathbf{u}=\mathbf{g}(1,3)=(4,\,3)^{\top}$. Die Jacobi-Matrix ist $\mathbf{J}_{\mathbf{g}}(\mathbf{x})=\bigl(\begin{smallmatrix}1&1\\x_2&x_1\end{smallmatrix}\bigr)$, an der Stelle $(1,\,3)$ also $\bigl(\begin{smallmatrix}1&1\\3&1\end{smallmatrix}\bigr)$. Der Gradient der äußeren Funktion ist $\nabla f(\mathbf{u})=(2u_1,\,-1)^{\top}=(8,\,-1)^{\top}$.

(b) Nach [(6.3)](#gl-6-3):

$$\nabla(f\circ\mathbf{g})(1,3)=\begin{pmatrix}1&3\\1&1\end{pmatrix}\begin{pmatrix}8\\-1\end{pmatrix}=\begin{pmatrix}8-3\\8-1\end{pmatrix}=\begin{pmatrix}5\\7\end{pmatrix}.$$

Probe: $F(\mathbf{x})=(x_1+x_2)^2-x_1x_2=x_1^2+x_1x_2+x_2^2$ hat die partiellen Ableitungen $2x_1+x_2=5$ und $x_1+2x_2=7$. Ohne Transponieren erhielte man $\mathbf{J}_{\mathbf{g}}\nabla f=(8-1;\ 24-1)^{\top}=(7,\,23)^{\top}$, also ein falsches Ergebnis.
:::
:::

:::aufgabe Aufgabe 21 ★★ Drei Wege
<span class="anker" id="aufg-21"></span>

Es sei $F(x)=g_1(x)\,g_2(x)\,g_3(x)$ mit $g_1(x)=x$, $g_2(x)=x^2$ und $g_3(x)=x^3$.

<ol class="al">

<li>

Zeichne das Netz der Wege von $x$ über $u_1,u_2,u_3$ zu $F=u_1u_2u_3$ und schreibe an jede Kante ihren Faktor.

</li>

<li>

Berechne $F'(x)$ als Summe über die drei Wege und vergleiche mit der Ableitung von $x^6$.

</li>

</ol>

:::loesung
(a) Von $x$ führen drei Kanten zu $u_1$, $u_2$, $u_3$ mit den Faktoren $1$, $2x$ und $3x^2$. Von $u_i$ führt je eine Kante zu $F=u_1u_2u_3$; ihr Faktor ist das Produkt der beiden anderen: $u_2u_3=x^5$, $u_1u_3=x^4$ und $u_1u_2=x^3$.

(b) Über die drei Wege summiert:

$$F'(x)=x^5\cdot1+x^4\cdot2x+x^3\cdot3x^2=x^5+2x^5+3x^5=6x^5 .$$

Das ist die Ableitung von $F(x)=x^6$. Der Weg über $u_k$ trägt $k\,x^5$ bei, weil $g_k=x^k$ die Ableitung $k\,x^{k-1}$ hat und die beiden anderen Faktoren zusammen $x^{6-k}$ ergeben. Die Produktregel für drei Faktoren ist also die Summe über drei Wege.
:::
:::

:::aufgabe Aufgabe 22 ★★ Kurve in der Höhenlinie
<span class="anker" id="aufg-22"></span>

Es sei $f(\mathbf{x})=x_1^2+4x_2^2$ und $\boldsymbol{\gamma}(t)=\bigl(\sqrt5\cos t,\ \tfrac{\sqrt5}2\sin t\bigr)^{\top}$.

<ol class="al">

<li>

Zeige, dass $\boldsymbol{\gamma}$ ganz in der Höhenlinie $f=5$ verläuft.

</li>

<li>

Bestimme $t$ mit $\boldsymbol{\gamma}(t)=(1,\,1)^{\top}$, berechne dort $\boldsymbol{\gamma}'(t)$ und prüfe $\nabla f^{\top}\boldsymbol{\gamma}'=0$. Vergleiche die Richtung mit dem Vektor $\mathbf{t}$ aus Abschnitt [4.3](richtungsableitung-und-steilster-anstieg.html#stufe-4-3).

</li>

<li>

Begründe allgemein mit [(6.4)](#gl-6-4): Verläuft eine differenzierbare Kurve in einer Niveaumenge von $f$, so steht $\nabla f$ senkrecht auf ihrem Geschwindigkeitsvektor.

</li>

</ol>

:::loesung
(a) $f(\boldsymbol{\gamma}(t))=5\cos^2t+4\cdot\tfrac54\sin^2t=5\,(\cos^2t+\sin^2t)=5$ für jedes $t$.

(b) Aus $\sqrt5\cos t=1$ und $\tfrac{\sqrt5}2\sin t=1$ folgt $\cos t=1/\sqrt5$ und $\sin t=2/\sqrt5$, also $t\approx1{,}107$. Dort ist

$$\boldsymbol{\gamma}'(t)=\bigl(-\sqrt5\sin t,\ \tfrac{\sqrt5}2\cos t\bigr)^{\top}=\bigl(-2,\ \tfrac12\bigr)^{\top},\qquad \nabla f(1,1)^{\top}\boldsymbol{\gamma}'=2\cdot(-2)+8\cdot\tfrac12=0 .$$

Der Geschwindigkeitsvektor ist $-\tfrac12\,(4,\,-1)^{\top}$, also parallel zum Vektor $\mathbf{t}$ aus Abschnitt [4.3](richtungsableitung-und-steilster-anstieg.html#stufe-4-3).

(c) Verläuft $\boldsymbol{\gamma}$ in der Niveaumenge zum Wert $c$, so ist $f(\boldsymbol{\gamma}(t))=c$ für alle $t$, und die Ableitung nach $t$ ist null. Nach [(6.4)](#gl-6-4) ist diese Ableitung $\nabla f(\boldsymbol{\gamma}(t))^{\top}\boldsymbol{\gamma}'(t)$. Also steht der Gradient senkrecht auf jedem Geschwindigkeitsvektor einer Kurve in der Niveaumenge.
:::
:::

:::aufgabe Aufgabe 23 ★★★ Eine Kette aus drei Stufen
<span class="anker" id="aufg-23"></span>

Es sei $F(\mathbf{x})=\sum_{i=1}^2(\mathbf{A}\mathbf{x})_i^2$ mit $\mathbf{A}=\bigl(\begin{smallmatrix}1&2\\0&1\end{smallmatrix}\bigr)$. Die Rechnung besteht aus drei Stufen: $\mathbf{u}=\mathbf{A}\mathbf{x}$, dann $v_i=u_i^2$ für jede Komponente, dann $F=v_1+v_2$.

<ol class="al">

<li>

Gib die drei Jacobi-Matrizen an der Stelle $\mathbf{x}=(2,\,1)^{\top}$ an und berechne $\mathbf{J}_F$ als ihr Produkt.

</li>

<li>

Zeige allgemein $\nabla F(\mathbf{x})=2\mathbf{A}^{\top}\mathbf{A}\mathbf{x}$ und prüfe das Ergebnis aus (a).

</li>

<li>

Rechne das Produkt aus (a) einmal von links und einmal von rechts aus. Welche Reihenfolge braucht weniger Multiplikationen, wenn $\mathbf{A}$ eine $n\times n$-Matrix ist?

</li>

</ol>

:::loesung
(a) An der Stelle $(2,\,1)$ ist $\mathbf{u}=\mathbf{A}\mathbf{x}=(4,\,1)^{\top}$, $\mathbf{v}=(16,\,1)^{\top}$ und $F=17$. Die Jacobi-Matrizen sind $\mathbf{J}_1=\mathbf{A}$, $\mathbf{J}_2=\operatorname{diag}(2u_1;\,2u_2)=\operatorname{diag}(8;\,2)$ und $\mathbf{J}_3=(1\ \ 1)$. Ihr Produkt ist

$$\mathbf{J}_F=(1\ \ 1)\,\operatorname{diag}(8;\,2)\,\begin{pmatrix}1&2\\0&1\end{pmatrix}=(8\ \ 2)\begin{pmatrix}1&2\\0&1\end{pmatrix}=(8\ \ 18).$$

(b) Transponiert ist $\nabla F=\mathbf{A}^{\top}\,\operatorname{diag}(2\mathbf{u})\,\mathbf{1}=\mathbf{A}^{\top}\,2\mathbf{u}=2\mathbf{A}^{\top}\mathbf{A}\mathbf{x}$. Mit $\mathbf{A}^{\top}\mathbf{A}=\bigl(\begin{smallmatrix}1&2\\2&5\end{smallmatrix}\bigr)$ ist $2\mathbf{A}^{\top}\mathbf{A}\mathbf{x}=2\,(4,\,9)^{\top}=(8,\,18)^{\top}$, wie in (a). Probe: $F=(x_1+2x_2)^2+x_2^2$ hat die partiellen Ableitungen $2\cdot4=8$ und $4\cdot4+2=18$.

(c) Von links: $(1\ \ 1)\,\operatorname{diag}(8;2)$ ist eine Zeile, für die man $n$ Multiplikationen braucht, und Zeile mal $\mathbf{A}$ braucht $n^2$. Von rechts: $\operatorname{diag}(8;2)\,\mathbf{A}$ braucht $n^2$ Multiplikationen, und die Zeile mal dem Ergebnis noch einmal $n^2$. Von links sind es also etwa $n^2$, von rechts etwa $2n^2$ Multiplikationen. Wäre die mittlere Matrix nicht diagonal, sondern voll besetzt, so kostete das Matrizenprodukt von rechts sogar etwa $n^3$. Von links, beim Ergebnis beginnend, entstehen immer nur Zeilen.
:::
:::
