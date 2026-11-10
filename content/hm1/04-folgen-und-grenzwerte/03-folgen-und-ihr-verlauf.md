---
title: Stufe 1: Folgen und ihr Verlauf
pfad: Elektrotechnik / 1. Semester / HöMa1 – Höhere Mathematik 1 / Folgen und Grenzwerte
adresse: elektrotechnik/1-semester/hohere-mathematik-1/folgen-und-grenzwerte
knoten: Kapitel 4: Folgen und Grenzwerte
order: 1240300
summary: Ein Grenzwert braucht etwas, das sich einem Wert nähert.
tags: Zahlenfolge, Folgenglieder, Index, Wertemenge, monoton wachsend, streng monoton wachsend, monoton fallend, streng monoton fallend
lang: de
---

<span class="anker" id="stufe-1"></span>

:::zweck
Ein Grenzwert braucht etwas, das sich einem Wert nähert. Diese Stufe legt fest, was eine Folge ist, und beschreibt ihren Verlauf mit den Begriffen aus [Kapitel 3](/wissen/elektrotechnik/1-semester/hohere-mathematik-1/funktionen-und-polynome/funktionen-und-polynome.html).
:::

**Die Idee.** Eine Folge ist eine nummerierte Liste ohne Ende: Jeder Platz $n$ bekommt genau eine Zahl. Eine Zuordnung, die jedem Eingang genau einen Wert gibt, ist eine Funktion ([Kapitel 3](/wissen/elektrotechnik/1-semester/hohere-mathematik-1/funktionen-und-polynome/funktionen-und-polynome.html)), hier mit natürlichen Zahlen als Eingang. Deshalb besteht ihr Graph aus einzelnen Punkten, zwischen den Plätzen gibt es nichts (Abb. [1](#abb-1)).

:::definition Definition 1.1 (Folge)
<span class="anker" id="satz-1-1"></span>

Eine __Zahlenfolge__ ist eine auf $\mathbb{N}$ (oder auf $\mathbb{N}_0$ oder einer unendlichen Teilmenge von $\mathbb{N}_0$) definierte reellwertige Funktion

$$f:\ \mathbb{N}\to\mathbb{R},\qquad n\mapsto f(n)=:f_n.$$

Man schreibt $\{f_n\}_{n\in\mathbb{N}}$, $\{f_n\}_{n=1}^\infty$ oder kurz $\{f_n\}$. Die Zahlen $f_n$ heißen __Folgenglieder__.
:::

⁠**So liest man das:** $n$ ist der __Index__, die Platznummer. $f_n$ ist die Zahl auf diesem Platz. Die Menge aller vorkommenden Zahlen heißt __Wertemenge__ $\mathcal W(f_n):=\{f_n:n\in\mathbb{N}\}$.

:::frage Ist $\{f_n\}$ nicht dasselbe wie die Wertemenge?
Nein. Die Klammer meint hier die Liste mit ihrer Reihenfolge. Die Folge $(-1)^n$ hat unendlich viele Glieder, ihre Wertemenge nur die zwei Elemente $-1$ und $1$.
:::

:::definition Definition 1.2 (Monotone und beschränkte Folgen)
<span class="anker" id="satz-1-2"></span>

Eine Folge heißt monoton wachsend, nach unten beschränkt und so weiter, wenn die zugehörige Funktion $f$ diese Eigenschaft hat. Für Folgen bedeutet das:

<ul>

<li>

__monoton wachsend__: $a_n\le a_{n+1}$ für alle $n$; __streng monoton wachsend__: $a_n<a_{n+1}$; __monoton fallend__: $a_n\ge a_{n+1}$; __streng monoton fallend__: $a_n>a_{n+1}$;

</li>

<li>

__nach oben beschränkt__: $a_n\le S$ für alle $n$ mit einem festen $S\in\mathbb{R}$; __nach unten beschränkt__: $R\le a_n$ für alle $n$ mit einem festen $R\in\mathbb{R}$; __beschränkt__: beides zugleich, also $|a_n|\le M$ für alle $n$ mit einem festen $M$.

</li>

</ul>
:::

⁠**So liest man das:** Für Funktionen verlangt Monotonie den Vergleich beliebiger Stellen $x<y$. Auf $\mathbb{N}$ genügt der Vergleich von Nachbarn, weil man von $n$ in Einerschritten zu jedem größeren $m$ kommt. Beschränkt heißt: Der Graph liegt in einem waagerechten Streifen. Die Pendelfolge ist beschränkt ($-1\le a_n\le3{,}5$), aber nicht monoton. Die Summenfolge ist streng monoton wachsend und durch 2 beschränkt. Die Folge $n^2$ ist streng monoton wachsend und unbeschränkt.

:::abbildung hm1/k4folgen 1
Oben die ersten Glieder der Pendelfolge und der Summenfolge als Punkte über dem Index, gestrichelt der Wert 2. Unten dieselben Glieder auf der Zahlengeraden: Der Index ist nicht mehr zu sehen, aber die Häufung bei 2.
:::

**Die geometrische Summe.** Viele Folgen entstehen durch Aufsummieren, darunter die Summenfolge.

:::satz Satz 1.3 (Geometrische Summe)
<span class="anker" id="satz-1-3"></span>

Für $q\in\mathbb{R}$ heißt die Folge $s_n:=\sum_{k=0}^nq^k=1+q+q^2+\dots+q^n$, $n\in\mathbb{N}_0$, __geometrische Summe__. Es gilt

<span class="anker" id="gl-1-1"></span>
$$s_n=\begin{cases}\dfrac{1-q^{n+1}}{1-q},&q\ne1,\\[2mm]n+1,&q=1.\end{cases} \tag{1.1}$$
:::

⁠**So liest man das:** $q$ ist das Verhältnis benachbarter Summanden, der Summand mit $k=0$ ist immer 1. Es gibt $n+1$ Summanden. Die Formel ersetzt $n+1$ Additionen durch eine Division.

:::beweis Teleskopsumme
Für $q=1$ stehen $n+1$ Einsen da. Für $q\ne1$ multipliziert man mit $1-q$:

$$(1-q)\,s_n=\sum_{k=0}^n\bigl(q^k-q^{k+1}\bigr)=(1-q)+(q-q^2)+\dots+(q^n-q^{n+1})=1-q^{n+1}.$$

Jede Potenz $q,\dots,q^n$ kommt einmal mit Plus und einmal mit Minus vor, nur der Anfang 1 und das Ende $q^{n+1}$ bleiben (eine __Teleskopsumme__). Teilen durch $1-q\ne0$ ergibt [(1.1)](#gl-1-1).
:::

⁠**Verlauf.** Für $q>0$ ist $s_{n+1}=s_n+q^{n+1}>s_n$: Die Folge wächst streng monoton. Für $q\ge1$ ist jeder Summand mindestens 1, also $s_n\ge n+1$, und die Folge ist unbeschränkt. Für $0<q<1$ ist $q^{n+1}>0$, also $0<s_n<\frac1{1-q}$, und die Folge ist beschränkt.

::::beispiel
Für $q=\frac12$ ergibt [(1.1)](#gl-1-1) die Summenfolge in geschlossener Form: $s_n=2\bigl(1-(\frac12)^{n+1}\bigr)=2-(\frac12)^n$, zum Beispiel $s_{10}=2047/1024=1{,}99902$. Der Rest $2-s_n=(\frac12)^n$ halbiert sich in jedem Schritt.
::::

⁠**Grenzfälle:** Für $q=0$ ist $s_n=1$. Für $q$ nahe 1 geht die Formel in $n+1$ über: $q=1{,}001$ und $n=9$ ergeben $10{,}05$ statt 10.

:::aufgabe Aufgabe 1 ★ Geometrische Summen
<span class="anker" id="aufg-1"></span>

<ol class="al">

<li>

Berechne $s_5$ für $q=\frac34$ als Bruch und vergleiche mit der Schranke $\frac1{1-q}$.

</li>

<li>

Schreibe für $q=-\frac12$ die Glieder $s_0$ bis $s_5$ auf. Ist die Folge monoton? Ist sie beschränkt?

</li>

<li>

Sage vorher, was für $q=-1$ passiert, und prüfe es mit [(1.1)](#gl-1-1).

</li>

</ol>

:::loesung
(a) $s_5=\dfrac{1-(3/4)^6}{1/4}=4\bigl(1-\frac{729}{4096}\bigr)=\frac{3367}{1024}=3{,}288$, unter der Schranke $\frac1{1-q}=4$. (b) $s_0,\dots,s_5=1;\ \frac12;\ \frac34;\ \frac58;\ \frac{11}{16};\ \frac{21}{32}$. Die Folge springt auf und ab, sie ist nicht monoton. Beschränkt ist sie: Aus [(1.1)](#gl-1-1) folgt $s_n=\frac23\bigl(1-(-\frac12)^{n+1}\bigr)$, also $\frac12\le s_n\le1$. (c) Die Summanden $+1$ und $-1$ heben sich paarweise auf: $s_n=1$ für gerade $n$, $s_n=0$ für ungerade $n$. Die Formel gibt $s_n=\frac12\bigl(1-(-1)^{n+1}\bigr)$, dasselbe.
:::
:::
