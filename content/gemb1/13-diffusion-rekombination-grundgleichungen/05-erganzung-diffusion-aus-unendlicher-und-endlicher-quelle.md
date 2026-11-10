---
title: Stufe 3: Ergänzung: Diffusion aus unendlicher und endlicher Quelle
pfad: Elektrotechnik / 4. Semester / GEMB1 – Grundlagen elektronischer Materialien und Bauelemente 1 / Diffusion, Rekombination und Grundgleichungen
adresse: elektrotechnik/4-semester/elektronische-materialien-und-bauelemente-1/diffusion-rekombination-und-grundgleichungen
knoten: Kapitel 13: Diffusion, Rekombination und Grundgleichungen
order: 4230500
summary: Die Gleichung steht.
tags: Gauß-Funktion, Gaußsche Fehlerintegral, Fehlerfunktion, Eindringtiefe
lang: de
---

<span class="anker" id="stufe-3"></span>

:::zweck
Die Gleichung steht. Diese Stufe löst sie für die zwei Fälle beim Dotieren: Der Vorrat an der Oberfläche ist unbegrenzt, oder er ist begrenzt.
:::

**Die Idee.** Ab $t=0$ dringen Fremdatome durch die Stirnfläche $A$ bei $x=0$ in einen Stab aus reinem Silizium ein. Die Gleichung ist in beiden Fällen [(2.2)](die-kontinuitatsgleichung.html#gl-2-2), nur der Rand unterscheidet sich. **Unendliche Quelle:** Ein Gas, etwa Monophosphan PH$_3$ für Phosphor, hält die Dichte an der Oberfläche fest. Die Menge im Stab wächst. **Endliche Quelle:** Eine dünne Schicht, etwa Aluminium, enthält einen festen Vorrat. Die Menge bleibt, und die Dichte an der Oberfläche sinkt.

:::abbildung gemb1/k13quellen 3
Links: unendliche Quelle, die Oberfläche bleibt auf $N_0$. Rechts: endliche Quelle, die Fläche unter jeder Kurve bleibt gleich. Die Kurven gehören zu drei Eindringtiefen $x_0=2\sqrt{Dt}$.
:::

:::satz Satz 3.1 (Unendliche Quelle)
<span class="anker" id="satz-3-1"></span>

Mit der Anfangsbedingung $N(x,0)=0$ für $x>0$ und den Randbedingungen $N(0,t)=N_0$ und $N\to0$ für $x\to\infty$ gilt

<span class="anker" id="gl-3-1"></span>
$$N(x,t)=N_0\Bigl[1-\frac2{\sqrt\pi}\int_{u=0}^{a}\exp(-u^2)\,\mathrm{d} u\Bigr]=N_0\bigl[1-\operatorname{erf}(a)\bigr],\qquad a=\frac x{2\sqrt{Dt}}. \tag{3.1}$$
:::

⁠**So liest man das:** Integriert wird die __Gauß-Funktion__ $y=c_1\exp[-c_2(x-x_\mathrm m)^2]$ mit $c_1=c_2=1$, $x_\mathrm m=0$. Dieses __Gaußsche Fehlerintegral__ hat keine geschlossene Lösung, die __Fehlerfunktion__ $\operatorname{erf}$ steht in Tabellen:

| $a$ | 0,25 | 0,5 | 0,75 | 1 | 1,25 | 1,5 | 2 | 2,5 |
|---|---|---|---|---|---|---|---|---|
| $1-\operatorname{erf}(a)$ | 0,724 | 0,480 | 0,289 | 0,157 | 0,077 | 0,034 | 0,0047 | 0,0004 |

Die __Eindringtiefe__ $x_0$ ist der Wert von $x$ für $a=1$: $x_0=2\sqrt{Dt}$ und $N(x_0,t)/N_0=1-\operatorname{erf}(1)=0{,}157$. Die Menge im Stab je Fläche ist $\int_0^\infty N\,\mathrm{d} x=2N_0\sqrt{Dt/\pi}$.

:::satz Satz 3.2 (Endliche Quelle)
<span class="anker" id="satz-3-2"></span>

Eine Schicht der Dicke $d$ enthalte $\mathcal N$ Atome, ihre Startdichte ist $N_0=\mathcal N/(A\,d)$. Mit $N(x,0)=0$ für $x>0$, ohne Abfluss über die Oberfläche ($\mathcal J(0,t)=0$) und mit fester Menge $\int_0^\infty N\,\mathrm{d} x=N_0d$ gilt

<span class="anker" id="gl-3-2"></span>
$$N(x,t)=\frac{N_0\,d}{\sqrt{\pi Dt}}\,\exp\Bigl(-\frac{x^2}{4Dt}\Bigr). \tag{3.2}$$
:::

⁠**So liest man das:** Das Profil ist eine halbe Gauß-Kurve, ihre Höhe sinkt mit $t^{-1/2}$. Die Eindringtiefe ist der Wert von $x$ mit dem Exponenten $-1$: wieder $x_0=2\sqrt{Dt}$, und $N(x_0,t)/N(0,t)=\mathrm{e}^{-1}=0{,}368$. **Gültigkeit:** $x_0\gg d$. Für $t\to0$ wächst [(3.2)](#gl-3-2) ohne Grenze, weil die Formel die Schicht als unendlich dünn behandelt.

:::herleitung Warum nur $x/\sqrt{Dt}$ zählt
Rand und Anfang der unendlichen Quelle enthalten keine Länge. Also kann $N$ nur von $a=x/(2\sqrt{Dt})$ abhängen: $N=g(a)$. Mit $\partial a/\partial t=-a/(2t)$ und $\partial a/\partial x=1/(2\sqrt{Dt})$ wird [(2.2)](die-kontinuitatsgleichung.html#gl-2-2) zu

$$-\frac a{2t}\,g'=\frac1{4t}\,g''\quad\Rightarrow\quad g''=-2a\,g'\quad\Rightarrow\quad g'=c\,\mathrm{e}^{-a^2}.$$

Integrieren mit $g(0)=N_0$, $g(\infty)=0$ ergibt [(3.1)](#gl-3-1). Die Ableitung einer Lösung nach $x$ ist wieder eine Lösung: So entsteht die Gauß-Kurve, und die Menge legt den Vorfaktor fest, denn $\int_0^\infty\mathrm{e}^{-x^2/(4Dt)}\mathrm{d} x=\sqrt{\pi Dt}$.
:::

::::beispiel
Bor bei 1100 °C aus unendlicher Quelle mit $N_0=10^{20}\,\mathrm{cm^{-3}}$: Nach 1 h ist $x_0=0{,}73$ µ m, bei 0,5 µ m liegen $3{,}3\cdot10^{19}\,\mathrm{cm^{-3}}$, die Dichte $10^{16}\,\mathrm{cm^{-3}}$ wird bei 2,0 µ m erreicht, und im Stab stecken $4{,}1\cdot10^{15}\,\mathrm{cm^{-2}}$.
::::

⁠**Grenzfälle:** Bei $x=0$ ist $N=N_0$, für $t\to\infty$ strebt $N$ an jedem festen Ort gegen $N_0$. Die Formeln hängen nur von $Dt$ ab: Bei höherer Temperatur gibt die Zeit $t_2=t_1D_1/D_2$ dasselbe Profil.

:::frage Warum wächst die Eindringtiefe mit $\sqrt t$ und nicht mit $t$?
Weil der Antrieb nachlässt. Je tiefer die Atome stehen, desto flacher ist das Profil und desto kleiner der Strom. Viermal so lange heißt nur doppelt so tief.
:::

:::aufgabe Aufgabe 3 ★★ Unendliche Quelle
<span class="anker" id="aufg-3"></span>

In reines Silizium diffundiert Arsen aus einer Quelle mit $N_0=5\cdot10^{19}\,\mathrm{cm^{-3}}$ für 2 h bei $D=10^{-13}\,\mathrm{cm^2/s}$.

<ol class="al">

<li>

Stelle die Differentialgleichung aus Fick-Gesetz und Kontinuitätsgleichung auf und nenne alle Anfangs- und Randbedingungen.

</li>

<li>

Wie groß ist $x_0$? In welcher Tiefe ist $N=1{,}7\cdot10^{18}\,\mathrm{cm^{-3}}$ (Tabelle)?

</li>

<li>

Wie viel Arsen steckt je cm$^2$ im Stab? Wie lange dauert dasselbe Profil bei $4D$?

</li>

</ol>

:::loesung
(a) Einsetzen gibt $\partial N/\partial t=D\,\partial^2N/\partial x^2$ mit $N(x,0)=0$ für $x>0$, $N(0,t)=N_0$, $N\to0$ für $x\to\infty$. (b) $x_0=2\sqrt{10^{-13}\,\mathrm{cm^2/s}\cdot7200\,\mathrm{s}}=0{,}54$ µ m. $N/N_0=0{,}034$ gehört zu $a=1{,}5$, also $x=1{,}5\,x_0=0{,}81$ µ m. (c) $2N_0\sqrt{Dt/\pi}=1{,}5\cdot10^{15}\,\mathrm{cm^{-2}}$. Nur $Dt$ zählt: 0,5 h.
:::
:::

:::aufgabe Aufgabe 4 ★★★ Endliche Quelle
<span class="anker" id="aufg-4"></span>

Auf einem Siliziumstab liegt eine Borschicht mit $N_0d=5\cdot10^{15}\,\mathrm{cm^{-2}}$. Der Stab bleibt 10 h bei 1100 °C.

<ol class="al">

<li>

Zeige durch Einsetzen, dass [(3.2)](#gl-3-2) die Gleichung [(2.2)](die-kontinuitatsgleichung.html#gl-2-2) erfüllt.

</li>

<li>

Wie groß sind $N(0,t)$ und $N$ bei $x=2$ µ m? In welcher Tiefe ist $N=10^{16}\,\mathrm{cm^{-3}}$?

</li>

<li>

Zeige $\mathcal J=N\,x/(2t)$ und berechne $\mathcal J$ an dieser Stelle.

</li>

<li>

Skizziere $N(t)$ an der festen Stelle $x=2$ µ m. Wann ist $N$ dort am größten?

</li>

<li>

Der Ofen läuft bei 1200 °C. Wie lange dauert dasselbe Profil?

</li>

</ol>

:::loesung
(a) Mit $N=c\,t^{-1/2}\mathrm{e}^{-x^2/(4Dt)}$ sind $\partial N/\partial t$ und $D\,\partial^2N/\partial x^2$ beide gleich $N\bigl(-\frac1{2t}+\frac{x^2}{4Dt^2}\bigr)$. (b) $Dt=1{,}32\cdot10^{-8}\,\mathrm{cm^2}$, $N(0,t)=2{,}45\cdot10^{19}\,\mathrm{cm^{-3}}$, $N(2\,\mu\text{m})=1{,}15\cdot10^{19}\,\mathrm{cm^{-3}}$. Aus $x^2=4Dt\ln(N(0,t)/N)$ folgt $x=6{,}4$ µ m. (c) $\partial N/\partial x=-N\,x/(2Dt)$ gibt $\mathcal J=N\,x/(2t)=8{,}9\cdot10^{7}\,\mathrm{cm^{-2}\,s^{-1}}$. (d) Für $t\to0$ und $t\to\infty$ geht $N\to0$, dazwischen liegt ein Maximum. $\partial N/\partial t=0$ gibt $t_\text{max}=x^2/(2D)=15$ h mit $N=1{,}2\cdot10^{19}\,\mathrm{cm^{-3}}$. (e) Bei 1200 °C ist $D$ 7,9-mal größer, also 76 min.
:::
:::
