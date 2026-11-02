---
title: Stufe 6: Die Eulersche Formel
pfad: Elektrotechnik / 1. Semester / Höhere Mathematik 1 / Potenzreihen und Eulersche Formel
order: 1270800
summary: e ix liegt auf dem Einheitskreis, Sinus und Cosinus sind Reihen.
tags: 
lang: de
---

<span class="anker" id="stufe-6"></span>

:::zweck
$\mathrm{e}^{\mathrm{i}x}$ liegt auf dem Einheitskreis, Sinus und Cosinus sind Reihen. Diese Stufe zeigt, dass beides dasselbe ist, und gewinnt daraus die Additionstheoreme.
:::

**Die Idee.** Die Potenzen von $\mathrm{i}$ wiederholen sich: $1,\mathrm{i},-1,-\mathrm{i},1,\dots$ Setzt man $\mathrm{i}x$ in die Exponentialreihe ein, wird jedes Glied gegenüber dem vorigen um $90^\circ$ gedreht (Abb. [6](#abb-6), rechts). Die geraden Glieder sind reell mit wechselndem Vorzeichen, das ist die Cosinusreihe. Die ungeraden sind imaginär, auch mit wechselndem Vorzeichen, das ist die Sinusreihe.

:::abbildung hm1/k7euler 6
Links der Einheitskreis für $\varphi=1$: Cosinus und Sinus sind die Koordinaten. Rechts die Reihe für $\varphi=2$ als Weg: Jeder Pfeil ist ein Glied $(2\mathrm{i})^n/n!$, gedreht um $90^\circ$ gegen den vorigen. Blau bildet den Cosinus, grün den Sinus, das Ziel ist $\mathrm{e}^{2\mathrm{i}}=-0{,}416+0{,}909\,\mathrm{i}$.
:::

:::satz Satz 6.1 (Eulersche Formel)
<span class="anker" id="satz-6-1"></span>

Für alle $x\in\mathbb{R}$ gilt

<span class="anker" id="gl-6-1"></span>
$$\mathrm{e}^{\mathrm{i}x}=\exp(\mathrm{i}x)=\cos x+\mathrm{i}\sin x. \tag{6.1}$$

Also ist $\operatorname{Re}(\mathrm{e}^{\mathrm{i}x})=\cos x$ und $\operatorname{Im}(\mathrm{e}^{\mathrm{i}x})=\sin x$. Daraus folgt für alle $x\in\mathbb{R}$:

<span class="anker" id="gl-6-2"></span>
$$(\sin x)^2+(\cos x)^2=1,\qquad\sin x\in[-1,1],\qquad\cos x\in[-1,1]. \tag{6.2}$$
:::

⁠**So liest man das:** [(6.2)](#gl-6-2) ist der Satz des Pythagoras auf dem Einheitskreis, hier aus Reihen bewiesen. **Gültigkeit:** $x$ muss reell sein, sonst sind $\cos x$ und $\sin x$ nicht Real- und Imaginärteil.

:::beweis Gerade und ungerade Glieder trennen
Es ist $(\mathrm{i}x)^{2k}=(-1)^kx^{2k}$ und $(\mathrm{i}x)^{2k+1}=\mathrm{i}(-1)^kx^{2k+1}$. Die Reihe ist absolut konvergent, also darf man sie nach geraden und ungeraden $n$ sortieren:

$$\mathrm{e}^{\mathrm{i}x}=\sum_{n=0}^\infty\frac{(\mathrm{i}x)^n}{n!}=\sum_{k=0}^\infty\frac{(-1)^k}{(2k)!}x^{2k}+\mathrm{i}\sum_{k=0}^\infty\frac{(-1)^k}{(2k+1)!}x^{2k+1}=\cos x+\mathrm{i}\sin x.$$

Beide Teilreihen sind reell, das sind Real- und Imaginärteil. Aus $|\mathrm{e}^{\mathrm{i}x}|=1$ (Satz [5.3](die-exponentialreihe-reell-und-komplex.html#satz-5-3)) folgt $(\cos x)^2+(\sin x)^2=|\mathrm{e}^{\mathrm{i}x}|^2=1$. Jede der beiden Zahlen ist also höchstens 1 im Betrag.
:::

:::satz Satz 6.2 (Additionstheoreme)
<span class="anker" id="satz-6-2"></span>

Für alle $x,y\in\mathbb{R}$ gilt:

<ol class="rm">

<li>

$\sin(x+y)=\sin x\cos y+\cos x\sin y$,

</li>

<li>

$\cos(x+y)=\cos x\cos y-\sin x\sin y$.

</li>

</ol>
:::

⁠**So liest man das:** Niemand muss diese Formeln auswendig können. Sie sind Real- und Imaginärteil von $\mathrm{e}^{\mathrm{i}(x+y)}=\mathrm{e}^{\mathrm{i}x}\mathrm{e}^{\mathrm{i}y}$. Das Minus in (ii) ist das $\mathrm{i}^2$.

:::beweis Funktionalgleichung zerlegen
Nach [(6.1)](#gl-6-1) und der Funktionalgleichung ist

$$\cos(x+y)+\mathrm{i}\sin(x+y)=\mathrm{e}^{\mathrm{i}x}\mathrm{e}^{\mathrm{i}y}=(\cos x+\mathrm{i}\sin x)(\cos y+\mathrm{i}\sin y).$$

Ausmultiplizieren ergibt rechts $(\cos x\cos y-\sin x\sin y)+\mathrm{i}(\sin x\cos y+\cos x\sin y)$. Die Realteile liefern (ii), die Imaginärteile (i).
:::

**Beispiel.** Mit $x=1$ und $y=0{,}5$: $\sin1\cos0{,}5+\cos1\sin0{,}5=0{,}7385+0{,}2590=0{,}9975=\sin1{,}5$. **Grenzfälle:** $y=-x$ gibt $1=\cos^2x+\sin^2x$, also [(6.2)](#gl-6-2). $y=x$ gibt $\sin2x=2\sin x\cos x$ und $\cos2x=\cos^2x-\sin^2x$, bei $x=1$ sind das $0{,}9093$ und $-0{,}4161$.

:::frage Ist die Eulersche Formel eine Definition oder ein Satz?
Ein Satz. Links steht die Exponentialreihe, rechts stehen zwei andere Reihen. Dass sie zusammenpassen, ist bewiesen. Festgelegt ist nur die Schreibweise $\mathrm{e}^z$.
:::

:::aufgabe Aufgabe 6 ★★ Mit Euler rechnen
<span class="anker" id="aufg-6"></span>

(a) Zeige $\cos x=\frac12(\mathrm{e}^{\mathrm{i}x}+\mathrm{e}^{-\mathrm{i}x})$ und $\sin x=\frac1{2\mathrm{i}}(\mathrm{e}^{\mathrm{i}x}-\mathrm{e}^{-\mathrm{i}x})$. (b) Folgere daraus $\cos^2x=\frac12(1+\cos2x)$ und prüfe bei $x=1$. (c) Zeige $\sin3x=3\sin x-4\sin^3x$ und prüfe bei $x=0{,}1$.

:::loesung
(a) $\mathrm{e}^{-\mathrm{i}x}=\cos x-\mathrm{i}\sin x$, weil $\cos$ gerade und $\sin$ ungerade ist. Addieren gibt $2\cos x$, Subtrahieren $2\mathrm{i}\sin x$. (b) $\cos^2x=\frac14(\mathrm{e}^{2\mathrm{i}x}+2+\mathrm{e}^{-2\mathrm{i}x})=\frac14(2\cos2x+2)=\frac12(1+\cos2x)$. Probe: Beide Seiten sind $0{,}29193$. (c) $\sin3x=\sin2x\cos x+\cos2x\sin x=2\sin x\cos^2x+(1-2\sin^2x)\sin x=2\sin x(1-\sin^2x)+\sin x-2\sin^3x=3\sin x-4\sin^3x$. Probe: Beide Seiten sind $0{,}29552$.
:::
:::
