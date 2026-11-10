---
title: 第 10 阶段：性质与全部形式概览
pfad: 电气工程 / 第 1 学期 / ET1 – 电气工程基础 1：电路分析导论 / 二端口网络
adresse: elektrotechnik/1-semester/grundlagen-der-elektrotechnik/zweitore
knoten: 第 6 章：二端口网络
order: 1161200
summary: 这四个数透露的不只是端口上的行为。本阶段从中读出三种性质：二端口网络在两个方向上的作用相同吗？它究竟有没有反向作用？它能获得功率吗？最后把所有形式并列。
tags: 互易, 有源, 无源, 小信号工作
lang: zh
---

<span class="anker" id="stufe-10"></span>

:::zweck
这四个数透露的不只是端口上的行为。本阶段从中读出三种性质：二端口网络在两个方向上的作用相同吗？它究竟有没有反向作用？它能获得功率吗？最后把所有形式并列。
:::

**基本思路。** 电阻不分方向，其电流只取决于两端的电压差。因此，电阻网络从端口 1 到端口 2 的作用与反方向一样强：交换原因和结果的位置，商不变。而受控源有方向。它从控制量作用到其输出，绝不反向。只有它才能打破对称性。也只有它能从外部引入能量。

:::definition 定义 10.1 (互易、无反向作用、有源)
<span class="anker" id="satz-10-1"></span>

如果相同的原因在两个方向上显示相同的结果，二端口网络就称为__互易__网络（也称可逆、传输对称）。如果输入不取决于输出，就称为无反向作用网络：

<span class="anker" id="gl-10-1"></span>
<span class="anker" id="gl-10-2"></span>
$$\begin{aligned} \text{互易：}\quad&Z_{12}=Z_{21},\quad Y_{12}=Y_{21},\quad H_{12}=-H_{21},\quad\det\mathbf A=1,\\ \text{无反向作用：}\quad&Z_{12}=0,\quad Y_{12}=0,\quad H_{12}=0,\quad\det\mathbf A=0. \end{aligned} \tag{10.1|10.2}$$

设 $P_1=U_1I_1$，输出功率 $P_2=-U_2I_2$，二端口网络吸收的功率为

<span class="anker" id="gl-10-3"></span>
$$P=P_1-P_2=U_1I_1+U_2I_2=Y_{11}U_1^2+(Y_{12}+Y_{21})U_1U_2+Y_{22}U_2^2. \tag{10.3}$$

如果在某个工作状态下可能有 $P<0$，二端口网络就是__有源__的；如果总有 $P\ge0$，就是__无源__的。
:::

