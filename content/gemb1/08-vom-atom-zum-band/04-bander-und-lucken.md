---
title: Stufe 2: Bänder und Lücken
pfad: Elektrotechnik / 4. Semester / GEMB1 – Grundlagen elektronischer Materialien und Bauelemente 1 / Vom Atom zum Band
adresse: elektrotechnik/4-semester/elektronische-materialien-und-bauelemente-1/vom-atom-zum-band
knoten: Kapitel 8: Vom Atom zum Band
order: 4180400
summary: Die Periodizität sagt noch nicht, welche Energien vorkommen.
tags: Bragg-Reflexion, Energieband, Bandlücke
lang: de
---

<span class="anker" id="stufe-2"></span>

:::zweck
Die Periodizität sagt noch nicht, welche Energien vorkommen. Diese Stufe löst das Kammpotential und zeigt: Die erlaubten Energien bilden Bereiche, zwischen denen Lücken liegen.
:::

**Die Idee.** An jeder Barriere wird ein kleiner Teil der Welle zurückgeworfen. Meist heben sich die Rückläufer auf, jeder kommt mit anderer Phase an. Ist aber der Umweg $2a$ ein ganzes Vielfaches der Wellenlänge, also $\lambda=2a/\nu$ oder $k=\nu\pi/a$, addieren sich alle. Die Welle wird vollständig reflektiert, das heißt __Bragg-Reflexion__. Das geschieht genau am Rand der Zone. Hin- und rücklaufende Welle bilden dort stehende Wellen, und davon gibt es zwei: Ist $x=0$ eine Topfmitte, hat $\cos(\pi x/a)$ seine Berge in den Töpfen, $\sin(\pi x/a)$ in den Barrieren. Die zweite spürt das hohe Potential und liegt energetisch höher. Für Energien dazwischen gibt es keine Lösung.

:::definition Definition 2.1 (Band und Lücke)
<span class="anker" id="satz-2-1"></span>

Ein __Energieband__ ist ein zusammenhängender Bereich erlaubter Energien, in dem es reelle $k$ gibt, also laufende Wellen. Eine __Bandlücke__ ist ein Bereich zwischen zwei Bändern ohne reelles $k$. Dort kann sich keine Welle im Kristall ausbreiten.
:::

:::abbildung gemb1/k8baender 2
$E(k)$ des Kammpotentials mit $w=1$ nm und $V_\mathrm B=1$ eV, gerechnet aus der Schrödinger-Gleichung. Gestrichelt die Parabel des freien Elektrons, blau getönt die Bänder, grau die Lücke. Die dickere Barriere macht die Bänder schmaler und flacher und die Lücke breiter.
:::

