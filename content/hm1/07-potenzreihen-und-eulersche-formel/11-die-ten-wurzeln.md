---
title: Stufe 9: Die $n$-ten Wurzeln
pfad: Elektrotechnik / 1. Semester / Höhere Mathematik 1 / Potenzreihen und Eulersche Formel
order: 1271100
summary: In mathbb R hat x 3=8 eine Lösung.
tags: Einheitswurzeln
lang: de
---

<span class="anker" id="stufe-9"></span>

:::zweck
In $\mathbb{R}$ hat $x^3=8$ eine Lösung. In $\mathbb{C}$ hat $z^n=a$ immer genau $n$ Lösungen. Diese Stufe erklärt das aus der Periode der Exponentialfunktion.
:::

**Die Idee.** Die $n$-te Potenz multipliziert den Winkel mit $n$. Rückwärts teilt man den Winkel durch $n$. Der Winkel von $a$ ist aber nur bis auf volle Umläufe festgelegt: $\alpha$, $\alpha+2\pi$, $\alpha+4\pi$ sind dieselbe Richtung. Nach dem Teilen durch $n$ sind es verschiedene Richtungen, im Abstand $2\pi/n$. Multipliziert man eine Lösung mit $\mathrm{e}^{2\pi\mathrm{i}/n}$, dreht man sie um $2\pi/n$, und ihre $n$-te Potenz bleibt gleich, weil $(\mathrm{e}^{2\pi\mathrm{i}/n})^n=1$ ist. Gleicher Betrag und gleicher Winkelabstand ergeben ein regelmäßiges $n$-Eck (Abb. [9](#abb-9)).

:::satz Satz 9.1 (Eigenschaften von $\mathrm{e}^z$)
<span class="anker" id="satz-9-1"></span>

Für alle $z,w\in\mathbb{C}$ gilt:

<ol class="al">

<li>

$|\mathrm{e}^z|=\mathrm{e}^{\operatorname{Re} z}>0$, insbesondere ist $\mathrm{e}^z\ne0$,

</li>

<li>

$\mathrm{e}^z=\mathrm{e}^w\Rightarrow z=w+2\pi\mathrm{i}\,k$ für ein $k\in\mathbb{Z}$.

</li>

</ol>
:::

⁠**So liest man das:** Der Realteil von $z$ bestimmt die Länge von $\mathrm{e}^z$, der Imaginärteil die Richtung. (b): $\exp$ ist auf $\mathbb{C}$ nicht injektiv, sondern hat die Periode $2\pi\mathrm{i}$. Daher kommen die vielen Wurzeln.

:::beweis Betrag und Winkel trennen
(a) $\mathrm{e}^z=\mathrm{e}^{\operatorname{Re} z}\mathrm{e}^{\mathrm{i}\operatorname{Im} z}$ mit $|\mathrm{e}^{\mathrm{i}\operatorname{Im} z}|=1$ und reellem $\mathrm{e}^{\operatorname{Re} z}>0$.

(b) Aus $\mathrm{e}^z=\mathrm{e}^w$ und $\mathrm{e}^z\ne0$ folgt $\mathrm{e}^{w-z}=1$. Mit (a) ist $\mathrm{e}^{\operatorname{Re}(w-z)}=1$, also $\operatorname{Re}(w-z)=0$, weil die reelle Exponentialfunktion injektiv ist. Also ist $w-z=\mathrm{i}\varphi$ mit $\varphi\in\mathbb{R}$ und $\mathrm{e}^{\mathrm{i}\varphi}=1$. Schreibe $\varphi=2\pi k+\varphi_0$ mit $k\in\mathbb{Z}$ und $\varphi_0\in[0,2\pi)$. Die Periodizität gibt $\mathrm{e}^{\mathrm{i}\varphi_0}=1=\mathrm{e}^{\mathrm{i}0}$. Wegen der Eindeutigkeit in Satz [8.1](polardarstellung-drehen-und-strecken.html#satz-8-1) ist $\varphi_0=0$.
:::

:::satz Satz 9.2 ($n$-te Wurzeln)
<span class="anker" id="satz-9-2"></span>

Seien $a=|a|\,\mathrm{e}^{\mathrm{i}\alpha}\ne0$ und $n\in\mathbb{N}$. Die Gleichung $z^n=a$ hat genau die $n$ Lösungen

<span class="anker" id="gl-9-1"></span>
$$z_k=|a|^{1/n}\,\mathrm{e}^{\mathrm{i}\varphi_k}\qquad\text{mit}\qquad\varphi_k=\frac{\alpha+2\pi k}n,\quad k=0,1,\dots,n-1. \tag{9.1}$$
:::

⁠**So liest man das:** $|a|^{1/n}$ ist die reelle Wurzel aus [Teil 3](/wissen/elektrotechnik/1-semester/hohere-mathematik-1/funktionen-und-polynome/funktionen-und-polynome.html), also der Radius des Kreises. $\varphi_0$ ist der Startwinkel, und jeder Schritt dreht um $2\pi/n$. Für $a=1$ heißen die Lösungen __Einheitswurzeln__. **Gültigkeit:** Für $a=0$ ist $z=0$ die einzige Lösung.

:::beweis Betrag und Winkel vergleichen
Mit $z=|z|\,\mathrm{e}^{\mathrm{i}\varphi}$ lautet die Gleichung $|z|^n\mathrm{e}^{\mathrm{i}n\varphi}=|a|\,\mathrm{e}^{\mathrm{i}\alpha}$. Die Beträge ergeben $|z|=|a|^{1/n}$. Dann ist $\mathrm{e}^{\mathrm{i}n\varphi}=\mathrm{e}^{\mathrm{i}\alpha}$, nach Satz [9.1](#satz-9-1) (b) also $n\varphi=\alpha+2\pi k$ für ein $k\in\mathbb{Z}$. Umgekehrt löst jedes solche $\varphi$ die Gleichung. Die Werte $k=0,\dots,n-1$ ergeben verschiedene Richtungen, denn die $\varphi_k$ liegen in einem Bereich kürzer als $2\pi$. Ein um $n$ größeres $k$ ergibt $\varphi_k+2\pi$, also dieselbe Zahl.
:::

:::abbildung hm1/k7wurzeln 9
Links die drei Lösungen von $z^3=8\mathrm{i}$ auf dem Kreis mit Radius 2, rechts die fünf Lösungen von $z^5=1$ auf dem Einheitskreis. Eine Drehung um $2\pi/n$ bildet das $n$-Eck auf sich ab.
:::

**Beispiel.** Für $z^3=8\mathrm{i}$ ist $|a|=8$ und $\alpha=\frac\pi2$, also $|z|=2$ und $\varphi_k=\frac\pi6+\frac{2\pi}3k$:

$$z_0=2\,\mathrm{e}^{\mathrm{i}\pi/6}=\sqrt3+\mathrm{i},\qquad z_1=2\,\mathrm{e}^{5\mathrm{i}\pi/6}=-\sqrt3+\mathrm{i},\qquad z_2=2\,\mathrm{e}^{3\mathrm{i}\pi/2}=-2\mathrm{i}.$$

Probe: $(\sqrt3+\mathrm{i})^2=2+2\sqrt3\,\mathrm{i}$ und $(2+2\sqrt3\,\mathrm{i})(\sqrt3+\mathrm{i})=2\sqrt3+2\mathrm{i}+6\mathrm{i}-2\sqrt3=8\mathrm{i}$. **Grenzfälle:** $n=1$ gibt $z_0=a$. $n=2$ gibt zwei gegenüberliegende Punkte, die Lösungen $\pm w$ aus [Teil 2](/wissen/elektrotechnik/1-semester/hohere-mathematik-1/komplexe-zahlen/komplexe-zahlen.html): Für $D=0{,}75-\mathrm{i}$ ist $\sqrt{|D|}=1{,}118=|1-0{,}5\mathrm{i}|$.

:::frage In $\mathbb{R}$ hat $x^3=8$ nur eine Lösung, warum hier drei?
Die reelle Lösung $2$ bleibt. In $\mathbb{C}$ kommen $2\,\mathrm{e}^{2\pi\mathrm{i}/3}$ und $2\,\mathrm{e}^{4\pi\mathrm{i}/3}$ neben der reellen Achse hinzu. Die Zahlengerade kennt nur die Richtungen $0$ und $\pi$.
:::

:::aufgabe Aufgabe 10 ★★ Wurzeln ziehen
<span class="anker" id="aufg-10"></span>

(a) Löse $z^4=-16$ in Normalform. (b) Löse $z^3=1+\mathrm{i}$ in Polarform und gib $z_0$ in Normalform an. (c) Zeige ohne Rechnung, dass die Summe aller Lösungen von $z^n=a$ für $n\ge2$ null ist. Tipp: Was macht die Drehung um $2\pi/n$ mit der Summe?

:::loesung
(a) $|a|=16$, $\alpha=\pi$: $|z|=2$ und $\varphi_k=\frac\pi4+\frac\pi2k$. Die Lösungen sind $\pm\sqrt2\pm\sqrt2\,\mathrm{i}$ mit allen vier Vorzeichenpaaren. (b) $|a|=\sqrt2$, $\alpha=\frac\pi4$: $|z|=2^{1/6}\approx1{,}1225$ und $\varphi_k=\frac\pi{12}+\frac{2\pi}3k$, also $\frac\pi{12},\ \frac34\pi,\ \frac{17}{12}\pi$. $z_0\approx1{,}0842+0{,}2905\,\mathrm{i}$. (c) Sei $\omega=\mathrm{e}^{2\pi\mathrm{i}/n}\ne1$ und $S$ die Summe. Multiplikation mit $\omega$ führt jede Lösung in die nächste über, die Summe bleibt also dieselbe: $\omega S=S$. Aus $(\omega-1)S=0$ folgt $S=0$.
:::
:::

:::aufgabe Aufgabe 11 ★★★ Die Periode von $\exp$
<span class="anker" id="aufg-11"></span>

(a) Bestimme alle $z\in\mathbb{C}$ mit $\mathrm{e}^z=1+\mathrm{i}$. (b) Bestimme alle $z$ mit $\mathrm{e}^z=-1$. (c) Warum hat $\mathrm{e}^z=0$ keine Lösung, obwohl jede andere komplexe Zahl getroffen wird?

:::loesung
(a) Sei $z=x+\mathrm{i}y$. Aus $\mathrm{e}^x=\sqrt2$ folgt $x=\ln\sqrt2\approx0{,}3466$, die Richtung gibt $y=\frac\pi4+2\pi k$ mit $k\in\mathbb{Z}$. (b) $|\mathrm{e}^z|=1$ gibt $x=0$, und $\mathrm{e}^{\mathrm{i}y}=-1$ gibt $y=\pi+2\pi k$. Also $z=\mathrm{i}\pi(2k+1)$ mit $k\in\mathbb{Z}$. (c) $|\mathrm{e}^z|=\mathrm{e}^{\operatorname{Re} z}>0$ für jedes $z$, also nie 0. Jedes $a=|a|\,\mathrm{e}^{\mathrm{i}\alpha}\ne0$ wird dagegen getroffen, von $z=\ln|a|+\mathrm{i}\alpha$.
:::
:::
