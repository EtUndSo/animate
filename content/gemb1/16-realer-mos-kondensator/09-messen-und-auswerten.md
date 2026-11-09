---
title: Stufe 7: Messen und Auswerten
pfad: Elektrotechnik / 4. Semester / Elektronische Materialien und Bauelemente 1 / Der reale MOS-Kondensator
order: 4260900
summary: Eine gemessene Kurve soll Dicke, Dotierung, Ladungen und Zustandsdichte eines fertigen Kondensators liefern.
tags: 
lang: de
---

<span class="anker" id="stufe-7"></span>

:::zweck
Eine gemessene Kurve soll Dicke, Dotierung, Ladungen und Zustandsdichte eines fertigen Kondensators liefern. Diese Stufe gibt den Rechenweg.
:::

**Die Idee.** Jeder Abschnitt der Kurve hängt an einer anderen Größe. Links oben zählt nur der Isolator, auf dem Plateau zusätzlich die größte Zone, und die Lage der Kurve auf der Spannungsachse enthält $V_\mathrm{FB}$. Man liest die Größen also nacheinander ab. Bei hoher Frequenz legt man ein Signal $v$ an und misst den Strom, $C=|i|/(2\pi fv)$. Quasi-statisch fährt man $V_\mathrm G$ langsam hoch und misst $i=C\,\mathrm{d} V_\mathrm G/\mathrm{d} t$, unterhalb der Rampengrenze aus Stufe [6](tiefenverarmung.html#stufe-6). Mit 1 mm$^2$ sind das im Rechenmodell 109 µ A bei 1 MHz und 10 mV, aber nur 35 pA bei 20 mV/s.

:::satz Satz 7.1 (Auswertung einer C-V-Kennlinie)
<span class="anker" id="satz-7-1"></span>

Mit der Gatefläche $A$ gilt der Reihe nach:

<ol>

<li>

⁠**Typ:** Große Kapazität bei negativem $V_\mathrm G$ heißt p-Substrat, bei positivem n-Substrat.

</li>

<li>

⁠**Isolator:** $C'_\mathrm{IS}\approx C_\mathrm{max}/A$ und $d_\mathrm{IS}=\varepsilon_\mathrm{IS}/C'_\mathrm{IS}$.

</li>

<li>

⁠**Zone:** Aus dem Plateau der Hochfrequenzkurve folgt $L_\mathrm{depl,max}=\varepsilon\,(1/C'_\mathrm{min}-1/C'_\mathrm{IS})$.

</li>

<li>

⁠**Dotierung:** $N_\mathrm A=2\varepsilon\varphi_\mathrm{s,SI}/(eL_\mathrm{depl,max}^2)$ mit $\varphi_\mathrm{s,SI}=2V_\mathrm T\ln(N_\mathrm A/n_\mathrm i)$, im Wechsel gerechnet.

</li>

<li>

⁠**Flachband:** $V_\mathrm{FB}$ ist die Stelle, an der die Kurve den Wert $C'_\mathrm{IS}C'_\mathrm{FB}/(C'_\mathrm{IS}+C'_\mathrm{FB})$ hat. Auch $V_\mathrm{th}$ liefert sie über [(3.2)](die-reale-bilanz-und-die-verschobene-schwelle.html#gl-3-2).

</li>

<li>

⁠**Stoffe und Ladungen:** $V_\mathrm{FB}$ über $d_\mathrm{IS}$ ist eine Gerade mit dem Achsenabschnitt $\Delta\Phi/e$ und der Steigung $-(Q'_\mathrm{IS}+Q'_\mathrm{SS})/\varepsilon_\mathrm{IS}$.

</li>

<li>

⁠**Interfacezustände:** Aus beiden Kurven beim selben $V_\mathrm G$ folgt

<span class="anker" id="gl-7-1"></span>
$$e^2D_\mathrm{it}\approx C'_\mathrm{it}=\Bigl(\frac1{C'_\mathrm{nf}}-\frac1{C'_\mathrm{IS}}\Bigr)^{-1}-C'_\mathrm{depl}=\Bigl(\frac1{C'_\mathrm{nf}}-\frac1{C'_\mathrm{IS}}\Bigr)^{-1}-\Bigl(\frac1{C'_\mathrm{hf}}-\frac1{C'_\mathrm{IS}}\Bigr)^{-1}. \tag{7.1}$$

</li>

</ol>

In Verarmung ist außerdem $1/C'^2_\mathrm{ges}$ eine Gerade in $V_\mathrm G$:

<span class="anker" id="gl-7-2"></span>
$$\frac1{C'^2_\mathrm{ges}}=\frac1{C'^2_\mathrm{IS}}+\frac{2\,(V_\mathrm G-V_\mathrm{FB})}{e\varepsilon N_\mathrm A}. \tag{7.2}$$
:::

⁠**So liest man das:** In [(7.1)](#gl-7-1) ist der erste Term $C'_\mathrm{depl}+C'_\mathrm{it}$, der zweite $C'_\mathrm{depl}$ allein. Die Gerade [(7.2)](#gl-7-2) liefert $N_\mathrm A$ aus der Steigung und $V_\mathrm{FB}$ aus dem Schnitt mit $1/C'^2_\mathrm{IS}$, ohne Rechnung im Wechsel. **Gültigkeit:** [(7.2)](#gl-7-2) gilt für $V_\mathrm{FB}<V_\mathrm G<V_\mathrm{th}$ in der Schottky-Näherung mit $D_\mathrm{it}\approx0$, sonst wird die Kurve flacher. [(7.1)](#gl-7-1) setzt voraus, dass die Zustände bei hoher Frequenz nicht folgen.

:::herleitung Die Gerade
In Verarmung ist $1/C'_\mathrm{ges}=1/C'_\mathrm{IS}+L_\mathrm{depl}/\varepsilon$ mit $L_\mathrm{depl}/\varepsilon=a\sqrt{\varphi_\mathrm s}$ und $a=\sqrt{2/(e\varepsilon N_\mathrm A)}$. Es gilt $a\gamma=2/C'_\mathrm{IS}$. Mit $\sqrt{\varphi_\mathrm s}=-\gamma/2+\sqrt{\gamma^2/4+V_\mathrm G-V_\mathrm{FB}}$ aus [(3.2)](die-reale-bilanz-und-die-verschobene-schwelle.html#gl-3-2) hebt sich der Term $1/C'_\mathrm{IS}$ weg, und es bleibt $1/C'_\mathrm{ges}=a\sqrt{\gamma^2/4+V_\mathrm G-V_\mathrm{FB}}$. Quadrieren ergibt [(7.2)](#gl-7-2).
:::

:::abbildung gemb1/k16auswertung 7
Das Rechenmodell als Messung bei hoher Frequenz. Links: Die Kurve mit den Ablesewerten. Rechts: Dieselbe Kurve als $1/C'^2$. Sie folgt der Geraden [(7.2)](#gl-7-2) (rot gestrichelt) und knickt bei $V_\mathrm{th}$ ab.
:::

::::beispiel
Bei $V_\mathrm G=-5$ V misst man 170,4 nF/cm$^2$. Daraus folgt $d_\mathrm{IS}=20{,}3$ nm, um 1,3 % zu groß, weil $C'_\mathrm{SC}$ endlich bleibt. Das Plateau 42,6 nF/cm$^2$ gibt die Weite 183 nm. Mit dem Start $\varphi_\mathrm{s,SI}=0{,}8$ V folgen $N_\mathrm A=3{,}09\cdot10^{16}$, $3{,}01\cdot10^{16}$ und $3{,}00\cdot10^{16}\,\mathrm{cm^{-3}}$. Der Flachbandwert 123,9 nF/cm$^2$ liegt bei $-0{,}96$ V. Die Gerade bestätigt das: $1/C'^2=2{,}20$ bei $-0{,}5$ V und 4,21 bei 0 V in $10^{-4}\,\mathrm{cm^4/nF^2}$ ergeben die Steigung 4,02, also $N_\mathrm A=3{,}0\cdot10^{16}\,\mathrm{cm^{-3}}$.
::::

⁠**Grenzfall:** Die wahre Kurve hat eine weiche Zonenkante. Dadurch schneidet ihre Gerade die Linie $1/C'^2_\mathrm{IS}$ bei $-0{,}94$ V, um rund $V_\mathrm T$ versetzt.

Kurz gesagt: Feste Ladung verschiebt die Kurve, Interfacezustände dehnen sie und heben $C'_\mathrm{nf}$ über $C'_\mathrm{hf}$, kleinere Dotierung senkt das Plateau, und Kapazität unter dem Plateau heißt, dass die Spannung zu schnell war.

:::frage Warum subtrahiert man in [(7.1)](#gl-7-1) nicht einfach $C'_\mathrm{nf}-C'_\mathrm{hf}$?
Weil $C'_\mathrm{it}$ nicht parallel zur Gesamtkapazität liegt, sondern parallel zu $C'_\mathrm{depl}$ hinter dem Isolator. Der Isolator in Reihe staucht jeden Unterschied. Erst nach dem Abziehen der Reihenschaltung stehen die Kapazitäten nebeneinander.
:::

:::aufgabe Aufgabe 9 ★★★ Einen unbekannten Kondensator entschlüsseln
<span class="anker" id="aufg-9"></span>

Eine Hochfrequenzkurve mit $\mathrm{SiO_2}$ auf Silizium und $A=0{,}25\,\mathrm{mm^2}$ zeigt $C_\mathrm{max}=345$ pF bei positivem $V_\mathrm G$, das Plateau 87,5 pF bei negativem $V_\mathrm G$ und $V_\mathrm{th}=-1{,}45$ V. $D_\mathrm{it}$ ist vernachlässigbar.

<ol class="al">

<li>

Welcher Typ liegt vor? Berechne $C'_\mathrm{IS}$ und $d_\mathrm{IS}$.

</li>

<li>

Berechne $L_\mathrm{depl,max}$ und die Dotierung.

</li>

<li>

Berechne $\gamma$ und $V_\mathrm{FB}$.

</li>

<li>

Der Isolator sei frei von Ladungen. Welche Austrittsarbeit hat das Gate? Wie groß ist das Feld im Isolator bei $V_\mathrm{th}$?

</li>

</ol>

:::loesung
(a) Große Kapazität bei positivem $V_\mathrm G$: n-Substrat. $C'_\mathrm{IS}=138\,\mathrm{nF/cm^2}$, $d_\mathrm{IS}=25$ nm. (b) $C'_\mathrm{min}=35{,}0\,\mathrm{nF/cm^2}$, $L_\mathrm{depl,max}=221$ nm. Mit $|\varphi_\mathrm{s,SI}|=0{,}75$ V als Start folgen $N_\mathrm D=1{,}99\cdot10^{16}$ und $2{,}00\cdot10^{16}\,\mathrm{cm^{-3}}$, dazu $|\varphi_\mathrm{s,SI}|=0{,}756$ V. (c) $\gamma=0{,}591\,\sqrt{\mathrm V}$, $V_\mathrm{FB}=-1{,}45+0{,}756+0{,}514=-0{,}18$ V. (d) $\Phi_\mathrm{SC}=4{,}23$ eV, $\Phi_\mathrm M=\Phi_\mathrm{SC}+eV_\mathrm{FB}=4{,}05$ eV. Über dem Isolator liegen $-0{,}514$ V, das Feld ist 20,5 MV/m.
:::
:::

:::aufgabe Aufgabe 10 ★★ Zustandsdichte aus zwei Kurven
<span class="anker" id="aufg-10"></span>

Am Oxid des Rechenmodells misst du in Verarmung beim selben $V_\mathrm G$ die Werte $C'_\mathrm{nf}=94{,}0\,\mathrm{nF/cm^2}$ und $C'_\mathrm{hf}=74{,}0\,\mathrm{nF/cm^2}$.

<ol class="al">

<li>

Berechne $C'_\mathrm{depl}$, $C'_\mathrm{it}$ und $D_\mathrm{it}$.

</li>

<li>

Um welchen Faktor irrt man mit $C'_\mathrm{nf}-C'_\mathrm{hf}$?

</li>

<li>

Berechne $L_\mathrm{depl}$ und $\varphi_\mathrm s$ für $N_\mathrm A=3\cdot10^{16}\,\mathrm{cm^{-3}}$.

</li>

</ol>

:::loesung
(a) $(1/94{,}0-1/172{,}7)^{-1}=206{,}3\,\mathrm{nF/cm^2}$, $C'_\mathrm{depl}=129{,}5\,\mathrm{nF/cm^2}$, also $C'_\mathrm{it}=76{,}8\,\mathrm{nF/cm^2}$ und $D_\mathrm{it}=4{,}8\cdot10^{11}/(\mathrm{eV\,cm^2})$. (b) Die Differenz ist 20,0 nF/cm$^2$, um den Faktor 3,84 zu klein. (c) $L_\mathrm{depl}=\varepsilon/C'_\mathrm{depl}=80$ nm, $\varphi_\mathrm s=eN_\mathrm AL_\mathrm{depl}^2/(2\varepsilon)=0{,}148$ V.
:::
:::
