---
title: Stage 5: The operating point
pfad: Electrical Engineering / 1st Semester / Fundamentals of Electrical Engineering / The Bipolar Transistor
order: 1200700
summary: Which region applies is not known in advance.
tags: load line, supply voltage
lang: en
---

<span class="anker" id="stufe-5"></span>

:::zweck
Which region applies is not known in advance. This stage determines the operating point by assuming and checking, and draws it as an intersection.
:::

**The idea.** The transistor supplies its characteristic curves, the circuit supplies mesh equations. Both must hold at once. The result is the operating point (OP), as in [Part 5](/wissen/en/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/quellen-und-ersatzquellen/quellen-und-ersatzquellen.html) the intersection of a characteristic curve with a straight line. Because each region has a different equivalent circuit, one assumes a region, calculates linearly and checks. A contradiction with the conditions [(4.1)](drei-bereiche-drei-ersatzschaltbilder.html#gl-4-1) to [(4.3)](drei-bereiche-drei-ersatzschaltbilder.html#gl-4-3) reveals the wrong assumption.

:::abbildung et1/k10arbeit 6
Left, the circuit of the reference model. Right, the linearized output characteristics with the load line from $(0;\,4\,\mathrm{mA})$ to $(12\,\mathrm{V};\,0)$. It meets the line $I_\mathrm{B}=10$ µ A at the operating point A. S is the point in saturation, Z the point in the cut-off region.
:::

:::satz Theorem 5.1 (Operating point of the circuit with base and collector resistor)
<span class="anker" id="satz-5-1"></span>

The input mesh is $U_\mathrm{in}=R_\mathrm{B}I_\mathrm{B}+U_\mathrm{BE}$, the output mesh is the __load line__ $U_\mathrm{CE}=U_\mathrm{CC}-R_\mathrm{C}I_\mathrm{C}$. For $U_\mathrm{in}\le U_\mathrm{BE,on}$ the transistor blocks and $U_\mathrm{BE}=U_\mathrm{in}$. For $U_\mathrm{in}>U_\mathrm{BE,on}$, in both conducting regions

<span class="anker" id="gl-5-1"></span>
$$I_\mathrm{B}=\frac{U_\mathrm{in}-U_\mathrm{BE,on}}{R_\mathrm{B}}. \tag{5.1}$$

Assuming active operation gives

<span class="anker" id="gl-5-2"></span>
$$I_\mathrm{C}=B\,I_\mathrm{B},\qquad U_\mathrm{CE}=U_\mathrm{CC}-B\,I_\mathrm{B}R_\mathrm{C}. \tag{5.2}$$

If the result is $U_\mathrm{CE}\ge U_\mathrm{CE,sat}$, the assumption is correct. Otherwise saturation applies, with

<span class="anker" id="gl-5-3"></span>
$$U_\mathrm{CE}=U_\mathrm{CE,sat},\qquad I_\mathrm{C}=\frac{U_\mathrm{CC}-U_\mathrm{CE,sat}}{R_\mathrm{C}}<B\,I_\mathrm{B}. \tag{5.3}$$
:::

⁠**How to read it:** $U_\mathrm{CC}$ is the __supply voltage__, $U_\mathrm{in}$ the input voltage against ground. $R_\mathrm{B}$ sets the base current, $R_\mathrm{C}$ converts the collector current into a voltage. **Validity:** emitter at ground, the linear model from Stage [4](drei-bereiche-drei-ersatzschaltbilder.html#stufe-4). Equation [(5.1)](#gl-5-1) holds in both conducting regions because the same 0.6 V source lies between B and E there.

::::beispiel
Reference model: $I_\mathrm{B}=(5\,\mathrm{V}-0.6\,\mathrm{V})/440\,\text{k}\Omega=10$ µ A, $I_\mathrm{C}=2$ mA, $U_\mathrm{CE}=12\,\mathrm{V}-6\,\mathrm{V}=6$ V. That is more than 0.2 V, so active (point A). A wrong first assumption does no harm: saturation would give $I_\mathrm{C}=3.93$ mA, but $B\,I_\mathrm{B}=2$ mA is smaller, in contradiction to [(4.3)](drei-bereiche-drei-ersatzschaltbilder.html#gl-4-3). For $U_\mathrm{in}=12$ V, $I_\mathrm{B}=25.9$ µ A. Assuming active operation would yield $U_\mathrm{CE}=-3.5$ V, a contradiction. In saturation, $I_\mathrm{C}=3.93$ mA and $B\,I_\mathrm{B}=5.18$ mA (point S).
::::

⁠**Limiting cases:** $R_\mathrm{C}=0$ gives $U_\mathrm{CE}=U_\mathrm{CC}$, and the output is rigid. $U_\mathrm{in}<0.6$ V gives $I_\mathrm{C}=0$ and $U_\mathrm{CE}=12$ V (point Z).

**The middle of the active region.** In the active region, $U_\mathrm{CE}$ lies between 0.2 V and $U_\mathrm{CC}$. So that a signal has equal room on both sides, the point is placed in the middle. With $\Delta U=U_\mathrm{CC}-U_\mathrm{CE,sat}=11.8$ V,

<span class="anker" id="gl-5-4"></span>
$$U_\mathrm{CE,OP}=U_\mathrm{CE,sat}+\frac{\Delta U}{2}=6.1\,\mathrm{V},\qquad I_\mathrm{C}=\frac{U_\mathrm{CC}-U_\mathrm{CE,OP}}{R_\mathrm{C}}=1.97\,\mathrm{mA}. \tag{5.4}$$

From this follows $R_\mathrm{B}=(U_\mathrm{in}-U_\mathrm{BE})\,B/I_\mathrm{C}=447$ k$\Omega$. The 440 k$\Omega$ of the reference model lie almost there.

**With an emitter resistor.** If the base lies directly at $U_\mathrm{in}$ and the emitter goes to ground via $R_\mathrm{E}$, the input mesh reads $U_\mathrm{in}=U_\mathrm{BE,on}+R_\mathrm{E}I_\mathrm{E}$. For $U_\mathrm{in}>0.6$ V the transistor does not block, and

<span class="anker" id="gl-5-5"></span>
$$I_\mathrm{E}=\frac{U_\mathrm{in}-U_\mathrm{BE,on}}{R_\mathrm{E}},\quad I_\mathrm{B}=\frac{I_\mathrm{E}}{1+B},\quad I_\mathrm{C}=B\,I_\mathrm{B},\quad U_\mathrm{CE}=U_\mathrm{CC}-R_\mathrm{C}I_\mathrm{C}-R_\mathrm{E}I_\mathrm{E}. \tag{5.5}$$

With $U_\mathrm{in}=2.6$ V and $R_\mathrm{E}=1$ k$\Omega$, $I_\mathrm{E}=2$ mA, $I_\mathrm{C}=1.99$ mA and $U_\mathrm{CE}=4.03$ V. Here $B$ came into play only in the last step and changes almost nothing. Stage [7](gegenkopplung-halt-den-arbeitspunkt-fest.html#stufe-7) makes use of this.

:::aufgabe Exercise 5 ★★ Calculating the operating point
<span class="anker" id="aufg-5"></span>

Given are T, $U_\mathrm{CC}=10$ V, $R_\mathrm{C}=2$ k$\Omega$, $R_\mathrm{B}=220$ k$\Omega$. (a) Determine the operating point for $U_\mathrm{in}=3$ V. (b) Determine it for $U_\mathrm{in}=8$ V. (c) Which $R_\mathrm{B}$ places the point in the middle of the active region at $U_\mathrm{in}=3$ V?

:::loesung
(a) $I_\mathrm{B}=2.4\,\mathrm{V}/220\,\text{k}\Omega=10.9$ µ A, $I_\mathrm{C}=2.18$ mA, $U_\mathrm{CE}=10\,\mathrm{V}-4.36\,\mathrm{V}=5.64$ V: active.

(b) $I_\mathrm{B}=33.6$ µ A, $B\,I_\mathrm{B}=6.73$ mA. Assuming active operation would give $U_\mathrm{CE}=-3.45$ V, a contradiction. So saturation: $U_\mathrm{CE}=0.2$ V, $I_\mathrm{C}=9.8\,\mathrm{V}/2\,\text{k}\Omega=4.9$ mA $<6.73$ mA.

(c) $U_\mathrm{CE,OP}=0.2\,\mathrm{V}+4.9\,\mathrm{V}=5.1$ V, $I_\mathrm{C}=4.9\,\mathrm{V}/2\,\text{k}\Omega=2.45$ mA, $I_\mathrm{B}=12.25$ µ A, $R_\mathrm{B}=2.4\,\mathrm{V}/12.25\,\mu\text{A}=196$ k$\Omega$.
:::
:::

:::aufgabe Exercise 6 ★★ Emitter resistor
<span class="anker" id="aufg-6"></span>

The base of T lies directly at $U_\mathrm{in}=1.6$ V, with $U_\mathrm{CC}=12$ V, $R_\mathrm{C}=2$ k$\Omega$, $R_\mathrm{E}=500\,\Omega$. (a) Determine $I_\mathrm{E}$, $I_\mathrm{B}$, $I_\mathrm{C}$ and $U_\mathrm{CE}$. (b) What changes if $B$ falls to 100?

:::loesung
(a) $I_\mathrm{E}=1\,\mathrm{V}/500\,\Omega=2$ mA, $I_\mathrm{B}=2\,\mathrm{mA}/201=9.95$ µ A, $I_\mathrm{C}=1.99$ mA, $U_\mathrm{CE}=12\,\mathrm{V}-3.98\,\mathrm{V}-1\,\mathrm{V}=7.02$ V.

(b) $I_\mathrm{E}$ stays at 2 mA, because it depends only on $U_\mathrm{in}$ and $R_\mathrm{E}$. $I_\mathrm{B}$ becomes 19.8 µ A, $I_\mathrm{C}$ becomes 1.98 mA, $U_\mathrm{CE}$ becomes 7.04 V. Half of $B$, but only 0.5 % less collector current.
:::
:::
