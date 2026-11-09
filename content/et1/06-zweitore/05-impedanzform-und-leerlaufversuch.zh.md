---
title: 第 3 阶段：阻抗形式与开路试验
pfad: 电气工程 / 第 1 学期 / 电气工程基础 / 二端口网络
order: 1160500
summary: 第一种选择：电流是原因。本阶段说明，为什么开路的端口能逐个显露这四个数。
tags: Z 参数, 开路输入电阻, 开路输出电阻, 开路转移电阻, 二端量, 转移量, 阻抗
lang: zh
---

<span class="anker" id="stufe-3"></span>

:::zweck
第一种选择：电流是原因。本阶段说明，为什么开路的端口能逐个显露这四个数。
:::

**基本思路。** 每个电压都是 $I_1$ 的份额与 $I_2$ 的份额之和。要单独看到一个份额，另一个份额必须消失，也就是其电流必须为零。端口开路时，其电流为零。端口 2 开路时，两个方程中都只剩下 $I_1$ 的份额。所以一次试验给出两个参数，交换端口后的试验给出另外两个。

:::definition 定义 3.1 (阻抗形式，Z 形式)
<span class="anker" id="satz-3-1"></span>

阻抗形式（也称电阻形式）以电流为原因：

<span class="anker" id="gl-3-1"></span>
$$U_1=Z_{11}I_1+Z_{12}I_2,\quad U_2=Z_{21}I_1+Z_{22}I_2,\qquad\text{简写为}\quad\mathbf U=\mathbf Z\cdot\mathbf I,\quad\mathbf Z=\begin{pmatrix}Z_{11}&Z_{12}\\mathbb{Z}_{21}&Z_{22}\end{pmatrix}. \tag{3.1}$$

__Z 参数__由两次开路试验得到：

<span class="anker" id="gl-3-2"></span>
$$Z_{11}=\left.\frac{U_1}{I_1}\right|_{I_2=0},\quad Z_{21}=\left.\frac{U_2}{I_1}\right|_{I_2=0},\quad Z_{12}=\left.\frac{U_1}{I_2}\right|_{I_1=0},\quad Z_{22}=\left.\frac{U_2}{I_2}\right|_{I_1=0}. \tag{3.2}$$
:::

