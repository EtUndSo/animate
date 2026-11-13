---
title: Stufe 2: Nullfolge nötig, aber nicht genug
pfad: Elektrotechnik / 1. Semester / HöMa1 – Höhere Mathematik 1 / Unendliche Reihen
adresse: elektrotechnik/1-semester/hohere-mathematik-1/unendliche-reihen
knoten: Kapitel 6: Unendliche Reihen
order: 1260400
summary: Eine Formel für S N gibt es selten.
tags: 
lang: de
---

<span class="anker" id="stufe-2"></span>

:::zweck
Eine Formel für $S_N$ gibt es selten. Diese Stufe überträgt das Cauchy-Kriterium auf Reihen, gewinnt daraus eine notwendige Bedingung und zeigt an der harmonischen Reihe, warum sie nicht genügt.
:::

**Die Idee.** Hat eine Treppe eine Grenzhöhe, kommt weit oben kaum noch etwas hinzu: Jedes Teilstück ab einer gewissen Stelle ist niedrig, egal wie lang. Das kürzeste Teilstück ist eine einzelne Stufe, also müssen die Stufen gegen 0 gehen. Das Umgekehrte gilt nicht: Viele niedrige Stufen können zusammen hoch sein.

:::satz Satz 2.1 (Cauchy-Kriterium für Reihen)
<span class="anker" id="satz-2-1"></span>

Die Reihe $\sum_{n=1}^\infty a_n$ konvergiert genau dann, wenn

<span class="anker" id="gl-2-1"></span>
$$\forall\,\varepsilon>0\quad\exists\,N_0=N_0(\varepsilon)\in\mathbb{N}:\quad\Bigl|\sum_{\ell=m+1}^na_\ell\Bigr|<\varepsilon\quad\forall\,n>m>N_0. \tag{2.1}$$
:::

⁠**So liest man das:** Die Summe im Betrag ist das Treppenstück von Stufe $m+1$ bis Stufe $n$, also $S_n-S_m$. Hinter $N_0$ ist jedes Stück niedriger als $\varepsilon$, auch ein sehr langes. Bei der Halbierungsreihe ist jedes Stück hinter $m$ kleiner als $(\frac12)^m$, für $\varepsilon=0{,}1$ genügt also $N_0=3$. Der Grenzwert kommt nicht vor, deshalb lässt sich das Kriterium prüfen, ohne $S$ zu kennen.

