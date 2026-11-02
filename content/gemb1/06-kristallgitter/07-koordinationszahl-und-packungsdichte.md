---
title: Stufe 5: Koordinationszahl und Packungsdichte
pfad: Elektrotechnik / 4. Semester / Elektronische Materialien und Bauelemente 1 / Kristallgitter
order: 4160700
summary: Die drei Würfel sehen ähnlich aus, füllen den Raum aber verschieden gut.
tags: 
lang: de
---

<span class="anker" id="stufe-5"></span>

:::zweck
Die drei Würfel sehen ähnlich aus, füllen den Raum aber verschieden gut. Diese Stufe zählt Atome, Nachbarn und den gefüllten Anteil und gewinnt daraus die Dichte.
:::

**Die Idee.** Die Atome werden stark vereinfacht zu harten Kugeln, die sich berühren. Wo sie sich berühren, entscheidet die kürzeste Verbindung zwischen zwei Gitterpunkten: bei SC die Würfelkante, bei BCC die Raumdiagonale, bei FCC die Flächendiagonale (Abb. [5](#abb-5)). Daraus folgt der Radius, und der Rest ist Zählen. Ist die Bindung nicht an Richtungen gebunden, senkt jeder weitere Nachbar die Energie. Deshalb ist die locker gepackte SC-Struktur relativ instabil und selten.

:::definition Definition 5.1 (Koordinationszahl und Packungsdichte)
<span class="anker" id="satz-5-1"></span>

Die Koordinationszahl ist die Zahl der nächsten, gleich weit entfernten Nachbarn eines Atoms, gemessen von Zentrum zu Zentrum. Die Packungsdichte ist der Anteil des Volumens, den die Kugeln füllen:

<span class="anker" id="gl-5-1"></span>
$$P=\frac{N\cdot\frac43\pi r_\mathrm{at}^3}{\Omega}. \tag{5.1}$$
:::

⁠**So liest man das:** $N$ ist die Zahl der Atome in der Zelle, $r_\mathrm{at}$ der Kugelradius, $\Omega$ das Zellvolumen, beim Würfel $a^3$. $P$ ist eine reine Zahl. Beim Zählen gehört ein Atom auf einer Ecke zu acht Zellen und zählt $\frac18$, auf einer Kante $\frac14$, auf einer Fläche $\frac12$, innen 1. **Gültigkeit:** $r_\mathrm{at}$ ist hier der halbe Nachbarabstand, kein Radius der Hülle, die keinen scharfen Rand hat.

:::abbildung gemb1/k6packung 5
Schnitte durch die Zellen, gezeigt sind die Kugelteile in der Zelle. Links und rechts eine Würfelfläche, in der Mitte der Schnitt durch zwei gegenüberliegende Kanten. Rot: die Linie, längs der sich die Kugeln berühren.
:::

:::satz Satz 5.2 (Packung der kubischen Gitter)
<span class="anker" id="satz-5-2"></span>

| Gitter | $N$ | Nachbarabstand | Nachbarn | $r_\mathrm{at}$ | $P$ |
|---|---|---|---|---|---|
| SC | $8\cdot\frac18=1$ | $a$ | 6 | $a/2$ | $\pi/6=52{,}4\,\%$ |
| BCC | $8\cdot\frac18+1=2$ | $\sqrt3\,a/2$ | 8 | $\sqrt3\,a/4$ | $\sqrt3\,\pi/8=68{,}0\,\%$ |
| FCC | $8\cdot\frac18+6\cdot\frac12=4$ | $a/\sqrt2$ | 12 | $\sqrt2\,a/4$ | $\sqrt2\,\pi/6=74{,}0\,\%$ |
:::

:::herleitung Packungsdichten
⁠**SC:** Die Kante ist $a=2r_\mathrm{at}$. Eine Kugel hat das Volumen $\frac43\pi(a/2)^3=\frac16\pi a^3$, also $P=\pi/6$.

⁠**BCC:** Die Raumdiagonale $\sqrt3\,a$ enthält Eckkugel, Mittelkugel und Eckkugel: $\sqrt3\,a=4r_\mathrm{at}$. Das Kugelvolumen ist $\frac{\sqrt3}{16}\pi a^3$. Zwei Atome ergeben $P=\sqrt3\,\pi/8$.

⁠**FCC:** Die Flächendiagonale $\sqrt2\,a$ enthält zwei Eckkugeln und die Flächenkugel: $\sqrt2\,a=4r_\mathrm{at}$. Das Kugelvolumen ist $\frac{1}{12\sqrt2}\pi a^3$. Vier Atome ergeben $P=\pi/(3\sqrt2)=\sqrt2\,\pi/6$.
:::

Aus der Zelle folgt auch die Dichte. $N$ Atome mit der Molmasse $M$ wiegen $N\,M/N_\mathrm{Av}$, also ist die Massendichte

<span class="anker" id="gl-5-2"></span>
$$\rho_\mathrm m=\frac{N\,M}{N_\mathrm{Av}\,\Omega}. \tag{5.2}$$

**Beispiel.** Aluminium ist FCC mit $a=0{,}4050$ nm. Der Nachbarabstand ist $a/\sqrt2=0{,}2864$ nm, also $r_\mathrm{at}=0{,}1432$ nm. Die Dichte der Atome ist $4/a^3=6{,}02\cdot10^{22}\,\mathrm{cm^{-3}}$. Mit [(5.2)](#gl-5-2) folgt $\rho_\mathrm m=2{,}698\,\mathrm{g/cm^3}$, gemessen werden 2,70 g/cm$^3$. **Grenzfälle:** In $P$ kürzt sich $a$ heraus: Alle FCC-Metalle haben dieselben 74 %, ob Gold oder Aluminium. Die zweite Schale liegt bei SC ($\sqrt2\,a$, 12 Punkte) und FCC ($a$, 6 Punkte) 41 % weiter als die erste, bei BCC ($a$, 6 Punkte) nur 15,5 %. Deshalb formen in BCC auch diese Punkte die Wigner-Seitz-Zelle mit.

:::frage Das Eckatom liegt doch vollständig da. Warum zählt nur ein Achtel?
Weil acht Würfel diese Ecke teilen und jedes Atom genau einmal in die Summe eingehen soll. Abb. [5](#abb-5) zeigt es für die Fläche: Von jeder Eckkugel liegt nur ein Viertel des Kreises in der Zelle.
:::

:::aufgabe Aufgabe 5 ★★ Wolfram
<span class="anker" id="aufg-5"></span>

Wolfram ist BCC mit $a=0{,}3165$ nm.

<ol class="al">

<li>

Berechne Nachbarabstand, $r_\mathrm{at}$ und den Abstand zur zweiten Schale.

</li>

<li>

Berechne die Atomdichte und $\rho_\mathrm m$.

</li>

<li>

Vorhersage: Um welchen Faktor wäre $\rho_\mathrm m$ größer, wenn dieselben Kugeln in FCC säßen?

</li>

</ol>

:::loesung
(a) Nachbarabstand $\sqrt3\,a/2=0{,}2741$ nm, $r_\mathrm{at}=0{,}1370$ nm, zweite Schale $a=0{,}3165$ nm, das ist das 1,155-fache. (b) $2/a^3=6{,}31\cdot10^{22}\,\mathrm{cm^{-3}}$. $\rho_\mathrm m=2\cdot183{,}84\,\mathrm{g/mol}/(6{,}022\cdot10^{23}\,\mathrm{mol^{-1}}\cdot(0{,}3165\cdot10^{-7}\,\mathrm{cm})^3)=19{,}26\,\mathrm{g/cm^3}$. (c) Gleiche Kugeln bedeuten gleiche Atommasse und gleiches Kugelvolumen, $\rho_\mathrm m$ wächst also wie $P$: $74{,}0/68{,}0=1{,}089$, das wären 20,97 g/cm$^3$.
:::
:::

:::aufgabe Aufgabe 6 ★★★ Nachbarn zählen in einer Verbindung
<span class="anker" id="aufg-6"></span>

In Rheniumtrioxid sitzen Re auf den Würfelecken und O auf den Kantenmitten.

<ol class="al">

<li>

Zähle die Atome je Sorte in der Zelle. Stimmt die Formel ReO$_3$?

</li>

<li>

Bestimme die Abstände Re-O, O-O und Re-Re in Einheiten von $a$. Wie viele nächste Nachbarn hat Re, wie viele Re-Nachbarn hat O? Prüfe mit einer Bilanz: Jede Re-O-Berührung zählt für beide Atome.

</li>

</ol>

:::loesung
(a) Re: $8\cdot\frac18=1$. O: Ein Würfel hat 12 Kanten, $12\cdot\frac14=3$. Das ergibt ReO$_3$. (b) Re-O $a/2$, O-O $a/\sqrt2=0{,}707\,a$, Re-Re $a$. Re hat 6 nächste Nachbarn (O längs der drei Achsen, je zwei). O hat 2 Re als nächste Nachbarn, links und rechts auf seiner Kante. Bilanz je Zelle: $1\cdot6=3\cdot2$.
:::
:::
