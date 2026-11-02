---
title: Stufe 5: Über Quader integrieren
pfad: Elektrotechnik / 3. Semester / Höhere Mathematik 3 / Integralrechnung im Rⁿ
order: 3120700
summary: Eine Funktion auf einem Rechteck lässt sich erst nach x und dann nach y integrieren oder umgekehrt.
tags: Quader, iteriertes Integral, Mehrfachintegral, Volumenintegral
lang: de
---

<span class="anker" id="stufe-5"></span>

:::zweck
Eine Funktion auf einem Rechteck lässt sich erst nach $x$ und dann nach $y$ integrieren oder umgekehrt. Diese Stufe zeigt, dass beides existiert und dasselbe ergibt. Damit ist das Mehrfachintegral erklärt.
:::

**Die Idee.** Der Graph von $f$ über einem Rechteck ist ein Gebirge. Das Volumen darunter findet man in Scheiben: Bei festem $y$ gibt $\int f\,\mathrm{d} x$ die Fläche einer Scheibe quer zur $y$-Achse. Summiert man diese Flächen über $y$, entsteht das Volumen. Schneidet man quer zur $x$-Achse, sollte dasselbe herauskommen (Abb. [5](#abb-5)). Das Bild macht es glaubhaft, beweisen muss man es aber mit Stufe [1](integrale-mit-parameter.html#stufe-1).

:::abbildung hm3/k2fubini 5
Dasselbe Gebirge über demselben Rechteck, in zwei Richtungen geschnitten. Links ist $y$ fest, die Scheibe hat die Fläche $\int f\,\mathrm{d} x$. Rechts ist $x$ fest, die Scheibe hat die Fläche $\int f\,\mathrm{d} y$.
:::

Sei $Q=[a_1,b_1]\times\dots\times[a_n,b_n]$ ein $n$-dimensionaler __Quader__ und $f:Q\to\mathbb{R}$ stetig. Es liegt nahe, nacheinander nach allen Variablen zu integrieren:

<span class="anker" id="gl-5-1"></span>
$$\int_{a_n}^{b_n}\Bigl(\cdots\int_{a_2}^{b_2}\Bigl(\int_{a_1}^{b_1}f(x_1,\dots,x_n)\,\mathrm{d} x_1\Bigr)\mathrm{d} x_2\cdots\Bigr)\mathrm{d} x_n. \tag{5.1}$$

Das ist ein __iteriertes Integral__. Jeder Schritt nimmt eine Variable weg, also genügt es, zwei Variablen zu betrachten. **Existenz:** Für stetiges $f:[a,b]\times[c,d]\to\mathbb{R}$ ist $F(y)=\int_a^bf(x,y)\,\mathrm{d} x$ nach Stufe [1](integrale-mit-parameter.html#stufe-1) stetig auf $[c,d]$. Also existiert $\int_c^d\bigl(\int_a^bf(x,y)\,\mathrm{d} x\bigr)\mathrm{d} y=\int_c^dF(y)\,\mathrm{d} y$. Offen ist nur noch die Reihenfolge.

:::satz Satz 5.1 (Satz von Fubini)
<span class="anker" id="satz-5-1"></span>

Für stetige Funktionen $f:[a,b]\times[c,d]\to\mathbb{R}$ gilt

<span class="anker" id="gl-5-2"></span>
$$\int_c^d\Bigl(\int_a^bf(x,y)\,\mathrm{d} x\Bigr)\mathrm{d} y=\int_a^b\Bigl(\int_c^df(x,y)\,\mathrm{d} y\Bigr)\mathrm{d} x. \tag{5.2}$$

Entsprechendes gilt in beliebigen Dimensionen.
:::

⁠**So liest man das:** Links ist $y$ die äußere Variable, rechts $x$. Das innere Integral behandelt die äußere Variable als Parameter. Voraussetzungen sind die Stetigkeit von $f$ und das kompakte Rechteck. Mit Modellzahlen: Auf $[0,1]\times[-1,1]$ ist $f(x,y)=4-x^2-y^2$ die Höhe der Kuppel.

:::beweis Beide Reihenfolgen haben dieselbe Ableitung
⁠**Schritt 1: Hilfsfunktion.** Für $(p,q)\in[a,b]\times[c,d]$ setze

$$w(p,q):=\int_a^p\Bigl(\int_c^qf(x,y)\,\mathrm{d} y\Bigr)\mathrm{d} x-\int_c^q\Bigl(\int_a^pf(x,y)\,\mathrm{d} x\Bigr)\mathrm{d} y.$$

Das sind die zwei Reihenfolgen mit variablen oberen Grenzen. Zu zeigen ist $w(b,d)=0$.

⁠**Schritt 2: Ableiten nach $p$.** Im ersten Term ist $p$ die obere Grenze, und der innere Ausdruck ist stetig in $x$. Der Hauptsatz gibt $\int_c^qf(p,y)\,\mathrm{d} y$. Im zweiten Term ist $p$ Parameter eines Integrals über $y$. Sein Integrand $\int_a^pf(x,y)\,\mathrm{d} x$ hat nach dem Hauptsatz die stetige Ableitung $f(p,y)$, und Stufe [1](integrale-mit-parameter.html#stufe-1) erlaubt das Ableiten unter dem Integral. Das gibt ebenfalls $\int_c^qf(p,y)\,\mathrm{d} y$. Also ist $\partial w/\partial p=0$.

⁠**Schritt 3: Ableiten nach $q$.** Mit vertauschten Rollen folgt genauso $\partial w/\partial q=0$.

⁠**Schritt 4: Schluss.** Also ist $w$ konstant auf dem Rechteck. Bei $(p,q)=(a,c)$ sind beide Integrale leer, also ist $w=0$ und damit $w(b,d)=0$. In höheren Dimensionen tauscht man je zwei benachbarte Variablen und hält die übrigen fest.
:::

**Beispiel.** Über $Q=[0,1]\times[-1,1]$ ist die Kuppelhöhe $4-x^2-y^2$. Erst nach $x$:

$$\int_{-1}^1\Bigl(\int_0^1(4-x^2-y^2)\,\mathrm{d} x\Bigr)\mathrm{d} y=\int_{-1}^1\Bigl(\frac{11}3-y^2\Bigr)\mathrm{d} y=\frac{20}3.$$

Erst nach $y$: $\int_0^1\bigl(\frac{22}3-2x^2\bigr)\mathrm{d} x=\frac{20}3$. Grob passt das: Die Fläche ist 2, die Höhe liegt zwischen 2 und 4. **Grenzfall:** Für $f\equiv1$ geben beide Reihenfolgen die Rechteckfläche $(b-a)(d-c)$.

**Die Reihenfolge wählen.** Die Wahl kann viel Arbeit sparen. Bei $\int_0^2\int_0^1y\,\mathrm{e}^{xy}\,\mathrm{d} x\,\mathrm{d} y$ kürzt sich innen das $y$ gegen die Stammfunktion, es entsteht $\int_0^2(\mathrm{e}^y-1)\,\mathrm{d} y=\mathrm{e}^2-3\approx4{,}39$. Erst nach $y$ wäre partielle Integration nötig.

:::definition Definition 5.2 (Mehrfachintegral)
<span class="anker" id="satz-5-2"></span>

Sei $Q=[a_1,b_1]\times\dots\times[a_n,b_n]$ und $f:Q\to\mathbb{R}$ stetig. Das iterierte Integral [(5.1)](#gl-5-1) heißt __Mehrfachintegral__ von $f$ über $Q$ und wird $\int_Qf(\boldsymbol{x})\,\mathrm{d}\boldsymbol{x}$ geschrieben.
:::

Statt $\mathrm{d}\boldsymbol{x}$ schreibt man auch $\mathrm{d}^n\boldsymbol{x}$, $\mathrm{d} x_1\dots\mathrm{d} x_n$ oder $\mathrm{d}(x_1,\dots,x_n)$. Für $n=3$ heißt es oft __Volumenintegral__, mit den Schreibweisen $\iiint_Qf(x,y,z)\,\mathrm{d} x\,\mathrm{d} y\,\mathrm{d} z=\iiint_Qf(x,y,z)\,\mathrm{d} V$.

:::satz Satz 5.3 (Linearität und Monotonie)
<span class="anker" id="satz-5-3"></span>

Für stetige $f_1,f_2$ auf dem endlichen Quader $Q$ und $\lambda_1,\lambda_2\in\mathbb{R}$ gilt

$$\int_Q(\lambda_1f_1+\lambda_2f_2)\,\mathrm{d}\boldsymbol{x}=\lambda_1\int_Qf_1\,\mathrm{d}\boldsymbol{x}+\lambda_2\int_Qf_2\,\mathrm{d}\boldsymbol{x},\qquad\int_Qf_1\,\mathrm{d}\boldsymbol{x}\le\int_Qf_2\,\mathrm{d}\boldsymbol{x}\ \text{ falls }f_1\le f_2\text{ in }Q.$$

Insbesondere gilt mit dem Volumen $|Q|:=(b_1-a_1)\cdots(b_n-a_n)$

<span class="anker" id="gl-5-3"></span>
$$\Bigl|\int_Qf(\boldsymbol{x})\,\mathrm{d}\boldsymbol{x}\Bigr|\le|Q|\,\sup_{\boldsymbol{x}\in Q}|f(\boldsymbol{x})|. \tag{5.3}$$
:::

⁠**So liest man das:** Das Mehrfachintegral rechnet sich wie ein Integral einer Variablen, denn beide Eigenschaften übertragen sich Schritt für Schritt durch das iterierte Integral. $|Q|$ ist das Volumen des Quaders, $\sup_Q|f|$ der größte Betrag von $f$. Für [(5.3)](#gl-5-3) integriert man $-S\le f\le S$ mit $S=\sup_Q|f|$ und benutzt $\int_QS\,\mathrm{d}\boldsymbol{x}=S\,|Q|$. Im Beispiel oben ist $S=4$ und $|Q|=2$, die Schranke $8$ liegt über $\frac{20}3$.

:::frage Gilt Fubini immer, wenn beide iterierten Integrale existieren?
Nein. Für $f(x,y)=\frac{x^2-y^2}{(x^2+y^2)^2}$ auf $(0,1]^2$ ist $f=\partial_y\frac{y}{x^2+y^2}$. Das gibt $\int_0^1f\,\mathrm{d} y=\frac1{1+x^2}$ und $\int_0^1\bigl(\int_0^1f\,\mathrm{d} y\bigr)\mathrm{d} x=\frac\pi4$. Wegen $f(x,y)=-f(y,x)$ ist die andere Reihenfolge $-\frac\pi4$. $f$ ist bei $(0,0)$ nicht stetig fortsetzbar, sondern unbeschränkt. Dort steckt zu viel positive und negative Masse, und die Reihenfolge entscheidet, was sich zuerst aufhebt.
:::

:::aufgabe Aufgabe 7 ★★ Die günstige Reihenfolge
<span class="anker" id="aufg-7"></span>

<ol class="al">

<li>

Berechne $\int_0^1\int_0^1\frac{y}{1+xy}\,\mathrm{d} x\,\mathrm{d} y$. Welche Reihenfolge ist bequemer?

</li>

<li>

Berechne $\int_0^1\frac{t^3-t}{\ln t}\,\mathrm{d} t$. Tipp: $\frac{t^3-t}{\ln t}=\int_1^3t^y\,\mathrm{d} y$.

</li>

</ol>

:::loesung
(a) Der Integrand ist stetig. Erst nach $x$: $\int_0^1\frac{y}{1+xy}\,\mathrm{d} x=\ln(1+y)$, und $\int_0^1\ln(1+y)\,\mathrm{d} y=2\ln2-1\approx0{,}386$. Erst nach $y$ wäre Partialbruchzerlegung nötig. (b) Für $0<t<1$ ist $\int_1^3t^y\,\mathrm{d} y=\bigl[\frac{t^y}{\ln t}\bigr]_1^3=\frac{t^3-t}{\ln t}$. $(t,y)\mapsto t^y$ ist auf $[0,1]\times[1,3]$ stetig, Fubini gilt also:

$$\int_0^1\frac{t^3-t}{\ln t}\,\mathrm{d} t=\int_1^3\Bigl(\int_0^1t^y\,\mathrm{d} t\Bigr)\mathrm{d} y=\int_1^3\frac{\mathrm{d} y}{1+y}=\ln\frac42=\ln2.$$
:::
:::

:::aufgabe Aufgabe 8 ★★ Wenn das Rechteck unendlich lang ist
<span class="anker" id="aufg-8"></span>

Sei $f(x,y)=(3-xy)(xy)^2\mathrm{e}^{-xy}$ auf $[0,1]\times[0,\infty)$.

<ol class="al">

<li>

Zeige $f=\partial_x\bigl(x^3y^2\mathrm{e}^{-xy}\bigr)=\partial_y\bigl(x^2y^3\mathrm{e}^{-xy}\bigr)$.

</li>

<li>

Berechne $\int_0^\infty\bigl(\int_0^1f\,\mathrm{d} x\bigr)\mathrm{d} y$ und $\int_0^1\bigl(\int_0^\infty f\,\mathrm{d} y\bigr)\mathrm{d} x$.

</li>

<li>

Warum widerspricht das Ergebnis nicht dem Satz von Fubini?

</li>

</ol>

:::loesung
(a) Beide Ableitungen geben $3x^2y^2\mathrm{e}^{-xy}-x^3y^3\mathrm{e}^{-xy}=(3-xy)(xy)^2\mathrm{e}^{-xy}$. (b) $\int_0^1f\,\mathrm{d} x=\bigl[x^3y^2\mathrm{e}^{-xy}\bigr]_{x=0}^1=y^2\mathrm{e}^{-y}$, und $\int_0^\infty y^2\mathrm{e}^{-y}\,\mathrm{d} y=\Gamma(3)=2$. Für $x>0$ ist $\int_0^\infty f\,\mathrm{d} y=\bigl[x^2y^3\mathrm{e}^{-xy}\bigr]_{y=0}^\infty=0$, für $x=0$ ist $f=0$. Die zweite Reihenfolge gibt also 0. (c) Fubini verlangt ein kompaktes Rechteck, hier ist der $y$-Bereich unbeschränkt. Für kleine $x$ sitzt die Masse von $f$ weit draußen bei $y\sim1/x$ und entzieht sich jeder festen Schranke.
:::
:::
