---
title: Rechenregeln und Identitäten für Divergenz und Rotation
pfad: Elektrotechnik / 3. Semester / Höhere Mathematik 3 / Differentialrechnung für Vektorfelder
order: 3010400
summary: Von Grund auf – das Handwerkszeug für Rechnungen mit $\nabla$. Produktregeln für $\operatorname{div}(\phi E)$ und $\operatorname{rot}(\phi E)$, die Kreuzprodukt-Regeln und vor allem die zwei zentralen Identitäten $\operatorname{div}\operatorname{rot}E=0$ (Wirbelfelder sind quellenfrei) und $\operatorname{rot}\operatorname{rot}E=\nabla\operatorname{div}E-\Delta E$. Dazu Vektorpotentiale, Eichfreiheit und die Coulomb-Eichung.
tags: Produktregel, Graßmann-Identität, div rot, rot rot, Vektorpotential, Wirbelfeld, Eichfreiheit, Coulomb-Eichung
---

## Anschaulich

Divergenz und Rotation sind definiert — jetzt brauchen wir die **Rechenregeln**, um mit ihnen so flüssig
umzugehen wie mit Produkt- und Kettenregel in HM1.

Der Schlüssel ist eine Doppelnatur des Nabla-Operators $\nabla$: Er verhält sich **teils wie ein Vektor** (man
bildet Skalar- und Kreuzprodukte) und ist **zugleich ein Ableitungsoperator** (es gelten Produktregeln). Diese
Doppelnatur erzeugt ein paar elegante Identitäten — und ein paar Fallstricke.

Zwei Identitäten ragen heraus und sind zueinander **spiegelbildlich**: Ein reines Gradientenfeld hat keine Wirbel
($\operatorname{rot}\operatorname{grad}=0$), und ein reines Wirbelfeld hat keine Quellen
($\operatorname{div}\operatorname{rot}=0$).

Die zweite große Identität, $\operatorname{rot}\operatorname{rot}=\nabla\operatorname{div}-\Delta$, steckt direkt
hinter der Wellengleichung der Elektrodynamik.

:::grafik
Szene: hoema3/differentialrechnung-vektorfelder/04-nullregeln-spiegel · Vorlage: zwei-nullregeln-2d
Zwei „Nullregeln" als spiegelnde Merkbilder. Oben: ein Gradientenfeld (Pfeile senkrecht auf Höhenlinien) mit
Stempel „$\operatorname{rot}\operatorname{grad}=0$ — wirbelfrei". Unten: ein reines Wirbelfeld (kreisende Pfeile)
mit Stempel „$\operatorname{div}\operatorname{rot}=0$ — quellenfrei". Rechts die Zerlegung
$\operatorname{rot}\operatorname{rot}E=\nabla\operatorname{div}E-\Delta E$ mit Hinweis „→ Wellengleichung".
(Rot = Gradientenfeld, orange = Wirbelfeld, grau = Höhenlinien.)
:::

## Produktregeln mit einem Skalarfeld

Multipliziert man ein Vektorfeld mit einer skalaren Funktion $\phi$, gelten Produktregeln ganz analog zur
eindimensionalen $(\phi\,E)'=\phi'E+\phi\,E'$ — nur dass „ableiten" hier $\operatorname{div}$ bzw.
$\operatorname{rot}$ heißt und der „Vorfaktor" $\phi'$ zum Gradienten $\nabla\phi$ wird:

$$\operatorname{div}(\phi\,E) = \nabla\phi\cdot E + \phi\,\operatorname{div}E,$$

$$\operatorname{rot}(\phi\,E) = \nabla\phi\times E + \phi\,\operatorname{rot}E.$$

