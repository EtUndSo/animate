---
title: Stufe 3: Nullfolgen vergleichen
pfad: Elektrotechnik / 1. Semester / HöMa1 – Höhere Mathematik 1 / Folgen und Grenzwerte
adresse: elektrotechnik/1-semester/hohere-mathematik-1/folgen-und-grenzwerte
knoten: Kapitel 4: Folgen und Grenzwerte
order: 1240500
summary: Bei sqrt n+4 -sqrt n steht n unter zwei Wurzeln, Auflösen nach n ist mühsam.
tags: Majorante, Fakultät, geometrische Folge
lang: de
---

<span class="anker" id="stufe-3"></span>

:::zweck
Bei $\sqrt{n+4}-\sqrt n$ steht $n$ unter zwei Wurzeln, Auflösen nach $n$ ist mühsam. Diese Stufe gewinnt das Spiel ohne Auflösen: durch Vergleich mit einer bekannten Nullfolge.
:::

**Die Idee.** Liegt eine Folge im Schlauch und eine zweite betragsmäßig darunter, liegt die zweite erst recht im Schlauch. Dasselbe $N_0$ gewinnt für beide (Abb. [3](#abb-3)).

:::satz Satz 3.1 (Vergleichskriterium)
<span class="anker" id="satz-3-1"></span>

Sei $n_0\in\mathbb{N}$ fest, und seien $\{a_n\}$, $\{b_n\}$ Zahlenfolgen mit

<span class="anker" id="gl-3-1"></span>
$$|b_n|\le|a_n|\qquad\forall\,n\ge n_0. \tag{3.1}$$

Dann gilt: Aus $\lim_{n\to\infty}a_n=0$ folgt $\lim_{n\to\infty}b_n=0$. Die Folge $\{a_n\}$ heißt dann __Majorante__ von $\{b_n\}$.
:::

⁠**So liest man das:** Die Ungleichung muss nicht von Anfang an gelten, ab $n_0$ genügt: Endlich viele Glieder zählen nie. **Voraussetzung nötig:** Ist $\{a_n\}$ keine Nullfolge, folgt nichts ($a_n=b_n=1$). Andersherum ($|b_n|\ge|a_n|$) folgt ebenfalls nichts ($a_n=\frac1n$, $b_n=1$).

:::beweis Dasselbe $N_0$, nur später
Sei $\varepsilon>0$. Da $\{a_n\}$ Nullfolge ist, gibt es $N_0(\varepsilon)$ mit $|a_n|<\varepsilon$ für alle $n>N_0$. Wähle $\tilde N_0:=\max\{N_0,n_0\}$. Für $n>\tilde N_0$ gelten beide Aussagen, also $|b_n|\le|a_n|<\varepsilon$.
:::

::::beispiel
Die Differenz $b_n=\sqrt{n+4}-\sqrt n$ besteht aus zwei unbeschränkten Termen. Erweitern mit der Summe der Wurzeln beseitigt sie (dritte binomische Formel):

$$0<b_n=\frac{(\sqrt{n+4}-\sqrt n)(\sqrt{n+4}+\sqrt n)}{\sqrt{n+4}+\sqrt n}=\frac{(n+4)-n}{\sqrt{n+4}+\sqrt n}\le\frac4{2\sqrt n}=\frac2{\sqrt n}.$$

Also ist $2/\sqrt n$ aus Stufe [2](das-epsilon-spiel.html#stufe-2) eine Majorante, und $\{b_n\}$ ist Nullfolge. Für $n=100$ ist $b_n=0{,}198$ und die Majorante $0{,}2$. Bei $\varepsilon=0{,}5$ gewinnt das $N_0=16$ der Majorante auch für $b_n$. Das kleinste wäre 14, denn $b_{14}=0{,}501$ und $b_{15}=0{,}486$.
::::

:::abbildung hm1/k4majorante 3
Die Folge $b_n=\sqrt{n+4}-\sqrt n$ (blau) liegt unter ihrer Majorante $2/\sqrt n$ (orange). Sobald die Majorante im Schlauch $\varepsilon=0{,}5$ bleibt, also für $n>16$, bleibt es $b_n$ auch.
:::

**Rechnen mit Nullfolgen.** Aus bekannten Nullfolgen entstehen neue.

:::satz Satz 3.2 (Rechnen mit Nullfolgen)
<span class="anker" id="satz-3-2"></span>

Seien $\{a_n\}$ und $\{b_n\}$ Nullfolgen und $\{c_n\}$ eine beschränkte Folge. Dann gilt:

<ol class="rm">

<li>

$\{\alpha\,a_n+\beta\,b_n\}$ ist eine Nullfolge für alle $\alpha,\beta\in\mathbb{R}$.

</li>

<li>

$\{\sqrt{|a_n|}\}$ ist eine Nullfolge.

</li>

<li>

$\{a_n\}$ ist beschränkt.

</li>

<li>

$\{a_n\cdot c_n\}$ ist eine Nullfolge.

</li>

</ol>
:::

⁠**So liest man das:** Die Regel (iv) sagt: Nullfolge mal beschränkt ist Nullfolge. Die Abweichung ist so gebaut: $d_n=(-1)^n\cdot\frac3n$, das Vorzeichen stört nicht. Die Regel (i) macht aus $\frac1n$ und $\frac2{\sqrt n}$ zum Beispiel $\frac6n-\frac5{\sqrt n}$. **Voraussetzung nötig:** Für unbeschränktes $c_n=n$ und $a_n=\frac1n$ ist $a_nc_n=1$, keine Nullfolge.

:::beweis Rechnen mit Nullfolgen
(i) Sei $\varepsilon>0$ und $M:=|\alpha|+|\beta|+1>0$. Zu $\varepsilon/M$ gibt es $N_1$ mit $|a_n|<\varepsilon/M$ für $n>N_1$ und $N_2$ mit $|b_n|<\varepsilon/M$ für $n>N_2$. Für $n>\max\{N_1,N_2\}$ folgt mit der Dreiecksungleichung $|\alpha a_n+\beta b_n|\le(|\alpha|+|\beta|)\,\varepsilon/M<\varepsilon$.

(ii) Sei $\varepsilon>0$. Zu $\tilde\varepsilon:=\varepsilon^2>0$ gibt es $\tilde N_0$ mit $|a_n|<\varepsilon^2$ für $n>\tilde N_0$. Weil die Wurzel streng monoton wächst, folgt $\sqrt{|a_n|}<\varepsilon$. Also gewinnt $N_0:=\tilde N_0$.

(iii) Zu $\varepsilon=1$ gibt es $N_0$ mit $|a_n|<1$ für $n>N_0$. Für die endlich vielen Glieder davor nimmt man das Maximum: Mit $M:=\max\{|a_1|,\dots,|a_{N_0}|,1\}$ gilt $|a_n|\le M$ für alle $n$.

(iv) Es gibt $M>0$ mit $|c_n|\le M$. Dann ist $|a_nc_n|\le M|a_n|$, und $M|a_n|$ ist nach (i) eine Nullfolge (mit $\beta=0$; dass $|a_n|$ selbst Nullfolge ist, zeigt [(2.1)](das-epsilon-spiel.html#gl-2-1) direkt). Das Vergleichskriterium liefert die Behauptung.
:::

**Wer gewinnt, Anstieg oder Abfall?** In $n\,q^n$ wächst der eine Faktor, der andere schrumpft. Der Schritt von $n$ zu $n+1$ multipliziert das Glied mit $q\,\frac{n+1}n$. Der Bruch geht gegen 1, ab einer Stelle ist der ganze Faktor also unter 1 und bleibt dort. Ebenso multipliziert der Schritt in $x^n/n!$ mit $x/(n+1)$, und das wird beliebig klein (Abb. [4](#abb-4)). Dabei ist $n!:=1\cdot2\cdot\ldots\cdot n$ die __Fakultät__, aus dem Vorgänger berechnet $n!=(n-1)!\cdot n$, zum Beispiel $4!=24$. Das Werkzeug dazu:

:::satz Satz 3.3 (Quadratisch fallend mal linear wachsend)
<span class="anker" id="satz-3-3"></span>

Seien $C,\tilde C>0$ Konstanten und $n_0\in\mathbb{N}$ fest. Gilt für alle $n\ge n_0$

<span class="anker" id="gl-3-2"></span>
$$|a_n|\le\frac C{n^2}\qquad\text{und}\qquad|b_n|\le\tilde C\cdot n, \tag{3.2}$$

dann ist $\{a_n\cdot b_n\}$ eine Nullfolge.
:::

⁠**So liest man das:** Der Anstieg von $b_n$ zehrt vom Abfall von $a_n$ eine Potenz von $n$ auf, eine bleibt übrig. Mit $|a_n|\le C/n$ reicht es nicht: $\frac1n\cdot n=1$. Beweis: $|a_nb_n|\le C\tilde C\cdot\frac1n$ für $n\ge n_0$, und rechts steht eine Nullfolge, also eine Majorante.

:::satz Satz 3.4 (Drei wichtige Nullfolgen)
<span class="anker" id="satz-3-4"></span>

Für $|q|<1$ und jedes feste $x\in\mathbb{R}$ sind Nullfolgen: (i) die __geometrische Folge__ $q^n$, (ii) $n\cdot q^n$, (iii) $\dfrac{x^n}{n!}$.
:::

⁠**So liest man das:** Exponentieller Abfall schlägt den linearen Anstieg, die Fakultät schlägt jede Potenz. **Voraussetzung nötig:** Für $q=-1$ bleibt $|q^n|=1$, für $|q|>1$ wächst $|q^n|$ ohne Grenze.

:::beweis Drei Nullfolgen, drei Majoranten
Für $q=0$ gelten (i) und (ii) sofort. Sei also $0<|q|<1$.

(i) Setze $k:=\frac1{|q|}-1>0$, also $\frac1{|q|}=1+k$. Bernoulli gibt $\frac1{|q|^n}=(1+k)^n\ge1+nk>nk$, also $|q^n|<\frac1k\cdot\frac1n$. Das ist eine Majorante.

(ii) Wegen $0<\sqrt{|q|}<1$ ist $k:=\frac1{\sqrt{|q|}}-1>0$, also $\sqrt{|q|}=\frac1{1+k}$. Wie in (i) ist $(1+k)^n>kn$, also

$$|q^n|=\bigl(\sqrt{|q|}\bigr)^n\cdot\bigl(\sqrt{|q|}\bigr)^n=\frac1{(1+k)^n}\cdot\frac1{(1+k)^n}<\frac1{kn}\cdot\frac1{kn}=\frac1{k^2}\cdot\frac1{n^2}.$$

Mit $a_n=q^n$, $C=1/k^2$, $b_n=n$, $\tilde C=1$ gilt [(3.2)](#gl-3-2).

(iii) Wähle $m\in\mathbb{N}$ mit $m\ge2|x|$. Für jedes $j>m$ ist dann $|x/j|<\frac12$. Für $n>m$ zerlegt man

$$\Bigl|\frac{x^n}{n!}\Bigr|=\underbrace{\Bigl|\frac x1\cdot\frac x2\cdot\ldots\cdot\frac xm\Bigr|}_{=:C}\cdot\Bigl|\frac x{m+1}\Bigr|\cdot\ldots\cdot\Bigl|\frac xn\Bigr|\le C\Bigl(\frac12\Bigr)^{n-m}=C\,2^m\Bigl(\frac12\Bigr)^n.$$

Die Zahl $C\,2^m$ hängt nur von $x$ ab, nicht von $n$. Nach (i) und Satz [3.2](#satz-3-2) (i) ist die rechte Seite eine Nullfolge, also eine Majorante.
:::

::::beispiel
Für $q=0{,}8$ ist in (i) $k=0{,}25$, also $0{,}8^n<4/n$. In (ii) ist $k=0{,}118$ und $C\approx72$. Das Glied $n\cdot0{,}8^n$ steigt bis $1{,}638$ bei $n=4$ und $5$, bei $n=50$ ist es noch $0{,}0007$. Die Folge $4^n/n!$ steigt bis $10{,}67$ bei $n=3$ und $4$, bei $n=20$ ist sie $4{,}5\cdot10^{-7}$.
::::

⁠**Grenzfall:** Für $q\to1$ wächst $C=1/k^2$ über alle Grenzen. Der Abfall setzt immer später ein, und $q=1$ ergibt die unbeschränkte Folge $n$.

:::abbildung hm1/k4tempo 4
Links $n\cdot0{,}8^n$, rechts $4^n/n!$. Beide steigen zuerst, weil der Faktor von einem Glied zum nächsten größer als 1 ist. Rechts der gestrichelten Linie bleibt er unter 1, und die Folge fällt gegen 0.
:::

:::frage $n\cdot0{,}8^n$ steigt am Anfang. Wie kann das eine Nullfolge sein?
Der Anfang zählt nicht. Das Kriterium fragt nur nach den Gliedern hinter $N_0$, und ab $n=5$ fällt die Folge unter jede Toleranz.
:::

:::aufgabe Aufgabe 4 ★★ Majorante finden
<span class="anker" id="aufg-4"></span>

Zeige mit dem Trick des Beispiels, dass $e_n=\sqrt{n+9}-\sqrt n$ eine Nullfolge ist. Gib eine Majorante der Form $C/\sqrt n$ an und daraus ein $N_0$ für $\varepsilon=0{,}05$.

:::loesung
Erweitern ergibt $e_n=\dfrac9{\sqrt{n+9}+\sqrt n}\le\dfrac9{2\sqrt n}=\dfrac{4{,}5}{\sqrt n}$. Das ist nach Satz [3.2](#satz-3-2) (i) eine Nullfolge, denn $2/\sqrt n$ ist eine. Für $\varepsilon=0{,}05$: $4{,}5/\sqrt n<0{,}05\iff\sqrt n>90\iff n>8100$. Also gewinnt $N_0=8100$.
:::
:::

:::aufgabe Aufgabe 5 ★★ Wann kippt die Folge?
<span class="anker" id="aufg-5"></span>

(a) Für welches $n$ ist $n\cdot0{,}9^n$ am größten? Nutze den Faktor $q\,\frac{n+1}n$. (b) Ab welchem Index ist die Folge dauerhaft kleiner als $0{,}1$? Rechne mit einem Taschenrechner. (c) Für welches $n$ ist $5^n/n!$ am größten? Warum liegt das Maximum nahe bei $x=5$?

:::loesung
(a) Der Faktor $0{,}9\,\frac{n+1}n$ ist größer als 1 für $n<9$ und genau 1 für $n=9$. Das Maximum liegt bei $n=9$ und $n=10$, beide Glieder sind $3{,}487$. (b) Hinter dem Maximum fällt die Folge. $60\cdot0{,}9^{60}=0{,}108$ und $61\cdot0{,}9^{61}=0{,}099$: Ab $n=61$ bleibt sie unter $0{,}1$. (c) Der Faktor $5/(n+1)$ ist mindestens 1 für $n\le4$, genau 1 für $n=4$. Das Maximum $26{,}04$ liegt bei $n=4$ und $n=5$. Allgemein ist der Faktor $x/(n+1)$ größer als 1, solange $n+1<x$ ist, deshalb liegt das Maximum bei $n\approx x$.
:::
:::
