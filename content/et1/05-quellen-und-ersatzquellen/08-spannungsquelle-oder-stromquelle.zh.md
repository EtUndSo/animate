---
title: 第 6 阶段：电压源还是电流源
pfad: 电气工程 / 第 1 学期 / 电气工程基础 / 电源与等效电源
order: 1150800
summary: 同一个实际电源有两种电路图。本阶段说明两者描述的是同一条直线，以及如何相互换算。
tags: 等效
lang: zh
---

<span class="anker" id="stufe-6"></span>

:::zweck
同一个实际电源有两种电路图。本阶段说明两者描述的是同一条直线，以及如何相互换算。
:::

**基本思路。** 一条直线可以从电压轴读取（高度 $U_\mathrm{q}$，斜率 $R_\mathrm{q}$），也可以从电流轴读取（截距 $I_\mathrm{q}$，斜率 $G_\mathrm{q}$）。如果两个网络的特性曲线相同，就称它们__等效__。这时从外部在接线端上进行任何测量，都无法判断接的是哪一个。

:::satz 定理 6.1 (实际电源的等效)
<span class="anker" id="satz-6-1"></span>

实际电压源与实际电流源等效的条件是

<span class="anker" id="gl-6-1"></span>
$$U_\mathrm{q}=\frac{I_\mathrm{q}}{G_\mathrm{q}}\qquad\text{且}\qquad R_\mathrm{q}=\frac{1}{G_\mathrm{q}}. \tag{6.1}$$
:::

:::herleitung 令两条直线相等
把式 [(5.1)](reale-quellen-und-der-arbeitspunkt.html#gl-5-1) 中的电流源方程解出电压，$U_\mathrm{AB}=(I_\mathrm{q}-I_\mathrm{A})/G_\mathrm{q}$，并令其等于电压源方程：

$$\frac{I_\mathrm{q}}{G_\mathrm{q}}-\frac{I_\mathrm{A}}{G_\mathrm{q}}=U_\mathrm{q}-R_\mathrm{q}I_\mathrm{A}.$$

这必须对任意电流都成立。因此不含 $I_\mathrm{A}$ 的项和含 $I_\mathrm{A}$ 的项必须分别相等。这就是式 [(6.1)](#gl-6-1)。
:::

⁠**如何理解：**电流 $I_\mathrm{q}=U_\mathrm{q}/R_\mathrm{q}$ 就是短路电流，电阻保持不变。在电流源形式中，开路时全部源电流流过 $G_\mathrm{q}$，并在那里产生开路电压。负载取用电流时，留给 $G_\mathrm{q}$ 的电流减少，电压下降。这是同一个压降，只是以分流而不是分压的方式出现。**适用条件：**这种等效只在接线端上成立，并且只对 $0<R_\mathrm{q}<\infty$ 成立。

:::abbildung et1/k5umwandlung 7
同一节电池，同一个工作点。左：0.5 A 流过全部元件。右：4.5 A 的源电流分为流过电导的 4 A 和流向负载的 0.5 A。在接线端上，电压和电流都一致。
:::

::::beispiel
9 V、2 $\Omega$ 的电池变为 $I_\mathrm{q}=4.5$ A 和 $G_\mathrm{q}=0.5$ S。在 8 V 的工作点上，电导取走 $0.5\,\mathrm{S}\cdot8\,\mathrm{V}=4$ A，留给负载 0.5 A（图 [7](#abb-7)）。
::::

⁠**极限情况：**当 $R_\mathrm{q}\to0$ 时，$I_\mathrm{q}\to\infty$。理想电压源没有电流源形式，理想电流源也没有电压源形式。

**选哪种形式？** 就计算而言，两者同样好。选用更能显示行为的形式：电压源是低阻的（理想情况为零），电流源是高阻的（理想情况为无穷大）。如果 $R_\mathrm{q}$ 比负载小得多，电压几乎不变，就选电压源形式。如果 $R_\mathrm{q}$ 比负载大得多，电流几乎不变，就选电流源形式。

:::frage 既然两者相同，电池开路时会白白发热 40.5 W 吗？
不会。在图 [7](#abb-7) 右侧，开路时 4.5 A 流过 2 $\Omega$，按 $P=UI$（[第 7 部分](/wissen/zh/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/leistung-anpassung-und-wirkungsgrad/leistung-und-anpassung.html)）将是 40.5 W。真实的电池并不发热，这里符合实际的是功率为 0 W 的电压源图景。等效电路在接线端上正确，在内部则不然。内部发生什么取决于结构，而不取决于特性曲线。在工作点上也是如此：内部是 0.5 W 对 32 W，外部两种情况都是 4 W。
:::

:::aufgabe 练习 7 ★ 转换
<span class="anker" id="aufg-7"></span>

(a) 把 5 V、100 $\Omega$ 转换为电流源。(b) 把 20 mA 并联 1 k$\Omega$ 转换为电压源。(c) 在 (a) 的两种形式上都接 400 $\Omega$，比较电压和电流。

:::loesung
(a) $I_\mathrm{q}=5\,\mathrm{V}/100\,\Omega=50$ mA，$G_\mathrm{q}=10$ mS。 (b) $U_\mathrm{q}=20\,\mathrm{mA}\cdot1\,\mathrm{k\Omega}=20$ V，$R_\mathrm{q}=1$ k$\Omega$。

(c) 电压源：分压，$U=5\,\mathrm{V}\cdot\frac{400}{500}=4$ V，$I=10$ mA。电流源：$50\,\mathrm{mA}\cdot(100\,\Omega\parallel400\,\Omega)=50\,\mathrm{mA}\cdot80\,\Omega=4$ V，$I=4\,\mathrm{V}/400\,\Omega=10$ mA。结果相同。
:::
:::
