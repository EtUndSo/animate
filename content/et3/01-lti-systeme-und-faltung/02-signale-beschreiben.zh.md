---
title: 第 1 阶段：信号的描述
pfad: 电气工程 / 第 3 学期 / 信号与系统 / LTI 系统与卷积
order: 3210200
summary: 在研究系统之前，需要一套描述信号的语言：几种基本形状，以及时间轴上的两种运算——平移和展缩。
tags: 信号, 归一化, 周期, 频率
lang: zh
---

<span class="anker" id="stufe-1"></span>

:::zweck
在研究系统之前，需要一套描述信号的语言：几种基本形状，以及时间轴上的两种运算——平移和展缩。
:::

__信号__是某个物理量随时间的变化过程，记作函数 $s(t)$。在系统理论中通常使用__归一化__的量：时间以 1 s 的倍数表示，电压以 1 V 的倍数表示。这样，物理量之间的方程就变成了纯数值之间的方程，写出 $\mathrm{e}^{-t}$ 时也不会有任何单位上的麻烦。

**基本信号。** 有些信号可以用简单的表达式描述，并且反复出现（图 [1](#abb-1)）：

$$\begin{gathered} \sin(2\pi t),\qquad \mathrm{e}^{-\pi t^2}\ \text{（高斯函数）},\qquad \varepsilon(t)=\begin{cases}0&t<0\\1&t\ge0\end{cases},\\ \operatorname{rect}(t)=\begin{cases}1&|t|\le\frac12\\0&|t|>\frac12\end{cases},\qquad \Lambda(t)=\begin{cases}1-|t|&|t|\le1\\0&|t|>1\end{cases}. \end{gathered}$$

阶跃 $\varepsilon(t)$ 和矩形 $\operatorname{rect}(t)$ 都有跳变。跳变点处究竟取什么值，是一种约定。常见的选择是在该处取 $\tfrac12$：这样，首尾相接的矩形之和处处恰好为 1。

:::abbildung et3/k1elementar 1
基本信号。右下：一个经过平移和展缩的矩形，中心位于 $t_0=2$，宽度 $T=2$，高度 $a=0.8$。
:::

**平移与展缩。** 对时间轴进行变换，就可以由一个信号得到新的信号：

<ul>

<li>

⁠**平移：**$t\to t-t_0$。当 $t_0>0$ 时，信号被*延迟* $t_0$，即向右移动。

</li>

<li>

⁠**展缩：**$t\to t/T$。当 $|T|>1$ 时信号变宽，当 $0<|T|<1$ 时信号变窄，当 $T<0$ 时信号还会被反转。

</li>

</ul>

把两者结合起来，再加上幅度 $a$，就可以得到例如矩形脉冲

<span class="anker" id="gl-1-1"></span>
$$s(t)=a\operatorname{rect}\Bigl(\frac{t-t_0}{T}\Bigr)=\begin{cases}a & |t-t_0|\le |T|/2\\ 0 & \text{其他}\end{cases} \tag{1.1}$$

其中心为 $t_0$，持续时间为 $|T|$，高度为 $a$。验证方法：把自变量 $(t-t_0)/T$ 代入 $\operatorname{rect}$ 的定义即可。同样，$\sin(2\pi t/T)=\sin(2\pi Ft)$ 是__周期__为 $T$、__频率__为 $F=1/T$ 的展缩后的正弦。

:::frage 明明是减去了一个量，为什么 $t-t_0$ 会把信号向右移？
新信号在时刻 $t$ 显示的，是旧信号在时刻 $t-t_0$，即*更早*时的值。旧信号做过的一切，新信号都晚 $t_0$ 才做。最简单的检验方法是看一个特征点：$\varepsilon(t-t_0)$ 的跳变沿位于自变量为零处，即 $t=t_0$。
:::

**复指数函数。** 对系统理论而言，最重要的信号是

$$\mathrm{e}^{\mathrm{j}2\pi Ft}=\cos(2\pi Ft)+\mathrm{j}\sin(2\pi Ft).$$

根据欧拉公式，由一对共轭复数可以得到实振荡：

$$\cos(2\pi Ft)=\frac{\mathrm{e}^{\mathrm{j}2\pi Ft}+\mathrm{e}^{-\mathrm{j}2\pi Ft}}{2},\qquad \sin(2\pi Ft)=\frac{\mathrm{e}^{\mathrm{j}2\pi Ft}-\mathrm{e}^{-\mathrm{j}2\pi Ft}}{2\mathrm{j}}.$$

对于振荡，延迟 $t_0$ 表现为相移：

<span class="anker" id="gl-1-2"></span>
$$\cos\bigl(2\pi F(t-t_0)\bigr)=\cos(2\pi Ft+\varphi)=\operatorname{Re}\bigl\{\mathrm{e}^{\mathrm{j}2\pi Ft}\,\mathrm{e}^{\mathrm{j}\varphi}\bigr\},\qquad\varphi=-2\pi Ft_0. \tag{1.2}$$

⁠**简而言之：**对于振荡，延迟等同于相位旋转；对于 $\mathrm{e}^{\mathrm{j}2\pi Ft}$，延迟甚至等同于乘以一个数 $\mathrm{e}^{\mathrm{j}\varphi}$。

:::aufgabe 练习 1 ★ 平移、展缩、相位
<span class="anker" id="aufg-1"></span>

<ol class="al">

<li>

$s(t)=2\operatorname{rect}\bigl(\frac{t-3}{4}\bigr)$ 从哪里开始、到哪里结束？脉冲有多高？

</li>

<li>

写出一个从 $t=1$ s 到 $t=4$ s 高度为 0.5 V 的矩形脉冲。

</li>

<li>

对 $s(t)=\varepsilon(t-1)$，画出 $s(-t)$ 的草图。跳变沿在哪里？

</li>

<li>

一个 $F=50$ Hz 的余弦信号被延迟 $t_0=5$ ms。延迟之后它的相位 $\varphi$ 是多少？

</li>

</ol>

:::loesung
(a) 中心 $t_0=3$，持续时间 $T=4$：从 $t=1$ 到 $t=5$，高度为 2。

(b) 中心 2.5 s，持续时间 3 s：$s(t)=0.5\operatorname{rect}\bigl(\frac{t-2.5}{3}\bigr)$。

(c) $s(-t)=\varepsilon(-t-1)$。跳变沿位于自变量为零处：$-t-1=0$，即 $t=-1$。在自变量 $\ge0$ 处，即 $t\le-1$ 时，函数值为 1。这是一个反转的阶跃：在 $-1$ 左侧为 1，右侧为 0。

(d) $\varphi=-2\pi Ft_0=-2\pi\cdot50\,\mathrm{Hz}\cdot5\,\mathrm{ms}=-\pi/2=-90^\circ$。延迟四分之一周期，就是旋转四分之一圈。
:::
:::
