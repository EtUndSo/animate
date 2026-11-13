---
title: Stufe 2: Wachstum, Logarithmus, allgemeine Potenz
pfad: Elektrotechnik / 1. Semester / HöMa1 – Höhere Mathematik 1 / Exponentialfunktion und Stetigkeit
adresse: elektrotechnik/1-semester/hohere-mathematik-1/exponentialfunktion-und-stetigkeit
knoten: Kapitel 5: Exponentialfunktion und Stetigkeit
order: 1250400
summary: e x ist definiert.
tags: natürlicher Logarithmus, allgemeine Potenz
lang: de
---

<span class="anker" id="stufe-2"></span>

:::zweck
$\mathrm{e}^x$ ist definiert. Offen ist, wie schnell die Funktion wächst, wie man $\mathrm{e}^x=y$ nach $x$ auflöst und was $2^{\sqrt2}$ bedeutet.
:::

**Die Idee.** Die Gerade $1+x$ liegt unter $\mathrm{e}^x$, daraus folgt fast alles über das Wachstum. Weil $\mathrm{e}^x$ streng wächst, lässt es sich umkehren. Mit $a=\mathrm{e}^{\log a}$ wird jede Potenz zu einer Potenz von $\mathrm{e}$.

:::satz Satz 2.1 (Eigenschaften der Exponentialfunktion)
<span class="anker" id="satz-2-1"></span>

<ol class="rm">

<li>

$\mathrm{e}^x\ge1+x$ für alle $x\in\mathbb{R}$.

</li>

<li>

$\mathrm{e}^x>\mathrm{e}^y$ für alle $x>y$, das heißt: $\exp$ ist streng monoton wachsend.

</li>

<li>

$|\mathrm{e}^x-1|\le\dfrac{|x|}{1-|x|}$ für alle $x\in\mathbb{R}$ mit $|x|<1$.

</li>

<li>

$\mathrm{e}^x>x^n$ für alle $x>4n^2$, $n\in\mathbb{N}$: $\exp$ wächst schneller als jede Potenz von $x$.

</li>

<li>

$\lim_{n\to\infty}\mathrm{e}^{-n}=0$.

</li>

</ol>
:::

⁠**So liest man das:** Nach (iii) liegt $\mathrm{e}^x$ nahe 0 nahe bei 1. Die Schranke in (iv) ist grob: Für $n=3$ fordert sie $x>36$, tatsächlich gilt $\mathrm{e}^x>x^3$ für alle $x\ge4{,}54$.

:::beweis Eigenschaften der Exponentialfunktion
(i) Für $x\le-1$ ist $1+x\le0<\mathrm{e}^x$. Für $x>-1$ ist $z_1(x)=1+x$, und $\{z_n(x)\}$ wächst ab $n=1$, also ist $1+x\le\lim z_n(x)=\mathrm{e}^x$.

(ii) $\mathrm{e}^x-\mathrm{e}^y=\mathrm{e}^y(\mathrm{e}^{x-y}-1)>0$, denn $\mathrm{e}^y>0$ und $\mathrm{e}^{x-y}\ge1+x-y>1$ nach (i).

(iii) Für $x=0$ steht $0\le0$ da. Für $0<x<1$ gibt (i) $\mathrm{e}^{-x}\ge1-x>0$, also $\mathrm{e}^x\le\frac1{1-x}$ und $0<\mathrm{e}^x-1\le\frac x{1-x}$. Für $-1<x<0$ gibt (i) $x\le\mathrm{e}^x-1$, und nach (ii) ist $\mathrm{e}^x-1<0$. Also ist $|\mathrm{e}^x-1|\le|x|\le\frac{|x|}{1-|x|}$.

(iv) Aus $x>4n^2$ folgt $\sqrt x>2n$, also $\frac x{2n}>\sqrt x$. Da $z_m(x)$ streng gegen $\mathrm{e}^x$ wächst, ist $\mathrm{e}^x>z_{2n}(x)=(1+\frac x{2n})^{2n}>(\sqrt x)^{2n}=x^n$.

