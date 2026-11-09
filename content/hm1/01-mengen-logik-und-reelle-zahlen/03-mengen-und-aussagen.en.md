---
title: Stage 1: Sets and statements
pfad: Electrical Engineering / 1st Semester / Higher Mathematics 1 / Sets, Logic and Real Numbers
order: 1210300
summary: Axioms speak about “all numbers with a property” and about “if, then.” This stage provides the language for that and a reliable method for proving rules for sets and statements.
tags: Venn diagram, elements, subset, superset, union, intersection, difference, complement
lang: en
---

<span class="anker" id="stufe-1"></span>

:::zweck
Axioms speak about “all numbers with a property” and about “if, then.” This stage provides the language for that and a reliable method for proving rules for sets and statements.
:::

**The idea.** For a set only one question counts: Does an object lie in it or not? The same goes for a statement: true or false? With two sets or statements there are therefore four cases, with three there are eight. You prove a rule by going through all the cases in a table. A __Venn diagram__ (sets drawn as regions) only illustrates; it shows one possible arrangement of the sets (Fig. [1](#abb-1)).

:::definition Definition 1.1 (Set)
<span class="anker" id="satz-1-1"></span>

A set is an unordered collection of definite, distinct objects, its __elements__. $x\in M$ means “$x$ is an element of $M$,” $x\notin M$ the opposite. For sets $A$, $B$ the following are defined:

| Symbol | Name | Meaning |
|---|---|---|
| $A\subset B$ | __subset__ | every element of $A$ lies in $B$ ($A=B$ is allowed); $B\supset A$: __superset__ |
| $A=B$ | equality | $A\subset B$ and $B\subset A$; otherwise one writes $A\ne B$ |
| $A\cup B$ | __union__ | all elements that lie in $A$ or in $B$, also in both |
| $A\cap B$ | __intersection__ | all elements that lie in $A$ and in $B$ |
| $A\setminus B$ | __difference__ | all elements of $A$ that do not lie in $B$ |
| $A^c$ | __complement__ | all elements of a fixed superset that do not lie in $A$ |
| $\emptyset=\{\,\}$ | __empty set__ | contains no element |
| $\mathcal P(A)$ | __power set__ | set of all subsets of $A$ |

$A$ and $B$ are called __disjoint__ if $A\cap B=\emptyset$.
:::

⁠**How to read it:** In the reference model, $A\cup B=\{1,2,3,4,5,6,7,11,12\}$, $A\cap B=\{2,3\}$, $A\setminus B=\{1,4,6,12\}$, $A^c=\{5,7,8,9,10,11\}$ relative to $G$. A set can be specified by a property: $\{x\in G:x\text{ even}\}=\{2,4,6,8,10,12\}$. We have $\mathcal P(\{5,7\})=\{\emptyset,\{5\},\{7\},\{5,7\}\}$. Always $\emptyset\subset A$, $A\cup\emptyset=A$, $A\cap\emptyset=\emptyset$, $A\setminus B=A\cap B^c$.

:::abbildung hm1/k1venn 1
Left, the elements of $G$ in the four regions. Right, $(A\cap B)^c$ is shaded: everything except the lens.
:::

:::definition Definition 1.2 (Statement and connectives)
<span class="anker" id="satz-1-2"></span>

A statement is an assertion that can only be true ($t$) or false ($f$). From statements $\mathcal A$, $\mathcal B$ new ones arise, defined by this __truth table__:

| $\mathcal A$ | $\mathcal B$ | $\neg\mathcal A$ | $\mathcal A\vee\mathcal B$ | $\mathcal A\wedge\mathcal B$ | $\mathcal A\Rightarrow\mathcal B$ | $\mathcal A\Leftrightarrow\mathcal B$ |
|---|---|---|---|---|---|---|
| $t$ | $t$ | $f$ | $t$ | $t$ | $t$ | $t$ |
| $t$ | $f$ | $f$ | $t$ | $f$ | $f$ | $f$ |
| $f$ | $t$ | $t$ | $t$ | $f$ | $t$ | $f$ |
| $f$ | $f$ | $t$ | $f$ | $f$ | $t$ | $t$ |

The names are __negation__, __disjunction__, __conjunction__, __implication__ and __equivalence__.
:::

⁠**How to read it:** “2 is a prime” is a true statement; “What time is it?” is not a statement. “Every even number from 4 on is the sum of two primes” is also a statement, even though nobody knows whether it is true (Goldbach's conjecture). Statements can depend on a __parameter__: $\mathcal T(n):=(n\text{ divides }12)$ is true for $n=4$ and false for $n=5$. “Or” includes “both.” $\neg$ binds most strongly: $\neg\mathcal A\vee\mathcal B$ means $(\neg\mathcal A)\vee\mathcal B$. $\mathcal A\Leftrightarrow\mathcal B$ is synonymous with $(\mathcal A\Rightarrow\mathcal B)\wedge(\mathcal B\Rightarrow\mathcal A)$. Two statements with the same table column are *equivalent*. If $\mathcal A\Rightarrow\mathcal B$ is true and $\mathcal A$ is true, then $\mathcal B$ is true. If $\mathcal A$ is false, the implication says nothing about $\mathcal B$.

:::frage Why is $f\Rightarrow t$ true? Surely nothing follows from something false.
It is true that a false $\mathcal A$ says nothing about $\mathcal B$. That is exactly why the implication is not violated then. The convention is forced: $\mathcal E(n)$ is supposed to be true for all $n$, and $n=6$ gives $f\Rightarrow t$, $n\le5$ gives $f\Rightarrow f$. If these rows were false, $\mathcal E(n)$ would be false there. Only $t\Rightarrow f$ occurs for no $n$, and that is the whole claim: $\{n\ge7\}$ lies in $\{n>5\}$. An implication is a subset relation.
:::

:::satz Theorem 1.3 (Rules and tautologies)
<span class="anker" id="satz-1-3"></span>

A __tautology__ is a statement that is true for all truth values of its building blocks. For sets in a common superset and for statements the following rules hold:

| Name | Sets | Statements |
|---|---|---|
| Double negation | $(A^c)^c=A$ | $\neg(\neg\mathcal A)\Leftrightarrow\mathcal A$ |
| Commutative | $A\cap B=B\cap A$, $A\cup B=B\cup A$ | $(\mathcal A\wedge\mathcal B)\Leftrightarrow(\mathcal B\wedge\mathcal A)$, $(\mathcal A\vee\mathcal B)\Leftrightarrow(\mathcal B\vee\mathcal A)$ |
| Associative | $(A\cap B)\cap C=A\cap(B\cap C)$, likewise with $\cup$ | $(\mathcal A\wedge(\mathcal B\wedge\mathcal C))\Leftrightarrow((\mathcal A\wedge\mathcal B)\wedge\mathcal C)$, likewise with $\vee$ |
| Distributive | $A\cap(B\cup C)=(A\cap B)\cup(A\cap C)$, $A\cup(B\cap C)=(A\cup B)\cap(A\cup C)$ | $(\mathcal A\wedge(\mathcal B\vee\mathcal C))\Leftrightarrow((\mathcal A\wedge\mathcal B)\vee(\mathcal A\wedge\mathcal C))$, $(\mathcal A\vee(\mathcal B\wedge\mathcal C))\Leftrightarrow((\mathcal A\vee\mathcal B)\wedge(\mathcal A\vee\mathcal C))$ |
| De Morgan | $(A\cap B)^c=A^c\cup B^c$, $(A\cup B)^c=A^c\cap B^c$ | $\neg(\mathcal A\wedge\mathcal B)\Leftrightarrow(\neg\mathcal A\vee\neg\mathcal B)$, $\neg(\mathcal A\vee\mathcal B)\Leftrightarrow(\neg\mathcal A\wedge\neg\mathcal B)$ |
| Idempotence | $A\cup A=A$, $A\cap A=A$ | $(\mathcal A\vee\mathcal A)\Leftrightarrow\mathcal A$, $(\mathcal A\wedge\mathcal A)\Leftrightarrow\mathcal A$ |
| Implication | $A\subset B\Leftrightarrow A^c\cup B=G$ ($G$ superset) | $(\mathcal A\Rightarrow\mathcal B)\Leftrightarrow(\neg\mathcal A\vee\mathcal B)$ |
| Contraposition | $A\subset B\Leftrightarrow B^c\subset A^c$ | $(\mathcal A\Rightarrow\mathcal B)\Leftrightarrow(\neg\mathcal B\Rightarrow\neg\mathcal A)$ |
| Transitivity | $(A\subset B\wedge B\subset C)\Rightarrow A\subset C$ | $((\mathcal A\Rightarrow\mathcal B)\wedge(\mathcal B\Rightarrow\mathcal C))\Rightarrow(\mathcal A\Rightarrow\mathcal C)$ |
:::

⁠**How to read it:** Left and right show the same rule, because every set relation is a statement about elements: $A\subset B$ means “for all $x$: $(x\in A)\Rightarrow(x\in B)$,” $A=B$ means “for all $x$: $(x\in A)\Leftrightarrow(x\in B)$,” and $x\in A\cap B$, $x\in A\cup B$, $x\in A\setminus B$ mean $(x\in A)\wedge(x\in B)$, $(x\in A)\vee(x\in B)$, $(x\in A)\wedge(x\notin B)$. The gates of digital electronics are $\neg$, $\wedge$, $\vee$ as circuits, and De Morgan makes it possible to build an AND from OR and inverters.

:::beweis De Morgan and contraposition by table
Go through all four cases of the building blocks. Reading $t$ as “$x$ lies in the set” makes this at the same time the proof for sets (__element table__).

| $\mathcal A$ | $\mathcal B$ | $\neg\mathcal A$ | $\neg\mathcal B$ | $\neg(\mathcal A\wedge\mathcal B)$ | $\neg\mathcal A\vee\neg\mathcal B$ | $\mathcal A\Rightarrow\mathcal B$ | $\neg\mathcal B\Rightarrow\neg\mathcal A$ |
|---|---|---|---|---|---|---|---|
| $t$ | $t$ | $f$ | $f$ | $f$ | $f$ | $t$ | $t$ |
| $t$ | $f$ | $f$ | $t$ | $t$ | $t$ | $f$ | $f$ |
| $f$ | $t$ | $t$ | $f$ | $t$ | $t$ | $t$ | $t$ |
| $f$ | $f$ | $t$ | $t$ | $t$ | $t$ | $t$ | $t$ |

Columns 5 and 6 agree, as do columns 7 and 8. The other rules work the same way. The transitivity of inclusion follows from that of implication: From $x\in A$ follows $x\in B$, and from that $x\in C$.
:::

::::beispiel
$(A\cap B)^c=G\setminus\{2,3\}$ has 10 elements. On the right stands $A^c\cup B^c=\{5,7,8,9,10,11\}\cup\{1,4,6,8,9,10,12\}$, the same 10 elements. Contraposition as a proof tool: Instead of “$n^2$ even $\Rightarrow$ $n$ even” one shows “$n$ odd $\Rightarrow$ $n^2$ odd”: $(2k+1)^2=2(2k^2+2k)+1$.
::::

⁠**Limiting cases:** For $B=\emptyset$, De Morgan becomes $G=G$. The domain matters: $(n\ge7\Leftrightarrow n>6)$ holds in $\mathbb{N}$; for $n=13/2$ it is $f\Leftrightarrow t$, hence false.

:::aufgabe Exercise 1 ★ Calculating with sets
<span class="anker" id="aufg-1"></span>

<ol class="al">

<li>

In the reference model, calculate $(A\cup B)^c$ and $A\setminus(A\cap B)$.

</li>

<li>

Show with an element table: $(A\setminus B)\cup(B\setminus A)=(A\cup B)\setminus(A\cap B)$.

</li>

<li>

How many elements does $\mathcal P(A\cap B)$ have? Predict how many $\mathcal P(M)$ has if $M$ has exactly $n$ elements, and justify it.

</li>

</ol>

:::loesung
(a) $A\cup B=\{1,2,3,4,5,6,7,11,12\}$, so $(A\cup B)^c=\{8,9,10\}$. $A\setminus(A\cap B)=A\setminus\{2,3\}=\{1,4,6,12\}$, which is $A\setminus B$. (b) For the cases $(\in,\in)$, $(\in,\notin)$, $(\notin,\in)$, $(\notin,\notin)$ of $x$ in $A$, $B$, both sides give $\notin,\in,\in,\notin$: $x$ lies in it if it lies in exactly one of the sets. (c) $A\cap B=\{2,3\}$ has 2 elements, $\mathcal P(A\cap B)$ has $2^2=4$. With $n$ elements you decide for each one individually: in or out. That makes $2^n$ subsets.
:::
:::

:::aufgabe Exercise 2 ★★ Reasoning with tables
<span class="anker" id="aufg-2"></span>

<ol class="al">

<li>

Show the transitivity of implication with a table of eight rows.

</li>

<li>

If the fuse is intact ($\mathcal A$), the lamp lights up ($\mathcal B$). This implication is true, and the lamp does not light up. What follows for the fuse? And if the lamp does light up?

</li>

<li>

Is $(\mathcal A\Rightarrow\mathcal B)\Leftrightarrow(\mathcal B\Rightarrow\mathcal A)$ a tautology?

</li>

</ol>

:::loesung
(a) The hypothesis $(\mathcal A\Rightarrow\mathcal B)\wedge(\mathcal B\Rightarrow\mathcal C)$ is true only for $(\mathcal A,\mathcal B,\mathcal C)=(t,t,t)$, $(f,t,t)$, $(f,f,t)$, $(f,f,f)$. In all four, $\mathcal A\Rightarrow\mathcal C$ is true. In the remaining four rows it is false, so the overall statement is true. (b) Contraposition: $\neg\mathcal B\Rightarrow\neg\mathcal A$, the fuse is not intact. If the lamp lights up, nothing follows: The row $f\Rightarrow t$ is allowed. (c) No: For $\mathcal A=t$, $\mathcal B=f$ the left side is $f\Leftrightarrow t$, hence false.
:::
:::
