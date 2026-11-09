---
title: Stage 6: Several inputs, several stages
pfad: Electrical Engineering / 1st Semester / Fundamentals of Electrical Engineering / The Operational Amplifier
order: 1210800
summary: The rule was for one input and one op amp.
tags: summing amplifier, difference amplifier
lang: en
---

<span class="anker" id="stufe-6"></span>

:::zweck
The rule was for one input and one op amp. This stage shows that it handles several inputs and whole chains without a new idea, because all the equations remain linear.
:::

**The idea.** In the __summing amplifier__, several resistors lead to the minus input (Fig. [8](#abb-8)). The node stays at 0 V, so each source sees only its own resistor and drives $U_{\mathrm{E}i}/R_{\mathrm{E}i}$, independently of the others. The virtual ground decouples the sources. All the currents together flow through $R_\mathrm{F}$, the feedback resistor. In the __difference amplifier__, one voltage arrives at each input. Here the superposition from [Part 5](/wissen/en/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/quellen-und-ersatzquellen/quellen-und-ersatzquellen.html) helps: you calculate each source on its own, and the other becomes a wire.

:::satz Theorem 6.1 (Summing amplifier, difference amplifier, chain)
<span class="anker" id="satz-6-1"></span>

<span class="anker" id="gl-6-1"></span>
$$U_\mathrm{A}=-R_\mathrm{F}\sum_i\frac{U_{\mathrm{E}i}}{R_{\mathrm{E}i}}, \tag{6.1}$$

<span class="anker" id="gl-6-2"></span>
$$U_\mathrm{A}=\frac{R_1+R_2}{R_1}\cdot\frac{R_4}{R_3+R_4}\,U_\mathrm{E2}-\frac{R_2}{R_1}\,U_\mathrm{E1}. \tag{6.2}$$

For $R_3=R_1$ and $R_4=R_2$, what remains is $U_\mathrm{A}=\frac{R_2}{R_1}\,(U_\mathrm{E2}-U_\mathrm{E1})$. Stages in a chain multiply: $G=G_1\,G_2$.
:::

⁠**How to read it:** In [(6.2)](#gl-6-2), $U_\mathrm{E1}$ is at the minus input through $R_1$ and $U_\mathrm{E2}$ at the divider $R_3$, $R_4$ ahead of the plus input; $R_2$ leads back. **Validity:** Op amp in the linear range. With superposition only the sum has to lie within the limits; the partial results are calculation quantities.

:::herleitung Difference amplifier by superposition
With $U_\mathrm{E2}=0$ no current flows through $R_3$, $R_4$, and the plus input is at 0 V. This is the inverting amplifier: $U_\mathrm{A1}=-(R_2/R_1)\,U_\mathrm{E1}$. With $U_\mathrm{E1}=0$ the source becomes a wire, so $R_1$ stays connected to ground and must not be dropped, because the output drives current through it via $R_2$. This is the non-inverting amplifier with $\varphi_+=U_\mathrm{E2}\,R_4/(R_3+R_4)$: $U_\mathrm{A2}=\bigl(1+R_2/R_1\bigr)\varphi_+$. The sum is [(6.2)](#gl-6-2).
:::

:::abbildung et1/k11addsub 8
Left, the summing amplifier: the currents of the three sources meet at the node and flow through $R_\mathrm{F}$. Right, the difference amplifier with $R_1=R_3$ and $R_2=R_4$: at 2.00 V and 2.05 V both inputs are at 1.64 V.
:::

::::beispiel [Examples]
⁠*Summing amplifier* with $R_\mathrm{F}=40$ k$\Omega$, $R_\mathrm{E1}=R_\mathrm{E2}=10$ k$\Omega$, $R_\mathrm{E3}=20$ k$\Omega$ and $0.5$ V, $-0.2$ V, $0.1$ V: the currents are 50, $-20$ and 5 µ A, together 35 µ A, so $U_\mathrm{A}=-1.4$ V. *Difference amplifier* with $R_1=R_3=10$ k$\Omega$, $R_2=R_4=40$ k$\Omega$, $U_\mathrm{E1}=2.00$ V, $U_\mathrm{E2}=2.05$ V: $\varphi_+=0.8\cdot2.05\,\mathrm{V}=1.64$ V. Through $R_1$ flows $(2.00-1.64)\,\mathrm{V}/10\,\mathrm{k\Omega}=36$ µ A, so $U_\mathrm{A}=1.64\,\mathrm{V}-36\,\mu\text{A}\cdot40\,\mathrm{k\Omega}=0.2$ V. Superposition gives $-8.0\,\mathrm{V}+8.2\,\mathrm{V}$, the same. The common mode of about 2 V is gone. *Chain* of two inverting amplifiers with $G_1=-4$ and $G_2=-2$: 0.5 V becomes $-2$ V, then $+4$ V, so $G=+8$.
::::

⁠**Limiting case:** $U_\mathrm{E1}=U_\mathrm{E2}$ gives 0.

**Procedure for larger circuits.** First determine the potentials of the inputs, then calculate stage by stage from left to right. In a chain, each output is the input of the next stage, a potential with a fixed value.

:::frage In Part 6, two-ports in a chain loaded each other. Why may I multiply here?
Because the output resistance of the first stage is almost zero. The 10 k$\Omega$ of the second stage load 3.75 m$\Omega$, and the voltage loss is $4\cdot10^{-7}$ of the value. The loop of the first stage compensates for it.
:::

:::aufgabe Exercise 6 ★★★ Summing amplifier and unequal resistors
<span class="anker" id="aufg-6"></span>

(a) A summing amplifier has $R_\mathrm{F}=20$ k$\Omega$ and the input resistors 10, 20 and 5 k$\Omega$. How large is $U_\mathrm{A}$ for 1 V, $-2$ V and 0.5 V? (b) On the difference amplifier from the example, $R_4$ deviates upward by 1 % (40.4 k$\Omega$). Calculate the factors in front of $U_\mathrm{E2}$ and $U_\mathrm{E1}$. (c) What output voltage arises at $U_\mathrm{E1}=U_\mathrm{E2}=2$ V? (d) What is $U_\mathrm{A}$ now at 2.00 V and 2.05 V? Why must a difference amplifier have tightly toleranced resistors?

:::loesung
(a) $U_\mathrm{A}=-(2\cdot1+1\cdot(-2)+4\cdot0.5)\,\mathrm{V}=-2$ V. (b) In front of $U_\mathrm{E2}$: $5\cdot40.4/50.4=4.0079$, in front of $U_\mathrm{E1}$: 4. (c) $2\,\mathrm{V}\cdot0.0079=15.9$ mV instead of 0. (d) $4.0079\cdot2.05\,\mathrm{V}-8\,\mathrm{V}=0.216$ V instead of 0.200 V. The 8 % error comes almost entirely from the common mode. A resistor with 1 % deviation makes the rejection $4/0.0079$, that is, 54 dB, worse than the op amp itself.
:::
:::
