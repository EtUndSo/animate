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

::::lernkarten
:::karte begriff Spannung
Was gibt die Spannung $U_{12}$ zwischen zwei Punkten $P_1$ und $P_2$ an?
---
Die Arbeit je Ladung, die das Feld auf dem Weg von $P_1$ nach $P_2$ abgibt, gleich der Differenz der Potenziale: $U_{12}=\varphi(P_1)-\varphi(P_2)$, Einheit Volt, $1\,\mathrm{V}=1\,\mathrm{J/C}$.
--- falsch
Die Ladung je Zeit, die von $P_1$ nach $P_2$ fließt. Sie ist die Differenz der Ladungen der beiden Punkte, $U_{12}=Q_1-Q_2$, Einheit Volt, $1\,\mathrm{V}=1\,\mathrm{C/s}$, also ein Coulomb je Sekunde.
--- falsch
Die gesamte Energie, die zwischen $P_1$ und $P_2$ gespeichert ist, gleich wie viel Ladung von $P_1$ nach $P_2$ hindurchgeht. Sie ist $U_{12}=W_{12}$, Einheit Volt, $1\,\mathrm{V}=1\,\mathrm{J}$.
--- falsch
Das Potenzial von $P_1$ allein, also die Arbeit je Ladung von $P_1$ bis zum Bezugspunkt: $U_{12}=\varphi(P_1)$, Einheit Volt, $1\,\mathrm{V}=1\,\mathrm{J/C}$. $P_2$ legt nur die Messrichtung fest.
:::
:::karte formel Spannung aus Potenzial, Feld und Arbeit
Wie berechnet man die Spannung $U_{12}$ aus den Potenzialen, aus dem Feld und aus der Arbeit an einer Ladung $Q$?
---
$U_{12}=\varphi(P_1)-\varphi(P_2)=\int_{P_1}^{P_2}\vec E\cdot\mathrm{d}\vec s=\frac{W_{12}}{Q}$. Das Integral hängt nur im elektrostatischen Feld nicht vom Weg ab. Die Reihenfolge zählt: $U_{21}=-U_{12}$.
--- falsch
$U_{12}=\varphi(P_2)-\varphi(P_1)=-\int_{P_1}^{P_2}\vec E\cdot\mathrm{d}\vec s=-\frac{W_{12}}{Q}$. Das Integral hängt nur im elektrostatischen Feld nicht vom Weg ab. Die Reihenfolge zählt: $U_{21}=-U_{12}$.
--- falsch
$U_{12}=\varphi(P_1)-\varphi(P_2)=\int_{P_1}^{P_2}\vec E\cdot\mathrm{d}\vec s=W_{12}\cdot Q$. Das Integral hängt nur im elektrostatischen Feld nicht vom Weg ab. Die Reihenfolge zählt: $U_{21}=-U_{12}$.
--- falsch
$U_{12}=\varphi(P_1)-\varphi(P_2)=\int_{P_1}^{P_2}\vec E\cdot\mathrm{d}\vec s=\frac{W_{12}}{Q}$. Das Integral hängt in jedem Feld nicht vom Weg ab. Die Reihenfolge zählt nicht: $U_{21}=U_{12}$.
:::
:::karte formel Spannung, Arbeit und Ladung
Wie hängen Spannung, Arbeit und Ladung zusammen, und was bedeutet danach die Angabe 9 V auf einer Blockbatterie?
---
$W=Q\,U$: Die Arbeit an einer Ladung ist Ladung mal durchlaufene Spannung. 9 V heißen also 9 J je Coulomb, das von Anschluss zu Anschluss gelangt. Die gesamte Energie hängt zusätzlich davon ab, wie viel Ladung die Batterie abgibt.
--- falsch
$W=U/Q$: Die Arbeit ist Spannung je Ladung. 9 V heißen also $1/9$ J für jedes Coulomb, das von einem Anschluss zum anderen gelangt; je mehr Ladung durchläuft, desto weniger Energie bekommt jedes einzelne Coulomb mit.
--- falsch
$W=U$: Spannung und Energie sind dieselbe Größe, nur in anderer Einheit angegeben. 9 V heißen also, dass die Batterie insgesamt 9 J Energie enthält, gleich wie viel Ladung sie abgeben kann.
--- falsch
$W=Q\,U$: Die Arbeit an einer Ladung ist Ladung mal durchlaufene Spannung. 9 V heißen also, dass die Batterie insgesamt 9 C Ladung gespeichert hat, die sie von einem Anschluss zum anderen abgeben kann.
:::
:::karte begriff Masse
Was ist die Masse einer Schaltung?
---
Der Punkt der Schaltung, dem man $\varphi:=0$ V zuordnet, auch Bezugspotenzial oder GND; mit dem Erdboden verbunden heißt er Erde. Seine Lage ist frei wählbar und ändert keine Spannung.
--- falsch
Der Punkt der Schaltung, über den der Strom in den Erdboden abfließt. Ohne diesen Abfluss könnte in der Schaltung kein Strom fließen, deshalb braucht jede Schaltung genau eine Masse.
--- falsch
Der Punkt der Schaltung mit dem niedrigsten Potenzial. Er liegt immer am Minuspol der Quelle, deshalb können Potenziale in einer Schaltung nie negativ sein, höchstens null.
--- falsch
Der Punkt der Schaltung, an dem die Spannung null ist. Jede Spannung misst man zwischen einem Punkt und der Masse, nie zwischen zwei anderen Punkten der Schaltung.
:::
:::karte begriff Zählpfeil
Was legt der Zählpfeil einer Spannung in einem Schaltplan fest?
---
Das Vorzeichen: Ein Pfeil von Punkt 1 nach Punkt 2 steht für $U_{12}=\varphi_1-\varphi_2$. Ist $U_{12}>0$, liegt Punkt 1 höher; kehrt man den Pfeil um, gilt $U_{21}=-U_{12}$.
--- falsch
Das Vorzeichen: Ein Pfeil von Punkt 1 nach Punkt 2 steht für $U_{12}=\varphi_2-\varphi_1$. Ist $U_{12}>0$, liegt Punkt 2 höher; kehrt man den Pfeil um, gilt $U_{21}=-U_{12}$.
--- falsch
Die Richtung, in die die Elektronen laufen: Ein Pfeil von Punkt 1 nach Punkt 2 heißt, dass Elektronen von 1 nach 2 wandern. Ohne Bewegung zeichnet man keinen Pfeil.
--- falsch
Den Betrag: Die Länge des Pfeils zeigt, wie groß die Spannung ist. Seine Richtung ist ohne Bedeutung, denn es gilt immer $U_{21}=U_{12}$.
:::
:::karte formel Potenziale von der Masse aus
Wie bestimmt man das Potenzial $\varphi_1$ eines Punkts, wenn man das Potenzial $\varphi_2$ eines anderen Punkts und die Spannung $U_{12}$ kennt?
---
$\varphi_1=\varphi_2+U_{12}$. Von der Masse ($\varphi=0$) aus geht man so Punkt für Punkt weiter und addiert die Spannungen mit Vorzeichen.
--- falsch
$\varphi_1=\varphi_2-U_{12}$. Von der Masse ($\varphi=0$) aus geht man so Punkt für Punkt weiter und zieht die Spannungen mit Vorzeichen ab.
--- falsch
$\varphi_1=U_{12}$, unabhängig von $\varphi_2$. Das Potenzial eines Punkts ist die Spannung zum Nachbarpunkt, die Masse spielt keine Rolle.
--- falsch
$\varphi_1=\varphi_2+|U_{12}|$. Von der Masse ($\varphi=0$) aus geht man so Punkt für Punkt weiter und addiert die Beträge der Spannungen, ohne Vorzeichen.
:::
:::karte formel Feld zwischen zwei Platten
Wie groß ist die Feldstärke zwischen zwei parallelen Platten im Abstand $d$, an denen die Spannung $U$ liegt?
---
$E=\frac{U}{d}$, überall zwischen den Platten gleich. Das gilt, solange $d$ klein gegen die Plattenbreite ist; die Feldstärke sagt, wie viel Spannung je Meter Weg abfällt.
--- falsch
$E=U\cdot d$, überall zwischen den Platten gleich. Das gilt, solange $d$ klein gegen die Plattenbreite ist; größerer Abstand ergibt bei gleicher Spannung ein stärkeres Feld.
--- falsch
$E=\frac{U}{d^2}$, wie beim Feld einer Punktladung, das mit dem Quadrat des Abstands fällt. Das gilt, solange $d$ klein gegen die Plattenbreite ist.
--- falsch
$E=\frac{U}{d}$, aber nur in der Mitte zwischen den Platten. Zu den Platten hin wird das Feld stärker, weil dort die Ladungen sitzen.
:::
:::karte herleitung Freiheit des Bezugspunkts
Zeige, dass ein anderer Bezugspunkt $P_0'$ alle Potenziale um dieselbe Konstante $c$ verschiebt und keine Spannung ändert.
---
Man geht von $P$ über den alten Bezugspunkt $P_0$ zum neuen: $\varphi'(P)=\int_{P}^{P_0'}\vec E\cdot\mathrm{d}\vec s=\int_{P}^{P_0}\vec E\cdot\mathrm{d}\vec s+\int_{P_0}^{P_0'}\vec E\cdot\mathrm{d}\vec s$, weil das Integral im elektrostatischen Feld nicht vom Weg abhängt.
---
Das erste Integral ist $\varphi(P)$, weil es bis zum alten Bezugspunkt läuft.
---
Das zweite Integral hängt nicht von $P$ ab, weil es nur zwischen $P_0$ und $P_0'$ läuft; man nennt es $c$. Also ist $\varphi'(P)=\varphi(P)+c$ für jeden Punkt.
---
In der Differenz fällt $c$ weg, $\varphi'_1-\varphi'_2=(\varphi_1+c)-(\varphi_2+c)=U_{12}$, weil beide Potenziale um denselben Betrag verschoben sind.
:::
:::karte zusammenhang Masse verschieben
Was passiert mit den Potenzialen und den Spannungen einer Schaltung, wenn man die Masse an einen anderen Punkt legt?
---
Alle Potenziale ändern sich um dieselbe Konstante $c$, $\varphi'(P)=\varphi(P)+c$. Die Spannungen bleiben gleich, weil sich $c$ in jeder Differenz heraushebt.
--- falsch
Die Potenziale bleiben gleich, aber die Spannungen ändern sich, weil sie nun gegen einen anderen Punkt der Schaltung gemessen werden.
--- falsch
Potenziale und Spannungen ändern sich um dieselbe Konstante $c$, weil jede Spannung aus den Potenzialen der Punkte berechnet wird.
--- falsch
Alle Potenziale werden mit demselben Faktor $c$ multipliziert. Die Spannungen ändern sich dadurch, ihr Verhältnis zueinander bleibt aber.
:::
:::karte zusammenhang Nur Differenzen wirken
Warum hat jedes Spannungsmessgerät zwei Anschlüsse?
---
Weil nur Potenzialdifferenzen wirken: Eine Kraft auf eine Ladung gibt es nur, wo sich das Potenzial mit dem Ort ändert. Ein überall gleich hohes Potenzial bewirkt nichts, egal wie hoch.
--- falsch
Weil ein Anschluss die positive und der andere die negative Ladung der Spannung aufnimmt. Erst beide Ladungen zusammen ergeben im Gerät den Messwert der Spannung.
--- falsch
Weil das Gerät die Potenziale der beiden Punkte addiert. Die Summe der beiden Potenziale ist die Spannung zwischen ihnen, ein einzelnes Potenzial wäre nur die Hälfte.
--- falsch
Weil ein Anschluss mit dem Erdboden verbunden sein muss. Nur gegen die Erde hat ein Potenzial einen festen Wert, den man messen kann; andere Punkte als Bezug eignen sich dafür nicht.
:::
:::karte zusammenhang Vogel auf der Leitung
Warum passiert einem Vogel auf einer Hochspannungsleitung nichts, obwohl sie gegen die Erde mehrere Hundert Kilovolt hat?
---
Weil nur die Spannung zwischen den berührten Punkten zählt: Zwischen seinen Füßen liegen bei $E\approx0{,}1$ V/m und 5 cm Abstand nur 5 mV. Das hohe Potenzial der Leitung selbst bewirkt nichts.
--- falsch
Weil eine einzelne Leitung gar kein Potenzial hat. Gefährlich wird die Hochspannung erst, wenn zwei Leitungen einander berühren und sich ihre Potenziale dabei zu einer Spannung addieren.
--- falsch
Weil zwischen Leitung und Vogel keine Masse liegt. Eine Spannung wirkt nur zwischen einem Punkt und der Masse, nicht zwischen zwei Füßen auf demselben Draht.
--- falsch
Weil ein Vogel zu klein ist, um nennenswert Ladung aufzunehmen. Erst ab der Größe eines Menschen kann die Spannung der Leitung gegen die Erde eine spürbare Wirkung entfalten.
:::
::::
