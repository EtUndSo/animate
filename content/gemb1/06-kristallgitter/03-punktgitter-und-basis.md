---
title: Stufe 1: Punktgitter und Basis
pfad: Elektrotechnik / 4. Semester / GEMB1 – Grundlagen elektronischer Materialien und Bauelemente 1 / Kristallgitter
adresse: elektrotechnik/4-semester/elektronische-materialien-und-bauelemente-1/kristallgitter
knoten: Kapitel 6: Kristallgitter
order: 4160300
summary: Ein Kristall enthält zu viele Atome, um sie einzeln zu nennen.
tags: Translation, Kristallstruktur, primitive Gittervektoren, Gittervektor, primitive Einheitszelle
lang: de
---

<span class="anker" id="stufe-1"></span>

:::zweck
Ein Kristall enthält zu viele Atome, um sie einzeln zu nennen. Diese Stufe trennt das, was sich wiederholt, vom Muster der Wiederholung.
:::

**Die Idee.** Eine Ziegelmauer, eine Bienenwabe und ein Fliesenmuster haben eines gemeinsam: Schiebt man sie um einen passenden Pfeil, liegen sie wieder deckungsgleich auf sich selbst. Diese Verschiebung heißt __Translation__. Markiert man in jedem Ziegel denselben Punkt, etwa seine linke untere Ecke, bleibt ein Muster aus Punkten übrig. Es enthält alles über die Wiederholung und nichts über den Ziegel. Der Ziegel ist die zweite Angabe. Genauso zerlegt man einen Kristall (Abb. [1](#abb-1)). Elektronenmikroskope mit hoher Auflösung zeigen dieses Muster direkt: Helle Punkte im Abstand von Bruchteilen eines Nanometers wiederholen sich über das ganze Bild.

:::abbildung gemb1/k6gitter 1
Links ein Punktgitter, grau eine Zelle, rot und grün zwei Verschiebungen. Mitte eine Basis aus zwei Atomen mit dem Abstandsvektor $\boldsymbol d$. Rechts der Kristall: An jedem Gitterpunkt hängt dieselbe Basis.
:::

:::definition Definition 1.1 (Kristall)
<span class="anker" id="satz-1-1"></span>

Ein Kristall ist eine räumlich periodische Anordnung von Basiseinheiten in einem festen Verband. Das Punktgitter ist eine Menge von Punkten, die allein die Periodizität trägt. Die Basis ist der Inhalt, der an jedem Gitterpunkt hängt: ein Atom, eine Atomgruppe, ein Molekül oder ein Ionenpaar. Zusammen ergeben sie die __Kristallstruktur__: Kristall = Punktgitter + Basis.
:::

:::definition Definition 1.2 (Primitive Gittervektoren)
<span class="anker" id="satz-1-2"></span>

Die Vektoren $\boldsymbol a_1,\boldsymbol a_2,\boldsymbol a_3$ heißen __primitive Gittervektoren__, wenn man jeden Gitterpunkt von einem festen Gitterpunkt aus mit

<span class="anker" id="gl-1-1"></span>
$$\boldsymbol R=\ell_1\boldsymbol a_1+\ell_2\boldsymbol a_2+\ell_3\boldsymbol a_3,\qquad \ell_1,\ell_2,\ell_3\ \text{ganz}, \tag{1.1}$$

erreicht und jedes solche $\boldsymbol R$ auf einem Gitterpunkt endet. In der Ebene entfällt $\boldsymbol a_3$. $\boldsymbol R$ heißt __Gittervektor__.
:::

⁠**So liest man das:** Die $\ell_i$ sind ganze Zahlen, positiv, negativ oder null, wie der Gitterindex $\ell$ in [Kapitel 2](/wissen/elektrotechnik/4-semester/elektronische-materialien-und-bauelemente-1/das-teilchen-in-der-box/das-teilchen-in-der-box.html). $\boldsymbol R$ ist ein Ortsvektor in nm, typische Längen beginnen bei 0,2 bis 0,6 nm. Die $\boldsymbol a_i$ müssen linear unabhängig sein, sie dürfen also nicht alle in einer Ebene liegen. Senkrecht zueinander oder gleich lang müssen sie nicht sein. Das Atom $j$ der Basis sitzt bei $\boldsymbol R+\boldsymbol d_j$, wobei $\boldsymbol d_j$ sein fester Abstandsvektor vom Gitterpunkt ist. **Gültigkeit:** [(1.1)](#gl-1-1) meint einen unendlich großen, fehlerfreien Kristall. Der Rand spielt kaum eine Rolle: Ein Würfel von 1 cm hat bei 0,5 nm Zellgröße $2\cdot10^{7}$ Zellen je Kante, und nur der Anteil $3\cdot10^{-7}$ davon liegt an den sechs Außenflächen.

:::definition Definition 1.3 (Einheitszelle)
<span class="anker" id="satz-1-3"></span>

Die Einheitszelle ist ein Gebiet, das den Raum allein durch Verschieben um Gittervektoren lückenlos und ohne Überlappung füllt. Die __primitive Einheitszelle__ ist die kleinste solche Zelle. Sie enthält genau einen Gitterpunkt. Das Parallelogramm aus $\boldsymbol a_1,\boldsymbol a_2$ und das Parallelepiped aus $\boldsymbol a_1,\boldsymbol a_2,\boldsymbol a_3$ sind primitive Einheitszellen mit dem Inhalt

<span class="anker" id="gl-1-2"></span>
$$\Omega=|\boldsymbol a_1\times\boldsymbol a_2|\quad\text{(Ebene)},\qquad \Omega=|\boldsymbol a_1\cdot(\boldsymbol a_2\times\boldsymbol a_3)|\quad\text{(Raum)}. \tag{1.2}$$
:::

⁠**So liest man das:** $\Omega$ ist die Fläche oder das Volumen je Gitterpunkt, typisch 0,01 bis 0,1 nm$^3$. „Kleinste“ meint den Inhalt der Kachel, nicht das Muster darin: Die Basis kann beliebig kompliziert sein. Die Form der primitiven Zelle ist frei wählbar, ihr Inhalt nicht.

:::herleitung Warum die Zelle genau einen Punkt enthält
Die Punkte sitzen auf den vier Ecken, und jede Ecke gehört zu vier Zellen: $4\cdot\frac14=1$. Die Punktdichte gehört zum Gitter, also ist $\Omega$ für alle primitiven Zellen gleich.
:::

::::beispiel die Mauer
Ein Ziegel ist 24 cm lang und 6 cm hoch, die Fuge 1 cm breit, jede Reihe ist um einen halben Ziegel versetzt. Dann sind $\boldsymbol a_1=(25;\,0)$ cm und $\boldsymbol a_2=(12{,}5;\,7)$ cm primitive Gittervektoren. Mit [(1.2)](#gl-1-2) ist $\Omega=175\,\mathrm{cm^2}$, also kommen 57 Ziegel auf 1 m$^2$: Der Zellinhalt liefert die Dichte. Die Vektoren $(12{,}5;\,7)$ cm und $(-12{,}5;\,7)$ cm erzeugen dasselbe Gitter mit derselben Fläche.
::::

⁠**Grenzfall:** Ohne Versatz wird $\boldsymbol a_2=(0;\,7)$ cm, die Zelle wird ein Rechteck, und $\Omega$ bleibt 175 cm$^2$.

:::frage Sitzt an jedem Gitterpunkt ein Atom?
Nicht unbedingt. Der Gitterpunkt ist ein Bezugspunkt, den man im Muster frei wählt. Verschiebt man alle Punkte um denselben Vektor, beschreibt das Gitter denselben Kristall.
:::

:::aufgabe Aufgabe 1 ★ Gitterpunkte prüfen
<span class="anker" id="aufg-1"></span>

Ein Gitter hat die primitiven Gittervektoren $\boldsymbol a_1=(3,0)$ nm und $\boldsymbol a_2=(1,2)$ nm.

<ol class="al">

<li>

Sind $(7,2)$ nm, $(4,4)$ nm und $(-2,2)$ nm Gitterpunkte?

</li>

<li>

Berechne $\Omega$. Sind $\boldsymbol a_1+\boldsymbol a_2$ und $\boldsymbol a_2$ ebenfalls primitiv? Und $2\boldsymbol a_1$ und $\boldsymbol a_2$? Welche Punkte fehlen im zweiten Fall?

</li>

</ol>

:::loesung
(a) Aus $(x,y)=\ell_1(3,0)+\ell_2(1,2)$ folgt $\ell_2=y/2$ und $\ell_1=(x-\ell_2)/3$. $(7,2)$: $\ell_2=1$, $\ell_1=2$, Gitterpunkt. $(4,4)$: $\ell_2=2$, $\ell_1=\frac23$, kein Gitterpunkt. $(-2,2)$: $\ell_2=1$, $\ell_1=-1$, Gitterpunkt. (b) $\Omega=|3\cdot2-0\cdot1|=6\,\mathrm{nm^2}$. Mit $\boldsymbol a_1+\boldsymbol a_2$ und $\boldsymbol a_2$ bleibt $\Omega=6\,\mathrm{nm^2}$, der Satz ist primitiv, denn $\boldsymbol a_1=(\boldsymbol a_1+\boldsymbol a_2)-\boldsymbol a_2$ ist erreichbar. Mit $2\boldsymbol a_1$ und $\boldsymbol a_2$ ist $\Omega=12\,\mathrm{nm^2}$, die Zelle enthält zwei Punkte. Es fehlt jeder Punkt mit ungeradem $\ell_1$, etwa $\boldsymbol a_1$ selbst.
:::
:::
