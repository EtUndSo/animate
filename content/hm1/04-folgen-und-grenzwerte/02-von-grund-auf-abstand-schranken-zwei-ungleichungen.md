---
title: Von Grund auf: Abstand, Schranken, zwei Ungleichungen
pfad: Elektrotechnik / 1. Semester / HöMa1 – Höhere Mathematik 1 / Folgen und Grenzwerte
adresse: elektrotechnik/1-semester/hohere-mathematik-1/folgen-und-grenzwerte
knoten: Kapitel 4: Folgen und Grenzwerte
order: 1240200
summary: Was „beliebig nah“ heißt und warum die reellen Zahlen keine Lücke haben dürfen
tags: Abstand, Abstandsregel, Supremum, Infimum, Vollständigkeitsaxiom
lang: de
---

Es gilt $\mathbb{N}=\{1,2,3,\dots\}$ und $\mathbb{N}_0=\mathbb{N}\cup\{0\}$. Das Zeichen $\forall$ heißt „für alle“, $\exists$ heißt „es gibt“ ([Kapitel 1](/wissen/elektrotechnik/1-semester/hohere-mathematik-1/mengen-logik-und-reelle-zahlen/mengen-logik-und-reelle-zahlen.html)). Aus [Kapitel 1](/wissen/elektrotechnik/1-semester/hohere-mathematik-1/mengen-logik-und-reelle-zahlen/mengen-logik-und-reelle-zahlen.html) werden vier Werkzeuge gebraucht.

⁠**Betrag als Abstand.** $|x|$ ist $x$ für $x\ge0$ und $-x$ für $x<0$. Die Zahl $|x-y|$ ist der __Abstand__ von $x$ und $y$ auf der Zahlengeraden. Addiert man $a$ zu $-\varepsilon<x-a<\varepsilon$, folgt die __Abstandsregel__

$$|x-a|<\varepsilon\quad\iff\quad a-\varepsilon<x<a+\varepsilon.$$

Die Zahl $x$ liegt dann im offenen Intervall $(a-\varepsilon,a+\varepsilon)$, zwischen den beiden Grenzen, aber nicht auf ihnen.

⁠**Dreiecksungleichung.** $|x+y|\le|x|+|y|$. Für Abstände heißt das: Ein Umweg über $z$ ist nie kürzer, $|x-y|\le|x-z|+|z-y|$. Die untere Form lautet $\bigl||x|-|y|\bigr|\le|x-y|$.

⁠**Schranken.** Das __Supremum__ $\sup M$ ist die kleinste obere Schranke einer Menge $M$, das __Infimum__ $\inf M$ die größte untere. Das __Vollständigkeitsaxiom__ fordert: Jede nach unten beschränkte, nicht leere Teilmenge von $\mathbb{R}$ hat ein Infimum in $\mathbb{R}$, entsprechend hat jede nach oben beschränkte ein Supremum. Ist $y<\sup M$, gibt es ein $x\in M$ mit $y<x\le\sup M$, sonst wäre $y$ eine kleinere obere Schranke.

⁠**Bernoulli-Ungleichung.** $(1+x)^n\ge1+nx$ für $x>-1$ und $n\in\mathbb{N}$; für $n\ge2$ und $x\ne0$ gilt sogar $>$.

::::formelsammlung
**Natürliche Zahlen**

$$\mathbb{N}=\{1,2,3,\dots\},\qquad\mathbb{N}_0=\mathbb{N}\cup\{0\}$$

$\forall$ heißt „für alle“, $\exists$ heißt „es gibt“.

**Abstand**

$$|x-y|$$

Der Abstand von $x$ und $y$ auf der Zahlengeraden; dabei ist $|x|$ gleich $x$ für $x\ge0$ und $-x$ für $x<0$.

**Abstandsregel**

$$|x-a|<\varepsilon\quad\iff\quad a-\varepsilon<x<a+\varepsilon$$

$x$ liegt im offenen Intervall $(a-\varepsilon,a+\varepsilon)$, zwischen den beiden Grenzen, aber nicht auf ihnen.

**Dreiecksungleichung**

$$|x+y|\le|x|+|y|,\qquad|x-y|\le|x-z|+|z-y|$$

Für Abstände: Ein Umweg über $z$ ist nie kürzer.

**Untere Dreiecksungleichung**

