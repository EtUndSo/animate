---
title: Stufe 5: Absolute Konvergenz und Vergleich
pfad: Elektrotechnik / 1. Semester / HöMa1 – Höhere Mathematik 1 / Unendliche Reihen
adresse: elektrotechnik/1-semester/hohere-mathematik-1/unendliche-reihen
knoten: Kapitel 6: Unendliche Reihen
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

(ii) $\{\bar S_N\}$ wächst monoton. Ist die Folge beschränkt, konvergiert sie nach dem Monotonie-Lemma. Konvergente Folgen sind beschränkt ([Kapitel 4](/wissen/elektrotechnik/1-semester/hohere-mathematik-1/folgen-und-grenzwerte/folgen-und-grenzwerte.html)).
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

::::formelsammlung
**Absolute und bedingte Konvergenz**

$$\sum_{n=1}^\infty|a_n|\ \text{konvergent}$$

Dann heißt $\sum_{n=1}^\infty a_n$ absolut konvergent. Ist $\sum a_n$ konvergent, aber $\sum|a_n|$ nicht, heißt die Reihe bedingt konvergent.

**Absolut konvergent ergibt konvergent**

$$\Bigl|\sum_{k=m+1}^na_k\Bigr|\le\sum_{k=m+1}^n|a_k|$$

Mit dem Cauchy-Kriterium folgt: Jede absolut konvergente Reihe ist konvergent. Die Umkehrung gilt nicht.

**Teilsummen der Beträge**

$$\bar S_N:=\sum_{k=1}^N|a_k|$$

$\sum_{n=1}^\infty a_n$ ist absolut konvergent $\iff$ $\{\bar S_N\}_{N=1}^\infty$ ist beschränkt; $\bar S_N$ wächst monoton.

**Vergleichskriterium**

$$|a_n|\le b_n\quad\text{für alle }n\in\mathbb{N}$$

(i) Ist $\sum b_n$ konvergent (eine Majorante von $\sum|a_n|$), dann ist $\sum a_n$ absolut konvergent. (ii) Ist $\sum|a_n|$ divergent (eine divergente Minorante von $\sum b_n$), dann ist auch $\sum b_n$ divergent. Die Bedingung genügt ab einem Index.

**Reihen mit festem Exponenten**

$$\sum_{n=1}^\infty\frac1{n^s}$$

Für festes $s\in\mathbb{R}$ konvergent, falls $s>1$, und divergent, falls $s\le1$; $s=1$ ist die harmonische Reihe. Für $s=2$ ist der Wert $\frac{\pi^2}6$ (ohne Beweis).

**Blockschranke**

$$B_k\le2^k\cdot\frac1{(2^k)^s}=\bigl(2^{1-s}\bigr)^k=q^k\qquad\text{mit}\qquad q:=2^{1-s}<1$$

Für $s>1$ und den Block $B_k:=\sum_{n=2^k}^{2^{k+1}-1}\frac1{n^s}$ aus $2^k$ Gliedern; daraus folgt $S_N\le\frac1{1-q}$ für alle $N$.
::::

