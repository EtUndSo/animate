---
title: Stufe 8: Strom als Signal
pfad: Elektrotechnik / 1. Semester / ET1 – Grundgebiete der Elektrotechnik 1: Einführung in die Schaltungsanalyse / Der Operationsverstärker
adresse: elektrotechnik/1-semester/grundlagen-der-elektrotechnik/der-operationsverstarker
knoten: Kapitel 11: Der Operationsverstärker
order: 1211000
summary: Bisher war die Spannung das Signal.
tags: Transimpedanzverstärker, differenzieller Widerstand, Negativimpedanzkonverter
lang: de
---

<span class="anker" id="stufe-8"></span>

:::zweck
Bisher war die Spannung das Signal. Viele Quellen liefern aber einen Strom. Diese Stufe wandelt Strom in Spannung und zeigt, dass der OPV einen negativen Widerstand nachbilden kann.
:::

**Strom in Spannung.** Eine Fotodiode liefert einen Strom, der von ihrer Spannung kaum abhängt. Im __Transimpedanzverstärker__ fließt er direkt in die virtuelle Masse und muss durch $R$ (Abb. [10](#abb-10) links):

<span class="anker" id="gl-8-1"></span>
$$U_\mathrm{A}=-R\,I_\mathrm{E},\qquad r_\mathrm{ein}=\frac{\Delta U_-}{\Delta I_\mathrm{E}}=\frac{R}{1+A}. \tag{8.1}$$

Mit $R=1$ M$\Omega$ werden 2 µ A zu $-2$ V. Der Knoten bewegt sich dabei nur um $2\,\mathrm{V}/A=20$ µ V. Das ist der kleine Eingangswiderstand von 10 $\Omega$, ein Wert für Änderungen (__differenzieller Widerstand__). Die Quelle sieht fast einen Kurzschluss, ihr Innenwiderstand spielt keine Rolle.

**Ein negativer Widerstand.** Ein Widerstand zieht bei positiver Spannung Strom in Zählpfeilrichtung (Verbraucherzählpfeilsystem, [Kapitel 2](/wissen/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/strom-widerstand-und-kirchhoff/strom-widerstand-und-kirchhoff.html)). Der __Negativimpedanzkonverter__ (NIC) schiebt stattdessen Strom heraus (Abb. [10](#abb-10) rechts). Klemme 1 liegt am Plus-Eingang, von dort führt ein $R$ zum Ausgang. Vom Ausgang führt ein gleiches $R$ zum Minus-Eingang, von dort $R_2$ nach Masse. Aus $\varphi_+=\varphi_-$ folgt $U_1=U_2$.

:::satz Satz 8.1 (NIC)
<span class="anker" id="satz-8-1"></span>

<span class="anker" id="gl-8-2"></span>
$$R_\mathrm{ein}=\frac{U_1}{I_1}=-R_2. \tag{8.2}$$

Die Regel gilt nur, solange der Widerstand $R_\mathrm{i}$, der an Klemme 1 gegen Masse wirkt, kleiner als $R_2$ ist.
:::

⁠**So liest man das:** $I_1$ zählt in Klemme 1 hinein, $U_1$ gegen Masse. $U_2$ und $I_2$ gehören zu $R_2$. $R_\mathrm{i}$ ist alles, was außen an Klemme 1 hängt, etwa Quelle und Last parallel. **Gültigkeit:** $U_\mathrm{A}=U_1(1+R/R_2)$ muss in den Grenzen liegen.

:::herleitung Warum das Vorzeichen kippt und wann die Regel hält
Durch $R_2$ fließt $I_2=U_2/R_2$, kein Strom geht in den Eingang, also fließt er auch durch das untere $R$: Der Ausgang liegt bei $U_\mathrm{A}=U_2+R\,I_2$. Das obere $R$ hat dieselbe Spannung und führt denselben Strom, vom Ausgang zu Klemme 1. Also ist $I_1=-I_2$ und $R_\mathrm{ein}=U_1/I_1=-R_2$.

Hier gibt es zwei Rückführungen, das untere $R$ gegenkoppelt, das linke mitkoppelt. Ändert sich $U_\mathrm{A}$, dann ändert sich $\varphi_-$ um den Anteil $\beta_-=R_2/(R_2+R)$ und $\varphi_+$ um $\beta_+=R_\mathrm{i}/(R_\mathrm{i}+R)$. Nur für $\beta_->\beta_+$ überwiegt die Gegenkopplung, also für $R_\mathrm{i}<R_2$.
:::

:::abbildung et1/k11nic 10
Links der Transimpedanzverstärker mit Stromquelle als Eingang. Rechts der NIC mit $R=10$ k$\Omega$ und $R_2=5$ k$\Omega$ bei 1 V an Klemme 1: Der Ausgang steht auf 3 V und schiebt 0,2 mA aus der Klemme heraus.
:::

::::beispiel
Mit $R=10$ k$\Omega$, $R_2=5$ k$\Omega$ und $U_1=1$ V ist $I_2=0{,}2$ mA, $U_\mathrm{A}=3$ V, $I_1=-0{,}2$ mA, also $R_\mathrm{ein}=-5$ k$\Omega$. Die Energie kommt aus der Versorgung des OPV. *Anwendung:* Eine Stromquelle mit 1 mA und Innenwiderstand $R_\mathrm{q}=10$ k$\Omega$ gibt an 1 k$\Omega$ nur 0,909 mA ab, weil ein Teil durch $R_\mathrm{q}$ geht. Parallel dazu ein NIC mit $R_2=R_\mathrm{q}$: Der Leitwert $1/R_\mathrm{q}-1/R_2$ verschwindet, die Last bekommt 1 mA. Die reale Quelle wirkt wie eine ideale. Der NIC liefert genau die 0,1 mA, die $R_\mathrm{q}$ abzweigt.
::::

⁠**Grenzfall:** Ohne Last ist $R_\mathrm{i}=R_\mathrm{q}=R_2$, beide Rückführungen sind gleich stark, die Schleifenverstärkung ist null, und die Regel gilt nicht mehr.

:::aufgabe Aufgabe 9 ★★★ Stromquelle kompensieren
<span class="anker" id="aufg-9"></span>

Ein NIC mit $R=10$ k$\Omega$ und $R_2=4{,}7$ k$\Omega$ liegt parallel zu einer Quelle mit 2 mA und $R_\mathrm{q}=4{,}7$ k$\Omega$. Die Last ist 1 k$\Omega$. (a) Welchen Strom bekommt die Last ohne NIC, welchen mit NIC? (b) Wo steht der OPV-Ausgang? (c) Bis zu welchem Lastwiderstand reicht der Ausgang von 11 V? (d) Warum ist die Schaltung mit Last stabil, ohne Last aber nicht?

:::loesung
(a) Ohne NIC $2\,\mathrm{mA}\cdot4{,}7/5{,}7=1{,}65$ mA, mit NIC 2 mA. (b) $U_1=2$ V, $I_2=0{,}426$ mA, $U_\mathrm{A}=2\,\mathrm{V}+10\,\mathrm{k\Omega}\cdot0{,}426\,\mathrm{mA}=6{,}26$ V. (c) $U_\mathrm{A}=U_1(1+R/R_2)=3{,}13\,U_1\le11$ V ergibt $U_1\le3{,}52$ V, also $R_\mathrm{L}\le1{,}76$ k$\Omega$. (d) Mit Last ist $R_\mathrm{i}=R_\mathrm{q}\parallel1\,\mathrm{k\Omega}=825\,\Omega<R_2$, die Gegenkopplung überwiegt. Ohne Last ist $R_\mathrm{i}=R_2$, die beiden Rückführungen heben sich auf.
:::
:::

::::formelsammlung
**Transimpedanzverstärker**

$$U_\mathrm{A}=-R\,I_\mathrm{E},\qquad r_\mathrm{ein}=\frac{\Delta U_-}{\Delta I_\mathrm{E}}=\frac{R}{1+A}$$

Der Strom $I_\mathrm{E}$ fließt in die virtuelle Masse und durch $R$ in der Rückführung; $r_\mathrm{ein}$ ist ein differenzieller Widerstand.

**Negativimpedanzkonverter**

$$R_\mathrm{ein}=\frac{U_1}{I_1}=-R_2$$

$I_1$ zählt in Klemme 1 hinein, $U_1$ gegen Masse. Der Ausgang liegt bei $U_\mathrm{A}=U_1(1+R/R_2)$ und muss in seinen Grenzen bleiben.

**Stabilität des NIC**

$$\beta_-=R_2/(R_2+R),\qquad \beta_+=R_\mathrm{i}/(R_\mathrm{i}+R),\qquad R_\mathrm{i}<R_2$$

Gegenkopplung über das untere $R$, Mitkopplung über den Weg zum Plus-Eingang; die Regel gilt nur für $\beta_->\beta_+$, also $R_\mathrm{i}<R_2$. $R_\mathrm{i}$ ist alles, was außen an Klemme 1 gegen Masse wirkt.
::::

::::lernkarten
:::karte begriff Transimpedanzverstärker
Was ist ein Transimpedanzverstärker, etwa für den Strom einer Fotodiode?
---
Eine OPV-Schaltung, die einen Strom in eine Spannung wandelt: Der Strom fließt in die virtuelle Masse und muss durch $R$ in der Rückführung, $U_\mathrm{A}=-R\,I_\mathrm{E}$.
--- falsch
Eine OPV-Schaltung, die eine Spannung in einen Strom wandelt: Der Ausgang treibt durch $R$ den Strom $U_\mathrm{E}/R$ in die angeschlossene Last, unabhängig von deren Wert.
--- falsch
Ein Verstärker, der den Strom einer Fotodiode um den Faktor $A$ vergrößert; sein Ausgang liefert den Strom $A\,I_\mathrm{E}$ an die Last.
--- falsch
Eine Schaltung, die den Strom über einen Widerstand gegen Masse in eine Spannung wandelt und diese dann mit $1+R_2/R_1$ weiter verstärkt.
:::
:::karte formel Gleichungen des Transimpedanzverstärkers
Wie groß sind die Ausgangsspannung und der Eingangswiderstand eines Transimpedanzverstärkers mit dem Rückführwiderstand $R$?
---
$U_\mathrm{A}=-R\,I_\mathrm{E},\qquad r_\mathrm{ein}=\frac{\Delta U_-}{\Delta I_\mathrm{E}}=\frac{R}{1+A}$. Mit $R=1$ M$\Omega$ werden 2 µ A zu $-2$ V, und die Quelle sieht nur 10 $\Omega$.
--- falsch
$U_\mathrm{A}=-R\,I_\mathrm{E}$ und $r_\mathrm{ein}=R$: Die Quelle sieht den vollen Rückführwiderstand, mit $R=1$ M$\Omega$ also 1 M$\Omega$.
--- falsch
$U_\mathrm{A}=-A\,R\,I_\mathrm{E}$ und $r_\mathrm{ein}=\frac{R}{1+A}$: Mit $R=1$ M$\Omega$ würden 2 µ A zu 200 kV, der Ausgang schlägt sofort an.
--- falsch
$U_\mathrm{A}=-R\,I_\mathrm{E}$ und $r_\mathrm{ein}=R\,(1+A)$: Der Eingang ist sehr hochohmig, mit $R=1$ M$\Omega$ rund 100 G$\Omega$.
:::
:::karte zusammenhang differenzieller Widerstand
Warum sieht eine Stromquelle am Eingang eines Transimpedanzverstärkers fast einen Kurzschluss, obwohl dort kein Draht nach Masse führt?
---
Bei 2 µ A bewegt sich der Knoten nur um $2\,\mathrm{V}/A=20$ µ V. Das ist ein differenzieller Widerstand, ein Wert für Änderungen, von nur 10 $\Omega$.
--- falsch
Der Knoten ist im OPV über 10 $\Omega$ mit Masse verbunden; über diesen inneren Widerstand fließt der Strom der Quelle nach Masse ab.
--- falsch
Der Rückführwiderstand von 1 M$\Omega$ liegt parallel zur Quelle; zusammen mit ihrem Innenwiderstand ergibt das fast einen Kurzschluss.
--- falsch
Der Knoten bewegt sich nur um 20 µ V, weil der Strom zu klein ist, um eine Spannung zu erzeugen; bei 2 mA wäre der Eingang hochohmig wie jeder andere Eingang.
:::
:::karte begriff Negativimpedanzkonverter
Was macht ein Negativimpedanzkonverter (NIC) an seiner Klemme 1, und woher kommt die Energie dafür?
---
Er wirkt wie ein negativer Widerstand: Bei positiver Spannung schiebt er Strom aus der Klemme heraus, $R_\mathrm{ein}=\frac{U_1}{I_1}=-R_2$. Die Energie kommt aus der Versorgung des OPV.
--- falsch
Er wirkt wie ein sehr großer Widerstand: Bei positiver Spannung nimmt er fast keinen Strom auf, $R_\mathrm{ein}=R_2\,(1+A)$. Energie braucht er dafür keine.
--- falsch
Er kehrt die Spannung an der Klemme um: Liegt dort $+U_1$, gibt er $-U_1$ aus. Der Strom bleibt in Zählpfeilrichtung, die Energie liefert die Quelle an Klemme 1 selbst, die dabei stärker belastet wird.
--- falsch
Er wirkt wie ein negativer Widerstand, $R_\mathrm{ein}=-R_2$. Die Energie dafür stammt aus der Ladung, die der Widerstand $R_2$ zuvor gespeichert hat, wie ein Kondensator.
:::
:::karte herleitung Warum das Vorzeichen kippt
Wie folgt aus der Regel für den gegengekoppelten OPV, dass der NIC an Klemme 1 den Widerstand $R_\mathrm{ein}=-R_2$ zeigt?
---
Aus $\varphi_+=\varphi_-$ folgt $U_1=U_2$, weil Klemme 1 am Plus-Eingang und $R_2$ am Minus-Eingang liegt.
---
Durch $R_2$ fließt $I_2=U_2/R_2$, und derselbe Strom fließt durch das untere $R$, weil kein Strom in den Eingang geht.
---
Der Ausgang liegt deshalb bei $U_\mathrm{A}=U_2+R\,I_2$, weil das untere $R$ zwischen Minus-Eingang und Ausgang liegt.
---
Das obere $R$ zwischen Ausgang und Klemme 1 hat dieselbe Spannung und führt denselben Strom, weil $U_1=U_2$ ist; dieser Strom fließt vom Ausgang zu Klemme 1.
---
Also ist $I_1=-I_2$ und $R_\mathrm{ein}=U_1/I_1=-R_2$, weil der Strom aus der Klemme heraus statt in sie hinein fließt.
:::
:::karte zusammenhang Zwei Rückführungen am NIC
Warum gilt die Regel für den NIC nur, solange der Widerstand $R_\mathrm{i}$, der an Klemme 1 gegen Masse wirkt, kleiner als $R_2$ ist?
---
Das untere $R$ koppelt mit $\beta_-=R_2/(R_2+R)$ gegen, der Weg zum Plus-Eingang mit $\beta_+=R_\mathrm{i}/(R_\mathrm{i}+R)$ mit. Nur für $\beta_->\beta_+$, also $R_\mathrm{i}<R_2$, überwiegt die Gegenkopplung.
--- falsch
Bei $R_\mathrm{i}>R_2$ fließt zu viel Strom in den Plus-Eingang; der Eingangsstrom ist dann nicht mehr klein gegen den Strom durch $R_2$.
--- falsch
Bei $R_\mathrm{i}>R_2$ reicht der Ausgang nicht mehr, weil $U_\mathrm{A}=U_1(1+R/R_2)$ dann für jede Spannung an Klemme 1 über 11 V liegt.
--- falsch
Der NIC hat zwei Rückführungen: Der Weg zum Plus-Eingang koppelt gegen, das untere $R$ koppelt mit; nur für $R_\mathrm{i}>R_2$ überwiegt die Gegenkopplung.
:::
:::karte zusammenhang Reale Stromquelle als ideale
Warum bekommt eine Last von 1 k$\Omega$ an einer Stromquelle mit 1 mA und dem Innenwiderstand $R_\mathrm{q}=10$ k$\Omega$ den vollen Strom, wenn ein NIC mit $R_2=R_\mathrm{q}$ parallel liegt?
---
Der negative Leitwert des NIC hebt den von $R_\mathrm{q}$ auf, $1/R_\mathrm{q}-1/R_2$ verschwindet. Der NIC liefert genau die 0,1 mA, die $R_\mathrm{q}$ abzweigt.
--- falsch
Der NIC schließt $R_\mathrm{q}$ kurz, sodass durch ihn kein Strom mehr fließen kann; die Last liegt dann direkt an der idealen Quelle.
--- falsch
Der NIC verdoppelt den Innenwiderstand auf 20 k$\Omega$; dadurch zweigt $R_\mathrm{q}$ nur noch halb so viel ab, und der Rest reicht der Last.
--- falsch
Der NIC liefert zusätzlich 1 mA aus seiner Versorgung; zusammen mit der Quelle fließen 2 mA, von denen die Last genau die Hälfte bekommt.
:::
:::karte zusammenhang NIC ohne Last
Was passiert mit dem NIC an der Stromquelle, wenn man die Last entfernt?
---
Dann ist $R_\mathrm{i}=R_\mathrm{q}=R_2$: Beide Rückführungen sind gleich stark, die Schleifenverstärkung ist null, und die Regel gilt nicht mehr. Mit Last ist $R_\mathrm{i}<R_2$.
--- falsch
Nichts: Der NIC liefert weiter seinen Strom, und an der offenen Klemme stellt sich eine feste Spannung ein, die die Regel für den OPV bestimmt.
--- falsch
Der Ausgang geht auf 0 V, weil ohne Last kein Strom fließt; der NIC schaltet sich damit von selbst ab und bleibt in einem stabilen Zustand.
--- falsch
Dann ist $R_\mathrm{i}$ unendlich groß und viel größer als $R_2$; die Gegenkopplung überwiegt besonders stark, und die Schaltung wird besonders stabil.
:::
:::karte zusammenhang Energie des NIC
Woher kommt die Energie, die ein NIC als negativer Widerstand an seiner Klemme abgibt?
---
Aus der Versorgung des OPV: Der Ausgang steht höher als die Klemme, etwa 3 V bei 1 V an der Klemme, und treibt über das obere $R$ Strom aus ihr heraus.
--- falsch
Aus dem Widerstand $R_2$, der in jedem Umlauf geladen und wieder entladen wird; ein NIC kann deshalb nur kurze Zeit Energie abgeben.
--- falsch
Aus der Quelle an Klemme 1 selbst: Der NIC nimmt ihr Energie ab und gibt sie mit umgekehrtem Vorzeichen zurück, in Summe also null.
--- falsch
Aus den Eingängen des OPV, die bei einem negativen Widerstand Strom liefern; deshalb gilt am NIC die Regel $I_+=I_-=0$ nicht.
:::
::::
