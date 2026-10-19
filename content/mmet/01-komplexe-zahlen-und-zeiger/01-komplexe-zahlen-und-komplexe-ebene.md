---
title: Komplexe Zahlen und die komplexe Ebene
pfad: Elektrotechnik / 1. Semester / Mathematische Methoden der Elektrotechnik / Komplexe Zahlen und Zeiger
order: 10100
summary: Von Grund auf erklärt – warum die reellen Zahlen nicht ausreichen, wie man sie um die imaginäre Einheit $j$ erweitert, wie man mit komplexen Zahlen $z=x+jy$ rechnet und warum die Exponentialform aus mühsamer Rechnung eine einfache Drehung macht. Jede Formel wird hergeleitet; Notation wie in der Vorlesung.
tags: komplexe Zahlen, imaginäre Einheit, komplexe Ebene, Betrag, Argument, Polarform, Eulersche Formel, Multiplikation
---

:::grafik
Einstiegs-Animation: Die komplexe Ebene mit reeller Achse (waagerecht) und imaginärer Achse (senkrecht). Eine
komplexe Zahl erscheint zunächst als Punkt $(x,y)$ und wird zum Pfeil vom Ursprung ($z = x + jy$), mit den
gestrichelten Projektionen $x$ und $y$. Dann der Ausblick auf den Kern des Artikels: Der Pfeil wird mit einer
zweiten komplexen Zahl multipliziert und **dreht und streckt sich** dabei — ein kurzer, langsamer Übergang, der
zeigt, worauf alles hinausläuft (Multiplizieren = Drehen und Strecken).
:::

:::konzept
Komplexe Zahlen lösen ein Problem, an dem die gewohnten Zahlen scheitern, und sie tun das auf eine Weise, die
sich als Glücksfall für die Elektrotechnik herausstellt: Eine komplexe Zahl ist zugleich ein **Punkt in einer
Ebene** und ein **Pfeil** — und das Multiplizieren solcher Pfeile bedeutet **Drehen und Strecken**. Weil
Wechselströme, Schwingungen und Signale im Kern nichts anderes sind als Drehungen, wird mit komplexen Zahlen
aus komplizierter Sinus-Rechnerei eine einfache Multiplikation. Dieser Artikel baut das Schritt für Schritt von
Null auf — niemand muss vorher etwas davon gehört haben.
:::

**Worum es geht:** „Mathematische Methoden der Elektrotechnik" beginnt mit dem Werkzeug, auf dem die gesamte
Signalverarbeitung ruht. Wir klären erst, *warum* man die reellen Zahlen überhaupt erweitern muss, führen die
__imaginäre Einheit__ ein, lernen das Rechnen mit komplexen Zahlen, zeichnen sie in die __komplexe Ebene__ und
arbeiten uns zur __Exponentialform__ vor — und leiten dabei jeden Schritt her.

## Warum reichen die reellen Zahlen nicht?

Fangen wir mit einer scheinbar harmlosen Gleichung an:

$$z^2 = -1.$$

Gibt es eine reelle Zahl $z$, die sie löst? Nein — und man kann genau sagen, warum. Quadriert man irgendeine
reelle Zahl, kommt nie etwas Negatives heraus: Eine positive Zahl mal sich selbst ist positiv
($2\cdot 2 = 4$), eine negative mal sich selbst ist **auch** positiv (denn „minus mal minus ist plus",
$(-2)\cdot(-2) = 4$), und $0^2 = 0$. Das Quadrat jeder reellen Zahl ist also **immer** $\ge 0$. Eine Zahl, deren
Quadrat $-1$ ist, kann unter den reellen Zahlen schlicht nicht existieren.

