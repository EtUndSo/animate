---
title: Das Wichtigste
pfad: Elektrotechnik / 1. Semester / ET1 – Grundgebiete der Elektrotechnik 1: Einführung in die Schaltungsanalyse / Strom und Spannung messen
adresse: elektrotechnik/1-semester/grundlagen-der-elektrotechnik/strom-und-spannung-messen
knoten: Kapitel 4: Strom und Spannung messen
order: 1140900
summary: Warum jedes Messgerät die Schaltung verändert und wie man trotzdem genau misst
tags: Amperemeter, Voltmeter, stromrichtige Messung, spannungsrichtige Messung, Wheatstonesche Messbrücke, Abgleich
lang: de
---

:::merke Die Antwort in drei Sätzen
<ol>

<li>

Ein __Amperemeter__ (Strommesser) liegt in Reihe im Stromkreis und fügt ihm seinen Innenwiderstand hinzu. Ein __Voltmeter__ (Spannungsmesser) liegt parallel und öffnet einen zweiten Strompfad. Beide zeigen den Wert der veränderten Schaltung.

</li>

<li>

Der relative Fehler ist rund $R_\mathrm i/R$ beim Amperemeter und rund $R/R_\mathrm i$ beim Voltmeter. Misst man beide zugleich, stimmt nur eine Anzeige: __stromrichtige Messung__ (der Strom stimmt) oder __spannungsrichtige Messung__ (die Spannung stimmt).

</li>

<li>

Die __Wheatstonesche Messbrücke__ (zwei Spannungsteiler an einer Quelle, dazwischen ein Instrument) vergleicht Widerstände. Im __Abgleich__ (eingestellt auf Anzeige null) fließt durch das Instrument kein Strom. Deshalb fallen sein Innenwiderstand, seine Skala und die Quellspannung aus dem Ergebnis $R_4=R_3R_2/R_1$ heraus.

</li>

</ol>
:::

:::kern Das Wichtigste
<ul>

<li>

Ein Messgerät ist ein Widerstand und zeigt den Wert der veränderten Schaltung.

</li>

<li>

Amperemeter: $I_R/I_R'=1+R_\mathrm i/R$. Voltmeter: $U_L/U_L'=1+R_L/R_\mathrm i$.

</li>

<li>

Bereich erweitern: $R_\mathrm{Shunt}=R_\mathrm{alt}I_\mathrm{alt}/(I_\mathrm{neu}-I_\mathrm{alt})$ und $R_\mathrm V=R_\mathrm{alt}(\alpha-1)$.

</li>

<li>

Stromrichtig $U/I=R+R_\mathrm{iA}$ für große, spannungsrichtig $U/I=R\parallel R_\mathrm{iV}$ für kleine $R$.

</li>

<li>

Abgleich: $R_4=R_3R_2/R_1$, unabhängig von Innenwiderstand, Skala und Quellspannung.

</li>

<li>

Verstimmt: $U_\mathrm d\approx\frac14U_\mathrm q\,\Delta R/R$. Ohne die gemeinsame Spannung reicht ein kleiner Bereich.

</li>

</ul>
:::

**Ein Prinzip hinter allen Ergebnissen.** Für die Schaltung ist ein Messgerät ein weiterer Widerstand. Alle Fehler folgen aus denselben Regeln wie in [Kapitel 2](/wissen/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/strom-widerstand-und-kirchhoff/strom-widerstand-und-kirchhoff.html): Maschenregel, Knotenregel, ohmsches Gesetz.

| Ergebnis | Woher es kommt |
|---|---|
| Innenwiderstand | Das Instrument braucht Strom, seine Spule hat Widerstand (Stufe [1](das-messgerat-ist-ein-bauteil.html#stufe-1)) |
| Neben- und Vorwiderstand | Stromteiler und Spannungsteiler schützen das Instrument (Stufe [2](den-messbereich-erweitern.html#stufe-2)) |
| $I_R'=U/(R+R_\mathrm i)$ | Ein Widerstand mehr in der Masche (Stufe [3](der-fehler-beim-strommessen.html#stufe-3)) |
| $U_L'=U_L/(1+R_L/R_\mathrm i)$ | Ein Zweig mehr am Knoten (Stufe [4](der-fehler-beim-spannungsmessen.html#stufe-4)) |
| Strom- und spannungsrichtig | Jedes Instrument liegt im Messkreis des anderen (Stufe [5](strom-und-spannung-zugleich.html#stufe-5)) |
| Abgleich $R_4=R_3R_2/R_1$ | Ohne Strom entnimmt das Instrument der Brücke nichts (Stufe [6](die-wheatstonesche-brucke.html#stufe-6)) |
| $U_\mathrm d\approx\frac14U_\mathrm q\,\Delta R/R$ | Die Brücke zieht die gemeinsame Spannung ab (Stufe [7](die-verstimmte-brucke.html#stufe-7)) |
