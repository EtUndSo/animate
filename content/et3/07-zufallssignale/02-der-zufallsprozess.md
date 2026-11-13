---
title: Stufe 1: Der Zufallsprozess
pfad: Elektrotechnik / 3. Semester / ET3 – Grundgebiete der Elektrotechnik 3: Signale und Systeme / Zufallssignale
adresse: elektrotechnik/3-semester/signale-und-systeme/zufallssignale
knoten: Kapitel 7: Zufallssignale
order: 3270200
summary: Wie beschreibt man ein Signal, dessen Verlauf man nicht kennt?
tags: Musterfunktion, Zufallsprozess, Zufallsgröße, Erwartungswert, Autokorrelationsfunktion
lang: de
---

<span class="anker" id="stufe-1"></span>

:::zweck
Wie beschreibt man ein Signal, dessen Verlauf man nicht kennt? Man stellt sich viele gleichartige Signale vor und mittelt über sie.
:::

**Die Idee.** Misst man das Rauschen an vielen gleich gebauten Widerständen bei gleicher Temperatur, bekommt man viele verschiedene Kurven ${}^ks(t)$, $k=1,2,\dots$ (Abb. [1](#abb-1)). Jede einzelne heißt __Musterfunktion__ oder Realisierung. Die gedachte Gesamtheit aller heißt __Zufallsprozess__ $s(t)$. Die Werte aller Musterfunktionen zu einem festen Zeitpunkt $t_1$ bilden eine __Zufallsgröße__ $s(t_1)$.

:::definition Definition 1.1 (Scharmittelwerte)
<span class="anker" id="satz-1-1"></span>

<span class="anker" id="gl-1-1"></span>
<span class="anker" id="gl-1-2"></span>
$$\begin{aligned} \mathrm E\{s(t_1)\}&=\lim_{M\to\infty}\frac1M\sum_{k=1}^M{}^ks(t_1),\qquad \mathrm E\{F[s(t_1)]\}=\lim_{M\to\infty}\frac1M\sum_{k=1}^MF\bigl[{}^ks(t_1)\bigr],\\ \varphi_{ss}(t_1,t_2)&=\mathrm E\{s(t_1)\,s(t_2)\}. \end{aligned} \tag{1.1|1.2}$$
:::

⁠**So liest man das:** $\mathrm E\{\cdot\}$ heißt __Erwartungswert__ oder Scharmittelwert: Man mittelt über alle Musterfunktionen zum selben Zeitpunkt, also senkrecht in Abb. [1](#abb-1). Mit $F[x]=x^2$ erhält man den quadratischen Mittelwert. Die __Autokorrelationsfunktion__ mittelt das Produkt der Werte zu zwei Zeitpunkten. Sie sagt, wie stark der Wert bei $t_2$ mit dem bei $t_1$ zusammenhängt.

:::abbildung et3/k7schar 1
Drei Musterfunktionen eines Zufallsprozesses (simuliert, Mittelwert 1). Das Scharmittel bildet man senkrecht, über alle Musterfunktionen bei demselben $t_1$ (rot gestrichelt). Das Zeitmittel bildet man waagerecht, entlang einer Musterfunktion.
:::

::::formelsammlung
**Erwartungswert (Scharmittelwert)**

$$\mathrm E\{s(t_1)\}=\lim_{M\to\infty}\frac1M\sum_{k=1}^M{}^ks(t_1)$$

Mittel über alle Musterfunktionen ${}^ks(t)$ des Zufallsprozesses zum selben Zeitpunkt $t_1$; die Werte bei $t_1$ bilden die Zufallsgröße $s(t_1)$.

**Scharmittel einer Funktion**

$$\mathrm E\{F[s(t_1)]\}=\lim_{M\to\infty}\frac1M\sum_{k=1}^MF\bigl[{}^ks(t_1)\bigr]$$

$F$ wird auf jeden Wert angewandt, dann wird gemittelt. Mit $F[x]=x^2$ der quadratische Mittelwert.

**Autokorrelationsfunktion**

$$\varphi_{ss}(t_1,t_2)=\mathrm E\{s(t_1)\,s(t_2)\}$$

Mittel des Produkts der Werte zu zwei Zeitpunkten: wie stark der Wert bei $t_2$ mit dem bei $t_1$ zusammenhängt.
::::

::::lernkarten
:::karte zusammenhang Beschreibung durch Mittelwerte
Warum stellt man sich zur Beschreibung eines Rauschsignals viele gleichartige Signale vor, statt nur das eine gemessene Signal zu betrachten?
---
Weil man den genauen Verlauf eines Zufallssignals nicht vorhersagen kann, wohl aber seine Eigenschaften im Mittel. Diese Mittelwerte bildet man über die Schar aller gleichartigen Signale.
--- falsch
Weil ein einzelnes gemessenes Signal zu wenig Leistung hat, um es sinnvoll auszuwerten. Erst viele gleichartige Signale zusammen ergeben eine Leistung, die ein Messgerät zuverlässig erfassen kann.
--- falsch
Weil sich die vielen Signale beim Addieren gegenseitig auslöschen und nur der vorhersagbare Anteil übrig bleibt. Aus dieser Summe berechnet man dann den genauen Verlauf jedes einzelnen Signals.
--- falsch
Weil das gemessene Signal durch die Messung verfälscht ist. Erst der Vergleich mit vielen anderen Messungen zeigt, welcher Teil der Kurve echt ist und welcher nur vom Messgerät selbst stammt.
:::
:::karte begriff Musterfunktion
Was bezeichnet man bei einem Zufallsprozess als Musterfunktion, etwa beim Rauschen vieler gleich gebauter Widerstände?
---
Eine einzelne der vielen möglichen Kurven ${}^ks(t)$, zum Beispiel das Rauschen, das an einem bestimmten Widerstand gemessen wird. Man nennt sie auch Realisierung des Prozesses.
--- falsch
Den Mittelwert aller Kurven ${}^ks(t)$ zu jedem Zeitpunkt, also die glatte Kurve, um die das Rauschen aller gleich gebauten Widerstände schwankt. Man nennt sie auch Erwartungskurve.
--- falsch
Eine Formel, aus der man das Rauschen jedes einzelnen Widerstands im Voraus berechnen kann. Sie enthält alle Bauteilwerte und liefert den genauen Verlauf zu jedem Zeitpunkt.
--- falsch
Die Gesamtheit aller Werte, die die Kurven ${}^ks(t)$ zu einem festen Zeitpunkt annehmen. Über diese Werte bildet man die Scharmittelwerte des Prozesses.
:::
:::karte begriff Zufallsprozess
Was versteht man unter dem Zufallsprozess $s(t)$, mit dem man ein Signal mit unbekanntem Verlauf beschreibt?
---
Die gedachte Gesamtheit aller Musterfunktionen ${}^ks(t)$, $k=1,2,\dots$, die unter gleichen Bedingungen entstehen können, etwa das Rauschen aller gleich gebauten Widerstände bei gleicher Temperatur.
--- falsch
Ein einzelnes, sehr lange gemessenes Rauschsignal, dessen Verlauf man vollständig aufzeichnet. Erst wenn die Messung unendlich lange dauert, wird aus diesem Signal ein Zufallsprozess.
--- falsch
Ein Rechenverfahren, das aus einem bekannten Signal durch Würfeln immer neue Signale erzeugt, etwa beim Simulieren von Rauschen. Der Zufallsprozess ist also eine Vorschrift, kein Signal.
--- falsch
Die Werte aller Musterfunktionen zu einem festen Zeitpunkt $t_1$. Der Zufallsprozess ist damit eine einzelne Zahl, die sich von Messung zu Messung zufällig ändert.
:::
:::karte begriff Zufallsgröße
Was ist die Zufallsgröße $s(t_1)$ eines Zufallsprozesses zu einem festen Zeitpunkt $t_1$?
---
Die Gesamtheit der Werte, die alle Musterfunktionen zum festen Zeitpunkt $t_1$ annehmen. Über sie bildet man die Scharmittelwerte, etwa den Erwartungswert $\mathrm E\{s(t_1)\}$.
--- falsch
Der Mittelwert einer einzigen Musterfunktion über alle Zeiten bis $t_1$. Er fasst den bisherigen Verlauf dieser Musterfunktion in einer einzigen Zahl zusammen.
--- falsch
Der Verlauf einer einzelnen Musterfunktion in der Umgebung von $t_1$. Aus diesem Ausschnitt bestimmt man, wie schnell sich das Signal zum Zeitpunkt $t_1$ ändert.
--- falsch
Der Erwartungswert $\mathrm E\{s(t_1)\}$ des Prozesses zum Zeitpunkt $t_1$, also eine feste Zahl. Sie ist für alle Musterfunktionen gleich und deshalb nicht mehr zufällig.
:::
:::karte begriff Erwartungswert
Was gibt der Erwartungswert $\mathrm E\{s(t_1)\}$ eines Zufallsprozesses an, und wie wird er gebildet?
---
Den Scharmittelwert zum Zeitpunkt $t_1$: den Mittelwert über alle Musterfunktionen zum selben Zeitpunkt, $\mathrm E\{s(t_1)\}=\lim_{M\to\infty}\frac1M\sum_{k=1}^M{}^ks(t_1)$.
--- falsch
Den Zeitmittelwert einer einzigen Musterfunktion: den Mittelwert ihrer Werte bis zum Zeitpunkt $t_1$, also $\mathrm E\{s(t_1)\}=\frac{1}{t_1}\int_0^{t_1}{}^1s(t)\,\mathrm{d} t$.
--- falsch
Den häufigsten Wert zum Zeitpunkt $t_1$: den Wert, den die meisten Musterfunktionen bei $t_1$ annehmen, also den Wert, der am wahrscheinlichsten auftritt.
--- falsch
Den Scharmittelwert zum Zeitpunkt $t_1$, gebildet über die Quadrate, $\mathrm E\{s(t_1)\}=\lim_{M\to\infty}\frac1M\sum_{k=1}^M{}^ks^2(t_1)$, damit sich positive und negative Werte nicht aufheben.
:::
:::karte formel Scharmittel einer Funktion
Wie bildet man den Scharmittelwert einer Funktion $F$ der Signalwerte, und was erhält man mit $F[x]=x^2$?
---
$\mathrm E\{F[s(t_1)]\}=\lim_{M\to\infty}\frac1M\sum_{k=1}^MF\bigl[{}^ks(t_1)\bigr]$: Man wendet $F$ auf den Wert jeder Musterfunktion bei $t_1$ an und mittelt dann. Mit $F[x]=x^2$ erhält man den quadratischen Mittelwert.
--- falsch
$\mathrm E\{F[s(t_1)]\}=F\bigl[\mathrm E\{s(t_1)\}\bigr]$: Man mittelt zuerst über alle Musterfunktionen und wendet $F$ dann auf den Mittelwert an. Mit $F[x]=x^2$ erhält man das Quadrat des Mittelwerts.
--- falsch
$\mathrm E\{F[s(t_1)]\}=\lim_{M\to\infty}\sum_{k=1}^MF\bigl[{}^ks(t_1)\bigr]$: Man wendet $F$ auf jede Musterfunktion an und summiert, ohne durch $M$ zu teilen. Mit $F[x]=x^2$ erhält man die Energie der Schar.
--- falsch
$\mathrm E\{F[s(t_1)]\}=\lim_{T\to\infty}\frac{1}{2T}\int_{-T}^{T}F\bigl[{}^1s(t)\bigr]\,\mathrm{d} t$: Man wendet $F$ auf eine Musterfunktion an und mittelt über die Zeit. Mit $F[x]=x^2$ erhält man den Effektivwert.
:::
:::karte zusammenhang Autokorrelationsfunktion
Warum mittelt die Autokorrelationsfunktion $\varphi_{ss}(t_1,t_2)$ eines Zufallsprozesses das Produkt der Werte zu zwei Zeitpunkten?
---
Weil sie angeben soll, wie stark der Wert bei $t_2$ mit dem bei $t_1$ zusammenhängt. Dazu mittelt man über die Schar das Produkt beider Werte: $\varphi_{ss}(t_1,t_2)=\mathrm E\{s(t_1)\,s(t_2)\}$.
--- falsch
Weil sie die Leistung des Prozesses angeben soll. Das Produkt der Werte zu zwei beliebigen Zeitpunkten ist bei jedem Prozess gleich dem Quadrat des Signals, also gleich seiner Leistung.
--- falsch
Weil man aus dem Produkt zweier Werte den genauen Verlauf zwischen $t_1$ und $t_2$ berechnen kann. Die AKF ersetzt so die unbekannte Musterfunktion durch eine vorhersagbare Kurve.
--- falsch
Weil ein Produkt immer positiv ist und sich die Werte beim Mitteln deshalb nicht aufheben. Die AKF misst so die mittlere Größe des Signals, unabhängig vom Zusammenhang der Werte.
:::
:::karte zusammenhang Scharmittel und Zeitmittel
Worin unterscheiden sich Scharmittel und Zeitmittel eines Zufallsprozesses, wenn man seine Musterfunktionen untereinander zeichnet?
---
Das Scharmittel bildet man senkrecht: über alle Musterfunktionen beim selben Zeitpunkt $t_1$. Das Zeitmittel bildet man waagerecht: entlang einer einzigen Musterfunktion über die Zeit.
--- falsch
Das Scharmittel bildet man waagerecht: entlang einer einzigen Musterfunktion über die Zeit. Das Zeitmittel bildet man senkrecht: über alle Musterfunktionen beim selben Zeitpunkt $t_1$.
--- falsch
Beide bildet man senkrecht über alle Musterfunktionen; das Scharmittel mittelt die Werte, das Zeitmittel ihre Quadrate. Deshalb ist das Zeitmittel stets größer als das Scharmittel.
--- falsch
Das Scharmittel mittelt über alle Musterfunktionen und alle Zeitpunkte zugleich. Das Zeitmittel mittelt nur über eine Musterfunktion und ist deshalb nur ein Teil des Scharmittels.
:::
::::
