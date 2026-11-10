---
title: 要点
pfad: 电气工程 / 第 1 学期 / ET1 – 电气工程基础 1：电路分析导论 / 半导体与二极管
adresse: elektrotechnik/1-semester/grundlagen-der-elektrotechnik/halbleiter-und-dioden
knoten: 第 9 章：半导体与二极管
order: 1191200
summary: 硅如何变成电流的阀门， 以及如何用它进行计算
tags: 
lang: zh
---

:::merke 三句话的答案
<ol>

<li>

在 pn 结处，可移动的电荷进入另一区域，留下固定的离子。这些离子的电场在空间电荷区内建立起势垒，使这种均衡过程停止。

</li>

<li>

热只能把比例为 $\mathrm{e}^{-W/(k_\mathrm BT)}$ 的载流子抬过高度为 $W$ 的势垒。正向电压降低势垒，因此电流按指数增长，每 60 mV 增大 10 倍：$I=I_\mathrm S(\mathrm{e}^{U/U_T}-1)$。在反向只剩下极小的电流 $-I_\mathrm S$。

</li>

<li>

在电路中，工作点位于特性曲线与负载线（由电源和电阻决定的直线）的交点。手算时，二极管变成一个具有固定正向电压的开关；对于工作点附近的微小变化，它变成电阻 $r=U_T/I$。

</li>

</ol>
:::

:::kern 要点
<ul>

<li>

能带：$W_\mathrm g$（硅 1.12 eV），比例 $\mathrm{e}^{-W/(k_\mathrm BT)}$；载流子是导带中的电子和价带中的空穴。

</li>

<li>

掺杂：施主给出 $n\approx N_\mathrm D$，受主给出 $p\approx N_\mathrm A$，处处 $n\,p=n_\mathrm i^2$。晶体保持中性。

</li>

<li>

pn 结：扩散、复合、固定离子、电场。$U_\mathrm{D0}=U_T\ln(N_\mathrm AN_\mathrm D/n_\mathrm i^2)$。

</li>

<li>

特性曲线：$I=I_\mathrm S(\mathrm{e}^{U/U_T}-1)$，$U_T=k_\mathrm BT/e=25.85$ mV（300 K），每十倍程 60 mV，没有阈值。

</li>

<li>

只要热量受到限制，击穿就是可逆的。齐纳二极管：$U_\mathrm Z$，$r_\mathrm Z$。变容二极管：$C_\mathrm{j}=\varepsilon A/w$。光电二极管：$I=I_\mathrm S(\mathrm{e}^{U/U_T}-1)-I_\mathrm{Ph}$，太阳能电池 $U_\mathrm L=U_T\ln(I_\mathrm{Ph}/I_\mathrm S+1)$。

</li>

<li>

工作点：特性曲线与负载线 $I=(U_0-U_\mathrm D)/R$ 的交点；通过 $U_\mathrm D=U_T\ln(I/I_\mathrm S+1)$ 迭代。

</li>

<li>

模型：导通时 $U_\mathrm D=0$ 或 $U_\mathrm F$，截止时 $I_\mathrm D=0$。假设、计算、检验：$I_\mathrm D>0$ 且 $U_\mathrm D<U_\mathrm F$。

</li>

<li>

小信号：$r=U_T/I$，条件是 $|u_\mathrm D|\ll U_T$。不要与 $U_\mathrm D/I$ 混淆。

</li>

<li>

电桥：峰值 $\hat u-2U_\mathrm F$，间隙在 $|u_\mathrm e|<2U_\mathrm F$ 时出现。电荷泵：$U_\mathrm a\to2U_\mathrm e-2U_\mathrm F$。

</li>

</ul>
:::
