---
title: Stufe 4: Lineare Unabhängigkeit
pfad: Elektrotechnik / 1. Semester / Höhere Mathematik 1 / Vektoren und Skalarprodukt
order: 1280600
summary: In einem Erzeugendensystem kann ein Vektor überflüssig sein: vec f liegt schon in span\ vec c,vec d\ .
tags: linear abhängig, linear unabhängig, nichttriviale Linearkombination, triviale, Ebene
lang: de
---

<span class="anker" id="stufe-4"></span>

:::zweck
In einem Erzeugendensystem kann ein Vektor überflüssig sein: $\vec f$ liegt schon in $\operatorname{span}\{\vec c,\vec d\}$. Diese Stufe macht aus „überflüssig“ ein Rechenkriterium.
:::

**Die Idee.** Überflüssig heißt: Ein Vektor lässt sich aus den anderen bauen, hier $\vec f=2\vec c-\vec d$. Bringt man alles auf eine Seite, entsteht $2\vec c-\vec d-\vec f=\vec0$. In dieser Form ist kein Vektor bevorzugt. Sie zeigt den Mechanismus: Man erreicht $\vec0$, obwohl nicht alle Koeffizienten null sind. Das geht genau dann, wenn einer der Vektoren überflüssig ist, denn jede solche Gleichung lässt sich nach einem Vektor mit Koeffizient $\ne0$ auflösen. Geometrisch liegen $\vec c,\vec d,\vec f$ in einer Ebene durch $O$ (Abb. [5](#abb-5)).

:::definition Definition 4.1 (Lineare Abhängigkeit)
<span class="anker" id="satz-4-1"></span>

Sei $V$ Vektorraum über dem Körper $\mathbb K$. Die Vektoren $\vec a_1,\dots,\vec a_n\in V$ heißen __linear abhängig__, falls es $(\alpha_1,\dots,\alpha_n)\in\mathbb K^n\setminus\{(0,\dots,0)\}$ gibt mit

<span class="anker" id="gl-4-1"></span>
$$\alpha_1\cdot\vec a_1+\alpha_2\cdot\vec a_2+\dots+\alpha_n\cdot\vec a_n=\vec0. \tag{4.1}$$

Ist das nicht der Fall, heißen $\vec a_1,\dots,\vec a_n$ __linear unabhängig__.
:::

⁠**So liest man das:** [(4.1)](#gl-4-1) sagt, dass sich $\vec0$ als __nichttriviale Linearkombination__ darstellen lässt, also mit mindestens einem Koeffizienten $\ne0$. Die __triviale__ Kombination mit lauter Nullen ergibt immer $\vec0$ und sagt nichts. Ist in [(4.1)](#gl-4-1) $\alpha_j\ne0$, darf man teilen, denn $\mathbb K$ ist ein Körper:

<span class="anker" id="gl-4-2"></span>
$$\vec a_j=-\sum_{i=1,\,i\ne j}^n\Bigl(\frac{\alpha_i}{\alpha_j}\Bigr)\cdot\vec a_i. \tag{4.2}$$

Für $(\alpha_1,\alpha_2,\alpha_3)=(2,-1,-1)$ gibt $j=3$ wieder $\vec f=2\vec c-\vec d$.

:::satz Satz 4.2 (Kriterium)
<span class="anker" id="satz-4-2"></span>

$\vec a_1,\dots,\vec a_n\in V$ sind genau dann linear unabhängig, wenn gilt:

<span class="anker" id="gl-4-3"></span>
$$\Bigl[\alpha_1\cdot\vec a_1+\dots+\alpha_n\cdot\vec a_n=\vec0\implies\alpha_1=\alpha_2=\dots=\alpha_n=0\Bigr]. \tag{4.3}$$
:::

⁠**So liest man das:** Der Nullvektor lässt sich nur trivial darstellen. In $\mathbb{R}^n$ ist [(4.3)](#gl-4-3) ein Gleichungssystem mit einer Gleichung je Komponente.

:::beweis Verneinung
Die Verneinung von [(4.1)](#gl-4-1) lautet: Für alle $(\alpha_1,\dots,\alpha_n)\ne(0,\dots,0)$ ist $\sum_i\alpha_i\vec a_i\ne\vec0$. Das ist [(4.3)](#gl-4-3) von hinten gelesen: Ist die Summe $\vec0$, kann das Tupel nicht von $(0,\dots,0)$ verschieden sein.
:::

:::satz Satz 4.3 (Linear unabhängige Vektoren)
<span class="anker" id="satz-4-3"></span>

Sei $V$ Vektorraum über $\mathbb K$.

<ol class="rm">

<li>

$\vec v$ ist linear unabhängig genau dann, wenn $\vec v\ne\vec0$.

</li>

<li>

$\vec v_1$ und $\vec v_2$ sind linear unabhängig genau dann, wenn keiner ein Vielfaches des anderen ist, das heißt $\vec v_1\ne\lambda\vec v_2$ und $\vec v_2\ne\mu\vec v_1$ für alle $\lambda,\mu\in\mathbb K$.

</li>

<li>

$\vec v_1,\dots,\vec v_n\in V$ sind linear unabhängig genau dann, wenn keiner der Vektoren $\vec v_i$ Linearkombination der übrigen ist.

</li>

</ol>
:::

⁠**So liest man das:** (iii) ist der Satz „keiner lässt sich aus den anderen bauen“, (i) und (ii) sind die Fälle $n=1$ und $n=2$. In (ii) reicht nicht eine der beiden Ungleichungen: Für $\vec v_1=\vec0$, $\vec v_2\ne\vec0$ ist $\vec v_2$ kein Vielfaches von $\vec v_1$, aber $\vec v_1=0\cdot\vec v_2$. **Grenzfall:** $\vec0$ und $\vec a$ sind immer linear abhängig, denn $1\cdot\vec0+0\cdot\vec a=\vec0$.

:::beweis Abhängigkeit und Bauen
(i) $\vec v=\vec0$ ist abhängig, denn $1\cdot\vec0=\vec0$. Sei $\vec v\ne\vec0$ und $\alpha\vec v=\vec0$. Wäre $\alpha\ne0$, folgte mit (V4), (V3) und Satz [2.3](der-vektorraum.html#satz-2-3) $\vec v=1\cdot\vec v=\frac1\alpha(\alpha\vec v)=\frac1\alpha\vec0=\vec0$, ein Widerspruch. Also ist $\alpha=0$.

(iii) Gezeigt wird die Verneinung: abhängig $\iff$ einer ist Linearkombination der übrigen. „$\Rightarrow$“: Das ist [(4.2)](#gl-4-2). „$\Leftarrow$“: Aus $\vec v_j=\sum_{i\ne j}\alpha_i\vec v_i$ folgt $\alpha_1\vec v_1+\dots+\alpha_{j-1}\vec v_{j-1}-\vec v_j+\alpha_{j+1}\vec v_{j+1}+\dots+\alpha_n\vec v_n=\vec0$. Mit $\alpha_j:=-1\ne0$ ist das [(4.1)](#gl-4-1).

(ii) ist (iii) für $n=2$: Linearkombination des einen anderen heißt Vielfaches.
:::

:::abbildung hm1/k8abhaengig 5
Die Vektoren $\vec c$, $\vec d$ und $\vec f=2\vec c-\vec d$ liegen in einer Ebene durch $O$ und sind linear abhängig. Der Weg $2\vec c$, dann $-\vec d$ führt zur Spitze von $\vec f$. Der Vektor $(0,0,2)$ ragt aus der Ebene heraus, darum sind $\vec c$, $\vec d$, $(0,0,2)$ linear unabhängig.
:::

**Beispiel.** $\vec c$ und $\vec d$ sind linear unabhängig: $s\vec c+t\vec d=(2s,s+t,2t)=\vec0$ erzwingt mit der ersten Komponente $s=0$, mit der dritten $t=0$. Dagegen ist $2\vec c-\vec d-\vec f=\vec0$ eine nichttriviale Kombination. Für die Polynome gilt $p+q-r=0$, also ist $\operatorname{span}\{p,q,r\}=\operatorname{span}\{p,q\}$. Die Polynome $1,x,x^2$ sind linear unabhängig: Ist $\alpha_0+\alpha_1x+\alpha_2x^2=0$ für alle $x$, folgt aus dem Identitätssatz ([Teil 3](/wissen/elektrotechnik/1-semester/hohere-mathematik-1/funktionen-und-polynome/funktionen-und-polynome.html)) $\alpha_0=\alpha_1=\alpha_2=0$.

**Ebenen.** Zwei linear unabhängige Richtungen spannen eine Ebene auf.

:::definition Definition 4.4 (Ebene)
<span class="anker" id="satz-4-4"></span>

Sind $\vec u,\vec v\in\mathbb{R}^n$ linear unabhängig und $\vec p\in\mathbb{R}^n$, so heißt

<span class="anker" id="gl-4-4"></span>
$$E=\{\vec w\in\mathbb{R}^n:\ \vec w=\vec p+s\cdot\vec u+t\cdot\vec v\ \text{ mit }s,t\in\mathbb{R}\} \tag{4.4}$$

die von $\vec u$ und $\vec v$ aufgespannte __Ebene__ durch den Punkt $P$ (mit $\vec p=\overrightarrow{OP}$). Die Gleichung $\vec w=\vec p+s\vec u+t\vec v$ ($s,t\in\mathbb{R}$) heißt Parameterdarstellung von $E$.
:::

⁠**So liest man das:** $E$ hat zwei Richtungsvektoren und liegt in $\mathbb{R}^n$ mit $n\ge2$, für $n=2$ ist $E=\mathbb{R}^2$. Mit $\vec p=(1,0,0)$, $\vec u=\vec c$, $\vec v=\vec d$ gibt $s=1$, $t=2$ den Punkt $(3,3,4)$. **Voraussetzung nötig:** Für $\vec v=2\vec u$ ist $s\vec u+t\vec v=(s+2t)\vec u$. Es bleibt nur eine Gerade.

:::frage Wenn keiner ein Vielfaches eines anderen ist, sind die Vektoren dann unabhängig?
Für zwei Vektoren ja, für drei nicht. $\vec c,\vec d,\vec f$ sind paarweise linear unabhängig und zusammen abhängig. Abhängigkeit kann mehrere Vektoren zugleich betreffen, deshalb verlangt Satz [4.3](#satz-4-3) (iii) einen Test gegen *alle* übrigen.
:::

:::aufgabe Aufgabe 5 ★★ Abhängig oder unabhängig
<span class="anker" id="aufg-5"></span>

Entscheide und gib bei Abhängigkeit eine nichttriviale Kombination an: (a) $(1,2,3)$, $(2,4,7)$; (b) $(1,0,1)$, $(0,1,1)$, $(1,1,2)$; (c) $(1,0,1)$, $(0,1,1)$, $(1,1,0)$; (d) die Polynome $1+x$, $1-x$, $2$; (e) $(1,i)$, $(i,-1)$ in $\mathbb{C}^2$, einmal über $\mathbb K=\mathbb{C}$ und einmal über $\mathbb K=\mathbb{R}$.

:::loesung
(a) Unabhängig: $\alpha+2\beta=0$ und $3\alpha+7\beta=0$ geben $\beta=0$, dann $\alpha=0$. (b) Abhängig: $(1,0,1)+(0,1,1)-(1,1,2)=\vec0$. (c) Unabhängig: $\alpha+\gamma=0$, $\beta+\gamma=0$, $\alpha+\beta=0$ geben $\alpha=\beta=-\gamma$ und $2\alpha=0$. (d) Abhängig: $(1+x)+(1-x)-2=0$. (e) Über $\mathbb{C}$ abhängig, denn $i\cdot(1,i)=(i,-1)$, also $i(1,i)-(i,-1)=\vec0$. Über $\mathbb{R}$ unabhängig: $\alpha(1,i)+\beta(i,-1)=(\alpha+i\beta,\ i\alpha-\beta)=\vec0$ mit reellen $\alpha,\beta$ erzwingt in der ersten Komponente $\alpha=\beta=0$.
:::
:::
