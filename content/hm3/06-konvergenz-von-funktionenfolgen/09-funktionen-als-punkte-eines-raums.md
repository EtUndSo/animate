---
title: Stufe 7: Funktionen als Punkte eines Raums
pfad: Elektrotechnik / 3. Semester / Höhere Mathematik 3 / Konvergenz von Funktionenfolgen
order: 3160900
summary: Diese Stufe gibt Funktionen eine Länge wie Vektoren.
tags: Norm, normierter Vektorraum, Vollständigkeit, Supremumsnorm
lang: de
---

<span class="anker" id="stufe-7"></span>

:::zweck
Diese Stufe gibt Funktionen eine Länge wie Vektoren. Gleichmäßige Konvergenz wird dadurch zu gewöhnlicher Konvergenz in einem Raum ohne Löcher.
:::

**Die Idee.** Ein Vektor aus $\mathbb{R}^N$ hat $N$ Komponenten. Eine Funktion auf $[a,b]$ hat eine Komponente je Stelle $x$, und addiert und gestreckt wird Komponente für Komponente. Misst man die Länge durch die größte Komponente, dann ist der Abstand zweier Funktionen ihr größter senkrechter Abstand (Abb. [7](#abb-7)).

:::abbildung hm3/k6norm 7
Links der Abstand $\|f-g\|_{\sup}$: die größte senkrechte Lücke zwischen zwei Kurven. Rechts $f_n(x)=|x|^{1+1/n}$ für $n=1,2,8$: Die Kurven sind stetig differenzierbar, ihr Grenzwert $|x|$ (rot) hat einen Knick.
:::

:::definition Definition 7.1 (Norm und Vollständigkeit)
<span class="anker" id="satz-7-1"></span>

Sei $V$ ein Vektorraum über $\mathbb{R}$ oder $\mathbb{C}$. Eine __Norm__ ordnet jedem $f\in V$ eine Zahl $\|f\|\ge0$ zu, so dass gilt:

<ol class="rm">

<li>

$\|f\|=0$ genau dann, wenn $f=0$,

</li>

<li>

$\|\lambda f\|=|\lambda|\,\|f\|$ für alle Skalare $\lambda$,

</li>

<li>

$\|f+g\|\le\|f\|+\|g\|$ (Dreiecksungleichung).

</li>

</ol>

$V$ heißt dann __normierter Vektorraum__. __Vollständigkeit__ von $V$ heißt: Jede Folge mit $\|f_m-f_n\|\to0$ für $m,n\to\infty$ konvergiert gegen ein Element von $V$, das heißt $\|f_n-f\|\to0$ für ein $f\in V$.
:::

:::definition Definition 7.2 (Supremumsnorm)
<span class="anker" id="satz-7-2"></span>

Für beschränkte $f:[a,b]\to\mathbb{C}$ heißt $\|f\|_{\sup}:=\sup_{x\in[a,b]}|f(x)|$ die __Supremumsnorm__.
:::

⁠**So liest man das:** Für $f(x)=x-x^2$ auf $[0,1]$ ist $\|f\|_{\sup}=\frac14$. Die drei Eigenschaften gelten: (i) Ist das Supremum null, ist $f(x)=0$ an jeder Stelle. (ii) folgt aus $|\lambda f(x)|=|\lambda|\,|f(x)|$. (iii) folgt aus $|f(x)+g(x)|\le|f(x)|+|g(x)|\le\|f\|_{\sup}+\|g\|_{\sup}$, denn die rechte Seite hängt nicht von $x$ ab. In dieser Sprache ist

<span class="anker" id="gl-7-1"></span>
$$f_n\to f\text{ gleichmäßig}\iff\|f_n-f\|_{\sup}\to0, \tag{7.1}$$

und das Cauchy-Kriterium lautet $\|f_m-f_n\|_{\sup}\to0$ für $m,n\to\infty$.

:::satz Satz 7.3 (Die stetigen Funktionen sind vollständig)
<span class="anker" id="satz-7-3"></span>

Die stetigen Funktionen auf einem Intervall $[a,b]$,

$$C^0([a,b];\mathbb{C}):=\{f:[a,b]\to\mathbb{C}\ \text{stetig}\},$$

bilden mit der Supremumsnorm einen vollständigen normierten Vektorraum.
:::

:::beweis Zwei frühere Sätze
Stetige Funktionen auf $[a,b]$ sind beschränkt, und Summen und Vielfache stetiger Funktionen sind stetig. Sei $\|f_m-f_n\|_{\sup}\to0$. Nach Satz [2.2](gleichmaige-konvergenz.html#satz-2-2) konvergiert $f_n$ gleichmäßig gegen eine beschränkte Funktion $f$. Nach Satz [3.1](stetigkeit-und-integral-bleiben-erhalten.html#satz-3-1) ist $f$ stetig, also $f\in C^0([a,b];\mathbb{C})$. Nach [(7.1)](#gl-7-1) gilt $\|f_n-f\|_{\sup}\to0$.
:::

⁠**So liest man das:** Eine Folge, deren Glieder einander nahe kommen, führt nicht aus den stetigen Funktionen heraus. Für stetige Funktionen schreibt man auch $\|f\|_{C^0}\equiv\|f\|_{\sup}$.

**Ableitungen im Raum.** Die Supremumsnorm allein reicht für differenzierbare Funktionen nicht. Die Funktionen aus Aufgabe [4](die-ableitung-braucht-mehr.html#aufg-4) sind stetig differenzierbar und erfüllen $\|f_m-f_n\|_{\sup}\to0$, ihr Grenzwert $|x|$ hat aber einen Knick. Bezüglich $\|\cdot\|_{\sup}$ hat $C^1$ also ein Loch. Deshalb zählt man die Ableitungen mit: Die Räume

$$C^k([a,b]):=\{f:[a,b]\to\mathbb{R}\ \ k\text{-mal stetig differenzierbar}\}$$

und $C^k([a,b];\mathbb{C})$, dasselbe mit Werten in $\mathbb{C}$, bilden mit der Norm

<span class="anker" id="gl-7-2"></span>
$$\|f\|_{C^k}:=\sup_{x\in[a,b]}\sum_{i=0}^k|f^{(i)}(x)| \tag{7.2}$$

vollständige normierte Vektorräume.

:::herleitung Vollständigkeit von $C^k$
Sei $\|f_m-f_n\|_{C^k}\to0$. Wegen $|f^{(i)}(x)|\le\sum_{j=0}^k|f^{(j)}(x)|$ ist jede Folge $(f_n^{(i)})_n$ mit $0\le i\le k$ eine Cauchy-Folge in $C^0$. Sie hat nach Satz [7.3](#satz-7-3) einen stetigen Grenzwert $f_i$. Satz [4.1](die-ableitung-braucht-mehr.html#satz-4-1) gibt der Reihe nach $f_i'=f_{i+1}$. Also ist $f:=f_0$ $k$-mal stetig differenzierbar mit $f^{(i)}=f_i$. Außerdem ist $\|f_n-f\|_{C^k}\le\sum_{i=0}^k\|f_n^{(i)}-f_i\|_{\sup}\to0$.
:::

:::frage Wozu braucht man Vollständigkeit beim Rechnen?
Sie erlaubt Existenzbeweise ohne Formel. Hat man ein Verfahren, dessen Ergebnisse einander immer näher kommen, dann existiert sein Grenzwert im selben Raum, auch wenn man ihn nicht aufschreiben kann. So war es in Stufe [5](funktionenreihen-und-der-m-test.html#stufe-5) bei $\sum_kx^k/k^2$.
:::

:::aufgabe Aufgabe 9 ★★ Polynome haben Löcher
<span class="anker" id="aufg-9"></span>

Sei $p_n(x)=\sum_{k=0}^nx^k/k!$ auf $[0,1]$. Zeige, dass $(p_n)$ die Bedingung $\|p_m-p_n\|_{\sup}\to0$ erfüllt, und folgere, dass die Polynome mit der Supremumsnorm nicht vollständig sind.

:::loesung
Für $m<n$ und $x\in[0,1]$ ist $|p_n(x)-p_m(x)|\le\sum_{k=m+1}^n1/k!$, und das strebt gegen null. In $C^0([0,1];\mathbb{C})$ ist der Grenzwert $\mathrm{e}^x$. Gäbe es ein Polynom $p$ mit $\|p_n-p\|_{\sup}\to0$, wäre $p=\mathrm{e}^x$ auf $[0,1]$, denn der Grenzwert ist eindeutig. Ein Polynom vom Grad $d$ hat aber die $(d+1)$-te Ableitung 0, die Exponentialfunktion nicht. Die Polynome haben also ein Loch.
:::
:::

:::aufgabe Aufgabe 10 ★★★ Eine Norm aus der Ableitung
<span class="anker" id="aufg-10"></span>

Sei $N(u)=\sup_{x\in[0,1]}|u'(x)|$.

<ol class="al">

<li>

Warum ist $N$ auf $C^1([0,1])$ keine Norm?

</li>

<li>

Zeige, dass $N$ auf $X=\{u\in C^1([0,1]):u(1)=0\}$ eine Norm ist.

</li>

<li>

Zeige $\|u\|_{\sup}\le N(u)$ für $u\in X$.

</li>

<li>

Zeige, dass $X$ mit $N$ vollständig ist.

</li>

</ol>

:::loesung
(a) Für $u=1$ ist $N(u)=0$, aber $u\neq0$. (b) Aus $N(u)=0$ folgt $u'=0$, also ist $u$ konstant, und wegen $u(1)=0$ ist $u=0$. Homogenität und Dreiecksungleichung erbt $N$ von der Supremumsnorm von $u'$. (c) $u(x)=-\int_x^1u'(y)\,\mathrm{d} y$ gibt $|u(x)|\le(1-x)N(u)\le N(u)$. (d) Sei $N(u_m-u_n)\to0$. Dann konvergiert $u_n'$ gleichmäßig gegen ein stetiges $v$. Nach (c) ist $\|u_m-u_n\|_{\sup}\to0$, also konvergiert $u_n$ gleichmäßig gegen ein $u$. Satz [4.1](die-ableitung-braucht-mehr.html#satz-4-1) gibt $u'=v$, und $u(1)=\lim u_n(1)=0$. Also ist $u\in X$ und $N(u_n-u)=\|u_n'-v\|_{\sup}\to0$.
:::
:::
