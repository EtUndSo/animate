---
title: 第 5 阶段：卷积的计算
pfad: 电气工程 / 第 3 学期 / ET3 – 电气工程基础 3：信号与系统 / LTI 系统与卷积
adresse: elektrotechnik/3-semester/signale-und-systeme/lti-systeme-und-faltung
knoten: 第 1 章：LTI 系统与卷积
order: 3210600
summary: 对于具体的信号，需要把积分 (4.2) 算出来。关键在于把两个因子都画成积分变量 tau 的函数。
tags: 
lang: zh
---

<span class="anker" id="stufe-5"></span>

:::zweck
对于具体的信号，需要把积分 [(4.2)](das-faltungsintegral.html#gl-4-2) 算出来。关键在于把两个因子都画成积分变量 $\tau$ 的函数。
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

::::beispiel RC 电路与矩形脉冲
时间常数为 $T=RC$ 的 RC 电路，其冲激响应是一个面积为 1 的衰减指数脉冲。短促的冲激瞬间把电容充到 $1/T$，随后电容经 $R$ 放电：

<span class="anker" id="gl-5-1"></span>
$$h(t)=\frac1T\,\varepsilon(t)\,\mathrm{e}^{-t/T}. \tag{5.1}$$

输入：从 $0$ 到 $T_0$、高度为 $a$ 的矩形。图 [6](#abb-6) 给出了两个时刻下两个因子的相对位置。共分三个区间：

<span class="anker" id="gl-5-2"></span>
$$g(t)=\begin{cases}0 & t<0,\\[2pt] a\bigl(1-\mathrm{e}^{-t/T}\bigr) & 0\le t\le T_0,\\[2pt] a\bigl(\mathrm{e}^{T_0/T}-1\bigr)\mathrm{e}^{-t/T} & t>T_0.\end{cases} \tag{5.2}$$
::::

:::herleitung 对矩形脉冲的响应
⁠**$t<0$：**平移后的 $h(t-\tau)$ 仅在 $\tau\le t<0$ 时非零，而 $s(\tau)$ 仅在 $\tau\ge0$ 时非零。两者没有重叠，$g=0$。

⁠**$0\le t\le T_0$：**重叠区间为 $0<\tau<t$：

$$g(t)=\int_0^ta\,\frac1T\,\mathrm{e}^{-(t-\tau)/T}\,\mathrm{d}\tau=\frac aT\,\mathrm{e}^{-t/T}\int_0^t\mathrm{e}^{\tau/T}\mathrm{d}\tau=\frac aT\,\mathrm{e}^{-t/T}\cdot T\bigl(\mathrm{e}^{t/T}-1\bigr)=a\bigl(1-\mathrm{e}^{-t/T}\bigr).$$

⁠**$t>T_0$：**只在 $0<\tau<T_0$ 内重叠：

$$g(t)=\frac aT\,\mathrm{e}^{-t/T}\int_0^{T_0}\mathrm{e}^{\tau/T}\mathrm{d}\tau=a\bigl(\mathrm{e}^{T_0/T}-1\bigr)\mathrm{e}^{-t/T}.$$
:::

在参考模型中（$a=1$，$T_0=T=1$ s）：$g(0.5)=0.3935$，$g(1)=0.6321$，$g(2)=0.2325$，$g(3)=0.0855$。这与图 [4](was-ein-lti-system-ist.html#abb-4) 中的 $g_0$ 是同一条曲线。

:::abbildung et3/k1schieben 6
图解卷积，$a=1$，$T_0=T=1$ s。蓝色：$s(\tau)$。红色：$h(t-\tau)$，已反转并平移 $t$。橙色面积就是 $g(t)$：$t=0.5$ s 时为 0.3935（部分重叠），$t=2$ s 时为 0.2325（整个矩形都位于 $h$ 已衰减的部分）。右：完整的响应及这两个点。
:::

:::frage 为什么反转的是 $h$，而不是 $s$？
也可以反转 $s$ 而不是 $h$：代换 $\tau'=t-\tau$ 把 $\int s(\tau)\,h(t-\tau)\,\mathrm{d}\tau$ 变成 $\int s(t-\tau')\,h(\tau')\,\mathrm{d}\tau'$。反转哪个函数能让平移过程更容易看清，就反转哪个，通常是形状较简单的那个。
:::

:::ltspice 对矩形脉冲的响应
⁠**绘制：**第 [2](ein-erstes-system-das-rc-glied.html#stufe-2) 阶段中的 RC 电路，信号源取 `PULSE(0 1 0 1u 1u 1)`：高度 1 V，持续时间 1 s。

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
