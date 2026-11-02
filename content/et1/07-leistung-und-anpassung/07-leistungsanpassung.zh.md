---
title: 第 6 阶段：功率匹配
pfad: 电气工程 / 第 1 学期 / 电气工程基础 / 功率、匹配与效率
order: 1170700
summary: 表中显示 P L 有一个最大值。本阶段求出它，并解释为什么它恰好位于 R L=R i 。
tags: 短路功率
lang: zh
---

<span class="anker" id="stufe-6"></span>

:::zweck
表中显示 $P_\mathrm{L}$ 有一个最大值。本阶段求出它，并解释为什么它恰好位于 $R_\mathrm{L}=R_\mathrm{i}$。
:::

**基本思路。** 两种影响相互对抗。$R_\mathrm{L}$ 小时，到来的库仑多，但它们的能量几乎全部留在 $R_\mathrm{i}$ 中。$R_\mathrm{L}$ 大时，每库仑几乎把全部能量都释放在负载中，但到来的库仑少。[第 5 部分](/wissen/zh/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/quellen-und-ersatzquellen/quellen-und-ersatzquellen.html)的直线 $U_\mathrm{L}=U_\mathrm{q}-R_\mathrm{i}I$ 使这一点一目了然：$P_\mathrm{L}=U_\mathrm{L}I$ 是直线下方矩形的面积（图 [7](#abb-7)）。当矩形的角位于直线中点，即电流和电压都为一半时，面积最大。这时 $R_\mathrm{i}$ 和 $R_\mathrm{L}$ 在相同电流下有相同的压降，所以两个电阻相等。

:::abbildung et1/k7rechteck 7
电池的电源直线及三个工作点。蓝色：$P_\mathrm{L}$，由 $I$ 和 $U_\mathrm{L}$ 构成的矩形。红色：$P_\mathrm{v}$，由 $I$ 和 $U_\mathrm{Ri}$ 构成的矩形。两者合起来是 $P_\mathrm{q}=U_\mathrm{q}I$。中间的角给出最大的蓝色矩形。
:::

:::satz 定理 6.1 (功率匹配)
<span class="anker" id="satz-6-1"></span>

由 $I=U_\mathrm{q}/(R_\mathrm{i}+R_\mathrm{L})$，负载上的功率为

<span class="anker" id="gl-6-1"></span>
$$P_\mathrm{L}(R_\mathrm{L})=\left(\frac{U_\mathrm{q}}{R_\mathrm{i}+R_\mathrm{L}}\right)^{\!2}R_\mathrm{L}=U_\mathrm{q}^2\,\frac{R_\mathrm{L}}{\bigl(R_\mathrm{i}(1+R_\mathrm{L}/R_\mathrm{i})\bigr)^2}=P_\mathrm{SC}\,\frac{\alpha}{(1+\alpha)^2}, \tag{6.1}$$

其中 $\alpha=R_\mathrm{L}/R_\mathrm{i}$，$P_\mathrm{SC}=U_\mathrm{q}^2/R_\mathrm{i}$。它在下列条件下最大：

<span class="anker" id="gl-6-2"></span>
$$R_\mathrm{L}=R_\mathrm{i},\qquad P_\mathrm{L,max}=\frac{U_\mathrm{q}^2}{4\,R_\mathrm{i}}=\frac{P_\mathrm{SC}}{4},\qquad I=\frac{I_\mathrm{SC}}{2},\qquad U_\mathrm{L}=\frac{U_\mathrm{q}}{2}. \tag{6.2}$$
:::

⁠**如何理解：**$P_\mathrm{SC}=U_\mathrm{q}I_\mathrm{SC}$ 是__短路功率__，即 $R_\mathrm{L}=0$ 时电源的功率。它全部落在 $R_\mathrm{i}$ 中，任何负载得到的都不超过它的四分之一。**适用条件：**电源是固定的，只选择 $R_\mathrm{L}$。对于等效电源，用 $U_\mathrm{OC}$ 代替 $U_\mathrm{q}$。

:::herleitung 最大值的三种求法
由商的求导法则 $\bigl(f/g\bigr)'=(f'g-f\,g')/g^2$，取 $f=\alpha$，$g=(1+\alpha)^2$，得

$$\frac{\mathrm{d} P_\mathrm{L}}{\mathrm{d}\alpha}=P_\mathrm{SC}\,\frac{(1+\alpha)^2-2\alpha(1+\alpha)}{(1+\alpha)^4}=P_\mathrm{SC}\,\frac{1-\alpha}{(1+\alpha)^3}.$$

导数在 $\alpha=1$ 处为零，之前为正，之后为负。这就是最大值。

不用导数：令 $x=I/I_\mathrm{SC}$，则 $P_\mathrm{L}=P_\mathrm{SC}\,x(1-x)$。这条抛物线的零点是 0 和 1，所以其最大值 $\frac14$ 位于 $x=\frac12$。

从机理上看：电流增量 $\mathrm{d} I$ 从电源带来 $U_\mathrm{q}\mathrm{d} I$，损耗增加 $2R_\mathrm{i}I\,\mathrm{d} I$。在 $I=I_\mathrm{SC}/2$ 时，损耗吃掉了增量：9 V 对 $2\cdot2\,\Omega\cdot2.25\,\mathrm{A}=9$ V。
:::

**例。** 对于 $R_\mathrm{L}=2\,\Omega$，有 $I=2.25$ A，$U_\mathrm{L}=4.5$ V，$P_\mathrm{L}=10.125$ W，这是 $P_\mathrm{SC}=40.5$ W 的四分之一。负载 0.5 $\Omega$ 和 8 $\Omega$ 都得到 6.48 W。一般来说，$\alpha$ 和 $1/\alpha$ 给出相同的功率，因为它们互换了 $x$ 和 $1-x$。**极限情况：**当 $\alpha\to0$ 时，电流固定，$P_\mathrm{L}\approx P_\mathrm{SC}\,\alpha$。当 $\alpha\to\infty$ 时，电压固定，$P_\mathrm{L}\approx P_\mathrm{SC}/\alpha$。

:::ltspice 抛物线与直线
⁠**绘制：**`voltage` 取 9，从 `q` 接到接地点，`res` 取 2，从 `q` 接到 `a`。负载用名为 `I1` 的电流源 `current`，从 `a` 接到接地点。

⁠**指令：**`.dc I1 0 4.5 0.01` 和 `.meas dc Pmax MAX V(a)*I(I1)`

⁠**你会看到：**绘出 `V(a)*I(I1)`：一条抛物线，最大值 10.125 W 出现在 2.25 A 处。`V(a)/9` 是效率，是一条下降的直线，在该处达到 0.5。在 3.6 A 和 0.9 A 处都是 6.48 W。对于练习 [6](#aufg-6)，填入 12 和 4，扫描到 3 A：1.5 A 处为 9 W，1 A 和 2 A 处都是 8 W。
:::

:::frage 我的负载是固定的。我应该选择使 $R_\mathrm{i}=R_\mathrm{L}$ 的电源吗？
不应该。该定理适用于固定的电源和可选的负载。如果负载固定而 $R_\mathrm{i}$ 可选，则 $R_\mathrm{i}=0$ 最好，因为 $U_\mathrm{q}^2R_\mathrm{L}/(R_\mathrm{i}+R_\mathrm{L})^2$ 随 $R_\mathrm{i}$ 减小。16 $\Omega$ 的负载在 $R_\mathrm{i}=2\,\Omega$ 时得到 4 W，在 $R_\mathrm{i}=0$ 时得到 5.06 W。
:::

:::aufgabe 练习 6 ★★ 接在放大器上的扬声器
<span class="anker" id="aufg-6"></span>

一个放大器的输出相当于 $U_\mathrm{q}=12$ V，$R_\mathrm{i}=4\,\Omega$。(a) 哪种扬声器得到的功率最大？这个功率是多少？(b) 8 $\Omega$ 的扬声器得到什么结果？比较功率和效率。(c) 哪一个负载与 8 $\Omega$ 得到相同的功率？(d) ★★★ 用式 [(6.1)](#gl-6-1) 证明 $\alpha$ 和 $1/\alpha$ 总是给出相同的功率。

:::loesung
(a) $R_\mathrm{L}=4\,\Omega$，$P_\mathrm{L,max}=144\,\mathrm{V^2}/16\,\Omega=9$ W，此时 $\eta=50$ %。 (b) $I=1$ A，$P_\mathrm{L}=8$ W，$\eta=\frac23$。功率只减少 11 %，而损耗从 9 W 降到 4 W。 (c) $\alpha=2$ 对应 $\alpha=\frac12$，即 $R_\mathrm{L}=2\,\Omega$：8 W，但只有 $\eta=\frac13$。

(d) $\dfrac{1/\alpha}{(1+1/\alpha)^2}=\dfrac{1/\alpha}{(\alpha+1)^2/\alpha^2}=\dfrac{\alpha}{(1+\alpha)^2}$。
:::
:::
