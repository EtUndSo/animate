---
title: Von Grund auf: Ventil, Wechselspannung und Wärmeenergie
pfad: Elektrotechnik / 1. Semester / ET1 – Grundgebiete der Elektrotechnik 1: Einführung in die Schaltungsanalyse / Halbleiter und Dioden
adresse: elektrotechnik/1-semester/grundlagen-der-elektrotechnik/halbleiter-und-dioden
knoten: Kapitel 9: Halbleiter und Dioden
order: 1190200
summary: Wie aus Silizium ein Ventil für Strom wird und wie man mit ihm rechnet
tags: Wechselspannung, Scheitelwert, Frequenz, Einweggleichrichter, Elektronenvolt, Wärmeenergie, Boltzmann-Konstanten, Boltzmann-Verteilung
lang: de
---

Eine __Wechselspannung__ wechselt periodisch ihr Vorzeichen. Hier ist sie sinusförmig, $u_\mathrm e(t)=\hat u\sin(2\pi ft)$, mit dem __Scheitelwert__ $\hat u$ (größter Betrag) und der __Frequenz__ $f$ (Schwingungen je Sekunde, Einheit Hz). Eine Schwingung dauert $T=1/f$, bei 50 Hz also 20 ms. Kleine Buchstaben stehen für zeitabhängige Größen.

:::abbildung et1/k9einweg 1
Links: Diode mit den Anschlüssen Anode (A) und Kathode (K) in Reihe mit einem Widerstand an einer Wechselspannung. Rechts oben: Am Widerstand erscheint nur die positive Halbwelle, um 0,7 V verkleinert. Rechts unten: Die Diode hält im Leiten 0,7 V und übernimmt im Sperren die ganze negative Spannung. $\hat u=12$ V, 50 Hz.
:::

