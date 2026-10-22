---
title: Millerindizes
pfad: Elektrotechnik / 4. Semester / Grundlagen elektronischer Materialien und Bauelemente / Kristallstruktur
order: 4020300
summary: Die kompakte Sprache, mit der man Ebenen und Richtungen in einem Kristall benennt. Der Trick: Man arbeitet mit den Kehrwerten der Achsabschnitte – so wird aus einer achsenparallelen Ebene (Abschnitt $\infty$) eine harmlose $0$. Daraus folgen die Notationen $(hkl)$ für Ebenen, $[uvw]$ für Richtungen, und die im kubischen System nützliche Regel $[hkl]\perp(hkl)$.
tags: Millerindizes, Kristallebene, Kristallrichtung, Kehrwerte, kubisches System, Silizium-Ätzen, Notation
---

:::grafik
Einstiegs-Animation: Ein Würfel dreht sich langsam; nacheinander leuchten verschiedene Kristallebenen auf und
werden beschriftet: eine Würfelfläche $(100)$, eine diagonale Ebene $(110)$, eine schräge Dreiecksebene $(111)$.
Zu jeder Ebene erscheinen kurz die Achsabschnitte und daneben, wie daraus über Kehrwerte die drei Indizes
entstehen. Kernbotschaft: Jede Ebene und jede Richtung im Kristall bekommt einen eindeutigen, kurzen Namen aus
drei Zahlen.
:::

:::konzept
Ein Kristall ist nicht in alle Richtungen gleich. Bestimmte Ebenen spalten leichter, bestimmte Flächen ätzen
langsamer, Ladungen fließen in manchen Richtungen besser. Man braucht daher eine **kompakte, eindeutige
Sprache**, um „diese Ebene" oder „jene Richtung" zu benennen — ohne jedes Mal Winkel und Achsabschnitte
ausschreiben zu müssen. Das leisten die __Millerindizes__. Ihr cleverer Kern ist ein kleiner Trick mit
**Kehrwerten**, der genau das Problem löst, an dem eine naive Benennung scheitern würde.
:::

**Worum es geht:** Wir leiten her, *warum* man Ebenen über die **Kehrwerte** ihrer Achsabschnitte benennt,
üben das Rezept an Beispielen, führen die Notation für __Richtungen__ ein, und sehen am anisotropen Ätzen von
Silizium, wofür das in der Technik konkret gebraucht wird.

## Warum Kehrwerte? Das Problem mit dem naiven Ansatz

Die naheliegende Idee wäre: Benenne eine Ebene einfach durch ihre drei **Achsabschnitte** — wo schneidet sie die
$x$-, $y$- und $z$-Achse (in Einheiten der Gitterkonstante)? Das funktioniert fast, scheitert aber an einem
häufigen Fall: Viele wichtige Ebenen liegen **parallel** zu einer Achse. Eine achsenparallele Ebene schneidet
diese Achse erst „im Unendlichen" — ihr Achsabschnitt ist $\infty$. Mit Unendlich zu rechnen und zu benennen ist
unpraktisch.

Der Trick: Man nimmt die **Kehrwerte** der Achsabschnitte. Denn der Kehrwert von Unendlich ist die harmlose
**Null**:

$$\frac{1}{\infty} = 0.$$

So wird aus „parallel zur Achse" (Abschnitt $\infty$) einfach der Index $0$ — keine Sonderbehandlung nötig.
Das ist der ganze Grund für die auf den ersten Blick seltsame Kehrwert-Vorschrift.

:::grafik
Eine Ebene parallel zur $y$- und $z$-Achse, die die $x$-Achse bei $1$ schneidet. Die Achsabschnitte
$1, \infty, \infty$ stehen daneben, darunter ihre Kehrwerte $1, 0, 0$ → Index $(100)$. Hervorgehoben: „$\infty$
wird zu $0$".
:::

## Das Rezept für die Ebene (hkl)

