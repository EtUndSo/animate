---
title: Stufe 9: Gleichrichter und Ladungspumpe
pfad: Elektrotechnik / 1. Semester / ET1 – Grundgebiete der Elektrotechnik 1: Einführung in die Schaltungsanalyse / Halbleiter und Dioden
adresse: elektrotechnik/1-semester/grundlagen-der-elektrotechnik/halbleiter-und-dioden
knoten: Kapitel 9: Halbleiter und Dioden
order: 1191100
summary: Der Einweggleichrichter verschenkt jede zweite Halbwelle.
tags: Brückengleichrichter, Glättung
lang: de
---

<span class="anker" id="stufe-9"></span>

:::zweck
Der Einweggleichrichter verschenkt jede zweite Halbwelle. Diese Stufe nutzt beide, und sie zeigt, wie man mit Dioden und Kondensatoren eine Spannung über die Quellenspannung hebt.
:::

**Die Idee.** Der __Brückengleichrichter__ (Graetz-Schaltung) besteht aus vier Dioden in einer Raute (Abb. [11](#abb-11)). Sie schalten die Last in jeder Halbwelle so um, dass der Strom sie immer von oben nach unten durchläuft. Bei positiver Spannung links läuft er durch D$_1$, die Last und D$_3$. Dabei liegt D$_2$ mit der Kathode oben auf dem hohen Potenzial, mit der Anode am tiefen Eingang, sie sperrt, ebenso D$_4$. In der anderen Halbwelle tauschen die Paare.

:::abbildung et1/k9graetz 11
Oben: Brücke in beiden Halbwellen, leitende Dioden farbig, gesperrte grau, das Pluszeichen markiert den höheren Eingang. Der Strom durch die Last $R$ hat immer dieselbe Richtung. Unten: Eingang $u_\mathrm e$ (grau) und Ausgang $u_\mathrm a$ (blau) für $\hat u=12$ V, $U_\mathrm F=0{,}7$ V.
:::

:::satz Satz 9.1 (Brückengleichrichter)
<span class="anker" id="satz-9-1"></span>

Im Modell mit Durchlassspannung gilt, da der Strom immer zwei Dioden in Reihe durchläuft,

<span class="anker" id="gl-9-1"></span>
$$u_\mathrm a=\begin{cases}|u_\mathrm e|-2U_\mathrm F&|u_\mathrm e|>2U_\mathrm F\\0&\text{sonst.}\end{cases} \tag{9.1}$$

Eine gesperrte Diode trägt höchstens $\hat u-U_\mathrm F$.
:::

⁠**So liest man das:** Für $|u_\mathrm e|<2U_\mathrm F$ leiten beide Paare nicht, $u_\mathrm a$ bleibt null. Am gesunkenen Scheitel liest man die doppelte Durchlassspannung ab. **Gültigkeit:** ohmsche Last. Eingang und Ausgang haben keinen gemeinsamen Bezugspunkt.

::::beispiel
Der Scheitel ist $12\,\mathrm{V}-1{,}4\,\mathrm{V}=10{,}6$ V, beim Einweggleichrichter 11,3 V. Die Lücke dauert je Halbwelle 0,74 ms, das sind 7,4 % der Zeit. Der Mittelwert ist 6,29 V, beim Einweggleichrichter nur 3,48 V.
::::

⁠**Grenzfälle:** Für $U_\mathrm F\to0$ ist $u_\mathrm a=|u_\mathrm e|$. Für $\hat u<1{,}4$ V bleibt der Ausgang null.

:::ltspice Brückengleichrichter
⁠**Zeichnen:** Quelle mit `SINE(0 12 50)` zwischen `a` und `b`. Dioden DM von `a` nach `p`, von `b` nach `p`, von Masse nach `a` und von Masse nach `b`. `res` 1k von `p` nach Masse.

⁠**Direktive:** `.tran 40m`

⁠**Was du siehst:** `V(p)` wie in Abb. [11](#abb-11), Scheitel 10,57 V, Mittelwert 6,29 V. Die Spannung $V(p,a)$ an der gesperrten Diode erreicht 11,28 V. Die Rechnung ergibt 10,6 V, 6,29 V und 11,3 V. Für Aufgabe [11](#aufg-11) setze 24 statt 12 ein.
:::

:::frage Das pulsiert noch stark. Ist das schon Gleichspannung?
Noch nicht. Ein Kondensator parallel zur Last (__Glättung__) lädt sich auf den Scheitel und speist die Last in der Lücke. In 10 ms verliert er $\Delta U=I\,\Delta t/C$ ([Kapitel 3](/wissen/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/der-kondensator/der-kondensator.html)). Mit $I=10{,}6$ mA und $C=470$ µ F sind das 0,23 V. Die Dioden leiten dann nur noch kurz am Scheitel.
:::

**Ladungspumpe.** Sie erzeugt aus einer Gleichspannung $U_\mathrm e$ eine höhere, ohne Spule. Die Dioden gelten hier als ideal (Abb. [12](#abb-12)). *Schritt 1:* Der Umschalter legt die untere Platte von $C_1$ an Masse. $C_1$ lädt sich über D$_1$ auf $U_\mathrm e$. *Schritt 2:* Der Umschalter legt die untere Platte an $U_\mathrm e$. Die Spannung an $C_1$ kann nicht springen ([Kapitel 3](/wissen/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/der-kondensator/der-kondensator.html)), also springt die obere Platte auf $2U_\mathrm e$. D$_1$ sperrt, weil ihre Kathode nun höher liegt, D$_2$ leitet, und $C_1$ gibt Ladung an den Ausgangskondensator $C_2$ ab. Nach wenigen Takten ist $U_\mathrm a\approx2U_\mathrm e$. In der Praxis begrenzen kleine Widerstände die Stromspitzen. Mit weiteren Pumpstufen nach demselben Schema steigt die Spannung weiter.

:::abbildung et1/k9pumpe 12
Ladungspumpe; die Stromwege der beiden Schritte sind farbig. Links lädt $U_\mathrm e$ den Kondensator $C_1$. Rechts liegen $U_\mathrm e$ und die Spannung an $C_1$ in Reihe und speisen $C_2$.
:::

:::herleitung Spannung nach $k$ Takten für $C_1=C_2$
Im ersten Schritt lädt sich auch $C_2$ über beide Dioden auf $U_\mathrm e$. Im Pumpschritt verbinden sich $C_1$ mit $2U_\mathrm e$ und $C_2$ mit $U_\mathrm a$. Die Ladung bleibt erhalten, gleiche Kondensatoren enden beim Mittelwert: $U_\mathrm a'=(2U_\mathrm e+U_\mathrm a)/2$. Der Abstand zum Endwert $2U_\mathrm e$ halbiert sich je Takt: $U_\mathrm a(k)=2U_\mathrm e-U_\mathrm e\,2^{-k}$.
:::

Mit $U_\mathrm e=5$ V ergibt das 7,5 V, 8,75 V, 9,38 V, und so weiter bis 10 V. Mit realen Dioden verliert man zweimal $U_\mathrm F$: Der Endwert ist $2U_\mathrm e-2U_\mathrm F=8{,}6$ V. **Grenzfall:** Fließt am Ausgang Strom, fehlt je Takt Ladung, und $U_\mathrm a$ bleibt unter dem Endwert.

:::aufgabe Aufgabe 11 ★★ Netzteil
<span class="anker" id="aufg-11"></span>

Eine Brücke liegt an $\hat u=24$ V, $U_\mathrm F=0{,}7$ V.

<ol class="al">

<li>

Wie groß ist der Scheitel von $u_\mathrm a$? Welche Sperrspannung muss jede Diode aushalten?

</li>

<li>

Welchen Anteil der Zeit ist $u_\mathrm a=0$?

</li>

<li>

Die Last zieht 100 mA. Welches $C$ begrenzt die Schwankung auf 1 V? Wie groß müsste es beim Einweggleichrichter sein, und warum?

</li>

</ol>

:::loesung
(a) $24\,\mathrm{V}-1{,}4\,\mathrm{V}=22{,}6$ V, Sperrspannung $24\,\mathrm{V}-0{,}7\,\mathrm{V}=23{,}3$ V. (b) $u_\mathrm a=0$ für $|\sin|<1{,}4/24$, also 3,34° um jeden Nulldurchgang, das sind $2\cdot3{,}34^\circ/180^\circ=3{,}7$ % der Zeit. (c) $C=I\,\Delta t/\Delta U=100\,\mathrm{mA}\cdot10\,\mathrm{ms}/1\,\mathrm{V}=1000$ µ F. Beim Einweggleichrichter kommt der Nachschub nur alle 20 ms, also 2000 µ F.
:::
:::

:::aufgabe Aufgabe 12 ★★ Pumpen zählen
<span class="anker" id="aufg-12"></span>

$U_\mathrm e=3$ V, $C_1=C_2$, ideale Dioden.

<ol class="al">

<li>

Wie groß ist $U_\mathrm a$ nach 1, 2 und 3 Takten?

</li>

<li>

Nach wie vielen Takten sind 99 % des Endwerts erreicht?

</li>

<li>

Welchen Endwert ergeben reale Dioden mit 0,7 V? Was bleibt bei $U_\mathrm e=1{,}5$ V, und was folgt daraus für Schaltungen mit kleiner Spannung?

</li>

</ol>

:::loesung
(a) $U_\mathrm a(k)=6\,\mathrm{V}-3\,\mathrm{V}\cdot2^{-k}$: 4,5 V, 5,25 V, 5,63 V. (b) $3\,\mathrm{V}\cdot2^{-k}\le0{,}06\,\mathrm{V}$ verlangt $2^k\ge50$, also $k=6$. (c) $6\,\mathrm{V}-1{,}4\,\mathrm{V}=4{,}6$ V. Bei 1,5 V bleiben $3\,\mathrm{V}-1{,}4\,\mathrm{V}=1{,}6$ V, kaum mehr als der Eingang. Bei kleinen Spannungen ersetzt man die Dioden daher durch Schalter.
:::
:::

::::formelsammlung
**Brückengleichrichter**

$$u_\mathrm a=\begin{cases}|u_\mathrm e|-2U_\mathrm F&|u_\mathrm e|>2U_\mathrm F\\0&\text{sonst.}\end{cases}$$

Modell mit Durchlassspannung; der Strom durchläuft immer zwei Dioden in Reihe. Gilt für eine ohmsche Last; Eingang und Ausgang haben keinen gemeinsamen Bezugspunkt.

**Sperrspannung je Diode**

$$\hat u-U_\mathrm F$$

Höchste Spannung an einer gesperrten Diode der Brücke.

**Glättung**

$$\Delta U=I\,\Delta t/C$$

Spannungsverlust des Kondensators parallel zur Last in der Zeit $\Delta t$ zwischen zwei Nachladungen, bei Laststrom $I$.

**Ladungspumpe je Takt**

$$U_\mathrm a'=(2U_\mathrm e+U_\mathrm a)/2$$

Ladungserhaltung beim Pumpschritt für $C_1=C_2$ und ideale Dioden: $C_1$ mit $2U_\mathrm e$ und $C_2$ mit $U_\mathrm a$ enden beim Mittelwert.

**Ladungspumpe nach mehreren Takten**

$$U_\mathrm a(k)=2U_\mathrm e-U_\mathrm e\,2^{-k}$$

Der Abstand zum Endwert $2U_\mathrm e$ halbiert sich je Takt. Fließt am Ausgang Strom, bleibt $U_\mathrm a$ unter dem Endwert.

**Endwert mit realen Dioden**

$$2U_\mathrm e-2U_\mathrm F$$

Zweimal die Durchlassspannung geht verloren.
::::

::::lernkarten
:::karte begriff Brückengleichrichter
Wie ist ein Brückengleichrichter aufgebaut, und was erreicht er gegenüber dem Einweggleichrichter?
---
Vier Dioden in einer Raute, auch Graetz-Schaltung genannt. Sie schalten die Last in jeder Halbwelle so um, dass der Strom sie immer in derselben Richtung durchläuft; so werden beide Halbwellen genutzt.
--- falsch
Zwei Dioden in Reihe mit der Last, die abwechselnd leiten. So wird die negative Halbwelle abgeschnitten, und der Ausgang ist doppelt so hoch wie beim Einweggleichrichter.
--- falsch
Vier Dioden in einer Raute, die alle gleichzeitig leiten. So teilt sich der Strom auf vier Wege auf, und jede Diode trägt nur ein Viertel des Laststroms.
--- falsch
Vier Dioden in einer Raute, auch Graetz-Schaltung genannt. Sie kehren die Richtung des Laststroms in jeder Halbwelle um, sodass am Ausgang eine saubere Wechselspannung ohne Lücken und ohne Verlust steht.
:::
:::karte zusammenhang Stromweg in der Brücke
Welche Dioden leiten in der Brücke bei positiver Spannung am linken Eingang, und warum sperrt D$_2$ dabei?
---
Der Strom läuft durch D$_1$, die Last und D$_3$. D$_2$ liegt mit der Kathode oben auf dem hohen Potenzial und mit der Anode am tiefen Eingang, sie sperrt, ebenso D$_4$; in der anderen Halbwelle tauschen die Paare.
--- falsch
Der Strom läuft durch D$_1$, D$_2$ und die Last, weil beide Dioden am linken Eingang liegen. D$_3$ und D$_4$ sperren, weil sie rechts an der negativen Seite hängen.
--- falsch
Alle vier Dioden leiten, und der Strom teilt sich gleichmäßig auf. D$_2$ führt dabei nur einen kleineren Strom, weil sie mit der Kathode oben auf dem hohen Potenzial liegt.
--- falsch
Der Strom läuft durch D$_1$, die Last und D$_3$. D$_2$ sperrt, weil ihre Anode oben auf dem hohen Potenzial liegt und ihre Kathode am tiefen Eingang; in der anderen Halbwelle tauschen die beiden Paare ihre Rollen.
:::
:::karte formel Ausgang der Brücke
Wie hängt die Ausgangsspannung $u_\mathrm a$ einer Brücke im Modell mit Durchlassspannung von der Eingangsspannung $u_\mathrm e$ ab, und warum steht dort $2U_\mathrm F$?
---
$u_\mathrm a=|u_\mathrm e|-2U_\mathrm F$ für $|u_\mathrm e|>2U_\mathrm F$, sonst $u_\mathrm a=0$, weil der Strom immer zwei Dioden in Reihe durchläuft. Gilt für eine ohmsche Last.
--- falsch
$u_\mathrm a=|u_\mathrm e|-U_\mathrm F$ für $|u_\mathrm e|>U_\mathrm F$, sonst $u_\mathrm a=0$, weil der Strom immer nur eine Diode durchläuft; die zweite wirkt nur in der anderen Halbwelle.
--- falsch
$u_\mathrm a=|u_\mathrm e|-4U_\mathrm F$ für $|u_\mathrm e|>4U_\mathrm F$, sonst $u_\mathrm a=0$, weil der Strom alle vier Dioden der Raute nacheinander durchläuft.
--- falsch
$u_\mathrm a=u_\mathrm e-2U_\mathrm F$ für $u_\mathrm e>2U_\mathrm F$, sonst $u_\mathrm a=u_\mathrm e+2U_\mathrm F$, weil der Strom zwei Dioden durchläuft und die negative Halbwelle negativ bleibt.
:::
:::karte zusammenhang Sperrspannung der Brückendioden
Welche Sperrspannung muss jede Diode einer Brücke an einer Wechselspannung mit 24 V Scheitelwert aushalten, und warum?
---
$24\,\mathrm{V}-0{,}7\,\mathrm{V}=23{,}3$ V: Eine gesperrte Diode trägt höchstens $\hat u-U_\mathrm F$, weil ihre Kathode am oberen Ausgang liegt, nur $U_\mathrm F$ unter dem hohen Eingang, und ihre Anode am tiefen Eingang.
--- falsch
$24\,\mathrm{V}-1{,}4\,\mathrm{V}=22{,}6$ V, weil an den beiden leitenden Dioden zusammen 1,4 V abfallen und die gesperrte Diode genau die Spannung am Ausgang trägt.
--- falsch
Die Hälfte von 24 V, also 12 V, weil sich die Sperrspannung gleichmäßig auf die beiden gesperrten Dioden aufteilt, die in dieser Halbwelle hintereinander zwischen den beiden Eingängen liegen.
--- falsch
48 V, weil die gesperrte Diode in der einen Halbwelle $+24$ V und in der anderen $-24$ V sieht und beide Werte zusammen aushalten muss.
:::
:::karte zusammenhang Brücke und Einweggleichrichter im Vergleich
Wie groß sind Scheitel und Mittelwert der Ausgangsspannung einer Brücke an 12 V Scheitelwert im Vergleich zum Einweggleichrichter?
---
Der Scheitel ist $12\,\mathrm{V}-1{,}4\,\mathrm{V}=10{,}6$ V statt 11,3 V, der Mittelwert 6,29 V statt nur 3,48 V. Die Brücke verliert eine Durchlassspannung mehr, nutzt aber beide Halbwellen.
--- falsch
Der Scheitel ist mit 11,3 V gleich, der Mittelwert mit 6,96 V genau doppelt so groß, weil die Brücke jede Halbwelle unverändert durchlässt.
--- falsch
Der Scheitel ist $12\,\mathrm{V}+1{,}4\,\mathrm{V}=13{,}4$ V, weil sich die Spannungen der beiden leitenden Dioden zur Eingangsspannung addieren; der Mittelwert ist mit 6,29 V fast doppelt so groß.
--- falsch
Der Scheitel ist $12\,\mathrm{V}-2{,}8\,\mathrm{V}=9{,}2$ V, weil vier Dioden je 0,7 V abziehen; der Mittelwert ist mit 3,48 V so groß wie beim Einweggleichrichter.
:::
:::karte begriff Glättung
Was bewirkt die Glättung hinter einem Gleichrichter, und wie stark schwankt die Spannung dabei?
---
Ein Kondensator parallel zur Last lädt sich auf den Scheitel und speist die Last in der Lücke. In der Zeit $\Delta t$ verliert er $\Delta U=I\,\Delta t/C$; die Dioden leiten dann nur noch kurz am Scheitel.
--- falsch
Ein Widerstand in Reihe zur Last begrenzt die Stromspitzen der Dioden. Die Spannung schwankt danach um $\Delta U=I\,R$, und die Dioden leiten während der ganzen Halbwelle.
--- falsch
Ein Kondensator in Reihe zur Last sperrt die Wechselanteile. Die Spannung schwankt um $\Delta U=C\,\Delta t/I$; je größer der Laststrom, desto glatter wird sie.
--- falsch
Ein Kondensator parallel zur Last lädt sich auf den Mittelwert und gibt in der Lücke den Rest ab. Er verliert dabei $\Delta U=I\,\Delta t/C$, und die Dioden leiten dafür ohne jede Unterbrechung weiter.
:::
:::karte zusammenhang Glättung beim Einweggleichrichter
Warum braucht ein Einweggleichrichter an 50 Hz für dieselbe Last und dieselbe Schwankung einen doppelt so großen Glättungskondensator wie eine Brücke?
---
Beim Einweggleichrichter kommt der Nachschub nur alle 20 ms statt alle 10 ms. Wegen $\Delta U=I\,\Delta t/C$ verlangt das doppelte $\Delta t$ das doppelte $C$, bei 100 mA und 1 V also 2000 µ F statt 1000 µ F.
--- falsch
Der Einweggleichrichter liefert nur die halbe Spannung, und die Energie im Kondensator wächst mit dem Quadrat der Spannung. Für dieselbe gespeicherte Energie braucht er deshalb die doppelte Kapazität.
--- falsch
Beim Einweggleichrichter fließt der Ladestrom durch nur eine Diode statt durch zwei. Der größere Ladestrom verlangt einen Kondensator, der doppelt so viel Ladung aufnehmen kann.
--- falsch
Beim Einweggleichrichter lädt sich der Kondensator nur auf den halben Scheitel auf. Um bei halber Spannung dieselbe Ladung zu speichern, braucht er die doppelte Kapazität.
:::
:::karte zusammenhang Ladungspumpe
Wie hebt eine Ladungspumpe mit zwei Dioden, zwei Kondensatoren und einem Umschalter eine Gleichspannung $U_\mathrm e$ auf fast $2U_\mathrm e$?
---
Erst liegt die untere Platte von $C_1$ an Masse, und $C_1$ lädt sich über D$_1$ auf $U_\mathrm e$. Dann kommt sie an $U_\mathrm e$; da die Spannung an $C_1$ nicht springt, springt die obere Platte auf $2U_\mathrm e$, und $C_1$ lädt über D$_2$ den $C_2$.
--- falsch
Zuerst lädt sich $C_1$ über D$_1$ auf $U_\mathrm e$, dann $C_2$ über D$_2$ ebenfalls auf $U_\mathrm e$. Beide Kondensatoren liegen am Ausgang in Reihe, und ihre Spannungen addieren sich ohne jedes Umschalten zu $2U_\mathrm e$, sobald beide voll geladen sind.
--- falsch
Die Dioden laden $C_1$ in jedem Takt auf $U_\mathrm e$ und entladen ihn schlagartig über $C_2$. Der Stromstoß erzeugt wie in einer Spule eine Induktionsspannung, die $C_2$ auf $2U_\mathrm e$ hebt.
--- falsch
Zuerst liegt die untere Platte von $C_1$ an $U_\mathrm e$, und $C_1$ lädt sich auf $2U_\mathrm e$. Dann legt der Umschalter sie an Masse, und $C_1$ gibt die Hälfte seiner Spannung über D$_1$ an $C_2$ weiter.
:::
:::karte formel Spannung der Ladungspumpe
Welche Spannung liefert eine Ladungspumpe mit $C_1=C_2$ und idealen Dioden nach $k$ Takten, und welcher Endwert ergibt sich mit realen Dioden?
---
$U_\mathrm a(k)=2U_\mathrm e-U_\mathrm e\,2^{-k}$: Der Abstand zum Endwert $2U_\mathrm e$ halbiert sich je Takt. Mit realen Dioden verliert man zweimal $U_\mathrm F$, der Endwert ist $2U_\mathrm e-2U_\mathrm F$.
--- falsch
$U_\mathrm a(k)=k\,U_\mathrm e$: Jeder Takt legt eine volle Eingangsspannung drauf, bis die Dioden durchbrechen. Mit realen Dioden ist es $k\,(U_\mathrm e-U_\mathrm F)$.
--- falsch
$U_\mathrm a(k)=2U_\mathrm e-U_\mathrm e\,2^{-k}$: Der Abstand zum Endwert halbiert sich je Takt. Mit realen Dioden verliert man nur einmal $U_\mathrm F$, der Endwert ist $2U_\mathrm e-U_\mathrm F$.
--- falsch
$U_\mathrm a(k)=2U_\mathrm e\,(1-\mathrm{e}^{-k})$: Die Spannung steigt wie beim Laden eines RC-Kreises. Mit realen Dioden bleibt der Endwert $2U_\mathrm e$, nur das Laden dauert länger.
:::
:::karte herleitung Spannung nach k Takten
Wie folgt für $C_1=C_2$ aus der Ladungserhaltung die Spannung $U_\mathrm a(k)=2U_\mathrm e-U_\mathrm e\,2^{-k}$ nach $k$ Takten?
---
Im ersten Schritt lädt sich auch $C_2$ über beide Dioden auf $U_\mathrm e$, weil die Eingangsspannung über D$_1$ und D$_2$ bis zum Ausgang durchgreift.
---
Im Pumpschritt verbinden sich $C_1$ mit $2U_\mathrm e$ und $C_2$ mit $U_\mathrm a$, weil die obere Platte von $C_1$ auf $2U_\mathrm e$ springt und D$_2$ leitet.
---
Danach ist $U_\mathrm a'=(2U_\mathrm e+U_\mathrm a)/2$, weil die Ladung erhalten bleibt und gleiche Kondensatoren beim Mittelwert enden.
---
Der Abstand zum Endwert $2U_\mathrm e$ halbiert sich also je Takt, und mit dem Anfangsabstand $U_\mathrm e$ folgt $U_\mathrm a(k)=2U_\mathrm e-U_\mathrm e\,2^{-k}$, weil $k$ Halbierungen den Faktor $2^{-k}$ ergeben.
:::
:::karte zusammenhang Ladungspumpe bei kleiner Spannung
Was bleibt von einer Ladungspumpe mit realen Dioden ($U_\mathrm F=0{,}7$ V) bei $U_\mathrm e=1{,}5$ V übrig, und was folgt daraus?
---
Der Endwert ist $3\,\mathrm{V}-1{,}4\,\mathrm{V}=1{,}6$ V, kaum mehr als der Eingang. Bei kleinen Spannungen ersetzt man die Dioden daher durch Schalter.
--- falsch
Der Endwert ist $3\,\mathrm{V}-0{,}7\,\mathrm{V}=2{,}3$ V, weil nur die Ausgangsdiode Spannung kostet. Die Pumpe lohnt sich deshalb gerade bei kleinen Spannungen.
--- falsch
Der Endwert ist 3 V wie bei idealen Dioden, weil der Kondensator die Durchlassspannung im Pumpschritt wieder ausgleicht. Die Dioden spielen hier keine Rolle.
--- falsch
Unter $2U_\mathrm F=1{,}4$ V Eingangsspannung arbeitet die Pumpe gar nicht, und bei 1,5 V liefert sie nur 0,1 V. Man braucht dann eine Spule.
:::
::::
