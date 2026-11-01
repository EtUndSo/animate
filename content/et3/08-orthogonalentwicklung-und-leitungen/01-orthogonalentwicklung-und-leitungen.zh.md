---
title: 正交展开与传输线
pfad: 电气工程 / 第 3 学期 / 信号与系统 / 正交展开与传输线
order: 3280100
summary: 两个补充专题：作为向量的信号， 电传输线上的波
tags: 正交, 标准正交, 广义帕塞瓦尔定理, 单位长度参数, 波动方程, 传播常数, 特性阻抗, 衰减常数
lang: zh
---

## 本文内容

本文在第 1 至[第 7 部分](/wissen/zh/elektrotechnik/3-semester/signale-und-systeme/zufallssignale/zufallssignale.html)的基础上补充两个专题。第一个专题推广了傅里叶级数：把信号按任意一组正交函数分解，就像把向量分解为它的各个分量一样。第二个专题说明长传输线上会发生什么：电压和电流以波的形式传播，并可能在终端被反射。最佳量化器本可作为第三个补充专题，但它已在[第 7 部分](/wissen/zh/elektrotechnik/3-semester/signale-und-systeme/zufallssignale/zufallssignale.html)（第 5 阶段）中讨论过。

:::merke 三句话的答案（读完本文后应觉得理所当然）
<ol>

<li>

对于标准正交基函数，函数的最佳系数就是它与该基函数的相关，而能量等于各系数的平方和。

</li>

<li>

在传输线上，每个电压都是一个入射波与一个反射波的叠加。传输线由传播常数 $\gamma$ 和特性阻抗 $Z$ 描述。

</li>

<li>

若在传输线终端接上等于其特性阻抗的负载，反射波就会消失。在无损传输线上，所有频率的传播速度都相同，信号无失真地到达。

</li>

</ol>
:::

**如何使用本文。**每个阶段包括基本思路、可展开解答的典型问题以及练习（★ 到 ★★★）。请先自己尝试，解答可在每道练习下方展开。

:::merke 本文的参考模型
<ul>

<li>

⁠**正交展开**：把 $[0,1]$ 上的 $f(t)=t^2$ 按标准正交多项式 $s_0=1$，$s_1=\sqrt3(2t-1)$，$s_2=\sqrt5(6t^2-6t+1)$ 展开。

</li>

<li>

⁠**同轴电缆**：$Z=50\,\Omega$，$C'=100$ pF/m，无损。

</li>

</ul>
:::

## 第 1 阶段：作为向量的信号——正交展开

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

## 第 2 阶段：传输线方程

<span class="anker" id="stufe-2"></span>

:::zweck
到目前为止，导线都被看作理想的连接。如果一条线路的长度与波长相比很长，信号通过它就需要一段可察觉的时间。本阶段建立描述这一现象的方程。
:::