(v) Nach (i) ist $0<\mathrm{e}^{-n}=\frac1{\mathrm{e}^n}\le\frac1{1+n}$, und das ist eine Majorante ([Kapitel 4](/wissen/elektrotechnik/1-semester/hohere-mathematik-1/folgen-und-grenzwerte/folgen-und-grenzwerte.html)).
:::

:::satz Satz 2.2 (Natürlicher Logarithmus)
<span class="anker" id="satz-2-2"></span>

Es gilt $\mathcal W(\exp)=\mathbb{R}^+$. Also ist $\exp:\mathbb{R}\to\mathbb{R}^+$ surjektiv und wegen der strengen Monotonie bijektiv. Die Umkehrfunktion $\log:\mathbb{R}^+\to\mathbb{R}$, $x\mapsto\log(x)$, heißt __natürlicher Logarithmus__, und es gilt

<span class="anker" id="gl-2-1"></span>
$$\exp(\log y)=y\quad\forall\,y\in\mathbb{R}^+,\qquad\log(\exp x)=x\quad\forall\,x\in\mathbb{R}. \tag{2.1}$$
:::

Injektiv ist $\exp$ wegen Satz [2.1](#satz-2-1) (ii). Dass jedes $y>0$ getroffen wird, zeigt der Zwischenwertsatz in Stufe [8](zwischenwerte-nullstellen-umkehrfunktion.html#stufe-8), sein Beweis benutzt $\log$ nicht.

:::satz Satz 2.3 (Eigenschaften des Logarithmus)
<span class="anker" id="satz-2-3"></span>

<ol class="rm">

<li>

$\log x<\log y$ für alle $x,y\in\mathbb{R}^+$ mit $x<y$: $\log$ ist streng monoton wachsend.

</li>

<li>

$\log(x\cdot y)=\log x+\log y$ und $\log\frac xy=\log x-\log y$ für alle $x,y\in\mathbb{R}^+$ (Funktionalgleichung).

</li>

<li>

$\log(x^n)=n\cdot\log x$ für alle $x\in\mathbb{R}^+$, $n\in\mathbb{N}$.

</li>

<li>

$\log(1+x)\le x$ für alle $x>-1$, gleichbedeutend $\log t\le t-1$ für alle $t>0$.

</li>

<li>

$\log x<\sqrt[n]{x}<x$ für alle $x>(4n^2)^n$, $n\ge2$: $\log$ wächst schwächer als jede Wurzel.

</li>

</ol>
:::

⁠**So liest man das:** $\log y$ ist der Exponent, mit dem man $\mathrm{e}$ potenzieren muss, um $y$ zu erhalten. Aus [(2.1)](#gl-2-1) folgen $\log1=0$, $\log\mathrm{e}=1$ und $\log\frac{1}{\mathrm{e}}=-1$. Für $y\le0$ gibt es keinen Logarithmus, $\mathrm{e}^x$ trifft diese Zahlen nie. Taschenrechner nennen diese Funktion meist $\ln$ und meinen mit $\log$ oft die Basis 10. Hier ist $\log10=2{,}3026$.

:::beweis Eigenschaften des Logarithmus
(i) Monotonie vererbt sich auf die Umkehrfunktion ([Kapitel 3](/wissen/elektrotechnik/1-semester/hohere-mathematik-1/funktionen-und-polynome/funktionen-und-polynome.html)). (ii) Mit $u=\log x$, $v=\log y$ ist $\log(xy)=\log(\mathrm{e}^u\mathrm{e}^v)=\log(\mathrm{e}^{u+v})=u+v$. Aus $0=\log\frac yy=\log y+\log\frac1y$ folgt $\log\frac1y=-\log y$ und damit die zweite Formel. (iii) Induktion mit (ii). (iv) Aus $0<1+x\le\mathrm{e}^x$ folgt mit (i) und [(2.1)](#gl-2-1) $\log(1+x)\le x$. (v) Setze $y=\sqrt[n]{x}$, also $y>4n^2$ und $y^n=x$. Satz [2.1](#satz-2-1) (iv) gibt $\mathrm{e}^y>y^n=x$, Anwenden von $\log$ gibt $y>\log x$. Und $y<x$ gilt, weil $x>1$ und $n\ge2$ ist.
:::

:::abbildung hm1/k5explog 2
$\mathrm{e}^x$ und $\log x$ sind Spiegelbilder an $y=x$. $\mathrm{e}^x$ liegt über $y=x+1$, $\log x$ unter $y=x-1$. Der Punkt $(1\,|\,\mathrm{e})$ geht in $(\mathrm{e}\,|\,1)$ über.
:::

:::definition Definition 2.4 (Allgemeine Potenz)
<span class="anker" id="satz-2-4"></span>

Für $a>0$ und $x\in\mathbb{R}$ heißt

<span class="anker" id="gl-2-2"></span>
$$a^x:=\mathrm{e}^{x\cdot\log a} \tag{2.2}$$

die __allgemeine Potenz__, $x\mapsto a^x$ die allgemeine Potenzfunktion von $\mathbb{R}$ nach $\mathbb{R}^+$.
:::

:::satz Satz 2.5 (Rechenregeln für Potenzen)
<span class="anker" id="satz-2-5"></span>

Für $a,b>0$, $x,y\in\mathbb{R}$ gilt: (i) $(a\cdot b)^x=a^x\cdot b^x$, (ii) $a^{x\cdot y}=(a^x)^y$, (iii) $a^{x+y}=a^x\cdot a^y$ (Funktionalgleichung), (iv) $\log(a^x)=x\cdot\log a$. Für rationales $x=\frac pq$ stimmt [(2.2)](#gl-2-2) mit der Potenz $a^{p/q}:=\sqrt[q]{a^p}$ überein.
:::

:::beweis Alles läuft über $\exp$ und $\log$
(iv) $\log(\mathrm{e}^{x\log a})=x\log a$ nach [(2.1)](#gl-2-1). (i) $\mathrm{e}^{x\log(ab)}=\mathrm{e}^{x\log a+x\log b}=\mathrm{e}^{x\log a}\mathrm{e}^{x\log b}$. (ii) $(a^x)^y=\mathrm{e}^{y\log(a^x)}=\mathrm{e}^{yx\log a}$ nach (iv). (iii) $\mathrm{e}^{(x+y)\log a}=\mathrm{e}^{x\log a}\mathrm{e}^{y\log a}$. Rationale $x$: Satz [2.3](#satz-2-3) (ii), (iii) geben $q\log\sqrt[q]{a^p}=\log(a^p)=p\log a$, also $\sqrt[q]{a^p}=\mathrm{e}^{\frac pq\log a}$.
:::

⁠**So liest man das:** Die Regeln aus [Kapitel 1](/wissen/elektrotechnik/1-semester/hohere-mathematik-1/mengen-logik-und-reelle-zahlen/mengen-logik-und-reelle-zahlen.html) gelten jetzt für reelle Exponenten.

::::beispiel
$2^{\sqrt2}=\mathrm{e}^{\sqrt2\cdot0{,}6931}=\mathrm{e}^{0{,}9803}=2{,}6651$.
::::

⁠**Grenzfälle:** $a=1$ ergibt $1^x=1$, denn $\log1=0$; $a=\mathrm{e}$ ergibt wieder $\mathrm{e}^x$. **Warum $a>0$:** Für $a<0$ ist nur ein Teil erklärt: $a^n$, $a^{-n}=1/a^n$ und $a^{1/n}$ für ungerades $n$. Mehr geht nicht widerspruchsfrei: $(-8)^{1/3}=-2$, aber mit $\frac26=\frac13$ wäre $\sqrt[6]{(-8)^2}=2$.

:::aufgabe Aufgabe 2 ★★ Gleichungen und Wachstum
<span class="anker" id="aufg-2"></span>

(a) Löse $3^x=20$. (b) Löse $\mathrm{e}^{2x}-5\mathrm{e}^x+6=0$. (c) Nach welcher Zeit verdoppelt sich ein Kapital bei $p=5$ und kontinuierlicher Verzinsung? (d) Ab welchem $x$ garantiert Satz [2.1](#satz-2-1) (iv) für $n=1$ die Ungleichung $\mathrm{e}^x>x$? Gilt sie auch sonst?

:::loesung
(a) $x=\log20/\log3=2{,}7268$. (b) Mit $u=\mathrm{e}^x>0$: $u^2-5u+6=(u-2)(u-3)=0$, also $x=\log2=0{,}6931$ oder $x=\log3=1{,}0986$. (c) $\mathrm{e}^{0{,}05\,T}=2$ gibt $T=\log2/0{,}05=13{,}86$ Jahre. (d) Für $x>4$. Sie gilt für alle $x$, denn $\mathrm{e}^x\ge1+x>x$.
:::
:::

::::formelsammlung
**Exponentialfunktion über der Geraden**

$$\mathrm{e}^x\ge1+x$$

Für alle $x\in\mathbb{R}$.

**Strenge Monotonie**

$$\mathrm{e}^x>\mathrm{e}^y\quad\text{für alle }x>y$$

Denn $\mathrm{e}^x-\mathrm{e}^y=\mathrm{e}^y(\mathrm{e}^{x-y}-1)>0$.

**Abschätzung nahe null**

$$|\mathrm{e}^x-1|\le\dfrac{|x|}{1-|x|}$$

Für alle $x\in\mathbb{R}$ mit $|x|<1$.

**Schneller als jede Potenz**

$$\mathrm{e}^x>x^n\quad\text{für alle }x>4n^2,\ n\in\mathbb{N}$$

Außerdem $\lim_{n\to\infty}\mathrm{e}^{-n}=0$.

**Natürlicher Logarithmus**

$$\exp(\log y)=y\quad\forall\,y\in\mathbb{R}^+,\qquad\log(\exp x)=x\quad\forall\,x\in\mathbb{R}$$

$\log:\mathbb{R}^+\to\mathbb{R}$ ist die Umkehrfunktion der Bijektion $\exp:\mathbb{R}\to\mathbb{R}^+$; $\log1=0$, $\log\mathrm{e}=1$. Für $y\le0$ gibt es keinen Logarithmus.

**Funktionalgleichung des Logarithmus**

$$\log(x\cdot y)=\log x+\log y,\qquad\log\frac xy=\log x-\log y$$

Für alle $x,y\in\mathbb{R}^+$; $\log$ ist streng monoton wachsend.

**Logarithmus einer Potenz**

$$\log(x^n)=n\cdot\log x$$

Für $x\in\mathbb{R}^+$, $n\in\mathbb{N}$.

**Logarithmus unter der Geraden**

$$\log(1+x)\le x\quad(x>-1),\qquad\log t\le t-1\quad(t>0)$$

Zwei Schreibweisen derselben Aussage.

**Langsamer als jede Wurzel**

$$\log x<\sqrt[n]{x}<x$$

Für alle $x>(4n^2)^n$, $n\ge2$.

**Allgemeine Potenz**

$$a^x:=\mathrm{e}^{x\cdot\log a}$$

Für $a>0$, $x\in\mathbb{R}$; $x\mapsto a^x$ geht von $\mathbb{R}$ nach $\mathbb{R}^+$. Für rationales $x=\frac pq$ stimmt sie mit $a^{p/q}:=\sqrt[q]{a^p}$ überein.

**Rechenregeln für Potenzen**

$$(a\cdot b)^x=a^x\cdot b^x,\quad a^{x\cdot y}=(a^x)^y,\quad a^{x+y}=a^x\cdot a^y,\quad\log(a^x)=x\cdot\log a$$

Für $a,b>0$, $x,y\in\mathbb{R}$.
::::

::::lernkarten
:::karte formel Eigenschaften der Exponentialfunktion
Welche Ungleichung verbindet $\mathrm{e}^x$ mit der Geraden $1+x$, und welche Monotonie der Exponentialfunktion folgt daraus?
---
$\mathrm{e}^x\ge1+x$ für alle $x\in\mathbb{R}$. Daraus folgt $\mathrm{e}^x>\mathrm{e}^y$ für alle $x>y$, denn $\mathrm{e}^x-\mathrm{e}^y=\mathrm{e}^y(\mathrm{e}^{x-y}-1)>0$: $\exp$ ist streng monoton wachsend.
--- falsch
$\mathrm{e}^x\le1+x$ für alle $x\in\mathbb{R}$: Die Gerade liegt über der Kurve. Daraus folgt, dass $\exp$ höchstens so schnell wächst wie $1+x$.
--- falsch
$\mathrm{e}^x\ge1+x$, aber nur für $x\ge0$; für negative $x$ ist $1+x$ größer. Die Monotonie von $\exp$ folgt daraus nur auf $[0,\infty)$.
--- falsch
$\mathrm{e}^x\ge1+x$ für alle $x\in\mathbb{R}$. Daraus folgt nur, dass $\exp$ monoton wachsend ist, nicht streng, weil die Kurve die Gerade bei 0 berührt.
:::
:::karte formel Abschätzung nahe null
Wie weit kann $\mathrm{e}^x$ für $|x|<1$ höchstens von 1 abweichen?
---
$|\mathrm{e}^x-1|\le\dfrac{|x|}{1-|x|}$ für alle $x\in\mathbb{R}$ mit $|x|<1$: Nahe 0 liegt $\mathrm{e}^x$ nahe bei 1, und die Abweichung geht mit $x$ gegen 0.
--- falsch
$|\mathrm{e}^x-1|\le|x|^2$ für alle $x\in\mathbb{R}$ mit $|x|<1$: Die Abweichung von 1 ist nahe 0 quadratisch klein, also viel kleiner als $|x|$ selbst.
--- falsch
$|\mathrm{e}^x-1|\le\dfrac{|x|}{1-|x|}$ für alle $x\in\mathbb{R}$: Die Abschätzung gilt überall, weil der Bruch für große $|x|$ ebenfalls groß wird.
--- falsch
$|\mathrm{e}^x-1|\ge\dfrac{|x|}{1-|x|}$ für alle $x\in\mathbb{R}$ mit $|x|<1$: Nahe 0 bleibt $\mathrm{e}^x$ mindestens um diesen Bruch von 1 entfernt.
:::
:::karte formel Schneller als jede Potenz
Ab welcher Stelle ist $\mathrm{e}^x$ nach dem Satz größer als $x^n$, und was folgt für die Folge $\mathrm{e}^{-n}$?
---
$\mathrm{e}^x>x^n$ für alle $x>4n^2$, $n\in\mathbb{N}$: $\exp$ wächst schneller als jede Potenz von $x$. Außerdem ist $\lim_{n\to\infty}\mathrm{e}^{-n}=0$.
--- falsch
$\mathrm{e}^x>x^n$ für alle $x>n$, $n\in\mathbb{N}$: Schon ab der Stelle $n$ überholt die Exponentialfunktion die Potenz. Außerdem ist $\lim_{n\to\infty}\mathrm{e}^{-n}=0$.
--- falsch
$\mathrm{e}^x>x^n$ nur für $n\le3$; höhere Potenzen wachsen schneller als $\exp$, sobald $x$ groß genug ist. Außerdem ist $\lim_{n\to\infty}\mathrm{e}^{-n}=1$.
--- falsch
$\mathrm{e}^x>x^n$ für alle $x>4n^2$, und $4n^2$ ist die kleinste solche Stelle: Vorher gilt $\mathrm{e}^x<x^n$. Außerdem ist $\lim_{n\to\infty}\mathrm{e}^{-n}=0$.
:::
:::karte herleitung Wachstum über die Exponentialfolge
Wie folgt $\mathrm{e}^x>x^n$ für $x>4n^2$ aus der Exponentialfolge $z_m(x)$?
---
Aus $x>4n^2$ folgt $\sqrt x>2n$, weil die Wurzel streng monoton wächst.
---
Daraus folgt $\frac x{2n}>\sqrt x$, weil $\frac x{2n}$ das Produkt von $\sqrt x$ mit $\frac{\sqrt x}{2n}>1$ ist.
---
Es ist $\mathrm{e}^x>z_{2n}(x)=(1+\frac x{2n})^{2n}$, weil $z_m(x)$ für $x>0$ streng gegen $\mathrm{e}^x$ wächst und jedes Glied deshalb unter dem Grenzwert liegt.
---
Also $\mathrm{e}^x>(1+\frac x{2n})^{2n}>(\sqrt x)^{2n}=x^n$, weil die Klammer größer als $\frac x{2n}>\sqrt x$ ist.
:::
:::karte begriff natürlicher Logarithmus
Wie ist der natürliche Logarithmus definiert, und welche Gleichungen verbinden ihn mit der Exponentialfunktion?
---
Als Umkehrfunktion $\log:\mathbb{R}^+\to\mathbb{R}$ der bijektiven Abbildung $\exp:\mathbb{R}\to\mathbb{R}^+$. Es gilt $\exp(\log y)=y$ für alle $y\in\mathbb{R}^+$ und $\log(\exp x)=x$ für alle $x\in\mathbb{R}$.
--- falsch
Als Kehrwert $\log(x):=1/\exp(x)$ der Exponentialfunktion, erklärt auf ganz $\mathbb{R}$. Es gilt $\log(x)\cdot\exp(x)=1$ für alle $x\in\mathbb{R}$, also $\log0=1$.
--- falsch
Als Umkehrfunktion $\log:\mathbb{R}\to\mathbb{R}$ der Exponentialfunktion, erklärt für alle reellen Zahlen. Es gilt $\exp(\log y)=y$ für alle $y\in\mathbb{R}$, auch für $y\le0$.
--- falsch
Als Umkehrfunktion $\log:\mathbb{R}^+\to\mathbb{R}$ von $\exp$. Es gilt $\exp(\log y)=y$ für alle $y\in\mathbb{R}^+$, aber $\log(\exp x)=x$ nur für $x>0$, weil $\log$ nur positive Zahlen verarbeitet.
:::
:::karte zusammenhang Logarithmus
Welche Zahl gibt $\log y$ an, und warum gibt es für $y\le0$ keinen Logarithmus?
---
$\log y$ ist der Exponent, mit dem man $\mathrm{e}$ potenzieren muss, um $y$ zu erhalten. Für $y\le0$ gibt es keinen, weil $\mathrm{e}^x$ diese Zahlen nie trifft: $\mathrm{e}^x>0$ für alle $x$.
--- falsch
$\log y$ ist der Exponent, mit dem man 10 potenzieren muss, um $y$ zu erhalten. Für $y\le0$ gibt es keinen, weil man die Zahl 10 dafür durch null teilen müsste.
--- falsch
$\log y$ ist der Bruchteil $y/\mathrm{e}$, also die Zahl, mit der man $\mathrm{e}$ multiplizieren muss, um $y$ zu erhalten. Für $y\le0$ wäre er nicht positiv und ist deshalb nicht erklärt.
--- falsch
$\log y$ ist der Exponent, mit dem man $\mathrm{e}$ potenzieren muss, um $y$ zu erhalten. Für $y\le0$ gibt es ihn auch, er ist dann negativ, etwa $\log\frac{1}{\mathrm{e}}=-1$.
:::
:::karte formel Funktionalgleichung des Logarithmus
Wie verwandelt der Logarithmus Produkte, Quotienten und Potenzen, und für welche Zahlen gilt das?
---
$\log(x\cdot y)=\log x+\log y$ und $\log\frac xy=\log x-\log y$ für alle $x,y\in\mathbb{R}^+$, außerdem $\log(x^n)=n\cdot\log x$ für $x\in\mathbb{R}^+$, $n\in\mathbb{N}$.
--- falsch
$\log(x\cdot y)=\log x\cdot\log y$ und $\log\frac xy=\frac{\log x}{\log y}$ für alle $x,y\in\mathbb{R}^+$, außerdem $\log(x^n)=(\log x)^n$ für $x\in\mathbb{R}^+$, $n\in\mathbb{N}$.
--- falsch
$\log(x+y)=\log x\cdot\log y$ und $\log(x-y)=\frac{\log x}{\log y}$ für alle $x>y>0$, außerdem $\log(x^n)=n\cdot\log x$ für $x\in\mathbb{R}^+$, $n\in\mathbb{N}$.
--- falsch
$\log(x\cdot y)=\log x+\log y$ und $\log\frac xy=\log x-\log y$ für alle $x,y\in\mathbb{R}$ mit $xy\ne0$, außerdem $\log(x^n)=n\cdot\log x$ für alle $x\ne0$, $n\in\mathbb{N}$.
:::
:::karte formel Wachstum des Logarithmus
Welche Gerade liegt über dem Logarithmus, und wie vergleicht sich sein Wachstum mit dem einer Wurzel?
---
$\log t\le t-1$ für alle $t>0$, gleichbedeutend $\log(1+x)\le x$ für alle $x>-1$. Außerdem ist $\log x<\sqrt[n]{x}<x$ für alle $x>(4n^2)^n$, $n\ge2$: $\log$ wächst schwächer als jede Wurzel.
--- falsch
$\log t\ge t-1$ für alle $t>0$: Der Logarithmus liegt über der Geraden. Außerdem wächst $\log$ schneller als jede Wurzel, weil er die Umkehrung der schnell wachsenden Exponentialfunktion ist.
--- falsch
$\log t\le t-1$ für alle $t>0$. Außerdem gilt $\log x<\sqrt[n]{x}$ nur für $n=2$; höhere Wurzeln wachsen so langsam, dass der Logarithmus sie für große $x$ überholt.
--- falsch
$\log t\le t-1$, aber nur für $t\ge1$; für $0<t<1$ liegt der Logarithmus über der Geraden. Außerdem gilt $\log x<\sqrt[n]{x}<x$ schon für alle $x>1$ und $n\ge2$.
:::
:::karte herleitung Funktionalgleichung des Logarithmus
Wie folgt $\log(x\cdot y)=\log x+\log y$ aus der Funktionalgleichung der Exponentialfunktion, und wie die Regel für Quotienten?
---
Man setzt $u=\log x$, $v=\log y$, also $x=\mathrm{e}^u$ und $y=\mathrm{e}^v$, weil $\exp(\log y)=y$ für $y\in\mathbb{R}^+$ gilt.
---
Dann ist $\log(xy)=\log(\mathrm{e}^u\mathrm{e}^v)=\log(\mathrm{e}^{u+v})=u+v$, weil $\mathrm{e}^{u+v}=\mathrm{e}^u\mathrm{e}^v$ und $\log(\exp x)=x$ gilt.
---
Aus $0=\log\frac yy=\log y+\log\frac1y$ folgt $\log\frac1y=-\log y$, weil $\log1=0$ ist.
---
Damit ist $\log\frac xy=\log x+\log\frac1y=\log x-\log y$, weil der Quotient das Produkt von $x$ mit $\frac1y$ ist.
:::
:::karte begriff allgemeine Potenz
Wie ist die allgemeine Potenz $a^x$ für $a>0$ und reelles $x$ definiert?
---
$a^x:=\mathrm{e}^{x\cdot\log a}$; die Funktion $x\mapsto a^x$ heißt allgemeine Potenzfunktion von $\mathbb{R}$ nach $\mathbb{R}^+$. Für rationales $x=\frac pq$ stimmt sie mit $a^{p/q}:=\sqrt[q]{a^p}$ überein.
--- falsch
$a^x:=\mathrm{e}^{x}\cdot\log a$; die Funktion $x\mapsto a^x$ ist ein festes Vielfaches der Exponentialfunktion. Für rationales $x=\frac pq$ stimmt sie mit $a^{p/q}:=\sqrt[q]{a^p}$ überein.
--- falsch
$a^x:=\mathrm{e}^{a\cdot\log x}$; die Funktion $x\mapsto a^x$ ist nur für $x>0$ erklärt und nimmt Werte in $\mathbb{R}^+$ an. Für rationales $x=\frac pq$ stimmt sie mit $\sqrt[q]{a^p}$ überein.
--- falsch
$a^x:=\mathrm{e}^{x\cdot\log a}$ für alle $a\in\mathbb{R}$, auch negative; die Funktion $x\mapsto a^x$ geht dann von $\mathbb{R}$ nach $\mathbb{R}$. Für rationales $x=\frac pq$ stimmt sie mit $\sqrt[q]{a^p}$ überein.
:::
:::karte formel Rechenregeln für Potenzen
Welche Rechenregeln gelten für die allgemeine Potenz mit $a,b>0$ und reellen Exponenten $x,y$?
---
$(a\cdot b)^x=a^x\cdot b^x$, $a^{x\cdot y}=(a^x)^y$, $a^{x+y}=a^x\cdot a^y$ und $\log(a^x)=x\cdot\log a$: Die Regeln für ganzzahlige Exponenten gelten jetzt für reelle.
--- falsch
$(a\cdot b)^x=a^x+b^x$, $a^{x\cdot y}=a^x\cdot a^y$, $a^{x+y}=(a^x)^y$ und $\log(a^x)=(\log a)^x$: Die Regeln für ganzzahlige Exponenten ändern sich bei reellen.
--- falsch
$(a\cdot b)^x=a^x\cdot b^x$, $a^{x\cdot y}=(a^x)^y$, $a^{x+y}=a^x\cdot a^y$, aber nur für rationale $x,y$; für irrationale Exponenten gibt es keine Rechenregeln.
--- falsch
$(a\cdot b)^x=a^x\cdot b^x$, $a^{x\cdot y}=a^x\cdot a^y$, $a^{x+y}=(a^x)^y$ und $\log(a^x)=x\cdot\log a$: Addition und Multiplikation im Exponenten tauschen die Rollen.
:::
:::karte zusammenhang positive Basis
Warum ist die allgemeine Potenz $a^x$ nur für $a>0$ erklärt?
---
Weil $\log a$ nur für $a>0$ existiert. Für $a<0$ ist nur ein Teil widerspruchsfrei erklärt: $(-8)^{1/3}=-2$, aber mit $\frac26=\frac13$ wäre $\sqrt[6]{(-8)^2}=2$.
--- falsch
Weil für $a<0$ jede Potenz $a^x$ negativ wäre und die Rechenregel $a^{x+y}=a^x\cdot a^y$ dann für alle Exponenten falsch würde, auch für ganzzahlige.
--- falsch
Weil für $a<0$ zwar alles widerspruchsfrei erklärt ist, man mit positiven Zahlen aber bequemer rechnet; $(-8)^{1/3}$ ist zum Beispiel eindeutig $-2$.
--- falsch
Weil $\mathrm{e}^x$ für negative $x$ nicht erklärt ist; für $a<0$ müsste man in $\mathrm{e}^{x\log a}$ einen negativen Exponenten einsetzen, und das geht nicht.
:::
::::
