---
title: Der Transformationssatz und Polarkoordinaten
pfad: Elektrotechnik / 3. Semester / Höhere Mathematik 3 / Koordinatentransformationen
order: 3040100
summary: Von Grund auf – wie man ein Integral in bequemere Koordinaten umschreibt, $\int_D f(y)\,dy=\int_B f(\Phi(x))\,|\det D\Phi(x)|\,dx$. Der Betrag der Jacobi-Determinante ist der lokale Flächen-/Volumenfaktor (die mehrdimensionale Substitutionsregel). In Polarkoordinaten liefert das das Element $r\,dr\,d\varphi$ – und als berühmte Anwendung das Gauß-Integral $\int_{-\infty}^{\infty}e^{-x^2}dx=\sqrt{\pi}$.
tags: Transformationssatz, Jacobi-Determinante, Substitutionsregel, Polarkoordinaten, Flächenelement, Gauß-Integral, Koordinatenwechsel
---

:::grafik
Einstiegs-Animation: Links ein Rechteck im $(r,\varphi)$-Raum, das durch die Abbildung $\Phi(r,\varphi)=(r\cos
\varphi,r\sin\varphi)$ auf eine **Kreisscheibe** abgebildet wird. Ein kleines Kästchen der Kantenlängen
$dr\times d\varphi$ wird dabei zu einer krummen „Masche" in der Scheibe — und diese hat die Fläche $r\,dr\,d\varphi$
(nicht $dr\,d\varphi$!). Der Streckfaktor $r$ wächst nach außen, die Maschen werden größer. Kernbotschaft: Beim
Koordinatenwechsel verzerrt sich das Flächenelement um den Faktor $|\det D\Phi|$ — hier gerade $r$.
:::

:::konzept
Integrale über **krumme** Gebiete (Kreise, Kugeln, Ellipsen) sind in kartesischen Koordinaten mühsam. Der
__Transformationssatz__ erlaubt den Wechsel in **bequeme** Koordinaten — Polar-, Zylinder-, Kugelkoordinaten —, in
denen das Gebiet und oft auch der Integrand einfach werden. Der Preis dafür ist ein Faktor: der Betrag der
__Jacobi-Determinante__ $|\det D\Phi|$, der misst, wie stark die Transformation das Volumen lokal **streckt oder
staucht**. Das ist nichts anderes als die **Substitutionsregel** aus HM1, hochgezogen in mehrere Dimensionen. Als
Belohnung fällt am Ende ein berühmtes Integral, das kartesisch unzugänglich ist: das Gauß-Integral.
:::

**Worum es geht:** Wir formulieren den __Transformationssatz__, verstehen die __Jacobi-Determinante__ als
Volumenfaktor, rechnen in __Polarkoordinaten__ ($\det D\Phi=r$) und berechnen damit das __Gauß-Integral__.

## Der Transformationssatz

Sei $\Phi:G\to\mathbb{R}^2$ stetig differenzierbar, und seien $B,D$ reguläre Bereiche mit $B\subset G$, sodass
$\Phi:B\to D$ **bijektiv** ist und $\det D\Phi(x)\neq0$ für alle $x\in B$. Dann gilt für jede stetige Funktion
$f:D\to\mathbb{R}$ der __Transformationssatz__:

$$\int_D f(y)\,dy = \int_B f(\Phi(x))\,\big|\det D\Phi(x)\big|\,dx.$$

