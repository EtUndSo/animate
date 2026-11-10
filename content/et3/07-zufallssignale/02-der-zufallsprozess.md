---
title: Stufe 1: Der Zufallsprozess
pfad: Elektrotechnik / 3. Semester / ET3 – Grundgebiete der Elektrotechnik 3: Signale und Systeme / Zufallssignale
adresse: elektrotechnik/3-semester/signale-und-systeme/zufallssignale
knoten: Kapitel 7: Zufallssignale
order: 3270200
summary: Wie beschreibt man ein Signal, dessen Verlauf man nicht kennt?
tags: Musterfunktion, Zufallsprozess, Zufallsgröße, Erwartungswert, Autokorrelationsfunktion
lang: de
---

<span class="anker" id="stufe-1"></span>

:::zweck
Wie beschreibt man ein Signal, dessen Verlauf man nicht kennt? Man stellt sich viele gleichartige Signale vor und mittelt über sie.
:::

**Die Idee.** Misst man das Rauschen an vielen gleich gebauten Widerständen bei gleicher Temperatur, bekommt man viele verschiedene Kurven ${}^ks(t)$, $k=1,2,\dots$ (Abb. [1](#abb-1)). Jede einzelne heißt __Musterfunktion__ oder Realisierung. Die gedachte Gesamtheit aller heißt __Zufallsprozess__ $s(t)$. Die Werte aller Musterfunktionen zu einem festen Zeitpunkt $t_1$ bilden eine __Zufallsgröße__ $s(t_1)$.

:::definition Definition 1.1 (Scharmittelwerte)
<span class="anker" id="satz-1-1"></span>

<span class="anker" id="gl-1-1"></span>
<span class="anker" id="gl-1-2"></span>
$$\begin{aligned} \mathrm E\{s(t_1)\}&=\lim_{M\to\infty}\frac1M\sum_{k=1}^M{}^ks(t_1),\qquad \mathrm E\{F[s(t_1)]\}=\lim_{M\to\infty}\frac1M\sum_{k=1}^MF\bigl[{}^ks(t_1)\bigr],\\ \varphi_{ss}(t_1,t_2)&=\mathrm E\{s(t_1)\,s(t_2)\}. \end{aligned} \tag{1.1|1.2}$$
:::

⁠**So liest man das:** $\mathrm E\{\cdot\}$ heißt __Erwartungswert__ oder Scharmittelwert: Man mittelt über alle Musterfunktionen zum selben Zeitpunkt, also senkrecht in Abb. [1](#abb-1). Mit $F[x]=x^2$ erhält man den quadratischen Mittelwert. Die __Autokorrelationsfunktion__ mittelt das Produkt der Werte zu zwei Zeitpunkten. Sie sagt, wie stark der Wert bei $t_2$ mit dem bei $t_1$ zusammenhängt.

:::abbildung et3/k7schar 1
Drei Musterfunktionen eines Zufallsprozesses (simuliert, Mittelwert 1). Das Scharmittel bildet man senkrecht, über alle Musterfunktionen bei demselben $t_1$ (rot gestrichelt). Das Zeitmittel bildet man waagerecht, entlang einer Musterfunktion.
:::
