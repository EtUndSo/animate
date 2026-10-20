---
title: Arbeitspunkt und Ersatzschaltung der Diode
pfad: Elektrotechnik / 1. Semester / Grundgebiete der Elektrotechnik 1 / Halbleiterbauelemente
order: 100400
summary: Wie man den Betriebspunkt einer Diode grafisch über den Schnittpunkt von Kennlinie und Arbeitsgerade findet und wie man die krumme Kennlinie durch einfache lineare Ersatzmodelle ersetzt, um damit rechnen zu können.
tags: Arbeitspunkt, Arbeitsgerade, Lastgerade, Ersatzschaltung, differentieller Widerstand, Diode
---

:::konzept
Die Diodenkennlinie ist gekrümmt — man kann also nicht einfach $U = R\cdot I$ ansetzen. Zwei Wege führen trotzdem
zum Ziel. **Grafisch**: Man zeichnet die Kennlinie und die „Spielregel" der äußeren Schaltung (eine Gerade) in
dasselbe Diagramm; ihr **Schnittpunkt** ist der Betriebszustand, der **Arbeitspunkt**. **Rechnerisch**: Man
ersetzt die Diode in der Nähe dieses Punktes durch ein einfaches lineares Modell — eine Schwellspannung und
einen kleinen Widerstand — und rechnet damit wie gewohnt.
:::

**Worum es geht:** Die nichtlineare Diode (voriger Abschnitt) soll in einer realen Schaltung berechenbar werden.
Wir bestimmen ihren __Arbeitspunkt__ über die __Arbeitsgerade__ und bauen dann stufenweise eine lineare
__Ersatzschaltung__.

## Die Arbeitsgerade

Eine Diode arbeitet nie allein, sondern mit einer Quelle $U_0$ und (mindestens) einem Vorwiderstand $R$ in
Reihe. Die __Maschenregel__ liefert $U_0 = R\cdot I + U_\text{D}$, und nach dem Diodenstrom aufgelöst:

$$I = \frac{U_0 - U_\text{D}}{R}.$$

- __$I$__: der __Strom__ durch Diode und Widerstand.
- __$U_0$__: die __Quellenspannung__.
- __$U_\text{D}$__: die __Diodenspannung__ (noch unbekannt).
- __$R$__: der __Vorwiderstand__.

Das ist eine **Gerade** im $I$-$U_\text{D}$-Diagramm, die __Arbeitsgerade__ (oder Lastgerade). Zwei Punkte legen
sie fest: Bei $U_\text{D} = 0$ (gedachter Kurzschluss der Diode) ist $I = U_0/R$, bei $I = 0$ (Leerlauf) ist
$U_\text{D} = U_0$. Ihre Steigung ist durch $-1/R$ gegeben — ein großer Vorwiderstand macht sie flach.

## Der Arbeitspunkt

Die Diode muss **gleichzeitig** zwei Bedingungen erfüllen: Sie liegt auf ihrer eigenen Kennlinie **und** auf der
Arbeitsgeraden der äußeren Schaltung. Beides zusammen gilt nur in ihrem **Schnittpunkt** — dem __Arbeitspunkt__
(AP). Er legt die tatsächliche Diodenspannung $U_\text{AP}$ und den Strom $I_\text{AP}$ fest.

Grafisch ist das denkbar einfach: Kennlinie und Arbeitsgerade ins selbe Diagramm zeichnen, Schnittpunkt ablesen.
Ändert man die Schaltung — etwa eine andere Quellenspannung —, verschiebt sich die Arbeitsgerade parallel, und
der Arbeitspunkt wandert auf der Kennlinie entlang.

:::grafik
Links die Schaltung: Quelle $U_0$, Vorwiderstand $R$, Diode in Reihe. Rechts das $I$-$U_\text{D}$-Diagramm mit der
gekrümmten Diodenkennlinie und der Arbeitsgeraden (von $U_0$ auf der Spannungsachse zu $U_0/R$ auf der
Stromachse). Ihr Schnittpunkt ist als Arbeitspunkt $(U_\text{AP}, I_\text{AP})$ markiert.
:::

## Lineare Ersatzschaltung

Für Rechnungen ersetzt man die Diode durch ein lineares Modell — je nach gewünschter Genauigkeit in drei Stufen.

**Stufe 1 — die ideale Diode.** Man behandelt die Diode als reinen Schalter: in Durchlassrichtung ein
widerstandsloser Draht ($U_\text{D} = 0$), in Sperrrichtung eine Unterbrechung. Gut für grobe Überschläge, in
denen die $0{,}7\,\text{V}$ neben großen Spannungen vernachlässigbar sind.

**Stufe 2 — ideale Diode plus Schleusenspannung.** Man ergänzt eine konstante __Schleusenspannung__ $U_\text{S}$
(etwa $0{,}7\,\text{V}$ bei Silizium) als „Gegenbatterie". Die Diode leitet erst, wenn die äußere Spannung
$U_\text{S}$ überschreitet, und hält dann diese Spannung. Das ist das gängige Modell für die meisten
Handrechnungen.

**Stufe 3 — zusätzlich der differentielle Widerstand.** Die reale Kennlinie ist auch oberhalb der Schwelle noch
leicht ansteigend. Diese Steigung modelliert man durch einen kleinen __differentiellen Widerstand__
$r_\text{D}$ in Reihe. Er ist die Steigung der Kennlinie **im Arbeitspunkt** und folgt durch Ableiten der
Shockley-Gleichung:

