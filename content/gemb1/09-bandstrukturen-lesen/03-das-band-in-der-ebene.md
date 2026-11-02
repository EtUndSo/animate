---
title: Stufe 1: Das Band in der Ebene
pfad: Elektrotechnik / 4. Semester / Elektronische Materialien und Bauelemente 1 / Bandstrukturen lesen
order: 4190300
summary: Teil 8 rechnete auf einer Kette.
tags: Hochsymmetriepunkt, Fläche konstanter Energie
lang: de
---

<span class="anker" id="stufe-1"></span>

:::zweck
[Teil 8](/wissen/elektrotechnik/4-semester/elektronische-materialien-und-bauelemente-1/vom-atom-zum-band/vom-atom-zum-band.html) rechnete auf einer Kette. Ein Kristall hat aber mehrere Richtungen. Diese Stufe überträgt die Rechnung auf ein Quadratgitter und zeigt, wie aus einer Fläche über der Brillouin-Zone das übliche Diagramm der Bandstruktur wird.
:::

**Die Idee.** Im Quadratgitter hat jedes Atom vier Nachbarn, zwei längs $x$ und zwei längs $y$. Jede Richtung trägt ihren eigenen Kosinus zur Energie bei. Aus der Zahl $k$ wird ein Vektor $\boldsymbol k=(k_x,k_y)$, aus der Kurve $E(k)$ eine Fläche über der Ebene. Die Einhüllende $\mathrm{e}^{\mathrm{j} k\ell a}$ wird zu $\mathrm{e}^{\mathrm{j}\boldsymbol k\cdot\boldsymbol R}$ mit $\boldsymbol R=\ell_1\boldsymbol a_1+\ell_2\boldsymbol a_2$, das Orbital am Platz heißt $|\ell_1,\ell_2\rangle$.

:::satz Satz 1.1 (Band des Quadratgitters)
<span class="anker" id="satz-1-1"></span>

Ein Kristall aus $N\times N$ Atomen mit $\boldsymbol a_1=(a,0)$, $\boldsymbol a_2=(0,a)$ und einem s-Orbital je Atom hat die Lösungen

<span class="anker" id="gl-1-1"></span>
$$|\psi_{k_x,k_y}\rangle=\frac1{\sqrt{N^2}}\sum_{\ell_1,\ell_2}\mathrm{e}^{\mathrm{j}\boldsymbol k\cdot\boldsymbol R}\,|\ell_1,\ell_2\rangle \tag{1.1}$$

mit der Energie

<span class="anker" id="gl-1-2"></span>
$$E(k_x,k_y)=E_\mathrm s-2V_\mathrm{ss}\cos(k_xa)-2V_\mathrm{ss}\cos(k_ya),\qquad-\frac\pi a\le k_x,k_y\le\frac\pi a. \tag{1.2}$$
:::

:::herleitung Das Rezept mit Zahlen statt Matrizen
Die Zelle ist ein Quadrat der Kante $a$ (Schritt 1), gewählt ist ein s-Orbital (2), also $M=1\cdot1=1$ (3). Mit den vier Nachbarzellen ist $\#=5$ (4). Die Mitte trägt $E_\mathrm s$, jede Nachbarzelle $-V_\mathrm{ss}$ (5 bis 7), die Phasen sind $\mathrm{e}^{\pm\mathrm{j} k_xa}$ und $\mathrm{e}^{\pm\mathrm{j} k_ya}$ (8). Schritt 9 ergibt

$$E(k_x,k_y)=-V_\mathrm{ss}\mathrm{e}^{\mathrm{j} k_xa}-V_\mathrm{ss}\mathrm{e}^{\mathrm{j} k_ya}-V_\mathrm{ss}\mathrm{e}^{-\mathrm{j} k_xa}-V_\mathrm{ss}\mathrm{e}^{-\mathrm{j} k_ya}+E_\mathrm s.$$

