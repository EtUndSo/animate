---
title: Stufe 8: Kleine Änderungen um den Arbeitspunkt
pfad: Elektrotechnik / 1. Semester / Grundlagen der Elektrotechnik / Halbleiter und Dioden
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

**Beispiel.** Im Rechenmodell ist $r=25{,}85\,\mathrm{mV}/4{,}31\,\mathrm{mA}=6{,}0\,\Omega$. Zur Quelle kommt ein Sinus mit 100 mV Scheitelwert. Für die Änderungen bilden $R$ und $r$ einen Spannungsteiler:

$$\hat u_\mathrm D=100\,\mathrm{mV}\cdot\frac{6{,}0\,\Omega}{1000\,\mathrm{\Omega}+6{,}0\,\Omega}=0{,}60\,\mathrm{mV},\qquad\hat\imath=\frac{100\,\mathrm{mV}}{1006\,\mathrm{\Omega}}=99{,}4\,\mu\text{A}.$$

Die exakte Rechnung für $U_0=5{,}1$ V ergibt $+0{,}59$ mV und $+99{,}4$ µ A. Am Widerstand erscheint das Signal fast ganz, an der Diode bleibt 0,6 %. **Grenzfälle:** Für $I\to0$ wird $r=U_T/I_\mathrm S=2{,}6\,\mathrm{T\Omega}$, die Diode trennt. Für große $I$ strebt $r$ gegen null, real bleibt der Bahnwiderstand.

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
