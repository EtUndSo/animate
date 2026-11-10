---
title: Stufe 2: Quantoren und indirekter Beweis
pfad: Elektrotechnik / 1. Semester / HöMa1 – Höhere Mathematik 1 / Mengen, Logik und reelle Zahlen
adresse: elektrotechnik/1-semester/hohere-mathematik-1/mengen-logik-und-reelle-zahlen
knoten: Kapitel 1: Mengen, Logik und reelle Zahlen
order: 1210400
summary: Alle Axiome haben die Form „für alle x gibt es ein y “.
tags: Allquantor, Existenzquantor, Gegenbeispiel, Widerspruchsannahme, Russellsche Antinomie
lang: de
---

<span class="anker" id="stufe-2"></span>

:::zweck
Alle Axiome haben die Form „für alle $x$ gibt es ein $y$“. Diese Stufe klärt, wie man solche Sätze liest und verneint, und wie man aus einer Verneinung einen Beweis macht.
:::

**Die Idee.** „Für alle $x$ aus $\{x_1,x_2,\dots\}$ gilt $\mathcal A(x)$“ ist ein langes Und: $\mathcal A(x_1)\wedge\mathcal A(x_2)\wedge\dots$ „Es gibt ein $x$“ ist ein langes Oder. De Morgan verwandelt beim Verneinen Und in Oder. Darum wird beim Verneinen aus „für alle“ ein „es gibt“.

:::definition Definition 2.1 (Quantoren)
<span class="anker" id="satz-2-1"></span>

$\forall$ heißt „für alle“ (__Allquantor__), $\exists$ „es gibt mindestens ein“ (__Existenzquantor__), $\exists_1$ „es gibt genau ein“, $\nexists$ „es gibt kein“.
:::

⁠**So liest man das:** Wahre Beispiele im Rechenmodell sind $\forall x\in A:x\le12$; $\exists x\in A:x>5$ (etwa $x=6$); $\exists_1x\in A\cap B:x>2$ (nämlich $x=3$); $\nexists x\in B:x=9$. Auch Teilbarkeit ist eine Quantor-Aussage: $m\mid p$ („$m$ teilt $p$“) heißt $\exists n\in\mathbb{N}:m\cdot n=p$, also $6\mid12$ wegen $6\cdot2=12$, und $7\nmid12$. Die Menge der Primzahlen ist $\{p\in\mathbb{N}\setminus\{1\}:\nexists m\in\{2,\dots,p-1\}\text{ mit }m\mid p\}$.

:::satz Satz 2.2 (Verneinungsregel)
<span class="anker" id="satz-2-2"></span>

<span class="anker" id="gl-2-1"></span>
$$\neg\bigl(\forall x\in M:\mathcal A(x)\bigr)\Leftrightarrow\bigl(\exists x\in M:\neg\mathcal A(x)\bigr),\quad \neg\bigl(\exists y\in N:\mathcal B(y)\bigr)\Leftrightarrow\bigl(\forall y\in N:\neg\mathcal B(y)\bigr). \tag{2.1}$$
:::

⁠**So liest man das:** Quantor tauschen, Aussage verneinen, bei geschachtelten Quantoren der Reihe nach. Im Rechenmodell ist die Verneinung von $\forall n\in\mathbb{N}:\mathcal E(n)$ die falsche Aussage $\exists n\in\mathbb{N}:(n\ge7\wedge n\le5)$. **Beweis-Idee:** $\neg(\mathcal A(x_1)\wedge\mathcal A(x_2)\wedge\dots)$ ist nach De Morgan $\neg\mathcal A(x_1)\vee\neg\mathcal A(x_2)\vee\dots$; die zweite Regel entsteht ebenso. **Grenzfall** $M=\emptyset$: „Für alle $x\in\emptyset$“ ist immer wahr, „es gibt $x\in\emptyset$“ immer falsch.

