---
title: Der Transformationssatz und Polarkoordinaten
pfad: Elektrotechnik / 3. Semester / Höhere Mathematik 3 / Koordinatentransformationen
order: 3040100
summary: Von Grund auf – wie man ein Flächenintegral in bequemere Koordinaten umschreibt, $\int_{\vec\Phi(B)}f(\vec x)\,d^2x=\int_B f(\vec\Phi(\vec u))\,\lvert\det D\vec\Phi(\vec u)\rvert\,d^2u$. Leitbild ist das Gummituch aus dem ersten Artikel – ein Gitter wird verzerrt, und jede Masche ändert ihre Fläche um den Faktor $\lvert\det D\vec\Phi\rvert$. Mit dem Flächenfaktor linearer Abbildungen, dem Beweis über den Satz von Stokes, der Substitutionsregel als Spezialfall, Polarkoordinaten mit $r\,dr\,d\varphi$ und dem Gauß-Integral $\int e^{-x^2}dx=\sqrt\pi$. Mit Beispiel-Seite.
tags: Transformationssatz, Jacobi-Determinante, Substitutionsregel, Polarkoordinaten, Flächenelement, Gauß-Integral, Koordinatenwechsel
---

## Anschaulich

Integrale über Kreisscheiben, Ringe oder Ellipsen sind in kartesischen Koordinaten mühsam — die Grenzen sind voller
Wurzeln. In Polarkoordinaten dagegen ist eine Kreisscheibe einfach ein Rechteck: Der Radius läuft von $0$ bis $R$, der Winkel
von $0$ bis $2\pi$. Der Preis für den Wechsel der Koordinaten ist ein Faktor im Integral.

**Das Leitbild dieses Artikels:** das **Gummituch** aus dem ersten Artikel. Auf das Tuch ist ein Gitter aus kleinen, gleich
großen Quadraten gezeichnet. Eine Abbildung $\vec\Phi$ verzerrt das Tuch, und aus jedem Quadrat wird eine krumme **Masche**.

Unter der Lupe sieht jede glatte Verzerrung linear aus; deshalb ist jede kleine Masche fast ein Parallelogramm. Ihre Fläche
ist die Fläche des Quadrats mal dem Betrag der __Jacobi-Determinante__ $\det D\vec\Phi$, der Determinante der Jacobi-Matrix aus
dem ersten Artikel. Dieser Betrag ist der __Flächenfaktor__.

Ein Integral über das verzerrte Tuch zählt jede Masche mit ihrer neuen Fläche. Das ist der __Transformationssatz__: Man
integriert über das einfache, unverzerrte Gitter und multipliziert mit dem Flächenfaktor.

Bei Polarkoordinaten wird das Gitter zu einem **Spinnennetz**. Weiter außen sind die Maschen größer, denn derselbe
Winkelschritt überstreicht dort einen längeren Bogen — der Flächenfaktor ist der Radius $r$. Damit gelingt am Ende sogar ein
Integral, das man kartesisch nicht ausrechnen kann: die Fläche unter der Glockenkurve, das Gauß-Integral.

:::grafik
Szene: hoema3/koordinatentransformationen/01-gummituch-maschen · Vorlage: gitter-verzerrung-2d
Links ein Rechteck in den Koordinaten $(r,\varphi)$ mit einem Gitter aus kleinen Rechtecken der Seiten $dr$ und $d\varphi$;
rechts sein Bild unter $\vec\Phi(r,\varphi)=(r\cos\varphi,\ r\sin\varphi)$, ein Spinnennetz auf der Kreisscheibe. Eine markierte
Masche wird links und rechts hervorgehoben und lässt sich mit der Maus verschieben; ein Zähler zeigt ihre Fläche rechts, etwa
$r\,dr\,d\varphi$, nach außen wachsend. Eine Lupe über der Masche zeigt, dass sie fast ein Parallelogramm ist. Kernaussage:
Beim Koordinatenwechsel zählt jede Masche mit dem Flächenfaktor $\lvert\det D\vec\Phi\rvert$. (Rot = Masche, blau = Gitter,
orange = Lupe, grau = Achsen.)
:::

## Lineare Abbildungen strecken Flächen um den Betrag der Determinante

Der Kern steckt schon in der linearen Algebra. **Die Akteure:** eine Matrix $A\in\mathbb{R}^{n\times n}$ und ein Quader
$Q\subseteq\mathbb{R}^n$ mit dem Volumen $\mathrm{vol}(Q)$ wie im Artikel über Integration über Mengen — in der Ebene ein
Rechteck mit seinem Flächeninhalt. Die lineare Abbildung $\vec u\mapsto A\vec u$ macht aus dem Quader ein __Parallelotop__
$AQ$, das schiefe Gegenstück eines Quaders, in der Ebene ein Parallelogramm. Sein Volumen ist

:::formel Lemma
$$\mathrm{vol}(AQ) = \lvert\det A\rvert\;\mathrm{vol}(Q).$$
:::

**So liest man das:** Der Betrag der Determinante ist der Streckfaktor für Volumina, in der Ebene für Flächen. Ihr Vorzeichen
sagt, ob die Abbildung die Orientierung erhält (positiv) oder spiegelt (negativ); für das Volumen zählt nur der Betrag.

Anders gesagt: $\det A$ ist das orientierte Volumen des Parallelotops, das die Spalten von $A$ aufspannen —
oder ihre Zeilen, denn eine Matrix und ihre Transponierte haben dieselbe Determinante.

**Im Bild:** Eine gleichmäßige Verzerrung des Gummituchs macht aus jedem Quadrat des Gitters dasselbe Parallelogramm, nur an
einer anderen Stelle. Alle Maschen ändern ihre Fläche um denselben Faktor.

:::herleitung
**In der Ebene** reicht die Schnürsenkelformel aus dem Artikel über die
[Integralsätze in der Ebene](/wissen/elektrotechnik/3-semester/hohere-mathematik-3/kurvenintegrale/integralsaetze-in-der-ebene.html).
Sei zuerst $Q$ das Einheitsquadrat $[0,1]^2$, und
seien $\vec a$ und $\vec b$ die Spalten von $A$. Das Bild $AQ$ ist das Parallelogramm mit den Ecken $\vec 0$, $\vec a$,
$\vec a+\vec b$ und $\vec b$. Für diese Reihenfolge der Ecken gibt die Formel

$$\frac12\Big(\det\big(\vec 0\,\big|\,\vec a\big)+\det\big(\vec a\,\big|\,\vec a+\vec b\big)+\det\big(\vec a+\vec b\,\big|\,\vec b\big)+\det\big(\vec b\,\big|\,\vec 0\big)\Big) = \det\big(\vec a\,\big|\,\vec b\big) = \det A,$$

denn die Determinante ist linear in jeder Spalte und verschwindet, wenn zwei Spalten gleich sind oder eine null ist.

Laufen die Ecken in dieser Reihenfolge gegen den Uhrzeigersinn, ist das die Fläche. Laufen sie im Uhrzeigersinn, ist es das
Negative der Fläche, denn rückwärts gelesen wechselt jede Determinante der Formel ihr Vorzeichen. In beiden Fällen ist die
Fläche $\lvert\det A\rvert$. Ist die Determinante null, liegen $\vec a$ und $\vec b$ auf einer Geraden, und das Parallelogramm
ist flach.

Ein achsenparalleles Rechteck mit den Kantenlängen $p$ und $q$ wird auf ein verschobenes Parallelogramm aus $p\,\vec a$ und
$q\,\vec b$ abgebildet. Seine Fläche ist

