---
title: Stufe 8: Zwei Schaltungen, die $U_\mathrm{BE}$ nutzen
pfad: Elektrotechnik / 1. Semester / ET1 – Grundgebiete der Elektrotechnik 1: Einführung in die Schaltungsanalyse / Der Bipolartransistor
adresse: elektrotechnik/1-semester/grundlagen-der-elektrotechnik/der-bipolartransistor
knoten: Kapitel 10: Der Bipolartransistor
order: 1201000
summary: Bisher war U BE eine Störung.
tags: Stromspiegel, Referenzstrom, Brumm
lang: de
---

<span class="anker" id="stufe-8"></span>

:::zweck
Bisher war $U_\mathrm{BE}$ eine Störung. Diese Stufe nutzt seine zwei Eigenschaften: Gleiches $U_\mathrm{BE}$ heißt gleicher Strom, und bei Stromänderungen bleibt $U_\mathrm{BE}$ fast gleich.
:::

**Die Idee: Stromspiegel.** Nach [(2.1)](warum-strom-durch-die-gesperrte-diode-fliet.html#gl-2-1) legt $U_\mathrm{BE}$ den Strom fest. Zwei gleiche Transistoren mit derselben Spannung $U_\mathrm{BE}$ führen also denselben Strom. Im __Stromspiegel__ (Abb. [9](#abb-9), links) ist T1 als Diode geschaltet: Basis und Kollektor sind verbunden. Der Strom $I_\mathrm{ref}$ durch den Widerstand stellt an T1 genau die Spannung $U_\mathrm{BE}$ ein, die dieser Strom braucht. T2 hängt an derselben Spannung und kopiert den Strom in einen anderen Zweig, unabhängig von seiner Last.

:::satz Satz 8.1 (Stromspiegel)
<span class="anker" id="satz-8-1"></span>

Mit gleichen Transistoren und $I_\mathrm{B1}=I_\mathrm{B2}$ gilt

<span class="anker" id="gl-8-1"></span>
$$I_\mathrm{ref}=\frac{U_\mathrm{CC}-U_\mathrm{BE}}{R_\mathrm{ref}}=I_\mathrm{C1}+I_\mathrm{B1}+I_\mathrm{B2}=(B+2)I_\mathrm{B2},\qquad I_\mathrm{C2}=B\,I_\mathrm{B2}=\frac{I_\mathrm{ref}}{1+\frac2B}\approx I_\mathrm{ref}. \tag{8.1}$$
:::

⁠**So liest man das:** $I_\mathrm{ref}$ ist der __Referenzstrom__. Die beiden Basisströme zweigen von ihm ab. Daher der kleine Fehler $2/B$. **Gültigkeit:** T2 aktiv, gleiche Transistoren und gleiche Temperatur, etwa auf einem Chip. Über die Neigung der Kennlinie liefert T2 bei großem $U_\mathrm{CE2}$ etwas mehr.

::::beispiel
Mit $R_\mathrm{ref}=5{,}7$ k$\Omega$ ist $I_\mathrm{ref}=2$ mA und $I_\mathrm{C2}=1{,}98$ mA, mit $R_\mathrm{L}$ beliebig bis $11{,}8\,\mathrm{V}/1{,}98\,\mathrm{mA}=5{,}96$ k$\Omega$. Danach wäre T2 gesättigt. Mit [(3.1)](eine-flache-viele-kennlinien.html#gl-3-1) wäre bei $U_\mathrm{CE2}=6$ V und $U_\mathrm{CE1}=0{,}6$ V der Strom in T2 um 7 % größer.
::::

⁠**Grenzfall:** Für $B\to\infty$ ist $I_\mathrm{C2}=I_\mathrm{ref}$.

**Die Idee: Spannungsregler.** Ein Gleichrichter mit Glättung ([Kapitel 9](/wissen/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/halbleiter-und-dioden/halbleiter-und-dioden.html)) liefert eine Gleichspannung mit einer Restwelligkeit, dem __Brumm__. Im Regler (Abb. [9](#abb-9), rechts) hält eine Zener-Diode die Basis auf $U_\mathrm{Z}$. Der Emitter ist der Ausgang und liegt eine Diodenspannung tiefer. Sinkt die Ausgangsspannung, weil die Last mehr Strom zieht, wächst $U_\mathrm{BE}$, und der Transistor liefert mehr nach. Über $U_\mathrm{CE}$ fällt der Rest der Eingangsspannung ab. Der Laststrom fließt nicht durch $R_1$, die Basis braucht nur den $B$-ten Teil. Die Zener-Diode wird also kaum belastet.

:::satz Satz 8.2 (Spannungsregler mit Zener-Diode)
<span class="anker" id="satz-8-2"></span>

Aus der Masche über Zener-Diode, BE-Strecke und Last folgt

<span class="anker" id="gl-8-2"></span>
$$U_\mathrm{A}=U_\mathrm{Z}-U_\mathrm{BE}. \tag{8.2}$$
:::

⁠**So liest man das:** $U_\mathrm{E,min}$ ist das Minimum der Eingangsspannung $U_\mathrm{E}$ im Brummtal, $U_\mathrm{A}$ die Ausgangsspannung. **Gültigkeit:** Es muss immer $U_\mathrm{E}>U_\mathrm{A}+U_\mathrm{CE,sat}$ gelten, damit T aktiv bleibt, und $R_1$ muss genug Strom liefern: $(U_\mathrm{E,min}-U_\mathrm{Z})/R_1>I_\mathrm{B}$. Sonst fällt die Zener-Diode aus dem Durchbruch, und der Brumm erreicht den Ausgang.

:::abbildung et1/k10spiegel 9
Links Stromspiegel: T1 als Diode erzeugt $U_\mathrm{BE}$, T2 kopiert den Strom. Mitte Spannungsregler mit Zener-Diode, der Emitter ist der Ausgang. Rechts der Verlauf: Die Eingangsspannung schwankt zwischen 10,5 V und 13,5 V, der Ausgang bleibt bei 5,6 V.
:::

::::beispiel
$U_\mathrm{Z}=6{,}2$ V ergibt $U_\mathrm{A}=5{,}6$ V. Bei 50 mA Last braucht die Basis 0,25 mA. Mit $R_1=1$ k$\Omega$ und $U_\mathrm{E}=12$ V$\,\pm1{,}5$ V fließen durch die Zener-Diode 4,05 mA bis 7,05 mA. Eine Zener-Diode mit 10 $\Omega$ Kleinsignalwiderstand macht aus 3 V Brumm nur 30 mV. Im Transistor entstehen bis zu $7{,}9\,\mathrm{V}\cdot50\,\mathrm{mA}=395$ mW, gerade unter $P_\mathrm{max}$. Der Regler wandelt die überschüssige Spannung in Wärme. Mit 0,68 V statt 0,6 V, dem genaueren $U_\mathrm{BE}$ bei 50 mA, wäre $U_\mathrm{A}$ um 80 mV kleiner.
::::

⁠**Grenzfall:** Ohne Last ist $I_\mathrm{B}\approx0$, $U_\mathrm{A}$ steigt leicht, $U_\mathrm{Z}$ bleibt.

:::frage Warum nicht die Zener-Diode allein?
Dann müsste der Vorwiderstand bei tiefster Eingangsspannung die ganzen 50 mA und dazu einen Rest für die Zener-Diode liefern. Bei Spitzenspannung flösse die Differenz durch die Zener-Diode, und der Vorwiderstand heizte mit rund 0,7 W. Der Transistor trennt beides: Die Zener-Diode gibt die Spannung vor, die Versorgung liefert den Strom über den Kollektor. Leistungstransistoren und daraus abgeleitete Bauteile schalten auch große Ströme, etwa in Umrichtern für Elektromotoren.
:::

:::aufgabe Aufgabe 10 ★★ Spiegel und Regler
<span class="anker" id="aufg-10"></span>

(a) Welches $R_\mathrm{ref}$ ergibt an $U_\mathrm{CC}=12$ V den Referenzstrom 1 mA? Wie groß ist $I_\mathrm{C2}$ für $B=200$ und für $B=50$? (b) Bis zu welchem $R_\mathrm{L}$ arbeitet der Spiegel bei $B=200$? (c) Ein Regler hat $U_\mathrm{Z}=9{,}1$ V, $R_1=470\,\Omega$, 30 mA Last, $U_\mathrm{E}$ von 12 V bis 15 V. Bestimme $U_\mathrm{A}$, den kleinsten Z-Strom, die größte Transistorleistung und die Spannungsreserve nach unten.

:::loesung
(a) $R_\mathrm{ref}=11{,}4\,\mathrm{V}/1\,\mathrm{mA}=11{,}4$ k$\Omega$. $I_\mathrm{C2}=1\,\mathrm{mA}/1{,}01=0{,}990$ mA, bei $B=50$ sind es $1\,\mathrm{mA}/1{,}04=0{,}962$ mA.

(b) $R_\mathrm{L}\le11{,}8\,\mathrm{V}/0{,}990\,\mathrm{mA}=11{,}9$ k$\Omega$.

(c) $U_\mathrm{A}=8{,}5$ V, $I_\mathrm{B}=0{,}15$ mA. Bei 12 V fließen durch $R_1$ dann $2{,}9\,\mathrm{V}/470\,\Omega=6{,}17$ mA, durch die Z-Diode 6,02 mA. Bei 15 V ist $P=6{,}5\,\mathrm{V}\cdot30\,\mathrm{mA}=195$ mW. Reserve: $12\,\mathrm{V}-8{,}5\,\mathrm{V}-0{,}2\,\mathrm{V}=3{,}3$ V.
:::
:::

::::formelsammlung
**Stromspiegel**

$$I_\mathrm{ref}=\frac{U_\mathrm{CC}-U_\mathrm{BE}}{R_\mathrm{ref}}=I_\mathrm{C1}+I_\mathrm{B1}+I_\mathrm{B2}=(B+2)I_\mathrm{B2},\qquad I_\mathrm{C2}=B\,I_\mathrm{B2}=\frac{I_\mathrm{ref}}{1+\frac2B}\approx I_\mathrm{ref}$$

T1 als Diode geschaltet (Basis und Kollektor verbunden), $I_\mathrm{B1}=I_\mathrm{B2}$; gleiche Transistoren, gleiche Temperatur, T2 aktiv. Der Fehler $2/B$ kommt von den beiden Basisströmen. Bei großem $U_\mathrm{CE2}$ liefert T2 etwas mehr.

**Spannungsregler mit Zener-Diode**

$$U_\mathrm{A}=U_\mathrm{Z}-U_\mathrm{BE}$$

Masche über Zener-Diode, BE-Strecke und Last; der Emitter ist der Ausgang. Bedingungen: $U_\mathrm{E}>U_\mathrm{A}+U_\mathrm{CE,sat}$, damit T aktiv bleibt, und $(U_\mathrm{E,min}-U_\mathrm{Z})/R_1>I_\mathrm{B}$ mit dem Minimum $U_\mathrm{E,min}$ der Eingangsspannung $U_\mathrm{E}$ im Brummtal. Die Basis braucht nur den $B$-ten Teil des Laststroms.
::::

::::lernkarten
:::karte begriff Stromspiegel
Wie ist ein Stromspiegel aus zwei gleichen Transistoren aufgebaut, und was leistet er?
---
Eine Schaltung, in der T1 als Diode geschaltet ist (Basis und Kollektor verbunden) und über einen Widerstand $I_\mathrm{ref}$ erhält. T2 liegt an derselben $U_\mathrm{BE}$ und kopiert den Strom in einen anderen Zweig, unabhängig von seiner Last.
--- falsch
Eine Schaltung, in der T1 und T2 in Reihe liegen, sodass derselbe Strom durch beide fließt. T2 spiegelt dabei die Spannung von T1 an der Masse und gibt sie mit umgekehrtem Vorzeichen an die Last aus.
--- falsch
Eine Schaltung, in der T1 den Basisstrom von T2 liefert. T2 verstärkt ihn noch einmal um $B$, sodass der Ausgangsstrom $B^2$-mal so groß ist wie der Strom durch den Widerstand an T1 und sich über diesen Widerstand fein einstellen lässt.
--- falsch
Eine Schaltung, in der T1 als Diode geschaltet ist und die Spannung an der Last misst. T2 regelt danach die Lastspannung auf denselben Wert wie an T1, unabhängig vom Strom.
:::
:::karte zusammenhang Warum der Spiegel kopiert
Warum führt T2 im Stromspiegel denselben Strom wie T1?
---
Nach $I_\mathrm{C}=I_\mathrm{S}\,\mathrm{e}^{U_\mathrm{BE}/U_T}$ legt $U_\mathrm{BE}$ den Strom fest. T1 stellt durch seinen Strom genau die nötige Spannung ein, T2 liegt an derselben; gleiche Transistoren gleicher Temperatur führen dann denselben Strom.
--- falsch
T1 und T2 liegen in Reihe, und durch eine Reihenschaltung fließt überall derselbe Strom. Die Spannung $U_\mathrm{BE}$ spielt dafür keine Rolle, nur die Knotenregel am gemeinsamen Anschluss.
--- falsch
T2 erhält über die verbundenen Basen denselben Basisstrom wie T1 und verstärkt ihn mit demselben $B$. Die Spannung $U_\mathrm{BE}$ ist dabei an beiden verschieden, weil die beiden Lasten verschieden groß sind und andere Ströme ziehen.
--- falsch
Der Widerstand an T1 begrenzt den Strom in beiden Zweigen gleichermaßen, weil beide Kollektoren an derselben Versorgung hängen. Ohne diesen Widerstand wären die Ströme verschieden.
:::
:::karte begriff Referenzstrom
Was ist der Referenzstrom $I_\mathrm{ref}$ in einem Stromspiegel, und wie groß ist er?
---
Der Strom durch den Widerstand $R_\mathrm{ref}$, der T1 speist und den T2 kopiert: $I_\mathrm{ref}=\frac{U_\mathrm{CC}-U_\mathrm{BE}}{R_\mathrm{ref}}$. Von ihm zweigen auch die beiden Basisströme ab.
--- falsch
Der Strom durch die Last von T2, den der Spiegel festhält: $I_\mathrm{ref}=\frac{U_\mathrm{CC}}{R_\mathrm{L}}$. Er hängt nur von der Last ab, nicht von $U_\mathrm{BE}$.
--- falsch
Der Basisstrom von T1, auf den sich beide Transistoren beziehen: $I_\mathrm{ref}=\frac{U_\mathrm{BE}}{R_\mathrm{ref}}$. Er ist $B$-mal kleiner als der Strom in T2.
--- falsch
Der Strom durch den Widerstand $R_\mathrm{ref}$, der nur T1 speist: $I_\mathrm{ref}=\frac{U_\mathrm{CC}+U_\mathrm{BE}}{R_\mathrm{ref}}$. Die beiden Basisströme fließen getrennt aus der Versorgung zu.
:::
:::karte formel Ausgangsstrom des Stromspiegels
Wie groß ist der Strom $I_\mathrm{C2}$ im Stromspiegel, und woher kommt der kleine Fehler gegenüber $I_\mathrm{ref}$?
---
$I_\mathrm{ref}=I_\mathrm{C1}+I_\mathrm{B1}+I_\mathrm{B2}=(B+2)I_\mathrm{B2}$, also $I_\mathrm{C2}=B\,I_\mathrm{B2}=\frac{I_\mathrm{ref}}{1+\frac2B}\approx I_\mathrm{ref}$. Die beiden Basisströme zweigen von $I_\mathrm{ref}$ ab, daher der Fehler $2/B$.
--- falsch
$I_\mathrm{ref}=I_\mathrm{C1}+I_\mathrm{B1}=(B+1)I_\mathrm{B1}$, also $I_\mathrm{C2}=\frac{I_\mathrm{ref}}{1+\frac1B}\approx I_\mathrm{ref}$. Nur der Basisstrom von T1 zweigt ab, daher der Fehler $1/B$.
--- falsch
$I_\mathrm{C2}=B\,I_\mathrm{ref}$, weil T2 den Referenzstrom als Basisstrom erhält und verstärkt. Der Fehler entsteht durch die Streuung von $B$ zwischen beiden Transistoren.
--- falsch
$I_\mathrm{ref}=I_\mathrm{C1}+I_\mathrm{B1}+I_\mathrm{B2}=(B+2)I_\mathrm{B2}$, also $I_\mathrm{C2}=(1+\frac2B)\,I_\mathrm{ref}$. T2 liefert immer etwas mehr als $I_\mathrm{ref}$, weil er die Basisströme mitführt.
:::
:::karte zusammenhang Grenze des Stromspiegels
Bis zu welchem Lastwiderstand arbeitet ein Stromspiegel mit $I_\mathrm{C2}=1{,}98$ mA an 12 V, und warum gibt es diese Grenze?
---
Bis $11{,}8\,\mathrm{V}/1{,}98\,\mathrm{mA}=5{,}96$ k$\Omega$. Bei größerem $R_\mathrm{L}$ bliebe für T2 weniger als $U_\mathrm{CE,sat}$; er wäre gesättigt und könnte den Strom nicht mehr halten.
--- falsch
Bis $12\,\mathrm{V}/1{,}98\,\mathrm{mA}=6{,}06$ k$\Omega$. Bei größerem $R_\mathrm{L}$ würde die Spannung an der Last größer als die Versorgung, was nach der Maschenregel unmöglich ist.
--- falsch
Für jeden Lastwiderstand, weil T2 eine ideale Stromquelle ist. Der Strom bleibt auch bei unendlich großem $R_\mathrm{L}$ genau 1,98 mA.
--- falsch
Bis $0{,}6\,\mathrm{V}/1{,}98\,\mathrm{mA}=0{,}3$ k$\Omega$. Bei größerem $R_\mathrm{L}$ fiele an der Last mehr als $U_\mathrm{BE}$ ab, und T1 würde sperren.
:::
:::karte begriff Brumm
Was bezeichnet man als Brumm an der Gleichspannung eines Gleichrichters mit Glättung?
---
Die Restwelligkeit, die der Gleichspannung nach Gleichrichtung und Glättung bleibt. Im Beispiel schwankt die Eingangsspannung des Reglers dadurch zwischen 10,5 V und 13,5 V.
--- falsch
Das Geräusch, das ein Transformator beim Gleichrichten erzeugt. Es entsteht durch die Kräfte im Eisenkern und hat mit der Spannung am Ausgang nichts zu tun.
--- falsch
Die Spannung, um die eine Diode im Gleichrichter die Ausgangsspannung verkleinert, rund 0,6 V je Diode. Sie bleibt auch bei perfekter Glättung erhalten.
--- falsch
Die Restwelligkeit der Netzspannung vor dem Gleichrichter. Hinter dem Gleichrichter mit Glättung ist sie verschwunden, weil die Glättung jede Schwankung vollständig beseitigt.
:::
:::karte formel Spannungsregler mit Zener-Diode
Welche Ausgangsspannung liefert der Spannungsregler mit Zener-Diode, und welche Bedingungen müssen dafür gelten?
---
$U_\mathrm{A}=U_\mathrm{Z}-U_\mathrm{BE}$ aus der Masche über Zener-Diode, BE-Strecke und Last. Es muss immer $U_\mathrm{E}>U_\mathrm{A}+U_\mathrm{CE,sat}$ gelten, und $R_1$ muss genug Strom liefern: $(U_\mathrm{E,min}-U_\mathrm{Z})/R_1>I_\mathrm{B}$.
--- falsch
$U_\mathrm{A}=U_\mathrm{Z}+U_\mathrm{BE}$ aus der Masche über Zener-Diode, BE-Strecke und Last. Es muss immer $U_\mathrm{E}<U_\mathrm{A}$ gelten, damit der Transistor gesperrt bleibt und die Zener-Diode allein regelt.
--- falsch
$U_\mathrm{A}=U_\mathrm{Z}$, weil die Zener-Diode direkt am Ausgang liegt. Der Transistor liefert nur den Strom und muss dafür in der Sättigung arbeiten: $U_\mathrm{E}=U_\mathrm{A}+U_\mathrm{CE,sat}$.
--- falsch
$U_\mathrm{A}=U_\mathrm{E}-U_\mathrm{Z}$ aus der Masche über $R_1$ und Zener-Diode. Es muss immer $U_\mathrm{E}>2\,U_\mathrm{Z}$ gelten, und der Laststrom muss vollständig durch $R_1$ fließen.
:::
:::karte zusammenhang Nachregeln im Spannungsregler
Was passiert im Spannungsregler, wenn die Last mehr Strom zieht und die Ausgangsspannung zu sinken beginnt?
---
Die Zener-Diode hält die Basis auf $U_\mathrm{Z}$. Sinkt der Emitter, wächst $U_\mathrm{BE}$, und der Transistor liefert mehr Strom nach; über $U_\mathrm{CE}$ fällt der Rest der Eingangsspannung ab.
--- falsch
Die Zener-Diode übernimmt den zusätzlichen Strom und hält so den Ausgang fest. Der Transistor ändert seinen Strom dabei nicht, weil seine Basis auf $U_\mathrm{Z}$ liegt.
--- falsch
Die Basis sinkt mit dem Emitter, $U_\mathrm{BE}$ bleibt gleich, und der Transistor sperrt kurz. Danach lädt $R_1$ den Ausgang wieder auf den alten Wert.
--- falsch
Sinkt der Emitter, sinkt auch $U_\mathrm{BE}$, und der Transistor liefert weniger Strom. Dadurch entlastet er die Versorgung, bis die Last wieder weniger Strom zieht und der Ausgang steigt.
:::
:::karte zusammenhang Kaum belastete Zener-Diode
Warum wird die Zener-Diode im Spannungsregler kaum belastet, auch wenn die Last 50 mA zieht?
---
Der Laststrom fließt über den Kollektor aus der Versorgung, nicht durch $R_1$. Die Basis braucht nur den $B$-ten Teil, bei 50 mA Last also 0,25 mA.
--- falsch
Die Zener-Diode liegt in Reihe mit der Last, trägt also deren Strom. Sie bleibt nur kühl, weil an ihr bei 50 mA kaum Spannung abfällt.
--- falsch
Die Last zieht ihren Strom über $R_1$, und $R_1$ begrenzt den Strom in der Zener-Diode auf 0,25 mA, gleich wie groß die Eingangsspannung und die Last gerade sind.
--- falsch
Der Transistor schaltet die Zener-Diode ab, sobald die Last Strom zieht. Sie arbeitet nur im Leerlauf und gibt dann die Spannung vor.
:::
:::karte zusammenhang Zener-Diode allein
Warum nimmt man für 50 mA Last nicht einfach eine Zener-Diode mit Vorwiderstand ohne Transistor?
---
Der Vorwiderstand müsste bei tiefster Eingangsspannung die ganzen 50 mA liefern; bei Spitzenspannung flösse die Differenz durch die Zener-Diode, und er heizte mit rund 0,7 W. Der Transistor trennt Spannungsvorgabe und Stromlieferung.
--- falsch
Eine Zener-Diode allein liefert nur ihre Durchbruchspannung, wenn kein Strom fließt; schon bei 1 mA bricht die Spannung zusammen. Der Transistor ist deshalb nötig, damit überhaupt eine stabile Spannung am Ausgang entsteht und stehen bleibt.
--- falsch
Eine Zener-Diode allein würde den Brumm verdoppeln, weil sie im Durchbruch wie eine Spannungsquelle mit Innenwiderstand null wirkt. Der Transistor dämpft den Brumm, indem er die Hälfte davon in Wärme umsetzt.
--- falsch
Eine Zener-Diode allein braucht eine negative Versorgung, weil sie in Sperrrichtung betrieben wird. Der Transistor kehrt die Polung um, damit der Regler an einer positiven Eingangsspannung arbeiten kann.
:::
:::karte zusammenhang Wärme im Regler
Wo bleibt im Spannungsregler die überschüssige Eingangsspannung, und was bedeutet das für den Transistor?
---
Sie fällt über $U_\mathrm{CE}$ ab und wird im Transistor zu Wärme. Im Beispiel entstehen bis zu $7{,}9\,\mathrm{V}\cdot50\,\mathrm{mA}=395$ mW, gerade unter $P_\mathrm{max}$.
--- falsch
Sie fällt an der Zener-Diode ab, die sie in Wärme umsetzt. Der Transistor bleibt kalt, weil er in der Sättigung arbeitet und an ihm nur 0,2 V liegen.
--- falsch
Sie wird in die Versorgung zurückgespeist, weil der Transistor wie ein Schalter arbeitet. Im Transistor entsteht deshalb fast keine Wärme.
--- falsch
Sie fällt am Lastwiderstand ab und erhöht dort die Leistung. Der Transistor setzt nur seine Basisleistung $U_\mathrm{BE}I_\mathrm{B}$ in Wärme um.
:::
::::
