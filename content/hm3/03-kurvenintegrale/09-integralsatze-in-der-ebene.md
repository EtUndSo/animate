---
title: Stufe 8: Integralsätze in der Ebene
pfad: Elektrotechnik / 3. Semester / Höhere Mathematik 3 / Kurvenintegrale
order: 3130900
summary: Für rotboldsymbol F =0 verschwinden Umläufe.
tags: regulärer Bereich, positiv orientiert, Greensche Formel, Zirkulation, äußeres Einheitsnormalenfeld, Fluss, Quellendichte, Wirbeldichte
lang: de
---

<span class="anker" id="stufe-8"></span>

:::zweck
Für $\operatorname{rot}\boldsymbol{F}=0$ verschwinden Umläufe. Diese Stufe sagt, was ein Umlauf für allgemeine Felder ergibt: das Integral von $\operatorname{rot}\boldsymbol{F}$ über die umlaufene Fläche. Daraus folgt die genaue Bedeutung von $\operatorname{div}$ und $\operatorname{rot}$.
:::

**Die Idee.** Teile eine Fläche in kleine Zellen und laufe um jede einmal herum. Auf einer gemeinsamen Kante zweier Zellen laufen beide Umläufe gegeneinander, ihre Beiträge heben sich auf. Übrig bleibt der äußere Rand. Dafür muss der Rand richtig orientiert sein (Abb. [8](#abb-8)).

:::abbildung hm3/k3rand 8
Links der Rand eines Normalbereichs $D$ aus vier Stücken, positiv orientiert: $D$ liegt immer links. Rechts ein Ring: Außen läuft der Rand gegen, innen im Uhrzeigersinn. Am Rand zeigt $\boldsymbol{t}$ in Laufrichtung, $\boldsymbol\nu$ aus $D$ heraus.
:::

:::definition Definition 8.1 (Regulärer Bereich, positiver Rand)
<span class="anker" id="satz-8-1"></span>

Ein __regulärer Bereich__ $D\subset\mathbb{R}^2$ ist eine beschränkte und abgeschlossene Menge, deren Inneres zusammenhängend ist und deren Rand aus endlich vielen geschlossenen regulären Kurven besteht. Der Rand $\partial D$ heißt __positiv orientiert__, wenn alle Randkurven so orientiert sind, dass längs der Durchlaufrichtung das Innere von $D$ links liegt.
:::

Bei einer Kreisscheibe läuft der Rand also gegen den Uhrzeigersinn. Bei einem Ring läuft der äußere Kreis gegen und der innere im Uhrzeigersinn.

:::satz Satz 8.2 (Green: Stokesscher Integralsatz in der Ebene)
<span class="anker" id="satz-8-2"></span>

Sei $D\subset\mathbb{R}^2$ ein regulärer Bereich mit positiv orientiertem Rand und $\boldsymbol{F}:\mathcal U\to\mathbb{R}^2$ stetig differenzierbar in einer Umgebung $\mathcal U\supset D$. Dann gilt

<span class="anker" id="gl-8-1"></span>
$$\int_D\operatorname{rot}\boldsymbol{F}(\boldsymbol{x})\,\mathrm{d}\boldsymbol{x}=\int_{\partial D}\boldsymbol{F}\cdot\mathrm{d}\boldsymbol{x}. \tag{8.1}$$

In den Komponenten $F_1=P$, $F_2=Q$ ist das die __Greensche Formel__

<span class="anker" id="gl-8-2"></span>
$$\int_D\Bigl(\frac{\partial Q}{\partial x}-\frac{\partial P}{\partial y}\Bigr)\mathrm{d} x\,\mathrm{d} y=\int_{\partial D}P\,\mathrm{d} x+Q\,\mathrm{d} y. \tag{8.2}$$
:::

⁠**So liest man das:** Links steht die summierte Wirbelstärke, rechts die __Zirkulation__, also die Arbeit des Felds auf einer Runde um den Rand. **Kontrolle:** Für $\boldsymbol V$ ist $\operatorname{rot}\boldsymbol V=2$. Über die Einheitskreisscheibe ergibt die linke Seite $2\pi$, die rechte $\int_0^{2\pi}1\,\mathrm{d} t=2\pi$. **Warum die Umgebung nötig ist:** Für $\boldsymbol{H}$ auf derselben Scheibe wäre links null und rechts $2\pi$, aber $\boldsymbol{H}$ ist im Nullpunkt nicht definiert.

:::beweis Green auf einem Normalbereich
Sei $D=\{(x,y):\alpha(y)\le x\le\beta(y),\;c\le y\le d\}$ mit stetig differenzierbaren $\alpha,\beta$. Kurz steht $Q|_\beta$ für $Q(\beta(y),y)$ und $Q|_\alpha$ für $Q(\alpha(y),y)$, ebenso bei $P$. Der Hauptsatz in $x$ und die Leibnizregel geben

$$\int_D\frac{\partial Q}{\partial x}\,\mathrm{d} x\,\mathrm{d} y=\int_c^dQ|_\beta\,\mathrm{d} y-\int_c^dQ|_\alpha\,\mathrm{d} y,$$

$$\begin{aligned} \int_D\frac{\partial P}{\partial y}\,\mathrm{d} x\,\mathrm{d} y&=\int_c^d\Bigl(\frac{\mathrm{d}}{\mathrm{d} y}\int_{\alpha(y)}^{\beta(y)}P\,\mathrm{d} x-P|_\beta\,\beta'+P|_\alpha\,\alpha'\Bigr)\mathrm{d} y\\ &=\Bigl[\int_{\alpha(y)}^{\beta(y)}P\,\mathrm{d} x\Bigr]_{y=c}^{d}-\int_c^dP|_\beta\,\beta'\,\mathrm{d} y+\int_c^dP|_\alpha\,\alpha'\,\mathrm{d} y. \end{aligned}$$

Der positive Rand besteht aus vier Stücken: $\Gamma_1$ rechts aufwärts, $(\beta(y),y)$ mit $y$ von $c$ nach $d$, $\Gamma_2$ oben nach links, $(x,d)$ mit $x$ von $\beta(d)$ nach $\alpha(d)$, $\Gamma_3$ links abwärts, $(\alpha(y),y)$ mit $y$ von $d$ nach $c$, und $\Gamma_4$ unten nach rechts, $(x,c)$ mit $x$ von $\alpha(c)$ nach $\beta(c)$. Auf $\Gamma_2,\Gamma_4$ ist $\mathrm{d} y=0$, auf $\Gamma_1,\Gamma_3$ ist $\mathrm{d} x=\beta'\mathrm{d} y$ bzw. $\alpha'\mathrm{d} y$. Also gilt

$$\int_{\Gamma_1+\Gamma_3}Q\,\mathrm{d} y=\int_c^dQ|_\beta\,\mathrm{d} y-\int_c^dQ|_\alpha\,\mathrm{d} y,\qquad\int_{\Gamma_1+\Gamma_3}P\,\mathrm{d} x=\int_c^dP|_\beta\,\beta'\,\mathrm{d} y-\int_c^dP|_\alpha\,\alpha'\,\mathrm{d} y,$$

$$\int_{\Gamma_2+\Gamma_4}P\,\mathrm{d} x=-\int_{\alpha(d)}^{\beta(d)}P(x,d)\,\mathrm{d} x+\int_{\alpha(c)}^{\beta(c)}P(x,c)\,\mathrm{d} x=-\Bigl[\int_{\alpha(y)}^{\beta(y)}P\,\mathrm{d} x\Bigr]_{y=c}^{d}.$$

Subtrahiert man die beiden Flächenintegrale, stehen rechts genau diese drei Ausdrücke: $\int_D(Q_x-P_y)\,\mathrm{d} x\,\mathrm{d} y=\sum_{i=1}^4\int_{\Gamma_i}\boldsymbol{F}\cdot\mathrm{d}\boldsymbol{x}=\int_{\partial D}\boldsymbol{F}\cdot\mathrm{d}\boldsymbol{x}$. Einen allgemeinen Bereich zerlegt man in Normalbereiche. Die Schnittkanten werden zweimal gegenläufig durchlaufen und fallen weg.
:::

**Der zweite Hauptsatz aus Green.** Green liefert in der Ebene einen zweiten Beweis. Ist $\mathcal G\subset\mathbb{R}^2$ einfach zusammenhängend, ist jede einfach geschlossene reguläre Kurve bis auf die Orientierung Rand eines regulären Bereichs $D\subset\mathcal G$. Aus $\operatorname{rot}\boldsymbol{F}=0$ folgt dann mit [(8.1)](#gl-8-1), dass ihr Integral null ist. Kurven mit Doppelpunkten zerlegt man.

**Fluss statt Zirkulation.** Green zählt den Anteil von $\boldsymbol{F}$ längs des Rands. Dreht man alles um $90^\circ$, zählt der Anteil quer zum Rand.

:::definition Definition 8.3 (Äußeres Einheitsnormalenfeld)
<span class="anker" id="satz-8-3"></span>

Sei $\partial D$ positiv orientiert mit Einheitstangentenfeld $\boldsymbol{t}$. Das Feld $\boldsymbol\nu$ längs $\partial D$ mit $\boldsymbol{t}=\boldsymbol\nu^\perp$, wobei $\boldsymbol\nu^\perp=(-\nu_2,\nu_1)$, heißt __äußeres Einheitsnormalenfeld__.
:::

$\boldsymbol\nu$ ist $\boldsymbol{t}$ um $90^\circ$ im Uhrzeigersinn gedreht, zeigt also rechts vom Läufer, und links liegt $D$.

:::satz Satz 8.4 (Gauß in der Ebene)
<span class="anker" id="satz-8-4"></span>

Mit den Voraussetzungen von Satz [8.2](#satz-8-2) gilt $\displaystyle\int_D\operatorname{div}\boldsymbol{F}(\boldsymbol{x})\,\mathrm{d}\boldsymbol{x}=\int_{\partial D}\boldsymbol{F}\cdot\boldsymbol\nu\;\mathrm{d} s$.
:::

:::beweis Gauß aus Green
Sei $\boldsymbol{F}^\perp=(-F_2,F_1)$. Nach [Teil 1](/wissen/elektrotechnik/3-semester/hohere-mathematik-3/differentialrechnung-fur-vektorfelder/differentialrechnung-fuer-vektorfelder.html) ist $\operatorname{div}\boldsymbol{F}=\operatorname{rot}\boldsymbol{F}^\perp$. Drehungen erhalten das Skalarprodukt, also ist $\boldsymbol{F}\cdot\boldsymbol\nu=\boldsymbol{F}^\perp\cdot\boldsymbol\nu^\perp=\boldsymbol{F}^\perp\cdot\boldsymbol{t}$. Mit Green für $\boldsymbol{F}^\perp$ und [(2.3)](das-kurvenintegral.html#gl-2-3) folgt

$$\int_D\operatorname{div}\boldsymbol{F}\,\mathrm{d}\boldsymbol{x}=\int_D\operatorname{rot}\boldsymbol{F}^\perp\,\mathrm{d}\boldsymbol{x}=\int_{\partial D}\boldsymbol{F}^\perp\cdot\boldsymbol{t}\;\mathrm{d} s=\int_{\partial D}\boldsymbol{F}\cdot\boldsymbol\nu\;\mathrm{d} s.$$

Umgekehrt folgt Green genauso aus Gauß, beide Sätze sind gleichwertig.
:::

Rechts steht der __Fluss__, das ist die Menge, die durch den Rand nach außen strömt.

**Was div und rot bedeuten.** Für stetiges $f$ ist $f(\boldsymbol{x})=\lim_{R\searrow0}\frac{1}{|B_R(\boldsymbol{x})|}\int_{B_R(\boldsymbol{x})}f(\boldsymbol{y})\,\mathrm{d}\boldsymbol{y}$ mit $B_R(\boldsymbol{x})=\{\boldsymbol{y}:|\boldsymbol{x}-\boldsymbol{y}|<R\}$: Der Mittelwert über eine kleine Scheibe ist fast der Wert in der Mitte. Mit $f=\operatorname{div}\boldsymbol{F}$ und $f=\operatorname{rot}\boldsymbol{F}$ geben Gauß und Green Formeln ohne Koordinaten:

<span class="anker" id="gl-8-3"></span>
$$\operatorname{div}\boldsymbol{F}(\boldsymbol{x})=\lim_{R\searrow0}\frac{1}{|B_R(\boldsymbol{x})|}\int_{\partial B_R(\boldsymbol{x})}\boldsymbol{F}\cdot\boldsymbol\nu\,\mathrm{d} s,\qquad\operatorname{rot}\boldsymbol{F}(\boldsymbol{x})=\lim_{R\searrow0}\frac{1}{|B_R(\boldsymbol{x})|}\int_{\partial B_R(\boldsymbol{x})}\boldsymbol{F}\cdot\boldsymbol{t}\,\mathrm{d} s. \tag{8.3}$$

$\operatorname{div}\boldsymbol{F}$ ist also Fluss pro Fläche, die __Quellendichte__. $\operatorname{rot}\boldsymbol{F}$ ist Zirkulation pro Fläche, die __Wirbeldichte__.

**Fläche aus dem Rand.** Wählt man $P=-y/2$, $Q=x/2$, ist $\partial_xQ-\partial_yP=1$. Hat $D$ als Rand eine einzige geschlossene reguläre Kurve $\gamma:[a,b]\to\mathbb{R}^2$, positiv orientiert, gibt [(8.2)](#gl-8-2)

<span class="anker" id="gl-8-4"></span>
$$|D|=\frac12\int_a^b\bigl(\gamma_1(t)\dot\gamma_2(t)-\gamma_2(t)\dot\gamma_1(t)\bigr)\mathrm{d} t=\frac12\int_a^b\det\bigl(\gamma(t)\,|\,\dot\gamma(t)\bigr)\mathrm{d} t. \tag{8.4}$$

Ein __Planimeter__ ist ein Messgerät, das so die Fläche aus dem Abfahren des Rands bestimmt. **Beispiel:** Die Ellipse $\{x^2/a_1^2+y^2/a_2^2\le1\}$ mit dem Rand $(a_1\cos t,\,a_2\sin t)$ hat $\det(\gamma|\dot\gamma)=a_1a_2$, also die Fläche $\pi a_1a_2$. Die Fläche ist damit leicht, ihr Umfang nach Stufe [1](kurven-beschreiben-und-messen.html#stufe-1) nicht.

:::frage Mein Weg läuft im Uhrzeigersinn. Was nun?
Green gilt für den positiven Rand. Läuft der Weg andersherum, ändert sich nach Stufe [3](warum-die-parametrisierung-egal-ist.html#stufe-3) das Vorzeichen des Kurvenintegrals, also bekommt das Flächenintegral ein Minus. Prüfe die Richtung immer zuerst.
:::

:::aufgabe Aufgabe 10 ★★ Dreieck: Auf die Richtung achten
<span class="anker" id="aufg-10"></span>

Berechne $\oint_\Gamma(\mathrm{e}^{x^2}-3y)\,\mathrm{d} x+(\sin y^3+x^2)\,\mathrm{d} y$ für den Rand des Dreiecks mit den Ecken $(0,0)\to(0,2)\to(2,0)\to(0,0)$, in dieser Reihenfolge durchlaufen.

:::loesung
Hier ist $\partial_xQ-\partial_yP=2x+3$. Die Reihenfolge läuft im Uhrzeigersinn, also ist das Ergebnis das Negative des Flächenintegrals. Auf dem Dreieck $T$ ist $\int_T3\,\mathrm{d} x\,\mathrm{d} y=6$ und $\int_T2x\,\mathrm{d} x\,\mathrm{d} y=2\int_0^2x(2-x)\,\mathrm{d} x=\frac83$. Ergebnis: $-\frac{26}{3}$. Die schwierigen Terme $\mathrm{e}^{x^2}$ und $\sin y^3$ fallen weg.
:::
:::

:::aufgabe Aufgabe 11 ★★ Ring prüfen
<span class="anker" id="aufg-11"></span>

Sei $D=\{1\le x^2+y^2\le4\}$ und $\boldsymbol{F}=(x-y,\,x+y)$.

<ol class="al">

<li>

Gib beide Randkreise positiv orientiert an, dazu $\boldsymbol{t}$ und $\boldsymbol\nu$.

</li>

<li>

Prüfe Green und Gauß, indem du beide Seiten berechnest.

</li>

</ol>

:::loesung
(a) Außen $\gamma_a(t)=2(\cos t,\sin t)$ mit $\boldsymbol{t}=(-\sin t,\cos t)$ und $\boldsymbol\nu=(\cos t,\sin t)$. Innen $\gamma_i(t)=(\cos t,-\sin t)$ mit $\boldsymbol{t}=(-\sin t,-\cos t)$ und $\boldsymbol\nu=(-\cos t,\sin t)$, das zeigt zum Mittelpunkt, also aus dem Ring heraus. (b) $\operatorname{rot}\boldsymbol{F}=\operatorname{div}\boldsymbol{F}=2$ und $|D|=3\pi$, beide Flächenintegrale sind $6\pi$. Außen ist $\boldsymbol{F}\cdot\boldsymbol{t}=\boldsymbol{F}\cdot\boldsymbol\nu=2$ mit $\mathrm{d} s=2\,\mathrm{d} t$, das gibt je $8\pi$. Innen ist $\boldsymbol{F}\cdot\boldsymbol{t}=\boldsymbol{F}\cdot\boldsymbol\nu=-1$ mit $\mathrm{d} s=\mathrm{d} t$, das gibt je $-2\pi$. Summe jeweils $6\pi$.
:::
:::

:::aufgabe Aufgabe 12 ★★ Fläche aus dem Rand
<span class="anker" id="aufg-12"></span>

Berechne die Fläche, die $\gamma(t)=(2+\cos t)(\cos t,\sin t)$, $0\le t\le2\pi$, umschließt.

:::loesung
Mit $r=2+\cos t$ ist $\gamma=r(\cos t,\sin t)$, und die Terme mit $r'$ fallen weg: $\det(\gamma|\dot\gamma)=r^2$. Also

$$|D|=\frac12\int_0^{2\pi}(4+4\cos t+\cos^2t)\,\mathrm{d} t=\frac12(8\pi+0+\pi)=\frac{9\pi}{2}\approx14{,}1.$$
:::
:::