Abb. [1](#abb-1) zeigt die Wirkung einer Diode. Die Masche ergibt $u_\mathrm e=u_\mathrm D+u_\mathrm a$. Ist $u_\mathrm e$ positiv, leitet die Diode, an ihr bleiben rund 0,7 V, der Rest liegt am Widerstand. Ist $u_\mathrm e$ negativ, fließt kein Strom. Dann ist $u_\mathrm a=0$, und die Diode trägt die ganze Spannung. Aus der Wechselspannung wird eine Spannung mit nur einem Vorzeichen. Diese Schaltung heißt __Einweggleichrichter__. Ihr Scheitel ist $12\,\mathrm{V}-0{,}7\,\mathrm{V}=11{,}3$ V.

Für das Warum braucht das Kapitel zwei Energiegrößen. Das __Elektronenvolt__ (eV) ist die Energie, die ein Elektron beim Durchlaufen von 1 V gewinnt ([Kapitel 1](/wissen/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/ladung-feld-und-potenzial/ladung-feld-und-potenzial.html)): $1\,\mathrm{eV}=e\cdot1\,\mathrm{V}=1{,}602\cdot10^{-19}$ J. Die __Wärmeenergie__ entsteht, weil Atome und Elektronen sich bei jeder Temperatur ungeordnet bewegen. Ihr Maß ist $k_\mathrm BT$ mit der absoluten Temperatur $T$ in K und der __Boltzmann-Konstanten__ $k_\mathrm B$. Bei 300 K ist $k_\mathrm BT=4{,}14\cdot10^{-21}\,\mathrm{J}=25{,}85$ meV. Die Stöße verteilen diese Energie ungleich: Wenige Teilchen haben viel, viele wenig. Im Gleichgewicht gilt die __Boltzmann-Verteilung__:

<span class="anker" id="gl-0-1"></span>
$$\text{Anteil der Teilchen mit mindestens der Energie }W=\mathrm{e}^{-W/(k_\mathrm BT)}. \tag{0.1}$$

Je $k_\mathrm BT$ mehr Energie sinkt der Anteil um den Faktor 2,718, bei $10\,k_\mathrm BT$ ist er $4{,}5\cdot10^{-5}$. Dasselbe Gesetz beschreibt, wie die Luft mit der Höhe dünner wird.

::::formelsammlung
**Sinusförmige Wechselspannung**

$$u_\mathrm e(t)=\hat u\sin(2\pi ft)$$

$\hat u$ ist der Scheitelwert (größter Betrag), $f$ die Frequenz (Schwingungen je Sekunde, Einheit Hz). Eine Schwingung dauert $T=1/f$. Kleine Buchstaben stehen für zeitabhängige Größen.

**Masche am Einweggleichrichter**

$$u_\mathrm e=u_\mathrm D+u_\mathrm a$$

Diode in Reihe mit einem Widerstand an $u_\mathrm e$; $u_\mathrm D$ liegt an der Diode, $u_\mathrm a$ am Widerstand. Leitet die Diode ($u_\mathrm e$ positiv), bleiben an ihr rund 0,7 V, der Scheitel des Ausgangs ist um 0,7 V kleiner als $\hat u$. Sperrt sie ($u_\mathrm e$ negativ), ist $u_\mathrm a=0$, und die Diode trägt die ganze Spannung.

**Elektronenvolt**

$$1\,\mathrm{eV}=e\cdot1\,\mathrm{V}=1{,}602\cdot10^{-19}\,\mathrm{J}$$

Energie, die ein Elektron beim Durchlaufen von 1 V gewinnt.

**Maß der Wärmeenergie**

$$k_\mathrm BT$$

$T$ absolute Temperatur in K, $k_\mathrm B=1{,}3806\cdot10^{-23}$ J/K die Boltzmann-Konstante. Bei 300 K ist $k_\mathrm BT=4{,}14\cdot10^{-21}\,\mathrm{J}=25{,}85$ meV.

**Boltzmann-Verteilung**

$$\text{Anteil der Teilchen mit mindestens der Energie }W=\mathrm{e}^{-W/(k_\mathrm BT)}$$

Gilt im Gleichgewicht. Je $k_\mathrm BT$ mehr Energie sinkt der Anteil um den Faktor 2,718.
::::

::::lernkarten
:::karte begriff Diode
Was leistet eine Diode in einer Schaltung, etwa in einem Ladegerät am Wechselspannungsnetz?
---
Sie ist ein Bauteil aus einem Halbleiter, das Strom in einer Richtung durchlässt (Durchlassrichtung) und in der anderen sperrt (Sperrrichtung). So wird aus einer Wechselspannung eine Spannung mit nur einem Vorzeichen.
--- falsch
Sie ist ein Bauteil aus einem Halbleiter, das Strom in beiden Richtungen gleich gut leitet, aber die Spannungsspitzen abschneidet. So wird aus einer Wechselspannung eine gleichmäßige Sinusspannung ohne Spitzen.
--- falsch
Sie ist ein Bauteil aus einem Metall, das Strom nur oberhalb einer festen Spannung durchlässt und darunter vollständig sperrt, gleich in welcher Richtung die Spannung an ihm anliegt.
--- falsch
Sie ist ein Bauteil aus einem Halbleiter, das in jeder Halbwelle Ladung speichert und in der nächsten wieder abgibt, ähnlich wie ein Kondensator, der ständig umgeladen wird. So entsteht eine Gleichspannung.
:::
:::karte begriff Wechselspannung
Was kennzeichnet eine Wechselspannung, wie sie ein Gleichrichter an seinem Eingang erhält?
---
Sie wechselt periodisch ihr Vorzeichen. Im betrachteten Fall ist sie sinusförmig, $u_\mathrm e(t)=\hat u\sin(2\pi ft)$, mit dem Scheitelwert $\hat u$ und der Frequenz $f$.
--- falsch
Sie ändert ihren Betrag periodisch, behält aber immer dasselbe Vorzeichen. Sie ist sinusförmig, $u_\mathrm e(t)=\hat u+\hat u\sin(2\pi ft)$, und schwankt zwischen null und dem doppelten Scheitelwert.
--- falsch
Sie wechselt periodisch ihr Vorzeichen, aber nur in Sprüngen zwischen zwei festen Werten. Eine sinusförmige Spannung zählt nicht dazu, weil sie stetig durch null läuft.
--- falsch
Sie entsteht, wenn man eine Gleichspannung durch eine Diode schickt: Die Diode schaltet in festem Takt ein und aus, sodass die Spannung zwischen null und ihrem Höchstwert wechselt.
:::
:::karte begriff Scheitelwert und Frequenz
Was geben Scheitelwert $\hat u$ und Frequenz $f$ einer sinusförmigen Wechselspannung an, und wie lange dauert eine Schwingung?
---
Der Scheitelwert ist der größte Betrag der Spannung, die Frequenz die Zahl der Schwingungen je Sekunde, Einheit Hz. Eine Schwingung dauert $T=1/f$, bei 50 Hz also 20 ms.
--- falsch
Der Scheitelwert ist der Mittelwert der Spannung über eine Schwingung, die Frequenz die Zahl der Nulldurchgänge je Sekunde. Eine Schwingung dauert $T=2/f$, bei 50 Hz also 40 ms.
--- falsch
Der Scheitelwert ist der größte Betrag der Spannung, die Frequenz die Dauer einer Schwingung in Sekunden. Eine Schwingung dauert deshalb $T=f$, bei 50 Hz also 50 s.
--- falsch
Der Scheitelwert ist der Abstand vom tiefsten zum höchsten Wert, die Frequenz die Zahl der Schwingungen je Minute. Eine Schwingung dauert $T=60/f$, bei 50 je Minute also 1,2 s.
:::
:::karte begriff Einweggleichrichter
Wie ist ein Einweggleichrichter aufgebaut, und welche Spannung liefert er an seinem Widerstand?
---
Eine Diode liegt in Reihe mit einem Widerstand an einer Wechselspannung. Am Widerstand erscheint nur die positive Halbwelle, um rund 0,7 V verkleinert; in der negativen Halbwelle fließt kein Strom, und $u_\mathrm a=0$.
--- falsch
Zwei Dioden liegen gegeneinander in Reihe mit einem Widerstand. Am Widerstand erscheinen beide Halbwellen mit gleichem Vorzeichen, jede um rund 1,4 V verkleinert, sodass der Ausgang nie null wird.
--- falsch
Eine Diode liegt parallel zu einem Widerstand an einer Wechselspannung. Am Widerstand erscheint nur die negative Halbwelle, weil die Diode in der positiven Halbwelle den Widerstand kurzschließt.
--- falsch
Eine Diode liegt in Reihe mit einem Widerstand an einer Wechselspannung. Am Widerstand erscheint die volle positive Halbwelle ohne Verlust; in der negativen Halbwelle bleibt dort ein Rest von $-0{,}7$ V stehen.
:::
:::karte zusammenhang Sperrende Diode im Einweggleichrichter
Warum trägt die Diode im Einweggleichrichter während der negativen Halbwelle die ganze Eingangsspannung?
---
Die Masche ergibt $u_\mathrm e=u_\mathrm D+u_\mathrm a$. In der negativen Halbwelle fließt kein Strom, also ist $u_\mathrm a=0$ am Widerstand, und die ganze Spannung $u_\mathrm e$ bleibt für die Diode.
--- falsch
Die Diode erzeugt in Sperrrichtung selbst eine Gegenspannung, die genau so groß ist wie $u_\mathrm e$. Beide heben sich deshalb auf, und durch den Widerstand fließt nur ein kleiner Rückstrom.
--- falsch
Die Masche ergibt $u_\mathrm e=u_\mathrm D+u_\mathrm a$. In der negativen Halbwelle fließt ein kleiner Rückstrom, der am Widerstand fast die ganze Spannung erzeugt; die Diode trägt dann nur 0,7 V.
--- falsch
Die Masche ergibt $u_\mathrm e=u_\mathrm D-u_\mathrm a$. Der Widerstand verdoppelt in der negativen Halbwelle die Spannung, und die Diode muss deshalb die doppelte Eingangsspannung tragen.
:::
:::karte zusammenhang Scheitel hinter der Diode
Warum erreicht die Ausgangsspannung eines Einweggleichrichters an einer Wechselspannung mit 12 V Scheitelwert nur 11,3 V?
---
Solange die Diode leitet, bleiben an ihr rund 0,7 V, und nur der Rest liegt am Widerstand: $12\,\mathrm{V}-0{,}7\,\mathrm{V}=11{,}3$ V.
--- falsch
Die Diode leitet erst ab 0,7 V und schneidet diesen Teil jeder Halbwelle ab; im Scheitel liegt an ihr dagegen keine Spannung mehr.
--- falsch
Die Diode verkleinert jede Spannung um denselben Anteil von etwa 6 %, weil ihr Widerstand fest ist.
--- falsch
Die Quelle bricht beim Stromfluss um 0,7 V ein; die Diode selbst trägt im Leiten keine Spannung.
:::
:::karte zusammenhang Elektronenvolt
Wie rechnet man die Wärmeenergie $k_\mathrm BT=4{,}14\cdot10^{-21}\,\mathrm{J}$ bei 300 K in Elektronenvolt um, und welchen Wert erhält man?
---
Man teilt durch $1\,\mathrm{eV}=e\cdot1\,\mathrm{V}=1{,}602\cdot10^{-19}$ J, die Energie, die ein Elektron beim Durchlaufen von 1 V gewinnt. Es ergibt sich $k_\mathrm BT=25{,}85$ meV.
--- falsch
Man multipliziert mit $1{,}602\cdot10^{-19}$, weil ein Elektronenvolt kleiner als ein Joule ist. Es ergibt sich $k_\mathrm BT=6{,}6\cdot10^{-40}$ eV, eine verschwindend kleine Energie.
--- falsch
Man teilt durch die Boltzmann-Konstante, weil das Elektronenvolt eine Einheit der Temperatur ist. Es ergibt sich $k_\mathrm BT=300$ eV, also genau die Temperatur in Kelvin.
--- falsch
Man teilt durch $1{,}602\cdot10^{-19}$ J je eV. Es ergibt sich $k_\mathrm BT=25{,}85$ eV, eine Energie, die ein Elektron erst nach rund 26 V Beschleunigung hätte.
:::
:::karte begriff Wärmeenergie
Woher kommt die Wärmeenergie der Atome und Elektronen in einem Festkörper, und durch welche Größe wird sie gemessen?
---
Atome und Elektronen bewegen sich bei jeder Temperatur ungeordnet. Das Maß dieser Energie ist $k_\mathrm BT$ mit der absoluten Temperatur $T$ in K und der Boltzmann-Konstanten $k_\mathrm B$.
--- falsch
Sie entsteht nur, wenn Strom durch den Festkörper fließt und die Elektronen an den Atomen abbremsen. Ihr Maß ist die elektrische Leistung, die im Körper in Wärme übergeht.
--- falsch
Atome und Elektronen bewegen sich nur oberhalb von 0 °C ungeordnet. Das Maß dieser Energie ist $k_\mathrm B\vartheta$ mit der Temperatur $\vartheta$ in °C, die darunter negativ wird.
--- falsch
Atome und Elektronen bewegen sich bei jeder Temperatur ungeordnet. Das Maß dieser Energie ist $k_\mathrm B/T$, sie wird also mit steigender Temperatur kleiner.
:::
:::karte begriff Boltzmann-Konstante
Welche Rolle spielt die Boltzmann-Konstante $k_\mathrm B$ für die Wärmeenergie, und welche Einheit hat sie?
---
Sie rechnet die absolute Temperatur in eine Energie um: Das Maß der Wärmeenergie ist $k_\mathrm BT$. Ihre Einheit ist J/K, $k_\mathrm B=1{,}3806\cdot10^{-23}$ J/K.
--- falsch
Sie rechnet die Temperatur in Grad Celsius in eine Spannung um: Das Maß der Wärmeenergie ist $k_\mathrm BT$ in Volt. Ihre Einheit ist V/°C, $k_\mathrm B=1{,}3806\cdot10^{-23}$ V/°C.
--- falsch
Sie gibt an, wie viele Teilchen bei einer Temperatur eine Energie überschreiten. Sie ist eine reine Zahl ohne Einheit, nämlich 2,718, die Basis der Exponentialfunktion.
--- falsch
Sie rechnet eine Energie in eine Temperatur um: Das Maß der Wärmeenergie ist $T/k_\mathrm B$. Ihre Einheit ist K/J, $k_\mathrm B=1{,}602\cdot10^{-19}$ K/J.
:::
:::karte begriff Boltzmann-Verteilung
Was beschreibt die Boltzmann-Verteilung für Teilchen im Gleichgewicht, deren Energie durch Stöße ungleich verteilt ist?
---
Den Anteil der Teilchen mit mindestens der Energie $W$: Er ist $\mathrm{e}^{-W/(k_\mathrm BT)}$. Wenige Teilchen haben viel Energie, viele wenig; mit steigender Temperatur wächst der Anteil.
--- falsch
Den Anteil der Teilchen mit mindestens der Energie $W$: Er ist $W/(k_\mathrm BT)$ und wächst linear mit der Energie, weil energiereiche Teilchen die anderen durch Stöße mitreißen.
--- falsch
Den Anteil der Teilchen mit genau der mittleren Energie $k_\mathrm BT$: Er ist für alle Stoffe gleich 1/2, denn die Stöße verteilen die Energie gleichmäßig auf alle Teilchen.
--- falsch
Den Anteil der Teilchen mit mindestens der Energie $W$: Er ist $\mathrm{e}^{-W/(k_\mathrm BT)}$ und sinkt mit steigender Temperatur, weil heiße Teilchen ihre Energie schneller abgeben.
:::
:::karte formel Anteil nach der Boltzmann-Verteilung
Wie groß ist nach der Boltzmann-Verteilung der Anteil der Teilchen mit mindestens der Energie $10\,k_\mathrm BT$, und wie ändert sich der Anteil je zusätzlichem $k_\mathrm BT$?
---
Er ist $4{,}5\cdot10^{-5}$. Je $k_\mathrm BT$ mehr Energie sinkt der Anteil um den Faktor 2,718, denn er ist $\mathrm{e}^{-W/(k_\mathrm BT)}$.
--- falsch
Er ist $4{,}5\cdot10^{-5}$. Je $k_\mathrm BT$ mehr Energie halbiert sich der Anteil, denn er ist $2^{-W/(k_\mathrm BT)}$ und fällt mit jeder Stufe auf die Hälfte.
--- falsch
Er ist $0{,}1$, also ein Zehntel. Je $k_\mathrm BT$ mehr Energie sinkt der Anteil um ein Hundertstel, denn er fällt linear mit $W/(k_\mathrm BT)$.
--- falsch
Er ist $4{,}5\cdot10^{-5}$. Je $k_\mathrm BT$ mehr Energie sinkt der Anteil um den Faktor 10, denn er ist $10^{-W/(k_\mathrm BT)}$.
:::
::::
