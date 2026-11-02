---
title: Stage 6: Joint distribution, independence, uncorrelatedness
pfad: Electrical Engineering / 3rd Semester / Signals and Systems / Random Signals
order: 3270700
summary: Two random variables at once: when are they related, and what follows for their sum?
tags: joint distribution, statistically independent, uncorrelated
lang: en
---

<span class="anker" id="stufe-6"></span>

:::zweck
Two random variables at once: when are they related, and what follows for their sum?
:::

The __joint distribution__ of two variables is $P_{sg}(x,y)=\mathrm{Prob}[s\le x\ \text{and}\ g\le y]$, its density is $p_{sg}=\frac{\partial^2P_{sg}}{\partial x\,\partial y}$. From it follow the individual distributions ($P_{sg}(x,\infty)=P_s(x)$) and the correlation $\varphi_{sg}=\iint xy\,p_{sg}(x,y)\,\mathrm{d} x\,\mathrm{d} y$. For jointly stationary processes, everything depends only on the time shift $\tau$ between $s(t)$ and $g(t+\tau)$.

:::definition Definition 6.1 (Independent, uncorrelated)
<span class="anker" id="satz-6-1"></span>

$s$ and $g$ are called __statistically independent__ if $p_{sg}(x,y)=p_s(x)\,p_g(y)$. They are called __uncorrelated__ if $\mu_{sg}=\varphi_{sg}-m_sm_g=0$.
:::

Independence implies uncorrelatedness: $\varphi_{sg}=\int xp_s\mathrm{d} x\cdot\int yp_g\mathrm{d} y=m_sm_g$. The converse does not hold: uncorrelated only means that there is no *linear* relationship (Exercise [5](#aufg-5)).

**The sum of two independent variables.** The sum $s=f+g$ takes the value $x$ if $f=u$ and $g=x-u$, for any $u$:

<span class="anker" id="gl-6-1"></span>
$$p_s(x)=\int_{-\infty}^{\infty}p_{fg}(u,x-u)\,\mathrm{d} u=p_f(x)*p_g(x)\quad(\text{independent}). \tag{6.1}$$

This is the convolution from [Part 1](/wissen/en/elektrotechnik/3-semester/signale-und-systeme/lti-systeme-und-faltung/lti-systeme-und-faltung.html), where it appeared in the example of the dice. Two uniformly distributed variables give a triangular density, three give an almost bell-shaped one (Fig. [2](#abb-2)).

:::abbildung et3/k7summen 2
Probability density functions of sums of independent random variables, each uniformly distributed on $[-\frac12,\frac12]$. Even the sum of three lies close to the Gaussian curve with the same variance (at $x=0$: 0.75 versus 0.80).
:::

:::aufgabe Exercise 5 ★★ Uncorrelated, but dependent
<span class="anker" id="aufg-5"></span>

$s$ is uniformly distributed on $[-1,1]$ and $g=s^2$. Show that $s$ and $g$ are uncorrelated, although $g$ is completely determined by $s$.

:::loesung
$m_s=0$ and $\mathrm E\{sg\}=\mathrm E\{s^3\}=\frac12\int_{-1}^1x^3\mathrm{d} x=0$, so $\mu_{sg}=0-0\cdot m_g=0$: uncorrelated. Nevertheless, $s$ determines the value of $g$. The relationship is quadratic, and a correlation captures only linear relationships: for positive $s$, $g$ increases with $s$; for negative $s$, it decreases; on average, the two tendencies cancel.
:::
:::
