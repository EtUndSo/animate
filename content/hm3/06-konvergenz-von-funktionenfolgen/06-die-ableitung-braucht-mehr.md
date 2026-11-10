---
title: Stufe 4: Die Ableitung braucht mehr
pfad: Elektrotechnik / 3. Semester / HöMa3 – Höhere Mathematik 3 / Konvergenz von Funktionenfolgen
adresse: elektrotechnik/3-semester/hohere-mathematik-3/konvergenz-von-funktionenfolgen
knoten: Kapitel 6: Konvergenz von Funktionenfolgen
order: 3160600
summary: Gleichmäßige Konvergenz kontrolliert die Höhe einer Kurve, nicht ihre Steigung.
tags: 
lang: de
---

<span class="anker" id="stufe-4"></span>

:::zweck
Gleichmäßige Konvergenz kontrolliert die Höhe einer Kurve, nicht ihre Steigung. Diese Stufe zeigt, was man für das Ableiten zusätzlich braucht.
:::

**Die Idee.** Die Rippel $w_n$ streben gleichmäßig gegen 0. Ihre Ableitungen $w_n'(x)=\cos(nx)$ erreichen aber für jedes $n$ den Betrag 1 (Abb. [4](#abb-4)). Bei $x=0$ ist $w_n'(0)=1$ für alle $n$, die Grenzfunktion hat dort die Ableitung 0. Der Mechanismus: Steigung ist Höhe mal Frequenz, und die Höhe $1/n$ wird durch die Frequenz $n$ genau ausgeglichen. Ableiten verstärkt kleine schnelle Störungen, Integrieren glättet sie. Das kennt man vom Kondensator: Sein Strom folgt der Ableitung der Spannung, eine kleine hochfrequente Störung der Spannung kann einen großen Strom bewirken.

:::abbildung hm3/k6rippel 4
Links die Rippel $w_4$ und $w_{16}$: Die Höhe sinkt mit $1/n$. Rechts ihre Ableitungen $\cos(4x)$ und $\cos(16x)$: Die Höhe bleibt 1, nur die Schwingung wird schneller.
:::

