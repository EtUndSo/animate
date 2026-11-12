---
title: Von Grund auf: Klemmen, Kennlinie, Linearität
pfad: Elektrotechnik / 1. Semester / ET1 – Grundgebiete der Elektrotechnik 1: Einführung in die Schaltungsanalyse / Quellen und Ersatzquellen
adresse: elektrotechnik/1-semester/grundlagen-der-elektrotechnik/quellen-und-ersatzquellen
knoten: Kapitel 5: Quellen und Ersatzquellen
order: 1150200
summary: Warum zwei Zahlen ein ganzes Netzwerk ersetzen
tags: Klemme, Eintor, Kennlinie, Leerlauf, linear
lang: de
---

Eine __Klemme__ ist ein Anschlusspunkt nach außen. Ein __Eintor__ ist ein Netzwerk mit genau zwei Klemmen, die ein Paar bilden: Der Strom, der an A hinausfließt, kommt an B wieder herein, denn Ladung geht nicht verloren (Knotenregel, [Kapitel 2](/wissen/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/strom-widerstand-und-kirchhoff/strom-widerstand-und-kirchhoff.html)). Ein Eintor hat deshalb nur einen Strom und eine Spannung. Es ist ein Zweipol aus [Kapitel 2](/wissen/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/strom-widerstand-und-kirchhoff/strom-widerstand-und-kirchhoff.html), auch wenn es innen viele Bauteile enthält. Die __Kennlinie__ ist der Zusammenhang dieser beiden Größen. Sie steht in diesem Kapitel immer im selben Diagramm: Klemmenstrom waagerecht, Klemmenspannung senkrecht.

Die Zählpfeile gelten im ganzen Kapitel: $U_\mathrm{AB}=\varphi_\mathrm{A}-\varphi_\mathrm{B}$ zählt von A nach B, $I_\mathrm{A}$ zählt aus der Klemme A heraus. Für die angeschlossene Last zeigen beide Pfeile in dieselbe Richtung (Verbraucher-Zählpfeile, [Kapitel 2](/wissen/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/strom-widerstand-und-kirchhoff/strom-widerstand-und-kirchhoff.html)), für das Eintor selbst entgegengesetzt (Erzeuger-Zählpfeile). Sind beide positiv, gibt das Eintor Leistung ab. __Leerlauf__ heißt: Die Klemmen sind offen, $I_\mathrm{A}=0$. Kurzschluss heißt: Die Klemmen sind durch einen Draht verbunden, $U_\mathrm{AB}=0$.

Ein Bauteil ist __linear__, wenn sein Strom proportional zu seiner Spannung ist. Ein Widerstand ist das, solange $R$ nicht vom Strom abhängt: Seine Kennlinie ist eine Gerade durch den Ursprung. Eine Glühlampe oder eine Diode ([Kapitel 9](/wissen/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/halbleiter-und-dioden/halbleiter-und-dioden.html)) ist es nicht. Das Zeichen $\parallel$ steht für den Widerstand einer Parallelschaltung, $R_1\parallel R_2=\frac{R_1R_2}{R_1+R_2}$ ([Kapitel 2](/wissen/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/strom-widerstand-und-kirchhoff/strom-widerstand-und-kirchhoff.html)). Es bindet stärker als das Plus, wie die Punktrechnung.

::::formelsammlung
**Zählpfeile am Eintor**

$$U_\mathrm{AB}=\varphi_\mathrm{A}-\varphi_\mathrm{B}$$

$U_\mathrm{AB}$ zählt von A nach B, der Klemmenstrom $I_\mathrm{A}$ aus der Klemme A heraus. Für die angeschlossene Last zeigen beide Pfeile in dieselbe Richtung (Verbraucher-Zählpfeile), für das Eintor selbst entgegengesetzt (Erzeuger-Zählpfeile). Sind beide positiv, gibt das Eintor Leistung ab.

**Leerlauf und Kurzschluss**

$$I_\mathrm{A}=0\quad\text{(Leerlauf)},\qquad U_\mathrm{AB}=0\quad\text{(Kurzschluss)}$$

Leerlauf: Die Klemmen sind offen. Kurzschluss: Die Klemmen sind durch einen Draht verbunden.

**Parallelschaltung (Schreibweise)**