$$\bigl||x|-|y|\bigr|\le|x-y|$$

Schätzt einen Abstand nach unten ab.

**Elemente dicht unter dem Supremum**

$$y<\sup M\ \Longrightarrow\ \text{es gibt }x\in M\text{ mit }y<x\le\sup M$$

$\sup M$ ist die kleinste obere Schranke, $\inf M$ die größte untere. Vollständigkeitsaxiom: Jede nach unten beschränkte, nicht leere Teilmenge von $\mathbb{R}$ hat ein Infimum in $\mathbb{R}$, jede nach oben beschränkte ein Supremum.

**Bernoulli-Ungleichung**

$$(1+x)^n\ge1+nx$$

Für $x>-1$ und $n\in\mathbb{N}$; für $n\ge2$ und $x\ne0$ gilt sogar $>$.
::::

::::lernkarten
:::karte formel Abstandsregel
Welche Ungleichungskette ist nach der Abstandsregel gleichwertig mit $|x-a|<\varepsilon$, und wo liegt $x$ dann auf der Zahlengeraden?
---
$|x-a|<\varepsilon\iff a-\varepsilon<x<a+\varepsilon$. Die Zahl $x$ liegt dann im offenen Intervall $(a-\varepsilon,a+\varepsilon)$: zwischen den beiden Grenzen, aber nicht auf ihnen.
--- falsch
$|x-a|<\varepsilon\iff a-\varepsilon\le x\le a+\varepsilon$. Die Zahl $x$ liegt dann im abgeschlossenen Intervall $[a-\varepsilon,a+\varepsilon]$, die beiden Grenzen sind also eingeschlossen.
--- falsch
$|x-a|<\varepsilon\iff x<a+\varepsilon$. Die Zahl $x$ liegt dann links der Grenze $a+\varepsilon$; eine untere Grenze gibt es nicht, weil ein Betrag nie negativ ist.
--- falsch
Die Kette $a-\varepsilon<x<a+\varepsilon$ gilt nur für $x\ge a$. Für $x<a$ ist der Betrag $a-x$, und dann liegt $x$ im Intervall $(a,a+\varepsilon)$ rechts von $a$.
:::
:::karte zusammenhang Abstand
Wie folgt aus dem Abstand $|x-a|<\varepsilon$ die Ungleichungskette $a-\varepsilon<x<a+\varepsilon$?
---
$|x-a|<\varepsilon$ heißt $-\varepsilon<x-a<\varepsilon$, weil $|x-a|$ die größere der Zahlen $x-a$ und $-(x-a)$ ist und beide kleiner als $\varepsilon$ sein müssen. Addiert man $a$ auf allen drei Seiten, folgt die Kette.
--- falsch
Man lässt den Betrag weg: Aus $|x-a|<\varepsilon$ wird $x-a<\varepsilon$, also $x<a+\varepsilon$. Die linke Grenze $a-\varepsilon$ kommt hinzu, weil Abstände nie negativ sind und $x$ deshalb nicht beliebig klein sein kann.
--- falsch
$|x-a|<\varepsilon$ heißt $0<x-a<\varepsilon$, weil ein Betrag nie negativ ist. Addiert man $a$, folgt $a<x<a+\varepsilon$; die Kette mit $a-\varepsilon$ ist nur eine bequeme, etwas großzügigere Schreibweise davon.
--- falsch
$|x-a|<\varepsilon$ heißt $-\varepsilon<x-a<\varepsilon$. Multipliziert man alle drei Seiten mit $a$, folgt die Kette $a-\varepsilon<x<a+\varepsilon$, denn die Multiplikation mit einer Zahl erhält jede Ungleichung.
:::
:::karte formel Dreiecksungleichung
Welche drei Formen der Dreiecksungleichung stehen als Werkzeug bereit: für Beträge, für Abstände und als untere Form?
---
$|x+y|\le|x|+|y|$; für Abstände $|x-y|\le|x-z|+|z-y|$, ein Umweg über $z$ ist also nie kürzer; die untere Form lautet $\bigl||x|-|y|\bigr|\le|x-y|$.
--- falsch
$|x+y|\ge|x|+|y|$; für Abstände $|x-y|\ge|x-z|+|z-y|$, der direkte Weg ist also nie kürzer als ein Umweg; die untere Form lautet $\bigl||x|-|y|\bigr|\ge|x-y|$.
--- falsch
$|x+y|=|x|+|y|$; für Abstände $|x-y|=|x-z|+|z-y|$ für jedes $z$, Teilstrecken addieren sich also immer; die untere Form lautet $\bigl||x|-|y|\bigr|=|x-y|$.
--- falsch
$|x+y|\le|x|+|y|$; für Abstände $|x-y|\le|x-z|\cdot|z-y|$, die beiden Teilstrecken multiplizieren sich also; die untere Form lautet $|x|-|y|\ge|x-y|$.
:::
:::karte zusammenhang Supremum
Warum gibt es zu jeder Zahl $y<\sup M$ ein Element $x\in M$ mit $y<x\le\sup M$?
---
Weil $\sup M$ die kleinste obere Schranke ist: Gäbe es kein solches $x$, wären alle Elemente von $M$ höchstens $y$. Dann wäre $y$ eine kleinere obere Schranke als $\sup M$.
--- falsch
Weil das Supremum immer zur Menge gehört: Man nimmt einfach $x=\sup M$ selbst. Ein Element echt zwischen $y$ und $\sup M$ muss es dagegen nicht geben.
--- falsch
Weil zwischen zwei verschiedenen reellen Zahlen immer eine weitere liegt, etwa der Mittelwert $\frac12(y+\sup M)$; dieser liegt deshalb in $M$ und erfüllt die Bedingung.
--- falsch
Weil $y$ dann eine untere Schranke von $M$ ist und das Vollständigkeitsaxiom zu jeder unteren Schranke ein Element von $M$ liefert, das dicht darüber liegt.
:::
:::karte zusammenhang Vollständigkeitsaxiom und Infimum
Welche Teilmengen von $\mathbb{R}$ besitzen nach dem Vollständigkeitsaxiom ein Infimum, und was gilt entsprechend für das Supremum?
---
Jede nach unten beschränkte, nicht leere Teilmenge von $\mathbb{R}$ hat ein Infimum in $\mathbb{R}$, also eine größte untere Schranke. Entsprechend hat jede nach oben beschränkte, nicht leere Teilmenge ein Supremum in $\mathbb{R}$.
--- falsch
Jede nicht leere Teilmenge von $\mathbb{R}$ hat ein Infimum in $\mathbb{R}$, auch ohne Schranke, weil die Zahlengerade keine Lücken hat. Entsprechend hat jede nicht leere Teilmenge von $\mathbb{R}$ ein Supremum in $\mathbb{R}$.
--- falsch
Jede nach unten beschränkte, nicht leere Teilmenge von $\mathbb{R}$ hat ein kleinstes Element, ihr Infimum. Entsprechend hat jede nach oben beschränkte, nicht leere Teilmenge ein größtes Element, ihr Supremum.
--- falsch
Jede nach unten beschränkte, nicht leere Teilmenge von $\mathbb{Q}$ hat ein Infimum in $\mathbb{Q}$; das Axiom gilt also schon für Brüche. Entsprechend hat jede nach oben beschränkte, nicht leere Teilmenge ein Supremum in $\mathbb{Q}$.
:::
:::karte formel Bernoulli-Ungleichung
Wie lautet die Bernoulli-Ungleichung, und unter welchen Voraussetzungen gilt sie sogar mit echtem Größerzeichen?
---
$(1+x)^n\ge1+nx$ für $x>-1$ und $n\in\mathbb{N}$. Für $n\ge2$ und $x\ne0$ gilt sogar $(1+x)^n>1+nx$.
--- falsch
$(1+x)^n\ge1+nx$ für alle $x\in\mathbb{R}$ und $n\in\mathbb{N}$. Für $x>0$ gilt sogar $(1+x)^n>1+nx$, für $x<0$ dagegen $\le$.
--- falsch
$(1+x)^n\le1+nx$ für $x>-1$ und $n\in\mathbb{N}$. Für $n\ge2$ und $x\ne0$ gilt sogar $(1+x)^n<1+nx$.
--- falsch
$(1+x)^n\ge1+x^n$ für $x>-1$ und $n\in\mathbb{N}$. Für $n\ge2$ und $x\ne0$ gilt sogar $(1+x)^n>1+x^n$.
:::
::::