In beiden erkennt man dieselbe Struktur: Einmal wirkt die Ableitung auf $\phi$ (ergibt $\nabla\phi$ „mal" $E$),
einmal auf $E$ (ergibt $\phi$ mal die Ableitung von $E$).

Die erste Regel gilt in **jeder** Dimension (wir haben sie schon für die Divergenz radialer Felder benutzt), die
zweite im $\mathbb{R}^3$.

## Werkzeug: Spat- und Graßmann-Identität

Für die Regeln mit Kreuzprodukten braucht man zwei Identitäten der Vektorrechnung im $\mathbb{R}^3$. Das
__Spatprodukt__ ist die Determinante aus drei Vektoren und misst das Volumen des aufgespannten Parallelepipeds:

$$a\cdot(b\times c) = \det(a\,|\,b\,|\,c) \qquad\text{(zyklisch vertauschbar).}$$

Das zweite Werkzeug löst ein doppeltes Kreuzprodukt auf:

:::formel Lemma
$$a\times(b\times c) = (a\cdot c)\,b - (a\cdot b)\,c \qquad (\text{Graßmann-Identität, „BAC}-\text{CAB"}).$$
:::

Hier sind $a,b,c\in\mathbb{R}^3$ Vektoren; das Ergebnis ist wieder ein Vektor in der von $b,c$ aufgespannten
Ebene. In Indexschreibweise steckt dahinter die Levi-Civita-Relation
$\sum_{k}\varepsilon_{ijk}\varepsilon_{klm}=\delta_{il}\delta_{jm}-\delta_{im}\delta_{jl}$.

Diese Werkzeuge übertragen sich auf $\nabla$ — solange man seine Doppelnatur (Vektor **und** Ableitung) beachtet.

## Produktregeln für Kreuzprodukte von Vektorfeldern

Für zwei differenzierbare Vektorfelder $E,B$ im $\mathbb{R}^3$ gelten:

$$\operatorname{div}(E\times B) = B\cdot\operatorname{rot}E - E\cdot\operatorname{rot}B,$$

$$\operatorname{rot}(E\times B) = E\,\operatorname{div}B - B\,\operatorname{div}E + (B\cdot\nabla)E - (E\cdot\nabla)B.$$

Dabei ist $(E\cdot\nabla)B=\sum_{j=1}^{3}E_j\,\dfrac{\partial B}{\partial x_j}$ die komponentenweise
Richtungsableitung von $B$ in Richtung $E$.

**Stolperstein:** $\nabla$ ist kein gewöhnlicher Vektor. Beim „Ausmultiplizieren" muss man stets mitdenken,
**worauf** die Ableitung gerade wirkt — sonst verliert man Terme. Die obigen Formeln sind genau das Ergebnis
dieser achtsamen Buchführung.

## Die zwei zentralen Identitäten

Die wichtigsten Regeln des Kapitels entstehen, wenn man **zwei** Operatoren hintereinander anwendet.

**1. Die Divergenz einer Rotation ist null.** Für jedes zweimal stetig differenzierbare Feld $E$ gilt:

:::formel Satz
$$\operatorname{div}\operatorname{rot}E = 0.$$
:::

:::herleitung
In Levi-Civita-Schreibweise ist

$$\operatorname{div}\operatorname{rot}E = \sum_{i,j,k}\varepsilon_{ijk}\,\frac{\partial^2 E_k}{\partial x_i\,\partial x_j}.$$

Die zweite Ableitung $\partial^2/\partial x_i\partial x_j$ ist **symmetrisch** in $i,j$ (Satz von Schwarz), das
Levi-Civita-Symbol $\varepsilon_{ijk}$ dagegen **antisymmetrisch** (die Vertauschung $i\leftrightarrow j$ kehrt
das Vorzeichen um). Summiert man ein symmetrisches mal ein antisymmetrisches Objekt, hebt sich alles paarweise
weg — die Summe ist null.
:::

Anschaulich: Ein reines **Wirbelfeld** hat **keine Quellen** — das genaue Gegenstück zu
$\operatorname{rot}\operatorname{grad}\phi=0$ (ein reines Gradientenfeld hat keine Wirbel).

**2. Die Rotation der Rotation.** Für jedes zweimal stetig differenzierbare Feld $E$ im $\mathbb{R}^3$ gilt:

:::formel Satz
$$\operatorname{rot}\operatorname{rot}E = \nabla(\operatorname{div}E) - \Delta E.$$
:::

:::herleitung
Formal ist $\operatorname{rot}\operatorname{rot}E=\nabla\times(\nabla\times E)$. Wendet man die Graßmann-Identität
$a\times(b\times c)=(a\cdot c)b-(a\cdot b)c$ mit $a=b=\nabla$ und $c=E$ an, entsteht

$$\nabla\times(\nabla\times E) = \nabla(\nabla\cdot E) - (\nabla\cdot\nabla)E = \nabla(\operatorname{div}E) - \Delta E.$$

**Wichtig:** $\nabla$ wirkt nach rechts, das Feld $E$ muss **an letzter Stelle** stehen — sonst ordnet die rein
algebraische Regel die Ableitungen falsch an. Mit dieser Buchführung ist $(\nabla\cdot\nabla)E=\Delta E$ (der
komponentenweise Laplace).
:::

Diese Identität ist das Herzstück der **Wellengleichung**: Aus den Maxwell-Gleichungen wird im quellenfreien Fall
($\operatorname{div}E=0$) daraus $\operatorname{rot}\operatorname{rot}E=-\Delta E$.

## Vektorpotentiale und Eichfreiheit

Die Identität $\operatorname{div}\operatorname{rot}=0$ führt — spiegelbildlich zum Skalarpotential — auf einen
neuen Begriff. Ein Vektorfeld $B$ heißt __Wirbelfeld__, wenn es die Rotation eines anderen Feldes ist:

:::formel Definition
$$B = \operatorname{rot}A.$$
:::

Dann heißt $A$ ein __Vektorpotential__ von $B$. Nach $\operatorname{div}\operatorname{rot}=0$ ist jedes solche $B$
zwangsläufig __divergenzfrei__ ($\operatorname{div}B=0$) — eine **notwendige** Bedingung. Wie bei den
Gradientenfeldern gilt die Umkehrung (ist jedes divergenzfreie Feld ein Wirbelfeld?) im Allgemeinen nicht; sie
hängt vom Gebiet ab.

**Eichfreiheit.** Vektorpotentiale sind nicht eindeutig: Zu $A$ darf man ein beliebiges **Gradientenfeld**
$\nabla\psi$ addieren, ohne $B$ zu ändern. Denn

$$\operatorname{rot}(A+\nabla\psi) = \operatorname{rot}A + \underbrace{\operatorname{rot}\nabla\psi}_{=0} = \operatorname{rot}A = B.$$

Diese Freiheit nutzt man, um ein bequemes $A$ zu wählen — etwa die __Coulomb-Eichung__ $\operatorname{div}A=0$.

:::herleitung
Ist $\operatorname{div}A\neq0$, so löst man die Poisson-Gleichung

$$\Delta\psi = \operatorname{div}A$$

und setzt $A'=A-\nabla\psi$. Dann ist $\operatorname{div}A'=\operatorname{div}A-\Delta\psi=0$, und wegen
$\operatorname{rot}\nabla\psi=0$ bleibt $\operatorname{rot}A'=B$ unverändert. In dieser Eichung vereinfacht sich die
zweite Identität zu $\operatorname{rot}B=\operatorname{rot}\operatorname{rot}A'=-\Delta A'$.
:::

:::grafik
Szene: hoema3/differentialrechnung-vektorfelder/04-eichfreiheit · Vorlage: vektorpotential-eichung-3d
Ein Wirbelfeld $B$ mit mehreren möglichen Vektorpotentialen $A$, $A'=A-\nabla\psi$, die alle dieselbe Rotation
geben (Eichfreiheit: „$+\nabla\psi$ ändert $B$ nicht"). Hervorgehoben die Coulomb-Eichung $\operatorname{div}A=0$
als die „aufgeräumte" Wahl; parallel das Spiegelbild Skalarpotential $\phi$ bis auf Konstante. (Rot = $B$, orange
= verschiedene $A$, grau = $\nabla\psi$.)
:::

## Bedeutung und Ausblick

Mit den Produktregeln und den beiden Null-Identitäten ist die **Differentialrechnung** für Felder vollständig:
Gradient, Divergenz, Rotation, Laplace und ihre Rechenregeln. Das ist das Handwerkszeug, mit dem man in der
Elektrodynamik die Feldgleichungen umformt.

Als Nächstes kommt die **Integralseite**: zunächst, wie man Integrale differenziert, die von einem Parameter
abhängen, und wie man über mehrdimensionale Bereiche integriert — das Kapitel __Integralrechnung im
$\mathbb{R}^n$__.

:::kern
- __Produktregeln:__ $\operatorname{div}(\phi E)=\nabla\phi\cdot E+\phi\operatorname{div}E$ (jede Dim.), $\operatorname{rot}(\phi E)=\nabla\phi\times E+\phi\operatorname{rot}E$ (in $\mathbb{R}^3$).
- Kreuzprodukte: $\operatorname{div}(E\times B)=B\cdot\operatorname{rot}E-E\cdot\operatorname{rot}B$ und $\operatorname{rot}(E\times B)=E\operatorname{div}B-B\operatorname{div}E+(B\cdot\nabla)E-(E\cdot\nabla)B$ (Werkzeug: __Graßmann__ $a\times(b\times c)=(a\cdot c)b-(a\cdot b)c$).
- __Zentrale Identitäten:__ $\operatorname{div}\operatorname{rot}E=0$ (Wirbelfeld quellenfrei; Beweis: symmetrisch × antisymmetrisch $=0$) und $\operatorname{rot}\operatorname{rot}E=\nabla\operatorname{div}E-\Delta E$ (→ Wellengleichung).
- Ein __Wirbelfeld__ $B=\operatorname{rot}A$ ($A$ = __Vektorpotential__) ist stets divergenzfrei (notwendig, nicht hinreichend).
- __Eichfreiheit:__ $A+\nabla\psi$ liefert dasselbe $B$; die __Coulomb-Eichung__ $\operatorname{div}A=0$ erreicht man über $\Delta\psi=\operatorname{div}A$, dann $\operatorname{rot}B=-\Delta A$.
:::

:::quiz
F: Warum steht in der Produktregel $\operatorname{div}(\phi E)=\nabla\phi\cdot E+\phi\operatorname{div}E$ der Gradient $\nabla\phi$ und nicht einfach $\phi'$?
A: Es ist dieselbe Struktur wie $(\phi E)'=\phi'E+\phi E'$ in 1D, nur dass „ableiten" hier $\operatorname{div}$ heißt. Wirkt die Ableitung auf das **Skalarfeld** $\phi$, entsteht sein Gradient $\nabla\phi$, der dann (als Vektor) mit $E$ skalar multipliziert wird.
F: Was ist mit der „Doppelnatur" von $\nabla$ gemeint, und welcher Fehler droht beim Rechnen?
A: $\nabla$ verhält sich teils wie ein **Vektor** (Skalar-/Kreuzprodukte) und ist zugleich ein **Ableitungsoperator** (Produktregeln). Beim Ausmultiplizieren muss man stets mitführen, **worauf** die Ableitung gerade wirkt — sonst gehen Terme verloren oder man wendet vektoralgebraische Regeln falsch an.
F: Warum ist $\operatorname{div}\operatorname{rot}E=0$ — welche Symmetrie steckt dahinter?
A: In Levi-Civita-Form ist es $\sum_{i,j,k}\varepsilon_{ijk}\,\partial^2 E_k/(\partial x_i\partial x_j)$. Die zweite Ableitung ist **symmetrisch** in $i,j$ (Schwarz), $\varepsilon_{ijk}$ **antisymmetrisch** — ihr Produkt summiert sich paarweise zu null. Anschaulich: ein reines Wirbelfeld hat keine Quellen.
F: Inwiefern ist $\operatorname{div}\operatorname{rot}=0$ das Spiegelbild von $\operatorname{rot}\operatorname{grad}=0$?
A: Beide sagen „zwei Operatoren hintereinander ergeben null". $\operatorname{rot}\operatorname{grad}\phi=0$: ein Gradientenfeld ist **wirbelfrei**. $\operatorname{div}\operatorname{rot}E=0$: ein Wirbelfeld ist **quellenfrei**. Gradient und Rotation liefern so die jeweils „komplementären" Felder.
F: Was besagt $\operatorname{rot}\operatorname{rot}E=\nabla(\operatorname{div}E)-\Delta E$, und wofür ist sie zentral?
A: Sie zerlegt die doppelte Rotation in einen Quellenanteil ($\nabla\operatorname{div}E$) und einen „Krümmungsanteil" ($\Delta E$). Sie ist das Herzstück der **Wellengleichungs-Herleitung** aus den Maxwell-Gleichungen: im quellenfreien Fall ($\operatorname{div}E=0$) wird daraus $\operatorname{rot}\operatorname{rot}E=-\Delta E$.
F: Was ist ein Vektorpotential, und warum ist $B=\operatorname{rot}A$ zwangsläufig divergenzfrei?
A: $A$ heißt Vektorpotential von $B$, wenn $B=\operatorname{rot}A$. Wegen $\operatorname{div}\operatorname{rot}=0$ folgt sofort $\operatorname{div}B=0$ — Divergenzfreiheit ist also eine **notwendige** Bedingung dafür, dass $B$ überhaupt ein Wirbelfeld sein kann.
F: Warum ist $\operatorname{div}B=0$ notwendig, aber nicht hinreichend für die Existenz eines Vektorpotentials?
A: Notwendig folgt es aus $\operatorname{div}\operatorname{rot}=0$. Die Umkehrung „divergenzfrei $\Rightarrow$ Wirbelfeld" hängt — wie bei Gradientenfeldern — von der **Topologie des Gebiets** ab und gilt nicht allgemein (später über die Integralsätze geklärt).
F: Was bedeutet Eichfreiheit beim Vektorpotential, und warum ändert das Addieren von $\nabla\psi$ das Feld $B$ nicht?
A: Das Vektorpotential ist nicht eindeutig: $A$ und $A+\nabla\psi$ liefern dasselbe $B$, denn $\operatorname{rot}(A+\nabla\psi)=\operatorname{rot}A+\operatorname{rot}\nabla\psi=\operatorname{rot}A$ (da $\operatorname{rot}\operatorname{grad}=0$). Diese Freiheit nutzt man, um ein bequemes $A$ zu wählen.
F: Wozu dient die Coulomb-Eichung $\operatorname{div}A=0$, und wie erreicht man sie?
A: Sie „räumt auf" und vereinfacht $\operatorname{rot}B=\operatorname{rot}\operatorname{rot}A=-\Delta A$. Ist $\operatorname{div}A\neq0$, löst man die Poisson-Gleichung $\Delta\psi=\operatorname{div}A$ und setzt $A'=A-\nabla\psi$; dann ist $\operatorname{div}A'=0$, und $B$ bleibt unverändert.
F: Warum muss man die Graßmann-Identität bei $\nabla\times(\nabla\times E)$ mit Vorsicht anwenden?
A: $\nabla$ ist ein Operator, der nach rechts wirkt — das abzuleitende Feld $E$ muss **an letzter Stelle** stehen. Die rein vektoralgebraische Regel würde Terme falsch anordnen; richtig angewandt ergibt sie $\nabla(\operatorname{div}E)-\Delta E$, nicht etwa $E$-Faktoren vor den Ableitungen.
:::
