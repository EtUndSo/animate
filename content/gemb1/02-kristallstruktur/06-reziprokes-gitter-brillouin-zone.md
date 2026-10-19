---
title: Reziprokes Gitter und 1. Brillouin-Zone
pfad: Elektrotechnik / 4. Semester / Grundlagen elektronischer Materialien und Bauelemente / Kristallstruktur
order: 4020600
summary: Warum man neben dem Gitter im Ortsraum ein zweites Gitter im Wellenzahl-Raum braucht – die Bühne, auf der sich später die gesamte Bandstruktur $E(k)$ abspielt. Hergeleitet an der 1D-Kette ($E(k)=2t(1-\cos ka)+V_0$), über die Bedingung $e^{ikR}=1$ zum reziproken Gitter, zur Vorschrift $\vec a_i\cdot\vec b_j=2\pi\delta_{ij}$ und zur 1. Brillouin-Zone als Wigner-Seitz-Zelle des reziproken Gitters.
tags: reziprokes Gitter, Brillouin-Zone, Wellenzahlraum, Bandstruktur, tight-binding, Bloch-Welle, Wigner-Seitz-Zelle
---

:::grafik
Einstiegs-Animation: Oben eine 1D-Atomkette im Ortsraum (Abstand $a$). Darunter wächst die Energie-Kurve
$E(k)$ als welliges Band, das sich mit der Periode $2\pi/a$ immer wiederholt. Rechts wird aus der sturen
Periodizität ein zweites Punktmuster destilliert: Punkte im $k$-Raum im Abstand $2\pi/a$ — das __reziproke
Gitter__ — und um den Ursprung herum ein hervorgehobenes Intervall $[-\pi/a, \pi/a]$, die __1. Brillouin-Zone__.
Kernbotschaft: Ein periodisches Gitter im Ortsraum erzeugt ein periodisches Gitter im Wellenzahl-Raum — und
genau dort lebt die ganze Elektronenphysik des Kristalls.
:::

:::konzept
Bis hierher haben wir den Kristall im **Ortsraum** beschrieben: wo die Atome sitzen. Für die Elektronen darin
brauchen wir aber eine zweite Beschreibung — im **Wellenzahl-Raum** (dem $k$-Raum). Der Grund: Ein Elektron im
Kristall ist eine **Welle**, und Wellen beschreibt man am besten über ihren Wellenvektor $\vec k$. Weil das
Gitter periodisch ist, zwingt es auch jeder Elektronenwelle eine Periodizität auf — und diese Periodizität
lebt in einem eigenen periodischen Punktmuster, dem __reziproken Gitter__. Dessen zentrale Zelle, die __1.
Brillouin-Zone__, ist die Bühne, auf der sich im nächsten Oberthema die gesamte __Bandstruktur__ $E(k)$ abspielt.
Dieser Artikel ist damit das Scharnier zwischen „Kristallgeometrie" und „Elektronenphysik".
:::

**Worum es geht:** Wir rechnen an der einfachsten denkbaren Kette die erste __Bandstruktur__ aus, lesen daran die
Periodizität im $k$-Raum ab, leiten daraus die Definition des __reziproken Gitters__ her (1D und 3D) und
definieren die __1. Brillouin-Zone__.

## Die erste Bandstruktur: eine 1D-Kette

Wir nehmen das einfachste Modell eines Kristalls: eine Kette von Gitterplätzen im Abstand $a$, durchnummeriert
mit dem **Platz-Index** $j$. Die Schrödinger-Gleichung auf so einem diskreten Gitter lautet (die zweite
Ableitung wird zur Differenz zwischen Nachbarplätzen):

$$-t\,(\psi_{j+1} - 2\psi_j + \psi_{j-1}) + V_j\,\psi_j = E\,\psi_j.$$

