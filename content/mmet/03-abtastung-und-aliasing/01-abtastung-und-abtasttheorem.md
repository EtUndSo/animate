---
title: Abtastung und das Abtasttheorem
pfad: Elektrotechnik / 1. Semester / Mathematische Methoden der Elektrotechnik / Abtastung und Aliasing
order: 30100
summary: Von Grund auf – wie aus einem zeitkontinuierlichen Signal eine Folge von Zahlen wird, die ein Computer verarbeiten kann. Wir klären, was die Abtastrate $f_s$ bedeutet, warum ein abgetasteter Sinus nur von der normierten Frequenz $f/f_s$ abhängt, und leiten das Abtasttheorem $f_s>2f_\text{max}$ her – die Bedingung, unter der beim Abtasten nichts verloren geht.
tags: Abtastung, Abtastrate, Abtastperiode, Abtasttheorem, Nyquist-Frequenz, normierte Frequenz, zeitdiskret
---

:::grafik
Einstiegs-Animation: Eine glatte Sinuskurve läuft über die Zeitachse; in gleichmäßigen Abständen $T_s$ fällt ein
„Messstrahl" herab und greift einen Wert ab — es entsteht eine Folge von Punkten (die Abtastwerte). Ein
Schieberegler für die Abtastrate $f_s$: bei hoher Rate liegen die Punkte dicht und zeichnen die Welle treu nach;
dreht man $f_s$ herunter, werden die Punkte so spärlich, dass sie plötzlich eine ganz andere, langsamere Welle
andeuten. Kernbotschaft: Abtasten heißt, das Signal in gleichen Zeitschritten zu „fotografieren" — und wie oft
man das tut, entscheidet, ob die Information erhalten bleibt.
:::

:::konzept
Ein Computer, ein Mikrocontroller, eine Soundkarte — keines dieser Geräte kann ein **zeitkontinuierliches**
Signal (eine Spannung, die zu *jedem* Zeitpunkt einen Wert hat) direkt verarbeiten. Sie kennen nur **Folgen von
Zahlen**. Der Übergang von der kontinuierlichen Welt in die digitale heißt __Abtastung__ (engl. *sampling*): Man
misst das Signal in regelmäßigen Zeitabständen und behält nur diese Stichproben. Sofort stellt sich die
entscheidende Frage: Wie oft muss man messen, damit man das Signal später **fehlerfrei** zurückgewinnen kann —
und nicht etwas völlig anderes herausbekommt? Die Antwort ist das __Abtasttheorem__, eine der wichtigsten
Aussagen der gesamten Signalverarbeitung.
:::

**Worum es geht:** Wir definieren __Abtastperiode__ und __Abtastrate__, sehen, dass ein abgetasteter Sinus nur von
der __normierten Frequenz__ $f/f_s$ abhängt, und leiten daraus her, *warum* man mit mehr als dem **Doppelten** der
höchsten Signalfrequenz abtasten muss.

## Vom kontinuierlichen Signal zur Zahlenfolge

Beim Abtasten greift man aus dem zeitkontinuierlichen Signal $x(t)$ nur die Werte zu den Zeitpunkten
$t = n\,T_s$ heraus (mit ganzzahligem $n = 0, 1, 2, \ldots$). Das Ergebnis ist eine **Folge** $x[n]$:

$$x[n] = x(n\,T_s).$$

- __$T_s$__: die __Abtastperiode__ — der feste Zeitabstand zwischen zwei Messungen.
- __$f_s = 1/T_s$__: die __Abtastrate__ (oder Abtastfrequenz) — wie viele Abtastwerte pro Sekunde, in Hertz. (Bei
  Audio-CDs z. B. $f_s = 44{,}1\,$kHz.)
- __$x[n]$__: der $n$-te Abtastwert; die eckige Klammer kennzeichnet ein **zeitdiskretes** Signal (nur für ganze
  $n$ definiert), im Unterschied zum runden $x(t)$.

:::grafik
Oben die kontinuierliche Kurve $x(t)$; darunter dieselbe Zeitachse mit senkrechten Abtast-Strahlen im Abstand
$T_s$; ganz unten die resultierende Folge $x[n]$ als Stielplot (Punkte mit Stielen auf ganzzahligen $n$).
Beschriftet $T_s$ und $f_s=1/T_s$.
:::

## Ein abgetasteter Sinus: nur die normierte Frequenz zählt

Das Wichtigste passiert, wenn wir einen Sinus abtasten. Nehmen wir $x(t) = \cos(2\pi f\,t)$ und setzen
$t = n/f_s$ ein:

$$x[n] = \cos\!\left(2\pi f\,\frac{n}{f_s}\right) = \cos\!\left(2\pi\,\frac{f}{f_s}\,n\right).$$

Die Folge hängt also **nicht** von $f$ und $f_s$ einzeln ab, sondern nur von ihrem **Verhältnis**:

$$\hat f = \frac{f}{f_s} \quad(\text{normierte Frequenz}), \qquad \hat\omega = 2\pi\,\frac{f}{f_s} \quad(\text{normierte Kreisfrequenz}).$$

- __$\hat f = f/f_s$__: wie viele **Perioden pro Abtastschritt** die Schwingung macht.
- Zwei physikalisch verschiedene Signale mit demselben $f/f_s$ ergeben **dieselbe** Abtastfolge — ein erster
  Hinweis darauf, dass beim Abtasten Information verloren gehen kann.

