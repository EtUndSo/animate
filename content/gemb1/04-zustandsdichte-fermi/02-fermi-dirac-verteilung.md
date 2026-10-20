---
title: Die Fermi-Dirac-Verteilung
pfad: Elektrotechnik / 4. Semester / Grundlagen elektronischer Materialien und Bauelemente / Zustandsdichte und Fermi-Verteilung
order: 4040200
summary: Welche der vorhandenen Plätze tatsächlich besetzt sind – die Besetzungswahrscheinlichkeit $f(E)=1/(1+e^{(E-E_f)/k_BT})$. Am Fermi-Niveau ist sie immer genau $\tfrac12$. Bei $T=0$ ist sie eine scharfe Stufe (alles bis $E_f$ voll), bei $T>0$ weicht sie über einige $k_BT$ auf. Weit oberhalb von $E_f$ vereinfacht sie sich zur Boltzmann-Verteilung – der Schlüssel zu einfachen Ladungsträgerformeln.
tags: Fermi-Dirac-Verteilung, Fermi-Energie, chemisches Potential, Pauli-Prinzip, Boltzmann-Näherung, thermisches Gleichgewicht, Besetzungswahrscheinlichkeit
---

:::grafik
Einstiegs-Animation: Die Kurve $f(E)$ über der Energie. Zuerst bei $T=0$ eine scharfe **Stufe**: links von $E_f$
gleich $1$ (voll besetzt), rechts $0$ (leer). Dann steigt die Temperatur, und die Stufe **weicht auf** zu einer
weichen S-Kurve — manche Zustände unter $E_f$ werden leer, manche darüber besetzt. Alle Kurven drehen sich dabei
um **denselben Punkt** $(E_f, \tfrac12)$. Nebenbei ein „Wasserpegel"-Bild: die Elektronen füllen die Plätze von
unten bis zur Höhe $E_f$. Kernbotschaft: $E_f$ ist der Füllstand, die Temperatur die Aufweichungsbreite.
:::

:::konzept
Die Zustandsdichte $D(E)$ hat uns gesagt, **wo** die Plätze sind. Jetzt die zweite Hälfte: **Welche** davon sind
besetzt? Elektronen sind __Fermionen__ und gehorchen dem Pauli-Prinzip — pro Zustand höchstens eines. Die
Statistik sehr vieler solcher Teilchen im thermischen Gleichgewicht liefert eine eindeutige Antwort: die
__Fermi-Dirac-Verteilung__ $f(E)$. Sie ist die **Besetzungsregel** und die zentrale Stellgröße der
Halbleiterphysik, denn über das __Fermi-Niveau__ $E_f$ steuert man (durch Dotierung oder Spannung) die Besetzung
**aller** Zustände auf einmal. Zusammen mit $D(E)$ ergibt sie im nächsten Artikel die Ladungsträgerdichte.
:::

**Worum es geht:** Wir stellen die __Fermi-Dirac-Verteilung__ vor, verstehen die Bedeutung des __Fermi-Niveaus__,
lesen die Grenzfälle $T=0$ und $T>0$ ab und leiten die __Boltzmann-Näherung__ her, die später einfache Formeln für
die Ladungsträgerdichte ermöglicht.

## Die Verteilung und ihre Bausteine

Für die Verteilung vieler ununterscheidbarer Fermionen auf viele Energieniveaus im **thermischen Gleichgewicht**
(feste Temperatur $T$) liefert die statistische Physik:

$$f(E) = \frac{1}{1 + \exp\!\left(\dfrac{E - E_f}{k_B T}\right)}.$$

$f(E)$ ist die **Wahrscheinlichkeit, dass ein Zustand bei der Energie $E$ besetzt ist** (ein Wert zwischen 0 und
1). Die Zutaten:

