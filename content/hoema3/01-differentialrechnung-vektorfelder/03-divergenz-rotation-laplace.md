---
title: Divergenz, Rotation und Laplace-Operator
pfad: Elektrotechnik / 3. Semester / Höhere Mathematik 3 / Differentialrechnung für Vektorfelder
order: 3010300
summary: Von Grund auf – die drei zentralen Differentialoperatoren der Vektoranalysis, alle aus dem Nabla-Symbol gebaut. Die Divergenz $\operatorname{div}E=\nabla\cdot E$ misst die Quelldichte, die Rotation $\operatorname{rot}E=\nabla\times E$ die Wirbeldichte, und der Laplace-Operator $\Delta=\operatorname{div}\operatorname{grad}$ die „Krümmung" eines Feldes. Mit der Schlüsselidentität $\operatorname{rot}\operatorname{grad}\phi=0$ und der Harmonizität des Coulomb-Potentials.
tags: Divergenz, Rotation, curl, Laplace-Operator, Quelldichte, Wirbeldichte, harmonische Funktion, Nabla, rotationsfrei
---

:::grafik
Einstiegs-Animation: Das Nabla-Symbol $\nabla$ in der Mitte, aus dem drei Operatoren herauswachsen —
__Gradient__ (Skalar → Vektor, schon bekannt), __Divergenz__ (Vektor → Skalar) und __Rotation__ (Vektor →
Vektor). Rechts zwei kleine Vektorfeld-Ausschnitte: eines, bei dem aus einem kleinen Kästchen netto mehr Pfeile
**heraus**strömen als hinein (positive Divergenz = __Quelle__), und eines, bei dem die Pfeile um einen Punkt
**herumwirbeln** (von null verschiedene Rotation = __Wirbel__). Kernbotschaft: Aus dem einen Symbol $\nabla$
entstehen die drei Grundoperatoren, die „Quellen" und „Wirbel" eines Feldes messen.
:::

:::konzept
Der Gradient hat aus einem Skalarfeld ein Vektorfeld gemacht. Jetzt geht es umgekehrt und tiefer: Aus einem
**Vektorfeld** liest man zwei lokale Kennzahlen ab — wie stark es an einem Punkt **entspringt** (die __Divergenz__,
eine Quelldichte) und wie stark es dort **wirbelt** (die __Rotation__, eine Wirbeldichte). Zusammen mit dem
__Laplace-Operator__ (der zweiten Ableitung der Feldtheorie) sind das die Grundbausteine, aus denen später alle
großen Integralsätze (Gauß, Stokes) und die Feldgleichungen der Physik (Maxwell, Wärmeleitung, Poisson) aufgebaut
werden. Alle drei entstehen formal aus **einem** Symbol, dem Nabla-Operator $\nabla$.
:::

**Worum es geht:** Wir definieren __Divergenz__ $\nabla\cdot E$ (Quelldichte), den __Laplace-Operator__
$\Delta=\nabla\cdot\nabla$ und die __Rotation__ $\nabla\times E$ (Wirbeldichte, in 3D und 2D) und zeigen die
Schlüsselidentität $\operatorname{rot}\operatorname{grad}\phi=0$.

## Die Divergenz: Quelldichte eines Feldes

Für ein differenzierbares Vektorfeld $E=(E_1,\ldots,E_n)^T$ auf einer offenen Menge $U\subset\mathbb{R}^n$ ist die
__Divergenz__ die Summe der „diagonalen" partiellen Ableitungen:

$$\operatorname{div} E := \nabla\cdot E = \sum_{j=1}^{n}\frac{\partial E_j}{\partial x_j}.$$

Sie macht aus einem Vektorfeld wieder eine **Funktion** (ein Skalarfeld). Anschaulich misst sie die lokale
__Quelldichte__: Ist $\operatorname{div}E>0$, so „entspringt" das Feld an diesem Punkt (eine **Quelle**, netto
strömt mehr heraus als hinein); ist sie negativ, verschwindet dort Feld (eine **Senke**); ist sie null, fließt
genauso viel hinein wie heraus (das Feld ist __quellenfrei__). Diese Deutung wird später der __Gaußsche
Integralsatz__ präzise machen.

