---
title: 第 6 阶段：运算规则（定理）
pfad: 电气工程 / 第 3 学期 / 信号与系统 / 傅里叶级数与变换
order: 3230700
summary: 不必每次都重新计算积分，而是使用规则：信号被平移、压缩、求导或调制时，频谱会怎样变化？每条规则都可以由该运算对单个振荡的作用推出。
tags: 能量谱密度
lang: zh
---

<span class="anker" id="stufe-6"></span>

:::zweck
不必每次都重新计算积分，而是使用规则：信号被平移、压缩、求导或调制时，频谱会怎样变化？每条规则都可以由该运算对单个振荡的作用推出。
:::

:::satz 定理 6.1 (傅里叶变换的定理)
<span class="anker" id="satz-6-1"></span>

<span class="anker" id="gl-6-1"></span>
<span class="anker" id="gl-6-2"></span>
<span class="anker" id="gl-6-3"></span>
<span class="anker" id="gl-6-4"></span>
<span class="anker" id="gl-6-5"></span>
<span class="anker" id="gl-6-6"></span>
<span class="anker" id="gl-6-7"></span>
<span class="anker" id="gl-6-8"></span>
<span class="anker" id="gl-6-9"></span>
<span class="anker" id="gl-6-10"></span>
<span class="anker" id="gl-6-11"></span>
$$\begin{aligned} &\text{叠加：} && \textstyle\sum_ia_is_i(t)\;\circ\!\!-\!\!\bullet\;\sum_ia_iS_i(f)\\ &\text{共轭：} && s^*(t)\;\circ\!\!-\!\!\bullet\;S^*(-f)\\ &\text{尺度变换：} && s(bt)\;\circ\!\!-\!\!\bullet\;\frac{1}{|b|}S\Bigl(\frac fb\Bigr),\quad b\neq0;\qquad s(-t)\;\circ\!\!-\!\!\bullet\;S(-f)\\ &\text{时移：} && s(t-t_0)\;\circ\!\!-\!\!\bullet\;S(f)\,\mathrm{e}^{-\mathrm{j}2\pi ft_0},\qquad\delta(t-t_0)\;\circ\!\!-\!\!\bullet\;\mathrm{e}^{-\mathrm{j}2\pi ft_0}\\ &\text{微分：} && \frac{\mathrm{d}^n}{\mathrm{d} t^n}s(t)\;\circ\!\!-\!\!\bullet\;(\mathrm{j}2\pi f)^nS(f)\\ &\text{对偶性：} && S(t)\;\circ\!\!-\!\!\bullet\;s(-f)\\ &\text{调制：} && \mathrm{e}^{\mathrm{j}2\pi Ft}s(t)\;\circ\!\!-\!\!\bullet\;S(f-F)\\ &\text{频域微分：} && -\mathrm{j}2\pi t\,s(t)\;\circ\!\!-\!\!\bullet\;\frac{\mathrm{d}}{\mathrm{d} f}S(f)\\ &\text{卷积、相乘：} && s_1*s_2\;\circ\!\!-\!\!\bullet\;S_1S_2,\qquad s_1s_2\;\circ\!\!-\!\!\bullet\;S_1*S_2\\ &\text{面积：} && \int s(t)\mathrm{d} t=S(0),\qquad\int S(f)\mathrm{d} f=s(0)\\ &\text{帕塞瓦尔定理：} && \int|s(t)|^2\mathrm{d} t=\int|S(f)|^2\mathrm{d} f \end{aligned} \tag{6.1|6.2|6.3|6.4|6.5|6.6|6.7|6.8|6.9|6.10|6.11}$$
:::

⁠**如何理解其中最重要的几条：**

<ul>

<li>

⁠**尺度变换：**在时间上压缩的信号（$|b|>1$）具有更宽的频谱。短信号需要许多频率。持续时间与带宽成反比关系。

</li>

<li>

