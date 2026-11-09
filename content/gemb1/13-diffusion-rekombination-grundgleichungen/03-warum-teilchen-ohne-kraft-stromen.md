---
title: Stufe 1: Warum Teilchen ohne Kraft strömen
pfad: Elektrotechnik / 4. Semester / Elektronische Materialien und Bauelemente 1 / Diffusion, Rekombination und Grundgleichungen
order: 4230300
summary: Bisher floss Strom nur, wenn ein Feld an den Ladungen zog.
tags: Konvektion, Teilchenkonzentration, Transportphänomen, Diffusionskoeffizient, Stoßquerschnitt
lang: de
---

<span class="anker" id="stufe-1"></span>

:::zweck
Bisher floss Strom nur, wenn ein Feld an den Ladungen zog. Eine ungleiche Dichte gleicht sich aber auch ohne jede Kraft aus. Diese Stufe findet das Gesetz dafür.
:::

**Die Idee.** Bei $T>0$ bewegt sich jedes Teilchen ungeordnet und stößt ständig mit anderen zusammen. Keine Richtung ist bevorzugt. Durch eine gedachte Ebene laufen deshalb Teilchen von beiden Seiten. Liegen links mehr Teilchen als rechts, kommen von links mehr (Abb. [1](#abb-1)). Es bleibt ein Nettostrom zur dünneren Seite, obwohl auf kein Teilchen eine Kraft in diese Richtung wirkt. Bei gleicher Dichte laufen die Teilchen weiter, aber von beiden Seiten gleich viele.

So vermischen sich zwei Gase in verbundenen Behältern, und so nimmt ein Siliziumkristall in einer Atmosphäre aus Boratomen Bor auf. Man dotiert auf diese Weise Halbleiter und härtet Metalle, etwa Stahl mit Chrom oder Kohlenstoff in einer dünnen Oberflächenschicht. Ein Duftstoff im Zimmer breitet sich dagegen vor allem durch __Konvektion__ (Luftbewegung) aus. Ohne sie würde ihn die Diffusion gleich verteilen.

:::abbildung gemb1/k13fick 1
Links: Teilchen, nach rechts dünner werdend. Durch die rote Ebene bei $x_\mathrm E$ läuft je eine Hälfte der Teilchen aus dem Abstand $l_\mathrm{mfp}$, von links mehr als von rechts. Rechts: die Dichte $N(x)$ an denselben drei Stellen.
:::

:::definition Definition 1.1 (Teilchenstromdichte)
<span class="anker" id="satz-1-1"></span>

Durchqueren je Zeit $\mathrm{d}\mathcal N/\mathrm{d} t$ Teilchen eine Fläche $A$ senkrecht zur $x$-Richtung, ist

<span class="anker" id="gl-1-1"></span>
$$\mathcal J=\frac1A\,\frac{\mathrm{d}\mathcal N}{\mathrm{d} t},\qquad[\mathcal J]=\mathrm{m^{-2}\,s^{-1}}. \tag{1.1}$$
:::

⁠**So liest man das:** $\mathcal N$ ist eine Teilchenzahl, $N=\mathcal N/V$ die __Teilchenkonzentration__. Haben alle Teilchen zusätzlich die gemeinsame Driftgeschwindigkeit $v_\mathrm d$, queren in $\mathrm{d} t$ alle aus dem Volumen $A\,v_\mathrm d\,\mathrm{d} t$ die Fläche, also ist $\mathcal J=N\,v_\mathrm d$. Ein Transport, den das Gefälle einer anderen Größe antreibt, heißt __Transportphänomen__: Ein Temperaturgefälle treibt die Wärmeleitung, ein Potentialgefälle den elektrischen Strom, ein Dichtegefälle die Diffusion.

:::satz Satz 1.2 (Erstes Fick-Gesetz, stationäre Diffusion)
<span class="anker" id="satz-1-2"></span>

Die Teilchenstromdichte ist dem Dichtegefälle proportional:

<span class="anker" id="gl-1-2"></span>
$$\mathcal J=-D\,\frac{\partial N}{\partial x}\quad\text{in einer Richtung},\qquad\boldsymbol{\mathcal J}=-D\operatorname{grad}N\quad\text{allgemein}. \tag{1.2}$$
:::

⁠**So liest man das:** $D$ ist der __Diffusionskoeffizient__ in cm$^2$/s (nicht die Zustandsdichte $D(E)$ aus [Teil 10](/wissen/elektrotechnik/4-semester/elektronische-materialien-und-bauelemente-1/zustandsdichte-und-fermi-verteilung/zustandsdichte-und-fermi-verteilung.html)). Das Minus sagt: Der Strom läuft zur kleineren Dichte. **Gültigkeit:** $N$ ändert sich auf der Länge $l_\mathrm{mfp}$ nur wenig.

:::herleitung Teilchen durch eine Ebene zählen
Ein Teilchen, das die Ebene bei $x_\mathrm E$ erreicht, hatte seinen letzten Stoß im Mittel im Abstand $l_\mathrm{mfp}$. $v$ sei der Betrag seiner Geschwindigkeit längs $x$. Von den Teilchen bei $x_\mathrm E-l_\mathrm{mfp}$ läuft die Hälfte nach rechts, von denen bei $x_\mathrm E+l_\mathrm{mfp}$ die Hälfte nach links:

$$\mathcal J=\tfrac12v\,N(x_\mathrm E-l_\mathrm{mfp})-\tfrac12v\,N(x_\mathrm E+l_\mathrm{mfp})\approx-v\,l_\mathrm{mfp}\,\frac{\partial N}{\partial x}.$$

Also ist $D=v\,l_\mathrm{mfp}=v^2\tau_\text{scat}$.
:::

:::zusatz Stöße im Gas
Ein Molekül mit Geschwindigkeit $v$ und Durchmesser $d_\mathrm M$ fliege durch ruhende Moleküle der Dichte $N$. Es trifft alle, deren Mittelpunkt in einer Röhre vom Querschnitt $\pi d_\mathrm M^2$ (__Stoßquerschnitt__) liegt. Die Stoßzahl je Zeit ist $Z=N\,v\,\pi d_\mathrm M^2$, also $\tau_\text{scat}=1/Z=1/(N\,v\,\pi d_\mathrm M^2)$, und die freie Weglänge $l_\mathrm{mfp}=v\tau_\text{scat}=1/(N\pi d_\mathrm M^2)$ hängt nicht von $v$ ab. Luft ($N=2{,}5\cdot10^{19}\,\mathrm{cm^{-3}}$, $d_\mathrm M=0{,}37$ nm, $v=470$ m/s) hat $Z=5\cdot10^{9}\,\mathrm{s^{-1}}$ und $l_\mathrm{mfp}=93$ nm.
:::

**Diffusion im Festkörper.** Im Kristall wandert ein Fremdatom durch Platzwechsel: Es tauscht den Gitterplatz mit einem Nachbarn oder springt auf einen Platz zwischen den Atomen. Jeder Sprung verlangt eine Mindestenergie $E_\text{Diff}$ aus der Wärmebewegung, und diese hat nur der Anteil $\exp(-E_\text{Diff}/(k_\mathrm BT))$:

<span class="anker" id="gl-1-3"></span>
$$D=D_0\exp\Bigl(-\frac{E_\text{Diff}}{k_\mathrm BT}\Bigr). \tag{1.3}$$

Bor wandert in Silizium über reguläre Gitterplätze, mit $D_0=6\,\mathrm{cm^2/s}$ und $E_\text{Diff}=3{,}6$ eV.

::::beispiel
Bei 1100 °C ist $k_\mathrm BT=118$ meV und $D=3{,}7\cdot10^{-13}\,\mathrm{cm^2/s}$. Fällt die Bordichte auf 1 µ m um $10^{19}\,\mathrm{cm^{-3}}$, ist $\mathcal J=3{,}7\cdot10^{10}\,\mathrm{cm^{-2}\,s^{-1}}$. Bei 1000 °C ist $D$ schon 11-mal kleiner, bei 300 K ist $D=2\cdot10^{-60}\,\mathrm{cm^2/s}$: Eine eingebaute Dotierung bleibt bei Raumtemperatur, wo sie ist.
::::

⁠**Grenzfälle:** Bei überall gleicher Dichte ist $\mathcal J=0$. Für $k_\mathrm BT\gg E_\text{Diff}$ strebt $D$ gegen $D_0$.

:::frage Woher „weiß“ ein Teilchen, wo die Dichte kleiner ist?
Es weiß es nicht. Jedes Teilchen läuft mit gleicher Wahrscheinlichkeit in jede Richtung. Der Strom entsteht erst beim Zählen, weil von der dichten Seite mehr Teilchen starten.
:::

:::aufgabe Aufgabe 1 ★ Diffusion berechnen
<span class="anker" id="aufg-1"></span>

<ol class="al">

<li>

Berechne $D$ für Bor bei 1000 °C und 1200 °C.

</li>

<li>

Bei 1000 °C fällt die Bordichte auf 0,5 µ m linear von $2\cdot10^{18}\,\mathrm{cm^{-3}}$ auf null. Wie groß ist $\mathcal J$? Wie viele Atome durchqueren 1 mm$^2$ in einer Stunde? Was ändert sich, wenn überall $10^{18}\,\mathrm{cm^{-3}}$ hinzukommen?

</li>

<li>

Ein Stoff hat $D=10^{-13}\,\mathrm{cm^2/s}$ bei 1000 °C und $8\cdot10^{-13}\,\mathrm{cm^2/s}$ bei 1100 °C. Bestimme $E_\text{Diff}$ und $D_0$.

</li>

</ol>

:::loesung
(a) Bei 1000 °C ist $D=3{,}4\cdot10^{-14}\,\mathrm{cm^2/s}$, bei 1200 °C ist $D=2{,}9\cdot10^{-12}\,\mathrm{cm^2/s}$, Faktor 86. (b) Gefälle $4\cdot10^{22}\,\mathrm{cm^{-4}}$, $\mathcal J=1{,}35\cdot10^{9}\,\mathrm{cm^{-2}\,s^{-1}}$. Durch 0,01 cm$^2$ in 3600 s gehen $4{,}9\cdot10^{10}$ Atome. Ein fester Zuschlag ändert nichts, denn nur die Steigung zählt. (c) $\ln(D_2/D_1)=(E_\text{Diff}/k_\mathrm B)(1/T_1-1/T_2)$ ergibt $E_\text{Diff}=3{,}1$ eV, damit $D_0=D_1\exp(E_\text{Diff}/(k_\mathrm BT_1))=0{,}25\,\mathrm{cm^2/s}$.
:::
:::
