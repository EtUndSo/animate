---
title: Stufe 4: Stetigkeit und Epsilon-Delta
pfad: Elektrotechnik / 1. Semester / Höhere Mathematik 1 / Exponentialfunktion und Stetigkeit
order: 1250600
summary: Der Grenzwert schaut an f(x 0) vorbei.
tags: stetig, rechtsseitig stetig, linksseitig stetig, stetig ergänzbar, stetige Ergänzung
lang: de
---

<span class="anker" id="stufe-4"></span>

:::zweck
Der Grenzwert schaut an $f(x_0)$ vorbei. Stetigkeit verlangt, dass beide übereinstimmen. Das Epsilon-Delta-Kriterium macht daraus einen Toleranztest ohne Folgen.
:::

**Die Idee.** Der Funktionswert soll das sein, was man von nahebei erwartet. Das ist die Aussage „kleine Änderung am Eingang, kleine Änderung am Ausgang“. Die drei Beispiele aus Abb. [3](grenzwerte-von-funktionen.html#abb-3) scheitern daran auf verschiedene Weise.

:::definition Definition 4.1 (Stetigkeit)
<span class="anker" id="satz-4-1"></span>

Sei $f:(a,b)\to\mathbb{R}$, $x_0\in(a,b)$. Dann heißt

<ol class="rm">

<li>

$f$ in $x_0$ __stetig__, falls $\lim\limits_{x\to x_0}f(x)=f(x_0)$,

</li>

<li>

$f$ in $x_0$ __rechtsseitig stetig__, falls $\lim\limits_{x\searrow x_0}f(x)=f(x_0)$,

</li>

<li>

$f$ in $x_0$ __linksseitig stetig__, falls $\lim\limits_{x\nearrow x_0}f(x)=f(x_0)$,

</li>

<li>

$f$ auf $(a,b)$ stetig, falls $f$ in jedem Punkt von $(a,b)$ stetig ist.

</li>

</ol>

$f:[a,b]\to\mathbb{R}$ heißt auf $[a,b]$ stetig, wenn $f$ auf $(a,b)$ stetig ist, in $a$ rechtsseitig und in $b$ linksseitig stetig; entsprechend für $[a,b)$ und $(a,b]$.
:::

⁠**So liest man das:** (i) enthält drei Forderungen: $f(x_0)$ ist erklärt, der Grenzwert existiert, beide sind gleich. Polynome sind nach [(3.3)](grenzwerte-von-funktionen.html#gl-3-3) überall stetig. $H$ ist bei 0 rechtsseitig stetig, nicht aber linksseitig: $\lim_{x\nearrow0}H(x)=0\ne1=H(0)$. **Grenzfall:** Konstante Funktionen sind überall stetig, jede Änderung am Ausgang ist 0.

:::satz Satz 4.2 ($\varepsilon$-$\delta$-Kriterium für Stetigkeit)
<span class="anker" id="satz-4-2"></span>

Sei $f:(a,b)\to\mathbb{R}$, $x_0\in(a,b)$. Dann ist $f$ genau dann in $x_0$ stetig, wenn gilt

<span class="anker" id="gl-4-1"></span>
$$\forall\,\varepsilon>0\ \ \exists\,\delta_0>0:\quad|f(x)-f(x_0)|<\varepsilon\quad\forall\,x\in(x_0-\delta_0,x_0+\delta_0). \tag{4.1}$$

Gleichbedeutend: $\forall\,\varepsilon>0\ \exists\,\delta_0>0$ mit $\bigl(x\in U_{\delta_0}(x_0)\Rightarrow f(x)\in U_\varepsilon(f(x_0))\bigr)$.
:::

⁠**So liest man das:** Es ist das Spiel aus [Teil 4](/wissen/elektrotechnik/1-semester/hohere-mathematik-1/folgen-und-grenzwerte/folgen-und-grenzwerte.html). Du gibst eine Toleranz $\varepsilon$ für den Ausgang vor, ich nenne $\delta_0$ für den Eingang. Ich gewinne, wenn alle Eingänge näher als $\delta_0$ an $x_0$ einen Ausgang näher als $\varepsilon$ an $f(x_0)$ erzeugen. $\delta_0=\delta_0(\varepsilon,x_0)$ darf von $\varepsilon$ und $x_0$ abhängen und muss so klein sein, dass $(x_0-\delta_0,x_0+\delta_0)\subset(a,b)$ gilt. Geometrisch bleibt das Graphenstück über dem $\delta_0$-Streifen im $\varepsilon$-Streifen (Abb. [4](#abb-4)).

:::beweis Beide Richtungen
„$\Leftarrow$“: Es gelte [(4.1)](#gl-4-1), und $\{x_n\}$ erfülle [(3.1)](grenzwerte-von-funktionen.html#gl-3-1). Sei $\varepsilon>0$ und $\delta_0$ wie in [(4.1)](#gl-4-1). Wegen $x_n\to x_0$ gibt es $N_0$ mit $|x_n-x_0|<\delta_0$ für alle $n>N_0$, also $|f(x_n)-f(x_0)|<\varepsilon$ für diese $n$. Das heißt $f(x_n)\to f(x_0)$.

„$\Rightarrow$“ indirekt: Gilt [(4.1)](#gl-4-1) nicht, gibt es $\varepsilon_1>0$ und zu jedem $\delta_0=\frac1n$ ein $x_n$ mit $|x_n-x_0|<\frac1n$ und $|f(x_n)-f(x_0)|\ge\varepsilon_1$. Dann ist $x_n\ne x_0$ und $x_n\to x_0$, aber $f(x_n)$ läuft nicht gegen $f(x_0)$.
:::

**Beispiel.** $f(x)=x^2$ bei $x_0=2$. Es ist $|x^2-4|=|x-2|\,|x+2|$. Um den zweiten Faktor zu begrenzen, verlangt man zuerst $|x-2|<1$, dann ist $|x+2|<5$. Also ist $\delta_0:=\min\{1,\varepsilon/5\}$ eine Antwort: Für $|x-2|<\delta_0$ ist $|x^2-4|<5\,\delta_0\le\varepsilon$. Für $\varepsilon=0{,}5$ ist $\delta_0=0{,}1$, und tatsächlich liegt $x^2$ für $x\in(1{,}9;\ 2{,}1)$ zwischen $3{,}61$ und $4{,}41$. An einer Stelle $x_0>0$ gibt derselbe Weg $\delta_0=\min\{1,\varepsilon/(2x_0+1)\}$: Je steiler der Graph, desto kleiner $\delta_0$. **Grenzfall:** Für $f(x)=|x|$ gewinnt bei $x_0=0$ die Antwort $\delta_0=\varepsilon$.

:::abbildung hm1/k5epsdelta 4
$x^2$ bei $x_0=2$, $\varepsilon=0{,}5$: Über dem Streifen $(1{,}9;\ 2{,}1)$ bleibt der Graph im Streifen $(3{,}5;\ 4{,}5)$. $\delta_0=0{,}1$ ist nicht die größte Antwort, aber sie gewinnt.
:::

:::analogie
„Stetig heißt: Den Graphen zeichnen, ohne abzusetzen.“ Das Bild passt auf Intervallen. Es stimmt nicht mehr, sobald der Definitionsbereich Lücken hat: $1/x$ auf $\mathbb{R}\setminus\{0\}$ ist in jedem Punkt stetig, der Graph hat trotzdem zwei Äste.
:::

:::definition Definition 4.3 (Stetige Ergänzung)
<span class="anker" id="satz-4-3"></span>

Sei $f:\dot U_\eta(x_0)\to\mathbb{R}$ in ganz $\dot U_\eta(x_0)$ stetig, und es existiere $y_0:=\lim_{x\to x_0}f(x)\in\mathbb{R}$. Dann heißt $f$ in $x_0$ __stetig ergänzbar__. Die Funktion

$$\tilde f(x):=\begin{cases}f(x),&x\in\dot U_\eta(x_0),\\y_0,&x=x_0\end{cases}$$

heißt __stetige Ergänzung__ (oder Fortsetzung) von $f$ auf $U_\eta(x_0)$.
:::

⁠**So liest man das:** Man füllt die Stelle mit dem einzigen Wert, der den Graphen schließt. **Beispiele:** $L$ wird mit $\tilde L(2)=4$ zur Geraden $x+2$. $h(x)=\frac{\mathrm{e}^x-1}x$ hat bei 0 keinen Wert, wird aber mit $\tilde h(0)=1$ nach [(3.5)](grenzwerte-von-funktionen.html#gl-3-5) stetig. **Nicht ergänzbar:** $H$ hat bei 0 keinen Grenzwert, $|1/x|$ wächst ohne Grenze.

:::aufgabe Aufgabe 4 ★★ Toleranzspiel
<span class="anker" id="aufg-4"></span>

Sei $f(x)=\sqrt x$, $x_0=4$. (a) Zeige $|\sqrt x-2|\le\frac12|x-4|$ für $x\ge0$. (b) Gib $\delta_0(\varepsilon)$ an. (c) Wie groß ist es für $\varepsilon=0{,}1$, und wie groß wäre das größte mögliche $\delta_0$?

:::loesung
(a) $|\sqrt x-2|=\frac{|x-4|}{\sqrt x+2}\le\frac12|x-4|$. (b) $\delta_0=\min\{2\varepsilon,4\}$; die 4 hält $x$ im Definitionsbereich $x>0$. (c) $\delta_0=0{,}2$. Am größten: $\sqrt x\in(1{,}9;\ 2{,}1)$ heißt $x\in(3{,}61;\ 4{,}41)$, also $\delta_0=\min\{0{,}39;\ 0{,}41\}=0{,}39$.
:::
:::
