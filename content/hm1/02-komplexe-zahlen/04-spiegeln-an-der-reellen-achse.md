---
title: Stufe 3: Spiegeln an der reellen Achse
pfad: Elektrotechnik / 1. Semester / Höhere Mathematik 1 / Komplexe Zahlen
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
