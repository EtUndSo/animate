---
title: Stufe 5: Reale Quellen und der Arbeitspunkt
pfad: Elektrotechnik / 1. Semester / ET1 – Grundgebiete der Elektrotechnik 1: Einführung in die Schaltungsanalyse / Quellen und Ersatzquellen
adresse: elektrotechnik/1-semester/grundlagen-der-elektrotechnik/quellen-und-ersatzquellen
knoten: Kapitel 5: Quellen und Ersatzquellen
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

::::beispiel
Mit 16 $\Omega$ sind $I_\mathrm{A}=9\,\mathrm{V}/18\,\Omega=0{,}5$ A und $U_\mathrm{AB}=8$ V, innen fällt 1 V ab. Mit 2 $\Omega$ sind es 2,25 A und 4,5 V. Beide Punkte liegen auf der Geraden: $9\,\mathrm{V}-2\,\Omega\cdot2{,}25\,\mathrm{A}=4{,}5$ V. Ihr Abstand zeigt den Innenwiderstand als Steigung: $\Delta U_\mathrm{AB}/\Delta I_\mathrm{A}=3{,}5\,\mathrm{V}/(-1{,}75\,\mathrm{A})=-2\,\Omega$.
::::

⁠**Grenzfälle:** Für $R_\mathrm{L}\to\infty$ liefert [(5.2)](#gl-5-2) den Leerlauf $U_\mathrm{AB}=U_\mathrm{q}$, für $R_\mathrm{L}\to0$ den Kurzschlussstrom $I_\mathrm{KS}=U_\mathrm{q}/R_\mathrm{q}=4{,}5$ A. Für $R_\mathrm{q}\to0$ bleibt die ideale Spannungsquelle. Auch eine nichtlineare Last lässt sich so behandeln: Ihre Kennlinie ist dann eine Kurve, der Schnittpunkt bleibt die Lösung ([Kapitel 9](/wissen/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/halbleiter-und-dioden/halbleiter-und-dioden.html)).

:::ltspice Die Kennlinie der Batterie
⁠**Zeichnen:** `voltage` mit 9 von `q` nach Masse, `res` mit 2 von `q` nach `a`. Als Last eine Stromquelle `current` namens `I1` von `a` nach Masse.

⁠**Direktive:** `.dc I1 0 4.5 0.05`

⁠**Was du siehst:** `V(a)` fällt als Gerade von 9 V bei 0 A auf 0 V bei 4,5 A. Bei 0,5 A stehen 8 V da, bei 2,25 A stehen 4,5 V da, die Punkte aus Abb. [6](#abb-6). Stelle für Aufgabe [6](#aufg-6) die Werte 12.6 und 0.01 ein und lasse bis 200 A laufen (`.dc I1 0 200 1`). Bei 150 A und bei 20 A liest du deine Klemmenspannungen ab.
:::

:::frage Warum zeigt das Messgerät an einer Batterie 9 V, obwohl sie innen 2 $\Omega$ hat?
Weil es fast keinen Strom zieht ([Kapitel 4](/wissen/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/strom-und-spannung-messen/strom-und-spannung-messen.html)). Mit 10 M$\Omega$ Eingangswiderstand fließen 0,9 µ A, innen fallen 1,8 µ V ab. Man misst praktisch den Leerlauf. Den Innenwiderstand sieht man erst unter Last.
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

::::formelsammlung
**Reale Spannungsquelle**

$$U_\mathrm{AB}=U_\mathrm{q}-R_\mathrm{q}\,I_\mathrm{A}$$

Ersatzschaltbild: ideale Spannungsquelle in Reihe mit $R_\mathrm{q}$ (Maschenregel). $U_\mathrm{q}$ ist die Leerlaufspannung, $R_\mathrm{q}$ der Innen- oder Quellwiderstand in $\Omega$: rund 2 $\Omega$ bei einem 9-V-Block, 10 m$\Omega$ bei einer Autobatterie. Gilt, solange $R_\mathrm{q}$ nicht vom Strom abhängt.

**Reale Stromquelle**

$$I_\mathrm{A}=I_\mathrm{q}-G_\mathrm{q}\,U_\mathrm{AB}$$

Ersatzschaltbild: ideale Stromquelle parallel zu $G_\mathrm{q}$ (Knotenregel): Von $I_\mathrm{q}$ zweigt $G_\mathrm{q}U_\mathrm{AB}$ ab, der Rest geht nach außen. $I_\mathrm{q}$ ist der Kurzschlussstrom, $G_\mathrm{q}$ der Quellleitwert in S.

**Arbeitsgerade**

$$U_\mathrm{AB}=R_\mathrm{L}I_\mathrm{A}$$

Gerade der Last durch den Ursprung. Ihr Schnittpunkt mit der Kennlinie der Quelle ist der Arbeitspunkt. Auch eine nichtlineare Last lässt sich so behandeln, ihre Kennlinie ist dann eine Kurve.

**Arbeitspunkt**

$$I_\mathrm{A}=\frac{U_\mathrm{q}}{R_\mathrm{q}+R_\mathrm{L}},\qquad U_\mathrm{AB}=\frac{R_\mathrm{L}}{R_\mathrm{q}+R_\mathrm{L}}\,U_\mathrm{q}$$

Aus dem Gleichsetzen $U_\mathrm{q}-R_\mathrm{q}I_\mathrm{A}=R_\mathrm{L}I_\mathrm{A}$. Für $R_\mathrm{L}\to\infty$ folgt der Leerlauf $U_\mathrm{AB}=U_\mathrm{q}$, für $R_\mathrm{q}\to0$ die ideale Spannungsquelle.

**Kurzschlussstrom**

$$I_\mathrm{KS}=U_\mathrm{q}/R_\mathrm{q}$$

Grenzfall $R_\mathrm{L}\to0$ des Arbeitspunkts; bei der Batterie mit 9 V und 2 $\Omega$ sind das 4,5 A.
::::

::::lernkarten
:::karte zusammenhang Spannungsabfall in der Batterie
Warum hält eine Batterie ihre Spannung unter Last nicht, und warum ist ihre Kennlinie eine fallende Gerade?
---
Der Strom muss durch die Batterie selbst: Ionen wandern durch die Elektrolytlösung, Elektronen durch Elektroden und Anschlüsse, dabei geht Energie als Wärme verloren. Dieser innere Abfall ist proportional zum Strom, an den Klemmen bleibt der Rest.
--- falsch
Die Chemie liefert bei großem Strom je Coulomb weniger Energie, weil sie sich schneller verbraucht. Die Spannung sinkt deshalb mit der bereits entnommenen Ladung, nicht mit dem Strom selbst; die Kennlinie fällt erst nach längerer Zeit ab, nicht sofort.
--- falsch
Die Last zieht Spannung aus der Batterie ab: Je kleiner ihr Widerstand, desto mehr Spannung nimmt sie für sich in Anspruch, und für die Klemmen der Batterie bleibt entsprechend weniger übrig, obwohl innen nichts verloren geht.
--- falsch
Der Strom erwärmt die Leitungen außerhalb der Batterie, innen geht keine Energie verloren. Der Abfall wächst mit dem Quadrat des Stroms, die Kennlinie ist nur näherungsweise gerade.
:::
:::karte begriff Ersatzschaltbild
Was ist ein Ersatzschaltbild, wie man es etwa für eine Batterie zeichnet?
---
Eine Schaltung aus idealen Elementen, die sich an den Klemmen wie das echte Bauteil verhält. Für die Batterie: ideale Spannungsquelle in Reihe mit dem Innenwiderstand.
--- falsch
Eine maßstabsgetreue Zeichnung des inneren Aufbaus. Sie zeigt, wo im Bauteil welcher Strom fließt und an welcher Stelle wie viel Wärme entsteht.
--- falsch
Eine Schaltung aus idealen Elementen, die auch im Inneren genau das echte Bauteil nachbildet, mit denselben Strömen und denselben Verlusten in jedem einzelnen Teil des Bauteils.
--- falsch
Ein Ersatzbauteil, das man einsetzt, wenn das eigentliche ausfällt. Es liefert an den Klemmen ungefähr dieselben Werte wie das Original.
:::
:::karte begriff reale Spannungsquelle
Wie ist eine reale Spannungsquelle im Ersatzschaltbild aufgebaut, und welche Gleichung gilt an ihren Klemmen?
---
Eine ideale Spannungsquelle in Reihe mit $R_\mathrm{q}$: $U_\mathrm{AB}=U_\mathrm{q}-R_\mathrm{q}\,I_\mathrm{A}$. Das ist die Maschenregel im Ersatzschaltbild; $U_\mathrm{q}$ ist die Leerlaufspannung.
--- falsch
Eine ideale Spannungsquelle parallel zu $R_\mathrm{q}$: $U_\mathrm{AB}=U_\mathrm{q}-R_\mathrm{q}\,I_\mathrm{A}$. Das ist die Knotenregel im Ersatzschaltbild; $U_\mathrm{q}$ ist die Spannung im Kurzschluss.
--- falsch
Eine ideale Spannungsquelle in Reihe mit $R_\mathrm{q}$: $U_\mathrm{AB}=U_\mathrm{q}+R_\mathrm{q}\,I_\mathrm{A}$. Der Innenwiderstand erhöht die Spannung, je mehr Strom fließt.
--- falsch
Eine ideale Stromquelle in Reihe mit $R_\mathrm{q}$: $U_\mathrm{AB}=R_\mathrm{q}\,I_\mathrm{A}$. Die Spannung wächst mit dem Strom, $U_\mathrm{q}$ wird erst unter voller Last erreicht.
:::
:::karte begriff reale Stromquelle
Wie ist eine reale Stromquelle im Ersatzschaltbild aufgebaut, und welche Gleichung gilt an ihren Klemmen?
---
Eine ideale Stromquelle parallel zu $G_\mathrm{q}$: $I_\mathrm{A}=I_\mathrm{q}-G_\mathrm{q}\,U_\mathrm{AB}$. Das ist die Knotenregel: Von $I_\mathrm{q}$ zweigt $G_\mathrm{q}U_\mathrm{AB}$ ab, der Rest geht nach außen; $I_\mathrm{q}$ ist der Kurzschlussstrom.
--- falsch
Eine ideale Stromquelle in Reihe mit $G_\mathrm{q}$: $I_\mathrm{A}=I_\mathrm{q}-G_\mathrm{q}\,U_\mathrm{AB}$. Das ist die Maschenregel im Ersatzschaltbild; $I_\mathrm{q}$ ist der Strom, der im Leerlauf nach außen fließt, also der größte Strom.
--- falsch
Eine ideale Stromquelle parallel zu $G_\mathrm{q}$: $I_\mathrm{A}=I_\mathrm{q}+G_\mathrm{q}\,U_\mathrm{AB}$. Der Leitwert liefert zusätzlichen Strom nach außen, je höher die Spannung an den Klemmen steigt.
--- falsch
Eine ideale Spannungsquelle parallel zu $G_\mathrm{q}$: $I_\mathrm{A}=G_\mathrm{q}\,U_\mathrm{AB}$. Der Strom folgt der Spannung, und $I_\mathrm{q}$ ist der größte Strom, der im Leerlauf fließt.
:::
:::karte begriff Innenwiderstand
Was gibt der Innenwiderstand $R_\mathrm{q}$ einer realen Spannungsquelle an, und wie groß ist er typisch?
---
Den Widerstand in Reihe zur idealen Quelle im Ersatzschaltbild, in $\Omega$; an ihm fällt $R_\mathrm{q}I_\mathrm{A}$ ab. Typisch sind rund 2 $\Omega$ bei einem 9-V-Block und 10 m$\Omega$ bei einer Autobatterie.
--- falsch
Den Widerstand der angeschlossenen Last, von der Quelle aus gesehen. Er bestimmt, wie viel Strom fließt, und beträgt bei einem 9-V-Block etwa 16 $\Omega$, bei einer Autobatterie einige Ohm.
--- falsch
Den Widerstand des Messgeräts, mit dem man die Quellenspannung anzeigt. Er ist bei allen Batterien gleich und liegt bei rund 10 M$\Omega$, damit die Anzeige nicht verfälscht wird.
--- falsch
Den Widerstand parallel zur idealen Quelle, über den sie sich im Leerlauf langsam selbst entlädt. Er beträgt rund 2 k$\Omega$ bei einem 9-V-Block und mehr bei größeren Batterien.
:::
:::karte begriff Arbeitsgerade und Arbeitspunkt
Was ist die Arbeitsgerade einer Last, und wie findet man mit ihr den Arbeitspunkt an einer Quelle?
---
Die Gerade $U_\mathrm{AB}=R_\mathrm{L}I_\mathrm{A}$ durch den Ursprung, die die Last vorgibt. Quellengleichung und Lastgleichung müssen zugleich gelten; das geht nur im Schnittpunkt beider Geraden, dem Arbeitspunkt.
--- falsch
Die Kennlinie der Quelle von Leerlauf bis Kurzschluss. Der Arbeitspunkt ist ihr Mittelpunkt, an dem die Quelle die halbe Leerlaufspannung und den halben Kurzschlussstrom abgibt, gleich welche Last anliegt.
--- falsch
Die Gerade $U_\mathrm{AB}=R_\mathrm{L}I_\mathrm{A}$ der Last durch den Ursprung. Der Arbeitspunkt ist ihr Schnittpunkt mit der Spannungsachse, denn dort liegt die Leerlaufspannung an.
--- falsch
Die Gerade der Last, die parallel zur Kennlinie der Quelle verläuft. Der Arbeitspunkt ist die Stelle, an der beide Geraden den kleinsten Abstand voneinander haben.
:::
:::karte formel Arbeitspunkt
Welcher Strom und welche Klemmenspannung stellen sich ein, wenn eine reale Spannungsquelle mit $U_\mathrm{q}$ und $R_\mathrm{q}$ eine Last $R_\mathrm{L}$ speist?
---
$I_\mathrm{A}=\frac{U_\mathrm{q}}{R_\mathrm{q}+R_\mathrm{L}}$ und $U_\mathrm{AB}=\frac{R_\mathrm{L}}{R_\mathrm{q}+R_\mathrm{L}}\,U_\mathrm{q}$, aus dem Gleichsetzen von Quellengerade und Arbeitsgerade. Für 9 V und 2 $\Omega$ an 16 $\Omega$ sind das 0,5 A und 8 V.
--- falsch
$I_\mathrm{A}=\frac{U_\mathrm{q}}{R_\mathrm{L}}$ und $U_\mathrm{AB}=U_\mathrm{q}$, weil der Innenwiderstand nur im Kurzschluss eine Rolle spielt. Für 9 V und 2 $\Omega$ an 16 $\Omega$ sind das 0,5625 A und 9 V.
--- falsch
$I_\mathrm{A}=\frac{U_\mathrm{q}}{R_\mathrm{q}+R_\mathrm{L}}$ und $U_\mathrm{AB}=\frac{R_\mathrm{q}}{R_\mathrm{q}+R_\mathrm{L}}\,U_\mathrm{q}$, aus dem Spannungsteiler. Für 9 V und 2 $\Omega$ an 16 $\Omega$ sind das 0,5 A und 1 V.
--- falsch
$I_\mathrm{A}=\frac{U_\mathrm{q}}{R_\mathrm{q}\parallel R_\mathrm{L}}$ und $U_\mathrm{AB}=U_\mathrm{q}$, weil Quelle und Last an denselben Klemmen parallel liegen und dieselbe Spannung haben. Für 9 V und 2 $\Omega$ an 16 $\Omega$ sind das etwa 5,1 A und 9 V.
:::
:::karte herleitung Arbeitspunkt aus zwei Geraden
Leite aus der Gleichung der realen Spannungsquelle und der Arbeitsgerade der Last den Strom und die Spannung im Arbeitspunkt her.
---
Die Quelle gibt $U_\mathrm{AB}=U_\mathrm{q}-R_\mathrm{q}\,I_\mathrm{A}$ vor, weil im Ersatzschaltbild innen $R_\mathrm{q}I_\mathrm{A}$ abfällt (Maschenregel).
---
Die Last gibt die Arbeitsgerade $U_\mathrm{AB}=R_\mathrm{L}I_\mathrm{A}$ vor, weil durch sie derselbe Klemmenstrom fließt und an ihr dieselbe Klemmenspannung liegt.
---
Gleichsetzen ergibt $U_\mathrm{q}-R_\mathrm{q}I_\mathrm{A}=R_\mathrm{L}I_\mathrm{A}$, weil beide Gleichungen zugleich gelten müssen und das nur im Schnittpunkt der Geraden geht.
---
Auflösen ergibt $I_\mathrm{A}=\frac{U_\mathrm{q}}{R_\mathrm{q}+R_\mathrm{L}}$, weil man die Glieder mit $I_\mathrm{A}$ auf eine Seite bringt und durch $R_\mathrm{q}+R_\mathrm{L}$ teilt.
---
Einsetzen in die Arbeitsgerade ergibt $U_\mathrm{AB}=\frac{R_\mathrm{L}}{R_\mathrm{q}+R_\mathrm{L}}\,U_\mathrm{q}$, weil an der Last $U_\mathrm{AB}=R_\mathrm{L}I_\mathrm{A}$ gilt.
:::
:::karte zusammenhang Wie sich der Arbeitspunkt einstellt
Warum stellt sich der Arbeitspunkt von selbst ein, wenn man eine Last an eine Quelle anschließt?
---
Lieferte die Quelle mehr Strom, als die Last abnimmt, sammelte sich Ladung an Klemme A, und ihr Potenzial stiege. Dann fiele der Strom der Quelle, und der Strom der Last stiege, bis beide Ströme gleich sind.
--- falsch
Die Quelle misst den Widerstand der Last und stellt ihre Spannung so ein, dass genau der passende Strom fließt. Ohne diese Regelung in der Quelle gäbe es keinen festen Punkt, und der Strom schwankte ständig.
--- falsch
Lieferte die Quelle mehr Strom, als die Last abnimmt, flösse der Überschuss durch den Innenwiderstand zurück. Der Arbeitspunkt ist erreicht, wenn nichts mehr zurückfließt.
--- falsch
Die Last nimmt sich so viel Strom, wie sie braucht, und die Quelle liefert ihn unabhängig von ihrer Spannung. Der Arbeitspunkt hängt deshalb nur von der Last ab.
:::
:::karte zusammenhang Leerlauf und Kurzschluss als Grenzfälle
Was liefern die Formeln für den Arbeitspunkt im Grenzfall $R_\mathrm{L}\to\infty$ und im Grenzfall $R_\mathrm{L}\to0$?
---
Für $R_\mathrm{L}\to\infty$ den Leerlauf mit $U_\mathrm{AB}=U_\mathrm{q}$, für $R_\mathrm{L}\to0$ den Kurzschlussstrom $I_\mathrm{KS}=U_\mathrm{q}/R_\mathrm{q}$, bei der Batterie 4,5 A.
--- falsch
Für $R_\mathrm{L}\to\infty$ den Kurzschluss mit $U_\mathrm{AB}=0$, für $R_\mathrm{L}\to0$ den Leerlauf mit $U_\mathrm{AB}=U_\mathrm{q}$, bei der Batterie also 0 V und 9 V.
--- falsch
Für $R_\mathrm{L}\to\infty$ einen unbegrenzt großen Strom, für $R_\mathrm{L}\to0$ die volle Spannung $U_\mathrm{q}$, weil die Last dann keine Spannung mehr aufnimmt.
--- falsch
Für $R_\mathrm{L}\to\infty$ den Leerlauf mit $U_\mathrm{AB}=U_\mathrm{q}$, für $R_\mathrm{L}\to0$ einen unbegrenzt großen Strom, weil dann nichts mehr den Strom begrenzt.
:::
:::karte zusammenhang Voltmeter an der Batterie
Warum zeigt ein Voltmeter an einer 9-V-Batterie mit 2 $\Omega$ Innenwiderstand praktisch 9 V an?
---
Weil es fast keinen Strom zieht: Mit 10 M$\Omega$ Eingangswiderstand fließen 0,9 µ A, innen fallen 1,8 µ V ab. Man misst praktisch den Leerlauf; den Innenwiderstand sieht man erst unter Last.
--- falsch
Weil der Innenwiderstand nur beim Laden wirkt: Beim Entladen, also auch beim Messen, fällt an ihm keine Spannung ab, und man sieht stets die volle Quellenspannung, gleich bei welcher Last.
--- falsch
Weil das Voltmeter den Innenwiderstand herausrechnet: Es misst Strom und Spannung zugleich, zieht den inneren Abfall ab und zeigt so die Quellenspannung an.
--- falsch
Weil das Voltmeter mit seinem kleinen Innenwiderstand die Batterie kurzschließt und den Innenwiderstand dabei überbrückt, sodass innen nichts abfällt.
:::
:::karte zusammenhang Licht beim Anlassen
Warum wird das Autolicht dunkler, wenn zugleich der Anlasser läuft?
---
Der große Strom des Anlassers erzeugt am Innenwiderstand einen großen Abfall, den auch das Licht spürt: Die Klemmenspannung sinkt von 12,4 V auf 10,94 V, die Leistung des Lichts von 248 W auf 193 W.
--- falsch
Weil der Anlasser dem Licht Strom wegnimmt: Beide teilen sich einen festen Batteriestrom, und der Anlasser als kleinerer Widerstand bekommt den größeren Teil davon, während die Klemmenspannung gleich bleibt.
--- falsch
Weil die Quellenspannung beim Anlassen durch die Kälte des Motors sinkt; der Innenwiderstand spielt dabei keine Rolle, er ist bei Autobatterien praktisch null.
--- falsch
Weil Licht und Anlasser in Reihe an der Batterie liegen: Am Anlasser fällt der größte Teil der 12,6 V ab, und für das Licht bleibt nur der Rest.
:::
::::
