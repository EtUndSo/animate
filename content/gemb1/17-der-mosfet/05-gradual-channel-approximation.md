---
title: Stufe 3: Gradual Channel Approximation
pfad: Elektrotechnik / 4. Semester / Elektronische Materialien und Bauelemente 1 / Der MOSFET
order: 4270500
summary: Stufe 2 erklärt, warum Strom fließt.
tags: Kanalpotential, Entwurfsparameter, Gatekapazität
lang: de
---

<span class="anker" id="stufe-3"></span>

:::zweck
Stufe [2](die-barriere-im-kanal.html#stufe-2) erklärt, warum Strom fließt. Diese Stufe rechnet ihn aus, solange die Inversionsschicht von der Source bis zum Drain reicht.
:::

**Die Idee.** Man könnte über alle Zustände summieren, das ist aber unnötig. Ab $V_\mathrm{th}$ ist die Zustandsdichte so groß, dass die MOS-Kapazität ein Plattenkondensator ist. Man zerlegt deshalb den Kanal in kurze Stücke. Jedes ist ein kleiner MOS-Kondensator, der die Spannung zwischen Gate und Kanal an dieser Stelle sieht: $V_\mathrm{GS}$ an der Source, nur noch $V_\mathrm{GS}-V_\mathrm{DS}$ am Drain. Zum Drain hin sitzt also weniger Ladung im Kanal. Der Strom ist trotzdem überall gleich, denn nach der Kontinuitätsgleichung geht im stationären Kanal keine Ladung verloren. Wo die Ladung kleiner ist, muss das Feld größer sein. Englisch gradual heißt allmählich: Das Potential ändert sich längs des Kanals so langsam, dass jedes Stück für sich als Kondensator gilt.

:::satz Satz 3.1 (Drainstrom in der Gradual Channel Approximation)
<span class="anker" id="satz-3-1"></span>

Mit dem __Kanalpotential__ $V(y)$ gegen die Source, $V(0)=0$, $V(L)=V_\mathrm{DS}$, gilt

<span class="anker" id="gl-3-1"></span>
$$Q'_\mathrm{inv}(y)=-C'_\mathrm{IS}\bigl(V_\mathrm{GS}-V_\mathrm{th}-V(y)\bigr), \tag{3.1}$$

<span class="anker" id="gl-3-2"></span>
$$I_\mathrm D=K\Bigl[(V_\mathrm{GS}-V_\mathrm{th})V_\mathrm{DS}-\frac12V_\mathrm{DS}^2\Bigr],\qquad K=\mu_\mathrm nC'_\mathrm{IS}\frac WL=\frac{\mu_\mathrm n\varepsilon_\mathrm{IS}}{d_\mathrm{IS}}\cdot\frac WL=\frac{\mu_\mathrm nC_\mathrm G}{L^2}. \tag{3.2}$$
:::

⁠**So liest man das:** $K$ heißt __Entwurfsparameter__ und hat die Einheit A/V$^2$, im Rechenmodell $K=0{,}863$ mA/V$^2$. $C_\mathrm G=C'_\mathrm{IS}WL$ ist die __Gatekapazität__, hier 0,43 pF. Das Verhältnis $W/L$ heißt englisch aspect ratio. Eine Fertigung legt $\mu_\mathrm n$, $\varepsilon_\mathrm{IS}$ und $d_\mathrm{IS}$ fest und meist auch $L$, entworfen wird mit $W$. **Gültigkeit:** (1) $V_\mathrm{GS}>V_\mathrm{th}$ und $V_\mathrm{DS}\le V_\mathrm{GS}-V_\mathrm{th}$, damit [(3.1)](#gl-3-1) überall positive Elektronendichte ergibt. (2) $|\mathcal E_x|\gg|\mathcal E_y|$, dann ist jedes Stück eindimensional. (3) $\mu_\mathrm n$ ist konstant. (4) $V_\mathrm{th}$ gilt an jeder Stelle des Kanals.

:::herleitung Ladung, Strom, Integration
⁠**Ladung.** Vom Oxid aus gesehen liegt an der Stelle $y$ die Spannung $V_\mathrm{GS}-V(y)$. Der Teil $V_\mathrm{th}$ davon wird gebraucht, um Austrittsarbeiten auszugleichen, ortsfeste Ladungen umzuladen und die Verarmungszone aufzubauen. Der Rest lädt die bewegliche Schicht auf, das ist [(3.1)](#gl-3-1).

⁠**Strom.** Elektronen driften mit $v=\mu_\mathrm n\,\mathrm{d} V/\mathrm{d} y$ zum Drain, also ist $j=e\,n\,\mu_\mathrm n\,\mathcal E_y$ dem Betrag nach. Integration über Weite und Tiefe gibt

$$I_\mathrm D=\int_0^W\!\mathrm{d} z\int\!\mathrm{d} x\,e\,n(x,y)\,v(y)=W\mu_\mathrm n\bigl|Q'_\mathrm{inv}(y)\bigr|\frac{\mathrm{d} V}{\mathrm{d} y}=W\mu_\mathrm nC'_\mathrm{IS}\bigl(V_\mathrm{GS}-V_\mathrm{th}-V\bigr)\frac{\mathrm{d} V}{\mathrm{d} y}.$$

⁠**Integration.** $I_\mathrm D$ hängt nicht von $y$ ab. Trennen der Variablen ergibt

$$\int_0^L\!\mathrm{d} y\,I_\mathrm D=I_\mathrm DL=W\mu_\mathrm nC'_\mathrm{IS}\int_0^{V_\mathrm{DS}}\!\mathrm{d} V\,\bigl(V_\mathrm{GS}-V_\mathrm{th}-V\bigr),$$

und das ist [(3.2)](#gl-3-2). Integriert man nur bis $y$, folgt der Verlauf des Potentials:

$$V(y)=(V_\mathrm{GS}-V_\mathrm{th})-\sqrt{(V_\mathrm{GS}-V_\mathrm{th})^2-\frac{2y}{L}\Bigl[(V_\mathrm{GS}-V_\mathrm{th})V_\mathrm{DS}-\frac12V_\mathrm{DS}^2\Bigr]}.$$
:::

:::abbildung gemb1/k17kanal 3
Rechenmodell bei $V_\mathrm{GS}=3$ V für drei Werte von $V_\mathrm{DS}$. Links: Das Potential steigt zum Drain hin immer steiler, gestrichelt eine Gerade. Rechts: Die Ladung fällt zum Drain hin. Überall ist das Produkt aus Ladung und $\mathrm{d} V/\mathrm{d} y$ gleich, denn der Strom ist überall gleich.
:::

::::beispiel
Bei $V_\mathrm{GS}=3$ V und $V_\mathrm{DS}=1$ V ist $I_\mathrm D=0{,}863\,\mathrm{mA/V^2}\cdot(2{,}677-0{,}5)\,\mathrm{V^2}=1{,}88$ mA. Die Ladung fällt von 462 auf 289 nC/cm$^2$, in der Mitte ist $V=0{,}44$ V statt 0,5 V. Bedingung (2) ist erfüllt: Im Mittel ist $\mathcal E_y=0{,}2$ MV/m, an der Oberfläche ist $\mathcal E_x=53$ MV/m, das 266-Fache. Die Elektronen laufen im Mittel mit $10^{6}$ cm/s.
::::

⁠**Grenzfall:** Für $V_\mathrm{DS}\to0$ ist $V(y)$ eine Gerade und $I_\mathrm D\approx K(V_\mathrm{GS}-V_\mathrm{th})V_\mathrm{DS}$. Das ist genau der Widerstand von 433 $\Omega$ aus Stufe [1](zwei-kontakte-am-mos-kondensator.html#stufe-1).

:::frage Stufe [2](die-barriere-im-kanal.html#stufe-2) spricht von Diffusion. Warum rechnet man hier nur mit Drift?
Der Strom ist an jeder Stelle gleich, man darf ihn also dort rechnen, wo das leicht geht. Im Kanal ist die Diffusion klein: Ihr Verhältnis zur Drift ist $V_\mathrm T/(V_\mathrm{GS}-V_\mathrm{th}-V)$, an der Source hier 1 %. Die Diffusion zählt nur auf dem kurzen Stück bis zur Spitze und liefert dort genau den Strom nach, den der Kanal abführt.
:::

:::aufgabe Aufgabe 3 ★★ Den Strom ausrechnen
<span class="anker" id="aufg-3"></span>

Gegeben sind 10 nm $\mathrm{SiO_2}$, $W=30$ µ m, $L=3$ µ m, $\mu_\mathrm n=400\,\mathrm{cm^2/(V\,s)}$, $V_\mathrm{th}=0{,}6$ V, $V_\mathrm{GS}=2$ V und $V_\mathrm{DS}=0{,}5$ V.

<ol class="al">

<li>

Berechne $C'_\mathrm{IS}$, $C_\mathrm G$ und $K$.

</li>

<li>

Berechne $I_\mathrm D$. Wie groß wäre der Fehler ohne den Term $V_\mathrm{DS}^2/2$?

</li>

<li>

Berechne $Q'_\mathrm{inv}$ an Source und Drain und $V(L/2)$. Um welchen Faktor ist $\mathrm{d} V/\mathrm{d} y$ am Drain größer als an der Source?

</li>

</ol>

:::loesung
(a) $C'_\mathrm{IS}=345{,}3\,\mathrm{nF/cm^2}$, $C_\mathrm G=0{,}31$ pF, $K=400\,\mathrm{cm^2/(V\,s)}\cdot345{,}3\,\mathrm{nF/cm^2}\cdot10=1{,}38$ mA/V$^2$. (b) $I_\mathrm D=1{,}38\,\mathrm{mA/V^2}\cdot(1{,}4\cdot0{,}5-0{,}125)\,\mathrm{V^2}=0{,}79$ mA. Ohne den Term wären es 0,97 mA, 21,7 % zu viel. (c) $Q'_\mathrm{inv}(0)=-483\,\mathrm{nC/cm^2}$, $Q'_\mathrm{inv}(L)=-311\,\mathrm{nC/cm^2}$. $V(L/2)=1{,}4\,\mathrm{V}-\sqrt{1{,}96-0{,}575}\,\mathrm{V}=0{,}223$ V. Weil $|Q'_\mathrm{inv}|\,\mathrm{d} V/\mathrm{d} y$ konstant ist, ist $\mathrm{d} V/\mathrm{d} y$ am Drain um $483/311=1{,}55$ größer.
:::
:::
