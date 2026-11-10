---
title: Stufe 5: Die beste Näherung
pfad: Elektrotechnik / 3. Semester / HöMa3 – Höhere Mathematik 3 / Fourier-Reihen
adresse: elektrotechnik/3-semester/hohere-mathematik-3/fourier-reihen
knoten: Kapitel 7: Fourier-Reihen
order: 3170600
summary: Warum gerade die Zahlen c k ?
tags: Projektion, trigonometrischen Polynome, Projektionsoperator, Besselsche Ungleichung, Lemma von Riemann-Lebesgue
lang: de
---

<span class="anker" id="stufe-5"></span>

:::zweck
Warum gerade die Zahlen $c_k$? Diese Stufe zeigt, dass keine andere Wahl von Faktoren im quadratischen Mittel näher an $f$ herankommt.
:::

**Die Idee.** Der Punkt einer Ebene, der einem Punkt im Raum am nächsten liegt, ist der Fußpunkt des Lots. Im $\mathbb{R}^n$ heißt das __Projektion__: Ist $\hat{\boldsymbol{e}}_1,\dots,\hat{\boldsymbol{e}}_m$ eine Orthonormalbasis eines Unterraums, hat $\boldsymbol v'=\sum_{k=1}^m(\boldsymbol v\cdot\hat{\boldsymbol{e}}_k)\,\hat{\boldsymbol{e}}_k$ den kleinsten Abstand zu $\boldsymbol v$, und $\boldsymbol v-\boldsymbol v'$ steht senkrecht auf dem Unterraum. Das Fourier-Polynom [(2.2)](koeffizienten-und-polynome.html#gl-2-2) hat genau diese Form.

**Der Unterraum.** Die __trigonometrischen Polynome__ vom Grad $\le N$ bilden den Raum $\mathcal V_N$ aller

$$S_N=\sum_{|k|\le N}\lambda_k\hat{\boldsymbol{e}}_k,\qquad\text{also}\quad S_N(x)=\sum_{|k|\le N}\lambda_k\mathrm{e}^{\mathrm{i}kx},\qquad(\lambda_{-N},\dots,\lambda_N)\in\mathbb{C}^{2N+1}.$$

Das ist ein komplexer Vektorraum der Dimension $2N+1$. Die Zahlen $\lambda_k$ sind Koordinaten, die $\hat{\boldsymbol{e}}_k$ eine orthonormale Basis. Deshalb misst man Längen wie in $\mathbb{C}^{2N+1}$:

<span class="anker" id="gl-5-1"></span>
$$\|S_N\|_2^2=\sum_{|k|\le N}\sum_{|\ell|\le N}\lambda_k\overline{\lambda_\ell}\,\langle\hat{\boldsymbol{e}}_k,\hat{\boldsymbol{e}}_\ell\rangle=\sum_{|k|\le N}\sum_{|\ell|\le N}\lambda_k\overline{\lambda_\ell}\,\delta_{k\ell}=\sum_{|k|\le N}|\lambda_k|^2. \tag{5.1}$$

Die Abbildung $T_N:f\mapsto T_Nf=\sum_{|k|\le N}\langle f,\hat{\boldsymbol{e}}_k\rangle\hat{\boldsymbol{e}}_k\in\mathcal V_N$ heißt __Projektionsoperator__ (Abb. [5](#abb-5)).

:::abbildung hm3/k7projektion 5
Die Funktion $f$ als Punkt über dem Unterraum $\mathcal V_N$. Der Fußpunkt des Lots ist $T_Nf$. Für jedes andere $S_N$ aus $\mathcal V_N$ entsteht ein rechtwinkliges Dreieck, und die Hypotenuse $f-S_N$ ist länger als die Kathete $f-T_Nf$.
:::

:::satz Satz 5.1 (Bestapproximation)
<span class="anker" id="satz-5-1"></span>

Sei $f$ wie in Definition [2.1](koeffizienten-und-polynome.html#satz-2-1). Für alle $N\in\mathbb{N}_0$ und alle $S_N\in\mathcal V_N$ gilt

<ol class="rm">

<li>

$\|f-S_N\|_2^2=\|f-T_Nf\|_2^2+\|T_Nf-S_N\|_2^2$ (Pythagoras),

</li>

<li>

$\|f-S_N\|_2^2\ge\|f-T_Nf\|_2^2$ (Bestapproximation im quadratischen Mittel, auch $L^2$-Bestapproximation),

</li>

<li>

$\|f-T_Nf\|_2^2=\|f\|_2^2-\|T_Nf\|_2^2$,

</li>

<li>

$\|T_Nf\|_2^2\le\|f\|_2^2$ (__Besselsche Ungleichung__).

</li>

</ol>
:::

:::beweis Lot und Pythagoras
Für $|k|\le N$ ist $\langle f-T_Nf,\hat{\boldsymbol{e}}_k\rangle=c_k-c_k=0$, denn von $T_Nf$ bleibt nach Satz [1.2](schwingungen-als-bausteine.html#satz-1-2) nur der Summand mit $\hat{\boldsymbol{e}}_k$. Also steht $f-T_Nf$ senkrecht auf jeder Linearkombination der $\hat{\boldsymbol{e}}_k$, insbesondere auf $T_Nf-S_N\in\mathcal V_N$. Für $\langle a,b\rangle=0$ gilt $\|a+b\|_2^2=\|a\|_2^2+\|b\|_2^2$. Mit $a=f-T_Nf$ und $b=T_Nf-S_N$ folgt (i), und daraus (ii). Mit $S_N=0$ folgt (iii), und wegen $\|f-T_Nf\|_2^2\ge0$ auch (iv).
:::

⁠**So liest man das:** (ii) sagt, dass $T_Nf$ den quadratischen Abstand minimiert, und (i) zeigt, dass jedes andere $S_N$ um $\|T_Nf-S_N\|_2^2$ schlechter ist. Mit [(5.1)](#gl-5-1) lautet die Besselsche Ungleichung konkret

<span class="anker" id="gl-5-2"></span>
$$\sum_{|k|\le N}|c_k|^2\le\frac1{2\pi}\int_0^{2\pi}|f(x)|^2\,\mathrm{d} x. \tag{5.2}$$

Die rechte Seite hängt nicht von $N$ ab. Also konvergiert $\sum_k|c_k|^2$, und die $c_k$ bilden eine Nullfolge. Für jede Riemann-integrierbare $f$ gilt damit das __Lemma von Riemann-Lebesgue__

<span class="anker" id="gl-5-3"></span>
$$\lim_{|k|\to\infty}\int_0^{2\pi}f(x)\,\mathrm{e}^{\mathrm{i}kx}\,\mathrm{d} x=0. \tag{5.3}$$

Auch $a_k$ und $b_k$ gehen deshalb gegen null. Der Mechanismus: Eine schnelle Schwingung pendelt so rasch, dass sich ihre Beiträge gegen das langsamere $f$ wegheben.

::::beispiel Rechteck, $N=1$
Es ist $T_1q=\frac4\pi\sin x$, $\|q\|_2^2=1$ und $\|T_1q\|_2^2=\frac12\cdot\frac{16}{\pi^2}=\frac8{\pi^2}\approx0{,}811$. Nach (iii) ist $\|q-T_1q\|_2^2\approx0{,}189$. Der Vergleichskandidat $S_1=\sin x$ gibt $\|q-S_1\|_2^2=\frac32-\frac4\pi\approx0{,}227$. Die Differenz $0{,}037$ ist genau $\|T_1q-S_1\|_2^2=\frac12(\frac4\pi-1)^2$.
::::

⁠**Grenzfall:** Liegt $f$ schon in $\mathcal V_N$, ist $T_Nf=f$ und der Abstand null.

:::frage Muss ich alle Koeffizienten neu rechnen, wenn ich $N$ erhöhe?
Nein. $c_k$ hängt nicht von $N$ ab, weil die Bausteine senkrecht aufeinander stehen: Ein neuer Baustein ändert die Anteile längs der alten nicht. Das ist der Vorteil einer orthogonalen Basis gegenüber einer beliebigen.
:::

:::frage Ist $T_Nf$ an jeder Stelle die beste Näherung?
Nein. Bestapproximation meint das Integral über die Periode. An der Stelle $\frac\pi2$ trifft $\sin x$ das Rechteck exakt, $T_1q$ liegt mit $1{,}27$ daneben. Dafür ist $T_1q$ im Mittel näher.
:::

:::aufgabe Aufgabe 5 ★★ Abstände rechnen
<span class="anker" id="aufg-5"></span>

<ol class="al">

<li>

Berechne $\|w\|_2^2$, dann $\|w-\frac\pi2\|_2^2$ und $\|w-T_1w\|_2^2$ mit Satz [5.1](#satz-5-1). Wie viel des Fehlers beseitigt die erste Schwingung?

</li>

<li>

Schreibe $\|q-\lambda\sin x\|_2^2$ als Polynom in $\lambda\in\mathbb{R}$ und bestimme das Minimum. Welche bekannte Zahl kommt heraus?

</li>

<li>

Zeige: Ableiten bildet $\mathcal V_N$ in sich ab. Welche Matrix gehört in der Basis $\hat{\boldsymbol{e}}_{-N},\dots,\hat{\boldsymbol{e}}_N$ dazu?

</li>

</ol>

:::loesung
(a) $\|w\|_2^2=\frac1{2\pi}\int_{-\pi}^\pi x^2\,\mathrm{d} x=\frac{\pi^2}3$. Mit $T_0w=\frac\pi2$ ist nach (iii) $\|w-\frac\pi2\|_2^2=\frac{\pi^2}3-\frac{\pi^2}4=\frac{\pi^2}{12}\approx0{,}822$. Für $T_1w=\frac\pi2-\frac4\pi\cos x$ ist $\|T_1w\|_2^2=\frac{\pi^2}4+\frac8{\pi^2}$, also $\|w-T_1w\|_2^2=\frac{\pi^2}{12}-\frac8{\pi^2}\approx0{,}012$. Die erste Schwingung beseitigt rund $98{,}6\,\%$ des Fehlers. (b) Mit $\langle q,\sin\rangle=\frac{b_1}2=\frac2\pi$ ist $\|q-\lambda\sin x\|_2^2=1-\frac{4\lambda}\pi+\frac{\lambda^2}2$. Das Minimum liegt bei $\lambda=\frac4\pi=b_1$. (c) $S_N'=\sum_{|k|\le N}\mathrm{i}k\,\lambda_k\hat{\boldsymbol{e}}_k$ liegt in $\mathcal V_N$. Die Matrix ist die Diagonalmatrix mit den Einträgen $-\mathrm{i}N,\dots,0,\dots,\mathrm{i}N$. Der Eintrag 0 gehört zu den Konstanten.
:::
:::
