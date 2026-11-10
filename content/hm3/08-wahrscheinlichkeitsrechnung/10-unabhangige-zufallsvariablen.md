---
title: Stufe 9: Unabhängige Zufallsvariablen
pfad: Elektrotechnik / 3. Semester / HöMa3 – Höhere Mathematik 3 / Wahrscheinlichkeitsrechnung
adresse: elektrotechnik/3-semester/hohere-mathematik-3/wahrscheinlichkeitsrechnung
knoten: Kapitel 8: Wahrscheinlichkeitsrechnung
order: 3181000
summary: Zwei Größen können zusammenhängen oder nicht.
tags: gemeinsame Verteilungsfunktion, Zufallsvektors, stochastisch unabhängig, unkorreliert
lang: de
---

<span class="anker" id="stufe-9"></span>

:::zweck
Zwei Größen können zusammenhängen oder nicht. Diese Stufe überträgt die Unabhängigkeit von Ereignissen auf Zufallsvariablen. Der Lohn: Erwartungswerte multiplizieren sich, Varianzen addieren sich.
:::

**Die Idee.** $X$ und $Y$ sind unabhängig, wenn keine Auskunft über $X$ die Chancen von $Y$ ändert. Es genügt, das für die Fragen „$X\le x$?“ und „$Y\le y$?“ zu verlangen, sie bestimmen nach Stufe [4](zufallsvariablen-und-verteilungsfunktion.html#stufe-4) alle Intervalle.

:::definition Definition 9.1 (Unabhängigkeit von Zufallsvariablen)
<span class="anker" id="satz-9-1"></span>

Seien $X,Y$ Zufallsvariablen auf $(\Omega,\mathcal E,\mathbb{P})$. Die Funktion $F_{X,Y}:\mathbb{R}^2\to\mathbb{R}$,

<span class="anker" id="gl-9-1"></span>
$$F_{X,Y}(x,y):=\mathbb{P}(X\le x,\,Y\le y)=\mathbb{P}(\{\omega\in\Omega:X(\omega)\le x\text{ und }Y(\omega)\le y\}), \tag{9.1}$$

heißt __gemeinsame Verteilungsfunktion__ von $X$ und $Y$ oder Verteilungsfunktion des __Zufallsvektors__ $\boldsymbol X=(X,Y)$. $X$ und $Y$ heißen __stochastisch unabhängig__, wenn die Ereignisse $\{X\le x\}$ und $\{Y\le y\}$ für alle $x,y$ unabhängig sind, also

<span class="anker" id="gl-9-2"></span>
$$F_{X,Y}(x,y)=F_X(x)\,F_Y(y)\quad\text{für alle }(x,y)\in\mathbb{R}^2. \tag{9.2}$$
:::

::::beispiel das Einheitsquadrat
Sei $\Omega=[0,1]^2$ mit der Fläche als $\mathbb{P}$ wie in Stufe [3](zusatzwissen-unabhangigkeit-und-bayes.html#stufe-3). Für stetige $g,h$ auf $[0,1]$ sei $X(\omega)=g(s)$ und $Y(\omega)=h(t)$ für $\omega=(s,t)$. Dann besteht $\{X\le x\}$ aus senkrechten und $\{Y\le y\}$ aus waagerechten Streifen. Solche Streifenmengen sind unabhängig, also auch $X$ und $Y$. Hier ist $\mathbb{P}(\mathrm{d}\omega)=\mathrm{d} s\,\mathrm{d} t$, und Erwartungswerte sind Flächenintegrale:

$$\mathbb{E}(X)=\int_\Omega X(\omega)\,\mathbb{P}(\mathrm{d}\omega)=\int_0^1\!\!\int_0^1X(s,t)\,\mathrm{d} s\,\mathrm{d} t=\int_0^1g(s)\,\mathrm{d} s,\qquad\mathbb{E}(Y)=\int_0^1h(t)\,\mathrm{d} t.$$

Das Doppelintegral von $g(s)h(t)$ zerfällt nach Fubini ([Kapitel 2](/wissen/elektrotechnik/3-semester/hohere-mathematik-3/integralrechnung-im-rn/integralrechnung-im-rn.html)), also ist $\mathbb{E}(XY)=\mathbb{E}(X)\,\mathbb{E}(Y)$. Für $g(s)=s^2$, $h(t)=2t$ gibt das $\frac13\cdot1=\frac13$.
::::

:::satz Satz 9.2 (Unabhängigkeit im diskreten Fall)
<span class="anker" id="satz-9-2"></span>

Diskrete $X,Y$ mit Wertebereichen $\{x_0,x_1,\dots\}$ und $\{y_0,y_1,\dots\}$ sind genau dann unabhängig, wenn

<span class="anker" id="gl-9-3"></span>
$$\mathbb{P}(X=x_k,\,Y=y_\ell)=\mathbb{P}(X=x_k)\,\mathbb{P}(Y=y_\ell)\quad\text{für alle }k,\ell. \tag{9.3}$$
:::

:::beweis Idee
Summiert man [(9.3)](#gl-9-3) über alle $x_k\le x$ und $y_\ell\le y$, entsteht [(9.2)](#gl-9-2). Umgekehrt ergeben sich die Einzelwahrscheinlichkeiten aus $F_{X,Y}$ als Sprunghöhen.
:::

:::satz Satz 9.3 (Folgen der Unabhängigkeit)
<span class="anker" id="satz-9-3"></span>

Für unabhängige $X,Y$, für die $\mathbb{E}(X^2)$ und $\mathbb{E}(Y^2)$ existieren, gilt

<span class="anker" id="gl-9-4"></span>
$$\mathbb{E}(XY)=\mathbb{E}(X)\,\mathbb{E}(Y),\qquad\operatorname{Cov}(X,Y)=0,\qquad\operatorname{Var}(X+Y)=\operatorname{Var}(X)+\operatorname{Var}(Y). \tag{9.4}$$
:::

:::beweis Für diskrete $X,Y$
Mit [(9.3)](#gl-9-3) zerfällt die Doppelsumme:

$$\mathbb{E}(XY)=\sum_{k,\ell}x_ky_\ell\,\mathbb{P}(X=x_k,\,Y=y_\ell)=\sum_kx_k\,\mathbb{P}(X=x_k)\sum_\ell y_\ell\,\mathbb{P}(Y=y_\ell)=\mathbb{E}(X)\,\mathbb{E}(Y).$$

Der Rest folgt aus [(8.3)](varianz-kovarianz-und-tschebyschew.html#gl-8-3) und [(8.2)](varianz-kovarianz-und-tschebyschew.html#gl-8-2).
:::

::::beispiel [Beispiele]
$W_1,W_2$ sind unabhängig, denn jedes Paar hat die Wahrscheinlichkeit $\frac14\cdot\frac14$. Das erklärt $\operatorname{Var}(S)=\frac54+\frac54$. Für binomialverteiltes $X=\sum_{i=1}^nX_i$ mit unabhängigen Treffern ist $\operatorname{Var}(X_i)=p-p^2$, also schrittweise $\operatorname{Var}(X)=np(1-p)$.
::::

⁠**Grenzfall:** Mit $Y=X$ versagt die Produktregel: $\mathbb{E}(W_1\cdot W_1)=\frac{15}2\neq\frac{25}4$.

:::definition Definition 9.4 (Unkorreliert)
<span class="anker" id="satz-9-4"></span>

Zufallsvariablen $X,Y$ mit $\operatorname{Cov}(X,Y)=0$ heißen __unkorreliert__.
:::

:::satz Satz 9.5 (Unabhängig und unkorreliert)
<span class="anker" id="satz-9-5"></span>

Unabhängige Zufallsvariablen sind unkorreliert. Die Umkehrung gilt nicht.
:::

Die erste Aussage steht in [(9.4)](#gl-9-4). Für die zweite sei $D=W_1-W_2$. Dann ist $\mathbb{E}(D)=0$ und $\mathbb{E}(DS)=\mathbb{E}(W_1^2)-\mathbb{E}(W_2^2)=0$, also $\operatorname{Cov}(D,S)=0$. Aber $\mathbb{P}(S=2,\,D=1)=0$, während $\mathbb{P}(S=2)\,\mathbb{P}(D=1)=\frac1{16}\cdot\frac3{16}\neq0$ ist. Die Kovarianz sieht nur einen linearen Trend (Abb. [9](#abb-9)).

:::abbildung hm3/k8gitter 9
Links kommen alle Kombinationen vor. Rechts ein Rhombus ohne Neigung: unkorreliert, aber $S=2$ erzwingt $D=0$.
:::

:::frage Reicht für die Varianzformel nicht schon „unkorreliert“?
Doch, in [(8.2)](varianz-kovarianz-und-tschebyschew.html#gl-8-2) steht nur die Kovarianz. Im Beispiel ist $\operatorname{Var}(S+D)=\operatorname{Var}(2W_1)=5=\frac52+\frac52$, obwohl $S$ und $D$ abhängig sind.
:::

:::aufgabe Aufgabe 14 ★★ Eine Tabelle auswerten
<span class="anker" id="aufg-14"></span>

$X$ und $Y$ haben die gemeinsamen Wahrscheinlichkeiten

|  | $Y=0$ | $Y=1$ | $Y=2$ |
|---|---|---|---|
| $X=0$ | 0,12 | 0,18 | 0,30 |
| $X=1$ | 0,08 | 0,12 | 0,20 |

Bestimme die Verteilungen von $X$ und $Y$. Prüfe die Unabhängigkeit. Berechne $\mathbb{E}(XY)$ und $\operatorname{Var}(X+Y)$.

:::loesung
Zeilen- und Spaltensummen: $X$ hat $0{,}6$; $0{,}4$ und $Y$ hat $0{,}2$; $0{,}3$; $0{,}5$. Alle sechs Einträge sind die Produkte, also unabhängig. $\mathbb{E}(XY)=1\cdot0{,}12+2\cdot0{,}20=0{,}52=0{,}4\cdot1{,}3$. Mit $\operatorname{Var}(X)=0{,}24$ und $\operatorname{Var}(Y)=2{,}3-1{,}69=0{,}61$ ist $\operatorname{Var}(X+Y)=0{,}85$.
:::
:::
