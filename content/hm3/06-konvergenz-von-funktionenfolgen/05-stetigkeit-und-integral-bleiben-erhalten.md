---
title: Stufe 3: Stetigkeit und Integral bleiben erhalten
pfad: Elektrotechnik / 3. Semester / Höhere Mathematik 3 / Konvergenz von Funktionenfolgen
order: 3160500
summary: In Stufe 1 gingen Stetigkeit und Integral verloren.
tags: Vertauschbarkeit von Grenzprozessen
lang: de
---

<span class="anker" id="stufe-3"></span>

:::zweck
In Stufe [1](punktweise-konvergenz.html#stufe-1) gingen Stetigkeit und Integral verloren. Diese Stufe zeigt, dass gleichmäßige Konvergenz beides rettet, und warum.
:::

**Die Idee.** Sei $f$ der gleichmäßige Grenzwert stetiger Funktionen. Dann liegt $f$ überall dicht an einer einzigen stetigen Funktion $f_{n_0}$. Um von $f(x)$ nach $f(y)$ zu kommen, nimmt man drei kurze Wege: zu $f_{n_0}(x)$, längs der stetigen Kurve zu $f_{n_0}(y)$, zurück zu $f(y)$ (Abb. [3](#abb-3)). Entscheidend ist, dass *dasselbe* $n_0$ an beiden Stellen passt. Punktweise Konvergenz garantiert das nicht.

:::abbildung hm3/k6drittel 3
Der Weg von $f(x)$ nach $f(y)$ über die stetige Kurve $f_{n_0}$. Die beiden roten Stücke sind kürzer als $\varepsilon/3$, weil $f_{n_0}$ überall im Schlauch um $f$ liegt. Das grüne Stück ändert den Wert um weniger als $\varepsilon/3$, weil $f_{n_0}$ stetig ist.
:::

:::satz Satz 3.1 (Der Grenzwert bleibt stetig)
<span class="anker" id="satz-3-1"></span>

Sei $(f_n)_{n\in\mathbb{N}}$ eine Folge stetiger Funktionen auf $[a,b]$ und $f_n\to f$ gleichmäßig auf $[a,b]$. Dann ist $f:[a,b]\to\mathbb{C}$ stetig.
:::

:::beweis Drei Drittel
Sei $x\in[a,b]$ und $\varepsilon>0$. Wegen der gleichmäßigen Konvergenz gibt es ein $n_0$ mit

$$|f(y)-f_{n_0}(y)|<\varepsilon/3\quad\text{für alle }y\in[a,b].$$

Weil $f_{n_0}$ stetig ist, gibt es ein $\delta>0$ mit $|f_{n_0}(x)-f_{n_0}(y)|<\varepsilon/3$, falls $|x-y|<\delta$. Für solche $y$ gilt

$$|f(x)-f(y)|\le|f(x)-f_{n_0}(x)|+|f_{n_0}(x)-f_{n_0}(y)|+|f_{n_0}(y)-f(y)|<\varepsilon.$$

Also ist $f$ in $x$ stetig, und $x$ war beliebig.
:::

⁠**So liest man das:** Beide Reihenfolgen der Grenzwerte geben $f(x)$: $\lim_{y\to x}\lim_{n\to\infty}f_n(y)=\lim_{n\to\infty}\lim_{y\to x}f_n(y)$. Das heißt __Vertauschbarkeit von Grenzprozessen__. Als Test gelesen: Springt der Grenzwert einer Folge stetiger Funktionen, ist die Konvergenz nicht gleichmäßig. Das erledigt die Entladekurven ohne Rechnung. Der Test gilt nur in dieser Richtung: Die Beulen haben die stetige Grenzfunktion 0 und konvergieren trotzdem nicht gleichmäßig. Zusammen mit dem Cauchy-Kriterium heißt der Satz: Erfüllt eine Folge stetiger Funktionen [(2.2)](gleichmaige-konvergenz.html#gl-2-2), dann konvergiert sie gegen eine stetige Funktion, auch wenn man diese nicht kennt.

:::satz Satz 3.2 (Integral und Grenzwert)
<span class="anker" id="satz-3-2"></span>

Sei $(f_n)_{n\in\mathbb{N}}$ eine Folge stetiger Funktionen und $f_n\to f$ gleichmäßig auf $[a,b]$. Dann gilt

<span class="anker" id="gl-3-1"></span>
$$\lim_{n\to\infty}\int_a^bf_n(x)\,\mathrm{d} x=\int_a^bf(x)\,\mathrm{d} x. \tag{3.1}$$
:::

:::beweis Fläche im Schlauch
Nach Satz [3.1](#satz-3-1) ist $f$ stetig, das Integral rechts existiert also. Zu $\varepsilon>0$ gibt es ein $N$ mit $|f(x)-f_n(x)|\le\varepsilon$ für alle $n\ge N$ und alle $x$. Dann ist

$$\Bigl|\int_a^bf(x)\,\mathrm{d} x-\int_a^bf_n(x)\,\mathrm{d} x\Bigr|\le\int_a^b|f(x)-f_n(x)|\,\mathrm{d} x\le(b-a)\,\varepsilon.$$
:::

⁠**So liest man das:** Die Fläche zwischen zwei Kurven ist höchstens Breite mal größter Abstand. Darin steckt die Länge $b-a$, und sie muss endlich sein (Aufgabe [3](#aufg-3)). **Beispiel:** Für den Rippel $w_3$ ist $\int_0^\pi w_3\,\mathrm{d} x=\frac29\approx0{,}22$, die Abschätzung gibt $\pi\cdot\frac13\approx1{,}05$, und für $n\to\infty$ gehen beide gegen null. Der Satz ist bequem, aber nicht scharf: Auch ohne gleichmäßige Konvergenz kann das Integral passen. So ist $\int_0^1u_n\,\mathrm{d} x=(1-\mathrm{e}^{-n})/n\to0$, und das ist das Integral der Grenzfunktion [(1.2)](punktweise-konvergenz.html#gl-1-2).

:::frage Wo scheitert der Beweis bei den Beulen?
An der Abschätzung. Sie braucht einen kleinen größten Abstand, die Beulen haben aber $d_n=n/\mathrm{e}$. Das gibt nur $\int_0^1b_n\,\mathrm{d} x\le n/\mathrm{e}$, und das sagt für große $n$ nichts. Die Fläche bleibt nahe 1, weil die Höhe wie $n$ wächst und die Breite wie $1/n$ schrumpft.
:::

**Komplexwertige Funktionen.** Ist $f=\operatorname{Re} f+\mathrm i\,\operatorname{Im} f$, dann ist

$$\int_a^bf(x)\,\mathrm{d} x=\int_a^b\operatorname{Re} f(x)\,\mathrm{d} x+\mathrm i\int_a^b\operatorname{Im} f(x)\,\mathrm{d} x,\qquad f'(x)=(\operatorname{Re} f)'(x)+\mathrm i\,(\operatorname{Im} f)'(x).$$

Alle Sätze dieses Kapitels gelten auch für komplexe Werte. Für $f(x)=\mathrm{e}^{\mathrm ix}=\cos x+\mathrm i\sin x$ auf $[0,\pi]$ ist $\int_0^\pi f\,\mathrm{d} x=0+2\mathrm i$.

:::aufgabe Aufgabe 3 ★★ Das Intervall muss endlich sein
<span class="anker" id="aufg-3"></span>

Sei $f_n(x)=\frac1n\mathrm{e}^{-x/n}$ auf $[0,\infty)$. Das Supremum in [(2.1)](gleichmaige-konvergenz.html#gl-2-1) ist hier über $[0,\infty)$ zu nehmen.

<ol class="al">

<li>

Zeige, dass $f_n$ gleichmäßig gegen 0 konvergiert.

</li>

<li>

Berechne $\int_0^\infty f_n\,\mathrm{d} x$. Gilt [(3.1)](#gl-3-1)?

</li>

<li>

Welche Stelle im Beweis von Satz [3.2](#satz-3-2) versagt?

</li>

</ol>

:::loesung
(a) $\sup_{x\ge0}|f_n(x)|=f_n(0)=1/n\to0$. (b) $\int_0^\infty\frac1n\mathrm{e}^{-x/n}\,\mathrm{d} x=\bigl[-\mathrm{e}^{-x/n}\bigr]_0^\infty=1$ für jedes $n$, aber das Integral der Grenzfunktion ist 0. Die Gleichung gilt nicht. (c) Die Abschätzung $\le(b-a)\,\varepsilon$ ist wertlos, weil $b-a=\infty$ ist. Die Kurve wird flacher und breiter, die Fläche bleibt gleich.
:::
:::
