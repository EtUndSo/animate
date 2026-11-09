---
title: Stage 9: Thevenin and Norton
pfad: Electrical Engineering / 1st Semester / Fundamentals of Electrical Engineering / Sources and Equivalent Sources
order: 1151100
summary: N is to feed many different loads.
tags: equivalent voltage source, equivalent current source, load characteristic
lang: en
---

<span class="anker" id="stufe-9"></span>

:::zweck
N is to feed many different loads. So far you would have to recalculate the entire network for each load. This stage replaces the network by a straight line, once and for all.
:::

**The idea.** Imagine the load replaced by a current source that draws exactly the current $I_\mathrm{A}$ from the network. The network notices no difference, since at the terminals it senses only this current. Now it contains only resistors and sources, so superposition is allowed. $U_\mathrm{AB}$ therefore consists of two parts: the share of the internal sources, which does not depend on the current, and the share of $I_\mathrm{A}$, which is proportional to it. A constant minus a factor times the current is a straight line. That is the entire reason why a linear network looks like a straight line from outside.

:::satz Theorem 9.1 (Equivalent sources: Thevenin and Norton)
<span class="anker" id="satz-9-1"></span>

Every linear one-port behaves at its terminals like an __equivalent voltage source__ and equally like an __equivalent current source__:

<span class="anker" id="gl-9-1"></span>
$$U_\mathrm{AB}=U_\mathrm{i}-R_\mathrm{i}\,I_\mathrm{A},\qquad\qquad I_\mathrm{A}=I_\mathrm{i}-G_\mathrm{i}\,U_\mathrm{AB}, \tag{9.1}$$

with

<span class="anker" id="gl-9-2"></span>
$$U_\mathrm{i}=U_\mathrm{OC},\qquad I_\mathrm{i}=I_\mathrm{SC},\qquad R_\mathrm{i}=\frac{1}{G_\mathrm{i}}=\frac{U_\mathrm{OC}}{I_\mathrm{SC}}. \tag{9.2}$$
:::

