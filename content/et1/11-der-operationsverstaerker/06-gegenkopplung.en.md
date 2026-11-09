---
title: Stage 4: Negative feedback
pfad: Electrical Engineering / 1st Semester / Fundamentals of Electrical Engineering / The Operational Amplifier
order: 1210600
summary: Without feedback the op amp is a switch.
tags: Feedback, positive feedback, non-inverting amplifier, voltage follower
lang: en
---

<span class="anker" id="stufe-4"></span>

:::zweck
Without feedback the op amp is a switch. This stage shows why a fed-back part of the output brings the difference of the inputs almost to zero, and why the gain then no longer depends on $A$.
:::

**The idea.** __Feedback__ means that part of the output quantity gets back to the input. If it counteracts the cause, it is negative feedback; if it reinforces the cause, it is __positive feedback__. With an op amp the path to the minus input gives negative feedback, because every voltage there acts with a negative sign.

In the __non-inverting amplifier__, $U_\mathrm{E}$ is at the plus input (Fig. [6](#abb-6)). The divider of $R_2$ and $R_1$ reports one fifth of the output to the minus input. Now apply $U_\mathrm{E}=1$ V. At first $U_\mathrm{A}=0$, so $\varphi_-=0$ and $U_\mathrm{D}=1$ V. The target value $A\,U_\mathrm{D}$ would be 100 kV, and the output runs upward. At 4 V output, $\varphi_-=0.8$ V, so 200 mV are still missing. At 4.9 V, 20 mV are missing, at 4.99 V only 2 mV, and the target has shrunk to 200 V. The output catches up with its target only when the two are equal: $A\,U_\mathrm{D}=U_\mathrm{A}$. That happens at $U_\mathrm{A}\approx5$ V and $U_\mathrm{D}=5\,\mathrm{V}/100000=50$ µ V. A drop would also be corrected immediately: if the output falls, $\varphi_-$ sinks, $U_\mathrm{D}$ grows, and the output rises.

The small difference is thus not a basic law of the component but the result of the loop. It cannot be zero, because without a difference there would be no output.

:::satz Theorem 4.1 (Amplifier with negative feedback)
<span class="anker" id="satz-4-1"></span>

If the fraction $\beta$ of the output is fed to the minus input and $U_\mathrm{E}$ is at the plus input, then in the linear range

<span class="anker" id="gl-4-1"></span>
$$U_\mathrm{D}=\frac{U_\mathrm{E}}{1+A\beta},\qquad G=\frac{U_\mathrm{A}}{U_\mathrm{E}}=\frac{A}{1+A\beta}=\frac1\beta\cdot\frac{1}{1+\dfrac1{A\beta}}. \tag{4.1}$$

For $A\beta\gg1$, $G\approx1/\beta$ with the relative deviation $-1/(A\beta)$. A change in $A$ acts weakened by the factor $1+A\beta$:

<span class="anker" id="gl-4-2"></span>
$$\frac{\Delta G}{G}\approx\frac{1}{1+A\beta}\cdot\frac{\Delta A}{A}. \tag{4.2}$$

With the divider, $\beta=R_1/(R_1+R_2)$, so $G\approx1+R_2/R_1$.
:::

⁠**How to read it:** $\beta$ is the fed-back fraction, between 0 and 1, here 0.2. $G$ is the gain of the whole circuit. $A\beta$ is the loop gain: a small change at $U_\mathrm{D}$ is amplified by $A$ and reported back weakened by $\beta$. Here $A\beta=20000$; this is the reserve that keeps the deviation small. **Validity:** $U_\mathrm{A,min}<U_\mathrm{A}<U_\mathrm{A,max}$, input current small compared with the divider current, $A$ at the frequency under consideration (Stage [10](wo-die-regeln-enden.html#stufe-10)).

:::herleitung The loop in equilibrium and in motion
Equilibrium: $U_\mathrm{A}=A\,U_\mathrm{D}$ and $U_\mathrm{D}=U_\mathrm{E}-\beta\,U_\mathrm{A}$. Substituting gives $U_\mathrm{D}=U_\mathrm{E}-A\beta\,U_\mathrm{D}$, and from this [(4.1)](#gl-4-1). Differentiating $G$ with respect to $A$ gives $\mathrm{d} G/\mathrm{d} A=1/(1+A\beta)^2$; dividing by $G$ yields [(4.2)](#gl-4-2).

Motion: inside the op amp, a current proportional to $U_\mathrm{D}$ charges a capacitance. The output therefore cannot jump but runs after its target value: $\tau\,\mathrm{d} U_\mathrm{A}/\mathrm{d} t=A\,U_\mathrm{D}-U_\mathrm{A}$, here with $\tau=A/(2\pi f_\mathrm{T})=15.9$ ms. This is the equation of the RC circuit from [Part 3](/wissen/en/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/der-kondensator/der-kondensator.html). With $U_\mathrm{D}=U_\mathrm{E}-\beta\,U_\mathrm{A}$ it becomes

$$\tau\,\frac{\mathrm{d} U_\mathrm{A}}{\mathrm{d} t}=A\,U_\mathrm{E}-(1+A\beta)\,U_\mathrm{A}.$$

The factor in front of $U_\mathrm{A}$ is negative, so every deviation decays: $U_\mathrm{A}(t)=G\,U_\mathrm{E}\,(1-\mathrm{e}^{-t/\tau_G})$ with $\tau_G=\tau/(1+A\beta)=0.80$ µ s. The loop is 20001 times faster than the op amp alone.
:::

:::abbildung et1/k11schleife 5
Left, the loop as a block diagram: at the summing point, $\beta\,U_\mathrm{A}$ is subtracted. Right, the response to a step from 0 to 1 V in the linear model: $U_\mathrm{A}$ rises with $\tau_G=0.80$ µ s to 5 V, $U_\mathrm{D}$ falls from 1 V to 50 µ V.
:::

::::beispiel
With $A\beta=20000$, 1 V at the input becomes $U_\mathrm{A}=4.99975$ V; the deviation from the ideal 5 V is 0.005 % $=1/(A\beta)$. The specimens scatter by a factor of four:

| $A$ | $U_\mathrm{D}$ | $U_\mathrm{A}$ | Deviation from 5 V |
|---|---|---|---|
| 50000 | 99.99 µ V | 4.99950 V | $-0.0100$ % |
| 100000 | 50.00 µ V | 4.99975 V | $-0.0050$ % |
| 200000 | 25.00 µ V | 4.99988 V | $-0.0025$ % |

A change in $A$ of 300 % shifts $G$ by 0.0075 %. You trade gain for accuracy: 100000 becomes 5, but in return two resistors determine the result.
::::

⁠**In short:** The gain is the reciprocal of the fed-back fraction. **Limiting cases:** $A\to\infty$ gives $U_\mathrm{D}\to0$ and $G=1/\beta$. $\beta\to0$ gives $G\to A$; without feedback, the open loop remains.

**Input and output.** At the plus input only $U_\mathrm{D}=50$ µ V lies across $r_\mathrm{e}$, so 50 pA flows, one two-millionth of the divider current of 100 µ A. The input resistance thus rises to $r_\mathrm{e}(1+A\beta)=20$ G$\Omega$. At the output, the loop acts against any loading: if a load pulls $U_\mathrm{A}$ down a little, $U_\mathrm{D}$ grows, and the internal voltage rises until the loss is almost compensated. The output resistance falls to $r_\mathrm{a}/(1+A\beta)=3.75$ m$\Omega$.

**The voltage follower.** With $R_2=0$ and $R_1\to\infty$, the output is connected directly to the minus input, $\beta=1$, $G=A/(1+A)=0.99999$. This __voltage follower__ does not amplify but isolates: input resistance 100 G$\Omega$, output resistance 0.75 m$\Omega$. A voltmeter of 1 M$\Omega$ on a source with 1 V and 100 k$\Omega$ internal resistance shows 0.909 V ([Part 4](/wissen/en/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/strom-und-spannung-messen/strom-und-spannung-messen.html)). With a voltage follower in front it shows 0.99999 V.

:::abbildung et1/k11nichtinv 6
Left, the non-inverting amplifier with potentials in the reference model. The minus input is only 50 µ V below the plus input. Right, the voltage follower as the limiting case $\beta=1$.
:::

:::frage Why not simply use an amplifier with $G=5$ instead of buying 100000 and discarding almost all of it?
Because its 5 would depend on $B$, $U_\mathrm{Early}$ and the temperature: a 1 % change inside would be 1 % in the result. With the reserve $A\beta=20000$ this becomes $5\cdot10^{-5}$ %.
:::

:::frage Just now the output is too low, so it jumps up, and then it is too high. Shouldn't it swing back and forth forever?
It would if it jumped to $A\,U_\mathrm{D}$ in one step: the error would be multiplied by 20000 on every trip around the loop. But the output does not jump. The internal capacitance limits its speed; it runs continuously and brakes as $U_\mathrm{D}$ shrinks. So it arrives without overshoot (derivation above).
:::

:::ltspice Measuring the difference
⁠**Draw:** `voltage` `VE` with 1 from net `p` to ground. A controlled source `e` as the op amp: output from net `a` to ground, control inputs `p` (plus) and `m` (minus), value `{A}`. `res` `R2` 40k from `a` to `m`, `R1` 10k from `m` to ground.

⁠**Directives:** `.param A=1e5`, `.step param A list 5e4 1e5 2e5`, `.op`, `.options numdgt=15`, `.meas op ua FIND V(a) AT=1e5`, `.meas op ud FIND V(p,m) AT=1e5`.

⁠**What you see:** `ua` = 4.99975 V, `ud` = 49.9975 µ V, as in the calculation. With `AT=5e4` you get 4.99950 V and 99.99 µ V. For Exercise [4](#aufg-4) set `R2` to 100k. Then swap `p` and `m`: `.op` shows 5.00025 V. Why that does not hold in reality is clarified in Stage [9](mitkopplung-und-der-schmitt-trigger.html#stufe-9).
:::

:::aufgabe Exercise 4 ★★ Scatter and reserve
<span class="anker" id="aufg-4"></span>

The amplifier is to have $G=11$, with $R_1=10$ k$\Omega$. (a) Choose $R_2$. How large are $\beta$ and $A\beta$? (b) How large is $U_\mathrm{D}$ at $U_\mathrm{A}=5.5$ V? (c) Calculate $G$ for $A=50000$ and $200000$. (d) What is the minimum $A$ that suffices for 0.1 % deviation? (e) What happens at $U_\mathrm{E}=2$ V? How large is $U_\mathrm{D}$ then?

:::loesung
(a) $1+R_2/R_1=11$, so $R_2=100$ k$\Omega$. $\beta=1/11=0.0909$, $A\beta=9091$. (b) $5.5\,\mathrm{V}/100000=55$ µ V. (c) $G=10.99758$ and $10.99940$, a difference of 0.016 %. (d) $1/(1+1/(A\beta))=0.999$ gives $A\beta=999$, so $A\ge10989$. (e) By calculation 22 V; the output is at 11 V. Then $\varphi_-=\beta\cdot11\,\mathrm{V}=1$ V and $U_\mathrm{D}=1$ V; the rule does not hold.
:::
:::
