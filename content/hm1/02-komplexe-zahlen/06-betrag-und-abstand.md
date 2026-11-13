---
title: Stufe 5: Betrag und Abstand
pfad: Elektrotechnik / 1. Semester / HöMa1 – Höhere Mathematik 1 / Komplexe Zahlen
adresse: elektrotechnik/1-semester/hohere-mathematik-1/komplexe-zahlen
knoten: Kapitel 2: Komplexe Zahlen
order: 1220600
summary: Komplexe Zahlen lassen sich nicht ordnen, aber messen.
tags: Abstand, untere Dreiecksungleichung
lang: de
---

<span class="anker" id="stufe-5"></span>

:::zweck
Komplexe Zahlen lassen sich nicht ordnen, aber messen. Diese Stufe überträgt Abstand und Betrag aus [Kapitel 1](/wissen/elektrotechnik/1-semester/hohere-mathematik-1/mengen-logik-und-reelle-zahlen/mengen-logik-und-reelle-zahlen.html) in die Ebene und zeigt, welche Regeln erhalten bleiben.
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

⁠**So liest man das:** Unter der Wurzel steht eine reelle Zahl größer oder gleich null, und $\sqrt a$ ist die nicht negative Lösung von $b^2=a$ ([Kapitel 1](/wissen/elektrotechnik/1-semester/hohere-mathematik-1/mengen-logik-und-reelle-zahlen/mengen-logik-und-reelle-zahlen.html)). Der __Abstand__ $d(z,w)$ hängt nur von der Differenz ab: $d(z,w)=|z-w|$. **Grenzfall:** Für reelles $z$ ist $|z|=\sqrt{x^2}=|x|$, der Betrag aus [Kapitel 1](/wissen/elektrotechnik/1-semester/hohere-mathematik-1/mengen-logik-und-reelle-zahlen/mengen-logik-und-reelle-zahlen.html).

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

::::beispiel
$|z_1|=\sqrt{10}\approx3{,}162$ und $|z_2|=\sqrt5\approx2{,}236$. Die Dreiecksungleichung: $|z_1+z_2|=|4+3\mathrm{i}|=5\le5{,}398$. Das Produkt: $|z_1z_2|=|1+7\mathrm{i}|=\sqrt{50}=\sqrt{10}\cdot\sqrt5$. Der Abstand: $d(z_1,z_2)=|2-\mathrm{i}|=\sqrt5$. Die untere Ungleichung: $0{,}926\le2{,}236$. Regel (v) für $z_1$: $3\le3{,}162\le4$.
::::

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

::::formelsammlung
**Abstand und Betrag**

$$d(z,w):=\sqrt{(x-u)^2+(y-v)^2},\qquad|z|:=d(z,0)=\sqrt{x^2+y^2}$$

Für $z=x+\mathrm{i}y$ und $w=u+\mathrm{i}v$ mit reellen $x,y,u,v$; es gilt $d(z,w)=|z-w|$. Für reelles $z$ ist $|z|=|x|$.

**Nicht negativ und symmetrisch**

$$|z|\ge0,\qquad|z|=0\Leftrightarrow z=0,\qquad d(z,w)=d(w,z),\qquad|\overline{z}|=|{-z}|=|z|$$

Für alle $z,w\in\mathbb{C}$; ebenso $d(z,w)\ge0$ und $d(z,w)=0\Leftrightarrow z=w$.

**Betrag und konjugierte Zahl**

$$z\overline{z}=|z|^2,\qquad1/z=\overline{z}\cdot1/|z|^2$$

Der Kehrwert für $z\ne0$. Aus $|z|=1$ folgt $1/z=\overline{z}$.

**Betrag eines Produkts**

$$|z\cdot w|=|z|\cdot|w|$$

Für alle $z,w\in\mathbb{C}$: Der Betrag eines Produkts ist das Produkt der Beträge.

**Betrag, Realteil und Imaginärteil**

$$\max\{|\operatorname{Re}(z)|,|\operatorname{Im}(z)|\}\le|z|\le|\operatorname{Re}(z)|+|\operatorname{Im}(z)|$$

Jede Kathete ist höchstens so lang wie die Hypotenuse, die Hypotenuse höchstens so lang wie beide Katheten zusammen.

**Dreiecksungleichung**

$$|z+w|\le|z|+|w|,\qquad d(z,w)\le d(z,\tilde z)+d(\tilde z,w)$$

