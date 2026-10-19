---
title: Teilchen in der Box (2D)
pfad: Elektrotechnik / 4. Semester / Grundlagen elektronischer Materialien und Bauelemente / Quantenmechanik
order: 4010400
summary: Der Schritt von einer auf zwei Raumrichtungen – warum sich das 2D-Problem in zwei unabhängige 1D-Probleme zerlegen lässt, wie sich die Energien einfach addieren und wie bei einer quadratischen Box ein neues Phänomen auftaucht: die Entartung, bei der verschiedene Zustände dieselbe Energie haben.
tags: Potentialkasten, 2D, Separationsansatz, Quantenzahlen, Entartung, Quantendraht
---

:::grafik
Einstiegs-Animation: Eine rechteckige Box (Breiten $L_x$, $L_y$), in der eine zweidimensionale stehende Welle
schwingt — wie die Oberfläche einer eingespannten Trommel. Nacheinander erscheinen die Muster
$(n_x, n_y) = (1,1), (2,1), (1,2), (2,2)$: Berge und Täler, getrennt durch gerade __Knotenlinien__, an denen die
Welle null ist. Darunter als „Draufsicht" das Betragsquadrat $|\psi|^2$ als Gitter aus Wahrscheinlichkeitshügeln.
Kernbotschaft: In zwei Richtungen eingesperrt ergeben sich Muster aus zwei Quantenzahlen — je eine pro Richtung.
:::

:::konzept
Beim eindimensionalen Kasten war das Elektron nur in einer Richtung eingesperrt. In einem echten Bauelement ist
es oft in **zwei** (oder drei) Richtungen eingeschränkt. Der schöne Befund: Man muss dafür nicht von vorn
anfangen. Solange die „Wände" in $x$- und $y$-Richtung unabhängig voneinander sind, **zerfällt** das Problem in
zwei getrennte 1D-Kästen — und die Ergebnisse von dort addieren sich einfach. Ganz neu ist nur eine Folge der
Symmetrie: Bei einer quadratischen Box können **verschiedene** Zustände **dieselbe** Energie haben. Das nennt man
Entartung.
:::

**Worum es geht:** Wir übertragen das Teilchen in der Box auf zwei Raumrichtungen. Dabei sehen wir, *warum* der
__Separationsansatz__ funktioniert, wie die Energien aus den beiden 1D-Lösungen entstehen, und was __Entartung__
ist und woher sie kommt.

## Das Modell: der rechteckige Kasten

Wir sperren das Elektron in ein Rechteck der Breiten $L_x$ und $L_y$ ein — innen frei, außen unendlich hohe
Wände:

$$V(x,y) = \begin{cases} 0, & 0 < x < L_x \ \text{und}\ 0 < y < L_y,\\[2pt] \infty, & \text{sonst}. \end{cases}$$

Entscheidend ist, dass sich dieses Potential als **Summe** schreiben lässt: eine Wand-Struktur in $x$ plus eine
in $y$, die sich nicht gegenseitig beeinflussen. Genau das macht gleich die Zerlegung möglich. Die
Randbedingungen sind wie zuvor: $\psi = 0$ auf dem gesamten Rand des Rechtecks.

:::grafik
Die rechteckige Box in der Draufsicht: ein Rechteck der Breiten $L_x$ (waagerecht) und $L_y$ (senkrecht), innen
$V = 0$ (frei beweglich), außen ringsum unendlich hohe Wände (schraffiert). Hervorgehoben, dass die
Wellenfunktion auf dem **gesamten Rand** null ist.
:::

## Warum man das Problem zerlegen darf: der Separationsansatz

Die stationäre Schrödinger-Gleichung hat in zwei Dimensionen zwei Krümmungsterme (einen pro Richtung):

$$-\frac{\hbar^2}{2m}\left(\frac{\partial^2 \psi}{\partial x^2} + \frac{\partial^2 \psi}{\partial y^2}\right) = E\,\psi.$$

Weil die $x$- und die $y$-„Welt" unabhängig sind, probiert man einen __Produktansatz__: Die Wellenfunktion sei
ein Produkt aus einem reinen $x$-Teil und einem reinen $y$-Teil,

$$\psi(x,y) = X(x)\cdot Y(y).$$

**Schritt 1** — einsetzen und durch $X(x)Y(y)$ teilen. Dann steht da

$$-\frac{\hbar^2}{2m}\frac{X''(x)}{X(x)} \;-\; \frac{\hbar^2}{2m}\frac{Y''(y)}{Y(y)} = E.$$

