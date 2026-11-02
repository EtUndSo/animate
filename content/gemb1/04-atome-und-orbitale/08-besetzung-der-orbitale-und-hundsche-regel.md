---
title: Stufe 6: Besetzung der Orbitale und Hundsche Regel
pfad: Elektrotechnik / 4. Semester / Elektronische Materialien und Bauelemente 1 / Atome und Orbitale
order: 4140800
summary: Jedes Orbital fasst zwei Elektronen.
tags: Abschirmung, effektive Kernladungszahl, Aufbauprinzip
lang: de
---

<span class="anker" id="stufe-6"></span>

:::zweck
Jedes Orbital fasst zwei Elektronen. Offen ist, in welcher Reihenfolge sich die Orbitale füllen, denn bei vielen Elektronen gelten die Energien des Wasserstoffs nicht mehr. Diese Stufe ordnet die Orbitale und füllt sie.
:::

**Die Idee.** Im Wasserstoff hängt die Energie nur von $n$ ab. Bei mehreren Elektronen stoßen sich diese ab, und innere Elektronen verdecken einen Teil der Kernladung. Das heißt __Abschirmung__: Ein äußeres Elektron sieht nicht $Z$, sondern eine kleinere __effektive Kernladungszahl__ $Z_\mathrm{eff}$. Ein s-Orbital reicht bis an den Kern. Es taucht unter die inneren Elektronen und spürt mehr Kernladung. Ein p-Orbital hält sein Drehimpuls vom Kern fern (Stufe [3](drei-quantenzahlen.html#stufe-3)), ein d-Orbital noch stärker. Deshalb liegt 2s unter 2p und 3s unter 3p unter 3d. Die Entartung in $\ell$ ist aufgehoben. Die Entartung in $m_\ell$ bleibt, denn keine Richtung ist ausgezeichnet.

:::definition Definition 6.1 (Elektronenkonfiguration)
<span class="anker" id="satz-6-1"></span>

Die Elektronenkonfiguration gibt die Besetzung der Unterschalen im Grundzustand des Atoms an: Zahl $n$, Buchstabe für $\ell$, Hochzahl für die Zahl der Elektronen.
:::

:::satz Satz 6.2 (Besetzungsregeln)
<span class="anker" id="satz-6-2"></span>

Im Grundzustand eines Atoms gelten drei Regeln:

<ol>

<li>

__Aufbauprinzip__: Die Orbitale füllen sich von unten: 1s, 2s, 2p, 3s, 3p, 4s, 3d, 4p, …

</li>

<li>

Pauli-Prinzip: je Orbital höchstens zwei Elektronen mit Spin $\uparrow\downarrow$.

</li>

<li>

Hundsche Regel: Energiegleiche Orbitale einer Unterschale werden zuerst einfach besetzt, und die Spins stehen parallel, sodass der Gesamtspin maximal wird. Erst dann beginnt die doppelte Besetzung.

</li>

</ol>
:::

⁠**So liest man das:** Die Hochzahl ist höchstens $2(2\ell+1)$, also 2, 6, 10, 14 für s, p, d, f. Im neutralen Atom ist die Summe aller Hochzahlen $Z$. **Gültigkeit:** Grundzustand eines freien Atoms. Die Schrödinger-Gleichung mit mehr als einem Elektron ist nicht mehr exakt lösbar, man braucht Näherungsverfahren. Die Rechnungen zeigen aber, dass sich die Dichte der Hülle in guter Näherung als Summe der Dichten einzelner Orbitale schreiben lässt. Darum darf man weiter in Orbitalen denken.

:::herleitung Warum einfach und warum parallel
⁠**Einfach:** Zwei Elektronen im selben Orbital teilen sich denselben Raum, ihre Coulomb-Abstoßung ist groß. In zwei Orbitalen mit verschiedenen Richtungen, etwa $2\mathrm p_x$ und $2\mathrm p_y$, liegen sie weiter auseinander.

⁠**Parallel:** Bei gleichem Spin ist $\Phi$ antisymmetrisch, und die Elektronen meiden sich (Abb. [5](spin-und-pauli-prinzip.html#abb-5) links). Wer sich meidet, stößt sich weniger ab und schirmt den Kern weniger ab. Beide Elektronen rücken dadurch näher an den Kern, und die Gesamtenergie sinkt.
:::

:::abbildung gemb1/k4besetzung 6
Kästchen sind Orbitale, Pfeile Elektronen, die Energie wächst nach oben (nicht maßstäblich). Beide Atome haben außen zwei s- und zwei p-Elektronen. Die äußeren p-Elektronen sitzen nach der Hundschen Regel einzeln und parallel, ein p-Orbital bleibt leer.
:::

**Beispiel.** Kohlenstoff hat sechs Elektronen: je zwei in 1s und 2s, zwei bleiben für 2p. Sie gehen einzeln in $2\mathrm p_x$ und $2\mathrm p_y$, also $1\mathrm s^2\,2\mathrm s^2\,2\mathrm p^2$. Silizium hat 14 Elektronen: $1\mathrm s^2\,2\mathrm s^2\,2\mathrm p^6\,3\mathrm s^2\,3\mathrm p^2$. Beide tragen außen dasselbe Muster $\mathrm s^2\mathrm p^2$. Wie stark die Abschirmung wirkt, zeigt Lithium. Sein 2s-Elektron lässt sich mit 5,39 eV lösen. Aus $|E|=13{,}6\,\mathrm{eV}\cdot Z_\mathrm{eff}^2/n^2$ (Stufe [2](das-wasserstoffatom.html#stufe-2) mit $Z_\mathrm{eff}$ statt $Z$) folgt $Z_\mathrm{eff}=1{,}26$ statt 3. **Grenzfälle:** Für $Z=1$ gibt es nichts abzuschirmen, und 2s und 2p sind wieder entartet. Bei Helium mit zwei 1s-Elektronen sinkt die Ionisierungsenergie von 54,4 eV für He$^+$ auf 24,6 eV, das ist $Z_\mathrm{eff}=1{,}34$.

Die Hundsche Regel hat auch für magnetische Werkstoffe zentrale Bedeutung: Parallele, ungepaarte Spins geben einem Atom ein magnetisches Moment. Eisen hat in 3d sechs Elektronen auf fünf Orbitale und damit vier ungepaarte Spins.

:::aufgabe Aufgabe 9 ★ Kästchen füllen
<span class="anker" id="aufg-9"></span>

<ol class="al">

<li>

Gib die Konfiguration von Stickstoff ($Z=7$), Sauerstoff ($Z=8$), Phosphor ($Z=15$) und Schwefel ($Z=16$) an.

</li>

<li>

Zeichne die äußeren p-Orbitale als Kästchen und zähle die ungepaarten Elektronen.

</li>

<li>

Welche dieser Atome haben außen dasselbe Muster?

</li>

</ol>

:::loesung
(a) N: $1\mathrm s^2\,2\mathrm s^2\,2\mathrm p^3$. O: $1\mathrm s^2\,2\mathrm s^2\,2\mathrm p^4$. P: $1\mathrm s^2\,2\mathrm s^2\,2\mathrm p^6\,3\mathrm s^2\,3\mathrm p^3$. S: $1\mathrm s^2\,2\mathrm s^2\,2\mathrm p^6\,3\mathrm s^2\,3\mathrm p^4$. (b) Bei $\mathrm p^3$ sitzen drei Elektronen einzeln und parallel: drei ungepaarte. Bei $\mathrm p^4$ ist ein Orbital doppelt besetzt: zwei ungepaarte. (c) N und P mit $\mathrm s^2\mathrm p^3$, O und S mit $\mathrm s^2\mathrm p^4$.
:::
:::

:::aufgabe Aufgabe 10 ★★ Abschirmung messen
<span class="anker" id="aufg-10"></span>

Das äußerste Elektron von Natrium ($Z=11$) sitzt in 3s, seine Ionisierungsenergie ist 5,14 eV. Bei Kalium ($Z=19$) sitzt es in 4s, mit 4,34 eV.

<ol class="al">

<li>

Berechne jeweils $Z_\mathrm{eff}$.

</li>

<li>

Grenzfall: Welches $Z_\mathrm{eff}$ wäre es bei vollständiger Abschirmung durch alle inneren Elektronen, welches ganz ohne Abschirmung? Welche Ionisierungsenergie ergäbe das für Natrium?

</li>

<li>

Warum liegt der Wert über dem Fall der vollständigen Abschirmung?

</li>

</ol>

:::loesung
(a) Aus $Z_\mathrm{eff}=n\sqrt{|E|/(13{,}6\,\mathrm{eV})}$ folgt für Na $3\sqrt{0{,}378}=1{,}84$ und für K $4\sqrt{0{,}319}=2{,}26$. (b) Vollständige Abschirmung: $Z_\mathrm{eff}=1$, für Na $13{,}6\,\mathrm{eV}/9=1{,}51$ eV. Keine Abschirmung: $Z_\mathrm{eff}=11$, für Na $13{,}6\,\mathrm{eV}\cdot121/9=183$ eV. Der Messwert liegt nahe am ersten Fall. (c) Ein s-Orbital taucht unter die inneren Schalen. Dort sieht es mehr als eine Ladung $+e$.
:::
:::
