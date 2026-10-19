---
title: Die Fourier-Reihe
pfad: Elektrotechnik / 1. Semester / Mathematische Methoden der Elektrotechnik / Spektrum und Fourier-Reihe
order: 20200
summary: Von Grund auf – warum sich jedes periodische Signal aus Schwingungen der Grundfrequenz $\omega_T$ und ihren ganzzahligen Vielfachen zusammensetzt, warum gerade nur diese „Harmonischen" erlaubt sind, und wie man mit einem Orthogonalitäts-Trick genau ihre Anteile $a_k$ berechnet. Mit vollständiger Herleitung und dem Rechteck-Beispiel.
tags: Fourier-Reihe, periodisches Signal, Grundfrequenz, Harmonische, Fourierkoeffizienten, Orthogonalität, Rechteckschwingung
---

:::grafik
Einstiegs-Animation: Eine waagerechte Zielkurve zeigt eine **Rechteckschwingung**. Darunter wird sie Stück für
Stück aus Sinusschwingungen aufgebaut: zuerst nur die Grundschwingung (eine glatte Sinuskurve), dann kommt die
dritte Harmonische hinzu, dann die fünfte, siebte … Mit jeder weiteren Harmonischen schmiegt sich die Summe
enger an die Rechteckform an — die Kanten werden steiler, die Plateaus flacher. An den Sprungstellen bleibt ein
kleiner Überschwinger (das Gibbs-Phänomen) sichtbar. Kernbotschaft: Selbst eine eckige Kurve ist nur eine Summe
runder Sinusschwingungen.
:::

:::konzept
Im vorigen Abschnitt durften die Frequenzen in einem Signal beliebig sein. Bei einem **periodischen** Signal —
einem, das sich exakt wiederholt — ist das anders: Es besteht ausschließlich aus Schwingungen der
**Grundfrequenz** und deren **ganzzahligen Vielfachen**, den Harmonischen. Das ist die Kernaussage der
**Fourier-Reihe**, und sie ist erstaunlich: Egal wie kantig oder krumm ein periodisches Signal aussieht — es ist
immer eine Summe sauberer Sinusschwingungen, deren Frequenzen auf einem festen Raster sitzen.
:::

**Worum es geht:** Wir klären drei Dinge von Grund auf — *warum* ein periodisches Signal nur aus Harmonischen
bestehen kann, *wie* die __Fourier-Reihe__ es darstellt, und *wie* man mit einem Orthogonalitäts-Trick die
Anteile (die __Fourierkoeffizienten__ $a_k$) ausrechnet.

## Periodische Signale und die Grundfrequenz

Ein Signal heißt __periodisch__, wenn es sich nach einer festen Zeit, der __Periodendauer__ $T$, exakt
wiederholt: $s(t + T) = s(t)$ für alle $t$ (dabei ist $T$ die *kleinste* solche positive Zeit). Daraus ergeben
sich zwei feste Bezugsgrößen:

- die __Grundfrequenz__ $1/T$ — wie oft sich das Signal pro Sekunde wiederholt (in Hertz).
- __$\omega_T = \dfrac{2\pi}{T}$__: die __Grundkreisfrequenz__ — der Winkelzuwachs pro Sekunde einer Schwingung,
  die genau einmal pro Periode durchläuft.

Diese Grundfrequenz ist der „Taktgeber" des Signals. Alle Bausteine, aus denen es sich zusammensetzen darf,
müssen zu diesem Takt passen — warum, zeigt der nächste Abschnitt.

## Warum nur ganzzahlige Vielfache? (Harmonische)

Hier lohnt es, genau hinzusehen, denn die Antwort erklärt, warum die Fourier-Reihe überhaupt so aussieht, wie
sie aussieht. Die Frage: Welche Sinusschwingungen darf man addieren, damit die Summe wieder die Periode $T$
hat?