Die Millerindizes $(hkl)$ einer Kristallebene bildet man in vier Schritten:

1. **Achsabschnitte** der Ebene mit den drei Achsen bestimmen (in Einheiten der Gitterkonstante).
2. Gemeinsame Faktoren **kürzen**.
3. **Kehrwerte** dieser Abschnitte bilden.
4. Mit dem kleinsten gemeinsamen Vielfachen der Nenner multiplizieren, bis **drei ganze, teilerfremde Zahlen**
   dastehen.

Das Ergebnis schreibt man in **runden Klammern** $(hkl)$ — ohne Kommas, ohne Leerzeichen. Ein negativer Index
wird als Balken über der Zahl geschrieben (z. B. $(\bar1 00)$).

**Durchgerechnetes Beispiel — Ebene mit Achsabschnitten $1, 1, 2$:**

$$\text{Abschnitte } 1,\,1,\,2 \;\longrightarrow\; \text{Kehrwerte } 1,\,1,\,\tfrac12 \;\xrightarrow{\times 2}\; (2\,2\,1).$$

:::grafik
Ein Würfel mit einer Ebene, die $x$ bei $1$, $y$ bei $1$, $z$ bei $2$ schneidet. Daneben die Rechnung
$1,1,2 \to 1,1,\tfrac12 \to (221)$ Schritt für Schritt eingeblendet.
:::

**Weitere wichtige Ebenen** (alle im Würfel):

- $(100)$: eine **Würfelfläche** (parallel zu $y$ und $z$).
- $(110)$: eine **diagonale** Ebene durch zwei gegenüberliegende Kanten.
- $(111)$: die Ebene, die alle drei Achsen bei $1$ schneidet (ein Dreieck, das drei Würfelecken verbindet).

Eine einzelne Ebene schreibt man $(hkl)$; die **Menge aller symmetrisch gleichwertigen** Ebenen fasst man in
**geschweiften Klammern** $\{hkl\}$ zusammen. Im Würfel gehören z. B. alle 6 Seitenflächen zur Familie
$\{100\}$.

:::grafik
Drei kleine Würfel nebeneinander mit je einer markierten Ebene: $(100)$ (Seitenfläche), $(110)$ (diagonale
Ebene), $(111)$ (Dreiecksebene). Darunter der Hinweis: $\{100\}$ = alle 6 äquivalenten Seitenflächen.
:::

## Richtungen [uvw]

Eine **Richtung** im Kristall schreibt man als Linearkombination der Gittervektoren:

$$\vec r = u\,\vec a_1 + v\,\vec a_2 + w\,\vec a_3.$$

- __$[uvw]$__: eine **einzelne** Richtung (eckige Klammern, keine Kommas), wobei $u,v,w$ auf kleinste ganze
  Zahlen gebracht werden.
- __$\langle uvw \rangle$__: die **Menge aller gleichwertigen** Richtungen.

Der Unterschied zur Ebene ist wichtig: Bei Richtungen nimmt man die Komponenten **direkt** (keine Kehrwerte) —
die Kehrwert-Vorschrift gilt nur für Ebenen.

:::grafik
Ein Würfel mit eingezeichneten Richtungspfeilen: $[100]$ entlang einer Kante, $[110]$ entlang einer
Flächendiagonale, $[111]$ entlang der Raumdiagonale. Notation-Legende: $[uvw]$ eine Richtung, $\langle uvw\rangle$
Richtungsschar, $(hkl)$ Ebene, $\{hkl\}$ Ebenenschar.
:::

## Die kubische Sonderregel — und ihre Grenze

Im **kubischen** Kristallsystem gilt eine besonders nützliche Beziehung: Die Richtung $[hkl]$ steht **senkrecht**
auf der gleichnamigen Ebene $(hkl)$.

$$[hkl] \perp (hkl) \qquad (\text{nur im kubischen System!}).$$

