---
title: Teilchen in der Box (3D) und der Quantenpunkt
pfad: Elektrotechnik / 4. Semester / Grundlagen elektronischer Materialien und Bauelemente / Quantenmechanik
order: 4010500
summary: Der letzte Schritt der Reihe – ein Elektron in allen drei Richtungen eingesperrt. Die Rechnung läuft wie in 2D, nur mit drei Quantenzahlen; das Ergebnis ist der Quantenpunkt, ein „künstliches Atom". Damit wird klar, wie das Einsperren in einer, zwei oder drei Richtungen zu Quantenfilm, Quantendraht und Quantenpunkt führt.
tags: Potentialkasten, 3D, Quantenpunkt, Quantenfilm, Quantendraht, Zustandsdichte, Separationsansatz
---

:::grafik
Einstiegs-Animation: Ein würfelförmiger Kasten, in dem eine dreidimensionale stehende Welle „atmet"; als
Schnitt wird $|\psi|^2$ als Wolke aus Wahrscheinlichkeitshügeln sichtbar. Rechts daneben die große Übersicht:
ein Volumenkristall, aus dem nacheinander ein dünner Film (Einsperren in 1 Richtung → __Quantenfilm__), ein
dünner Draht (2 Richtungen → __Quantendraht__) und ein winziger Punkt (3 Richtungen → __Quantenpunkt__) werden —
mit den zugehörigen Energie-Darstellungen, die von „fast kontinuierlich" zu „scharf diskret" übergehen.
Kernbotschaft: Je mehr Richtungen man einsperrt, desto diskreter werden die Energien.
:::

:::konzept
Nach einer und zwei Richtungen kommt nun der letzte Schritt: ein Elektron, das in **allen drei** Raumrichtungen
eingesperrt ist. Die Rechnung bringt nichts grundlegend Neues mehr — sie läuft genau wie in 2D, nur mit einer
dritten Richtung und einer dritten Quantenzahl. Das Ergebnis ist aber technologisch aufregend: der
**Quantenpunkt**, ein nur wenige Nanometer großer Halbleiterkristall, der sich wie ein „künstliches Atom" mit
vollständig diskreten Energieniveaus verhält. Und rückblickend ordnet dieser Schritt die ganze Familie der
Nanostrukturen.
:::

**Worum es geht:** Wir übertragen das Teilchen in der Box auf drei Dimensionen, lesen die Energien ab und
verstehen damit die Reihe __Quantenfilm__ → __Quantendraht__ → __Quantenpunkt__ (Einsperren in 1, 2 bzw. 3
Richtungen) sowie einen ersten Blick darauf, wie sich dabei die __Zustandsdichte__ ändert.

## Das Modell und die Separation

Wir sperren das Elektron in einen Quader der Kantenlängen $L_x, L_y, L_z$ ein — innen frei, außen unendlich hohe
Wände. Weil sich das Potential wieder additiv in einen $x$-, $y$- und $z$-Anteil trennt, funktioniert der
__Separationsansatz__ genau wie in 2D, nur mit einem Faktor mehr:

$$\psi(x,y,z) = X(x)\,Y(y)\,Z(z).$$

Eingesetzt zerfällt die Schrödinger-Gleichung in **drei** unabhängige 1D-Kastenprobleme — je eines pro Richtung,
jedes mit seiner eigenen Quantenzahl $n_x, n_y, n_z$. Die Lösungen und ihre Quantisierung
($k = n\pi/L$) übernehmen wir unverändert aus dem 1D-Fall.

:::grafik
Der Quader (Kantenlängen $L_x, L_y, L_z$) mit einem Pfeil, der ihn in drei 1D-Kästen aufspaltet — je einen für
$X(x)$, $Y(y)$, $Z(z)$. Darunter die Zusammensetzung $\psi = X\,Y\,Z$ und $E = E_x + E_y + E_z$.
:::

## Zustände und Energien

Die Eigenfunktionen sind Produkte dreier Sinus-Wellen, mit drei Quantenzahlen:

$$\psi_{n_x,n_y,n_z}(x,y,z) = \sqrt{\frac{8}{L_x L_y L_z}}\;\sin\!\left(\frac{n_x\pi x}{L_x}\right)\sin\!\left(\frac{n_y\pi y}{L_y}\right)\sin\!\left(\frac{n_z\pi z}{L_z}\right).$$

Und die Energien sind — wie zu erwarten — die **Summe** der drei 1D-Beiträge:

$$E_{n_x,n_y,n_z} = \frac{h^2}{8m}\left(\frac{n_x^2}{L_x^2} + \frac{n_y^2}{L_y^2} + \frac{n_z^2}{L_z^2}\right).$$

- __$n_x, n_y, n_z$__: die drei __Quantenzahlen__ (eine pro Richtung, jeweils $\ge 1$).
- __$L_x, L_y, L_z$__: die __Kantenlängen__ des Quaders.

:::grafik
Drei Energieleitern nebeneinander (für $x$, $y$, $z$), verbunden durch „$+$" zur Gesamtenergie
$E = E_x + E_y + E_z$. Beispielhaft wird ein Zustand $(n_x,n_y,n_z) = (2,1,1)$ aus der zweiten $x$-Sprosse und den
jeweils ersten $y$- und $z$-Sprossen zusammengesetzt.
:::

