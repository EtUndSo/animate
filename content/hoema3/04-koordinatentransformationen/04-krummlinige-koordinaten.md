---
title: Differentialoperatoren in krummlinigen Koordinaten
pfad: Elektrotechnik / 3. Semester / Höhere Mathematik 3 / Koordinatentransformationen
order: 3040400
summary: Von Grund auf – wie Gradient, Divergenz und Laplace in Polar-, Zylinder- und Kugelkoordinaten aussehen. Der Schlüssel sind die Maßfaktoren $h_u=|\partial\Phi/\partial u|$, die messen, wie stark eine Koordinate den Raum streckt. Mit ihnen bekommt der Gradient Faktoren $1/h_u$, und die Laplace-Operatoren in Polar-/Kugelkoordinaten erhalten ihre bekannte Gestalt – inklusive der radialen Form, mit der das Coulomb-Potential sofort als harmonisch fällt.
tags: krummlinige Koordinaten, Maßfaktoren, orthogonale Koordinaten, Gradient, Divergenz, Laplace-Operator, Zylinderkoordinaten, Kugelkoordinaten
---

:::grafik
Einstiegs-Animation: Die Koordinatenlinien von Polar-/Kugelkoordinaten (Kreise und Strahlen) mit dem **lokalen
Dreibein** $\hat e_u,\hat e_v,\hat e_w$, das — anders als in kartesischen Koordinaten — an jedem Punkt in eine
andere Richtung zeigt (es „dreht sich mit"). Daneben die __Maßfaktoren__: Ein Schritt $d\varphi$ im Winkel
überstreicht den Bogen $r\,d\varphi$ — der Faktor $h_\varphi=r$. Eine Formelkachel zeigt, wie dadurch im Gradienten
überall ein $1/h_u$ auftaucht. Kernbotschaft: In krummlinigen Koordinaten drehen sich die Basisvektoren mit, und
die Maßfaktoren $h_u$ übersetzen zwischen Koordinatenschritt und echter Länge.
:::

:::konzept
In Polar-, Zylinder- und Kugelkoordinaten rechnet man zwar bequem, aber die vertrauten Operatoren $\nabla$,
$\operatorname{div}$, $\Delta$ sehen anders aus als in kartesischen Koordinaten. Der Grund: Die Basisvektoren
$\hat e_u,\hat e_v,\hat e_w$ **drehen sich** von Punkt zu Punkt mit, und jede Koordinate „zählt" unterschiedlich —
ein Winkelschritt $d\varphi$ ist weiter außen eine größere Strecke. Diesen Umrechnungsfaktor fassen die
__Maßfaktoren__ $h_u$. Mit ihnen schreibt man Gradient, Divergenz und Laplace in jedem orthogonalen
Koordinatensystem hin — und versteht, woher die „Zusatzterme" in der Polar-/Kugel-Laplace kommen, die man zum
Lösen symmetrischer Feldprobleme (Wärmeleitung, Potentiale) ständig braucht.
:::

**Worum es geht:** Wir führen __krummlinige (orthogonale) Koordinaten__ mit ihren __Maßfaktoren__ $h_u$ ein und
leiten __Gradient__, __Divergenz__ und __Laplace-Operator__ in diesen Koordinaten her (Polar/Zylinder/Kugel).

## Koordinatenvektorfelder und Maßfaktoren

Eine stetig differenzierbare, injektive Abbildung $\Phi(u,v,w)=(x,y,z)$ mit $\det D\Phi\ne0$ definiert ein
__krummliniges Koordinatensystem__ $(u,v,w)$. Die **natürlichen Koordinatenvektorfelder** sind die partiellen
Ableitungen $a_u=\partial\Phi/\partial u$ usw. — sie zeigen tangential zu den Koordinatenlinien. Ihre Längen sind
die __Maßfaktoren__, und auf Länge 1 normiert ergeben sich die **normierten Koordinatenvektorfelder**:

$$h_u = \left|\frac{\partial\Phi}{\partial u}\right|, \qquad \hat e_u = \frac{1}{h_u}\frac{\partial\Phi}{\partial u} \qquad(\text{analog } v,w).$$

Anders als in kartesischen Koordinaten **drehen** sich diese Basisvektoren mit dem Ort mit. Bilden sie in jedem
Punkt eine **Orthonormalbasis**, spricht man von einem __orthogonalen__ Koordinatensystem (Polar, Zylinder, Kugel
sind alle orthogonal). Die Maßfaktoren der wichtigsten Systeme:

- **Polar** $(r,\varphi)$: $h_r=1$, $h_\varphi=r$.
- **Zylinder** $(r,\varphi,z)$: $h_r=1$, $h_\varphi=r$, $h_z=1$.
- **Kugel** $(r,\vartheta,\varphi)$: $h_r=1$, $h_\vartheta=r$, $h_\varphi=r\sin\vartheta$.

(Man erkennt die Jacobi-Determinante wieder: $\det D\Phi = h_u h_v h_w$ — bei Kugel $1\cdot r\cdot r\sin\vartheta =
r^2\sin\vartheta$, genau der Volumenfaktor.)

:::grafik
Das lokale Dreibein in Kugelkoordinaten ($\hat e_r,\hat e_\vartheta,\hat e_\varphi$) an einem Punkt; die drei
Koordinatenlinien mit ihren Bogenlängen $dr$, $h_\vartheta\,d\vartheta=r\,d\vartheta$,
$h_\varphi\,d\varphi=r\sin\vartheta\,d\varphi$. Beschriftung „Maßfaktor = Koordinatenschritt → echte Länge".
:::

## Der Gradient

In einem orthogonalen Koordinatensystem zerlegt man jedes Vektorfeld als $F=F_u\hat e_u+F_v\hat e_v+F_w\hat e_w$
(mit $F_u=F\cdot\hat e_u$). Für den Gradienten einer Funktion $f$ ergibt sich — jede Ableitung durch ihren
Maßfaktor geteilt — die Transformationsformel

$$\nabla f = \frac{1}{h_u}\frac{\partial f}{\partial u}\,\hat e_u + \frac{1}{h_v}\frac{\partial f}{\partial v}\,\hat e_v + \frac{1}{h_w}\frac{\partial f}{\partial w}\,\hat e_w.$$

Das $1/h_u$ ist anschaulich: Der Gradient misst Änderung **pro Länge**, nicht pro Koordinate — und eine
Koordinate der Länge $h_u\,du$ muss entsprechend umgerechnet werden. In **Zylinder-/Polarkoordinaten** heißt das

$$\nabla f = \frac{\partial f}{\partial r}\,\hat e_r + \frac{1}{r}\frac{\partial f}{\partial \varphi}\,\hat e_\varphi + \frac{\partial f}{\partial z}\,\hat e_z.$$

## Divergenz und Laplace

Bei der Divergenz muss man zusätzlich beachten, dass sich die Basisvektoren **mitdrehen** — beim Ableiten von $F$
werden also auch die $\hat e$ abgeleitet (in Zylinderkoordinaten etwa $\frac{\partial}{\partial\varphi}\hat e_r=
\hat e_\varphi$ und $\frac{\partial}{\partial\varphi}\hat e_\varphi=-\hat e_r$). Für Zylinderkoordinaten ergibt
sich daraus

$$\operatorname{div}E = \frac{1}{r}\frac{\partial}{\partial r}(r E_r) + \frac{1}{r}\frac{\partial E_\varphi}{\partial\varphi} + \frac{\partial E_z}{\partial z}.$$

Setzt man $E=\nabla f$ ein, folgt der __Laplace-Operator in Zylinder-/Polarkoordinaten__:

$$\Delta f = \frac{\partial^2 f}{\partial r^2} + \frac{1}{r}\frac{\partial f}{\partial r} + \frac{1}{r^2}\frac{\partial^2 f}{\partial\varphi^2} + \frac{\partial^2 f}{\partial z^2}.$$

Allgemein gilt in **orthogonalen** Koordinaten die kompakte Formel

$$\Delta f = \frac{1}{h_u h_v h_w}\left[\frac{\partial}{\partial u}\!\Big(\frac{h_v h_w}{h_u}\frac{\partial f}{\partial u}\Big) + \frac{\partial}{\partial v}\!\Big(\frac{h_u h_w}{h_v}\frac{\partial f}{\partial v}\Big) + \frac{\partial}{\partial w}\!\Big(\frac{h_u h_v}{h_w}\frac{\partial f}{\partial w}\Big)\right].$$

:::grafik
Links die rotierenden Basisvektoren in Zylinderkoordinaten mit den Ableitungen $\partial_\varphi\hat e_r=\hat e_\varphi$,
$\partial_\varphi\hat e_\varphi=-\hat e_r$ (Ursprung des Zusatzterms $\tfrac1r E_r$ in der Divergenz). Rechts die
allgemeine orthogonale Laplace-Formel mit den Maßfaktoren $h_u h_v h_w$.
:::

**Eigenes Beispiel (Kugel-Laplace).** Mit den Kugel-Maßfaktoren $h_r=1$, $h_\vartheta=r$, $h_\varphi=r\sin\vartheta$
liefert die allgemeine Formel den __Laplace-Operator in Kugelkoordinaten__:

$$\Delta f = \frac{1}{r^2}\frac{\partial}{\partial r}\!\Big(r^2\frac{\partial f}{\partial r}\Big) + \frac{1}{r^2\sin\vartheta}\frac{\partial}{\partial\vartheta}\!\Big(\sin\vartheta\,\frac{\partial f}{\partial\vartheta}\Big) + \frac{1}{r^2\sin^2\vartheta}\frac{\partial^2 f}{\partial\varphi^2}.$$

Für eine **radialsymmetrische** Funktion $f=f(r)$ bleibt nur der erste Term, $\Delta f = \frac{1}{r^2}(r^2 f')' =
f''+\frac{2}{r}f'$. Probe am Coulomb-Potential $f=\frac1r$: $f'=-\frac1{r^2}$, $r^2 f'=-1$, also
$\Delta f=\frac1{r^2}\cdot 0 = 0$ — das Coulomb-Potential ist harmonisch (für $r\ne0$), passend zu Kapitel 1.

**Stolperstein:** (1) Die Formeln gelten für **orthogonale** Koordinaten (Dreibein orthonormal). (2) Die
„Zusatzterme" (wie $\frac1r\partial_r$) sind **keine Willkür**, sondern kommen aus den Maßfaktoren bzw. der
mitdrehenden Basis — man darf sie nie vergessen. (3) Die Reihenfolge $(r,\vartheta,\varphi)$ und die
Winkelkonvention müssen zur gewählten Parametrisierung passen.

:::kern
Eine krummlinige Koordinatenabbildung $\Phi(u,v,w)$ hat __natürliche__ Vektorfelder $\partial\Phi/\partial u$ mit
Längen, den __Maßfaktoren__ $h_u=|\partial\Phi/\partial u|$, und __normierte__ $\hat e_u=\frac1{h_u}\partial\Phi/
\partial u$ (die sich mitdrehen). __Orthogonal__ = Dreibein orthonormal; dann $\det D\Phi=h_u h_v h_w$
(Polar $h_r=1,h_\varphi=r$; Zylinder $1,r,1$; Kugel $1,r,r\sin\vartheta$). __Gradient__
$\nabla f=\sum_i \frac{1}{h_i}\partial_i f\,\hat e_i$ (Polar/Zylinder $\partial_r f\,\hat e_r+\frac1r\partial_\varphi
f\,\hat e_\varphi+\partial_z f\,\hat e_z$). __Divergenz__ Zylinder $\frac1r\partial_r(rE_r)+\frac1r\partial_\varphi
E_\varphi+\partial_z E_z$ (Basis dreht mit!). __Laplace__ Polar/Zylinder $\partial_{rr}f+\frac1r\partial_r f+\frac1{r^2}
\partial_{\varphi\varphi}f+\partial_{zz}f$; allgemein orthogonal $\Delta f=\frac{1}{h_u h_v h_w}\sum_i\partial_i(\frac{h_u h_v h_w}{h_i^2}\partial_i f)$;
Kugel $\frac1{r^2}\partial_r(r^2\partial_r f)+\frac1{r^2\sin\vartheta}\partial_\vartheta(\sin\vartheta\,\partial_\vartheta f)+\frac1{r^2\sin^2\vartheta}\partial_{\varphi\varphi}f$;
radial $f''+\frac2r f'$ (Coulomb $\tfrac1r$ harmonisch).
:::

Damit ist das Rechen-Handwerkszeug (Transformationen, Volumina, Potentiale, krummlinige Operatoren) komplett. Zum
Schluss der Vektoranalysis kommen die großen __Integralsätze im Raum__ — der Satz von Stokes über Flächen und der
Satz von Gauß für Volumina —, die Rand und Inneres im Dreidimensionalen verbinden. Das ist das nächste Kapitel.
