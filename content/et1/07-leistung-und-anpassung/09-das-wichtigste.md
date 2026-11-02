---
title: Das Wichtigste
pfad: Elektrotechnik / 1. Semester / Grundlagen der Elektrotechnik / Leistung, Anpassung und Wirkungsgrad
order: 1170900
summary: Warum am Leistungsmaximum die Hälfte der Energie in der Quelle bleibt
tags: Stromwärme, Leistungsanpassung, Wirkungsgrad, Spannungsanpassung, Stromanpassung
lang: de
---

:::merke Die Antwort in drei Sätzen
<ol>

<li>

Spannung ist Energie je Ladung, Strom ist Ladung je Zeit. Ihr Produkt ist Energie je Zeit: $p=u\,i$.

</li>

<li>

Im Widerstand beschleunigt das Feld die Elektronen, und jeder Stoß übergibt die gewonnene Energie dem Atomgitter. Deshalb wird dort die ganze Leistung zu Wärme, der __Stromwärme__, mit $P=R\,I^2$.

</li>

<li>

Eine Quelle mit Innenwiderstand $R_\mathrm{i}$ gibt die größte Leistung an die Last $R_\mathrm{L}=R_\mathrm{i}$ ab. Das heißt __Leistungsanpassung__. Dort teilt sich die Energie jeder Ladung zu gleichen Teilen auf Quelle und Last, und der __Wirkungsgrad__, der genutzte Anteil der Leistung, beträgt 50 %. Eine feste Spannung liefert die __Spannungsanpassung__ (Last groß gegen die Quelle), einen festen Strom die __Stromanpassung__ (Last klein gegen die Quelle).

</li>

</ol>
:::

:::kern Das Wichtigste
<ul>

<li>

Leistung ist Energie je Coulomb mal Coulomb je Sekunde: $p=u\,i$. Energie ist ihr Zeitintegral.

</li>

<li>

Im Widerstand geben Stöße alles ans Gitter: $P=R\,I^2=U^2/R$, begrenzt durch $P_\mathrm{max}$.

</li>

<li>

Am Widerstand ist bei Sinusspannung $P=\frac12\hat u^2/R=\frac12\hat\imath^2R$.

</li>

<li>

Gleiche Leistung bei $n$-facher Spannung senkt den Leitungsverlust auf $1/n^2$.

</li>

<li>

Bilanz: $P_\mathrm{q}=P_\mathrm{v}+P_\mathrm{L}$. Wirkungsgrad: $\eta=U_\mathrm{L}/U_\mathrm{q}=R_\mathrm{L}/(R_\mathrm{L}+R_\mathrm{i})$.

</li>

<li>

Größte Leistung bei $R_\mathrm{L}=R_\mathrm{i}$: $P_\mathrm{L,max}=U_\mathrm{q}^2/(4R_\mathrm{i})$, mit $\eta=\frac12$, weil Strom und Wirkungsgrad linear gegeneinander laufen.

</li>

<li>

Energietechnik will $R_\mathrm{L}\gg R_\mathrm{i}$, Signalübertragung $R_\mathrm{L}=R_\mathrm{i}$. Ersatzquellen geben das Maximum richtig an, den Wirkungsgrad nicht.

</li>

</ul>
:::

**Ein Prinzip hinter allen Ergebnissen.** Jede Leistung ist das Produkt zweier Antworten: Wie viel Energie gibt ein Coulomb an dieser Stelle ab, und wie viele Coulomb kommen je Sekunde vorbei?

| Ergebnis | Woher es kommt |
|---|---|
| $p=u\,i$ | Energie je Ladung mal Ladung je Zeit (Stufe [1](energie-je-ladung-mal-ladung-je-zeit.html#stufe-1)) |
| $P=R\,I^2=U^2/R$, Belastbarkeit | Stöße geben alles ans Gitter; doppelter Strom heißt doppelt so viele Coulomb, die je doppelt so viel abgeben (Stufe [2](warum-der-widerstand-warm-wird.html#stufe-2)) |
| $P=\frac12\hat u^2/R$ | $u$ und $i$ wechseln gemeinsam das Vorzeichen, $\cos^2$ hat den Mittelwert $\frac12$ (Stufe [3](mittlere-leistung-bei-sinusspannung.html#stufe-3)) |
| Hochspannungsleitungen | Dieselbe Leistung mit weniger Coulomb, von denen jedes weniger verliert (Stufe [4](leitungsverluste.html#stufe-4)) |
| $\eta=U_\mathrm{L}/U_\mathrm{q}$ | Anteil der Energie je Coulomb, der die Last erreicht (Stufe [5](wohin-die-leistung-einer-quelle-geht.html#stufe-5)) |
| $R_\mathrm{L}=R_\mathrm{i}$ | Strom und Lastspannung laufen linear gegeneinander, ihr Produkt ist in der Mitte am größten (Stufe [6](leistungsanpassung.html#stufe-6)) |
| $\eta=50\,\%$ am Maximum | Die Mitte heißt: Die Hälfte der Energie je Coulomb bleibt innen (Stufe [7](warum-50-und-welches-ziel-gilt.html#stufe-7)) |
