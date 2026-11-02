---
title: Stage 10: Three basic circuits
pfad: Electrical Engineering / 1st Semester / Fundamentals of Electrical Engineering / The Bipolar Transistor
order: 1201200
summary: Input and output need two terminals each, and the transistor has three in total.
tags: common-emitter circuit, common-collector circuit, emitter follower, common-base circuit, voltage swing, buffer
lang: en
---

<span class="anker" id="stufe-10"></span>

:::zweck
Input and output need two terminals each, and the transistor has three in total. So one terminal becomes common for the signal. This stage works out the three possibilities.
:::

**The idea.** The common terminal gives the circuit its name (Fig. [12](#abb-12)). In the __common-emitter circuit__, the signal comes in at the base and leaves from the collector. $u_\mathrm{in}$ lies fully across the BE path and produces $i_\mathrm{c}=S\,u_\mathrm{in}$. This current flows through $R_\mathrm{C}$ and pulls the collector potential down: the output is inverted. In the __common-collector circuit__, the signal comes in at the base and leaves from the emitter. The emitter follows the base: if it stood still, $U_\mathrm{BE}$ would change, and the resulting current would at once raise it via $R_\mathrm{E}$. That is why it is also called the __emitter follower__. In the __common-base circuit__, the base is held fixed and the signal comes in at the emitter. If the emitter falls, $U_\mathrm{BE}$ rises, and more current pulls the collector down: input and output move in the same sense. The magnitude corresponds to the common-emitter circuit.

:::abbildung et1/k10grundschaltungen 12
Top, the three basic circuits; bottom, their characteristics from the reference model with $U_\mathrm{CC}=12$ V. Common emitter ($R_\mathrm{C}=3$ k$\Omega$): falling, steep around 0.6 V. Common collector ($R_\mathrm{E}=3$ k$\Omega$): the output lies around 0.6 V below the input (gray). Common base: like the common emitter, mirrored at the vertical axis, rising.
:::

:::satz Theorem 10.1 (Voltage gain of the basic circuits)
<span class="anker" id="satz-10-1"></span>

For small signals in the active region, $r_\mathrm{CE}$ neglected, $A=u_\mathrm{out}/u_\mathrm{in}$:

<span class="anker" id="gl-10-1"></span>
$$A_\mathrm{emitter}=-S\,R_\mathrm{C}=-\frac{U_{R_\mathrm{C}}}{U_T},\qquad A_\mathrm{collector}=\frac{S\,R_\mathrm{E}}{1+S\,R_\mathrm{E}}<1,\qquad A_\mathrm{base}=+S\,R_\mathrm{C}. \tag{10.1}$$

With an emitter resistor, $A=-R_\mathrm{C}/(R_\mathrm{E}+1/S)\approx-R_\mathrm{C}/R_\mathrm{E}$; with $r_\mathrm{CE}$, $A_\mathrm{emitter}=-S\,(R_\mathrm{C}\parallel r_\mathrm{CE})$.
:::

⁠**How to read it:** $U_{R_\mathrm{C}}=I_\mathrm{C}R_\mathrm{C}$ is the DC voltage across the collector resistor, 6 V in the reference model. **In short:** the gain of the common-emitter circuit is the DC voltage across the collector resistor divided by $U_T$. Neither $B$ nor the transistor type appears in it. **Validity:** $|u_\mathrm{be}|\ll U_T$, $R_\mathrm{C}\ll r_\mathrm{CE}$, driven by a source with low internal resistance.

:::herleitung Three meshes in the small signal
For the signal, $U_\mathrm{CC}$ is ground. Common emitter: $u_\mathrm{be}=u_\mathrm{in}$, $u_\mathrm{out}=-R_\mathrm{C}i_\mathrm{c}=-R_\mathrm{C}S\,u_\mathrm{in}$, and with $S=I_\mathrm{C}/U_T$ follows $S\,R_\mathrm{C}=I_\mathrm{C}R_\mathrm{C}/U_T$. With an emitter resistor: $u_\mathrm{in}=u_\mathrm{be}+R_\mathrm{E}S\,u_\mathrm{be}$, the larger part of $u_\mathrm{in}$ lies across $R_\mathrm{E}$, and the rest, $u_\mathrm{be}=u_\mathrm{in}/(1+S\,R_\mathrm{E})$, does the controlling. Common collector: $u_\mathrm{out}=R_\mathrm{E}S\,u_\mathrm{be}$ with $u_\mathrm{be}=u_\mathrm{in}-u_\mathrm{out}$, solve. Common base: the base rests, so $u_\mathrm{be}=-u_\mathrm{in}$ and $u_\mathrm{out}=-R_\mathrm{C}S\,u_\mathrm{be}=+S\,R_\mathrm{C}u_\mathrm{in}$.
:::

**Example.** Common-emitter circuit at point A: $A=-6\,\mathrm{V}/26\,\mathrm{mV}=-231$, more accurately $-215$ with $r_\mathrm{CE}$. 1 mV at the input becomes 0.23 V at the output. The point in the middle allows a __voltage swing__, an output amplitude, of almost 6 V, but at 25 mV at the input the tangent has long ceased to be valid. For the small-signal limit of 2.6 mV it is 0.6 V. For an amplifier, the operating point must lie in the area of nearly constant slope, and the swing should be as large as possible. The version with negative feedback has $A=-3\,\text{k}\Omega/(1\,\text{k}\Omega+12.9\,\Omega)=-2.96$: only 1.3 % of $u_\mathrm{in}$ lies across the BE path, but in exchange the gain is determined almost entirely by two resistors. Emitter follower with $R_\mathrm{E}=3$ k$\Omega$ at 2 mA: $S\,R_\mathrm{E}=231$, $A=0.996$. Its strength is not the voltage but the current: the current gain is $1+B=201$. It serves as a __buffer__: it hardly loads the source and drives the load with low impedance. **Limiting cases:** $R_\mathrm{E}\to0$ in the form with negative feedback gives $-S\,R_\mathrm{C}$. $R_\mathrm{E}\to\infty$ for the emitter follower gives $A\to1$.

| Circuit | $A$ | Input resistance | Output resistance | Use |
|---|---|---|---|---|
| Common emitter | $-231$ | $r_\mathrm{BE}=2.6$ k$\Omega$ | $R_\mathrm{C}=3$ k$\Omega$ | Amplifying voltage |
| Common collector | $0.996$ | $r_\mathrm{BE}+(1+B)R_\mathrm{E}=606$ k$\Omega$ | $1/S=13\,\Omega$ | Buffer, current gain |
| Common base | $+231$ | $1/S=13\,\Omega$ | $R_\mathrm{C}=3$ k$\Omega$ | Amplifying a low-impedance source |

:::frage But a real common-emitter circuit has a flatter characteristic than the common-base circuit. Why should the magnitude be the same?
It is the same with direct drive, equal $R_\mathrm{C}$ and equal current. If there is a series resistor before the base, or a source with internal resistance, it forms a voltage divider with $r_\mathrm{BE}$, and only part of $u_\mathrm{in}$ reaches the BE path. Then the characteristic of the common-emitter circuit is flatter. In the common-base circuit this divider does not arise, because the low-impedance source sits at the emitter.
:::

:::ltspice The transfer characteristic of the common-emitter circuit
⁠**Draw:** `voltage` `VCC` with 12 at `res` 3k to the collector (net `c`), `npn` with model `T`, emitter at ground, at the base `voltage` `VE`.

⁠**Directives:** the model from Stage [3](eine-flache-viele-kennlinien.html#stufe-3), `.dc VE 0.5 0.7 0.1m`, `.meas dc a1 FIND V(c) AT=0.5995`, `.meas dc a2 FIND V(c) AT=0.6005`, `.meas dc au PARAM (a2-a1)/1m`.

⁠**What you see:** $U_\mathrm{out}$ falls from 12 V to nearly 0, within a window of around 60 mV. `au` gives $-213$, against $-215$ in the calculation. LTspice calculates with $U_T=25.86$ mV and is at 1.98 mA at $U_\mathrm{BE}=0.6$ V. For Exercise [12](#aufg-12), set `VCC` to 9, the resistor to 4.7k and the `AT` values to 0.582 and 0.583: `au` then gives $-169$ at 0.98 mA.
:::

:::aufgabe Exercise 12 ★★★ Amplifier and follower
<span class="anker" id="aufg-12"></span>

T operates at $I_\mathrm{C}=1$ mA and $U_\mathrm{CE}=4.3$ V with $U_\mathrm{CC}=9$ V, $R_\mathrm{C}=4.7$ k$\Omega$. (a) Predict how large $A$ of the common-emitter circuit is, using only the voltage across $R_\mathrm{C}$. (b) How large is the output amplitude at $\hat u_\mathrm{in}=2$ mV? How does $r_\mathrm{CE}$ change the result? (c) With an emitter resistor of 470 $\Omega$: How large is $A$? (d) As an emitter follower with $R_\mathrm{E}=4.7$ k$\Omega$: How large is $A$? Is the output inverted?

:::loesung
(a) $U_{R_\mathrm{C}}=4.7$ V, so $A=-4.7\,\mathrm{V}/26\,\mathrm{mV}=-181$.

(b) $\hat u_\mathrm{out}=0.36$ V. With $r_\mathrm{CE}=78$ k$\Omega$, $A=-S(R_\mathrm{C}\parallel r_\mathrm{CE})=-171$, only 6 % less.

(c) $A=-4.7\,\text{k}\Omega/(470\,\Omega+26\,\Omega)=-9.5$. The approximation $-R_\mathrm{C}/R_\mathrm{E}$ gives $-10$.

(d) $S\,R_\mathrm{E}=181$, $A=0.994$. The output is not inverted; the emitter follows the base in phase.
:::
:::
