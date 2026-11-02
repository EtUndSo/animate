---
title: Stufe 6: Mengen und Scheiben
pfad: Elektrotechnik / 3. Semester / Höhere Mathematik 3 / Integralrechnung im Rⁿ
order: 3120800
summary: Die meisten Körper sind keine Quader.
tags: kompakter Träger, Träger, Lebesgue-Integral, wohldefiniert
lang: de
---

<span class="anker" id="stufe-6"></span>

:::zweck
Die meisten Körper sind keine Quader. Diese Stufe sagt, was ein Integral über eine beliebige Menge bedeutet, und berechnet Volumina aus Querschnitten.
:::

**Die Idee.** Eine beschränkte Menge passt in einen Quader. Setzt man den Integranden außerhalb der Menge null, zählt nur die Menge. Das ist die Definition. Zum Rechnen taugt sie selten, dafür braucht man Scheiben: Ein Körper ist ein Stapel dünner Schichten, und jede Schicht hat fast das Volumen Fläche mal Dicke. Verschiebt man die Schichten seitlich, ändert sich keine von ihnen (Abb. [6](#abb-6)).

:::abbildung hm3/k2cavalieri 6
Links ein Kegel auf der Spitze mit $R=2$, $H=3$. Der Schnitt auf Höhe $z$ ist ein Kreis mit Radius $2z/3$. Rechts sind dieselben Scheiben seitlich verschoben. Auf jeder Höhe bleibt die Schnittfläche gleich.
:::

:::definition Definition 6.1 (Kompakter Träger)
<span class="anker" id="satz-6-1"></span>

Gibt es für eine stetige Funktion $f:\mathbb{R}^n\to\mathbb{R}$ ein $R>0$ mit $f(\boldsymbol{x})=0$ für alle $\boldsymbol{x}\in\mathbb{R}^n$ mit $|\boldsymbol{x}|>R$, dann liegt ein __kompakter Träger__ vor. Für solche $f$ setzt man

$$\int_{\mathbb{R}^n}f(\boldsymbol{x})\,\mathrm{d}\boldsymbol{x}:=\int_Qf(\boldsymbol{x})\,\mathrm{d}\boldsymbol{x}$$

mit einem geeigneten Quader $Q$, außerhalb dessen $f=0$ ist.
:::

Der __Träger__ ist der Abschluss der Menge $\{f\neq0\}$, er ist hier abgeschlossen und beschränkt, also kompakt. Welcher Quader, ist egal, denn ein größerer fügt nur Stücke mit $f=0$ hinzu. Beispiel: $f(x)=\max(0,1-|x|)$ hat $R=1$, und $\int_\mathbb{R} f\,\mathrm{d} x=1$.

**Weiter als stetig.** Es liegt nahe, den Integralbegriff auf Funktionen zu erweitern, die in einem geeigneten Sinn Grenzwerte stetiger Funktionen mit kompaktem Träger sind. Der passende Rahmen dafür ist das __Lebesgue-Integral__. Seine Theorie wird hier nicht entwickelt, nur eines ihrer Ergebnisse wird gleich benutzt.

**Integral über eine Menge.** Sei $M\subset\mathbb{R}^n$ abgeschlossen und beschränkt, $f:M\to\mathbb{R}$ stetig und $Q\supset M$ ein Quader. Man setzt $f$ durch null fort:

<span class="anker" id="gl-6-1"></span>
$$\bar f(\boldsymbol{x})=\begin{cases}f(\boldsymbol{x})&\boldsymbol{x}\in M,\\0&\boldsymbol{x}\in Q\setminus M,\end{cases}\qquad\int_Mf(\boldsymbol{x})\,\mathrm{d}\boldsymbol{x}:=\int_Q\bar f(\boldsymbol{x})\,\mathrm{d}\boldsymbol{x}. \tag{6.1}$$

Das hat einen Haken: $\bar f$ ist im Allgemeinen nicht stetig, denn am Rand von $M$ springt sie von $f$ auf null. Stufe [5](uber-quader-integrieren.html#stufe-5) sagt deshalb nichts über die rechte Seite. Die Lebesguesche Theorie garantiert aber, dass dieses Integral für abgeschlossene, beschränkte $M$ __wohldefiniert__ ist, also einen eindeutigen Wert hat, zum Beispiel mit $\bar f$ als Grenzwert geeigneter stetiger Funktionen in $Q$. Die praktische Rechnung braucht zusätzlich einen genügend glatten Rand von $M$ und zerlegt $M$ in Scheiben.

:::satz Satz 6.2 (Prinzip von Cavalieri)
<span class="anker" id="satz-6-2"></span>

Gegeben sei ein Körper $M=\{(x,y,z)\in\mathbb{R}^3:(x,y)\in D(z),\ 0\le z\le H\}$ mit Schnittflächen $D(z)\subset\mathbb{R}^2$, deren Flächeninhalt $\mathcal A(z)=|D(z)|$ stetig von $z$ abhängt. Dann gilt

<span class="anker" id="gl-6-2"></span>
$$\operatorname{vol}(M)=\int_0^H\mathcal A(z)\,\mathrm{d} z. \tag{6.2}$$
:::

:::herleitung Riemann-Summe über die Höhe
Zerlege die Höhe in $N$ Scheiben der Dicke $h=H/N$. Die $k$-te Scheibe hat rund das Volumen $\mathcal A(z_k)\,h$ mit einem $z_k$ im Bereich $(k-1)h\le z_k\le kh$. Aufaddieren gibt

$$\operatorname{vol}(M)\sim h\sum_{k=1}^N\mathcal A(z_k).$$

Das ist eine Riemann-Summe von $\mathcal A$ auf $[0,H]$. Da $\mathcal A$ stetig ist, existiert der Grenzwert $h\searrow0$ unabhängig von der Wahl der $z_k$, und er ist [(6.2)](#gl-6-2).
:::

⁠**So liest man das:** $H$ ist die Höhe, $D(z)$ der ebene Querschnitt auf Höhe $z$, $\mathcal A(z)$ seine Fläche. Bei der Kuppel ist $H=4$ und $\mathcal A(0)=4\pi$. Es zählt nur diese Fläche, nicht wo der Querschnitt liegt oder welche Form er hat. Zwei Körper mit auf jeder Höhe gleicher Schnittfläche haben dasselbe Volumen.

**Beispiel: Kegel.** Ein Kegel mit Grundkreis vom Radius $R$ und Höhe $H$ wird auf die Spitze gestellt. Der Radius wächst linear mit $z$, also ist $\mathcal A(z)=\pi(zR/H)^2$ und

$$\operatorname{vol}=\int_0^H\pi\frac{R^2}{H^2}z^2\,\mathrm{d} z=\frac\pi3R^2H.$$

Bei $R=2$, $H=3$ ist das $4\pi$. **Grenzfall:** Bei konstantem $\mathcal A$ bleibt Grundfläche mal Höhe.

**Beispiel: Kuppel.** Auf Höhe $z$ ist $x^2+y^2\le4-z$, ein Kreis mit $\mathcal A(z)=\pi(4-z)$. Also ist

<span class="anker" id="gl-6-3"></span>
$$\operatorname{vol}(K)=\int_0^4\pi(4-z)\,\mathrm{d} z=8\pi. \tag{6.3}$$

:::analogie
Ein Stapel Münzen lässt sich schief schieben, ohne dass sich sein Volumen ändert. Jede Münze bleibt dieselbe. Das Bild hört auf zu stimmen, wenn die Schichten dick sind: Eine echte Münze hat auf ihrer ganzen Dicke dieselbe Schnittfläche, ein Kegel nicht. Erst der Grenzwert $h\searrow0$ macht daraus eine exakte Aussage.
:::

:::aufgabe Aufgabe 9 ★★ Scheiben zählen
<span class="anker" id="aufg-9"></span>

<ol class="al">

<li>

Ein Kugeltank mit Radius 2 ist bis zur Höhe $h$ über seinem tiefsten Punkt gefüllt, $0\le h\le4$. Berechne das Volumen $V(h)$. Prüfe $V(4)$ und $V(2)$.

</li>

<li>

Berechne das Volumen des Oktaeders $\{|x|+|y|+|z|\le1\}$. Tipp: Die Schnitte sind Quadrate.

</li>

</ol>

:::loesung
(a) Der Mittelpunkt liegt bei $z=2$. Auf Höhe $z$ ist der Schnitt ein Kreis mit $r^2=4-(z-2)^2=4z-z^2$. Also ist

$$V(h)=\int_0^h\pi(4z-z^2)\,\mathrm{d} z=\pi\Bigl(2h^2-\frac{h^3}3\Bigr).$$

$V(4)=\frac{32\pi}3=\frac43\pi\cdot2^3$ ist die ganze Kugel, $V(2)=\frac{16\pi}3$ die Hälfte. (b) Auf Höhe $z$ ist $|x|+|y|\le1-|z|$, ein Quadrat mit Diagonalen der Länge $2(1-|z|)$ und Fläche $\mathcal A(z)=2(1-|z|)^2$. Also ist $\operatorname{vol}=2\int_0^12(1-z)^2\,\mathrm{d} z=\frac43$.
:::
:::
