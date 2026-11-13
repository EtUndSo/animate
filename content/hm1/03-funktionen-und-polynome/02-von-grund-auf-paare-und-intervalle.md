---
title: Von Grund auf: Paare und Intervalle
pfad: Elektrotechnik / 1. Semester / HöMa1 – Höhere Mathematik 1 / Funktionen und Polynome
adresse: elektrotechnik/1-semester/hohere-mathematik-1/funktionen-und-polynome
knoten: Kapitel 3: Funktionen und Polynome
order: 1230200
summary: Wann sich eine Gleichung rückwärts lösen lässt und warum jede Nullstelle einen Faktor abspaltet
tags: kartesische Produkt, Intervalle, offen, abgeschlossen, halboffen
lang: de
---

Mengen, die Zeichen $\in$, $\subset$ und die Zahlbereiche kennt [Kapitel 1](/wissen/elektrotechnik/1-semester/hohere-mathematik-1/mengen-logik-und-reelle-zahlen/mengen-logik-und-reelle-zahlen.html). Dazu kommen zwei Bausteine. Das __kartesische Produkt__ (auch Kreuzprodukt) zweier Mengen ist die Menge aller geordneten Paare:

$$A\times B:=\bigl\{(a,b):a\in A\ \wedge\ b\in B\bigr\}.$$

Die Reihenfolge zählt, $(1,2)\neq(2,1)$. Für $n$ Mengen entsprechend $A_1\times\dots\times A_n:=\{(a_1,\dots,a_n):a_i\in A_i\text{ für alle }i\}$, und $A^n:=A\times\dots\times A$ mit $n$ Faktoren. $\mathbb{R}^2$ ist die Zahlenebene.

__Intervalle__ sind die zusammenhängenden Stücke der Zahlengeraden. Für $a\le b$ heißen die beschränkten Mengen $(a,b):=\{x\in\mathbb{R}:a<x<b\}$ __offen__, $[a,b]:=\{x\in\mathbb{R}:a\le x\le b\}$ __abgeschlossen__, und $(a,b]$ und $[a,b)$ __halboffen__. Die eckige Klammer heißt: Der Endpunkt gehört dazu, die runde: Er gehört nicht dazu. Unbeschränkt sind $(a,\infty):=\{x\in\mathbb{R}:a<x\}$, $[a,\infty):=\{x\in\mathbb{R}:a\le x\}$, $(-\infty,b):=\{x\in\mathbb{R}:x<b\}$, $(-\infty,b]:=\{x\in\mathbb{R}:x\le b\}$ und $(-\infty,\infty):=\mathbb{R}$. Das Zeichen $\infty$ ist keine Zahl, deshalb steht dort immer die runde Klammer. Außerdem ist $\mathbb{R}_0^+:=[0,\infty)$.

::::formelsammlung
**Kartesisches Produkt**

$$A\times B:=\bigl\{(a,b):a\in A\ \wedge\ b\in B\bigr\}$$

Die Menge aller geordneten Paare, auch Kreuzprodukt genannt; die Reihenfolge zählt, $(1,2)\neq(2,1)$.

**Produkt von $n$ Mengen**

$$A_1\times\dots\times A_n:=\{(a_1,\dots,a_n):a_i\in A_i\text{ für alle }i\},\qquad A^n:=A\times\dots\times A$$

$A^n$ hat $n$ Faktoren; $\mathbb{R}^2$ ist die Zahlenebene.

**Beschränkte Intervalle**

$$(a,b):=\{x\in\mathbb{R}:a<x<b\},\qquad[a,b]:=\{x\in\mathbb{R}:a\le x\le b\}$$

Für $a\le b$: $(a,b)$ ist offen, $[a,b]$ abgeschlossen, $(a,b]$ und $[a,b)$ sind halboffen. Eckige Klammer: Der Endpunkt gehört dazu; runde Klammer: Er gehört nicht dazu.

**Nach rechts unbeschränkte Intervalle**

$$(a,\infty):=\{x\in\mathbb{R}:a<x\},\qquad[a,\infty):=\{x\in\mathbb{R}:a\le x\}$$

$\infty$ ist keine Zahl, deshalb steht dort immer die runde Klammer.

**Nach links unbeschränkte Intervalle**

$$(-\infty,b):=\{x\in\mathbb{R}:x<b\},\qquad(-\infty,b]:=\{x\in\mathbb{R}:x\le b\},\qquad(-\infty,\infty):=\mathbb{R}$$

Die Intervalle sind die zusammenhängenden Stücke der Zahlengeraden.

**Nicht negative Zahlen**

$$\mathbb{R}_0^+:=[0,\infty)$$

Die Null gehört dazu.
::::

