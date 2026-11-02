---
title: Stufe 6: Die Schwellspannung
pfad: Elektrotechnik / 4. Semester / Elektronische Materialien und Bauelemente 1 / Die MOS-Kapazität
order: 4250800
summary: Die Bandverbiegung beim Einsatz der Inversion ist bekannt.
tags: Schwellspannung, Inversionsladung
lang: de
---

<span class="anker" id="stufe-6"></span>

:::zweck
Die Bandverbiegung beim Einsatz der Inversion ist bekannt. Von außen stellt man aber die Gatespannung ein. Diese Stufe rechnet um und zeigt, wohin weitere Spannung geht.
:::

**Die Idee.** Bis zum Einsatz der starken Inversion besteht die Ladung im Halbleiter fast nur aus Ionen der Verarmungszone. Bilanz [(2.2)](wie-sich-die-gatespannung-aufteilt.html#gl-2-2) und Ladung [(4.2)](verarmung.html#gl-4-2) geben also direkt die Gatespannung. Darüber liefern die Elektronen die Ladung, und das auf engstem Raum: Eine kleine Zunahme von $\varphi_\mathrm s$ erzeugt viel neue Ladung. Fast jedes weitere Volt fällt deshalb am Isolator ab, wie bei der Akkumulation.

:::satz Satz 6.1 (Schwellspannung des idealen MIS-Kondensators)
<span class="anker" id="satz-6-1"></span>

Die __Schwellspannung__ $V_\mathrm{th}$ ist die Gatespannung beim Einsatz der starken Inversion:

<span class="anker" id="gl-6-1"></span>
$$V_\mathrm{th}=\varphi_\mathrm{s,SI}-\frac{Q'_\mathrm{SC}(\varphi_\mathrm{s,SI})}{C'_\mathrm{IS}}=\varphi_\mathrm{s,SI}+\gamma\sqrt{\varphi_\mathrm{s,SI}}. \tag{6.1}$$

Für den Einsatz der schwachen Inversion gilt ebenso $V_\mathrm{WI}=\varphi_\mathrm{s,WI}+\gamma\sqrt{\varphi_\mathrm{s,WI}}$. Oberhalb der Schwelle gilt näherungsweise

<span class="anker" id="gl-6-2"></span>
$$V_\mathrm G=\varphi_\mathrm s-\frac{Q'_\mathrm{SC}}{C'_\mathrm{IS}},\qquad\varphi_\mathrm s\approx\varphi_\mathrm{s,SI},\qquad Q'_\mathrm{inv}\approx-C'_\mathrm{IS}\bigl(V_\mathrm G-V_\mathrm{th}\bigr). \tag{6.2}$$
:::

⁠**So liest man das:** Der erste Summand in [(6.1)](#gl-6-1) ist die Spannung im Halbleiter, der zweite die am Isolator. $Q'_\mathrm{inv}$ ist die __Inversionsladung__, die Flächenladung der Elektronen. Ein n-Substrat hat bei gleicher Dotierung gerade den negativen Wert von $V_\mathrm{th}$. **Gültigkeit:** idealer Kondensator, Boltzmann-Näherung. Bei $V_\mathrm{WI}$ ist $n(0)=n_\mathrm i\ll N_\mathrm A$, dort zählen nur die Ionen.

:::abbildung gemb1/k15schwelle 6
Exakte Lösung des Rechenmodells. Links: $\varphi_\mathrm s$ folgt zunächst der Gatespannung und bleibt über $V_\mathrm{th}$ fast stehen. Rechts: Die Verarmungsladung sättigt, die Inversionsladung wächst linear. Gestrichelt die Näherung [(6.2)](#gl-6-2).
:::

**Beispiel.** Im Rechenmodell ist $V_\mathrm{WI}=0{,}389+0{,}360=0{,}749$ V und $V_\mathrm{th}=0{,}777+0{,}510=1{,}287$ V mit $Q'_\mathrm{SC}=-88{,}0\,\mathrm{nC/cm^2}$. Im Isolator herrschen dann 25,5 MV/m. Von $V_\mathrm{th}$ bis 3 V steigt $\varphi_\mathrm s$ nur von 0,777 auf 0,936 V, die Verarmungsladung von 88,0 auf 96,5 nC/cm$^2$. Die Elektronen liefern 260 nC/cm$^2$, das sind $1{,}6\cdot10^{12}$ Elektronen je cm$^2$. Die Näherung [(6.2)](#gl-6-2) ergibt 296 nC/cm$^2$, sie überschätzt um den Teil der Spannung, der noch in $\varphi_\mathrm s$ geht. **Grenzfälle:** $d_\mathrm{IS}\to0$ gibt die untere Schranke $V_\mathrm{th}\to\varphi_\mathrm{s,SI}$, 2 nm Oxid ergeben 0,828 V. Stärkere Dotierung vergrößert die Ionenladung: Bei 20 nm Oxid sind es 1,004 V für $N_\mathrm A=10^{16}\,\mathrm{cm^{-3}}$ und 1,806 V für $10^{17}\,\mathrm{cm^{-3}}$.

:::frage Geschieht an der Schwellspannung etwas Sprunghaftes?
Nein. $n(0)$ wächst stetig, und auch darunter gibt es Elektronen. $V_\mathrm{th}$ ist eine Festlegung. Sie ist sinnvoll, weil sich dort in wenigen zehn Millivolt das Verhalten ändert: Darunter wächst die Ladung mit der Wurzel von $\varphi_\mathrm s$, darüber exponentiell.
:::

:::aufgabe Aufgabe 7 ★★ Schwellspannung berechnen
<span class="anker" id="aufg-7"></span>

Gegeben sind $N_\mathrm A=10^{17}\,\mathrm{cm^{-3}}$ und $d_\mathrm{IS}=10$ nm $\mathrm{SiO_2}$.

<ol class="al">

<li>

Berechne $\varphi_\mathrm{s,SI}$, $L_\mathrm{depl,max}$, $Q'_\mathrm{SC}$ beim Übergang und die Spannung $V_\mathrm{IS}$ dort.

</li>

<li>

Berechne $\gamma$, $V_\mathrm{th}$ und $V_\mathrm{WI}$. Welche Raumladungsdichte herrscht bei $V_\mathrm{WI}$ an der Grenzfläche?

</li>

<li>

Schätze Inversionsladung und Elektronen je cm$^2$ bei $V_\mathrm G=2$ V.

</li>

</ol>

:::loesung
(a) $\varphi_\mathrm{s,SI}=2\cdot0{,}420\,\mathrm{V}=0{,}840$ V, $L_\mathrm{depl,max}=104$ nm, $Q'_\mathrm{SC}=-166{,}9\,\mathrm{nC/cm^2}$, $V_\mathrm{IS}=166{,}9/345{,}3\,\mathrm{V}=0{,}483$ V. (b) $\gamma=0{,}528\,\sqrt{\mathrm V}$, $V_\mathrm{th}=0{,}840+0{,}483=1{,}323$ V. $V_\mathrm{WI}=0{,}420+0{,}342=0{,}762$ V. Dort sind beide Trägerdichten $n_\mathrm i$, also ist $\rho\approx-eN_\mathrm A=-16{,}0$ mC/cm$^3$. (c) $Q'_\mathrm{inv}\approx-345{,}3\,\mathrm{nF/cm^2}\cdot0{,}677\,\mathrm{V}=-234\,\mathrm{nC/cm^2}$, also $1{,}46\cdot10^{12}$ Elektronen je cm$^2$. Der Wert ist eine obere Schätzung.
:::
:::

:::aufgabe Aufgabe 8 ★★★ Schwelle entwerfen
<span class="anker" id="aufg-8"></span>

Der Kondensator soll bei $N_\mathrm A=3\cdot10^{16}\,\mathrm{cm^{-3}}$ die Schwelle $V_\mathrm{th}=1{,}0$ V haben.

<ol class="al">

<li>

Welche Oxiddicke braucht man? Warum ist $V_\mathrm{th}=0{,}7$ V bei dieser Dotierung unerreichbar?

</li>

<li>

Bei gleicher Dicke steigt die Dotierung auf $5\cdot10^{16}\,\mathrm{cm^{-3}}$. Wie groß wird $V_\mathrm{th}$?

</li>

</ol>

:::loesung
(a) Aus [(6.1)](#gl-6-1) folgt $\gamma=(V_\mathrm{th}-\varphi_\mathrm{s,SI})/\sqrt{\varphi_\mathrm{s,SI}}=0{,}2227/0{,}8817\,\sqrt{\mathrm V}=0{,}2526\,\sqrt{\mathrm V}$. Dann ist $C'_\mathrm{IS}=\sqrt{2\varepsilon eN_\mathrm A}/\gamma=395\,\mathrm{nF/cm^2}$, also $d_\mathrm{IS}=8{,}74$ nm. $V_\mathrm{th}$ kann nicht unter $\varphi_\mathrm{s,SI}=0{,}777$ V sinken, denn der Isolatoranteil ist nie negativ. (b) $\varphi_\mathrm{s,SI}=0{,}804$ V, und $\gamma$ wächst mit $\sqrt{N_\mathrm A}$, das ergibt $V_\mathrm{th}=1{,}096$ V.
:::
:::
