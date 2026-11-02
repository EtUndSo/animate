---
title: Stufe 11: Das Gesetz der großen Zahlen
pfad: Elektrotechnik / 3. Semester / Höhere Mathematik 3 / Wahrscheinlichkeitsrechnung
order: 3181200
summary: Warum liefert das Mitteln vieler Messungen einen stabilen Wert, obwohl jede einzelne streut?
tags: konvergieren stochastisch, identisch verteilt, i.i.d., fast sicher, punktweise fast sicher, Monte-Carlo-Integration
lang: de
---

<span class="anker" id="stufe-11"></span>

:::zweck
Warum liefert das Mitteln vieler Messungen einen stabilen Wert, obwohl jede einzelne streut? Diese Stufe beweist das zuerst für große, feste Messreihen und formuliert es dann für eine einzelne, immer weiter laufende Reihe.
:::

**Die Idee.** Bei $n$ unabhängigen Messungen addieren sich die Varianzen. Die Summe streut also nur wie $\sqrt n$, der Mittelwert wie $1/\sqrt n$. Die Tschebyschew-Ungleichung macht daraus eine Aussage über Wahrscheinlichkeiten.

**Viele Zufallsvariablen.** $X_1,\dots,X_n$ auf demselben Raum bilden den Zufallsvektor $\boldsymbol X=(X_1,\dots,X_n):\Omega\to\mathbb{R}^n$ mit der gemeinsamen Verteilungsfunktion $F_{\boldsymbol X}(\boldsymbol{x}):=\mathbb{P}(X_1\le x_1,\dots,X_n\le x_n)$.

:::definition Definition 11.1 (Unabhängigkeit von $n$ Zufallsvariablen)
<span class="anker" id="satz-11-1"></span>

$X_1,\dots,X_n$ heißen stochastisch unabhängig, wenn

<span class="anker" id="gl-11-1"></span>
$$F_{\boldsymbol X}(x_1,\dots,x_n)=F_{X_1}(x_1)\cdots F_{X_n}(x_n)\quad\text{für alle }(x_1,\dots,x_n)\in\mathbb{R}^n. \tag{11.1}$$

Eine Folge $(X_i)_{i\in\mathbb{N}}$ heißt unabhängig, wenn das für jede endliche Auswahl gilt.
:::

