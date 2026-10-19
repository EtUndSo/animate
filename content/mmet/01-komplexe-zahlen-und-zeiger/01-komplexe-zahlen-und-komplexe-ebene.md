---
title: Komplexe Zahlen und die komplexe Ebene
pfad: Elektrotechnik / 1. Semester / Mathematische Methoden der Elektrotechnik / Komplexe Zahlen und Zeiger
order: 10100
summary: Von Grund auf erklärt – warum die reellen Zahlen nicht ausreichen, wie man sie um die imaginäre Einheit erweitert, wie man mit komplexen Zahlen rechnet und warum die Exponentialform aus mühsamer Rechnung eine einfache Drehung macht. Jede Formel wird hergeleitet.
tags: komplexe Zahlen, imaginäre Einheit, komplexe Ebene, Betrag, Phase, Polarform, Eulersche Formel, Multiplikation
---

:::grafik
Einstiegs-Animation: Die komplexe Ebene mit reeller Achse (waagerecht) und imaginärer Achse (senkrecht). Eine
komplexe Zahl erscheint zunächst als Punkt $(a,b)$ und wird zum Pfeil vom Ursprung ($z = a + jb$), mit den
gestrichelten Projektionen $a$ und $b$. Dann der Ausblick auf den Kern des Artikels: Der Pfeil wird mit einer
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

$$x^2 = -1.$$

Gibt es eine reelle Zahl $x$, die sie löst? Nein — und man kann genau sagen, warum. Quadriert man irgendeine
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

$$j^2 = -1.$$

Ein Wort zur Schreibweise: In der Mathematik heißt diese Einheit $i$. In der Elektrotechnik ist $i$ aber schon
für den **Strom** vergeben, deshalb schreibt man sie dort $j$. Wir benutzen durchgehend $j$.

Der Name „imaginär" (eingebildet) ist historisch und etwas unglücklich — er suggeriert, diese Zahlen seien
weniger real als die gewohnten. Das sind sie nicht. $j$ ist einfach eine Zahl in einer **neuen Richtung**, die
senkrecht zu den vertrauten Zahlen zeigt; gleich, wenn wir sie in die Ebene zeichnen, wird das ganz anschaulich.

## Komplexe Zahlen und das Rechnen mit ihnen

Mit $j$ in der Hand kann man nun Zahlen bauen, die einen gewöhnlichen und einen „neuen" Anteil haben. Eine
__komplexe Zahl__ hat die Form

$$z = a + j\,b.$$

- __$z$__: die __komplexe Zahl__.
- __$a = \operatorname{Re}(z)$__: der __Realteil__ — eine ganz gewöhnliche reelle Zahl.
- __$b = \operatorname{Im}(z)$__: der __Imaginärteil__ — ebenfalls eine reelle Zahl, nämlich der Faktor **nach**
  dem $j$ (also $b$ selbst, **nicht** $jb$).

Gerechnet wird mit solchen Ausdrücken wie mit gewohnten Klammern — mit der **einen** zusätzlichen Regel, dass
überall $j^2$ durch $-1$ ersetzt wird. Sehen wir uns die beiden Grundrechenarten an, denn gerade hier zeigt
sich später der ganze Vorteil der komplexen Zahlen.

**Addition** ist langweilig einfach: Man addiert Real- und Imaginärteile getrennt,

$$z_1 + z_2 = (a_1 + j b_1) + (a_2 + j b_2) = (a_1 + a_2) + j\,(b_1 + b_2).$$

**Multiplikation** ist der interessante Fall. Man multipliziert die Klammern wie gewohnt aus (jedes Glied mit
jedem) und ersetzt am Ende $j^2$ durch $-1$. Schritt für Schritt:

$$z_1 \cdot z_2 = (a_1 + j b_1)(a_2 + j b_2) = a_1 a_2 + a_1\,j b_2 + j b_1\,a_2 + j b_1\,j b_2.$$

Im letzten Summanden steckt $j\cdot j = j^2 = -1$, also $j b_1\,j b_2 = j^2 b_1 b_2 = -\,b_1 b_2$. Sortiert man
nach reellem und imaginärem Anteil, bleibt

$$z_1 \cdot z_2 = (a_1 a_2 - b_1 b_2) + j\,(a_1 b_2 + a_2 b_1).$$

Das ist korrekt, aber unübersichtlich: vier Produkte, ein Vorzeichenwechsel, getrenntes Sortieren. Und schlimmer
— wenn man eigentlich wissen will, *wie lang* das Ergebnis ist und *in welche Richtung* es zeigt, muss man aus
diesem Ausdruck erst wieder Betrag und Winkel ausrechnen. Merke dir dieses mühsame Ergebnis; wir kommen darauf
zurück und zeigen, dass es mit der Exponentialform in einer Zeile und mit klarer Bedeutung geht.

