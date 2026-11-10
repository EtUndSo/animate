---
title: 第 11 阶段：二进制接收的误码率
pfad: 电气工程 / 第 3 学期 / ET3 – 电气工程基础 3：信号与系统 / 随机信号
adresse: elektrotechnik/3-semester/signale-und-systeme/zufallssignale
knoten: 第 7 章：随机信号
order: 3271200
summary: 接收机必须作出判决：脉冲发送了没有？它出错的频率有多高？
tags: 
lang: zh
---

<span class="anker" id="stufe-11"></span>

:::zweck
接收机必须作出判决：脉冲发送了没有？它出错的频率有多高？
:::

**思路。** 匹配滤波器输出端的采样值服从高斯分布，方差为 $N$（噪声）；若发送了脉冲，其均值为 $\sqrt{S_a}$，否则为 0。接收机把它与判决门限 $C$ 比较。当噪声把取值推过门限时，就发生错误。两种差错概率就是两条高斯曲线位于门限另一侧的面积：

<span class="anker" id="gl-11-1"></span>
$$P_{e1}=\mathrm{Prob}[y_1\le C]=\tfrac12\operatorname{erfc}\Bigl(\frac{\sqrt{S_a}-C}{\sqrt{2N}}\Bigr),\qquad P_{e0}=\mathrm{Prob}[y_0>C]=\tfrac12\operatorname{erfc}\Bigl(\frac{C}{\sqrt{2N}}\Bigr). \tag{11.1}$$

若两种情况发送得一样频繁，平均误码率（差错概率）为 $\frac12(P_{e1}+P_{e0})$。当门限恰好位于中间，即 $C=\sqrt{S_a}/2$ 时，它最小。采用匹配滤波器（$S_a/N=E_s/N_0$）时：

<span class="anker" id="gl-11-2"></span>
$$P_{e,\min}=\tfrac12\operatorname{erfc}\sqrt{\frac{E_s}{8N_0}}. \tag{11.2}$$

⁠**如何理解：**误码率只取决于 $E_s/N_0$，而且下降得极快：10 dB 时为 $5.7\cdot10^{-2}$，16 dB 时为 $8\cdot10^{-4}$，20 dB 时为 $2.9\cdot10^{-7}$（图 [4](#abb-4)）。只要信号能量多几个分贝，就能把一个无法使用的传输变成几乎无差错的传输。

:::abbildung et3/k7pe 4
采用匹配滤波器的通断键控接收的最小误码率。红点：10 dB、16 dB、20 dB。
:::

:::aufgabe 练习 11 ★★ 误码率
<span class="anker" id="aufg-11"></span>

<ol class="al">

<li>

计算 $E_s/N_0=10$ dB 时的 $P_{e,\min}$。提示：$\operatorname{erfc}(1.118)=0.114$。

</li>

<li>

为什么最佳门限位于 0 与 $\sqrt{S_a}$ 的正中间？若把门限向上移，$P_{e1}$ 和 $P_{e0}$ 会怎样变化？

</li>

</ol>

:::loesung
(a) $E_s/N_0=10$：$\sqrt{10/8}=1.118$，$P_{e,\min}=\frac12\cdot0.114=0.057$。

(b) 两条高斯曲线的宽度相同。两块差错面积之和在两条曲线的交点处最小，由对称性可知交点就在正中间。若把门限向上移，$P_{e0}$ 会变小，但 $P_{e1}$ 增大得更多，因为门限移进了上方那条曲线的密集部分。
:::
:::
