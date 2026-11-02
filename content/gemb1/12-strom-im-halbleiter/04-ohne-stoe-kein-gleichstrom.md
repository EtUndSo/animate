---
title: Stufe 2: Ohne Stöße kein Gleichstrom
pfad: Elektrotechnik / 4. Semester / Elektronische Materialien und Bauelemente 1 / Strom im Halbleiter
order: 4220400
summary: Nach (1.2) wächst k im Feld immer weiter.
tags: Bloch-Schwingung, Störstellenstreuung, Legierungsstreuung, elastische Streuung, inelastische Streuung, Streuzeit, Streurate
lang: de
---

<span class="anker" id="stufe-2"></span>

:::zweck
Nach [(1.2)](strom-aus-besetzten-zustanden.html#gl-1-2) wächst $k$ im Feld immer weiter. Diese Stufe zeigt, was ein idealer Kristall daraus machen würde und welche Stöße einen stetigen Strom erst möglich machen.
:::

**Die Idee.** Läuft $k$ ungestört, erreicht es den Zonenrand und tritt am anderen Rand wieder ein. Damit wechselt $v$ das Vorzeichen: Das Elektron pendelt. Das ist die __Bloch-Schwingung__ (auch Bloch-Oszillation). Im Mittel fließt kein Strom, ein idealer Kristall wäre im Gleichfeld ein Isolator. Im echten Kristall wirft ein Stoß das Elektron zurück, lange bevor es weit gekommen ist. Das Feld baut die Schieflage auf, die Stöße bauen sie ab, und dazwischen stellt sich ein fester Strom ein (Abb. [2](#abb-2)).

:::satz Satz 2.1 (Bloch-Schwingung)
<span class="anker" id="satz-2-1"></span>

Im Band $E(k)=E_\mathrm C+2t_0(1-\cos(ka))$ gilt mit $k(0)=0$ unter konstanter Kraft $F$ ohne Stöße

<span class="anker" id="gl-2-1"></span>
$$v(t)=v_\text{max}\sin\Bigl(\frac{Fa}\hbar\,t\Bigr),\qquad T_\mathrm B=\frac{2\pi\hbar}{|F|\,a}=\frac h{|F|\,a},\qquad\Delta x=\frac{4t_0}{|F|}. \tag{2.1}$$
:::

⁠**So liest man das:** $T_\mathrm B$ ist die Zeit für einen Zonendurchlauf, die Strecke $2\pi/a$ in $k$. $\Delta x$ ist die Länge des überstrichenen Ortsbereichs, Bandbreite durch Kraft. **Herleitung:** Mit $k=Ft/\hbar$ folgt $v$ aus $v(k)=(2t_0a/\hbar)\sin(ka)$, und $x(t)=\int v\,\mathrm{d} t=(2t_0/F)\bigl(1-\cos(Fat/\hbar)\bigr)$.

:::abbildung gemb1/k12bloch 2
Links ohne Stöße: $k$ springt am Zonenrand von $\pi/a$ nach $-\pi/a$, $v$ pendelt um null. Rechts mit Stößen, schematisch: Jeder Stoß setzt $k$ zurück, hier vereinfacht auf null. Im Mittel bleibt die Verschiebung $F\tau/\hbar$. Die Zeitachsen sind verschieden: $\tau\ll T_\mathrm B$.
:::

:::definition Definition 2.2 (Streuung)
<span class="anker" id="satz-2-2"></span>

Ein Stoß ist ein plötzlicher Übergang eines Ladungsträgers von $k$ nach $k'$. Ladungsträger streuen an Gitterschwingungen (Phononen), am Coulomb-Potential von Verunreinigungen und Dotierstoffen (__Störstellenstreuung__ an ionisierten Atomen), an der unregelmäßigen Atomfolge von Kristallen aus mehreren Atomsorten (__Legierungsstreuung__), an Fehlstellen und anderen Defekten im Gitter und an anderen Elektronen. Ändert sich nur der Impuls bei gleicher Energie, heißt das __elastische Streuung__, ändert sich auch die Energie, __inelastische Streuung__.
:::

⁠**So liest man das:** Die Rümpfe selbst sind kein Hindernis wie im Gasmodell. Die Welle wird zwar an jedem Rumpf etwas gestreut, doch alle Teilwellen setzen sich zur Bloch-Funktion zusammen, die ungestört weiterläuft ([Teil 8](/wissen/elektrotechnik/4-semester/elektronische-materialien-und-bauelemente-1/vom-atom-zum-band/vom-atom-zum-band.html)). Streuen kann nur, was die Periode stört: Ein schwingender Rumpf sitzt neben seinem Platz, ein Dotieratom trägt eine andere Ladung. Am schweren Ion prallt das Elektron elastisch ab, mit einem Phonon tauscht es Energie aus. Stöße zweier Elektronen lassen die Summe ihrer $k$ gleich und ändern in einem Parabelband den Strom nicht.

:::satz Satz 2.3 (Matthiessensche Regel)
<span class="anker" id="satz-2-3"></span>

Haben unabhängige Prozesse die mittleren Stoßzeiten $\tau_i$, so gilt für die gesamte __Streuzeit__ $\tau_\text{scat}$

<span class="anker" id="gl-2-2"></span>
$$\frac1{\tau_\text{scat}}=\frac1{\tau_\text{e-ph}}+\frac1{\tau_\text{e-ion}}+\frac1{\tau_\text{e-e}}+\dots \tag{2.2}$$
:::

⁠**So liest man das:** $1/\tau_i$ ist die __Streurate__, die Zahl der Stöße je Sekunde. Es addieren sich die Raten, nicht die Zeiten, denn in einer kurzen Zeit $\mathrm{d} t$ stößt ein Träger mit der Wahrscheinlichkeit $\mathrm{d} t/\tau_1+\mathrm{d} t/\tau_2+\dots$. Das kleinste $\tau_i$ bestimmt das Ergebnis. Die Indizes stehen für Phonon, Ion und Elektron.

**Beispiel.** Bei $\mathcal E=2\cdot10^5$ V/m ist in der Kette $T_\mathrm B=82{,}7$ ps und $\Delta x=10$ µ m. In der Probe ist $\tau_\text{e-ph}=0{,}21$ ps und $\tau_\text{e-ion}=1{,}24$ ps, zusammen $1/\tau_\text{scat}=(4{,}83+0{,}81)\cdot10^{12}\,\mathrm{s^{-1}}$, also $\tau_\text{scat}=0{,}18$ ps. Auf einen Zonendurchlauf kämen über 400 Stöße: Die Schwingung beginnt gar nicht. **Grenzfall:** Für $\mathcal E\to0$ geht $T_\mathrm B\to\infty$.

:::aufgabe Aufgabe 2 ★ Raten addieren
<span class="anker" id="aufg-2"></span>

<ol class="al">

<li>

Drei Prozesse haben $\tau=0{,}5$ ps, 1,5 ps und 6 ps. Berechne $\tau_\text{scat}$. Warum ist der Mittelwert der Zeiten falsch? Um wie viel Prozent wächst $\tau_\text{scat}$, wenn der seltenste Prozess wegfällt?

</li>

<li>

Weil $\mu\propto\tau$ ist ([Teil 1](/wissen/elektrotechnik/4-semester/elektronische-materialien-und-bauelemente-1/welle-teilchen-und-schrodinger-gleichung/welle-teilchen-und-schroedinger-gleichung.html)), gilt dasselbe für Kehrwerte von Beweglichkeiten. Zwei Mechanismen allein ergäben 900 und $300\,\mathrm{cm^2/(V\,s)}$. Wie groß ist $\mu$ zusammen?

</li>

<li>

Ein Kristall hat $a=0{,}5$ nm und liegt im Feld $10^6$ V/m. Berechne $T_\mathrm B$. Wie viele Stöße kommen bei $\tau_\text{scat}=0{,}1$ ps auf eine Schwingung? Was müsste man ändern, um die Schwingung zu sehen?

</li>

</ol>

:::loesung
(a) $1/\tau_\text{scat}=(2+0{,}667+0{,}167)\,\mathrm{ps^{-1}}=2{,}833\,\mathrm{ps^{-1}}$, also $\tau_\text{scat}=0{,}353$ ps. Der Mittelwert 2,67 ps wäre länger als die kürzeste Zeit, aber ein zusätzlicher Prozess macht Stöße nur häufiger. Ohne den dritten ist $\tau_\text{scat}=0{,}375$ ps, 6,2 % mehr. (b) $1/\mu=1/900+1/300$ ergibt $\mu=225\,\mathrm{cm^2/(V\,s)}$, kleiner als der kleinere Wert. (c) $T_\mathrm B=h/(e\mathcal Ea)=8{,}27$ ps, rund 83 Stöße je Schwingung. Man braucht größeres $a$ und längeres $\tau_\text{scat}$, etwa ein Schichtpaket mit $a=10$ nm und $T_\mathrm B=0{,}41$ ps.
:::
:::
