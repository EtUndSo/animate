---
title: Stage 5: The rule and the virtual ground
pfad: Electrical Engineering / 1st Semester / ET1 – Fundamentals of Electrical Engineering 1: Introduction to Circuit Analysis / The Operational Amplifier
adresse: elektrotechnik/1-semester/grundlagen-der-elektrotechnik/der-operationsverstarker
knoten: Chapter 11: The Operational Amplifier
order: 1210700
summary: Stage 4 calculated with A .
tags: inverting amplifier
lang: en
---

<span class="anker" id="stufe-5"></span>

:::zweck
Stage [4](gegenkopplung.html#stufe-4) calculated with $A$. But the deviation is tiny. This stage turns this into a rule for all circuits with negative feedback and applies it to the most important case: the input at the minus terminal.
:::

**The idea.** In every circuit, $|U_\mathrm{D}|\le11\,\mathrm{V}/100000=110$ µ V as long as the output does not hit its limit. Compared with voltages in the volt range, that is nothing. So if you calculate with $U_\mathrm{D}=0$, you make an error of the order of $1/(A\beta)$. With that, $A$ is no longer needed.

:::satz Theorem 5.1 (The rule for the op amp with negative feedback)
<span class="anker" id="satz-5-1"></span>

As long as $U_\mathrm{A,min}<U_\mathrm{A}<U_\mathrm{A,max}$,

<ol>

<li>

$\varphi_+=\varphi_-$: The output adjusts itself so that the difference vanishes.

</li>

<li>

$I_+=I_-=0$: No current flows into the inputs.

</li>

<li>

The output supplies any current needed. No node equation is written for the output node.

</li>

</ol>

Set up the node rule at the minus input, solve for $U_\mathrm{A}$, and check the limits last.
:::

In the __inverting amplifier__, the plus input is at ground, $U_\mathrm{E}$ arrives at the minus input through $R_1$, and $R_2$ leads back from the output (Fig. [7](#abb-7)). From $\varphi_-=\varphi_+=0$ and $I_-=0$ it follows that

<span class="anker" id="gl-5-1"></span>
$$\frac{U_\mathrm{E}}{R_1}+\frac{U_\mathrm{A}}{R_2}=0\quad\Rightarrow\quad U_\mathrm{A}=-\frac{R_2}{R_1}\,U_\mathrm{E},\qquad R_\mathrm{in}=\frac{U_\mathrm{E}}{I_1}=R_1. \tag{5.1}$$

⁠**How to read it:** $I_1$ is the current through $R_1$. $R_\mathrm{in}$ is the resistance the source sees: only $R_1$, because its right end is firmly at 0 V. With finite $A$, $G=-(R_2/R_1)\big/\bigl(1+1/(A\beta)\bigr)$ with the same $\beta=R_1/(R_1+R_2)$. **Validity:** like the rule, and $A\beta\gg1$.

:::herleitung Finite $A$ in the inverting amplifier
Superposition at the divider of $R_1$ and $R_2$ gives $\varphi_-=(R_2\,U_\mathrm{E}+R_1\,U_\mathrm{A})/(R_1+R_2)$. With $\varphi_+=0$, $U_\mathrm{D}=-\varphi_-$, so $U_\mathrm{A}=-A\,\varphi_-$. Solving: $U_\mathrm{A}(1+A\beta)=-A\,(1-\beta)\,U_\mathrm{E}$ with $1-\beta=R_2/(R_1+R_2)$. Because $A(1-\beta)=A\beta\cdot R_2/R_1$, the formula follows. The loop sees $U_\mathrm{E}$ as a fixed value, so $\beta$ is the same divider as in Stage [4](gegenkopplung.html#stufe-4).
:::

**The mechanism of the virtual ground.** At $U_\mathrm{E}=1$ V, the voltage across $R_1$ drives a current of 100 µ A to the minus input. It cannot enter the op amp. So it has to go through $R_2$. For 100 µ A through 40 k$\Omega$, the right end of $R_2$ must be 4 V lower, so the output goes to $-4$ V. The current continues into the output and through the lower output transistor to $U_\mathrm{B-}$ (red line in Fig. [7](#abb-7)). At the node only the tiny voltage $\varphi_-=-U_\mathrm{D}=U_\mathrm{A}/(-A)=+40$ µ V remains. The node behaves like a ground but is not one:

<ul>

<li>

A real ground takes in current. The virtual one passes it on to $R_2$; nothing flows between the node and ground.

</li>

<li>

A real ground always stays at 0 V. The virtual one holds its potential only because the output keeps readjusting. If the output is at its limit, the virtual ground is gone (Fig. [7](#abb-7) bottom).

</li>

<li>

If you connect the node to ground with a wire, the 100 µ A flows there, $R_2$ carries no current, and $U_\mathrm{A}=0$.

</li>

</ul>

**Why no input current flows nevertheless.** There is almost no voltage between the inputs, but no conductor either. They have the same potential but are not connected: 40 µ V across $r_\mathrm{e}=1$ M$\Omega$ gives 40 pA, 2.5 million times less than $I_1$. Both act together: the differential stage has a high resistance, and the loop leaves it almost no voltage.

:::frage At 0 V at the node with current arriving, shouldn't the minus input have zero resistance?
That is how it looks to the source: behind $R_1$ it sees a point that holds its potential no matter what current arrives. But that is done by the output via $R_2$. The input itself remains high-resistance at 1 M$\Omega$.
:::

:::abbildung et1/k11invert 7
Top, the inverting amplifier, in red the current path at $U_\mathrm{E}=+1$ V. Bottom, the limit: $\hat u_\mathrm{E}=3.5$ V would give 14 V, and the output hits its limit at $\pm11$ V. Then $\varphi_-$ rises to as much as 0.6 V, and the virtual ground is gone.
:::

::::beispiel
$U_\mathrm{A}=-4\cdot1\,\mathrm{V}=-4$ V, more precisely $-3.9998$ V with finite $A$. $R_\mathrm{in}=10$ k$\Omega$. With a load of 2 k$\Omega$ to ground, 2 mA flows, and the output takes in 2.1 mA: load plus feedback. The source $U_\mathrm{E}$ notices nothing of this.
::::

⁠**Limiting cases:** $R_2=R_1$ only reverses the sign. $R_2\to0$ gives $U_\mathrm{A}=0$.

**The first limit.** Rule 1 assumes that the output reaches the demanded voltage. At $G=-4$ this ends at $|U_\mathrm{E}|=11\,\mathrm{V}/4=2.75$ V. Above that, $U_\mathrm{A}=\mp11$ V is fixed, the loop is open, and the divider of $R_1$ and $R_2$ determines the node: $\varphi_-=0.8\,U_\mathrm{E}+0.2\,U_\mathrm{A}$, so $+0.6$ V at 3.5 V.

:::aufgabe Exercise 5 ★★ Inverting amplifier
<span class="anker" id="aufg-5"></span>

$R_1=4.7$ k$\Omega$, $R_2=47$ k$\Omega$, $U_\mathrm{E}=0.5$ V. (a) Determine $U_\mathrm{A}$, $I_1$ and $R_\mathrm{in}$. (b) At $A=100000$, how large are $\varphi_-$ and the exact $G$? (c) A load of 1 k$\Omega$ hangs on the output. How large is the output current, and where does it come from? (d) Up to which $U_\mathrm{E}$ does the output reach? How large is $\varphi_-$ at $U_\mathrm{E}=2$ V?

:::loesung
(a) $U_\mathrm{A}=-10\cdot0.5\,\mathrm{V}=-5$ V, $I_1=106.4$ µ A, $R_\mathrm{in}=4.7$ k$\Omega$. (b) $\varphi_-=5\,\mathrm{V}/A=50$ µ V. With $\beta=4.7/51.7=0.0909$, $G=-10/(1+1.1\cdot10^{-4})=-9.9989$. (c) The load carries 5 mA, the feedback 0.106 mA. Into the output flow 5.11 mA, onward to $U_\mathrm{B-}$. (d) $|U_\mathrm{E}|\le1.1$ V. At 2 V, $U_\mathrm{A}=-11$ V and $\varphi_-=(47\cdot2-4.7\cdot11)\,\mathrm{V}/51.7=0.818$ V.
:::
:::
