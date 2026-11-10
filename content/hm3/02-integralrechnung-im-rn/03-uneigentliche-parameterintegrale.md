---
title: Uneigentliche Parameterintegrale
pfad: Elektrotechnik / 3. Semester / HöMa3 – Höhere Mathematik 3 / Integralrechnung im Rⁿ
adresse: elektrotechnik/3-semester/hohere-mathematik-3/integralrechnung-im-rn
knoten: Kapitel 2: Integralrechnung im Rⁿ
order: 3120300
summary: Läuft ein Parameterintegral bis ins Unendliche oder wird der Integrand an einem Rand unbeschränkt, dann gelten die Ergebnisse des letzten Abschnitts nicht mehr ohne Weiteres.
tags: obere Schranke, Supremum, Maximum, uneigentliches Integral, uneigentlich integrierbar, absolut konvergent, Vergleichsfunktion, uneigentliches Parameterintegral
lang: de
---

<span class="anker" id="stufe-2"></span>

:::zweck
Läuft ein Parameterintegral bis ins Unendliche oder wird der Integrand an einem Rand unbeschränkt, dann gelten die Ergebnisse des letzten Abschnitts nicht mehr ohne Weiteres. Dieser Abschnitt zeigt, wie es schiefgeht, welche Bedingung das verhindert, und wendet sie auf drei wichtige Integrale an: die Fourier-Transformation, die Gamma-Funktion und die Laplace-Transformation.
:::

### Was du dafür brauchst: Supremum und Maximum

<span class="anker" id="stufe-2-1"></span>

Für Abschätzungen braucht man die kleinste Zahl, die über allen Werten einer Funktion liegt. Sie muss selbst kein Wert der Funktion sein.

Eine Zahl $S$ heißt __obere Schranke__ einer Menge reeller Zahlen, wenn keine Zahl der Menge größer ist als $S$. Die kleinste obere Schranke heißt __Supremum__ und wird $\sup$ geschrieben. Für eine Funktion $f$ auf einer Menge $M$ schreibt man $\sup_{\boldsymbol{x}\in M}f(\boldsymbol{x})$ für das Supremum aller ihrer Werte. Ist das Supremum selbst ein Wert von $f$, heißt es das __Maximum__. Eine stetige Funktion auf einer kompakten Menge hat immer ein Maximum; das ist der Satz vom Maximum.

::::beispiel
Für $\mathrm{e}^{-t}$ auf $(0,\infty)$ ist $\sup=1$. Das ist kein Wert der Funktion, denn $\mathrm{e}^{-t}<1$ für $t>0$; ein Maximum gibt es also nicht. Auf dem kompakten Intervall $[0,1]$ ist $1=\mathrm{e}^{-0}$ das Maximum. Für festes $t>0$ ist $\sup_{x\in\mathbb{R}}|\sin(tx)|=1$, angenommen bei $tx=\pi/2$.
::::

⁠**Kurz gesagt:** Das Supremum ist die kleinste obere Schranke der Werte; wird es angenommen, ist es das Maximum.

### Was du dafür brauchst: uneigentliche Integrale

<span class="anker" id="stufe-2-2"></span>

