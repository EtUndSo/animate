---
title: Stufe 5: Rechenregeln
pfad: Elektrotechnik / 1. Semester / Höhere Mathematik 1 / Folgen und Grenzwerte
order: 1240700
summary: Epsilontik verlangt, den Grenzwert vorher zu kennen.
tags: 
lang: de
---

<span class="anker" id="stufe-5"></span>

:::zweck
Epsilontik verlangt, den Grenzwert vorher zu kennen. Rechenregeln liefern ihn aus den Bausteinen, ganz ohne $\varepsilon$.
:::

**Die Idee.** Liegt $a_n$ nah bei $a$ und $b_n$ nah bei $b$, liegt die Summe nah bei $a+b$: Die Fehler addieren sich höchstens. Beim Produkt zeigt Abb. [6](#abb-6) den Mechanismus: Der Unterschied zwischen den Rechtecken $a_nb_n$ und $ab$ besteht aus zwei Streifen, jeder hat eine Seite, die gegen 0 geht.

:::satz Satz 5.1 (Rechenregeln für konvergente Folgen)
<span class="anker" id="satz-5-1"></span>

Seien $\{a_n\}$, $\{b_n\}$ konvergent mit Grenzwerten $a,b\in\mathbb{R}$. Dann konvergieren die folgenden Folgen, und es gilt:

<ol class="rm">

<li>

$\lim\limits_{n\to\infty}(a_n+b_n)=\Bigl(\lim\limits_{n\to\infty}a_n\Bigr)+\Bigl(\lim\limits_{n\to\infty}b_n\Bigr)=a+b$,

</li>

<li>

$\lim\limits_{n\to\infty}(a_n\cdot b_n)=\Bigl(\lim\limits_{n\to\infty}a_n\Bigr)\cdot\Bigl(\lim\limits_{n\to\infty}b_n\Bigr)=a\cdot b$,

</li>

<li>

falls $a_n\ne0$ für alle $n$ und $a\ne0$: $\lim\limits_{n\to\infty}\dfrac1{a_n}=\Bigl(\lim\limits_{n\to\infty}a_n\Bigr)^{-1}=a^{-1}$,

</li>

<li>

$\lim\limits_{n\to\infty}|a_n|=\Bigl|\lim\limits_{n\to\infty}a_n\Bigr|=|a|$,

</li>

<li>

falls $a_n\ge0$ für alle $n$: $\lim\limits_{n\to\infty}\sqrt{a_n}=\sqrt{\lim\limits_{n\to\infty}a_n}=\sqrt a$.

</li>

</ol>
:::

⁠**So liest man das:** Jede Regel sagt zweierlei: Die neue Folge konvergiert, und ihr Grenzwert lässt sich aus $a$ und $b$ rechnen. Lesen darf man die Gleichung nur von rechts nach links: Existieren die Grenzwerte rechts, existiert der links. Aus der Konvergenz von $a_n+b_n$ folgt nichts über die Summanden, wie $(-1)^n+(-1)^{n+1}=0$ zeigt. **Voraussetzung nötig:** In (iii) darf $a$ nicht 0 sein: $a_n=\frac1n$ hat Grenzwert 0, aber $1/a_n=n$ ist unbeschränkt.

:::abbildung hm1/k4produkt 6
Produktregel als Fläche: $a_nb_n-ab=(a_n-a)\,b_n+a\,(b_n-b)$. Die Fläche $a_nb_n$ ist das ganze Rechteck, $ab$ der blaue Teil. Für größere $n$ werden beide Streifen schmaler, ihre Fläche geht gegen 0. Das Bild zeigt positive Größen, die Gleichung gilt für alle.
:::

:::beweis Rechenregeln
Alle Teile führen den Abstand auf die Nullfolgen $a_n-a$ und $b_n-b$ zurück.

(i) $(a_n+b_n)-(a+b)=(a_n-a)+(b_n-b)$ ist nach Satz [3.2](nullfolgen-vergleichen.html#satz-3-2) (i) eine Nullfolge.

(ii) Einschieben von $\pm a\,b_n$ gibt $|a_nb_n-ab|=|(a_n-a)\,b_n+a\,(b_n-b)|\le|b_n|\,|a_n-a|+|a|\,|b_n-b|$. Nach Satz [4.2](der-grenzwert.html#satz-4-2) (ii) ist $|b_n|\le C$, also ist $C\,|a_n-a|+|a|\,|b_n-b|$ eine Majorante.

(iii) Zu $\varepsilon=|a|/2$ gibt es $N_0$ mit $|a_n-a|<|a|/2$ für $n>N_0$. Die untere Dreiecksungleichung gibt dort $|a_n|\ge|a|-|a_n-a|>|a|/2$. Also ist $\bigl|\frac1{a_n}-\frac1a\bigr|=\frac{|a-a_n|}{|a_n|\,|a|}\le\frac2{a^2}\,|a_n-a|$ eine Majorante.

(iv) Die untere Dreiecksungleichung gibt $\bigl||a_n|-|a|\bigr|\le|a_n-a|$, eine Majorante.

(v) Es ist $a\ge0$, denn für $a<0$ läge kein Glied $a_n\ge0$ im Schlauch mit $\varepsilon=|a|$. Für $a=0$ ist das Satz [3.2](nullfolgen-vergleichen.html#satz-3-2) (ii). Für $a>0$ gilt nach der dritten binomischen Formel $(\sqrt{a_n}-\sqrt a)(\sqrt{a_n}+\sqrt a)=a_n-a$, also $|\sqrt{a_n}-\sqrt a|=\dfrac{|a_n-a|}{\sqrt{a_n}+\sqrt a}\le\dfrac{|a_n-a|}{\sqrt a}$, wieder eine Majorante.
:::

**Beispiel.** Für $r_n=\dfrac{3n^2-n+5}{n^2+4n+1}$ passen die Regeln nicht direkt, denn Zähler und Nenner sind unbeschränkt. Kürzen mit der höchsten Potenz $n^2$ macht aus beiden konvergente Folgen:

$$r_n=\frac{3-\frac1n+\frac5{n^2}}{1+\frac4n+\frac1{n^2}}\ \longrightarrow\ \frac{3-0+0}{1+0+0}=3.$$

Dabei sind $\frac1n$, $\frac1{n^2}$ Nullfolgen, die Regeln (i) und (ii) geben Zähler und Nenner, (iii) und (ii) den Bruch. Zahlen: $r_{10}=2{,}092$, $r_{100}=2{,}875$, $r_{1000}=2{,}987$. Im Rechenmodell gilt ebenso $a_n+s_n\to4$, $a_n\cdot s_n\to4$, $1/a_n\to\frac12$ und $\sqrt{s_n}\to\sqrt2$. **Grenzfälle:** Ist der Grad des Zählers kleiner als der des Nenners, ergibt das Kürzen 0, ist er größer, wird die Folge unbeschränkt. Bei gleichem Grad zählt das Verhältnis der führenden Koeffizienten, hier $3/1$.

:::frage Bei $\sqrt{n+4}-\sqrt n$ gilt doch „unendlich minus unendlich gleich null“?
Das Ergebnis stimmt, die Begründung nicht. Regel (i) setzt konvergente Summanden voraus, $\sqrt n$ konvergiert nicht. Dass die Differenz zweier unbeschränkter Folgen nichts Bestimmtes ergibt, zeigen $(n+4)-n=4$ und $(2n)-n=n$. Hier hilft erst das Umformen.
:::

:::aufgabe Aufgabe 7 ★★ Grenzwerte ausrechnen
<span class="anker" id="aufg-7"></span>

Bestimme die Grenzwerte und nenne jede benutzte Regel, oder begründe, warum keiner existiert. (a) $\dfrac{5n^2+2}{2n^2-n}$, (b) $\sqrt{n^2+6n}-n$, (c) $\dfrac{4n+1}{n^2+3}+0{,}9^n\,\dfrac{n}{n+1}$, (d) $\dfrac{3^n}{n^5}$.

:::loesung
(a) Kürzen mit $n^2$: $\dfrac{5+2/n^2}{2-1/n}\to\frac52$ nach (i), (ii), (iii). (b) Erweitern: $\dfrac{(n^2+6n)-n^2}{\sqrt{n^2+6n}+n}=\dfrac6{\sqrt{1+6/n}+1}\to\dfrac6{1+1}=3$ nach (i), (iii), (v). (c) Der erste Summand ist $\dfrac{4/n+1/n^2}{1+3/n^2}\to0$. Der zweite ist die Nullfolge $0{,}9^n$ mal der beschränkten Folge $n/(n+1)$. Der Grenzwert ist 0. (d) Mit $q=3^{-1/5}<1$ ist $n^5/3^n=(n\,q^n)^5\to0$ nach Satz [3.4](nullfolgen-vergleichen.html#satz-3-4) (ii) und Regel (ii). Der Kehrwert einer positiven Nullfolge wächst über jede Schranke: Die Folge ist bestimmt divergent.
:::
:::
