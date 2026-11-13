---
title: Stufe 7: Verdichten und der Entscheidungsweg
pfad: Elektrotechnik / 1. Semester / HöMa1 – Höhere Mathematik 1 / Unendliche Reihen
adresse: elektrotechnik/1-semester/hohere-mathematik-1/unendliche-reihen
knoten: Kapitel 6: Unendliche Reihen
order: 1260900
summary: Bei frac1 nlog n schweigen Quotient und Wurzel ( alpha=1 ), und die Reihen sumfrac1 n s helfen auch nicht.
tags: 
lang: de
---

<span class="anker" id="stufe-7"></span>

:::zweck
Bei $\frac1{n\log n}$ schweigen Quotient und Wurzel ($\alpha=1$), und die Reihen $\sum\frac1{n^s}$ helfen auch nicht. Diese Stufe macht aus dem Blocktrick von Stufe [5](absolute-konvergenz-und-vergleich.html#stufe-5) einen allgemeinen Test. Damit ist der Werkzeugkasten voll, und ein Entscheidungsweg ordnet ihn.
:::

**Die Idee.** Fallen die Glieder monoton, ist in einem Block jedes Glied höchstens das erste und mindestens das letzte. Ein Block aus $2^k$ Gliedern lässt sich also durch $2^k$ mal ein Glied ersetzen, nach oben wie nach unten (Abb. [7](#abb-7)). Von der ganzen Reihe bleiben nur die Glieder an Zweierpotenzen, die Reihe wird „verdichtet“.

:::satz Satz 7.1 (Cauchyscher Verdichtungssatz)
<span class="anker" id="satz-7-1"></span>

Sei $\sum_{n=1}^\infty a_n$ eine Reihe mit $\{a_n\}$ monoton fallend und $a_n>0$ für alle $n\in\mathbb{N}$. Dann gilt:

<span class="anker" id="gl-7-1"></span>
$$\sum_{n=1}^\infty a_n\ \text{ist konvergent}\quad\iff\quad\sum_{k=0}^\infty2^k\,a_{(2^k)}\ \text{ist konvergent}. \tag{7.1}$$
:::

⁠**So liest man das:** Mit $n_k:=2^k$ ist $\{a_{n_k}\}$ eine Teilfolge von $\{a_n\}$. Nur jedes „$2^k$-te“ Glied wird summiert, dafür mit dem Gewicht $2^k$: Für $k=3$ steht rechts $8\,a_8$. Der Satz sagt nicht, dass beide Reihen denselben Wert haben. **Voraussetzung nötig:** Sei $a_n=\frac1{n^2}$ an den Zweierpotenzen und $a_n=\frac1n$ sonst. Rechts steht $\sum(\frac12)^k$, links divergiert die Reihe, weil an den Zweierpotenzen nur eine konvergente Reihe fehlt.

:::beweis Zwei Blockzerlegungen
„$\Leftarrow$“: Der Block $n=2^k,\dots,2^{k+1}-1$ hat $2^k$ Glieder, jedes höchstens $a_{(2^k)}$:

$$S_{2^m-1}=\sum_{k=0}^{m-1}\ \sum_{n=2^k}^{2^{k+1}-1}a_n\le\sum_{k=0}^{m-1}2^k\,a_{(2^k)}.$$

Konvergiert die rechte Reihe, ist $\{S_N\}$ beschränkt, das Monotonie-Lemma gibt die Konvergenz.

„$\Rightarrow$“: Der Block $n=2^{k-1}+1,\dots,2^k$ hat $2^{k-1}$ Glieder, jedes mindestens $a_{(2^k)}$:

$$S_{2^m}=a_1+\sum_{k=1}^m\ \sum_{n=2^{k-1}+1}^{2^k}a_n\ge\sum_{k=1}^m2^{k-1}\,a_{(2^k)}=\frac12\sum_{k=1}^m2^k\,a_{(2^k)}.$$

Ist $\{S_N\}$ beschränkt, sind die Teilsummen rechts beschränkt und wachsen, also konvergiert die rechte Reihe.
:::

:::abbildung hm1/k6verdichtung 7
Der Satz am Beispiel $a_n=\frac1n$. Links überdecken die Rechtecke $2^k\,a_{(2^k)}$ alle Balken, rechts liegen die Rechtecke $2^{k-1}\,a_{(2^k)}$ in den Balken. Die Reihe liegt also zwischen der Hälfte der verdichteten Reihe und ihr selbst.
:::

::::beispiel
Sei $a_n=\frac1{n\log n}$ für $n\ge2$. Die Glieder fallen, weil $n$ und $\log n$ wachsen. Dass die Reihe bei 2 beginnt, stört nicht: Setzt man $a_1:=a_2$, ändert ein zusätzliches Glied die Konvergenz nicht. Es ist

$$2^k\,a_{(2^k)}=\frac{2^k}{2^k\,\log(2^k)}=\frac1{\log2}\cdot\frac1k\qquad(k\ge1).$$

Das ist die harmonische Reihe mal einer Zahl, also divergiert $\sum_{n=2}^\infty\frac1{n\log n}$. Sichtbar wird das kaum: Für $D_N=\sum_{n=2}^N\frac1{n\log n}$ ist $D_{10}=1{,}650$, $D_{1000}=2{,}727$, $D_{10^6}=3{,}420$.
::::

⁠**Grenzfall:** Für $a_n=\frac1{n^s}$ mit $s>0$ ist $2^k\,a_{(2^k)}=(2^{1-s})^k$, das ist genau die Aussage aus Stufe [5](absolute-konvergenz-und-vergleich.html#stufe-5).

**Warum die Vergleichsreihen hier nicht helfen.** Der Logarithmus wächst langsamer als jede Wurzel: Für alle $m\in\mathbb{N}$ gilt ([Kapitel 5](/wissen/elektrotechnik/1-semester/hohere-mathematik-1/exponentialfunktion-und-stetigkeit/exponentialfunktion-und-stetigkeit.html))

$$1<\log x<\sqrt[m]x=x^{\frac1m}\qquad\forall\,x>(4m^2)^m.$$

Mit $\varepsilon=\frac1m$ folgt $1<\log n<n^\varepsilon$ für alle $n\ge C(\varepsilon)$ mit einer Schranke $C(\varepsilon)$, und daraus

$$\frac1{n^{1+\varepsilon}}<\frac1{n\log n}<\frac1n\qquad\text{für große }n\in\mathbb{N}.$$

Die obere Reihe divergiert, ist also keine brauchbare Majorante. Die untere konvergiert, ist also keine brauchbare Minorante. Das Glied sitzt in der Lücke zwischen beiden, für jedes noch so kleine $\varepsilon$. Für $\varepsilon=\frac12$ und $n=10^6$ lauten die drei Zahlen $10^{-9}$, $7{,}2\cdot10^{-8}$ und $10^{-6}$.

**Der Entscheidungsweg.** Damit sind alle Tests vorhanden. Ihre Reihenfolge geht von billig zu teuer: Zuerst kommt die Frage, die nur einen Blick kostet, dann die Bauform des Glieds. Alle Tests messen dasselbe, nämlich wie schnell die Glieder fallen: gemessen an $q^n$ (Quotient, Wurzel), an $\frac1{n^s}$ (Vergleich) oder in Blöcken (Verdichtung). Je langsamer die Glieder fallen, desto feiner muss das Werkzeug sein (Abb. [8](#abb-8)). Vier Durchläufe zeigt die Tabelle.

:::abbildung hm1/k6wegweiser 8
Der Entscheidungsweg, von oben nach unten. Ab der vierten Frage wird $\sum|a_n|$ beurteilt. Bei positiven Gliedern ist das die Reihe selbst. Bei gemischten Vorzeichen zeigt eine divergente $\sum|a_n|$ nur, dass die Reihe nicht absolut konvergiert.
:::

| Reihe | Weg und Ergebnis |
|---|---|
| $\sum\frac{2n}{3n+1}$ | Die Glieder streben gegen $\frac23$, nicht gegen 0: divergent |
| $\sum\frac{(-1)^n}{n+\sqrt n}$ | Die Schrittweite fällt gegen 0: konvergent nach Leibniz. Wegen $\frac1{n+\sqrt n}\ge\frac1{2n}$ divergieren die Beträge: bedingt konvergent |
| $\sum\frac{7^n}{(2n)!}$ | Fakultät: Der Quotient $\frac7{(2n+1)(2n+2)}$ strebt gegen 0: absolut konvergent |
| $\sum\frac{n+1}{n^3+2}$ | Nur Potenzen von $n$, der Quotient gibt $\alpha=1$. Vergleich: $\frac{n+1}{n^3+2}\le\frac{2n}{n^3}=\frac2{n^2}$: absolut konvergent |

:::frage Es gibt oft mehrere Wege. Welcher ist richtig?
Jeder, der ein Ergebnis liefert. $\sum\frac1{2^n}$ passt zu mehreren Fragen des Schemas, das Schema nennt nur den meist kürzesten Weg. Schweigt ein Test, ist das keine Aussage über die Reihe, sondern über den Test.
:::

:::aufgabe Aufgabe 8 ★★★ Die Lücke vermessen
<span class="anker" id="aufg-8"></span>

Für $\beta>0$ sei $c_n=\dfrac1{n(\log n)^\beta}$, $n\ge2$. Verdichte und zeige: Die Reihe konvergiert für $\beta>1$ und divergiert für $\beta\le1$. Warum ist $\sum\frac1{n(\log n)^2}$ kein Widerspruch dazu, dass $\frac1{n(\log n)^2}>\frac1{n^{1+\varepsilon}}$ für große $n$ gilt?

:::loesung
$c_n$ fällt, weil $n$ und $\log n$ wachsen und $\beta>0$ ist. Es ist $2^k\,c_{(2^k)}=\frac{2^k}{2^k(k\log2)^\beta}=(\log2)^{-\beta}\frac1{k^\beta}$ für $k\ge1$. Nach Satz [5.4](absolute-konvergenz-und-vergleich.html#satz-5-4) konvergiert das genau für $\beta>1$. Kein Widerspruch: $\sum\frac1{n^{1+\varepsilon}}$ ist eine konvergente Reihe, die unter $c_n$ liegt. Eine Reihe mit Decke unter der eigenen Treppe sagt nichts über deren Decke.
:::
:::

:::aufgabe Aufgabe 9 ★★ Sechs Reihen sortieren
<span class="anker" id="aufg-9"></span>

Gehe den Weg und entscheide: konvergent (absolut oder bedingt) oder divergent. (a) $\sum\frac{3n-1}{4n+5}$, (b) $\sum\frac{n^2}{n^4+1}$, (c) $\sum_{n\ge2}\frac{(-1)^n}{\log n}$, (d) $\sum\frac{4^n}{n\,3^n}$, (e) $\sum\bigl(\frac{2n}{3n+1}\bigr)^n$, (f) $\sum_{n\ge2}\frac1{n\sqrt{\log n}}$.

:::loesung
(a) Glieder streben gegen $\frac34$: divergent. (b) $\frac{n^2}{n^4+1}\le\frac1{n^2}$: absolut konvergent. (c) $\frac1{\log n}$ fällt gegen 0, Leibniz gibt Konvergenz. Wegen $\log n<n$ ist $\frac1{\log n}>\frac1n$, die Beträge divergieren: bedingt konvergent. (d) Quotient $\frac43\cdot\frac n{n+1}\to\frac43$: divergent. (e) Wurzel $\frac{2n}{3n+1}\to\frac23$: absolut konvergent. (f) Verdichten gibt $\frac1{\sqrt{k\log2}}$, also eine Reihe mit $s=\frac12$: divergent.
:::
:::

::::formelsammlung
**Cauchyscher Verdichtungssatz**

$$\sum_{n=1}^\infty a_n\ \text{ist konvergent}\quad\iff\quad\sum_{k=0}^\infty2^k\,a_{(2^k)}\ \text{ist konvergent}$$

Für $\{a_n\}$ monoton fallend und $a_n>0$. Über die Werte sagt der Satz nichts; ohne Monotonie kann er falsch werden.

**Schranken beim Verdichten**

$$S_{2^m-1}\le\sum_{k=0}^{m-1}2^k\,a_{(2^k)},\qquad S_{2^m}\ge\frac12\sum_{k=1}^m2^k\,a_{(2^k)}$$

Blöcke aus $2^k$ beziehungsweise $2^{k-1}$ Gliedern, jedes höchstens beziehungsweise mindestens $a_{(2^k)}$.

**Logarithmus im Nenner**

$$2^k\,a_{(2^k)}=\frac1{\log2}\cdot\frac1k$$

Für $a_n=\frac1{n\log n}$, $n\ge2$, und $k\ge1$: die harmonische Reihe mal einer Zahl, also divergiert $\sum_{n=2}^\infty\frac1{n\log n}$.

**Lücke zwischen den Vergleichsreihen**

$$\frac1{n^{1+\varepsilon}}<\frac1{n\log n}<\frac1n\qquad\text{für große }n\in\mathbb{N}$$

Für jedes noch so kleine $\varepsilon$, weil $1<\log x<\sqrt[m]x=x^{\frac1m}$ für alle $x>(4m^2)^m$ ([Kapitel 5](/wissen/elektrotechnik/1-semester/hohere-mathematik-1/exponentialfunktion-und-stetigkeit/exponentialfunktion-und-stetigkeit.html)). Die obere Reihe divergiert, die untere konvergiert: Keine taugt zum Vergleich.

**Die Lücke vermessen**

$$c_n=\frac1{n(\log n)^\beta},\qquad2^k\,c_{(2^k)}=(\log2)^{-\beta}\frac1{k^\beta}$$

Für $\beta>0$, $n\ge2$ und $k\ge1$: Die Reihe konvergiert für $\beta>1$ und divergiert für $\beta\le1$.
::::

::::lernkarten
:::karte formel Cauchyscher Verdichtungssatz
Was sagt der Cauchysche Verdichtungssatz über eine Reihe $\sum a_n$, deren Glieder $a_n>0$ monoton fallen?
---
$\sum_{n=1}^\infty a_n$ ist genau dann konvergent, wenn $\sum_{k=0}^\infty2^k\,a_{(2^k)}$ konvergent ist. Über die Werte der beiden Reihen sagt der Satz nichts.
--- falsch
$\sum_{n=1}^\infty a_n$ ist genau dann konvergent, wenn $\sum_{k=0}^\infty2^k\,a_{(2^k)}$ konvergent ist, und dann haben beide Reihen denselben Wert.
--- falsch
$\sum_{n=1}^\infty a_n$ ist genau dann konvergent, wenn $\sum_{k=0}^\infty a_{(2^k)}$ konvergent ist: Es genügt, die Glieder an den Zweierpotenzen ohne Gewicht zu summieren.
--- falsch
Ist $\sum_{k=0}^\infty2^k\,a_{(2^k)}$ konvergent, so ist es auch $\sum_{n=1}^\infty a_n$; die Umkehrung gilt nicht, weil die verdichtete Reihe größer ist.
:::
:::karte zusammenhang Monotonie beim Verdichten
Was passiert beim Verdichten, wenn die Glieder $a_n>0$ nicht monoton fallen?
---
Dann kann der Satz falsch werden: Für $a_n=\frac1{n^2}$ an den Zweierpotenzen und $a_n=\frac1n$ sonst konvergiert die verdichtete Reihe $\sum(\frac12)^k$, die Reihe selbst divergiert.
--- falsch
Nichts: Die Glieder an den Zweierpotenzen bestimmen das Verhalten der Reihe immer, die Monotonie vereinfacht nur den Beweis mit den beiden Blockzerlegungen.
--- falsch
Dann ist die verdichtete Reihe gar nicht erklärt, weil $a_{(2^k)}$ nur für monoton fallende Folgen gebildet werden darf.
--- falsch
Dann gilt der Satz noch in einer Richtung: Divergiert die verdichtete Reihe, so divergiert auch $\sum a_n$; nur die Umkehrung geht verloren, weil sich die Blöcke nicht mehr nach oben abschätzen lassen.
:::
:::karte herleitung Zwei Blockzerlegungen
Wie beweist man den Cauchyschen Verdichtungssatz mit zwei Zerlegungen der Teilsummen in Blöcke?
---
„$\Leftarrow$“: Der Block $n=2^k,\dots,2^{k+1}-1$ hat $2^k$ Glieder, jedes höchstens $a_{(2^k)}$, weil die Glieder monoton fallen.
---
Also gilt $S_{2^m-1}\le\sum_{k=0}^{m-1}2^k\,a_{(2^k)}$; konvergiert die rechte Reihe, ist $\{S_N\}$ beschränkt und konvergiert, weil $S_N$ wegen $a_n>0$ wächst und das Monotonie-Lemma greift.
---
„$\Rightarrow$“: Der Block $n=2^{k-1}+1,\dots,2^k$ hat $2^{k-1}$ Glieder, jedes mindestens $a_{(2^k)}$, weil die Glieder monoton fallen.
---
Also gilt $S_{2^m}\ge\sum_{k=1}^m2^{k-1}\,a_{(2^k)}=\frac12\sum_{k=1}^m2^k\,a_{(2^k)}$, weil $S_{2^m}$ aus $a_1>0$ und diesen Blöcken besteht.
---
Ist $\{S_N\}$ beschränkt, sind die Teilsummen der verdichteten Reihe beschränkt und wachsen, also konvergiert sie, weil das Monotonie-Lemma gilt.
:::
:::karte zusammenhang Logarithmus im Nenner
Warum divergiert die Reihe $\sum_{n=2}^\infty\frac1{n\log n}$, und welcher Test zeigt es?
---
Der Verdichtungssatz: Die Glieder fallen, weil $n$ und $\log n$ wachsen, und $2^k\,a_{(2^k)}=\frac1{\log2}\cdot\frac1k$ ergibt die harmonische Reihe mal einer Zahl, die divergiert.
--- falsch
Die notwendige Bedingung: $n\log n$ wächst langsamer als $n$, also bleiben die Glieder $\frac1{n\log n}$ über einer festen positiven Schranke und bilden keine Nullfolge.
--- falsch
Das Quotientenkriterium: Der Quotient $\frac{n\log n}{(n+1)\log(n+1)}$ strebt gegen eine Zahl über 1, also wachsen die Glieder am Ende.
--- falsch
Sie divergiert gar nicht: Verdichten ergibt $2^k\,a_{(2^k)}=\frac1{\log2}\cdot\frac1{k^2}$, eine konvergente Reihe, also konvergiert sie, nur sehr langsam.
:::
:::karte zusammenhang Lücke zwischen den Vergleichsreihen
Warum helfen die Vergleichsreihen $\sum\frac1{n^s}$ bei den Gliedern $\frac1{n\log n}$ nicht weiter?
---
Weil $\log n$ langsamer wächst als jede Wurzel, gilt $\frac1{n^{1+\varepsilon}}<\frac1{n\log n}<\frac1n$ für große $n$. Die obere Reihe divergiert, die untere konvergiert: Keine taugt zum Vergleich.
--- falsch
Weil $\frac1{n\log n}$ größer als $\frac1n$ ist; die harmonische Reihe wäre eine divergente Minorante, aber Minoranten liefern nie eine Aussage über die Konvergenz einer anderen Reihe.
--- falsch
Weil $\log n$ schneller wächst als jede Potenz $n^\varepsilon$; dann liegt $\frac1{n\log n}$ unter $\frac1{n^{1+\varepsilon}}$, und die Reihe konvergiert schon nach dem Vergleich.
--- falsch
Weil die Vergleichsreihen nur für ganzzahlige Exponenten $s$ erklärt sind, und das Glied $\frac1{n\log n}$ entspricht keinem ganzzahligen Exponenten.
:::
:::karte zusammenhang Entscheidungsweg
Nach welchem Grundsatz ist der Entscheidungsweg für Reihen geordnet, und was messen alle seine Tests?
---
Von billig zu teuer: zuerst die Frage, ob die Glieder gegen 0 gehen, dann die Bauform des Glieds. Alle Tests messen, wie schnell die Glieder fallen: an $q^n$, an $\frac1{n^s}$ oder in Blöcken.
--- falsch
Von teuer zu billig: zuerst die feinsten Werkzeuge wie die Verdichtung, weil sie immer eine Antwort geben, und zuletzt die notwendige Bedingung als Probe.
--- falsch
Von billig zu teuer; die Tests messen aber Verschiedenes: Quotient und Wurzel die Größe der Glieder, Vergleich und Verdichtung ihr Vorzeichenmuster und ihre Reihenfolge.
--- falsch
Von billig zu teuer: zuerst der Quotient, weil er für jede Reihe einen Wert $\alpha$ liefert, und erst danach die Frage, ob die Glieder gegen 0 gehen.
:::
:::karte zusammenhang wenn ein Test schweigt
Was bedeutet es, wenn ein Test im Entscheidungsweg schweigt, und welcher von mehreren möglichen Wegen ist der richtige?
---
Schweigt ein Test, ist das keine Aussage über die Reihe, sondern über den Test. Richtig ist jeder Weg, der ein Ergebnis liefert; das Schema nennt nur den meist kürzesten.
--- falsch
Schweigt ein Test, divergiert die Reihe, denn eine konvergente Reihe würde jeder passende Test erkennen. Richtig ist nur der Weg, den das Schema nennt.
--- falsch
Schweigt ein Test, konvergiert die Reihe höchstens bedingt, weil absolute Konvergenz immer erkannt wird. Richtig ist jeder Weg, der ein Ergebnis liefert.
--- falsch
Schweigt ein Test, kann auch kein anderer Test die Frage mehr entscheiden. Richtig ist deshalb immer der Weg, der zuerst angewandt wurde.
:::
:::karte formel Die Lücke vermessen
Für welche $\beta>0$ konvergiert die Reihe mit den Gliedern $c_n=\frac1{n(\log n)^\beta}$, $n\ge2$, und wie zeigt man das?
---
Verdichten gibt $2^k\,c_{(2^k)}=(\log2)^{-\beta}\frac1{k^\beta}$ für $k\ge1$. Nach den Reihen $\sum\frac1{n^s}$ konvergiert das genau für $\beta>1$; für $\beta\le1$ divergiert die Reihe.
--- falsch
Verdichten gibt $2^k\,c_{(2^k)}=(\log2)^{-\beta}\frac1{k^\beta}$ für $k\ge1$. Das konvergiert für alle $\beta>0$, weil der Logarithmus im Nenner die Glieder genug verkleinert.
--- falsch
Verdichten gibt $2^k\,c_{(2^k)}=(\log2)^{-\beta}\frac1{k^\beta}$ für $k\ge1$. Das konvergiert genau für $\beta\ge1$, der Grenzfall $\beta=1$ gehört zur konvergenten Seite.
--- falsch
Verdichten gibt $2^k\,c_{(2^k)}=(\log2)^{-\beta}\frac1{2^{k\beta}}$, eine geometrische Reihe mit $q=2^{-\beta}<1$; sie konvergiert für alle $\beta>0$.
:::
::::
