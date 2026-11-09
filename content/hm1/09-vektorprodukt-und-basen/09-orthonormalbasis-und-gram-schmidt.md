---
title: Stufe 7: Orthonormalbasis und Gram-Schmidt
pfad: Elektrotechnik / 1. Semester / Höhere Mathematik 1 / Vektorprodukt und Basen
order: 1290900
summary: Koordinaten in einer schiefen Basis verlangen ein Gleichungssystem.
tags: Orthonormalbasis, Normierungsschritt
lang: de
---

<span class="anker" id="stufe-7"></span>

:::zweck
Koordinaten in einer schiefen Basis verlangen ein Gleichungssystem. In einer rechtwinkligen Basis genügt je ein Skalarprodukt. Diese Stufe zeigt das und baut eine solche Basis aus einer beliebigen.
:::

**Die Idee.** Das Skalarprodukt mit $\vec v_j$ blendet alles aus, was senkrecht zu $\vec v_j$ steht. Aus $\sum_i\alpha_i\vec v_i$ überlebt also nur $\alpha_j$. Um eine solche Basis zu bauen, zieht man von jedem neuen Vektor den Teil ab, der in den fertigen Richtungen liegt. Das ist die Projektion, und der Rest steht nach Satz [4.4](orthonormalsysteme-und-projektion.html#satz-4-4) senkrecht (Abb. [7](#abb-7)).

:::satz Satz 7.1 (Darstellungssatz)
<span class="anker" id="satz-7-1"></span>

Ist $\mathcal B=(\vec v_1,\dots,\vec v_n)$ ein Orthonormalsystem in $V=\mathbb{R}^n$, dann ist $\mathcal B$ auch Basis von $V$, und jedes $\vec x\in V$ hat die eindeutige Darstellung

<span class="anker" id="gl-7-1"></span>
$$\vec x=\sum_{i=1}^n\langle\vec x,\vec v_i\rangle\,\vec v_i. \tag{7.1}$$
:::

⁠**So liest man das:** Der Koordinatenvektor ist $\vec x_{\mathcal B}=(\langle\vec x,\vec v_1\rangle,\dots,\langle\vec x,\vec v_n\rangle)$, jede Koordinate ist ein einziges Skalarprodukt. Im Modell: $\vec x=3\vec f_1-3\vec f_2+3\vec f_3$, Probe $\|\vec x\|^2=27=9+9+9$. **Voraussetzung:** Es müssen $n$ Vektoren sein. Die Projektion [(4.5)](orthonormalsysteme-und-projektion.html#gl-4-5) ist dieselbe Summe, nur vorzeitig abgebrochen: Ohne $\vec f_3$ fehlt der Rest $3\vec f_3$.

:::beweis Skalarprodukt mit $\vec v_j$
Unabhängig: Aus $\sum_\ell\alpha_\ell\vec v_\ell=\vec0$ folgt für jedes $j$ mit Linearität im ersten Eingang $0=\langle\sum_\ell\alpha_\ell\vec v_\ell,\vec v_j\rangle=\sum_\ell\alpha_\ell\langle\vec v_\ell,\vec v_j\rangle=\alpha_j$. Wegen $\dim\mathbb{R}^n=n$ ist $\mathcal B$ nach Satz [6.5](die-dimension.html#satz-6-5) (ii) eine Basis. Also hat jedes $\vec x$ eine eindeutige Darstellung $\vec x=\sum_ia_i\vec v_i$, und dieselbe Rechnung gibt $\langle\vec x,\vec v_j\rangle=a_j$.
:::

:::definition Definition 7.2 (Orthonormalbasis)
<span class="anker" id="satz-7-2"></span>

Ist $\mathcal B$ ein ONS von $V$ und zugleich eine Basis von $V$, heißt $\mathcal B$ __Orthonormalbasis__ (kurz ONB) von $V$.
:::

Eine ONB ist aus zwei Gründen günstig: [(7.1)](#gl-7-1) ist leicht zu berechnen, und die Projektion [(4.5)](orthonormalsysteme-und-projektion.html#gl-4-5) braucht eine ONB des Unterraums. Offen ist, woher man sie bekommt.

:::satz Satz 7.3 (Gram-Schmidt)
<span class="anker" id="satz-7-3"></span>

Seien $\vec b_1,\dots,\vec b_m\in\mathbb{R}^n$ linear unabhängig. Mit

<span class="anker" id="gl-7-2"></span>
$$\vec c_1:=\frac1{\|\vec b_1\|}\vec b_1,\qquad\text{für }k=2,\dots,m:\quad\vec d_k:=\vec b_k-\sum_{i=1}^{k-1}\langle\vec b_k,\vec c_i\rangle\,\vec c_i,\quad\vec c_k:=\frac1{\|\vec d_k\|}\vec d_k \tag{7.2}$$

bilden $\vec c_1,\dots,\vec c_m$ ein ONS, und es gilt $\operatorname{span}\{\vec b_1,\dots,\vec b_m\}=\operatorname{span}\{\vec c_1,\dots,\vec c_m\}$.
:::

⁠**So liest man das:** Der __Normierungsschritt__ teilt durch die Länge. Der Schritt davor ist genau $\vec d_k=\vec b_k-\operatorname{Proj}_{\operatorname{span}\{\vec c_1,\dots,\vec c_{k-1}\}}(\vec b_k)$. Warum genau die Projektion? Zieht man weniger ab, bleibt ein Anteil längs eines $\vec c_i$, zieht man mehr ab, entsteht er mit anderem Vorzeichen. Nur bei der Projektion ist der Rest senkrecht zu allen fertigen Richtungen.

:::abbildung hm1/k9gs 7
Ein Gram-Schmidt-Schritt für $\vec b_1=\vec a=(3,1)$, $\vec b_2=\vec b=(1,2)$. Links: $\vec c_1$ ist $\vec a$ auf Länge 1 gestaucht. Mitte: Von $\vec b$ wird die Projektion auf $\vec c_1$ abgezogen, der Rest $\vec d_2=(-\frac12,\frac32)$ steht senkrecht. Rechts: Nach dem Normieren bilden $\vec c_1,\vec c_2$ ein ONS.
:::

:::beweis Induktion über $k$
Behauptet wird: $\vec c_1,\dots,\vec c_k$ sind definiert, orthonormal, und ihr Aufspann ist $\operatorname{span}\{\vec b_1,\dots,\vec b_k\}$. Für $k=1$ gilt das, denn $\vec b_1\ne\vec0$. Schritt $k-1\to k$:

⁠**Definiert.** Wäre $\vec d_k=\vec0$, läge $\vec b_k$ in $\operatorname{span}\{\vec c_1,\dots,\vec c_{k-1}\}=\operatorname{span}\{\vec b_1,\dots,\vec b_{k-1}\}$, ein Widerspruch zur Unabhängigkeit.

⁠**Orthonormal.** $\|\vec c_k\|=1$ gilt nach Konstruktion. Für $\ell<k$ ist mit der Linearität im ersten Eingang und $\langle\vec c_i,\vec c_\ell\rangle=\delta_{i\ell}$ für $i,\ell\le k-1$

$$\langle\vec c_k,\vec c_\ell\rangle=\frac1{\|\vec d_k\|}\Bigl[\langle\vec b_k,\vec c_\ell\rangle-\sum_{i=1}^{k-1}\langle\vec b_k,\vec c_i\rangle\langle\vec c_i,\vec c_\ell\rangle\Bigr]=\frac1{\|\vec d_k\|}\bigl[\langle\vec b_k,\vec c_\ell\rangle-\langle\vec b_k,\vec c_\ell\rangle\bigr]=0.$$

⁠**Gleicher Aufspann.** „$\subset$“: Nach [(7.2)](#gl-7-2) ist $\vec b_k=\|\vec d_k\|\vec c_k+\sum_i\langle\vec b_k,\vec c_i\rangle\vec c_i\in\operatorname{span}\{\vec c_1,\dots,\vec c_k\}$. „$\supset$“: $\vec c_k=\frac1{\|\vec d_k\|}\bigl(\vec b_k-\sum_i\langle\vec b_k,\vec c_i\rangle\vec c_i\bigr)$ liegt in $\operatorname{span}\{\vec b_1,\dots,\vec b_k\}$, denn die $\vec c_i$ mit $i<k$ liegen nach Induktionsvoraussetzung in $\operatorname{span}\{\vec b_1,\dots,\vec b_{k-1}\}$.
:::

::::beispiel
Für $(\vec a,\vec b)$: $\vec c_1=\frac1{\sqrt{10}}(3,1)$, $\langle\vec b,\vec c_1\rangle=\frac5{\sqrt{10}}$, $\vec d_2=(1,2)-\frac12(3,1)=(-\frac12,\frac32)$, $\|\vec d_2\|^2=\frac52$, $\vec c_2=\frac1{\sqrt{10}}(-1,3)$. Die Koordinaten von $(5,0)$ sind nun Skalarprodukte: $\frac{15}{\sqrt{10}}$ und $-\frac5{\sqrt{10}}$, Probe $\frac{225+25}{10}=25$. **Die Reihenfolge zählt:** Mit $(\vec b,\vec a)$ beginnt man mit $\frac1{\sqrt5}(1,2)$ und erhält als Rest $\vec a-\vec b=(2,-1)$. Das ONS ist also nicht eindeutig.
::::

⁠**Grenzfälle:** Ist $(\vec b_i)$ schon ein ONS, ändert das Verfahren nichts. Bei abhängiger Eingabe entsteht $\vec d_k=\vec0$: Für $\vec u,\vec v,\vec w=2\vec u-\vec v$ bricht es beim dritten Vektor ab.

:::frage Warum muss ich $\vec c_i$ benutzen und nicht $\vec b_i$?
Die Formel [(4.5)](orthonormalsysteme-und-projektion.html#gl-4-5) verlangt ein ONS. Die $\vec b_i$ sind weder normiert noch senkrecht, wie das Gegenbeispiel in Stufe [4](orthonormalsysteme-und-projektion.html#stufe-4) zeigt. Mit nicht normierten, aber senkrechten $\vec d_i$ ginge es auch, wenn man wie in [Teil 8](/wissen/elektrotechnik/1-semester/hohere-mathematik-1/vektoren-und-skalarprodukt/vektoren-und-skalarprodukt.html) durch $\|\vec d_i\|^2$ teilt.
:::

:::aufgabe Aufgabe 8 ★★ Gram-Schmidt im Raum
<span class="anker" id="aufg-8"></span>

Sei $\vec b_1=(1,1,0)$, $\vec b_2=(1,0,1)$, $\vec b_3=(0,1,1)$. (a) Bestimme mit [(7.2)](#gl-7-2) eine ONB des $\mathbb{R}^3$. (b) Bestimme die Koordinaten von $\vec y=(1,2,3)$ bezüglich dieser ONB und mache die Probe mit $\|\vec y\|^2$.

:::loesung
(a) $\vec c_1=\frac1{\sqrt2}(1,1,0)$. $\vec d_2=\vec b_2-\frac12(1,1,0)=(\frac12,-\frac12,1)$, $\vec c_2=\frac1{\sqrt6}(1,-1,2)$. $\vec d_3=\vec b_3-\frac12(1,1,0)-\frac16(1,-1,2)=(-\frac23,\frac23,\frac23)$, $\vec c_3=\frac1{\sqrt3}(-1,1,1)$. Nach Satz [7.1](#satz-7-1) ist das eine ONB. (b) $\frac3{\sqrt2}$, $\frac5{\sqrt6}$, $\frac4{\sqrt3}$. Probe: $\frac92+\frac{25}6+\frac{16}3=14=\|\vec y\|^2$.
:::
:::
