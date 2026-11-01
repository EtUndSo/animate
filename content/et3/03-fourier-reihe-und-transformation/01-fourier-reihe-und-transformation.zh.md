---
title: 傅里叶级数与傅里叶变换
pfad: 电气工程 / 第 3 学期 / 信号与系统 / 傅里叶级数与变换
order: 3230100
summary: 每个信号都是振荡的叠加
tags: 频谱, 频率响应, 基频, 谐波, 傅里叶级数, 直流分量, 正交, 功率
lang: zh
---

## 本文内容

[第 2 部分](/wissen/zh/elektrotechnik/3-semester/signale-und-systeme/laplace-transformation/laplace-transformation.html)表明，每个信号都是基本单元 $\mathrm{e}^{pt}$ 的叠加，而 LTI 系统只是把每个基本单元乘以一个数。傅里叶描述只使用虚轴上的基本单元 $p=\mathrm{j}2\pi f$：既不增长也不衰减的纯振荡 $\mathrm{e}^{\mathrm{j}2\pi ft}$。这有一个很大的优点：振荡具有频率，而频率可以听到、测量和滤波。__频谱__ $S(f)$ 表明信号中各个频率分别以怎样的幅度和相位存在。

:::merke 三句话的答案（读完本文后应觉得理所当然）
<ol>

<li>

周期信号是位于基频整数倍处的各个振荡之和（傅里叶级数）；非周期信号是对所有频率的积分（傅里叶积分）。

</li>

<li>

每个振荡 $\mathrm{e}^{\mathrm{j}2\pi ft}$ 都是特征函数：LTI 系统把它乘以 $H(f)$，因此卷积变成了乘积 $G(f)=S(f)\,H(f)$。

</li>

<li>

所有运算规则（时移、展缩、调制、对偶性）都可以由相应运算对单个振荡的作用推出。

</li>

</ol>
:::

**所有结论背后的同一个原理。**

