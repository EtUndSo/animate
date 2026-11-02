---
title: 第 4 阶段：能量谱密度
pfad: 电气工程 / 第 3 学期 / 信号与系统 / 相关函数
order: 3260500
summary: 相关函数的傅里叶变换是什么？它表明能量如何分布在各个频率上。
tags: 能量谱密度, 互能量谱密度
lang: zh
---

<span class="anker" id="stufe-4"></span>

:::zweck
相关函数的傅里叶变换是什么？它表明能量如何分布在各个频率上。
:::

:::satz 定理 4.1 (能量信号的维纳–辛钦定理)
<span class="anker" id="satz-4-1"></span>

<span class="anker" id="gl-4-1"></span>
$$\varphi^E_{ss}(\tau)=s^*(-\tau)*s(\tau)\;\circ\!\!-\!\!\bullet\;S^*(f)\,S(f)=|S(f)|^2,\qquad\varphi^E_{sg}(\tau)\;\circ\!\!-\!\!\bullet\;S^*(f)\,G(f). \tag{4.1}$$
:::

⁠**如何理解：**$|S(f)|^2$ 称为__能量谱密度__。它是实的，永不为负，并且对实信号而言是 $f$ 的偶函数。信号的相位丢失了：幅度谱相同的所有信号都有相同的自相关函数。$S^*G$ 称为__互能量谱密度__。推导只需要卷积定理、时间反转和共轭：$s^*(-\tau)\circ\!\!-\!\!\bullet\,S^*(f)$（[第 3 部分](/wissen/zh/elektrotechnik/3-semester/signale-und-systeme/fourier-reihe-und-transformation/fourier-reihe-und-transformation.html)）。

**帕塞瓦尔定理。** 在 $\tau=0$ 处，自相关函数就是能量。利用面积定理：

<span class="anker" id="gl-4-2"></span>
$$E_s=\varphi^E_{ss}(0)=\int_{-\infty}^{\infty}|s(t)|^2\,\mathrm{d} t=\int_{-\infty}^{\infty}|S(f)|^2\,\mathrm{d} f. \tag{4.2}$$

两个正交信号的频谱也是正交的：$\int s^*g\,\mathrm{d} t=\int S^*G\,\mathrm{d} f=0$。

**例：指数脉冲。** $s(t)=\varepsilon(t)\mathrm{e}^{-t}$ 的频谱为 $S(f)=\frac{1}{1+\mathrm{j}2\pi f}$，因此 $|S|^2=\frac{1}{1+(2\pi f)^2}$。它同时也是 $\operatorname{Re}\{S\}$，而 $\operatorname{Re}\{S\}$ 的逆变换是信号的偶部（[第 3 部分](/wissen/zh/elektrotechnik/3-semester/signale-und-systeme/fourier-reihe-und-transformation/fourier-reihe-und-transformation.html)）：

$$\varphi^E_{ss}(\tau)=\tfrac12\mathrm{e}^{-|\tau|},\qquad E_s=\varphi^E_{ss}(0)=\tfrac12.$$

在时域中由 $\int_0^\infty\mathrm{e}^{-2t}\mathrm{d} t=\frac12$，在频域中由 $\int\frac{\mathrm{d} f}{1+(2\pi f)^2}=\frac12$，都得到同样的值。图 [2](#abb-2) 给出了信号、它的自相关函数以及两个频谱。

:::abbildung et3/k6exp 2
指数脉冲（$RC=1$ s）。左：信号及其自相关函数 $\frac12\mathrm{e}^{-|\tau|}$（偶函数，最大值 $=E_s=\frac12$）。右：幅度谱和能量谱密度，后者衰减得更快：能量集中在低频。
:::

:::aufgabe 练习 4 ★ 验证帕塞瓦尔定理
<span class="anker" id="aufg-4"></span>

在时域中计算 $\operatorname{rect}(t)$ 的能量，再利用式 [(4.2)](#gl-4-2) 由其频谱计算。由此可以得出 si 函数的哪个著名积分？

:::loesung
时域：$E=\int\operatorname{rect}^2\mathrm{d} t=1$。频域：$\int\operatorname{si}^2(\pi f)\mathrm{d} f$。因此 $\int_{-\infty}^\infty\operatorname{si}^2(\pi f)\mathrm{d} f=1$。
:::
:::
