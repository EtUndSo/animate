---
title: Stufe 1: Mengen und Aussagen
pfad: Elektrotechnik / 1. Semester / HöMa1 – Höhere Mathematik 1 / Mengen, Logik und reelle Zahlen
adresse: elektrotechnik/1-semester/hohere-mathematik-1/mengen-logik-und-reelle-zahlen
knoten: Kapitel 1: Mengen, Logik und reelle Zahlen
order: 1210300
summary: Axiome reden über „alle Zahlen mit einer Eigenschaft“ und über „wenn, dann“.
tags: Venn-Diagramm, Elemente, Teilmenge, Obermenge, Vereinigung, Durchschnitt, Differenz, Komplement
lang: de
---

<span class="anker" id="stufe-1"></span>

:::zweck
Axiome reden über „alle Zahlen mit einer Eigenschaft“ und über „wenn, dann“. Diese Stufe liefert die Sprache dafür und ein sicheres Verfahren, Regeln für Mengen und Aussagen zu beweisen.
:::

**Die Idee.** Für eine Menge zählt nur eine Frage: Liegt ein Objekt darin oder nicht? Für eine Aussage ebenso: wahr oder falsch? Bei zwei Mengen oder Aussagen gibt es deshalb vier Fälle, bei dreien acht. Eine Regel beweist man, indem man alle Fälle in einer Tafel durchgeht. Ein __Venn-Diagramm__ (Mengen als Flächen gezeichnet) veranschaulicht nur, es zeigt eine mögliche Lage der Mengen (Abb. [1](#abb-1)).

:::definition Definition 1.1 (Menge)
<span class="anker" id="satz-1-1"></span>

Eine Menge ist eine ungeordnete Zusammenfassung bestimmter, wohlunterscheidbarer Objekte, ihrer __Elemente__. $x\in M$ heißt „$x$ ist Element von $M$“, $x\notin M$ das Gegenteil. Für Mengen $A$, $B$ sind festgelegt:

| Zeichen | Name | Bedeutung |
|---|---|---|
| $A\subset B$ | __Teilmenge__ | jedes Element von $A$ liegt in $B$ ($A=B$ ist erlaubt); $B\supset A$: __Obermenge__ |
| $A=B$ | Gleichheit | $A\subset B$ und $B\subset A$; sonst schreibt man $A\ne B$ |
| $A\cup B$ | __Vereinigung__ | alle Elemente, die in $A$ oder in $B$ liegen, auch in beiden |
| $A\cap B$ | __Durchschnitt__ | alle Elemente, die in $A$ und in $B$ liegen |
| $A\setminus B$ | __Differenz__ | alle Elemente von $A$, die nicht in $B$ liegen |
| $A^c$ | __Komplement__ | alle Elemente einer festen Obermenge, die nicht in $A$ liegen |
| $\emptyset=\{\,\}$ | __leere Menge__ | enthält kein Element |
| $\mathcal P(A)$ | __Potenzmenge__ | Menge aller Teilmengen von $A$ |

$A$ und $B$ heißen __disjunkt__, wenn $A\cap B=\emptyset$.
:::

⁠**So liest man das:** Im Rechenmodell ist $A\cup B=\{1,2,3,4,5,6,7,11,12\}$, $A\cap B=\{2,3\}$, $A\setminus B=\{1,4,6,12\}$, $A^c=\{5,7,8,9,10,11\}$ bezogen auf $G$. Eine Menge lässt sich durch eine Eigenschaft angeben: $\{x\in G:x\text{ gerade}\}=\{2,4,6,8,10,12\}$. Es ist $\mathcal P(\{5,7\})=\{\emptyset,\{5\},\{7\},\{5,7\}\}$. Immer gilt $\emptyset\subset A$, $A\cup\emptyset=A$, $A\cap\emptyset=\emptyset$, $A\setminus B=A\cap B^c$.

:::abbildung hm1/k1venn 1
Links die Elemente von $G$ in den vier Bereichen. Rechts ist $(A\cap B)^c$ gefärbt, alles außer der Linse.
:::

:::definition Definition 1.2 (Aussage und Verknüpfungen)
<span class="anker" id="satz-1-2"></span>

Eine Aussage ist eine Behauptung, die nur wahr ($w$) oder falsch ($f$) sein kann. Aus Aussagen $\mathcal A$, $\mathcal B$ entstehen neue, festgelegt durch diese __Wahrheitstafel__:

| $\mathcal A$ | $\mathcal B$ | $\neg\mathcal A$ | $\mathcal A\vee\mathcal B$ | $\mathcal A\wedge\mathcal B$ | $\mathcal A\Rightarrow\mathcal B$ | $\mathcal A\Leftrightarrow\mathcal B$ |
|---|---|---|---|---|---|---|
| $w$ | $w$ | $f$ | $w$ | $w$ | $w$ | $w$ |
| $w$ | $f$ | $f$ | $w$ | $f$ | $f$ | $f$ |
| $f$ | $w$ | $w$ | $w$ | $f$ | $w$ | $f$ |
| $f$ | $f$ | $w$ | $f$ | $f$ | $w$ | $w$ |

Die Namen sind __Negation__, __Disjunktion__, __Konjunktion__, __Implikation__ und __Äquivalenz__.
:::

⁠**So liest man das:** „2 ist Primzahl“ ist eine wahre Aussage, „Wie spät ist es?“ keine. Auch „jede gerade Zahl ab 4 ist Summe zweier Primzahlen“ ist eine Aussage, obwohl niemand weiß, ob sie wahr ist (Goldbachsche Vermutung). Aussagen können von einem __Parameter__ abhängen: $\mathcal T(n):=(n\text{ teilt }12)$ ist für $n=4$ wahr und für $n=5$ falsch. „Oder“ schließt „beide“ ein. $\neg$ bindet am stärksten: $\neg\mathcal A\vee\mathcal B$ heißt $(\neg\mathcal A)\vee\mathcal B$. $\mathcal A\Leftrightarrow\mathcal B$ ist gleichbedeutend mit $(\mathcal A\Rightarrow\mathcal B)\wedge(\mathcal B\Rightarrow\mathcal A)$. Zwei Aussagen mit derselben Tafelspalte sind *äquivalent*. Ist $\mathcal A\Rightarrow\mathcal B$ wahr und $\mathcal A$ wahr, dann ist $\mathcal B$ wahr. Ist $\mathcal A$ falsch, sagt die Implikation nichts über $\mathcal B$.

:::frage Warum ist $f\Rightarrow w$ wahr? Aus etwas Falschem folgt doch nichts.
Richtig ist: Ein falsches $\mathcal A$ sagt nichts über $\mathcal B$. Genau deshalb ist die Implikation dann nicht verletzt. Die Festlegung ist erzwungen: $\mathcal E(n)$ soll für alle $n$ wahr sein, und $n=6$ liefert $f\Rightarrow w$, $n\le5$ liefert $f\Rightarrow f$. Wären diese Zeilen falsch, wäre $\mathcal E(n)$ dort falsch. Nur $w\Rightarrow f$ kommt für kein $n$ vor, und das ist die ganze Behauptung: $\{n\ge7\}$ liegt in $\{n>5\}$. Eine Implikation ist eine Teilmengenbeziehung.
:::

:::satz Satz 1.3 (Rechenregeln und Tautologien)
<span class="anker" id="satz-1-3"></span>

Eine __Tautologie__ ist eine Aussage, die für alle Wahrheitswerte ihrer Bausteine wahr ist. Für Mengen in einer Obermenge und für Aussagen gelten die folgenden Regeln:

| Name | Mengen | Aussagen |
|---|---|---|
| Doppelt | $(A^c)^c=A$ | $\neg(\neg\mathcal A)\Leftrightarrow\mathcal A$ |
| Kommutativ | $A\cap B=B\cap A$, $A\cup B=B\cup A$ | $(\mathcal A\wedge\mathcal B)\Leftrightarrow(\mathcal B\wedge\mathcal A)$, $(\mathcal A\vee\mathcal B)\Leftrightarrow(\mathcal B\vee\mathcal A)$ |
| Assoziativ | $(A\cap B)\cap C=A\cap(B\cap C)$, ebenso mit $\cup$ | $(\mathcal A\wedge(\mathcal B\wedge\mathcal C))\Leftrightarrow((\mathcal A\wedge\mathcal B)\wedge\mathcal C)$, ebenso mit $\vee$ |
| Distributiv | $A\cap(B\cup C)=(A\cap B)\cup(A\cap C)$, $A\cup(B\cap C)=(A\cup B)\cap(A\cup C)$ | $(\mathcal A\wedge(\mathcal B\vee\mathcal C))\Leftrightarrow((\mathcal A\wedge\mathcal B)\vee(\mathcal A\wedge\mathcal C))$, $(\mathcal A\vee(\mathcal B\wedge\mathcal C))\Leftrightarrow((\mathcal A\vee\mathcal B)\wedge(\mathcal A\vee\mathcal C))$ |
| De Morgan | $(A\cap B)^c=A^c\cup B^c$, $(A\cup B)^c=A^c\cap B^c$ | $\neg(\mathcal A\wedge\mathcal B)\Leftrightarrow(\neg\mathcal A\vee\neg\mathcal B)$, $\neg(\mathcal A\vee\mathcal B)\Leftrightarrow(\neg\mathcal A\wedge\neg\mathcal B)$ |
| Idempotenz | $A\cup A=A$, $A\cap A=A$ | $(\mathcal A\vee\mathcal A)\Leftrightarrow\mathcal A$, $(\mathcal A\wedge\mathcal A)\Leftrightarrow\mathcal A$ |
| Implikation | $A\subset B\Leftrightarrow A^c\cup B=G$ ($G$ Obermenge) | $(\mathcal A\Rightarrow\mathcal B)\Leftrightarrow(\neg\mathcal A\vee\mathcal B)$ |
| Kontraposition | $A\subset B\Leftrightarrow B^c\subset A^c$ | $(\mathcal A\Rightarrow\mathcal B)\Leftrightarrow(\neg\mathcal B\Rightarrow\neg\mathcal A)$ |
| Transitivität | $(A\subset B\wedge B\subset C)\Rightarrow A\subset C$ | $((\mathcal A\Rightarrow\mathcal B)\wedge(\mathcal B\Rightarrow\mathcal C))\Rightarrow(\mathcal A\Rightarrow\mathcal C)$ |
:::

⁠**So liest man das:** Links und rechts steht dieselbe Regel, weil jede Mengenbeziehung eine Aussage über Elemente ist: $A\subset B$ heißt „für alle $x$: $(x\in A)\Rightarrow(x\in B)$“, $A=B$ heißt „für alle $x$: $(x\in A)\Leftrightarrow(x\in B)$“, und $x\in A\cap B$, $x\in A\cup B$, $x\in A\setminus B$ heißen $(x\in A)\wedge(x\in B)$, $(x\in A)\vee(x\in B)$, $(x\in A)\wedge(x\notin B)$. Die Gatter der Digitaltechnik sind $\neg$, $\wedge$, $\vee$ als Schaltung, und De Morgan erlaubt, ein Und aus Oder und Invertern zu bauen.

:::beweis De Morgan und Kontraposition per Tafel
Alle vier Fälle der Bausteine durchgehen. Liest man $w$ als „$x$ liegt in der Menge“, ist das zugleich der Beweis für Mengen (__Element-Tafel__).

| $\mathcal A$ | $\mathcal B$ | $\neg\mathcal A$ | $\neg\mathcal B$ | $\neg(\mathcal A\wedge\mathcal B)$ | $\neg\mathcal A\vee\neg\mathcal B$ | $\mathcal A\Rightarrow\mathcal B$ | $\neg\mathcal B\Rightarrow\neg\mathcal A$ |
|---|---|---|---|---|---|---|---|
| $w$ | $w$ | $f$ | $f$ | $f$ | $f$ | $w$ | $w$ |
| $w$ | $f$ | $f$ | $w$ | $w$ | $w$ | $f$ | $f$ |
| $f$ | $w$ | $w$ | $f$ | $w$ | $w$ | $w$ | $w$ |
| $f$ | $f$ | $w$ | $w$ | $w$ | $w$ | $w$ | $w$ |

Spalte 5 und 6 stimmen überein, ebenso Spalte 7 und 8. Die anderen Regeln gehen genauso. Die Transitivität der Inklusion folgt aus der der Implikation: Aus $x\in A$ folgt $x\in B$, daraus $x\in C$.
:::

::::beispiel
$(A\cap B)^c=G\setminus\{2,3\}$ hat 10 Elemente. Rechts steht $A^c\cup B^c=\{5,7,8,9,10,11\}\cup\{1,4,6,8,9,10,12\}$, dieselben 10 Elemente. Kontraposition als Beweismittel: Statt „$n^2$ gerade $\Rightarrow$ $n$ gerade“ zeigt man „$n$ ungerade $\Rightarrow$ $n^2$ ungerade“: $(2k+1)^2=2(2k^2+2k)+1$.
::::

⁠**Grenzfälle:** Für $B=\emptyset$ wird De Morgan zu $G=G$. Der Grundbereich zählt mit: $(n\ge7\Leftrightarrow n>6)$ gilt in $\mathbb{N}$, für $n=13/2$ ist es $f\Leftrightarrow w$, also falsch.

:::aufgabe Aufgabe 1 ★ Mengen ausrechnen
<span class="anker" id="aufg-1"></span>

<ol class="al">

<li>

Berechne im Rechenmodell $(A\cup B)^c$ und $A\setminus(A\cap B)$.

</li>

<li>

Zeige mit einer Element-Tafel: $(A\setminus B)\cup(B\setminus A)=(A\cup B)\setminus(A\cap B)$.

</li>

<li>

Wie viele Elemente hat $\mathcal P(A\cap B)$? Sage voraus, wie viele $\mathcal P(M)$ hat, wenn $M$ genau $n$ Elemente hat, und begründe es.

</li>

</ol>

:::loesung
(a) $A\cup B=\{1,2,3,4,5,6,7,11,12\}$, also $(A\cup B)^c=\{8,9,10\}$. $A\setminus(A\cap B)=A\setminus\{2,3\}=\{1,4,6,12\}$, das ist $A\setminus B$. (b) Für die Fälle $(\in,\in)$, $(\in,\notin)$, $(\notin,\in)$, $(\notin,\notin)$ von $x$ in $A$, $B$ liefern beide Seiten $\notin,\in,\in,\notin$: $x$ liegt darin, wenn es in genau einer der Mengen liegt. (c) $A\cap B=\{2,3\}$ hat 2 Elemente, $\mathcal P(A\cap B)$ hat $2^2=4$. Bei $n$ Elementen entscheidet man für jedes einzeln: drin oder nicht. Das sind $2^n$ Teilmengen.
:::
:::

:::aufgabe Aufgabe 2 ★★ Schließen mit Tafeln
<span class="anker" id="aufg-2"></span>

<ol class="al">

<li>

Zeige die Transitivität der Implikation mit einer Tafel aus acht Zeilen.

</li>

<li>

Wenn die Sicherung ganz ist ($\mathcal A$), leuchtet die Lampe ($\mathcal B$). Diese Implikation ist wahr, und die Lampe leuchtet nicht. Was folgt für die Sicherung? Und wenn die Lampe leuchtet?

</li>

<li>

Ist $(\mathcal A\Rightarrow\mathcal B)\Leftrightarrow(\mathcal B\Rightarrow\mathcal A)$ eine Tautologie?

</li>

</ol>

:::loesung
(a) Die Voraussetzung $(\mathcal A\Rightarrow\mathcal B)\wedge(\mathcal B\Rightarrow\mathcal C)$ ist nur für $(\mathcal A,\mathcal B,\mathcal C)=(w,w,w)$, $(f,w,w)$, $(f,f,w)$, $(f,f,f)$ wahr. In allen vier ist $\mathcal A\Rightarrow\mathcal C$ wahr. In den übrigen vier Zeilen ist sie falsch, die Gesamtaussage also wahr. (b) Kontraposition: $\neg\mathcal B\Rightarrow\neg\mathcal A$, die Sicherung ist nicht ganz. Leuchtet die Lampe, folgt nichts: Die Zeile $f\Rightarrow w$ ist erlaubt. (c) Nein: Für $\mathcal A=w$, $\mathcal B=f$ ist links $f\Leftrightarrow w$, also falsch.
:::
:::

::::formelsammlung
**Element**

$$x\in M,\qquad x\notin M$$

„$x$ ist Element von $M$“ bzw. das Gegenteil. Eine Menge ist eine ungeordnete Zusammenfassung bestimmter, wohlunterscheidbarer Objekte, ihrer Elemente.

**Teilmenge und Gleichheit**

$$A\subset B,\qquad A=B$$

$A\subset B$: Jedes Element von $A$ liegt in $B$, also für alle $x$: $(x\in A)\Rightarrow(x\in B)$; $A=B$ ist erlaubt. $B\supset A$: $B$ ist Obermenge von $A$. $A=B$ heißt $A\subset B$ und $B\subset A$, also für alle $x$: $(x\in A)\Leftrightarrow(x\in B)$.

**Vereinigung, Durchschnitt, Differenz**

$$A\cup B,\qquad A\cap B,\qquad A\setminus B$$

$x\in A\cup B$ heißt $(x\in A)\vee(x\in B)$, auch in beiden; $x\in A\cap B$ heißt $(x\in A)\wedge(x\in B)$; $x\in A\setminus B$ heißt $(x\in A)\wedge(x\notin B)$.

**Komplement, leere Menge, Potenzmenge**

$$A^c,\qquad\emptyset=\{\,\},\qquad\mathcal P(A)$$

$A^c$: alle Elemente einer festen Obermenge, die nicht in $A$ liegen. $\emptyset$ enthält kein Element. $\mathcal P(A)$ ist die Menge aller Teilmengen von $A$; hat $A$ genau $n$ Elemente, hat $\mathcal P(A)$ genau $2^n$. $A$ und $B$ heißen disjunkt, wenn $A\cap B=\emptyset$.

**Regeln mit leerer Menge und Differenz**

$$\emptyset\subset A,\qquad A\cup\emptyset=A,\qquad A\cap\emptyset=\emptyset,\qquad A\setminus B=A\cap B^c$$

Für jede Menge $A$; die letzte Regel für Mengen $A$, $B$ in einer festen Obermenge.

**Wahrheitstafel der Verknüpfungen**

$$\begin{array}{cc|ccccc}\mathcal A&\mathcal B&\neg\mathcal A&\mathcal A\vee\mathcal B&\mathcal A\wedge\mathcal B&\mathcal A\Rightarrow\mathcal B&\mathcal A\Leftrightarrow\mathcal B\\\hline w&w&f&w&w&w&w\\w&f&f&w&f&f&f\\f&w&w&w&f&w&f\\f&f&w&f&f&w&w\end{array}$$

Negation („nicht“), Disjunktion („oder“, schließt „beide“ ein), Konjunktion („und“), Implikation („wenn, dann“), Äquivalenz („genau dann, wenn“). $\neg$ bindet am stärksten. $\mathcal A\Rightarrow\mathcal B$ ist nur bei $w\Rightarrow f$ falsch.

**Implikation und Äquivalenz umschreiben**

$$(\mathcal A\Rightarrow\mathcal B)\Leftrightarrow(\neg\mathcal A\vee\mathcal B),\qquad(\mathcal A\Leftrightarrow\mathcal B)\Leftrightarrow\bigl((\mathcal A\Rightarrow\mathcal B)\wedge(\mathcal B\Rightarrow\mathcal A)\bigr)$$

Zwei Aussagen mit derselben Tafelspalte sind äquivalent. Eine Tautologie ist eine Aussage, die für alle Wahrheitswerte ihrer Bausteine wahr ist; die folgenden Regeln sind Tautologien bzw. gelten für Mengen in einer Obermenge $G$.

**Doppelte Verneinung und Idempotenz**

$$(A^c)^c=A,\qquad\neg(\neg\mathcal A)\Leftrightarrow\mathcal A,\qquad A\cup A=A,\qquad A\cap A=A$$

Für Aussagen ebenso $(\mathcal A\vee\mathcal A)\Leftrightarrow\mathcal A$ und $(\mathcal A\wedge\mathcal A)\Leftrightarrow\mathcal A$.

**Kommutativ- und Assoziativgesetze**

$$A\cap B=B\cap A,\qquad A\cup B=B\cup A,\qquad(A\cap B)\cap C=A\cap(B\cap C)$$

Das Assoziativgesetz ebenso mit $\cup$; für Aussagen mit $\wedge$ und $\vee$, etwa $(\mathcal A\wedge\mathcal B)\Leftrightarrow(\mathcal B\wedge\mathcal A)$ und $(\mathcal A\wedge(\mathcal B\wedge\mathcal C))\Leftrightarrow((\mathcal A\wedge\mathcal B)\wedge\mathcal C)$.

**Distributivgesetze für Mengen**

$$A\cap(B\cup C)=(A\cap B)\cup(A\cap C),\qquad A\cup(B\cap C)=(A\cup B)\cap(A\cup C)$$

Für beliebige Mengen $A$, $B$, $C$.

**Distributivgesetze für Aussagen**

$$(\mathcal A\wedge(\mathcal B\vee\mathcal C))\Leftrightarrow((\mathcal A\wedge\mathcal B)\vee(\mathcal A\wedge\mathcal C))$$

Ebenso mit vertauschten Rollen: $(\mathcal A\vee(\mathcal B\wedge\mathcal C))\Leftrightarrow((\mathcal A\vee\mathcal B)\wedge(\mathcal A\vee\mathcal C))$.

**De-Morgan-Regeln für Mengen**

$$(A\cap B)^c=A^c\cup B^c,\qquad(A\cup B)^c=A^c\cap B^c$$

Beweis mit einer Element-Tafel: alle vier Fälle durchgehen, wie ein Element zu $A$ und $B$ liegen kann.

**De-Morgan-Regeln für Aussagen**

$$\neg(\mathcal A\wedge\mathcal B)\Leftrightarrow(\neg\mathcal A\vee\neg\mathcal B),\qquad\neg(\mathcal A\vee\mathcal B)\Leftrightarrow(\neg\mathcal A\wedge\neg\mathcal B)$$

Beweis mit einer Wahrheitstafel. Beim Verneinen wird Und zu Oder und umgekehrt.

**Implikation für Mengen**

$$A\subset B\Leftrightarrow A^c\cup B=G$$

$G$ ist die Obermenge; das Gegenstück zu $(\mathcal A\Rightarrow\mathcal B)\Leftrightarrow(\neg\mathcal A\vee\mathcal B)$.

**Kontraposition**

$$(\mathcal A\Rightarrow\mathcal B)\Leftrightarrow(\neg\mathcal B\Rightarrow\neg\mathcal A),\qquad A\subset B\Leftrightarrow B^c\subset A^c$$

Beweismittel: Statt „$n^2$ gerade $\Rightarrow$ $n$ gerade“ zeigt man „$n$ ungerade $\Rightarrow$ $n^2$ ungerade“.

**Transitivität**

$$((\mathcal A\Rightarrow\mathcal B)\wedge(\mathcal B\Rightarrow\mathcal C))\Rightarrow(\mathcal A\Rightarrow\mathcal C),\qquad(A\subset B\wedge B\subset C)\Rightarrow A\subset C$$

Die Transitivität der Inklusion folgt aus der der Implikation: Aus $x\in A$ folgt $x\in B$, daraus $x\in C$.
::::

::::lernkarten
:::karte begriff Menge und Elemente
Was ist eine Menge, und was bedeutet die Schreibweise $x\in M$?
---
Eine ungeordnete Zusammenfassung bestimmter, wohlunterscheidbarer Objekte, ihrer Elemente. $x\in M$ heißt „$x$ ist Element von $M$“, $x\notin M$ das Gegenteil.
--- falsch
Eine geordnete Liste von Objekten, in der jedes Objekt mehrfach vorkommen darf. $x\in M$ heißt „$x$ steht an erster Stelle von $M$“, $x\notin M$ das Gegenteil.
--- falsch
Eine ungeordnete Zusammenfassung von Objekten, die auch unbestimmt sein dürfen. $x\in M$ heißt „$M$ ist ein Teil von $x$“, $x\notin M$ das Gegenteil.
--- falsch
Eine Zusammenfassung gleichartiger Zahlen in festgelegter Reihenfolge, ihrer Elemente. $x\in M$ heißt „$x$ ist eine Teilmenge von $M$“.
:::
:::karte begriff Teilmenge und Obermenge
Wann heißt eine Menge $A$ Teilmenge einer Menge $B$, und was bedeutet dann $B\supset A$?
---
$A\subset B$, wenn jedes Element von $A$ in $B$ liegt; $A=B$ ist erlaubt. $B\supset A$ sagt dasselbe von $B$ aus: $B$ ist Obermenge von $A$.
--- falsch
$A\subset B$, wenn jedes Element von $B$ in $A$ liegt; $A=B$ ist erlaubt. $B\supset A$ heißt dann, dass $B$ ganz in $A$ enthalten ist.
--- falsch
$A\subset B$, wenn jedes Element von $A$ in $B$ liegt und $B$ mindestens ein weiteres Element hat; $A=B$ ist ausgeschlossen. $B\supset A$: $B$ ist Obermenge.
--- falsch
$A\subset B$, wenn $A$ und $B$ mindestens ein gemeinsames Element haben. $B\supset A$ heißt, dass sie mindestens ein Element nicht gemeinsam haben.
:::
:::karte formel Gleichheit von Mengen
Wie zeigt man, dass zwei Mengen $A$ und $B$ gleich sind?
---
Man zeigt $A\subset B$ und $B\subset A$. Gleichheit heißt „für alle $x$: $(x\in A)\Leftrightarrow(x\in B)$“; Reihenfolge und Darstellung der Elemente spielen keine Rolle.
--- falsch
Man zeigt, dass beide gleich viele Elemente haben. Mengen mit derselben Anzahl von Elementen sind gleich, auch wenn die Elemente selbst verschieden sind.
--- falsch
Man zeigt $A\subset B$; die Umkehrung $B\subset A$ folgt daraus von selbst, weil die Teilmengenbeziehung immer in beide Richtungen gilt.
--- falsch
Man zeigt, dass ihre Elemente in derselben Reihenfolge aufgezählt werden. Bei anderer Reihenfolge der Elemente sind es verschiedene Mengen.
:::
:::karte begriff Vereinigung und Durchschnitt
Welche Elemente enthalten die Vereinigung $A\cup B$ und der Durchschnitt $A\cap B$?
---
$A\cup B$ enthält alle Elemente, die in $A$ oder in $B$ liegen, auch die in beiden. $A\cap B$ enthält alle Elemente, die in $A$ und in $B$ liegen.
--- falsch
$A\cup B$ enthält alle Elemente, die in genau einer der beiden Mengen liegen. $A\cap B$ enthält alle Elemente, die in $A$ und in $B$ liegen.
--- falsch
$A\cup B$ enthält alle Elemente, die in $A$ und in $B$ liegen. $A\cap B$ enthält alle Elemente, die in $A$ oder in $B$ liegen, auch die in beiden.
--- falsch
$A\cup B$ enthält alle Elemente, die in $A$ oder in $B$ liegen, auch die in beiden. $A\cap B$ enthält alle Elemente von $A$, die nicht in $B$ liegen.
:::
:::karte begriff Differenz und Komplement
Was enthalten die Differenz $A\setminus B$ und das Komplement $A^c$?
---
$A\setminus B$ enthält alle Elemente von $A$, die nicht in $B$ liegen. $A^c$ enthält alle Elemente einer festen Obermenge, die nicht in $A$ liegen; es gilt $A\setminus B=A\cap B^c$.
--- falsch
$A\setminus B$ enthält alle Elemente von $B$, die nicht in $A$ liegen. $A^c$ enthält alle Elemente einer festen Obermenge, die nicht in $A$ liegen; es gilt $A\setminus B=A\cup B^c$.
--- falsch
$A\setminus B$ enthält alle Elemente, die in genau einer der beiden Mengen liegen. $A^c$ enthält alle Elemente, die in $A$ liegen, aber in keiner anderen Menge.
--- falsch
$A\setminus B$ enthält alle Elemente von $A$, die nicht in $B$ liegen. $A^c$ enthält alle Objekte überhaupt, die nicht in $A$ liegen; eine feste Obermenge braucht man dafür nicht.
:::
:::karte begriff leere Menge
Was ist die leere Menge, und in welcher Beziehung steht sie zu jeder anderen Menge $A$?
---
Die Menge $\emptyset=\{\,\}$, die kein Element enthält. Sie ist Teilmenge jeder Menge, $\emptyset\subset A$, und es gilt $A\cup\emptyset=A$ und $A\cap\emptyset=\emptyset$.
--- falsch
Die Menge $\{0\}$, die nur die Null enthält. Sie ist Teilmenge jeder Zahlenmenge, und es gilt $A\cup\{0\}=A$ und $A\cap\{0\}=\{0\}$ für jede Menge $A$.
--- falsch
Die Menge $\emptyset=\{\,\}$, die kein Element enthält. Sie ist Teilmenge keiner anderen Menge, weil sie kein Element mit ihr teilt; außerdem gilt $A\cap\emptyset=A$.
--- falsch
Die Menge $\emptyset=\{\,\}$, die kein Element enthält. Sie ist nur Teilmenge von sich selbst, und es gilt $A\cup\emptyset=\emptyset$ für jede Menge $A$.
:::
:::karte begriff disjunkt
Wann nennt man zwei Mengen $A$ und $B$ disjunkt?
---
Wenn sie kein gemeinsames Element haben, also $A\cap B=\emptyset$ gilt.
--- falsch
Wenn sie keine gemeinsame Obermenge haben, also nicht in derselben Grundmenge liegen.
--- falsch
Wenn ihre Vereinigung leer ist, also $A\cup B=\emptyset$ gilt.
--- falsch
Wenn keine der beiden Mengen Teilmenge der anderen ist, also weder $A\subset B$ noch $B\subset A$ gilt.
:::
:::karte begriff Potenzmenge
Was ist die Potenzmenge $\mathcal P(A)$ einer Menge $A$?
---
Die Menge aller Teilmengen von $A$, einschließlich $\emptyset$ und $A$ selbst. Beispiel: $\mathcal P(\{5,7\})=\{\emptyset,\{5\},\{7\},\{5,7\}\}$.
--- falsch
Die Menge aller Elemente von $A$ und ihrer Quadrate. Beispiel: $\mathcal P(\{5,7\})=\{5,7,25,49\}$, die Elemente mit ihren zweiten Potenzen.
--- falsch
Die Menge aller Teilmengen von $A$ mit genau einem Element. Beispiel: $\mathcal P(\{5,7\})=\{\{5\},\{7\}\}$, ohne $\emptyset$ und ohne $A$.
--- falsch
Die Menge aller nicht leeren Teilmengen von $A$. Beispiel: $\mathcal P(\{5,7\})=\{\{5\},\{7\},\{5,7\}\}$, denn die leere Menge ist keine Teilmenge.
:::
:::karte zusammenhang Anzahl der Teilmengen
Warum hat die Potenzmenge einer Menge mit $n$ Elementen genau $2^n$ Elemente?
---
Weil man für jedes der $n$ Elemente einzeln entscheidet, ob es in der Teilmenge liegt oder nicht. Das sind $n$ Entscheidungen mit je zwei Möglichkeiten, also $2^n$ Teilmengen.
--- falsch
Weil sich die Zahl der Elemente bei jeder Vereinigung zweier Teilmengen verdoppelt. Nach $n$ Vereinigungen, eine für jedes Element, sind es $2^n$.
--- falsch
Weil jede Teilmenge genau zwei Elemente hat und man aus $n$ Elementen auf diese Weise $2^n$ Paare bilden kann; die leere Menge zählt nicht mit.
--- falsch
Weil jedes Element in genau zwei Teilmengen liegt, in der Menge aus ihm allein und in der ganzen Menge. Die Teilmengen verdoppeln sich deshalb mit jedem Element.
:::
:::karte begriff Venn-Diagramm
Was ist ein Venn-Diagramm, und warum ersetzt es keinen Beweis einer Mengenregel?
---
Eine Zeichnung, die Mengen als Flächen darstellt. Sie veranschaulicht nur und zeigt eine mögliche Lage der Mengen; ein Beweis muss alle Fälle erfassen, etwa mit einer Element-Tafel.
--- falsch
Eine Zeichnung, die Mengen als Flächen darstellt. Sie ist ein vollständiger Beweis, wenn die Flächen sauber gezeichnet sind, weil darin jede mögliche Lage der Mengen vorkommt.
--- falsch
Eine Tabelle, die für jedes Element einträgt, in welchen Mengen es liegt. Sie ersetzt keinen Beweis, weil sie nur endlich viele Elemente zeigen kann.
--- falsch
Eine Zeichnung, die Aussagen als Pfeile darstellt. Sie ersetzt keinen Beweis, weil man aus Pfeilen keine Wahrheitswerte ablesen kann.
:::
:::karte begriff Aussage
Was ist eine Aussage im Sinn der Logik, und ist die Frage „Wie spät ist es?“ eine?
---
Eine Behauptung, die nur wahr oder falsch sein kann. „Wie spät ist es?“ ist keine Aussage; „jede gerade Zahl ab 4 ist Summe zweier Primzahlen“ ist eine, obwohl niemand weiß, ob sie wahr ist.
--- falsch
Eine Behauptung, deren Wahrheitswert bekannt ist. „Wie spät ist es?“ ist keine Aussage, und eine unbewiesene Vermutung ist auch keine, solange niemand ihren Wahrheitswert kennt.
--- falsch
Jeder sinnvolle Satz der Sprache. „Wie spät ist es?“ ist eine Aussage, weil die Frage einen klaren Inhalt hat und sich zu jeder Zeit eindeutig beantworten lässt.
--- falsch
Eine Behauptung, die wahr, falsch oder unentschieden sein kann. „Wie spät ist es?“ ist eine Aussage mit dem dritten Wert „unentschieden“, weil sie nichts behauptet.
:::
:::karte begriff Parameter
Was bedeutet es, dass eine Aussage von einem Parameter abhängt?
---
Die Aussage enthält eine Variable, und ihr Wahrheitswert hängt von deren Wert ab: $\mathcal T(n):=(n\text{ teilt }12)$ ist für $n=4$ wahr und für $n=5$ falsch.
--- falsch
Die Aussage ist für alle Werte der Variable wahr: $\mathcal T(n):=(n\text{ teilt }12)$ ist deshalb nur dann eine Aussage, wenn sie für jedes $n$ gilt.
--- falsch
Die Aussage ist für genau einen Wert der Variable wahr und für alle anderen falsch: $\mathcal T(n):=(n\text{ teilt }12)$ ist nur für $n=12$ wahr.
--- falsch
Die Aussage hängt von einer festen Zahl ab, die ihren Wahrheitswert nicht beeinflusst: $\mathcal T(n):=(n\text{ teilt }12)$ ist für jedes $n$ wahr.
:::
:::karte begriff Wahrheitstafel
Was ist eine Wahrheitstafel, mit der man die Verknüpfungen von Aussagen festlegt?
---
Eine Tabelle, die für jede Kombination der Wahrheitswerte $w$ und $f$ der Bausteine den Wahrheitswert der verknüpften Aussage angibt. Bei zwei Bausteinen hat sie vier Zeilen.
--- falsch
Eine Tabelle, die für jede Aussage festhält, ob sie schon bewiesen ist. Bei zwei Bausteinen hat sie zwei Zeilen, eine für jeden der beiden Bausteine.
--- falsch
Eine Tabelle, die für jede Kombination der Wahrheitswerte $w$ und $f$ der Bausteine den Wahrheitswert der verknüpften Aussage angibt. Bei zwei Bausteinen hat sie zwei Zeilen.
--- falsch
Eine Liste der wahren Aussagen eines Gebiets, aus der man durch Nachschlagen entscheidet, ob eine neue Aussage wahr ist. Falsche Aussagen stehen nicht darin.
:::
:::karte begriff Negation
Wann ist die Negation $\neg\mathcal A$ wahr, und wie stark bindet das Zeichen $\neg$?
---
$\neg\mathcal A$ („nicht $\mathcal A$“) ist genau dann wahr, wenn $\mathcal A$ falsch ist. $\neg$ bindet am stärksten: $\neg\mathcal A\vee\mathcal B$ heißt $(\neg\mathcal A)\vee\mathcal B$.
--- falsch
$\neg\mathcal A$ („nicht $\mathcal A$“) ist genau dann wahr, wenn $\mathcal A$ falsch ist. $\neg$ bindet am schwächsten: $\neg\mathcal A\vee\mathcal B$ heißt $\neg(\mathcal A\vee\mathcal B)$.
--- falsch
$\neg\mathcal A$ („nicht $\mathcal A$“) ist immer falsch, weil es das Gegenteil einer Aussage behauptet. $\neg$ bindet am stärksten: $\neg\mathcal A\vee\mathcal B$ heißt $(\neg\mathcal A)\vee\mathcal B$.
--- falsch
$\neg\mathcal A$ („nicht $\mathcal A$“) ist genau dann wahr, wenn $\mathcal A$ wahr ist; es betont die Aussage nur. $\neg$ bindet am stärksten, wie ein Vorzeichen.
:::
:::karte begriff Konjunktion und Disjunktion
Wann sind die Konjunktion $\mathcal A\wedge\mathcal B$ und die Disjunktion $\mathcal A\vee\mathcal B$ wahr?
---
$\mathcal A\wedge\mathcal B$ („und“) ist nur wahr, wenn beide Aussagen wahr sind. $\mathcal A\vee\mathcal B$ („oder“) ist wahr, wenn mindestens eine wahr ist; „oder“ schließt „beide“ ein.
--- falsch
$\mathcal A\wedge\mathcal B$ („und“) ist nur wahr, wenn beide Aussagen wahr sind. $\mathcal A\vee\mathcal B$ („oder“) ist wahr, wenn genau eine wahr ist; sind beide wahr, ist sie falsch.
--- falsch
$\mathcal A\wedge\mathcal B$ („und“) ist wahr, wenn mindestens eine der beiden Aussagen wahr ist. $\mathcal A\vee\mathcal B$ („oder“) ist nur wahr, wenn beide wahr sind.
--- falsch
$\mathcal A\wedge\mathcal B$ („und“) ist wahr, wenn beide Aussagen denselben Wahrheitswert haben. $\mathcal A\vee\mathcal B$ („oder“) ist wahr, wenn sie verschiedene Wahrheitswerte haben.
:::
:::karte begriff Implikation
In welchem einzigen Fall ist die Implikation $\mathcal A\Rightarrow\mathcal B$ falsch?
---
Nur wenn $\mathcal A$ wahr und $\mathcal B$ falsch ist. Ist $\mathcal A$ falsch, ist $\mathcal A\Rightarrow\mathcal B$ wahr und sagt nichts über $\mathcal B$; gleichwertig ist $\neg\mathcal A\vee\mathcal B$.
--- falsch
Wenn $\mathcal A$ falsch ist, gleich welchen Wert $\mathcal B$ hat: Aus etwas Falschem folgt nichts, deshalb ist die Implikation dann falsch; gleichwertig ist $\mathcal A\wedge\mathcal B$.
--- falsch
Wenn $\mathcal A$ und $\mathcal B$ verschiedene Wahrheitswerte haben, also bei $w\Rightarrow f$ und bei $f\Rightarrow w$; gleichwertig ist dann die Äquivalenz $\mathcal A\Leftrightarrow\mathcal B$.
--- falsch
Nur wenn $\mathcal A$ falsch und $\mathcal B$ wahr ist. Ist $\mathcal A$ wahr, ist $\mathcal A\Rightarrow\mathcal B$ immer wahr und sagt nichts über $\mathcal B$; gleichwertig ist $\mathcal A\vee\neg\mathcal B$.
:::
:::karte zusammenhang Implikation mit falscher Voraussetzung
Warum ist eine Implikation mit falscher Voraussetzung, also $f\Rightarrow w$ oder $f\Rightarrow f$, wahr?
---
Weil ein falsches $\mathcal A$ nichts über $\mathcal B$ sagt, die Implikation also nicht verletzt ist. Die Festlegung ist erzwungen: $\mathcal E(n):=(n\ge7\Rightarrow n>5)$ soll für alle $n$ wahr sein, und $n=6$ liefert $f\Rightarrow w$.
--- falsch
Weil eine falsche Voraussetzung die Folgerung automatisch wahr macht: Aus $f$ folgt immer $w$. Deshalb ist $f\Rightarrow f$ eigentlich falsch und nur der Einfachheit halber als wahr festgelegt worden.
--- falsch
Weil man Implikationen mit falscher Voraussetzung nicht prüfen kann und sie deshalb vorsichtshalber als wahr zählt. Die Festlegung ist willkürlich und hätte genauso gut anders ausfallen können.
--- falsch
Weil $\mathcal A\Rightarrow\mathcal B$ dasselbe bedeutet wie $\mathcal B\Rightarrow\mathcal A$: Bei $f\Rightarrow w$ gilt umgekehrt $w\Rightarrow f$, und auch diese Zeile ist nach der Wahrheitstafel wahr.
:::
:::karte zusammenhang Implikation als Teilmengenbeziehung
Warum sagt eine für alle $n$ wahre Implikation wie $\mathcal E(n):=(n\ge7\Rightarrow n>5)$ dasselbe wie eine Teilmengenbeziehung?
---
Weil nur die Zeile $w\Rightarrow f$ die Implikation verletzt und sie für kein $n$ vorkommt: Jedes $n$ mit $n\ge7$ erfüllt $n>5$. Also liegt $\{n\ge7\}$ in $\{n>5\}$.
--- falsch
Weil beide Seiten dieselbe Menge beschreiben: Jedes $n$ mit $n\ge7$ erfüllt $n>5$, und jedes $n$ mit $n>5$ erfüllt $n\ge7$. Also ist $\{n\ge7\}=\{n>5\}$.
--- falsch
Weil die Implikation festlegt, dass $\{n>5\}$ in $\{n\ge7\}$ liegt: Die Folgerung beschreibt immer die kleinere Menge, die Voraussetzung die größere.
--- falsch
Weil die Implikation auch $f\Rightarrow w$ ausschließt: Kein $n$ erfüllt $n>5$, ohne $n\ge7$ zu erfüllen. Also liegt $\{n>5\}$ ganz in $\{n\ge7\}$.
:::
:::karte begriff Äquivalenz
Wann ist die Äquivalenz $\mathcal A\Leftrightarrow\mathcal B$ wahr, und wann heißen zwei Aussagen äquivalent?
---
$\mathcal A\Leftrightarrow\mathcal B$ ist wahr, wenn $\mathcal A$ und $\mathcal B$ denselben Wahrheitswert haben; gleichbedeutend ist $(\mathcal A\Rightarrow\mathcal B)\wedge(\mathcal B\Rightarrow\mathcal A)$. Zwei Aussagen mit derselben Tafelspalte heißen äquivalent.
--- falsch
$\mathcal A\Leftrightarrow\mathcal B$ ist wahr, wenn beide Aussagen wahr sind; gleichbedeutend ist $\mathcal A\wedge\mathcal B$. Zwei Aussagen heißen äquivalent, wenn beide schon bewiesen sind und dasselbe besagen.
--- falsch
$\mathcal A\Leftrightarrow\mathcal B$ ist wahr, wenn $\mathcal A$ und $\mathcal B$ verschiedene Wahrheitswerte haben. Zwei Aussagen heißen äquivalent, wenn sich ihre Tafelspalten in jeder Zeile unterscheiden.
--- falsch
$\mathcal A\Leftrightarrow\mathcal B$ ist wahr, wenn $\mathcal A\Rightarrow\mathcal B$ wahr ist; die Umkehrung muss nicht gelten. Zwei Aussagen heißen äquivalent, wenn eine von ihnen aus der anderen folgt.
:::
:::karte begriff Tautologie
Was versteht man unter einer Tautologie, wie sie die Rechenregeln für Aussagen bilden?
---
Eine Aussage, die für alle Wahrheitswerte ihrer Bausteine wahr ist. Beispiel: $(\mathcal A\Rightarrow\mathcal B)\Leftrightarrow(\neg\mathcal B\Rightarrow\neg\mathcal A)$; in jeder Zeile der Tafel steht $w$.
--- falsch
Eine Aussage, die für mindestens eine Belegung ihrer Bausteine wahr ist. Beispiel: $\mathcal A\wedge\mathcal B$, das für $\mathcal A$ und $\mathcal B$ wahr ebenfalls wahr ist.
--- falsch
Eine Aussage, die für alle Wahrheitswerte ihrer Bausteine falsch ist. Beispiel: $\mathcal A\wedge\neg\mathcal A$; in jeder Zeile der Tafel steht $f$.
--- falsch
Eine Aussage, die zufällig wahr ist, weil ihre Bausteine wahr sind. Beispiel: „2 ist eine Primzahl, und 3 ist eine Primzahl“.
:::
:::karte formel De-Morgan-Regeln
Wie lauten die De-Morgan-Regeln für Mengen und für Aussagen?
---
$(A\cap B)^c=A^c\cup B^c$ und $(A\cup B)^c=A^c\cap B^c$; für Aussagen $\neg(\mathcal A\wedge\mathcal B)\Leftrightarrow(\neg\mathcal A\vee\neg\mathcal B)$ und $\neg(\mathcal A\vee\mathcal B)\Leftrightarrow(\neg\mathcal A\wedge\neg\mathcal B)$. Beim Verneinen wird Und zu Oder und umgekehrt.
--- falsch
$(A\cap B)^c=A^c\cap B^c$ und $(A\cup B)^c=A^c\cup B^c$; für Aussagen $\neg(\mathcal A\wedge\mathcal B)\Leftrightarrow(\neg\mathcal A\wedge\neg\mathcal B)$ und $\neg(\mathcal A\vee\mathcal B)\Leftrightarrow(\neg\mathcal A\vee\neg\mathcal B)$. Die Verneinung wird auf jeden Baustein verteilt, die Verknüpfung bleibt.
--- falsch
$(A\cap B)^c=A\cup B$ und $(A\cup B)^c=A\cap B$; für Aussagen $\neg(\mathcal A\wedge\mathcal B)\Leftrightarrow(\mathcal A\vee\mathcal B)$ und $\neg(\mathcal A\vee\mathcal B)\Leftrightarrow(\mathcal A\wedge\mathcal B)$. Beim Verneinen wird nur die Verknüpfung getauscht, die Bausteine bleiben.
--- falsch
$(A\cap B)^c=A^c\cup B^c$ und $(A\cup B)^c=A^c\cap B^c$; die Regeln gelten aber nur für Mengen, weil sich Aussagen nicht als Flächen zeichnen lassen und es für sie deshalb kein Gegenstück gibt.
:::
:::karte formel Kontraposition
Was besagt die Kontraposition, und wie nutzt man sie als Beweismittel?
---
$(\mathcal A\Rightarrow\mathcal B)\Leftrightarrow(\neg\mathcal B\Rightarrow\neg\mathcal A)$, für Mengen $A\subset B\Leftrightarrow B^c\subset A^c$. Statt „$n^2$ gerade $\Rightarrow$ $n$ gerade“ zeigt man „$n$ ungerade $\Rightarrow$ $n^2$ ungerade“.
--- falsch
$(\mathcal A\Rightarrow\mathcal B)\Leftrightarrow(\mathcal B\Rightarrow\mathcal A)$, für Mengen $A\subset B\Leftrightarrow B\subset A$. Statt „$n^2$ gerade $\Rightarrow$ $n$ gerade“ zeigt man „$n$ gerade $\Rightarrow$ $n^2$ gerade“.
--- falsch
$(\mathcal A\Rightarrow\mathcal B)\Leftrightarrow(\neg\mathcal A\Rightarrow\neg\mathcal B)$, für Mengen $A\subset B\Leftrightarrow A^c\subset B^c$. Statt „$n^2$ gerade $\Rightarrow$ $n$ gerade“ zeigt man „$n^2$ ungerade $\Rightarrow$ $n$ ungerade“.
--- falsch
$(\mathcal A\Rightarrow\mathcal B)\Leftrightarrow(\neg\mathcal B\Rightarrow\neg\mathcal A)$; sie gilt aber nur für Aussagen über endlich viele Zahlen. Für Aussagen über alle $n\in\mathbb{N}$ braucht man stattdessen genügend viele Beispiele.
:::
:::karte zusammenhang Mengen und Aussagen
Warum gelten für Mengen und für Aussagen dieselben Rechenregeln?
---
Weil jede Mengenbeziehung eine Aussage über Elemente ist: $x\in A\cap B$ heißt $(x\in A)\wedge(x\in B)$, $x\in A\cup B$ heißt $(x\in A)\vee(x\in B)$, $A\subset B$ heißt „für alle $x$: $(x\in A)\Rightarrow(x\in B)$“.
--- falsch
Weil Mengen und Aussagen dasselbe sind: Jede Menge ist eine Aussage, die wahr ist, wenn die Menge Elemente hat, und falsch, wenn sie leer ist. Deshalb übertragen sich alle Regeln.
--- falsch
Weil man die Regeln für Mengen mit Venn-Diagrammen beweist und sich die Diagramme auf Aussagen übertragen lassen, indem man die Flächen als Wahrheitswerte liest.
--- falsch
Weil die Regeln für beide getrennt als Axiome festgelegt sind. Dass sie für Mengen und Aussagen gleich ausfallen, ist eine Vereinbarung, die man auch anders treffen könnte.
:::
:::karte begriff Element-Tafel
Was ist eine Element-Tafel, mit der man Regeln für Mengen beweist?
---
Eine Wahrheitstafel, in der man $w$ als „$x$ liegt in der Menge“ und $f$ als „$x$ liegt nicht darin“ liest. Sie geht alle Fälle durch, wie ein Element zu den beteiligten Mengen liegen kann.
--- falsch
Eine Tabelle, die alle Elemente der Obermenge aufzählt und für jedes einzeln einträgt, in welchen Mengen es liegt. Für unendliche Mengen ist sie deshalb nicht anwendbar.
--- falsch
Eine Wahrheitstafel, in der man $w$ als „die Menge ist nicht leer“ und $f$ als „die Menge ist leer“ liest. Sie zeigt, welche der beteiligten Mengen Elemente haben.
--- falsch
Ein Venn-Diagramm mit eingetragenen Elementen, das eine mögliche Lage der Mengen zeigt. Es beweist die Regel für genau diese eine Lage der Mengen.
:::
:::karte herleitung De Morgan per Wahrheitstafel
Wie beweist man die Regel $\neg(\mathcal A\wedge\mathcal B)\Leftrightarrow(\neg\mathcal A\vee\neg\mathcal B)$ mit einer Wahrheitstafel, und wie überträgt man sie auf Mengen?
---
Man schreibt die vier Fälle $ww$, $wf$, $fw$, $ff$ für $\mathcal A$ und $\mathcal B$ auf, weil jede Aussage nur wahr oder falsch sein kann und es bei zwei Bausteinen genau diese Kombinationen gibt.
---
Man berechnet die Spalten $\neg\mathcal A$ und $\neg\mathcal B$ und daraus $\neg(\mathcal A\wedge\mathcal B)$ und $\neg\mathcal A\vee\neg\mathcal B$, weil die Wahrheitstafel der Verknüpfungen jeden dieser Werte festlegt.
---
Beide Spalten lauten $f,w,w,w$; die beiden Seiten sind also äquivalent und die Regel eine Tautologie, weil Aussagen mit derselben Tafelspalte äquivalent sind.
---
Liest man $w$ als „$x$ liegt in der Menge“, ist dieselbe Tafel eine Element-Tafel für $(A\cap B)^c=A^c\cup B^c$, weil $x\in A\cap B$ dasselbe heißt wie $(x\in A)\wedge(x\in B)$.
:::
::::
