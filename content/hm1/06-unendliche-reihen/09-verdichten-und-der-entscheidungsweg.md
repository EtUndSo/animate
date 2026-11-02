---
title: Stufe 7: Verdichten und der Entscheidungsweg
pfad: Elektrotechnik / 1. Semester / Höhere Mathematik 1 / Unendliche Reihen
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

**Beispiel.** Sei $a_n=\frac1{n\log n}$ für $n\ge2$. Die Glieder fallen, weil $n$ und $\log n$ wachsen. Dass die Reihe bei 2 beginnt, stört nicht: Setzt man $a_1:=a_2$, ändert ein zusätzliches Glied die Konvergenz nicht. Es ist

$$2^k\,a_{(2^k)}=\frac{2^k}{2^k\,\log(2^k)}=\frac1{\log2}\cdot\frac1k\qquad(k\ge1).$$

Das ist die harmonische Reihe mal einer Zahl, also divergiert $\sum_{n=2}^\infty\frac1{n\log n}$. Sichtbar wird das kaum: Für $D_N=\sum_{n=2}^N\frac1{n\log n}$ ist $D_{10}=1{,}650$, $D_{1000}=2{,}727$, $D_{10^6}=3{,}420$. **Grenzfall:** Für $a_n=\frac1{n^s}$ mit $s>0$ ist $2^k\,a_{(2^k)}=(2^{1-s})^k$, das ist genau die Aussage aus Stufe [5](absolute-konvergenz-und-vergleich.html#stufe-5).

**Warum die Vergleichsreihen hier nicht helfen.** Der Logarithmus wächst langsamer als jede Wurzel: Für alle $m\in\mathbb{N}$ gilt ([Teil 5](/wissen/elektrotechnik/1-semester/hohere-mathematik-1/exponentialfunktion-und-stetigkeit/exponentialfunktion-und-stetigkeit.html))

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
