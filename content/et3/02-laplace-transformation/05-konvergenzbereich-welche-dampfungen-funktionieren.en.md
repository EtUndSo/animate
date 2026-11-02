---
title: Region of convergence: which damping rates work
pfad: Electrical Engineering / 3rd Semester / Signals and Systems / Laplace Transform
order: 3220500
summary: Every signal as a superposition of $\ee^{pt}$, and why an LTI system turns this into a multiplication
tags: 
lang: en
---

<span class="anker" id="stufe-2-3"></span>

**The idea.** The factor $\mathrm{e}^{-\sigma t}$ acts on both sides of the time axis, but in opposite ways. For $t\to+\infty$ it damps more strongly the larger $\sigma$ is. For $t\to-\infty$, $\mathrm{e}^{-\sigma t}=\mathrm{e}^{\sigma|t|}$, so there a large $\sigma$ amplifies. This gives the three shapes of the region of convergence:

<ul>

<li>

⁠**right-sided signal**, $s(t)=0$ for $t<0$, growing at most like $\mathrm{e}^{\alpha t}$: every $\sigma>\alpha$ works. Region of convergence: the half-plane to the *right* of a boundary.

</li>

<li>

⁠**left-sided signal**: only the side $t\to-\infty$ matters, and small $\sigma$ help. Region of convergence: a half-plane to the *left* of a boundary.

</li>

<li>

⁠**two-sided signal**: both conditions must hold at once. Region of convergence: a *strip*, which may also be empty.

</li>

</ul>

Why are the boundaries always vertical? Because $|\mathrm{e}^{-pt}|=\mathrm{e}^{-\sigma t}$. Whether $\int|s(t)\mathrm{e}^{-pt}|\mathrm{d} t$ is finite depends only on $\sigma$, never on $f$.

⁠**In short:** The region of convergence is the set of all damping rates $\sigma$ for which $s(t)\,\mathrm{e}^{-\sigma t}$ becomes absolutely integrable.

:::merke The basic transform pairs (used throughout the chapter)
For any complex number $p_0$:

<span class="anker" id="gl-2-2"></span>
<span class="anker" id="gl-2-3"></span>
<span class="anker" id="gl-2-4"></span>
<span class="anker" id="gl-2-5"></span>
$$\begin{aligned} \mathrm{e}^{p_0t}\,\varepsilon(t)\quad&\longleftrightarrow\quad\frac{1}{p-p_0},&&\operatorname{Re} p>\operatorname{Re} p_0,\\ -\mathrm{e}^{p_0t}\,\varepsilon(-t)\quad&\longleftrightarrow\quad\frac{1}{p-p_0},&&\operatorname{Re} p<\operatorname{Re} p_0,\\ \delta(t)\quad&\longleftrightarrow\quad1,&&\text{all }p,\\ t\,\varepsilon(t)\quad&\longleftrightarrow\quad\frac{1}{p^2},&&\operatorname{Re} p>0. \end{aligned} \tag{2.2|2.3|2.4|2.5}$$

