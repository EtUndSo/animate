---
title: Stage 4: The integral becomes a sum
pfad: Electrical Engineering / 3rd Semester / Signals and Systems / Laplace Transform
order: 3220700
summary: The conjecture taken literally: for the signals that system theory almost always deals with, the signal is a finite sum of complex exponentials.
tags: partial fraction expansion, stability, natural response
lang: en
---

<span class="anker" id="stufe-4"></span>

:::zweck
The conjecture taken literally: for the signals that system theory almost always deals with, the signal is a *finite sum* of complex exponentials. The poles are the exponents.
:::

**The idea.** For networks of $R$, $L$, $C$ and for all systems described by a differential equation, $S(p)$ is a ratio of polynomials. For simple poles, the __partial fraction expansion__ writes it as

$$S(p)=A_0+\sum_{r=1}^{R}\frac{A_r}{p-p_r},\qquad A_r=\lim_{p\to p_r}(p-p_r)\,S(p).$$

Each term is the transform of *a single building block*: by [(2.2)](konvergenzbereich-welche-dampfungen-funktionieren.html#gl-2-2), $A_r/(p-p_r)$ belongs to $A_r\,\mathrm{e}^{p_r t}\varepsilon(t)$ if the region of convergence lies to the right of the pole, and by [(2.4)](konvergenzbereich-welche-dampfungen-funktionieren.html#gl-2-4) the constant term $A_0$ belongs to $A_0\,\delta(t)$. So for a right-sided signal

<span class="anker" id="gl-4-1"></span>
$$s(t)=A_0\,\delta(t)+\sum_{r=1}^{R}A_r\,\mathrm{e}^{p_r t}\,\varepsilon(t). \tag{4.1}$$

⁠**In short:** A right-sided signal with a rational Laplace transform is a finite sum of building blocks $\mathrm{e}^{p_r t}$. The poles are the exponents, and the partial fraction coefficients are the weights.

This means you can read off any such signal from its poles, using the map from Fig. [1](warum-gerade.html#abb-1): $\operatorname{Re} p_r$ tells you whether the building block decays or grows, and $\operatorname{Im} p_r$ how fast it oscillates. A conjugate pair of poles $p_r,p_r^*$ together gives a real damped oscillation. This is also the core of __stability__: a causal building block $\mathrm{e}^{p_r t}\varepsilon(t)$ decays if and only if $\operatorname{Re} p_r<0$. A causal system is therefore stable if all poles of $H(p)$ lie in the left half-plane.

**Example.** The step response from Stage [3](aus-der-faltung-wird-eine-multiplikation.html#stufe-3) has the poles $0$ and $-1$:

$$g(t)=\underbrace{1\cdot\mathrm{e}^{0\cdot t}}_{\text{pole }0\text{ (from }S)}\;\underbrace{-\;1\cdot\mathrm{e}^{-t}}_{\text{pole }-1\text{ (from }H)}\qquad(t>0).$$

The pole of the input gives the part that the input forces (the final voltage 1). The pole of the system gives the __natural response__ of the RC circuit, the decay with $RC=1$ s. This holds in general: the output $G=SH$ contains the poles of the input and the poles of the system.

:::zusatz Why the integral collapses into a sum: the residue theorem
This section needs the residue theorem from complex analysis. It explains why [(2.1)](der-trick-dampfen-zerlegen-zuruckmultiplizieren.html#gl-2-1) and [(4.1)](#gl-4-1) are the same and why the region of convergence decides the signal.

Let $S(p)$ be a ratio of polynomials whose numerator degree is lower than its denominator degree, with simple poles.

<ul>

<li>

⁠**$t>0$:** Close the line of integration with a large semicircle to the *left*. There $\operatorname{Re} p\to-\infty$, so $|\mathrm{e}^{pt}|=\mathrm{e}^{\operatorname{Re} p\,t}\to0$, and $S(p)\to0$. In the limit the semicircle contributes nothing (Jordan's lemma). The closed path runs counterclockwise, and the residue theorem gives

$$s(t)=\sum_{\text{poles left of the line}}\operatorname*{Res}_{p=p_r}\bigl[S(p)\,\mathrm{e}^{pt}\bigr]=\sum_{\text{left}}A_r\,\mathrm{e}^{p_r t}.$$

The residue at a simple pole is $\lim_{p\to p_r}(p-p_r)S(p)\mathrm{e}^{pt}=A_r\mathrm{e}^{p_rt}$: exactly the partial fraction coefficient.

</li>

<li>

⁠**$t<0$:** Now $\mathrm{e}^{pt}$ vanishes for $\operatorname{Re} p\to+\infty$. Close to the *right*; the path runs clockwise, which gives a minus sign:

$$s(t)=-\sum_{\text{poles right of the line}}A_r\,\mathrm{e}^{p_r t}.$$

</li>

</ul>

⁠**Consequence:** The position of the line, that is, the region of convergence, decides which poles give causal building blocks (left of the line) and which give anticausal ones (right of the line). Example: $S(p)=\frac{1}{(p+1)(p+2)}=\frac{1}{p+1}-\frac{1}{p+2}$ (Fig. [5](#abb-5)). If the line lies between the poles, $-2<\sigma<-1$, then $-2$ acts for $t>0$ and $-1$ for $t<0$:

$$s(t)=-\mathrm{e}^{-2t}\varepsilon(t)-\mathrm{e}^{-t}\varepsilon(-t).$$

Evaluated numerically on the line $\sigma=-1.5/\mathrm s$: $s(1\,\mathrm{s})=-0.1353=-\mathrm{e}^{-2}$ and $s(-1\,\mathrm{s})=-2.7183=-\mathrm{e}^{1}$. If the line lies to the right of both poles, the same formula gives the causal signal $(\mathrm{e}^{-t}-\mathrm{e}^{-2t})\varepsilon(t)$; if it lies to the left of both, it gives the anticausal signal $-(\mathrm{e}^{-t}-\mathrm{e}^{-2t})\varepsilon(-t)$.

:::abbildung et3/k2residuen 5
Line of integration $\sigma=-1.5/\mathrm s$ in the strip $-2<\operatorname{Re} p<-1$ (blue) and the semicircles that close it (red).
:::
:::

:::aufgabe Exercise 7 ★★★ (Going further) Same formula, two signals
<span class="anker" id="aufg-7"></span>

$S(p)=\dfrac{1}{p+1}$.

<ol class="al">

<li>

Region of convergence $\operatorname{Re} p>-1$. Evaluate the inversion formula with the residue theorem, separately for $t>0$ and $t<0$.

</li>

<li>

The same for the region of convergence $\operatorname{Re} p<-1$.

</li>

<li>

Compare with the basic transform pairs [(2.2)](konvergenzbereich-welche-dampfungen-funktionieren.html#gl-2-2) and [(2.3)](konvergenzbereich-welche-dampfungen-funktionieren.html#gl-2-3). What does this teach you about the statement “$S(p)=1/(p+1)$” without a region of convergence?

</li>

</ol>

:::loesung
(a) Line to the right of the pole, for example $\sigma=0$. For $t>0$, close to the left: the pole $-1$ lies inside, $\operatorname*{Res}_{p=-1}\frac{\mathrm{e}^{pt}}{p+1}=\mathrm{e}^{-t}$, so $s(t)=\mathrm{e}^{-t}$. For $t<0$, close to the right: there is no pole to the right of the line, so $s(t)=0$. Together, $s(t)=\mathrm{e}^{-t}\varepsilon(t)$.

(b) Line to the left of the pole, for example $\sigma=-2$. For $t>0$, close to the left: no pole, $s(t)=0$. For $t<0$, close to the right: pole inside, clockwise path, $s(t)=-\mathrm{e}^{-t}$. Together, $s(t)=-\mathrm{e}^{-t}\varepsilon(-t)$.

(c) These are exactly the basic transform pairs [(2.2)](konvergenzbereich-welche-dampfungen-funktionieren.html#gl-2-2) and [(2.3)](konvergenzbereich-welche-dampfungen-funktionieren.html#gl-2-3) with $p_0=-1$. The statement “$S(p)=1/(p+1)$” alone does not determine the signal. Only with the region of convergence is it clear on which side of the line the pole lies and whether it gives a causal or an anticausal building block.
:::
:::
