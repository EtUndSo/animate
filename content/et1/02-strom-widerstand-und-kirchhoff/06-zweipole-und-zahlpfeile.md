---
title: Stufe 5: Zweipole und Zählpfeile
pfad: Elektrotechnik / 1. Semester / ET1 – Grundgebiete der Elektrotechnik 1: Einführung in die Schaltungsanalyse / Strom, Widerstand und Kirchhoff
adresse: elektrotechnik/1-semester/grundlagen-der-elektrotechnik/strom-widerstand-und-kirchhoff
knoten: Kapitel 2: Strom, Widerstand und Kirchhoff
order: 1120600
summary: Ab jetzt zählt nicht mehr, was im Bauteil geschieht, sondern was an seinen Anschlüssen messbar ist.
tags: Zweipol, Kennlinie, Blackbox, Netzwerk, linearer Zweipol, nichtlinearen Zweipol, Verbraucherzählpfeilsystem, Erzeuger- oder Generatorzählpfeilsystem
lang: de
---

<span class="anker" id="stufe-5"></span>

:::zweck
Ab jetzt zählt nicht mehr, was im Bauteil geschieht, sondern was an seinen Anschlüssen messbar ist. Dazu braucht man einen Begriff für das Bauteil und eine Vereinbarung über Vorzeichen.
:::

**Die Idee.** Zum Rechnen genügt, wie ein Bauteil auf Spannung mit Strom antwortet. Das Innere darf unbekannt sein. Vorzeichen legt man vorab mit Pfeilen fest, denn vor der Rechnung kennt man die wahren Richtungen oft nicht. Das Ergebnis sagt dann, ob die Wirklichkeit dem Pfeil folgt.

:::definition Definition 5.1 (Zweipol, Blackbox, Netzwerk)
<span class="anker" id="satz-5-1"></span>

Ein __Zweipol__ ist ein Bauelement, das sich durch Strom und Spannung zwischen seinen zwei Anschlussklemmen vollständig beschreiben lässt. Stationär (zeitunabhängig) ist das seine __Kennlinie__ $I=f(U)$. Eine __Blackbox__ ist ein System, dessen Verhalten nach außen bekannt ist, dessen Aufbau aber unbekannt oder unwichtig ist. Ein __Netzwerk__ ist eine Zusammenschaltung von Zweipolen. Ist die Kennlinie eine Gerade durch den Ursprung, gilt

<span class="anker" id="gl-5-1"></span>
$$G=\frac IU=\text{const}\quad\text{bzw.}\quad R=\frac UI=\text{const}. \tag{5.1}$$
:::

