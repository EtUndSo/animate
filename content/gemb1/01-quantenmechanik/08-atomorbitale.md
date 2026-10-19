---
title: Atomorbitale
pfad: Elektrotechnik / 4. Semester / Grundlagen elektronischer Materialien und Bauelemente / Quantenmechanik
order: 4010800
summary: Der Abschluss der Quantenmechanik-Reihe – jetzt kein Kasten mehr, sondern das trichterförmige Coulomb-Potential des Atomkerns. Aus der Schrödinger-Gleichung fallen drei Quantenzahlen, die Energieformel $E_n = -13{,}6\,\text{eV}/n^2$ und die vertrauten s-, p-, d-Orbitale. Mit dem Pauli-Prinzip erklärt das die Schalen und das Periodensystem – und schlägt die Brücke zu Bindungen und Energiebändern im Festkörper.
tags: Atomorbitale, Wasserstoffatom, Quantenzahlen, Coulomb-Potential, Pauli-Prinzip, Schalen, Periodensystem
---

:::grafik
Einstiegs-Animation: Links ein rotierender Satz der bekannten Orbitalformen — eine kugelförmige $s$-Wolke, drei
hantelförmige $p$-Wolken entlang $x,y,z$, dann die komplizierteren $d$-Formen. Die Wolken sind als
Wahrscheinlichkeitsdichte $|\psi|^2$ gezeichnet (dicht = hohe Aufenthaltswahrscheinlichkeit). Rechts baut sich
daraus ein Schalenbild auf: $n=1,2,3$ als Energieleiter, die Elektronen füllen die Plätze von unten auf.
Kernbotschaft: Dieselbe Schrödinger-Gleichung wie in der Box — nur im Trichter-Potential des Kerns — erzeugt die
Orbitale, aus denen Chemie und Festkörper aufgebaut sind.
:::

:::konzept
Wir haben das Elektron bisher in **Kästen** mit flachem Boden gesperrt. Im Atom ist das Potential aber kein
Kasten, sondern der **trichterförmige** Sog des positiven Kerns: Je näher das Elektron kommt, desto tiefer
fällt die Energie (das Coulomb-Potential $\propto -1/r$). Löst man die Schrödinger-Gleichung für diesen Trichter,
kommen keine einfachen Sinus-Wellen heraus, sondern die __Atomorbitale__ — die dreidimensionalen
Aufenthaltswolken $s, p, d, \dots$. Sie sind das letzte Puzzleteil der Quantenmechanik, das wir brauchen: Aus
ihnen entstehen durch das __Pauli-Prinzip__ die Elektronenschalen, das Periodensystem — und, wenn viele Atome
zusammenrücken, die **Energiebänder** des Festkörpers, um die es im Rest dieses Moduls geht.
:::

**Worum es geht:** Wir lösen (qualitativ) die Schrödinger-Gleichung für das einfachste Atom, den Wasserstoff, und
sehen, wie aus dem dreidimensionalen Trichter-Potential **drei Quantenzahlen**, die Energieformel und die
Orbitalformen entstehen. Dann füllen wir die Orbitale mit Elektronen und erklären damit Schalen und
Periodensystem — und schlagen die Brücke zum Festkörper.

## Das Potential: ein Trichter statt eines Kastens

Im Wasserstoffatom zieht der Kern (eine positive Ladung $+e$) das Elektron (Ladung $-e$) an. Die potentielle
Energie dieser Anziehung ist das __Coulomb-Potential__

$$V(r) = -\frac{e^2}{4\pi\varepsilon_0\, r}.$$

- __$r$__: der Abstand zwischen Elektron und Kern.
- __$-$ Vorzeichen__: Die Energie ist **negativ** — das Elektron ist gebunden, es sitzt in einer Energiemulde.
- __$\propto 1/r$__: Der „Trichter" wird zum Kern hin ($r \to 0$) unendlich tief.

Der entscheidende Unterschied zur Box: Dieses Potential hat **keine senkrechten Wände** und **keinen flachen
Boden** — es ist radialsymmetrisch (hängt nur vom Abstand $r$ ab, nicht von der Richtung) und wird nach innen
immer tiefer. Genau diese Form bestimmt, welche Wellen hineinpassen.

:::grafik
Querschnitt des Coulomb-Trichters $V(r) = -e^2/(4\pi\varepsilon_0 r)$: eine nach innen immer steiler abfallende
Kurve. Zum Vergleich daneben der Kasten mit flachem Boden und senkrechten Wänden. Beschriftung: „Kasten → feste
Wände" vs. „Atom → Trichter, radialsymmetrisch".
:::

## Drei Richtungen, drei Quantenzahlen