- __$E_f$__: die __Fermi-Energie__ (auch __Fermi-Niveau__) — der Energiewert, bei dem die
  Besetzungswahrscheinlichkeit genau $\tfrac12$ ist. Sie ist das __chemische Potential__ der Elektronen, der
  „Wasserstand". Wichtig: $E_f$ muss **kein erlaubter Zustand** sein — bei einem Halbleiter liegt sie mitten in
  der Bandlücke, wo es gar keine Zustände gibt.
- __$k_B T$__: die __thermische Energie__ ($k_B$ = Boltzmann-Konstante). Bei Raumtemperatur ($T\approx300\,$K) ist
  $k_B T \approx 25{,}9\,$meV. Sie legt die „Aufweichungsbreite" der Verteilung fest.

:::grafik
Die S-förmige Kurve $f(E)$ über $E$, von 1 (links) auf 0 (rechts) fallend, mit markiertem Punkt $(E_f, \tfrac12)$.
Die Breite des Übergangsbereichs ist als „$\sim$ einige $k_B T$" bemaßt.
:::

## Die Grenzfälle sofort ablesbar

Direkt aus der Formel:

- **Am Fermi-Niveau** ($E = E_f$): Der Exponent ist $0$, also $\exp(0)=1$ und $f = \tfrac{1}{1+1} = \tfrac12$ —
  und zwar bei **jeder** Temperatur.
- **Weit unterhalb** ($E \ll E_f$): Exponent stark negativ → $f \to 1$ (Zustand sicher besetzt).
- **Weit oberhalb** ($E \gg E_f$): Exponent stark positiv → $f \to 0$ (Zustand sicher leer).

:::grafik
Dieselbe $f(E)$-Kurve, an drei Stellen beschriftet: linker Plateaubereich „$f\approx1$ besetzt", der Punkt
„$f=\tfrac12$ bei $E_f$", rechter Bereich „$f\approx0$ leer".
:::

## Bei T = 0: die scharfe Stufe

Am absoluten Nullpunkt springt der Exponent bei $E = E_f$ von $-\infty$ auf $+\infty$. Die Verteilung wird zur
**Stufenfunktion**: alle Zustände bis $E_f$ exakt besetzt ($f=1$), alle darüber exakt leer ($f=0$).

**Warum genau diese Stufe?** Bei $T=0$ gibt es keine thermische Energie, um ein Elektron über $E_f$ zu heben. Das
Pauli-Prinzip zwingt die Elektronen, die Plätze **lückenlos von unten** aufzufüllen — wie Wasser, das ein Gefäß
bis zu einer scharfen Oberfläche füllt. Das ist der Grundzustand des Elektronensystems.

:::grafik
$f(E)$ bei $T=0$ als rechteckige Stufe (1 bis $E_f$, dann 0). Daneben das Füllbild: Energieplätze von unten bis zur
scharfen Linie $E_f$ voll, darüber leer.
:::

## Bei T > 0: die Stufe weicht auf

Mit steigender Temperatur „weicht" die thermische Energie die Stufe auf: In einem Fenster von einigen $k_B T$ um
$E_f$ werden manche Zustände **unterhalb** $E_f$ leer (ein Elektron wurde thermisch angeregt) und manche
**oberhalb** besetzt. Je höher $T$, desto breiter dieser Übergang.

Entscheidend: Alle Kurven drehen sich um den **Fixpunkt** $(E_f, \tfrac12)$. Die Temperatur ändert die **Breite**
des Übergangs, nicht diesen Angelpunkt.

:::grafik
Mehrere $f(E)$-Kurven für $T=0$ (Stufe) und wachsende $T_1 < T_2 < T_3$ (immer breitere S-Kurven), die sich alle
im Punkt $(E_f, \tfrac12)$ schneiden. Pfeile „breiter mit höherer Temperatur".
:::

