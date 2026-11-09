---
title: Stufe 5: Absolute Konvergenz und Vergleich
pfad: Elektrotechnik / 1. Semester / Höhere Mathematik 1 / Unendliche Reihen
order: 1260700
summary: Stufe 3 braucht ein strenges Vorzeichenmuster.
tags: absolut konvergent, bedingt konvergent, majorisiert, Majorante, Minorante
lang: de
---

<span class="anker" id="stufe-5"></span>

:::zweck
Stufe [3](wechselnde-vorzeichen.html#stufe-3) braucht ein strenges Vorzeichenmuster. Für beliebige Vorzeichen hilft ein anderer Weg: alle Glieder positiv machen. Dann bleibt nur die Frage nach der Decke.
:::

**Die Idee.** Sind alle Glieder positiv, steigt die Treppe nur, und das Monotonie-Lemma sagt: Eine Decke genügt für die Konvergenz. Konvergiert schon die Treppe der Beträge, kann die ursprüngliche Treppe nirgends mehr hin, denn jedes ihrer Teilstücke ist höchstens so hoch wie das Stück der Beträge. Eine Decke findet man durch Vergleich: Wer unter einer Treppe mit Decke bleibt, hat selbst eine.

:::definition Definition 5.1 (Absolute und bedingte Konvergenz)
<span class="anker" id="satz-5-1"></span>

Die Reihe $\sum_{n=1}^\infty a_n$ heißt __absolut konvergent__, wenn $\sum_{n=1}^\infty|a_n|$ konvergiert. Ist $\sum_{n=1}^\infty a_n$ konvergent, aber $\sum_{n=1}^\infty|a_n|$ nicht, heißt die Reihe __bedingt konvergent__.
:::

:::satz Satz 5.2 (Absolut konvergente Reihen)
<span class="anker" id="satz-5-2"></span>

Für eine Reihe $\sum_{n=1}^\infty a_n$ gilt:

<ol class="rm">

<li>

Jede absolut konvergente Reihe ist auch konvergent.

</li>

<li>

Mit $\bar S_N:=\sum_{k=1}^N|a_k|$ gilt: $\sum_{n=1}^\infty a_n$ ist absolut konvergent $\iff$ $\{\bar S_N\}_{N=1}^\infty$ ist beschränkt.

</li>

</ol>
:::

⁠**So liest man das:** $\bar S_N$ ist die Höhe der Betragstreppe, bei $L_N$ etwa $\bar S_3=H_3=1{,}833$ statt $L_3=0{,}833$. (i) gilt nicht umgekehrt: $L_N$ konvergiert, die Beträge bilden die harmonische Reihe. Diese Reihe ist also bedingt konvergent. Die Reihe $\sum\frac{(-1)^n}{n^2}$ ist dagegen absolut konvergent, weil $Q_N$ konvergiert.

:::beweis Dreiecksungleichung und Monotonie
(i) Sei $\varepsilon>0$. Das Cauchy-Kriterium für $\sum|a_k|$ gibt ein $N_0$ mit $\sum_{k=m+1}^n|a_k|<\varepsilon$ für alle $n>m>N_0$. Die Dreiecksungleichung ergibt $\bigl|\sum_{k=m+1}^na_k\bigr|\le\sum_{k=m+1}^n|a_k|<\varepsilon$, und das Cauchy-Kriterium für $\sum a_k$ ist erfüllt.

(ii) $\{\bar S_N\}$ wächst monoton. Ist die Folge beschränkt, konvergiert sie nach dem Monotonie-Lemma. Konvergente Folgen sind beschränkt ([Teil 4](/wissen/elektrotechnik/1-semester/hohere-mathematik-1/folgen-und-grenzwerte/folgen-und-grenzwerte.html)).
:::

:::satz Satz 5.3 (Vergleichskriterium)
<span class="anker" id="satz-5-3"></span>

Seien $\sum_{n=1}^\infty a_n$ und $\sum_{n=1}^\infty b_n$ Reihen mit $|a_n|\le b_n$ für alle $n\in\mathbb{N}$.

<ol class="rm">

<li>

Ist $\sum_{n=1}^\infty b_n$ konvergent, dann ist $\sum_{n=1}^\infty a_n$ absolut konvergent.

</li>

<li>

Ist $\sum_{n=1}^\infty|a_n|$ divergent, dann ist auch $\sum_{n=1}^\infty b_n$ divergent.

</li>

</ol>
:::

⁠**So liest man das:** Aus der Bedingung folgt $b_n\ge0$. Für $a_n=(-\frac13)^n$ und $b_n=(\frac12)^n$ ist sie erfüllt. Man sagt, $\sum b_n$ __majorisiert__ $\sum|a_n|$, und nennt $\sum b_n$ eine __Majorante__ von $\sum|a_n|$. Im Fall (ii) ist $\sum|a_n|$ eine divergente __Minorante__ von $\sum b_n$. Weil endlich viele Glieder die Konvergenz nicht ändern, genügt die Bedingung ab einem Index. **Richtung beachten:** Liegen die $|a_n|$ über einer konvergenten oder unter einer divergenten Reihe, folgt nichts: $\frac1n\ge\frac1{n^2}$ und $\frac1{n^2}\le\frac1n$.

:::beweis Stück für Stück kleiner
(i) Sei $\varepsilon>0$. Das Cauchy-Kriterium für $\sum b_k$ gibt $N_0$ mit $\sum_{k=m+1}^nb_k<\varepsilon$ für $n>m>N_0$. Dann ist $\sum_{k=m+1}^n|a_k|\le\sum_{k=m+1}^nb_k<\varepsilon$, also konvergiert $\sum|a_k|$.

(ii) $\bar S_N$ wächst monoton und ist nach Satz [5.2](#satz-5-2) (ii) unbeschränkt, also gilt $\bar S_N\to\infty$. Wegen $\sum_{n=1}^Nb_n\ge\bar S_N$ wachsen auch die Teilsummen von $\sum b_n$ über jede Grenze.
:::

Für den Vergleich braucht man bekannte Reihen. Neben der geometrischen ist das diese Familie:

:::satz Satz 5.4 (Die Reihen $\sum1/n^s$)
<span class="anker" id="satz-5-4"></span>

Für festes $s\in\mathbb{R}$ ist $\sum_{n=1}^\infty\frac1{n^s}$ konvergent, falls $s>1$, und divergent, falls $s\le1$.
:::

⁠**So liest man das:** Der Exponent $s$ misst, wie schnell die Glieder fallen. $s=2$ ergibt $Q_N$, $s=1$ die harmonische Reihe, $s=\frac12$ die Reihe $\sum\frac1{\sqrt n}$. Die Grenze liegt genau bei $s=1$, und dieser Fall gehört zur divergenten Seite.

:::beweis Blöcke und drei Fälle
Fall $s\le0$: $\frac1{n^s}=n^{|s|}\ge1$ ist keine Nullfolge.

Fall $0<s\le1$: $\frac1{n^s}=\frac1n\,n^{1-s}\ge\frac1n$. Die harmonische Reihe ist eine divergente Minorante.

Fall $s>1$: Sei $B_k:=\sum_{n=2^k}^{2^{k+1}-1}\frac1{n^s}$ der Block aus $2^k$ Gliedern ab $n=2^k$. Weil $x^s$ wächst, ist jedes Glied höchstens das erste. Also

$$B_k\le2^k\cdot\frac1{(2^k)^s}=\bigl(2^{1-s}\bigr)^k=q^k\qquad\text{mit}\qquad q:=2^{1-s}<1.$$

Zusammen folgt $S_{2^m-1}=\sum_{k=0}^{m-1}B_k\le\sum_{k=0}^{m-1}q^k\le\frac1{1-q}$. Wegen $N\le2^N-1$ und weil $S_N$ wächst, gilt $S_N\le\frac1{1-q}$ für alle $N$. Das Monotonie-Lemma gibt die Konvergenz.
:::

⁠**Der Mechanismus:** Blockweise gelesen ist jede dieser Reihen eine geometrische Reihe mit $q=2^{1-s}$ (Abb. [5](#abb-5)). Bei $s=2$ halbieren sich die Blöcke. Bei $s=1$ ist $q=1$: Die harmonische Reihe ist im Blockbild die geometrische Reihe auf der Grenze.

:::abbildung hm1/k6bloecke 5
Die Blocksummen $B_k$ (Punkte) und ihre geometrische Schranke (orange gestrichelt). Links $s=1$: Die Blöcke bleiben zwischen $\frac12$ und 1, ihre Summe wächst ohne Ende. Rechts $s=2$: Die Blöcke fallen mindestens wie $(\frac12)^k$.
:::

::::beispiel [Beispiele]
Für $s=2$ ergibt die Schranke $Q_N\le2$. Tatsächlich ist $Q_{10}=1{,}5498$, $Q_{100}=1{,}6350$, der Wert ist $\frac{\pi^2}6=1{,}6449$ (ohne Beweis). Wegen $|\sin n|\le1$ ist $\sum\frac{\sin n}{n^2}$ absolut konvergent. Für $n\ge1$ ist $\frac{2n+1}{n^3+n}\le\frac{3n}{n^3}=\frac3{n^2}$, das ergibt ebenfalls eine konvergente Majorante. Aus $2n+3\le5n$ folgt $\frac1{2n+3}\ge\frac15\cdot\frac1n$: Die Minorante $\frac15\sum\frac1n$ divergiert, also auch $\sum\frac1{2n+3}$.
::::

⁠**Grenzfall:** Für $s$ knapp über 1 ist $\frac1{1-q}$ riesig: $s=1{,}01$ gibt die Schranke $145$. Die Reihe konvergiert, aber kaum sichtbar.

:::frage Reicht für die Decke nicht $a_n\le b_n$ ohne Betrag?
Für positive Glieder ist das dasselbe. Mit negativen Gliedern nicht: $a_n=-1$ liegt unter jeder Reihe mit $b_n\ge0$, zum Beispiel $b_n=(\frac12)^n$, und $\sum a_n$ divergiert trotzdem. Die Decke begrenzt nur die Höhe nach oben. Erst der Betrag verhindert auch den Absturz nach unten.
:::

:::aufgabe Aufgabe 6 ★★ Decke oder keine
<span class="anker" id="aufg-6"></span>

Entscheide mit einem Vergleich: (a) $\sum\frac{n+2}{n^3+1}$, (b) $\sum\frac1{\sqrt n+4}$, (c) $\sum\frac{\cos n}{2^n}$. (d) Für welche $s\in\mathbb{R}$ ist $\sum(-1)^n\frac1{n^s}$ absolut konvergent, bedingt konvergent, divergent?

:::loesung
(a) $\frac{n+2}{n^3+1}\le\frac{3n}{n^3}=\frac3{n^2}$: absolut konvergent. (b) Aus $\sqrt n+4\le5\sqrt n$ folgt $\frac1{\sqrt n+4}\ge\frac15\cdot\frac1{\sqrt n}$, eine divergente Minorante mit $s=\frac12$: divergent. (c) $\bigl|\frac{\cos n}{2^n}\bigr|\le(\frac12)^n$: absolut konvergent. (d) $s>1$: absolut konvergent. $0<s\le1$: konvergent nach Leibniz, die Beträge divergieren, also bedingt konvergent. $s\le0$: keine Nullfolge, divergent.
:::
:::
