---
title: Stufe 7: Verformen und zweiter Hauptsatz
pfad: Elektrotechnik / 3. Semester / Höhere Mathematik 3 / Kurvenintegrale
order: 3130800
summary: Sterngebiete sind nicht die einzigen Gebiete, auf denen rotboldsymbol F =0 reicht.
tags: Homotopie, Homotopie geschlossener Kurven, Homotopie mit festen Endpunkten, einfach zusammenhängend, Argumentfunktion
lang: de
---

<span class="anker" id="stufe-7"></span>

:::zweck
Sterngebiete sind nicht die einzigen Gebiete, auf denen $\operatorname{rot}\boldsymbol{F}=0$ reicht. Diese Stufe findet die genaue Bedingung: Jede geschlossene Kurve muss sich im Gebiet auf einen Punkt zusammenziehen lassen.
:::

**Die Idee.** Verformt man eine Kurve stetig innerhalb des Gebiets, ändert sich das Kurvenintegral eines Felds mit Integrabilitätsbedingungen nicht. Lässt sich eine geschlossene Kurve auf einen Punkt zusammenziehen, hat sie also dasselbe Integral wie ein Punkt, nämlich null. Ein Loch kann das verhindern (Abb. [7](#abb-7)).

:::abbildung hm3/k3homotopie 7
Links eine Verformung mit festen Endpunkten von $\gamma_0$ nach $\gamma_1$. Rechts die Ebene ohne Nullpunkt: Eine geschlossene Kurve neben dem Loch lässt sich auf einen Punkt zusammenziehen, eine um das Loch nicht.
:::

Eine __Homotopie__ ist eine stetige Abbildung $\boldsymbol h:[0,1]\times[a,b]\to\mathcal U$. Für jedes feste $v$ ist $\gamma_v(t)=\boldsymbol h(v,t)$ eine Kurve. Läuft der Verformungsparameter $v$ von 0 bis 1, geht $\gamma_0$ stetig in $\gamma_1$ über.

:::satz Satz 7.1 (Vertauschungsregel)
<span class="anker" id="satz-7-1"></span>

Sei $\mathcal U\subset\mathbb{R}^n$ offen, $\boldsymbol h$ zweimal stetig differenzierbar und $\boldsymbol{F}$ stetig differenzierbar auf $\mathcal U$ mit Integrabilitätsbedingungen. Dann gilt

<span class="anker" id="gl-7-1"></span>
$$\frac{\partial}{\partial v}\Bigl(\boldsymbol{F}(\boldsymbol h)\cdot\frac{\partial\boldsymbol h}{\partial t}\Bigr)=\frac{\partial}{\partial t}\Bigl(\boldsymbol{F}(\boldsymbol h)\cdot\frac{\partial\boldsymbol h}{\partial v}\Bigr). \tag{7.1}$$
:::

:::beweis Vertauschungsregel
Die Produkt- und Kettenregel geben links $\sum_{j,k}\frac{\partial F_j}{\partial x_k}\frac{\partial h_k}{\partial v}\frac{\partial h_j}{\partial t}+\boldsymbol{F}\cdot\frac{\partial^2\boldsymbol h}{\partial v\,\partial t}$ und rechts dasselbe mit $v,t$ getauscht. Die zweiten Ableitungen von $\boldsymbol h$ sind nach Schwarz gleich. In der Summe rechts benennt man $j,k$ um, und die Integrabilitätsbedingung $\partial F_j/\partial x_k=\partial F_k/\partial x_j$ macht sie zur Summe links.
:::

Mit Ableiten unter dem Integral, dieser Regel und dem Hauptsatz in $t$ folgt für die Kurvenschar

<span class="anker" id="gl-7-2"></span>
$$\begin{aligned} \frac{\mathrm{d}}{\mathrm{d} v}\int_{\gamma_v}\boldsymbol{F}\cdot\mathrm{d}\boldsymbol{x}&=\int_a^b\frac{\partial}{\partial v}\Bigl(\boldsymbol{F}(\boldsymbol h)\cdot\frac{\partial\boldsymbol h}{\partial t}\Bigr)\mathrm{d} t=\int_a^b\frac{\partial}{\partial t}\Bigl(\boldsymbol{F}(\boldsymbol h)\cdot\frac{\partial\boldsymbol h}{\partial v}\Bigr)\mathrm{d} t\\ &=\Bigl[\boldsymbol{F}(\boldsymbol h(v,t))\cdot\frac{\partial\boldsymbol h}{\partial v}(v,t)\Bigr]_{t=a}^{b}. \end{aligned} \tag{7.2}$$

Die Änderung des Integrals ist also reiner Randterm. Er verschwindet in zwei Fällen:

<ol class="rm">

<li>

__Homotopie geschlossener Kurven__: $\boldsymbol h(v,a)=\boldsymbol h(v,b)$ für alle $v$. Beide Enden laufen gemeinsam, also ist auch $\frac{\partial\boldsymbol h}{\partial v}(v,a)=\frac{\partial\boldsymbol h}{\partial v}(v,b)$, und die beiden Randwerte heben sich auf.

</li>

<li>

__Homotopie mit festen Endpunkten__: $\frac{\partial\boldsymbol h}{\partial v}(v,a)=\frac{\partial\boldsymbol h}{\partial v}(v,b)=0$ für alle $v$. Die Enden bewegen sich nicht.

</li>

</ol>

:::satz Satz 7.2 (Homotopieinvarianz)
<span class="anker" id="satz-7-2"></span>

Für Vektorfelder mit Integrabilitätsbedingungen ändert sich das Kurvenintegral nicht unter (i) Homotopien geschlossener Kurven und (ii) Homotopien mit festen Endpunkten. Es gilt also $\int_{\gamma_0}\boldsymbol{F}\cdot\mathrm{d}\boldsymbol{x}=\int_{\gamma_1}\boldsymbol{F}\cdot\mathrm{d}\boldsymbol{x}$.
:::

⁠**Beispiel:** $\boldsymbol h(v,t)=\bigl((1-v)R_0+vR_1\bigr)(\cos t,\sin t)$ verformt den Kreis $K_{R_0}$ in $\mathbb{R}^2\setminus\{0\}$ in den Kreis $K_{R_1}$. Deshalb hängt [(4.2)](wann-nur-start-und-ziel-zahlen.html#gl-4-2) nicht von $R$ ab.

:::definition Definition 7.3 (Einfach zusammenhängend)
<span class="anker" id="satz-7-3"></span>

Ein Gebiet $\mathcal G\subset\mathbb{R}^n$ heißt __einfach zusammenhängend__, wenn es zu jeder geschlossenen stetigen Kurve $\gamma:[a,b]\to\mathcal G$ eine stetige Homotopie geschlossener Kurven $\boldsymbol h:[0,1]\times[a,b]\to\mathcal G$ gibt mit $\boldsymbol h(0,t)=\gamma(t)$ und $\boldsymbol h(1,t)=\text{konst}$ für alle $t$.
:::

⁠**So liest man das:** Jede geschlossene Kurve lässt sich im Gebiet auf einen Punkt zusammenziehen und bleibt dabei geschlossen. Das ist wichtig, denn sonst könnte man jede Kurve von ihrem Ende her auf den Startpunkt einrollen. In der Ebene heißt es anschaulich: keine Löcher. Ringe und $\mathbb{R}^2\setminus\{0\}$ sind nicht einfach zusammenhängend, die geschlitzte Ebene schon. Im Raum täuscht das Wort Loch: $\mathbb{R}^3\setminus\{0\}$ ist einfach zusammenhängend, denn eine Kurve lässt sich am fehlenden Punkt vorbeiziehen.

:::frage Hat eine einfache Kurve etwas mit einem einfach zusammenhängenden Gebiet zu tun?
Nein, die beiden teilen nur das Wort. *Einfach* ist eine Eigenschaft einer Kurve: kein Doppelpunkt, $\gamma(s)=\gamma(t)$ mit $s<t$ nur für $s=a$, $t=b$ (Stufe [1](kurven-beschreiben-und-messen.html#stufe-1)). *Einfach zusammenhängend* ist eine Eigenschaft eines Gebiets: Alle geschlossenen Kurven darin lassen sich zusammenziehen, auch solche mit Doppelpunkten. Beides ist unabhängig voneinander. Der Einheitskreis ist eine einfache Kurve im Gebiet $\mathbb{R}^2\setminus\{0\}$, das nicht einfach zusammenhängend ist. Die Acht ist keine einfache Kurve im einfach zusammenhängenden $\mathbb{R}^2$.
:::

:::satz Satz 7.4 (Sterngebiete)
<span class="anker" id="satz-7-4"></span>

Sterngebiete sind einfach zusammenhängend.
:::

Ist $\gamma$ geschlossen und $\boldsymbol{x}_0$ Sternzentrum, zieht $\boldsymbol h(v,t):=(1-v)\gamma(t)+v\,\boldsymbol{x}_0$ die Kurve geradlinig auf $\boldsymbol{x}_0$ zusammen. Alle Zwischenpunkte liegen auf Strecken von $\boldsymbol{x}_0$ aus, also in $\mathcal G$, und jede Zwischenkurve bleibt geschlossen.

:::satz Satz 7.5 (Zweiter Hauptsatz für Kurvenintegrale)
<span class="anker" id="satz-7-5"></span>

Sei $\mathcal G\subset\mathbb{R}^n$ einfach zusammenhängend und $\boldsymbol{F}$ stetig differenzierbar auf $\mathcal G$. Dann gilt: $\boldsymbol{F}$ ist konservativ $\iff$ $\boldsymbol{F}$ erfüllt die Integrabilitätsbedingungen.
:::

:::beweis Zweiter Hauptsatz
„$\Rightarrow$“: Konservativ heißt $\boldsymbol{F}=\nabla\varphi$, und nach [Teil 1](/wissen/elektrotechnik/3-semester/hohere-mathematik-3/differentialrechnung-fur-vektorfelder/differentialrechnung-fuer-vektorfelder.html) ist die Jacobi-Matrix dann symmetrisch. „$\Leftarrow$“: Sei $\gamma$ regulär parametrisiert und geschlossen. Nach Voraussetzung gibt es eine Homotopie geschlossener Kurven von $\gamma$ auf eine konstante Kurve $\gamma_1$, und dort ist $\int_{\gamma_1}\boldsymbol{F}\cdot\mathrm{d}\boldsymbol{x}=0$. Ist $\boldsymbol h$ zweimal stetig differenzierbar, folgt $\int_\gamma\boldsymbol{F}\cdot\mathrm{d}\boldsymbol{x}=0$ aus Satz [7.2](#satz-7-2). Den allgemeinen Fall führt man durch Glätten von $\boldsymbol h$ darauf zurück. Satz [4.2](wann-nur-start-und-ziel-zahlen.html#satz-4-2) gibt die Behauptung.
:::

⁠**So liest man das:** Der Satz verallgemeinert das Poincaré-Lemma für Gradientenfelder, denn jedes Sterngebiet ist einfach zusammenhängend. Er schließt die Lücke aus Stufe [4](wann-nur-start-und-ziel-zahlen.html#stufe-4). Dort fehlte die Umkehrung, und $\boldsymbol{H}$ auf $\mathbb{R}^2\setminus\{0\}$ zeigt, dass man auf den einfachen Zusammenhang nicht verzichten kann. Nimmt man die geschlitzte Ebene, gibt es das Potential: die __Argumentfunktion__, der Winkel mit Werten in $(-\pi,\pi)$,

<span class="anker" id="gl-7-3"></span>
$$\varphi(x,y)=\begin{cases}\arctan(y/x)&x>0\\\frac\pi2-\arctan(x/y)&x\le0,\;y>0\\-\frac\pi2-\arctan(x/y)&x\le0,\;y<0\end{cases},\qquad\nabla\varphi=\boldsymbol{H}. \tag{7.3}$$

Auf $\mathbb{R}^2\setminus\{0\}$ lässt sie sich nicht stetig fortsetzen: Am negativen $x$-Strahl springt sie um $2\pi$. Das ist der Wert aus [(4.2)](wann-nur-start-und-ziel-zahlen.html#gl-4-2), der Winkel wächst bei einem Umlauf um $2\pi$.

:::aufgabe Aufgabe 8 ★ Gebiete einordnen
<span class="anker" id="aufg-8"></span>

Skizziere die Mengen. Welche sind wegzusammenhängend, welche Sterngebiete, welche einfach zusammenhängend?

<ol class="al">

<li>

$\{(x,y):y>0\}$

</li>

<li>

$\{(x,y):x\neq0\}$

</li>

<li>

$\{(x,y):1<x^2+y^2<9\}$

</li>

<li>

derselbe Ring ohne die Strecke $\{(x,0):1<x<3\}$

</li>

<li>

$\mathbb{R}^3$ ohne die $z$-Achse

</li>

</ol>

:::loesung
(a) Halbebene: konvex, also alles drei. (b) Zwei getrennte Halbebenen: nicht wegzusammenhängend, also kein Gebiet und kein Sterngebiet. (c) Ring: wegzusammenhängend, kein Sterngebiet, nicht einfach zusammenhängend. (d) Aufgeschnittener Ring: wegzusammenhängend, einfach zusammenhängend, denn keine Kurve kann mehr um das Loch laufen. Kein Sterngebiet, von keinem Punkt aus sieht man alles. Der Satz über Sterngebiete lässt sich also nicht umkehren. (e) Wegzusammenhängend, kein Sterngebiet, nicht einfach zusammenhängend: Ein Kreis um die Achse lässt sich nicht zusammenziehen.
:::
:::

:::aufgabe Aufgabe 9 ★★ Vorhersagen statt rechnen
<span class="anker" id="aufg-9"></span>

Bestimme ohne Integral den Wert von $\oint\boldsymbol{H}\cdot\mathrm{d}\boldsymbol{x}$ für

<ol class="al">

<li>

die Ellipse $(2\cos t,\sin t)$, $0\le t\le2\pi$. Gib eine Homotopie zum Einheitskreis an.

</li>

<li>

den Kreis mit Radius 1 um $(3,0)$,

</li>

<li>

den zweimal durchlaufenen Einheitskreis.

</li>

</ol>

:::loesung
(a) $\boldsymbol h(v,t)=((2-v)\cos t,\,\sin t)$ ist eine Homotopie geschlossener Kurven in $\mathbb{R}^2\setminus\{0\}$, denn $\cos t$ und $\sin t$ sind nie zugleich null. $\boldsymbol{H}$ erfüllt die Integrabilitätsbedingungen, also bleibt der Wert des Einheitskreises: $2\pi$. (b) $0$. Der Kreis läuft nicht um den Nullpunkt, in der Halbebene $x>0$ lässt er sich zusammenziehen. (c) $4\pi$, denn nach Stufe [2](das-kurvenintegral.html#stufe-2) addieren sich die beiden Umläufe.
:::
:::
