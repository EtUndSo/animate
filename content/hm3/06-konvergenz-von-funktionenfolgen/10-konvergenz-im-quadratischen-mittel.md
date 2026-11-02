---
title: Stufe 8: Konvergenz im quadratischen Mittel
pfad: Elektrotechnik / 3. Semester / Höhere Mathematik 3 / Konvergenz von Funktionenfolgen
order: 3161000
summary: Diese Stufe misst den Abstand zweier Funktionen durch eine Fläche, in der ein schmaler Bereich kaum zählt, und zeigt, dass dieser Abstand aus einem Skalarprodukt stammt.
tags: R-integrierbar, Konvergenz im quadratischen Mittel, Skalarprodukt, L^2-Konvergenz, orthogonal, Legendre-Polynome, Lebesgue-Integral, fast überall
lang: de
---

<span class="anker" id="stufe-8"></span>

:::zweck
Diese Stufe misst den Abstand zweier Funktionen durch eine Fläche, in der ein schmaler Bereich kaum zählt, und zeigt, dass dieser Abstand aus einem Skalarprodukt stammt.
:::

**Die Idee.** Gleichmäßige Konvergenz passt, wenn man glatte Funktionen durch Potenzreihen darstellt, etwa durch Taylorreihen. Für Funktionen mit Sprüngen passt sie nicht. Sei $\operatorname{sgn}(x)=1$ für $x>0$, $-1$ für $x<0$ und $0$ für $x=0$. Nähere diesen Rechteckverlauf auf $[-1,1]$ durch die stetigen Rampen $v_n(x)=\max(-1,\min(1,nx))$ an. Die Näherung wird sichtbar besser, doch der größte Abstand bleibt 1. Gleichmäßig kann die Konvergenz nach Satz [3.1](stetigkeit-und-integral-bleiben-erhalten.html#satz-3-1) auch nicht sein (Abb. [8](#abb-8)). Der Fehler sitzt aber auf einem immer schmaleren Stück. Man misst ihn deshalb durch das Integral des quadrierten Fehlers. Es ist proportional zur Energie, die ein Fehlersignal in einem Widerstand umsetzt.

:::abbildung hm3/k6mittel 8
Links der Rechteckverlauf (rot) und die Rampen $v_2$, $v_6$. Rechts die quadrierte Abweichung $|v_6-\operatorname{sgn}|^2$: Ihre Höhe bleibt nahe 1, ihre Fläche ist $2/(3n)$ und schrumpft.
:::

:::definition Definition 8.1 (Konvergenz im quadratischen Mittel)
<span class="anker" id="satz-8-1"></span>

Eine beschränkte Funktion heißt __R-integrierbar__, wenn ihre Riemann-Summen für immer feinere Zerlegungen gegen denselben Wert streben. Der Vektorraum dieser Funktionen auf $[a,b]$ mit Werten in $\mathbb{C}$ heißt $\mathcal R([a,b];\mathbb{C})$. Seien $f_n,f\in\mathcal R([a,b];\mathbb{C})$. __Konvergenz im quadratischen Mittel__ der Folge gegen $f$ heißt

<span class="anker" id="gl-8-1"></span>
$$\lim_{n\to\infty}\int_a^b|f_n(x)-f(x)|^2\,\mathrm{d} x=0. \tag{8.1}$$
:::

⁠**So liest man das:** $\mathcal R([a,b];\mathbb{C})$ enthält alle stetigen und stückweise stetigen Funktionen. Die Verkettung $g\circ f$ einer R-integrierbaren Funktion $f$ mit einer stetigen Funktion $g$ ist wieder R-integrierbar, insbesondere $|f|^2$. Das Integral in [(8.1)](#gl-8-1) existiert also. Für die Rampen ist es $2\int_0^{1/n}(1-nx)^2\,\mathrm{d} x=\frac{2}{3n}\to0$.

**Vergleich.** Für beschränkte $f_n,f$ gilt $\int_a^b|f_n-f|^2\,\mathrm{d} x\le(b-a)\sup_x|f_n(x)-f(x)|^2$. Gleichmäßige Konvergenz stetiger Funktionen zieht also die Konvergenz im quadratischen Mittel nach sich. Die Umkehrung ist falsch: Bei den Entladekurven ist $\int_0^1\mathrm{e}^{-2nx}\,\mathrm{d} x=(1-\mathrm{e}^{-2n})/(2n)\to0$ ohne gleichmäßige Konvergenz. Punktweise Konvergenz genügt ebenfalls nicht: $\int_0^1b_n^2\,\mathrm{d} x=\frac n4\bigl(1-(1+2n+2n^2)\mathrm{e}^{-2n}\bigr)\to\infty$. Umgekehrt folgt aus [(8.1)](#gl-8-1) nicht die punktweise Konvergenz: Läuft ein Rechteck der Höhe 1 immer wieder über $[0,1]$ und wird dabei schmaler (Breiten $1,\frac12,\frac12,\frac14,\frac14,\frac14,\frac14,\dots$), strebt die Fläche gegen null, aber an jeder Stelle kommen die Werte 1 und 0 unendlich oft vor.

| Folge | punktweise | gleichmäßig | quadr. Mittel | $\int f_n\to0$ |
|---|---|---|---|---|
| Rippel $w_n$ | ja | ja | ja | ja |
| Entladekurven $u_n$ | ja | nein | ja | ja |
| Beulen $b_n$ | ja | nein | nein | nein |
| laufendes Rechteck | nein | nein | ja | ja |

**Das Skalarprodukt.** Für $f,g\in\mathcal R([a,b];\mathbb{C})$ definiert man das hermitesche __Skalarprodukt__ und die zugehörige Länge

<span class="anker" id="gl-8-2"></span>
$$\langle f,g\rangle:=\frac1{b-a}\int_a^bf(x)\,\overline{g(x)}\,\mathrm{d} x,\qquad\|f\|_2^2:=\langle f,f\rangle=\frac1{b-a}\int_a^b|f(x)|^2\,\mathrm{d} x. \tag{8.2}$$

⁠**So liest man das:** $\|f\|_2$ ist der Effektivwert von $f$ auf $[a,b]$. Für $f(x)=x$ auf $[-1,1]$ ist $\|f\|_2^2=\frac13$. Der Strich ist die komplexe Konjugation. Er macht $\langle f,f\rangle$ reell und nicht negativ, und es gilt $\langle g,f\rangle=\overline{\langle f,g\rangle}$, das heißt hermitesch. Der Faktor $1/(b-a)$ ist für die Konvergenz unerheblich, auf unbeschränkten Gebieten lässt man ihn weg. Es gilt $f_n\to f$ im quadratischen Mittel genau dann, wenn $\|f_n-f\|_2\to0$. Deshalb heißt dieser Begriff auch __$L^2$-Konvergenz__. Für die Rampen ist $\|v_n-\operatorname{sgn}\|_2^2=\frac{1}{3n}$. Gilt $\langle f,g\rangle=0$, heißen $f,g$ __orthogonal__. Systeme solcher Funktionen sind das Werkzeug der Näherung im quadratischen Mittel, etwa die __Legendre-Polynome__ $1$, $x$, $\frac12(3x^2-1)$ auf $[-1,1]$.

Streng genommen ist $\|\cdot\|_2$ auf $\mathcal R([a,b];\mathbb{C})$ keine Norm: Jede Funktion, die nur an endlich vielen Stellen von null abweicht, hat $\|f\|_2=0$. Die übrigen Eigenschaften gelten.

:::satz Satz 8.2 (Cauchy-Schwarz und Dreiecksungleichung)
<span class="anker" id="satz-8-2"></span>

Für $f,g\in\mathcal R([a,b];\mathbb{C})$ gilt $|\langle f,g\rangle|\le\|f\|_2\,\|g\|_2$ und $\|f+g\|_2\le\|f\|_2+\|g\|_2$.
:::

:::beweis Ein Quadrat ist nicht negativ
Für jedes $\lambda\in\mathbb{C}$ ist $0\le\|f-\lambda g\|_2^2=\|f\|_2^2-2\operatorname{Re}(\overline\lambda\langle f,g\rangle)+|\lambda|^2\|g\|_2^2$. Ist $\|g\|_2>0$, gibt $\lambda=\langle f,g\rangle/\|g\|_2^2$ die Ungleichung $0\le\|f\|_2^2-|\langle f,g\rangle|^2/\|g\|_2^2$. Ist $\|g\|_2=0$, gibt $\lambda=t\langle f,g\rangle$ für alle $t>0$ die Ungleichung $0\le\|f\|_2^2-2t|\langle f,g\rangle|^2$, also $\langle f,g\rangle=0$. Die Dreiecksungleichung folgt aus $\|f+g\|_2^2=\|f\|_2^2+2\operatorname{Re}\langle f,g\rangle+\|g\|_2^2\le(\|f\|_2+\|g\|_2)^2$.
:::

:::satz Satz 8.3 (Integral und quadratisches Mittel)
<span class="anker" id="satz-8-3"></span>

Seien $f_n,f\in\mathcal R([a,b];\mathbb{C})$ und $f_n\to f$ im quadratischen Mittel auf $[a,b]$. Dann gilt $\lim_{n\to\infty}\int_a^bf_n\,\mathrm{d} x=\int_a^bf\,\mathrm{d} x$.
:::

:::beweis Cauchy-Schwarz mit der Eins
Aus der Monotonie des Integrals und Satz [8.2](#satz-8-2) mit $h=|f_n-f|$ und der Funktion $1$ folgt

$$\Bigl|\int_a^bf_n\,\mathrm{d} x-\int_a^bf\,\mathrm{d} x\Bigr|\le\int_a^b|f_n-f|\,\mathrm{d} x\le(b-a)^{1/2}\Bigl(\int_a^b|f_n-f|^2\,\mathrm{d} x\Bigr)^{1/2}\to0.$$
:::

⁠**So liest man das:** Der Faktor $(b-a)^{1/2}$ zeigt, dass das Intervall endlich sein muss. Die Funktionen aus Aufgabe [3](stetigkeit-und-integral-bleiben-erhalten.html#aufg-3) haben $\int_0^\infty f_n^2\,\mathrm{d} x=\frac{1}{2n}\to0$, ihr Integral bleibt aber 1.

**Der Raum $L^2$.** Eine Folge in $\mathcal R$ mit $\|f_m-f_n\|_2\to0$ muss weder punktweise konvergieren noch eine beschränkte Grenzfunktion haben. Das zeigt $f_n(x)=\min(n,x^{-1/4})$ auf $[0,1]$ mit $f_n(0)=n$: Die Bedingung gilt, der Grenzwert $x^{-1/4}$ ist unbeschränkt. Eine Integralnorm sieht einzelne Stellen nicht: Der Wert an einer Sprungstelle ändert kein Integral. Man ergänzt deshalb die fehlenden Grenzwerte: Der Raum $L^2((a,b);\mathbb{C})$ besteht aus den Folgen mit $\|f_m-f_n\|_2\to0$, und Folgen, deren Differenz bezüglich $\|\cdot\|_2$ eine Nullfolge ist, gelten als gleich. Konkret sind das die quadratisch Lebesgue-integrierbaren Funktionen. Das __Lebesgue-Integral__ erweitert das Riemann-Integral auf viel unregelmäßigere Funktionen. Zwei Funktionen gelten als gleich, wenn sie __fast überall__ übereinstimmen, also außer auf einer Menge, die sich durch abzählbar viele Intervalle beliebig kleiner Gesamtlänge überdecken lässt. Dieser Raum ist nach Konstruktion vollständig. Weil seine Norm aus einem Skalarprodukt stammt, heißt er __Hilbertraum__.

:::aufgabe Aufgabe 11 ★★ Zelte
<span class="anker" id="aufg-11"></span>

Sei $z_n(x)=h_n\max(0,\,1-|nx-1|)$ auf $[0,1]$ für $n\ge2$: ein Zelt der Höhe $h_n$ und der Breite $2/n$ mit Spitze bei $x=1/n$. Untersuche für (a) $h_n=1$, (b) $h_n=\sqrt n$, (c) $h_n=n$ die punktweise und gleichmäßige Konvergenz, die Konvergenz im quadratischen Mittel und den Grenzwert von $\int_0^1z_n\,\mathrm{d} x$.

:::loesung
In allen Fällen ist $z_n(0)=0$, und für $x>0$ ist $z_n(x)=0$ ab $n\ge2/x$. Die Grenzfunktion ist 0. Weiter ist $\sup_x|z_n(x)|=h_n$, $\int_0^1z_n\,\mathrm{d} x=h_n/n$ und $\int_0^1z_n^2\,\mathrm{d} x=\frac{2h_n^2}{3n}$. (a) $h_n=1$: nicht gleichmäßig, $\int z_n^2=\frac{2}{3n}\to0$, also im quadratischen Mittel, und $\int z_n=\frac1n\to0$. (b) $h_n=\sqrt n$: nicht gleichmäßig, $\int z_n^2=\frac23$, also nicht im quadratischen Mittel. Trotzdem ist $\int z_n=1/\sqrt n\to0$. (c) $h_n=n$: nicht gleichmäßig, $\int z_n^2=\frac{2n}3\to\infty$, und $\int z_n=1\not\to0$. Das Integral der Grenzfunktion ist 0. Nach Satz [8.3](#satz-8-3) kann also keine Konvergenz im quadratischen Mittel vorliegen.
:::
:::

:::aufgabe Aufgabe 12 ★★ Auf stetigen Funktionen
<span class="anker" id="aufg-12"></span>

<ol class="al">

<li>

Zeige, dass $\|\cdot\|_2$ auf $C^0([a,b];\mathbb{C})$ eine Norm ist: Aus $\|f\|_2=0$ folgt $f=0$.

</li>

<li>

Zeige mit den Rampen $v_n$, dass $C^0([-1,1];\mathbb{C})$ mit $\|\cdot\|_2$ nicht vollständig ist.

</li>

</ol>

:::loesung
(a) Sei $f(x_0)\neq0$. Wegen der Stetigkeit gilt $|f(x)|\ge\frac12|f(x_0)|$ auf einem Intervall der Länge $\ell>0$. Also ist $\|f\|_2^2\ge\frac{\ell}{b-a}\cdot\frac14|f(x_0)|^2>0$. Die übrigen Eigenschaften stehen in Stufe [8](#stufe-8). (b) Aus $\|v_n-\operatorname{sgn}\|_2^2=\frac1{3n}$ und der Dreiecksungleichung folgt $\|v_m-v_n\|_2\to0$. Gäbe es ein stetiges $g$ mit $\|v_n-g\|_2\to0$, wäre $\|g-\operatorname{sgn}\|_2=0$. Das Argument aus (a), angewandt auf $(0,1]$ und auf $[-1,0)$, gibt $g=1$ rechts und $g=-1$ links von 0. Das widerspricht der Stetigkeit bei 0.
:::
:::
