---
title: Key points
pfad: Electrical Engineering / 1st Semester / Fundamentals of Electrical Engineering / The Operational Amplifier
order: 1211300
summary: How a huge, imprecise factor turns into a component whose behavior is determined by the resistors alone
tags: differential amplifier, loop gain, virtual ground, Noise, Comparator
lang: en
---

:::merke The answer in three sentences
<ol>

<li>

Inside sits a __differential amplifier__, a circuit that responds only to the difference between two voltages: $U_\mathrm{A}=A\,U_\mathrm{D}$ with $U_\mathrm{D}=\varphi_+-\varphi_-$. With $A=100000$ and at most 11 V at the output, this leaves a window of $\pm110$ µ V for $U_\mathrm{D}$.

</li>

<li>

Negative feedback routes the fraction $\beta$ of the output to the minus input. The output runs until the loop comes to rest, and that happens when $U_\mathrm{D}$ is just enough for the output: 5 V need 50 µ V. The gain becomes $G\approx1/\beta$, and the __loop gain__ $A\beta$ (the factor for one trip around the loop) only sets the small deviation.

</li>

<li>

This yields a rule: equal potentials at the inputs, no current into them, node rule at the minus input. It explains the __virtual ground__ (a node at 0 V with no connection to ground) and all the basic circuits. It ends where the output hits its limit, where the feedback changes sign, and where $A\beta$ becomes small.

</li>

</ol>
:::

:::kern Key points
<ul>

<li>

Noise: $u_\mathrm{r,eff}=\sqrt{\int|u_\mathrm{r}(f)|^2\mathrm{d} f}$, thermal $|u_\mathrm{r,R}|^2=4k_\mathrm{B}TR$. Amplifying does not change the SNR; it helps only against later disturbances. $\mathrm{SNR}_\mathrm{dB}=20\lg(u_\mathrm{s}/u_\mathrm{r})$.

</li>

<li>

Differential amplifier: fixed total current, $U_\mathrm{A}=S\,R_\mathrm{C}\,U_\mathrm{D}$, each BE junction carries $U_\mathrm{D}/2$, common mode has no effect.

</li>

<li>

Model: $U_\mathrm{A}=A(\varphi_+-\varphi_-)$ up to the limits. Window $\pm110$ µ V, comparator without feedback.

</li>

<li>

Negative feedback: $U_\mathrm{D}=U_\mathrm{E}/(1+A\beta)$, $G=\frac1\beta\cdot\frac1{1+1/(A\beta)}$, $\Delta G/G=\frac{1}{1+A\beta}\Delta A/A$. The output runs until the loop rests. At 5 V, 50 µ V remains.

</li>

<li>

Rule: $\varphi_+=\varphi_-$, $I_\pm=0$, node rule at the minus input, check the limits last. Virtual ground: 0 V through regulation, no path to ground. The current runs through the feedback into the output.

</li>

<li>

$G=-R_2/R_1$, $G=1+R_2/R_1$, $U_\mathrm{A}=-R_\mathrm{F}\sum U_{\mathrm{E}i}/R_{\mathrm{E}i}$, $U_\mathrm{A}=\frac{R_2}{R_1}(U_\mathrm{E2}-U_\mathrm{E1})$, integrator $-\frac{1}{RC}\int u_\mathrm{E}\mathrm{d} t$, differentiator $-RC\,\mathrm{d} u_\mathrm{E}/\mathrm{d} t$, logarithmic amplifier $-U_T\ln(U_\mathrm{E}/RI_\mathrm{S})$, exponential amplifier $-RI_\mathrm{S}\mathrm{e}^{U_\mathrm{E}/U_T}$, transimpedance $-R\,I_\mathrm{E}$, NIC $R_\mathrm{in}=-R_2$.

</li>

<li>

Positive feedback: the effect reinforces the cause, output at the limit, thresholds $\beta\,U_\mathrm{A,max}$ and $\beta\,U_\mathrm{A,min}$.

</li>

<li>

Limits: overdrive, $U_\mathrm{off}/\beta$, $I_\mathrm{B}R_2$, CMRR, $G\,f_G=f_\mathrm{T}$.

</li>

</ul>
:::

**One principle behind all the results.** The output of an op amp with negative feedback is not a calculation with $A$ but the state in which the loop comes to rest. For this, $A$ only has to be large; its exact value does not matter.

| Result | Where it comes from |
|---|---|
| __Noise__ (random interference voltage), signal-to-noise ratio | Individual charges move at random; amplifying raises signal and disturbance alike (Stage [1](rauschen.html#stufe-1)) |
| $U_\mathrm{A}=S\,R_\mathrm{C}\,U_\mathrm{D}$, common mode without effect | A fixed total current: only its division can change (Stage [2](der-differenzverstarker.html#stufe-2)) |
| __Comparator__ (voltage comparison circuit) | Without feedback, almost no input voltage fits into the window (Stage [3](der-opv-ohne-ruckfuhrung.html#stufe-3)) |
| $U_\mathrm{D}=U_\mathrm{A}/A$, $G\approx1/\beta$ | The output runs until the loop comes to rest (Stage [4](gegenkopplung.html#stufe-4)) |
| $G=-R_2/R_1$, virtual ground | Rule and node rule at the minus input (Stage [5](die-regel-und-die-virtuelle-masse.html#stufe-5)) |
| Summing amplifier, difference amplifier, chain | Currents add, effects superpose (Stage [6](mehrere-eingange-mehrere-stufen.html#stufe-6)) |
| Integrator, logarithmic amplifier | One component sets the current, the other the voltage (Stage [7](rechnen-mit-kondensator-und-diode.html#stufe-7)) |
| Current-to-voltage converter, negative resistance | The output supplies any current the rule demands (Stage [8](strom-als-signal.html#stufe-8)) |
| Schmitt trigger | Wrong sign: the effect reinforces its cause (Stage [9](mitkopplung-und-der-schmitt-trigger.html#stufe-9)) |
| Limits of the rule | Everything that reduces $A\beta$ or shifts $U_\mathrm{D}$ (Stage [10](wo-die-regeln-enden.html#stufe-10)) |
