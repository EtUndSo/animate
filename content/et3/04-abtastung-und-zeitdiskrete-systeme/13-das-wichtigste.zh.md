---
title: 要点
pfad: 电气工程 / 第 3 学期 / 信号与系统 / 采样与离散时间系统
order: 3241300
summary: 从连续信号到数值序列： 采样定理、离散卷积、DFT、FFT 与 z 变换
tags: 
lang: zh
---

:::merke 三句话的答案
<ol>

<li>

采样就是乘以狄拉克梳状函数。在频谱中，它变成与一个梳状函数的卷积：频谱以采样率为周期重复。

</li>

<li>

如果这些重复的部分互不重叠（采样率高于最高频率的两倍），就可以用理想低通滤波器精确地恢复信号。否则就会产生混叠。

</li>

<li>

适用于函数的工具同样适用于数值序列：求和形式的卷积、具有周期频谱的傅里叶变换、作为该频谱样本值的 DFT，以及与拉普拉斯变换相对应的 z 变换。

</li>

</ol>
:::

:::kern 要点
<ul>

<li>

理想采样：$s_\mathrm a=\sum s(nT)\delta(t-nT)$；频谱为 $\frac1T\sum_kS(f-k/T)$，以 $1/T$ 为周期。

</li>

<li>

采样定理：$f_\mathrm A\ge2f_\mathrm g$；恢复：$s(t)=\sum s(nT)\operatorname{si}(\pi(t-nT)/T)$；否则产生混叠。

</li>

<li>

一个域中离散，意味着另一个域中周期。

</li>

<li>

离散卷积 $g(n)=\sum_ms(m)h(n-m)$；$h(n)=\operatorname{Tr}\{\delta(n)\}$；稳定：$\sum|h(n)|<\infty$。

</li>

<li>

递归系统 $g(n)=s(n)+bg(n-1)$：$h(n)=b^n\varepsilon(n)$，$H_\mathrm a=\frac{1}{1-b\mathrm{e}^{-\mathrm{j}2\pi f}}$。

</li>

<li>

$S_\mathrm a(f)=\sum s(n)\mathrm{e}^{-\mathrm{j}2\pi nf}$，周期为 1；$s(n)=\int_{-1/2}^{1/2}S_\mathrm a\mathrm{e}^{\mathrm{j}2\pi nf}\mathrm{d} f$。

</li>

<li>

DFT：$S_d(k)=\sum_{n=0}^{M-1}s_d(n)\mathrm{e}^{-\mathrm{j}2\pi kn/M}$，$s_d=\frac1M\sum S_d\mathrm{e}^{\mathrm{j}2\pi kn/M}$；FFT $\approx M\,\mathrm{lb}\,M$；循环卷积 $\leftrightarrow S_dH_d$。

</li>

<li>

降采样使频带伸展（若 $cf_\mathrm g>\frac12$ 则产生混叠），升采样产生频谱镜像。

</li>

<li>

$S(z)=\sum s(n)z^{-n}$；$z^{-n_0}$ $=$ 延时；$H(z)=\frac{\sum a_qz^{-q}}{1-\sum b_pz^{-p}}$；因果且稳定：所有极点都在 $|z|<1$ 内。

</li>

</ul>
:::
