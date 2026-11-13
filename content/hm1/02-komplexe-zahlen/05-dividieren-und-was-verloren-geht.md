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

::::formelsammlung
**Kehrwert**

$$z^{-1}=\frac1z=\frac{\overline{z}}{z\overline{z}}=\frac{x}{x^2+y^2}-\mathrm{i}\,\frac{y}{x^2+y^2}\qquad\text{mit}\qquad z\cdot z^{-1}=1$$

Für $z=x+\mathrm{i}y\ne0$; dann ist $x^2+y^2>0$. Geometrisch: an der reellen Achse spiegeln, durch $x^2+y^2$ teilen. Für $z=0$ gibt es keinen Kehrwert, denn $0\cdot w=0\ne1$.

**Division**

$$\frac wz=w\cdot z^{-1}=\frac{w\,\overline{z}}{x^2+y^2}$$

Für $z=x+\mathrm{i}y\ne0$ und beliebiges $w$: mit der konjugierten Zahl des Nenners erweitern, der Nenner wird reell.

**$\mathbb{C}$ ist ein Körper**

$$-z=-x-\mathrm{i}y,\qquad(1,0)\odot(x,y)=(x,y)$$

Alle Körperaxiome gelten, mit dem Negativen $-z$, dem Einselement $(1,0)$ und dem Kehrwert $1/z$ für $z\ne0$. Deshalb gelten Bruchrechnung, binomische Formeln und der Schluss von $zw=0$ auf $z=0$ oder $w=0$.

**$\mathbb{C}$ ist nicht angeordnet**

$$1\cdot1+\mathrm{i}\cdot\mathrm{i}=1+(-1)=0$$

Wären $1\cdot1>0$ und $\mathrm{i}\cdot\mathrm{i}>0$ wie jedes Quadrat einer Zahl $\ne0$ in einem angeordneten Körper, folgte mit (T2) $0>0$, gegen (T1). Vergleichen darf man nur reelle Größen wie $\operatorname{Re}(z)$ oder $|z|$.
::::

