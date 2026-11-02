---
title: 要点
pfad: 电气工程 / 第 1 学期 / 电气工程基础 / 功率、匹配与效率
order: 1170900
summary: 为什么在功率最大时有一半能量留在电源中
tags: 焦耳热, 功率匹配, 效率, 电压匹配, 电流匹配
lang: zh
---

:::merke 三句话的答案
<ol>

<li>

电压是单位电荷的能量，电流是单位时间的电荷。两者的乘积是单位时间的能量：$p=u\,i$。

</li>

<li>

在电阻中，电场使电子加速，每次碰撞都把获得的能量交给原子晶格。因此，那里的全部功率都变成热，即__焦耳热__，$P=R\,I^2$。

</li>

<li>

内阻为 $R_\mathrm{i}$ 的电源向负载 $R_\mathrm{L}=R_\mathrm{i}$ 输出的功率最大，这称为__功率匹配__。此时每份电荷的能量在电源和负载之间平分，__效率__（功率中被利用的比例）为 50 %。固定的电压由__电压匹配__（负载远大于电源内阻）提供，固定的电流由__电流匹配__（负载远小于电源内阻）提供。

</li>

</ol>
:::

:::kern 要点
<ul>

<li>

功率是每库仑的能量乘以每秒的库仑数：$p=u\,i$。能量是它对时间的积分。

</li>

<li>

在电阻中，碰撞把一切都交给晶格：$P=R\,I^2=U^2/R$，受 $P_\mathrm{max}$ 限制。

</li>

<li>

正弦电压下，电阻上的 $P=\frac12\hat u^2/R=\frac12\hat\imath^2R$。

</li>

<li>

相同功率下，电压提高到 $n$ 倍，线路损耗降到 $1/n^2$。

</li>

<li>

平衡：$P_\mathrm{q}=P_\mathrm{v}+P_\mathrm{L}$。效率：$\eta=U_\mathrm{L}/U_\mathrm{q}=R_\mathrm{L}/(R_\mathrm{L}+R_\mathrm{i})$。

</li>

<li>

最大功率在 $R_\mathrm{L}=R_\mathrm{i}$ 时：$P_\mathrm{L,max}=U_\mathrm{q}^2/(4R_\mathrm{i})$，此时 $\eta=\frac12$，因为电流和效率线性地此消彼长。

</li>

<li>

电力工程要求 $R_\mathrm{L}\gg R_\mathrm{i}$，信号传输要求 $R_\mathrm{L}=R_\mathrm{i}$。等效电源能正确给出最大值，但不能正确给出效率。

</li>

</ul>
:::
