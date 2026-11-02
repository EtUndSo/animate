---
title: Stufe 6: Die Brillouin-Zone
pfad: Elektrotechnik / 4. Semester / Elektronische Materialien und Bauelemente 1 / Kristallwachstum und reziprokes Gitter
order: 4170800
summary: Jede Welle bleibt dieselbe, wenn man boldsymbol k um ein boldsymbol G verschiebt.
tags: 
lang: de
---

<span class="anker" id="stufe-6"></span>

:::zweck
Jede Welle bleibt dieselbe, wenn man $\boldsymbol k$ um ein $\boldsymbol G$ verschiebt. Im $k$-Raum gibt es also unendlich viele Kopien. Diese Stufe wählt einen Bereich aus, der jede Welle genau einmal enthält.
:::

**Die Idee.** Das reziproke Gitter ist selbst ein Bravais-Gitter. Also lässt sich auf ihm dieselbe Frage stellen wie in [Teil 6](/wissen/elektrotechnik/4-semester/elektronische-materialien-und-bauelemente-1/kristallgitter/kristallgitter.html): Welches Gebiet gehört zu einem Punkt? Jedes $\boldsymbol k$ hat einen nächsten reziproken Gitterpunkt $\boldsymbol G$. Zieht man $\boldsymbol G$ ab, landet es im Hoheitsgebiet des Ursprungs. Dort liegt jede Welle genau einmal, und zwar mit dem kleinstmöglichen $|\boldsymbol k|$.

:::definition Definition 6.1 (Erste Brillouin-Zone)
<span class="anker" id="satz-6-1"></span>

Die erste Brillouin-Zone ist die Wigner-Seitz-Zelle des reziproken Gitters um $\boldsymbol G=0$: alle $\boldsymbol k$, die dem Ursprung näher sind als jedem anderen reziproken Gitterpunkt. Ihr Rand besteht aus den Mittelebenen,

<span class="anker" id="gl-6-1"></span>
$$\boldsymbol k\cdot\frac{\boldsymbol G}{|\boldsymbol G|}=\frac{|\boldsymbol G|}2, \tag{6.1}$$

und ihr Inhalt ist $(2\pi)^3/\Omega$.
:::