:::beweis Cauchy-Folge der Teilsummen
Für $n>m$ ist $S_n-S_m=\sum_{\ell=m+1}^na_\ell$. Bedingung [(2.1)](#gl-2-1) sagt also, dass $\{S_N\}$ eine Cauchy-Folge ist (für $n=m$ ist der Abstand 0, Vertauschen ändert den Betrag nicht). In $\mathbb{R}$ ist das nach [Kapitel 4](/wissen/elektrotechnik/1-semester/hohere-mathematik-1/folgen-und-grenzwerte/folgen-und-grenzwerte.html) gleichbedeutend mit Konvergenz.
:::

:::satz Satz 2.2 (Notwendige Bedingung)
<span class="anker" id="satz-2-2"></span>

Konvergiert $\sum_{n=1}^\infty a_n$, dann gilt $\lim_{n\to\infty}a_n=0$.
:::

⁠**So liest man das:** Ist $\{a_n\}$ keine Nullfolge, muss die Reihe divergieren. Das ist die Kontraposition und der billigste Test überhaupt. Die Bedingung ist nur notwendig, nicht hinreichend: Aus $a_n\to0$ folgt keine Konvergenz.

::::beispiel [Beispiele]
Für $|q|\ge1$ ist $|q^n|\ge1$, also divergiert die geometrische Reihe. Bei $\sum\frac n{2n+1}$ streben die Glieder gegen $\frac12$, also divergiert auch sie.
::::

:::beweis Ein Stück aus einer Stufe
Wähle in [(2.1)](#gl-2-1) $n=m+1$. Das ergibt $|a_{m+1}|<\varepsilon$ für alle $m>N_0$, also ist $\{a_n\}$ nach dem Epsilon-Kriterium eine Nullfolge.
:::

:::satz Satz 2.3 (Harmonische Reihe)
<span class="anker" id="satz-2-3"></span>

Die Glieder $\frac1n$ bilden eine Nullfolge, aber die harmonische Reihe $\sum_{n=1}^\infty\frac1n$ divergiert. Für alle $m\in\mathbb{N}$ gilt

<span class="anker" id="gl-2-2"></span>
$$H_{2^m}\ge1+\frac m2. \tag{2.2}$$
:::

⁠**So liest man das:** $H_{2^m}$ ist die Teilsumme nach $2^m$ Gliedern, für $m=4$ also $H_{16}=3{,}381\ge3$. Jede Verdopplung von $N$ bringt mindestens $\frac12$.

:::beweis Gruppen, die je mindestens $\frac12$ ergeben
Fasse die Glieder zu Gruppen mit $1,2,4,8,\dots$ Gliedern zusammen:

$$H_{2^m}=1+\frac12+\Bigl(\frac13+\frac14\Bigr)+\Bigl(\frac15+\dots+\frac18\Bigr)+\dots+\Bigl(\frac1{2^{m-1}+1}+\dots+\frac1{2^m}\Bigr).$$

Gruppe $j$ endet bei $\frac1{2^j}$ und hat $2^{j-1}$ Glieder. Jedes davon ist mindestens so groß wie das letzte, also ist die Gruppe mindestens $2^{j-1}\cdot\frac1{2^j}=\frac12$. Mit $m$ Gruppen folgt [(2.2)](#gl-2-2). Damit ist $\{H_N\}$ unbeschränkt, und eine unbeschränkte Folge konvergiert nicht ([Kapitel 4](/wissen/elektrotechnik/1-semester/hohere-mathematik-1/folgen-und-grenzwerte/folgen-und-grenzwerte.html)).
:::

⁠**Der Mechanismus:** Von Gruppe zu Gruppe halbiert sich die Höhe der Glieder, ihre Anzahl verdoppelt sich, das Produkt bleibt (Abb. [2](#abb-2)). Die Glieder schrumpfen gerade zu langsam gegen ihre wachsende Zahl. Das verletzt das Cauchy-Kriterium: Das Stück von $m+1$ bis $2m$ hat $m$ Glieder, jedes mindestens $\frac1{2m}$, also ist es mindestens $\frac12$, egal wie groß $m$ ist.

:::abbildung hm1/k6harmonisch 2
Die Glieder $\frac1n$ als Balken. Die Gruppen mit 1, 2, 4 und 8 Gliedern liegen über den gestrichelten Linien, also ist jede mindestens $\frac12$. Die Treppe bekommt damit unbegrenzt oft $\frac12$ dazu.
:::

**Zahlen.** $H_{1024}=7{,}509$ (Schranke 6), $H_{10^6}=14{,}39$. Die 5 überschreitet $H_N$ erst bei $N=83$, die 10 erst bei $N=12367$. Numerisch sieht das nach einer Decke aus, nur der Beweis zeigt, dass es keine gibt. **Grenzfall:** Für $m=1$ gilt in [(2.2)](#gl-2-2) Gleichheit, $H_2=1{,}5$. Für große $m$ ist die Schranke grob, die Gruppen sind größer als $\frac12$ und nähern sich $\log2=0{,}693$.

:::frage Die Treppe wird immer flacher. Muss sie dann nicht irgendwo ankommen?
Richtig ist: Die Zuwächse verschwinden. Falsch ist der Schluss auf eine Decke. Auch $\sqrt n$ hat immer kleinere Nachbarabstände und wächst ohne Grenze ([Kapitel 4](/wissen/elektrotechnik/1-semester/hohere-mathematik-1/folgen-und-grenzwerte/folgen-und-grenzwerte.html)). Eine Decke gibt es nur, wenn die Summe aller künftigen Zuwächse klein ist, nicht jeder einzelne.
:::

:::aufgabe Aufgabe 2 ★★ Langsam, aber ohne Decke
<span class="anker" id="aufg-2"></span>

<ol class="al">

<li>

Welches $m$ garantiert nach [(2.2)](#gl-2-2) $H_{2^m}\ge10$? Um welchen Faktor liegt dieses $N=2^m$ über der wahren Schwelle $12367$?

</li>

<li>

Zeige $\sum_{n=1}^N\frac1{\sqrt n}\ge\sqrt N$, indem du jedes Glied nach unten abschätzt. Was folgt für die Reihe?

</li>

<li>

Sagt die notwendige Bedingung etwas über $\sum\frac{n^2}{n^2+1}$, $\sum\cos(\pi n)$ und $\sum\frac1{n+1}$? Entscheide.

</li>

</ol>

:::loesung
(a) $1+\frac m2\ge10$ verlangt $m\ge18$, also $N=2^{18}=262144$. Das ist das $21{,}2$-Fache der wahren Schwelle: Die Abschätzung ist grob, aber sie reicht für die Divergenz. (b) Für $n\le N$ ist $\frac1{\sqrt n}\ge\frac1{\sqrt N}$, also ist die Summe mindestens $N\cdot\frac1{\sqrt N}=\sqrt N$. Die Teilsummen sind unbeschränkt, die Reihe divergiert, obwohl die Glieder eine Nullfolge bilden. (c) $\frac{n^2}{n^2+1}\to1$ und $\cos(\pi n)=(-1)^n$ sind keine Nullfolgen, beide Reihen divergieren. Bei $\frac1{n+1}\to0$ sagt die Bedingung nichts. Die Reihe ist die harmonische ohne ihr erstes Glied und divergiert.
:::
:::

::::formelsammlung
**Cauchy-Kriterium für Reihen**

$$\forall\,\varepsilon>0\quad\exists\,N_0=N_0(\varepsilon)\in\mathbb{N}:\quad\Bigl|\sum_{\ell=m+1}^na_\ell\Bigr|<\varepsilon\quad\forall\,n>m>N_0$$

Gleichbedeutend mit der Konvergenz von $\sum_{n=1}^\infty a_n$. Die Summe im Betrag ist $S_n-S_m$; der Grenzwert kommt nicht vor.

**Notwendige Bedingung**

$$\sum_{n=1}^\infty a_n\ \text{konvergent}\quad\Longrightarrow\quad\lim_{n\to\infty}a_n=0$$

Nur notwendig, nicht hinreichend. Kontraposition: Ist $\{a_n\}$ keine Nullfolge, divergiert die Reihe; so divergiert die geometrische Reihe für $|q|\ge1$.

**Harmonische Reihe**

$$H_{2^m}\ge1+\frac m2$$

Für alle $m\in\mathbb{N}$, mit $H_N=\sum_{n=1}^N\frac1n$. Die Glieder $\frac1n$ bilden eine Nullfolge, trotzdem divergiert $\sum_{n=1}^\infty\frac1n$: Gruppe $j$ hat $2^{j-1}$ Glieder und ist mindestens $2^{j-1}\cdot\frac1{2^j}=\frac12$.
::::

::::lernkarten
:::karte formel Cauchy-Kriterium für Reihen
Wie lautet das Cauchy-Kriterium für die Konvergenz einer Reihe $\sum_{n=1}^\infty a_n$, und warum lässt es sich prüfen, ohne den Grenzwert zu kennen?
---
Die Reihe konvergiert genau dann, wenn $\forall\,\varepsilon>0\ \exists\,N_0\in\mathbb{N}:\ \bigl|\sum_{\ell=m+1}^na_\ell\bigr|<\varepsilon$ für alle $n>m>N_0$. Jedes Treppenstück hinter $N_0$ ist niedriger als $\varepsilon$; der Grenzwert kommt nicht vor.
--- falsch
Die Reihe konvergiert genau dann, wenn $\forall\,\varepsilon>0\ \exists\,N_0\in\mathbb{N}:\ |a_n|<\varepsilon$ für alle $n>N_0$. Jede einzelne Stufe hinter $N_0$ ist niedriger als $\varepsilon$; der Grenzwert kommt nicht vor.
--- falsch
Die Reihe konvergiert genau dann, wenn $\exists\,N_0\in\mathbb{N}\ \forall\,\varepsilon>0:\ \bigl|\sum_{\ell=m+1}^na_\ell\bigr|<\varepsilon$ für alle $n>m>N_0$. Ein einziger Index gilt für jede Toleranz zugleich; der Grenzwert kommt nicht vor.
--- falsch
Die Reihe konvergiert genau dann, wenn $\forall\,\varepsilon>0\ \exists\,N_0\in\mathbb{N}:\ \bigl|\sum_{\ell=m+1}^na_\ell\bigr|<\varepsilon$ für alle $n>m>N_0$. Prüfen lässt es sich aber nur mit bekanntem Grenzwert, weil $N_0$ von ihm abhängt.
:::
:::karte zusammenhang Cauchy-Folge
Was hat die Summe $\sum_{\ell=m+1}^na_\ell$ im Cauchy-Kriterium mit den Teilsummen zu tun, und warum ist das Kriterium deshalb gleichbedeutend mit Konvergenz?
---
Für $n>m$ ist $\sum_{\ell=m+1}^na_\ell=S_n-S_m$. Das Kriterium sagt also, dass $\{S_N\}$ eine Cauchy-Folge ist, und in $\mathbb{R}$ ist das nach [Kapitel 4](/wissen/elektrotechnik/1-semester/hohere-mathematik-1/folgen-und-grenzwerte/folgen-und-grenzwerte.html) gleichbedeutend mit Konvergenz.
--- falsch
Für $n>m$ ist $\sum_{\ell=m+1}^na_\ell=S_n+S_m$. Das Kriterium sagt also, dass die Teilsummen beschränkt sind, und beschränkte Folgen konvergieren in $\mathbb{R}$ nach [Kapitel 4](/wissen/elektrotechnik/1-semester/hohere-mathematik-1/folgen-und-grenzwerte/folgen-und-grenzwerte.html).
--- falsch
Für $n>m$ ist $\sum_{\ell=m+1}^na_\ell=S_n-S_m$. Das Kriterium sagt also, dass $\{S_N\}$ eine Cauchy-Folge ist; Cauchy-Folgen konvergieren aber nicht immer, das Kriterium ist nur notwendig.
--- falsch
Für $n>m$ ist $\sum_{\ell=m+1}^na_\ell=a_n-a_m$. Das Kriterium sagt also, dass die Glieder $\{a_n\}$ eine Cauchy-Folge bilden, und das ist gleichbedeutend mit der Konvergenz der Reihe.
:::
:::karte formel notwendige Bedingung
Welche notwendige Bedingung an die Glieder folgt aus der Konvergenz einer Reihe, und wie nutzt man sie als Test?
---
Konvergiert $\sum_{n=1}^\infty a_n$, dann gilt $\lim_{n\to\infty}a_n=0$. Getestet wird mit der Kontraposition: Ist $\{a_n\}$ keine Nullfolge, muss die Reihe divergieren. Aus $a_n\to0$ folgt keine Konvergenz.
--- falsch
Konvergiert $\sum_{n=1}^\infty a_n$, dann gilt $\lim_{n\to\infty}a_n=0$. Getestet wird mit der Umkehrung: Ist $\{a_n\}$ eine Nullfolge, dann konvergiert die Reihe, und sonst divergiert sie in jedem Fall.
--- falsch
Konvergiert $\sum_{n=1}^\infty a_n$, dann fallen die Glieder monoton. Getestet wird mit der Kontraposition: Steigen die Glieder irgendwo an, so muss die Reihe divergieren.
--- falsch
Konvergiert $\sum_{n=1}^\infty a_n$ gegen $S$, dann gilt $\lim_{n\to\infty}a_n=S$. Getestet wird mit der Kontraposition: Streben die Glieder nicht gegen $S$, so muss die Reihe divergieren.
:::
:::karte begriff harmonische Reihe
Was ist die harmonische Reihe, und was zeigt sie über den Zusammenhang zwischen Nullfolge und Konvergenz?
---
Die Reihe $\sum_{n=1}^\infty\frac1n=1+\frac12+\frac13+\dots$. Ihre Glieder $\frac1n$ bilden eine Nullfolge, trotzdem divergiert sie, denn $H_{2^m}\ge1+\frac m2$ für alle $m\in\mathbb{N}$: Schrumpfende Glieder reichen nicht.
--- falsch
Die Reihe $\sum_{n=1}^\infty\frac1n=1+\frac12+\frac13+\dots$. Ihre Glieder bilden eine Nullfolge, also konvergiert sie, denn $H_{2^m}\le1+\frac m2$ für alle $m\in\mathbb{N}$: Die Teilsummen wachsen nur langsam.
--- falsch
Die Reihe $\sum_{n=1}^\infty\frac1n=1+\frac12+\frac13+\dots$. Ihre Glieder bilden eine Nullfolge, und ihre Teilsummen pendeln; deshalb divergiert sie, ohne über alle Grenzen zu wachsen.
--- falsch
Die Reihe $\sum_{n=1}^\infty\frac1n=1+\frac12+\frac13+\dots$. Ihre Glieder bilden eine Nullfolge, und die Teilsummen bleiben unter 15, wie $H_{10^6}=14{,}39$ zeigt: Sie konvergiert, nur sehr langsam.
:::
:::karte herleitung Gruppen, die je mindestens ein Halb ergeben
Wie zeigt man mit Gruppen aus $1,2,4,8,\dots$ Gliedern, dass $H_{2^m}\ge1+\frac m2$ gilt und die harmonische Reihe divergiert?
---
Man schreibt $H_{2^m}=1+\frac12+\bigl(\frac13+\frac14\bigr)+\bigl(\frac15+\dots+\frac18\bigr)+\dots$, weil Klammern in einer endlichen Summe nichts ändert.
---
Gruppe $j$ endet bei $\frac1{2^j}$ und hat $2^{j-1}$ Glieder, weil sie die Nenner $2^{j-1}+1$ bis $2^j$ umfasst.
---
Jede Gruppe ist mindestens $2^{j-1}\cdot\frac1{2^j}=\frac12$, weil jedes ihrer Glieder mindestens so groß ist wie das letzte.
---
Mit dem Anfangsglied 1 und $m$ Gruppen folgt $H_{2^m}\ge1+\frac m2$, weil jede der $m$ Gruppen mindestens $\frac12$ beiträgt.
---
Also ist $\{H_N\}$ unbeschränkt und konvergiert nicht, weil konvergente Folgen nach [Kapitel 4](/wissen/elektrotechnik/1-semester/hohere-mathematik-1/folgen-und-grenzwerte/folgen-und-grenzwerte.html) beschränkt sind.
:::
:::karte zusammenhang zu langsam schrumpfende Glieder
Warum divergiert die harmonische Reihe, obwohl jedes einzelne Glied gegen 0 geht?
---
Weil sich von Gruppe zu Gruppe die Höhe der Glieder halbiert und ihre Anzahl verdoppelt; das Produkt bleibt mindestens $\frac12$. Die Glieder schrumpfen zu langsam gegen ihre wachsende Zahl.
--- falsch
Weil die Glieder zwar gegen 0 gehen, aber nicht monoton fallen. Bei monoton fallenden Nullfolgen konvergiert die Reihe immer, denn dann kommt mit jeder Stufe weniger hinzu als zuvor, und die Treppe flacht ab.
--- falsch
Weil jedes einzelne Glied mindestens $\frac12$ beiträgt. Die Treppe steigt also bei jeder Stufe um einen festen Betrag und wächst deshalb über jede Grenze, egal wie weit man geht.
--- falsch
Weil die Teilsummen pendeln, ohne sich festzulegen: Die Gruppen tragen abwechselnd mehr und weniger als $\frac12$ bei, und deshalb gibt es keinen Grenzwert, nur eine Decke.
:::
:::karte zusammenhang flache Treppe ohne Decke
Warum hat die Treppe der Teilsummen $H_N$ keine Decke, obwohl ihre Zuwächse verschwinden?
---
Weil eine Decke nur entsteht, wenn die Summe aller künftigen Zuwächse klein ist, nicht schon jeder einzelne. Auch $\sqrt n$ hat immer kleinere Nachbarabstände und wächst ohne Grenze.
--- falsch
Sie hat eine Decke, man sieht sie nur numerisch nicht: Verschwindende Zuwächse erzwingen immer einen Grenzwert, er liegt bei der harmonischen Reihe nur sehr weit oben, jenseits von 15.
--- falsch
Weil die Zuwächse nur bei endlich vielen Stufen verschwinden; danach werden sie wieder größer, und die Treppe steigt erneut über jede feste Höhe hinaus.
--- falsch
Weil eine Decke nur entsteht, wenn jeder einzelne Zuwachs kleiner als $\frac12$ ist. Bei der harmonischen Reihe ist schon der zweite Zuwachs genau $\frac12$, das ist zu viel.
:::
:::karte zusammenhang Divergenz der geometrischen Reihe
Warum divergiert die geometrische Reihe $\sum_{n=0}^\infty q^n$ für $|q|\ge1$?
---
Weil für $|q|\ge1$ auch $|q^n|\ge1$ ist. Die Glieder bilden also keine Nullfolge, und nach der notwendigen Bedingung muss die Reihe divergieren.
--- falsch
Weil für $|q|\ge1$ der Nenner von $\frac1{1-q}$ null oder negativ wird. Eine Reihe mit negativem oder unendlichem Wert gilt als divergent.
--- falsch
Weil für $|q|\ge1$ jedes Glied mindestens 1 ist. Die Teilsummen wachsen also monoton und steigen über jede Grenze, auch bei negativem $q$ wie $q=-1$.
--- falsch
Weil für $|q|\ge1$ auch $|q^n|\ge1$ ist. Das zeigt die Divergenz aber nur für $q\ge1$; für $q\le-1$ heben sich die Glieder paarweise auf.
:::
::::
