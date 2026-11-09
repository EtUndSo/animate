---
title: 第 7 阶段：离散时间相关与周期相关
pfad: 电气工程 / 第 3 学期 / 信号与系统 / 相关函数
order: 3260800
summary: 对于样本值，积分变为求和。借助 DFT 可以快速计算相关。
tags: 快速相关
lang: zh
---

<span class="anker" id="stufe-7"></span>

:::zweck
对于样本值，积分变为求和。借助 DFT 可以快速计算相关。
:::

:::satz 定理 7.1 (离散时间相关)
<span class="anker" id="satz-7-1"></span>

<span class="anker" id="gl-7-1"></span>
$$\varphi^E_{sg}(m)=\sum_{n=-\infty}^{\infty}s^*(n)\,g(n+m)=s^*(-m)*g(m),\qquad E_s=\sum_n|s(n)|^2=\int_{-1/2}^{1/2}|S_\mathrm a(f)|^2\,\mathrm{d} f, \tag{7.1}$$

<span class="anker" id="gl-7-2"></span>
$$\varphi^E_{ss}(m)\;\circ\!\!-\!\!\bullet\;|S_\mathrm a(f)|^2\ (\text{周期为}\ 1),\qquad\varphi^E_{gg}(m)=\varphi^E_{ss}(m)*\varphi^E_{hh}(m). \tag{7.2}$$
:::

对于采样后的低通信号，有 $\varphi^E_{sg}(mT)=T\sum_ns^*(nT)g((n+m)T)$ 和 $E_s=T\sum_n|s(nT)|^2$。离散时间能量信号是平方可和的序列。

::::beispiel
$s=(1,2,1)$：当 $m=-2,\dots,2$ 时，$\varphi^E_{ss}=(1,4,6,4,1)$。最大值 $6=E_s$ 位于 $m=0$，偶对称，有五个值而不是三个。在 $f=0$ 处用维纳–辛钦定理验证：$|S_\mathrm a(0)|^2=(1+2+1)^2=16=\sum_m\varphi^E_{ss}(m)$。
::::

**周期相关。** 与卷积的情形一样（[第 4 部分](/wissen/zh/elektrotechnik/3-semester/signale-und-systeme/abtastung-und-zeitdiskrete-systeme/abtastung-und-zeitdiskrete-systeme.html)），对于周期为 $M$ 的序列有：

<span class="anker" id="gl-7-3"></span>
$$\varphi^E_{sgd}(m)=\sum_{n=0}^{M-1}s_d^*(n)\,g_d(n+m)\;\circ\!\!-\!\!\bullet\;S_d^*(k)\,G_d(k). \tag{7.3}$$

用 FFT 来计算时，这称为__快速相关__。为了使周期相关重现普通的相关，$M$ 必须足够大。对于 $(1,2,1)$，取 $M=3$ 得到相互重叠的序列 $(6,5,5)$，而取 $M=5$ 得到 $(6,4,1,1,4)$，即循环排列的普通自相关函数。

**功率信号。** 对于能量无穷大的信号，要取平均：

<span class="anker" id="gl-7-4"></span>
$$\varphi^L_{sg}(\tau)=\lim_{T\to\infty}\frac1T\int_{-T/2}^{T/2}s^*(t)\,g(t+\tau)\,\mathrm{d} t. \tag{7.4}$$

若两个信号都是周期相同的周期信号，取一个周期就足够了，而且相关函数也是周期的。例：$A\cos(2\pi Ft+\varphi_0)$ 的自相关函数为 $\frac{A^2}{2}\cos(2\pi F\tau)$。相位 $\varphi_0$ 消失了，而在 $\tau=0$ 处，自相关函数等于功率 $\frac{A^2}{2}$。

:::aufgabe 练习 6 ★ 离散自相关函数
<span class="anker" id="aufg-6"></span>

<ol class="al">

<li>

手算验证 $(1,2,1)$ 的自相关函数。

</li>

<li>

求 $(1,-1)$ 的自相关函数。$\varphi(\pm1)<0$ 说明该信号有什么特点？

</li>

</ol>

:::loesung
(a) $\varphi(0)=1+4+1=6$，$\varphi(\pm1)=1\cdot2+2\cdot1=4$，$\varphi(\pm2)=1\cdot1=1$。

(b) $\varphi(0)=2$，$\varphi(\pm1)=-1$。时移为 1 时取负值，意味着相邻的值往往符号相反：信号变化很快。与此相符，$|S_\mathrm a(f)|^2=|1-\mathrm{e}^{-\mathrm{j}2\pi f}|^2=2-2\cos(2\pi f)$ 在 $f=0$ 处为零，在 $f=\frac12$ 处最大：这是一个高通信号。
:::
:::

:::aufgabe 练习 7 ★★ 余弦的自相关函数
<span class="anker" id="aufg-7"></span>

利用式 [(7.4)](#gl-7-4)，在一个周期上推导 $A\cos(2\pi Ft+\varphi_0)$ 的自相关函数。为什么 $\varphi_0$ 会消失？这对用自相关函数测量相位意味着什么？

:::loesung
令 $\omega=2\pi F$，并利用 $\cos a\cos b=\frac12[\cos(a-b)+\cos(a+b)]$：

$$\frac1T\int_0^TA^2\cos(\omega t+\varphi_0)\cos(\omega t+\omega\tau+\varphi_0)\mathrm{d} t=\frac{A^2}{2}\cos(\omega\tau)+\frac{A^2}{2T}\int_0^T\cos(2\omega t+\omega\tau+2\varphi_0)\mathrm{d} t.$$

第二个积分跨越两个完整的周期，因此为零。相位 $\varphi_0$ 只是平移了时间原点，而对所有时间取平均并不知道原点在哪里。因此，单个信号的自相关函数无法测量相位。相反，*两个*信号的相位差则由互相关函数显示出来。
:::
:::
