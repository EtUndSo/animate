---
title: Stufe 9: Gleichrichter und Ladungspumpe
pfad: Elektrotechnik / 1. Semester / Grundlagen der Elektrotechnik / Halbleiter und Dioden
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
Noch nicht. Ein Kondensator parallel zur Last (__Glättung__) lädt sich auf den Scheitel und speist die Last in der Lücke. In 10 ms verliert er $\Delta U=I\,\Delta t/C$ ([Teil 3](/wissen/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/der-kondensator/der-kondensator.html)). Mit $I=10{,}6$ mA und $C=470$ µ F sind das 0,23 V. Die Dioden leiten dann nur noch kurz am Scheitel.
:::

**Ladungspumpe.** Sie erzeugt aus einer Gleichspannung $U_\mathrm e$ eine höhere, ohne Spule. Die Dioden gelten hier als ideal (Abb. [12](#abb-12)). *Schritt 1:* Der Umschalter legt die untere Platte von $C_1$ an Masse. $C_1$ lädt sich über D$_1$ auf $U_\mathrm e$. *Schritt 2:* Der Umschalter legt die untere Platte an $U_\mathrm e$. Die Spannung an $C_1$ kann nicht springen ([Teil 3](/wissen/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/der-kondensator/der-kondensator.html)), also springt die obere Platte auf $2U_\mathrm e$. D$_1$ sperrt, weil ihre Kathode nun höher liegt, D$_2$ leitet, und $C_1$ gibt Ladung an den Ausgangskondensator $C_2$ ab. Nach wenigen Takten ist $U_\mathrm a\approx2U_\mathrm e$. In der Praxis begrenzen kleine Widerstände die Stromspitzen. Mit weiteren Pumpstufen nach demselben Schema steigt die Spannung weiter.

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
