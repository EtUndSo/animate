---
title: Zufall und Ereignisse
pfad: Informatik / Machine Learning / Mathematische Grundlagen / Wahrscheinlichkeit
adresse: informatik/machine-learning/mathematische-grundlagen/wahrscheinlichkeit
knoten: Kapitel 4: Wahrscheinlichkeit
nachschlagen: ja
order: 15240200
summary: Bevor man mit Unsicherheit rechnen kann, muss man aufschreiben, was alles geschehen kann.
tags: Menge, Elemente, leere Menge, Teilmenge, Vereinigung, Schnitt, Komplement, disjunkt
lang: de
---

<span class="anker" id="stufe-1"></span>

:::zweck
Bevor man mit Unsicherheit rechnen kann, muss man aufschreiben, was alles geschehen kann. Dieser Abschnitt stellt dafür die Sprache der Mengen bereit und führt drei Grundbegriffe ein: den Vorgang mit ungewissem Ausgang, die Menge aller möglichen Ausgänge und die Aussagen über den Ausgang, deren Wahrscheinlichkeit man später wissen will.
:::

### Was du dafür brauchst: Mengen

<span class="anker" id="stufe-1-1"></span>

Eine __Menge__ ist eine Zusammenfassung von Dingen. Diese Dinge heißen ihre __Elemente__. Man schreibt sie mit geschweiften Klammern, etwa $A=\{2,\,4,\,6\}$, und schreibt $4\in A$ für „$4$ ist Element von $A$“ und $5\notin A$ für das Gegenteil. Auf die Reihenfolge und auf Wiederholungen kommt es nicht an: $\{2,4,6\}$ und $\{6,2,4,2\}$ sind dieselbe Menge. Die Menge ohne Elemente heißt __leere Menge__ und wird $\emptyset$ geschrieben. Für eine endliche Menge $A$ bezeichnet $\#A$ die Anzahl ihrer Elemente, hier $\#A=3$.

$A$ heißt __Teilmenge__ von $B$, geschrieben $A\subseteq B$, wenn jedes Element von $A$ auch in $B$ liegt. Aus zwei Mengen entstehen neue:

<ul>

<li>

die __Vereinigung__ $A\cup B$: alle Elemente, die in $A$ oder in $B$ liegen, auch in beiden;

</li>

<li>

der __Schnitt__ $A\cap B$: alle Elemente, die in $A$ und in $B$ liegen;

</li>

<li>

das __Komplement__ $A^{\mathrm c}$ bezüglich einer festen Grundmenge $\Omega$: alle Elemente von $\Omega$, die nicht in $A$ liegen.

</li>

</ul>

Zwei Mengen ohne gemeinsames Element heißen __disjunkt__; dann ist $A\cap B=\emptyset$. Vereinigung und Schnitt gibt es auch für viele Mengen $A_1,A_2,\dots$; man schreibt $\bigcup_iA_i$ und $\bigcap_iA_i$. Zwei Regeln werden oft gebraucht, die Regeln von __De Morgan__:

<span class="anker" id="gl-1-1"></span>
$$(A\cup B)^{\mathrm c}=A^{\mathrm c}\cap B^{\mathrm c},\qquad (A\cap B)^{\mathrm c}=A^{\mathrm c}\cup B^{\mathrm c}. \tag{1.1}$$

Die erste sagt: Nicht in $A$ oder $B$ zu liegen heißt, weder in $A$ noch in $B$ zu liegen.

::::beispiel [Rechenbeispiel]
In der Grundmenge $\Omega=\{1,\dots,6\}$ sei $A=\{2,4,6\}$ und $B=\{5,6\}$. Dann ist $A\cup B=\{2,4,5,6\}$, $A\cap B=\{6\}$, $A^{\mathrm c}=\{1,3,5\}$ und $B^{\mathrm c}=\{1,2,3,4\}$. Zur Probe der ersten Regel: $(A\cup B)^{\mathrm c}=\{1,3\}$ und $A^{\mathrm c}\cap B^{\mathrm c}=\{1,3\}$.
::::

⁠**Kurz gesagt:** Vereinigung heißt „oder“, Schnitt heißt „und“, Komplement heißt „nicht“; disjunkte Mengen haben nichts gemeinsam.

### Zufallsexperiment und Ergebnisraum

<span class="anker" id="stufe-1-2"></span>

Ein Würfelwurf, eine Messung mit zufälligem Fehler und die Auswahl der Wohnungen für einen Datensatz haben etwas gemeinsam: Man weiß, welche Ausgänge möglich sind, aber nicht, welcher eintritt. Will man darüber rechnen, schreibt man zuerst alle möglichen Ausgänge auf.

