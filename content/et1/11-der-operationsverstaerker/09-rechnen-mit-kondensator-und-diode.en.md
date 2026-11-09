---
title: Stage 7: Calculating with capacitor and diode
pfad: Electrical Engineering / 1st Semester / Fundamentals of Electrical Engineering / The Operational Amplifier
order: 1210900
summary: So far one resistor turned voltage into current and a second turned current into voltage.
tags: 
lang: en
---

<span class="anker" id="stufe-7"></span>

:::zweck
So far one resistor turned voltage into current and a second turned current into voltage. This stage inserts other components without changing the rule. That is how the op amp got its name: it carries out mathematical operations.
:::

**The idea.** If the plus input is at ground, the node rule at the minus input says: the current of the input component flows entirely through the feedback component, $I_\mathrm{in}=-I_\mathrm{fb}$. The input component sees $U_\mathrm{E}$ and supplies a current. The feedback component sees $U_\mathrm{A}$ and has to carry the same current. Which function arises is determined solely by their current-voltage laws (Fig. [9](#abb-9)).

:::satz Theorem 7.1 (Operations)
<span class="anker" id="satz-7-1"></span>

With the plus input at ground and an ideal op amp,

<span class="anker" id="gl-7-1"></span>
<span class="anker" id="gl-7-2"></span>
<span class="anker" id="gl-7-3"></span>
<span class="anker" id="gl-7-4"></span>
$$\begin{aligned} \text{Integrator: }&u_\mathrm{A}(t)=u_\mathrm{A}(0)-\frac{1}{R\,C}\int_0^t u_\mathrm{E}(t')\,\mathrm{d} t', \\ \text{Differentiator: }&u_\mathrm{A}(t)=-R\,C\,\frac{\mathrm{d} u_\mathrm{E}}{\mathrm{d} t}, \\ \text{Logarithmic amplifier: }&U_\mathrm{A}=-U_T\,\ln\frac{U_\mathrm{E}}{R\,I_\mathrm{S}}, \\ \text{Exponential amplifier: }&U_\mathrm{A}=-R\,I_\mathrm{S}\,\mathrm{e}^{U_\mathrm{E}/U_T}. \end{aligned} \tag{7.1|7.2|7.3|7.4}$$
:::

⁠**How to read it:** $R\,C$ is a time constant in s, $I_\mathrm{S}$ the saturation reverse current of the diode, $U_T=26$ mV. **Validity:** [(7.3)](#gl-7-3) requires $U_\mathrm{E}>0$ and $U_\mathrm{E}/R\gg I_\mathrm{S}$, [(7.4)](#gl-7-4) requires $U_\mathrm{E}\gg U_T$, and all require an output within its limits.

:::herleitung Four node rules
Integrator: $i=u_\mathrm{E}/R$ flows through $R$. It charges the capacitor, $C\,\mathrm{d} u_C/\mathrm{d} t=i$. The left plate is firmly at 0, so $u_\mathrm{A}=-u_C$. Differentiator: $i=C\,\mathrm{d} u_\mathrm{E}/\mathrm{d} t$ through the capacitor at the input, $u_\mathrm{A}=-R\,i$. Logarithmic amplifier: $I=U_\mathrm{E}/R$ flows through the diode, so $I=I_\mathrm{S}\,\mathrm{e}^{U_\mathrm{F}/U_T}$ with the diode voltage $U_\mathrm{F}=-U_\mathrm{A}$. Solving gives [(7.3)](#gl-7-3). Exponential amplifier: $U_\mathrm{E}$ is across the diode, and its current $I_\mathrm{S}\,\mathrm{e}^{U_\mathrm{E}/U_T}$ flows through $R$.
:::

:::abbildung et1/k11bauteile 9
Four circuits, one rule: the left component turns the input voltage into a current, and the upper one demands an output voltage for it. The nodes are at virtual ground.
:::

::::beispiel [Examples]
⁠*Integrator* with $R=10$ k$\Omega$, $C=10$ nF, so $R\,C=100$ µ s. At $U_\mathrm{E}=1$ V a fixed current of 100 µ A flows. Unlike in the RC circuit from [Part 3](/wissen/en/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/der-kondensator/der-kondensator.html), it does not decrease during charging, because the voltage across $R$ stays at 1 V. $u_\mathrm{A}$ falls steadily by 10 V/ms and reaches $-11$ V after 1.1 ms. A square wave of $\pm1$ V at 1 kHz becomes a triangle wave of $\pm2.5$ V. *Differentiator* with the same $R\,C$: a triangle wave of $\pm1$ V at 1 kHz rises by 4 V/ms, and $u_\mathrm{A}$ becomes a square wave of $\pm0.4$ V. For a sine wave its magnitude grows with frequency, $\hat u_\mathrm{A}/\hat u_\mathrm{E}=2\pi f\,R\,C$: 0.63 at 1 kHz, 62.8 at 100 kHz. That is why it amplifies high-frequency noise (Stage [1](rauschen.html#stufe-1)) particularly strongly. *Logarithmic amplifier* with $R=10$ k$\Omega$ and $I_\mathrm{S}=1.9\cdot10^{-13}$ A: 0.1 V, 1 V, 10 V give $-0.462$ V, $-0.522$ V, $-0.582$ V. Each decade (factor of 10) adds $U_T\ln10=59.9$ mV. *Exponential amplifier* with the same values: 0.5 V gives $-0.427$ V, and every 18 mV more doubles the magnitude.
::::

⁠**Limiting cases:** $u_\mathrm{E}=0$ leaves the integrator standing; it holds $u_\mathrm{A}(0)$. At $U_\mathrm{E}<0$ the diode of the logarithmic amplifier blocks, the feedback is interrupted, and the output runs to its limit: the rule holds only as long as the return path conducts.

**Multiplying.** Because $\ln x+\ln y=\ln(x\,y)$, a chain multiplies in analog fashion: two logarithmic amplifiers, a summing amplifier, an exponential amplifier. At the output, up to a fixed factor, stands the product $U_x\,U_y$. Because $U_T$ and $I_\mathrm{S}$ depend on temperature, in practice the diodes are replaced by transistors with additional temperature compensation. Before digital computers, such circuits formed calculating machines, hence the name operational amplifier.

:::aufgabe Exercise 7 ★★ Integrator
<span class="anker" id="aufg-7"></span>

$R=100$ k$\Omega$, $C=10$ nF, $u_\mathrm{A}(0)=0$. (a) How large is $R\,C$? Where is $u_\mathrm{A}$ after 10 ms at $U_\mathrm{E}=-0.2$ V? (b) When does the output hit its limit? (c) A square wave of $\pm0.5$ V at 100 Hz is applied. What is the amplitude of the triangle wave? What happens at 20 Hz?

:::loesung
(a) $R\,C=1$ ms. $u_\mathrm{A}$ rises at 200 V/s, to $+2$ V after 10 ms. (b) After $11\,\mathrm{V}/(200\,\mathrm{V/s})=55$ ms. (c) A half period of 5 ms changes $u_\mathrm{A}$ by 2.5 V, so the amplitude is 1.25 V. At 20 Hz the swing is 12.5 V. With $u_\mathrm{A}(0)=0$ and a positive start, the triangle wave reaches $-11$ V and hits the limit.
:::
:::

:::aufgabe Exercise 8 ★★ Logarithmic amplifier
<span class="anker" id="aufg-8"></span>

$R=1$ k$\Omega$, $I_\mathrm{S}=1.9\cdot10^{-13}$ A. (a) Calculate $U_\mathrm{A}$ for 1 V and 2 V. Predict the difference without using $I_\mathrm{S}$. (b) How far does $U_\mathrm{A}$ sweep when $U_\mathrm{E}$ runs from 10 mV to 10 V? (c) At 330 K instead of 300 K, $U_T=28.6$ mV. By how much does that alone shift $U_\mathrm{A}$ at a current of 100 µ A?

:::loesung
(a) 1 mA gives $-0.582$ V, 2 mA gives $-0.600$ V. The difference is $U_T\ln2=18$ mV, without $I_\mathrm{S}$. (b) Three decades: $3\cdot59.9\,\mathrm{mV}=180$ mV. (c) $U_\mathrm{F}$ grows from 0.522 V to 0.574 V, that is, by 52 mV. In reality $I_\mathrm{S}$ also rises strongly, which is why temperature compensation is needed.
:::
:::
