---
title: Stufe 5: Funktionenreihen und der M-Test
pfad: Elektrotechnik / 3. Semester / Höhere Mathematik 3 / Konvergenz von Funktionenfolgen
order: 3160700
summary: Für unendliche Summen von Funktionen fehlt ein Test, der gleichmäßige Konvergenz zeigt, ohne dass man die Summe kennt.
tags: Funktionenreihe
lang: de
---

<span class="anker" id="stufe-5"></span>

:::zweck
Für unendliche Summen von Funktionen fehlt ein Test, der gleichmäßige Konvergenz zeigt, ohne dass man die Summe kennt. Diese Stufe liefert ihn.
:::

**Die Idee.** Eine __Funktionenreihe__ hat die Form

<span class="anker" id="gl-5-1"></span>
$$f(x)=\sum_{k=0}^\infty g_k(x),\qquad\text{mit den Partialsummen}\quad f_n(x)=\sum_{k=0}^ng_k(x). \tag{5.1}$$

Sie konvergiert punktweise oder gleichmäßig, wenn die Folge $f_n$ das tut. Der Abstand zwischen $f_n$ und $f$ ist der Rest der Reihe. Deckelt man jedes Glied durch eine Zahl $M_k$, die nicht von $x$ abhängt, ist dieser Rest an allen Stellen zugleich klein (Abb. [5](#abb-5)). Das ist die Majoranten-Idee aus [Teil 2](/wissen/elektrotechnik/3-semester/hohere-mathematik-3/integralrechnung-im-rn/integralrechnung-im-rn.html), jetzt für Summen.

:::abbildung hm3/k6mtest 5
Links die Partialsummen $f_1$, $f_2$, $f_4$ der Reihe $\sum_{k\ge1}x^k/k^2$ und ihre Summe $f$. Rechts die Deckel $M_k=1/k^2$. Der Rest nach $k=3$ (rot) beschränkt $|f-f_3|$ an jeder Stelle.
:::

:::satz Satz 5.1 (Weierstraßscher M-Test)
<span class="anker" id="satz-5-1"></span>

Seien $g_k:[a,b]\to\mathbb{C}$ Funktionen mit

<span class="anker" id="gl-5-2"></span>
$$|g_k(x)|\le M_k\quad\text{für alle }x\in[a,b]\qquad\text{und}\qquad\sum_{k=0}^\infty M_k<\infty. \tag{5.2}$$

Dann konvergiert $f_n(x)=\sum_{k=0}^ng_k(x)$ gleichmäßig auf $[a,b]$.
:::

:::beweis Der Rest hängt nicht von $x$ ab
Für alle $m<n$ gilt nach der Dreiecksungleichung

$$\sup_{x\in[a,b]}|f_m(x)-f_n(x)|=\sup_{x\in[a,b]}\Bigl|\sum_{k=m+1}^ng_k(x)\Bigr|\le\sum_{k=m+1}^nM_k\le\sum_{k=m+1}^\infty M_k.$$

Der Rest rechts strebt für $m\to\infty$ gegen null. Das Cauchy-Kriterium gibt die Behauptung.
:::

⁠**So liest man das:** $M_k$ ist eine Zahl je Glied, die beste Wahl ist $M_k=\sup_x|g_k(x)|$. Die Summe der Deckel muss endlich sein. Dann überträgt sich die Konvergenz der Zahlenreihe auf alle Stellen zugleich.

:::satz Satz 5.2 (Gliedweise rechnen)
<span class="anker" id="satz-5-2"></span>

Die $g_k$ seien stetig auf $[a,b]$.

<ol class="rm">

<li>

Konvergiert $\sum_kg_k$ gleichmäßig gegen $f$, dann ist $f$ stetig, und $\int_a^bf\,\mathrm{d} x=\sum_{k=0}^\infty\int_a^bg_k\,\mathrm{d} x$.

</li>

<li>

Sind die $g_k$ stetig differenzierbar, konvergiert $\sum_kg_k$ punktweise gegen $f$ und $\sum_kg_k'$ gleichmäßig, dann ist $f$ stetig differenzierbar, und $f'=\sum_{k=0}^\infty g_k'$.

</li>

</ol>
:::

:::beweis Endliche Summen zuerst
Für die endliche Summe $f_n$ gilt $\int_a^bf_n\,\mathrm{d} x=\sum_{k=0}^n\int_a^bg_k\,\mathrm{d} x$ und $f_n'=\sum_{k=0}^ng_k'$. Auf die Folge $f_n$ wendet man die Sätze [3.1](stetigkeit-und-integral-bleiben-erhalten.html#satz-3-1), [3.2](stetigkeit-und-integral-bleiben-erhalten.html#satz-3-2) und [4.1](die-ableitung-braucht-mehr.html#satz-4-1) an.
:::

**Beispiel.** Sei $f(x)=\sum_{k=1}^\infty x^k/k^2$ auf $[-1,1]$. Wegen $|x^k/k^2|\le1/k^2=:M_k$ konvergiert die Reihe gleichmäßig, und $f$ ist stetig, obwohl man keine Formel für $f$ hat. Der Test liefert sogar eine Fehlerschranke, die für alle $x$ gilt: $\sum_{k>10}1/k^2<\sum_{k>10}\frac{1}{k(k-1)}=\frac1{10}$. Die Partialsumme $f_{10}$ weicht also überall um weniger als $0{,}1$ von $f$ ab. **Grenzfall:** An der schlechtesten Stelle $x=1$ ist $f(1)=\pi^2/6$ und $f_{10}(1)\approx1{,}5498$, die Abweichung also rund $0{,}095$.

:::frage Konvergiert eine Reihe nur dann gleichmäßig, wenn der M-Test greift?
Nein, er ist hinreichend, nicht notwendig. Für $\sum_{k\ge1}(-1)^kx^k/k$ auf $[0,1]$ ist $\sup_x|g_k(x)|=1/k$, und $\sum1/k=\infty$. Der Test greift nicht. Die Vorzeichen wechseln aber, und die Beträge fallen. Deshalb ist der Rest höchstens das erste weggelassene Glied, also höchstens $1/(n+1)$. Die Reihe konvergiert gleichmäßig.
:::

:::aufgabe Aufgabe 5 ★★ Konvergent, aber nicht gleichmäßig
<span class="anker" id="aufg-5"></span>

Sei $g_k(x)=x^2/(1+x^2)^k$ für $k\ge0$ auf $[-1,1]$.

<ol class="al">

<li>

Berechne die Summe $f(x)=\sum_{k=0}^\infty g_k(x)$. Unterscheide $x\neq0$ und $x=0$.

</li>

<li>

Zeige ohne weitere Rechnung, dass die Konvergenz nicht gleichmäßig ist.

</li>

<li>

Warum scheitert der M-Test? Tipp: Werte $g_k$ bei $x^2=1/k$ aus und benutze $(1+1/k)^k\le\mathrm{e}$.

</li>

</ol>

:::loesung
(a) Für $x\neq0$ ist $q=1/(1+x^2)\in(0,1)$, die geometrische Reihe gibt $f(x)=x^2/(1-q)=1+x^2$. Bei $x=0$ sind alle Glieder null, also $f(0)=0$. (b) Die $g_k$ und damit die Partialsummen sind stetig, $f$ springt bei 0. Nach Satz [3.1](stetigkeit-und-integral-bleiben-erhalten.html#satz-3-1) ist die Konvergenz nicht gleichmäßig. (c) Bei $x^2=1/k$ ist $g_k(x)=\frac1k(1+\frac1k)^{-k}\ge\frac{1}{\mathrm{e}\,k}$. Jede obere Schranke erfüllt also $M_k\ge1/(\mathrm{e} k)$, und $\sum_kM_k=\infty$.
:::
:::

:::aufgabe Aufgabe 6 ★★ Gliedweise ableiten
<span class="anker" id="aufg-6"></span>

Sei $f(x)=\sum_{k=1}^\infty\frac1k\mathrm{e}^{-kx}$ auf $[1,3]$.

<ol class="al">

<li>

Zeige mit dem M-Test, dass die Reihe und die Reihe der Ableitungen gleichmäßig konvergieren.

</li>

<li>

Berechne $f'(x)$ als geschlossenen Ausdruck und $f'(1)$.

</li>

</ol>

:::loesung
(a) Für $x\ge1$ ist $|\frac1k\mathrm{e}^{-kx}|\le\mathrm{e}^{-k}$. Die Ableitung $-\mathrm{e}^{-kx}$ hat dieselbe Schranke, und $\sum_k\mathrm{e}^{-k}$ ist eine geometrische Reihe. (b) Nach Satz [5.2](#satz-5-2) ist $f'(x)=-\sum_{k\ge1}\mathrm{e}^{-kx}=-\dfrac{\mathrm{e}^{-x}}{1-\mathrm{e}^{-x}}=-\dfrac{1}{\mathrm{e}^x-1}$, also $f'(1)=-1/(\mathrm{e}-1)\approx-0{,}582$.
:::
:::
