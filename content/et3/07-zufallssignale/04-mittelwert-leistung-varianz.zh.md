---
title: 第 3 阶段：均值、功率、方差
pfad: 电气工程 / 第 3 学期 / 信号与系统 / 随机信号
order: 3270400
summary: 最重要的一阶平均值及其直观含义。
tags: 直流分量, 功率, 方差, 交流功率, 标准差
lang: zh
---

<span class="anker" id="stufe-3"></span>

:::zweck
最重要的一阶平均值及其直观含义。
:::

数学期望是线性的：对任意随机变量，$\mathrm E\{\sum_ia_is_i\}=\sum_ia_i\mathrm E\{s_i\}$。对平稳过程定义：

<span class="anker" id="gl-3-1"></span>
$$m_s=\mathrm E\{s(t)\},\qquad L_s=\mathrm E\{s^2(t)\},\qquad\sigma_s^2=L_s-m_s^2. \tag{3.1}$$

⁠**如何理解：**对各态历经过程，$m_s$ 就是时间平均，即信号的__直流分量__；$L_s$ 是平方的时间平均，即__功率__（[第 6 部分](/wissen/zh/elektrotechnik/3-semester/signale-und-systeme/korrelationsfunktionen/korrelationsfunktionen.html)）。__方差__ $\sigma_s^2$ 等于功率减去直流分量的功率，也就是__交流功率__。它的平方根，即__标准差__ $\sigma_s$，是交流分量的有效值。万用表拨到 AC 挡时显示 $\sigma_s$，拨到 DC 挡时显示 $m_s$。

:::aufgabe 练习 1 ★ 信号的平均值
<span class="anker" id="aufg-1"></span>

一个各态历经信号的直流分量为 2 V，有效值（包括所有分量，即“真有效值”）为 2.5 V。归一化功率、方差和标准差各是多少？

:::loesung
$L_s=2.5^2=6.25$ V$^2$，$\sigma_s^2=L_s-m_s^2=6.25-4=2.25$ V$^2$，$\sigma_s=1.5$ V。拨到 AC 挡的仪表显示 1.5 V。
:::
:::
