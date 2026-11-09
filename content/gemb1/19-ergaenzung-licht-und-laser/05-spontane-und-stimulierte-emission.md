---
title: Stufe 3: Spontane und stimulierte Emission
pfad: Elektrotechnik / 4. Semester / Elektronische Materialien und Bauelemente 1 / Ergänzung: Licht und Laser
order: 4290500
summary: Ein angeregtes Elektron fällt zurück, aber wann und wodurch?
tags: kohärent, Photonenstromdichte, metastabil, Wirkungsquerschnitt
lang: de
---

<span class="anker" id="stufe-3"></span>

:::zweck
Ein angeregtes Elektron fällt zurück, aber wann und wodurch? Diese Stufe unterscheidet zwei Wege nach unten. Der eine erzeugt Licht in alle Richtungen, der andere kopiert ein vorhandenes Photon.
:::

**Die Idee.** Ohne weitere Anregung fällt ein Elektron von $E_2$ nach $E_1$ zurück, im Mittel nach der Lebensdauer $\tau_{21}$ und zu einem zufälligen Zeitpunkt. Das Photon fliegt in eine zufällige Richtung. Das ist die spontane Emission, die Ursache der Fluoreszenz. Kommt vorher ein passendes Photon vorbei, kann es den Sprung auslösen. Sein Feld schwingt im Takt $\omega_{21}$ und treibt die schwingende Ladung aus Stufe [1](absorption-und-emission.html#stufe-1), und die Ladung strahlt im Gleichtakt mit dem Feld. Das Photon wird nicht absorbiert, es fliegt weiter. Dazu kommt ein zweites, das in Energie, Richtung und Phase mit ihm übereinstimmt. Das ist die stimulierte Emission (Abb. [3](#abb-3)). Licht, dessen Wellen so im Gleichtakt laufen, heißt __kohärent__.

:::abbildung gemb1/k19drei 3
Die drei Vorgänge zwischen $E_1$ und $E_2$. Gefüllter Kreis: Elektron vorher, offener Kreis: Elektron nachher. Bei der stimulierten Emission laufen beide Photonen im Gleichtakt in dieselbe Richtung, bei der spontanen Emission ist die Richtung zufällig.
:::

:::definition Definition 3.1 (Drei Vorgänge)
<span class="anker" id="satz-3-1"></span>

Für $\hbar\omega=\hbar\omega_{21}$ gilt, mit $r_\mathrm{st}$ als Zahl der ausgelösten Sprünge je Elektron und Sekunde:

| Vorgang | Voraussetzung | Photonen | Rate je Elektron |
|---|---|---|---|
| Absorption | $E_1$ besetzt, $E_2$ frei, Photon da | $1\to0$ | $r_\mathrm{st}$ |
| spontane Emission | $E_2$ besetzt, $E_1$ frei | $0\to1$ | $1/\tau_{21}$ |
| stimulierte Emission | $E_2$ besetzt, $E_1$ frei, Photon da | $1\to2$ | $r_\mathrm{st}$ |
:::

:::satz Satz 3.2 (Lebensdauer und stimulierte Rate)
<span class="anker" id="satz-3-2"></span>

Sitzen $N_2$ Elektronen je Volumen auf $E_2$, gilt ohne passendes Licht

<span class="anker" id="gl-3-1"></span>
$$\frac{\mathrm{d} N_2}{\mathrm{d} t}=-\frac{N_2}{\tau_{21}},\qquad N_2(t)=N_2(0)\,\mathrm{e}^{-t/\tau_{21}}. \tag{3.1}$$

Licht mit der __Photonenstromdichte__ $j_\mathrm{Ph}$ (Photonen je Fläche und Zeit) löst je Elektron nach oben wie nach unten die Rate

<span class="anker" id="gl-3-2"></span>
$$r_\mathrm{st}=A_\mathrm{Ph}\,j_\mathrm{Ph} \tag{3.2}$$

aus.
:::

⁠**So liest man das:** Jedes Elektron fällt mit derselben Wahrscheinlichkeit je Zeit (wie in [Teil 13](/wissen/elektrotechnik/4-semester/elektronische-materialien-und-bauelemente-1/diffusion-rekombination-und-grundgleichungen/diffusion-rekombination-grundgleichungen.html)). Der strahlungslose Weg zählt in $\tau_{21}$ mit. Erlaubte Übergänge dauern Nanosekunden, in GaAs rund $10^{-8}$ s ([Teil 13](/wissen/elektrotechnik/4-semester/elektronische-materialien-und-bauelemente-1/diffusion-rekombination-und-grundgleichungen/diffusion-rekombination-grundgleichungen.html)). Verbietet der Drehimpuls den Sprung, sind es Millisekunden, und das Niveau heißt __metastabil__. $A_\mathrm{Ph}$ ist der __Wirkungsquerschnitt__: die Trefffläche, die ein Elektron dem Photon bietet. Je Sekunde treffen es alle Photonen, die durch diese Fläche fliegen. Die Rate ist für beide Richtungen gleich, denn beide sind dieselbe Kopplung an dasselbe Feld. **Gültigkeit:** Beide Niveaus müssen gleich entartet sein ([Teil 2](/wissen/elektrotechnik/4-semester/elektronische-materialien-und-bauelemente-1/das-teilchen-in-der-box/das-teilchen-in-der-box.html)).

::::beispiel
Bei $N_2(0)=5\cdot10^{18}\,\mathrm{cm^{-3}}$ entstehen anfangs $N_2/\tau_{21}=5\cdot10^{21}$ Photonen je cm$^3$ und Sekunde, das sind 1440 W/cm$^3$. Nach 1 ms sind 36,8 % übrig, nach 4,6 ms noch 1 %. Stimulierte und spontane Emission sind gleich schnell bei $r_\mathrm{st}\tau_{21}=1$, also $j_\mathrm{Ph}=1/(A_\mathrm{Ph}\tau_{21})=3{,}3\cdot10^{22}\,\mathrm{cm^{-2}\,s^{-1}}$. Das ist die Intensität $\hbar\omega_{21}\,j_\mathrm{Ph}=9{,}6$ kW/cm$^2$, rund $10^{5}$-mal mehr als Sonnenlicht aller Farben. Deshalb sieht man stimulierte Emission im Alltag nicht.
::::

⁠**Grenzfall:** Für $j_\mathrm{Ph}\to0$ bleibt nur [(3.1)](#gl-3-1), und für $t\to\infty$ ist das Gleichgewicht erreicht.

:::frage Ein stationärer Zustand ändert sich nie. Warum fällt das Elektron trotzdem von selbst?
Stationär ist $E_2$ nur für das Elektron allein. Tatsächlich hängt es am elektromagnetischen Feld, und dieses Feld ruht auch ohne Photon nie ganz. Diese Kopplung gibt dem Niveau eine endliche Lebensdauer. Der Zeitpunkt ist zufällig, die Ursache nicht.
:::

:::aufgabe Aufgabe 4 ★★ Warten und zählen
<span class="anker" id="aufg-4"></span>

Ein Stoff hat $\tau_{21}=2$ ms, $E_2-E_1=1{,}60$ eV, $A_\mathrm{Ph}=2\cdot10^{-20}\,\mathrm{cm^2}$ und anfangs $N_2=4\cdot10^{18}\,\mathrm{cm^{-3}}$.

<ol class="al">

<li>

Nach welcher Zeit sind noch 10 % oben? Welche Energie je cm$^3$ wird insgesamt frei?

</li>

<li>

Ein passender Laserstrahl trägt $3{,}3\cdot10^{15}$ Photonen je Sekunde durch 1 mm$^2$. Wie groß ist $r_\mathrm{st}\tau_{21}$? Auf welche Fläche müsste man ihn bündeln, damit beide Emissionen gleich schnell sind?

</li>

</ol>

:::loesung
(a) $t=\tau_{21}\ln10=4{,}6$ ms. Frei werden $4\cdot10^{18}\,\mathrm{cm^{-3}}\cdot1{,}60\,\mathrm{eV}=1{,}03$ J/cm$^3$. (b) $j_\mathrm{Ph}=3{,}3\cdot10^{17}\,\mathrm{cm^{-2}\,s^{-1}}$, also $r_\mathrm{st}=6{,}5\cdot10^{-3}\,\mathrm{s^{-1}}$ und $r_\mathrm{st}\tau_{21}=1{,}3\cdot10^{-5}$. Gleichstand verlangt eine $7{,}6\cdot10^{4}$-mal kleinere Fläche, also $1{,}3\cdot10^{-7}\,\mathrm{cm^2}=13$ µ m$^2$.
:::
:::