Lange galt das als das Ende der Geschichte. Der entscheidende Einfall war, die Frage umzudrehen: Statt zu sagen
„so eine Zahl gibt es nicht", **definiert** man einfach eine neue, die genau das leistet — und schaut, ob man
damit widerspruchsfrei rechnen kann. (Man kann; die so entstehenden Zahlen sind sogar in einem präzisen Sinn
„vollständig".) Das ist derselbe Schritt, den die Mathematik schon früher gegangen ist: Auch die negativen
Zahlen („was ist $3 - 5$?") und die Brüche („was ist $1 : 2$?") waren einst neue Erfindungen, die eine Lücke
geschlossen haben.

## Die imaginäre Einheit

Wir führen also eine neue Zahl ein, die __imaginäre Einheit__, und legen als ihre einzige Eigenschaft fest:

$$j = \sqrt{-1}, \qquad\text{also}\qquad j^2 = -1.$$

Die Lösungen von $z^2=-1$ sind damit $z=\pm j$. Ein Wort zur Schreibweise: In der Mathematik heißt diese Einheit
$i$. In der Elektrotechnik ist $i$ aber schon für den **Strom** vergeben, deshalb schreibt man sie dort $j$ — und
so auch in dieser Vorlesung. Wir benutzen durchgehend $j$.

Der Name „imaginär" (eingebildet) ist historisch und etwas unglücklich — er suggeriert, diese Zahlen seien
weniger real als die gewohnten. Das sind sie nicht. $j$ ist einfach eine Zahl in einer **neuen Richtung**, die
senkrecht zu den vertrauten Zahlen zeigt; gleich, wenn wir sie in die Ebene zeichnen, wird das ganz anschaulich.
(Allgemein heißt eine Zahl $j\cdot y$ mit reellem $y$ eine __imaginäre Zahl__.)

## Komplexe Zahlen und das Rechnen mit ihnen

Mit $j$ in der Hand kann man nun Zahlen bauen, die einen gewöhnlichen und einen „neuen" Anteil haben. Eine
__komplexe Zahl__ hat die Form

$$z = x + j\,y, \qquad x,\,y \in \mathbb{R}.$$

- __$z \in \mathbb{C}$__: die __komplexe Zahl__ (($\mathbb{C}$ = Menge der komplexen Zahlen).
- __$x = \operatorname{Re}\{z\}$__: der __Realteil__ — eine ganz gewöhnliche reelle Zahl.
- __$y = \operatorname{Im}\{z\}$__: der __Imaginärteil__ — ebenfalls eine reelle Zahl, nämlich der Faktor **nach**
  dem $j$ (also $y$ selbst, **nicht** $jy$).

Gerechnet wird mit solchen Ausdrücken wie mit gewohnten Klammern — mit der **einen** zusätzlichen Regel, dass
überall $j^2$ durch $-1$ ersetzt wird. Sehen wir uns die beiden Grundrechenarten an, denn gerade hier zeigt
sich später der ganze Vorteil der komplexen Zahlen.

**Addition** ist langweilig einfach: Man addiert Real- und Imaginärteile getrennt,

$$z_1 + z_2 = (x_1 + j y_1) + (x_2 + j y_2) = (x_1 + x_2) + j\,(y_1 + y_2).$$

:::grafik
Animation zur Addition: In der komplexen Ebene liegen zwei Pfeile $z_1$ und $z_2$ vom Ursprung. Der zweite
Pfeil wird an die Spitze des ersten verschoben (Pfeil-an-Pfeil, „Spitze an Fuß"), und der Summenpfeil
$z_1 + z_2$ führt vom Ursprung zur neuen Spitze. Sichtbar wird, dass sich dabei die waagerechten Anteile
($x_1+x_2$) und die senkrechten Anteile ($y_1+y_2$) getrennt addieren — genau die komponentenweise Rechnung.
:::

**Multiplikation** ist der interessante Fall. Man multipliziert die Klammern wie gewohnt aus (jedes Glied mit
jedem) und ersetzt am Ende $j^2$ durch $-1$. Schritt für Schritt:

$$z_1 \cdot z_2 = (x_1 + j y_1)(x_2 + j y_2) = x_1 x_2 + x_1\,j y_2 + j y_1\,x_2 + j y_1\,j y_2.$$

Im letzten Summanden steckt $j\cdot j = j^2 = -1$, also $j y_1\,j y_2 = j^2 y_1 y_2 = -\,y_1 y_2$. Sortiert man
nach reellem und imaginärem Anteil, bleibt

$$z_1 \cdot z_2 = (x_1 x_2 - y_1 y_2) + j\,(x_1 y_2 + x_2 y_1).$$

Das ist korrekt, aber unübersichtlich: vier Produkte, ein Vorzeichenwechsel, getrenntes Sortieren. Und schlimmer
— wenn man eigentlich wissen will, *wie lang* das Ergebnis ist und *in welche Richtung* es zeigt, muss man aus
diesem Ausdruck erst wieder Betrag und Winkel ausrechnen. Merke dir dieses mühsame Ergebnis; wir kommen darauf
zurück und zeigen, dass es mit der Exponentialform in einer Zeile und mit klarer Bedeutung geht.

## Die komplexe Ebene

Eine komplexe Zahl besteht aus **zwei** unabhängigen reellen Zahlen, $x$ und $y$. Alles, was durch zwei Zahlen
festgelegt ist, lässt sich als Punkt in einer **Ebene** zeichnen — und genau das ist die große Idee hinter der
__Gaußschen Zahlenebene__ (der komplexen Ebene). Die waagerechte Achse trägt den Realteil, die senkrechte den
Imaginärteil. Die Zahl $z = x + jy$ ist dann der Punkt mit den Koordinaten $(x, y)$.

Noch nützlicher ist es, $z$ als **Pfeil** vom Ursprung zu diesem Punkt zu sehen. In diesem Bild wird vieles
sofort anschaulich:

- Die **Addition** zweier komplexer Zahlen ist das Aneinanderhängen der Pfeile (Spitze an Fuß), genau wie bei
  Kräften oder Vektoren — das passt zur komponentenweisen Addition von oben.
- Die __konjugiert komplexe Zahl__ $z^* = x - j y$ (gleicher Realteil, Imaginärteil mit umgekehrtem Vorzeichen)
  ist der an der reellen Achse **gespiegelte** Pfeil. Sie ist nützlich, weil ihr Produkt mit $z$ rein reell
  wird: $z\cdot z^* = (x+jy)(x-jy) = x^2 - (jy)^2 = x^2 + y^2$ (hier hebt sich der imaginäre Anteil auf). Das ist
  genau das Quadrat der Pfeillänge — gleich mehr dazu.

Jetzt wird auch klar, warum „imaginär" kein Makel ist: Der imaginäre Anteil ist einfach die **zweite
Koordinate**, die Höhe über der reellen Achse.

:::grafik
Die Gaußsche Zahlenebene mit reeller Achse (waagerecht) und imaginärer Achse (senkrecht). Eine Zahl $z = x + jy$
als Punkt $(x,y)$ und als Pfeil vom Ursprung; gestrichelt die Projektionen auf beide Achsen ($x$ waagerecht, $y$
senkrecht). Zusätzlich die an der reellen Achse gespiegelte konjugierte Zahl $z^*$.
:::

## Betrag und Argument: die Polarform

Einen Pfeil kann man auf zwei Arten festlegen. Bisher haben wir ihn über seine **Koordinaten** $x$ und $y$
beschrieben. Genauso gut geht es über seine **Länge** und seinen **Winkel** — und diese zweite Beschreibung ist
die __Polarform__. Beide enthalten dieselbe Information, nur anders verpackt; wir leiten den Zusammenhang her.

Zeichnet man den Pfeil $z = x + jy$ mitsamt seinen Projektionen, entsteht ein **rechtwinkliges Dreieck**: Die
waagerechte Kathete hat die Länge $x$, die senkrechte die Länge $y$, und der Pfeil selbst ist die Hypotenuse.
Nach dem **Satz des Pythagoras** ist das Quadrat der Hypotenuse die Summe der Kathetenquadrate — die Länge des
Pfeils, der __Betrag__ $r = |z|$, ist also

$$r = |z| = \sqrt{x^2 + y^2}.$$

Den Winkel bekommt man aus den Winkelfunktionen desselben Dreiecks. Der __Winkel__ (das __Argument__) $\alpha$ ist
der Winkel des Pfeils gegen die positive reelle Achse. Im rechtwinkligen Dreieck gilt „Ankathete = Hypotenuse mal
Kosinus" und „Gegenkathete = Hypotenuse mal Sinus", also

$$x = r\cos\alpha, \qquad y = r\sin\alpha.$$

Setzt man das in $z = x + jy$ ein und klammert $r$ aus, erhält man die Polarform:

$$z = x + jy = r\cos\alpha + j\,r\sin\alpha = r\,(\cos\alpha + j\sin\alpha).$$

- __$r = |z|$__: der __Betrag__ — die Länge des Pfeils (immer $\ge 0$).
- __$\alpha$__: der __Winkel / das Argument__ — der Winkel gegen die positive reelle Achse.

**Das Argument ist nur bis auf Vielfache von $2\pi$ eindeutig.** Dreht man den Pfeil um eine volle Umdrehung
weiter, zeigt er wieder gleich: $\alpha_k = \alpha + 2\pi k$ (mit $k\in\mathbb{Z}$) beschreibt dieselbe Zahl $z$.
Die Menge all dieser Winkel heißt $\arg(z)$. Damit die Angabe eindeutig wird, beschränkt man $\alpha$ üblicherweise
auf den __Hauptwert__ $-\pi < \alpha \le \pi$ (er deckt alle vier Quadranten einmal ab).

**Stolperstein: das Argument richtig bestimmen.** Umgekehrt (von $x, y$ zum Winkel) ist man versucht, einfach
$\alpha = \arctan(y/x)$ zu rechnen. Das ist eine häufige Fehlerquelle: Der Arkustangens liefert nur Winkel
zwischen $-\tfrac{\pi}{2}$ und $+\tfrac{\pi}{2}$, deckt also nur die **rechte** Halbebene (I. und IV. Quadrant)
ab. Liegt $z$ links (negativer Realteil $x<0$), zeigt der Pfeil in Wirklichkeit in die andere Richtung, und man
muss $\pi$ addieren. Der Grund ist, dass $\arctan$ aus dem Verhältnis $y/x$ das Vorzeichen von Zähler und Nenner
nicht mehr einzeln sehen kann — $\tfrac{y}{x}$ und $\tfrac{-y}{-x}$ sind gleich, obwohl die Pfeile entgegengesetzt
zeigen. Sicher ist, den **Quadranten** aus den Vorzeichen von $x$ und $y$ mitzudenken; die Funktion
$\operatorname{atan2}(y,x)$ nimmt einem genau das ab.

:::grafik
Derselbe Pfeil $z$ in der Gaußschen Zahlenebene, nun als Hypotenuse eines rechtwinkligen Dreiecks: waagerechte
Kathete $x$, senkrechte Kathete $y$, Hypotenuse $r = |z| = \sqrt{x^2+y^2}$, dazu der eingezeichnete Winkel $\alpha$
als Bogen zur reellen Achse. Beschriftet die Beziehungen $x = r\cos\alpha$ und $y = r\sin\alpha$.
:::

## Die Eulersche Formel – woher sie kommt

Bisher ist $(\cos\alpha + j\sin\alpha)$ nur eine Abkürzung für „Pfeil der Länge 1 unter dem Winkel
$\alpha$". Die __Eulersche Formel__ behauptet nun etwas Erstaunliches — dass dieser Ausdruck **genau** eine
Exponentialfunktion ist:

$$e^{\,j\alpha} = \cos\alpha + j\sin\alpha.$$

Das darf man nicht einfach glauben, man kann es herleiten. Das sauberste Argument nutzt die
**Reihenentwicklungen** (Taylor-Reihen), mit denen man $e^x$, $\cos$ und $\sin$ als unendliche Summen schreibt:

$$e^{x} = 1 + x + \frac{x^2}{2!} + \frac{x^3}{3!} + \frac{x^4}{4!} + \ldots$$

Diese Reihe gilt für jede Zahl, die man einsetzen darf — auch für die imaginäre Zahl $j\alpha$. Setzen wir
sie ein und nutzen die Potenzen von $j$ (die sich im Viererzyklus wiederholen: $j^1 = j$, $j^2 = -1$, $j^3 =
-j$, $j^4 = +1$, dann von vorn):

$$e^{\,j\alpha} = 1 + j\alpha + \frac{(j\alpha)^2}{2!} + \frac{(j\alpha)^3}{3!} + \frac{(j\alpha)^4}{4!} + \ldots
= 1 + j\alpha - \frac{\alpha^2}{2!} - j\frac{\alpha^3}{3!} + \frac{\alpha^4}{4!} + \ldots$$

Jetzt sortiert man die Summanden danach, ob sie ein $j$ enthalten oder nicht — also in einen **reellen** und
einen **imaginären** Teil:

$$e^{\,j\alpha} = \underbrace{\left(1 - \frac{\alpha^2}{2!} + \frac{\alpha^4}{4!} - \ldots\right)}_{=\,\cos\alpha} + \; j\underbrace{\left(\alpha - \frac{\alpha^3}{3!} + \frac{\alpha^5}{5!} - \ldots\right)}_{=\,\sin\alpha}.$$

Die beiden geklammerten Reihen sind aber genau die bekannten Reihenentwicklungen von $\cos\alpha$ und
$\sin\alpha$. Damit ist $e^{j\alpha} = \cos\alpha + j\sin\alpha$ — nicht per Definition, sondern **bewiesen**.

Setzt man diese Formel in die Polarform ein, bekommt die Darstellung ihre endgültige, kompakteste Gestalt, die
__Exponentialform__:

$$z = r\,(\cos\alpha + j\sin\alpha) = r\,e^{\,j\alpha}.$$

- __$r = |z|$__: der __Betrag__ (Länge des Pfeils).
- __$e^{\,j\alpha}$__: der __Einheitszeiger__ — ein Pfeil der Länge 1 unter dem Winkel $\alpha$. Multiplizieren
  mit $r$ streckt ihn auf die richtige Länge.

:::grafik
Der Einheitskreis in der Gaußschen Zahlenebene; auf ihm der Punkt $e^{j\alpha}$ unter dem Winkel $\alpha$, mit den
Projektionen $\cos\alpha$ (auf die reelle Achse) und $\sin\alpha$ (auf die imaginäre Achse). Das illustriert
$e^{j\alpha} = \cos\alpha + j\sin\alpha$: Realteil ist der Kosinus, Imaginärteil der Sinus.
:::

## Der Lohn: Multiplikation als Drehen und Strecken

Jetzt zahlt sich die ganze Vorarbeit aus. Erinnern wir uns an das mühsame kartesische Ergebnis von oben:

$$z_1 \cdot z_2 = (x_1 x_2 - y_1 y_2) + j\,(x_1 y_2 + x_2 y_1).$$

Dasselbe Produkt in der Exponentialform. Wir schreiben beide Zahlen als $z_1 = r_1 e^{j\alpha_1}$ und
$z_2 = r_2 e^{j\alpha_2}$ und multiplizieren — wobei wir nur das Potenzgesetz $e^{a}\cdot e^{b} = e^{a+b}$
brauchen, das auch für imaginäre Exponenten gilt:

$$z_1 \cdot z_2 = r_1 e^{\,j\alpha_1}\cdot r_2 e^{\,j\alpha_2} = r_1\,r_2\;e^{\,j\alpha_1}e^{\,j\alpha_2} = r_1\,r_2\;e^{\,j(\alpha_1 + \alpha_2)}.$$

In Worten: **Die Beträge multiplizieren sich, die Winkel addieren sich.** Und das ist nicht nur kürzer — es ist
auch sofort *bedeutungsvoll*: Man sieht direkt, wie lang ($r_1 r_2$) und wie gedreht ($\alpha_1 + \alpha_2$)
das Ergebnis ist. Das kartesische Ergebnis enthält zwar dieselbe Zahl, verbirgt aber Länge und Winkel in einer
Mischung aus vier Produkten.

Und man sieht auch **warum** sich die Winkel addieren: weil sie als **Exponenten** auftreten und sich Exponenten
beim Multiplizieren addieren. Genau hier steckt der tiefere Grund, überhaupt zur Exponentialform überzugehen.

**Die geometrische Deutung.** Multiplizieren mit einer komplexen Zahl heißt also: **strecken** (um deren Betrag)
und **drehen** (um deren Winkel). Zwei Spezialfälle machen das greifbar:

- Multiplizieren mit einer **reellen** Zahl $c>0$ (Winkel $0$) streckt nur — kein Drehen. Das ist die vertraute
  Skalierung.
- Multiplizieren mit $e^{\,j\alpha}$ (Betrag $1$) **dreht nur** um den Winkel $\alpha$, ohne die Länge zu
  ändern. Der Faktor $e^{j\alpha}$ ist also ein reiner **Dreh-Operator**.

Dieser letzte Punkt ist der Grund, warum die ganze Wechselstrom- und Signaltechnik komplex rechnet: Eine
Schwingung ist ein Pfeil, der sich mit der Zeit dreht — und Drehen ist in der komplexen Ebene einfach
Multiplizieren mit $e^{j\alpha}$.

:::grafik
Zwei Zeiger $z_1$ und $z_2$ und ihr Produkt: Die Länge des Produkts ist das Produkt der Längen, der Winkel die
Summe der Winkel ($\alpha_1 + \alpha_2$). Daneben separat die reine Drehung: ein Zeiger und sein mit
$e^{j\alpha}$ multipliziertes, um $\alpha$ gedrehtes Abbild gleicher Länge.
:::

## Zweite Sichtweise: $j$ ist eine Drehung um 90°

Mit der geometrischen Deutung lässt sich jetzt sogar die Ausgangsregel $j^2 = -1$ noch einmal völlig neu
verstehen — nicht als willkürliche Festlegung, sondern als zwangsläufige Folge. Die Zahl $j$ hat den Realteil
$0$ und den Imaginärteil $1$, liegt also als Pfeil der Länge $1$ genau auf der imaginären Achse, unter dem Winkel
$90^\circ$. In Exponentialform ist sie

$$j = e^{\,j\pi/2}.$$

Nach dem gerade Gelernten bedeutet **Multiplizieren mit $j$** daher eine **Drehung um $90^\circ$** (bei Länge
$1$, also ohne Streckung). Und nun der Clou: $j^2$ heißt „zweimal mit $j$ multiplizieren", also **zweimal um
$90^\circ$ drehen** — zusammen $180^\circ$. Ein Pfeil, der bei $+1$ startet und um $180^\circ$ gedreht wird,
zeigt auf $-1$. Also ist $j^2 = -1$ — nicht per Dekret, sondern weil zweimal 90° genau eine Halbdrehung ist. Die
Potenzen von $j$ laufen entsprechend in 90°-Schritten im Kreis: $j^0 = 1$ (0°), $j^1 = j$ (90°), $j^2 = -1$
(180°), $j^3 = -j$ (270°), $j^4 = 1$ (360°, wieder am Start).

Das ist genau die Art von Einsicht, die Vertrauen schafft: Die zunächst mysteriöse Regel „$j^2 = -1$" ist in
Wahrheit nur die Aussage, dass eine Vierteldrehung, zweimal ausgeführt, eine Halbdrehung ergibt.

:::grafik
Animation: Ein Pfeil startet bei $+1$ auf der reellen Achse. Schrittweise wird mit $j$ multipliziert, und der
Pfeil springt jeweils um $90^\circ$ weiter: $1 \to j \to -1 \to -j \to 1$. Die vier Positionen auf dem
Einheitskreis sind beschriftet; hervorgehoben, dass die zwei Schritte von $1$ nach $-1$ zusammen eine
$180^\circ$-Drehung sind — die anschauliche Bedeutung von $j^2 = -1$.
:::

:::kern
Die reellen Zahlen können $z^2 = -1$ nicht lösen (jedes reelle Quadrat ist $\ge 0$); man erweitert sie um die
__imaginäre Einheit__ $j=\sqrt{-1}$ mit $j^2 = -1$ (in der ET $j$ statt $i$). Eine __komplexe Zahl__ $z = x + jy$
hat __Realteil__ $x=\operatorname{Re}\{z\}$ und __Imaginärteil__ $y=\operatorname{Im}\{z\}$ und ist ein
Punkt/Pfeil in der __Gaußschen Zahlenebene__. Addition läuft komponentenweise, Multiplikation über
Ausmultiplizieren mit $j^2=-1$. In der __Polarform__ beschreibt man den Pfeil durch __Betrag__
$r = |z| = \sqrt{x^2+y^2}$ (Pythagoras) und __Argument__ $\alpha$ (Winkelfunktionen), also
$z = r(\cos\alpha + j\sin\alpha)$; $\arg(z)$ ist nur bis auf $2\pi$ eindeutig, Hauptwert $-\pi<\alpha\le\pi$. Die
über die Reihenentwicklung bewiesene __Eulersche Formel__ $e^{j\alpha} = \cos\alpha + j\sin\alpha$ führt auf die
__Exponentialform__ $z = r\,e^{j\alpha}$. Ihr entscheidender Vorteil: Multiplizieren = __Beträge mal, Winkel
plus__ (weil Exponenten sich addieren), also geometrisch __Strecken und Drehen__ — und $e^{j\alpha}$ ist eine
reine Drehung.
:::

Ein Zeiger, der sich mit der Zeit dreht — das ist der Schritt von der ruhenden komplexen Zahl zur
**Schwingung**. Damit beschreibt man Sinussignale als rotierende Zeiger (__Phasoren__), das Thema des nächsten
Abschnitts.
