---
title: Stufe 6: Der Aus-Zustand
pfad: Elektrotechnik / 4. Semester / Elektronische Materialien und Bauelemente 1 / Der MOSFET
order: 4270800
summary: Unter V th sagt die Parabel I mathrm D=0 .
tags: Unterschwellsteigung
lang: de
---

<span class="anker" id="stufe-6"></span>

:::zweck
Unter $V_\mathrm{th}$ sagt die Parabel $I_\mathrm D=0$. Diese Stufe zeigt, wie groß der Strom dort wirklich ist und wie schnell er mit $V_\mathrm{GS}$ fällt.
:::

**Die Idee.** Die Barriere aus Stufe [2](die-barriere-im-kanal.html#stufe-2) ist endlich. Wärme hebt Elektronen aus der Source hinüber, wie in der Diode. Es sind so wenige, dass sie kein Feld längs des Kanals tragen, $V_\mathrm{DS}$ fällt fast ganz am Drain ab. Am Drain werden die Elektronen abgesaugt, an der Source strömen sie nach. Dazwischen entsteht ein Dichtegefälle, und der Strom ist Diffusion. Er wächst exponentiell, wenn die Barriere sinkt. Anders als in der Diode senkt man sie aber nicht direkt: Die Gatespannung muss durch einen kapazitiven Teiler.

:::satz Satz 6.1 (Unterschwellstrom)
<span class="anker" id="satz-6-1"></span>

Für $V_\mathrm{GS}<V_\mathrm{th}$ und $V_\mathrm{DS}\gg V_\mathrm T$ gilt mit der Oberflächenfeldstärke $\mathcal E_\mathrm s$ und der Schichtdicke $d_\mathrm{inv}$

<span class="anker" id="gl-6-1"></span>
$$I_\mathrm D=eD_\mathrm n\frac WL\,n(0)\,d_\mathrm{inv},\qquad d_\mathrm{inv}=\frac{V_\mathrm T}{\mathcal E_\mathrm s},\qquad\mathcal E_\mathrm s=\sqrt{\frac{2eN_\mathrm A\varphi_\mathrm s}{\varepsilon}}, \tag{6.1}$$

ausgeschrieben

<span class="anker" id="gl-6-2"></span>
$$I_\mathrm D=eD_\mathrm n\frac WL\,V_\mathrm T\sqrt{\frac{\varepsilon}{2eN_\mathrm A\varphi_\mathrm s}}\,\frac{n_\mathrm i^2}{N_\mathrm A}\exp\Bigl(\frac{\varphi_\mathrm s}{V_\mathrm T}\Bigr). \tag{6.2}$$
:::

⁠**So liest man das:** $\varphi_\mathrm s$ folgt aus $V_\mathrm{GS}=V_\mathrm{FB}+\varphi_\mathrm s+\gamma\sqrt{\varphi_\mathrm s}$, die Exponentialfunktion bestimmt den Verlauf. **Gültigkeit:** Verarmung und schwache Inversion. Bei $V_\mathrm{DS}\lesssim3V_\mathrm T$ bleibt am Drain die Dichte $n(0)\,\mathrm{e}^{-V_\mathrm{DS}/V_\mathrm T}$, dann kommt der Faktor $1-\mathrm{e}^{-V_\mathrm{DS}/V_\mathrm T}$ hinzu.

:::herleitung Diffusion durch eine dünne Schicht
Ohne Rekombination ist die Diffusionsstromdichte konstant, die Dichte fällt also linear von der Source bis null am Drain. Mit $n_\mathrm s$ Elektronen je Fläche an der Source folgt $I_\mathrm D=eD_\mathrm nWn_\mathrm s/L$. In $x$-Richtung steigt $E_\mathrm C$ an der Grenzfläche mit $e\mathcal E_\mathrm s$. Nach der Tiefe $V_\mathrm T/\mathcal E_\mathrm s$ ist der Boltzmann-Faktor auf $1/\mathrm{e}$ gefallen. Rechnet man die Schicht als Rechteck dieser Dicke, ist $n_\mathrm s=n(0)\,d_\mathrm{inv}$. Die Feldstärke ist $\mathcal E_\mathrm s=eN_\mathrm AL_\mathrm{depl}/\varepsilon$ ([Teil 15](/wissen/elektrotechnik/4-semester/elektronische-materialien-und-bauelemente-1/die-mos-kapazitat/die-mos-kapazitaet.html)), das ergibt [(6.1)](#gl-6-1).
:::

:::definition Definition 6.2 (Unterschwellsteigung)
<span class="anker" id="satz-6-2"></span>

Die __Unterschwellsteigung__ $S$ ist die Änderung von $V_\mathrm{GS}$, die $I_\mathrm D$ um eine Dekade (Faktor 10) ändert:

<span class="anker" id="gl-6-3"></span>
$$S=\Bigl(\frac{\partial\log_{10}I_\mathrm D}{\partial V_\mathrm{GS}}\Bigr)^{-1}. \tag{6.3}$$
:::

Streng ist $S$ der Kehrwert einer Steigung, deshalb sagt man auch inverse Unterschwellsteigung. Die Einheit ist mV/Dekade, kleiner ist besser.

:::satz Satz 6.3 (Unterschwellsteigung des MOSFET)
<span class="anker" id="satz-6-3"></span>

Die Gatespannung erreicht die Oberfläche nur über einen Teiler, und das begrenzt $S$:

<span class="anker" id="gl-6-4"></span>
$$\delta\varphi_\mathrm s=\delta V_\mathrm{GS}\,\frac{C'_\mathrm{IS}}{C'_\mathrm{IS}+C'_\mathrm{depl}},\qquad S=V_\mathrm T\ln(10)\,\frac{C'_\mathrm{IS}+C'_\mathrm{depl}}{C'_\mathrm{IS}}\ge V_\mathrm T\ln(10)=59{,}5\,\mathrm{mV/Dekade}. \tag{6.4}$$
:::

:::herleitung Von der Diode zum MOSFET
⁠**Diode.** Aus $j\propto\mathrm{e}^{eU_\mathrm{pn}/(k_\mathrm BT)}$ folgt

$$\frac{\partial\log_{10}j}{\partial U_\mathrm{pn}}=\frac1{\ln10}\cdot\frac1j\cdot\frac{\partial j}{\partial U_\mathrm{pn}}=\frac{e}{k_\mathrm BT\ln10},$$

also $V_\mathrm T\ln10$ je Dekade. Die Spannung verschiebt die Barriere dort eins zu eins.

⁠**MOSFET.** Aus [(6.2)](#gl-6-2) kommt derselbe Faktor mit $\varphi_\mathrm s$ statt $U_\mathrm{pn}$, die langsame Wurzel fällt nicht ins Gewicht. Also ist $S=V_\mathrm T\ln(10)\,\delta V_\mathrm{GS}/\delta\varphi_\mathrm s$. Isolator und Verarmungszone tragen dieselbe Ladungsänderung und bilden eine Reihenschaltung ([Teil 15](/wissen/elektrotechnik/4-semester/elektronische-materialien-und-bauelemente-1/die-mos-kapazitat/die-mos-kapazitaet.html)). Die Kapazität der Zone folgt aus $L_\mathrm{depl}$:

$$C'_\mathrm{depl}=\Bigl|\frac{\mathrm{d}(eN_\mathrm AL_\mathrm{depl})}{\mathrm{d}\varphi_\mathrm s}\Bigr|=eN_\mathrm A\cdot\frac{\varepsilon}{eN_\mathrm AL_\mathrm{depl}}=\frac{\varepsilon}{L_\mathrm{depl}}.$$

Für die Gatekapazität gilt ebenso: Im Aus-Zustand ist $C_\mathrm G=WL\,C'_\mathrm{IS}C'_\mathrm{depl}/(C'_\mathrm{IS}+C'_\mathrm{depl})$, in starker Inversion $C_\mathrm G\approx WLC'_\mathrm{IS}$, denn dort ist die Inversionskapazität viel größer als $C'_\mathrm{IS}$. Grenzflächenzustände ([Teil 16](/wissen/elektrotechnik/4-semester/elektronische-materialien-und-bauelemente-1/der-reale-mos-kondensator/realer-mos-kondensator.html)) liegen parallel zu $C'_\mathrm{depl}$ und vergrößern $S$ weiter.
:::

:::abbildung gemb1/k17unterschwelle 6
Links: Kapazitiver Teiler im Aus-Zustand. Rechts: Transferkennlinie des Rechenmodells bei $V_\mathrm{DS}=5$ V, logarithmisch. Blau die numerische Rechnung mit Drift und Diffusion, rot gestrichelt [(6.2)](#gl-6-2), grün gestrichelt [(4.1)](ausgangskennlinien.html#gl-4-1). Das Dreieck zeigt eine Dekade bei $V_\mathrm{GS}=0$.
:::

::::beispiel
Bei $V_\mathrm{GS}=0$ ist $\varphi_\mathrm s=0{,}539$ V, $L_\mathrm{depl}=152$ nm, $\mathcal E_\mathrm s=7{,}1$ MV/m und $d_\mathrm{inv}=3{,}7$ nm. Mit $n(0)=3{,}0\cdot10^{12}\,\mathrm{cm^{-3}}$ ergibt [(6.1)](#gl-6-1) den Strom $I_\mathrm D=23$ pA, die numerische Rechnung 31 pA. Im Mittel sitzen dabei nur 1,4 Elektronen im Kanal. Gegen 3,09 mA bei $V_\mathrm{GS}=3$ V sind das acht Größenordnungen. Es ist $C'_\mathrm{depl}=68\,\mathrm{nF/cm^2}$, nur 72 % von $\delta V_\mathrm{GS}$ erreichen die Oberfläche, und $S=83$ mV/Dekade. Die Gatekapazität ist 0,12 pF statt 0,43 pF.
::::

⁠**Grenzfälle:** Für $C'_\mathrm{IS}\gg C'_\mathrm{depl}$ folgt die Oberfläche dem Gate eins zu eins, $S\to59{,}5$ mV/Dekade. Für $C'_\mathrm{IS}=C'_\mathrm{depl}$ ist $\delta\varphi_\mathrm s=\frac12\delta V_\mathrm{GS}$ und $S=119$ mV/Dekade: Die Bänder lassen sich nicht mehr wirksam verschieben. Bei 350 K ist die Grenze 69 mV/Dekade.

:::frage Warum schaltet ein MOSFET bei 300 K nicht steiler als 60 mV/Dekade, so gut das Gate auch ist?
Das Gate kann die Barriere höchstens eins zu eins senken. Wie viele Elektronen dann hinüberkommen, bestimmt ihre Energieverteilung in der Source, und die fällt mit $\exp(-E/(k_\mathrm BT))$. Die Grenze kommt also aus der Wärme, nicht aus dem Aufbau.
:::

:::aufgabe Aufgabe 8 ★★ Der kapazitive Teiler
<span class="anker" id="aufg-8"></span>

Ein Substrat hat $N_\mathrm A=3\cdot10^{16}\,\mathrm{cm^{-3}}$, im Aus-Zustand ist $\varphi_\mathrm s=0{,}6$ V.

<ol class="al">

<li>

Berechne $C'_\mathrm{depl}$ und dann $\delta\varphi_\mathrm s/\delta V_\mathrm{GS}$ und $S$ für 20, 5 und 100 nm $\mathrm{SiO_2}$.

</li>

<li>

Bei welcher Dicke ist $C'_\mathrm{IS}=C'_\mathrm{depl}$? Wie groß ist dann $S$?

</li>

<li>

Vorhersage: Wie groß ist die untere Grenze von $S$ bei 350 K und bei 400 K?

</li>

</ol>

:::loesung
(a) $L_\mathrm{depl}=161$ nm, $C'_\mathrm{depl}=64{,}4\,\mathrm{nF/cm^2}$. Bei 20 nm: 0,728 und 81,7 mV/Dekade. Bei 5 nm: $C'_\mathrm{IS}=690{,}6\,\mathrm{nF/cm^2}$, 0,915 und 65,1 mV/Dekade. Bei 100 nm: $C'_\mathrm{IS}=34{,}5\,\mathrm{nF/cm^2}$, 0,349 und 170,6 mV/Dekade. (b) $d_\mathrm{IS}=\varepsilon_\mathrm{IS}/C'_\mathrm{depl}=54$ nm, $S=2\cdot59{,}5=119$ mV/Dekade. (c) Die Grenze ist $\propto T$: 69,4 und 79,4 mV/Dekade.
:::
:::

:::aufgabe Aufgabe 9 ★★ Wie tief muss die Schwelle liegen?
<span class="anker" id="aufg-9"></span>

Ein Transistor hat $V_\mathrm{th}=0{,}4$ V, $S=90$ mV/Dekade und bei $V_\mathrm{GS}=V_\mathrm{th}$ den Strom 1 µ A.

<ol class="al">

<li>

Wie groß ist der Strom bei $V_\mathrm{GS}=0$?

</li>

<li>

Welches $V_\mathrm{th}$ braucht man für 1 pA bei $V_\mathrm{GS}=0$? Und welches bei $S=60$ mV/Dekade?

</li>

<li>

Um welchen Faktor steigt der Strom bei $V_\mathrm{GS}=0$, wenn $V_\mathrm{th}$ um 100 mV sinkt?

</li>

</ol>

:::loesung
(a) $0{,}4\,\mathrm{V}/(90\,\mathrm{mV/Dekade})=4{,}44$ Dekaden, also $1\,\mathrm{\mu A}\cdot10^{-4{,}44}=36$ pA. (b) Von 1 µ A bis 1 pA sind sechs Dekaden, also $V_\mathrm{th}=0{,}54$ V. Mit $S=60$ mV/Dekade reichen 0,36 V. (c) $10^{100/90}=12{,}9$.
:::
:::
