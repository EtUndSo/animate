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
