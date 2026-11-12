---
title: Stufe 1: Energie je Ladung mal Ladung je Zeit
pfad: Elektrotechnik / 1. Semester / ET1 – Grundgebiete der Elektrotechnik 1: Einführung in die Schaltungsanalyse / Leistung, Anpassung und Wirkungsgrad
adresse: elektrotechnik/1-semester/grundlagen-der-elektrotechnik/leistung-anpassung-und-wirkungsgrad
knoten: Kapitel 7: Leistung, Anpassung und Wirkungsgrad
order: 1170200
summary: Spannung sagt, wie viel Energie eine Ladung abgibt, Strom, wie viel Ladung vorbeikommt.
tags: 
lang: de
---

<span class="anker" id="stufe-1"></span>

:::zweck
Spannung sagt, wie viel Energie eine Ladung abgibt, Strom, wie viel Ladung vorbeikommt. Diese Stufe verbindet beides zur Energie je Zeit.
:::

**Die Idee.** Zwischen den Anschlüssen eines Bauteils liegt die Spannung $U$. Nach [Kapitel 1](/wissen/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/ladung-feld-und-potenzial/ladung-feld-und-potenzial.html) gibt jedes Coulomb, das vom höheren zum niedrigeren Potenzial gelangt, die Energie $U$ in Joule ab. Der Strom $I$ zählt, wie viele Coulomb je Sekunde durchlaufen. Je Sekunde werden also $U\cdot I$ Joule umgesetzt (Abb. [1](#abb-1)). Beide Faktoren sind nötig: Spannung ohne Strom setzt nichts um, weil keine Ladung läuft. Strom ohne Spannung setzt nichts um, weil keine Ladung etwas abgibt.

:::abbildung et1/k7ladung 1
Last mit 8 V und 0,5 A. Unten der Potenzialverlauf: Jedes Coulomb verliert 8 J. Gezeichnet sind positive Ladungen in Stromrichtung. Elektronen laufen umgekehrt, das Ergebnis ist dasselbe.
:::

:::definition Definition 1.1 (Energie und Leistung)
<span class="anker" id="satz-1-1"></span>

Läuft die Ladung $\mathrm{d} Q$ durch die Spannung $u$, gibt sie die Energie $\mathrm{d} W=u\,\mathrm{d} Q$ ab. Mit dem Strom $i=\mathrm{d} Q/\mathrm{d} t$ folgen

<span class="anker" id="gl-1-1"></span>
$$p(t)=\frac{\mathrm{d} W}{\mathrm{d} t}=u(t)\,i(t),\qquad W=\int u\,\mathrm{d} Q=\int_{t_1}^{t_2}u(t)\,i(t)\,\mathrm{d} t. \tag{1.1}$$

Für Gleichgrößen, also wenn $U$ und $I$ nicht von der Zeit abhängen, ist

<span class="anker" id="gl-1-2"></span>
$$W=U\,I\,\Delta t,\qquad P=\frac{W}{\Delta t}=U\,I. \tag{1.2}$$
:::

⁠**So liest man das:** $u$ in V, $i$ in A, $p$ in Watt: $[P]=\mathrm{V\,A}=\mathrm{J/s}=\mathrm W$. Eine Anzeige-LED setzt 20 mW um, ein Wasserkocher 2 kW, ein Kraftwerksblock 1 GW. Der Ausdruck $W/\Delta t$ ist allgemein der Mittelwert der Leistung über die Zeit $\Delta t$, $p(t)$ ihr Momentanwert. Geräte laufen oft dauerhaft, deshalb kennzeichnet man sie durch die Leistung und nicht durch die Energie. Für die Energie gilt $1\,\mathrm{W\,s}=1\,\mathrm{V\,A\,s}=1\,\mathrm{J}=1\,\mathrm{N\,m}$. Die Elektrotechnik rechnet meist in Wattsekunden oder Kilowattstunden, $1\,\mathrm{kWh}=3{,}6\,\mathrm{MJ}$. Joule ist bei Verbrennungsvorgängen üblich, Newtonmeter für mechanische Arbeit.

⁠**Vorzeichen:** Mit Verbraucher-Zählpfeilen ([Kapitel 2](/wissen/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/strom-widerstand-und-kirchhoff/strom-widerstand-und-kirchhoff.html)) heißt $p>0$: Das Bauteil nimmt Energie auf, $p<0$: Es gibt Energie ab. Mit Erzeuger-Zählpfeilen ist es umgekehrt. **Gültigkeit:** $p=u\,i$ gilt für jedes Eintor, wenn $u$ und $i$ am selben Anschlusspaar gezählt werden. Über das Innere des Bauteils wird nichts vorausgesetzt.

:::herleitung Warum nur Spannung und Strom zählen
In der Zeit $\mathrm{d} t$ tritt am Anschluss 1 die Ladung $\mathrm{d} Q=i\,\mathrm{d} t$ ein und am Anschluss 2 dieselbe Ladung aus (Knotenregel, [Kapitel 2](/wissen/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/strom-widerstand-und-kirchhoff/strom-widerstand-und-kirchhoff.html)). Das Innere bleibt unverändert. Für die Bilanz ist es so, als wäre $\mathrm{d} Q$ unmittelbar von $\varphi_1$ nach $\varphi_2$ gelangt. Nach [Kapitel 1](/wissen/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/ladung-feld-und-potenzial/ladung-feld-und-potenzial.html) ist die abgegebene Energie $\mathrm{d} W=(\varphi_1-\varphi_2)\,\mathrm{d} Q=u\,i\,\mathrm{d} t$. Division durch $\mathrm{d} t$ ergibt [(1.1)](#gl-1-1). Elektronen laufen umgekehrt und tragen negative Ladung. Beide Vorzeichen zusammen ergeben dasselbe Produkt.
:::

::::beispiel
An $R_\mathrm{L}=16\,\Omega$ liegen 8 V, es fließen 0,5 A ([Kapitel 5](/wissen/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/quellen-und-ersatzquellen/quellen-und-ersatzquellen.html)). Jedes Coulomb gibt 8 J ab, je Sekunde kommen 0,5 C: $P=4$ W. In einer Stunde sind das $W=4\,\mathrm{W}\cdot3600\,\mathrm{s}=14{,}4\,\mathrm{kJ}=4\,\mathrm{Wh}$. Einzeln gezählt laufen je Sekunde $I/e=3{,}12\cdot10^{18}$ Elektronen durch, jedes gibt $e\cdot8\,\mathrm{V}=1{,}28\cdot10^{-18}$ J ab. Das Produkt sind wieder 4 W.
::::

⁠**Grenzfälle:** An offenen Klemmen sind es 9 V und 0 A, also $P=0$. Ein idealer Draht hat $U=0$, also $P=0$ bei jedem Strom.

:::frage Wird im Bauteil Strom verbraucht?
Nein. Vor und hinter dem Bauteil fließt derselbe Strom, die Ladung kommt vollständig wieder heraus. Verbraucht wird Energie: Die Ladung läuft auf niedrigerem Potenzial weiter. Auf der Rechnung für den „Stromverbrauch“ stehen deshalb Kilowattstunden.
:::

:::aufgabe Aufgabe 1 ★ Energie und Vorzeichen
<span class="anker" id="aufg-1"></span>

(a) Ein Akku mit 3,7 V speichert die Ladung 2 Ah (2 A eine Stunde lang). Wie viel Energie ist das in Wh und in kJ? Wie lange versorgt er ein Gerät mit 0,74 W? (b) Ein Wasserkocher mit 2 kW läuft 3 Minuten. Wie viele kWh sind das, und was kosten sie bei 30 ct/kWh? (c) An einem Eintor misst man mit Verbraucher-Zählpfeilen $U=12$ V und $I=-3$ A. Nimmt es Leistung auf, oder gibt es welche ab?

:::loesung
(a) $Q=2\,\mathrm{A}\cdot3600\,\mathrm{s}=7200$ C, also $W=3{,}7\,\mathrm{V}\cdot7200\,\mathrm{C}=26{,}64$ kJ $=7{,}4$ Wh. Bei 0,74 W reicht das 10 h. (b) $W=2\,\mathrm{kW}\cdot0{,}05\,\mathrm{h}=0{,}1$ kWh, das kostet 3 ct. (c) $P=12\,\mathrm{V}\cdot(-3\,\mathrm{A})=-36$ W. Das Eintor gibt 36 W ab.
:::
:::

::::formelsammlung
**Energie und Leistung**

$$p(t)=\frac{\mathrm{d} W}{\mathrm{d} t}=u(t)\,i(t),\qquad W=\int u\,\mathrm{d} Q=\int_{t_1}^{t_2}u(t)\,i(t)\,\mathrm{d} t$$

Die Ladung $\mathrm{d} Q$ gibt beim Durchlaufen der Spannung $u$ die Energie $\mathrm{d} W=u\,\mathrm{d} Q$ ab, mit dem Strom $i=\mathrm{d} Q/\mathrm{d} t$. $p(t)$ ist der Momentanwert der Leistung. Gilt für jedes Eintor, wenn $u$ und $i$ am selben Anschlusspaar gezählt werden; über das Innere wird nichts vorausgesetzt. Mit Verbraucher-Zählpfeilen heißt $p>0$: Das Bauteil nimmt Energie auf, $p<0$: Es gibt Energie ab; mit Erzeuger-Zählpfeilen umgekehrt.

**Gleichgrößen**

$$W=U\,I\,\Delta t,\qquad P=\frac{W}{\Delta t}=U\,I$$

$U$ und $I$ hängen nicht von der Zeit ab. Allgemein ist $W/\Delta t$ der Mittelwert der Leistung über die Zeit $\Delta t$.

**Einheiten**

$$[P]=\mathrm{V\,A}=\mathrm{J/s}=\mathrm W,\qquad 1\,\mathrm{W\,s}=1\,\mathrm{V\,A\,s}=1\,\mathrm{J}=1\,\mathrm{N\,m},\qquad 1\,\mathrm{kWh}=3{,}6\,\mathrm{MJ}$$

Leistung in Watt. Energie in der Elektrotechnik meist in Wattsekunden oder Kilowattstunden.
::::

::::lernkarten
:::karte begriff Leistung
Was gibt die elektrische Leistung an, die ein Bauteil umsetzt, und wie folgt sie aus Spannung und Strom?
---
Die Energie, die je Zeit umgesetzt wird. Die Spannung gibt die Energie je Coulomb an, der Strom die Coulomb je Sekunde, ihr Produkt ist $p=u\,i$ in Watt.
--- falsch
Die Ladung, die je Zeit durch das Bauteil fließt. Sie steigt mit der Spannung und wird wie der Strom in Coulomb je Sekunde angegeben.
--- falsch
Die gesamte Energie, die ein Bauteil während seines Betriebs aufnimmt. Sie ist das Produkt aus Spannung, Strom und Betriebszeit und wird in Watt angegeben.
--- falsch
Die Energie, die eine einzelne Ladung im Bauteil abgibt. Sie ist das Produkt aus Spannung und Elementarladung und wird in Watt angegeben.
:::
:::karte formel Momentanleistung und Energie
Wie berechnet man aus den zeitabhängigen Größen $u(t)$ und $i(t)$ eines Eintors die Leistung und die Energie zwischen $t_1$ und $t_2$?
---
$p(t)=\frac{\mathrm{d} W}{\mathrm{d} t}=u(t)\,i(t)$ und $W=\int_{t_1}^{t_2}u(t)\,i(t)\,\mathrm{d} t$. Die Leistung ist der Momentanwert, die Energie ihr Zeitintegral.
--- falsch
$p(t)=u(t)\,i(t)$ und $W=p(t_2)\,(t_2-t_1)$. Die Energie folgt aus der Leistung am Ende des Zeitraums, weil sie sich bis dahin aufgebaut hat.
--- falsch
$p(t)=\frac{\mathrm{d} W}{\mathrm{d} t}=u(t)\,i(t)$ und $W=\frac{\mathrm{d} p}{\mathrm{d} t}$. Die Energie ist die Änderung der Leistung, weil sie den Zuwachs je Zeit misst.
--- falsch
$p(t)=\int_{t_1}^{t_2}u(t)\,i(t)\,\mathrm{d} t$ und $W=u(t)\,i(t)$. Die Leistung sammelt sich über die Zeit an, die Energie ist ihr Momentanwert.
:::
:::karte formel Energie und Leistung bei Gleichgrößen
Wie berechnet man Energie und Leistung, wenn Spannung $U$ und Strom $I$ während der Zeit $\Delta t$ konstant sind?
---
$W=U\,I\,\Delta t$ und $P=\frac{W}{\Delta t}=U\,I$. Allgemein ist $W/\Delta t$ der Mittelwert der Leistung über die Zeit $\Delta t$, $p(t)$ ihr Momentanwert.
--- falsch
$P=U\,I\,\Delta t$ und $W=\frac{P}{\Delta t}=U\,I$. Die Leistung wächst mit der Betriebszeit, die Energie ist der Wert, den das Gerät gerade aufnimmt.
--- falsch
$W=U\,I\,\Delta t$ und $P=\frac{W}{\Delta t}=U\,I$. Das gilt auch bei zeitabhängigen Größen, wenn man für $U$ und $I$ die Spitzenwerte einsetzt.
--- falsch
$W=\frac{U}{I}\,\Delta t$ und $P=\frac{W}{\Delta t}=\frac{U}{I}$. Die Leistung steigt mit der Spannung und sinkt mit dem Strom, der die Energie verteilt.
:::
:::karte formel Einheiten von Leistung und Energie
In welchen Einheiten gibt man Leistung und elektrische Energie an, und wie hängen diese Einheiten zusammen?
---
Leistung in Watt, $[P]=\mathrm{V\,A}=\mathrm{J/s}=\mathrm W$. Energie in $1\,\mathrm{W\,s}=1\,\mathrm{V\,A\,s}=1\,\mathrm{J}=1\,\mathrm{N\,m}$, in der Elektrotechnik meist in Wattsekunden oder Kilowattstunden, $1\,\mathrm{kWh}=3{,}6\,\mathrm{MJ}$.
--- falsch
Leistung in Watt, $[P]=\mathrm{V/A}=\mathrm{J\,s}=\mathrm W$. Energie in Wattstunden, $1\,\mathrm{Wh}=1\,\mathrm{J}$, in der Elektrotechnik meist in Kilowatt, $1\,\mathrm{kW}=3{,}6\,\mathrm{MJ}$.
--- falsch
Leistung in Kilowattstunden, $1\,\mathrm{kWh}=1000\,\mathrm{W}$. Energie in Watt, $[W]=\mathrm{V\,A}=\mathrm{J/s}$, in der Elektrotechnik meist in Joule, weil Wattsekunden unüblich sind.
--- falsch
Leistung in Watt, $[P]=\mathrm{V\,A}=\mathrm{J/s}=\mathrm W$. Energie in Joule oder Kilowattstunden, wobei $1\,\mathrm{kWh}=3{,}6\,\mathrm{kJ}$ ist, weil eine Stunde 3600 Sekunden hat.
:::
:::karte formel Vorzeichen der Leistung
Was sagt das Vorzeichen der Leistung $p=u\,i$ aus, wenn Spannung und Strom an einem Eintor mit Verbraucher-Zählpfeilen gezählt werden?
---
$p>0$ heißt: Das Bauteil nimmt Energie auf. $p<0$ heißt: Es gibt Energie ab. Mit Erzeuger-Zählpfeilen ist es umgekehrt.
--- falsch
$p>0$ heißt: Das Bauteil gibt Energie ab. $p<0$ heißt: Es nimmt Energie auf. Mit Erzeuger-Zählpfeilen gilt dieselbe Zuordnung.
--- falsch
$p<0$ kommt bei Verbraucher-Zählpfeilen nicht vor, weil Energie je Zeit nie negativ werden kann. Ein Minus deutet auf einen Messfehler hin.
--- falsch
$p>0$ heißt: Das Bauteil nimmt Energie auf. $p<0$ heißt: Es nimmt ebenfalls Energie auf, nur mit umgekehrter Stromrichtung im Inneren.
:::
:::karte zusammenhang Spannung und Strom als Faktoren
Warum setzt ein Bauteil keine Leistung um, wenn an ihm Spannung, aber kein Strom, oder Strom, aber keine Spannung liegt?
---
Spannung ohne Strom setzt nichts um, weil keine Ladung läuft. Strom ohne Spannung setzt nichts um, weil keine Ladung etwas abgibt. Beispiele sind offene Klemmen und ein idealer Draht.
--- falsch
Spannung ohne Strom setzt sehr wohl Leistung um, weil die Ladungen unter Spannung stehen. Nur Strom ohne Spannung setzt nichts um, weil dann im Bauteil kein Feld herrscht.
--- falsch
Strom ohne Spannung setzt sehr wohl Leistung um, weil die Ladungen das Bauteil durchlaufen und es erwärmen. Nur Spannung ohne Strom setzt nichts um, weil keine Ladung läuft.
--- falsch
Weil die Energie nicht von den Ladungen, sondern vom Widerstand des Bauteils abgegeben wird. Ohne Spannung oder ohne Strom ist sein Widerstand nicht festgelegt.
:::
:::karte zusammenhang Stromverbrauch
Wird in einem elektrischen Gerät Strom verbraucht, und was wird auf der Rechnung für den „Stromverbrauch“ tatsächlich abgerechnet?
---
Nein. Vor und hinter dem Gerät fließt derselbe Strom, die Ladung kommt vollständig wieder heraus, nur auf niedrigerem Potenzial. Verbraucht wird Energie, deshalb stehen Kilowattstunden auf der Rechnung.
--- falsch
Ja. Hinter dem Gerät fließt weniger Strom als davor, weil ein Teil der Ladung im Gerät bleibt und dort zu Wärme wird. Abgerechnet wird die verbrauchte Ladung, umgerechnet in Kilowattstunden.
--- falsch
Ja. Der Strom wird im Gerät aufgebraucht und fließt über den Schutzleiter ab. Abgerechnet wird deshalb die Ladung, die das Gerät insgesamt aufgenommen hat, gemessen in Amperestunden.
--- falsch
Nein, aber die Ladung kommt langsamer wieder heraus, weil sie im Gerät Bewegungsenergie abgegeben hat. Abgerechnet wird diese Bewegungsenergie der Elektronen, gemessen in Kilowatt.
:::
:::karte zusammenhang Gültigkeit für jedes Eintor
Warum gilt $p=u\,i$ für jedes Eintor, ohne dass man etwas über das Innere des Bauteils wissen muss?
---
Weil in der Zeit $\mathrm{d} t$ an einem Anschluss die Ladung $\mathrm{d} Q=i\,\mathrm{d} t$ ein- und am anderen dieselbe Ladung austritt und das Innere unverändert bleibt. Für die Bilanz ist es, als wäre $\mathrm{d} Q$ unmittelbar von $\varphi_1$ nach $\varphi_2$ gelangt.
--- falsch
Weil jedes Bauteil im Inneren ein Widerstand ist, an dem die Leistung als Wärme entsteht. Deshalb genügt es, Spannung und Strom an den Anschlüssen zu kennen, gleich in welcher Richtung und an welcher Stelle sie gezählt werden.
--- falsch
Weil man $u$ und $i$ beliebig an verschiedenen Stellen der Schaltung messen darf. Die Leistung hängt nur von den Beträgen der beiden Größen ab, nicht davon, wo sie gezählt werden.
--- falsch
Sie gilt nur für Bauteile, deren Inneres bekannt ist, weil man sonst nicht weiß, ob die Ladung innen Energie speichert. Bei unbekanntem Inneren bilanziert man die Energie einzeln.
:::
:::karte zusammenhang Leistung als Kennzeichen von Geräten
Warum kennzeichnet man elektrische Geräte meist durch ihre Leistung und nicht durch die Energie, die sie aufnehmen?
---
Weil Geräte oft dauerhaft laufen. Die aufgenommene Energie wächst mit der Betriebszeit, die Leistung als Energie je Zeit beschreibt dagegen das Gerät selbst.
--- falsch
Weil die Energie eines Geräts nicht messbar ist, solange es läuft. Erst nach dem Abschalten lässt sich aus der Leistung zurückrechnen, wie viel es aufgenommen hat.
--- falsch
Weil Leistung und Energie dieselbe Größe sind und Watt nur die kürzere Einheit ist. Die Angabe in Joule wäre gleichwertig, aber deutlich unübersichtlicher.
--- falsch
Weil die Leistung angibt, wie viel Ladung das Gerät je Sekunde verbraucht. Diese Angabe braucht man, um die passende Sicherung für das Gerät zu wählen.
:::
:::karte herleitung Leistung eines Eintors
Leite aus der Energie, die eine Ladung beim Wechsel von $\varphi_1$ nach $\varphi_2$ abgibt, die Leistung $p=u\,i$ eines Eintors her.
---
In der Zeit $\mathrm{d} t$ tritt am Anschluss 1 die Ladung $\mathrm{d} Q=i\,\mathrm{d} t$ ein und am Anschluss 2 dieselbe Ladung aus, weil nach der Knotenregel keine Ladung im Bauteil bleibt.
---
Für die Bilanz ist es so, als wäre $\mathrm{d} Q$ unmittelbar von $\varphi_1$ nach $\varphi_2$ gelangt, weil das Innere unverändert bleibt.
---
Die abgegebene Energie ist $\mathrm{d} W=(\varphi_1-\varphi_2)\,\mathrm{d} Q=u\,i\,\mathrm{d} t$, weil jedes Coulomb beim Potenzialwechsel die Potenzialdifferenz in Joule abgibt.
---
Division durch $\mathrm{d} t$ ergibt $p(t)=\frac{\mathrm{d} W}{\mathrm{d} t}=u(t)\,i(t)$, weil Leistung Energie je Zeit ist.
---
Für Elektronen gilt dasselbe, weil sie umgekehrt laufen und negative Ladung tragen; beide Vorzeichen zusammen ergeben dasselbe Produkt.
:::
::::
