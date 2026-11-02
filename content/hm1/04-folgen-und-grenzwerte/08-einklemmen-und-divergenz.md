---
title: Stufe 6: Einklemmen und Divergenz
pfad: Elektrotechnik / 1. Semester / Höhere Mathematik 1 / Folgen und Grenzwerte
order: 1240800
summary: sqrt[n] n lässt sich nicht in Summen und Produkte zerlegen.
tags: divergent, bestimmt divergent, unbestimmt divergent
lang: de
---

<span class="anker" id="stufe-6"></span>

:::zweck
$\sqrt[n]{n}$ lässt sich nicht in Summen und Produkte zerlegen. Diese Stufe zeigt die Konvergenz durch Einklemmen und gibt den Folgen ohne Grenzwert ihre Namen.
:::

**Die Idee.** Läuft eine Folge zwischen zwei anderen, die zum selben Ziel laufen, bleibt ihr keine andere Wahl. Für große $n$ liegen beide Nachbarn im Schlauch um $a$, und die eingeklemmte Folge liegt zwischen ihnen (Abb. [7](#abb-7)).

:::satz Satz 6.1 (Sandwich-Lemma)
<span class="anker" id="satz-6-1"></span>

Für $\{a_n\}$, $\{b_n\}$, $\{c_n\}$ gebe es ein $N_0\in\mathbb{N}$, so dass

<span class="anker" id="gl-6-1"></span>
$$c_n\le a_n\le b_n\quad\forall\,n>N_0\qquad\text{und}\qquad\lim_{n\to\infty}c_n=\lim_{n\to\infty}b_n=a. \tag{6.1}$$

Dann ist $\{a_n\}$ konvergent mit $\lim_{n\to\infty}a_n=a$.
:::

⁠**So liest man das:** $a_n$ wird von unten und oben eingeklemmt, ohne dass man über $a_n$ selbst mehr wissen muss. Die Pendelfolge liegt zwischen $2-\frac3n$ und $2+\frac3n$, also gilt $a_n\to2$ ohne jedes $\varepsilon$. **Voraussetzung nötig:** Die beiden Grenzwerte müssen gleich sein. Aus $-1\le(-1)^n\le1$ folgt nichts. **Grenzfall:** Für $c_n=0$ und $a=0$ ergibt sich das Vergleichskriterium für $0\le a_n\le b_n$.

:::beweis Sandwich-Lemma
Sei $\varepsilon>0$. Wegen [(6.1)](#gl-6-1) gibt es $N_1$ und $N_2$ mit $-\varepsilon<c_n-a<\varepsilon$ für $n>N_1$ und $-\varepsilon<b_n-a<\varepsilon$ für $n>N_2$. Für $n>\tilde N_0:=\max\{N_0,N_1,N_2\}$ folgt $-\varepsilon<c_n-a\le a_n-a\le b_n-a<\varepsilon$, also $|a_n-a|<\varepsilon$.
:::

:::satz Satz 6.2 (Zwei $n$-te Wurzeln)
<span class="anker" id="satz-6-2"></span>

Es gilt (a) $\lim_{n\to\infty}\sqrt[n]{x}=1$ für jedes $x>0$, (b) $\lim_{n\to\infty}\sqrt[n]{n}=1$.
:::

⁠**So liest man das:** Die Wurzel $\sqrt[n]{x}$ ist die positive Zahl, deren $n$-te Potenz $x$ ergibt. Teil (a) sagt: Mit wachsendem $n$ reicht eine Zahl nahe 1, um durch Potenzieren jedes feste $x$ zu erreichen. Teil (b) sagt das sogar für das wachsende $n$ selbst.

:::beweis Einklemmen mit Bernoulli
(b) Für $k>0$ und $n\ge2$ gibt Bernoulli zweimal

$$(1+k)^{2n}=(1+k)^n\cdot(1+k)^n>(1+nk)(1+nk)>n^2k^2.$$

Sei $n\ge2$ und $k:=\sqrt[2n]{n}-1>0$. Dann ist $(1+k)^{2n}=n$, also $n>n^2k^2$ und damit $k<\frac1{\sqrt n}$. Das heißt $1\le\sqrt[2n]{n}<1+\frac1{\sqrt n}$, und Quadrieren ergibt

$$1\le\sqrt[n]{n}<\Bigl(1+\frac1{\sqrt n}\Bigr)^2.$$

Rechts steht nach den Rechenregeln eine Folge mit Grenzwert $(1+0)^2=1$. Das Sandwich-Lemma gibt (b).

(a) Für $x=1$ ist $\sqrt[n]{1}=1$. Für $x>1$ und $n>x$ gilt $1\le\sqrt[n]{x}\le\sqrt[n]{n}$, weil die Wurzel streng monoton wächst. Das Sandwich-Lemma und (b) ergeben die Behauptung. Für $0<x<1$ setzt man $y=\frac1x>1$. Dann ist $\sqrt[n]{x}=1/\sqrt[n]{y}\to1$ nach Rechenregel (iii).

Die Reihenfolge ist wichtig: (a) benutzt (b). Der Beweis von (b) darf deshalb (a) nicht benutzen, sonst setzte er voraus, was er zeigen soll.
:::

⁠**Zahlen:** $\sqrt[n]{n}=1{,}2589;\ 1{,}0471;\ 1{,}0069$ für $n=10;\ 100;\ 1000$, die obere Schranke ist dort $1{,}7325;\ 1{,}2100;\ 1{,}0642$.

:::abbildung hm1/k4sandwich 7
Die Folge $\sqrt[n]{n}$ (blau) zwischen der konstanten Folge 1 (grün) und $(1+1/\sqrt n)^2$ (orange). Beide Nachbarn streben gegen 1, die mittlere hat keine andere Wahl. Ihr größter Wert ist $\sqrt[3]{3}=1{,}442$.
:::

**Folgen ohne Grenzwert.** Nicht jede Folge hat einen Grenzwert, und es gibt zwei Arten, ihn zu verfehlen.

:::definition Definition 6.3 (Konvergenz und Divergenz)
<span class="anker" id="satz-6-3"></span>

<ol class="rm">

<li>

Die Folge $\{a_n\}$ heißt konvergent, falls es eine Zahl $a\in\mathbb{R}$ gibt mit $\lim_{n\to\infty}a_n=a$.

</li>

<li>

Folgen, die nicht konvergent sind, heißen __divergent__, und zwar __bestimmt divergent__, falls $a_n\to\infty$ oder $a_n\to-\infty$, und __unbestimmt divergent__ in allen anderen Fällen.

</li>

</ol>

Dabei bedeutet $a_n\to\infty$: $\forall\,M>0\ \exists\,n_0\in\mathbb{N}$ mit $a_n>M$ für alle $n>n_0$. Entsprechend bedeutet $a_n\to-\infty$: $\forall\,M>0\ \exists\,n_0\in\mathbb{N}$ mit $a_n<-M$ für alle $n>n_0$.
:::

⁠**So liest man das:** $n^2$ ist bestimmt divergent: Zu jeder Höhe $M$ gibt es einen Index, ab dem alle Glieder darüber bleiben. $(-1)^n$ ist unbestimmt divergent. Das Wort „konvergent“ fordert nur, dass es ein $a$ *gibt*, man muss es nicht kennen. Die Bedingung $a\in\mathbb{R}$ sieht harmlos aus, ihr Gewicht zeigt Stufe [7](monotone-folgen-und-die-vollstandigkeit.html#stufe-7).

:::frage Ist eine unbeschränkte Folge immer bestimmt divergent?
Nein. $(-1)^n\,n$ ist unbeschränkt und springt zwischen großen positiven und großen negativen Werten. Bestimmt divergent verlangt, dass ab einem Index alle Glieder jenseits von $M$ bleiben.
:::

:::aufgabe Aufgabe 8 ★★ Einklemmen und einordnen
<span class="anker" id="aufg-8"></span>

(a) Zeige mit dem Sandwich-Lemma, dass $\sqrt[n]{2^n+5^n}\to5$. Berechne $n=1$ und $n=10$ zur Kontrolle. (b) Ordne ein: konvergent, bestimmt oder unbestimmt divergent? $(-2)^n$; $\sqrt[n]{7}+(-1)^n/n$; $\sqrt{n}\,$; $\frac{n^2}{n+1}$.

:::loesung
(a) Es ist $5^n\le2^n+5^n\le2\cdot5^n$, also $5\le\sqrt[n]{2^n+5^n}\le5\sqrt[n]{2}$, und rechts geht es gegen 5. Zahlen: $n=1$ ergibt 7, $n=10$ ergibt $5{,}00005$ bei der Schranke $5{,}359$. (b) $(-2)^n$: unbeschränkt mit wechselndem Vorzeichen, unbestimmt divergent. $\sqrt[n]{7}+(-1)^n/n\to1+0=1$: konvergent. $\sqrt n$: Für $n>M^2$ ist $\sqrt n>M$, bestimmt divergent. $\frac{n^2}{n+1}\ge\frac{n^2}{2n}=\frac n2$: bestimmt divergent.
:::
:::
