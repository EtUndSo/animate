---
title: Stufe 1: Ereignisse und Wahrscheinlichkeit
pfad: Elektrotechnik / 3. Semester / HöMa3 – Höhere Mathematik 3 / Wahrscheinlichkeitsrechnung
adresse: elektrotechnik/3-semester/hohere-mathematik-3/wahrscheinlichkeitsrechnung
knoten: Kapitel 8: Wahrscheinlichkeitsrechnung
order: 3180200
summary: Bevor man rechnet, muss feststehen, was passieren kann, welche Fragen zugelassen sind und wie ihnen Zahlen zugeordnet werden.
tags: Zufallsexperiment, Stichprobenraum, Elementarereignis, Ereignis, Ereignisraum, Sigma-Algebra, abzählbar, Potenzmenge
lang: de
---

<span class="anker" id="stufe-1"></span>

:::zweck
Bevor man rechnet, muss feststehen, was passieren kann, welche Fragen zugelassen sind und wie ihnen Zahlen zugeordnet werden. Diese Stufe legt diese drei Dinge fest.
:::

**Die Idee.** Ein __Zufallsexperiment__ ist ein Vorgang, dessen Ausgang vorher offen ist. Alle möglichen Ausgänge bilden den __Stichprobenraum__ $\Omega$, ein einzelner Ausgang $\omega\in\Omega$ heißt __Elementarereignis__. Für die Vierer-Würfel ist $\Omega=\{1,2,3,4\}^2$ mit 16 Paaren. Die Wahl hängt von der Frage ab: Für die Summe reicht $\Omega'=\{2,\dots,8\}$, aber diese sieben Ausgänge sind nicht gleich wahrscheinlich.