## Die komplexe Ebene

Eine komplexe Zahl besteht aus **zwei** unabhängigen reellen Zahlen, $a$ und $b$. Alles, was durch zwei Zahlen
festgelegt ist, lässt sich als Punkt in einer **Ebene** zeichnen — und genau das ist die große Idee hinter der
__komplexen Ebene__ (auch Gaußsche Ebene). Die waagerechte Achse trägt den Realteil, die senkrechte den
Imaginärteil. Die Zahl $z = a + jb$ ist dann der Punkt mit den Koordinaten $(a, b)$.

Noch nützlicher ist es, $z$ als **Pfeil** vom Ursprung zu diesem Punkt zu sehen. In diesem Bild wird vieles
sofort anschaulich:

- Die **Addition** zweier komplexer Zahlen ist das Aneinanderhängen der Pfeile (Spitze an Fuß), genau wie bei
  Kräften oder Vektoren — das passt zur komponentenweisen Addition von oben.
- Die __konjugiert komplexe Zahl__ $z^* = a - j b$ (gleicher Realteil, Imaginärteil mit umgekehrtem Vorzeichen)
  ist der an der reellen Achse **gespiegelte** Pfeil. Sie ist nützlich, weil ihr Produkt mit $z$ rein reell
  wird: $z\cdot z^* = (a+jb)(a-jb) = a^2 - (jb)^2 = a^2 + b^2$ (hier hebt sich der imaginäre Anteil auf). Das ist
  genau das Quadrat der Pfeillänge — gleich mehr dazu.

Jetzt wird auch klar, warum „imaginär" kein Makel ist: Der imaginäre Anteil ist einfach die **zweite
Koordinate**, die Höhe über der reellen Achse.

:::grafik
Die komplexe Ebene mit reeller Achse (waagerecht) und imaginärer Achse (senkrecht). Eine Zahl $z = a + jb$ als
Punkt $(a,b)$ und als Pfeil vom Ursprung; gestrichelt die Projektionen auf beide Achsen ($a$ waagerecht, $b$
senkrecht). Zusätzlich die an der reellen Achse gespiegelte konjugierte Zahl $z^*$.
:::

## Betrag und Phase: die Polarform

Einen Pfeil kann man auf zwei Arten festlegen. Bisher haben wir ihn über seine **Koordinaten** $a$ und $b$
beschrieben. Genauso gut geht es über seine **Länge** und seinen **Winkel** — und diese zweite Beschreibung ist
die __Polarform__. Beide enthalten dieselbe Information, nur anders verpackt; wir leiten den Zusammenhang her.

Zeichnet man den Pfeil $z = a + jb$ mitsamt seinen Projektionen, entsteht ein **rechtwinkliges Dreieck**: Die
waagerechte Kathete hat die Länge $a$, die senkrechte die Länge $b$, und der Pfeil selbst ist die Hypotenuse.
Nach dem **Satz des Pythagoras** ist das Quadrat der Hypotenuse die Summe der Kathetenquadrate — die Länge des
Pfeils, der __Betrag__ $|z|$, ist also

$$|z| = \sqrt{a^2 + b^2}.$$

Den Winkel bekommt man aus den Winkelfunktionen desselben Dreiecks. Der __Phasenwinkel__ (oder kurz die
__Phase__) $\varphi$ ist der Winkel des Pfeils gegen die positive reelle Achse. Im rechtwinkligen Dreieck gilt
„Ankathete = Hypotenuse mal Kosinus" und „Gegenkathete = Hypotenuse mal Sinus", also

$$a = |z|\cos\varphi, \qquad b = |z|\sin\varphi.$$

Setzt man das in $z = a + jb$ ein und klammert $|z|$ aus, erhält man die Polarform:

$$z = a + jb = |z|\cos\varphi + j\,|z|\sin\varphi = |z|\,(\cos\varphi + j\sin\varphi).$$

- __$|z|$__: der __Betrag__ — die Länge des Pfeils (immer $\ge 0$).
- __$\varphi$__: die __Phase__ — der Winkel gegen die positive reelle Achse.

