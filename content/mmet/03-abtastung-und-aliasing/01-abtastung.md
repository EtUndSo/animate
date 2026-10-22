---
title: Abtastung und zeitdiskrete Signale
pfad: Elektrotechnik / 1. Semester / Mathematische Methoden der Elektrotechnik / Abtastung und Aliasing
order: 30100
summary: Von Grund auf – wie aus einem zeitkontinuierlichen Signal $s(t)$ durch Abtasten mit der Abtastrate $r=1/T_s$ die Zahlenfolge $\tilde s[n]=s(nT_s)$ wird, die ein Computer verarbeiten kann. Wir sehen, dass ein abgetasteter Sinus nur von der normierten Kreisfrequenz $\hat\omega=\omega T_s$ abhängt – und damit seine absolute Frequenz „vergisst". Genau das ist die Wurzel von Aliasing.
tags: Abtastung, Abtastrate, Abtastperiode, zeitdiskretes Signal, normierte Kreisfrequenz, A/D-Umsetzer, Quantisierung
---

:::grafik
Einstiegs-Animation: Ein glattes Signal $s(t)$ läuft in einen Block „Abtaster", über den von unten die
Abtastperiode $T_s$ eingespeist wird; heraus kommt eine Folge von Stielen $\tilde s[n]$. Zwischen den
Abtastzeitpunkten $nT_s$ „weiß" die Folge nichts mehr über den Verlauf dazwischen. Rechts wandelt ein zweiter
Block (Quantisierer) die Höhen in Zahlen mit endlich vielen Stellen um. Kernbotschaft: Abtasten verwandelt ein
kontinuierliches Signal in eine Zahlenfolge — den Rohstoff jeder digitalen Signalverarbeitung.
:::

:::konzept
Ein Computer, ein Mikrocontroller, eine Soundkarte kennen keine zeitkontinuierlichen Signale (Spannungen, die zu
*jedem* Zeitpunkt einen Wert haben), sondern nur **endliche Folgen von Zahlen**. Der Übergang von der analogen in
die digitale Welt heißt __Abtastung__ (engl. *sampling*): Man misst das Signal in gleichen Zeitabständen und
behält nur diese Stichproben. Dabei passiert etwas Subtiles, das die gesamte digitale Signalverarbeitung prägt:
Ein abgetasteter Sinus hängt nur noch vom **Verhältnis** aus Signal- und Abtastfrequenz ab — seine absolute
Frequenz ist nicht mehr aus der Folge allein ablesbar. Das ist der Keim des __Aliasing__, das wir in den nächsten
Artikeln untersuchen.
:::

**Worum es geht:** Wir definieren __Abtastperiode__ $T_s$ und __Abtastrate__ $r$, ordnen die Abtastung in die
__A/D-Umsetzung__ ein und zeigen, dass ein abgetasteter Sinus nur von der __normierten Kreisfrequenz__
$\hat\omega=\omega T_s$ abhängt.

## Der Abtaster: aus $s(t)$ wird $\tilde s[n]$

Beim Abtasten greift man aus dem zeitkontinuierlichen Signal $s(t)$ nur die Werte zu den äquidistanten
Zeitpunkten $t_n = n\,T_s$ heraus ($n\in\mathbb Z$). Das Ergebnis ist eine **Folge**, die man mit einer Tilde und
eckigen Klammern schreibt:

$$\tilde s[n] = s(n\,T_s) = s\!\left(\frac{n}{r}\right).$$

- __$T_s$__: die __Abtastperiode__ — der feste Zeitabstand zwischen zwei Messungen.
- __$r = 1/T_s$__: die __Abtastrate__ (Abtastfrequenz), in Hertz — wie viele Abtastwerte pro Sekunde. (In der
  Literatur oft auch $f_s$ geschrieben.)
- __$\tilde s[n]$__: der $n$-te Abtastwert. Die **eckige** Klammer kennzeichnet ein __zeitdiskretes__ Signal (nur
  für ganze $n$ definiert), im Unterschied zum runden $s(t)$. Formal ist es eine Abbildung $\tilde s:\mathbb
  Z\to\mathbb R$.

:::grafik
Oben die kontinuierliche Kurve $s(t)$; darunter dieselbe Zeitachse mit senkrechten Abtast-Strahlen im Abstand
$T_s$; ganz unten die Folge $\tilde s[n]$ als Stielplot über ganzzahligem $n$. Beschriftet $T_s$ und $r=1/T_s$.
:::

## Einordnung: A/D- und D/A-Umsetzung

Die reine Abtastung ist nur der erste Teil der Digitalisierung. Ein echter __A/D-Umsetzer__ (Analog-Digital)
besteht aus zwei Stufen:

- dem __Abtaster__ (zeitliche Diskretisierung) → $\tilde s[n]$,
- dem __Quantisierer__, der jeden Wert auf endlich viele Stufen rundet (z. B. $k=16\,$bit) → $\tilde s_q[n]$, denn
  jede gespeicherte Zahl hat nur endlich viele Binärstellen.

