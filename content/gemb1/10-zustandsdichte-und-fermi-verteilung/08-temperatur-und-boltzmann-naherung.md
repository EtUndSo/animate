---
title: Stufe 6: Temperatur und Boltzmann-Näherung
pfad: Elektrotechnik / 4. Semester / GEMB1 – Grundlagen elektronischer Materialien und Bauelemente 1 / Zustandsdichte und Fermi-Verteilung
adresse: elektrotechnik/4-semester/elektronische-materialien-und-bauelemente-1/zustandsdichte-und-fermi-verteilung
knoten: Kapitel 10: Zustandsdichte und Fermi-Verteilung
order: 4200800
summary: Die Fermi-Verteilung steht als Formel da.
tags: Aufweichzone, Stufenfunktion, Maxwell-Boltzmann-Verteilung, Boltzmann-Faktor
lang: de
---

<span class="anker" id="stufe-6"></span>

:::zweck
Die Fermi-Verteilung steht als Formel da. Diese Stufe liest ihr Verhalten ab und vereinfacht sie dort, wo die Plätze dünn besetzt sind.
:::

**Die Idee.** Bei $T=0$ bietet das Gitter keine Energie an: Die Elektronen füllen die Plätze lückenlos von unten bis $E_\mathrm F$. Bei $T>0$ stößt das Gitter die Elektronen mit Energien um $k_\mathrm BT$ an. Ein Elektron tief unter $E_\mathrm F$ bleibt, wo es ist, denn in Reichweite ist alles voll. Nur knapp unter $E_\mathrm F$ gibt es darüber freie Plätze. Die Stufe wird weich, aber nur in einem Streifen um $E_\mathrm F$ (Abb. [6](#abb-6)).

:::abbildung gemb1/k10fermi 6
Links $f$ für 0 K, 300 K und 1000 K: Alle Kurven gehen durch $(E_\mathrm F,\frac12)$. Die Tangente der 1000-K-Kurve erreicht 0 und 1 bei $E_\mathrm F\pm2k_\mathrm BT$. Rechts dieselbe Verteilung logarithmisch über $(E-E_\mathrm F)/(k_\mathrm BT)$: Ab etwa 3 fällt sie mit dem Boltzmann-Faktor (rot gestrichelt) zusammen.
:::

:::satz Satz 6.1 (Verhalten der Fermi-Verteilung)
<span class="anker" id="satz-6-1"></span>

<span class="anker" id="gl-6-1"></span>
$$f(E)\approx\begin{cases}1&\text{für }E_\mathrm F-E\gg k_\mathrm BT,\\\frac12&\text{für }E=E_\mathrm F,\\0&\text{für }E-E_\mathrm F\gg k_\mathrm BT,\end{cases}\qquad T\to0:\quad f(E)=\begin{cases}1&E<E_\mathrm F,\\0&E>E_\mathrm F.\end{cases} \tag{6.1}$$

Die Steigung bei $E_\mathrm F$ ist $-1/(4k_\mathrm BT)$. Die Tangente trifft 1 und 0 bei $E_\mathrm F\mp2k_\mathrm BT$. Dieser Streifen der Breite $4k_\mathrm BT$ heißt __Aufweichzone__.
:::

⁠**So liest man das:** Bei $T\to0$ strebt der Exponent für $E>E_\mathrm F$ gegen $+\infty$ und für $E<E_\mathrm F$ gegen $-\infty$, also entsteht die __Stufenfunktion__. Bei 300 K ist die Zone 103 meV breit, bei 1000 K sind es 345 meV. Sie ist symmetrisch: $f(E_\mathrm F+\Delta E)=1-f(E_\mathrm F-\Delta E)$. Ein Platz bei $E_\mathrm F+\Delta E$ ist also so oft besetzt wie einer bei $E_\mathrm F-\Delta E$ leer ist. Elektronen, die über $E_\mathrm F$ auftauchen, fehlen spiegelbildlich unter $E_\mathrm F$. Die Temperatur ändert die Breite, nicht den Punkt $f=\frac12$.

**Boltzmann-Näherung.** Weit oberhalb von $E_\mathrm F$ ist die Exponentialfunktion im Nenner groß gegen 1.

:::satz Satz 6.2 (Boltzmann-Näherung)
<span class="anker" id="satz-6-2"></span>

Für $E-E_\mathrm F\gg k_\mathrm BT$ gilt

<span class="anker" id="gl-6-2"></span>
$$f(E)=\frac1{1+\mathrm{e}^{(E-E_\mathrm F)/(k_\mathrm BT)}}\approx\mathrm{e}^{-(E-E_\mathrm F)/(k_\mathrm BT)}. \tag{6.2}$$
:::

⁠**So liest man das:** Das ist die klassische __Maxwell-Boltzmann-Verteilung__. Sie gilt, weil die Plätze dort so dünn besetzt sind, dass sich zwei Elektronen fast nie um denselben Platz bewerben. Das Pauli-Prinzip spielt keine Rolle mehr. Der __Boltzmann-Faktor__ $\mathrm{e}^{-\Delta E/(k_\mathrm BT)}$ sagt, wie viel seltener ein Platz besetzt ist, der um $\Delta E$ höher liegt. **Warum exponentiell?** Das Gitter muss $\Delta E$ hergeben. Nach [(5.1)](die-fermi-verteilung.html#gl-5-1) sinkt seine Entropie um $\Delta E/T$, nach [(4.2)](anordnungen-zahlen.html#gl-4-2) also sein Gewicht um den Faktor $\mathrm{e}^{-\Delta E/(k_\mathrm BT)}$. Genau so selten ist das Ereignis. **Gültigkeit:** Der relative Fehler ist exakt $\mathrm{e}^{-(E-E_\mathrm F)/(k_\mathrm BT)}$, denn mit $u=(E-E_\mathrm F)/(k_\mathrm BT)$ ist $\mathrm{e}^{-u}\,(1+\mathrm{e}^{u})-1=\mathrm{e}^{-u}$.

::::beispiel
| $(E-E_\mathrm F)/(k_\mathrm BT)$ | 1 | 3 | 4,6 | 8 |
|---|---|---|---|---|
| $f$ | 0,269 | 0,0474 | 0,00995 | 0,00034 |
| Boltzmann | 0,368 | 0,0498 | 0,01005 | 0,00034 |
| relativer Fehler | 37 % | 5,0 % | 1,0 % | 0,03 % |

Die Regel lautet also: Ab $E-E_\mathrm F>3k_\mathrm BT$ liegt der Fehler unter 5 %, ab $4{,}6\,k_\mathrm BT$ unter 1 %. Das sind bei 300 K 78 meV und 119 meV, bei 3 K ein Hundertstel davon. Ein Platz 0,1 eV über $E_\mathrm F$ hat bei 300 K die Besetzung 0,0205, die Näherung gibt 0,0209.
::::

:::frage Muss bei $E_\mathrm F$ ein Zustand liegen?
Nein. $f(E)$ sagt, wie wahrscheinlich ein Platz dieser Energie besetzt wäre, falls es ihn gibt. Ohne Platz ist $D=0$, und das Produkt $D\,f$ ist null. $E_\mathrm F$ darf deshalb auch dort liegen, wo es keine Zustände gibt.
:::

:::aufgabe Aufgabe 8 ★ Kurzfragen zur Verteilung
<span class="anker" id="aufg-8"></span>

<ol class="al">

<li>

Skizziere $f$ für $T_1\to0$ und $T_1<T_2<T_3$ in einem Bild. Was haben alle Kurven gemeinsam?

</li>

<li>

Wie groß muss $(E-E_\mathrm F)/(k_\mathrm BT)$ sein, damit der Fehler von [(6.2)](#gl-6-2) höchstens 2 % beträgt? Was heißt das bei 77 K und bei 400 K in meV?

</li>

<li>

Bei welcher Temperatur ist ein Platz 0,1 eV über $E_\mathrm F$ zu 1 % besetzt?

</li>

</ol>

:::loesung
(a) Eine Stufe und zwei weiche Kurven, alle durch $f(E_\mathrm F)=\frac12$, mit wachsender Breite. (b) $\mathrm{e}^{-u}\le0{,}02$ verlangt $u\ge\ln50=3{,}91$: 26,0 meV bei 77 K, 135 meV bei 400 K. (c) $f=0{,}01$ heißt $\mathrm{e}^u=99$, also $u=4{,}60$ und $T=0{,}1\,\mathrm{eV}/(k_\mathrm B\ln99)=253$ K.
:::
:::