Eine Schwingung mit der Kreisfrequenz $\omega$ hat selbst die Periode $2\pi/\omega$. Damit die **Summe** sich
nach $T$ wiederholt, muss **jeder einzelne** Baustein nach $T$ wieder genau am Anfang stehen — er muss in der
Zeit $T$ also eine **ganze Zahl** von Schwingungen vollenden. Das bedeutet, seine Kreisfrequenz muss ein
ganzzahliges Vielfaches von $\omega_T$ sein:

$$\omega_k = k\,\omega_T, \qquad k = 1, 2, 3, \ldots$$

Erlaubt sind also nur die Grundkreisfrequenz $\omega_T$ und ihre **ganzzahligen Vielfachen** $2\omega_T,
3\omega_T, \ldots$ — die __Harmonischen__ (die $k$-te Harmonische hat die $k$-fache Grundfrequenz). Dazu kommt der
Gleichanteil (Frequenz $0$) als Mittelwert.

**Warum nicht eine beliebige Zwischenfrequenz?** Nähme man etwa eine Schwingung mit $\omega = 1{,}5\,\omega_T$
hinzu, so hätte diese nach $T$ gerade erst anderthalb Schwingungen hinter sich — sie stünde **nicht** wieder am
Anfang. Die Summe würde sich nach $T$ nicht mehr exakt wiederholen, wäre also gar nicht mehr periodisch mit $T$.
Eine nicht-ganzzahlige Frequenz zerstört die Periodizität. Genau deshalb — und nur deshalb — sind ausschließlich
die Harmonischen zugelassen.

:::grafik
Zwei Fälle über zwei Perioden $T$: Oben eine Harmonische (z. B. $3\omega_T$), die in $T$ genau drei volle
Schwingungen macht und am Ende wieder am Startwert ist — gestrichelt markiert, dass sich alles sauber
wiederholt. Unten eine „verbotene" Zwischenfrequenz ($1{,}5\,\omega_T$), die nach $T$ mitten in der Schwingung
steht; die Fortsetzung passt nicht zur ersten Periode — die Periodizität ist zerstört.
:::

## Die Fourier-Reihe (komplexe Form)

Damit lässt sich jedes periodische Signal als Summe seiner Harmonischen schreiben. Am elegantesten in komplexer
Form, mit rotierenden Zeigern (wie im Abschnitt über das Spektrum) für positive **und** negative Frequenzen:

$$s(t) = \sum_{k=-\infty}^{\infty} a_k\,e^{\,j k \omega_T t}.$$

- __$a_k$__: der komplexe __Fourierkoeffizient__ der $k$-ten Harmonischen — er enthält Amplitude und Phase dieser
  Teilschwingung (die Höhe und Lage der Spektrallinie bei $\omega_k = k\omega_T$). Es sind dieselben
  Spektralkoeffizienten $a_k$ wie im vorigen Abschnitt, nur jetzt für unendlich viele Harmonische.
- __$e^{\,j k \omega_T t}$__: der rotierende Einheitszeiger der $k$-ten Harmonischen.

Für ein **reelles** Signal sind die Koeffizienten konjugiert symmetrisch, $a_{-k} = a_k^{*}$ — genau die
Spiegelbild-Eigenschaft der positiven und negativen Spektrallinien aus dem vorigen Abschnitt. Die ganze
Information über das Signal steckt jetzt in der Zahlenfolge der $a_k$.

## Wie man die Koeffizienten findet: die Orthogonalität

Die große Frage ist: Wie bekommt man zu einem gegebenen Signal die Koeffizienten $a_k$ heraus? Hier könnte man
auf die Idee kommen, ein riesiges Gleichungssystem aufzustellen (das Signal an vielen Zeitpunkten gleich der
Summe setzen) — das wäre mühsam und unübersichtlich. Es geht viel eleganter, mit einer besonderen Eigenschaft
der Harmonischen.

**Der Schlüssel — die Orthogonalität.** Mittelt man das Produkt zweier harmonischer Zeiger über eine volle
Periode, so passiert etwas Bemerkenswertes:

