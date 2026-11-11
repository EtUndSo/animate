---
title: 第 7 阶段：狄拉克冲激
pfad: 电气工程 / 第 3 学期 / ET3 – 电气工程基础 3：信号与系统 / LTI 系统与卷积
adresse: elektrotechnik/3-semester/signale-und-systeme/lti-systeme-und-faltung
knoten: 第 1 章：LTI 系统与卷积
order: 3210800
summary: 狄拉克冲激就是第 4 阶段中的那个极限对象。它不是普通的函数。它的全部性质都源于一个事实：它只通过自己的面积起作用。
tags: 广义函数, 理想延时器, 广义求导
lang: zh
---

<span class="anker" id="stufe-7"></span>

:::zweck
狄拉克冲激就是第 [4](das-faltungsintegral.html#stufe-4) 阶段中的那个极限对象。它不是普通的函数。它的全部性质都源于一个事实：它只通过自己的面积起作用。
:::

**$\delta$ 是什么，不是什么。** 当 $T_0\to0$ 时，矩形 $\frac{1}{T_0}\operatorname{rect}(t/T_0)$ 越来越窄、越来越高，而面积始终为 1（图 [8](#abb-8)）。在普通函数的意义下，这个极限并不存在：一个除某一点外处处为零的函数，无论它在该点取什么值，面积都为零。因此 $\delta(t)$ 是一个__广义函数__（又称分布）：一种仅由其在积分号下的作用、即由式 [(4.1)](das-faltungsintegral.html#gl-4-1) 来定义的对象。它被画成一个箭头，箭头的高度表示权重（面积）。

:::abbildung et3/k1dirac 8
左：面积为 1、越来越窄且越来越高的矩形。右：极限对象的符号。箭头的高度是权重，而不是函数值。
:::

:::satz 定理 7.1 (狄拉克冲激的性质)
<span class="anker" id="satz-7-1"></span>

<span class="anker" id="gl-7-1"></span>
<span class="anker" id="gl-7-2"></span>
<span class="anker" id="gl-7-3"></span>
<span class="anker" id="gl-7-4"></span>
<span class="anker" id="gl-7-5"></span>
<span class="anker" id="gl-7-6"></span>
$$\begin{aligned} &\text{权重：} && [a\,\delta(t)]*s(t)=a\,s(t),\qquad a_1\delta(t)+a_2\delta(t)=(a_1+a_2)\,\delta(t),\\ &\text{筛选：} && \int_{-\infty}^{\infty}\delta(\tau)\,s(-\tau)\,\mathrm{d}\tau=s(0),\qquad s(t)\,\delta(t-T)=s(T)\,\delta(t-T),\\ &\text{面积：} && \int_{-\infty}^{\infty}a\,\delta(t)\,\mathrm{d} t=a,\\ &\text{尺度变换：} && \delta(bt)=\frac{1}{|b|}\,\delta(t)\quad(b\neq0),\qquad \delta(-t)=\delta(t),\\ &\text{平移：} && \delta(t-t_0)*s(t)=s(t-t_0),\\ &\text{积分：} && \varepsilon(t)=\int_{-\infty}^t\delta(\tau)\,\mathrm{d}\tau,\qquad \frac{\mathrm{d}}{\mathrm{d} t}\varepsilon(t)=\delta(t). \end{aligned} \tag{7.1|7.2|7.3|7.4|7.5|7.6}$$
:::

⁠**如何理解：**乘积 $s(t)\,\delta(t-T)$ 只可能在 $T$ 点起作用，因此只有 $s(T)$ 有意义。压缩后的冲激 $\delta(bt)$ 同样是“无限高”的，但它的面积只有 $1/|b|$。$h(t)=\delta(t-t_0)$ 的系统把每个信号延迟 $t_0$，称为__理想延时器__。此外，由于阶跃是冲激的变上限积分，带跳变的函数也可以求导：高度为 $A$ 的跳变变成 $A\,\delta$。这称为__广义求导__。注意：许多运算，例如平方（$\delta^2$），对狄拉克冲激是没有定义的。

:::herleitung 尺度变换与筛选乘积
⁠**尺度变换。**对 $b>0$，令 $\vartheta=b\tau$：

$$\delta(bt)*s(t)=\int\delta(b\tau)\,s(t-\tau)\,\mathrm{d}\tau=\frac1b\int\delta(\vartheta)\,s\Bigl(t-\frac\vartheta b\Bigr)\mathrm{d}\vartheta=\frac1b\,s(t).$$

对 $b<0$，这一代换使积分方向反向，结果为 $-\frac1b=\frac{1}{|b|}$。因此 $\delta(bt)$ 的作用与 $\frac1{|b|}\delta(t)$ 相同。取 $b=-1$，即得对称性 $\delta(-t)=\delta(t)$。

⁠**筛选乘积。**把 $s(t)\delta(t)$ 与任意 $g(t)$ 做卷积，由筛选性质得

$$[s(t)\delta(t)]*g(t)=\int s(\tau)\delta(\tau)\,g(t-\tau)\,\mathrm{d}\tau=s(0)\,g(t)=[s(0)\delta(t)]*g(t).$$

两者对每个 $g$ 的作用都相同，所以 $s(t)\delta(t)=s(0)\delta(t)$。再经平移即得 $s(t)\delta(t-T)=s(T)\delta(t-T)$。

⁠**积分。**$\varepsilon(t)=\delta(t)*\varepsilon(t)=\int\delta(\tau)\,\varepsilon(t-\tau)\,\mathrm{d}\tau$，而 $\varepsilon(t-\tau)$ 恰在 $\tau\le t$ 时等于 1。
:::

:::frage 可是 $\delta(0)$ 是无穷大。那 $\delta(2t)$ 不就和 $\delta(t)$ 一样吗？
不是。“无限高”并不能刻画 $\delta$，因为除 $0$ 点以外，两者的所有函数值都相同，而 $0$ 点处的值不是一个数。刻画 $\delta$ 的是它的面积。如果把面积为 1 的矩形压缩到一半宽度而保持高度不变，面积就会减半。所以 $\delta(2t)=\frac12\delta(t)$。
:::

:::aufgabe 练习 8 ★ 用 $\delta$ 进行计算
<span class="anker" id="aufg-8"></span>

计算： (a) $\int_{-\infty}^\infty\delta(t-2)\,\mathrm{e}^{-t}\mathrm{d} t$， (b) $\mathrm{e}^{-t}\,\delta(t-1)$， (c) $\int_{-\infty}^\infty\delta(2t)\,\mathrm{d} t$， (d) $\delta(t)*\delta(t-3)$， (e) $\operatorname{rect}(t)*\delta(t-1)$， (f) $\frac{\mathrm{d}}{\mathrm{d} t}\bigl[3\,\varepsilon(t-1)\bigr]$。

:::loesung
(a) $\mathrm{e}^{-2}=0.135$； (b) $\mathrm{e}^{-1}\,\delta(t-1)$； (c) $\tfrac12$； (d) $\delta(t-3)$； (e) $\operatorname{rect}(t-1)$； (f) $3\,\delta(t-1)$。
:::
:::
