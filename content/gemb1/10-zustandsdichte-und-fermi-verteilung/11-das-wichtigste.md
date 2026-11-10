---
title: Das Wichtigste
pfad: Elektrotechnik / 4. Semester / GEMB1 – Grundlagen elektronischer Materialien und Bauelemente 1 / Zustandsdichte und Fermi-Verteilung
adresse: elektrotechnik/4-semester/elektronische-materialien-und-bauelemente-1/zustandsdichte-und-fermi-verteilung
knoten: Kapitel 10: Zustandsdichte und Fermi-Verteilung
order: 4201100
summary: Plätze mal Besetzung: Wie viele Ladungsträger ein Kristall enthält
tags: 
lang: de
---

:::kern Das Wichtigste
<ul>

<li>

⁠**Grundformel:** $n=\int\mathrm{d} E\,D(E)\,f(E)$ und $p=\int\mathrm{d} E\,D(E)\,(1-f(E))$: Plätze mal Besetzung.

</li>

<li>

⁠**Zählen:** Raster $2\pi/L$ im $k$-Raum, $D=(2/L^d)\,\mathrm{d} Z/\mathrm{d} E\propto E^{-1/2},E^0,E^{1/2}$ für $d=1,2,3$. Bänder: $D_\mathrm C=4\pi(2m_\mathrm C^*)^{3/2}h^{-3}\sqrt{E-E_\mathrm C}$, $D_\mathrm V$ gespiegelt, $m^*_\mathrm{DOS}=(g^2m_xm_ym_z)^{1/3}$.

</li>

<li>

⁠**Besetzung:** $W=\prod_ig_i!/(N_i!\,(g_i-N_i)!)$, $S=k_\mathrm B\ln W$, Maximum: $f=1/(1+\mathrm{e}^{(E-E_\mathrm F)/(k_\mathrm BT)})$, $f(E_\mathrm F)=\frac12$. $T=0$: Stufe, sonst Zone der Breite $4k_\mathrm BT$. Für $E-E_\mathrm F\gg k_\mathrm BT$: $f\approx\mathrm{e}^{-(E-E_\mathrm F)/(k_\mathrm BT)}$.

</li>

<li>

⁠**Dichten:** $n=N_\mathrm C\mathrm{e}^{-(E_\mathrm C-E_\mathrm F)/(k_\mathrm BT)}$, $p=N_\mathrm V\mathrm{e}^{-(E_\mathrm F-E_\mathrm V)/(k_\mathrm BT)}$, $N=2(2\pi m^*k_\mathrm BT/h^2)^{3/2}$. $n\,p=N_\mathrm CN_\mathrm V\mathrm{e}^{-E_\mathrm g/(k_\mathrm BT)}$.

</li>

<li>

⁠**Ergänzung Metall:** $E_\mathrm{F0}=\hbar^2(3\pi^2n)^{2/3}/(2m^*)$, $n_\mathrm{th}/n\approx4k_\mathrm BT/E_\mathrm F$, $c_V\approx\frac{\pi^2}2nk_\mathrm BT/T_\mathrm F$.

</li>

</ul>
:::

:::merke Die Antwort in drei Sätzen
<ol>

<li>

Die Dichte der Ladungsträger ist die Summe über alle Plätze mal ihrer Besetzung, und die Plätze zählt man als Raster im $k$-Raum.

</li>

<li>

Die Besetzung folgt aus der Abzählung der Anordnungen: Die Verteilung mit den meisten Anordnungen ist die Fermi-Verteilung, und Wärme macht nur einen Streifen der Breite $4k_\mathrm BT$ um $E_\mathrm F$ weich.

</li>

<li>

Liegt $E_\mathrm F$ in der Lücke, sieht ein Band nur den Boltzmann-Faktor bis zu seinem Rand: Es wirkt wie $N_\mathrm C$ oder $N_\mathrm V$ Plätze auf dem Rand, und das Produkt $n\,p$ hängt nicht mehr von $E_\mathrm F$ ab.

</li>

</ol>
:::

**Ein Prinzip hinter allen Ergebnissen.** Alles in diesem Kapitel ist Zählen: erst die Plätze im $k$-Raum, dann die Anordnungen der Elektronen auf diesen Plätzen.

| Ergebnis | Woher es kommt |
|---|---|
| $D\propto E^{(d-2)/2}$ | Größe der Fläche gleicher Energie mal $\mathrm{d} k/\mathrm{d} E$ (Stufe [1](warum-man-zustande-zahlt.html#stufe-1) und [2](kreisring-und-kugelschale.html#stufe-2)) |
| $m^*_\mathrm{DOS}$ | Volumen der Ellipsoide, $g$-mal gezählt (Stufe [3](leitungsband-und-valenzband.html#stufe-3)) |
| Scharfes Maximum von $W$ | Sehr viele Plätze und Elektronen (Stufe [4](anordnungen-zahlen.html#stufe-4)) |
| Fermi-Verteilung | Größtes $W$ bei Pauli-Regel, gegebener Energie und Zahl (Stufe [5](die-fermi-verteilung.html#stufe-5)) |
| Stufe und Zone $4k_\mathrm BT$ | Nur freie Plätze in Reichweite zählen (Stufe [6](temperatur-und-boltzmann-naherung.html#stufe-6)) |
| Boltzmann-Faktor | Entropieverlust des Gitters für die Energie $\Delta E$ (Stufe [6](temperatur-und-boltzmann-naherung.html#stufe-6)) |
| $N_\mathrm C\propto T^{3/2}$ | Plätze im Fenster $k_\mathrm BT$ am Rand (Stufe [7](elektronen-und-locher-im-gleichgewicht.html#stufe-7)) |
| $n\,p$ ohne $E_\mathrm F$ | Die Exponenten der Besetzung heben sich auf (Stufe [7](elektronen-und-locher-im-gleichgewicht.html#stufe-7)) |
| $E_\mathrm{F0}>0$ bei $T=0$ | Pauli-Prinzip stapelt die Elektronen im Topf (Stufe [8](erganzung-das-metall-als-potentialtopf.html#stufe-8)) |
