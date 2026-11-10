---
title: The chain rule
pfad: Computer Science / Machine Learning / Mathematical Foundations / Derivative, Gradient and Chain Rule
adresse: informatik/machine-learning/mathematische-grundlagen/ableitung-gradient-und-kettenregel
knoten: Chapter 3: Derivative, Gradient and Chain Rule
nachschlagen: ja
order: 15230300
summary: Many functions arise by substituting one function into another.
tags: composition, logistic function
lang: en
---

<span class="anker" id="stufe-2"></span>

:::zweck
Many functions arise by substituting one function into another. The chain rule says how the derivative of such a composition follows from the derivatives of the parts: the factors of the individual stages are multiplied. This holds for chains with any number of links. At the end comes the logistic function, whose derivative can be expressed in terms of the function itself.
:::

### Composition

<span class="anker" id="stufe-2-1"></span>

You compute the function $(3x+1)^2$ in two steps: first $u=3x+1$, then $u^2$. Many formulas are built like this, as simple steps carried out one after another. If you recognize this construction, you can assemble the derivative from the derivatives of the steps.

:::definition Definition 2.1 (Composition)
<span class="anker" id="satz-2-1"></span>

If $g$ and $f$ are functions and every value $g(x)$ lies where $f$ is defined, then the function

$$(f\circ g)(x)=f\bigl(g(x)\bigr)$$

is called the __composition__ of $f$ and $g$, read “$f$ after $g$”. The function $g$, which is applied first, is called the inner function; $f$ is called the outer function.
:::

::::beispiel [Worked example]
For $F(x)=(3x+1)^2$, the inner function is $g(x)=3x+1$ and the outer one is $f(u)=u^2$, so $F=f\circ g$. At the point $1$, $g(1)=4$ and $F(1)=f(4)=16$. The order matters: $(g\circ f)(x)=g(f(x))=3x^2+1$ is a different function, with the value $4$ at the point $1$.
::::

⁠**In short:** A composition $f\circ g$ applies first $g$ and then $f$; the order cannot be swapped.

### The chain rule

<span class="anker" id="stufe-2-2"></span>

