---
title: Das Wichtigste
pfad: Elektrotechnik / 1. Semester / ET1 – Grundgebiete der Elektrotechnik 1: Einführung in die Schaltungsanalyse / Der Kondensator
adresse: elektrotechnik/1-semester/grundlagen-der-elektrotechnik/der-kondensator
knoten: Kapitel 3: Der Kondensator
order: 1131200
summary: Wie Strom in einen Isolator fließt und wo danach die Energie steckt
tags: Feldenergie, Zeitkonstante
lang: de
---

:::merke Die Antwort in drei Sätzen
<ol>

<li>

Ein Kondensator lässt Ladung nicht durch, er verschiebt sie: Elektronen verlassen die eine Platte und kommen auf der anderen an, und an beiden Anschlüssen fließt im selben Moment derselbe Strom.

</li>

<li>

Die getrennte Ladung $Q$ erzeugt das Feld zwischen den Platten. Dieses Feld bestimmt die Spannung $U=Q/C$, und in ihm steckt die __Feldenergie__ $\frac12CU^2$, gespeichert im Raum zwischen den Platten.

</li>

<li>

Ladung braucht Strom und Zeit, also springt die Spannung nicht. Der leere Kondensator wirkt im ersten Moment wie ein Kurzschluss (Strom bei 0 V), der volle wie eine Unterbrechung (Spannung ohne Strom). Dazwischen läuft eine Exponentialkurve mit der __Zeitkonstante__ $\tau=RC$, der Zeit, die den Takt des Ladens vorgibt.

</li>

</ol>
:::

:::kern Das Wichtigste
<ul>

<li>

Der Kondensator trennt Ladung: $+Q$ und $-Q$, Gesamtladung null. An beiden Anschlüssen fließt derselbe Strom, durch die Lücke keine Ladung.

</li>

<li>

Kapazität: $C=Q/U$; $i=C\,\mathrm{d} u/\mathrm{d} t$; $u(t)=u(t_0)+\frac1C\int_{t_0}^ti\,\mathrm{d} t'$. $u$ springt nicht, Gleichstrom wird gesperrt.

</li>

<li>

Plattenkondensator: $C=\varepsilon A/d$ mit $\varepsilon=\varepsilon_0\varepsilon_\mathrm{r}$, $\varepsilon_0=8{,}854\cdot10^{-12}$ A s/(V m).

</li>

<li>

Energie: $W=\frac12CU^2=\frac12QU=Q^2/(2C)$, im Feld mit der Dichte $w=\frac12\varepsilon E^2$.

</li>

<li>

Parallel: $C_\mathrm{G}=\sum C_i$. Reihe: $1/C_\mathrm{G}=\sum1/C_i$.

</li>

<li>

Insel: $Q_\mathrm{ges}=\sum C_iU_i=$ const. Die Energie bleibt dabei nicht erhalten.

</li>

<li>

Laden: $u_C=U_0(1-\mathrm{e}^{-t/\tau})$, $i=\frac{U_0}{R}\mathrm{e}^{-t/\tau}$. Entladen: $u_C=U_0\,\mathrm{e}^{-t/\tau}$, $i=-\frac{U_0}{R}\mathrm{e}^{-t/\tau}$. Zeitkonstante $\tau=RC$.

</li>

<li>

Allgemein: $u_C(t)=u_\infty+(u_C(0)-u_\infty)\,\mathrm{e}^{-t/\tau}$. Leer wirkt er im ersten Moment wie ein Kurzschluss, voll wie eine Unterbrechung.

</li>

</ul>
:::

**Ein Prinzip hinter allen Ergebnissen.** Die Spannung zeigt an, wie viel Ladung getrennt ist, und Ladung ändert sich nur durch Strom. Aus diesen beiden Tatsachen, $u=q/C$ und $i=\mathrm{d} q/\mathrm{d} t$, folgen alle Ergebnisse dieses Kapitels.

| Ergebnis | Woher es kommt |
|---|---|
| Strom trotz Lücke | Ladung wird verschoben, nicht durchgereicht (Stufe [1](warum-strom-in-einen-isolator-fliet.html#stufe-1)) |
| $Q=CU$ | doppelte Ladung, doppeltes Feld, doppelte Spannung (Stufe [2](die-kapazitat.html#stufe-2)) |
| $i=C\,\mathrm{d} u/\mathrm{d} t$, $u$ springt nicht | Strom ist Ladung je Zeit (Stufe [3](strom-und-spannung-am-kondensator.html#stufe-3)) |
| $C=\varepsilon A/d$ | Feld je Ladung hängt an Fläche, Abstand und Stoff (Stufe [4](plattenkondensator-und-dielektrikum.html#stufe-4)) |
| Bauformen | $A$ groß, $d$ klein, $\varepsilon$ groß (Stufe [5](bauformen-und-selbstentladung.html#stufe-5)) |
| $W=\frac12CU^2$ | jede weitere Ladung läuft gegen die schon vorhandene Spannung (Stufe [6](die-gespeicherte-energie.html#stufe-6)) |
| Parallel- und Reihenschaltung | gleiche Spannung oder gleiche Ladung (Stufe [7](parallel-und-reihenschaltung.html#stufe-7)) |
| Umladen | Ladung kann eine Insel nicht verlassen (Stufe [8](ladungserhaltung-beim-umschalten.html#stufe-8)) |
| Kurzschluss, Unterbrechung, Exponentialkurve | der Strom hängt an der Spannung, die er selbst aufbaut (Stufe [9](aufladen-uber-einen-widerstand.html#stufe-9)) |
| Entladen, $\tau=RC$ | dieselbe Rückkopplung mit anderem Startwert (Stufe [10](entladen-und-zeitkonstante.html#stufe-10)) |
