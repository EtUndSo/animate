---
title: Stufe 8: Ergänzung: Das Metall als Potentialtopf
pfad: Elektrotechnik / 4. Semester / Elektronische Materialien und Bauelemente 1 / Zustandsdichte und Fermi-Verteilung
order: 4201000
summary: Im Metall liegt E mathrm F mitten im Band, die Boltzmann-Näherung versagt also.
tags: quasi-freien, Potentialtopf, Einelektronennäherung, Fermi-Kugel, Fermi-Temperatur, Fermi-Geschwindigkeit, spezifische Wärme
lang: de
---

<span class="anker" id="stufe-8"></span>

:::zweck
Im Metall liegt $E_\mathrm F$ mitten im Band, die Boltzmann-Näherung versagt also. Diese Stufe rechnet die Elektronen eines Metalls mit dem einfachsten Modell aus und zeigt, was klassisch nicht zu verstehen ist.
:::

**Die Idee.** Klassisch hätte ein Elektron die Energie $\frac32k_\mathrm BT$ und wäre bei $T=0$ in Ruhe. Das widerspricht der Quantenmechanik: Die Elektronen müssen sich wegen des Pauli-Prinzips auf immer höhere Niveaus stapeln, auch ohne Wärme. Das Modell: Die Kerne bilden mit den gebundenen Elektronen ein Potential, das die gebundenen Elektronen weitgehend abschirmen. Die beweglichen, die __quasi-freien__ Elektronen, spüren davon wenig. Man ersetzt es durch einen __Potentialtopf__ mit Wänden an der Oberfläche (Abb. [8](#abb-8)). Die Elektronen untereinander bleiben unberücksichtigt, das heißt __Einelektronennäherung__.

:::abbildung gemb1/k10metall 8
Links: Das Potential der Atomrümpfe (grau) und der Topf als Näherung. Mitte: Bei $T=0$ sind alle Zustände in der Fermi-Kugel mit Radius $k_\mathrm F$ besetzt, bei $T>0$ wird ihr Rand unscharf. Rechts: $D(E)$ (schwarz) und die besetzten Plätze $D\,f$ (blau), die Aufweichzone übertrieben breit.
:::

:::satz Satz 8.1 (Fermi-Energie bei $T=0$)
<span class="anker" id="satz-8-1"></span>

Für $n$ Elektronen je Volumen im Topf, $E$ vom Topfboden gemessen, gilt mit $m^*\approx m_0$

<span class="anker" id="gl-8-1"></span>
$$E_\mathrm{F0}=\frac{\hbar^2k_\mathrm F^2}{2m^*}=\frac{\hbar^2}{2m^*}\bigl(3\pi^2n\bigr)^{2/3},\quad k_\mathrm F=\bigl(3\pi^2n\bigr)^{1/3},\quad T_\mathrm F=\frac{E_\mathrm{F0}}{k_\mathrm B},\quad v_\mathrm F=\sqrt{\frac{2E_\mathrm{F0}}{m^*}}. \tag{8.1}$$
:::

:::herleitung Auffüllen bis $E_\mathrm{F0}$
Bei $T=0$ ist $f$ die Stufe aus [(6.1)](temperatur-und-boltzmann-naherung.html#gl-6-1). Mit $D(E)=(2m^*)^{3/2}\sqrt E/(2\pi^2\hbar^3)$ aus Stufe [2](kreisring-und-kugelschale.html#stufe-2) folgt

$$n=\int_0^{E_\mathrm{F0}}D(E)\,\mathrm{d} E=\frac{(2m^*)^{3/2}}{2\pi^2\hbar^3}\cdot\frac23\,E_\mathrm{F0}^{3/2}.$$

Auflösen ergibt [(8.1)](#gl-8-1). **Kontrolle:** Die Kugel mit Radius $k_\mathrm F$ fasst $2\cdot\frac43\pi k_\mathrm F^3/(2\pi/L)^3=L^3k_\mathrm F^3/(3\pi^2)$ Elektronen, je Volumen also $n=k_\mathrm F^3/(3\pi^2)$.
:::

⁠**So liest man das:** Die besetzten Zustände füllen im $k$-Raum die __Fermi-Kugel__ mit dem Fermi-Radius $k_\mathrm F$. $T_\mathrm F$ ist die __Fermi-Temperatur__, $v_\mathrm F$ die __Fermi-Geschwindigkeit__ der schnellsten Elektronen. Stehende Wellen im Topf sind Überlagerungen einer hinlaufenden und einer rücklaufenden Welle: Zu jedem $+\boldsymbol k$ gehört ein $-\boldsymbol k$, und im Mittel bewegt sich trotz der hohen Geschwindigkeiten keine Ladung.

::::beispiel
Kupfer: $E_\mathrm{F0}=7{,}03$ eV, rund 270-mal $k_\mathrm BT$. $k_\mathrm F=13{,}6\,\mathrm{nm^{-1}}$, $T_\mathrm F=8{,}2\cdot10^4$ K, das 60-Fache der Schmelztemperatur, und $v_\mathrm F=1{,}57\cdot10^6$ m/s, rund 13-mal so viel wie die klassische Geschwindigkeit $\sqrt{3k_\mathrm BT/m_0}$ bei 300 K. Mehr Elektronen je Volumen heben $E_\mathrm{F0}$.
::::

**Endliche Temperatur.** Ein Metall erwärmt seine Elektronen über Stöße mit dem Gitter, bei denen Phononen ([Teil 9](/wissen/elektrotechnik/4-semester/elektronische-materialien-und-bauelemente-1/bandstrukturen-lesen/bandstrukturen-lesen.html)) entstehen oder verschwinden. Aufnehmen können nur solche, die einen freien Platz in Reichweite finden, also die aus der Aufweichzone. Da $k_\mathrm BT\ll E_\mathrm F$ ist, ändert sich die Verteilung kaum, und der Anteil der angeregten Elektronen ist klein:

<span class="anker" id="gl-8-2"></span>
$$\frac{n_\mathrm{th}}n\approx\frac{4k_\mathrm BT}{E_\mathrm F},\qquad E_\mathrm F\approx E_\mathrm{F0}\Bigl(1-\frac{\pi^2}{12}\Bigl(\frac{k_\mathrm BT}{E_\mathrm{F0}}\Bigr)^2\Bigr). \tag{8.2}$$

Für Kupfer bei 300 K sind es 1,5 %. $E_\mathrm F$ sinkt, weil $D$ mit $E$ wächst: Über $E_\mathrm F$ gibt es mehr Plätze als darunter, bei fester Elektronenzahl muss $E_\mathrm F$ also etwas nach unten rücken, hier um 0,08 meV. Wärmeausdehnung, die $n$ verkleinert, und die Änderung der Bandstruktur senken $E_\mathrm F$ zusätzlich wenig.

**Spezifische Wärme.** Jedes angeregte Elektron nimmt rund $k_\mathrm BT$ auf. Die Wärmeenergie je Volumen ist also $w_\mathrm{th}\propto n\,(4k_\mathrm BT/E_\mathrm F)\,k_\mathrm BT$ und die __spezifische Wärme__ der Elektronen $c_V=\partial w_\mathrm{th}/\partial T$. Die exakte Rechnung ersetzt den Faktor 4 durch $\pi^2/4$:

<span class="anker" id="gl-8-3"></span>
$$c_V\approx\frac{\pi^2}2\,n\,k_\mathrm B\,\frac T{T_\mathrm F}. \tag{8.3}$$

Das ist linear in $T$, und Messungen bestätigen es. Bei Kupfer ist $c_V$ bei 300 K nur 1,2 % des klassischen Werts $\frac32nk_\mathrm B$. Die vielen Metallelektronen tragen zur Wärmekapazität also fast nichts bei.

:::frage Elektronen mit 1570 km/s bei $T=0$: Ist das Metall dann nicht heiß?
Nein. Temperatur misst nach [(5.1)](die-fermi-verteilung.html#gl-5-1) nicht die Bewegungsenergie, sondern wie viel Energie zu einem Zuwachs an Entropie gehört. Die Elektronen an der Kugeloberfläche können keine Energie abgeben, denn alle tieferen Plätze sind besetzt. Bei $T=0$ gibt es nur eine Anordnung, also $S=0$.
:::

:::aufgabe Aufgabe 10 ★★ Aluminium
<span class="anker" id="aufg-10"></span>

Aluminium ist FCC mit $a=0{,}4050$ nm ([Teil 6](/wissen/elektrotechnik/4-semester/elektronische-materialien-und-bauelemente-1/kristallgitter/kristallgitter.html)) und gibt drei Elektronen je Atom frei.

<ol class="al">

<li>

Berechne $n$, $E_\mathrm{F0}$, $k_\mathrm F$, $v_\mathrm F$ und $T_\mathrm F$.

</li>

<li>

Wie groß sind bei 300 K der Anteil $n_\mathrm{th}/n$ und die Absenkung von $E_\mathrm F$?

</li>

<li>

Berechne $c_V$ in J/(cm$^3$ K) und vergleiche mit $\frac32nk_\mathrm B$.

</li>

</ol>

:::loesung
(a) $n=3\cdot4/a^3=1{,}81\cdot10^{23}\,\mathrm{cm^{-3}}$, $E_\mathrm{F0}=11{,}65$ eV, $k_\mathrm F=17{,}5\,\mathrm{nm^{-1}}$, $v_\mathrm F=2{,}0\cdot10^6$ m/s, $T_\mathrm F=1{,}35\cdot10^5$ K. (b) $4k_\mathrm BT/E_\mathrm F=0{,}89\,\%$. Absenkung: relativ $4{,}1\cdot10^{-6}$, also 0,047 meV. (c) $c_V=(\pi^2/2)\,n\,k_\mathrm B\,T/T_\mathrm F=0{,}027$ J/(cm$^3$ K), klassisch 3,74 J/(cm$^3$ K). Das sind 0,73 %.
:::
:::