**思路。** 把传输线分成长度为 $\mathrm{d} s$ 的许多小段。每一小段都有一个串联电阻和一个串联电感（来自去线和回线），以及一个并联电容和一个并联电导（位于两导线之间）。对于均匀传输线，这些量与长度成正比：$R'\mathrm{d} s$，$L'\mathrm{d} s$，$C'\mathrm{d} s$，$G'\mathrm{d} s$，其中 $R'$、$L'$、$C'$、$G'$ 为__单位长度参数__（分布参数），即每米的值（图 [1](#abb-1)）。

:::abbildung et3/k8element
长度为 $\mathrm{d} s$ 的一小段传输线的等效电路，含单位长度参数 $R'$、$L'$、$G'$、$C'$。
:::

:::satz 定理 2.1 (传输线方程（电报方程）)
<span class="anker" id="satz-2-1"></span>

<span class="anker" id="gl-2-1"></span>
$$\frac{\partial u}{\partial s}=-\Bigl(R'+L'\frac{\partial}{\partial t}\Bigr)i,\qquad\frac{\partial i}{\partial s}=-\Bigl(G'+C'\frac{\partial}{\partial t}\Bigr)u. \tag{2.1}$$
:::

:::herleitung 传输线方程
对这一小段应用基尔霍夫电压定律：$u=R'\mathrm{d} s\,i+L'\mathrm{d} s\,\frac{\partial i}{\partial t}+\bigl(u+\frac{\partial u}{\partial s}\mathrm{d} s\bigr)$，因此 $\frac{\partial u}{\partial s}\mathrm{d} s=-R'\mathrm{d} s\,i-L'\mathrm{d} s\,\frac{\partial i}{\partial t}$。基尔霍夫电流定律：电流 $i$ 的一部分经 $G'\mathrm{d} s$ 和 $C'\mathrm{d} s$ 流走，$i=G'\mathrm{d} s\,u+C'\mathrm{d} s\,\frac{\partial u}{\partial t}+\bigl(i+\frac{\partial i}{\partial s}\mathrm{d} s\bigr)$。再除以 $\mathrm{d} s$。（严格地说，电流定律中出现的是这一小段末端的电压；二者之差是 $\mathrm{d} s$ 的二阶小量。）
:::

⁠**如何理解：**电压沿传输线下降，因为有电流流过串联元件。电流沿传输线减小，因为它经由导线之间的并联元件漏走。这两个方程在空间和时间上把 $u$ 和 $i$ 耦合起来。

## 第 3 阶段：正弦激励下的波

<span class="anker" id="stufe-3"></span>

:::zweck
借助相量，偏微分方程变成关于位置的常微分方程。它的解由两个沿相反方向传播的波组成。
:::

令 $u(s,t)=\sqrt2\operatorname{Re}\{\underline U(s)\mathrm{e}^{\mathrm{j}2\pi ft}\}$，对 $i$ 也同样处理，则 $\frac{\partial}{\partial t}$ 变为 $\mathrm{j}2\pi f$：

$$\frac{\mathrm{d}\underline U}{\mathrm{d} s}=-(R'+\mathrm{j}2\pi fL')\,\underline I,\qquad\frac{\mathrm{d}\underline I}{\mathrm{d} s}=-(G'+\mathrm{j}2\pi fC')\,\underline U.$$

对第一个方程求导并代入第二个方程，得到__波动方程__ $\frac{\mathrm{d}^2\underline U}{\mathrm{d} s^2}=\gamma^2\underline U$。

:::satz 定理 3.1 (入射波与反射波)
<span class="anker" id="satz-3-1"></span>

<span class="anker" id="gl-3-1"></span>
$$\underline U(s)=\underline U_1\mathrm{e}^{-\gamma s}+\underline U_2\mathrm{e}^{\gamma s},\qquad\underline I(s)=\frac{1}{Z}\bigl(\underline U_1\mathrm{e}^{-\gamma s}-\underline U_2\mathrm{e}^{\gamma s}\bigr), \tag{3.1}$$

其中__传播常数__和__特性阻抗__为

<span class="anker" id="gl-3-2"></span>
$$\gamma=\sqrt{(R'+\mathrm{j}2\pi fL')(G'+\mathrm{j}2\pi fC')}=\alpha+\mathrm{j}\beta,\qquad Z=\sqrt{\frac{R'+\mathrm{j}2\pi fL'}{G'+\mathrm{j}2\pi fC'}}. \tag{3.2}$$
:::

⁠**如何理解：**令 $\gamma=\alpha+\mathrm{j}\beta$，第一项在时域中变为 $\hat u_1\mathrm{e}^{-\alpha s}\cos(2\pi ft-\beta s+\varphi_1)$：这是一个沿 $s$ 增大方向传播、并在传播过程中以__衰减常数__ $\alpha$ 衰减的波。过零点以速度 $v=2\pi f/\beta$ 移动，波长为 $\lambda=2\pi/\beta$。第二项沿相反方向传播。$Z$ 是单个波中电压与电流之比。常数 $\underline U_1$、$\underline U_2$ 由边界条件确定，例如由始端的电压和电流确定：$\underline U_{1,2}=\frac12(\underline U_a\pm Z\underline I_a)$。

**终端的反射。** 若传输线在终端（$s=l$）接有电阻 $R_\mathrm E=\underline U_e/\underline I_e$，则电压可以写成

<span class="anker" id="gl-3-3"></span>
$$\underline U(s)=\tfrac12(R_\mathrm E+Z)\,\underline I_e\,\mathrm{e}^{\gamma(l-s)}+\tfrac12(R_\mathrm E-Z)\,\underline I_e\,\mathrm{e}^{-\gamma(l-s)}. \tag{3.3}$$

第一项是正向行波（入射波），第二项是从终端返回的波（反射波）。当 $R_\mathrm E=Z$ 时，反射波消失：以特性阻抗作终端负载时，到达的波被完全吸收，就好像传输线无限延伸下去一样。终端处两个波之比就是__反射系数__ $r=\frac{R_\mathrm E-Z}{R_\mathrm E+Z}$（补充：短路时 $r=-1$，开路时 $r=+1$）。

:::frage 为什么对于短线，终端负载不正确也不会造成影响？
因为这时反射波几乎立刻就返回了。若沿传输线的传播时延与信号变化的持续时间相比很小（线长与波长相比很短），入射波与反射波实际上是同时叠加的，人们只会察觉到终端电阻。只有当传播时延变得可以相比拟时，例如对于快速数字信号或在高频下，反射才会以回波的形式出现并使信号失真。
:::

## 第 4 阶段：无损传输线

<span class="anker" id="stufe-4"></span>

:::zweck
没有损耗（$R'=G'=0$）时，特性阻抗和传播速度都与频率无关。于是波动解对任意信号都成立，而不仅限于正弦信号。
:::

当 $R'=G'=0$ 时，$\gamma=\mathrm{j}2\pi f\sqrt{L'C'}$：没有衰减（$\alpha=0$），且 $\beta$ 与 $f$ 成正比。由此得：

<span class="anker" id="gl-4-1"></span>
$$Z=\sqrt{\frac{L'}{C'}},\qquad v=\frac{1}{\sqrt{L'C'}},\qquad\frac{\partial^2u}{\partial s^2}=L'C'\frac{\partial^2u}{\partial t^2}. \tag{4.1}$$

:::satz 定理 4.1 (达朗贝尔解)
<span class="anker" id="satz-4-1"></span>

波动方程 [(4.1)](#gl-4-1) 的每个解都具有形式

<span class="anker" id="gl-4-2"></span>
$$u(s,t)=u_\mathrm{fw}(s-vt)+u_\mathrm{bw}(s+vt) \tag{4.2}$$

其中 $u_\mathrm{fw}$（正向）和 $u_\mathrm{bw}$（反向）是任意（二次可微的）函数。
:::

⁠**如何理解：**任意的信号波形都以速度 $v$ 沿传输线不变地传播。这是因为所有频率分量都同样快，衰减也同样小：传输线是[第 5 部分](/wissen/zh/elektrotechnik/3-semester/signale-und-systeme/tiefpass-und-bandpasssysteme/tiefpass-und-bandpasssysteme.html)意义上的无失真系统，时延为 $l/v$。$u$ 的波动方程可由式 [(2.1)](#gl-2-1) 得到：把第一个方程对 $s$ 求导，把第二个方程对 $t$ 求导，再消去 $i$。

**例：同轴电缆。** 由 $Z=50\,\Omega$ 和 $C'=100$ pF/m 得 $L'=Z^2C'=250$ nH/m 以及 $v=\frac{1}{\sqrt{L'C'}}=2\cdot10^8$ m/s，即光速的三分之二（由于电缆中的电介质）。信号通过 10 m 电缆需要 50 ns。若电缆终端接的是 75 $\Omega$ 而不是 50 $\Omega$，则 $r=\frac{75-50}{75+50}=0.2$：电压幅度的 20 % 作为回波返回。

:::ltspice 传输线上的反射
⁠**绘制：**电压源 `voltage`，取 `PULSE(0 2 0 1n 1n 10n 1)`，内阻 `res` 取 `50`，接到节点 `in`。从 `in` 引出一条无损传输线 `tline`，取 `Td=50n Z0=50`（例子中 10 m 长的同轴电缆），接到节点 `end`，在那里接 `res`，取 `{RE}`，接地。由于内阻等于 $Z$，出发的是一个 1 V 的波，而回波在信号源处被完全吸收。

⁠**指令：**`.param RE=75`，`.step param RE list 1m 50 75 1G`（几乎短路、匹配、75 $\Omega$、几乎开路），`.tran 0 200n 0 0.1n`。

⁠**你会看到：**在 `in` 处，首先是 1 V 的脉冲。经过 $2\cdot50\,\mathrm{ns}=100$ ns 后，回波以高度 $r\cdot1$ V 返回：$-1$、$0$、$0.2$ 和 $+1$，恰好是 $r=\frac{R_\mathrm E-Z}{R_\mathrm E+Z}$。在 `end` 处，50 ns 后出现的是正向波与反向波之和，$(1+r)\cdot1$ V。把 `Td` 和 `Z0` 设为你在练习 [4](#aufg-4)(a) 中得到的值，把 `RE` 设为 100，并把回波高度与你在练习 [4](#aufg-4)(b) 中的结果比较。
:::

:::aufgabe 练习 3 ★★ 验证达朗贝尔解
<span class="anker" id="aufg-3"></span>

通过代入证明：$u(s,t)=u_\mathrm{fw}(s-vt)$ 在 $v=1/\sqrt{L'C'}$ 时是波动方程 [(4.1)](#gl-4-1) 的解。相应的电流与电压有什么关系？提示：利用 $R'=0$ 时的第一个传输线方程。

:::loesung
令 $x=s-vt$：$\frac{\partial^2u}{\partial s^2}=u_\mathrm{fw}''(x)$，$\frac{\partial^2u}{\partial t^2}=v^2u_\mathrm{fw}''(x)$。波动方程要求 $u''=L'C'v^2u''$，因此 $v^2=\frac{1}{L'C'}$。电流：当 $R'=0$ 时，$\frac{\partial u}{\partial s}=-L'\frac{\partial i}{\partial t}$，因此 $u_\mathrm{fw}'(x)=-L'\frac{\partial i}{\partial t}$。设 $i=u_\mathrm{fw}(x)/Z$，得 $\frac{\partial i}{\partial t}=-\frac vZu'_\mathrm{fw}$；由于 $L'v/Z=L'\cdot\frac{1}{\sqrt{L'C'}}\cdot\sqrt{\frac{C'}{L'}}=1$，二者是一致的。在正向行波中，电压与电流处处之比为 $Z$。
:::
:::

:::aufgabe 练习 4 ★★ 电缆与终端负载
<span class="anker" id="aufg-4"></span>

一条无损电缆的 $L'=300$ nH/m，$C'=120$ pF/m。

<ol class="al">

<li>

计算 $Z$、$v$ 以及 5 m 电缆的传播时延。

</li>

<li>

终端必须接多大的电阻，才不会产生反射？终端接 100 $\Omega$ 时，反射系数是多少？

</li>

<li>

若要求线长至多为波长的十分之一，那么 5 m 电缆在多高的频率以下仍可视为“短”线？

</li>

</ol>

:::loesung
(a) $Z=\sqrt{300/120}\cdot\sqrt{\frac{\text{nH}}{\text{pF}}}=\sqrt{2.5\cdot10^3}\,\Omega=50\,\Omega$。$v=\frac{1}{\sqrt{300\cdot10^{-9}\cdot120\cdot10^{-12}}}\,\mathrm{m/s}=\frac{1}{\sqrt{3.6\cdot10^{-17}}}\,\mathrm{m/s}=1.67\cdot10^8$ m/s。5 m 的传播时延：30 ns。

(b) 接 $Z=50\,\Omega$ 的电阻。接 100 $\Omega$ 时：$r=\frac{100-50}{150}=\frac13$。

(c) $\lambda=v/f\ge50$ m，因此 $f\le\frac{1.67\cdot10^8}{50}\,\mathrm{Hz}=3.3$ MHz。
:::
:::

:::kern 要点
<ul>

<li>

标准正交：$\int s_is_j\mathrm{d} t=\delta_{ij}$；最佳系数 $b_i=\int fs_i\mathrm{d} t$；$E_r=E_f-\sum b_i^2$；完备时：$E_f=\sum b_i^2$。

</li>

<li>

传输线方程：$\partial_su=-(R'+L'\partial_t)i$，$\partial_si=-(G'+C'\partial_t)u$。

</li>

<li>

相量（$\omega=2\pi f$）：$\underline U=\underline U_1\mathrm{e}^{-\gamma s}+\underline U_2\mathrm{e}^{\gamma s}$；$\gamma=\sqrt{(R'+\mathrm{j}\omega L')(G'+\mathrm{j}\omega C')}=\alpha+\mathrm{j}\beta$；$Z=\sqrt{\frac{R'+\mathrm{j}\omega L'}{G'+\mathrm{j}\omega C'}}$。

</li>

<li>

以 $Z$ 作终端负载：无反射；$r=\frac{R_\mathrm E-Z}{R_\mathrm E+Z}$。

</li>

<li>

无损：$Z=\sqrt{L'/C'}$，$v=1/\sqrt{L'C'}$，$u=u_\mathrm{fw}(s-vt)+u_\mathrm{bw}(s+vt)$。

</li>

</ul>
:::
