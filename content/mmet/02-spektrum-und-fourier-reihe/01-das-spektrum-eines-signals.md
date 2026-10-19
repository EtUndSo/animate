---
title: Das Spektrum eines Signals
pfad: Elektrotechnik / 1. Semester / Mathematische Methoden der Elektrotechnik / Spektrum und Fourier-Reihe
order: 20100
summary: Wie man ein Signal nicht über der Zeit, sondern über der Frequenz betrachtet – als Summe von Sinusanteilen – und warum ein reeller Ton immer zwei Spektrallinien bei positiver und negativer Frequenz erzeugt.
tags: Spektrum, Frequenzbereich, Summe von Sinussignalen, Spektrallinien, negative Frequenz, zweiseitiges Spektrum
---

:::konzept
Ein Signal lässt sich auf zwei Arten betrachten: über der **Zeit** (wie es schwingt) oder über der **Frequenz**
(aus welchen Tönen es zusammengesetzt ist). Die zweite Sicht ist das **Spektrum**. So wie ein Prisma weißes
Licht in seine Farben zerlegt, zerlegt das Spektrum ein Signal in seine Sinusanteile — und zeigt für jeden, wie
stark (Amplitude) und wie verschoben (Phase) er ist. Oft ist diese Darstellung viel einfacher als die
Zeitkurve: Ein kompliziert aussehendes Signal besteht häufig aus nur wenigen Frequenzen.
:::

**Worum es geht:** Ein einzelner Zeiger beschreibt eine Frequenz (voriger Abschnitt). Jetzt setzen wir Signale
aus **mehreren** Frequenzen zusammen und führen den __Frequenzbereich__ ein — die Beschreibung eines Signals
durch sein __Spektrum__.

## Ein Signal als Summe von Sinussignalen

Die Grundidee: Fast jedes interessante Signal lässt sich als Summe von Sinusschwingungen verschiedener Frequenzen
schreiben,

$$x(t) = A_0 + \sum_{k} A_k\,\cos(2\pi f_k\,t + \varphi_k).$$

- __$A_0$__: der __Gleichanteil__ (Mittelwert, die Frequenz-null-Komponente).
- __$A_k$__: die __Amplitude__ der $k$-ten Teilschwingung.
- __$f_k$__: deren __Frequenz__.
- __$\varphi_k$__: deren __Phase__.

Jeder Summand ist eine reine Sinusschwingung mit ihren drei Kenngrößen. Das __Spektrum__ ist nun schlicht die
**Liste all dieser Anteile** — für jede vorkommende Frequenz $f_k$ ihre Amplitude und Phase. Man zeichnet es als
__Spektrallinien__: an jeder Frequenz ein senkrechter Strich, dessen Höhe die Amplitude angibt (das
__Amplitudenspektrum__), dazu getrennt die Phase (das __Phasenspektrum__).

:::grafik
Oben ein zusammengesetztes Zeitsignal $x(t)$ (Summe mehrerer Kosinusschwingungen, sieht „wellig" aus). Darunter
sein Amplitudenspektrum: wenige senkrechte Linien bei den Frequenzen $f_1, f_2, \ldots$, deren Höhen die
Amplituden $A_1, A_2, \ldots$ sind, plus eine Linie bei $f = 0$ der Höhe $A_0$. Ein Pfeil „Zeitbereich →
Frequenzbereich" verbindet beide.
:::

## Zeit- und Frequenzbereich: zwei Sichten auf dasselbe Signal

Zeitkurve und Spektrum enthalten **dieselbe** Information, nur anders geordnet. Der __Zeitbereich__ beantwortet
„was macht das Signal in jedem Augenblick?", der __Frequenzbereich__ „woraus ist es zusammengesetzt?". Für viele
Aufgaben ist die Frequenzsicht die bequemere — etwa beim Filtern, wo man gezielt einzelne Frequenzanteile
abschwächen will.

**Anders betrachtet.** Ein Akkord auf dem Klavier ist im Zeitbereich eine unübersichtlich zappelnde Druckkurve,
im Frequenzbereich aber einfach drei scharfe Linien bei den drei Tonhöhen. Das Spektrum macht die verborgene
Einfachheit sichtbar.

## Positive und negative Frequenzen: das zweiseitige Spektrum

Hier kommt ein Punkt, der zunächst überrascht. Nach der umgekehrten Eulerschen Formel ist jeder reelle Kosinus
die Summe zweier gegenläufig rotierender Zeiger:

$$A\cos(2\pi f t + \varphi) = \tfrac{1}{2}A\,e^{\,j\varphi}\,e^{\,j2\pi f t} + \tfrac{1}{2}A\,e^{-j\varphi}\,e^{-j2\pi f t}.$$

Ein einzelner reeller Ton erzeugt also **zwei** Spektrallinien: eine bei der positiven Frequenz $+f$ und eine
bei der negativen Frequenz $-f$ — jede mit der halben Amplitude, und die beiden komplexen Amplituden sind
zueinander **konjugiert komplex**. Das nennt man das __zweiseitige Spektrum__.

Was bedeutet eine „negative Frequenz"? Sie ist kein eigenständig erzeugbarer Ton, sondern die **mathematische
Begleiterin**: der im Uhrzeigersinn rotierende Zeiger, der zusammen mit seinem gegenläufigen Partner den
Imaginärteil aufhebt und so ein **reelles** Signal ergibt. Dass die negativen Linien immer als konjugierte
Spiegelbilder der positiven auftreten, ist genau das Kennzeichen eines reellen Signals.

:::grafik
Das zweiseitige Amplitudenspektrum eines einzelnen Kosinus: zwei Linien gleicher Höhe $\tfrac{A}{2}$ bei $+f$ und
$-f$, symmetrisch zur Frequenz null. Daneben die Deutung: zwei gegenläufig rotierende Zeiger (gegen und im
Uhrzeigersinn), deren Summe stets reell (auf der reellen Achse) bleibt.
:::

**Stolperstein: die negative Linie nicht vergessen.** Zeichnet man das Spektrum eines Kosinus nur mit der Linie
bei $+f$, ist es unvollständig. Zum reellen Signal gehört immer auch die konjugierte Linie bei $-f$ — sonst wäre
das Signal komplex. In der einseitigen Darstellung (nur $f \ge 0$) fasst man beide zusammen und verdoppelt die
Amplitude; beide Konventionen sind gebräuchlich, man muss nur wissen, welche man gerade benutzt.

:::kern
Das __Spektrum__ beschreibt ein Signal im __Frequenzbereich__ — als Summe von Sinusanteilen
$x(t) = A_0 + \sum_k A_k\cos(2\pi f_k t + \varphi_k)$, dargestellt durch __Spektrallinien__ (Amplitude und Phase
je Frequenz). Zeit- und Frequenzbereich tragen dieselbe Information. Ein reeller Ton erzeugt im __zweiseitigen
Spektrum__ zwei Linien bei $+f$ und $-f$ mit halber Amplitude und zueinander __konjugierten__ komplexen
Amplituden; die __negative Frequenz__ ist die konjugierte Begleiterin, die das Signal reell macht.
:::

Bei einem __periodischen__ Signal sind die Frequenzen nicht beliebig, sondern ganzzahlige Vielfache einer
Grundfrequenz. Wie man ein beliebiges periodisches Signal in genau diese Oberschwingungen zerlegt, beschreibt die
__Fourier-Reihe__.
