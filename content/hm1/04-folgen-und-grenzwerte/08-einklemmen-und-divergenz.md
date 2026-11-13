---
title: Stufe 6: Einklemmen und Divergenz
pfad: Elektrotechnik / 1. Semester / HöMa1 – Höhere Mathematik 1 / Folgen und Grenzwerte
adresse: elektrotechnik/1-semester/hohere-mathematik-1/folgen-und-grenzwerte
knoten: Kapitel 4: Folgen und Grenzwerte
order: 1240800
summary: sqrt[n] n lässt sich nicht in Summen und Produkte zerlegen.
tags: divergent, bestimmt divergent, unbestimmt divergent
lang: de
---

<span class="anker" id="stufe-6"></span>

:::zweck
$\sqrt[n]{n}$ lässt sich nicht in Summen und Produkte zerlegen. Diese Stufe zeigt die Konvergenz durch Einklemmen und gibt den Folgen ohne Grenzwert ihre Namen.
:::

**Die Idee.** Läuft eine Folge zwischen zwei anderen, die zum selben Ziel laufen, bleibt ihr keine andere Wahl. Für große $n$ liegen beide Nachbarn im Schlauch um $a$, und die eingeklemmte Folge liegt zwischen ihnen (Abb. [7](#abb-7)).

:::satz Satz 6.1 (Sandwich-Lemma)
<span class="anker" id="satz-6-1"></span>

Für $\{a_n\}$, $\{b_n\}$, $\{c_n\}$ gebe es ein $N_0\in\mathbb{N}$, so dass

<span class="anker" id="gl-6-1"></span>
$$c_n\le a_n\le b_n\quad\forall\,n>N_0\qquad\text{und}\qquad\lim_{n\to\infty}c_n=\lim_{n\to\infty}b_n=a. \tag{6.1}$$

Dann ist $\{a_n\}$ konvergent mit $\lim_{n\to\infty}a_n=a$.
:::

⁠**So liest man das:** $a_n$ wird von unten und oben eingeklemmt, ohne dass man über $a_n$ selbst mehr wissen muss. Die Pendelfolge liegt zwischen $2-\frac3n$ und $2+\frac3n$, also gilt $a_n\to2$ ohne jedes $\varepsilon$. **Voraussetzung nötig:** Die beiden Grenzwerte müssen gleich sein. Aus $-1\le(-1)^n\le1$ folgt nichts. **Grenzfall:** Für $c_n=0$ und $a=0$ ergibt sich das Vergleichskriterium für $0\le a_n\le b_n$.

:::beweis Sandwich-Lemma
Sei $\varepsilon>0$. Wegen [(6.1)](#gl-6-1) gibt es $N_1$ und $N_2$ mit $-\varepsilon<c_n-a<\varepsilon$ für $n>N_1$ und $-\varepsilon<b_n-a<\varepsilon$ für $n>N_2$. Für $n>\tilde N_0:=\max\{N_0,N_1,N_2\}$ folgt $-\varepsilon<c_n-a\le a_n-a\le b_n-a<\varepsilon$, also $|a_n-a|<\varepsilon$.
:::

:::satz Satz 6.2 (Zwei $n$-te Wurzeln)
<span class="anker" id="satz-6-2"></span>

Es gilt (a) $\lim_{n\to\infty}\sqrt[n]{x}=1$ für jedes $x>0$, (b) $\lim_{n\to\infty}\sqrt[n]{n}=1$.
:::

⁠**So liest man das:** Die Wurzel $\sqrt[n]{x}$ ist die positive Zahl, deren $n$-te Potenz $x$ ergibt. Teil (a) sagt: Mit wachsendem $n$ reicht eine Zahl nahe 1, um durch Potenzieren jedes feste $x$ zu erreichen. Teil (b) sagt das sogar für das wachsende $n$ selbst.

:::beweis Einklemmen mit Bernoulli
(b) Für $k>0$ und $n\ge2$ gibt Bernoulli zweimal

$$(1+k)^{2n}=(1+k)^n\cdot(1+k)^n>(1+nk)(1+nk)>n^2k^2.$$

Sei $n\ge2$ und $k:=\sqrt[2n]{n}-1>0$. Dann ist $(1+k)^{2n}=n$, also $n>n^2k^2$ und damit $k<\frac1{\sqrt n}$. Das heißt $1\le\sqrt[2n]{n}<1+\frac1{\sqrt n}$, und Quadrieren ergibt

$$1\le\sqrt[n]{n}<\Bigl(1+\frac1{\sqrt n}\Bigr)^2.$$

Rechts steht nach den Rechenregeln eine Folge mit Grenzwert $(1+0)^2=1$. Das Sandwich-Lemma gibt (b).

(a) Für $x=1$ ist $\sqrt[n]{1}=1$. Für $x>1$ und $n>x$ gilt $1\le\sqrt[n]{x}\le\sqrt[n]{n}$, weil die Wurzel streng monoton wächst. Das Sandwich-Lemma und (b) ergeben die Behauptung. Für $0<x<1$ setzt man $y=\frac1x>1$. Dann ist $\sqrt[n]{x}=1/\sqrt[n]{y}\to1$ nach Rechenregel (iii).

Die Reihenfolge ist wichtig: (a) benutzt (b). Der Beweis von (b) darf deshalb (a) nicht benutzen, sonst setzte er voraus, was er zeigen soll.
:::

⁠**Zahlen:** $\sqrt[n]{n}=1{,}2589;\ 1{,}0471;\ 1{,}0069$ für $n=10;\ 100;\ 1000$, die obere Schranke ist dort $1{,}7325;\ 1{,}2100;\ 1{,}0642$.

:::abbildung hm1/k4sandwich 7
Die Folge $\sqrt[n]{n}$ (blau) zwischen der konstanten Folge 1 (grün) und $(1+1/\sqrt n)^2$ (orange). Beide Nachbarn streben gegen 1, die mittlere hat keine andere Wahl. Ihr größter Wert ist $\sqrt[3]{3}=1{,}442$.
:::

**Folgen ohne Grenzwert.** Nicht jede Folge hat einen Grenzwert, und es gibt zwei Arten, ihn zu verfehlen.

:::definition Definition 6.3 (Konvergenz und Divergenz)
<span class="anker" id="satz-6-3"></span>

<ol class="rm">

<li>

Die Folge $\{a_n\}$ heißt konvergent, falls es eine Zahl $a\in\mathbb{R}$ gibt mit $\lim_{n\to\infty}a_n=a$.

</li>

<li>

Folgen, die nicht konvergent sind, heißen __divergent__, und zwar __bestimmt divergent__, falls $a_n\to\infty$ oder $a_n\to-\infty$, und __unbestimmt divergent__ in allen anderen Fällen.

</li>

</ol>

Dabei bedeutet $a_n\to\infty$: $\forall\,M>0\ \exists\,n_0\in\mathbb{N}$ mit $a_n>M$ für alle $n>n_0$. Entsprechend bedeutet $a_n\to-\infty$: $\forall\,M>0\ \exists\,n_0\in\mathbb{N}$ mit $a_n<-M$ für alle $n>n_0$.
:::

⁠**So liest man das:** $n^2$ ist bestimmt divergent: Zu jeder Höhe $M$ gibt es einen Index, ab dem alle Glieder darüber bleiben. $(-1)^n$ ist unbestimmt divergent. Das Wort „konvergent“ fordert nur, dass es ein $a$ *gibt*, man muss es nicht kennen. Die Bedingung $a\in\mathbb{R}$ sieht harmlos aus, ihr Gewicht zeigt Stufe [7](monotone-folgen-und-die-vollstandigkeit.html#stufe-7).

:::frage Ist eine unbeschränkte Folge immer bestimmt divergent?
Nein. $(-1)^n\,n$ ist unbeschränkt und springt zwischen großen positiven und großen negativen Werten. Bestimmt divergent verlangt, dass ab einem Index alle Glieder jenseits von $M$ bleiben.
:::

:::aufgabe Aufgabe 8 ★★ Einklemmen und einordnen
<span class="anker" id="aufg-8"></span>

(a) Zeige mit dem Sandwich-Lemma, dass $\sqrt[n]{2^n+5^n}\to5$. Berechne $n=1$ und $n=10$ zur Kontrolle. (b) Ordne ein: konvergent, bestimmt oder unbestimmt divergent? $(-2)^n$; $\sqrt[n]{7}+(-1)^n/n$; $\sqrt{n}\,$; $\frac{n^2}{n+1}$.

:::loesung
(a) Es ist $5^n\le2^n+5^n\le2\cdot5^n$, also $5\le\sqrt[n]{2^n+5^n}\le5\sqrt[n]{2}$, und rechts geht es gegen 5. Zahlen: $n=1$ ergibt 7, $n=10$ ergibt $5{,}00005$ bei der Schranke $5{,}359$. (b) $(-2)^n$: unbeschränkt mit wechselndem Vorzeichen, unbestimmt divergent. $\sqrt[n]{7}+(-1)^n/n\to1+0=1$: konvergent. $\sqrt n$: Für $n>M^2$ ist $\sqrt n>M$, bestimmt divergent. $\frac{n^2}{n+1}\ge\frac{n^2}{2n}=\frac n2$: bestimmt divergent.
:::
:::

::::formelsammlung
**Sandwich-Lemma**

$$c_n\le a_n\le b_n\quad\forall\,n>N_0\qquad\text{und}\qquad\lim_{n\to\infty}c_n=\lim_{n\to\infty}b_n=a$$

Dann ist $\{a_n\}$ konvergent mit $\lim_{n\to\infty}a_n=a$. Die beiden Grenzwerte müssen gleich sein.

**Zwei $n$-te Wurzeln**

$$\lim_{n\to\infty}\sqrt[n]{x}=1\ \ (x>0),\qquad\lim_{n\to\infty}\sqrt[n]{n}=1$$

Bewiesen durch Einklemmen: $1\le\sqrt[n]{n}<\bigl(1+\frac1{\sqrt n}\bigr)^2$ für $n\ge2$.

**Bestimmt divergent**

$$a_n\to\infty:\quad\forall\,M>0\ \exists\,n_0\in\mathbb{N}\ \text{mit}\ a_n>M\ \text{für alle}\ n>n_0$$

Entsprechend $a_n\to-\infty$ mit $a_n<-M$. Divergent heißt nicht konvergent; unbestimmt divergent sind alle divergenten Folgen, die nicht bestimmt divergent sind.
::::

::::lernkarten
:::karte formel Sandwich-Lemma
Was besagt das Sandwich-Lemma für drei Folgen $\{a_n\}$, $\{b_n\}$, $\{c_n\}$, und welche Voraussetzung an die Grenzwerte ist unverzichtbar?
---
Gilt $c_n\le a_n\le b_n$ für alle $n>N_0$ und $\lim_{n\to\infty}c_n=\lim_{n\to\infty}b_n=a$, dann ist $\{a_n\}$ konvergent mit $\lim_{n\to\infty}a_n=a$. Die beiden Grenzwerte der Nachbarn müssen gleich sein.
--- falsch
Gilt $c_n\le a_n\le b_n$ für alle $n>N_0$ und konvergieren $c_n$ und $b_n$, dann konvergiert $a_n$ gegen den Mittelwert der beiden Grenzwerte; gleich müssen die Grenzwerte der Nachbarn dafür nicht sein.
--- falsch
Gilt $c_n\le a_n\le b_n$ für alle $n>N_0$ und $\lim_{n\to\infty}c_n=\lim_{n\to\infty}b_n=a$, dann ist $\{a_n\}$ beschränkt; konvergent ist $a_n$ nur, wenn man zusätzlich weiß, dass $a_n$ monoton ist.
--- falsch
Gilt $c_n\le a_n\le b_n$ für alle $n\in\mathbb{N}$ und $\lim_{n\to\infty}a_n=a$, dann konvergieren auch $c_n$ und $b_n$ gegen $a$: Die eingeklemmte Folge zieht ihre beiden Nachbarn zu ihrem eigenen Grenzwert mit.
:::
:::karte herleitung Sandwich-Lemma
Wie beweist man das Sandwich-Lemma aus $c_n\le a_n\le b_n$ für $n>N_0$ und $c_n\to a$, $b_n\to a$?
---
Sei $\varepsilon>0$. Es gibt $N_1$ mit $-\varepsilon<c_n-a<\varepsilon$ für $n>N_1$ und $N_2$ mit $-\varepsilon<b_n-a<\varepsilon$ für $n>N_2$, weil beide Nachbarn gegen $a$ konvergieren.
---
Für $n>\tilde N_0:=\max\{N_0,N_1,N_2\}$ gelten alle drei Aussagen zugleich, weil $n$ dann jeden der drei Indizes übertrifft.
---
Dort folgt $-\varepsilon<c_n-a\le a_n-a\le b_n-a<\varepsilon$, weil man in $c_n\le a_n\le b_n$ auf allen drei Seiten $a$ abziehen darf.
---
Also ist $|a_n-a|<\varepsilon$ für alle $n>\tilde N_0$, weil das nach der Abstandsregel dasselbe bedeutet; damit gilt $a_n\to a$.
:::
:::karte zusammenhang gleiche Grenzwerte nötig
Warum folgt aus $-1\le(-1)^n\le1$ nichts über die Konvergenz von $(-1)^n$, und welcher Sonderfall des Sandwich-Lemmas ist das Vergleichskriterium?
---
Weil die beiden Nachbarn verschiedene Grenzwerte haben, $-1$ und $1$; dazwischen bleibt der eingeklemmten Folge Platz zum Pendeln. Für $c_n=0$ und $a=0$ ergibt sich das Vergleichskriterium für $0\le a_n\le b_n$.
--- falsch
Weil $(-1)^n$ nicht monoton ist und das Sandwich-Lemma nur für monotone Folgen gilt. Für $c_n=0$ und $a=0$ ergibt sich das Vergleichskriterium für $0\le a_n\le b_n$, weil dann beide Nachbarn monoton sind.
--- falsch
Es folgt doch etwas: $(-1)^n$ konvergiert gegen 0, die Mitte zwischen $-1$ und $1$. Für $c_n=b_n$ ergibt sich das Vergleichskriterium, weil dann beide Nachbarn gleich sind und die Folge festlegen.
--- falsch
Weil die Nachbarn konstant sind und konstante Folgen keinen Grenzwert haben, sie nähern sich ja nichts an. Für $c_n=0$ und $a=1$ ergibt sich das Vergleichskriterium für $0\le a_n\le b_n$.
:::
:::karte formel Zwei n-te Wurzeln
Gegen welche Werte streben die $n$-ten Wurzeln $\sqrt[n]{x}$ für festes $x>0$ und $\sqrt[n]{n}$, wenn $n$ wächst?
---
Beide gegen 1: $\lim_{n\to\infty}\sqrt[n]{x}=1$ für jedes $x>0$ und $\lim_{n\to\infty}\sqrt[n]{n}=1$. Mit wachsendem $n$ reicht eine Zahl nahe 1, um durch Potenzieren $x$ und sogar das wachsende $n$ zu erreichen.
--- falsch
$\lim_{n\to\infty}\sqrt[n]{x}=1$ für jedes $x>0$, aber $\sqrt[n]{n}$ wächst ohne Grenze, weil unter der Wurzel das wachsende $n$ steht und schneller zunimmt, als der Wurzelexponent es ausgleichen kann.
--- falsch
$\lim_{n\to\infty}\sqrt[n]{x}=x$ für jedes $x>0$, weil die Wurzel den Wert einer festen Zahl nicht ändert, und $\lim_{n\to\infty}\sqrt[n]{n}=1$, weil sich das $n$ unter der Wurzel und im Exponenten kürzt.
--- falsch
$\lim_{n\to\infty}\sqrt[n]{x}=1$ nur für $x\ge1$ und $\lim_{n\to\infty}\sqrt[n]{x}=0$ für $0<x<1$; $\lim_{n\to\infty}\sqrt[n]{n}=1$, weil $n\ge1$ ist und deshalb der erste Fall greift.
:::
:::karte herleitung Einklemmen mit Bernoulli
Wie zeigt man mit der Bernoulli-Ungleichung und dem Sandwich-Lemma, dass $\sqrt[n]{n}\to1$ gilt?
---
Für $k>0$ und $n\ge2$ gibt Bernoulli zweimal $(1+k)^{2n}=(1+k)^n\cdot(1+k)^n>(1+nk)(1+nk)>n^2k^2$, weil $(1+k)^n>1+nk$ für $n\ge2$ und $k\ne0$ gilt.
---
Setze für $n\ge2$ die Zahl $k:=\sqrt[2n]{n}-1>0$. Dann ist $(1+k)^{2n}=n$, also $n>n^2k^2$ und damit $k<\frac1{\sqrt n}$, weil man durch $n^2$ teilen und die Wurzel ziehen darf.
---
Das heißt $1\le\sqrt[2n]{n}<1+\frac1{\sqrt n}$, und Quadrieren ergibt $1\le\sqrt[n]{n}<\bigl(1+\frac1{\sqrt n}\bigr)^2$, weil Quadrieren positiver Zahlen die Ungleichungen erhält.
---
Rechts steht nach den Rechenregeln eine Folge mit Grenzwert $(1+0)^2=1$, links die konstante Folge 1; das Sandwich-Lemma gibt $\sqrt[n]{n}\to1$, weil beide Nachbarn gegen 1 streben.
:::
:::karte zusammenhang Reihenfolge der Beweise
Wie folgt $\sqrt[n]{x}\to1$ für $x>1$ aus $\sqrt[n]{n}\to1$, und warum darf der Beweis für $\sqrt[n]{n}$ nicht umgekehrt den für $\sqrt[n]{x}$ benutzen?
---
Für $n>x$ gilt $1\le\sqrt[n]{x}\le\sqrt[n]{n}$, weil die Wurzel streng monoton wächst; das Sandwich-Lemma gibt $\sqrt[n]{x}\to1$. Weil dieser Teil den anderen benutzt, darf der andere ihn nicht benutzen: Er setzte sonst voraus, was er zeigen soll.
--- falsch
Für $n>x$ gilt $\sqrt[n]{n}\le\sqrt[n]{x}\le1$, und das Sandwich-Lemma gibt $\sqrt[n]{x}\to1$. Die Reihenfolge der Beweise ist dabei beliebig, weil beide Aussagen ohnehin wahr sind und ein Beweis sich auf jede wahre Aussage stützen darf.
--- falsch
Man setzt $x=n$ ein, weil $x$ beliebig gewählt werden darf; dann ist $\sqrt[n]{x}=\sqrt[n]{n}\to1$. Umgekehrt dürfte man genauso $n=x$ setzen und den einen Beweis aus dem anderen gewinnen, die beiden Beweise sind gleichwertig.
--- falsch
Für $n>x$ gilt $1\le\sqrt[n]{x}\le\sqrt[n]{n}$, und die Rechenregeln geben $\sqrt[n]{x}\to1$. Der Beweis für $\sqrt[n]{n}$ darf den für $\sqrt[n]{x}$ trotzdem benutzen, solange er ihn nur ein einziges Mal und erst am Ende benutzt.
:::
:::karte begriff divergent
Wann heißt eine Folge divergent, und was genau fordert das Gegenteil, die Konvergenz?
---
Eine Folge heißt divergent, wenn sie nicht konvergent ist. Konvergent heißt: Es gibt eine Zahl $a\in\mathbb{R}$ mit $\lim_{n\to\infty}a_n=a$; man muss diese Zahl nicht kennen.
--- falsch
Eine Folge heißt divergent, wenn sie unbeschränkt ist. Konvergent heißt: Sie ist beschränkt, denn dann gibt es eine Zahl $a\in\mathbb{R}$, der sich ihre Glieder nähern müssen.
--- falsch
Eine Folge heißt divergent, wenn sie gegen $\infty$ strebt. Konvergent heißt: Es gibt ein $a$ mit $\lim_{n\to\infty}a_n=a$, wobei auch $a=\infty$ als Grenzwert zugelassen ist.
--- falsch
Eine Folge heißt divergent, wenn man ihren Grenzwert nicht als Formel angeben kann. Konvergent heißt: Der Grenzwert $a$ ist bekannt und als Zahl hinschreibbar.
:::
:::karte begriff bestimmt divergent
Wann heißt eine Folge bestimmt divergent, und was bedeutet dabei die Schreibweise $a_n\to\infty$ genau?
---
Wenn $a_n\to\infty$ oder $a_n\to-\infty$ gilt. Dabei heißt $a_n\to\infty$: $\forall\,M>0\ \exists\,n_0\in\mathbb{N}$ mit $a_n>M$ für alle $n>n_0$; entsprechend heißt $a_n\to-\infty$, dass $a_n<-M$ für alle $n>n_0$.
--- falsch
Wenn sie unbeschränkt ist, also $\forall\,M>0\ \exists\,n\in\mathbb{N}$ mit $|a_n|>M$. Dabei genügt es, dass hinter jeder Höhe irgendwann ein Glied darüber liegt, wie bei $(-1)^n\,n$; das bedeutet die Schreibweise $a_n\to\infty$.
--- falsch
Wenn $a_n\to\infty$ oder $a_n\to-\infty$ gilt. Dabei heißt $a_n\to\infty$: $\exists\,M>0\ \forall\,n_0\in\mathbb{N}$ mit $a_n>M$ für ein $n>n_0$; eine einzige feste Höhe $M$ wird also immer wieder übertroffen.
--- falsch
Wenn sie streng monoton wächst. Dabei heißt $a_n\to\infty$, dass $a_{n+1}>a_n$ für alle $n$ gilt; jede streng monoton wachsende Folge ist deshalb bestimmt divergent, auch die Summenfolge.
:::
:::karte begriff unbestimmt divergent
Welche Folgen heißen unbestimmt divergent, und welches Beispiel aus dem Rechenmodell gehört dazu?
---
Divergente Folgen, die weder gegen $\infty$ noch gegen $-\infty$ streben, also alle divergenten Folgen außer den bestimmt divergenten. Ein Beispiel ist $(-1)^n$, die ewig springt.
--- falsch
Folgen, deren Konvergenzverhalten noch unbekannt ist, weil niemand einen Grenzwert gefunden hat. Ein Beispiel ist die Wurzelfolge, deren Grenzwert sich nicht als Bruch schreiben lässt.
--- falsch
Divergente Folgen, die gegen $\infty$ oder $-\infty$ streben, ohne dass man vorher weiß, gegen welches von beiden. Ein Beispiel ist $n^2$, die ohne Grenze wächst.
--- falsch
Beschränkte Folgen ohne Grenzwert; unbeschränkte Folgen sind dagegen immer bestimmt divergent. Ein Beispiel ist $(-1)^n$, ein Gegenbeispiel $(-1)^n\,n$, die bestimmt divergiert.
:::
:::karte zusammenhang unbeschränkt, aber nicht bestimmt divergent
Ist eine unbeschränkte Folge immer bestimmt divergent?
---
Nein. $(-1)^n\,n$ ist unbeschränkt und springt zwischen großen positiven und großen negativen Werten. Bestimmt divergent verlangt, dass ab einem Index alle Glieder jenseits von $M$ bleiben.
--- falsch
Ja. Unbeschränkt heißt, dass die Glieder über jede Höhe $M$ hinausgehen, und das ist genau die Bedingung $a_n\to\infty$; offen ist dabei höchstens noch das Vorzeichen der Glieder.
--- falsch
Nein, aber nur wegen der Monotonie: Eine unbeschränkte Folge ist bestimmt divergent, wenn sie monoton ist, und sonst konvergent, wie $(-1)^n\,n$, deren Vorzeichen sich aufheben.
--- falsch
Ja, sofern sie nach oben unbeschränkt ist; nur nach unten unbeschränkte Folgen können unbestimmt divergieren, weil $a_n\to-\infty$ in der Definition gar nicht vorkommt.
:::
:::karte zusammenhang Pendelfolge eingeklemmt
Wie zeigt das Sandwich-Lemma ohne jedes $\varepsilon$, dass die Pendelfolge $a_n=2+(-1)^n\,\frac3n$ gegen 2 konvergiert?
---
Sie liegt zwischen $2-\frac3n$ und $2+\frac3n$, weil $(-1)^n$ nur die Werte $-1$ und $1$ annimmt. Beide Nachbarn konvergieren nach den Rechenregeln gegen 2, also bleibt der eingeklemmten Folge keine andere Wahl.
--- falsch
Sie liegt zwischen $-1$ und $3{,}5$, ihrem kleinsten und ihrem größten Glied. Die Mitte dieses Streifens liegt ungefähr bei 2, und das Sandwich-Lemma gibt die Mitte zwischen den Nachbarn als Grenzwert.
--- falsch
Sie liegt zwischen $2-\frac3n$ und $2+\frac3n$; die beiden Nachbarn haben verschiedene Grenzwerte, aber ihr Abstand $\frac6n$ geht gegen 0, und das genügt dem Sandwich-Lemma auch ohne gleiche Grenzwerte.
--- falsch
Sie liegt zwischen ihren Gliedern $a_{n-1}$ und $a_{n+1}$, weil sie um 2 pendelt. Beide Nachbarn sind Glieder derselben Folge und haben deshalb denselben Grenzwert, nämlich 2.
:::
::::
