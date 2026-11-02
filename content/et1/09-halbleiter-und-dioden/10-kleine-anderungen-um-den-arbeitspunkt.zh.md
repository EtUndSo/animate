---
title: 第 8 阶段：工作点附近的微小变化
pfad: 电气工程 / 第 1 学期 / 电气工程基础 / 半导体与二极管
order: 1191000
summary: 小信号常常叠加在直流电压上，而只有变化量才重要。本阶段说明：对于微小变化，二极管相当于一个阻值由直流电流设定的电阻。
tags: 微分电阻, 小信号
lang: zh
---

<span class="anker" id="stufe-8"></span>

:::zweck
小信号常常叠加在直流电压上，而只有变化量才重要。本阶段说明：对于微小变化，二极管相当于一个阻值由直流电流设定的电阻。
:::

**基本思路。** 在工作点附近，每条光滑曲线都与其切线重合（图 [10](#abb-10)）。机理是：电压增加 1 mV，势垒就降低 1 meV。势垒以上的比例因此增大 $1/25.85=3.9$ %，而且总是当前电流的同一百分比。因此电流大意味着绝对变化大，也就是电阻小。

:::abbildung et1/k9kleinsignal 10
左：工作点(0.692 V | 4.31 mA) 附近的特性曲线局部。切线斜率为 $1/r=0.167$ S，与横轴交于 $U_\mathrm D-U_T=0.667$ V。右：对小信号而言，直流电压源不存在，二极管就是电阻 $r$。
:::

:::satz 定理 8.1 (微分电阻)
<span class="anker" id="satz-8-1"></span>

在直流电流为 $I$ 的工作点处，对于微小变化 $u_\mathrm D$ 和 $i$，有

<span class="anker" id="gl-8-1"></span>
$$r=\frac{\mathrm{d} U_\mathrm D}{\mathrm{d} I}=\frac{U_T}{I+I_\mathrm S}\approx\frac{U_T}{I},\qquad u_\mathrm D=r\,i. \tag{8.1}$$
:::

⁠**如何理解：**$r$ 称为__微分电阻__，在 1 mA 时为 25.85 $\Omega$。小写字母表示相对于工作点的偏差，即__小信号__。**适用条件：**$|u_\mathrm D|\ll U_T$。1 mV 时误差为 2 %，5 mV 时为 10 %，25.85 mV 时已达 72 %。

:::herleitung 特性曲线的斜率
对式 [(4.1)](warum-der-strom-exponentiell-wachst.html#gl-4-1) 求导：$\mathrm{d} I/\mathrm{d} U_\mathrm D=(I_\mathrm S/U_T)\,\mathrm{e}^{U_\mathrm D/U_T}=(I+I_\mathrm S)/U_T$。其倒数就是 $r$。指数函数求导后还原自身，所以结果中只出现 $I$，而在正向 $I_\mathrm S$ 被略去。$I_\mathrm S$ 不同的两个二极管在相同电流下具有相同的 $r$。
:::

**例。** 在参考模型中，$r=25.85\,\mathrm{mV}/4.31\,\mathrm{mA}=6.0\,\Omega$。电源上叠加一个峰值为 100 mV 的正弦信号。对于变化量，$R$ 和 $r$ 构成分压器：

$$\hat u_\mathrm D=100\,\mathrm{mV}\cdot\frac{6.0\,\Omega}{1000\,\mathrm{\Omega}+6.0\,\Omega}=0.60\,\mathrm{mV},\qquad\hat\imath=\frac{100\,\mathrm{mV}}{1006\,\mathrm{\Omega}}=99.4\,\mu\text{A}.$$

$U_0=5.1$ V 的精确计算给出 $+0.59$ mV 和 $+99.4$ µ A。信号几乎全部出现在电阻上，二极管上只留下 0.6 %。**极限情况：**$I\to0$ 时 $r=U_T/I_\mathrm S=2.6\,\mathrm{T\Omega}$，二极管起隔断作用。$I$ 很大时 $r$ 趋于零，实际上还剩下体电阻。

:::ltspice 工作点与信号
⁠**绘制：**电源 `voltage` 从 `in` 接地，取值 `5`，在 `Advanced` 中把 AC Amplitude 设为 `1`。`res` 1k 从 `in` 接到 `d`，`diode` DM 从 `d` 接地，模型同上。

⁠**指令：**先用 `.op`，再用 `.ac dec 1 1k 10k`

⁠**你会看到：**用 `.op` 时显示 $V(d)=0.693$ V，$I(D1)=4.31$ mA。用 `.ac` 时 $V(d)$ 处显示 $-44.5$ dB，即比值 0.00597。这就是例题中的 $r/(R+r)$。做练习 [10](#aufg-10) 时，改变数值并读出你的 $r$。
:::

:::frage 二极管的电阻为什么不是 $U_\mathrm D/I$？
那是从原点到工作点的连线斜率的倒数：$0.692\,\mathrm{V}/4.31\,\mathrm{mA}=161\,\Omega$。它描述的是在工作点处通过相同电流的电阻，但不是特性曲线在该点的性质。电流对变化的响应有多强，只有切线才能说明，而切线陡 27 倍。对于欧姆电阻，两者重合。
:::

:::aufgabe 练习 10 ★★ 斜率与切线
<span class="anker" id="aufg-10"></span>

<ol class="al">

<li>

计算 2 mA 和 20 mA 时的 $r$。

</li>

<li>

在 2 mA 时电压升高 10 mV。切线预测的电流是多少，特性曲线给出的电流是多少？为什么切线在下方？

</li>

<li>

三个相同的二极管串联，经一个电阻由 12 V 供电，通过 2 mA。计算三个二极管上的电压和电阻值。电源升高 1 V 时，二极管上的电压变化多少？

</li>

</ol>

:::loesung
(a) 12.9 $\Omega$ 和 1.29 $\Omega$。 (b) 切线：$2\,\mathrm{mA}+10\,\mathrm{mV}/12.9\,\Omega=2.77$ mA。特性曲线：$2\,\mathrm{mA}\cdot\mathrm{e}^{0.387}=2.94$ mA。指数曲线向上弯曲，总是位于其切线上方。 (c) 电压 $3\cdot0.673\,\mathrm{V}=2.02$ V，$R=(12\,\mathrm{V}-2.02\,\mathrm{V})/2\,\mathrm{mA}=5.0\,\mathrm{k\Omega}$。三个二极管合计 $r=38.8\,\Omega$。1 V 变为 $1\,\mathrm{V}\cdot38.8/5039=7.7$ mV。
:::
:::
