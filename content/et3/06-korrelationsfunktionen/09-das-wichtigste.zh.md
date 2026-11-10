---
title: 要点
pfad: 电气工程 / 第 3 学期 / ET3 – 电气工程基础 3：信号与系统 / 相关函数
adresse: elektrotechnik/3-semester/signale-und-systeme/korrelationsfunktionen
knoten: 第 6 章：相关函数
order: 3260900
summary: 两个信号有多相似？ 能量又如何分布在各个频率上？
tags: 
lang: zh
---

:::merke 三句话的答案
<ol>

<li>

两个信号的相似程度用它们乘积的积分来度量。相关函数对每个时移 $\tau$ 都这样做；它是与反转信号的卷积。

</li>

<li>

自相关函数的傅里叶变换是能量谱密度 $|S(f)|^2$。自相关函数在 $\tau=0$ 处的值就是能量（帕塞瓦尔定理）。

</li>

<li>

LTI 系统把能量谱密度乘以 $|H(f)|^2$，并把自相关函数与 $h$ 的自相关函数做卷积。

</li>

</ol>
:::

:::kern 要点
<ul>

<li>

$E_s=\int|s|^2\mathrm{d} t$；$L_s=\lim\frac{1}{2T}\int_{-T}^T|s|^2\mathrm{d} t$。

</li>

<li>

$p_{sg}=\frac{\int s^*g\,\mathrm{d} t}{\sqrt{E_sE_g}}$，$|p|\le1$，$p=0$：正交。

</li>

<li>

$\varphi^E_{sg}(\tau)=\int s^*(t)g(t+\tau)\mathrm{d} t=s^*(-\tau)*g(\tau)$；$\varphi^E_{gs}(\tau)=\varphi^{E*}_{sg}(-\tau)$。

</li>

<li>

自相关函数：偶函数（对实信号），最大值 $\varphi^E_{ss}(0)=E_s$，持续时间加倍。

</li>

<li>

$\varphi^E_{ss}\leftrightarrow|S|^2$，$\varphi^E_{sg}\leftrightarrow S^*G$；帕塞瓦尔定理 $\int|s|^2\mathrm{d} t=\int|S|^2\mathrm{d} f$。

</li>

<li>

维纳–李关系：$\varphi^E_{gg}=\varphi^E_{ss}*\varphi^E_{hh}$，$|G|^2=|S|^2|H|^2$；$\varphi^E_{sg}=\varphi^E_{ss}*h$。

</li>

<li>

带通：$\varphi^E_{sgT}=\frac12s_T^*(-\tau)*g_T(\tau)$。

</li>

<li>

离散：$\varphi(m)=\sum s^*(n)g(n+m)$，$\leftrightarrow|S_\mathrm a|^2$；周期：$S_d^*G_d$。

</li>

</ul>
:::
