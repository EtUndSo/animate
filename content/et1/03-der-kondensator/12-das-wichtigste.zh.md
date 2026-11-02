---
title: 要点
pfad: 电气工程 / 第 1 学期 / 电气工程基础 / 电容器
order: 1131200
summary: 电流如何流入绝缘体 能量之后又在哪里
tags: 电场能量, 时间常数
lang: zh
---

:::merke 三句话的答案
<ol>

<li>

电容器不让电荷通过，而是使电荷移动：电子离开一块极板，同时有电子到达另一块极板，两个接线端在同一时刻流过相同的电流。

</li>

<li>

分离的电荷 $Q$ 产生极板之间的电场。这个电场决定电压 $U=Q/C$，其中含有__电场能量__ $\frac12CU^2$，储存在极板之间的空间里。

</li>

<li>

电荷的积累需要电流和时间，所以电压不会跳变。空的电容器在最初瞬间相当于短路（0 V 时有电流），充满的电容器相当于开路（有电压而无电流）。两者之间是一条指数曲线，其__时间常数__ $\tau=RC$ 给出充电的节奏。

</li>

</ol>
:::

:::kern 要点
<ul>

<li>

电容器使电荷分离：$+Q$ 和 $-Q$，总电荷为零。两个接线端的电流相同，没有电荷穿过间隙。

</li>

<li>

电容：$C=Q/U$；$i=C\,\mathrm{d} u/\mathrm{d} t$；$u(t)=u(t_0)+\frac1C\int_{t_0}^ti\,\mathrm{d} t'$。$u$ 不跳变，直流被隔断。

</li>

<li>

平行板电容器：$C=\varepsilon A/d$，其中 $\varepsilon=\varepsilon_0\varepsilon_\mathrm{r}$，$\varepsilon_0=8.854\cdot10^{-12}$ A s/(V m)。

</li>

<li>

能量：$W=\frac12CU^2=\frac12QU=Q^2/(2C)$，存在于电场中，密度为 $w=\frac12\varepsilon E^2$。

</li>

<li>

并联：$C_\mathrm{G}=\sum C_i$。串联：$1/C_\mathrm{G}=\sum1/C_i$。

</li>

<li>

孤岛：$Q_\mathrm{tot}=\sum C_iU_i=$ const。这时能量并不守恒。

</li>

<li>

充电：$u_C=U_0(1-\mathrm{e}^{-t/\tau})$，$i=\frac{U_0}{R}\mathrm{e}^{-t/\tau}$。放电：$u_C=U_0\,\mathrm{e}^{-t/\tau}$，$i=-\frac{U_0}{R}\mathrm{e}^{-t/\tau}$。时间常数 $\tau=RC$。

</li>

<li>

一般形式：$u_C(t)=u_\infty+(u_C(0)-u_\infty)\,\mathrm{e}^{-t/\tau}$。空的电容器在最初瞬间相当于短路，充满的相当于开路。

</li>

</ul>
:::