Für alle $z,w,\tilde z\in\mathbb{C}$: Ein Umweg über $\tilde z$ ist nie kürzer. Gleichheit tritt ein, wenn die Pfeile in dieselbe Richtung zeigen.

**Untere Dreiecksungleichung**

$$|z-w|\le|z|+|w|,\qquad\bigl||z|-|w|\bigr|\le|z-w|,\qquad\bigl||z|-|w|\bigr|\le|z+w|$$

Für alle $z,w\in\mathbb{C}$; die beiden rechten Ungleichungen schätzen nach unten ab.

**Betragsquadrat einer Summe**

$$|z\pm w|^2=|z|^2\pm2\operatorname{Re}(z\overline{w})+|w|^2$$

Addiert ergibt sich $|z+w|^2+|z-w|^2=2|z|^2+2|w|^2$: Die Quadrate der beiden Diagonalen eines Parallelogramms ergeben zusammen die Quadrate aller vier Seiten.

**Kreis und Kreisscheibe**

$$|z-c|=r,\qquad|z-c|\le r$$

Kreis um $c$ mit Radius $r$ bzw. Kreisscheibe, weil $|z-c|$ der Abstand von $z$ zu $c$ ist. Solche Ungleichungen sind erlaubt, weil beide Seiten reell sind.
::::

