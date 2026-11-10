---
title: Stufe 5: Drei diskrete Verteilungen
pfad: Elektrotechnik / 3. Semester / HöMa3 – Höhere Mathematik 3 / Wahrscheinlichkeitsrechnung
adresse: elektrotechnik/3-semester/hohere-mathematik-3/wahrscheinlichkeitsrechnung
knoten: Kapitel 8: Wahrscheinlichkeitsrechnung
order: 3180600
summary: Drei Situationen kehren immer wieder: Treffer bei Wiederholungen, seltene Ereignisse und Stichproben ohne Zurücklegen.
tags: diskret, Wahrscheinlichkeitsfunktion, Bernoulli-Experiment, binomialverteilt, Binomialverteilung, Poisson-verteilt, Poisson-Verteilung, hypergeometrisch verteilt
lang: de
---

<span class="anker" id="stufe-5"></span>

:::zweck
Drei Situationen kehren immer wieder: Treffer bei Wiederholungen, seltene Ereignisse und Stichproben ohne Zurücklegen. Diese Stufe leitet die zugehörigen Verteilungen her.
:::

:::definition Definition 5.1 (Diskrete Zufallsvariable)
<span class="anker" id="satz-5-1"></span>

Eine Zufallsvariable mit endlichem oder abzählbar unendlichem Wertebereich $\{x_0,x_1,\dots\}$ heißt __diskret__. Ihre __Wahrscheinlichkeitsfunktion__ ist $p_X(x):=\mathbb{P}(X=x_k)$ für $x=x_k$ und $p_X(x):=0$ sonst. Aufsummieren gibt $F_X(x)=\sum_{x_k\le x}p_X(x_k)$.
:::

**Wiederholte Versuche.** Ein __Bernoulli-Experiment__ hat genau zwei Ausgänge: $\omega=1$ (Treffer) mit $\mathbb{P}(1)=p$ und $\omega=0$ mit $\mathbb{P}(0)=1-p$, $p\in(0,1)$. Für $p=\frac12$ ist das ein Laplace-Experiment. Bei $n$ Wiederholungen unter gleichen Bedingungen ist $\Omega=\{0,1\}^n$ mit $\mathbb{P}^n(\omega)=\mathbb{P}(\omega_1)\cdots\mathbb{P}(\omega_n)$. Das Produkt drückt die Unabhängigkeit der Versuche aus. Das Ereignis „genau $k$ Treffer“ enthält $\binom nk$ Folgen, denn so viele Wahlen der Trefferplätze gibt es, und jede Folge hat die Wahrscheinlichkeit $p^k(1-p)^{n-k}$.

:::definition Definition 5.2 (Binomialverteilung)
<span class="anker" id="satz-5-2"></span>

$X$ heißt __binomialverteilt__ mit $n\in\mathbb{N}$, $p\in[0,1]$, wenn gilt:

<span class="anker" id="gl-5-1"></span>
$$b_{n,p}(k):=\mathbb{P}(X=k)=\binom nkp^k(1-p)^{n-k}\quad\text{für }k=0,1,\dots,n. \tag{5.1}$$

Die Wahrscheinlichkeitsfunktion $b_{n,p}$ heißt __Binomialverteilung__.
:::

$X$ zählt die Treffer. Die Summe aller Werte ist $(p+1-p)^n=1$ nach dem binomischen Satz.

::::beispiel
Greift man aus der Kiste fünfmal mit Zurücklegen, ist $n=5$, $p=\frac15$ und $\mathbb{P}(X\ge2)\approx0{,}263$.
::::

⁠**Grenzfall:** $n=1$ ist das Bernoulli-Experiment.

**Seltene Ereignisse.** Bei sehr vielen Versuchen mit kleiner Trefferquote kennt man oft nur die mittlere Trefferzahl $\lambda=np$.

:::definition Definition 5.3 (Poisson-Verteilung)
<span class="anker" id="satz-5-3"></span>

$X$ heißt __Poisson-verteilt__ mit $\lambda>0$, wenn gilt:

<span class="anker" id="gl-5-2"></span>
$$P_\lambda(k):=\mathbb{P}(X=k)=\frac{\lambda^k}{k!}\,\mathrm{e}^{-\lambda}\quad\text{für }k\in\mathbb{N}_0. \tag{5.2}$$

Die Wahrscheinlichkeitsfunktion $P_\lambda$ heißt __Poisson-Verteilung__.
:::

Die Summe ist 1, weil $\sum_k\lambda^k/k!=\mathrm{e}^\lambda$ gilt.

:::satz Satz 5.4 (Poisson als Grenzfall)
<span class="anker" id="satz-5-4"></span>