::::lernkarten
:::karte begriff kartesisches Produkt
Welche Menge ist das kartesische Produkt $A\times B$ zweier Mengen $A$ und $B$, und spielt die Reihenfolge in den Paaren eine Rolle?
---
Die Menge aller geordneten Paare mit erstem Eintrag aus $A$ und zweitem aus $B$: $A\times B:=\{(a,b):a\in A\ \wedge\ b\in B\}$. Die Reihenfolge zählt, $(1,2)\neq(2,1)$.
--- falsch
Die Menge aller Paare aus je einem Element von $A$ und einem von $B$, wobei die Reihenfolge nicht zählt: $(1,2)$ und $(2,1)$ sind dasselbe Paar, weil beide dieselben Elemente enthalten.
--- falsch
Die Menge aller Produkte $a\cdot b$ mit $a\in A$ und $b\in B$. Die Reihenfolge zählt nicht, weil die Multiplikation reeller Zahlen kommutativ ist, $1\cdot2=2\cdot1$.
--- falsch
Die Menge aller Elemente, die sowohl in $A$ als auch in $B$ liegen: $A\times B:=\{x:x\in A\ \wedge\ x\in B\}$. Die Reihenfolge von $A$ und $B$ zählt nicht.
:::
:::karte formel Produkt von n Mengen
Wie bildet man das kartesische Produkt von $n$ Mengen, und was bezeichnet die Schreibweise $A^n$?
---
$A_1\times\dots\times A_n:=\{(a_1,\dots,a_n):a_i\in A_i\text{ für alle }i\}$, der $i$-te Eintrag stammt aus $A_i$. $A^n:=A\times\dots\times A$ mit $n$ Faktoren; so ist $\mathbb{R}^2$ die Zahlenebene.
--- falsch
$A_1\times\dots\times A_n:=\{(a_1,\dots,a_n):a_i\in A_i\text{ für alle }i\}$, der $i$-te Eintrag stammt aus $A_i$. $A^n$ ist die Menge der Potenzen $a^n$ mit $a\in A$; so ist $\mathbb{R}^2$ die Menge der Quadrate.
--- falsch
$A_1\times\dots\times A_n:=\{(a_1,\dots,a_n):a_i\in A_1\cap\dots\cap A_n\}$, jeder Eintrag liegt in allen Mengen zugleich. $A^n$ ist das Produkt aus $n$ Faktoren $A$, etwa $\mathbb{R}^2$.
--- falsch
$A_1\times\dots\times A_n:=\{a_1+\dots+a_n:a_i\in A_i\text{ für alle }i\}$, also alle Summen aus je einem Element. $A^n:=A\times\dots\times A$ mit $n$ Faktoren, etwa $\mathbb{R}^2$.
:::
:::karte zusammenhang Intervalle
Warum steht bei einem unbeschränkten Intervall wie $[a,\infty)$ an der Seite von $\infty$ immer eine runde Klammer?
---
Weil $\infty$ keine Zahl ist und deshalb nicht zum Intervall gehören kann; die runde Klammer heißt: Der Endpunkt gehört nicht dazu. So ist $[a,\infty):=\{x\in\mathbb{R}:a\le x\}$ und $(-\infty,\infty):=\mathbb{R}$.
--- falsch
Weil das Intervall dort offen sein muss, damit es unbeschränkt bleibt: Mit eckiger Klammer wäre $\infty$ sein größter Wert, und $[a,\infty]$ wäre dann ein beschränktes Intervall.
--- falsch
Weil runde Klammern bei Intervallen anzeigen, dass sie unbeschränkt sind; eckige Klammern stehen nur bei beschränkten Intervallen, die runde Klammer sagt nichts über den Endpunkt.
--- falsch
Weil man $\infty$ nur von unten annähern kann. Die Zahl $\infty$ selbst gehört zwar zu $\mathbb{R}$, ist aber größer als jede andere reelle Zahl und wird deshalb aus dem Intervall ausgeschlossen.
:::
:::karte begriff offen
Wann heißt ein beschränktes Intervall offen, und woran erkennt man das an seiner Schreibweise?
---
Wenn keiner der beiden Endpunkte dazugehört: Für $a\le b$ ist $(a,b):=\{x\in\mathbb{R}:a<x<b\}$ offen. Die runden Klammern zeigen an, dass $a$ und $b$ nicht dazugehören.
--- falsch
Wenn beide Endpunkte dazugehören: Für $a\le b$ ist $(a,b):=\{x\in\mathbb{R}:a\le x\le b\}$ offen. Die runden Klammern zeigen an, dass das Intervall zu beiden Seiten für seine Endpunkte offen ist.
--- falsch
Wenn genau einer der beiden Endpunkte dazugehört, etwa bei $(a,b]$. Die runde Klammer zeigt die offene Seite an, die eckige die geschlossene; ohne offene Seite heißt es abgeschlossen.
--- falsch
Wenn es unendlich viele Zahlen enthält, also $a<b$ gilt; für $a=b$ enthält es nur eine Zahl und ist abgeschlossen. Die Klammern geben nur die Schreibrichtung des Intervalls an.
:::
:::karte begriff abgeschlossen
Wann heißt ein beschränktes Intervall abgeschlossen, und wie schreibt man es?
---
Wenn beide Endpunkte dazugehören: Für $a\le b$ ist $[a,b]:=\{x\in\mathbb{R}:a\le x\le b\}$ abgeschlossen. Die eckigen Klammern zeigen an, dass $a$ und $b$ dazugehören.
--- falsch
Wenn keiner der beiden Endpunkte dazugehört: Für $a\le b$ ist $[a,b]:=\{x\in\mathbb{R}:a<x<b\}$ abgeschlossen; die eckigen Klammern schließen die Endpunkte $a$ und $b$ aus.
--- falsch
Wenn es nach beiden Seiten beschränkt ist, gleich ob die Endpunkte dazugehören; $(a,b)$ und $[a,b]$ sind beide abgeschlossen, nur $(a,\infty)$ und $(-\infty,b)$ sind es nicht.
--- falsch
Wenn mindestens ein Endpunkt dazugehört, etwa bei $[a,b)$ oder $[a,b]$. Eine eckige Klammer auf einer Seite genügt, damit das Intervall abgeschlossen heißt.
:::
:::karte begriff halboffen
Welche beschränkten Intervalle heißen halboffen, und was zeigen ihre Klammern an?
---
Die Intervalle $(a,b]$ und $[a,b)$ für $a\le b$: Genau ein Endpunkt gehört dazu. Die eckige Klammer markiert den Endpunkt, der dazugehört, die runde den, der fehlt.
--- falsch
Die Intervalle $(a,\infty)$ und $(-\infty,b)$: Sie sind auf einer Seite beschränkt und auf der anderen nicht. Die runde Klammer markiert jeweils die unbeschränkte Seite.
--- falsch
Die Intervalle $(a,b]$ und $[a,b)$ für $a\le b$: Genau ein Endpunkt gehört dazu. Die runde Klammer markiert den Endpunkt, der dazugehört, die eckige den, der fehlt.
--- falsch
Die Intervalle $(a,b)$ für $a\le b$: Sie heißen halboffen, weil ihre Endpunkte fehlen, die Zahlen dazwischen aber dazugehören. Die runden Klammern zeigen das an.
:::
:::karte formel unbeschränkte Intervalle
Wie sind die unbeschränkten Intervalle und die Menge $\mathbb{R}_0^+$ als Mengen reeller Zahlen festgelegt?
---
$(a,\infty):=\{x\in\mathbb{R}:a<x\}$, $[a,\infty):=\{x\in\mathbb{R}:a\le x\}$, $(-\infty,b):=\{x\in\mathbb{R}:x<b\}$, $(-\infty,b]:=\{x\in\mathbb{R}:x\le b\}$, $(-\infty,\infty):=\mathbb{R}$ und $\mathbb{R}_0^+:=[0,\infty)$.
--- falsch
$(a,\infty):=\{x\in\mathbb{R}:a<x\}$, $[a,\infty):=\{x\in\mathbb{R}:a\le x\}$, $(-\infty,b):=\{x\in\mathbb{R}:x<b\}$, $(-\infty,b]:=\{x\in\mathbb{R}:x\le b\}$, $(-\infty,\infty):=\mathbb{R}$ und $\mathbb{R}_0^+:=(0,\infty)$, ohne die Null.
--- falsch
$(a,\infty):=\{x\in\mathbb{R}:a\le x\}$, $[a,\infty):=\{x\in\mathbb{R}:a<x\}$, $(-\infty,b):=\{x\in\mathbb{R}:x\le b\}$, $(-\infty,b]:=\{x\in\mathbb{R}:x<b\}$, $(-\infty,\infty):=\mathbb{R}$ und $\mathbb{R}_0^+:=[0,\infty)$.
--- falsch
$(a,\infty):=\{x\in\mathbb{R}:a<x\}$, $[a,\infty]:=\{x\in\mathbb{R}:a\le x\le\infty\}$, $(-\infty,b):=\{x\in\mathbb{R}:x<b\}$, $[-\infty,\infty]:=\mathbb{R}$ und $\mathbb{R}_0^+:=[0,\infty]$, mit $\infty$ als Endpunkt.
:::
::::
