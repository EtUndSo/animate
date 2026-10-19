---
title: Das Spektrum eines Signals
pfad: Elektrotechnik / 1. Semester / Mathematische Methoden der Elektrotechnik / Spektrum und Fourier-Reihe
order: 20100
summary: Von Grund auf – wie man ein Signal nicht über der Zeit, sondern nach seinen Frequenzanteilen beschreibt, warum man die „Zutaten" einer Kurve nicht ansehen kann und das Spektrum sie sichtbar macht, und warum ein einzelner reeller Ton immer zwei Spektrallinien erzeugt.
tags: Spektrum, Frequenzbereich, Summe von Sinussignalen, Spektrallinien, negative Frequenz, zweiseitiges Spektrum
---

:::grafik
Einstiegs-Animation: Oben läuft eine zunächst „wild" aussehende Zeitkurve $x(t)$. Wie durch ein Prisma wird sie
langsam in ihre Bestandteile zerlegt — einzelne, saubere Kosinusschwingungen gleiten heraus und stapeln sich.
Darunter erscheint parallel das Ergebnis: ein Diagramm über der **Frequenz**, in dem für jede enthaltene
Schwingung genau eine senkrechte Linie steht (Höhe = Stärke). Kernbotschaft: Eine komplizierte Zeitkurve ist oft
nur eine Summe weniger einfacher Töne — und das **Spektrum** macht diese Zutaten sichtbar.
:::

:::konzept
Jedes Signal lässt sich auf zwei Arten anschauen:

- über der **Zeit** — wie es in jedem Augenblick schwingt (die gewohnte Kurve),
- über der **Frequenz** — aus welchen Schwingungen es zusammengesetzt ist.

Die zweite Sicht ist das **Spektrum**. So wie ein Prisma weißes Licht in seine Farben zerlegt, zerlegt das
Spektrum ein Signal in seine Sinusanteile und zeigt für jeden, wie stark er ist. Oft ist diese Sicht viel
einfacher als die Zeitkurve: Ein kompliziert aussehendes Signal besteht häufig nur aus wenigen Frequenzen.
:::

**Worum es geht:** Einen einzelnen Zeiger (voriger Abschnitt) kennen wir — er beschreibt *eine* Frequenz. Jetzt
setzen wir Signale aus **mehreren** Frequenzen zusammen und führen den __Frequenzbereich__ ein: die Beschreibung
eines Signals durch sein __Spektrum__.

## Ein Signal aus mehreren Frequenzen

Die Grundidee ist einfach: Man addiert mehrere Sinusschwingungen verschiedener Frequenzen. Jede einzelne ist
eine saubere Kosinuskurve mit ihren drei Kenngrößen (Amplitude, Frequenz, Phase); zusammen ergeben sie ein
komplizierteres Signal:

$$x(t) = A_0 + \sum_{k} A_k\,\cos(2\pi f_k\,t + \varphi_k).$$

