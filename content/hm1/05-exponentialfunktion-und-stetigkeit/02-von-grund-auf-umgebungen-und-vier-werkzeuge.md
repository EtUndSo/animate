---
title: Von Grund auf: Umgebungen und vier Werkzeuge
pfad: Elektrotechnik / 1. Semester / HöMa1 – Höhere Mathematik 1 / Exponentialfunktion und Stetigkeit
adresse: elektrotechnik/1-semester/hohere-mathematik-1/exponentialfunktion-und-stetigkeit
knoten: Kapitel 5: Exponentialfunktion und Stetigkeit
order: 1250200
summary: Was alles daraus folgt, dass kleine Änderungen am Eingang kleine Änderungen am Ausgang machen
tags: Umgebung, punktierte Umgebung
lang: de
---

⁠**Umgebung.** Für $\eta>0$ (griechisch eta) heißt $U_\eta(x_0):=(x_0-\eta,x_0+\eta)$ __Umgebung__ von $x_0$ und $\dot U_\eta(x_0):=U_\eta(x_0)\setminus\{x_0\}$ __punktierte Umgebung__: Sie lässt die Stelle selbst aus. $x\in U_\eta(x_0)$ bedeutet $|x-x_0|<\eta$.

⁠**Werkzeuge.** *Monotonie-Lemma* ([Kapitel 4](/wissen/elektrotechnik/1-semester/hohere-mathematik-1/folgen-und-grenzwerte/folgen-und-grenzwerte.html)): Monotone beschränkte Folgen konvergieren. *Sandwich-Lemma* ([Kapitel 4](/wissen/elektrotechnik/1-semester/hohere-mathematik-1/folgen-und-grenzwerte/folgen-und-grenzwerte.html)): Aus $c_n\le a_n\le b_n$ und $\lim c_n=\lim b_n=a$ folgt $\lim a_n=a$. *Bernoulli* ([Kapitel 1](/wissen/elektrotechnik/1-semester/hohere-mathematik-1/mengen-logik-und-reelle-zahlen/mengen-logik-und-reelle-zahlen.html)): $(1+h)^m>1+mh$ für $h>-1$, $h\ne0$, $m\ge2$. *Intervallschachtelung* ([Kapitel 1](/wissen/elektrotechnik/1-semester/hohere-mathematik-1/mengen-logik-und-reelle-zahlen/mengen-logik-und-reelle-zahlen.html)): Geschachtelte Intervalle $[a_n,b_n]$ mit $b_n-a_n\to0$ enthalten genau eine gemeinsame Zahl.

Aus [Kapitel 3](/wissen/elektrotechnik/1-semester/hohere-mathematik-1/funktionen-und-polynome/funktionen-und-polynome.html) stammen $\mathcal W(f)$ (Wertebereich) und die Aussage: Streng monotone $f$ sind auf $\mathcal W(f)$ bijektiv, $f^{-1}$ ist monoton in dieselbe Richtung. Außerdem ist $\mathbb{R}^+:=(0,\infty)$.
