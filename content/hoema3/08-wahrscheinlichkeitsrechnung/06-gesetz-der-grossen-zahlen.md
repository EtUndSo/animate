---
title: Das Gesetz der großen Zahlen
pfad: Elektrotechnik / 3. Semester / Höhere Mathematik 3 / Wahrscheinlichkeitsrechnung
order: 3080600
summary: Von Grund auf – warum sich der Zufall im Mittel herausmittelt. Für unabhängige Variablen addieren sich die Varianzen, also hat das Mittel $\overline X_n=\frac1n\sum X_i$ die Varianz $\sigma^2/n\to0$. Die Tschebyschew-Ungleichung liefert daraus das schwache Gesetz: $\overline X_n$ konvergiert stochastisch gegen $\mu$. Unter i.i.d. gilt sogar das starke Gesetz – fast sichere Konvergenz. So wird der Erwartungswert zum beobachtbaren Grenzwert relativer Häufigkeiten.
tags: Gesetz der großen Zahlen, i.i.d., stochastische Konvergenz, fast sichere Konvergenz, Tschebyschew, Varianz-Additivität, Mittelwert, relative Häufigkeit
---

:::grafik
Einstiegs-Animation: Ein Münzwurf, immer wieder wiederholt. Oben läuft die Folge der Einzelergebnisse (0/1,
zufällig zappelnd), darunter die __relative Häufigkeit__ $\overline X_n=\frac1n\sum_{i=1}^n X_i$ — anfangs
schwankend, dann enger und enger um den Erwartungswert $\mu=p$ einpendelnd. Ein schrumpfender $\varepsilon$-Schlauch
um $\mu$ zeigt: Die Streuung des Mittels ist $\mathrm{Var}(\overline X_n)=\sigma^2/n$ und geht gegen null. Rechts der
Unterschied __schwach__ (für festes großes $n$ liegt $\overline X_n$ mit hoher Wahrscheinlichkeit nahe $\mu$) vs.
__stark__ (fast jede einzelne unendliche Wurffolge konvergiert gegen $\mu$). Kernbotschaft: Mitteln vieler
unabhängiger Experimente macht den Zufall vorhersagbar — der Erwartungswert wird beobachtbar.
:::

:::konzept
Das __Gesetz der großen Zahlen__ ist die Brücke zwischen Theorie und Beobachtung: Es rechtfertigt, warum der abstrakte
__Erwartungswert__ $\mu$ tatsächlich der „im Mittel angenommene Wert" ist, den man an Daten abliest. Der Mechanismus
ist verblüffend einfach: Für unabhängige Variablen __addieren sich die Varianzen__ (Artikel 5), also hat das Mittel
$\overline X_n$ die Varianz $\sigma^2/n$ — sie schrumpft mit wachsendem $n$. Die __Tschebyschew-Ungleichung__
(Artikel 4) übersetzt das sofort in: Das Mittel bleibt mit immer höherer Wahrscheinlichkeit nahe bei $\mu$. Das ist
das __schwache Gesetz__ (stochastische Konvergenz). Unter der stärkeren i.i.d.-Annahme gilt sogar das __starke
Gesetz__: fast **jede** einzelne unendliche Versuchsreihe konvergiert gegen $\mu$.
:::

**Worum es geht:** Wir verallgemeinern __Unabhängigkeit__ auf $n$ Variablen (Produkt/Varianz-Additivität, Satz
8.53), beweisen das __schwache Gesetz__ (Satz 8.54) via Tschebyschew, führen __i.i.d.__ ein und formulieren das
__starke Gesetz__ (Satz 8.58, fast sichere Konvergenz).

## Unabhängigkeit mehrerer Zufallsvariablen

__Definition 8.49.__ $X_1,\dots,X_n$ heißen __unabhängig__, wenn die gemeinsame Verteilungsfunktion faktorisiert:
$$P(X_1\le x_1,\dots,X_n\le x_n)=P(X_1\le x_1)\cdots P(X_n\le x_n)\quad\text{für alle }(x_1,\dots,x_n).$$
__Bemerkung 8.50:__ (i) Wie bei Ereignissen reicht **paarweise** Unabhängigkeit nicht; die Produktformel muss für die
ganze Familie gelten. (ii) Eine Folge $(X_i)_{i\in\mathbb N}$ heißt unabhängig, wenn **jede** endliche Teilauswahl
unabhängig ist. Im diskreten Fall faktorisiert entsprechend die Wahrscheinlichkeitsfunktion (Bem. 8.51), im
absolut-stetigen die $n$-dimensionale Dichte (Satz 8.52: Randdichten durch Ausintegrieren, Unabhängigkeit ⟺
$f_X=f_{X_1}\cdots f_{X_n}$).

