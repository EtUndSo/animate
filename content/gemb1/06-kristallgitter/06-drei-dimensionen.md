---
title: Stufe 4: Drei Dimensionen
pfad: Elektrotechnik / 4. Semester / Elektronische Materialien und Bauelemente 1 / Kristallgitter
order: 4160600
summary: Im Raum kommen zu den drei Längen drei Winkel hinzu.
tags: Kristallachsen, Elementarzelle, Gitterwinkel, primitiv, basiszentriert, innenzentriert, flächenzentriert, einfach kubische
lang: de
---

<span class="anker" id="stufe-4"></span>

:::zweck
Im Raum kommen zu den drei Längen drei Winkel hinzu. Diese Stufe ordnet die Möglichkeiten und stellt die drei kubischen Gitter vor, die für Metalle und Silizium zählen.
:::

**Die Idee.** Das Zählen aus Stufe [2](bravais-gitter-in-einer-und-zwei-dimensionen.html#stufe-2) geht weiter. Sechs Zahlen legen eine Zelle fest. Sonderwerte, etwa gleiche Längen oder rechte Winkel, bringen zusätzliche Symmetrie und führen auf sieben Systeme. Innerhalb eines Systems kann man Zusatzpunkte in die Zelle setzen, ohne die Symmetrie zu ändern. So entstehen genau 14 Bravais-Gitter.

:::definition Definition 4.1 (Elementarzelle)
<span class="anker" id="satz-4-1"></span>

Die drei __Kristallachsen__ sind linear unabhängige Richtungen, längs derer sich das Gitter wiederholt. Ein kartesisches System müssen sie nicht bilden. Die __Elementarzelle__ ist das Parallelepiped mit den Kanten längs dieser Achsen. Seine Kantenlängen $a$, $b$, $c$ sind die Gitterkonstanten, die Winkel $\alpha$ (zwischen $b$ und $c$), $\beta$ (zwischen $a$ und $c$) und $\gamma$ (zwischen $a$ und $b$) die __Gitterwinkel__. Man wählt die Zelle mit der größten Symmetrie und dabei möglichst kleinen Gitterkonstanten. Sie kann deshalb mehr als einen Gitterpunkt enthalten.
:::

| System | Längen | Winkel | Zelltypen | Gitter |
|---|---|---|---|---|
| triklin | $a\ne b\ne c$ | $\alpha\ne\beta\ne\gamma$ | P | 1 |
| monoklin | $a\ne b\ne c$ | $\alpha=\gamma=90°$, $\beta\ne90°$ | P, B | 2 |
| orthorhombisch | $a\ne b\ne c$ | $\alpha=\beta=\gamma=90°$ | P, B, I, F | 4 |
| hexagonal | $a=b\ne c$ | $\alpha=\beta=90°$, $\gamma=120°$ | P | 1 |
| rhomboedrisch | $a=b=c$ | $\alpha=\beta=\gamma\ne90°$ | P | 1 |
| tetragonal | $a=b\ne c$ | $\alpha=\beta=\gamma=90°$ | P, I | 2 |
| kubisch | $a=b=c$ | $\alpha=\beta=\gamma=90°$ | P, I, F | 3 |

⁠**So liest man das:** Die Zeilen sind nach wachsender Symmetrie geordnet. Die Zelltypen sind __primitiv__ (P, Punkte nur auf den Ecken), __basiszentriert__ (B, dazu die Mitten zweier gegenüberliegender Flächen), __innenzentriert__ oder raumzentriert (I, dazu die Zellmitte) und __flächenzentriert__ (F, dazu die Mitten aller sechs Flächen). Statt $7\cdot4=28$ Fällen gibt es nur 14, weil manche Zentrierung ein schon vorhandenes Gitter ergibt, wie beim Quadrat mit Mittelpunkt, und andere die Symmetrie des Systems zerstört.

:::abbildung gemb1/k6kubisch 4
Oben die Würfelzellen der drei kubischen Gitter mit primitiven Vektoren (rot). Orange: Zusatzpunkte. Unten die Wigner-Seitz-Zellen im selben Maßstab: Würfel, abgestumpftes Oktaeder und Rhombendodekaeder. Ihr Inhalt sinkt von $a^3$ über $a^3/2$ auf $a^3/4$.
:::

:::satz Satz 4.2 (Die drei kubischen Gitter)
<span class="anker" id="satz-4-2"></span>

Alle drei haben den Würfel mit der Kante $a$ als Elementarzelle. Das __einfach kubische__ Gitter (SC) hat Punkte nur auf den Ecken:

<span class="anker" id="gl-4-1"></span>
$$\boldsymbol a_1=(a,0,0),\quad \boldsymbol a_2=(0,a,0),\quad \boldsymbol a_3=(0,0,a). \tag{4.1}$$

Das __kubisch raumzentrierte__ Gitter (BCC oder krz) hat zusätzlich einen Punkt in der Würfelmitte:

<span class="anker" id="gl-4-2"></span>
$$\boldsymbol a_1=\tfrac a2(1,1,-1),\quad \boldsymbol a_2=\tfrac a2(-1,1,1),\quad \boldsymbol a_3=\tfrac a2(1,-1,1). \tag{4.2}$$

Das __kubisch flächenzentrierte__ Gitter (FCC oder kfz) hat zusätzlich je einen Punkt in den sechs Flächenmitten:

<span class="anker" id="gl-4-3"></span>
$$\boldsymbol a_1=\tfrac a2(1,1,0),\quad \boldsymbol a_2=\tfrac a2(1,0,1),\quad \boldsymbol a_3=\tfrac a2(0,1,1). \tag{4.3}$$
:::

⁠**So liest man das:** SC kommt fast nur bei Polonium vor, BCC etwa bei Na, $\alpha$-Fe, W, Cr, V und K, FCC bei Al, Cu, Au und Ag. Bei BCC zeigen die Vektoren längs halber Raumdiagonalen zu Nachbarn, bei FCC längs halber Flächendiagonalen. Die Wigner-Seitz-Zelle ist bei SC der Würfel $a\times a\times a$ um das Atom, bei BCC ein __abgestumpftes Oktaeder__ mit 14 Flächen und bei FCC ein __Rhombendodekaeder__ mit 12 Rauten, eine je Nachbar (Abb. [4](#abb-4)). Die 8 Sechsecke des Oktaeders stammen von den 8 nächsten Nachbarn, die 6 Quadrate von den 6 Punkten im Abstand $a$.

:::herleitung Warum die Würfelkanten bei BCC und FCC nicht reichen
Die Vektoren [(4.1)](#gl-4-1) erreichen bei BCC nur die Ecken. Die Zellmitte $\frac a2(1,1,1)$ ist keine ganzzahlige Kombination davon, also fehlen Gitterpunkte. Mit [(4.2)](#gl-4-2) erreicht man sie, denn vom Eckpunkt $(0,0,0)$ aus ist $\boldsymbol a_1+\boldsymbol a_2+\boldsymbol a_3=\frac a2(1,1,1)$. Die Würfelkanten stecken ebenfalls darin: $\boldsymbol a_1+\boldsymbol a_3=(a,0,0)$. Das Spatprodukt [(1.2)](punktgitter-und-basis.html#gl-1-2) ergibt für SC, BCC und FCC die Inhalte $a^3$, $a^3/2$ und $a^3/4$. Also enthält der Würfel 1, 2 und 4 Gitterpunkte.
:::

⁠**Grenzfall:** Streckt man BCC längs einer Würfelkante, gelten die Vektoren [(4.2)](#gl-4-2) mit gestreckter dritter Komponente weiter, und das Gitter wird tetragonal raumzentriert.

:::frage Warum gibt es kein kubisch basiszentriertes Gitter?
Zusatzpunkte nur auf zwei gegenüberliegenden Flächen zeichnen eine Achse aus. Dann ist die 120°-Drehung um die Raumdiagonale, die jedes kubische Gitter hat, keine Symmetrie mehr. Das Gitter ist tetragonal, nicht kubisch.
:::

:::zusatz Symmetrie und Richtungsabhängigkeit
Neben der Translation kann eine Zelle weitere __Symmetrieoperationen__ erlauben: Drehung um eine Drehachse, Spiegelung an einer Spiegelebene, __Inversion__ an einem Inversionszentrum (jeder Punkt wandert durch das Zentrum auf die Gegenseite) und __Inversionsdrehung__ um eine Inversionsdrehachse (erst Drehung, dann Inversion). Es gibt 1-, 2-, 3-, 4- und 6-zählige Drehachsen, also 360°, 180°, 120°, 90° und 60°. Fünfzählig geht nicht, denn Fünfecke füllen die Ebene nicht. Eine einfache tetragonale Zelle hat eine vierzählige Achse längs $c$, die auch Inversionsdrehachse ist, eine Spiegelebene senkrecht dazu und ihre Mitte als Inversionszentrum. Ordnet man alle Zellen nach ihren Kombinationen von Operationen, entstehen 32 __Kristallklassen__.

Symmetrie wirkt auf Messwerte. Im orthorhombischen Kristall sind elektrische Leitfähigkeit und Wärmeausdehnung im Allgemeinen in allen drei Richtungen verschieden, im tetragonalen in zwei Richtungen gleich, im kubischen in allen dreien. Richtungsabhängige Stoffe heißen __anisotrop__. Ein Polykristall mit zufällig gedrehten Kristalliten ist im Mittel __isotrop__.
:::

:::aufgabe Aufgabe 4 ★★ Das FCC-Gitter aufbauen
<span class="anker" id="aufg-4"></span>

Gegeben sind die Vektoren [(4.3)](#gl-4-3).

<ol class="al">

<li>

Erreiche die Würfelecken $(a,0,0)$ und $(a,a,a)$ sowie die Flächenmitte $\frac a2(1,1,2)$. Welche $\ell_i$ gehören dazu?

</li>

<li>

Berechne das Spatprodukt und die Länge von $\boldsymbol a_1$.

</li>

<li>

Ist auch $(a,0,0)$, $\frac a2(1,1,0)$, $\frac a2(1,0,1)$ ein primitiver Satz? Prüfe mit dem Spatprodukt und zeige, dass $\boldsymbol a_3$ erreichbar ist.

</li>

<li>

Wie viele Gitterpunkte liegen in der Wigner-Seitz-Zelle von SC, BCC und FCC?

</li>

</ol>

:::loesung
(a) $\boldsymbol a_1+\boldsymbol a_2-\boldsymbol a_3=(a,0,0)$ mit $\ell=(1,1,-1)$, $\ \boldsymbol a_1+\boldsymbol a_2+\boldsymbol a_3=(a,a,a)$ mit $\ell=(1,1,1)$, $\ \boldsymbol a_2+\boldsymbol a_3=\frac a2(1,1,2)$ mit $\ell=(0,1,1)$. (b) $\boldsymbol a_2\times\boldsymbol a_3=\frac{a^2}4(-1,-1,1)$, also $|\boldsymbol a_1\cdot(\boldsymbol a_2\times\boldsymbol a_3)|=a^3/4$. $|\boldsymbol a_1|=a/\sqrt2=0{,}707\,a$. (c) Das Spatprodukt ist wieder $a^3/4$. Der Satz erzeugt nur Gitterpunkte, hat aber den kleinsten Inhalt, ist also primitiv. Probe: $\boldsymbol a_3=\boldsymbol a_1+\boldsymbol a_2-(a,0,0)$. (d) Je einer, denn die Wigner-Seitz-Zelle ist primitiv. Ihr Inhalt ist $a^3$, $a^3/2$ und $a^3/4$.
:::
:::
