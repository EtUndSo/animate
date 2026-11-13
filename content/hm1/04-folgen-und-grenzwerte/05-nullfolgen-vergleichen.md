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

::::formelsammlung
**Vergleichskriterium**

$$|b_n|\le|a_n|\qquad\forall\,n\ge n_0$$

Mit festem $n_0\in\mathbb{N}$: Aus $\lim_{n\to\infty}a_n=0$ folgt $\lim_{n\to\infty}b_n=0$. $\{a_n\}$ heißt Majorante von $\{b_n\}$. Andersherum oder ohne Nullfolge $a_n$ folgt nichts.

**Rechnen mit Nullfolgen**

$$\{\alpha\,a_n+\beta\,b_n\},\qquad\{\sqrt{|a_n|}\},\qquad\{a_n\cdot c_n\}$$

Sind Nullfolgen, wenn $\{a_n\}$, $\{b_n\}$ Nullfolgen sind, $\alpha,\beta\in\mathbb{R}$ und $\{c_n\}$ beschränkt ist; jede Nullfolge ist beschränkt. Nullfolge mal beschränkt ist Nullfolge.

**Fakultät**

$$n!:=1\cdot2\cdot\ldots\cdot n,\qquad n!=(n-1)!\cdot n$$

Aus dem Vorgänger berechnet.

**Quadratisch fallend mal linear wachsend**

$$|a_n|\le\frac C{n^2}\qquad\text{und}\qquad|b_n|\le\tilde C\cdot n$$

Gilt das für alle $n\ge n_0$ mit Konstanten $C,\tilde C>0$, dann ist $\{a_n\cdot b_n\}$ eine Nullfolge, denn $|a_nb_n|\le C\tilde C\cdot\frac1n$. Mit $|a_n|\le C/n$ reicht es nicht.

**Drei wichtige Nullfolgen**

$$q^n,\qquad n\cdot q^n,\qquad\frac{x^n}{n!}$$

Für $|q|<1$ und jedes feste $x\in\mathbb{R}$; $q^n$ heißt geometrische Folge. Der Schritt von $n$ zu $n+1$ multipliziert $n\,q^n$ mit $q\,\frac{n+1}n$ und $x^n/n!$ mit $x/(n+1)$. Für $q=-1$ bleibt $|q^n|=1$, für $|q|>1$ wächst $|q^n|$ ohne Grenze.
::::