$$\big\lvert\det\big(p\,\vec a\,\big|\,q\,\vec b\big)\big\rvert = pq\,\lvert\det A\rvert.$$

**Im Bild:** Die Spalten $\vec a$ und $\vec b$ sind die beiden Gitterpfeile des Tuchs; das Quadrat wird zu dem
Parallelogramm, das sie aufspannen.

**In jeder Dimension** hilft das Gauß-Verfahren. Ist die Determinante null, liegen die Spalten in einer __Hyperebene__ — einem
Unterraum der Dimension $n-1$ —, und das Bild hat das Volumen null. Sonst bringen Zeilenumformungen $A$ auf Diagonalform,
und rückwärts gelesen ist $A$ ein Produkt: Auf $Q$ wirkt zuerst eine Diagonalmatrix, danach wirken nur noch Umformungen zweier
Sorten, die kein Volumen ändern.

- Eine **Scherung** addiert zur $i$-ten Koordinate das $\lambda$-Fache der $j$-ten, für zwei verschiedene Indizes. Jede Gerade
  in $x_i$-Richtung wird dabei in sich verschoben, denn auf ihr ist $x_j$ fest. Die Schnitte einer Menge mit diesen Geraden
  werden also nur versetzt, nicht gedehnt. Nach Fubini ist das Volumen das Integral der Schnittlängen über die übrigen
  Koordinaten; es bleibt gleich. Die Determinante einer Scherung ist $1$. **Im Bild:** Die Gitterzeilen des Tuchs gleiten
  gegeneinander wie die Karten eines Stapels.
- Eine **Vertauschung** zweier Koordinaten ändert kein Volumen. Ihre Determinante ist $-1$.

Die Diagonalmatrix mit den Einträgen $d_1,\ldots,d_n$ macht aus $Q$ wieder einen Quader, dessen Kanten mit den Beträgen
$\lvert d_k\rvert$ gestreckt sind. Sein Volumen ist $\mathrm{vol}(Q)$ mal $\lvert d_1\cdots d_n\rvert$. Weil die Determinante
eines Produkts das Produkt der Determinanten ist, unterscheidet sich $\det A$ von $d_1\cdots d_n$ höchstens im Vorzeichen —
daraus folgt das Lemma.
:::

::::beispiel Parallelogramme aus dem Einheitsquadrat
Das Einheitsquadrat unter vier Matrizen:

$$A_1 = \begin{pmatrix}2&0\\0&3\end{pmatrix}, \qquad A_2 = \begin{pmatrix}2&1\\1&1\end{pmatrix}, \qquad A_3 = \begin{pmatrix}0&1\\1&0\end{pmatrix}, \qquad A_4 = \begin{pmatrix}1&2\\1&2\end{pmatrix}.$$

**(a)** $A_1$ streckt waagerecht um $2$ und senkrecht um $3$. Es entsteht ein Rechteck der Fläche $6$, und

$$\det A_1 = 2\cdot3-0\cdot0 = 6.$$

**(b)** $A_2$ macht daraus das Parallelogramm mit den Ecken $(0,0)$, $(2,1)$, $(3,2)$ und $(1,1)$. Die Schnürsenkelformel gibt
der Reihe nach die Determinanten $0$, $1$, $1$ und $0$, also die Fläche $1$ — passend zu

$$\det A_2 = 2\cdot1-1\cdot1 = 1.$$

Das Quadrat wird schief und in die Länge gezogen, behält aber seine Fläche.

**(c)** $A_3$ vertauscht die Koordinaten — eine Spiegelung an der Diagonalen. Die Fläche bleibt $1$, aber

$$\det A_3 = 0\cdot0-1\cdot1 = -1.$$

**(d)** Bei $A_4$ sind beide Spalten Vielfache von $(1,1)$. Das Quadrat wird auf die Strecke von $(0,0)$ bis $(3,3)$
flachgedrückt, mit der Fläche $0$, und

$$\det A_4 = 1\cdot2-2\cdot1 = 0.$$

**Im Bild:** Bei (c) wird das Gummituch umgedreht. Die Maschen behalten ihre Fläche, nur ihr Umlaufsinn kehrt sich um: Die
Ecken $(0,0)$, $(1,0)$, $(1,1)$, $(0,1)$ laufen gegen den Uhrzeigersinn, ihre Bilder $(0,0)$, $(0,1)$, $(1,1)$, $(1,0)$ im
Uhrzeigersinn. Bei (d) wird das Tuch zu einem Faden zusammengedrückt — genau das schließt der Transformationssatz aus.
::::

## Der Transformationssatz

**Die Akteure:** ein __Gebiet__ $G\subseteq\mathbb{R}^2$ — eine offene, zusammenhängende Menge —, eine stetig differenzierbare
Abbildung $\vec\Phi:G\to\mathbb{R}^2$ und ein regulärer Bereich $B\subseteq G$. Ein __regulärer Bereich__ ist wie im Artikel über die
[Integralsätze in der Ebene](/wissen/elektrotechnik/3-semester/hohere-mathematik-3/kurvenintegrale/integralsaetze-in-der-ebene.html)
eine beschränkte, abgeschlossene Menge mit zusammenhängendem Inneren, deren Rand aus endlich vielen geschlossenen
regulären Kurven besteht.

Die Abbildung nimmt einen Punkt $\vec u$ — die neuen Koordinaten — und gibt einen Punkt der Ebene aus:

$$\vec x = \vec\Phi(\vec u).$$

**Im Bild:** $B$ ist das unverzerrte Gitter, sein Bild $\vec\Phi(B)$ das verzerrte Tuch. Verlangt wird dreierlei: Das Bild ist
wieder ein regulärer Bereich; $\vec\Phi$ ist auf $B$ __injektiv__ — verschiedene Punkte haben verschiedene Bilder, das Tuch
liegt nirgends doppelt —; und $\vec\Phi$ drückt nirgends flach:

$$\det D\vec\Phi(\vec u)\neq0 \quad\text{für alle } \vec u\in B.$$

Dann gilt für jede stetige Funktion $f:\vec\Phi(B)\to\mathbb{R}$

:::formel Satz
$$\int_{\vec\Phi(B)}f(\vec x)\,d^2x = \int_B f\big(\vec\Phi(\vec u)\big)\,\big\lvert\det D\vec\Phi(\vec u)\big\rvert\,d^2u.$$
:::

**So liest man das:** Links integriert man über das krumme Gebiet $\vec\Phi(B)$ in den alten Koordinaten $\vec x$. Rechts
integriert man über das einfache Gebiet $B$ in den neuen Koordinaten $\vec u$: Man setzt $\vec\Phi$ in $f$ ein und gewichtet
mit dem Flächenfaktor.

Die neuen Koordinaten heißen hier $\vec u$, die alten $\vec x$, damit $(x,y)$ später wie gewohnt die kartesischen
Koordinaten sein können.

**Im Bild:** Jede kleine Masche des verzerrten Tuchs ist unter der Lupe ein Parallelogramm, das aus einem Quadrat des Gitters
entstand. Ihre Fläche ist $\lvert\det D\vec\Phi\rvert$ mal die Fläche des Quadrats — genau dieser Faktor steht im Integral.

:::herleitung
**Die Idee, in jeder Dimension.** Unter der Lupe ist $\vec\Phi$ nahe einem Punkt $\vec u_0$ fast linear. Das ist die totale
Differenzierbarkeit aus dem ersten Artikel:

