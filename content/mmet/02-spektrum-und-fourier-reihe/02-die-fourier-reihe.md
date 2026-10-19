---
title: Die Fourier-Reihe
pfad: Elektrotechnik / 1. Semester / Mathematische Methoden der Elektrotechnik / Spektrum und Fourier-Reihe
order: 20200
summary: Von Grund auf – warum sich jedes periodische Signal aus Schwingungen der Grundfrequenz und ihren ganzzahligen Vielfachen zusammensetzt, warum gerade nur diese „Harmonischen" erlaubt sind, und wie man mit einem Orthogonalitäts-Trick genau ihre Anteile berechnet. Mit vollständiger Herleitung und dem Rechteck-Beispiel.
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
Anteile (die __Fourierkoeffizienten__) ausrechnet.

## Periodische Signale und die Grundfrequenz

Ein Signal heißt __periodisch__, wenn es sich nach einer festen Zeit, der __Periodendauer__ $T_0$, exakt
wiederholt: $x(t + T_0) = x(t)$ für alle $t$. Daraus ergeben sich zwei feste Bezugsgrößen:

- __$f_0 = \dfrac{1}{T_0}$__: die __Grundfrequenz__ — wie oft sich das Signal pro Sekunde wiederholt.
- __$\omega_0 = 2\pi f_0 = \dfrac{2\pi}{T_0}$__: die __Grundkreisfrequenz__.

Diese Grundfrequenz ist der „Taktgeber" des Signals. Alle Bausteine, aus denen es sich zusammensetzen darf,
müssen zu diesem Takt passen — warum, zeigt der nächste Abschnitt.

## Warum nur ganzzahlige Vielfache? (Harmonische)

Hier lohnt es, genau hinzusehen, denn die Antwort erklärt, warum die Fourier-Reihe überhaupt so aussieht, wie
sie aussieht. Die Frage: Welche Sinusschwingungen darf man addieren, damit die Summe wieder die Periode $T_0$
hat?

Eine Schwingung mit der Frequenz $f$ hat selbst die Periode $1/f$. Damit die **Summe** sich nach $T_0$
wiederholt, muss **jeder einzelne** Baustein nach $T_0$ wieder genau am Anfang stehen — er muss in der Zeit
$T_0$ also eine **ganze Zahl** von Schwingungen vollenden. Das bedeutet $T_0 = k \cdot \tfrac{1}{f}$ mit einer
ganzen Zahl $k$, und aufgelöst:

$$f = k\,f_0, \qquad k = 1, 2, 3, \ldots$$

Erlaubt sind also nur die Grundfrequenz $f_0$ und ihre **ganzzahligen Vielfachen** $2f_0, 3f_0, \ldots$ — die
__Harmonischen__ (die $k$-te Harmonische hat die $k$-fache Grundfrequenz). Dazu kommt der Gleichanteil (Frequenz
$0$) als Mittelwert.

**Warum nicht eine beliebige Zwischenfrequenz?** Nähme man etwa eine Schwingung mit $f = 1{,}5\,f_0$ hinzu, so
hätte diese nach $T_0$ gerade erst anderthalb Schwingungen hinter sich — sie stünde **nicht** wieder am Anfang.
Die Summe würde sich nach $T_0$ nicht mehr exakt wiederholen, wäre also gar nicht mehr periodisch mit $T_0$. Eine
nicht-ganzzahlige Frequenz zerstört die Periodizität. Genau deshalb — und nur deshalb — sind ausschließlich die
Harmonischen zugelassen.

:::grafik
Zwei Fälle über zwei Perioden $T_0$: Oben eine Harmonische (z. B. $3f_0$), die in $T_0$ genau drei volle
Schwingungen macht und am Ende wieder am Startwert ist — gestrichelt markiert, dass sich alles sauber
wiederholt. Unten eine „verbotene" Zwischenfrequenz ($1{,}5\,f_0$), die nach $T_0$ mitten in der Schwingung
steht; die Fortsetzung passt nicht zur ersten Periode — die Periodizität ist zerstört.
:::

