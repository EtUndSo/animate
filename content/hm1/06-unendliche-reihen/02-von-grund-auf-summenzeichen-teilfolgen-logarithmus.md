---
title: Von Grund auf: Summenzeichen, Teilfolgen, Logarithmus
pfad: Elektrotechnik / 1. Semester / HöMa1 – Höhere Mathematik 1 / Unendliche Reihen
adresse: elektrotechnik/1-semester/hohere-mathematik-1/unendliche-reihen
knoten: Kapitel 6: Unendliche Reihen
order: 1260200
summary: Wann hat eine Summe ohne Ende einen Wert?
tags: Teilfolge
lang: de
---

⁠**Summenzeichen.** $\sum_{n=1}^Na_n$ heißt: Setze für den Laufindex $n$ der Reihe nach $1,2,\dots,N$ ein und addiere. Der Name des Laufindex spielt keine Rolle, $\sum_{n=1}^3n^2=\sum_{\ell=1}^3\ell^2=14$. Die Dreiecksungleichung aus [Kapitel 1](/wissen/elektrotechnik/1-semester/hohere-mathematik-1/mengen-logik-und-reelle-zahlen/mengen-logik-und-reelle-zahlen.html) gilt für endlich viele Summanden: $\bigl|\sum_{n=m}^Na_n\bigr|\le\sum_{n=m}^N|a_n|$.

⁠**Aus [Kapitel 4](/wissen/elektrotechnik/1-semester/hohere-mathematik-1/folgen-und-grenzwerte/folgen-und-grenzwerte.html)** werden gebraucht: die geometrische Summe $\sum_{n=0}^Nq^n=\frac{1-q^{N+1}}{1-q}$ für $q\ne1$, das Monotonie-Lemma (monoton und beschränkt ergibt konvergent), die Aussage „in $\mathbb{R}$ ist eine Folge genau dann konvergent, wenn sie eine Cauchy-Folge ist“, die Rechenregeln für Grenzwerte sowie $q^n\to0$ für $|q|<1$ und $\sqrt[n]{n}\to1$.

⁠**Teilfolge.** Streicht man aus einer Folge Glieder und behält die Reihenfolge bei, entsteht eine __Teilfolge__ $\{a_{n_k}\}_{k\in\mathbb{N}}$ mit Indizes $n_1<n_2<\dots$ Weil die $n_k$ streng wachsende natürliche Zahlen sind, gilt $n_k\ge k$. Konvergiert $a_n\to a$, gilt deshalb auch $a_{n_k}\to a$: Für $k>N_0$ ist $n_k>N_0$, das Glied liegt also im Schlauch. Umgekehrt sagt eine einzelne Teilfolge nichts über die ganze Folge: $0;\,1;\,0;\,1;\,\dots$ hat die konstanten Teilfolgen 0 und 1.

⁠**Logarithmus und Potenzen.** Der natürliche Logarithmus $\log x$ ist für $x>0$ die Umkehrfunktion von $\mathrm{e}^x$ ([Kapitel 5](/wissen/elektrotechnik/1-semester/hohere-mathematik-1/exponentialfunktion-und-stetigkeit/exponentialfunktion-und-stetigkeit.html)). In der Elektrotechnik heißt er meist $\log x$, die Basis 10 ist hier nie gemeint. Er wächst streng monoton, es gilt $\log(2^k)=k\log2$ und $\log2=0{,}693$. Für $s\in\mathbb{R}$ und $x>0$ ist $x^s:=\mathrm{e}^{s\log x}$. Für $s>0$ wächst $x^s$ streng monoton in $x$, und es gilt $(2^k)^s=(2^s)^k$.

⁠**Kontraposition.** Aus „$A$ ergibt $B$“ folgt „nicht $B$ ergibt nicht $A$“ ([Kapitel 1](/wissen/elektrotechnik/1-semester/hohere-mathematik-1/mengen-logik-und-reelle-zahlen/mengen-logik-und-reelle-zahlen.html)).

::::formelsammlung
**Summenzeichen**

$$\sum_{n=1}^Na_n=a_1+\dots+a_N$$

Für den Laufindex $n$ der Reihe nach $1,2,\dots,N$ einsetzen und addieren; der Name des Laufindex spielt keine Rolle.

**Dreiecksungleichung für endlich viele Summanden**

$$\bigl|\sum_{n=m}^Na_n\bigr|\le\sum_{n=m}^N|a_n|$$

Der Betrag einer endlichen Summe ist höchstens die Summe der Beträge.

**Geometrische Summe**

$$\sum_{n=0}^Nq^n=\frac{1-q^{N+1}}{1-q}$$

Für $q\ne1$ ([Kapitel 4](/wissen/elektrotechnik/1-semester/hohere-mathematik-1/folgen-und-grenzwerte/folgen-und-grenzwerte.html)).

**Werkzeuge aus [Kapitel 4](/wissen/elektrotechnik/1-semester/hohere-mathematik-1/folgen-und-grenzwerte/folgen-und-grenzwerte.html)**

$$q^n\to0\quad\text{für }|q|<1,\qquad\sqrt[n]{n}\to1$$

Dazu das Monotonie-Lemma (monoton und beschränkt ergibt konvergent), die Rechenregeln für Grenzwerte und: In $\mathbb{R}$ ist eine Folge genau dann konvergent, wenn sie eine Cauchy-Folge ist.

**Teilfolge**

$$\{a_{n_k}\}_{k\in\mathbb{N}},\quad n_1<n_2<\dots,\qquad n_k\ge k$$

Glieder streichen, Reihenfolge behalten. Aus $a_n\to a$ folgt $a_{n_k}\to a$; eine einzelne Teilfolge sagt aber nichts über die ganze Folge.