$$r_\text{D} = \frac{\mathrm{d}U}{\mathrm{d}I} = \frac{U_\text{T}}{I_\text{AP}}.$$

- __$r_\text{D}$__: der __differentielle Widerstand__ der Diode im Arbeitspunkt.
- __$U_\text{T}$__: die __Temperaturspannung__ ($\approx 26\,\text{mV}$).
- __$I_\text{AP}$__: der __Arbeitspunktstrom__.

Wichtig: $r_\text{D}$ ist **kein** fester Bauteilwert, sondern hängt vom Arbeitspunkt ab — bei größerem Strom
wird er kleiner. Er gilt nur für kleine Auslenkungen um den Arbeitspunkt (Kleinsignalbetrieb). Bei großen
Strömen kommt noch der konstante __Bahnwiderstand__ des Halbleitermaterials hinzu.

:::grafik
Drei Ersatzschaltbilder nebeneinander, zunehmend genauer: (1) ideale Diode allein, (2) ideale Diode + Batterie
$U_\text{S}$, (3) ideale Diode + $U_\text{S}$ + Widerstand $r_\text{D}$. Darüber jeweils die zugehörige
genäherte Kennlinie (senkrechte Stufe / geknickte Senkrechte / geknickte Gerade mit Steigung $1/r_\text{D}$).
:::

:::kern
Der __Arbeitspunkt__ einer Diode ist der **Schnittpunkt** ihrer Kennlinie mit der __Arbeitsgeraden__
$I = (U_0 - U_\text{D})/R$ (Steigung $-1/R$, Achsenpunkte $U_0$ und $U_0/R$). Für Rechnungen ersetzt man die
Diode durch eine lineare __Ersatzschaltung__ in drei Stufen: ideale Diode (Schalter), + __Schleusenspannung__
$U_\text{S} \approx 0{,}7\,\text{V}$, + __differentieller Widerstand__ $r_\text{D} = U_\text{T}/I_\text{AP}$ (nur
im Kleinsignal, arbeitspunktabhängig).
:::

Mit Arbeitspunkt und Ersatzmodell lässt sich die Diode in Schaltungen berechnen. Damit sind die Werkzeuge
beisammen, um ihre wichtigste Anwendung zu verstehen: die __Gleichrichtung__ von Wechselspannung.

:::quiz
F: Warum kann man bei einer Diode nicht einfach $U=R\,I$ ansetzen?
A: Ihre Kennlinie ist gekrümmt (nichtlinear), der „Widerstand" $U/I$ ist also nicht konstant. Man braucht entweder die grafische Arbeitspunktmethode oder ein lineares Ersatzmodell.
F: Woher kommt die Arbeitsgerade, und was beschreibt sie?
A: Aus der Maschenregel der äußeren Schaltung: $I=(U_0-U_D)/R$. Sie ist die „Spielregel" von Quelle und Vorwiderstand — alle Betriebszustände, die die äußere Schaltung zulässt.
F: Warum ist der Arbeitspunkt gerade der Schnittpunkt von Kennlinie und Arbeitsgerade?
A: Die Diode muss gleichzeitig ihrer eigenen Kennlinie *und* der Bedingung der äußeren Schaltung genügen. Nur im Schnittpunkt sind beide erfüllt — er legt $U_{AP}$ und $I_{AP}$ fest.
F: Was bestimmt die Steigung der Arbeitsgeraden?
A: Der Vorwiderstand: Die Steigung ist $-1/R$. Ein großer Vorwiderstand macht die Gerade flach, ein kleiner steil.
F: Wie wandert der Arbeitspunkt, wenn man die Quellenspannung erhöht?
A: Die Arbeitsgerade verschiebt sich parallel (gleiche Steigung $-1/R$, anderer Achsenschnittpunkt $U_0$). Der Schnittpunkt mit der Kennlinie wandert auf ihr entlang zu höherem Strom.
F: Was leistet die einfachste Ersatzschaltung (ideale Diode als Schalter)?
A: Sie behandelt die Diode als widerstandslosen Draht in Durchlass und als Unterbrechung in Sperrrichtung ($U_D=0$). Das genügt für grobe Überschläge, wenn die 0,7 V neben großen Spannungen vernachlässigbar sind.
F: Was fügt die zweite Stufe (ideale Diode + Schleusenspannung) hinzu?
A: Eine konstante „Gegenbatterie" $U_S\approx0{,}7\,$V: Die Diode leitet erst, wenn die äußere Spannung sie überschreitet, und hält dann diese Spannung. Das ist das Standardmodell für Handrechnungen.
F: Wofür steht der differentielle Widerstand $r_D$?
A: Für die leichte Steigung der Kennlinie oberhalb der Schwelle, modelliert als kleiner Reihenwiderstand. Er ist die Ableitung $dU/dI$ im Arbeitspunkt, $r_D=U_T/I_{AP}$.
F: Warum ist $r_D$ kein fester Bauteilwert?
A: Er hängt vom Arbeitspunkt ab: $r_D=U_T/I_{AP}$ wird mit steigendem Strom kleiner. Zudem gilt er nur für kleine Auslenkungen um den Arbeitspunkt (Kleinsignalbetrieb).
F: Warum reicht das Kleinsignalmodell mit $r_D$ bei großen Strömen nicht mehr?
A: Es beschreibt nur die lokale Steigung um den Arbeitspunkt. Bei großen Strömen kommt zusätzlich der konstante Bahnwiderstand des Halbleitermaterials hinzu, den $r_D$ nicht erfasst.
:::
