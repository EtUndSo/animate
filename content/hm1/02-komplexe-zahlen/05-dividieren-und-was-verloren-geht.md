---
title: Stufe 4: Dividieren, und was verloren geht
pfad: Elektrotechnik / 1. Semester / HöMa1 – Höhere Mathematik 1 / Komplexe Zahlen
adresse: elektrotechnik/1-semester/hohere-mathematik-1/komplexe-zahlen
knoten: Kapitel 2: Komplexe Zahlen
order: 1220500
summary: Stufe 3 liefert ein reelles Produkt.
tags: 
lang: de
---

<span class="anker" id="stufe-4"></span>

:::zweck
Stufe [3](spiegeln-an-der-reellen-achse.html#stufe-3) liefert ein reelles Produkt. Diese Stufe macht daraus die Division, zeigt, dass $\mathbb{C}$ ein Körper ist, und erklärt, warum die Anordnung fehlt.
:::

**Die Idee.** Durch eine reelle Zahl lässt sich teilen: Realteil und Imaginärteil werden einzeln geteilt. Also erweitert man den Bruch mit der konjugierten Zahl des Nenners. Der Wert bleibt gleich, der Nenner wird reell. In der Ebene entsteht $1/z$ in zwei Schritten: an der reellen Achse spiegeln, dann durch $x^2+y^2$ teilen (Abb. [4](#abb-4)). Genau so zerlegt die Wechselstromrechnung Brüche aus komplexen Widerständen in Real- und Imaginärteil.

:::abbildung hm1/k2kehrwert 4
Der Kehrwert von $z_2$ in zwei Schritten: spiegeln und durch 5 teilen. Der Kehrwert liegt auf dem Pfeil von $\overline{z_2}$.
:::

:::satz Satz 4.1 (Kehrwert und Division)
<span class="anker" id="satz-4-1"></span>

Zu jedem $z=x+\mathrm{i}y\ne0$ gibt es die Zahl

<span class="anker" id="gl-4-1"></span>
$$z^{-1}=\frac1z=\frac{\overline{z}}{z\overline{z}}=\frac{x}{x^2+y^2}-\mathrm{i}\,\frac{y}{x^2+y^2}\qquad\text{mit}\qquad z\cdot z^{-1}=1. \tag{4.1}$$

Für beliebiges $w$ ist damit $\dfrac wz=w\cdot z^{-1}=\dfrac{w\,\overline{z}}{x^2+y^2}$.
:::

⁠**So liest man das:** Der Nenner $x^2+y^2$ ist reell. **Gültigkeit:** Wegen $z\ne0$ ist $x\ne0$ oder $y\ne0$, also $x^2+y^2>0$. Für $z=0$ gibt es keinen Kehrwert, denn $0\cdot w=0\ne1$ für jedes $w$. **Grenzfall:** Für $y=0$ wird aus [(4.1)](#gl-4-1) der reelle Kehrwert $x/x^2=1/x$.

:::beweis Produkt mit dem Kehrwert
Sei $N:=x^2+y^2>0$. Der Kehrwert ist das Paar $(x/N,\,-y/N)$. Nach [(1.2)](paare-statt-einzelner-zahlen.html#gl-1-2) gilt

$$(x,y)\odot\Bigl(\frac xN,\frac{-y}N\Bigr)=\Bigl(\frac{x\cdot x}N-\frac{y\cdot(-y)}N,\;\frac{x\cdot(-y)}N+\frac{y\cdot x}N\Bigr)=\Bigl(\frac{x^2+y^2}N,\;0\Bigr)=(1,0).$$
:::

::::beispiel
Mit dem Rechenmodell, Nenner $z_2\overline{z_2}=5$:

$$\frac{z_1}{z_2}=\frac{(3+\mathrm{i})(1-2\mathrm{i})}{(1+2\mathrm{i})(1-2\mathrm{i})}=\frac{3-6\mathrm{i}+\mathrm{i}-2\mathrm{i}^2}{5}=\frac{5-5\mathrm{i}}{5}=1-\mathrm{i}.$$

Probe: $(1-\mathrm{i})(1+2\mathrm{i})=1+2\mathrm{i}-\mathrm{i}-2\mathrm{i}^2=3+\mathrm{i}$. Außerdem ist $1/z_2=(1-2\mathrm{i})/5=0{,}2-0{,}4\mathrm{i}$ und $1/\mathrm{i}=-\mathrm{i}$.
::::

:::satz Satz 4.2 ($\mathbb{C}$ ist ein Körper)
<span class="anker" id="satz-4-2"></span>

$\mathbb{C}$ erfüllt mit $+$ und $\cdot$ alle Körperaxiome aus [Kapitel 1](/wissen/elektrotechnik/1-semester/hohere-mathematik-1/mengen-logik-und-reelle-zahlen/mengen-logik-und-reelle-zahlen.html): Kommutativ-, Assoziativ- und Distributivgesetz, neutrale Elemente $0\ne1$, zu jedem $z$ das Negative $-z$ und zu jedem $z\ne0$ den Kehrwert $1/z$.
:::

⁠**So liest man das:** Was in [Kapitel 1](/wissen/elektrotechnik/1-semester/hohere-mathematik-1/mengen-logik-und-reelle-zahlen/mengen-logik-und-reelle-zahlen.html) nur aus den Körperaxiomen folgt, gilt auch in $\mathbb{C}$: Bruchrechnung, binomische Formeln und der Schluss von $zw=0$ auf $z=0$ oder $w=0$.

:::beweis Idee
Die Addition läuft getrennt und erbt alle Gesetze von $\mathbb{R}$, mit $-z=-x-\mathrm{i}y$. [(1.2)](paare-statt-einzelner-zahlen.html#gl-1-2) ändert sich nicht beim Tausch der Indizes 1 und 2: Die Multiplikation ist kommutativ. Assoziativ- und Distributivgesetz zeigt man, indem man beide Seiten nach [(1.2)](paare-statt-einzelner-zahlen.html#gl-1-2) ausrechnet. $(1,0)\odot(x,y)=(x,y)$ zeigt das Einselement, [(4.1)](#gl-4-1) das Axiom (M4), den Kehrwert.
:::

:::satz Satz 4.3 ($\mathbb{C}$ ist nicht angeordnet)
<span class="anker" id="satz-4-3"></span>

Es gibt keine Relation „$>0$“ auf $\mathbb{C}$ mit den Anordnungsaxiomen aus [Kapitel 1](/wissen/elektrotechnik/1-semester/hohere-mathematik-1/mengen-logik-und-reelle-zahlen/mengen-logik-und-reelle-zahlen.html): (T1) Für jedes $x$ gilt genau eines von $x>0$, $x=0$, $-x>0$. (T2) Aus $x>0$ und $y>0$ folgt $x+y>0$. (T3) Aus $x>0$ und $y>0$ folgt $x\cdot y>0$.
:::

⁠**So liest man das:** Für nicht reelle Zahlen haben $z<w$ und $z>0$ keine Bedeutung. Vergleichen darf man nur reelle Größen wie $\operatorname{Re}(z)$ oder $|z|$.

:::beweis Widerspruch
Angenommen, es gäbe eine solche Relation. Für jedes $x\ne0$ wäre dann $x\cdot x>0$: Bei $x>0$ folgt das aus (T3), bei $-x>0$ aus (T3) und $(-x)(-x)=x\cdot x$. Insbesondere wären $1\cdot1>0$ und $\mathrm{i}\cdot\mathrm{i}>0$. Mit (T2) folgte $1\cdot1+\mathrm{i}\cdot\mathrm{i}>0$. Das ist $1+(-1)=0>0$, ein Widerspruch zu (T1).
:::

:::frage Lässt sich nicht eine Reihenfolge festlegen, etwa zuerst nach dem Realteil, dann nach dem Imaginärteil?
Sortieren kann man so. Das verträgt sich nur nicht mit der Multiplikation: Es ergäbe $\mathrm{i}>0$, aber $\mathrm{i}\cdot\mathrm{i}=-1<0$, gegen (T3). Der Beweis zeigt, dass das jede Festlegung trifft.
:::

:::aufgabe Aufgabe 4 ★ Teilen
<span class="anker" id="aufg-4"></span>

(a) Bringe $\dfrac{7+\mathrm{i}}{2-\mathrm{i}}$ auf Normalform. (b) Berechne $\dfrac{10}{1+3\mathrm{i}}+\dfrac{3-\mathrm{i}}{1+\mathrm{i}}$. (c) Löse $(2+\mathrm{i})z-3=-2+3\mathrm{i}$ und mache die Probe.

:::loesung
(a) $\dfrac{(7+\mathrm{i})(2+\mathrm{i})}{(2-\mathrm{i})(2+\mathrm{i})}=\dfrac{14+7\mathrm{i}+2\mathrm{i}+\mathrm{i}^2}{5}=\dfrac{13+9\mathrm{i}}5=2{,}6+1{,}8\mathrm{i}$.

(b) $\dfrac{10(1-3\mathrm{i})}{10}=1-3\mathrm{i}$ und $\dfrac{(3-\mathrm{i})(1-\mathrm{i})}{2}=\dfrac{3-3\mathrm{i}-\mathrm{i}+\mathrm{i}^2}2=\dfrac{2-4\mathrm{i}}2=1-2\mathrm{i}$. Die Summe ist $2-5\mathrm{i}$.

(c) $(2+\mathrm{i})z=1+3\mathrm{i}$, also $z=\dfrac{(1+3\mathrm{i})(2-\mathrm{i})}{5}=\dfrac{2-\mathrm{i}+6\mathrm{i}-3\mathrm{i}^2}5=\dfrac{5+5\mathrm{i}}5=1+\mathrm{i}$. Probe: $(2+\mathrm{i})(1+\mathrm{i})-3=1+3\mathrm{i}-3=-2+3\mathrm{i}$.
:::
:::

:::aufgabe Aufgabe 5 ★★ Ein Versuch, $\mathbb{C}$ anzuordnen
<span class="anker" id="aufg-5"></span>

Jemand nennt $z$ positiv, wenn $\operatorname{Re}(z)>0$ ist. Prüfe (T1), (T2) und (T3) und gib für jedes verletzte Axiom ein Gegenbeispiel an.

:::loesung
(T1) ist verletzt: Für $\mathrm{i}$ ist $\operatorname{Re}(\mathrm{i})=0$ und $\operatorname{Re}(-\mathrm{i})=0$, also ist weder $\mathrm{i}$ noch $-\mathrm{i}$ positiv, obwohl $\mathrm{i}\ne0$. (T2) gilt, denn nach Stufe [3](spiegeln-an-der-reellen-achse.html#stufe-3) ist $\operatorname{Re}(z+w)=\operatorname{Re}(z)+\operatorname{Re}(w)>0$. (T3) ist verletzt: $z=1+2\mathrm{i}$ ist positiv, aber $z\cdot z=-3+4\mathrm{i}$ hat den Realteil $-3$. Der Grund ist das Glied $-y_1y_2$ im Realteil des Produkts.
:::
:::
