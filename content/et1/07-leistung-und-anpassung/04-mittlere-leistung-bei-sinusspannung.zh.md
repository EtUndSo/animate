---
title: 第 3 阶段：正弦电压下的平均功率
pfad: 电气工程 / 第 1 学期 / 电气工程基础 / 功率、匹配与效率
order: 1170400
summary: 在交流电压下，功率不断变化。本阶段找出决定发热的那一个数。
tags: 振幅, 周期, 角频率, 有效值
lang: zh
---

<span class="anker" id="stufe-3"></span>

:::zweck
在交流电压下，功率不断变化。本阶段找出决定发热的那一个数。
:::

**基本思路。** 在电阻上，$i$ 与 $u$ 成正比。两者同时变号，所以它们的乘积永远不为负。电荷反向运动时，电压也反向，电荷仍然释放能量。正负两个半波都发热（图 [4](#abb-4)）。功率在零和峰值之间脉动，速度是电压的两倍。其平均值位于一半高度处。

:::abbildung et1/k7sinus 4
左图为加热电阻上的电压和电流。右图为瞬时功率 $p(t)$。它在 0 和 20 W 之间围绕平均值 $P=10$ W 振荡，达到最大值的次数是 $u$ 的两倍。
:::

:::satz 定理 3.1 (电阻上的平均功率)
<span class="anker" id="satz-3-1"></span>

对于加在 $R$ 上的 $u(t)=\hat u\cos(\omega t)$，流过的电流为 $i(t)=\hat\imath\cos(\omega t)$，其中 $\hat\imath=\hat u/R$。功率的时间平均值为

<span class="anker" id="gl-3-1"></span>
$$P=\frac1T\int_0^T u(t)\,i(t)\,\mathrm{d} t=\frac12\,\frac{\hat u^2}{R}=\frac12\,\hat\imath^2R. \tag{3.1}$$
:::

⁠**如何理解：**$\hat u$ 和 $\hat\imath$ 是__振幅__，即峰值。$T$ 是__周期__，$\omega=2\pi/T$ 是__角频率__。在电网中，$T=20$ ms，$\omega=314$ 1/s。**适用条件：**平均值要在整数个周期上计算。公式只在 $i$ 与 $u$ 成正比时成立，即只适用于电阻。

:::herleitung 因子 $\frac12$ 从何而来
代入得 $p=u\,i=u^2/R=(\hat u^2/R)\cos^2(\omega t)$。利用 $\cos^2x=\frac12(1+\cos2x)$ 得

$$P=\frac{1}{T\,R}\int_0^T\hat u^2\cos^2(\omega t)\,\mathrm{d} t=\frac{1}{T\,R}\int_0^T\hat u^2\,\frac12\bigl(1+\cos(2\omega t)\bigr)\,\mathrm{d} t=\frac12\,\frac{\hat u^2}{R}.$$

余弦部分在 $T$ 内经历两次完整振荡，其积分为零。由 $\hat u=R\,\hat\imath$ 得第二种形式。
:::

**例。** 对于 $\hat u=10$ V 和 $R=5\,\Omega$，有 $\hat\imath=2$ A，功率峰值为 20 W，$P=10$ W。在 50 Hz 时，每周期有 0.2 J 进入晶格。**极限情况：**当 $\omega\to0$ 时，$u$ 变成直流电压，$p$ 停留在 $\hat u^2/R$。因子 $\frac12$ 消失，因为此时已无法在整数个周期上取平均。

:::zusatz 有效值
直流电压 $U$ 在 $R$ 上产生相同热量的条件是 $U^2/R=\frac12\hat u^2/R$，即 $U=\hat u/\sqrt2$。这个值称为__有效值__。这里为 7.07 V。插座的 230 V 是有效值，振幅为 325 V。
:::

:::ltspice 测量平均功率
⁠**绘制：**`voltage` 从 `a` 接到接地点，设为 `SINE(0 10 50)`，`res` `R1` 取 5，从 `a` 接到接地点。

⁠**指令：**`.tran 0 40m 0 10u` 和 `.meas tran Pm AVG V(a)*I(R1) FROM=0 TO=40m`

⁠**你会看到：**绘出 `V(a)*I(R1)`：曲线保持在 0 和 20 W 之间，以 100 Hz 振荡。日志给出 `Pm` = 10 W。对于练习 [3](#aufg-3)，填入振幅 325 和你求出的电阻，读出 2 kW 和 4 kW。
:::

:::frage 在交流电中，电子只是来回摆动。这怎么能传递能量？
因为能量并不随电子一起传播。即使在 1 A/mm$^2$ 和 50 Hz 下，电子每半个周期也只移动约 0.5 µ m。电阻中的电场使电子在两个方向上加速，每次碰撞都把能量交给晶格。这不需要电子前进，只需要电压和电流。
:::

:::aufgabe 练习 3 ★★ 暖风机
<span class="anker" id="aufg-3"></span>

一台暖风机接在 $\hat u=325$ V、50 Hz 的正弦电压上，平均吸收 2 kW。(a) $R$、$\hat\imath$ 和功率峰值各是多少？(b) 每秒有多少次 $p=0$？(c) 一个元件阻断每隔一个的半波。在 $R$ 不变时，预测平均功率。

:::loesung
(a) 由式 [(3.1)](#gl-3-1)：$R=\hat u^2/(2P)=26.4\,\Omega$，$\hat\imath=\hat u/R=12.3$ A，峰值 $\hat u\,\hat\imath=2P=4$ kW。 (b) 每周期两次，即每秒 100 次。 (c) 每隔一个半波缺失一个，也就是缺失一半能量：1 kW。
:::
:::
