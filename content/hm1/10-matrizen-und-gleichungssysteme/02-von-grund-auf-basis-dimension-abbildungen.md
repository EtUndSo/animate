---
title: Von Grund auf: Basis, Dimension, Abbildungen
pfad: Elektrotechnik / 1. Semester / HöMa1 – Höhere Mathematik 1 / Matrizen und lineare Gleichungssysteme
adresse: elektrotechnik/1-semester/hohere-mathematik-1/matrizen-und-lineare-gleichungssysteme
knoten: Kapitel 10: Matrizen und lineare Gleichungssysteme
order: 1300200
summary: Eine Matrix ist eine lineare Abbildung in Zahlen, ein Gleichungssystem fragt rückwärts nach ihr
tags: Unterraum, Aufspann, Basis, Dimension, Basisergänzung, Standardbasis, injektiv, surjektiv
lang: de
---

⁠**Schreibweise.** $\mathbb K$ ist $\mathbb{R}$ oder $\mathbb{C}$. Vektoren stehen ab hier ohne Pfeil. Elemente von $\mathbb K^n$ sind Spalten; im Fließtext steht $(2,1)$ für die Spalte $\bigl(\begin{smallmatrix}2\\1\end{smallmatrix}\bigr)$. Der Nullvektor von $V$ heißt $0_V$, kurz 0.

⁠**Unterraum ([Kapitel 8](/wissen/elektrotechnik/1-semester/hohere-mathematik-1/vektoren-und-skalarprodukt/vektoren-und-skalarprodukt.html)).** $U\subset V$ ist ein __Unterraum__, wenn (U1) $0\in U$, (U2) $a,b\in U\Rightarrow a+b\in U$ und (U3) $a\in U\Rightarrow\alpha a\in U$ für alle $\alpha\in\mathbb K$ gilt. Der __Aufspann__ $\operatorname{span}\{v_1,\dots,v_k\}$ ist die Menge aller Linearkombinationen $\sum_j\alpha_jv_j$.

⁠**Basis und Dimension ([Kapitel 9](/wissen/elektrotechnik/1-semester/hohere-mathematik-1/vektorprodukt-und-basen/vektorprodukt-und-basen.html)).** Linear unabhängige Vektoren, die $V$ aufspannen, bilden eine __Basis__ $\mathcal B=(v_1,\dots,v_n)$. Gleichbedeutend: Jedes $v\in V$ hat genau eine Darstellung $v=\sum_{j}\alpha_jv_j$. Alle Basen sind gleich lang, ihre Länge ist die __Dimension__ $\dim V$; es ist $\dim\{0\}=0$. Mehr als $\dim V$ Vektoren sind stets abhängig. Linear unabhängige Vektoren lassen sich zu einer Basis ergänzen (__Basisergänzung__). Die __Standardbasis__ von $\mathbb K^n$ besteht aus den Einheitsvektoren $e_j$ mit einer 1 an Stelle $j$ und sonst Nullen; also ist $\dim\mathbb K^n=n$. Sind $v_1,\dots,v_k$ linear unabhängig, so ist $\dim\operatorname{span}\{v_1,\dots,v_k\}=k$.

⁠**Abbildungen ([Kapitel 3](/wissen/elektrotechnik/1-semester/hohere-mathematik-1/funktionen-und-polynome/funktionen-und-polynome.html)).** $f:A\to B$ heißt __injektiv__, wenn aus $f(x)=f(y)$ folgt $x=y$, __surjektiv__, wenn jedes $y\in B$ getroffen wird, __bijektiv__, wenn beides gilt. Dann gibt es die Umkehrabbildung $f^{-1}:B\to A$ mit $f^{-1}(f(x))=x$ und $f(f^{-1}(y))=y$. Die Hintereinanderausführung ist $(g\circ f)(x)=g(f(x))$, gesprochen „$g$ nach $f$“.
