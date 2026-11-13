---
title: Stufe 11: Fehlerwahrscheinlichkeit beim Binärempfang
pfad: Elektrotechnik / 3. Semester / ET3 – Grundgebiete der Elektrotechnik 3: Signale und Systeme / Zufallssignale
adresse: elektrotechnik/3-semester/signale-und-systeme/zufallssignale
knoten: Kapitel 7: Zufallssignale
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

::::formelsammlung
**Fehlerwahrscheinlichkeiten**

$$P_{e1}=\mathrm{Prob}[y_1\le C]=\tfrac12\operatorname{erfc}\Bigl(\frac{\sqrt{S_a}-C}{\sqrt{2N}}\Bigr),\qquad P_{e0}=\mathrm{Prob}[y_0>C]=\tfrac12\operatorname{erfc}\Bigl(\frac{C}{\sqrt{2N}}\Bigr)$$

Abtastwert gaußverteilt mit der Varianz $N$ und dem Mittelwert $\sqrt{S_a}$ (gesendet) bzw. 0 (nicht gesendet), Schwelle $C$.

**Mittlere Fehlerwahrscheinlichkeit, beste Schwelle**

$$\frac12(P_{e1}+P_{e0}),\qquad C=\sqrt{S_a}/2$$

Beide Fälle gleich oft gesendet; am kleinsten mit der Schwelle genau in der Mitte.

**Minimale Fehlerwahrscheinlichkeit**

$$P_{e,\min}=\tfrac12\operatorname{erfc}\sqrt{\frac{E_s}{8N_0}}$$

Mit Korrelationsfilter ($S_a/N=E_s/N_0$). Hängt nur von $E_s/N_0$ ab und fällt extrem schnell.
::::