:::definition Definition 1.1 (Zufallsexperiment, Ergebnis, Ergebnisraum)
<span class="anker" id="satz-1-1"></span>

Ein __Zufallsexperiment__ ist ein Vorgang, dessen Ausgang man vorher nicht sicher kennt. Jeder mögliche Ausgang heißt __Ergebnis__. Die Menge aller Ergebnisse heißt __Ergebnisraum__ und wird $\Omega$ geschrieben.
:::

Ein Ergebnis wird oft $\omega$ genannt. Beim Aufschreiben muss jeder mögliche Ausgang genau einem Ergebnis entsprechen: Es darf keines fehlen, und zwei Ergebnisse dürfen nicht gleichzeitig eintreten. Wie fein man unterscheidet, legt man selbst fest. Wer beim Würfeln nur wissen will, ob eine Sechs fällt, kommt mit $\Omega=\{\text{Sechs},\ \text{keine Sechs}\}$ aus.

Es gibt drei Arten von Ergebnisräumen. Ein Würfelwurf hat endlich viele Ergebnisse. Zählt man, wie oft man würfeln muss, bis die erste Sechs fällt, so ist $\Omega=\{1,2,3,\dots\}$: unendlich viele Ergebnisse, die man aber durchnummerieren kann; eine solche Menge heißt __abzählbar unendlich__. Misst man eine Temperatur, so kann im Prinzip jede reelle Zahl herauskommen, und $\Omega=\mathbb{R}$ lässt sich nicht mehr durchnummerieren.

::::beispiel [Rechenbeispiel]
Beim Wurf zweier unterscheidbarer Würfel, eines roten und eines blauen, ist ein Ergebnis ein Paar $(a,\,b)$ aus der Augenzahl $a$ des roten und $b$ des blauen Würfels. Also ist

$$\Omega=\{(a,\,b): a,b\in\{1,\dots,6\}\},\qquad \#\Omega=6\cdot6=36 .$$

Die Ergebnisse $(1,\,2)$ und $(2,\,1)$ sind verschieden: Einmal zeigt der rote Würfel die Eins, einmal der blaue.
::::

⁠**Kurz gesagt:** Ein Zufallsexperiment hat einen ungewissen Ausgang; der Ergebnisraum $\Omega$ ist die Menge aller möglichen Ausgänge.

### Ereignisse

<span class="anker" id="stufe-1-3"></span>

Meist interessiert nicht das genaue Ergebnis, sondern eine Aussage darüber: „Die Augenzahl ist gerade“, „die Temperatur liegt über $30$ Grad“, „das Bauteil ist defekt“. Jede solche Aussage trifft auf manche Ergebnisse zu und auf andere nicht. Man kann sie deshalb durch die Menge der Ergebnisse ersetzen, auf die sie zutrifft.

:::definition Definition 1.2 (Ereignis)
<span class="anker" id="satz-1-2"></span>

Ein __Ereignis__ ist eine Teilmenge $A\subseteq\Omega$ des Ergebnisraums. Das Ereignis $A$ __tritt ein__, wenn das Ergebnis $\omega$ des Experiments in $A$ liegt.
:::