Jede Frage mit der Antwort ja oder nein legt eine Teilmenge von $\Omega$ fest: die Ausgänge mit der Antwort ja. Eine solche Teilmenge heißt __Ereignis__. Der Frage „Ist die Summe 5?“ entspricht $A=\{(1,4),(2,3),(3,2),(4,1)\}$, der Antwort nein das Komplement $A^c$ (Abb. [1](#abb-1)).

Die Mengensprache übersetzt sich so: Die Vereinigung $A\cup B$ heißt „$A$ oder $B$ tritt ein“, der Schnitt $A\cap B$ „beide treten ein“, die Differenz $A\setminus B$ „$A$, aber nicht $B$“, das Komplement $A^c=\Omega\setminus A$ „$A$ tritt nicht ein“. $\Omega$ ist das sichere, die leere Menge $\emptyset$ das unmögliche Ereignis. Ist $A\cap B=\emptyset$, heißen $A$ und $B$ disjunkt, sie schließen sich aus. $|A|$ ist die Anzahl der Elemente von $A$. Für eine Folge heißt $\bigcup_iA_i$ „mindestens ein $A_i$ tritt ein“, $\bigcap_iA_i$ „alle treten ein“, und beim Komplement tauschen beide die Rollen (Regel von de Morgan):

<span class="anker" id="gl-1-1"></span>
$$\Bigl(\bigcup_{i\in\mathbb{N}}A_i\Bigr)^c=\bigcap_{i\in\mathbb{N}}A_i^c. \tag{1.1}$$

:::abbildung hm3/k8wuerfel 1
Der Stichprobenraum der Vierer-Würfel als Gitter aus 16 Feldern. $A$ ist „Summe 5“, $B$ ist „erster Würfel mindestens 3“. Der Schnitt $A\cap B$ besteht aus zwei Feldern.
:::

Nicht jede Teilmenge muss als Ereignis zählen. Zeigt ein Messgerät nur an, in welchem von acht Bereichen eine Spannung liegt, sind nur diese Bereiche sinnvolle Fragen, nicht der exakte Wert. Die Menge aller zugelassenen Ereignisse heißt __Ereignisraum__ $\mathcal E$. Er hängt von der Aufgabe ab, muss aber diese Operationen vertragen.

:::definition Definition 1.1 ($\sigma$-Algebra)
<span class="anker" id="satz-1-1"></span>

Sei $\Omega$ eine Menge. Ein System $\mathcal E$ von Teilmengen von $\Omega$ heißt $\sigma$-Algebra oder __Sigma-Algebra__ über $\Omega$, wenn gilt:

<ol class="rm">

<li>

$\Omega\in\mathcal E$.

</li>

<li>

Sind $A,B\in\mathcal E$, so ist auch $A\setminus B\in\mathcal E$.

</li>

<li>

Sind $A_i\in\mathcal E$ für alle $i\in\mathbb{N}$, so ist auch $\bigcup_{i\in\mathbb{N}}A_i\in\mathcal E$.

</li>

</ol>
:::

⁠**So liest man das:** (iii) erlaubt „irgendwann tritt eines der $A_i$ ein“. Das sind abzählbar viele Ereignisse: Eine Menge heißt __abzählbar__, wenn sich ihre Elemente als endliche oder unendliche Folge schreiben lassen, wie bei $\mathbb{N}$, $\mathbb{Z}$ und $\mathbb{Q}$, aber nicht bei $[0,1]$. Alles Weitere folgt aus den drei Regeln:

:::beweis Folgerungen aus den drei Regeln
$\emptyset=\Omega\setminus\Omega\in\mathcal E$ und $A^c=\Omega\setminus A\in\mathcal E$. Setzt man in (iii) $A_1=A$, $A_2=B$, $A_i=\emptyset$ für $i\ge3$, folgt $A\cup B\in\mathcal E$. Zweimal (ii) gibt $A\cap B=A\setminus(A\setminus B)\in\mathcal E$. Mit [(1.1)](#gl-1-1) folgt für eine Folge $\bigcap_iA_i=\bigl(\bigcup_iA_i^c\bigr)^c\in\mathcal E$.
:::

Die größte $\sigma$-Algebra ist die __Potenzmenge__ $\mathcal P(\Omega)$, die Menge aller Teilmengen einschließlich $\emptyset$. Die kleinste ist $\{\emptyset,\Omega\}$.

**Die Wahrscheinlichkeit.** $\mathbb{P}(A)$ soll der Anteil der Fälle sein, in denen $A$ bei sehr vielen Wiederholungen eintritt, die relative Häufigkeit. Anteile sind nicht negativ, der von $\Omega$ ist 1, und die sich ausschließender Ereignisse addieren sich, passend zu (iii) auch für abzählbar viele.

:::definition Definition 1.2 (Wahrscheinlichkeitsmaß)
<span class="anker" id="satz-1-2"></span>

Sei $\mathcal E$ eine $\sigma$-Algebra über $\Omega$. Eine Funktion $\mathbb{P}:\mathcal E\to[0,\infty)$ mit $\mathbb{P}(\Omega)=1$ heißt __Wahrscheinlichkeitsmaß__, wenn sie $\sigma$-__additiv__ ist: Für paarweise disjunkte $A_i\in\mathcal E$ gilt

<span class="anker" id="gl-1-2"></span>
$$\mathbb{P}\Bigl(\bigcup_{i\in\mathbb{N}}A_i\Bigr)=\sum_{i\in\mathbb{N}}\mathbb{P}(A_i). \tag{1.2}$$

Das Tripel $(\Omega,\mathcal E,\mathbb{P})$ heißt __Wahrscheinlichkeitsraum__.
:::

:::satz Satz 1.3 (Rechenregeln)
<span class="anker" id="satz-1-3"></span>

Für Ereignisse $A,B$ gilt:

<ol class="rm">

<li>

$\mathbb{P}(\emptyset)=0$, und $\mathbb{P}$ ist für endlich viele disjunkte Ereignisse additiv.

</li>

<li>

$\mathbb{P}(A^c)=1-\mathbb{P}(A)$ (__Gegenwahrscheinlichkeit__).

</li>

<li>

Aus $A\subset B$ folgt $\mathbb{P}(B\setminus A)=\mathbb{P}(B)-\mathbb{P}(A)$ und damit $\mathbb{P}(A)\le\mathbb{P}(B)$ (__Monotonie__).

</li>

<li>

$\mathbb{P}(A\cup B)=\mathbb{P}(A)+\mathbb{P}(B)-\mathbb{P}(A\cap B)$.

</li>

</ol>
:::

:::beweis Rechenregeln
(i) In [(1.2)](#gl-1-2) mit $A_1=\Omega$ und $A_i=\emptyset$ sonst steht $1=1+\sum_{i\ge2}\mathbb{P}(\emptyset)$. Das geht nur mit $\mathbb{P}(\emptyset)=0$. Füllt man endlich viele Ereignisse mit $\emptyset$ zu einer Folge auf, folgt die endliche Additivität. (ii) $\Omega=A\cup A^c$ ist disjunkt. (iii) $B=A\cup(B\setminus A)$ ist disjunkt, und $\mathbb{P}(B\setminus A)\ge0$. (iv) $A\cup B=A\cup(B\setminus(A\cap B))$ ist disjunkt, und $A\cap B\subset B$.
:::

In (iv) zählt der Schnitt sonst doppelt. In Abb. [1](#abb-1) gibt das $\frac4{16}+\frac8{16}-\frac2{16}=\frac{10}{16}$.

:::satz Satz 1.4 (Stetigkeit von $\mathbb{P}$)
<span class="anker" id="satz-1-4"></span>

Für eine aufsteigende Folge $A_1\subset A_2\subset\dots$ von Ereignissen gilt $\lim_{n\to\infty}\mathbb{P}(A_n)=\mathbb{P}\bigl(\bigcup_{k\in\mathbb{N}}A_k\bigr)$. Für eine absteigende Folge $A_1\supset A_2\supset\dots$ gilt $\lim_{n\to\infty}\mathbb{P}(A_n)=\mathbb{P}\bigl(\bigcap_{k\in\mathbb{N}}A_k\bigr)$.
:::

:::beweis Stetigkeit
Aufsteigend: $B_1=A_1$ und $B_k=A_k\setminus A_{k-1}$ sind disjunkt, ihre Vereinigung bis $n$ ist $A_n$. Aus [(1.2)](#gl-1-2) folgt

$$\mathbb{P}\Bigl(\bigcup_kA_k\Bigr)=\sum_{k=1}^\infty\mathbb{P}(B_k)=\lim_{n\to\infty}\sum_{k=1}^n\mathbb{P}(B_k)=\lim_{n\to\infty}\mathbb{P}(A_n).$$

Absteigend: Die Komplemente $A_n^c$ steigen auf. Die Behauptung folgt mit [(1.1)](#gl-1-1) und Regel (ii).
:::

::::beispiel
Sei $A_n$ „unter den ersten $n$ Würfen eines Vierer-Würfels keine 4“. Dann ist $\mathbb{P}(A_n)=(3/4)^n$, die $A_n$ fallen ab, und ihr Schnitt „nie eine 4“ hat die Wahrscheinlichkeit $\lim_n(3/4)^n=0$.
::::

:::frage Warum lässt man nicht immer alle Teilmengen als Ereignisse zu?
Bei abzählbarem $\Omega$ geht das. Auf einem Intervall lässt sich dagegen nicht jeder Teilmenge widerspruchsfrei eine Länge zuordnen.
:::

:::aufgabe Aufgabe 1 ★ $\sigma$-Algebra prüfen
<span class="anker" id="aufg-1"></span>

Sei $\Omega=\{1,2,3,4\}$. Sind $\mathcal E_1=\{\emptyset,\{1\},\{2,3,4\},\Omega\}$ und $\mathcal E_2=\{\emptyset,\{1\},\{2\},\Omega\}$ $\sigma$-Algebren? Gib die kleinste $\sigma$-Algebra an, die $\{1\}$ und $\{2\}$ enthält.

:::loesung
$\mathcal E_1$ ja, alle Differenzen und Vereinigungen bleiben drin. $\mathcal E_2$ nein, $\{1\}\cup\{2\}$ fehlt. Die gesuchte $\sigma$-Algebra enthält auch $\{1,2\}$ und $\{3,4\}$, die Bausteine $\{1\},\{2\},\{3,4\}$ ergeben $2^3=8$ Mengen: $\emptyset$, $\{1\}$, $\{2\}$, $\{3,4\}$, $\{1,2\}$, $\{1,3,4\}$, $\{2,3,4\}$, $\Omega$.
:::
:::

:::aufgabe Aufgabe 2 ★★ Drei Ereignisse
<span class="anker" id="aufg-2"></span>

Vierer-Würfel: Wie wahrscheinlich ist es, dass mindestens ein Würfel 4 zeigt oder die Summe 5 ist? Leite dazu aus Satz [1.3](#satz-1-3) die Formel für $\mathbb{P}(A\cup B\cup C)$ her. Tipp: Setze $D=A\cup B$.

:::loesung
Mit $D=A\cup B$ ist $\mathbb{P}(D\cup C)=\mathbb{P}(D)+\mathbb{P}(C)-\mathbb{P}(D\cap C)$, und $D\cap C=(A\cap C)\cup(B\cap C)$. Zweimal Regel (iv) gibt die Summe der Einzelwahrscheinlichkeiten, minus die der Zweierschnitte, plus den Dreierschnitt. Hier sind die Anzahlen $4,4,4$, dann $1,1,1$, dann 0, also $\frac{12-3}{16}=\frac9{16}$.
:::
:::
