---
title: Stufe 1: Paare statt einzelner Zahlen
pfad: Elektrotechnik / 1. Semester / Höhere Mathematik 1 / Komplexe Zahlen
order: 1220200
summary: In mathbb R hat x 2=-1 keine Lösung.
tags: Normalform
lang: de
---

<span class="anker" id="stufe-1"></span>

:::zweck
In $\mathbb{R}$ hat $x^2=-1$ keine Lösung. Diese Stufe baut eine größere Zahlenmenge, in der die Gleichung lösbar ist und $\mathbb{R}$ unverändert enthalten bleibt.
:::

**Die Idee.** Jede Erweiterung der Zahlen löst eine Gleichung, die vorher keine Lösung hatte: $x+1=0$ führt von $\mathbb{N}$ zu $\mathbb{Z}$, $2x=1$ von $\mathbb{Z}$ zu $\mathbb{Q}$, $x^2=2$ von $\mathbb{Q}$ zu $\mathbb{R}$. Bei $x^2=-1$ liegt der Fall anders. Die Parabel $y=x^2$ erreicht die Höhe $-1$ nie (Abb. [1](#abb-1)), denn in $\mathbb{R}$ gilt $x^2\ge0$ ([Teil 1](/wissen/elektrotechnik/1-semester/hohere-mathematik-1/mengen-logik-und-reelle-zahlen/mengen-logik-und-reelle-zahlen.html)). Es fehlt kein Punkt zwischen anderen Punkten wie bei $\sqrt2$, sondern jeder Punkt der Zahlengeraden scheidet aus. Die Lösung muss neben der Geraden liegen. Deshalb kommt eine zweite Koordinate hinzu: Man rechnet mit Paaren $(x,y)$. Die Paare $(x,0)$ sollen die reellen Zahlen bleiben, und $(0,1)$ soll zum Quadrat $(-1,0)$ ergeben.

:::abbildung hm1/k2parabel 1
Die Gerade $y=2$ schneidet die Parabel zweimal, die Lösungen $\pm\sqrt2$ liegen auf der Zahlengeraden. Die Gerade $y=-1$ schneidet sie nie: Kein reelles $x$ löst $x^2=-1$.
:::

:::definition Definition 1.1 (Komplexe Zahlen)
<span class="anker" id="satz-1-1"></span>

Die Menge der komplexen Zahlen ist $\mathbb{C}:=\{(x,y):x,y\in\mathbb{R}\}$ mit der Addition $\oplus$ und der Multiplikation $\odot$:

<span class="anker" id="gl-1-1"></span>
<span class="anker" id="gl-1-2"></span>
$$\begin{aligned} (x_1,y_1)\oplus(x_2,y_2)&:=(x_1+x_2,\;y_1+y_2),\\ (x_1,y_1)\odot(x_2,y_2)&:=(x_1x_2-y_1y_2,\;x_1y_2+x_2y_1). \end{aligned} \tag{1.1|1.2}$$

Das Nullelement ist $(0,0)$, das Einselement ist $(1,0)$, die imaginäre Einheit ist $\mathrm{i}:=(0,1)$.
:::

⁠**So liest man das:** $x$ und $y$ sind reelle Zahlen ohne Einheit, $\oplus$ und $\odot$ neue Rechenarten für Paare. **Grenzfall:** Für $y_1=y_2=0$ ergeben [(1.1)](#gl-1-1) und [(1.2)](#gl-1-2) die Paare $(x_1+x_2,0)$ und $(x_1x_2,0)$. Die Paare $(x,0)$ rechnen also genau wie die reellen Zahlen $x$. Deshalb schreibt man $x$ statt $(x,0)$, $+$ statt $\oplus$, $\cdot$ statt $\odot$, und es gilt $\mathbb{R}\subset\mathbb{C}$.

:::satz Satz 1.2 (Imaginäre Einheit und Normalform)
<span class="anker" id="satz-1-2"></span>

<ol class="rm">

<li>

Es gilt $\mathrm{i}^2=-1$.

</li>

<li>

Jede komplexe Zahl hat genau eine __Normalform__ $z=x+\mathrm{i}y$ mit $x,y\in\mathbb{R}$.

</li>

<li>

In der Normalform gilt $(x_1+\mathrm{i}y_1)+(x_2+\mathrm{i}y_2)=(x_1+x_2)+\mathrm{i}(y_1+y_2)$ und

</li>

</ol>

<span class="anker" id="gl-1-3"></span>
$$(x_1+\mathrm{i}y_1)(x_2+\mathrm{i}y_2)=(x_1x_2-y_1y_2)+\mathrm{i}(x_1y_2+x_2y_1). \tag{1.3}$$
:::

⁠**So liest man das:** Die Formel [(1.3)](#gl-1-3) muss niemand auswendig lernen: Klammern ausmultiplizieren, $\mathrm{i}^2=-1$ einsetzen, sortieren. Das Minus in $x_1x_2-y_1y_2$ ist das $\mathrm{i}^2$. In der Mathematik heißt die imaginäre Einheit $\mathrm{i}$, in der Elektrotechnik $\mathrm{j}$, weil $i$ dort der Strom ist. Dieses Kapitel schreibt aufrecht $\mathrm{i}$. **Gültigkeit:** $x$ und $y$ müssen reell sein. Sonst ist die Darstellung nicht eindeutig: $\mathrm{i}=\mathrm{i}+\mathrm{i}\cdot0=0+\mathrm{i}\cdot1$.

:::beweis Rechnen mit Paaren
(i) Nach [(1.2)](#gl-1-2) ist $\mathrm{i}\cdot\mathrm{i}=(0,1)\odot(0,1)=(0\cdot0-1\cdot1,\;0\cdot1+0\cdot1)=(-1,0)=-1$.

(ii) Für reelles $y$ ist $\mathrm{i}y=(0,1)\odot(y,0)=(0\cdot y-1\cdot0,\;0\cdot0+y\cdot1)=(0,y)$, also $x+\mathrm{i}y=(x,0)\oplus(0,y)=(x,y)$. Das Paar legt $x$ und $y$ eindeutig fest.

(iii) Nach (ii) sind die rechten Seiten genau die Paare aus [(1.1)](#gl-1-1) und [(1.2)](#gl-1-2).
:::

::::beispiel
Summe und Produkt des Rechenmodells:

$$z_1+z_2=(3+1)+\mathrm{i}(1+2)=4+3\mathrm{i},\qquad z_1z_2=(3+\mathrm{i})(1+2\mathrm{i})=3+6\mathrm{i}+\mathrm{i}+2\mathrm{i}^2=1+7\mathrm{i}.$$

Die Paarformel [(1.2)](#gl-1-2) gibt dasselbe: $(3\cdot1-1\cdot2,\;3\cdot2+1\cdot1)=(1,7)$. Die Potenzen von $\mathrm{i}$ wiederholen sich mit der Periode 4: $\mathrm{i}^1=\mathrm{i}$, $\mathrm{i}^2=-1$, $\mathrm{i}^3=-\mathrm{i}$, $\mathrm{i}^4=1$. Also zählt nur der Rest von $n$ bei Division durch 4, zum Beispiel $\mathrm{i}^{10}=\mathrm{i}^8\,\mathrm{i}^2=-1$.
::::

:::frage Gibt es $\mathrm{i}$ wirklich, oder ist das ein Rechentrick?
Auf der Zahlengeraden gibt es $\mathrm{i}$ nicht, so weit stimmt der Zweifel. Aber $\mathrm{i}$ ist das Paar $(0,1)$, und [(1.2)](#gl-1-2) ist eine eindeutige Vorschrift für Paare. „Imaginär“ ist nur ein historischer Name.
:::

:::aufgabe Aufgabe 1 ★ Rechnen in der Normalform
<span class="anker" id="aufg-1"></span>

Bringe auf die Form $x+\mathrm{i}y$: (a) $(4-\mathrm{i})(2+3\mathrm{i})$, (b) $(1+\mathrm{i})^2$ und damit $(1+\mathrm{i})^4$, (c) $\mathrm{i}^{27}+\mathrm{i}^{42}$.

:::loesung
(a) $8+12\mathrm{i}-2\mathrm{i}-3\mathrm{i}^2=11+10\mathrm{i}$. (b) $(1+\mathrm{i})^2=1+2\mathrm{i}+\mathrm{i}^2=2\mathrm{i}$, also $(1+\mathrm{i})^4=(2\mathrm{i})^2=-4$. (c) $27=4\cdot6+3$ gibt $\mathrm{i}^{27}=\mathrm{i}^3=-\mathrm{i}$, und $42=4\cdot10+2$ gibt $\mathrm{i}^{42}=\mathrm{i}^2=-1$. Die Summe ist $-1-\mathrm{i}$.
:::
:::
