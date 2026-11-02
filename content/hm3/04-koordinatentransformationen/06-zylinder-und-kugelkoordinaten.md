---
title: Stufe 4: Zylinder- und Kugelkoordinaten
pfad: Elektrotechnik / 3. Semester / Höhere Mathematik 3 / Koordinatentransformationen
order: 3140600
summary: Im Raum geht man genauso vor.
tags: Zylinderkoordinaten, Rotationskörper, verallgemeinerten Zylinderkoordinaten, Kugelkoordinaten
lang: de
---

<span class="anker" id="stufe-4"></span>

:::zweck
Im Raum geht man genauso vor. Diese Stufe liefert die Faktoren für Zylinder und Kugel und die Volumenformel für Rotationskörper.
:::

**Die Idee.** Die Herleitung aus Stufe [1](der-transformationssatz.html#stufe-1) benutzt die Dimension nirgends, deshalb gilt der Transformationssatz unverändert im $\mathbb{R}^3$, und zwar für $\Phi:B\to D$ zwischen beschränkten, abgeschlossenen Körpern mit stückweise glattem Rand. Was bleibt, ist die Wahl der Koordinaten: Für Körper mit einer Achse nimmt man zu den Polarkoordinaten die Höhe hinzu, für Kugeln braucht man zwei Winkel.

**Zylinderkoordinaten.** Die __Zylinderkoordinaten__ sind $\Phi(r,\varphi,z)=(r\cos\varphi,\,r\sin\varphi,\,z)$. Die Höhe $z$ bleibt unverändert, der Faktor ist wie in der Ebene $\det D\Phi=r$. Das Volumen des Kuppelkörpers ist damit

$$\int_0^{2\pi}\!\!\int_0^2\!\!\int_0^{4-r^2}r\,\mathrm{d} z\,\mathrm{d} r\,\mathrm{d}\varphi=2\pi\int_0^2(4-r^2)\,r\,\mathrm{d} r=8\pi.$$

**Rotationskörper.** Sei $p:\mathbb{R}\to\mathbb{R}$ stetig differenzierbar mit $p(z)\neq0$ auf $[a,b]$. Der __Rotationskörper__ $\mathcal R=\{(x,y,z):a\le z\le b,\;x^2+y^2\le p(z)^2\}$ entsteht, wenn sich das Profil $p$ um die $z$-Achse dreht. Die __verallgemeinerten Zylinderkoordinaten__

<span class="anker" id="gl-4-1"></span>
$$\Phi(r,\varphi,z)=\begin{pmatrix}r\,p(z)\cos\varphi\\r\,p(z)\sin\varphi\\z\end{pmatrix},\qquad(r,\varphi,z)\in[0,1]\times[0,2\pi]\times[a,b], \tag{4.1}$$

machen daraus einen Quader. Hier ist $r$ ein relativer Radius, $p(z)=1$ ist der Standardfall. Entwickeln nach der letzten Zeile $(0,0,1)$ gibt $\det D\Phi(r,\varphi,z)=r\,p(z)^2$, also

<span class="anker" id="gl-4-2"></span>
$$\operatorname{vol}(\mathcal R)=\int_{\mathcal R}1\,\mathrm{d} x\,\mathrm{d} y\,\mathrm{d} z=\int_a^b\!\!\int_0^1\!\!\int_0^{2\pi}r\,p(z)^2\,\mathrm{d}\varphi\,\mathrm{d} r\,\mathrm{d} z=\pi\int_a^bp(z)^2\,\mathrm{d} z. \tag{4.2}$$

⁠**So liest man das:** $\pi p(z)^2$ ist die Fläche der Kreisscheibe in der Höhe $z$, der Körper ist ein Stapel solcher Scheiben, wie beim Prinzip von Cavalieri aus [Teil 2](/wissen/elektrotechnik/3-semester/hohere-mathematik-3/integralrechnung-im-rn/integralrechnung-im-rn.html). **Kontrolle:** Für den Zylinder mit $p=R$ kommt $\pi R^2(b-a)$ heraus. Der Kuppelkörper hat das Profil $p(z)=\sqrt{4-z}$ auf $[0,4]$, und $\pi\int_0^4(4-z)\,\mathrm{d} z=8\pi$ stimmt mit dem Wert von oben überein. An der Spitze ist $p=0$, aber wie in Stufe [3](polarkoordinaten.html#stufe-3) genügt ein Grenzübergang.

**Kugelkoordinaten.** Die __Kugelkoordinaten__ der Kugel $\overline{B_R(0)}\subset\mathbb{R}^3$ benutzen den Abstand $r$, den Winkel $\theta$ zur $z$-Achse und den Winkel $\varphi$ in der $x$-$y$-Ebene (Abb. [4](#abb-4)). Der Nordpol hat $\theta=0$, der Äquator $\theta=\frac\pi2$:

<span class="anker" id="gl-4-3"></span>
$$\Phi(r,\theta,\varphi)=\begin{pmatrix}x(r,\theta,\varphi)\\y(r,\theta,\varphi)\\z(r,\theta,\varphi)\end{pmatrix}=\begin{pmatrix}r\sin\theta\cos\varphi\\r\sin\theta\sin\varphi\\r\cos\theta\end{pmatrix},\qquad r\in[0,R],\;\theta\in[0,\pi],\;\varphi\in[0,2\pi]. \tag{4.3}$$

:::abbildung hm3/k4kugel 4
Links: $r$ ist der Abstand vom Nullpunkt, $\theta$ der Winkel zur $z$-Achse, $\varphi$ der Winkel in der $x$-$y$-Ebene. Der Breitenkreis durch $P$ (grün) hat den Radius $r\sin\theta$. Rechts: die Zelle mit ihren drei Kantenlängen.
:::

:::herleitung Der Faktor der Kugel
Entwickeln nach der letzten Zeile von

$$D\Phi=\begin{pmatrix}\sin\theta\cos\varphi&r\cos\theta\cos\varphi&-r\sin\theta\sin\varphi\\\sin\theta\sin\varphi&r\cos\theta\sin\varphi&r\sin\theta\cos\varphi\\\cos\theta&-r\sin\theta&0\end{pmatrix}$$

gibt $\det D\Phi=\cos\theta\cdot r^2\sin\theta\cos\theta+r\sin\theta\cdot r\sin^2\theta=r^2\sin\theta$, also

<span class="anker" id="gl-4-4"></span>
$$\det D\Phi(r,\theta,\varphi)=\frac{\partial(x,y,z)}{\partial(r,\theta,\varphi)}=r^2\sin\theta. \tag{4.4}$$

Anschaulich hat die Zelle die Kanten $\mathrm{d} r$, $r\,\mathrm{d}\theta$ und $r\sin\theta\,\mathrm{d}\varphi$, denn der Breitenkreis hat nur den Radius $r\sin\theta$. Am Äquator ist er am längsten, an den Polen schrumpft er auf null.
:::

Wie bei Polarkoordinaten sind die Voraussetzungen an den Rändern $r=0$, $\theta\in\{0,\pi\}$, $\varphi\in\{0,2\pi\}$ verletzt, und wie dort rettet ein Grenzübergang die Formel. Für stetiges $f:\mathbb{R}^3\to\mathbb{R}$ gilt

<span class="anker" id="gl-4-5"></span>
$$\int_{B_R(0)}f(x,y,z)\,\mathrm{d} x\,\mathrm{d} y\,\mathrm{d} z=\int_0^R\!\!\int_0^\pi\!\!\int_0^{2\pi}f(\Phi(r,\theta,\varphi))\,r^2\sin\theta\,\mathrm{d}\varphi\,\mathrm{d}\theta\,\mathrm{d} r. \tag{4.5}$$

⁠**Kontrolle:** Mit $f=1$ folgt $\frac{R^3}3\cdot2\cdot2\pi=\frac43\pi R^3$, für die Modellkugel also $\frac{32}3\pi\approx33{,}5$. Dasselbe gibt [(4.2)](#gl-4-2) mit dem Profil $p(z)=\sqrt{R^2-z^2}$ auf $[-R,R]$. Hängt der Integrand nur vom Abstand ab, liefern die Winkel den Faktor $\int_0^\pi\!\int_0^{2\pi}\sin\theta\,\mathrm{d}\varphi\,\mathrm{d}\theta=4\pi$.

:::frage Welche Koordinaten soll ich nehmen?
Die, in denen das Gebiet ein Quader wird und der Integrand möglichst wenig Winkel enthält. Eine Achse in der Aufgabe heißt Zylinder, und die Achse muss nicht die $z$-Achse sein. Ein Abstand von einem Punkt heißt Kugel. Ellipsen und Ellipsoide streckt man erst auf Kreis und Kugel, zum Beispiel mit $\Phi(r,\varphi)=(a\,r\cos\varphi,\,b\,r\sin\varphi)$ und dem Faktor $a\,b\,r$.
:::

:::aufgabe Aufgabe 6 ★★ Kugel und Ellipsoid
<span class="anker" id="aufg-6"></span>

<ol class="al">

<li>

Berechne $\int_{B_2(0)}z^2\,\mathrm{d}\boldsymbol{x}$. Kontrolle: Was ergibt $\int_{B_2(0)}(x^2+y^2+z^2)\,\mathrm{d}\boldsymbol{x}$, und warum sind die drei Summanden gleich groß?

</li>

<li>

Berechne das Volumen des Ellipsoids $x^2+\frac{y^2}4+\frac{z^2}9\le1$ mit gestreckten Kugelkoordinaten.

</li>

</ol>

:::loesung
(a) Mit $z=r\cos\theta$ ist

$$\int_{B_2(0)}z^2\,\mathrm{d}\boldsymbol{x}=2\pi\int_0^2r^4\,\mathrm{d} r\int_0^\pi\cos^2\theta\sin\theta\,\mathrm{d}\theta=2\pi\cdot\frac{32}5\cdot\frac23=\frac{128\pi}{15}\approx26{,}8.$$

Kontrolle: $\int_{B_2(0)}|\boldsymbol{x}|^2\,\mathrm{d}\boldsymbol{x}=4\pi\int_0^2r^4\,\mathrm{d} r=\frac{128\pi}5$. Das Vertauschen der Koordinaten bildet die Kugel auf sich ab, die drei Summanden sind also gleich, und ein Drittel davon ist $\frac{128\pi}{15}$.

(b) Mit $\Phi(r,\theta,\varphi)=(r\sin\theta\cos\varphi,\,2r\sin\theta\sin\varphi,\,3r\cos\theta)$ auf $r\in[0,1]$ wird $\frac{x^2}1+\frac{y^2}4+\frac{z^2}9=r^2$. Gegenüber den Kugelkoordinaten sind die zweite und die dritte Zeile von $D\Phi$ mit 2 und 3 multipliziert, also ist $\det D\Phi=6r^2\sin\theta$. Das Volumen ist $6\cdot\frac43\pi=8\pi$.
:::
:::

:::aufgabe Aufgabe 7 ★★ Kegel um eine andere Achse
<span class="anker" id="aufg-7"></span>

Sei $C=\{(x,y,z):x^2+z^2\le y^2/4,\;0\le y\le2\}$. Berechne $\int_C\frac{1}{1+x^2+z^2}\,\mathrm{d}\boldsymbol{x}$.

:::loesung
Zylinderkoordinaten um die $y$-Achse: $\Phi(r,\varphi,y)=(r\cos\varphi,\,y,\,r\sin\varphi)$ mit $|\det D\Phi|=r$ und $0\le r\le y/2$. Dann

$$\int_C\frac{\mathrm{d}\boldsymbol{x}}{1+x^2+z^2}=\int_0^2\!\!\int_0^{y/2}\frac{2\pi r}{1+r^2}\,\mathrm{d} r\,\mathrm{d} y=\pi\int_0^2\ln\Bigl(1+\frac{y^2}4\Bigr)\mathrm{d} y.$$

Mit $y=2t$ und partieller Integration ist $\int_0^2\ln(1+y^2/4)\,\mathrm{d} y=2\int_0^1\ln(1+t^2)\,\mathrm{d} t=2\bigl[t\ln(1+t^2)-2t+2\arctan t\bigr]_0^1=2\ln2-4+\pi$. Ergebnis: $\pi(2\ln2-4+\pi)\approx1{,}66$.
:::
:::

:::aufgabe Aufgabe 8 ★★★ Torus auf zwei Wegen
<span class="anker" id="aufg-8"></span>

Sei $\mathcal T$ der Volltorus $\bigl(\sqrt{x^2+y^2}-3\bigr)^2+z^2\le1$.

<ol class="al">

<li>

Berechne sein Volumen mit Zylinderkoordinaten.

</li>

<li>

Berechne es mit $\Phi(s,\varphi,\beta)=\bigl((3+s\cos\beta)\cos\varphi,\,(3+s\cos\beta)\sin\varphi,\,s\sin\beta\bigr)$ auf $[0,1]\times[0,2\pi]\times[0,2\pi]$. Was bedeuten $s$ und $\beta$ anschaulich?

</li>

</ol>

:::loesung
(a) In Zylinderkoordinaten ist $(r-3)^2+z^2\le1$, also $2\le r\le4$ und $|z|\le\sqrt{1-(r-3)^2}$:

$$\operatorname{vol}(\mathcal T)=2\pi\int_2^42\sqrt{1-(r-3)^2}\;r\,\mathrm{d} r=4\pi\int_{-1}^1\sqrt{1-s^2}\,(s+3)\,\mathrm{d} s=4\pi\cdot3\cdot\frac\pi2=6\pi^2\approx59{,}2.$$

Der Term mit $s$ ist ungerade und fällt weg, $\int_{-1}^1\sqrt{1-s^2}\,\mathrm{d} s=\frac\pi2$ ist die halbe Kreisfläche.

(b) $s$ ist der Abstand vom Mittelkreis $r=3$, $z=0$, und $\beta$ der Winkel im kreisförmigen Querschnitt. Die Rechnung gibt $|\det D\Phi|=s(3+s\cos\beta)$, also $\int_0^1\!\int_0^{2\pi}\!\int_0^{2\pi}s(3+s\cos\beta)\,\mathrm{d}\beta\,\mathrm{d}\varphi\,\mathrm{d} s=2\pi\cdot3\cdot2\pi\cdot\frac12=6\pi^2$. Das ist die Querschnittsfläche $\pi$ mal der Umfang $2\pi\cdot3$ des Mittelkreises.
:::
:::
