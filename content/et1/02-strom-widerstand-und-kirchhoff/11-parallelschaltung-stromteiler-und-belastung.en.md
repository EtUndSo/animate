---
title: Stage 10: Parallel connection, current divider and loading
pfad: Electrical Engineering / 1st Semester / Fundamentals of Electrical Engineering / Current, Resistance and Kirchhoff's Laws
order: 1121100
summary: The second basic pattern: resistors side by side.
tags: parallel connection, current divider, load resistor
lang: en
---

<span class="anker" id="stufe-10"></span>

:::zweck
The second basic pattern: resistors side by side. This answers what happens to a voltage divider from which current is drawn.
:::

**The idea.** All the resistors hang on the same two nodes, and so on the same voltage. Each additional resistor opens an additional path, and the node rule adds the currents. That is why the conductances add, just as the cross sections of wires side by side add.

:::satz Theorem 10.1 (Parallel connection and current divider)
<span class="anker" id="satz-10-1"></span>

For $N$ resistors in a __parallel connection__,

<span class="anker" id="gl-10-1"></span>
<span class="anker" id="gl-10-2"></span>
$$\begin{aligned} U&=U_1=\dots=U_N,\qquad I=I_1+\dots+I_N,\qquad I_i=G_i\,U=\frac{U}{R_i},\\ G_\mathrm{tot}&=\frac{1}{R_\mathrm{tot}}=\sum_{i=1}^{N}G_i=\sum_{i=1}^{N}\frac{1}{R_i},\qquad R_\mathrm{tot}=\Bigl(\sum_{i=1}^N\frac1{R_i}\Bigr)^{-1}. \end{aligned} \tag{10.1|10.2}$$

For two resistors one writes $R_1\parallel R_2$:

<span class="anker" id="gl-10-3"></span>
$$R_1\parallel R_2=\frac{R_1\,R_2}{R_1+R_2},\qquad I_1=I_\mathrm{tot}\,\frac{G_1}{G_1+G_2}=I_\mathrm{tot}\,\frac{R_2}{R_1+R_2},\quad I_2=I_\mathrm{tot}\,\frac{G_2}{G_1+G_2}. \tag{10.3}$$
:::

⁠**How to read it:** The currents divide in the ratio of the conductances, the __current divider__. In the expression for $I_1$, $R_2$ is in the numerator: the current favors the smaller resistor. **Validity:** Both resistors lie between the same two nodes, and the leads are ideal.

:::herleitung Total conductance and current divider
The node rule gives $I=\sum I_i$, so with the same $U$, $I=(G_1+\dots+G_N)\,U$. For two branches, $U=I_\mathrm{tot}/(G_1+G_2)$ and thus $I_1=G_1\,U$. With $G=1/R$,

$$I_1=I_\mathrm{tot}\,\frac{1/R_1}{1/R_1+1/R_2}=I_\mathrm{tot}\,\frac{R_2}{R_1+R_2}.$$
:::

::::beispiel
$R_1$ and $R_2$ of the chain in parallel at 9 V: $G_\mathrm{tot}=0.5+1=1.5$ mS, so $R_\mathrm{tot}=667\,\Omega$, less than the smaller value, and $I=13.5$ mA. The current divider gives $I_1=13.5\,\mathrm{mA}\cdot1/3=4.5$ mA, $I_2=9$ mA. Mixed networks are combined from the inside out: $6\,\mathrm{k\Omega}$ in parallel with $1\,\mathrm{k\Omega}+2\,\mathrm{k\Omega}$ gives $6\parallel3=2\,\mathrm{k\Omega}$.
::::

⁠**Limiting cases:** $R_2\to\infty$ gives $R_1$; the open branch does not count. $R_2\to0$ gives 0; the short circuit takes over the entire current. $R_1=R_2$ gives $R_1/2$.