::::lernkarten
:::karte formel Vergleichskriterium
Was besagt das Vergleichskriterium für zwei Folgen $\{a_n\}$ und $\{b_n\}$, und ab welchem Index muss die Ungleichung gelten?
---
Gilt $|b_n|\le|a_n|$ für alle $n\ge n_0$ mit festem $n_0\in\mathbb{N}$, dann folgt aus $\lim_{n\to\infty}a_n=0$ auch $\lim_{n\to\infty}b_n=0$. Die Ungleichung muss erst ab $n_0$ gelten, weil endlich viele Glieder nie zählen.
--- falsch
Gilt $|b_n|\le|a_n|$ für alle $n\in\mathbb{N}$ ohne Ausnahme, dann folgt aus $\lim_{n\to\infty}a_n=0$ auch $\lim_{n\to\infty}b_n=0$. Schon ein einziges Glied mit $|b_n|>|a_n|$ macht das Kriterium unbrauchbar.
--- falsch
Gilt $|b_n|\ge|a_n|$ für alle $n\ge n_0$ mit festem $n_0\in\mathbb{N}$, dann folgt aus $\lim_{n\to\infty}a_n=0$ auch $\lim_{n\to\infty}b_n=0$, weil die größere Folge die kleinere in den Schlauch mitzieht.
--- falsch
Gilt $|b_n|\le|a_n|$ für alle $n\ge n_0$, dann folgt aus $\lim_{n\to\infty}b_n=0$ auch $\lim_{n\to\infty}a_n=0$: Liegt die kleinere Folge im Schlauch, liegt die größere wegen der Ungleichung ebenfalls darin.
:::
:::karte begriff Majorante
Wann heißt eine Folge $\{a_n\}$ eine Majorante der Folge $\{b_n\}$, und was folgt, wenn die Majorante eine Nullfolge ist?
---
Wenn $|b_n|\le|a_n|$ für alle $n\ge n_0$ mit einem festen $n_0\in\mathbb{N}$ gilt, $\{a_n\}$ also betragsmäßig über $\{b_n\}$ liegt. Ist die Majorante eine Nullfolge, ist es nach dem Vergleichskriterium auch $\{b_n\}$.
--- falsch
Wenn $|b_n|\le|a_n|$ für alle $n\ge n_0$ gilt. Ist $\{b_n\}$ eine Nullfolge, ist es nach dem Vergleichskriterium auch die Majorante $\{a_n\}$, weil sie von der kleineren Folge in den Schlauch mitgezogen wird.
--- falsch
Wenn $a_n\ge b_n$ für alle $n$ gilt, ohne Betrag: $\{a_n\}$ liegt also über $\{b_n\}$. Ist die Majorante eine Nullfolge, ist $\{b_n\}$ nach dem Vergleichskriterium ebenfalls eine, weil sie darunter liegt.
--- falsch
Wenn $\{a_n\}$ die kleinste Folge mit $|b_n|\le|a_n|$ ist, also unter allen solchen Folgen die untere Grenze bildet; jede Folge hat deshalb genau eine Majorante, so wie jede Menge höchstens ein Supremum.
:::
:::karte zusammenhang Voraussetzungen des Vergleichskriteriums
Warum folgt aus dem Vergleich nichts, wenn die größere Folge keine Nullfolge ist oder die Ungleichung andersherum gilt?
---
Weil es dann Gegenbeispiele gibt: Für $a_n=b_n=1$ gilt $|b_n|\le|a_n|$, aber $a_n$ ist keine Nullfolge und $b_n$ auch nicht. Für $a_n=\frac1n$ und $b_n=1$ gilt $|b_n|\ge|a_n|$ mit der Nullfolge $a_n$, doch $b_n$ ist keine.
--- falsch
Doch, es folgt etwas: Ist die größere Folge keine Nullfolge, ist es die kleinere auch nicht, denn eine Majorante überträgt Konvergenz und Divergenz gleichermaßen auf die Folge darunter, in beide Richtungen.
--- falsch
Weil das Kriterium nur für positive Folgen gilt: Andersherum oder ohne Nullfolge können negative Glieder entstehen, und dann sagt der Betrag nichts mehr darüber aus, ob ein Glied im Schlauch liegt.
--- falsch
Weil die Ungleichung dann erst ab einem Index $n_0$ gilt und die Glieder davor das Ergebnis verfälschen können: Erst eine Ungleichung für alle $n\in\mathbb{N}$ ohne Ausnahme würde in diesen Fällen etwas liefern.
:::
:::karte zusammenhang Differenz zweier Wurzeln
Wie zeigt man, dass $b_n=\sqrt{n+4}-\sqrt n$ eine Nullfolge ist, ohne die Bedingung $|b_n|<\varepsilon$ nach $n$ aufzulösen?
---
Man erweitert mit der Summe der Wurzeln (dritte binomische Formel): $0<b_n=\frac{(n+4)-n}{\sqrt{n+4}+\sqrt n}\le\frac4{2\sqrt n}=\frac2{\sqrt n}$. Damit ist die bekannte Nullfolge $2/\sqrt n$ eine Majorante.
--- falsch
Man rechnet $\sqrt{n+4}-\sqrt n=\sqrt{(n+4)-n}=\sqrt4=2$, weil die Wurzel einer Differenz die Differenz der Wurzeln ist. Damit ist $b_n$ konstant 2 und gar keine Nullfolge.
--- falsch
Beide Terme sind unbeschränkt, ihre Differenz ist also „unendlich minus unendlich“, und das ist 0. Eine Majorante braucht man nicht, weil sich zwei gleich schnell wachsende Terme aufheben.
--- falsch
Man erweitert mit der Summe der Wurzeln: $b_n=\frac{(n+4)-n}{\sqrt{n+4}+\sqrt n}\ge\frac4{2\sqrt n}=\frac2{\sqrt n}$. Damit liegt $b_n$ über einer Nullfolge und ist nach dem Vergleichskriterium selbst eine.
:::
:::karte formel Rechnen mit Nullfolgen
Welche vier Regeln gelten für zwei Nullfolgen $\{a_n\}$, $\{b_n\}$ und eine beschränkte Folge $\{c_n\}$?
---
(i) $\{\alpha\,a_n+\beta\,b_n\}$ ist eine Nullfolge für alle $\alpha,\beta\in\mathbb{R}$; (ii) $\{\sqrt{|a_n|}\}$ ist eine Nullfolge; (iii) $\{a_n\}$ ist beschränkt; (iv) $\{a_n\cdot c_n\}$ ist eine Nullfolge.
--- falsch
(i) $\{\alpha\,a_n+\beta\,b_n\}$ ist eine Nullfolge nur für $|\alpha|,|\beta|\le1$; (ii) $\{\sqrt{|a_n|}\}$ ist eine Nullfolge; (iii) $\{a_n\}$ ist beschränkt; (iv) $\{a_n\cdot c_n\}$ ist eine Nullfolge.
--- falsch
(i) $\{\alpha\,a_n+\beta\,b_n\}$ ist eine Nullfolge für alle $\alpha,\beta\in\mathbb{R}$; (ii) $\{\sqrt{|a_n|}\}$ ist keine, weil Wurzeln kleine Zahlen vergrößern; (iii) $\{a_n\}$ ist beschränkt; (iv) $\{a_n\cdot c_n\}$ ist eine Nullfolge.
--- falsch
(i) $\{\alpha\,a_n+\beta\,b_n\}$ ist eine Nullfolge für alle $\alpha,\beta\in\mathbb{R}$; (ii) $\{\sqrt{|a_n|}\}$ ist eine Nullfolge; (iii) $\{a_n\}$ ist monoton fallend; (iv) $\{a_n\cdot c_n\}$ ist es für jede Folge $\{c_n\}$.
:::
:::karte zusammenhang Nullfolge mal beschränkt
Warum ist das Produkt einer Nullfolge mit einer beschränkten Folge wieder eine Nullfolge, und warum darf die Beschränktheit nicht fehlen?
---
Mit $|c_n|\le M$ ist $|a_nc_n|\le M|a_n|$, und $M|a_n|$ ist eine Nullfolge, also nach dem Vergleichskriterium eine Majorante. Ohne Schranke geht es schief: Für die unbeschränkte Folge $c_n=n$ und $a_n=\frac1n$ ist $a_nc_n=1$.
--- falsch
Weil jedes Produkt mit einem Faktor, der gegen 0 geht, selbst gegen 0 geht; die Beschränktheit ist nur bequem. Auch für $c_n=n$ und $a_n=\frac1n$ geht $a_nc_n$ deshalb gegen 0.
--- falsch
Weil eine beschränkte Folge selbst eine Nullfolge ist und das Produkt zweier Nullfolgen wieder eine ergibt. Ohne Schranke wäre $c_n$ divergent, und dann divergiert jedes Produkt mit $c_n$.
--- falsch
Mit $|c_n|\le M$ ist $|a_nc_n|\le M+|a_n|$, und das ist eine Nullfolge, also eine Majorante. Ohne Schranke fehlt die Zahl $M$, und $a_nc_n$ ist dann nie eine Nullfolge.
:::
:::karte zusammenhang Nullfolgen sind beschränkt
Warum ist jede Nullfolge beschränkt, obwohl ihre ersten Glieder beliebig groß sein dürfen?
---
Zu $\varepsilon=1$ gibt es $N_0$ mit $|a_n|<1$ für $n>N_0$. Davor stehen nur endlich viele Glieder, deren Maximum existiert: Mit $M:=\max\{|a_1|,\dots,|a_{N_0}|,1\}$ gilt $|a_n|\le M$ für alle $n$.
--- falsch
Weil jede Nullfolge monoton fällt: Ihr erstes Glied ist deshalb eine obere Schranke, $|a_n|\le|a_1|$ für alle $n$, und 0 ist eine untere Schranke, weil die Glieder gegen 0 fallen.
--- falsch
Zu $\varepsilon=1$ gibt es $N_0$ mit $|a_n|<1$ für $n>N_0$; damit ist 1 eine Schranke für alle Glieder, denn die Glieder vor $N_0$ zählen bei Folgen nie, auch nicht bei Schranken.
--- falsch
Weil die Glieder gegen 0 gehen und deshalb ihr Supremum 0 ist; jede Folge mit einem Supremum ist beschränkt, und das Vollständigkeitsaxiom garantiert, dass es existiert.
:::
:::karte zusammenhang Fakultät
Warum ist $\frac{x^n}{n!}$ für jedes feste $x\in\mathbb{R}$ eine Nullfolge, obwohl $x^n$ ohne Grenze wachsen kann?
---
Weil die Fakultät $n!=(n-1)!\cdot n$ in jedem Schritt mit dem wachsenden Faktor $n$ multipliziert: Der Schritt zum nächsten Glied multipliziert mit $x/(n+1)$, und das wird beliebig klein.
--- falsch
Weil $n!$ schneller wächst als $x^n$, solange $|x|<1$ ist; für $|x|\ge1$ wächst $x^n$ mit, und $\frac{x^n}{n!}$ ist dann keine Nullfolge, sondern bleibt nur beschränkt, weil beide gleich schnell wachsen.
--- falsch
Weil der Schritt von einem Glied zum nächsten mit $x/n!$ multipliziert, und $n!$ ist schon ab $n=4$ größer als jede feste Zahl $x$; deshalb fällt die Folge vom ersten Glied an gegen 0.
--- falsch
Weil die Fakultät $n!=n^n$ ist und $n^n$ für $n>|x|$ größer als $|x|^n$ wird; der Bruch $(x/n)^n$ ist dann eine geometrische Folge mit festem $q<1$ und damit eine Nullfolge.
:::
:::karte formel Quadratisch fallend mal linear wachsend
Unter welchen Bedingungen an $|a_n|$ und $|b_n|$ ist das Produkt $\{a_n\cdot b_n\}$ eine Nullfolge, wenn $b_n$ linear wachsen darf?
---
Gilt für alle $n\ge n_0$ $|a_n|\le\frac C{n^2}$ und $|b_n|\le\tilde C\cdot n$ mit Konstanten $C,\tilde C>0$, dann ist $\{a_n\cdot b_n\}$ eine Nullfolge, denn $|a_nb_n|\le C\tilde C\cdot\frac1n$. Mit $|a_n|\le C/n$ reicht es nicht: $\frac1n\cdot n=1$.
--- falsch
Gilt für alle $n\ge n_0$ $|a_n|\le\frac Cn$ und $|b_n|\le\tilde C\cdot n$ mit Konstanten $C,\tilde C>0$, dann ist $\{a_n\cdot b_n\}$ eine Nullfolge, denn der Abfall $\frac1n$ hebt den Anstieg $n$ auf.
--- falsch
Gilt für alle $n\ge n_0$ $|a_n|\le\frac C{n^2}$ und $|b_n|\le\tilde C\cdot n^2$ mit Konstanten $C,\tilde C>0$, dann ist $\{a_n\cdot b_n\}$ eine Nullfolge, denn der quadratische Abfall schlägt auch einen quadratischen Anstieg.
--- falsch
Gilt $|a_n|\le\frac C{n^2}$ und $|b_n|\le\tilde C\cdot n$ für alle $n\in\mathbb{N}$ ohne Ausnahme, dann ist $\{a_n\cdot b_n\}$ eine Nullfolge; gelten die Abschätzungen erst ab einem $n_0$, folgt nichts.
:::
:::karte formel Drei wichtige Nullfolgen
Welche drei Folgen sind für $|q|<1$ und jedes feste $x\in\mathbb{R}$ Nullfolgen, und was schlägt dabei was?
---
Die geometrische Folge $q^n$, die Folge $n\cdot q^n$ und $\frac{x^n}{n!}$. Exponentieller Abfall schlägt den linearen Anstieg, die Fakultät schlägt jede Potenz.
--- falsch
Die geometrische Folge $q^n$, die Folge $n\cdot q^n$ und $\frac{x^n}{n!}$, letztere aber nur für $|x|<1$, weil eine Potenz mit $|x|\ge1$ jede Fakultät schlägt.
--- falsch
Die geometrische Folge $q^n$ und $\frac{x^n}{n!}$, nicht aber $n\cdot q^n$: Der lineare Anstieg schlägt den exponentiellen Abfall, weil $n$ über alle Grenzen wächst.
--- falsch
Die geometrische Folge $q^n$, die Folge $n\cdot q^n$ und $\frac{n!}{x^n}$. Exponentieller Abfall schlägt den linearen Anstieg, die Potenz schlägt die Fakultät.
:::
:::karte begriff geometrische Folge
Was ist die geometrische Folge, und für welche $q$ ist sie eine Nullfolge?
---
Die Folge der Potenzen $q^n$ einer festen Zahl $q\in\mathbb{R}$. Sie ist eine Nullfolge für $|q|<1$; für $q=-1$ bleibt $|q^n|=1$, für $|q|>1$ wächst $|q^n|$ ohne Grenze.
--- falsch
Die Folge der Summen $1+q+\dots+q^n$ einer festen Zahl $q\in\mathbb{R}$. Sie ist eine Nullfolge für $|q|<1$, weil die Summanden dann immer kleiner werden und schließlich verschwinden.
--- falsch
Die Folge der Potenzen $q^n$ einer festen Zahl $q\in\mathbb{R}$. Sie ist eine Nullfolge für $|q|\le1$, auch für $q=-1$, weil sich die Glieder $-1$ und $1$ im Mittel gegenseitig aufheben.
--- falsch
Die Folge der Potenzen $q^n$ einer festen Zahl $q\in\mathbb{R}$. Sie ist eine Nullfolge nur für $0<q<1$; für negative $q$ springt das Vorzeichen, und eine springende Folge hat keinen Grenzwert.
:::
:::karte herleitung geometrische Folge ist Nullfolge
Wie zeigt man mit der Bernoulli-Ungleichung, dass die geometrische Folge $q^n$ für $0<|q|<1$ eine Nullfolge ist?
---
Setze $k:=\frac1{|q|}-1$; dann ist $k>0$, weil $|q|<1$ ist, und $\frac1{|q|}=1+k$.
---
Bernoulli gibt $\frac1{|q|^n}=(1+k)^n\ge1+nk>nk$, weil $k>-1$ ist und $1>0$.
---
Daraus folgt $|q^n|<\frac1k\cdot\frac1n$, weil beim Übergang zu den Kehrwerten positiver Zahlen die Ungleichung umkehrt.
---
Rechts steht eine Nullfolge, weil $\frac1n$ eine ist und der feste Faktor $\frac1k$ daran nichts ändert. Sie ist eine Majorante, und das Vergleichskriterium gibt $q^n\to0$.
:::
:::karte herleitung Fakultät schlägt Potenz
Wie zeigt man, dass $\frac{x^n}{n!}$ für jedes feste $x\in\mathbb{R}$ eine Nullfolge ist?
---
Wähle $m\in\mathbb{N}$ mit $m\ge2|x|$; dann ist $|x/j|<\frac12$ für jedes $j>m$, weil $j$ dann größer als $2|x|$ ist.
---
Für $n>m$ zerlegt man $\bigl|\frac{x^n}{n!}\bigr|$ in $C:=\bigl|\frac x1\cdot\frac x2\cdot\ldots\cdot\frac xm\bigr|$ und die Faktoren $\bigl|\frac x{m+1}\bigr|,\dots,\bigl|\frac xn\bigr|$, weil $\frac{x^n}{n!}$ das Produkt der Brüche $\frac xj$ für $j=1,\dots,n$ ist.
---
Es folgt $\bigl|\frac{x^n}{n!}\bigr|\le C\bigl(\frac12\bigr)^{n-m}=C\,2^m\bigl(\frac12\bigr)^n$, weil jeder der $n-m$ hinteren Faktoren kleiner als $\frac12$ ist.
---
Die Zahl $C\,2^m$ hängt nur von $x$ ab, nicht von $n$; die rechte Seite ist deshalb ein festes Vielfaches der Nullfolge $(\frac12)^n$, also eine Majorante, weil Vielfache von Nullfolgen Nullfolgen sind.
:::
:::karte zusammenhang Anstieg oder Abfall
Warum ist $n\cdot q^n$ für $|q|<1$ eine Nullfolge, obwohl die Glieder, etwa bei $n\cdot0{,}8^n$, zuerst steigen?
---
Der Schritt von $n$ zu $n+1$ multipliziert das Glied mit $q\,\frac{n+1}n$. Der Bruch geht gegen 1, ab einer Stelle ist der Faktor also betragsmäßig unter 1 und bleibt dort. Der Anfang zählt nicht: $n\cdot0{,}8^n$ steigt bis $1{,}638$ bei $n=4$ und 5 und fällt danach.
--- falsch
Der Schritt von $n$ zu $n+1$ multipliziert das Glied mit $q+\frac1n$. Das ist anfangs größer als 1 und wird erst für $n>\frac1{1-q}$ kleiner als 1; ab dort fällt die Folge, und der Anfang zählt nicht, weil endlich viele Glieder nie zählen.
--- falsch
Weil der Faktor $n$ nach endlich vielen Schritten aufhört, merklich zu wachsen: Für große $n$ ist $n$ praktisch konstant, und übrig bleibt die geometrische Folge $q^n$, die gegen 0 geht. Der Anstieg am Anfang kommt nur vom Faktor $n$.
--- falsch
Weil $n\cdot q^n\le q^n$ für alle $n$ gilt, sobald $|q|<1$ ist: Der Faktor $n$ wird durch die Potenz mehr als aufgefangen, und $q^n$ ist eine Majorante. Das scheinbare Steigen am Anfang ist nur ein Rundungseffekt beim Rechnen.
:::
::::
