---
title: Stufe 5: Der Streuterm und die Relaxationszeit
pfad: Elektrotechnik / 4. Semester / Elektronische Materialien und Bauelemente 1 / Strom im Halbleiter
order: 4220700
summary: (3.2) kennt keine Stöße, und Stufe 2 hat gezeigt, dass es ohne sie nicht geht.
tags: Fermis Goldene Regel, Relaxationszeit-Näherung, Relaxationszeit
lang: de
---

<span class="anker" id="stufe-5"></span>

:::zweck
[(3.2)](vom-wellenpaket-zur-verteilungsfunktion.html#gl-3-2) kennt keine Stöße, und Stufe [2](ohne-stoe-kein-gleichstrom.html#stufe-2) hat gezeigt, dass es ohne sie nicht geht. Diese Stufe fügt sie ein und ersetzt den schwierigen Stoßterm durch eine einzige Zeit.
:::

**Die Idee.** Ein Stoß versetzt einen Punkt der Wolke sprunghaft von $k$ nach $k'$, am selben Ort (Abb. [5](#abb-5)). Ein Zustand $k$ hat also Zufluss und Abfluss, beide brauchen einen besetzten Start und ein freies Ziel. Im Gleichgewicht ist die Bilanz null, und je größer die Abweichung, desto stärker wird sie abgebaut.

:::satz Satz 5.1 (Boltzmann-Transportgleichung)
<span class="anker" id="satz-5-1"></span>

Mit Stößen gilt $\mathrm{d} f/\mathrm{d} t=\partial f/\partial t|_\text{coll.}$, also

<span class="anker" id="gl-5-1"></span>
$$\frac{\partial f}{\partial t}+v\,\frac{\partial f}{\partial x}+\frac F\hbar\,\frac{\partial f}{\partial k}=\frac{\partial f}{\partial t}\Bigr|_\text{coll.}, \tag{5.1}$$

<span class="anker" id="gl-5-2"></span>
$$\frac{\partial f}{\partial t}\Bigr|_\text{coll.}=\sum_{k'}\Bigl[S(k'\to k)\,f_{k'}(1-f_k)-S(k\to k')\,f_k(1-f_{k'})\Bigr]. \tag{5.2}$$
:::

⁠**So liest man das:** coll. steht für englisch collision, Stoß. $S(k\to k')$ ist die Übergangsrate in 1/s, die Quantenmechanik liefert sie aus dem Störpotential (__Fermis Goldene Regel__). $f_k$ steht kurz für $f(x,k,t)$. Der erste Summand streut hinein: $k'$ muss besetzt sein, Faktor $f_{k'}$, und $k$ frei, Faktor $1-f_k$ (Pauli-Prinzip). Im Halbleiter mit $E_\mathrm F$ in der Lücke ist $1-f\approx1$, im Metall sind die meisten Ziele voll. Der zweite Summand streut heraus.

:::satz Satz 5.2 (Detaillierte Balance)
<span class="anker" id="satz-5-2"></span>

Im Gleichgewicht ist [(5.2)](#gl-5-2) null, und zwar für jedes Paar $k,k'$ einzeln:

<span class="anker" id="gl-5-3"></span>
$$S(k'\to k)\,f_{k'}(1-f_k)-S(k\to k')\,f_k(1-f_{k'})=0. \tag{5.3}$$
:::

⁠**So liest man das:** Jeder Weg läuft im Gleichgewicht gleich oft hin und zurück. Mit $f/(1-f)=\mathrm{e}^{-(E-E_\mathrm F)/(k_\mathrm BT)}$ folgt $S(k'\to k)/S(k\to k')=\exp(-(E_k-E_{k'})/(k_\mathrm BT))$. Bei elastischer Streuung ist das Verhältnis 1. Aufwärts um 63 meV ist es $\mathrm{e}^{-2{,}44}=0{,}087$, denn aufwärts muss ein vorhandenes Phonon geschluckt werden, abwärts kann auch ein neues entstehen.

:::abbildung gemb1/k12streuung 5
Links: Streuung in einen Zustand $k$ hinein und aus ihm heraus. Rechts: Abklingen einer Abweichung für die Zeiten des Rechenmodells. Die Gesamtkurve (blau) liegt unter beiden Einzelkurven.
:::

:::definition Definition 5.3 (Relaxationszeit-Näherung)
<span class="anker" id="satz-5-3"></span>

Die __Relaxationszeit-Näherung__ ersetzt [(5.2)](#gl-5-2) durch $\partial f/\partial t|_\text{coll.}\approx(f^0-f)/\tau$. Damit lautet die Boltzmann-Transportgleichung

<span class="anker" id="gl-5-4"></span>
$$\frac{\partial f}{\partial t}+v\,\frac{\partial f}{\partial x}+\frac F\hbar\,\frac{\partial f}{\partial k}=-\frac{f-f^0}\tau. \tag{5.4}$$
:::

⁠**So liest man das:** Stöße ziehen $f$ zum örtlichen Gleichgewicht $f^0$ mit derselben Dichte, denn sie ändern $k$, nicht die Zahl der Elektronen. [(5.2)](#gl-5-2) verschwindet bei $f=f^0$. Die eigentliche Näherung ist, kleine Abweichungen mit einem einzigen Faktor $1/\tau$ abzubauen. **Gültigkeit:** $|f-f^0|\ll f^0$. Im Allgemeinen hängt $\tau$ von $E$ ab, hier gilt es als fest.

**Lösung ohne Feld.** In homogener Probe ohne Kraft bleibt, weil $f^0$ zeitlich fest ist,

<span class="anker" id="gl-5-5"></span>
$$\frac{\partial f}{\partial t}=\frac{\partial(f-f^0)}{\partial t}=-\frac{f-f^0}\tau\quad\Rightarrow\quad\delta f(t)=\delta f(t=0)\,\mathrm{e}^{-t/\tau},\qquad\delta f=f-f^0. \tag{5.5}$$

Eine Anregung klingt auf der Zeitskala $\tau$ ab, daher der Name __Relaxationszeit__ ([Teil 1](/wissen/elektrotechnik/4-semester/elektronische-materialien-und-bauelemente-1/welle-teilchen-und-schrodinger-gleichung/welle-teilchen-und-schroedinger-gleichung.html)). Mehrere Prozesse liefern je einen Term $-(f-f^0)/\tau_i$. Das ist [(2.2)](ohne-stoe-kein-gleichstrom.html#gl-2-2): $\tau$ in [(5.4)](#gl-5-4) ist $\tau_\text{scat}$.

::::beispiel
In der Probe ist $\tau_\text{scat}=0{,}18$ ps. Eine Abweichung ist nach 0,82 ps auf 1 % gefallen, das sind 4,6 Streuzeiten.
::::

⁠**Grenzfall:** Für $\tau\to\infty$ verschwindet die rechte Seite von [(5.4)](#gl-5-4), und es bleibt [(3.2)](vom-wellenpaket-zur-verteilungsfunktion.html#gl-3-2).

:::aufgabe Aufgabe 5 ★★ Hin, zurück und abklingen
<span class="anker" id="aufg-5"></span>

<ol class="al">

<li>

Leite das Verhältnis $S(k'\to k)/S(k\to k')$ aus [(5.3)](#gl-5-3) her. Berechne es für 40 meV aufwärts bei 300 K und bei 77 K. Warum kühlen sich Elektronen mit viel Überschussenergie durch Phononen ab?

</li>

<li>

Ein Lichtblitz hebt $f$ in einem Zustand um $\delta f(0)=0{,}08$ an, $\tau=0{,}25$ ps. Wie groß ist $\delta f$ nach 0,5 ps? Wie groß, wenn ein zweiter Prozess mit 1 ps hinzukommt?

</li>

</ol>

:::loesung
(a) Aus [(5.3)](#gl-5-3) folgt $S(k'\to k)/S(k\to k')=[f_k/(1-f_k)]/[f_{k'}/(1-f_{k'})]=\exp(-(E_k-E_{k'})/(k_\mathrm BT))$, $E_\mathrm F$ fällt heraus. Für 40 meV: 0,213 bei 300 K, $2{,}4\cdot10^{-3}$ bei 77 K. Abwärts ist viel wahrscheinlicher als aufwärts, also gibt das Elektron im Mittel Energie an das Gitter ab. (b) $0{,}08\,\mathrm{e}^{-2}=0{,}0108$. Mit dem zweiten Prozess ist $1/\tau_\text{scat}=(4+1)\,\mathrm{ps^{-1}}$, $\tau_\text{scat}=0{,}20$ ps und $\delta f=0{,}08\,\mathrm{e}^{-2{,}5}=0{,}0066$.
:::
:::
