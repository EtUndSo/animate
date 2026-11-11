---
title: 第 11 阶段：傅里叶变换与拉普拉斯变换——存在性的界限
pfad: 电气工程 / 第 3 学期 / ET3 – 电气工程基础 3：信号与系统 / 傅里叶级数与变换
adresse: elektrotechnik/3-semester/signale-und-systeme/fourier-reihe-und-transformation
knoten: 第 3 章：傅里叶级数与变换
order: 3231200
summary: 傅里叶积分在什么情况下存在？它与拉普拉斯变换有什么关系？
tags: 中心极限定理
lang: zh
---

<span class="anker" id="stufe-11"></span>

:::zweck
傅里叶积分在什么情况下存在？它与拉普拉斯变换有什么关系？
:::

存在的一个充分条件是绝对可积，即 $\int|s(t)|\mathrm{d} t<\infty$。拉普拉斯变换先用 $\mathrm{e}^{-\sigma t}$ 加权，从而扩大了可变换信号的范围（[第 2 章](/wissen/zh/elektrotechnik/3-semester/signale-und-systeme/laplace-transformation/laplace-transformation.html)）：

$$S_{\mathcal{L}}(\sigma+\mathrm{j}2\pi f)=\mathcal{F}\bigl\{s(t)\mathrm{e}^{-\sigma t}\bigr\}(f).$$

因此，它从两个方面考察信号：像傅里叶变换一样考察频率分量，同时考察指数增长或衰减。若 $\sigma=0$ 位于收敛域内，傅里叶变换就是虚轴上的拉普拉斯变换。但借助狄拉克冲激（第 [8](singulare-signale-und-linienspektren.html#stufe-8) 阶段），傅里叶变换还能处理拉普拉斯变换处理不了的信号：在全部时间上存在的常数和振荡。一般而言，只要信号的增长不快于 $t$ 的某个幂函数就足够了，更确切地说，只要对某个 $n\ge0$ 有 $\int|s(t)|\,(1+t^2)^{-n}\mathrm{d} t<\infty$。常数、振荡、阶跃和 $t^n$ 都满足这一条件，而像 $\mathrm{e}^{t}\varepsilon(t)$ 这样按指数增长的信号则不满足；它们只能由拉普拉斯变换处理。

:::zusatz 为什么多次卷积会趋于高斯曲线
把 $\operatorname{rect}(t)$ 与自身作 $M$ 重卷积，其频谱为 $\operatorname{si}^M(\pi f)$。对小的 $f$，$\operatorname{si}(\pi f)\approx1-\frac{(\pi f)^2}{6}$，且 $\ln(1+w)\approx w$，因此

$$\operatorname{si}^M(\pi f)=\mathrm{e}^{M\ln\operatorname{si}(\pi f)}\approx\mathrm{e}^{-M(\pi f)^2/6}\;\bullet\!\!-\!\!\circ\;\sqrt{\frac{6}{\pi M}}\,\mathrm{e}^{-6t^2/M}.$$

对大的 $M$，只有小 $f$ 的区域有贡献，近似也就越来越好。$M=4$ 时，$t=0$ 处的精确值为 $0.667$，高斯曲线给出 $0.691$。这是__中心极限定理__（见统计部分）的一个实例：许多相同的、面积有限的正脉冲的卷积趋近于高斯曲线，前提是这些脉冲衰减得足够快，更确切地说，它们的二阶矩 $\int t^2s(t)\,\mathrm{d} t$ 有限。一个例子是由许多短时积分器级联而成的系统的冲激响应。没有这个条件就不成立：练习 [7](die-rechenregeln-theoreme.html#aufg-7) 中的 $\frac{1}{1+t^2}$ 的二阶矩为无穷大，其 $M$ 重卷积（频谱为 $\pi^M\mathrm{e}^{-2\pi M|f|}$）仍是形如 $\frac{1}{1+t^2}$ 的展宽曲线。
:::

:::aufgabe 练习 14 ★★★ （拓展）检验高斯近似
<span class="anker" id="aufg-14"></span>

<ol class="al">

<li>

对 $M=2$，比较精确值 $\Lambda(0)=1$ 与高斯近似。

</li>

<li>

证明高斯曲线 $\sqrt{6/(\pi M)}\,\mathrm{e}^{-6t^2/M}$ 的面积为 1。为什么必然如此？

</li>

</ol>

:::loesung
(a) $M=2$：$\sqrt{6/(2\pi)}=0.977$，而不是 $\Lambda(0)=1$，即偏低 2.3 %。$M=4$ 时：0.691，而不是 0.667，即偏高 3.6 %。因此，即使只卷积几次，高斯曲线就已经接近精确结果。只有对大的 $M$，近似才能任意好，因为只有在这种情况下，频谱中才仅有小的 $f$ 起作用。

(b) $\int\mathrm{e}^{-6t^2/M}\mathrm{d} t=\sqrt{\pi M/6}$；乘以 $\sqrt{6/(\pi M)}$ 得 1。必然如此：卷积的面积等于各面积之积，这里为 $1^M=1$。在频谱中，这就是 $f=0$ 处的值 $\operatorname{si}^M(0)=1$，而近似式 $\mathrm{e}^{-M(\pi f)^2/6}$ 在该处的值也为 1。
:::
:::