**Warum diese Statistik für Elektronen?** Weil das Pauli-Prinzip verbietet, dass sich Teilchen im selben Zustand
häufen. Klassische (unterscheidbare) Teilchen dürften das — sie folgen der Boltzmann-Statistik, bei der beliebig
viele dasselbe Niveau besetzen. Fermionen können das nicht, und genau dieser Zwang „ein Platz, ein Teilchen"
führt mathematisch auf die Fermi-Dirac-Form mit der charakteristischen Sättigung bei $f=1$.

## Die Boltzmann-Näherung

Für die spätere Integration ist die volle Fermi-Funktion unbequem. Zum Glück vereinfacht sie sich für Zustände
**weit oberhalb** des Fermi-Niveaus — genau der Fall für Elektronen im Leitungsband eines Halbleiters, wo die
Bandkante typisch $\gtrsim 0{,}5\,$eV über $E_f$ liegt, also $E - E_f \gg k_B T$. Dann ist der Exponentialterm
riesig, und man darf im Nenner die $1$ vernachlässigen:

$$f(E) = \frac{1}{1 + \underbrace{\exp\!\big(\tfrac{E-E_f}{k_B T}\big)}_{\gg 1}} \;\approx\; \exp\!\left(-\frac{E-E_f}{k_B T}\right).$$

Das ist die **Boltzmann-Verteilung** — die klassische Näherung, in der das Pauli-Prinzip keine Rolle mehr spielt,
weil die Plätze so dünn besetzt sind ($f \ll 1$), dass sich praktisch nie zwei Elektronen um denselben streiten.
Genau diese Vereinfachung macht die Ladungsträgerdichten im nächsten Artikel zu einfachen Exponentialformeln.

**Grenze (wichtig):** Die Näherung gilt nur für __nicht-entartete__ Halbleiter, bei denen $E_f$ mehrere $k_B T$
**innerhalb** der Bandlücke von der Bandkante entfernt bleibt. Rückt $E_f$ durch starke Dotierung an eine
Bandkante oder ins Band (ein __entarteter__ Halbleiter), muss man wieder die volle Fermi-Funktion verwenden.

