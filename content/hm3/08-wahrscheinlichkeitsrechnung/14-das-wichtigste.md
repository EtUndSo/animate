---
title: Das Wichtigste
pfad: Elektrotechnik / 3. Semester / HöMa3 – Höhere Mathematik 3 / Wahrscheinlichkeitsrechnung
adresse: elektrotechnik/3-semester/hohere-mathematik-3/wahrscheinlichkeitsrechnung
knoten: Kapitel 8: Wahrscheinlichkeitsrechnung
order: 3181400
summary: Was sich über den Zufall exakt sagen lässt
tags: 
lang: de
---

:::kern Das Wichtigste
<ul>

<li>

$(\Omega,\mathcal E,\mathbb{P})$: $\mathcal E$ ist eine $\sigma$-Algebra, $\mathbb{P}$ ist $\sigma$-additiv mit $\mathbb{P}(\Omega)=1$. Laplace: $\mathbb{P}(A)=|A|/|\Omega|$. Urne: $n^k$, $n!/(n-k)!$, $\binom nk$, $\binom{n+k-1}k$.

</li>

<li>

$\mathbb{P}(A|B)=\mathbb{P}(A\cap B)/\mathbb{P}(B)$. Unabhängig: $\mathbb{P}(A\cap B)=\mathbb{P}(A)\,\mathbb{P}(B)$. Total: $\mathbb{P}(B)=\sum_i\mathbb{P}(B|A_i)\,\mathbb{P}(A_i)$. Bayes: $\mathbb{P}(A_k|B)=\mathbb{P}(B|A_k)\,\mathbb{P}(A_k)/\mathbb{P}(B)$.

</li>

<li>

$F_X(x)=\mathbb{P}(X\le x)$ steigt, ist rechtsseitig stetig, von 0 nach 1. $\mathbb{P}(a<X\le b)=F_X(b)-F_X(a)=\int_a^bf_X\,\mathrm{d} x$.

</li>

<li>

Binomial $\binom nkp^k(1-p)^{n-k}$, Poisson $\lambda^k\mathrm{e}^{-\lambda}/k!$, hypergeometrisch $\binom Mk\binom{N-M}{n-k}/\binom Nn$, normal $\mathbb{P}(X\le x)=\Phi((x-\mu)/\sigma)$.

</li>

<li>

$\mathbb{E}(X)=\sum_kx_k\,\mathbb{P}(X=x_k)$ oder $\int_\mathbb{R} xf_X\,\mathrm{d} x$, immer linear. $\operatorname{Var}(X)=\mathbb{E}(X^2)-\mathbb{E}(X)^2$, $\operatorname{Var}(X+Y)=\operatorname{Var}(X)+\operatorname{Var}(Y)+2\operatorname{Cov}(X,Y)$. Tschebyschew: $\mathbb{P}(|X-\mu|\ge\varepsilon)\le\sigma^2/\varepsilon^2$.

</li>

<li>

Unabhängig: $F_{X,Y}=F_XF_Y$, $f_{X,Y}=f_Xf_Y$, $\mathbb{E}(XY)=\mathbb{E}(X)\,\mathbb{E}(Y)$, also unkorreliert. Randdichte: $f_X(x)=\int_\mathbb{R} f(x,y)\,\mathrm{d} y$.

</li>

<li>

Große Zahlen: $\operatorname{Var}(\overline X_n)=\sigma^2/n$, $\overline X_n\to\mu$ stochastisch und, für i.i.d., fast sicher.

</li>

<li>

Grenzwertsatz: $S_n^*=(S_n-n\mu)/(\sqrt n\,\sigma)$ erfüllt $\mathbb{P}(S_n^*\le x)\to\Phi(x)$.

</li>

</ul>
:::

:::merke Die Antwort in drei Sätzen
<ol>

<li>

Wahrscheinlichkeiten verhalten sich wie Anteile an einem Ganzen, und aus dieser einen Annahme folgen alle Rechenregeln vom Urnenmodell bis zur Formel von Bayes.

</li>

<li>

Eine Zufallsvariable ist durch ihre Verteilung beschrieben, und zwei Zahlen fassen sie zusammen: der Erwartungswert die Lage, die Varianz die Breite.

</li>

<li>

Mittelt man $n$ unabhängige Wiederholungen, schrumpft die Streuung wie $\sigma/\sqrt n$, der Mittelwert läuft gegen $\mu$, und die Restabweichung folgt immer derselben Glocke.

</li>

</ol>
:::

**Ein Prinzip hinter allen Ergebnissen.** $\mathbb{P}$ ist ein Maß und $\mathbb{E}$ das Integral dazu. Unabhängigkeit zerlegt Summen und Integrale in Faktoren.

| Ergebnis | Woher es kommt |
|---|---|
| Rechenregeln, Stetigkeit | $\sigma$-Additivität auf disjunkten Zerlegungen |
| Total, Bayes | Zerlegung von $\Omega$ und Multiplikationsregel |
| $\mathbb{E}(XY)=\mathbb{E}(X)\,\mathbb{E}(Y)$ | Doppelsumme zerfällt in ein Produkt |
| Gesetz der großen Zahlen | $\operatorname{Var}(\overline X_n)=\sigma^2/n$ plus Tschebyschew |
| Zentraler Grenzwertsatz | Vom Faktor bleibt nur $1-t^2/(2n)$, also Mittel und Varianz |