__Satz 8.53.__ Sind $X_1,\dots,X_n$ unabhängig (mit existierenden Momenten), so
$$\text{(i)}\quad E\Big(\prod_{i=1}^n X_i\Big)=\prod_{i=1}^n E(X_i),\qquad\text{(ii)}\quad \mathrm{Var}\Big(\sum_{i=1}^n X_i\Big)=\sum_{i=1}^n\mathrm{Var}(X_i).$$
Teil (ii) ist der entscheidende Baustein: Weil alle Kovarianzen verschwinden, addieren sich die Varianzen ohne
Mischterme.

## Das schwache Gesetz der großen Zahlen

Sei $(X_i)$ unabhängig mit gleichem $E(X_i)=\mu$ und $\mathrm{Var}(X_i)=\sigma^2$. Das __Stichprobenmittel__
$$\overline X_n:=\frac1n\sum_{i=1}^n X_i$$
hat nach der Linearität den Erwartungswert $E(\overline X_n)=\mu$, und mit $\mathrm{Var}(cX)=c^2\mathrm{Var}(X)$ und
Satz 8.53(ii) die Varianz
$$\mathrm{Var}(\overline X_n)=\frac{1}{n^2}\sum_{i=1}^n\mathrm{Var}(X_i)=\frac{n\sigma^2}{n^2}=\frac{\sigma^2}{n}.$$
Hier steckt der ganze Mechanismus: Das Mitteln drückt die Varianz um den Faktor $n$ herunter. Tschebyschew (Satz
8.37) gibt damit sofort
$$P\big(|\overline X_n-\mu|\ge\varepsilon\big)\le\frac{\mathrm{Var}(\overline X_n)}{\varepsilon^2}=\frac{\sigma^2}{n\varepsilon^2}\xrightarrow{n\to\infty}0.$$

__Satz 8.54 (Schwaches Gesetz).__ Für unabhängige $(X_i)$ mit gleichem $\mu$ und $\sigma^2$ gilt für jedes
$\varepsilon>0$
$$\lim_{n\to\infty}P\big(|\overline X_n-\mu|\ge\varepsilon\big)=0,\qquad\text{äquivalent}\quad \lim_{n\to\infty}P\big(|\overline X_n-\mu|<\varepsilon\big)=1.$$
Man sagt: Die Mittel $\overline X_n$ konvergieren __stochastisch__ gegen $\mu$. __Bemerkung 8.55:__ Es genügt sogar,
dass die Varianzen **gleichmäßig beschränkt** sind ($\mathrm{Var}(X_i)\le M$) — dann konvergiert
$\frac{S_n-E(S_n)}{n}$ stochastisch gegen $0$ (gleiche Verteilung ist nicht nötig).

:::grafik
Links die Varianz-Reduktion: Einzelverteilung mit Streuung $\sigma$, daneben die Verteilung von $\overline X_n$ mit
Streuung $\sigma/\sqrt n$ — immer schmaler um $\mu$. Rechts die Tschebyschew-Schranke $\sigma^2/(n\varepsilon^2)$, die
mit $n$ gegen null fällt; darunter der Unterschied „stochastisch" (Wahrscheinlichkeit großer Abweichung → 0) vs.
„fast sicher" (einzelne Pfade konvergieren).
:::

## Das starke Gesetz: fast sichere Konvergenz

Das schwache Gesetz sagt für **festes großes $n$**: $\overline X_n$ liegt meist nahe $\mu$. Intuitiv erwartet man
mehr — dass eine **einzelne** unendliche Wurffolge die relative Häufigkeit $\to\mu$ treibt. Das präzisiert man mit:

__Definition 8.56.__ $X_i$ heißen __identisch verteilt__, wenn alle $F_{X_i}$ (bzw. $p_{X_i}$, $f_{X_i}$) gleich sind.
Unabhängig und identisch verteilt heißt kurz __i.i.d.__ (independent, identically distributed). __Definition 8.59:__
Ein Ereignis tritt __fast sicher__ ein, wenn $P(A)=1$.

