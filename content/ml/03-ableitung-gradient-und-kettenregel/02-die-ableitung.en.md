---
title: The derivative
pfad: Computer Science / Machine Learning / Mathematical Foundations / Derivative, Gradient and Chain Rule
adresse: informatik/machine-learning/mathematische-grundlagen/ableitung-gradient-und-kettenregel
knoten: Chapter 3: Derivative, Gradient and Chain Rule
nachschlagen: ja
order: 15230200
summary: The derivative measures how strongly a function of one variable responds to a small change in its input.
tags: secant line, difference quotient, limit, differentiable, derivative, tangent line, kink, linear approximation
lang: en
---

<span class="anker" id="stufe-1"></span>

:::zweck
The derivative measures how strongly a function of one variable responds to a small change in its input. This section introduces it as a limit of slopes, interprets it as the slope of the line that hugs the curve most closely, and provides the rules with which you compute derivatives without forming a limit every time. At the end comes the second derivative, which describes how the slope itself changes.
:::

### Rate of change and difference quotient

<span class="anker" id="stufe-1-1"></span>

A function $f$ assigns a number $f(x)$ to every number $x$. If you increase $x$ by a small amount $h$, the value usually changes too, namely by $f(x+h)-f(x)$. Whether that is a lot or a little only becomes clear by comparison with $h$: a change in value of $0.1$ is large if $x$ has grown by only $0.001$, and small if $x$ has grown by $100$. You therefore divide the one change by the other.

In the picture of the graph, this is a slope. You draw a line through the two points $(x,\,f(x))$ and $(x+h,\,f(x+h))$ of the graph. Such a line through two points of a curve is called a __secant line__. Its slope is the difference in height between the two points divided by their horizontal distance. It indicates how steeply the graph rises on average between the two points.

:::definition Definition 1.1 (Difference quotient)
<span class="anker" id="satz-1-1"></span>

For a function $f$, a point $x$ and a number $h\ne0$,

<span class="anker" id="gl-1-1"></span>
$$\frac{f(x+h)-f(x)}{h} \tag{1.1}$$

is called the __difference quotient__ of $f$ at the point $x$ with step size $h$. It is the slope of the secant line through $(x,\,f(x))$ and $(x+h,\,f(x+h))$.
:::

The step size $h$ may also be negative; then the second point lies to the left of $x$. For $h=0$ the quotient is not defined, because you cannot divide by zero.

::::beispiel [Worked example]
Let $f(x)=x^3$ and $x=2$, so $f(2)=8$. For three step sizes,

$$\frac{3^3-8}{1}=19,\qquad \frac{2.5^3-8}{0.5}=\frac{15.625-8}{0.5}=15.25,\qquad \frac{2.1^3-8}{0.1}=\frac{9.261-8}{0.1}=12.61 .$$