Umgekehrt macht ein __D/A-Umsetzer__ (bzw. __D/C-Umsetzer__, *Diskret-Continuierlich*) aus der Folge wieder ein
zeitkontinuierliches Signal — durch Rekonstruktion und Interpolation zwischen den Abtastwerten (Thema eines
späteren Artikels). In diesem und dem nächsten Artikel betrachten wir die **ideale** Abtastung, also ohne den
Quantisierungsfehler.

:::grafik
Blockkette: $s(t)$ → [Abtaster, $T_s$] → $\tilde s[n]$ → [Quantisierer, $k$ bit] → $\tilde s_q[n]$, die ersten
beiden zusammengefasst als „A/D-Umsetzer"; darunter die Rückrichtung $\tilde s[n]$ → [D/C-Umsetzer, $T_s$] →
$s(t)$.
:::

## Ein abgetasteter Sinus: nur die normierte Kreisfrequenz zählt

Das Wichtigste zeigt sich am Sinus, dem Grundbaustein aller Signale. Tastet man
$s(t) = A\cos(\omega t + \varphi)$ ab, setzt man $t = nT_s$ ein:

$$\tilde s[n] = A\cos(\omega\,T_s\,n + \varphi) = A\cos(\hat\omega\,n + \varphi), \qquad \hat\omega = \omega\,T_s = \frac{\omega}{r}.$$

