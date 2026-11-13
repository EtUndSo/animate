---
title: Stufe 1: Paare statt einzelner Zahlen
pfad: Elektrotechnik / 1. Semester / HöMa1 – Höhere Mathematik 1 / Komplexe Zahlen
adresse: elektrotechnik/1-semester/hohere-mathematik-1/komplexe-zahlen
knoten: Kapitel 2: Komplexe Zahlen
order: 1220200
summary: In mathbb R hat x 2=-1 keine Lösung.
tags: Normalform
lang: de
---

<span class="anker" id="stufe-1"></span>

:::zweck
In $\mathbb{R}$ hat $x^2=-1$ keine Lösung. Diese Stufe baut eine größere Zahlenmenge, in der die Gleichung lösbar ist und $\mathbb{R}$ unverändert enthalten bleibt.
:::

**Die Idee.** Jede Erweiterung der Zahlen löst eine Gleichung, die vorher keine Lösung hatte: $x+1=0$ führt von $\mathbb{N}$ zu $\mathbb{Z}$, $2x=1$ von $\mathbb{Z}$ zu $\mathbb{Q}$, $x^2=2$ von $\mathbb{Q}$ zu $\mathbb{R}$. Bei $x^2=-1$ liegt der Fall anders. Die Parabel $y=x^2$ erreicht die Höhe $-1$ nie (Abb. [1](#abb-1)), denn in $\mathbb{R}$ gilt $x^2\ge0$ ([Kapitel 1](/wissen/elektrotechnik/1-semester/hohere-mathematik-1/mengen-logik-und-reelle-zahlen/mengen-logik-und-reelle-zahlen.html)). Es fehlt kein Punkt zwischen anderen Punkten wie bei $\sqrt2$, sondern jeder Punkt der Zahlengeraden scheidet aus. Die Lösung muss neben der Geraden liegen. Deshalb kommt eine zweite Koordinate hinzu: Man rechnet mit Paaren $(x,y)$. Die Paare $(x,0)$ sollen die reellen Zahlen bleiben, und $(0,1)$ soll zum Quadrat $(-1,0)$ ergeben.

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

::::formelsammlung
**Komplexe Zahlen**

$$\mathbb{C}:=\{(x,y):x,y\in\mathbb{R}\}$$

Die Menge aller Paare reeller Zahlen. Das Nullelement ist $(0,0)$, das Einselement $(1,0)$.

**Addition und Multiplikation von Paaren**

$$(x_1,y_1)\oplus(x_2,y_2):=(x_1+x_2,\;y_1+y_2),\qquad(x_1,y_1)\odot(x_2,y_2):=(x_1x_2-y_1y_2,\;x_1y_2+x_2y_1)$$

Für $y_1=y_2=0$ entstehen $(x_1+x_2,0)$ und $(x_1x_2,0)$: Die Paare $(x,0)$ rechnen wie die reellen Zahlen $x$. Deshalb schreibt man $x$ statt $(x,0)$, $+$ statt $\oplus$, $\cdot$ statt $\odot$, und es gilt $\mathbb{R}\subset\mathbb{C}$.

**Imaginäre Einheit**

$$\mathrm{i}:=(0,1),\qquad\mathrm{i}^2=-1$$

$\mathrm{i}^2=(0,1)\odot(0,1)=(-1,0)$. In der Elektrotechnik schreibt man $\mathrm{j}$, weil $i$ dort der Strom ist.

**Normalform**

$$z=x+\mathrm{i}y$$

Mit $x,y\in\mathbb{R}$; jede komplexe Zahl hat genau eine Normalform, denn $x+\mathrm{i}y=(x,y)$. Für nicht reelle $x,y$ ist die Darstellung nicht eindeutig: $\mathrm{i}=\mathrm{i}+\mathrm{i}\cdot0=0+\mathrm{i}\cdot1$.

**Summe in der Normalform**

$$(x_1+\mathrm{i}y_1)+(x_2+\mathrm{i}y_2)=(x_1+x_2)+\mathrm{i}(y_1+y_2)$$

Realteile und Imaginärteile addieren sich getrennt.

**Produkt in der Normalform**

$$(x_1+\mathrm{i}y_1)(x_2+\mathrm{i}y_2)=(x_1x_2-y_1y_2)+\mathrm{i}(x_1y_2+x_2y_1)$$

Klammern ausmultiplizieren, $\mathrm{i}^2=-1$ einsetzen, sortieren. Das Minus in $x_1x_2-y_1y_2$ ist das $\mathrm{i}^2$.

**Potenzen von $\mathrm{i}$**

$$\mathrm{i}^1=\mathrm{i},\qquad\mathrm{i}^2=-1,\qquad\mathrm{i}^3=-\mathrm{i},\qquad\mathrm{i}^4=1$$

Die Potenzen wiederholen sich mit der Periode 4; es zählt nur der Rest von $n$ bei Division durch 4.
::::

::::lernkarten
:::karte zusammenhang zweite Koordinate
Warum lässt sich $x^2=-1$ nicht wie $x^2=2$ lösen, indem man eine Lücke der Zahlengeraden füllt?
---
Weil in $\mathbb{R}$ stets $x^2\ge0$ gilt: Die Parabel $y=x^2$ erreicht die Höhe $-1$ nie. Es fehlt kein Punkt zwischen anderen, jeder Punkt der Geraden scheidet aus; die Lösung muss neben der Geraden liegen.
--- falsch
Weil die Lücke bei $x^2=-1$ zu schmal ist, um sie mit Dezimalzahlen zu treffen: Die Lösung liegt zwischen $-1$ und $0$, hat aber eine nie endende, nicht periodische Darstellung.
--- falsch
Weil die Parabel $y=x^2$ die Höhe $-1$ nur in einem einzigen Punkt berührt, der auf der Zahlengeraden fehlt. Diesen einen Punkt ergänzt man, indem man eine zweite Koordinate einführt.
--- falsch
Weil $-1$ auf der rechten Seite steht: Gleichungen, deren rechte Seite negativ ist, haben grundsätzlich keine Lösung, auch dann nicht, wenn man die Zahlengerade um weitere Punkte ergänzt.
:::
:::karte begriff komplexe Zahl
Was ist eine komplexe Zahl, und wie ist die Menge $\mathbb{C}$ der komplexen Zahlen festgelegt?
---
Ein Paar $(x,y)$ reeller Zahlen. $\mathbb{C}:=\{(x,y):x,y\in\mathbb{R}\}$ ist die Menge aller Paare mit einer Addition $\oplus$ und einer Multiplikation $\odot$; Nullelement $(0,0)$, Einselement $(1,0)$.
--- falsch
Eine Wurzel aus einer negativen reellen Zahl, etwa die Wurzel aus $-2$. $\mathbb{C}$ ist die Menge dieser Wurzeln; sie liegen neben der Zahlengeraden und ergänzen $\mathbb{R}$ zu einer größeren Menge.
--- falsch
Eine reelle Zahl, die man zusätzlich mit dem Zeichen $\mathrm{i}$ versieht. $\mathbb{C}$ ist also $\mathbb{R}$ mit einem neuen Rechenzeichen, das beim Quadrieren das Vorzeichen des Ergebnisses umdreht.
--- falsch
Ein Paar $(x,y)$ reeller Zahlen. $\mathbb{C}$ ist die Menge aller solchen Paare, die man Koordinate für Koordinate addiert und multipliziert, also mit dem Produkt $(x_1x_2,\;y_1y_2)$.
:::
:::karte formel Addition und Multiplikation von Paaren
Nach welchen Vorschriften addiert und multipliziert man zwei komplexe Zahlen, solange man sie als Paare schreibt?
---
$(x_1,y_1)\oplus(x_2,y_2):=(x_1+x_2,\;y_1+y_2)$ und $(x_1,y_1)\odot(x_2,y_2):=(x_1x_2-y_1y_2,\;x_1y_2+x_2y_1)$. Nur die Addition läuft Koordinate für Koordinate.
--- falsch
$(x_1,y_1)\oplus(x_2,y_2):=(x_1+x_2,\;y_1+y_2)$ und $(x_1,y_1)\odot(x_2,y_2):=(x_1x_2,\;y_1y_2)$. Beide Rechenarten laufen Koordinate für Koordinate, wie bei Vektoren.
--- falsch
$(x_1,y_1)\oplus(x_2,y_2):=(x_1+x_2,\;y_1+y_2)$ und $(x_1,y_1)\odot(x_2,y_2):=(x_1x_2+y_1y_2,\;x_1y_2+x_2y_1)$. Ein Minus tritt nirgends auf.
--- falsch
$(x_1,y_1)\oplus(x_2,y_2):=(x_1+y_1,\;x_2+y_2)$ und $(x_1,y_1)\odot(x_2,y_2):=(x_1x_2-y_1y_2,\;x_1y_2+x_2y_1)$. Addiert wird innerhalb jedes Paars.
:::
:::karte zusammenhang reelle Zahlen als Paare
Warum darf man das Paar $(x,0)$ einfach als reelle Zahl $x$ schreiben und $\mathbb{R}\subset\mathbb{C}$ sagen?
---
Weil diese Paare genau wie die reellen Zahlen rechnen: Für $y_1=y_2=0$ ergeben Addition und Multiplikation die Paare $(x_1+x_2,0)$ und $(x_1x_2,0)$. Deshalb schreibt man auch $+$ statt $\oplus$ und $\cdot$ statt $\odot$.
--- falsch
Weil man das so festlegt, ohne dass es Folgen hat: Die Rechenarten für Paare stimmen mit denen von $\mathbb{R}$ ohnehin nicht überein, die Schreibweise $x$ ist nur eine bequeme Abkürzung für das Paar.
--- falsch
Weil $(x,0)$ und $(0,x)$ dieselbe Zahl darstellen und eine der beiden Koordinaten immer null ist; welche Koordinate verschwindet, spielt für das Rechnen mit den Paaren keine Rolle.
--- falsch
Weil diese Paare beim Addieren wie reelle Zahlen rechnen. Beim Multiplizieren entsteht zwar auch $(x_1x_2,0)$, aber nur, solange beide Faktoren positiv sind; sonst kippt das Vorzeichen.
:::
:::karte begriff imaginäre Einheit
Welches Paar ist die imaginäre Einheit $\mathrm{i}$, und welche Gleichung erfüllt sie?
---
Das Paar $\mathrm{i}:=(0,1)$. Nach der Multiplikation für Paare ist $\mathrm{i}\cdot\mathrm{i}=(0\cdot0-1\cdot1,\;0\cdot1+0\cdot1)=(-1,0)$, also $\mathrm{i}^2=-1$; damit ist $x^2=-1$ lösbar.
--- falsch
Das Paar $(1,0)$, also das Einselement. Es erfüllt $\mathrm{i}^2=1$ und trägt nur einen eigenen Namen, damit man es von der reellen Eins unterscheidet.
--- falsch
Die Zahl links von der Null, deren Quadrat $-1$ ist; in $\mathbb{C}$ bleibt das Quadrat einer negativen Zahl negativ, deshalb gilt $\mathrm{i}^2=-1$.
--- falsch
Das Paar $(0,1)$. Koordinatenweise multipliziert ist $\mathrm{i}\cdot\mathrm{i}=(0\cdot0,\;1\cdot1)=(0,1)$, also $\mathrm{i}^2=\mathrm{i}$; erst die Normalform macht daraus $-1$.
:::
:::karte begriff Normalform
Was ist die Normalform einer komplexen Zahl, und unter welcher Bedingung ist sie eindeutig?
---
Die Schreibweise $z=x+\mathrm{i}y$ mit $x,y\in\mathbb{R}$; jede komplexe Zahl hat genau eine. Ohne die Bedingung „reell“ wäre etwa $\mathrm{i}=\mathrm{i}+\mathrm{i}\cdot0=0+\mathrm{i}\cdot1$ zweimal dargestellt.
--- falsch
Die Schreibweise $z=x+\mathrm{i}y$ mit beliebigen $x,y\in\mathbb{C}$; jede komplexe Zahl hat genau eine, weil $x$ und $y$ durch $z$ festgelegt sind, gleich aus welcher Zahlenmenge sie stammen.
--- falsch
Die Schreibweise $z=x+\mathrm{i}y$ mit $x,y\in\mathbb{R}$ und $x\ge y$. Ohne diese Bedingung könnte man Realteil und Imaginärteil vertauschen und erhielte dieselbe Zahl in zwei Formen.
--- falsch
Die Schreibweise als Paar $(x,y)$ mit $x\ge0$ und $y\ge0$; jede komplexe Zahl hat genau eine, weil man negative Teile vorher durch Spiegeln an den Achsen beseitigt.
:::
:::karte formel Produktformel
Wie multipliziert man zwei komplexe Zahlen in der Normalform, und woher kommt das Minus im Realteil?
---
$(x_1+\mathrm{i}y_1)(x_2+\mathrm{i}y_2)=(x_1x_2-y_1y_2)+\mathrm{i}(x_1y_2+x_2y_1)$: ausmultiplizieren, $\mathrm{i}^2=-1$ einsetzen, sortieren. Das Minus in $x_1x_2-y_1y_2$ ist das $\mathrm{i}^2$.
--- falsch
$(x_1+\mathrm{i}y_1)(x_2+\mathrm{i}y_2)=x_1x_2+\mathrm{i}y_1y_2$: Realteile und Imaginärteile werden getrennt multipliziert, wie sie bei der Addition getrennt addiert werden. Ein Minus tritt nicht auf.
--- falsch
$(x_1+\mathrm{i}y_1)(x_2+\mathrm{i}y_2)=(x_1x_2+y_1y_2)+\mathrm{i}(x_1y_2+x_2y_1)$: ausmultiplizieren und sortieren. Ein Minus tritt nur auf, wenn einer der Imaginärteile negativ ist.
--- falsch
$(x_1+\mathrm{i}y_1)(x_2+\mathrm{i}y_2)=(x_1x_2-y_1y_2)+\mathrm{i}(x_1y_2-x_2y_1)$: ausmultiplizieren und sortieren. Das Minus steht in beiden Teilen, weil $\mathrm{i}$ jedes Mischglied umpolt.
:::
:::karte formel Potenzen von i
Wie berechnet man eine hohe Potenz $\mathrm{i}^n$ wie $\mathrm{i}^{10}$, ohne $n$-mal zu multiplizieren?
---
Die Potenzen wiederholen sich mit der Periode 4: $\mathrm{i}^1=\mathrm{i}$, $\mathrm{i}^2=-1$, $\mathrm{i}^3=-\mathrm{i}$, $\mathrm{i}^4=1$. Es zählt nur der Rest von $n$ bei Division durch 4, etwa $\mathrm{i}^{10}=\mathrm{i}^8\,\mathrm{i}^2=-1$.
--- falsch
Die Potenzen wiederholen sich mit der Periode 2: $\mathrm{i}^1=\mathrm{i}$, $\mathrm{i}^2=-1$, danach wieder $\mathrm{i}$ und $-1$. Es zählt nur, ob $n$ gerade oder ungerade ist, etwa $\mathrm{i}^{4}=\mathrm{i}^2=-1$.
--- falsch
Man rechnet $\mathrm{i}^n=(-1)^n$, weil $\mathrm{i}$ bei jeder weiteren Multiplikation mit sich selbst wieder zu $-1$ wird. Es zählt nur, ob $n$ gerade oder ungerade ist, etwa $\mathrm{i}^{10}=(-1)^{10}=1$.
--- falsch
Die Potenzen wiederholen sich mit der Periode 4, in der Reihenfolge $\mathrm{i}$, $-\mathrm{i}$, $-1$, $1$. Es zählt nur der Rest von $n$ bei Division durch 4, etwa $\mathrm{i}^{10}=\mathrm{i}^2=-\mathrm{i}$.
:::
:::karte herleitung Rechnen mit Paaren
Wie folgt aus den Rechenvorschriften für Paare, dass $\mathrm{i}^2=-1$ gilt und jedes Paar $(x,y)$ die Form $x+\mathrm{i}y$ hat?
---
$\mathrm{i}\cdot\mathrm{i}=(0,1)\odot(0,1)=(0\cdot0-1\cdot1,\;0\cdot1+0\cdot1)=(-1,0)$, weil die erste Koordinate eines Produkts $x_1x_2-y_1y_2$ ist.
---
$(-1,0)$ ist die reelle Zahl $-1$, weil die Paare $(x,0)$ genau wie die reellen Zahlen $x$ rechnen; also gilt $\mathrm{i}^2=-1$.
---
Für reelles $y$ ist $\mathrm{i}y=(0,1)\odot(y,0)=(0\cdot y-1\cdot0,\;0\cdot0+y\cdot1)=(0,y)$, weil man $y$ als Paar $(y,0)$ einsetzt.
---
Damit ist $x+\mathrm{i}y=(x,0)\oplus(0,y)=(x,y)$, weil die Addition Koordinate für Koordinate läuft; das Paar legt $x$ und $y$ eindeutig fest.
:::
:::karte zusammenhang imaginär
Warum ist $\mathrm{i}$ kein bloßer Rechentrick, obwohl es auf der Zahlengeraden nicht vorkommt?
---
Weil $\mathrm{i}$ das Paar $(0,1)$ ist, für das die Multiplikation eindeutig festgelegt ist. Auf der Zahlengeraden liegt es nicht; „imaginär“ ist ein historischer Name.
--- falsch
Weil $\mathrm{i}$ auf der Zahlengeraden doch vorkommt, als Zahl zwischen $-1$ und $0$, deren Quadrat $-1$ ist; man hat sie nur lange übersehen, daher der Name „imaginär“.
--- falsch
Weil $\mathrm{i}$ eine Abkürzung für die Wurzel aus $-1$ ist, für die alle Wurzelregeln aus $\mathbb{R}$ unverändert gelten; „imaginär“ heißt nur, dass man sie nicht zeichnen kann.
--- falsch
Weil die Elektrotechnik $\mathrm{i}$ als Strom misst: Seine Existenz folgt aus Messungen, mathematisch bleibt es ein Rechentrick, für den es keine eigene Definition gibt.
:::
:::karte zusammenhang Schreibweise in der Elektrotechnik
Warum schreibt man die imaginäre Einheit in der Elektrotechnik als $\mathrm{j}$ statt als $\mathrm{i}$?
---
Weil $i$ dort schon den Strom bezeichnet. Gemeint ist dieselbe imaginäre Einheit, das Paar $(0,1)$ mit dem Quadrat $-1$; nur der Buchstabe ist ein anderer.
--- falsch
Weil $\mathrm{j}$ in der Elektrotechnik eine andere Zahl ist, nämlich $\mathrm{j}=-\mathrm{i}$; sie erfüllt $\mathrm{j}^2=+1$ und passt besser zu Spannungen.
--- falsch
Weil $\mathrm{i}$ in der Elektrotechnik zu klein wäre: $\mathrm{j}$ steht für $1000\,\mathrm{i}$, damit die Imaginärteile von Spannungen und Strömen handliche Zahlen werden.
--- falsch
Weil $\mathrm{j}$ das Paar $(1,0)$ bezeichnet. Die Elektrotechnik zählt die Koordinaten in umgekehrter Reihenfolge, deshalb braucht sie einen neuen Buchstaben.
:::
::::
