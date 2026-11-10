---
title: 第 1 阶段：能量与功率
pfad: 电气工程 / 第 3 学期 / ET3 – 电气工程基础 3：信号与系统 / 相关函数
adresse: elektrotechnik/3-semester/signale-und-systeme/korrelationsfunktionen
knoten: 第 6 章：相关函数
order: 3260200
summary: 在比较信号之前，需要一个度量信号“大小”的量。在系统理论中，这个量就是能量；对于无限长的信号，则是功率。
tags: 信号能量, 能量信号, 功率, 功率信号
lang: zh
---

<span class="anker" id="stufe-1"></span>

:::zweck
在比较信号之前，需要一个度量信号“大小”的量。在系统理论中，这个量就是能量；对于无限长的信号，则是功率。
:::

在电阻 $R$ 上，从 $t_1$ 到 $t_2$ 这段时间内有能量 $\frac1R\int u^2\mathrm{d} t$ 转化为热。去掉因子 $1/R$，这个表达式就称为__信号能量__：

<span class="anker" id="gl-1-1"></span>
$$E_s=\int_{-\infty}^{\infty}|s(t)|^2\,\mathrm{d} t. \tag{1.1}$$

若它有限，则称 $s$ 为__能量信号__（例如任何脉冲）。若信号无限长地持续下去而不衰减（余弦、阶跃），它的能量就是无穷大。这时改为度量平均__功率__：

<span class="anker" id="gl-1-2"></span>
$$L_s=\lim_{T\to\infty}\frac{1}{2T}\int_{-T}^{T}|s(t)|^2\,\mathrm{d} t. \tag{1.2}$$

若它有限，则称 $s$ 为__功率信号__。对于周期信号，在一个周期上取平均就足够了。对于狄拉克冲激，能量和功率都没有定义（$\delta^2$ 不存在）。

:::aufgabe 练习 1 ★ 能量还是功率？
<span class="anker" id="aufg-1"></span>

求下列信号的能量或功率：(a) $a\operatorname{rect}(t/T)$，(b) $\varepsilon(t)\mathrm{e}^{-t}$，(c) $A\cos(2\pi Ft)$，(d) $\varepsilon(t)$。

:::loesung
(a) $E=a^2|T|$。(b) $E=\int_0^\infty\mathrm{e}^{-2t}\mathrm{d} t=\frac12$。(c) 能量无穷大，功率为 $\frac{A^2}{2}$（$\cos^2$ 的平均值为 $\frac12$）。(d) 能量无穷大，功率为 $\lim\frac{1}{2T}\int_0^T1\,\mathrm{d} t=\frac12$：信号在一半的时间里为 1。
:::
:::
