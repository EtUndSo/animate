---
title: Stufe 5: Die Basis
pfad: Elektrotechnik / 1. Semester / Höhere Mathematik 1 / Vektorprodukt und Basen
order: 1290700
summary: Bisher waren Linearkombinationen Beispiele.
tags: Basis, Koordinaten, Koordinatenvektor, Standardbasis
lang: de
---

<span class="anker" id="stufe-5"></span>

:::zweck
Bisher waren Linearkombinationen Beispiele. Diese Stufe sagt, wann eine Liste von Vektoren als Koordinatensystem taugt: Jeder Vektor muss sich aus ihr bauen lassen, und zwar auf genau eine Weise.
:::

**Die Idee.** Koordinaten sind eine Adresse: $(5,0)=2\vec a-\vec b$ heißt zwei Schritte längs $\vec a$, ein Schritt rückwärts längs $\vec b$ (Abb. [5](#abb-5)). Eine Adresse taugt, wenn jeder Punkt eine hat und kein Punkt zwei.

:::abbildung hm1/k9basis 5
Derselbe Vektor in zwei Koordinatensystemen. Links die Standardbasis: $(5,0)=5\vec e_1+0\,\vec e_2$. Rechts die Basis $(\vec a,\vec b)$ mit schiefem Gitter: $(5,0)=2\vec a-\vec b$, die Koordinaten sind $2,-1$. Der Punkt ist derselbe, nur die Adresse wechselt.
:::

:::definition Definition 5.1 (Basis)
<span class="anker" id="satz-5-1"></span>

Sei $V$ ein Vektorraum über $\mathbb K$, $n\in\mathbb{N}$ fest und $\mathcal B=(\vec b_1,\dots,\vec b_n)\in V\times\dots\times V$ ein geordnetes $n$-Tupel von Vektoren. Dann heißt $\mathcal B$ eine __Basis__ von $V$, wenn es zu jedem $\vec a\in V$ eindeutig bestimmte $\alpha_1,\dots,\alpha_n\in\mathbb K$ gibt mit

<span class="anker" id="gl-5-1"></span>
$$\vec a=\alpha_1\vec b_1+\dots+\alpha_n\vec b_n. \tag{5.1}$$

Die Zahlen $\alpha_1,\dots,\alpha_n$ heißen __Koordinaten__ von $\vec a$ bezüglich $\mathcal B$, und $\vec a_{\mathcal B}:=(\alpha_1,\dots,\alpha_n)$ heißt __Koordinatenvektor__.
:::

⁠**So liest man das:** „Geordnet“ heißt, dass die Reihenfolge zählt: In $(\vec b,\vec a)$ tauschen die Koordinaten die Plätze. „Eindeutig“ heißt, dass jeder Vektor genau eine Adresse hat. **Beispiel:** $(\vec e_1,\dots,\vec e_n)$ ist die __Standardbasis__ des $\mathbb{R}^n$: Es gilt $\vec a=a_1\vec e_1+\dots+a_n\vec e_n$, und aus $\sum_j\alpha_j\vec e_j=\vec a$ folgt Stelle für Stelle $\alpha_j=a_j$. Dort sind Koordinaten und Komponenten dasselbe.

:::satz Satz 5.2 (Charakterisierung)
<span class="anker" id="satz-5-2"></span>

$\mathcal B=(\vec b_1,\dots,\vec b_n)$ ist genau dann eine Basis von $V\ne\{\vec0\}$, wenn gilt:

<ol>

<li>

$V=\operatorname{span}\{\vec b_1,\dots,\vec b_n\}$, das heißt $\vec b_1,\dots,\vec b_n$ sind ein Erzeugendensystem von $V$,

</li>

<li>

$\vec b_1,\dots,\vec b_n$ sind linear unabhängig.

</li>

</ol>
:::

⁠**So liest man das:** (1) ist die Existenz der Adresse, (2) ihre Eindeutigkeit. Lineare Unabhängigkeit ([Teil 8](/wissen/elektrotechnik/1-semester/hohere-mathematik-1/vektoren-und-skalarprodukt/vektoren-und-skalarprodukt.html)) ist die Eindeutigkeit für den Nullvektor, und das reicht schon für alle Vektoren.

:::beweis Zwei Richtungen
„$\Rightarrow$“: Nach [(5.1)](#gl-5-1) lässt sich jedes $\vec a\in V$ aus den $\vec b_j$ bauen, also gilt (1). Für (2) sei $\sum_j\alpha_j\vec b_j=\vec0$. Es gilt auch $\vec0=\sum_j0\cdot\vec b_j$. Wegen der Eindeutigkeit ist $\alpha_1=\dots=\alpha_n=0$.

„$\Leftarrow$“: Nach (1) hat jedes $\vec a\in V$ eine Darstellung $\vec a=\sum_i\alpha_i\vec b_i$. Wäre auch $\vec a=\sum_i\beta_i\vec b_i$, ergäbe die Differenz $\vec0=\sum_i(\alpha_i-\beta_i)\vec b_i$. Wegen (2) ist $\alpha_i=\beta_i$ für alle $i$.
:::

**Beispiel.** $(\vec a,\vec b)$ ist eine Basis des $\mathbb{R}^2$. Unabhängig: Aus $s\vec a+t\vec b=\vec0$, also $3s+t=0$ und $s+2t=0$, folgt $s=t=0$. Erzeugend: Für jedes $\vec y=(y_1,y_2)$ ist $\vec y=\frac{2y_1-y_2}5\vec a+\frac{3y_2-y_1}5\vec b$. Der Vektor $(5,0)$ hat den Koordinatenvektor $(5,0)$ bezüglich der Standardbasis und $(2,-1)$ bezüglich $(\vec a,\vec b)$. **Beide Voraussetzungen sind nötig:** $(\vec a)$ ist unabhängig, erzeugt aber $(5,0)$ nicht. $(\vec a,\vec b,\vec a+\vec b)$ erzeugt, ist aber abhängig: $(4,3)=1\vec a+1\vec b+0(\vec a+\vec b)=0\vec a+0\vec b+1(\vec a+\vec b)$ hat zwei Adressen.

**Der Zahlbereich zählt.** $(\vec e_1,\dots,\vec e_n)$ ist auch Basis von $\mathbb{C}^n$ über $\mathbb K=\mathbb{C}$, dasselbe Argument mit $a_j,\alpha_j\in\mathbb{C}$. Über $\mathbb K=\mathbb{R}$ ist sie keine: $(\mathrm{i},1)\in\mathbb{C}^2$ hat keine Darstellung $\alpha_1\vec e_1+\alpha_2\vec e_2$ mit reellen $\alpha_j$. Setzt man $\vec b_j:=\mathrm{i}\,\vec e_j$, ist $(\vec e_1,\dots,\vec e_n,\vec b_1,\dots,\vec b_n)$ eine Basis von $\mathbb{C}^n$ über $\mathbb{R}$, denn jedes $\vec a\in\mathbb{C}^n$ hat die Darstellung $\vec a=\sum_j\operatorname{Re}(a_j)\vec e_j+\sum_j\operatorname{Im}(a_j)\vec b_j$ mit eindeutigen reellen Koordinaten. Das ist der Zeiger der Wechselstromrechnung: Eine komplexe Zahl trägt zwei reelle.

:::frage Ändert sich der Vektor, wenn ich die Basis wechsle?
Nein. Der Vektor bleibt derselbe, nur seine Koordinaten ändern sich. Das ist die Stolperstelle: Der Koordinatenvektor $(2,-1)$ bezüglich $(\vec a,\vec b)$ meint den Vektor $(5,0)$, nicht den Vektor $(2,-1)$ der Standardbasis.
:::

:::aufgabe Aufgabe 6 ★ Koordinaten
<span class="anker" id="aufg-6"></span>

(a) Zeige, dass $\vec c=(2,1)$, $\vec d=(1,3)$ eine Basis des $\mathbb{R}^2$ bilden, und bestimme die Koordinaten von $(4,7)$. (b) Warum ist $((1,2),(-2,-4))$ keine Basis? Welcher Teil von Satz [5.2](#satz-5-2) scheitert? (c) Gib die Koordinaten von $(1+2\mathrm{i},-\mathrm{i})\in\mathbb{C}^2$ über $\mathbb{R}$ bezüglich $(\vec e_1,\vec e_2,\mathrm{i}\vec e_1,\mathrm{i}\vec e_2)$ an.

:::loesung
(a) Unabhängig, denn $s(2,1)+t(1,3)=\vec0$ gibt $2s+t=0$, $s+3t=0$, also $s=t=0$. Erzeugend: $\vec y=\frac{3y_1-y_2}5\vec c+\frac{2y_2-y_1}5\vec d$. Für $(4,7)$ gilt $(1,2)$: $(2,1)+2(1,3)=(4,7)$. (b) $(-2,-4)=-2(1,2)$: Unabhängigkeit fehlt, und erzeugt wird nur eine Gerade. Beide Teile scheitern. (c) $(1,0,2,-1)$, denn $1+2\mathrm{i}=1\cdot1+2\cdot\mathrm{i}$ und $-\mathrm{i}=0\cdot1+(-1)\cdot\mathrm{i}$.
:::
:::
