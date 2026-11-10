---
title: Numerical differentiation and the gradient check
pfad: Computer Science / Machine Learning / Mathematical Foundations / Derivative, Gradient and Chain Rule
adresse: informatik/machine-learning/mathematische-grundlagen/ableitung-gradient-und-kettenregel
knoten: Chapter 3: Derivative, Gradient and Chain Rule
nachschlagen: ja
order: 15231200
summary: You can also estimate derivatives without a formula: you evaluate the function at two nearby points and form the difference quotient.
tags: forward difference, truncation error, central difference, floating-point numbers, machine epsilon, catastrophic cancellation, gradient check, relative error
lang: en
---

<span class="anker" id="stufe-11"></span>

:::zweck
You can also estimate derivatives without a formula: you evaluate the function at two nearby points and form the difference quotient. This is too slow for computing all derivatives of a function with many inputs, but ideal for checking a derivative that you derived or programmed. This section shows how accurate the two usual quotients are, why too small a step size does harm, and how to carry out and assess a gradient check.
:::

### The forward difference

<span class="anker" id="stufe-11-1"></span>

By the definition [(1.3)](die-ableitung.html#gl-1-3), the difference quotient approaches the derivative as $h$ goes to zero. If you compute it with a fixed small $h$, you get an approximation, and the question is how good it is.

:::definition Definition 11.1 (Forward difference)
<span class="anker" id="satz-11-1"></span>

For a fixed step size $h>0$,

<span class="anker" id="gl-11-1"></span>
$$D_+f(x)=\frac{f(x+h)-f(x)}{h} \tag{11.1}$$

is called the __forward difference__. Its deviation from $f'(x)$ that arises solely because $h$ is not zero is called the __truncation error__.
:::

The quadratic approximation [(1.6)](die-ableitung.html#gl-1-6) gives the truncation error: substituting $f(x+h)\approx f(x)+f'(x)h+\tfrac12f''(x)h^2$ gives

<span class="anker" id="gl-11-2"></span>
$$D_+f(x)\approx f'(x)+\tfrac12f''(x)\,h . \tag{11.2}$$

So the error is roughly proportional to $h$: a ten times smaller $h$ gives a roughly ten times smaller truncation error.

::::beispiel [Worked example]
For $f(x)=x^3$ at the point $2$ with $h=10^{-3}$, $2.001^3=8.012006001$ and

$$D_+f(2)=\frac{8.012006001-8}{0.001}=12.006001 .$$

The error $0.006001$ matches $\tfrac12f''(2)\,h=\tfrac12\cdot12\cdot0.001=0.006$; the remainder $0.000001=h^2$ is the next term.
::::

⁠**In short:** The forward difference has a truncation error of about $\tfrac12f''(x)\,h$, proportional to the step size.

### The central difference

<span class="anker" id="stufe-11-2"></span>

The forward difference measures the slope of the secant line between $x$ and $x+h$, and for a curved graph this secant line is systematically steeper or flatter than the tangent line at $x$. If you place the secant line symmetrically around $x$, from $x-h$ to $x+h$, this error cancels out.

:::definition Definition 11.2 (Central difference)
<span class="anker" id="satz-11-2"></span>

For a fixed step size $h>0$,

<span class="anker" id="gl-11-3"></span>
$$D_0f(x)=\frac{f(x+h)-f(x-h)}{2h} \tag{11.3}$$

is called the __central difference__.
:::

:::satz Theorem 11.3 (Truncation error of the central difference)
<span class="anker" id="satz-11-3"></span>

If $f$ has a continuous third derivative, then

<span class="anker" id="gl-11-4"></span>
$$D_0f(x)\approx f'(x)+\tfrac16f'''(x)\,h^2 . \tag{11.4}$$

So the truncation error is roughly proportional to $h^2$.
:::

:::herleitung Why the curvature cancels
You continue the quadratic approximation from Section [1.5](die-ableitung.html#stufe-1-5) by one term. If, as with the parabola there, you also match the third derivative, the term $\tfrac16f'''(x)\,h^3$ is added; the factor $\tfrac16$ arises because the third derivative of $h^3$ equals $6$. Thus

$$f(x\pm h)\approx f(x)\pm f'(x)\,h+\tfrac12f''(x)\,h^2\pm\tfrac16f'''(x)\,h^3 .$$

If you subtract the two equations from each other, the terms with even powers of $h$ drop out, because they have the same sign in both equations: $f(x)$ and the curvature term $\tfrac12f''h^2$. What remains is $f(x+h)-f(x-h)\approx2f'(x)\,h+\tfrac13f'''(x)\,h^3$, and dividing by $2h$ gives [(11.4)](#gl-11-4). Intuitively: the curvature makes the right secant line steeper and the left one flatter, and the central difference is the mean of the two.
:::

For a quadratic function, $f'''=0$, and the central difference is exact for every $h$. It needs two new evaluations of $f$, the forward difference only one if $f(x)$ is already known.

::::beispiel [Worked example]
For $f(x)=x^3$ at the point $2$ with $h=10^{-3}$, $1.999^3=7.988005999$ and

$$D_0f(2)=\frac{8.012006001-7.988005999}{0.002}=\frac{0.024000002}{0.002}=12.000001 .$$

The error is $0.000001=\tfrac16\cdot6\cdot h^2$, six thousand times smaller than with the forward difference.
::::

⁠**In short:** The central difference has a truncation error of about $\tfrac16f'''(x)\,h^2$, because the curvature term cancels.

### What you need for this: floating-point numbers

<span class="anker" id="stufe-11-3"></span>

According to the two formulas for the truncation error, you would only have to choose $h$ small enough. With a calculator and with any numerical software, this goes wrong, and the reason is the way computers store numbers.

Computers store non-integers as __floating-point numbers__: as a number with a fixed number of digits in the binary system, times a power of two. The usual choice is double precision according to the IEEE 754 standard, with $53$ binary digits, which is about $16$ decimal digits. The result of every arithmetic operation is rounded to the nearest representable number. The relative error of this rounding is at most $2^{-53}\approx1.1\cdot10^{-16}$. The distance from $1$ to the next larger representable number is twice as large,

$$\varepsilon_{\mathrm M}=2^{-52}\approx2.2\cdot10^{-16};$$

this number is called __machine epsilon__, and numerical software reports it under this name. In single precision with $24$ binary digits, about $7$ decimal digits, $\varepsilon_{\mathrm M}=2^{-23}\approx1.2\cdot10^{-7}$.

Rounding becomes dangerous when you subtract almost equal numbers. The leading digits cancel, the rounding errors of the trailing ones remain, and only a few digits of the result are still correct. This is called __catastrophic cancellation__. A difference quotient subtracts exactly such numbers from each other, and the smaller $h$ is, the more similar they are.

::::beispiel [Worked example]
For $f(x)=x^3$ at the point $2$ and $h=10^{-8}$, $f(2+h)=8.00000012\ldots$ Both function values are about $8$, and each carries a rounding error of up to about $8\cdot1.1\cdot10^{-16}\approx9\cdot10^{-16}$. Their difference is about $1.2\cdot10^{-7}$; an error of $10^{-15}$ in it is a relative error of almost $10^{-8}$. So after the subtraction, only about $8$ of the $16$ digits are still correct, and the division by $h$ changes nothing about that.
::::

⁠**In short:** Computers round every result to about $16$ digits, $\varepsilon_{\mathrm M}=2^{-52}$; when you subtract almost equal numbers, only a few correct digits remain.

### The error curve

<span class="anker" id="stufe-11-4"></span>

In a difference quotient, two errors therefore work against each other. The truncation error becomes smaller with smaller $h$. The rounding error becomes larger with smaller $h$: the error of the difference in the numerator stays about the same, but it is divided by an ever smaller $h$.

:::satz Theorem 11.4 (Total error of the difference quotients)
<span class="anker" id="satz-11-4"></span>

If the function values are accurate up to a relative error of at most $\tfrac12\varepsilon_{\mathrm M}$, the total error is approximately at most

<span class="anker" id="gl-11-5"></span>
$$E_+(h)=\tfrac12|f''(x)|\,h+\frac{\varepsilon_{\mathrm M}|f(x)|}{h}\qquad\text{and}\qquad E_0(h)=\tfrac16|f'''(x)|\,h^2+\frac{\varepsilon_{\mathrm M}|f(x)|}{2h} \tag{11.5}$$

for the forward and the central difference, respectively. $E_+$ is smallest at $h_+=\sqrt{2\varepsilon_{\mathrm M}|f|/|f''|}$, with the value $\sqrt{2\varepsilon_{\mathrm M}|f|\,|f''|}$; $E_0$ is smallest at $h_0=\bigl(\tfrac32\varepsilon_{\mathrm M}|f|/|f'''|\bigr)^{1/3}$.
:::

:::herleitung The best step size
The numerator contains two function values, each with a rounding error of up to $\tfrac12\varepsilon_{\mathrm M}|f|$, together up to $\varepsilon_{\mathrm M}|f|$. For the forward difference, this is divided by $h$, for the central one by $2h$. On top of that come the truncation errors [(11.2)](#gl-11-2) and [(11.4)](#gl-11-4). A function of the form $a\,h+b/h$ with $a,b>0$ has the derivative $a-b/h^2$, which becomes zero at $h=\sqrt{b/a}$; there, the value is $2\sqrt{ab}$. With $a=\tfrac12|f''|$ and $b=\varepsilon_{\mathrm M}|f|$, this gives $h_+$. For $a\,h^2+b/h$, the derivative is $2ah-b/h^2$, which becomes zero at $h^3=b/(2a)$; with $a=\tfrac16|f'''|$ and $b=\tfrac12\varepsilon_{\mathrm M}|f|$, this gives $h_0$.
:::

If you plot the error against $h$ on log-log axes, a V appears (Fig. [20](#abb-20)). On the right, the curve rises with slope $1$ (forward) or $2$ (central), because the truncation error dominates there. On the left, it falls with slope $-1$, because the rounding error dominates there. The measured points on the left scatter, because rounding errors turn out larger or smaller depending on the number; [(11.5)](#gl-11-5) gives only their order of magnitude. As a rule of thumb, you choose $h\approx\sqrt{\varepsilon_{\mathrm M}}\approx10^{-8}$ for the forward difference and $h\approx\varepsilon_{\mathrm M}^{1/3}\approx6\cdot10^{-6}$ for the central one, each times the order of magnitude of $x$ if $|x|$ is larger than $1$.

:::abbildung ml/k3vkurve 20
The error of the two difference quotients for $f(x)=x^3$ at the point $2$, computed in double precision, against the step size $h$ from $10^{-15}$ to $10^{-1}$, both axes logarithmic. On the right, the truncation error dominates (slope $1$ or $2$), on the left the rounding error (slope $-1$). The dashed curves are the estimates [(11.5)](#gl-11-5); the lowest points lie at $h\approx10^{-8}$ (forward) and $h\approx3\cdot10^{-6}$ (central).
:::

::::beispiel [Worked example]
For $f(x)=x^3$ at the point $2$, $|f|=8$, $|f''|=12$ and $|f'''|=6$. The best step size of the forward difference is $h_+=\sqrt{2\cdot2.2\cdot10^{-16}\cdot8/12}\approx1.7\cdot10^{-8}$, with an error of about $\sqrt{2\cdot2.2\cdot10^{-16}\cdot8\cdot12}\approx2.1\cdot10^{-7}$; relative to $f'(2)=12$, that is about eight correct digits. The best step size of the central difference is $h_0=(1.5\cdot2.2\cdot10^{-16}\cdot8/6)^{1/3}\approx7.6\cdot10^{-6}$, with an error of about $(7.6\cdot10^{-6})^2+2.2\cdot10^{-16}\cdot8/(2\cdot7.6\cdot10^{-6})\approx1.7\cdot10^{-10}$, about eleven correct digits. Fig. [20](#abb-20) confirms both: the measured errors were $7.3\cdot10^{-8}$ at $h=10^{-8}$ and $2.0\cdot10^{-11}$ at $h\approx3.2\cdot10^{-6}$. With $h=10^{-14}$, by contrast, even the first decimal place is wrong for both quotients.
::::

⁠**In short:** Too large an $h$ gives truncation errors, too small a one gives rounding errors; the best choice is $h\approx10^{-8}$ for the forward difference and $h\approx10^{-5}$ to $10^{-6}$ for the central one, and the central difference then reaches about eleven instead of eight correct digits.

### The gradient check

<span class="anker" id="stufe-11-5"></span>

If you derive a gradient by hand or program it as backward steps, it is easy to make mistakes: a forgotten path, a missing transpose, a wrong factor. A difference quotient needs no derivation; it only evaluates the function. Comparing the two finds such mistakes reliably.

:::definition Definition 11.5 (Gradient check)
<span class="anker" id="satz-11-5"></span>

In a __gradient check__, you compare a computed gradient $\mathbf{g}_{\mathrm a}$ at a point $\mathbf{x}$ with the numerical gradient $\mathbf{g}_{\mathrm n}$, whose components are central differences,

<span class="anker" id="gl-11-6"></span>
$$g_{\mathrm n,j}=\frac{f(\mathbf{x}+h\,\mathbf{e}_j)-f(\mathbf{x}-h\,\mathbf{e}_j)}{2h}. \tag{11.6}$$

For each component, you compute the __relative error__

<span class="anker" id="gl-11-7"></span>
$$\rho_j=\frac{|g_{\mathrm a,j}-g_{\mathrm n,j}|}{\max\bigl(|g_{\mathrm a,j}|,\,|g_{\mathrm n,j}|\bigr)}, \tag{11.7}$$

where you set $\rho_j=0$ if both values are zero.
:::

You compare relatively because an absolute error of $10^{-6}$ is excellent for a derivative of $10^{6}$ but a complete failure for a derivative of $10^{-6}$. With calculations in double precision and $h$ of the order of $10^{-5}$, these empirical values apply: a relative error above $10^{-2}$ almost certainly means a mistake in the formula. Between $10^{-2}$ and $10^{-4}$, the result is suspicious. Below $10^{-4}$, it is usually fine for functions with kinks, and $10^{-7}$ or less is a good result. A check costs $2n$ evaluations of $f$; you therefore check only at a few points or only some components. Reverse mode is there for the actual calculation, the difference quotient for checking it.

::::beispiel [Worked example 1]
For $f(\mathbf{x})=x_1^2x_2+x_2^2$, suppose someone derived the gradient $(2x_1x_2,\ x_1^2+x_2)^{\top}$, with a forgotten factor $2$. At the point $(1,\,2)$, this is $\mathbf{g}_{\mathrm a}=(4,\,3)^{\top}$. With $h=0.001$,

$$\begin{aligned} g_{\mathrm n,1}&=\frac{f(1.001,\ 2)-f(0.999,\ 2)}{0.002}=\frac{6.004002-5.996002}{0.002}=4,\\ g_{\mathrm n,2}&=\frac{f(1,\ 2.001)-f(1,\ 1.999)}{0.002}=\frac{6.005001-5.995001}{0.002}=5 . \end{aligned}$$

Here the central differences are exact because $f$ is at most quadratic in each single variable. The relative errors are $\rho_1=0$ and $\rho_2=|3-5|/5=0.4$: the second component is wrong.
::::

::::beispiel [Worked example 2]
The formula to be checked is $\sigma'(x)=\sigma(x)(1-\sigma(x))$ at the point $1$. To ten decimal places, $\sigma(1)\approx0.7310585786$, and the formula gives $0.7310585786\cdot0.2689414214\approx0.1966119332$. With $h=0.01$, $\sigma(1.01)\approx0.7330201492$ and $\sigma(0.99)\approx0.7290879223$, so

$$g_{\mathrm n}=\frac{0.7330201492-0.7290879223}{0.02}=\frac{0.0039322269}{0.02}\approx0.196611345 .$$

The relative error is $\rho\approx5.9\cdot10^{-7}/0.1966\approx3.0\cdot10^{-6}$. It comes from the truncation error of the comparatively large step size and is far below the threshold $10^{-2}$; the formula is correct. In double precision with $h=10^{-5}$, it drops to about $10^{-11}$.
::::

⁠**In short:** The gradient check compares a computed gradient componentwise with central differences; relative errors above $10^{-2}$ indicate a mistake in the formula, those below $10^{-7}$ a correct formula.

### Kinks and other pitfalls

<span class="anker" id="stufe-11-6"></span>

A gradient check can sound the alarm although the formula is correct, or stay silent although it is wrong. The most common causes can be foreseen.

The first cause is kinks. At a kink, as with $|x|$ or $\max(x,\,0)$ at the point $0$, there is no derivative. If a kink lies between $x-h$ and $x+h$, the central difference measures a mixture of the two slopes on the left and on the right, while the computed derivative knows only one of them. The second cause is too low a precision. In single precision, $\varepsilon_{\mathrm M}\approx1.2\cdot10^{-7}$; by [(11.5)](#gl-11-5), the best step size of the central difference is then about $10^{-2}$, and relative errors around $10^{-5}$ to $10^{-3}$ are normal even with a correct formula. The third is too small a step size, which drives up the rounding error. The fourth is very small gradients: if both values are almost zero, the relative error says little, and you also look at the absolute error. Finally, you should check at a random point, not at a special one: at the point $\mathbf{x}=\mathbf{0}$, many terms of a formula vanish, and with them the mistakes hidden in these terms.

:::warnung Only what you check is checked
A passed gradient check at one point shows that the formula is correct there, not everywhere. A forgotten term that is zero at the checked point goes unnoticed. So check at several points with irregular numbers, and check all components that are computed differently.
:::

::::beispiel [Worked example]
For $f(x)=|x|$ at the point $x=10^{-6}$, the derivative is $1$. With $h=10^{-5}$, the kink at $0$ lies between $x-h$ and $x+h$, and

$$D_0f(10^{-6})=\frac{|1.1\cdot10^{-5}|-|-0.9\cdot10^{-5}|}{2\cdot10^{-5}}=\frac{0.2\cdot10^{-5}}{2\cdot10^{-5}}=0.1 .$$

The relative error is $0.9$, although the formula $f'(x)=1$ for $x>0$ is correct. With $h=10^{-7}$, the kink lies outside, and the central difference is exactly $1$.
::::

⁠**In short:** Kinks, single precision, too small step sizes and gradients close to zero distort the check; you check at several irregular points.

:::aufgabe Exercise 39 ★ Two difference quotients
<span class="anker" id="aufg-39"></span>

Let $f(x)=\mathrm{e}^x$ and $x=0$, so $f'(0)=1$.

<ol class="al">

<li>

Use a calculator to compute $D_+f(0)$ and $D_0f(0)$ for $h=0.1$ and $h=0.01$.

</li>

<li>

Compare the errors with the approximations $\tfrac12f''(0)\,h$ and $\tfrac16f'''(0)\,h^2$.

</li>

</ol>

:::loesung
(a) With $\mathrm{e}^{0.1}\approx1.105170918$, $\mathrm{e}^{-0.1}\approx0.904837418$, $\mathrm{e}^{0.01}\approx1.010050167$ and $\mathrm{e}^{-0.01}\approx0.990049834$:

$$\begin{aligned} h=0.1:&\quad D_+=\frac{1.105170918-1}{0.1}\approx1.05171,\\ &\quad D_0=\frac{1.105170918-0.904837418}{0.2}\approx1.001668;\\ h=0.01:&\quad D_+=\frac{1.010050167-1}{0.01}\approx1.005017,\\ &\quad D_0=\frac{1.010050167-0.990049834}{0.02}\approx1.0000167 . \end{aligned}$$

(b) The errors of the forward difference are $0.0517$ and $0.0050$; the approximation $\tfrac12h$ predicts $0.05$ and $0.005$. The errors of the central difference are $0.00167$ and $0.0000167$; the approximation $\tfrac16h^2$ predicts $0.00167$ and $0.0000167$. A ten times smaller $h$ makes the one error ten times smaller and the other a hundred times smaller.
:::
:::

:::aufgabe Exercise 40 ★★ A gradient check
<span class="anker" id="aufg-40"></span>

For $f(\mathbf{x})=x_1\,\mathrm{e}^{x_2}$, someone claims that $\nabla f(\mathbf{x})=(\mathrm{e}^{x_2},\ \mathrm{e}^{x_2})^{\top}$.

<ol class="al">

<li>

At the point $(2,\,0)$, compute the numerical gradient with $h=0.01$ and the relative errors of both components. Which component is wrong?

</li>

<li>

Why would the check at the point $(1,\,0)$ have been unsuitable?

</li>

</ol>

:::loesung
(a) With respect to $x_1$: $\frac{f(2.01,\,0)-f(1.99,\,0)}{0.02}=\frac{2.01-1.99}{0.02}=1$; the claim says $\mathrm{e}^0=1$, so $\rho_1=0$. With respect to $x_2$:

$$g_{\mathrm n,2}=\frac{2\,\mathrm{e}^{0.01}-2\,\mathrm{e}^{-0.01}}{0.02}\approx\frac{2.0201003-1.9800997}{0.02}\approx2.0000333 .$$

The claim says $1$, so $\rho_2=|1-2.0000333|/2.0000333\approx0.5$. The second component is wrong; the correct value is $x_1\mathrm{e}^{x_2}=2$.

(b) At the point $(1,\,0)$, $x_1\mathrm{e}^{x_2}=1=\mathrm{e}^{x_2}$: there the wrong formula happens to agree with the correct one, and the check would have given only a relative error of about $2\cdot10^{-5}$, caused by the truncation error. The mistake would have gone undetected.
:::
:::

:::aufgabe Exercise 41 ★★ The best step size
<span class="anker" id="aufg-41"></span>

Let $f(x)=\mathrm{e}^x$ at the point $1$, so $f=f''=f'''=\mathrm{e}$.

<ol class="al">

<li>

Compute $h_+$, $h_0$ and the corresponding smallest errors by [(11.5)](#gl-11-5) for double precision.

</li>

<li>

Repeat the calculation for single precision. How many correct digits can you then expect at most?

</li>

</ol>

:::loesung
(a) With $|f|=|f''|=|f'''|=\mathrm{e}$ and $\varepsilon_{\mathrm M}\approx2.22\cdot10^{-16}$:

$$\begin{aligned} h_+&=\sqrt{2\varepsilon_{\mathrm M}}\approx2.1\cdot10^{-8}, & E_+(h_+)&=\mathrm{e}\sqrt{2\varepsilon_{\mathrm M}}\approx5.7\cdot10^{-8},\\ h_0&=(1.5\,\varepsilon_{\mathrm M})^{1/3}\approx6.9\cdot10^{-6}, & E_0(h_0)&=\tfrac{\mathrm{e}}6h_0^2+\frac{\varepsilon_{\mathrm M}\mathrm{e}}{2h_0}\approx6.5\cdot10^{-11}. \end{aligned}$$

Relative to $f'(1)=\mathrm{e}$, these are relative errors of about $2\cdot10^{-8}$ and $2\cdot10^{-11}$, that is, just under eight and just under eleven correct digits.

(b) With $\varepsilon_{\mathrm M}\approx1.19\cdot10^{-7}$, we get $h_+\approx4.9\cdot10^{-4}$ with $E_+\approx1.3\cdot10^{-3}$, and $h_0\approx5.6\cdot10^{-3}$ with $E_0\approx4.3\cdot10^{-5}$. Relative to $\mathrm{e}$, these are about $5\cdot10^{-4}$ and $1.6\cdot10^{-5}$: you can expect at most about three and five correct digits, respectively. A gradient check in single precision therefore yields relative errors around $10^{-5}$ to $10^{-3}$ even with a correct formula.
:::
:::

:::aufgabe Exercise 42 ★★★ A kink in the graph
<span class="anker" id="aufg-42"></span>

Let $f(\mathbf{x})=\max(x_1,\,x_2)\cdot x_3$.

<ol class="al">

<li>

Compute the gradient in reverse mode at the point $(2,\ 2.000001,\ 3)$.

</li>

<li>

Compute the central difference with respect to $x_1$ with $h=10^{-5}$ and the relative error. Is the formula wrong?

</li>

<li>

What does reverse mode yield at the point $(2,\,2,\,3)$, and why is there no gradient there?

</li>

</ol>

:::loesung
(a) At the point $(2,\ 2.000001,\ 3)$, $v=\max(x_1,x_2)=x_2=2.000001$ and $f=6.000003$. Backward: $\bar f=1$, $\bar v=x_3=3$, $\bar x_3=v=2.000001$; the maximum passes $\bar v$ on to the larger input $x_2$, so $\bar x_2=3$ and $\bar x_1=0$. The gradient is $(0,\ 3,\ 2.000001)^{\top}$.

(b) $f(2.00001,\ 2.000001,\ 3)=3\cdot2.00001=6.00003$ and $f(1.99999,\ 2.000001,\ 3)=3\cdot2.000001=6.000003$, so

$$g_{\mathrm n,1}=\frac{6.00003-6.000003}{0.00002}=\frac{0.000027}{0.00002}=1.35$$

and $\rho_1=|0-1.35|/1.35=1$. Nevertheless, the formula is correct. The kink at $x_1=x_2$ lies between $x_1-h$ and $x_1+h$: to the right of it, $f$ rises with slope $3$ in $x_1$; to the left of it, not at all, and the central difference mixes both.

(c) At the point $(2,\,2,\,3)$, both inputs of the maximum are equal. Reverse mode passes $\bar v=3$ to one of the two, depending on which one the calculation treats as larger in case of a tie; so it yields $(3,\,0,\,2)^{\top}$ or $(0,\,3,\,2)^{\top}$. There is no gradient there: if you increase $x_1$, $f$ rises with slope $3$; if you decrease $x_1$, $f$ stays the same. The one-sided slopes are different, as for $|x|$ at the point $0$.
:::
:::
