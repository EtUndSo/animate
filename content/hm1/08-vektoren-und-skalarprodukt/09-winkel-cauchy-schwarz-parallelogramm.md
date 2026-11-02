---
title: Stufe 7: Winkel, Cauchy-Schwarz, Parallelogramm
pfad: Elektrotechnik / 1. Semester / Höhere Mathematik 1 / Vektoren und Skalarprodukt
order: 1280900
summary: In der Ebene ist ein Winkel ein Drehwinkel, im mathbb R 4 gibt es nichts zu zeichnen.
tags: orientierte Winkel, Drehwinkel, Argument, nichtorientierte Winkel, Parallelogrammgleichung
lang: de
---

<span class="anker" id="stufe-7"></span>

:::zweck
In der Ebene ist ein Winkel ein Drehwinkel, im $\mathbb{R}^4$ gibt es nichts zu zeichnen. Diese Stufe drückt den Winkel durch das Skalarprodukt aus und zeigt, warum dieselbe Formel in $\mathbb{R}^n$ erlaubt ist.
:::

**Die Idee.** Projiziert man $\vec x$ auf die Richtung von $\vec y$, bleibt ein Rest. Im rechtwinkligen Dreieck aus Anteil, Rest und $\vec x$ ist $\vec x$ die Hypotenuse. Eine Kathete ist nie länger als die Hypotenuse, also gilt $|\text{Anteil}|\le\|\vec x\|$. Das ist Cauchy-Schwarz, und der Grund ist ein Quadrat, das nicht negativ sein kann: $\|\text{Rest}\|^2\ge0$. Der Quotient aus Anteil und $\|\vec x\|$ ist der Kosinus des Winkels aus der Schule.

:::satz Satz 7.1 (Orientierter Winkel)
<span class="anker" id="satz-7-1"></span>

Im $\mathbb{R}^2$ gilt für $\vec u,\vec v\in\mathbb{R}^2\setminus\{\vec0\}$

<span class="anker" id="gl-7-1"></span>
$$\cos(\alpha)=\frac{u_1v_1+u_2v_2}{\|\vec u\|\cdot\|\vec v\|}, \tag{7.1}$$

wobei $\alpha=\arg(z_v)-\arg(z_u)\in(-2\pi,2\pi)$ der __orientierte Winkel__ (__Drehwinkel__) zwischen $\vec u$ und $\vec v$ ist. Dabei wird $\vec u=(u_1,u_2)$ mit $z_u=u_1+iu_2\in\mathbb{C}$ identifiziert.
:::

⁠**So liest man das:** $\arg(z)\in[0,2\pi)$ ist das __Argument__ von $z$, der Winkel von der positiven reellen Achse zum Zeiger von $z$. Der Winkel $\alpha$ ist die Drehung von $\vec u$ nach $\vec v$ mit Vorzeichen. Im Modell ist $\arg(3+i)=18{,}43^\circ$ und $\arg(1+2i)=63{,}43^\circ$, also $\alpha=45^\circ$. Die Formel gibt $\cos\alpha=\frac5{\sqrt{10}\sqrt5}=\frac1{\sqrt2}$. Vertauscht man die Vektoren, wird $\alpha$ zu $-\alpha$, $\cos$ bleibt gleich.

:::beweis Über komplexe Zahlen
Nach der Polarform ([Teil 7](/wissen/elektrotechnik/1-semester/hohere-mathematik-1/potenzreihen-und-eulersche-formel/potenzreihen-und-eulersche-formel.html)) ist $z_u=|z_u|\,\mathrm{e}^{i\varphi}$, $z_v=|z_v|\,\mathrm{e}^{i\psi}$ mit $\varphi=\arg(z_u)$, $\psi=\arg(z_v)$, $|z_u|=\|\vec u\|$, $|z_v|=\|\vec v\|$. Mit $\alpha=\psi-\varphi$ und der Eulerschen Formel ist

$$\frac{z_v}{z_u}=\frac{\|\vec v\|}{\|\vec u\|}\,\mathrm{e}^{i\alpha}=\frac{\|\vec v\|}{\|\vec u\|}\bigl(\cos\alpha+i\sin\alpha\bigr).$$

Der Realteil gibt mit $z_u\bar z_u=\|\vec u\|^2$

$$\cos\alpha=\frac{\|\vec u\|}{\|\vec v\|}\operatorname{Re}\frac{z_v\,\bar z_u}{z_u\,\bar z_u}=\frac{\operatorname{Re}\bigl((v_1+iv_2)(u_1-iu_2)\bigr)}{\|\vec u\|\cdot\|\vec v\|}=\frac{u_1v_1+u_2v_2}{\|\vec u\|\cdot\|\vec v\|}.$$
:::

:::satz Satz 7.2 (Cauchy-Schwarz-Ungleichung)
<span class="anker" id="satz-7-2"></span>

Für $\vec x,\vec y\in\mathbb{R}^n$ gilt

<span class="anker" id="gl-7-2"></span>
$$|\langle\vec x,\vec y\rangle|\le\|\vec x\|\cdot\|\vec y\|. \tag{7.2}$$

