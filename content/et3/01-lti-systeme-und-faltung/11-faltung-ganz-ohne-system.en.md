---
title: Stage 10: Convolution without any system
pfad: Electrical Engineering / 3rd Semester / ET3 – Fundamentals of Electrical Engineering 3: Signals and Systems / LTI Systems and Convolution
adresse: elektrotechnik/3-semester/signale-und-systeme/lti-systeme-und-faltung
knoten: Chapter 1: LTI Systems and Convolution
order: 3211100
summary: Why the response to a single impulse describes the whole system
tags: 
lang: en
---

<span class="anker" id="stufe-10"></span>

:::frage Convolution is usually explained with a system that a signal passes through. What does it mean when no system is involved at all?
Convolution is a mathematical operation with a general meaning of its own: *for every way of splitting a result into two parts, multiply the weights of the two parts, and sum over all splittings.* The system is one interpretation of this (part 1: when did the impulse arrive; part 2: how old is it), not the only one.

⁠**An example with neither a system nor time: two dice.** What is the probability that the sum of the dice is $k$? Every splitting $k=i+(k-i)$ contributes, with the probability $P_1(i)\,P_2(k-i)$:

$$P(k)=\sum_iP_1(i)\,P_2(k-i).$$

This is a convolution, with exactly the same structure as $g(t)=\int s(\tau)h(t-\tau)\mathrm{d}\tau$: $\tau$ corresponds to the number on the first die, $t$ to the sum, and $t-\tau$ to the number on the second die. Two uniformly distributed dice (“rectangles”) give a triangular distribution, just like $\operatorname{rect}*\operatorname{rect}=\Lambda$ in Exercise [5](die-faltung-ausrechnen.html#aufg-5). The sum 7 is the most frequent because it has the most splittings (Fig. [9](#abb-9)).

More examples: a moving average over measured values is a convolution with a rectangle. A blurred photo is the sharp image convolved with the spot of light that the optics make from a single point. And multiplying two polynomials convolves their coefficients (Exercise [11](#aufg-11)).
:::

:::abbildung et3/k1wuerfel 9
Probabilities of the sum of the dice. Each distribution is the convolution of the previous one with that of a single die. The rectangle becomes a triangle ($P(7)=6/36$), and the triangle becomes a bell-shaped curve ($P(10)=P(11)=27/216$).
:::

:::zusatz Why convolutions occur so often
If you convolve more and more identical distributions, the result approaches a Gaussian curve, almost regardless of the initial shape (central limit theorem). That is why noise, the sum of many small independent influences, is so often Gaussian.
:::

:::aufgabe Exercise 11 ★ Convolution with dice and polynomials
<span class="anker" id="aufg-11"></span>

<ol class="al">

<li>

Compute $P(7)$ and $P(4)$ for two dice from the convolution sum. Which splittings contribute in each case?

</li>

<li>

Compute $P(10)$ for three dice by convolving the distribution for two dice with the distribution for one die.

</li>

<li>

Multiply out $(1+2x)(3+x)$. Show that the coefficient sequence of the result is the convolution of the sequences $(1,2)$ and $(3,1)$.

</li>

</ol>

:::loesung
(a) $P(7)$: splittings $1+6,\,2+5,\dots,6+1$, six in all, each with $\frac16\cdot\frac16$: $P(7)=\frac{6}{36}=\frac16$. $P(4)$: $1+3,\,2+2,\,3+1$: $\frac{3}{36}=\frac{1}{12}$.

(b) $P_3(10)=\sum_{j=1}^6P_2(10-j)\cdot\frac16=\frac16\bigl[P_2(9)+P_2(8)+P_2(7)+P_2(6)+P_2(5)+P_2(4)\bigr]=\frac16\cdot\frac{4+5+6+5+4+3}{36}=\frac{27}{216}=\frac18$.

(c) $(1+2x)(3+x)=3+x+6x+2x^2=3+7x+2x^2$. The coefficient of $x^k$ collects all pairs of powers with $i+j=k$: $c_0=1\cdot3=3$, $c_1=1\cdot1+2\cdot3=7$, $c_2=2\cdot1=2$. This is the convolution sum $c_k=\sum_ia_ib_{k-i}$, the same structure as with the dice.
:::
:::
