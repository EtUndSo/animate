---
title: Stufe 1: Strom ist bewegte Ladung
pfad: Elektrotechnik / 1. Semester / ET1 – Grundgebiete der Elektrotechnik 1: Einführung in die Schaltungsanalyse / Strom, Widerstand und Kirchhoff
adresse: elektrotechnik/1-semester/grundlagen-der-elektrotechnik/strom-widerstand-und-kirchhoff
knoten: Kapitel 2: Strom, Widerstand und Kirchhoff
order: 1120200
summary: Kapitel 1 hat Ladungen betrachtet, die ruhen oder einzeln fliegen.
tags: Ladungsdichte, Stromstärke, Stromkreis, stationär
lang: de
---

<span class="anker" id="stufe-1"></span>

:::zweck
[Kapitel 1](/wissen/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/ladung-feld-und-potenzial/ladung-feld-und-potenzial.html) hat Ladungen betrachtet, die ruhen oder einzeln fliegen. In einem Draht bewegen sich unzählige Ladungen gemeinsam. Diese Stufe gibt dieser Bewegung zwei Maße.
:::

**Die Idee.** Man stellt sich an eine Stelle des Leiters und misst, wie viel Ladung je Sekunde vorbeikommt. Das hängt von drei Dingen ab: wie dicht die Ladung sitzt, wie schnell sie läuft und wie groß der Querschnitt ist. In der Zeit $\Delta t$ kommt genau die Ladung durch die Fläche, die vorher höchstens den Weg $v\,\Delta t$ entfernt war (Abb. [1](#abb-1)).

:::abbildung et1/k2strom 1
Ladungsträger mit der Geschwindigkeit $v$ in einem Leiter. Alle Ladung im getönten Stück läuft in der Zeit $\Delta t$ durch die Fläche $A$. Das Stück hat das Volumen $A\,v\,\Delta t$.
:::

:::definition Definition 1.1 (Strom und Stromdichte)
<span class="anker" id="satz-1-1"></span>

Die __Ladungsdichte__ $q=\Delta Q/\Delta V$ ist die Ladung je Volumen. Die __Stromstärke__ (kurz Strom) ist die Ladung, die je Zeit durch eine Fläche läuft. Die Stromdichte ist der Strom je Fläche:

<span class="anker" id="gl-1-1"></span>
<span class="anker" id="gl-1-2"></span>
$$\begin{aligned} i&=\lim_{\Delta t\to0}\frac{\Delta Q}{\Delta t}=\frac{\mathrm{d} Q}{\mathrm{d} t},\qquad I=q\,v\,A,\qquad [I]=\mathrm{C/s}=\mathrm A,\\ j&=\frac IA=q\,v,\qquad\vec j=q\,\vec v. \end{aligned} \tag{1.1|1.2}$$
:::

⁠**So liest man das:** $i$ ist der zeitabhängige Strom, $I$ der zeitlich konstante, in Ampere: 3 mA im Rechenmodell, 20 mA in einer Leuchtdiode, 16 A in einer Hausleitung. $q$ hat die Einheit $\mathrm{C/m^3}$. Für die freien Elektronen im Kupfer ist $q=-n\,e=-1{,}36\cdot10^{10}\,\mathrm{C/m^3}$. $j$ hat die Einheit $\mathrm{A/m^2}$, Hausleitungen führen rund $10\,\mathrm{A/mm^2}$. Der Vektor $\vec j$ zeigt für $q>0$ in Richtung von $\vec v$, für $q<0$ entgegengesetzt. **Gültigkeit:** $I=q\,v\,A$ setzt voraus, dass $q$ und $v$ über $A$ gleich sind und $v$ senkrecht auf $A$ steht.

:::herleitung Strom aus Dichte und Geschwindigkeit
Die Fläche sei $A=\Delta x\,\Delta y$. Das getönte Stück hat das Volumen $\Delta V=\Delta x\,\Delta y\,\Delta z$ mit $\Delta z=v\,\Delta t$. Es enthält die Ladung $\Delta Q=q\,\Delta V=q\,A\,v\,\Delta t$, die in der Zeit $\Delta t$ durch $A$ läuft. Also ist $\Delta Q/\Delta t=q\,v\,A$.
:::

**Wann fließt dauerhaft Strom?** Zwei Bedingungen müssen erfüllt sein. Erstens braucht der Kreis eine Quelle, etwa eine Batterie oder ein Netzteil. Sie liefert Energie, keine Ladung: Die Ladungsträger sitzen schon im Leiter, die Quelle treibt sie nur im Kreis herum. Zweitens muss der __Stromkreis__ geschlossen sein, also ein Weg, der in sich zurückläuft. An einer Unterbrechung staut sich sonst Ladung, ihr Feld hebt das antreibende Feld auf, und der Strom endet. Ein zeitlich konstanter Strom im geschlossenen Kreis heißt __stationär__.

::::beispiel
Im Rechenmodell laufen 3 mC je Sekunde durch den Draht, das sind $3\,\mathrm{mC}/e=1{,}87\cdot10^{16}$ Elektronen. Die Stromdichte ist $j=3\,\mathrm{mA}/0{,}5\,\mathrm{mm^2}=6\,\mathrm{mA/mm^2}$. Ein Meter Draht enthält die freie Ladung $n\,e\,A=6800$ C. Die gesamte Ladung, die eine Blockbatterie in ihrem Leben umsetzt (rund 1800 C), steckt also schon in 26 cm dieses Drahts. **Kontrolle:** Für $v=0$ ist $I=0$, gleichgültig wie viel Ladung im Draht sitzt. Doppelte Fläche bei gleichem $v$ ergibt doppelten Strom, denn es sind zwei Drähte nebeneinander.
::::

:::frage Werden die Elektronen im Verbraucher verbraucht?
Nein. Ladung bleibt erhalten, aus einem Bauteil kommen je Sekunde so viele Elektronen heraus, wie hineinlaufen. Verbraucht wird Energie: Jedes Coulomb gibt seine Energie je Ladung, die Spannung, an das Bauteil ab und läuft auf niedrigerem Potenzial weiter.
:::

:::aufgabe Aufgabe 1 ★ Strom, Ladung, Stromdichte
<span class="anker" id="aufg-1"></span>

<ol class="al">

<li>

Eine Leuchtdiode führt 5 min lang 20 mA. Wie viel Ladung läuft durch sie, wie viele Elektronen sind das?

</li>

<li>

Ein Kabel mit $1{,}5\,\mathrm{mm^2}$ Querschnitt führt 16 A. Wie groß ist $j$ in $\mathrm{A/mm^2}$?

</li>

<li>

In welche Richtung zeigt $\vec j$ in einem Draht, in dem Elektronen nach rechts laufen?

</li>

</ol>

:::loesung
(a) $Q=I\,t=20\,\mathrm{mA}\cdot300\,\mathrm{s}=6$ C, das sind $6\,\mathrm{C}/e=3{,}7\cdot10^{19}$ Elektronen. (b) $j=16\,\mathrm{A}/1{,}5\,\mathrm{mm^2}=10{,}7\,\mathrm{A/mm^2}$. (c) Nach links: Für Elektronen ist $q<0$, also zeigt $\vec j=q\,\vec v$ gegen $\vec v$.
:::
:::

::::formelsammlung
**Ladungsdichte**

$$q=\Delta Q/\Delta V$$

Ladung je Volumen, Einheit $\mathrm{C/m^3}$. Für die freien Elektronen eines Metalls mit der Elektronendichte $n$ ist $q=-n\,e$.

**Stromstärke**

$$i=\lim_{\Delta t\to0}\frac{\Delta Q}{\Delta t}=\frac{\mathrm{d} Q}{\mathrm{d} t},\qquad [I]=\mathrm{C/s}=\mathrm A$$

Ladung, die je Zeit durch eine Fläche läuft; $i$ zeitabhängig, $I$ zeitlich konstant. Dauerhaft fließt Strom nur mit einer Quelle in einem geschlossenen Stromkreis; zeitlich konstant heißt er stationär.

**Strom aus Dichte und Geschwindigkeit**

$$I=q\,v\,A$$

Ladungsdichte $q$, Geschwindigkeit $v$ der Ladungsträger, Querschnittsfläche $A$. Gilt, wenn $q$ und $v$ über $A$ gleich sind und $v$ senkrecht auf $A$ steht.

**Stromdichte**

$$j=\frac IA=q\,v,\qquad\vec j=q\,\vec v$$

Strom je Fläche, Einheit $\mathrm{A/m^2}$. $\vec j$ zeigt für $q>0$ in Richtung von $\vec v$, für $q<0$ entgegengesetzt.
::::

::::lernkarten
:::karte begriff Stromstärke
Was gibt die Stromstärke in einem Leiter an, und in welcher Einheit misst man sie?
---
Die Ladung, die je Zeit durch eine Fläche läuft: $i=\mathrm{d} Q/\mathrm{d} t$, Einheit Ampere, $[I]=\mathrm{C/s}=\mathrm A$. Kurz heißt sie Strom.
--- falsch
Die Ladung, die insgesamt im Leiter sitzt, gemessen in Coulomb. Je mehr freie Ladung ein Draht enthält, desto größer ist sein Strom.
--- falsch
Die Geschwindigkeit, mit der die Ladungsträger durch den Leiter laufen, gemessen in Meter je Sekunde. Kurz heißt sie Strom.
--- falsch
Die Energie, die je Zeit durch eine Fläche läuft: $i=\mathrm{d} W/\mathrm{d} t$, Einheit Ampere, $[I]=\mathrm{J/s}=\mathrm A$. Kurz heißt sie Strom.
:::
:::karte begriff Ladungsdichte
Was gibt die Ladungsdichte $q$ an, mit der man den Strom in einem Leiter berechnet?
---
Die Ladung je Volumen, $q=\Delta Q/\Delta V$, Einheit $\mathrm{C/m^3}$. Für die freien Elektronen im Kupfer ist $q=-n\,e$, also negativ.
--- falsch
Die Ladung je Querschnittsfläche, $q=\Delta Q/A$, Einheit $\mathrm{C/m^2}$. Für die freien Elektronen im Kupfer ist sie positiv.
--- falsch
Die Zahl der freien Elektronen je Volumen, $q=n$, Einheit $\mathrm{m^{-3}}$. Sie ist immer positiv, auch für Elektronen.
--- falsch
Die Ladung, die je Sekunde durch ein Volumen läuft, Einheit $\mathrm{A/m^3}$. Sie ist ein Maß dafür, wie stark der Strom ist.
:::
:::karte begriff Stromdichte
Was gibt die Stromdichte $j$ an, und wie hängt sie mit Ladungsdichte und Geschwindigkeit zusammen?
---
Den Strom, der je Querschnittsfläche durch den Leiter läuft: $j=\frac IA=q\,v$, Einheit $\mathrm{A/m^2}$. Als Vektor ist $\vec j=q\,\vec v$.
--- falsch
Den Strom je Querschnittsfläche: $j=I\,A=q\,v$, Einheit $\mathrm{A\,m^2}$. Ein dickerer Draht hat bei gleichem Strom die größere Stromdichte.
--- falsch
Den Strom je Länge des Leiters: $j=I/L$, Einheit $\mathrm{A/m}$. Je länger der Draht, desto kleiner ist seine Stromdichte.
--- falsch
Die Ladung je Volumen mal Querschnitt: $j=q\,A$, Einheit $\mathrm{C/m}$. Sie hängt nicht von der Geschwindigkeit der Ladung ab.
:::
:::karte begriff Stromkreis und stationär
Was ist ein Stromkreis, und wann heißt der Strom darin stationär?
---
Ein Weg für den Strom, der in sich zurückläuft. Stationär heißt ein zeitlich konstanter Strom in einem solchen geschlossenen Kreis.
--- falsch
Jede Verbindung von einer Quelle zu einem Verbraucher, auch ohne Rückweg. Stationär heißt ein Strom, der nur in eine Richtung fließt.
--- falsch
Ein Weg für den Strom, der in sich zurückläuft. Stationär heißt ein Strom, dessen Ladungsträger im Leiter ruhen und nicht driften.
--- falsch
Ein Weg, auf dem die Quelle Ladung abgibt, die im Verbraucher bleibt. Stationär heißt ein Strom, der langsam und gleichmäßig fließt.
:::
:::karte formel Strom aus Dichte und Geschwindigkeit
Wie hängt der Strom $I$ in einem Leiter von Ladungsdichte, Geschwindigkeit und Querschnitt ab?
---
$I=q\,v\,A$: Ladungsdichte mal Geschwindigkeit mal Querschnittsfläche. Es gilt, wenn $q$ und $v$ über $A$ gleich sind und $v$ senkrecht auf $A$ steht.
--- falsch
$I=q\,v/A$: Ladungsdichte mal Geschwindigkeit, geteilt durch die Querschnittsfläche. Ein dünnerer Draht führt bei gleichem $q$ und $v$ deshalb mehr Strom.
--- falsch
$I=q\,A/v$: Ladungsdichte mal Querschnittsfläche, geteilt durch die Geschwindigkeit. Langsamere Ladung verweilt länger an der Fläche und ergibt mehr Strom.
--- falsch
$I=q\,v\,A$: Ladungsdichte mal Geschwindigkeit mal Querschnittsfläche. Es gilt für jede Richtung von $v$, auch wenn $v$ parallel zur Fläche $A$ liegt.
:::
:::karte herleitung Strom aus Dichte und Geschwindigkeit
Leite aus der Ladungsdichte $q$ und der Geschwindigkeit $v$ der Ladungsträger her, dass durch eine Fläche $A$ der Strom $I=q\,v\,A$ fließt.
---
In der Zeit $\Delta t$ läuft genau die Ladung durch $A$, die vorher höchstens den Weg $v\,\Delta t$ entfernt war, weil sie sich mit der Geschwindigkeit $v$ auf die Fläche zubewegt.
---
Mit $A=\Delta x\,\Delta y$ hat dieses Stück das Volumen $\Delta V=\Delta x\,\Delta y\,\Delta z$ mit $\Delta z=v\,\Delta t$, weil es die Fläche $A$ um den Weg $v\,\Delta t$ nach hinten verlängert.
---
Es enthält die Ladung $\Delta Q=q\,\Delta V=q\,A\,v\,\Delta t$, weil die Ladungsdichte die Ladung je Volumen ist.
---
Also ist $\Delta Q/\Delta t=q\,v\,A$, weil der Strom die Ladung je Zeit ist, die durch die Fläche läuft.
:::
:::karte zusammenhang Richtung der Stromdichte
In welche Richtung zeigt die Stromdichte $\vec j$ in einem Draht, in dem Elektronen nach rechts laufen, und warum?
---
Nach links: Für Elektronen ist $q<0$, deshalb zeigt $\vec j=q\,\vec v$ entgegen ihrer Geschwindigkeit $\vec v$, also gegen ihre Laufrichtung.
--- falsch
Nach rechts, weil $\vec j=q\,\vec v$ immer in die Bewegungsrichtung der Ladungsträger zeigt, gleich welches Vorzeichen sie tragen.
--- falsch
Quer zum Draht, weil die Stromdichte durch die Querschnittsfläche zeigt und nicht längs des Leiters.
--- falsch
Sie hat keine Richtung, weil die Stromdichte wie der Strom eine Zahl ist; bei Elektronen ist nur ihr Vorzeichen negativ.
:::
:::karte zusammenhang Ruhende Ladungsträger
Warum fließt kein Strom, wenn die Ladungsträger im Mittel ruhen, obwohl ein Meter Draht 6800 C freie Ladung enthält?
---
Weil der Strom nach $I=q\,v\,A$ auch von der Geschwindigkeit abhängt: Für $v=0$ ist $I=0$, gleichgültig wie viel Ladung im Draht sitzt.
--- falsch
Weil 6800 C zu wenig sind: Ein messbarer Strom braucht mehr Ladung, als in einem Meter Draht steckt, also einige Meter mehr.
--- falsch
Weil der Strom nur vom Querschnitt abhängt: Ein dünner Draht führt keinen Strom, gleichgültig wie viel Ladung in ihm sitzt.
--- falsch
Weil sich die freie Ladung im Draht ständig neu bildet und wieder verschwindet. Im Mittel ist sie deshalb null und trägt keinen Strom.
:::
:::karte zusammenhang Unterbrochener Stromkreis
Warum endet der Strom, wenn der Stromkreis an einer Stelle unterbrochen ist?
---
Weil sich an der Unterbrechung Ladung staut. Ihr Feld hebt das antreibende Feld auf, und die Ladungsträger kommen zur Ruhe.
--- falsch
Weil die Quelle ihre Ladung nur in einen geschlossenen Kreis abgeben kann. Ohne Rückweg bleiben ihre Ladungsträger in ihr.
--- falsch
Weil die Ladungsträger an der Unterbrechung verbraucht werden. Ohne Rückweg kommen keine neuen nach, und der Leiter wird leer.
--- falsch
Weil an der Unterbrechung die Spannung der Quelle verschwindet. Ohne geschlossenen Kreis baut die Quelle gar keine Spannung auf.
:::
:::karte zusammenhang Was ein Verbraucher verbraucht
Was wird in einem Verbraucher verbraucht, wenn Strom durch ihn fließt, und was liefert die Quelle?
---
Energie, nicht Ladung: Aus dem Bauteil kommen je Sekunde so viele Elektronen heraus, wie hineinlaufen. Die Quelle liefert Energie; die Ladungsträger sitzen schon im Leiter.
--- falsch
Ladung: Ein Teil der Elektronen bleibt im Bauteil zurück, deshalb kommen je Sekunde weniger heraus, als hineinlaufen. Die Quelle muss laufend neue Elektronen in den Leiter nachliefern.
--- falsch
Strom: Hinter dem Verbraucher ist der Strom kleiner als davor, weil das Bauteil ihn für seine Arbeit aufnimmt. Die Quelle liefert den Strom.
--- falsch
Spannung und Ladung zugleich: Die Elektronen geben im Bauteil ihre Ladung ab und laufen ungeladen zur Quelle zurück, die sie neu auflädt.
:::
::::
