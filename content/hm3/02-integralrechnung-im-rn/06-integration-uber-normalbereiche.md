---
title: Integration über Normalbereiche
pfad: Elektrotechnik / 3. Semester / Höhere Mathematik 3 / Integralrechnung im Rⁿ
order: 3120600
summary: Mit der Fortsetzung durch null ist das Integral über eine Menge erklärt, aber noch nicht berechenbar.
tags: Normalbereich, regulär, regulärer Bereich, Oktant
lang: de
---

<span class="anker" id="stufe-5"></span>

:::zweck
Mit der Fortsetzung durch null ist das Integral über eine Menge erklärt, aber noch nicht berechenbar. Dieser Abschnitt beschreibt Bereiche, die zwischen zwei Kurven oder zwei Flächen liegen, und führt das Integral darüber auf zwei oder drei gewöhnliche Integrale zurück.
:::

### Normalbereiche

<span class="anker" id="stufe-5-1"></span>

Wie rechnet man das Integral über eine Menge aus, die kein Rechteck ist? Am einfachsten geht es, wenn jede Gerade in einer Richtung die Menge in einem einzigen Stück durchquert.

Man zerlegt den Bereich in Streifen. Für jedes feste $x$ läuft ein senkrechter Streifen von einer unteren zur oberen Randkurve; oder für jedes feste $y$ ein waagerechter Streifen von einer linken zur rechten Randkurve (Abb. [13](#abb-13)). Es ist derselbe Gedanke wie beim iterierten Integral, nur sind die Streifen verschieden lang.

:::abbildung hm3/k2normal 13
Die Linse zwischen den Kurven $y=x^2$ und $y=x$, einmal senkrecht (links) und einmal waagerecht (rechts) in Streifen geschnitten. Links läuft $y$ bei festem $x$ von $x^2$ bis $x$, rechts läuft $x$ bei festem $y$ von $y$ bis $\sqrt y$.
:::

:::definition Definition 5.1 (Normalbereich)
<span class="anker" id="satz-5-1"></span>

Ein __Normalbereich__ im $\mathbb{R}^2$ ist eine Menge $D\subset\mathbb{R}^2$ der Form

$$\begin{aligned} \text{Typ 1:}\quad&D=\{(x,y)\in\mathbb{R}^2:\ \alpha(y)\le x\le\beta(y),\ c\le y\le d\}\quad\text{mit stetigen }\alpha,\beta\colon[c,d]\to\mathbb{R},\\ \text{Typ 2:}\quad&D=\{(x,y)\in\mathbb{R}^2:\ \mu(x)\le y\le\nu(x),\ a\le x\le b\}\quad\text{mit stetigen }\mu,\nu\colon[a,b]\to\mathbb{R} . \end{aligned}$$

Ein Normalbereich heißt __regulär__, wenn die Funktionen $\alpha$ und $\beta$ beziehungsweise $\mu$ und $\nu$ stetig differenzierbar sind.
:::

⁠**So liest man das:** Beim Typ 1 schneidet jede waagerechte Gerade $y=\text{konst}$ mit $c\le y\le d$ den Bereich in einer Strecke von $\alpha(y)$ bis $\beta(y)$. Beim Typ 2 schneidet jede senkrechte Gerade $x=\text{konst}$ mit $a\le x\le b$ den Bereich in einer Strecke von $\mu(x)$ bis $\nu(x)$. Regulär heißt: Die Randkurven haben überall eine Tangente mit endlicher Steigung, die sich stetig ändert. Ein Rechteck ist ein regulärer Normalbereich beider Typen, mit konstanten Randfunktionen.

⁠**Beispiel: Linse.** Die Menge zwischen den Kurven $y=x^2$ und $y=x$ für $0\le x\le1$. Als Typ 2 ist sie $\{x^2\le y\le x,\ 0\le x\le1\}$ mit $\mu(x)=x^2$ und $\nu(x)=x$. Als Typ 1 ist sie $\{y\le x\le\sqrt y,\ 0\le y\le1\}$ mit $\alpha(y)=y$ und $\beta(y)=\sqrt y$. Als Typ 2 ist sie regulär. Als Typ 1 ist sie es nicht, denn $\beta(y)=\sqrt y$ ist bei $y=0$ nicht differenzierbar. Ob ein Normalbereich regulär ist, hängt also von der Beschreibung ab.

:::hintergrund Wozu man Normalbereiche braucht
Das Integral über eine Menge ist mit der Fortsetzung durch null erklärt, und diese springt am Rand. Der Satz von Fubini aus Abschnitt [3](mehrfachintegrale.html#stufe-3) setzt aber stetige Integranden voraus. Ein Normalbereich löst dieses Problem durch seine Form. Bei festem $y$ besteht die Zeile des umgebenden Quaders aus drei Stücken: links von $\alpha(y)$ ist $\bar f=0$, zwischen $\alpha(y)$ und $\beta(y)$ ist $\bar f=f$, rechts von $\beta(y)$ ist wieder $\bar f=0$. Die Sprünge sitzen also genau an den Grenzen des inneren Integrals, und es bleibt das gewöhnliche Integral $\int_{\alpha(y)}^{\beta(y)}f(x,y)\,\mathrm{d} x$ einer stetigen Funktion. Nach der Leibnizregel, Satz [1.10](integrale-mit-parameter-uber-endlichen-intervallen.html#satz-1-10), im Teil für bloß stetige Funktionen, hängt es stetig von $y$ ab, und das äußere Integral existiert. Der Sprung verschwindet so aus der Rechnung. Wäre der Schnitt einer Zeile mit dem Bereich nicht eine einzige Strecke, sondern zerfiele er in mehrere Stücke, deren Zahl sich mit $y$ ändert, ginge das nicht mehr so einfach. Dann zerlegt man den Bereich in mehrere Normalbereiche.
:::

⁠**Kurz gesagt:** Ein Normalbereich liegt zwischen zwei Graphen stetiger Funktionen; jede Gerade in einer Achsenrichtung schneidet ihn in einer einzigen Strecke.

### Integration über Normalbereiche

<span class="anker" id="stufe-5-2"></span>

Über einen Normalbereich integriert man in zwei Schritten: zuerst längs jeder Strecke, dann über die Lage der Strecke.

:::satz Satz 5.2 (Integration über Normalbereiche)
<span class="anker" id="satz-5-2"></span>

Sei $D\subset\mathbb{R}^2$ ein Normalbereich und $f\colon D\to\mathbb{R}$ stetig. Dann ist das Integral von $f$ über $D$ wohldefiniert, und es gilt für den Typ 1

<span class="anker" id="gl-5-1"></span>
$$\int_Df(x,y)\,\mathrm{d} x\,\mathrm{d} y=\int_c^d\Bigl(\int_{\alpha(y)}^{\beta(y)}f(x,y)\,\mathrm{d} x\Bigr)\mathrm{d} y , \tag{5.1}$$

und entsprechend $\int_Df\,\mathrm{d} x\,\mathrm{d} y=\int_a^b\bigl(\int_{\mu(x)}^{\nu(x)}f(x,y)\,\mathrm{d} y\bigr)\mathrm{d} x$ für den Typ 2. Für $f\equiv1$ erhält man den Flächeninhalt

<span class="anker" id="gl-5-2"></span>
$$|D|=\int_c^d\ell(y)\,\mathrm{d} y\qquad\text{mit}\qquad\ell(y)=\beta(y)-\alpha(y). \tag{5.2}$$

Ferner gilt die Abschätzung

$$\Bigl|\int_Df(x,y)\,\mathrm{d} x\,\mathrm{d} y\Bigr|\le|D|\sup_{(x,y)\in D}|f(x,y)| .$$
:::

⁠**So liest man das:** Innen läuft $x$ bei festem $y$ von der linken Randkurve $\alpha(y)$ zur rechten $\beta(y)$; $\ell(y)$ ist die Länge dieser Strecke. Außen läuft $y$ zwischen den festen Zahlen $c$ und $d$. Das Ergebnis des inneren Integrals hängt noch von $y$ ab, das des äußeren nicht mehr. **Grenzfall:** Bei konstanten $\alpha$ und $\beta$ ist $D$ ein Rechteck, und [(5.1)](#gl-5-1) ist das iterierte Integral aus Abschnitt [3](mehrfachintegrale.html#stufe-3).

:::herleitung Zeile für Zeile
Man setzt $f$ wie in [(4.1)](integration-uber-mengen-und-berechnung-von-volumina.html#gl-4-1) durch null auf einen Quader $Q=[a',b']\times[c,d]$ fort, der $D$ enthält. Bei festem $y$ ist $\bar f(x,y)$ gleich $f(x,y)$ für $\alpha(y)\le x\le\beta(y)$ und sonst null. Das Integral über die Zeile des Quaders ist also $\int_{\alpha(y)}^{\beta(y)}f(x,y)\,\mathrm{d} x$. Nach der Leibnizregel, im Teil für bloß stetige Funktionen, ist das stetig in $y$; das äußere Integral existiert also. Die Abschätzung folgt wie [(3.3)](mehrfachintegrale.html#gl-3-3) aus $-S\le f\le S$ mit $S=\sup_D|f|$ und aus [(5.2)](#gl-5-2).
:::

⁠**Beispiel: Linse.** Für $f(x,y)=x$ auf der Linse, in beiden Beschreibungen:

$$\int_0^1\Bigl(\int_{x^2}^xx\,\mathrm{d} y\Bigr)\mathrm{d} x=\int_0^1(x^2-x^3)\,\mathrm{d} x=\frac1{12},\qquad\int_0^1\Bigl(\int_y^{\sqrt y}x\,\mathrm{d} x\Bigr)\mathrm{d} y=\int_0^1\frac{y-y^2}2\,\mathrm{d} y=\frac1{12} .$$

Der Flächeninhalt ist $|D|=\int_0^1(x-x^2)\,\mathrm{d} x=\frac16$. Die Abschätzung ergibt $\frac1{12}\le\frac16\cdot1$.

:::hintergrund Warum das innere Integral keine festen Grenzen haben darf
Feste Grenzen beschreiben ein Rechteck. Schreibt man $\int_0^1\int_0^1x\,\mathrm{d} y\,\mathrm{d} x$ statt $\int_0^1\int_{x^2}^xx\,\mathrm{d} y\,\mathrm{d} x$, integriert man über das ganze Quadrat, nicht über die Linse, und erhält $\frac12$ statt $\frac1{12}$. Eine Faustregel hilft: Nach dem inneren Integral darf die äußere Variable noch vorkommen, nach dem äußeren muss eine Zahl herauskommen. Die inneren Grenzen dürfen nur von äußeren Variablen abhängen, nie von der Variablen, über die gerade integriert wird.
:::

⁠**Kurz gesagt:** Über einen Normalbereich integriert man von innen nach außen; die inneren Grenzen sind die Randfunktionen der äußeren Variablen.

### Zerlegung in reguläre Normalbereiche

<span class="anker" id="stufe-5-3"></span>

Viele Bereiche sind kein einzelner regulärer Normalbereich, weil eine Randfunktion an einer Stelle eine unendliche Steigung hat. Man zerlegt sie dann in mehrere Stücke.

Gängige Integrationsbereiche $D\subset\mathbb{R}^2$ lassen sich als Vereinigung von endlich vielen regulären Normalbereichen $D_j$, $j=1,\dots,N$, darstellen, die sich höchstens längs ihrer Randkurven überlappen. Stetige Funktionen $f\colon D\to\mathbb{R}$ integriert man dann stückweise:

<span class="anker" id="gl-5-3"></span>
$$\int_Df(\boldsymbol{x})\,\mathrm{d}\boldsymbol{x}=\sum_{j=1}^N\int_{D_j}f(\boldsymbol{x})\,\mathrm{d}\boldsymbol{x} . \tag{5.3}$$

Es lässt sich zeigen, dass das Ergebnis nicht von der gewählten Zerlegung abhängt. Eine Vereinigung von endlich vielen regulären Normalbereichen heißt in diesem Kapitel ein __regulärer Bereich__.

⁠**Beispiel: Kreisscheibe.** Die Kreisscheibe $D=\{x^2+y^2\le4\}$ mit dem Radius $2$ ist ein Normalbereich vom Typ 1 mit $\alpha(y)=-\sqrt{4-y^2}$, $\beta(y)=\sqrt{4-y^2}$ und $y\in[-2,2]$. Aber $\beta'(y)=-y/\sqrt{4-y^2}$ wächst für $y\to\pm2$ über alle Grenzen: Oben und unten hat der Kreis eine waagerechte Tangente, und als Funktion von $y$ hat der Rand dort eine unendliche Steigung. Als Typ 1 ist $D$ deshalb nicht regulär. Man zerlegt (Abb. [14](#abb-14)):

<ul>

<li>

den Mittelstreifen $|y|\le\sqrt2$ als regulären Normalbereich vom Typ 1, mit denselben $\alpha$, $\beta$;

</li>

<li>

die obere Kappe $\sqrt2\le y\le\sqrt{4-x^2}$, $|x|\le\sqrt2$, als regulären Normalbereich vom Typ 2;

</li>

<li>

die untere Kappe, gespiegelt.

</li>

</ul>

Bei $|y|=\sqrt2$ hat der Rand die Steigung $\pm1$, und beide Beschreibungen haben dort endliche Ableitungen. Mit der Substitution $s=2\sin\theta$ ist

$$\int_{-\sqrt2}^{\sqrt2}\sqrt{4-s^2}\,\mathrm{d} s=\int_{-\pi/4}^{\pi/4}4\cos^2\theta\,\mathrm{d}\theta=\Bigl[2\theta+\sin(2\theta)\Bigr]_{-\pi/4}^{\pi/4}=\pi+2 .$$

Der Mittelstreifen hat nach [(5.2)](#gl-5-2) die Fläche $\int_{-\sqrt2}^{\sqrt2}2\sqrt{4-y^2}\,\mathrm{d} y=2\pi+4$. Jede Kappe hat die Fläche $\int_{-\sqrt2}^{\sqrt2}\bigl(\sqrt{4-x^2}-\sqrt2\bigr)\mathrm{d} x=(\pi+2)-4=\pi-2$. Zusammen ergibt [(5.3)](#gl-5-3) $2\pi+4+2(\pi-2)=4\pi$, den Flächeninhalt eines Kreises mit dem Radius $2$.

:::abbildung hm3/k2kreis 14
Die Kreisscheibe mit dem Radius $2$, zerlegt in drei reguläre Normalbereiche: den Mittelstreifen $|y|\le\sqrt2$ vom Typ 1 (blau) und oben und unten je eine Kappe vom Typ 2 (orange). An den Schnittlinien hat der Kreis die Steigung $\pm1$.
:::

⁠**Kurz gesagt:** Bereiche, deren Rand irgendwo eine unendliche Steigung hat, zerlegt man in reguläre Normalbereiche und addiert die Integrale.

### Räumliche Normalbereiche

<span class="anker" id="stufe-5-4"></span>

Derselbe Gedanke geht eine Dimension höher: Ein Körper zwischen einem Boden und einem Deckel wird zu einem Integral über seinen Schatten in der Ebene.

Über jedem Punkt $(x,y)$ des Schattens $D$ steht ein senkrechter Stab vom Boden bis zum Deckel. Man integriert zuerst längs des Stabs, also über $z$, und danach über den Schatten (Abb. [15](#abb-15)). Der Begriff des Normalbereichs lässt sich so von Dimension zu Dimension fortsetzen; hier genügt der Raum.

:::abbildung hm3/k2raum 15
Der Körper $M$ aus zwei Zylindern mit dem Radius $2$ im ersten Oktanten. Der Schatten $D$ ist ein Viertelkreis in der $x$-$y$-Ebene. Über dem Punkt $(x,y)$ reicht der Stab von $z=0$ bis zum Deckel $z=\sqrt{4-x^2}$.
:::

:::satz Satz 5.3 (Räumliche Normalbereiche)
<span class="anker" id="satz-5-3"></span>

Sei $D\subset\mathbb{R}^2$ ein regulärer Bereich, $\psi_1,\psi_2\colon D\to\mathbb{R}$ stetig mit $\psi_1\le\psi_2$ und

$$M=\{(x,y,z)\in\mathbb{R}^3:\ \psi_1(x,y)\le z\le\psi_2(x,y),\ (x,y)\in D\}.$$

Für stetiges $f\colon M\to\mathbb{R}$ gilt

<span class="anker" id="gl-5-4"></span>
$$\int_Mf(x,y,z)\,\mathrm{d} x\,\mathrm{d} y\,\mathrm{d} z=\int_D\Bigl(\int_{\psi_1(x,y)}^{\psi_2(x,y)}f(x,y,z)\,\mathrm{d} z\Bigr)\mathrm{d} x\,\mathrm{d} y . \tag{5.4}$$
:::

⁠**So liest man das:** $\psi_1(x,y)$ ist die Höhe des Bodens, $\psi_2(x,y)$ die des Deckels über dem Punkt $(x,y)$, und $D$ ist der Schatten des Körpers in der $x$-$y$-Ebene. Das innere Integral hängt noch von $x$ und $y$ ab, das äußere ist ein Integral über einen ebenen Bereich wie im letzten Unterabschnitt. Für $f\equiv1$ ist $\operatorname{vol}(M)=\int_D(\psi_2-\psi_1)\,\mathrm{d} x\,\mathrm{d} y$. Ist der Boden eben und der Abstand $\psi_2-\psi_1=H$ konstant, bleibt $H\,|D|$: Grundfläche mal Höhe.

⁠**Beispiel: noch einmal die Kuppel.** Mit dem Boden $\psi_1=0$, dem Deckel $\psi_2=4-x^2-y^2$ und der Kreisscheibe $D$ vom Radius $2$ als Schatten ist

$$\operatorname{vol}(K)=\int_{-2}^2\Bigl(\int_{-\sqrt{4-y^2}}^{\sqrt{4-y^2}}(4-y^2-x^2)\,\mathrm{d} x\Bigr)\mathrm{d} y=\frac43\int_{-2}^2(4-y^2)^{3/2}\,\mathrm{d} y=8\pi .$$

Innen gilt $\int_{-s}^s(s^2-x^2)\,\mathrm{d} x=\frac43s^3$ für jede Zahl $s>0$, hier mit $s=\sqrt{4-y^2}$. Außen ergibt die Substitution $y=2\sin\theta$ den Wert $16\int_{-\pi/2}^{\pi/2}\cos^4\theta\,\mathrm{d}\theta=6\pi$. Das stimmt mit [(4.3)](integration-uber-mengen-und-berechnung-von-volumina.html#gl-4-3) überein; die Scheiben waren bequemer. Hier wurde die Kreisscheibe als Typ 1 verwendet; das ist erlaubt, weil die Integrationsformel nur stetige Randfunktionen braucht.

⁠**Beispiel: zwei Zylinder.** Sei $M=Z_1\cap Z_2\cap O$ mit den Zylindern $Z_1=\{x^2+y^2\le4\}$ und $Z_2=\{x^2+z^2\le4\}$ und $O=\{x\ge0,\ y\ge0,\ z\ge0\}$. Dieses Achtel des Raums heißt der erste __Oktant__. $Z_2$ begrenzt $z$, $Z_1$ begrenzt $y$, beide in Abhängigkeit von $x$:

$$M=\{(x,y,z):\ 0\le z\le\sqrt{4-x^2},\ (x,y)\in D\},\quad D=\{(x,y):\ 0\le y\le\sqrt{4-x^2},\ 0\le x\le2\}.$$

Der Schatten $D$ ist ein ebener Normalbereich vom Typ 2. Also ist

$$\int_Mf\,\mathrm{d} x\,\mathrm{d} y\,\mathrm{d} z=\int_0^2\Bigl(\int_0^{\sqrt{4-x^2}}\Bigl(\int_0^{\sqrt{4-x^2}}f(x,y,z)\,\mathrm{d} z\Bigr)\mathrm{d} y\Bigr)\mathrm{d} x .$$

Für $f\equiv1$ ergibt das $\operatorname{vol}(M)=\int_0^2(4-x^2)\,\mathrm{d} x=\frac{16}3$. Für $f=x^2+y^2+z^2$ ist das innere Doppelintegral $x^2(4-x^2)+\frac23(4-x^2)^2$, und es folgt $\int_Mf\,\mathrm{d} V=\frac{704}{45}\approx15{,}6$.

:::merke Vorgehen bei einem Mehrfachintegral über einen Bereich
Den Bereich skizzieren und als Normalbereich schreiben, nötigenfalls zerlegen. Von innen nach außen integrieren: Innen stehen Funktionen der äußeren Variablen, ganz außen Zahlen. Die Reihenfolge so wählen, dass die Grenzen einfach werden und die Rechnung kurz.
:::

:::hintergrund Welche Variable gehört nach innen?
Die Variable, deren Grenzen sich am leichtesten als Funktionen der anderen schreiben lassen. Bei den zwei Zylindern hängen die Grenzen von $y$ und $z$ nur von $x$ ab, also steht $x$ außen. Mit $x$ innen müsste man den Bereich zerlegen, denn dann gilt $0\le x\le\sqrt{4-\max(y,z)^2}$, und das Maximum wechselt auf der Diagonalen $y=z$.
:::

⁠**Kurz gesagt:** Über einen Körper zwischen Boden und Deckel integriert man zuerst längs der senkrechten Stäbe und dann über den Schatten.

### Aufgaben

<span class="anker" id="stufe-5-5"></span>

:::aufgabe Aufgabe 14 ★★ Ein Betrag zwingt zum Zerlegen
<span class="anker" id="aufg-14"></span>

Sei $D=\{(x,y):0\le x\le2,\ x-1\le y\le1\}$. Skizziere $D$ und berechne $\int_D|y|\,\mathrm{d} x\,\mathrm{d} y$. Tipp: Das Vorzeichen von $y$ wechselt im inneren Integral nur für einen Teil der $x$.

:::loesung
$D$ ist ein Normalbereich vom Typ 2 mit $\mu(x)=x-1$ und $\nu(x)=1$ für $0\le x\le2$, ein Dreieck mit den Ecken $(0,-1)$, $(0,1)$ und $(2,1)$. Für $1\le x\le2$ ist $\mu(x)\ge0$, also ist $|y|=y$ im ganzen inneren Integral: $\int_{x-1}^1y\,\mathrm{d} y=\frac12\bigl(1-(x-1)^2\bigr)$. Für $0\le x\le1$ ist $\mu(x)\le0$, und man teilt bei $y=0$: $\int_{x-1}^0(-y)\,\mathrm{d} y+\int_0^1y\,\mathrm{d} y=\frac12\bigl((x-1)^2+1\bigr)$. Damit ist

$$\int_D|y|\,\mathrm{d} x\,\mathrm{d} y=\int_0^1\tfrac12\bigl((x-1)^2+1\bigr)\mathrm{d} x+\int_1^2\tfrac12\bigl(1-(x-1)^2\bigr)\mathrm{d} x=\frac23+\frac13=1 .$$
:::
:::

:::aufgabe Aufgabe 15 ★★ Reihenfolge tauschen
<span class="anker" id="aufg-15"></span>

Berechne $\int_0^1\bigl(\int_y^1\mathrm{e}^{x^2}\,\mathrm{d} x\bigr)\mathrm{d} y$. Tipp: Das innere Integral hat keine elementare Stammfunktion. Beschreibe das Dreieck als Normalbereich vom anderen Typ.

:::loesung
Das Gebiet ist $\{y\le x\le1,\ 0\le y\le1\}$, ein Normalbereich vom Typ 1: das Dreieck mit den Ecken $(0,0)$, $(1,0)$ und $(1,1)$. Als Typ 2 ist es $\{0\le y\le x,\ 0\le x\le1\}$. Also ist

$$\int_0^1\Bigl(\int_0^x\mathrm{e}^{x^2}\,\mathrm{d} y\Bigr)\mathrm{d} x=\int_0^1x\,\mathrm{e}^{x^2}\,\mathrm{d} x=\Bigl[\tfrac12\mathrm{e}^{x^2}\Bigr]_0^1=\frac{\mathrm{e}-1}2\approx0{,}859 .$$

In der neuen Reihenfolge liefert das innere Integral den Faktor $x$, und genau der fehlte zur Stammfunktion.
:::
:::

:::aufgabe Aufgabe 16 ★★ Körper als Normalbereich
<span class="anker" id="aufg-16"></span>

<ol class="al">

<li>

Sei $M=\{(x,y,z):x,y,z\ge0,\ x+\frac y2+\frac z3\le1\}$. Schreibe $M$ als räumlichen Normalbereich und berechne $\operatorname{vol}(M)$ und $\int_Mx\,\mathrm{d} x\,\mathrm{d} y\,\mathrm{d} z$.

</li>

<li>

Berechne das Volumen des Körpers über der Kreisscheibe $x^2+y^2\le1$ zwischen den Ebenen $z=-1-x$ und $z=2+y$. Tipp: Symmetrie.

</li>

</ol>

:::loesung
(a) Für $(x,y)$ im Schatten reicht $z$ von $0$ bis $3\bigl(1-x-\frac y2\bigr)$. Der Schatten ist das Dreieck $D=\{0\le y\le2(1-x),\ 0\le x\le1\}$, ein Normalbereich vom Typ 2. Mit $L=2(1-x)$ ist das innere Integral

$$\int_0^L3\Bigl(\frac L2-\frac y2\Bigr)\mathrm{d} y=3\Bigl(\frac{L^2}2-\frac{L^2}4\Bigr)=\frac34L^2=3(1-x)^2 .$$

Also ist $\operatorname{vol}(M)=\int_0^13(1-x)^2\,\mathrm{d} x=1$ und $\int_Mx\,\mathrm{d} x\,\mathrm{d} y\,\mathrm{d} z=\int_0^13x(1-x)^2\,\mathrm{d} x=\frac14$. Zur Kontrolle: $M$ ist eine Pyramide mit der Grundfläche $\frac12\cdot1\cdot2=1$ und der Höhe $3$, also $\operatorname{vol}=\frac13\cdot1\cdot3=1$.

(b) Der Boden ist $\psi_1=-1-x$, der Deckel $\psi_2=2+y$, die Höhe also $\psi_2-\psi_1=3+x+y\ge3-\sqrt2>0$ auf der Kreisscheibe $D$. Damit ist $\operatorname{vol}=\int_D(3+x+y)\,\mathrm{d} x\,\mathrm{d} y$. Die Kreisscheibe ist symmetrisch zu beiden Achsen. Beim Typ 1 ist innen $\int_{-\sqrt{1-y^2}}^{\sqrt{1-y^2}}x\,\mathrm{d} x=0$, also $\int_Dx=0$, und ebenso $\int_Dy=0$. Es bleibt $\operatorname{vol}=3\,|D|=3\pi$.
:::
:::