Gleichheit gilt genau dann, wenn $\vec x$ und $\vec y$ linear abhängig sind.
:::

⁠**So liest man das:** Das Skalarprodukt ist nie größer als das Produkt der Längen. Am größten wird es, wenn beide Vektoren auf einer Geraden durch $O$ liegen. Im Modell: $|\langle\vec a,\vec b\rangle|=5\le\sqrt{50}=7{,}07$. Die Form aus [Teil 1](/wissen/elektrotechnik/1-semester/hohere-mathematik-1/mengen-logik-und-reelle-zahlen/mengen-logik-und-reelle-zahlen.html) ist sogar stärker, denn dort steht links $\sum_i|x_iy_i|\ge|\sum_ix_iy_i|$.

:::beweis Der Rest hat Länge $\ge0$
⁠*Fall $\vec y=\vec0$.* Beide Seiten sind 0, es gilt Gleichheit, und $\vec x,\vec0$ sind linear abhängig.

⁠*Fall $\vec y\ne\vec0$.* Setze $\vec e:=\vec y/\|\vec y\|$, dann ist $\|\vec e\|=1$. Nach [(5.2)](skalarprodukt-norm-abstand.html#gl-5-2) mit $\vec z=\langle\vec x,\vec e\rangle\vec e$ und Homogenität ist

<span class="anker" id="gl-7-3"></span>
$$0\le\bigl\|\vec x-\langle\vec x,\vec e\rangle\vec e\bigr\|^2=\|\vec x\|^2-2\langle\vec x,\vec e\rangle^2+\langle\vec x,\vec e\rangle^2\|\vec e\|^2=\|\vec x\|^2-\langle\vec x,\vec e\rangle^2. \tag{7.3}$$

Also ist $|\langle\vec x,\vec e\rangle|\le\|\vec x\|$. Multiplizieren mit $\|\vec y\|$ gibt [(7.2)](#gl-7-2), denn $\langle\vec x,\vec y\rangle=\|\vec y\|\langle\vec x,\vec e\rangle$.

⁠*Gleichheit* in [(7.2)](#gl-7-2) heißt: Rechts in [(7.3)](#gl-7-3) steht 0. Nach der Definitheit ist das $\vec x=\langle\vec x,\vec e\rangle\vec e=\frac{\langle\vec x,\vec y\rangle}{\|\vec y\|^2}\vec y$, also sind $\vec x,\vec y$ linear abhängig. Umgekehrt: Sind $\vec x,\vec y$ linear abhängig und $\vec y\ne\vec0$, ist $\vec x$ nach Satz [4.3](lineare-unabhangigkeit.html#satz-4-3) (ii) ein Vielfaches von $\vec y$, denn $\vec y=\mu\vec x$ erzwingt $\mu\ne0$. Dann ist der Rest $\vec0$, und in [(7.3)](#gl-7-3) steht Gleichheit.
:::

:::definition Definition 7.3 (Nichtorientierter Winkel)
<span class="anker" id="satz-7-3"></span>

Für $\vec x,\vec y\in\mathbb{R}^n\setminus\{\vec0\}$ ist durch

<span class="anker" id="gl-7-4"></span>
$$\cos(\phi)=\frac{\langle\vec x,\vec y\rangle}{\|\vec x\|\cdot\|\vec y\|},\qquad0\le\phi\le\pi, \tag{7.4}$$

der __nichtorientierte Winkel__ $\phi$ zwischen $\vec x$ und $\vec y$ erklärt.
:::

⁠**So liest man das:** Die rechte Seite liegt wegen [(7.2)](#gl-7-2) in $[-1,1]$. Weil $\cos$ auf $[0,\pi]$ streng monoton fällt, gibt es genau ein $\phi$, die Definition ist also sinnvoll. Ohne Cauchy-Schwarz könnte der Quotient $2$ sein, und es gäbe keinen Winkel. Es gilt $\langle\vec x,\vec y\rangle=0\iff\phi=\frac\pi2$, das ist „senkrecht“ aus Stufe [5](skalarprodukt-norm-abstand.html#stufe-5). Für $\vec c,\vec d$ ist $\cos\phi=\frac15$, also $\phi=78{,}46^\circ$. **Grenzfälle:** $\vec y=\vec x$ gibt $\phi=0$, $\vec y=-\vec x$ gibt $\phi=\pi$. Das sind die Gleichheitsfälle von Cauchy-Schwarz. Ein orientierter Winkel existiert nur in $\mathbb{R}^2$.

:::abbildung hm1/k8winkel 8
Links die Winkel im Modell: $\vec a$ hat das Argument $18{,}43^\circ$, $\vec b$ das Argument $63{,}43^\circ$, die Differenz ist $45^\circ$. Rechts die Parallelogrammgleichung: Die Diagonalen $\vec a+\vec b$ und $\vec a-\vec b$ haben die Längenquadrate 25 und 5, die Summe 30 ist die Summe der vier Seitenquadrate $10+5+10+5$.
:::

:::frage Warum gibt es im Raum keinen orientierten Winkel?
Ein Drehsinn setzt voraus, dass man von einer festen Seite auf die Ebene der beiden Vektoren schaut. Im $\mathbb{R}^2$ gibt es diese Seite. Im $\mathbb{R}^3$ kann man um die Ebene herumgehen. Zeichnet man $\vec x,\vec y$ auf ein Blatt, läuft die Drehung von der Vorderseite gesehen gegen den Uhrzeiger und von der Rückseite gesehen mit ihm.
:::

:::satz Satz 7.4 (Parallelogrammgleichung)
<span class="anker" id="satz-7-4"></span>

Für $\vec x,\vec y\in\mathbb{R}^n$ gilt

<span class="anker" id="gl-7-5"></span>
<span class="anker" id="gl-7-6"></span>
$$\begin{aligned} \|\vec x+\vec y\|^2+\|\vec x-\vec y\|^2&=2\|\vec x\|^2+2\|\vec y\|^2,\\ \|\vec x+\vec y\|^2-\|\vec x-\vec y\|^2&=4\langle\vec x,\vec y\rangle. \end{aligned} \tag{7.5|7.6}$$
:::

⁠**So liest man das:** [(7.5)](#gl-7-5) heißt __Parallelogrammgleichung__: Die Quadrate der Diagonalen ergeben zusammen die Quadrate der vier Seiten. [(7.6)](#gl-7-6) sagt: Wer Längen messen kann, kennt auch das Skalarprodukt, also die Winkel. Beweis: Addieren beziehungsweise Subtrahieren der beiden Fälle von [(5.2)](skalarprodukt-norm-abstand.html#gl-5-2) mit $\vec z=\vec y$. Im Modell: $25+5=2\cdot10+2\cdot5$ und $25-5=4\cdot5$.

**Dreiecksungleichung.** Aus [(5.2)](skalarprodukt-norm-abstand.html#gl-5-2) und [(7.2)](#gl-7-2) folgt $\|\vec x+\vec y\|^2\le\|\vec x\|^2+2\|\vec x\|\,\|\vec y\|+\|\vec y\|^2=(\|\vec x\|+\|\vec y\|)^2$. Das ist (N) aus Satz [5.2](skalarprodukt-norm-abstand.html#satz-5-2) ohne Umweg über [Teil 1](/wissen/elektrotechnik/1-semester/hohere-mathematik-1/mengen-logik-und-reelle-zahlen/mengen-logik-und-reelle-zahlen.html).

:::aufgabe Aufgabe 8 ★★ Winkel am Würfel
<span class="anker" id="aufg-8"></span>

Ein Würfel hat die Ecken $(\pm1,\pm1,\pm1)$. (a) Unter welchem Winkel schneiden sich $(1,1,1)$ und $(-1,1,1)$, zwei Raumdiagonalen? (b) Welchen Winkel schließt die Kante $(1,0,0)$ mit $(1,1,1)$ ein? (c) Prüfe Cauchy-Schwarz für $(1,2,3)$ mit $(3,2,1)$ und mit $(-2,-4,-6)$. Welcher Fall ist der Gleichheitsfall, und welches $\phi$ gehört dazu?

:::loesung
(a) $\cos\phi=\frac{-1+1+1}{\sqrt3\sqrt3}=\frac13$, $\phi=70{,}53^\circ$. (b) $\cos\phi=\frac1{\sqrt3}$, $\phi=54{,}74^\circ$. (c) $10\le\sqrt{14}\sqrt{14}=14$, echt kleiner. $|-28|=\sqrt{14}\sqrt{56}=28$: Gleichheit, denn $(-2,-4,-6)=-2(1,2,3)$. Das Skalarprodukt ist negativ, also $\phi=\pi$.
:::
:::

:::aufgabe Aufgabe 9 ★★ Parallelogramm
<span class="anker" id="aufg-9"></span>

(a) Ein Parallelogramm hat die Seiten $\|\vec x\|=5$, $\|\vec y\|=3$ und die Diagonale $\|\vec x+\vec y\|=7$. Bestimme die andere Diagonale, $\langle\vec x,\vec y\rangle$ und den Winkel. (b) Zeige: Die Diagonalen sind genau dann gleich lang, wenn $\vec x\perp\vec y$ (Rechteck). (c) Zeige: $(\vec x+\vec y)\perp(\vec x-\vec y)$ genau dann, wenn $\|\vec x\|=\|\vec y\|$ (Raute).

:::loesung
(a) $\|\vec x-\vec y\|^2=2\cdot25+2\cdot9-49=19$, also $\|\vec x-\vec y\|=\sqrt{19}=4{,}36$. Nach [(7.6)](#gl-7-6) ist $\langle\vec x,\vec y\rangle=\frac{49-19}4=7{,}5$, also $\cos\phi=\frac{7{,}5}{15}=\frac12$, $\phi=60^\circ$. (b) Nach [(7.6)](#gl-7-6): $\|\vec x+\vec y\|=\|\vec x-\vec y\|\iff\langle\vec x,\vec y\rangle=0$. (c) Bilinear: $\langle\vec x+\vec y,\vec x-\vec y\rangle=\|\vec x\|^2-\|\vec y\|^2$, und das ist genau dann 0, wenn $\|\vec x\|=\|\vec y\|$.
:::
:::