**The loaded voltage divider.** The voltage of a divider is to supply another circuit stage; the __load resistor__ $R_\mathrm L$ lies in parallel with $R_2$ (Fig. [11](#abb-11)). The mechanism: at the middle node an additional path opens, the total resistance falls, the current through $R_1$ rises, more drops across $R_1$, and the middle potential falls. With $R_2'=R_2\parallel R_\mathrm L$ in [(9.3)](reihenschaltung-und-spannungsteiler.html#gl-9-3):

<span class="anker" id="gl-10-4"></span>
$$\frac{U_2}{U}=\frac{R_2\parallel R_\mathrm L}{R_1+R_2\parallel R_\mathrm L}=\frac{R_2\,R_\mathrm L}{R_1\,(R_2+R_\mathrm L)+R_2\,R_\mathrm L},\quad I_\mathrm L=\frac{U_2}{R_\mathrm L}=\frac{U\,R_2}{R_1\,(R_2+R_\mathrm L)+R_2\,R_\mathrm L}. \tag{10.4}$$

⁠**Limiting cases:** $R_\mathrm L\to\infty$ gives $I_\mathrm L\to0$ and the unloaded rule. $R_\mathrm L=R_2$ gives $U_2/U=R_2/(2R_1+R_2)=\frac12R_2/(R_1+\frac12R_2)$.

:::abbildung et1/k2belastung 11
Left: loaded voltage divider. Right: $U_2$ versus $R_\mathrm L$ for $R_1=2\,\mathrm{k\Omega}$, $R_2=1\,\mathrm{k\Omega}$, $U=9$ V, by [(10.4)](#gl-10-4). With $R_\mathrm L=1\,\mathrm{k\Omega}$, 1.8 V remain; with $10\,\mathrm{k\Omega}$, it is 2.81 V. Only far above $R_1\parallel R_2=667\,\Omega$ is the load imperceptible.
:::

::::beispiel
For the chain, the relative error $\delta=(U_{2,0}-U_2)/U_{2,0}$ against the unloaded 3 V is: $R_\mathrm L=1\,\mathrm{k\Omega}$ gives 40 %, $10\,\mathrm{k\Omega}$ gives 6.3 %, $100\,\mathrm{k\Omega}$ gives 0.66 %. The error is $\delta=R_\mathrm i/(R_\mathrm i+R_\mathrm L)$ with $R_\mathrm i=R_1\parallel R_2$ (Exercise [11](#aufg-11)). So the divider acts like a source with the internal resistance $R_\mathrm i$ ([Part 5](/wissen/en/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/quellen-und-ersatzquellen/quellen-und-ersatzquellen.html)).
::::

:::ltspice Measuring the load
⁠**Draw:** source `voltage` with `9` from `in` to ground, `res` `R1 2k` from `in` to `mid`, `R2 1k` from `mid` to ground, `RL` with value `{RL}` from `mid` to ground.

⁠**Directives:** `.step param RL list 1k 2k 6k 10k 100k`, `.tran 1m`, `.meas tran u2 FIND V(mid) AT=1m`.

⁠**What you see:** The SPICE Error Log gives $U_2$ for each step: 1.80 V; 2.25 V; 2.70 V; 2.81 V; 2.98 V. Compare the value for $6\,\mathrm{k\Omega}$ with Exercise [11](#aufg-11)(b).
:::

**Application: R-2R ladder.** The current divider carries a second D/A converter (Fig. [12](#abb-12)). The trick is self-similarity: at the last node there is $2R\parallel2R=R$. Together with the $R$ in front, that again gives $2R$. So each node looks at $2R$ to the right and $2R$ downward, its current divides 1:1, and the voltage halves from node to node (divider of $R$ and $2R\parallel2R$). The source supplies $I_\mathrm{ref}=U_\mathrm{ref}/R$, and the binary-weighted currents $I_\mathrm{ref}/2$, $I_\mathrm{ref}/4$, $I_\mathrm{ref}/8$ and so on arise. An external circuit ([Part 11](/wissen/en/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/der-operationsverstarker/der-operationsverstaerker.html)) holds the collecting rail at ground potential. That is why all the $2R$ see the same potential below, whether they switch to the rail or to ground, and the currents do not change on switching. The bit near the source is the most significant (MSB, most significant bit), the one at the end the least significant (LSB). $I_\mathrm{out}$ is the sum of the switched-on currents.

:::abbildung et1/k2r2r 12
R-2R ladder with $R=1\,\mathrm{k\Omega}$ at $U_\mathrm{ref}=8$ V. Node voltages in red, branch currents in blue. The switches are set to the number 1010: $4\,\mathrm{mA}+1\,\mathrm{mA}=5$ mA flow to the collecting rail.
:::

:::frage How can the resistance fall when another one is added?
Here, “more resistors” means more paths. The existing branch continues to carry the same current, the new one carries additional current. At the same voltage, more flows in total, so $U/I$ is smaller.
:::

:::aufgabe Exercise 10 ★★ Parallel and mixed
<span class="anker" id="aufg-10"></span>

<ol class="al">

<li>

Calculate $R_\mathrm{tot}$ for $2$, $3$ and $6\,\mathrm{k\Omega}$ in parallel, and all the currents at 12 V.

</li>

<li>

10 mA divide between $1\,\mathrm{k\Omega}$ and $9\,\mathrm{k\Omega}$. How large are the two currents?

</li>

<li>

$1\,\mathrm{k\Omega}$ is in series with $4\,\mathrm{k\Omega}\parallel(1\,\mathrm{k\Omega}+3\,\mathrm{k\Omega})$ at 9 V. Determine $R_\mathrm{tot}$ and all the currents.

</li>

</ol>

:::loesung
(a) $G_\mathrm{tot}=0.5+0.333+0.167=1$ mS, so $R_\mathrm{tot}=1\,\mathrm{k\Omega}$. Currents 6, 4 and 2 mA, sum 12 mA. (b) $I_1=10\,\mathrm{mA}\cdot9/10=9$ mA, $I_2=1$ mA. The small resistor carries nine times as much. (c) $1+3=4\,\mathrm{k\Omega}$, $4\parallel4=2\,\mathrm{k\Omega}$, $R_\mathrm{tot}=3\,\mathrm{k\Omega}$. Total current 3 mA, 1.5 mA in each of the two equal branches.
:::
:::

:::aufgabe Exercise 11 ★★★ Mastering the load
<span class="anker" id="aufg-11"></span>

The divider is $R_1=2\,\mathrm{k\Omega}$, $R_2=1\,\mathrm{k\Omega}$ at 9 V.

<ol class="al">

<li>

Show from [(10.4)](#gl-10-4) that $\delta=R_\mathrm i/(R_\mathrm i+R_\mathrm L)$ with $R_\mathrm i=R_1\parallel R_2$.

</li>

<li>

Which $R_\mathrm L$ gives $\delta=10\,\%$? How large is $U_2$ then?

</li>

<li>

A divider of $200\,\Omega$ and $100\,\Omega$ has the same ratio. Calculate $U_2$ at $R_\mathrm L=1\,\mathrm{k\Omega}$. What does the better voltage cost?

</li>

<li>

Limiting case: How large is $I_\mathrm L$ for $R_\mathrm L\to0$ with the original divider?

</li>

</ol>

:::loesung
(a) Unloaded, $U_{2,0}=U\,R_2/(R_1+R_2)$. From [(10.4)](#gl-10-4) follows

$$\frac{U_2}{U_{2,0}}=\frac{R_\mathrm L\,(R_1+R_2)}{R_1R_2+R_\mathrm L\,(R_1+R_2)}=\frac{R_\mathrm L}{R_\mathrm i+R_\mathrm L},\qquad\delta=1-\frac{U_2}{U_{2,0}}=\frac{R_\mathrm i}{R_\mathrm i+R_\mathrm L}.$$

(b) $\delta=0.1$ gives $R_\mathrm L=9\,R_\mathrm i=6\,\mathrm{k\Omega}$ and $U_2=2.7$ V.

(c) $R_\mathrm i=66.7\,\Omega$, $U_2=2.81$ V, the same error as before at $10\,\mathrm{k\Omega}$. In exchange, 30 mA instead of 3 mA flow in the divider, and it converts 270 mW instead of 27 mW.

(d) $R_\mathrm L\to0$ short-circuits $R_2$: $I_\mathrm L=9\,\mathrm{V}/2\,\mathrm{k\Omega}=4.5$ mA.
:::
:::

:::aufgabe Exercise 12 ★★★ R-2R ladder
<span class="anker" id="aufg-12"></span>

A ladder with four nodes as in Fig. [12](#abb-12) has $R=10\,\mathrm{k\Omega}$ and $U_\mathrm{ref}=5$ V.

<ol class="al">

<li>

What resistance does the source see? How large are $I_\mathrm{ref}$ and the node voltages?

</li>

<li>

How large are the four currents through the upper $2R$?

</li>

<li>

How large is $I_\mathrm{out}$ at the number 1001, and how large is the smallest step?

</li>

</ol>

:::loesung
(a) The source sees $2R\parallel2R=R=10\,\mathrm{k\Omega}$, so $I_\mathrm{ref}=0.5$ mA. Node voltages 5; 2.5; 1.25; 0.625 V. (b) 0.25; 0.125; 0.0625; 0.03125 mA. (c) Number 1001: $0.25+0.03125=0.281$ mA. The smallest step is 31.25 µ A.
:::
:::
