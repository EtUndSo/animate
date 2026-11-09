---
title: Stufe 6: Tiefenverarmung
pfad: Elektrotechnik / 4. Semester / Elektronische Materialien und Bauelemente 1 / Der reale MOS-Kondensator
order: 4260800
summary: Bisher war die Gleichspannung langsam und nur das Signal schnell.
tags: 
lang: de
---

<span class="anker" id="stufe-6"></span>

:::zweck
Bisher war die Gleichspannung langsam und nur das Signal schnell. Diese Stufe klärt, was geschieht, wenn auch die Gleichspannung den Elektronen davonläuft.
:::

**Die Idee.** Springt $V_\mathrm G$ über $V_\mathrm{th}$, verlangt das Gate sofort mehr negative Ladung im Halbleiter. Elektronen gibt es noch nicht, denn ihre Erzeugung dauert Sekunden. Die Löcher dagegen reagieren in Pikosekunden und weichen zurück: Die Zone wächst über $L_\mathrm{depl,max}$ hinaus, und $\varphi_\mathrm s$ steigt weit über $\varphi_\mathrm{s,SI}$. Das ist kein Gleichgewicht. In der Zone ist $n\cdot p<n_\mathrm i^2$, und die Erzeugung von Paaren überwiegt die Rekombination. Das Feld zieht die Elektronen an die Grenzfläche und die Löcher ins Substrat. Die Inversionsschicht entsteht nachträglich, die Zone schrumpft, bis das Gleichgewicht erreicht ist.

:::satz Satz 6.1 (Tiefenverarmung im p-Substrat)
<span class="anker" id="satz-6-1"></span>

