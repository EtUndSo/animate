---
title: Volumenintegrale: Zylinder- und Kugelkoordinaten
pfad: Elektrotechnik / 3. Semester / Höhere Mathematik 3 / Koordinatentransformationen
order: 3040200
summary: Von Grund auf – der Transformationssatz in 3D mit seinen beiden Arbeitspferden. Zylinderkoordinaten liefern das Volumenelement $dV=r\,dr\,d\varphi\,dz$, Kugelkoordinaten $dV=r^2\sin\vartheta\,dr\,d\vartheta\,d\varphi$. Damit fallen Kugel- und Zylindervolumen in wenigen Zeilen, und der Faktor $r^2$ macht singuläre radiale Funktionen wie das Coulomb-Potential $1/|x|$ im Raum integrierbar.
tags: Volumenintegral, Zylinderkoordinaten, Kugelkoordinaten, Jacobi-Determinante, Rotationskörper, Kugelvolumen, singuläre radiale Funktion, Coulomb-Potential
---

:::grafik
Einstiegs-Animation: Zwei Volumen-„Maschen" im Raum. Links __Zylinderkoordinaten__ $(r,\varphi,z)$: ein
Volumenelement der Kantenlängen $dr$, $r\,d\varphi$, $dz$ — Volumen $r\,dr\,d\varphi\,dz$. Rechts
__Kugelkoordinaten__ $(r,\vartheta,\varphi)$: ein Element der Kantenlängen $dr$, $r\,d\vartheta$,
$r\sin\vartheta\,d\varphi$ — Volumen $r^2\sin\vartheta\,dr\,d\vartheta\,d\varphi$. Eine Animation zeigt, warum der
Breitenkreis bei Polarwinkel $\vartheta$ nur den Radius $r\sin\vartheta$ hat (zu den Polen hin schrumpft er auf
null). Kernbotschaft: In 3D liefern Zylinder- und Kugelkoordinaten die Volumenfaktoren $r$ bzw. $r^2\sin\vartheta$.
:::

:::konzept
Der Transformationssatz gilt in **jeder** Dimension. In drei Dimensionen hat man zwei Standard-Koordinatensysteme,
die fast alle symmetrischen Probleme lösen: __Zylinderkoordinaten__ (für zylindersymmetrische Aufgaben) und
__Kugelkoordinaten__ (für kugelsymmetrische). Jedes bringt seinen Jacobi-Faktor mit — $r$ bzw. $r^2\sin\vartheta$ —,
und damit werden Kugel-, Zylinder- und Rotationskörper-Volumina zur Fingerübung. Der Faktor $r^2$ in
Kugelkoordinaten hat zudem eine tiefe Konsequenz: Er „entschärft" Singularitäten, sodass im Raum selbst Funktionen
integrierbar bleiben, die am Ursprung über alle Grenzen wachsen — etwa das Coulomb-Potential.
:::

**Worum es geht:** Wir übertragen den Transformationssatz auf __Volumenintegrale__, nutzen
__Zylinderkoordinaten__ (auch für __Rotationskörper__) und __Kugelkoordinaten__ und zeigen, warum singuläre
radiale Funktionen ($\le c/|x|^\alpha$, $\alpha<3$) integrierbar sind.

## Zylinderkoordinaten

Zylinderkoordinaten sind die Polarkoordinaten der $xy$-Ebene, ergänzt um die unveränderte Höhe $z$:

$$\Phi(r,\varphi,z) = (r\cos\varphi,\ r\sin\varphi,\ z), \qquad \det D\Phi = r.$$

Das Volumenelement ist also $dV = r\,dr\,d\varphi\,dz$ — der Polarfaktor $r$, die Höhe $z$ geht ohne Faktor ein.
Damit wird jedes zylindersymmetrische Volumen einfach.

**Rotationskörper.** Allgemeiner beschreibt man einen Rotationskörper $R=\{a\le z\le b,\ x^2+y^2\le f(z)^2\}$
(Rotation des Profils $f(z)$ um die $z$-Achse) durch **verallgemeinerte** Zylinderkoordinaten $\Phi(r,\varphi,z)=
(r f(z)\cos\varphi,\ r f(z)\sin\varphi,\ z)$ mit $r\in[0,1]$. Dann ist $\det D\Phi = r\,f(z)^2$, und das Volumen

