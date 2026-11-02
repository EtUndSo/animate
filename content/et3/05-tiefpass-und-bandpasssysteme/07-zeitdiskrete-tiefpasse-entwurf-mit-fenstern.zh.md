---
title: 第 6 阶段：离散时间低通——窗函数设计法
pfad: 电气工程 / 第 3 学期 / 信号与系统 / 低通与带通系统
order: 3250700
summary: 如何设计数字低通？与因果模拟低通完全一样：取理想低通，加以延迟，再用窗截断。
tags: 
lang: zh
---

<span class="anker" id="stufe-6"></span>

:::zweck
如何设计数字低通？与因果模拟低通完全一样：取理想低通，加以延迟，再用窗截断。
:::

理想离散时间低通具有周期重复的矩形频率响应，其单位脉冲响应为

$$h(n)=2f_\mathrm g\operatorname{si}(2\pi f_\mathrm gn),$$

因此在参考模型中（$f_\mathrm g=0.2$），$h(0)=0.4$，$h(\pm1)=0.303$，$h(\pm2)=0.094$，$h(\pm3)=-0.062$。它同样不是因果的。把它乘以一个有 $2N+1$ 个值的窗 $w(n)$，再平移 $N$，就得到一个具有线性相位的 FIR 滤波器。窗决定了结果（图 [4](#abb-4)）：

<ul>

<li>

⁠**矩形窗：**过渡最陡，但旁瓣高。在参考模型中（$N=10$），从 $f=0.3$ 起的阻带仍高达 $-26.6$ dB，通带波动约 $\pm0.5$ dB。

</li>

<li>

⁠**汉宁窗：**过渡较平缓，但阻带深得多：从 $f=0.3$ 起最高为 $-45.9$ dB，通带平坦度在 $0.05$ dB 以内。

</li>

</ul>

原因与[第 3 部分](/wissen/zh/elektrotechnik/3-semester/signale-und-systeme/fourier-reihe-und-transformation/fourier-reihe-und-transformation.html)中短时傅里叶变换的情形相同：窗的频谱与理想频率响应作卷积，而矩形的硬边沿会产生缓慢衰减的旁瓣。

:::abbildung et3/k5fenster 4
两个 $f_\mathrm g=0.2$、有 21 个系数的 FIR 低通的幅频响应。矩形窗：边沿陡峭，从 $f=0.3$ 起只衰减到 $-26.6$ dB。汉宁窗：边沿较平缓，从 $f=0.3$ 起最高为 $-45.9$ dB。
:::

:::aufgabe 练习 6 ★ 半带滤波器
<span class="anker" id="aufg-6"></span>

计算 $f_\mathrm g=0.25$ 的理想离散时间低通的系数 $h(0)$ 到 $h(3)$。你注意到了什么？为什么这在 FIR 滤波器中可以节省计算量？

:::loesung
$h(n)=0.5\operatorname{si}(\pi n/2)$：$h(0)=0.5$，$h(\pm1)=\frac1\pi=0.318$，$h(\pm2)=0$，$h(\pm3)=-\frac{1}{3\pi}=-0.106$。除 $h(0)$ 外，所有偶数下标的系数都为零，因为对偶数 $n$ 有 $\sin(\pi n/2)=0$。在 FIR 滤波器中，这些乘法可以省去，几乎占全部乘法的一半。
:::
:::
