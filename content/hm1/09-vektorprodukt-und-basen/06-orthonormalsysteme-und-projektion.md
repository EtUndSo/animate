---
title: Stufe 4: Orthonormalsysteme und Projektion
pfad: Elektrotechnik / 1. Semester / HöMa1 – Höhere Mathematik 1 / Vektorprodukt und Basen
adresse: elektrotechnik/1-semester/hohere-mathematik-1/vektorprodukt-und-basen
knoten: Kapitel 9: Vektorprodukt und Basen
order: 1290600
summary: Kapitel 8 projiziert auf eine Gerade und auf eine Hyperebene.
tags: Orthonormalsystem, orthonormal, Kronecker-Symbol, orthogonale Projektion, Lotraum
lang: de
---

<span class="anker" id="stufe-4"></span>

:::zweck
[Kapitel 8](/wissen/elektrotechnik/1-semester/hohere-mathematik-1/vektoren-und-skalarprodukt/vektoren-und-skalarprodukt.html) projiziert auf eine Gerade und auf eine Hyperebene. Diese Stufe projiziert auf jeden Unterraum, den senkrechte Einheitsvektoren aufspannen, und zeigt, warum das Ergebnis der nächste Punkt ist.
:::

**Die Idee.** Gesucht ist zu einem Punkt $P$ der nächste Punkt $Q$ eines Unterraums $U$ (Abb. [4](#abb-4)). Stehen die Richtungen von $U$ senkrecht, stören sie einander nicht: Der Abstand zerfällt in einen Beitrag je Richtung, und man optimiert jede Koordinate für sich.

:::definition Definition 4.1 (Orthonormalsystem)
<span class="anker" id="satz-4-1"></span>

Die Vektoren $\vec v_1,\dots,\vec v_k\in\mathbb{R}^n$ bilden ein __Orthonormalsystem__ (kurz ONS), sie heißen auch __orthonormal__, wenn für alle $i,j=1,\dots,k$ gilt

<span class="anker" id="gl-4-1"></span>
$$\langle\vec v_i,\vec v_j\rangle=\delta_{ij}:=\begin{cases}1&\text{für }i=j,\\0&\text{für }i\ne j.\end{cases} \tag{4.1}$$
:::

⁠**So liest man das:** $\delta_{ij}$ heißt __Kronecker-Symbol__. Die Fälle $i=j$ sagen „normiert“, also $\|\vec v_i\|=1$, die Fälle $i\ne j$ sagen „orthogonal“, also $\vec v_i\perp\vec v_j$. Die Einheitsvektoren $\vec e_1,\dots,\vec e_n$ bilden ein ONS, ebenso $\vec f_1,\vec f_2,\vec f_3$ aus dem Modell: $\langle\vec f_1,\vec f_2\rangle=\frac19(-2+4-2)=0$.

**Die Aufgabe.** Sei $\vec p=\overrightarrow{OP}\in\mathbb{R}^n$ und $U:=\operatorname{span}\{\vec v_1,\dots,\vec v_k\}$ mit einem ONS. Gesucht ist $\vec q\in U$ mit

<span class="anker" id="gl-4-2"></span>
$$\|\vec p-\vec q\|=\min_{\vec u\in U}\|\vec p-\vec u\|=:\operatorname{dist}(P,U). \tag{4.2}$$

Jedes Element von $U$ hat die Form $\sum_it_i\vec v_i$. Gesucht sind also $k$ Zahlen.

:::satz Satz 4.2 (Abstandsformel)
<span class="anker" id="satz-4-2"></span>

Sei $\vec p\in\mathbb{R}^n$, $\vec v_1,\dots,\vec v_k$ ein ONS im $\mathbb{R}^n$ und $t_1,\dots,t_k\in\mathbb{R}$ beliebig. Dann gilt

<span class="anker" id="gl-4-3"></span>
$$\Bigl\|\vec p-\sum_{i=1}^kt_i\vec v_i\Bigr\|^2=\|\vec p\|^2-\sum_{i=1}^k\langle\vec p,\vec v_i\rangle^2+\sum_{i=1}^k\bigl[t_i-\langle\vec p,\vec v_i\rangle\bigr]^2. \tag{4.3}$$
:::

⁠**So liest man das:** Nur die letzte Summe hängt von den $t_i$ ab, sie ist nie negativ und genau für $t_i=\langle\vec p,\vec v_i\rangle$ gleich 0. Also ist $\vec q:=\sum_i\langle\vec p,\vec v_i\rangle\vec v_i$ der einzige nächste Punkt, und es gilt

<span class="anker" id="gl-4-4"></span>
$$\operatorname{dist}(P,U)=\Bigl\|\vec p-\sum_{i=1}^k\langle\vec p,\vec v_i\rangle\vec v_i\Bigr\|. \tag{4.4}$$

:::beweis Ausmultiplizieren und quadratisch ergänzen
Mit Linearität und Symmetrie ([Kapitel 8](/wissen/elektrotechnik/1-semester/hohere-mathematik-1/vektoren-und-skalarprodukt/vektoren-und-skalarprodukt.html)) wird

$$\Bigl\|\vec p-\sum_it_i\vec v_i\Bigr\|^2=\Bigl\langle\vec p-\sum_it_i\vec v_i,\ \vec p-\sum_jt_j\vec v_j\Bigr\rangle=\langle\vec p,\vec p\rangle-2\sum_it_i\langle\vec p,\vec v_i\rangle+\sum_{i,j}t_it_j\langle\vec v_i,\vec v_j\rangle.$$

Wegen [(4.1)](#gl-4-1) bleibt von der Doppelsumme nur $\sum_it_i^2$. Hier zeigt sich der Mechanismus: Ohne Orthogonalität blieben gemischte Glieder $t_it_j$, und die Koordinaten wären gekoppelt. Quadratische Ergänzung $t_i^2-2t_i\langle\vec p,\vec v_i\rangle=(t_i-\langle\vec p,\vec v_i\rangle)^2-\langle\vec p,\vec v_i\rangle^2$ ergibt [(4.3)](#gl-4-3).
:::

:::definition Definition 4.3 (Orthogonale Projektion)
<span class="anker" id="satz-4-3"></span>

Sei $\vec p\in\mathbb{R}^n$, $\vec v_1,\dots,\vec v_k$ ein ONS und $U:=\operatorname{span}\{\vec v_1,\dots,\vec v_k\}$. Dann heißt

<span class="anker" id="gl-4-5"></span>
$$\operatorname{Proj}_U(\vec p)=P_U(\vec p):=\sum_{i=1}^k\langle\vec p,\vec v_i\rangle\,\vec v_i\in U \tag{4.5}$$

die __orthogonale Projektion__ von $\vec p$ auf $U$.
:::

:::satz Satz 4.4 (Eigenschaften der Projektion)
<span class="anker" id="satz-4-4"></span>

Für $\vec p$ und $U$ wie in der Definition gilt:

<ol class="al">

<li>

Es gilt $[\vec p-\operatorname{Proj}_U(\vec p)]\perp\vec u$ für alle $\vec u\in U$.

</li>

<li>

Für $\vec w_0\in U$ sind gleichwertig: (1) $\|\vec p-\vec w_0\|$ ist minimal unter allen $\|\vec p-\vec w\|$, $\vec w\in U$; (2) $\vec w_0=\operatorname{Proj}_U(\vec p)$; (3) $\vec p-\vec w_0\perp\vec v_j$ für alle $j=1,\dots,k$.

</li>

</ol>
:::

⁠**So liest man das:** Der Rest steht senkrecht auf ganz $U$, und daran erkennt man den nächsten Punkt. **Grenzfälle:** Für $k=1$ ist das die Projektion aus [Kapitel 8](/wissen/elektrotechnik/1-semester/hohere-mathematik-1/vektoren-und-skalarprodukt/vektoren-und-skalarprodukt.html) mit $\|\vec v\|=1$. Für $\vec p\in U$ ist der Rest $\vec0$.

:::beweis Skalarprodukt mit $\vec v_j$
(a): Mit [(4.5)](#gl-4-5) und [(4.1)](#gl-4-1) ist $\langle\vec p-\operatorname{Proj}_U(\vec p),\vec v_j\rangle=\langle\vec p,\vec v_j\rangle-\sum_i\langle\vec p,\vec v_i\rangle\langle\vec v_i,\vec v_j\rangle=\langle\vec p,\vec v_j\rangle-\langle\vec p,\vec v_j\rangle=0$. Jedes $\vec u\in U$ ist Linearkombination der $\vec v_j$.

(b): (1)$\iff$(2) sagt Satz [4.2](#satz-4-2), (2)$\Rightarrow$(3) sagt (a). (3)$\Rightarrow$(2): Schreibe $\vec w_0=\sum_it_i\vec v_i$. Aus (3) folgt $\langle\vec p,\vec v_j\rangle=\langle\vec w_0,\vec v_j\rangle=t_j$.
:::

::::beispiel
Sei $\vec p=\vec x=(5,1,-1)$ und $U=\operatorname{span}\{\vec f_1,\vec f_2\}$. Dann ist $\langle\vec x,\vec f_1\rangle=3$, $\langle\vec x,\vec f_2\rangle=-3$, also $\vec q=3\vec f_1-3\vec f_2=(3,0,-3)$. Der Rest $(2,1,2)$ hat die Länge 3 und steht senkrecht auf $\vec f_1,\vec f_2$. Probe mit [(4.3)](#gl-4-3) für $t=(2,-1)$: $\|\vec x-2\vec f_1+\vec f_2\|^2=14=27-18+1+4$.
::::

:::abbildung hm1/k9proj 4
Die Ebene $U$ durch $O$ wird von $\vec f_1,\vec f_2$ aufgespannt. Der nächste Punkt zu $P=(5,1,-1)$ ist $Q=(3,0,-3)=3\vec f_1-3\vec f_2$. Der Rest $\vec p-\vec q$ steht senkrecht auf $U$ und hat die Länge 3.
:::

⁠**Warum die Voraussetzung ONS nötig ist:** Für $\vec v_1=(1,0)$, $\vec v_2=\frac1{\sqrt2}(1,1)$ haben beide die Länge 1, stehen aber nicht senkrecht. Für $\vec p=(1,1)$ gibt die Formel [(4.5)](#gl-4-5) den Vektor $(2,1)\ne\vec p$, obwohl $\vec p$ im Aufspann liegt.

:::definition Definition 4.5 (Lotraum)
<span class="anker" id="satz-4-5"></span>

Sei $U\subset\mathbb{R}^n$ ein linearer Unterraum. Die Menge $U^\perp:=\{\vec w\in\mathbb{R}^n:\ \langle\vec w,\vec u\rangle=0\text{ für alle }\vec u\in U\}$ heißt __Lotraum__ von $U$.
:::

⁠**So liest man das:** $U^\perp$ enthält alle Vektoren, die auf ganz $U$ senkrecht stehen, zum Beispiel den Rest der Projektion. $U^\perp$ ist immer ein Unterraum: $\vec0$ liegt darin, und wegen der Linearität bleiben Summen und Vielfache senkrecht.

:::satz Satz 4.6 (Lotraum im $\mathbb{R}^3$)
<span class="anker" id="satz-4-6"></span>

Für linear unabhängige $\vec v_1,\vec v_2\in\mathbb{R}^3$ und $U:=\operatorname{span}\{\vec v_1,\vec v_2\}$ gilt $U^\perp=\operatorname{span}\{\vec v_1\times\vec v_2\}$ und $(U^\perp)^\perp=U$.
:::

⁠**Beweis der ersten Aussage:** „$\supset$“ ist (E2). „$\subset$“: Für $\vec x\in U^\perp$ gibt [(2.1)](rechenregeln-und-geometrie-im-raum.html#gl-2-1) den Vektor $\vec x\times(\vec v_1\times\vec v_2)=\langle\vec x,\vec v_2\rangle\vec v_1-\langle\vec x,\vec v_1\rangle\vec v_2=\vec0$. Nach Satz [2.1](rechenregeln-und-geometrie-im-raum.html#satz-2-1) (i) sind $\vec x$ und $\vec v_1\times\vec v_2\ne\vec0$ abhängig, also ist $\vec x$ ein Vielfaches davon. Die zweite Aussage folgt in Stufe [6](die-dimension.html#stufe-6).

:::frage Ist das dieselbe Projektion wie in Kapitel 8?
Ja, nur von der anderen Seite gerechnet. Für eine Hyperebene durch $O$ mit Normale $\vec n$ zieht [Kapitel 8](/wissen/elektrotechnik/1-semester/hohere-mathematik-1/vektoren-und-skalarprodukt/vektoren-und-skalarprodukt.html) den Anteil längs $\vec n$ ab: $\vec q=\vec p-\langle\vec p,\vec n\rangle\vec n$. Im Beispiel gibt das mit $\vec n=\vec f_3$ ebenfalls $(5,1,-1)-(2,1,2)=(3,0,-3)$.
:::

:::aufgabe Aufgabe 5 ★★ Projektion im $\mathbb{R}^4$
<span class="anker" id="aufg-5"></span>

Sei $\vec v_1=\frac12(1,1,1,1)$, $\vec v_2=\frac12(1,1,-1,-1)$, $\vec p=(3,1,2,0)$, $U=\operatorname{span}\{\vec v_1,\vec v_2\}$. (a) Prüfe [(4.1)](#gl-4-1). (b) Berechne $\operatorname{Proj}_U(\vec p)$ und $\operatorname{dist}(P,U)$. (c) Prüfe, dass der Rest senkrecht auf $U$ steht. (d) Wie groß ist $\|\vec p-2\vec v_1-2\vec v_2\|^2$ nach [(4.3)](#gl-4-3)?

:::loesung
(a) $\|\vec v_1\|^2=\|\vec v_2\|^2=\frac14\cdot4=1$, $\langle\vec v_1,\vec v_2\rangle=\frac14(1+1-1-1)=0$. (b) $\langle\vec p,\vec v_1\rangle=3$, $\langle\vec p,\vec v_2\rangle=1$, also $\operatorname{Proj}_U(\vec p)=3\vec v_1+\vec v_2=(2,2,1,1)$. Der Rest ist $(1,-1,1,-1)$, und $\operatorname{dist}(P,U)=2$. Probe: $14-9-1=4$. (c) $\langle(1,-1,1,-1),\vec v_1\rangle=0$, $\langle(1,-1,1,-1),\vec v_2\rangle=0$. (d) $14-10+(2-3)^2+(2-1)^2=6$.
:::
:::
