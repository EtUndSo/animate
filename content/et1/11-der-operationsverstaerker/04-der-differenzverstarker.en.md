---
title: Stage 2: The differential amplifier
pfad: Electrical Engineering / 1st Semester / Fundamentals of Electrical Engineering / The Operational Amplifier
order: 1210400
summary: A disturbance on both lines should vanish, and the difference between them should be amplified.
tags: common-mode voltage, non-inverting input, inverting input
lang: en
---

<span class="anker" id="stufe-2"></span>

:::zweck
A disturbance on both lines should vanish, and the difference between them should be amplified. This takes a circuit whose output depends only on the difference of two voltages.
:::

**The idea.** Two identical transistors T1 and T2 hang with their emitters on the common node E (Fig. [2](#abb-2)). Below them sits T3. Its base is at the fixed voltage $U_\mathrm{bias}$, so it acts as a current source ([Part 10](/wissen/en/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/der-bipolartransistor/der-bipolartransistor.html)) and draws the fixed current $I_0$ out of the node. The base currents are small, so $I_\mathrm{C1}+I_\mathrm{C2}=I_0$ holds. The sum is fixed; only the division can change.

If both bases rise by the same amount, E rises with them, because T3 holds the current fixed and with it $U_\mathrm{BE}$. Nothing changes. This common part is called the __common-mode voltage__, $U_\mathrm{cm}=(\varphi_++\varphi_-)/2$. If only the base of T2 rises, T2 draws more current. T1 gets less by exactly this amount. More voltage drops across the right collector resistor, less across the left one, and the voltage between the collectors swings.

:::abbildung et1/k11diff 2
Left, the differential amplifier with $I_0=2$ mA and $R_\mathrm{C}=3$ k$\Omega$. T3 holds the sum fixed. Right, the division: around $U_\mathrm{D}=0$, 1 mA flows in each branch; at 100 mV, 97.9 % flows through T2.
:::

:::satz Theorem 2.1 (Differential amplifier)
<span class="anker" id="satz-2-1"></span>

T1 has its base at the input $\varphi_-$, T2 at the input $\varphi_+$. With $U_\mathrm{D}=\varphi_+-\varphi_-$ and $U_\mathrm{A}=U_\mathrm{a1}-U_\mathrm{a2}$,

<span class="anker" id="gl-2-1"></span>
$$I_\mathrm{C2}=\frac{I_0}{1+\mathrm{e}^{-U_\mathrm{D}/U_T}},\qquad I_\mathrm{C1}=\frac{I_0}{1+\mathrm{e}^{U_\mathrm{D}/U_T}},\qquad U_\mathrm{A}=R_\mathrm{C}\,(I_\mathrm{C2}-I_\mathrm{C1}). \tag{2.1}$$

For $|U_\mathrm{D}|\ll U_T$ this is a straight line:

<span class="anker" id="gl-2-2"></span>
$$U_\mathrm{A}=A_\mathrm{D}\,U_\mathrm{D},\qquad A_\mathrm{D}=S\,R_\mathrm{C}=\frac{I_0\,R_\mathrm{C}}{2\,U_T}=\frac{U_{R_\mathrm{C}}}{U_T}. \tag{2.2}$$
:::

⁠**How to read it:** $S=I_\mathrm{C}/U_T$ is the transconductance of one transistor at $I_\mathrm{C}=I_0/2$. $U_{R_\mathrm{C}}=I_0R_\mathrm{C}/2$ is the quiescent voltage across one collector resistor. $\varphi_+$ is called the __non-inverting input__ because the output follows it in the same direction, $\varphi_-$ the __inverting input__. **Validity:** identical transistors, both in the active region, base currents small compared with $I_0$.

:::herleitung Division and gain
Both emitters are at the same potential, so $U_\mathrm{BE2}-U_\mathrm{BE1}=U_\mathrm{D}$. With $I_\mathrm{C}=I_\mathrm{S}\,\mathrm{e}^{U_\mathrm{BE}/U_T}$ it follows that $I_\mathrm{C2}/I_\mathrm{C1}=\mathrm{e}^{U_\mathrm{D}/U_T}$. Together with $I_\mathrm{C1}+I_\mathrm{C2}=I_0$ this gives [(2.1)](#gl-2-1). For small changes: the sum is fixed, so $\Delta I_\mathrm{C1}=-\Delta I_\mathrm{C2}$. Both are $S$ times the change in their own $U_\mathrm{BE}$, so the changes are equal and opposite. Their difference is $U_\mathrm{D}$, so each junction carries $\pm U_\mathrm{D}/2$. Thus $\Delta I_\mathrm{C2}=S\,U_\mathrm{D}/2$ and $U_\mathrm{A}=2R_\mathrm{C}\,\Delta I_\mathrm{C2}=S\,R_\mathrm{C}\,U_\mathrm{D}$.
:::

::::beispiel
At rest, 1 mA flows in each branch, and the collectors are at $12\,\mathrm{V}-3\,\mathrm{V}=9$ V. $S=38.5$ mS, so $A_\mathrm{D}=3\,\mathrm{V}/26\,\mathrm{mV}=115$. At $U_\mathrm{D}=1$ mV, $\pm19.2$ µ A moves between the branches, each collector moves by 57.7 mV, and together that makes $U_\mathrm{A}=115$ mV. A disturbance of 100 mV on both inputs changes nothing about this.
::::

⁠**Limiting cases:** $U_\mathrm{D}=0$ gives $I_0/2$ per branch. At $|U_\mathrm{D}|\gg U_T$ everything flows through one transistor, $U_\mathrm{A}\to\pm R_\mathrm{C}I_0=\pm6$ V. The linear range is only a few $U_T$ wide: at 26 mV the straight line gives 3.0 V, the exact curve 2.77 V.

**Input.** An input signal $U_\mathrm{D}$ lies across two BE junctions in series, so the input resistance is $2\,r_\mathrm{BE}=2B/S=10.4$ k$\Omega$. With a total current of 20 µ A instead of 2 mA it is 1.04 M$\Omega$, and each base draws only 50 nA. That is where $r_\mathrm{e}$ and $I_\mathrm{B}$ in the reference model come from.

**From the differential amplifier to the op amp.** $A_\mathrm{D}=U_{R_\mathrm{C}}/U_T$ stays at a few hundred, because $U_{R_\mathrm{C}}$ cannot exceed the supply. A current mirror ([Part 10](/wissen/en/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/der-bipolartransistor/der-bipolartransistor.html)) in place of the resistors brings both current changes to one side and acts there like the parallel connection of two $r_\mathrm{CE}$. This gives $S\,r_\mathrm{CE}/2=U_\mathrm{Early}/(2U_T)\approx1400$. Behind it follow a voltage amplifier stage and an emitter follower for the low output resistance. Together that makes $10^5$ to $10^6$. This value depends on $B$, $U_\mathrm{Early}$ and the temperature: large, but imprecise.

:::frage Why is there only half the difference across each transistor if I raise only one base?
Because node E goes along by half. T2 wants more current, but the sum is fixed, so E rises until T1 gives up exactly that much. The fixed sum demands equal and opposite changes of $U_\mathrm{BE}$. Putting the whole difference on one junction gives twice the true $A_\mathrm{D}$.
:::

:::ltspice The current division
⁠**Draw:** Two `npn` Q1, Q2 with model `T`. The collectors each through a `res` 3k to `voltage` 12, nets `a1`, `a2`. Both emitters on net `e`, from there `current` 2m to a `voltage` $-12$. Base of Q1 to ground, base of Q2 to `voltage` `VP`.

⁠**Directives:** `.model T NPN(IS=1.55e-13 BF=186 VAF=74)`, `.dc VP -0.2 0.2 0.1m`, `.meas dc u1 FIND V(a1)-V(a2) AT=-0.5m`, `.meas dc u2 FIND V(a1)-V(a2) AT=0.5m`, `.meas dc ad PARAM (u2-u1)/1m`.

⁠**What you see:** `Ic(Q1)` and `Ic(Q2)` cross at 0; at 100 mV, Q2 carries 97.8 % of the current. `ad` gives 111.4 against 115 in the calculation, because LTspice calculates with $U_T=25.85$ mV and includes $r_\mathrm{CE}$. Insert the values from Exercise [2](#aufg-2).
:::

:::aufgabe Exercise 2 ★★ Differential stage
<span class="anker" id="aufg-2"></span>

A differential stage made of transistors T operates with $I_0=1$ mA, $R_\mathrm{C}=5$ k$\Omega$ and $U_\mathrm{CC}=12$ V. (a) Determine $S$, $A_\mathrm{D}$ and the quiescent potential of the collectors. (b) How large is $U_\mathrm{A}$ at $U_\mathrm{D}=2$ mV? How much current moves? (c) Both inputs rise by 1 V. What happens to E, the currents and $U_\mathrm{A}$? (d) Predict: Does $A_\mathrm{D}$ change if $I_0$ is doubled and $R_\mathrm{C}$ halved?

:::loesung
(a) $S=0.5\,\mathrm{mA}/26\,\mathrm{mV}=19.2$ mS, $A_\mathrm{D}=96.2$, collectors at $12\,\mathrm{V}-2.5\,\mathrm{V}=9.5$ V. (b) $U_\mathrm{A}=192$ mV. $S\,U_\mathrm{D}/2=19.2$ µ A moves. (c) E rises by 1 V, $U_\mathrm{BE}$ and the currents stay the same, $U_\mathrm{A}=0$. (d) No: $A_\mathrm{D}=U_{R_\mathrm{C}}/U_T$, and $U_{R_\mathrm{C}}=2.5$ V stays the same.
:::
:::
