---
title: Stufe 4: Der Sägezahn zu Fuß
pfad: Elektrotechnik / 3. Semester / Höhere Mathematik 3 / Fourier-Reihen
order: 3170500
summary: Stufe 3 ließ offen, ob eine Fourier-Reihe konvergiert.
tags: 
lang: de
---

<span class="anker" id="stufe-4"></span>

:::zweck
Stufe [3](rechenregeln.html#stufe-3) ließ offen, ob eine Fourier-Reihe konvergiert. Am Sägezahn lässt sich das direkt nachrechnen, samt dem Verhalten an einem Sprung.
:::

**Die Idee.** Der Sägezahn $s$ hat $a_k=0$ und $b_k=\frac1k$ (Aufgabe [4](#aufg-4)). Seine Reihe ist also $\sum_{k\ge1}\frac{\sin kx}k$. Der M-Test hilft nicht, denn $\sum\frac1k$ divergiert. Der Trick: Jeder Summand ist das Integral eines Cosinus, und die Summe der Cosinusse hat eine geschlossene Form.

:::satz Satz 4.1 (Summenformel)
<span class="anker" id="satz-4-1"></span>

Für $N\in\mathbb{N}$ und $x\notin2\pi\mathbb{Z}$ gilt

<span class="anker" id="gl-4-1"></span>
$$\sum_{|k|\le N}\mathrm{e}^{\mathrm{i}kx}=\frac{\sin\bigl((N+\frac12)x\bigr)}{\sin\frac x2}. \tag{4.1}$$
:::

:::beweis Summenformel
Multipliziere die linke Seite mit $\mathrm{e}^{\mathrm{i}x/2}-\mathrm{e}^{-\mathrm{i}x/2}=2\mathrm{i}\sin\frac x2$. Das Produkt ist eine Teleskopsumme, in der sich aufeinanderfolgende Summanden aufheben: $\sum_{|k|\le N}\bigl(\mathrm{e}^{\mathrm{i}(k+\frac12)x}-\mathrm{e}^{\mathrm{i}(k-\frac12)x}\bigr)=\mathrm{e}^{\mathrm{i}(N+\frac12)x}-\mathrm{e}^{-\mathrm{i}(N+\frac12)x}=2\mathrm{i}\sin\bigl((N+\frac12)x\bigr)$.
:::

⁠**So liest man das:** Die Summe vieler Zeiger wird zu einem einzigen Bruch. Für $N=1$, $x=\frac\pi2$ steht links $1+2\cos\frac\pi2=1$, rechts $\sin\frac{3\pi}4/\sin\frac\pi4=1$.

:::satz Satz 4.2 (Reihe des Sägezahns)
<span class="anker" id="satz-4-2"></span>

Für alle $x\in\mathbb{R}$ gilt $s(x)=\sum_{k=1}^\infty\frac{\sin kx}k$. Für jedes $\alpha\in(0,\pi)$ konvergiert die Reihe auf $[\alpha,2\pi-\alpha]$ gleichmäßig.
:::

:::beweis Reihe des Sägezahns
⁠**Schritt 1: Integral statt Summe.** Weil $\sin k\pi=0$ ist, gilt $\frac{\sin kx}k=\int_\pi^x\cos ky\,\mathrm{d} y$. Außerdem ist $\sum_{k=1}^N\cos ky=\frac12\bigl(\sum_{|k|\le N}\mathrm{e}^{\mathrm{i}ky}-1\bigr)$. Mit [(4.1)](#gl-4-1) folgt für $x\in(0,2\pi)$

$$\sum_{k=1}^N\frac{\sin kx}k=\frac12\int_\pi^x\frac{\sin\bigl((N+\frac12)y\bigr)}{\sin\frac y2}\,\mathrm{d} y+\frac{\pi-x}2.$$

⁠**Schritt 2: Der Rest wird klein.** Sei $v(y)=1/\sin\frac y2$. Partielle Integration ergibt

$$\int_\pi^xv(y)\sin\bigl((N+\tfrac12)y\bigr)\,\mathrm{d} y=-\Bigl[\frac{v(y)\cos\bigl((N+\frac12)y\bigr)}{N+\frac12}\Bigr]_\pi^x+\int_\pi^x\frac{v'(y)\cos\bigl((N+\frac12)y\bigr)}{N+\frac12}\,\mathrm{d} y.$$

Auf $[\alpha,2\pi-\alpha]$ sind $v$ und $v'$ beschränkt, denn dort ist $\sin\frac y2\ge\sin\frac\alpha2>0$. Also ist der Rest höchstens eine von $x$ unabhängige Konstante mal $\frac1{N+1/2}$. Das ist die gleichmäßige Konvergenz.

⁠**Schritt 3: die übrigen Stellen.** Für $x\in2\pi\mathbb{Z}$ sind alle Summanden null, und $s(x)=0$. Sonst hilft die Periodizität.
:::

⁠**So liest man das:** Abseits der Sprünge fällt der Fehler wie $1/N$, am Sprung liefert die Reihe die Mitte $0$ zwischen $\frac\pi2$ und $-\frac\pi2$. Auf ganz $(0,2\pi)$ ist die Konvergenz nicht gleichmäßig: $T_Ns$ ist stetig mit $T_Ns(0)=0$, bleibt also dicht neben $x=0$ fern von $s\approx\frac\pi2$. Die Voraussetzung $\alpha>0$ ist deshalb nötig (Abb. [4](#abb-4)).

:::abbildung hm3/k7saege 4
Der Sägezahn $s$ und zwei Fourier-Polynome. Im getönten Bereich $[\alpha,2\pi-\alpha]$ legt sich $T_{25}s$ gleichmäßig an $s$. Nahe den Sprüngen schwingt es, und bei $0$ und $2\pi$ läuft jedes $T_Ns$ durch den roten Punkt, den Wert 0.
:::

**Integrieren glättet.** Integriert man den Sägezahn, wird aus dem Sprung ein Knick und aus $\frac1k$ der Faktor $\frac1{k^2}$.

:::satz Satz 4.3 (Integral des Sägezahns)
<span class="anker" id="satz-4-3"></span>

Für alle $x\in[0,2\pi]$ gilt

<span class="anker" id="gl-4-2"></span>
$$\frac{(\pi-x)^2}4=\sum_{k=1}^\infty\frac{\cos kx}{k^2}+C\qquad\text{mit}\quad C=\sum_{k=1}^\infty\frac{(-1)^{k+1}}{k^2}, \tag{4.2}$$

und die Reihe konvergiert gleichmäßig.
:::

:::beweis Integral des Sägezahns
Für $x\in(0,2\pi)$ ist $\frac{(\pi-x)^2}4=-\int_\pi^x\frac{\pi-y}2\,\mathrm{d} y=-\int_\pi^x\sum_{k\ge1}\frac{\sin ky}k\,\mathrm{d} y$. Das Intervall zwischen $\pi$ und $x$ liegt in einem $[\alpha,2\pi-\alpha]$, dort ist die Konvergenz gleichmäßig. Summe und Integral dürfen also vertauscht werden ([Teil 6](/wissen/elektrotechnik/3-semester/hohere-mathematik-3/konvergenz-von-funktionenfolgen/konvergenz-von-funktionenfolgen.html)):

$$\frac{(\pi-x)^2}4=-\sum_{k\ge1}\int_\pi^x\frac{\sin ky}k\,\mathrm{d} y=\sum_{k\ge1}\frac{\cos kx}{k^2}-\sum_{k\ge1}\frac{(-1)^k}{k^2}.$$

Nach dem M-Test mit $M_k=\frac1{k^2}$ konvergiert $\sum\frac{\cos kx}{k^2}$ gleichmäßig auf $\mathbb{R}$, die Summe ist also stetig. Beide Seiten von [(4.2)](#gl-4-2) sind auf $[0,2\pi]$ stetig und stimmen auf $(0,2\pi)$ überein, also auch in den Endpunkten.
:::

⁠**So liest man das:** Links steht eine stetige Parabel, rechts eine Reihe, deren Koeffizienten wie $1/k^2$ fallen. Bei $x=0$ liefert [(4.2)](#gl-4-2) die Beziehung $\frac{\pi^2}4=\sum_{k\ge1}\frac1{k^2}+C$. Die Zahl $C$ ist damit noch nicht bekannt. Dazu fehlt ein Werkzeug, das die $|c_k|^2$ insgesamt erfasst.

:::aufgabe Aufgabe 4 ★ Sägezahn nachrechnen
<span class="anker" id="aufg-4"></span>

<ol class="al">

<li>

Zeige, dass $s$ ungerade ist, und berechne $b_k$ durch partielle Integration.

</li>

<li>

Setze $x=\frac\pi2$ in Satz [4.2](#satz-4-2) ein. Welche Reihe mit welchem Wert entsteht?

</li>

<li>

Was liefert die Reihe bei $x=\pi$, und warum ist das ohne Rechnung klar?

</li>

</ol>

:::loesung
(a) Für $x\in(0,2\pi)$ ist $s(-x)=s(2\pi-x)=\frac{\pi-2\pi+x}2=-s(x)$. Also ist $a_k=0$, und

$$b_k=\frac1{2\pi}\int_0^{2\pi}(\pi-x)\sin kx\,\mathrm{d} x=\frac1{2\pi}\Bigl(\Bigl[-(\pi-x)\frac{\cos kx}k\Bigr]_0^{2\pi}-\int_0^{2\pi}\frac{\cos kx}k\,\mathrm{d} x\Bigr)=\frac1{2\pi}\cdot\frac{2\pi}k=\frac1k.$$

(b) Gerade $k$ fallen weg, und es entsteht $1-\frac13+\frac15-\dots=s(\frac\pi2)=\frac\pi4$. (c) Alle Summanden sind null wegen $\sin k\pi=0$, und $s(\pi)=0$. Ohne Rechnung: Jede Schwingung $\sin kx$ ist dort null.
:::
:::