⁠**How to read it:** The first form is named after Thevenin, the second after Norton. $U_\mathrm{OC}$ is the voltage at open terminals, $I_\mathrm{SC}$ the current through the short-circuited terminals. $R_\mathrm{i}$ is the same in both forms. The straight line is also called the __load characteristic__. For small $R_\mathrm{i}$ you usually choose the Thevenin form, for large $R_\mathrm{i}$ the Norton form (Stage [6](spannungsquelle-oder-stromquelle.html#stufe-6)). **Validity:** The one-port must be linear, the load need not be. The statement holds only for the terminals; it says nothing about powers inside (Stage [6](spannungsquelle-oder-stromquelle.html#stufe-6)).

:::herleitung The straight line from superposition
With the imagined current source $I_\mathrm{A}$ at the terminals, [(8.1)](uberlagerung.html#gl-8-1) gives

$$U_\mathrm{AB}=\underbrace{\sum_k a_kU_{\mathrm{q}k}+\sum_k Z_kI_{\mathrm{q}k}}_{\text{internal sources}}\;\underbrace{-\,R_\mathrm{i}I_\mathrm{A}}_{\text{terminal current}}.$$

For $I_\mathrm{A}=0$ the first part remains, so it is $U_\mathrm{OC}$. With all internal sources turned off, the second part remains: there $R_\mathrm{i}$ is the total resistance of the turned-off network between A and B. The minus comes from the reference arrow: $I_\mathrm{A}$ flows out of A, so inside from B to A, with A lower. With $U_\mathrm{AB}=0$, $I_\mathrm{A}=I_\mathrm{SC}=U_\mathrm{OC}/R_\mathrm{i}$. Rearranging gives the second form.
:::

**Three ways to the two numbers.**

<ol>

<li>

⁠**Open circuit and short circuit:** Calculate or measure $U_\mathrm{OC}$ and $I_\mathrm{SC}$; $R_\mathrm{i}$ follows from [(9.2)](#gl-9-2).

</li>

<li>

⁠**Turning off the sources:** Voltage sources as wires, current sources as gaps, then determine the total resistance between A and B. That is $R_\mathrm{i}$. In addition, one of the two quantities $U_\mathrm{OC}$ or $I_\mathrm{SC}$.

</li>

<li>

⁠**Two load cases:** If you must not short-circuit, measure the points $(I_\mathrm{x},U_\mathrm{x})$ and $(I_\mathrm{y},U_\mathrm{y})$ with two loads. Both lie on the line, $U_\mathrm{x}=U_\mathrm{i}-R_\mathrm{i}I_\mathrm{x}$ and $U_\mathrm{y}=U_\mathrm{i}-R_\mathrm{i}I_\mathrm{y}$. Subtracting and substituting gives

<span class="anker" id="gl-9-3"></span>
$$R_\mathrm{i}=-\frac{U_\mathrm{x}-U_\mathrm{y}}{I_\mathrm{x}-I_\mathrm{y}},\qquad U_\mathrm{i}=U_\mathrm{x}+R_\mathrm{i}I_\mathrm{x}=\frac{U_\mathrm{x}I_\mathrm{y}-U_\mathrm{y}I_\mathrm{x}}{I_\mathrm{y}-I_\mathrm{x}}. \tag{9.3}$$

</li>

</ol>

:::abbildung et1/k5ersatz 10
Left, network N; right, its two equivalent sources. At the terminals, all three cannot be told apart.
:::

::::beispiel
For N, $U_\mathrm{OC}=9$ V is known from Stage [8](uberlagerung.html#stufe-8). In the short circuit, $R_2$ lies between two connected terminals and carries no current. The voltage source drives $U_\mathrm{q1}/R_1=3$ A through the terminals, the current source 1.5 A: $I_\mathrm{SC}=U_\mathrm{q1}/R_1+I_\mathrm{q2}=4.5$ A. From this follows $R_\mathrm{i}=9\,\mathrm{V}/4.5\,\mathrm{A}=2\,\Omega$. The second way confirms it: turned off, $R_1$ and $R_2$ are in parallel, $6\,\Omega\parallel3\,\Omega=2\,\Omega$. The Norton form has $I_\mathrm{i}=4.5$ A and $G_\mathrm{i}=0.5$ S (Fig. [10](#abb-10)).

These are exactly the numbers of the battery from Stage [5](reale-quellen-und-der-arbeitspunkt.html#stufe-5). Without looking at the network again, for 16 $\Omega$ it follows that $I_\mathrm{A}=9\,\mathrm{V}/18\,\Omega=0.5$ A and $U_\mathrm{AB}=8$ V. **Check** in the original: through $R_1$ come $(18-8)\,\mathrm{V}/6\,\Omega=1.667$ A, plus 1.5 A, which makes 3.167 A. Of this, $R_2$ takes the largest part with $8\,\mathrm{V}/3\,\Omega=2.667$ A, and 0.5 A goes to the load. If $I_\mathrm{q2}=0$, the voltage divider from partial circuit 1 would remain, with $U_\mathrm{i}=\frac{R_2}{R_1+R_2}U_\mathrm{q1}=6$ V, $I_\mathrm{i}=U_\mathrm{q1}/R_1=3$ A and unchanged $R_\mathrm{i}=R_1\parallel R_2$.

:::abbildung et1/k5geraden 11
The characteristic curves of N with one source and with both. Each source shifts the line upward in parallel; the slope $R_\mathrm{i}=2\,\Omega$ stays, because it depends only on the resistors. The sum of 6 V and 3 V and the sum of 3 A and 1.5 A are the superposition.
:::
::::

::::beispiel [Second example] a real current source
An ideal current source $I_\mathrm{q}=3$ A with $R_\mathrm{q}=20\,\Omega$ in parallel feeds terminal A through $R_\mathrm{v}=10\,\Omega$. Its other pole is B, and $R_\mathrm{p}=30\,\Omega$ lies between A and B. In the short circuit $R_\mathrm{p}$ is bypassed, and the current divider gives $I_\mathrm{SC}=I_\mathrm{q}\frac{R_\mathrm{q}}{R_\mathrm{q}+R_\mathrm{v}}=2$ A. In the open circuit $R_\mathrm{v}$ and $R_\mathrm{p}$ are in series. They carry $I_\mathrm{q}\frac{R_\mathrm{q}}{R_\mathrm{q}+R_\mathrm{v}+R_\mathrm{p}}=1$ A, so $U_\mathrm{OC}=R_\mathrm{p}\cdot1\,\mathrm{A}=30$ V. The quotient is $R_\mathrm{i}=15\,\Omega$. Turned off, the current source becomes a gap and its parallel resistor stays: $R_\mathrm{i}=R_\mathrm{p}\parallel(R_\mathrm{q}+R_\mathrm{v})=15\,\Omega$, or as a conductance $G_\mathrm{i}=G_\mathrm{p}+\frac{1}{R_\mathrm{q}+R_\mathrm{v}}$.
::::

⁠**Limiting cases:** If an ideal voltage source lies directly across the terminals, $R_\mathrm{i}=0$ and the Norton form does not exist. If an ideal current source lies in series with a terminal, $R_\mathrm{i}=\infty$ and the Thevenin form does not exist. If the sources exactly cancel, $U_\mathrm{OC}=0$ and $I_\mathrm{SC}=0$. Then the quotient fails, but Way 2 still gives $R_\mathrm{i}$.

:::ltspice Network and equivalent source side by side
⁠**Draw:** N with `voltage` 18, `res` 6 and `res` 3, the current source with 1.5 from ground to `a`. Next to it, separately, the equivalent source with `voltage` 9 and `res` 2 up to the net `b`. At `a` and at `b`, one current source `current` each with the value `{IZ}` to ground.

⁠**Directives:** `.param IZ=0`, `.step param IZ list 0 0.5 2.25 4.5`, `.op`

⁠**What you see:** `V(a)` and `V(b)` lie on top of each other: 9 V, 8 V, 4.5 V, 0 V. Build the network from Exercise [11](#aufg-11) in the same way: at `IZ=0` it shows your $U_\mathrm{OC}$, and at your $I_\mathrm{SC}$, `V(a)` falls to zero.
:::

:::frage Is N now really the same as the battery?
At the terminals yes. Every load shows the same current and the same voltage on both. Inside no: in the open circuit, N converts 27 W in $R_2$ and 13.5 W in $R_1$, while the battery rests. Equivalent sources answer questions at the terminals, and no others.
:::

:::aufgabe Exercise 10 ★★ Two load cases
<span class="anker" id="aufg-10"></span>

On an unknown linear device you measure 10 V and 1 A with 10 $\Omega$ at the terminals, then 8 V and 2 A with 4 $\Omega$. (a) Determine $R_\mathrm{i}$, $U_\mathrm{i}$ and $I_\mathrm{SC}$ with [(9.3)](#gl-9-3). (b) Predict current and voltage for 1 $\Omega$.

:::loesung
(a) $R_\mathrm{i}=-\frac{10-8}{1-2}\,\Omega=2\,\Omega$, $U_\mathrm{i}=10\,\mathrm{V}+2\,\Omega\cdot1\,\mathrm{A}=12$ V. Check with the fraction: $\frac{10\cdot2-8\cdot1}{2-1}\,\mathrm{V}=12$ V. $I_\mathrm{SC}=6$ A.

(b) $I_\mathrm{A}=12\,\mathrm{V}/3\,\Omega=4$ A, $U_\mathrm{AB}=4$ V.
:::
:::

:::aufgabe Exercise 11 ★★★ Two real sources
<span class="anker" id="aufg-11"></span>

Between B and a node C lie 2 $\Omega$ and, in parallel with it, an ideal current source of 5 A driving from B to C. From C, 3 $\Omega$ leads to a node D. From D, an ideal voltage source of 4 V leads to terminal A, with its plus terminal at D. Between A and B lie 5 $\Omega$. (a) Calculate $U_\mathrm{OC}$ by superposition. (b) Calculate $R_\mathrm{i}$ by turning off the sources, and from it $I_\mathrm{SC}$. (c) Limiting case: The voltage source has 10 V. What do open circuit and short circuit show, and what is $R_\mathrm{i}$ now?

:::loesung
(a) Current source only (voltage source as a wire, terminals open): the 5 A feed 2 $\Omega$ in parallel with $3\,\Omega+5\,\Omega$, so $2\,\Omega\parallel8\,\Omega=1.6\,\Omega$, and C is at 8 V against B. The divider of 3 $\Omega$ and 5 $\Omega$ gives $U'=8\,\mathrm{V}\cdot\frac58=5$ V.

Voltage source only (current source open): it drives $4\,\mathrm{V}/10\,\Omega=0.4$ A from the plus terminal through 3 $\Omega$ and 2 $\Omega$ to B and through the 5 $\Omega$ from B to A. So A lies 2 V lower than B: $U''=-2$ V. Together: $U_\mathrm{OC}=3$ V. In general $U_\mathrm{OC}=\frac{I_\mathrm{q2}R_\mathrm{q2}-U_\mathrm{q1}}{R_\mathrm{q1}+R_\mathrm{q2}+R_3}\,R_3$, if $R_\mathrm{q1}$ is the 3 $\Omega$, $R_\mathrm{q2}$ the 2 $\Omega$ and $R_3$ the 5 $\Omega$.

(b) Turned off, 3 $\Omega$ and 2 $\Omega$ are in series and in parallel with 5 $\Omega$: $R_\mathrm{i}=5\,\Omega\parallel5\,\Omega=2.5\,\Omega$. Thus $I_\mathrm{SC}=3\,\mathrm{V}/2.5\,\Omega=1.2$ A. Directly: the current source with 2 $\Omega$ acts like 10 V with 2 $\Omega$ (Stage [6](spannungsquelle-oder-stromquelle.html#stufe-6)). The 5 $\Omega$ are short-circuited, so $I_\mathrm{SC}=(10\,\mathrm{V}-4\,\mathrm{V})/5\,\Omega=1.2$ A.

(c) With 10 V the two shares cancel: $U_\mathrm{OC}=0$ and $I_\mathrm{SC}=0$. The quotient is indeterminate, but $R_\mathrm{i}$ stays 2.5 $\Omega$, because it does not depend on the sources. From outside, the network is a pure resistor.
:::
:::
