---
title: 信号、LTI 系统与卷积
pfad: 电气工程 / 第 3 学期 / 信号与系统 / LTI 系统与卷积
order: 3210100
summary: 为什么对单个冲激的响应 能够描述整个系统
tags: 信号, 归一化, 周期, 频率, 系统, 变换, 线性, 时不变
lang: zh
---

## 本文内容

系统接收一个信号，输出另一个信号：RC 电路使电压变得平滑，音箱箱体给声音染上音色，测量放大器对信号进行延迟和放大。本文要回答的问题是：**要对任意输入信号算出系统的输出，需要知道系统的哪些信息？**

对于线性时不变（LTI）系统这一大类系统，答案出奇地简短：只需知道系统对单个无限短冲激的响应。把这一个响应变成其他所有响应的工具，就是卷积。

:::merke 三句话的答案（读完本文后应觉得理所当然）
<ol>

<li>

每个信号都是无穷多个短冲激的叠加：在每个时刻 $\tau$ 都有一个权重为 $s(\tau)\,\mathrm{d}\tau$ 的冲激。

</li>

<li>

LTI 系统对平移后的冲激的响应是平移后的冲激响应 $h(t-\tau)$（时不变性），对冲激之和的响应是各响应之和（线性）。

</li>

<li>

因此，输出就是卷积 $g(t)=\int s(\tau)\,h(t-\tau)\,\mathrm{d}\tau$，而 $h(t)$ 完整地描述了该系统。

</li>

</ol>
:::

**所有结论背后的同一个原理。** 下表把本文的每一项结论都归结到“分解、让一个基本单元通过系统、再合成”这一原理上。