$$\frac{1}{T}\int_{0}^{T} e^{\,j n \omega_T t}\,e^{-j k \omega_T t}\,\mathrm{d}t = \frac{1}{T}\int_{0}^{T} e^{\,j(n-k)\omega_T t}\,\mathrm{d}t = \begin{cases} 1, & n = k,\\[2pt] 0, & n \neq k. \end{cases}$$

Warum? Für $n = k$ ist der Integrand $e^{0} = 1$, das Mittel über eine Periode ist also $1$. Für $n \neq k$
dreht sich der Zeiger $e^{j(n-k)\omega_T t}$ in der Zeit $T$ genau $(n-k)$-mal **ganz** im Kreis — und ein
voller Umlauf mittelt sich zu null (für jede Position oben gibt es eine gegenüberliegende unten). Verschiedene
Harmonische „stören sich" beim Mitteln also nicht; nur die gleiche überlebt. (In der Sprache der
__Orthogonalität__: Mit dem Skalarprodukt $\langle s_1, s_2\rangle = \int_0^T s_1(t)\,s_2^{*}(t)\,\mathrm{d}t$
stehen verschiedene harmonische Zeiger „senkrecht" aufeinander.)

**Die Koeffizientenformel.** Diesen Effekt nutzt man wie ein Sieb. Man multipliziert die Fourier-Reihe mit
$e^{-j k \omega_T t}$ und mittelt über eine Periode. Nach der Orthogonalität bleibt von der ganzen Summe nur der
eine Term mit $n = k$ übrig:

$$\frac{1}{T}\int_{0}^{T} s(t)\,e^{-j k \omega_T t}\,\mathrm{d}t = \sum_{n} a_n\,\underbrace{\frac{1}{T}\int_{0}^{T} e^{\,j(n-k)\omega_T t}\,\mathrm{d}t}_{=\,1 \text{ nur für } n=k} = a_k.$$

Damit ist die Formel für die __Fourierkoeffizienten__ hergeleitet:

$$a_k = \frac{1}{T}\int_{0}^{T} s(t)\,e^{-j k \omega_T t}\,\mathrm{d}t.$$

In Worten: Man „fragt" das Signal, wie viel es von der $k$-ten Harmonischen enthält, indem man es mit deren
gegenläufigem Zeiger multipliziert und mittelt. Das Multiplizieren mit $e^{-jk\omega_T t}$ hält die $k$-te
Harmonische gleichsam „an" (ihr Produkt wird konstant), während alle anderen weiterrotieren und sich
wegmitteln.