With $p_0=0$, [(2.2)](#gl-2-2) gives the step: $\varepsilon(t)\leftrightarrow1/p$ for $\operatorname{Re} p>0$. The first two lines have the *same* expression and different regions of convergence: only the expression and the region of convergence together determine the signal.
:::

:::herleitung Basic transform pairs
[(2.2)](#gl-2-2): $\int_0^\infty\mathrm{e}^{-(p-p_0)t}\mathrm{d} t=\Bigl[\frac{-\mathrm{e}^{-(p-p_0)t}}{p-p_0}\Bigr]_0^\infty=\frac{1}{p-p_0}$. The value at the upper limit vanishes if and only if $\operatorname{Re}(p-p_0)>0$.

[(2.3)](#gl-2-3): $-\int_{-\infty}^0\mathrm{e}^{-(p-p_0)t}\mathrm{d} t=-\Bigl[\frac{-\mathrm{e}^{-(p-p_0)t}}{p-p_0}\Bigr]_{-\infty}^0=\frac{1}{p-p_0}$. The value for $t\to-\infty$ vanishes if and only if $\operatorname{Re}(p-p_0)<0$.

[(2.4)](#gl-2-4): sifting property, $\int\delta(t)\mathrm{e}^{-pt}\mathrm{d} t=\mathrm{e}^{0}=1$.

[(2.5)](#gl-2-5): integration by parts, $\int_0^\infty t\,\mathrm{e}^{-pt}\mathrm{d} t=\Bigl[\frac{-t\,\mathrm{e}^{-pt}}{p}\Bigr]_0^\infty+\frac1p\int_0^\infty\mathrm{e}^{-pt}\mathrm{d} t=0+\frac{1}{p^2}$ for $\operatorname{Re} p>0$.
:::

:::frage Why do the exponential terms drop out when evaluating $\int_0^\infty\mathrm{e}^{-bt}\mathrm{e}^{-pt}\mathrm{d} t$, and why is the result $\frac{1}{b+p}$ and not $\frac{1}{-(b+p)}$?
Both come from inserting the limits. The antiderivative of $\mathrm{e}^{-(b+p)t}$ is $-\frac{\mathrm{e}^{-(b+p)t}}{b+p}$, with a minus sign because differentiating produces the factor $-(b+p)$. Then you compute “upper limit minus lower limit”:

$$\int_0^\infty\mathrm{e}^{-(b+p)t}\mathrm{d} t=\underbrace{\lim_{t\to\infty}\Bigl(-\frac{\mathrm{e}^{-(b+p)t}}{b+p}\Bigr)}_{=\,0}-\Bigl(-\frac{\mathrm{e}^{0}}{b+p}\Bigr)=\frac{1}{b+p}.$$

<ul>

<li>

⁠**Upper limit:** $|\mathrm{e}^{-(b+p)t}|=\mathrm{e}^{-(\operatorname{Re} b+\sigma)t}$ tends to zero if and only if $\operatorname{Re} p>-\operatorname{Re} b$. This condition *is* the region of convergence. Outside it, the exponential term would remain and grow without bound.

</li>

<li>

⁠**Lower limit:** $\mathrm{e}^0=1$, so no exponential term is left there.

</li>

<li>

⁠**Sign:** The minus sign of the antiderivative meets the minus sign with which the lower limit is subtracted. Minus times minus gives plus.

</li>

</ul>

For the left-sided pulse $\mathrm{e}^{-bt}\varepsilon(-t)$ it is the other way round. The integral runs from $-\infty$ to $0$, so now $t=0$ is the *upper* limit. Its contribution $-\frac{1}{b+p}$ is not subtracted, so the minus sign remains. The lower limit $t\to-\infty$ vanishes only for $\operatorname{Re}(b+p)<0$, which is why this region of convergence lies on the left. With $p_0=-b$ these are the basic transform pairs [(2.2)](#gl-2-2) and [(2.3)](#gl-2-3).
:::

:::frage Do we look at the real parts of $b$ and $p$ because the decay of the integrand decides integrability? For some $b$ the signal decays, for others it grows and does not fall to zero, and the integral does not converge because something keeps being added.
Yes, exactly. The magnitude of the integrand is

$$\bigl|\mathrm{e}^{-(b+p)t}\bigr|=\mathrm{e}^{-\operatorname{Re}(b+p)\,t}\cdot\underbrace{\bigl|\mathrm{e}^{-\mathrm{j}\operatorname{Im}(b+p)\,t}\bigr|}_{=\,1}.$$

The imaginary part only makes the integrand rotate in the complex plane; it does not change the magnitude. Growth or decay is decided by the real part alone. Three refinements:

<ul>

<li>

What counts is the *sum* $\operatorname{Re} b+\sigma$. The signal itself may grow ($\operatorname{Re} b<0$) as long as the damping $\sigma$ is stronger. This is the “damp” trick from Section 2.2.

</li>

<li>

“Tends to zero” alone is not enough. $1/t$ also tends to zero, but $\int_1^\infty\frac{\mathrm{d} t}{t}=\infty$, because the contributions shrink too slowly. Exponential decay is fast enough: $\int_0^\infty\mathrm{e}^{-\operatorname{Re}(b+p)t}\mathrm{d} t=\frac{1}{\operatorname{Re}(b+p)}$ is finite.

</li>

<li>

On the boundary $\operatorname{Re}(b+p)=0$ the integrand has the constant magnitude 1 and only rotates. The integral then oscillates instead of approaching a value, and exactly at the pole it even grows linearly (Exercise [3a](#aufg-3a)). This is why the boundary line does not belong to the region of convergence.

</li>

</ul>
:::

:::frage So does this hold for any function at all?
No, only for functions with a non-empty region of convergence. Three counterexamples:

<ul>

<li>

$\mathrm{e}^{t^2}\varepsilon(t)$ grows faster than any exponential function. $\mathrm{e}^{t^2-\sigma t}\to\infty$ for every $\sigma$, so no damping is enough.

</li>

<li>

$\mathrm{e}^{|t|}$: the right half requires $\sigma>1$, the left half $\sigma<-1$. Both at once is impossible.

</li>

<li>

Even the constant $s(t)=1$ for all $t$: on the right $\sigma>0$, on the left $\sigma<0$. The Fourier transform still covers such signals, with a Dirac impulse in the spectrum.

</li>

</ul>

For right-sided signals with at most exponential growth it always works. This includes every signal that is switched on in a circuit at $t=0$.
:::

:::frage Why is a single line enough when the $p$-plane is two-dimensional?
Every line in the region of convergence gives the same $s(t)$: with a larger $\sigma$ you damp more strongly in step 1 and multiply back more strongly in step 3, and the two cancel. Numerically confirmed: with $\sigma=0.2$ and $\sigma=1/\mathrm s$, the step gives $s(1\,\mathrm{s})\approx1.00$ and $s(-1\,\mathrm{s})\approx0.00$ both times. So the plane contains more than you need for the superposition. Its use lies elsewhere: in the plane, $S(p)$ can be described by a few numbers, the poles and zeros. (Aside: $S(p)$ is complex differentiable in the region of convergence, so its values on one line determine the function in the whole region.)
:::

:::aufgabe Exercise 2 ★ Laplace is Fourier of a damped signal
<span class="anker" id="aufg-2"></span>

<ol class="al">

<li>

Show that $S(\sigma+\mathrm{j}2\pi f)=\mathcal{F}\{s(t)\,\mathrm{e}^{-\sigma t}\}(f)$ by splitting $\mathrm{e}^{-pt}$ into two factors.

</li>

<li>

Check it for the step: compute $\mathcal{F}\{\mathrm{e}^{-\sigma t}\varepsilon(t)\}$ for $\sigma>0$ directly and compare with $S(p)=1/p$.

</li>

</ol>

:::loesung
(a) $S(\sigma+\mathrm{j}2\pi f)=\int s(t)\,\mathrm{e}^{-(\sigma+\mathrm{j}2\pi f)t}\mathrm{d} t=\int\bigl[s(t)\mathrm{e}^{-\sigma t}\bigr]\mathrm{e}^{-\mathrm{j}2\pi ft}\mathrm{d} t=\mathcal{F}\{s(t)\mathrm{e}^{-\sigma t}\}(f)$.

(b) $\mathcal{F}\{\mathrm{e}^{-\sigma t}\varepsilon(t)\}=\int_0^\infty\mathrm{e}^{-(\sigma+\mathrm{j}2\pi f)t}\mathrm{d} t=\dfrac{1}{\sigma+\mathrm{j}2\pi f}$ for $\sigma>0$. This is $1/p$ at the point $p=\sigma+\mathrm{j}2\pi f$.
:::
:::

:::aufgabe Exercise 3 ★★ A growing signal
<span class="anker" id="aufg-3"></span>

$s(t)=\mathrm{e}^{2t}\varepsilon(t)$, for example the impulse response of an unstable system ($t$ in s).

<ol class="al">

<li>

Why is there no Fourier transform in the classical sense?

</li>

<li>

For which $\sigma$ is $s(t)\,\mathrm{e}^{-\sigma t}$ absolutely integrable?

</li>

<li>

Compute $S(p)$ directly from the integral. Sketch the pole and the region of convergence in the $p$-plane.

</li>

<li>

Which $\sigma$ may you use in the inversion formula? The expression $S(\mathrm{j}2\pi f)$ is finite. Why may you still not choose $\sigma=0$, and which signal would $\sigma=0$ give? (Hint: [(2.3)](#gl-2-3).)

</li>

</ol>

:::loesung
(a) $\int_0^\infty\mathrm{e}^{2t}\mathrm{d} t=\infty$: the signal is not absolutely integrable. Intuitively: nothing that grows can be built from oscillations of constant amplitude.

(b) $|s(t)\mathrm{e}^{-\sigma t}|=\mathrm{e}^{(2-\sigma)t}$ for $t>0$, integrable if and only if $\sigma>2/\mathrm s$.

(c) $S(p)=\int_0^\infty\mathrm{e}^{-(p-2)t}\mathrm{d} t=\dfrac{1}{p-2}$ for $\operatorname{Re} p>2$. Pole at $p=2$, region of convergence to the right of it, as for every right-sided signal. Numerical check: $S(3)=1$, $S(2.5+\mathrm{j})=0.4-0.8\mathrm{j}$.

(d) Any $\sigma>2/\mathrm s$, for example $\sigma=3/\mathrm s$. The value $\sigma=0$ lies to the left of the pole, so outside the region of convergence. The expression $1/(\mathrm{j}2\pi f-2)$ is finite, but it belongs to a *different* signal: by [(2.3)](#gl-2-3), $-\mathrm{e}^{2t}\varepsilon(-t)$ also has the transform $1/(p-2)$, with region of convergence $\operatorname{Re} p<2$. With $\sigma=0$ you would get this left-sided, decaying signal. It is the signal whose Fourier transform really is $1/(\mathrm{j}2\pi f-2)$.
:::
:::

:::aufgabe Exercise 3a ★★ What happens on the boundary
<span class="anker" id="aufg-3a"></span>

$s(t)=\mathrm{e}^{(1+3\mathrm{j})t}\varepsilon(t)$, so $b=-1-3\mathrm{j}$ ($t$ in s).

<ol class="al">

<li>

For which $\sigma$ does $\int_0^\infty s(t)\,\mathrm{e}^{-pt}\mathrm{d} t$ converge? What role does the 3 play?

</li>

<li>

Set $p=1+\mathrm{j}\omega$, exactly on the boundary, and compute $\int_0^T s(t)\,\mathrm{e}^{-pt}\mathrm{d} t$. What happens as $T\to\infty$? Distinguish $\omega\neq3$ and $\omega=3$. Where is the pole?

</li>

</ol>

:::loesung
(a) $b+p=(\sigma-1)+\mathrm{j}(\omega-3)$ with $p=\sigma+\mathrm{j}\omega$. The magnitude of the integrand is $\mathrm{e}^{-(\sigma-1)t}$, so the integral converges if and only if $\sigma>1$. The 3 (the angular frequency of the signal) does not appear in the magnitude. It only determines where on the boundary line the pole sits: $S(p)=\frac{1}{p-(1+3\mathrm{j})}$, pole at $p=1+3\mathrm{j}$.

(b) With $p=1+\mathrm{j}\omega$, $b+p=\mathrm{j}(\omega-3)$.

<ul>

<li>

$\omega\neq3$: $\displaystyle\int_0^T\mathrm{e}^{-\mathrm{j}(\omega-3)t}\mathrm{d} t=\frac{1-\mathrm{e}^{-\mathrm{j}(\omega-3)T}}{\mathrm{j}(\omega-3)}$. As $T$ grows, the numerator runs around a circle centered at 1 and approaches no value. The integral stays bounded but has no limit.

</li>

<li>

$\omega=3$, that is, exactly at the pole $p=1+3\mathrm{j}$: the integrand is constantly 1, the integral equals $T$ and grows without bound.

</li>

</ul>

So the integral converges nowhere on the boundary line. The region of convergence is the open half-plane $\operatorname{Re} p>1$.
:::
:::

:::aufgabe Exercise 4 ★ True or false? Give reasons
<span class="anker" id="aufg-4"></span>

<ol class="al">

<li>

Every function has a Laplace transform.

</li>

<li>

Whether $p$ lies in the region of convergence depends only on $\operatorname{Re} p$.

</li>

<li>

If the imaginary axis lies in the region of convergence, $S(\mathrm{j}2\pi f)$ is the Fourier transform of $s(t)$.

</li>

<li>

In the inversion formula, $\sigma=1/\mathrm s$ gives a different signal than $\sigma=2/\mathrm s$ if both lie in the region of convergence.

</li>

<li>

$\cos(2\pi f_0t)$ is an eigenfunction of every LTI system.

</li>

</ol>

:::loesung
(a) False. Counterexamples: $\mathrm{e}^{t^2}\varepsilon(t)$, $\mathrm{e}^{|t|}$, the two-sided constant.

(b) True. $|s(t)\mathrm{e}^{-pt}|=|s(t)|\mathrm{e}^{-\sigma t}$; the frequency $f$ does not appear in the magnitude. This is why the region of convergence consists of whole vertical lines.

(c) True. With $\sigma=0$, $S(\mathrm{j}2\pi f)=\int s(t)\mathrm{e}^{-\mathrm{j}2\pi ft}\mathrm{d} t=\mathcal{F}\{s\}(f)$.

(d) False. Every line in the region of convergence gives the same signal, because the damping by $\mathrm{e}^{-\sigma t}$ and the multiplication back by $\mathrm{e}^{\sigma t}$ cancel.

(e) False. The output is $|H|\cos(2\pi f_0t+\varphi)$ with $H=H(\mathrm{j}2\pi f_0)$. It is a multiple of $\cos(2\pi f_0t)$ only if $\varphi=0$ or $\varphi=\pi$, that is, only if $H(\mathrm{j}2\pi f_0)$ is real. For the RC low-pass filter this is not the case at any frequency $f_0>0$.
:::
:::