| 结论 | 来源 |
|---|---|
| 卷积积分 | 叠加冲激，叠加平移后的冲激响应（第 [4](#stufe-4) 阶段） |
| 计算时的反转 | $h(t-\tau)$ 是对 $t-\tau$ 秒之前到达的冲激的响应（第 [5](#stufe-5) 阶段） |
| $\delta$ 是单位元 | 由冲激组成的信号，通过一个使每个冲激都保持不变的系统（第 [6](#stufe-6) 阶段） |
| 交换律、结合律、分配律 | 互换角色、系统级联、系统并联（第 [6](#stufe-6) 阶段） |
| 筛选性质、狄拉克冲激的尺度变换 | $\delta$ 仅通过其面积来定义（第 [7](#stufe-7) 阶段） |
| 阶跃响应 $=$ 冲激响应的积分 | 阶跃是到 $t$ 为止所有冲激之和（第 [8](#stufe-8) 阶段） |
| 因果性、稳定性 | 对 $h(t)$ 的条件：冲激到来之前为零，$\vert h\vert $ 的面积有限（第 [9](#stufe-9) 阶段） |
| 没有系统的卷积 | 同样的叠加，例如两个骰子的点数之和（第 [10](#stufe-10) 阶段） |

**如何使用本文。**每个阶段包括基本思路、可展开解答的典型问题以及练习（★ 到 ★★★）。请先自己尝试，解答可在每道练习下方展开。

:::merke 本文的参考模型
<ul>

<li>

⁠**RC 低通滤波器**，$T=RC=1$ s（例如 $R=1\,\mathrm{M}\Omega$，$C=1\,\mu\text{F}$）。时间以 s 为单位，电压以 V 为单位，因此所有计算都是无量纲的。

</li>

<li>

⁠**矩形脉冲**：高度 $a=1$ V，持续时间 $T_0=1$ s，从 $t=0$ 开始。

</li>

</ul>

脚本 `rechnung_kap1.py` 可复算这些数值和曲线。
:::

## 第 1 阶段：信号的描述

<span class="anker" id="stufe-1"></span>

:::zweck
在研究系统之前，需要一套描述信号的语言：几种基本形状，以及时间轴上的两种运算——平移和展缩。
:::

__信号__是某个物理量随时间的变化过程，记作函数 $s(t)$。在系统理论中通常使用__归一化__的量：时间以 1 s 的倍数表示，电压以 1 V 的倍数表示。这样，物理量之间的方程就变成了纯数值之间的方程，写出 $\mathrm{e}^{-t}$ 时也不会有任何单位上的麻烦。

**基本信号。** 有些信号可以用简单的表达式描述，并且反复出现（图 [1](#abb-1)）：

$$\begin{gathered} \sin(2\pi t),\qquad \mathrm{e}^{-\pi t^2}\ \text{（高斯函数）},\qquad \varepsilon(t)=\begin{cases}0&t<0\\1&t\ge0\end{cases},\\ \operatorname{rect}(t)=\begin{cases}1&|t|\le\frac12\\0&|t|>\frac12\end{cases},\qquad \Lambda(t)=\begin{cases}1-|t|&|t|\le1\\0&|t|>1\end{cases}. \end{gathered}$$

阶跃 $\varepsilon(t)$ 和矩形 $\operatorname{rect}(t)$ 都有跳变。跳变点处究竟取什么值，是一种约定。常见的选择是在该处取 $\tfrac12$：这样，首尾相接的矩形之和处处恰好为 1。

:::abbildung et3/k1elementar
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

⁠**简而言之：**对于振荡，延迟等同于相位旋转；对于 $\mathrm{e}^{\mathrm{j}2\pi Ft}$，延迟甚至等同于乘以一个数 $\mathrm{e}^{\mathrm{j}\varphi}$。在[第 2 部分](/wissen/zh/elektrotechnik/3-semester/signale-und-systeme/laplace-transformation/laplace-transformation.html)中，整个拉普拉斯变换都建立在这一性质之上。

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

## 第 2 阶段：第一个系统——RC 电路

<span class="anker" id="stufe-2"></span>

:::zweck
RC 低通滤波器（图 [2](#abb-2)）已经在小范围内展现了本文的全部思想：复指数函数通过它之后只是乘上了一个数；而对于阶跃输入，电路以一条指数曲线作为响应。
:::

**微分方程。** 流过 $R$ 的电流为 $(u_1-u_2)/R$。这一电流全部流入电容并为其充电，$C\,\dot u_2=(u_1-u_2)/R$。整理得：

<span class="anker" id="gl-2-1"></span>
$$RC\,\frac{\mathrm{d} u_2}{\mathrm{d} t}+u_2=u_1. \tag{2.1}$$

:::abbildung et3/k1rcschaltung
RC 低通滤波器：输入为 $u_1$，输出为电容两端的电压 $u_2$。参考模型中 $RC=1$ s。
:::

**输入 $\mathrm{e}^{\mathrm{j}2\pi Ft}$：输出等于一个数乘以输入。** 若施加 $u_1=\mathrm{e}^{\mathrm{j}2\pi Ft}$，则稳态时输出具有相同的形式，只是幅度和相位不同：$u_2=H(F)\,\mathrm{e}^{\mathrm{j}2\pi Ft}$。原因在于求导不改变函数的形式，$\frac{\mathrm{d}}{\mathrm{d} t}\mathrm{e}^{\mathrm{j}2\pi Ft}=\mathrm{j}2\pi F\,\mathrm{e}^{\mathrm{j}2\pi Ft}$。代入式 [(2.1)](#gl-2-1)：

$$H(F)\,\mathrm{e}^{\mathrm{j}2\pi Ft}\,(1+\mathrm{j}2\pi FRC)=\mathrm{e}^{\mathrm{j}2\pi Ft}\quad\Longrightarrow\quad H(F)=\frac{1}{1+\mathrm{j}2\pi FRC}.$$

用相量法进行交流分析，也会得到同样的结果：电容的阻抗为 $1/(\mathrm{j}2\pi FC)$，电路是一个分压器，

$$\underline U_2=\frac{1/(\mathrm{j}2\pi FC)}{R+1/(\mathrm{j}2\pi FC)}\,\underline U_1=\frac{1}{1+\mathrm{j}2\pi FRC}\,\underline U_1.$$

相量所对应的实际电压为 $u(t)=\operatorname{Re}\{\sqrt2\,|\underline U|\,\mathrm{e}^{\mathrm{j}(2\pi Ft+\varphi)}\}=\sqrt2\,|\underline U|\cos(2\pi Ft+\varphi)$（有效值相量）。

:::satz 定理 2.1 (RC 低通滤波器的传递函数（频率响应）)
<span class="anker" id="satz-2-1"></span>

令 $x=2\pi FRC$，则

<span class="anker" id="gl-2-2"></span>
<span class="anker" id="gl-2-3"></span>
$$\begin{aligned} \operatorname{Re}\{H\}&=\frac{1}{1+x^2},\qquad \operatorname{Im}\{H\}=\frac{-x}{1+x^2},\\ |H(F)|&=\sqrt{\operatorname{Re}\{H\}^2+\operatorname{Im}\{H\}^2}=\sqrt{H\,H^*}=\frac{1}{\sqrt{1+x^2}},\qquad \varphi(F)=-\arctan x. \end{aligned} \tag{2.2|2.3}$$
:::

⁠**如何理解：**$|H|$ 表明幅度按多大的因子缩小，$\varphi$ 表明振荡滞后多大的角度。在 $x=1$ 处，即参考模型中 $F=1/(2\pi RC)=0.16$ Hz 时，$|H|=0.707$，$\varphi=-45^\circ$。在 $x=10$ 处，$|H|=0.0995$，$\varphi=-84.3^\circ$（图 [3](#abb-3)）。**极限情况：**$F\to0$ 时 $H\to1$（电容有足够的时间充满电）；$F\to\infty$ 时 $H\to0$，且 $\varphi\to-90^\circ$（电容相当于短路）。

:::abbildung et3/k1bode
RC 低通滤波器传递函数的幅值和相位随 $x=2\pi FRC$ 的变化（对数坐标）。慢的振荡几乎不变地通过；快的振荡被衰减，并且滞后最多可达 $90^\circ$。
:::

**一般情况下的相位。** 对任意复数 $H=\operatorname{Re}\{H\}+\mathrm{j}\operatorname{Im}\{H\}$，有

<span class="anker" id="gl-2-4"></span>
$$\varphi=\arctan\frac{\operatorname{Im}\{H\}}{\operatorname{Re}\{H\}}+\lambda\pi+l\cdot2\pi,\qquad \lambda=\begin{cases}0&\operatorname{Re}\{H\}\ge0\\1&\operatorname{Re}\{H\}<0\end{cases},\quad l\ \text{为整数}, \tag{2.4}$$

其中 $\arctan$ 取 $[-\pi/2,\pi/2]$ 内的主值。

:::frage 为什么相位公式需要附加项 $\lambda\pi$？
$\arctan$ 只看比值 $\operatorname{Im}/\operatorname{Re}$。$1+\mathrm{j}$ 和 $-1-\mathrm{j}$ 这两个数的比值同为 1，却位于相对的两个象限。$\arctan1=45^\circ$ 对 $1+\mathrm{j}$ 是正确的。而对 $-1-\mathrm{j}$，真正的角度是 $45^\circ+180^\circ=225^\circ$，等价于 $-135^\circ$（取 $l=-1$）。只要实部为负，就必须加上 $\pi$。
:::

**阶跃输入：指数曲线。** 在 $t=0$ 时施加电压 $u_1=1$ V，此时电容未充电。对 $t\ge0$，用电流 $i$ 表示，由基尔霍夫电压定律得

$$1=R\,i(t)+\frac1C\int_0^ti(\tau)\,\mathrm{d}\tau.$$

求导得 $0=R\,\frac{\mathrm{d} i}{\mathrm{d} t}+\frac iC$，因此 $\frac{\mathrm{d} i}{i}=-\frac{\mathrm{d} t}{RC}$，积分得

$$\ln|i|=-\frac{t}{RC}+K\quad\Longrightarrow\quad i(t)=A\,\mathrm{e}^{-t/RC},\qquad A=i(0)=\frac1R,$$

因为在最初瞬间，全部电压都加在 $R$ 上。再由基尔霍夫电压定律 $u_2=1-R\,i$ 得到

<span class="anker" id="gl-2-5"></span>
$$u_2(t)=1-\mathrm{e}^{-t/RC}\qquad(t\ge0). \tag{2.5}$$

其机理是：电容充得越满，留给 $R$ 的电压就越小，充电电流就越小，电容继续充电也就越慢。正是这种反馈使曲线呈指数形式。

:::ltspice RC 低通滤波器：阶跃响应与频率响应
⁠**绘制：**电压源 `voltage` 接在节点 `in` 上，`res` 取 `1Meg`，从 `in` 接到 `out`，`cap` 取 `1u`，从 `out` 接地，因此 $RC=1$ s。注意：SPICE 把 `1M` 读作 1 毫（milli）；兆要写成 `Meg`。

⁠**阶跃：**信号源取 `PULSE(0 1 0 1u 1u 100)`，指令为 `.tran 5`。像 `.meas tran g1 FIND V(out) AT=1` 这样的测量语句可以给出精确值；结果显示在 SPICE Error Log 中（View，SPICE Error Log）。预期结果：0.5 s 时为 0.393，1 s 时为 0.632，3 s 时为 0.950，即式 [(2.5)](#gl-2-5) 中的 $1-\mathrm{e}^{-t}$。

⁠**频率响应：**信号源的值取 `AC 1`，并用指令 `.ac dec 100 0.01 100` 代替 `.tran`。LTspice 画出以 dB 表示的幅值（实线）和相位（虚线）。在 0.159 Hz（$x=1$）处，它们显示 $-3.0$ dB（即 $|H|=0.707$）和 $-45^\circ$。把 $x=10$ 处的值与你在练习 [2](#aufg-2)(a) 中的结果比较。
:::

:::aufgabe 练习 2 ★★ 频率响应与相位
<span class="anker" id="aufg-2"></span>

<ol class="al">

<li>

计算 RC 低通滤波器在 $x=0$、$1$ 和 $10$ 时的 $|H|$ 和 $\varphi$。在参考模型中，$x=10$ 对应多少 Hz 的频率？

</li>

<li>

施加信号 $u_1(t)=\cos(2\pi Ft)$，其中 $x=1$。写出 $u_2(t)$。若 $RC=1$ s，$u_2$ 滞后多少秒？

</li>

<li>

用式 [(2.4)](#gl-2-4) 求 $-1-\mathrm{j}$、$-\mathrm{j}$ 和 $-2$ 的相位。

</li>

</ol>

:::loesung
(a) $x=0$：$|H|=1$，$\varphi=0$。$x=1$：$|H|=0.707$，$\varphi=-45^\circ$。$x=10$：$|H|=0.0995$，$\varphi=-84.3^\circ$。$x=10$ 意味着 $F=10/(2\pi RC)=1.59$ Hz。

(b) $u_2(t)=0.707\cos(2\pi Ft-45^\circ)$，其中 $2\pi F=1/\mathrm s$，即 $F=0.159$ Hz。它滞后 $t_0=-\varphi/(2\pi F)=(\pi/4)/(1/\mathrm s)=0.785$ s。

(c) $-1-\mathrm{j}$：$\arctan1=45^\circ$，实部为负，因此加上 $180^\circ$：得 $225^\circ$，等价于 $-135^\circ$。$-\mathrm{j}$：实部为零，虚部为负；$\arctan(\operatorname{Im}/\operatorname{Re})$ 趋于 $-90^\circ$，所以相位为 $-90^\circ$。$-2$：$\arctan0=0$，实部为负，因此相位为 $180^\circ$。
:::
:::

## 第 3 阶段：什么是 LTI 系统

<span class="anker" id="stufe-3"></span>

:::zweck
RC 电路具有两个性质，其余一切都建立在这两个性质之上：它是线性的，并且是时不变的。本阶段给出这两个性质的定义，并说明它们使什么成为可能。
:::

__系统__把输入信号对应到一个输出信号：

$$g(t)=\operatorname{Tr}\{s(t)\}.$$

这种从函数到函数的映射称为__变换__。它并不是把一个数值映射为另一个数值：时刻 $t$ 的输出可以取决于输入在过去的整个变化过程。在 RC 电路中，$u_2(t)$ 取决于到时刻 $t$ 为止积累了多少电荷。

:::definition 定义 3.1 (LTI 系统)
<span class="anker" id="satz-3-1"></span>

称一个系统为

<ul>

<li>

__线性__系统，如果对任意常数 $a_i$ 叠加原理都成立：

<span class="anker" id="gl-3-1"></span>
$$\operatorname{Tr}\Bigl\{\sum_ia_is_i(t)\Bigr\}=\sum_ia_i\operatorname{Tr}\{s_i(t)\}=\sum_ia_ig_i(t); \tag{3.1}$$

</li>

<li>

__时不变__系统，如果对任意平移量 $t_0$ 都有

<span class="anker" id="gl-3-2"></span>
$$\operatorname{Tr}\{s(t-t_0)\}=g(t-t_0). \tag{3.2}$$

</li>

</ul>

既线性又时不变的系统简称为__LTI 系统__（LTI 即 linear time-invariant，线性时不变）。
:::

在 RC 电路中，线性来自这样一个事实：微分方程 [(2.1)](#gl-2-1) 中既不含 $u_1$ 与 $u_2$ 的乘积，也不含它们的平方。时不变性则来自 $R$ 和 $C$ 不随时间变化。所有由 $R$、$L$、$C$ 组成的网络都可以用常系数线性微分方程来描述。但并非每个 LTI 系统都如此：例如第 [7](#stufe-7) 阶段中的理想延时器就没有这样的方程。

**这两个性质带来了什么。** 如果已知系统对矩形脉冲 $s_0$ 的响应 $g_0$，那么无需进一步计算，就能知道系统对任意多个经过平移和缩放的矩形脉冲之和的响应。图 [4](#abb-4) 以 $s(t)=s_0(t)+0.5\,s_0(t-2)$ 为例展示了这一点：输出为 $g_0(t)+0.5\,g_0(t-2)$。

:::abbildung et3/k1doppel
左：矩形 $s_0$（高度 1 V，持续时间 1 s）及 RC 电路的响应 $g_0$。右：一对脉冲。响应（红色）是 $g_0(t)$ 与经过平移、减半的副本 $0.5\,g_0(t-2)$（虚线）之和。
:::

:::frage $g(t)=2s(t)+1$ 是线性的吗？它的特性曲线毕竟是一条直线啊。
不是。对于线性系统，零输入必须产生零输出：在式 [(3.1)](#gl-3-1) 中令所有 $a_i=0$，就得到 $\operatorname{Tr}\{0\}=0$。而这里 $\operatorname{Tr}\{0\}=1$。叠加原理同样不成立：两个输入分别作用时，输出之和为 $2s_1+2s_2+2$；而两者同时作用时，输出为 $2s_1+2s_2+1$。不经过原点的直线称为*仿射*的，而不是线性的。
:::

:::ltspice 验证叠加性：两个矩形
⁠**绘制：**第 [2](#stufe-2) 阶段中的 RC 电路，但用两个串联的电压源 `voltage`：`V1` 负端接地、正端接节点 `a`，值为 `PULSE(0 {a1} 0 1u 1u 1)`；在它上面串接 `V2`，从 `a` 接到 `in`，值为 `PULSE(0 {a2} 2 1u 1u 1)`。串联时电压相加，因此 RC 电路得到的输入是 $a_1s_0(t)+a_2s_0(t-2)$。

⁠**指令：**`.param a1=1 a2=0.5`，`.step param a1 list 0 1`，`.step param a2 list 0 0.5`，`.tran 0 6 0 1m`。LTspice 运行全部四种组合，并把结果叠画在一起。

⁠**你会看到：**曲线 $0$、$g_0(t)$、$0.5\,g_0(t-2)$ 以及它们的和，与图 [4](#abb-4) 相同。在 $t=2.5$ s 处：$0.141+0.197=0.338$。输入之和给出响应之和（线性），平移 2 s 的信号源给出平移 2 s 的曲线（时不变性）。
:::

:::aufgabe 练习 3 ★ 是不是 LTI？
<span class="anker" id="aufg-3"></span>

检验下列各系统是否线性、是否时不变： (a) $g(t)=3\,s(t-2)$， (b) $g(t)=s(t)^2$， (c) $g(t)=s(t)+1$， (d) $g(t)=t\,s(t)$， (e) $g(t)=s(2t)$， (f) $g(t)=\int_{-\infty}^ts(\tau)\,\mathrm{d}\tau$。

:::loesung
(a) 线性且时不变（增益为 3，延迟为 2）：LTI。 (b) 非线性：$\operatorname{Tr}\{2s\}=4s^2\neq2s^2$。时不变。 (c) 非线性（仿射，$\operatorname{Tr}\{0\}=1$）。时不变。 (d) 线性。不是时不变的：$\operatorname{Tr}\{s(t-t_0)\}=t\,s(t-t_0)$，但 $g(t-t_0)=(t-t_0)\,s(t-t_0)$。因子 $t$ 是一个随时间变化的元件。 (e) 线性。不是时不变的：$\operatorname{Tr}\{s(t-t_0)\}=s(2t-t_0)$，但 $g(t-t_0)=s(2t-2t_0)$。压缩时间的同时，也压缩了每一次平移。 (f) LTI。线性，因为积分是线性的。时不变：$\int_{-\infty}^ts(\tau-t_0)\mathrm{d}\tau=\int_{-\infty}^{t-t_0}s(\vartheta)\mathrm{d}\vartheta=g(t-t_0)$。它的冲激响应为 $\varepsilon(t)$（第 [8](#stufe-8) 阶段）。
:::
:::

## 第 4 阶段：卷积积分

<span class="anker" id="stufe-4"></span>

:::zweck
借助线性和时不变性，可以由系统对单个短脉冲的响应，算出它对*任意*信号的响应。其结果就是卷积积分。
:::

**思路（分四步）。**

<ol>

<li>

⁠**分解。**用宽度为 $T_0$ 的窄矩形组成的阶梯来近似输入信号。基本单元是持续时间为 $T_0$、高度为 $1/T_0$，即面积为 1 的矩形 $s_0(t)$。位于 $nT_0$ 处的台阶，就是把这个基本单元平移 $nT_0$，再乘以权重 $s(nT_0)\,T_0$（即该窄条的面积）：

$$s(t)\approx s_a(t)=\sum_{n=-\infty}^{\infty}s(nT_0)\,s_0(t-nT_0)\,T_0.$$

</li>

<li>

⁠**让一个基本单元通过系统。**系统对 $s_0$ 的响应为 $g_0(t)$。这个响应需要知道，但只需知道一次。

</li>

<li>

⁠**再合成。**时不变性：平移后的基本单元产生平移后的响应。线性：权重和求和都原样传递到输出。因此

$$g_a(t)=\sum_{n=-\infty}^{\infty}s(nT_0)\,g_0(t-nT_0)\,T_0\approx g(t).$$

</li>

<li>

⁠**取极限 $T_0\to0$。**阶梯变成信号本身。面积为 1 的矩形变成__狄拉克冲激__（$\delta$ 函数）$\delta(t)$，即面积为 1 的无限短冲激（第 [7](#stufe-7) 阶段）。系统对它的响应称为__冲激响应__ $h(t)$。$nT_0$ 变为连续变量 $\tau$，$T_0$ 变为微分 $\mathrm{d}\tau$，求和变为积分。

</li>

</ol>

:::abbildung et3/k1treppe
上：三角脉冲 $s(t)=\Lambda(t-1)$ 及其 $T_0=0.5$ s 的阶梯近似。下：RC 电路的精确响应，以及平移后的各矩形响应之和。最大偏差从 0.17（$T_0=0.5$ s）降到 0.08（$0.25$ s）和 0.03（$0.1$ s）。
:::

:::satz 定理 4.1 (卷积积分)
<span class="anker" id="satz-4-1"></span>

每个信号 $s(t)$ 都满足

<span class="anker" id="gl-4-1"></span>
$$s(t)=\int_{-\infty}^{\infty}s(\tau)\,\delta(t-\tau)\,\mathrm{d}\tau, \tag{4.1}$$

冲激响应为 $h(t)$ 的 LTI 系统对它的响应为

<span class="anker" id="gl-4-2"></span>
$$g(t)=\int_{-\infty}^{\infty}s(\tau)\,h(t-\tau)\,\mathrm{d}\tau. \tag{4.2}$$
:::

⁠**如何理解：**$\tau$ 是某个输入冲激出现的时刻，$s(\tau)\,\mathrm{d}\tau$ 是它的权重（窄条的面积）。$h(t-\tau)$ 是系统在时刻 $t$ 对一个在时刻 $\tau$、即 $t-\tau$ 秒之前到达的冲激的响应。输出汇集了过去所有的冲激，每个冲激的权重取决于系统在经过这段时间之后对它还“记得”多少。该式是精确的，对每个 LTI 系统都成立。

⁠**简而言之：**LTI 系统的输出是其冲激响应的叠加：冲激响应被平移到输入的每一个时刻，并以该时刻的输入值加权。

:::frage 为什么矩形基本单元的面积必须为 1？
这样，基本单元的响应在取极限时才能保持确定的形状。高度固定为 1 的矩形，在 $T_0\to0$ 时面积趋于零，它的响应也会消失。高度取 $1/T_0$ 时，面积保持为 1，响应趋于 $h(t)$。对于 RC 电路，响应的峰值为 $(1-\mathrm{e}^{-T_0})/T_0$：$T_0=1$ s 时为 0.632，0.5 s 时为 0.787，0.1 s 时为 0.952；当 $T_0\to0$ 时，它变为 $1=h(0^+)$。在这一过程中，响应的面积始终为 1。
:::

:::frage 冲激 $\delta(t)$ 在现实中存在吗？如果不存在，我该怎样测量 $h(t)$？
无限短的冲激并不存在。但任何远短于系统时间常数的脉冲都可以胜任。此时系统只感受到它的面积，响应实际上就是 $(\text{面积})\cdot h(t)$。对于 $RC=1$ s 的 RC 电路，它对 1 ms 脉冲的响应峰值与 $h(0^+)$ 只相差 0.05 %。冲激响应实际上也是这样测量的：在房间里拍一下手，录下混响。
:::

:::ltspice 用短矩形近似冲激响应
⁠**绘制：**第 [2](#stufe-2) 阶段中的 RC 电路，信号源取 `PULSE(0 {1/T0} 0 1n 1n {T0})`：宽度为 $T_0$、高度为 $1/T_0$ 的矩形，因此面积为 1。

⁠**指令：**`.param T0=1`，`.step param T0 list 1 0.5 0.1 1m`，`.tran 0 10 0 1m`，`.meas tran peak MAX V(out)`，`.meas tran area INTEG V(out)`。

⁠**你会看到：**峰值依次为 0.632、0.787、0.952 和 0.9995，与 $(1-\mathrm{e}^{-T_0})/T_0$ 给出的一致。对 1 ms 的脉冲，响应实际上已经就是 $h(t)=\mathrm{e}^{-t}$。四次运行的面积都是 1.000：远短于 $RC$ 的脉冲只通过它的面积起作用。
:::

:::aufgabe 练习 4 ★★ 细看阶梯近似
<span class="anker" id="aufg-4"></span>

<ol class="al">

<li>

计算 RC 电路（$RC=1$ s）对从 $0$ 到 $T_0$、高度为 $1/T_0$ 的矩形的响应 $g_0(t)$。为此，利用式 [(2.5)](#gl-2-5)，并把矩形写成两个阶跃之差。

</li>

<li>

证明 $g_0(T_0)=(1-\mathrm{e}^{-T_0})/T_0$，并证明当 $T_0\to0$ 时它趋于 1。

</li>

<li>

为什么图 [5](#abb-5) 中的近似 $g_a$ 来得太晚？（提示：在上升沿和下降沿上，台阶分别位于三角形的什么位置？）

</li>

</ol>

:::loesung
(a) 该矩形为 $\frac{1}{T_0}[\varepsilon(t)-\varepsilon(t-T_0)]$。由线性和时不变性，结合阶跃响应 [(2.5)](#gl-2-5)，得

$$g_0(t)=\frac{1}{T_0}\Bigl[\bigl(1-\mathrm{e}^{-t}\bigr)\varepsilon(t)-\bigl(1-\mathrm{e}^{-(t-T_0)}\bigr)\varepsilon(t-T_0)\Bigr].$$

(b) 在 $t=T_0$ 处第二项为零：$g_0(T_0)=(1-\mathrm{e}^{-T_0})/T_0$。对于小的 $T_0$，利用 $\mathrm{e}^{-T_0}\approx1-T_0+T_0^2/2$，得到 $\approx1-T_0/2\to1=h(0^+)$。数值：$T_0=1$、0.5 和 0.1 s 时分别为 0.632、0.787 和 0.952。

(c) 每个台阶从其区间的*起点*到终点都保持值 $s(nT_0)$。因此，在上升沿上阶梯位于三角形下方，在下降沿上则位于其上方：平均而言，阶梯延迟了 $T_0/2$。输出继承了这一延迟；在下降段，$g_a$ 位于 $g$ 的上方（$T_0=0.5$ s 时，$g_a(2)=0.508$，而不是 $0.400$）。$T_0$ 越小，延迟越小，误差也随之减小。
:::
:::

## 第 5 阶段：卷积的计算

<span class="anker" id="stufe-5"></span>

:::zweck
对于具体的信号，需要把积分 [(4.2)](#gl-4-2) 算出来。关键在于把两个因子都画成积分变量 $\tau$ 的函数。
:::

**计算步骤。** 对固定的时刻 $t$：

<ol>

<li>

以 $\tau$ 为横轴画出 $s(\tau)$。

</li>

<li>

画出 $h(-\tau)$：把 $h$ 关于纵轴*反转*。

</li>

<li>

$h(t-\tau)$：把反转后的 $h$ 向右*平移* $t$。

</li>

<li>

把两者*相乘*，再对 $\tau$ *积分*：结果就是 $g(t)$。

</li>

</ol>

随着 $t$ 增大，反转后的 $h$ 从左向右滑过 $s$。在两者不重叠的地方，$g(t)=0$。

为什么要反转？作为 $\tau$ 的函数，自变量 $t-\tau$ 随 $\tau$ 增大而减小。$h$ 的起点（年龄为零）位于 $\tau=t$，越早的冲激位于越左边。对于 RC 电路，$h$ 在起点处最大：系统对最近的过去“记得”最清楚。

**例：RC 电路与矩形脉冲。** 时间常数为 $T=RC$ 的 RC 电路，其冲激响应是一个面积为 1 的衰减指数脉冲（第 [8](#stufe-8) 阶段将推导它）：

<span class="anker" id="gl-5-1"></span>
$$h(t)=\frac1T\,\varepsilon(t)\,\mathrm{e}^{-t/T}. \tag{5.1}$$

输入：从 $0$ 到 $T_0$、高度为 $a$ 的矩形。图 [6](#abb-6) 给出了两个时刻下两个因子的相对位置。共分三个区间：

<span class="anker" id="gl-5-2"></span>
$$g(t)=\begin{cases}0 & t<0,\\[2pt] a\bigl(1-\mathrm{e}^{-t/T}\bigr) & 0\le t\le T_0,\\[2pt] a\bigl(\mathrm{e}^{T_0/T}-1\bigr)\mathrm{e}^{-t/T} & t>T_0.\end{cases} \tag{5.2}$$

:::herleitung 对矩形脉冲的响应
⁠**$t<0$：**平移后的 $h(t-\tau)$ 仅在 $\tau\le t<0$ 时非零，而 $s(\tau)$ 仅在 $\tau\ge0$ 时非零。两者没有重叠，$g=0$。

⁠**$0\le t\le T_0$：**重叠区间为 $0<\tau<t$：

$$g(t)=\int_0^ta\,\frac1T\,\mathrm{e}^{-(t-\tau)/T}\,\mathrm{d}\tau=\frac aT\,\mathrm{e}^{-t/T}\int_0^t\mathrm{e}^{\tau/T}\mathrm{d}\tau=\frac aT\,\mathrm{e}^{-t/T}\cdot T\bigl(\mathrm{e}^{t/T}-1\bigr)=a\bigl(1-\mathrm{e}^{-t/T}\bigr).$$

⁠**$t>T_0$：**只在 $0<\tau<T_0$ 内重叠：

$$g(t)=\frac aT\,\mathrm{e}^{-t/T}\int_0^{T_0}\mathrm{e}^{\tau/T}\mathrm{d}\tau=a\bigl(\mathrm{e}^{T_0/T}-1\bigr)\mathrm{e}^{-t/T}.$$
:::

在参考模型中（$a=1$，$T_0=T=1$ s）：$g(0.5)=0.3935$，$g(1)=0.6321$，$g(2)=0.2325$，$g(3)=0.0855$。这与图 [4](#abb-4) 中的 $g_0$ 是同一条曲线。

:::abbildung et3/k1schieben
图解卷积，$a=1$，$T_0=T=1$ s。蓝色：$s(\tau)$。红色：$h(t-\tau)$，已反转并平移 $t$。橙色面积就是 $g(t)$：$t=0.5$ s 时为 0.3935（部分重叠），$t=2$ s 时为 0.2325（整个矩形都位于 $h$ 已衰减的部分）。右：完整的响应及这两个点。
:::

:::frage 为什么反转的是 $h$，而不是 $s$？
也可以反转 $s$，因为卷积满足交换律（第 [6](#stufe-6) 阶段）。反转哪个函数能让平移过程更容易看清，就反转哪个，通常是形状较简单的那个。
:::

:::ltspice 对矩形脉冲的响应
⁠**绘制：**第 [2](#stufe-2) 阶段中的 RC 电路，信号源取 `PULSE(0 1 0 1u 1u 1)`：高度 1 V，持续时间 1 s。

⁠**指令：**`.tran 0 20 0 1m`，每个时刻一条测量语句，例如 `.meas tran g2 FIND V(out) AT=2`，再加上 `.meas tran gmax MAX V(out)` 和 `.meas tran area INTEG V(out)`。

⁠**你会看到：**$g(0.5)=0.3935$，$g(1)=0.6321$，$g(2)=0.2325$，$g(3)=0.0855$，与式 [(5.2)](#gl-5-2) 给出的完全一致。把 `gmax` 和 `area` 与你在练习 [6](#aufg-6) 中的结果比较。
:::

:::aufgabe 练习 5 ★★ 矩形与矩形
<span class="anker" id="aufg-5"></span>

按上述步骤计算 $\operatorname{rect}(t)*\operatorname{rect}(t)$。分 $|t|>1$、$-1\le t\le0$ 和 $0\le t\le1$ 三种情况讨论。结果是哪一个基本信号？

:::loesung
反转后的矩形仍是 $\operatorname{rect}$（它是对称的）；平移后它占据区间 $[t-\frac12,t+\frac12]$。积分值就是它与 $[-\frac12,\frac12]$ 重叠部分的长度：

<ul>

<li>

$|t|>1$：没有重叠，结果为 0。

</li>

<li>

$-1\le t\le0$：重叠部分从 $-\frac12$ 到 $t+\frac12$，长度为 $1+t$。

</li>

<li>

$0\le t\le1$：重叠部分从 $t-\frac12$ 到 $\frac12$，长度为 $1-t$。

</li>

</ul>

合起来，当 $|t|\le1$ 时结果为 $1-|t|$：$\operatorname{rect}*\operatorname{rect}=\Lambda$。数值：$t=0$、0.5 和 0.8 时分别为 1.000、0.500 和 0.200。
:::
:::

:::aufgabe 练习 6 ★★ 检验矩形脉冲的响应
<span class="anker" id="aufg-6"></span>

<ol class="al">

<li>

证明式 [(5.2)](#gl-5-2) 在 $t=T_0$ 处连续。为什么它必须连续？

</li>

<li>

$g(t)$ 在何处取得最大值？在参考模型中，最大值是多少？

</li>

<li>

证明 $g(t)$ 下方的面积等于 $aT_0$，并利用 $\int h\,\mathrm{d} t=1$ 不经计算说明其原因。

</li>

</ol>

:::loesung
(a) 在 $t=T_0$ 处：$a(1-\mathrm{e}^{-T_0/T})$ 与 $a(\mathrm{e}^{T_0/T}-1)\mathrm{e}^{-T_0/T}=a(1-\mathrm{e}^{-T_0/T})$，两者相等。物理上：电容电压不能跳变，因为那需要无穷大的电流。数学上：有界信号与可积的 $h$ 的卷积是连续的。

(b) 在脉冲期间 $g$ 上升，脉冲结束后 $g$ 下降。最大值位于 $t=T_0$：$g(1\,\mathrm{s})=1-\mathrm{e}^{-1}=0.632$。

(c) 通过计算：

$$\int g\,\mathrm{d} t=a\Bigl[T_0-T\bigl(1-\mathrm{e}^{-T_0/T}\bigr)\Bigr]+a\bigl(\mathrm{e}^{T_0/T}-1\bigr)T\mathrm{e}^{-T_0/T}=aT_0.$$

不经计算：卷积的面积等于各自面积的乘积，$\int g\,\mathrm{d} t=\int\!\!\int s(\tau)h(t-\tau)\,\mathrm{d}\tau\,\mathrm{d} t=\int s\,\mathrm{d}\tau\cdot\int h\,\mathrm{d} t=aT_0\cdot1$。数值：1.000。
:::
:::

## 第 6 阶段：卷积的运算规则

<span class="anker" id="stufe-6"></span>

:::zweck
卷积在许多方面与乘法相似。每一条运算规则对系统都有其含义。
:::

卷积积分简写为__卷积乘积__ $g(t)=s(t)*h(t)$。于是式 [(4.1)](#gl-4-1) 可写成 $s(t)=s(t)*\delta(t)$。

<ol class="al">

<li>

⁠**单位元。**$s*\delta=s$：狄拉克冲激扮演数字 1 的角色。$h(t)=\delta(t)$ 的系统使每个信号都原样通过，称为__理想无失真__系统。

</li>

<li>

⁠**交换律。**$s*h=h*s$。含义：输入和冲激响应可以互换角色。冲激响应为 $s$ 的系统对输入 $h$ 的响应，与系统 $h$ 对输入 $s$ 的响应完全相同。

</li>

<li>

⁠**结合律。**$(f*s)*h=f*(s*h)$。含义：两个级联的系统相当于一个系统，其冲激响应是这两个冲激响应的卷积。

</li>

<li>

⁠**分配律。**$f*(s+h)=f*s+f*h$。含义：两个并联且输出相加的系统，相当于一个冲激响应为两者冲激响应之和的系统。

</li>

<li>

⁠**复信号。**由于卷积是线性的，它可以分解为实部和虚部：

<span class="anker" id="gl-6-1"></span>
$$s*h=\bigl[\operatorname{Re} s*\operatorname{Re} h-\operatorname{Im} s*\operatorname{Im} h\bigr]+\mathrm{j}\bigl[\operatorname{Re} s*\operatorname{Im} h+\operatorname{Im} s*\operatorname{Re} h\bigr]. \tag{6.1}$$

</li>

</ol>

:::herleitung 交换律
作代换 $\tau'=t-\tau$，于是 $\tau=t-\tau'$，$\mathrm{d}\tau=-\mathrm{d}\tau'$。积分限 $\tau=\mp\infty$ 变为 $\tau'=\pm\infty$；交换上下限恰好抵消负号：

$$s*h=\int_{-\infty}^{\infty}s(\tau)\,h(t-\tau)\,\mathrm{d}\tau=\int_{-\infty}^{\infty}s(t-\tau')\,h(\tau')\,\mathrm{d}\tau'=h*s.$$
:::

:::abbildung et3/k1bloecke
上：级联，冲激响应为 $h_1*h_2$（结合律）。下：并联后相加，冲激响应为 $h_1+h_2$（分配律）。
:::

:::aufgabe 练习 7 ★★ 两个 RC 电路级联
<span class="anker" id="aufg-7"></span>

两个 $RC=1$ s 的 RC 电路级联。假设第二个电路不对第一个电路构成负载（例如在两者之间接入一个电压跟随器）。

<ol class="al">

<li>

计算级联系统的冲激响应 $h*h$，其中 $h(t)=\mathrm{e}^{-t}\varepsilon(t)$。

</li>

<li>

它在何时达到最大值？它的面积是多少？

</li>

<li>

为什么需要“不构成负载”这一条件？

</li>

</ol>

:::loesung
(a) 对于 $t\ge0$：

$$(h*h)(t)=\int_0^t\mathrm{e}^{-\tau}\mathrm{e}^{-(t-\tau)}\mathrm{d}\tau=\mathrm{e}^{-t}\int_0^t\mathrm{d}\tau=t\,\mathrm{e}^{-t}.$$

因此 $h_{\text{级联}}(t)=t\,\mathrm{e}^{-t}\varepsilon(t)$。

(b) 导数：$(1-t)\mathrm{e}^{-t}$ 在 $t=1$ s 处为零，最大值为 $\mathrm{e}^{-1}=0.368$。面积：$\int_0^\infty t\mathrm{e}^{-t}\mathrm{d} t=1=1\cdot1$（面积之积）。

(c) 如果不加解耦，第二个 RC 电路会从第一个电容中汲取电流。这时第一个电容上的电压就不再是空载 RC 电路的电压，级联系统的冲激响应也就不是 $h*h$。它仍然是一个 LTI 系统，只是冲激响应不同。把各个响应做卷积的前提是：没有哪个系统会反过来影响自己的输入。
:::
:::

## 第 7 阶段：狄拉克冲激

<span class="anker" id="stufe-7"></span>

:::zweck
狄拉克冲激就是第 [4](#stufe-4) 阶段中的那个极限对象。它不是普通的函数。它的全部性质都源于一个事实：它只通过自己的面积起作用。
:::

**$\delta$ 是什么，不是什么。** 当 $T_0\to0$ 时，矩形 $\frac{1}{T_0}\operatorname{rect}(t/T_0)$ 越来越窄、越来越高，而面积始终为 1（图 [8](#abb-8)）。在普通函数的意义下，这个极限并不存在：一个除某一点外处处为零的函数，无论它在该点取什么值，面积都为零。因此 $\delta(t)$ 是一个__广义函数__（又称分布）：一种仅由其在积分号下的作用、即由式 [(4.1)](#gl-4-1) 来定义的对象。它被画成一个箭头，箭头的高度表示权重（面积）。

:::abbildung et3/k1dirac
左：面积为 1、越来越窄且越来越高的矩形。右：极限对象的符号。箭头的高度是权重，而不是函数值。
:::

:::satz 定理 7.1 (狄拉克冲激的性质)
<span class="anker" id="satz-7-1"></span>

<span class="anker" id="gl-7-1"></span>
<span class="anker" id="gl-7-2"></span>
<span class="anker" id="gl-7-3"></span>
<span class="anker" id="gl-7-4"></span>
<span class="anker" id="gl-7-5"></span>
<span class="anker" id="gl-7-6"></span>
$$\begin{aligned} &\text{权重：} && [a\,\delta(t)]*s(t)=a\,s(t),\qquad a_1\delta(t)+a_2\delta(t)=(a_1+a_2)\,\delta(t),\\ &\text{筛选：} && \int_{-\infty}^{\infty}\delta(\tau)\,s(-\tau)\,\mathrm{d}\tau=s(0),\qquad s(t)\,\delta(t-T)=s(T)\,\delta(t-T),\\ &\text{面积：} && \int_{-\infty}^{\infty}a\,\delta(t)\,\mathrm{d} t=a,\\ &\text{尺度变换：} && \delta(bt)=\frac{1}{|b|}\,\delta(t),\qquad \delta(-t)=\delta(t),\\ &\text{平移：} && \delta(t-t_0)*s(t)=s(t-t_0),\\ &\text{积分：} && \varepsilon(t)=\int_{-\infty}^t\delta(\tau)\,\mathrm{d}\tau,\qquad \frac{\mathrm{d}}{\mathrm{d} t}\varepsilon(t)=\delta(t). \end{aligned} \tag{7.1|7.2|7.3|7.4|7.5|7.6}$$
:::

⁠**如何理解：**乘积 $s(t)\,\delta(t-T)$ 只可能在 $T$ 点起作用，因此只有 $s(T)$ 有意义。压缩后的冲激 $\delta(bt)$ 同样是“无限高”的，但它的面积只有 $1/|b|$。$h(t)=\delta(t-t_0)$ 的系统把每个信号延迟 $t_0$，称为__理想延时器__。此外，由于阶跃是冲激的变上限积分，带跳变的函数也可以求导：高度为 $A$ 的跳变变成 $A\,\delta$。这称为__广义求导__。注意：许多运算，例如平方（$\delta^2$），对狄拉克冲激是没有定义的。

:::herleitung 尺度变换与筛选乘积
⁠**尺度变换。**对 $b>0$，令 $\vartheta=b\tau$：

$$\delta(bt)*s(t)=\int\delta(b\tau)\,s(t-\tau)\,\mathrm{d}\tau=\frac1b\int\delta(\vartheta)\,s\Bigl(t-\frac\vartheta b\Bigr)\mathrm{d}\vartheta=\frac1b\,s(t).$$

对 $b<0$，这一代换使积分方向反向，结果为 $-\frac1b=\frac{1}{|b|}$。因此 $\delta(bt)$ 的作用与 $\frac1{|b|}\delta(t)$ 相同。取 $b=-1$，即得对称性 $\delta(-t)=\delta(t)$。

⁠**筛选乘积。**把 $s(t)\delta(t)$ 与任意 $g(t)$ 做卷积，由筛选性质得

$$[s(t)\delta(t)]*g(t)=\int s(\tau)\delta(\tau)\,g(t-\tau)\,\mathrm{d}\tau=s(0)\,g(t)=[s(0)\delta(t)]*g(t).$$

两者对每个 $g$ 的作用都相同，所以 $s(t)\delta(t)=s(0)\delta(t)$。再经平移即得 $s(t)\delta(t-T)=s(T)\delta(t-T)$。

⁠**积分。**$\varepsilon(t)=\delta(t)*\varepsilon(t)=\int\delta(\tau)\,\varepsilon(t-\tau)\,\mathrm{d}\tau$，而 $\varepsilon(t-\tau)$ 恰在 $\tau\le t$ 时等于 1。
:::

:::frage 可是 $\delta(0)$ 是无穷大。那 $\delta(2t)$ 不就和 $\delta(t)$ 一样吗？
不是。“无限高”并不能刻画 $\delta$，因为除 $0$ 点以外，两者的所有函数值都相同，而 $0$ 点处的值不是一个数。刻画 $\delta$ 的是它的面积。如果把面积为 1 的矩形压缩到一半宽度而保持高度不变，面积就会减半。所以 $\delta(2t)=\frac12\delta(t)$。
:::

:::aufgabe 练习 8 ★ 用 $\delta$ 进行计算
<span class="anker" id="aufg-8"></span>

计算： (a) $\int_{-\infty}^\infty\delta(t-2)\,\mathrm{e}^{-t}\mathrm{d} t$， (b) $\mathrm{e}^{-t}\,\delta(t-1)$， (c) $\int_{-\infty}^\infty\delta(2t)\,\mathrm{d} t$， (d) $\delta(t)*\delta(t-3)$， (e) $\operatorname{rect}(t)*\delta(t-1)$， (f) $\frac{\mathrm{d}}{\mathrm{d} t}\bigl[3\,\varepsilon(t-1)\bigr]$。

:::loesung
(a) $\mathrm{e}^{-2}=0.135$； (b) $\mathrm{e}^{-1}\,\delta(t-1)$； (c) $\tfrac12$； (d) $\delta(t-3)$； (e) $\operatorname{rect}(t-1)$； (f) $3\,\delta(t-1)$。
:::
:::

## 第 8 阶段：积分与微分

<span class="anker" id="stufe-8"></span>

:::zweck
积分器和微分器都是 LTI 系统。它们把阶跃响应和冲激响应联系起来，并使我们能够由 RC 电路的阶跃响应得到它的冲激响应。
:::

**积分器。** 把式 [(7.6)](#gl-7-6) 中的 $\delta$ 换成任意的 $s$，同样的计算给出

<span class="anker" id="gl-8-1"></span>
$$s(t)*\varepsilon(t)=\int_{-\infty}^ts(\tau)\,\mathrm{d}\tau. \tag{8.1}$$

冲激响应为 $\varepsilon(t)$ 的系统求出其输入的变上限积分，称为__积分器__。若交换角色来读（$\varepsilon*s$），式 [(8.1)](#gl-8-1) 表明：**系统的阶跃响应是其冲激响应的变上限积分。**用 RC 电路来检验：$\int_0^t\mathrm{e}^{-\tau}\mathrm{d}\tau=1-\mathrm{e}^{-t}$，正是式 [(2.5)](#gl-2-5)。微分方程和卷积这两条相互独立的途径，得到了相同的结果。

**微分器。** 积分器后接一个__微分器__，任何信号都保持不变；这个级联是理想无失真的。因此，微分器的冲激响应是广义函数 $\delta'(t)$（__冲激偶__），其定义为

<span class="anker" id="gl-8-2"></span>
$$\delta'(t)*s(t)=\frac{\mathrm{d}}{\mathrm{d} t}s(t). \tag{8.2}$$

近似地看，$\delta'$ 是一个窄的双矩形脉冲：先是一个高度为 $+1/T_0^2$ 的矩形，再是一个高度为 $-1/T_0^2$ 的矩形，宽度均为 $T_0$。它被画成一对箭头，一个向上，一个向下。

**冲激响应 $=$ 阶跃响应的导数。** 由于 $\delta=\frac{\mathrm{d}}{\mathrm{d} t}\varepsilon$，且系统是线性时不变的，所以 $h=\frac{\mathrm{d}}{\mathrm{d} t}(\text{阶跃响应})$。对于 RC 电路，利用乘积法则：

<span class="anker" id="gl-8-3"></span>
$$h(t)=\frac{\mathrm{d}}{\mathrm{d} t}\Bigl[\bigl(1-\mathrm{e}^{-t/RC}\bigr)\varepsilon(t)\Bigr]=\frac{1}{RC}\mathrm{e}^{-t/RC}\varepsilon(t)+\bigl(1-\mathrm{e}^{-t/RC}\bigr)\delta(t)=\frac{1}{RC}\mathrm{e}^{-t/RC}\varepsilon(t). \tag{8.3}$$

根据式 [(7.2)](#gl-7-2)，第二项为零：$(1-\mathrm{e}^{0})\,\delta(t)=0$。其背后的机理是：RC 电路的阶跃响应没有跳变，因为电容充电需要时间。只有带跳变的阶跃响应，才会在 $h$ 中产生狄拉克冲激（练习 [9](#aufg-9)）。

:::aufgabe 练习 9 ★★ 高通滤波器：冲激响应中的狄拉克冲激
<span class="anker" id="aufg-9"></span>

若把 $R$ 和 $C$ 互换，输出电压就取自 $R$ 两端（CR 高通滤波器，$RC=1$ s）。它的阶跃响应为 $\mathrm{e}^{-t}\varepsilon(t)$。

<ol class="al">

<li>

从机理上解释这一阶跃响应：最初瞬间 $R$ 两端的电压是多少？很长时间之后又是多少？

</li>

<li>

通过求导求出冲激响应。其中的狄拉克分量在物理上意味着什么？

</li>

<li>

检验：对冲激响应积分，必须重新得到阶跃响应。

</li>

</ol>

:::loesung
(a) 最初瞬间电容未充电，因此其两端没有电压。全部 1 V 都加在 $R$ 上。随后电流给电容充电；电容电压按 $1-\mathrm{e}^{-t}$ 上升，$R$ 上剩下 $\mathrm{e}^{-t}$。很长时间之后，电容充满，不再有电流流过，$R$ 上也就没有电压了。

(b) 乘积法则：

$$h(t)=\frac{\mathrm{d}}{\mathrm{d} t}\bigl[\mathrm{e}^{-t}\varepsilon(t)\bigr]=-\mathrm{e}^{-t}\varepsilon(t)+\mathrm{e}^{0}\,\delta(t)=\delta(t)-\mathrm{e}^{-t}\varepsilon(t).$$

这里阶跃响应在 $t=0$ 处从 0 跳变到 1，因此狄拉克分量保留了下来。物理上：无限短的冲激直接通过，因为电容无法在零时间内建立起电压。冲激送到电容上的电荷，随后又经 $R$ 沿相反方向流走：$-\mathrm{e}^{-t}$。

(c) $\int_{-\infty}^t\bigl[\delta(\tau)-\mathrm{e}^{-\tau}\varepsilon(\tau)\bigr]\mathrm{d}\tau=\varepsilon(t)-\bigl(1-\mathrm{e}^{-t}\bigr)\varepsilon(t)=\mathrm{e}^{-t}\varepsilon(t)$。
:::
:::

## 第 9 阶段：因果与稳定

<span class="anker" id="stufe-9"></span>

:::zweck
每个实际系统都应具备的两个性质，可以直接从 $h(t)$ 读出。
:::

:::definition 定义 9.1 (因果、稳定)
<span class="anker" id="satz-9-1"></span>

如果输出不会先于输入出现，则称系统是__因果__的。对于 LTI 系统，这意味着

<span class="anker" id="gl-9-1"></span>
$$h(t)=0\quad\text{对于}\ t<0. \tag{9.1}$$

如果系统对每个有界输入 $|s(t)|\le A<\infty$ 都以有界输出作为响应，则称系统是__稳定__的（更准确地说是 BIBO 稳定，即 *bounded input, bounded output*，有界输入、有界输出）。
:::

因果：时刻 0 的冲激，在这一时刻之前不可能产生任何作用。于是在卷积中只有过去的冲激有贡献，$g(t)=\int_{-\infty}^ts(\tau)h(t-\tau)\mathrm{d}\tau$。

:::satz 定理 9.2 (稳定性条件)
<span class="anker" id="satz-9-2"></span>

LTI 系统稳定，当且仅当其冲激响应绝对可积：

<span class="anker" id="gl-9-2"></span>
$$\int_{-\infty}^{\infty}|h(\tau)|\,\mathrm{d}\tau<\infty. \tag{9.2}$$
:::

:::herleitung 稳定性条件
⁠**充分性。**利用积分的三角不等式以及 $|s|\le A$：

$$|g(t)|=\Bigl|\int h(\tau)\,s(t-\tau)\,\mathrm{d}\tau\Bigr|\le\int|h(\tau)|\,|s(t-\tau)|\,\mathrm{d}\tau\le A\int|h(\tau)|\,\mathrm{d}\tau.$$

若该积分有限，则 $g$ 有界。

⁠**必要性。**若 $\int|h|=\infty$，则选取最不利的有界输入：$s(t_1-\tau)=\operatorname{sign}h(\tau)$，即始终取 $\pm1$，且符号与 $h$ 相同。于是 $g(t_1)=\int|h(\tau)|\,\mathrm{d}\tau=\infty$，尽管 $|s|\le1$。
:::

例子：RC 电路的 $\int|h|=1$，是稳定的。理想延时器（$\int|\delta(t-t_0)|\mathrm{d} t=1$）是稳定的。积分器的 $\int_0^\infty\varepsilon\,\mathrm{d} t=\infty$，是不稳定的：它对有界的阶跃输出无界的斜坡 $t\,\varepsilon(t)$。

:::aufgabe 练习 10 ★★ 因果吗？稳定吗？
<span class="anker" id="aufg-10"></span>

研究 (a) $h(t)=\mathrm{e}^{-2t}\varepsilon(t)$，(b) $h(t)=\mathrm{e}^{t}\varepsilon(t)$，(c) $h(t)=\varepsilon(t)-\varepsilon(t-1)$，(d) $h(t)=\mathrm{e}^{-|t|}$，(e) $h(t)=\delta(t+1)$。对于每个不稳定的系统，给出一个会产生无界输出的有界输入。

:::loesung
(a) 因果，$\int|h|=\tfrac12$：稳定。

(b) 因果，$\int_0^\infty\mathrm{e}^t\mathrm{d} t=\infty$：不稳定。阶跃 $\varepsilon(t)$ 产生 $\int_0^t\mathrm{e}^\tau\mathrm{d}\tau=\mathrm{e}^t-1$，它是无界的。

(c) 因果，$\int|h|=1$：稳定。该系统求输入在最近一秒内的积分（滑动窗口）。

(d) 非因果，因为 $t<0$ 时 $h(t)\neq0$。$\int\mathrm{e}^{-|t|}\mathrm{d} t=2$：稳定。

(e) $\delta(t+1)$ 在 $t=-1<0$ 处起作用：$g(t)=s(t+1)$；系统提前一秒就“看到”了输入。非因果，但稳定（$\int|h|=1$）。
:::
:::

## 第 10 阶段：没有系统的卷积

<span class="anker" id="stufe-10"></span>

:::frage 当信号真的通过一个系统时，卷积对我来说是讲得通的。可如果根本不涉及任何系统，卷积又意味着什么呢？
卷积是一种数学运算，它本身就具有普遍的含义：**对于把一个结果拆成两部分的每一种拆分方式，把两部分的权重相乘，再对所有拆分方式求和。**系统只是对此的一种解释（第一部分：冲激何时到达；第二部分：它的年龄有多大），而不是唯一的解释。

⁠**一个既没有系统、也没有时间的例子：两个骰子。**骰子点数之和为 $k$ 的概率是多少？每一种拆分 $k=i+(k-i)$ 都有贡献，其概率为 $P_1(i)\,P_2(k-i)$：

$$P(k)=\sum_iP_1(i)\,P_2(k-i).$$

这是一个卷积，其结构与 $g(t)=\int s(\tau)h(t-\tau)\mathrm{d}\tau$ 完全相同：$\tau$ 对应第一个骰子的点数，$t$ 对应点数之和，$t-\tau$ 对应第二个骰子的点数。两个均匀分布的骰子（“矩形”）给出三角形分布，正如练习 [5](#aufg-5) 中的 $\operatorname{rect}*\operatorname{rect}=\Lambda$。点数之和 7 出现得最频繁，因为它的拆分方式最多（图 [9](#abb-9)）。

更多的例子：对测量值做滑动平均，就是与一个矩形做卷积。一张模糊的照片，是清晰的图像与光学系统由单个点所成的光斑的卷积。而两个多项式相乘时，就是在对它们的系数做卷积（练习 [11](#aufg-11)）。
:::

:::abbildung et3/k1wuerfel
骰子点数之和的概率。每个分布都是前一个分布与单个骰子的分布的卷积。矩形变成三角形（$P(7)=6/36$），三角形又变成钟形曲线（$P(10)=P(11)=27/216$）。
:::

:::zusatz 为什么卷积如此常见
如果把越来越多相同的分布做卷积，结果会趋近于高斯曲线，而这几乎与初始形状无关（中心极限定理）。正因为如此，噪声作为许多微小的独立影响之和，往往服从高斯分布。而系数的卷积对应于多项式的乘积，这一事实正是所有把卷积变为乘积的变换的核心：[第 2 部分](/wissen/zh/elektrotechnik/3-semester/signale-und-systeme/laplace-transformation/laplace-transformation.html)用基本单元 $\mathrm{e}^{pt}$ 代替幂 $x^n$，做的是同样的事情。
:::

:::aufgabe 练习 11 ★ 骰子与多项式中的卷积
<span class="anker" id="aufg-11"></span>

<ol class="al">

<li>

用卷积和计算两个骰子的 $P(7)$ 和 $P(4)$。两种情况下分别有哪些拆分方式有贡献？

</li>

<li>

把两个骰子的分布与一个骰子的分布做卷积，计算三个骰子的 $P(10)$。

</li>

<li>

展开 $(1+2x)(3+x)$。证明结果的系数序列是序列 $(1,2)$ 与 $(3,1)$ 的卷积。

</li>

</ol>

:::loesung
(a) $P(7)$：拆分方式为 $1+6,\,2+5,\dots,6+1$，共六种，每种的概率为 $\frac16\cdot\frac16$：$P(7)=\frac{6}{36}=\frac16$。$P(4)$：$1+3,\,2+2,\,3+1$：$\frac{3}{36}=\frac{1}{12}$。

(b) $P_3(10)=\sum_{j=1}^6P_2(10-j)\cdot\frac16=\frac16\bigl[P_2(9)+P_2(8)+P_2(7)+P_2(6)+P_2(5)+P_2(4)\bigr]=\frac16\cdot\frac{4+5+6+5+4+3}{36}=\frac{27}{216}=\frac18$。

(c) $(1+2x)(3+x)=3+x+6x+2x^2=3+7x+2x^2$。$x^k$ 的系数汇集了所有满足 $i+j=k$ 的幂次对：$c_0=1\cdot3=3$，$c_1=1\cdot1+2\cdot3=7$，$c_2=2\cdot1=2$。这就是卷积和 $c_k=\sum_ia_ib_{k-i}$，与骰子的情形结构相同。
:::
:::

:::kern 要点
<ul>

<li>

平移 $t\to t-t_0$ 产生延迟，展缩 $t\to t/T$ 使信号变宽；$a\operatorname{rect}\bigl(\frac{t-t_0}{T}\bigr)$：中心 $t_0$，持续时间 $|T|$，高度 $a$。

</li>

<li>

RC 低通滤波器：$H(F)=\dfrac{1}{1+\mathrm{j}2\pi FRC}$，$|H|=\dfrac{1}{\sqrt{1+(2\pi FRC)^2}}$， $\varphi=-\arctan(2\pi FRC)$；阶跃响应为 $1-\mathrm{e}^{-t/RC}$。

</li>

<li>

LTI：叠加原理，以及 $\operatorname{Tr}\{s(t-t_0)\}=g(t-t_0)$。

</li>

<li>

$s(t)=\int s(\tau)\delta(t-\tau)\mathrm{d}\tau$，以及 $g(t)=\int s(\tau)h(t-\tau)\mathrm{d}\tau=s*h$。

</li>

<li>

计算方法：反转、平移、相乘、积分。

</li>

<li>

$s*\delta=s$；交换律、结合律（级联：$h_1*h_2$）、分配律（并联：$h_1+h_2$）。

</li>

<li>

$s(t)\delta(t-T)=s(T)\delta(t-T)$；$\delta(bt)=\delta(t)/|b|$；$\delta(t-t_0)*s=s(t-t_0)$；$\frac{\mathrm{d}}{\mathrm{d} t}\varepsilon=\delta$。

</li>

<li>

阶跃响应 $=\int h$，冲激响应 $=\frac{\mathrm{d}}{\mathrm{d} t}$ 阶跃响应。

</li>

<li>

因果：$t<0$ 时 $h(t)=0$。稳定：$\int|h|\mathrm{d} t<\infty$。

</li>

</ul>
:::

**[第 2 部分](/wissen/zh/elektrotechnik/3-semester/signale-und-systeme/laplace-transformation/laplace-transformation.html)预告。** 本文把信号分解为冲激 $\delta(t-\tau)$。系统对其中每一个冲激的响应都是 $h$ 的一个平移副本，所有副本都必须加起来：这就是卷积。[第 2 部分](/wissen/zh/elektrotechnik/3-semester/signale-und-systeme/laplace-transformation/laplace-transformation.html)把信号分解为基本单元 $\mathrm{e}^{pt}$。系统对其中每一个基本单元的响应只是乘上一个数 $H(p)$，卷积就变成了乘法。