## Die Fourier-Reihe (komplexe Form)

Damit lässt sich jedes periodische Signal als Summe seiner Harmonischen schreiben. Am elegantesten in komplexer
Form, mit rotierenden Zeigern (wie im Abschnitt über das Spektrum) für positive **und** negative Frequenzen:

$$x(t) = \sum_{k=-\infty}^{\infty} c_k\,e^{\,j k \omega_0 t}.$$

- __$c_k$__: der komplexe __Fourierkoeffizient__ der $k$-ten Harmonischen — er enthält Amplitude und Phase dieser
  Teilschwingung (die Höhe und Lage der Spektrallinie bei $k f_0$).
- __$e^{\,j k \omega_0 t}$__: der rotierende Einheitszeiger der $k$-ten Harmonischen.

Für ein **reelles** Signal sind die Koeffizienten konjugiert symmetrisch, $c_{-k} = c_k^{*}$ — genau die
Spiegelbild-Eigenschaft der positiven und negativen Spektrallinien aus dem vorigen Abschnitt. Die ganze
Information über das Signal steckt jetzt in der Zahlenfolge der $c_k$.

## Wie man die Koeffizienten findet: die Orthogonalität

Die große Frage ist: Wie bekommt man zu einem gegebenen Signal die Koeffizienten $c_k$ heraus? Hier könnte man
auf die Idee kommen, ein riesiges Gleichungssystem aufzustellen (das Signal an vielen Zeitpunkten gleich der
Summe setzen) — das wäre mühsam und unübersichtlich. Es geht viel eleganter, mit einer besonderen Eigenschaft
der Harmonischen.

**Der Schlüssel — die Orthogonalität.** Mittelt man das Produkt zweier harmonischer Zeiger über eine volle
Periode, so passiert etwas Bemerkenswertes:

$$\frac{1}{T_0}\int_{0}^{T_0} e^{\,j m \omega_0 t}\,e^{-j k \omega_0 t}\,\mathrm{d}t = \frac{1}{T_0}\int_{0}^{T_0} e^{\,j(m-k)\omega_0 t}\,\mathrm{d}t = \begin{cases} 1, & m = k,\\[2pt] 0, & m \neq k. \end{cases}$$

Warum? Für $m = k$ ist der Integrand $e^{0} = 1$, das Mittel über eine Periode ist also $1$. Für $m \neq k$
dreht sich der Zeiger $e^{j(m-k)\omega_0 t}$ in der Zeit $T_0$ genau $(m-k)$-mal **ganz** im Kreis — und ein
voller Umlauf mittelt sich zu null (für jede Position oben gibt es eine gegenüberliegende unten). Verschiedene
Harmonische „stören sich" beim Mitteln also nicht; nur die gleiche überlebt.

**Die Koeffizientenformel.** Diesen Effekt nutzt man wie ein Sieb. Man multipliziert die Fourier-Reihe mit
$e^{-j k \omega_0 t}$ und mittelt über eine Periode. Nach der Orthogonalität bleibt von der ganzen Summe nur der
eine Term mit $m = k$ übrig:

$$\frac{1}{T_0}\int_{0}^{T_0} x(t)\,e^{-j k \omega_0 t}\,\mathrm{d}t = \sum_{m} c_m\,\underbrace{\frac{1}{T_0}\int_{0}^{T_0} e^{\,j(m-k)\omega_0 t}\,\mathrm{d}t}_{=\,1 \text{ nur für } m=k} = c_k.$$

Damit ist die Formel für die __Fourierkoeffizienten__ hergeleitet:

$$c_k = \frac{1}{T_0}\int_{0}^{T_0} x(t)\,e^{-j k \omega_0 t}\,\mathrm{d}t.$$

In Worten: Man „fragt" das Signal, wie viel es von der $k$-ten Harmonischen enthält, indem man es mit deren
gegenläufigem Zeiger multipliziert und mittelt. Das Multiplizieren mit $e^{-jk\omega_0 t}$ hält die $k$-te
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