:::grafik
Zwei Mittelungs-Bilder nebeneinander. Links: Produkt einer Harmonischen mit sich selbst — die Fläche unter der
Kurve ist über eine Periode deutlich von null verschieden (der Zeiger steht „still"). Rechts: Produkt zweier
**verschiedener** Harmonischer — die Kurve pendelt symmetrisch um null, die Flächen über und unter der Achse
heben sich auf, das Mittel ist null. Darunter das Fazit „gleiche Harmonische: bleibt; verschiedene: mitteln sich
weg".
:::

## Das Spektrum eines periodischen Signals

Trägt man die $|a_k|$ über der Kreisfrequenz auf, entsteht das Spektrum — und es ist ein **diskretes
Linienspektrum**: Es gibt nur Linien bei den Harmonischen $0, \omega_T, 2\omega_T, 3\omega_T, \ldots$ (und
spiegelbildlich bei den negativen). Dazwischen ist nichts. Das ist der entscheidende Unterschied zu einem
beliebigen Signal: Weil ein periodisches Signal nur aus Harmonischen besteht, sitzen seine Spektrallinien auf
einem festen, gleichmäßigen Raster mit dem Abstand $\omega_T$.

:::grafik
Das diskrete Amplitudenspektrum $|a_k|$ über der Kreisfrequenz: Linien ausschließlich bei $0, \omega_T,
2\omega_T, 3\omega_T, \ldots$ (und bei $-\omega_T, -2\omega_T, \ldots$), mit dem konstanten Linienabstand
$\omega_T$. Betont, dass dazwischen keine Anteile liegen.
:::

## Beispiel: die Rechteckschwingung

Rechnen wir es an einem konkreten, berühmten Fall durch. Die __Rechteckschwingung__ springt zwischen $+1$ (in
der ersten Halbperiode) und $-1$ (in der zweiten) hin und her. Einsetzen in die Koeffizientenformel und
Ausrechnen des Integrals über die beiden Hälften liefert (mit $\omega_T T = 2\pi$ und $e^{-jk\pi} = (-1)^k$):

$$a_k = \frac{j}{\pi k}\left((-1)^k - 1\right) = \begin{cases} -\dfrac{2j}{\pi k}, & k \text{ ungerade},\\[6pt] 0, & k \text{ gerade}. \end{cases}$$

Daraus liest man zwei Dinge ab:

- **Nur ungerade Harmonische.** Alle geraden Koeffizienten sind null — die Rechteckschwingung enthält nur
  $\omega_T, 3\omega_T, 5\omega_T, \ldots$
- **Amplituden fallen mit $1/k$.** Die höheren Harmonischen werden immer schwächer.

In reeller Schreibweise ist das die bekannte Reihe

$$s(t) = \frac{4}{\pi}\left(\sin\omega_T t + \frac{1}{3}\sin 3\omega_T t + \frac{1}{5}\sin 5\omega_T t + \ldots\right).$$

Genau das zeigt die Einstiegs-Animation: Mit jeder weiteren ungeraden Harmonischen wird die Summe eckiger. An
den Sprungstellen bleibt allerdings immer ein kleiner Überschwinger von rund $9\,\%$, der auch bei unendlich
vielen Gliedern nicht verschwindet — das __Gibbs-Phänomen__. Es zeigt anschaulich, dass sich ein echter,
unendlich steiler Sprung aus glatten Sinuskurven nur im Grenzwert, aber nie „perfekt an jeder Stelle" nachbilden
lässt.

:::grafik
Die Rechteck-Rekonstruktion in Stufen: die Grundschwingung allein, dann $+$ dritte Harmonische, dann $+$ fünfte,
$+$ siebte — jede Summe der Zielform näher. An den Sprungstellen der kleine, nicht verschwindende Überschwinger
(Gibbs) hervorgehoben. Daneben das zugehörige Linienspektrum mit nur ungeraden Linien und $1/k$-Abfall.
:::

:::kern
Ein __periodisches__ Signal (Periode $T$, Grundkreisfrequenz $\omega_T = 2\pi/T$) besteht ausschließlich aus
__Harmonischen__ — Schwingungen bei $\omega_k = k\omega_T$ —, weil nur ganzzahlige Vielfache nach $T$ wieder am
Anfang stehen (eine Zwischenfrequenz zerstört die Periodizität). Die __Fourier-Reihe__ ist
$s(t) = \sum_k a_k e^{jk\omega_T t}$ mit $a_{-k} = a_k^{*}$ für reelle Signale. Die __Fourierkoeffizienten__
findet man über die __Orthogonalität__ der Harmonischen (verschiedene mitteln sich über eine Periode weg):
$a_k = \tfrac{1}{T}\int_{0}^{T} s(t)\,e^{-jk\omega_T t}\,\mathrm{d}t$. Das Spektrum ist ein __diskretes
Linienspektrum__ im Raster $\omega_T$. Beispiel __Rechteckschwingung__: nur ungerade Harmonische mit
$1/k$-Abfall, $s(t) = \tfrac{4}{\pi}\sum_{k\,\text{ung.}}\tfrac1k\sin(k\omega_T t)$, mit Gibbs-Überschwinger an
den Sprüngen.
:::

Die Fourier-Reihe gilt für **periodische** Signale und liefert ein **diskretes** Spektrum. Lässt man die Periode
immer länger werden (das Signal wird „einmalig", nicht mehr periodisch), rücken die Spektrallinien immer enger
zusammen und verschmelzen zu einem **kontinuierlichen** Spektrum — das führt zur Fourier-Transformation für
nicht-periodische Signale.

:::quiz
F: Was ist die zentrale, überraschende Aussage der Fourier-Reihe?
A: Jedes periodische Signal — egal wie kantig oder krumm — ist eine Summe reiner Sinusschwingungen, deren Frequenzen ausschließlich auf einem festen Raster (Grundfrequenz und ihre ganzzahligen Vielfachen) sitzen. Selbst ein Rechteck ist nur eine Summe runder Schwingungen.
F: Warum dürfen nur ganzzahlige Vielfache der Grundfrequenz vorkommen?
A: Damit sich die Summe nach $T$ exakt wiederholt, muss jeder Baustein in der Zeit $T$ eine ganze Zahl von Schwingungen vollenden und wieder am Anfang stehen — das heißt $\omega_k=k\omega_T$. Nur dann bleibt die Summe periodisch mit $T$.
F: Was passiert, wenn man eine Zwischenfrequenz wie $1{,}5\,\omega_T$ hinzunimmt?
A: Diese Schwingung hätte nach $T$ erst anderthalb Perioden hinter sich, stünde also nicht wieder am Startwert. Die Summe würde sich nach $T$ nicht mehr exakt wiederholen — die Periodizität wäre zerstört. Darum sind Zwischenfrequenzen verboten.
F: Was bedeutet der Fourierkoeffizient $a_k$ anschaulich?
A: $a_k$ ist die komplexe Amplitude der $k$-ten Harmonischen — er enthält Stärke und Phase der Spektrallinie bei $\omega_k=k\omega_T$. Die ganze Information über das Signal steckt in der Zahlenfolge der $a_k$.
F: Warum gilt für ein reelles Signal $a_{-k}=a_k^*$?
A: Ein reeller Kosinus entsteht nur, wenn sich die Imaginärteile des mit $+\omega$ und des mit $-\omega$ rotierenden Zeigers aufheben — das verlangt konjugierte Koeffizienten. Diese Spiegelbild-Symmetrie ist das Erkennungszeichen eines reellen Signals.
F: Was besagt die Orthogonalität der Harmonischen?
A: Mittelt man das Produkt zweier harmonischer Zeiger über eine volle Periode, ergibt sich $1$ bei gleicher Harmonischer und $0$ bei verschiedenen. Verschiedene Harmonische „stören sich" beim Mitteln nicht — sie stehen im Sinne des Skalarprodukts senkrecht aufeinander.
F: Warum mittelt sich $e^{j(n-k)\omega_T t}$ für $n\neq k$ über eine Periode zu null?
A: Der Zeiger dreht in der Zeit $T$ genau $(n-k)$-mal voll im Kreis; zu jeder Position oben gibt es eine gegenüberliegende unten, sodass sich alle Beiträge aufheben. Nur für $n=k$ ist der Integrand konstant $1$ und das Mittel ungleich null.
F: Wie nutzt die Koeffizientenformel die Orthogonalität wie ein Sieb?
A: Man multipliziert die Reihe mit $e^{-jk\omega_T t}$ und mittelt über eine Periode. Alle Terme $n\neq k$ mitteln sich weg, nur der mit $n=k$ bleibt — übrig bleibt $a_k=\tfrac1T\int_0^T s(t)e^{-jk\omega_T t}\,dt$. Das Multiplizieren „hält die $k$-te Harmonische an", während die anderen weiterrotieren.
F: Warum hat ein periodisches Signal ein diskretes Linienspektrum?
A: Weil es nur aus Harmonischen besteht, sitzen die Spektrallinien ausschließlich bei $0,\omega_T,2\omega_T,\dots$ (und spiegelbildlich negativ), mit konstantem Abstand $\omega_T$. Dazwischen gibt es keine Anteile — anders als beim beliebigen Signal.
F: Was lehrt das Gibbs-Phänomen beim Rechteck über die Grenzen der Fourier-Darstellung?
A: An den Sprungstellen bleibt ein fester Überschwinger von ~9 %, der auch bei unendlich vielen Gliedern nicht verschwindet. Ein unendlich steiler Sprung lässt sich aus glatten Sinuskurven nur im Grenzwert (im Mittel), aber nie punktweise perfekt nachbilden.
:::
