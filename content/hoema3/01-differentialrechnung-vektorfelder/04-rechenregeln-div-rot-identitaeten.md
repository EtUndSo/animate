---
title: Rechenregeln und Identitäten für Divergenz und Rotation
pfad: Elektrotechnik / 3. Semester / Höhere Mathematik 3 / Differentialrechnung für Vektorfelder
order: 3010400
summary: Von Grund auf – das Handwerkszeug für Rechnungen mit $\nabla$. Produktregeln für $\operatorname{div}(\phi E)$ und $\operatorname{rot}(\phi E)$, die Kreuzprodukt-Regeln, und vor allem die beiden zentralen Identitäten $\operatorname{div}\operatorname{rot}E=0$ (Wirbelfelder sind quellenfrei) und $\operatorname{rot}\operatorname{rot}E=\nabla\operatorname{div}E-\Delta E$. Dazu Vektorpotentiale, ihre Eichfreiheit und die Coulomb-Eichung.
tags: Produktregel, Graßmann-Identität, div rot, rot rot, Vektorpotential, Wirbelfeld, Eichfreiheit, Coulomb-Eichung
---

:::grafik
Einstiegs-Animation: Zwei „Nullregeln" als Merkbilder, die einander spiegeln. Oben: ein Gradientenfeld (Pfeile
senkrecht auf Höhenlinien) mit großem Stempel „$\operatorname{rot}\operatorname{grad}=0$ — wirbelfrei". Unten: ein
reines Wirbelfeld (kreisende Pfeile) mit Stempel „$\operatorname{div}\operatorname{rot}=0$ — quellenfrei". In der
Mitte ein Vektorfeld, das per Identität in einen „quellenartigen" und einen „wirbelartigen" Anteil zerlegt wird
($\operatorname{rot}\operatorname{rot}E=\nabla\operatorname{div}E-\Delta E$). Kernbotschaft: Zwei Hintereinander-
Anwendungen der Operatoren geben null — das ist der Schlüssel zu Potentialen und zur Wellengleichung.
:::

:::konzept
Divergenz und Rotation sind definiert — jetzt braucht man die **Rechenregeln**, um mit ihnen flüssig umzugehen,
ganz wie Produkt- und Kettenregel in HM1. Der Nabla-Operator $\nabla$ verhält sich dabei **teils** wie ein
Vektor (Kreuz- und Skalarprodukte), ist aber **auch** ein Ableitungsoperator (Produktregeln) — diese
Doppelnatur ist der Grund für einige hübsche Identitäten und einige Fallstricke. Zwei Identitäten ragen heraus:
$\operatorname{div}\operatorname{rot}=0$ und $\operatorname{rot}\operatorname{rot}=\nabla\operatorname{div}-\Delta$.
Die erste ist das Gegenstück zu $\operatorname{rot}\operatorname{grad}=0$ und führt zum Begriff des
__Vektorpotentials__; die zweite steht hinter der Wellengleichung der Elektrodynamik.
:::

**Worum es geht:** Wir sammeln die __Produktregeln__ für $\operatorname{div}$ und $\operatorname{rot}$, beweisen
die zentralen Identitäten $\operatorname{div}\operatorname{rot}E=0$ und $\operatorname{rot}\operatorname{rot}E=
\nabla\operatorname{div}E-\Delta E$ und führen __Vektorpotentiale__ samt __Eichfreiheit__ ein.

## Produktregeln mit einem Skalarfeld

Multipliziert man ein Vektorfeld mit einer skalaren Funktion $\phi$, gelten Produktregeln ganz analog zur
eindimensionalen $(\phi\,E)' = \phi' E + \phi\,E'$ — nur dass „ableiten" hier $\operatorname{div}$ bzw.
$\operatorname{rot}$ heißt und der „Vorfaktor" $\phi'$ zum Gradienten $\nabla\phi$ wird:

$$\operatorname{div}(\phi\,E) = \nabla\phi\cdot E + \phi\,\operatorname{div}E, \qquad \operatorname{rot}(\phi\,E) = \nabla\phi\times E + \phi\,\operatorname{rot}E.$$