__Satz 8.58 (Starkes Gesetz).__ Für i.i.d. $(X_i)$ mit Erwartungswert $\mu$ gilt
$$P\Big(\big\{\omega:\lim_{n\to\infty}\tfrac1n\textstyle\sum_{i=1}^n X_i(\omega)=\mu\big\}\Big)=1.$$
Die Mittel konvergieren __fast sicher__ (punktweise für fast jedes $\omega$) gegen $\mu$. Das ist genau die Aussage,
dass die relative Häufigkeit von „Kopf" bei unendlich wiederholtem Münzwurf mit an Sicherheit grenzender
Wahrscheinlichkeit gegen $p$ strebt.

__Stark impliziert schwach (Bem. 8.60).__ Für die Ereignisse $A_n=\{|\overline X_k-\mu|\ge\varepsilon\ \text{für
ein }k\ge n\}$ bildet man eine **absteigende** Folge; nach der Stetigkeit des Maßes (Satz 8.4) ist $\lim_n
P(A_n)=P(A_\infty)$ mit $A_\infty=\bigcap_n A_n$. Dieser Durchschnitt enthält alle $\omega$, für die $\overline
X_n(\omega)\not\to\mu$ — nach dem starken Gesetz eine Nullmenge, $P(A_\infty)=0$. Da
$P(|\overline X_n-\mu|\ge\varepsilon)\le P(A_n)\to0$, folgt das schwache Gesetz. __Fast sichere Konvergenz ist also
stärker als stochastische__; umgekehrt gilt nur, dass eine **Teilfolge** fast sicher konvergiert.

**Stolperstein:** (1) __Schwach vs. stark__: schwach = stochastische Konvergenz (für festes großes $n$ meist nahe
$\mu$); stark = fast sichere Konvergenz (fast jeder einzelne Pfad konvergiert). Stark ⇒ schwach, nicht umgekehrt. (2)
Das schwache Gesetz braucht nur __Unabhängigkeit + beschränkte Varianz__, das starke die volle __i.i.d.__-Annahme.
(3) „Fast sicher" heißt $P=1$, **nicht** „für alle $\omega$" — eine Ausnahme-Nullmenge ist erlaubt. (4) Die
Varianz-Reduktion $\sigma^2/n$ braucht $\mathrm{Cov}=0$ (Unkorreliertheit); bei abhängigen Variablen gilt sie i. A.
nicht. (5) Das Gesetz sagt nichts über **einzelne** Ausgänge — der „Spielerfehlschluss" (nach vielen Kopf müsse Zahl
kommen) ist falsch; es mittelt nur über $n\to\infty$.

:::kern
__Unabhängigkeit__ von $X_1,\dots,X_n$ (Def. 8.49): gemeinsame Verteilungsfunktion faktorisiert (paarweise reicht
nicht; Folge: jede endliche Teilauswahl). __Satz 8.53__: unabhängig ⇒ $E(\prod X_i)=\prod E(X_i)$ und
$\mathrm{Var}(\sum X_i)=\sum\mathrm{Var}(X_i)$. __Stichprobenmittel__ $\overline X_n=\frac1n\sum X_i$: $E(\overline
X_n)=\mu$, $\mathrm{Var}(\overline X_n)=\sigma^2/n$ (Varianz-Reduktion!). __Schwaches Gesetz__ (Satz 8.54) via
Tschebyschew: $P(|\overline X_n-\mu|\ge\varepsilon)\le\frac{\sigma^2}{n\varepsilon^2}\to0$ — $\overline X_n\to\mu$
__stochastisch__ (genügt: Varianzen gleichmäßig beschränkt, Bem. 8.55). __i.i.d.__ (Def. 8.56): unabhängig +
identisch verteilt; __fast sicher__ (Def. 8.59): $P(A)=1$. __Starkes Gesetz__ (Satz 8.58): i.i.d. ⇒
$\overline X_n\to\mu$ __fast sicher__ (punktweise für fast jedes $\omega$). Stark ⇒ schwach (Bem. 8.60, via Satz
8.4); umgekehrt nur Teilfolge.
:::

Das Gesetz der großen Zahlen sagt, **wohin** das Mittel strebt ($\mu$), aber nicht, **wie** die Abweichung
$\overline X_n-\mu$ verteilt ist. Skaliert man sie richtig (mit $\sqrt n$), erscheint universell die Glockenkurve —
das ist der __zentrale Grenzwertsatz__, der krönende Abschluss des nächsten (und letzten) Artikels.

