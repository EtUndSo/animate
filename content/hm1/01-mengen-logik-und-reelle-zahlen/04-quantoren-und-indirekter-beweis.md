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

::::formelsammlung
**Quantoren**

$$\forall,\qquad\exists,\qquad\exists_1,\qquad\nexists$$

„für alle“ (Allquantor), „es gibt mindestens ein“ (Existenzquantor), „es gibt genau ein“, „es gibt kein“.

**Verneinungsregel**

$$\neg\bigl(\forall x\in M:\mathcal A(x)\bigr)\Leftrightarrow\bigl(\exists x\in M:\neg\mathcal A(x)\bigr),\qquad\neg\bigl(\exists y\in N:\mathcal B(y)\bigr)\Leftrightarrow\bigl(\forall y\in N:\neg\mathcal B(y)\bigr)$$

Quantor tauschen, Aussage verneinen; bei geschachtelten Quantoren der Reihe nach. „Für alle“ ist ein langes Und, „es gibt“ ein langes Oder, verneint wird nach De Morgan. Ein einziges Gegenbeispiel widerlegt „für alle“. Für $M=\emptyset$ ist „für alle“ immer wahr, „es gibt“ immer falsch.

**Reihenfolge der Quantoren**

$$\bigl(\exists s\in F\ \forall g\in H:K(g,s)\bigr)\Rightarrow\bigl(\forall g\in H\ \exists s\in F:K(g,s)\bigr)$$

Die Umkehrung ist falsch: Verschiedene Quantoren darf man nicht vertauschen. Mit $K(g,s)$ „Gerät $g$ hängt an Sicherung $s$“: links gilt eine Sicherung für alle Geräte, rechts darf $s$ vom Gerät abhängen.

**Teilbarkeit und Primzahlen**

$$m\mid p\ \Leftrightarrow\ \exists n\in\mathbb{N}:m\cdot n=p,\qquad\{p\in\mathbb{N}\setminus\{1\}:\nexists m\in\{2,\dots,p-1\}\text{ mit }m\mid p\}$$

$m\mid p$ heißt „$m$ teilt $p$“; die Menge rechts ist die Menge der Primzahlen.

**Indirekter Beweis**

$$\bigl((\neg\mathcal A\Rightarrow\mathcal B)\wedge\neg\mathcal B\bigr)\Rightarrow\mathcal A$$

Ist $\neg\mathcal A\Rightarrow\mathcal B$ wahr und $\mathcal B$ falsch, dann ist $\mathcal A$ wahr. Man nimmt das Gegenteil der Behauptung an (Widerspruchsannahme) und schließt, bis etwas Falsches herauskommt. Für eine Implikation $\mathcal A\Rightarrow\mathcal B$ lautet die Annahme $\mathcal A\wedge\neg\mathcal B$.
::::

