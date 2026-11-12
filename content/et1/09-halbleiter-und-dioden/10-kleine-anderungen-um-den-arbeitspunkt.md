---
title: Stufe 8: Kleine Änderungen um den Arbeitspunkt
pfad: Elektrotechnik / 1. Semester / ET1 – Grundgebiete der Elektrotechnik 1: Einführung in die Schaltungsanalyse / Halbleiter und Dioden
adresse: elektrotechnik/1-semester/grundlagen-der-elektrotechnik/halbleiter-und-dioden
knoten: Kapitel 9: Halbleiter und Dioden
order: 1191000
summary: Oft reitet ein kleines Signal auf einer Gleichspannung, und nur die Änderung zählt.
tags: differentieller Widerstand, Kleinsignal
lang: de
---

<span class="anker" id="stufe-8"></span>

:::zweck
Oft reitet ein kleines Signal auf einer Gleichspannung, und nur die Änderung zählt. Diese Stufe zeigt: Für kleine Änderungen wirkt die Diode wie ein Widerstand, dessen Wert der Gleichstrom einstellt.
:::

**Die Idee.** Nahe am AP fällt jede glatte Kurve mit ihrer Tangente zusammen (Abb. [10](#abb-10)). Der Mechanismus: 1 mV mehr senkt die Barriere um 1 meV. Der Anteil über der Barriere steigt dadurch um $1/25{,}85=3{,}9$ %, und zwar immer um denselben Prozentsatz des aktuellen Stroms. Großer Strom bedeutet also große absolute Änderung und damit kleinen Widerstand.

:::abbildung et1/k9kleinsignal 10
Links: Ausschnitt der Kennlinie um den AP (0,692 V | 4,31 mA). Die Tangente hat die Steigung $1/r=0{,}167$ S und trifft die Achse bei $U_\mathrm D-U_T=0{,}667$ V. Rechts: Für das kleine Signal ist die Gleichspannungsquelle weg, die Diode ist der Widerstand $r$.
:::

:::satz Satz 8.1 (Differentieller Widerstand)
<span class="anker" id="satz-8-1"></span>

Im AP mit dem Gleichstrom $I$ gilt für kleine Änderungen $u_\mathrm D$ und $i$

<span class="anker" id="gl-8-1"></span>
$$r=\frac{\mathrm{d} U_\mathrm D}{\mathrm{d} I}=\frac{U_T}{I+I_\mathrm S}\approx\frac{U_T}{I},\qquad u_\mathrm D=r\,i. \tag{8.1}$$
:::

⁠**So liest man das:** $r$ heißt __differentieller Widerstand__, bei 1 mA sind es 25,85 $\Omega$. Kleine Buchstaben sind die Abweichungen vom AP, das __Kleinsignal__. **Gültigkeit:** $|u_\mathrm D|\ll U_T$. Bei 1 mV beträgt der Fehler 2 %, bei 5 mV 10 %, bei 25,85 mV schon 72 %.

:::herleitung Steigung der Kennlinie
Ableiten von [(4.1)](warum-der-strom-exponentiell-wachst.html#gl-4-1): $\mathrm{d} I/\mathrm{d} U_\mathrm D=(I_\mathrm S/U_T)\,\mathrm{e}^{U_\mathrm D/U_T}=(I+I_\mathrm S)/U_T$. Der Kehrwert ist $r$. Die Exponentialfunktion reproduziert sich beim Ableiten, darum steht nur $I$ im Ergebnis, und $I_\mathrm S$ fällt im Durchlass heraus. Zwei Dioden mit verschiedenem $I_\mathrm S$ haben beim selben Strom dasselbe $r$.
:::

::::beispiel
Im Rechenmodell ist $r=25{,}85\,\mathrm{mV}/4{,}31\,\mathrm{mA}=6{,}0\,\Omega$. Zur Quelle kommt ein Sinus mit 100 mV Scheitelwert. Für die Änderungen bilden $R$ und $r$ einen Spannungsteiler:

$$\hat u_\mathrm D=100\,\mathrm{mV}\cdot\frac{6{,}0\,\Omega}{1000\,\mathrm{\Omega}+6{,}0\,\Omega}=0{,}60\,\mathrm{mV},\qquad\hat\imath=\frac{100\,\mathrm{mV}}{1006\,\mathrm{\Omega}}=99{,}4\,\mu\text{A}.$$

Die exakte Rechnung für $U_0=5{,}1$ V ergibt $+0{,}59$ mV und $+99{,}4$ µ A. Am Widerstand erscheint das Signal fast ganz, an der Diode bleibt 0,6 %.
::::

⁠**Grenzfälle:** Für $I\to0$ wird $r=U_T/I_\mathrm S=2{,}6\,\mathrm{T\Omega}$, die Diode trennt. Für große $I$ strebt $r$ gegen null, real bleibt der Bahnwiderstand.

:::ltspice Arbeitspunkt und Signal
⁠**Zeichnen:** Quelle `voltage` von `in` nach Masse, Wert `5`, unter `Advanced` bei AC Amplitude `1` eintragen. `res` 1k von `in` nach `d`, `diode` DM von `d` nach Masse, Modell wie oben.

⁠**Direktiven:** zuerst `.op`, dann `.ac dec 1 1k 10k`

⁠**Was du siehst:** Mit `.op` steht $V(d)=0{,}693$ V und $I(D1)=4{,}31$ mA. Mit `.ac` steht bei $V(d)$ der Wert $-44{,}5$ dB, also das Verhältnis 0,00597. Das ist $r/(R+r)$ aus dem Beispiel. Ändere für Aufgabe [10](#aufg-10) die Werte und lies dein $r$ ab.
:::

:::frage Warum ist der Widerstand der Diode nicht $U_\mathrm D/I$?
Das wäre der Kehrwert der Steigung der Linie vom Ursprung zum AP: $0{,}692\,\mathrm{V}/4{,}31\,\mathrm{mA}=161\,\Omega$. Sie beschreibt, welcher Widerstand am AP denselben Strom führen würde, ist aber keine Eigenschaft der Kennlinie an dieser Stelle. Wie stark der Strom auf eine Änderung antwortet, sagt nur die Tangente, und die ist 27-mal steiler. Bei einem ohmschen Widerstand fallen beide zusammen.
:::

:::aufgabe Aufgabe 10 ★★ Steigung und Tangente
<span class="anker" id="aufg-10"></span>

<ol class="al">

<li>

Berechne $r$ bei 2 mA und bei 20 mA.

</li>

<li>

Bei 2 mA steigt die Spannung um 10 mV. Welchen Strom sagt die Tangente voraus, welchen die Kennlinie? Warum liegt die Tangente darunter?

</li>

<li>

Drei gleiche Dioden in Reihe führen 2 mA aus 12 V über einen Widerstand. Berechne die Spannung an den drei Dioden und den Widerstand. Um wie viel ändert sich die Spannung an den Dioden, wenn die Quelle um 1 V steigt?

</li>

</ol>

:::loesung
(a) 12,9 $\Omega$ und 1,29 $\Omega$. (b) Tangente: $2\,\mathrm{mA}+10\,\mathrm{mV}/12{,}9\,\Omega=2{,}77$ mA. Kennlinie: $2\,\mathrm{mA}\cdot\mathrm{e}^{0{,}387}=2{,}94$ mA. Eine Exponentialkurve krümmt sich nach oben und liegt immer über ihrer Tangente. (c) Spannung $3\cdot0{,}673\,\mathrm{V}=2{,}02$ V, $R=(12\,\mathrm{V}-2{,}02\,\mathrm{V})/2\,\mathrm{mA}=5{,}0\,\mathrm{k\Omega}$. Die drei Dioden haben zusammen $r=38{,}8\,\Omega$. Aus 1 V werden $1\,\mathrm{V}\cdot38{,}8/5039=7{,}7$ mV.
:::
:::

::::formelsammlung
**Differentieller Widerstand**

$$r=\frac{\mathrm{d} U_\mathrm D}{\mathrm{d} I}=\frac{U_T}{I+I_\mathrm S}\approx\frac{U_T}{I},\qquad u_\mathrm D=r\,i$$

$I$ Gleichstrom im Arbeitspunkt; $u_\mathrm D$ und $i$ sind die kleinen Abweichungen vom Arbeitspunkt (Kleinsignal). Gilt für $|u_\mathrm D|\ll U_T$. Für $I\to0$ wird $r=U_T/I_\mathrm S$, für große $I$ strebt $r$ gegen null, real bleibt der Bahnwiderstand. Nicht verwechseln mit $U_\mathrm D/I$.

**Signalanteil an der Diode**

$$r/(R+r)$$

Für kleine Änderungen ist die Gleichspannungsquelle weg und die Diode der Widerstand $r$; mit dem Widerstand $R$ in Reihe bildet sie einen Spannungsteiler.
::::

::::lernkarten
:::karte begriff differentieller Widerstand
Was gibt der differentielle Widerstand $r$ einer Diode im Arbeitspunkt an?
---
Den Kehrwert der Steigung der Kennlinie im Arbeitspunkt, $r=\frac{\mathrm{d} U_\mathrm D}{\mathrm{d} I}$. Er verknüpft kleine Änderungen von Spannung und Strom, $u_\mathrm D=r\,i$; bei 1 mA sind es 25,85 $\Omega$.
--- falsch
Den Quotienten aus Spannung und Strom im Arbeitspunkt, $U_\mathrm D/I$. Er gibt an, welcher Widerstand denselben Strom führen würde; bei 1 mA sind es rund 650 $\Omega$.
--- falsch
Den Widerstand der neutralen Gebiete der Diode, wenige $\Omega$. Er bleibt bei jedem Strom gleich und verknüpft kleine Änderungen von Spannung und Strom, $u_\mathrm D=r\,i$.
--- falsch
Den Kehrwert der Steigung der Arbeitsgerade, also den Widerstand $R$. Er gibt an, wie stark sich der Strom ändert, wenn sich die Quellenspannung ein wenig ändert.
:::
:::karte formel Differentieller Widerstand
Wie berechnet man den differentiellen Widerstand einer Diode aus dem Gleichstrom $I$ im Arbeitspunkt, und wann gilt $u_\mathrm D=r\,i$?
---
$r=\frac{U_T}{I+I_\mathrm S}\approx\frac{U_T}{I}$, bei 1 mA also 25,85 $\Omega$. Die Beziehung gilt für $|u_\mathrm D|\ll U_T$; bei 5 mV beträgt der Fehler schon 10 %.
--- falsch
$r=\frac{U_T}{I}$, und die Beziehung gilt für jede Signalgröße, solange die Diode leitet, weil die Kennlinie im Durchlass eine Gerade ist.
--- falsch
$r=\frac{I}{U_T}$, bei 1 mA also 0,039 $\Omega$. Die Beziehung gilt für $|u_\mathrm D|\ll U_T$; bei 5 mV beträgt der Fehler schon 10 %.
--- falsch
$r=\frac{U_T}{I_\mathrm S}$, unabhängig vom Arbeitspunkt, bei der Diode mit $I_\mathrm S=10^{-14}$ A also 2,6 T$\Omega$. Die Beziehung gilt für $|u_\mathrm D|\ll U_T$.
:::
:::karte herleitung Steigung der Kennlinie
Wie folgt aus der Shockley-Gleichung der differentielle Widerstand $r=\frac{U_T}{I+I_\mathrm S}$?
---
Ableiten nach der Spannung ergibt $\mathrm{d} I/\mathrm{d} U_\mathrm D=(I_\mathrm S/U_T)\,\mathrm{e}^{U_\mathrm D/U_T}$, weil der Summand $-1$ beim Ableiten wegfällt.
---
Daraus wird $\mathrm{d} I/\mathrm{d} U_\mathrm D=(I+I_\mathrm S)/U_T$, weil nach der Shockley-Gleichung $I_\mathrm S$ mal der Exponentialfunktion gleich $I+I_\mathrm S$ ist; die Exponentialfunktion reproduziert sich beim Ableiten.
---
Der Kehrwert ist $r=\frac{\mathrm{d} U_\mathrm D}{\mathrm{d} I}=\frac{U_T}{I+I_\mathrm S}$, weil $r$ die Spannungsänderung je Stromänderung angibt.
---
Im Durchlass gilt $r=U_T/I$, weil $I_\mathrm S$ neben dem Strom herausfällt; zwei Dioden mit verschiedenem $I_\mathrm S$ haben beim selben Strom dasselbe $r$.
:::
:::karte zusammenhang Großer Strom, kleiner Widerstand
Warum hat eine Diode bei großem Gleichstrom einen kleinen differentiellen Widerstand?
---
1 mV mehr senkt die Barriere um 1 meV, und der Strom steigt um $1/25{,}85=3{,}9$ %, immer derselbe Prozentsatz des aktuellen Stroms. Großer Strom heißt große absolute Änderung, also kleiner Widerstand.
--- falsch
Bei großem Strom erwärmt sich die Diode, und ihr Material leitet besser. Der Widerstand sinkt deshalb mit der Temperatur der Diode, nicht mit dem Strom selbst, und kehrt beim Abkühlen zurück.
--- falsch
Bei großem Strom ist die Barriere ganz verschwunden, und die Diode verhält sich wie ein Stück Draht. Ihr Widerstand ist dann nur noch der Bahnwiderstand der neutralen Gebiete.
--- falsch
1 mV mehr erhöht den Strom immer um denselben Betrag von 3,9 µ A, gleich wie groß er ist. Bei großem Strom ist diese feste Änderung relativ klein, und deshalb sinkt der Widerstand.
:::
:::karte begriff Kleinsignal
Was bezeichnet man bei einer Diode im Arbeitspunkt als Kleinsignal, und wie schreibt man es?
---
Die kleinen Abweichungen von Spannung und Strom um den Arbeitspunkt. Man schreibt sie mit kleinen Buchstaben, $u_\mathrm D$ und $i$, und für sie gilt $u_\mathrm D=r\,i$.
--- falsch
Den Gleichstrom im Arbeitspunkt, wenn er kleiner als 1 mA ist. Man schreibt ihn mit kleinem Buchstaben $i$, und für ihn gilt $U_\mathrm D=r\,i$ mit dem Widerstand $r$.
--- falsch
Die Abweichungen von Spannung und Strom um den Arbeitspunkt, die größer als $U_T$ sind. Erst sie verschieben den Arbeitspunkt merklich und werden deshalb eigens bezeichnet.
--- falsch
Die Spannung an der Diode, solange sie unter 0,6 V liegt und kaum Strom fließt. Man schreibt sie mit kleinem Buchstaben, weil der Strom in diesem Bereich klein ist.
:::
:::karte zusammenhang Kleines Signal am Widerstand
Warum erscheint ein kleines Signal, das zur Quelle einer Diodenschaltung hinzukommt, fast ganz am Widerstand $R$ und kaum an der Diode?
---
Für die Änderungen ist die Gleichspannungsquelle weg, und die Diode ist der Widerstand $r$. $R$ und $r$ bilden einen Spannungsteiler; mit 6,0 $\Omega$ neben 1 k$\Omega$ bleiben an der Diode nur 0,6 %.
--- falsch
Die Diode hat für Änderungen denselben Widerstand wie für den Gleichstrom, $U_\mathrm D/I=161\,\Omega$. Neben 1 k$\Omega$ ist das wenig, und deshalb bleiben an ihr rund 14 % des Signals.
--- falsch
Das Signal ist kleiner als die Durchlassspannung und kann die Diode deshalb nicht durchdringen. Es staut sich am Widerstand und erscheint dort in voller Größe, an der Diode gar nicht.
--- falsch
$R$ und $r$ bilden für die Änderungen einen Spannungsteiler, aber $r$ ist viel größer als $R$, weil die Kennlinie im Arbeitspunkt flach ist. Deshalb liegt das Signal fast ganz am Widerstand.
:::
:::karte zusammenhang Steigung statt Quotient
Warum ist der Widerstand der Diode für kleine Änderungen nicht der Quotient $U_\mathrm D/I$?
---
$U_\mathrm D/I$ ist der Kehrwert der Steigung der Linie vom Ursprung zum Arbeitspunkt, im Beispiel 161 $\Omega$. Wie stark der Strom auf eine Änderung antwortet, sagt nur die Tangente, und die ist 27-mal steiler.
--- falsch
$U_\mathrm D/I$ wäre richtig, wenn man vorher die Durchlassspannung abzieht: Der Quotient aus $U_\mathrm D-U_\mathrm F$ und $I$ ist der Widerstand für kleine Änderungen, im Beispiel also nahe null, weil $U_\mathrm D$ dort fast gleich $U_\mathrm F$ ist.
--- falsch
$U_\mathrm D/I$ und $r$ sind bei der Diode gleich, nur misst man $r$ mit Wechselstrom. Die Unterschiede, die man in der Anzeige sieht, kommen allein vom Messgerät.
--- falsch
$U_\mathrm D/I$ ist die Steigung der Tangente. Sie ist bei der Diode 27-mal flacher als die Linie vom Ursprung, und deshalb ist $r$ größer als $U_\mathrm D/I$.
:::
:::karte zusammenhang Tangente unter der Kennlinie
Warum sagt die Tangente im Arbeitspunkt bei 10 mV mehr Spannung einen kleineren Strom voraus, als die Kennlinie liefert?
---
Eine Exponentialkurve krümmt sich nach oben und liegt immer über ihrer Tangente. Bei 2 mA sagt die Tangente 2,77 mA voraus, die Kennlinie liefert 2,94 mA.
--- falsch
Die Tangente berücksichtigt den Sperrstrom nicht, die Kennlinie schon; der Unterschied von 0,17 mA ist genau dieser Sperrstrom.
--- falsch
Die Tangente gilt nur für fallende Spannung; für steigende Spannung muss man ihre Steigung verdoppeln, sonst unterschätzt sie den Strom systematisch.
--- falsch
Eine Exponentialkurve krümmt sich nach unten und liegt unter ihrer Tangente; dass die Kennlinie hier mehr liefert, liegt allein am Bahnwiderstand.
:::
:::karte zusammenhang Grenzfälle des differentiellen Widerstands
Was passiert mit dem differentiellen Widerstand einer Diode für $I\to0$ und für sehr große Ströme?
---
Für $I\to0$ wird $r=U_T/I_\mathrm S=2{,}6\,\mathrm{T\Omega}$, die Diode trennt. Für große $I$ strebt $r$ gegen null, real bleibt der Bahnwiderstand.
--- falsch
Für $I\to0$ wird $r$ null, weil kein Strom auch keine Spannung braucht. Für große $I$ wächst $r$ unbegrenzt, weil die Barriere dann ganz verschwindet.
--- falsch
Für $I\to0$ und für große $I$ bleibt $r$ gleich $U_T$ geteilt durch 1 A, weil der Widerstand nur von der Temperatur abhängt und nicht vom Strom.
--- falsch
Für $I\to0$ wird $r$ sehr klein, weil $I_\mathrm S$ winzig ist und kaum Spannung braucht. Für große $I$ strebt $r$ gegen einige k$\Omega$, den Bahnwiderstand.
:::
::::
