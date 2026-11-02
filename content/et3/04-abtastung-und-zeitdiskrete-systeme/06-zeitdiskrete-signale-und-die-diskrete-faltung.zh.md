---
title: 第 5 阶段：离散时间信号与离散卷积
pfad: 电气工程 / 第 3 学期 / 信号与系统 / 采样与离散时间系统
order: 3240600
summary: 从现在起，所有计算都只使用数值序列 s(n) 。本阶段把卷积、基本信号和 LTI 系统推广到序列。
tags: 离散卷积, 单位脉冲, 移不变, LSI 系统, 单位脉冲响应, 差分, 累加, FIR 滤波器
lang: zh
---

<span class="anker" id="stufe-5"></span>

:::zweck
从现在起，所有计算都只使用数值序列 $s(n)$。本阶段把卷积、基本信号和 LTI 系统推广到序列。
:::

**样本值的卷积。** 若系统的输入 $s$ 和冲激响应 $h$ 都是低通信号，并以奈奎斯特率采样，则二者都可以写成 si 级数 [(3.3)](abtasttheorem-und-ruckgewinnung.html#gl-3-3)。由于 $\operatorname{si}(\pi t/T)*\operatorname{si}(\pi t/T)=T\operatorname{si}(\pi t/T)$（[第 3 部分](/wissen/zh/elektrotechnik/3-semester/signale-und-systeme/fourier-reihe-und-transformation/fourier-reihe-und-transformation.html)），输出的样本值仅由样本值即可求得：

$$g(nT)=T\sum_{m=-\infty}^{\infty}s(mT)\,h\bigl((n-m)T\bigr).$$

归一化到 $T=1$ 后，这就是__离散卷积__：

<span class="anker" id="gl-5-1"></span>
$$g(n)=\sum_{m=-\infty}^{\infty}s(m)\,h(n-m)=s(n)*h(n). \tag{5.1}$$

**基本序列。**

$$\delta(n)=\begin{cases}1&n=0\\0&n\neq0\end{cases},\qquad \varepsilon(n)=\sum_{m=-\infty}^n\delta(m)=\begin{cases}0&n<0\\1&n\ge0\end{cases},\qquad \varepsilon(n)\,a^n,\qquad \mathrm{e}^{\mathrm{j}2\pi Fn}.$$

__单位脉冲__ $\delta(n)$ 是普通的序列，而不是广义函数：它在 $n=0$ 处取值 1。它是离散卷积的单位元，$s(n)*\delta(n)=s(n)$。以 $n=0$ 为中心、由 $2M+1$ 个 1 组成的矩形序列为 $\varepsilon(n+M)-\varepsilon(n-M-1)$。

**线性与移不变。** 若叠加原理成立，则称离散时间系统是线性的；若对每个整数 $m$ 都有 $\operatorname{Tr}\{s(n-m)\}=g(n-m)$，则称它是__移不变__的。同时具有这两个性质的系统称为__LSI 系统__。利用__单位脉冲响应__ $h(n)=\operatorname{Tr}\{\delta(n)\}$，与[第 1 部分](/wissen/zh/elektrotechnik/3-semester/signale-und-systeme/lti-systeme-und-faltung/lti-systeme-und-faltung.html)一样可得

$$g(n)=\operatorname{Tr}\Bigl\{\sum_ms(m)\delta(n-m)\Bigr\}=\sum_ms(m)\operatorname{Tr}\{\delta(n-m)\}=\sum_ms(m)\,h(n-m).$$

这里不需要取极限：序列本身*就是*加权、平移后的单位脉冲之和。

**差分与求和。** 与导数相对应的是__差分__ $g(n)=s(n)-s(n-1)$，因此 $h(n)=\delta(n)-\delta(n-1)$。与积分相对应的是__累加__ $g(n)=\sum_{m\le n}s(m)=s(n)*\varepsilon(n)$。二者相互抵消：$[\delta(n)-\delta(n-1)]*\varepsilon(n)=\varepsilon(n)-\varepsilon(n-1)=\delta(n)$。

**差分方程、FIR 与 IIR。** 描述离散时间系统的不是微分方程，而是差分方程：

<span class="anker" id="gl-5-2"></span>
$$g(n)=\underbrace{\sum_{q=0}^{Q}a_q\,s(n-q)}_{\text{FIR 部分}}+\underbrace{\sum_{p=1}^{P}b_p\,g(n-p)}_{\text{IIR 部分}}. \tag{5.2}$$

输出是以往输入值和输出值的加权和。若输出只取决于输入值（$b_p=0$），单位脉冲响应在 $Q+1$ 个值之后就结束：这是__FIR 滤波器__（finite impulse response，有限长单位脉冲响应）。有反馈时（$b_p\neq0$），单位脉冲响应可以无限长：这是__IIR 滤波器__（infinite impulse response，无限长单位脉冲响应）。二者都由延时单元（存储一个采样周期的存储器）、乘法器和加法器构成（图 [4](#abb-4)）。

:::abbildung et3/k4block 4
一阶系统 $g(n)=a_0s(n)+a_1s(n-1)+b_1g(n-1)$。方框 $T$ 将一个值存储一个采样周期。左边是非递归部分，右边是输出的反馈。
:::

:::aufgabe 练习 4 ★ 手算离散卷积
<span class="anker" id="aufg-4"></span>

将 $s=(1,1,1)$ 与 $h=(1,2)$ 做卷积，二者均从 $n=0$ 开始。结果有多长？为什么？

:::loesung
$g(0)=1$，$g(1)=1\cdot2+1\cdot1=3$，$g(2)=3$，$g(3)=1\cdot2=2$：$(1,3,3,2)$。长度为 $3+2-1=4$：当 $h$ 的最后一个值与 $s$ 的最后一个值相遇时，产生最后一个非零值。
:::
:::