Der Ausweg nutzt Stufe [3](stetigkeit-und-integral-bleiben-erhalten.html#stufe-3): Integrale dürfen tauschen. Also schreibt man $f_n$ mit dem Hauptsatz als Integral seiner Ableitung und verlangt die Kontrolle für die Ableitungen.

:::satz Satz 4.1 (Ableitung und Grenzwert)
<span class="anker" id="satz-4-1"></span>

Sei $(f_n)_{n\in\mathbb{N}}$ eine Folge stetig differenzierbarer Funktionen auf $[a,b]$ mit

$$f_n\to f\ \text{ punktweise auf }[a,b]\quad\text{und}\quad(f_n')_{n\in\mathbb{N}}\ \text{ gleichmäßig konvergent auf }[a,b].$$

Dann ist $f$ stetig differenzierbar auf $[a,b]$, und $f'(x)=\lim_{n\to\infty}f_n'(x)$.
:::

:::beweis Über das Integral
⁠**Schritt 1: $f_n$ konvergiert gleichmäßig.** Nach dem Hauptsatz ist

<span class="anker" id="gl-4-1"></span>
$$f_n(x)=f_n(a)+\int_a^xf_n'(y)\,\mathrm{d} y. \tag{4.1}$$

Mit der Dreiecksungleichung und der Monotonie des Integrals folgt

$$\sup_{x\in[a,b]}|f_n(x)-f_m(x)|\le|f_n(a)-f_m(a)|+\int_a^b|f_n'(y)-f_m'(y)|\,\mathrm{d} y.$$

Der erste Summand strebt für $m,n\to\infty$ gegen null, weil $f_n(a)$ konvergiert. Der zweite ist höchstens $(b-a)\sup_y|f_n'(y)-f_m'(y)|$ und strebt nach dem Cauchy-Kriterium für die Folge $f_n'$ gegen null. Also konvergiert $f_n$ nach Satz [2.2](gleichmaige-konvergenz.html#satz-2-2) gleichmäßig, und der Grenzwert ist die punktweise Grenzfunktion $f$.

⁠**Schritt 2: Grenzübergang.** Sei $f^*$ der gleichmäßige Grenzwert von $f_n'$. Die $f_n'$ sind stetig, also ist $f^*$ nach Satz [3.1](stetigkeit-und-integral-bleiben-erhalten.html#satz-3-1) stetig. In [(4.1)](#gl-4-1) darf man nach Satz [3.2](stetigkeit-und-integral-bleiben-erhalten.html#satz-3-2) zum Grenzwert gehen:

$$f(x)=f(a)+\int_a^xf^*(y)\,\mathrm{d} y.$$

⁠**Schritt 3: Hauptsatz.** Der Integrand $f^*$ ist stetig. Nach dem Hauptsatz ist $f$ stetig differenzierbar mit $f'=f^*$.
:::

⁠**So liest man das:** Die gleichmäßige Bedingung betrifft die Ableitungen. Von $f_n$ selbst braucht man wenig: Schritt 1 benutzt nur die Stelle $x=a$. Die gleichmäßige Konvergenz von $f_n$ ist ein Ergebnis, keine Voraussetzung.

**Warum jede Voraussetzung nötig ist.** Fehlt die gleichmäßige Konvergenz der Ableitungen, wird der Satz falsch: Bei den Rippeln ist $f=0$, aber $w_n'(\pi)=(-1)^n$ konvergiert gar nicht. Fehlt die Konvergenz der $f_n$, dann ebenfalls: Für $f_n(x)=n$ konvergiert $f_n'=0$ gleichmäßig, $f_n$ aber nirgends.

⁠**Grenzfall:** Macht man die Höhe schneller klein, greift der Satz. Für $f_n(x)=x^2+\frac{1}{n^2}\sin(nx)$ ist $f_n'(x)=2x+\frac1n\cos(nx)$, und das konvergiert wegen $|\frac1n\cos(nx)|\le\frac1n$ gleichmäßig gegen $2x$. Also ist $f(x)=x^2$ mit $f'(x)=2x$, wie es sein muss.

:::frage $w_n$ konvergiert doch gleichmäßig, und $f=0$ ist differenzierbar. Reicht das nicht?
Nein. Bei den Rippeln existiert $f'=0$, aber die Folge der Ableitungen konvergiert nicht dagegen. Der Satz verlangt deshalb etwas von den Ableitungen, nicht von der Grenzfunktion.
:::

:::aufgabe Aufgabe 4 ★★ Es entsteht ein Knick
<span class="anker" id="aufg-4"></span>

Sei $f_n(x)=|x|^{1+1/n}$ auf $[-1,1]$.

<ol class="al">

<li>

Zeige, dass $f_n$ stetig differenzierbar ist, und gib $f_n'$ an.

</li>

<li>

Zeige $\sup_x\bigl|f_n(x)-|x|\bigr|\le1/(n+1)$.

</li>

<li>

Warum ist Satz [4.1](#satz-4-1) nicht anwendbar? Welche Voraussetzung fehlt?

</li>

</ol>

:::loesung
(a) Für $x>0$ ist $f_n'(x)=(1+\frac1n)x^{1/n}$, für $x<0$ ist $f_n'(x)=-(1+\frac1n)|x|^{1/n}$. Bei $x=0$ ist der Differenzenquotient $|h|^{1+1/n}/h$ dem Betrag nach $|h|^{1/n}\to0$, also $f_n'(0)=0$. Wegen $|x|^{1/n}\to0$ für $x\to0$ ist $f_n'$ stetig. (b) Wegen der Symmetrie reicht $x\in[0,1]$. Mit $t=x^{1/n}$ ist $x-x^{1+1/n}=t^n(1-t)$. Das Maximum liegt bei $t=n/(n+1)$ und ist $(n/(n+1))^n/(n+1)\le1/(n+1)$. (c) $f_n'(x)\to\operatorname{sgn}(x)$ punktweise. Die $f_n'$ sind stetig, die Grenzfunktion springt, also konvergiert $f_n'$ nach Satz [3.1](stetigkeit-und-integral-bleiben-erhalten.html#satz-3-1) nicht gleichmäßig. Diese Voraussetzung fehlt. Das passt dazu, dass $|x|$ bei 0 nicht differenzierbar ist.
:::
:::
