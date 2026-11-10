---
title: Stufe 7: Intervallschachtelung und Wurzeln
pfad: Elektrotechnik / 1. Semester / HöMa1 – Höhere Mathematik 1 / Mengen, Logik und reelle Zahlen
adresse: elektrotechnik/1-semester/hohere-mathematik-1/mengen-logik-und-reelle-zahlen
knoten: Kapitel 1: Mengen, Logik und reelle Zahlen
order: 1210900
summary: Das Axiom garantiert Grenzen.
tags: Intervall, nicht negativen Zahlen, Wurzel
lang: de
---

<span class="anker" id="stufe-7"></span>

:::zweck
Das Axiom garantiert Grenzen. Diese Stufe macht daraus ein Bauverfahren und beweist damit, dass $x^2=2$ in $\mathbb{R}$ genau eine positive Lösung hat.
:::

**Die Idee.** Man fängt die gesuchte Zahl zwischen zwei Brüchen ein und halbiert das Intervall immer wieder, bis es beliebig klein ist (Abb. [7](#abb-7)). Jedes Intervall liegt im vorigen. Die Vollständigkeit garantiert, dass es einen Punkt gibt, der in allen liegt. In $\mathbb{Q}$ kann dieser Punkt fehlen. Ein __Intervall__ ist $[a,b]:=\{x\in\mathbb{R}:a\le x\le b\}$, die __nicht negativen Zahlen__ sind $\mathbb{R}_0^+:=\{x\in\mathbb{R}:x\ge0\}$.

:::satz Satz 7.1 (Intervallschachtelung)
<span class="anker" id="satz-7-1"></span>

Für Zahlen $a_n,b_n\in\mathbb{R}$, $n\in\mathbb{N}$, gelte $a_1\le a_2\le a_3\le\dots\le b_3\le b_2\le b_1$ und

<span class="anker" id="gl-7-1"></span>
$$\forall\varepsilon>0\ \exists n\in\mathbb{N}:\ 0\le b_n-a_n<\varepsilon. \tag{7.1}$$

Dann gibt es genau ein $x\in\mathbb{R}$ mit $a_n\le x\le b_n$ für alle $n\in\mathbb{N}$.
:::

⁠**So liest man das:** $\varepsilon$ (griechisch Epsilon) ist eine beliebig kleine positive Zahl. [(7.1)](#gl-7-1) heißt: Die Intervalle $[a_n,b_n]$ werden kleiner als jede vorgegebene Länge. **Warum die Voraussetzungen:** Ohne [(7.1)](#gl-7-1) ist $x$ nicht eindeutig: Für $a_n=-\frac1n$, $b_n=1+\frac1n$ liegt ganz $[0,1]$ in allen Intervallen. In $\mathbb{Q}$ gilt der Satz nicht: Die Brüche $a_n,b_n$ aus Abb. [7](#abb-7) erfüllen alle Bedingungen, aber kein Bruch liegt in allen Intervallen.

:::beweis Intervallschachtelung
⁠*Existenz.* Für beliebige $n,k$ sei $m$ die größere der beiden Zahlen. Dann $a_n\le a_m\le b_m\le b_k$. Also ist jedes $b_k$ obere Schranke von $A:=\{a_n:n\in\mathbb{N}\}$. Nach Satz [6.5](das-vollstandigkeitsaxiom.html#satz-6-5) (i) existiert $x:=\sup A$. Es ist $a_n\le x$, weil $x$ obere Schranke ist, und $x\le b_k$, weil $x$ die kleinste ist.

⁠*Eindeutigkeit.* Lägen $x<\tilde x$ in allen Intervallen, wäre $b_n-a_n\ge\tilde x-x=:\varepsilon>0$ für alle $n$, gegen [(7.1)](#gl-7-1).
:::

:::abbildung hm1/k1schachtelung 7
Halbieren für $x^2=2$: Ist das Quadrat der Mitte kleiner als 2, wird sie die neue linke Grenze, sonst die neue rechte. Die Länge ist $b_n-a_n=2^{1-n}$.
:::

:::satz Satz 7.2 (Wurzel)
<span class="anker" id="satz-7-2"></span>

Zu jedem $y\in\mathbb{R}_0^+$ gibt es genau ein $x\in\mathbb{R}_0^+$ mit $x^2=y$. Man schreibt $x=\sqrt y$ („__Wurzel__ aus $y$“). Für $x,y\ge0$ gilt $\sqrt{xy}=\sqrt x\sqrt y$.
:::

⁠**So liest man das:** Die Wurzel ist die nicht negative Lösung, $\sqrt{4}=2$ und nicht $-2$. Die Gleichung $z^2=2$ hat zwei Lösungen: $\sqrt2$ und $-\sqrt2$, denn $(-1)(-1)=1$. Die Produktregel braucht $x,y\ge0$: $\sqrt{(-1)(-1)}=1$, aber $\sqrt{-1}$ gibt es in $\mathbb{R}$ nicht. **Grenzfall** $y=0$: Die einzige Lösung ist $x=0$.

:::beweis Existenz für $y=2$, Eindeutigkeit, Produktregel
Man startet mit $a_1=1$, $b_1=2$ und halbiert wie in Abb. [7](#abb-7). Alle $a_n$, $b_n$ sind Brüche, also ist nach Satz [6.1](das-vollstandigkeitsaxiom.html#satz-6-1) nie $a_n^2=2$ oder $b_n^2=2$. Das gibt $a_n^2<2<b_n^2$ und $b_n-a_n=2^{1-n}\le\frac1n$ wegen $2^{n-1}\ge n$ (Aufgabe [10](elementare-ungleichungen.html#aufg-10)). Nach Satz [6.5](das-vollstandigkeitsaxiom.html#satz-6-5) (vi) gilt [(7.1)](#gl-7-1), also gibt es $x$ mit $a_n\le x\le b_n$ für alle $n$.

Warum $x^2=2$: Aus $a_n\le x\le b_n$ folgt nach Satz [4.2](anordnungsaxiome.html#satz-4-2) (e) $a_n^2\le x^2\le b_n^2$. Auch 2 liegt in $[a_n^2,b_n^2]$. Dieses Intervall hat die Länge $(b_n-a_n)(b_n+a_n)\le4\cdot\frac1n$. Der Abstand von $x^2$ und 2 ist also kleiner als jede positive Zahl und damit null. Für andere $y>0$ startet man mit $[0,y+1]$; trifft eine Mitte $m$ genau $m^2=y$, ist $x=m$. Für $y=0$ ist $x=0$. *Eindeutigkeit:* Aus $u>v\ge0$ folgt $u^2>v^2$, zwei verschiedene nicht negative Zahlen haben verschiedene Quadrate.

⁠*Produktregel:* $\sqrt x\sqrt y\ge0$ und $(\sqrt x\sqrt y)^2=xy$ (M1, M2), und die nicht negative Lösung ist eindeutig.
:::

::::beispiel
Nach sechs Schritten ist $1{,}40625\le\sqrt2\le1{,}4375$, Breite $2^{-5}=0{,}03125$. Dezimalzahlen sind dieselbe Idee mit zehn statt zwei Teilen: Jede Ziffer schränkt das Intervall auf ein Zehntel ein. Deshalb hat jede reelle Zahl eine Darstellung [(0.1)](von-grund-auf-zahlbereiche-und-dezimalzahlen.html#gl-0-1).
::::

:::frage Es reicht doch, $\sqrt2$ vom Taschenrechner abzulesen. Wozu der Aufwand?
Für jeden Zahlenwert reicht das. Der Rechner zeigt aber einen Bruch, $1{,}414213562$, dessen Quadrat nicht 2 ist. Die Frage hier lautet: Gibt es überhaupt eine Zahl mit Quadrat genau 2? In $\mathbb{Q}$ nein, in $\mathbb{R}$ ja, und dieser Unterschied trägt später Grenzwerte und Stetigkeit.
:::

:::aufgabe Aufgabe 8 ★★★ Die Wurzel aus 3
<span class="anker" id="aufg-8"></span>

<ol class="al">

<li>

Führe drei Halbierungsschritte für $x^2=3$ aus, Start $[1,2]$. Wie breit ist das Ergebnis?

</li>

<li>

Beweise $\sqrt3\notin\mathbb{Q}$. Hinweis: Eine Zahl, die nicht durch 3 teilbar ist, hat die Form $3k\pm1$.

</li>

<li>

An welcher Stelle scheitert derselbe Beweis für $\sqrt4$?

</li>

</ol>

:::loesung
(a) Mitte $1{,}5$: $2{,}25<3$, also $[1{,}5;\,2]$. Mitte $1{,}75$: $3{,}0625>3$, also $[1{,}5;\,1{,}75]$. Mitte $1{,}625$: $2{,}640625<3$, also $[1{,}625;\,1{,}75]$. Breite $\frac18=0{,}125$. (b) Annahme: $\sqrt3=\frac pq$, $p,q\in\mathbb{N}$, nicht beide durch 3 teilbar. Dann $p^2=3q^2$. Wäre $p=3k\pm1$, dann $p^2=3(3k^2\pm2k)+1$, nicht durch 3 teilbar. Also $p=3k$, damit $q^2=3k^2$, und ebenso ist $q$ durch 3 teilbar. Widerspruch. (c) Aus $p^2=4q^2$ folgt $p=2k$ und $k^2=q^2$. Das sagt nichts über die Teilbarkeit von $q$: $\sqrt4=\frac21$.
:::
:::