- __$A_0$__: der __Gleichanteil__ — der konstante Mittelwert (die „Schwingung" mit Frequenz null).
- __$A_k$__: die __Amplitude__ der $k$-ten Teilschwingung.
- __$f_k$__: deren __Frequenz__.
- __$\varphi_k$__: deren __Phase__.

Umgekehrt gelesen ist das die zentrale Aussage: Fast jedes interessante Signal lässt sich so zerlegen. Das
__Spektrum__ ist dann nichts anderes als die **vollständige Zutatenliste** — für jede vorkommende Frequenz die
zugehörige Amplitude und Phase.

:::grafik
Animation „Signal aufbauen": Start mit einer einzelnen Kosinuskurve. Schritt für Schritt kommt je eine weitere
Schwingung anderer Frequenz hinzu; die Summenkurve wird mit jedem Summanden „welliger" und verliert ihre
offensichtliche Einfachheit. Parallel wächst im Frequenzdiagramm bei jeder neuen Schwingung genau eine Linie
hinzu. Sichtbar: Die Zeitkurve wird unübersichtlich, das Spektrum bleibt übersichtlich (wenige Linien).
:::

## Zeit- und Frequenzbereich: zwei Sichten, dieselbe Information

Zeitkurve und Spektrum enthalten **genau dieselbe** Information, nur anders geordnet:

- Der __Zeitbereich__ beantwortet: „Was macht das Signal in jedem Augenblick?"
- Der __Frequenzbereich__ beantwortet: „Woraus ist es zusammengesetzt?"

**Warum nicht einfach bei der Zeitkurve bleiben?** Weil man einer Zeitkurve ihre Zutaten **nicht ansieht**.
Blickt man auf ein welliges Signal, kann man nicht erkennen, welche Frequenzen darin stecken und wie stark —
genau diese Frage beantwortet das Spektrum direkt. Und für viele Aufgaben ist die Frequenzsicht die einzig
bequeme: Beim **Filtern** etwa will man gezielt bestimmte Frequenzanteile abschwächen; im Zeitbereich ist das
kaum zu fassen, im Frequenzbereich bedeutet es schlicht „diese Linien kleiner machen".

**Zweite Sichtweise (Analogie):** Ein Akkord auf dem Klavier ist im Zeitbereich eine unübersichtlich zappelnde
Druckkurve, im Frequenzbereich aber einfach drei scharfe Linien bei den drei Tonhöhen. Das Spektrum macht die
verborgene Einfachheit sichtbar.

:::grafik
Dasselbe Signal in zwei gekoppelten Diagrammen nebeneinander: links die Zeitkurve $x(t)$ (wellig), rechts das
Frequenzdiagramm mit wenigen Linien. Ein Pfeil „Zeitbereich ⇄ Frequenzbereich" betont, dass beide dieselbe
Information tragen.
:::

## Die Spektrallinien: Amplituden- und Phasenspektrum

Man zeichnet das Spektrum als __Spektrallinien__: An jeder vorkommenden Frequenz $f_k$ steht eine senkrechte
Linie. Weil jede Teilschwingung **zwei** Angaben hat (Amplitude und Phase), braucht man genau genommen zwei
Diagramme:

- das __Amplitudenspektrum__ — Linienhöhe = Amplitude $A_k$ (wie stark),
- das __Phasenspektrum__ — Linienhöhe = Phase $\varphi_k$ (wie verschoben),

jeweils über der Frequenz aufgetragen. Der Gleichanteil $A_0$ erscheint als Linie bei $f = 0$.

:::grafik
Übereinander das Amplitudenspektrum (Linien der Höhe $A_0, A_1, A_2, \ldots$ an den Frequenzen $0, f_1, f_2,
\ldots$) und das Phasenspektrum (Linien der Höhe $\varphi_1, \varphi_2, \ldots$ an denselben Frequenzen). Achsen
beschriftet (Frequenz waagerecht).
:::

## Positive und negative Frequenzen: das zweiseitige Spektrum

Jetzt ein Punkt, der zunächst überrascht, sich aber direkt herleiten lässt. Wir haben im vorigen Abschnitt
gesehen, dass ein Kosinus die Summe **zweier** gegenläufig rotierender Zeiger ist. Schreiben wir das sauber auf.

**Schritt 1** — umgekehrte Eulersche Formel: Für jeden Winkel gilt $\cos\alpha = \tfrac{1}{2}\big(e^{j\alpha} +
e^{-j\alpha}\big)$.

**Schritt 2** — einsetzen mit $\alpha = 2\pi f t + \varphi$ und die Phase in eine komplexe Amplitude
$\underline{X} = A\,e^{j\varphi}$ ziehen:

$$A\cos(2\pi f t + \varphi) = \tfrac{1}{2}\,\underline{X}\,e^{\,j2\pi f t} + \tfrac{1}{2}\,\underline{X}^{*}\,e^{-j2\pi f t}.$$

**Schritt 3** — ablesen: Der erste Summand ist ein Zeiger, der mit der **positiven** Frequenz $+f$ rotiert, der
zweite einer mit der **negativen** Frequenz $-f$. Ein einzelner reeller Ton erzeugt im Spektrum also **zwei**
Linien: eine bei $+f$ und eine bei $-f$, jede mit der halben Amplitude, und ihre komplexen Amplituden sind
zueinander **konjugiert** ($\tfrac12\underline{X}$ und $\tfrac12\underline{X}^*$). Das nennt man das
__zweiseitige Spektrum__.

**Was ist eine „negative Frequenz"?** Sie ist kein eigenständig erzeugbarer Ton, sondern die **mathematische
Begleiterin**: der im Uhrzeigersinn rotierende Zeiger, der zusammen mit seinem gegenläufigen Partner den
Imaginärteil aufhebt und so ein **reelles** Signal ergibt. Dass die negativen Linien immer die konjugierten
Spiegelbilder der positiven sind, ist genau das Erkennungszeichen eines reellen Signals.

:::grafik
Oben das zweiseitige Amplitudenspektrum eines einzelnen Kosinus: zwei gleich hohe Linien der Höhe $\tfrac{A}{2}$
bei $+f$ und $-f$, symmetrisch zur Frequenz null. Unten die Deutung als Animation: zwei gegenläufig rotierende
Zeiger ($\tfrac12\underline{X}$ gegen den Uhrzeigersinn, $\tfrac12\underline{X}^*$ im Uhrzeigersinn), deren Summe
in jedem Moment auf der reellen Achse bleibt (rein reell).
:::

**Einseitig oder zweiseitig?** Beide Darstellungen sind gebräuchlich:

- **Zweiseitig** ($-f$ und $+f$): mathematisch die „ehrliche" Form, passt zur komplexen Rechnung.
- **Einseitig** (nur $f \ge 0$): Man fasst die beiden Linien zusammen und verdoppelt die Amplitude — anschaulicher
  für die Praxis.

Man muss nur wissen, welche man gerade benutzt.

**Stolperstein:** Zeichnet man das Spektrum eines Kosinus nur mit der Linie bei $+f$, ist es im zweiseitigen Bild
**unvollständig** — die konjugierte Linie bei $-f$ gehört zwingend dazu, sonst wäre das Signal nicht reell.

:::kern
Das __Spektrum__ beschreibt ein Signal im __Frequenzbereich__: als Summe von Sinusanteilen $x(t) = A_0 + \sum_k
A_k\cos(2\pi f_k t + \varphi_k)$, dargestellt durch __Spektrallinien__ (Amplitude und Phase je Frequenz). Zeit-
und Frequenzbereich tragen dieselbe Information — aber die Zutaten sieht man nur im Spektrum. Ein reeller Ton
ergibt im __zweiseitigen Spektrum__ zwei Linien bei $+f$ und $-f$ mit halber Amplitude und zueinander
__konjugierten__ komplexen Amplituden; die __negative Frequenz__ ist die konjugierte Begleiterin, die das Signal
reell macht (herleitbar aus $\cos\alpha = \tfrac12(e^{j\alpha}+e^{-j\alpha})$).
:::

Bisher durften die Frequenzen $f_k$ beliebig sein. Bei einem **periodischen** Signal sind sie nicht beliebig,
sondern ganzzahlige Vielfache einer Grundfrequenz. Wie man ein beliebiges periodisches Signal in genau diese
Oberschwingungen zerlegt, beschreibt die __Fourier-Reihe__ — das nächste Thema.
