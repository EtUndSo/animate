---
title: Stufe 5: Kennlinie, Durchbruch und Spezialdioden
pfad: Elektrotechnik / 1. Semester / ET1 – Grundgebiete der Elektrotechnik 1: Einführung in die Schaltungsanalyse / Halbleiter und Dioden
adresse: elektrotechnik/1-semester/grundlagen-der-elektrotechnik/halbleiter-und-dioden
knoten: Kapitel 9: Halbleiter und Dioden
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

**Kapazitätsdiode.** Die trägerfreie Zone ist eine isolierende Schicht zwischen zwei leitenden Gebieten, also ein Kondensator ([Kapitel 3](/wissen/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/der-kondensator/der-kondensator.html)) mit der Fläche $A$ und dem Abstand $w$. Die __Sperrschichtkapazität__ sinkt mit der Sperrspannung $U_\mathrm R=-U$, weil die Zone wächst:

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

::::formelsammlung
**Leistung im Durchbruch**

$$P=U\,I$$

Wärme in der Diode; sie zerstört die Diode im Durchbruch, wenn nichts den Strom begrenzt. Der Durchbruch selbst schadet nicht.

**Widerstand der Zener-Diode**

$$r_\mathrm Z=\Delta U/\Delta I$$

Kleiner Widerstand der fast senkrechten Kennlinie oberhalb von $U_\mathrm Z$. Ein Vorwiderstand nimmt Schwankungen der Quelle auf.

**Sperrschichtkapazität**

$$C_\mathrm{Sp}=\frac{\varepsilon A}{w}=\frac{C_0}{\sqrt{1+U_\mathrm R/U_\mathrm{D0}}}$$

$A$ Fläche, $w$ Breite der Zone, $U_\mathrm R=-U$ die Sperrspannung. Gilt für einen scharfen Übergang in Sperrrichtung. Kapazitätsdioden nutzen den Effekt.

**Photonenenergie und innerer Photoeffekt**

$$W=h\,c/\lambda,\qquad W\ge W_\mathrm g$$

$h$ Planck-Konstante, $c$ Lichtgeschwindigkeit, $\lambda$ Wellenlänge. Ist $W\ge W_\mathrm g$, hebt ein Photon ein Elektron ins Leitungsband; bei Silizium verlangt das $\lambda\le1107$ nm.

**Beleuchtete Diode**

$$I=I_\mathrm S\bigl(\mathrm{e}^{U/U_T}-1\bigr)-I_\mathrm{Ph}$$

$I_\mathrm{Ph}$ ist der Photostrom, der Lichtleistung proportional. Ersatzschaltbild: Stromquelle parallel zur Diode. Als Lichtsensor in Sperrrichtung ist $I\approx-I_\mathrm{Ph}$. Eine Solarzelle arbeitet bei $U>0$ und $I<0$ und gibt Leistung ab.

**Leerlaufspannung**

$$U_\mathrm L=U_T\ln\Bigl(\frac{I_\mathrm{Ph}}{I_\mathrm S}+1\Bigr)$$

Gilt im Leerlauf ($I=0$). Zehnfaches Licht hebt $U_\mathrm L$ nur um rund 60 mV; bei Silizium liegt die Spannung im Betrieb um 0,5 V. Für $I_\mathrm{Ph}=0$ ist $U_\mathrm L=0$.
::::

