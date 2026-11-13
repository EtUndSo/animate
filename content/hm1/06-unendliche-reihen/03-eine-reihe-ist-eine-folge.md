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

::::formelsammlung
**Teilsumme**

$$S_N:=\sum_{n=1}^Na_n=a_1+\dots+a_N\in\mathbb{R}$$

$N$-te Teilsumme oder Partialsumme zur reellen Folge $\{a_n\}_{n\in\mathbb{N}}$; die $a_n$ heißen Glieder. Die Folge $\{S_N\}_{N\in\mathbb{N}}$ heißt unendliche Reihe oder kurz Reihe.

**Konvergenz einer Reihe**

$$\lim_{N\to\infty}S_N=S$$

Dann konvergiert die Reihe mit Grenzwert $S$; existiert der Grenzwert in $\mathbb{R}$ nicht, heißt sie divergent. $\sum_{n=1}^\infty a_n$ steht für die Folge $\{S_N\}$ und, falls sie konvergiert, für $S$.

**Glieder aus Teilsummen**

$$a_n=S_n-S_{n-1}$$

Für $n\ge2$.

**Anderer Startindex**

$$\sum_{n=p}^\infty a_n\ \text{meint}\ \bigl\{\sum_{n=p}^Na_n\bigr\}_{N=p}^\infty$$

Für $p\in\mathbb{Z}$. Ein anderer Start verschiebt alle Teilsummen um dieselbe Zahl: Der Wert ändert sich, die Konvergenz nie.

**Geometrische Reihe**

$$\sum_{n=0}^\infty q^n=\lim_{N\to\infty}\sum_{n=0}^Nq^n=\frac1{1-q}$$

Für $q\in\mathbb{R}$ mit $|q|<1$; $q$ ist das Verhältnis benachbarter Glieder. Für $|q|\ge1$ divergiert die Reihe.

**Teleskopsumme**

$$\sum_{n=1}^N\frac1{n(n+1)}=1-\frac1{N+1}$$

Wegen $\frac1{n(n+1)}=\frac1n-\frac1{n+1}$ heben sich alle inneren Glieder auf; der Wert der Reihe ist 1.
::::

