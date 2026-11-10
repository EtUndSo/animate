---
title: Stage 10: Discharging and time constant
pfad: Electrical Engineering / 1st Semester / ET1 – Fundamentals of Electrical Engineering 1: Introduction to Circuit Analysis / The Capacitor
adresse: elektrotechnik/1-semester/grundlagen-der-elektrotechnik/der-kondensator
knoten: Chapter 3: The Capacitor
order: 1131100
summary: The charged capacitor gives its charge back through a resistor.
tags: 
lang: en
---

<span class="anker" id="stufe-10"></span>

:::zweck
The charged capacitor gives its charge back through a resistor. It is the same equation with a different starting value. From this follows a rule for every switching process in the RC circuit.
:::

**The idea.** The switch moves from position 1 to 2, and the battery is disconnected. The capacitor holds its 9 V, because they cannot jump. This voltage is now across $R$. The electrons of the negative plate run back through $R$ to the positive one. So the current runs against the reference arrow of Fig. [9](aufladen-uber-einen-widerstand.html#abb-9), and it jumps: a moment ago it was zero, now it is $-0.9$ mA. With every charge that flows off, the voltage falls and with it the current. At first the capacitor acts like a source that keeps getting weaker.

:::satz Theorem 10.1 (Discharging)
<span class="anker" id="satz-10-1"></span>

Without a battery, Kirchhoff's voltage law reads $u_R+u_C=0$, that is, $RC\,\mathrm{d} u_C/\mathrm{d} t+u_C=0$. With $u_C(0)=U_0$ and $t\ge0$,

<span class="anker" id="gl-10-1"></span>
$$u_C(t)=U_0\,\mathrm{e}^{-t/\tau},\qquad i(t)=-\frac{U_0}{R}\,\mathrm{e}^{-t/\tau},\qquad u_R(t)=-U_0\,\mathrm{e}^{-t/\tau}. \tag{10.1}$$
:::

In general, for every switching process in the RC circuit with a constant source, the voltage runs from the starting value $u_C(0)$ to the final value $u_\infty$ according to

<span class="anker" id="gl-10-2"></span>
$$u_C(t)=u_\infty+\bigl(u_C(0)-u_\infty\bigr)\,\mathrm{e}^{-t/\tau}. \tag{10.2}$$

⁠**How to read it:** The minus sign on $i$ says: the current runs against the reference arrow. $u_\infty$ is the voltage the capacitor reaches after a long time, $U_0$ when charging, 0 when discharging. The difference from the final value shrinks in every time $\tau$ to 36.8 %. **Validity:** $\tau$ is formed with the resistance of the respective current path. Here both positions have the same $R$.

:::herleitung General rule
For the distance $x=u_\infty-u_C$, as in Stage [9](aufladen-uber-einen-widerstand.html#stufe-9), $\mathrm{d} x/\mathrm{d} t=-x/\tau$. Steps 2 to 4 hold for either sign of $x$ if you write $\ln|x|$, and give $x(t)=x(0)\,\mathrm{e}^{-t/\tau}$. Substituting $x(0)=u_\infty-u_C(0)$ gives [(10.2)](#gl-10-2). For $u_\infty=0$ this yields [(10.1)](#gl-10-1); for $u_\infty=U_0$ and $u_C(0)=0$ it yields [(9.3)](aufladen-uber-einen-widerstand.html#gl-9-3).
:::

**The time constant.** $\tau=RC$ is the time after which the current and the remaining voltage have fallen to $1/\mathrm{e}$. In charging, 63.2 % has then been reached. Charging and discharging get faster with smaller $C$, because less charge has to be moved, and with smaller $R$, because more current flows. $U_0$ does not appear in $\tau$: twice the voltage gives twice the current, but also twice the charge. The table holds for every RC circuit, the last row for the reference model.

| Time | $1\tau$ | $2\tau$ | $3\tau$ | $4\tau$ | $5\tau$ |
|---|---|---|---|---|---|
| Charging: $1-\mathrm{e}^{-t/\tau}$ in % | 63.2 | 86.5 | 95.0 | 98.2 | 99.3 |
| Discharging: $\mathrm{e}^{-t/\tau}$ in % | 36.8 | 13.5 | 5.0 | 1.8 | 0.7 |
| Charging: $u_C$ in V | 5.69 | 7.78 | 8.55 | 8.84 | 8.94 |

:::abbildung et1/k3entladen 12
Five seconds of charging, five seconds of discharging. The voltage is continuous; the percentages refer to the final value in charging and to the starting value in discharging. The current jumps at switching and changes sign in discharging; the jumps are dashed.
:::

::::beispiel
In the reference model, discharging starts at 9 V. At the first moment $u_R=-9$ V and $i=-0.9$ mA. After 1 s, $u_C=3.31$ V and $i=-0.331$ mA; after 3 s only 0.448 V remains. If you charge for only 5 s as in Fig. [12](#abb-12), discharging starts at 8.94 V.
::::

⁠**Check:** The charge that flows through $R$ during discharging is $\int_0^\infty|i|\,\mathrm{d} t=\frac{U_0}{R}\,\tau=C\,U_0$, exactly the stored charge. **Limiting case:** For $u_C(0)=u_\infty$ the bracket in [(10.2)](#gl-10-2) is zero: nothing happens, the capacitor is already in its final state.

:::frage Why may the current jump at switching, but the voltage may not?
The voltage is tied to the stored charge, and that can change only with finite current in finite time. The current has no such store. At every moment it follows from the voltage across $R$, and that changes when the switch is thrown.
:::

:::ltspice Charging and discharging in the RC circuit
⁠**Draw:** `voltage` from `in` to ground with `PULSE(0 9 0 1u 1u 5 10)`, `res` with `10k` from `in` to `out`, `cap` with `100u` from `out` to ground. The source replaces the switch: 9 V for 5 s, then 0 V, that is, a path back through $R$.

⁠**Directives:** `.tran 0 10 0 1m`, plus measurements such as `.meas tran u1 FIND V(out) AT=1` for $t=1$, 2, 3, 5 and 6 s as well as `.meas tran i0 FIND I(R1) AT=10u`.

⁠**What you see:** 5.69 V; 7.78 V; 8.55 V; 8.94 V during charging, as in the table, then 3.29 V at 6 s, that is, 36.8 % of 8.94 V. At the start `i0` $=0.90$ mA. Then set 12 V, `4.7k` and `220u` and check your results from Exercise [10](aufladen-uber-einen-widerstand.html#aufg-10).
:::

:::aufgabe Exercise 12 ★★ Starting values and self-discharge
<span class="anker" id="aufg-12"></span>

Let $R=10\,\mathrm{k\Omega}$, $C=100\,\mu\text{F}$ and $\tau=1$ s.

<ol class="al">

<li>

The capacitor already carries 3 V when $U_0=9$ V is connected. Give $u_C(t)$ and calculate $u_C(1\,\mathrm{s})$.

</li>

<li>

How long does it take here for $u_C$ to rise from 3 V to 6 V?

</li>

<li>

Discharging from 9 V: When does $u_C$ fall below 1 V?

</li>

<li>

The charged capacitor (9 V) is disconnected, and only $R_\mathrm{I}=1\,\mathrm{M\Omega}$ discharges it. How large is $u_C$ after one minute?

</li>

</ol>

:::loesung
(a) With [(10.2)](#gl-10-2), $u_\infty=9$ V and $u_C(0)=3$ V: $u_C(t)=9\,\mathrm{V}-6\,\mathrm{V}\cdot\mathrm{e}^{-t/\tau}$. For $t=1$ s: 6.79 V.

(b) $6=9-6\,\mathrm{e}^{-t/\tau}$ gives $\mathrm{e}^{-t/\tau}=\frac12$, so $t=\tau\ln2=0.693$ s.

(c) $9\,\mathrm{e}^{-t/\tau}=1$ gives $t=\tau\ln9=2.20$ s.

(d) The time constant is $R_\mathrm{I}\,C=100$ s, so $u_C(60\,\mathrm{s})=9\,\mathrm{V}\cdot\mathrm{e}^{-0.6}=4.94$ V.
:::
:::
