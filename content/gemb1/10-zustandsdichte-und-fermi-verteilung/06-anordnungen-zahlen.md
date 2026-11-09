---
title: Stufe 4: Anordnungen zählen
pfad: Elektrotechnik / 4. Semester / Elektronische Materialien und Bauelemente 1 / Zustandsdichte und Fermi-Verteilung
order: 4200600
summary: Die Plätze sind gezählt.
tags: Mikrozustand, Verteilung, statistische Gewicht, Stirling-Formel
lang: de
---

<span class="anker" id="stufe-4"></span>

:::zweck
Die Plätze sind gezählt. Offen ist, mit welcher Wahrscheinlichkeit einer besetzt ist. Diese Stufe zählt dafür nicht Plätze, sondern Anordnungen von Elektronen auf Plätzen.
:::

**Die Idee.** Das Gitter stößt die Elektronen unablässig an, das System springt deshalb ständig von einer Anordnung zur nächsten. Die Grundannahme der Statistik lautet: Keine erlaubte Anordnung ist bevorzugt. Was man misst, ist dann die Verteilung, zu der die meisten Anordnungen gehören. Bei großen Zahlen ist sie so viel häufiger als alle anderen, dass man nur sie sieht. Keine Kraft schiebt die Elektronen dorthin, sie ist schlicht der wahrscheinlichste Fall.

**Das Modell.** Man teilt die Energieachse in schmale Gruppen der Breite $\mathrm{d} E$. Gruppe $i$ hat die Energie $E_i$ und enthält $g_i$ Plätze, also ist $g_i/\mathrm{d} E$ die Zustandsdichte, noch ohne das Teilen durch das Volumen. In ihr sitzen $N_i$ Elektronen. Elektronen sind nicht unterscheidbar, und jeder Platz fasst höchstens eines.

:::definition Definition 4.1 (Mikrozustand und statistisches Gewicht)
<span class="anker" id="satz-4-1"></span>

Ein __Mikrozustand__ ist eine vollständige Angabe, welche Plätze besetzt sind. Eine __Verteilung__ $(N_1,N_2,\dots)$ sagt nur, wie viele Elektronen je Gruppe sitzen. Das __statistische Gewicht__ $W$ ist die Zahl der Mikrozustände einer Verteilung:

<span class="anker" id="gl-4-1"></span>
$$W=\prod_i\frac{g_i!}{N_i!\,(g_i-N_i)!}=\prod_i\binom{g_i}{N_i}. \tag{4.1}$$
:::

