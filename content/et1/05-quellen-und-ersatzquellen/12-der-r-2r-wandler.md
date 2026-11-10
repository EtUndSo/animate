---
title: Stufe 10: Der R-2R-Wandler
pfad: Elektrotechnik / 1. Semester / ET1 – Grundgebiete der Elektrotechnik 1: Einführung in die Schaltungsanalyse / Quellen und Ersatzquellen
adresse: elektrotechnik/1-semester/grundlagen-der-elektrotechnik/quellen-und-ersatzquellen
knoten: Kapitel 5: Quellen und Ersatzquellen
order: 1151200
summary: Ein Prozessor kennt nur Bits, ein Lautsprecher braucht eine Spannung.
tags: Digital-Analog-Wandler
lang: de
---

<span class="anker" id="stufe-10"></span>

:::zweck
Ein Prozessor kennt nur Bits, ein Lautsprecher braucht eine Spannung. Der R-2R-Wandler übersetzt das. Er ist Überlagerung und Ersatzquelle in einer einzigen Schaltung.
:::

**Die Idee.** Ein __Digital-Analog-Wandler__ macht aus einer Binärzahl mit den Bits $d_2d_1d_0$ eine Spannung. In Abb. [12](#abb-12) legt jeder Schalter seinen 2$R$-Widerstand entweder an $U_\mathrm{ref}$ (Bit 1) oder an 0 V (Bit 0). Ein Schalter auf 0 V ist eine abgeschaltete Spannungsquelle. Die Überlagerung steckt also schon im Aufbau: Jedes gesetzte Bit ist eine Quelle, alle anderen sind Drähte. Die Leiter aus $R$ und $2R$ ist so bemessen, dass jede Sprosse die Wirkung halbiert.

:::abbildung et1/k5r2r 12
R-2R-Wandler für drei Bit in der Stellung 101. Jeder Umschalter verbindet seinen Widerstand mit $U_\mathrm{ref}$ oder mit Masse. Abgegriffen wird rechts oben.
:::

:::satz Satz 10.1 (R-2R-Leiter)
<span class="anker" id="satz-10-1"></span>

Für den Wandler aus Abb. [12](#abb-12) bei offenem Ausgang gilt

<span class="anker" id="gl-10-1"></span>
$$U_\mathrm{aus}=U_\mathrm{ref}\left(\frac{d_2}{2}+\frac{d_1}{4}+\frac{d_0}{8}\right),\qquad R_\mathrm{i}=R. \tag{10.1}$$
:::

⁠**So liest man das:** $d_k$ ist 0 oder 1, $U_\mathrm{ref}$ die feste Bezugsspannung (einige Volt), $R$ meist einige k$\Omega$. Das höchstwertige Bit trägt die halbe Bezugsspannung bei, jedes weitere die Hälfte des vorigen. $R_\mathrm{i}$ hängt nicht von der Schalterstellung ab: Beim Abschalten wird $U_\mathrm{ref}$ zu 0 V, und dann führt jeder Zweig nach Masse, wie auch immer sein Schalter steht. **Gültigkeit:** ideale Schalter ohne eigenen Widerstand, Ausgang unbelastet.

:::herleitung Ersatzquelle von links nach rechts
Am linken Knoten liegen 2$R$ gegen Masse und 2$R$ gegen $U_0=d_0U_\mathrm{ref}$. Das ist eine Ersatzquelle mit $\frac12U_0$ und $2R\parallel2R=R$. Mit dem Längswiderstand werden daraus $\frac12U_0$ und $2R$. Am nächsten Knoten trifft das auf 2$R$ gegen $U_1=d_1U_\mathrm{ref}$: wieder zwei gleiche Zweige, also die Mittelwertsbildung aus [(7.2)](quellen-zusammenschalten.html#gl-7-2), die Ersatzquelle $\frac12\bigl(\frac12U_0+U_1\bigr)$ und wieder $R$. Der letzte Knoten wiederholt das:

$$U_\mathrm{aus}=\tfrac12\Bigl(\tfrac12\bigl(\tfrac12U_0+U_1\bigr)+U_2\Bigr)=\tfrac12U_2+\tfrac14U_1+\tfrac18U_0.$$

Dieselbe Zahl liefert die Überlagerung. Beispiel Quelle $U_1$: Am mittleren Knoten sieht sie links 2$R$ und rechts $R+2R=3R$, zusammen $\frac65R$. Der Teiler ergibt dort $\frac{6/5}{6/5+2}=\frac38U_1$. Der Weg zum Ausgang teilt noch einmal mit $\frac{2R}{R+2R}=\frac23$, also $\frac38\cdot\frac23=\frac14$.
:::

::::beispiel
Mit $U_\mathrm{ref}=8$ V und $R=1$ k$\Omega$ wiegen die Bits 4 V, 2 V und 1 V. Die Stellung 101 ergibt 5 V. Eine Last mit $R_\mathrm{L}=R$ bildet mit $R_\mathrm{i}$ einen Teiler und halbiert das auf 2,5 V. Deshalb folgt in echten Wandlern ein Operationsverstärker ([Kapitel 11](/wissen/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/der-operationsverstarker/der-operationsverstaerker.html)) mit sehr hohem Eingangswiderstand: Er zieht praktisch keinen Strom, die Leiter bleibt im Leerlauf.
::::

⁠**Grenzfälle:** Stellung 000 ergibt 0 V, Stellung 111 ergibt 7 V, eine Stufe unter $U_\mathrm{ref}$.

:::ltspice Der Wandler zählt
⁠**Zeichnen:** Abb. [12](#abb-12) ohne Schalter: 2$R$ von Knoten `n0` nach Masse, dann je 2$R$ von `n0`, `n1`, `n2` zu einer Quelle `voltage` gegen Masse und $R$ zwischen den Knoten, $R=1$ k$\Omega$. Die Quellen zählen binär: `PULSE(0 8 1m 1u 1u 1m 2m)`, `PULSE(0 8 2m 1u 1u 2m 4m)`, `PULSE(0 8 4m 1u 1u 4m 8m)`.

⁠**Direktive:** `.tran 8m`

⁠**Was du siehst:** `V(n2)` ist eine Treppe mit Stufen von 1 V, von 0 V bis 7 V. Mit einer Last von 1 k$\Omega$ an `n2` steigt sie nur noch bis 3,5 V. Mit 3 k$\Omega$ erscheint auf der obersten Stufe dein Ergebnis aus Aufgabe [12](#aufg-12)(c).
:::

:::frage Wozu dient der einzelne 2$R$-Widerstand ganz links?
Er macht die Leiter gleichmäßig. Mit ihm ist alles links von jedem Knoten eine Ersatzquelle mit $2R$, genau wie der Zweig des eigenen Schalters. Nur dann entstehen zwei gleiche Zweige und ein reiner Mittelwert. Ohne ihn wäre der linke Zweig $3R$ groß, und die Gewichte wären nicht mehr binär.
:::

:::aufgabe Aufgabe 12 ★★ Vier Bit
<span class="anker" id="aufg-12"></span>

(a) Ein Wandler mit vier Bit läuft an $U_\mathrm{ref}=16$ V. Wie groß sind die Stufe, der Höchstwert und die Spannung bei 1011? (b) Wie groß ist eine Stufe bei acht Bit an 5 V? (c) Der Drei-Bit-Wandler aus dem Beispiel steht auf 111 und speist $R_\mathrm{L}=3R$. Welche Spannung stellt sich ein?

:::loesung
(a) Stufe $16\,\mathrm{V}/2^4=1$ V. Höchstwert $15$ V. 1011: $8+0+2+1=11$ V. Die Formel läuft weiter mit $d_3/2+d_2/4+d_1/8+d_0/16$.

(b) $5\,\mathrm{V}/256=19{,}5$ mV.

(c) Leerlauf 7 V, Innenwiderstand $R$. Teiler: $7\,\mathrm{V}\cdot\frac{3R}{R+3R}=5{,}25$ V.
:::
:::
