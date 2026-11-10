---
title: Stufe 5: Besetzung und Ladungsneutralität
pfad: Elektrotechnik / 4. Semester / GEMB1 – Grundlagen elektronischer Materialien und Bauelemente 1 / Eigenhalbleiter und Dotierung
adresse: elektrotechnik/4-semester/elektronische-materialien-und-bauelemente-1/eigenhalbleiter-und-dotierung
knoten: Kapitel 11: Eigenhalbleiter und Dotierung
order: 4210700
summary: Im dotierten Kristall gilt n=p nicht mehr.
tags: Deltafunktion
lang: de
---

<span class="anker" id="stufe-5"></span>

:::zweck
Im dotierten Kristall gilt $n=p$ nicht mehr. Diese Stufe bestimmt, wie stark die Störstellen besetzt sind, und stellt die Gleichung auf, die $E_\mathrm F$ festlegt.
:::

**Die Idee.** Die Rechnung bleibt dieselbe: Plätze mal Besetzung. Neu sind drei Dinge. Die Störstellen liefern zusätzliche Plätze in der Lücke. Diese Plätze fassen nur ein Elektron. Und an die Stelle von $n=p$ tritt die Ladungsbilanz: Alle Elektronen wechseln nur die Zustände, verlassen den Kristall aber nicht. Also bleibt die Summe aller Ladungen null.

**Zustände der Störstellen.** Bis zu Dichten um $10^{19}\,\mathrm{cm^{-3}}$ sind die Donatoren so weit getrennt, dass sich ihre Wellenfunktionen nicht überlappen. Bei $10^{16}\,\mathrm{cm^{-3}}$ sind sie 46 nm voneinander entfernt, die Bahn misst 3,3 nm. Jedes Atom liefert also einen Zustand bei exakt derselben Energie. Das beschreibt die __Deltafunktion__ $\delta(x-x_0)$, die für $x\ne x_0$ null ist, bei $x_0$ unendlich und die Fläche 1 hat, sodass $\int\delta(x-x_0)\,g(x)\,\mathrm{d} x=g(x_0)$ für jede Funktion $g$ gilt:

<span class="anker" id="gl-5-1"></span>
$$D_\mathrm D(E)=N_\mathrm D\,\delta(E-E_\mathrm D),\qquad D_\mathrm A(E)=N_\mathrm A\,\delta(E-E_\mathrm A). \tag{5.1}$$

:::satz Satz 5.1 (Besetzung der Störstellen)
<span class="anker" id="satz-5-1"></span>

Besetzt heißt neutral. Dichte der neutralen und der ionisierten Donatoren, Dichte der ionisierten Akzeptoren:

<span class="anker" id="gl-5-2"></span>
<span class="anker" id="gl-5-3"></span>
$$\begin{aligned} f_\mathrm D&=\frac1{1+\frac12\exp\frac{E_\mathrm D-E_\mathrm F}{k_\mathrm BT}},\qquad N_\mathrm D^0=\int D_\mathrm D\,f_\mathrm D\,\mathrm{d} E=N_\mathrm D\,f_\mathrm D, \\ N_\mathrm D^+&=N_\mathrm D-N_\mathrm D^0=\frac{N_\mathrm D}{1+2\exp\frac{E_\mathrm F-E_\mathrm D}{k_\mathrm BT}},\qquad N_\mathrm A^-=\frac{N_\mathrm A}{1+g_\mathrm A\exp\frac{E_\mathrm A-E_\mathrm F}{k_\mathrm BT}}. \end{aligned} \tag{5.2|5.3}$$
:::

