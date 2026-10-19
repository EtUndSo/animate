---
title: Zeiger (Phasoren) und Sinussignale
pfad: Elektrotechnik / 1. Semester / Mathematische Methoden der Elektrotechnik / Komplexe Zahlen und Zeiger
order: 10200
summary: Warum ein Sinussignal nichts anderes ist als der Schatten eines rotierenden Zeigers – und wie man mit diesem Phasor das lästige Rechnen mit Sinus und Kosinus in einfache Addition komplexer Zahlen verwandelt.
tags: Sinussignal, Amplitude, Kreisfrequenz, Phase, Phasor, Zeiger, komplexe Amplitude, Zeigeraddition
---

:::konzept
Ein Sinussignal ist der **Schatten eines rotierenden Zeigers**. Stell dir einen Pfeil der Länge $A$ vor, der
sich mit konstanter Geschwindigkeit in der komplexen Ebene dreht. Projiziert man seine Spitze auf die reelle
Achse, wandert dieser Schatten als Kosinuskurve auf und ab. Hält man die Zeit an, ist der Pfeil eine komplexe
Zahl — der **Phasor**. Der ganze Gewinn: Das umständliche Rechnen mit Sinus und Kosinus wird zum einfachen
Addieren von Pfeilen.
:::

**Worum es geht:** Komplexe Zahlen (voriger Abschnitt) treffen auf Schwingungen. Wir beschreiben das
__Sinussignal__ durch seine drei Kenngrößen, fassen es als __Zeiger__ (Phasor) zusammen und sehen, warum sich
gleichfrequente Signale dann durch bloße __Zeigeraddition__ überlagern lassen.

## Das Sinussignal und seine drei Parameter

Ein harmonisches Signal schreibt man in der Signalverarbeitung meist als Kosinus:

$$x(t) = A\,\cos(\omega t + \varphi).$$

- __$A$__: die __Amplitude__ — der Maximalausschlag des Signals.
- __$\omega$__: die __Kreisfrequenz__ in $\text{rad}/\text{s}$, also wie schnell die Schwingung abläuft.
- __$\varphi$__: die __Nullphase__ — der Winkel zum Zeitpunkt $t = 0$, also die „Verschiebung" der Kurve.

Die Kreisfrequenz hängt mit der gewohnten __Frequenz__ $f$ (in Hertz) und der __Periodendauer__ $T$ zusammen
über

$$\omega = 2\pi f = \frac{2\pi}{T}.$$

Drei Zahlen — Amplitude, Frequenz, Phase — legen die Schwingung also vollständig fest.

:::grafik
Eine Kosinuskurve über der Zeit mit markierter Amplitude $A$ (Höhe), Periodendauer $T$ (Abstand zweier Maxima)
und der Phasenverschiebung $\varphi$ (horizontale Verschiebung des ersten Maximums gegenüber $t = 0$).
:::

## Der Zeiger (Phasor)

Bei festem $\omega$ unterscheiden sich zwei Signale nur noch in **Amplitude** und **Phase**. Genau diese beiden
Angaben stecken in einer einzigen komplexen Zahl, dem __Phasor__ (oder __komplexen Amplitude__):

$$\underline{X} = A\,e^{\,j\varphi}.$$

- __$\underline{X}$__: der __Phasor__ — ein ruhender Zeiger mit Länge $A$ und Winkel $\varphi$.
- __$A$__: die __Amplitude__ (Betrag des Zeigers).
- __$\varphi$__: die __Nullphase__ (Winkel des Zeigers).

Die Frequenz $\omega$ taucht im Phasor **nicht** auf — sie wird ausgeklammert, weil in einer Schaltung ohnehin
alle Signale dieselbe Frequenz haben und diese konstant bleibt. Der Phasor speichert also nur das, was sich von
Signal zu Signal unterscheidet: wie groß und wie verschoben.

## Der rotierende Zeiger

Die Zeit kommt über einen rotierenden Faktor wieder ins Spiel. Multipliziert man den Phasor mit $e^{j\omega t}$,
dreht sich der Zeiger mit der Kreisfrequenz $\omega$ gegen den Uhrzeigersinn. Das ursprüngliche reelle Signal ist
dann genau der **Realteil** (die Projektion auf die reelle Achse):

$$x(t) = \operatorname{Re}\!\left\{\underline{X}\,e^{\,j\omega t}\right\} = \operatorname{Re}\!\left\{A\,e^{\,j(\omega t + \varphi)}\right\} = A\cos(\omega t + \varphi).$$