⁠**时移：**延迟不改变模，只改变相位，而且相位随 $f$ 线性变化：每个振荡都被移动相同的时间，而频率越高，这段时间对应的角度就越大。

</li>

<li>

⁠**微分：**$\frac{\mathrm{d}}{\mathrm{d} t}\mathrm{e}^{\mathrm{j}2\pi ft}=\mathrm{j}2\pi f\,\mathrm{e}^{\mathrm{j}2\pi ft}$。微分会放大高频。

</li>

<li>

⁠**对偶性：**正变换与逆变换只在指数的符号上不同。因此，每个变换对都会给出另一个角色互换的变换对。

</li>

<li>

⁠**调制：**乘以 $\mathrm{e}^{\mathrm{j}2\pi Ft}$ 使整个频谱移动 $F$。每台无线电发射机都是这样工作的。

</li>

<li>

⁠**相乘：**两个信号乘积的频谱是两者频谱的卷积，这是卷积定理的对应形式。

</li>

<li>

⁠**帕塞瓦尔定理：**能量在两个域中相同。$|S(f)|^2$ 是按频率分布的__能量谱密度__。

</li>

</ul>

:::herleitung 尺度变换、时移、微分、对偶性、调制、相乘、帕塞瓦尔定理
⁠**尺度变换**（$b>0$，$\tau=bt$）：$\int s(bt)\mathrm{e}^{-\mathrm{j}2\pi ft}\mathrm{d} t=\frac1b\int s(\tau)\mathrm{e}^{-\mathrm{j}2\pi(f/b)\tau}\mathrm{d}\tau=\frac1bS(f/b)$。当 $b<0$ 时积分上下限互换，因此为 $1/|b|$。

⁠**时移**（$\tau=t-t_0$）：$\int s(\tau)\mathrm{e}^{-\mathrm{j}2\pi f(\tau+t_0)}\mathrm{d}\tau=\mathrm{e}^{-\mathrm{j}2\pi ft_0}S(f)$。令 $s=\delta$，即得 $\delta(t-t_0)$ 的变换对。

⁠**微分：**将逆变换对 $t$ 求导：$\frac{\mathrm{d}}{\mathrm{d} t}\int S\mathrm{e}^{\mathrm{j}2\pi ft}\mathrm{d} f=\int\mathrm{j}2\pi f\,S\,\mathrm{e}^{\mathrm{j}2\pi ft}\mathrm{d} f$。

⁠**对偶性：**在逆变换中用 $-t$ 代替 $t$：$s(-t)=\int S(f)\mathrm{e}^{-\mathrm{j}2\pi ft}\mathrm{d} f$。再把变量名 $t$ 和 $f$ 互换：$s(-f)=\int S(t)\mathrm{e}^{-\mathrm{j}2\pi ft}\mathrm{d} t$，这正是 $S(t)$ 的正变换。

⁠**调制：**$\int\mathrm{e}^{\mathrm{j}2\pi Ft}s(t)\mathrm{e}^{-\mathrm{j}2\pi ft}\mathrm{d} t=\int s(t)\mathrm{e}^{-\mathrm{j}2\pi(f-F)t}\mathrm{d} t=S(f-F)$。频域微分可用同样的方法，将正变换对 $f$ 求导得到。

