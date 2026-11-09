---
title: Stufe 3: Stern und Dreieck
pfad: Elektrotechnik / 1. Semester / Grundlagen der Elektrotechnik / Quellen und Ersatzquellen
order: 1150500
summary: Eine Brücke ohne Abgleich hat weder Gruppen noch Symmetrie.
tags: Dreieck, Stern, Anlieger, Zweitoren, \pi-Schaltung, T-Schaltung, Dämpfungsglieder
lang: de
---

<span class="anker" id="stufe-3"></span>

:::zweck
Eine Brücke ohne Abgleich hat weder Gruppen noch Symmetrie. Die Stern-Dreieck-Transformation tauscht ein Stück des Netzes so aus, dass Gruppen entstehen.
:::

**Die Idee.** Ein __Dreieck__ sind drei Widerstände zwischen drei Klemmen. Ein __Stern__ sind drei Widerstände von drei Klemmen zu einem gemeinsamen inneren Knoten, dem Sternpunkt. Beide haben drei Klemmen und drei Zahlen. Mit passenden Werten sind sie von außen nicht zu unterscheiden. Der Tausch hilft, weil der Sternpunkt ein neuer Knoten ist, an dem jeder Sternwiderstand in Reihe mit dem Nachbarn dahinter liegt.

:::satz Satz 3.1 (Stern-Dreieck-Transformation)
<span class="anker" id="satz-3-1"></span>

Klemmen 1, 2, 3, Sternpunkt 0. Vom Dreieck zum Stern:

<span class="anker" id="gl-3-1"></span>
$$R_{10}=\frac{R_{12}R_{31}}{R_{12}+R_{23}+R_{31}},\qquad R_{20}=\frac{R_{12}R_{23}}{R_{12}+R_{23}+R_{31}},\qquad R_{30}=\frac{R_{23}R_{31}}{R_{12}+R_{23}+R_{31}}. \tag{3.1}$$

Vom Stern zum Dreieck, mit den Leitwerten $G_{ij}=1/R_{ij}$:

<span class="anker" id="gl-3-2"></span>
$$G_{12}=\frac{G_{10}G_{20}}{G_{10}+G_{20}+G_{30}},\qquad G_{23}=\frac{G_{20}G_{30}}{G_{10}+G_{20}+G_{30}},\qquad G_{31}=\frac{G_{30}G_{10}}{G_{10}+G_{20}+G_{30}}. \tag{3.2}$$
:::

