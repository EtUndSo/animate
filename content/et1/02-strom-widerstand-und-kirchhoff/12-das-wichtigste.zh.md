---
title: 要点
pfad: 电气工程 / 第 1 学期 / ET1 – 电气工程基础 1：电路分析导论 / 电流、电阻与基尔霍夫定律
adresse: elektrotechnik/1-semester/grundlagen-der-elektrotechnik/strom-widerstand-und-kirchhoff
knoten: 第 2 章：电流、电阻与基尔霍夫定律
order: 1121200
summary: 为什么电子缓慢爬行，电流却立刻出现， 以及为什么电路网络服从守恒定律
tags: 漂移速度, 电流密度, 分压器
lang: zh
---

:::merke 三句话的答案
<ol>

<li>

导体中的电场使自由电子加速，碰撞又使它们失去获得的速度。剩下的是一个很小的、与电场成正比的__漂移速度__（沿导体的平均速度）。因此，__电流密度__（单位横截面积上的电流）与电场成正比，对元件就得到 $U=R\,I$。

</li>

<li>

节点定律就是电荷守恒，网孔定律就是能量守恒。

</li>

<li>

三条定律合起来，为每个网络提供的方程数恰好等于未知量的个数。串联时电压被分配（__分压器__：两个电阻，其比值决定分电压），并联时电流被分配。

</li>

</ol>
:::

:::kern 要点
<ul>

<li>

电流：$i=\mathrm{d} Q/\mathrm{d} t$，$I=q\,v\,A$；电流密度 $\vec j=q\,\vec v$。

</li>

<li>

漂移：$\vec v_\mathrm D=-\mu\,\vec E$，$v_\mathrm D=I/(n\,e\,A)$；电流立刻出现，因为传播的是电场。

</li>

<li>

材料：$\vec j=\sigma\,\vec E$，$\sigma=n\,e\,\mu=1/\rho$。

</li>

<li>

元件：$U=R\,I$，$R=\rho\,L/A$，$G=1/R$；功率 $P=U\,I$。

</li>

<li>

E 系列：$w=(\sqrt[N]{10})^i$；温度：$R(\vartheta)=R(\vartheta_0)(1+\alpha\,(\vartheta-\vartheta_0))$；PTC、NTC。

</li>

<li>

二端元件：特性曲线 $I=f(U)$；负载惯例同向，发电机惯例反向；电子逆着习惯电流方向运动。

</li>

<li>

网络：$k$ 个节点，$z$ 条支路，$m=z-k+1$ 个独立网孔；树由 $k-1$ 条支路组成。

</li>

<li>

节点定律：$\sum I=0$，$k-1$ 个方程；网孔定律：$\sum U=0$，$z-k+1$ 个方程。

</li>

<li>

串联：$R_\mathrm{tot}=\sum R_i$，$U_\nu/U=R_\nu/\sum R_i$，仅限空载。

</li>

<li>

并联：$G_\mathrm{tot}=\sum G_i$，$R_1\parallel R_2=R_1R_2/(R_1+R_2)$，$I_1=I_\mathrm{tot}\,R_2/(R_1+R_2)$。

</li>

<li>

带负载：$U_2/U=(R_2\parallel R_\mathrm L)/(R_1+R_2\parallel R_\mathrm L)$，误差 $R_\mathrm i/(R_\mathrm i+R_\mathrm L)$。

</li>

</ul>
:::

**[第 3 章](/wissen/zh/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/der-kondensator/der-kondensator.html)预告。** 节点几乎不储存电荷。由两块大极板构成的电容器正好相反：它储存电荷和能量。