::::lernkarten
:::karte begriff unendliche Reihe und Reihe
Was genau ist die unendliche Reihe zu einer reellen Folge $\{a_n\}_{n\in\mathbb{N}}$, wenn man unendlich viele Zahlen gar nicht der Reihe nach addieren kann?
---
Die Folge $\{S_N\}_{N\in\mathbb{N}}$ der Teilsummen $S_N:=\sum_{n=1}^Na_n$, kurz Reihe genannt. Das Symbol $\sum_{n=1}^\infty a_n$ steht für diese Folge und, falls sie konvergiert, für ihren Grenzwert.
--- falsch
Die Zahl $a_1+a_2+a_3+\dots$, die man erhält, wenn man alle Glieder auf einmal addiert. Das Symbol $\sum_{n=1}^\infty a_n$ steht für diese Zahl, die es zu jeder reellen Folge gibt.
--- falsch
Die Folge $\{a_n\}_{n\in\mathbb{N}}$ selbst, nur mit Pluszeichen zwischen den Gliedern geschrieben. Das Symbol $\sum_{n=1}^\infty a_n$ steht für diese Folge und, falls sie konvergiert, für ihren Grenzwert.
--- falsch
Die Folge der Mittelwerte $\frac1N(a_1+\dots+a_N)$, kurz Reihe genannt. Das Symbol $\sum_{n=1}^\infty a_n$ steht für diese Folge und, falls sie konvergiert, für ihren Grenzwert.
:::
:::karte begriff Teilsumme und Partialsumme
Was bezeichnet bei einer Reihe die $N$-te Teilsumme oder Partialsumme $S_N$, und wie gewinnt man aus den Teilsummen die einzelnen Glieder zurück?
---
Die Summe der ersten $N$ Glieder, $S_N=a_1+\dots+a_N$, im Bild die Höhe der Treppe nach $N$ Stufen. Zurück gilt $a_n=S_n-S_{n-1}$ für $n\ge2$.
--- falsch
Die Summe der Glieder ab Nummer $N$, also $a_N+a_{N+1}+\dots$, im Bild der noch fehlende Rest der Treppe. Zurück gilt $a_n=S_n-S_{n+1}$ für alle $n\ge1$.
--- falsch
Das $N$-te Glied $a_N$ selbst, im Bild die Höhe einer einzelnen Stufe. Zurück gilt $a_n=S_n$ für alle $n$: Teilsummen und Glieder bilden dieselbe Folge.
--- falsch
Die Summe der ersten $N$ Glieder, $S_N=a_1+\dots+a_N$. Zurück gilt $a_n=S_n+S_{n-1}$ für $n\ge2$, weil jede Teilsumme die vorige schon enthält.
:::
:::karte begriff Glieder
Was nennt man die Glieder einer Reihe $\sum_{n=1}^\infty a_n$, und welche Rollen spielen dabei die Indizes $n$ und $N$?
---
Die Zahlen $a_n$ der zugrunde liegenden Folge, also die einzelnen Summanden. Der Index $n$ zählt die Summanden, $N$ sagt, wo man mit dem Addieren aufhört.
--- falsch
Die Teilsummen $S_N$, also die Zwischenstände beim Addieren. Der Index $N$ zählt diese Zwischenstände, $n$ gibt an, wie weit man noch vom Grenzwert entfernt ist.
--- falsch
Die Zahlen $a_n$ der Folge, also die einzelnen Summanden. Der Index $N$ zählt die Summanden, $n$ sagt, wo man mit dem Addieren aufhört.
--- falsch
Die Abstände $S-S_N$ zwischen Grenzwert und Teilsumme, also die Reste der Reihe. Der Index $n$ zählt die Summanden, $N$ sagt, wo man aufhört.
:::
:::karte zusammenhang Konvergenz und konvergiert
Warum braucht man für die Konvergenz einer Reihe keinen neuen Grenzwertbegriff, und wann konvergiert eine Reihe mit Grenzwert $S$?
---
Weil die Teilsummen eine Folge bilden und Grenzwerte von Folgen seit [Kapitel 4](/wissen/elektrotechnik/1-semester/hohere-mathematik-1/folgen-und-grenzwerte/folgen-und-grenzwerte.html) erklärt sind. Die Reihe konvergiert mit Grenzwert $S$, wenn $\lim_{N\to\infty}S_N=S$ gilt.
--- falsch
Weil man nur die Glieder betrachten muss, deren Grenzwert seit [Kapitel 4](/wissen/elektrotechnik/1-semester/hohere-mathematik-1/folgen-und-grenzwerte/folgen-und-grenzwerte.html) erklärt ist. Die Reihe konvergiert mit Grenzwert $S$, wenn $\lim_{n\to\infty}a_n=S$ gilt.
--- falsch
Weil man eine Reihe wie eine endliche Summe ausrechnet und keinen Grenzwert braucht. Die Reihe konvergiert mit Grenzwert $S$, wenn eine Teilsumme $S_N$ den Wert $S$ genau erreicht.
--- falsch
Weil die Teilsummen eine Folge bilden. Die Reihe konvergiert mit Grenzwert $S$, sobald die Teilsummen $S_N$ beschränkt sind; $S$ ist dann ihre kleinste obere Schranke.
:::
:::karte zusammenhang divergent
Was bedeutet es für die Teilsummen, wenn eine Reihe divergent heißt, und muss die Reihe dann über alle Grenzen wachsen?
---
Divergent heißt nur, dass $\lim_{N\to\infty}S_N$ in $\mathbb{R}$ nicht existiert. Die Teilsummen können über alle Grenzen wachsen wie bei $1+1+1+\dots$ oder pendeln wie bei $1-1+1-\dots$
--- falsch
Divergent heißt, dass die Teilsummen über alle Grenzen wachsen. Eine Reihe wie $1-1+1-\dots$, deren Teilsummen nur pendeln, ist deshalb nicht divergent, sondern hat den Wert $\frac12$.
--- falsch
Divergent heißt, dass die Glieder keine Nullfolge bilden. Gehen die Glieder gegen 0, ist die Reihe nicht divergent, auch wenn ihre Teilsummen immer weiter wachsen.
--- falsch
Divergent heißt, dass man den Grenzwert der Teilsummen nicht als geschlossene Formel angeben kann. Die Teilsummen dürfen dabei durchaus gegen eine Zahl in $\mathbb{R}$ streben.
:::
:::karte begriff geometrische Reihe
Was ist die geometrische Reihe, für welche $q$ konvergiert sie, und welchen Wert hat sie dann?
---
Die Reihe $\sum_{n=0}^\infty q^n=1+q+q^2+\dots$, in der jedes Glied das $q$-Fache des vorigen ist. Für $q\in\mathbb{R}$ mit $|q|<1$ konvergiert sie gegen $\frac1{1-q}$, für $|q|\ge1$ divergiert sie.
--- falsch
Die Reihe $\sum_{n=0}^\infty q^n=1+q+q^2+\dots$, in der jedes Glied das $q$-Fache des vorigen ist. Für alle $q\ne1$ konvergiert sie gegen $\frac1{1-q}$; nur bei $q=1$ wird der Nenner null.
--- falsch
Die Reihe $\sum_{n=0}^\infty q^n=1+q+q^2+\dots$, in der jedes Glied das $q$-Fache des vorigen ist. Für $|q|<1$ konvergiert sie gegen $\frac q{1-q}$, weil ihr erstes Glied $q$ ist.
--- falsch
Die Reihe $\sum_{n=1}^\infty nq=q+2q+3q+\dots$, in der jedes Glied um $q$ größer ist als das vorige. Für $|q|<1$ konvergiert sie gegen $\frac1{1-q}$, sonst divergiert sie.
:::
:::karte herleitung Grenzübergang in der geometrischen Summe
Wie folgt aus der geometrischen Summe, dass $\sum_{n=0}^\infty q^n=\frac1{1-q}$ für $|q|<1$ gilt?
---
Die Teilsummen sind geometrische Summen, $S_N=\sum_{n=0}^Nq^n=\frac{1-q^{N+1}}{1-q}$, weil diese Formel aus [Kapitel 4](/wissen/elektrotechnik/1-semester/hohere-mathematik-1/folgen-und-grenzwerte/folgen-und-grenzwerte.html) für jedes $q\ne1$ gilt, also erst recht für $|q|<1$.
---
Für $|q|<1$ ist $q^{N+1}$ eine Nullfolge, weil $q^n\to0$ für $|q|<1$ gilt.
---
Die Rechenregeln für Grenzwerte ergeben $S_N\to\frac1{1-q}$, weil der Nenner $1-q$ nicht von $N$ abhängt und nicht null ist.
:::
:::karte zusammenhang anderer Start
Was geschieht mit Wert und Konvergenz einer Reihe, wenn ihr Index nicht bei 1, sondern bei einem anderen $p\in\mathbb{Z}$ beginnt?
---
Ein anderer Start verschiebt alle Teilsummen um dieselbe Zahl. Das ändert den Wert der Reihe, aber nie ihre Konvergenz; $\sum_{n=p}^\infty a_n$ meint die Folge $\bigl\{\sum_{n=p}^Na_n\bigr\}_{N=p}^\infty$.
--- falsch
Ein anderer Start ändert weder den Wert noch die Konvergenz, weil endlich viele Summanden neben unendlich vielen nicht ins Gewicht fallen; die Reihen sind gleich.
--- falsch
Ein anderer Start kann die Konvergenz ändern: Lässt man genügend viele Anfangsglieder weg, wird aus einer divergenten Reihe eine konvergente, weil nur kleine Glieder übrig bleiben.
--- falsch
Ein anderer Start verschiebt alle Glieder um denselben Betrag, aus $a_n$ wird $a_n+p$. Das ändert den Wert und im Allgemeinen auch die Konvergenz der Reihe.
:::
:::karte zusammenhang Dezimalzahl mit Neunerperiode
Warum ist $0{,}999\dots$ genau gleich 1, obwohl keine der Teilsummen $0{,}9;\ 0{,}99;\ 0{,}999;\ \dots$ die 1 erreicht?
---
Weil das Symbol $0{,}999\dots$ nicht eine dieser Teilsummen meint, sondern ihren Grenzwert: $\frac9{10}\sum_{n=0}^\infty(\frac1{10})^n=\frac9{10}\cdot\frac{10}9=1$. Beide Schreibweisen bezeichnen dieselbe Zahl.
--- falsch
Weil man nach unendlich vielen Neunen auf 1 rundet: Der Unterschied $10^{-N}$ wird so klein, dass man ihn weglässt; streng genommen bleibt $0{,}999\dots$ ein wenig unter 1.
--- falsch
Weil das Symbol die letzte der Teilsummen meint, und diese letzte Teilsumme hat unendlich viele Neunen; deshalb erreicht sie die 1 im Unterschied zu allen früheren.
--- falsch
Weil $0{,}999\dots$ und 1 sich um die Zahl $0{,}000\dots1$ unterscheiden, die man in $\mathbb{R}$ gleich null setzt. Die Gleichheit ist also eine Vereinbarung und keine Rechnung.
:::
:::karte zusammenhang Teleskopsumme
Warum lässt sich die Teilsumme der Reihe $\sum\frac1{n(n+1)}$ geschlossen angeben, und welchen Wert hat die Reihe?
---
Wegen $\frac1{n(n+1)}=\frac1n-\frac1{n+1}$ heben sich in der Teleskopsumme alle inneren Glieder auf, es bleibt $1-\frac1{N+1}$. Der Wert der Reihe ist deshalb 1.
--- falsch
Wegen $\frac1{n(n+1)}=\frac1n-\frac1{n+1}$ heben sich alle inneren Glieder auf, es bleibt $1-\frac1{N+1}$. Der Wert ist trotzdem unendlich, weil beide Teilreihen divergieren.
--- falsch
Wegen $\frac1{n(n+1)}=\frac1n+\frac1{n+1}$ ergeben die Glieder zwei harmonische Reihen, es bleibt $H_N+H_{N+1}-1$. Die Reihe divergiert deshalb wie die harmonische.
--- falsch
Weil man die ersten Teilsummen ausrechnet: $\frac12$, $\frac23$, $\frac34$, allgemein $\frac N{N+1}$. Der Wert der Reihe ist deshalb $\frac N{N+1}$, er hängt vom Abbruch ab.
:::
::::
