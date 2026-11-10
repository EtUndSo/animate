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
