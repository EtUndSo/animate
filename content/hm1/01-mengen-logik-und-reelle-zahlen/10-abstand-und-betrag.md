---
title: Stufe 8: Abstand und Betrag
pfad: Elektrotechnik / 1. Semester / Höhere Mathematik 1 / Mengen, Logik und reelle Zahlen
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
