---
title: 要点
pfad: 电气工程 / 第 3 学期 / ET3 – 电气工程基础 3：信号与系统 / 正交展开与传输线
adresse: elektrotechnik/3-semester/signale-und-systeme/orthogonalentwicklung-und-leitungen
knoten: 第 8 章：正交展开与传输线
order: 3280600
summary: 两个补充专题：作为向量的信号， 电传输线上的波
tags: 
lang: zh
---

:::merke 三句话的答案
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
