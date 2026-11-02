---
title: Stufe 5: Betrag und Abstand
pfad: Elektrotechnik / 1. Semester / Höhere Mathematik 1 / Komplexe Zahlen
order: 1220600
summary: Komplexe Zahlen lassen sich nicht ordnen, aber messen.
tags: Abstand, untere Dreiecksungleichung
lang: de
---

<span class="anker" id="stufe-5"></span>

:::zweck
Komplexe Zahlen lassen sich nicht ordnen, aber messen. Diese Stufe überträgt Abstand und Betrag aus [Teil 1](/wissen/elektrotechnik/1-semester/hohere-mathematik-1/mengen-logik-und-reelle-zahlen/mengen-logik-und-reelle-zahlen.html) in die Ebene und zeigt, welche Regeln erhalten bleiben.
:::

**Die Idee.** In $\mathbb{R}$ misst $|x|$ den Abstand zum Nullpunkt. In der Ebene übernimmt das der Satz des Pythagoras: Die Strecke von 0 nach $z$ ist die Hypotenuse eines rechtwinkligen Dreiecks mit den Katheten $|x|$ und $|y|$ (Abb. [5](#abb-5), links). Der Abstand zweier Punkte ist die Hypotenuse über den Differenzen ihrer Koordinaten. Das Ergebnis ist reell, hier ist „größer“ wieder erlaubt.

:::abbildung hm1/k2betrag 5
Links Betrag und Abstand als Hypotenusen: $|z_1|^2=3^2+1^2$ und $d(z_1,z_2)^2=2^2+1^2$. Rechts die Dreiecksungleichung: Der Weg über $z_1$ ist länger als der direkte Weg zu $z_1+z_2$.
:::

:::definition Definition 5.1 (Abstand und Betrag)
<span class="anker" id="satz-5-1"></span>

Für $z=x+\mathrm{i}y$ und $w=u+\mathrm{i}v$ mit reellen $x,y,u,v$ sei

<span class="anker" id="gl-5-1"></span>
$$d(z,w):=\sqrt{(x-u)^2+(y-v)^2},\qquad |z|:=d(z,0)=\sqrt{x^2+y^2}. \tag{5.1}$$
:::

⁠**So liest man das:** Unter der Wurzel steht eine reelle Zahl größer oder gleich null, und $\sqrt a$ ist die nicht negative Lösung von $b^2=a$ ([Teil 1](/wissen/elektrotechnik/1-semester/hohere-mathematik-1/mengen-logik-und-reelle-zahlen/mengen-logik-und-reelle-zahlen.html)). Der __Abstand__ $d(z,w)$ hängt nur von der Differenz ab: $d(z,w)=|z-w|$. **Grenzfall:** Für reelles $z$ ist $|z|=\sqrt{x^2}=|x|$, der Betrag aus [Teil 1](/wissen/elektrotechnik/1-semester/hohere-mathematik-1/mengen-logik-und-reelle-zahlen/mengen-logik-und-reelle-zahlen.html).

:::satz Satz 5.2 (Rechenregeln für Betrag und Abstand)
<span class="anker" id="satz-5-2"></span>

Für alle $z,w,\tilde z\in\mathbb{C}$ gilt:

<ol class="rm">

<li>

$|z|\ge0$ und ($|z|=0\Leftrightarrow z=0$), ebenso $d(z,w)\ge0$ und ($d(z,w)=0\Leftrightarrow z=w$),

</li>

<li>

$d(z,w)=d(w,z)$ und $|\overline{z}|=|{-z}|=|z|$,

</li>

<li>

$z\overline{z}=|z|^2$, für $z\ne0$ also $1/z=\overline{z}\cdot1/|z|^2$,

</li>

<li>

$|z\cdot w|=|z|\cdot|w|$,

</li>

<li>

$\max\{|\operatorname{Re}(z)|,|\operatorname{Im}(z)|\}\le|z|\le|\operatorname{Re}(z)|+|\operatorname{Im}(z)|$,

</li>

<li>

$|z+w|\le|z|+|w|$ und $d(z,w)\le d(z,\tilde z)+d(\tilde z,w)$ (Dreiecksungleichung),

</li>

<li>

$|z-w|\le|z|+|w|$, $\bigl||z|-|w|\bigr|\le|z-w|$ und $\bigl||z|-|w|\bigr|\le|z+w|$ (__untere Dreiecksungleichung__).

</li>

</ol>
:::

⁠**So liest man das:** (iv): Der Betrag eines Produkts ist das Produkt der Beträge. (v): Die Hypotenuse ist höchstens so lang wie beide Katheten zusammen, und jede Kathete ist höchstens so lang wie sie. (vi): Ein Umweg über $\tilde z$ ist nie kürzer. **Gültigkeit:** Die Regeln gelten ohne Einschränkung, aber $|z+w|=|z|+|w|$ ist keine Regel: Gleichheit tritt ein, wenn die Pfeile in dieselbe Richtung zeigen, wie bei $z_2$ und $2z_2$: $3\sqrt5=\sqrt5+2\sqrt5$.

:::beweis Rechenregeln für den Betrag
(i), (ii): Eine Summe von Quadraten ist genau dann null, wenn beide Quadrate null sind, und Vorzeichenwechsel ändern sie nicht.

(iii): Stufe [3](spiegeln-an-der-reellen-achse.html#stufe-3), Regel (vi), und [(4.1)](dividieren-und-was-verloren-geht.html#gl-4-1).

(iv): $|zw|^2=zw\,\overline{zw}=z\overline{z}\,w\overline{w}=|z|^2|w|^2$ nach (iii) und $\overline{zw}=\overline{z}\,\overline{w}$. Beide Beträge sind nicht negativ, man darf die Wurzel ziehen.

(v): $x^2\le x^2+y^2$ und $y^2\le x^2+y^2$ geben die linke Ungleichung, $x^2+y^2\le x^2+2|x||y|+y^2=(|x|+|y|)^2$ die rechte.

(vi): Mit (iii) und den Konjugationsregeln ist

$$|z+w|^2=(z+w)(\overline{z}+\overline{w})=|z|^2+z\overline{w}+\overline{z}w+|w|^2=|z|^2+2\operatorname{Re}(z\overline{w})+|w|^2,$$

denn $\overline{z}w$ ist die zu $z\overline{w}$ konjugierte Zahl. Nach (v) und (iv) ist $\operatorname{Re}(z\overline{w})\le|z\overline{w}|=|z||w|$. Also gilt $|z+w|^2\le(|z|+|w|)^2$. Die Abstandsform folgt aus $z-w=(z-\tilde z)+(\tilde z-w)$.

(vii): $-w$ statt $w$ in (vi) gibt die erste Ungleichung. Aus $|z|=|(z-w)+w|\le|z-w|+|w|$ folgt $|z|-|w|\le|z-w|$, mit vertauschten Rollen $|w|-|z|\le|z-w|$, zusammen die zweite. $-w$ statt $w$ darin gibt die dritte.
:::

**Beispiel.** $|z_1|=\sqrt{10}\approx3{,}162$ und $|z_2|=\sqrt5\approx2{,}236$. Die Dreiecksungleichung: $|z_1+z_2|=|4+3\mathrm{i}|=5\le5{,}398$. Das Produkt: $|z_1z_2|=|1+7\mathrm{i}|=\sqrt{50}=\sqrt{10}\cdot\sqrt5$. Der Abstand: $d(z_1,z_2)=|2-\mathrm{i}|=\sqrt5$. Die untere Ungleichung: $0{,}926\le2{,}236$. Regel (v) für $z_1$: $3\le3{,}162\le4$.

**Punktmengen.** Weil $|z-c|$ der Abstand von $z$ zu $c$ ist, beschreibt $|z-c|=r$ den Kreis um $c$ mit Radius $r$ und $|z-c|\le r$ die Kreisscheibe. Bedingungen an $\operatorname{Re}(z)$ oder $\operatorname{Im}(z)$ schneiden Halbebenen aus. Solche Ungleichungen sind erlaubt, weil beide Seiten reell sind.

:::frage Warum steht unter der Wurzel $x^2+y^2$ und nicht $z^2$?
Für reelles $z$ ist $|z|=\sqrt{z^2}$, das verleitet. In $\mathbb{C}$ ist $z^2$ im Allgemeinen nicht reell und kann negativ sein, zum Beispiel $(2\mathrm{i})^2=-4$. Der Betrag soll eine Länge sein, und Pythagoras addiert Quadrate reeller Längen. Richtig ist $|z|=\sqrt{z\overline{z}}$.
:::

:::aufgabe Aufgabe 6 ★★ Punktmengen
<span class="anker" id="aufg-6"></span>

Skizziere in der komplexen Ebene: (a) $\{z:|z-1-\mathrm{i}|\le2\}$, (b) $\{z:|z-2|=|z+2\mathrm{i}|\}$, (c) $\{z:\operatorname{Re}((1+\mathrm{i})z)>1\}$. Tipp zu (b): Beide Seiten quadrieren und $z=x+\mathrm{i}y$ einsetzen.

:::loesung
(a) $|z-(1+\mathrm{i})|\le2$ ist die Kreisscheibe um $1+\mathrm{i}$ mit Radius 2, einschließlich des Randes.

(b) $(x-2)^2+y^2=x^2+(y+2)^2$ gibt $-4x+4=4y+4$, also $y=-x$. Das ist die Gerade durch den Nullpunkt mit Steigung $-1$. Geometrisch sind es alle Punkte, die von $2$ und $-2\mathrm{i}$ gleich weit entfernt sind: die Mittelsenkrechte der Verbindungsstrecke.

(c) $(1+\mathrm{i})(x+\mathrm{i}y)=(x-y)+\mathrm{i}(x+y)$. Die Bedingung lautet $x-y>1$, also $y<x-1$. Das ist die Halbebene unterhalb der Geraden $y=x-1$, ohne die Gerade.
:::
:::

:::aufgabe Aufgabe 7 ★★★ Parallelogramm und Einheitskreis
<span class="anker" id="aufg-7"></span>

(a) Zeige $|z+w|^2+|z-w|^2=2|z|^2+2|w|^2$ und prüfe die Gleichung mit $z_1$ und $z_2$. Was sagt sie über die Diagonalen des Parallelogramms? (b) Zeige: Aus $|z|=1$ folgt $1/z=\overline{z}$. Prüfe das mit $z=0{,}6+0{,}8\mathrm{i}$. (c) Sage vorher, wo $1/(2z)$ für dieses $z$ liegt, und rechne nach.

:::loesung
(a) Wie im Beweis der Dreiecksungleichung ist $|z\pm w|^2=|z|^2\pm2\operatorname{Re}(z\overline{w})+|w|^2$. Beim Addieren fallen die Mischglieder weg. Probe: $25+5=30=2\cdot10+2\cdot5$. Die Quadrate der beiden Diagonalen eines Parallelogramms ergeben zusammen die Quadrate aller vier Seiten.

(b) Aus $z\overline{z}=|z|^2=1$ folgt $1/z=\overline{z}$. Für $z=0{,}6+0{,}8\mathrm{i}$ ist $|z|^2=0{,}36+0{,}64=1$ und $(0{,}6+0{,}8\mathrm{i})(0{,}6-0{,}8\mathrm{i})=0{,}36+0{,}64=1$.

(c) Vorhersage: Spiegeln und durch $|2z|^2=4$ teilen, also liegt der Kehrwert auf dem Pfeil von $\overline{z}$ beim Betrag $0{,}5$. Rechnung: $1/(2z)=\overline{z}/2=0{,}3-0{,}4\mathrm{i}$.
:::
:::