**Stolperstein: die Phase richtig bestimmen.** Umgekehrt (von $a, b$ zum Winkel) ist man versucht, einfach
$\varphi = \arctan(b/a)$ zu rechnen. Das ist eine häufige Fehlerquelle: Der Arkustangens liefert nur Winkel
zwischen $-\tfrac{\pi}{2}$ und $+\tfrac{\pi}{2}$, also nur die **rechte** Halbebene. Liegt $z$ links (negativer
Realteil $a<0$), zeigt der Pfeil in Wirklichkeit in die andere Richtung, und man muss $\pi$ (also $180^\circ$)
addieren. Der Grund ist, dass $\arctan$ aus dem Verhältnis $b/a$ das Vorzeichen von Zähler und Nenner nicht
mehr einzeln sehen kann — $\tfrac{b}{a}$ und $\tfrac{-b}{-a}$ sind gleich, obwohl die Pfeile entgegengesetzt
zeigen. Sicher ist, den **Quadranten** aus den Vorzeichen von $a$ und $b$ mitzudenken; die Funktion
$\operatorname{atan2}(b,a)$ nimmt einem genau das ab.

:::grafik
Derselbe Pfeil $z$ in der komplexen Ebene, nun als Hypotenuse eines rechtwinkligen Dreiecks: waagerechte Kathete
$a$, senkrechte Kathete $b$, Hypotenuse $|z| = \sqrt{a^2+b^2}$, dazu der eingezeichnete Winkel $\varphi$ als
Bogen zur reellen Achse. Beschriftet die Beziehungen $a = |z|\cos\varphi$ und $b = |z|\sin\varphi$.
:::

## Die Eulersche Formel – woher sie kommt

Bisher ist $(\cos\varphi + j\sin\varphi)$ nur eine Abkürzung für „Pfeil der Länge 1 unter dem Winkel
$\varphi$". Die __Eulersche Formel__ behauptet nun etwas Erstaunliches — dass dieser Ausdruck **genau** eine
Exponentialfunktion ist:

$$e^{\,j\varphi} = \cos\varphi + j\sin\varphi.$$

Das darf man nicht einfach glauben, man kann es herleiten. Das sauberste Argument nutzt die
**Reihenentwicklungen** (Taylor-Reihen), mit denen man $e^x$, $\cos$ und $\sin$ als unendliche Summen schreibt:

$$e^{x} = 1 + x + \frac{x^2}{2!} + \frac{x^3}{3!} + \frac{x^4}{4!} + \ldots$$

Diese Reihe gilt für jede Zahl, die man einsetzen darf — auch für die imaginäre Zahl $x = j\varphi$. Setzen wir
sie ein und nutzen die Potenzen von $j$ (die sich im Viererzyklus wiederholen: $j^1 = j$, $j^2 = -1$, $j^3 =
-j$, $j^4 = +1$, dann von vorn):

$$e^{\,j\varphi} = 1 + j\varphi + \frac{(j\varphi)^2}{2!} + \frac{(j\varphi)^3}{3!} + \frac{(j\varphi)^4}{4!} + \ldots
= 1 + j\varphi - \frac{\varphi^2}{2!} - j\frac{\varphi^3}{3!} + \frac{\varphi^4}{4!} + \ldots$$

Jetzt sortiert man die Summanden danach, ob sie ein $j$ enthalten oder nicht — also in einen **reellen** und
einen **imaginären** Teil:

$$e^{\,j\varphi} = \underbrace{\left(1 - \frac{\varphi^2}{2!} + \frac{\varphi^4}{4!} - \ldots\right)}_{=\,\cos\varphi} + \; j\underbrace{\left(\varphi - \frac{\varphi^3}{3!} + \frac{\varphi^5}{5!} - \ldots\right)}_{=\,\sin\varphi}.$$

Die beiden geklammerten Reihen sind aber genau die bekannten Reihenentwicklungen von $\cos\varphi$ und
$\sin\varphi$. Damit ist $e^{j\varphi} = \cos\varphi + j\sin\varphi$ — nicht per Definition, sondern **bewiesen**.

Setzt man diese Formel in die Polarform ein, bekommt die Darstellung ihre endgültige, kompakteste Gestalt, die
__Exponentialform__:

$$z = |z|\,(\cos\varphi + j\sin\varphi) = |z|\,e^{\,j\varphi}.$$

- __$|z|$__: der __Betrag__ (Länge des Pfeils).
- __$e^{\,j\varphi}$__: der __Einheitszeiger__ — ein Pfeil der Länge 1 unter dem Winkel $\varphi$. Multiplizieren
  mit $|z|$ streckt ihn auf die richtige Länge.

:::grafik
Der Einheitskreis in der komplexen Ebene; auf ihm der Punkt $e^{j\varphi}$ unter dem Winkel $\varphi$, mit den
Projektionen $\cos\varphi$ (auf die reelle Achse) und $\sin\varphi$ (auf die imaginäre Achse). Das illustriert
$e^{j\varphi} = \cos\varphi + j\sin\varphi$: Realteil ist der Kosinus, Imaginärteil der Sinus.
:::

## Der Lohn: Multiplikation als Drehen und Strecken