So ist etwa $[111]$ die Flächennormale von $(111)$. **Warum nur kubisch?** Weil nur dort die drei Achsen
orthogonal **und** gleich lang sind. In anderen Systemen (hexagonal, monoklin …) sind die Achsen schief oder
verschieden lang — dann stimmt die Senkrecht-Beziehung im Allgemeinen **nicht**.

:::grafik
Ein kubischer Würfel mit der Ebene $(111)$ und dem darauf senkrecht stehenden Pfeil $[111]$. Daneben ein schiefes
(monoklines) Gitter, bei dem $[111]$ sichtbar **nicht** senkrecht auf $(111)$ steht — mit rotem „✗".
:::

## Anwendung: anisotropes Ätzen von Silizium

Wozu das Ganze? In der Mikro- und Nanotechnik nutzt man, dass verschiedene Kristallebenen **unterschiedlich
schnell** ätzen. Beim nasschemischen Ätzen von $(100)$-Silizium ätzen die $\{111\}$-Ebenen am **langsamsten** —
sie bleiben als saubere Flanken stehen und legen die Form der geätzten Struktur fest.

Den charakteristischen Flankenwinkel kann man mit der kubischen Sonderregel sofort ausrechnen: Der Winkel
zwischen zwei Ebenen ist der Winkel zwischen ihren Normalenrichtungen $[100]$ und $[111]$. Im kubischen System
gilt für den Winkel zwischen zwei Richtungen das normale Skalarprodukt:

$$\cos\theta = \frac{[100]\cdot[111]}{\big|[100]\big|\,\big|[111]\big|} = \frac{1}{\sqrt{1}\,\sqrt{3}} = \frac{1}{\sqrt3} \;\Longrightarrow\; \theta \approx 54{,}7^\circ.$$

Genau dieser Winkel von $54{,}7^\circ$ tritt zwischen einer $(100)$-Oberfläche und den freigelegten
$\{111\}$-Flanken auf — er bestimmt die Form von Ätzgräben, Membranen und Nanodraht-Flanken in der
Siliziumtechnologie.

:::grafik
Querschnitt durch geätztes $(100)$-Silizium: eine trapezförmige Grube, deren Flanken die $\{111\}$-Ebenen sind;
der Winkel zwischen Oberfläche und Flanke ist mit $54{,}7^\circ$ bemaßt. Daneben die Rechnung
$\cos\theta = 1/\sqrt3$.
:::

:::kern
__Millerindizes__ benennen Ebenen und Richtungen im Kristall. **Ebene $(hkl)$:** Achsabschnitte → **Kehrwerte** →
kleinste teilerfremde ganze Zahlen; der Kehrwert-Trick macht aus einem achsenparallelen Abschnitt $\infty$ die
$0$. **Richtung $[uvw]$:** Komponenten $\vec r = u\vec a_1+v\vec a_2+w\vec a_3$ **direkt** (keine Kehrwerte).
Klammer-Konvention: $(hkl)$ eine Ebene, $\{hkl\}$ Ebenenschar, $[uvw]$ eine Richtung, $\langle uvw\rangle$
Richtungsschar. Im **kubischen** System (und nur dort) gilt $[hkl]\perp(hkl)$. Anwendung: Beim Ätzen von
$(100)$-Si legen die langsamen $\{111\}$-Flanken die Form fest, mit dem Winkel $\cos\theta=1/\sqrt3\Rightarrow
54{,}7^\circ$.
:::

Gitter und ihre Ebenen können wir jetzt beschreiben. Offen bleibt die Frage nach dem **Warum**: Warum ordnen sich
die Atome überhaupt zu einer bestimmten Struktur? Die Antwort liegt in den __Bindungstypen__ — ionisch, kovalent,
metallisch, van der Waals — dem Thema des nächsten Artikels.