:::grafik
Dieselbe Abtastfolge (identische Punkte) mit zwei dahinterliegenden Sinuskurven verschiedener Frequenz, die beide
exakt durch die Punkte gehen — darüber „gleiche $f/f_s$ → gleiche Folge". Daneben die Formel
$x[n]=\cos(2\pi \hat f n)$.
:::

## Wie oft muss man abtasten? Das Abtasttheorem

Jetzt die Kernfrage. Betrachte eine einzelne Schwingung mit Frequenz $f$ (Periodendauer $1/f$). Um ihre
**Oszillation** überhaupt zu erfassen, braucht man mindestens einen Hoch- und einen Tiefpunkt pro Periode — also
mindestens **zwei** Abtastwerte pro Periode. Das heißt, die Abtastperiode muss kürzer als die halbe Periodendauer
sein: $T_s < \tfrac{1}{2f}$, oder umgestellt $f_s > 2f$.

Enthält ein Signal Frequenzanteile bis zur höchsten Frequenz $f_\text{max}$, muss diese Bedingung für **alle**
davon gelten. Das ist das __Abtasttheorem__ (Nyquist-Shannon):

$$f_s > 2\,f_\text{max}.$$

- __$f_\text{max}$__: die höchste im Signal vorkommende Frequenz.
- __$f_s/2$__: die __Nyquist-Frequenz__ — die höchste Frequenz, die bei gegebener Abtastrate noch eindeutig
  erfassbar ist.

**Warum genau der Faktor 2?** Weil eine Schwingung ihre Richtung pro Periode zweimal ändert (einmal hoch, einmal
runter). Mit weniger als zwei Punkten pro Periode kann die Punktfolge die schnelle Schwingung nicht von einer
langsameren unterscheiden — sie „passt" auf mehrere Kurven gleichzeitig (siehe oben). Genau dann entsteht der
Fehler, den wir im nächsten Artikel als __Aliasing__ untersuchen.

:::grafik
Drei Fälle derselben Schwingung: (a) viele Punkte pro Periode (treu), (b) genau 2 Punkte pro Periode (Grenzfall
$f_s=2f$), (c) weniger als 2 (die Punkte liegen auf einer scheinbar langsameren Welle). Jeweils die Zahl
„Abtastwerte pro Periode" markiert und die Bedingung $f_s>2f$ als Trennlinie.
:::

## Warum nicht einfach „sehr schnell" abtasten?

Man könnte meinen: Je höher $f_s$, desto besser — warum dann überhaupt ein Theorem? Weil hohe Abtastraten teuer
sind: mehr Datenmenge, schnellere (teurere) Wandler, mehr Speicher und Rechenlast. Das Abtasttheorem sagt
**genau**, wie niedrig man gehen darf, ohne Information zu verlieren — nämlich knapp über $2f_\text{max}$. In der
Praxis begrenzt man das Signal vor dem Abtasten mit einem **Anti-Aliasing-Tiefpass** auf $f_\text{max}<f_s/2$,
damit das Theorem garantiert erfüllt ist. (Audio: hörbar bis ~20 kHz → $f_s=44{,}1\,$kHz liegt knapp über
$2\cdot 20\,$kHz.)

:::grafik
Ein Frequenzbereich-Bild: das Signalspektrum reicht bis $f_\text{max}$; eine senkrechte Linie bei der
Nyquist-Frequenz $f_s/2$ markiert die Grenze. Fall „$f_\text{max}<f_s/2$" (grün, erlaubt) vs. „$f_\text{max}>f_s/2$"
(rot, Aliasing). Davor ein Anti-Aliasing-Tiefpass, der alles über $f_s/2$ abschneidet.
:::

:::kern
Beim __Abtasten__ behält man nur die Werte $x[n]=x(nT_s)$ zu den Zeitpunkten $nT_s$ (__Abtastperiode__ $T_s$,
__Abtastrate__ $f_s=1/T_s$ in Hz). Ein abgetasteter Sinus $x[n]=\cos(2\pi\tfrac{f}{f_s}n)$ hängt nur von der
__normierten Frequenz__ $\hat f=f/f_s$ ab — gleiche $f/f_s$ ⇒ gleiche Folge. Damit die Oszillation erfasst wird,
braucht man **mehr als zwei** Abtastwerte pro Periode der höchsten Frequenz: das __Abtasttheorem__
$f_s>2f_\text{max}$ (Faktor 2, weil eine Periode zwei Richtungswechsel hat). Die __Nyquist-Frequenz__ $f_s/2$ ist
die höchste eindeutig erfassbare Frequenz; in der Praxis sichert ein **Anti-Aliasing-Tiefpass** die Bedingung.
:::

Wird das Abtasttheorem **verletzt** ($f_s < 2f_\text{max}$), verschwindet die Information nicht einfach — es
passiert etwas Tückischeres: Eine hohe Frequenz tarnt sich als eine niedrigere und erscheint im abgetasteten
Signal als völlig falscher Ton. Dieses Phänomen, das __Aliasing__, und wie man die „Scheinfrequenz" ausrechnet,
ist das Thema des nächsten Artikels.