$$\frac{\big\lvert\vec\Phi(\vec u)-\vec\Phi(\vec u_0)-D\vec\Phi(\vec u_0)\,(\vec u-\vec u_0)\big\rvert}{\lvert\vec u-\vec u_0\rvert}\to0 \qquad\text{für } \vec u\to\vec u_0.$$

Ein kleiner Quader $Q$ um $\vec u_0$ wird deshalb fast auf ein Parallelotop abgebildet, und nach dem Lemma ist

$$\mathrm{vol}\big(\vec\Phi(Q)\big) \approx \big\lvert\det D\vec\Phi(\vec u_0)\big\rvert\;\mathrm{vol}(Q).$$

Legt man ein feines Gitter aus kleinen Quadern $Q_k$ mit Mittelpunkten $\vec u_k$ über $B$, zerlegen die Bildzellen
$\vec\Phi(Q_k)$ das Gebiet $\vec\Phi(B)$. In der Näherung

$$\sum_k f\big(\vec\Phi(\vec u_k)\big)\,\mathrm{vol}\big(\vec\Phi(Q_k)\big) \approx \sum_k f\big(\vec\Phi(\vec u_k)\big)\,\big\lvert\det D\vec\Phi(\vec u_k)\big\rvert\,\mathrm{vol}(Q_k)$$

ist die linke Summe eine Näherung für das Integral über $\vec\Phi(B)$, die rechte eine für das Integral über $B$ — die beiden
Seiten des Satzes. Werden die Quader feiner, verschwindet der Fehler. Das ist die Beweisidee; einen vollständigen
Beweis in jeder Dimension führen wir hier nicht.

**Im Bild:** Links zählt man die Maschen des verzerrten Tuchs mit ihrer echten Fläche, rechts die Quadrate des Gitters mit
ihrem Flächenfaktor. Für feine Gitter ist das dieselbe Summe.
:::

:::herleitung
**Der Beweis in der Ebene**, mit drei Zusatzannahmen. Erstens ist $f$ sogar stetig differenzierbar, und zwar
auf einer offenen, __sternförmigen__ Menge $U\subseteq\mathbb{R}^2$, die $\vec\Phi(B)$ enthält: Von einem Zentrum $\vec x_0$ aus
ist wie beim Aussichtsturm im Poincaré-Lemma jeder Punkt von $U$ auf gerader Linie sichtbar. Zweitens ist $\vec\Phi$ zweimal
stetig differenzierbar. Drittens ist der Rand von $B$ eine einzige geschlossene reguläre Kurve
$\vec\gamma:[a,b]\to\mathbb{R}^2$, positiv orientiert.

Weil das Innere von $B$ zusammenhängt und die Determinante nirgends null ist, hat sie nach dem Zwischenwertsatz überall
dasselbe Vorzeichen. Sei sie zuerst positiv.

**Schritt 1: $f$ als Rotation.** Man setzt

$$\vec F(\vec x) := \int_0^1 t\,f\big(\vec x_0+t(\vec x-\vec x_0)\big)\,(\vec x-\vec x_0)^{\perp}\,dt, \qquad \vec w^{\,\perp} := (-w_2,\ w_1).$$

Dabei dreht $\perp$ einen Vektor um $90^\circ$ nach links. Dann ist $\vec F$ auf $U$ stetig differenzierbar, und

$$\operatorname{rot}\vec F = \partial_1F_2-\partial_2F_1 = f.$$

Der Ansatz ist derselbe wie im Poincaré-Lemma: Man integriert längs der Strahlen vom Zentrum aus. Die Rechnung steht am Ende
der Box.

**Im Bild:** $\vec F$ ist ein Wind, dessen Wirbelstärke an jedem Punkt genau $f$ ist.

**Schritt 2: Stokes auf dem Bild.** Der Rand von $\vec\Phi(B)$ ist das Bild des Randes von $B$: Weil $\vec\Phi$ nahe jedem
Punkt umkehrbar ist (Satz über die Umkehrabbildung) und auf $B$ injektiv, gehen innere Punkte in innere und Randpunkte in
Randpunkte über. Durchlaufen wird der Rand von der Kurve $\vec\Phi\circ\vec\gamma$. Sie ist regulär, weil $D\vec\Phi$ umkehrbar
ist.

Sie ist auch wieder positiv orientiert. Die nach links gedrehte Tangente $\dot{\vec\gamma}^{\,\perp}$ zeigt ins Innere von
$B$, ihr Bild unter $D\vec\Phi$ ins Innere von $\vec\Phi(B)$, und dieses Bild liegt links von der neuen Tangente:

$$\det\big(D\vec\Phi\,\dot{\vec\gamma}\,\big|\,D\vec\Phi\,\dot{\vec\gamma}^{\,\perp}\big) = \det D\vec\Phi\cdot\det\big(\dot{\vec\gamma}\,\big|\,\dot{\vec\gamma}^{\,\perp}\big) = \det D\vec\Phi\cdot\lvert\dot{\vec\gamma}\rvert^2 > 0.$$

Eine positive Determinante zweier Vektoren heißt: Der zweite liegt links vom ersten. Nach dem Satz von Stokes in der Ebene
und der Definition des Kurvenintegrals ist deshalb

$$\int_{\vec\Phi(B)}f\,d^2x = \int_{\vec\Phi(B)}\operatorname{rot}\vec F\,d^2x = \oint_{\partial\vec\Phi(B)}\vec F\cdot d\vec x,$$

$$\oint_{\partial\vec\Phi(B)}\vec F\cdot d\vec x = \int_a^b\vec F\Big(\vec\Phi\big(\vec\gamma(t)\big)\Big)\cdot\frac{d}{dt}\vec\Phi\big(\vec\gamma(t)\big)\,dt.$$

**Schritt 3: zurück nach $B$.** Nach der Kettenregel ist die $j$-te Komponente der Geschwindigkeit

$$\frac{d}{dt}\Phi_j\big(\vec\gamma(t)\big) = \nabla\Phi_j\big(\vec\gamma(t)\big)\cdot\dot{\vec\gamma}(t).$$

Im Integranden steht deshalb

$$\vec F\big(\vec\Phi(\vec\gamma)\big)\cdot\frac{d}{dt}\vec\Phi(\vec\gamma) = \sum_{j=1}^2F_j\big(\vec\Phi(\vec\gamma)\big)\,\nabla\Phi_j(\vec\gamma)\cdot\dot{\vec\gamma},$$

und das ist der Integrand eines Kurvenintegrals längs des Randes von $B$:

$$\oint_{\partial\vec\Phi(B)}\vec F\cdot d\vec x = \sum_{j=1}^2\oint_{\partial B}\vec H_j\cdot d\vec u, \qquad \vec H_j := \big(F_j\circ\vec\Phi\big)\,\nabla\Phi_j.$$

**Im Bild:** Statt den Rand des verzerrten Tuchs abzufahren, fährt man den Rand des unverzerrten Gitters ab und rechnet jeden
Schritt mit der Lupe — der Jacobi-Matrix — in den verzerrten Schritt um.

**Schritt 4: noch einmal Stokes, auf $B$.** Die Felder $\vec H_j$ sind stetig differenzierbar, weil $\vec\Phi$ es zweimal ist.
Ihre Rotation ist nach der Produktregel

$$\operatorname{rot}\vec H_j = \partial_1\Big(\big(F_j\circ\vec\Phi\big)\,\partial_2\Phi_j\Big)-\partial_2\Big(\big(F_j\circ\vec\Phi\big)\,\partial_1\Phi_j\Big) = \partial_1\big(F_j\circ\vec\Phi\big)\,\partial_2\Phi_j-\partial_2\big(F_j\circ\vec\Phi\big)\,\partial_1\Phi_j,$$

