---
title: 本章要点
pfad: 电气工程 / 第 3 学期 / 信号与系统 / 拉普拉斯变换
order: 3220900
summary: 每个信号都是 $\mathrm{e}^{pt}$ 的叠加， 以及为什么 LTI 系统的作用因此变成乘法
tags: 
lang: zh
---

:::merke 三句话的答案
<ol>

<li>

LTI 系统对基本分量 $\mathrm{e}^{pt}$ 只能乘以一个数 $H(p)$，因为对 $\mathrm{e}^{pt}$ 而言，平移就等同于相乘。

</li>

<li>

每个存在收敛域的信号都是这类基本分量的叠加。$S(p)$ 给出基本分量 $\mathrm{e}^{pt}$ 以多大的权重包含在信号中。

</li>

<li>

正因如此，卷积变成了乘法：$G(p)=H(p)\,S(p)$。若 $S(p)$ 是有理函数，信号就是以极点为指数的有限和 $\sum_r A_r\mathrm{e}^{p_r t}$。

</li>

</ol>
:::

:::kern 本章要点
<ul>

<li>

$\mathrm{e}^{p(t-\tau)}=\mathrm{e}^{-p\tau}\mathrm{e}^{pt}$，因此 $\mathrm{e}^{pt}*h=H(p)\,\mathrm{e}^{pt}$，其中 $H(p)=\int h(t)\mathrm{e}^{-pt}\mathrm{d} t$。

</li>

<li>

$p=\sigma+\mathrm{j}2\pi f$：$\sigma$ 是基本分量的增长率，$f$ 是其频率。

</li>

<li>

$s(t)=\frac{1}{2\pi\mathrm{j}}\int_{\sigma-\mathrm{j}\infty}^{\sigma+\mathrm{j}\infty}S(p)\mathrm{e}^{pt}\mathrm{d} p$，$\sigma$ 位于收敛域内；每条这样的直线都给出同一个 $s(t)$。

</li>

<li>

$S(\sigma+\mathrm{j}2\pi f)=\mathcal{F}\{s(t)\mathrm{e}^{-\sigma t}\}$；$\sigma=0$ 时即为傅里叶变换。

</li>

<li>

收敛域：只取决于 $\sigma$；右边信号为右半平面，左边信号为左半平面，双边信号为带状区域。

</li>

<li>

$\mathrm{e}^{p_0t}\varepsilon(t)\leftrightarrow\frac{1}{p-p_0}$，$\operatorname{Re} p>\operatorname{Re} p_0$；$-\mathrm{e}^{p_0t}\varepsilon(-t)\leftrightarrow\frac{1}{p-p_0}$，$\operatorname{Re} p<\operatorname{Re} p_0$。

</li>

<li>

$G(p)=S(p)H(p)$；求导 $\to p$，积分 $\to1/p$。

</li>

<li>

有理且右边：$s(t)=A_0\delta(t)+\sum_rA_r\mathrm{e}^{p_rt}\varepsilon(t)$，极点 = 指数。因果且稳定：所有极点都在左侧。

</li>

</ul>
:::