:::grafik
Die volle $f(E)$-Kurve und darüber gestrichelt die exponentielle Boltzmann-Näherung; beide liegen weit rechts von
$E_f$ (im „Schwanz") praktisch übereinander, nahe $E_f$ weichen sie sichtbar ab. Markiert der Gültigkeitsbereich
„$E-E_f \gg k_B T$".
:::

:::kern
Die __Fermi-Dirac-Verteilung__ $f(E)=\dfrac{1}{1+\exp((E-E_f)/k_BT)}$ gibt die Besetzungswahrscheinlichkeit eines
Zustands an. Das __Fermi-Niveau__ $E_f$ (= chemisches Potential, „Wasserstand") ist die Energie mit
$f(E_f)=\tfrac12$ — **immer**, bei jeder Temperatur — und muss selbst kein erlaubter Zustand sein. $k_BT\approx
25{,}9\,$meV (300 K) ist die Aufweichungsbreite. **$T=0$:** scharfe **Stufe** (Pauli füllt lückenlos von unten).
**$T>0$:** Aufweichung über einige $k_BT$ um $E_f$, Kurven drehen um den Fixpunkt $(E_f,\tfrac12)$. Für $E-E_f\gg
k_BT$ (Leitungsband eines nicht-entarteten Halbleiters) gilt die __Boltzmann-Näherung__
$f\approx e^{-(E-E_f)/k_BT}$ — Grundlage der einfachen Ladungsträgerformeln.
:::

Wir haben jetzt beide Bausteine: $D(E)$ sagt, **wo** Plätze sind, $f(E)$, **welche** besetzt sind. Ihr Produkt,
über die Energie integriert, ergibt die gesuchte __Ladungsträgerdichte__ — Elektronen im Leitungsband und Löcher
im Valenzband. Das ist das Thema des nächsten Artikels, der die Kette aus Quantenmechanik und Statistik
abschließt.

:::quiz
F: Was gibt die Fermi-Dirac-Verteilung $f(E)$ an?
A: Die Wahrscheinlichkeit (zwischen 0 und 1), dass ein Zustand bei der Energie $E$ im thermischen Gleichgewicht besetzt ist. Zusammen mit der Zustandsdichte sagt sie, welche der vorhandenen Plätze tatsächlich gefüllt sind.
F: Was bedeutet das Fermi-Niveau $E_f$, und warum muss es kein erlaubter Zustand sein?
A: $E_f$ ist die Energie mit Besetzungswahrscheinlichkeit $\tfrac12$ — das chemische Potential bzw. der „Wasserstand" der Elektronen. Es ist nur ein Bezugswert der Statistik; bei einem Halbleiter liegt es mitten in der Bandlücke, wo es gar keine Zustände gibt.
F: Warum ist $f(E_f)=\tfrac12$ bei jeder Temperatur?
A: Bei $E=E_f$ ist der Exponent $(E-E_f)/k_BT=0$, also $\exp(0)=1$ und $f=\tfrac{1}{1+1}=\tfrac12$. Die Temperatur kürzt sich heraus — deshalb drehen sich alle Kurven um den Fixpunkt $(E_f,\tfrac12)$.
F: Wie sieht die Verteilung bei $T=0$ aus und warum?
A: Eine scharfe Stufe: alle Zustände bis $E_f$ besetzt ($f=1$), alle darüber leer ($f=0$). Ohne thermische Energie kann kein Elektron über $E_f$ gehoben werden, und das Pauli-Prinzip füllt die Plätze lückenlos von unten auf.
F: Was passiert mit der Verteilung bei steigender Temperatur?
A: Die Stufe weicht auf — in einem Fenster von einigen $k_BT$ um $E_f$ werden manche Zustände darunter leer und manche darüber besetzt. Je höher $T$, desto breiter der Übergang, aber der Fixpunkt $(E_f,\tfrac12)$ bleibt.
F: Warum folgen Elektronen der Fermi-Dirac- und nicht der Boltzmann-Statistik?
A: Das Pauli-Prinzip verbietet, dass zwei Elektronen denselben Zustand besetzen — klassische Teilchen dürften sich beliebig häufen. Dieser Zwang „ein Platz, ein Teilchen" führt auf die Sättigung bei $f=1$ und damit die charakteristische Fermi-Dirac-Form.
F: Was bedeutet die thermische Energie $k_BT$ für die Verteilung?
A: Sie legt die Breite des Übergangsbereichs fest (bei 300 K rund 26 meV). Nur in einem Fenster von einigen $k_BT$ um $E_f$ ist $f$ weder 0 noch 1 — dort findet die thermische Umverteilung statt.
F: Wie entsteht aus der Fermi-Funktion die Boltzmann-Näherung?
A: Weit oberhalb von $E_f$ ($E-E_f\gg k_BT$) ist der Exponentialterm riesig, sodass man im Nenner die 1 vernachlässigen darf. Übrig bleibt $f\approx e^{-(E-E_f)/k_BT}$ — die klassische Boltzmann-Verteilung.
F: Warum spielt in der Boltzmann-Näherung das Pauli-Prinzip keine Rolle mehr?
A: Dort ist $f\ll1$, die Plätze sind so dünn besetzt, dass praktisch nie zwei Elektronen um denselben Zustand konkurrieren. Ohne diese Konkurrenz verhalten sich die Elektronen wie klassische, unterscheidbare Teilchen.
F: Wann versagt die Boltzmann-Näherung?
A: Bei entarteten Halbleitern, wo $E_f$ durch starke Dotierung an eine Bandkante oder ins Band rückt. Dann ist $E-E_f$ nicht mehr $\gg k_BT$, die 1 im Nenner zählt wieder, und man muss die volle Fermi-Funktion verwenden.
:::