denn die beiden Terme mit $\partial_1\partial_2\Phi_j$ heben sich nach dem Satz von Schwarz weg. Die Kettenregel gibt

$$\partial_i\big(F_j\circ\vec\Phi\big) = \sum_{k=1}^2\big(\partial_kF_j\circ\vec\Phi\big)\,\partial_i\Phi_k.$$

Dabei leitet $\partial_i$ links nach $u_i$ ab, und $\partial_kF_j$ ist die Ableitung von $F_j$ nach $x_k$. Eingesetzt entsteht

$$\operatorname{rot}\vec H_j = \sum_{k=1}^2\big(\partial_kF_j\circ\vec\Phi\big)\,\big(\partial_1\Phi_k\,\partial_2\Phi_j-\partial_2\Phi_k\,\partial_1\Phi_j\big).$$

Die Klammer ist null, wenn $k$ und $j$ gleich sind. In den beiden übrigen Fällen ist sie

$$j=2,\ k=1:\quad \partial_1\Phi_1\,\partial_2\Phi_2-\partial_2\Phi_1\,\partial_1\Phi_2 = \det D\vec\Phi, \qquad j=1,\ k=2:\quad \partial_1\Phi_2\,\partial_2\Phi_1-\partial_2\Phi_2\,\partial_1\Phi_1 = -\det D\vec\Phi.$$

Zusammen bleibt

$$\operatorname{rot}\vec H_1+\operatorname{rot}\vec H_2 = \big(\partial_1F_2\circ\vec\Phi-\partial_2F_1\circ\vec\Phi\big)\det D\vec\Phi = \big(f\circ\vec\Phi\big)\det D\vec\Phi.$$

Der Satz von Stokes auf $B$ macht aus der Summe der Randintegrale das Integral dieser Rotation über $B$. Weil die Determinante
positiv ist, ist sie ihr eigener Betrag — das ist die rechte Seite des Satzes.

**Im Bild:** Die Wirbel des Winds auf dem verzerrten Tuch, auf das Gitter zurückgeholt, sind die alten Wirbel mal dem
Flächenfaktor — eine Masche mit doppelter Fläche fasst doppelt so viel Wirbel.

**Bei negativer Determinante** kehrt $\vec\Phi$ die Orientierung um: $\vec\Phi\circ\vec\gamma$ läuft so, dass das Innere rechts
liegt, und in Schritt 2 kommt ein Minuszeichen hinzu. Am Ende steht $-\det D\vec\Phi$ — wieder der Betrag.

**Die Rechnung zu Schritt 1.** Sei der Einfachheit halber $\vec x_0=\vec 0$; sonst verschiebt man. Die Komponenten von
$\vec F$ sind

$$F_1(\vec x) = -\int_0^1 t\,f(t\vec x)\,x_2\,dt, \qquad F_2(\vec x) = \int_0^1 t\,f(t\vec x)\,x_1\,dt.$$

Ableiten unter dem Integral ist erlaubt, weil der Integrand stetig differenzierbar ist (Artikel über Parameterintegrale).
Produkt- und Kettenregel geben

$$\partial_1F_2(\vec x) = \int_0^1 t\Big(t\,(\partial_1f)(t\vec x)\,x_1+f(t\vec x)\Big)\,dt, \qquad \partial_2F_1(\vec x) = -\int_0^1 t\Big(t\,(\partial_2f)(t\vec x)\,x_2+f(t\vec x)\Big)\,dt.$$

Damit ist

$$\operatorname{rot}\vec F(\vec x) = \int_0^1\Big(t^2\,(\nabla f)(t\vec x)\cdot\vec x+2t\,f(t\vec x)\Big)\,dt = \int_0^1\frac{d}{dt}\Big(t^2f(t\vec x)\Big)\,dt = f(\vec x).$$

**Was der Beweis nicht abdeckt:** Für ein nur stetiges $f$ oder einen Rand aus mehreren Kurven braucht man zusätzliche
Näherungs- und Zerlegungsargumente, die hier nicht ausgeführt werden.
:::

::::beispiel Ellipse und gefaltetes Tuch
**(a) Die Ellipse aus dem Kreis.** Wie im Artikel über Integration über Mengen bezeichnet $S_1$ die abgeschlossene
Kreisscheibe vom Radius $1$ um den Ursprung. Die Abbildung

$$\vec\Phi(u_1,u_2) = (2u_1,\ 3u_2), \qquad D\vec\Phi = \begin{pmatrix}2&0\\0&3\end{pmatrix}, \qquad \det D\vec\Phi = 6,$$

bildet $S_1$ injektiv auf die Ellipse

$$E = \Big\{(x,y)\in\mathbb{R}^2 : \frac{x^2}{4}+\frac{y^2}{9}\le1\Big\}$$

mit den Halbachsen $2$ und $3$ ab, denn für den Bildpunkt gilt

$$\frac{(2u_1)^2}{4}+\frac{(3u_2)^2}{9} = u_1^2+u_2^2.$$

Mit $f=1$ gibt der Satz die Fläche

$$\mathrm{vol}(E) = \int_{S_1}6\,d^2u = 6\pi.$$

Das passt zu $\pi\cdot2\cdot3$, der Fläche, die die Planimeter-Formel im Artikel über die Integralsätze in der Ebene für
diese Ellipse liefert.

**Im Bild:** Das Gummituch wird überall gleich gestreckt, waagerecht um $2$, senkrecht um $3$. Jede Masche wird sechsmal so
groß, der Kreis zur Ellipse.

**(b) Ohne Injektivität zählt man doppelt.** Die Abbildung

$$\vec\Phi(u_1,u_2) = \big(u_1^2,\ u_2\big), \qquad \det D\vec\Phi(\vec u) = 2u_1,$$

bildet das Rechteck $[-1,1]\times[0,1]$ auf das Einheitsquadrat ab. Sie ist aber nicht injektiv: Jeder Bildpunkt mit positiver
erster Koordinate hat zwei Urbilder, und auf der Faltlinie ist die Determinante null. Die rechte Seite des Satzes mit $f=1$
wäre

$$\int_0^1\int_{-1}^{1}\lvert2u_1\rvert\,du_1\,du_2 = 2,$$

die Fläche des Quadrats ist aber $1$.

**Im Bild:** Das Tuch wird längs der Linie $u_1=0$ gefaltet, und beide Hälften landen aufeinander auf demselben Quadrat. Jede
Masche des Quadrats liegt zweimal da, und der Flächenfaktor zählt beide Lagen.
::::

## In einer Dimension: die Substitutionsregel

Für Funktionen einer Variablen ist der Satz die Substitutionsregel. Dort steht die Ableitung ohne Betrag, dafür mit
orientierten Grenzen: Für ein stetig differenzierbares $\psi:[\alpha,\beta]\to\mathbb{R}$ und ein auf dem Bild von $\psi$
stetiges $f$ gilt

:::formel
$$\int_{\psi(\alpha)}^{\psi(\beta)}f(x)\,dx = \int_\alpha^\beta f\big(\psi(u)\big)\,\psi'(u)\,du.$$
:::

**So liest man das:** $\psi$ ist die Verzerrung eines eindimensionalen Gummibands, $\psi'$ ihr Streckfaktor mit Vorzeichen.
Läuft $\psi$ rückwärts, ist $\psi'$ negativ, und zugleich stehen links die Grenzen verkehrt herum.