**Schritt 2** — der erste Summand hängt **nur** von $x$ ab, der zweite **nur** von $y$, ihre Summe ist aber die
konstante Energie $E$. Das geht nur, wenn jeder Summand für sich konstant ist. Man nennt diese beiden Konstanten
$E_x$ und $E_y$, mit $E = E_x + E_y$.

**Schritt 3** — damit zerfällt alles in **zwei getrennte 1D-Kastenprobleme**, je eines für $X(x)$ und $Y(y)$ —
genau die Gleichung, die wir im vorigen Abschnitt schon gelöst haben. Die Lösungen und die Quantisierung
übernehmen wir direkt:

$$k_{x} = \frac{n_x\pi}{L_x}, \qquad k_{y} = \frac{n_y\pi}{L_y}, \qquad n_x, n_y = 1, 2, 3, \ldots$$

Der tiefere Grund, *warum* die Zerlegung klappt: Weil sich das Potential additiv in einen $x$- und einen
$y$-Anteil trennt, sind die Bewegungen in beide Richtungen **unabhängig** — und unabhängige Teilprobleme darf man
getrennt lösen und danach zusammensetzen.

:::grafik
Schema der Separation: Das 2D-Rechteck-Problem wird mit einem Pfeil in zwei 1D-Kästen aufgespalten — einen in
$x$-Richtung (liefert $X(x) = \sin(n_x\pi x/L_x)$) und einen in $y$-Richtung (liefert $Y(y) = \sin(n_y\pi y/L_y)$).
Darunter die Zusammensetzung $\psi(x,y) = X(x)\,Y(y)$ und $E = E_x + E_y$.
:::

## Die Zustände und ihre Energien

Die Eigenfunktionen sind also Produkte zweier Sinus-Wellen, und jeder Zustand trägt jetzt **zwei** Quantenzahlen:

$$\psi_{n_x, n_y}(x,y) = \frac{2}{\sqrt{L_x L_y}}\,\sin\!\left(\frac{n_x\pi x}{L_x}\right)\sin\!\left(\frac{n_y\pi y}{L_y}\right).$$

Die Energien sind die **Summe** der beiden 1D-Energien:

$$E_{n_x, n_y} = \frac{h^2}{8m}\left(\frac{n_x^2}{L_x^2} + \frac{n_y^2}{L_y^2}\right).$$

- __$n_x, n_y$__: die beiden __Quantenzahlen__ (eine pro Richtung, jeweils $\ge 1$).
- __$L_x, L_y$__: die __Breiten__ des Kastens in $x$ und $y$.

:::grafik
Die Energie als Summe zweier 1D-Beiträge: links die Energieleiter der $x$-Bewegung ($E_x \propto n_x^2/L_x^2$),
rechts die der $y$-Bewegung ($E_y \propto n_y^2/L_y^2$); ein „$+$" führt zur Gesamtenergie $E_{n_x,n_y} = E_x +
E_y$. Beispielhaft wird der Zustand $(n_x,n_y) = (2,1)$ aus der zweiten $x$-Sprosse und der ersten $y$-Sprosse
zusammengesetzt.
:::

In Worten: Die Bewegung in $x$ und in $y$ trägt jeweils ihre eigene „Teilchen-in-der-Box"-Energie bei, und beide
addieren sich. Die $|\psi_{n_x,n_y}|^2$-Muster zeigen entsprechend ein **Schachbrett** aus
Wahrscheinlichkeitshügeln, getrennt durch Knotenlinien.

:::grafik
Vier Dichteplots (Draufsicht auf die Box) für $(n_x,n_y) = (1,1), (2,1), (1,2), (2,2)$: $(1,1)$ ein einzelner
Hügel in der Mitte; $(2,1)$ und $(1,2)$ zwei Hügel nebeneinander bzw. übereinander (eine Knotenlinie); $(2,2)$
vier Hügel im Schachbrett. Knotenlinien (null) markiert.
:::

## Entartung: verschiedene Zustände, gleiche Energie

Jetzt das wirklich Neue gegenüber dem 1D-Fall. Betrachten wir eine **quadratische** Box, $L_x = L_y = L$. Dann
vereinfacht sich die Energie zu

$$E_{n_x, n_y} = \frac{h^2}{8mL^2}\left(n_x^2 + n_y^2\right).$$

