---
title: Stufe 2: Wandernde Grenzen
pfad: Elektrotechnik / 3. Semester / Höhere Mathematik 3 / Integralrechnung im Rⁿ
order: 3120400
summary: Oft hängen auch die Integrationsgrenzen vom Parameter ab.
tags: Leibnizregel
lang: de
---

<span class="anker" id="stufe-2"></span>

:::zweck
Oft hängen auch die Integrationsgrenzen vom Parameter ab. Diese Stufe zeigt, welche Terme dadurch beim Ableiten hinzukommen.
:::

**Die Idee.** Das Integral $F(y)=\int_{\alpha(y)}^{\beta(y)}f(x,y)\,\mathrm{d} x$ ist eine Fläche mit beweglichen Rändern. Ändert sich $y$ um ein kleines $\Delta y$, geschehen drei Dinge (Abb. [2](#abb-2)). Die Kurve hebt oder senkt sich, das ändert die Fläche um rund $\Delta y\int_\alpha^\beta\partial_yf\,\mathrm{d} x$. Die rechte Grenze rückt um rund $\beta'(y)\,\Delta y$ vor, dort kommt ein Streifen der Höhe $f(\beta,y)$ hinzu. Die linke Grenze rückt um rund $\alpha'(y)\,\Delta y$ vor, dort fällt ein Streifen der Höhe $f(\alpha,y)$ weg. Teilt man durch $\Delta y$ und lässt $\Delta y\to0$, entsteht die __Leibnizregel__.

:::abbildung hm3/k2leibniz 2
Die drei Beiträge zur Änderung der Fläche. Das Band zwischen den Kurven gehört zum Integral über $\partial_yf$. Der rechte Streifen ist der positive Randterm, der linke der negative. Alle Streifen werden für $\Delta y\to0$ proportional zu $\Delta y$.
:::

:::satz Satz 2.1 (Leibnizregel)
<span class="anker" id="satz-2-1"></span>

Seien $\alpha,\beta:[c,d]\to\mathbb{R}$ stetig differenzierbar und $f$ stetig differenzierbar in einer Umgebung von

$$D=\{(x,y)\in\mathbb{R}^2:\alpha(y)\le x\le\beta(y),\ c\le y\le d\}.$$

Dann ist $F(y):=\int_{\alpha(y)}^{\beta(y)}f(x,y)\,\mathrm{d} x$ stetig differenzierbar auf $[c,d]$, und es gilt

<span class="anker" id="gl-2-1"></span>
$$F'(y)=\int_{\alpha(y)}^{\beta(y)}\frac{\partial f}{\partial y}(x,y)\,\mathrm{d} x+f(\beta(y),y)\,\beta'(y)-f(\alpha(y),y)\,\alpha'(y). \tag{2.1}$$

Sind nur $f$, $\alpha$ und $\beta$ stetig, ist $F$ immer noch stetig. Für die stetige Differenzierbarkeit von $F$ genügt es, zusätzlich die Existenz und Stetigkeit von $\partial f/\partial y$, $\alpha'$ und $\beta'$ vorauszusetzen.
:::

⁠**So liest man das:** Der erste Term ist die Änderung der Kurve bei festen Grenzen, also Stufe [1](integrale-mit-parameter.html#stufe-1). Der zweite ist die Höhe am rechten Rand mal der Geschwindigkeit dieses Rands. Der dritte ist dasselbe am linken Rand, mit Minus, weil ein vorrückender linker Rand Fläche abschneidet.

:::herleitung Kettenregel und Hauptsatz
Setze $J(p,q,y):=\int_p^qf(x,y)\,\mathrm{d} x$. Dann ist $F(y)=J(\alpha(y),\beta(y),y)$. Die partiellen Ableitungen von $J$ sind:

<ul>

<li>

$\partial J/\partial q=f(q,y)$ nach dem Hauptsatz.

</li>

<li>

$\partial J/\partial p=-f(p,y)$ nach dem Hauptsatz, denn $\int_p^q=-\int_q^p$.

</li>

<li>

$\partial J/\partial y=\int_p^q\partial_yf(x,y)\,\mathrm{d} x$ nach Satz [1.1](integrale-mit-parameter.html#satz-1-1).

</li>

</ul>

Alle drei sind stetig, also gilt die Kettenregel aus [Teil 1](/wissen/elektrotechnik/3-semester/hohere-mathematik-3/differentialrechnung-fur-vektorfelder/differentialrechnung-fuer-vektorfelder.html):

$$F'(y)=\frac{\partial J}{\partial p}\,\alpha'(y)+\frac{\partial J}{\partial q}\,\beta'(y)+\frac{\partial J}{\partial y}.$$

Einsetzen gibt [(2.1)](#gl-2-1). Die Stetigkeit von $F'$ folgt aus der Stetigkeit aller drei Terme.
:::

**Beispiel.** Bei $F(y)=\int_0^y\mathrm{e}^{-xy}\,\mathrm{d} x$ für $y>0$ ist $y$ zugleich Dämpfung und obere Grenze. Mit $\alpha=0$ und $\beta(y)=y$ gibt [(2.1)](#gl-2-1)

$$F'(y)=-\int_0^yx\,\mathrm{e}^{-xy}\,\mathrm{d} x+\mathrm{e}^{-y^2}.$$

Bei $y=1$ ist das $-(1-\frac{2}{\mathrm{e}})+\frac{1}{\mathrm{e}}=\frac{3}{\mathrm{e}}-1\approx0{,}104$. Kontrolle: Es ist $F(y)=(1-\mathrm{e}^{-y^2})/y$, und Ableiten gibt bei $y=1$ denselben Wert.

⁠**Grenzfälle:** Bei festen Grenzen ist $\alpha'=\beta'=0$, es bleibt Satz [1.1](integrale-mit-parameter.html#satz-1-1). Hängt $f$ nicht von $y$ ab, bleibt $F'=f(\beta)\beta'-f(\alpha)\alpha'$, das ist der Hauptsatz mit Kettenregel. Bei $\alpha=\beta$ ist $F=0$, und die beiden Randterme heben sich auf.

⁠**Warum differenzierbare Grenzen?** $F(y)=\int_0^{|y|}1\,\mathrm{d} x=|y|$ ist stetig, aber bei $y=0$ nicht differenzierbar. Der Knick steckt in der Grenze $\beta(y)=|y|$.

In der Elektrotechnik hat die Antwort eines Systems, das zur Zeit null eingeschaltet wird, genau diese Bauart: Die Zeit steckt im Integranden und in der oberen Grenze.

:::frage Warum nicht erst das Integral ausrechnen und dann ableiten?
Das geht und gibt dasselbe, wenn es eine Stammfunktion in geschlossener Form gibt. Die Regel hilft im anderen Fall. In Aufgabe [3](#aufg-3) gibt es für den Integranden keine elementare Stammfunktion, die Ableitung von $F$ lässt sich trotzdem angeben.
:::

:::aufgabe Aufgabe 3 ★ Ableiten ohne Stammfunktion
<span class="anker" id="aufg-3"></span>

Sei $F(y)=\int_y^{y^2}\frac{\mathrm{e}^{xy}}{x}\,\mathrm{d} x$ für $y\ge1$. Berechne $F'(y)$ als geschlossenen Ausdruck. Welchen Wert hat $F'(1)$?

:::loesung
Mit $\alpha(y)=y$, $\beta(y)=y^2$ und $f=\mathrm{e}^{xy}/x$ ist $\partial_yf=\mathrm{e}^{xy}$. Auf $D$ ist $x\ge1$, also ist $f$ dort stetig differenzierbar. Aus [(2.1)](#gl-2-1):

$$F'(y)=\int_y^{y^2}\mathrm{e}^{xy}\,\mathrm{d} x+\frac{\mathrm{e}^{y^3}}{y^2}\,2y-\frac{\mathrm{e}^{y^2}}{y}=\frac{\mathrm{e}^{y^3}-\mathrm{e}^{y^2}}{y}+\frac{2\mathrm{e}^{y^3}}{y}-\frac{\mathrm{e}^{y^2}}{y}=\frac{3\mathrm{e}^{y^3}-2\mathrm{e}^{y^2}}{y}.$$

Bei $y=1$ ist $F'(1)=\mathrm{e}$.
:::
:::