::::lernkarten
:::karte formel Kehrwert
Wie berechnet man den Kehrwert einer komplexen Zahl $z=x+\mathrm{i}y\ne0$ in Normalform?
---
$z^{-1}=\frac1z=\frac{\overline{z}}{z\overline{z}}=\frac{x}{x^2+y^2}-\mathrm{i}\,\frac{y}{x^2+y^2}$ mit $z\cdot z^{-1}=1$. Wegen $z\ne0$ ist der reelle Nenner $x^2+y^2>0$.
--- falsch
$\frac1z=\frac1x+\mathrm{i}\,\frac1y$: Man nimmt die Kehrwerte von Realteil und Imaginärteil einzeln, wie man auch einzeln addiert. Das geht, solange $x\ne0$ und $y\ne0$ sind.
--- falsch
$z^{-1}=\frac1z=\frac{\overline{z}}{z\overline{z}}=\frac{x}{x^2+y^2}+\mathrm{i}\,\frac{y}{x^2+y^2}$ mit $z\cdot z^{-1}=1$. Wegen $z\ne0$ ist der reelle Nenner $x^2+y^2>0$.
--- falsch
$z^{-1}=\frac1z=\frac{\overline{z}}{z\overline{z}}=\frac{x}{x^2-y^2}-\mathrm{i}\,\frac{y}{x^2-y^2}$ mit $z\cdot z^{-1}=1$. Der Nenner ist reell, darf aber nicht null sein, also $x\ne\pm y$.
:::
:::karte formel Division
Wie teilt man eine komplexe Zahl $w$ durch $z=x+\mathrm{i}y\ne0$, und warum funktioniert das?
---
Man erweitert mit der konjugierten Zahl des Nenners: $\frac wz=\frac{w\,\overline{z}}{x^2+y^2}$. Der Wert bleibt gleich, der Nenner wird reell, und durch eine reelle Zahl teilt man Realteil und Imaginärteil einzeln.
--- falsch
Man teilt Realteil durch Realteil und Imaginärteil durch Imaginärteil. Das ist erlaubt, weil die Division wie die Addition getrennt je Koordinate läuft; der Nenner muss dafür in beiden Teilen von null verschieden sein.
--- falsch
Man erweitert mit $z$ selbst: $\frac wz=\frac{wz}{z^2}$. Der Wert bleibt gleich, und der Nenner $z^2$ ist reell, weil beim Quadrieren das $\mathrm{i}$ zu $-1$ wird; dann teilt man Realteil und Imaginärteil einzeln.
--- falsch
Man erweitert mit der konjugierten Zahl des Nenners: $\frac wz=\frac{w\,\overline{z}}{x^2-y^2}$. Der Wert bleibt gleich, und der Nenner wird nach der dritten binomischen Formel reell, solange $x\ne\pm y$ ist.
:::
:::karte zusammenhang Kehrwert in der Ebene
Wie entsteht der Kehrwert $1/z$ geometrisch aus dem Punkt $z$ in der komplexen Ebene?
---
In zwei Schritten: an der reellen Achse spiegeln, dann durch $x^2+y^2$ teilen. Der Kehrwert liegt deshalb auf dem Pfeil von $\overline{z}$; für $z_2$ ist er ein Fünftel von $\overline{z_2}$.
--- falsch
In zwei Schritten: um $90^\circ$ gegen den Uhrzeigersinn drehen, dann durch $x^2+y^2$ teilen. Der Kehrwert steht deshalb immer senkrecht auf dem Pfeil von $z$.
--- falsch
In einem Schritt: am Nullpunkt spiegeln. Der Kehrwert ist der umgekehrte Pfeil $-z$, weil $z+(-z)=0$ ist und der Kehrwert die Rechnung mit $z$ wieder aufhebt.
--- falsch
In zwei Schritten: an der reellen Achse spiegeln, dann mit $x^2+y^2$ multiplizieren. Der Kehrwert liegt deshalb auf dem Pfeil von $\overline{z}$, aber weiter außen als $z$ selbst.
:::
:::karte zusammenhang kein Kehrwert der Null
Warum hat $z=0$ keinen Kehrwert, während jedes $z\ne0$ einen hat?
---
Für $z=0$ ist $0\cdot w=0\ne1$ für jedes $w$, kein Produkt mit der Null ergibt also 1. Für $z\ne0$ ist $x\ne0$ oder $y\ne0$, also $x^2+y^2>0$, und der Bruch mit diesem Nenner ist erklärt.
--- falsch
Auch $z=0$ hat in $\mathbb{C}$ einen Kehrwert, eine unendlich ferne Zahl auf der imaginären Achse; nur in $\mathbb{R}$ fehlt er, weil dort die zweite Achse fehlt.
--- falsch
Keinen Kehrwert haben alle $z$ mit $x=0$ oder $y=0$, weil dann einer der Brüche $\frac x{x^2+y^2}$ und $\frac y{x^2+y^2}$ den Zähler null hat und wegfällt.
--- falsch
Für $z=0$ ist $\overline{z}=0$, und man müsste durch $\overline{z}$ teilen. Für $z\ne0$ gibt es den Kehrwert nur, wenn zusätzlich $x^2-y^2\ne0$ ist, sonst verschwindet der Nenner.
:::
:::karte zusammenhang Körper
Warum ist $\mathbb{C}$ ein Körper, und welche Rechenregeln gelten deshalb auch in $\mathbb{C}$?
---
Die Addition läuft getrennt und erbt alle Gesetze von $\mathbb{R}$; die Multiplikation ist kommutativ, assoziativ und distributiv, mit Einselement $(1,0)$ und Kehrwert für jedes $z\ne0$. Deshalb gelten Bruchrechnung, binomische Formeln und der Schluss von $zw=0$ auf $z=0$ oder $w=0$.
--- falsch
Weil $\mathbb{C}$ die reellen Zahlen enthält und jede Menge, die einen Körper enthält, selbst ein Körper ist. Deshalb gelten Bruchrechnung und binomische Formeln, aber nur für die reellen Zahlen in $\mathbb{C}$; für alle anderen muss man jede Regel neu prüfen.
--- falsch
Weil es auf $\mathbb{C}$ eine Anordnung mit allen Anordnungsaxiomen gibt, aus der die Körperaxiome folgen. Deshalb gelten Bruchrechnung, binomische Formeln und das Rechnen mit Ungleichungen in $\mathbb{C}$ genau wie in $\mathbb{R}$, auch das Quadrieren.
--- falsch
Alle Körperaxiome gelten, und sogar die Null hat einen Kehrwert, weil $\overline{0}=0$ ist und man mit ihm erweitern kann. Deshalb gelten Bruchrechnung und binomische Formeln, aber nicht der Schluss von $zw=0$ auf $z=0$ oder $w=0$.
:::
:::karte herleitung Produkt mit dem Kehrwert
Wie bestätigt man mit der Multiplikation für Paare, dass $(x/N,\,-y/N)$ mit $N:=x^2+y^2>0$ der Kehrwert von $(x,y)$ ist?
---
Die erste Koordinate des Produkts ist $\frac{x\cdot x}N-\frac{y\cdot(-y)}N$, weil man $x_1x_2-y_1y_2$ mit dem zweiten Faktor $\Bigl(\frac xN,\frac{-y}N\Bigr)$ bildet; sie ergibt $\frac{x^2+y^2}N$.
---
Die zweite Koordinate ist $\frac{x\cdot(-y)}N+\frac{y\cdot x}N$, und sie ist null, weil sich die beiden Mischglieder aufheben.
---
Das Produkt ist also $\Bigl(\frac{x^2+y^2}N,\;0\Bigr)=(1,0)$, weil $N=x^2+y^2$ ist; und $(1,0)$ ist das Einselement.
---
Teilen durch $N$ ist erlaubt, weil aus $z\ne0$ folgt, dass $x\ne0$ oder $y\ne0$ ist, und damit $N>0$.
:::
:::karte herleitung keine Anordnung auf den komplexen Zahlen
Wie führt die Annahme einer Relation „$>0$“ auf $\mathbb{C}$ mit den Anordnungsaxiomen (T1) bis (T3) zu einem Widerspruch?
---
Für jedes $x\ne0$ wäre $x\cdot x>0$, weil bei $x>0$ das Axiom (T3) greift und bei $-x>0$ ebenfalls (T3) mit $(-x)(-x)=x\cdot x$.
---
Insbesondere wären $1\cdot1>0$ und $\mathrm{i}\cdot\mathrm{i}>0$, weil $1\ne0$ und $\mathrm{i}\ne0$ gilt.
---
Nach (T2) folgte $1\cdot1+\mathrm{i}\cdot\mathrm{i}>0$, weil die Summe positiver Zahlen positiv ist.
---
Das ist $1+(-1)=0>0$, ein Widerspruch zu (T1), weil für $0$ nur die Beziehung $0=0$ gelten darf und nicht zugleich $0>0$.
:::
:::karte zusammenhang nur reelle Größen vergleichen
Welche Vergleiche mit „kleiner“ und „größer“ sind bei komplexen Zahlen noch erlaubt, da $\mathbb{C}$ nicht angeordnet ist?
---
Nur Vergleiche reeller Größen wie $\operatorname{Re}(z)$ oder $|z|$, denn dort gelten die Anordnungsaxiome von $\mathbb{R}$. Für nicht reelle Zahlen haben $z<w$ und $z>0$ keine Bedeutung.
--- falsch
Alle Vergleiche wie in $\mathbb{R}$, sofern man zuerst nach dem Realteil und bei Gleichheit nach dem Imaginärteil sortiert; diese Reihenfolge verträgt sich mit allen Rechenarten.
--- falsch
Nur Vergleiche zwischen Zahlen mit gleichem Imaginärteil. Für sie gilt $z<w$ genau dann, wenn $\mathrm{i}z<\mathrm{i}w$, weil die Drehung die Reihenfolge erhält.
--- falsch
Gar keine: Auch Realteile und andere reelle Größen, die aus komplexen Zahlen berechnet werden, darf man nicht mehr vergleichen, weil sie aus $\mathbb{C}$ stammen.
:::
:::karte zusammenhang Sortieren nach Realteil und Imaginärteil
Warum ergibt das Sortieren zuerst nach dem Realteil und dann nach dem Imaginärteil keine Anordnung von $\mathbb{C}$?
---
Sortieren kann man so, aber es verträgt sich nicht mit der Multiplikation: Es ergäbe $\mathrm{i}>0$, aber $\mathrm{i}\cdot\mathrm{i}=-1<0$, gegen (T3). Das trifft jede Festlegung.
--- falsch
Weil dabei zwei verschiedene Zahlen gleich eingeordnet würden: Zahlen mit gleichem Realteil ließen sich nicht mehr unterscheiden, und damit wäre (T1) verletzt.
--- falsch
Weil es sich nicht mit der Addition verträgt: Die Summe zweier so positiver Zahlen kann einen negativen Realteil haben, und damit wäre (T2) verletzt.
--- falsch
Weil der Imaginärteil keine reelle Zahl ist und man ihn deshalb nicht der Größe nach sortieren kann; nur die Realteile lassen sich miteinander vergleichen.
:::
::::