⁠**So liest man das:** Ein solcher __linearer Zweipol__ ist der ohmsche Widerstand (Abb. [4](das-ohmsche-gesetz-aus-feld-und-stoen.html#abb-4) rechts, jede Gerade ein Wert). Auch Batterie und Spannungsquelle gehören zu den Bausteinen linearer Netze, ihre Kennlinie läuft aber nicht durch den Ursprung ([Kapitel 5](/wissen/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/quellen-und-ersatzquellen/quellen-und-ersatzquellen.html)). Bei einem __nichtlinearen Zweipol__ wie der Glühlampe (Abb. [5](reale-widerstande-werte-und-temperatur.html#abb-5) rechts) hängt $U/I$ vom Arbeitspunkt ab, dort gilt [(5.1)](#gl-5-1) nicht.

:::definition Definition 5.2 (Zählpfeilsysteme)
<span class="anker" id="satz-5-2"></span>

Der Spannungspfeil zeigt von 1 nach 2 und meint $U_{12}=\varphi_1-\varphi_2$ ([Kapitel 1](/wissen/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/ladung-feld-und-potenzial/ladung-feld-und-potenzial.html)). Der Strompfeil zählt positive Ladung in Pfeilrichtung. Beim __Verbraucherzählpfeilsystem__ (VZS) zeigen Spannungs- und Strompfeil an einem Zweipol in dieselbe Richtung, beim __Erzeuger- oder Generatorzählpfeilsystem__ (GZS) in entgegengesetzte. Für einen Widerstand gilt

<span class="anker" id="gl-5-2"></span>
$$U=R\,I\quad\text{(VZS)},\qquad U=-R\,I\quad\text{(GZS)}. \tag{5.2}$$
:::

⁠**So liest man das:** Beide Systeme sind nur Vereinbarungen. Die Richtung beider Pfeile ist frei wählbar, das ändert Vorzeichen, nie die Physik. Üblich sind VZS am Verbraucher und GZS an der Quelle, denn dann sind im Normalbetrieb alle Zahlen positiv (Abb. [6](#abb-6) links). **Warum das passt:** Im Verbraucher läuft positive Ladung vom hohen zum tiefen Potenzial und gibt Energie ab, Strom und Spannung sind gleichsinnig. In der Quelle wird sie vom tiefen zum hohen Potenzial gehoben, Strom und Spannung sind gegensinnig. Im VZS bedeutet $U\,I>0$ deshalb Aufnahme von Energie, im GZS Abgabe.

Die __technische Stromrichtung__ ist die Richtung, in der positive Ladung liefe: außerhalb der Quelle von Plus nach Minus. Sie entspricht dem Strompfeil am Verbraucher im VZS. Die Elektronen laufen entgegengesetzt.

:::abbildung et1/k2zaehlpfeil 6
Links: Kette aus Quelle und $3\,\mathrm{k\Omega}$ mit den üblichen Pfeilen. An der Quelle gegensinnig (GZS), am Widerstand gleichsinnig (VZS), alle Werte positiv. Die Elektronen laufen gegen den Strompfeil. Rechts: Derselbe Widerstand, einmal mit gedrehtem Spannungspfeil. Es ändert sich nur das Vorzeichen.
:::

::::beispiel
9 V an $3\,\mathrm{k\Omega}$ ergeben $I=3$ mA. Zeigt der Spannungspfeil von unten nach oben, ist $U=\varphi_\text{unten}-\varphi_\text{oben}=-9$ V, und [(5.2)](#gl-5-2) lautet $-9\,\mathrm{V}=-3\,\mathrm{k\Omega}\cdot3\,\mathrm{mA}$. **Kontrolle:** Dreht man beide Pfeile, wird aus $U=R\,I$ die Gleichung $-U=R\,(-I)$, also wieder dieselbe.
::::

:::frage Elektronen laufen von Minus nach Plus. Warum rechnet man andersherum?
Die Richtung wurde festgelegt, bevor man Elektronen kannte, und sie schadet nicht: In $\vec j=q\,\vec v$ ändern bei den Elektronen beide Faktoren das Vorzeichen. Elektronen nach links ergeben dieselbe Stromdichte wie positive Ladung nach rechts. Spannungsabfall, Wärme und Magnetfeld hängen nur von $\vec j$ ab.
:::

:::aufgabe Aufgabe 5 ★ Vorzeichen deuten
<span class="anker" id="aufg-5"></span>

<ol class="al">

<li>

Eine Blackbox im VZS zeigt $U=5$ V und $I=-2$ mA. Nimmt sie Energie auf oder gibt sie ab, und wie viel je Sekunde?

</li>

<li>

Eine Autobatterie im GZS zeigt $U=14$ V und $I=-10$ A. Was geschieht mit ihr?

</li>

<li>

In einem Draht laufen Elektronen nach rechts, der Betrag des Stroms ist 2 mA. Der Strompfeil zeigt nach rechts. Wie groß ist $I$?

</li>

</ol>

:::loesung
(a) $U\,I=-10$ mW im VZS: Die Box gibt 10 mW ab, sie arbeitet als Quelle. (b) $U\,I=-140$ W im GZS: Sie gibt nicht ab, sondern nimmt 140 W auf. Sie wird geladen. (c) Der Strom im Sinn positiver Ladung läuft nach links, also $I=-2$ mA.
:::
:::

::::formelsammlung
**Kennlinie eines Zweipols**

$$I=f(U)$$

Stationärer Zusammenhang zwischen Strom und Spannung an den zwei Anschlussklemmen.

**Linearer Zweipol**

$$G=\frac IU=\text{const}\quad\text{bzw.}\quad R=\frac UI=\text{const}$$

Die Kennlinie ist eine Gerade durch den Ursprung, etwa beim ohmschen Widerstand. Beim nichtlinearen Zweipol (Glühlampe) hängt $U/I$ vom Arbeitspunkt ab.

**Spannungspfeil**

$$U_{12}=\varphi_1-\varphi_2$$

Der Spannungspfeil zeigt von 1 nach 2; der Strompfeil zählt positive Ladung in Pfeilrichtung. Beide Richtungen sind frei wählbar: Das ändert Vorzeichen, nie die Physik.

**Widerstand im VZS und im GZS**

$$U=R\,I\quad\text{(VZS)},\qquad U=-R\,I\quad\text{(GZS)}$$

VZS: Spannungs- und Strompfeil gleichsinnig, üblich am Verbraucher; GZS: gegensinnig, üblich an der Quelle. So sind im Normalbetrieb alle Zahlen positiv.

**Vorzeichen der Leistung**

$$U\,I>0$$

Im VZS bedeutet das Aufnahme von Energie, im GZS Abgabe. Die technische Stromrichtung läuft außerhalb der Quelle von Plus nach Minus, die Elektronen laufen entgegengesetzt.
::::

::::lernkarten
:::karte begriff Zweipol
Was ist ein Zweipol, wie man ihn zur Berechnung von Schaltungen verwendet?
---
Ein Bauelement, das sich durch Strom und Spannung zwischen seinen zwei Anschlussklemmen vollständig beschreiben lässt. Sein Inneres darf unbekannt sein.
--- falsch
Ein Bauelement mit einem Plus- und einem Minuspol, das selbst Energie liefert, etwa eine Batterie. Widerstände zählen nicht dazu.
--- falsch
Ein Bauelement, das sich durch seinen inneren Aufbau aus genau zwei Materialien vollständig beschreiben lässt. Strom und Spannung an den Klemmen folgen daraus.
--- falsch
Eine Verbindung zweier Knoten über einen Draht ohne Bauteil. Zwischen ihren beiden Enden liegt deshalb keine Spannung.
:::
:::karte begriff Kennlinie
Was beschreibt die Kennlinie eines Zweipols im stationären Fall?
---
Den Zusammenhang $I=f(U)$ zwischen Strom und Spannung an seinen Klemmen. Für den ohmschen Widerstand ist sie eine Gerade durch den Ursprung.
--- falsch
Den zeitlichen Verlauf des Stroms nach dem Einschalten, $I=f(t)$. Für den ohmschen Widerstand ist sie eine waagerechte Gerade.
--- falsch
Den Zusammenhang $R=f(\vartheta)$ zwischen Widerstand und Temperatur. Für den ohmschen Widerstand ist sie eine Gerade durch den Ursprung.
--- falsch
Den Verlauf des Potenzials längs des Bauteils von einer Klemme zur anderen. Für den ohmschen Widerstand fällt es gleichmäßig von Klemme zu Klemme ab.
:::
:::karte begriff Blackbox und Netzwerk
Was bedeuten die Begriffe Blackbox und Netzwerk bei der Berechnung von Schaltungen?
---
Eine Blackbox ist ein System, dessen Verhalten nach außen bekannt ist, dessen Aufbau aber unbekannt oder unwichtig ist. Ein Netzwerk ist eine Zusammenschaltung von Zweipolen.
--- falsch
Eine Blackbox ist ein Bauteil, dessen Werte man nicht messen kann, weil es versiegelt ist. Ein Netzwerk ist die Verbindung mehrerer Rechner und Geräte über Datenkabel oder Funk.
--- falsch
Eine Blackbox ist ein System, dessen Aufbau bekannt ist, dessen Verhalten nach außen aber erst gemessen werden muss. Ein Netzwerk ist eine Zusammenschaltung von Zweipolen.
--- falsch
Eine Blackbox ist ein System, dessen Verhalten nach außen bekannt ist. Ein Netzwerk ist eine Zusammenschaltung von Quellen, Widerstände gehören nicht dazu.
:::
:::karte begriff linearer Zweipol
Wann heißt ein Zweipol linear, und welches Bauteil ist ein Beispiel dafür?
---
Wenn seine Kennlinie eine Gerade durch den Ursprung ist, also $R=\frac UI=\text{const}$. Beispiel: der ohmsche Widerstand.
--- falsch
Wenn seine Kennlinie irgendeine Gerade ist, auch eine, die nicht durch den Ursprung läuft. Beispiel: die Glühlampe.
--- falsch
Wenn sein Strom nach dem Einschalten mit der Zeit gleichmäßig wächst. Beispiel: der ohmsche Widerstand.
--- falsch
Wenn $U/I$ vom Arbeitspunkt abhängt, aber stetig ist. Beispiel: die Glühlampe, deren Widerstand mit dem Strom gleichmäßig steigt.
:::
:::karte begriff nichtlinearer Zweipol
Was kennzeichnet einen nichtlinearen Zweipol wie die Glühlampe?
---
Seine Kennlinie ist keine Gerade durch den Ursprung: Der Quotient $U/I$ hängt vom Arbeitspunkt ab, $R=\frac UI=\text{const}$ gilt nicht.
--- falsch
Er hat mehr als zwei Anschlüsse, deshalb lässt er sich nicht durch eine einzige Kennlinie $I=f(U)$ zwischen zwei Klemmen beschreiben.
--- falsch
Seine Kennlinie ist eine Gerade, die nicht durch den Ursprung läuft. Der Quotient $U/I$ ist trotzdem konstant.
--- falsch
Bei ihm lässt sich der Quotient $U/I$ nicht bilden, weil Strom und Spannung nicht gleichzeitig messbar sind.
:::
:::karte formel Spannungspfeil und Strompfeil
Welche Spannung meint ein Spannungspfeil von Punkt 1 nach Punkt 2, und was zählt ein Strompfeil?
---
$U_{12}=\varphi_1-\varphi_2$, das Potenzial am Pfeilanfang minus das am Pfeilende. Der Strompfeil zählt positive Ladung in Pfeilrichtung.
--- falsch
$U_{12}=\varphi_2-\varphi_1$, das Potenzial am Pfeilende minus das am Pfeilanfang. Der Strompfeil zählt Elektronen in Pfeilrichtung.
--- falsch
$U_{12}=\varphi_1+\varphi_2$, die Summe der Potenziale beider Punkte. Der Strompfeil zählt positive Ladung in Pfeilrichtung.
--- falsch
$U_{12}=\varphi_1-\varphi_2$, das Potenzial am Pfeilanfang minus das am Pfeilende. Der Strompfeil zeigt immer vom Plus- zum Minuspol der Quelle.
:::
:::karte begriff Verbraucherzählpfeilsystem
Wie liegen Spannungs- und Strompfeil an einem Zweipol im Verbraucherzählpfeilsystem (VZS), und was bedeutet dort $U\,I>0$?
---
In dieselbe Richtung, gleichsinnig. Am Widerstand gilt dann $U=R\,I$, und $U\,I>0$ bedeutet Aufnahme von Energie.
--- falsch
In entgegengesetzte Richtungen, gegensinnig. Am Widerstand gilt dann $U=R\,I$, und $U\,I>0$ bedeutet Aufnahme von Energie.
--- falsch
In dieselbe Richtung, gleichsinnig. Am Widerstand gilt dann $U=-R\,I$, und $U\,I>0$ bedeutet Abgabe von Energie.
--- falsch
Der Strompfeil zeigt in Laufrichtung der Elektronen, der Spannungspfeil zum Minuspol. $U\,I>0$ bedeutet Abgabe von Energie.
:::
:::karte begriff Erzeuger- oder Generatorzählpfeilsystem
Wie liegen Spannungs- und Strompfeil im Erzeuger- oder Generatorzählpfeilsystem (GZS), und wo verwendet man es üblicherweise?
---
In entgegengesetzte Richtungen, gegensinnig. Man verwendet es an der Quelle; dort bedeutet $U\,I>0$ Abgabe von Energie. Am Widerstand lautete das ohmsche Gesetz $U=-R\,I$.
--- falsch
In dieselbe Richtung, gleichsinnig. Man verwendet es an der Quelle; dort bedeutet $U\,I>0$ Abgabe von Energie. Am Widerstand gilt wie gewohnt $U=R\,I$.
--- falsch
In entgegengesetzte Richtungen, gegensinnig. Man verwendet es am Verbraucher; dort bedeutet $U\,I>0$ Aufnahme von Energie, und am Widerstand gilt $U=R\,I$.
--- falsch
Beide Pfeile zeigen vom Minus- zum Pluspol der Quelle. Man verwendet es nur an Batterien; dort ist $U\,I$ immer negativ, solange die Batterie Energie an den Kreis liefert.
:::
:::karte begriff technische Stromrichtung
Wie ist die technische Stromrichtung festgelegt, und wie laufen die Elektronen dazu?
---
Als die Richtung, in der positive Ladung liefe: außerhalb der Quelle von Plus nach Minus. Die Elektronen laufen entgegengesetzt.
--- falsch
Als die Richtung, in der die Elektronen laufen: außerhalb der Quelle von Minus nach Plus. Positive Ladung bewegt sich in Metallen nicht.
--- falsch
Als die Richtung, in der positive Ladung liefe: außerhalb der Quelle von Minus nach Plus. Die Elektronen laufen in dieselbe Richtung.
--- falsch
Als die Richtung, in die man den Strompfeil an der Quelle zeichnet, gleich wie man ihn wählt. Die Elektronen laufen in dieselbe Richtung.
:::
:::karte zusammenhang Elektronen gegen den Strompfeil
Warum darf man mit der technischen Stromrichtung rechnen, obwohl die Elektronen entgegengesetzt laufen?
---
Weil in $\vec j=q\,\vec v$ bei Elektronen beide Faktoren das Vorzeichen wechseln: Elektronen nach links wirken wie positive Ladung nach rechts. Spannungsabfall, Wärme und Magnetfeld hängen nur von $\vec j$ ab.
--- falsch
Weil der Fehler klein ist: Elektronen tragen nur einen kleinen Teil des Stroms, den größeren Teil tragen die positiven Ionen des Gitters, die in Pfeilrichtung durch den Draht wandern.
--- falsch
Weil man am Ende jedes Ergebnis mit $-1$ multipliziert. Erst diese Korrektur liefert die wirklichen Spannungen und Ströme und die richtige Wärme.
--- falsch
Weil die Richtung bei einem stationären Strom keine Rolle spielt. Ein zeitlich konstanter Strom hat keine Richtung, deshalb sind seine Vorzeichen frei wählbar und für die Rechnung ohne jede Bedeutung.
:::
:::karte zusammenhang Wahl der Zählpfeilsysteme
Warum wählt man am Verbraucher das VZS und an der Quelle das GZS?
---
Weil dann im Normalbetrieb alle Zahlen positiv sind: Im Verbraucher läuft positive Ladung vom hohen zum tiefen Potenzial, in der Quelle wird sie vom tiefen zum hohen gehoben.
--- falsch
Weil nur so die Rechnung richtig wird: Mit vertauschten Systemen ergäben sich falsche Beträge der Ströme und Spannungen, und die Energiebilanz ginge nicht auf.
--- falsch
Weil die Elektronen im Verbraucher in Pfeilrichtung laufen und in der Quelle gegen sie. Die Pfeile folgen so immer der Bewegung der Elektronen.
--- falsch
Weil die Quelle Ladung erzeugt und der Verbraucher sie aufnimmt. Die Pfeile zeigen deshalb an beiden Bauteilen zu der Stelle, an der die Ladung am Ende verschwindet.
:::
:::karte zusammenhang Negatives Ergebnis
Was bedeutet ein negatives Ergebnis für einen Strom, dessen Pfeil man vor der Rechnung frei gewählt hat?
---
Dass der wirkliche Strom gegen den Pfeil fließt. Die Pfeilwahl legt nur das Vorzeichen fest, nie die Physik.
--- falsch
Dass die Rechnung falsch ist: Ströme sind Beträge und können nicht negativ sein. Man muss den Pfeil umdrehen und neu rechnen.
--- falsch
Dass das Bauteil Energie abgibt, gleich welches Zählpfeilsystem gilt und welches Vorzeichen die Spannung hat.
--- falsch
Dass der Strom von Elektronen getragen wird statt von positiver Ladung. Seine Richtung ist dieselbe wie die des Pfeils.
:::
::::
