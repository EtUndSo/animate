---
title: 第 9 阶段：用切线代替曲线
pfad: 电气工程 / 第 1 学期 / 电气工程基础 / 双极型晶体管
order: 1201100
summary: 放大器围绕放大区中的一个固定点工作。在那里，小变化看到的不是指数函数，而是一条直线。本阶段读出它的斜率，并把它们画成等效电路。
tags: 小信号, 偏导数, 输入电阻, 输出电阻, 厄利电压, 扩展等效电路, 小信号等效电路
lang: zh
---

<span class="anker" id="stufe-9"></span>

:::zweck
放大器围绕放大区中的一个固定点工作。在那里，小变化看到的不是指数函数，而是一条直线。本阶段读出它的斜率，并把它们画成等效电路。
:::

**基本思路。** 第 [4](drei-bereiche-drei-ersatzschaltbilder.html#stufe-4) 阶段的线性模型有两个缺陷。它把 BE 通路当作固定电压，所以输入电阻为零。它又把输出特性曲线当作水平线，所以电导为零。实际上这两个斜率都是有限的。对于工作点附近的小变化，只需采用在二极管（[第 9 部分](/wissen/zh/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/halbleiter-und-dioden/halbleiter-und-dioden.html)）中用过的切线：第 [3](eine-flache-viele-kennlinien.html#stufe-3) 阶段的地形在那里变成一个平的斜面，每个方向有一个斜率。

这种分解写成：总量等于直流分量加变化量，$u_\mathrm{BE}(t)=U_\mathrm{BE}+u_\mathrm{be}(t)$，$i_\mathrm{C}(t)=I_\mathrm{C}+i_\mathrm{c}(t)$。带小写下标的小写字母称为__小信号__。符号 $\partial$ 表示__偏导数__：固定其他变量，对一个变量求导，也就是一个截面的斜率。

:::definition 定义 9.1 (工作点处的小信号量)
<span class="anker" id="satz-9-1"></span>

<span class="anker" id="gl-9-1"></span>
$$S=\frac{\partial I_\mathrm{C}}{\partial U_\mathrm{BE}}=\frac{I_\mathrm{C}}{U_T},\qquad r_\mathrm{BE}=\frac{\partial U_\mathrm{BE}}{\partial I_\mathrm{B}}=\frac{U_T}{I_\mathrm{B}}=\frac{B}{S},\qquad G_\mathrm{CE}=\frac1{r_\mathrm{CE}}=\frac{\partial I_\mathrm{C}}{\partial U_\mathrm{CE}}=\frac{I_\mathrm{C}}{U_\mathrm{Early}+U_\mathrm{CE}}. \tag{9.1}$$

于是对变化量有

<span class="anker" id="gl-9-2"></span>
$$i_\mathrm{b}=\frac{u_\mathrm{be}}{r_\mathrm{BE}},\qquad i_\mathrm{c}=S\,u_\mathrm{be}+\frac{u_\mathrm{ce}}{r_\mathrm{CE}}. \tag{9.2}$$
:::

⁠**如何理解：**跨导 $S$ 以 A/V 为单位，是控制特性曲线的斜率；$r_\mathrm{BE}$ 是__输入电阻__，即输入特性曲线的斜率的倒数。$r_\mathrm{CE}$ 是__输出电阻__。输出特性曲线的直线向左延长，相交于 $-U_\mathrm{Early}$。__厄利电压__ $U_\mathrm{Early}$ 的典型值在 50 V 到 200 V 之间，T 的值为 74 V。机理：$U_\mathrm{CB}$ 增大使空间电荷区向基区内扩展。基区变窄，密度梯度变陡，电流变大。**适用条件：**放大区，且 $|u_\mathrm{be}|\ll U_T$。

:::herleitung 斜率
由 $I_\mathrm{C}=I_\mathrm{S}\mathrm{e}^{U_\mathrm{BE}/U_T}$ 得 $\frac{\partial I_\mathrm{C}}{\partial U_\mathrm{BE}}=\frac{1}{U_T}I_\mathrm{S}\mathrm{e}^{U_\mathrm{BE}/U_T}=\frac{I_\mathrm{C}}{U_T}$。指数函数的导数等于函数本身除以指数中的标度。同样，$\partial I_\mathrm{B}/\partial U_\mathrm{BE}=I_\mathrm{B}/U_T$。它的倒数就是 $r_\mathrm{BE}$。由 $I_\mathrm{B}=I_\mathrm{C}/B$ 得 $r_\mathrm{BE}=B/S$。式 [(3.1)](eine-flache-viele-kennlinien.html#gl-3-1) 中的第三个因子给出 $\partial I_\mathrm{C}/\partial U_\mathrm{CE}=I_\mathrm{C}/(74\,\mathrm{V}+U_\mathrm{CE})$。在点 A，分母为 80 V。式 [(9.2)](#gl-9-2) 中的和就是切平面，它综合了两个方向。
:::

:::abbildung et1/k10tangente 10
左：控制特性曲线及其在点 A（2 mA）处的切线，斜率 $S=76.9$ mS。右：两个 $U_\mathrm{BE}$ 值对应的输出特性曲线。曲线之间的距离是 $S$ 的作用。每条曲线的斜率是 $1/r_\mathrm{CE}$，向左延长后到达 $-74$ V。
:::

**例。** 在点 A，$S=2\,\mathrm{mA}/26\,\mathrm{mV}=76.9$ mS，即 $1/S=13\,\Omega$，还有 $r_\mathrm{BE}=200/S=2.6$ k$\Omega$ 和 $r_\mathrm{CE}=80\,\mathrm{V}/2\,\mathrm{mA}=40$ k$\Omega$。$S$ 的机理：$U_\mathrm{BE}$ 增加 1 mV 使势垒降低，按切线计算注入增加 3.85 %，即 77 µ A。要通过输出侧达到同样的效果，需要 $U_\mathrm{CE}$ 增加 3 V。**简而言之：**跨导等于电流除以 $U_T$，与 $B$ 和 $I_\mathrm{S}$ 无关。**极限情况：**$I_\mathrm{C}\to0$ 给出 $S\to0$：没有静态电流就没有控制作用。$U_\mathrm{Early}\to\infty$ 给出 $r_\mathrm{CE}\to\infty$，即理想电流源。

**多小才算小？** 精确地说，$i_\mathrm{c}=I_\mathrm{C}(\mathrm{e}^{u_\mathrm{be}/U_T}-1)$，切线给出的是 $I_\mathrm{C}u_\mathrm{be}/U_T$。当 $u_\mathrm{be}=+1$ mV 时误差为 2 %，当 $+5$ mV 时误差为 10 %（$+424$ µ A 而不是 $+385$ µ A），而当 $-5$ mV 时只有 $-350$ µ A。正半波大于负半波，信号发生失真。在 26 mV 时切线已不可用。

**从模型到等效电路。** 切线变成元件（图 [11](#abb-11)）。__扩展等效电路__包含直流分量。输入端是电源 $U_0$ 与 $r_\mathrm{BE}$ 串联。其中 $U_0=U_\mathrm{BE}-U_T=0.574$ V 是输入特性曲线的切线与坐标轴的交点。输出端是受控电流源 $I$ 与 $r_\mathrm{CE}$ 并联。它在点 A 输出 $I=1.85$ mA，其余 0.15 mA 流过 $r_\mathrm{CE}$。去掉直流分量，就得到__小信号等效电路__。这时恒定电源消失：恒定电压变成导线，$U_\mathrm{CC}$ 也是如此（叠加，[第 5 部分](/wissen/zh/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/quellen-und-ersatzquellen/quellen-und-ersatzquellen.html)）。转换规则是：如果一个电流取决于它自身这对接线端上的电压，它就是电阻。如果它取决于别处的电压，它就是受控源，这里是电压控制电流源（VCCS，[第 6 部分](/wissen/zh/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/zweitore/zweitore.html)）。用二端口网络来表示，这就是 Y 参数 $Y_{11}=1/r_\mathrm{BE}$，$Y_{12}=0$，$Y_{21}=S$，$Y_{22}=G_\mathrm{CE}$。

:::abbildung et1/k10kleinsignal 11
左：导通状态下用于直流量的扩展等效电路。右：小信号等效电路：常量消失了，只剩下斜率。电源 $S\,u_\mathrm{be}$ 是沿 $U_\mathrm{BE}$ 方向的切线，$r_\mathrm{CE}$ 是沿 $U_\mathrm{CE}$ 方向的切线。
:::

:::frage 跨导不就是输出特性曲线族中的斜率吗？
不是。那里 $U_\mathrm{CE}$ 是水平轴，所以斜率是 $1/r_\mathrm{CE}$。跨导属于 $U_\mathrm{BE}$ 方向，在输出曲线族中表现为两条曲线之间的垂直距离除以它们的 $U_\mathrm{BE}$ 之差。
:::

:::frage 为什么 $1/S=13\,\Omega$，而 $r_\mathrm{BE}=2.6$ k$\Omega$？两者测的不是同一个电压吗？
两者都是用电压变化量除以电流，但除的是不同的电流。$1/S$ 除以 $I_\mathrm{C}$ 的变化量，$r_\mathrm{BE}$ 除以小 $B$ 倍的 $I_\mathrm{B}$ 的变化量。因此输入电阻大 $B$ 倍。这里的比值是 200。
:::

:::aufgabe 练习 11 ★★ 小信号量
<span class="anker" id="aufg-11"></span>

T 工作在 $I_\mathrm{C}=0.5$ mA，$U_\mathrm{CE}=6$ V。(a) 求 $S$、$1/S$、$r_\mathrm{BE}$ 和 $r_\mathrm{CE}$。(b) 对 $u_\mathrm{be}=\pm5$ mV，比较精确的电流变化量和切线给出的值。(c) 预测：如果电流增大到两倍，(a) 中的四个值如何变化？

:::loesung
(a) $S=19.2$ mS，$1/S=52\,\Omega$，$r_\mathrm{BE}=200/S=10.4$ k$\Omega$，$r_\mathrm{CE}=80\,\mathrm{V}/0.5\,\mathrm{mA}=160$ k$\Omega$。

(b) 切线：$\pm96$ µ A。精确值：$+106$ µ A 和 $-87$ µ A。

(c) $S$ 加倍，$1/S$、$r_\mathrm{BE}$ 和 $r_\mathrm{CE}$ 减半。这四个量都与电流成正比或成反比。
:::
:::
