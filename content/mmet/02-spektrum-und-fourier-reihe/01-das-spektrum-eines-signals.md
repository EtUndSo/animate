---
title: Das Spektrum eines Signals
pfad: Elektrotechnik / 1. Semester / Mathematische Methoden der Elektrotechnik / Spektrum und Fourier-Reihe
order: 20100
summary: Von Grund auf – wie man ein Signal nicht über der Zeit, sondern nach seinen Frequenzanteilen beschreibt, warum man die „Zutaten" einer Kurve nicht ansehen kann und das Spektrum sie sichtbar macht, und warum ein einzelner reeller Ton im zweiseitigen Spektrum immer zwei Linien $a_k$ und $a_{-k}=a_k^*$ erzeugt.
tags: Spektrum, Frequenzbereich, Summe von Sinussignalen, Spektrallinien, negative Frequenz, zweiseitiges Spektrum
---

:::grafik
Einstiegs-Animation: Oben läuft eine zunächst „wild" aussehende Zeitkurve $s(t)$. Wie durch ein Prisma wird sie
langsam in ihre Bestandteile zerlegt — einzelne, saubere Kosinusschwingungen gleiten heraus und stapeln sich.
Darunter erscheint parallel das Ergebnis: ein Diagramm über der **Kreisfrequenz** $\omega$, in dem für jede
enthaltene Schwingung genau eine senkrechte Linie steht (Höhe = Stärke). Kernbotschaft: Eine komplizierte
Zeitkurve ist oft nur eine Summe weniger einfacher Töne — und das **Spektrum** macht diese Zutaten sichtbar.
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

$$s(t) = X_0 + \sum_{k} A_k\,\cos(\omega_k\,t + \varphi_k), \qquad \omega_k = 2\pi f_k.$$