:::frage Reichen fünf Beispiele, um „für alle“ zu beweisen?
Nein. Ein Beispiel prüft nur ein $x$. Nach [(2.1)](#gl-2-1) widerlegt dagegen ein einziges __Gegenbeispiel__ die Aussage „für alle“. „Es gibt“ beweist man umgekehrt mit einem Beispiel.
:::

::::beispiel geschachtelte Quantoren
$H$ seien die Geräte eines Haushalts, $F$ die Sicherungen, $K(g,s)$ heiße „Gerät $g$ hängt an Sicherung $s$“. Dann sagen

$$\mathcal P:=\bigl(\forall g\in H\ \exists s\in F:K(g,s)\bigr),\qquad \mathcal Q:=\bigl(\exists s\in F\ \forall g\in H:K(g,s)\bigr)$$

Verschiedenes (Abb. [2](#abb-2)): Bei $\mathcal P$ darf $s$ vom Gerät abhängen, bei $\mathcal Q$ gilt eine Sicherung für alle. Aus $\mathcal Q$ folgt $\mathcal P$, die Umkehrung ist falsch. **Die Reihenfolge verschiedener Quantoren darf man nicht vertauschen.** Die Verneinungen lauten $\neg\mathcal P=(\exists g\ \forall s:\neg K(g,s))$, ein Gerät hängt an keiner Sicherung, und $\neg\mathcal Q=(\forall s\ \exists g:\neg K(g,s))$, jede Sicherung lässt mindestens ein Gerät aus.

:::abbildung hm1/k1quantoren 2
Das rechte Bild erfüllt beide Aussagen, das linke nur die erste.
:::
::::

:::satz Satz 2.3 (Indirekter Beweis)
<span class="anker" id="satz-2-3"></span>

Ist $\neg\mathcal A\Rightarrow\mathcal B$ wahr und $\mathcal B$ falsch, dann ist $\mathcal A$ wahr.
:::

⁠**So liest man das:** Man nimmt das Gegenteil der Behauptung an (__Widerspruchsannahme__) und schließt, bis etwas Falsches herauskommt. Ein Blick in die Tafel zeigt den Mechanismus: Wäre $\neg\mathcal A$ wahr, müsste auch $\mathcal B$ wahr sein. Also ist $\neg\mathcal A$ falsch. Soll man eine Implikation $\mathcal A\Rightarrow\mathcal B$ indirekt zeigen, lautet die Annahme nach De Morgan $\mathcal A\wedge\neg\mathcal B$. **Beispiel:** Es gibt keine kleinste positive rationale Zahl. Annahme: $r$ wäre die kleinste. Dann ist $r/2$ rational, positiv und kleiner als $r$. Das ist falsch, also gibt es kein solches $r$.

**Warum man Axiome braucht.** Sei $M=\{N:N\notin N\}$ die Menge aller Mengen, die sich nicht selbst enthalten (__Russellsche Antinomie__, 1903). Ist $M\in M$ wahr, erfüllt $M$ die Bedingung nicht, also $M\notin M$. Ist $M\notin M$ wahr, erfüllt $M$ die Bedingung, also $M\in M$. Beides ist unmöglich, die Konstruktion ist unzulässig. Ebenso widersprüchlich ist der Satz „Dieser Satz ist falsch“. Solche Befunde lösten die Grundlagenkrise der Mathematik aus, von Hilberts Forderung nach einem widerspruchsfreien Aufbau (1900) bis zu Gödels Unvollständigkeitssätzen (1931). Die Lehre: Gewissheit gibt es nur relativ zu festgelegten Annahmen. Deshalb baut man die Zahlen auf Axiomen auf.

:::aufgabe Aufgabe 3 ★★ Verneinen und indirekt beweisen
<span class="anker" id="aufg-3"></span>

<ol class="al">

<li>

Verneine: „Jede Schaltung enthält ein Bauteil, das warm wird.“

</li>

<li>

Verneine $\forall\varepsilon>0\ \exists n\in\mathbb{N}:\frac1n<\varepsilon$. Wird die Aussage wahr oder falsch, wenn man die Quantoren vertauscht?

</li>

<li>

Zeige indirekt: Ist $n^2$ ungerade, dann ist $n$ ungerade.

</li>

</ol>

:::loesung
(a) „Es gibt eine Schaltung, in der kein Bauteil warm wird.“ (b) Verneinung: $\exists\varepsilon>0\ \forall n\in\mathbb{N}:\frac1n\ge\varepsilon$. Vertauscht: $\exists n\in\mathbb{N}\ \forall\varepsilon>0:\frac1n<\varepsilon$ ist falsch, denn für $\varepsilon=\frac1n$ steht $\frac1n<\frac1n$. Die Originalaussage ist dagegen wahr, das zeigt Stufe [6](das-vollstandigkeitsaxiom.html#stufe-6). (c) Annahme: $n^2$ ungerade und $n$ gerade, $n=2k$. Dann ist $n^2=2\cdot2k^2$ gerade, Widerspruch.
:::
:::