**Logarithmus**

$$\log(2^k)=k\log2,\qquad\log2=0{,}693$$

$\log x$ ist für $x>0$ der natürliche Logarithmus, die Umkehrfunktion von $\mathrm{e}^x$; er wächst streng monoton. Die Basis 10 ist nie gemeint.

**Potenz mit reellem Exponenten**

$$x^s:=\mathrm{e}^{s\log x},\qquad(2^k)^s=(2^s)^k$$

Für $s\in\mathbb{R}$ und $x>0$; für $s>0$ wächst $x^s$ streng monoton in $x$.
::::

::::lernkarten
:::karte formel Summenzeichen
Was bedeutet die Schreibweise $\sum_{n=1}^Na_n$, und welche Rolle spielt dabei der Name des Laufindex?
---
Man setzt für den Laufindex $n$ der Reihe nach $1,2,\dots,N$ ein und addiert. Der Name des Laufindex spielt keine Rolle: $\sum_{n=1}^3n^2=\sum_{\ell=1}^3\ell^2=14$.
--- falsch
Man setzt für den Laufindex $n$ der Reihe nach $1,2,\dots,N$ ein und multipliziert. Der Name des Laufindex spielt keine Rolle: Für $n^2$ und $N=3$ ergibt sich $1\cdot4\cdot9=36$.
--- falsch
Man addiert die Glieder $a_1,\dots,a_N$. Der Laufindex muss aber $n$ heißen, denn mit einem anderen Buchstaben ergibt $\sum_{\ell=1}^3\ell^2$ eine andere Zahl als $\sum_{n=1}^3n^2$.
--- falsch
Man addiert nur das erste und das letzte Glied, also $a_1+a_N$. Der Name des Laufindex spielt keine Rolle: $\sum_{n=1}^3n^2=1+9=10$.
:::
:::karte formel Dreiecksungleichung für endlich viele Summanden
Welche Abschätzung liefert die Dreiecksungleichung für eine Summe aus endlich vielen Summanden $a_m,\dots,a_N$?
---
$\bigl|\sum_{n=m}^Na_n\bigr|\le\sum_{n=m}^N|a_n|$: Der Betrag der Summe ist höchstens so groß wie die Summe der Beträge.
--- falsch
$\bigl|\sum_{n=m}^Na_n\bigr|\ge\sum_{n=m}^N|a_n|$: Der Betrag der Summe ist mindestens so groß wie die Summe der Beträge.
--- falsch
$\bigl|\sum_{n=m}^Na_n\bigr|=\sum_{n=m}^N|a_n|$: Betrag und Summe dürfen bei endlich vielen Summanden immer vertauscht werden.
--- falsch
$\bigl|\sum_{n=m}^Na_n\bigr|\le\max_n|a_n|$: Der Betrag der Summe ist höchstens so groß wie der größte einzelne Betrag.
:::
:::karte zusammenhang Teilfolge
Warum hat jede Teilfolge einer konvergenten Folge denselben Grenzwert, und warum sagt umgekehrt eine einzelne Teilfolge nichts über die ganze Folge?
---
Weil $n_k\ge k$ gilt: Für $k>N_0$ ist $n_k>N_0$, das Glied $a_{n_k}$ liegt also im Schlauch um $a$. Umgekehrt hat $0;\,1;\,0;\,1;\,\dots$ die konstanten Teilfolgen 0 und 1, ohne zu konvergieren.
--- falsch
Weil eine Teilfolge weniger Glieder hat und deshalb früher im Schlauch liegt. Umgekehrt gilt dasselbe: Konvergiert eine Teilfolge, so konvergiert die ganze Folge gegen denselben Wert.
--- falsch
Weil $n_k\le k$ gilt: Die Teilfolge ist der Folge immer voraus und erreicht den Schlauch zuerst. Umgekehrt legt eine konvergente Teilfolge den Grenzwert der ganzen Folge fest.
--- falsch
Weil eine Teilfolge die Reihenfolge der Glieder beliebig ändern darf, ohne den Grenzwert zu ändern. Umgekehrt hat $0;\,1;\,0;\,1;\,\dots$ überhaupt keine konvergente Teilfolge.
:::
:::karte formel Logarithmus und Potenzen
Wie ist die Potenz $x^s$ für $s\in\mathbb{R}$ und $x>0$ über den Logarithmus festgelegt, und welche Rechenregeln werden für Zweierpotenzen gebraucht?
---
$x^s:=\mathrm{e}^{s\log x}$ mit dem natürlichen Logarithmus. Für $s>0$ wächst $x^s$ streng monoton in $x$; es gilt $(2^k)^s=(2^s)^k$ und $\log(2^k)=k\log2$.
--- falsch
$x^s:=\mathrm{e}^{s\log x}$ mit dem Logarithmus zur Basis 10. Für $s>0$ wächst $x^s$ streng monoton in $x$; es gilt $(2^k)^s=(2^s)^k$ und $\log(2^k)=k\log2$.
--- falsch
$x^s:=\mathrm{e}^{s\log x}$ mit dem natürlichen Logarithmus. Für jedes $s\in\mathbb{R}$ wächst $x^s$ streng monoton in $x$; es gilt $(2^k)^s=2^{k+s}$ und $\log(2^k)=k\log2$.
--- falsch
$x^s:=s\cdot\log x$ mit dem natürlichen Logarithmus. Für $s>0$ wächst $x^s$ streng monoton in $x$; es gilt $(2^k)^s=(2^s)^k$ und $\log(2^k)=(\log2)^k$.
:::
::::
