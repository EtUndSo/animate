---
title: Stufe 2: Koeffizienten und Polynome
pfad: Elektrotechnik / 3. Semester / HöMa3 – Höhere Mathematik 3 / Fourier-Reihen
adresse: elektrotechnik/3-semester/hohere-mathematik-3/fourier-reihen
knoten: Kapitel 7: Fourier-Reihen
order: 3170300
summary: Diese Stufe macht aus dem Skalarprodukt von Stufe 1 eine Definition für jede periodische Funktion und schreibt das Ergebnis auch reell.
tags: Fourier-Koeffizient, Fourier-Polynom
lang: de
---

<span class="anker" id="stufe-2"></span>

:::zweck
Diese Stufe macht aus dem Skalarprodukt von Stufe [1](schwingungen-als-bausteine.html#stufe-1) eine Definition für jede periodische Funktion und schreibt das Ergebnis auch reell.
:::

**Die Idee.** Ist $f$ eine endliche Summe von Bausteinen, ist der Faktor vor $\hat{\boldsymbol{e}}_k$ gleich $\langle f,\hat{\boldsymbol{e}}_k\rangle$. Für eine Kurve wie das Rechteck $q$ ist offen, ob sie so eine Summe ist. Das Integral $\langle f,\hat{\boldsymbol{e}}_k\rangle$ lässt sich aber trotzdem ausrechnen. Man nimmt es als Definition und baut aus den Bausteinen bis zur Frequenz $N$ eine Näherung.

:::definition Definition 2.1 (Fourier-Koeffizient und Fourier-Polynom)
<span class="anker" id="satz-2-1"></span>

Sei $f:\mathbb{R}\to\mathbb{C}$ $2\pi$-periodisch und über $[0,2\pi]$ Riemann-integrierbar. Dann heißt für $k\in\mathbb{Z}$

<span class="anker" id="gl-2-1"></span>
$$c_k=\langle f,\hat{\boldsymbol{e}}_k\rangle=\frac1{2\pi}\int_0^{2\pi}f(x)\,\mathrm{e}^{-\mathrm{i}kx}\,\mathrm{d} x \tag{2.1}$$

der $k$-te __Fourier-Koeffizient__ von $f$, und für $N\in\mathbb{N}_0$ heißt

<span class="anker" id="gl-2-2"></span>
$$T_Nf=\sum_{|k|\le N}c_k\hat{\boldsymbol{e}}_k=\sum_{|k|\le N}\langle f,\hat{\boldsymbol{e}}_k\rangle\,\hat{\boldsymbol{e}}_k \tag{2.2}$$

das $N$-te __Fourier-Polynom__ von $f$.
:::

⁠**So liest man das:** $c_k$ ist der Anteil von $\hat{\boldsymbol{e}}_k$ in $f$, und $c_0$ ist der Mittelwert von $f$. Das Minuszeichen im Exponenten kommt aus der Konjugation in [(1.1)](schwingungen-als-bausteine.html#gl-1-1). Der Integrand hat die Periode $2\pi$, deshalb darf man über jede volle Periode integrieren: $c_k=\frac1{2\pi}\int_{x_0}^{x_0+2\pi}f(x)\,\mathrm{e}^{-\mathrm{i}kx}\,\mathrm{d} x$ für jedes $x_0\in\mathbb{R}$. Was am Anfang wegfällt, kommt am Ende wieder hinzu. Oft ist $x_0=-\pi$ bequem.

:::satz Satz 2.2 (Reelle Darstellung)
<span class="anker" id="satz-2-2"></span>

Sei $f$ wie in Definition [2.1](#satz-2-1), und für $k\in\mathbb{Z}$ sei

<span class="anker" id="gl-2-3"></span>
$$a_k=\frac1\pi\int_0^{2\pi}f(x)\cos(kx)\,\mathrm{d} x,\qquad b_k=\frac1\pi\int_0^{2\pi}f(x)\sin(kx)\,\mathrm{d} x. \tag{2.3}$$

Dann gilt für alle $k\in\mathbb{N}_0$: $a_{-k}=a_k$, $b_{-k}=-b_k$ (also $b_0=0$), $c_k=\frac12(a_k-\mathrm{i}\,b_k)$, $c_{-k}=\frac12(a_k+\mathrm{i}\,b_k)$ und

<span class="anker" id="gl-2-4"></span>
$$T_Nf(x)=\frac{a_0}2+\sum_{k=1}^N\bigl(a_k\cos(kx)+b_k\sin(kx)\bigr). \tag{2.4}$$
:::

:::beweis Reelle Darstellung
Die Eulersche Formel $\mathrm{e}^{-\mathrm{i}kx}=\cos kx-\mathrm{i}\sin kx$ in [(2.1)](#gl-2-1) gibt $c_k=\frac12(a_k-\mathrm{i}\,b_k)$. Der Cosinus ist gerade und der Sinus ungerade, das gibt $a_{-k}=a_k$ und $b_{-k}=-b_k$ und damit $c_{-k}$. Für $k\ge1$ fasst man die beiden Summanden zu $\pm k$ zusammen:

$$c_k\mathrm{e}^{\mathrm{i}kx}+c_{-k}\mathrm{e}^{-\mathrm{i}kx}=\tfrac12a_k\bigl(\mathrm{e}^{\mathrm{i}kx}+\mathrm{e}^{-\mathrm{i}kx}\bigr)-\tfrac{\mathrm{i}}2b_k\bigl(\mathrm{e}^{\mathrm{i}kx}-\mathrm{e}^{-\mathrm{i}kx}\bigr)=a_k\cos kx+b_k\sin kx.$$

Der Summand zu $k=0$ ist $c_0=a_0/2$.
:::

⁠**So liest man das:** Der Faktor $\frac1\pi$ statt $\frac1{2\pi}$ hat einen Grund: Für $k,\ell\in\mathbb{N}$ gilt

<span class="anker" id="gl-2-5"></span>
$$\frac1\pi\int_0^{2\pi}\cos kx\cos\ell x\,\mathrm{d} x=\frac1\pi\int_0^{2\pi}\sin kx\sin\ell x\,\mathrm{d} x=\delta_{k\ell},\qquad\frac1\pi\int_0^{2\pi}\sin kx\cos\ell x\,\mathrm{d} x=0. \tag{2.5}$$

Mit diesem reellen Skalarprodukt sind $\cos kx$ und $\sin kx$ für $k\ge1$ orthonormal. Die Konstante 1 ist es nicht: $\frac1\pi\int_0^{2\pi}1\,\mathrm{d} x=2$. Deshalb steht in [(2.4)](#gl-2-4) die Hälfte $a_0/2$, und $a_0$ selbst passt in dieselbe Formel [(2.3)](#gl-2-3) wie alle anderen.

::::beispiel das Rechteck
Für $k\ge1$ ist $\int_0^\pi\cos kx\,\mathrm{d} x=\int_\pi^{2\pi}\cos kx\,\mathrm{d} x=0$, außerdem $a_0=0$. Also sind alle $a_k$ null. Weiter ist

<span class="anker" id="gl-2-6"></span>
$$b_k=\frac1\pi\Bigl(\int_0^\pi\sin kx\,\mathrm{d} x-\int_\pi^{2\pi}\sin kx\,\mathrm{d} x\Bigr)=\frac{2\bigl(1-(-1)^k\bigr)}{\pi k}=\begin{cases}\dfrac4{\pi k}&k\text{ ungerade,}\\0&k\text{ gerade.}\end{cases} \tag{2.6}$$

Also ist $T_Nq(x)=\frac4\pi\sum_{k\le N,\ k\text{ ungerade}}\frac{\sin kx}k$. An der Stelle $x=\frac\pi2$ ergibt das für $N=1,3,5$ die Werte $1{,}27$, $0{,}85$, $1{,}10$, die um den Wert $q(\frac\pi2)=1$ pendeln.
::::

⁠**Grenzfall:** $c_0=0$, denn $q$ verbringt gleich viel Zeit bei $+1$ und bei $-1$. Abb. [2](#abb-2) zeigt die Näherungen.

:::abbildung hm3/k7rechteck 2
Links: Das Rechteck $q$ und drei Fourier-Polynome. Mit wachsendem $N$ schmiegt sich die Kurve an $q$ an, an den Sprüngen läuft sie durch den Wert 0. Rechts: Die reellen Koeffizienten $b_k$ von $q$ fallen wie $1/k$, die geraden sind null.
:::

:::aufgabe Aufgabe 2 ★★ Rampe mit Plateau
<span class="anker" id="aufg-2"></span>

Sei $f$ die $2\pi$-periodische Funktion mit $f(x)=x$ auf $[0,\pi]$ und $f(x)=\pi$ auf $(\pi,2\pi)$. Berechne $a_0$, $a_k$ und $b_k$ für $k\ge1$, gib $T_2f$ an und bestimme $c_0$, $c_1$, $c_2$.

:::loesung
$a_0=\frac1\pi\bigl(\frac{\pi^2}2+\pi^2\bigr)=\frac{3\pi}2$. Für $k\ge1$ ist $\int_0^\pi x\cos kx\,\mathrm{d} x=\frac{(-1)^k-1}{k^2}$ und $\int_\pi^{2\pi}\cos kx\,\mathrm{d} x=0$, also $a_k=\frac{(-1)^k-1}{\pi k^2}$: $-\frac2{\pi k^2}$ für ungerades $k$, sonst 0. Weiter ist $\int_0^\pi x\sin kx\,\mathrm{d} x=-\frac{\pi(-1)^k}k$ und $\pi\int_\pi^{2\pi}\sin kx\,\mathrm{d} x=\frac{\pi((-1)^k-1)}k$, also $b_k=-\frac1k$. Damit

$$T_2f(x)=\frac{3\pi}4-\frac2\pi\cos x-\sin x-\frac12\sin2x,\qquad c_0=\frac{3\pi}4,\quad c_1=-\frac1\pi+\frac{\mathrm{i}}2,\quad c_2=\frac{\mathrm{i}}4.$$
:::
:::