$$\mathrm{vol}(R) = \int_a^b\!\int_0^1\!\int_0^{2\pi} r\,f(z)^2\,d\varphi\,dr\,dz = \pi\int_a^b f(z)^2\,dz$$

— die bekannte Rotationskörper-Formel. **Eigenes Beispiel:** Der Zylinder (Radius $R$, Höhe $H$, $f(z)=R$) hat
$\mathrm{vol}=\pi\int_0^H R^2\,dz=\pi R^2 H$.

:::grafik
Zylinderkoordinaten-Gitter: konzentrische Kreise ($r$), Winkelstrahlen ($\varphi$), Höhenebenen ($z$); ein
Volumenelement $r\,dr\,d\varphi\,dz$ hervorgehoben. Daneben ein Rotationskörper mit Profil $f(z)$ und die Formel
$\mathrm{vol}=\pi\int f(z)^2\,dz$.
:::

## Kugelkoordinaten

Für kugelsymmetrische Probleme parametrisiert man den Raum durch Radius $r$, __Polarwinkel__ $\vartheta$ (von der
$z$-Achse gemessen, $\vartheta\in[0,\pi]$) und __Azimut__ $\varphi\in[0,2\pi]$:

$$\Phi(r,\vartheta,\varphi) = \begin{pmatrix} r\sin\vartheta\cos\varphi \\ r\sin\vartheta\sin\varphi \\ r\cos\vartheta \end{pmatrix}, \qquad \det D\Phi = \frac{\partial(x,y,z)}{\partial(r,\vartheta,\varphi)} = r^2\sin\vartheta.$$

Das Volumenelement ist $dV = r^2\sin\vartheta\,dr\,d\vartheta\,d\varphi$. Der Faktor $r^2\sin\vartheta$ ist
anschaulich: Ein kleines Kästchen hat die radiale Kante $dr$, die „Meridian"-Kante $r\,d\vartheta$ und die
„Breitenkreis"-Kante $r\sin\vartheta\,d\varphi$ — denn der Breitenkreis beim Polarwinkel $\vartheta$ hat nur den
Radius $r\sin\vartheta$ (an den Polen null, am Äquator maximal). Für stetiges $f$:

$$\int_{B_R(0)} f\,dx\,dy\,dz = \int_0^R\!\int_0^{\pi}\!\int_0^{2\pi} f(\Phi(r,\vartheta,\varphi))\,r^2\sin\vartheta\,d\varphi\,d\vartheta\,dr.$$

**Eigenes Beispiel (Kugelvolumen).** Mit $f\equiv1$:

$$\mathrm{vol}(B_R) = \int_0^R\!\int_0^{\pi}\!\int_0^{2\pi} r^2\sin\vartheta\,d\varphi\,d\vartheta\,dr = 2\pi\underbrace{\int_0^\pi \sin\vartheta\,d\vartheta}_{=\,2}\int_0^R r^2\,dr = 4\pi\cdot\frac{R^3}{3} = \frac{4}{3}\pi R^3.$$

Die drei Integrationen separieren sauber — ein Musterbeispiel für die Kraft passender Koordinaten.

:::grafik
Kugelkoordinaten: Radius $r$, Polarwinkel $\vartheta$ (von der $z$-Achse), Azimut $\varphi$; das Volumenelement mit
Kanten $dr$, $r\,d\vartheta$, $r\sin\vartheta\,d\varphi$. Hervorgehoben der Breitenkreis-Radius $r\sin\vartheta$
(schrumpft zu den Polen). Daneben die separierte Rechnung zu $\tfrac{4}{3}\pi R^3$.
:::

**Stolperstein:** Winkelkonvention beachten — hier ist $\vartheta\in[0,\pi]$ der **Polarwinkel** von der
$z$-Achse und $\varphi\in[0,2\pi]$ der Azimut; manche Bücher vertauschen die Buchstaben. Und: Den Faktor
$r^2\sin\vartheta$ **nie vergessen** — er ist die häufigste Fehlerquelle beim Rechnen mit Kugelkoordinaten. (Wie
bei den Polarkoordinaten erfüllt $\Phi$ an den Rändern $r=0$, $\vartheta\in\{0,\pi\}$ die Voraussetzungen des
Satzes nicht exakt; der $\varepsilon$-Grenzwert rettet die Formel.)

