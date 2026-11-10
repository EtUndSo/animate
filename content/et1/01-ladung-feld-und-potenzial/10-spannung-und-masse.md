---
title: Stufe 8: Spannung und Masse
pfad: Elektrotechnik / 1. Semester / ET1 – Grundgebiete der Elektrotechnik 1: Einführung in die Schaltungsanalyse / Ladung, Feld und Potenzial
adresse: elektrotechnik/1-semester/grundlagen-der-elektrotechnik/ladung-feld-und-potenzial
knoten: Kapitel 1: Ladung, Feld und Potenzial
order: 1111000
summary: Der Wert eines Potenzials hängt vom Bezugspunkt ab, die Differenz zweier Potenziale nicht.
tags: Spannung, Masse, Erde, Schaltplänen, Zählpfeil, Knoten
lang: de
---

<span class="anker" id="stufe-8"></span>

:::zweck
Der Wert eines Potenzials hängt vom Bezugspunkt ab, die Differenz zweier Potenziale nicht. Diese Differenz ist die technisch wichtige Größe. Diese Stufe zeigt, wie man mit ihr in einer Schaltung rechnet.
:::

**Die Idee.** Auf eine Ladung wirkt nur dann eine Kraft, wenn sich das Potenzial mit dem Ort ändert. Ein überall gleich hohes Potenzial bewirkt nichts, egal wie hoch es ist. Wirksam sind deshalb nur Differenzen, und jedes Spannungsmessgerät hat zwei Anschlüsse. Der Nullpunkt ist frei wählbar: Erklärt man einen Punkt einer Schaltung zum Nullpunkt, bekommt jeder andere Punkt eine Zahl. Verschiebt man den Nullpunkt, verschieben sich alle Zahlen gemeinsam, ihre Differenzen bleiben.

:::definition Definition 8.1 (Elektrische Spannung und Masse)
<span class="anker" id="satz-8-1"></span>

Die __Spannung__ zwischen $P_1$ und $P_2$ ist

<span class="anker" id="gl-8-1"></span>
$$U_{12}=\varphi(P_1)-\varphi(P_2)=\int_{P_1}^{P_2}\vec E\cdot\mathrm{d}\vec s=\frac{W_{12}}{Q}, \tag{8.1}$$

mit der Einheit $[U]=[W]\cdot[Q]^{-1}=\mathrm{N\,m\,A^{-1}\,s^{-1}}=\mathrm{kg\,m^2\,A^{-1}\,s^{-3}}=\mathrm V$. Der Punkt einer Schaltung, dem man $\varphi:=0$ V zuordnet, heißt __Masse__ oder Bezugspotenzial, englisch GND (ground). Ist er mit dem Erdboden verbunden, spricht man von __Erde__. Von dort aus gilt

<span class="anker" id="gl-8-2"></span>
$$\varphi_1=\varphi_2+U_{12}. \tag{8.2}$$
:::

:::satz Satz 8.2 (Homogenes Feld, Freiheit des Bezugspunkts)
<span class="anker" id="satz-8-2"></span>

Zwischen zwei parallelen Platten im Abstand $d$ mit der Spannung $U$ ist $E=U/d$. Verschiebt man den Bezugspunkt, ändern sich alle Potenziale um dieselbe Konstante $c$, alle Spannungen bleiben gleich:

<span class="anker" id="gl-8-3"></span>
$$E=\frac{U}{d},\qquad\varphi'(P)=\varphi(P)+c\quad\Longrightarrow\quad\varphi'_1-\varphi'_2=U_{12}. \tag{8.3}$$
:::