**Entartung im Würfel.** Ist der Kasten ein Würfel ($L_x = L_y = L_z = L$), hängt die Energie nur von der Summe
$n_x^2 + n_y^2 + n_z^2$ ab. Dann sind — noch häufiger als in 2D — verschiedene Zustände entartet. Zum Beispiel
haben $(1,1,2)$, $(1,2,1)$ und $(2,1,1)$ alle die Summe $6$ und damit **dieselbe** Energie: ein dreifach
entartetes Niveau. Wie zuvor ist die Ursache die hohe Symmetrie des Würfels.

:::grafik
Energieniveaus des Würfels; auf Höhe $E \propto 6$ liegen **drei** Zustände, markiert als $(1,1,2)$, $(1,2,1)$,
$(2,1,1)$, verbunden durch Dreh-/Spiegelpfeile „Würfel-Symmetrie" — ein dreifach entartetes Niveau.
:::

## Die Reihe: Quantenfilm, Quantendraht, Quantenpunkt

Jetzt der große Zusammenhang. Entscheidend ist, in **wie vielen** Richtungen man das Elektron auf wenige
Nanometer einsperrt. In den eingesperrten Richtungen werden die Energien diskret; in den **freien** Richtungen
bewegt sich das Elektron weiter wie ein (fast) freies Teilchen mit kontinuierlicher Energie:

- **Einsperren in 1 Richtung** (dünne Schicht): __Quantenfilm__ — das Elektron ist in einer Ebene frei
  beweglich (ein zweidimensionales Elektronengas). Grundlage z. B. von Hochfrequenztransistoren.
- **Einsperren in 2 Richtungen** (dünner Draht): __Quantendraht__ — Bewegung nur noch entlang einer Linie.
- **Einsperren in 3 Richtungen** (winziger Punkt): __Quantenpunkt__ — in keiner Richtung mehr frei, **alle**
  Energien sind diskret.

Der __Quantenpunkt__ ist deshalb etwas Besonderes: Mit seinen vollständig diskreten Niveaus verhält er sich wie
ein **künstliches Atom** — nur dass man seine „Energieniveaus" über die Größe $L$ einstellen kann (Erinnerung:
$E \propto 1/L^2$). Genau das nutzen etwa Quantenpunkt-Displays, deren Leuchtfarbe allein von der Größe der
Kriställchen abhängt.

:::grafik
Vier Fälle nebeneinander (Volumen → Film → Draht → Punkt) mit der Zahl der eingesperrten Richtungen (0/1/2/3).
Unter jedem Fall sind die freien Richtungen als Pfeile und die eingesperrten als „Wände" dargestellt; darunter
die zugehörige schematische Energie-/Zustandsdarstellung, die von „quasikontinuierlich" (Volumen) bis „scharfe
diskrete Linien" (Quantenpunkt = künstliches Atom) reicht.
:::

## Ausblick: die Zustandsdichte hängt von der Dimension ab

Eine Folge ist so wichtig, dass sie ein eigenes Thema bekommt: Wie **viele** Zustände es in einem kleinen
Energiebereich gibt — die __Zustandsdichte__ $D(E)$ — hängt entscheidend davon ab, in wie vielen Richtungen das
Elektron frei ist. Qualitativ:

- **3D (Volumen):** $D(E)$ steigt glatt wie $\sqrt{E}$ an.
- **2D (Quantenfilm):** $D(E)$ ist eine **Treppenfunktion** (stufenweise konstant).
- **1D (Quantendraht):** $D(E)$ hat scharfe Spitzen an den Subband-Kanten.
- **0D (Quantenpunkt):** $D(E)$ besteht aus einzelnen, scharfen Linien (wie bei einem Atom).

Diese unterschiedlichen Formen sind der Grund, warum niederdimensionale Strukturen so andere elektronische und
optische Eigenschaften haben — und warum man sie gezielt herstellt. Die Herleitung folgt im Oberthema zur
Zustandsdichte.

:::grafik
Vier kleine $D(E)$-über-$E$-Diagramme nebeneinander: 3D (ansteigende Wurzelkurve), 2D (Treppe), 1D (Kurve mit
scharfen Spitzen an den Stufen), 0D (einzelne senkrechte Linien). Beschriftet mit „Volumen / Film / Draht /
Punkt".
:::

:::kern
Beim __3D-Kasten__ trennt der __Separationsansatz__ $\psi = X(x)Y(y)Z(z)$ das Problem in drei unabhängige
1D-Kästen; jeder Zustand hat drei __Quantenzahlen__, und die Energien addieren sich:
$E_{n_x,n_y,n_z} = \tfrac{h^2}{8m}\big(\tfrac{n_x^2}{L_x^2}+\tfrac{n_y^2}{L_y^2}+\tfrac{n_z^2}{L_z^2}\big)$. Im
__Würfel__ gibt es starke __Entartung__ (z. B. dreifach bei $(1,1,2),(1,2,1),(2,1,1)$). Die Zahl der
eingesperrten Richtungen ordnet die Nanostrukturen: __Quantenfilm__ (1), __Quantendraht__ (2), __Quantenpunkt__
(3 → vollständig diskret, „künstliches Atom", Farbe über die Größe). Entsprechend ändert sich die
__Zustandsdichte__ $D(E)$ (3D: $\sqrt{E}$, 2D: Treppe, 1D: Spitzen, 0D: Linien).
:::

Bisher waren die Wände **unendlich** hoch — das Elektron blieb perfekt gefangen. In Wirklichkeit sind Barrieren
endlich hoch, und dann passiert etwas, das es klassisch nicht gibt: Die Welle dringt in die Wand ein und kann
sie sogar **durchdringen**. Das ist der __Tunneleffekt__, das Thema des nächsten Abschnitts.