Trägt man die $|c_k|$ über der Frequenz auf, entsteht das Spektrum — und es ist ein **diskretes Linienspektrum**:
Es gibt nur Linien bei den Harmonischen $0, f_0, 2f_0, 3f_0, \ldots$ (und spiegelbildlich bei den negativen).
Dazwischen ist nichts. Das ist der entscheidende Unterschied zu einem beliebigen Signal: Weil ein periodisches
Signal nur aus Harmonischen besteht, sitzen seine Spektrallinien auf einem festen, gleichmäßigen Raster mit dem
Abstand $f_0$.

:::grafik
Das diskrete Amplitudenspektrum $|c_k|$ über der Frequenz: Linien ausschließlich bei $0, f_0, 2f_0, 3f_0,
\ldots$ (und bei $-f_0, -2f_0, \ldots$), mit dem konstanten Linienabstand $f_0$. Betont, dass dazwischen keine
Anteile liegen.
:::

## Beispiel: die Rechteckschwingung

Rechnen wir es an einem konkreten, berühmten Fall durch. Die __Rechteckschwingung__ springt zwischen $+1$ (in
der ersten Halbperiode) und $-1$ (in der zweiten) hin und her. Einsetzen in die Koeffizientenformel und
Ausrechnen des Integrals über die beiden Hälften liefert (mit $\omega_0 T_0 = 2\pi$ und $e^{-jk\pi} = (-1)^k$):

$$c_k = \frac{j}{\pi k}\left((-1)^k - 1\right) = \begin{cases} -\dfrac{2j}{\pi k}, & k \text{ ungerade},\\[6pt] 0, & k \text{ gerade}. \end{cases}$$

Daraus liest man zwei Dinge ab:

- **Nur ungerade Harmonische.** Alle geraden Koeffizienten sind null — die Rechteckschwingung enthält nur
  $f_0, 3f_0, 5f_0, \ldots$
- **Amplituden fallen mit $1/k$.** Die höheren Harmonischen werden immer schwächer.

In reeller Schreibweise ist das die bekannte Reihe

$$x(t) = \frac{4}{\pi}\left(\sin\omega_0 t + \frac{1}{3}\sin 3\omega_0 t + \frac{1}{5}\sin 5\omega_0 t + \ldots\right).$$

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
Ein __periodisches__ Signal (Periode $T_0$, Grundfrequenz $f_0 = 1/T_0$) besteht ausschließlich aus __Harmonischen__
— Schwingungen bei $k f_0$ —, weil nur ganzzahlige Vielfache nach $T_0$ wieder am Anfang stehen (eine
Zwischenfrequenz zerstört die Periodizität). Die __Fourier-Reihe__ ist $x(t) = \sum_k c_k e^{jk\omega_0 t}$ mit
$c_{-k} = c_k^{*}$ für reelle Signale. Die __Fourierkoeffizienten__ findet man über die __Orthogonalität__ der
Harmonischen (verschiedene mitteln sich über eine Periode weg): $c_k = \tfrac{1}{T_0}\int_{0}^{T_0} x(t)\,e^{-jk\omega_0 t}\,\mathrm{d}t$.
Das Spektrum ist ein __diskretes Linienspektrum__ im Raster $f_0$. Beispiel __Rechteckschwingung__: nur ungerade
Harmonische mit $1/k$-Abfall, $x(t) = \tfrac{4}{\pi}\sum_{k\,\text{ung.}}\tfrac1k\sin(k\omega_0 t)$, mit
Gibbs-Überschwinger an den Sprüngen.
:::

Die Fourier-Reihe gilt für **periodische** Signale und liefert ein **diskretes** Spektrum. Lässt man die Periode
immer länger werden (das Signal wird „einmalig", nicht mehr periodisch), rücken die Spektrallinien immer enger
zusammen und verschmelzen zu einem **kontinuierlichen** Spektrum — das führt zur Fourier-Transformation für
nicht-periodische Signale.
