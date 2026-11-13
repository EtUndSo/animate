---
title: Stufe 8: Abstand und Betrag
pfad: Elektrotechnik / 1. Semester / HöMa1 – Höhere Mathematik 1 / Mengen, Logik und reelle Zahlen
adresse: elektrotechnik/1-semester/hohere-mathematik-1/mengen-logik-und-reelle-zahlen
knoten: Kapitel 1: Mengen, Logik und reelle Zahlen
order: 1211000
summary: Grenzwerte messen, wie nah zwei Zahlen beieinanderliegen.
tags: Abstand, Absolutbetrag, Dreiecksungleichung, untere Dreiecksungleichung
lang: de
---

<span class="anker" id="stufe-8"></span>

:::zweck
Grenzwerte messen, wie nah zwei Zahlen beieinanderliegen. Dafür braucht man den Abstand und eine Regel für Umwege.
:::

**Die Idee.** Der Abstand zweier Zahlen ist die Länge der Strecke zwischen ihnen auf der Geraden. Die Länge hängt nicht von der Richtung ab, und ein Umweg über einen dritten Punkt ist nie kürzer (Abb. [8](#abb-8)). Der Betrag ist der Abstand von der Null.

:::definition Definition 8.1 (Abstand und Betrag)
<span class="anker" id="satz-8-1"></span>

Für $x,y\in\mathbb{R}$ heißen

<span class="anker" id="gl-8-1"></span>
$$d(x,y):=\begin{cases}x-y,&x\ge y\\y-x,&x<y\end{cases}\qquad\text{und}\qquad|x|:=d(x,0)=\begin{cases}x,&x\ge0\\-x,&x<0\end{cases} \tag{8.1}$$

__Abstand__ von $x$ und $y$ und __Absolutbetrag__ von $x$.
:::

⁠**So liest man das:** $d$ wie englisch distance. Aus der Definition folgt

<span class="anker" id="gl-8-2"></span>
$$d(x,y)=d(x-y,0)=|x-y|,\ \ -|x|\le x\le|x|,\ \ |x|=\max\{x,-x\},\ \ -|x|=\min\{x,-x\}. \tag{8.2}$$

Im Rechenmodell ist $|x|=3$, $|y|=5$ und $d(x,y)=|{-3}-5|=8$. Das Minuszeichen in [(8.1)](#gl-8-1) täuscht: Für $x<0$ ist $-x$ positiv, der Betrag ist nie negativ. Werte mit Toleranz schreibt man so: $|U-5\,\mathrm V|\le0{,}1\,\mathrm V$ heißt, $U$ liegt zwischen 4,9 V und 5,1 V.

:::satz Satz 8.2 (Eigenschaften von Abstand und Betrag)
<span class="anker" id="satz-8-2"></span>

Für alle $x,y,z\in\mathbb{R}$ gilt:

|  | Abstand | Betrag |
|---|---|---|
| positiv | $d(x,y)\ge0$ | $\vert x\vert \ge0$ |
| definit | $d(x,y)=0\Leftrightarrow x=y$ | $\vert x\vert =0\Leftrightarrow x=0$ |
| symmetrisch, Produkt | $d(x,y)=d(y,x)$ | $\vert xy\vert =\vert x\vert \vert y\vert $; für $z\ne0$: $\vert x/z\vert =\vert x\vert /\vert z\vert $ |
| __Dreiecksungleichung__ | $d(x,y)\le d(x,z)+d(z,y)$ | $\vert x+y\vert \le\vert x\vert +\vert y\vert $ |

Außerdem gilt $|x-y|\le|x|+|y|$, die __untere Dreiecksungleichung__ $\bigl||x|-|y|\bigr|\le|x\pm y|$ und $|x|=\sqrt{x^2}$.
:::

⁠**So liest man das:** Die Dreiecksungleichung schätzt eine Summe nach oben ab, die untere nach unten.

:::frage Warum gilt nicht $|x+y|=|x|+|y|$?
Das stimmt nur bei gleichen Vorzeichen oder wenn ein Summand null ist. Bei verschiedenen Vorzeichen heben sich die Summanden teilweise auf: $|-3+5|=2<8$. Im schlimmsten Fall addieren sich zwei Fehler, das sagt die Ungleichung.
:::

:::abbildung hm1/k1betrag 8
Rechenmodell $x=-3$, $y=5$. Direkt ist $d(x,y)=8$. Der Umweg über $z=7$ ergibt $10+2=12$. Für jedes $z$ zwischen $x$ und $y$, etwa $z=1$, ergibt er genau 8 ($4+4$).
:::

:::beweis Dreiecksungleichung und Folgerungen
Definitheit und Symmetrie stehen in [(8.1)](#gl-8-1). *Dreiecksungleichung für $d$.* Ohne Beschränkung der Allgemeinheit (kurz o. B. d. A.: die übrigen Fälle gehen durch Umbenennen in diesen über) sei $x<y$; für $x=y$ steht links 0. Für $z=x$ oder $z=y$ ist ein Summand 0, die Ungleichung eine Gleichung. Es bleiben drei Fälle. $x<y<z$: $d(x,z)+d(z,y)=2z-x-y>2y-x-y=y-x$. $x<z<y$: Die Summe ist genau $y-x$. $z<x<y$: Die Summe ist $x+y-2z>x+y-2x=y-x$.

⁠*Produkt.* Ist $xy=0$, sind nach Satz [3.2](korperaxiome.html#satz-3-2) (v) beide Seiten 0. Für $xy>0$ haben $x$, $y$ nach Satz [4.2](anordnungsaxiome.html#satz-4-2) (c) gleiche Vorzeichen, und $|x||y|$ ist $xy$ oder $(-x)(-y)$, beides $xy$. $xy<0$ geht ebenso. Für den Quotienten: $z\cdot\frac xz=x$ gibt $|z|\,|\frac xz|=|x|$.

⁠*Betrag.* $|x+y|=|x-(-y)|=d(x,-y)\le d(x,0)+d(0,-y)=|x|+|y|$, denn $|-y|=|y|$. Mit $-y$ statt $y$ folgt $|x-y|\le|x|+|y|$.

⁠*Untere Dreiecksungleichung.* $|x|=|(x-y)+y|\le|x-y|+|y|$, also $|x|-|y|\le|x-y|$. Durch Tauschen von $x$ und $y$ auch $|y|-|x|\le|x-y|$. Nach [(8.2)](#gl-8-2) ist das Maximum der beiden $\bigl||x|-|y|\bigr|$. Mit $-y$ statt $y$ folgt die Variante mit $+$.

⁠*Wurzel.* $|x|\ge0$ und $|x|^2=x^2$, also ist $|x|$ die eindeutige nicht negative Lösung von $z^2=x^2$.
:::

::::beispiel
Mit $x=-3$, $y=5$: $|x+y|=2\le8=|x|+|y|$ und $\bigl||x|-|y|\bigr|=2\le|x+y|=2$.
::::

⁠**Grenzfall** $y=0$: Alle Ungleichungen werden zu $|x|=|x|$.

:::aufgabe Aufgabe 9 ★★ Betragsungleichungen
<span class="anker" id="aufg-9"></span>

<ol class="al">

<li>

Beschreibe $\{x\in\mathbb{R}:|x-2|\le3\}$ als Intervall.

</li>

<li>

Löse $|x-2|+|x+1|\le5$ durch Fallunterscheidung an den Stellen $x=-1$ und $x=2$.

</li>

<li>

Zwei Spannungen erfüllen $|U_1-5\,\mathrm V|\le0{,}1\,\mathrm V$, $|U_2-3\,\mathrm V|\le0{,}2\,\mathrm V$. Wie weit kann $U_1+U_2$ höchstens von 8 V abweichen? Gib ein Paar an, das den Wert erreicht.

</li>

</ol>

:::loesung
(a) $-3\le x-2\le3$, also $[-1,5]$. (b) Für $x\ge2$: $2x-1\le5$, also $2\le x\le3$. Für $-1\le x<2$: $(2-x)+(x+1)=3\le5$, immer wahr. Für $x<-1$: $1-2x\le5$, also $-2\le x<-1$. Zusammen: $[-2,3]$. (c) $|(U_1+U_2)-8\,\mathrm V|\le|U_1-5\,\mathrm V|+|U_2-3\,\mathrm V|\le0{,}3\,\mathrm V$. Erreicht bei $U_1=5{,}1\,\mathrm V$, $U_2=3{,}2\,\mathrm V$.
:::
:::

::::formelsammlung
**Abstand und Absolutbetrag**

$$d(x,y):=\begin{cases}x-y,&x\ge y\\y-x,&x<y\end{cases}\qquad|x|:=d(x,0)=\begin{cases}x,&x\ge0\\-x,&x<0\end{cases}$$

Für $x,y\in\mathbb{R}$. Der Betrag ist der Abstand von der Null und nie negativ.

**Folgerungen aus der Definition**

$$d(x,y)=d(x-y,0)=|x-y|,\ \ -|x|\le x\le|x|,\ \ |x|=\max\{x,-x\},\ \ -|x|=\min\{x,-x\}$$

Für alle $x,y\in\mathbb{R}$.

**Positiv, definit, symmetrisch**

$$d(x,y)\ge0,\qquad d(x,y)=0\Leftrightarrow x=y,\qquad d(x,y)=d(y,x)$$

Für den Betrag: $|x|\ge0$ und $|x|=0\Leftrightarrow x=0$.

**Betrag von Produkt und Quotient**

$$|xy|=|x||y|,\qquad|x/z|=|x|/|z|$$

Der Quotient für $z\ne0$.

**Dreiecksungleichung**

$$d(x,y)\le d(x,z)+d(z,y),\qquad|x+y|\le|x|+|y|$$

Ein Umweg über einen dritten Punkt ist nie kürzer. Sie schätzt eine Summe nach oben ab; Gleichheit beim Betrag nur bei gleichen Vorzeichen oder wenn ein Summand null ist.

**Untere Dreiecksungleichung und Wurzel**

$$|x-y|\le|x|+|y|,\qquad\bigl||x|-|y|\bigr|\le|x\pm y|,\qquad|x|=\sqrt{x^2}$$

Die untere Dreiecksungleichung schätzt nach unten ab.
::::

::::lernkarten
:::karte begriff Abstand
Wie ist der Abstand $d(x,y)$ zweier reeller Zahlen definiert?
---
Durch $d(x,y)=x-y$ für $x\ge y$ und $d(x,y)=y-x$ für $x<y$: die Länge der Strecke zwischen $x$ und $y$ auf der Zahlengeraden. Es gilt $d(x,y)=|x-y|$.
--- falsch
Durch $d(x,y)=x-y$ für alle $x,y$: die gerichtete Länge der Strecke von $y$ nach $x$. Für $x<y$ ist der Abstand deshalb negativ, für $x>y$ positiv.
--- falsch
Durch $d(x,y)=x+y$ für $x\ge y$ und $d(x,y)=y+x$ für $x<y$: die Summe der Entfernungen beider Zahlen von der Null auf der Zahlengeraden.
--- falsch
Durch $d(x,y)=x-y$ für $x<y$ und $d(x,y)=y-x$ für $x\ge y$: die Länge der Strecke zwischen $x$ und $y$ auf der Zahlengeraden. Es gilt $d(x,y)=|x-y|$.
:::
:::karte begriff Absolutbetrag
Wie ist der Absolutbetrag $|x|$ einer reellen Zahl definiert?
---
Als Abstand von der Null: $|x|:=d(x,0)$, also $|x|=x$ für $x\ge0$ und $|x|=-x$ für $x<0$.
--- falsch
Als Abstand von der Eins: $|x|:=d(x,1)$, also $|x|=x-1$ für $x\ge1$ und $|x|=1-x$ für $x<1$.
--- falsch
Als Quadrat der Zahl: $|x|:=x^2$, also immer nicht negativ; für $x=-3$ ist zum Beispiel $|x|=9$.
--- falsch
Als Abstand von der Null: $|x|:=d(x,0)$, also $|x|=-x$ für $x\ge0$ und $|x|=x$ für $x<0$.
:::
:::karte begriff Betrag
Was misst der Betrag einer reellen Zahl, und warum ist er nie negativ, obwohl in seiner Definition $-x$ vorkommt?
---
Den Abstand der Zahl von der Null. Das Minuszeichen täuscht: $-x$ steht nur für $x<0$, und dann ist $-x$ positiv, für $x=-3$ etwa $|x|=3$.
--- falsch
Den Abstand der Zahl von der Null. Er kann negativ sein, wenn die Zahl negativ ist: Für $x<0$ ist $|x|=-x$, und das Minuszeichen zeigt genau das an.
--- falsch
Die Anzahl der Stellen der Zahl vor dem Komma. Er ist nie negativ, weil man Stellen nur zählen kann; das Minus in der Definition betrifft nur das Vorzeichen.
--- falsch
Den Abstand der Zahl von der Eins. Er ist nie negativ, weil man bei negativen Zahlen zuerst 1 addiert und danach das Vorzeichen streicht.
:::
:::karte formel Abstand über Betrag
Welche Beziehungen zwischen Abstand, Betrag, Maximum und Minimum folgen direkt aus der Definition des Betrags?
---
Für alle $x,y\in\mathbb{R}$ gilt $d(x,y)=d(x-y,0)=|x-y|$, $-|x|\le x\le|x|$, $|x|=\max\{x,-x\}$ und $-|x|=\min\{x,-x\}$: Der Abstand ist der Betrag der Differenz.
--- falsch
Für alle $x,y\in\mathbb{R}$ gilt $d(x,y)=|x|-|y|$, $|x|\le x\le-|x|$, $|x|=\min\{x,-x\}$ und $-|x|=\max\{x,-x\}$: Der Abstand ist die Differenz der Beträge.
--- falsch
Für alle $x,y\in\mathbb{R}$ gilt $d(x,y)=|x+y|$, $-|x|\le x\le|x|$, $|x|=\max\{x,-x\}$ und $-|x|=\min\{x,-x\}$: Der Abstand ist der Betrag der Summe.
--- falsch
Für alle $x,y\in\mathbb{R}$ gilt $d(x,y)=d(x-y,0)=|x-y|$, $x\le-|x|\le|x|$, $|x|=\max\{x,0\}$ und $-|x|=\min\{x,0\}$: Der Betrag ist nie kleiner als null.
:::
:::karte formel Dreiecksungleichung
Wie lautet die Dreiecksungleichung für den Abstand und für den Betrag?
---
$d(x,y)\le d(x,z)+d(z,y)$: Ein Umweg über $z$ ist nie kürzer als der direkte Weg. Für den Betrag: $|x+y|\le|x|+|y|$; sie schätzt eine Summe nach oben ab.
--- falsch
$d(x,y)\ge d(x,z)+d(z,y)$: Der direkte Weg ist nie kürzer als ein Umweg über $z$. Für den Betrag: $|x+y|\ge|x|+|y|$; sie schätzt eine Summe nach unten ab.
--- falsch
$d(x,y)=d(x,z)+d(z,y)$ für jedes $z$: Jeder Umweg ist genau so lang wie der direkte Weg. Für den Betrag: $|x+y|=|x|+|y|$; man darf den Betrag aufteilen.
--- falsch
$d(x,y)\le d(x,z)\cdot d(z,y)$: Ein Umweg über $z$ multipliziert die Wege. Für den Betrag: $|xy|\le|x|+|y|$; sie schätzt ein Produkt nach oben ab.
:::
:::karte formel untere Dreiecksungleichung
Wie lautet die untere Dreiecksungleichung, und wozu dient sie?
---
$\bigl||x|-|y|\bigr|\le|x\pm y|$. Sie schätzt eine Summe oder Differenz nach unten ab, während die Dreiecksungleichung nach oben abschätzt.
--- falsch
$\bigl||x|-|y|\bigr|\ge|x\pm y|$. Sie schätzt eine Summe oder Differenz nach oben ab, genau wie die Dreiecksungleichung, nur etwas genauer als diese.
--- falsch
$|x|-|y|=|x-y|$. Sie gibt den Betrag einer Differenz exakt an, während die Dreiecksungleichung ihn nur nach oben abschätzt.
--- falsch
$\bigl||x|-|y|\bigr|\le|x|+|y|$. Sie schätzt die Summe der Beträge nach unten ab und wird nur für Zahlen mit gleichem Vorzeichen gebraucht.
:::
:::karte formel Betrag eines Produkts
Wie verhält sich der Betrag bei Produkten und Quotienten, und wie schreibt man ihn als Wurzel?
---
$|xy|=|x||y|$ und für $z\ne0$ $|x/z|=|x|/|z|$; außerdem $|x|=\sqrt{x^2}$, weil $|x|$ die nicht negative Lösung von $z^2=x^2$ ist.
--- falsch
$|xy|\le|x||y|$ und für $z\ne0$ $|x/z|\le|x|/|z|$; außerdem $|x|=\sqrt x$ für alle $x$, weil die Wurzel das Vorzeichen entfernt.
--- falsch
$|xy|=|x|+|y|$ und für $z\ne0$ $|x/z|=|x|-|z|$; außerdem $|x|=\sqrt{x^2}$, weil Quadrieren das Vorzeichen entfernt.
--- falsch
$|xy|=|x||y|$ nur bei gleichen Vorzeichen, bei verschiedenen ist $|xy|=-|x||y|$; außerdem $|x|=x^2$ für $|x|\ge1$.
:::
:::karte zusammenhang keine Gleichheit in der Dreiecksungleichung
Warum gilt im Allgemeinen nicht $|x+y|=|x|+|y|$?
---
Weil sich Summanden mit verschiedenen Vorzeichen teilweise aufheben: $|-3+5|=2<8$. Gleichheit gilt nur bei gleichen Vorzeichen oder wenn ein Summand null ist.
--- falsch
Weil der Betrag eine Summe immer verkleinert: Auch bei gleichen Vorzeichen ist $|x+y|$ echt kleiner als $|x|+|y|$, außer für $x=y=0$.
--- falsch
Weil der Betrag nur für einzelne Zahlen erklärt ist; für Summen muss man jeden Summanden einzeln betrachten, und dann ist $|x+y|$ nicht festgelegt.
--- falsch
Weil sich Summanden mit gleichen Vorzeichen gegenseitig verstärken: $|3+5|=8>2$. Gleichheit gilt nur bei verschiedenen Vorzeichen der Summanden.
:::
:::karte zusammenhang Toleranz
Was bedeutet eine Angabe wie $|U-5\,\mathrm V|\le0{,}1\,\mathrm V$ für den Wert $U$?
---
Dass $U$ höchstens $0{,}1\,\mathrm V$ von $5\,\mathrm V$ abweicht, also zwischen 4,9 V und 5,1 V liegt; der Betrag misst den Abstand von $U$ zu $5\,\mathrm V$.
--- falsch
Dass $U$ zwischen $5\,\mathrm V$ und $5{,}1\,\mathrm V$ liegt; nach unten ist keine Abweichung erlaubt, weil der Betrag nie negativ sein kann.
--- falsch
Dass $U$ genau $5{,}1\,\mathrm V$ oder genau $4{,}9\,\mathrm V$ beträgt; Werte dazwischen erfüllen die Ungleichung nicht.
--- falsch
Dass $U$ höchstens $0{,}1\,\mathrm V$ groß ist; die $5\,\mathrm V$ geben nur den Messbereich an, in dem man misst.
:::
:::karte zusammenhang Toleranzen addieren
Zwei Spannungen erfüllen $|U_1-5\,\mathrm V|\le0{,}1\,\mathrm V$ und $|U_2-3\,\mathrm V|\le0{,}2\,\mathrm V$. Wie weit kann $U_1+U_2$ höchstens von 8 V abweichen, und warum?
---
Um $0{,}3\,\mathrm V$: Nach der Dreiecksungleichung ist $|(U_1+U_2)-8\,\mathrm V|\le|U_1-5\,\mathrm V|+|U_2-3\,\mathrm V|\le0{,}3\,\mathrm V$; erreicht bei $U_1=5{,}1\,\mathrm V$, $U_2=3{,}2\,\mathrm V$.
--- falsch
Um $0{,}2\,\mathrm V$: Die größere der beiden Toleranzen bestimmt die Abweichung der Summe, und die kleinere geht in ihr auf, weil sich Abweichungen nicht addieren.
--- falsch
Um $0{,}1\,\mathrm V$: Die beiden Abweichungen heben sich teilweise auf, deshalb bleibt von ihnen nur die Differenz $0{,}2\,\mathrm V-0{,}1\,\mathrm V$ übrig.
--- falsch
Um $0{,}3\,\mathrm V$, aber dieser Wert wird nie erreicht, weil die beiden Spannungen nicht zugleich an ihrer Grenze liegen können; die Schranke ist nur grob.
:::
:::karte zusammenhang Umweg über einen dritten Punkt
Wann ist der Umweg über einen Punkt $z$ in der Dreiecksungleichung $d(x,y)\le d(x,z)+d(z,y)$ genau so lang wie der direkte Weg?
---
Wenn $z$ zwischen $x$ und $y$ liegt oder mit einem der beiden zusammenfällt. Für $x=-3$, $y=5$ ergibt $z=1$ genau $4+4=8$, der Umweg über $z=7$ dagegen $10+2=12$.
--- falsch
Nie: Ein Umweg über einen dritten Punkt ist immer echt länger als der direkte Weg, auch wenn $z$ zwischen $x$ und $y$ liegt; nur $z=x$ wäre eine Ausnahme.
--- falsch
Wenn $z$ außerhalb der Strecke zwischen $x$ und $y$ liegt; liegt $z$ dazwischen, wird der Umweg länger, weil man an $z$ ein zweites Mal ansetzt.
--- falsch
Wenn $z$ genau in der Mitte zwischen $x$ und $y$ liegt; für jeden anderen Punkt $z$, auch zwischen $x$ und $y$, ist der Umweg echt länger.
:::
:::karte herleitung untere Dreiecksungleichung
Wie folgt die untere Dreiecksungleichung $\bigl||x|-|y|\bigr|\le|x-y|$ aus der Dreiecksungleichung?
---
Man schreibt $|x|=|(x-y)+y|\le|x-y|+|y|$, weil die Dreiecksungleichung für die Summanden $x-y$ und $y$ gilt.
---
Daraus folgt $|x|-|y|\le|x-y|$, weil man auf beiden Seiten $|y|$ abziehen darf.
---
Durch Tauschen von $x$ und $y$ folgt ebenso $|y|-|x|\le|x-y|$, weil der Abstand symmetrisch ist.
---
Das Maximum der beiden linken Seiten ist $\bigl||x|-|y|\bigr|$, weil allgemein $|x|=\max\{x,-x\}$ gilt; also folgt die Behauptung.
:::
::::
