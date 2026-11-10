---
title: Stage 2: Quantifiers and indirect proof
pfad: Electrical Engineering / 1st Semester / HöMa1 – Higher Mathematics 1 / Sets, Logic and Real Numbers
adresse: elektrotechnik/1-semester/hohere-mathematik-1/mengen-logik-und-reelle-zahlen
knoten: Chapter 1: Sets, Logic and Real Numbers
order: 1210400
summary: All axioms have the form “for all x there is a y .” This stage clarifies how to read and negate such sentences, and how to turn a negation into a proof.
tags: universal quantifier, existential quantifier, counterexample, contradiction hypothesis, Russell's paradox
lang: en
---

<span class="anker" id="stufe-2"></span>

:::zweck
All axioms have the form “for all $x$ there is a $y$.” This stage clarifies how to read and negate such sentences, and how to turn a negation into a proof.
:::

**The idea.** “For all $x$ in $\{x_1,x_2,\dots\}$, $\mathcal A(x)$ holds” is a long and: $\mathcal A(x_1)\wedge\mathcal A(x_2)\wedge\dots$ “There is an $x$” is a long or. When negating, De Morgan turns and into or. That is why negation turns “for all” into “there is.”

:::definition Definition 2.1 (Quantifiers)
<span class="anker" id="satz-2-1"></span>

$\forall$ means “for all” (__universal quantifier__), $\exists$ “there is at least one” (__existential quantifier__), $\exists_1$ “there is exactly one,” $\nexists$ “there is no.”
:::

⁠**How to read it:** True examples in the reference model are $\forall x\in A:x\le12$; $\exists x\in A:x>5$ (for instance $x=6$); $\exists_1x\in A\cap B:x>2$ (namely $x=3$); $\nexists x\in B:x=9$. Divisibility is also a quantifier statement: $m\mid p$ (“$m$ divides $p$”) means $\exists n\in\mathbb{N}:m\cdot n=p$, so $6\mid12$ because $6\cdot2=12$, and $7\nmid12$. The set of primes is $\{p\in\mathbb{N}\setminus\{1\}:\nexists m\in\{2,\dots,p-1\}\text{ with }m\mid p\}$.

:::satz Theorem 2.2 (Negation rule)
<span class="anker" id="satz-2-2"></span>

<span class="anker" id="gl-2-1"></span>
$$\neg\bigl(\forall x\in M:\mathcal A(x)\bigr)\Leftrightarrow\bigl(\exists x\in M:\neg\mathcal A(x)\bigr),\quad \neg\bigl(\exists y\in N:\mathcal B(y)\bigr)\Leftrightarrow\bigl(\forall y\in N:\neg\mathcal B(y)\bigr). \tag{2.1}$$
:::

⁠**How to read it:** Swap the quantifier, negate the statement; with nested quantifiers, one after the other. In the reference model, the negation of $\forall n\in\mathbb{N}:\mathcal E(n)$ is the false statement $\exists n\in\mathbb{N}:(n\ge7\wedge n\le5)$. **Proof idea:** $\neg(\mathcal A(x_1)\wedge\mathcal A(x_2)\wedge\dots)$ is by De Morgan $\neg\mathcal A(x_1)\vee\neg\mathcal A(x_2)\vee\dots$; the second rule arises the same way. **Limiting case** $M=\emptyset$: “For all $x\in\emptyset$” is always true, “there is $x\in\emptyset$” always false.

:::frage Do five examples suffice to prove “for all”?
No. An example only checks one $x$. By [(2.1)](#gl-2-1), on the other hand, a single __counterexample__ refutes a “for all” statement. Conversely, “there is” is proved with one example.
:::

::::beispiel nested quantifiers
Let $H$ be the devices of a household, $F$ the fuses, and let $K(g,s)$ mean “device $g$ is connected to fuse $s$.” Then

$$\mathcal P:=\bigl(\forall g\in H\ \exists s\in F:K(g,s)\bigr),\qquad \mathcal Q:=\bigl(\exists s\in F\ \forall g\in H:K(g,s)\bigr)$$

say different things (Fig. [2](#abb-2)): In $\mathcal P$, $s$ may depend on the device; in $\mathcal Q$, one fuse serves all. From $\mathcal Q$ follows $\mathcal P$; the converse is false. **The order of different quantifiers must not be swapped.** The negations are $\neg\mathcal P=(\exists g\ \forall s:\neg K(g,s))$, one device is connected to no fuse, and $\neg\mathcal Q=(\forall s\ \exists g:\neg K(g,s))$, every fuse leaves out at least one device.

:::abbildung hm1/k1quantoren 2
The right picture satisfies both statements, the left one only the first.
:::
::::

:::satz Theorem 2.3 (Indirect proof)
<span class="anker" id="satz-2-3"></span>

If $\neg\mathcal A\Rightarrow\mathcal B$ is true and $\mathcal B$ is false, then $\mathcal A$ is true.
:::

⁠**How to read it:** You assume the opposite of the claim (__contradiction hypothesis__) and reason until something false comes out. A look at the table shows the mechanism: If $\neg\mathcal A$ were true, $\mathcal B$ would have to be true as well. So $\neg\mathcal A$ is false. To show an implication $\mathcal A\Rightarrow\mathcal B$ indirectly, the assumption by De Morgan is $\mathcal A\wedge\neg\mathcal B$. **Example:** There is no smallest positive rational number. Assumption: $r$ is the smallest. Then $r/2$ is rational, positive and smaller than $r$. That is false, so there is no such $r$.

**Why axioms are needed.** Let $M=\{N:N\notin N\}$ be the set of all sets that do not contain themselves (__Russell's paradox__, 1903). If $M\in M$ is true, $M$ does not satisfy the condition, so $M\notin M$. If $M\notin M$ is true, $M$ satisfies the condition, so $M\in M$. Both are impossible; the construction is inadmissible. Just as contradictory is the sentence “This sentence is false.” Such findings triggered the foundational crisis of mathematics, from Hilbert's demand for a consistent structure (1900) to Gödel's incompleteness theorems (1931). The lesson: Certainty exists only relative to agreed assumptions. That is why numbers are built on axioms.

:::aufgabe Exercise 3 ★★ Negating and proving indirectly
<span class="anker" id="aufg-3"></span>

<ol class="al">

<li>

Negate: “Every circuit contains a component that gets warm.”

</li>

<li>

Negate $\forall\varepsilon>0\ \exists n\in\mathbb{N}:\frac1n<\varepsilon$. Does the statement become true or false if the quantifiers are swapped?

</li>

<li>

Show indirectly: If $n^2$ is odd, then $n$ is odd.

</li>

</ol>

:::loesung
(a) “There is a circuit in which no component gets warm.” (b) Negation: $\exists\varepsilon>0\ \forall n\in\mathbb{N}:\frac1n\ge\varepsilon$. Swapped: $\exists n\in\mathbb{N}\ \forall\varepsilon>0:\frac1n<\varepsilon$ is false, because for $\varepsilon=\frac1n$ we get $\frac1n<\frac1n$. The original statement, by contrast, is true, as Stage [6](das-vollstandigkeitsaxiom.html#stufe-6) shows. (c) Assumption: $n^2$ odd and $n$ even, $n=2k$. Then $n^2=2\cdot2k^2$ is even, a contradiction.
:::
:::
