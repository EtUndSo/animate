---
title: Das Wichtigste
pfad: Elektrotechnik / 1. Semester / Grundlagen der Elektrotechnik / Halbleiter und Dioden
order: 1191200
summary: Wie aus Silizium ein Ventil für Strom wird und wie man mit ihm rechnet
tags: 
lang: de
---

:::merke Die Antwort in drei Sätzen
<ol>

<li>

Am pn-Übergang wandern bewegliche Ladungen in das jeweils andere Gebiet und lassen feste Ionen zurück. Deren Feld baut in der Raumladungszone eine Barriere auf, die den Ausgleich stoppt.

</li>

<li>

Wärme hebt nur den Anteil $\mathrm{e}^{-W/(k_\mathrm BT)}$ der Ladungsträger über eine Barriere der Höhe $W$. Spannung in Durchlassrichtung senkt die Barriere, also wächst der Strom exponentiell, je 60 mV um den Faktor 10: $I=I_\mathrm S(\mathrm{e}^{U/U_T}-1)$. In Sperrrichtung bleibt nur der winzige Strom $-I_\mathrm S$.

</li>

<li>

In einer Schaltung liegt der Arbeitspunkt im Schnitt der Kennlinie mit der Arbeitsgerade (der Geraden, die Quelle und Widerstand vorgeben). Für Handrechnungen wird die Diode zum Schalter mit einer festen Durchlassspannung, und für kleine Änderungen um den Arbeitspunkt zum Widerstand $r=U_T/I$.

</li>

</ol>
:::

:::kern Das Wichtigste
<ul>

<li>

Bänder: $W_\mathrm g$ (Silizium 1,12 eV), Anteil $\mathrm{e}^{-W/(k_\mathrm BT)}$; Träger sind Elektronen im LB und Löcher im VB.

</li>

<li>

Dotierung: Donatoren ergeben $n\approx N_\mathrm D$, Akzeptoren $p\approx N_\mathrm A$, überall $n\,p=n_\mathrm i^2$. Der Kristall bleibt neutral.

</li>

<li>

pn-Übergang: Diffusion, Rekombination, feste Ionen, Feld. $U_\mathrm{D0}=U_T\ln(N_\mathrm AN_\mathrm D/n_\mathrm i^2)$.

</li>

<li>

Kennlinie: $I=I_\mathrm S(\mathrm{e}^{U/U_T}-1)$, $U_T=k_\mathrm BT/e=25{,}85$ mV bei 300 K, 60 mV je Dekade, keine Schwelle.

</li>

<li>

Durchbruch ist reversibel, solange die Wärme begrenzt bleibt. Zener-Diode: $U_\mathrm Z$, $r_\mathrm Z$. Kapazitätsdiode: $C_\mathrm{Sp}=\varepsilon A/w$. Photodiode: $I=I_\mathrm S(\mathrm{e}^{U/U_T}-1)-I_\mathrm{Ph}$, Solarzelle $U_\mathrm L=U_T\ln(I_\mathrm{Ph}/I_\mathrm S+1)$.

</li>

<li>

Arbeitspunkt: Schnitt von Kennlinie und Arbeitsgerade $I=(U_0-U_\mathrm D)/R$; iterieren über $U_\mathrm D=U_T\ln(I/I_\mathrm S+1)$.

</li>

<li>

Modelle: leitend $U_\mathrm D=0$ oder $U_\mathrm F$, sperrend $I_\mathrm D=0$. Annehmen, rechnen, prüfen: $I_\mathrm D>0$ und $U_\mathrm D<U_\mathrm F$.

</li>

<li>

Kleinsignal: $r=U_T/I$ für $|u_\mathrm D|\ll U_T$. Nicht verwechseln mit $U_\mathrm D/I$.

</li>

<li>

Brücke: Scheitel $\hat u-2U_\mathrm F$, Lücke bei $|u_\mathrm e|<2U_\mathrm F$. Ladungspumpe: $U_\mathrm a\to2U_\mathrm e-2U_\mathrm F$.

</li>

</ul>
:::

**Ein Prinzip hinter allen Ergebnissen.** Wärme verteilt Energie zufällig, und der Anteil der Teilchen oberhalb einer Energie fällt exponentiell mit dieser Energie. Fast alles in diesem Kapitel folgt daraus, sobald man fragt, welche Energie im jeweiligen Fall zählt.

| Ergebnis | Woher es kommt |
|---|---|
| Reines Silizium leitet kaum | Die Bandlücke (Energie bis zum freien Elektron) ist 43-mal größer als die Wärmeenergie (Stufe [1](warum-silizium-kaum-leitet.html#stufe-1)) |
| Dotierung liefert fast jedes Fremdatom als Ladungsträger | Das Elektron ist nur mit dem 1,7-fachen der Wärmeenergie gebunden (Stufe [2](dotierung.html#stufe-2)) |
| Diffusionsspannung $U_\mathrm{D0}$ | Die Barriere wächst, bis der Anteil darüber dem Dichteverhältnis entspricht (Stufe [3](die-raumladungszone.html#stufe-3)) |
| $I=I_\mathrm S(\mathrm{e}^{U/U_T}-1)$ | Die Spannung verschiebt die Barriere und damit den Anteil (Stufe [4](warum-der-strom-exponentiell-wachst.html#stufe-4)) |
| $U_\mathrm D$ bleibt fast konstant, Schaltermodell | Der Strom ändert sich je 60 mV um den Faktor 10 (Stufe [6](der-arbeitspunkt.html#stufe-6) und [7](lineare-ersatzschaltungen.html#stufe-7)) |
| $r=U_T/I$ | Die Ableitung der Exponentialfunktion ist die Funktion selbst (Stufe [8](kleine-anderungen-um-den-arbeitspunkt.html#stufe-8)) |
