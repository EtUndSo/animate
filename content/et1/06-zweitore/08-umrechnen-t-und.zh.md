---
title: 第 6 阶段：换算、T 与 $\pi$
pfad: 电气工程 / 第 1 学期 / 电气工程基础 / 二端口网络
order: 1160800
summary: Z 形式和 Y 形式描述同一个二端口网络。本阶段说明如何从一种形式变到另一种形式，以及某种形式何时根本不存在。
tags: 
lang: zh
---

<span class="anker" id="stufe-6"></span>

:::zweck
Z 形式和 Y 形式描述同一个二端口网络。本阶段说明如何从一种形式变到另一种形式，以及某种形式何时根本不存在。
:::

**基本思路。** Y 形式和 Z 形式是同样的两个方程，一个对电压求解，另一个对电流求解。因此转换就是解方程组，而这正是“从头开始”一节中的逆矩阵所做的事。

:::satz 定理 6.1 (Z 与 Y 的换算)
<span class="anker" id="satz-6-1"></span>

电导矩阵和电阻矩阵互为逆矩阵，$\mathbf Y\cdot\mathbf Z=\mathbf 1$：

<span class="anker" id="gl-6-1"></span>
$$\mathbf Y=\mathbf Z^{-1}=\frac{1}{\det\mathbf Z}\begin{pmatrix}Z_{22}&-Z_{12}\\-Z_{21}&Z_{11}\end{pmatrix},\qquad \mathbf Z=\mathbf Y^{-1}=\frac{1}{\det\mathbf Y}\begin{pmatrix}Y_{22}&-Y_{12}\\-Y_{21}&Y_{11}\end{pmatrix} \tag{6.1}$$

其中 $\det\mathbf Z=Z_{11}Z_{22}-Z_{12}Z_{21}$，$\det\mathbf Y=Y_{11}Y_{22}-Y_{12}Y_{21}$。
:::

⁠**如何理解：**求逆的是整个矩阵，而不是逐个数取倒数。每个元素都带有整个分母，所以每个 Y 参数都取决于所有 Z 参数。**适用条件：**行列式不得为零。

:::herleitung 求逆的两种途径
⁠**用矩阵。**由 $\mathbf I=\mathbf Y\mathbf U$ 和 $\mathbf U=\mathbf Z\mathbf I$ 得，对每个 $\mathbf I$ 都有 $\mathbf I=\mathbf Y\mathbf Z\,\mathbf I$，所以 $\mathbf Y\mathbf Z=\mathbf 1$。

⁠**在 Z 等效电路上用短路试验。**$U_2=0$ 时，$Z_{21}I_1=-Z_{22}I_2$，所以 $I_2=-\frac{Z_{21}}{Z_{22}}I_1$，$U_1=\bigl(Z_{11}-Z_{12}\frac{Z_{21}}{Z_{22}}\bigr)I_1$。于是

$$Y_{11}=\frac{I_1}{U_1}=\frac{Z_{22}}{Z_{11}Z_{22}-Z_{12}Z_{21}},\qquad Y_{21}=\frac{I_2}{U_1}=-\frac{Z_{21}}{Z_{11}Z_{22}-Z_{12}Z_{21}}.$$

$U_1=0$ 时，$-Z_{11}I_1=Z_{12}I_2$，所以 $I_1=-\frac{Z_{12}}{Z_{11}}I_2$，$U_2=\bigl(Z_{22}-Z_{21}\frac{Z_{12}}{Z_{11}}\bigr)I_2$。由此得

$$Y_{12}=-\frac{Z_{12}}{Z_{11}Z_{22}-Z_{12}Z_{21}},\qquad Y_{22}=\frac{Z_{11}}{Z_{11}Z_{22}-Z_{12}Z_{21}}.$$
:::