Mit $\mathrm{e}^{\mathrm{j} x}+\mathrm{e}^{-\mathrm{j} x}=2\cos x$ folgt [(1.2)](#gl-1-2). Die Summe in [(1.1)](#gl-1-1) hat $N^2$ gleich große Glieder, daher die Normierung.
:::

⁠**So liest man das:** $\boldsymbol k\cdot\boldsymbol R=\ell_1k_xa+\ell_2k_ya$ ist die Phase am Platz. Die Fläche [(1.2)](#gl-1-2) sieht aus wie ein Eierkarton und reicht von $E_\mathrm s-4V_\mathrm{ss}$ bis $E_\mathrm s+4V_\mathrm{ss}$. Bei $\boldsymbol k=0$ haben alle Nachbarn gleiches Vorzeichen, jedes Paar bindet. An der Ecke der Zone wechselt es in beide Richtungen, jedes Paar ist antibindend. Die Zone ist ein Quadrat der Kante $2\pi/a$ mit $N^2$ Werten von $\boldsymbol k$.

:::definition Definition 1.2 (Bandstruktur und Flächen konstanter Energie)
<span class="anker" id="satz-1-2"></span>

Ein __Hochsymmetriepunkt__ ist ein Punkt der Brillouin-Zone, der bei den Drehungen und Spiegelungen des Kristalls in sich oder in einen gleichwertigen Punkt übergeht. Im Quadrat sind das $\Gamma=(0,0)$, die Mitte der Zone, $X=(\pi/a,0)$, die Mitte einer Kante, und $M=(\pi/a,\pi/a)$, eine Ecke. Die Bandstruktur zeigt $E$ längs eines Wegs durch solche Punkte, hier $\Gamma\to X\to M\to\Gamma$. Eine __Fläche konstanter Energie__ enthält alle $\boldsymbol k$ mit demselben $E$. In der Ebene ist sie eine Linie.
:::

:::abbildung gemb1/k9quadrat 1
Quadratgitter mit $E_\mathrm s=-5$ eV und $V_\mathrm{ss}=0{,}5$ eV. Links: Zone mit dem Weg (Pfeile) und blau den Linien konstanter Energie, Zahlen in eV. Unten sind sie fast Kreise, bei $E=-5$ eV ein Quadrat über Eck. Rechts: Die Bandstruktur ist die Fläche [(1.2)](#gl-1-2) längs des Wegs, in denselben Farben.
:::

Ein Weg genügt, weil die Symmetrie viele Richtungen gleichwertig macht. Das Dreieck $\Gamma XM$ wiederholt sich achtmal in der Zone.

**Beispiel.** Im Rechenmodell ist $E(\Gamma)=-7$ eV, $E(X)=-5$ eV, $E(M)=-3$ eV, die Zone endet bei $\pi/a=12{,}57\,\mathrm{nm^{-1}}$. Nahe $\Gamma$ gilt $\cos x\approx1-x^2/2$, also $E\approx E_\mathrm s-4V_\mathrm{ss}+V_\mathrm{ss}a^2(k_x^2+k_y^2)$. Das sind Kreise mit $m^*=\hbar^2/(2V_\mathrm{ss}a^2)=1{,}22\,m_0$ in beiden Richtungen. Bei $E=E_\mathrm s$ ist $\cos(k_xa)+\cos(k_ya)=0$, also $|k_x|+|k_y|=\pi/a$: Aus dem Kreis wird ein Quadrat, denn das Gitter ist nicht rund. Bei $X$ ist die Steigung null, doch $X$ ist kein Extremum. Die Massen sind dort $-1{,}22\,m_0$ längs $x$ und $+1{,}22\,m_0$ längs $y$, die Fläche hat einen Sattel. **Grenzfall:** Für $k_y=0$ bleibt das Band der Kette, um $2V_\mathrm{ss}$ nach unten geschoben. **Drei Dimensionen:** Im einfach kubischen Gitter kommt $-2V_\mathrm{ss}\cos(k_za)$ dazu, die Breite wird $12V_\mathrm{ss}$. Kurz gesagt: In allen Gittern dieses Kapitels ist die Bandbreite das Doppelte der Summe der Kopplungen zu allen Nachbarn.

:::frage Läuft das Elektron diesen Weg $\Gamma\to X\to M\to\Gamma$ entlang?
Nein. $\boldsymbol k$ ist kein Ort, und der Weg ist keine Bahn. Jeder Punkt der Zone gehört zu einem eigenen Zustand, der Weg wählt nur aus, welche Zustände im Diagramm erscheinen.
:::

:::aufgabe Aufgabe 1 ★★ Ein Rechteckgitter
<span class="anker" id="aufg-1"></span>

Ein Gitter hat die Kanten $a_x=0{,}3$ nm und $a_y=0{,}5$ nm, $E_\mathrm s=-4$ eV und die Kopplungen $V_x=0{,}8$ eV, $V_y=0{,}2$ eV.

<ol class="al">

<li>

Führe das Rezept durch und gib $E(k_x,k_y)$ an. Warum ist $V_x$ größer als $V_y$?

</li>

<li>

Berechne die Zonenränder und die Energien an $\Gamma$, $X=(\pi/a_x,0)$, $Y=(0,\pi/a_y)$ und an der Ecke.

</li>

<li>

Bestimme $m_x$ und $m_y$ bei $\Gamma$. Vorhersage: Welche Form haben die Linien konstanter Energie knapp über dem Minimum, und welche Achse ist länger?

</li>

</ol>

:::loesung
(a) $M=1$, $\#=5$, Nachbarzellen $-V_x$ und $-V_y$, Phasen $\mathrm{e}^{\pm\mathrm{j} k_xa_x}$ und $\mathrm{e}^{\pm\mathrm{j} k_ya_y}$, also $E=E_\mathrm s-2V_x\cos(k_xa_x)-2V_y\cos(k_ya_y)$. Längs $x$ sind die Atome näher, die Orbitale überlappen stärker. (b) $\pi/a_x=10{,}47\,\mathrm{nm^{-1}}$, $\pi/a_y=6{,}28\,\mathrm{nm^{-1}}$. $E(\Gamma)=-6$ eV, $E(X)=-2{,}8$ eV, $E(Y)=-5{,}2$ eV, Ecke $-2$ eV. (c) $m_x=\hbar^2/(2V_xa_x^2)=0{,}529\,m_0$, $m_y=0{,}762\,m_0$. Die Linien sind Ellipsen, die lange Achse liegt längs $k_y$, Verhältnis $\sqrt{m_y/m_x}=1{,}20$.
:::
:::
