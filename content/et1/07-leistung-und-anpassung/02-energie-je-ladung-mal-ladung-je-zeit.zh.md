---
title: 第 1 阶段：单位电荷的能量乘以单位时间的电荷
pfad: 电气工程 / 第 1 学期 / 电气工程基础 / 功率、匹配与效率
order: 1170200
summary: 电压说明一份电荷释放多少能量，电流说明有多少电荷经过。本阶段把两者结合成单位时间的能量。
tags: 
lang: zh
---

<span class="anker" id="stufe-1"></span>

:::zweck
电压说明一份电荷释放多少能量，电流说明有多少电荷经过。本阶段把两者结合成单位时间的能量。
:::

**基本思路。** 元件的两个接线端之间有电压 $U$。由[第 1 部分](/wissen/zh/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/ladung-feld-und-potenzial/ladung-feld-und-potenzial.html)可知，每库仑电荷从较高电位到达较低电位时释放能量 $U$（以焦耳计）。电流 $I$ 计数每秒通过多少库仑。因此每秒转换 $U\cdot I$ 焦耳（图 [1](#abb-1)）。两个因子缺一不可：有电压而无电流时什么也不转换，因为没有电荷运动；有电流而无电压时什么也不转换，因为没有电荷释放能量。

:::abbildung et1/k7ladung 1
负载上为 8 V 和 0.5 A。下方是电位变化：每库仑损失 8 J。图中画的是沿电流方向运动的正电荷。电子的运动方向相反，结果相同。
:::

:::definition 定义 1.1 (能量与功率)
<span class="anker" id="satz-1-1"></span>

电荷 $\mathrm{d} Q$ 经过电压 $u$ 时释放能量 $\mathrm{d} W=u\,\mathrm{d} Q$。由电流 $i=\mathrm{d} Q/\mathrm{d} t$ 得

<span class="anker" id="gl-1-1"></span>
$$p(t)=\frac{\mathrm{d} W}{\mathrm{d} t}=u(t)\,i(t),\qquad W=\int u\,\mathrm{d} Q=\int_{t_1}^{t_2}u(t)\,i(t)\,\mathrm{d} t. \tag{1.1}$$

对于直流量，即 $U$ 和 $I$ 不随时间变化时，有

<span class="anker" id="gl-1-2"></span>
$$W=U\,I\,\Delta t,\qquad P=\frac{W}{\Delta t}=U\,I. \tag{1.2}$$
:::

⁠**如何理解：**$u$ 的单位为 V，$i$ 的单位为 A，$p$ 的单位为瓦特：$[P]=\mathrm{V\,A}=\mathrm{J/s}=\mathrm W$。一个指示 LED 转换 20 mW，一个电水壶转换 2 kW，一台发电机组转换 1 GW。表达式 $W/\Delta t$ 一般是时间 $\Delta t$ 内功率的平均值，$p(t)$ 是其瞬时值。设备常常持续运行，因此用功率而不是能量来标明。对于能量，有 $1\,\mathrm{W\,s}=1\,\mathrm{V\,A\,s}=1\,\mathrm{J}=1\,\mathrm{N\,m}$。电气工程中多用瓦秒或千瓦时计算，$1\,\mathrm{kWh}=3.6\,\mathrm{MJ}$。焦耳常用于燃烧过程，牛顿米用于机械功。

⁠**符号：**采用负载惯例（[第 2 部分](/wissen/zh/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/strom-widerstand-und-kirchhoff/strom-widerstand-und-kirchhoff.html)）时，$p>0$ 表示元件吸收能量，$p<0$ 表示元件释放能量。采用发电机惯例时正好相反。**适用条件：**只要 $u$ 和 $i$ 在同一对接线端上计量，$p=u\,i$ 对任何一端口网络都成立。对元件内部不作任何假设。

:::herleitung 为什么只有电压和电流起作用
在时间 $\mathrm{d} t$ 内，电荷 $\mathrm{d} Q=i\,\mathrm{d} t$ 从接线端 1 进入，同样的电荷从接线端 2 流出（节点定律，[第 2 部分](/wissen/zh/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/strom-widerstand-und-kirchhoff/strom-widerstand-und-kirchhoff.html)）。内部保持不变。就能量平衡而言，相当于 $\mathrm{d} Q$ 直接从 $\varphi_1$ 到达 $\varphi_2$。由[第 1 部分](/wissen/zh/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/ladung-feld-und-potenzial/ladung-feld-und-potenzial.html)可知，释放的能量为 $\mathrm{d} W=(\varphi_1-\varphi_2)\,\mathrm{d} Q=u\,i\,\mathrm{d} t$。除以 $\mathrm{d} t$ 即得式 [(1.1)](#gl-1-1)。电子运动方向相反，且带负电。两个符号合在一起，得到同样的乘积。
:::

::::beispiel
$R_\mathrm{L}=16\,\Omega$ 上的电压为 8 V，电流为 0.5 A（[第 5 部分](/wissen/zh/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/quellen-und-ersatzquellen/quellen-und-ersatzquellen.html)）。每库仑释放 8 J，每秒到来 0.5 C：$P=4$ W。一小时内为 $W=4\,\mathrm{W}\cdot3600\,\mathrm{s}=14.4\,\mathrm{kJ}=4\,\mathrm{Wh}$。逐个计数时，每秒通过 $I/e=3.12\cdot10^{18}$ 个电子，每个释放 $e\cdot8\,\mathrm{V}=1.28\cdot10^{-18}$ J。乘积仍是 4 W。
::::

⁠**极限情况：**接线端开路时为 9 V 和 0 A，所以 $P=0$。理想导线的 $U=0$，所以在任何电流下 $P=0$。

:::frage 元件中电流被消耗了吗？
没有。元件前后流过的电流相同，电荷全部又流了出来。被消耗的是能量：电荷以较低的电位继续前进。因此“耗电量”的账单上写的是千瓦时。
:::

:::aufgabe 练习 1 ★ 能量与符号
<span class="anker" id="aufg-1"></span>

(a) 一块 3.7 V 的充电电池储存 2 Ah 的电荷（2 A 持续一小时）。这相当于多少 Wh 和多少 kJ？它能为 0.74 W 的设备供电多久？(b) 一个 2 kW 的电水壶工作 3 分钟。这是多少 kWh？按 30 ct/kWh 计算要花多少钱？(c) 在一个一端口网络上，按负载惯例测得 $U=12$ V，$I=-3$ A。它是吸收功率还是输出功率？

:::loesung
(a) $Q=2\,\mathrm{A}\cdot3600\,\mathrm{s}=7200$ C，所以 $W=3.7\,\mathrm{V}\cdot7200\,\mathrm{C}=26.64$ kJ $=7.4$ Wh。在 0.74 W 下可用 10 h。 (b) $W=2\,\mathrm{kW}\cdot0.05\,\mathrm{h}=0.1$ kWh，费用为 3 ct。 (c) $P=12\,\mathrm{V}\cdot(-3\,\mathrm{A})=-36$ W。该一端口网络输出 36 W。
:::
:::
