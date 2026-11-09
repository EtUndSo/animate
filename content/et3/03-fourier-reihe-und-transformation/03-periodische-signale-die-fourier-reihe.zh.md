---
title: 第 2 阶段：周期信号——傅里叶级数
pfad: 电气工程 / 第 3 学期 / 信号与系统 / 傅里叶级数与变换
order: 3230300
summary: 周期信号每经过 T 就重复一次。它可以由振荡构成，但只能由非常特定的振荡构成。本阶段说明是哪些振荡，以及如何求出它们的权重。
tags: 基频, 谐波, 傅里叶级数, 直流分量, 正交
lang: zh
---

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

周期为 $T=1/F$、功率有限（$|s(t)|^2$ 在一个周期内的平均值有限）的信号可以表示为式 [(2.1)](#gl-2-1)，其中

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

::::beispiel 有限级数
$s_p(t)=1+2\cos(2\pi Ft)+\sin(4\pi Ft)$。利用欧拉公式，无需积分即可读出系数：

$$2\cos(2\pi Ft)=\mathrm{e}^{\mathrm{j}2\pi Ft}+\mathrm{e}^{-\mathrm{j}2\pi Ft},\qquad\sin(4\pi Ft)=\frac{1}{2\mathrm{j}}\mathrm{e}^{\mathrm{j}4\pi Ft}-\frac{1}{2\mathrm{j}}\mathrm{e}^{-\mathrm{j}4\pi Ft},$$

所以 $S_p(0)=1$，$S_p(\pm1)=1$，$S_p(2)=-\tfrac{\mathrm{j}}{2}$，$S_p(-2)=\tfrac{\mathrm{j}}{2}$，其余均为零。验证：$S_p(-2)=S_p^*(2)$。
::::

::::beispiel 方波
对参考模型（$|t|\le T_1/2$ 时为 1，$T_1=T/2$）：

<span class="anker" id="gl-2-6"></span>
$$S_p(0)=\frac{T_1}{T},\qquad S_p(k)=\frac1T\int_{-T_1/2}^{T_1/2}\mathrm{e}^{-\mathrm{j}2\pi kFt}\mathrm{d} t=\frac{\sin(\pi kT_1/T)}{\pi k}\quad(k\neq0). \tag{2.6}$$

当 $T_1=T/2$ 时：$S_p(0)=0.5$，$S_p(\pm1)=1/\pi=0.318$，$S_p(\pm2)=0$，$S_p(\pm3)=-0.106$，$S_p(\pm5)=0.064$。缺少偶次谐波，因为对偶数 $k$ 有 $\sin(\pi k/2)=0$。所有系数都是实数，因为信号是偶函数，$s(-t)=s(t)$：$S_p(k)$ 的虚部为 $-\frac1T\int_{-T/2}^{T/2}s(t)\sin(2\pi kFt)\,\mathrm{d} t$，被积函数是奇函数：$t\to-t$ 时变号，零点两侧的贡献相互抵消，所以它为零。图 [1](#abb-1) 给出了两种占空比下的系数：脉冲越窄，系数衰减越慢。

:::abbildung et3/k3koeff 1
方波（0/1）在两种脉冲宽度下的傅里叶系数。虚线：包络 $\frac{T_1}{T}\operatorname{si}(\pi kT_1/T)$。$T_1=T/2$ 时缺少偶次谐波，$T_1=T/4$ 时缺少 4 的倍数次谐波。
:::
::::

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