⁠**相乘：**对信号 $s_1(t)$ 和 $s_2(t)$ 应用卷积定理，即 $s_1*s_2\;\circ\!\!-\!\!\bullet\;S_1S_2$，再对这个变换对应用对偶性：$S_1(t)S_2(t)\;\circ\!\!-\!\!\bullet\;s_1(-f)*s_2(-f)$。重新命名即得式 [(6.9)](#gl-6-9)。

⁠**面积：**在正变换中令 $f=0$，在逆变换中令 $t=0$。

⁠**帕塞瓦尔定理：**$\int|s|^2\mathrm{d} t=\int s\,s^*\mathrm{d} t$ 是乘积 $s(t)s^*(t)$ 的积分，因此由相乘、共轭和面积定理，它等于 $\bigl[S(f)*S^*(-f)\bigr]_{f=0}=\int S(\nu)S^*(\nu)\mathrm{d}\nu$。
:::

:::frage 为什么延迟不改变频谱的模？
因为延迟既不衰减也不放大任何振荡，只是把每个振荡平移。每个振荡都被平移相同的时间 $t_0$，在频率 $f$ 处，这对应于角度 $2\pi ft_0$。因此，相位是 $f$ 的一条直线，斜率为 $-2\pi t_0$。$|H|=1$ 且相位为线性的系统，会使信号延迟而不改变其形状。
:::

:::aufgabe 练习 6 ★★ 应用定理
<span class="anker" id="aufg-6"></span>

利用 $\operatorname{rect}(t)\;\circ\!\!-\!\!\bullet\;\operatorname{si}(\pi f)$（直接由定义得到：$\int_{-1/2}^{1/2}\mathrm{e}^{-\mathrm{j}2\pi ft}\,\mathrm{d} t=\operatorname{si}(\pi f)$）和上述定理。

<ol class="al">

<li>

求从 $t=0$ 到 $t=2$ s、高度为 1 的矩形脉冲的频谱。它在 $f=0$ 处的模是多少？第一个零点在哪里？

</li>

<li>

求 $F_0=5$ Hz 时 $\cos(2\pi F_0t)\operatorname{rect}(t)$ 的频谱，并画出草图。

</li>

</ol>

:::loesung
(a) 该脉冲为 $\operatorname{rect}\bigl(\frac{t-1}{2}\bigr)$。由尺度变换（$T=2$）和时移（$t_0=1$ s）得：$2\operatorname{si}(2\pi f)\,\mathrm{e}^{-\mathrm{j}2\pi f}$。$f=0$ 处的模为 2（即面积）。第一个零点在 $f=0.5$ Hz。时移只改变相位。

(b) $\cos(2\pi F_0t)=\frac12\mathrm{e}^{\mathrm{j}2\pi F_0t}+\frac12\mathrm{e}^{-\mathrm{j}2\pi F_0t}$，由调制定理得：$\frac12\operatorname{si}(\pi(f-5))+\frac12\operatorname{si}(\pi(f+5))$。即位于 $\pm5$ Hz 处的两个高度为 $\frac12$ 的 si 主瓣，第一个零点分别在其两侧 1 Hz 处。
:::
:::

:::aufgabe 练习 7 ★★ 以对偶性为工具
<span class="anker" id="aufg-7"></span>

由练习 [4](vom-periodischen-zum-einmaligen-signal.html#aufg-4) 可知 $\mathrm{e}^{-|t|}\;\circ\!\!-\!\!\bullet\;\frac{2}{1+(2\pi f)^2}$。不用积分，利用这一结果求 $\frac{1}{1+t^2}$ 的频谱。

:::loesung
对该变换对应用对偶性：$\frac{2}{1+(2\pi t)^2}\;\circ\!\!-\!\!\bullet\;\mathrm{e}^{-|f|}$。再对时间轴进行展缩。令 $x(t)=\frac{2}{1+(2\pi t)^2}$，则 $x\bigl(\frac{t}{2\pi}\bigr)=\frac{2}{1+t^2}$，因此由尺度变换定理（$b=\frac1{2\pi}$）得 $\frac{2}{1+t^2}\;\circ\!\!-\!\!\bullet\;2\pi\,\mathrm{e}^{-2\pi|f|}$。两边除以 2 得

$$\frac{1}{1+t^2}\;\circ\!\!-\!\!\bullet\;\pi\,\mathrm{e}^{-2\pi|f|}.$$

用面积定理验证：$\int\frac{\mathrm{d} t}{1+t^2}=\pi=S(0)$。
:::
:::
