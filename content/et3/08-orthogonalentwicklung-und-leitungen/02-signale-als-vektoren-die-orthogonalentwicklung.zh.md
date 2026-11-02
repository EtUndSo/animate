---
title: 第 1 阶段：作为向量的信号——正交展开
pfad: 电气工程 / 第 3 学期 / 信号与系统 / 正交展开与传输线
order: 3280200
summary: 傅里叶级数把信号分解为振荡。同样的做法适用于任何正交函数系。本阶段说明如何求出系数，以及为什么这些系数给出最佳逼近。
tags: 正交, 标准正交, 广义帕塞瓦尔定理
lang: zh
---

<span class="anker" id="stufe-1"></span>

:::zweck
傅里叶级数把信号分解为振荡。同样的做法适用于任何正交函数系。本阶段说明如何求出系数，以及为什么这些系数给出最佳逼近。
:::

**思路。** 空间中的向量相对于相互垂直的单位向量 $\vec e_i$ 具有分量 $b_i=\vec f\cdot\vec e_i$。对于区间 $[0,T]$ 上的信号，积分 $\int_0^Tf(t)g(t)\mathrm{d} t$ 起着内积的作用。若该积分为零，则称两个信号__正交__（[第 6 部分](/wissen/zh/elektrotechnik/3-semester/signale-und-systeme/korrelationsfunktionen/korrelationsfunktionen.html)）。由 $M$ 个函数 $s_i(t)$ 组成的函数系称为__标准正交__的，条件是

<span class="anker" id="gl-1-1"></span>
$$\int_0^Ts_i(t)\,s_j(t)\,\mathrm{d} t=\begin{cases}1&i=j\\0&i\neq j\end{cases}. \tag{1.1}$$

用 $\sum_{i=0}^{M-1}b_is_i(t)$ 逼近能量信号 $f(t)$，剩下逼近误差 $r(t)=f(t)-\sum b_is_i(t)$。

:::satz 定理 1.1 (正交展开)
<span class="anker" id="satz-1-1"></span>

误差的能量 $E_r=\int_0^Tr^2\mathrm{d} t$ 取最小值的条件是

<span class="anker" id="gl-1-2"></span>
$$b_i=\int_0^Tf(t)\,s_i(t)\,\mathrm{d} t. \tag{1.2}$$

此时 $E_r=E_f-\sum_ib_i^2$。若随着 $M$ 增大有 $E_r\to0$（完备函数系），则__广义帕塞瓦尔定理__ $E_f=\sum_ib_i^2$ 成立。
:::

:::herleitung 系数与误差能量
$E_r=\int_0^T\bigl(f-\sum_ib_is_i\bigr)^2\mathrm{d} t$。对 $b_j$ 求导并令其为零：

$$\frac{\partial E_r}{\partial b_j}=-2\int_0^T\Bigl(f-\sum_ib_is_i\Bigr)s_j\,\mathrm{d} t=0\quad\Longrightarrow\quad\int_0^Tfs_j\,\mathrm{d} t=\sum_ib_i\int_0^Ts_is_j\,\mathrm{d} t=b_j.$$

由于标准正交性，和式中只剩下 $i=j$ 一项。代入这些 $b_i$ 并把平方展开，交叉项同样由于标准正交性而消失：$E_r=E_f-2\sum b_i^2+\sum b_i^2=E_f-\sum b_i^2$。
:::

⁠**如何理解：**每个系数都单独确定，与其他系数无关。增加一个基函数时，原有的系数保持不变。这就是正交函数系的优点，与傅里叶级数（[第 3 部分](/wissen/zh/elektrotechnik/3-semester/signale-und-systeme/fourier-reihe-und-transformation/fourier-reihe-und-transformation.html)）完全一样。$b_i$ 就是互相关 $\varphi^E_{fs_i}(0)$。正因为如此，可以用一组相关滤波器 $h_i(t)=s_i(T-t)$ 来测量这些系数，只需在 $t=T$ 时刻对它们的输出采样（[第 7 部分](/wissen/zh/elektrotechnik/3-semester/signale-und-systeme/zufallssignale/zufallssignale.html)）。

