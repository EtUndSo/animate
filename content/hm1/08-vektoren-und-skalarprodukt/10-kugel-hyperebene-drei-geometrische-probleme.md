---
title: Stufe 8: Kugel, Hyperebene, drei geometrische Probleme
pfad: Elektrotechnik / 1. Semester / HöMa1 – Höhere Mathematik 1 / Vektoren und Skalarprodukt
adresse: elektrotechnik/1-semester/hohere-mathematik-1/vektoren-und-skalarprodukt
knoten: Kapitel 8: Vektoren und Skalarprodukt
order: 1281000
summary: Eine Ebene im mathbb R 3 braucht zwei Richtungen, ihr Gegenstück im mathbb R k braucht k-1 .
tags: Kugeloberfläche, Kreis, Einheitskreislinie, Hyperebene, Aufpunkt, Lotrichtung, Hessesche Normalform, orthogonale Projektion
lang: de
---

<span class="anker" id="stufe-8"></span>

:::zweck
Eine Ebene im $\mathbb{R}^3$ braucht zwei Richtungen, ihr Gegenstück im $\mathbb{R}^k$ braucht $k-1$. Diese Stufe beschreibt sie durch die eine Richtung, die senkrecht darauf steht, und löst damit drei geometrische Probleme.
:::

**Die Idee.** Mit dem Skalarprodukt beschreibt man Mengen durch Bedingungen. „Gleicher Abstand von einem Punkt“ gibt eine Kugel. „Senkrecht auf einer festen Richtung“ gibt eine Hyperebene: Von den $k$ Richtungen des $\mathbb{R}^k$ fällt eine weg, alle anderen bleiben frei. Statt $k-1$ erlaubte Richtungen aufzuzählen, nennt man die eine verbotene (Abb. [9](#abb-9)).

:::definition Definition 8.1 (Kugeloberfläche und Kreis)
<span class="anker" id="satz-8-1"></span>

Sei $\vec p=\overrightarrow{OP}\in\mathbb{R}^k$ und $\varrho>0$. Dann heißt $K=\{\vec u\in\mathbb{R}^k:\ \|\vec u-\vec p\|=\varrho\}$ __Kugeloberfläche__ (__Kreis__ für $k=2$) mit Mittelpunkt $P$ und Radius $\varrho$.
:::

⁠**So liest man das:** $K$ enthält alle Punkte mit Abstand $\varrho$ von $P$. Für $k=2$, $\vec p=\vec0$, $\varrho=1$ entsteht die __Einheitskreislinie__ $S^1$: $u_1^2+u_2^2=1$. Beispiel: $(4,6)$ liegt auf dem Kreis um $(1,2)$ mit Radius 5, denn $\|(3,4)\|=5$.

**Parameterform.** Hyperebenen im $\mathbb{R}^k$ werden wie Ebenen im $\mathbb{R}^3$ aufgespannt, aber von $k-1$ linear unabhängigen Richtungen $\vec v_1,\dots,\vec v_{k-1}\in\mathbb{R}^k$:

$$H=\{\vec w+\alpha_1\vec v_1+\dots+\alpha_{k-1}\vec v_{k-1}:\ \alpha_1,\dots,\alpha_{k-1}\in\mathbb{R}\}\subset\mathbb{R}^k.$$

Das heißt Parameterdarstellung der __Hyperebene__ mit __Aufpunkt__ $\vec w\in\mathbb{R}^k$. Für $k=3$ ist $H$ eine Ebene, für $k=2$ eine Gerade. Für großes $k$ sind das viele Richtungen.

:::definition Definition 8.2 (Hyperebene mit Lotrichtung)
<span class="anker" id="satz-8-2"></span>

Für $\vec w\in\mathbb{R}^k$ und $\vec n\in\mathbb{R}^k\setminus\{\vec0\}$ heißt

<span class="anker" id="gl-8-1"></span>
$$H_{\vec w,\vec n}:=\{\vec w+\vec v:\ \vec v\in\mathbb{R}^k,\ \langle\vec v,\vec n\rangle=0\}=\{\vec u\in\mathbb{R}^k:\ \langle\vec u-\vec w,\vec n\rangle=0\} \tag{8.1}$$

Hyperebene mit Aufpunkt $\vec w$ und __Lotrichtung__ $\vec n$. Setzt man $\beta:=\langle\vec w,\vec n\rangle\in\mathbb{R}$, so gilt

<span class="anker" id="gl-8-2"></span>
$$H_{\vec w,\vec n}=\{\vec u\in\mathbb{R}^k:\ \langle\vec u,\vec n\rangle=\beta\}=:H_{\beta,\vec n}. \tag{8.2}$$
:::

⁠**So liest man das:** $\vec u$ liegt in $H$, wenn der Pfeil vom Aufpunkt zu $\vec u$ senkrecht auf $\vec n$ steht. Linearität macht daraus $\langle\vec u,\vec n\rangle=\beta$, ausgeschrieben eine lineare Gleichung $n_1u_1+\dots+n_ku_k=\beta$. Im Modell ist $2x_1+x_2+2x_3=6$ die Hyperebene mit Lotrichtung $(2,1,2)$ und Aufpunkt $\vec w=(3,0,0)$. Die Richtungen $\vec v_1=(1,0,-1)$ und $\vec v_2=(-1,2,0)$ stehen senkrecht auf der Lotrichtung und sind linear unabhängig, das gibt die Parameterform, zum Beispiel $\vec w-\vec v_1+\vec v_2=(1,2,1)$.

Die Gleichung $\langle\vec u,\vec n\rangle=\beta$ darf man mit jedem $\alpha\ne0$ multiplizieren, ohne $H$ zu ändern. Wählt man $\alpha=\frac1{\|\vec n\|}$ oder, falls dann die rechte Seite negativ wäre, $\alpha=-\frac1{\|\vec n\|}$, darf man ohne Einschränkung $\|\vec n\|=1$ und $\beta\ge0$ annehmen.

:::definition Definition 8.3 (Hessesche Normalform)
<span class="anker" id="satz-8-3"></span>

Ist $\vec n\in\mathbb{R}^k$ mit $\|\vec n\|=1$ und $\beta\ge0$, so heißt $H=\{\vec u\in\mathbb{R}^k:\ \langle\vec u,\vec n\rangle=\beta\}\subset\mathbb{R}^k$ __Hessesche Normalform__ der Hyperebene $H$.
:::

⁠**So liest man das:** Im Modell teilt man durch $\|(2,1,2)\|=3$: $\frac23x_1+\frac13x_2+\frac23x_3=2$, also $\vec n=(\frac23,\frac13,\frac23)$ und $\beta=2$. Im $\mathbb{R}^2$ ist $3x_1+4x_2=10$ eine Gerade mit $\vec n=(\frac35,\frac45)$, $\beta=2$. Die Normalform zeigt, wie weit $H$ vom Ursprung entfernt ist: $\beta\vec n$ liegt in $H$, weil $\langle\beta\vec n,\vec n\rangle=\beta$, und Problem B zeigt $\operatorname{dist}(O,H)=\beta$.

:::abbildung hm1/k8hyperebene 9
Die Ebene $H$: $2x_1+x_2+2x_3=6$ schneidet die Achsen bei 3, 6 und 3, die Achsenstücke dahinter sind gestrichelt. Der Einheitsvektor $\vec n$ steht senkrecht auf ihr. Der nächste Punkt zum Ursprung ist $\beta\vec n$ mit $\beta=2$. Der Punkt $P=(3,3,3)$ hat den Lotfußpunkt $Q=(1,2,1)$ und den Abstand 3.
:::

Für die drei Probleme sei $G=\{\vec w+\alpha\vec v:\alpha\in\mathbb{R}\}\subset\mathbb{R}^k$ eine Gerade und $H=\{\vec u\in\mathbb{R}^k:\langle\vec u,\vec n\rangle=\beta\}$ eine Hyperebene in Hessescher Normalform.

**Problem A: Schnitt von Gerade und Hyperebene.** Man setzt $\vec u=\vec w+\alpha\vec v$ ein. Linearität gibt eine Gleichung mit der einzigen Unbekannten $\alpha$:

<span class="anker" id="gl-8-3"></span>
$$\langle\vec w,\vec n\rangle+\alpha\,\langle\vec v,\vec n\rangle=\beta. \tag{8.3}$$

<ul>

<li>

⁠**Fall 1:** $\langle\vec v,\vec n\rangle\ne0$. $G$ ist nicht parallel zu $H$, und

<span class="anker" id="gl-8-4"></span>
$$\alpha^*:=\frac{\beta-\langle\vec w,\vec n\rangle}{\langle\vec v,\vec n\rangle} \quad\text{liefert den eindeutigen Schnittpunkt}\quad G\cap H=\{\vec w+\alpha^*\vec v\}. \tag{8.4}$$

</li>

<li>

⁠**Fall 2a:** $\langle\vec v,\vec n\rangle=0$ und $\langle\vec w,\vec n\rangle\ne\beta$. $G$ ist parallel zu $H$, [(8.3)](#gl-8-3) ist nicht lösbar, $G\cap H=\emptyset$.

</li>

<li>

⁠**Fall 2b:** $\langle\vec v,\vec n\rangle=0$ und $\langle\vec w,\vec n\rangle=\beta$. Jedes $\alpha$ löst [(8.3)](#gl-8-3), also ist $G\subset H$.

</li>

</ul>

::::beispiel
Für $\vec w=(1,0,-1)$, $\vec v=(2,0,1)$ ist $\langle\vec w,\vec n\rangle=0$ und $\langle\vec v,\vec n\rangle=2$. Das gibt $\alpha^*=1$ und den Schnittpunkt $S=(3,0,0)$. Die Richtung $(1,0,-1)$ ist parallel zu $H$: Mit $\vec w=(1,0,-1)$ liegt Fall 2a vor, mit $\vec w=(1,2,1)$ Fall 2b.
::::

**Problem B: Lotfußpunkt und Abstand.** Gesucht ist zu $P$ mit $\vec p=\overrightarrow{OP}$ der Punkt $\vec q\in H$ mit $\vec p-\vec q\in\{\alpha\vec n:\alpha\in\mathbb{R}\}$. Also schneidet man die Gerade durch $P$ mit Richtung $\vec n$ mit $H$. Das ist Problem A mit $\vec w:=\vec p$, $\vec v:=\vec n$. Wegen $\langle\vec n,\vec n\rangle=1\ne0$ liegt Fall 1 vor, also ist $\alpha^*=\beta-\langle\vec p,\vec n\rangle$ und

<span class="anker" id="gl-8-5"></span>
$$\vec q=\vec p+\bigl(\beta-\langle\vec p,\vec n\rangle\bigr)\vec n,\qquad\operatorname{dist}(P,H)=\min_{\vec z\in H}\|\vec p-\vec z\|=\|\vec p-\vec q\|=\bigl|\beta-\langle\vec p,\vec n\rangle\bigr|. \tag{8.5}$$

Der Punkt $\vec q$ heißt __orthogonale Projektion__ von $P$ auf $H$. Er ist der nächste Punkt, aus demselben Grund wie in Stufe [6](projektion-und-abstand-zur-geraden.html#stufe-6): Für $\vec z\in H$ ist $\langle\vec q-\vec z,\vec n\rangle=\beta-\beta=0$, also steht $\vec q-\vec z$ senkrecht auf $\vec p-\vec q$, und Pythagoras gibt $\|\vec p-\vec z\|^2=\|\vec p-\vec q\|^2+\|\vec q-\vec z\|^2$. Für $P=O$ folgt $\operatorname{dist}(O,H)=\beta$.

::::beispiel
Für $P=(3,3,3)$ ist $\langle\vec p,\vec n\rangle=5$, also $\alpha^*=-3$, $\vec q=(1,2,1)$ und $\operatorname{dist}(P,H)=3$, dagegen $\operatorname{dist}(O,H)=2$.
::::

**Problem C: Winkel zwischen Gerade und Hyperebene.** Gesucht ist der Winkel $\gamma$ zwischen $G$ und ihrer Projektion $G'$ auf $H$. Vorausgesetzt wird (a) $\langle\vec v,\vec n\rangle\ne0$, also ein eindeutiger Schnittpunkt, und (b) $\vec v\notin\operatorname{span}\{\vec n\}$, sonst ist $G'$ nur ein Punkt. Es sei $\delta\in(0,\frac\pi2)$ der Winkel zwischen $\vec n$ und $\vec v$ oder $-\vec v$, je nachdem, welcher Vektor $\cos\delta>0$ liefert. Die Vektoren $\vec n$, $\vec v$ und die Richtung von $G'$ liegen in einer Ebene, und $\vec n$ steht senkrecht auf $G'$. Also ist $\gamma=\frac\pi2-\delta$, und mit [(7.4)](winkel-cauchy-schwarz-parallelogramm.html#gl-7-4) gilt

<span class="anker" id="gl-8-6"></span>
$$\sin\gamma=\cos\Bigl(\frac\pi2-\gamma\Bigr)=\cos\delta=\frac{|\langle\vec n,\vec v\rangle|}{\|\vec n\|\cdot\|\vec v\|}\ne0. \tag{8.6}$$

Damit lässt sich $\gamma\in(0,\frac\pi2)$ berechnen.

::::beispiel
Für $\vec v=(2,0,1)$ ist $\sin\gamma=\frac2{\sqrt5}$, also $\gamma=63{,}43^\circ$ und $\delta=26{,}57^\circ$ (Abb. [10](#abb-10)).
::::

⁠**Grenzfälle:** Für $G$ senkrecht auf $H$ gibt die Formel $\gamma=\frac\pi2$, für $G$ parallel zu $H$ gibt sie $\gamma=0$.

:::abbildung hm1/k8geradewinkel 10
Die Gerade $G$ durchstößt $H$ in $S=(3,0,0)$. In $S$ steht $\vec n$ senkrecht auf $H$. $G'$ ist die Projektion von $G$ auf $H$. Die Winkel $\gamma=63{,}43^\circ$ und $\delta=26{,}57^\circ$ ergänzen sich zu $90^\circ$.
:::

:::frage Warum soll man $\vec n$ normieren? Die Ebene ändert sich doch nicht.
Die Menge ändert sich nicht, die Formeln werden kürzer. Mit $\|\vec n\|=1$ fällt in [(8.5)](#gl-8-5) der Nenner $\|\vec n\|$ weg, und $|\beta-\langle\vec p,\vec n\rangle|$ ist direkt ein Abstand.
:::

:::aufgabe Aufgabe 10 ★★ Hessesche Normalform
<span class="anker" id="aufg-10"></span>

(a) Bringe $3x_1-4x_2=-10$ auf Hessesche Normalform. (b) Bestimme für $P=(1,2)$ den Lotfußpunkt und den Abstand. (c) Im $\mathbb{R}^4$ ist $x_1+x_2+x_3+x_4=2$ eine Hyperebene. Bestimme für $P=(2,2,2,2)$ Lotfußpunkt und Abstand.

:::loesung
(a) Die Lotrichtung $(3,-4)$ hat Länge 5. Weil rechts $-10$ steht, multipliziert man mit $-\frac15$: $-\frac35x_1+\frac45x_2=2$. Also $\vec n=(-\frac35,\frac45)$, $\beta=2$. (b) $\langle\vec p,\vec n\rangle=1$, also $\vec q=\vec p+(2-1)\vec n=(\frac25,\frac{14}5)$, Abstand 1. Probe: $3\cdot\frac25-4\cdot\frac{14}5=-10$. (c) $\vec n=\frac12(1,1,1,1)$, $\beta=1$. $\langle\vec p,\vec n\rangle=4$, also $\vec q=\vec p-3\vec n=(\frac12,\frac12,\frac12,\frac12)$, Abstand 3.
:::
:::

:::aufgabe Aufgabe 11 ★★★ Alle drei Probleme
<span class="anker" id="aufg-11"></span>

Gegeben sind $H$: $x_1+2x_2+2x_3=9$, $G$: $(3,0,0)+\alpha(1,1,0)$ und $P=(2,4,4)$. (a) Bestimme die Hessesche Normalform und $\operatorname{dist}(O,H)$. (b) Bestimme den Schnittpunkt von $G$ und $H$. (c) Bestimme den Winkel zwischen $G$ und $H$. (d) Bestimme Lotfußpunkt und Abstand von $P$. (e) Welche der Richtungen $(2,-1,0)$ und $(1,1,1)$ ist parallel zu $H$?

:::loesung
(a) Die Lotrichtung $(1,2,2)$ hat Länge 3: $\vec n=(\frac13,\frac23,\frac23)$, $\beta=3=\operatorname{dist}(O,H)$. (b) $\langle\vec w,\vec n\rangle=1$, $\langle\vec v,\vec n\rangle=1$, $\alpha^*=2$, Schnittpunkt $(5,2,0)$. Probe: $5+4=9$. (c) $\sin\gamma=\frac1{1\cdot\sqrt2}$, also $\gamma=45^\circ$. (d) $\langle\vec p,\vec n\rangle=6$, $\vec q=\vec p-3\vec n=(1,2,2)$, Abstand 3. (e) $(2,-1,0)$, denn $\langle(2,-1,0),(1,2,2)\rangle=0$. Für $(1,1,1)$ ergibt sich 5.
:::
:::