Wie beim 3D-Kasten ist das Elektron in **allen drei** Raumrichtungen gebunden — und wie dort führt jede
Richtung eine eigene Quantenzahl ein. Weil der Trichter aber kugelsymmetrisch ist, rechnet man nicht in
$x,y,z$, sondern in **Kugelkoordinaten** (Abstand $r$, zwei Winkel $\theta, \varphi$). Der Separationsansatz
trennt die Wellenfunktion in einen **Radialteil** (hängt von $r$ ab) und einen **Winkelteil**:

$$\psi_{n,l,m}(r,\theta,\varphi) = R_{n,l}(r)\cdot Y_{l,m}(\theta,\varphi).$$

- __$R_{n,l}(r)$__: der __Radialteil__ — beschreibt, in welchem Abstand vom Kern sich das Elektron aufhält.
- __$Y_{l,m}(\theta,\varphi)$__: der __Winkelteil__ (die __Kugelflächenfunktionen__) — beschreibt die **Form**
  bzw. Ausrichtung der Wolke.

Aus den Randbedingungen in jeder Koordinate fallen drei __Quantenzahlen__ mit festen Wertebereichen
([uni-frankfurt](https://www.theochem.uni-frankfurt.de/teaching/2018_2019_ws_tc1/TC1_L12_2018_19.pdf),
[chemie.de](https://www.chemie.de/lexikon/Wasserstoffatom.html)):

- __Hauptquantenzahl $n = 1, 2, 3, \dots$__ — bestimmt die **Energie** und grob die Größe der Wolke (die
  „Schale"). Sie ist das direkte Gegenstück zur Quantenzahl der Box.
- __Nebenquantenzahl $l = 0, 1, \dots, n-1$__ — bestimmt die **Form** (den Bahndrehimpuls). Die Werte
  $l = 0,1,2,3$ heißen traditionell $s, p, d, f$.
- __Magnetquantenzahl $m = -l, \dots, 0, \dots, +l$__ — bestimmt die **Ausrichtung** der Wolke im Raum (ihre
  Orientierung z. B. relativ zu einem Magnetfeld).

:::grafik
Ein Baumdiagramm: oben $n$ (Schale), darunter die erlaubten $l$ (Form), darunter die erlaubten $m$
(Ausrichtung). Für $n=2$ beispielhaft ausgeklappt: $l=0$ (ein $s$) und $l=1$ (drei $p$ mit $m=-1,0,+1$). Jede
Verzweigung ist mit ihrem Wertebereich beschriftet ($l<n$, $|m|\le l$).
:::

## Die Energie — und eine überraschende Entartung

Löst man den Radialteil, kommt für das Wasserstoffatom eine bemerkenswert einfache Energieformel heraus:

$$E_n = -\frac{E_0}{n^2}, \qquad E_0 \approx 13{,}6\ \text{eV}.$$

- __$E_n$__: die Energie des Niveaus — **negativ** (gebunden), und mit wachsendem $n$ rückt sie gegen null
  (immer schwächer gebunden).
- __$E_0 \approx 13{,}6\ \text{eV}$__: die __Rydberg-Energie__; $-13{,}6\,$eV ist die Energie des Grundzustands
  ($n=1$, das $1s$-Orbital) — zugleich die Energie, die man braucht, um das Elektron ganz vom Atom zu lösen.

Das Überraschende: Die Energie hängt **nur von $n$** ab — **nicht** von $l$ oder $m$
([evulpo](https://evulpo.com/de/de/dashboard/lesson/de-p-sek-06structure-of-matter-02quantum-physics-03energyvalues-and-orbitals-of-the-hydrogen-atom)).
Alle Orbitale einer Schale ($2s$ und $2p$, oder $3s$, $3p$, $3d$) liegen energetisch gleich — sie sind
__entartet__. Zählt man alle $(l,m)$-Kombinationen zu festem $n$, kommt man auf genau $n^2$ Zustände gleicher
Energie. Diese starke Entartung ist eine Besonderheit des $1/r$-Potentials; bei einem anderen Trichter-Profil
wäre sie aufgehoben. (Im Mehrelektronen-Atom ist sie es tatsächlich — dort liegt $2s$ etwas tiefer als $2p$.)

:::grafik
Energieleiter $E_n = -13{,}6\,\text{eV}/n^2$: die Sprossen bei $-13{,}6$, $-3{,}4$, $-1{,}5$ eV rücken nach oben
immer enger zusammen und häufen sich bei $E=0$. Neben jeder Sprosse ist angedeutet, wie viele Orbitale ($n^2$)
auf ihr liegen — alle auf gleicher Höhe (entartet).
:::

## Die Formen: s, p, d

Der Winkelteil $Y_{l,m}$ legt fest, wie die Wolke **aussieht**. Die Nebenquantenzahl $l$ (also $s/p/d$) ist dabei
die entscheidende Größe, und zu jedem $l$ gibt es $2l+1$ Orientierungen (die $m$-Werte):

- __$s$ ($l=0$)__: **eine** kugelsymmetrische Wolke — das Elektron ist in alle Richtungen gleich wahrscheinlich.
- __$p$ ($l=1$)__: **drei** hantelförmige Wolken, ausgerichtet entlang $x$, $y$ und $z$.
- __$d$ ($l=2$)__: **fünf** komplexere, meist vierlappige Wolken.

Allgemein gilt also $2l+1$ Orbitale pro Unterschale; summiert man über alle $l$ von $0$ bis $n-1$, erhält man
wieder die $n^2$ Orbitale der Schale.

:::grafik
Galerie der Orbitalformen als $|\psi|^2$-Wolken: 1× $s$ (Kugel), 3× $p$ (Hanteln entlang $x/y/z$), 5× $d$
(vierlappig). Unter jeder Gruppe steht $2l+1$ (= 1, 3, 5) als Zahl der Orientierungen.
:::

## Pauli-Prinzip, Schalen und das Periodensystem

Jetzt kommt die eine Zutat, die aus den Orbitalen echte Atome macht: Elektronen haben zusätzlich einen
**Spin** mit zwei Einstellungen ($\uparrow$ oder $\downarrow$), und das __Pauli-Prinzip__ verbietet, dass zwei
Elektronen in **allen** Quantenzahlen übereinstimmen. Folge: In jedes Orbital passen **höchstens zwei**
Elektronen (ein $\uparrow$, ein $\downarrow$).

Damit lässt sich jedes Atom „auffüllen": Man setzt die Elektronen von unten (tiefste Energie zuerst) in die
Orbitale, je zwei pro Orbital. Pro Schale $n$ gibt es $n^2$ Orbitale, also $2n^2$ Plätze:

- $n=1$: $2\cdot 1 = 2$ Elektronen (K-Schale)
- $n=2$: $2\cdot 4 = 8$ Elektronen (L-Schale)
- $n=3$: $2\cdot 9 = 18$ Elektronen (M-Schale)

Genau diese Zahlen $2, 8, 18, \dots$ sind der Grund für den **Aufbau des Periodensystems** und dafür, warum
chemisch so unterschiedliche Elemente wie die Edelgase (volle Schale) oder die Alkalimetalle (ein einzelnes
Elektron in einer neuen Schale) existieren. Die chemischen Eigenschaften stecken fast vollständig in den
**äußersten**, nur teilweise gefüllten Orbitalen — den __Valenzelektronen__.

:::grafik
Ein Aufbau-Schema: Energieleiter mit Orbitalkästchen ($1s$; $2s$, $2p$; $3s$, $3p$ …), die mit Pfeil-Paaren
($\uparrow\downarrow$) von unten aufgefüllt werden. Am Rand die Schalen-Kapazitäten $2, 8, 18$ und die Markierung
der obersten, nur teilgefüllten __Valenzelektronen__.
:::

:::kern
Im Atom ersetzt das __Coulomb-Potential__ $V(r)=-e^2/(4\pi\varepsilon_0 r)$ (Trichter, radialsymmetrisch) den
Kasten. Die Schrödinger-Gleichung trennt in Radial- und Winkelteil $\psi_{nlm}=R_{nl}(r)\,Y_{lm}(\theta,\varphi)$
und liefert **drei Quantenzahlen**: $n$ (Energie/Größe), $l=0..n{-}1$ (Form: $s,p,d,f$), $m=-l..+l$ (Ausrichtung,
$2l+1$ Stück). Die Energie $E_n=-13{,}6\,\text{eV}/n^2$ hängt **nur von $n$** ab → jede Schale ist $n^2$-fach
__entartet__ (Besonderheit des $1/r$-Potentials). Mit Spin und __Pauli-Prinzip__ (max. 2 Elektronen pro Orbital)
fasst Schale $n$ genau $2n^2$ Elektronen ($2,8,18,\dots$) — das erklärt Schalen, __Valenzelektronen__ und das
Periodensystem.
:::

Damit ist die Quantenmechanik-Grundausstattung komplett: Wir wissen, wie **ein** Elektron in einem Potential
gebundene, diskrete Zustände einnimmt. Im Festkörper sitzen aber $10^{23}$ Atome dicht beieinander. Wenn ihre
Orbitale überlappen, verschmelzen die vielen einzelnen Niveaus zu breiten __Energiebändern__ — und genau daraus
ergibt sich, ob ein Material Leiter, Halbleiter oder Isolator ist. Bevor wir das verstehen, brauchen wir aber
erst das Gerüst, in dem die Atome stecken: die __Kristallstruktur__, das Thema des nächsten Oberthemas.
