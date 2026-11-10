---
title: Stufe 2: Der Vektorraum
pfad: Elektrotechnik / 1. Semester / HöMa1 – Höhere Mathematik 1 / Vektoren und Skalarprodukt
adresse: elektrotechnik/1-semester/hohere-mathematik-1/vektoren-und-skalarprodukt
knoten: Kapitel 8: Vektoren und Skalarprodukt
order: 1280400
summary: Polynome haben keine Pfeilspitze, und doch rechnet man mit ihnen wie mit Pfeilen.
tags: kommutative Gruppe, Kommutativgesetz, Assoziativgesetz, neutrales Element, Inverses, Vektorraum, linearer Raum, Vektoraddition
lang: de
---

<span class="anker" id="stufe-2"></span>

:::zweck
Polynome haben keine Pfeilspitze, und doch rechnet man mit ihnen wie mit Pfeilen. Diese Stufe zieht heraus, welche Regeln man wirklich braucht.
:::

**Die Idee.** Addiert man die Polynome $p$ und $q$ Stelle für Stelle, entsteht $r$, genau wie bei Pfeilen: Bei $x=2$ ist $3+3=6$ (Abb. [3](#abb-3)). Jetzt schreibt man die wenigen Regeln auf, die alle Rechnungen tragen, und nennt sie Axiome. Was aus ihnen folgt, gilt dann für jedes Objekt, das sie erfüllt, ohne neuen Beweis.

:::abbildung hm1/k8polynome 3
Die Polynome $p$, $q$ und $r=p+q$. An jeder Stelle $x$ addieren sich die Werte: Bei $x=2$ stapeln sich $p(2)=3$ und $q(2)=3$ zu $r(2)=6$. Bei $x=-1$ sind alle drei null. Ein Polynom ist hier ein Vektor mit einer Komponente je Stelle $x$.
:::

:::definition Definition 2.1 (Kommutative Gruppe)
<span class="anker" id="satz-2-1"></span>

Eine Menge $G\ne\emptyset$ mit einer Verknüpfung $+:G\times G\to G$, $(a,b)\mapsto a+b$, heißt __kommutative Gruppe__ $(G,+)$, falls für alle $a,b,c\in G$ gilt:

<ul>

<li>

⁠**(A1)** $a+b=b+a$ (__Kommutativgesetz__),

</li>

<li>

⁠**(A2)** $a+(b+c)=(a+b)+c$ (__Assoziativgesetz__),

</li>

<li>

⁠**(A3)** es gibt $0\in G$ mit $a+0=a$ für alle $a\in G$ (__neutrales Element__),

</li>

<li>

⁠**(A4)** zu jedem $a\in G$ gibt es $b\in G$ mit $a+b=0$ (__Inverses__, Schreibweise $b=:-a$).

</li>

</ul>
:::

:::definition Definition 2.2 (Vektorraum)
<span class="anker" id="satz-2-2"></span>

Eine Menge $V\ne\emptyset$ heißt __Vektorraum__ über $\mathbb K$ (auch __linearer Raum__), wenn eine Verknüpfung $+_V:V\times V\to V$, $(\vec u,\vec v)\mapsto\vec u+_V\vec v$, genannt __Vektoraddition__, und eine Abbildung $\bullet_s:\mathbb K\times V\to V$, $(\alpha,\vec u)\mapsto\alpha\bullet_s\vec u$, genannt __skalare Multiplikation__, definiert sind, so dass für alle $\alpha,\beta\in\mathbb K$ und $\vec u,\vec v\in V$ gilt:

<ul>

<li>

⁠**(V1)** $(V,+_V)$ ist eine kommutative Gruppe,

</li>

<li>

⁠**(V2)** $\alpha\bullet_s(\vec u+_V\vec v)=(\alpha\bullet_s\vec u)+_V(\alpha\bullet_s\vec v)$,

</li>

<li>

⁠**(V3)** $(\alpha+\beta)\bullet_s\vec u=(\alpha\bullet_s\vec u)+_V(\beta\bullet_s\vec u)$ und $(\alpha\cdot\beta)\bullet_s\vec u=\alpha\bullet_s(\beta\bullet_s\vec u)$,

</li>

<li>

⁠**(V4)** $1\bullet_s\vec u=\vec u$ für die Eins $1\in\mathbb K$ (__Normierung__).

</li>

</ul>
:::

⁠**So liest man das:** Die Elemente von $V$ heißen Vektoren, die von $\mathbb K$ heißen __Skalare__. Die Zusätze $V$ und $s$ zeigen: Links in (V3) steht das Plus in $\mathbb K$, rechts das Plus in $V$. (V2) und der erste Teil von (V3) ähneln dem Distributivgesetz in $\mathbb{R}$, der zweite Teil von (V3) dem Assoziativgesetz. Deshalb multipliziert man wie gewohnt aus, und ab jetzt entfallen die Zusätze: $\vec u+\vec v$, $\alpha\vec u$. Das neutrale Element heißt Nullvektor $\vec0$, es gilt $\vec u+\vec0=\vec u=\vec0+\vec u$. Das Inverse erfüllt $\vec u+(-\vec u)=\vec0$. **Voraussetzung nötig:** Ohne (V4) dürfte man auf $\mathbb{R}^2$ die Streckung $\alpha\bullet\vec u:=\vec0$ für alle $\alpha,\vec u$ wählen. (V1) bis (V3) gelten dann, aber Strecken vernichtet alles.

:::satz Satz 2.3 (Folgerungen aus den Axiomen)
<span class="anker" id="satz-2-3"></span>

In jedem Vektorraum gilt für alle $\alpha\in\mathbb K$ und $\vec u\in V$:

$$0\cdot\vec u=\vec0,\qquad\alpha\cdot\vec0=\vec0,\qquad(-1)\cdot\vec u=-\vec u.$$
:::

⁠**So liest man das:** Links steht die Zahl 0, rechts der Vektor $\vec0$. Die Aussagen sehen selbstverständlich aus, stehen aber in keinem Axiom. Für Polynome besagen sie $0\cdot p=$ Nullfunktion und $(-1)\cdot p=-p$, ohne dass man es dort nachrechnen muss.

:::beweis Aus den Axiomen
⁠*Zweite Regel.* Aus $\vec0+\vec u=\vec u$ folgt mit (V2) $\alpha\cdot\vec0+\alpha\cdot\vec u=\alpha\cdot\vec u$. Addiert man auf beiden Seiten $-(\alpha\cdot\vec u)$, bleibt mit (A2), (A4) und (A3) $\alpha\cdot\vec0=\vec0$.

⁠*Erste Regel.* In $\mathbb K$ ist $0+0=0$, nach (V3) also $0\cdot\vec u+0\cdot\vec u=0\cdot\vec u$. Addiert man $-(0\cdot\vec u)$, bleibt $0\cdot\vec u=\vec0$.

⁠*Dritte Regel.* Mit (V4), (V3) und der ersten Regel ist $\vec u+(-1)\cdot\vec u=1\cdot\vec u+(-1)\cdot\vec u=(1+(-1))\cdot\vec u=0\cdot\vec u=\vec0$. Das Inverse ist eindeutig: Aus $\vec u+\vec b=\vec0$ folgt $\vec b=\vec b+(\vec u+(-\vec u))=(\vec b+\vec u)+(-\vec u)=-\vec u$. Also ist $(-1)\cdot\vec u=-\vec u$.
:::

**Wichtige Vektorräume.**

<ol class="al">

<li>

$V=\mathbb{R}^n$ über $\mathbb K=\mathbb{R}$ mit [(1.1)](pfeile-addieren-und-strecken.html#gl-1-1). Die Axiome folgen Komponente für Komponente aus den Rechenregeln in $\mathbb{R}$, (V2) etwa aus $\alpha(x_j+y_j)=\alpha x_j+\alpha y_j$.

</li>

<li>

$V=\mathbb{C}^n$ über $\mathbb K=\mathbb{C}$, mit denselben Formeln. Auch $\mathbb{C}^n$ über $\mathbb K=\mathbb{R}$ ist ein Vektorraum, aber ein anderer, denn es sind weniger Streckungen erlaubt (Aufgabe [5](lineare-unabhangigkeit.html#aufg-5)).

</li>

<li>

__Funktionenraum__: Für eine Menge $M\ne\emptyset$ ist $V=\{f:M\to\mathbb K\}$ ein Vektorraum über $\mathbb K$ mit den __punktweisen__ Verknüpfungen $(f+g)(m):=f(m)+g(m)$ und $(\alpha\cdot f)(m):=\alpha\cdot f(m)$. Speziell ist $V=\{p:\mathbb{R}\to\mathbb{R}\mid p\text{ ist Polynom}\}$ ein Vektorraum, denn Summe und Vielfaches von Polynomen sind wieder Polynome.

</li>

<li>

__Euklidische Ebene__ $\mathbb{R}^2$ und __euklidischer Raum__ $\mathbb{R}^3$ oder $\mathbb{R}^n$: der Fall (a), gelesen als Pfeile $\vec u=\overrightarrow{OP}$, identifiziert mit Punkten. Dann bedeutet $+$ hintereinanderhängen und $\cdot$ strecken oder stauchen.

</li>

</ol>

⁠**Grenzfälle:** Für $n=1$ sind die Vektoren die reellen Zahlen selbst. Der kleinste Vektorraum ist $\{\vec0\}$. In der Elektrotechnik sind Signale Vektoren: Zwei Spannungsverläufe addieren sich punktweise wie $p$ und $q$.

:::frage Ein Polynom hat doch keine Richtung. Wie kann es ein Vektor sein?
Richtung und Länge gehören nicht zur Definition. Vektor heißt nur: Element eines Vektorraums. Jeder Beweis dieser Stufe benutzt allein die Axiome, also passt er auch auf Polynome. Länge und Winkel kommen erst in Stufe [5](skalarprodukt-norm-abstand.html#stufe-5).
:::

:::aufgabe Aufgabe 2 ★★★ Ein ungewohnter Vektorraum
<span class="anker" id="aufg-2"></span>

Sei $V=(0,\infty)$ über $\mathbb{R}$ mit $x\oplus y:=x\cdot y$ und $\alpha\odot x:=x^\alpha$. (a) Was ist hier der Nullvektor, was das Inverse von $x$? (b) Prüfe (V2) bis (V4). (c) Was sagt Satz [2.3](#satz-2-3) über $0\odot x$ und $(-1)\odot x$ aus? (d) Warum scheitert $V=(0,\infty)$ mit der gewöhnlichen Addition und Multiplikation?

:::loesung
(a) Nullvektor ist die Zahl 1, denn $x\oplus1=x$. Das Inverse ist $\frac1x$, denn $x\oplus\frac1x=1$. (A1), (A2) sind die Gesetze der Multiplikation. (b) (V2): $\alpha\odot(x\oplus y)=(xy)^\alpha=x^\alpha y^\alpha$. (V3): $x^{\alpha+\beta}=x^\alpha x^\beta$ und $x^{\alpha\beta}=(x^\beta)^\alpha$. (V4): $x^1=x$. (c) $0\odot x=x^0=1$, also der Nullvektor, und $(-1)\odot x=x^{-1}$, also das Inverse. Die Potenzregeln sind hier Sätze über Vektorräume. (d) Mit dem gewöhnlichen Plus fehlt das neutrale Element, denn $0\notin(0,\infty)$, und $(-1)\cdot x$ verlässt die Menge.
:::
:::
