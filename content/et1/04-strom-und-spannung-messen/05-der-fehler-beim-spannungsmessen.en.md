---
title: Stage 4: The error in measuring voltage
pfad: Electrical Engineering / 1st Semester / Fundamentals of Electrical Engineering / Measuring Current and Voltage
order: 1140500
summary: The voltmeter lies outside the circuit, and yet current flows through it.
tags: 
lang: en
---

<span class="anker" id="stufe-4"></span>

:::zweck
The voltmeter lies outside the circuit, and yet current flows through it. This stage shows when that lowers the voltage it is supposed to measure.
:::

**The idea.** The voltmeter opens a second current path between two nodes. Its current has to come from somewhere. If a current source (it holds its current fixed, [Part 5](/wissen/en/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/quellen-und-ersatzquellen/quellen-und-ersatzquellen.html)) drives the load resistor $R_L$, the fixed current divides: whatever flows through the voltmeter is missing in $R_L$, and the voltage falls (Fig. [5](#abb-5)). If, on the other hand, $R_L$ hangs directly on an ideal voltage source, the source supplies the additional current and nothing changes. Errors therefore arise only where the current cannot flow in freely. In the voltage divider, $R_1$ slows the supply: the total current rises, more drops across $R_1$, and the midpoint falls.

:::abbildung et1/k4spannung 5
The voltmeter (range 10 V, dashed: internal resistance and ideal device) on two equivalent circuits. In both it diverts 13.6 µ A, and the reading falls from 3 V to 2.727 V.
:::

:::satz Theorem 4.1 (Error of the voltmeter)
<span class="anker" id="satz-4-1"></span>

On a current source $I_\mathrm q$ with load $R_L$, without a meter $U_L=I_\mathrm qR_L$, and with a meter

<span class="anker" id="gl-4-1"></span>
$$U_L'=I_\mathrm q\,(R_L\parallel R_\mathrm i)=U_L\cdot\frac{1}{1+R_L/R_\mathrm i}. \tag{4.1}$$

The relative error is $f=-R_L/(R_L+R_\mathrm i)$, so for $R_L\ll R_\mathrm i$, $f\approx-R_L/R_\mathrm i$. On the voltage divider the same holds with $R_L=R_1\parallel R_2$.
:::

⁠**How to read it:** The fraction is the error factor. $R_L$ is the resistance the meter finds between its terminals. A small error requires $R_\mathrm i\gg R_L$, ideally $R_\mathrm i\to\infty$. **Validity:** ideal sources, resistances independent of the voltage.

:::herleitung Error factor
With the node rule $I_\mathrm q=I_{RL}'+I_{\mathrm{i}}$, the current divides between two parallel resistors, and $U_L'$ is across both. So $U_L'=I_\mathrm q\,R_LR_\mathrm i/(R_L+R_\mathrm i)$, and canceling $R_\mathrm i$ gives [(4.1)](#gl-4-1). On the divider, without a meter $U_2=U\,R_2/(R_1+R_2)$. With a meter, $R_2$ is replaced by $R_2\parallel R_\mathrm i$ (loaded voltage divider, [Part 2](/wissen/en/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/strom-widerstand-und-kirchhoff/strom-widerstand-und-kirchhoff.html)):

$$U_2'=U\,\frac{R_2R_\mathrm i}{R_1R_2+R_\mathrm i(R_1+R_2)} \quad\Rightarrow\quad \frac{U_2'}{U_2}=\frac{R_\mathrm i(R_1+R_2)}{R_1R_2+R_\mathrm i(R_1+R_2)}=\frac{1}{1+(R_1\parallel R_2)/R_\mathrm i}.$$
:::

**Example.** On the divider, $R_1\parallel R_2=20$ k$\Omega$ and $R_L/R_\mathrm i=0.1$. The reading is $3\,\mathrm{V}/1.1=2.727$ V, so $f=-9.1\,\%$. The mechanism in numbers: the current through $R_1$ rises from 100 µ A to 104.5 µ A, of which 90.9 µ A flow through $R_2$ and 13.6 µ A through the voltmeter. The same values result from $I_\mathrm q=150$ µ A on $R_L=20$ k$\Omega$. A digital multimeter with 10 M$\Omega$ shows 2.994 V, so $f=-0.2\,\%$.

⁠**Limiting cases:** $R_\mathrm i\to\infty$ gives $f\to0$. $R_L\to0$ (source directly on the meter) also gives $f\to0$. At $R_\mathrm i=R_L$ the voltage is halved.

:::frage 200 k$\Omega$ sounds like a lot. Why does the meter still disturb the divider?
Large or small exists only in comparison with $R_L$. The divider carries only 100 µ A. Next to that, 13.6 µ A are not a small share.
:::

:::aufgabe Exercise 4 ★★ High-resistance divider
<span class="anker" id="aufg-4"></span>

$R_1=6$ M$\Omega$ and $R_2=3$ M$\Omega$ are connected to 9 V. (a) What do the voltmeter with 200 k$\Omega$ and the digital multimeter with 10 M$\Omega$ show across $R_2$? (b) How do you recover the true value from the reading 2.5 V? (c) What $R_\mathrm i$ would be needed for 1 % error?

:::loesung
(a) $R_L=6\,\mathrm{M\Omega}\parallel3\,\mathrm{M\Omega}=2$ M$\Omega$, the true value is 3 V. With 200 k$\Omega$: $3\,\mathrm{V}/(1+10)=0.273$ V, $f=-91\,\%$. With 10 M$\Omega$: $3\,\mathrm{V}/(1+0.2)=2.5$ V, $f=-16.7\,\%$.

(b) Rearranging [(4.1)](#gl-4-1): $U=U'(1+R_L/R_\mathrm i)=2.5\,\mathrm{V}\cdot1.2=3$ V. (c) $R_L/(R_L+R_\mathrm i)\le0.01$ gives $R_\mathrm i\ge99\,R_L=198$ M$\Omega$.
:::
:::
