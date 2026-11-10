---
title: 要点
pfad: 电气工程 / 第 1 学期 / ET1 – 电气工程基础 1：电路分析导论 / 运算放大器
adresse: elektrotechnik/1-semester/grundlagen-der-elektrotechnik/der-operationsverstarker
knoten: 第 11 章：运算放大器
order: 1211300
summary: 一个巨大而不精确的倍数，如何变成 行为只由电阻决定的器件
tags: 差分放大器, 环路增益, 虚地
lang: zh
---

:::merke 三句话的答案
<ol>

<li>

内部是一个__差分放大器__，即只对两个电压之差作出反应的电路：$U_\mathrm{A}=A\,U_\mathrm{D}$，其中 $U_\mathrm{D}=\varphi_+-\varphi_-$。当 $A=100000$、输出最高 11 V 时，留给 $U_\mathrm{D}$ 的窗口只有 $\pm110$ µ V。

</li>

<li>

负反馈把输出的比例 $\beta$ 送到负输入端。输出不断变化，直到环路静止下来，这时 $U_\mathrm{D}$ 刚好够维持输出：5 V 需要 50 µ V。增益变为 $G\approx1/\beta$，__环路增益__ $A\beta$（沿环路走一圈的倍数）只决定那一点小偏差。

</li>

<li>

由此得到一条规则：两个输入端电位相等，没有电流流入，在负输入端列节点定律。它解释了__虚地__（一个处于 0 V 却没有连到接地点的节点）和所有基本电路。它在以下情况失效：输出到达极限、反馈改变符号、$A\beta$ 变小。

</li>

</ol>
:::

:::kern 要点
<ul>

<li>

噪声：$u_\mathrm{r,eff}=\sqrt{\int|u_\mathrm{r}(f)|^2\mathrm{d} f}$，热噪声 $|u_\mathrm{r,R}|^2=4k_\mathrm{B}TR$。放大不改变 SNR，只对后来的干扰有帮助。$\mathrm{SNR}_\mathrm{dB}=20\lg(u_\mathrm{s}/u_\mathrm{r})$。

</li>

<li>

差分放大器：总电流固定，$U_\mathrm{A}=S\,R_\mathrm{C}\,U_\mathrm{D}$，每个 BE 结承担 $U_\mathrm{D}/2$，共模不起作用。

</li>

<li>

模型：$U_\mathrm{A}=A(\varphi_+-\varphi_-)$，直到极限。窗口 $\pm110$ µ V，没有反馈时是比较器。

</li>

<li>

负反馈：$U_\mathrm{D}=U_\mathrm{E}/(1+A\beta)$，$G=\frac1\beta\cdot\frac1{1+1/(A\beta)}$，$\Delta G/G=\frac{1}{1+A\beta}\Delta A/A$。输出不断变化，直到环路静止。5 V 时剩下 50 µ V。

</li>

<li>

规则：$\varphi_+=\varphi_-$，$I_\pm=0$，在负输入端列节点定律，最后检查极限。虚地：靠调节维持 0 V，没有通往接地点的路径。电流经反馈流入输出端。

</li>

<li>

$G=-R_2/R_1$，$G=1+R_2/R_1$，$U_\mathrm{A}=-R_\mathrm{F}\sum U_{\mathrm{E}i}/R_{\mathrm{E}i}$，$U_\mathrm{A}=\frac{R_2}{R_1}(U_\mathrm{E2}-U_\mathrm{E1})$，积分器 $-\frac{1}{RC}\int u_\mathrm{E}\mathrm{d} t$，微分器 $-RC\,\mathrm{d} u_\mathrm{E}/\mathrm{d} t$，对数放大器 $-U_T\ln(U_\mathrm{E}/RI_\mathrm{S})$，指数放大器 $-RI_\mathrm{S}\mathrm{e}^{U_\mathrm{E}/U_T}$，跨阻放大器 $-R\,I_\mathrm{E}$，NIC $R_\mathrm{in}=-R_2$。

</li>

<li>

正反馈：结果加强原因，输出位于极限，阈值 $\beta\,U_\mathrm{A,max}$ 和 $\beta\,U_\mathrm{A,min}$。

</li>

<li>

界限：过驱动，$U_\mathrm{off}/\beta$，$I_\mathrm{B}R_2$，CMRR，$G\,f_G=f_\mathrm{T}$。

</li>

</ul>
:::
