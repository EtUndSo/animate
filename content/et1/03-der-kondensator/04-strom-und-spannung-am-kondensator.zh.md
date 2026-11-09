---
title: 第 3 阶段：电容器上的电流与电压
pfad: 电气工程 / 第 1 学期 / 电气工程基础 / 电容器
order: 1130400
summary: 在电阻上，电压在同一时刻决定电流。电容器则不同：这里电流取决于电压变化的快慢。本阶段建立这一定律。
tags: 电流源
lang: zh
---

<span class="anker" id="stufe-3"></span>

:::zweck
在电阻上，电压在同一时刻决定电流。电容器则不同：这里电流取决于电压变化的快慢。本阶段建立这一定律。
:::

**基本思路。** 电压表明到目前为止流入了多少电荷。电流改变这些电荷。电流大，电压上升就快。没有电流，电压就保持不变，即使它很高。所以电流不是由电压的数值决定，而是由电压的变化决定。

:::satz 定理 3.1 (电容器上的电流与电压)
<span class="anker" id="satz-3-1"></span>

电流和电压的参考箭头方向相同时（[第 2 部分](/wissen/zh/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/strom-widerstand-und-kirchhoff/strom-widerstand-und-kirchhoff.html)），对随时间变化的量有

<span class="anker" id="gl-3-1"></span>
<span class="anker" id="gl-3-2"></span>
$$\begin{aligned} i(t)&=\frac{\mathrm{d} q}{\mathrm{d} t}=C\,\frac{\mathrm{d} u(t)}{\mathrm{d} t},\\ u(t)&=\frac{q(t)}{C}=u(t_0)+\frac1C\int_{t_0}^{t}i(t')\,\mathrm{d} t'. \end{aligned} \tag{3.1|3.2}$$
:::

:::herleitung 电流与电压
电流是单位时间的电荷，$i=\mathrm{d} q/\mathrm{d} t$（[第 2 部分](/wissen/zh/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/strom-widerstand-und-kirchhoff/strom-widerstand-und-kirchhoff.html)）。代入 $q=C\,u$，并把常数 $C$ 提到导数之外，就得到式 [(3.1)](#gl-3-1)。反过来，电荷是电流曲线下的面积，正如路程是速度曲线下的面积（[第 1 部分](/wissen/zh/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/ladung-feld-und-potenzial/ladung-feld-und-potenzial.html)）：$q(t)=q(t_0)+\int_{t_0}^{t}i\,\mathrm{d} t'$。除以 $C$ 就得到式 [(3.2)](#gl-3-2)。
:::

⁠**如何理解：**小写字母表示随时间变化的量，$t'$ 是积分变量，$u(t_0)$ 是起始时刻的电压。$i$ 的单位为 A，$C$ 的单位为 F，$\mathrm{d} u/\mathrm{d} t$ 的单位为 V/s。1 mA 流入 100 µF 时，电压以 10 V/s 上升。**符号：**$q$ 是电流箭头所指向的那块极板上的电荷。$i>0$ 时它增加，$u$ 上升；$i<0$ 时 $u$ 下降。**适用条件：**$C$ 必须恒定。

**两个推论。** 第一：**电压不跳变。**在时间 $\Delta t$ 内跳变 $\Delta U$ 需要 $i=C\,\Delta U/\Delta t$。当 $\Delta t\to0$ 时电流将无限增大，因为电荷 $C\,\Delta U$ 必须在零时间内到达。在 100 µF 上 1 µs 内升高 9 V，就已需要 900 A。电流则可以跳变，因为它不与储存的量相关联。第二：**电压恒定时没有电流。**由 $\mathrm{d} u/\mathrm{d} t=0$ 得 $i=0$，电容器隔断直流。

::::beispiel
__电流源__是一种无论电压如何都保持电流不变的元件。它通过开关 S 向串联的电阻和未充电的电容器供电（图 [3](#abb-3)）。它提供 $I=0.9$ mA，$R$ 和 $C$ 取 RC 电路的值。在 $t=0$ 闭合 S 时，$u_R$ 跳变到固定值 $R\,I=9$ V。对电容器，由式 [(3.2)](#gl-3-2) 和 $u_C(0)=0$ 得

<span class="anker" id="gl-3-3"></span>
$$u_C(t)=\frac{Q(t)}{C}=\frac{I\,t}{C}=9\,\mathrm{V/s}\cdot t. \tag{3.3}$$

电压沿直线增长。尽管电流跳变，电压仍从零开始连续变化。理想电流源会不停地充电，直到电介质被击穿。在 1 s 时，两个电压相等。

:::abbildung et1/k3rampe 3
电流源通过 $R=10\,\mathrm{k\Omega}$ 给电容器充电。闭合 S 时，$u_R$ 跳变到 9 V 并保持不变。$u_C$ 从零开始以 9 V/s 上升，因为每秒到达的电荷相同。
:::
::::

⁠**极限情况：**当 $C\to\infty$ 时斜率变为零，电压纹丝不动。因此很大的电容器能把电压固定住。

:::frage 空的电容器上电压为 0 V。那么电流不是必须为零吗？
这只对电阻成立。对电容器，$u=0$ 不能说明 $i$ 的大小，因为 $i$ 取决于 $u$ 的斜率，而不是它的数值。在图 [3](#abb-3) 中，$t=0$ 时电压为零，电流却是 0.9 mA。
:::

:::aufgabe 练习 3 ★★ 从电流到电压，再回来
<span class="anker" id="aufg-3"></span>

一个 100 µF 的电容器在 $t=0$ 时是空的。电流从 0 到 2 s 为 $+0.5$ mA，从 2 s 到 3 s 为零，从 3 s 到 4 s 为 $-1$ mA。

<ol class="al">

<li>

画出 $u(t)$，并给出 2 s、3 s 和 4 s 时的值。

</li>

<li>

3 s 时它带多少电荷？

</li>

<li>

另一个 10 µF 的电容器上，电压在 5 ms 内从 2 V 均匀升到 7 V。电流是多少？

</li>

<li>

为什么 $i(t)$ 可以有竖直的边，而 $u(t)$ 不可以？

</li>

</ol>

:::loesung
(a) 电流恒定时，$u$ 是斜率为 $i/C$ 的直线。0 到 2 s：$0.5\,\mathrm{mA}/100\,\mu\text{F}=5$ V/s，因此 $u(2\,\mathrm{s})=10$ V。2 s 到 3 s：$i=0$，电压保持 10 V。3 s 到 4 s：$-10$ V/s，因此 $u(4\,\mathrm{s})=0$。曲线是一个梯形。

(b) $Q=C\,u=100\,\mu\text{F}\cdot10\,\mathrm{V}=1$ mC。这也是到 3 s 为止 $i(t)$ 曲线下的面积：$0.5\,\mathrm{mA}\cdot2\,\mathrm{s}$。

(c) $i=C\,\Delta u/\Delta t=10\,\mu\text{F}\cdot5\,\mathrm{V}/5\,\mathrm{ms}=10$ mA。

(d) $u$ 由 $i$ 曲线下的面积得出。即使 $i$ 有棱角，面积也总是连续增长。而 $u$ 若有棱角，就需要无限大的电流。
:::
:::