Jetzt zahlt sich die ganze Vorarbeit aus. Erinnern wir uns an das mühsame kartesische Ergebnis von oben:

$$z_1 \cdot z_2 = (a_1 a_2 - b_1 b_2) + j\,(a_1 b_2 + a_2 b_1).$$

Dasselbe Produkt in der Exponentialform. Wir schreiben beide Zahlen als $z_1 = |z_1|e^{j\varphi_1}$ und
$z_2 = |z_2|e^{j\varphi_2}$ und multiplizieren — wobei wir nur das Potenzgesetz $e^{x}\cdot e^{y} = e^{x+y}$
brauchen, das auch für imaginäre Exponenten gilt:

$$z_1 \cdot z_2 = |z_1|e^{\,j\varphi_1}\cdot |z_2|e^{\,j\varphi_2} = |z_1|\,|z_2|\;e^{\,j\varphi_1}e^{\,j\varphi_2} = |z_1|\,|z_2|\;e^{\,j(\varphi_1 + \varphi_2)}.$$

In Worten: **Die Beträge multiplizieren sich, die Winkel addieren sich.** Und das ist nicht nur kürzer — es ist
auch sofort *bedeutungsvoll*: Man sieht direkt, wie lang ($|z_1||z_2|$) und wie gedreht ($\varphi_1 + \varphi_2$)
das Ergebnis ist. Das kartesische Ergebnis enthält zwar dieselbe Zahl, verbirgt aber Länge und Winkel in einer
Mischung aus vier Produkten.

Und man sieht auch **warum** sich die Winkel addieren: weil sie als **Exponenten** auftreten und sich Exponenten
beim Multiplizieren addieren. Genau hier steckt der tiefere Grund, überhaupt zur Exponentialform überzugehen.

**Die geometrische Deutung.** Multiplizieren mit einer komplexen Zahl heißt also: **strecken** (um deren Betrag)
und **drehen** (um deren Winkel). Zwei Spezialfälle machen das greifbar:

- Multiplizieren mit einer **reellen** Zahl $r>0$ (Winkel $0$) streckt nur — kein Drehen. Das ist die vertraute
  Skalierung.
- Multiplizieren mit $e^{\,j\varphi}$ (Betrag $1$) **dreht nur** um den Winkel $\varphi$, ohne die Länge zu
  ändern. Der Faktor $e^{j\varphi}$ ist also ein reiner **Dreh-Operator**.

Dieser letzte Punkt ist der Grund, warum die ganze Wechselstrom- und Signaltechnik komplex rechnet: Eine
Schwingung ist ein Pfeil, der sich mit der Zeit dreht — und Drehen ist in der komplexen Ebene einfach
Multiplizieren mit $e^{j\varphi}$.

:::grafik
Zwei Zeiger $z_1$ und $z_2$ und ihr Produkt: Die Länge des Produkts ist das Produkt der Längen, der Winkel die
Summe der Winkel ($\varphi_1 + \varphi_2$). Daneben separat die reine Drehung: ein Zeiger und sein mit
$e^{j\varphi}$ multipliziertes, um $\varphi$ gedrehtes Abbild gleicher Länge.
:::

:::kern
Die reellen Zahlen können $x^2 = -1$ nicht lösen (jedes reelle Quadrat ist $\ge 0$); man erweitert sie um die
__imaginäre Einheit__ $j$ mit $j^2 = -1$ (in der ET $j$ statt $i$). Eine __komplexe Zahl__ $z = a + jb$ hat
__Realteil__ $a$ und __Imaginärteil__ $b$ und ist ein Punkt/Pfeil in der __komplexen Ebene__. Addition läuft
komponentenweise, Multiplikation über Ausmultiplizieren mit $j^2=-1$. In der __Polarform__ beschreibt man den
Pfeil durch __Betrag__ $|z| = \sqrt{a^2+b^2}$ (Pythagoras) und __Phase__ $\varphi$ (Winkelfunktionen), also
$z = |z|(\cos\varphi + j\sin\varphi)$. Die über die Reihenentwicklung bewiesene __Eulersche Formel__
$e^{j\varphi} = \cos\varphi + j\sin\varphi$ führt auf die __Exponentialform__ $z = |z|e^{j\varphi}$. Ihr
entscheidender Vorteil: Multiplizieren = __Beträge mal, Winkel plus__ (weil Exponenten sich addieren), also
geometrisch __Strecken und Drehen__ — und $e^{j\varphi}$ ist eine reine Drehung.
:::

Ein Zeiger, der sich mit der Zeit dreht — das ist der Schritt von der ruhenden komplexen Zahl zur
**Schwingung**. Damit beschreibt man Sinussignale als rotierende Zeiger (__Phasoren__), das Thema des nächsten
Abschnitts.
