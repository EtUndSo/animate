---
title: Stufe 1: Der Konvergenzkreis
pfad: Elektrotechnik / 1. Semester / Höhere Mathematik 1 / Potenzreihen und Eulersche Formel
order: 1270300
summary: Polynome (Teil 3) sind endliche Summen von Potenzen.
tags: Koeffizienten, Definitionsmenge
lang: de
---

<span class="anker" id="stufe-1"></span>

:::zweck
Polynome ([Teil 3](/wissen/elektrotechnik/1-semester/hohere-mathematik-1/funktionen-und-polynome/funktionen-und-polynome.html)) sind endliche Summen von Potenzen. Diese Stufe lässt die Summe nie enden und klärt, für welche $x$ das Ergebnis eine Zahl ist.
:::

**Die Idee.** Für festes $x$ ist $\sum a_nx^n$ eine gewöhnliche Reihe. Das $x$ steckt nur im Faktor $x^n$, und das ist eine geometrische Folge. Angenommen, die Reihe konvergiert noch bei $y$. Dann sind die Glieder $a_ny^n$ beschränkt. Bei $|x|<|y|$ ist jedes Glied zusätzlich um den Faktor $|x/y|^n$ kleiner, und dieser Faktor schrumpft geometrisch. Also konvergiert die Reihe dort absolut. Konvergenz an einer Stelle zieht Konvergenz an allen Stellen mit kleinerem Betrag nach sich. Der Konvergenzbereich kann deshalb keine Löcher haben: Er reicht vom Nullpunkt gleichmäßig nach außen bis zu einem Radius (Abb. [1](#abb-1)).

:::abbildung hm1/k7kreis 1
Links die Glieder von $f$: Für $x=1$ fallen sie schnell, für $x=2$ wie $1/n$, für $x=3$ wachsen sie ab $n=3$. Rechts der Konvergenzbereich in der komplexen Ebene (Stufe [5](die-exponentialreihe-reell-und-komplex.html#stufe-5)) mit $R=2$. Auf dem Rand entscheidet jeder Punkt für sich: bei $-2$ Konvergenz (grün), bei $2$ Divergenz (rot).
:::

:::definition Definition 1.1 (Potenzreihe, Konvergenzradius)
<span class="anker" id="satz-1-1"></span>

Sei $a_0,a_1,a_2,\dots$ eine Folge reeller Zahlen. Die Abbildung $f:K\to\mathbb{R}$, $x\mapsto\sum_{n=0}^\infty a_nx^n$ heißt Potenzreihe in $x$, die $a_n$ heißen __Koeffizienten__. Die __Definitionsmenge__ ist $K:=\{x\in\mathbb{R}:\sum_{n=0}^\infty a_nx^n\text{ ist konvergent}\}$. Die Zahl $R:=\sup\{|y|:y\in K\}$ heißt Konvergenzradius, mit $R:=\infty$, wenn diese Menge unbeschränkt ist.
:::

⁠**So liest man das:** Die $a_n$ sind feste Zahlen ohne Einheit, $x$ ist die Variable. Für $x=0$ bleibt nur $a_0$, denn $0^0=1$ ([Teil 1](/wissen/elektrotechnik/1-semester/hohere-mathematik-1/mengen-logik-und-reelle-zahlen/mengen-logik-und-reelle-zahlen.html)). Also ist $0\in K$, und es gilt $0\le R\le\infty$.

:::satz Satz 1.2 (Konvergenzradius)
<span class="anker" id="satz-1-2"></span>

Sei $\sum a_nx^n$ eine Potenzreihe mit Konvergenzradius $R$ und Definitionsmenge $K$.

<ol class="rm">

<li>

Ist $R=0$, dann ist $K=\{0\}$: Die Reihe konvergiert nur für $x=0$.

</li>

<li>

Ist $R>0$, dann ist $(-R,R)\subset K$, und für alle $x$ mit $|x|<R$ ist die Reihe sogar absolut konvergent.

</li>

<li>

Für $|x|>R$ ist die Reihe divergent.

</li>

</ol>
:::

⁠**So liest man das:** Innen absolute Konvergenz, außen Divergenz. **Gültigkeit:** Für $|x|=R$ sagt der Satz nichts. Die Randpunkte muss man einzeln prüfen.

:::beweis Geometrische Majorante
(i), (iii): Nach Definition des Supremums gilt $|y|\le R$ für alle $y\in K$. Ein $x$ mit $|x|>R$ liegt also nicht in $K$. Für $R=0$ bleibt nur $y=0$.

(ii): Sei $|x|<R$. Weil $R$ die kleinste obere Schranke ist, ist $|x|$ keine obere Schranke. Es gibt also $y\in K$ mit $|x|<|y|\le R$. Die Reihe $\sum a_ny^n$ konvergiert, also sind ihre Glieder beschränkt: $|a_ny^n|\le C$ für alle $n$. Damit ist

$$|a_nx^n|=|a_ny^n|\,\Bigl|\frac xy\Bigr|^n\le C\,q^n\qquad\text{mit}\qquad q:=\Bigl|\frac xy\Bigr|<1.$$

Die geometrische Reihe $\sum Cq^n$ ist eine konvergente Majorante.
:::

**Beispiel.** Bei $f$ reicht die Definition. Für $x=2$ sind die Glieder $1/n$, die harmonische Reihe divergiert. Für $x=-2$ sind sie $(-1)^n/n$, die Reihe konvergiert nach Leibniz. Aus $-2\in K$ folgt $R\ge2$. Wäre $R>2$, läge $2$ nach (ii) in $K$. Also ist $R=2$ und $K=[-2,2)$.

⁠**Warum die Form $a_nx^n$ nötig ist:** Die Reihe $\sum_{n\ge1}n^{-x}$ hängt ebenfalls von $x$ ab, konvergiert aber genau für $x>1$. Das ist eine Halbgerade, kein Bereich um 0, denn der geometrische Faktor fehlt. **Grenzfälle:** Ein Polynom ($a_n=0$ ab einer Stelle) hat $R=\infty$. Die Reihe $\sum n!\,x^n$ hat $R=0$, denn $|x|^n/n!$ ist für jedes $x$ eine Nullfolge ([Teil 4](/wissen/elektrotechnik/1-semester/hohere-mathematik-1/folgen-und-grenzwerte/folgen-und-grenzwerte.html)), also wachsen die Glieder für $x\ne0$ über alle Grenzen.

:::frage Warum heißt es Kreis, wenn $x$ auf einer Geraden liegt?
Auf der reellen Achse ist es das Intervall $(-R,R)$, so weit stimmt der Einwand. Der Beweis benutzt aber nur Beträge. Setzt man komplexe Zahlen ein (Stufe [5](die-exponentialreihe-reell-und-komplex.html#stufe-5)), gilt er wörtlich, und $|z|<R$ ist eine Kreisscheibe.
:::

:::aufgabe Aufgabe 1 ★ Bereich ohne Kriterium
<span class="anker" id="aufg-1"></span>

(a) Bestimme $R$ und $K$ von $\sum_{n=0}^\infty3^nx^n$. (b) Bestimme $R$ und $K$ von $\sum_{n=1}^\infty x^n/n^2$, auch die Randpunkte. (c) Eine Potenzreihe konvergiert bei $x=4$ und divergiert bei $x=-7$. Was folgt für $R$? Was lässt sich über $x=-3$, $x=-4$, $x=5$ und $x=8$ sagen?

:::loesung
(a) Das ist die geometrische Reihe mit $q=3x$. Sie konvergiert genau für $|3x|<1$: $R=\frac13$, $K=(-\frac13,\frac13)$. Bei $|x|=\frac13$ haben die Glieder den Betrag 1. (b) Bei $x=\pm1$ ist $\sum1/n^2$ Majorante, also $\pm1\in K$ und $R\ge1$. Für $|x|>1$ wächst $|x|^n/n^2$ über alle Grenzen. Also ist $R=1$ und $K=[-1,1]$. (c) $4\in K$ gibt $R\ge4$, und $-7\notin K$ gibt $R\le7$. $x=-3$: absolut konvergent, denn $3<4\le R$. $x=8$: divergent, denn $8>7\ge R$. Über $x=-4$ und $x=5$ ist nichts bekannt: $-4$ kann ein Randpunkt sein, und $R$ kann unter oder über 5 liegen.
:::
:::