::::lernkarten
:::karte begriff Allquantor und Existenzquantor
Was bedeuten die Quantoren $\forall$, $\exists$, $\exists_1$ und $\nexists$?
---
$\forall$ heißt „für alle“ (Allquantor), $\exists$ „es gibt mindestens ein“ (Existenzquantor), $\exists_1$ „es gibt genau ein“ und $\nexists$ „es gibt kein“.
--- falsch
$\forall$ heißt „für alle“ (Allquantor), $\exists$ „es gibt genau ein“ (Existenzquantor), $\exists_1$ „es gibt mindestens ein“ und $\nexists$ „nicht für alle“.
--- falsch
$\forall$ heißt „für fast alle“ (Allquantor), $\exists$ „es gibt mindestens ein“ (Existenzquantor), $\exists_1$ „es gibt höchstens ein“ und $\nexists$ „es gibt kein“.
--- falsch
$\forall$ heißt „es gibt ein“ (Allquantor), $\exists$ „für alle“ (Existenzquantor), $\exists_1$ „für genau eines“ und $\nexists$ „für keines“.
:::
:::karte zusammenhang Verneinen von „für alle“
Warum wird beim Verneinen einer Aussage aus „für alle“ ein „es gibt“?
---
Weil „für alle $x$ aus $\{x_1,x_2,\dots\}$ gilt $\mathcal A(x)$“ ein langes Und $\mathcal A(x_1)\wedge\mathcal A(x_2)\wedge\dots$ ist und De Morgan beim Verneinen Und in Oder verwandelt. Ein langes Oder ist ein „es gibt“.
--- falsch
Weil „für alle“ ein langes Oder ist und die Verneinung eines Oder nach De Morgan immer ein „es gibt“ ergibt. Ein langes Und dagegen würde beim Verneinen zu „es gibt kein“.
--- falsch
Weil man eine Für-alle-Aussage nur widerlegen kann, indem man alle Fälle einzeln prüft; „es gibt“ ist dabei nur eine verkürzte Schreibweise für „für alle bis auf einen Fall“.
--- falsch
Weil die Verneinung den Quantor unverändert lässt und nur die Aussage dahinter verneint; dass ein „es gibt“ entsteht, ist eine bloße Vereinbarung der Schreibweise.
:::
:::karte formel Verneinungsregel
Wie verneint man die Aussagen $\forall x\in M:\mathcal A(x)$ und $\exists y\in N:\mathcal B(y)$?
---
$\neg\bigl(\forall x\in M:\mathcal A(x)\bigr)\Leftrightarrow\bigl(\exists x\in M:\neg\mathcal A(x)\bigr)$ und $\neg\bigl(\exists y\in N:\mathcal B(y)\bigr)\Leftrightarrow\bigl(\forall y\in N:\neg\mathcal B(y)\bigr)$: Quantor tauschen, Aussage verneinen.
--- falsch
$\neg\bigl(\forall x\in M:\mathcal A(x)\bigr)\Leftrightarrow\bigl(\forall x\in M:\neg\mathcal A(x)\bigr)$ und $\neg\bigl(\exists y\in N:\mathcal B(y)\bigr)\Leftrightarrow\bigl(\exists y\in N:\neg\mathcal B(y)\bigr)$: Quantor behalten, Aussage verneinen.
--- falsch
$\neg\bigl(\forall x\in M:\mathcal A(x)\bigr)\Leftrightarrow\bigl(\exists x\in M:\mathcal A(x)\bigr)$ und $\neg\bigl(\exists y\in N:\mathcal B(y)\bigr)\Leftrightarrow\bigl(\forall y\in N:\mathcal B(y)\bigr)$: Quantor tauschen, Aussage behalten.
--- falsch
$\neg\bigl(\forall x\in M:\mathcal A(x)\bigr)\Leftrightarrow\bigl(\exists x\notin M:\mathcal A(x)\bigr)$ und $\neg\bigl(\exists y\in N:\mathcal B(y)\bigr)\Leftrightarrow\bigl(\forall y\notin N:\mathcal B(y)\bigr)$: Quantor tauschen, Grundmenge verneinen.
:::
:::karte begriff Gegenbeispiel
Was ist ein Gegenbeispiel, und warum genügen Beispiele nicht, um eine Für-alle-Aussage zu beweisen?
---
Ein einziges $x$, für das $\mathcal A(x)$ falsch ist; nach der Verneinungsregel widerlegt es „für alle $x$ gilt $\mathcal A(x)$“. Ein Beispiel prüft dagegen nur ein $x$; mit einem Beispiel beweist man „es gibt“.
--- falsch
Ein $x$, für das $\mathcal A(x)$ wahr ist; es bestätigt „für alle $x$ gilt $\mathcal A(x)$“. Fünf solche Beispiele genügen als Beweis, wenn sie verschieden genug gewählt sind und keines aus der Reihe fällt.
--- falsch
Ein einziges $x$, für das $\mathcal A(x)$ falsch ist; es widerlegt „es gibt ein $x$ mit $\mathcal A(x)$“. Für-alle-Aussagen beweist man dagegen mit genügend vielen Beispielen.
--- falsch
Eine Aussage, die einer anderen widerspricht. Ein einziges Gegenbeispiel genügt nicht, um „für alle“ zu widerlegen; man braucht mehrere, damit kein Zufall vorliegt.
:::
:::karte zusammenhang Reihenfolge der Quantoren
Warum darf man in $\forall g\in H\ \exists s\in F:K(g,s)$ („jedes Gerät hängt an einer Sicherung“) die beiden Quantoren nicht vertauschen?
---
Weil sich die Bedeutung ändert: Bei $\forall g\ \exists s$ darf die Sicherung $s$ vom Gerät $g$ abhängen, bei $\exists s\ \forall g$ muss eine Sicherung für alle Geräte gelten. Aus der zweiten folgt die erste, die Umkehrung ist falsch.
--- falsch
Weil $\exists s\ \forall g$ die schwächere Aussage ist: Sie verlangt nur irgendeine Sicherung, während $\forall g\ \exists s$ für jedes Gerät eine eigene Sicherung fordert. Aus der ersten folgt die zweite deshalb nicht.
--- falsch
Weil sich die Bedeutung ändert: Bei $\forall g\ \exists s$ muss eine Sicherung für alle Geräte gelten, bei $\exists s\ \forall g$ darf die Sicherung vom Gerät abhängen. Aus der ersten folgt die zweite.
--- falsch
Man darf sie vertauschen, weil beide Aussagen dieselben Quantoren enthalten. Nur die Reihenfolge des Lesens ändert sich, die Bedeutung bleibt in beiden Fällen gleich.
:::
:::karte zusammenhang leere Grundmenge
Welchen Wahrheitswert haben „für alle $x\in\emptyset$ gilt $\mathcal A(x)$“ und „es gibt $x\in\emptyset$ mit $\mathcal A(x)$“?
---
„Für alle $x\in\emptyset$“ ist immer wahr, „es gibt $x\in\emptyset$“ immer falsch: Es gibt kein $x$, das ein Gegenbeispiel sein könnte, aber auch keines, das die Existenz belegt.
--- falsch
Beide sind immer falsch, weil eine Aussage über die leere Menge nichts behauptet und deshalb nicht wahr sein kann; es fehlt jedes $x$, an dem man sie prüfen könnte.
--- falsch
Beide sind immer wahr, weil man über die leere Menge alles behaupten darf, ohne einen Widerspruch zu erzeugen; kein $x$ kann einer der beiden Aussagen widersprechen.
--- falsch
„Für alle $x\in\emptyset$“ ist immer falsch, „es gibt $x\in\emptyset$“ immer wahr, weil die leere Menge selbst als Element zählt und deshalb ein $x$ vorhanden ist.
:::
:::karte formel Teilbarkeit
Wie schreibt man die Teilbarkeit $m\mid p$ („$m$ teilt $p$“) als Aussage mit einem Quantor?
---
$m\mid p$ heißt $\exists n\in\mathbb{N}:m\cdot n=p$. So gilt $6\mid12$ wegen $6\cdot2=12$, aber $7\nmid12$.
--- falsch
$m\mid p$ heißt $\forall n\in\mathbb{N}:m\cdot n=p$. So gilt $6\mid12$, weil jedes Vielfache von 6 gleich 12 ist.
--- falsch
$m\mid p$ heißt $\exists n\in\mathbb{N}:p\cdot n=m$. So gilt $12\mid6$, weil $12$ ein Vielfaches von $6$ ist.
--- falsch
$m\mid p$ heißt $\exists n\in\mathbb{N}:m+n=p$. So gilt $6\mid12$ wegen $6+6=12$, und ebenso $7\mid12$ wegen $7+5=12$.
:::
:::karte formel Indirekter Beweis
Unter welchen Voraussetzungen ist eine Aussage $\mathcal A$ nach dem Satz über den indirekten Beweis wahr?
---
Wenn $\neg\mathcal A\Rightarrow\mathcal B$ wahr und $\mathcal B$ falsch ist. Wäre $\neg\mathcal A$ wahr, müsste nach der Tafel auch $\mathcal B$ wahr sein; also ist $\neg\mathcal A$ falsch.
--- falsch
Wenn $\neg\mathcal A\Rightarrow\mathcal B$ wahr und $\mathcal B$ wahr ist. Dann ist auch $\neg\mathcal A$ wahr, und die doppelte Verneinung macht daraus ein wahres $\mathcal A$.
--- falsch
Wenn $\mathcal A\Rightarrow\mathcal B$ wahr und $\mathcal B$ wahr ist. Aus einer wahren Folgerung schließt man nach der Wahrheitstafel auf eine wahre Voraussetzung.
--- falsch
Wenn $\neg\mathcal A\Rightarrow\mathcal B$ falsch und $\mathcal B$ falsch ist. Dann sind beide Seiten falsch, und die Tafel ergibt für $\mathcal A$ den Wert wahr.
:::
:::karte begriff Widerspruchsannahme
Was ist die Widerspruchsannahme in einem indirekten Beweis, und wie lautet sie, wenn $\mathcal A\Rightarrow\mathcal B$ zu zeigen ist?
---
Die Annahme, dass das Gegenteil der Behauptung gilt; aus ihr schließt man, bis etwas Falsches herauskommt. Für $\mathcal A\Rightarrow\mathcal B$ lautet sie nach De Morgan $\mathcal A\wedge\neg\mathcal B$.
--- falsch
Die Annahme, dass das Gegenteil der Behauptung gilt; aus ihr schließt man, bis etwas Falsches herauskommt. Für $\mathcal A\Rightarrow\mathcal B$ lautet sie $\neg\mathcal A\Rightarrow\neg\mathcal B$.
--- falsch
Die Annahme, dass die Behauptung selbst gilt; aus ihr schließt man so lange weiter, bis etwas Wahres herauskommt. Für $\mathcal A\Rightarrow\mathcal B$ lautet sie $\mathcal A\wedge\mathcal B$.
--- falsch
Die Annahme, dass das Gegenteil der Behauptung gilt; aus ihr schließt man, bis etwas Falsches herauskommt. Für $\mathcal A\Rightarrow\mathcal B$ lautet sie $\neg\mathcal A\wedge\mathcal B$.
:::
:::karte herleitung keine kleinste positive rationale Zahl
Wie zeigt man indirekt, dass es keine kleinste positive rationale Zahl gibt?
---
Man nimmt an, $r$ wäre die kleinste positive rationale Zahl, weil ein indirekter Beweis mit dem Gegenteil der Behauptung beginnt.
---
Dann ist $r/2$ rational und positiv, weil die Hälfte eines positiven Bruchs wieder ein positiver Bruch ist.
---
Außerdem ist $r/2$ kleiner als $r$, weil $r$ positiv ist.
---
Das ist falsch, weil $r$ die kleinste positive rationale Zahl sein sollte; also gibt es kein solches $r$.
:::
:::karte begriff Russellsche Antinomie
Was zeigt die Russellsche Antinomie über die Menge $M=\{N:N\notin N\}$ aller Mengen, die sich nicht selbst enthalten?
---
Dass diese Konstruktion unzulässig ist: Aus $M\in M$ folgt $M\notin M$, und aus $M\notin M$ folgt $M\in M$. Beides ist unmöglich.
--- falsch
Dass $M$ die Menge aller Mengen ist: Keine Menge enthält sich selbst, also erfüllt jede Menge die Bedingung, und $M$ enthält sie alle.
--- falsch
Dass $M\in M$ gilt: Weil $M$ alle Mengen enthält, die sich nicht selbst enthalten, enthält $M$ auch sich selbst, und es entsteht kein Widerspruch.
--- falsch
Dass Mengen keine unendlich vielen Elemente haben dürfen: Nur bei unendlichen Mengen kann eine Menge Element von sich selbst sein.
:::
:::karte begriff Axiom
Was ist ein Axiom, und warum baut man die Zahlen auf Axiomen auf?
---
Eine Grundannahme, die man festlegt und nicht beweist. Widersprüche wie die Russellsche Antinomie zeigen: Gewissheit gibt es nur relativ zu festgelegten Annahmen.
--- falsch
Eine Aussage, die so einleuchtend ist, dass sie keinen Beweis braucht. Man baut die Zahlen darauf auf, weil einleuchtende Aussagen niemals zu Widersprüchen führen können.
--- falsch
Ein Satz, der aus wenigen Grundannahmen bewiesen wurde und deshalb als gesichert gilt. Man baut die Zahlen darauf auf, weil bewiesene Sätze keine weiteren Annahmen brauchen.
--- falsch
Eine Grundannahme, die man festlegt und später beweist, sobald genug Rechenregeln bekannt sind. Bis dahin dient sie nur als vorläufige Arbeitshypothese.
:::
::::
