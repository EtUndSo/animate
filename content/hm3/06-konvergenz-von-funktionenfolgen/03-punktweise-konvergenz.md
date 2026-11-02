---
title: Stufe 1: Punktweise Konvergenz
pfad: Elektrotechnik / 3. Semester / Höhere Mathematik 3 / Konvergenz von Funktionenfolgen
order: 3160300
summary: An jeder festen Stelle ist eine Folge von Funktionen eine Zahlenfolge.
tags: Funktionenfolge, Punktweise Konvergenz, Grenzfunktion
lang: de
---

<span class="anker" id="stufe-1"></span>

:::zweck
An jeder festen Stelle ist eine Folge von Funktionen eine Zahlenfolge. Diese Stufe bildet so den Grenzwert und zeigt, dass dabei Stetigkeit und Integral verloren gehen können.
:::

**Die Idee.** Gegeben ist eine __Funktionenfolge__ $(f_n)_{n\in\mathbb{N}}$, also Funktionen $f_n:[a,b]\to\mathbb{R}$ oder $f_n:[a,b]\to\mathbb{C}$. Halte eine Stelle $x$ fest. Dann sind $f_1(x),f_2(x),f_3(x),\dots$ gewöhnliche Zahlen. Im Bild liest man sie ab, indem man die Kurven mit der Senkrechten bei $x$ schneidet (Abb. [1](#abb-1)). Hat diese Zahlenfolge an jeder Stelle einen Grenzwert, entsteht daraus eine neue Funktion.

:::abbildung hm3/k6punkt 1
Links die Entladekurven $u_n$ für $n=1,4,16$. Ihre Grenzfunktion (rot) ist auf $(0,1]$ null und hat bei $x=0$ den Wert 1. Rechts die Beulen $b_n$ für $n=2,4,8$. Sie streben an jeder Stelle gegen null, ihre Fläche aber gegen 1.
:::

:::definition Definition 1.1 (Punktweise Konvergenz)
<span class="anker" id="satz-1-1"></span>

Seien $(f_n)_{n\in\mathbb{N}}$ und $f$ beschränkte Funktionen auf $[a,b]$. __Punktweise Konvergenz__ der Folge gegen die __Grenzfunktion__ $f$ heißt

<span class="anker" id="gl-1-1"></span>
$$\lim_{n\to\infty}f_n(x)=f(x)\quad\text{für jedes }x\in[a,b], \tag{1.1}$$

gleichbedeutend $\lim_{n\to\infty}|f_n(x)-f(x)|=0$ für jedes $x\in[a,b]$.
:::

⁠**So liest man das:** Für jedes $x$ wird eine eigene Zahlenfolge geprüft. Bei $f_n(x)=x/n$ auf $[0,1]$ ist das an der Stelle $x=\frac12$ die Folge $\frac12,\frac14,\frac16,\dots$ mit Grenzwert 0, und die Grenzfunktion ist $f=0$. Ausgeschrieben heißt [(1.1)](#gl-1-1): Zu jedem $\varepsilon>0$ und jedem $x$ gibt es ein $N$ mit $|f_n(x)-f(x)|<\varepsilon$ für alle $n\ge N$. Dieses $N$ darf von $x$ abhängen.

**Beispiel: die Entladekurven.** Bei $x=0$ ist $u_n(0)=1$ für alle $n$. Für $x>0$ gilt $\mathrm{e}^{-nx}\to0$. Die Grenzfunktion ist also

<span class="anker" id="gl-1-2"></span>
$$f(x)=\begin{cases}1&x=0,\\0&0<x\le1.\end{cases} \tag{1.2}$$

Wie groß $n$ für $u_n(x)<0{,}01$ sein muss, hängt von der Stelle ab: Die Bedingung heißt $n>\ln(100)/x\approx4{,}6/x$. Das gibt $n\ge10$ bei $x=0{,}5$, $n\ge47$ bei $x=0{,}1$ und $n\ge461$ bei $x=0{,}01$. Ein $n$, das für alle $x>0$ zugleich passt, gibt es nicht.

**Verlust 1: die Stetigkeit.** Jedes $u_n$ ist stetig, die Grenzfunktion [(1.2)](#gl-1-2) springt bei $x=0$. Das ist eine Frage der Reihenfolge zweier Grenzwerte:

$$\lim_{x\to0^+}\Bigl(\lim_{n\to\infty}u_n(x)\Bigr)=0,\qquad\lim_{n\to\infty}\Bigl(\lim_{x\to0^+}u_n(x)\Bigr)=1.$$

**Verlust 2: das Integral.** Die Beulen streben an jeder Stelle gegen null: Es ist $b_n(0)=0$, und für $x>0$ gewinnt die Exponentialfunktion gegen $n^2$. Das Integral der Grenzfunktion ist 0. Mit $t=nx$ und partieller Integration folgt aber

<span class="anker" id="gl-1-3"></span>
$$\int_0^1b_n(x)\,\mathrm{d} x=\int_0^nt\,\mathrm{e}^{-t}\,\mathrm{d} t=1-(1+n)\,\mathrm{e}^{-n}\;\longrightarrow\;1. \tag{1.3}$$

Für $n=2,4,8$ ist das $0{,}594$; $0{,}908$; $0{,}997$. Der Mechanismus: Die Beule wird wie $n$ höher und wie $1/n$ schmaler, ihre Fläche bleibt also ungefähr gleich. Keine feste Stelle sieht sie lange, denn sie wandert zum Rand. Das Integral sieht sie immer. **Grenzfall:** Für $n=1$ gibt [(1.3)](#gl-1-3) den Wert $1-2/\mathrm{e}\approx0{,}264$, wie die direkte Rechnung $\int_0^1x\,\mathrm{e}^{-x}\,\mathrm{d} x$.

:::frage Die Entladekurven nähern sich doch sichtbar der Null. Was ist das Problem?
Die Kurve $u_{16}$ liegt fast überall nahe null, aber nicht nahe $x=0$. An der Stelle $x=1/n$ ist $u_n(1/n)=\mathrm{e}^{-1}\approx0{,}368$, für jedes $n$. Die schlechte Stelle wandert zum Rand, sie verschwindet aber nie.
:::

:::aufgabe Aufgabe 1 ★ Grenzfunktionen bestimmen
<span class="anker" id="aufg-1"></span>

Bestimme jeweils die Grenzfunktion. Ist sie stetig?

<ol class="al">

<li>

$f_n(x)=1/(1+x^{2n})$ auf $[0,2]$.

</li>

<li>

$f_n(x)=x^{1/n}$ auf $[0,1]$. Wie groß muss $n$ für $f_n(x)>0{,}9$ bei $x=0{,}5$ und bei $x=0{,}01$ sein?

</li>

<li>

$f_n(x)=\mathrm{e}^{-x/n}$ auf $[0,1]$.

</li>

</ol>

:::loesung
(a) Für $0\le x<1$ gilt $x^{2n}\to0$, also $f(x)=1$. Bei $x=1$ ist $f_n(1)=\frac12$. Für $1<x\le2$ gilt $x^{2n}\to\infty$, also $f(x)=0$. Die Grenzfunktion springt bei $x=1$. (b) Für $x>0$ ist $x^{1/n}=\mathrm{e}^{(\ln x)/n}\to1$, bei $x=0$ ist der Wert 0. Die Grenzfunktion springt bei $x=0$. Die Bedingung $x^{1/n}>0{,}9$ heißt $n>\ln x/\ln0{,}9$, also $n\ge7$ bei $x=0{,}5$ und $n\ge44$ bei $x=0{,}01$. (c) $\mathrm{e}^{-x/n}\to1$ für alle $x$. Die Grenzfunktion $f=1$ ist stetig.
:::
:::

Punktweise Konvergenz ist also zu schwach. Die nächste Stufe verlangt, dass alle Stellen zugleich nahe am Grenzwert sind.