Das Integral aus Unterabschnitt [1.1](integrale-mit-parameter-uber-endlichen-intervallen.html#stufe-1-1) braucht ein beschränktes Intervall und eine stetige Funktion darauf. Viele wichtige Integrale laufen aber bis ins Unendliche, oder ihr Integrand wird an einem Ende unbeschränkt.

Man integriert dann zuerst über ein endliches Stück, auf dem alles harmlos ist, und lässt das Stück danach wachsen.

**Unendliches Intervall.** Ist $u$ stetig auf $[a,\infty)$, dann setzt man

$$\int_a^\infty u(t)\,\mathrm{d} t:=\lim_{T\to\infty}\int_a^Tu(t)\,\mathrm{d} t ,$$

falls dieser Grenzwert existiert. Ein so erklärtes Integral heißt __uneigentliches Integral__. Existiert der Grenzwert, sagt man, das Integral *konvergiert*, sonst *divergiert* es.

**Unbeschränkter Integrand.** Ist $u$ stetig auf $(a,b]$ und bei $a$ unbeschränkt, dann setzt man entsprechend $\int_a^bu(t)\,\mathrm{d} t:=\lim_{s\searrow a}\int_s^bu(t)\,\mathrm{d} t$.

**Allgemein.** Für ein offenes Intervall $(a,b)$ mit $-\infty\le a<b\le\infty$ und stetiges $u$ darauf integriert man über abgeschlossene Stücke $[a',b']\subset(a,b)$ und lässt $a'\to a$ und $b'\to b$ gehen, und zwar unabhängig voneinander. Existiert der Grenzwert, heißt $u$ __uneigentlich integrierbar__ auf $(a,b)$.

::::beispiel
Für eine Zahl $\kappa>0$ ist $\int_0^T\mathrm{e}^{-\kappa t}\,\mathrm{d} t=\frac{1-\mathrm{e}^{-\kappa T}}\kappa\to\frac1\kappa$, also $\int_0^\infty\mathrm{e}^{-\kappa t}\,\mathrm{d} t=\frac1\kappa$. Ebenso ist $\int_1^Tt^{-2}\,\mathrm{d} t=1-\frac1T\to1$, aber $\int_1^Tt^{-1}\,\mathrm{d} t=\ln T\to\infty$. Allgemein konvergiert $\int_1^\infty t^{-r}\,\mathrm{d} t$ genau für Exponenten $r>1$ und $\int_0^1t^{-r}\,\mathrm{d} t$ genau für $r<1$; zum Beispiel ist $\int_0^1t^{-1/2}\,\mathrm{d} t=\lim_{s\searrow0}\bigl(2-2\sqrt s\bigr)=2$.
::::

⁠**Kurz gesagt:** Ein uneigentliches Integral ist der Grenzwert der Integrale über endliche Stücke, die gegen das ganze Intervall wachsen.

### Was du dafür brauchst: absolute Konvergenz und Vergleich

<span class="anker" id="stufe-2-3"></span>

Ob ein uneigentliches Integral konvergiert, sieht man selten am Grenzwert direkt. Meist vergleicht man den Integranden mit einer Funktion, deren Integral man kennt.

**Absolute Konvergenz.** Ein uneigentliches Integral $\int_a^bu(t)\,\mathrm{d} t$ heißt __absolut konvergent__, wenn auch $\int_a^b|u(t)|\,\mathrm{d} t$ konvergiert. Ein absolut konvergentes Integral konvergiert, und es gilt $\bigl|\int_a^bu\,\mathrm{d} t\bigr|\le\int_a^b|u|\,\mathrm{d} t$.

**Vergleichskriterium.** Ist $|u(t)|\le v(t)$ auf $(a,b)$ und konvergiert $\int_a^bv(t)\,\mathrm{d} t$, dann konvergiert $\int_a^bu(t)\,\mathrm{d} t$ absolut. Die Funktion $v$ heißt dabei __Vergleichsfunktion__.

**Exponentialfunktion gegen Potenz.** Für $m\ge0$ und $\kappa>0$ ist $t^m\mathrm{e}^{-\kappa t}$ auf $[0,\infty)$ beschränkt. Das Maximum liegt bei $t=m/\kappa$. Die $\mathrm{e}$-Funktion gewinnt also gegen jede Potenz.

::::beispiel
$\int_0^\infty t^2\,\mathrm{e}^{-t}\,\mathrm{d} t$ konvergiert absolut. Denn $t^2\mathrm{e}^{-t}=\bigl(t^2\mathrm{e}^{-t/2}\bigr)\,\mathrm{e}^{-t/2}$, und der erste Faktor ist höchstens $16\,\mathrm{e}^{-2}\approx2{,}17$, sein Maximum bei $t=4$. Also ist $v(t)=2{,}17\,\mathrm{e}^{-t/2}$ eine Vergleichsfunktion mit $\int_0^\infty v\,\mathrm{d} t=4{,}34$. Der genaue Wert des Integrals ist $2$.
::::

⁠**Ein Integral, das nur bedingt konvergiert:** $\int_0^\infty\frac{\sin t}t\,\mathrm{d} t$ konvergiert, aber nicht absolut. Der Integrand ist bei $t=0$ harmlos, denn $\frac{\sin t}t\to1$.

:::hintergrund Warum $\int_0^\infty\frac{\sin t}t\,\mathrm{d} t$ konvergiert, aber nicht absolut
Man zerlegt die Fläche in Bögen zwischen $k\pi$ und $(k+1)\pi$. Auf diesem Stück hat $\sin t$ ein festes Vorzeichen, und $|\sin t|$ hat die Fläche $2$. Teilt man durch $t$, liegt die Fläche des Bogens zwischen $\frac2{(k+1)\pi}$ und $\frac2{k\pi}$. Die Bögen wechseln das Vorzeichen und werden immer kleiner. Ihre Summe konvergiert deshalb, aus demselben Grund wie die Reihe $1-\frac12+\frac13-\dots$: Jeder neue Bogen macht einen Teil des vorigen wieder rückgängig. Die Beträge der Bögen dagegen sind mindestens $\frac2{(k+1)\pi}$, und die harmonische Reihe $\sum\frac1{k+1}$ divergiert. Das Integral lebt also davon, dass sich positive und negative Bögen fast aufheben.
:::

⁠**Kurz gesagt:** Liegt der Betrag des Integranden unter einer Vergleichsfunktion mit endlichem Integral, konvergiert das Integral absolut. Die $\mathrm{e}$-Funktion gewinnt gegen jede Potenz.

### Was du dafür brauchst: die Substitutionsregel

<span class="anker" id="stufe-2-4"></span>

Ein Integral wird oft einfacher, wenn man eine neue Integrationsvariable einführt. Mehrere Rechnungen dieses Kapitels tun das.

:::satz Satz 2.1 (Substitutionsregel)
<span class="anker" id="satz-2-1"></span>

Sei $\sigma\colon[a,b]\to\mathbb{R}$ stetig differenzierbar und $u$ stetig auf einem Intervall, das alle Werte $\sigma(t)$ enthält. Dann gilt

$$\int_a^bu\bigl(\sigma(t)\bigr)\,\sigma'(t)\,\mathrm{d} t=\int_{\sigma(a)}^{\sigma(b)}u(s)\,\mathrm{d} s .$$
:::

⁠**So liest man das:** Man ersetzt $s=\sigma(t)$ und $\mathrm{d} s=\sigma'(t)\,\mathrm{d} t$, und die Grenzen wandern mit. Ein häufiger Sonderfall ist $\sigma(t)=x\,t$ mit einer festen Zahl $x>0$: $\int_0^\infty u(xt)\,\mathrm{d} t=\frac1x\int_0^\infty u(s)\,\mathrm{d} s$. Für uneigentliche Integrale folgt das aus dem endlichen Fall, indem man die obere Grenze gegen unendlich gehen lässt.

::::beispiel
Mit $\sigma(t)=t^2$ und $u=\cos$ ist $\int_0^12t\cos(t^2)\,\mathrm{d} t=\int_0^1\cos s\,\mathrm{d} s=\sin1\approx0{,}841$.
::::

:::hintergrund Woher der Faktor $\sigma'(t)$ kommt
Die Abbildung $t\mapsto\sigma(t)$ bildet ein kurzes Stück der Länge $\Delta t$ bei $t$ auf ein Stück der Länge ungefähr $|\sigma'(t)|\,\Delta t$ ab. Der Faktor $\sigma'(t)$ sagt also, wie stark die Substitution die $t$-Achse an dieser Stelle streckt oder staucht. In der Riemann-Summe $\sum_ku(\sigma(t_k))\,\sigma'(t_k)\,\Delta t$ ist jeder Summand deshalb ungefähr „Wert von $u$ mal Länge des Bildstücks“, also ein Summand einer Riemann-Summe von $u$ über das Bildintervall. Ohne den Faktor würde man jedes Bildstück so zählen, als hätte es die Länge $\Delta t$.
:::

⁠**Kurz gesagt:** Bei der Substitution $s=\sigma(t)$ wird $\mathrm{d} s=\sigma'(t)\,\mathrm{d} t$; der Faktor $\sigma'$ misst, wie stark $\sigma$ die Achse streckt.

### Was du dafür brauchst: Integrale komplexer Funktionen

<span class="anker" id="stufe-2-5"></span>

Die Fourier-Transformation in diesem Abschnitt integriert Funktionen mit komplexen Werten. Man führt das auf zwei reelle Integrale zurück.

Hat eine Funktion $f(t)=u(t)+\mathrm i\,v(t)$ den Realteil $u$ und den Imaginärteil $v$, dann setzt man

$$\int_a^bf(t)\,\mathrm{d} t:=\int_a^bu(t)\,\mathrm{d} t+\mathrm i\int_a^bv(t)\,\mathrm{d} t .$$

Die Abschätzung $\bigl|\int_a^bf\,\mathrm{d} t\bigr|\le\int_a^b|f|\,\mathrm{d} t$ gilt auch hier. Für reelle Zahlen $\xi$ und $x$ gilt nach der Eulerschen Formel

$$\mathrm{e}^{-\mathrm i\xi x}=\cos(\xi x)-\mathrm i\sin(\xi x),\qquad|\mathrm{e}^{-\mathrm i\xi x}|=1 .$$

::::beispiel
$\int_0^\pi\mathrm{e}^{\mathrm it}\,\mathrm{d} t=\int_0^\pi\cos t\,\mathrm{d} t+\mathrm i\int_0^\pi\sin t\,\mathrm{d} t=0+2\mathrm i=2\mathrm i$. Der Betrag $2$ ist kleiner als $\int_0^\pi|\mathrm{e}^{\mathrm it}|\,\mathrm{d} t=\pi$.
::::

⁠**Kurz gesagt:** Komplexe Integranden integriert man nach Real- und Imaginärteil getrennt.

### Das uneigentliche Parameterintegral

<span class="anker" id="stufe-2-6"></span>

Läuft das Integral über $t$ bis ins Unendliche, ist das Parameterintegral für jeden Parameter ein uneigentliches Integral.

Für jedes feste $\boldsymbol{x}$ integriert man zuerst bis zu einer endlichen Grenze $T$ und lässt dann $T\to\infty$ gehen. Bei jedem endlichen $T$ hat man ein Parameterintegral aus dem letzten Abschnitt.

:::definition Definition 2.2 (Uneigentliches Parameterintegral)
<span class="anker" id="satz-2-2"></span>

Sei $\mathcal U\subset\mathbb{R}^n$ offen und $f\colon\mathcal U\times[a,\infty)\to\mathbb{R}$ stetig. Konvergiert das Integral für jedes $\boldsymbol{x}\in\mathcal U$, dann heißt

$$F(\boldsymbol{x})=\int_a^\infty f(\boldsymbol{x},t)\,\mathrm{d} t=\lim_{T\to\infty}F_T(\boldsymbol{x}),\qquad F_T(\boldsymbol{x})=\int_a^Tf(\boldsymbol{x},t)\,\mathrm{d} t,$$

ein __uneigentliches Parameterintegral__. Entsprechend für ein offenes Intervall $(a,b)$ mit $-\infty\le a<b\le\infty$, wie im Unterabschnitt [2.2](#stufe-2-2).
:::

⁠**So liest man das:** Jedes $F_T$ ist nach Satz [1.7](integrale-mit-parameter-uber-endlichen-intervallen.html#satz-1-7) stetig. Das uneigentliche Parameterintegral ist der Grenzwert dieser stetigen Funktionen für $T\to\infty$. Ob der Grenzwert wieder stetig ist, ist die Frage dieses Abschnitts.

::::beispiel
Die Abklingkurven über ganz $[0,\infty)$: Für $x>0$ ist $F_T(x)=\frac{1-\mathrm{e}^{-xT}}x$ und $F(x)=\int_0^\infty\mathrm{e}^{-xt}\,\mathrm{d} t=\frac1x$. Für $x\le0$ divergiert das Integral, weil $\mathrm{e}^{-xt}\ge1$ ist. Das uneigentliche Parameterintegral ist also auf $\mathcal U=(0,\infty)$ erklärt.
::::

⁠**Kurz gesagt:** Ein uneigentliches Parameterintegral ist für jeden Parameter der Grenzwert der Integrale bis $T$.

### Ein stetiger Integrand mit unstetigem Integral

<span class="anker" id="stufe-2-7"></span>

Für endliche Intervalle macht ein stetiger Integrand das Parameterintegral stetig. Für uneigentliche Integrale gilt das im Allgemeinen nicht, selbst dann nicht, wenn das Integral für jeden Parameter konvergiert.

Sei

$$f(x,t)=\frac{\sin(tx)}t\quad\text{für }t\neq0,\qquad f(x,0)=x .$$

Diese Funktion ist stetig auf $\mathbb{R}\times[0,\infty)$, denn $\frac{\sin(tx)}t\to x$ für $t\to0$. Bekannt ist $\int_{-\infty}^\infty\frac{\sin t}t\,\mathrm{d} t=\pi$. Der Integrand ist gerade, also ist $\int_0^\infty\frac{\sin s}s\,\mathrm{d} s=\frac\pi2$. Für $x>0$ ergibt die Substitution $s=tx$ denselben Wert, für $x<0$ wegen $\sin(-s)=-\sin s$ den Wert mit Minus, und für $x=0$ ist der Integrand null:

<span class="anker" id="gl-2-1"></span>
$$F(x)=\int_0^\infty f(x,t)\,\mathrm{d} t=\begin{cases}\pi/2,&x>0,\\0,&x=0,\\-\pi/2,&x<0.\end{cases} \tag{2.1}$$

Das Parameterintegral springt bei $x=0$, obwohl $f$ überall stetig ist und das Integral für jedes $x$ konvergiert.

:::abbildung hm3/k2sprung 5
Links $F_T(x)$ über $T$: Bei $x=0{,}2$ dauert die Annäherung an $\pi/2$ fünfmal so lang wie bei $x=1$. Rechts dieselben Integrale über $x$: Jede Kurve ist stetig, aber der Übergang bei $x=0$ wird mit wachsendem $T$ immer steiler. Im Grenzwert entsteht ein Sprung.
:::

**Der Mechanismus.** Dieselbe Substitution zeigt für $x>0$:

$$F_T(x)=\int_0^T\frac{\sin(tx)}t\,\mathrm{d} t=\int_0^{Tx}\frac{\sin s}s\,\mathrm{d} s .$$

Es zählt nur das Produkt $Tx$. Bei $x=0{,}01$ braucht man ein hundertmal größeres $T$ als bei $x=1$, um denselben Abstand zu $\pi/2$ zu erreichen (Abb. [5](#abb-5)). Je näher $x$ bei null liegt, desto langsamer konvergiert das Integral, und kein einzelnes $T$ reicht für alle $x$. Jedes $F_T$ ist stetig und hat bei $x=0$ den Wert $0$; erst der Grenzwert springt.

⁠**Kurz gesagt:** Ein uneigentliches Parameterintegral eines stetigen Integranden kann unstetig sein, wenn es für manche Parameter immer langsamer konvergiert.

### Gleichmäßige Konvergenz

<span class="anker" id="stufe-2-8"></span>

Im letzten Beispiel hängt die Geschwindigkeit, mit der $F_T(x)$ gegen $F(x)$ strebt, vom Parameter ab. Fordert man dieselbe Geschwindigkeit für alle Parameter, dann bleibt die Stetigkeit erhalten.

Was nach dem Abschneiden bei $T$ fehlt, ist das Restintegral $\int_T^\infty f(\boldsymbol{x},t)\,\mathrm{d} t$. Es soll für alle Parameter zugleich klein werden, sobald $T$ groß genug ist.

:::definition Definition 2.3 (Gleichmäßige Konvergenz)
<span class="anker" id="satz-2-3"></span>

Das uneigentliche Parameterintegral $\int_a^\infty f(\boldsymbol{x},t)\,\mathrm{d} t$ heißt in $\mathcal U$ __gleichmäßig konvergent__, wenn es zu jedem $\varepsilon>0$ ein $T_0$ gibt, das nicht von $\boldsymbol{x}$ abhängt, mit

$$\Bigl|\int_T^\infty f(\boldsymbol{x},t)\,\mathrm{d} t\Bigr|<\varepsilon\quad\text{für alle }T\ge T_0\text{ und alle }\boldsymbol{x}\in\mathcal U .$$
:::

::::beispiel
$\int_0^\infty\mathrm{e}^{-t}\cos(xt)\,\mathrm{d} t$ ist auf $\mathbb{R}$ gleichmäßig konvergent, denn $\bigl|\int_T^\infty\mathrm{e}^{-t}\cos(xt)\,\mathrm{d} t\bigr|\le\int_T^\infty\mathrm{e}^{-t}\,\mathrm{d} t=\mathrm{e}^{-T}$ für jedes $x$. Zu $\varepsilon$ passt $T_0=\ln(1/\varepsilon)$. Das Integral [(2.1)](#gl-2-1) ist auf $(0,\infty)$ dagegen nicht gleichmäßig konvergent: Zu jedem $T$ wähle $x=1/T$. Dann ist das Restintegral $\int_{Tx}^\infty\frac{\sin s}s\,\mathrm{d} s=\int_1^\infty\frac{\sin s}s\,\mathrm{d} s\approx0{,}625$, egal wie groß $T$ ist.
::::

:::satz Satz 2.4 (Gleichmäßig konvergente Parameterintegrale)
<span class="anker" id="satz-2-4"></span>

Sei $\mathcal U\subset\mathbb{R}^n$ offen, $f\colon\mathcal U\times[a,\infty)\to\mathbb{R}$ stetig und $\int_a^\infty f(\boldsymbol{x},t)\,\mathrm{d} t$ in $\mathcal U$ gleichmäßig konvergent. Dann ist $F(\boldsymbol{x})=\int_a^\infty f(\boldsymbol{x},t)\,\mathrm{d} t$ stetig in $\mathcal U$.
:::

:::beweis Ein endliches Stück und ein kleiner Rest
Sei $\boldsymbol{x}\in\mathcal U$ und $\varepsilon>0$. Wähle $T\ge T_0$ so, dass das Restintegral für alle Parameter kleiner als $\varepsilon/3$ ist. Dann gilt für jedes $\boldsymbol{y}\in\mathcal U$

$$|F(\boldsymbol{y})-F(\boldsymbol{x})|\le|F_T(\boldsymbol{y})-F_T(\boldsymbol{x})|+\Bigl|\int_T^\infty f(\boldsymbol{y},t)\,\mathrm{d} t\Bigr|+\Bigl|\int_T^\infty f(\boldsymbol{x},t)\,\mathrm{d} t\Bigr|<|F_T(\boldsymbol{y})-F_T(\boldsymbol{x})|+\frac{2\varepsilon}3 .$$

Nach Satz [1.7](integrale-mit-parameter-uber-endlichen-intervallen.html#satz-1-7) ist $F_T$ stetig, also ist der erste Summand kleiner als $\varepsilon/3$, sobald $\boldsymbol{y}$ nahe genug bei $\boldsymbol{x}$ liegt. Dann ist $|F(\boldsymbol{y})-F(\boldsymbol{x})|<\varepsilon$. Entscheidend ist, dass $T$ für $\boldsymbol{x}$ und $\boldsymbol{y}$ dasselbe sein darf; das liefert die Gleichmäßigkeit.
:::

⁠**Kurz gesagt:** Wird das Restintegral für alle Parameter zugleich klein, dann ist das uneigentliche Parameterintegral stetig.

### Majorante und Majorantenkriterium

<span class="anker" id="stufe-2-9"></span>

Die gleichmäßige Konvergenz direkt nachzuprüfen, ist mühsam. Bequemer ist eine einzige feste Funktion, die über allen Kurven der Schar liegt und selbst ein endliches Integral hat.

Abb. [6](#abb-6) zeigt das für die Kurven $\mathrm{e}^{-t}\cos(xt)$. Wie schnell sie auch schwingen, sie bleiben alle zwischen $-\mathrm{e}^{-t}$ und $\mathrm{e}^{-t}$. Die Funktion $\mathrm{e}^{-t}$ wirkt wie ein Dach über der ganzen Schar.

:::abbildung hm3/k2dach 6
Die Kurven $\mathrm{e}^{-t}\cos(xt)$ für $x=0$ (grau, sie fällt mit $g$ zusammen), $x=2$ und $x=5$. Alle liegen zwischen $-g$ und $g$ mit $g(t)=\mathrm{e}^{-t}$ (rot gestrichelt). Die Schranke $g$ hängt nicht von $x$ ab, und ihr Integral über $[0,\infty)$ ist $1$.
:::

:::satz Satz 2.5 (Majorantenkriterium)
<span class="anker" id="satz-2-5"></span>

Sei $\mathcal U\subset\mathbb{R}^n$ offen, $-\infty\le a<b\le\infty$ und $f\colon\mathcal U\times(a,b)\to\mathbb{R}$ stetig. Es gebe eine uneigentlich integrierbare Funktion $g\colon(a,b)\to\mathbb{R}$ mit

<span class="anker" id="gl-2-2"></span>
$$|f(\boldsymbol{x},t)|\le g(t)\quad\text{in }\mathcal U\times(a,b),\qquad\int_a^bg(t)\,\mathrm{d} t<\infty . \tag{2.2}$$

Dann ist das Parameterintegral $F(\boldsymbol{x})=\int_a^bf(\boldsymbol{x},t)\,\mathrm{d} t$ stetig in $\mathcal U$. Sind ferner die partiellen Ableitungen $\partial f/\partial x_k$ stetig in $\mathcal U\times(a,b)$, und gibt es uneigentlich integrierbare Funktionen $G_k\colon(a,b)\to\mathbb{R}$ mit

<span class="anker" id="gl-2-3"></span>
$$\Bigl|\frac{\partial f}{\partial x_k}(\boldsymbol{x},t)\Bigr|\le G_k(t)\quad\text{in }\mathcal U\times(a,b),\qquad\int_a^bG_k(t)\,\mathrm{d} t<\infty , \tag{2.3}$$

dann ist $F$ stetig differenzierbar in $\mathcal U$, und Ableitung und Integral dürfen vertauscht werden wie in [(1.3)](integrale-mit-parameter-uber-endlichen-intervallen.html#gl-1-3).
:::

Eine Funktion $g$ wie in [(2.2)](#gl-2-2) heißt __Majorante__ des Integranden.

⁠**So liest man das:** Eine Majorante ist eine Vergleichsfunktion aus Unterabschnitt [2.3](#stufe-2-3), die für *alle* Parameter zugleich passt. Entscheidend ist, dass $g$ nur von $t$ abhängt, nicht von $\boldsymbol{x}$. Das Intervall $(a,b)$ darf unendlich sein, und der Integrand darf an den Enden unbeschränkt werden.

:::beweis Die Majorante macht den Rest für alle Parameter klein
Seien $[a_T,b_T]\subset(a,b)$ abgeschlossene Stücke mit $a_T\to a$ und $b_T\to b$ für $T\to\infty$, und $F_T(\boldsymbol{x})=\int_{a_T}^{b_T}f(\boldsymbol{x},t)\,\mathrm{d} t$. Wegen [(2.2)](#gl-2-2) gilt für alle $\boldsymbol{x}\in\mathcal U$

$$|F(\boldsymbol{x})-F_T(\boldsymbol{x})|\le r_T:=\int_a^{a_T}g(t)\,\mathrm{d} t+\int_{b_T}^bg(t)\,\mathrm{d} t,\qquad r_T\to0 .$$

Weil $r_T$ nicht von $\boldsymbol{x}$ abhängt, ist das die gleichmäßige Konvergenz, und wie im Beweis von Satz [2.4](#satz-2-4) folgt die Stetigkeit von $F$.

Für die Ableitung sei $I_k(\boldsymbol{x})=\int_a^b\frac{\partial f}{\partial x_k}(\boldsymbol{x},t)\,\mathrm{d} t$. Nach dem ersten Teil, angewendet auf $\partial f/\partial x_k$ mit der Majorante $G_k$, ist $I_k$ stetig. Wie eben ist $\bigl|\partial_{x_k}F_T(\boldsymbol{y})-I_k(\boldsymbol{y})\bigr|\le\tilde r_T$ für alle $\boldsymbol{y}$, mit den Resten $\tilde r_T$ von $G_k$ statt $g$; dabei ist $\partial_{x_k}F_T=\int_{a_T}^{b_T}\partial_{x_k}f\,\mathrm{d} t$ nach Satz [1.8](integrale-mit-parameter-uber-endlichen-intervallen.html#satz-1-8). Der Hauptsatz gibt für kleine $h$

$$F_T(\boldsymbol{x}+h\,\hat{\boldsymbol{e}}_k)-F_T(\boldsymbol{x})=\int_0^h\partial_{x_k}F_T(\boldsymbol{x}+s\,\hat{\boldsymbol{e}}_k)\,\mathrm{d} s .$$

Für $T\to\infty$ geht die linke Seite gegen $F(\boldsymbol{x}+h\,\hat{\boldsymbol{e}}_k)-F(\boldsymbol{x})$, die rechte unterscheidet sich von $\int_0^hI_k(\boldsymbol{x}+s\,\hat{\boldsymbol{e}}_k)\,\mathrm{d} s$ um höchstens $|h|\,\tilde r_T\to0$. Also ist $F(\boldsymbol{x}+h\,\hat{\boldsymbol{e}}_k)-F(\boldsymbol{x})=\int_0^hI_k(\boldsymbol{x}+s\,\hat{\boldsymbol{e}}_k)\,\mathrm{d} s$, und weil $I_k$ stetig ist, folgt mit dem Hauptsatz $\partial_{x_k}F(\boldsymbol{x})=I_k(\boldsymbol{x})$.
:::

⁠**Warum $g$ nicht von $\boldsymbol{x}$ abhängen darf:** Für das Beispiel [(2.1)](#gl-2-1) müsste $g(t)\ge\sup_x\frac{|\sin(tx)|}t=\frac1t$ gelten, denn das Supremum wird bei $tx=\pi/2$ angenommen. Aber $\int_1^\infty\frac{\mathrm{d} t}t=\infty$. Es gibt also keine Majorante, und $F$ darf springen.

::::beispiel
$F(x)=\int_0^\infty\mathrm{e}^{-t}\cos(xt)\,\mathrm{d} t$ auf $\mathbb{R}$. Hier passen $g(t)=\mathrm{e}^{-t}$ und $G(t)=t\,\mathrm{e}^{-t}$, denn $|\partial_x(\mathrm{e}^{-t}\cos(xt))|=|t\,\mathrm{e}^{-t}\sin(xt)|\le t\,\mathrm{e}^{-t}$; beide sind über $[0,\infty)$ integrierbar. Also ist $F$ stetig differenzierbar mit

$$F'(x)=-\int_0^\infty t\,\mathrm{e}^{-t}\sin(xt)\,\mathrm{d} t .$$

Zweimal partiell integriert ist $F(x)=\frac1{1+x^2}$, also $F'(1)=-\frac12$, und das Integral ergibt denselben Wert.
::::

⁠**Grenzfall:** $F(0)=\int_0^\infty\mathrm{e}^{-t}\,\mathrm{d} t=1$.

:::hintergrund Wie Fläche verloren gehen kann: drei Fluchtwege
Hinter allen Gegenbeispielen steckt dasselbe Bild. Für jedes feste $t$ geht der Integrand gegen einen Grenzwert, die Fläche aber nicht gegen die Fläche des Grenzwerts. Die Fläche entkommt auf einem von drei Wegen (Abb. [7](#abb-7)); diese Einteilung ist in der Analysis gebräuchlich. Sie kann nach oben fliehen, in eine immer höhere und schmalere Spitze, wie in Abb. [3](integrale-mit-parameter-uber-endlichen-intervallen.html#abb-3). Sie kann in die Breite fliehen: Die Kurve wird flacher und breiter, an jeder Stelle geht sie gegen null, aber die Fläche bleibt. Und sie kann nach rechts fliehen: Ein Buckel fester Form wandert ins Unendliche, an jeder festen Stelle ist er irgendwann vorbei.

Eine Majorante versperrt alle drei Wege. Unter dem festen Dach $g$ kann keine Spitze höher werden als $g$, und in einem schmalen Streifen hat $g$ selbst nur wenig Fläche. Weit draußen ist $\int_T^\infty g\,\mathrm{d} t$ klein, und mehr Fläche kann dort auch der Integrand nicht haben, für welchen Parameter auch immer. Die Fläche bleibt also eingesperrt. Bemerkenswert ist, dass alle drei Fluchtwege mit positiven Funktionen funktionieren: Absolute Konvergenz für jeden einzelnen Parameter hilft nicht, es kommt allein darauf an, ob ein gemeinsames Dach existiert.

:::abbildung hm3/k2flucht 7
Drei Kurvenscharen, jede Kurve mit der Fläche $1$ über $[0,\infty)$; an jeder festen Stelle $t$ gehen die Werte für $x\to0$ gegen null. Links $\frac1x\mathrm{e}^{-t/x}$ und in der Mitte $x\,\mathrm{e}^{-xt}$, jeweils für $x=1$ (blau), $x=\frac12$ (orange) und $x=\frac14$ (rot). Rechts ein Dreieck der Höhe $1$ und der Breite $2$ um die Stelle $t=1/x$, für $x=1$, $x=\frac13$ und $x=\frac16$. Keine der drei Scharen hat eine Majorante.
:::
:::

⁠**Kurz gesagt:** Liegt der Betrag des Integranden für alle Parameter unter derselben integrierbaren Funktion, dann ist das uneigentliche Parameterintegral stetig; mit Majoranten für die Ableitungen darf man unter dem Integral ableiten.

### Die Fourier-Transformation

<span class="anker" id="stufe-2-10"></span>

Ein wichtiges uneigentliches Parameterintegral ordnet einer Funktion $f$ eine neue Funktion zu. Ihr Parameter $\xi$ ist eine Kreisfrequenz.

Man multipliziert $f(x)$ mit der Schwingung $\mathrm{e}^{-\mathrm i\xi x}$ und integriert über die ganze Achse. Das Ergebnis misst, wie stark $f$ mit dieser Schwingung übereinstimmt. Für jedes $\xi$ erhält man eine komplexe Zahl.

:::definition Definition 2.6 (Fourier-Transformation)
<span class="anker" id="satz-2-6"></span>

Sei $f\colon\mathbb{R}\to\mathbb{C}$ stetig und absolut uneigentlich integrierbar, also $\int_\mathbb{R}|f(x)|\,\mathrm{d} x<\infty$. Die Funktion

<span class="anker" id="gl-2-4"></span>
$$\hat f(\xi)=\frac1{\sqrt{2\pi}}\int_\mathbb{R} f(x)\,\mathrm{e}^{-\mathrm i\xi x}\,\mathrm{d} x,\qquad\xi\in\mathbb{R}, \tag{2.4}$$

heißt die __Fourier-Transformierte__ von $f$.
:::

Hier ist $\xi$ der Parameter und $x$ die Integrationsvariable. Der Vorfaktor $1/\sqrt{2\pi}$ ist eine Vereinbarung; andere Bücher wählen andere Vorfaktoren.

:::satz Satz 2.7 (Eigenschaften der Fourier-Transformierten)
<span class="anker" id="satz-2-7"></span>

Für stetiges, absolut uneigentlich integrierbares $f\colon\mathbb{R}\to\mathbb{C}$ ist $\hat f$ stetig und beschränkt, mit $|\hat f(\xi)|\le\frac1{\sqrt{2\pi}}\int_\mathbb{R}|f|\,\mathrm{d} x$. Sind für ein $k\in\mathbb{N}$ und alle $0\le j\le k$ die Funktionen $x\mapsto x^jf(x)$ absolut integrierbar, dann ist $\hat f$ $k$-mal stetig differenzierbar, und $\xi\mapsto\hat f^{(j)}(\xi)$ ist die Fourier-Transformierte von $x\mapsto(-\mathrm ix)^jf(x)$.
:::

:::beweis Majoranten, die nicht von $\xi$ abhängen
Wegen $|\mathrm{e}^{-\mathrm i\xi x}|=1$ ist $|f(x)\,\mathrm{e}^{-\mathrm i\xi x}|/\sqrt{2\pi}=|f(x)|/\sqrt{2\pi}=:g(x)$. Das ist eine Majorante, die nicht von $\xi$ abhängt. Satz [2.5](#satz-2-5), angewendet auf Real- und Imaginärteil mit $\mathcal U=\mathbb{R}$, gibt die Stetigkeit, und die Abschätzung aus Unterabschnitt [2.5](#stufe-2-5) gibt $|\hat f(\xi)|\le\int_\mathbb{R} g\,\mathrm{d} x$. Die Ableitung nach $\xi$ trifft nur die Schwingung: $\partial_\xi\bigl(f(x)\,\mathrm{e}^{-\mathrm i\xi x}\bigr)=(-\mathrm ix)f(x)\,\mathrm{e}^{-\mathrm i\xi x}$, mit der Majorante $|x\,f(x)|/\sqrt{2\pi}$. Satz [2.5](#satz-2-5) erlaubt also das Ableiten unter dem Integral, und das Ergebnis ist die Fourier-Transformierte von $(-\mathrm ix)f(x)$. Wiederholt man das $k$-mal, folgt die Aussage.
:::

::::beispiel
$f(x)=\mathrm{e}^{-|x|}$. Der Imaginärteil $-\mathrm{e}^{-|x|}\sin(\xi x)$ ist ungerade in $x$ und integriert sich zu null. Mit $\int_0^\infty\mathrm{e}^{-x}\cos(\xi x)\,\mathrm{d} x=\frac1{1+\xi^2}$ aus dem letzten Unterabschnitt folgt

$$\hat f(\xi)=\frac2{\sqrt{2\pi}}\int_0^\infty\mathrm{e}^{-x}\cos(\xi x)\,\mathrm{d} x=\sqrt{\frac2\pi}\,\frac1{1+\xi^2}.$$

Die Funktion $x\,\mathrm{e}^{-|x|}$ ist absolut integrierbar, also ist $\hat f$ stetig differenzierbar. Zur Kontrolle der Ableitungsregel: Die Fourier-Transformierte von $(-\mathrm ix)\mathrm{e}^{-|x|}$ ist $-\frac2{\sqrt{2\pi}}\int_0^\infty x\,\mathrm{e}^{-x}\sin(\xi x)\,\mathrm{d} x=-\frac2{\sqrt{2\pi}}\cdot\frac{2\xi}{(1+\xi^2)^2}$, und das ist $\frac{\mathrm{d}}{\mathrm{d}\xi}\sqrt{\frac2\pi}\frac1{1+\xi^2}$.
::::

:::hintergrund Warum jede Ableitung einen Faktor $-\mathrm ix$ bringt und was das bedeutet
Der Parameter $\xi$ steckt nur in der Schwingung $\mathrm{e}^{-\mathrm i\xi x}$, und deren Ableitung nach $\xi$ ist $-\mathrm ix$ mal sie selbst. Jede Ableitung von $\hat f$ multipliziert den Integranden also mit $-\mathrm ix$. Dieser Faktor wächst mit $|x|$. Damit das Integral danach noch konvergiert und eine Majorante hat, muss $f$ für große $|x|$ schnell genug abfallen. Daraus ergibt sich ein Zusammenhang, der die Fourier-Transformation durchzieht: Je schneller $f$ abfällt, desto öfter lässt sich $\hat f$ ableiten. Im Beispiel fällt $\mathrm{e}^{-|x|}$ schneller als jede Potenz, und $\hat f$ ist beliebig oft differenzierbar.
:::

⁠**Kurz gesagt:** Die Fourier-Transformierte einer absolut integrierbaren Funktion ist stetig und beschränkt; jede Ableitung nach $\xi$ entspricht einem Faktor $-\mathrm ix$ im Integranden.

### Lokale Majoranten

<span class="anker" id="stufe-2-11"></span>

Für viele wichtige Parameterintegrale gibt es keine Majorante, die für alle Parameter zugleich gilt. Man braucht sie aber auch nicht.

Stetigkeit und Differenzierbarkeit in einem Punkt hängen nur davon ab, wie sich eine Funktion in einer beliebig kleinen Umgebung dieses Punkts verhält. Eigenschaften dieser Art heißen __lokal__. Es genügt deshalb, um jeden Punkt herum eine eigene Majorante zu finden. Verschiedene Punkte dürfen verschiedene Majoranten haben.

:::abbildung hm3/k2majorante 8
Für $x_0=1$ liegen alle Kurven $\mathrm{e}^{-xt}$ mit $x>\frac12$ unter der Majorante $g(t)=\mathrm{e}^{-t/2}$. Die Kurve zu $x=0{,}2$ gehört nicht zu dieser Umgebung und läuft darüber; sie bekommt ihre eigene Majorante.
:::

:::satz Satz 2.8 (Lokale Majoranten)
<span class="anker" id="satz-2-8"></span>

Sei $\mathcal U\subset\mathbb{R}^n$ offen und $f\colon\mathcal U\times(a,b)\to\mathbb{R}$ stetig. Gibt es zu jedem Punkt $\boldsymbol{x}_0\in\mathcal U$ eine offene Umgebung $\mathcal V(\boldsymbol{x}_0)\subset\mathcal U$ von $\boldsymbol{x}_0$, auf der die Voraussetzungen von Satz [2.5](#satz-2-5) gelten, mit Majoranten, die von $\boldsymbol{x}_0$ abhängen dürfen, dann gelten dessen Aussagen auf ganz $\mathcal U$.
:::

⁠**So liest man das:** Man wendet Satz [2.5](#satz-2-5) auf die offene Menge $\mathcal V(\boldsymbol{x}_0)$ statt auf $\mathcal U$ an. Er liefert Stetigkeit und Differenzierbarkeit in $\mathcal V(\boldsymbol{x}_0)$, insbesondere im Punkt $\boldsymbol{x}_0$. Weil das für jeden Punkt geht, gilt es überall.

::::beispiel
$F(x)=\int_0^\infty\mathrm{e}^{-xt}\,\mathrm{d} t=\frac1x$ auf $\mathcal U=(0,\infty)$. Für festes $t$ ist $\sup_{x>0}\mathrm{e}^{-xt}=1$, und die Konstante $1$ ist über $(0,\infty)$ nicht integrierbar; eine Majorante für alle $x>0$ gibt es also nicht. Zu $x_0>0$ wähle aber $\mathcal V(x_0)=(x_0/2,\infty)$. Dort ist $\mathrm{e}^{-xt}\le\mathrm{e}^{-x_0t/2}$ und $|\partial_x\mathrm{e}^{-xt}|=t\,\mathrm{e}^{-xt}\le t\,\mathrm{e}^{-x_0t/2}$, beides integrierbar (Abb. [8](#abb-8)). Also ist $F$ stetig differenzierbar mit $F'(x)=-\int_0^\infty t\,\mathrm{e}^{-xt}\,\mathrm{d} t=-\frac1{x^2}$, wie die Formel $F=1/x$ bestätigt.
::::

⁠**Kurz gesagt:** Eine Majorante in der Nähe jedes Punkts genügt, weil Stetigkeit und Differenzierbarkeit lokale Eigenschaften sind.

### Die Gamma-Funktion

<span class="anker" id="stufe-2-12"></span>

Hier steckt der Parameter nicht in einer $\mathrm{e}$-Funktion, sondern im Exponenten einer Potenz. Das Integral setzt die Fakultät $n!$ auf alle positiven Zahlen fort.

Man stellt sich die Kurven $t^{x-1}\mathrm{e}^{-t}$ vor: Für großes $x$ steigen sie zuerst stark an, bevor die $\mathrm{e}$-Funktion sie herunterdrückt; für $x<1$ sind sie bei $t=0$ unbeschränkt. Die Fläche darunter hängt vom Exponenten ab.

:::definition Definition 2.9 (Gamma-Funktion)
<span class="anker" id="satz-2-9"></span>

Für $x>0$ heißt

<span class="anker" id="gl-2-5"></span>
$$\Gamma(x)=\int_0^\infty\mathrm{e}^{-t}\,t^{x-1}\,\mathrm{d} t \tag{2.5}$$

die __Gamma-Funktion__.
:::

:::satz Satz 2.10 (Ableitung der Gamma-Funktion)
<span class="anker" id="satz-2-10"></span>

$\Gamma$ ist stetig differenzierbar auf $(0,\infty)$, und es gilt

<span class="anker" id="gl-2-6"></span>
$$\Gamma'(x)=\int_0^\infty\mathrm{e}^{-t}\,t^{x-1}\ln t\,\mathrm{d} t . \tag{2.6}$$
:::

:::beweis Lokale Majorante
Beim Ableiten nach $x$ entsteht $\partial_xt^{x-1}=\partial_x\mathrm{e}^{(x-1)\ln t}=t^{x-1}\ln t$. Zu $x_0>0$ sei $\mathcal V(x_0)=(x_0/2,\,2x_0)$. Für $x\in\mathcal V(x_0)$ ist $t^{x-1}\le t^{x_0/2-1}$ für $0<t\le1$ und $t^{x-1}\le t^{2x_0-1}$ für $t\ge1$. Also ist

$$g(t)=\mathrm{e}^{-t}\bigl(t^{x_0/2-1}+t^{2x_0-1}\bigr)$$

eine Majorante auf $\mathcal V(x_0)$. Sie ist integrierbar: Nahe $0$ wegen $x_0/2-1>-1$ (Unterabschnitt [2.2](#stufe-2-2)), für große $t$, weil die $\mathrm{e}$-Funktion gewinnt. Für die Ableitung nimmt man $g(t)\,|\ln t|$ als Majorante (Aufgabe [7](#aufg-7)). Nach Satz [2.8](#satz-2-8) folgt die Behauptung.
:::

::::beispiel
$\Gamma(1)=\int_0^\infty\mathrm{e}^{-t}\,\mathrm{d} t=1$, und partielle Integration ergibt $\Gamma(2)=\int_0^\infty t\,\mathrm{e}^{-t}\,\mathrm{d} t=1$. Nach [(2.6)](#gl-2-6) ist $\Gamma'(1)=\int_0^\infty\mathrm{e}^{-t}\ln t\,\mathrm{d} t\approx-0{,}577$. Die Ableitung ist negativ, weil $\ln t<0$ auf $(0,1)$ ist und dieser Teil hier überwiegt.
::::

:::hintergrund Wozu die Gamma-Funktion: die Fakultät für alle positiven Zahlen
Partielle Integration ergibt $\Gamma(x+1)=x\,\Gamma(x)$ (Aufgabe [7](#aufg-7)). Das ist dieselbe Regel wie $(n+1)!=(n+1)\cdot n!$, nur um eins verschoben. Mit $\Gamma(1)=1$ folgt $\Gamma(n+1)=n!$ für jede natürliche Zahl $n$. Die Gamma-Funktion ist also eine glatte Kurve durch die Punkte $(n+1,\,n!)$, und sie liefert Werte dazwischen. Zum Beispiel ergibt die Substitution $t=s^2$ mit dem bekannten Wert $\int_0^\infty\mathrm{e}^{-s^2}\,\mathrm{d} s=\sqrt\pi/2$

$$\Gamma\bigl(\tfrac12\bigr)=\int_0^\infty\mathrm{e}^{-t}\,t^{-1/2}\,\mathrm{d} t=2\int_0^\infty\mathrm{e}^{-s^2}\,\mathrm{d} s=\sqrt\pi .$$

Eine „halbe Fakultät“ ist also $\Gamma(\tfrac32)=\tfrac12\Gamma(\tfrac12)=\tfrac{\sqrt\pi}2\approx0{,}886$.
:::

⁠**Kurz gesagt:** Die Gamma-Funktion setzt die Fakultät fort; abgeleitet wird sie unter dem Integral, wobei der Faktor $\ln t$ entsteht.

### Die Laplace-Transformation

<span class="anker" id="stufe-2-13"></span>

Viele Funktionen der Zeit wachsen für große $t$ an und haben deshalb kein endliches Integral über $[0,\infty)$. Multipliziert man sie mit einer abklingenden $\mathrm{e}$-Funktion, wird das Integral endlich.

Man dämpft die Funktion $f(t)$ mit $\mathrm{e}^{-xt}$. Die Dämpfung $x>0$ ist der Parameter. Je stärker man dämpft, desto mehr zählt nur der Anfang von $f$.

Eine Funktion $f\colon[0,\infty)\to\mathbb{R}$ hat __höchstens polynomiales Wachstum__, wenn es Konstanten $C$ und $m\in\mathbb{N}$ gibt mit $|f(t)|\le C\,(1+t^m)$ für alle $t\ge0$.

:::definition Definition 2.11 (Laplace-Transformation)
<span class="anker" id="satz-2-11"></span>

Sei $f\colon[0,\infty)\to\mathbb{R}$ stetig mit höchstens polynomialem Wachstum. Die Funktion

<span class="anker" id="gl-2-7"></span>
$$F(x)=\mathcal{L} f(x)=\int_0^\infty f(t)\,\mathrm{e}^{-xt}\,\mathrm{d} t,\qquad x>0, \tag{2.7}$$

heißt die (reelle) __Laplace-Transformierte__ von $f$.
:::

:::satz Satz 2.12 (Ableitungen der Laplace-Transformierten)
<span class="anker" id="satz-2-12"></span>

Die Laplace-Transformierte ist für jedes $x>0$ erklärt und auf $(0,\infty)$ beliebig oft differenzierbar. Für alle $k\in\mathbb{N}$ gilt

<span class="anker" id="gl-2-8"></span>
$$F^{(k)}(x)=\int_0^\infty(-t)^kf(t)\,\mathrm{e}^{-xt}\,\mathrm{d} t,\qquad\text{also}\qquad\frac{\mathrm{d}^k}{\mathrm{d} x^k}(\mathcal{L} f)(x)=\mathcal{L}\bigl((-t)^kf(t)\bigr)(x). \tag{2.8}$$
:::

:::herleitung Lokale Majorante
Sei $x_0>0$ und $\mathcal V(x_0)=(x_0/2,\infty)$. Für $x\in\mathcal V(x_0)$ gilt

$$|f(t)\,\mathrm{e}^{-xt}|\le|f(t)|\,\exp\bigl(-\tfrac12x_0t\bigr)\le C_1\exp\bigl(-\tfrac14x_0t\bigr)=:g(t)$$

mit einer Konstanten $C_1>0$. Denn $|f(t)|\exp(-\frac14x_0t)\le C(1+t^m)\exp(-\frac14x_0t)$ ist beschränkt: Die $\mathrm{e}$-Funktion gewinnt gegen die Potenz. Weil $g$ über $(0,\infty)$ integrierbar ist, folgt aus dem Majorantenkriterium die Stetigkeit von $F$ in $\mathcal V(x_0)$, und weil $x_0>0$ beliebig ist, auf ganz $(0,\infty)$. Für die Ableitungen wiederholt man das Argument: Es ist $\partial_x\mathrm{e}^{-xt}=-t\,\mathrm{e}^{-xt}$, und $(-t)^kf(t)$ wächst wieder höchstens polynomial. Mit Satz [2.8](#satz-2-8) folgt [(2.8)](#gl-2-8) Schritt für Schritt für $k=1,2,\dots$
:::

⁠**So liest man das:** Jede Ableitung nach $x$ zieht einen Faktor $-t$ aus der Dämpfung $\mathrm{e}^{-xt}$ heraus.

::::beispiel
Für $f=1$ ist $\mathcal{L}1(x)=\frac1x$. Nach [(2.8)](#gl-2-8) ist $\mathcal{L}\bigl((-t)^k\bigr)(x)=\frac{\mathrm{d}^k}{\mathrm{d} x^k}\frac1x=\frac{(-1)^kk!}{x^{k+1}}$, also

$$\mathcal{L}(t^k)(x)=\int_0^\infty t^k\,\mathrm{e}^{-xt}\,\mathrm{d} t=\frac{k!}{x^{k+1}} .$$

Bei $k=1$ und $x=2$ ist das $\int_0^\infty t\,\mathrm{e}^{-2t}\,\mathrm{d} t=\frac14$.
::::

:::hintergrund Ein Integral für $n!$ und die Verbindung zur Gamma-Funktion
Setzt man im Beispiel $x=1$, ergibt sich $\int_0^\infty t^n\mathrm{e}^{-t}\,\mathrm{d} t=n!$, also $\Gamma(n+1)=n!$ ohne jede partielle Integration: Man hat nur das einfache Integral $\int_0^\infty\mathrm{e}^{-xt}\,\mathrm{d} t=1/x$ $n$-mal nach dem Parameter abgeleitet. Dieser Kunstgriff, ein schwieriges Integral durch Ableiten eines leichten nach einem Parameter zu gewinnen, ist eine der wichtigsten Anwendungen dieses Abschnitts. Allgemeiner ergibt die Substitution $s=xt$ für jede Zahl $a>0$

$$\mathcal{L}\bigl(t^{a-1}\bigr)(x)=\int_0^\infty t^{a-1}\mathrm{e}^{-xt}\,\mathrm{d} t=\frac1{x^a}\int_0^\infty s^{a-1}\mathrm{e}^{-s}\,\mathrm{d} s=\frac{\Gamma(a)}{x^a}.$$
:::

:::hintergrund Warum es keine Majorante für alle $x>0$ gibt
Die Dämpfung $\mathrm{e}^{-xt}$ wird für $x\to0$ immer schwächer. Für $f=1$ werden die Kurven $\mathrm{e}^{-xt}$ immer flacher und breiter, ähnlich wie in der Mitte von Abb. [7](#abb-7), und ihre Fläche $1/x$ wächst sogar über alle Grenzen. Ein gemeinsames Dach für alle $x>0$ müsste deshalb über der Konstanten $1$ liegen und hätte unendliche Fläche. Hält man dagegen $x$ von null fern, etwa $x>x_0/2$, dann dämpft schon $\mathrm{e}^{-x_0t/2}$ jede Potenz weg. Deshalb ist die Laplace-Transformierte auf ganz $(0,\infty)$ glatt, obwohl es keine globale Majorante gibt.
:::

⁠**Kurz gesagt:** Die Laplace-Transformierte dämpft $f$ mit $\mathrm{e}^{-xt}$; sie ist für $x>0$ beliebig oft differenzierbar, und jede Ableitung bringt einen Faktor $-t$.

### Aufgaben

<span class="anker" id="stufe-2-14"></span>

:::aufgabe Aufgabe 6 ★★ Absolute Konvergenz reicht nicht
<span class="anker" id="aufg-6"></span>

<ol class="al">

<li>

Sei $f(x,t)=x\,\mathrm{e}^{-xt}$ für $x\ge0$, $t\ge0$. Berechne $F(x)=\int_0^\infty f(x,t)\,\mathrm{d} t$. Ist das Integral absolut konvergent? Ist $F$ bei $x=0$ stetig?

</li>

<li>

Berechne $\sup_{x\ge0}f(x,t)$ für festes $t>0$ und begründe, warum es keine Majorante gibt.

</li>

<li>

Zeige, dass $P(x)=\int_0^\infty\frac{\cos(xt)}{1+t^2}\,\mathrm{d} t$ auf $\mathbb{R}$ stetig ist.

</li>

</ol>

:::loesung
(a) Für $x>0$ ist $F(x)=\bigl[-\mathrm{e}^{-xt}\bigr]_{t=0}^{\infty}=1$. Für $x=0$ ist $f=0$, also $F(0)=0$. Das Integral ist für jedes $x$ absolut konvergent, denn $f\ge0$. Trotzdem ist $F$ bei $x=0$ nicht stetig.

(b) Für festes $t>0$ ist $\partial_x\bigl(x\,\mathrm{e}^{-xt}\bigr)=(1-xt)\,\mathrm{e}^{-xt}$, das Maximum liegt also bei $x=1/t$ und hat den Wert $\frac1{\mathrm{e} t}$. Eine Majorante müsste $g(t)\ge\frac1{\mathrm{e} t}$ erfüllen, und das ist auf $[1,\infty)$ nicht integrierbar. Anschaulich ist das der Fluchtweg „in die Breite“ aus Abb. [7](#abb-7): Für $x\to0$ verteilt sich die Fläche $1$ auf eine immer breitere und flachere Kurve.

(c) Es ist $\bigl|\frac{\cos(xt)}{1+t^2}\bigr|\le\frac1{1+t^2}=:g(t)$ für alle $x$, und $\int_0^\infty g\,\mathrm{d} t=\bigl[\arctan t\bigr]_0^\infty=\frac\pi2$. Der Integrand ist stetig auf $\mathbb{R}\times[0,\infty)$, also ist $P$ nach Satz [2.5](#satz-2-5) auf $\mathbb{R}$ stetig.
:::
:::

:::aufgabe Aufgabe 7 ★★ Gamma und Laplace
<span class="anker" id="aufg-7"></span>

<ol class="al">

<li>

Zeige $\Gamma(x+1)=x\,\Gamma(x)$ für $x>0$ und folgere $\Gamma(n+1)=n!$ für $n\in\mathbb{N}$.

</li>

<li>

Gib für $\partial_x\bigl(\mathrm{e}^{-t}t^{x-1}\bigr)$ eine Majorante auf $\mathcal V(x_0)=(x_0/2,\,2x_0)$ an und begründe, dass sie integrierbar ist.

</li>

<li>

Zeige, dass die Laplace-Transformation linear ist: $\mathcal{L}(\lambda_1f_1+\lambda_2f_2)=\lambda_1\mathcal{L} f_1+\lambda_2\mathcal{L} f_2$. Berechne damit $\mathcal{L}(3t^4+2t^2)(x)$.

</li>

<li>

Berechne $\mathcal{L}(t\sin t)(x)$ aus $\mathcal{L}(\sin t)(x)=\frac1{1+x^2}$.

</li>

</ol>

:::loesung
(a) Partielle Integration mit $u=t^x$ und $v'=\mathrm{e}^{-t}$:

$$\Gamma(x+1)=\int_0^\infty\mathrm{e}^{-t}t^x\,\mathrm{d} t=\Bigl[-\mathrm{e}^{-t}t^x\Bigr]_0^\infty+x\int_0^\infty\mathrm{e}^{-t}t^{x-1}\,\mathrm{d} t=x\,\Gamma(x).$$

Die Randterme verschwinden: bei $t=0$ wegen $x>0$, für $t\to\infty$, weil die $\mathrm{e}$-Funktion gewinnt. Mit $\Gamma(1)=1$ folgt $\Gamma(2)=1$, $\Gamma(3)=2\cdot1$, und allgemein $\Gamma(n+1)=n\,\Gamma(n)=\dots=n!$.

(b) Auf $\mathcal V(x_0)$ ist $\bigl|\partial_x\bigl(\mathrm{e}^{-t}t^{x-1}\bigr)\bigr|=\mathrm{e}^{-t}t^{x-1}|\ln t|\le G(t):=\mathrm{e}^{-t}\bigl(t^{x_0/2-1}+t^{2x_0-1}\bigr)|\ln t|$. Integrierbar nahe $0$: Es ist $t^{x_0/2-1}|\ln t|=t^{x_0/4-1}\cdot t^{x_0/4}|\ln t|$, und $t^{x_0/4}|\ln t|$ ist auf $(0,1]$ beschränkt, weil es für $t\to0$ gegen null geht. Es bleibt ein Vielfaches von $t^{x_0/4-1}$, und das ist wegen $x_0/4-1>-1$ integrierbar. Für große $t$ ist $t^{2x_0-1}\ln t\le t^{2x_0}$, und die $\mathrm{e}$-Funktion gewinnt.

(c) $\mathcal{L}(\lambda_1f_1+\lambda_2f_2)(x)=\int_0^\infty(\lambda_1f_1+\lambda_2f_2)\,\mathrm{e}^{-xt}\,\mathrm{d} t=\lambda_1\mathcal{L} f_1(x)+\lambda_2\mathcal{L} f_2(x)$, weil das Integral über $[0,T]$ linear ist und Grenzwerte von Summen Summen der Grenzwerte sind. Mit $\mathcal{L}(t^k)=k!/x^{k+1}$:

$$\mathcal{L}(3t^4+2t^2)(x)=3\cdot\frac{24}{x^5}+2\cdot\frac2{x^3}=\frac{72}{x^5}+\frac4{x^3}.$$

(d) $\sin t$ ist beschränkt, hat also höchstens polynomiales Wachstum. Aus [(2.8)](#gl-2-8) mit $k=1$ folgt $\mathcal{L}(-t\sin t)=\frac{\mathrm{d}}{\mathrm{d} x}\frac1{1+x^2}$, also

$$\mathcal{L}(t\sin t)(x)=-\frac{\mathrm{d}}{\mathrm{d} x}\frac1{1+x^2}=\frac{2x}{(1+x^2)^2}.$$
:::
:::

:::aufgabe Aufgabe 8 ★★★ Kosinus unter der Glocke
<span class="anker" id="aufg-8"></span>

Sei $I(x)=\int_0^\infty\mathrm{e}^{-t^2}\cos(xt)\,\mathrm{d} t$ für $x\in\mathbb{R}$. Bekannt ist $\int_0^\infty\mathrm{e}^{-t^2}\,\mathrm{d} t=\sqrt\pi/2$.

<ol class="al">

<li>

Zeige mit Majoranten, dass $I$ stetig differenzierbar ist, und gib $I'$ als Integral an.

</li>

<li>

Zeige durch partielle Integration $I'(x)=-\frac x2I(x)$.

</li>

<li>

Löse diese Differentialgleichung mit dem Startwert $I(0)$. Welchen Wert hat $I(2)$?

</li>

</ol>

:::loesung
(a) $|\mathrm{e}^{-t^2}\cos(xt)|\le\mathrm{e}^{-t^2}$ und $|\partial_x(\mathrm{e}^{-t^2}\cos(xt))|=|t\,\mathrm{e}^{-t^2}\sin(xt)|\le t\,\mathrm{e}^{-t^2}$. Beide Schranken hängen nicht von $x$ ab und sind über $[0,\infty)$ integrierbar, $\int_0^\infty t\,\mathrm{e}^{-t^2}\,\mathrm{d} t=\frac12$. Nach Satz [2.5](#satz-2-5) ist $I$ stetig differenzierbar mit

$$I'(x)=-\int_0^\infty t\,\mathrm{e}^{-t^2}\sin(xt)\,\mathrm{d} t .$$

(b) Mit der Stammfunktion $-\frac12\mathrm{e}^{-t^2}$ von $t\,\mathrm{e}^{-t^2}$:

$$\int_0^\infty t\,\mathrm{e}^{-t^2}\sin(xt)\,\mathrm{d} t=\Bigl[-\tfrac12\mathrm{e}^{-t^2}\sin(xt)\Bigr]_0^\infty+\frac x2\int_0^\infty\mathrm{e}^{-t^2}\cos(xt)\,\mathrm{d} t=\frac x2I(x),$$

also $I'(x)=-\frac x2I(x)$.

(c) Es ist $\frac{\mathrm{d}}{\mathrm{d} x}\bigl(I(x)\,\mathrm{e}^{x^2/4}\bigr)=\bigl(I'(x)+\frac x2I(x)\bigr)\mathrm{e}^{x^2/4}=0$. Also ist $I(x)\,\mathrm{e}^{x^2/4}$ konstant, gleich $I(0)=\frac{\sqrt\pi}2$, und

$$I(x)=\frac{\sqrt\pi}2\,\mathrm{e}^{-x^2/4},\qquad I(2)=\frac{\sqrt\pi}{2\mathrm{e}}\approx0{,}326 .$$

Die Glockenkurve $\mathrm{e}^{-t^2}$ wird also wieder zu einer Glockenkurve.
:::
:::