- __$\psi_j$__: die Wellenfunktion am Platz $j$.
- __$t$__: der __Kopplungs-/Hopping-Parameter__ — wie stark benachbarte Plätze „miteinander reden".
- __$V_j$__: die potentielle Energie am Platz $j$; wir setzen sie konstant $V_j \equiv V_0$.

Jetzt der entscheidende Ansatz: Weil das Gitter periodisch ist, probieren wir eine **ebene Welle** (den
Bloch-Ansatz) — hier ist $i$ die imaginäre Einheit, nicht der Platz-Index:

$$\psi_j = A\,e^{ikx_j} = A\,e^{ikja}, \qquad x_j = j\,a.$$

Der Clou: Ein Nachbarplatz unterscheidet sich dann nur um einen **Phasenfaktor**:

$$\psi_{j+1} = \psi_j\,e^{ika}, \qquad \psi_{j-1} = \psi_j\,e^{-ika}.$$

:::grafik
Die 1D-Kette mit Plätzen $\ldots, j-1, j, j+1, \ldots$ im Abstand $a$; darüber eine durchlaufende Welle
$A\,e^{ikja}$. Pfeile zeigen, dass der Schritt zum Nachbarn die Welle nur um $e^{\pm ika}$ dreht (gleiche
Amplitude, verschobene Phase).
:::

Einsetzen und durch $\psi_j$ teilen lässt die ganze Kette verschwinden — übrig bleibt eine Gleichung nur noch für
die Zahl $k$. Mit der Euler-Identität $\tfrac12(e^{ika} + e^{-ika}) = \cos(ka)$ wird daraus:

$$E(k) = 2t\,\bigl(1 - \cos(ka)\bigr) + V_0.$$

Das ist die **erste Bandstruktur**: eine wellige Kurve, die angibt, welche Energie ein Elektron mit Wellenzahl
$k$ hat. Entscheidend ist ihre **Periodizität**: $\cos(ka)$ wiederholt sich mit der Periode $2\pi/a$, also tut es
$E(k)$ auch. Ein $k$ und ein $k + 2\pi/a$ beschreiben **denselben** physikalischen Zustand.

