---
title: 第 7 阶段：高斯分布
pfad: 电气工程 / 第 3 学期 / ET3 – 电气工程基础 3：信号与系统 / 随机信号
adresse: elektrotechnik/3-semester/signale-und-systeme/zufallssignale
knoten: 第 7 章：随机信号
order: 3270800
summary: 为什么噪声常常服从高斯分布？怎样用高斯分布进行计算？
tags: 中心极限定理, 误差函数
lang: zh
---

<span class="anker" id="stufe-7"></span>

:::zweck
为什么噪声常常服从高斯分布？怎样用高斯分布进行计算？
:::

把许多概率密度相互卷积，结果就趋于一条高斯曲线（__中心极限定理__，[第 3 章](/wissen/zh/elektrotechnik/3-semester/signale-und-systeme/fourier-reihe-und-transformation/fourier-reihe-und-transformation.html)）。噪声通常是非常多微小的独立贡献之和，例如许多电子的运动。因此它服从高斯分布。

:::satz 定理 7.1 (高斯（正态）分布)
<span class="anker" id="satz-7-1"></span>

<span class="anker" id="gl-7-1"></span>
$$p_s(x)=\frac{1}{\sqrt{2\pi\sigma_s^2}}\,\mathrm{e}^{-(x-m_s)^2/(2\sigma_s^2)},\qquad P_s(x)=\frac12+\frac12\operatorname{erf}\Bigl(\frac{x-m_s}{\sqrt{2\sigma_s^2}}\Bigr)=\frac12\operatorname{erfc}\Bigl(\frac{m_s-x}{\sqrt{2\sigma_s^2}}\Bigr) \tag{7.1}$$

其中__误差函数__ $\operatorname{erf}(x)=\frac{2}{\sqrt\pi}\int_0^x\mathrm{e}^{-\xi^2}\mathrm{d}\xi$，$\operatorname{erfc}=1-\operatorname{erf}$。
:::

⁠**如何理解：**均值和方差完全确定了高斯分布。在均值周围 $\pm\sigma_s$ 的范围内有 68.3 % 的取值，$\pm2\sigma_s$ 内有 95.4 %，$\pm3\sigma_s$ 内有 99.73 %。高斯曲线的积分没有闭合形式，因此引入函数 erf，它可以查表或用数值方法计算。对于大的 $x$，$\operatorname{erfc}(x)\approx\frac{\mathrm{e}^{-x^2}}{\sqrt\pi\,x}$。

**计算规则。** 两个独立的高斯变量之和仍服从高斯分布，且 $m_s=m_1+m_2$，$\sigma_s^2=\sigma_1^2+\sigma_2^2$。高斯过程通过 LTI 系统后仍是高斯过程，因为卷积积分是一个（无限的）加权和。此外，对于两个联合高斯变量，“不相关”与“独立”是一回事：若归一化互协方差 $\rho=\mu_{sg}/(\sigma_s\sigma_g)$ 为零，联合概率密度就分解为乘积。

:::zusatz 二维高斯概率密度
对于零均值、联合高斯分布、相关系数为 $\rho$ 的 $s,g$，

$$p_{sg}(x,y)=\frac{1}{2\pi\sigma_s\sigma_g\sqrt{1-\rho^2}}\exp\Bigl(-\frac{\sigma_g^2x^2+\sigma_s^2y^2-2\rho\sigma_s\sigma_gxy}{2\sigma_s^2\sigma_g^2(1-\rho^2)}\Bigr).$$

它可以借助归一化的和变量与差变量 $\frac{s}{\sigma_s}\pm\frac{g}{\sigma_g}$ 求得：这两个变量互不相关，方差为 $2(1\pm\rho)$，并且由于服从高斯分布而相互独立。等概率密度线是椭圆；在归一化坐标 $x/\sigma_s$、$y/\sigma_g$ 中，椭圆的轴沿着这些和与差的方向。当 $\rho=0$ 时，它们变为圆（在 $\sigma_s=\sigma_g$ 时），概率密度等于两个单独概率密度的乘积。
:::

:::aufgabe 练习 6 ★ 用高斯分布计算
<span class="anker" id="aufg-6"></span>

一个噪声电压服从高斯分布，$m=0$，$\sigma=1$ mV。

<ol class="al">

<li>

它大于 2 mV 的概率是多少？（提示：$\operatorname{erfc}(1.414)=0.0455$。）

</li>

<li>

把两个这样的独立电压相加。和服从什么分布？

</li>

</ol>

:::loesung
(a) $\mathrm{Prob}[x>2\,\mathrm{mV}]=\frac12\operatorname{erfc}\bigl(\frac{2}{\sqrt2}\bigr)=\frac12\operatorname{erfc}(1.414)=0.023$，即 2.3 %。

(b) 服从高斯分布，$m=0$，$\sigma^2=2$ mV$^2$，$\sigma=1.41$ mV。
:::
:::
