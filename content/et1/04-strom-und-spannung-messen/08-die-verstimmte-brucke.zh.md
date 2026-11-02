---
title: 第 7 阶段：不平衡电桥
pfad: 电气工程 / 第 1 学期 / 电气工程基础 / 电流与电压的测量
order: 1140800
summary: 如果电阻只有微小变化或连续变化，就不再重新调节。这时偏离零点的量就是测量信号。本阶段说明为什么这样能看到极小的变化。
tags: 应变片
lang: zh
---

<span class="anker" id="stufe-7"></span>

:::zweck
如果电阻只有微小变化或连续变化，就不再重新调节。这时偏离零点的量就是测量信号。本阶段说明为什么这样能看到极小的变化。
:::

**基本思路。** 单独一台仪表必须显示全部电压，而变化只是其中极小的一部分。电桥减去了很大的公共电压。只剩下变化，它可以用一个小量程来测。因为读数误差与满量程值挂钩，所以它随量程一起减小。

:::satz 定理 7.1 (电桥电压)
<span class="anker" id="satz-7-1"></span>

两个中点之间的电压为 $U_\mathrm d=U_4-U_2$，其中 $U_2$ 是 $R_2$ 上的电压，$U_4$ 是 $R_4$ 上的电压：

<span class="anker" id="gl-7-1"></span>
$$U_\mathrm d=U_\mathrm q\left(\frac{R_4}{R_3+R_4}-\frac{R_2}{R_1+R_2}\right)=U_\mathrm q\,\frac{R_1R_4-R_2R_3}{(R_1+R_2)(R_3+R_4)}. \tag{7.1}$$

当 $R_1=R_2=R_3=R$ 且 $R_4=R+\Delta R$ 时，

<span class="anker" id="gl-7-2"></span>
$$U_\mathrm d=\frac{U_\mathrm q}{4}\cdot\frac{\Delta R/R}{1+\Delta R/(2R)}\approx\frac{U_\mathrm q}{4}\cdot\frac{\Delta R}{R}\qquad\text{当 }\Delta R\ll R\text{ 时}. \tag{7.2}$$
:::

⁠**如何理解：**式 [(7.1)](#gl-7-1) 的分子在平衡时为零。$\Delta R/R$ 是相对变化量，无单位。**适用条件：**电压表不取用明显的电流。**极限情况：**$\Delta R=0$ 得 $U_\mathrm d=0$。$\Delta R\to\infty$ 得 $U_\mathrm d\to U_\mathrm q/2$：此时右侧中点位于正极。

:::herleitung 微小变化
由 $U_2=U_\mathrm q/2$ 和 $U_4=U_\mathrm q(R+\Delta R)/(2R+\Delta R)$ 得

$$U_\mathrm d=U_\mathrm q\,\frac{2(R+\Delta R)-(2R+\Delta R)}{2(2R+\Delta R)}=\frac{U_\mathrm q\,\Delta R}{4R+2\Delta R}=\frac{U_\mathrm q}{4}\cdot\frac{\Delta R/R}{1+\Delta R/(2R)}.$$
:::

:::abbildung et1/k4dms 9
左：带可变 $R_4$ 的电桥。右：同一变化在两种刻度上的情况：红线为读数，浅色带为读数误差。在 10 V 刻度上，9 mV 的变化淹没在误差中。在 100 mV 刻度上，偏差本身就是信号。
:::

**例：应变片。** __应变片__是粘贴在构件上的一条薄金属带。构件伸长时，金属带变长变细，其电阻 $R=\rho\,l/A$ 增大。电阻的相对变化约为应变的两倍。在 2 ‰ 的应变下，$R_4$ 增大 0.4 %，从 350 $\Omega$ 变为 351.4 $\Omega$。此时 $U_2=4.500$ V，$U_4=9\,\mathrm{V}\cdot351.4/701.4=4.509$ V，所以 $U_\mathrm d=8.98$ mV。近似式给出 9.00 mV，偏差 0.2 %。10 M$\Omega$ 电压表中流过 0.9 nA，相对于支路中的 12.9 mA，比例为 $7\cdot10^{-8}$：可以忽略。

**为什么这样更准确。** 直接测量时，仪表必须区分 4.509 V 和 4.500 V，也就是在 10 V 量程上可靠地显示小数点后三位。但它 $\pm100$ mV 的读数误差是待测变化的十一倍。在电桥上，100 mV 量程的 $\pm1$ mV 就够了，只有前者的百分之一（图 [9](#abb-9)）。此外还有两个优点。电源波动 1 % 时，$U_4$ 变化 45 mV，是信号的五倍，而 $U_\mathrm d$ 只变化 0.09 mV。如果四个电阻都按同一倍数变化，例如因为受热，$U_\mathrm d$ 保持不变。

:::frage 不能测量 $U_4$，再在心里减去 4.5 V 吗？
算是可以算，但 $\pm100$ mV 的读数误差仍留在结果中。电桥在仪表测量之前就做了减法。所以仪表可以用小量程。
:::

⁠**从这里开始：**除非另有说明，在后面的所有部分中，测量仪表都视为理想的：电流表 $R_\mathrm i\to0$，电压表 $R_\mathrm i\to\infty$。

:::aufgabe 练习 8 ★★★ 两片应变片
<span class="anker" id="aufg-8"></span>

右侧支路中现在有两片应变片：$R_3=R-\Delta R$ 受压缩短，$R_4=R+\Delta R$ 受拉伸长，$R_1=R_2=R$。(a) 求 $U_\mathrm d$ 的一般表达式及例题中的数值。(b) 为什么结果关于 $\Delta R$ 严格线性？(c) 如果四个电阻都因受热变化 1 %，会发生什么变化？

:::loesung
(a) $R_3+R_4=2R$，所以 $U_4=U_\mathrm q(R+\Delta R)/(2R)$。由 $U_2=U_\mathrm q/2$ 得 $U_\mathrm d=\frac12U_\mathrm q\,\Delta R/R=4.5\,\mathrm{V}\cdot0.004=18.0$ mV，是一片应变片时的两倍。

(b) 和 $R_3+R_4$ 保持为 $2R$。因此右侧支路的电流保持 12.9 mA，$U_4$ 恰好随 $R_4$ 增长。只有一片应变片时，和也随之增大，这就产生了式 [(7.2)](#gl-7-2) 中的分母。

(c) 没有变化：在式 [(7.1)](#gl-7-1) 中，所有电阻的公共因子被约去。
:::
:::
