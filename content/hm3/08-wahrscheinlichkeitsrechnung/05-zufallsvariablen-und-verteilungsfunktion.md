---
title: Stufe 4: Zufallsvariablen und Verteilungsfunktion
pfad: Elektrotechnik / 3. Semester / HöMa3 – Höhere Mathematik 3 / Wahrscheinlichkeitsrechnung
adresse: elektrotechnik/3-semester/hohere-mathematik-3/wahrscheinlichkeitsrechnung
knoten: Kapitel 8: Wahrscheinlichkeitsrechnung
order: 3180500
summary: Meist interessiert nicht der Ausgang selbst, sondern eine Zahl, die aus ihm folgt: eine Summe, eine Anzahl, eine Ausfallzeit.
tags: Zufallsvariable, Messbarkeit, Verteilungsfunktion
lang: de
---

<span class="anker" id="stufe-4"></span>

:::zweck
Meist interessiert nicht der Ausgang selbst, sondern eine Zahl, die aus ihm folgt: eine Summe, eine Anzahl, eine Ausfallzeit. Diese Stufe macht aus solchen Zahlen ein mathematisches Objekt und beschreibt es durch eine einzige Funktion.
:::

**Die Idee.** Eine Zufallsvariable ist eine Funktion, die jedem Ausgang eine Zahl zuordnet. An ihr selbst ist nichts zufällig, zufällig ist nur, welcher Ausgang eintritt. Bei den Vierer-Würfeln ist $S(\omega_1,\omega_2)=\omega_1+\omega_2$ eine solche Funktion. Die Frage „Ist der Wert höchstens $x$?“ muss dabei ein zugelassenes Ereignis sein, sonst hätte sie keine Wahrscheinlichkeit.

:::definition Definition 4.1 (Zufallsvariable und Verteilungsfunktion)
<span class="anker" id="satz-4-1"></span>

Eine reelle __Zufallsvariable__ ist eine Funktion $X:\Omega\to\mathbb{R}$ mit

<span class="anker" id="gl-4-1"></span>
$$\{\omega\in\Omega:X(\omega)\le x\}\in\mathcal E\quad\text{für alle }x\in\mathbb{R}. \tag{4.1}$$

Diese Eigenschaft heißt __Messbarkeit__. Die Funktion $F_X(x):=\mathbb{P}(X\le x)$, $x\in\mathbb{R}$, heißt __Verteilungsfunktion__ von $X$. Dabei steht $\mathbb{P}(X\le x)$ kurz für $\mathbb{P}(\{\omega\in\Omega:X(\omega)\le x\})$.
:::

⁠**So liest man das:** $F_X(x)$ ist die Wahrscheinlichkeit, dass $X$ höchstens $x$ ist. Für $a<b$ ist $\{X\le a\}\subset\{X\le b\}$, also folgt aus Regel (iii) von Satz [1.3](ereignisse-und-wahrscheinlichkeit.html#satz-1-3)

<span class="anker" id="gl-4-2"></span>
$$\mathbb{P}(a<X\le b)=F_X(b)-F_X(a). \tag{4.2}$$

Mit einer stetigen Funktion $g:\mathbb{R}\to\mathbb{R}$ ist auch $Y=g(X)$ eine Zufallsvariable, denn $\{x:g(x)\le y\}$ ist abgeschlossen und entsteht aus Intervallen durch abzählbar viele Mengenoperationen.

::::beispiel die Summe
Für $S$ zählt man die Felder von Abb. [1](ereignisse-und-wahrscheinlichkeit.html#abb-1) längs der Nebendiagonalen ab:

| $s$ | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
|---|---|---|---|---|---|---|---|
| $16\,\mathbb{P}(S=s)$ | 1 | 2 | 3 | 4 | 3 | 2 | 1 |
| $16\,F_S(s)$ | 1 | 3 | 6 | 10 | 13 | 15 | 16 |

$F_S$ ist eine Treppe (Abb. [4](#abb-4)): null für $x<2$, eins für $x\ge8$, und die Sprunghöhe ist die Wahrscheinlichkeit des Werts.

:::abbildung hm3/k8treppe 4
Summe zweier Vierer-Würfel. Rechts summiert die Verteilungsfunktion die Balken von links auf. An jedem Sprung gilt der obere Wert, denn $\{S\le s\}$ enthält $s$.
:::
::::

:::satz Satz 4.2 (Eigenschaften der Verteilungsfunktion)
<span class="anker" id="satz-4-2"></span>

Die Verteilungsfunktion $F_X:\mathbb{R}\to[0,1]$ einer Zufallsvariablen ist monoton steigend und rechtsseitig stetig, und es gilt $\lim_{x\to-\infty}F_X(x)=0$, $\lim_{x\to\infty}F_X(x)=1$.
:::

:::beweis Eigenschaften der Verteilungsfunktion
Monotonie: Aus $x\le y$ folgt $\{X\le x\}\subset\{X\le y\}$. Die drei Grenzwerte folgen aus Satz [1.4](ereignisse-und-wahrscheinlichkeit.html#satz-1-4):

Fällt $x_n$ von oben gegen $x$, fallen die Mengen $\{X\le x_n\}$ ab, ihr Schnitt ist $\{X\le x\}$. Also gilt $F_X(x_n)\to F_X(x)$.

Für $x_n\to-\infty$ monoton ist der Schnitt der abfallenden Mengen $\{X\le x_n\}$ leer, kein $\omega$ liegt in allen. Für $x_n\to\infty$ monoton ist die Vereinigung der steigenden Mengen $\Omega$, jedes $\omega$ liegt irgendwann drin.
:::

⁠**Grenzfall:** Für eine Konstante $X\equiv c$ ist $F_X(x)=0$ für $x<c$ und $F_X(x)=1$ für $x\ge c$, eine einzige Stufe.

:::frage Warum ist $F_X$ von rechts stetig, aber nicht von links?
Das liegt am $\le$. Von links kommend ist die Vereinigung der Mengen $\{X\le x_n\}$ nur $\{X<x\}$. Es fehlt $\mathbb{P}(X=x)$, die Sprunghöhe.
:::

:::aufgabe Aufgabe 6 ★ Ein Spiel als Zufallsvariable
<span class="anker" id="aufg-6"></span>

Bei den Vierer-Würfeln zahlt ein Spiel $X=6$ für $(4,4)$, $X=2$ für jedes andere Paar mit gleichen Augenzahlen, sonst $X=0$. Gib $F_X$ an. Wie groß sind $F_X(0)$, $F_X(1)$ und $\mathbb{P}(0<X\le2)$?

:::loesung
$\mathbb{P}(X=6)=\frac1{16}$, $\mathbb{P}(X=2)=\frac3{16}$, $\mathbb{P}(X=0)=\frac{12}{16}$. Also ist $F_X(x)=0$ für $x<0$, $\frac34$ für $0\le x<2$, $\frac{15}{16}$ für $2\le x<6$ und 1 für $x\ge6$. Damit $F_X(0)=F_X(1)=\frac34$, denn $X=0$ kommt vor. $\mathbb{P}(0<X\le2)=F_X(2)-F_X(0)=\frac3{16}$.
:::
:::
