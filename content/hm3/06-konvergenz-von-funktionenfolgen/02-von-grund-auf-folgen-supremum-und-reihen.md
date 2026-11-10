---
title: Von Grund auf: Folgen, Supremum und Reihen
pfad: Elektrotechnik / 3. Semester / HöMa3 – Höhere Mathematik 3 / Konvergenz von Funktionenfolgen
adresse: elektrotechnik/3-semester/hohere-mathematik-3/konvergenz-von-funktionenfolgen
knoten: Kapitel 6: Konvergenz von Funktionenfolgen
order: 3160200
summary: Funktionenfolgen werden auf Zahlenfolgen zurückgeführt.
tags: Konvergenz, Cauchy-Folge, Supremum, beschränkt, Partialsumme, Reihe, absolut konvergent, Rest
lang: de
---

:::zweck
Funktionenfolgen werden auf Zahlenfolgen zurückgeführt. Hier stehen die Tatsachen über Zahlen, die dieses Kapitel benutzt.
:::

**Konvergenz.** __Konvergenz__ einer Zahlenfolge $(s_n)_{n\in\mathbb{N}}$ aus $\mathbb{R}$ oder $\mathbb{C}$ gegen $s$ heißt: Zu jedem $\varepsilon>0$ gibt es ein $N\in\mathbb{N}$ mit $|s_n-s|<\varepsilon$ für alle $n\ge N$. Man schreibt $s_n\to s$ für $n\to\infty$. Ab dem Index $N$ bleiben also alle Glieder näher als $\varepsilon$ am Grenzwert.

**Cauchy-Folgen.** Eine __Cauchy-Folge__ ist eine Folge, deren Glieder einander beliebig nahe kommen: Zu jedem $\varepsilon>0$ gibt es ein $N$ mit $|s_m-s_n|<\varepsilon$ für alle $m,n\ge N$. Kurz: $|s_m-s_n|\to0$ für $m,n\to\infty$. Jede konvergente Folge ist eine Cauchy-Folge. In $\mathbb{R}$ und $\mathbb{C}$ gilt auch die Umkehrung, und das ist die Vollständigkeit dieser Zahlbereiche. In den rationalen Zahlen fehlt sie: $1;\ 1{,}4;\ 1{,}41;\ 1{,}414;\dots$ ist eine Cauchy-Folge aus $\mathbb{Q}$, aber ihr Grenzwert $\sqrt2$ liegt nicht in $\mathbb{Q}$.

**Supremum.** Das __Supremum__ $\sup M$ einer nach oben beschränkten Menge $M\subset\mathbb{R}$ ist ihre kleinste obere Schranke. Anders als das Maximum muss es nicht zur Menge gehören: $\sup\{x:0<x<1\}=1$, ein Maximum gibt es dort nicht. Eine Funktion $f$ auf $[a,b]$ heißt __beschränkt__, wenn $\sup_{x\in[a,b]}|f(x)|<\infty$ gilt. Jede stetige Funktion auf $[a,b]$ ist beschränkt und nimmt ihr Maximum an.

**Reihen.** Eine __Partialsumme__ ist eine endliche Summe $\sum_{k=0}^ns_k$, eine __Reihe__ $\sum_{k=0}^\infty s_k$ der Grenzwert der Partialsummen. Sie heißt __absolut konvergent__, wenn $\sum_{k=0}^\infty|s_k|<\infty$ gilt, und dann konvergiert sie auch selbst. Der __Rest__ $\sum_{k=m+1}^\infty s_k$ einer konvergenten Reihe strebt für $m\to\infty$ gegen null. Zum Vergleich dienen die __geometrische Reihe__ $\sum_{k=0}^\infty q^k=1/(1-q)$ für $|q|<1$ sowie $\sum_{k=1}^\infty1/k^2<\infty$ und $\sum_{k=1}^\infty1/k=\infty$. Liegen die Beträge der Glieder unter den Gliedern einer konvergenten Reihe, konvergiert die Reihe absolut.

**Abschätzen.** Die __Dreiecksungleichung__ $|s+t|\le|s|+|t|$ gilt in $\mathbb{R}$ und $\mathbb{C}$. Das Integral ist monoton: Aus $g\le h$ auf $[a,b]$ folgt $\int_a^bg\,\mathrm{d} x\le\int_a^bh\,\mathrm{d} x$. Damit gilt $\bigl|\int_a^bf\,\mathrm{d} x\bigr|\le\int_a^b|f|\,\mathrm{d} x\le(b-a)\sup_{x\in[a,b]}|f(x)|$.