::::lernkarten
:::karte begriff absolut konvergent und absolute Konvergenz
Wann heißt eine Reihe $\sum_{n=1}^\infty a_n$ absolut konvergent, und welche Reihe muss man dafür untersuchen?
---
Wenn die Reihe der Beträge $\sum_{n=1}^\infty|a_n|$ konvergiert, die Reihe also auch dann konvergiert, wenn man alle Minuszeichen durch Pluszeichen ersetzt.
--- falsch
Wenn der Betrag $\bigl|\sum_{n=1}^\infty a_n\bigr|$ des Grenzwerts endlich ist; man untersucht also die Reihe selbst, das ist dasselbe wie gewöhnliche Konvergenz der Reihe.
--- falsch
Wenn alle Glieder positiv sind und die Reihe konvergiert; Reihen mit negativen Gliedern können deshalb nie absolut konvergent sein.
--- falsch
Wenn $\sum_{n=1}^\infty a_n$ konvergiert und die Beträge $|a_n|$ monoton fallen; man untersucht also die Folge der Beträge, nicht ihre Reihe.
:::
:::karte begriff bedingt konvergent
Wann heißt eine Reihe bedingt konvergent, und welche Reihe aus dem Rechenmodell ist ein Beispiel dafür?
---
Wenn $\sum_{n=1}^\infty a_n$ konvergiert, $\sum_{n=1}^\infty|a_n|$ aber nicht. Beispiel ist die alternierende harmonische Reihe: $L_N$ konvergiert, die Beträge bilden die harmonische Reihe.
--- falsch
Wenn $\sum_{n=1}^\infty|a_n|$ konvergiert, $\sum_{n=1}^\infty a_n$ aber nicht. Beispiel ist die alternierende harmonische Reihe, deren Beträge die harmonische Reihe bilden.
--- falsch
Wenn $\sum_{n=1}^\infty a_n$ nur unter einer Bedingung an die Glieder konvergiert, etwa $a_n\to0$. Beispiel ist die harmonische Reihe, deren Glieder gegen 0 gehen, obwohl ihre Teilsummen wachsen.
--- falsch
Wenn $\sum_{n=1}^\infty a_n$ konvergiert, $\sum_{n=1}^\infty|a_n|$ aber nicht. Beispiel ist $\sum\frac{(-1)^n}{n^2}$, weil ihre Glieder ihr Vorzeichen wechseln.
:::
:::karte formel absolut konvergente Reihen
Was folgt aus der absoluten Konvergenz einer Reihe, und wie lässt sie sich mit den Teilsummen der Beträge $\bar S_N$ prüfen?
---
Jede absolut konvergente Reihe ist auch konvergent. Mit $\bar S_N:=\sum_{k=1}^N|a_k|$ gilt: $\sum_{n=1}^\infty a_n$ ist absolut konvergent $\iff$ $\{\bar S_N\}_{N=1}^\infty$ ist beschränkt.
--- falsch
Jede konvergente Reihe ist auch absolut konvergent. Mit $\bar S_N:=\sum_{k=1}^N|a_k|$ gilt: $\sum_{n=1}^\infty a_n$ ist absolut konvergent $\iff$ $\{\bar S_N\}_{N=1}^\infty$ ist beschränkt.
--- falsch
Jede absolut konvergente Reihe ist auch konvergent. Mit $\bar S_N:=\sum_{k=1}^N|a_k|$ gilt: $\sum_{n=1}^\infty a_n$ ist absolut konvergent $\iff$ $\bar S_N\to0$ für $N\to\infty$.
--- falsch
Jede absolut konvergente Reihe ist auch konvergent. Mit $\bar S_N:=\bigl|\sum_{k=1}^Na_k\bigr|$ gilt: $\sum_{n=1}^\infty a_n$ ist absolut konvergent $\iff$ $\{\bar S_N\}_{N=1}^\infty$ ist beschränkt.
:::
:::karte herleitung Dreiecksungleichung und Cauchy-Kriterium
Wie folgt mit dem Cauchy-Kriterium und der Dreiecksungleichung, dass jede absolut konvergente Reihe konvergiert?
---
Zu $\varepsilon>0$ gibt das Cauchy-Kriterium für $\sum|a_k|$ ein $N_0$ mit $\sum_{k=m+1}^n|a_k|<\varepsilon$ für alle $n>m>N_0$, weil $\sum|a_k|$ konvergiert.
---
Die Dreiecksungleichung ergibt $\bigl|\sum_{k=m+1}^na_k\bigr|\le\sum_{k=m+1}^n|a_k|<\varepsilon$, weil sie für endlich viele Summanden gilt.
---
Damit erfüllt $\sum a_k$ das Cauchy-Kriterium und konvergiert, weil das Kriterium gleichbedeutend mit Konvergenz ist.
:::
:::karte formel Vergleichskriterium
Was folgt nach dem Vergleichskriterium aus $|a_n|\le b_n$ für alle $n\in\mathbb{N}$, und zwar in beiden Richtungen?
---
Ist $\sum b_n$ konvergent, dann ist $\sum a_n$ absolut konvergent. Ist $\sum|a_n|$ divergent, dann ist auch $\sum b_n$ divergent. Die Bedingung braucht nur ab einem Index zu gelten.
--- falsch
Ist $\sum b_n$ divergent, dann ist auch $\sum|a_n|$ divergent. Ist $\sum|a_n|$ konvergent, dann ist auch $\sum b_n$ konvergent. Die Bedingung braucht nur ab einem Index zu gelten.
--- falsch
Ist $\sum b_n$ konvergent, dann ist $\sum a_n$ konvergent, aber nicht unbedingt absolut. Ist $\sum|a_n|$ divergent, dann ist auch $\sum b_n$ divergent. Die Bedingung muss für alle $n$ gelten.
--- falsch
Ist $\sum b_n$ konvergent, dann ist $\sum a_n$ absolut konvergent, und beide Reihen haben denselben Wert. Ist $\sum|a_n|$ divergent, dann ist auch $\sum b_n$ divergent.
:::
:::karte zusammenhang Majorante und majorisiert
Was heißt es, dass $\sum b_n$ die Reihe $\sum|a_n|$ majorisiert, und warum liefert eine konvergente Majorante die absolute Konvergenz von $\sum a_n$?
---
Es heißt $|a_n|\le b_n$, und $\sum b_n$ heißt Majorante. Dann ist jedes Stück $\sum_{k=m+1}^n|a_k|$ höchstens $\sum_{k=m+1}^nb_k<\varepsilon$, das Cauchy-Kriterium überträgt sich also von $\sum b_n$ auf $\sum|a_n|$.
--- falsch
Es heißt $a_n\le b_n$ ohne Betrag, und $\sum b_n$ heißt Majorante. Dann ist jede Teilsumme von $\sum a_n$ höchstens die von $\sum b_n$, und eine Decke nach oben reicht für die Konvergenz.
--- falsch
Es heißt $b_n\le|a_n|$, und $\sum b_n$ heißt Majorante. Dann ist jedes Stück der Betragstreppe mindestens so hoch wie das von $\sum b_n$, und die Konvergenz überträgt sich nach oben.
--- falsch
Es heißt $|a_n|\le b_n$, und $\sum b_n$ heißt Majorante. Dann haben beide Reihen denselben Grenzwert, weil die kleinere Reihe von der größeren Schritt für Schritt mitgezogen wird.
:::
:::karte begriff Minorante
Was ist im Vergleichskriterium eine divergente Minorante, und welchen Schluss erlaubt sie?
---
Gilt $|a_n|\le b_n$ und divergiert $\sum|a_n|$, so ist $\sum|a_n|$ eine divergente Minorante von $\sum b_n$: eine Reihe, die gliedweise darunter liegt. Dann divergiert auch $\sum b_n$.
--- falsch
Gilt $|a_n|\le b_n$ und divergiert $\sum b_n$, so ist $\sum b_n$ eine divergente Minorante von $\sum|a_n|$: eine Reihe, die gliedweise darüber liegt. Dann divergiert auch die kleinere $\sum|a_n|$.
--- falsch
Gilt $|a_n|\le b_n$ und konvergiert $\sum|a_n|$, so ist $\sum|a_n|$ eine Minorante von $\sum b_n$: eine Reihe, die gliedweise darunter liegt. Dann konvergiert auch $\sum b_n$.
--- falsch
Gilt $|a_n|\ge b_n$ und divergiert $\sum|a_n|$, so ist $\sum|a_n|$ eine divergente Minorante von $\sum b_n$: eine Reihe, die gliedweise darüber liegt. Dann divergiert auch $\sum b_n$.
:::
:::karte zusammenhang Richtung beachten
Was folgt, wenn die Beträge $|a_n|$ über einer konvergenten oder unter einer divergenten Reihe liegen?
---
Nichts: $\frac1n\ge\frac1{n^2}$ liegt über einer konvergenten Reihe und divergiert, $\frac1{n^2}\le\frac1n$ liegt unter einer divergenten und konvergiert. Schlüsse gibt es nur unter einer konvergenten oder über einer divergenten Reihe.
--- falsch
Liegen sie über einer konvergenten Reihe, konvergiert $\sum|a_n|$ erst recht; liegen sie unter einer divergenten, divergiert $\sum|a_n|$ erst recht, denn der Vergleich wirkt in beide Richtungen.
--- falsch
Liegen sie über einer konvergenten Reihe, divergiert $\sum|a_n|$; liegen sie unter einer divergenten, konvergiert $\sum|a_n|$, denn die Vergleichsreihe wirkt dann als Gegenbeispiel.
--- falsch
Über $\sum|a_n|$ folgt nichts, wohl aber über $\sum a_n$: Liegen die Beträge über einer konvergenten Reihe, ist $\sum a_n$ bedingt konvergent, sonst divergent.
:::
:::karte formel Reihen mit festem Exponenten
Für welche festen $s\in\mathbb{R}$ konvergiert die Reihe $\sum_{n=1}^\infty\frac1{n^s}$, und zu welcher Seite gehört der Grenzfall $s=1$?
---
Sie konvergiert, falls $s>1$, und divergiert, falls $s\le1$. Der Grenzfall $s=1$ ist die harmonische Reihe und gehört zur divergenten Seite.
--- falsch
Sie konvergiert, falls $s\ge1$, und divergiert, falls $s<1$. Der Grenzfall $s=1$ gehört zur konvergenten Seite, weil die Glieder dort eine Nullfolge bilden.
--- falsch
Sie konvergiert, falls $s>0$, weil die Glieder dann eine Nullfolge bilden, und divergiert, falls $s\le0$. Auch $s=1$ konvergiert also.
--- falsch
Sie konvergiert, falls $s\ge2$, und divergiert, falls $s<2$. Der Grenzfall $s=2$ ist die Quadratreihe und gehört zur konvergenten Seite.
:::
:::karte herleitung Blöcke und drei Fälle
Wie zeigt man mit drei Fällen und Blöcken aus $2^k$ Gliedern, dass $\sum_{n=1}^\infty\frac1{n^s}$ genau für $s>1$ konvergiert?
---
Für $s\le0$ divergiert die Reihe, weil $\frac1{n^s}=n^{|s|}\ge1$ keine Nullfolge ist.
---
Für $0<s\le1$ divergiert sie, weil $\frac1{n^s}=\frac1n\,n^{1-s}\ge\frac1n$ gilt und die harmonische Reihe eine divergente Minorante ist.
---
Für $s>1$ gilt für den Block $B_k:=\sum_{n=2^k}^{2^{k+1}-1}\frac1{n^s}$ die Schranke $B_k\le2^k\cdot\frac1{(2^k)^s}=q^k$ mit $q:=2^{1-s}<1$, weil $x^s$ wächst und deshalb jedes der $2^k$ Glieder höchstens das erste ist.
---
Also ist $S_{2^m-1}=\sum_{k=0}^{m-1}B_k\le\sum_{k=0}^{m-1}q^k\le\frac1{1-q}$, weil die Teilsummen der geometrischen Reihe mit $0<q<1$ unter ihrem Wert bleiben.
---
Wegen $N\le2^N-1$ gilt $S_N\le\frac1{1-q}$ für alle $N$, weil $S_N$ wächst; das Monotonie-Lemma gibt die Konvergenz.
:::
:::karte zusammenhang geometrische Reihe auf der Grenze
Warum ist die harmonische Reihe im Blockbild die geometrische Reihe auf der Grenze?
---
Weil blockweise gelesen jede Reihe $\sum\frac1{n^s}$ unter einer geometrischen Reihe mit $q=2^{1-s}$ liegt, $B_k\le q^k$. Für $s=1$ ist $q=1$: Die Blöcke bleiben zwischen $\frac12$ und 1, ihre Summe wächst ohne Ende.
--- falsch
Weil ihre Glieder $\frac1n$ selbst eine geometrische Folge mit $q=\frac12$ bilden; das Blockbild macht nur sichtbar, dass sie gerade noch konvergiert.
--- falsch
Weil blockweise $q=2^{1-s}$ gilt und $q=1$ schon bei $s=0$ erreicht ist; die harmonische Reihe mit $s=1$ hat deshalb $q=\frac12$ und ist bereits eine konvergente geometrische Reihe.
--- falsch
Weil ihre Blöcke genau wie $(\frac12)^k$ fallen: Die Grenze liegt darin, dass ihre Summe den Wert 2 erreicht, aber nicht überschreitet.
:::
:::karte zusammenhang Betrag in der Bedingung
Warum verlangt das Vergleichskriterium $|a_n|\le b_n$ und nicht bloß $a_n\le b_n$?
---
Weil eine Decke nur die Höhe nach oben begrenzt: $a_n=-1$ liegt unter $b_n=(\frac12)^n$, und $\sum a_n$ divergiert trotzdem. Erst der Betrag verhindert auch den Absturz nach unten; für positive Glieder ist beides dasselbe.
--- falsch
Weil man den Betrag nur der Schreibweise wegen setzt: Für Reihen mit negativen Gliedern liefert $a_n\le b_n$ dieselben Schlüsse, denn negative Glieder verkleinern die Reihe nur.
--- falsch
Weil das Kriterium nur für Reihen mit positiven Gliedern gilt und der Betrag das ausdrückt; bei Reihen mit negativen Gliedern ist es nicht anwendbar, auch nicht mit Betrag.
--- falsch
Weil ohne Betrag die Majorante negativ sein könnte; der Betrag sorgt allein dafür, dass $b_n\ge0$ ist, an die $a_n$ selbst stellt er keine Bedingung.
:::
::::