Die Bilanz [(3.1)](die-reale-bilanz-und-die-verschobene-schwelle.html#gl-3-1) lautet mit der Inversionsladung $Q'_\mathrm{inv}$

<span class="anker" id="gl-6-1"></span>
$$V_\mathrm G=V_\mathrm{FB}+\varphi_\mathrm s+\gamma\sqrt{\varphi_\mathrm s}+\frac{|Q'_\mathrm{inv}|}{C'_\mathrm{IS}},\qquad\frac{\mathrm{d}|Q'_\mathrm{inv}|}{\mathrm{d} t}=j_\mathrm{gen}=\frac{e\,n_\mathrm iL_\mathrm{depl}}{2\tau_\text{rec}}. \tag{6.1}$$

Direkt nach dem Sprung ist $Q'_\mathrm{inv}=0$, und es gelten

<span class="anker" id="gl-6-2"></span>
$$\sqrt{\varphi_\mathrm s}=-\frac\gamma2+\sqrt{\frac{\gamma^2}{4}+V_\mathrm G-V_\mathrm{FB}},\qquad L_\mathrm{depl}=\sqrt{\frac{2\varepsilon\varphi_\mathrm s}{eN_\mathrm A}}>L_\mathrm{depl,max},\qquad C'_\mathrm{ges}=\frac{C'_\mathrm{IS}\,\varepsilon/L_\mathrm{depl}}{C'_\mathrm{IS}+\varepsilon/L_\mathrm{depl}}. \tag{6.2}$$
:::

⁠**So liest man das:** Das ist die Formel der Verarmung, ohne die Grenze bei $\varphi_\mathrm{s,SI}$. Die Kapazität fällt unter das Plateau $C'_\mathrm{min}$. **Gültigkeit:** Der Sprung ist schneller als die Erzeugung, und nur thermische Generation in der Zone liefert Elektronen.

:::herleitung Ohne Elektronen bleibt nur die Zone
$Q'_\mathrm{SC}$ ist die Summe aus der Ionenladung $-\sqrt{2\varepsilon eN_\mathrm A\varphi_\mathrm s}$ und $Q'_\mathrm{inv}$. Mit $Q'_\mathrm{inv}=0$ wird [(3.1)](die-reale-bilanz-und-die-verschobene-schwelle.html#gl-3-1) eine quadratische Gleichung für $\sqrt{\varphi_\mathrm s}$. Jedes erzeugte Elektron erhöht $|Q'_\mathrm{inv}|$ um $e$.
:::

:::abbildung gemb1/k16tief 6
Rechenmodell bei hoher Frequenz. Links: Bei langsamer Gleichspannung bleibt das Plateau (grün), bei schneller fällt die Kapazität weiter (rot). Der Pfeil zeigt die Rückkehr nach einem Sprung auf 3 V. Rechts: Dieselbe Rückkehr über der Zeit. Nach 21 s ist das Gleichgewicht (grün gepunktet) erreicht.
:::

::::beispiel
Ein Sprung von unterhalb $V_\mathrm{th}$ auf 3 V ergibt $V_\mathrm G-V_\mathrm{FB}=3{,}96$ V. Daraus folgen $\varphi_\mathrm s=2{,}97$ V, $L_\mathrm{depl}=358$ nm, das 1,95-Fache von $L_\mathrm{depl,max}$, und $C'_\mathrm{ges}=24{,}8\,\mathrm{nF/cm^2}$, das 0,144-Fache von $C'_\mathrm{IS}$. Im Gleichgewicht wären es $\varphi_\mathrm s=0{,}956$ V, 203 nm und $|Q'_\mathrm{inv}|=422\,\mathrm{nC/cm^2}$. Diese Ladung geteilt durch $j_\mathrm{gen}$ bei mittlerer Zonenweite ergibt 24 s, die Lösung von [(6.1)](#gl-6-1) ergibt 21 s. **Rampe:** Steigt $V_\mathrm G$ gleichmäßig, braucht die Schicht $\mathrm{d}|Q'_\mathrm{inv}|/\mathrm{d} t=C'_\mathrm{IS}\,\mathrm{d} V_\mathrm G/\mathrm{d} t$. Das schafft die Erzeugung nur bis $j_\mathrm{gen}/C'_\mathrm{IS}=75$ mV/s. Bei 1 V/s fehlt der Faktor 13.
::::

⁠**Grenzfälle:** Für $V_\mathrm G<V_\mathrm{th}$ gibt [(6.2)](#gl-6-2) den Gleichgewichtswert, für $\tau_\text{rec}\to0$ verschwindet die Tiefenverarmung. Licht erzeugt in der Zone ebenfalls Paare und verkürzt die Rückkehr.

:::frage Ist Tiefenverarmung dasselbe wie die Hochfrequenzkurve?
Nein. Bei der Hochfrequenzkurve ist nur das Signal schnell, die Gleichspannung ist langsam, und die Inversionsschicht existiert. Bei Tiefenverarmung ist die Gleichspannung selbst zu schnell, und die Schicht fehlt. Das Plateau zeigt $L_\mathrm{depl,max}$, die Tiefenverarmung liegt darunter.
:::

:::aufgabe Aufgabe 8 ★★ Ein Sprung und seine Folgen
<span class="anker" id="aufg-8"></span>

Gegeben sind $N_\mathrm A=10^{16}\,\mathrm{cm^{-3}}$, 30 nm $\mathrm{SiO_2}$, $V_\mathrm{FB}=-0{,}5$ V und $\tau_\text{rec}=10$ µ s.

<ol class="al">

<li>

Berechne $V_\mathrm{th}$, $L_\mathrm{depl,max}$ und das Plateau $C'_\mathrm{min}$.

</li>

<li>

$V_\mathrm G$ springt auf 4 V. Berechne $\varphi_\mathrm s$, $L_\mathrm{depl}$ und $C'_\mathrm{ges}$ direkt danach.

</li>

<li>

Schätze die Zeit bis zum Gleichgewicht mit $|Q'_\mathrm{inv}|\approx C'_\mathrm{IS}(V_\mathrm G-V_\mathrm{th})$ und der mittleren Zonenweite.

</li>

</ol>

:::loesung
(a) $C'_\mathrm{IS}=115{,}1\,\mathrm{nF/cm^2}$, $\gamma=0{,}500\,\sqrt{\mathrm V}$. $V_\mathrm{th}=-0{,}5+0{,}720+0{,}425=0{,}645$ V, $L_\mathrm{depl,max}=305$ nm, $C'_\mathrm{min}=26{,}2\,\mathrm{nF/cm^2}$. (b) $\sqrt{\varphi_\mathrm s}=-0{,}250+\sqrt{0{,}0626+4{,}5}=1{,}886$, also $\varphi_\mathrm s=3{,}56$ V, $L_\mathrm{depl}=678$ nm und $C'_\mathrm{ges}=13{,}5\,\mathrm{nF/cm^2}$. (c) $|Q'_\mathrm{inv}|=386\,\mathrm{nC/cm^2}$, mittlere Weite 491 nm, $j_\mathrm{gen}=3{,}5\cdot10^{-9}\,\mathrm{A/cm^2}$, also rund 110 s.
:::
:::
