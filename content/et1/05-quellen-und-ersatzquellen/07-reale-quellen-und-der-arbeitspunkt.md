---
title: Stufe 5: Reale Quellen und der Arbeitspunkt
pfad: Elektrotechnik / 1. Semester / Grundlagen der Elektrotechnik / Quellen und Ersatzquellen
order: 1150700
summary: Eine Batterie hält ihre Spannung unter Last nicht.
tags: Ersatzschaltbild, reale Spannungsquelle, reale Stromquelle, Arbeitsgerade, Arbeitspunkt
lang: de
---

<span class="anker" id="stufe-5"></span>

:::zweck
Eine Batterie hält ihre Spannung unter Last nicht. Diese Stufe zeigt warum und findet den Punkt der Kennlinie, den eine Last einstellt.
:::

**Die Idee.** In einer Batterie treibt die Chemie Ladung an und liefert dafür je Coulomb eine feste Energie, die Quellenspannung. Der Strom muss aber durch die Batterie selbst: Ionen wandern durch die Elektrolytlösung, Elektronen durch Elektroden und Anschlüsse. Dabei geht Energie als Wärme verloren, genau wie in einem Widerstand. An den Klemmen bleibt nur der Rest. Je größer der Strom, desto mehr fällt innen ab. Dieser Abfall ist proportional zum Strom, also ist die Kennlinie eine fallende Gerade.

:::abbildung et1/k5arbeitsgerade 6
Links die reale Spannungsquelle an einer Last. Rechts die Kennlinie der Quelle (blau) von Leerlauf bis Kurzschluss und die Arbeitsgerade jeder Last. Der Schnittpunkt ist der Arbeitspunkt: mit 16 $\Omega$ bei 0,5 A und 8 V, mit 2 $\Omega$ bei 2,25 A und 4,5 V.
:::

:::definition Definition 5.1 (Reale Quellen)
<span class="anker" id="satz-5-1"></span>

Ein __Ersatzschaltbild__ ist eine Schaltung aus idealen Elementen, die sich an den Klemmen wie das echte Bauteil verhält. Die __reale Spannungsquelle__ ist eine ideale Spannungsquelle in Reihe mit $R_\mathrm{q}$, die __reale Stromquelle__ eine ideale Stromquelle parallel zu $G_\mathrm{q}$:

<span class="anker" id="gl-5-1"></span>
$$U_\mathrm{AB}=U_\mathrm{q}-R_\mathrm{q}\,I_\mathrm{A}, \qquad\qquad I_\mathrm{A}=I_\mathrm{q}-G_\mathrm{q}\,U_\mathrm{AB}. \tag{5.1}$$
:::

⁠**So liest man das:** $U_\mathrm{q}$ ist die Leerlaufspannung. $R_\mathrm{q}$ ist der Innen- oder Quellwiderstand in $\Omega$: rund 2 $\Omega$ bei einem 9-V-Block, 10 m$\Omega$ bei einer Autobatterie. $I_\mathrm{q}$ ist der Kurzschlussstrom, $G_\mathrm{q}$ der Quellleitwert in S. Die erste Gleichung ist die Maschenregel im Ersatzschaltbild, die zweite die Knotenregel: Von $I_\mathrm{q}$ zweigt $G_\mathrm{q}U_\mathrm{AB}$ ab, der Rest geht nach außen. **Gültigkeit:** Die Gerade gilt, solange $R_\mathrm{q}$ nicht vom Strom abhängt. Echte Batterien weichen bei großem Strom und im Alter ab.

**Die Arbeitsgerade.** Eine Last gibt eine zweite Gleichung vor, $U_\mathrm{AB}=R_\mathrm{L}I_\mathrm{A}$. Diese Gerade durch den Ursprung heißt __Arbeitsgerade__. Beide Gleichungen müssen zugleich gelten. Das geht nur im Schnittpunkt, dem __Arbeitspunkt__. Gleichsetzen von $U_\mathrm{q}-R_\mathrm{q}I_\mathrm{A}=R_\mathrm{L}I_\mathrm{A}$ ergibt:

<span class="anker" id="gl-5-2"></span>
$$I_\mathrm{A}=\frac{U_\mathrm{q}}{R_\mathrm{q}+R_\mathrm{L}},\qquad U_\mathrm{AB}=\frac{R_\mathrm{L}}{R_\mathrm{q}+R_\mathrm{L}}\,U_\mathrm{q}. \tag{5.2}$$

Der Mechanismus dahinter: Lieferte die Quelle mehr Strom, als die Last abnimmt, sammelte sich Ladung an Klemme A und ihr Potenzial stiege. Dann fiele der Strom der Quelle, und der Strom der Last stiege. Das geht so lange, bis beide Ströme gleich sind.

