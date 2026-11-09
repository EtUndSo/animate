---
title: Stufe 6: Der Arbeitspunkt
pfad: Elektrotechnik / 1. Semester / Grundlagen der Elektrotechnik / Halbleiter und Dioden
order: 1190800
summary: Bei einem Widerstand liefert U=R\,I sofort das Ergebnis.
tags: Arbeitsgerade, Arbeitspunkt, Arbeitspunktanalyse, Arbeitspunktsynthese, Leerlauf, Kurzschluss, Hysterese, Iteration
lang: de
---

<span class="anker" id="stufe-6"></span>

:::zweck
Bei einem Widerstand liefert $U=R\,I$ sofort das Ergebnis. Die Diode folgt einer anderen Kurve. Diese Stufe findet Spannung und Strom der Diode in einer Schaltung.
:::

**Die Idee.** Zwei Bedingungen müssen zugleich gelten. Die Diode lässt nur Punkte auf ihrer Kennlinie zu. Der Rest der Schaltung, Quelle und Widerstand, lässt nur Punkte auf der __Arbeitsgerade__ zu ([Teil 5](/wissen/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/quellen-und-ersatzquellen/quellen-und-ersatzquellen.html)). Die Schaltung findet den Schnittpunkt selbst: Ist $U_\mathrm D$ zu klein, liefert der Widerstand mehr Strom, als die Diode durchlässt. Ladung staut sich am Knoten zwischen beiden und hebt sein Potenzial, bis beide Ströme gleich sind.

:::abbildung et1/k9arbeitsgerade 8
Schaltung des Rechenmodells und grafische Lösung. Rot die Arbeitsgerade durch Leerlauf und Kurzschluss. Blau die Kennlinie der Diode, Schnittpunkt bei 0,69 V und 4,31 mA. Grün die Kennlinie eines Widerstands von 250 $\Omega$ anstelle der Diode, Schnittpunkt bei 1 V und 4 mA.
:::

:::definition Definition 6.1 (Arbeitspunkt)
<span class="anker" id="satz-6-1"></span>

Der __Arbeitspunkt__ (AP) ist der Punkt auf der Kennlinie, den Strom durch das Bauteil und Spannung über dem Bauteil festlegen. __Arbeitspunktanalyse__ heißt, ihn aus der gegebenen Schaltung zu ermitteln. __Arbeitspunktsynthese__ heißt, die Bauteile so zu wählen, dass ein gewünschter AP entsteht.
:::

**Der lineare Fall.** Ersetzt man die Diode durch einen Widerstand $R_1$, gelten Bauteilgleichung, Maschenregel und daraus die Arbeitsgerade:

<span class="anker" id="gl-6-1"></span>
$$I=\frac{U_{R1}}{R_1},\qquad U_0=U_R+U_{R1}=R\,I+U_{R1},\qquad I=\frac{U_0-U_{R1}}{R}. \tag{6.1}$$

Zwei lineare Gleichungen lassen sich auflösen, mit $R_1=250\,\Omega$ folgt $I=U_0/(R+R_1)=4$ mA und $U_{R1}=1$ V. Das Gleichungssystem zu lösen heißt, beide Geraden zu schneiden.

:::satz Satz 6.2 (Arbeitspunkt der Diode)
<span class="anker" id="satz-6-2"></span>

Für die Reihenschaltung gelten zugleich

<span class="anker" id="gl-6-2"></span>
$$I=\frac{U_0-U_\mathrm D}{R}\qquad\text{und}\qquad I=I_\mathrm S\bigl(\mathrm{e}^{U_\mathrm D/U_T}-1\bigr). \tag{6.2}$$

Die Kennlinie steigt überall, die Gerade fällt überall, also gibt es genau einen Schnittpunkt.
:::

