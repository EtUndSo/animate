---
title: Stufe 11: Fehlerwahrscheinlichkeit beim Binärempfang
pfad: Elektrotechnik / 3. Semester / Signale und Systeme / Zufallssignale
order: 3271200
summary: Der Empfänger soll entscheiden: Wurde der Impuls gesendet oder nicht?
tags: 
lang: de
---

<span class="anker" id="stufe-11"></span>

:::zweck
Der Empfänger soll entscheiden: Wurde der Impuls gesendet oder nicht? Wie oft irrt er sich?
:::

**Die Idee.** Der Abtastwert am Ausgang des Korrelationsfilters ist gaußverteilt mit der Varianz $N$ (Rauschen) und dem Mittelwert $\sqrt{S_a}$, wenn gesendet wurde, oder 0, wenn nicht. Der Empfänger vergleicht mit einer Schwelle $C$. Ein Fehler passiert, wenn das Rauschen den Wert über die Schwelle schiebt. Die beiden Fehlerwahrscheinlichkeiten sind die Flächen der beiden Gaußkurven jenseits der Schwelle:

<span class="anker" id="gl-11-1"></span>
$$P_{e1}=\mathrm{Prob}[y_1\le C]=\tfrac12\operatorname{erfc}\Bigl(\frac{\sqrt{S_a}-C}{\sqrt{2N}}\Bigr),\qquad P_{e0}=\mathrm{Prob}[y_0>C]=\tfrac12\operatorname{erfc}\Bigl(\frac{C}{\sqrt{2N}}\Bigr). \tag{11.1}$$

Werden beide Fälle gleich oft gesendet, ist die mittlere Fehlerwahrscheinlichkeit $\frac12(P_{e1}+P_{e0})$. Sie wird am kleinsten, wenn die Schwelle genau in der Mitte liegt, $C=\sqrt{S_a}/2$. Mit dem Korrelationsfilter ($S_a/N=E_s/N_0$):

<span class="anker" id="gl-11-2"></span>
$$P_{e,\min}=\tfrac12\operatorname{erfc}\sqrt{\frac{E_s}{8N_0}}. \tag{11.2}$$

⁠**So liest man das:** Die Fehlerwahrscheinlichkeit hängt nur von $E_s/N_0$ ab und fällt extrem schnell: bei 10 dB $5{,}7\cdot10^{-2}$, bei 16 dB $8\cdot10^{-4}$, bei 20 dB $2{,}9\cdot10^{-7}$ (Abb. [4](#abb-4)). Wenige Dezibel mehr Signalenergie machen aus einer unbrauchbaren eine fast fehlerfreie Übertragung.

:::abbildung et3/k7pe 4
Minimale Fehlerwahrscheinlichkeit beim Ein-Aus-Empfang mit Korrelationsfilter. Rote Punkte: 10 dB, 16 dB, 20 dB.
:::

:::aufgabe Aufgabe 11 ★★ Fehlerwahrscheinlichkeit
<span class="anker" id="aufg-11"></span>

<ol class="al">

<li>

Berechne $P_{e,\min}$ für $E_s/N_0=10$ dB. Tipp: $\operatorname{erfc}(1{,}118)=0{,}114$.

</li>

<li>

Warum liegt die optimale Schwelle in der Mitte zwischen 0 und $\sqrt{S_a}$? Was passiert mit $P_{e1}$ und $P_{e0}$, wenn man sie nach oben verschiebt?

</li>

</ol>

:::loesung
(a) $E_s/N_0=10$: $\sqrt{10/8}=1{,}118$, $P_{e,\min}=\frac12\cdot0{,}114=0{,}057$.

(b) Die beiden Gaußkurven haben dieselbe Breite. Die Summe der beiden Fehlerflächen ist am kleinsten, wo sich die Kurven schneiden, und das ist aus Symmetriegründen die Mitte. Schiebt man die Schwelle nach oben, wird $P_{e0}$ kleiner, aber $P_{e1}$ wächst stärker, weil die Schwelle in den dichten Teil der oberen Kurve rückt.
:::
:::
