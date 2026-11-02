---
title: 第 12 阶段：离散时间随机信号
pfad: 电气工程 / 第 3 学期 / 信号与系统 / 随机信号
order: 3271300
summary: 上述一切同样适用于随机数序列，只是用求和代替积分。
tags: 离散时间白噪声
lang: zh
---

<span class="anker" id="stufe-12"></span>

:::zweck
上述一切同样适用于随机数序列，只是用求和代替积分。
:::

若以 $T\le\frac{1}{2f_\mathrm g}$ 对一个带限于 $f_\mathrm g$ 的过程采样，样本值就构成一个离散时间过程 $s(n)$。分布、数学期望和相关的定义都与前面相同，只是时间平均变为求和，例如 $\varphi_{ss}(m)=\lim_{M\to\infty}\frac{1}{2M+1}\sum_{n=-M}^{M}s(n)s(n+m)$。通过单位脉冲响应为 $h(n)$ 的 LSI 系统后：

<span class="anker" id="gl-12-1"></span>
$$m_g=m_s\sum_nh(n),\qquad\varphi_{gg}(m)=\varphi_{ss}(m)*\varphi^E_{hh}(m),\qquad\Phi_{gg,\mathrm a}(f)=\Phi_{ss,\mathrm a}(f)\,|H_\mathrm a(f)|^2, \tag{12.1}$$

其中周期功率谱密度为 $\Phi_{ss,\mathrm a}(f)=\sum_m\varphi_{ss}(m)\mathrm{e}^{-\mathrm{j}2\pi fm}$，且 $L_s=\int_{-1/2}^{1/2}\Phi_{ss,\mathrm a}\mathrm{d} f$。__离散时间白噪声__ 满足 $\Phi_{ss,\mathrm a}=N$ 和 $\varphi_{ss}(m)=N\delta(m)$：相继的数互不相关。与连续时间的情形不同，它的功率是有限的，$L_s=N$。

**例 1：对两个值取平均。** 均匀分布的白噪声（$\sigma_s^2=\frac1{12}$）通过 $h(n)=\frac12[\delta(n)+\delta(n-1)]$，即 $g(n)=\frac12[s(n)+s(n-1)]$。利用 $\varphi^E_{hh}=\frac14\delta(m+1)+\frac12\delta(m)+\frac14\delta(m-1)$：

$$\varphi_{gg}(m)=\tfrac{\sigma_s^2}{4}\delta(m+1)+\tfrac{\sigma_s^2}{2}\delta(m)+\tfrac{\sigma_s^2}{4}\delta(m-1).$$

方差减半为 $\frac{1}{24}$，而且相邻的输出值现在是相关的（它们共用一个输入值）。输出值服从三角分布，因为每个输出值都是两个独立的均匀分布数之和的一半。用 200,000 个数进行模拟，得到的方差为 0.0415，理论值为 $\frac1{24}=0.0417$。

**例 2：递归滤波器（AR(1) 过程，即一阶自回归过程）。** 方差为 $\sigma_s^2$ 的白噪声通过 $h(n)=b^n\varepsilon(n)$（[第 4 部分](/wissen/zh/elektrotechnik/3-semester/signale-und-systeme/abtastung-und-zeitdiskrete-systeme/abtastung-und-zeitdiskrete-systeme.html)）。利用 $\varphi^E_{hh}(m)=\sum_kb^kb^{k+|m|}=\frac{b^{|m|}}{1-b^2}$：

<span class="anker" id="gl-12-2"></span>
$$\varphi_{gg}(m)=\frac{\sigma_s^2}{1-b^2}\,b^{|m|},\qquad\Phi_{gg,\mathrm a}(f)=\frac{\sigma_s^2}{1-2b\cos(2\pi f)+b^2}. \tag{12.2}$$

当 $b=0.6$ 时，输出方差是输入方差的 $1.56$ 倍，相邻值的相关系数为 $0.6$。$b$ 越接近 1，低频分量就越强（图 [5](#abb-5)）。

:::abbildung et3/k7ar 5
AR(1) 过程的功率谱密度，以 1 为周期。$b=0.6$ 时其值从 6.25（$f=0$）变化到 0.39（$f=\frac12$），$b=0.9$ 时从 100 变化到 0.28。
:::

:::aufgabe 练习 12 ★★ AR(1) 过程
<span class="anker" id="aufg-12"></span>

均匀分布的白噪声（$\sigma_s^2=\frac1{12}$）通过 $g(n)=s(n)+0.6\,g(n-1)$。

<ol class="al">

<li>

计算输出方差和 $\varphi_{gg}(1)/\varphi_{gg}(0)$。

</li>

<li>

利用几何级数推导 $\varphi^E_{hh}(m)=\frac{b^{|m|}}{1-b^2}$。

</li>

<li>

输出还是均匀分布的吗？你大致预期是什么分布？为什么？

</li>

</ol>

:::loesung
(a) $\sigma_g^2=\frac{1/12}{1-0.36}=0.130$，$\varphi_{gg}(1)/\varphi_{gg}(0)=b=0.6$。模拟结果为 0.130 和 0.600。

(b) 当 $m\ge0$ 时：$\sum_{k\ge0}b^kb^{k+m}=b^m\sum_kb^{2k}=\frac{b^m}{1-b^2}$。单位脉冲响应的自相关函数是偶函数，因此一般地有 $b^{|m|}$。

(c) 不再是均匀分布：每个输出值都是许多独立输入值的加权和，$g(n)=\sum_kb^ks(n-k)$。根据中心极限定理，它近似服从高斯分布。当 $b=0.6$ 时，只有少数几项有明显贡献，因此这种近似比较粗略，但分布已经明显呈钟形。
:::
:::
