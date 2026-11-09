---
title: Stufe 7: Die Knotenregel ist Ladungserhaltung
pfad: Elektrotechnik / 1. Semester / Grundlagen der Elektrotechnik / Strom, Widerstand und Kirchhoff
order: 1120800
summary: Die erste Gleichungsart: Was verlangt die Erhaltung der Ladung an einem Knoten?
tags: 
lang: de
---

<span class="anker" id="stufe-7"></span>

:::zweck
Die erste Gleichungsart: Was verlangt die Erhaltung der Ladung an einem Knoten?
:::

**Die Idee.** Ein Knoten ist ein Stück Draht. Fließt mehr hinein als heraus, sammelt sich auf ihm Ladung, und sein Potenzial steigt. Dadurch sinkt die Spannung an den zuführenden Widerständen, und sie steigt an den abführenden. Der Zufluss nimmt ab, der Abfluss nimmt zu, bis beide gleich sind. Diese Selbstregelung läuft in Nanosekunden ab. Sie ist der Mechanismus hinter der Regel: Der Knoten stellt sich auf genau das Potenzial ein, bei dem nichts hängen bleibt.

:::satz Satz 7.1 (Knotenregel, erstes kirchhoffsches Gesetz)
<span class="anker" id="satz-7-1"></span>

Die Summe aller Ströme, die in einen Knoten hineinfließen, ist in jedem Zeitpunkt null. Gleichwertig ist die Summe der zufließenden Ströme gleich der Summe der abfließenden:

<span class="anker" id="gl-7-1"></span>
$$\sum_{\nu=1}^{N}I_\nu=0\quad\text{(alle Pfeile zum Knoten)},\qquad\sum I_\mathrm{zu}=\sum I_\mathrm{ab}. \tag{7.1}$$

Für ein Netz mit $k$ Knoten sind $k-1$ dieser Gleichungen unabhängig.
:::

⁠**So liest man das:** Die Pfeile sind frei wählbar. Zeigen alle zum Knoten, muss mindestens einer der Ströme negativ sein, oder alle sind null. Bei gemischten Pfeilen zählen zufließende positiv, abfließende negativ. **Gültigkeit:** Der Knoten darf keine nennenswerte Ladung speichern. Das gilt, solange sich die Ströme langsam gegen die Ausgleichszeit ändern. Die Herleitung gibt dafür eine Zahl.

:::abbildung et1/k2knoten 8
Links: Knoten mit zwei zufließenden und drei abfließenden Strömen, Summe je 7 mA. Rechts: Die Regel gilt auch für eine Hülle um einen Teil des Netzes, hier um $K_2$, $K_3$ und $R_\mathrm e$. Der Strom in $R_\mathrm e$ bleibt innen und zählt nicht.
:::

:::herleitung Knotenregel aus der Ladungserhaltung
Für die Ladung $Q_\mathrm K$ auf dem Knoten gilt $\mathrm{d} Q_\mathrm K/\mathrm{d} t=\sum I_\nu$, denn Ladung entsteht und verschwindet nicht. Wie klein $Q_\mathrm K$ bleibt, zeigt eine Abschätzung mit [Teil 1](/wissen/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/ladung-feld-und-potenzial/ladung-feld-und-potenzial.html): Eine Metallkugel mit 1 cm Radius hat das Potenzial $\varphi=k_\mathrm C\,Q/r$ mit der Coulomb-Konstante $k_\mathrm C=8{,}99\cdot10^{9}\,\mathrm{N\,m^2/C^2}$. Für 9 V reichen $Q=10$ pC. Ein Überschuss von 3 mA liefert das in 3,3 ns. Deshalb ist $\mathrm{d} Q_\mathrm K/\mathrm{d} t$ gegen die Ströme vernachlässigbar, und es bleibt $\sum I_\nu=0$.
:::

**Warum eine Gleichung überflüssig ist.** Jeder Zweig verbindet zwei Knoten. Sein Strom tritt deshalb in genau zwei Knotengleichungen auf, einmal mit $+$ (zufließend) und einmal mit $-$ (abfließend). Addiert man alle $k$ Gleichungen, heben sich alle Ströme auf. Eine Gleichung folgt also aus den übrigen, und jede Auswahl von $k-1$ Gleichungen ist unabhängig.

::::beispiel
Alle Strompfeile im Netz zeigen in Richtung des tatsächlichen Stroms: von $K_1$ durch die Widerstände nach unten, $I_\mathrm e$ von $K_2$ nach $K_3$, $I_0$ durch die Quelle von $K_4$ nach $K_1$. Die Knotengleichungen lauten

$$\begin{aligned} K_1:&\quad +I_0-I_\mathrm a-I_\mathrm c=0, & K_2:&\quad +I_\mathrm a-I_\mathrm b-I_\mathrm e=0,\\ K_3:&\quad +I_\mathrm c-I_\mathrm d+I_\mathrm e=0, & K_4:&\quad -I_0+I_\mathrm b+I_\mathrm d=0. \end{aligned}$$

Die Summe der ersten drei ist $I_0-I_\mathrm b-I_\mathrm d=0$, die vierte Gleichung mit umgekehrtem Vorzeichen. Addiert man nur $K_2$ und $K_3$, fällt $I_\mathrm e$ heraus, und es bleibt die Hülle aus Abb. [8](#abb-8): $I_\mathrm a+I_\mathrm c=I_\mathrm b+I_\mathrm d$. **Kontrolle:** An einem Punkt mit nur zwei Zweigen folgt $I_1=I_2$. Durch hintereinanderliegende Bauteile fließt derselbe Strom.
::::

:::frage Gilt die Regel auch, wenn an einem Knoten ein Kondensator hängt?
Ja. Der Strom zur Platte ist ein Zweigstrom wie jeder andere, die Ladung sammelt sich nicht auf dem Knoten, sondern auf der Platte. [Teil 3](/wissen/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/der-kondensator/der-kondensator.html) behandelt das.
:::

:::aufgabe Aufgabe 7 ★★ Knotenregel anwenden
<span class="anker" id="aufg-7"></span>

<ol class="al">

<li>

Vier Strompfeile zeigen zum Knoten: $I_1=5$ mA, $I_2=-2$ mA, $I_3=-1$ mA. Wie groß ist $I_4$, und in welche Richtung fließt er wirklich?

</li>

<li>

Zeige aus den Knotengleichungen des Netzes $I_0=I_\mathrm b+I_\mathrm d$. Welche Hülle gehört dazu?

</li>

<li>

Vorhersage: Ein Überschuss von nur 1 µ A bliebe 1 s lang auf der Kugel aus der Herleitung. Welches Potenzial hätte sie? Warum geschieht das nicht?

</li>

</ol>

:::loesung
(a) $5-2-1+I_4=0$, also $I_4=-2$ mA: Es fließen 2 mA aus dem Knoten heraus.

(b) Addition von $K_1$, $K_2$, $K_3$ gibt $I_0-I_\mathrm b-I_\mathrm d=0$. Das ist die Hülle um $K_1$, $K_2$, $K_3$ oder, gleichwertig, die Gleichung von $K_4$. Mit Zahlen: $4=1+3$.

(c) $Q=1\,\mu\text{C}$ ergibt $\varphi=k_\mathrm C\,Q/r=0{,}9$ MV. Lange bevor dieser Wert erreicht wäre, treibt das steigende Potenzial den Überschuss ab. Das ist die Selbstregelung.
:::
:::