Für $n\to\infty$, $p\to0$ mit $np=\lambda$ gilt $b_{n,p}(k)\to P_\lambda(k)$ für jedes feste $k$.
:::

:::beweis Grenzübergang
Mit $p=\lambda/n$ wird aus [(5.1)](#gl-5-1)

$$\frac{n!}{k!\,(n-k)!}\Bigl(\frac\lambda n\Bigr)^k\Bigl(1-\frac\lambda n\Bigr)^{n-k} =\frac{\lambda^k}{k!}\cdot\underbrace{\frac nn\cdot\frac{n-1}n\cdots\frac{n-k+1}n}_{\to1}\cdot\underbrace{\Bigl(1-\frac\lambda n\Bigr)^n}_{\to\mathrm{e}^{-\lambda}}\cdot\underbrace{\Bigl(1-\frac\lambda n\Bigr)^{-k}}_{\to1}.$$

Der erste und der dritte Block haben eine feste Zahl von Faktoren.
:::

::::beispiel
Von 200 Bauteilen fällt jedes mit $p=0{,}01$ aus, also $\lambda=2$. Die Binomialverteilung gibt $\mathbb{P}(X=0)=0{,}134$, Poisson $\mathrm{e}^{-2}=0{,}135$ (Abb. [5](#abb-5)). Man nennt sie deshalb auch Verteilung der seltenen Ereignisse.

:::abbildung hm3/k8poisson 5
Binomialverteilung für $n=200$, $p=0{,}01$ und Poisson-Verteilung für $\lambda=2$.
:::
::::

**Stichprobe ohne Zurücklegen.** Eine Urne enthält $N$ Elemente, $M\le N$ davon haben eine Eigenschaft. Man entnimmt $n\le N$ Stück auf einmal, und $X$ zählt, wie viele davon die Eigenschaft haben. Das ist Fall (iii) des Urnenmodells.

:::definition Definition 5.5 (Hypergeometrische Verteilung)
<span class="anker" id="satz-5-5"></span>

$X$ heißt __hypergeometrisch verteilt__ mit $N,M,n\in\mathbb{N}$, wenn gilt:

<span class="anker" id="gl-5-3"></span>
$$h(k;N,M,n):=\mathbb{P}(X=k)=\frac{\binom Mk\binom{N-M}{n-k}}{\binom Nn}\quad\text{für }k=0,\dots,n. \tag{5.3}$$

Die Wahrscheinlichkeitsfunktion $h(\,\cdot\,;N,M,n)$ heißt __hypergeometrische Verteilung__.
:::

Ein Binomialkoeffizient $\binom ab$ mit $b>a$ ist dabei null.

::::beispiel
Die Rechnung für die Kiste in Stufe [2](zahlen.html#stufe-2) ist genau dieser Fall mit $N=20$, $M=4$, $n=5$. Ohne Zurücklegen ist $\mathbb{P}(X\ge2)\approx0{,}249$, mit Zurücklegen $0{,}263$.
::::

⁠**Grenzfall:** Ist $N$ groß gegen $n$, verändert das Herausnehmen die Urne kaum, und [(5.3)](#gl-5-3) geht in [(5.1)](#gl-5-1) mit $p=M/N$ über.

:::aufgabe Aufgabe 7 ★★ Turnier
<span class="anker" id="aufg-7"></span>

Spielerin A gewinnt einen Satz mit $p=\frac35$, unabhängig von den anderen. Wer zuerst zwei Sätze gewinnt, siegt. Wie wahrscheinlich siegt A? Prüfe das Ergebnis für $p=\frac12$.

:::loesung
Denkt man sich drei Sätze gespielt, ändert das den Sieger nicht. A braucht mindestens zwei Treffer: $3p^2(1-p)+p^3=3p^2-2p^3$. Für $p=\frac35$ ist das $\frac{81}{125}=0{,}648$, für $p=\frac12$ gerade $\frac12$.
:::
:::

:::aufgabe Aufgabe 8 ★★★ Aus welcher Kiste?
<span class="anker" id="aufg-8"></span>

Zwei gleich aussehende Kisten enthalten je 20 Teile, die eine 4 defekte, die andere 10. Du wählst zufällig eine Kiste und ziehst 4 Teile, genau 2 sind defekt. Wie wahrscheinlich stammt die Stichprobe aus der schlechteren Kiste?

:::loesung
Hypergeometrisch mit $\binom{20}4=4845$: gute Kiste $\binom42\binom{16}2=720$, schlechte Kiste $\binom{10}2\binom{10}2=2025$. Die Vorwahl $\frac12$ kürzt sich in [(3.4)](zusatzwissen-unabhangigkeit-und-bayes.html#gl-3-4): $\frac{2025}{720+2025}=\frac{45}{61}\approx0{,}738$.
:::
:::