Für ein **Gradientenfeld** $E=\nabla\phi$ ist die Divergenz gerade die Summe der zweiten Ableitungen,
$\operatorname{div}\nabla\phi = \sum_j \partial^2\phi/\partial x_j^2$ — das führt direkt zum Laplace-Operator. Für
Rechnungen nützlich ist die **Produktregel** (Skalarfeld $\phi$ mal Vektorfeld $F$):

$$\operatorname{div}(\phi\,F) = \nabla\phi\cdot F + \phi\,\operatorname{div}F.$$

:::grafik
Zwei Vektorfeld-Ausschnitte mit je einem kleinen Kästchen: links eine Quelle ($\operatorname{div}E>0$, Pfeile
strömen auswärts), rechts eine Senke ($\operatorname{div}E<0$, Pfeile einwärts), dazwischen ein quellenfreier Fall
($\operatorname{div}E=0$, gleich viel rein wie raus). Darunter die Formel $\operatorname{div}E=\sum_j\partial E_j/\partial x_j$.
:::

**Beispiel (Divergenz radialsymmetrischer Felder).** Für $E(x)=f(r)\,\hat e_r$ (mit $r=|x|$, $\hat e_r=x/r$)
schreibt man $E=\frac{f(r)}{r}\,x$ und wendet die Produktregel mit $\phi=\frac{f(r)}{r}$ und $F=x$ an. Mit
$\operatorname{div}x=n$, $\nabla\big(\tfrac{f(r)}{r}\big)=\tfrac{f'(r)r-f(r)}{r^2}\hat e_r$ und $\hat e_r\cdot x=r$:

$$\operatorname{div} E = \frac{f'(r)r-f(r)}{r} + n\,\frac{f(r)}{r} = f'(r) + (n-1)\,\frac{f(r)}{r}.$$

Diese kompakte Formel erspart in der Feldtheorie viel Rechnerei.

## Der Laplace-Operator

Wendet man nacheinander Gradient und Divergenz an, entsteht der wichtigste Operator **zweiter** Ordnung, der
__Laplace-Operator__. Für eine zweimal differenzierbare Funktion $\phi:U\to\mathbb{R}$ ist

$$\Delta\phi := \sum_{j=1}^{n}\frac{\partial^2\phi}{\partial x_j^2} = \operatorname{div}(\nabla\phi), \qquad\text{formal}\quad \Delta = \nabla\cdot\nabla.$$

Wegen dieser Produktform schreibt man ihn in den Natur- und Ingenieurwissenschaften oft $\nabla^2$. Laut
Definition wirkt $\Delta$ auf **Skalarfelder**; auf ein Vektorfeld $F=(F_1,\ldots,F_n)^T$ wendet man ihn
**komponentenweise** an, $\Delta F = (\Delta F_1,\ldots,\Delta F_n)^T$. Eine Funktion mit $\Delta\phi=0$ heißt
__harmonisch__ — solche Funktionen beschreiben Gleichgewichtszustände (Potentiale im ladungsfreien Raum,
stationäre Temperaturverteilungen).

**Beispiel (Harmonizität des Coulomb-Potentials).** Für $u(x)=\dfrac{Q}{4\pi r}$ auf $\mathbb{R}^3\setminus\{0\}$
ist (voriger Artikel) $E=-\nabla u=\dfrac{Q}{4\pi r^2}\hat e_r$, also ein radiales Feld mit $f(r)=\frac{Q}{4\pi r^2}$.
Die radiale Divergenzformel mit $n=3$ gibt

$$\Delta u = \operatorname{div}(\nabla u) = -\operatorname{div}E = -\Big(f'(r) + 2\,\tfrac{f(r)}{r}\Big) = -\Big(-\tfrac{2Q}{4\pi r^3} + \tfrac{2}{r}\tfrac{Q}{4\pi r^2}\Big) = 0 \quad\text{in } \mathbb{R}^3\setminus\{0\}.$$

Das Coulomb-Potential ist also **harmonisch** außerhalb der Ladung — ein Spezialfall der Poisson-Gleichung, auf
die wir im Kapitel über die Integralsätze zurückkommen.

## Die Rotation in 3D

Für ein differenzierbares Vektorfeld $E=(E_1,E_2,E_3)$ auf $U\subset\mathbb{R}^3$ ist die __Rotation__ (englisch
__curl__) das formale Kreuzprodukt von $\nabla$ mit $E$:

$$\operatorname{rot} E := \nabla\times E = \begin{pmatrix} \dfrac{\partial E_3}{\partial x_2} - \dfrac{\partial E_2}{\partial x_3} \\[2mm] \dfrac{\partial E_1}{\partial x_3} - \dfrac{\partial E_3}{\partial x_1} \\[2mm] \dfrac{\partial E_2}{\partial x_1} - \dfrac{\partial E_1}{\partial x_2} \end{pmatrix}.$$

Sie macht aus einem Vektorfeld wieder ein **Vektorfeld**. Ihre Komponenten sind ein Maß für die lokale
__Wirbeldichte__ um die jeweilige Koordinatenachse — wie stark das Feld dort „zirkuliert". Das wird später der
__Stokessche Integralsatz__ präzise machen.

Zwei praktische Schreibweisen: Mit dem __Levi-Civita-Symbol__ $\varepsilon_{ijk}\in\{-1,0,1\}$ ($\varepsilon_{123}=1$,
zyklisch) ist $(\operatorname{rot}F)_i = \sum_{j,k=1}^{3}\varepsilon_{ijk}\,\dfrac{\partial F_k}{\partial x_j}$. Als
**Merkregel** dient die Determinantenschreibweise (formal nach der ersten Spalte entwickelt):

$$\operatorname{rot} F = \det\begin{pmatrix} \hat e_1 & \partial/\partial x_1 & F_1 \\ \hat e_2 & \partial/\partial x_2 & F_2 \\ \hat e_3 & \partial/\partial x_3 & F_3 \end{pmatrix}.$$

**Stolperstein:** Die (dreikomponentige) Rotation in dieser Form gibt es nur im $\mathbb{R}^3$ — das Kreuzprodukt
ist eine Besonderheit von drei Dimensionen. Die Divergenz dagegen ist in jeder Dimension definiert.

:::grafik
Ein wirbelndes 3D-Vektorfeld um eine Achse; ein kleines „Schaufelrad" an einem Punkt, dessen Drehachse und
Drehsinn den Rotationsvektor $\operatorname{rot}E$ anzeigen (Betrag = Wirbelstärke). Daneben die
Determinanten-Merkregel.
:::

## Die Rotation in 2D

Betrachtet man ein ebenes Feld $E=(E_1,E_2,0)$, das nicht von $x_3$ abhängt, so hat seine 3D-Rotation nur eine
von null verschiedene Komponente (die dritte). Das motiviert die __Rotation in 2D__ als **skalare** Größe:

$$\operatorname{rot} E = \frac{\partial E_2}{\partial x_1} - \frac{\partial E_1}{\partial x_2}.$$

In der Ebene sind **sowohl** Divergenz als auch Rotation skalare Funktionen, und sie gehen durch eine
$90^\circ$-Drehung des Feldes ineinander über: Mit $F^{\perp} = (-F_2, F_1)$ (das um $\tfrac{\pi}{2}$ gegen den
Uhrzeigersinn gedrehte Feld) gilt

$$\operatorname{div} F = \operatorname{rot} F^{\perp}, \qquad \operatorname{div} F^{\perp} = -\operatorname{rot} F.$$

Quelle und Wirbel sind in der Ebene also „dasselbe, um 90° gedreht" — eine Symmetrie, die beim Rechnen mit
ebenen Feldern (und später bei Green/Gauß in der Ebene) immer wieder auftaucht.

## Gradientenfelder sind wirbelfrei: $\operatorname{rot}\operatorname{grad}\phi = 0$

Jetzt schließt sich der Kreis zur __Integrabilitätsbedingung__ aus dem vorigen Artikel. Ist $F=\nabla\phi$ ein
(zweimal stetig differenzierbares) Gradientenfeld, so gelten die Integrabilitätsbedingungen
$\dfrac{\partial F_k}{\partial x_j} = \dfrac{\partial F_j}{\partial x_k}$ für alle $j,k$ (das ist die Symmetrie der
Jacobi-Matrix, Satz von Schwarz). In $n=2,3$ ist das genau gleichbedeutend mit dem Verschwinden der Rotation:

$$\operatorname{rot}\big(\nabla\phi\big) = 0 \qquad\text{(für alle } \phi\in C^2\text{).}$$

Man prüft das direkt: Die erste Komponente von $\operatorname{rot}\nabla\phi$ ist $\partial_{x_2}\partial_{x_3}\phi -
\partial_{x_3}\partial_{x_2}\phi$, und das ist nach Schwarz null (ebenso die anderen Komponenten).

**Das ist eine notwendige Bedingung:** Ein Gradientenfeld ist stets **rotationsfrei**. Die spannende Kernfrage der
Vektoranalysis ist die **Umkehrung** — ist jedes rotationsfreie Feld ein Gradientenfeld? Im Allgemeinen **nein**
(es hängt von der Gestalt des Gebiets ab). Unter welchen Zusatzvoraussetzungen die Bedingung $\operatorname{rot}F=0$
doch ausreicht, klärt später der Stokessche Integralsatz (Stichwort: einfach zusammenhängende Gebiete,
Poincaré-Lemma).

:::grafik
Links ein Gradientenfeld (Pfeile stehen senkrecht auf den Niveaulinien, laufen „bergab/bergauf", kein Wirbel) mit
der Marke $\operatorname{rot}=0$. Rechts ein echtes Wirbelfeld (Pfeile kreisen) mit $\operatorname{rot}\neq0$ —
„kann kein Gradientenfeld sein". Dazwischen der Pfeil „$\operatorname{rot}\operatorname{grad}\phi=0$ (Schwarz),
notwendig – Umkehrung: siehe Stokes".
:::

:::kern
Aus dem Nabla-Operator $\nabla$ entstehen drei Operatoren. Die __Divergenz__ $\operatorname{div}E=\nabla\cdot E=
\sum_j\partial E_j/\partial x_j$ (Vektor→Skalar) misst die __Quelldichte__ ($>0$ Quelle, $<0$ Senke, $=0$
quellenfrei); Produktregel $\operatorname{div}(\phi F)=\nabla\phi\cdot F+\phi\operatorname{div}F$; radial
$\operatorname{div}(f(r)\hat e_r)=f'(r)+(n-1)\tfrac{f(r)}{r}$. Der __Laplace-Operator__ $\Delta\phi=\sum_j\partial^2\phi/
\partial x_j^2=\operatorname{div}\nabla\phi=\nabla^2$ (2. Ordnung, skalar bzw. komponentenweise); $\Delta\phi=0$
heißt __harmonisch__ (z. B. Coulomb-Potential $\tfrac{Q}{4\pi r}$ in $\mathbb{R}^3\setminus\{0\}$). Die __Rotation__
(3D) $\operatorname{rot}E=\nabla\times E$ (Determinanten-/Levi-Civita-Merkregel, $(\operatorname{rot}F)_i=\sum
\varepsilon_{ijk}\partial F_k/\partial x_j$) misst die __Wirbeldichte__ (nur $\mathbb{R}^3$); in 2D skalar
$\operatorname{rot}E=\partial_{x_1}E_2-\partial_{x_2}E_1$ mit $\operatorname{div}F=\operatorname{rot}F^\perp$.
Schlüsselidentität: $\operatorname{rot}\operatorname{grad}\phi=0$ (Schwarz) — Gradientenfelder sind **wirbelfrei**
(notwendig; Umkehrung nur auf geeigneten Gebieten, später via Stokes).
:::

Divergenz und Rotation gehorchen einer Reihe eleganter **Rechenregeln und Identitäten** — etwa
$\operatorname{div}\operatorname{rot}F=0$ und $\operatorname{rot}\operatorname{rot}F=\nabla\operatorname{div}F-\Delta F$.
Sie sind das Handwerkszeug für alle folgenden Rechnungen und das Thema des nächsten Artikels.

:::quiz
F: Warum ist die Divergenz ein Skalar, die (3D-)Rotation aber ein Vektor — was misst jede der beiden?
A: Die Divergenz $\nabla\cdot E$ bündelt die „auseinanderstrebende" Information zu **einer** Zahl pro Punkt: die **Quelldichte** (wie viel netto herausströmt). Die Rotation $\nabla\times E$ braucht eine **Richtung** (Drehachse) und eine Stärke — das ist ein Vektor, der die **Wirbeldichte** beschreibt.
F: Was bedeuten $\operatorname{div}E>0$, $<0$ und $=0$ anschaulich?
A: $>0$: eine **Quelle** — aus einer kleinen Umgebung strömt netto mehr heraus als hinein. $<0$: eine **Senke** — es verschwindet Feld. $=0$: **quellenfrei** — es fließt genauso viel rein wie raus. Präzise wird das durch den Gaußschen Satz (Fluss durch die Hülle).
F: Warum führt $\operatorname{div}(\operatorname{grad}\phi)$ auf den Laplace-Operator, und was misst $\Delta\phi$ anschaulich?
A: Setzt man $E=\nabla\phi$ in die Divergenz ein, entstehen die diagonalen zweiten Ableitungen $\sum_j\partial^2\phi/\partial x_j^2=\Delta\phi$. $\Delta\phi$ misst, wie stark der Wert an einem Punkt vom **Mittel seiner Umgebung** abweicht (eine „Krümmung" des Feldes).
F: Was bedeutet es physikalisch, dass eine Funktion harmonisch ist ($\Delta\phi=0$)?
A: Sie beschreibt einen **Gleichgewichtszustand**: kein Punkt weicht vom Umgebungsmittel ab (Mittelwerteigenschaft). Beispiele sind das Potential im ladungsfreien Raum oder eine stationäre Temperaturverteilung — nichts „quillt" oder „staut" sich.
F: Warum ist das Coulomb-Potential $\frac{Q}{4\pi r}$ außerhalb der Ladung harmonisch, nicht aber im Ursprung?
A: Für $r>0$ gibt die radiale Divergenzformel exakt $\Delta u=0$ — im leeren Raum gibt es keine Quelle. Im Ursprung sitzt die Punktladung selbst (Singularität); dort ist $u$ nicht definiert und $\Delta u$ wird zur Quelle (Poisson-Gleichung, später).
F: Warum gibt es die dreikomponentige Rotation nur im $\mathbb{R}^3$, die Divergenz aber in jeder Dimension?
A: Die Rotation ist formal das Kreuzprodukt $\nabla\times E$, und das Kreuzprodukt (Vektor senkrecht auf zwei Vektoren) ist eine Besonderheit von genau drei Dimensionen. Die Divergenz ist nur eine Summe von Ableitungen und funktioniert in jedem $\mathbb{R}^n$.
F: Warum ist die Rotation in 2D eine skalare Größe, und wie hängen Divergenz und Rotation dort über eine $90°$-Drehung zusammen?
A: Ein ebenes Feld hat als 3D-Rotation nur die dritte Komponente $\partial_{x_1}E_2-\partial_{x_2}E_1$ — also eine Zahl. Mit dem um $90°$ gedrehten Feld $F^\perp=(-F_2,F_1)$ gilt $\operatorname{div}F=\operatorname{rot}F^\perp$: Quelle und Wirbel sind „dasselbe, um $90°$ gedreht".
F: Warum gilt $\operatorname{rot}(\operatorname{grad}\phi)=0$, und welche Eigenschaft steckt dahinter?
A: Jede Komponente von $\operatorname{rot}\nabla\phi$ ist eine Differenz gemischter zweiter Ableitungen, z. B. $\partial_{x_2}\partial_{x_3}\phi-\partial_{x_3}\partial_{x_2}\phi$. Nach dem Satz von Schwarz vertauschen diese, also ist alles null: Gradientenfelder sind **wirbelfrei**.
F: Warum ist „$\operatorname{rot}F=0$" nur notwendig, nicht hinreichend dafür, dass $F$ ein Gradientenfeld ist?
A: Notwendig folgt es aus $\operatorname{rot}\operatorname{grad}=0$. Ob die Umkehrung gilt, hängt von der **Gestalt des Gebiets** ab: Auf einem Gebiet mit „Loch" kann ein Feld überall rotationsfrei sein und trotzdem kein globales Potential haben. Erst einfach zusammenhängende Gebiete sichern die Umkehrung (Poincaré/Stokes, später).
F: Was besagt die radiale Divergenzformel $\operatorname{div}(f(r)\hat e_r)=f'(r)+(n-1)\frac{f(r)}{r}$ — insbesondere der Term $(n-1)\frac{f(r)}{r}$?
A: $f'(r)$ ist die Änderung der Feldstärke entlang des Radius; $(n-1)\frac{f(r)}{r}$ ist ein rein **geometrischer** Beitrag, weil radiale Pfeile beim Auseinanderlaufen eine mit $r^{n-1}$ wachsende Fläche „aufspannen". Er erklärt, warum gerade ein $\sim r^{-(n-1)}$-Feld quellenfrei ist (die beiden Terme heben sich auf).
:::