**Im Bild:** In einer Dimension kann man die Richtung über die Grenzen mitführen; die beiden Minuszeichen gleichen sich aus.
In der Ebene gibt es keine Grenzen mit Richtung — man integriert über Mengen —, deshalb steht dort der Betrag.

:::herleitung
**Direkt mit dem Hauptsatz.** Ist $s$ eine Stammfunktion von $f$, so ist nach der Kettenregel $s\circ\psi$ eine
Stammfunktion von $(f\circ\psi)\,\psi'$. Beide Seiten sind deshalb dieselbe Differenz:

$$\int_{\psi(\alpha)}^{\psi(\beta)}f(x)\,dx = s\big(\psi(\beta)\big)-s\big(\psi(\alpha)\big) = \int_\alpha^\beta f\big(\psi(u)\big)\,\psi'(u)\,du.$$

Dafür muss $\psi$ weder injektiv sein noch eine Ableitung ohne Nullstellen haben — in einer Dimension ist die Regel sogar
allgemeiner als der Satz.

**Vergleich mit dem Satz.** Hat $\psi'$ keine Nullstelle, ist es nach dem Zwischenwertsatz überall positiv oder überall
negativ. Bei positivem $\psi'$ wächst $\psi$ und bildet $[\alpha,\beta]$ auf $[\psi(\alpha),\psi(\beta)]$ ab; der Betrag ist
überflüssig. Bei negativem $\psi'$ fällt $\psi$ und bildet $[\alpha,\beta]$ auf $[\psi(\beta),\psi(\alpha)]$ ab. Die Regel gibt
dann

$$\int_{\psi(\beta)}^{\psi(\alpha)}f(x)\,dx = -\int_{\psi(\alpha)}^{\psi(\beta)}f(x)\,dx = -\int_\alpha^\beta f\big(\psi(u)\big)\,\psi'(u)\,du,$$

und weil $\psi'$ negativ ist, ist das

$$-\int_\alpha^\beta f\big(\psi(u)\big)\,\psi'(u)\,du = \int_\alpha^\beta f\big(\psi(u)\big)\,\lvert\psi'(u)\rvert\,du.$$

Das ist der Satz in einer Dimension: das Integral über das Bild links, das Integral mit dem Betrag rechts.

**Im Bild:** Das Minuszeichen der vertauschten Grenzen und das negative Vorzeichen des Streckfaktors heben sich auf.
:::

::::beispiel Substitution rückwärts und gefaltet
**(a) Rückwärts.** Die fallende Abbildung

$$\psi(u) = 3-u, \qquad \psi'(u) = -1,$$

bildet $[0,2]$ auf $[1,3]$ ab. Für $f(x)=x$ geben das Integral über das Bild und das mit dem Betrag umgerechnete denselben
Wert:

$$\int_1^3 x\,dx = 4, \qquad \int_0^2(3-u)\,\lvert-1\rvert\,du = \Big[3u-\frac{u^2}{2}\Big]_0^2 = 4.$$

Mit orientierten Grenzen und ohne Betrag stehen auf beiden Seiten Minuszeichen:

$$\int_{\psi(0)}^{\psi(2)}x\,dx = \int_3^1 x\,dx = -4, \qquad \int_0^2(3-u)\cdot(-1)\,du = -4.$$

**Im Bild:** Das Gummiband wird umgedreht, wie bei der Spiegelung oben; seine Länge bleibt, nur die Richtung kehrt sich um.

**(b) Gefaltet.** Die Abbildung

$$\psi(u) = u^2, \qquad \psi'(u) = 2u,$$

läuft auf $[-1,1]$ von $1$ nach $0$ und zurück nach $1$. Für $f(x)=x$ gibt die Regel auf beiden Seiten null:

$$\int_{\psi(-1)}^{\psi(1)}x\,dx = \int_1^1 x\,dx = 0, \qquad \int_{-1}^{1}u^2\cdot2u\,du = \Big[\frac{u^4}{2}\Big]_{-1}^{1} = 0.$$

Mit dem Betrag dagegen zählt man das Intervall $[0,1]$ doppelt:

$$\int_{-1}^{1}u^2\,\lvert2u\rvert\,du = 2\int_0^1 2u^3\,du = 1 = 2\int_0^1 x\,dx.$$

**Im Bild:** Das Gummiband wird bei $u=0$ gefaltet; beide Hälften landen auf $[0,1]$, eine rückwärts, eine vorwärts. Mit
Vorzeichen heben sich die beiden Lagen auf wie ein Weg hin und zurück. Mit dem Betrag zählt jede Lage, wie beim gefalteten
Tuch in der Ebene.
::::

## Polarkoordinaten

Das wichtigste Beispiel. Die abgeschlossene Kreisscheibe vom Radius $R>0$ um den Ursprung,

$$S_R = \big\{(x,y)\in\mathbb{R}^2 : x^2+y^2\le R^2\big\},$$

wird durch den Radius $r$ und den Winkel $\varphi$ beschrieben:

$$\vec\Phi(r,\varphi) = (r\cos\varphi,\ r\sin\varphi), \qquad (r,\varphi)\in[0,R]\times[0,2\pi].$$

Die Jacobi-Matrix und ihre Determinante sind

$$D\vec\Phi(r,\varphi) = \begin{pmatrix}\cos\varphi & -r\sin\varphi\\ \sin\varphi & r\cos\varphi\end{pmatrix}, \qquad \det D\vec\Phi(r,\varphi) = r\cos^2\varphi+r\sin^2\varphi = r.$$

:::herleitung
Die Spalten der Jacobi-Matrix sind die Ableitungen nach den beiden neuen Koordinaten:

$$\frac{\partial\vec\Phi}{\partial r} = (\cos\varphi,\ \sin\varphi), \qquad \frac{\partial\vec\Phi}{\partial\varphi} = (-r\sin\varphi,\ r\cos\varphi).$$

Die Determinante ist „links oben mal rechts unten minus rechts oben mal links unten", und $\cos^2\varphi+\sin^2\varphi=1$.

**Im Bild:** Der erste Gitterpfeil zeigt radial nach außen und hat die Länge $1$, der zweite tangential und hat die Länge
$r$. Sie stehen senkrecht aufeinander und spannen ein Rechteck der Fläche $r$ auf. Im ersten Artikel kam derselbe Faktor
schon heraus.
:::

Für stetiges $f:\mathbb{R}^2\to\mathbb{R}$ gilt deshalb — mit einer Begründung weiter unten, denn die Voraussetzungen des
Satzes sind am Mittelpunkt verletzt —

:::formel
$$\int_{S_R}f(x,y)\,d(x,y) = \int_0^R\int_0^{2\pi}f(r\cos\varphi,\ r\sin\varphi)\;r\,d\varphi\,dr.$$
:::

**So liest man das:** Rechts steht das Integral über das Rechteck $[0,R]\times[0,2\pi]$, nach Fubini als Doppelintegral. Das
__Flächenelement__ — die Fläche einer kleinen Masche — ist in Polarkoordinaten $r\,dr\,d\varphi$ und nicht $dr\,d\varphi$. Für
die Jacobi-Determinante ist in Koordinaten auch die Schreibweise

$$\det D\vec\Phi(r,\varphi) = \frac{\partial(x,y)}{\partial(r,\varphi)}$$

üblich.

