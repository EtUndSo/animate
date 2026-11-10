---
title: Stufe 1: Eine Reihe ist eine Folge
pfad: Elektrotechnik / 1. Semester / HöMa1 – Höhere Mathematik 1 / Unendliche Reihen
adresse: elektrotechnik/1-semester/hohere-mathematik-1/unendliche-reihen
knoten: Kapitel 6: Unendliche Reihen
order: 1260300
summary: Unendlich viele Zahlen kann niemand der Reihe nach addieren.
tags: unendliche Reihe, Partialsumme, Glieder, konvergiert, divergent, Teleskopsumme
lang: de
---

<span class="anker" id="stufe-1"></span>

:::zweck
Unendlich viele Zahlen kann niemand der Reihe nach addieren. Diese Stufe legt fest, was eine Summe ohne Ende bedeutet, und rechnet den wichtigsten Fall aus.
:::

**Die Idee.** Man addiert nicht alle Zahlen, sondern die ersten $N$, und beobachtet, was mit wachsendem $N$ geschieht. So entsteht eine Treppe: Jeder Summand ist eine Stufe, die Höhe nach $N$ Stufen ist die Teilsumme. Strebt die Höhe gegen einen festen Wert, heißt dieser Wert die Summe (Abb. [1](#abb-1)). Neues braucht man dazu nicht: Die Höhen sind eine Folge, und für Folgen ist „Grenzwert“ seit [Kapitel 4](/wissen/elektrotechnik/1-semester/hohere-mathematik-1/folgen-und-grenzwerte/folgen-und-grenzwerte.html) erklärt.

:::definition Definition 1.1 (Reihe, Teilsumme, Konvergenz)
<span class="anker" id="satz-1-1"></span>

Zu einer reellen Folge $\{a_n\}_{n\in\mathbb{N}}$ bildet man

<span class="anker" id="gl-1-1"></span>
$$S_N:=\sum_{n=1}^Na_n=a_1+\dots+a_N\in\mathbb{R}. \tag{1.1}$$

Die neue Folge $\{S_N\}_{N\in\mathbb{N}}$ heißt __unendliche Reihe__ oder kurz Reihe. Die Zahl $S_N$ heißt $N$-te Teilsumme oder __Partialsumme__, die $a_n$ heißen __Glieder__ der Reihe. Die Reihe __konvergiert__ mit Grenzwert $S$, wenn

<span class="anker" id="gl-1-2"></span>
$$\lim_{N\to\infty}S_N=S \tag{1.2}$$

gilt. Existiert dieser Grenzwert in $\mathbb{R}$ nicht, heißt die Reihe __divergent__.
:::

⁠**So liest man das:** $a_n$ ist die Stufe Nummer $n$, $S_N$ die Höhe danach. Bei der harmonischen Reihe ist $a_3=\frac13$ und $S_3=H_3=1{,}833$. Der Index $n$ zählt die Summanden, $N$ sagt, wo man aufhört. Zwischen den Folgen besteht der Zusammenhang $a_n=S_n-S_{n-1}$ für $n\ge2$. Das Symbol $\sum_{n=1}^\infty a_n$ steht für zweierlei: für die Folge $\{S_N\}$ und, falls sie konvergiert, für ihren Grenzwert $S$. Es ist keine Addition unendlich vieler Zahlen. Der Index muss nicht bei 1 beginnen: $\sum_{n=p}^\infty a_n$ mit $p\in\mathbb{Z}$ meint die Folge $\bigl\{\sum_{n=p}^Na_n\bigr\}_{N=p}^\infty$. Ein anderer Start verschiebt alle Teilsummen um dieselbe Zahl. Das ändert den Wert, aber nie die Konvergenz. Divergent heißt nur „kein Grenzwert in $\mathbb{R}$“: Die Höhe kann über alle Grenzen wachsen wie bei $1+1+1+\dots$ oder pendeln wie bei $1-1+1-\dots$

:::abbildung hm1/k6treppe 1
Teilsummen als Treppe, die Punkte sind die Höhen $S_N$. Links die Halbierungsreihe: Jede Stufe halbiert den Rest bis zur Decke 2. Rechts die harmonische Reihe: Die Stufen schrumpfen ebenfalls, eine Decke gibt es nicht. Rot die Stufe $a_1$ beziehungsweise $a_2$.
:::

:::satz Satz 1.2 (Geometrische Reihe)
<span class="anker" id="satz-1-2"></span>

Für $q\in\mathbb{R}$ mit $|q|<1$ konvergiert die geometrische Reihe, und es gilt

<span class="anker" id="gl-1-3"></span>
$$\sum_{n=0}^\infty q^n=\lim_{N\to\infty}\sum_{n=0}^Nq^n=\frac1{1-q}. \tag{1.3}$$
:::

⁠**So liest man das:** $q$ ist das Verhältnis benachbarter Glieder, das Glied mit $n=0$ ist 1. Für $q=\frac13$ steht dort $1+\frac13+\frac19+\dots=\frac32$. Bedingung ist $|q|<1$, für $|q|\ge1$ divergiert die Reihe (Stufe [2](nullfolge-notig-aber-nicht-genug.html#stufe-2)).

:::beweis Grenzübergang in der geometrischen Summe
Nach [Kapitel 4](/wissen/elektrotechnik/1-semester/hohere-mathematik-1/folgen-und-grenzwerte/folgen-und-grenzwerte.html) ist $S_N=\sum_{n=0}^Nq^n=\frac{1-q^{N+1}}{1-q}$. Für $|q|<1$ ist $q^{N+1}$ eine Nullfolge, die Rechenregeln ergeben $S_N\to\frac1{1-q}$.
:::

::::beispiel
Für $q=\frac12$ ist $G_N=2-(\frac12)^N$ mit $G_{10}=1{,}99902$, der Grenzwert ist $\frac1{1-1/2}=2$. Für $q=-\frac12$ pendeln die Teilsummen $1;\ 0{,}5;\ 0{,}75;\ 0{,}625;\ \dots$ um den Wert $\frac23$. Für $q=0{,}9$ ist der Wert 10, aber $S_{10}=6{,}862$: Erst $N=43$ unterschreitet 1 % Abstand, denn der Abstand zum Grenzwert ist der Anteil $0{,}9^{N+1}$ von $S$. In einer Schleife mit Umlauffaktor $q$ ist $\frac1{1-q}$ die Gesamtverstärkung, jeder Umlauf liefert einen Summanden.
::::

⁠**Grenzfälle:** Für $q=0$ bleibt nur das Glied 1 und die Formel gibt 1. Für $q\to1$ wächst $\frac1{1-q}$ über jede Grenze, passend zu $1+1+1+\dots$

:::frage Ist $0{,}999\dots$ wirklich gleich 1, oder nur fast?
Keine Teilsumme $0{,}9;\ 0{,}99;\ 0{,}999;\ \dots$ erreicht die 1. Das Symbol $0{,}999\dots$ meint aber nicht eine dieser Zahlen, sondern ihren Grenzwert: $\frac9{10}\sum_{n=0}^\infty(\frac1{10})^n=\frac9{10}\cdot\frac{10}9=1$. Beide Schreibweisen bezeichnen genau dieselbe Zahl.
:::

:::aufgabe Aufgabe 1 ★ Erste Reihen
<span class="anker" id="aufg-1"></span>

<ol class="al">

<li>

Schreibe $0{,}272727\dots$ als geometrische Reihe und daraus als Bruch.

</li>

<li>

Berechne $\sum_{n=3}^\infty(\frac23)^n$. Klammere dazu zuerst $(\frac23)^3$ aus.

</li>

<li>

Zeige mit $\frac1{n(n+1)}=\frac1n-\frac1{n+1}$, dass $\sum_{n=1}^N\frac1{n(n+1)}=1-\frac1{N+1}$ ist (eine __Teleskopsumme__, [Kapitel 4](/wissen/elektrotechnik/1-semester/hohere-mathematik-1/folgen-und-grenzwerte/folgen-und-grenzwerte.html)), und gib den Wert der Reihe an.

</li>

</ol>

:::loesung
(a) $0{,}2727\ldots=\frac{27}{100}\sum_{n=0}^\infty(\frac1{100})^n=\frac{27}{100}\cdot\frac{100}{99}=\frac{27}{99}=\frac3{11}$. (b) $(\frac23)^3\sum_{n=0}^\infty(\frac23)^n=\frac8{27}\cdot3=\frac89$. (c) In $\sum_{n=1}^N(\frac1n-\frac1{n+1})$ heben sich alle inneren Glieder auf, es bleibt $1-\frac1{N+1}$. Der Wert der Reihe ist 1.
:::
:::
