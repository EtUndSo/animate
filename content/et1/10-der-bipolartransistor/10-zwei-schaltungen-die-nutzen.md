---
title: Stufe 8: Zwei Schaltungen, die $U_\mathrm{BE}$ nutzen
pfad: Elektrotechnik / 1. Semester / Grundlagen der Elektrotechnik / Der Bipolartransistor
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

**Die Idee: Spannungsregler.** Ein Gleichrichter mit Glättung ([Teil 9](/wissen/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/halbleiter-und-dioden/halbleiter-und-dioden.html)) liefert eine Gleichspannung mit einer Restwelligkeit, dem __Brumm__. Im Regler (Abb. [9](#abb-9), rechts) hält eine Zener-Diode die Basis auf $U_\mathrm{Z}$. Der Emitter ist der Ausgang und liegt eine Diodenspannung tiefer. Sinkt die Ausgangsspannung, weil die Last mehr Strom zieht, wächst $U_\mathrm{BE}$, und der Transistor liefert mehr nach. Über $U_\mathrm{CE}$ fällt der Rest der Eingangsspannung ab. Der Laststrom fließt nicht durch $R_1$, die Basis braucht nur den $B$-ten Teil. Die Zener-Diode wird also kaum belastet.

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
