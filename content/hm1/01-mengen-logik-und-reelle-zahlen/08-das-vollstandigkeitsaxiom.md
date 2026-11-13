---
title: Stufe 6: Das Vollständigkeitsaxiom
pfad: Elektrotechnik / 1. Semester / HöMa1 – Höhere Mathematik 1 / Mengen, Logik und reelle Zahlen
adresse: elektrotechnik/1-semester/hohere-mathematik-1/mengen-logik-und-reelle-zahlen
knoten: Kapitel 1: Mengen, Logik und reelle Zahlen
order: 1210800
summary: mathbb Q erfüllt alle bisherigen Axiome.
tags: nach oben beschränkt, obere Schranke, nach unten beschränkt, untere Schranke, beschränkt, Supremum, Infimum, Maximum
lang: de
---

<span class="anker" id="stufe-6"></span>

:::zweck
$\mathbb{Q}$ erfüllt alle bisherigen Axiome. Trotzdem fehlt etwas: Die Zahl, deren Quadrat 2 ist. Diese Stufe zeigt das und nennt das Axiom, das $\mathbb{R}$ von $\mathbb{Q}$ trennt.
:::

**Die Idee.** $\mathbb{N}$ und $\mathbb{Z}$ haben sichtbare Lücken. $\mathbb{Q}$ liegt scheinbar lückenlos: Zwischen zwei Brüchen $p/q<u/v$ liegt immer ein weiterer, $\frac12(p/q+u/v)=p/q+\frac12(u/v-p/q)$. Trotzdem gibt es Stellen, die kein Bruch trifft (Abb. [6](#abb-6)). Vollständigkeit heißt: Jede solche Grenze ist eine Zahl.

:::satz Satz 6.1 (Die Wurzel aus 2 ist kein Bruch)
<span class="anker" id="satz-6-1"></span>

Es gibt kein $r\in\mathbb{Q}$ mit $r^2=2$.
:::

:::beweis Indirekt
Annahme: $r=\frac pq$ mit $p,q\in\mathbb{N}$ (das Vorzeichen spielt keine Rolle), so weit gekürzt, dass $p$ und $q$ nicht beide gerade sind. Aus $r^2=2$ folgt $p^2=2q^2$, also ist $p^2$ gerade. Nach der Kontraposition aus Stufe [1](mengen-und-aussagen.html#stufe-1) ist $p$ gerade, $p=2k$. Einsetzen: $4k^2=2q^2$, also $q^2=2k^2$, und ebenso ist $q$ gerade. Dann sind $p$ und $q$ beide gerade, im Widerspruch zum Kürzen.
:::

⁠**So liest man das:** $r^2=2$ ist also in $\mathbb{Q}$ nicht lösbar. Für $r^2=4$ scheitert der Beweis, wie es sein muss (Aufgabe [8](intervallschachtelung-und-wurzeln.html#aufg-8)).

:::abbildung hm1/k1luecke 6
Die Brüche aus $D$ und die Brüche mit $x^2>2$ liegen beliebig dicht beieinander, zum Beispiel 1,414 und 1,415. Die Stelle dazwischen ist kein Bruch.
:::

:::definition Definition 6.2 (Schranke, Supremum, Infimum)
<span class="anker" id="satz-6-2"></span>

Sei $\mathbb K$ total angeordnet und $M\subset\mathbb K$.

<ol class="rm">

<li>

$M$ heißt __nach oben beschränkt__, wenn es $S\in\mathbb K$ gibt mit $x\le S$ für alle $x\in M$. Jedes solche $S$ heißt __obere Schranke__. Entsprechend __nach unten beschränkt__ und __untere Schranke__ mit $R\le x$. Beides zusammen heißt __beschränkt__.

</li>

<li>

$S$ heißt __Supremum__ von $M$, $S=\sup M$, wenn $S$ eine obere Schranke ist und für jede obere Schranke $\tilde S$ gilt $S\le\tilde S$ (kleinste obere Schranke).

</li>

<li>

$R$ heißt __Infimum__ von $M$, $R=\inf M$, wenn $R$ eine untere Schranke ist und für jede untere Schranke $\tilde R$ gilt $\tilde R\le R$ (größte untere Schranke).

</li>

<li>

Liegt $S$ in $M$, heißt es __Maximum__ ($\max M$), liegt $R$ in $M$, heißt es __Minimum__ ($\min M$).

</li>

</ol>
:::

⁠**So liest man das:** Schranken stehen außen und sind nicht eindeutig: $\{2,3,5,7\}$ hat die obere Schranke 7, aber auch 100. Hier ist $\sup=\max=7$, $\inf=\min=2$. $\mathbb{N}$ hat die untere Schranke 1 und keine obere (Satz [6.5](#satz-6-5)).

:::frage Ist das Supremum nicht das größte Element?
Nur, wenn es in der Menge liegt. $M=\{2-\frac1n:n\in\mathbb{N}\}=\{1,\frac32,\frac53,\dots\}$ hat $\min M=1$ und $\sup M=2$, aber kein Maximum, denn $2\notin M$. Im Rechenmodell ist $D$ nach oben beschränkt, zum Beispiel durch $1{,}5$. In $\mathbb{Q}$ hat $D$ trotzdem kein Supremum: Zu jeder oberen Schranke gibt es eine kleinere.
:::

:::definition Definition 6.3 (Vollständigkeitsaxiom (V))
<span class="anker" id="satz-6-3"></span>

Ein total angeordneter Körper $\mathbb K$ heißt __vollständig__, wenn jede nach unten beschränkte, nicht leere Menge $M\subset\mathbb K$ eine größte untere Schranke $\inf M\in\mathbb K$ besitzt.
:::

⁠**So liest man das:** Entscheidend ist „$\in\mathbb K$“. $\mathbb{Q}$ ist nicht vollständig: $\{x\in\mathbb{Q}:x>0,\ x^2>2\}$ ist nach unten beschränkt und nicht leer, hat aber in $\mathbb{Q}$ keine größte untere Schranke. Die Kandidatin wäre $\sqrt2\notin\mathbb{Q}$. **Warum „nicht leer“ und „beschränkt“:** Für $M=\emptyset$ ist jede Zahl untere Schranke, es gibt keine größte. $M=\mathbb{Z}$ hat keine untere Schranke.

:::satz Satz 6.4 (Hauptsatz)
<span class="anker" id="satz-6-4"></span>

Es gibt im Wesentlichen genau einen total angeordneten, vollständigen Körper, der $\mathbb{Q}$ enthält. Das ist der __Körper der reellen Zahlen__ $\mathbb{R}$, seine Ordnung stimmt auf $\mathbb{Q}$ mit der gewohnten überein.
:::

⁠**So liest man das:** Der Beweis führt zu weit, hier reicht die Bedeutung: Die drei Axiomgruppen legen $\mathbb{R}$ bis auf Umbenennen eindeutig fest, deshalb darf man von *den* reellen Zahlen sprechen. Das ersetzt die vorläufige Definition. Der Körper $\{0,1\}$ erfüllt nur die Körperaxiome, $\mathbb{Q}$ auch die Anordnung, erst $\mathbb{R}$ alle drei Gruppen. Gleichwertig zu (V) ist die Forderung, dass jede Cauchy-Folge konvergiert ([Kapitel 4](/wissen/elektrotechnik/1-semester/hohere-mathematik-1/folgen-und-grenzwerte/folgen-und-grenzwerte.html)).

:::satz Satz 6.5 (Folgerungen aus der Vollständigkeit)
<span class="anker" id="satz-6-5"></span>

In $\mathbb{R}$ gilt:

<ol class="rm">

<li>

Jede nach oben beschränkte, nicht leere Menge $M$ hat ein Supremum, und es gilt $\sup M=-\inf(-M)$ mit $-M:=\{-x:x\in M\}$.

</li>

<li>

Supremum und Infimum einer Menge sind eindeutig.

</li>

<li>

Ist $S=\sup M$, dann gibt es zu jedem $y<S$ ein $x\in M$ mit $y<x\le S$. Für das Infimum gilt das Entsprechende.

</li>

<li>

$\mathbb{N}$ ist nicht nach oben beschränkt.

</li>

<li>

__Satz von Archimedes:__ Für alle $x,y>0$ gibt es ein $n\in\mathbb{N}$ mit $nx>y$.

</li>

<li>

Für jedes $x>0$ gibt es ein $n\in\mathbb{N}$ mit $0<\frac1n<x$ (Eudoxus).

</li>

</ol>
:::

⁠**So liest man das:** (iii): Dicht unter dem Supremum liegt immer ein Element der Menge. (v): Mit genügend vielen kleinen Schritten $x$ kommt man über jede Höhe $y$. Für $x=0{,}001$ und $y=1000$ reicht $n=1\,000\,001$. Für $x=0$ gilt (v) nicht, denn $nx=0$. (vi): Für $x=0{,}003$ reicht $n=334$. Man kann (v) auch als Axiom fordern. Das ist weniger als (V), denn $\mathbb{Q}$ erfüllt es.

:::beweis Folgerungen
(i) Mit $M$ ist $-M$ nicht leer, und ist $S$ obere Schranke von $M$, dann $-S$ untere Schranke von $-M$ nach Satz [4.2](anordnungsaxiome.html#satz-4-2) (a). (V) liefert $R=\inf(-M)$. Weil das Spiegeln obere in untere Schranken übersetzt und die Reihenfolge dreht, ist $-R$ die kleinste obere Schranke von $M$.

(ii) Sind $S_1$, $S_2$ Suprema, sind beide obere Schranken. Also $S_1\le S_2$, weil $S_1$ die kleinste ist, und $S_2\le S_1$ ebenso. Nach (O1) ist $S_1=S_2$.

(iii) Indirekt: Gäbe es $y<S$ ohne solches $x$, wäre $x\le y$ für alle $x\in M$ (Verneinung, [(2.1)](quantoren-und-indirekter-beweis.html#gl-2-1)). Dann wäre $y$ eine obere Schranke kleiner als $S$, gegen die Definition von $\sup M$. Dass $x\le S$ ist, liegt daran, dass $S$ obere Schranke ist.

(iv) Indirekt: Sonst gäbe es $S=\sup\mathbb{N}$ nach (i). Nach (iii) gibt es $n\in\mathbb{N}$ mit $S-1<n$. Dann ist $n+1>S$ und $n+1\in\mathbb{N}$, gegen „obere Schranke“.

(v) Indirekt: Sei $nx\le y$ für alle $n$. Wegen $x^{-1}>0$ folgt nach (O4) $n\le yx^{-1}$ für alle $n$, gegen (iv). (vi): $y:=1$ in (v) gibt $nx>1$, also $x>\frac1n>0$.
:::

:::aufgabe Aufgabe 7 ★★ Schranken bestimmen
<span class="anker" id="aufg-7"></span>

Bestimme Supremum, Infimum, Maximum und Minimum in $\mathbb{R}$, soweit vorhanden, und begründe: (a) $M_1=\{x\in\mathbb{Q}:x^2\le4\}$, (b) $M_2=\{\frac{(-1)^n}n:n\in\mathbb{N}\}$, (c) $M_3=\{x\in\mathbb{Q}:x^2<3\}$. Welche dieser Größen fehlen in (c), wenn man nur in $\mathbb{Q}$ sucht?

:::loesung
(a) $M_1=\{x\in\mathbb{Q}:-2\le x\le2\}$: $\sup=\max=2$, $\inf=\min=-2$. (b) $M_2=\{-1,\frac12,-\frac13,\frac14,\dots\}$: $\sup=\max=\frac12$, $\inf=\min=-1$. (c) $\sup M_3=\sqrt3$, $\inf M_3=-\sqrt3$, kein Maximum und kein Minimum, weil $\sqrt3\notin\mathbb{Q}$ (Aufgabe [8](intervallschachtelung-und-wurzeln.html#aufg-8)). In $\mathbb{Q}$ fehlen auch Supremum und Infimum: Zu jeder rationalen oberen Schranke gibt es eine kleinere.
:::
:::

::::formelsammlung
**Die Wurzel aus 2 ist kein Bruch**

$$\nexists r\in\mathbb{Q}:\ r^2=2$$

Indirekter Beweis: Aus $r=\frac pq$, gekürzt, folgt $p^2=2q^2$, und $p$ und $q$ wären beide gerade. Trotzdem liegt zwischen zwei Brüchen $p/q<u/v$ immer ein weiterer, $\frac12(p/q+u/v)$.

**Schranken**

$$x\le S\ \text{für alle}\ x\in M,\qquad R\le x\ \text{für alle}\ x\in M$$

Für $M\subset\mathbb K$, $\mathbb K$ total angeordnet, $S,R\in\mathbb K$: $S$ ist obere Schranke ($M$ nach oben beschränkt), $R$ untere Schranke ($M$ nach unten beschränkt); beides zusammen heißt beschränkt. Schranken sind nicht eindeutig.

**Supremum und Infimum**

$$S=\sup M,\qquad R=\inf M$$

$\sup M$: obere Schranke $S$ mit $S\le\tilde S$ für jede obere Schranke $\tilde S$ (kleinste obere Schranke). $\inf M$: untere Schranke $R$ mit $\tilde R\le R$ für jede untere Schranke $\tilde R$ (größte untere Schranke). Liegen sie in $M$, heißen sie Maximum ($\max M$) und Minimum ($\min M$).

**Vollständigkeitsaxiom (V)**

$$M\subset\mathbb K,\ M\ne\emptyset,\ M\ \text{nach unten beschränkt}\quad\Longrightarrow\quad\inf M\in\mathbb K$$

Ein total angeordneter Körper mit dieser Eigenschaft heißt vollständig. $\mathbb{Q}$ ist nicht vollständig: $\{x\in\mathbb{Q}:x>0,\ x^2>2\}$ hat in $\mathbb{Q}$ keine größte untere Schranke. Es gibt im Wesentlichen genau einen total angeordneten, vollständigen Körper, der $\mathbb{Q}$ enthält: den Körper der reellen Zahlen $\mathbb{R}$.

**Supremum aus dem Infimum**

$$\sup M=-\inf(-M),\qquad-M:=\{-x:x\in M\}$$

In $\mathbb{R}$ für jede nach oben beschränkte, nicht leere Menge $M$. Supremum und Infimum einer Menge sind eindeutig.

**Elemente dicht unter dem Supremum**

$$\forall y<S\ \exists x\in M:\ y<x\le S$$

Für $S=\sup M$; für das Infimum gilt das Entsprechende.

**Satz von Archimedes**

$$\forall x,y>0\ \exists n\in\mathbb{N}:\ nx>y$$

Folgt daraus, dass $\mathbb{N}$ nicht nach oben beschränkt ist. Für $x=0$ falsch. Auch $\mathbb{Q}$ erfüllt ihn; als Axiom wäre er weniger als (V).

**Eudoxus**

$$\forall x>0\ \exists n\in\mathbb{N}:\ 0<\frac1n<x$$

Der Satz von Archimedes mit $y:=1$.
::::

::::lernkarten
:::karte zusammenhang Lücken in den Brüchen
Warum liegen die Brüche scheinbar lückenlos auf der Zahlengeraden, und warum haben sie trotzdem Lücken?
---
Zwischen zwei Brüchen $p/q<u/v$ liegt immer ein weiterer, etwa $\frac12(p/q+u/v)$. Trotzdem gibt es Stellen, die kein Bruch trifft: Kein $r\in\mathbb{Q}$ erfüllt $r^2=2$.
--- falsch
Zwischen zwei Brüchen liegt nur dann ein weiterer, wenn ihre Nenner verschieden sind. Lücken entstehen dort, wo zwei Brüche mit demselben Nenner direkt nebeneinander liegen.
--- falsch
Zwischen zwei Brüchen $p/q<u/v$ liegt immer ein weiterer, etwa $\frac12(p/q+u/v)$. Deshalb haben die Brüche keine Lücken; $\sqrt2$ ist ein Bruch mit sehr großem Nenner.
--- falsch
Zwischen zwei Brüchen $p/q<u/v$ liegen nur endlich viele weitere. Die Lücken sind die Stellen zwischen zwei benachbarten Brüchen, die es nach diesem Argument geben muss.
:::
:::karte herleitung die Wurzel aus 2 ist kein Bruch
Wie beweist man indirekt, dass es kein $r\in\mathbb{Q}$ mit $r^2=2$ gibt?
---
Annahme: $r=\frac pq$ mit $p,q\in\mathbb{N}$, so weit gekürzt, dass $p$ und $q$ nicht beide gerade sind; das Vorzeichen spielt keine Rolle, weil $r$ und $-r$ dasselbe Quadrat haben.
---
Aus $r^2=2$ folgt $p^2=2q^2$, also ist $p^2$ gerade, weil es das Doppelte der ganzen Zahl $q^2$ ist.
---
Dann ist $p$ gerade, $p=2k$, weil nach der Kontraposition von „$n$ ungerade $\Rightarrow$ $n^2$ ungerade“ jede Zahl mit geradem Quadrat selbst gerade ist.
---
Einsetzen gibt $4k^2=2q^2$, also $q^2=2k^2$, und ebenso ist $q$ gerade, weil dasselbe Argument wie für $p$ greift.
---
Dann sind $p$ und $q$ beide gerade; das ist ein Widerspruch, weil der Bruch so weit gekürzt war, dass sie nicht beide gerade sind.
:::
:::karte begriff nach oben beschränkt und obere Schranke
Wann heißt eine Menge $M\subset\mathbb K$ in einem total angeordneten Körper nach oben beschränkt, und was ist eine obere Schranke?
---
$M$ heißt nach oben beschränkt, wenn es $S\in\mathbb K$ gibt mit $x\le S$ für alle $x\in M$. Jedes solche $S$ heißt obere Schranke; obere Schranken sind nicht eindeutig.
--- falsch
$M$ heißt nach oben beschränkt, wenn es $S\in M$ gibt mit $x\le S$ für alle $x\in M$. Dieses $S$ heißt obere Schranke; jede beschränkte Menge hat genau eine.
--- falsch
$M$ heißt nach oben beschränkt, wenn es zu jedem $x\in M$ ein $S\in\mathbb K$ mit $x\le S$ gibt. Jedes solche $S$ heißt obere Schranke von $M$.
--- falsch
$M$ heißt nach oben beschränkt, wenn $M$ nur endlich viele Elemente hat. Das größte Element heißt obere Schranke; unendliche Mengen haben keine.
:::
:::karte begriff nach unten beschränkt und untere Schranke
Wann heißt eine Menge $M\subset\mathbb K$ in einem total angeordneten Körper nach unten beschränkt, und was ist eine untere Schranke?
---
$M$ heißt nach unten beschränkt, wenn es $R\in\mathbb K$ gibt mit $R\le x$ für alle $x\in M$. Jedes solche $R$ heißt untere Schranke; untere Schranken sind nicht eindeutig.
--- falsch
$M$ heißt nach unten beschränkt, wenn es $R\in\mathbb K$ gibt mit $R\ge x$ für alle $x\in M$. Jedes solche $R$ heißt untere Schranke, weil es unter keinem Element liegt.
--- falsch
$M$ heißt nach unten beschränkt, wenn alle Elemente von $M$ positiv sind. Die Null ist dann die untere Schranke von $M$, und eine andere gibt es nicht.
--- falsch
$M$ heißt nach unten beschränkt, wenn es $R\in M$ gibt mit $R\le x$ für alle $x\in M$. Dieses kleinste Element heißt untere Schranke und ist eindeutig.
:::
:::karte begriff beschränkt
Wann heißt eine Teilmenge $M$ eines total angeordneten Körpers $\mathbb K$ beschränkt?
---
Wenn sie nach oben und nach unten beschränkt ist, es also $R,S\in\mathbb K$ gibt mit $R\le x$ und $x\le S$ für alle $x\in M$.
--- falsch
Wenn sie nach oben oder nach unten beschränkt ist; eine der beiden Schranken genügt, so ist zum Beispiel auch $\mathbb{N}$ beschränkt.
--- falsch
Wenn sie endlich viele Elemente hat. Unendliche Mengen sind nie beschränkt, auch nicht die Menge $\{2-\frac1n:n\in\mathbb{N}\}$.
--- falsch
Wenn sie ein größtes und ein kleinstes Element besitzt, also ein Maximum und ein Minimum hat, die beide in $M$ liegen.
:::
:::karte begriff Supremum
Wann heißt $S$ Supremum einer Menge $M\subset\mathbb K$, geschrieben $S=\sup M$?
---
Wenn $S$ eine obere Schranke von $M$ ist und für jede obere Schranke $\tilde S$ gilt $S\le\tilde S$; das Supremum ist die kleinste obere Schranke.
--- falsch
Wenn $S$ das größte Element von $M$ ist, also $S\in M$ und $x\le S$ für alle $x\in M$. Mengen ohne größtes Element haben deshalb kein Supremum.
--- falsch
Wenn $S$ eine obere Schranke von $M$ ist und für jede obere Schranke $\tilde S$ gilt $S\ge\tilde S$; das Supremum ist die größte obere Schranke von $M$.
--- falsch
Wenn $S$ eine obere Schranke von $M$ ist, die selbst in $\mathbb K$ liegt. Jede obere Schranke ist ein Supremum, deshalb hat $M$ meist viele Suprema.
:::
:::karte begriff Infimum
Wann heißt $R$ Infimum einer Menge $M\subset\mathbb K$, geschrieben $R=\inf M$?
---
Wenn $R$ eine untere Schranke von $M$ ist und für jede untere Schranke $\tilde R$ gilt $\tilde R\le R$; das Infimum ist die größte untere Schranke.
--- falsch
Wenn $R$ eine untere Schranke von $M$ ist und für jede untere Schranke $\tilde R$ gilt $R\le\tilde R$; das Infimum ist die kleinste untere Schranke.
--- falsch
Wenn $R$ das kleinste Element von $M$ ist, also $R\in M$ und $R\le x$ für alle $x\in M$. Mengen ohne kleinstes Element haben kein Infimum.
--- falsch
Wenn $R$ eine untere Schranke von $M$ ist und alle Elemente von $M$ echt größer als $R$ sind; liegt $R$ selbst in $M$, ist es kein Infimum.
:::
:::karte begriff Maximum und Minimum
Wann heißt das Supremum einer Menge Maximum und das Infimum Minimum?
---
Wenn es in der Menge liegt: Liegt $S=\sup M$ in $M$, heißt es Maximum ($\max M$); liegt $R=\inf M$ in $M$, heißt es Minimum ($\min M$).
--- falsch
Wenn es eine natürliche Zahl ist: Ganzzahlige Suprema heißen Maximum, ganzzahlige Infima Minimum, gleich ob sie in $M$ liegen oder nicht.
--- falsch
Immer: Maximum und Minimum sind nur andere Namen für Supremum und Infimum, die man bei endlichen Mengen statt der lateinischen Namen verwendet.
--- falsch
Wenn es nicht in der Menge liegt: Das Maximum ist die Grenze, an die sich die Elemente annähern, ohne sie zu erreichen; beim Minimum ebenso.
:::
:::karte zusammenhang Supremum ohne Maximum
Warum hat die Menge $M=\{2-\frac1n:n\in\mathbb{N}\}$ das Supremum 2, aber kein Maximum?
---
Weil 2 eine obere Schranke ist und jede kleinere Zahl von einem Element $2-\frac1n$ übertroffen wird; 2 ist also die kleinste obere Schranke. Wegen $2\notin M$ ist sie kein Maximum.
--- falsch
Weil 2 das größte Element von $M$ ist, das man für sehr große $n$ erhält; ein Maximum gibt es trotzdem nicht, weil $M$ unendlich viele Elemente hat.
--- falsch
Weil jede Zahl über 2 eine obere Schranke ist und 2 die erste von ihnen; ein Maximum gibt es nicht, weil $M$ auch kein Minimum hat und beides zusammengehört.
--- falsch
Weil $2-\frac1n$ für $n=1$ den größten Wert 1 annimmt und 2 nur eine von vielen oberen Schranken ist; das Supremum ist deshalb eigentlich 1, das Maximum ebenso.
:::
:::karte begriff vollständig
Wann heißt ein total angeordneter Körper $\mathbb K$ vollständig?
---
Wenn jede nach unten beschränkte, nicht leere Menge $M\subset\mathbb K$ eine größte untere Schranke $\inf M\in\mathbb K$ besitzt (Vollständigkeitsaxiom (V)).
--- falsch
Wenn jede nach unten beschränkte, nicht leere Menge $M\subset\mathbb K$ ein kleinstes Element $\min M\in M$ besitzt (Vollständigkeitsaxiom (V)).
--- falsch
Wenn jede nicht leere Menge $M\subset\mathbb K$ eine größte untere Schranke $\inf M\in\mathbb K$ besitzt, auch ohne untere Schranke (Vollständigkeitsaxiom (V)).
--- falsch
Wenn er die Körperaxiome und die Anordnungsaxiome vollständig erfüllt, also kein Axiom dieser beiden Gruppen fehlt (Vollständigkeitsaxiom (V)).
:::
:::karte begriff Vollständigkeit
Welche Eigenschaft der Zahlengeraden beschreibt die Vollständigkeit, und welcher der Körper $\mathbb{Q}$ und $\mathbb{R}$ hat sie?
---
Dass die Zahlengerade keine Lücken hat: Jede nach unten beschränkte, nicht leere Menge hat ein Infimum im Körper. $\mathbb{R}$ hat sie, $\mathbb{Q}$ nicht: $\{x\in\mathbb{Q}:x>0,\ x^2>2\}$ hat in $\mathbb{Q}$ kein Infimum.
--- falsch
Dass die Zahlengerade keine Lücken hat: Zwischen zwei Zahlen liegt immer eine weitere. $\mathbb{Q}$ und $\mathbb{R}$ haben sie beide, weil zwischen zwei Brüchen stets ihr Mittelwert liegt.
--- falsch
Dass die Zahlengerade nach oben und unten unbeschränkt ist: Zu jeder Zahl gibt es eine größere. $\mathbb{R}$ hat sie, $\mathbb{Q}$ nicht, weil die Brüche bei großen Nennern enden.
--- falsch
Dass jede Zahl eine Dezimaldarstellung hat. $\mathbb{Q}$ hat sie, $\mathbb{R}$ nicht, weil Zahlen wie $\sqrt2$ unendlich viele Ziffern brauchen und nie fertig aufgeschrieben sind.
:::
:::karte zusammenhang nicht leer und beschränkt
Warum verlangt das Vollständigkeitsaxiom, dass die Menge nicht leer und nach unten beschränkt ist?
---
Weil es sonst kein Infimum geben kann: Für $M=\emptyset$ ist jede Zahl untere Schranke, und es gibt keine größte. $M=\mathbb{Z}$ hat gar keine untere Schranke.
--- falsch
Weil sonst das Infimum nicht eindeutig wäre: Die leere Menge hätte zwei Infima, und $\mathbb{Z}$ hätte eines für die positiven und eines für die negativen Zahlen.
--- falsch
Die Bedingungen dienen nur der Vereinfachung: Auch die leere Menge und $\mathbb{Z}$ haben ein Infimum in $\mathbb{R}$, es liegt nur nicht in $\mathbb{Q}$.
--- falsch
Weil sonst das Infimum in der Menge liegen müsste: Für $M=\emptyset$ wäre $\inf M\in\emptyset$, und $\mathbb{Z}$ hat kein kleinstes Element.
:::
:::karte begriff Körper der reellen Zahlen
Was besagt der Hauptsatz über den Körper der reellen Zahlen $\mathbb{R}$?
---
Es gibt bis auf Umbenennen genau einen total angeordneten, vollständigen Körper, der $\mathbb{Q}$ enthält; seine Ordnung stimmt auf $\mathbb{Q}$ mit der gewohnten überein.
--- falsch
Es gibt viele verschiedene total angeordnete, vollständige Körper, die $\mathbb{Q}$ enthalten, und $\mathbb{R}$ ist der kleinste davon. Welchen man nimmt, ist eine Frage der Bequemlichkeit.
--- falsch
Es gibt genau einen total angeordneten Körper, der $\mathbb{Q}$ enthält, und das ist $\mathbb{R}$. Die Vollständigkeit folgt dann von selbst aus den Körper- und Anordnungsaxiomen.
--- falsch
Es gibt genau einen vollständigen Körper, der $\mathbb{Q}$ enthält; ob er total angeordnet ist, spielt keine Rolle. Deshalb stimmen auch die komplexen Zahlen mit $\mathbb{R}$ überein.
:::
:::karte formel Supremum über das Infimum
Warum hat in $\mathbb{R}$ auch jede nach oben beschränkte, nicht leere Menge $M$ ein Supremum, und wie hängt es mit einem Infimum zusammen?
---
Spiegeln an der Null macht aus oberen Schranken von $M$ untere Schranken von $-M:=\{-x:x\in M\}$ und dreht die Reihenfolge. (V) liefert $\inf(-M)$, und es gilt $\sup M=-\inf(-M)$.
--- falsch
Weil jede nach oben beschränkte Menge ein Maximum hat; das Supremum ist dieses Maximum. Mit dem Infimum hängt es über $\sup M=\inf M$ zusammen.
--- falsch
Spiegeln an der Null macht aus oberen Schranken von $M$ untere Schranken von $-M:=\{-x:x\in M\}$. (V) liefert $\inf(-M)$, und es gilt $\sup M=\inf(-M)$, weil Spiegeln die Reihenfolge erhält.
--- falsch
Weil das Vollständigkeitsaxiom (V) ausdrücklich auch obere Schranken nennt. Mit dem Infimum hängt das Supremum über $\sup M=-\inf M$ zusammen.
:::
:::karte formel Elemente dicht unter dem Supremum
Was garantiert die Definition des Supremums $S=\sup M$ für jede Zahl $y<S$?
---
Es gibt ein $x\in M$ mit $y<x\le S$. Gäbe es keines, wäre $x\le y$ für alle $x\in M$, also $y$ eine obere Schranke kleiner als $S$, gegen die Definition.
--- falsch
Es gibt ein $x\in M$ mit $x=S$, denn das Supremum wird von der Menge immer erreicht; zwischen $y$ und $S$ liegen keine weiteren Elemente von $M$.
--- falsch
Es gibt kein $x\in M$ mit $y<x$, denn alle Elemente liegen unterhalb jeder Zahl, die kleiner als das Supremum ist; $y$ ist selbst eine obere Schranke.
--- falsch
Es gibt ein $x\in M$ mit $x>S$, das zwischen $S$ und der nächsten oberen Schranke liegt; das Supremum ist nur eine untere Grenze dafür.
:::
:::karte herleitung natürliche Zahlen unbeschränkt
Wie zeigt man indirekt mit dem Supremum, dass $\mathbb{N}$ in $\mathbb{R}$ nicht nach oben beschränkt ist?
---
Wäre $\mathbb{N}$ nach oben beschränkt, gäbe es $S=\sup\mathbb{N}$, weil in $\mathbb{R}$ jede nach oben beschränkte, nicht leere Menge ein Supremum hat.
---
Zu $S-1<S$ gibt es dann ein $n\in\mathbb{N}$ mit $S-1<n$, weil dicht unter dem Supremum immer ein Element der Menge liegt.
---
Dann ist $n+1>S$ und $n+1\in\mathbb{N}$, weil man auf beiden Seiten 1 addieren darf und $\mathbb{N}$ mit $n$ auch $n+1$ enthält.
---
Das ist ein Widerspruch, weil $S$ als obere Schranke größer oder gleich jedem Element von $\mathbb{N}$ sein müsste.
:::
:::karte formel Satz von Archimedes
Was besagt der Satz von Archimedes über zwei positive reelle Zahlen $x$ und $y$?
---
Für alle $x,y>0$ gibt es ein $n\in\mathbb{N}$ mit $nx>y$: Mit genügend vielen kleinen Schritten $x$ kommt man über jede Höhe $y$. Für $x=0$ gilt das nicht, denn $nx=0$.
--- falsch
Für alle $x,y>0$ gilt $nx>y$ für jedes $n\in\mathbb{N}$: Schon ein einziger Schritt $x$ übertrifft jede Höhe $y$, weil $x$ positiv ist.
--- falsch
Für alle $x,y>0$ gibt es ein $n\in\mathbb{N}$ mit $nx>y$; das gilt aber nur in $\mathbb{Q}$, weil man in $\mathbb{R}$ keine ganzzahligen Vielfachen einer irrationalen Zahl bilden kann.
--- falsch
Für alle $x,y>0$ gibt es ein $n\in\mathbb{N}$ mit $x>ny$: Jede Zahl ist größer als ein Vielfaches jeder anderen, auch eine sehr kleine.
:::
:::karte formel Eudoxus
Warum gibt es zu jedem $x>0$ ein $n\in\mathbb{N}$ mit $0<\frac1n<x$?
---
Nach dem Satz von Archimedes mit $y:=1$ gibt es $n$ mit $nx>1$, also $x>\frac1n>0$. Für $x=0{,}003$ reicht zum Beispiel $n=334$.
--- falsch
Weil $\frac1n$ für jedes $n$ kleiner als jede positive Zahl ist; schon $n=1$ erfüllt $\frac11<x$ für alle $x>0$, auch für sehr kleine.
--- falsch
Nach dem Satz von Archimedes mit $y:=x$ gibt es $n$ mit $nx>x$, also $\frac1n<1$. Für $x=0{,}003$ reicht zum Beispiel schon $n=2$.
--- falsch
Weil $\mathbb{N}$ nach oben beschränkt ist: Die Kehrwerte $\frac1n$ haben deshalb eine positive untere Schranke, und unter $x$ liegt immer einer davon.
:::
:::karte zusammenhang Archimedes als Axiom
Warum genügt es nicht, statt des Vollständigkeitsaxioms den Satz von Archimedes als Axiom zu fordern?
---
Weil Archimedes weniger fordert als (V): Auch $\mathbb{Q}$ erfüllt ihn, hat aber Lücken. Mit Archimedes allein bliebe offen, ob es eine Zahl mit Quadrat 2 gibt.
--- falsch
Weil Archimedes mehr fordert als (V): Kein total angeordneter Körper erfüllt ihn, auch $\mathbb{R}$ nicht, sodass die Axiome widersprüchlich würden.
--- falsch
Es genügt sehr wohl: Archimedes und (V) sind gleichwertig; man wählt (V) nur, weil es kürzer zu formulieren ist und sich leichter merken lässt.
--- falsch
Weil Archimedes nur für natürliche Zahlen gilt: Für reelle $x$ und $y$ lässt sich kein Vielfaches $nx$ bilden, das $y$ übertrifft.
:::
::::