| 结论 | 来源 |
|---|---|
| 频率响应 $H(f)$ | 振荡 $\mathrm{e}^{\mathrm{j}2\pi ft}$ 的特征值（第 [1](#stufe-1) 阶段） |
| 傅里叶级数，只含 $F$ 的整数倍 | 只有这些振荡具有周期 $T$（第 [2](#stufe-2) 阶段） |
| 级数的分析公式 | 不同频率的振荡相互正交（第 [2](#stufe-2) 阶段） |
| 帕塞瓦尔定理、吉布斯现象、周期输入下的 LTI 系统 | 每个谐波单独考虑（第 [3](#stufe-3) 阶段） |
| 傅里叶积分 | 周期 $\to\infty$，谱线相互靠拢（第 [4](#stufe-4) 阶段） |
| 实信号的 $S(-f)=S^*(f)$ | 振荡以共轭对的形式出现（第 [5](#stufe-5) 阶段） |
| 时移、展缩、微分、调制 | 该运算对 $\mathrm{e}^{\mathrm{j}2\pi ft}$ 的作用（第 [6](#stufe-6) 阶段） |
| 对偶性 | 正变换与逆变换只差一个符号（第 [6](#stufe-6) 阶段） |
| 线谱、狄拉克梳状函数、阶跃 | 含狄拉克冲激的极限情况（第 [8](#stufe-8) 阶段） |
| 希尔伯特变换 | 因果信号由一半即可确定（第 [9](#stufe-9) 阶段） |
| 短时傅里叶变换 | 一个片段的频谱（第 [10](#stufe-10) 阶段） |

**如何使用本文。**每个阶段包括基本思路、可展开解答的典型问题以及练习（★ 到 ★★★）。请先自己尝试，解答可在每道练习下方展开。

:::merke 本文的参考模型
<ul>

<li>

⁠**方波**：在 0 与 1 之间变化，周期 $T=2\pi$ s，占空比为 $\frac12$：$|t|\le T/4$ 时为 1，$T/4<|t|\le T/2$ 时为 0，并作周期延拓。基频 $F=1/T=0.159$ Hz，因此 $2\pi F=1/\mathrm s$。

</li>

<li>

⁠**RC 低通滤波器**，$RC=1$ s，$H(f)=1/(1+\mathrm{j}2\pi f\,RC)$。在方波的第 $k$ 次谐波处，$2\pi kF\cdot RC=k$，因此 $H(kF)=1/(1+\mathrm{j} k)$。

</li>

<li>

⁠**矩形脉冲** $\operatorname{rect}(t)$ 与 $\operatorname{si}(x)=\sin(x)/x$。

</li>

</ul>

脚本 `rechnung_kap3.py` 可重新计算这些数值和曲线。
:::

## 第 1 阶段：作为特征函数的振荡

<span class="anker" id="stufe-1"></span>

:::zweck
在基本单元 $\mathrm{e}^{pt}$ 中，从现在起只使用纯振荡。本阶段说明 LTI 系统对它们起什么作用。
:::

当 $p=\mathrm{j}2\pi f$ 为纯虚数时，基本单元变成幅度恒定的振荡：

$$\mathrm{e}^{\mathrm{j}2\pi ft}=\cos(2\pi ft)+\mathrm{j}\sin(2\pi ft).$$

与每个基本单元一样，它是每个 LTI 系统的特征函数（延迟就是乘以 $\mathrm{e}^{-\mathrm{j}2\pi f\tau}$）：

<span class="anker" id="gl-1-1"></span>
$$\mathrm{e}^{\mathrm{j}2\pi ft}*h(t)=H(f)\,\mathrm{e}^{\mathrm{j}2\pi ft},\qquad H(f)=\int_{-\infty}^{\infty}h(t)\,\mathrm{e}^{-\mathrm{j}2\pi ft}\,\mathrm{d} t. \tag{1.1}$$

$H(f)$ 称为__频率响应__或传递函数。它的模表示频率为 $f$ 的振荡被放大或衰减的程度，它的相位表示该振荡被移动了多少。两个系统级联时，依次相乘：$H(f)=H_1(f)H_2(f)$。若拉普拉斯变换 $H(p)$ 在虚轴上存在，则 $H(f)=H(p)|_{p=\mathrm{j}2\pi f}$。

⁠**简而言之：**频率响应就是 LTI 系统乘到纯振荡上的那个数。

## 第 2 阶段：周期信号——傅里叶级数

<span class="anker" id="stufe-2"></span>

:::zweck
周期信号每经过 $T$ 就重复一次。它可以由振荡构成，但只能由非常特定的振荡构成。本阶段说明是哪些振荡，以及如何求出它们的权重。
:::

**思路。** 振荡 $\mathrm{e}^{\mathrm{j}2\pi ft}$ 经过 $T$ 后重复，当且仅当 $fT$ 为整数。因此，周期为 $T$ 的信号只包含频率 $f_k=kF$（其中 $F=1/T$ 为__基频__），即__谐波__：

<span class="anker" id="gl-2-1"></span>
$$s_p(t)=\sum_{k=-\infty}^{\infty}S_p(k)\,\mathrm{e}^{\mathrm{j}2\pi kFt}. \tag{2.1}$$

这就是__傅里叶级数__（综合）。$S_p(k)$ 是第 $k$ 次谐波的复权重。

**实信号。** 对实信号有 $s_p=s_p^*$。对式 [(2.1)](#gl-2-1) 取共轭，$\mathrm{e}^{\mathrm{j}2\pi kFt}$ 就变成 $-k$ 对应的振荡。比较系数得

$$S_p(-k)=S_p^*(k).$$

于是每一对 $k,-k$ 给出 $2\operatorname{Re}\{S_p(k)\mathrm{e}^{\mathrm{j}2\pi kFt}\}$，即一个实的余弦振荡。令 $S_p(k)=|S_p(k)|\,\mathrm{e}^{\mathrm{j}\varphi_p(k)}$，得：

<span class="anker" id="gl-2-2"></span>
<span class="anker" id="gl-2-3"></span>
$$\begin{aligned} s_p(t)&=S_p(0)+2\sum_{k=1}^{\infty}|S_p(k)|\cos\bigl(2\pi kFt+\varphi_p(k)\bigr)\\ &=S_p(0)+2\sum_{k=1}^{\infty}\Bigl[\operatorname{Re}\{S_p(k)\}\cos(2\pi kFt)-\operatorname{Im}\{S_p(k)\}\sin(2\pi kFt)\Bigr]. \end{aligned} \tag{2.2|2.3}$$

相位 $\varphi_p(k)$ 的求法与任何复数相同：用 $\arctan$ 并作象限修正（实部为负时加 $\pi$）。$S_p(0)$ 是__直流分量__，即信号的平均值。

**求权重：正交性。** 如何从和式中提取出单个 $S_p(n)$？乘以 $\mathrm{e}^{-\mathrm{j}2\pi nFt}$，并在一个周期内取平均。在此过程中，其他所有谐波都消失了：

<span class="anker" id="gl-2-4"></span>
$$\frac1T\int_0^T\mathrm{e}^{\mathrm{j}2\pi(k-n)Ft}\,\mathrm{d} t=\begin{cases}1&k=n\\0&k\neq n\end{cases}. \tag{2.4}$$

当 $k\neq n$ 时，相量 $\mathrm{e}^{\mathrm{j}2\pi(k-n)Ft}$ 在一个周期内恰好转 $|k-n|$ 整圈，其平均值为零。当 $k=n$ 时，它静止不动。因此，不同频率的振荡称为__正交__的。剩下的是：

:::satz 定理 2.1 (傅里叶级数)
<span class="anker" id="satz-2-1"></span>

周期为 $T=1/F$、功率有限的信号可以表示为式 [(2.1)](#gl-2-1)，其中

<span class="anker" id="gl-2-5"></span>
$$S_p(k)=\frac1T\int_{t_1}^{t_1+T}s_p(t)\,\mathrm{e}^{-\mathrm{j}2\pi kFt}\,\mathrm{d} t, \tag{2.5}$$

$t_1$ 可任意选取（分析）。
:::

⁠**如何理解：**$S_p(k)$ 是信号用第 $k$ 次谐波“反向旋转”之后的平均值。若信号中含有该谐波，则相量在此处不再旋转，其份额在取平均后保留下来。$S_p(0)$ 就是平均值。

:::herleitung 分析公式
将式 [(2.1)](#gl-2-1) 乘以 $\mathrm{e}^{-\mathrm{j}2\pi nFt}$，在一个周期内积分，并交换求和与积分的次序：

$$\int_0^Ts_p(t)\mathrm{e}^{-\mathrm{j}2\pi nFt}\mathrm{d} t=\sum_kS_p(k)\int_0^T\mathrm{e}^{\mathrm{j}2\pi(k-n)Ft}\mathrm{d} t=S_p(n)\,T.$$

当 $k\neq n$ 时，积分为 $\frac{\mathrm{e}^{\mathrm{j}2\pi(k-n)FT}-1}{\mathrm{j}2\pi(k-n)F}=0$，因为 $\mathrm{e}^{\mathrm{j}2\pi(k-n)}=1$。由于被积函数的周期为 $T$，可以在任意长度为 $T$ 的区间上积分。
:::

**例：有限级数。** $s_p(t)=1+2\cos(2\pi Ft)+\sin(4\pi Ft)$。利用欧拉公式，无需积分即可读出系数：

$$2\cos(2\pi Ft)=\mathrm{e}^{\mathrm{j}2\pi Ft}+\mathrm{e}^{-\mathrm{j}2\pi Ft},\qquad\sin(4\pi Ft)=\frac{1}{2\mathrm{j}}\mathrm{e}^{\mathrm{j}4\pi Ft}-\frac{1}{2\mathrm{j}}\mathrm{e}^{-\mathrm{j}4\pi Ft},$$

所以 $S_p(0)=1$，$S_p(\pm1)=1$，$S_p(2)=-\tfrac{\mathrm{j}}{2}$，$S_p(-2)=\tfrac{\mathrm{j}}{2}$，其余均为零。验证：$S_p(-2)=S_p^*(2)$。

**例：方波。** 对参考模型（$|t|\le T_1/2$ 时为 1，$T_1=T/2$）：

<span class="anker" id="gl-2-6"></span>
$$S_p(0)=\frac{T_1}{T},\qquad S_p(k)=\frac1T\int_{-T_1/2}^{T_1/2}\mathrm{e}^{-\mathrm{j}2\pi kFt}\mathrm{d} t=\frac{\sin(\pi kT_1/T)}{\pi k}\quad(k\neq0). \tag{2.6}$$

当 $T_1=T/2$ 时：$S_p(0)=0.5$，$S_p(\pm1)=1/\pi=0.318$，$S_p(\pm2)=0$，$S_p(\pm3)=-0.106$，$S_p(\pm5)=0.064$。缺少偶次谐波，因为对偶数 $k$ 有 $\sin(\pi k/2)=0$。所有系数都是实数，因为信号是偶函数（第 [5](#stufe-5) 阶段）。图 [1](#abb-1) 给出了两种占空比下的系数：脉冲越窄，系数衰减越慢。

:::abbildung et3/k3koeff
方波（0/1）在两种脉冲宽度下的傅里叶系数。虚线：包络 $\frac{T_1}{T}\operatorname{si}(\pi kT_1/T)$。$T_1=T/2$ 时缺少偶次谐波，$T_1=T/4$ 时缺少 4 的倍数次谐波。
:::

:::frage 为什么周期信号在谐波之间没有频率？
因为和式中的每个振荡本身都必须具有周期 $T$，否则和就不是周期的。频率为 $f=1.5F$ 的振荡在经过 $T$ 之后只转了一圈半，所处位置与开始时不同。无论权重选得多么巧妙，都无法弥补这一点，因为不同的频率相互正交，不能彼此抵消。
:::

:::aufgabe 练习 1 ★ 读出系数
<span class="anker" id="aufg-1"></span>

$s_p(t)=\frac12+\cos\bigl(2\pi Ft+\frac\pi3\bigr)+\frac12\sin(6\pi Ft)$。

<ol class="al">

<li>

利用欧拉公式求出所有 $S_p(k)$。验证 $S_p(-k)=S_p^*(k)$。

</li>

<li>

给出 $|S_p(1)|$ 和 $\varphi_p(1)$，并与式 [(2.2)](#gl-2-2) 比较。

</li>

</ol>

:::loesung
(a) $\cos(x+\frac\pi3)=\frac12\mathrm{e}^{\mathrm{j}\pi/3}\mathrm{e}^{\mathrm{j} x}+\frac12\mathrm{e}^{-\mathrm{j}\pi/3}\mathrm{e}^{-\mathrm{j} x}$，$\frac12\sin(3x)=\frac{1}{4\mathrm{j}}\mathrm{e}^{\mathrm{j}3x}-\frac{1}{4\mathrm{j}}\mathrm{e}^{-\mathrm{j}3x}$，其中 $x=2\pi Ft$：

$$S_p(0)=\tfrac12,\quad S_p(\pm1)=\tfrac12\mathrm{e}^{\pm\mathrm{j}\pi/3}=0.25\pm0.433\mathrm{j},\quad S_p(3)=-\tfrac{\mathrm{j}}{4},\quad S_p(-3)=\tfrac{\mathrm{j}}{4},$$

其余均为零。$S_p(-1)=S_p^*(1)$ 与 $S_p(-3)=S_p^*(3)$ 成立。

(b) $|S_p(1)|=\frac12$，$\varphi_p(1)=60^\circ$。代入式 [(2.2)](#gl-2-2)：$2\cdot\frac12\cos(2\pi Ft+60^\circ)$，正是信号中的余弦项。（由帕塞瓦尔定理求功率：$\frac14+2\cdot\frac14+2\cdot\frac1{16}=0.875$。）
:::
:::

:::aufgabe 练习 2 ★★ 窄方波
<span class="anker" id="aufg-2"></span>

$T_1=T/4$ 的方波。

<ol class="al">

<li>

由式 [(2.6)](#gl-2-6) 计算 $S_p(0)$、$S_p(1)$、$S_p(2)$ 和 $S_p(4)$。

</li>

<li>

为什么 $S_p(4)=0$？请用正交性解释：脉冲中能容纳第四次谐波的多少个周期？

</li>

</ol>

:::loesung
(a) $S_p(0)=\frac14$，$S_p(1)=\frac{\sin(\pi/4)}{\pi}=0.225$，$S_p(2)=\frac{\sin(\pi/2)}{2\pi}=0.159$，$S_p(4)=\frac{\sin\pi}{4\pi}=0$。

(b) 第四次谐波的周期为 $T/4$，恰好等于脉冲宽度。分析公式在脉冲上对 $\mathrm{e}^{-\mathrm{j}2\pi4Ft}$ 积分，也就是对相量恰好一整圈积分。平均值为零。一般地，若脉冲中恰好能容纳第 $k$ 次谐波的整数个周期，则 $S_p(k)$ 为零。
:::
:::

## 第 3 阶段：功率、收敛性与 LTI 系统

<span class="anker" id="stufe-3"></span>

:::zweck
每个谐波对信号的贡献有多大？截断的级数对信号的近似有多好？LTI 系统对周期输入起什么作用？
:::

:::satz 定理 3.1 (傅里叶级数的帕塞瓦尔定理)
<span class="anker" id="satz-3-1"></span>

<span class="anker" id="gl-3-1"></span>
$$L_s=\frac1T\int_0^T|s_p(t)|^2\,\mathrm{d} t=\sum_{k=-\infty}^{\infty}|S_p(k)|^2. \tag{3.1}$$
:::

⁠**如何理解：**信号的平均__功率__等于各个谐波的功率之和。由于不同的谐波相互正交，交叉项消失。对方波有 $L_s=\frac12$。直流分量贡献 $0.25$，即 50 %。加上 $k=\pm1$ 为 90.5 %，$|k|\le3$ 时为 95.0 %，$|k|\le9$ 时为 98.0 %。

:::herleitung 帕塞瓦尔定理
$|s_p|^2=s_ps_p^*=\sum_k\sum_lS_p(k)S_p^*(l)\,\mathrm{e}^{\mathrm{j}2\pi(k-l)Ft}$。在一个周期内取平均，由式 [(2.4)](#gl-2-4)，只剩下 $k=l$ 的项：$\sum_k|S_p(k)|^2$。
:::

**截断级数与吉布斯现象。** 若只取 $|k|\le N$ 的谐波，得到__部分和__ $s_{p,N}(t)=\sum_{k=-N}^{N}S_p(k)\mathrm{e}^{\mathrm{j}2\pi kFt}$。误差 $s_p-s_{p,N}$ 的功率等于被略去的各项 $|S_p(k)|^2$ 之和；若信号的功率有限，则当 $N\to\infty$ 时它趋于零。然而在跳变处会残留一个过冲（图 [2](#abb-2)）：随着 $N$ 增大，它变得越来越窄，但其高度趋于跳变高度的约 9 %（$N=3$ 时为 10.0 %，$N=9$ 时为 9.1 %，$N=27$ 时为 9.0 %，极限为 8.95 %）。这就是__吉布斯现象__。它与收敛并不矛盾：过冲下方的面积，从而误差功率，仍然趋于零。

:::abbildung et3/k3gibbs
方波（$T=2\pi$ s）的部分和，包含 $|k|\le N$ 的谐波。在边沿处残留约为跳变高度 9 % 的过冲，随着 $N$ 增大，它只是变窄。
:::

**LTI 系统的周期输入。** 每个谐波都是特征函数，被乘以 $H(kF)$。因此输出具有相同的周期，其系数为

<span class="anker" id="gl-3-2"></span>
$$G_p(k)=S_p(k)\,H(kF). \tag{3.2}$$

在参考模型中，$H(kF)=1/(1+\mathrm{j} k)$。基波以 $|H|=0.707$ 和 $-45^\circ$ 传输，三次谐波以 $0.316$ 和 $-71.6^\circ$ 传输，五次谐波以 $0.196$ 和 $-78.7^\circ$ 传输。在输出端，三次谐波的大小只有基波的 15 %，而在输入端为 33 %。RC 电路把边沿变圆（图 [3](#abb-3)）。输出在 0.041 与 0.959 之间摆动。

:::abbildung et3/k3rc
方波通过 $RC=1$ s 的 RC 低通滤波器，按谐波之和计算，$G_p(k)=S_p(k)/(1+\mathrm{j} k)$。输出在 0.041 与 0.959 之间按指数规律充电和放电。
:::

:::frage 对无穷多个谐波进行计算，难道不比微分方程麻烦得多吗？
对于单个方波通过 RC 电路的情况，确实如此：充放电曲线可以直接写出来。但级数的长处在于，它说明了输出*为什么*是这个样子。边沿由高次谐波构成，而 RC 电路衰减的恰恰是这些谐波。此外，式 [(3.2)](#gl-3-2) 适用于每一个 LTI 系统，甚至适用于那些根本不知道其微分方程、只知道其实测频率响应的系统。
:::

:::ltspice 方波通过 RC 电路
⁠**绘制：**RC 电路（`res` 取 `1Meg`，`cap` 取 `1u`），信号源取 `PULSE(0 1 0 1u 1u {pi} {2*pi})`：周期为 $2\pi$ s，占空比为 $\frac12$。

⁠**指令：**`.tran 0 {20*pi} 0 1m`，`.four {1/(2*pi)} 5 V(in) V(out)`，以及用来关闭数据压缩的 `.options plotwinsize=0`；没有这条指令，`.four` 就不准确。`.four` 把最后一个周期分解为各次谐波，并把结果写入 SPICE Error Log。

⁠**你会看到：**在稳态下，`V(out)` 在 0.041 与 0.959 之间摆动。对 $k\ge1$，`.four` 给出式 [(2.2)](#gl-2-2) 中余弦振荡的幅度 $2|S_p(k)|$。在输入端，它们依次是 0.637、0、0.212、0、0.127：偶次谐波不存在。在输出端，三次谐波只有基波的 15 %，而不是 33 %。输出端的相位比输入端分别大 $45^\circ$、$71.6^\circ$ 和 $78.7^\circ$，因为 `.four` 把滞后计为正值。把输出幅度减半，与你在练习 [3](#aufg-3)(b) 中的结果比较。FFT 视图（在绘图窗口中单击右键，View，FFT）在 0.159 Hz 的奇数倍处显示同样的谱线。
:::

:::aufgabe 练习 3 ★★ 功率与高次谐波
<span class="anker" id="aufg-3"></span>

<ol class="al">

<li>

用式 [(3.1)](#gl-3-1) 验证：方波的谐波 $k=0,\pm1$ 携带了 90.5 % 的功率。

</li>

<li>

计算 RC 输出的 $|G_p(1)|$、$|G_p(3)|$、$|G_p(5)|$。若只考虑 $k=\pm1,\pm3,\pm5$，输出的交流功率（不含 $k=0$）中有多大比例在基波上？

</li>

<li>

为什么输出看起来已经比输入“更像正弦”？

</li>

</ol>

:::loesung
(a) $|S_p(0)|^2+2|S_p(1)|^2=0.25+2/\pi^2=0.25+0.2026=0.4526$，即 $0.5$ 的 90.5 %。

(b) $|G_p(k)|=|S_p(k)|/\sqrt{1+k^2}$：$|G_p(1)|=0.2251$，$|G_p(3)|=0.0336$，$|G_p(5)|=0.0125$。这些谐波的交流功率：$2(0.0507+0.0011+0.0002)=0.1039$。基波所占比例为 $0.0507/0.0519=97.5\,\%$。在输入端，对相同的谐波，这一比例仅为 86.9 %。

(c) $|H(kF)|=1/\sqrt{1+k^2}\approx1/k$：谐波次数越高，衰减就越强。剩下的主要是基波，而几乎只由基波构成的信号就几乎是正弦信号。
:::
:::

## 第 4 阶段：从周期信号到非周期信号

<span class="anker" id="stufe-4"></span>

:::zweck
单个脉冲不是周期的，但可以把它看作周期无限长的周期信号。在此过程中，求和变成了积分。
:::

**思路。** 把持续时间小于 $T$ 的脉冲 $s(t)$ 作周期延拓。这时级数的系数是一个固定函数的取值：

$$S_p(k)=\frac1T\int_{-\infty}^{\infty}s(t)\mathrm{e}^{-\mathrm{j}2\pi kFt}\mathrm{d} t=F\cdot S(kF),\qquad S(f)=\int_{-\infty}^{\infty}s(t)\mathrm{e}^{-\mathrm{j}2\pi ft}\mathrm{d} t.$$

若把周期加倍，谱线间隔 $F$ 减半，谱线以两倍的密度对同一包络 $S(f)$ 进行采样（图 [4](#abb-4)）。在极限 $T\to\infty$ 下，间隔 $F$ 变为微分 $\mathrm{d} f$，和式 $\sum_kS(kF)\mathrm{e}^{\mathrm{j}2\pi kFt}F$ 变为积分。

:::abbildung et3/k3grenz
矩形脉冲 $\operatorname{rect}(t)$ 分别以 $T=2$ s 和 $T=4$ s 作周期延拓。乘以 $T$ 后的傅里叶系数位于同一包络 $S(f)=\operatorname{si}(\pi f)$ 上，间隔为 $1/T$。当 $T\to\infty$ 时，它们无间隙地填满整条曲线。
:::

:::satz 定理 4.1 (傅里叶变换)
<span class="anker" id="satz-4-1"></span>

<span class="anker" id="gl-4-1"></span>
$$S(f)=\int_{-\infty}^{\infty}s(t)\,\mathrm{e}^{-\mathrm{j}2\pi ft}\,\mathrm{d} t,\qquad s(t)=\int_{-\infty}^{\infty}S(f)\,\mathrm{e}^{\mathrm{j}2\pi ft}\,\mathrm{d} f. \tag{4.1}$$

简记：$s(t)\;\circ\!\!-\!\!\bullet\;S(f)$ 或 $S(f)=\mathcal{F}\{s(t)\}$。
:::

⁠**如何理解：**$S(f)$ 是__频谱密度__：单位频率区间上的权重。若 $s$ 是以 V 为单位的电压，则 $S$ 的单位为 V/Hz。逆变换由所有振荡合成信号，每个振荡的权重为 $S(f)\,\mathrm{d} f$。存在的一个充分条件是 $\int|s(t)|\mathrm{d} t<\infty$。傅里叶变换就是虚轴上的拉普拉斯变换，$S(f)=S_{\mathcal{L}}(\mathrm{j}2\pi f)$，前提是虚轴位于收敛域内（[第 2 部分](/wissen/zh/elektrotechnik/3-semester/signale-und-systeme/laplace-transformation/laplace-transformation.html)）。

⁠**卷积变成乘积。**与[第 2 部分](/wissen/zh/elektrotechnik/3-semester/signale-und-systeme/laplace-transformation/laplace-transformation.html)一样：$s(t)*h(t)\;\circ\!\!-\!\!\bullet\;S(f)\,H(f)$。由 $s*\delta=s$ 得 $S(f)\cdot\mathcal{F}\{\delta\}=S(f)$，因此 $\delta(t)\;\circ\!\!-\!\!\bullet\;1$：狄拉克冲激以相同的权重包含所有频率。

**例：指数脉冲。** RC 电路的冲激响应 $h(t)=\frac1{RC}\varepsilon(t)\mathrm{e}^{-t/RC}$：

$$H(f)=\frac1{RC}\int_0^\infty\mathrm{e}^{-(1/RC+\mathrm{j}2\pi f)t}\mathrm{d} t=\frac{1}{1+\mathrm{j}2\pi f\,RC}.$$

这与交流分析（[第 1 部分](/wissen/zh/elektrotechnik/3-semester/signale-und-systeme/lti-systeme-und-faltung/lti-systeme-und-faltung.html)）得到的频率响应相同。因此，冲激响应包含了关于频率特性的全部信息。

:::frage $S_p(k)$ 与 $S(f)$ 除了一个是离散的之外，还有什么区别？
单位。$S_p(k)$ 是幅度（V）：第 $k$ 次谐波确实具有这样的强度。$S(f)$ 是密度（V/Hz）：在非周期信号中，没有哪个单独的频率具有有限的幅度；只有一个频带 $\Delta f$ 大约携带 $S(f)\,\Delta f$。这就是 $S_p(k)=F\cdot S(kF)$ 的原因：每条谱线代表宽度为 $F$ 的一个频带。
:::

:::aufgabe 练习 4 ★ 双边指数脉冲
<span class="anker" id="aufg-4"></span>

对 $a>0$，把积分分成 $t<0$ 和 $t>0$ 两部分，计算 $\mathcal{F}\{\mathrm{e}^{-a|t|}\}$。证明结果是实的偶函数，并用信号的对称性解释这一点。

:::loesung
$$\int_{-\infty}^0\mathrm{e}^{at}\mathrm{e}^{-\mathrm{j}2\pi ft}\mathrm{d} t+\int_0^\infty\mathrm{e}^{-at}\mathrm{e}^{-\mathrm{j}2\pi ft}\mathrm{d} t=\frac{1}{a-\mathrm{j}2\pi f}+\frac{1}{a+\mathrm{j}2\pi f}=\frac{2a}{a^2+(2\pi f)^2}.$$

结果是 $f$ 的实偶函数。必然如此：信号是实的偶函数，所以其奇部为零，因而 $\operatorname{Im} S$ 也为零（第 [5](#stufe-5) 阶段）。
:::
:::

## 第 5 阶段：信号与频谱中的对称性

<span class="anker" id="stufe-5"></span>

:::zweck
信号是实的、偶的还是奇的，可以直接从其频谱看出。本阶段推导相应的规则。
:::

**偶部与奇部。** 若复函数满足 $x(t)=x^*(-t)$，则称它为__偶__函数；若满足 $x(t)=-x^*(-t)$，则称它为__奇__函数。（对实函数而言，这就是通常的镜像对称和关于原点的点对称。）每个信号都可以唯一地分解为这两部分：

<span class="anker" id="gl-5-1"></span>
$$s(t)=s_g(t)+s_u(t),\qquad s_g(t)=\tfrac12\bigl[s(t)+s^*(-t)\bigr],\qquad s_u(t)=\tfrac12\bigl[s(t)-s^*(-t)\bigr]. \tag{5.1}$$

:::satz 定理 5.1 (对称性)
<span class="anker" id="satz-5-1"></span>

<span class="anker" id="gl-5-2"></span>
$$s_g(t)\;\circ\!\!-\!\!\bullet\;\operatorname{Re}\{S(f)\},\qquad s_u(t)\;\circ\!\!-\!\!\bullet\;\mathrm{j}\operatorname{Im}\{S(f)\}. \tag{5.2}$$

对**实**信号有 $S(-f)=S^*(f)$：实部和模 $|S|$ 是 $f$ 的偶函数，虚部和相位是奇函数。实的偶信号具有实的偶频谱。实的奇信号具有纯虚的奇频谱。
:::

:::herleitung 对称性
首先：$\mathcal{F}\{s^*(-t)\}=\int s^*(-t)\mathrm{e}^{-\mathrm{j}2\pi ft}\mathrm{d} t$。令 $\tau=-t$，则该式等于 $\int s^*(\tau)\mathrm{e}^{\mathrm{j}2\pi f\tau}\mathrm{d}\tau=\bigl(\int s(\tau)\mathrm{e}^{-\mathrm{j}2\pi f\tau}\mathrm{d}\tau\bigr)^*=S^*(f)$。因此

$$\mathcal{F}\{s_g\}=\tfrac12\bigl[S(f)+S^*(f)\bigr]=\operatorname{Re}\{S(f)\},\qquad\mathcal{F}\{s_u\}=\tfrac12\bigl[S(f)-S^*(f)\bigr]=\mathrm{j}\operatorname{Im}\{S(f)\}.$$

对实信号 $s$ 有 $\mathcal{F}\{s^*(t)\}=\mathcal{F}\{s(t)\}$。一般地，$\mathcal{F}\{s^*(t)\}=\int s^*\mathrm{e}^{-\mathrm{j}2\pi ft}\mathrm{d} t=\bigl(\int s\,\mathrm{e}^{\mathrm{j}2\pi ft}\mathrm{d} t\bigr)^*=S^*(-f)$。所以 $S(f)=S^*(-f)$。
:::

⁠**简而言之：**对实信号而言，频谱的负半部分是正半部分的共轭镜像，不包含任何新的信息。

**例。** 指数脉冲 $\varepsilon(t)\mathrm{e}^{-t}$（实信号）的偶部为 $\frac12\mathrm{e}^{-|t|}$，奇部为 $\frac12\operatorname{sgn}(t)\mathrm{e}^{-|t|}$。其频谱 $H(f)=\frac{1}{1+\mathrm{j}2\pi f}$ 的实部 $\frac{1}{1+(2\pi f)^2}$ 是偶函数，正是 $\frac12\mathrm{e}^{-|t|}$ 的变换；虚部 $\frac{-2\pi f}{1+(2\pi f)^2}$ 是奇函数（图 [5](#abb-5)）。

:::abbildung et3/k3gerade
指数脉冲（$RC=1$ s）分解为偶部（蓝）和奇部（红）。右图：频谱。偶部给出实部（$f$ 的偶函数），奇部给出虚部（$f$ 的奇函数）。
:::

:::aufgabe 练习 5 ★ 由对称性判断
<span class="anker" id="aufg-5"></span>

无需计算，关于频谱可以得出什么结论？(a) $s(t)=\operatorname{rect}(t)$，(b) $s(t)=\operatorname{sgn}(t)\operatorname{rect}(t/2)$，(c) $s(t)=\mathrm{e}^{\mathrm{j}2\pi t}\operatorname{rect}(t)$，(d) 一个实信号满足 $S(1\,\mathrm{Hz})=2-3\mathrm{j}$：$S(-1\,\mathrm{Hz})$ 是多少？

:::loesung
(a) 实且偶：频谱为实偶函数（$\operatorname{si}(\pi f)$）。 (b) 实且奇：频谱为纯虚奇函数。 (c) 复信号，但 $x^*(-t)=\mathrm{e}^{-\mathrm{j}2\pi(-t)}\operatorname{rect}(-t)=x(t)$：按定义的意义，该信号是偶的，因此其频谱是实的。由调制定理，频谱为 $\operatorname{si}(\pi(f-1))$，是实的，但不关于 $f=0$ 对称，因为信号不是实的。 (d) $S(-1\,\mathrm{Hz})=S^*(1\,\mathrm{Hz})=2+3\mathrm{j}$。
:::
:::

## 第 6 阶段：运算规则（定理）

<span class="anker" id="stufe-6"></span>

:::zweck
不必每次都重新计算积分，而是使用规则：信号被平移、压缩、求导或调制时，频谱会怎样变化？每条规则都可以由该运算对单个振荡的作用推出。
:::

:::satz 定理 6.1 (傅里叶变换的定理)
<span class="anker" id="satz-6-1"></span>

<span class="anker" id="gl-6-1"></span>
<span class="anker" id="gl-6-2"></span>
<span class="anker" id="gl-6-3"></span>
<span class="anker" id="gl-6-4"></span>
<span class="anker" id="gl-6-5"></span>
<span class="anker" id="gl-6-6"></span>
<span class="anker" id="gl-6-7"></span>
<span class="anker" id="gl-6-8"></span>
<span class="anker" id="gl-6-9"></span>
<span class="anker" id="gl-6-10"></span>
<span class="anker" id="gl-6-11"></span>
$$\begin{aligned} &\text{叠加：} && \textstyle\sum_ia_is_i(t)\;\circ\!\!-\!\!\bullet\;\sum_ia_iS_i(f)\\ &\text{共轭：} && s^*(t)\;\circ\!\!-\!\!\bullet\;S^*(-f)\\ &\text{尺度变换：} && s(bt)\;\circ\!\!-\!\!\bullet\;\frac{1}{|b|}S\Bigl(\frac fb\Bigr),\quad b\neq0;\qquad s(-t)\;\circ\!\!-\!\!\bullet\;S(-f)\\ &\text{时移：} && s(t-t_0)\;\circ\!\!-\!\!\bullet\;S(f)\,\mathrm{e}^{-\mathrm{j}2\pi ft_0},\qquad\delta(t-t_0)\;\circ\!\!-\!\!\bullet\;\mathrm{e}^{-\mathrm{j}2\pi ft_0}\\ &\text{微分：} && \frac{\mathrm{d}^n}{\mathrm{d} t^n}s(t)\;\circ\!\!-\!\!\bullet\;(\mathrm{j}2\pi f)^nS(f)\\ &\text{对偶性：} && S(t)\;\circ\!\!-\!\!\bullet\;s(-f)\\ &\text{调制：} && \mathrm{e}^{\mathrm{j}2\pi Ft}s(t)\;\circ\!\!-\!\!\bullet\;S(f-F)\\ &\text{频域微分：} && -\mathrm{j}2\pi t\,s(t)\;\circ\!\!-\!\!\bullet\;\frac{\mathrm{d}}{\mathrm{d} f}S(f)\\ &\text{卷积、相乘：} && s_1*s_2\;\circ\!\!-\!\!\bullet\;S_1S_2,\qquad s_1s_2\;\circ\!\!-\!\!\bullet\;S_1*S_2\\ &\text{面积：} && \int s(t)\mathrm{d} t=S(0),\qquad\int S(f)\mathrm{d} f=s(0)\\ &\text{帕塞瓦尔定理：} && \int|s(t)|^2\mathrm{d} t=\int|S(f)|^2\mathrm{d} f \end{aligned} \tag{6.1|6.2|6.3|6.4|6.5|6.6|6.7|6.8|6.9|6.10|6.11}$$
:::

⁠**如何理解其中最重要的几条：**

<ul>

<li>

⁠**尺度变换：**在时间上压缩的信号（$|b|>1$）具有更宽的频谱。短信号需要许多频率。持续时间与带宽成反比关系。

</li>

<li>

⁠**时移：**延迟不改变模，只改变相位，而且相位随 $f$ 线性变化：每个振荡都被移动相同的时间，而频率越高，这段时间对应的角度就越大。

</li>

<li>

⁠**微分：**$\frac{\mathrm{d}}{\mathrm{d} t}\mathrm{e}^{\mathrm{j}2\pi ft}=\mathrm{j}2\pi f\,\mathrm{e}^{\mathrm{j}2\pi ft}$。微分会放大高频。

</li>

<li>

⁠**对偶性：**正变换与逆变换只在指数的符号上不同。因此，每个变换对都会给出另一个角色互换的变换对。

</li>

<li>

⁠**调制：**乘以 $\mathrm{e}^{\mathrm{j}2\pi Ft}$ 使整个频谱移动 $F$。每台无线电发射机都是这样工作的。

</li>

<li>

⁠**相乘：**两个信号乘积的频谱是两者频谱的卷积，这是卷积定理的对应形式。

</li>

<li>

⁠**帕塞瓦尔定理：**能量在两个域中相同。$|S(f)|^2$ 是按频率分布的__能量谱密度__。

</li>

</ul>

:::herleitung 尺度变换、时移、微分、对偶性、调制、相乘、帕塞瓦尔定理
⁠**尺度变换**（$b>0$，$\tau=bt$）：$\int s(bt)\mathrm{e}^{-\mathrm{j}2\pi ft}\mathrm{d} t=\frac1b\int s(\tau)\mathrm{e}^{-\mathrm{j}2\pi(f/b)\tau}\mathrm{d}\tau=\frac1bS(f/b)$。当 $b<0$ 时积分上下限互换，因此为 $1/|b|$。

⁠**时移**（$\tau=t-t_0$）：$\int s(\tau)\mathrm{e}^{-\mathrm{j}2\pi f(\tau+t_0)}\mathrm{d}\tau=\mathrm{e}^{-\mathrm{j}2\pi ft_0}S(f)$。令 $s=\delta$，即得 $\delta(t-t_0)$ 的变换对。

⁠**微分：**将逆变换对 $t$ 求导：$\frac{\mathrm{d}}{\mathrm{d} t}\int S\mathrm{e}^{\mathrm{j}2\pi ft}\mathrm{d} f=\int\mathrm{j}2\pi f\,S\,\mathrm{e}^{\mathrm{j}2\pi ft}\mathrm{d} f$。

⁠**对偶性：**在逆变换中用 $-t$ 代替 $t$：$s(-t)=\int S(f)\mathrm{e}^{-\mathrm{j}2\pi ft}\mathrm{d} f$。再把变量名 $t$ 和 $f$ 互换：$s(-f)=\int S(t)\mathrm{e}^{-\mathrm{j}2\pi ft}\mathrm{d} t$，这正是 $S(t)$ 的正变换。

⁠**调制：**$\int\mathrm{e}^{\mathrm{j}2\pi Ft}s(t)\mathrm{e}^{-\mathrm{j}2\pi ft}\mathrm{d} t=\int s(t)\mathrm{e}^{-\mathrm{j}2\pi(f-F)t}\mathrm{d} t=S(f-F)$。频域微分可用同样的方法，将正变换对 $f$ 求导得到。

⁠**相乘：**对信号 $s_1(t)$ 和 $s_2(t)$ 应用卷积定理，即 $s_1*s_2\;\circ\!\!-\!\!\bullet\;S_1S_2$，再对这个变换对应用对偶性：$S_1(t)S_2(t)\;\circ\!\!-\!\!\bullet\;s_1(-f)*s_2(-f)$。重新命名即得式 [(6.9)](#gl-6-9)。

⁠**面积：**在正变换中令 $f=0$，在逆变换中令 $t=0$。

⁠**帕塞瓦尔定理：**$\int|s|^2\mathrm{d} t=\int s\,s^*\mathrm{d} t$ 是乘积 $s(t)s^*(t)$ 的积分，因此由相乘、共轭和面积定理，它等于 $\bigl[S(f)*S^*(-f)\bigr]_{f=0}=\int S(\nu)S^*(\nu)\mathrm{d}\nu$。
:::

:::frage 为什么延迟不改变频谱的模？
因为延迟既不衰减也不放大任何振荡，只是把每个振荡平移。每个振荡都被平移相同的时间 $t_0$，在频率 $f$ 处，这对应于角度 $2\pi ft_0$。因此，相位是 $f$ 的一条直线，斜率为 $-2\pi t_0$。$|H|=1$ 且相位为线性的系统，会使信号延迟而不改变其形状。
:::

:::aufgabe 练习 6 ★★ 应用定理
<span class="anker" id="aufg-6"></span>

利用 $\operatorname{rect}(t)\;\circ\!\!-\!\!\bullet\;\operatorname{si}(\pi f)$（第 [7](#stufe-7) 阶段）和上述定理。

<ol class="al">

<li>

求从 $t=0$ 到 $t=2$ s、高度为 1 的矩形脉冲的频谱。它在 $f=0$ 处的模是多少？第一个零点在哪里？

</li>

<li>

求 $F_0=5$ Hz 时 $\cos(2\pi F_0t)\operatorname{rect}(t)$ 的频谱，并画出草图。

</li>

</ol>

:::loesung
(a) 该脉冲为 $\operatorname{rect}\bigl(\frac{t-1}{2}\bigr)$。由尺度变换（$T=2$）和时移（$t_0=1$ s）得：$2\operatorname{si}(2\pi f)\,\mathrm{e}^{-\mathrm{j}2\pi f}$。$f=0$ 处的模为 2（即面积）。第一个零点在 $f=0.5$ Hz。时移只改变相位。

(b) $\cos(2\pi F_0t)=\frac12\mathrm{e}^{\mathrm{j}2\pi F_0t}+\frac12\mathrm{e}^{-\mathrm{j}2\pi F_0t}$，由调制定理得：$\frac12\operatorname{si}(\pi(f-5))+\frac12\operatorname{si}(\pi(f+5))$。即位于 $\pm5$ Hz 处的两个高度为 $\frac12$ 的 si 主瓣，第一个零点分别在其两侧 1 Hz 处。
:::
:::

:::aufgabe 练习 7 ★★ 以对偶性为工具
<span class="anker" id="aufg-7"></span>

由练习 [4](#aufg-4) 可知 $\mathrm{e}^{-|t|}\;\circ\!\!-\!\!\bullet\;\frac{2}{1+(2\pi f)^2}$。不用积分，利用这一结果求 $\frac{1}{1+t^2}$ 的频谱。

:::loesung
对该变换对应用对偶性：$\frac{2}{1+(2\pi t)^2}\;\circ\!\!-\!\!\bullet\;\mathrm{e}^{-|f|}$。再对时间轴进行展缩。令 $x(t)=\frac{2}{1+(2\pi t)^2}$，则 $x\bigl(\frac{t}{2\pi}\bigr)=\frac{2}{1+t^2}$，因此由尺度变换定理（$b=\frac1{2\pi}$）得 $\frac{2}{1+t^2}\;\circ\!\!-\!\!\bullet\;2\pi\,\mathrm{e}^{-2\pi|f|}$。两边除以 2 得

$$\frac{1}{1+t^2}\;\circ\!\!-\!\!\bullet\;\pi\,\mathrm{e}^{-2\pi|f|}.$$

用面积定理验证：$\int\frac{\mathrm{d} t}{1+t^2}=\pi=S(0)$。
:::
:::

## 第 7 阶段：矩形、si 函数与三角形

<span class="anker" id="stufe-7"></span>

:::zweck
有三个变换对经常出现。借助上述定理，它们都可以由一次计算得到。
:::

**矩形。** 利用 $\operatorname{si}(x)=\sin(x)/x$：

$$\int_{-1/2}^{1/2}\mathrm{e}^{-\mathrm{j}2\pi ft}\mathrm{d} t=\frac{\mathrm{e}^{-\mathrm{j}\pi f}-\mathrm{e}^{\mathrm{j}\pi f}}{-\mathrm{j}2\pi f}=\frac{\sin(\pi f)}{\pi f}=\operatorname{si}(\pi f).$$

:::satz 定理 7.1 (矩形、si 函数与三角形)
<span class="anker" id="satz-7-1"></span>

<span class="anker" id="gl-7-1"></span>
<span class="anker" id="gl-7-2"></span>
<span class="anker" id="gl-7-3"></span>
<span class="anker" id="gl-7-4"></span>
$$\begin{aligned} \operatorname{rect}\Bigl(\frac tT\Bigr)&\;\circ\!\!-\!\!\bullet\;|T|\operatorname{si}(\pi Tf),\\ \operatorname{si}\Bigl(\frac{\pi t}{T}\Bigr)&\;\circ\!\!-\!\!\bullet\;|T|\operatorname{rect}(Tf),\\ \Lambda(t)=\operatorname{rect}(t)*\operatorname{rect}(t)&\;\circ\!\!-\!\!\bullet\;\operatorname{si}^2(\pi f),\\ \operatorname{si}(\pi t)*\operatorname{si}(\pi t)&=\operatorname{si}(\pi t). \end{aligned} \tag{7.1|7.2|7.3|7.4}$$
:::

⁠**如何理解：**持续时间为 $T$ 的矩形，其频谱的高度为 $T$（即矩形的面积），零点位于 $1/T$ 的所有非零整数倍处。时长加倍，频谱宽度就减半（图 [6](#abb-6)）。式 [(7.2)](#gl-7-2) 由对偶性得到，式 [(7.3)](#gl-7-3) 由卷积定理得到；式 [(7.4)](#gl-7-4) 成立，是因为在频域中 $\operatorname{rect}(f)\cdot\operatorname{rect}(f)=\operatorname{rect}(f)$：理想低通滤波器不会改变已经限制在其通带内的信号。

:::abbildung et3/k3rectsi
$\operatorname{rect}(t/T)$ 及其频谱 $|T|\operatorname{si}(\pi Tf)$，$T=1$ s 和 $T=2$ s。持续时间加倍：高度加倍（$=$ 面积），宽度减半，第一个零点位于 $1/T$。
:::

:::ltspice 矩形脉冲的频谱
⁠**绘制：**只需一个电压源 `voltage`，取 `PULSE(0 1 0 1u 1u {T0} 16)`：持续时间为 $T_0$ 的矩形，每 16 s 重复一次。

⁠**指令：**`.param T0=1`，`.step param T0 list 1 2`，`.tran 0 16 0 1m`，再加上用来关闭数据压缩的 `.options plotwinsize=0` 和 `.four 0.0625 40 V(in)`。

⁠**你会看到：**每 16 s 重复一次，使频谱变成间隔为 $1/16$ Hz 的谱线（第 [4](#stufe-4) 阶段）。`.four` 给出它们的幅度 $\frac{2}{16}\,|T_0\operatorname{si}(\pi T_0f)|$，即 si 包络的采样值。$T_0=1$ s 时，1 Hz 和 2 Hz 处的谱线为零；$T_0=2$ s 时，0.5 Hz、1 Hz、1.5 Hz 和 2 Hz 处的谱线都已为零。直流分量从 0.0625 加倍到 0.125。因此，持续时间加倍意味着宽度减半、高度加倍，与图 [6](#abb-6) 相同。在 FFT 视图中可以直接看到包络及其零点。
:::

:::aufgabe 练习 8 ★ si 函数的面积与能量
<span class="anker" id="aufg-8"></span>

不用积分，计算 $\int_{-\infty}^\infty\operatorname{si}(\pi t)\mathrm{d} t$ 和 $\int_{-\infty}^\infty\operatorname{si}^2(\pi t)\mathrm{d} t$。利用面积定理和帕塞瓦尔定理。

:::loesung
面积定理：$\int\operatorname{si}(\pi t)\mathrm{d} t=\mathcal{F}\{\operatorname{si}(\pi t)\}(0)=\operatorname{rect}(0)=1$。帕塞瓦尔定理：$\int\operatorname{si}^2(\pi t)\mathrm{d} t=\int\operatorname{rect}^2(f)\mathrm{d} f=1$。
:::
:::

:::aufgabe 练习 9 ★★ 三角形与多次卷积
<span class="anker" id="aufg-9"></span>

<ol class="al">

<li>

求 $\Lambda(t/2)$（半宽为 2 s 的三角形）的频谱。零点在哪里？

</li>

<li>

$\operatorname{rect}*\operatorname{rect}*\operatorname{rect}$ 的频谱是什么？为什么卷积的次数越多，旁瓣衰减得越快？

</li>

</ol>

:::loesung
(a) $\Lambda(t)\circ\!\!-\!\!\bullet\operatorname{si}^2(\pi f)$，再由 $T=2$ 的尺度变换得：$\Lambda(t/2)\circ\!\!-\!\!\bullet\,2\operatorname{si}^2(2\pi f)$。零点位于 $f=k/2$，$k\neq0$。

(b) $\operatorname{si}^3(\pi f)$。每多卷积一次，频谱就多乘一个 $\operatorname{si}(\pi f)$，而它在旁瓣中按 $1/(\pi f)$ 衰减。对 $M$ 重卷积，旁瓣按 $1/f^M$ 衰减。在时域中：矩形有跳变（按 $1/f$ 衰减），三角形有折点（$1/f^2$），三重卷积的导数是连续的（$1/f^3$）。信号越光滑，其频谱衰减越快。
:::
:::

## 第 8 阶段：奇异信号与线谱

<span class="anker" id="stufe-8"></span>

:::zweck
常数、振荡、阶跃和周期信号都不是绝对可积的。借助频谱中的狄拉克冲激，它们仍然可以进行变换。这样，傅里叶级数与傅里叶积分就统一起来了。
:::

:::satz 定理 8.1 (奇异变换对)
<span class="anker" id="satz-8-1"></span>

<span class="anker" id="gl-8-1"></span>
<span class="anker" id="gl-8-2"></span>
<span class="anker" id="gl-8-3"></span>
<span class="anker" id="gl-8-4"></span>
<span class="anker" id="gl-8-5"></span>
<span class="anker" id="gl-8-6"></span>
<span class="anker" id="gl-8-7"></span>
$$\begin{aligned} \delta(t)&\;\circ\!\!-\!\!\bullet\;1, & c&\;\circ\!\!-\!\!\bullet\;c\,\delta(f),\\ \mathrm{e}^{\mathrm{j}2\pi Ft}&\;\circ\!\!-\!\!\bullet\;\delta(f-F), & \cos(2\pi Ft)&\;\circ\!\!-\!\!\bullet\;\tfrac12\delta(f+F)+\tfrac12\delta(f-F),\\ & & \sin(2\pi Ft)&\;\circ\!\!-\!\!\bullet\;\tfrac{\mathrm{j}}{2}\delta(f+F)-\tfrac{\mathrm{j}}{2}\delta(f-F),\\ \textstyle\sum_kS_p(k)\mathrm{e}^{\mathrm{j}2\pi kFt}&\;\circ\!\!-\!\!\bullet\;\textstyle\sum_kS_p(k)\,\delta(f-kF),\\ \textstyle\sum_n\delta(t-nT)&\;\circ\!\!-\!\!\bullet\;\frac{1}{|T|}\textstyle\sum_k\delta\Bigl(f-\frac kT\Bigr),\\ \varepsilon(t)&\;\circ\!\!-\!\!\bullet\;\tfrac12\delta(f)+\frac{1}{\mathrm{j}2\pi f}, & \operatorname{sgn}(t)&\;\circ\!\!-\!\!\bullet\;\frac{1}{\mathrm{j}\pi f},\\ \int_{-\infty}^ts(\tau)\mathrm{d}\tau&\;\circ\!\!-\!\!\bullet\;\frac{S(f)}{\mathrm{j}2\pi f}+\tfrac12S(0)\,\delta(f). \end{aligned} \tag{8.1|8.2|8.3|8.4|8.5|8.6|8.7}$$
:::

⁠**如何理解：**

<ul>

<li>

常数是频率为 0 的振荡，它的频谱是 $f=0$ 处的一条谱线。振荡 $\mathrm{e}^{\mathrm{j}2\pi Ft}$ 是 $F$ 处的一条谱线。实余弦在 $\pm F$ 处有两条权重减半的谱线。

</li>

<li>

周期信号具有__线谱__：位于各次谐波处的狄拉克冲激，以傅里叶系数为权重。因此，傅里叶级数是傅里叶积分的一个特例。

</li>

<li>

__狄拉克梳状函数（冲激串）__，即间隔为 $T$ 的一串冲激，其频谱仍是狄拉克梳状函数，间隔为 $1/T$，权重为 $1/|T|$（图 [7](#abb-7)）。这个变换对在采样中（[第 4 部分](/wissen/zh/elektrotechnik/3-semester/signale-und-systeme/abtastung-und-zeitdiskrete-systeme/abtastung-und-zeitdiskrete-systeme.html)）将起决定性作用。

</li>

<li>

阶跃具有直流分量 $\frac12$（谱线 $\frac12\delta(f)$）和交流分量 $\frac12\operatorname{sgn}(t)$，后者的频谱按 $1/f$ 衰减。

</li>

</ul>

:::herleitung 奇异变换对
⁠**常数、振荡：**对 $\delta(t)\circ\!\!-\!\!\bullet\,1$ 应用对偶性：$1\circ\!\!-\!\!\bullet\,\delta(-f)=\delta(f)$。调制使谱线移动：$\mathrm{e}^{\mathrm{j}2\pi Ft}\cdot1\circ\!\!-\!\!\bullet\,\delta(f-F)$。余弦和正弦由欧拉公式得到。

⁠**线谱：**对所有谐波叠加。

⁠**狄拉克梳状函数：**它以 $T$ 为周期。其傅里叶系数为 $S_p(k)=\frac1T\int_{-T/2}^{T/2}\delta(t)\mathrm{e}^{-\mathrm{j}2\pi kFt}\mathrm{d} t=\frac1T$，对所有 $k$ 均成立。结合线谱即得式 [(8.5)](#gl-8-5)。

⁠**符号函数：**$\operatorname{sgn}(t)$ 是 $\operatorname{sgn}(t)\mathrm{e}^{-a|t|}$ 在 $a\to0$ 时的极限情况：

$$\int_0^\infty\mathrm{e}^{-(a+\mathrm{j}2\pi f)t}\mathrm{d} t-\int_{-\infty}^0\mathrm{e}^{(a-\mathrm{j}2\pi f)t}\mathrm{d} t=\frac{1}{a+\mathrm{j}2\pi f}-\frac{1}{a-\mathrm{j}2\pi f}=\frac{-\mathrm{j}4\pi f}{a^2+(2\pi f)^2}\;\xrightarrow{a\to0}\;\frac{1}{\mathrm{j}\pi f}.$$

⁠**阶跃：**$\varepsilon(t)=\frac12+\frac12\operatorname{sgn}(t)$，因此为 $\frac12\delta(f)+\frac{1}{\mathrm{j}2\pi f}$。

⁠**积分：**$\int_{-\infty}^ts\,\mathrm{d}\tau=s*\varepsilon$，再利用卷积定理和筛选性质 $S(f)\delta(f)=S(0)\delta(f)$。
:::

:::abbildung et3/k3kamm
$T=0.5$ s 的狄拉克梳状函数及其频谱：仍是梳状函数，间隔为 $1/T=2$ Hz，权重为 $1/T=2$。时域中冲激越密，谱线相距越远。
:::

:::frage 可是由 $\frac{\mathrm{d}}{\mathrm{d} t}\varepsilon=\delta$ 可得 $\mathrm{j}2\pi f\,S(f)=1$，所以 $S(f)=\frac{1}{\mathrm{j}2\pi f}$。那么 $\frac12\delta(f)$ 是从哪里来的？
方程 $\mathrm{j}2\pi f\,S(f)=1$ 只在 $f\neq0$ 处确定 $S$。在 $f=0$ 处，左边为 $0\cdot S(0)$；$S$ 中若含有一项 $c\,\delta(f)$，它会因 $f\delta(f)=0$ 而被消去。这与求导会“遗忘”常数相对应：$\varepsilon(t)$ 与 $\varepsilon(t)+b$ 具有相同的导数。哪个常数是正确的，由偶部决定：$\varepsilon$ 的平均值为 $\frac12$，所以 $c=\frac12$。
:::

**例：接通的余弦。** $\varepsilon(t)\cos(2\pi Ft)$。相乘变为卷积，而与狄拉克冲激卷积就是平移：

$$\Bigl[\tfrac12\delta(f)+\tfrac{1}{\mathrm{j}2\pi f}\Bigr]*\tfrac12\bigl[\delta(f+F)+\delta(f-F)\bigr] =\tfrac14\bigl[\delta(f+F)+\delta(f-F)\bigr]-\frac{\mathrm{j}}{4\pi}\Bigl[\frac{1}{f+F}+\frac{1}{f-F}\Bigr].$$

除了 $\pm F$ 处减半的谱线外，还出现了一个宽的频谱：接通过程本身包含 $\pm F$ 附近的频率。

:::aufgabe 练习 10 ★ 线谱
<span class="anker" id="aufg-10"></span>

<ol class="al">

<li>

给出 $s(t)=3+2\cos(2\pi\cdot50\,\mathrm{Hz}\cdot t)$ 的频谱，并画出草图。

</li>

<li>

给出参考模型中方波在 $|f|\le0.5$ Hz 范围内的频谱。

</li>

</ol>

:::loesung
(a) $3\,\delta(f)+\delta(f-50\,\mathrm{Hz})+\delta(f+50\,\mathrm{Hz})$：零频处一条权重为 3 的谱线，$\pm50$ Hz 处两条权重为 1 的谱线。

(b) $F=0.159$ Hz。0.5 Hz 以内有 $k=0,\pm1,\pm2,\pm3$，但 $k=\pm2$ 不存在：

$$0.5\,\delta(f)+0.318\bigl[\delta(f-0.159)+\delta(f+0.159)\bigr]-0.106\bigl[\delta(f-0.477)+\delta(f+0.477)\bigr].$$
:::
:::

:::aufgabe 练习 11 ★★ 符号函数与积分
<span class="anker" id="aufg-11"></span>

<ol class="al">

<li>

用式 [(5.2)](#gl-5-2) 验证：$\operatorname{sgn}(t)$ 的频谱必定是纯虚的奇函数。

</li>

<li>

用式 [(8.7)](#gl-8-7) 计算 $\int_{-\infty}^t\operatorname{rect}(\tau)\mathrm{d}\tau$ 的频谱。这是什么信号？

</li>

</ol>

:::loesung
(a) $\frac{1}{\mathrm{j}\pi f}=-\frac{\mathrm{j}}{\pi f}$：纯虚；且 $-\frac{\mathrm{j}}{\pi(-f)}=+\frac{\mathrm{j}}{\pi f}$，所以是奇函数。这与实的奇信号相符。

(b) $\frac{\operatorname{si}(\pi f)}{\mathrm{j}2\pi f}+\frac12\delta(f)$。该信号是矩形的变上限积分：$t\le-\frac12$ 时为 0，然后是一段斜坡，在 $t=\frac12$ 处升到 1，此后恒为 1。它在全部时间上的平均值为 $\frac12$，因此有 $\frac12\delta(f)$。
:::
:::

## 第 9 阶段：希尔伯特变换与解析信号

<span class="anker" id="stufe-9"></span>

:::zweck
对于因果信号，频谱的实部与虚部相互关联：一个决定另一个。同样的计算还能得到一个只含正频率的信号。
:::

**因果信号。** 若 $t<0$ 时 $s(t)=0$，则偶部和奇部在 $t>0$ 时相等（均为 $\frac12s$），在 $t<0$ 时互为相反数。因此 $s_u(t)=s_g(t)\operatorname{sgn}(t)$，$s_g(t)=s_u(t)\operatorname{sgn}(t)$。在频域中，乘以 $\operatorname{sgn}$ 变为与 $\frac{1}{\mathrm{j}\pi f}$ 卷积：

:::satz 定理 9.1 (因果信号的希尔伯特关系)
<span class="anker" id="satz-9-1"></span>

对因果信号，

<span class="anker" id="gl-9-1"></span>
$$\operatorname{Re}\{S(f)\}=\operatorname{Im}\{S(f)\}*\frac{1}{\pi f},\qquad\operatorname{Im}\{S(f)\}=-\operatorname{Re}\{S(f)\}*\frac{1}{\pi f}. \tag{9.1}$$
:::

⁠**如何理解：**与 $\frac{1}{\pi f}$ 的卷积称为__希尔伯特变换__。对于因果系统，只要知道频率响应的实部就够了，虚部可由它求出。因此，因果性是对频谱的一个很强的约束。

**解析分量。** 利用*频域*中的阶跃，可以截去负频率：$S_+(f)=S(f)\,\varepsilon(f)$。由对偶性得 $\varepsilon(f)\;\bullet\!\!-\!\!\circ\;\frac12\delta(t)+\frac{\mathrm{j}}{2\pi t}$，因此

<span class="anker" id="gl-9-2"></span>
$$s_+(t)=\frac12s(t)+\frac{\mathrm{j}}{2}\,\hat s(t),\qquad\hat s(t)=s(t)*\frac{1}{\pi t}\;\circ\!\!-\!\!\bullet\;-\mathrm{j}\operatorname{sgn}(f)\,S(f). \tag{9.2}$$

$s_+$ 称为__解析分量__，$\hat s$ 称为 $s$ 的希尔伯特变换。对实信号有 $S_-(f)=S_+^*(-f)$，因此 $s_-=s_+^*$，且 $s(t)=s_++s_-=2\operatorname{Re}\{s_+(t)\}$。$s_+$ 的实部与虚部同样互为希尔伯特变换。

**希尔伯特变换器。** $h(t)=\frac{1}{\pi t}$ 的 LTI 系统具有 $H(f)=-\mathrm{j}\operatorname{sgn}(f)$：在所有频率上模均为 1（__全通__系统），$f>0$ 时相位为 $-90^\circ$，$f<0$ 时为 $+90^\circ$。它把 $\cos(2\pi Ft)$ 变为

$$\tfrac12\bigl[\delta(f+F)+\delta(f-F)\bigr]\cdot\bigl(-\mathrm{j}\operatorname{sgn}(f)\bigr)=\tfrac{\mathrm{j}}{2}\delta(f+F)-\tfrac{\mathrm{j}}{2}\delta(f-F)\;\bullet\!\!-\!\!\circ\;\sin(2\pi Ft).$$

⁠**简而言之：**希尔伯特变换器把每个振荡的相位移动 $90^\circ$，而不改变其幅度。

:::aufgabe 练习 12 ★★ 希尔伯特变换器
<span class="anker" id="aufg-12"></span>

<ol class="al">

<li>

希尔伯特变换器把 $\sin(2\pi Ft)$ 变成什么？应用两次得到什么？

</li>

<li>

求 $\cos(2\pi Ft)$ 的解析分量 $s_+(t)$，并验证 $s=2\operatorname{Re}\{s_+\}$。

</li>

<li>

为什么希尔伯特变换器不是因果的？请看 $h(t)$。

</li>

</ol>

:::loesung
(a) $\sin(2\pi Ft)\circ\!\!-\!\!\bullet\frac{\mathrm{j}}{2}\delta(f+F)-\frac{\mathrm{j}}{2}\delta(f-F)$。乘以 $-\mathrm{j}\operatorname{sgn}(f)$：在 $-F$ 处乘以 $+\mathrm{j}$，在 $+F$ 处乘以 $-\mathrm{j}$。结果：$-\frac12\delta(f+F)-\frac12\delta(f-F)$，即 $-\cos(2\pi Ft)$。应用两次：$(-\mathrm{j}\operatorname{sgn}f)^2=-1$，因此信号被反相。

(b) $S_+(f)=S(f)\varepsilon(f)=\frac12\delta(f-F)$，所以 $s_+(t)=\frac12\mathrm{e}^{\mathrm{j}2\pi Ft}=\frac12\bigl[\cos(2\pi Ft)+\mathrm{j}\sin(2\pi Ft)\bigr]$。这与 $\frac12(s+\mathrm{j}\hat s)$（其中 $\hat s=\sin$）一致。$2\operatorname{Re}\{s_+\}=\cos(2\pi Ft)$。

(c) $h(t)=\frac{1}{\pi t}$ 在 $t<0$ 时也不为零。因此，时刻 $t$ 的输出取决于未来的输入值。实际中，用截断的冲激响应来近似希尔伯特变换器，代价是引入一段延迟。
:::
:::

## 第 10 阶段：短时傅里叶变换

<span class="anker" id="stufe-10"></span>

:::zweck
频谱 $S(f)$ 描述的是信号在全部时间上的情况。然而，语音或音乐的频率在不断变化。短时傅里叶变换（STFT）要回答的问题是：信号*在时刻 $t$ 附近*包含哪些频率？
:::

**思路。** 截取 $t$ 附近的一个片段，只对这一片段进行变换。采用宽度为 $T_0$ 的矩形窗：

$$s_T(\tau,t)=s(\tau)\operatorname{rect}\Bigl(\frac{\tau-t}{T_0}\Bigr)\;\circ\!\!-\!\!\bullet\;S_T(f,t)=S(f)*\bigl[T_0\operatorname{si}(\pi T_0f)\,\mathrm{e}^{-\mathrm{j}2\pi tf}\bigr].$$

片段的频谱是真实频谱被窗的 si 频谱模糊之后的结果。短窗在时间上定位准确，但在频率上模糊严重（尺度变换定理）。矩形的硬边沿还会产生衰减缓慢的旁瓣。因此，平滑的窗更好，例如__汉宁窗__

<span class="anker" id="gl-10-1"></span>
$$w(\tau)=\tfrac12\Bigl[1+\cos\Bigl(\frac{2\pi\tau}{T_0}\Bigr)\Bigr]\operatorname{rect}\Bigl(\frac{\tau}{T_0}\Bigr)=\cos^2\Bigl(\frac{\pi\tau}{T_0}\Bigr)\operatorname{rect}\Bigl(\frac{\tau}{T_0}\Bigr). \tag{10.1}$$

:::satz 定理 10.1 (短时傅里叶变换)
<span class="anker" id="satz-10-1"></span>

<span class="anker" id="gl-10-2"></span>
$$S_T(f,t)=\int_{-\infty}^{\infty}s(\tau)\,w(\tau-t)\,\mathrm{e}^{-\mathrm{j}2\pi f\tau}\,\mathrm{d}\tau. \tag{10.2}$$

若依次平移 $T$ 的各个窗相加为常数，即 $\sum_nw(\tau-nT)=c$，则

<span class="anker" id="gl-10-3"></span>
$$s(\tau)=\frac1c\sum_ns(\tau)\,w(\tau-nT),\qquad S(f)=\frac1c\sum_nS_T(f,nT). \tag{10.3}$$
:::

⁠**如何理解：**$S_T(f,t)$ 是一个随时间变化的频谱。把 $|S_T|$ 作为 $t$ 和 $f$ 的函数画出来，就得到__语谱图（时频图）__。对于偏移量 $T=T_0/2$ 的汉宁窗，$c=1$，因为 $\cos^2x+\sin^2x=1$（图 [8](#abb-8)）：各片段无缝地拼合成整个信号，它们的频谱之和就是整个频谱。

:::abbildung et3/k3hann
宽度为 $T_0=2$ s 的汉宁窗，依次偏移 $T=1$ s（蓝）。它们的和处处恰好为 1（红）。
:::

:::aufgabe 练习 13 ★ 汉宁窗
<span class="anker" id="aufg-13"></span>

证明当 $T=T_0/2$ 时 $\sum_nw(\tau-nT)=1$。提示：每一点上恰好有两个窗重叠。把第二个窗用 $\cos^2(x-\frac\pi2)$ 表示。

:::loesung
对于 $T=T_0/2$，当 $\tau$ 位于 $nT$ 与 $(n+1)T$ 之间时，恰好只有第 $n$ 个和第 $n+1$ 个窗不为零。令 $x=\pi(\tau-nT)/T_0$：

$$w(\tau-nT)+w(\tau-(n+1)T)=\cos^2x+\cos^2\Bigl(x-\frac\pi2\Bigr)=\cos^2x+\sin^2x=1.$$
:::
:::

## 第 11 阶段：傅里叶变换与拉普拉斯变换——存在性的界限

<span class="anker" id="stufe-11"></span>

:::zweck
傅里叶积分在什么情况下存在？它与拉普拉斯变换有什么关系？
:::

存在的一个充分条件是绝对可积，即 $\int|s(t)|\mathrm{d} t<\infty$。拉普拉斯变换先用 $\mathrm{e}^{-\sigma t}$ 加权，从而扩大了可变换信号的范围（[第 2 部分](/wissen/zh/elektrotechnik/3-semester/signale-und-systeme/laplace-transformation/laplace-transformation.html)）：

$$S_{\mathcal{L}}(\sigma+\mathrm{j}2\pi f)=\mathcal{F}\bigl\{s(t)\mathrm{e}^{-\sigma t}\bigr\}(f).$$

因此，它从两个方面考察信号：像傅里叶变换一样考察频率分量，同时考察指数增长或衰减。若 $\sigma=0$ 位于收敛域内，傅里叶变换就是虚轴上的拉普拉斯变换。但借助狄拉克冲激（第 [8](#stufe-8) 阶段），傅里叶变换还能处理拉普拉斯变换处理不了的信号：在全部时间上存在的常数和振荡。一般而言，只要对每个 $c>0$ 都有 $\int|s(t)|\mathrm{e}^{-c|t|}\mathrm{d} t<\infty$ 就足够了。这时信号可以像幂函数 $t^n$ 那样增长，但不能按指数增长。

:::zusatz 为什么多次卷积会趋于高斯曲线
把 $\operatorname{rect}(t)$ 与自身作 $M$ 重卷积，其频谱为 $\operatorname{si}^M(\pi f)$。对小的 $f$，$\operatorname{si}(\pi f)\approx1-\frac{(\pi f)^2}{6}$，且 $\ln(1+w)\approx w$，因此

$$\operatorname{si}^M(\pi f)=\mathrm{e}^{M\ln\operatorname{si}(\pi f)}\approx\mathrm{e}^{-M(\pi f)^2/6}\;\bullet\!\!-\!\!\circ\;\sqrt{\frac{6}{\pi M}}\,\mathrm{e}^{-6t^2/M}.$$

对大的 $M$，只有小 $f$ 的区域有贡献，近似也就越来越好。$M=4$ 时，$t=0$ 处的精确值为 $0.667$，高斯曲线给出 $0.691$。这是__中心极限定理__（见统计部分）的一个实例：许多面积有限的正脉冲的卷积趋近于高斯曲线。一个例子是由许多短时积分器级联而成的系统的冲激响应。
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

:::kern 要点
<ul>

<li>

$\mathrm{e}^{\mathrm{j}2\pi ft}*h=H(f)\mathrm{e}^{\mathrm{j}2\pi ft}$；$H(f)=\int h\,\mathrm{e}^{-\mathrm{j}2\pi ft}\mathrm{d} t$。

</li>

<li>

级数：$s_p=\sum S_p(k)\mathrm{e}^{\mathrm{j}2\pi kFt}$，$S_p(k)=\frac1T\int_Ts_p\mathrm{e}^{-\mathrm{j}2\pi kFt}\mathrm{d} t$；实信号：$S_p(-k)=S_p^*(k)$。

</li>

<li>

帕塞瓦尔定理：$\frac1T\int_T|s_p|^2=\sum|S_p(k)|^2$；吉布斯现象：跳变处约 9 % 的过冲；LTI：$G_p(k)=S_p(k)H(kF)$。

</li>

<li>

$S(f)=\int s\,\mathrm{e}^{-\mathrm{j}2\pi ft}\mathrm{d} t$，$s=\int S\mathrm{e}^{\mathrm{j}2\pi ft}\mathrm{d} f$；$s*h\leftrightarrow SH$，$s_1s_2\leftrightarrow S_1*S_2$。

</li>

<li>

实信号：$S(-f)=S^*(f)$；偶部 $\leftrightarrow\operatorname{Re} S$，奇部 $\leftrightarrow\mathrm{j}\operatorname{Im} S$。

</li>

<li>

$s(bt)\leftrightarrow\frac1{|b|}S(f/b)$；$s(t-t_0)\leftrightarrow S\mathrm{e}^{-\mathrm{j}2\pi ft_0}$；$\frac{\mathrm{d}}{\mathrm{d} t}\leftrightarrow\mathrm{j}2\pi f$；$\mathrm{e}^{\mathrm{j}2\pi Ft}s\leftrightarrow S(f-F)$；$S(t)\leftrightarrow s(-f)$。

</li>

<li>

$\operatorname{rect}(t/T)\leftrightarrow|T|\operatorname{si}(\pi Tf)$；$\Lambda\leftrightarrow\operatorname{si}^2$；$\delta\leftrightarrow1$；$1\leftrightarrow\delta(f)$；$\cos\leftrightarrow\frac12[\delta(f+F)+\delta(f-F)]$。

</li>

<li>

梳状函数 $\leftrightarrow$ 梳状函数：$\sum\delta(t-nT)\leftrightarrow\frac1{|T|}\sum\delta(f-k/T)$；$\varepsilon\leftrightarrow\frac12\delta(f)+\frac{1}{\mathrm{j}2\pi f}$。

</li>

<li>

希尔伯特变换：$h=\frac{1}{\pi t}$，$H=-\mathrm{j}\operatorname{sgn}(f)$；$s_+=\frac12(s+\mathrm{j}\hat s)$，$s=2\operatorname{Re} s_+$。

</li>

</ul>
:::