::::lernkarten
:::karte begriff Anode und Kathode
Welche Seite einer Diode heißt Anode, welche Kathode, und wie zeigt das Schaltzeichen die Durchlassrichtung?
---
Die p-Seite heißt Anode, die n-Seite Kathode; beide tragen Metallkontakte. Das Dreieck des Schaltzeichens zeigt in Durchlassrichtung, von der Anode zur Kathode.
--- falsch
Die n-Seite heißt Anode, die p-Seite Kathode. Das Dreieck des Schaltzeichens zeigt in Sperrrichtung, und der Strich markiert die Seite, an der der Strom eintritt.
--- falsch
Die p-Seite heißt Anode, die n-Seite Kathode. Das Dreieck des Schaltzeichens zeigt in Sperrrichtung, also von der Kathode zur Anode.
--- falsch
Der Anschluss mit dem höheren Potenzial heißt immer Anode, der andere Kathode. Die Namen wechseln deshalb mit der Polung der angelegten Spannung.
:::
:::karte zusammenhang Kennlinie ohne Schwelle
Warum zeigt die Kennlinie einer Diode in linearer Darstellung scheinbar einen Knick bei 0,6 V, obwohl sie keine Schwelle hat?
---
Der Knick liegt am Maßstab, eine Exponentialfunktion hat keine Schwelle. Auf einer Achse bis 10 mA erreicht die Kurve 1 % des Endwerts bei 0,595 V, auf einer bis 10 µ A schon bei 0,417 V.
--- falsch
Bei 0,6 V verschwindet die Barriere der Raumladungszone schlagartig, und die Diode schaltet von Sperren auf Leiten um. Darunter fließt gar kein Strom, darüber der volle, den die Schaltung zulässt.
--- falsch
Der Knick ist echt: Bei 0,6 V setzt der Bahnwiderstand der neutralen Gebiete ein und begrenzt den Strom, sodass die Kurve oberhalb gerade weiterläuft und darunter waagerecht bleibt.
--- falsch
Der Knick liegt am Maßstab, aber nur bei Silizium: Dort ist der Sperrstrom null, und die Kurve beginnt erst bei 0,6 V. Bei Germanium beginnt sie tiefer und hat deshalb keinen Knick.
:::
:::karte begriff Durchbruch
Was geschieht beim Durchbruch einer Diode, und wodurch wird sie dabei zerstört?
---
Bei großer Sperrspannung steigt der Sperrstrom steil an. Der Durchbruch selbst schadet nicht; zerstört wird die Diode erst durch die Wärme $P=U\,I$, wenn nichts den Strom begrenzt.
--- falsch
Bei großer Sperrspannung reißt die Raumladungszone mechanisch auf, und der Strom steigt steil an. Die Diode ist danach dauerhaft leitend, gleich wie groß der Strom war.
--- falsch
Bei großer Durchlassspannung verschwindet die Barriere, und der Strom steigt steil an. Dabei schmilzt die Diode sofort, auch wenn ein Widerstand den Strom begrenzt.
--- falsch
Bei großer Sperrspannung sinkt der Sperrstrom auf null, weil die Zone den ganzen Kristall füllt. Zerstört wird die Diode durch die hohe Spannung selbst, nicht durch Wärme.
:::
:::karte begriff Lawineneffekt und Zener-Effekt
Durch welche zwei Mechanismen setzt bei großer Sperrspannung der Durchbruch einer Diode ein?
---
Beim Lawineneffekt setzen Träger, die das starke Feld beschleunigt, durch Stöße neue Paare frei. Beim Zener-Effekt gelangen Elektronen im starken Feld direkt aus dem VB ins LB.
--- falsch
Beim Lawineneffekt schmilzt die Zone durch die Wärme und wird leitend. Beim Zener-Effekt wandern die Ionen im starken Feld aus der Zone heraus und lassen sie zusammenbrechen.
--- falsch
Beim Lawineneffekt gelangen Elektronen im starken Feld direkt aus dem VB ins LB. Beim Zener-Effekt setzen beschleunigte Träger durch Stöße neue Paare frei.
--- falsch
Beim Lawineneffekt rutschen die Mehrheitsträger über die gesunkene Barriere. Beim Zener-Effekt senkt das Feld den Bandabstand, bis die Wärme genügt, um Elektronen anzuheben.
:::
:::karte zusammenhang Zener-Diode mit Vorwiderstand
Warum hält eine Zener-Diode mit Vorwiderstand ihre Spannung fast fest, wenn die Quelle schwankt?
---
Oberhalb von $U_\mathrm Z$ ist ihre Kennlinie fast senkrecht, ihr kleiner Widerstand ist $r_\mathrm Z=\Delta U/\Delta I$. Der Vorwiderstand nimmt die Schwankung auf: Der Strom ändert sich, die Spannung kaum.
--- falsch
Sie hat in Sperrrichtung einen sehr großen Widerstand, der die Schwankung der Quelle fast ganz übernimmt. Der Vorwiderstand führt dann einen konstanten Strom, und die Spannung an ihm bleibt fest.
--- falsch
Oberhalb von $U_\mathrm Z$ fließt kein Strom mehr durch sie, sie trennt die Last von der Quelle. Der Vorwiderstand teilt die Spannung dann in einem festen Verhältnis, das die Schwankung halbiert.
--- falsch
Sie arbeitet im Durchlass, wo ihre Spannung immer genau 0,7 V beträgt. Mehrere davon in Reihe ergeben $U_\mathrm Z$, und der Vorwiderstand begrenzt nur den Strom durch sie.
:::
:::karte begriff Sperrschichtkapazität
Was ist die Sperrschichtkapazität eines pn-Übergangs, und warum sinkt sie mit der Sperrspannung?
---
Die trägerfreie Zone ist eine isolierende Schicht zwischen zwei leitenden Gebieten, also ein Kondensator mit Fläche $A$ und Abstand $w$: $C_\mathrm{Sp}=\varepsilon A/w$. Mit der Sperrspannung wächst $w$, also sinkt $C_\mathrm{Sp}$.
--- falsch
Die Kapazität zwischen den beiden Metallkontakten der Diode. Sie sinkt mit der Sperrspannung, weil sich die Kontakte unter der Kraft des Feldes ein wenig voneinander entfernen.
--- falsch
Die trägerfreie Zone wirkt als Kondensator mit $C_\mathrm{Sp}=\varepsilon A\,w$. Mit der Sperrspannung wird die Zone schmaler, weil das Feld die Ionen zusammendrückt, und die Kapazität sinkt deshalb.
--- falsch
Die Fähigkeit der Zone, Ladungsträger zu speichern, die bei Sperrspannung abfließen. Je mehr Sperrspannung anliegt, desto mehr Träger fehlen ihr, und die Kapazität sinkt deshalb genau proportional zu $U_\mathrm R$.
:::
:::karte formel Kapazitätsdiode
Wie hängt die Sperrschichtkapazität von der Sperrspannung $U_\mathrm R=-U$ ab, und wofür nutzt man das in Kapazitätsdioden?
---
$C_\mathrm{Sp}=\frac{C_0}{\sqrt{1+U_\mathrm R/U_\mathrm{D0}}}$ für einen scharfen Übergang in Sperrrichtung. Mit ihr verstellt man per Spannung die Frequenz von Schwingkreisen, etwa in Funkempfängern.
--- falsch
$C_\mathrm{Sp}=C_0\sqrt{1+U_\mathrm R/U_\mathrm{D0}}$, sie wächst also mit der Sperrspannung. Man nutzt sie, um per Spannung die Lautstärke von Funkempfängern zu verstellen.
--- falsch
$C_\mathrm{Sp}=\frac{C_0}{1+U_\mathrm R/U_\mathrm{D0}}$, ohne Wurzel. Man nutzt sie als Speicher für große Energiemengen, weil sie mit steigender Spannung immer mehr Ladung aufnimmt und nie voll wird.
--- falsch
$C_\mathrm{Sp}=\frac{C_0}{\sqrt{1+U_\mathrm R/U_\mathrm{D0}}}$ für den Betrieb im Durchlass. Man nutzt sie, um den Strom durch die Diode bei hohen Frequenzen zu glätten.
:::
:::karte begriff Photonen und innerer Photoeffekt
Was sind Photonen, und wann löst ein Photon in einem Halbleiter den inneren Photoeffekt aus?
---
Photonen sind die Energiepakete des Lichts mit $W=h\,c/\lambda$. Ist $W\ge W_\mathrm g$, hebt ein Photon ein Elektron ins LB, das ist der innere Photoeffekt; bei Silizium verlangt das $\lambda\le1107$ nm.
--- falsch
Photonen sind die Elektronen, die Licht aus einer Oberfläche schlägt. Der innere Photoeffekt tritt ein, wenn ihre Energie größer als die Wärmeenergie ist, bei Silizium also für jede Wellenlänge.
--- falsch
Photonen sind die Energiepakete des Lichts mit $W=h\,c/\lambda$. Ist $W\ge W_\mathrm g$, hebt ein Photon ein Elektron ins LB; bei Silizium verlangt das $\lambda\ge1107$ nm, also langwelliges Licht.
--- falsch
Photonen sind Lichtteilchen, deren Energie mit der Helligkeit wächst. Der innere Photoeffekt tritt bei jedem Licht ein, wenn es nur hell genug ist, weil sich die Energien vieler Photonen addieren.
:::
:::karte begriff Photostrom
Was ist der Photostrom einer beleuchteten Diode, und in welche Richtung fließt er?
---
Der Strom der Paare, die das Licht erzeugt und das Feld der Zone trennt: Das Elektron läuft zur n-Seite, das Loch zur p-Seite. Er fließt in Sperrrichtung und ist der Lichtleistung proportional.
--- falsch
Der Strom, den das Licht in den Metallkontakten auslöst. Er fließt von Anode nach Kathode durch die Diode, also in Durchlassrichtung, und wächst mit dem Logarithmus der Lichtleistung.
--- falsch
Der Strom der Paare, die das Licht erzeugt und das Feld der Zone trennt: Das Elektron läuft zur p-Seite, das Loch zur n-Seite. Er fließt in Durchlassrichtung und ist der Lichtleistung proportional.
--- falsch
Der Strom der Paare, die das Licht erzeugt und das Feld der Zone trennt. Er fließt in Sperrrichtung, hängt aber nur von der Wellenlänge ab und nicht davon, wie hell das Licht ist.
:::
:::karte formel Beleuchtete Diode
Wie lautet die Kennlinie einer beleuchteten Diode, und durch welches Ersatzschaltbild wird sie dargestellt?
---
$I=I_\mathrm S\bigl(\mathrm{e}^{U/U_T}-1\bigr)-I_\mathrm{Ph}$: Die Kennlinie verschiebt sich um den Photostrom nach unten. Das Ersatzschaltbild ist eine Stromquelle parallel zur Diode.
--- falsch
$I=I_\mathrm S\bigl(\mathrm{e}^{U/U_T}-1\bigr)+I_\mathrm{Ph}$: Die Kennlinie verschiebt sich um den Photostrom nach oben. Das Ersatzschaltbild ist eine Spannungsquelle in Reihe mit der Diode.
--- falsch
$I=(I_\mathrm S-I_\mathrm{Ph})\bigl(\mathrm{e}^{U/U_T}-1\bigr)$: Licht verkleinert den Sperrstrom. Das Ersatzschaltbild ist ein Widerstand parallel zur Diode, dessen Wert mit dem Licht sinkt.
--- falsch
$I=I_\mathrm S\bigl(\mathrm{e}^{U/U_T}-1\bigr)-I_\mathrm{Ph}$: Die Kennlinie verschiebt sich um den Photostrom nach rechts. Das Ersatzschaltbild ist eine Stromquelle in Reihe mit der Diode.
:::
:::karte zusammenhang Photodiode als Lichtsensor
Warum betreibt man eine Photodiode als Lichtsensor in Sperrrichtung?
---
Dann ist $I\approx-I_\mathrm{Ph}$: Der Anteil $I_\mathrm S(\mathrm{e}^{U/U_T}-1)$ ist auf $-I_\mathrm S$ geschrumpft, und der Strom folgt direkt dem Photostrom, also der Lichtleistung.
--- falsch
Dann ist die Spannung an ihr der Lichtleistung proportional, und man kann die Helligkeit direkt mit einem Voltmeter an den Anschlüssen ablesen.
--- falsch
Dann leitet sie nicht, und das Licht kann die Zone ungehindert durchdringen; im Durchlass würden die freien Elektronen das Licht verschlucken.
--- falsch
Dann ist $I\approx-I_\mathrm S$: Der Strom hängt nicht vom Licht ab, und die Diode dient als fester Bezug, gegen den man die Helligkeit vergleicht.
:::
:::karte formel Leerlaufspannung der Solarzelle
Wie groß ist die Leerlaufspannung einer beleuchteten Diode, und warum hebt zehnfaches Licht sie nur um rund 60 mV?
---
$U_\mathrm L=U_T\ln\Bigl(\frac{I_\mathrm{Ph}}{I_\mathrm S}+1\Bigr)$ für $I=0$. Zehnfaches Licht verzehnfacht $I_\mathrm{Ph}$, doch der Logarithmus macht daraus nur rund 60 mV mehr.
--- falsch
$U_\mathrm L=U_T\,\frac{I_\mathrm{Ph}}{I_\mathrm S}$ für $I=0$. Zehnfaches Licht hebt sie trotzdem nur um rund 60 mV, weil sich die Zelle dabei erwärmt und $U_T$ entsprechend sinkt.
--- falsch
$U_\mathrm L=I_\mathrm{Ph}\,R$ mit dem inneren Widerstand der Zelle. Zehnfaches Licht hebt sie nur um rund 60 mV, weil dieser Widerstand mit dem Licht stark sinkt und den Anstieg fast aufhebt.
--- falsch
$U_\mathrm L=U_T\ln\Bigl(\frac{I_\mathrm S}{I_\mathrm{Ph}}+1\Bigr)$ für $I=0$. Zehnfaches Licht senkt sie um rund 60 mV, weil mehr Ladungsträger die Zone leeren.
:::
:::karte begriff Solarzelle
Was ist eine Solarzelle, und woran erkennt man an ihren Zählpfeilen, dass sie Leistung abgibt?
---
Eine großflächige Photodiode, die bei $U>0$ und $I<0$ arbeitet. Das Produkt $U\,I$ ist dann negativ, sie gibt also Leistung ab; ihre Spannung liegt bei Silizium im Betrieb um 0,5 V.
--- falsch
Eine Photodiode, die in Sperrrichtung bei $U<0$ und $I<0$ arbeitet. Das Produkt $U\,I$ ist dann positiv, und sie gibt diese Leistung als Strom an die Last ab.
--- falsch
Eine großflächige Photodiode, die bei $U>0$ und $I>0$ arbeitet. Das Licht verstärkt dabei den Durchlassstrom, und die zusätzliche Leistung fließt über die Anschlüsse in die Last.
--- falsch
Eine Zener-Diode, die Licht in Wärme umwandelt. Sie gibt Leistung ab, weil ihre Spannung $U_\mathrm Z$ bei Beleuchtung über die Diffusionsspannung steigt.
:::
::::
