---
title: Das Wichtigste
pfad: Elektrotechnik / 1. Semester / Grundlagen der Elektrotechnik / Strom, Widerstand und Kirchhoff
order: 1121200
summary: Warum Elektronen kriechen, der Strom aber sofort da ist, und warum Netze Erhaltungssätzen gehorchen
tags: Driftgeschwindigkeit, Stromdichte, Spannungsteiler
lang: de
---

:::merke Die Antwort in drei Sätzen
<ol>

<li>

Das Feld im Leiter beschleunigt die freien Elektronen, Stöße nehmen ihnen die gewonnene Geschwindigkeit wieder ab. Es bleibt eine kleine __Driftgeschwindigkeit__ (mittlere Geschwindigkeit längs des Leiters), die dem Feld proportional ist. Deshalb ist die __Stromdichte__, der Strom je Querschnittsfläche, dem Feld proportional, und für das Bauteil folgt $U=R\,I$.

</li>

<li>

Die Knotenregel ist Ladungserhaltung, die Maschenregel ist Energieerhaltung.

</li>

<li>

Zusammen liefern die drei Gesetze für jedes Netz genau so viele Gleichungen, wie es Unbekannte hat. In Reihe teilt sich die Spannung (__Spannungsteiler__: zwei Widerstände, deren Verhältnis eine Teilspannung festlegt), parallel teilt sich der Strom.

</li>

</ol>
:::

:::kern Das Wichtigste
<ul>

<li>

Strom: $i=\mathrm{d} Q/\mathrm{d} t$, $I=q\,v\,A$; Stromdichte $\vec j=q\,\vec v$.

</li>

<li>

Drift: $\vec v_\mathrm D=-\mu\,\vec E$, $v_\mathrm D=I/(n\,e\,A)$; Strom sofort, weil das Feld läuft.

</li>

<li>

Material: $\vec j=\sigma\,\vec E$, $\sigma=n\,e\,\mu=1/\rho$.

</li>

<li>

Bauteil: $U=R\,I$, $R=\rho\,L/A$, $G=1/R$; Leistung $P=U\,I$.

</li>

<li>

E-Reihe: $w=(\sqrt[N]{10})^i$; Temperatur: $R(\vartheta)=R(\vartheta_0)(1+\alpha\,(\vartheta-\vartheta_0))$; PTC, NTC.

</li>

<li>

Zweipol: Kennlinie $I=f(U)$; VZS gleichsinnig, GZS gegensinnig; Elektronen laufen gegen den technischen Strom.

</li>

<li>

Netz: $k$ Knoten, $z$ Zweige, $m=z-k+1$ unabhängige Maschen; Baum aus $k-1$ Zweigen.

</li>

<li>

Knotenregel: $\sum I=0$, $k-1$ Gleichungen; Maschenregel: $\sum U=0$, $z-k+1$ Gleichungen.

</li>

<li>

Reihe: $R_\mathrm{ges}=\sum R_i$, $U_\nu/U=R_\nu/\sum R_i$, nur unbelastet.

</li>

<li>

Parallel: $G_\mathrm{ges}=\sum G_i$, $R_1\parallel R_2=R_1R_2/(R_1+R_2)$, $I_1=I_\mathrm{ges}\,R_2/(R_1+R_2)$.

</li>

<li>

Belastet: $U_2/U=(R_2\parallel R_\mathrm L)/(R_1+R_2\parallel R_\mathrm L)$, Fehler $R_\mathrm i/(R_\mathrm i+R_\mathrm L)$.

</li>

</ul>
:::

**Ausblick auf [Teil 3](/wissen/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/der-kondensator/der-kondensator.html).** Ein Knoten speichert fast keine Ladung. Der Kondensator aus zwei großen Platten tut das Gegenteil: Er speichert Ladung und Energie.

**Ein Prinzip hinter allen Ergebnissen.** Zwei Erhaltungssätze und ein Gleichgewicht tragen das Kapitel: Ladung geht nicht verloren, Energie geht nicht verloren, und im Leiter halten sich Antrieb durch das Feld und Bremsen durch Stöße die Waage.

| Ergebnis | Woher es kommt |
|---|---|
| $I=\mathrm{d} Q/\mathrm{d} t$, $j=q\,v$ | Ladung, die in einer Zeit durch eine Fläche läuft (Stufe [1](strom-ist-bewegte-ladung.html#stufe-1)) |
| kleine, konstante Drift | Gleichgewicht aus Feld und Stößen, riesige Elektronendichte (Stufe [2](langsame-elektronen-sofortiger-strom.html#stufe-2)) |
| Strom ist sofort da | Das Feld läuft, nicht die Elektronen; der Draht ist schon voll (Stufe [2](langsame-elektronen-sofortiger-strom.html#stufe-2)) |
| $U=R\,I$, $R=\rho L/A$ | Drift proportional zum Feld, Feld proportional zur Spannung (Stufe [3](das-ohmsche-gesetz-aus-feld-und-stoen.html#stufe-3)) |
| Temperaturabhängigkeit | Wärme ändert die Stoßzeit oder die Zahl der Ladungsträger (Stufe [4](reale-widerstande-werte-und-temperatur.html#stufe-4)) |
| Zählpfeile, $m=z-k+1$ | Vereinbarung und Abzählen, bevor gerechnet wird (Stufen [5](zweipole-und-zahlpfeile.html#stufe-5) und [6](knoten-zweige-maschen.html#stufe-6)) |
| Knotenregel | Ladungserhaltung: Ein Knoten speichert nichts (Stufe [7](die-knotenregel-ist-ladungserhaltung.html#stufe-7)) |
| Maschenregel | Energieerhaltung: Ein Umlauf endet auf dem Startpotenzial (Stufe [8](die-maschenregel-ist-energieerhaltung.html#stufe-8)) |
| Spannungsteiler, Stromteiler | Beide Regeln, angewandt auf Reihe und Parallele (Stufen [9](reihenschaltung-und-spannungsteiler.html#stufe-9) und [10](parallelschaltung-stromteiler-und-belastung.html#stufe-10)) |
