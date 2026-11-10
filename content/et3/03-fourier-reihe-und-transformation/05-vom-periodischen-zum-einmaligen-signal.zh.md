---
title: 第 4 阶段：从周期信号到非周期信号
pfad: 电气工程 / 第 3 学期 / ET3 – 电气工程基础 3：信号与系统 / 傅里叶级数与变换
adresse: elektrotechnik/3-semester/signale-und-systeme/fourier-reihe-und-transformation
knoten: 第 3 章：傅里叶级数与变换
order: 3230500
summary: 单个脉冲不是周期的，但可以把它看作周期无限长的周期信号。在此过程中，求和变成了积分。
tags: 频谱密度
lang: zh
---

<span class="anker" id="stufe-4"></span>

:::zweck
单个脉冲不是周期的，但可以把它看作周期无限长的周期信号。在此过程中，求和变成了积分。
:::

**思路。** 把持续时间小于 $T$ 的脉冲 $s(t)$ 作周期延拓。这时级数的系数是一个固定函数的取值：

$$S_p(k)=\frac1T\int_{-\infty}^{\infty}s(t)\mathrm{e}^{-\mathrm{j}2\pi kFt}\mathrm{d} t=F\cdot S(kF),\qquad S(f)=\int_{-\infty}^{\infty}s(t)\mathrm{e}^{-\mathrm{j}2\pi ft}\mathrm{d} t.$$

若把周期加倍，谱线间隔 $F$ 减半，谱线以两倍的密度对同一包络 $S(f)$ 进行采样（图 [4](#abb-4)）。在极限 $T\to\infty$ 下，间隔 $F$ 变为微分 $\mathrm{d} f$，和式 $\sum_kS(kF)\mathrm{e}^{\mathrm{j}2\pi kFt}F$ 变为积分。

:::abbildung et3/k3grenz 4
矩形脉冲 $\operatorname{rect}(t)$ 分别以 $T=2$ s 和 $T=4$ s 作周期延拓。乘以 $T$ 后的傅里叶系数位于同一包络 $S(f)=\operatorname{si}(\pi f)$ 上，间隔为 $1/T$。当 $T\to\infty$ 时，它们无间隙地填满整条曲线。
:::

:::satz 定理 4.1 (傅里叶变换)
<span class="anker" id="satz-4-1"></span>

<span class="anker" id="gl-4-1"></span>
$$S(f)=\int_{-\infty}^{\infty}s(t)\,\mathrm{e}^{-\mathrm{j}2\pi ft}\,\mathrm{d} t,\qquad s(t)=\int_{-\infty}^{\infty}S(f)\,\mathrm{e}^{\mathrm{j}2\pi ft}\,\mathrm{d} f. \tag{4.1}$$

简记：$s(t)\;\circ\!\!-\!\!\bullet\;S(f)$ 或 $S(f)=\mathcal{F}\{s(t)\}$。
:::

⁠**如何理解：**$S(f)$ 是__频谱密度__：单位频率区间上的权重。若 $s$ 是以 V 为单位的电压，则 $S$ 的单位为 V/Hz。逆变换由所有振荡合成信号，每个振荡的权重为 $S(f)\,\mathrm{d} f$。存在的一个充分条件是 $\int|s(t)|\mathrm{d} t<\infty$。傅里叶变换就是虚轴上的拉普拉斯变换，$S(f)=S_{\mathcal{L}}(\mathrm{j}2\pi f)$，前提是虚轴位于收敛域内（[第 2 章](/wissen/zh/elektrotechnik/3-semester/signale-und-systeme/laplace-transformation/laplace-transformation.html)）。

⁠**卷积变成乘积。**与[第 2 章](/wissen/zh/elektrotechnik/3-semester/signale-und-systeme/laplace-transformation/laplace-transformation.html)一样：$s(t)*h(t)\;\circ\!\!-\!\!\bullet\;S(f)\,H(f)$。由 $s*\delta=s$ 得 $S(f)\cdot\mathcal{F}\{\delta\}=S(f)$，因此 $\delta(t)\;\circ\!\!-\!\!\bullet\;1$：狄拉克冲激以相同的权重包含所有频率。

::::beispiel 指数脉冲
RC 电路的冲激响应 $h(t)=\frac1{RC}\varepsilon(t)\mathrm{e}^{-t/RC}$：

$$H(f)=\frac1{RC}\int_0^\infty\mathrm{e}^{-(1/RC+\mathrm{j}2\pi f)t}\mathrm{d} t=\frac{1}{1+\mathrm{j}2\pi f\,RC}.$$

这与交流分析（[第 1 章](/wissen/zh/elektrotechnik/3-semester/signale-und-systeme/lti-systeme-und-faltung/lti-systeme-und-faltung.html)）得到的频率响应相同。因此，冲激响应包含了关于频率特性的全部信息。
::::

:::frage $S_p(k)$ 与 $S(f)$ 除了一个是离散的之外，还有什么区别？
单位。$S_p(k)$ 是幅度（V）：第 $k$ 次谐波确实具有这样的强度。$S(f)$ 是密度（V/Hz）：在非周期信号中，没有哪个单独的频率具有有限的幅度；只有一个频带 $\Delta f$ 大约携带 $S(f)\,\Delta f$。这就是 $S_p(k)=F\cdot S(kF)$ 的原因：每条谱线代表宽度为 $F$ 的一个频带。
:::

:::aufgabe 练习 4 ★ 双边指数脉冲
<span class="anker" id="aufg-4"></span>

对 $a>0$，把积分分成 $t<0$ 和 $t>0$ 两部分，计算 $\mathcal{F}\{\mathrm{e}^{-a|t|}\}$。证明结果是实的偶函数，并用信号的对称性解释这一点。

:::loesung
$$\int_{-\infty}^0\mathrm{e}^{at}\mathrm{e}^{-\mathrm{j}2\pi ft}\mathrm{d} t+\int_0^\infty\mathrm{e}^{-at}\mathrm{e}^{-\mathrm{j}2\pi ft}\mathrm{d} t=\frac{1}{a-\mathrm{j}2\pi f}+\frac{1}{a+\mathrm{j}2\pi f}=\frac{2a}{a^2+(2\pi f)^2}.$$

结果是 $f$ 的实偶函数。必然如此：信号是实的偶函数，所以其奇部为零，因而 $\operatorname{Im} S$ 也为零（第 [5](symmetrien-im-signal-und-im-spektrum.html#stufe-5) 阶段）。
:::
:::
