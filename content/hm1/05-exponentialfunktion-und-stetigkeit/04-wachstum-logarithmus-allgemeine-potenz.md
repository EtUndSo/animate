---
title: Stufe 2: Wachstum, Logarithmus, allgemeine Potenz
pfad: Elektrotechnik / 1. Semester / Höhere Mathematik 1 / Exponentialfunktion und Stetigkeit
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

(v) Nach (i) ist $0<\mathrm{e}^{-n}=\frac1{\mathrm{e}^n}\le\frac1{1+n}$, und das ist eine Majorante ([Teil 4](/wissen/elektrotechnik/1-semester/hohere-mathematik-1/folgen-und-grenzwerte/folgen-und-grenzwerte.html)).
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
(i) Monotonie vererbt sich auf die Umkehrfunktion ([Teil 3](/wissen/elektrotechnik/1-semester/hohere-mathematik-1/funktionen-und-polynome/funktionen-und-polynome.html)). (ii) Mit $u=\log x$, $v=\log y$ ist $\log(xy)=\log(\mathrm{e}^u\mathrm{e}^v)=\log(\mathrm{e}^{u+v})=u+v$. Aus $0=\log\frac yy=\log y+\log\frac1y$ folgt $\log\frac1y=-\log y$ und damit die zweite Formel. (iii) Induktion mit (ii). (iv) Aus $0<1+x\le\mathrm{e}^x$ folgt mit (i) und [(2.1)](#gl-2-1) $\log(1+x)\le x$. (v) Setze $y=\sqrt[n]{x}$, also $y>4n^2$ und $y^n=x$. Satz [2.1](#satz-2-1) (iv) gibt $\mathrm{e}^y>y^n=x$, Anwenden von $\log$ gibt $y>\log x$. Und $y<x$ gilt, weil $x>1$ und $n\ge2$ ist.
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

⁠**So liest man das:** Die Regeln aus [Teil 1](/wissen/elektrotechnik/1-semester/hohere-mathematik-1/mengen-logik-und-reelle-zahlen/mengen-logik-und-reelle-zahlen.html) gelten jetzt für reelle Exponenten.

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