⁠**So liest man das:** Der Binomialkoeffizient $\binom{g_i}{N_i}$ zählt, auf wie viele Arten man $N_i$ von $g_i$ Plätzen auswählt. Die Gruppen sind voneinander unabhängig, deshalb das Produkt. Nicht verwechseln: Ein Zustand ist eine Lösung der Schrödinger-Gleichung für ein Elektron, ein Mikrozustand eine Konfiguration aller Elektronen. Abb. [4](#abb-4) zeigt eine Gruppe mit $g_i=4$.

:::abbildung gemb1/k10mikro 4
Links Energiegruppen mit verschieden vielen Plätzen. Mitte: Eine Gruppe mit $g_i=4$ und $N_i=2$ hat sechs Mikrozustände. Rechts das Gewicht zweier gleicher Gruppen, die zusammen vier Elektronen teilen: Die ausgeglichene Verteilung $N_1=2$ hat die meisten Anordnungen.
:::

::::beispiel
Zwei Gruppen gleicher Energie mit je $g=4$ Plätzen teilen sich vier Elektronen. Für $N_1=0,\dots,4$ ist $W=1,16,36,16,1$, zusammen 70 Mikrozustände. Die ausgeglichene Verteilung $N_1=2$ tritt in 51 % der Fälle auf. Bei $g=40$ und 40 Elektronen liegt $N_1$ zu 96 % zwischen 16 und 24, und der Fall $N_1=0$ ist um den Faktor $5\cdot10^{-23}$ seltener als $N_1=20$. Für $g=10^{22}$ ist die relative Breite des Maximums $7\cdot10^{-12}$. Die häufigste Verteilung ist dann praktisch die einzige.
::::

:::definition Definition 4.2 (Entropie)
<span class="anker" id="satz-4-2"></span>

Die Entropie einer Verteilung ist

<span class="anker" id="gl-4-2"></span>
$$S=k_\mathrm B\ln W. \tag{4.2}$$
:::

⁠**So liest man das:** $S$ hat die Einheit J/K oder eV/K. Der Logarithmus macht aus dem Produkt der Gruppen eine Summe, die Entropie zweier Teile addiert sich also. Nur eine Anordnung, $W=1$, heißt $S=0$. Für die Gruppen ergibt [(4.1)](#gl-4-1)

<span class="anker" id="gl-4-3"></span>
$$\frac S{k_\mathrm B}=\sum_i\bigl[\ln(g_i!)-\ln(N_i!)-\ln\bigl((g_i-N_i)!\bigr)\bigr]. \tag{4.3}$$

Für große Zahlen ersetzt man die Fakultäten durch die __Stirling-Formel__ $\ln(n!)\approx n\ln n-n$. Bei $n=100$ ist $\ln(n!)=363{,}7$ und die Näherung 360,5, der Fehler 0,9 %. Aus [(4.3)](#gl-4-3) wird

<span class="anker" id="gl-4-4"></span>
$$\frac S{k_\mathrm B}\approx\sum_i\bigl[(g_i\ln g_i-g_i)-(N_i\ln N_i-N_i)-\bigl((g_i-N_i)\ln(g_i-N_i)-(g_i-N_i)\bigr)\bigr]. \tag{4.4}$$

⁠**Gültigkeit:** $N_i$ und $g_i-N_i$ müssen groß sein. In einem Kristall enthält schon ein Fenster von 1 meV in 1 cm$^3$ rund $10^{18}$ Plätze.

:::frage Warum landen nicht alle Elektronen so tief wie möglich?
Bei $T=0$ tun sie das, denn das Gitter kann keine Energie abgeben. Bei $T>0$ bietet es Energie an. Ein Elektron weiter oben ist dann erlaubt, und nach oben gibt es meist viel mehr leere Plätze, also mehr Anordnungen. Das Ergebnis ist ein Ausgleich zwischen wenig Energie und vielen Anordnungen.
:::

:::aufgabe Aufgabe 6 ★ Anordnungen von Hand
<span class="anker" id="aufg-6"></span>

<ol class="al">

<li>

Wie viele Mikrozustände hat eine Gruppe mit $g=5$, $N=2$?

</li>

<li>

Zwei gleiche Gruppen mit $g=3$ teilen sich drei Elektronen. Gib $W$ für alle Verteilungen an und prüfe die Summe mit $\binom63$.

</li>

<li>

Drei Gruppen mit je $g=3$ haben die Energien $0$, $\Delta E$, $2\Delta E$. Drei Elektronen haben zusammen die Energie $3\Delta E$. Welche Verteilungen sind möglich, und welche ist die häufigere?

</li>

<li>

Wie groß ist der Fehler der Stirling-Formel für $\ln(20!)$?

</li>

</ol>

:::loesung
(a) $\binom52=10$. (b) $W=1,9,9,1$ für $N_1=0,1,2,3$, Summe $20=\binom63$. (c) Es muss $N_1+N_2+N_3=3$ und $N_2+2N_3=3$ gelten. Das erlaubt $(0,3,0)$ mit $W=1$ und $(1,1,1)$ mit $W=3\cdot3\cdot3=27$. Die breite Verteilung ist 27-mal häufiger. (d) Exakt 42,34, Stirling 39,91, Fehler 5,7 %.
:::
:::