In Worten: Statt über das (krumme) Zielgebiet $D$ integriert man über das (einfache) Urbildgebiet $B$ — man setzt
die Transformation $\Phi$ in $f$ ein und multipliziert mit dem Betrag der Jacobi-Determinante. Für $n=1$ ist das
genau die vertraute **Substitutionsregel** $\int_{\Phi(a)}^{\Phi(b)} f(y)\,dy = \int_a^b f(\Phi(x))\,\Phi'(x)\,dx$
(dort steht $\Phi'$ ohne Betrag, weil die Orientierung über die Integrationsgrenzen mitgeführt wird).

## Warum die Jacobi-Determinante?

Der Faktor $|\det D\Phi|$ ist kein Zufall, sondern reine **Geometrie**. Für eine lineare Abbildung $A\in
\mathbb{R}^{n\times n}$ ist $|\det A|$ gerade das Volumen des von den Spalten aufgespannten Parallelotops — und
damit der Faktor, um den $A$ **jedes** Volumen streckt:

$$\mathrm{vol}(AQ) = |\det A|\,\mathrm{vol}(Q).$$

Eine differenzierbare Abbildung $\Phi$ ist lokal durch ihre lineare Näherung $\Phi(x)\approx\Phi(x_0)+D\Phi(x_0)
(x-x_0)$ gegeben. Ein winziger Quader $Q$ um $x_0$ wird daher auf ein Gebiet vom Volumen
$\mathrm{vol}(\Phi(Q))\approx|\det D\Phi(x_0)|\,\mathrm{vol}(Q)$ abgebildet. Summiert man das über alle kleinen
Quader (Riemann-Summe), entsteht genau der Faktor $|\det D\Phi|$ im Integral — in jeder Dimension.

:::grafik
Ein kleiner Quader $Q$ bei $x_0$, der durch $\Phi$ auf eine verzerrte Zelle abgebildet wird; daneben die lineare
Näherung $D\Phi(x_0)$, deren Determinante das Volumenverhältnis $\mathrm{vol}(\Phi(Q))/\mathrm{vol}(Q)\approx
|\det D\Phi(x_0)|$ angibt. Beschriftung „Jacobi-Determinante = lokaler Volumenfaktor".
:::

## Polarkoordinaten

Das wichtigste Beispiel. Die Kreisscheibe $B_R(0)=\{x^2+y^2\le R^2\}$ parametrisiert man durch

$$\Phi(r,\varphi) = \begin{pmatrix} r\cos\varphi \\ r\sin\varphi \end{pmatrix}, \qquad (r,\varphi)\in[0,R]\times[0,2\pi].$$

Die Jacobi-Matrix und ihre Determinante sind

$$D\Phi(r,\varphi) = \begin{pmatrix} \cos\varphi & -r\sin\varphi \\ \sin\varphi & r\cos\varphi \end{pmatrix}, \qquad \det D\Phi(r,\varphi) = r\cos^2\varphi + r\sin^2\varphi = r.$$

Nach dem Transformationssatz wird daraus das __Flächenelement in Polarkoordinaten__ $dx\,dy = r\,dr\,d\varphi$, und
für stetiges $f$:

$$\int_{B_R(0)} f(x,y)\,dx\,dy = \int_0^R\!\int_0^{2\pi} f(\Phi(r,\varphi))\,r\,d\varphi\,dr.$$

Der Faktor $r$ ist anschaulich klar: Weiter außen überstreicht derselbe Winkelzuwachs $d\varphi$ einen längeren
Bogen, die Maschen werden größer. Für die Jacobi-Determinante ist auch die Schreibweise
$\det D\Phi=\frac{\partial(x,y)}{\partial(r,\varphi)}$ gebräuchlich.

**Stolperstein:** Streng genommen ist $\Phi$ auf $[0,R]\times[0,2\pi]$ **weder bijektiv** (bei $r=0$ wird die ganze
Winkelkante auf den Ursprung abgebildet) **noch** ist $\det D\Phi\ne0$ dort ($r=0$). Man schränkt deshalb formal auf
$[\varepsilon,R]\times[\varepsilon,2\pi]$ ein; der weggelassene Beitrag (eine Nullmenge am Rand) geht für
$\varepsilon\to0$ gegen null, und die Formel bleibt gültig. Außerdem steht im Satz der **Betrag** $|\det D\Phi|$ —
das Vorzeichen (die Orientierung) wird nicht mitgezählt.

**Eigenes Beispiel.** Der Flächeninhalt der Scheibe folgt sofort mit $f\equiv1$:
$\int_0^R\int_0^{2\pi} r\,d\varphi\,dr = 2\pi\int_0^R r\,dr = 2\pi\cdot\tfrac{R^2}{2} = \pi R^2$.

## Das Gauß-Integral

Jetzt die klassische Belohnung. Die Funktion $e^{-x^2}$ hat **keine** elementare Stammfunktion — das Integral
$\int_{-\infty}^{\infty} e^{-x^2}\,dx$ scheint unzugänglich. Über den Umweg eines **Flächenintegrals** in
Polarkoordinaten gelingt es dennoch. Für das rotationssymmetrische $e^{-(x^2+y^2)}$ ist

$$\int_{B_R(0)} e^{-(x^2+y^2)}\,dx\,dy = \int_0^{2\pi}\!\int_0^{R} e^{-r^2}\,r\,dr\,d\varphi = 2\pi\cdot\Big[-\tfrac12 e^{-r^2}\Big]_0^{R} = \pi\big(1 - e^{-R^2}\big) \ \xrightarrow{R\to\infty}\ \pi.$$

Der entscheidende Trick: In Polarkoordinaten liefert der Faktor $r$ gerade die „innere Ableitung", sodass
$e^{-r^2}r$ elementar integrierbar wird. Andererseits klemmt man das Quadrat des gesuchten Integrals
$I(R)=\int_{-R}^{R}e^{-x^2}dx$ zwischen zwei Kreisscheiben ein (Sandwich),

$$\int_{B_R(0)} e^{-(x^2+y^2)}dx\,dy \ \le\ \big(I(R)\big)^2 \ \le\ \int_{B_{\sqrt{2}R}(0)} e^{-(x^2+y^2)}dx\,dy,$$

und beide Seiten streben gegen $\pi$. Also $\big(\int_{-\infty}^\infty e^{-x^2}dx\big)^2=\pi$, und damit das
berühmte Ergebnis

$$\int_{-\infty}^{\infty} e^{-x^2}\,dx = \sqrt{\pi}.$$

:::grafik
Die Glockenfläche $e^{-(x^2+y^2)}$ über der Ebene; ihr Volumen wird in Polarkoordinaten als $\int_0^{2\pi}\int_0^R
e^{-r^2}r\,dr\,d\varphi=\pi(1-e^{-R^2})$ berechnet. Daneben das Sandwich: das Quadrat $(\int e^{-x^2}dx)^2$
zwischen zwei Kreisscheiben eingeklemmt, Grenzwert $\pi$ → $\int e^{-x^2}dx=\sqrt\pi$.
:::

:::kern
Der __Transformationssatz__ schreibt ein Integral in neue Koordinaten um: für bijektives, stetig
differenzierbares $\Phi:B\to D$ mit $\det D\Phi\ne0$ gilt $\int_D f(y)\,dy=\int_B f(\Phi(x))\,|\det D\Phi(x)|\,dx$
(mehrdimensionale __Substitutionsregel__; 1D ohne Betrag). Der Faktor $|\det D\Phi|$ ist der lokale
**Volumenfaktor** ($\mathrm{vol}(\Phi(Q))\approx|\det D\Phi|\,\mathrm{vol}(Q)$ aus der linearen Näherung). In
__Polarkoordinaten__ $\Phi(r,\varphi)=(r\cos\varphi,r\sin\varphi)$ ist $\det D\Phi=r$, also $dx\,dy=r\,dr\,d\varphi$
und $\int_{B_R}f\,dx\,dy=\int_0^R\int_0^{2\pi} f\,r\,d\varphi\,dr$ (Scheibenfläche $\pi R^2$). **Stolperstein:** Betrag
nehmen; Randfälle ($r=0$) per $\varepsilon$-Grenzwert. Anwendung: __Gauß-Integral__ $\int_{B_R}e^{-(x^2+y^2)}=
\pi(1-e^{-R^2})\to\pi$ + Sandwich $\Rightarrow \int_{-\infty}^\infty e^{-x^2}dx=\sqrt\pi$.
:::

Dasselbe Prinzip trägt in drei Dimensionen — dort führen __Zylinder-__ und __Kugelkoordinaten__ zu den
Volumenelementen $r\,dr\,d\varphi\,dz$ bzw. $r^2\sin\vartheta\,dr\,d\vartheta\,d\varphi$. Das ist das Thema des
nächsten Artikels.