⁠**如何理解：**如果端口 1 的 1 A 在开路的端口 2 上产生一个电压，那么在互易二端口网络中，端口 2 的 1 A 在开路的端口 1 上产生相同的电压（图 [12](#abb-12)）。这就是 $Z_{21}=Z_{12}$。在节点方程（[第 8 章](/wissen/zh/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/maschenstrom-und-knotenpotentialverfahren/maschenstrom-und-knotenpotential.html)）中，每个电阻把它的电导填入两个镜像位置，所以矩阵保持对称。互易并不意味着镜像对称：T 形网络有 $Z_{11}\neq Z_{22}$，却仍是互易的。由于第四个参数已确定，互易二端口网络只有三个自由参数，正好对应 T 形和 $\pi$ 形的三个元件。它总可以用不含电源的 T 形或 $\pi$ 形网络来模拟，元件值允许为负。无反向作用时，同样有三个数是自由的：输入电阻、输出电阻、控制量。这是放大器的基本形式。$\mathbf A$ 和 $\mathbf H$ 的条件由下面的换算得出。式 [(10.3)](#gl-10-3) 中 $P_2$ 的负号是因为 $I_2$ 指向内部。最后一种形式由代入式 [(5.1)](admittanzform-und-kurzschlussversuch.html#gl-5-1) 得到。

:::abbildung et1/k6umkehr 12
左：T 形网络。100 mA 在另一个开路端口上产生的电压在两个方向上都是 2 V，尽管 $R_\mathrm{a}\neq R_\mathrm{c}$。右：放大器模型。端口 1 的 1 µ A 在端口 2 上产生 $-2$ V，端口 2 的 1 µ A 在端口 1 上产生 0 V。
:::

::::beispiel
T 形网络吸收 $P_1=7.75\,\mathrm{V}\cdot250\,\mathrm{mA}=1.9375$ W，输出 $P_2=3\,\mathrm{V}\cdot50\,\mathrm{mA}=0.15$ W。差值 $P=1.7875$ W 正是电阻中的热量：$0.9375+0.8+0.05$ W。每个电阻吸收 $I^2R\geq0$，因此由电阻组成的二端口网络总是无源的。含电容器和电感线圈时也是如此。无源二端口网络甚至可以包含受控源，起决定作用的只有 $P$。放大器模型吸收 $P_1=20\,\mathrm{mV}\cdot10\,\mu\text{A}=0.2$ µ W，向负载输出 $P_2=4\,\mathrm{V}\cdot0.8\,\mathrm{mA}=3.2$ mW，是前者的 16 000 倍。它是有源的。能量不是来自输入信号，而是来自用于供电的辅助电源，它不出现在二端口模型中。这个模型适用于固定直流状态附近的小信号（__小信号工作__，[第 10 章](/wissen/zh/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/der-bipolartransistor/der-bipolartransistor.html)）。
::::

⁠**极限情况：**$U_1=U_2=0$ 时 $P=0$。由理想导线组成的二端口网络在任何状态下都有 $P=0$，它是无源的，没有任何损失。

:::ltspice 功率从哪里来
⁠**绘制：**电压源 `voltage` 取 `20m`，从 `1` 接地，`Rin` 取 `2k`，从 `1` 接地。受控电流源 `g` 取 `50m`：输出从 `2` 接地，控制输入从 `1` 接地。`res` 取 `20k`，`res` 取 `5k`，都从 `2` 接地。这个值是 $Y_{21}=H_{21}/H_{11}$。

⁠**指令：**`.op`，`.meas op Uout FIND V(2)`，`.meas op Pin PARAM V(1)*I(Rin)`，`.meas op Pload PARAM V(2)*V(2)/5000`，`.meas op Pg PARAM V(2)*I(G1)`。

⁠**你会看到：**$\mathtt{Uout}=-4$ V，`Pin` $=0.2$ µ W，`Pload` $=3.2$ mW，`Pg` $=-4$ mW。受控源输出 4 mW，其中 3.2 mW 送给负载，其余使 20 k$\Omega$ 发热。为练习 [10](#aufg-10)(b) 设置数值 `10m`、`1k`、`50m`、`50k` 和 `10k`，得 $\mathtt{Uout}=-4.17$ V。
:::

**全部形式一览。** 同样的四个量，四种原因的选择：

| 形式 | 原因 | 结果 | T 形网络 |
|---|---|---|---|
| Z（电阻矩阵） | $I_1$，$I_2$ | $U_1$，$U_2$ | $Z_{11}=35\,\Omega$，$Z_{12}=Z_{21}=20\,\Omega$，$Z_{22}=40\,\Omega$ |
| Y（电导矩阵） | $U_1$，$U_2$ | $I_1$，$I_2$ | $Y_{11}=40$ mS，$Y_{12}=Y_{21}=-20$ mS，$Y_{22}=35$ mS |
| H（串并联矩阵） | $I_1$，$U_2$ | $U_1$，$I_2$ | $H_{11}=25\,\Omega$，$H_{12}=0.5$，$H_{21}=-0.5$，$H_{22}=25$ mS |
| A（链式矩阵） | $U_2$，$-I_2$ | $U_1$，$I_1$ | $A_{11}=1.75$，$A_{12}=50\,\Omega$，$A_{21}=50$ mS，$A_{22}=2$ |

每次换算都是把两个方程对新的量求解。以下供查阅，每个矩阵都由另外三个矩阵表示：

$$\mathbf Z=\begin{pmatrix}\frac{Y_{22}}{\det\mathbf Y}&\frac{-Y_{12}}{\det\mathbf Y}\\[3pt]\frac{-Y_{21}}{\det\mathbf Y}&\frac{Y_{11}}{\det\mathbf Y}\end{pmatrix} =\begin{pmatrix}\frac{\det\mathbf H}{H_{22}}&\frac{H_{12}}{H_{22}}\\[3pt]\frac{-H_{21}}{H_{22}}&\frac{1}{H_{22}}\end{pmatrix} =\begin{pmatrix}\frac{A_{11}}{A_{21}}&\frac{\det\mathbf A}{A_{21}}\\[3pt]\frac{1}{A_{21}}&\frac{A_{22}}{A_{21}}\end{pmatrix},$$

$$\mathbf Y=\begin{pmatrix}\frac{Z_{22}}{\det\mathbf Z}&\frac{-Z_{12}}{\det\mathbf Z}\\[3pt]\frac{-Z_{21}}{\det\mathbf Z}&\frac{Z_{11}}{\det\mathbf Z}\end{pmatrix} =\begin{pmatrix}\frac{1}{H_{11}}&\frac{-H_{12}}{H_{11}}\\[3pt]\frac{H_{21}}{H_{11}}&\frac{\det\mathbf H}{H_{11}}\end{pmatrix} =\begin{pmatrix}\frac{A_{22}}{A_{12}}&\frac{-\det\mathbf A}{A_{12}}\\[3pt]\frac{-1}{A_{12}}&\frac{A_{11}}{A_{12}}\end{pmatrix},$$

$$\mathbf H=\begin{pmatrix}\frac{\det\mathbf Z}{Z_{22}}&\frac{Z_{12}}{Z_{22}}\\[3pt]\frac{-Z_{21}}{Z_{22}}&\frac{1}{Z_{22}}\end{pmatrix} =\begin{pmatrix}\frac{1}{Y_{11}}&\frac{-Y_{12}}{Y_{11}}\\[3pt]\frac{Y_{21}}{Y_{11}}&\frac{\det\mathbf Y}{Y_{11}}\end{pmatrix} =\begin{pmatrix}\frac{A_{12}}{A_{22}}&\frac{\det\mathbf A}{A_{22}}\\[3pt]\frac{-1}{A_{22}}&\frac{A_{21}}{A_{22}}\end{pmatrix},$$

$$\mathbf A=\begin{pmatrix}\frac{Z_{11}}{Z_{21}}&\frac{\det\mathbf Z}{Z_{21}}\\[3pt]\frac{1}{Z_{21}}&\frac{Z_{22}}{Z_{21}}\end{pmatrix} =\begin{pmatrix}\frac{-Y_{22}}{Y_{21}}&\frac{-1}{Y_{21}}\\[3pt]\frac{-\det\mathbf Y}{Y_{21}}&\frac{-Y_{11}}{Y_{21}}\end{pmatrix} =\begin{pmatrix}\frac{-\det\mathbf H}{H_{21}}&\frac{-H_{11}}{H_{21}}\\[3pt]\frac{-H_{22}}{H_{21}}&\frac{-1}{H_{21}}\end{pmatrix}.$$

由 $\mathbf A$ 得出式 [(10.1)](#gl-10-1) 和式 [(10.2)](#gl-10-2) 中的条件：由第一行，$Z_{12}=\det\mathbf A/A_{21}$，$Z_{21}=1/A_{21}$，所以 $\det\mathbf A=Z_{12}/Z_{21}$。互易时它为 1，无反向作用时它为 0。同样，$Z_{12}=H_{12}/H_{22}$，$Z_{21}=-H_{21}/H_{22}$，因此 $H_{12}=-H_{21}$。

:::frage 那么，非互易就意味着有源吗？
不是。互易是关于对称性的说法，有源是关于功率的说法。两者虽然都与受控源有关，却不是一回事。练习 [10](#aufg-10)(d) 给出一个 $Z_{12}\neq Z_{21}$ 却从不获得功率的二端口网络。
:::

:::aufgabe 练习 10 ★★ 读出性质
<span class="anker" id="aufg-10"></span>

对每个二端口网络检验：它是互易的吗？无反向作用吗？有源还是无源？

<ol class="al">

<li>

$Y_{11}=2$ mS，$Y_{12}=Y_{21}=-1$ mS，$Y_{22}=3$ mS。提示：画出 $\pi$ 形网络。

</li>

<li>

$H_{11}=1$ k$\Omega$，$H_{12}=0$，$H_{21}=50$，$H_{22}=20$ µ S，负载 10 k$\Omega$，$U_1=10$ mV。

</li>

<li>

$A_{11}=2$，$A_{12}=30\,\Omega$，$A_{21}=0.1$ S，$A_{22}=2$。

</li>

<li>

$Z_{11}=Z_{22}=10\,\Omega$，$Z_{12}=5\,\Omega$，$Z_{21}=-5\,\Omega$。为此由 $U_1I_1+U_2I_2$ 计算 $P$。

</li>

</ol>

:::loesung
(a) 互易，$Y_{12}=Y_{21}$，有反向作用。$\pi$ 形网络的 $G_2=1$ mS，$G_1=1$ mS，$G_3=2$ mS，都为正：都是电阻，所以无源。

(b) $H_{12}=0$：无反向作用，非互易（$H_{21}\neq-H_{12}$）。$I_1=10$ µ A，输出端把 0.5 mA 送入 $50\,\text{k}\Omega\parallel10\,\text{k}\Omega=8.33$ k$\Omega$，$U_2=-4.17$ V。$P_1=0.1$ µ W，$P_2=U_2^2/R_\mathrm{L}=1.74$ mW。有源。

(c) $\det\mathbf A=4-3=1$：互易，有反向作用。由 $Z_{11}=Z_{22}=20\,\Omega$，$Z_{12}=Z_{21}=10\,\Omega$ 得由正电阻 10、10、10 $\Omega$ 组成的 T 形网络：无源，并且因 $A_{11}=A_{22}$ 而镜像对称。

(d) $Z_{12}=5\,\Omega\neq Z_{21}=-5\,\Omega$：非互易，有反向作用。$P=I_1(10I_1+5I_2)+I_2(-5I_1+10I_2)=10\,\Omega\,(I_1^2+I_2^2)\geq0$：无源。交叉项相互抵消。这是一个非互易但无源的二端口网络。
:::
:::