⁠**So liest man das:** $U_{12}$ heißt „Spannung von 1 nach 2“, die Reihenfolge zählt: $U_{21}=-U_{12}$. In __Schaltplänen__, den Zeichnungen einer Schaltung, steht dafür ein __Zählpfeil__ von Punkt 1 nach Punkt 2 (Abb. [9](#abb-9)). Er legt das Vorzeichen fest: Ist $U_{12}>0$, liegt Punkt 1 höher. Eine positive Ladung gewinnt dann beim Lauf längs des Pfeils Bewegungsenergie, ein Elektron verliert sie. Die Feldstärke sagt, wie viel Spannung je Meter Weg abfällt. Potenziale dürfen negativ sein, das heißt: tiefer als die Masse.

Typische Spannungen: Messgrenze moderner Spannungsmesser 0,1 nV, Fernsehantenne 12 µ V bis 10 mV, zwischen Hand und Herz 1 mV, Autobatterie 12 V, Lichtnetz 230 V, Hochspannungsleitung 120 bis 800 kV, Van-de-Graaff-Generator (Bandgenerator für hohe Spannungen) 10 MV, Blitz bis 100 MV.

⁠**Gültigkeit:** Das Integral in [(8.1)](#gl-8-1) hängt nur im elektrostatischen Feld nicht vom Weg ab. Ein Draht im Schaltplan gilt als ideal, alle seine Punkte haben dasselbe Potenzial. Das ist berechtigt: Bei 0,1 V/m fallen über 10 cm Draht nur 10 mV ab.

:::herleitung Plattenpaar und Bezugspunkt
⁠**Feldstärke.** Zwischen A und B ist $\vec E$ konstant und zeigt längs des Wegs: $U_\mathrm{AB}=\int_0^dE\,\mathrm{d} x=E\,d$.

⁠**Bezugspunkt.** Mit [(7.1)](das-potenzial.html#gl-7-1) und Wegunabhängigkeit ist

$$\varphi'(P)=\int_{P}^{P_0'}\vec E\cdot\mathrm{d}\vec s=\int_{P}^{P_0}\vec E\cdot\mathrm{d}\vec s+\int_{P_0}^{P_0'}\vec E\cdot\mathrm{d}\vec s=\varphi(P)+c.$$

Das zweite Integral hängt nicht von $P$ ab, in der Differenz fällt es weg.
:::

:::abbildung et1/k1symbole 9
Links und Mitte: Schaltzeichen einer Batterie (langer dünner Strich: Pluspol) und einer Gleichspannungsquelle, die eine feste Spannung liefert. Der Zählpfeil zeigt vom Plus- zum Minusanschluss. Rechts: Zwei Punkte, zwei Zählpfeile, zwei Vorzeichen.
:::

:::abbildung et1/k1masse 10
Derselbe Stromkreis mit Masse an drei Stellen. Die Potenziale sind 9 V, 3 V, 0 V, dann 6 V, 0 V, $-3$ V, dann 0 V, $-6$ V, $-9$ V. Jedes Mal liegen 6 V am oberen und 3 V am unteren Widerstand.
:::

::::beispiel
Im Plattenpaar ist $E=9\,\mathrm{V}/3\,\mathrm{mm}=3$ kV/m, 1000-mal weniger als die Durchschlagsfeldstärke von Luft. Eine Blockbatterie liefert rund 0,5 Ah (Ampere mal Stunden), das sind 1800 C. Ihre gesamte Energie ist $W=Q\,U=1800\,\mathrm{C}\cdot9\,\mathrm{V}=16{,}2$ kJ $=4{,}5$ Wh. Im Stromkreis liegt die Masse zunächst am Minuspol (Abb. [10](#abb-10) links). Mit [(8.2)](#gl-8-2) ergibt sich von unten nach oben 0 V, $0+3$ V, $3+6$ V. Wandert die Masse in die Mitte, sinkt jedes Potenzial um 3 V. Die Spannung am oberen Widerstand ist vorher $9\,\mathrm{V}-3\,\mathrm{V}$, nachher $6\,\mathrm{V}-0\,\mathrm{V}$. In Kraftfahrzeugen ist meist der Minuspol der Batterie mit der Karosserie verbunden, sie ist dort die Masse.
::::

⁠**Kurz gesagt:** Spannung ist Energie je Ladung zwischen zwei Punkten.

⁠**Grenzfälle:** Für $P_2=P_1$ ist $U=0$, ebenso für zwei Punkte im selben ruhenden Metallstück. Bei $d=3$ µ m ergäben 9 V schon 3 MV/m.

:::frage Warum passiert einem Vogel auf der Hochspannungsleitung nichts?
Die Leitung hat gegen die Erde mehrere Hundert Kilovolt, doch der Vogel berührt nur die Leitung. Zwischen seinen Füßen liegen bei $E\approx0{,}1$ V/m und 5 cm Abstand nur 5 mV. Es zählt die Differenz zwischen den berührten Punkten, nicht das Potenzial selbst.
:::

:::frage Fließt Strom in die Masse ab?
Über einen einzelnen Masseanschluss nicht. Strom braucht einen geschlossenen Weg, und der eine Anschluss bietet keinen Rückweg. Masse ist eine Vereinbarung über den Nullpunkt, kein Abfluss.
:::

:::ltspice Masse verschieben
⁠**Zeichnen:** Quelle `voltage` mit `9` von `a` nach `b`, `res` mit `2k` von `a` nach `m`, `res` mit `1k` von `m` nach `b`. Setze das Massesymbol zuerst an `b`, dann an `m`, dann an `a`. LTspice braucht immer eine Masse. Die Widerstände erklärt [Kapitel 2](/wissen/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/strom-widerstand-und-kirchhoff/strom-widerstand-und-kirchhoff.html), hier sorgen sie nur für die Aufteilung 6 V und 3 V.

⁠**Direktiven:** `.op`, dazu für jedes Netz ohne Masse eine Messung wie `.meas op pa FIND V(a)`. Das Netz mit Masse hat keinen eigenen Wert, für es setzt du 0 ein.

⁠**Was du siehst:** Masse an `b`: $\mathtt{V(a)}=9$ V, $\mathtt{V(m)}=3$ V. Masse an `m`: $\mathtt{V(a)}=6$ V, $\mathtt{V(b)}=-3$ V. Masse an `a`: $\mathtt{V(m)}=-6$ V, $\mathtt{V(b)}=-9$ V. Die Differenz zwischen `a` und `m` ist immer 6 V. Baue danach das Netz aus Aufgabe [9](#aufg-9) mit `5k`, `4k`, `3k` auf und prüfe deine Potenziale.
:::

:::aufgabe Aufgabe 8 ★ Spannung und Energie
<span class="anker" id="aufg-8"></span>

<ol class="al">

<li>

Ein Blitz transportiert 5 C über 100 MV. Wie groß ist die Energie in MJ und in kWh?

</li>

<li>

Luft schlägt bei $3\cdot10^6$ V/m durch. Welche Spannung braucht ein Funke über 1 cm?

</li>

<li>

Es ist $U_{12}=+5$ V. Wie groß ist $U_{21}$? Welcher Punkt liegt höher?

</li>

</ol>

:::loesung
(a) $W=Q\,U=5\,\mathrm{C}\cdot100\,\mathrm{MV}=500$ MJ $=139$ kWh. (b) $U=E\,d=3\cdot10^6\,\mathrm{V/m}\cdot0{,}01\,\mathrm{m}=30$ kV. (c) $U_{21}=-5$ V, Punkt 1 liegt 5 V höher.
:::
:::

:::aufgabe Aufgabe 9 ★★ Potenziale in einer Kette
<span class="anker" id="aufg-9"></span>

Eine 12-V-Quelle speist drei hintereinanderliegende Widerstände. Die Verbindungspunkte (__Knoten__) heißen 1 (Pluspol), 2, 3 und 4 (Minuspol). Es ist $U_{12}=5$ V, $U_{23}=4$ V, $U_{34}=3$ V.

<ol class="al">

<li>

Gib alle Potenziale an, wenn die Masse an Knoten 4 liegt, und dann, wenn sie an Knoten 3 liegt.

</li>

<li>

Berechne $U_{24}$ und $U_{13}$ in beiden Fällen. Was fällt auf?

</li>

</ol>

:::loesung
(a) Masse an 4: $\varphi_4=0$, $\varphi_3=3$ V, $\varphi_2=7$ V, $\varphi_1=12$ V. Masse an 3: alle Werte sinken um 3 V, $\varphi_4=-3$ V, $\varphi_3=0$, $\varphi_2=4$ V, $\varphi_1=9$ V. (b) Erster Fall: $U_{24}=7$ V, $U_{13}=12\,\mathrm{V}-3\,\mathrm{V}=9$ V. Zweiter Fall: $U_{24}=4\,\mathrm{V}-(-3\,\mathrm{V})=7$ V, $U_{13}=9\,\mathrm{V}-0=9$ V. Die Spannungen bleiben gleich.
:::
:::