**T 与 $\pi$。** 第 [3](impedanzform-und-leerlaufversuch.html#stufe-3) 阶段 T 形网络的 Z 矩阵可用式 [(6.1)](#gl-6-1) 求逆，$\pi$ 形网络的 Y 矩阵可直接从短路试验读出。设 $D=R_\mathrm{a}R_\mathrm{b}+R_\mathrm{a}R_\mathrm{c}+R_\mathrm{b}R_\mathrm{c}=\det\mathbf Z$，并联电导为 $G_1$、$G_3$，串联电导为 $G_2$，则

<span class="anker" id="gl-6-2"></span>
$$\mathbf Y_\mathrm{T}=\frac1D\begin{pmatrix}R_\mathrm{b}+R_\mathrm{c}&-R_\mathrm{b}\\-R_\mathrm{b}&R_\mathrm{a}+R_\mathrm{b}\end{pmatrix},\qquad \mathbf Y_\pi=\begin{pmatrix}G_1+G_2&-G_2\\-G_2&G_2+G_3\end{pmatrix}. \tag{6.2}$$

令两者相等，得 $G_2=-Y_{12}$，$G_1=Y_{11}+Y_{12}$，$G_3=Y_{22}+Y_{21}$。$G_3=0$ 时，$\mathbf Y_\pi$ 变为 $I_1=(G_1+G_2)U_1-G_2U_2$，$I_2=-G_2U_1+G_2U_2$ 这一对方程。这就是[第 5 部分](/wissen/zh/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/quellen-und-ersatzquellen/quellen-und-ersatzquellen.html)的星形-三角形变换：T 是星形，$\pi$ 是三角形。用 Z 参数描述自然引出 T 形网络，用 Y 参数描述则引出与之对偶的 $\pi$ 形网络。反过来，每个 $Z_{12}=Z_{21}$ 的二端口网络都有一个不含电源的 T 形等效电路和一个 $\pi$ 形等效电路（第 [10](eigenschaften-und-alle-formen-im-uberblick.html#stufe-10) 阶段）。

:::abbildung et1/k6tpi 8
两种电路，同一个二端口网络。左为 15、20 和 20 $\Omega$ 的 T 形网络，右为等效的 50、50 和 66.7 $\Omega$ 的 $\pi$ 形网络。两者都有 $\det\mathbf Z=1000\,\Omega^2$。在端口上，任何测量都无法区分它们。
:::

**例。** $\det\mathbf Z=35\cdot40\,\Omega^2-20\cdot20\,\Omega^2=1000\,\Omega^2$，所以

$$\mathbf Y=\frac{1}{1000\,\Omega^2}\begin{pmatrix}40&-20\\-20&35\end{pmatrix}\Omega=\begin{pmatrix}40&-20\\-20&35\end{pmatrix}\mathrm{mS},$$

这正是短路试验的结果。$\pi$ 形网络的 $G_2=20$ mS，$G_1=40\,\mathrm{mS}-20\,\mathrm{mS}=20$ mS，$G_3=15$ mS，即 50 $\Omega$、50 $\Omega$ 和 66.7 $\Omega$。接同样的电源和负载，它同样给出 7.75 V 和 3 V。

⁠**极限情况：并非每种形式都存在。**串联电阻 $R$ 和并联电阻 $R$ 单独位于两个端口之间时，分别有

$$\mathbf Y_\text{串联}=G\begin{pmatrix}1&-1\\-1&1\end{pmatrix},\qquad\mathbf Z_\text{并联}=R\begin{pmatrix}1&1\\1&1\end{pmatrix}.$$

两个行列式都为零。串联电阻没有 Z 形式：这时总有 $I_2=-I_1$，电流不能自由选择，所以不能作为原因。并联电阻没有 Y 形式，因为总有 $U_1=U_2$。理想电流控制电流源也是如此：它的电流是刚性耦合的。

:::frage 为什么 $Y_{11}$ 为正，$Y_{21}$ 却为负？
这是参考箭头造成的。$U_2=0$ 时，端口 1 上的正电压驱动电流流入，$Y_{11}>0$。这个电流从另一个端口流出，但计数方向是流入。因此 T 形、$\pi$ 形等无源电路的转移电导为负。
:::

:::aufgabe 练习 6 ★ 去与回
<span class="anker" id="aufg-6"></span>

一个二端口网络有 $Z_{11}=20\,\Omega$，$Z_{12}=Z_{21}=10\,\Omega$，$Z_{22}=55\,\Omega$。

<ol class="al">

<li>

计算 $\mathbf Y$。

</li>

<li>

求 T 形网络和 $\pi$ 形网络的各电阻。

</li>

<li>

写出 100 $\Omega$ 串联电阻的 $\mathbf Y$。为什么 $\mathbf Z=\mathbf Y^{-1}$ 行不通？

</li>

</ol>

:::loesung
(a) $\det\mathbf Z=20\cdot55\,\Omega^2-10\cdot10\,\Omega^2=1000\,\Omega^2$，所以 $Y_{11}=55$ mS，$Y_{12}=Y_{21}=-10$ mS，$Y_{22}=20$ mS。 (b) T：$R_\mathrm{b}=10\,\Omega$，$R_\mathrm{a}=10\,\Omega$，$R_\mathrm{c}=45\,\Omega$。$\pi$：$G_2=10$ mS，$G_1=45$ mS，$G_3=10$ mS，即串联 100 $\Omega$，并联 22.2 $\Omega$ 和 100 $\Omega$。 (c) $Y_{11}=Y_{22}=10$ mS，$Y_{12}=Y_{21}=-10$ mS，$\det\mathbf Y=0$。逆矩阵不存在，因为总有 $I_2=-I_1$，电流不能自由选择。
:::
:::
