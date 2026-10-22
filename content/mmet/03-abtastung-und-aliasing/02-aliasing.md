---
title: Aliasing
pfad: Elektrotechnik / 1. Semester / Mathematische Methoden der Elektrotechnik / Abtastung und Aliasing
order: 30200
summary: Von Grund auf – warum ganz verschiedene Sinussignale nach dem Abtasten dieselbe Zahlenfolge ergeben und dadurch ununterscheidbar werden. Wir leiten alle „Alias-Frequenzen" her: $\hat\omega_k=\hat\omega_0+2\pi k$ und $\hat\omega_k=2\pi k-\hat\omega_0$. Daraus folgt, dass jede abgetastete Schwingung eine eindeutige Haupt-Aliasfrequenz im Intervall $-\pi<\hat\omega_0<\pi$ besitzt.
tags: Aliasing, Alias-Frequenz, normierte Kreisfrequenz, Haupt-Aliasfrequenz, Unterabtastung, zeitdiskreter Sinus
---

:::grafik
Einstiegs-Animation: Eine feste Abtastfolge (Stiele auf ganzzahligem $n$). Zuerst läuft eine langsame
Kosinuskurve genau durch die Stiele. Dann wird ihre Frequenz hochgedreht — und sobald sie eine bestimmte Grenze
überschreitet, läuft plötzlich eine viel **schnellere** Kurve ebenfalls exakt durch dieselben Stiele. Beide
„passen" auf die gleiche Folge. Ein Zähler zeigt: $\hat\omega_0$, $\hat\omega_0+2\pi$, $2\pi-\hat\omega_0$, …
ergeben alle dieselbe Folge. Kernbotschaft: Nach dem Abtasten sind unendlich viele verschiedene Frequenzen
ununterscheidbar — das ist Aliasing.
:::

:::konzept
Im vorigen Artikel haben wir gesehen: Ein abgetasteter Sinus hängt nur von der __normierten Kreisfrequenz__
$\hat\omega$ ab, und zwei verschiedene zeitkontinuierliche Signale können dieselbe Folge $\tilde s[n]$ erzeugen.
Jetzt rechnen wir **genau** aus, welche Frequenzen das sind. Das Ergebnis ist verblüffend und für die Praxis
entscheidend: Zu jeder abgetasteten Schwingung gehören **unendlich viele** zeitkontinuierliche Frequenzen, die
alle dieselbe Zahlenfolge liefern — die __Alias-Frequenzen__. Dieses „Verwechseln" von Frequenzen heißt
__Aliasing__ (von engl. *alias*, Deckname) und ist der Grund, warum man beim Abtasten so sorgfältig sein muss.
:::

**Worum es geht:** Wir leiten aus der Periodizität und Symmetrie des Kosinus **alle** Alias-Frequenzen her
($\hat\omega_0+2\pi k$ und $2\pi k-\hat\omega_0$), ordnen sie auf der Frequenzachse an und finden die ausgezeichnete
__Haupt-Aliasfrequenz__.

## Zwei Zutaten: der Kosinus ist periodisch und gerade

Wir starten mit einer abgetasteten Schwingung mit normierter Kreisfrequenz $\hat\omega_0$:

$$\tilde s_0[n] = \cos(\hat\omega_0\,n + \varphi).$$

Zwei elementare Eigenschaften des Kosinus sind der Schlüssel:

- **periodisch mit $2\pi$:** $\cos(x + 2\pi m) = \cos(x)$ für jedes ganze $m$.
- **gerade (symmetrisch):** $\cos(-x) = \cos(x)$, also auch $\tilde s_0[n] = \cos(-\hat\omega_0 n - \varphi)$.

Beide zusammen erzeugen die beiden Familien von Alias-Frequenzen.

:::grafik
Zwei kleine Kosinus-Merkbilder: links „Periode $2\pi$" ($\cos(x)$ und $\cos(x+2\pi)$ deckungsgleich), rechts
„gerade" ($\cos(x)$ und $\cos(-x)$ deckungsgleich). Darunter $\tilde s_0[n]=\cos(\hat\omega_0 n+\varphi)=
\cos(-\hat\omega_0 n-\varphi)$.
:::