⁠**So liest man das:** $R_{10}$ führt von Klemme 1 zum Sternpunkt, $R_{12}$ von Klemme 1 zu Klemme 2. __Anlieger__ heißen die zwei Elemente, die anliegen: Für $R_{10}$ sind es die Dreiecksseiten an Klemme 1, für $G_{12}$ die Sternzweige an den Klemmen 1 und 2. Als Merksatz: Sternwiderstand = Produkt der Anliegerwiderstände durch den Umfangswiderstand des Dreiecks. Dreiecksleitwert = Produkt der Anliegerleitwerte durch die Summe der Sternleitwerte. Gleichwertig zu [(3.2)](#gl-3-2) ist $R_{12}=R_{10}+R_{20}+R_{10}R_{20}/R_{30}$ mit zyklisch vertauschten Indizes. **Gültigkeit:** Die Gleichheit gilt für jede äußere Beschaltung, aber nur an den drei Klemmen. Der Sternpunkt ist im Original kein Knoten, und die Ströme in den Widerständen selbst unterscheiden sich.

:::herleitung Stern zum Dreieck, dann umkehren
Im Stern gilt am Sternpunkt die Knotenregel $G_{10}(\varphi_1-\varphi_0)+G_{20}(\varphi_2-\varphi_0)+G_{30}(\varphi_3-\varphi_0)=0$. Mit $S=G_{10}+G_{20}+G_{30}$ folgt $\varphi_0=(G_{10}\varphi_1+G_{20}\varphi_2+G_{30}\varphi_3)/S$. Der Strom in Klemme 1 ist damit

$$I_1=G_{10}(\varphi_1-\varphi_0)=\frac{G_{10}G_{20}}{S}(\varphi_1-\varphi_2)+\frac{G_{10}G_{30}}{S}(\varphi_1-\varphi_3).$$

Im Dreieck ist $I_1=G_{12}(\varphi_1-\varphi_2)+G_{31}(\varphi_1-\varphi_3)$. Der Vergleich liefert [(3.2)](#gl-3-2), und zwar für beliebige Potenziale. Klemme 2 liefert entsprechend $G_{23}$.

Für die Umkehrung sei $H=R_{10}R_{20}+R_{20}R_{30}+R_{30}R_{10}$. Dann ist $S=H/(R_{10}R_{20}R_{30})$, und [(3.2)](#gl-3-2) wird zu $R_{12}=H/R_{30}$, $R_{23}=H/R_{10}$, $R_{31}=H/R_{20}$. Daraus folgen $R_{12}R_{31}=H^2/(R_{20}R_{30})$ und $R_{12}+R_{23}+R_{31}=H^2/(R_{10}R_{20}R_{30})$. Der Quotient ist $R_{10}$, das ist [(3.1)](#gl-3-1).
:::

:::abbildung et1/k5bruecke 4
Links eine Brücke ohne Abgleich mit dem Dreieck 1-2-3 (blau). Rechts ist das Dreieck durch einen Stern ersetzt (rot). Jetzt liegen 4 $\Omega$ und 20 $\Omega$ in Reihe, ebenso 8 $\Omega$ und 16 $\Omega$.
:::

::::beispiel
In Abb. [4](#abb-4) ist $R_{12}=10\,\Omega$, $R_{23}=R_{31}=20\,\Omega$, der Umfang beträgt 50 $\Omega$. Aus [(3.1)](#gl-3-1) folgen $R_{10}=4\,\Omega$, $R_{20}=4\,\Omega$, $R_{30}=8\,\Omega$. Die Brücke zerfällt in Gruppen:

$$R_\mathrm{AB}=4\,\Omega+(4\,\Omega+20\,\Omega)\parallel(8\,\Omega+16\,\Omega)=4\,\Omega+12\,\Omega=16\,\Omega.$$
::::

⁠**Kontrolle** an den Klemmen 1, 2 bei offener Klemme 3: Der Stern hat $4+4=8\,\Omega$, das Dreieck $10\,\Omega\parallel40\,\Omega=8\,\Omega$. **Grenzfälle:** Drei gleiche Dreieckswiderstände ergeben einen Stern mit einem Drittel des Werts. Für $R_{12}\to0$ gehen $R_{10}$ und $R_{20}$ gegen null, und $R_{30}$ wird $R_{23}\parallel R_{31}$, genau das, was das kurzgeschlossene Dreieck ist.

**$\pi$ und T.** Bei __Zweitoren__ ([Teil 6](/wissen/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/zweitore/zweitore.html)) zeichnet man Dreieck und Stern so, dass ein Eingang links und ein Ausgang rechts liegen. Das Dreieck heißt dann __$\pi$-Schaltung__, der Stern __T-Schaltung__. Formeln und Regeln bleiben. In der Nachrichtentechnik baut man so __Dämpfungsglieder__, die ein Signal um einen festen Faktor abschwächen und an beiden Klemmenpaaren denselben Eingangswiderstand zeigen (Leistungsanpassung, [Teil 7](/wissen/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/leistung-anpassung-und-wirkungsgrad/leistung-und-anpassung.html)). Auch Filter aus Spulen und Kondensatoren lassen sich wahlweise in der einen oder der anderen Form bauen.

:::frage Welches Dreieck soll ich umwandeln?
Jedes, nach dessen Umwandlung Gruppen entstehen. In einer Brücke geht auch das untere Dreieck oder sogar ein Stern, der in ein Dreieck verwandelt wird. Das Ergebnis ist immer dasselbe.
:::

:::aufgabe Aufgabe 4 ★★ Hin und zurück
<span class="anker" id="aufg-4"></span>

(a) Drei Widerstände von je 12 $\Omega$ bilden ein Dreieck. Wie groß sind die Sternwiderstände? (b) In einer Brücke seien die drei oberen Widerstände (Dreieck A, C, D) je 6 $\Omega$, von C führen 1 $\Omega$ und von D 4 $\Omega$ nach B. Berechne $R_\mathrm{AB}$. (c) Wandle den Stern $R_{10}=5\,\Omega$, $R_{20}=R_{30}=10\,\Omega$ in ein Dreieck um, einmal mit [(3.2)](#gl-3-2) und einmal mit der Widerstandsform.

:::loesung
(a) Umfang 36 $\Omega$, $R_\mathrm{Stern}=\frac{12\cdot12}{36}\,\Omega=4\,\Omega$, ein Drittel des Dreieckswerts.

(b) Das Dreieck wird zu drei Sternwiderständen mit je 2 $\Omega$. Dann ist $R_\mathrm{AB}=2\,\Omega+(2\,\Omega+1\,\Omega)\parallel(2\,\Omega+4\,\Omega)=2\,\Omega+3\,\Omega\parallel6\,\Omega=4\,\Omega$.

(c) Leitwerte 0,2 S, 0,1 S, 0,1 S, Summe 0,4 S. $G_{12}=\frac{0{,}2\cdot0{,}1}{0{,}4}$ S $=0{,}05$ S, $G_{23}=0{,}025$ S, $G_{31}=0{,}05$ S. Das sind $R_{12}=20\,\Omega$, $R_{23}=40\,\Omega$, $R_{31}=20\,\Omega$. Widerstandsform: $R_{12}=5+10+\frac{5\cdot10}{10}=20\,\Omega$, $R_{23}=10+10+\frac{10\cdot10}{5}=40\,\Omega$, $R_{31}=10+5+\frac{10\cdot5}{10}=20\,\Omega$.
:::
:::