How does $F=f\circ g$ respond to a small change in $x$? You follow the change through the two stages. By the linear approximation, the first stage passes on a small change $\Delta x$ as approximately $\Delta u\approx g'(x)\,\Delta x$. The second stage passes on this change as $\Delta y\approx f'(u)\,\Delta u$. Combined, $\Delta y\approx f'(u)\,g'(x)\,\Delta x$. As in a gear train with two gear stages, the factors of the stages multiply (Fig. [4](#abb-4)).

:::abbildung ml/k3getriebe 4
The chain rule as a gear train for $y=(3x+1)^2$ at the point $1$. All three number lines have the same scale. The first stage stretches the piece $\Delta x=0.01$ (blue) to three times its length, $\Delta u=0.03$ (orange), and the second stage stretches that to about eight times its length, $\Delta y=0.2409\approx0.24$ (red).
:::

:::satz Theorem 2.2 (Chain rule)
<span class="anker" id="satz-2-2"></span>

If $g$ is differentiable at the point $x$ and $f$ is differentiable at the point $g(x)$, then $f\circ g$ is differentiable at the point $x$, and

<span class="anker" id="gl-2-1"></span>
$$(f\circ g)'(x)=f'\bigl(g(x)\bigr)\cdot g'(x). \tag{2.1}$$
:::

What matters is where the derivatives are evaluated: $g'$ at the point $x$, but $f'$ at the point $u=g(x)$, that is, where the outer function actually operates. With $u=g(x)$ and $y=f(u)$, the rule is often written as $\frac{\mathrm{d} y}{\mathrm{d} x}=\frac{\mathrm{d} y}{\mathrm{d} u}\cdot\frac{\mathrm{d} u}{\mathrm{d} x}$. This looks as if $\mathrm{d} u$ cancels out. As a mnemonic this is useful, as a justification it is not, because the symbols are not fractions but limits.

:::beweis Chain rule
Let $u=g(x)$. By the linear approximation [(1.4)](die-ableitung.html#gl-1-4), $g(x+h)=u+g'(x)\,h+r_g(h)$ with $r_g(h)/h\to0$, and $f(u+k)=f(u)+f'(u)\,k+r_f(k)$ with $r_f(k)/k\to0$; here let $r_f(0)=0$. Set $k=g(x+h)-u=g'(x)\,h+r_g(h)$. Then

$$f\bigl(g(x+h)\bigr)-f(u)=f'(u)\,k+r_f(k)=f'(u)\,g'(x)\,h+f'(u)\,r_g(h)+r_f(k).$$

After dividing by $h$, the middle term tends to $0$. For the last one, write $r_f(k)/h=\bigl(r_f(k)/k\bigr)\cdot(k/h)$ as long as $k\ne0$; the first factor tends to $0$ because $k$ tends to $0$ along with $h$, and the second tends to $g'(x)$. If $k=0$, the term is $0$ anyway. What remains is $f'(u)\,g'(x)$.
:::

::::beispiel [Worked example]
For $F(x)=(3x+1)^2$, $g'(x)=3$ and $f'(u)=2u$. At the point $1$, $u=g(1)=4$, so

$$F'(1)=f'(4)\cdot g'(1)=8\cdot3=24 .$$

Check: multiplied out, $F(x)=9x^2+6x+1$, so $F'(x)=18x+6$ and $F'(1)=24$. Fig. [4](#abb-4) shows the same thing with numbers: $F(1.01)=4.03^2=16.2409$, and the linear approximation predicts $16+24\cdot0.01=16.24$.
::::

⁠**In short:** In a composition, the derivatives of the stages multiply, each evaluated at the point where its stage operates: $(f\circ g)'(x)=f'(g(x))\,g'(x)$.

### Chains with many links

<span class="anker" id="stufe-2-3"></span>

Most calculations consist of more than two steps. The chain rule can be applied repeatedly: with three stages, $f_3\circ f_2\circ f_1=f_3\circ(f_2\circ f_1)$, and applying [(2.1)](#gl-2-1) twice gives a product of three factors. The same holds for any number of stages.

:::satz Theorem 2.3 (Chain rule for many links)
<span class="anker" id="satz-2-3"></span>

Let $u_0=x$ and $u_k=f_k(u_{k-1})$ for $k=1,\dots,L$, and let each function $f_k$ be differentiable at the point $u_{k-1}$. Then

<span class="anker" id="gl-2-2"></span>
$$\frac{\mathrm{d} u_L}{\mathrm{d} x}=f_L'(u_{L-1})\cdot f_{L-1}'(u_{L-2})\cdots f_1'(u_0). \tag{2.2}$$
:::

For the calculation, this implies an order. Each factor needs the value at which its stage operates. You therefore first compute the intermediate values $u_1,u_2,\dots$, as in the ordinary evaluation, and only then the factors. In which order you then multiply the factors does not matter for numbers.

::::beispiel [Worked example]
Let $y=\dfrac1{(x^2+1)^3}$ at the point $x=1$. The chain has three links:

$$u_1=x^2+1=2,\qquad u_2=u_1^3=8,\qquad y=\frac1{u_2}=\frac18 .$$

The factors are $\frac{\mathrm{d} u_1}{\mathrm{d} x}=2x=2$, $\frac{\mathrm{d} u_2}{\mathrm{d} u_1}=3u_1^2=12$ and $\frac{\mathrm{d} y}{\mathrm{d} u_2}=-\frac1{u_2^2}=-\frac1{64}$, so

$$\frac{\mathrm{d} y}{\mathrm{d} x}=2\cdot12\cdot\Bigl(-\frac1{64}\Bigr)=-\frac{24}{64}=-0.375 .$$

Check: by the power rule and the chain rule, $y=(x^2+1)^{-3}$ has the derivative $-3\,(x^2+1)^{-4}\cdot2x$, which at the point $1$ is $-6/16=-0.375$.
::::

⁠**In short:** In a long chain, the derivative is the product of the derivatives of all links; you first compute the intermediate values, then the factors.

### The logistic function

<span class="anker" id="stufe-2-4"></span>

Some quantities should lie smoothly between two bounds, for example a proportion between $0$ and $1$. A function that maps every real number into this range, without a jump, without a kink and always increasing, is the logistic function. It also describes growth with saturation: a quantity first grows almost exponentially and then approaches an upper limit. Its derivative is a nice example of the chain rule and has a remarkable form.

:::definition Definition 2.4 (Logistic function)
<span class="anker" id="satz-2-4"></span>

The function

<span class="anker" id="gl-2-3"></span>
$$\sigma(x)=\frac1{1+\mathrm{e}^{-x}} \tag{2.3}$$

is called the __logistic function__.
:::

For large positive $x$, $\mathrm{e}^{-x}$ is almost $0$ and $\sigma(x)$ almost $1$. For large negative $x$, $\mathrm{e}^{-x}$ is huge and $\sigma(x)$ almost $0$. At the point $0$, $\sigma(0)=\tfrac12$. Moreover, $\sigma(-x)=1-\sigma(x)$, because $\frac1{1+\mathrm{e}^{x}}=\frac{\mathrm{e}^{-x}}{\mathrm{e}^{-x}+1}=1-\frac1{1+\mathrm{e}^{-x}}$; the graph is therefore symmetric about the point $(0,\,\tfrac12)$ (Fig. [5](#abb-5)).

:::satz Theorem 2.5 (Derivative of the logistic function)
<span class="anker" id="satz-2-5"></span>

The following holds:

<span class="anker" id="gl-2-4"></span>
$$\sigma'(x)=\sigma(x)\,\bigl(1-\sigma(x)\bigr). \tag{2.4}$$

The derivative is positive everywhere and at most $\tfrac14$; it takes its largest value $\tfrac14$ at the point $0$.
:::

:::herleitung The derivative of the logistic function
The function is a chain with three links: $u_1=-x$, $u_2=1+\mathrm{e}^{u_1}$, $\sigma=1/u_2$. The factors are $-1$, $\mathrm{e}^{u_1}=\mathrm{e}^{-x}$ and $-1/u_2^2$. By [(2.2)](#gl-2-2),

$$\sigma'(x)=-\frac1{(1+\mathrm{e}^{-x})^2}\cdot\mathrm{e}^{-x}\cdot(-1)=\frac{\mathrm{e}^{-x}}{(1+\mathrm{e}^{-x})^2}=\frac1{1+\mathrm{e}^{-x}}\cdot\frac{\mathrm{e}^{-x}}{1+\mathrm{e}^{-x}} .$$

The first factor is $\sigma(x)$. The second is $\frac{(1+\mathrm{e}^{-x})-1}{1+\mathrm{e}^{-x}}=1-\sigma(x)$. Because $\sigma(x)$ lies between $0$ and $1$, both factors are positive. For a number $p$ between $0$ and $1$, $p\,(1-p)=\tfrac14-(p-\tfrac12)^2\le\tfrac14$, with equality exactly for $p=\tfrac12$, that is, for $x=0$.
:::

:::abbildung ml/k3logistisch 5
The logistic function $\sigma$ (blue) rises from $0$ to $1$, most steeply at the point $0$. Its derivative (red) takes its largest value $\tfrac14$ there and quickly becomes small on both sides. Marked are the values at the points $0$ and $2$ from the worked example.
:::

::::beispiel [Worked example]
At the point $2$, $\mathrm{e}^{-2}\approx0.1353$, so $\sigma(2)\approx1/1.1353\approx0.8808$ and

$$\sigma'(2)=\sigma(2)\,\bigl(1-\sigma(2)\bigr)\approx0.8808\cdot0.1192\approx0.1050 .$$

Once $\sigma(2)$ has been computed, the derivative costs only one subtraction and one multiplication, and no further exponential function. At the point $10$, $\sigma(10)\approx0.99995$ and $\sigma'(10)\approx0.0000454$: far out, the function is almost horizontal, and small changes of the input barely arrive at the output.
::::

⁠**In short:** The logistic function $\sigma(x)=1/(1+\mathrm{e}^{-x})$ maps every number smoothly into the interval between $0$ and $1$; its derivative is $\sigma(1-\sigma)$, at most $\tfrac14$, and can be computed from the function value alone.

:::aufgabe Exercise 5 ★ Bell curve
<span class="anker" id="aufg-5"></span>

Let $f(x)=\mathrm{e}^{-x^2}$.

<ol class="al">

<li>

Determine the inner and the outer function and compute $f'(x)$.

</li>

<li>

Compute $f'(0)$, $f'(1)$ and $f'(-1)$ and interpret the signs on the graph.

</li>

</ol>

:::loesung
(a) The inner function is $u=-x^2$ with $u'=-2x$, the outer one is $\mathrm{e}^u$ with the derivative $\mathrm{e}^u$. By the chain rule, $f'(x)=\mathrm{e}^{-x^2}\cdot(-2x)=-2x\,\mathrm{e}^{-x^2}$.

(b) $f'(0)=0$: the graph has a horizontal tangent line at the point $0$; its peak is there. $f'(1)=-2/\mathrm{e}\approx-0.7358$: to the right of the peak, it falls. $f'(-1)=2/\mathrm{e}\approx0.7358$: to the left of the peak, it rises. Because $f(-x)=f(x)$, the slopes at the points $\pm1$ are equal in magnitude and opposite in sign.
:::
:::

:::aufgabe Exercise 6 ★★ A chain with three links
<span class="anker" id="aufg-6"></span>

Let $y=\sqrt{1+x^4}$.

<ol class="al">

<li>

Decompose the function into three links $u_1$, $u_2$, $y$, and at the point $x=1$ compute first all intermediate values, then all factors.

</li>

<li>

Compute $\frac{\mathrm{d} y}{\mathrm{d} x}$ at the point $1$ as the product of the factors, and check it with the chain rule in a single step.

</li>

</ol>

:::loesung
(a) The links are $u_1=x^4$, $u_2=1+u_1$ and $y=\sqrt{u_2}$. At the point $1$, the intermediate values are $u_1=1$, $u_2=2$ and $y=\sqrt2\approx1.4142$. The factors are $\frac{\mathrm{d} u_1}{\mathrm{d} x}=4x^3=4$, $\frac{\mathrm{d} u_2}{\mathrm{d} u_1}=1$ and $\frac{\mathrm{d} y}{\mathrm{d} u_2}=\frac1{2\sqrt{u_2}}=\frac1{2\sqrt2}\approx0.3536$.

(b) The product is $4\cdot1\cdot\frac1{2\sqrt2}=\frac2{\sqrt2}=\sqrt2\approx1.4142$. In a single step: $y'=\frac1{2\sqrt{1+x^4}}\cdot4x^3$, so at the point $1$ it is $\frac4{2\sqrt2}=\sqrt2$.
:::
:::

:::aufgabe Exercise 7 ★★ Properties of the logistic function
<span class="anker" id="aufg-7"></span>

<ol class="al">

<li>

Use [(2.4)](#gl-2-4) and $\sigma(-x)=1-\sigma(x)$ to show that $\sigma'(-x)=\sigma'(x)$. What does this mean for the graph of $\sigma'$?

</li>

<li>

Compute $\sigma(1)$ and $\sigma'(1)$ to four decimal places.

</li>

<li>

Compute the second derivative $\sigma''$, expressed in terms of $\sigma$, and determine its sign for $x>0$ and for $x<0$. What does this say about the curvature of the graph of $\sigma$?

</li>

</ol>

:::loesung
(a) With $\sigma(-x)=1-\sigma(x)$, we get $\sigma'(-x)=\sigma(-x)\,\bigl(1-\sigma(-x)\bigr)=\bigl(1-\sigma(x)\bigr)\,\sigma(x)=\sigma'(x)$. The graph of $\sigma'$ is symmetric about the vertical axis, as Fig. [5](#abb-5) shows.

(b) $\mathrm{e}^{-1}\approx0.3679$, so $\sigma(1)=1/1.3679\approx0.7311$ and $\sigma'(1)\approx0.7311\cdot0.2689\approx0.1966$.

(c) With the product rule and the chain rule: $\sigma''=(\sigma-\sigma^2)'=\sigma'-2\sigma\sigma'=\sigma'\,(1-2\sigma)=\sigma(1-\sigma)(1-2\sigma)$. For $x>0$, $\sigma>\tfrac12$, so $1-2\sigma<0$ and $\sigma''<0$: the graph bends downward there. For $x<0$, $\sigma''>0$, and it bends upward. At the point $0$, the curvature changes its sign; the slope is largest there.
:::
:::

:::aufgabe Exercise 8 ★★★ The derivative of an inverse function
<span class="anker" id="aufg-8"></span>

For $x>0$, $\mathrm{e}^{\ln x}=x$.

<ol class="al">

<li>

Differentiate both sides with respect to $x$ using the chain rule and conclude that $(\ln x)'=1/x$, assuming that $\ln$ is differentiable.

</li>

<li>

Proceed in the same way with $(\sqrt x)^2=x$ and compare with the power rule.

</li>

<li>

The inverse function of the logistic function is $\ell(p)=\ln\frac{p}{1-p}$ for $0<p<1$. Check that $\ell(\sigma(x))=x$, and compute $\ell'(p)$ once directly and once via $\sigma'$.

</li>

</ol>

:::loesung
(a) The left-hand side is a composition with the inner function $\ln x$ and the outer function $\mathrm{e}^u$. By the chain rule, its derivative is $\mathrm{e}^{\ln x}\cdot(\ln x)'=x\cdot(\ln x)'$. The right-hand side has the derivative $1$. So $x\,(\ln x)'=1$ and $(\ln x)'=1/x$.

(b) From $(\sqrt x)^2=x$ it follows that $2\sqrt x\cdot(\sqrt x)'=1$, so $(\sqrt x)'=\frac1{2\sqrt x}=\tfrac12x^{-1/2}$, exactly the power rule with $n=\tfrac12$.

(c) We have $1-\sigma(x)=\frac{\mathrm{e}^{-x}}{1+\mathrm{e}^{-x}}$, so $\frac{\sigma(x)}{1-\sigma(x)}=\frac1{\mathrm{e}^{-x}}=\mathrm{e}^x$ and $\ell(\sigma(x))=\ln\mathrm{e}^x=x$. Directly, $\ell(p)=\ln p-\ln(1-p)$ and

$$\ell'(p)=\frac1p+\frac1{1-p}=\frac{1}{p\,(1-p)} .$$

Via $\sigma'$: differentiating $\ell(\sigma(x))=x$ gives $\ell'(\sigma(x))\cdot\sigma'(x)=1$, so $\ell'(p)=\frac1{\sigma'(x)}=\frac1{p(1-p)}$ with $p=\sigma(x)$. Where $\sigma$ is flat, its inverse function is steep.
:::
:::
