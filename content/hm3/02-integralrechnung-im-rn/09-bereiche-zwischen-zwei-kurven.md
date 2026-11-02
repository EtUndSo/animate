---
title: Stufe 7: Bereiche zwischen zwei Kurven
pfad: Elektrotechnik / 3. Semester / Höhere Mathematik 3 / Integralrechnung im Rⁿ
order: 3120900
summary: Ein Bereich in der Ebene ist selten ein Rechteck.
tags: Normalbereich, regulär
lang: de
---

<span class="anker" id="stufe-7"></span>

:::zweck
Ein Bereich in der Ebene ist selten ein Rechteck. Diese Stufe zerlegt Bereiche zwischen zwei Kurven in zwei gewöhnliche Integrale und zeigt, warum die Grenzen innen Funktionen sind.
:::

**Die Idee.** Man zerlegt den Bereich in Streifen. Für jedes feste $x$ läuft ein senkrechter Streifen von der unteren zur oberen Randkurve. Das ist ein Integral einer Variablen. Danach summiert man die Streifen über $x$. Das ist derselbe Gedanke wie bei Fubini, nur sind die Streifen verschieden lang, und ihre Länge hängt von der äußeren Variablen ab (Abb. [7](#abb-7)).

:::abbildung hm3/k2normal 7
Die Linse zwischen $y=x^2$ und $y=x$ lässt sich senkrecht (links) und waagerecht (Mitte) in Streifen schneiden. Rechts die Kreisscheibe mit Radius 2 aus drei regulären Normalbereichen: Mittelstreifen vom Typ 1, oben und unten je eine Kappe vom Typ 2.
:::

:::definition Definition 7.1 (Normalbereich)
<span class="anker" id="satz-7-1"></span>

Ein __Normalbereich__ im $\mathbb{R}^2$ ist eine Menge der Form

$$\begin{aligned} \text{Typ 1:}\quad&D=\{(x,y)\in\mathbb{R}^2:\alpha(y)\le x\le\beta(y),\ c\le y\le d\},\qquad\alpha,\beta:[c,d]\to\mathbb{R}\text{ stetig},\\ \text{Typ 2:}\quad&D=\{(x,y)\in\mathbb{R}^2:\mu(x)\le y\le\nu(x),\ a\le x\le b\},\qquad\mu,\nu:[a,b]\to\mathbb{R}\text{ stetig}. \end{aligned}$$

Normalbereiche heißen __regulär__, wenn $\alpha,\beta$ bzw. $\mu,\nu$ stetig differenzierbar sind.
:::

:::satz Satz 7.2 (Integration über Normalbereiche)
<span class="anker" id="satz-7-2"></span>

Sei $D$ ein Normalbereich und $f:D\to\mathbb{R}$ stetig. Dann ist das Integral von $f$ über $D$ wohldefiniert, und es gilt

<span class="anker" id="gl-7-1"></span>
$$\int_Df(x,y)\,\mathrm{d} x\,\mathrm{d} y=\int_c^d\Bigl(\int_{\alpha(y)}^{\beta(y)}f(x,y)\,\mathrm{d} x\Bigr)\mathrm{d} y\quad\text{(Typ 1)}, \tag{7.1}$$

entsprechend $\int_a^b\bigl(\int_{\mu(x)}^{\nu(x)}f(x,y)\,\mathrm{d} y\bigr)\mathrm{d} x$ für Typ 2. Für $f\equiv1$ erhält man den Flächeninhalt

<span class="anker" id="gl-7-2"></span>
$$|D|=\int_c^d\ell(y)\,\mathrm{d} y\quad\text{mit}\quad\ell(y)=\beta(y)-\alpha(y). \tag{7.2}$$

Ferner gilt $\bigl|\int_Df(x,y)\,\mathrm{d} x\,\mathrm{d} y\bigr|\le|D|\,\sup_{(x,y)\in D}|f(x,y)|$.
:::

⁠**So liest man das:** Innen läuft $x$ bei festem $y$ von der linken Randkurve $\alpha(y)$ zur rechten $\beta(y)$. $\ell(y)$ ist die Breite des Streifens auf Höhe $y$. Außen läuft $y$ über feste Zahlen. Das Ergebnis des inneren Integrals hängt noch von $y$ ab, das des äußeren nicht mehr. **Grenzfall:** Bei konstanten $\alpha$, $\beta$ ist $D$ ein Rechteck, und [(7.1)](#gl-7-1) ist das iterierte Integral aus Stufe [5](uber-quader-integrieren.html#stufe-5).

:::herleitung Warum die Grenzen so aussehen
Fortsetzung durch null wie in [(6.1)](mengen-und-scheiben.html#gl-6-1). Bei festem $y$ ist $\bar f(x,y)$ gleich $f(x,y)$ für $\alpha(y)\le x\le\beta(y)$ und sonst null. Das Integral über die Zeile des Quaders ist also $\int_{\alpha(y)}^{\beta(y)}f(x,y)\,\mathrm{d} x$. Nach der Leibnizregel, Teil über bloße Stetigkeit, ist das stetig in $y$, das äußere Integral existiert also. Die Abschätzung folgt wie in [(5.3)](uber-quader-integrieren.html#gl-5-3) aus $-S\le f\le S$ und [(7.2)](#gl-7-2).
:::

**Beispiel: Linse.** $D$ liegt zwischen $y=x^2$ und $y=x$. Als Typ 2 ist $x^2\le y\le x$, $0\le x\le1$. Als Typ 1 ist $y\le x\le\sqrt y$, $0\le y\le1$. Für $f(x,y)=x$:

$$\int_0^1\Bigl(\int_{x^2}^xx\,\mathrm{d} y\Bigr)\mathrm{d} x=\int_0^1(x^2-x^3)\,\mathrm{d} x=\frac1{12},\qquad\int_0^1\Bigl(\int_y^{\sqrt y}x\,\mathrm{d} x\Bigr)\mathrm{d} y=\int_0^1\frac{y-y^2}2\,\mathrm{d} y=\frac1{12}.$$

Der Flächeninhalt ist $|D|=\int_0^1(x-x^2)\,\mathrm{d} x=\frac16$. Die Abschätzung gibt $\frac1{12}\le\frac16\cdot1$. Als Typ 2 ist die Linse regulär. Als Typ 1 ist sie es nicht, denn $\sqrt y$ ist bei $y=0$ nicht differenzierbar. Regularität hängt also von der Beschreibung ab.

**Zerlegen.** Gängige Bereiche $D\subset\mathbb{R}^2$ sind Vereinigungen von endlich vielen regulären Normalbereichen $D_j$, die sich höchstens längs ihrer Randkurven überlappen. Stetige Funktionen integriert man dann stückweise:

<span class="anker" id="gl-7-3"></span>
$$\int_Df(\boldsymbol{x})\,\mathrm{d}\boldsymbol{x}=\sum_{j=1}^N\int_{D_j}f(\boldsymbol{x})\,\mathrm{d}\boldsymbol{x}. \tag{7.3}$$

Das Ergebnis hängt nicht von der gewählten Zerlegung ab.

**Beispiel: Kreisscheibe.** Der Grundkreis der Kuppel ist $D=\{x^2+y^2\le4\}$. Er ist ein Normalbereich vom Typ 1 mit $\alpha(y)=-\sqrt{4-y^2}$, $\beta(y)=\sqrt{4-y^2}$, $y\in[-2,2]$. Aber $\beta'(y)=-y/\sqrt{4-y^2}$ wächst für $y\to\pm2$ unbeschränkt: Der Rand hat dort eine waagerechte Tangente, als Funktion von $y$ also eine unendliche Steigung. $D$ ist deshalb kein regulärer Normalbereich. Zerlegung hilft: Der Mittelstreifen $|y|\le\sqrt2$ ist regulär vom Typ 1. Die Kappen $\sqrt2\le|y|$ sind regulär vom Typ 2, $\sqrt2\le y\le\sqrt{4-x^2}$ mit $|x|\le\sqrt2$, und unten gespiegelt. Mit $\int_{-\sqrt2}^{\sqrt2}\sqrt{4-s^2}\,\mathrm{d} s=2+\pi$ ergeben sich für Streifen und Kappen die Flächen $4+2\pi$ und je $\pi-2$, zusammen $4\pi$.

:::frage Warum darf das innere Integral keine festen Grenzen haben?
Feste Grenzen beschreiben ein Rechteck. Bei $\int_0^1\int_{0}^{1}$ statt $\int_0^1\int_{x^2}^x$ rechnet man über das Quadrat, nicht über die Linse. Faustregel: Nach dem inneren Integral darf die äußere Variable noch auftauchen, nach dem äußeren muss eine Zahl herauskommen.
:::

:::aufgabe Aufgabe 10 ★★ Ein Betrag zwingt zum Zerlegen
<span class="anker" id="aufg-10"></span>

Sei $D=\{(x,y):0\le x\le2,\ x-1\le y\le1\}$. Skizziere $D$ und berechne $\int_D|y|\,\mathrm{d} x\,\mathrm{d} y$. Tipp: Das Vorzeichen von $y$ wechselt im inneren Integral nur für einen Teil der $x$.

:::loesung
$D$ ist Typ 2 mit $\mu(x)=x-1$, $\nu(x)=1$. Für $1\le x\le2$ ist $\mu\ge0$, also $\int_{x-1}^1y\,\mathrm{d} y=\frac12(1-(x-1)^2)$. Für $0\le x\le1$ ist $\mu\le0$, man teilt bei $y=0$: $\int_{x-1}^0(-y)\,\mathrm{d} y+\int_0^1y\,\mathrm{d} y=\frac12((x-1)^2+1)$. Damit ist

$$\int_D|y|\,\mathrm{d} x\,\mathrm{d} y=\int_0^1\tfrac12\bigl((x-1)^2+1\bigr)\mathrm{d} x+\int_1^2\tfrac12\bigl(1-(x-1)^2\bigr)\mathrm{d} x=\frac23+\frac13=1.$$
:::
:::

:::aufgabe Aufgabe 11 ★★ Reihenfolge tauschen
<span class="anker" id="aufg-11"></span>

Berechne $\int_0^1\bigl(\int_y^1\mathrm{e}^{x^2}\,\mathrm{d} x\bigr)\mathrm{d} y$. Tipp: Das innere Integral hat keine elementare Stammfunktion. Beschreibe das Dreieck als Normalbereich vom anderen Typ.

:::loesung
Das Gebiet ist $y\le x\le1$, $0\le y\le1$, das Dreieck mit den Ecken $(0,0)$, $(1,0)$, $(1,1)$. Vom Typ 2 ist es $0\le y\le x$, $0\le x\le1$. Also ist

$$\int_0^1\Bigl(\int_0^x\mathrm{e}^{x^2}\,\mathrm{d} y\Bigr)\mathrm{d} x=\int_0^1x\,\mathrm{e}^{x^2}\,\mathrm{d} x=\Bigl[\tfrac12\mathrm{e}^{x^2}\Bigr]_0^1=\frac{\mathrm{e}-1}2\approx0{,}859.$$
:::
:::