:::grafik
Die Kurve $E(k) = 2t(1-\cos ka)+V_0$ über $k$: ein welliges Band zwischen $V_0$ (bei $k=0$) und $V_0+4t$ (am
Rand). Eingezeichnet die Periode $2\pi/a$ und zwei Punkte $k$ und $k+2\pi/a$ auf gleicher Höhe („gleicher
Zustand").
:::

## Vom periodischen Band zum reziproken Gitter

Dass $E(k)$ periodisch ist, ist kein Zufall der Kette, sondern Folge der Gitter-Periodizität. Allgemein gilt: Eine
**gitterperiodische** Größe — etwa die Elektronendichte $\sim |\psi|^2$ — darf sich **nicht ändern**, wenn man um
einen Gittervektor $R = j\,a$ verschiebt. Der Bloch-Phasenfaktor $e^{ikR}$ muss dann gleich $1$ sein:

$$e^{ikR} \overset{!}{=} 1 \;\Longrightarrow\; kR = m\cdot 2\pi \;\Longrightarrow\; k_m = m\,\frac{2\pi}{a}, \quad m \in \mathbb{Z}.$$

Diese ausgezeichneten Wellenzahlen $k_m$ bilden selbst wieder ein **periodisches Punktgitter** — aber im
$k$-Raum, mit der Gitterkonstante $2\pi/a$. Das ist das __reziproke Gitter__ in 1D.

- __„reziprok"__: Großer Atomabstand $a$ → **enges** reziprokes Gitter ($2\pi/a$ klein), und umgekehrt. Die
  beiden Gitter verhalten sich invers zueinander.

:::grafik
Oben das reale Gitter (Punkte im Abstand $a$), darunter das reziproke Gitter (Punkte im Abstand $2\pi/a$). Ein
Doppelpfeil „$a \leftrightarrow 2\pi/a$" betont die inverse Beziehung (enger Realraum → weiter $k$-Raum).
:::

## Das reziproke Gitter in 3D

In drei Dimensionen sucht man zu den primitiven Gittervektoren $\vec a_1, \vec a_2, \vec a_3$ die reziproken
Vektoren $\vec b_1, \vec b_2, \vec b_3$. Die Bedingung $e^{i\vec k\cdot\vec R} = 1$ für **alle** Gittervektoren
$\vec R$ führt auf die kompakte __Orthogonalitätsbedingung__:

$$\vec a_i \cdot \vec b_j = 2\pi\,\delta_{ij}.$$

- __$\delta_{ij}$__: das __Kronecker-Delta__ ($1$ falls $i=j$, sonst $0$) — jeder $\vec b_j$ steht senkrecht auf
  den beiden „anderen" $\vec a$-Vektoren.

Diese Bedingung löst man explizit mit Kreuzprodukten:

$$\vec b_1 = 2\pi\,\frac{\vec a_2 \times \vec a_3}{\vec a_1\cdot(\vec a_2 \times \vec a_3)}, \quad \vec b_2 = 2\pi\,\frac{\vec a_3 \times \vec a_1}{\vec a_1\cdot(\vec a_2 \times \vec a_3)}, \quad \vec b_3 = 2\pi\,\frac{\vec a_1 \times \vec a_2}{\vec a_1\cdot(\vec a_2 \times \vec a_3)}.$$

Der Nenner $\vec a_1\cdot(\vec a_2 \times \vec a_3)$ ist das **Spatprodukt** — das Volumen der primitiven Zelle.
Warum funktioniert das? $\vec b_1 \propto \vec a_2 \times \vec a_3$ steht per Konstruktion senkrecht auf $\vec a_2$
und $\vec a_3$ (also $\vec a_2\cdot\vec b_1 = \vec a_3\cdot\vec b_1 = 0$), und der Vorfaktor ist gerade so
gewählt, dass $\vec a_1\cdot\vec b_1 = 2\pi$ herauskommt — genau die Orthogonalitätsbedingung.

:::grafik
Ein primitives Zell-Parallelepiped mit $\vec a_1, \vec a_2, \vec a_3$; daneben der konstruierte $\vec b_1$ als
Normale auf der von $\vec a_2, \vec a_3$ aufgespannten Fläche, mit der Notiz $\vec a_1\cdot\vec b_1 = 2\pi$,
$\vec a_2\cdot\vec b_1 = \vec a_3\cdot\vec b_1 = 0$.
:::

## Die 1. Brillouin-Zone

Das reziproke Gitter ist selbst ein Bravais-Gitter — also kann man darauf **erneut die
Wigner-Seitz-Konstruktion** anwenden (alle Punkte, die dem Ursprung näher sind als jedem anderen reziproken
Gitterpunkt). Diese Zelle hat einen eigenen Namen: die __1. Brillouin-Zone__ ([Oxford Solid State](https://vaia.com/en-us/textbooks/physics/the-oxford-solid-state-basics-1-edition/chapter-13)).

In 1D ist das schlicht das Intervall

$$k \in \left[-\frac{\pi}{a},\; +\frac{\pi}{a}\right].$$

Das ist genau **eine Periode** der Bandstruktur $E(k)$ — und deshalb reicht es, $E(k)$ nur auf der 1.
Brillouin-Zone zu betrachten; alles andere wiederholt sich. Genau das macht die Bandstruktur-Darstellung im
nächsten Oberthema so kompakt.

:::grafik
Die $E(k)$-Kurve mit dem Bereich $[-\pi/a, +\pi/a]$ farbig unterlegt als 1. Brillouin-Zone; links und rechts
davon blass die Wiederholungen. Hinweis „eine Periode genügt".
:::

## BCC und FCC tauschen die Plätze

Ein überraschendes, für Silizium wichtiges Ergebnis: Setzt man die primitiven **BCC**-Vektoren in die
$\vec b_i$-Formeln ein, kommt ein **FCC**-Gitter im reziproken Raum heraus — und umgekehrt ist das reziproke
Gitter von FCC ein BCC ([Cambridge QCMP](https://www.sp.phy.cam.ac.uk/files/media/qcmp_lectures_5-8_2020-21.pdf),
[Oxford Solid State](https://vaia.com/en-us/textbooks/physics/the-oxford-solid-state-basics-1-edition/chapter-13)).

Daraus folgt direkt die Form der Brillouin-Zonen:

- **1. Brillouin-Zone eines FCC-Kristalls** = WS-Zelle des reziproken (BCC-)Gitters = **abgestumpftes
  Oktaeder** (14 Flächen).
- **1. Brillouin-Zone eines BCC-Kristalls** = WS-Zelle des reziproken (FCC-)Gitters = **Rhombendodekaeder**.

Das ist nicht bloß Geometrie: **Silizium** hat die Diamantstruktur (ein FCC-Gitter mit zweiatomiger Basis),
also ist seine Brillouin-Zone das abgestumpfte Oktaeder — die Bühne, auf der die Silizium-Bandstruktur mit ihren
hochsymmetrischen Punkten ($\Gamma$, $X$, $L$) gezeichnet wird.

:::grafik
Links ein BCC-Realgitter → Pfeil „reziprok" → FCC; darunter die resultierende 1. Brillouin-Zone als
abgestumpftes Oktaeder (für FCC-/Diamant-Kristalle wie Si). Daneben FCC → reziprok BCC → Rhombendodekaeder.
:::

:::kern
Ein periodisches Gitter im Ortsraum erzeugt ein periodisches __reziprokes Gitter__ im $k$-Raum. **1D-Kette:** aus
der diskreten Schrödinger-Gleichung mit Bloch-Ansatz $\psi_j = A\,e^{ikja}$ (Nachbarn = Phasenfaktoren
$e^{\pm ika}$) folgt die erste Bandstruktur $E(k) = 2t(1-\cos ka)+V_0$, periodisch mit $2\pi/a$. Die Forderung,
dass gitterperiodische Größen unter $R$ invariant sind ($e^{ikR}\overset{!}{=}1$), liefert das reziproke Gitter
$k_m = m\,2\pi/a$. **3D:** $\vec a_i\cdot\vec b_j = 2\pi\delta_{ij}$ mit
$\vec b_1 = 2\pi\,\tfrac{\vec a_2\times\vec a_3}{\vec a_1\cdot(\vec a_2\times\vec a_3)}$ (Nenner = Zellvolumen). Die
__1. Brillouin-Zone__ ist die Wigner-Seitz-Zelle des reziproken Gitters (1D: $[-\pi/a,\pi/a]$ = eine Periode von
$E(k)$). Reziprok vertauschen sich **BCC $\leftrightarrow$ FCC**; die BZ von FCC/Silizium ist ein abgestumpftes
Oktaeder.
:::

Damit ist das Oberthema Kristallstruktur abgeschlossen — wir haben den Ortsraum (Gitter, Zelle, Bindung,
Herstellung) **und** den $k$-Raum (reziprokes Gitter, Brillouin-Zone). Die erste Bandstruktur $E(k)$ war schon
ein Vorgeschmack. Im nächsten Oberthema, der __Bandstruktur__, verstehen wir, warum aus den vielen Atomniveaus
breite **Bänder** werden, wie dazwischen eine **Bandlücke** entsteht und was ein Material dadurch zum Leiter,
Halbleiter oder Isolator macht.

:::quiz
F: Warum braucht man neben dem Ortsraum-Gitter überhaupt ein zweites Gitter im Wellenzahlraum?
A: Ein Elektron im Kristall ist eine Welle, die man am besten über ihren Wellenvektor $\vec k$ beschreibt. Die Gitterperiodizität zwingt dieser Welle eine Periodizität im $k$-Raum auf, die in einem eigenen Punktmuster — dem reziproken Gitter — lebt; dort spielt die gesamte Elektronenphysik.
F: Warum vereinfacht der Bloch-Ansatz $\psi_j=A e^{ikja}$ die diskrete Schrödinger-Gleichung so stark?
A: Weil sich ein Nachbarplatz dann nur um einen Phasenfaktor unterscheidet ($\psi_{j\pm1}=\psi_j e^{\pm ika}$). Teilt man durch $\psi_j$, verschwindet die ganze Kette und es bleibt eine Gleichung allein für die Zahl $k$.
F: Wie entsteht aus dem Bloch-Ansatz die Bandstruktur $E(k)=2t(1-\cos ka)+V_0$?
A: Einsetzen der Phasenfaktoren und $\tfrac12(e^{ika}+e^{-ika})=\cos(ka)$ liefert direkt $E(k)$. Die Kurve gibt an, welche Energie ein Elektron mit Wellenzahl $k$ hat — eine wellige Funktion zwischen $V_0$ und $V_0+4t$.
F: Warum ist $E(k)$ periodisch mit $2\pi/a$, und was bedeutet das physikalisch?
A: $\cos(ka)$ wiederholt sich mit Periode $2\pi/a$, also auch $E(k)$. Daher beschreiben $k$ und $k+2\pi/a$ denselben physikalischen Zustand — höhere $k$ bringen keine neue Information.
F: Wie folgt das reziproke Gitter aus der Forderung $e^{ikR}=1$?
A: Eine gitterperiodische Größe darf sich beim Verschieben um einen Gittervektor $R=ja$ nicht ändern, also muss der Bloch-Phasenfaktor $e^{ikR}=1$ sein. Das erzwingt $k_m=m\,2\pi/a$ — ein periodisches Punktgitter im $k$-Raum.
F: Was bedeutet „reziprok" an der Beziehung zwischen Real- und $k$-Raum-Gitter?
A: Die Gitterkonstanten verhalten sich invers: Ein großer Atomabstand $a$ ergibt ein enges reziprokes Gitter ($2\pi/a$ klein) und umgekehrt. Weiter Realraum heißt also dichter $k$-Raum.
F: Was besagt die Orthogonalitätsbedingung $\vec a_i\cdot\vec b_j=2\pi\delta_{ij}$?
A: Jeder reziproke Vektor $\vec b_j$ steht senkrecht auf den beiden „anderen" $\vec a$-Vektoren und ergibt mit dem eigenen $\vec a_j$ gerade $2\pi$. Das ist die 3D-Verallgemeinerung von $e^{i\vec k\cdot\vec R}=1$ für alle Gittervektoren.
F: Warum liefert die Kreuzprodukt-Formel für $\vec b_1$ genau diese Bedingung?
A: $\vec b_1\propto\vec a_2\times\vec a_3$ steht per Konstruktion senkrecht auf $\vec a_2$ und $\vec a_3$ (die beiden Skalarprodukte werden null), und der Vorfaktor mit dem Spatprodukt (Zellvolumen) im Nenner ist so gewählt, dass $\vec a_1\cdot\vec b_1=2\pi$ herauskommt.
F: Was ist die 1. Brillouin-Zone, und warum genügt es, $E(k)$ nur dort zu betrachten?
A: Sie ist die Wigner-Seitz-Zelle des reziproken Gitters (1D: $[-\pi/a,\pi/a]$). Da sie genau eine Periode der Bandstruktur umfasst und sich alles andere wiederholt, reicht die Darstellung auf dieser einen Zone.
F: Welche Form hat die Brillouin-Zone von Silizium, und wie kommt das zustande?
A: Reziprok vertauschen sich BCC und FCC; Silizium hat die Diamantstruktur (FCC-Gitter mit zweiatomiger Basis), sein reziprokes Gitter ist also BCC. Dessen Wigner-Seitz-Zelle — und damit die 1. Brillouin-Zone von Si — ist ein abgestumpftes Oktaeder.
:::