**例。** $[0,1]$ 上的 $f(t)=t^2$，$E_f=\frac15$。取 $s_0=1$ 和 $s_1=\sqrt3(2t-1)$：

$$b_0=\int_0^1t^2\mathrm{d} t=\tfrac13,\qquad b_1=\sqrt3\int_0^1t^2(2t-1)\mathrm{d} t=\tfrac{\sqrt3}{6}=0.289,\qquad\sum b_i^2=\tfrac19+\tfrac1{12}=\tfrac{7}{36}.$$

逼近式为 $\frac13+\frac{\sqrt3}{6}\sqrt3(2t-1)=t-\frac16$，即能量意义下的最佳直线。误差能量为 $\frac15-\frac7{36}=\frac{1}{180}=0.0056$，即 $E_f$ 的 2.8 %。再加上 $s_2=\sqrt5(6t^2-6t+1)$，就增加了系数 $b_2=\frac{\sqrt5}{30}=0.075$，而误差变为零，因为 $t^2$ 本身就是二次多项式。

:::aufgabe 练习 1 ★ 验证标准正交性
<span class="anker" id="aufg-1"></span>

证明 $s_0=1$ 和 $s_1=\sqrt3(2t-1)$ 在 $[0,1]$ 上是标准正交的。为什么 $s_1$ 需要因子 $\sqrt3$？

:::loesung
$\int_0^11\cdot\sqrt3(2t-1)\mathrm{d} t=\sqrt3\,[t^2-t]_0^1=0$：正交。$\int_0^11^2\mathrm{d} t=1$。$\int_0^13(2t-1)^2\mathrm{d} t=3\cdot\bigl[\frac{(2t-1)^3}{6}\bigr]_0^1=3\cdot\frac{1+1}{6}=1$。若没有这个因子，$2t-1$ 的能量只有 $\frac13$。因子 $\sqrt3$ 把它归一化到 1；否则 $b_1=\int fs_1\mathrm{d} t$ 就不是正确的系数。
:::
:::

:::aufgabe 练习 2 ★★ 最佳逼近
<span class="anker" id="aufg-2"></span>

<ol class="al">

<li>

对 $f(t)=t^2$ 重新计算 $b_1$，并验证逼近式 $t-\frac16$。

</li>

<li>

直接计算 $\int_0^1\bigl(t^2-t+\frac16\bigr)^2\mathrm{d} t$，以验证 $E_r=\frac{1}{180}$。

</li>

<li>

求 $f(t)=\sqrt2\cos(2\pi t)$ 关于 $s_0$ 和 $s_1$ 的系数。这个结果说明了什么？

</li>

</ol>

:::loesung
(a) $\int_0^1t^2(2t-1)\mathrm{d} t=\frac24-\frac13=\frac16$，因此 $b_1=\frac{\sqrt3}{6}$。逼近式：$\frac13+\frac{\sqrt3}{6}\cdot\sqrt3(2t-1)=\frac13+t-\frac12=t-\frac16$。

(b) $\int_0^1\bigl(t^2-t+\tfrac16\bigr)^2\mathrm{d} t=\int_0^1\bigl(t^4-2t^3+\tfrac43t^2-\tfrac13t+\tfrac1{36}\bigr)\mathrm{d} t=\tfrac15-\tfrac12+\tfrac49-\tfrac16+\tfrac1{36}=\tfrac{1}{180}$。

(c) $b_0=\sqrt2\int_0^1\cos(2\pi t)\mathrm{d} t=0$，$b_1=\sqrt6\int_0^1(2t-1)\cos(2\pi t)\mathrm{d} t=0$（余弦关于 $t=\frac12$ 对称，而 $2t-1$ 是反对称的）。两个系数都为零：该函数与两个基函数都正交，逼近结果为零，全部信号内容都留在误差中。一组基只适用于与其基函数相似的信号。
:::
:::
