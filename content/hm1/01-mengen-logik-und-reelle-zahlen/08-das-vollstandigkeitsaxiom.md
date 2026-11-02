---
title: Stufe 6: Das Vollständigkeitsaxiom
pfad: Elektrotechnik / 1. Semester / Höhere Mathematik 1 / Mengen, Logik und reelle Zahlen
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

⁠**So liest man das:** Der Beweis führt zu weit, hier reicht die Bedeutung: Die drei Axiomgruppen legen $\mathbb{R}$ bis auf Umbenennen eindeutig fest, deshalb darf man von *den* reellen Zahlen sprechen. Das ersetzt die vorläufige Definition. Der Körper $\{0,1\}$ erfüllt nur die Körperaxiome, $\mathbb{Q}$ auch die Anordnung, erst $\mathbb{R}$ alle drei Gruppen. Gleichwertig zu (V) ist die Forderung, dass jede Cauchy-Folge konvergiert ([Teil 4](/wissen/elektrotechnik/1-semester/hohere-mathematik-1/folgen-und-grenzwerte/folgen-und-grenzwerte.html)).

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