⁠**如何理解：**$Z_{11}$ 是__开路输入电阻__，$Z_{22}$ 是__开路输出电阻__，$Z_{21}$ 是正向__开路转移电阻__，$Z_{12}$ 是反向开路转移电阻。它们的单位都是 $\Omega$，典型值从欧姆到兆欧。下标相同的参数称为__二端量__：它们是另一侧端接固定时一对接线端的电阻。下标不同的参数称为__转移量__：它们联系两侧。字母 $Z$ 代表__阻抗__。它把电阻推广到交流量下的电容器和电感线圈。这里所有的 $Z$ 都是实电阻，对它们有 $Z_{ii}=R_{ii}$。**适用条件：**两个电流都必须可以自由选择（第 [6](umrechnen-t-und.html#stufe-6) 阶段）。

**等效电路。** 这两个方程可以画出来（图 [4](#abb-4) 左）。电压之和就是串联。$Z_{11}I_1$ 取决于本端口的电流，这是一个电阻。$Z_{12}I_2$ 取决于另一端口的电流，这是一个受控电压源（CCVS）。端口 2 的构成完全相同。从这张图可以看到开路的机理：$I_2=0$ 时，电源 $Z_{12}I_2$ 提供零伏，$Z_{22}$ 中没有电流（图 [4](#abb-4) 右）。$U_1$ 只降在 $Z_{11}$ 上，$U_2$ 就是电源电压 $Z_{21}I_1$。

:::abbildung et1/k6zesb 4
左：Z 形式的等效电路，每侧一个电阻与一个电流控制电压源串联。右：端口 2 的开路试验，注入电流为 $I_\mathrm{q}$。灰色部分因 $I_2=0$ 而不起作用。端口 1 开路的试验是其镜像，给出 $Z_{12}$ 和 $Z_{22}$。
:::

::::beispiel
在 T 形网络的端口 1 注入 100 mA 电流，端口 2 保持开路。电流流过 $R_\mathrm{a}$ 和 $R_\mathrm{b}$，$U_1=3.5$ V。$R_\mathrm{c}$ 中没有电流，上面没有压降，$U_2$ 就是 $R_\mathrm{b}$ 上的电压：2 V。所以 $Z_{11}=35\,\Omega$，$Z_{21}=20\,\Omega$。从端口 2 同样操作得 $U_2=4$ V，$U_1=2$ V，于是

$$\mathbf Z=\begin{pmatrix}R_\mathrm{a}+R_\mathrm{b}&R_\mathrm{b}\\mathbb{R}_\mathrm{b}&R_\mathrm{b}+R_\mathrm{c}\end{pmatrix}=\begin{pmatrix}35&20\\20&40\end{pmatrix}\Omega.$$
::::

⁠**电桥。**这些试验不需要地线。图 [2](vom-vierpol-zum-zweitor.html#abb-2) 右的电桥因两条支路电阻相同，把端口 1 的电流平分，两条支路都是 $R_\mathrm{x}+R_\mathrm{y}$。端口 2 开路，两条支路中点之间的电压为 $\frac{I_1}{2}R_\mathrm{y}-\frac{I_1}{2}R_\mathrm{x}$。由对称性，反向同样成立：

<span class="anker" id="gl-3-3"></span>
$$Z_{11}=Z_{22}=(R_\mathrm{x}+R_\mathrm{y})\parallel(R_\mathrm{x}+R_\mathrm{y})=\frac{R_\mathrm{x}+R_\mathrm{y}}{2},\qquad Z_{21}=Z_{12}=\frac{R_\mathrm{y}-R_\mathrm{x}}{2}. \tag{3.3}$$

⁠**极限情况：**$R_\mathrm{b}\to0$ 时 $Z_{12}=Z_{21}=0$：并联支路是一根导线，两个端口解耦。$R_\mathrm{x}=R_\mathrm{y}$ 时电桥平衡（[第 4 部分](/wissen/zh/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/strom-und-spannung-messen/strom-und-spannung-messen.html)），同样 $Z_{21}=0$。

:::frage 为什么在输入端用电流而不用电压？我手边更容易有电压源。
这也可以。重要的只是另一个端口开路。然后测量 $U_1$ 和 $I_1$，求它们的商。注入电流只是符合这种形式的思路：它是原因，电压是结果。
:::

:::aufgabe 练习 3 ★★ 作为二端口网络的电桥
<span class="anker" id="aufg-3"></span>

在图 [2](vom-vierpol-zum-zweitor.html#abb-2) 的电桥中，设 $R_\mathrm{x}=30\,\Omega$，$R_\mathrm{y}=50\,\Omega$。

<ol class="al">

<li>

求 $\mathbf Z$，并由此求具有相同四个参数的 T 形网络。

</li>

<li>

端口 1 通 100 mA、端口 2 开路时，$U_1$ 和 $U_2$ 是多少？

</li>

<li>

交换两个值，$R_\mathrm{x}=50\,\Omega$，$R_\mathrm{y}=30\,\Omega$。$\mathbf Z$ 和 T 形网络有什么变化？这个结果意味着什么？

</li>

</ol>

:::loesung
(a) 由式 [(3.3)](#gl-3-3)：$Z_{11}=Z_{22}=40\,\Omega$，$Z_{12}=Z_{21}=10\,\Omega$。T 形网络：$R_\mathrm{b}=Z_{12}=10\,\Omega$，$R_\mathrm{a}=R_\mathrm{c}=30\,\Omega$。 (b) $U_1=40\,\Omega\cdot100\,\mathrm{mA}=4$ V，$U_2=10\,\Omega\cdot100\,\mathrm{mA}=1$ V。直接计算：两条支路各 50 mA，$U_2=50\,\mathrm{mA}\cdot(50-30)\,\Omega=1$ V。 (c) $Z_{11}$ 和 $Z_{22}$ 不变，$Z_{12}=Z_{21}=-10\,\Omega$。T 形网络将有 $R_\mathrm{b}=-10\,\Omega$，$R_\mathrm{a}=R_\mathrm{c}=50\,\Omega$。负元件并不存在，这里的 T 只是一个计算量。它表示：在相同的 $I_1$ 下，$U_2$ 的符号相反。
:::
:::