Die Energie hängt also nur von der Summe $n_x^2 + n_y^2$ ab. Und hier passiert etwas, das es in 1D nicht gab:
**Verschiedene** Paare $(n_x, n_y)$ können **dieselbe** Summe und damit dieselbe Energie liefern. Das einfachste
Beispiel:

- Zustand $(1, 2)$: $\;n_x^2 + n_y^2 = 1 + 4 = 5$.
- Zustand $(2, 1)$: $\;n_x^2 + n_y^2 = 4 + 1 = 5$.

Beide haben dieselbe Energie $E = \tfrac{5 h^2}{8mL^2}$, sind aber **physikalisch verschiedene** Zustände (einmal
schwingt die Welle stärker in $x$, einmal in $y$). Dieses Zusammenfallen mehrerer verschiedener Zustände auf
einem Energieniveau heißt __Entartung__; die Anzahl der Zustände mit gleicher Energie ist der __Entartungsgrad__.

**Woher kommt die Entartung?** Aus der **Symmetrie** der quadratischen Box: Vertauscht man $x$ und $y$ (dreht die
Box um $90^\circ$), geht der Zustand $(1,2)$ in $(2,1)$ über — und weil die Box quadratisch ist, ändert sich die
Energie dabei nicht. Zerstört man die Symmetrie, indem man die Box ungleichseitig macht ($L_x \neq L_y$), fällt
die Entartung weg: Dann sind $(1,2)$ und $(2,1)$ wegen der unterschiedlichen Nenner wieder verschieden. Entartung
ist also immer ein Fingerzeig auf eine zugrunde liegende Symmetrie — ein Gedanke, der bei den Atomorbitalen (mit
ihrer Kugelsymmetrie) und im Kristall wiederkehrt.

:::grafik
Links die Energieleiter der quadratischen Box mit beschrifteten Niveaus; auf Höhe $E \propto 5$ liegen **zwei**
Zustände, markiert als $(1,2)$ und $(2,1)$ — ein entartetes Niveau. Daneben die beiden zugehörigen
$|\psi|^2$-Muster (zwei Hügel waagerecht bzw. senkrecht), verbunden durch einen 90°-Drehpfeil „Symmetrie der
quadratischen Box". Rechts: Macht man $L_x \neq L_y$, spalten die beiden Niveaus auf (Entartung aufgehoben).
:::

## Bezug zum Bauelement

Das 2D-Modell ist nicht nur Theorie. Sperrt man Elektronen in **zwei** Richtungen auf wenige Nanometer ein und
lässt sie nur in der dritten frei, entsteht ein __Quantendraht__ — ein Leiter, in dem sich Elektronen praktisch
nur noch entlang einer Linie bewegen. Die hier berechneten diskreten $(n_x, n_y)$-Niveaus sind dann die
„Kanäle", in denen der Strom fließt. Die Idee, Elektronen gezielt in einer, zwei oder drei Richtungen
einzusperren (Quantenfilm, Quantendraht, Quantenpunkt), ist eine der Grundideen der modernen Nanoelektronik —
und sie folgt vollständig aus der hier gezeigten Rechnung.

:::kern
Beim __2D-Kasten__ ($V=0$ im Rechteck, $\infty$ außen) trennt der __Separationsansatz__ $\psi(x,y) = X(x)Y(y)$
das Problem in zwei unabhängige 1D-Kästen — möglich, weil sich das Potential additiv in $x$ und $y$ trennt. Jeder
Zustand hat zwei __Quantenzahlen__: $\psi_{n_x,n_y} = \tfrac{2}{\sqrt{L_xL_y}}\sin(n_x\pi x/L_x)\sin(n_y\pi y/L_y)$,
und die Energien **addieren sich**: $E_{n_x,n_y} = \tfrac{h^2}{8m}\big(\tfrac{n_x^2}{L_x^2}+\tfrac{n_y^2}{L_y^2}\big)$.
Bei der **quadratischen** Box ($L_x=L_y$) tritt __Entartung__ auf — verschiedene $(n_x,n_y)$ mit gleichem
$n_x^2+n_y^2$ haben dieselbe Energie (z. B. $(1,2)$ und $(2,1)$); Ursache ist die Symmetrie, und bei $L_x\neq L_y$
verschwindet sie wieder. Technische Anwendung: der __Quantendraht__.
:::

Der nächste Schritt ist naheliegend: das Einsperren in **allen drei** Raumrichtungen — der __Quantenpunkt__ —,
mit dem die Reihe Quantenfilm/Quantendraht/Quantenpunkt vollständig wird und die wichtige Frage nach der
Zustandsdichte aufwirft.