:::quiz
F: Warum braucht ein Kristall überhaupt eine eigene Sprache für Ebenen und Richtungen?
A: Weil ein Kristall anisotrop ist: Bestimmte Ebenen spalten leichter, ätzen langsamer oder leiten besser. Man braucht eine kompakte, eindeutige Benennung, um „diese Ebene/Richtung" anzugeben, ohne jedes Mal Winkel und Achsabschnitte auszuschreiben.
F: Warum bildet man die Millerindizes aus den Kehrwerten der Achsabschnitte?
A: Viele wichtige Ebenen liegen parallel zu einer Achse und schneiden sie erst „im Unendlichen" (Abschnitt $\infty$). Der Kehrwert von $\infty$ ist die harmlose $0$, sodass achsenparallele Ebenen ohne Sonderbehandlung einen Index $0$ bekommen — genau dafür ist der Kehrwert-Trick da.
F: Was bedeutet der Index $0$ in einem Millerindex anschaulich?
A: Er bedeutet, dass die Ebene parallel zur entsprechenden Achse verläuft (sie schneidet sie nie im Endlichen). $(100)$ ist z. B. eine Würfelfläche, parallel zur $y$- und $z$-Achse.
F: Wie läuft das vierschrittige Rezept für $(hkl)$ ab?
A: Achsabschnitte bestimmen, gemeinsame Faktoren kürzen, Kehrwerte bilden, mit dem kgV der Nenner auf drei ganze, teilerfremde Zahlen multiplizieren. Das Ergebnis steht in runden Klammern ohne Kommas, negative Indizes als Balken über der Zahl.
F: Worin unterscheidet sich die Benennung von Richtungen von der von Ebenen?
A: Bei Richtungen nimmt man die Komponenten $\vec r=u\vec a_1+v\vec a_2+w\vec a_3$ direkt (auf kleinste ganze Zahlen gebracht), ohne Kehrwerte. Die Kehrwert-Vorschrift gilt ausschließlich für Ebenen.
F: Was bedeuten die verschiedenen Klammern $(hkl)$, $\{hkl\}$, $[uvw]$, $\langle uvw\rangle$?
A: Runde $(hkl)$ = eine einzelne Ebene, geschweifte $\{hkl\}$ = alle symmetrisch gleichwertigen Ebenen; eckige $[uvw]$ = eine einzelne Richtung, spitze $\langle uvw\rangle$ = alle gleichwertigen Richtungen. Einzeln vs. Schar, Ebene vs. Richtung.
F: Warum fasst man z. B. alle sechs Würfelflächen zur Familie $\{100\}$ zusammen?
A: Weil sie durch die Würfelsymmetrie ineinander überführt werden und physikalisch gleichwertig sind — $(100),(010),(001)$ und ihre Gegenflächen verhalten sich identisch. Die geschweifte Klammer benennt diese ganze symmetrische Familie auf einmal.
F: Warum gilt $[hkl]\perp(hkl)$ nur im kubischen System?
A: Nur dort sind die drei Achsen orthogonal und gleich lang, sodass die Richtung mit denselben Zahlen senkrecht auf der Ebene steht. In schiefen oder ungleich langen Systemen (hexagonal, monoklin) stimmt diese Senkrecht-Beziehung im Allgemeinen nicht.
F: Warum legen beim Ätzen von (100)-Silizium gerade die $\{111\}$-Ebenen die Form fest?
A: Die $\{111\}$-Ebenen ätzen am langsamsten, bleiben also als saubere Flanken stehen, während die anderen Richtungen schneller abgetragen werden. Dadurch bestimmen sie die geometrische Form der geätzten Gräben und Membranen.
F: Wie bestimmt man den Flankenwinkel von 54,7° mit der kubischen Sonderregel?
A: Der Winkel zwischen $(100)$-Oberfläche und $\{111\}$-Flanke ist der Winkel zwischen ihren Normalen $[100]$ und $[111]$. Mit dem Skalarprodukt (im kubischen System erlaubt) ist $\cos\theta=\frac{1}{\sqrt1\sqrt3}=1/\sqrt3$, also $\theta\approx54{,}7^\circ$.
:::
