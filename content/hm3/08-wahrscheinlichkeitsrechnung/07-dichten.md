---
title: Stufe 6: Dichten
pfad: Elektrotechnik / 3. Semester / HöMa3 – Höhere Mathematik 3 / Wahrscheinlichkeitsrechnung
adresse: elektrotechnik/3-semester/hohere-mathematik-3/wahrscheinlichkeitsrechnung
knoten: Kapitel 8: Wahrscheinlichkeitsrechnung
order: 3180700
summary: Eine Lebensdauer kann jeden Wert annehmen, und jeder einzelne Wert hat die Wahrscheinlichkeit null.
tags: absolut stetig, Dichte, Standard-Normalverteilung, Borel-Algebra, Verteilung, Dirac-Masse
lang: de
---

<span class="anker" id="stufe-6"></span>

:::zweck
Eine Lebensdauer kann jeden Wert annehmen, und jeder einzelne Wert hat die Wahrscheinlichkeit null. Sinnvoll sind nur Intervalle. Diese Stufe ersetzt die Wahrscheinlichkeitsfunktion durch eine Dichte.
:::

**Die Idee.** Für die LED gilt $F_X(x)=1-\mathrm{e}^{-x/2}$ für $x\ge0$, ohne Sprünge. Formel [(4.2)](zufallsvariablen-und-verteilungsfunktion.html#gl-4-2) erinnert an den Hauptsatz: $F_X(b)-F_X(a)$ sieht aus wie das Integral einer Ableitung. Diese Ableitung misst, wie viel Wahrscheinlichkeit je Längeneinheit bei $x$ liegt.

:::definition Definition 6.1 (Absolut stetige Zufallsvariable)
<span class="anker" id="satz-6-1"></span>

$X$ heißt __absolut stetig__, wenn es eine nichtnegative integrierbare Funktion $f_X:\mathbb{R}\to[0,\infty)$ gibt mit

<span class="anker" id="gl-6-1"></span>
$$F_X(x)=\int_{-\infty}^xf_X(y)\,\mathrm{d} y\quad\text{für alle }x\in\mathbb{R}. \tag{6.1}$$

$f_X$ heißt __Dichte__ von $X$.
:::

⁠**So liest man das:** Der Begriff beschreibt die Verteilungsfunktion, nicht die Funktion $X$. Es gilt $\int_\mathbb{R} f_X\,\mathrm{d} x=1$, und $\mathbb{P}(a<X\le b)=\int_a^bf_X(x)\,\mathrm{d} x$ ist die Fläche unter der Dichte. Daraus folgt $\mathbb{P}(X=x)=0$ für jedes $x$, es spielt also keine Rolle, ob ein Intervall offen oder abgeschlossen ist. An Stetigkeitsstellen von $f_X$ ist $F_X'(x)=f_X(x)$. Die Dichte selbst ist keine Wahrscheinlichkeit und darf größer als 1 sein, erst $f_X(x)\,\mathrm{d} x$ ist ein Anteil.

::::beispiel [Beispiele]
Die LED hat $f_X(x)=\frac12\mathrm{e}^{-x/2}$ für $x\ge0$, sonst 0. Damit ist $\mathbb{P}(1<X\le3)=\mathrm{e}^{-1/2}-\mathrm{e}^{-3/2}\approx0{,}383$ (Abb. [6](#abb-6)). Weitere Standardfälle:

<ul>

<li>

⁠**Gleichverteilung** auf $[a,b]$: $f_X(x)=(b-a)^{-1}$ für $x\in[a,b]$, sonst 0. Gleich lange Teilintervalle sind gleich wahrscheinlich.

</li>

<li>

⁠**Normalverteilung** $X\sim\mathcal N(\mu,\sigma^2)$ mit $\mu\in\mathbb{R}$, $\sigma>0$:

<span class="anker" id="gl-6-2"></span>
$$f_X(x)=\frac1{\sigma\sqrt{2\pi}}\exp\Bigl(-\frac12\Bigl(\frac{x-\mu}\sigma\Bigr)^2\Bigr). \tag{6.2}$$

Für $\mu=0$, $\sigma=1$ heißt sie __Standard-Normalverteilung__. Mit $u=(x-\mu)/(\sigma\sqrt2)$ wird $\int_\mathbb{R} f_X\,\mathrm{d} x$ zum Gauß-Integral $\frac1{\sqrt\pi}\int_\mathbb{R}\mathrm{e}^{-u^2}\,\mathrm{d} u=1$. $\mu$ verschiebt die Glocke, $\sigma$ streckt sie. Mit dem $\sigma$ in $\sigma$-Algebra hat das nichts zu tun.

</li>

</ul>

:::abbildung hm3/k8dichte 6
Links die Dichte der LED mit der Fläche $\mathbb{P}(1<X\le3)$. Rechts Normalverteilungen mit $\mu=0$ und $\mu=2$: Jede Fläche ist 1, darum ist die schmale Glocke höher.
:::
::::

**Rechnen mit der Normalverteilung.** Die Verteilungsfunktion von $\mathcal N(0,1)$ heißt

<span class="anker" id="gl-6-3"></span>
$$\Phi(x):=\frac1{\sqrt{2\pi}}\int_{-\infty}^x\mathrm{e}^{-y^2/2}\,\mathrm{d} y \tag{6.3}$$

und hat keine geschlossene Form. Man liest sie aus einer Tabelle ab. Aus der Symmetrie der Glocke folgt $\Phi(-x)=1-\Phi(x)$.

| $x$ | 0,5 | 1 | 1,5 | 1,645 | 1,96 | 2 | 2,5 | 3 |
|---|---|---|---|---|---|---|---|---|
| $\Phi(x)$ | 0,6915 | 0,8413 | 0,9332 | 0,9500 | 0,9750 | 0,9772 | 0,9938 | 0,9987 |

Die Substitution $y=(t-\mu)/\sigma$ zeigt für $X\sim\mathcal N(\mu,\sigma^2)$: $\mathbb{P}(X\le x)=\Phi\bigl((x-\mu)/\sigma\bigr)$.

::::beispiel
Für das Netzteil sei $U\sim\mathcal N(5,\;0{,}2^2)$ in Volt. Dann ist $\mathbb{P}(4{,}8<U\le5{,}4)=\Phi(2)-\Phi(-1)\approx0{,}9772-0{,}1587=0{,}8185$.
::::

**Der Raum dahinter.** Zu einer stetigen Dichte $f$ auf $\Omega=\mathbb{R}$ möchte man $\mathbb{P}(A):=\int_Af(x)\,\mathrm{d} x$ setzen. Für offene Intervalle und endliche Vereinigungen davon ist das ein Integral aus [Kapitel 2](/wissen/elektrotechnik/3-semester/hohere-mathematik-3/integralrechnung-im-rn/integralrechnung-im-rn.html). Diese Mengen bilden aber keine $\sigma$-Algebra, auch wenn man auf „offen“ verzichtet: Abzählbar viele Intervalle vereinigen sich im Allgemeinen nicht zu einer endlichen Vereinigung. Die kleinste $\sigma$-Algebra, die alle offenen Intervalle enthält, heißt __Borel-Algebra__ $\mathcal B$. Die Lebesguesche Integrationstheorie erlaubt das Integrieren über alle Mengen aus $\mathcal B$, das ergibt den Raum $(\mathbb{R},\mathcal B,\mathbb{P})$. Ebenso beschreibt $\mathbb{P}(A)=\int_A|\psi(\boldsymbol{x})|^2\,\mathrm{d}\boldsymbol{x}$ die Aufenthaltswahrscheinlichkeit eines Quantenteilchens mit Wellenfunktion $\psi:\mathbb{R}^3\to\mathbb{C}$, $\int_{\mathbb{R}^3}|\psi|^2\,\mathrm{d}\boldsymbol{x}=1$.

Für jede Zufallsvariable $X$ ist die __Verteilung__ das Wahrscheinlichkeitsmaß auf $\mathbb{R}$

<span class="anker" id="gl-6-4"></span>
$$\mathbb{P}_X(A)=\mathbb{P}(X\in A)=\mathbb{P}(\{\omega\in\Omega:X(\omega)\in A\}),\quad A\in\mathcal B. \tag{6.4}$$

Sie löst $X$ vom ursprünglichen $\Omega$ und sagt, mit welcher Wahrscheinlichkeit $X$ in einem Bereich liegt. Es gilt $\mathbb{P}_X((a,b])=F_X(b)-F_X(a)$, im absolut stetigen Fall also $\int_a^bf_X\,\mathrm{d} x$, und im diskreten Fall $\mathbb{P}_X(A)=\sum_{x_k\in A}p_X(x_k)$.

Beide Fälle lassen sich formal vereinen. Eine __Dirac-Masse__ $\delta_c$ legt das Gewicht 1 in den Punkt $c$: $\int_A\delta_c(\mathrm{d} x)$ ist 1 für $c\in A$, sonst 0. Ersetzt man $f(x)\,\mathrm{d} x$ durch $\sum_ip_i\,\delta_{\omega_i}(\mathrm{d} x)$, wird aus $\int_Af(x)\,\mathrm{d} x$ die Summe $\sum_{\omega_i\in A}p_i$. Die Konstante $X\equiv c$ ist nicht absolut stetig, sie hat nur die singuläre Dichte $\delta_c$. **Grenzfall:** Für $\sigma\to0$ zieht sich die Glocke zu $\delta_\mu$ zusammen.

**Neue Variable aus alter.** Für $Y=g(X)$ geht man über $F_Y$: $\{g(X)\le y\}$ nach $X$ umformen, dann ableiten. Ist $X$ gleichverteilt auf $[0,1)$ und $Y=-2\ln(1-X)$, gilt $\{Y\le y\}=\{X\le1-\mathrm{e}^{-y/2}\}$ für $y\ge0$, also $F_Y(y)=1-\mathrm{e}^{-y/2}$, die Lebensdauer der LED. So erzeugt ein Rechner aus gleichverteilten Zufallszahlen andere Verteilungen.

:::aufgabe Aufgabe 9 ★ Normieren
<span class="anker" id="aufg-9"></span>

Sei $f(x)=c\,x(2-x)$ für $x\in[0,2]$ und 0 sonst. Bestimme $c$ so, dass $f$ eine Dichte ist, dazu $F_X$ und $\mathbb{P}(X>\frac32)$.

:::loesung
$\int_0^2x(2-x)\,\mathrm{d} x=\frac43$, also $c=\frac34$. Für $x\in[0,2]$ ist $F_X(x)=\frac34(x^2-\frac{x^3}3)$, links davon 0, rechts davon 1. $\mathbb{P}(X>\frac32)=1-\frac34(\frac94-\frac98)=\frac5{32}$.
:::
:::

:::aufgabe Aufgabe 10 ★★ Transformieren
<span class="anker" id="aufg-10"></span>

Sei $X$ gleichverteilt auf $(0,1]$. Bestimme Verteilungsfunktion und Dichte von (a) $Y=X^2$ und (b) $Z=1/X$.

:::loesung
(a) Für $y\in(0,1]$ ist $F_Y(y)=\mathbb{P}(X\le\sqrt y)=\sqrt y$, also $f_Y(y)=\frac1{2\sqrt y}$. Für $y\le0$ ist $F_Y=0$, für $y\ge1$ ist $F_Y=1$. Die Dichte ist bei 0 unbeschränkt, ihr Integral bleibt 1. (b) Für $z\ge1$ ist $F_Z(z)=\mathbb{P}(X\ge1/z)=1-\frac1z$, also $f_Z(z)=\frac1{z^2}$. Für $z<1$ ist beides null.
:::
:::