- __$\hat\omega = \omega T_s$__: die __normierte Kreisfrequenz__. Sie ist **dimensionslos** (Einheit „rad"), denn
  $\omega$ hat die Einheit $1/\text{s}$ und $T_s$ die Einheit s. Auch $n$ ist dimensionslos.
- Gleichwertig gilt $\hat\omega = 2\pi\,\dfrac{T_s}{T}$ — das **Verhältnis** aus Abtastperiode $T_s$ und
  Periodendauer $T$ des Sinussignals.

Die Folge hängt also **nur** von $\hat\omega$ ab, nicht von $\omega$ und $r$ einzeln.

:::grafik
Links die kontinuierliche Kosinuskurve $s(t)$; rechts der Stielplot $\tilde s[n]=A\cos(\hat\omega n+\varphi)$.
Dazwischen die Umrechnung $\hat\omega=\omega T_s=2\pi T_s/T$ mit markierter Periodendauer $T$ und Abtastabstand
$T_s$.
:::

**Zahlenbeispiel:** Ein Ton $s(t)=\cos(2\pi\cdot 200\,\text{Hz}\cdot t)$ (also $T=5\,$ms) werde mit
$r=1\,$kHz abgetastet ($T_s=1\,$ms). Dann

$$\hat\omega = 2\pi\cdot 200\cdot 0{,}001 = 0{,}4\pi \quad\Rightarrow\quad \tilde s[n] = \cos(0{,}4\pi\,n),$$

und es liegen $T/T_s = 5$ Abtastwerte pro Periode.

:::grafik
Derselbe 200-Hz-Kosinus kontinuierlich und abgetastet bei $r=1\,$kHz: fünf Stiele pro Signalperiode, die
Folgenformel $\tilde s[n]=\cos(0{,}4\pi n)$ daneben.
:::

## Die absolute Frequenz geht verloren

Hier liegt der springende Punkt. Weil $\tilde s[n]$ nur $\hat\omega$ enthält, steckt in der Folge **keine
Information** über $T_s$ bzw. die Abtastrate $r$ — und damit auch nicht über die *absolute* Frequenz $\omega$ des
Originalsignals. Kennt man die Abtastrate nicht, kann man aus der Zahlenfolge allein nicht sagen, welche Frequenz
$s(t)$ hatte.

Noch schärfer: Zwei **verschiedene** zeitkontinuierliche Sinussignale (verschiedene $\omega$) können bei derselben
Abtastrate **dieselbe** Folge $\tilde s[n]$ ergeben — wenn ihre normierten Kreisfrequenzen zusammenfallen. Genau
dieses „Zusammenfallen" ist das Phänomen __Aliasing__, das wir im nächsten Artikel genau ausrechnen.

:::grafik
Eine einzige Abtastfolge (identische Stiele), durch die zwei verschiedene kontinuierliche Kosinuskurven
unterschiedlicher Frequenz exakt hindurchlaufen; Beschriftung „gleiche Folge, verschiedene $s(t)$ → ohne $r$
nicht unterscheidbar".
:::

:::kern
__Abtasten__ behält nur die Werte $\tilde s[n]=s(nT_s)=s(n/r)$ zu den Zeitpunkten $nT_s$: __Abtastperiode__ $T_s$,
__Abtastrate__ $r=1/T_s$ (Hz, in der Literatur auch $f_s$). Die vollständige __A/D-Umsetzung__ = Abtaster +
__Quantisierer__ ($\to\tilde s_q[n]$); der __D/C-Umsetzer__ macht daraus wieder $s(t)$. Ein abgetasteter Sinus ist
$\tilde s[n]=A\cos(\hat\omega n+\varphi)$ mit der **dimensionslosen** __normierten Kreisfrequenz__
$\hat\omega=\omega T_s=\omega/r=2\pi T_s/T$. Die Folge hängt nur von $\hat\omega$ ab — die **absolute** Frequenz
$\omega$ ist ohne Kenntnis von $r$ nicht rekonstruierbar. Dass verschiedene $s(t)$ dieselbe Folge liefern können,
ist die Wurzel von __Aliasing__.
:::

Verschiedene Signale, die nach dem Abtasten ununterscheidbar werden — das klingt nach Informationsverlust, und
genau das ist __Aliasing__. Im nächsten Artikel leiten wir her, **welche** Frequenzen bei fester Abtastrate
dieselbe Folge erzeugen (die „Alias-Frequenzen") und welche davon die ausgezeichnete ist.

:::quiz
F: Warum muss ein zeitkontinuierliches Signal für den Computer überhaupt abgetastet werden?
A: Ein Computer kennt keine zu jedem Zeitpunkt definierte Spannung, sondern nur endliche Zahlenfolgen. Das Abtasten misst das Signal in gleichen Zeitabständen und behält nur diese Stichproben — so entsteht der verarbeitbare Rohstoff $\tilde s[n]$.
F: Was bedeutet die eckige Klammer in $\tilde s[n]$ gegenüber dem runden $s(t)$?
A: Die runde Klammer steht für ein zeitkontinuierliches Signal (für jedes reelle $t$ definiert), die eckige für ein zeitdiskretes, das nur für ganze $n$ existiert. $\tilde s[n]$ ist formal eine Abbildung $\mathbb Z\to\mathbb R$ — eine Zahlenfolge.
F: Wie hängen Abtastperiode $T_s$ und Abtastrate $r$ zusammen, und was bedeuten sie?
A: $T_s$ ist der feste Zeitabstand zwischen zwei Messungen, $r=1/T_s$ die Zahl der Abtastwerte pro Sekunde (Hz). Ein kleineres $T_s$ bedeutet also eine höhere Abtastrate und dichtere Stichproben.
F: Aus welchen zwei Stufen besteht ein vollständiger A/D-Umsetzer, und warum braucht es beide?
A: Erstens der Abtaster (zeitliche Diskretisierung → $\tilde s[n]$), zweitens der Quantisierer, der jeden Wert auf endlich viele Stufen rundet (→ $\tilde s_q[n]$). Beide sind nötig, weil der Computer sowohl nur zu diskreten Zeiten misst als auch jede Zahl mit endlich vielen Binärstellen speichert.
F: Warum ist die normierte Kreisfrequenz $\hat\omega=\omega T_s$ dimensionslos?
A: $\omega$ hat die Einheit $1/\text{s}$, $T_s$ die Einheit s — ihr Produkt ist einheitenlos (in „rad"). Auch der Folgenindex $n$ ist dimensionslos, sodass $\tilde s[n]=A\cos(\hat\omega n+\varphi)$ ohne physikalische Zeiteinheit auskommt.
F: Warum hängt ein abgetasteter Sinus nur von $\hat\omega$ ab und nicht von $\omega$ und $r$ einzeln?
A: Setzt man $t=nT_s$ ein, erscheint $\omega$ und $T_s$ nur als Produkt $\omega T_s=\hat\omega$. Die Folge „sieht" also nur das Verhältnis $\hat\omega=2\pi T_s/T$ aus Abtastperiode und Signalperiode, nicht die beiden Größen getrennt.
F: Was bedeutet $\hat\omega=2\pi T_s/T$ anschaulich?
A: Es ist der Bruchteil einer Signalperiode, der zwischen zwei Abtastungen vergeht, mal $2\pi$. Klein ist $\hat\omega$, wenn viele Abtastwerte in eine Periode fallen; groß, wenn pro Periode nur wenige Stichproben genommen werden.
F: Warum lässt sich aus der Folge allein die absolute Frequenz des Originalsignals nicht rekonstruieren?
A: Weil $\tilde s[n]$ nur $\hat\omega$ enthält und $\hat\omega=\omega T_s$ ist, kennt man ohne die Abtastrate $r=1/T_s$ den Faktor nicht, mit dem man auf $\omega$ zurückrechnen müsste. Ohne $r$ ist die absolute Frequenz verloren.
F: Wieso können zwei verschiedene kontinuierliche Sinussignale dieselbe Abtastfolge ergeben?
A: Wenn ihre normierten Kreisfrequenzen bei gleicher Abtastrate zusammenfallen, liefern sie an allen Abtastzeitpunkten exakt dieselben Werte. Zwischen den Abtastpunkten unterscheiden sie sich zwar, aber dort misst man nicht — genau dieses Zusammenfallen ist Aliasing.
F: Warum betrachtet man in diesen Artikeln die „ideale" Abtastung ohne Quantisierung?
A: Um das grundlegende Phänomen (Verlust der absoluten Frequenz, Aliasing) sauber zu verstehen, blendet man den zusätzlichen Quantisierungsfehler aus. Dieser ist ein separater Effekt des Rundens und verdeckt sonst die zeitliche Diskretisierung als eigentliche Ursache.
:::
