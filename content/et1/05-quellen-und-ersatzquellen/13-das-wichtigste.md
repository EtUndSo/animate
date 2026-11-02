---
title: Das Wichtigste
pfad: Elektrotechnik / 1. Semester / Grundlagen der Elektrotechnik / Quellen und Ersatzquellen
order: 1151300
summary: Warum zwei Zahlen ein ganzes Netzwerk ersetzen
tags: Superposition, Leerlaufspannung, Innenwiderstand, Ersatzquelle, Kurzschluss
lang: de
---

:::merke Die Antwort in drei Sätzen
<ol>

<li>

In einem linearen Netzwerk addieren sich die Wirkungen der Quellen, denn alle Gleichungen sind linear. Das ist die __Superposition__, die Überlagerung.

</li>

<li>

Daher ist die Spannung an zwei Klemmen A und B eine Gerade im Klemmenstrom: $U_\mathrm{AB}=U_\mathrm{LL}-R_\mathrm{i}\,I_\mathrm{A}$. Die Quellen legen die __Leerlaufspannung__ $U_\mathrm{LL}$ fest (Spannung bei offenen Klemmen), die Widerstände den __Innenwiderstand__ $R_\mathrm{i}$ (die Neigung).

</li>

<li>

Eine Gerade hat zwei Zahlen. Das Netzwerk verhält sich also wie eine __Ersatzquelle__, eine Quelle mit Innenwiderstand. Leerlauf und __Kurzschluss__ (verbundene Klemmen) liefern die Zahlen: $R_\mathrm{i}=U_\mathrm{LL}/I_\mathrm{KS}$.

</li>

</ol>
:::

:::kern Das Wichtigste
<ul>

<li>

Reihe: Widerstände addieren, gleicher Strom. Parallel: Leitwerte addieren, gleiche Spannung. Von innen nach außen zusammenfassen.

</li>

<li>

Knoten gleichen Potenzials darf man verbinden, stromlose Zweige auftrennen. Symmetrie zeigt, wo das geht.

</li>

<li>

Stern und Dreieck sind an den Klemmen austauschbar: $R_{10}=R_{12}R_{31}/(R_{12}+R_{23}+R_{31})$.

</li>

<li>

Ideale Quellen halten eine Größe fest. Reale Quellen: $U_\mathrm{AB}=U_\mathrm{q}-R_\mathrm{q}I_\mathrm{A}$. Umwandeln: $I_\mathrm{q}=U_\mathrm{q}/R_\mathrm{q}$, gleicher Widerstand.

</li>

<li>

Überlagerung: Spannungsquellen werden Drähte, Stromquellen Lücken, Teilwirkungen addieren sich. Leistungen addieren sich nicht.

</li>

<li>

Jedes lineare Eintor ist eine Gerade: $U_\mathrm{i}=U_\mathrm{LL}$, $I_\mathrm{i}=I_\mathrm{KS}$, $R_\mathrm{i}=U_\mathrm{LL}/I_\mathrm{KS}$. Der Arbeitspunkt ist der Schnitt mit der Geraden der Last.

</li>

</ul>
:::

**Ein Prinzip hinter allen Ergebnissen.** Ein lineares Netzwerk verhält sich an zwei Klemmen wie eine einzige Gerade im Strom-Spannungs-Diagramm, deshalb reichen zwei Zahlen. Von außen zählt nur diese Kennlinie: Zwei Schaltungen mit gleicher Geraden sind austauschbar, ganz gleich, wie sie innen aussehen. Die Tabelle ordnet die Ergebnisse diesem Gedanken zu.

| Ergebnis | Woher es kommt |
|---|---|
| Gesamtwiderstand | Ohne Quelle geht die Kennlinie durch den Ursprung, eine Zahl reicht (Stufe [1](widerstande-zusammenfassen.html#stufe-1)) |
| Symmetrie, Halbschaltung | Gleiche Potenziale darf man verbinden, stromlose Zweige auftrennen (Stufe [2](symmetrie-nutzen.html#stufe-2)) |
| Stern und Dreieck | Drei Klemmen, drei Zahlen, also austauschbar (Stufe [3](stern-und-dreieck.html#stufe-3)) |
| Ideale Quellen | Grenzfälle der Geraden: waagerecht und senkrecht (Stufe [4](ideale-quellen.html#stufe-4)) |
| Arbeitspunkt | Schnitt der Quellengeraden mit der Lastgeraden (Stufe [5](reale-quellen-und-der-arbeitspunkt.html#stufe-5)) |
| Umwandeln von Quellen | Dieselbe Gerade, von der anderen Achse aus gelesen (Stufe [6](spannungsquelle-oder-stromquelle.html#stufe-6)) |
| Quellen zusammenschalten | Geraden addieren sich in Spannung oder in Strom (Stufe [7](quellen-zusammenschalten.html#stufe-7)) |
| Überlagerung | Lineare Gleichungen, jede Quelle wirkt für sich (Stufe [8](uberlagerung.html#stufe-8)) |
| Thevenin und Norton | Überlagerung mit dem Klemmenstrom als weiterer Ursache (Stufe [9](thevenin-und-norton.html#stufe-9)) |
| R-2R-Wandler | Jeder Schalter ist eine Quelle, jede Sprosse halbiert (Stufe [10](der-r-2r-wandler.html#stufe-10)) |