## Familie 1: Vielfache von $2\pi$ addieren

Wir erhöhen die normierte Kreisfrequenz um ein ganzzahliges Vielfaches von $2\pi$ und schauen, was mit der Folge
passiert:

$$\tilde s_k[n] = \cos\big[(\hat\omega_0 + 2\pi k)\,n + \varphi\big] = \cos\big(\hat\omega_0 n + \varphi + 2\pi k n\big).$$

Der Zusatzterm $2\pi k n$ ist — weil $k$ **und** $n$ ganzzahlig sind — stets ein Vielfaches von $2\pi$ und fällt
im Kosinus weg:

$$\tilde s_k[n] = \cos(\hat\omega_0 n + \varphi) = \tilde s_0[n] \qquad\Longrightarrow\qquad \hat\omega_k = \hat\omega_0 + 2\pi k.$$

Alle normierten Kreisfrequenzen, die sich um $2\pi k$ unterscheiden, ergeben also **dieselbe** Folge.

:::grafik
Rechenkette $\cos[(\hat\omega_0+2\pi k)n+\varphi]=\cos(\hat\omega_0 n+\varphi+2\pi kn)=\cos(\hat\omega_0 n+\varphi)$
mit hervorgehobenem „$2\pi kn$ = Vielfaches von $2\pi$ (da $k,n\in\mathbb Z$)"; Ergebnis $\hat\omega_k=\hat\omega_0
+2\pi k$.
:::

## Familie 2: Spiegelung am Vielfachen von $2\pi$

Jetzt nutzen wir, dass der Kosinus **gerade** ist. Wir bilden die Folge zur Frequenz $2\pi k - \hat\omega_0$:

$$\tilde s_k^{-}[n] = \cos\big[(2\pi k - \hat\omega_0)\,n - \varphi\big] = \cos\big[2\pi k n - (\hat\omega_0 n + \varphi)\big].$$

Der Term $2\pi k n$ fällt wieder weg, übrig bleibt $\cos[-(\hat\omega_0 n + \varphi)]$ — und weil der Kosinus
gerade ist, ist das gleich $\cos(\hat\omega_0 n + \varphi)$:

$$\tilde s_k^{-}[n] = \cos(\hat\omega_0 n + \varphi) = \tilde s_0[n] \qquad\Longrightarrow\qquad \hat\omega_k = 2\pi k - \hat\omega_0.$$

:::grafik
Rechenkette $\cos[(2\pi k-\hat\omega_0)n-\varphi]=\cos[2\pi kn-(\hat\omega_0 n+\varphi)]=\cos[-(\hat\omega_0 n+
\varphi)]=\cos(\hat\omega_0 n+\varphi)$ mit markiertem „gerade"-Schritt; Ergebnis $\hat\omega_k=2\pi k-\hat\omega_0$.
:::

## Alle Alias-Frequenzen auf einen Blick

Zusammengefasst liefern **alle** normierten Kreisfrequenzen

$$\boxed{\;\hat\omega_k = \hat\omega_0 + 2\pi k \quad\text{oder}\quad \hat\omega_k = 2\pi k - \hat\omega_0, \qquad k\in\mathbb Z\;}$$

exakt dieselbe zeitdiskrete Folge $\tilde s_0[n]$. Trägt man sie über der Achse $\hat\omega$ auf, erkennt man die
Struktur: Die Alias-Frequenzen treten als **äquidistante Paare im Abstand $2\pi$** auf (die beiden Familien),
gespiegelt um die Vielfachen von $2\pi$ bzw. $\pi$.

Genau **eine** davon ist ausgezeichnet: die betragskleinste. Sie liegt immer im Intervall

$$-\pi < \hat\omega_0 < \pi \qquad(\text{\underline{Haupt-Aliasfrequenz}}),$$

und alle anderen sind „Kopien" davon. Die Haupt-Aliasfrequenz ist die natürliche Wahl, um die Folge zu
repräsentieren — und sie wird im nächsten Artikel bei der Rekonstruktion wichtig.

