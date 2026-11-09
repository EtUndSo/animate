---
title: Stage 1: Energy per charge times charge per time
pfad: Electrical Engineering / 1st Semester / Fundamentals of Electrical Engineering / Power, Matching and Efficiency
order: 1170200
summary: Voltage says how much energy a charge gives off, current says how much charge passes.
tags: 
lang: en
---

<span class="anker" id="stufe-1"></span>

:::zweck
Voltage says how much energy a charge gives off, current says how much charge passes. This stage combines the two into energy per time.
:::

**The idea.** Between the terminals of a component there is a voltage $U$. According to [Part 1](/wissen/en/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/ladung-feld-und-potenzial/ladung-feld-und-potenzial.html), every coulomb that gets from the higher to the lower potential gives off the energy $U$ in joules. The current $I$ counts how many coulombs pass through per second. So $U\cdot I$ joules are converted per second (Fig. [1](#abb-1)). Both factors are needed: voltage without current converts nothing, because no charge is moving. Current without voltage converts nothing, because no charge gives anything off.

:::abbildung et1/k7ladung 1
Load with 8 V and 0.5 A. Below, the potential curve: each coulomb loses 8 J. Positive charges are drawn moving in the direction of the current. Electrons move the opposite way; the result is the same.
:::

:::definition Definition 1.1 (Energy and power)
<span class="anker" id="satz-1-1"></span>

If the charge $\mathrm{d} Q$ passes through the voltage $u$, it gives off the energy $\mathrm{d} W=u\,\mathrm{d} Q$. With the current $i=\mathrm{d} Q/\mathrm{d} t$, it follows that

<span class="anker" id="gl-1-1"></span>
$$p(t)=\frac{\mathrm{d} W}{\mathrm{d} t}=u(t)\,i(t),\qquad W=\int u\,\mathrm{d} Q=\int_{t_1}^{t_2}u(t)\,i(t)\,\mathrm{d} t. \tag{1.1}$$

For DC quantities, that is, when $U$ and $I$ do not depend on time,

<span class="anker" id="gl-1-2"></span>
$$W=U\,I\,\Delta t,\qquad P=\frac{W}{\Delta t}=U\,I. \tag{1.2}$$
:::

⁠**How to read it:** $u$ in V, $i$ in A, $p$ in watts: $[P]=\mathrm{V\,A}=\mathrm{J/s}=\mathrm W$. An indicator LED converts 20 mW, an electric kettle 2 kW, a power plant unit 1 GW. The expression $W/\Delta t$ is in general the mean value of the power over the time $\Delta t$, and $p(t)$ is its instantaneous value. Devices often run continuously, which is why they are characterized by their power and not by their energy. For energy, $1\,\mathrm{W\,s}=1\,\mathrm{V\,A\,s}=1\,\mathrm{J}=1\,\mathrm{N\,m}$. Electrical engineering mostly calculates in watt-seconds or kilowatt-hours, $1\,\mathrm{kWh}=3.6\,\mathrm{MJ}$. Joules are common for combustion processes, newton-meters for mechanical work.

⁠**Signs:** In the passive sign convention (PSC, [Part 2](/wissen/en/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/strom-widerstand-und-kirchhoff/strom-widerstand-und-kirchhoff.html)), $p>0$ means that the component absorbs energy, and $p<0$ that it gives off energy. In the active sign convention (ASC), it is the other way around. **Validity:** $p=u\,i$ holds for every one-port if $u$ and $i$ are counted at the same pair of terminals. Nothing is assumed about the interior of the component.

:::herleitung Why only voltage and current count
In the time $\mathrm{d} t$, the charge $\mathrm{d} Q=i\,\mathrm{d} t$ enters at terminal 1 and the same charge leaves at terminal 2 (node rule, [Part 2](/wissen/en/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/strom-widerstand-und-kirchhoff/strom-widerstand-und-kirchhoff.html)). The interior remains unchanged. For the balance, it is as if $\mathrm{d} Q$ had gone directly from $\varphi_1$ to $\varphi_2$. According to [Part 1](/wissen/en/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/ladung-feld-und-potenzial/ladung-feld-und-potenzial.html), the energy given off is $\mathrm{d} W=(\varphi_1-\varphi_2)\,\mathrm{d} Q=u\,i\,\mathrm{d} t$. Dividing by $\mathrm{d} t$ gives [(1.1)](#gl-1-1). Electrons move the opposite way and carry negative charge. The two signs together give the same product.
:::

::::beispiel
At $R_\mathrm{L}=16\,\Omega$ there are 8 V, and 0.5 A flow ([Part 5](/wissen/en/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/quellen-und-ersatzquellen/quellen-und-ersatzquellen.html)). Each coulomb gives off 8 J, and 0.5 C arrive per second: $P=4$ W. In one hour that is $W=4\,\mathrm{W}\cdot3600\,\mathrm{s}=14.4\,\mathrm{kJ}=4\,\mathrm{Wh}$. Counted individually, $I/e=3.12\cdot10^{18}$ electrons pass through per second, and each gives off $e\cdot8\,\mathrm{V}=1.28\cdot10^{-18}$ J. The product is again 4 W.
::::

⁠**Limiting cases:** At open terminals there are 9 V and 0 A, so $P=0$. An ideal wire has $U=0$, so $P=0$ at any current.

:::frage Is current used up in the component?
No. The same current flows before and after the component; the charge comes back out completely. What is used up is energy: the charge continues at a lower potential. That is why the bill for “electricity consumption” shows kilowatt-hours.
:::

:::aufgabe Exercise 1 ★ Energy and sign
<span class="anker" id="aufg-1"></span>

(a) A rechargeable battery with 3.7 V stores the charge 2 Ah (2 A for one hour). How much energy is that in Wh and in kJ? How long does it supply a device with 0.74 W? (b) An electric kettle with 2 kW runs for 3 minutes. How many kWh is that, and what do they cost at 30 ct/kWh? (c) At a one-port, $U=12$ V and $I=-3$ A are measured in the passive sign convention. Does it absorb power or deliver it?

:::loesung
(a) $Q=2\,\mathrm{A}\cdot3600\,\mathrm{s}=7200$ C, so $W=3.7\,\mathrm{V}\cdot7200\,\mathrm{C}=26.64$ kJ $=7.4$ Wh. At 0.74 W, that lasts 10 h. (b) $W=2\,\mathrm{kW}\cdot0.05\,\mathrm{h}=0.1$ kWh, which costs 3 ct. (c) $P=12\,\mathrm{V}\cdot(-3\,\mathrm{A})=-36$ W. The one-port delivers 36 W.
:::
:::
