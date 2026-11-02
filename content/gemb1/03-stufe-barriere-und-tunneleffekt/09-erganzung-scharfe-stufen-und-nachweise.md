---
title: Stufe 7: Ergänzung: Scharfe Stufen und Nachweise
pfad: Elektrotechnik / 4. Semester / Elektronische Materialien und Bauelemente 1 / Stufe, Barriere und Tunneleffekt
order: 4130900
summary: Die Rechnung sagt für E>V 0 Reflexion voraus.
tags: Schottky-Kontakt, Feldemission, Glühemission
lang: de
---

<span class="anker" id="stufe-7"></span>

:::zweck
Die Rechnung sagt für $E>V_0$ Reflexion voraus. Bei einem Ball beobachtet man sie nie. Diese Ergänzung klärt, wann eine Kante scharf genug ist, und nennt Effekte, die nur der Tunneleffekt erklärt.
:::

**Die Idee.** Bisher sprang $V$ an einem Punkt. Echte Kanten steigen über eine Strecke $d$ an. Für die Welle zählt, wie $d$ zur Wellenlänge steht. Ist $d$ klein gegen $\lambda$, merkt die Welle den Anstieg als Sprung. Ist $d$ viel größer, passt sich die Welle Stück für Stück an, und eine reflektierte Welle baut sich nicht auf, denn die Beiträge der einzelnen Stücke heben sich weg (Abb. [8](#abb-8)).

:::abbildung gemb1/k3rampe 8
Links: scharfe Stufe (gestrichelt) und Stufe mit einem Anstieg über die Breite $d=1$ nm (blau), bei $E=3$ eV und $V_0=2$ eV. Rechts: Reflexionskoeffizient über $d$, logarithmisch. Schon bei $d=0{,}4$ nm ist $R=1{,}3\cdot10^{-3}$, bei $d=1$ nm nur noch $10^{-7}$.
:::

:::zusatz Stufe mit stetigem Anstieg
Für $V(x)=V_0/(1+\mathrm{e}^{-4x/d})$ lässt sich die Schrödinger-Gleichung exakt lösen. Es ist

$$R=\biggl[\frac{\sinh\bigl(\frac\pi4d(k_\mathrm I-k_\mathrm{II})\bigr)}{\sinh\bigl(\frac\pi4d(k_\mathrm I+k_\mathrm{II})\bigr)}\biggr]^2\approx\mathrm{e}^{-\pi k_\mathrm{II}d}=\mathrm{e}^{-2\pi^2d/\lambda_\mathrm{II}}\quad\text{für }k_\mathrm{II}\,d\gg1.$$

$d\to0$ ergibt [(2.3)](reflexion-trotz-genugender-energie.html#gl-2-3). Maßgeblich ist die größere Wellenlänge $\lambda_\mathrm{II}$ oberhalb der Kante.
:::

**Elektron an einem Metall-Halbleiter-Kontakt.** In Atom- und Kernphysik beobachtet man $T<1$ knapp über $V_0$, wenn die Wellenlänge groß gegen den Anstieg ist. An einem sperrenden Kontakt zwischen Metall und Halbleiter (__Schottky-Kontakt__) steigt die Energie um rund $V_0=0{,}8$ eV, bei sehr starker Dotierung über nur $d\approx4{,}5$ nm. Links ist $\lambda=1{,}37$ nm, knapp über der Kante wird die Wellenlänge rechts viel größer: Bei $E-V_0=1$ meV ist $\lambda_\mathrm{II}=39$ nm und $R\approx0{,}10$. Dort wird Reflexion trotz $E>V_0$ tatsächlich beobachtet. Bei 20 meV ist $R$ schon $4\cdot10^{-5}$, die scharfe Stufe ergäbe 0,53.

**Ball am Hügel.** Ein Fußball mit 0,4 kg und 10 m/s schafft einen Hügel von 5,1 m Höhe. Seine Wellenlänge ist $h/(mv)=1{,}7\cdot10^{-34}$ m. Für $d=1$ m ist $d/\lambda\approx10^{34}$, und $R$ ist von null nicht zu unterscheiden. Kein Hang lässt sich auf die Wellenlänge begrenzen. Auch das Tunneln bleibt Mikrosystemen vorbehalten: Es verlangt eine Barriere, die nicht viel dicker als $\delta$ ist.

**Nachweise des Tunneleffekts.** Mehrere Effekte in Kernphysik, Festkörperphysik und Optik versteht man nur mit dem Tunneln.

<ul>

<li>

__Feldemission__: Aus kaltem Metall treten bei kleiner Feldstärke kaum Elektronen aus, ihre Energie liegt rund $V_0-E=4{,}5$ eV unter der des Vakuums. Beim Heizen erreichen genügend viele $E\ge V_0$, das ist die __Glühemission__. Sehr hohe Feldstärken, etwa an einer Metallspitze, verbiegen das Potential außen zu $V(x)=V_0-e\mathcal Ex$. Es entsteht eine dreieckige Barriere der Breite $L=(V_0-E)/(e\mathcal E)$. Bei $\mathcal E=5\cdot10^{9}$ V/m ist $L=0{,}9$ nm, und ein großer Strom tunnelt. Bei $10^{6}$ V/m wäre $L=4{,}5$ µ m.

</li>

<li>

⁠**Schottky-Kontakte:** Auf hochdotierten Halbleitern ($n>10^{17}\,\mathrm{cm^{-3}}$ freie Elektronen) ist die Barriere so dünn, dass der Strom durch Tunneln fließt. Viele ohmsche Kontakte sind in Wirklichkeit Tunnelkontakte. Wie viele Elektronen eine bestimmte Energie haben, hängt von der Temperatur ab, also verrät die Temperaturabhängigkeit des Stroms den Transportweg.

</li>

<li>

⁠**Tunneldioden:** Der Strom besteht aus Elektronen, die von den fast voll besetzten Zuständen der p-Seite (Valenzband) in die Zustände der n-Seite (Leitungsband) tunneln.

</li>

</ul>

:::frage Warum rechnet man dann überhaupt mit scharfen Kanten?
Weil sie für Elektronen an dünnen Schichten gut passen: Eine Grenzfläche zwischen zwei Stoffen ist nur wenige Atomlagen breit, also ist $d$ nicht größer als $\lambda$.
:::

:::aufgabe Aufgabe 12 ★ Ball und Elektron
<span class="anker" id="aufg-12"></span>

<ol class="al">

<li>

Vergleiche $\lambda$ eines Elektrons mit $E=2$ eV mit einer 0,5 nm breiten Grenzfläche, und $\lambda$ des Fußballs mit $d=1$ m. Wo gilt die Rechnung mit der scharfen Kante?

</li>

<li>

Der Fußball steht vor einer 10 cm dicken Wand, die seine Energie um $V_0-E=1$ J übersteigt. Wie groß ist der Exponent $2\kappa L$? Was folgt für $T$?

</li>

</ol>

:::loesung
(a) Elektron: $\lambda=0{,}87$ nm, größer als die Grenzfläche, die Kante wirkt scharf. Fußball: $\lambda=1{,}7\cdot10^{-34}$ m, also $d/\lambda\approx6\cdot10^{33}$. Hier gilt die klassische Rechnung. (b) $\kappa=\sqrt{2\cdot0{,}4\,\mathrm{kg}\cdot1\,\mathrm{J}}/\hbar=8{,}5\cdot10^{33}\,\mathrm{m^{-1}}$. Dann ist $2\kappa L=1{,}7\cdot10^{33}$, also $T\approx\mathrm{e}^{-1{,}7\cdot10^{33}}$, praktisch null.
:::
:::
