---
title: Stufe 5: Kennlinie, Durchbruch und Spezialdioden
pfad: Elektrotechnik / 1. Semester / Grundlagen der Elektrotechnik / Halbleiter und Dioden
order: 1190700
summary: Die Gleichung steht.
tags: Anode, Kathode, Lawineneffekt, Zener-Effekt, Durchbruch, Sperrschichtkapazität, Photonen, innerer Photoeffekt
lang: de
---

<span class="anker" id="stufe-5"></span>

:::zweck
Die Gleichung steht. Diese Stufe liest sie als Kurve, ergänzt den Durchbruch und zeigt, was man aus den Eigenschaften des Übergangs sonst noch baut.
:::

**Die Idee.** Die p-Seite heißt __Anode__, die n-Seite __Kathode__, beide tragen Metallkontakte. Das Dreieck des Schaltzeichens zeigt in Durchlassrichtung. In linearer Darstellung sieht man scheinbar einen Knick bei 0,6 V (Abb. [6](#abb-6)). Er liegt am Maßstab, denn eine Exponentialfunktion hat keine Schwelle. Auf einer Achse bis 10 mA erreicht die Kurve 1 % des Endwerts bei 0,595 V, auf einer Achse bis 10 µ A schon bei 0,417 V. Logarithmisch ist sie eine Gerade.

:::abbildung et1/k9kennlinie 6
Aufbau, Schaltzeichen mit Zählpfeilen und Kennlinie des Rechenmodells. Mitte: linear, der Sperrstrom $10^{-14}$ A ist unsichtbar. Rechts: logarithmisch eine Gerade, nur nahe $U=0$ biegt sie wegen des Summanden $-1$ ab.
:::

**Durchbruch.** Bei großer Sperrspannung wird das Feld in der Zone so stark, dass Träger durch Stöße neue Paare freisetzen (__Lawineneffekt__) oder Elektronen direkt aus dem VB ins LB gelangen (__Zener-Effekt__). Der Sperrstrom steigt steil an, das ist der __Durchbruch__. Er selbst schadet nicht. Zerstört wird eine Diode erst durch die Wärme $P=U\,I$, wenn nichts den Strom begrenzt.

**Zener-Diode.** Sie ist für den Betrieb im Durchbruch gebaut und hat eine genau festgelegte Spannung $U_\mathrm Z$ (Abb. [7](#abb-7) links). Im Durchlass verhält sie sich wie eine pn-Diode. Oberhalb von $U_\mathrm Z$ ist die Kennlinie fast senkrecht, ihr kleiner Widerstand ist $r_\mathrm Z=\Delta U/\Delta I$. Ein Vorwiderstand nimmt Schwankungen der Quelle auf: Die Spannung am Bauteil ändert sich kaum, der Strom ändert sich. Mit $r_\mathrm Z=10\,\Omega$ bewirken 18 mA Stromänderung nur 0,18 V.

**Kapazitätsdiode.** Die trägerfreie Zone ist eine isolierende Schicht zwischen zwei leitenden Gebieten, also ein Kondensator ([Teil 3](/wissen/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/der-kondensator/der-kondensator.html)) mit der Fläche $A$ und dem Abstand $w$. Die __Sperrschichtkapazität__ sinkt mit der Sperrspannung $U_\mathrm R=-U$, weil die Zone wächst:

<span class="anker" id="gl-5-1"></span>
$$C_\mathrm{Sp}=\frac{\varepsilon A}{w}=\frac{C_0}{\sqrt{1+U_\mathrm R/U_\mathrm{D0}}}. \tag{5.1}$$

Mit $A=1\,\mathrm{mm^2}$ ist $C_0=241$ pF, bei 25 V sind es 40 pF und $w=2{,}6$ µ m. **Gültigkeit:** scharfer Übergang, Betrieb in Sperrrichtung. Dioden mit besonders starkem Effekt heißen Kapazitätsdioden. Mit ihnen verstellt man per Spannung die Frequenz von Schwingkreisen, etwa in Funkempfängern. Ein Schwingkreis aus Spule und Kondensator schwingt mit einer Frequenz, die von $C$ abhängt.

:::abbildung et1/k9spezial 7
Links: Zener-Diode mit $U_\mathrm Z=5{,}1$ V und $r_\mathrm Z=10\,\Omega$. Mitte: Kapazität nach [(5.1)](#gl-5-1). Rechts: Solarzelle mit $I_\mathrm S=1$ nA für drei Beleuchtungen. Der Strom folgt dem Licht, die Leerlaufspannung kaum. Unten: Schaltzeichen und Ersatzschaltbild der Photodiode.
:::

**Photodiode.** Licht besteht aus Energiepaketen, den __Photonen__, mit $W=h\,c/\lambda$ ($h$: Planck-Konstante, $c$: Lichtgeschwindigkeit, $\lambda$: Wellenlänge). Ist $W\ge W_\mathrm g$, hebt ein Photon ein Elektron ins LB (__innerer Photoeffekt__). Bei Silizium verlangt das $\lambda\le1107$ nm. Das Feld der Zone trennt das Paar: Das Elektron läuft zur n-Seite, das Loch zur p-Seite. Das ist ein Strom von Kathode nach Anode durch die Diode, also in Sperrrichtung, und er ist der Lichtleistung proportional.

:::satz Satz 5.1 (Beleuchtete Diode)
<span class="anker" id="satz-5-1"></span>

Die Kennlinie verschiebt sich um den __Photostrom__ $I_\mathrm{Ph}$ nach unten. Das Ersatzschaltbild ist eine Stromquelle parallel zur Diode:

<span class="anker" id="gl-5-2"></span>
$$I=I_\mathrm S\bigl(\mathrm{e}^{U/U_T}-1\bigr)-I_\mathrm{Ph},\qquad\text{Leerlauf }(I=0):\ U_\mathrm L=U_T\ln\Bigl(\frac{I_\mathrm{Ph}}{I_\mathrm S}+1\Bigr). \tag{5.2}$$
:::

⁠**So liest man das:** Als Lichtsensor betreibt man die Photodiode in Sperrrichtung, dann ist $I\approx-I_\mathrm{Ph}$. Eine __Solarzelle__ ist eine großflächige Photodiode, die bei $U>0$ und $I<0$ arbeitet: Das Produkt $U\,I$ ist negativ, sie gibt Leistung ab. Zehnfaches Licht hebt $I_\mathrm{Ph}$ auf das Zehnfache, aber $U_\mathrm L$ nur um 60 mV. Der Grund ist der Logarithmus in [(5.2)](#gl-5-2). Die Spannung hängt vor allem vom Material ab, bei Silizium im Betrieb rund 0,5 V. Im Modell mit $I_\mathrm S=1$ nA ist $U_\mathrm L=0{,}505$ V, 0,536 V und 0,564 V bei 0,3 A, 1 A und 3 A. **Grenzfall:** $I_\mathrm{Ph}=0$ ergibt [(4.1)](warum-der-strom-exponentiell-wachst.html#gl-4-1) und $U_\mathrm L=0$.

:::frage Die Diode leitet doch erst ab 0,6 V. Ist das nicht eine Schwelle?
In einer Schaltung mit Strömen um 1 mA wirkt es so: Bei 0,4 V fließen nur 52 nA, kaum messbar. Der Strom wächst aber von 0 V an gleichmäßig, je 60 mV um den Faktor 10. Es gibt keine Spannung, an der etwas umschaltet. Nur der Betrag wird irgendwann für die Schaltung wichtig.
:::

:::aufgabe Aufgabe 5 ★★ Spannung festhalten
<span class="anker" id="aufg-5"></span>

Eine Zener-Diode mit $U_\mathrm Z=5{,}1$ V und $r_\mathrm Z=10\,\Omega$ liegt über $R=220\,\Omega$ an einer Quelle, die zwischen 10 V und 14 V schwankt.

<ol class="al">

<li>

Wie groß ist der Strom an beiden Enden, wenn die Diode genau 5,1 V hält?

</li>

<li>

Um wie viel ändert sich die Diodenspannung wirklich? Um welchen Faktor ist die Schwankung kleiner geworden?

</li>

<li>

Welche Leistung setzt die Diode bei 14 V um?

</li>

</ol>

:::loesung
(a) $I=(10\,\mathrm{V}-5{,}1\,\mathrm{V})/220\,\Omega=22{,}3$ mA und $(14\,\mathrm{V}-5{,}1\,\mathrm{V})/220\,\Omega=40{,}5$ mA. (b) $\Delta U=r_\mathrm Z\Delta I=10\,\Omega\cdot18{,}2\,\mathrm{mA}=0{,}18$ V. Genauer teilt $R$ mit $r_\mathrm Z$: $4\,\mathrm{V}\cdot10/230=0{,}17$ V. Die Schwankung ist 23-mal kleiner. (c) $P=5{,}1\,\mathrm{V}\cdot40{,}5\,\mathrm{mA}=0{,}21$ W.
:::
:::

:::aufgabe Aufgabe 6 ★★ Solarzelle
<span class="anker" id="aufg-6"></span>

Eine Zelle hat $I_\mathrm S=1$ nA und bei voller Sonne $I_\mathrm{Ph}=3$ A.

<ol class="al">

<li>

Berechne $U_\mathrm L$. Wie ändert sich $U_\mathrm L$, wenn das Licht auf ein Drittel sinkt?

</li>

<li>

Berechne $I$ und die abgegebene Leistung bei $U=0{,}5$ V.

</li>

<li>

Wie viele Zellen braucht man in Reihe, um bei je 0,5 V eine Batterie mit 14 V zu laden?

</li>

</ol>

:::loesung
(a) $U_\mathrm L=25{,}85\,\mathrm{mV}\cdot\ln(3\cdot10^{9}+1)=0{,}564$ V. Bei 1 A ist $U_\mathrm L=0{,}536$ V, also nur 28 mV weniger. (b) $I=10^{-9}\,\mathrm{A}\cdot(\mathrm{e}^{19{,}34}-1)-3\,\mathrm{A}=0{,}25\,\mathrm{A}-3\,\mathrm{A}=-2{,}75$ A. Abgegeben werden $0{,}5\,\mathrm{V}\cdot2{,}75\,\mathrm{A}=1{,}37$ W. (c) $14\,\mathrm{V}/0{,}5\,\mathrm{V}=28$ Zellen.
:::
:::