## Singuläre radiale Funktionen sind integrierbar

Der Faktor $r^2$ in Kugelkoordinaten hat eine wichtige Folge für **singuläre** Felder, die am Ursprung
explodieren. Ist $f:\mathbb{R}^3\setminus\{0\}\to\mathbb{R}$ stetig mit

$$|f(x)| \le \frac{c}{|x|^\alpha} \quad\text{für ein } \alpha < 3,$$

so konvergiert $\int_{B_R(0)}f\,dx$ (als Grenzwert $\varepsilon\to0$ über $\{\varepsilon\le|x|\le R\}$) **absolut**,
und

$$\int_{B_R(0)}|f(x)|\,dx \le c\,\frac{4\pi R^{3-\alpha}}{3-\alpha}.$$

**Warum?** In Kugelkoordinaten ist $\int_{\varepsilon\le|x|\le R}\frac{1}{|x|^\alpha}\,dx = 4\pi\int_\varepsilon^R
\frac{r^2}{r^\alpha}\,dr = 4\pi\int_\varepsilon^R r^{2-\alpha}\,dr$. Dieses Integral bleibt für $\varepsilon\to0$
genau dann **endlich**, wenn $2-\alpha>-1$, also $\alpha<3$ — der Faktor $r^2$ aus dem Volumenelement verschiebt
die kritische Schwelle von (naiv) $\alpha<1$ auf $\alpha<3$.

Die wichtigsten Beispiele: Das **Coulomb-Potential** $\varphi(x)=\frac{1}{4\pi|x|}$ (Exponent $\alpha=1<3$) und
sogar seine ersten Ableitungen, die wie $1/|x|^2$ divergieren ($\alpha=2<3$), sind über Kugeln integrierbar.
Genau das sichert die Wohldefiniertheit der Potentialintegrale im nächsten Artikel.

:::grafik
Die radiale Singularität $1/|x|^\alpha$ am Ursprung; daneben die Rechnung $\int_\varepsilon^R r^{2-\alpha}\,dr$,
die dank des $r^2$-Volumenfaktors für $\alpha<3$ konvergiert. Markiert: Coulomb $1/|x|$ ($\alpha=1$) und Feld
$1/|x|^2$ ($\alpha=2$) — beide integrierbar.
:::

:::kern
Der __Transformationssatz__ gilt in 3D für __Volumenintegrale__. __Zylinderkoordinaten__
$\Phi=(r\cos\varphi,r\sin\varphi,z)$: $\det D\Phi=r$, $dV=r\,dr\,d\varphi\,dz$; Rotationskörper (verallg. Zylinder
$\det=rf(z)^2$) haben $\mathrm{vol}=\pi\int_a^b f(z)^2\,dz$ (Zylinder $\pi R^2 H$). __Kugelkoordinaten__
$\Phi=(r\sin\vartheta\cos\varphi,r\sin\vartheta\sin\varphi,r\cos\vartheta)$ ($\vartheta\in[0,\pi]$ Polarwinkel,
$\varphi\in[0,2\pi]$): $\det D\Phi=r^2\sin\vartheta$, $dV=r^2\sin\vartheta\,dr\,d\vartheta\,d\varphi$ (Breitenkreis
hat Radius $r\sin\vartheta$); Kugelvolumen $\tfrac{4}{3}\pi R^3$ (separiert). **Faktor nie vergessen!**
Der $r^2$-Faktor macht __singuläre radiale Funktionen__ integrierbar: $|f|\le c/|x|^\alpha$ mit $\alpha<3$ ⟹
$\int_{B_R}|f|\le c\tfrac{4\pi R^{3-\alpha}}{3-\alpha}$ (da $\int r^{2-\alpha}dr$ für $\alpha<3$ endlich); Coulomb
$1/|x|$ ($\alpha=1$) und $1/|x|^2$ ($\alpha=2$) integrierbar.
:::

Dass das Coulomb-Potential im Raum integrierbar ist, ist der Schlüssel zur __Potentialtheorie__: Man kann das
Potential einer Ladungs- oder Massenverteilung als Integral über lauter Punktpotentiale $1/|x-y|$ bilden. Dieses
__Newtonpotential__ und seine Eigenschaften (Poisson-Gleichung) sind das Thema des nächsten Artikels.