**Im Bild:** Das Spinnennetz. Eine Masche zwischen den Radien $r$ und $r+dr$ und den Winkeln $\varphi$ und $\varphi+d\varphi$
ist ein Stück eines Kreisrings — fast ein Rechteck mit den Seiten $dr$ und $r\,d\varphi$, dem Bogen. Ihre Fläche ist
$r\,dr\,d\varphi$.

**Der Haken am Mittelpunkt.** Auf $[0,R]\times[0,2\pi]$ ist $\vec\Phi$ nicht injektiv: Die ganze Kante bei $r=0$ wird auf den
Ursprung abgebildet, und die Winkel $0$ und $2\pi$ treffen dieselbe Halbgerade. Außerdem ist die Determinante bei $r=0$
null. Die Voraussetzungen des Satzes sind also verletzt — die Formel gilt trotzdem.

:::grafik
Szene: hoema3/koordinatentransformationen/01-nabe-und-keil · Vorlage: kreisscheibe-ausschnitt-2d
Die Kreisscheibe $S_R$ als Spinnennetz. Ein Regler für $\varepsilon$ schneidet die Nabe — die Scheibe vom Radius $\varepsilon$ —
und einen Keil mit dem Öffnungswinkel $\varepsilon$ heraus; daneben das Rechteck $[0,R]\times[0,2\pi]$ in den Koordinaten
$(r,\varphi)$ mit den beiden zugehörigen Streifen. Ein Zähler zeigt die fehlende Fläche $\pi\varepsilon^2+\frac{\varepsilon}{2}R^2$,
die mit $\varepsilon$ gegen null geht. Kernaussage: Die Stellen, an denen die Polarkoordinaten den Satz verletzen, tragen
nichts zum Integral bei. (Rot = herausgeschnittene Teile, blau = Gitter, grau = Achsen.)
:::

:::herleitung
Man schränkt $\vec\Phi$ für kleines $\varepsilon>0$ auf das kleinere Rechteck

$$B_\varepsilon = [\varepsilon,R]\times[\varepsilon,2\pi]$$

ein. Dort ist $\vec\Phi$ injektiv — die Winkel überdecken weniger als eine volle Umdrehung —, und die Determinante ist
mindestens $\varepsilon$. Der Satz gilt also für $B_\varepsilon$.

Das Bild $\vec\Phi(B_\varepsilon)$ ist die Kreisscheibe ohne die kleine Scheibe vom Radius $\varepsilon$ und ohne den schmalen
Keil zwischen den Winkeln $0$ und $\varepsilon$. Beide zusammen haben höchstens die Fläche

$$\pi\varepsilon^2+\frac{\varepsilon}{2}\,R^2.$$

Auf der Kreisscheibe ist $f$ als stetige Funktion beschränkt, etwa durch eine Zahl $c$:

$$\lvert f(x,y)\rvert\le c \quad\text{für alle } (x,y)\in S_R.$$

Links unterscheiden sich deshalb die Integrale über $S_R$ und über $\vec\Phi(B_\varepsilon)$ höchstens um $c$ mal diese
Fläche. Rechts fehlen dem Rechteck $[0,R]\times[0,2\pi]$ die beiden Streifen $[0,\varepsilon)\times[0,2\pi]$ und
$[\varepsilon,R]\times[0,\varepsilon)$, zusammen höchstens mit der Fläche

$$2\pi\varepsilon+R\varepsilon;$$

auf ihnen ist der Integrand $f(\vec\Phi)\,r$ betragsmäßig höchstens $cR$. Für $\varepsilon\to0$ gehen beide Unterschiede gegen
null, und aus dem Satz für $B_\varepsilon$ wird die Formel.

**Im Bild:** Man schneidet aus dem Spinnennetz die Nabe und einen schmalen Keil heraus. Auf dem Rest ist alles in Ordnung,
und das Herausgeschnittene wird beliebig klein.
:::

::::beispiel Polarkoordinaten in Aktion
**(a) Die Kreisfläche** mit $f=1$:

$$\int_0^R\int_0^{2\pi}r\,d\varphi\,dr = 2\pi\cdot\frac{R^2}{2} = \pi R^2.$$

**(b) Der Kreisring** zwischen den Radien $R_1$ und $R_2$, mit $0<R_1<R_2$: Der Radius läuft jetzt von $R_1$ bis $R_2$, mit
derselben Begründung wie für die Scheibe, und die Fläche ist

$$\int_{R_1}^{R_2}\int_0^{2\pi}r\,d\varphi\,dr = \pi\big(R_2^2-R_1^2\big).$$

**(c) Der runde Laib** aus dem Artikel über Mehrfachintegrale hat über der Einheitskreisscheibe die Höhe

$$f(x,y) = 1-x^2-y^2, \qquad f(r\cos\varphi,\ r\sin\varphi) = 1-r^2.$$

Sein Volumen ist

$$\int_0^1\int_0^{2\pi}\big(1-r^2\big)\,r\,d\varphi\,dr = 2\pi\Big(\frac12-\frac14\Big) = \frac{\pi}{2}.$$

Dort kam dasselbe aus Scheiben und einem Integral über $\cos^4$, im Artikel über Integration über Mengen aus waagerechten
Schnitten — hier ist es eine Zeile.

**(d) Das Trägheitsmoment einer Scheibe** um ihre Achse ist das Integral des Abstandsquadrats zur Achse über die Masse. Eine
Scheibe der Masse $m$ und vom Radius $R$, gleichmäßig mit der Flächendichte

$$\varrho = \frac{m}{\pi R^2}$$

belegt, hat deshalb das Trägheitsmoment

$$J = \varrho\int_{S_R}\big(x^2+y^2\big)\,d(x,y) = \varrho\int_0^R\int_0^{2\pi}r^2\cdot r\,d\varphi\,dr = \varrho\,\frac{\pi R^4}{2}.$$

Eingesetzt:

$$J = \frac{m}{\pi R^2}\cdot\frac{\pi R^4}{2} = \frac{mR^2}{2}.$$

**Im Bild:** Sobald Gebiet und Integrand nur vom Radius abhängen, ist die Winkel-Integration ein bloßer Faktor $2\pi$. Übrig
bleibt ein Integral über $r$, in dem der Flächenfaktor $r$ mitläuft — die äußeren Ringe des Spinnennetzes zählen mehr.
::::

## Das Gauß-Integral

Die Glockenkurve $e^{-x^2}$ hat keine Stammfunktion, die sich mit elementaren Funktionen schreiben lässt. Ihr Integral über die
ganze Zahlengerade lässt sich trotzdem ausrechnen — über einen Umweg durch die Ebene:

:::formel
$$\int_{-\infty}^{\infty}e^{-x^2}\,dx = \sqrt\pi.$$
:::

**So liest man das:** Links steht ein uneigentliches Integral, der Grenzwert der Integrale über immer größere Intervalle. Die
Fläche unter der Glockenkurve ist endlich, obwohl die Kurve nirgends null wird.

**Im Bild:** Statt der Glockenkurve betrachtet man den Glockenberg $e^{-(x^2+y^2)}$ über der Ebene. Er ist rund; in
Polarkoordinaten hängt er nur vom Radius ab, und dort liefert der Flächenfaktor $r$ genau die innere Ableitung, die zum
Integrieren fehlte.

