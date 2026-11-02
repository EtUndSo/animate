---
title: Stufe 3: Mittlere Leistung bei Sinusspannung
pfad: Elektrotechnik / 1. Semester / Grundlagen der Elektrotechnik / Leistung, Anpassung und Wirkungsgrad
order: 1170400
summary: An einer Wechselspannung ändert sich die Leistung ständig.
tags: Amplituden, Periodendauer, Kreisfrequenz, Effektivwert
lang: de
---

<span class="anker" id="stufe-3"></span>

:::zweck
An einer Wechselspannung ändert sich die Leistung ständig. Diese Stufe findet die eine Zahl, die die Erwärmung bestimmt.
:::

**Die Idee.** Am Widerstand ist $i$ proportional zu $u$. Beide wechseln gleichzeitig das Vorzeichen, ihr Produkt ist deshalb nie negativ. Läuft die Ladung rückwärts, ist auch die Spannung umgekehrt, und sie gibt wieder Energie ab. Beide Halbwellen heizen (Abb. [4](#abb-4)). Die Leistung pulsiert zwischen null und dem Spitzenwert, doppelt so schnell wie die Spannung. Ihr Mittelwert liegt auf halber Höhe.

:::abbildung et1/k7sinus 4
Links Spannung und Strom am Heizwiderstand. Rechts die Momentanleistung $p(t)$. Sie schwingt zwischen 0 und 20 W um den Mittelwert $P=10$ W und ist doppelt so oft maximal wie $u$.
:::

:::satz Satz 3.1 (Mittlere Leistung am Widerstand)
<span class="anker" id="satz-3-1"></span>

Für $u(t)=\hat u\cos(\omega t)$ an $R$ fließt $i(t)=\hat\imath\cos(\omega t)$ mit $\hat\imath=\hat u/R$. Der zeitliche Mittelwert der Leistung ist

<span class="anker" id="gl-3-1"></span>
$$P=\frac1T\int_0^T u(t)\,i(t)\,\mathrm{d} t=\frac12\,\frac{\hat u^2}{R}=\frac12\,\hat\imath^2R. \tag{3.1}$$
:::

⁠**So liest man das:** $\hat u$ und $\hat\imath$ sind die __Amplituden__, die Spitzenwerte. $T$ ist die __Periodendauer__, $\omega=2\pi/T$ die __Kreisfrequenz__. Am Netz sind es $T=20$ ms und $\omega=314$ 1/s. **Gültigkeit:** Der Mittelwert läuft über ganze Perioden. Die Formel gilt nur, wenn $i$ proportional zu $u$ ist, also für Widerstände.

:::herleitung Woher der Faktor $\frac12$ kommt
Einsetzen ergibt $p=u\,i=u^2/R=(\hat u^2/R)\cos^2(\omega t)$. Mit $\cos^2x=\frac12(1+\cos2x)$ wird

$$P=\frac{1}{T\,R}\int_0^T\hat u^2\cos^2(\omega t)\,\mathrm{d} t=\frac{1}{T\,R}\int_0^T\hat u^2\,\frac12\bigl(1+\cos(2\omega t)\bigr)\,\mathrm{d} t=\frac12\,\frac{\hat u^2}{R}.$$

Der Kosinusteil durchläuft in $T$ zwei volle Schwingungen, sein Integral ist null. Mit $\hat u=R\,\hat\imath$ folgt die zweite Form.
:::

**Beispiel.** Für $\hat u=10$ V und $R=5\,\Omega$ sind $\hat\imath=2$ A, der Spitzenwert der Leistung 20 W und $P=10$ W. Bei 50 Hz fließen je Periode 0,2 J ins Gitter. **Grenzfall:** Für $\omega\to0$ wird aus $u$ eine Gleichspannung und $p$ bleibt bei $\hat u^2/R$ stehen. Der Faktor $\frac12$ fällt weg, denn über ganze Perioden lässt sich dann nicht mehr mitteln.

:::zusatz Effektivwert
Eine Gleichspannung $U$ erzeugt an $R$ dieselbe Wärme, wenn $U^2/R=\frac12\hat u^2/R$ ist, also $U=\hat u/\sqrt2$. Dieser Wert heißt __Effektivwert__. Hier sind es 7,07 V. Die 230 V der Steckdose sind ein Effektivwert, die Amplitude beträgt 325 V.
:::

:::ltspice Mittlere Leistung messen
⁠**Zeichnen:** `voltage` von `a` nach Masse mit `SINE(0 10 50)`, `res` `R1` mit 5 von `a` nach Masse.

⁠**Direktiven:** `.tran 0 40m 0 10u` und `.meas tran Pm AVG V(a)*I(R1) FROM=0 TO=40m`

⁠**Was du siehst:** Trage `V(a)*I(R1)` auf: Die Kurve bleibt zwischen 0 und 20 W und schwingt mit 100 Hz. Das Log nennt `Pm` = 10 W. Für Aufgabe [3](#aufg-3) setzt du die Amplitude 325 und deinen Widerstand ein und liest 2 kW und 4 kW ab.
:::

:::frage Bei Wechselstrom pendeln die Elektronen nur hin und her. Wie kann das Energie liefern?
Weil die Energie nicht mit den Elektronen reist. Selbst bei 1 A/mm$^2$ und 50 Hz legen sie je Halbperiode nur rund 0,5 µ m zurück. Das Feld im Widerstand beschleunigt sie in beiden Richtungen, und jeder Stoß gibt Energie ans Gitter ab. Dafür braucht es kein Vorankommen, nur Spannung und Strom.
:::

:::aufgabe Aufgabe 3 ★★ Der Heizlüfter
<span class="anker" id="aufg-3"></span>

Ein Heizlüfter nimmt an einer Sinusspannung mit $\hat u=325$ V und 50 Hz im Mittel 2 kW auf. (a) Wie groß sind $R$, $\hat\imath$ und der Spitzenwert der Leistung? (b) Wie oft je Sekunde ist $p=0$? (c) Ein Bauteil sperrt jede zweite Halbwelle. Sage die mittlere Leistung voraus, wenn $R$ gleich bleibt.

:::loesung
(a) Aus [(3.1)](#gl-3-1): $R=\hat u^2/(2P)=26{,}4\,\Omega$, $\hat\imath=\hat u/R=12{,}3$ A, Spitzenwert $\hat u\,\hat\imath=2P=4$ kW. (b) Je Periode zweimal, also 100-mal je Sekunde. (c) Es fehlt jede zweite Halbwelle, also die Hälfte der Energie: 1 kW.
:::
:::
