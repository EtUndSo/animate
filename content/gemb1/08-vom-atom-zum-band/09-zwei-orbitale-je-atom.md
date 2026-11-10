---
title: Stufe 7: Zwei Orbitale je Atom
pfad: Elektrotechnik / 4. Semester / GEMB1 – Grundlagen elektronischer Materialien und Bauelemente 1 / Vom Atom zum Band
adresse: elektrotechnik/4-semester/elektronische-materialien-und-bauelemente-1/vom-atom-zum-band
knoten: Kapitel 8: Vom Atom zum Band
order: 4180900
summary: Bisher hatte jedes Atom ein Orbital und die Kette ein Band.
tags: 
lang: de
---

<span class="anker" id="stufe-7"></span>

:::zweck
Bisher hatte jedes Atom ein Orbital und die Kette ein Band. Diese Stufe gibt jedem Atom ein s- und ein p-Orbital. Dann entstehen zwei Bänder, und die Lücke zwischen ihnen lässt sich ausrechnen.
:::

**Die Idee.** Das Punktgitter bleibt gleich, also auch die Einhüllende $\mathrm{e}^{\mathrm{j} k\ell a}$. Nur kann das Elektron am Platz $\ell$ in zwei Orbitalen sein: Aus jeder Zahl der Rechnung wird eine $2\times2$-Matrix. Neu sind die Vorzeichen, denn das p-Orbital hat eine positive und eine negative Keule. Nach [(3.3)](zwei-atome.html#gl-3-3) ist die Kopplung negativ, wenn beide Orbitale dort, wo sie sich treffen, gleiches Vorzeichen haben, sonst positiv.

**Der Ansatz.** Mit $|\ell\rangle\to c_1|\mathrm s,\ell\rangle+c_2|\mathrm p,\ell\rangle$ wird

<span class="anker" id="gl-7-1"></span>
$$|\psi_k\rangle=\frac1{\sqrt N}\sum_\ell\mathrm{e}^{\mathrm{j} k\ell a}\bigl(c_1|\mathrm s,\ell\rangle+c_2|\mathrm p,\ell\rangle\bigr). \tag{7.1}$$

Die p-Orbitale zeigen längs der Kette, alle gleich ausgerichtet: positive Keule links, negative rechts (Abb. [7](#abb-7)). Am selben Atom gilt $\langle\mathrm s|\hat H|\mathrm s\rangle=E_\mathrm s$, $\langle\mathrm p|\hat H|\mathrm p\rangle=E_\mathrm p$ und $\langle\mathrm s,\ell|\hat H|\mathrm p,\ell\rangle=0$: Das s-Orbital überdeckt beide Keulen gleich, Plus und Minus heben sich auf. $V_\mathrm{ss}$, $V_\mathrm{sp}$, $V_\mathrm{pp}$ sind Beträge.

:::abbildung gemb1/k8sp 7
Links: Kopplung zum rechten Nachbarn. Blau positiv, Rot negativ; gleiche Vorzeichen im Überlappgebiet geben ein negatives Element. Rechts: Bänder für $E_\mathrm s=-5$ eV, $E_\mathrm p=-1$ eV, $V_\mathrm{ss}=0{,}5$ eV, $V_\mathrm{pp}=0{,}75$ eV, $V_\mathrm{sp}=0{,}6$ eV, gestrichelt für $V_\mathrm{sp}=0$.
:::

Die Kopplung an den rechten und linken Nachbarn liest man ab, mit den Zeilen $\langle\mathrm s,\ell|$, $\langle\mathrm p,\ell|$ und den Spalten $|\mathrm s\rangle$, $|\mathrm p\rangle$ des Nachbarn. Links ist die Lage gespiegelt: Das s-Orbital trifft die negative Keule des linken Nachbarn.

:::satz Satz 7.1 (Zwei Bänder)
<span class="anker" id="satz-7-1"></span>

Die Regel aus Stufe [5](viele-atome.html#stufe-5) ergibt

<span class="anker" id="gl-7-2"></span>
$$\det\left|\begin{pmatrix}-V_\mathrm{ss}&-V_\mathrm{sp}\\V_\mathrm{sp}&V_\mathrm{pp}\end{pmatrix}\mathrm{e}^{\mathrm{j} ka}+\begin{pmatrix}E_\mathrm s-E&0\\0&E_\mathrm p-E\end{pmatrix}+\begin{pmatrix}-V_\mathrm{ss}&V_\mathrm{sp}\\-V_\mathrm{sp}&V_\mathrm{pp}\end{pmatrix}\mathrm{e}^{-\mathrm{j} ka}\right|\overset!=0. \tag{7.2}$$

Mit $\tilde E_\mathrm s=E_\mathrm s-2V_\mathrm{ss}\cos(ka)$ und $\tilde E_\mathrm p=E_\mathrm p+2V_\mathrm{pp}\cos(ka)$ sind die Lösungen

<span class="anker" id="gl-7-3"></span>
$$E_\pm(k)=\frac{\tilde E_\mathrm s+\tilde E_\mathrm p}2\pm\sqrt{\Bigl(\frac{\tilde E_\mathrm s-\tilde E_\mathrm p}2\Bigr)^2+4V_\mathrm{sp}^2\sin^2(ka)}. \tag{7.3}$$
:::

:::herleitung Die Determinante
Die Summe hat die Hauptdiagonale $\tilde E_\mathrm s-E$, $\tilde E_\mathrm p-E$. Daneben stehen $-V_\mathrm{sp}\mathrm{e}^{\mathrm{j} ka}+V_\mathrm{sp}\mathrm{e}^{-\mathrm{j} ka}=-2\mathrm{j} V_\mathrm{sp}\sin(ka)$ und $+2\mathrm{j} V_\mathrm{sp}\sin(ka)$. Also ist $(\tilde E_\mathrm s-E)(\tilde E_\mathrm p-E)-4V_\mathrm{sp}^2\sin^2(ka)=0$.
:::

⁠**So liest man das:** Zwei Orbitale je Atom, zwei Bänder. Für $V_\mathrm{sp}=0$ bleiben die Kosinus-Bänder $\tilde E_\mathrm s$ und $\tilde E_\mathrm p$. Das p-Band steht auf dem Kopf: Bei $k=0$ treffen sich gleich ausgerichtete p-Orbitale mit entgegengesetzten Keulen, jedes Paar ist antibindend. Bei $k=\pi/a$ kehrt jedes zweite Orbital sein Vorzeichen um, und die Paare binden. Deshalb kommen sich die Bänder am Zonenrand am nächsten. Dort und bei $k=0$ ist $\sin(ka)=0$, die Zustände sind rein s oder rein p. Dazwischen mischt $V_\mathrm{sp}$ beide Orbitale, und die Bänder stoßen sich ab. Die Bandlücke ist

<span class="anker" id="gl-7-4"></span>
$$E_\mathrm g=(E_\mathrm p-2V_\mathrm{pp})-(E_\mathrm s+2V_\mathrm{ss}). \tag{7.4}$$

⁠**Gültigkeit:** $E_\mathrm p-E_\mathrm s>2(V_\mathrm{ss}+V_\mathrm{pp})$, und die Bandkanten liegen am Zonenrand.

::::beispiel
Mit den Zahlen aus Abb. [7](#abb-7) reicht das untere Band von $-6$ bis $-4$ eV, das obere von $-2{,}5$ bis $+0{,}5$ eV, also $E_\mathrm g=1{,}5$ eV. Bei $ka=\pi/2$ ist $\tilde E_\mathrm s=-5$ eV und $\tilde E_\mathrm p=-1$ eV, und $V_\mathrm{sp}$ schiebt die Energien auf $-5{,}332$ und $-0{,}668$ eV.
::::

⁠**Grenzfall:** Ohne Kopplungen bleiben die Atomniveaus mit $E_\mathrm g=E_\mathrm p-E_\mathrm s$.

:::aufgabe Aufgabe 8 ★ Vorzeichen bestimmen
<span class="anker" id="aufg-8"></span>

Die Beträge seien $V_\mathrm{ss}$, $V_\mathrm{sp}$ und für p-Orbitale $V_{\mathrm{pp}\sigma}$ (längs der Verbindungslinie) und $V_{\mathrm{pp}\pi}$ (parallel zueinander, senkrecht dazu). Gib $\langle\text{links}|\hat H|\text{rechts}\rangle$ an:

<ol class="al">

<li>

zwei s-Orbitale,

</li>

<li>

links s, rechts p längs der Linie, die negative Keule zeigt nach links,

</li>

<li>

zwei p-Orbitale längs der Linie, die positiven Keulen zeigen aufeinander zu,

</li>

<li>

zwei p-Orbitale senkrecht zur Linie, die positiven Keulen zeigen in dieselbe Richtung,

</li>

<li>

links s, rechts p senkrecht zur Linie,

</li>

<li>

links p längs der Linie, rechts p senkrecht zur Linie.

</li>

</ol>

:::loesung
(a) $-V_\mathrm{ss}$. (b) Die negative Keule trifft das positive s-Orbital: $+V_\mathrm{sp}$. (c) Beide positiven Keulen treffen sich: $-V_{\mathrm{pp}\sigma}$. (d) Seitlich oben plus plus, unten minus minus: $-V_{\mathrm{pp}\pi}$. (e) s liegt in der Knotenebene, Plus und Minus heben sich auf: 0. (f) Ebenso: 0.
:::
:::

:::aufgabe Aufgabe 9 ★★ Zwei Atome mit s und p
<span class="anker" id="aufg-9"></span>

Die Atome A (links) und B (rechts) haben je ein s- und ein p-Orbital längs der Verbindungslinie, positive Keule links. Es gilt $\psi=c_1\phi_{\mathrm s,\mathrm A}+c_2\phi_{\mathrm s,\mathrm B}+c_3\phi_{\mathrm p,\mathrm A}+c_4\phi_{\mathrm p,\mathrm B}$ mit $E_\mathrm s=-5$ eV, $E_\mathrm p=-1$ eV, $V_\mathrm{ss}=1$ eV, $V_\mathrm{pp}=0{,}5$ eV.

<ol class="al">

<li>

Stelle die $4\times4$-Matrix auf. Welche Elemente sind null, welches Vorzeichen haben die übrigen?

</li>

<li>

Welche Bedingung liefert nichttriviale Lösungen? Bestimme die vier Energien für $V_\mathrm{sp}=0$.

</li>

<li>

Ein Rechner ergibt für $V_\mathrm{sp}=0{,}8$ eV die Werte $-6{,}138$, $-4{,}174$, $-1{,}362$ und $-0{,}326$ eV. In welche Richtung schiebt $V_\mathrm{sp}$ die s-Niveaus und die p-Niveaus? Prüfe die Summe.

</li>

</ol>

:::loesung
(a) In der Reihenfolge s,A; s,B; p,A; p,B ist die Diagonale $E_\mathrm s,E_\mathrm s,E_\mathrm p,E_\mathrm p$, und es gilt $H_{12}=-V_\mathrm{ss}$, $H_{14}=-V_\mathrm{sp}$, $H_{23}=V_\mathrm{sp}$, $H_{34}=V_\mathrm{pp}$, gespiegelt dasselbe. Null sind $H_{13}$ und $H_{24}$, die Elemente zwischen s und p am selben Atom. (b) $\det|\boldsymbol H-E\mathbf1|=0$. Für $V_\mathrm{sp}=0$ zerfällt die Matrix in zwei $2\times2$-Blöcke: $E=E_\mathrm s\mp V_\mathrm{ss}=-6$, $-4$ eV und $E=E_\mathrm p\mp V_\mathrm{pp}=-1{,}5$, $-0{,}5$ eV. (c) Beide s-Niveaus sinken, beide p-Niveaus steigen: $V_\mathrm{sp}$ stößt die Paare voneinander ab. Die Summe bleibt $-12{,}0$ eV $=2E_\mathrm s+2E_\mathrm p$.
:::
:::

:::aufgabe Aufgabe 10 ★★★ Kette mit p-Orbitalen senkrecht zur Linie
<span class="anker" id="aufg-10"></span>

Eine Kette hat je ein s-Orbital und ein p-Orbital senkrecht zur Kette, mit $E_\mathrm s=-6$ eV und $E_\mathrm p=-2$ eV. Die Kopplungen sind $V_\mathrm{ss}$ und $V_\mathrm{pp}=2V_\mathrm{ss}$.

<ol class="al">

<li>

Wie viele Bänder gibt es? Wie groß ist die erste Brillouin-Zone?

</li>

<li>

Stelle die drei $2\times2$-Matrizen und die Determinante auf. Warum fällt die s-p-Kopplung weg?

</li>

<li>

Bestimme beide Bänder $E(k)$. Warum steht das p-Band hier nicht auf dem Kopf?

</li>

<li>

Skizziere die Bänder für $V_\mathrm{ss}=0{,}2$, $0{,}5$ und $0{,}8$ eV und bestimme jeweils die Lücke. Was lässt sich über den Stoff sagen, wenn das s-Band voll ist?

</li>

</ol>

:::loesung
(a) 1 Atom mal 2 Orbitale, also 2 Bänder. Die Zone reicht von $-\pi/a$ bis $\pi/a$. (b) s koppelt an beide Keulen gleich stark mit verschiedenem Vorzeichen, die Summe ist null. Alle Matrizen sind diagonal: $\mathrm{diag}(-V_\mathrm{ss},-V_\mathrm{pp})$ außen, $\mathrm{diag}(E_\mathrm s,E_\mathrm p)$ in der Mitte. (c) $E=-6\,\mathrm{eV}-2V_\mathrm{ss}\cos(ka)$ und $E=-2\,\mathrm{eV}-4V_\mathrm{ss}\cos(ka)$. Seitlich überlappende p-Orbitale haben gleiches Vorzeichen, das Element ist negativ, der Boden liegt bei $k=0$. (d) Oberkante des s-Bands bei $k=\pi/a$, Unterkante des p-Bands bei $k=0$: $E_\mathrm g=4\,\mathrm{eV}-6V_\mathrm{ss}$, also 2,8 eV, 1,0 eV und keine Lücke bei 0,8 eV. Große Lücke: Isolator, kleine: Halbleiter, keine: Metall.
:::
:::