:::grafik
Szene: hoema3/koordinatentransformationen/01-glockenberg-sandwich · Vorlage: flaeche-3d-mit-draufsicht
Links der Glockenberg $e^{-(x^2+y^2)}$ als Fläche über der Ebene, rechts die Draufsicht mit drei Grundflächen: der Kreisscheibe
vom Radius $R$, dem Quadrat $[-R,R]^2$ und der Kreisscheibe vom Radius $\sqrt2\,R$ durch die Ecken des Quadrats. Ein Regler
für $R$ lässt alle drei wachsen; drei Zähler zeigen die Volumina über ihnen, bei den Kreisen $\pi(1-e^{-R^2})$ und
$\pi(1-e^{-2R^2})$. Kernaussage: Das Volumen über dem Quadrat ist eingeklemmt, und beide Schranken streben gegen $\pi$.
(Blau = Glockenberg, rot = Quadrat, orange = Kreise, grau = Achsen.)
:::

:::herleitung
**Schritt 1: der Glockenberg über einer Kreisscheibe.** In Polarkoordinaten ist

$$\int_{S_R}e^{-(x^2+y^2)}\,d(x,y) = \int_0^R\int_0^{2\pi}e^{-r^2}\,r\,d\varphi\,dr = 2\pi\int_0^R e^{-r^2}\,r\,dr.$$

Weil $-\frac12e^{-r^2}$ die Ableitung $e^{-r^2}\,r$ hat, folgt

$$2\pi\int_0^R e^{-r^2}\,r\,dr = 2\pi\Big[-\frac12\,e^{-r^2}\Big]_0^R = \pi\big(1-e^{-R^2}\big).$$

Für $R\to\infty$ strebt das gegen $\pi$.

**Schritt 2: das Quadrat dazwischen.** Das Integral der Glockenkurve bis $R$ ist

$$g(R) := \int_{-R}^{R}e^{-x^2}\,dx.$$

Nach Fubini, mit $e^{-(x^2+y^2)}$ als Produkt von $e^{-x^2}$ und $e^{-y^2}$, ist

$$\int_{[-R,R]^2}e^{-(x^2+y^2)}\,d(x,y) = \int_{-R}^{R}\Big(\int_{-R}^{R}e^{-x^2}\,dx\Big)\,e^{-y^2}\,dy.$$

Das innere Integral ist $g(R)$; man zieht es vor das äußere, und das äußere ist noch einmal $g(R)$. Das Integral über das
Quadrat ist also $g(R)^2$.

Das Quadrat enthält die Kreisscheibe $S_R$ und liegt in der Kreisscheibe vom Radius $\sqrt2\,R$, die durch seine Ecken geht.
Weil der Integrand positiv ist, wächst das Integral mit dem Gebiet, und Schritt 1 für beide Radien gibt

$$\pi\big(1-e^{-R^2}\big) \le g(R)^2 \le \pi\big(1-e^{-2R^2}\big).$$

**Schritt 3: der Grenzwert.** Beide Schranken streben für $R\to\infty$ gegen $\pi$, also nach dem Sandwich-Prinzip auch
$g(R)^2$. Weil der Integrand positiv ist, wachsen die Integrale über $[0,b]$ und $[-b,0]$ mit $b$ und bleiben unter
$\sqrt\pi$. Beide uneigentlichen Hälften existieren also, und ihre Summe ist der Grenzwert:

$$\int_{-\infty}^{\infty}e^{-x^2}\,dx = \lim_{R\to\infty}g(R) = \sqrt\pi.$$

**Im Bild:** Das Volumen über dem Quadrat liegt zwischen den Volumina über zwei Kreisscheiben, und beide fassen für großes
$R$ fast den ganzen Glockenberg.
:::

::::beispiel Die Glocke in Zahlen
Die beiden Schranken aus der Herleitung,

$$\text{unten: }\ \pi\big(1-e^{-R^2}\big), \qquad \text{oben: }\ \pi\big(1-e^{-2R^2}\big),$$

für zwei Radien, dazwischen der numerische Wert von $g(R)^2$:

| $R$ | unten | $g(R)^2$ | oben |
|---|---|---|---|
| $1$ | $1{,}986$ | $2{,}231$ | $2{,}716$ |
| $2$ | $3{,}084$ | $3{,}112$ | $3{,}141$ |

Für den kleinen Radius ist die Klemme noch weit, für den großen schon eng. Dort fehlt $g(R)^2$ nur noch knapp ein Prozent
an $\pi\approx3{,}1416$, denn die Glocke ist außerhalb von $[-2,2]$ fast null.

**Die Normalverteilung**, die Glockenkurve der Statistik, folgt mit der Substitution

$$t = \sqrt2\,x, \qquad dt = \sqrt2\,dx,$$

auf $[-R,R]$ und dann im Grenzwert:

$$\int_{-\infty}^{\infty}e^{-t^2/2}\,dt = \sqrt2\int_{-\infty}^{\infty}e^{-x^2}\,dx = \sqrt{2\pi}.$$

Deshalb steht in ihrer Dichte

$$\frac{1}{\sqrt{2\pi}}\,e^{-t^2/2}$$

der Vorfaktor $\frac{1}{\sqrt{2\pi}}$: Er macht die Gesamtwahrscheinlichkeit zu $1$.

**Im Bild:** Der Glockenberg hat das Volumen $\pi$. Das Quadrat über $[-R,R]^2$ fasst schon fast alles davon, und das Volumen
über dem Quadrat ist das Quadrat der Fläche unter der Glockenkurve.
::::

## Bedeutung und Ausblick

Der Transformationssatz ist die mehrdimensionale Substitutionsregel. Er erlaubt, ein Integral in die Koordinaten zu
übersetzen, in denen Gebiet und Integrand einfach werden — und der Flächenfaktor $\lvert\det D\vec\Phi\rvert$ sagt, wie man
dabei die Maschen umrechnet. In der Elektrotechnik rechnet man so Flüsse durch kreisförmige Querschnitte, Ladungen auf
Scheiben und Trägheitsmomente von Rotoren.

Der Satz gilt in jeder Dimension. Im Raum werden aus dem Spinnennetz die __Zylinderkoordinaten__ mit dem Volumenelement
$r\,dr\,d\varphi\,dz$ und die __Kugelkoordinaten__ mit $r^2\sin\theta\,dr\,d\theta\,d\varphi$, wobei $\theta$ der Winkel gegen
die $z$-Achse ist. Mit ihnen berechnet der nächste Artikel Volumina von Rotationskörpern und Kugeln und klärt, wann Integrale
über Funktionen mit einer Singularität im Ursprung noch endlich sind.

:::kern
- Eine lineare Abbildung $A$ ändert jedes Volumen um den Betrag ihrer Determinante: $\mathrm{vol}(AQ)=\lvert\det A\rvert\,\mathrm{vol}(Q)$.
- __Transformationssatz__: $\int_{\vec\Phi(B)}f\,d^2x=\int_B f(\vec\Phi)\,\lvert\det D\vec\Phi\rvert\,d^2u$ für injektives, nirgends flachdrückendes $\vec\Phi$.
- Im Bild zählt jede Masche des verzerrten Gummituchs mit dem Flächenfaktor $\lvert\det D\vec\Phi\rvert$ — unter der Lupe ist sie ein Parallelogramm.
- Ohne Injektivität liegt das Tuch doppelt, und die rechte Seite zählt doppelt.
- Beweis in der Ebene: $f$ als Rotation schreiben, Stokes auf dem Bild, Kettenregel, Stokes auf $B$ — übrig bleibt $\det D\vec\Phi$.
- In einer Dimension ist das die Substitutionsregel; dort ersetzen orientierte Grenzen den Betrag.
- __Polarkoordinaten__: Der Flächenfaktor ist $r$, das Flächenelement $r\,dr\,d\varphi$ — die Maschen des Spinnennetzes wachsen nach außen.
- Am Mittelpunkt sind die Voraussetzungen verletzt, die Formel gilt trotzdem: Nabe und Keil werden beliebig klein.
- __Gauß-Integral__: $\int_{-\infty}^{\infty}e^{-x^2}dx=\sqrt\pi$, über den Glockenberg in Polarkoordinaten und ein Sandwich zwischen zwei Kreisscheiben.
:::

