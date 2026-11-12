---
title: Stufe 3: Mittlere Leistung bei Sinusspannung
pfad: Elektrotechnik / 1. Semester / ET1 – Grundgebiete der Elektrotechnik 1: Einführung in die Schaltungsanalyse / Leistung, Anpassung und Wirkungsgrad
adresse: elektrotechnik/1-semester/grundlagen-der-elektrotechnik/leistung-anpassung-und-wirkungsgrad
knoten: Kapitel 7: Leistung, Anpassung und Wirkungsgrad
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

::::beispiel
Für $\hat u=10$ V und $R=5\,\Omega$ sind $\hat\imath=2$ A, der Spitzenwert der Leistung 20 W und $P=10$ W. Bei 50 Hz fließen je Periode 0,2 J ins Gitter.
::::

⁠**Grenzfall:** Für $\omega\to0$ wird aus $u$ eine Gleichspannung und $p$ bleibt bei $\hat u^2/R$ stehen. Der Faktor $\frac12$ fällt weg, denn über ganze Perioden lässt sich dann nicht mehr mitteln.

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

::::formelsammlung
**Sinusgrößen am Widerstand**

$$u(t)=\hat u\cos(\omega t),\qquad i(t)=\hat\imath\cos(\omega t),\qquad\hat\imath=\hat u/R,\qquad\omega=2\pi/T$$

$\hat u$, $\hat\imath$ Amplituden (Spitzenwerte), $T$ Periodendauer, $\omega$ Kreisfrequenz. Am Netz sind $T=20$ ms und $\omega=314$ 1/s.

**Momentanleistung am Widerstand**

$$p=u\,i=u^2/R=(\hat u^2/R)\cos^2(\omega t)$$

Nie negativ, weil $u$ und $i$ gleichzeitig das Vorzeichen wechseln. Pulsiert zwischen 0 und $\hat u^2/R$, doppelt so schnell wie $u$. Mit $\cos^2x=\frac12(1+\cos2x)$ zerfällt sie in den Mittelwert und einen Kosinus der doppelten Frequenz.

**Mittlere Leistung am Widerstand**

$$P=\frac1T\int_0^T u(t)\,i(t)\,\mathrm{d} t=\frac12\,\frac{\hat u^2}{R}=\frac12\,\hat\imath^2R$$

Zeitlicher Mittelwert über ganze Perioden. Gilt nur, wenn $i$ proportional zu $u$ ist, also für Widerstände. Für $\omega\to0$ wird $u$ zur Gleichspannung, $p$ bleibt bei $\hat u^2/R$, und der Faktor $\frac12$ fällt weg.

**Effektivwert**

$$U=\hat u/\sqrt2$$

Die Gleichspannung, die an $R$ dieselbe Wärme erzeugt: $U^2/R=\frac12\hat u^2/R$. Die 230 V der Steckdose sind ein Effektivwert, die Amplitude beträgt 325 V.
::::