The secant lines become flatter the closer the second point moves to $(2,\,8)$ (Fig. [1](#abb-1)). For an arbitrary $h$ you calculate with $(2+h)^3=8+12h+6h^2+h^3$:

<span class="anker" id="gl-1-2"></span>
$$\frac{(2+h)^3-8}{h}=\frac{12h+6h^2+h^3}{h}=12+6h+h^2 . \tag{1.2}$$

With $h=1$, $h=0.5$ and $h=0.1$ this formula again gives $19$, $15.25$ and $12.61$. With $h=0.01$ it gives $12.0601$, with $h=-0.1$ it gives $12-0.6+0.01=11.41$.

:::abbildung ml/k3sekante 1
Secant lines of the graph of $f(x)=x^3$ through the point $(2,\,8)$, with the slopes $19$ for $h=1$ (red) and $15.25$ for $h=0.5$ (orange). With a smaller step size $h$ the second point moves closer, the secant line becomes flatter, and its slope $12+6h+h^2$ approaches the slope $12$ of the tangent line (dashed).
:::
::::

⁠**In short:** The difference quotient is the change in the function value divided by the change in the input, the average slope between two points of the graph.

### The derivative

<span class="anker" id="stufe-1-2"></span>

In the worked example, the slopes of the secant lines lie closer to $12$ the smaller $|h|$ is, and they do so from both sides: $12.61$ for $h=0.1$, $11.41$ for $h=-0.1$. They do not reach the value $12$ itself for any $h\ne0$, but they come arbitrarily close to it. That is why $12$ is called the limit of the secant slopes. In general, a quantity that depends on $h$ has the __limit__ $c$ as $h\to0$ if it lies arbitrarily close to $c$ as soon as $h$ is close enough to $0$ and not equal to $0$. Positive and negative $h$ count equally.

:::definition Definition 1.2 (Derivative)
<span class="anker" id="satz-1-2"></span>

A function $f$ is called __differentiable__ at the point $x$ if the difference quotient has a limit as $h\to0$. This limit

<span class="anker" id="gl-1-3"></span>
$$f'(x)=\lim_{h\to0}\frac{f(x+h)-f(x)}{h} \tag{1.3}$$

is called the __derivative__ of $f$ at the point $x$. It is also written $\frac{\mathrm{d} f}{\mathrm{d} x}(x)$. The line through $(x,\,f(x))$ with the slope $f'(x)$ is called the __tangent line__ to the graph.
:::

If $f$ is differentiable at every point, then $f'$ is again a function: it assigns to every $x$ the slope of the graph at that point. It is called the derivative function or, for short, also the derivative. The notation $\frac{\mathrm{d} f}{\mathrm{d} x}$ is reminiscent of the quotient in [(1.1)](#gl-1-1), but it is not itself a fraction; it is the symbol for the limit.

::::beispiel [Worked example 1]
By [(1.2)](#gl-1-2), the difference quotient of $f(x)=x^3$ at the point $2$ equals $12+6h+h^2$. As $h\to0$, $6h$ and $h^2$ become arbitrarily small, so $f'(2)=12$. The same calculation at an arbitrary point $x$, with $(x+h)^3=x^3+3x^2h+3xh^2+h^3$, gives the quotient $3x^2+3xh+h^2$ and hence $f'(x)=3x^2$.
::::

Not every function is differentiable everywhere. A typical exception is a __kink__: a point at which the graph continues without a jump but has a different slope to its left than to its right. There, the secant slopes with $h>0$ approach the slope on the right, and those with $h<0$ the slope on the left. Because the two differ, there is no common limit and therefore no derivative; no line hugs both sides at once. The best-known example is the absolute value function $|x|$ at the point $0$.

::::beispiel [Worked example 2]
The absolute value function $f(x)=|x|$ has no derivative at the point $0$. Its difference quotient is $|h|/h$, that is, $1$ for every $h>0$ and $-1$ for every $h<0$. There is no number that it approaches from both sides. The graph has a kink at $0$: to the left it has slope $-1$, to the right slope $+1$. At every other point $|x|$ is differentiable, with derivative $1$ for $x>0$ and $-1$ for $x<0$.
::::

⁠**In short:** The derivative $f'(x)$ is the limit of the secant slopes, that is, the slope of the tangent line; at a kink it does not exist.

### The linear approximation

<span class="anker" id="stufe-1-3"></span>

What is the tangent line good for? If you look at a smooth graph through an ever stronger magnifying glass, you see less and less of its curvature. Under strong magnification, only a straight piece of the curve is left, and this piece lies on the tangent line (Fig. [2](#abb-2)). Near the point $x$ you may therefore replace the function by its tangent line. Calculating with a straight line is much easier than with the function itself.

:::abbildung ml/k3lupe 2
The magnifying glass: the graph of $f(x)=x^3$ (blue) and its tangent line $8+12\,(x-2)$ at the point $2$ (red, dashed) in three windows, each ten times narrower than the previous one. In the last window, the curve and the tangent line can no longer be told apart.
:::

:::satz Theorem 1.3 (Linear approximation)
<span class="anker" id="satz-1-3"></span>

If $f$ is differentiable at the point $x$, then

<span class="anker" id="gl-1-4"></span>
$$f(x+h)=f(x)+f'(x)\,h+r(h)\qquad\text{with}\qquad \lim_{h\to0}\frac{r(h)}{h}=0 . \tag{1.4}$$

The expression $f(x)+f'(x)\,h$ is called the __linear approximation__ of $f$ at the point $x$, and $r(h)$ is its error.
:::

:::beweis Linear approximation
Set $r(h)=f(x+h)-f(x)-f'(x)\,h$; then the equation on the left holds by construction. For $h\ne0$,

$$\frac{r(h)}{h}=\frac{f(x+h)-f(x)}{h}-f'(x),$$

and by [(1.3)](#gl-1-3) the first term tends to $f'(x)$, so the difference tends to $0$.
:::

The condition $r(h)/h\to0$ says more than that the error becomes small. After all, $h$ itself also becomes small; what matters is that the error vanishes faster than $h$. If you halve $h$, the change $f'(x)\,h$ becomes half as large, but the error shrinks to well below half. That is the precise meaning of the magnifying glass.

Equation [(1.4)](#gl-1-4) also provides the most intuitive interpretation of the derivative. A small change $h$ of the input arrives at the output as approximately $f'(x)\,h$. So the derivative is the *factor* by which the function passes on small changes, its sensitivity at the point $x$. A large $|f'(x)|$ means that even small changes of the input change the value a lot; a negative $f'(x)$ means that the value falls when the input grows.

::::beispiel [Worked example]
For $f(x)=x^3$ at the point $2$ and $h=0.01$, the linear approximation gives

$$f(2.01)\approx8+12\cdot0.01=8.12 .$$

The exact value is $f(2.01)=2.01^3=8.120601$. The error is $r(0.01)=0.000601$; by the calculation for [(1.2)](#gl-1-2), in general $r(h)=6h^2+h^3$. The quotient $r(h)/h=6h+h^2$ equals $0.0601$ for $h=0.01$ and $0.006001$ for $h=0.001$: it tends to zero, as the theorem requires.
::::

⁠**In short:** Near $x$, $f(x+h)\approx f(x)+f'(x)\,h$; the derivative is the factor by which small changes are passed on, and the error vanishes faster than $h$.

:::hintergrund Why the tangent line in particular is the best line
Every line through the point $(x,\,f(x))$ gives an approximation $f(x+h)\approx f(x)+m\,h$ with some slope $m$. Its error is $f(x+h)-f(x)-m\,h$. Dividing it by $h$ gives the difference quotient minus $m$, and that tends to $f'(x)-m$ as $h\to0$. Only for $m=f'(x)$ is this limit zero. For every other slope, the error ultimately remains about as large as $|f'(x)-m|\cdot|h|$, so it shrinks only as fast as $h$ itself. The tangent line is therefore the only line through the point whose error vanishes faster than $h$. In this sense it is the best linear approximation, and this is exactly how the derivative can also be defined: as the one number $m$ for which $f(x+h)-f(x)-m\,h$ tends to zero faster than $h$. This form of the definition has the advantage that it carries over without change to functions with many inputs, where there is no quotient anymore because you cannot divide by a vector. Section [3](partielle-ableitungen-und-der-gradient.html#stufe-3) makes use of it.
:::

### Differentiation rules

<span class="anker" id="stufe-1-4"></span>

Computing every derivative via the limit is tedious. Fortunately, a few basic derivatives and four rules are enough to differentiate almost any formula built from basic arithmetic operations and familiar functions. Table [1](#tab-1) lists the basic derivatives that this chapter uses.

<span class="anker" id="tab-1"></span>

**Table 1:** Basic derivatives. The power rule holds for every real exponent $n$; for non-integer $n$ only when $x>0$. The angles in $\sin$ and $\cos$ are measured in radians.

| Function $f(x)$ | Derivative $f'(x)$ | Example |
|---|---|---|
| $c$ (constant) | $0$ | $f(x)=7$: $f'(x)=0$ |
| $x^n$ | $n\,x^{n-1}$ | $x^3\mapsto3x^2$, $\ \tfrac1x=x^{-1}\mapsto-\tfrac1{x^2}$, $\ \sqrt x=x^{1/2}\mapsto\tfrac1{2\sqrt x}$ |
| $\mathrm{e}^x$ | $\mathrm{e}^x$ | at the point $0$: slope $1$ |
| $\ln x$ ($x>0$) | $\tfrac1x$ | at the point $1$: slope $1$ |
| $\sin x$ | $\cos x$ | at the point $0$: slope $1$ |
| $\cos x$ | $-\sin x$ | at the point $0$: slope $0$ |

:::satz Theorem 1.4 (Differentiation rules)
<span class="anker" id="satz-1-4"></span>

If $u$ and $v$ are differentiable at the point $x$ and $c$ is a number, then the following hold there:

<span class="anker" id="gl-1-5"></span>
$$\begin{aligned} (u+v)'&=u'+v' &&\text{(sum rule)}\\ (c\,u)'&=c\,u' &&\text{(constant multiple rule)}\\ (u\,v)'&=u'\,v+u\,v' &&\text{(product rule)}\\ \Bigl(\frac uv\Bigr)'&=\frac{u'\,v-u\,v'}{v^2}\quad\text{if }v(x)\ne0 &&\text{(quotient rule)} \end{aligned} \tag{1.5}$$
:::

The first two rules follow immediately from the definition, because difference quotients of sums and multiples split up in the same way. The product rule is less obvious. A picture makes it clear: think of $u\,v$ as the area of a rectangle with sides $u$ and $v$. If the sides grow by $\Delta u$ and $\Delta v$, three strips are added: $u\,\Delta v$, $v\,\Delta u$ and the small corner piece $\Delta u\,\Delta v$. For small changes, the corner piece is a product of two small quantities and vanishes faster than the two strips. What remains is $\Delta(uv)\approx v\,\Delta u+u\,\Delta v$, and dividing by $h$ gives the product rule.

:::beweis Product rule and power rule
With $\Delta u=u(x+h)-u(x)$ and $\Delta v=v(x+h)-v(x)$, exactly

$$u(x+h)\,v(x+h)-u(x)\,v(x)=v(x)\,\Delta u+u(x)\,\Delta v+\Delta u\,\Delta v .$$

After dividing by $h$, $\Delta u/h$ tends to $u'(x)$ and $\Delta v/h$ to $v'(x)$. The last term is $(\Delta u/h)\cdot\Delta v$; its first factor tends to $u'(x)$, its second to $0$, because a differentiable function changes only a little for small $h$. So the whole quotient tends to $u'(x)\,v(x)+u(x)\,v'(x)$.

For the power rule with a natural number $n$, you multiply out $(x+h)^n$. By the binomial theorem,

$$(x+h)^n=x^n+n\,x^{n-1}h+(\text{terms with }h^2,h^3,\dots,h^n),$$

so the difference quotient is $n\,x^{n-1}$ plus terms that still contain at least one $h$. As $h\to0$, $n\,x^{n-1}$ remains. The quotient rule follows from the product rule, applied to $u=(u/v)\cdot v$.
:::

::::beispiel [Worked example]
Let $f(x)=(x^2+1)(x-3)$; we want $f'(2)$. With $u=x^2+1$, $u'=2x$, $v=x-3$, $v'=1$, the product rule gives

$$f'(x)=2x\,(x-3)+(x^2+1)\cdot1,\qquad f'(2)=4\cdot(-1)+5\cdot1=1 .$$

Check: multiplied out, $f(x)=x^3-3x^2+x-3$, so $f'(x)=3x^2-6x+1$ and $f'(2)=12-12+1=1$.
::::

⁠**In short:** With the basic derivatives in the table and the rules for sums, multiples, products and quotients, you differentiate compound formulas without forming a limit.

:::hintergrund Why the exponential function is its own derivative
For every base $a>0$, $a^{x+h}-a^x=a^x\,(a^h-1)$. The difference quotient of $a^x$ is therefore $a^x$ times the difference quotient of $a^x$ at the point $0$, that is, $a^x\cdot\frac{a^h-1}{h}$: the slope at every point is the function value times the slope at the point $0$. For $a=2$ this slope at the point $0$ is about $0.693$, for $a=3$ about $1.099$. In between there is exactly one base for which it is $1$, and this base is Euler's number $\mathrm{e}\approx2.718$. For it, the slope everywhere equals the function value. The derivative of $\ln x$ follows from this, because the logarithm undoes the exponential function: if $y=\ln x$, then $x=\mathrm{e}^y$, and a small change in $y$ changes $x$ by $\mathrm{e}^y=x$ times as much. Conversely, a small change in $x$ therefore changes $y$ by $1/x$ times as much.
:::

### The second derivative and the quadratic approximation

<span class="anker" id="stufe-1-5"></span>

The tangent line gives the direction of the graph, but not how the graph bends away from it. Whether the curve deviates upward or downward from the tangent line, and how strongly, depends on how the slope itself changes. You again measure this change with a derivative, namely with the derivative of the derivative.

:::definition Definition 1.5 (Higher derivatives)
<span class="anker" id="satz-1-5"></span>

If the derivative function $f'$ is differentiable at the point $x$, then $f''(x)=(f')'(x)$ is called the __second derivative__ of $f$ at the point $x$. Correspondingly, $f'''=(f'')'$ is the third derivative, and in general you write $f^{(k)}$ for the $k$th derivative.
:::

If $f''(x)>0$, the slope grows at $x$; the graph bends upward away from the tangent line and lies above it near $x$. If $f''(x)<0$, it bends downward. The second derivative therefore measures the __curvature__ of the graph, more precisely: how fast its slope changes.

With the second derivative, the approximation becomes more accurate. You replace the tangent line by the parabola that has the same value, the same slope and the same second derivative as $f$ at the point $x$. A parabola $p(h)=a+b\,h+c\,h^2$ has $p(0)=a$, $p'(0)=b$ and $p''(0)=2c$. For these three numbers to match $f(x)$, $f'(x)$ and $f''(x)$, we need $a=f(x)$, $b=f'(x)$ and $c=\tfrac12f''(x)$. That is where the factor $\tfrac12$ comes from.

:::satz Theorem 1.6 (Quadratic approximation)
<span class="anker" id="satz-1-6"></span>

If $f$ is twice differentiable near $x$ and $f''$ is continuous at the point $x$, then

<span class="anker" id="gl-1-6"></span>
$$f(x+h)=f(x)+f'(x)\,h+\tfrac12f''(x)\,h^2+r_2(h)\qquad\text{with}\qquad\lim_{h\to0}\frac{r_2(h)}{h^2}=0 . \tag{1.6}$$
:::

Here continuous means that $f''$ changes only a little, without a jump, when the point changes slightly. The proof works similarly to the one for the linear approximation, with one more step; the statement is called Taylor's theorem. The error $r_2(h)$ now vanishes faster than $h^2$, so for small $h$ much faster still than the error of the linear approximation.

::::beispiel [Worked example]
For $f(x)=x^3$, $f'(x)=3x^2$, $f''(x)=6x$ and $f'''(x)=6$. At the point $2$, $f''(2)=12>0$: the graph bends upward away from the tangent line, as the left panel of Fig. [2](#abb-2) shows. The quadratic approximation for $h=0.01$ is

$$f(2.01)\approx8+12\cdot0.01+\tfrac12\cdot12\cdot0.01^2=8+0.12+0.0006=8.1206 .$$

The exact value is $8.120601$, the error only $0.000001=h^3$. Fig. [3](#abb-3) shows the sum of the three terms.

:::abbildung ml/k3rtaylor1 3
The quadratic approximation of $f(x)=x^3$ at the point $2$ for $h=0.01$ as the sum of value, slope term and curvature term.
:::
::::

⁠**In short:** The second derivative measures how fast the slope changes, that is, the curvature; with it, the approximation becomes $f(x+h)\approx f(x)+f'(x)\,h+\tfrac12f''(x)\,h^2$.

:::hintergrund Higher-order Taylor polynomials
You can go further and match the third and all further derivatives as well. The polynomial

$$f(x)+f'(x)\,h+\frac{f''(x)}{2}\,h^2+\frac{f'''(x)}{6}\,h^3+\dots+\frac{f^{(k)}(x)}{k!}\,h^k$$

is called the Taylor polynomial of order $k$; here $k!=1\cdot2\cdots k$. Like the factor $\tfrac12$, the denominators $k!$ come from the fact that the $k$th derivative of $h^k$ equals $k!$. For $f(x)=x^3$, the Taylor polynomial of order three is already exact: $8+12h+6h^2+h^3$ is exactly $(2+h)^3$. For most functions, the approximation improves with each order as long as $h$ is small enough. For this chapter, orders one and two suffice.
:::

:::aufgabe Exercise 1 ★ Secant lines and the tangent line
<span class="anker" id="aufg-1"></span>

Let $f(x)=x^2$.

<ol class="al">

<li>

Compute the difference quotient at the point $3$ for $h=1$, $h=0.1$ and $h=-0.1$.

</li>

<li>

Show that the difference quotient at the point $3$ equals $6+h$, and determine $f'(3)$.

</li>

<li>

State the tangent line at the point $3$ and use it to compute an approximation for $3.02^2$. How large is the error?

</li>

</ol>

:::loesung
(a) With $f(3)=9$,

$$\frac{4^2-9}{1}=7,\qquad \frac{3.1^2-9}{0.1}=\frac{9.61-9}{0.1}=6.1,\qquad \frac{2.9^2-9}{-0.1}=\frac{8.41-9}{-0.1}=5.9 .$$

The secant line to the right is steeper and the one to the left is flatter than the tangent line, because the graph of the parabola curves upward.

(b) $(3+h)^2=9+6h+h^2$, so the difference quotient is $\frac{6h+h^2}{h}=6+h$. As $h\to0$, it tends to $6$ from both sides; thus $f'(3)=6$, in agreement with the rule $(x^2)'=2x$.

(c) The tangent line is $t(x)=9+6\,(x-3)$. It gives $3.02^2\approx9+6\cdot0.02=9.12$. The exact value is $3.02^2=9.1204$. The error $0.0004=0.02^2$ is exactly $h^2$, because $f(3+h)-9-6h=h^2$. It vanishes faster than $h$, as the linear approximation promises.
:::
:::

:::aufgabe Exercise 2 ★ Differentiating with the rules
<span class="anker" id="aufg-2"></span>

Differentiate and evaluate at the given point.

<ol class="al">

<li>

$f(x)=4x^3-2x+7$ at the point $1$;

</li>

<li>

$f(x)=x^2\,\mathrm{e}^x$ at the points $0$ and $1$;

</li>

<li>

$f(x)=\dfrac{x}{1+x^2}$ at the points $0$ and $1$. What does the result at the point $1$ mean for the graph?

</li>

</ol>

:::loesung
(a) Sum rule and constant multiple rule together with the power rule: $f'(x)=12x^2-2$, so $f'(1)=10$.

(b) Product rule with $u=x^2$, $v=\mathrm{e}^x$: $f'(x)=2x\,\mathrm{e}^x+x^2\,\mathrm{e}^x=(2x+x^2)\,\mathrm{e}^x$. So $f'(0)=0$ and $f'(1)=3\mathrm{e}\approx8.155$.

(c) Quotient rule with $u=x$, $u'=1$, $v=1+x^2$, $v'=2x$:

$$f'(x)=\frac{1\cdot(1+x^2)-x\cdot2x}{(1+x^2)^2}=\frac{1-x^2}{(1+x^2)^2},\qquad f'(0)=1,\qquad f'(1)=0 .$$

At the point $1$, the graph has a horizontal tangent line. Its highest point lies there: for all $x$, $\frac{x}{1+x^2}\le\frac12$, because $1+x^2-2x=(x-1)^2\ge0$, and $f(1)=\tfrac12$.
:::
:::

:::aufgabe Exercise 3 ★★ Square roots under the magnifying glass
<span class="anker" id="aufg-3"></span>

Let $f(x)=\sqrt x$.

<ol class="al">

<li>

Compute $f'(x)$ and $f''(x)$ with the power rule.

</li>

<li>

Use the linear and the quadratic approximation at the point $4$ to compute an approximate value for $\sqrt{4.1}$. Compare both with a calculator.

</li>

<li>

Does the tangent line lie above or below the graph? Justify your answer with the sign of $f''(4)$.

</li>

</ol>

:::loesung
(a) With $\sqrt x=x^{1/2}$, we get $f'(x)=\tfrac12x^{-1/2}=\frac1{2\sqrt x}$ and $f''(x)=-\tfrac14x^{-3/2}$.

(b) At the point $4$, $f(4)=2$, $f'(4)=\tfrac14$ and $f''(4)=-\tfrac14\cdot\tfrac18=-\tfrac1{32}$. With $h=0.1$:

$$\text{linear: }2+\tfrac14\cdot0.1=2.025,\qquad \text{quadratic: }2.025-\tfrac12\cdot\tfrac1{32}\cdot0.01=2.025-0.00015625=2.02484375 .$$

The calculator gives $\sqrt{4.1}\approx2.0248457$. The error of the linear approximation is about $1.5\cdot10^{-4}$, that of the quadratic one only about $1.9\cdot10^{-6}$.

(c) Since $f''(4)<0$, the graph bends downward away from the tangent line; the tangent line lies above the graph. That is why the linear approximation $2.025$ is too large.
:::
:::

:::aufgabe Exercise 4 ★★ Kink or no kink
<span class="anker" id="aufg-4"></span>

<ol class="al">

<li>

Use the difference quotient to show that $g(x)=x\,|x|$ is differentiable at the point $0$, and determine $g'(0)$.

</li>

<li>

Determine $g'(x)$ for $x>0$ and for $x<0$. Does $g'$ itself have a derivative at the point $0$?

</li>

<li>

The function $m(x)=\max(x,\,0)$ returns $x$ if $x$ is positive and $0$ otherwise. Where is it differentiable, and what values does its derivative take there?

</li>

</ol>

:::loesung
(a) We have $g(0)=0$ and $\frac{g(h)-g(0)}{h}=\frac{h\,|h|}{h}=|h|$. This tends to $0$ from both sides, so $g'(0)=0$. The absolute value alone has a kink, but the factor $x$ flattens the two branches at the origin.

(b) For $x>0$, $g(x)=x^2$ and $g'(x)=2x$; for $x<0$, $g(x)=-x^2$ and $g'(x)=-2x$. Together with (a), $g'(x)=2|x|$ for all $x$. This function has a kink at $0$; its difference quotient $2|h|/h$ is $\pm2$. So $g$ is differentiable once, but not twice.

(c) For $x>0$, $m(x)=x$ with $m'(x)=1$; for $x<0$, $m(x)=0$ with $m'(x)=0$. At the point $0$, the difference quotient is $1$ for $h>0$ and $0$ for $h<0$; there is no derivative there. The graph has a kink at $0$.
:::
:::
