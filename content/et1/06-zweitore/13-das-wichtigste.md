---
title: Das Wichtigste
pfad: Elektrotechnik / 1. Semester / ET1 – Grundgebiete der Elektrotechnik 1: Einführung in die Schaltungsanalyse / Zweitore
adresse: elektrotechnik/1-semester/grundlagen-der-elektrotechnik/zweitore
knoten: Kapitel 6: Zweitore
order: 1161300
summary: Warum vier Zahlen ein ganzes Netzwerk ersetzen und jede Parameterform nur eine andere Wahl ist
tags: Torbedingung, Zweitorparameter, Impedanzform, Admittanzform, Hybridform, Kettenform
lang: de
---

:::merke Die Antwort in drei Sätzen
<ol>

<li>

In jedem Tor fließt der Strom, der in die eine Klemme hineinfließt, aus der anderen wieder heraus (__Torbedingung__). Von außen bleiben deshalb zwei Spannungen und zwei Ströme.

</li>

<li>

In einem linearen Zweitor ohne eigene Quellen legen zwei dieser vier Größen die anderen beiden fest. Jede abhängige Größe ist eine Summe aus zwei Anteilen, deshalb reichen vier Zahlen, die __Zweitorparameter__.

</li>

<li>

Die __Impedanzform__ (Ströme gegeben), die __Admittanzform__ (Spannungen gegeben), die __Hybridform__ (Eingangsstrom und Ausgangsspannung gegeben) und die __Kettenform__ (Ausgangsgrößen gegeben) beschreiben dasselbe Zweitor. Leerlauf und Kurzschluss setzen eine gegebene Größe null und legen so die Parameter einzeln frei.

</li>

</ol>
:::

:::kern Das Wichtigste
<ul>

<li>

Zweitor: vier Klemmen, Torbedingung $I_{1'}=-I_1$, $I_{2'}=-I_2$. Torgrößen $U_1$, $I_1$, $U_2$, $I_2$, Strompfeile zeigen hinein.

</li>

<li>

Linear, ohne eigene Quellen: zwei Größen legen die anderen fest, vier Parameter.

</li>

<li>

Z: $\mathbf U=\mathbf Z\,\mathbf I$, Leerlaufversuche. Y: $\mathbf I=\mathbf Y\,\mathbf U$, Kurzschlussversuche. $\mathbf Y=\mathbf Z^{-1}$.

</li>

<li>

H: $(U_1,I_2)$ aus $(I_1,U_2)$. A: $(U_1,I_1)$ aus $(U_2,-I_2)$.

</li>

<li>

Ein Parameter ist ein Quotient aus Wirkung und Ursache, bei null gesetzter anderer Ursache. $I=0$ heißt Leerlauf, $U=0$ heißt Kurzschluss.

</li>

<li>

Eigener Strom ergibt Widerstand, fremder Strom oder fremde Spannung ergibt gesteuerte Quelle. Spannungen addieren sich in Reihe, Ströme parallel.

</li>

<li>

Last: $Z_1=Z_{11}-\frac{Z_{12}Z_{21}}{Z_{22}+Z_\mathrm{L}}$, $Y_1=Y_{11}-\frac{Y_{12}Y_{21}}{Y_{22}+Y_\mathrm{L}}$.

</li>

<li>

T: $\mathbf Z$ mit $R_\mathrm{a}+R_\mathrm{b}$, $R_\mathrm{b}$, $R_\mathrm{b}+R_\mathrm{c}$. $\pi$: $\mathbf Y$ mit $G_1+G_2$, $-G_2$, $G_2+G_3$. Umrechnung Stern-Dreieck.

</li>

<li>

Reihe, Reihe: Z addiert. Parallel, parallel: Y addiert. Reihe, parallel: H addiert. Kette: A multipliziert. Voraussetzung: Torbedingung bleibt.

</li>

<li>

Umkehrbar: $Z_{12}=Z_{21}$, $Y_{12}=Y_{21}$, $H_{12}=-H_{21}$, $\det\mathbf A=1$. Rückwirkungsfrei: $Z_{12}=Y_{12}=H_{12}=0$, $\det\mathbf A=0$.

</li>

<li>

Leistung: $P=U_1I_1+U_2I_2$, aktiv, wenn $P<0$ möglich ist.

</li>

</ul>
:::

**Ausblick auf [Kapitel 7](/wissen/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/leistung-anpassung-und-wirkungsgrad/leistung-und-anpassung.html).** Die Leistung $P$ aus Stufe [10](eigenschaften-und-alle-formen-im-uberblick.html#stufe-10) führt zur nächsten Frage: Bei welcher Last gibt eine Quelle oder ein Zweitor die größte Leistung ab, und was kostet das an Wirkungsgrad?

**Ein Prinzip hinter allen Ergebnissen.** Von vier Torgrößen wählt man zwei als Ursachen, die anderen zwei sind die Wirkungen. Diese Wahl ändert nichts am Zweitor, nur an der Rechnung, und jedes Ergebnis folgt aus ihr.

| Ergebnis | Woher es kommt |
|---|---|
| Vier Torgrößen statt sechs | Ein Zweipol an jedem Klemmenpaar gibt die Ladung, die er abgibt, an der anderen Klemme zurück (Stufe [1](vom-vierpol-zum-zweitor.html#stufe-1)) |
| Vier Parameter | Überlagerung: zwei Ursachen mal zwei Wirkungen (Stufe [2](vier-groen-zwei-gleichungen-vier-zahlen.html#stufe-2)) |
| Z-Parameter aus Leerlaufversuchen | Ursachen sind Ströme, ein offenes Tor setzt einen Strom null (Stufe [3](impedanzform-und-leerlaufversuch.html#stufe-3)) |
| Eingangswiderstand hängt von der Last ab | Die zweite Ursache $I_2$ wirkt über $Z_{12}$ auf den Eingang zurück (Stufe [4](das-zweitor-im-betrieb.html#stufe-4)) |
| Y-Parameter aus Kurzschlussversuchen | Ursachen sind Spannungen, ein Draht setzt eine Spannung null (Stufe [5](admittanzform-und-kurzschlussversuch.html#stufe-5)) |
| $\mathbf Y=\mathbf Z^{-1}$, T und $\pi$ | Dieselben zwei Gleichungen, nach den anderen zwei Größen aufgelöst (Stufe [6](umrechnen-t-und.html#stufe-6)) |
| Hybridform | Ursachen gemischt, passend zu Bauteilen mit Stromeingang und Stromquellenausgang (Stufe [7](hybridform.html#stufe-7)) |
| Kettenform, Matrixprodukt | Die Ursachen einer Stufe sind die Wirkungen der nächsten (Stufe [8](kettenform.html#stufe-8)) |
| Z, Y, H addieren sich | Was beide Teile teilen, gehört zu den Ursachen, was sich summiert, zu den Wirkungen (Stufe [9](zusammenschaltung.html#stufe-9)) |
| Umkehrbar, rückwirkungsfrei, aktiv | Beziehungen zwischen den vier Zahlen und ihren Vorzeichen (Stufe [10](eigenschaften-und-alle-formen-im-uberblick.html#stufe-10)) |