::::lernkarten
:::karte begriff Amplituden
Was bezeichnen die Amplituden $\hat u$ und $\hat\imath$ einer Sinusspannung $u(t)=\hat u\cos(\omega t)$ und des zugehörigen Stroms?
---
Die Spitzenwerte, also die größten Werte, die Spannung und Strom im Lauf einer Periode erreichen. Am Widerstand gilt $\hat\imath=\hat u/R$.
--- falsch
Die Mittelwerte von Spannung und Strom über eine ganze Periode. Am Widerstand gilt $\hat\imath=\hat u/R$, weil auch die Mittelwerte dem ohmschen Gesetz folgen.
--- falsch
Die Werte, die eine Gleichspannung und ein Gleichstrom hätten, wenn sie dieselbe Wärme erzeugen. An der Steckdose beträgt die Amplitude 230 V.
--- falsch
Die Abstände zwischen dem größten und dem kleinsten Wert von Spannung und Strom. Am Widerstand gilt $\hat\imath=\hat u/R$.
:::
:::karte begriff Periodendauer
Was gibt die Periodendauer $T$ einer Sinusspannung an, und wie groß ist sie am Netz mit 50 Hz?
---
Die Zeit, nach der sich der Verlauf der Spannung wiederholt, also die Dauer einer vollen Schwingung. Am Netz sind es $T=20$ ms.
--- falsch
Die Zeit, die eine Halbwelle dauert, also vom einen Nulldurchgang der Spannung bis zum nächsten. Am Netz sind es $T=10$ ms.
--- falsch
Die Zahl der vollen Schwingungen je Sekunde, also wie oft sich der Verlauf in einer Sekunde wiederholt. Am Netz ist $T=50$ 1/s.
--- falsch
Die Zeit, die die Spannung braucht, um vom Nullwert auf ihren Spitzenwert zu steigen. Am Netz sind es $T=5$ ms.
:::
:::karte begriff Kreisfrequenz
Was gibt die Kreisfrequenz $\omega$ im Ausdruck $u(t)=\hat u\cos(\omega t)$ an, und wie hängt sie mit der Periodendauer zusammen?
---
Wie schnell das Argument des Kosinus mit der Zeit wächst: In einer Periodendauer $T$ wächst $\omega t$ um $2\pi$, also ist $\omega=2\pi/T$. Am Netz sind es 314 1/s.
--- falsch
Die Zahl der vollen Schwingungen je Sekunde. Sie ist der Kehrwert der Periodendauer, $\omega=1/T$, und beträgt am Netz mit 20 ms deshalb 50 1/s.
--- falsch
Wie schnell die Spannung beim Nulldurchgang in Volt je Sekunde ansteigt. Sie ist $\omega=\hat u/T$ und hängt deshalb von der Amplitude ab.
--- falsch
Die Zeit, in der der Kosinus einmal ganz durchläuft, in Bogenmaß gemessen. Sie ist $\omega=2\pi\,T$, am Netz also 0,126 s.
:::
:::karte begriff Effektivwert
Was ist der Effektivwert einer Sinusspannung, und wie hängt er mit ihrer Amplitude zusammen?
---
Die Gleichspannung $U$, die an demselben Widerstand dieselbe Wärme erzeugt. Aus $U^2/R=\frac12\hat u^2/R$ folgt $U=\hat u/\sqrt2$; die 230 V der Steckdose sind ein Effektivwert, die Amplitude beträgt 325 V.
--- falsch
Der Mittelwert der Spannung über eine Halbwelle. Er ist $U=\hat u/2$, weil die Spannung im Mittel halb so groß ist wie ihr Spitzenwert; die 230 V der Steckdose sind daher die Amplitude.
--- falsch
Die Gleichspannung $U$, die an demselben Widerstand dieselbe Wärme erzeugt. Weil die Leistung im Mittel halb so groß ist, folgt $U=\hat u/2$; zu den 230 V gehört die Amplitude 460 V.
--- falsch
Der größte Wert, den die Spannung wirklich erreicht, im Unterschied zum gerechneten Wert $\hat u$. Er ist $U=\sqrt2\,\hat u$; die Steckdose liefert also 325 V effektiv und 230 V als Amplitude.
:::
:::karte formel Mittlere Leistung am Widerstand
Wie groß ist die mittlere Leistung an einem Widerstand $R$ bei der Sinusspannung $u(t)=\hat u\cos(\omega t)$, und wann gilt die Formel?
---
$P=\frac1T\int_0^T u(t)\,i(t)\,\mathrm{d} t=\frac12\,\frac{\hat u^2}{R}=\frac12\,\hat\imath^2R$. Gemittelt wird über ganze Perioden; die Formel gilt nur, wenn $i$ proportional zu $u$ ist, also für Widerstände.
--- falsch
$P=\frac1T\int_0^T u(t)\,i(t)\,\mathrm{d} t=\frac12\,\frac{\hat u^2}{R}$. Die Formel gilt für jedes Bauteil, weil der Mittelwert von $\cos^2$ stets $\frac12$ ist, gleich wie Strom und Spannung zusammenhängen.
--- falsch
$P=\frac{\hat u^2}{R}$, weil die Wärme vom Spitzenwert bestimmt wird. Zwischen den Spitzen kühlt der Widerstand nicht merklich ab, deshalb zählt für die Erwärmung nur der größte Wert.
--- falsch
$P=0$, weil sich die Beiträge der positiven und der negativen Halbwelle gegenseitig aufheben. Der Widerstand erwärmt sich nur, wenn man über eine einzelne Halbwelle mittelt.
:::
:::karte zusammenhang Beide Halbwellen heizen
Warum heizt an einem Widerstand auch die negative Halbwelle einer Wechselspannung, statt der positiven entgegenzuwirken?
---
Am Widerstand ist $i$ proportional zu $u$, beide wechseln gleichzeitig das Vorzeichen, ihr Produkt ist nie negativ. Läuft die Ladung rückwärts, ist auch die Spannung umgekehrt, und sie gibt wieder Energie ab.
--- falsch
Weil jeder Widerstand die negative Halbwelle wie ein Gleichrichter nach oben umklappt. Ohne diese Wirkung würde die negative Halbwelle dem Widerstand die Wärme der positiven Halbwelle wieder vollständig entziehen.
--- falsch
Weil in der negativen Halbwelle nur der Strom das Vorzeichen wechselt, die Spannung aber positiv bleibt. Das Produkt ist dann zwar negativ, für die Wärme zählt aber sein Betrag.
--- falsch
Weil die Elektronen in der negativen Halbwelle stehen bleiben und das Gitter in dieser Zeit nur die Wärme weiterleitet, die es in der positiven Halbwelle aufgenommen hat.
:::
:::karte zusammenhang Verlauf der Momentanleistung
Wie verläuft die Momentanleistung an einem Widerstand bei Sinusspannung, und wo liegt ihr Mittelwert?
---
Sie pulsiert zwischen null und dem Spitzenwert $\hat u^2/R$, doppelt so schnell wie die Spannung, bei 50 Hz also mit 100 Hz. Ihr Mittelwert liegt auf halber Höhe.
--- falsch
Sie schwingt zwischen $-\hat u^2/R$ und $+\hat u^2/R$, genauso schnell wie die Spannung. Ihr Mittelwert ist null, weil sich die beiden Halbwellen aufheben.
--- falsch
Sie pulsiert zwischen null und dem Spitzenwert $\hat u^2/R$, halb so schnell wie die Spannung, weil nur jede zweite Halbwelle heizt. Ihr Mittelwert liegt auf halber Höhe.
--- falsch
Sie ist konstant gleich $\hat u^2/R$, weil Spannung und Strom zwar schwingen, ihr Produkt aber nicht. Der Mittelwert ist deshalb derselbe wie der Spitzenwert.
:::
:::karte zusammenhang Grenzfall Gleichspannung
Warum fällt der Faktor $\frac12$ in der mittleren Leistung weg, wenn die Kreisfrequenz gegen null geht?
---
Für $\omega\to0$ wird aus $u$ eine Gleichspannung, und $p$ bleibt bei $\hat u^2/R$ stehen. Über ganze Perioden lässt sich dann nicht mehr mitteln.
--- falsch
Er fällt nicht weg: Auch eine Gleichspannung erzeugt im Mittel nur $\frac12\,\hat u^2/R$, weil der Widerstand die Hälfte der Energie an die Quelle zurückgibt.
--- falsch
Für $\omega\to0$ wird die Periodendauer null, und das Integral über eine Periode verschwindet. Die Leistung geht dann gegen null statt gegen $\hat u^2/R$.
--- falsch
Für $\omega\to0$ wird aus $u$ eine Gleichspannung, und $p$ verdoppelt sich auf $2\,\hat u^2/R$, weil die Elektronen nicht mehr umkehren müssen.
:::
:::karte zusammenhang Energie bei pendelnden Elektronen
Wie kann Wechselstrom Energie an einen Widerstand liefern, obwohl die Elektronen dabei nur hin- und herpendeln?
---
Weil die Energie nicht mit den Elektronen reist. Das Feld im Widerstand beschleunigt sie in beiden Richtungen, und jeder Stoß gibt Energie ans Gitter ab; ein Vorankommen ist dafür nicht nötig.
--- falsch
Weil die Elektronen bei jedem Pendeln ein Stück weiter wandern und nach vielen Perioden doch vom Kraftwerk bis zum Gerät gelangen. Erst dort, am Ende ihres langen Wegs, geben sie ihre Energie ab.
--- falsch
Weil nur die Elektronen in der Hinrichtung Energie abgeben; in der Rückrichtung bewegen sie sich ohne Feld und stoßen nicht. Im Mittel bleibt so die Hälfte der Energie.
--- falsch
Weil die Elektronen beim Umkehren ihrer Richtung kurz stillstehen und dabei ihre ganze Bewegungsenergie abgeben. Je höher die Frequenz, desto öfter geschieht das.
:::
:::karte zusammenhang Gesperrte Halbwelle
Was geschieht mit der mittleren Leistung an einem Widerstand, wenn ein Bauteil jede zweite Halbwelle der Sinusspannung sperrt?
---
Sie halbiert sich: Jede Halbwelle liefert gleich viel Energie, und nun fehlt jede zweite, also die Hälfte der Energie. Aus 2 kW wird 1 kW.
--- falsch
Sie bleibt gleich, weil die verbleibende Halbwelle dann die doppelte Energie liefert. Der Widerstand nimmt im Mittel weiterhin 2 kW auf.
--- falsch
Sie sinkt auf ein Viertel, weil die Leistung quadratisch von der Spannung abhängt und die halbe Spannung ein Viertel bringt. Aus 2 kW werden 500 W.
--- falsch
Sie verdoppelt sich, weil sich positive und negative Halbwelle nicht mehr gegenseitig aufheben. Aus 2 kW werden dann 4 kW.
:::
:::karte herleitung Faktor ein Halb
Leite aus $p=u\,i$ für $u(t)=\hat u\cos(\omega t)$ an $R$ den Mittelwert $P=\frac12\,\frac{\hat u^2}{R}$ der Leistung her.
---
Einsetzen ergibt $p=u\,i=u^2/R=(\hat u^2/R)\cos^2(\omega t)$, weil am Widerstand $i$ proportional zu $u$ ist.
---
Mit $\cos^2x=\frac12(1+\cos2x)$ wird der Integrand eine Konstante plus ein Kosinus der doppelten Frequenz, weil sich das Quadrat so in zwei Teile zerlegen lässt.
---
Im Mittelwert $\frac{1}{T\,R}\int_0^T\hat u^2\,\frac12\bigl(1+\cos(2\omega t)\bigr)\,\mathrm{d} t$ hat der Kosinusteil das Integral null, weil er in $T$ zwei volle Schwingungen durchläuft.
---
Es bleibt $\frac12\,\frac{\hat u^2}{R}$, weil der Mittelwert einer Konstanten die Konstante selbst ist.
---
Mit $\hat u=R\,\hat\imath$ folgt die zweite Form $\frac12\,\hat\imath^2R$, weil man den Spitzenwert der Spannung durch den des Stroms ersetzt.
:::
::::