$$R_1\parallel R_2=\frac{R_1R_2}{R_1+R_2}$$

$\parallel$ steht für den Widerstand einer Parallelschaltung. Das Zeichen bindet stärker als das Plus, wie die Punktrechnung.
::::

::::lernkarten
:::karte begriff Klemme
Was ist eine Klemme, wenn man ein Netzwerk von außen betrachtet?
---
Ein Anschlusspunkt des Netzwerks nach außen. Über zwei Klemmen, etwa A und B, wird das Netzwerk mit dem verbunden, was man anschließt.
--- falsch
Ein innerer Knoten des Netzwerks, an dem mindestens drei Zweige zusammentreffen und an dem von außen nichts angeschlossen werden kann.
--- falsch
Ein Bauteil, das zwei Leitungen fest verbindet und dabei den Strom begrenzt, damit das Netzwerk geschützt bleibt.
--- falsch
Der Pluspol einer Quelle. Ein Netzwerk ohne Quelle hat deshalb keine Klemmen, auch wenn Leitungen nach außen führen.
:::
:::karte begriff Eintor
Was ist ein Eintor, und warum hat es nur einen Strom und eine Spannung?
---
Ein Netzwerk mit genau zwei Klemmen, die ein Paar bilden: Der Strom, der an A hinausfließt, kommt an B wieder herein, weil Ladung nicht verloren geht. Es ist ein Zweipol, auch mit vielen Bauteilen innen.
--- falsch
Ein Netzwerk mit genau einem Bauteil zwischen zwei Klemmen. Enthält es mehrere Bauteile, fließen an den Klemmen mehrere Ströme, und jedes Bauteil braucht seine eigene Kennlinie.
--- falsch
Ein Netzwerk mit nur einer Klemme: Der Strom fließt dort hinein und wird innen gespeichert. Eine Spannung entsteht erst, wenn man eine zweite Klemme anschließt, deshalb gibt es nur eine Spannung und einen Strom.
--- falsch
Ein Netzwerk mit zwei Klemmen, an denen verschiedene Ströme fließen dürfen. Es hat trotzdem nur eine Spannung und einen Strom, weil man außen nur den größeren der beiden Ströme misst.
:::
:::karte begriff Kennlinie
Was zeigt die Kennlinie eines Eintors, und wie ist ihr Diagramm in diesem Kapitel angelegt?
---
Den Zusammenhang zwischen Klemmenstrom und Klemmenspannung des Eintors. Im Diagramm steht der Klemmenstrom waagerecht und die Klemmenspannung senkrecht.
--- falsch
Den Verlauf der Klemmenspannung über der Zeit vom Einschalten an. Im Diagramm steht die Zeit waagerecht und die Klemmenspannung senkrecht.
--- falsch
Den Widerstand jedes einzelnen Bauteils im Eintor. Im Diagramm steht die Lage des Bauteils zwischen A und B waagerecht und sein Widerstand senkrecht darüber.
--- falsch
Die Leistung, die das Eintor abgibt, abhängig von der Last. Im Diagramm steht der Lastwiderstand waagerecht und die abgegebene Leistung senkrecht.
:::
:::karte formel Zählpfeile am Eintor
Wie sind Klemmenspannung $U_\mathrm{AB}$ und Klemmenstrom $I_\mathrm{A}$ eines Eintors in diesem Kapitel gezählt, und wann gibt das Eintor Leistung ab?
---
$U_\mathrm{AB}=\varphi_\mathrm{A}-\varphi_\mathrm{B}$ zählt von A nach B, $I_\mathrm{A}$ aus der Klemme A heraus. Für das Eintor sind das Erzeuger-Zählpfeile, für die Last Verbraucher-Zählpfeile. Sind beide Größen positiv, gibt das Eintor Leistung ab.
--- falsch
$U_\mathrm{AB}=\varphi_\mathrm{A}-\varphi_\mathrm{B}$ zählt von A nach B, $I_\mathrm{A}$ in die Klemme A hinein. Für das Eintor sind das Verbraucher-Zählpfeile. Sind beide Größen positiv, gibt das Eintor Leistung ab.
--- falsch
$U_\mathrm{AB}=\varphi_\mathrm{B}-\varphi_\mathrm{A}$ zählt von B nach A, $I_\mathrm{A}$ aus der Klemme A heraus. Für das Eintor sind das Erzeuger-Zählpfeile. Sind beide Größen positiv, nimmt das Eintor Leistung auf.
--- falsch
$U_\mathrm{AB}=\varphi_\mathrm{A}-\varphi_\mathrm{B}$ zählt von A nach B, $I_\mathrm{A}$ aus A heraus. Für Eintor und Last gelten dieselben Pfeile; ob das Eintor Leistung abgibt, zeigen die Vorzeichen nicht, nur sein Aufbau mit oder ohne Quelle.
:::
:::karte begriff Leerlauf und Kurzschluss
Was bedeuten Leerlauf und Kurzschluss an den Klemmen eines Eintors, und welche Größe ist dabei jeweils null?
---
Im Leerlauf sind die Klemmen offen, es fließt kein Klemmenstrom: $I_\mathrm{A}=0$. Im Kurzschluss sind die Klemmen durch einen Draht verbunden, die Klemmenspannung ist null: $U_\mathrm{AB}=0$.
--- falsch
Im Leerlauf ist keine Quelle im Eintor wirksam, deshalb ist $U_\mathrm{AB}=0$. Im Kurzschluss sind die Klemmen durch einen Draht verbunden, durch den kein Strom fließt: $I_\mathrm{A}=0$.
--- falsch
Im Leerlauf sind die Klemmen offen, also sind Strom und Spannung null: $I_\mathrm{A}=0$ und $U_\mathrm{AB}=0$. Im Kurzschluss werden beide Größen unbegrenzt groß.
--- falsch
Im Leerlauf sind die Klemmen durch einen Draht verbunden: $U_\mathrm{AB}=0$. Im Kurzschluss sind die Klemmen offen, weil die Leitung durchgebrannt ist: $I_\mathrm{A}=0$.
:::
:::karte begriff linear
Wann nennt man ein Bauteil linear, und unter welcher Bedingung ist ein Widerstand linear?
---
Wenn sein Strom proportional zu seiner Spannung ist. Ein Widerstand ist linear, solange $R$ nicht vom Strom abhängt; seine Kennlinie ist dann eine Gerade durch den Ursprung. Glühlampe und Diode sind es nicht.
--- falsch
Wenn sein Widerstand gleichmäßig mit dem Strom wächst. Ein Widerstand ist linear, solange $R$ proportional zum Strom ist; seine Kennlinie ist dann eine Gerade durch den Ursprung. Eine Glühlampe ist das Musterbeispiel.
--- falsch
Wenn seine beiden Anschlüsse auf einer Linie liegen, also an gegenüberliegenden Enden. Ein Widerstand ist deshalb immer linear, gleich ob $R$ vom Strom abhängt oder nicht.
--- falsch
Wenn sein Strom proportional zum Quadrat seiner Spannung ist. Ein Widerstand ist linear, solange er sich dabei erwärmt; seine Kennlinie ist eine Parabel durch den Ursprung.
:::
:::karte formel Parallelzeichen
Wofür steht das Zeichen $\parallel$ in einem Ausdruck wie $R_1\parallel R_2$, und wie bindet es im Vergleich zum Plus?
---
Für den Widerstand der Parallelschaltung: $R_1\parallel R_2=\frac{R_1R_2}{R_1+R_2}$. Es bindet stärker als das Plus, wie die Punktrechnung.
--- falsch
Für den Widerstand der Parallelschaltung: $R_1\parallel R_2=\frac{R_1R_2}{R_1+R_2}$. Es bindet schwächer als das Plus, also bedeutet $R_\mathrm{a}+R_\mathrm{b}\parallel R_\mathrm{c}$ dasselbe wie $(R_\mathrm{a}+R_\mathrm{b})\parallel R_\mathrm{c}$.
--- falsch
Für den Widerstand der Parallelschaltung: $R_1\parallel R_2=R_1+R_2$. Es bindet schwächer als das Plus, man rechnet es deshalb immer erst zum Schluss.
--- falsch
Für die Aussage, dass zwei Widerstände gleich groß sind: $R_1\parallel R_2$ heißt $R_1=R_2$. Es ist kein Rechenzeichen und hat deshalb keinen Vorrang vor dem Plus.
:::
::::
