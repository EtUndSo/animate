---
title: 第 3 阶段：空间电荷区
pfad: 电气工程 / 第 1 学期 / 电气工程基础 / 半导体与二极管
order: 1190500
summary: 一块 n 型和一块 p 型材料各自只是电阻。本阶段说明它们的交界处会形成什么，以及它为什么是势垒。
tags: 扩散, 空间电荷, 漂移, 内建电压
lang: zh
---

<span class="anker" id="stufe-3"></span>

:::zweck
一块 n 型和一块 p 型材料各自只是电阻。本阶段说明它们的交界处会形成什么，以及它为什么是势垒。
:::

**基本思路。** 在一块晶体中，p 区与 n 区相邻。发生四个步骤（图 [4](#abb-4)）：

<ol>

<li>

⁠**扩散。**载流子作无规则运动。从高密度区域出去的比进来的多。这种由随机运动造成的均衡称为__扩散__。电子从 n 区移向 p 区，空穴相反。

</li>

<li>

⁠**复合。**这些载流子在对方区域遇到那里的多数载流子而消失。此后交界附近几乎没有自由载流子。

</li>

<li>

⁠**留下固定离子。**那里的离子不再被抵消：n 侧是 $\mathrm P^+$，p 侧是 $\mathrm B^-$。这种固定电荷称为__空间电荷__，这一层称为空间电荷区。

</li>

<li>

⁠**电场阻止均衡。**离子产生从 n 侧指向 p 侧的电场。它把电子推回 n 区，把空穴推回 p 区（__漂移__，[第 2 部分](/wissen/zh/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/strom-widerstand-und-kirchhoff/strom-widerstand-und-kirchhoff.html)）。这个区不断扩大，直到漂移电流恰好抵消扩散电流。

</li>

</ol>

:::abbildung et1/k9rlz 4
无外加电压的 pn 结。上：方块是固定离子，实心圆是电子，空心圆是空穴。该区内没有可移动载流子，电场 $E$ 指向 p 侧。下：电位只在该区内上升，总共升高 $U_\mathrm{D0}=0.71$ V。这个电位台阶阻碍电子向 p 侧运动。
:::

:::satz 定理 3.1 (内建电压与区宽)
<span class="anker" id="satz-3-1"></span>

对于突变结，用热电压 $U_T=k_\mathrm BT/e$ 表示，有

<span class="anker" id="gl-3-1"></span>
$$U_\mathrm{D0}=U_T\ln\frac{N_\mathrm AN_\mathrm D}{n_\mathrm i^2},\qquad w=\sqrt{\frac{2\varepsilon}{e}\Bigl(\frac1{N_\mathrm A}+\frac1{N_\mathrm D}\Bigr)U_\mathrm{D0}},\qquad E_\mathrm{max}=\frac{2U_\mathrm{D0}}{w}. \tag{3.1}$$
:::

⁠**如何理解：**$U_\mathrm{D0}$ 是__内建电压__，即两个区域之间的电位台阶，硅的典型值约为 0.7 到 0.9 V。电子在向 p 侧运动时遇到能量势垒 $W_\mathrm B=e\,U_\mathrm{D0}$。$w$ 是该区的宽度，$\varepsilon=\varepsilon_0\varepsilon_\mathrm r=1.04\cdot10^{-10}$ A s/(V m) 是介电常数（[第 3 部分](/wissen/zh/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/der-kondensator/der-kondensator.html)）。该区更深地伸入掺杂较轻的一侧：$w_\mathrm n/w_\mathrm p=N_\mathrm A/N_\mathrm D$。**适用条件：**平衡状态；式 [(3.1)](#gl-3-1) 中的密度以 1/m$^3$ 为单位代入。

:::herleitung 电位台阶与宽度
⁠**电位台阶。**p 侧的电子已经爬过势垒。由式 [(0.1)](von-grund-auf-ventil-wechselspannung-und-warmeenergie.html#gl-0-1)，密度满足 $n_\mathrm p/n_\mathrm n=\mathrm{e}^{-U_\mathrm{D0}/U_T}$。用 $n_\mathrm n=N_\mathrm D$ 和由式 [(2.1)](dotierung.html#gl-2-1) 得到的 $n_\mathrm p=n_\mathrm i^2/N_\mathrm A$，即得第一个方程。

⁠**宽度。**两侧所带电荷量相同，所以 $N_\mathrm Aw_\mathrm p=N_\mathrm Dw_\mathrm n$。电场从边缘向交界线性增长，在交界处达到面电荷的场强值（[第 3 部分](/wissen/zh/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/der-kondensator/der-kondensator.html)），$E_\mathrm{max}=e\,N_\mathrm Dw_\mathrm n/\varepsilon$。电压是场强曲线下的面积，即一个三角形：$U_\mathrm{D0}=\tfrac12E_\mathrm{max}w$。结合 $w=w_\mathrm n+w_\mathrm p$ 得式 [(3.1)](#gl-3-1)。
:::

::::beispiel
$U_\mathrm{D0}=25.85\,\mathrm{mV}\cdot\ln10^{12}=0.714$ V，即 $27.6\,U_T$。因此势垒只让比例 $\mathrm{e}^{-27.6}=10^{-12}$ 通过，恰好等于密度之比 $10^{4}/10^{16}$。此外，$w=0.43$ µ m，两个区域各占一半，$E_\mathrm{max}=3.3$ MV/m，相当于空气的击穿场强（[第 1 部分](/wissen/zh/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/ladung-feld-und-potenzial/ladung-feld-und-potenzial.html)）。
::::

⁠**极限情况：**若一侧掺杂重得多，该区几乎全部位于另一侧。一侧掺杂增加到十倍，$U_\mathrm{D0}$ 只升高 60 mV。

:::frage 二极管内部有 0.71 V。为什么测量它时得到 0 V，为什么它不驱动电流？
这个电位台阶是真实存在的，但它不是回路中唯一的台阶。金属触点与半导体相接处还会产生其他接触电压。沿任何闭合回路，它们的总和为零，因为平衡时没有能量来源。这个台阶只是建立起扩散与漂移之间的平衡。
:::

:::aufgabe 练习 3 ★★ 单边结
<span class="anker" id="aufg-3"></span>

一个 pn 结的 $N_\mathrm A=10^{18}\,\mathrm{cm^{-3}}$，$N_\mathrm D=10^{15}\,\mathrm{cm^{-3}}$。

<ol class="al">

<li>

计算 $U_\mathrm{D0}$、$w$ 和 $E_\mathrm{max}$。

</li>

<li>

该区在每一侧有多宽？为什么它几乎全部位于轻掺杂区？

</li>

</ol>

:::loesung
(a) $U_\mathrm{D0}=25.85\,\mathrm{mV}\cdot\ln(10^{33}/10^{20})=0.774$ V。由于 $1/N_\mathrm A$ 相对于 $1/N_\mathrm D$ 可以忽略，$w=\sqrt{2\varepsilon U_\mathrm{D0}/(e\,N_\mathrm D)}=1.00$ µ m，$E_\mathrm{max}=2U_\mathrm{D0}/w=1.55$ MV/m。 (b) $w_\mathrm n/w_\mathrm p=1000$，所以 $w_\mathrm n=1.00$ µ m，$w_\mathrm p=1.0$ nm。两侧必须提供相同的离子电荷。轻掺杂区的离子稀疏一千倍，因此需要一千倍的深度。
:::
:::
