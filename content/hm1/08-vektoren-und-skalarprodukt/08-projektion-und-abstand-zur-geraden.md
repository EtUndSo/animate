---
title: Stufe 6: Projektion und Abstand zur Geraden
pfad: Elektrotechnik / 1. Semester / HöMa1 – Höhere Mathematik 1 / Vektoren und Skalarprodukt
adresse: elektrotechnik/1-semester/hohere-mathematik-1/vektoren-und-skalarprodukt
knoten: Kapitel 8: Vektoren und Skalarprodukt
order: 1280800
summary: Wie weit ist ein Punkt von einer Geraden entfernt?
tags: Abstand, Lotfußpunkt, Lot, Orthogonalprojektion
lang: de
---

<span class="anker" id="stufe-6"></span>

:::zweck
Wie weit ist ein Punkt von einer Geraden entfernt? Die Gerade hat unendlich viele Punkte. Diese Stufe zeigt, dass einer genügt: der Fußpunkt des Lots.
:::

**Die Idee.** Sei $Q$ der Punkt und $g$ die Gerade. Man sucht $R$ auf $g$ so, dass der Rest $\vec u=\vec q-\vec r$ senkrecht auf der Richtung $\vec v$ steht. Das liefert zwei Dinge. Erstens legt $\langle\vec u,\vec v\rangle=0$ die Lage von $R$ fest, denn die Gleichung ist in der Unbekannten linear. Zweitens ist $R$ der nächste Punkt: Zu jedem anderen Punkt der Geraden ist der Weg die Hypotenuse eines rechtwinkligen Dreiecks mit Kathete $\vec u$, also länger (Abb. [7](#abb-7)).

:::satz Satz 6.1 (Abstand Punkt zu Gerade)
<span class="anker" id="satz-6-1"></span>

Sei $Q\in\mathbb{R}^n$ mit $\vec q=\overrightarrow{OQ}$ und $g:\ \vec x=\vec p+t\vec v$ ($t\in\mathbb{R}$) eine Gerade mit $\vec v\ne\vec0$. Der __Abstand__ $\operatorname{dist}(Q,g):=\min_{\vec r\in g}\|\vec q-\vec r\|$ wird genau in $\vec r=\vec p+\alpha\vec v$ mit

<span class="anker" id="gl-6-1"></span>
$$\alpha=\frac{\langle\vec q-\vec p,\vec v\rangle}{\|\vec v\|^2} \tag{6.1}$$

angenommen, und dort gilt $\vec q-\vec r\perp\vec v$ sowie

<span class="anker" id="gl-6-2"></span>
$$\operatorname{dist}(Q,g)=\|\vec q-\vec r\|=\Bigl\|\vec q-\vec p-\frac{\langle\vec q-\vec p,\vec v\rangle}{\|\vec v\|^2}\cdot\vec v\Bigr\|. \tag{6.2}$$
:::

⁠**So liest man das:** $\vec r$ heißt __Lotfußpunkt__, $\vec u=\vec q-\vec r$ steht als __Lot__ senkrecht auf $g$. Die Zahl $\alpha$ sagt, wie viele Schritte $\vec v$ man von $P$ aus bis zu $R$ geht. Dass $\vec v\ne\vec0$ ist, braucht man, um durch $\|\vec v\|^2$ zu teilen.

:::herleitung Die Bedingung legt $\alpha$ fest
Mit $\vec u=\vec q-\vec r$ und $\vec r=\vec p+\alpha\vec v$ lautet die Bedingung $\langle\vec q-(\vec p+\alpha\vec v),\vec v\rangle=0$. Linearität im ersten Eingang gibt $\langle\vec q-\vec p,\vec v\rangle-\alpha\langle\vec v,\vec v\rangle=0$. Wegen $\langle\vec v,\vec v\rangle=\|\vec v\|^2\ne0$ folgt [(6.1)](#gl-6-1).
:::

:::beweis $R$ ist der nächste Punkt
Sei $\vec z=\vec p+t\vec v$ ein beliebiger Punkt von $g$. Dann ist $\vec q-\vec z=\vec u+(\alpha-t)\vec v$, und $\vec u\perp(\alpha-t)\vec v$. Pythagoras [(5.2)](skalarprodukt-norm-abstand.html#gl-5-2) gibt

$$\|\vec q-\vec z\|^2=\|\vec u\|^2+(\alpha-t)^2\|\vec v\|^2\ge\|\vec u\|^2.$$

Gleichheit steht genau für $t=\alpha$, denn $\|\vec v\|\ne0$.
:::

:::abbildung hm1/k8projektion 7
Links der Abstand von $Q=(2,6)$ zur Geraden $(0,2)+t\,\vec a$. Der Lotfußpunkt ist $R=(3,3)$, das Lot $\vec u=(-1,3)$ steht senkrecht auf $\vec a$. Der Weg zu $P=(0,2)$ ist die Hypotenuse, also länger. Rechts die Orthogonalprojektion von $\vec b$ auf $\vec a$: $\vec b$ zerfällt in $\frac12\vec a=(1{,}5;\ 0{,}5)$ und den Rest $(-0{,}5;\ 1{,}5)$.
:::

::::beispiel
Für $\vec p=(0,2)$, $\vec v=\vec a$, $\vec q=(2,6)$ ist $\vec q-\vec p=(2,4)$, also $\alpha=\frac{6+4}{10}=1$, $\vec r=(3,3)$ und $\vec u=(-1,3)$. Probe: $\langle\vec u,\vec a\rangle=-3+3=0$. Der Abstand ist $\sqrt{10}=3{,}162$. Der Punkt $P$ selbst liegt weiter weg, $\|\vec q-\vec p\|^2=20=10+10$, genau wie im Beweis mit $t=0$.
::::

⁠**Grenzfälle:** Liegt $Q$ auf $g$, ist $\vec u=\vec0$ und der Abstand 0. Ersetzt man $\vec v$ durch $c\vec v$ mit $c\ne0$, wird $\alpha$ zu $\alpha/c$, und $\vec r$ bleibt derselbe Punkt.

**Orthogonalprojektion.** Für $\vec p=\vec0$ geht die Gerade durch $O$ und ist der Unterraum $\operatorname{span}\{\vec v\}$.

:::definition Definition 6.2 (Orthogonalprojektion)
<span class="anker" id="satz-6-2"></span>

Für $\vec v\ne\vec0$ heißt

<span class="anker" id="gl-6-3"></span>
$$\vec r=\alpha\cdot\vec v=\frac{\langle\vec q,\vec v\rangle}{\|\vec v\|^2}\cdot\vec v=\Bigl\langle\vec q,\frac{\vec v}{\|\vec v\|}\Bigr\rangle\frac{\vec v}{\|\vec v\|}=:\operatorname{Proj}_{\vec v}(\vec q) \tag{6.3}$$

__Orthogonalprojektion__ von $\vec q$ auf den linearen Unterraum $U:=\operatorname{span}\{\vec v\}$. Es gilt $\bigl(\vec q-\operatorname{Proj}_{\vec v}(\vec q)\bigr)\perp\vec v$.
:::

⁠**So liest man das:** $\vec v/\|\vec v\|$ ist die Richtung mit Länge 1, $\langle\vec q,\vec v/\|\vec v\|\rangle$ der Anteil von $\vec q$ in dieser Richtung. Für $\vec q=\vec b$, $\vec v=\vec a$ ist $\operatorname{Proj}_{\vec a}(\vec b)=\frac5{10}\vec a=(1{,}5;\ 0{,}5)$, der Rest $(-0{,}5;\ 1{,}5)$ steht senkrecht auf $\vec a$. Für $\vec q=(2,-3)$ ist $\operatorname{Proj}_{\vec e_1}(\vec q)=2\vec e_1$ und $\operatorname{Proj}_{\vec e_2}(\vec q)=-3\vec e_2$. Die Summe gibt $\vec q$ zurück: Hier ist $\vec q=\sum_{j=1}^2\langle\vec q,\vec e_j\rangle\vec e_j$. Die Komponenten eines Vektors sind also seine Skalarprodukte mit den Einheitsvektoren. In der Elektrotechnik kehrt das als Arbeit wieder: $W=\langle\vec F,\vec s\rangle$ zählt von der Kraft nur den Anteil längs des Wegs.

:::frage Warum steht in [(6.1)](#gl-6-1) $\|\vec v\|^2$ und nicht $\|\vec v\|$?
Ein Faktor $\|\vec v\|$ macht aus $\vec v$ die Richtung mit Länge 1, das gibt den Anteil von $\vec q-\vec p$ längs der Geraden. Der zweite rechnet diesen Anteil in Schritte der Länge $\|\vec v\|$ um.
:::

:::aufgabe Aufgabe 7 ★★ Abstand im Raum
<span class="anker" id="aufg-7"></span>

Gegeben sind $g:\ (1,0,1)+t(1,2,2)$ und $Q=(5,5,3)$.

<ol class="al">

<li>

Bestimme $\alpha$, den Lotfußpunkt, das Lot und $\operatorname{dist}(Q,g)$. Prüfe die Orthogonalität.

</li>

<li>

Prüfe die Formel aus dem Beweis für $t=0$.

</li>

<li>

Sage vorher, was sich ändert, wenn man den Richtungsvektor durch $(3,6,6)$ ersetzt.

</li>

<li>

Berechne $\operatorname{Proj}_{\vec v}(\vec q)$ für $\vec v=(1,2,2)$, $\vec q=(5,5,3)$ und zeige allgemein $\operatorname{Proj}_{\vec v}(\operatorname{Proj}_{\vec v}(\vec q))=\operatorname{Proj}_{\vec v}(\vec q)$.

</li>

</ol>

:::loesung
(a) $\vec q-\vec p=(4,5,2)$, $\alpha=\frac{4+10+4}9=2$, $\vec r=(3,4,5)$, $\vec u=(2,1,-2)$, $\operatorname{dist}(Q,g)=3$. Probe: $2+2-4=0$. (b) $\|\vec q-\vec p\|^2=16+25+4=45=9+2^2\cdot9$. (c) $\alpha$ wird $\frac23$, der Lotfußpunkt und der Abstand bleiben. (d) $\operatorname{Proj}_{\vec v}(\vec q)=\frac{21}9(1,2,2)=(\frac73,\frac{14}3,\frac{14}3)$, der Rest $(\frac83,\frac13,-\frac53)$ steht senkrecht auf $\vec v$. Allgemein: $\vec s:=\operatorname{Proj}_{\vec v}(\vec q)=\lambda\vec v$ gibt $\operatorname{Proj}_{\vec v}(\vec s)=\frac{\lambda\|\vec v\|^2}{\|\vec v\|^2}\vec v=\vec s$. Ein Punkt, der schon auf der Geraden liegt, bleibt liegen.
:::
:::