⁠**So liest man das:** [(6.1)](#gl-6-1) sagt, dass $\boldsymbol k$ und $\boldsymbol k-\boldsymbol G$ gleich lang sind. Die Konstruktion ist die aus [Teil 6](/wissen/elektrotechnik/4-semester/elektronische-materialien-und-bauelemente-1/kristallgitter/kristallgitter.html): Verbindungslinien vom Ursprung zu den Nachbarn ziehen, jede mittig senkrecht schneiden, das kleinste eingeschlossene Gebiet nehmen. Auf der Kette liegen die Nachbarn bei $\pm2\pi/a$, die Schnitte bei $\pm\pi/a$. Das ist der Bereich aus [Teil 2](/wissen/elektrotechnik/4-semester/elektronische-materialien-und-bauelemente-1/das-teilchen-in-der-box/das-teilchen-in-der-box.html).

:::abbildung gemb1/k7zonen 6
Oben: Konstruktion in der Ebene für die reziproken Gitter aus Abb. [5](reziproke-gittervektoren-in-der-ebene-und-im-raum.html#abb-5). Verbindungslinien grün, Mittelsenkrechte rot, Zone grau. Unten: erste Brillouin-Zonen der kubischen Kristalle, nicht maßstäblich zueinander.
:::

**Beispiele** (Abb. [6](#abb-6)). Das Rechteckgitter hat ein Rechteck als Zone, das zentriert rechteckige ein Sechseck. Im Raum folgt die Form aus dem reziproken Gitter:

| Kristallgitter | reziprokes Gitter | Form der Zone | Inhalt |
|---|---|---|---|
| SC | SC | Würfel, $\vert k_x\vert ,\vert k_y\vert ,\vert k_z\vert \le\pi/a$ | $(2\pi/a)^3$ |
| BCC | FCC | Rhombendodekaeder | $2\,(2\pi/a)^3$ |
| FCC | BCC | abgestumpftes Oktaeder | $4\,(2\pi/a)^3$ |

Die Zone eines FCC-Kristalls hat die Form der Wigner-Seitz-Zelle von BCC und umgekehrt. Der Würfel des SC-Kristalls hat die Kantenlänge $2\pi/a$. **Beispiel Silizium:** FCC, also abgestumpftes Oktaeder. Die Quadratflächen liegen $2\pi/a=11{,}57\,\mathrm{nm^{-1}}$ von der Mitte entfernt, die Sechseckflächen $\sqrt3\,\pi/a=10{,}02\,\mathrm{nm^{-1}}$. Der Inhalt ist $6190\,\mathrm{nm^{-3}}$.

**Höhere Zonen.** Jenseits der ersten Zone folgen weitere: Gebiete, die man vom Ursprung aus erreicht, indem man eine, zwei oder mehr Mittelebenen überquert. Im SC-Gitter beginnen sie bei $|k_x|>\pi/a$. Sie sind kompliziert geformte Vielecke mit demselben Inhalt wie die erste Zone, und jede lässt sich mit passenden $\boldsymbol G$ in die erste falten. Auf der Kette ist die zweite Zone der zweite Parabelabschnitt aus Abb. [4](das-reziproke-gitter-in-einer-dimension.html#abb-4).

:::satz Satz 6.2 (Zustände in der Zone)
<span class="anker" id="satz-6-2"></span>

Ein Kristall aus $N$ primitiven Zellen hat in jeder Brillouin-Zone genau $N$ Werte von $\boldsymbol k$. Weil jeder Zustand mit zwei Elektronen besetzt werden kann, fasst jede Zone $2N$ Elektronen, also zwei je primitive Zelle.
:::

:::herleitung Zählen mit periodischen Rändern
Für einen Würfel der Kante $L$ erlauben periodische Ränder ([Teil 2](/wissen/elektrotechnik/4-semester/elektronische-materialien-und-bauelemente-1/das-teilchen-in-der-box/das-teilchen-in-der-box.html)) die Werte $k_x=n_x2\pi/L$, entsprechend $k_y$ und $k_z$. Jeder Wert belegt im $k$-Raum das Volumen $(2\pi)^3/L^3$. Die Zone hat den Inhalt $(2\pi)^3/\Omega$. Der Quotient ist $L^3/\Omega=N$. Die Form der Zone geht nicht ein, also gilt das Ergebnis für jede Gitterstruktur.
:::

**Beispiel.** Eine Kette von 1 µm mit $a=0{,}2$ nm hat 5000 Punkte. Die $k$-Werte liegen $0{,}00628\,\mathrm{nm^{-1}}$ auseinander, die Zone ist $31{,}4\,\mathrm{nm^{-1}}$ breit. Das ergibt 5000 Werte. **Kontrolle:** [Teil 2](/wissen/elektrotechnik/4-semester/elektronische-materialien-und-bauelemente-1/das-teilchen-in-der-box/das-teilchen-in-der-box.html) fand für $N$ Punkte $N$ Energien. **Grenzfall:** Für $L\to\infty$ liegen die Werte beliebig dicht, die Zone bleibt gleich groß. $k$ wird stetig.

:::frage Silizium hat zwei Atome je Zelle. Zählt die Zone Atome oder Zellen?
Zellen. $N$ ist die Zahl der Gitterpunkte, die Basis kommt in [(5.3)](reziproke-gittervektoren-in-der-ebene-und-im-raum.html#gl-5-3) nicht vor. Jedes Siliziumatom hat aber 4 Außenelektronen, je Zelle sind das 8. Sie brauchen also vier Zonen oder, in eine Zone gefaltet, vier Abschnitte.
:::

:::aufgabe Aufgabe 7 ★★ Die Zone eines BCC-Kristalls
<span class="anker" id="aufg-7"></span>

Wolfram ist BCC mit $a=0{,}3165$ nm.

<ol class="al">

<li>

Berechne mit den Vektoren aus der Tabelle $\boldsymbol a_2\times\boldsymbol a_3$, das Spatprodukt und $\boldsymbol b_1,\boldsymbol b_2,\boldsymbol b_3$.

</li>

<li>

Prüfe [(5.2)](reziproke-gittervektoren-in-der-ebene-und-im-raum.html#gl-5-2) an zwei Beispielen. Wie viele nächste Nachbarn hat der Ursprung im reziproken Gitter, und in welchem Abstand?

</li>

<li>

Wie weit liegen die Flächen der Zone von der Mitte entfernt? Wie groß ist ihr Inhalt?

</li>

</ol>

:::loesung
(a) $\boldsymbol a_2\times\boldsymbol a_3=\frac{a^2}4(2,2,0)=\frac{a^2}2(1,1,0)$, Spatprodukt $\frac{a^3}2=0{,}0159\,\mathrm{nm^3}$. Damit $\boldsymbol b_1=\frac{2\pi}a(1,1,0)$, $\boldsymbol b_2=\frac{2\pi}a(0,1,1)$, $\boldsymbol b_3=\frac{2\pi}a(1,0,1)$ mit $2\pi/a=19{,}85\,\mathrm{nm^{-1}}$. (b) $\boldsymbol a_1\cdot\boldsymbol b_1=\frac a2\cdot\frac{2\pi}a\cdot2=2\pi$, $\boldsymbol a_1\cdot\boldsymbol b_2=\frac a2\cdot\frac{2\pi}a(1-1)=0$. Das reziproke Gitter ist FCC mit Würfelkante $39{,}70\,\mathrm{nm^{-1}}$. Der Ursprung hat 12 nächste Nachbarn im Abstand $\sqrt2\cdot2\pi/a=28{,}08\,\mathrm{nm^{-1}}$. (c) Die 12 Rautenflächen liegen $\sqrt2\,\pi/a=14{,}04\,\mathrm{nm^{-1}}$ von der Mitte entfernt, Inhalt $2\,(2\pi/a)^3=15\,650\,\mathrm{nm^{-3}}$.
:::
:::

:::aufgabe Aufgabe 8 ★★ Zustände zählen
<span class="anker" id="aufg-8"></span>

Ein Siliziumwürfel hat 1 µm Kantenlänge.

<ol class="al">

<li>

Wie viele primitive Zellen und wie viele Atome enthält er?

</li>

<li>

Wie groß ist der Abstand benachbarter $k$-Werte? Prüfe, dass Zonenvolumen durch Volumen je $k$-Wert die Zahl aus (a) ergibt.

</li>

<li>

Wie viele Plätze fasst eine Zone, wie viele Außenelektronen hat der Würfel?

</li>

</ol>

:::loesung
(a) $N=4\,(1000/0{,}5431)^3=2{,}50\cdot10^{10}$ Zellen und $4{,}99\cdot10^{10}$ Atome. (b) $2\pi/L=0{,}00628\,\mathrm{nm^{-1}}$. $4\,(2\pi/a)^3/(2\pi/L)^3=4\,(L/a)^3=2{,}50\cdot10^{10}$. (c) Eine Zone fasst $2N=4{,}99\cdot10^{10}$ Elektronen. Der Würfel hat $8N=2{,}00\cdot10^{11}$ Außenelektronen, genug für vier Zonen.
:::
:::
