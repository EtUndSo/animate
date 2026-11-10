---
title: Stage 3: The op amp without feedback
pfad: Electrical Engineering / 1st Semester / ET1 – Fundamentals of Electrical Engineering 1: Introduction to Circuit Analysis / The Operational Amplifier
adresse: elektrotechnik/1-semester/grundlagen-der-elektrotechnik/der-operationsverstarker
knoten: Chapter 11: The Operational Amplifier
order: 1210500
summary: The amplifier stages become a component with a few terminals.
tags: saturation, ideal op amp, flash converter
lang: en
---

<span class="anker" id="stufe-3"></span>

:::zweck
The amplifier stages become a component with a few terminals. This stage fixes its model and shows what it does without an external circuit: it compares.
:::

**The idea.** The op amp has two inputs, one output and two terminals for the supply, $U_\mathrm{B+}$ and $U_\mathrm{B-}$ (Fig. [3](#abb-3)). It has no ground terminal: the output refers to the middle of the supply. Every output current comes from the supply terminals, which are usually omitted in circuit diagrams. That is why the three visible terminals do not satisfy the node rule.

The output delivers $A$ times $U_\mathrm{D}$, but only up to its limits. With $\pm11$ V and $A=100000$ the linear portion already ends at $\pm110$ µ V. Any larger difference drives the output to a limit, __saturation__.

:::definition Definition 3.1 (Model of the op amp)
<span class="anker" id="satz-3-1"></span>

<span class="anker" id="gl-3-1"></span>
$$U_\mathrm{D}=\varphi_+-\varphi_-,\qquad U_\mathrm{A}=\begin{cases}U_\mathrm{A,max}&\text{for }A\,U_\mathrm{D}\ge U_\mathrm{A,max},\\A\,U_\mathrm{D}&\text{in between},\\U_\mathrm{A,min}&\text{for }A\,U_\mathrm{D}\le U_\mathrm{A,min}.\end{cases} \tag{3.1}$$

The __ideal op amp__ has $r_\mathrm{e}\to\infty$ (no input current), $A\to\infty$ at all frequencies, $r_\mathrm{a}=0$ (the output current adjusts itself so that all node and mesh equations are satisfied) and no noise.
:::

⁠**How to read it:** $U_\mathrm{A,max}<U_\mathrm{B+}$ and $U_\mathrm{A,min}>U_\mathrm{B-}$, because between the output and the supply there are transistors across which voltage drops, here 1 V each. **Validity:** The model is static; the sluggishness of the output follows in Stage [4](gegenkopplung.html#stufe-4).

:::abbildung et1/k11opv 3
Left, the circuit symbol with supply terminals. Right, the characteristic curve in the reference model. The slope is $A$, and the linear portion is only $\pm110$ µ V wide. Note the axis: on a scale in volts it would be a vertical step.
:::

**The comparator.** Without feedback, $|U_\mathrm{D}|$ is almost always larger than the window. The op amp then only reports which input is higher: $U_\mathrm{A,max}$ for $\varphi_+>\varphi_-$, $U_\mathrm{A,min}$ for $\varphi_+<\varphi_-$. This is the comparator. One application is the __flash converter__, an analog-to-digital converter (Fig. [4](#abb-4)). A voltage divider produces comparison voltages, and each comparator compares $U_\mathrm{E}$ with one of them. All work at the same time, hence the name (flash, as in lightning). $n$ bits need $2^n-1$ comparators, so 8 bits need 255.

:::abbildung et1/k11flash 4
2-bit flash converter with $U_\mathrm{Ref}=6$ V and equal resistors. The inputs draw no current, so the resistors are in series, and the taps are at 6, 4 and 2 V. At $U_\mathrm{E}=3.2$ V only K3 switches up.
:::

::::beispiel
At $U_\mathrm{E}=3.2$ V, $U_\mathrm{D}=-2.8$ V at K1, $-0.8$ V at K2 and $+1.2$ V at K3. K1 and K2 are at $-11$ V, K3 at $+11$ V. The three outputs distinguish four ranges: below 2 V, 2 to 4 V, 4 to 6 V, above 6 V.
::::

⁠**Limiting case:** For $A\to\infty$ the window becomes a point and the characteristic curve a step at $U_\mathrm{D}=0$.

:::aufgabe Exercise 3 ★ Comparators
<span class="anker" id="aufg-3"></span>

(a) A flash converter as in Fig. [4](#abb-4) has $U_\mathrm{Ref}=9$ V. Where are the taps? Which comparators are high at $U_\mathrm{E}=4$ V? (b) How many comparators are needed for 3 bits? (c) Op amp V sees $U_\mathrm{D}=50$ µ V, then 300 µ V. How large is $U_\mathrm{A}$ in each case?

:::loesung
(a) 9, 6 and 3 V. At 4 V only K3 has $U_\mathrm{D}>0$ ($+1$ V); K1 and K2 have $-5$ V and $-2$ V. (b) $2^3-1=7$. (c) 5 V in the window. At 300 µ V it would be 30 V; the output is at 11 V.
:::
:::