:::quiz
F: Warum ändert eine lineare Abbildung $A$ der Ebene jede Fläche um den Faktor $\lvert\det A\rvert$?
A: Das Einheitsquadrat wird auf das Parallelogramm aus den Spalten $\vec a,\vec b$ abgebildet. Nach der Schnürsenkelformel hat es die orientierte Fläche $\det(\vec a\,|\,\vec b)=\det A$, weil die Determinante linear in jeder Spalte ist und bei gleichen Spalten verschwindet; laufen die Ecken im Uhrzeigersinn, ist das das Negative der Fläche. Ein Rechteck mit den Kanten $p,q$ geht in das Parallelogramm aus $p\vec a$ und $q\vec b$ über, mit der Fläche $pq\,\lvert\det A\rvert$.
F: Was besagt der Transformationssatz, und was bedeutet er im Bild des Gummituchs?
A: Ist $\vec\Phi$ stetig differenzierbar, auf dem regulären Bereich $B$ injektiv mit $\det D\vec\Phi\neq0$ und $\vec\Phi(B)$ wieder ein regulärer Bereich, so ist $\int_{\vec\Phi(B)}f\,d^2x=\int_B f(\vec\Phi(\vec u))\,\lvert\det D\vec\Phi(\vec u)\rvert\,d^2u$ für stetiges $f$. Das verzerrte Tuch besteht aus Maschen, die unter der Lupe Parallelogramme sind; jede hat die Fläche des ursprünglichen Quadrats mal $\lvert\det D\vec\Phi\rvert$.
F: Was geht schief, wenn $\vec\Phi$ nicht injektiv ist?
A: Dann liegt das Tuch an manchen Stellen doppelt, und die rechte Seite zählt diese Maschen doppelt. Beim Falten $(u_1,u_2)\mapsto(u_1^2,u_2)$ von $[-1,1]\times[0,1]$ auf das Einheitsquadrat gibt das Integral von $\lvert2u_1\rvert$ den Wert $2$, die Fläche ist aber $1$.
F: Wie verläuft der Beweis in der Ebene über den Satz von Stokes?
A: Man schreibt $f$ als Rotation eines Felds $\vec F$, durch Integration längs der Strahlen einer sternförmigen Menge, und wendet Stokes auf $\vec\Phi(B)$ an. Mit der Kettenregel wird das Randintegral zu einem Kurvenintegral längs des Randes von $B$ für die Felder $\vec H_j=(F_j\circ\vec\Phi)\nabla\Phi_j$. Stokes auf $B$ und der Satz von Schwarz lassen als Rotation genau $(f\circ\vec\Phi)\det D\vec\Phi$ übrig; bei negativer Determinante kehrt sich die Randorientierung um, und es bleibt der Betrag.
F: Warum steht in der Substitutionsregel $\psi'$ ohne Betrag, im Transformationssatz aber der Betrag der Determinante?
A: In einer Dimension führt man die Richtung über die Grenzen mit: Läuft $\psi$ rückwärts, sind die Grenzen vertauscht, und dieses Minuszeichen gleicht das negative $\psi'$ aus — bei $\psi(u)=3-u$ geben beide Seiten $-4$, mit Betrag und Bildintervall beide $4$. In der Ebene integriert man über Mengen ohne Richtung, deshalb zählt nur der Flächenfaktor. Die Regel gilt in einer Dimension sogar für nicht injektive $\psi$ wie $u^2$ auf $[-1,1]$: Die beiden Lagen heben sich mit Vorzeichen auf.
F: Was ergibt der Transformationssatz für die Ellipse mit den Halbachsen $2$ und $3$?
A: Die Abbildung $(2u_1,3u_2)$ bildet die Einheitskreisscheibe injektiv auf die Ellipse ab und hat die Determinante $6$. Die Fläche ist also $6$ mal die Fläche der Kreisscheibe, $6\pi$ — dasselbe wie mit der Planimeter-Formel.
F: Warum ist in Polarkoordinaten das Flächenelement $r\,dr\,d\varphi$?
A: Die Jacobi-Matrix von $(r\cos\varphi,r\sin\varphi)$ hat die Spalten $(\cos\varphi,\sin\varphi)$ und $(-r\sin\varphi,r\cos\varphi)$ und die Determinante $r\cos^2\varphi+r\sin^2\varphi=r$. Im Bild ist eine Masche des Spinnennetzes fast ein Rechteck mit den Seiten $dr$ und dem Bogen $r\,d\varphi$; weiter außen überstreicht derselbe Winkelschritt mehr.
F: Warum gilt die Polarformel, obwohl $\vec\Phi$ am Mittelpunkt die Voraussetzungen des Satzes verletzt?
A: Auf $[0,R]\times[0,2\pi]$ ist $\vec\Phi$ nicht injektiv und hat bei $r=0$ die Determinante null. Auf $[\varepsilon,R]\times[\varepsilon,2\pi]$ gilt der Satz; im Bild fehlen nur die Nabe vom Radius $\varepsilon$ und ein Keil mit dem Winkel $\varepsilon$, zusammen höchstens $\pi\varepsilon^2+\frac{\varepsilon}{2}R^2$ an Fläche, und rechts zwei schmale Streifen. Weil $f$ beschränkt ist, gehen beide Unterschiede für $\varepsilon\to0$ gegen null.
F: Wie berechnet man mit Polarkoordinaten den runden Laib und das Trägheitsmoment einer Scheibe?
A: Der Laib mit der Höhe $1-x^2-y^2$ über der Einheitskreisscheibe hat das Volumen $\int_0^1\int_0^{2\pi}(1-r^2)\,r\,d\varphi\,dr=2\pi(\frac12-\frac14)=\frac{\pi}{2}$, wie zuvor mit Scheiben. Das Trägheitsmoment ist die Dichte $\frac{m}{\pi R^2}$ mal $\int_{S_R}(x^2+y^2)\,d(x,y)$, also mal $\frac{\pi R^4}{2}$, zusammen $\frac{mR^2}{2}$.
F: Wie entsteht das Gauß-Integral $\int_{-\infty}^{\infty}e^{-x^2}dx=\sqrt\pi$, und warum steht in der Normalverteilung der Vorfaktor $\frac{1}{\sqrt{2\pi}}$?
A: In Polarkoordinaten liefert der Flächenfaktor $r$ die innere Ableitung: Der Glockenberg $e^{-(x^2+y^2)}$ hat über der Kreisscheibe vom Radius $R$ das Volumen $\pi(1-e^{-R^2})$. Das Quadrat $g(R)^2$ der Fläche unter der Glocke bis $R$ ist das Volumen über $[-R,R]^2$ und liegt zwischen den Volumina über den Scheiben vom Radius $R$ und $\sqrt2R$; beide streben gegen $\pi$, also ist das Integral $\sqrt\pi$. Mit $t=\sqrt2x$ folgt $\int e^{-t^2/2}dt=\sqrt{2\pi}$, und der Vorfaktor $\frac{1}{\sqrt{2\pi}}$ macht die Gesamtwahrscheinlichkeit zu $1$.
:::
