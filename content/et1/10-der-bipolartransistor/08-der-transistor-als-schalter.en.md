---
title: Stage 6: The transistor as a switch
pfad: Electrical Engineering / 1st Semester / Fundamentals of Electrical Engineering / The Bipolar Transistor
order: 1200800
summary: A switch should be fully off or fully on.
tags: inverter, logic levels, power hyperbola
lang: en
---

<span class="anker" id="stufe-6"></span>

:::zweck
A switch should be fully off or fully on. This stage shows why it uses the ends of the load line for this, builds the inverter from it and names the limits of the component.
:::

**The idea.** The transistor converts the power $P=U_\mathrm{CE}I_\mathrm{C}+U_\mathrm{BE}I_\mathrm{B}$ into heat, in practice only the first term. In the cut-off region $I_\mathrm{C}=0$; in saturation $U_\mathrm{CE}$ is small. At both points the product stays low. It is largest in the middle of the load line. That is why a switch jumps between Z and S. This also gives the largest separation of the two output levels, and there is no mechanism: the transistor switches very quickly and without wear. An amplifier, by contrast, works in the active region. There the characteristic is approximately linear, and the higher power dissipation matters less than an undistorted signal.

The smallest logic circuit is the __inverter__: the same circuit as in Fig. [6](der-arbeitspunkt.html#abb-6), with $U_\mathrm{out}=U_\mathrm{CE}$ as the output. A high input voltage gives a low output voltage and vice versa. As __logic levels__, a low voltage counts as 0 and a high one as 1.

:::satz Theorem 6.1 (Characteristic of the inverter)
<span class="anker" id="satz-6-1"></span>

With the linear model,

<span class="anker" id="gl-6-1"></span>
$$U_\mathrm{out}= \begin{cases} U_\mathrm{CC} & U_\mathrm{in}<U_\mathrm{BE},\\[2pt] U_\mathrm{CC}-B\,R_\mathrm{C}\dfrac{U_\mathrm{in}-U_\mathrm{BE}}{R_\mathrm{B}} & U_\mathrm{BE}\le U_\mathrm{in}\le U_\mathrm{in,sat},\\[6pt] U_\mathrm{CE,sat} & U_\mathrm{in}>U_\mathrm{in,sat}, \end{cases} \tag{6.1}$$

<span class="anker" id="gl-6-2"></span>
$$U_\mathrm{in,sat}=\frac{(U_\mathrm{CC}-U_\mathrm{CE,sat})\,R_\mathrm{B}}{B\,R_\mathrm{C}}+U_\mathrm{BE}. \tag{6.2}$$
:::

⁠**How to read it:** The middle branch is a straight line with slope $-B\,R_\mathrm{C}/R_\mathrm{B}$. $U_\mathrm{in,sat}$ is the input voltage at which the transistor reaches saturation. Below $U_\mathrm{BE}$ the input counts as 0, above $U_\mathrm{in,sat}$ as 1. In between, the signal is ambiguous. That is why $R_\mathrm{B}$ is chosen small enough to bring $U_\mathrm{in,sat}$ close to $U_\mathrm{BE}$. The derivation is [(5.2)](der-arbeitspunkt.html#gl-5-2) with [(5.1)](der-arbeitspunkt.html#gl-5-1), solved for $U_\mathrm{in}$ at $U_\mathrm{CE}=U_\mathrm{CE,sat}$. **Validity:** for slow signals. Very fast changes are limited by the charge in the base.

:::abbildung et1/k10schalter 7
Left, the inverter characteristic with $R_\mathrm{B}=20$ k$\Omega$, knees at 0.6 V and 0.99 V. Center, a square-wave signal between 0 and 5 V at the input (gray) and the inverted output between 12 V and 0.2 V (blue). Right, the permitted operating points: below the power hyperbola, $I_\mathrm{C,max}$ and $U_\mathrm{CE,max}$. The operating point A, with 12 mW, lies deep inside the permitted area.
:::

**Example.** With $R_\mathrm{B}=20$ k$\Omega$, the slope is $-30$ and $U_\mathrm{in,sat}=0.99$ V. A logic input of 5 V gives $I_\mathrm{B}=220$ µ A and $B\,I_\mathrm{B}=44$ mA, far above the 3.93 mA that $R_\mathrm{C}$ allows. So the transistor is overdriven by a factor of eleven and stays reliably switched on even with a poor specimen. In it, $0.2\,\mathrm{V}\cdot3.93\,\mathrm{mA}+0.6\,\mathrm{V}\cdot0.22\,\mathrm{mA}=0.92$ mW arise, while it switches a power of 46 mW in $R_\mathrm{C}$. At point A it would be 12 mW in the transistor. **Limiting case:** for $B\,R_\mathrm{C}/R_\mathrm{B}\to\infty$, the characteristic becomes a vertical jump at $U_\mathrm{BE}$.

**Operating limits.** Three values limit the permitted operating points (Fig. [7](#abb-7), right). Above $U_\mathrm{CE,max}$ the CB boundary breaks down. Above $I_\mathrm{C,max}$ the base and the lead wires are overloaded. Above the __power hyperbola__ $I_\mathrm{C}=P_\mathrm{max}/U_\mathrm{CE}$ the component becomes too hot. Outside these limits the service life drops rapidly, or the component fails at once. For T, the hyperbola lies at 10 mA at 40 V and at 100 mA at 4 V.

:::aufgabe Exercise 7 ★★ Inverter
<span class="anker" id="aufg-7"></span>

An inverter with T runs at $U_\mathrm{CC}=5$ V with $R_\mathrm{C}=1$ k$\Omega$ and $R_\mathrm{B}=10$ k$\Omega$. (a) Determine the slope and $U_\mathrm{in,sat}$. (b) The input is at 3.3 V. Determine $I_\mathrm{B}$, $I_\mathrm{C}$ and the power in the transistor. Compare it with the maximum on the load line. (c) Is an input of 3.3 V also enough for $B=50$?

:::loesung
(a) Slope $-200\cdot1\,\text{k}\Omega/10\,\text{k}\Omega=-20$. $U_\mathrm{in,sat}=4.8\,\mathrm{V}/20+0.6\,\mathrm{V}=0.84$ V.

(b) $I_\mathrm{B}=2.7\,\mathrm{V}/10\,\text{k}\Omega=270$ µ A, $B\,I_\mathrm{B}=54$ mA, far above $I_\mathrm{C}=4.8\,\mathrm{V}/1\,\text{k}\Omega=4.8$ mA, so saturation. $P=0.2\,\mathrm{V}\cdot4.8\,\mathrm{mA}+0.6\,\mathrm{V}\cdot0.27\,\mathrm{mA}=1.12$ mW. On the load line, $U_\mathrm{CE}I_\mathrm{C}=U_\mathrm{CE}(U_\mathrm{CC}-U_\mathrm{CE})/R_\mathrm{C}$. The maximum lies at $U_\mathrm{CC}/2$ with $U_\mathrm{CC}^2/(4R_\mathrm{C})=6.25$ mW.

(c) $U_\mathrm{in,sat}=4.8\,\mathrm{V}/5+0.6\,\mathrm{V}=1.56$ V $<3.3$ V: yes.
:::
:::
