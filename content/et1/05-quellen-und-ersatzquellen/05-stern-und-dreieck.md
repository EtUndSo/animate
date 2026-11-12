---
title: Stufe 3: Stern und Dreieck
pfad: Elektrotechnik / 1. Semester / ET1 – Grundgebiete der Elektrotechnik 1: Einführung in die Schaltungsanalyse / Quellen und Ersatzquellen
adresse: elektrotechnik/1-semester/grundlagen-der-elektrotechnik/quellen-und-ersatzquellen
knoten: Kapitel 5: Quellen und Ersatzquellen
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

**$\pi$ und T.** Bei __Zweitoren__ ([Kapitel 6](/wissen/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/zweitore/zweitore.html)) zeichnet man Dreieck und Stern so, dass ein Eingang links und ein Ausgang rechts liegen. Das Dreieck heißt dann __$\pi$-Schaltung__, der Stern __T-Schaltung__. Formeln und Regeln bleiben. In der Nachrichtentechnik baut man so __Dämpfungsglieder__, die ein Signal um einen festen Faktor abschwächen und an beiden Klemmenpaaren denselben Eingangswiderstand zeigen (Leistungsanpassung, [Kapitel 7](/wissen/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/leistung-anpassung-und-wirkungsgrad/leistung-und-anpassung.html)). Auch Filter aus Spulen und Kondensatoren lassen sich wahlweise in der einen oder der anderen Form bauen.

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

::::formelsammlung
**Dreieck zum Stern**

$$R_{10}=\frac{R_{12}R_{31}}{R_{12}+R_{23}+R_{31}},\qquad R_{20}=\frac{R_{12}R_{23}}{R_{12}+R_{23}+R_{31}},\qquad R_{30}=\frac{R_{23}R_{31}}{R_{12}+R_{23}+R_{31}}$$

Klemmen 1, 2, 3, Sternpunkt 0; $R_{10}$ führt von Klemme 1 zum Sternpunkt, $R_{12}$ von Klemme 1 zu Klemme 2. Sternwiderstand = Produkt der Anliegerwiderstände (Dreiecksseiten an der Klemme) durch den Umfangswiderstand des Dreiecks. Drei gleiche Dreieckswiderstände ergeben einen Stern mit einem Drittel des Werts.

**Stern zum Dreieck**

$$G_{12}=\frac{G_{10}G_{20}}{G_{10}+G_{20}+G_{30}},\qquad G_{23}=\frac{G_{20}G_{30}}{G_{10}+G_{20}+G_{30}},\qquad G_{31}=\frac{G_{30}G_{10}}{G_{10}+G_{20}+G_{30}}$$

Mit $G_{ij}=1/R_{ij}$. Dreiecksleitwert = Produkt der Anliegerleitwerte (Sternzweige an beiden Klemmen) durch die Summe der Sternleitwerte. Die Gleichheit gilt für jede äußere Beschaltung, aber nur an den drei Klemmen; die Ströme in den Widerständen selbst unterscheiden sich.

**Stern zum Dreieck, Widerstandsform**

$$R_{12}=R_{10}+R_{20}+R_{10}R_{20}/R_{30}$$

Gleichwertig zur Leitwertform; $R_{23}$ und $R_{31}$ mit zyklisch vertauschten Indizes.
::::

