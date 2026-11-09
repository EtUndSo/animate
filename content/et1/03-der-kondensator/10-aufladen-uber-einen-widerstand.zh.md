---
title: 第 9 阶段：通过电阻充电
pfad: 电气工程 / 第 1 学期 / 电气工程基础 / 电容器
order: 1131000
summary: 接在电压源上时，充电电流取决于电容器电压，而电容器电压又取决于充电电流。本阶段建立描述这一反馈的方程，并从头求解。
tags: 短路, 开路, 微分方程
lang: zh
---

<span class="anker" id="stufe-9"></span>

:::zweck
接在电压源上时，充电电流取决于电容器电压，而电容器电压又取决于充电电流。本阶段建立描述这一反馈的方程，并从头求解。
:::

**基本思路。** 在 RC 电路（图 [9](#abb-9)）中，开关 S 在 $t=0$ 时从位置 2 转到位置 1，电容器是空的。电压不能跳变（第 [3](strom-und-spannung-am-kondensator.html#stufe-3) 阶段），所以 $u_C(0)=0$。全部电池电压都加在 $R$ 上，流过 $i(0)=U_0/R=0.9$ mA。在这一瞬间，电容器相当于一根导线，所以称为__短路__：有电流，电压为零。原因是：还没有电荷被分离，也就没有阻碍电流的电场。

电流带来电荷，$u_C$ 上升。根据基尔霍夫电压定律，留给 $R$ 的电压减小，电流下降，$u_C$ 上升变慢。这一反馈决定了整条曲线的形状。最后 $u_C=U_0$。$R$ 上不再有电压，$i=0$：电容器相当于__开路__，接线端如同断开。原因是：被分离电荷的电场把极板抬高到电池极的电位，$R$ 上不再有电位降。

:::abbildung et1/k3rckreis 9
左：带参考箭头的 RC 电路，基尔霍夫电压定律 $U_0=u_R+u_C$。位置 1 充电，位置 2 放电。右：两个等效电路：$t=0$ 时空的电容器相当于导线，很长时间后充满的电容器相当于断开的接线端。
:::

**方程。** 基尔霍夫电压定律（[第 2 部分](/wissen/zh/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/strom-widerstand-und-kirchhoff/strom-widerstand-und-kirchhoff.html)）为 $U_0=u_R+u_C$。由欧姆定律 $u_R=R\,i$ 和式 [(3.1)](strom-und-spannung-am-kondensator.html#gl-3-1) 中的 $i=C\,\mathrm{d} u_C/\mathrm{d} t$ 得

<span class="anker" id="gl-9-1"></span>
$$U_0=R\,C\,\frac{\mathrm{d} u_C}{\mathrm{d} t}+u_C. \tag{9.1}$$

这是一个__微分方程__：所求的量与其导数同时出现在方程中。要求的不是一个数，而是整个函数 $u_C(t)$。用 $\tau=RC$ 整理后得

<span class="anker" id="gl-9-2"></span>
$$\frac{\mathrm{d} u_C}{\mathrm{d} t}=\frac{U_0-u_C}{\tau}. \tag{9.2}$$

用文字表述：曲线的斜率等于到最终值的距离除以 $\tau$。因此每个点 $(t,u_C)$ 都对应确定的斜率（图 [10](#abb-10)）。从初始值出发，处处沿着这个斜率走，画出的就是解。所以每个初始值恰好对应一条曲线。

:::abbildung et1/k3richtung 10
式 [(9.2)](#gl-9-2) 的图示：每条灰色短线表示该处的斜率，$U_0=9$ V，$\tau=1$ s。远低于 9 V 时斜率大，9 V 时为零，更高时为负。曲线沿短线从初始值 0 V、3 V 和 12 V 出发，全都趋近同一个最终值。
:::

:::satz 定理 9.1 (充电)
<span class="anker" id="satz-9-1"></span>

当 $u_C(0)=0$ 且 $t\ge0$ 时，有

<span class="anker" id="gl-9-3"></span>
$$u_C(t)=U_0\bigl(1-\mathrm{e}^{-t/\tau}\bigr),\qquad i(t)=\frac{U_0}{R}\,\mathrm{e}^{-t/\tau},\qquad u_R(t)=U_0\,\mathrm{e}^{-t/\tau},\qquad\tau=R\,C. \tag{9.3}$$
:::

⁠**如何理解：**$\mathrm{e}=2.718$ 是欧拉数。$\tau$ 是时间常数，单位为 s：$\mathrm{\Omega\cdot F}=\frac{\mathrm V}{\mathrm A}\cdot\frac{\mathrm{A\,s}}{\mathrm V}=\mathrm s$。因子 $\mathrm{e}^{-t/\tau}$ 从 1 开始，每经过时间 $\tau$ 就降到原来的 $1/\mathrm{e}$，即 36.8 %。**适用条件：**理想元件，恒定电源，$t=0$ 是开关动作的时刻。

:::herleitung 从头求解方程
⁠**第 1 步：只有到终点的距离才重要。**令 $x(t)=U_0-u_C(t)$。因为 $U_0$ 是常数，所以 $\mathrm{d} x/\mathrm{d} t=-\mathrm{d} u_C/\mathrm{d} t$，式 [(9.2)](#gl-9-2) 变为

$$\frac{\mathrm{d} x}{\mathrm{d} t}=-\frac{x}{\tau},\qquad x(0)=U_0.$$

$x$ 的变化与 $x$ 本身成正比：剩余量越大，缩小得越快。

⁠**第 2 步：除以 $x$。**对 $x>0$ 有 $\frac1x\,\frac{\mathrm{d} x}{\mathrm{d} t}=-\frac1\tau$。根据链式法则，左边是 $\ln x(t)$ 的导数，因为 $\frac{\mathrm{d}}{\mathrm{d} t}\ln x(t)=\frac1x\,\frac{\mathrm{d} x}{\mathrm{d} t}$。

⁠**第 3 步：积分。**于是 $\ln x(t)$ 有恒定的斜率 $-1/\tau$，是一条直线：$\ln x(t)=-t/\tau+K$，$K$ 为常数。

⁠**第 4 步：消去对数。**两边取指数函数，得 $x(t)=\mathrm{e}^{K}\,\mathrm{e}^{-t/\tau}$。当 $t=0$ 时为 $x(0)=\mathrm{e}^{K}$，所以 $\mathrm{e}^{K}=U_0$。于是 $x(t)=U_0\,\mathrm{e}^{-t/\tau}$。

⁠**第 5 步：换回原变量。**$u_C=U_0-x=U_0(1-\mathrm{e}^{-t/\tau})$。求导：$i=C\,\mathrm{d} u_C/\mathrm{d} t=\frac{C\,U_0}{\tau}\mathrm{e}^{-t/\tau}=\frac{U_0}{R}\mathrm{e}^{-t/\tau}$，而 $u_R=R\,i$。

⁠**验算：**代入式 [(9.1)](#gl-9-1) 得 $R\,C\cdot\frac{U_0}{\tau}\mathrm{e}^{-t/\tau}+U_0-U_0\mathrm{e}^{-t/\tau}=U_0$。结果正确。

⁠**同样的方法用于电流：**由 $U_0=R\,i+\frac1C\int_0^ti\,\mathrm{d} t'$ 求导得 $0=R\,\frac{\mathrm{d} i}{\mathrm{d} t}+\frac iC$。简写为 $\frac{\mathrm{d} i}{i}=-\frac{\mathrm{d} t}{RC}$，第 2 到 4 步给出 $\ln i=-\frac{t}{RC}+\ln\frac{U_0}{R}$，于是又得到 $i=\frac{U_0}{R}\mathrm{e}^{-t/RC}$。
:::

::::beispiel
在参考模型中，$t=1$ s 时 $u_C=9\,\mathrm{V}\cdot(1-\mathrm{e}^{-1})=5.69$ V，$u_R=3.31$ V，$i=0.331$ mA（图 [11](#abb-11)）。两个电压之和在任何时刻都是 9 V。起点处的切线以 $U_0/\tau=9$ V/s 上升，恰好在 $t=\tau$ 时达到 9 V：如果初始电流像第 [3](strom-und-spannung-am-kondensator.html#stufe-3) 阶段那样保持不变，电容器经过 $\tau$ 就充满了。
::::

⁠**简而言之：**$\tau$ 是最终电荷除以初始电流，$C\,U_0/(U_0/R)=RC$。

:::abbildung et1/k3laden 11
充电，$U_0=9$ V，$R=10\,\mathrm{k\Omega}$，$C=100\,\mu\text{F}$。左边是电压，右边是电流。电流在 $t=0$ 时从零跳变到 0.9 mA，然后衰减。起点处的切线在 $t=\tau=1$ s 时到达最终值。圆点对应 $t=\tau$。
:::

⁠**极限情况：**当 $t\to0$ 时 $\mathrm{e}^{-t/\tau}\to1$：$u_C=0$，$i=U_0/R$，这就是短路。当 $t\to\infty$ 时 $\mathrm{e}^{-t/\tau}\to0$：$u_C=U_0$，$i=0$，这就是开路。当 $R\to0$ 时 $\tau\to0$，$i(0)\to\infty$。若实际导线电阻为 0.1 $\Omega$，则为 90 A，持续 10 µs。

:::frage 电容器真的会完全充满吗？
从数学上说永远不会，因为 $\mathrm{e}^{-t/\tau}$ 达不到零。实际上经过几个 $\tau$ 就够了：$5\tau$ 后只差 0.7 %，在参考模型中是 61 mV。这时充电电流还有 6 µA，与第 [5](bauformen-und-selbstentladung.html#stufe-5) 阶段的漏电流处于同一数量级。
:::

:::aufgabe 练习 10 ★★ 另一个 RC 电路
<span class="anker" id="aufg-10"></span>

12 V 电源通过 4.7 k$\Omega$ 给一个空的 220 µF 电容器充电。

<ol class="al">

<li>

求 $\tau$ 和 $i(0)$。

</li>

<li>

1 s 后 $u_C$ 是多少？

</li>

<li>

$u_C$ 何时达到 12 V 的一半？何时达到 99 %？

</li>

<li>

预测：$R$ 加倍时，$\tau$ 和 $i(0)$ 如何变化？最终电压如何变化？

</li>

</ol>

:::loesung
(a) $\tau=4.7\,\mathrm{k\Omega}\cdot220\,\mu\text{F}=1.034$ s，$i(0)=12\,\mathrm{V}/4.7\,\mathrm{k\Omega}=2.55$ mA。

(b) $u_C=12\,\mathrm{V}\cdot(1-\mathrm{e}^{-1/1.034})=7.44$ V。

(c) 由 $\mathrm{e}^{-t/\tau}=\frac12$ 得 $t=\tau\ln2=0.717$ s。对于 99 %，$\mathrm{e}^{-t/\tau}=0.01$，因此 $t=\tau\ln100=4.76$ s。

(d) $\tau$ 加倍，$i(0)$ 减半，最终电压仍为 12 V，因为最后 $R$ 中不再有电流。
:::
:::

:::aufgabe 练习 11 ★★★ 充电的能量平衡
<span class="anker" id="aufg-11"></span>

RC 电路中的电容器从 0 充电到 $U_0$。

<ol class="al">

<li>

用 $W_\mathrm{B}=\int_0^\infty U_0\,i\,\mathrm{d} t$ 证明电池放出 $C\,U_0^2$。

</li>

<li>

用 $W_R=\int_0^\infty R\,i^2\,\mathrm{d} t$ 证明电阻中有 $\frac12CU_0^2$ 变为热。给出参考模型中的数值。

</li>

<li>

全部损耗都产生在 $R$ 中，为什么结果中却没有 $R$？

</li>

</ol>

:::loesung
(a) $W_\mathrm{B}=U_0\int_0^\infty i\,\mathrm{d} t=U_0\,Q=C\,U_0^2$，因为电流的积分就是电荷。计算过程：$\int_0^\infty\frac{U_0}{R}\mathrm{e}^{-t/\tau}\mathrm{d} t=\frac{U_0}{R}\tau=C\,U_0$。

(b) $W_R=\int_0^\infty R\,\frac{U_0^2}{R^2}\mathrm{e}^{-2t/\tau}\mathrm{d} t=\frac{U_0^2}{R}\cdot\frac\tau2=\frac12CU_0^2$。参考模型：电池提供 8.10 mJ，其中电容器和电阻各得 4.05 mJ。

(c) 较小的 $R$ 使电流增大，但使时间缩短。因此在 $W_R=\frac{U_0^2}{R}\cdot\frac{\tau}{2}=\frac{U_0^2}{R}\cdot\frac{RC}{2}$ 中，$R$ 恰好约去。只要电容器从零开始，用固定电压充电的效率总是 50 %。损耗式 [(8.3)](ladungserhaltung-beim-umschalten.html#gl-8-3) 背后也是同样的计算。
:::
:::
