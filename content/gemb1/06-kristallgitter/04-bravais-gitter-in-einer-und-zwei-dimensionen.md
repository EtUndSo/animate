---
title: Stufe 2: Bravais-Gitter in einer und zwei Dimensionen
pfad: Elektrotechnik / 4. Semester / Elektronische Materialien und Bauelemente 1 / Kristallgitter
order: 4160400
summary: Nicht jedes regelmäßige Punktmuster lässt sich durch (1.1) erzeugen.
tags: Translationssymmetrie, Gitterkonstante, Polyacetylen, Kohlenstoff-Nanoröhre, Graphen
lang: de
---

<span class="anker" id="stufe-2"></span>

:::zweck
Nicht jedes regelmäßige Punktmuster lässt sich durch [(1.1)](punktgitter-und-basis.html#gl-1-1) erzeugen. Diese Stufe sagt, welche es sind, und zählt sie.
:::

**Die Idee.** Stelle dich auf einen Punkt eines Musters und schau dich um. Dann geh zu einem anderen Punkt, ohne dich zu drehen. Sieht alles genau gleich aus, gehören beide Punkte zum selben Gitter. In der Ebene ist ein Gitter durch drei Zahlen festgelegt: zwei Längen $a$, $b$ und den Winkel $\gamma$ dazwischen. Für fast alle Werte hat es außer den Translationen nur eine Symmetrie, die Drehung um 180°. Besondere Werte bringen weitere Symmetrien, und nur vier solche Sonderfälle gibt es. Mit dem allgemeinen Fall sind das fünf Gitter.

:::definition Definition 2.1 (Bravais-Gitter)
<span class="anker" id="satz-2-1"></span>

Ein Bravais-Gitter ist ein periodisches Gitter mit __Translationssymmetrie__: Jede Translation lässt sich als ganzzahlige Linearkombination primitiver Gittervektoren schreiben, und jede solche Translation bildet das Gitter auf sich ab. Gleichbedeutend: Jeder Gitterpunkt hat dieselbe Umgebung in denselben Richtungen.
:::

**Eine Dimension.** Hier gibt es genau ein Bravais-Gitter: die Kette gleich weit entfernter Punkte $x_\ell=\ell\,a$ mit ganzem $\ell$, wie in [Teil 2](/wissen/elektrotechnik/4-semester/elektronische-materialien-und-bauelemente-1/das-teilchen-in-der-box/das-teilchen-in-der-box.html). Die __Gitterkonstante__ $a$ ist der Abstand der Punkte, der Gittervektor ist diese eine Zahl. Alle Vielfalt steckt in der Basis. In __Polyacetylen__ bilden Kohlenstoffatome eine Zickzackkette mit je einem Wasserstoffatom. Das Muster wiederholt sich nach zwei CH-Gruppen, die Basis hat vier Atome. Eine __Kohlenstoff-Nanoröhre__, ein Röhrchen aus Kohlenstoff-Sechsecken, ist längs der Achse periodisch, ihre Basis enthält Dutzende Atome.

**Zwei Dimensionen.** Es gibt genau fünf Bravais-Gitter (Abb. [2](#abb-2)):

| Gitter | Vektoren | Winkel | Symmetrie neben der 180°-Drehung |
|---|---|---|---|
| schiefwinklig | $a\ne b$ | beliebig | keine |
| rechteckig | $a\ne b$ | $\gamma=90°$ | zwei Spiegelachsen |
| zentriert rechteckig | $a=b$ | beliebig | zwei Spiegelachsen |
| quadratisch | $a=b$ | $\gamma=90°$ | Drehung um 90° |
| hexagonal | $a=b$ | $\gamma=60°$ | Drehung um 60° |

⁠**So liest man das:** Das zentriert rechteckige Gitter ist ein Rechteck mit einem weiteren Punkt in der Mitte. Seine primitiven Vektoren führen von einer Ecke zu den Mitten, sind also gleich lang und spannen eine Raute auf. Rechteck und Raute sind verschiedene Sonderfälle, deshalb sind es zwei Gitter. In jedem Fall ist $\Omega=a\,b\sin\gamma$ aus [(1.2)](punktgitter-und-basis.html#gl-1-2), beim quadratischen Gitter also $a^2$, beim hexagonalen $\frac{\sqrt3}2a^2$.

:::abbildung gemb1/k6bravais 2
Die fünf Bravais-Gitter der Ebene mit je einer primitiven Zelle (blau) und ihren Vektoren (rot). Die Wabe unten rechts ist keines: Volle und offene Punkte sehen ihre Nachbarn in entgegengesetzten Richtungen.
:::

::::beispiel die Wabe
__Graphen__ ist eine einzelne Lage Kohlenstoff in Wabenform mit 0,142 nm Abstand zwischen Nachbarn. Alle Atome sind gleich, ihre Umgebungen nicht: Ein Atom hat seine drei Nachbarn oben links, oben rechts und unten, das nächste Atom unten links, unten rechts und oben (Abb. [2](#abb-2)). Die Wabe ist deshalb ein hexagonales Gitter mit zweiatomiger Basis: $\boldsymbol d_1=0$, $\boldsymbol d_2=\frac13(\boldsymbol a_1+\boldsymbol a_2)$. Die Gitterkonstante ist $a=\sqrt3\cdot0{,}142\,\mathrm{nm}=0{,}246$ nm, die Zelle hat $\Omega=0{,}0524\,\mathrm{nm^2}$, also kommen 38 Atome auf 1 nm$^2$.
::::

⁠**Grenzfall:** Mit nur einem Atom je Zelle wäre die Dichte halb so groß, das Muster aber ein echtes hexagonales Bravais-Gitter.

:::frage Setzt man in jede Quadratmitte eines quadratischen Gitters einen Punkt: Entsteht ein sechstes Gitter?
Nein. Die Vektoren $\frac a2(1,1)$ und $\frac a2(-1,1)$ erreichen alle Punkte, sind gleich lang und stehen senkrecht. Das ist wieder ein quadratisches Gitter, um 45° gedreht, mit $a'=a/\sqrt2$. Beim Rechteck stehen die Vektoren zu den Mitten nicht senkrecht, dort entsteht wirklich ein neues Gitter.
:::

:::aufgabe Aufgabe 2 ★★ Zwei Atomsorten im Quadrat
<span class="anker" id="aufg-2"></span>

Atome A und B sitzen abwechselnd wie die Felder eines Schachbretts auf einem quadratischen Raster mit dem Abstand $c=0{,}282$ nm.

<ol class="al">

<li>

Warum ist $c$ nicht die Gitterkonstante? Bestimme Gitter, Gitterkonstante und Basis.

</li>

<li>

Gib $\Omega$ an und zähle, wie viele Atome jeder Sorte in einer Zelle liegen.

</li>

</ol>

:::loesung
(a) Die Translation um $c$ führt A auf B, sie bildet das Muster nicht auf sich ab. Gleiche Plätze liegen längs der Diagonalen des Rasters. Das Gitter ist quadratisch, um 45° gedreht, mit $a=\sqrt2\,c=0{,}399$ nm. Die Basis ist A bei $\boldsymbol d_1=0$ und B bei $\boldsymbol d_2=(c,0)$. (b) $\Omega=a^2=2c^2=0{,}159\,\mathrm{nm^2}$. Die Ecken zählen $4\cdot\frac14=1$ A, in der Mitte liegt ein B.
:::
:::