Die erste Regel gilt in **jeder** Dimension (sie haben wir schon bei der Divergenz radialer Felder benutzt), die
zweite im $\mathbb{R}^3$ (und sinngemäß in 2D, wo $\nabla\phi\times E$ zum Skalar
$\partial_{x_1}\phi\,E_2-\partial_{x_2}\phi\,E_1$ wird). In beiden erkennt man dieselbe Struktur: einmal wirkt die
Ableitung auf $\phi$ (ergibt $\nabla\phi$ „mal" $E$), einmal auf $E$ (ergibt $\phi$ mal die Ableitung von $E$).

## Zwei Vektoridentitäten als Werkzeug

Für die Regeln mit Kreuzprodukten braucht man zwei Identitäten aus der Vektorrechnung im $\mathbb{R}^3$. Das
__Spatprodukt__ ist die Determinante aus drei Vektoren,

$$a\cdot(b\times c) = \det(a\,|\,b\,|\,c) \qquad\text{(zyklisch vertauschbar)},$$

und die __Graßmann-Identität__ („BAC−CAB-Regel") löst ein doppeltes Kreuzprodukt auf:

$$a\times(b\times c) = (a\cdot c)\,b - (a\cdot b)\,c.$$

In Indexschreibweise steckt dahinter die Levi-Civita-Relation $\sum_{k}\varepsilon_{ijk}\varepsilon_{klm} =
\delta_{il}\delta_{jm}-\delta_{im}\delta_{jl}$. Diese Werkzeuge übertragen sich auf $\nabla$, solange man seine
Doppelnatur (Vektor **und** Ableitung) beachtet.

## Produktregeln für Kreuzprodukte von Vektorfeldern

Für zwei differenzierbare Vektorfelder $E, B$ im $\mathbb{R}^3$ gelten:

$$\operatorname{div}(E\times B) = B\cdot\operatorname{rot}E - E\cdot\operatorname{rot}B,$$

$$\operatorname{rot}(E\times B) = E\,\operatorname{div}B - B\,\operatorname{div}E + (B\cdot\nabla)E - (E\cdot\nabla)B.$$

Dabei ist $(E\cdot\nabla)B = \sum_{j=1}^{3} E_j\,\dfrac{\partial B}{\partial x_j}$ die komponentenweise
Richtungsableitung von $B$ in Richtung $E$. Beide Formeln folgen aus der Levi-Civita-Darstellung von Kreuzprodukt
und Rotation zusammen mit der Produktregel (für die zweite braucht man die Graßmann-Identität).

**Stolperstein:** $\nabla$ ist kein gewöhnlicher Vektor. Beim „Ausmultiplizieren" muss man stets mitdenken,
**worauf** die Ableitung gerade wirkt — sonst verliert man Terme. Die obigen Formeln sind genau das korrekte
Ergebnis dieser achtsamen Buchführung.

## Die zwei zentralen Identitäten

Jetzt die wichtigsten Regeln des ganzen Kapitels — sie entstehen, wenn man **zwei** Operatoren hintereinander
anwendet.

**1. Die Divergenz einer Rotation ist null.** Für jedes zweimal stetig differenzierbare Feld $E$ gilt

$$\operatorname{div}\operatorname{rot}E = 0.$$

*Beweis.* In Levi-Civita-Schreibweise ist $\operatorname{div}\operatorname{rot}E = \sum_{i,j,k}\varepsilon_{ijk}
\dfrac{\partial^2 E_k}{\partial x_i\,\partial x_j}$. Die zweite Ableitung $\partial^2/\partial x_i\partial x_j$ ist
**symmetrisch** in $i,j$ (Schwarz), das Levi-Civita-Symbol $\varepsilon_{ijk}$ dagegen **antisymmetrisch** ($i
\leftrightarrow j$ kehrt das Vorzeichen um). Summiert man ein symmetrisches mal ein antisymmetrisches Objekt, hebt
sich alles paarweise weg — die Summe ist null. $\square$

Anschaulich: Ein reines **Wirbelfeld** (eine Rotation) hat **keine Quellen**. Das ist das genaue Gegenstück zur
Identität $\operatorname{rot}\operatorname{grad}\phi=0$ aus dem vorigen Artikel (ein reines **Gradientenfeld** hat
keine Wirbel).

**2. Die Rotation der Rotation.** Für jedes zweimal stetig differenzierbare Feld $E$ im $\mathbb{R}^3$ gilt

$$\operatorname{rot}\operatorname{rot}E = \nabla(\operatorname{div}E) - \Delta E.$$

Sie folgt aus der Graßmann-Identität, formal angewandt auf $\nabla\times(\nabla\times E)$ mit $\nabla\cdot\nabla
= \Delta$ — wobei das Feld $E$ **immer an letzter Stelle** stehen muss (Ableitungen wirken nach rechts). Diese
Identität ist das Herzstück der Herleitung der **Wellengleichung** in der Elektrodynamik: Aus den
Maxwell-Gleichungen wird mit ihr $\operatorname{rot}\operatorname{rot}E = -\Delta E$ (im quellenfreien Fall
$\operatorname{div}E=0$), und daraus die Wellengleichung.

:::grafik
Links die beiden „Nullregeln" nebeneinander als Spiegelbild: $\operatorname{rot}\operatorname{grad}\phi=0$
(Gradientenfeld, wirbelfrei) und $\operatorname{div}\operatorname{rot}E=0$ (Wirbelfeld, quellenfrei), jeweils mit
dem Argument „symmetrisch × antisymmetrisch = 0". Rechts die Zerlegung $\operatorname{rot}\operatorname{rot}E=
\nabla\operatorname{div}E-\Delta E$ mit dem Hinweis „→ Wellengleichung (Maxwell)".
:::

## Vektorpotentiale und Eichfreiheit

Die Identität $\operatorname{div}\operatorname{rot}=0$ führt — spiegelbildlich zum Skalarpotential — auf einen
neuen Begriff. Ein Vektorfeld $B$ heißt __Rotations-__ oder __Wirbelfeld__, wenn es die Rotation eines anderen
Feldes ist:

$$B = \operatorname{rot}A,$$

und $A$ heißt dann ein __Vektorpotential__ von $B$. Nach $\operatorname{div}\operatorname{rot}=0$ ist jedes solche
$B$ zwangsläufig __divergenzfrei__ ($\operatorname{div}B=0$) — eine **notwendige** Bedingung. Wie bei den
Gradientenfeldern ist die **Umkehrung** (ist jedes divergenzfreie Feld ein Wirbelfeld?) im Allgemeinen nicht
richtig und hängt vom Gebiet ab.

**Eichfreiheit.** Weder Skalar- noch Vektorpotentiale sind eindeutig: Zu einem Skalarpotential darf man eine
beliebige Konstante addieren, zu einem Vektorpotential sogar ein beliebiges **Gradientenfeld** — denn
$\operatorname{rot}(A + \nabla\psi) = \operatorname{rot}A + \underbrace{\operatorname{rot}\nabla\psi}_{=0} =
\operatorname{rot}A = B$. Diese Freiheit nutzt man, um ein Vektorpotential mit bequemen Eigenschaften zu wählen,
etwa die __Coulomb-Eichung__ $\operatorname{div}A = 0$: Ist $\operatorname{div}A \neq 0$, so löst man die
Poisson-Gleichung $\Delta\psi = \operatorname{div}A$ und setzt $A' = A - \nabla\psi$; dann ist
$\operatorname{div}A' = 0$. In dieser Eichung vereinfacht sich die zweite Identität zu
$\operatorname{rot}B = \operatorname{rot}\operatorname{rot}A' = -\Delta A'$.

:::grafik
Ein Wirbelfeld $B$ mit mehreren möglichen Vektorpotentialen $A$, $A'=A-\nabla\psi$, die alle dieselbe Rotation
geben (Eichfreiheit, „$+\nabla\psi$ ändert $B$ nicht"). Hervorgehoben die Coulomb-Eichung $\operatorname{div}A=0$
als die „aufgeräumte" Wahl. Parallel das Spiegelbild: Skalarpotential $\phi$ bis auf Konstante.
:::

:::kern
__Produktregeln__: $\operatorname{div}(\phi E)=\nabla\phi\cdot E+\phi\operatorname{div}E$ (jede Dim.),
$\operatorname{rot}(\phi E)=\nabla\phi\times E+\phi\operatorname{rot}E$; für Kreuzprodukte
$\operatorname{div}(E\times B)=B\cdot\operatorname{rot}E-E\cdot\operatorname{rot}B$ und
$\operatorname{rot}(E\times B)=E\operatorname{div}B-B\operatorname{div}E+(B\cdot\nabla)E-(E\cdot\nabla)B$ (Werkzeug:
__Graßmann-Identität__ $a\times(b\times c)=(a\cdot c)b-(a\cdot b)c$). Zwei zentrale Identitäten:
$\operatorname{div}\operatorname{rot}E=0$ (Wirbelfeld quellenfrei; Beweis: symmetrisch × antisymmetrisch $=0$) und
$\operatorname{rot}\operatorname{rot}E=\nabla\operatorname{div}E-\Delta E$ (→ Wellengleichung). Ein __Wirbelfeld__
$B=\operatorname{rot}A$ ($A$ __Vektorpotential__) ist stets divergenzfrei (notwendig). __Eichfreiheit__:
$A+\nabla\psi$ liefert dasselbe $B$; __Coulomb-Eichung__ $\operatorname{div}A=0$ erreicht man über
$\Delta\psi=\operatorname{div}A$, dann $\operatorname{rot}B=-\Delta A$.
:::

Damit ist die **Differentialrechnung** für Felder vollständig: Gradient, Divergenz, Rotation, Laplace und ihre
Identitäten. Als Nächstes kommt die **Integralseite** — zunächst, wie man Integrale, die von einem Parameter
abhängen, differenziert und wie man über mehrdimensionale Bereiche integriert. Das ist das Thema des Kapitels
__Integralrechnung im $\mathbb{R}^n$__.
