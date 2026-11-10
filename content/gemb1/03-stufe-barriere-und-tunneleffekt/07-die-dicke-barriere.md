---
title: Stufe 5: Die dicke Barriere
pfad: Elektrotechnik / 4. Semester / GEMB1 – Grundlagen elektronischer Materialien und Bauelemente 1 / Stufe, Barriere und Tunneleffekt
adresse: elektrotechnik/4-semester/elektronische-materialien-und-bauelemente-1/stufe-barriere-und-tunneleffekt
knoten: Kapitel 3: Stufe, Barriere und Tunneleffekt
order: 4130700
summary: Formel (4.3) ist exakt, aber unhandlich.
tags: Gateoxid, Rastertunnelmikroskop, Resonanzen, Totalreflexion, verhinderte Totalreflexion
lang: de
---

<span class="anker" id="stufe-5"></span>

:::zweck
Formel [(4.3)](tunneln-durch-eine-dunne-wand.html#gl-4-3) ist exakt, aber unhandlich. Diese Stufe findet eine kurze Näherung, die zeigt, warum Tunnelströme so empfindlich auf die Dicke reagieren, und klärt, was bei Energien über der Barriere geschieht.
:::

**Die Idee.** Die Amplitude fällt auf dem Weg durch die Barriere um $\mathrm{e}^{-\kappa L}$. $T$ zählt das Quadrat, also $\mathrm{e}^{-2\kappa L}$. Alles andere ändert sich langsam. Für dicke Barrieren bleibt deshalb ein fester Vorfaktor mal eine Exponentialfunktion.

:::satz Satz 5.1 (Näherung für die dicke Barriere)
<span class="anker" id="satz-5-1"></span>

Für $\kappa L\gg1$ gilt

<span class="anker" id="gl-5-1"></span>
$$T(L,E)\approx16\,\frac{E}{V_0}\Bigl(1-\frac{E}{V_0}\Bigr)\exp\Bigl(-2\sqrt{\frac{2m}{\hbar^2}(V_0-E)}\;L\Bigr)=16\,\frac{E}{V_0}\Bigl(1-\frac{E}{V_0}\Bigr)\mathrm{e}^{-2\kappa L}. \tag{5.1}$$
:::

⁠**So liest man das:** Der Vorfaktor liegt zwischen 0 und 4 und hat sein Maximum bei $E=V_0/2$. Der Exponent entscheidet. Er enthält $L$ linear und $V_0-E$ unter der Wurzel. Auf logarithmischer Achse ist $T(L)$ deshalb eine Gerade (Abb. [5](#abb-5) links). **Gültigkeit:** Ab $\kappa L\approx2$ ist die Abweichung unter 4 %.

:::herleitung Von [(4.3)](tunneln-durch-eine-dunne-wand.html#gl-4-3) zu [(5.1)](#gl-5-1)
Für $\kappa L\gg1$ ist $\sinh(\kappa L)\approx\frac12\mathrm{e}^{\kappa L}$, der Fehler ist von der Größe $\mathrm{e}^{-2\kappa L}$. Damit ist der Nenner in [(4.3)](tunneln-durch-eine-dunne-wand.html#gl-4-3) viel größer als 1, die 1 entfällt, und es bleibt $T\approx4\frac E{V_0}(1-\frac E{V_0})\cdot4\mathrm{e}^{-2\kappa L}$.
:::

:::abbildung gemb1/k3tunnelT 5
Barriere mit $V_0=2$ eV. Links: $T$ über der Breite, exakt nach [(4.3)](tunneln-durch-eine-dunne-wand.html#gl-4-3), logarithmisch. Rechts: $T$ über der Energie für $L=1$ nm, auch oberhalb der Barriere. Grau: $E<V_0$. Punkte: $T=1$ an den Resonanzen.
:::

::::beispiel
Für $E=0{,}5$ eV und $L=1$ nm ist der Vorfaktor 3 und $\mathrm{e}^{-12{,}55}=3{,}55\cdot10^{-6}$, also $T=1{,}06\cdot10^{-5}$ wie exakt. Die Dicke wiegt schwer:

| $T$ bei $V_0=2$ eV | $L=0{,}5$ nm | $L=1$ nm | $L=2$ nm | $L=3$ nm |
|---|---|---|---|---|
| $E=0{,}5$ eV | $5{,}6\cdot10^{-3}$ | $1{,}1\cdot10^{-5}$ | $3{,}8\cdot10^{-11}$ | $1{,}3\cdot10^{-16}$ |
| $E=1{,}5$ eV | $7{,}8\cdot10^{-2}$ | $2{,}1\cdot10^{-3}$ | $1{,}5\cdot10^{-6}$ | $1{,}1\cdot10^{-9}$ |
::::

⁠**Grenzfälle:** Für $E\to0$ geht $T\to0$: Die lange einlaufende Welle hat an der Kante fast einen Knoten, sie wird fast ganz reflektiert. Je 0,1 nm mehr Dicke sinkt $T$ um den Faktor $\mathrm{e}^{2\kappa\cdot0{,}1\,\mathrm{nm}}$, bei $V_0-E=3$ eV also um 5,9.

**Wo das zählt.** Im Feldeffekttransistor trennt das __Gateoxid__, eine dünne Isolierschicht, die Steuerelektrode vom Stromkanal. Mit $V_0-E=3$ eV wächst $T$ beim Dünnen von 1,5 nm auf 1,0 nm um den Faktor 7100. Dieser Leckstrom begrenzt, wie dünn die Schicht werden darf. Das __Rastertunnelmikroskop__ nutzt dieselbe Empfindlichkeit: Zwischen einer Metallspitze und einer Oberfläche im Abstand von etwa 1 nm tunneln Elektronen durch das Vakuum. Bei einer 4,5 eV hohen Barriere ändern 0,1 nm den Strom um den Faktor 8,8, und einzelne Atome werden sichtbar. Gezielt genutzt wird das Tunneln in Tunneldioden, resonanten Tunneldioden und Tunnel-Transistoren.

**Energien über der Barriere.** Für $E>V_0$ ist $k_\mathrm{II}=\sqrt{2m(E-V_0)}/\hbar$ reell. Dieselbe Rechnung mit $k_\mathrm{II}$ statt $\kappa$ macht aus $\sinh$ den $\sin$, und das Vorzeichen im Nenner dreht sich:

<span class="anker" id="gl-5-2"></span>
$$T=\Bigl[1+\frac{\sin^2(k_\mathrm{II}L)}{4\frac{E}{V_0}\bigl(\frac{E}{V_0}-1\bigr)}\Bigr]^{-1}\qquad(E>V_0). \tag{5.2}$$

Beide Kanten reflektieren, und die Teilwellen überlagern sich. Für $k_\mathrm{II}L=n\pi$ löschen sie sich aus, und es ist $T=1$. Diese Stellen heißen __Resonanzen__: Über der Barriere passt dann eine ganze Zahl halber Wellenlängen in die Breite $L$, wie in der Box aus [Kapitel 2](/wissen/elektrotechnik/4-semester/elektronische-materialien-und-bauelemente-1/das-teilchen-in-der-box/das-teilchen-in-der-box.html). Für $L=1$ nm liegen sie bei $E=2{,}38$ eV, 3,50 eV und 5,38 eV (Abb. [5](#abb-5) rechts). Bei $E=2{,}09$ eV ist $T$ nur 0,16, obwohl das Elektron über die Barriere passt. Für $E\to V_0$ gehen [(4.3)](tunneln-durch-eine-dunne-wand.html#gl-4-3) und [(5.2)](#gl-5-2) stetig ineinander über. Für $V_0\to0$ wird $T=1$.

:::frage Warum steht im Exponenten $2\kappa L$ und nicht $\kappa L$?
Die Amplitude fällt mit $\mathrm{e}^{-\kappa L}$. $T$ ist aber ein Verhältnis von Betragsquadraten, und das Quadrat verdoppelt den Exponenten.
:::

:::analogie
Licht, das im Glas flach auf die Grenzfläche zur Luft trifft, wird vollständig reflektiert. Das ist die __Totalreflexion__. Hinter der Grenzfläche ist das Feld nicht sofort null: Es klingt als evaneszente Welle ab und trägt im Mittel keine Energie fort (Abb. [6](#abb-6) links). Bringt man ein zweites Prisma bis auf einen Abstand von etwa einer Lichtwellenlänge heran, koppelt ein Teil des Lichts hinüber. Das ist die __verhinderte Totalreflexion__: Der Luftspalt wirkt wie die Barriere. In der Optoelektronik koppelt man so Wellen in Wellenleiter ein und aus. Das Bild stimmt für die Form der Welle, nicht für die Zahlen: Licht hat keine Masse, und ob es abklingt, entscheidet der Einfallswinkel, nicht eine Energiedifferenz $V_0-E$.
:::

:::abbildung gemb1/k3prisma 6
Links: Totalreflexion an der schrägen Fläche eines Prismas. Dahinter klingt die Welle ab. Rechts: Ein zweites Prisma im kleinen Abstand fängt die abklingende Welle auf, ein Teil des Lichts läuft geradeaus weiter.
:::

:::aufgabe Aufgabe 9 ★★ Vier Tunnelwahrscheinlichkeiten
<span class="anker" id="aufg-9"></span>

Eine Barriere hat $V_0=2{,}5$ eV. Rechne in eV und nm.

<ol class="al">

<li>

Berechne mit [(5.1)](#gl-5-1) $T$ für $E=1$ eV und $E=2$ eV, jeweils bei $L=0{,}6$ nm und $L=3$ nm.

</li>

<li>

Wie groß sind die Wellenlängen der einlaufenden Elektronen?

</li>

<li>

Halbiere $L=0{,}6$ nm bei $E=2$ eV. Vergleiche die Näherung mit [(4.3)](tunneln-durch-eine-dunne-wand.html#gl-4-3). Warum weicht sie jetzt merklich ab?

</li>

</ol>

:::loesung
(a) Bei $E=1$ eV ist der Vorfaktor $16\cdot0{,}4\cdot0{,}6=3{,}84$ und $\kappa=6{,}27\,\mathrm{nm^{-1}}$. Damit $T=3{,}84\,\mathrm{e}^{-7{,}53}=2{,}06\cdot10^{-3}$ bei 0,6 nm und $T=3{,}84\,\mathrm{e}^{-37{,}65}=1{,}71\cdot10^{-16}$ bei 3 nm. Bei $E=2$ eV ist der Vorfaktor $16\cdot0{,}8\cdot0{,}2=2{,}56$ und $\kappa=3{,}62\,\mathrm{nm^{-1}}$. Damit $T=2{,}56\,\mathrm{e}^{-4{,}35}=3{,}31\cdot10^{-2}$ und $T=2{,}56\,\mathrm{e}^{-21{,}74}=9{,}29\cdot10^{-10}$. (b) $\lambda=1{,}226\,\mathrm{nm}/\sqrt{E/\mathrm{eV}}$: 1,23 nm und 0,87 nm. (c) Bei $L=0{,}3$ nm ist $\kappa L=1{,}09$. Näherung 0,291, exakt 0,270. Die 8 % Abweichung entstehen, weil $\sinh(\kappa L)\approx\frac12\mathrm{e}^{\kappa L}$ bei so kleinem $\kappa L$ nicht mehr gilt und die 1 im Nenner zählt.
:::
:::

:::aufgabe Aufgabe 10 ★★ Dünne Schichten und Resonanzen
<span class="anker" id="aufg-10"></span>

<ol class="al">

<li>

Eine Isolierschicht hat $V_0-E=3{,}1$ eV. Um welchen Faktor steigt der Tunnelstrom, wenn sie von 2 nm auf 1,2 nm schrumpft? Der Strom ist dabei proportional zu $T$, der Vorfaktor ändert sich nicht.

</li>

<li>

Welche Dickenänderung ändert $T$ um den Faktor 10?

</li>

<li>

Eine Barriere hat $V_0=1$ eV und $L=0{,}8$ nm. Bei welchen zwei kleinsten Energien ist $T=1$? Wie groß ist $T$ bei $k_\mathrm{II}L=\pi/2$?

</li>

</ol>

:::loesung
(a) $\kappa=5{,}123\sqrt{3{,}1}\,\mathrm{nm^{-1}}=9{,}02\,\mathrm{nm^{-1}}$. Faktor $\mathrm{e}^{2\kappa\cdot0{,}8\,\mathrm{nm}}=1{,}9\cdot10^{6}$. (b) $\Delta L=\ln10/(2\kappa)=0{,}128$ nm, das sind rund zwei Drittel eines Atomabstands von 0,2 nm. (c) $k_\mathrm{II}L=n\pi$ ergibt $E=V_0+n^2\pi^2\hbar^2/(2mL^2)$. Mit $\pi^2/(26{,}25\cdot0{,}64)=0{,}587$ eV sind das 1,59 eV und 3,35 eV. Für $k_\mathrm{II}L=\pi/2$ ist $E=1{,}147$ eV und $\sin^2=1$, also $T=1/(1+1/(4\cdot1{,}147\cdot0{,}147))=0{,}40$.
:::
:::