::::lernkarten
:::karte begriff Dreieck und Stern
Was unterscheidet ein Dreieck von einem Stern aus drei Widerständen, und was haben beide gemeinsam?
---
Ein Dreieck sind drei Widerstände zwischen drei Klemmen, ein Stern drei Widerstände von drei Klemmen zu einem gemeinsamen inneren Knoten, dem Sternpunkt. Beide haben drei Klemmen und drei Zahlen; mit passenden Werten sind sie von außen nicht zu unterscheiden.
--- falsch
Ein Dreieck sind drei Widerstände in Reihe zwischen zwei Klemmen, ein Stern drei parallele Widerstände zwischen denselben zwei Klemmen. Gemeinsam ist beiden nur der Gesamtwiderstand, den man an diesen Klemmen misst.
--- falsch
Ein Dreieck sind drei Widerstände von drei Klemmen zu einem inneren Knoten, ein Stern drei Widerstände zwischen drei Klemmen. Beide haben drei Klemmen, sind von außen aber nur bei gleichen Werten nicht zu unterscheiden.
--- falsch
Ein Dreieck sind drei Widerstände zwischen drei Klemmen, ein Stern hat zusätzlich einen vierten Widerstand im Sternpunkt. Wegen dieser vierten Zahl ist der Stern allgemeiner und kann jedes Dreieck ersetzen, aber nicht umgekehrt, weil dem Dreieck eine Zahl fehlt.
:::
:::karte formel Dreieck zum Stern
Wie berechnet man aus einem Dreieck mit $R_{12}$, $R_{23}$, $R_{31}$ den Sternwiderstand $R_{10}$ an Klemme 1?
---
$R_{10}=\frac{R_{12}R_{31}}{R_{12}+R_{23}+R_{31}}$: Produkt der Anliegerwiderstände, der beiden Dreiecksseiten an Klemme 1, durch den Umfangswiderstand des Dreiecks. $R_{20}$ und $R_{30}$ folgen entsprechend.
--- falsch
$R_{10}=\frac{R_{12}R_{23}}{R_{12}+R_{23}+R_{31}}$: Produkt der beiden Dreiecksseiten, die an Klemme 2 liegen, durch den Umfangswiderstand des Dreiecks. $R_{20}$ und $R_{30}$ folgen entsprechend durch zyklisches Vertauschen.
--- falsch
$R_{10}=R_{12}+R_{31}$: Der Sternwiderstand ist die Reihe der beiden Dreiecksseiten an Klemme 1, weil der Strom von Klemme 1 über beide Seiten weiterfließt.
--- falsch
$R_{10}=\frac{R_{12}+R_{23}+R_{31}}{R_{12}R_{31}}$: Umfangswiderstand des Dreiecks durch das Produkt der Anliegerwiderstände an Klemme 1. $R_{20}$ und $R_{30}$ folgen entsprechend.
:::
:::karte formel Stern zum Dreieck
Wie berechnet man aus einem Stern mit den Leitwerten $G_{10}$, $G_{20}$, $G_{30}$ den Dreiecksleitwert $G_{12}$, und wie lautet die gleichwertige Widerstandsform?
---
$G_{12}=\frac{G_{10}G_{20}}{G_{10}+G_{20}+G_{30}}$: Produkt der Anliegerleitwerte durch die Summe der Sternleitwerte. Gleichwertig ist $R_{12}=R_{10}+R_{20}+R_{10}R_{20}/R_{30}$, die übrigen mit zyklisch vertauschten Indizes.
--- falsch
$G_{12}=\frac{G_{10}G_{20}}{G_{10}+G_{20}+G_{30}}$: Produkt der Anliegerleitwerte durch die Summe der Sternleitwerte. Gleichwertig ist $R_{12}=\frac{R_{10}R_{20}}{R_{10}+R_{20}+R_{30}}$, dieselbe Form wie vom Dreieck zum Stern.
--- falsch
$G_{12}=G_{10}+G_{20}$: Die Sternzweige an den Klemmen 1 und 2 liegen zwischen diesen Klemmen parallel. Gleichwertig ist $R_{12}=R_{10}\parallel R_{20}$, die übrigen mit zyklisch vertauschten Indizes.
--- falsch
$G_{12}=\frac{G_{30}}{G_{10}+G_{20}+G_{30}}$: der gegenüberliegende Leitwert durch die Summe der Sternleitwerte. Gleichwertig ist $R_{12}=R_{10}+R_{20}$, weil der Strom von 1 nach 2 durch zwei Sternzweige fließt.
:::
:::karte begriff Anlieger
Welche Elemente heißen bei der Stern-Dreieck-Transformation Anlieger, etwa für $R_{10}$ und für $G_{12}$?
---
Die zwei Elemente, die anliegen: Für den Sternwiderstand $R_{10}$ sind es die Dreiecksseiten an Klemme 1, für den Dreiecksleitwert $G_{12}$ die Sternzweige an den Klemmen 1 und 2.
--- falsch
Die zwei Elemente, die gegenüberliegen: Für den Sternwiderstand $R_{10}$ ist es die Dreiecksseite zwischen den Klemmen 2 und 3, für $G_{12}$ der Sternzweig an Klemme 3.
--- falsch
Die Widerstände, die außen an den Klemmen angeschlossen sind und weder zum Stern noch zum Dreieck gehören, etwa die Last an Klemme 1 bei der Berechnung des Sternwiderstands $R_{10}$.
--- falsch
Die zwei Elemente, die anliegen: Für den Sternwiderstand $R_{10}$ sind es die Sternzweige an den Klemmen 2 und 3, für $G_{12}$ die Dreiecksseiten an Klemme 1.
:::
:::karte herleitung Stern zum Dreieck
Leite aus der Knotenregel am Sternpunkt die Formel für den Dreiecksleitwert $G_{12}$ her.
---
Am Sternpunkt gilt $G_{10}(\varphi_1-\varphi_0)+G_{20}(\varphi_2-\varphi_0)+G_{30}(\varphi_3-\varphi_0)=0$, weil dort nur die drei Sternzweige angeschlossen sind und keine Ladung verloren geht.
---
Mit $S=G_{10}+G_{20}+G_{30}$ folgt $\varphi_0=(G_{10}\varphi_1+G_{20}\varphi_2+G_{30}\varphi_3)/S$, weil man die Gleichung nach $\varphi_0$ auflöst.
---
Der Strom in Klemme 1 ist $I_1=G_{10}(\varphi_1-\varphi_0)=\frac{G_{10}G_{20}}{S}(\varphi_1-\varphi_2)+\frac{G_{10}G_{30}}{S}(\varphi_1-\varphi_3)$, weil man $\varphi_0$ einsetzt und nach Potenzialdifferenzen ordnet.
---
Im Dreieck ist $I_1=G_{12}(\varphi_1-\varphi_2)+G_{31}(\varphi_1-\varphi_3)$, weil an Klemme 1 die beiden Dreiecksseiten zu den Klemmen 2 und 3 hängen.
---
Der Vergleich liefert $G_{12}=\frac{G_{10}G_{20}}{G_{10}+G_{20}+G_{30}}$, weil beide Ausdrücke für beliebige Potenziale gleich sein müssen und deshalb die Faktoren vor $(\varphi_1-\varphi_2)$ übereinstimmen.
:::
:::karte herleitung Dreieck zum Stern durch Umkehren
Leite aus den Formeln für die Umwandlung vom Stern zum Dreieck die Formel für den Sternwiderstand $R_{10}$ her.
---
Man setzt $H=R_{10}R_{20}+R_{20}R_{30}+R_{30}R_{10}$; dann ist $S=H/(R_{10}R_{20}R_{30})$, weil die Summe der Sternleitwerte, auf den Hauptnenner gebracht, genau diesen Bruch ergibt.
---
Die Formeln vom Stern zum Dreieck werden zu $R_{12}=H/R_{30}$, $R_{23}=H/R_{10}$, $R_{31}=H/R_{20}$, weil man jeden Dreiecksleitwert umkehrt und $S$ einsetzt.
---
Daraus folgen $R_{12}R_{31}=H^2/(R_{20}R_{30})$ und $R_{12}+R_{23}+R_{31}=H^2/(R_{10}R_{20}R_{30})$, weil die drei Brüche auf dem Hauptnenner im Zähler wieder $H$ mal $H$ ergeben.
---
Der Quotient ist $R_{10}=\frac{R_{12}R_{31}}{R_{12}+R_{23}+R_{31}}$, weil sich $H^2$ und $R_{20}R_{30}$ herauskürzen.
:::
:::karte zusammenhang Warum der Tausch hilft
Warum kann der Tausch eines Dreiecks gegen einen Stern eine Brücke ohne Abgleich berechenbar machen?
---
Der Sternpunkt ist ein neuer Knoten, an dem jeder Sternwiderstand in Reihe mit dem Nachbarn dahinter liegt. So entstehen Reihen- und Parallelgruppen, die man zusammenfassen kann.
--- falsch
Weil der Stern weniger Widerstände hat als das Dreieck und das Netz dadurch kleiner wird. Mit weniger Widerständen genügen die Regeln für Reihe und Parallel, um das ganze Netz zusammenzufassen.
--- falsch
Weil der Stern die Ströme in den Widerständen unverändert lässt, sodass man sie direkt aus dem Stern ablesen kann, ohne das Netz zusammenzufassen.
--- falsch
Weil der Tausch die Brücke abgleicht: Danach liegen ihre mittleren Knoten auf gleichem Potenzial, und der Querzweig ist stromlos.
:::
:::karte zusammenhang Gültigkeit der Umwandlung
Wofür gilt die Gleichwertigkeit von Stern und Dreieck, und wofür gilt sie nicht?
---
Für jede äußere Beschaltung, aber nur an den drei Klemmen. Der Sternpunkt ist im Original kein Knoten, und die Ströme in den Widerständen selbst unterscheiden sich.
--- falsch
Nur für die äußere Beschaltung, für die man gerechnet hat, dafür aber auch im Inneren: Die Ströme in den Widerständen sind in beiden Formen gleich.
--- falsch
Für jede äußere Beschaltung und auch im Inneren. Der Sternpunkt entspricht im Dreieck dem Mittelpunkt der längsten Seite, dort liegt dasselbe Potenzial.
--- falsch
Nur wenn alle drei Widerstände gleich groß sind. Sonst unterscheiden sich die Spannungen an den Klemmen, und man muss das ganze Netz neu rechnen.
:::
:::karte zusammenhang Grenzfälle der Umwandlung
Was ergibt die Umwandlung vom Dreieck zum Stern bei drei gleichen Dreieckswiderständen, und was, wenn $R_{12}\to0$ geht?
---
Drei gleiche Dreieckswiderstände ergeben einen Stern mit einem Drittel des Werts. Für $R_{12}\to0$ gehen $R_{10}$ und $R_{20}$ gegen null, und $R_{30}$ wird $R_{23}\parallel R_{31}$, genau das kurzgeschlossene Dreieck.
--- falsch
Drei gleiche Dreieckswiderstände ergeben einen Stern mit dem dreifachen Wert. Für $R_{12}\to0$ gehen alle drei Sternwiderstände gegen null, weil das Dreieck dann überall kurzgeschlossen ist.
--- falsch
Drei gleiche Dreieckswiderstände ergeben einen Stern mit demselben Wert. Für $R_{12}\to0$ geht $R_{30}$ gegen null, und $R_{10}$ und $R_{20}$ werden zu $R_{31}$ und $R_{23}$.
--- falsch
Drei gleiche Dreieckswiderstände ergeben einen Stern mit einem Drittel des Werts. Für $R_{12}\to0$ bleiben alle Sternwiderstände endlich, und $R_{30}$ wird $R_{23}+R_{31}$.
:::
:::karte begriff Zweitor
Was ist ein Zweitor, und wie zeichnet man Stern und Dreieck, wenn sie als Zweitor dienen?
---
Ein Netzwerk mit zwei Klemmenpaaren, einem Eingang und einem Ausgang. Man zeichnet Dreieck und Stern so, dass der Eingang links und der Ausgang rechts liegt.
--- falsch
Ein Netzwerk mit genau zwei Klemmen, die ein Paar bilden. Man zeichnet Dreieck und Stern dafür so, dass beide Klemmen links liegen.
--- falsch
Ein Netzwerk aus genau zwei Widerständen, einem Längs- und einem Querwiderstand. Stern und Dreieck sind deshalb keine Zweitore.
--- falsch
Ein Netzwerk mit zwei Quellen, je einer am Eingang und am Ausgang. Man zeichnet Dreieck und Stern dafür so, dass beide Quellen in der Mitte zwischen den Klemmen liegen.
:::
:::karte begriff T-Schaltung und Pi-Schaltung
Wie heißen Dreieck und Stern, wenn man sie als Zweitor mit dem Eingang links und dem Ausgang rechts zeichnet, und was ändert sich an ihrer Umwandlung?
---
Das Dreieck heißt dann $\pi$-Schaltung, der Stern T-Schaltung. Formeln und Regeln der Stern-Dreieck-Transformation bleiben dieselben.
--- falsch
Das Dreieck heißt dann T-Schaltung, der Stern $\pi$-Schaltung. Für die Umwandlung gelten eigene Formeln, weil Eingang und Ausgang getrennt sind.
--- falsch
Das Dreieck heißt dann $\pi$-Schaltung, der Stern T-Schaltung. Ineinander umwandeln lassen sie sich aber nicht mehr, weil Eingang und Ausgang verschieden sind.
--- falsch
Der Stern heißt dann $\pi$-Schaltung, das Dreieck bleibt Dreieck. Die Formeln der Stern-Dreieck-Transformation gelten unverändert, nur in der Leitwertform.
:::
:::karte begriff Dämpfungsglied
Wozu dienen Dämpfungsglieder, die man in der Nachrichtentechnik in T- oder $\pi$-Form baut?
---
Sie schwächen ein Signal um einen festen Faktor ab und zeigen an beiden Klemmenpaaren denselben Eingangswiderstand.
--- falsch
Sie verstärken ein schwaches Signal um einen festen Faktor und zeigen an beiden Klemmenpaaren denselben Eingangswiderstand.
--- falsch
Sie schwächen große Signale stärker ab als kleine und begrenzen so die Spitzen; ihr Eingangswiderstand ist an beiden Seiten verschieden.
--- falsch
Sie trennen ein Signal nach Frequenzen und lassen nur einen Bereich durch; dazu bestehen sie stets aus Spulen und Kondensatoren.
:::
::::
