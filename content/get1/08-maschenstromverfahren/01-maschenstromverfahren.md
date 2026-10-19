---
title: Das Maschenstromverfahren
pfad: Elektrotechnik / 1. Semester / Grundgebiete der Elektrotechnik 1 / Maschenstromverfahren
order: 80100
summary: Ein systematisches Schema, das ein Netzwerk mit möglichst wenigen Unbekannten löst – man rechnet nicht mit Zweigströmen, sondern mit umlaufenden Maschenströmen und einer übersichtlich aufgebauten Widerstandsmatrix.
tags: Maschenstromverfahren, Maschenstrom, Widerstandsmatrix, Netzwerkanalyse, Kirchhoff
---

:::konzept
Löst man ein Netzwerk direkt mit Kirchhoff, hat man eine Unbekannte pro Zweig — schnell werden das viele.
Das **Maschenstromverfahren** ist ein Trick, der die Zahl der Unbekannten auf das Nötigste drückt: Man führt für
jede Masche einen gedachten **umlaufenden Strom** ein. Weil so ein Kreisstrom in jeden Knoten genauso hinein-
wie hinausfließt, ist die Knotenregel **automatisch** erfüllt — man muss nur noch Maschengleichungen aufstellen
und ein kleines Gleichungssystem lösen.
:::

**Worum es geht:** Statt für jede Schaltung neu zu überlegen, liefert das __Maschenstromverfahren__ ein festes
Rezept, das sich mechanisch abarbeiten lässt und direkt auf ein lineares Gleichungssystem in Matrixform führt.

## Die Idee: Maschenströme statt Zweigströme

Ein __Maschenstrom__ ist ein fiktiver Strom, der eine Masche vollständig umläuft. Man nimmt für jede der
$m = z - (k-1)$ unabhängigen Maschen genau einen solchen Strom an. Der tatsächliche __Zweigstrom__ ergibt sich
später aus diesen Maschenströmen.

Der entscheidende Vorteil: Ein umlaufender Strom tritt in jeden Knoten der Masche ein und auch wieder aus — die
__Knotenregel__ ist dadurch von vornherein erfüllt. Es bleiben nur die $m$ __Maschengleichungen__, also deutlich
weniger Unbekannte als bei $z$ Zweigströmen.

Vorbereitung: Alle __Stromquellen__ werden zuvor in äquivalente __Spannungsquellen__ umgewandelt (mit der
Quellenumwandlung aus Kap. 7), damit in jeder Masche nur Spannungen zu bilanzieren sind.

:::grafik
Ein Netzwerk mit zwei Fenstern (Maschen), in jedes ist ein kreisförmiger Maschenstrom-Pfeil $I_1$ bzw. $I_2$
eingezeichnet (beide im Uhrzeigersinn). Im gemeinsamen Mittelzweig fließen beide, der Hinweis „dort
Zweigstrom $= I_1 - I_2$".
:::

## Die Gleichungen aufstellen

Das Schöne ist die feste Struktur. Für $m$ Maschen schreibt man das System als Matrixgleichung

$$\mathbf{R}\cdot\vec{I} = \vec{U},$$

mit der __Widerstandsmatrix__ $\mathbf{R}$, dem Vektor der gesuchten Maschenströme $\vec{I}$ und dem Vektor der
Quellenspannungen $\vec{U}$. Die Einträge folgen einer einfachen Regel:

- __$R_{ii}$__ (Diagonale): die __Summe aller Widerstände__ in Masche $i$.
- __$R_{ij}$__ (außerhalb der Diagonale): der __gemeinsame Widerstand__ von Masche $i$ und $j$, mit **negativem**
  Vorzeichen, wenn die beiden Maschenströme ihn gegensinnig durchfließen (der Normalfall bei gleichsinnig —
  etwa alle im Uhrzeigersinn — gewählten Maschenströmen).
- __$U_i$__ (rechte Seite): die __Summe der Quellenspannungen__ in Masche $i$, positiv, wenn die Quelle in
  Richtung des Maschenstroms treibt.

Die Matrix ist dabei immer **symmetrisch** ($R_{ij} = R_{ji}$) — eine nützliche Kontrolle beim Aufstellen.

## Rezept und Beispiel

**Schritt 1** — Stromquellen in Spannungsquellen umwandeln, unabhängige Maschen festlegen, in jede einen
Maschenstrom (z. B. alle im Uhrzeigersinn) einzeichnen.

**Schritt 2** — die Widerstandsmatrix nach obiger Regel hinschreiben. Für zwei Maschen, die sich den Widerstand
$R_2$ teilen (Masche 1 mit $U_0, R_1, R_2$; Masche 2 mit $R_2, R_3$):

$$\begin{aligned}
(R_1 + R_2)\,I_1 \;-\; R_2\,I_2 &= U_0,\\
-\,R_2\,I_1 \;+\; (R_2 + R_3)\,I_2 &= 0.
\end{aligned}$$

**Schritt 3** — das Gleichungssystem nach den Maschenströmen $I_1, I_2$ auflösen (einsetzen, Cramersche Regel
oder Gauß).

**Schritt 4** — die gesuchten __Zweigströme__ zurückgewinnen: Ein Zweig, der nur zu einer Masche gehört, trägt
deren Maschenstrom; ein von zwei Maschen geteilter Zweig trägt die **Differenz** der beiden Maschenströme (im
Beispiel fließt durch $R_2$ der Strom $I_1 - I_2$).

:::grafik
Die 2×2-Widerstandsmatrix des Beispiels mit hervorgehobener Struktur: Diagonale $R_1+R_2$ und $R_2+R_3$ (Summe
je Masche), Nebendiagonale $-R_2$ (gemeinsamer Widerstand, negativ), rechte Seite $U_0$ und $0$.
:::

:::kern
Das __Maschenstromverfahren__ nutzt umlaufende __Maschenströme__ als Unbekannte — dadurch ist die Knotenregel
automatisch erfüllt und es bleiben nur $m = z-(k-1)$ Gleichungen. Nach Umwandlung aller Stromquellen in
Spannungsquellen schreibt man $\mathbf{R}\,\vec{I} = \vec{U}$ mit $R_{ii}$ = Summe der Widerstände in Masche $i$,
$R_{ij}$ = −(gemeinsamer Widerstand) und $U_i$ = Summe der Quellenspannungen; die Matrix ist symmetrisch. Lösen,
dann __Zweigströme__ als Maschenstrom bzw. als **Differenz** zweier Maschenströme ablesen.
:::

Das Gegenstück dazu — mit Knotenpotentialen statt Maschenströmen als Unbekannten — ist das
__Knotenpotentialverfahren__, das sich besonders für Netze mit vielen Zweigen zwischen wenigen Knoten eignet.
