---
title: Stufe 3: Spiegeln an der reellen Achse
pfad: Elektrotechnik / 1. Semester / HöMa1 – Höhere Mathematik 1 / Komplexe Zahlen
adresse: elektrotechnik/1-semester/hohere-mathematik-1/komplexe-zahlen
knoten: Kapitel 2: Komplexe Zahlen
order: 1220400
summary: Durch x+iy lässt sich noch nicht teilen.
tags: 
lang: de
---

<span class="anker" id="stufe-3"></span>

:::zweck
Durch $x+\mathrm{i}y$ lässt sich noch nicht teilen. Diese Stufe führt das Spiegelbild von $z$ ein, das aus jeder Zahl durch Multiplikation eine reelle macht, und sammelt die Rechenregeln.
:::

**Die Idee.** Auch $-\mathrm{i}$ löst $x^2=-1$, denn $(-\mathrm{i})^2=\mathrm{i}^2=-1$. Die Rechengesetze können $\mathrm{i}$ und $-\mathrm{i}$ nicht unterscheiden. Tauscht man in einer richtigen Rechnung überall $\mathrm{i}$ gegen $-\mathrm{i}$, bleibt sie deshalb richtig. In der Ebene ist dieser Tausch die Spiegelung an der reellen Achse (Abb. [3](#abb-3)). Multipliziert man $z$ mit seinem Spiegelbild, heben sich die Mischglieder mit $\mathrm{i}$ auf.

:::abbildung hm1/k2konjugiert 3
$z_1$ und sein Spiegelbild $\overline{z_1}$. Die Summe liegt auf der reellen Achse, weil sich die Imaginärteile aufheben, die Differenz auf der imaginären Achse, weil sich die Realteile aufheben.
:::

:::definition Definition 3.1 (Konjugiert komplexe Zahl)
<span class="anker" id="satz-3-1"></span>

Zu $z=x+\mathrm{i}y$ heißt $\overline{z}:=x-\mathrm{i}y\in\mathbb{C}$ die zu $z$ konjugierte Zahl.
:::

:::satz Satz 3.2 (Rechenregeln in $\mathbb{C}$)
<span class="anker" id="satz-3-2"></span>

Für alle $z=x+\mathrm{i}y$ und $w=u+\mathrm{i}v$ mit reellen $x,y,u,v$ gilt:

<ol class="rm">

<li>

$\operatorname{Re}(z+w)=\operatorname{Re}(z)+\operatorname{Re}(w)$,

</li>

<li>

$\operatorname{Im}(z+w)=\operatorname{Im}(z)+\operatorname{Im}(w)$,

</li>

<li>

$\overline{z+w}=\overline{z}+\overline{w}$,

</li>

<li>

$\overline{z\cdot w}=\overline{z}\cdot\overline{w}$,

</li>

<li>

$\overline{\overline{z}}=z$,

</li>

<li>

$z\overline{z}=x^2+y^2$, also $\operatorname{Im}(z\overline{z})=0$ und $\operatorname{Re}(z\overline{z})=x^2+y^2$,

</li>

<li>

$z+\overline{z}=2\operatorname{Re}(z)$ und $z-\overline{z}=2\mathrm{i}\operatorname{Im}(z)$.

</li>

</ol>
:::

⁠**So liest man das:** Realteil, Imaginärteil und Konjugation dürfen in Summen hineingezogen werden. Die Konjugation darf auch in Produkte hinein, das ist der Tausch $\mathrm{i}\leftrightarrow-\mathrm{i}$. Der Realteil darf das nicht: $\operatorname{Re}(z_1z_2)=1$, aber $\operatorname{Re}(z_1)\operatorname{Re}(z_2)=3$, denn in den Realteil des Produkts geht auch $-y_1y_2$ ein. In der Elektrotechnik schreibt man statt $\overline{z}$ oft $z^*$.

:::beweis Rechenregeln
(i), (ii): Die Addition läuft getrennt, $z+w=(x+u)+\mathrm{i}(y+v)$.

(iii): $\overline{z+w}=(x+u)-\mathrm{i}(y+v)=(x-\mathrm{i}y)+(u-\mathrm{i}v)$.

(iv): Nach [(1.3)](paare-statt-einzelner-zahlen.html#gl-1-3) ist $zw=(xu-yv)+\mathrm{i}(xv+uy)$, also $\overline{zw}=(xu-yv)-\mathrm{i}(xv+uy)$. Dieselbe Formel mit $-y$ und $-v$ gibt $\overline{z}\,\overline{w}=(xu-yv)+\mathrm{i}(-xv-uy)$. Beide stimmen überein.

(v): Zweimal das Vorzeichen von $y$ wechseln.

(vi): $(x+\mathrm{i}y)(x-\mathrm{i}y)=x^2-\mathrm{i}xy+\mathrm{i}xy-\mathrm{i}^2y^2=x^2+y^2$.

(vii): $(x+\mathrm{i}y)+(x-\mathrm{i}y)=2x$ und $(x+\mathrm{i}y)-(x-\mathrm{i}y)=2\mathrm{i}y$.
:::

::::beispiel
Für $z_1$ ist $\overline{z_1}=3-\mathrm{i}$, $z_1\overline{z_1}=9+1=10$, $z_1+\overline{z_1}=6=2\cdot3$ und $z_1-\overline{z_1}=2\mathrm{i}=2\mathrm{i}\cdot1$. Probe zu (iv): $\overline{z_1z_2}=1-7\mathrm{i}$ und $\overline{z_1}\,\overline{z_2}=(3-\mathrm{i})(1-2\mathrm{i})=3-6\mathrm{i}-\mathrm{i}+2\mathrm{i}^2=1-7\mathrm{i}$.
::::

⁠**Grenzfall:** Für $y=0$ ist $\overline{z}=z$ und $z\overline{z}=x^2$. Reelle Zahlen liegen auf der Spiegelachse und ändern sich nicht.

:::frage Ist $z\overline{z}$ nicht dasselbe wie $z^2$?
Nur für reelle $z$. Bei $z^2$ addieren sich die Mischglieder zu $2\mathrm{i}xy$, bei $z\overline{z}$ heben sie sich auf. Im Rechenmodell ist $z_2^2=-3+4\mathrm{i}$, aber $z_2\overline{z_2}=5$.
:::

:::aufgabe Aufgabe 3 ★ Reell oder rein imaginär?
<span class="anker" id="aufg-3"></span>

Sei $z=2-5\mathrm{i}$. (a) Sage ohne Rechnung vorher, welche der Zahlen $z+\overline{z}$, $z-\overline{z}$, $z\overline{z}$, $z^2+\overline{z}^2$, $(z-\overline{z})^2$ reell und welche rein imaginär ist. Rechne dann nach. (b) Zeige für jedes $z\in\mathbb{C}$: $z$ ist genau dann reell, wenn $\overline{z}=z$, und genau dann rein imaginär, wenn $\overline{z}=-z$.

:::loesung
(a) Vorhersage: $z+\overline{z}$ ist reell, $z-\overline{z}$ rein imaginär, $z\overline{z}$ reell, $z^2+\overline{z}^2=z^2+\overline{z^2}$ reell (Summe einer Zahl und ihres Spiegelbilds), $(z-\overline{z})^2$ reell (Quadrat einer rein imaginären Zahl). Rechnung: $z+\overline{z}=4$, $z-\overline{z}=-10\mathrm{i}$, $z\overline{z}=4+25=29$. Mit $z^2=4-20\mathrm{i}+25\mathrm{i}^2=-21-20\mathrm{i}$ ist $z^2+\overline{z}^2=-42$, und $(z-\overline{z})^2=(-10\mathrm{i})^2=-100$.

(b) Nach Regel (vii) aus Stufe [3](#stufe-3) ist $\overline{z}=z$ gleichwertig mit $2\mathrm{i}\operatorname{Im}(z)=0$, also mit $\operatorname{Im}(z)=0$. Ebenso ist $\overline{z}=-z$ gleichwertig mit $2\operatorname{Re}(z)=0$, also mit $\operatorname{Re}(z)=0$.
:::
:::

::::formelsammlung
**Konjugierte Zahl**

$$\overline{z}:=x-\mathrm{i}y$$

Für $z=x+\mathrm{i}y$ mit $x,y\in\mathbb{R}$: das Spiegelbild von $z$ an der reellen Achse, in der Elektrotechnik oft $z^*$. Der Tausch von $\mathrm{i}$ gegen $-\mathrm{i}$ lässt jede richtige Rechnung richtig.

**Realteil und Imaginärteil einer Summe**

$$\operatorname{Re}(z+w)=\operatorname{Re}(z)+\operatorname{Re}(w),\qquad\operatorname{Im}(z+w)=\operatorname{Im}(z)+\operatorname{Im}(w)$$

Für alle $z,w\in\mathbb{C}$. Für Produkte gilt das nicht: In den Realteil des Produkts geht auch $-y_1y_2$ ein.

**Konjugation von Summe und Produkt**

$$\overline{z+w}=\overline{z}+\overline{w},\qquad\overline{z\cdot w}=\overline{z}\cdot\overline{w},\qquad\overline{\overline{z}}=z$$

Für alle $z,w\in\mathbb{C}$; die Konjugation darf in Summen und Produkte hineingezogen werden.

**Produkt mit der konjugierten Zahl**

$$z\overline{z}=x^2+y^2$$

Für $z=x+\mathrm{i}y$ mit $x,y\in\mathbb{R}$; also $\operatorname{Im}(z\overline{z})=0$ und $\operatorname{Re}(z\overline{z})=x^2+y^2$. Nur für reelle $z$ gleich $z^2$.

**Realteil und Imaginärteil über die konjugierte Zahl**

$$z+\overline{z}=2\operatorname{Re}(z),\qquad z-\overline{z}=2\mathrm{i}\operatorname{Im}(z)$$

Daraus: $z$ ist genau dann reell, wenn $\overline{z}=z$, und genau dann rein imaginär, wenn $\overline{z}=-z$.
::::

::::lernkarten
:::karte begriff konjugiert komplexe Zahl
Wie ist die zu $z=x+\mathrm{i}y$ konjugierte Zahl $\overline{z}$ definiert, und was bedeutet sie in der komplexen Ebene?
---
Für $z=x+\mathrm{i}y$ mit $x,y\in\mathbb{R}$ ist $\overline{z}:=x-\mathrm{i}y$. In der Ebene ist $\overline{z}$ das Spiegelbild von $z$ an der reellen Achse; in der Elektrotechnik schreibt man oft $z^*$.
--- falsch
Für $z=x+\mathrm{i}y$ mit $x,y\in\mathbb{R}$ ist $\overline{z}:=-x+\mathrm{i}y$. In der Ebene ist $\overline{z}$ das Spiegelbild von $z$ an der imaginären Achse; in der Elektrotechnik schreibt man oft $z^*$.
--- falsch
Für $z=x+\mathrm{i}y$ mit $x,y\in\mathbb{R}$ ist $\overline{z}:=-x-\mathrm{i}y$. In der Ebene ist $\overline{z}$ das Spiegelbild von $z$ am Nullpunkt, also der umgekehrte Pfeil; man schreibt dafür auch $z^*$.
--- falsch
Für $z=x+\mathrm{i}y$ mit $x,y\in\mathbb{R}$ ist $\overline{z}:=y+\mathrm{i}x$. In der Ebene entsteht $\overline{z}$, indem man Realteil und Imaginärteil vertauscht, also an der Winkelhalbierenden spiegelt.
:::
:::karte zusammenhang Spiegeln an der reellen Achse
Warum bleibt eine richtige Rechnung richtig, wenn man darin überall $\mathrm{i}$ durch $-\mathrm{i}$ ersetzt?
---
Weil auch $-\mathrm{i}$ die Gleichung $x^2=-1$ löst, $(-\mathrm{i})^2=\mathrm{i}^2=-1$; die Rechengesetze können $\mathrm{i}$ und $-\mathrm{i}$ nicht unterscheiden. In der Ebene ist der Tausch die Spiegelung an der reellen Achse.
--- falsch
Weil $\mathrm{i}$ und $-\mathrm{i}$ dieselbe Zahl sind: Das Vorzeichen vor $\mathrm{i}$ hat keine Bedeutung, weil $\mathrm{i}$ selbst schon das Vorzeichen $-1$ in sich trägt und jedes weitere Minus darin einfach aufgeht.
--- falsch
Sie bleibt nur bei Summen richtig. Bei Produkten ändert der Tausch das Ergebnis, weil $(-\mathrm{i})^2=+1$ ist und die Grundregel $\mathrm{i}^2=-1$ nach dem Tausch nicht mehr erfüllt wäre.
--- falsch
Weil der Tausch einer Drehung um $90^\circ$ entspricht, die alle Abstände und Winkel erhält. Die Ergebnisse werden dabei nur mitgedreht und bleiben deshalb richtig, wenn man sie zurückdreht.
:::
:::karte formel Rechenregeln der Konjugation
Welche Regeln gelten für das Konjugieren von Summen und Produkten und für doppeltes Konjugieren?
---
Für alle $z,w\in\mathbb{C}$: $\overline{z+w}=\overline{z}+\overline{w}$, $\overline{z\cdot w}=\overline{z}\cdot\overline{w}$ und $\overline{\overline{z}}=z$. Die Konjugation darf in Summen und in Produkte hineingezogen werden.
--- falsch
Für alle $z,w\in\mathbb{C}$: $\overline{z+w}=\overline{z}+\overline{w}$, aber $\overline{z\cdot w}=z\cdot\overline{w}$, und $\overline{\overline{z}}=-z$. Die Konjugation darf nur in Summen hineingezogen werden, in Produkte trifft sie einen Faktor.
--- falsch
Für alle $z,w\in\mathbb{C}$: $\overline{z+w}=\overline{z}-\overline{w}$, $\overline{z\cdot w}=\overline{z}\cdot\overline{w}$ und $\overline{\overline{z}}=z$. Beim Konjugieren einer Summe wechselt das Rechenzeichen zwischen den Summanden.
--- falsch
Für alle $z,w\in\mathbb{C}$: $\overline{z+w}=\overline{z}+\overline{w}$ und $\overline{\overline{z}}=z$. Für Produkte gilt keine solche Regel, weil sich $\mathrm{i}$ und $-\mathrm{i}$ beim Multiplizieren nicht vertauschen lassen.
:::
:::karte zusammenhang Realteil eines Produkts
Warum darf man den Realteil in eine Summe hineinziehen, aber nicht in ein Produkt?
---
Die Addition läuft getrennt je Koordinate, also gilt $\operatorname{Re}(z+w)=\operatorname{Re}(z)+\operatorname{Re}(w)$. In den Realteil des Produkts geht nach der Produktformel aber auch $-y_1y_2$ ein: $\operatorname{Re}(z_1z_2)=1$, aber $\operatorname{Re}(z_1)\operatorname{Re}(z_2)=3$.
--- falsch
Man darf es doch: Der Realteil verträgt sich wie die Konjugation mit Summen und Produkten, also gilt auch $\operatorname{Re}(zw)=\operatorname{Re}(z)\operatorname{Re}(w)$ für alle $z$ und $w$; nur der Imaginärteil stört.
--- falsch
Weil beim Produkt die Realteile addiert werden: Nach der Produktformel ist der Realteil von $zw$ gleich $\operatorname{Re}(z)+\operatorname{Re}(w)$, während die Imaginärteile miteinander multipliziert werden.
--- falsch
Weil der Realteil eines Produkts null ist, sobald beide Faktoren nicht reell sind: Das Produkt zweier nicht reeller Zahlen ist stets rein imaginär, sein Realteil hängt von nichts ab.
:::
:::karte formel Produkt mit der konjugierten Zahl
Was ergibt das Produkt $z\overline{z}$ für $z=x+\mathrm{i}y$, und warum ist es reell?
---
$z\overline{z}=x^2+y^2$, also $\operatorname{Im}(z\overline{z})=0$. Beim Ausmultiplizieren heben sich die Mischglieder $-\mathrm{i}xy$ und $\mathrm{i}xy$ auf, und $-\mathrm{i}^2y^2$ ist $+y^2$.
--- falsch
$z\overline{z}=x^2-y^2$, also $\operatorname{Im}(z\overline{z})=0$. Beim Ausmultiplizieren heben sich die Mischglieder auf, und nach der dritten binomischen Formel bleibt die Differenz der beiden Quadrate stehen.
--- falsch
$z\overline{z}=x^2+y^2+2\mathrm{i}xy$. Reell ist das nur, wenn $x=0$ oder $y=0$ gilt, weil sich die beiden Mischglieder beim Ausmultiplizieren zu $2\mathrm{i}xy$ addieren, statt sich aufzuheben.
--- falsch
$z\overline{z}=(x+y)^2$, also $\operatorname{Im}(z\overline{z})=0$. Beim Ausmultiplizieren verdoppeln sich die Mischglieder, und $\mathrm{i}$ fällt heraus, weil $\mathrm{i}\cdot(-\mathrm{i})=1$ ist.
:::
:::karte zusammenhang Unterschied zum Quadrat
Warum ist $z\overline{z}$ im Allgemeinen nicht dasselbe wie $z^2$?
---
Bei $z^2$ addieren sich die Mischglieder zu $2\mathrm{i}xy$, bei $z\overline{z}$ heben sie sich auf. Gleich sind beide nur für reelle $z$; im Rechenmodell ist $z_2^2=-3+4\mathrm{i}$, aber $z_2\overline{z_2}=5$.
--- falsch
Es ist dasselbe: $\overline{z}$ unterscheidet sich von $z$ nur im Vorzeichen eines Teils, und beim Quadrieren fallen Vorzeichen ohnehin weg. Deshalb gilt $z\overline{z}=z^2$ für jedes $z$.
--- falsch
Weil $z^2$ immer reell und nicht negativ ist, $z\overline{z}$ dagegen im Allgemeinen einen Imaginärteil hat. Gleich sind beide nur für rein imaginäre $z$, weil dann der Realteil fehlt.
--- falsch
Bei $z^2$ heben sich die Mischglieder auf, bei $z\overline{z}$ addieren sie sich zu $2\mathrm{i}xy$. Gleich sind beide nur für rein imaginäre $z$, denn dann ergeben beide $-y^2$.
:::
:::karte formel Realteil und Imaginärteil über die konjugierte Zahl
Wie gewinnt man Realteil und Imaginärteil einer Zahl $z$ aus $z$ und $\overline{z}$ zurück?
---
Aus $z+\overline{z}=2\operatorname{Re}(z)$ und $z-\overline{z}=2\mathrm{i}\operatorname{Im}(z)$: Die Summe liegt auf der reellen Achse, weil sich die Imaginärteile aufheben, die Differenz auf der imaginären Achse.
--- falsch
Aus $z+\overline{z}=2\operatorname{Re}(z)$ und $z-\overline{z}=2\operatorname{Im}(z)$. Summe und Differenz liegen beide auf der reellen Achse, weil sich der Faktor $\mathrm{i}$ jeweils heraushebt und nur reelle Anteile übrig bleiben.
--- falsch
Aus $z+\overline{z}=\operatorname{Re}(z)$ und $z-\overline{z}=\mathrm{i}\operatorname{Im}(z)$. Die Summe ist der Realteil selbst, weil das Spiegelbild denselben Realteil hat und dieser nicht doppelt gezählt wird.
--- falsch
Aus $z+\overline{z}=2\mathrm{i}\operatorname{Im}(z)$ und $z-\overline{z}=2\operatorname{Re}(z)$. Die Summe liegt auf der imaginären Achse, weil sich die Realteile aufheben, die Differenz auf der reellen Achse.
:::
:::karte zusammenhang reell oder rein imaginär
Woran erkennt man mithilfe der Konjugation, ob eine Zahl $z$ reell oder rein imaginär ist?
---
$z$ ist genau dann reell, wenn $\overline{z}=z$, und genau dann rein imaginär, wenn $\overline{z}=-z$. Denn $z-\overline{z}=2\mathrm{i}\operatorname{Im}(z)$ und $z+\overline{z}=2\operatorname{Re}(z)$.
--- falsch
$z$ ist genau dann reell, wenn $\overline{z}=-z$, und genau dann rein imaginär, wenn $\overline{z}=z$. Denn beim Spiegeln an der reellen Achse wechselt der Realteil sein Vorzeichen.
--- falsch
$z$ ist genau dann reell, wenn $z\overline{z}$ reell ist, und genau dann rein imaginär, wenn $z\overline{z}$ negativ ist. Denn das Produkt zeigt das Vorzeichen von $\mathrm{i}^2$.
--- falsch
$z$ ist genau dann reell, wenn $\overline{z}=z$. Für rein imaginäre Zahlen gibt es kein solches Kennzeichen, weil ihr Spiegelbild auf der reellen Achse liegt.
:::
:::karte herleitung Konjugation eines Produkts
Wie zeigt man mit der Produktformel, dass $\overline{z\cdot w}=\overline{z}\cdot\overline{w}$ für $z=x+\mathrm{i}y$ und $w=u+\mathrm{i}v$ gilt?
---
Es ist $zw=(xu-yv)+\mathrm{i}(xv+uy)$, weil man ausmultipliziert und $\mathrm{i}^2=-1$ einsetzt.
---
Also ist $\overline{zw}=(xu-yv)-\mathrm{i}(xv+uy)$, weil Konjugieren nur das Vorzeichen des Imaginärteils wechselt.
---
Dieselbe Formel mit $-y$ und $-v$ gibt $\overline{z}\,\overline{w}=(xu-yv)+\mathrm{i}(-xv-uy)$, weil $\overline{z}=x-\mathrm{i}y$ und $\overline{w}=u-\mathrm{i}v$ die Imaginärteile $-y$ und $-v$ haben.
---
Beide Ergebnisse stimmen überein, weil $(-y)(-v)=yv$ den Realteil nicht ändert und der Imaginärteil in beiden Fällen $-(xv+uy)$ ist.
:::
::::