**Die Rechnung.** Mit dem Rand [(1.1)](was-aus-der-periodizitat-folgt.html#gl-1-1) löst man die Schrödinger-Gleichung für eine Zelle, etwa auf dem Gitter [(0.1)](von-grund-auf-was-aus-fruheren-teilen-gebraucht-wird.html#gl-0-1) (Energien in meV):

| Barriere $b$ | 1. Band | Lücke | 2. Band | Breite 1. Band | $v_\text{max}$ im 1. Band |
|---|---|---|---|---|---|
| 0,2 nm | 119 bis 268 | 267 | 535 bis 1071 | 149 | $1{,}40\cdot10^5$ m/s |
| 0,4 nm | 162 bis 221 | 387 | 608 bis 876 | 59 | $6{,}3\cdot10^4$ m/s |

⁠**So liest man das:** Ein einzelner Topf hat die Niveaus 191 meV und 703 meV. Das erste Band liegt um das erste Niveau, das zweite um das zweite: Die Bänder stammen von den Zuständen der einzelnen Töpfe. Der Mechanismus der Breite ist das Tunneln. Je dünner oder niedriger die Barriere, desto stärker reicht die Welle zum Nachbarn, desto breiter das Band und desto kleiner die Lücke. Mit dem Band wächst $\partial E/\partial k$, das Elektron läuft schneller. Bei $E\approx0{,}19$ eV ist $\kappa=4{,}61\,\mathrm{nm^{-1}}$, also schwächen 0,2 nm mehr Barriere um $\mathrm{e}^{\kappa\cdot0{,}2\,\mathrm{nm}}=2{,}51$. Die Bandbreite sinkt um $149/59=2{,}52$.

**Warum die Lücke am Zonenrand sitzt.** In der Parabelschar aus [Kapitel 7](/wissen/elektrotechnik/4-semester/elektronische-materialien-und-bauelemente-1/kristallwachstum-und-reziprokes-gitter/kristallwachstum-und-reziprokes-gitter.html) schneiden sich dort zwei Äste: $k=\pi/a$ und $k-2\pi/a=-\pi/a$ haben dieselbe Energie. Ihre Überlagerung sind die stehenden Wellen der Idee. Das Potential trennt sie, und die Lücke öffnet sich.

::::beispiel
Für $b=0{,}2$ nm ist $a=1{,}2$ nm. Das freie Elektron hätte am Zonenrand $\hbar^2(\pi/a)^2/(2m_0)=261$ meV, das mittlere Potential $V_\mathrm Bb/a$ gibt 167 meV dazu, zusammen 428 meV. Das liegt in der Lücke von 268 bis 535 meV. In der Lückenmitte hat $k$ einen imaginären Anteil, die Amplitude fällt je Periode auf 45 %, nach fünf Perioden auf 1,8 %. Für diese Energie wirkt der Kristall wie eine Wand, ein Elektron läuft zurück.
::::

⁠**Grenzfälle:** Für $b\to\infty$ schrumpft jedes Band auf das Niveau des Einzeltopfs. Für $b\to0$ schließen sich die Lücken, und die Parabel bleibt.

:::zusatz Lücken für Schall und Licht
Bänder und Lücken gelten für alle Wellen in periodischen Strukturen. Reihen von Säulen sperren Schall in einem Frequenzband. Spiegel für extremes UV-Licht mit $\lambda=13{,}5$ nm, mit dem man Chips belichtet, sind Stapel aus etwa 40 Doppelschichten Molybdän und Silizium mit der Periode $\lambda/2$. Dieses Licht wird sogar von Luft verschluckt, Linsen scheiden aus. Im Stapel fällt es in die Lücke und kehrt um.
:::

:::aufgabe Aufgabe 2 ★★ Wo liegen die Lücken?
<span class="anker" id="aufg-2"></span>

Ein Kammpotential hat $w=1{,}2$ nm, $b=0{,}3$ nm und $V_\mathrm B=0{,}8$ eV, Masse $m_0$.

<ol class="al">

<li>

Bei welchen $k$ und $\lambda$ tritt Bragg-Reflexion für $\nu=1,2,3$ auf?

</li>

<li>

Schätze die Lage der drei Lücken aus Parabel und mittlerem Potential.

</li>

<li>

Die genaue Rechnung ergibt die Bänder 101 bis 176, 414 bis 703, 960 bis 1576 und ab 1778 meV. Prüfe deine Schätzung.

</li>

<li>

Vorhersage: Was geschieht mit den Bändern, wenn $V_\mathrm B$ auf 2 eV steigt?

</li>

</ol>

:::loesung
(a) $a=1{,}5$ nm: $k=\nu\pi/a=2{,}09$, $4{,}19$, $6{,}28\,\mathrm{nm^{-1}}$ und $\lambda=2a/\nu=3$, $1{,}5$, $1$ nm. (b) Mittleres Potential $V_\mathrm Bb/a=160$ meV. Parabel 167, 668, 1504 meV, zusammen 327, 828, 1664 meV. (c) Alle drei liegen in den Lücken 176 bis 414, 703 bis 960, 1576 bis 1778 meV. (d) $\kappa$ wächst, das Tunneln sinkt: Die Bänder werden schmaler, die Lücken breiter.
:::
:::