:::quiz
F: Warum schrumpft die Varianz des Stichprobenmittels $\overline X_n$ auf $\sigma^2/n$?
A: Für unabhängige Variablen addieren sich die Varianzen (Satz 8.53): $\mathrm{Var}(\sum X_i)=n\sigma^2$. Der Vorfaktor $\frac1n$ geht quadratisch ein ($\mathrm{Var}(c X)=c^2\mathrm{Var}(X)$), also $\mathrm{Var}(\overline X_n)=\frac{1}{n^2}\cdot n\sigma^2=\sigma^2/n$ — Mitteln drückt die Streuung mit $n$ herunter.
F: Wie folgt das schwache Gesetz aus der Tschebyschew-Ungleichung?
A: Tschebyschew gibt $P(|\overline X_n-\mu|\ge\varepsilon)\le\mathrm{Var}(\overline X_n)/\varepsilon^2=\sigma^2/(n\varepsilon^2)$. Für $n\to\infty$ geht die rechte Seite gegen null, also auch die Wahrscheinlichkeit großer Abweichungen — das ist genau die stochastische Konvergenz $\overline X_n\to\mu$.
F: Was bedeutet stochastische Konvergenz anschaulich?
A: Für jedes feste $\varepsilon>0$ wird die Wahrscheinlichkeit, dass das Mittel um mehr als $\varepsilon$ von $\mu$ abweicht, mit wachsendem $n$ beliebig klein. Bei großer Stichprobe liegt $\overline X_n$ also in den allermeisten Fällen nahe bei $\mu$ — eine Aussage über festes großes $n$.
F: Welche Voraussetzungen braucht das schwache Gesetz wirklich?
A: Es genügt Unabhängigkeit (bzw. verschwindende Kovarianzen) und gleichmäßig beschränkte Varianzen $\mathrm{Var}(X_i)\le M$ (Bem. 8.55); gleiche Verteilung ist nicht nötig. Entscheidend ist nur, dass die Varianz des Mittels gegen null geht.
F: Worin unterscheidet sich das starke vom schwachen Gesetz?
A: Das schwache Gesetz sagt, dass $\overline X_n$ für festes großes $n$ mit hoher Wahrscheinlichkeit nahe $\mu$ liegt (stochastisch). Das starke sagt, dass fast jede **einzelne** unendliche Folge $\overline X_n(\omega)$ gegen $\mu$ konvergiert (fast sicher) — eine Aussage über ganze Pfade, nicht nur einzelne $n$.
F: Was bedeutet i.i.d. und warum braucht das starke Gesetz diese stärkere Annahme?
A: i.i.d. heißt unabhängig und identisch verteilt — alle $X_i$ haben dieselbe Verteilung. Das starke Gesetz macht eine Aussage über das Langzeitverhalten ganzer unendlicher Folgen, und dafür braucht man die volle Gleichartigkeit der Experimente, nicht nur beschränkte Varianzen.
F: Was heißt „fast sicher", und warum ist das nicht dasselbe wie „immer"?
A: Fast sicher heißt $P(A)=1$, das Ereignis tritt mit Wahrscheinlichkeit $1$ ein. Es dürfen aber Ausnahme-$\omega$ existieren, solange sie eine Nullmenge bilden — z. B. die (an sich mögliche) Folge aus lauter Kopf hat Wahrscheinlichkeit $0$, verhindert die fast sichere Konvergenz aber nicht.
F: Warum impliziert das starke Gesetz das schwache, aber nicht umgekehrt?
A: Fast sichere Konvergenz kontrolliert das gesamte Restverhalten ab $n$; über die Stetigkeit des Maßes (Satz 8.4, absteigende Ereignisse) folgt daraus die stochastische. Umgekehrt sichert stochastische Konvergenz nur, dass eine Teilfolge fast sicher konvergiert — nicht die ganze Folge.
F: Wie rechtfertigt das Gesetz der großen Zahlen die Deutung des Erwartungswerts?
A: Es zeigt, dass der Durchschnitt vieler unabhängiger Wiederholungen gegen $\mu=E(X)$ strebt. Damit wird der abstrakt definierte Erwartungswert zum beobachtbaren Grenzwert der relativen Häufigkeiten — genau die intuitive Bedeutung „im Mittel angenommener Wert".
F: Warum ist der „Spielerfehlschluss" (nach vielen Kopf müsse bald Zahl kommen) mit dem Gesetz unvereinbar?
A: Das Gesetz macht nur eine Aussage über das Mittel bei $n\to\infty$, nicht über einzelne künftige Ausgänge. Bei unabhängigen Würfen ändert die Vergangenheit die Wahrscheinlichkeit des nächsten Wurfs nicht; die relative Häufigkeit nähert sich $p$ durch die schiere Masse weiterer Würfe, nicht durch „Ausgleich".
:::
