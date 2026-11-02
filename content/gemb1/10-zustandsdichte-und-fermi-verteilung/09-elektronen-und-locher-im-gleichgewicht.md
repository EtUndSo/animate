---
title: Stufe 7: Elektronen und Löcher im Gleichgewicht
pfad: Elektrotechnik / 4. Semester / Elektronische Materialien und Bauelemente 1 / Zustandsdichte und Fermi-Verteilung
order: 4200900
summary: Plätze und Besetzung sind bekannt.
tags: Massenwirkungsgesetz
lang: de
---

<span class="anker" id="stufe-7"></span>

:::zweck
Plätze und Besetzung sind bekannt. Diese Stufe setzt sie zusammen und erhält die Dichten $n$ und $p$ eines Kristalls mit Bandlücke.
:::

**Die Idee.** Im Metall liegt $E_\mathrm F$ in einem Band, im Halbleiter in der Lücke. Dort gibt es keine Zustände, aber die Ausläufer von $f$ reichen in beide Bänder. Im Leitungsband ist $f$ winzig: wenige Elektronen. Im Valenzband fehlt ein winziger Anteil: wenige Löcher. Da $D$ am Rand bei null beginnt und $f$ exponentiell fällt, hat das Produkt $D\,f$ eine schmale Spitze knapp hinter dem Rand (Abb. [7](#abb-7)). Im reinen Kristall hinterlässt jedes Elektron ein Loch, also ist $n=p$, und $E_\mathrm F$ liegt ungefähr in der Mitte der Lücke.

:::satz Satz 7.1 (Fermi-Verteilung der Löcher)
<span class="anker" id="satz-7-1"></span>

Ein Platz ist mit der Wahrscheinlichkeit $f_\mathrm h=1-f$ leer:

<span class="anker" id="gl-7-1"></span>
$$f_\mathrm h(E)=1-f(E)=\frac{\exp\bigl(\frac{E-E_\mathrm F}{k_\mathrm BT}\bigr)}{1+\exp\bigl(\frac{E-E_\mathrm F}{k_\mathrm BT}\bigr)}=\frac1{\exp\bigl(\frac{E_\mathrm F-E}{k_\mathrm BT}\bigr)+1}. \tag{7.1}$$
:::

Im letzten Schritt sind Zähler und Nenner durch die Exponentialfunktion geteilt. Die Form ist dieselbe wie [(5.2)](die-fermi-verteilung.html#gl-5-2) mit vertauschtem Vorzeichen: Für Löcher zeigt die Energieachse nach unten.

:::satz Satz 7.2 (Ladungsträgerdichten im Gleichgewicht)
<span class="anker" id="satz-7-2"></span>

Liegt $E_\mathrm F$ mindestens rund $3k_\mathrm BT$ von beiden Bandrändern entfernt, gilt

<span class="anker" id="gl-7-2"></span>
$$n=\int_{E_\mathrm C}^\infty\mathrm{d} E\,D_\mathrm C(E)\,f(E)=N_\mathrm C\exp\Bigl(-\frac{E_\mathrm C-E_\mathrm F}{k_\mathrm BT}\Bigr),\qquad N_\mathrm C=2\Bigl(\frac{2\pi m_\mathrm C^*k_\mathrm BT}{h^2}\Bigr)^{3/2}, \tag{7.2}$$

<span class="anker" id="gl-7-3"></span>
$$p=\int_{-\infty}^{E_\mathrm V}\mathrm{d} E\,D_\mathrm V(E)\,\bigl(1-f(E)\bigr)=N_\mathrm V\exp\Bigl(-\frac{E_\mathrm F-E_\mathrm V}{k_\mathrm BT}\Bigr),\qquad N_\mathrm V=2\Bigl(\frac{2\pi m_\mathrm V^*k_\mathrm BT}{h^2}\Bigr)^{3/2}. \tag{7.3}$$
:::

:::herleitung Das Integral über das Leitungsband
Im ganzen Band ist $E-E_\mathrm F\ge E_\mathrm C-E_\mathrm F\gg k_\mathrm BT$, also gilt [(6.2)](temperatur-und-boltzmann-naherung.html#gl-6-2). Man schreibt $E-E_\mathrm F=(E-E_\mathrm C)+(E_\mathrm C-E_\mathrm F)$. Der zweite Teil ist konstant und kommt vor das Integral. Mit $u=(E-E_\mathrm C)/(k_\mathrm BT)$ wird

$$n=\frac{4\pi(2m_\mathrm C^*)^{3/2}}{h^3}\,(k_\mathrm BT)^{3/2}\,\mathrm{e}^{-(E_\mathrm C-E_\mathrm F)/(k_\mathrm BT)}\int_0^\infty\sqrt u\,\mathrm{e}^{-u}\,\mathrm{d} u,\qquad\int_0^\infty\sqrt u\,\mathrm{e}^{-u}\,\mathrm{d} u=\frac{\sqrt\pi}2.$$

Das Band endet zwar oben, aber $\mathrm{e}^{-u}$ macht die Obergrenze unwichtig. Aus $4\pi\cdot\frac{\sqrt\pi}2=2\pi^{3/2}$ folgt der Vorfaktor $2(2\pi m_\mathrm C^*k_\mathrm BT/h^2)^{3/2}$. Für $p$ läuft alles gleich mit [(7.1)](#gl-7-1) und $u=(E_\mathrm V-E)/(k_\mathrm BT)$.
:::

⁠**So liest man das:** $N_\mathrm C$ und $N_\mathrm V$ sind die effektiven Zustandsdichten, Einheit 1/cm$^3$. Es ist so, als säßen alle Plätze des Bands in der Zahl $N_\mathrm C$ direkt auf dem Rand $E_\mathrm C$ und würden mit dem Boltzmann-Faktor besetzt. Das Integral ist in einer einzigen Zahl verschwunden. Anschaulich ist $N_\mathrm C=\frac{\sqrt\pi}2\,k_\mathrm BT\,D_\mathrm C(E_\mathrm C+k_\mathrm BT)$: Plätze in einem Fenster der Breite $k_\mathrm BT$. Daher $N_\mathrm C\propto T^{3/2}$: Das Fenster wird breiter, und die Dichte in ihm wächst. Für Silizium bei 300 K ist $N_\mathrm C=2{,}82\cdot10^{19}\,\mathrm{cm^{-3}}$ und $N_\mathrm V=1{,}83\cdot10^{19}\,\mathrm{cm^{-3}}$. Praktisch ist $N=2{,}51\cdot10^{19}\,\mathrm{cm^{-3}}\,(m^*/m_0)^{3/2}(T/300\,\mathrm{K})^{3/2}$.

:::abbildung gemb1/k10dichte 7
Silizium bei 300 K mit $E_\mathrm F$ in Lückenmitte. Links die Zustandsdichte, Mitte die Fermi-Verteilung und $1-f$, rechts das Produkt am Leitungsbandrand über $(E-E_\mathrm C)/(k_\mathrm BT)$, auf das Maximum bezogen: Die Fläche ist $n$, das Maximum liegt bei $E_\mathrm C+k_\mathrm BT/2$.
:::

:::satz Satz 7.3 (Massenwirkungsgesetz)
<span class="anker" id="satz-7-3"></span>

Im thermischen Gleichgewicht gilt, gleich wo $E_\mathrm F$ liegt, solange [(7.2)](#gl-7-2) und [(7.3)](#gl-7-3) gelten:

<span class="anker" id="gl-7-4"></span>
$$n\cdot p=N_\mathrm CN_\mathrm V\,\mathrm{e}^{-E_\mathrm g/(k_\mathrm BT)}. \tag{7.4}$$
:::

⁠**So liest man das:** Beim Multiplizieren addieren sich die Exponenten, und $E_\mathrm F$ fällt heraus. Das __Massenwirkungsgesetz__ heißt so, weil es dasselbe sagt wie in der Chemie. Wärme bildet Paare aus Elektron und Loch mit einer Rate, die nur von $T$ abhängt, und Paare verschwinden, wenn ein Elektron ein Loch trifft, mit einer Rate proportional $n\,p$. Rückt $E_\mathrm F$ nach oben, wächst $n$ um genau den Faktor, um den $p$ sinkt.

**Beispiel.** Silizium, $E_\mathrm F$ in Lückenmitte, also $E_\mathrm C-E_\mathrm F=0{,}56$ eV $=21{,}7\,k_\mathrm BT$. Der Rand ist mit $3{,}9\cdot10^{-10}$ besetzt, und es folgen $n=1{,}10\cdot10^{10}\,\mathrm{cm^{-3}}$ und $p=7{,}16\cdot10^{9}\,\mathrm{cm^{-3}}$. Mit $E_\mathrm C-E_\mathrm F=0{,}2$ eV wären es $n=1{,}23\cdot10^{16}\,\mathrm{cm^{-3}}$ und $p=6{,}41\cdot10^{3}\,\mathrm{cm^{-3}}$. In beiden Fällen ist $n\,p=7{,}89\cdot10^{19}\,\mathrm{cm^{-6}}$. Dass $n$ und $p$ im ersten Fall nicht gleich sind, liegt an $N_\mathrm C\ne N_\mathrm V$. **Grenzfälle:** Für $T\to0$ gehen $n$ und $p$ gegen null. Bei 400 K ist $n\,p$ um den Faktor $1{,}2\cdot10^5$ größer, nur 2,4 davon stammen aus $T^3$, der Rest aus dem Exponenten. Für $E_\mathrm C-E_\mathrm F=3k_\mathrm BT$ ist [(7.2)](#gl-7-2) um 1,7 % zu groß, für $E_\mathrm F=E_\mathrm C$ schon um 31 %. Dort muss man mit der vollen Verteilung rechnen.

:::frage Ein Band von Silizium hat rund $5\cdot10^{22}$ Plätze je cm$^3$. Warum zählen nur $3\cdot10^{19}$?
Plätze höher im Band sind um den Boltzmann-Faktor schwächer besetzt und tragen kaum bei: 89 % der Elektronen sitzen unter $E_\mathrm C+3k_\mathrm BT$. $N_\mathrm C$ ist nicht die Zahl der Plätze im Band, sondern die Zahl der thermisch erreichbaren.
:::

:::aufgabe Aufgabe 9 ★★ GaAs bei zwei Lagen von $E_\mathrm F$
<span class="anker" id="aufg-9"></span>

Für GaAs gelte $E_\mathrm g=1{,}42$ eV, $m_\mathrm C^*=0{,}067\,m_0$, $m_\mathrm V^*=0{,}47\,m_0$, $T=300$ K.

<ol class="al">

<li>

Berechne $N_\mathrm C$ und $N_\mathrm V$. Warum unterscheiden sie sich um einen Faktor 19?

</li>

<li>

$E_\mathrm F$ liege 0,75 eV unter $E_\mathrm C$. Berechne $n$, $p$ und $n\,p$. Darf man hier die Boltzmann-Näherung benutzen?

</li>

<li>

$E_\mathrm F$ steigt um 0,1 eV. Um welche Faktoren ändern sich $n$, $p$ und $n\,p$?

</li>

<li>

Um welchen Faktor wächst $N_\mathrm C$ von 300 K bis 400 K?

</li>

</ol>

:::loesung
(a) $N_\mathrm C=4{,}35\cdot10^{17}\,\mathrm{cm^{-3}}$, $N_\mathrm V=8{,}09\cdot10^{18}\,\mathrm{cm^{-3}}$. Der Faktor ist $(0{,}47/0{,}067)^{3/2}=18{,}6$: Das leichte Elektron hat ein steiles Band mit wenigen Plätzen. (b) $n=1{,}10\cdot10^5\,\mathrm{cm^{-3}}$, $p=4{,}49\cdot10^7\,\mathrm{cm^{-3}}$, $n\,p=4{,}91\cdot10^{12}\,\mathrm{cm^{-6}}$. Die Abstände sind $29\,k_\mathrm BT$ und $25{,}9\,k_\mathrm BT$, die Näherung gilt. (c) $\mathrm{e}^{0{,}1/0{,}02585}=47{,}9$: $n$ wächst um 47,9, $p$ sinkt um 47,9, $n\,p$ bleibt. (d) $(4/3)^{3/2}=1{,}54$.
:::
:::
