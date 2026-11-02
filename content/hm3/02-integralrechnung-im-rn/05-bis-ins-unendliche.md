---
title: Stufe 3: Bis ins Unendliche
pfad: Elektrotechnik / 3. Semester / Höhere Mathematik 3 / Integralrechnung im Rⁿ
order: 3120500
summary: Läuft das Integral bis ins Unendliche, gilt das Ergebnis aus Stufe 1 nicht mehr.
tags: uneigentliches Parameterintegral, gleichmäßige Konvergenz, Majorante
lang: de
---

<span class="anker" id="stufe-3"></span>

:::zweck
Läuft das Integral bis ins Unendliche, gilt das Ergebnis aus Stufe [1](integrale-mit-parameter.html#stufe-1) nicht mehr. Diese Stufe zeigt, wie es schiefgeht und welche Bedingung das verhindert.
:::

**Die Idee.** Ein __uneigentliches Parameterintegral__ $F(\boldsymbol{x})=\int_a^\infty f(\boldsymbol{x},t)\,\mathrm{d} t$ ist der Grenzwert der Integrale $F_T(\boldsymbol{x})=\int_a^Tf(\boldsymbol{x},t)\,\mathrm{d} t$ für $T\to\infty$. Jedes $F_T$ ist nach Stufe [1](integrale-mit-parameter.html#stufe-1) stetig. Ein Grenzwert stetiger Funktionen muss aber nicht stetig sein. Das passiert, wenn $F_T$ für manche $\boldsymbol{x}$ immer langsamer gegen $F$ strebt. Im Beweis von Satz [1.1](integrale-mit-parameter.html#satz-1-1) verhinderte das die Kompaktheit von $[a,b]$. Das Intervall $[a,\infty)$ ist nicht kompakt.

**Ein stetiger Integrand mit unstetigem Integral.** Sei $f(x,t)=\sin(tx)/t$ für $t\neq0$ und $f(x,0)=x$. Diese Funktion ist stetig auf $\mathbb{R}\times[0,\infty)$, denn $\sin(tx)/t\to x$ für $t\to0$. Bekannt ist $\int_{-\infty}^\infty\frac{\sin t}{t}\,\mathrm{d} t=\pi$. Der Integrand ist gerade, also ist $\int_0^\infty\frac{\sin s}{s}\,\mathrm{d} s=\frac\pi2$. Die Substitution $s=tx$ gibt für $x>0$ denselben Wert, und $\sin$ ist ungerade:

<span class="anker" id="gl-3-1"></span>
$$F(x)=\int_0^\infty f(x,t)\,\mathrm{d} t=\begin{cases}\pi/2&x>0,\\0&x=0,\\-\pi/2&x<0.\end{cases} \tag{3.1}$$

$F$ springt bei $x=0$, obwohl $f$ überall stetig ist und das Integral für jedes $x$ konvergiert.

:::abbildung hm3/k2sprung 3
Links $F_T(x)$ über $T$: Bei $x=0{,}2$ dauert die Annäherung an $\pi/2$ fünfmal so lang wie bei $x=1$. Rechts dieselben Integrale über $x$: Jede Kurve ist stetig, aber der Übergang bei $x=0$ wird immer steiler. Im Grenzwert entsteht ein Sprung.
:::

**Der Mechanismus.** Dieselbe Substitution zeigt für $x>0$: $F_T(x)=\int_0^{Tx}\frac{\sin s}{s}\,\mathrm{d} s$. Es zählt nur das Produkt $Tx$. Bei $x=0{,}01$ braucht man ein 100-mal größeres $T$ als bei $x=1$, um denselben Abstand zu $\pi/2$ zu erreichen (Abb. [3](#abb-3)). Für $x\to0$ konvergiert das Integral also immer langsamer, und kein einzelnes $T$ reicht für alle $x$. Außerdem ist es nicht absolut konvergent: $\int_0^\infty|\sin s|/s\,\mathrm{d} s=\infty$. Es lebt von Vorzeichenwechseln.

:::definition Definition 3.1 (Gleichmäßige Konvergenz)
<span class="anker" id="satz-3-1"></span>

Gibt es zu jedem $\varepsilon>0$ ein $T_0$, das nicht von $\boldsymbol{x}$ abhängt, mit $\bigl|\int_T^\infty f(\boldsymbol{x},t)\,\mathrm{d} t\bigr|<\varepsilon$ für alle $T\ge T_0$ und alle $\boldsymbol{x}\in\mathcal U$, dann liegt bei $\int_a^\infty f(\boldsymbol{x},t)\,\mathrm{d} t$ in $\mathcal U$ __gleichmäßige Konvergenz__ vor.
:::

Unter dieser Voraussetzung gilt ein Ergebnis wie Satz [1.1](integrale-mit-parameter.html#satz-1-1). Man sichert sie meist durch eine feste obere Schranke.

:::satz Satz 3.2 (Majorantenkriterium)
<span class="anker" id="satz-3-2"></span>

Sei $\mathcal U\subset\mathbb{R}^n$ offen, $-\infty\le a<b\le\infty$ und $f:\mathcal U\times(a,b)\to\mathbb{R}$ stetig. Es gebe eine uneigentlich integrierbare Funktion $g:(a,b)\to\mathbb{R}$, eine __Majorante__, mit

<span class="anker" id="gl-3-2"></span>
$$|f(\boldsymbol{x},t)|\le g(t)\quad\text{in }\mathcal U\times(a,b),\qquad\int_a^bg(t)\,\mathrm{d} t<\infty. \tag{3.2}$$

Dann ist $F(\boldsymbol{x})=\int_a^bf(\boldsymbol{x},t)\,\mathrm{d} t$ stetig in $\mathcal U$. Sind ferner die $\partial f/\partial x_k$ stetig auf $\mathcal U\times(a,b)$, und gibt es uneigentlich integrierbare Funktionen $G_k:(a,b)\to\mathbb{R}$ mit

<span class="anker" id="gl-3-3"></span>
$$\Bigl|\frac{\partial f}{\partial x_k}(\boldsymbol{x},t)\Bigr|\le G_k(t)\quad\text{in }\mathcal U\times(a,b),\qquad\int_a^bG_k(t)\,\mathrm{d} t<\infty, \tag{3.3}$$

dann ist $F$ stetig differenzierbar in $\mathcal U$, und Ableitung und Integral dürfen vertauscht werden wie in [(1.2)](integrale-mit-parameter.html#gl-1-2).
:::

⁠**So liest man das:** Entscheidend ist, dass $g$ nur von $t$ abhängt, nicht von $\boldsymbol{x}$. Die Majorante deckelt die ganze Kurvenschar auf einmal. Das Intervall $(a,b)$ darf unendlich sein, und der Integrand darf an den Enden eine Polstelle haben. In $\mathbb{R}\times(0,\infty)$ ist etwa $\mathrm{e}^{-t}\cos(xt)$ durch $g(t)=\mathrm{e}^{-t}$ beschränkt, für jedes $x$.

:::beweis Der Rest ist für alle $\boldsymbol{x}$ zugleich klein
Sei $F_T(\boldsymbol{x})=\int_{a_T}^{b_T}f(\boldsymbol{x},t)\,\mathrm{d} t$ mit kompakten $[a_T,b_T]\subset(a,b)$, $a_T\to a$ und $b_T\to b$ für $T\to\infty$. Wegen [(3.2)](#gl-3-2) gilt für alle $\boldsymbol{x}$

$$|F(\boldsymbol{x})-F_T(\boldsymbol{x})|\le r_T:=\int_a^{a_T}g(t)\,\mathrm{d} t+\int_{b_T}^bg(t)\,\mathrm{d} t,\qquad r_T\to0.$$

Das ist gleichmäßige Konvergenz, denn $r_T$ hängt nicht von $\boldsymbol{x}$ ab. Es folgt

$$|F(\boldsymbol{y})-F(\boldsymbol{x})|\le|F_T(\boldsymbol{y})-F_T(\boldsymbol{x})|+2r_T.$$

Wähle $T$ mit $2r_T<\varepsilon/2$. Da $F_T$ nach Satz [1.1](integrale-mit-parameter.html#satz-1-1) stetig ist, ist auch der erste Summand kleiner als $\varepsilon/2$, wenn $\boldsymbol{y}$ nahe genug bei $\boldsymbol{x}$ liegt.

Für die Ableitung sei $H_k(\boldsymbol{x})=\int_a^b\partial_{x_k}f(\boldsymbol{x},t)\,\mathrm{d} t$. Nach dem ersten Teil ist $H_k$ stetig, und wegen [(3.3)](#gl-3-3) strebt $\partial_{x_k}F_T$ für $T\to\infty$ gleichmäßig gegen $H_k$. Im Hauptsatz $F_T(\boldsymbol{x}+h\hat{\boldsymbol{e}}_k)-F_T(\boldsymbol{x})=\int_0^h\partial_{x_k}F_T(\boldsymbol{x}+s\hat{\boldsymbol{e}}_k)\,\mathrm{d} s$ darf man daher zum Grenzwert übergehen. Es entsteht dieselbe Formel mit $F$ und $H_k$, und daraus folgt $\partial_{x_k}F=H_k$.
:::

⁠**Warum $g$ nicht von $\boldsymbol{x}$ abhängen darf:** Für das Beispiel [(3.1)](#gl-3-1) müsste $g(t)\ge\sup_x|\sin(tx)|/t=1/t$ gelten, denn das Supremum, die kleinste obere Schranke, wird bei $tx=\pi/2$ erreicht. Es ist aber $\int_1^\infty\frac{\mathrm{d} t}{t}=\infty$. Es gibt also keine Majorante, und $F$ darf springen.

**Beispiel.** $F(x)=\int_0^\infty\mathrm{e}^{-t}\cos(xt)\,\mathrm{d} t$. Hier passen $g(t)=\mathrm{e}^{-t}$ und $G(t)=t\,\mathrm{e}^{-t}$, beide integrierbar. Also ist $F$ stetig differenzierbar mit $F'(x)=-\int_0^\infty t\,\mathrm{e}^{-t}\sin(xt)\,\mathrm{d} t$. Zweimal partiell integriert ist $F(x)=1/(1+x^2)$, also $F'(1)=-\frac12$, und das Integral gibt denselben Wert. **Grenzfall:** $F(0)=\int_0^\infty\mathrm{e}^{-t}\,\mathrm{d} t=1$.

:::frage Ist das Beispiel mit $\sin(tx)/t$ nur deshalb unstetig, weil das Integral nicht absolut konvergiert?
Nein. Absolute Konvergenz für jedes einzelne $x$ hilft nicht, das zeigt Aufgabe [4](#aufg-4). Es zählt nicht, ob das Integral für jedes $x$ konvergiert, sondern ob es für alle $x$ gleich schnell konvergiert.
:::

:::aufgabe Aufgabe 4 ★★ Absolute Konvergenz reicht nicht
<span class="anker" id="aufg-4"></span>

<ol class="al">

<li>

Sei $f(x,t)=x\,\mathrm{e}^{-xt}$ für $x\ge0$, $t\ge0$. Berechne $F(x)=\int_0^\infty f(x,t)\,\mathrm{d} t$. Ist das Integral absolut konvergent? Ist $F$ bei $x=0$ stetig?

</li>

<li>

Berechne $\sup_{x\ge0}f(x,t)$ für festes $t>0$ und begründe, warum es keine Majorante gibt.

</li>

<li>

Zeige, dass $G(x)=\int_0^\infty\frac{\cos(xt)}{1+t^2}\,\mathrm{d} t$ auf $\mathbb{R}$ stetig ist.

</li>

</ol>

:::loesung
(a) Für $x>0$ ist $F(x)=\bigl[-\mathrm{e}^{-xt}\bigr]_0^\infty=1$. Für $x=0$ ist $f=0$, also $F(0)=0$. Das Integral ist absolut konvergent, denn $f\ge0$. Trotzdem ist $F$ bei $x=0$ unstetig. (b) Die Ableitung nach $x$ ist $(1-xt)\mathrm{e}^{-xt}$, das Maximum liegt bei $x=1/t$ und hat den Wert $\frac{1}{\mathrm{e} t}$. Eine Majorante müsste also $g(t)\ge\frac1{\mathrm{e} t}$ erfüllen, und das ist auf $[1,\infty)$ nicht integrierbar. Anschaulich läuft die Fläche 1 für $x\to0$ nach rechts ins Unendliche weg. (c) $g(t)=1/(1+t^2)$ ist eine Majorante, unabhängig von $x$, mit $\int_0^\infty g\,\mathrm{d} t=\frac\pi2$. Der Integrand ist stetig, also ist $G$ auf $\mathbb{R}$ stetig.
:::
:::
