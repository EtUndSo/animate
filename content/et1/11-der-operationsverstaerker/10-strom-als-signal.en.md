---
title: Stage 8: Current as the signal
pfad: Electrical Engineering / 1st Semester / Fundamentals of Electrical Engineering / The Operational Amplifier
order: 1211000
summary: So far the voltage was the signal.
tags: transimpedance amplifier, differential resistance, negative impedance converter
lang: en
---

<span class="anker" id="stufe-8"></span>

:::zweck
So far the voltage was the signal. But many sources supply a current. This stage converts current into voltage and shows that the op amp can emulate a negative resistance.
:::

**Current into voltage.** A photodiode supplies a current that hardly depends on its voltage. In the __transimpedance amplifier__ it flows directly into the virtual ground and has to pass through $R$ (Fig. [10](#abb-10) left):

<span class="anker" id="gl-8-1"></span>
$$U_\mathrm{A}=-R\,I_\mathrm{E},\qquad r_\mathrm{in}=\frac{\Delta U_-}{\Delta I_\mathrm{E}}=\frac{R}{1+A}. \tag{8.1}$$

With $R=1$ M$\Omega$, 2 µ A becomes $-2$ V. The node moves by only $2\,\mathrm{V}/A=20$ µ V. This is the small input resistance of 10 $\Omega$, a value for changes (__differential resistance__). The source sees almost a short circuit, and its internal resistance plays no role.

**A negative resistance.** At positive voltage a resistor draws current in the direction of the reference arrow (passive sign convention, [Part 2](/wissen/en/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/strom-widerstand-und-kirchhoff/strom-widerstand-und-kirchhoff.html)). The __negative impedance converter__ (NIC) instead pushes current out (Fig. [10](#abb-10) right). Terminal 1 is at the plus input, and from there an $R$ leads to the output. From the output an equal $R$ leads to the minus input, and from there $R_2$ to ground. From $\varphi_+=\varphi_-$ it follows that $U_1=U_2$.

:::satz Theorem 8.1 (NIC)
<span class="anker" id="satz-8-1"></span>

<span class="anker" id="gl-8-2"></span>
$$R_\mathrm{in}=\frac{U_1}{I_1}=-R_2. \tag{8.2}$$

The rule holds only as long as the resistance $R_\mathrm{i}$ that acts at terminal 1 with respect to ground is smaller than $R_2$.
:::

⁠**How to read it:** $I_1$ counts into terminal 1, $U_1$ with respect to ground. $U_2$ and $I_2$ belong to $R_2$. $R_\mathrm{i}$ is everything hanging on terminal 1 from outside, for example source and load in parallel. **Validity:** $U_\mathrm{A}=U_1(1+R/R_2)$ must lie within the limits.

:::herleitung Why the sign flips and when the rule holds
Through $R_2$ flows $I_2=U_2/R_2$, and no current goes into the input, so it also flows through the lower $R$: the output is at $U_\mathrm{A}=U_2+R\,I_2$. The upper $R$ has the same voltage and carries the same current, from the output to terminal 1. So $I_1=-I_2$ and $R_\mathrm{in}=U_1/I_1=-R_2$.

There are two feedback paths here: the lower $R$ gives negative feedback, the left one positive feedback. If $U_\mathrm{A}$ changes, $\varphi_-$ changes by the fraction $\beta_-=R_2/(R_2+R)$ and $\varphi_+$ by $\beta_+=R_\mathrm{i}/(R_\mathrm{i}+R)$. Negative feedback prevails only for $\beta_->\beta_+$, that is, for $R_\mathrm{i}<R_2$.
:::

:::abbildung et1/k11nic 10
Left, the transimpedance amplifier with a current source as input. Right, the NIC with $R=10$ k$\Omega$ and $R_2=5$ k$\Omega$ at 1 V on terminal 1: the output is at 3 V and pushes 0.2 mA out of the terminal.
:::

**Example.** With $R=10$ k$\Omega$, $R_2=5$ k$\Omega$ and $U_1=1$ V, $I_2=0.2$ mA, $U_\mathrm{A}=3$ V, $I_1=-0.2$ mA, so $R_\mathrm{in}=-5$ k$\Omega$. The energy comes from the supply of the op amp. *Application:* A current source with 1 mA and internal resistance $R_\mathrm{q}=10$ k$\Omega$ delivers only 0.909 mA to 1 k$\Omega$, because part of it goes through $R_\mathrm{q}$. In parallel with it, a NIC with $R_2=R_\mathrm{q}$: the conductance $1/R_\mathrm{q}-1/R_2$ vanishes, and the load gets 1 mA. The real source acts like an ideal one. The NIC supplies exactly the 0.1 mA that $R_\mathrm{q}$ branches off. **Limiting case:** Without a load, $R_\mathrm{i}=R_\mathrm{q}=R_2$, both feedback paths are equally strong, the loop gain is zero, and the rule no longer holds.

:::aufgabe Exercise 9 ★★★ Compensating a current source
<span class="anker" id="aufg-9"></span>

A NIC with $R=10$ k$\Omega$ and $R_2=4.7$ k$\Omega$ is in parallel with a source with 2 mA and $R_\mathrm{q}=4.7$ k$\Omega$. The load is 1 k$\Omega$. (a) What current does the load get without the NIC, and what with it? (b) Where is the op amp output? (c) Up to what load resistance does the output's 11 V suffice? (d) Why is the circuit stable with a load but not without one?

:::loesung
(a) Without the NIC $2\,\mathrm{mA}\cdot4.7/5.7=1.65$ mA, with the NIC 2 mA. (b) $U_1=2$ V, $I_2=0.426$ mA, $U_\mathrm{A}=2\,\mathrm{V}+10\,\mathrm{k\Omega}\cdot0.426\,\mathrm{mA}=6.26$ V. (c) $U_\mathrm{A}=U_1(1+R/R_2)=3.13\,U_1\le11$ V gives $U_1\le3.52$ V, so $R_\mathrm{L}\le1.76$ k$\Omega$. (d) With a load, $R_\mathrm{i}=R_\mathrm{q}\parallel1\,\mathrm{k\Omega}=825\,\Omega<R_2$, and negative feedback prevails. Without a load, $R_\mathrm{i}=R_2$, and the two feedback paths cancel each other.
:::
:::