:::herleitung Woher die Faktoren kommen
Ein Platz im Band hat zwei Zustände, leer oder besetzt, mit dem Verhältnis $\mathrm{e}^{-(E-E_\mathrm F)/(k_\mathrm BT)}$. Der Donator hat drei: leer oder besetzt mit Spin auf oder Spin ab. Ein zweites Elektron kommt nicht hinein, die Coulomb-Abstoßung würde viel mehr kosten als $\Delta E_\mathrm D$. Also zählt „besetzt“ doppelt: $f_\mathrm D/(1-f_\mathrm D)=2\,\mathrm{e}^{-(E_\mathrm D-E_\mathrm F)/(k_\mathrm BT)}$. Auflösen ergibt [(5.2)](#gl-5-2). Mit $y=\frac12\exp\frac{E_\mathrm D-E_\mathrm F}{k_\mathrm BT}$ ist $1-f_\mathrm D=\frac{1+y}{1+y}-\frac1{1+y}=\frac y{1+y}=\frac1{1+1/y}$, und das ist der Bruch für $N_\mathrm D^+$.

Beim Akzeptor zählt das gebundene Loch: $f_\mathrm A=1/\bigl(1+\frac1{g_\mathrm A}\exp\frac{E_\mathrm F-E_\mathrm A}{k_\mathrm BT}\bigr)$ ist die Besetzung mit einem Loch, also die neutrale Form. Es hat die zwei Spinrichtungen. In Si, Ge und GaAs hat es zusätzlich die Wahl zwischen dem Band der leichten und dem der schweren Löcher ([Kapitel 9](/wissen/elektrotechnik/4-semester/elektronische-materialien-und-bauelemente-1/bandstrukturen-lesen/bandstrukturen-lesen.html)). Darum ist dort $g_\mathrm A=4$. Zählt man nur den Spin, ist $g_\mathrm A=2$.
:::

Für $E_\mathrm D-E_\mathrm F>3k_\mathrm BT$ ist der Exponentialterm klein, und $1/(1+\varepsilon)\approx1-\varepsilon$ ergibt

<span class="anker" id="gl-5-4"></span>
$$N_\mathrm D^+\approx N_\mathrm D\bigl[1-2\,\mathrm{e}^{-(E_\mathrm D-E_\mathrm F)/(k_\mathrm BT)}\bigr],\qquad N_\mathrm A^-\approx N_\mathrm A\bigl[1-g_\mathrm A\,\mathrm{e}^{-(E_\mathrm F-E_\mathrm A)/(k_\mathrm BT)}\bigr]. \tag{5.4}$$

:::satz Satz 5.2 (Ladungsneutralität)
<span class="anker" id="satz-5-2"></span>

Im thermodynamischen Gleichgewicht ist der homogene Halbleiter neutral:

<span class="anker" id="gl-5-5"></span>
$$p+N_\mathrm D^+-n-N_\mathrm A^-=0. \tag{5.5}$$
:::

⁠**So liest man das:** Positiv sind Löcher und ionisierte Donatoren, negativ Elektronen und ionisierte Akzeptoren. Im Eigenhalbleiter bleibt $p-n=0$. Die Gleichung heißt auch Elektroneutralitätsbedingung. Die fünf Unbekannten $E_\mathrm F$, $n$, $p$, $N_\mathrm D^+$, $N_\mathrm A^-$ sind durch [(0.1)](von-grund-auf-was-aus-fruheren-teilen-gebraucht-wird.html#gl-0-1), [(5.3)](#gl-5-3) und [(5.5)](#gl-5-5) festgelegt. Mit [(5.4)](#gl-5-4) lautet die Gleichung für $E_\mathrm F$

<span class="anker" id="gl-5-6"></span>
$$N_\mathrm V\mathrm{e}^{-\frac{E_\mathrm F-E_\mathrm V}{k_\mathrm BT}}+N_\mathrm D\bigl[1-2\mathrm{e}^{-\frac{E_\mathrm D-E_\mathrm F}{k_\mathrm BT}}\bigr]=N_\mathrm C\mathrm{e}^{-\frac{E_\mathrm C-E_\mathrm F}{k_\mathrm BT}}+N_\mathrm A\bigl[1-g_\mathrm A\mathrm{e}^{-\frac{E_\mathrm F-E_\mathrm A}{k_\mathrm BT}}\bigr]. \tag{5.6}$$

Sie lässt sich nur numerisch lösen, etwa mit dem Newton-Verfahren. Die Lösung ist eindeutig: Die positive Ladung fällt mit steigendem $E_\mathrm F$, die negative wächst (Abb. [5](#abb-5)). Überwiegt eine Sorte, entfällt die andere, oder sie wird über die effektive Dichte berücksichtigt. Ohne Akzeptoren bleibt $p+N_\mathrm D^+-n=0$.

:::abbildung gemb1/k11neutral 5
Links: Zustandsdichte mit dem Donatorniveau, nicht maßstäblich. Der Pfeil steht für die Deltafunktion. Rechts: Silizium mit $N_\mathrm D=10^{16}\,\mathrm{cm^{-3}}$ bei 300 K. Aufgetragen sind $n$, $p$ und $N_\mathrm D^+$ als Funktion der gedachten Lage von $E_\mathrm F$, gestrichelt die Summe $p+N_\mathrm D^+$. Im Schnittpunkt mit $n$ ist die Ladung ausgeglichen, dort liegt $E_\mathrm F$.
:::

::::beispiel
Die Probe aus dem Rechenmodell hat bei 300 K den Schnittpunkt bei $E_\mathrm C-E_\mathrm F=205$ meV. Dann ist $E_\mathrm D-E_\mathrm F=160$ meV $=6{,}2\,k_\mathrm BT$, und nach [(5.4)](#gl-5-4) sind $2\,\mathrm{e}^{-6{,}2}=0{,}40$ % neutral. Die Löcher mit $p=7{,}9\cdot10^{3}\,\mathrm{cm^{-3}}$ sind zwölf Zehnerpotenzen seltener als die Elektronen.
::::

⁠**Grenzfälle:** Für $E_\mathrm F\ll E_\mathrm D$ geht $N_\mathrm D^+$ gegen $N_\mathrm D$, für $E_\mathrm F\gg E_\mathrm D$ gegen null.

:::frage Bei $E=E_\mathrm F$ ist $f=\frac12$. Warum ist der Donator bei $E_\mathrm F=E_\mathrm D$ zu zwei Dritteln besetzt?
$f=\frac12$ gilt für einen Platz, der besetzt oder leer sein kann, mit je einer Möglichkeit. Der Donator hat zwei Möglichkeiten für besetzt und eine für leer. Bei gleichem Gewicht jeder Möglichkeit sind es $\frac23$ zu $\frac13$.
:::

:::aufgabe Aufgabe 6 ★★ Besetzung und Bilanz
<span class="anker" id="aufg-6"></span>

<ol class="al">

<li>

Welcher Anteil der Donatoren ist ionisiert für $E_\mathrm F=E_\mathrm D+2k_\mathrm BT$, $E_\mathrm D$, $E_\mathrm D-2k_\mathrm BT$ und $E_\mathrm D-3k_\mathrm BT$? Vergleiche mit $1-f$ der gewöhnlichen Fermi-Verteilung.

</li>

<li>

Welcher Anteil der Akzeptoren ist für $E_\mathrm F=E_\mathrm A+3k_\mathrm BT$ ionisiert, mit $g_\mathrm A=4$ und mit $g_\mathrm A=2$?

</li>

<li>

Si mit $N_\mathrm D=2\cdot10^{16}\,\mathrm{cm^{-3}}$ ($\Delta E_\mathrm D=45$ meV) und $N_\mathrm A=5\cdot10^{15}\,\mathrm{cm^{-3}}$ bei 150 K: Nimm an, alles ist ionisiert. Berechne $n$ und $E_\mathrm C-E_\mathrm F$. Prüfe die Annahme mit [(5.3)](#gl-5-3).

</li>

</ol>

:::loesung
(a) Mit $x=(E_\mathrm D-E_\mathrm F)/(k_\mathrm BT)=-2$, 0, 2, 3 ist der ionisierte Anteil $1/(1+2\mathrm{e}^{-x})=6{,}3$ %, 33 %, 79 %, 91 %. $1-f$ ergäbe 12 %, 50 %, 88 %, 95 %. (b) $g_\mathrm A=4$: 83 %, $g_\mathrm A=2$: 91 %. (c) $n=N_\mathrm D-N_\mathrm A=1{,}5\cdot10^{16}\,\mathrm{cm^{-3}}$. Mit $N_\mathrm C(150\,\mathrm{K})=9{,}96\cdot10^{18}\,\mathrm{cm^{-3}}$ und $k_\mathrm BT=12{,}93$ meV ist $E_\mathrm C-E_\mathrm F=84{,}0$ meV, also $E_\mathrm D-E_\mathrm F=3{,}0\,k_\mathrm BT$ und 91 % ionisiert. Die Annahme stimmt nur grob. Numerisch folgen $n=1{,}34\cdot10^{16}\,\mathrm{cm^{-3}}$ und 85,5 meV.
:::
:::