:::grafik
Die Achse $\hat\omega/\pi$ mit den Spektrallinien der Alias-Frequenzen: ein grau hinterlegtes Band
$(-\pi,\pi)$ enthält die Haupt-Aliasfrequenz; links und rechts davon die Kopien im Abstand $2\pi$. Pfeile „falten"
die äußeren Linien ins Band zurück. Formeln $\hat\omega_k=\hat\omega_0+2\pi k$ und $2\pi k-\hat\omega_0$.
:::

## Was das praktisch bedeutet

Knüpfen wir an das Beispiel aus dem vorigen Artikel an: Ein 200-Hz-Ton, abgetastet mit
$r=1\,$kHz, hat $\hat\omega_0 = 0{,}4\pi$. Seine Alias-Frequenzen sind $0{,}4\pi + 2\pi = 2{,}4\pi$ (entspricht
$f = r\hat\omega/2\pi = 1200\,$Hz) und $2\pi - 0{,}4\pi = 1{,}6\pi$ ($f = 800\,$Hz), dann $2800\,$Hz, $1800\,$Hz
usw. Alle diese Töne — **200 Hz, 800 Hz, 1200 Hz, 1800 Hz, …** — erzeugen bei $r=1\,$kHz die **identische**
Zahlenfolge.

Die Folge: Tastet man einen 1200-Hz-Ton mit nur 1 kHz ab, erscheint er im abgetasteten Signal als **200-Hz**-Ton
— eine Frequenz, die gar nicht im Original war. Dieselbe Verwechslung sieht man im Alltag als „rückwärts
drehendes Wagenrad" im Film: Die Bild-Abtastrate (Bilder pro Sekunde) ist zu niedrig für die schnelle Drehung.

:::grafik
Eine Abtastfolge bei $r=1\,$kHz, durch die drei Kosinuskurven (200 Hz, 800 Hz, 1200 Hz) exakt hindurchlaufen,
alle mit denselben Stielen; Beschriftung „bei $r=1\,$kHz ununterscheidbar". Daneben als Alltagsbild ein
Wagenrad mit zu niedriger Bildrate, das scheinbar rückwärts läuft.
:::