**Beispiel.** Mit 16 $\Omega$ sind $I_\mathrm{A}=9\,\mathrm{V}/18\,\Omega=0{,}5$ A und $U_\mathrm{AB}=8$ V, innen fällt 1 V ab. Mit 2 $\Omega$ sind es 2,25 A und 4,5 V. Beide Punkte liegen auf der Geraden: $9\,\mathrm{V}-2\,\Omega\cdot2{,}25\,\mathrm{A}=4{,}5$ V. Ihr Abstand zeigt den Innenwiderstand als Steigung: $\Delta U_\mathrm{AB}/\Delta I_\mathrm{A}=3{,}5\,\mathrm{V}/(-1{,}75\,\mathrm{A})=-2\,\Omega$. **Grenzfälle:** Für $R_\mathrm{L}\to\infty$ liefert [(5.2)](#gl-5-2) den Leerlauf $U_\mathrm{AB}=U_\mathrm{q}$, für $R_\mathrm{L}\to0$ den Kurzschlussstrom $I_\mathrm{KS}=U_\mathrm{q}/R_\mathrm{q}=4{,}5$ A. Für $R_\mathrm{q}\to0$ bleibt die ideale Spannungsquelle. Auch eine nichtlineare Last lässt sich so behandeln: Ihre Kennlinie ist dann eine Kurve, der Schnittpunkt bleibt die Lösung ([Teil 9](/wissen/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/halbleiter-und-dioden/halbleiter-und-dioden.html)).

:::ltspice Die Kennlinie der Batterie
⁠**Zeichnen:** `voltage` mit 9 von `q` nach Masse, `res` mit 2 von `q` nach `a`. Als Last eine Stromquelle `current` namens `I1` von `a` nach Masse.

⁠**Direktive:** `.dc I1 0 4.5 0.05`

⁠**Was du siehst:** `V(a)` fällt als Gerade von 9 V bei 0 A auf 0 V bei 4,5 A. Bei 0,5 A stehen 8 V da, bei 2,25 A stehen 4,5 V da, die Punkte aus Abb. [6](#abb-6). Stelle für Aufgabe [6](#aufg-6) die Werte 12.6 und 0.01 ein und lasse bis 200 A laufen (`.dc I1 0 200 1`). Bei 150 A und bei 20 A liest du deine Klemmenspannungen ab.
:::

:::frage Warum zeigt das Messgerät an einer Batterie 9 V, obwohl sie innen 2 $\Omega$ hat?
Weil es fast keinen Strom zieht ([Teil 4](/wissen/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/strom-und-spannung-messen/strom-und-spannung-messen.html)). Mit 10 M$\Omega$ Eingangswiderstand fließen 0,9 µ A, innen fallen 1,8 µ V ab. Man misst praktisch den Leerlauf. Den Innenwiderstand sieht man erst unter Last.
:::

:::aufgabe Aufgabe 6 ★ Das Licht beim Anlassen
<span class="anker" id="aufg-6"></span>

Eine Autobatterie hat 12,6 V und 10 m$\Omega$. Der Anlasser wirkt wie 74 m$\Omega$. (a) Berechne Strom und Klemmenspannung beim Anlassen. (b) Wie groß wäre der Kurzschlussstrom? (c) Das Licht zieht allein 20 A. Wie groß ist dabei die Klemmenspannung, welchen Widerstand hat es also? (d) Wie groß ist die Klemmenspannung, wenn Licht und Anlasser zugleich laufen? Warum wird das Licht dunkler?

:::loesung
(a) $I_\mathrm{A}=12{,}6\,\mathrm{V}/84\,\mathrm{m\Omega}=150$ A, $U_\mathrm{AB}=12{,}6\,\mathrm{V}-10\,\mathrm{m\Omega}\cdot150\,\mathrm{A}=11{,}1$ V.

(b) $I_\mathrm{KS}=12{,}6\,\mathrm{V}/10\,\mathrm{m\Omega}=1260$ A.

(c) $U_\mathrm{AB}=12{,}6\,\mathrm{V}-0{,}2\,\mathrm{V}=12{,}4$ V, also $R=12{,}4\,\mathrm{V}/20\,\mathrm{A}=0{,}62\,\Omega$.

(d) Licht und Anlasser parallel: $0{,}62\,\Omega\parallel74\,\mathrm{m\Omega}=66{,}1\,\mathrm{m\Omega}$. Spannungsteiler mit 10 m$\Omega$: $U_\mathrm{AB}=10{,}94$ V. Die Batterie liefert 165,6 A, das Licht erhält 17,65 A statt 20 A. Der große Strom des Anlassers erzeugt innen 1,66 V Abfall, den auch das Licht spürt. Seine Leistung sinkt von 248 W auf 193 W.
:::
:::
