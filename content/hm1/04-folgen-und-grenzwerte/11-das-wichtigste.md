---
title: Das Wichtigste
pfad: Elektrotechnik / 1. Semester / HöMa1 – Höhere Mathematik 1 / Folgen und Grenzwerte
adresse: elektrotechnik/1-semester/hohere-mathematik-1/folgen-und-grenzwerte
knoten: Kapitel 4: Folgen und Grenzwerte
order: 1241100
summary: Was „beliebig nah“ heißt und warum die reellen Zahlen keine Lücke haben dürfen
tags: 
lang: de
---

:::merke Die Antwort in drei Sätzen
<ol>

<li>

Eine Folge $\{a_n\}$ konvergiert gegen $a$, wenn es zu jeder Toleranz $\varepsilon>0$ einen Index $N_0$ gibt, ab dem alle Glieder näher als $\varepsilon$ bei $a$ liegen: $|a_n-a|<\varepsilon$ für alle $n>N_0$.

</li>

<li>

Vergleich, Rechenregeln und Einklemmen führen neue Grenzwerte auf bekannte zurück.

</li>

<li>

Monotone beschränkte Folgen und Cauchy-Folgen konvergieren in $\mathbb{R}$, aber nicht in $\mathbb{Q}$. Darin zeigt sich, dass $\mathbb{R}$ vollständig ist.

</li>

</ol>
:::

:::kern Das Wichtigste
<ul>

<li>

Folge: Funktion auf $\mathbb{N}$. Konvergent gegen $a$: $\forall\,\varepsilon>0\ \exists\,N_0\ \forall\,n>N_0:\ |a_n-a|<\varepsilon$.

</li>

<li>

Nullfolgen: $\frac1n$, $\frac1{\sqrt n}$, $q^n$ und $nq^n$ für $|q|<1$, $x^n/n!$. Nullfolge mal beschränkt ist Nullfolge.

</li>

<li>

Vergleich: $|b_n|\le|a_n|$ und $a_n\to0$ ergibt $b_n\to0$. Sandwich: $c_n\le a_n\le b_n$ und $c_n,b_n\to a$ ergibt $a_n\to a$.

</li>

<li>

Grenzwerte vertragen $+$, $\cdot$, Kehrwert ($a\ne0$), Betrag, Wurzel ($a_n\ge0$). Konvergente Folgen sind beschränkt, ihr Grenzwert ist eindeutig.

</li>

<li>

$\sqrt[n]{x}\to1$, $\sqrt[n]{n}\to1$, $\sum_{k=0}^nq^k=(1-q^{n+1})/(1-q)$ für $q\ne1$.

</li>

<li>

Monoton und beschränkt ergibt konvergent mit $\lim a_n=\sup\mathcal W(a_n)$. In $\mathbb{R}$: konvergent $\iff$ Cauchy. In $\mathbb{Q}$ kann der Grenzwert fehlen (Heron-Verfahren für $\sqrt2$).

</li>

</ul>
:::

**Ein Prinzip hinter allen Ergebnissen.** Konvergenz ist eine Aussage über Abstände. Jedes Ergebnis dieses Kapitels schätzt einen Abstand durch Abstände ab, die schon als klein bekannt sind. Nur die Existenz des Grenzwerts lässt sich nicht abschätzen, sie kommt aus den Axiomen.

| Ergebnis | Woher es kommt |
|---|---|
| Nullfolge, Epsilon-Kriterium | Der Abstand zur 0 unterbietet jede Toleranz (Stufe [2](das-epsilon-spiel.html#stufe-2)) |
| Vergleichskriterium, $q^n$, $x^n/n!$ | Ein kleinerer Abstand unterbietet sie erst recht (Stufe [3](nullfolgen-vergleichen.html#stufe-3)) |
| Grenzwert $a$ | Der Abstand zu $a$ ist eine Nullfolge (Stufe [4](der-grenzwert.html#stufe-4)) |
| Rechenregeln | Der Abstand einer Summe oder eines Produkts folgt aus den Einzelabständen (Stufe [5](rechenregeln.html#stufe-5)) |
| Sandwich-Lemma | Zwei Nachbarn klemmen den Abstand von beiden Seiten ein (Stufe [6](einklemmen-und-divergenz.html#stufe-6)) |
| Monotonie-Lemma | Der Abstand zum Supremum schrumpft; dass es existiert, sagt die Vollständigkeit (Stufe [7](monotone-folgen-und-die-vollstandigkeit.html#stufe-7)) |
| Cauchy-Folgen | Die Abstände untereinander ersetzen den Abstand zum unbekannten Ziel (Stufe [8](cauchy-folgen-und-die-axiome.html#stufe-8)) |