Ein Ereignis mit genau einem Ergebnis, $\{\omega\}$, heißt __Elementarereignis__. $\Omega$ selbst tritt immer ein und heißt __sicheres Ereignis__. Die leere Menge $\emptyset$ tritt nie ein und heißt __unmögliches Ereignis__. Die Mengenoperationen aus Unterabschnitt [1.1](#stufe-1-1) übersetzen die Wörter der Alltagssprache: $A\cup B$ ist „$A$ oder $B$“, $A\cap B$ ist „$A$ und $B$“, und das __Gegenereignis__ $A^{\mathrm c}$ ist „nicht $A$“. Disjunkte Ereignisse heißen __unvereinbar__: Sie können nicht zusammen eintreten.

::::beispiel [Rechenbeispiel]
Beim Würfelwurf ist $\Omega=\{1,\dots,6\}$. „Gerade Augenzahl“ ist $A=\{2,4,6\}$, „mindestens fünf“ ist $B=\{5,6\}$. Das Ereignis „gerade und mindestens fünf“ ist $A\cap B=\{6\}$, „gerade oder mindestens fünf“ ist $A\cup B=\{2,4,5,6\}$, „ungerade“ ist $A^{\mathrm c}=\{1,3,5\}$. Die Ereignisse $\{1\}$ und $\{2\}$ sind unvereinbar; $A$ und $B$ sind es nicht, denn beide treten ein, wenn die Sechs fällt.
::::

⁠**Kurz gesagt:** Ein Ereignis ist die Menge der Ergebnisse, auf die eine Aussage zutrifft; „oder“, „und“ und „nicht“ werden zu Vereinigung, Schnitt und Komplement.

:::hintergrund Welche Teilmengen sind Ereignisse?
Bei endlichem oder abzählbar unendlichem $\Omega$ darf jede Teilmenge ein Ereignis sein. Bei $\Omega=[0,\,1]$ geht das nicht mehr: Man kann beweisen, dass es keine Wahrscheinlichkeit gibt, die allen Teilmengen von $[0,\,1]$ einen Wert zuweist, jedem Teilintervall seine Länge gibt, verschobene Mengen gleich behandelt und die Rechenregeln aus Abschnitt [2](wahrscheinlichkeit-2.html#stufe-2) erfüllt. Die Teilmengen, für die das schiefgeht, sind so verwickelt, dass man sie nicht hinschreiben kann; man braucht zu ihrer Konstruktion ein eigenes Axiom der Mengenlehre, das Auswahlaxiom. Die Theorie beschränkt sich deshalb auf eine Auswahl von Teilmengen, die alle Intervalle enthält und unter Komplement und abzählbaren Vereinigungen abgeschlossen ist. Alle Mengen, die in der Praxis vorkommen, gehören dazu, und dieses Kapitel braucht die Einschränkung nirgends.
:::

:::aufgabe Aufgabe 1 ★ Ereignisse beim Wurf zweier Würfel
<span class="anker" id="aufg-1"></span>

Ein roter und ein blauer Würfel werden geworfen. Es sei $A$ = „die Augensumme ist $7$“ und $B$ = „der rote Würfel zeigt die Sechs“.

<ol class="al">

<li>

Schreibe $A$, $B$ und $A\cap B$ als Mengen von Paaren und gib ihre Anzahlen an.

</li>

<li>

Wie viele Ergebnisse hat $A\cup B$? Erkläre, warum $\#(A\cup B)=\#A+\#B-\#(A\cap B)$ gilt.

</li>

<li>

Sind $A$ und das Ereignis „die Augensumme ist $8$“ unvereinbar?

</li>

</ol>

:::loesung
(a) $A=\{(1,6),(2,5),(3,4),(4,3),(5,2),(6,1)\}$ mit $6$ Elementen, $B=\{(6,1),(6,2),\dots,(6,6)\}$ mit $6$ Elementen und $A\cap B=\{(6,1)\}$ mit einem Element.

(b) $\#(A\cup B)=6+6-1=11$. Zählt man $\#A+\#B$, so wird jedes Element von $A\cap B$ zweimal gezählt, einmal in $A$ und einmal in $B$; deshalb zieht man es einmal ab. Das ist der Additionssatz aus Unterabschnitt [2.3](wahrscheinlichkeit-2.html#stufe-2-3) in der Form für Anzahlen.

(c) Ja. Ein Paar hat nur eine Augensumme; es kann nicht zugleich die Summe $7$ und die Summe $8$ haben. Die beiden Ereignisse sind disjunkt.
:::
:::

:::aufgabe Aufgabe 2 ★★ Aussagen als Mengen
<span class="anker" id="aufg-2"></span>

Ein Gerät hat drei Baugruppen. $A_k$ sei das Ereignis „Baugruppe $k$ fällt aus“, $k=1,2,3$.

<ol class="al">

<li>

Drücke mit Vereinigung, Schnitt und Komplement aus: „mindestens eine fällt aus“, „keine fällt aus“, „alle drei fallen aus“, „genau Baugruppe $1$ fällt aus“.

</li>

<li>

Zeige mit den Regeln von De Morgan, dass „nicht mindestens eine fällt aus“ dasselbe Ereignis ist wie „keine fällt aus“.

</li>

</ol>

:::loesung
(a) „Mindestens eine fällt aus“ ist $A_1\cup A_2\cup A_3$. „Keine fällt aus“ ist $A_1^{\mathrm c}\cap A_2^{\mathrm c}\cap A_3^{\mathrm c}$. „Alle drei fallen aus“ ist $A_1\cap A_2\cap A_3$. „Genau Baugruppe $1$ fällt aus“ ist $A_1\cap A_2^{\mathrm c}\cap A_3^{\mathrm c}$.

(b) Zweimal die erste Regel von De Morgan: $(A_1\cup A_2\cup A_3)^{\mathrm c}=\bigl((A_1\cup A_2)\cup A_3\bigr)^{\mathrm c}=(A_1\cup A_2)^{\mathrm c}\cap A_3^{\mathrm c}=A_1^{\mathrm c}\cap A_2^{\mathrm c}\cap A_3^{\mathrm c}$. Das Gegenteil von „mindestens eine“ ist „keine“.
:::
:::
