---
title: Stufe 8: Ergänzung: Zustandsdichten in Potentialkästen
pfad: Elektrotechnik / 4. Semester / GEMB1 – Grundlagen elektronischer Materialien und Bauelemente 1 / Das Teilchen in der Box
adresse: elektrotechnik/4-semester/elektronische-materialien-und-bauelemente-1/das-teilchen-in-der-box
knoten: Kapitel 2: Das Teilchen in der Box
order: 4121000
summary: In einem großen Stück liegen die Niveaus so dicht, dass sich einzelne nicht mehr auflösen lassen.
tags: Zustandsdichte, Born-von-Kármán-Bedingung
lang: de
---

<span class="anker" id="stufe-8"></span>

:::zweck
In einem großen Stück liegen die Niveaus so dicht, dass sich einzelne nicht mehr auflösen lassen. Diese Stufe fragt nach ihrer Dichte auf der Energieachse.
:::

**Die Idee.** Der Abstand der Niveaus ist kleiner als jede Messgenauigkeit, und nach der Unschärferelation hat ein Zustand, der nur kurz besteht, ohnehin keine scharfe Energie. Also zählt man. In der Ebene der Quantenzahlen belegt jeder Zustand ein Kästchen der Fläche 1 (Abb. [8](#abb-8)). Eine feste Energie legt dort einen Kreis um den Ursprung fest. Alle Zustände mit kleinerer Energie liegen darin, nur im ersten Quadranten, denn Quantenzahlen sind positiv. Die Zahl der Zustände ist also die Viertelkreisfläche. Im Raum wird daraus ein Achtel einer Kugel. Leitet man die Zahl nach der Energie ab, erhält man die Dichte.

:::definition Definition 8.1 (Zustandsdichte)
<span class="anker" id="satz-8-1"></span>

$Z(E)$ ist die Zahl der Quantenzustände mit einer Energie bis $E$, gemessen vom Boden der Box. Die __Zustandsdichte__ eines Materials in $d$ Dimensionen ist

<span class="anker" id="gl-8-1"></span>
$$D(E)=\frac2{L^d}\,\frac{\mathrm{d} Z}{\mathrm{d} E},\qquad d=1,2,3. \tag{8.1}$$
:::

⁠**So liest man das:** $D(E)\,\mathrm{d} E$ ist die Zahl der Plätze für Elektronen im Energiebereich $\mathrm{d} E$, je Länge, Fläche oder Volumen. Die 2 kommt aus dem Pauli-Prinzip. Das Teilen durch $L^d$ macht eine Materialeigenschaft daraus, die von der Größe des Stücks nicht abhängt. Im Material tritt $m^*$ an die Stelle von $m_0$. Die Einheit ist $1/(\mathrm{eV\,cm}^d)$. Die Formel für $d=3$ ist zentral: Elektronen, die in Metallen und Halbleitern den Strom tragen, lassen sich in erster Näherung als Teilchen in einer großen 3D-Box beschreiben.

:::satz Satz 8.2 (Zustandsdichten)
<span class="anker" id="satz-8-2"></span>

Für eine Box mit Kantenlänge $L$ und Masse $m^*$ gilt:

| $d$ | $Z(E)$ | $D(E)$ |
|---|---|---|
| 1 | $\dfrac{(8m^*)^{1/2}L}{h}\,E^{1/2}$ | $\dfrac2h\sqrt{\dfrac{2m^*}{E}}=\dfrac1{\pi\hbar}\sqrt{\dfrac{2m^*}{E}}\;\propto E^{-1/2}$ |
| [2.5ex] 2 | $\dfrac{2\pi m^*L^2}{h^2}\,E$ | $\dfrac{4\pi m^*}{h^2}=\dfrac{m^*}{\pi\hbar^2}\;\propto E^0$ |
| [2.5ex] 3 | $\dfrac{\pi(8m^*)^{3/2}L^3}{6h^3}\,E^{3/2}$ | $\dfrac{\pi(8m^*)^{3/2}}{2h^3}\sqrt E=\dfrac{2\sqrt2\cdot4\pi}{h^3}\,m^{*3/2}\sqrt E=\dfrac{m^*}{\pi^2\hbar^3}\sqrt{2m^*E}\;\propto E^{1/2}$ |
:::

:::herleitung Zählen in der Ebene der Quantenzahlen
Für die quadratische oder würfelförmige Box hängt $E$ nur vom Radius $n'$ ab, mit $n'^2=n_x^2$, $n_x^2+n_y^2$ oder $n_x^2+n_y^2+n_z^2$:

$$E=\frac{h^2}{8m^*L^2}\,n'^2\quad\Longrightarrow\quad n'=\frac{(8m^*)^{1/2}L}{h}\,E^{1/2}.$$

Die Zahl der Zustände ist in 1D die Strecke $Z=n'$, in 2D der Viertelkreis $Z=\frac14\pi n'^2$, in 3D das Kugelachtel $Z=\frac18\cdot\frac43\pi n'^3=\frac\pi6n'^3$. Einsetzen ergibt die Spalte $Z(E)$. Ohne Spin und je Box folgen

$$\frac{\mathrm{d} Z}{\mathrm{d} E}=\frac{(2m^*)^{1/2}L}{h}\,E^{-1/2},\qquad\frac{\mathrm{d} Z}{\mathrm{d} E}=\frac{2\pi m^*L^2}{h^2},\qquad\frac{\mathrm{d} Z}{\mathrm{d} E}=\frac{\pi(8m^*)^{3/2}L^3}{4h^3}\,E^{1/2}.$$

Mit dem Faktor $2/L^d$ aus [(8.1)](#gl-8-1) steht die rechte Spalte da.
:::

:::abbildung gemb1/k2dichte 8
Links: Zustände der quadratischen Box, rot die mit einer Energie unter dem Wert zum Radius $n'=6$. Rechts oben: wirkliche Niveaus leicht unsymmetrischer Boxen ohne Entartung. Rechts unten: mittlere Dichte. Nach oben werden die Niveaus in 1D dünner, in 3D dichter.
:::

⁠**Warum die Exponenten?** Der Energieabstand benachbarter Radien wächst wie $n'$. In 1D liegt je Radius ein Zustand, die Dichte fällt. In 2D wächst der Kreisring wie $n'$ mit, die Dichte bleibt. In 3D wächst die Kugelschale wie $n'^2$, die Dichte steigt. **Gültigkeit:** Die glatte Funktion $D(E)$ stimmt nur als Mittelwert über viele Niveaus, also für große Quantenzahlen.

::::beispiel
Bei $m^*=m_0$ ist in 3D $D(1\,\mathrm{eV})=6{,}8\cdot10^{21}\,\mathrm{eV^{-1}\,cm^{-3}}$, in 2D $D=4{,}2\cdot10^{14}\,\mathrm{eV^{-1}\,cm^{-2}}$, in 1D $D(0{,}1\,\mathrm{eV})=5{,}2\cdot10^{7}\,\mathrm{eV^{-1}\,cm^{-1}}$. **Kontrolle:** Für $n'=20$ gibt der Viertelkreis 314 Zustände, exaktes Zählen 294, bei $n'=50$ sind es 1963 und 1911. Der Fehler sitzt am Kreisrand und verliert an Gewicht.
::::

**Periodische Ränder.** Im Inneren eines großen Kristalls spielen die Wände keine Rolle. Bequemer ist deshalb die __Born-von-Kármán-Bedingung__ $\psi(x+L)=\psi(x)$. Sie erlaubt laufende Wellen $\psi(x)=\frac1{\sqrt L}\,\mathrm{e}^{\mathrm{j} kx}$ mit

<span class="anker" id="gl-8-2"></span>
$$k_x=n_x\frac{2\pi}{L_x},\qquad k_y=n_y\frac{2\pi}{L_y},\qquad k_z=n_z\frac{2\pi}{L_z},\qquad n_i\in\mathbb{Z}. \tag{8.2}$$

Die Werte liegen doppelt so weit auseinander wie in der Box, dafür zählen beide Vorzeichen. Je Intervall $\mathrm{d} k$ gibt es in beiden Fällen $L/\pi\cdot\mathrm{d} k$ Zustände, die Zustandsdichte bleibt dieselbe.

:::frage In 1D wird $D(E)$ bei $E\to0$ unendlich. Gibt es dort unendlich viele Zustände?
Nein. $Z(E)$ bleibt endlich, denn $\int E^{-1/2}\,\mathrm{d} E$ ist bei null endlich. Nahe dem Boden liegen die Zustände nur am dichtesten.
:::

:::aufgabe Aufgabe 11 ★★ Zustände zählen
<span class="anker" id="aufg-11"></span>

Eine Würfelbox hat $L=100$ nm, $m^*=m_0$.

<ol class="al">

<li>

Wie groß sind $n'$ und $Z$ bei $E=50$ meV?

</li>

<li>

Wie viele Plätze für Elektronen enthält 1 cm$^3$ eines Materials mit derselben Masse im Bereich von 0,500 eV bis 0,501 eV?

</li>

<li>

Vorhersage: In einem Quantenfilm trägt jedes Teilband ab seiner Unterkante einen festen Wert zur Dichte bei. Skizziere $D(E)$. Was entsteht für sehr dicke Filme?

</li>

</ol>

:::loesung
(a) $E_0=0{,}376\,\mathrm{eV\,nm^2}/(100\,\mathrm{nm})^2=3{,}76\cdot10^{-5}$ eV, also $n'=\sqrt{E/E_0}=36{,}5$ und $Z=\frac\pi6n'^3=2{,}5\cdot10^4$. (b) $D(0{,}5\,\mathrm{eV})=6{,}81\cdot10^{21}\cdot\sqrt{0{,}5}\,\mathrm{eV^{-1}\,cm^{-3}}=4{,}8\cdot10^{21}\,\mathrm{eV^{-1}\,cm^{-3}}$. Mal 1 meV ergibt $4{,}8\cdot10^{18}$ Plätze. (c) Eine Treppe: Bei jedem $E_n=n^2E_0$ steigt $D(E)$ um denselben Wert $4\pi m^*/(h^2L_z)$ je Volumen. Für dicke Filme liegen $\sqrt{E/E_0}$ Stufen unter $E$, und die Treppe folgt genau der Dichte in 3D, $\frac{2\sqrt2\cdot4\pi}{h^3}m^{*3/2}\sqrt E$.
:::
:::
