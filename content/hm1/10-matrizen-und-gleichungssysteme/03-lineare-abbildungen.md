---
title: Stufe 1: Lineare Abbildungen
pfad: Elektrotechnik / 1. Semester / Höhere Mathematik 1 / Matrizen und lineare Gleichungssysteme
order: 1300300
summary: Die Teile 8 und 9 handeln von einzelnen Vektorräumen.
tags: strukturerhaltend, linear, Nullabbildung, Identität, Punktauswertung, Linearisierung, affin
lang: de
---

<span class="anker" id="stufe-1"></span>

:::zweck
Die [Teile 8](/wissen/elektrotechnik/1-semester/hohere-mathematik-1/vektoren-und-skalarprodukt/vektoren-und-skalarprodukt.html) und 9 handeln von einzelnen Vektorräumen. Jetzt geht es um Abbildungen zwischen ihnen. Nützlich sind nur solche, die Addieren und Strecken nicht zerstören.
:::

**Die Idee.** Eine Abbildung ist linear, wenn die Reihenfolge keine Rolle spielt: Erst addieren und dann abbilden ergibt dasselbe wie erst abbilden und dann addieren. Für das Strecken gilt das Gleiche. Ein Parallelogramm aus zwei Pfeilen geht deshalb in ein Parallelogramm über und seine Diagonale in dessen Diagonale (Abb. [1](#abb-1)). Solche Abbildungen heißen auch __strukturerhaltend__.

:::abbildung hm1/k10linear 1
Die Scherung $S$ erhält das Parallelogramm aus $a=(2,1)$ und $b=(-1,1)$: Das Bild der Diagonale $a+b$ ist die Diagonale aus $Sa$ und $Sb$.
:::

:::definition Definition 1.1 (Lineare Abbildung)
<span class="anker" id="satz-1-1"></span>

Seien $V$ und $W$ Vektorräume über demselben Körper $\mathbb K=\mathbb{R}$ oder $\mathbb{C}$. Eine Abbildung $L:V\to W$ heißt __linear__, wenn für alle $\alpha\in\mathbb K$ und $v,v_1,v_2\in V$ gilt:

<ul>

<li>

⁠**(L1)** $L(v_1+v_2)=L(v_1)+L(v_2)$,

</li>

<li>

⁠**(L2)** $L(\alpha v)=\alpha L(v)$.

</li>

</ul>

Die Menge aller linearen Abbildungen von $V$ nach $W$ heißt $\operatorname{Lin}(V,W)$.
:::

⁠**So liest man das:** Links in (L1) steht die Addition von $V$, rechts die von $W$. Statt $L(v)$ schreibt man oft $Lv$. Im Bild: $S(a+b)=S(1,2)=(3,2)$ und $Sa+Sb=(3,1)+(0,1)=(3,2)$.

**Beispiele.**

<ul>

<li>

$x\mapsto bx$ auf $\mathbb{R}$ ist linear, denn $b(\alpha x_1+x_2)=\alpha bx_1+bx_2$. Der Graph ist eine Gerade durch den Ursprung.

</li>

<li>

$x\mapsto x^2$ ist nicht linear: $(2\cdot3)^2=36$, aber $2\cdot3^2=18$.

</li>

<li>

$g:\mathbb{R}^2\to\mathbb{R}^2$, $g(u)=u+(1,2)$ ist nicht linear: $g(0)=(1,2)$, und $g(2u)\ne2g(u)$.

</li>

<li>

Die __Nullabbildung__ $v\mapsto0_W$ und die __Identität__ $\operatorname{Id}:V\to V$, $v\mapsto v$ sind linear.

</li>

<li>

Auf dem Raum $\mathcal P_2$ der Polynome vom Grad höchstens 2 ist die __Punktauswertung__ $p\mapsto p(2)$ linear, denn $(p+q)(2)=p(2)+q(2)$ gilt nach Definition der Summe von Funktionen.

</li>

</ul>

:::satz Satz 1.2 (Rechenregeln)
<span class="anker" id="satz-1-2"></span>

Sei $L:V\to W$ linear. Dann gilt:

<ol class="al">

<li>

$L(0_V)=0_W$ und $L(v-\tilde v)=L(v)-L(\tilde v)$ für alle $v,\tilde v\in V$;

</li>

<li>

$L(\lambda_1v_1+\dots+\lambda_nv_n)=\lambda_1L(v_1)+\dots+\lambda_nL(v_n)$ für alle $\lambda_i\in\mathbb K$, $v_i\in V$;

</li>

<li>

sind $v_1,\dots,v_n$ linear abhängig, so auch $L(v_1),\dots,L(v_n)$.

</li>

</ol>
:::

:::beweis Rechenregeln
(a) Es ist $0\cdot0_V=0_V$ (Zahl mal Vektor), also $L(0_V)=L(0\cdot0_V)=0\cdot L(0_V)=0_W$ nach (L2). Weiter ist $v-\tilde v=v+(-1)\tilde v$, also nach (L1), (L2) $L(v-\tilde v)=L(v)+(-1)L(\tilde v)=L(v)-L(\tilde v)$.

(b) Wiederholtes Anwenden von (L1) trennt die Summanden, (L2) zieht die Zahlen heraus.

(c) Abhängig heißt: $\lambda_1v_1+\dots+\lambda_nv_n=0_V$ mit $(\lambda_1,\dots,\lambda_n)\ne(0,\dots,0)$. Wendet man $L$ an, folgt aus (a) und (b) $\lambda_1L(v_1)+\dots+\lambda_nL(v_n)=0_W$ mit denselben Zahlen. Das ist eine nichttriviale Nullkombination der Bilder.
:::

⁠**So liest man das:** (b) ist das Prinzip dieses Kapitels. (c) sagt: Eine Abhängigkeit überlebt jede lineare Abbildung. Die Umkehrung ist falsch: Unabhängige Vektoren können abhängige Bilder haben. Bei der Presse sind $e_1,e_2$ unabhängig, ihre Bilder $(1,2)$ und $(2,4)$ nicht. **Grenzfall:** Die Nullabbildung macht jede Familie abhängig. **Warum linear nötig ist:** Für $g$ von oben ist $g(0)\ne0$.

⁠**Warum das zählt.** Die Tangente an den Graphen einer Funktion in $x_0$ ist $x\mapsto y_0+b(x-x_0)$, also eine verschobene lineare Abbildung mit der Steigung $b$. Nahe bei $x_0$ ersetzt sie die Funktion (__Linearisierung__). Deshalb reicht die lineare Theorie weit über Geraden hinaus.

:::frage Heißt $f(x)=2x+1$ nicht „lineare Funktion“?
Im Schulsinn ja, dort meint das Wort „der Graph ist eine Gerade“. Im Sinn von (L1), (L2) nein, denn $f(0)=1\ne0$. Eine lineare Abbildung plus eine feste Verschiebung heißt __affin__.
:::

:::aufgabe Aufgabe 1 ★ Linear oder nicht
<span class="anker" id="aufg-1"></span>

Entscheide und gib bei „nein“ ein Gegenbeispiel mit Zahlen an: (a) $L(x_1,x_2)=(x_1-x_2,\ 3x_1)$; (b) $f(x_1,x_2)=x_1x_2$; (c) $k(x)=|x|$ auf $\mathbb{R}$; (d) $h(p)=p(0)+p(1)$ auf $\mathcal P_2$.

:::loesung
(a) Linear, denn $L$ gehört zur Matrix $\bigl(\begin{smallmatrix}1&-1\\3&0\end{smallmatrix}\bigr)$. (b) Nein: $f(2,2)=4$, aber $2f(1,1)=2$. (c) Nein: $k(-1)=1$, aber $-k(1)=-1$. (d) Linear: $h(\alpha p+q)=\alpha p(0)+q(0)+\alpha p(1)+q(1)=\alpha h(p)+h(q)$, weil Summen von Funktionen punktweise erklärt sind.
:::
:::
