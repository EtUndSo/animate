---
title: Stufe 3: Sinus und Cosinus als Reihen
pfad: Elektrotechnik / 1. Semester / Höhere Mathematik 1 / Potenzreihen und Eulersche Formel
order: 1270500
summary: Die Schuldefinition am Dreieck setzt Winkel und Bogenlängen voraus, die bisher nicht definiert sind.
tags: 
lang: de
---

<span class="anker" id="stufe-3"></span>

:::zweck
Die Schuldefinition am Dreieck setzt Winkel und Bogenlängen voraus, die bisher nicht definiert sind. Diese Stufe definiert Sinus und Cosinus nur durch Rechnen und Grenzwerte.
:::

**Die Idee.** Beide Reihen sind gleich gebaut: Das Vorzeichen wechselt, und die Nenner sind Fakultäten, die schneller wachsen als jede geometrische Folge. Der Sinus enthält nur ungerade Potenzen, der Cosinus nur gerade. Dass dies die Funktionen aus der Schule sind, zeigen die Stufen [6](die-eulersche-formel.html#stufe-6) bis [8](polardarstellung-drehen-und-strecken.html#stufe-8).

:::definition Definition 3.1 (Sinusreihe und Cosinusreihe)
<span class="anker" id="satz-3-1"></span>

Für $x\in\mathbb{R}$ sei

<span class="anker" id="gl-3-1"></span>
$$\sin x:=\sum_{n=0}^\infty\frac{(-1)^n}{(2n+1)!}\,x^{2n+1},\qquad \cos x:=\sum_{n=0}^\infty\frac{(-1)^n}{(2n)!}\,x^{2n}. \tag{3.1}$$
:::

⁠**So liest man das:** Ausgeschrieben ist $\sin x=x-\frac{x^3}6+\frac{x^5}{120}-\dots$ und $\cos x=1-\frac{x^2}2+\frac{x^4}{24}-\dots$. Das Argument $x$ ist eine reine Zahl. Sie entspricht dem Winkel im Bogenmaß (Stufe [8](polardarstellung-drehen-und-strecken.html#stufe-8)).

:::satz Satz 3.2 (Eigenschaften von Sinus und Cosinus)
<span class="anker" id="satz-3-2"></span>

Beide Reihen haben den Konvergenzradius $R=\infty$. Außerdem gilt:

<ol class="rm">

<li>

$\sin$ und $\cos$ sind stetig auf $\mathbb{R}$,

</li>

<li>

$\sin(-x)=-\sin x$ und $\cos(-x)=\cos x$ für alle $x\in\mathbb{R}$,

</li>

<li>

$\cos0=1$ und $\sin0=0$,

</li>

<li>

$\lim_{x\to0}\frac{\sin x}x=1$.

</li>

</ol>
:::

⁠**So liest man das:** (ii): Die Symmetrie kommt von den Exponenten. (iv): Für kleine $x$ ist $\sin x$ fast $x$.

:::beweis Wurzelkriterium und Einsetzen
Radius: Das Quotientenkriterium scheidet aus, denn jeder zweite Koeffizient ist null. Die übrigen haben den Betrag $1/m!$. Für $m\ge2$ enthält $m!=1\cdot2\cdots m$ mindestens $m/2$ Faktoren, die mindestens $m/2$ sind. Also ist $m!\ge(m/2)^{m/2}$ und

$$0\le\sqrt[m]{\frac1{m!}}\le\sqrt{\frac2m}\to0.$$

Damit ist $B=0$ und $R=\infty$.

(i) folgt aus Satz [2.3](den-radius-ausrechnen.html#satz-2-3). (ii): $(-x)^{2n+1}=-x^{2n+1}$ und $(-x)^{2n}=x^{2n}$. (iii): Für $x=0$ bleibt nur das Glied $n=0$, beim Cosinus $0^0=1$, beim Sinus $0^1=0$. (iv): Für $x\ne0$ ist $\frac{\sin x}x=\sum_{n=0}^\infty\frac{(-1)^n}{(2n+1)!}x^{2n}$. Das ist wieder eine Potenzreihe mit $R=\infty$, also stetig in 0, mit dem Wert 1 bei $x=0$.
:::

**Beispiel.** $\sin1\approx1-\frac16+\frac1{120}=0{,}84167$. Nach Leibniz ist der Fehler höchstens das nächste Glied $\frac1{5040}\approx0{,}0002$. Genau ist $\sin1=0{,}84147$. Ebenso $\cos1\approx1-\frac12+\frac1{24}-\frac1{720}=0{,}54028$ (genau $0{,}54030$).

⁠**Grenzfall kleine $x$:** Bei $x=0{,}1$ ist $\sin x=0{,}09983$. Die Näherung $\sin x\approx x$ irrt um $1{,}7\cdot10^{-4}$, das ist fast genau $x^3/6$. Die Näherung $\cos x\approx1-x^2/2$ irrt um $4{,}2\cdot10^{-6}$, also um $x^4/24$. **Grenzfall große $x$:** Bei $x=6$ sind die Beträge der Glieder $6;\ 36;\ 64{,}8;\ 55{,}5;\ 27{,}8;\ \dots$ Sie heben sich zu $\sin6=-0{,}279$ fast auf (Abb. [3](#abb-3)).

:::abbildung hm1/k7sinus 3
Die Teilsummen $s_N=\sum_{n=0}^N\frac{(-1)^n}{(2n+1)!}x^{2n+1}$ der Sinusreihe. $s_0=x$ ist die Tangente im Nullpunkt. Jede weitere Teilsumme folgt dem Sinus ein Stück länger und läuft dann weg, weil sie ein Polynom ist.
:::

:::frage Darf ich in die Reihe Grad einsetzen?
Einsetzen lässt sich jede Zahl, aber das Ergebnis ist dann nicht der Sinus des Winkels: Die Reihe gibt $\sin30=-0{,}988$, während $\sin30^\circ=\frac12$ ist. Die Formel $\sin x\approx x$ gilt nur im Bogenmaß.
:::

:::aufgabe Aufgabe 3 ★★ Reihen auswerten
<span class="anker" id="aufg-3"></span>

(a) Berechne $\sin0{,}5$ und $\cos0{,}5$ aus je drei Gliedern und schätze den Fehler ab. (b) Wende das Quotientenkriterium für Reihen direkt auf die Glieder $b_n=\frac{(-1)^n}{(2n+1)!}x^{2n+1}$ an. Warum widerspricht das nicht dem Beweis oben? (c) Grenzfall: Zeige $\lim_{x\to0}\frac{1-\cos x}{x^2}=\frac12$.

:::loesung
(a) $\sin0{,}5\approx0{,}5-\frac{0{,}125}6+\frac{0{,}03125}{120}=0{,}479427$, Fehler höchstens $\frac{0{,}5^7}{5040}=1{,}6\cdot10^{-6}$. $\cos0{,}5\approx1-0{,}125+\frac{0{,}0625}{24}=0{,}877604$, Fehler höchstens $\frac{0{,}5^6}{720}=2{,}2\cdot10^{-5}$. Genau sind $0{,}479426$ und $0{,}877583$. (b) $\bigl|\frac{b_{n+1}}{b_n}\bigr|=\frac{x^2}{(2n+2)(2n+3)}\to0$ für jedes $x\neq0$, also absolute Konvergenz für alle $x$. Kein Widerspruch: Ausgeschlossen war nur die Formel mit den Koeffizienten $a_n$, unter denen Nullen sind. Hier stehen die Glieder ohne Nullen. (c) Für $x\ne0$ ist $\frac{1-\cos x}{x^2}=\sum_{n=1}^\infty\frac{(-1)^{n+1}}{(2n)!}x^{2n-2}=\frac12-\frac{x^2}{24}+\dots$ Diese Potenzreihe mit $R=\infty$ ist stetig und hat bei 0 den Wert $\frac12$. Bei $x=0{,}1$: $0{,}49958$.
:::
:::