⁠**So liest man das:** $U_\mathrm D$ ist die Spannung $U$ aus [(4.1)](warum-der-strom-exponentiell-wachst.html#gl-4-1). Die Arbeitsgerade zeichnet man durch zwei Punkte, ohne die Diode zu beachten: __Leerlauf__ ($I=0$, $U_\mathrm D=U_0$) und __Kurzschluss__ ($U_\mathrm D=0$, $I=U_0/R$). Die Kennlinie kommt aus der Gleichung oder einem Datenblatt. **Gültigkeit:** Bauteile, deren Kennlinie zurückläuft oder deren Zustand von der Vorgeschichte abhängt (__Hysterese__), können mehrere Schnittpunkte haben. Mehrere nichtlineare Bauteile löst man numerisch oder mit Ersatzschaltungen (Stufe [7](lineare-ersatzschaltungen.html#stufe-7)).

[(6.2)](#gl-6-2) lässt sich nicht nach $U_\mathrm D$ auflösen, weil $U_\mathrm D$ im Exponenten und außerhalb steht. Man löst grafisch oder durch __Iteration__, also durch wiederholtes Einsetzen: Schätze $U_\mathrm D$, berechne $I=(U_0-U_\mathrm D)/R$, dann $U_\mathrm D=U_T\ln(I/I_\mathrm S+1)$, und wiederhole.

::::beispiel
Start mit $U_\mathrm D=0{,}7$ V. Schritt 1: $I=4{,}300$ mA, $U_\mathrm D=0{,}69245$ V. Schritt 2: $I=4{,}3076$ mA, $U_\mathrm D=0{,}69249$ V. Damit ist der AP (0,692 V | 4,31 mA), am Widerstand liegen 4,31 V. Verdoppelt man $U_0$ auf 10 V, verdoppelt sich der Strom fast, auf 9,29 mA, und $U_\mathrm D$ steigt nur um 20 mV auf 0,712 V.
::::

⁠**Grenzfälle:** Bei $U_0=0{,}5$ V ist $I=2{,}3$ µ A, fast die ganze Quellenspannung bleibt an der Diode. Bei negativem $U_0$ ist $I=-I_\mathrm S$, die Quelle liegt ganz an der Diode.

:::frage Warum rechnet man nicht umgekehrt: $U_\mathrm D$ schätzen, $I$ aus der Exponentialfunktion, dann $U_\mathrm D=U_0-R\,I$?
Weil dieser Weg auseinanderläuft. Ein Fehler von 1 mV ändert den Diodenstrom um 3,9 %, also 0,17 mA, und das ergibt am Widerstand 167 mV Fehler. Im ersten Verfahren schrumpft der Fehler je Schritt um denselben Faktor, $r/R=0{,}006$ (Stufe [8](kleine-anderungen-um-den-arbeitspunkt.html#stufe-8)). Die flache Logarithmusfunktion dämpft, die steile Exponentialfunktion verstärkt.
:::

:::aufgabe Aufgabe 7 ★★ Arbeitspunkt finden und einstellen
<span class="anker" id="aufg-7"></span>

Die Diode des Rechenmodells liegt in Reihe mit $R=470\,\Omega$ an $U_0=3$ V.

<ol class="al">

<li>

Bestimme Leerlauf und Kurzschluss der Arbeitsgerade.

</li>

<li>

Iteriere von 0,7 V aus, bis sich drei Stellen nicht mehr ändern.

</li>

<li>

Arbeitspunktsynthese: Welches $R$ ergibt an $U_0=5$ V den Strom 2 mA? Welcher Strom fließt mit dem Normwert 2,2 k$\Omega$?

</li>

<li>

Die Diode wird umgedreht. Was misst man an Diode und Widerstand?

</li>

</ol>

:::loesung
(a) Leerlauf $U_\mathrm D=3$ V, Kurzschluss $I=3\,\mathrm{V}/470\,\Omega=6{,}38$ mA. (b) $U_\mathrm D=0{,}7$ V ergibt $I=4{,}894$ mA, das ergibt $U_\mathrm D=0{,}6958$ V, dann $I=4{,}903$ mA und wieder $U_\mathrm D=0{,}6958$ V. AP: (0,696 V | 4,90 mA). (c) Bei 2 mA ist $U_\mathrm D=0{,}673$ V, also $R=(5\,\mathrm{V}-0{,}673\,\mathrm{V})/2\,\mathrm{mA}=2{,}16\,\mathrm{k\Omega}$. Mit 2,2 k$\Omega$ fließen 1,97 mA. (d) Die Diode sperrt: $I=-10^{-14}$ A, am Widerstand 4,7 pV, an der Diode $-3$ V.
:::
:::