:::kern
__Aliasing__: Verschiedene zeitkontinuierliche Sinussignale ergeben nach dem Abtasten mit derselben Rate $r$
dieselbe Folge. Aus der $2\pi$-Periodizität und der Geradheit des Kosinus
($\tilde s_0[n]=\cos(\hat\omega_0 n+\varphi)=\cos(-\hat\omega_0 n-\varphi)$) folgen **alle** __Alias-Frequenzen__:
$\hat\omega_k=\hat\omega_0+2\pi k$ **und** $\hat\omega_k=2\pi k-\hat\omega_0$ ($k\in\mathbb Z$). Sie liegen als
Paare im Abstand $2\pi$ auf der $\hat\omega$-Achse; die eindeutige __Haupt-Aliasfrequenz__ liegt in
$-\pi<\hat\omega_0<\pi$. Praktisch: Eine zu hohe Frequenz tarnt sich als eine tiefere (z. B. $1200\,$Hz $\to$
$200\,$Hz bei $r=1\,$kHz; „Wagenrad-Effekt").
:::

Wenn unendlich viele Frequenzen dieselbe Folge erzeugen — welche davon gibt ein D/A-Umsetzer bei der
Rekonstruktion wieder aus? Und unter welcher Bedingung ist das Ergebnis **eindeutig** das Originalsignal? Das
beantwortet der nächste Artikel über die Rekonstruktion und das __Abtasttheorem__.

:::quiz
F: Was ist Aliasing in einem Satz?
A: Aliasing ist das Phänomen, dass verschiedene zeitkontinuierliche Sinussignale nach dem Abtasten mit derselben Rate exakt dieselbe Zahlenfolge ergeben und dadurch ununterscheidbar werden. Eine hohe Frequenz „tarnt" sich als eine andere.
F: Welche zwei Eigenschaften des Kosinus erzeugen die Alias-Frequenzen?
A: Die $2\pi$-Periodizität ($\cos(x+2\pi m)=\cos x$) und die Geradheit ($\cos(-x)=\cos x$). Die erste erzeugt die Familie $\hat\omega_0+2\pi k$, die zweite die gespiegelte Familie $2\pi k-\hat\omega_0$.
F: Warum fällt beim Erhöhen um $2\pi k$ der Zusatzterm im Kosinus weg?
A: Der Zusatz ist $2\pi k n$, und weil sowohl $k$ als auch der Folgenindex $n$ ganzzahlig sind, ist das stets ein ganzzahliges Vielfaches von $2\pi$. Der Kosinus ist $2\pi$-periodisch, also ändert dieser Term die Folge nicht.
F: Wie entsteht die zweite Alias-Familie $\hat\omega_k=2\pi k-\hat\omega_0$?
A: Man setzt die Frequenz $2\pi k-\hat\omega_0$ ein; der Term $2\pi kn$ fällt wieder weg, übrig bleibt $\cos[-(\hat\omega_0 n+\varphi)]$. Weil der Kosinus gerade ist, ist das gleich $\cos(\hat\omega_0 n+\varphi)$ — also dieselbe Folge.
F: Warum ist es wesentlich, dass $n$ ganzzahlig ist, damit Aliasing auftritt?
A: Nur für ganze $n$ ist $2\pi k n$ ein Vielfaches von $2\pi$ und verschwindet im Kosinus. Bei einem zeitkontinuierlichen Signal (reelles Argument) träfe das nicht zu — die Frequenzen wären unterscheidbar. Aliasing ist also eine Folge der zeitlichen Diskretisierung.
F: Was ist die Haupt-Aliasfrequenz und warum ist sie ausgezeichnet?
A: Sie ist die betragskleinste der unendlich vielen Alias-Frequenzen und liegt im Intervall $-\pi<\hat\omega_0<\pi$. Alle anderen sind „Kopien" davon; sie ist die natürliche eindeutige Repräsentantin der abgetasteten Folge.
F: Warum gibt es zu einer Folge unendlich viele zeitkontinuierliche Frequenzen und nicht nur eine?
A: Jede der beiden Familien läuft über alle ganzen $k$, also $\dots,\hat\omega_0,\hat\omega_0\pm2\pi,\dots$ und $\dots,2\pi k-\hat\omega_0,\dots$. Zu jeder abgetasteten Schwingung gehören damit unendlich viele kontinuierliche Frequenzen, die exakt dieselben Abtastwerte liefern.
F: Wie ordnen sich die Alias-Frequenzen auf der $\hat\omega$-Achse an?
A: Als äquidistante Paare im Abstand $2\pi$, gespiegelt um die Vielfachen von $\pi$ bzw. $2\pi$. Anschaulich werden alle äußeren Linien ins Grundband $(-\pi,\pi)$ „zurückgefaltet", wo die Haupt-Aliasfrequenz sitzt.
F: Warum erscheint ein mit 1 kHz abgetasteter 1200-Hz-Ton als 200-Hz-Ton?
A: Bei $r=1\,$kHz hat 1200 Hz die normierte Kreisfrequenz $2{,}4\pi$, deren Haupt-Alias $2{,}4\pi-2\pi=0{,}4\pi$ ist — genau die von 200 Hz. Beide liefern dieselbe Folge, und die Rekonstruktion wählt die tiefe Frequenz im Grundband.
F: Was hat der „rückwärts drehende Wagenrad-Effekt" im Film mit Aliasing zu tun?
A: Die Bildrate (Bilder pro Sekunde) ist eine Abtastrate; dreht sich das Rad zu schnell dafür, fällt seine Drehfrequenz mit einer niedrigeren (oder negativen) Alias-Frequenz zusammen. Das Auge sieht dann eine langsame oder rückwärtige Drehung — dieselbe Frequenzverwechslung wie beim Signal-Aliasing.
:::