::::lernkarten
:::karte formel Abstand und Betrag
Wie sind der Abstand $d(z,w)$ und der Betrag $|z|$ für $z=x+\mathrm{i}y$ und $w=u+\mathrm{i}v$ definiert?
---
$d(z,w):=\sqrt{(x-u)^2+(y-v)^2}$ und $|z|:=d(z,0)=\sqrt{x^2+y^2}$, für reelle $x,y,u,v$. Beides sind Hypotenusen nach Pythagoras, also reelle Zahlen größer oder gleich null.
--- falsch
$d(z,w):=|x-u|+|y-v|$ und $|z|:=d(z,0)=|x|+|y|$, für reelle $x,y,u,v$. Man addiert die Wege entlang der beiden Achsen, wie auf einem Straßengitter mit rechtwinkligen Kreuzungen.
--- falsch
$d(z,w):=\sqrt{(x-u)^2-(y-v)^2}$ und $|z|:=d(z,0)=\sqrt{x^2-y^2}$, für reelle $x,y,u,v$. Das Minus unter der Wurzel kommt von $\mathrm{i}^2=-1$ im Imaginärteil.
--- falsch
$d(z,w):=\sqrt{(x-u)^2+(y-v)^2}$ und $|z|:=\sqrt{z^2}$, für reelle $x,y,u,v$. Der Betrag ist wie in $\mathbb{R}$ die Wurzel aus dem Quadrat der Zahl selbst.
:::
:::karte zusammenhang Betrag
Warum steht beim Betrag einer komplexen Zahl unter der Wurzel $x^2+y^2$ und nicht $z^2$, obwohl in $\mathbb{R}$ $|x|=\sqrt{x^2}$ gilt?
---
Weil $z^2$ in $\mathbb{C}$ im Allgemeinen nicht reell ist und negativ sein kann, etwa $(2\mathrm{i})^2=-4$. Der Betrag ist eine Länge, Pythagoras addiert Quadrate reeller Längen; richtig ist $|z|=\sqrt{z\overline{z}}$.
--- falsch
Es ist dasselbe: Für jedes $z$ gilt $z^2=x^2+y^2$, weil beim Quadrieren das Vorzeichen von $\mathrm{i}$ verschwindet. Man schreibt $x^2+y^2$ nur, um das $\mathrm{i}$ unter der Wurzel zu vermeiden.
--- falsch
Weil die Wurzel aus $z^2$ in $\mathbb{C}$ zwei Werte hätte, $z$ und $-z$. Mit $x^2+y^2$ wählt man unter beiden den Wert mit positivem Realteil aus, und der ist dann der Betrag.
--- falsch
Weil $z^2$ zu groß wäre: Es zählt Realteil und Imaginärteil doppelt, und $x^2+y^2$ ist genau die Hälfte davon. Die Wurzel daraus liefert dann die richtige Länge des Pfeils.
:::
:::karte zusammenhang Abstand
Warum ist der Abstand zweier komplexer Zahlen der Betrag ihrer Differenz, $d(z,w)=|z-w|$?
---
Weil $d(z,w)$ nur von den Differenzen $x-u$ und $y-v$ der Koordinaten abhängt, und das sind Realteil und Imaginärteil von $z-w$. Geometrisch ist $z-w$ der Pfeil von $w$ nach $z$, sein Betrag dessen Länge.
--- falsch
Weil der Abstand die Differenz der Beträge ist, $d(z,w)=|z|-|w|$; das ist dasselbe wie $|z-w|$, weil der Betrag mit der Subtraktion verträglich ist und man ihn in die Differenz hineinziehen darf.
--- falsch
Weil $d(z,w)$ nur von den Summen $x+u$ und $y+v$ der Koordinaten abhängt, und das sind Realteil und Imaginärteil von $z+w$. Deshalb gilt ebenso $d(z,w)=|z+w|$, beide Formeln sind gleichwertig.
--- falsch
Weil man Abstände nur auf der reellen Achse messen kann: Man projiziert $z$ und $w$ auf diese Achse und nimmt den Betrag der Differenz ihrer Realteile; der Imaginärteil fällt dabei weg.
:::
:::karte formel Betrag und konjugierte Zahl
Wie hängen Betrag und konjugierte Zahl zusammen, und was folgt daraus für den Kehrwert?
---
$z\overline{z}=|z|^2$, für $z\ne0$ also $1/z=\overline{z}\cdot1/|z|^2$: spiegeln und durch $|z|^2$ teilen. Außerdem haben $z$, $\overline{z}$ und $-z$ denselben Betrag: $|\overline{z}|=|{-z}|=|z|$.
--- falsch
$z\overline{z}=|z|$, für $z\ne0$ also $1/z=\overline{z}\cdot1/|z|$. Außerdem haben $z$ und $\overline{z}$ denselben Betrag, $-z$ dagegen den Betrag $-|z|$, weil der Pfeil umgekehrt ist.
--- falsch
$z\overline{z}=|z|^2$ gilt nur für reelle $z$, sonst ist $z\overline{z}$ nicht reell. Den Kehrwert bekommt man deshalb nur über die Paarformel und nicht über den Betrag.
--- falsch
$z+\overline{z}=|z|^2$, für $z\ne0$ also $1/z=\overline{z}\cdot1/|z|^2$. Außerdem haben $z$, $\overline{z}$ und $-z$ denselben Betrag, weil Spiegeln die Längen erhält.
:::
:::karte formel Betrag eines Produkts
Wie hängt der Betrag eines Produkts $zw$ mit den Beträgen der Faktoren zusammen, und wie begründet man das?
---
$|z\cdot w|=|z|\cdot|w|$. Denn $|zw|^2=zw\,\overline{zw}=z\overline{z}\,w\overline{w}=|z|^2|w|^2$ wegen $\overline{zw}=\overline{z}\,\overline{w}$; beide Beträge sind nicht negativ, man darf die Wurzel ziehen.
--- falsch
$|z\cdot w|=|z|+|w|$. Denn beim Multiplizieren addieren sich die Längen der Pfeile, so wie man bei der Addition die Pfeile aneinanderhängt und ihre Längen zusammenzählt.
--- falsch
$|z\cdot w|\le|z|\cdot|w|$, mit Gleichheit nur bei reellen Faktoren. Denn die Mischglieder mit $\mathrm{i}$ heben sich beim Multiplizieren teilweise auf und verkürzen dadurch den Pfeil.
--- falsch
$|z\cdot w|=|z|\cdot|w|$ nur für $\operatorname{Re}(z)\operatorname{Re}(w)\ge0$. Denn in den Realteil des Produkts geht $-y_1y_2$ ein, und dieser Anteil kann den Betrag des Produkts verkleinern.
:::
:::karte formel Betrag, Realteil und Imaginärteil
Wie lässt sich der Betrag $|z|$ durch $|\operatorname{Re}(z)|$ und $|\operatorname{Im}(z)|$ nach oben und nach unten abschätzen?
---
$\max\{|\operatorname{Re}(z)|,|\operatorname{Im}(z)|\}\le|z|\le|\operatorname{Re}(z)|+|\operatorname{Im}(z)|$: Jede Kathete ist höchstens so lang wie die Hypotenuse, und die Hypotenuse ist höchstens so lang wie beide Katheten zusammen.
--- falsch
$|\operatorname{Re}(z)|+|\operatorname{Im}(z)|\le|z|\le2\max\{|\operatorname{Re}(z)|,|\operatorname{Im}(z)|\}$: Die Hypotenuse ist mindestens so lang wie beide Katheten zusammen, aber höchstens doppelt so lang wie die längere.
--- falsch
$\min\{|\operatorname{Re}(z)|,|\operatorname{Im}(z)|\}\le|z|\le\max\{|\operatorname{Re}(z)|,|\operatorname{Im}(z)|\}$: Die Hypotenuse liegt in ihrer Länge immer zwischen der kürzeren und der längeren der beiden Katheten.
--- falsch
$|z|=|\operatorname{Re}(z)|+|\operatorname{Im}(z)|$: Die Hypotenuse ist genau so lang wie beide Katheten zusammen, weil man vom Nullpunkt erst waagerecht und dann senkrecht zum Punkt $z$ läuft.
:::
:::karte zusammenhang Dreiecksungleichung
Warum gilt die Dreiecksungleichung $|z+w|\le|z|+|w|$ auch für komplexe Zahlen, und wann tritt Gleichheit ein?
---
Weil $|z+w|^2=|z|^2+2\operatorname{Re}(z\overline{w})+|w|^2$ und $\operatorname{Re}(z\overline{w})\le|z||w|$ ist; geometrisch ist der Weg über $z$ ein Umweg. Gleichheit tritt ein, wenn die Pfeile in dieselbe Richtung zeigen.
--- falsch
Weil $|z+w|^2=|z|^2+|w|^2$ ist, und das ist höchstens $(|z|+|w|)^2$; geometrisch ist das der Satz des Pythagoras. Gleichheit tritt ein, wenn die beiden Pfeile senkrecht aufeinander stehen.
--- falsch
Weil $|z+w|^2=|z|^2+2\operatorname{Re}(z\overline{w})+|w|^2$ und $\operatorname{Re}(z\overline{w})\le|z||w|$ ist; geometrisch ist der Weg über $z$ ein Umweg. Gleichheit tritt ein, wenn die Pfeile in entgegengesetzte Richtungen zeigen.
--- falsch
Weil man die Dreiecksungleichung aus $\mathbb{R}$ getrennt auf Realteil und Imaginärteil anwendet und die Ergebnisse addiert. Gleichheit tritt nur ein, wenn $z$ und $w$ beide reell sind.
:::
:::karte herleitung Dreiecksungleichung
Wie zeigt man $|z+w|\le|z|+|w|$ für komplexe Zahlen $z$, $w$ mithilfe der Konjugation?
---
$|z+w|^2=(z+w)(\overline{z}+\overline{w})$, weil das Betragsquadrat das Produkt mit der konjugierten Zahl ist und die Konjugation in Summen hineingezogen werden darf.
---
Ausmultipliziert ist das $|z|^2+z\overline{w}+\overline{z}w+|w|^2=|z|^2+2\operatorname{Re}(z\overline{w})+|w|^2$, weil $\overline{z}w$ die zu $z\overline{w}$ konjugierte Zahl ist und eine Zahl plus ihre konjugierte den doppelten Realteil ergibt.
---
Es gilt $\operatorname{Re}(z\overline{w})\le|z\overline{w}|=|z||w|$, weil der Realteil höchstens so groß ist wie der Betrag und der Betrag eines Produkts das Produkt der Beträge ist.
---
Also gilt $|z+w|^2\le(|z|+|w|)^2$, und die Behauptung folgt, weil beide Seiten nicht negativ sind und man die Wurzel ziehen darf.
---
Die Abstandsform $d(z,w)\le d(z,\tilde z)+d(\tilde z,w)$ folgt, weil $z-w=(z-\tilde z)+(\tilde z-w)$ ist und der Abstand der Betrag der Differenz ist.
:::
:::karte zusammenhang untere Dreiecksungleichung
Was schätzt die untere Dreiecksungleichung bei komplexen Zahlen ab, und woraus folgt sie?
---
Sie schätzt $|z-w|$ und $|z+w|$ nach unten ab: $\bigl||z|-|w|\bigr|\le|z-w|$ und $\bigl||z|-|w|\bigr|\le|z+w|$. Sie folgt allein aus der Dreiecksungleichung, etwa über $|z|=|(z-w)+w|\le|z-w|+|w|$.
--- falsch
Sie schätzt $|z+w|$ nach oben ab: $|z+w|\le\bigl||z|-|w|\bigr|$. Sie folgt daraus, dass sich Pfeile mit verschiedener Richtung beim Addieren teilweise aufheben, so dass die Summe kürzer wird.
--- falsch
Sie schätzt $|z-w|$ nach unten ab, $|z|-|w|\le|z-w|$, aber nur für $|z|\ge|w|$. Den Fall $|z|<|w|$ gibt es in $\mathbb{C}$ nicht, weil man komplexe Zahlen nicht der Größe nach vergleichen kann.
--- falsch
Sie gibt $|z-w|$ exakt an: $|z-w|=\bigl||z|-|w|\bigr|$. In $\mathbb{R}$ war das nur eine Abschätzung, in $\mathbb{C}$ wird daraus eine Gleichung, weil man die Pfeile vor dem Subtrahieren ausrichten kann.
:::
:::karte zusammenhang Punktmengen
Welche Punktmengen der komplexen Ebene beschreiben $|z-c|=r$ und $|z-c|\le r$, und warum darf man hier eine Ungleichung schreiben?
---
$|z-c|=r$ ist der Kreis um $c$ mit Radius $r$, $|z-c|\le r$ die Kreisscheibe, denn $|z-c|$ ist der Abstand von $z$ zu $c$. Die Ungleichung ist erlaubt, weil beide Seiten reell sind.
--- falsch
$|z-c|=r$ ist die Gerade durch $c$ mit der Steigung $r$, $|z-c|\le r$ die Halbebene unter ihr. Die Ungleichung ist erlaubt, weil $c$ und $r$ fest gewählt sind und sich nicht ändern.
--- falsch
$|z-c|=r$ ist der Kreis um $-c$ mit Radius $r$, $|z-c|\le r$ das Äußere dieses Kreises. Die Ungleichung ist erlaubt, weil beide Seiten reell sind und sich deshalb vergleichen lassen.
--- falsch
$|z-c|=r$ ist der Kreis um $c$ mit Radius $r$, $|z-c|\le r$ die Kreisscheibe. Die Ungleichung ist erlaubt, weil $z-c$ für Punkte der Kreisscheibe immer eine reelle Zahl ist.
:::
:::karte zusammenhang Einheitskreis
Was gilt für den Kehrwert einer komplexen Zahl $z$ mit $|z|=1$, und warum?
---
Dann ist $1/z=\overline{z}$, denn aus $z\overline{z}=|z|^2=1$ folgt das direkt. Der Kehrwert ist dann nur das Spiegelbild an der reellen Achse, etwa für $z=0{,}6+0{,}8\mathrm{i}$.
--- falsch
Dann ist $1/z=z$, denn aus $|z|=1$ folgt $z=1$: Die einzige komplexe Zahl mit dem Betrag 1 ist die Eins selbst, und sie ist ihr eigener Kehrwert.
--- falsch
Dann ist $1/z=-z$, denn der Kehrwert spiegelt am Nullpunkt, und bei Betrag 1 ändert sich die Länge des Pfeils dabei nicht; nur die Richtung kehrt sich um.
--- falsch
Dann ist $1/z=\overline{z}$ nur für reelle $z$, also für $z=\pm1$. Für andere Zahlen mit $|z|=1$ muss man das Spiegelbild zusätzlich durch $x^2-y^2$ teilen.
:::
:::karte zusammenhang Diagonalen des Parallelogramms
Was sagt die Gleichung $|z+w|^2+|z-w|^2=2|z|^2+2|w|^2$ über ein Parallelogramm, und warum gilt sie?
---
Die Quadrate der beiden Diagonalen ergeben zusammen die Quadrate aller vier Seiten. Sie gilt, weil $|z\pm w|^2=|z|^2\pm2\operatorname{Re}(z\overline{w})+|w|^2$ ist und sich beim Addieren die Mischglieder aufheben.
--- falsch
Die beiden Diagonalen eines Parallelogramms sind immer gleich lang. Sie gilt, weil $|z+w|=|z-w|$ für alle $z$ und $w$ ist; beide Seiten der Gleichung sind deshalb doppelt so groß.
--- falsch
Die Summe der beiden Diagonalen ist doppelt so lang wie die Summe zweier Seiten. Sie gilt ebenso ohne Quadrate, $|z+w|+|z-w|=2|z|+2|w|$, weil sich Längen addieren.
--- falsch
Die Quadrate der beiden Diagonalen ergeben zusammen die Quadrate aller vier Seiten, aber nur bei einem Rechteck. Sonst bleiben die Mischglieder $\pm2\operatorname{Re}(z\overline{w})$ stehen.
:::
::::
