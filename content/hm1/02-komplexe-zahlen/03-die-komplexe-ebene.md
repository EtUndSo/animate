---
title: Stufe 2: Die komplexe Ebene
pfad: Elektrotechnik / 1. Semester / HöMa1 – Höhere Mathematik 1 / Komplexe Zahlen
adresse: elektrotechnik/1-semester/hohere-mathematik-1/komplexe-zahlen
knoten: Kapitel 2: Komplexe Zahlen
order: 1220300
summary: Ein Paar ist ein Punkt.
tags: reelle Achse, imaginären Achse, rein imaginären, Gaußsche Zahlenebene
lang: de
---

<span class="anker" id="stufe-2"></span>

:::zweck
Ein Paar ist ein Punkt. Diese Stufe zeichnet die komplexen Zahlen in die Ebene und zeigt, was die Addition und die Multiplikation mit $\mathrm{i}$ dort bedeuten.
:::

**Die Idee.** Man trägt $x$ nach rechts und $y$ nach oben auf. Die waagerechte __reelle Achse__ ist $\mathbb{R}$, auf der senkrechten __imaginären Achse__ liegen die __rein imaginären__ Zahlen $\mathrm{i}y$. Jede komplexe Zahl ist ein Punkt oder, gleichwertig, ein Pfeil (Vektor) vom Nullpunkt zu diesem Punkt. Die Addition läuft getrennt je Koordinate: Der Pfeil von $z_2$ wird an die Spitze von $z_1$ gehängt. Beide Reihenfolgen zusammen bilden ein Parallelogramm, die Summe ist seine vierte Ecke (Abb. [2](#abb-2), links). In der Wechselstromrechnung heißen diese Pfeile Zeiger, und Spannungen addieren sich genau so.

:::abbildung hm1/k2ebene 2
Links $z_1$, $z_2$ und das Parallelogramm, orange die reelle Achse: $z_1+z_2=4+3\mathrm{i}$ liegt 3 plus 1 nach rechts und 1 plus 2 nach oben. Rechts dreht jede Multiplikation mit $\mathrm{i}$ um $90^\circ$. Aus $z_1$ werden die Ecken eines Quadrats, aus $1$ die grauen Punkte $\mathrm{i}$, $-1$, $-\mathrm{i}$.
:::

:::definition Definition 2.1 (Realteil, Imaginärteil, Gaußsche Zahlenebene)
<span class="anker" id="satz-2-1"></span>

Für $z=x+\mathrm{i}y$ mit $x,y\in\mathbb{R}$ heißt $x=:\operatorname{Re}(z)$ der Realteil und $y=:\operatorname{Im}(z)$ der Imaginärteil von $z$. Die komplexe Ebene mit den Koordinaten $\operatorname{Re}(z)$ und $\operatorname{Im}(z)$ heißt auch __Gaußsche Zahlenebene__. Es gilt $z=w$ genau dann, wenn $\operatorname{Re}(z)=\operatorname{Re}(w)$ und $\operatorname{Im}(z)=\operatorname{Im}(w)$.
:::

⁠**So liest man das:** Beide Teile sind reell: Der Imaginärteil von $3+\mathrm{i}$ ist 1, nicht $\mathrm{i}$. Eine Gleichung in $\mathbb{C}$ steht also für zwei reelle Gleichungen. Die Differenz $z-w$ ist der Pfeil von $w$ nach $z$, denn $w+(z-w)=z$. Im Rechenmodell ist $z_1-z_2=2-\mathrm{i}$.

:::satz Satz 2.2 (Multiplikation mit $\mathrm{i}$)
<span class="anker" id="satz-2-2"></span>

Für $z=x+\mathrm{i}y$ ist $\mathrm{i}z=-y+\mathrm{i}x$. Der Pfeil von $z$ wird dabei um $90^\circ$ gegen den Uhrzeigersinn um den Nullpunkt gedreht.
:::

⁠**So liest man das:** Aus dem Punkt $(x,y)$ wird $(-y,x)$. Zweimal gedreht ergibt die halbe Drehung, also das Vorzeichen: Das ist der Mechanismus hinter $\mathrm{i}^2=-1$. Eine Vierteldrehung verlässt die Zahlengerade. Deshalb konnte $\mathrm{i}$ dort nicht liegen.

:::beweis Vierteldrehung
Es ist $\mathrm{i}(x+\mathrm{i}y)=\mathrm{i}x+\mathrm{i}^2y=-y+\mathrm{i}x$. Der Pfeil von $z$ ist die Hypotenuse eines rechtwinkligen Dreiecks mit der waagerechten Kathete $x$ und der senkrechten Kathete $y$, beide mit Vorzeichen gezählt. Die Vierteldrehung macht aus $x$ nach rechts $x$ nach oben und aus $y$ nach oben $y$ nach links. Der gedrehte Pfeil endet also bei $(-y,x)$.
:::

::::beispiel
$\mathrm{i}z_1=-1+3\mathrm{i}$, $\mathrm{i}^2z_1=-3-\mathrm{i}=-z_1$, $\mathrm{i}^3z_1=1-3\mathrm{i}$, $\mathrm{i}^4z_1=z_1$ (Abb. [2](#abb-2), rechts).
::::

⁠**Grenzfall:** Ein reeller Faktor $r$ dreht nicht, er streckt: $r(x+\mathrm{i}y)=rx+\mathrm{i}ry$. Für $r=-1$ kehrt er den Pfeil um, wie zweimal $\mathrm{i}$.

:::frage Ist die komplexe Ebene nicht nur die gewöhnliche Koordinatenebene?
Als Menge und beim Addieren ja. Der Unterschied ist die Multiplikation: [(1.2)](paare-statt-einzelner-zahlen.html#gl-1-2) macht aus zwei Punkten wieder einen Punkt, und man kann dadurch teilen (Stufe [4](dividieren-und-was-verloren-geht.html#stufe-4)). Erst das macht aus der Ebene ein Zahlensystem.
:::

:::aufgabe Aufgabe 2 ★★ Geometrie mit Zahlen
<span class="anker" id="aufg-2"></span>

Gegeben sind $P=1+\mathrm{i}$, $Q=4+2\mathrm{i}$, $R=2+4\mathrm{i}$. (a) Berechne die vierte Ecke $S$ des Parallelogramms mit den Seiten $PQ$ und $PR$. Zeige, dass beide Diagonalen dieselbe Mitte haben. (b) Drehe $Q$ um den Punkt $P$ um $90^\circ$ gegen den Uhrzeigersinn. Tipp: Der Pfeil von $P$ nach $Q$ ist $Q-P$. (c) Grenzfall: Was liefert deine Formel aus (b) für $Q=P$?

:::loesung
(a) Von $P$ aus gehen die Pfeile $Q-P=3+\mathrm{i}$ und $R-P=1+3\mathrm{i}$. Die vierte Ecke ist $S=P+(Q-P)+(R-P)=Q+R-P=5+5\mathrm{i}$. Die Mitten der Diagonalen sind $(P+S)/2=(6+6\mathrm{i})/2=3+3\mathrm{i}$ und $(Q+R)/2=(6+6\mathrm{i})/2=3+3\mathrm{i}$.

(b) Man dreht den Pfeil $Q-P$ und setzt ihn wieder bei $P$ an: $P+\mathrm{i}(Q-P)=1+\mathrm{i}+\mathrm{i}(3+\mathrm{i})=1+\mathrm{i}-1+3\mathrm{i}=4\mathrm{i}$. (c) $P+\mathrm{i}\cdot0=P$: Der Drehpunkt bleibt liegen.
:::
:::

::::formelsammlung
**Realteil und Imaginärteil**

$$z=x+\mathrm{i}y,\qquad x=:\operatorname{Re}(z),\qquad y=:\operatorname{Im}(z)$$

Für $x,y\in\mathbb{R}$; beide Teile sind reell, der Imaginärteil ist die Zahl vor $\mathrm{i}$. In der komplexen Ebene (Gaußsche Zahlenebene) ist $\operatorname{Re}(z)$ die Koordinate nach rechts, $\operatorname{Im}(z)$ die nach oben; auf der waagerechten reellen Achse liegt $\mathbb{R}$, auf der senkrechten imaginären Achse liegen die rein imaginären Zahlen $\mathrm{i}y$.

**Gleichheit**

$$z=w\ \Leftrightarrow\ \bigl(\operatorname{Re}(z)=\operatorname{Re}(w)\ \text{und}\ \operatorname{Im}(z)=\operatorname{Im}(w)\bigr)$$

Eine Gleichung in $\mathbb{C}$ steht für zwei reelle Gleichungen.

**Addition und Differenz als Pfeile**

$$w+(z-w)=z$$

Die Summe ist die vierte Ecke des Parallelogramms aus den Pfeilen der Summanden; die Differenz $z-w$ ist der Pfeil von $w$ nach $z$.

**Multiplikation mit $\mathrm{i}$**

$$\mathrm{i}z=-y+\mathrm{i}x$$

Für $z=x+\mathrm{i}y$: Aus dem Punkt $(x,y)$ wird $(-y,x)$, der Pfeil dreht sich um $90^\circ$ gegen den Uhrzeigersinn um den Nullpunkt. Zweimal gedreht ergibt das Vorzeichen, $\mathrm{i}^2=-1$.

**Reeller Faktor**

$$r(x+\mathrm{i}y)=rx+\mathrm{i}ry$$

Für reelles $r$: Der Pfeil wird gestreckt, nicht gedreht; $r=-1$ kehrt ihn um.
::::

::::lernkarten
:::karte begriff komplexe Ebene
Wie stellt man eine komplexe Zahl $z=x+\mathrm{i}y$ in der komplexen Ebene dar?
---
Als Punkt mit $x$ nach rechts und $y$ nach oben, gleichwertig als Pfeil vom Nullpunkt zu diesem Punkt. Alle Paare zusammen bilden die komplexe Ebene; $\mathbb{R}$ ist darin die waagerechte Achse.
--- falsch
Als Punkt, zu dem man $y$ nach rechts und $x$ nach oben abträgt, oder gleichwertig als Pfeil vom Nullpunkt zu diesem Punkt. Alle Paare zusammen bilden die komplexe Ebene; $\mathbb{R}$ ist darin die senkrechte Achse.
--- falsch
Als Strecke auf der Zahlengeraden, die bei $x$ beginnt und bei $y$ endet. Die komplexe Ebene ist die Menge dieser Strecken, und die reellen Zahlen sind darin die Strecken der Länge null.
--- falsch
Als Punkt, zu dem man $x$ nach rechts und $\mathrm{i}y$ nach oben abträgt. Weil $\mathrm{i}y$ keine reelle Zahl ist, lässt sich die komplexe Ebene nur für $y=0$ wirklich zeichnen.
:::
:::karte begriff Realteil
Wie ist der Realteil $\operatorname{Re}(z)$ einer komplexen Zahl $z=x+\mathrm{i}y$ definiert?
---
Für $z=x+\mathrm{i}y$ mit $x,y\in\mathbb{R}$ ist $\operatorname{Re}(z):=x$, der Anteil ohne $\mathrm{i}$. In der komplexen Ebene ist er die Koordinate nach rechts; bei $z_1=3+\mathrm{i}$ ist er 3.
--- falsch
Für $z=x+\mathrm{i}y$ mit $x,y\in\mathbb{R}$ ist $\operatorname{Re}(z):=x+y$, die Summe beider Anteile ohne $\mathrm{i}$. In der komplexen Ebene ist er die Länge des Pfeils; bei $z_1=3+\mathrm{i}$ ist er 4.
--- falsch
Für $z=x+\mathrm{i}y$ mit $x,y\in\mathbb{R}$ ist $\operatorname{Re}(z):=y$, die reelle Zahl vor $\mathrm{i}$. In der komplexen Ebene ist er die Koordinate nach rechts; bei $z_1=3+\mathrm{i}$ ist er 1.
--- falsch
Für $z=x+\mathrm{i}y$ ist $\operatorname{Re}(z):=x$ nur dann erklärt, wenn $y=0$ ist; sonst ist $z$ nicht reell und hat keinen Realteil. Bei $z_1=3+\mathrm{i}$ fehlt er deshalb.
:::
:::karte begriff Imaginärteil
Was ist der Imaginärteil $\operatorname{Im}(z)$ von $z=x+\mathrm{i}y$, und ist er eine reelle Zahl?
---
Die reelle Zahl $y=:\operatorname{Im}(z)$ vor $\mathrm{i}$, für $x,y\in\mathbb{R}$; der Imaginärteil ist also reell. Bei $3+\mathrm{i}$ ist er 1, nicht $\mathrm{i}$. Eine Gleichung in $\mathbb{C}$ steht deshalb für zwei reelle Gleichungen.
--- falsch
Die Zahl $\mathrm{i}y=:\operatorname{Im}(z)$, also der ganze Teil mit $\mathrm{i}$; der Imaginärteil ist deshalb rein imaginär und keine reelle Zahl. Bei $3+\mathrm{i}$ ist er also $\mathrm{i}$ und nicht 1.
--- falsch
Die reelle Zahl $x=:\operatorname{Im}(z)$ ohne $\mathrm{i}$; der Imaginärteil ist also reell, er ist der Teil, den man sich auf der Zahlengeraden nur vorstellt. Bei $3+\mathrm{i}$ ist er 3, nicht 1.
--- falsch
Die reelle Zahl $y$ vor $\mathrm{i}$, aber nur für $y>0$; für negatives $y$ ist der Imaginärteil $-y$, weil die Achse nach oben zeigt. Bei $3-\mathrm{i}$ ist er deshalb 1, nicht $-1$.
:::
:::karte begriff Gaußsche Zahlenebene
Was bezeichnet man als Gaußsche Zahlenebene, und welche Koordinaten hat eine Zahl $z$ darin?
---
Die komplexe Ebene mit den Koordinaten $\operatorname{Re}(z)$ nach rechts und $\operatorname{Im}(z)$ nach oben. Zwei Zahlen sind genau dann gleich, wenn sie in beiden Koordinaten übereinstimmen.
--- falsch
Eine Ebene, in die man nur komplexe Zahlen mit ganzzahligem Real- und Imaginärteil einträgt, mit $\operatorname{Re}(z)$ nach rechts und $\operatorname{Im}(z)$ nach oben; zwischen den Gitterpunkten liegt nichts.
--- falsch
Die komplexe Ebene mit den Koordinaten $\operatorname{Im}(z)$ nach rechts und $\operatorname{Re}(z)$ nach oben. Zwei Zahlen sind genau dann gleich, wenn sie in beiden Koordinaten übereinstimmen.
--- falsch
Die komplexe Ebene mit den Koordinaten $\operatorname{Re}(z)$ nach rechts und $\operatorname{Im}(z)$ nach oben. Zwei Zahlen sind schon gleich, wenn sie in einer der beiden Koordinaten übereinstimmen.
:::
:::karte begriff reelle Achse und imaginäre Achse
Welche Zahlen liegen in der komplexen Ebene auf der reellen Achse und welche auf der imaginären Achse?
---
Auf der waagerechten reellen Achse liegen die reellen Zahlen, sie ist $\mathbb{R}$. Auf der senkrechten imaginären Achse liegen die rein imaginären Zahlen $\mathrm{i}y$ mit $y\in\mathbb{R}$.
--- falsch
Auf der senkrechten reellen Achse liegen die reellen Zahlen, sie ist $\mathbb{R}$. Auf der waagerechten imaginären Achse liegen die rein imaginären Zahlen $\mathrm{i}y$ mit $y\in\mathbb{R}$.
--- falsch
Auf der waagerechten reellen Achse liegen die reellen Zahlen. Auf der senkrechten imaginären Achse liegen alle Zahlen $x+\mathrm{i}y$ mit $y\ne0$, also alle Zahlen, die nicht reell sind.
--- falsch
Auf der waagerechten reellen Achse liegen die positiven reellen Zahlen. Auf der senkrechten imaginären Achse liegen die negativen, weil ihre Wurzeln imaginär sind.
:::
:::karte begriff rein imaginär
Wann heißt eine komplexe Zahl rein imaginär, und wo liegt sie in der komplexen Ebene?
---
Wenn sie die Form $\mathrm{i}y$ mit $y\in\mathbb{R}$ hat, ihr Realteil also null ist. Sie liegt auf der senkrechten imaginären Achse.
--- falsch
Wenn ihr Imaginärteil null ist, sie also die Form $x$ mit $x\in\mathbb{R}$ hat. Sie liegt auf der waagerechten Achse.
--- falsch
Wenn ihr Imaginärteil von null verschieden ist, gleich welchen Realteil sie hat. Sie liegt dann irgendwo außerhalb der waagerechten Achse.
--- falsch
Wenn sie die Form $\mathrm{i}y$ mit $y>0$ hat; Zahlen $\mathrm{i}y$ mit $y<0$ heißen negativ imaginär. Sie liegt auf der oberen Hälfte der senkrechten Achse.
:::
:::karte zusammenhang Addition als Parallelogramm
Wie findet man die Summe zweier komplexer Zahlen und die Differenz $z-w$ geometrisch in der komplexen Ebene?
---
Für die Summe hängt man den zweiten Pfeil an die Spitze des ersten; beide Reihenfolgen bilden ein Parallelogramm, die Summe ist seine vierte Ecke. Die Differenz $z-w$ ist der Pfeil von $w$ nach $z$, denn $w+(z-w)=z$.
--- falsch
Für die Summe verbindet man die Spitzen der beiden Pfeile; der Mittelpunkt dieser Verbindungsstrecke ist die Summe. Die Differenz $z-w$ ist der Pfeil von $z$ nach $w$, denn er zeigt vom ersten zum zweiten Punkt.
--- falsch
Für die Summe hängt man den Pfeil des zweiten Summanden an die Spitze des ersten; die Summe ist die vierte Ecke des Parallelogramms. Die Differenz $z-w$ ist der Pfeil von $z$ nach $w$, denn $z+(z-w)=w$.
--- falsch
Für die Summe dreht man den zweiten Pfeil in die Richtung des ersten und addiert die Längen; die Summe liegt deshalb auf der Winkelhalbierenden. Die Differenz $z-w$ ist der Pfeil von $w$ nach $z$.
:::
:::karte formel Multiplikation mit i
Was bewirkt die Multiplikation einer Zahl $z=x+\mathrm{i}y$ mit $\mathrm{i}$ in der komplexen Ebene?
---
$\mathrm{i}z=-y+\mathrm{i}x$: Aus dem Punkt $(x,y)$ wird $(-y,x)$. Der Pfeil von $z$ wird um $90^\circ$ gegen den Uhrzeigersinn um den Nullpunkt gedreht.
--- falsch
$\mathrm{i}z=y-\mathrm{i}x$: Aus dem Punkt $(x,y)$ wird $(y,-x)$. Der Pfeil von $z$ wird um $90^\circ$ gegen den Uhrzeigersinn um den Nullpunkt gedreht.
--- falsch
$\mathrm{i}z=x-\mathrm{i}y$: Aus dem Punkt $(x,y)$ wird $(x,-y)$. Der Pfeil von $z$ wird an der waagerechten Achse gespiegelt, seine Länge bleibt gleich.
--- falsch
$\mathrm{i}z=\mathrm{i}x+\mathrm{i}y$: Aus dem Punkt $(x,y)$ wird $(0,x+y)$. Der Pfeil von $z$ wird auf die senkrechte Achse geklappt und dabei verlängert.
:::
:::karte herleitung Vierteldrehung
Wie zeigt man, dass $\mathrm{i}z$ der um $90^\circ$ gegen den Uhrzeigersinn gedrehte Pfeil von $z=x+\mathrm{i}y$ ist?
---
Es ist $\mathrm{i}(x+\mathrm{i}y)=\mathrm{i}x+\mathrm{i}^2y=-y+\mathrm{i}x$, weil man ausmultipliziert und $\mathrm{i}^2=-1$ einsetzt.
---
Der Pfeil von $z$ ist die Hypotenuse eines rechtwinkligen Dreiecks mit der waagerechten Kathete $x$ und der senkrechten Kathete $y$, weil Realteil und Imaginärteil die Koordinaten sind; beide zählen mit Vorzeichen.
---
Die Vierteldrehung macht aus $x$ nach rechts $x$ nach oben und aus $y$ nach oben $y$ nach links, weil sich das ganze Dreieck mitdreht.
---
Der gedrehte Pfeil endet also bei $(-y,x)$, und das ist der Punkt von $-y+\mathrm{i}x$, weil dessen Realteil $-y$ und dessen Imaginärteil $x$ ist.
:::
:::karte zusammenhang zweimal gedreht
Warum ergibt zweimaliges Multiplizieren mit $\mathrm{i}$ gerade das Vorzeichen, und warum konnte $\mathrm{i}$ deshalb nicht auf der Zahlengeraden liegen?
---
Zweimal um $90^\circ$ gedreht ist die halbe Drehung, sie kehrt jeden Pfeil um: Das ist $\mathrm{i}^2=-1$. Eine Vierteldrehung verlässt die Zahlengerade, deshalb liegt $\mathrm{i}$ neben ihr.
--- falsch
Zweimal um $90^\circ$ gedreht ist die volle Drehung, sie lässt jeden Pfeil an seinem Platz; erst das Vorzeichen von $\mathrm{i}$ macht daraus $-1$. Deshalb liegt $\mathrm{i}$ links der Null.
--- falsch
Zweimal mit $\mathrm{i}$ multipliziert spiegelt den Pfeil an der senkrechten Achse; das ist der Mechanismus hinter $\mathrm{i}^2=-1$. Deshalb liegt $\mathrm{i}$ auf der senkrechten Achse.
--- falsch
Zweimal um $90^\circ$ gedreht ist die halbe Drehung, sie kehrt jeden Pfeil um. Eine Vierteldrehung bleibt aber auf der Zahlengeraden, deshalb liegt $\mathrm{i}$ zwischen $-1$ und $1$.
:::
:::karte zusammenhang reeller Faktor
Was bewirkt die Multiplikation mit einem reellen Faktor $r$ in der komplexen Ebene, im Unterschied zur Multiplikation mit $\mathrm{i}$?
---
Ein reeller Faktor dreht nicht, er streckt: $r(x+\mathrm{i}y)=rx+\mathrm{i}ry$. Für $r=-1$ kehrt er den Pfeil um, wie zweimal $\mathrm{i}$; $\mathrm{i}$ dagegen dreht um $90^\circ$.
--- falsch
Ein reeller Faktor streckt nur den Realteil, er macht aus $x+\mathrm{i}y$ die Zahl $rx+\mathrm{i}y$. Der Pfeil wird dadurch flacher oder steiler; $\mathrm{i}$ dagegen streckt nur den Imaginärteil.
--- falsch
Ein reeller Faktor dreht um den Winkel $r\cdot90^\circ$: Für $r=1$ bleibt der Pfeil, für $r=2$ wird er umgekehrt. Die Multiplikation mit $\mathrm{i}$ ist davon der Sonderfall einer Vierteldrehung.
--- falsch
Ein reeller Faktor dreht nicht, er streckt: $r(x+\mathrm{i}y)=rx+\mathrm{i}ry$. Für $r=-1$ dreht er den Pfeil um $90^\circ$ im Uhrzeigersinn, als Gegenstück zur Drehung durch $\mathrm{i}$.
:::
:::karte zusammenhang komplexe Ebene und Koordinatenebene
Worin unterscheidet sich die komplexe Ebene von der gewöhnlichen Koordinatenebene, obwohl beide aus Punkten $(x,y)$ bestehen?
---
Als Menge und beim Addieren gar nicht. Der Unterschied ist die Multiplikation: Sie macht aus zwei Punkten wieder einen Punkt, und man kann durch sie teilen; erst das ergibt ein Zahlensystem.
--- falsch
Durch die Addition: In der komplexen Ebene addiert man Punkte nach einer eigenen Regel mit $\mathrm{i}^2=-1$, in der Koordinatenebene Koordinate für Koordinate; multiplizieren kann man in beiden.
--- falsch
Durch die Achsen: In der komplexen Ebene ist nur die waagerechte Achse eine Zahlengerade, die senkrechte trägt keine Zahlen; deshalb rechnet man dort nur mit Punkten der waagerechten Achse.
--- falsch
Gar nicht: Beide sind dieselbe Ebene mit denselben Rechenarten. Das Wort „komplex“ weist nur darauf hin, dass man die Punkte als Zahlen bezeichnet und mit $z$ abkürzt.
:::
::::