- __$X_0$__: der __Gleichanteil__ — der konstante Mittelwert (die „Schwingung" mit Frequenz null).
- __$A_k$__: die __Amplitude__ der $k$-ten Teilschwingung.
- __$\omega_k$__: deren __Kreisfrequenz__ (gleichwertig die Frequenz $f_k = \omega_k/2\pi$ in Hertz).
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
Dasselbe Signal in zwei gekoppelten Diagrammen nebeneinander: links die Zeitkurve $s(t)$ (wellig), rechts das
Frequenzdiagramm mit wenigen Linien. Ein Pfeil „Zeitbereich ⇄ Frequenzbereich" betont, dass beide dieselbe
Information tragen.
:::

## Die Spektrallinien: Amplituden- und Phasenspektrum

Man zeichnet das Spektrum als __Spektrallinien__: An jeder vorkommenden Kreisfrequenz $\omega_k$ steht eine
senkrechte Linie. Weil jede Teilschwingung **zwei** Angaben hat (Amplitude und Phase), braucht man genau genommen
zwei Diagramme:

- das __Amplitudenspektrum__ — Linienhöhe = Amplitude $A_k$ (wie stark),
- das __Phasenspektrum__ — Linienhöhe = Phase $\varphi_k$ (wie verschoben),

jeweils über der Kreisfrequenz aufgetragen. Der Gleichanteil $X_0$ erscheint als Linie bei $\omega = 0$.

:::grafik
Übereinander das Amplitudenspektrum (Linien der Höhe $X_0, A_1, A_2, \ldots$ an den Kreisfrequenzen $0, \omega_1,
\omega_2, \ldots$) und das Phasenspektrum (Linien der Höhe $\varphi_1, \varphi_2, \ldots$ an denselben Frequenzen).
Achsen beschriftet (Kreisfrequenz $\omega$ waagerecht).
:::

## Positive und negative Frequenzen: das zweiseitige Spektrum

Jetzt ein Punkt, der zunächst überrascht, sich aber direkt herleiten lässt. Wir haben im vorigen Abschnitt
gesehen, dass ein Kosinus die Summe **zweier** gegenläufig rotierender Zeiger ist. Schreiben wir das sauber auf.

**Schritt 1** — umgekehrte Eulersche Formel: Für jeden Winkel gilt $\cos\alpha = \tfrac{1}{2}\big(e^{j\alpha} +
e^{-j\alpha}\big)$.

**Schritt 2** — einsetzen mit $\alpha = \omega t + \varphi$ und die Phase in den Phasor (die komplexe Amplitude)
$X = A\,e^{j\varphi}$ ziehen:

$$A\cos(\omega t + \varphi) = \tfrac{1}{2}\,X\,e^{\,j\omega t} + \tfrac{1}{2}\,X^{*}\,e^{-j\omega t}.$$

**Schritt 3** — ablesen: Der erste Summand ist ein Zeiger, der mit der **positiven** Kreisfrequenz $+\omega$
rotiert, der zweite einer mit der **negativen** Kreisfrequenz $-\omega$. Ein einzelner reeller Ton erzeugt im
Spektrum also **zwei** Linien: eine bei $+\omega$ und eine bei $-\omega$, jede mit der halben Amplitude, und ihre
komplexen Amplituden sind zueinander **konjugiert** ($\tfrac12 X$ und $\tfrac12 X^*$). Das nennt man das
__zweiseitige Spektrum__.

**Eine Notation für alle Linien.** Damit man Gleichanteil, positive und negative Linien einheitlich schreiben
kann, fasst man die komplexen Amplituden aller Teilschwingungen zu **Spektralkoeffizienten** $a_k$ zusammen:

$$s(t) = \sum_{k=-N}^{N} a_k\,e^{\,j\omega_k t}, \qquad a_k = \begin{cases} X_0 & k = 0,\\[2pt] \tfrac{1}{2}X_k & k > 0,\\[2pt] \tfrac{1}{2}X_{-k}^{*} & k < 0,\end{cases} \qquad \omega_{-k} = -\omega_k.$$

Jeder reelle Ton $k>0$ mit Phasor $X_k = A_k e^{j\varphi_k}$ liefert damit genau zwei Koeffizienten:
$a_k = \tfrac12 X_k$ bei $+\omega_k$ und $a_{-k} = \tfrac12 X_k^{*}$ bei $-\omega_k$. Beide sind zueinander
konjugiert, also

$$a_{-k} = a_k^{*}.$$

Das ist das **Erkennungszeichen eines reellen Signals**: Sein zweiseitiges Spektrum ist konjugiert-symmetrisch.
Gezeichnet wird meist das Betragsspektrum $|a_k|$ über $\omega_k$ — und das ist dann spiegelsymmetrisch zu
$\omega = 0$ (denn $|a_{-k}| = |a_k|$).

**Was ist eine „negative Frequenz"?** Sie ist kein eigenständig erzeugbarer Ton, sondern die **mathematische
Begleiterin**: der im Uhrzeigersinn rotierende Zeiger, der zusammen mit seinem gegenläufigen Partner den
Imaginärteil aufhebt und so ein **reelles** Signal ergibt. Dass die negativen Linien immer die konjugierten
Spiegelbilder der positiven sind ($a_{-k} = a_k^*$), ist genau dieser Reellheits-Nachweis.

:::grafik
Oben das zweiseitige Betragsspektrum eines einzelnen Kosinus: zwei gleich hohe Linien der Höhe $|a_k| = |a_{-k}| =
\tfrac{A}{2}$ bei $+\omega$ und $-\omega$, symmetrisch zur Frequenz null. Unten die Deutung als Animation: zwei
gegenläufig rotierende Zeiger ($a_k\,e^{j\omega t}$ gegen den Uhrzeigersinn, $a_{-k}\,e^{-j\omega t}$ im
Uhrzeigersinn, mit $a_{-k} = a_k^*$), deren Summe in jedem Moment auf der reellen Achse bleibt (rein reell).
:::

**Einseitig oder zweiseitig?** Beide Darstellungen sind gebräuchlich:

- **Zweiseitig** ($-\omega$ und $+\omega$): mathematisch die „ehrliche" Form, passt zur komplexen Rechnung mit den
  $a_k$.
- **Einseitig** (nur $\omega \ge 0$): Man fasst die beiden Linien zusammen und verdoppelt die Amplitude —
  anschaulicher für die Praxis.

Man muss nur wissen, welche man gerade benutzt.

**Stolperstein:** Zeichnet man das Spektrum eines Kosinus nur mit der Linie bei $+\omega$, ist es im zweiseitigen
Bild **unvollständig** — die konjugierte Linie $a_{-k} = a_k^*$ bei $-\omega$ gehört zwingend dazu, sonst wäre das
Signal nicht reell.

:::kern
Das __Spektrum__ beschreibt ein Signal im __Frequenzbereich__: als Summe von Sinusanteilen
$s(t) = X_0 + \sum_k A_k\cos(\omega_k t + \varphi_k)$, dargestellt durch __Spektrallinien__ (Amplitude und Phase
je Kreisfrequenz). Zeit- und Frequenzbereich tragen dieselbe Information — aber die Zutaten sieht man nur im
Spektrum. Fasst man die Phasoren $X_k = A_k e^{j\varphi_k}$ zu __Spektralkoeffizienten__ zusammen
($a_0 = X_0$, $a_k = \tfrac12 X_k$ für $k>0$, $a_{-k} = \tfrac12 X_k^*$), wird $s(t) = \sum_k a_k e^{j\omega_k t}$.
Ein reeller Ton ergibt im __zweiseitigen Spektrum__ zwei Linien bei $+\omega$ und $-\omega$ mit halber Amplitude;
sie sind __konjugiert__ ($a_{-k} = a_k^*$) — das Betragsspektrum $|a_k|$ ist daher spiegelsymmetrisch. Die
__negative Frequenz__ ist die konjugierte Begleiterin, die das Signal reell macht (herleitbar aus
$\cos\alpha = \tfrac12(e^{j\alpha}+e^{-j\alpha})$).
:::

Bisher durften die Frequenzen $\omega_k$ beliebig sein. Bei einem **periodischen** Signal sind sie nicht beliebig,
sondern ganzzahlige Vielfache einer Grundfrequenz $\omega_T$. Wie man ein beliebiges periodisches Signal in genau
diese Oberschwingungen zerlegt, beschreibt die __Fourier-Reihe__ — das nächste Thema.

:::quiz
F: Was ist der Unterschied zwischen Zeit- und Frequenzbereich, und warum enthalten beide dieselbe Information?
A: Der Zeitbereich zeigt, was das Signal in jedem Augenblick macht; der Frequenzbereich zeigt, aus welchen Schwingungen es zusammengesetzt ist. Beide Beschreibungen sind nur verschiedene Anordnungen derselben Daten — aus der einen lässt sich die andere vollständig rekonstruieren.
F: Warum reicht die Zeitkurve allein nicht, obwohl sie alle Information enthält?
A: Einer welligen Zeitkurve sieht man ihre Frequenz-Zutaten nicht an — man erkennt nicht, welche Töne mit welcher Stärke darin stecken. Genau diese Frage beantwortet das Spektrum direkt, weshalb es für Aufgaben wie Filtern unentbehrlich ist.
F: Wofür steht der Gleichanteil $X_0$, und wo erscheint er im Spektrum?
A: $X_0$ ist der konstante Mittelwert des Signals — die „Schwingung" mit Frequenz null. Im Spektrum erscheint er als Linie bei $\omega=0$.
F: Warum braucht ein vollständiges Spektrum zwei Diagramme?
A: Jede Teilschwingung ist durch zwei Angaben bestimmt — Amplitude und Phase. Das Amplitudenspektrum trägt die Stärke $A_k$, das Phasenspektrum die Verschiebung $\varphi_k$ je Frequenz auf; erst beide zusammen legen das Signal eindeutig fest.
F: Warum erzeugt ein einzelner reeller Ton im zweiseitigen Spektrum zwei Linien?
A: Nach $\cos\alpha=\tfrac12(e^{j\alpha}+e^{-j\alpha})$ ist ein Kosinus die Summe zweier gegenläufig rotierender Zeiger — einer bei $+\omega$, einer bei $-\omega$, jeder mit halber Amplitude. Deshalb stehen im zweiseitigen Spektrum stets zwei Linien.
F: Was bedeutet die konjugierte Symmetrie $a_{-k}=a_k^*$, und wovon ist sie das Erkennungszeichen?
A: Die Linie bei $-\omega_k$ ist die komplex Konjugierte der Linie bei $+\omega_k$. Das ist das Erkennungszeichen eines reellen Signals; nur so heben sich die Imaginärteile der beiden Zeiger auf und die Summe bleibt reell. Das Betragsspektrum $|a_k|$ ist dadurch spiegelsymmetrisch zu $\omega=0$.
F: Was ist eine „negative Frequenz" physikalisch, und ist sie ein eigener Ton?
A: Nein — sie ist kein eigenständig erzeugbarer Ton, sondern die mathematische Begleiterin: der im Uhrzeigersinn rotierende Zeiger, der zusammen mit seinem gegenläufigen Partner den Imaginärteil aufhebt. Sie sorgt dafür, dass die komplexe Darstellung ein reelles Signal ergibt.
F: Wie hängen die Spektralkoeffizienten $a_k$ mit den Phasoren $X_k$ zusammen?
A: Es ist $a_0=X_0$, $a_k=\tfrac12 X_k$ für $k>0$ und $a_{-k}=\tfrac12 X_k^*$. So fasst man Gleichanteil, positive und negative Linien einheitlich zusammen, und das Signal wird $s(t)=\sum_k a_k e^{j\omega_k t}$.
F: Worin unterscheiden sich einseitiges und zweiseitiges Spektrum?
A: Das zweiseitige Spektrum zeigt Linien bei $-\omega$ und $+\omega$ (mathematisch „ehrlich", passt zur komplexen Rechnung mit $a_k$). Das einseitige fasst beide zu einer Linie bei $\omega\ge0$ zusammen und verdoppelt die Amplitude (anschaulicher für die Praxis). Man muss nur wissen, welche man gerade verwendet.
F: Warum ist ein Kosinus-Spektrum mit nur der Linie bei $+\omega$ im zweiseitigen Bild falsch?
A: Ohne die konjugierte Linie $a_{-k}=a_k^*$ bei $-\omega$ wäre das dargestellte Signal nicht reell, sondern ein komplexer rotierender Zeiger. Die negative Linie gehört zwingend dazu, damit das Signal den gemessenen reellen Kosinus beschreibt.
:::
