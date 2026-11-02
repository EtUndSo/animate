---
title: 要点
pfad: 电气工程 / 第 3 学期 / 信号与系统 / 傅里叶级数与变换
order: 3231300
summary: 每个信号都是振荡的叠加
tags: 
lang: zh
---

:::merke 三句话的答案
<ol>

<li>

周期信号是位于基频整数倍处的各个振荡之和（傅里叶级数）；非周期信号是对所有频率的积分（傅里叶积分）。

</li>

<li>

每个振荡 $\mathrm{e}^{\mathrm{j}2\pi ft}$ 都是特征函数：LTI 系统把它乘以 $H(f)$，因此卷积变成了乘积 $G(f)=S(f)\,H(f)$。

</li>

<li>

所有运算规则（时移、展缩、调制、对偶性）都可以由相应运算对单个振荡的作用推出。

</li>

</ol>
:::

:::kern 要点
<ul>

<li>

$\mathrm{e}^{\mathrm{j}2\pi ft}*h=H(f)\mathrm{e}^{\mathrm{j}2\pi ft}$；$H(f)=\int h\,\mathrm{e}^{-\mathrm{j}2\pi ft}\mathrm{d} t$。

</li>

<li>

级数：$s_p=\sum S_p(k)\mathrm{e}^{\mathrm{j}2\pi kFt}$，$S_p(k)=\frac1T\int_Ts_p\mathrm{e}^{-\mathrm{j}2\pi kFt}\mathrm{d} t$；实信号：$S_p(-k)=S_p^*(k)$。

</li>

<li>

帕塞瓦尔定理：$\frac1T\int_T|s_p|^2=\sum|S_p(k)|^2$；吉布斯现象：跳变处约 9 % 的过冲；LTI：$G_p(k)=S_p(k)H(kF)$。

</li>

<li>

$S(f)=\int s\,\mathrm{e}^{-\mathrm{j}2\pi ft}\mathrm{d} t$，$s=\int S\mathrm{e}^{\mathrm{j}2\pi ft}\mathrm{d} f$；$s*h\leftrightarrow SH$，$s_1s_2\leftrightarrow S_1*S_2$。

</li>

<li>

实信号：$S(-f)=S^*(f)$；偶部 $\leftrightarrow\operatorname{Re} S$，奇部 $\leftrightarrow\mathrm{j}\operatorname{Im} S$。

</li>

<li>

$s(bt)\leftrightarrow\frac1{|b|}S(f/b)$；$s(t-t_0)\leftrightarrow S\mathrm{e}^{-\mathrm{j}2\pi ft_0}$；$\frac{\mathrm{d}}{\mathrm{d} t}\leftrightarrow\mathrm{j}2\pi f$；$\mathrm{e}^{\mathrm{j}2\pi Ft}s\leftrightarrow S(f-F)$；$S(t)\leftrightarrow s(-f)$。

</li>

<li>

$\operatorname{rect}(t/T)\leftrightarrow|T|\operatorname{si}(\pi Tf)$；$\Lambda\leftrightarrow\operatorname{si}^2$；$\delta\leftrightarrow1$；$1\leftrightarrow\delta(f)$；$\cos\leftrightarrow\frac12[\delta(f+F)+\delta(f-F)]$。

</li>

<li>

梳状函数 $\leftrightarrow$ 梳状函数：$\sum\delta(t-nT)\leftrightarrow\frac1{|T|}\sum\delta(f-k/T)$；$\varepsilon\leftrightarrow\frac12\delta(f)+\frac{1}{\mathrm{j}2\pi f}$。

</li>

<li>

希尔伯特变换：$h=\frac{1}{\pi t}$，$H=-\mathrm{j}\operatorname{sgn}(f)$；$s_+=\frac12(s+\mathrm{j}\hat s)$，$s=2\operatorname{Re} s_+$。

</li>

</ul>
:::
