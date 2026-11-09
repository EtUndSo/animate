---
title: Stufe 5: Zweipole und Zählpfeile
pfad: Elektrotechnik / 1. Semester / Grundlagen der Elektrotechnik / Strom, Widerstand und Kirchhoff
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

⁠**So liest man das:** Ein solcher __linearer Zweipol__ ist der ohmsche Widerstand (Abb. [4](das-ohmsche-gesetz-aus-feld-und-stoen.html#abb-4) rechts, jede Gerade ein Wert). Auch Batterie und Spannungsquelle gehören zu den Bausteinen linearer Netze, ihre Kennlinie läuft aber nicht durch den Ursprung ([Teil 5](/wissen/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/quellen-und-ersatzquellen/quellen-und-ersatzquellen.html)). Bei einem __nichtlinearen Zweipol__ wie der Glühlampe (Abb. [5](reale-widerstande-werte-und-temperatur.html#abb-5) rechts) hängt $U/I$ vom Arbeitspunkt ab, dort gilt [(5.1)](#gl-5-1) nicht.

:::definition Definition 5.2 (Zählpfeilsysteme)
<span class="anker" id="satz-5-2"></span>

Der Spannungspfeil zeigt von 1 nach 2 und meint $U_{12}=\varphi_1-\varphi_2$ ([Teil 1](/wissen/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/ladung-feld-und-potenzial/ladung-feld-und-potenzial.html)). Der Strompfeil zählt positive Ladung in Pfeilrichtung. Beim __Verbraucherzählpfeilsystem__ (VZS) zeigen Spannungs- und Strompfeil an einem Zweipol in dieselbe Richtung, beim __Erzeuger- oder Generatorzählpfeilsystem__ (GZS) in entgegengesetzte. Für einen Widerstand gilt

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
