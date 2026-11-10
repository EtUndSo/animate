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