::::lernkarten
:::karte zusammenhang Abtastwert am Filterausgang
Wie ist der Abtastwert am Ausgang des Korrelationsfilters beim Ein-Aus-Empfang verteilt, je nachdem, ob der Impuls gesendet wurde?
---
Gaußverteilt mit der Varianz $N$ des Rauschens und dem Mittelwert $\sqrt{S_a}$, wenn der Impuls gesendet wurde, oder mit dem Mittelwert 0, wenn nicht.
--- falsch
Gleichverteilt zwischen 0 und $\sqrt{S_a}$, wenn der Impuls gesendet wurde, und exakt 0, wenn nicht, weil ohne Impuls kein Rauschen durch das Filter gelangt.
--- falsch
Gaußverteilt mit dem Mittelwert $\sqrt{S_a}$ in beiden Fällen, weil das Rauschen den Mittelwert verschiebt; nur die Varianz ist ohne Impuls kleiner.
--- falsch
Gaußverteilt mit dem Mittelwert $S_a$ und der Varianz $N^2$, wenn der Impuls gesendet wurde, oder mit dem Mittelwert $N$, wenn nicht.
:::
:::karte formel Fehlerwahrscheinlichkeiten
Wie groß sind beim Ein-Aus-Empfang die beiden Fehlerwahrscheinlichkeiten $P_{e1}$ und $P_{e0}$ bei der Entscheidungsschwelle $C$?
---
$P_{e1}=\mathrm{Prob}[y_1\le C]=\tfrac12\operatorname{erfc}\Bigl(\frac{\sqrt{S_a}-C}{\sqrt{2N}}\Bigr)$ und $P_{e0}=\mathrm{Prob}[y_0>C]=\tfrac12\operatorname{erfc}\Bigl(\frac{C}{\sqrt{2N}}\Bigr)$: die Flächen der beiden Gaußkurven jenseits der Schwelle.
--- falsch
$P_{e1}=\mathrm{Prob}[y_1>C]=\tfrac12\operatorname{erfc}\Bigl(\frac{C}{\sqrt{2N}}\Bigr)$ und $P_{e0}=\mathrm{Prob}[y_0\le C]=\tfrac12\operatorname{erfc}\Bigl(\frac{\sqrt{S_a}-C}{\sqrt{2N}}\Bigr)$: die Flächen der beiden Gaußkurven diesseits der Schwelle.
--- falsch
$P_{e1}=\tfrac12\operatorname{erfc}\Bigl(\frac{\sqrt{S_a}-C}{N}\Bigr)$ und $P_{e0}=\tfrac12\operatorname{erfc}\Bigl(\frac{C}{N}\Bigr)$: Man teilt den Abstand zur Schwelle durch die Varianz $N$ des Rauschens, nicht durch ihre Wurzel.
--- falsch
$P_{e1}=P_{e0}=\tfrac12\operatorname{erfc}\Bigl(\frac{\sqrt{S_a}}{\sqrt{2N}}\Bigr)$ für jede Schwelle $C$: Die Schwelle verschiebt nur, welcher der beiden Fehler auftritt, nicht wie oft.
:::
:::karte formel Mittlere Fehlerwahrscheinlichkeit und beste Schwelle
Wie groß ist die mittlere Fehlerwahrscheinlichkeit, wenn beide Fälle gleich oft gesendet werden, und wo liegt die beste Schwelle?
---
$\frac12(P_{e1}+P_{e0})$; sie wird am kleinsten, wenn die Schwelle genau in der Mitte zwischen den beiden Mittelwerten liegt, also bei $C=\sqrt{S_a}/2$.
--- falsch
$P_{e1}+P_{e0}$; sie wird am kleinsten, wenn die Schwelle bei $C=\sqrt{S_a}$ liegt, also genau beim Mittelwert für einen gesendeten Impuls.
--- falsch
$P_{e1}\,P_{e0}$; sie wird am kleinsten, wenn die Schwelle bei $C=0$ liegt, weil dann jeder positive Abtastwert als Impuls erkannt wird.
--- falsch
$\frac12(P_{e1}+P_{e0})$; sie wird am kleinsten, wenn die Schwelle bei $C=\sqrt{N}$ liegt, also eine Standardabweichung über dem Mittelwert ohne Impuls.
:::
:::karte formel Minimale Fehlerwahrscheinlichkeit
Wie groß ist die kleinste Fehlerwahrscheinlichkeit beim Ein-Aus-Empfang mit Korrelationsfilter und optimaler Schwelle?
---
$P_{e,\min}=\tfrac12\operatorname{erfc}\sqrt{\frac{E_s}{8N_0}}$, weil mit dem Korrelationsfilter $S_a/N=E_s/N_0$ ist. Sie hängt also nur von $E_s/N_0$ ab.
--- falsch
$P_{e,\min}=\tfrac12\operatorname{erfc}\sqrt{\frac{E_s}{N_0}}$, weil mit dem Korrelationsfilter der Abstand der Mittelwerte gleich $E_s/N_0$ ist. Sie hängt also nur von $E_s/N_0$ ab.
--- falsch
$P_{e,\min}=\tfrac12\operatorname{erfc}\sqrt{\frac{8E_s}{N_0}}$, weil der Abstand zur Schwelle achtfach in die Rechnung eingeht. Sie hängt außerdem von der Form des Signals ab.
--- falsch
$P_{e,\min}=\frac{N_0}{8E_s}$, weil die Fehlerwahrscheinlichkeit umgekehrt proportional zum Signal-Rausch-Verhältnis ist. Doppelte Energie halbiert also die Fehler.
:::
:::karte zusammenhang Schnell fallende Fehlerwahrscheinlichkeit
Warum machen wenige Dezibel mehr Signalenergie aus einer unbrauchbaren eine fast fehlerfreie Übertragung?
---
Weil $P_{e,\min}$ die Fläche unter dem Ausläufer einer Gaußkurve ist und deshalb extrem schnell fällt: bei 10 dB $5{,}7\cdot10^{-2}$, bei 16 dB $8\cdot10^{-4}$, bei 20 dB $2{,}9\cdot10^{-7}$.
--- falsch
Weil $P_{e,\min}$ proportional zu $N_0/E_s$ ist: Jedes zusätzliche Dezibel halbiert die Fehlerwahrscheinlichkeit, sodass 10 dB mehr sie ungefähr auf ein Tausendstel senken.
--- falsch
Weil ab etwa 16 dB das Rauschen vollständig unterdrückt wird: Darüber ist die Fehlerwahrscheinlichkeit exakt null, darunter liegt sie bei etwa 50 %.
--- falsch
Weil Dezibel eine logarithmische Einheit sind: Die Fehlerwahrscheinlichkeit fällt linear mit der Zahl der Dezibel, und wenige Dezibel entsprechen schon einer großen Energieänderung.
:::
:::karte zusammenhang Schwelle in der Mitte
Warum liegt die optimale Entscheidungsschwelle genau in der Mitte zwischen 0 und $\sqrt{S_a}$?
---
Weil beide Gaußkurven dieselbe Breite haben. Die Summe der beiden Fehlerflächen ist dort am kleinsten, wo sich die Kurven schneiden, und das ist aus Symmetriegründen die Mitte.
--- falsch
Weil der Empfänger beide Fehler gleich schwer bewertet; hätte die Kurve für einen gesendeten Impuls eine größere Breite, läge die beste Schwelle trotzdem genau in der Mitte.
--- falsch
Weil in der Mitte beide Gaußkurven ihr Maximum haben; dort ist die Dichte der Abtastwerte am größten, und die Entscheidung ist deshalb am sichersten.
--- falsch
Weil die Schwelle stets bei der halben Signalleistung liegen muss; $\sqrt{S_a}/2$ ist gerade die Hälfte der Leistung des Abtastwerts, gleichgültig, wie stark das Rauschen ist.
:::
:::karte zusammenhang Schwelle nach oben verschoben
Was passiert mit $P_{e1}$ und $P_{e0}$, wenn man die Entscheidungsschwelle aus der Mitte nach oben verschiebt?
---
$P_{e0}$ wird kleiner, aber $P_{e1}$ wächst stärker, weil die Schwelle in den dichten Teil der oberen Gaußkurve rückt. Die mittlere Fehlerwahrscheinlichkeit steigt deshalb.
--- falsch
$P_{e0}$ und $P_{e1}$ werden beide kleiner, weil eine höhere Schwelle das Rauschen besser abschneidet. Die mittlere Fehlerwahrscheinlichkeit sinkt deshalb deutlich.
--- falsch
$P_{e1}$ wird kleiner, aber $P_{e0}$ wächst stärker, weil weniger Werte ohne Impuls unter der Schwelle bleiben. Die mittlere Fehlerwahrscheinlichkeit steigt deshalb.
--- falsch
$P_{e0}$ wird um genau so viel kleiner, wie $P_{e1}$ wächst, weil die Gesamtfläche beider Kurven erhalten bleibt. Die mittlere Fehlerwahrscheinlichkeit bleibt deshalb gleich.
:::
::::