Wie bei Ereignissen genügt es nicht, Paare zu prüfen: Die $A_1,A_2,A_3$ aus Stufe [3](zusatzwissen-unabhangigkeit-und-bayes.html#stufe-3) geben mit $X_i=1$ auf $A_i$ und $X_i=0$ sonst ein Gegenbeispiel. Im diskreten Fall lautet die Bedingung $\mathbb{P}(\boldsymbol X=\boldsymbol{x})=\mathbb{P}(X_1=x_1)\cdots\mathbb{P}(X_n=x_n)$. Für Dichten gilt wörtlich dasselbe wie in Stufe [10](zufallsvektoren-mit-dichte.html#stufe-10):

:::satz Satz 11.2 (Dichten in $n$ Dimensionen)
<span class="anker" id="satz-11-2"></span>

Besitzt $\boldsymbol X$ die Dichte $f_{\boldsymbol X}:\mathbb{R}^n\to[0,\infty)$, also $F_{\boldsymbol X}(\boldsymbol{x})=\int_{-\infty}^{x_1}\cdots\int_{-\infty}^{x_n}f_{\boldsymbol X}(\boldsymbol{y})\,\mathrm{d} y_n\dots\mathrm{d} y_1$, dann sind die $X_i$ absolut stetig mit den Randdichten

<span class="anker" id="gl-11-2"></span>
$$f_{X_1}(x_1)=\int_{-\infty}^\infty\cdots\int_{-\infty}^\infty f_{\boldsymbol X}(x_1,y_2,\dots,y_n)\,\mathrm{d} y_2\dots\mathrm{d} y_n \tag{11.2}$$

und entsprechend für $X_2,\dots,X_n$. Sie sind genau dann unabhängig, wenn $f_{\boldsymbol X}=f_{X_1}\cdots f_{X_n}$ auf $\mathbb{R}^n$ gilt.
:::

:::satz Satz 11.3 (Produkte und Summen)
<span class="anker" id="satz-11-3"></span>

Sind $X_1,\dots,X_n$ unabhängig und existieren Erwartungswerte und Varianzen, dann gilt

<span class="anker" id="gl-11-3"></span>
$$\mathbb{E}\Bigl(\prod_{i=1}^nX_i\Bigr)=\prod_{i=1}^n\mathbb{E}(X_i),\qquad\operatorname{Var}\Bigl(\sum_{i=1}^nX_i\Bigr)=\sum_{i=1}^n\operatorname{Var}(X_i). \tag{11.3}$$
:::

Beides folgt durch Induktion aus Satz [9.3](unabhangige-zufallsvariablen.html#satz-9-3), weil $X_1\cdots X_{n-1}$ und $X_n$ unabhängig sind und ebenso $X_1+\dots+X_{n-1}$ und $X_n$.

**Das schwache Gesetz.** Sei $(X_i)$ eine unabhängige Folge mit $\mathbb{E}(X_i)=\mu$, $\operatorname{Var}(X_i)=\sigma^2$ für alle $i$. Für den Mittelwert $\overline X_n:=\frac1n\sum_{i=1}^nX_i$ gilt $\mathbb{E}(\overline X_n)=\mu$ und nach [(8.2)](varianz-kovarianz-und-tschebyschew.html#gl-8-2) und [(11.3)](#gl-11-3)

<span class="anker" id="gl-11-4"></span>
$$\operatorname{Var}(\overline X_n)=\frac1{n^2}\sum_{i=1}^n\operatorname{Var}(X_i)=\frac{\sigma^2}n. \tag{11.4}$$

Aus der Tschebyschew-Ungleichung folgt $\mathbb{P}(|\overline X_n-\mu|\ge\varepsilon)\le\sigma^2/(n\varepsilon^2)$. Ohne Unabhängigkeit gilt das nicht: Für $X_i=X_1$ bleibt $\overline X_n=X_1$ und streut wie am Anfang.

:::satz Satz 11.4 (Schwaches Gesetz der großen Zahlen)
<span class="anker" id="satz-11-4"></span>

Sei $(X_i)_{i\in\mathbb{N}}$ eine Folge unabhängiger Zufallsvariablen, die alle denselben Erwartungswert $\mu$ und dieselbe Varianz $\sigma^2$ haben. Dann gilt für jedes $\varepsilon>0$

<span class="anker" id="gl-11-5"></span>
$$\lim_{n\to\infty}\mathbb{P}\Bigl(\Bigl|\frac1n\sum_{i=1}^nX_i-\mu\Bigr|\ge\varepsilon\Bigr)=0 \quad\text{bzw.}\quad \lim_{n\to\infty}\mathbb{P}\Bigl(\Bigl|\frac1n\sum_{i=1}^nX_i-\mu\Bigr|<\varepsilon\Bigr)=1. \tag{11.5}$$
:::

Die Mittelwerte __konvergieren stochastisch__ gegen $\mu$: Wiederholt man das Gesamtexperiment mit festem großem $n$, liegt $\overline X_n$ fast immer nahe bei $\mu$. Die Herleitung zeigt mehr: Sind die $X_i$ unabhängig mit $\operatorname{Var}(X_i)\le M<\infty$ für alle $i$ und ist $S_n:=\sum_{i=1}^nX_i$, gilt

<span class="anker" id="gl-11-6"></span>
$$\lim_{n\to\infty}\mathbb{P}\Bigl(\Bigl|\frac{S_n-\mathbb{E}(S_n)}n\Bigr|\ge\varepsilon\Bigr)=0, \tag{11.6}$$

denn $\operatorname{Var}(S_n/n)\le M/n$. **Beispiel:** Für 1000 Würfe eines Vierer-Würfels ist $\mathbb{P}(|\overline X_{1000}-\frac52|\ge0{,}1)\le\frac{5/4}{1000\cdot0{,}01}=0{,}125$.

**Das starke Gesetz.** Das schwache Gesetz spricht über viele Reihen fester Länge. Wirft man aber eine einzige Münze immer weiter, erwartet man, dass genau diese Folge der Mittelwerte konvergiert: $\overline X_n(\omega)\to\mu$ (Abb. [11](#abb-11)). Zufallsvariablen $X_i$ heißen __identisch verteilt__, wenn ihre Verteilungsfunktionen gleich sind, im diskreten Fall also die $p_{X_i}$, im absolut stetigen die $f_{X_i}$ im Sinne der Integration. Dann sind auch Erwartungswerte und Varianzen gleich, falls sie existieren. Unabhängig und identisch verteilt kürzt man __i.i.d.__ ab (engl. independent identically distributed).

:::abbildung hm3/k8mittel 11
Laufender Mittelwert eines Vierer-Würfels in drei simulierten Reihen. Jede läuft für sich gegen $\mu=2{,}5$. Gestrichelt ist $\mu\pm\sigma/\sqrt n$.
:::

:::satz Satz 11.5 (Starkes Gesetz der großen Zahlen)
<span class="anker" id="satz-11-5"></span>

Für eine i.i.d.-Folge $(X_i)_{i\in\mathbb{N}}$ auf $(\Omega,\mathcal E,\mathbb{P})$ mit Erwartungswert $\mu$ gilt

<span class="anker" id="gl-11-7"></span>
$$\mathbb{P}\Bigl(\Bigl\{\omega\in\Omega:\lim_{n\to\infty}\frac1n\sum_{i=1}^nX_i(\omega)=\mu\Bigr\}\Bigr)=1. \tag{11.7}$$

Gleichbedeutend hat die Menge der $\omega$, für die der Grenzwert nicht existiert oder von $\mu$ abweicht, die Wahrscheinlichkeit 0.
:::

Der Satz wird hier ohne Beweis benutzt. Ein Ereignis $A$ tritt __fast sicher__ ein, wenn $\mathbb{P}(A)=1$ gilt. Der Satz sagt also: Die Mittelwerte konvergieren __punktweise fast sicher__ gegen $\mu$.

:::beweis Stark impliziert schwach
Sei $\varepsilon>0$, die Folge wie im Satz, und $A_n=\{\omega:|\overline X_k(\omega)-\mu|\ge\varepsilon\text{ für ein }k\ge n\}$. Die $A_n$ fallen ab, nach Satz [1.4](ereignisse-und-wahrscheinlichkeit.html#satz-1-4) gilt $\lim_n\mathbb{P}(A_n)=\mathbb{P}(A_\infty)$ mit $A_\infty=\bigcap_nA_n$. Für $\omega\in A_\infty$ gibt es beliebig große $k$ mit $|\overline X_k(\omega)-\mu|\ge\varepsilon$, also konvergiert $\overline X_n(\omega)$ nicht gegen $\mu$. Nach dem starken Gesetz ist $\mathbb{P}(A_\infty)=0$. Wegen $\{|\overline X_n-\mu|\ge\varepsilon\}\subset A_n$ folgt

$$0\le\lim_{n\to\infty}\mathbb{P}(|\overline X_n-\mu|\ge\varepsilon)\le\lim_{n\to\infty}\mathbb{P}(A_n)=0.$$
:::

Das Argument zeigt allgemein: Punktweise Konvergenz fast sicher impliziert stochastische Konvergenz.

:::frage Gilt auch die Umkehrung?
Nein. Auf $\Omega=[0,1]$ mit der Länge als $\mathbb{P}$ sei $Y_n$ gleich 1 auf einem wandernden Intervall ($[0,1]$, dann die zwei Hälften, dann die vier Viertel, und so weiter) und sonst 0. Die Längen gehen gegen 0, also $Y_n\to0$ stochastisch, aber jedes $\omega$ wird immer wieder getroffen. Es lässt sich zeigen: Konvergiert $Y_n$ stochastisch gegen $Y$, dann konvergiert eine Teilfolge punktweise fast sicher gegen $Y$.
:::

:::aufgabe Aufgabe 18 ★★ Integrieren mit Zufallszahlen
<span class="anker" id="aufg-18"></span>

Seien $U_1,U_2,\dots$ i.i.d. gleichverteilt auf $[0,1]$ und $f:[0,1]\to\mathbb{R}$ stetig.

<ol class="al">

<li>

Zeige: $\frac1n\sum_{i=1}^nf(U_i)\to\int_0^1f(x)\,\mathrm{d} x$ fast sicher. Das ist die __Monte-Carlo-Integration__.

</li>

<li>

Für $f(x)=x^2$: Welches $n$ garantiert die Tschebyschew-Ungleichung für einen Fehler unter $0{,}01$ mit mindestens 90 %?

</li>

</ol>

:::loesung
(a) $Y_i=f(U_i)$ sind i.i.d. mit $\mathbb{E}(Y_i)=\int_0^1f(x)\,\mathrm{d} x$ nach [(7.3)](der-erwartungswert.html#gl-7-3), das starke Gesetz gibt die Behauptung. (b) $\mathbb{E}(Y_1)=\frac13$, $\mathbb{E}(Y_1^2)=\frac15$, also $\sigma^2=\frac4{45}$. Aus $\frac{4/45}{n\cdot10^{-4}}\le0{,}1$ folgt $n\ge\frac{80000}9$, also $n\ge8889$.
:::
:::