Die letzte Gleichheit ist direkt die Eulersche Formel: Der Realteil von $A\,e^{j(\omega t+\varphi)}$ ist
$A\cos(\omega t+\varphi)$. Anschaulich: Der rotierende Zeiger ist das „volle" komplexe Signal, das reelle
Sinussignal sein Schatten auf der reellen Achse.

**Anders betrachtet.** Man kann das Signal auch als Summe **zweier** gegenläufig rotierender Zeiger sehen, denn
nach der umgekehrten Eulerschen Formel ist $\cos\theta = \tfrac{1}{2}(e^{j\theta} + e^{-j\theta})$. Diese
Zerlegung in eine positive und eine negative Frequenz ist später der Schlüssel zum **Spektrum**.

:::grafik
Links die komplexe Ebene mit dem rotierenden Zeiger $\underline{X}e^{j\omega t}$ (Drehrichtung gegen den
Uhrzeigersinn, Winkelgeschwindigkeit $\omega$). Rechts, zeitlich daneben aufgetragen, die Projektion seiner
Spitze auf die reelle Achse, die als Kosinuskurve $x(t)$ mitwandert — eine Momentlinie verbindet Zeigerspitze
und Kurvenpunkt. (Animation: Zeiger dreht, Kurve entsteht.)
:::

## Summe gleichfrequenter Signale = Zeigeraddition

Hier zahlt sich alles aus. Addiert man mehrere Sinussignale **gleicher Frequenz**, ist das Ergebnis wieder ein
Sinussignal derselben Frequenz — und seinen Phasor bekommt man durch einfache **Addition der Einzelphasoren**:

$$\underline{X}_\text{ges} = \underline{X}_1 + \underline{X}_2 + \ldots$$

Statt Kosinusterme mit verschiedenen Phasen mühsam mit Additionstheoremen zusammenzufassen, legt man einfach die
Zeiger als Pfeile aneinander (Real- und Imaginärteile addieren sich getrennt) und liest Amplitude und Phase des
Summenzeigers ab. Das ist die __Zeigeraddition__ und der eigentliche Grund, warum man in der Wechselstrom- und
Signaltechnik komplex rechnet. Ein weiterer Bonus: Ableiten wird zur Multiplikation mit $j\omega$, Integrieren
zur Division durch $j\omega$ — aus Differentialgleichungen werden algebraische Gleichungen.

:::grafik
Zwei Phasoren $\underline{X}_1$ und $\underline{X}_2$ (gleiche Frequenz, verschiedene Amplitude/Phase) werden
als Pfeile aneinandergehängt; der resultierende Summenzeiger $\underline{X}_\text{ges}$ vom Ursprung zur Spitze
ist hervorgehoben, mit abgelesener Amplitude und Phase. Daneben der Hinweis, dass die drei zugehörigen
Kosinuskurven sich im Zeitbereich genauso überlagern.
:::

**Stolperstein: Sinus oder Kosinus?** Die Phasorlage hängt davon ab, ob man das Signal als Kosinus oder als
Sinus ansetzt. Ein Sinus ist ein um $\tfrac{\pi}{2}$ verschobener Kosinus: $\sin(\omega t) = \cos(\omega t -
\tfrac{\pi}{2})$. Rechnet man konsequent mit **einer** Konvention (meist Kosinus), ist alles stimmig — mischt
man beide, verschieben sich alle Phasen um $90^\circ$. Deshalb immer vorher festlegen, welche Bezugsform gilt.

:::kern
Ein __Sinussignal__ $x(t) = A\cos(\omega t + \varphi)$ hat drei Parameter: __Amplitude__ $A$, __Kreisfrequenz__
$\omega = 2\pi f$ und __Nullphase__ $\varphi$. Bei fester Frequenz steckt alles Unterscheidende im __Phasor__
$\underline{X} = A e^{j\varphi}$ (Frequenz ausgeklammert). Das Signal ist der Realteil des __rotierenden Zeigers__:
$x(t) = \operatorname{Re}\{\underline{X} e^{j\omega t}\}$. Der große Vorteil: __gleichfrequente__ Signale
überlagern sich durch __Zeigeraddition__ ($\underline{X}_\text{ges} = \underline{X}_1 + \underline{X}_2 + \ldots$),
und Ableiten/Integrieren wird zu $\cdot\,j\omega$ bzw. $/\,j\omega$. Konvention Kosinus vs. Sinus konsequent halten.
:::

Ein einzelner Zeiger beschreibt eine einzelne Frequenz. Setzt man ein Signal aus mehreren Frequenzen zusammen,
führt das direkt zum __Spektrum__ — der Darstellung eines Signals nach seinen Frequenzanteilen.
