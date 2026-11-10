---
title: Stufe 8: Ergänzung: Elektronegativität und Valenz
pfad: Elektrotechnik / 4. Semester / GEMB1 – Grundlagen elektronischer Materialien und Bauelemente 1 / Atome und Orbitale
adresse: elektrotechnik/4-semester/elektronische-materialien-und-bauelemente-1/atome-und-orbitale
knoten: Kapitel 4: Atome und Orbitale
order: 4141000
summary: Das Periodensystem ordnet, es misst nicht.
tags: Kation, Elektronenaffinität, Anion, Elektronegativität, Valenz
lang: de
---

<span class="anker" id="stufe-8"></span>

:::zweck
Das Periodensystem ordnet, es misst nicht. Diese Stufe misst, wie fest ein Atom seine Elektronen hält, und zählt Ladungen in Verbindungen.
:::

**Die Idee.** Wie fest ein äußeres Elektron sitzt, entscheiden $n$ und $Z_\mathrm{eff}$. Innerhalb einer Periode bleibt $n$ gleich, und $Z$ wächst. Elektronen derselben Schale schirmen sich kaum ab, also sitzt das Elektron fester. Am Ende der Periode, beim Edelgas, ist die Ionisierungsenergie am größten. Im nächsten Element beginnt eine neue Schale, und sie bricht ein (Abb. [8](#abb-8)). Innerhalb einer Gruppe wächst nach unten $n$, und das Elektron sitzt lockerer.

:::abbildung gemb1/k4ionisierung 8
Energie, die das äußerste Elektron aus dem freien Atom löst, für $Z=1$ bis 36. Rot: Edelgase. Blau: Alkalimetalle. Die gestrichelten Linien trennen die Perioden.
:::

:::definition Definition 8.1 (Drei Energien eines Atoms)
<span class="anker" id="satz-8-1"></span>

Die Ionisierungsenergie $\Delta E_\mathrm{IE}>0$ ist der Aufwand für $\mathrm A\to\mathrm A^++\mathrm e^-$. Das positive Ion heißt __Kation__. Die __Elektronenaffinität__ $\Delta E_\mathrm{EA}$ ist die Energieänderung bei $\mathrm B+\mathrm e^-\to\mathrm B^-$. Das negative Ion heißt __Anion__. Ist $\Delta E_\mathrm{EA}<0$, wird Energie frei. Die __Elektronegativität__ ist das Mittel

<span class="anker" id="gl-8-1"></span>
$$\mathrm{EN}=\tfrac12\bigl(\Delta E_\mathrm{IE}-\Delta E_\mathrm{EA}\bigr). \tag{8.1}$$
:::

⁠**So liest man das:** EN mittelt den Aufwand für das Abgeben und den Gewinn beim Aufnehmen eines Elektrons. Sie misst, wie stark ein Atom in einem Molekül Elektronen an sich zieht. $\Delta E_\mathrm{IE}$ reicht von 3,9 eV (Cäsium) bis 24,6 eV (Helium), $\Delta E_\mathrm{EA}$ bis $-3{,}6$ eV (Chlor). Links unten im Periodensystem stehen Metalle, rechts oben Isolatoren, dazwischen Halbleiter. Wasserstoff wird erst unter extrem hohem Druck metallisch. **Gültigkeit:** Die Werte gelten für freie Atome und lassen sich nicht direkt auf Moleküle oder Festkörper übertragen.

:::definition Definition 8.2 (Valenz)
<span class="anker" id="satz-8-2"></span>

Die __Valenz__ (auch Oxidationszahl, Wertigkeit) ist eine ganze Zahl mit Vorzeichen: die Ladung, die ein Atom hätte, wenn man die Außenelektronen einer Verbindung nach diesem Schema verteilt:

<ol>

<li>

Freies Element: null. Einatomiges Ion: seine Ladung, in NaCl $+1$ für Na$^+$, $-1$ für Cl$^-$.

</li>

<li>

Elektronenpaar zwischen verschiedenen Atomen: Es zählt ganz für das Atom mit der größeren Elektronegativität. In H$_2$O hat O die Valenz $-2$, jedes H $+1$.

</li>

<li>

Elektronenpaar zwischen gleichen Atomen: Es zählt je zur Hälfte. In H$_2$O$_2$ mit einem Paar zwischen den O-Atomen hat jedes O die Valenz $-1$.

</li>

</ol>
:::

⁠**So liest man das:** Valenzen sind formale Ladungen, kein Messwert. Die wirkliche Elektronendichte hängt von der Elektronegativität der Partner und der Umgebung ab.

::::beispiel
Chlor hat $\Delta E_\mathrm{IE}=12{,}97$ eV und $\Delta E_\mathrm{EA}=-3{,}61$ eV, also $\mathrm{EN}=8{,}29$ eV. Natrium hat 5,14 eV und $-0{,}55$ eV, also $\mathrm{EN}=2{,}84$ eV. **Kontrollen:** Für Wasserstoff ist $\Delta E_\mathrm{IE}=13{,}6$ eV gleich $|E_1|$. Die Valenzen eines neutralen Moleküls summieren sich zu null: in H$_2$O ist $2\cdot(+1)-2=0$.
::::

:::frage Warum sinkt die Ionisierungsenergie von Stickstoff zu Sauerstoff, obwohl $Z$ wächst?
Stickstoff hat drei einfach besetzte 2p-Orbitale. Das vierte 2p-Elektron des Sauerstoffs muss sich ein Orbital teilen. Die Abstoßung hebt es an, es löst sich leichter: 13,62 eV statt 14,53 eV. Der Knick von Beryllium zu Bor (9,32 eV auf 8,30 eV) hat einen anderen Grund: Bors äußerstes Elektron sitzt im höheren 2p.
:::

:::aufgabe Aufgabe 12 ★★ Zahlen und Ladungen
<span class="anker" id="aufg-12"></span>

<ol class="al">

<li>

Silizium hat $\Delta E_\mathrm{IE}=8{,}15$ eV und $\Delta E_\mathrm{EA}=-1{,}39$ eV, Sauerstoff 13,62 eV und $-1{,}46$ eV. Berechne beide EN. Welches Atom zieht die Elektronen an sich?

</li>

<li>

Gib die Valenzen in SiO$_2$, Al$_2$O$_3$, HF, Cl$_2$ und OF$_2$ an. Fluor hat die größte EN.

</li>

<li>

Vorhersage: Ordne Na, Mg, Cl und Ar nach steigender Ionisierungsenergie.

</li>

</ol>

:::loesung
(a) $\mathrm{EN}(\mathrm{Si})=(8{,}15+1{,}39)/2\,\mathrm{eV}=4{,}77$ eV, $\mathrm{EN}(\mathrm O)=(13{,}62+1{,}46)/2\,\mathrm{eV}=7{,}54$ eV. Sauerstoff zieht die Elektronen an sich. (b) SiO$_2$: Si $+4$, O $-2$. Al$_2$O$_3$: Al $+3$, O $-2$. HF: H $+1$, F $-1$. Cl$_2$: 0. OF$_2$: F $-1$, O $+2$, denn Fluor zieht stärker als Sauerstoff. (c) Na 5,14 eV, Mg 7,65 eV, Cl 12,97 eV, Ar 15,76 eV. Innerhalb der Periode 3 wächst der Wert mit $Z$.
:::
:::
