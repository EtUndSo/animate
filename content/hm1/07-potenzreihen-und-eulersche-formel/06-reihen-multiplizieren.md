---
title: Stufe 4: Reihen multiplizieren
pfad: Elektrotechnik / 1. Semester / Höhere Mathematik 1 / Potenzreihen und Eulersche Formel
order: 1270600
summary: Wer exp(z)exp(w) ausrechnen will, muss zwei Reihen multiplizieren.
tags: doppelt indizierte Folge, Doppelreihe, Binomialkoeffizienten
lang: de
---

<span class="anker" id="stufe-4"></span>

:::zweck
Wer $\exp(z)\exp(w)$ ausrechnen will, muss zwei Reihen multiplizieren. Diese Stufe klärt, in welcher Reihenfolge das erlaubt ist, und liefert die binomische Formel dazu.
:::

**Die Idee.** Zwei endliche Summen multipliziert man „jeder mit jedem“. Bei Reihen entsteht eine unendliche Tabelle (Abb. [4](#abb-4)), und man braucht eine Reihenfolge. [Teil 6](/wissen/elektrotechnik/1-semester/hohere-mathematik-1/unendliche-reihen/unendliche-reihen.html) gibt die Antwort: Bei absoluter Konvergenz ist jede Reihenfolge gleich gut. Bei Potenzreihen bietet sich die Reihenfolge nach Diagonalen an, denn dort stehen alle Glieder mit derselben Potenz von $x$.

:::abbildung hm1/k7cauchy 4
Das Produkt zweier Potenzreihen als Tabelle. In einer Diagonale ist $n+m=k$ fest, also steht dort überall $x^k$. Die Summe der Vorfaktoren einer Diagonale ist $c_k$.
:::

**Doppelreihen.** Eine __doppelt indizierte Folge__ $a_{ij}$ ($i,j\in\mathbb{N}$) ist eine unendliche Tabelle. Eine Reihenfolge ist eine Bijektion $\psi:\mathbb{N}\times\mathbb{N}\to\mathbb{N}$: Jedes Feld $(i,j)$ bekommt genau eine Nummer $k=\psi(i,j)$. Damit wird die __Doppelreihe__

$$\sum_{i,j=1}^\infty a_{ij}:=\sum_{k=1}^\infty a_{\psi^{-1}(k)}$$

zu einer gewöhnlichen Reihe über einen Index. Ist sie absolut konvergent, führt nach [Teil 6](/wissen/elektrotechnik/1-semester/hohere-mathematik-1/unendliche-reihen/unendliche-reihen.html) jede Umordnung zum selben Grenzwert, also jedes $\psi$. Insbesondere darf man zuerst zeilenweise oder zuerst spaltenweise summieren:

<span class="anker" id="gl-4-1"></span>
$$\sum_{i,j=1}^\infty a_{ij}=\sum_{i=1}^\infty\Bigl(\sum_{j=1}^\infty a_{ij}\Bigr)=\sum_{j=1}^\infty\Bigl(\sum_{i=1}^\infty a_{ij}\Bigr). \tag{4.1}$$

:::satz Satz 4.1 (Multiplikation von Reihen)
<span class="anker" id="satz-4-1"></span>

Seien $\sum_{n=1}^\infty a_n$ und $\sum_{m=1}^\infty b_m$ absolut konvergent. Dann ist die Doppelreihe absolut konvergent, und es gilt

$$\Bigl(\sum_{n=1}^\infty a_n\Bigr)\cdot\Bigl(\sum_{m=1}^\infty b_m\Bigr)=\sum_{n,m=1}^\infty a_nb_m.$$
:::

:::beweis Spaltenweise summieren
Absolute Konvergenz: Jede endliche Summe von Beträgen $|a_nb_m|$ ist höchstens $(\sum|a_n|)(\sum|b_m|)$. Die Teilsummen der Doppelreihe der Beträge steigen also monoton und sind beschränkt. Damit gilt [(4.1)](#gl-4-1). Der Faktor $\sum_na_n$ ist eine feste Zahl und darf in die Reihe über $m$ hinein:

$$\Bigl(\sum_na_n\Bigr)\sum_mb_m=\sum_mb_m\Bigl(\sum_na_n\Bigr)=\sum_m\Bigl(\sum_na_nb_m\Bigr)=\sum_{n,m}a_nb_m.$$
:::

:::satz Satz 4.2 (Cauchy-Produkt)
<span class="anker" id="satz-4-2"></span>

Seien $\sum_{n=0}^\infty a_nx^n$ und $\sum_{m=0}^\infty b_mx^m$ Potenzreihen mit Konvergenzradien $R$ und $S$. Dann hat ihr Produkt einen Konvergenzradius $T\ge\min(R,S)$, und mit $c_k:=\sum_{\ell=0}^ka_\ell b_{k-\ell}$ gilt

<span class="anker" id="gl-4-2"></span>
$$\Bigl(\sum_{n=0}^\infty a_nx^n\Bigr)\cdot\Bigl(\sum_{m=0}^\infty b_mx^m\Bigr)=\sum_{k=0}^\infty c_kx^k. \tag{4.2}$$

Für $x=1$ steht dort für absolut konvergente Reihen $\bigl(\sum a_n\bigr)\bigl(\sum b_m\bigr)=\sum_{k=0}^\infty c_k$.
:::

⁠**So liest man das:** $c_k$ sammelt alle Produkte, deren Indizes sich zu $k$ addieren: $c_0=a_0b_0$, $c_1=a_0b_1+a_1b_0$, $c_2=a_0b_2+a_1b_1+a_2b_0$. Das Produkt zweier Potenzreihen ist wieder eine Potenzreihe. **Grenzfall:** $T$ kann größer sein als $\min(R,S)$. Bei $(1-x)\sum x^n=1$ ist $R=\infty$, $S=1$, aber $T=\infty$.

:::beweis Nach Diagonalen sortieren
Für $|x|<\min(R,S)$ sind beide Reihen absolut konvergent (Stufe [1](der-konvergenzkreis.html#stufe-1)). Nach dem vorigen Satz ist das Produkt die absolut konvergente Doppelreihe $\sum_{n,m}a_nb_mx^{n+m}$. Ihre Reihenfolge ist frei, also sammelt man alle Felder mit $n+m=k$. Das sind die Glieder $a_\ell b_{k-\ell}x^k$ mit $\ell=0,\dots,k$.
:::

⁠**Warum die absolute Konvergenz nötig ist:** $a_n=b_n=(-1)^n/\sqrt{n+1}$ ergibt eine konvergente Reihe (Leibniz), aber nicht absolut. In $c_k$ haben alle $k+1$ Summanden dasselbe Vorzeichen, und jeder hat mindestens den Betrag $\frac2{k+2}$. Also ist $|c_k|\ge1$ (zum Beispiel $c_{10}=2{,}29$), und $\sum c_k$ divergiert.

::::beispiel
Für $a_n=b_n=1$ und $|x|<1$ ist $c_k=k+1$, also $\frac1{(1-x)^2}=\sum_{k=0}^\infty(k+1)x^k$. Bei $x=\frac12$ ergibt beides 4.
::::

:::satz Satz 4.3 (Binomische Formel)
<span class="anker" id="satz-4-3"></span>

Für $n\in\mathbb{N}$ und $a,b\in\mathbb{C}$ gilt mit dem __Binomialkoeffizienten__ $\binom nk:=\frac{n!}{k!\,(n-k)!}$ und $0!:=1$:

<span class="anker" id="gl-4-3"></span>
$$(a+b)^n=\sum_{k=0}^n\binom nk a^kb^{n-k}. \tag{4.3}$$
:::

⁠**So liest man das:** Für $n=2$ steht dort $b^2+2ab+a^2$. Der Mechanismus: Beim Ausmultiplizieren wählt man aus jeder der $n$ Klammern $a$ oder $b$. Das Produkt $a^kb^{n-k}$ entsteht so oft, wie man $k$ Klammern auswählen kann: $n(n-1)\cdots(n-k+1)$ geordnete Möglichkeiten, geteilt durch die $k!$ Reihenfolgen. Das benutzt nur Körperaxiome, also gilt es auch in $\mathbb{C}$. **Probe:** $(1+\mathrm{i})^4=1+4\mathrm{i}+6\mathrm{i}^2+4\mathrm{i}^3+\mathrm{i}^4=-4$ wie in [Teil 2](/wissen/elektrotechnik/1-semester/hohere-mathematik-1/komplexe-zahlen/komplexe-zahlen.html).

:::frage Warum nach Diagonalen und nicht zeilenweise?
Zeilenweise ist auch richtig, ergibt aber nur Zahl mal Reihe. Erst die Diagonalen machen aus dem Produkt wieder eine Potenzreihe.
:::

:::aufgabe Aufgabe 4 ★★ Cauchy-Produkt anwenden
<span class="anker" id="aufg-4"></span>

(a) Berechne $c_0$ bis $c_3$ und allgemein $c_k$ für $\bigl(\sum x^n\bigr)\bigl(\sum(-1)^mx^m\bigr)$ und vergleiche mit $1/(1-x^2)$. (b) Berechne $(1+\mathrm{i})^6$ mit [(4.3)](#gl-4-3) und prüfe mit $(1+\mathrm{i})^2=2\mathrm{i}$. (c) Grenzfall: Bestimme $T$ für $(1+x)\sum(-x)^n$.

:::loesung
(a) $a_n=1$, $b_m=(-1)^m$: $c_k=\sum_{\ell=0}^k(-1)^{k-\ell}$. Das ergibt $c_0=1$, $c_1=0$, $c_2=1$, $c_3=0$, allgemein 1 für gerades und 0 für ungerades $k$. Das Produkt ist $1+x^2+x^4+\dots=\frac1{1-x^2}$, passend zu $\frac1{1-x}\cdot\frac1{1+x}$. (b) $(1+\mathrm{i})^6=1+6\mathrm{i}+15\mathrm{i}^2+20\mathrm{i}^3+15\mathrm{i}^4+6\mathrm{i}^5+\mathrm{i}^6=1+6\mathrm{i}-15-20\mathrm{i}+15+6\mathrm{i}-1=-8\mathrm{i}$. Probe: $(2\mathrm{i})^3=-8\mathrm{i}$. (c) $c_0=1$ und $c_k=b_k+b_{k-1}=0$ für $k\ge1$. Das Produkt ist 1, also $T=\infty$ bei $\min(R,S)=1$.
:::
:::
