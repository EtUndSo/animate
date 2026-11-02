---
title: 概览: 拉普拉斯变换
kurz: 概览
pfad: 电气工程 / 第 3 学期 / 信号与系统 / 拉普拉斯变换
order: 3220100
summary: 每个信号都是 $\ee^{pt}$ 的叠加， 以及为什么 LTI 系统的作用因此变成乘法
tags: 
lang: zh
---

## 本章内容

:::frage 从代入特征函数的卷积积分得到 $H(p)$ 的这段计算，我已经理解了。但我觉得拉普拉斯变换背后远不止这条计算规则：任意函数都可以写成复指数函数之和。
这个猜想抓住了问题的核心。没有它，特征函数的那段计算只不过是个奇特的结论，因为它本身只对 $\mathrm{e}^{pt}$ 这一个信号成立。正是因为（几乎）每个信号都能由这样的基本分量（构件）组合而成，它才能对*每个*输入信号给出结论。以下三点细化使这个猜想变得精确：

<ol>

<li>

一般来说，它不是求和，而是*积分*：无穷多个基本分量 $\mathrm{e}^{pt}$，每个都带有无穷小的权重。这些基本分量位于 $p$ 平面中的一条竖直线 $\operatorname{Re} p=\sigma$ 上（第 [2](ein-signal-aus-lauter-bausteinen.html#stufe-2) 阶段）。

</li>

<li>

并非任意函数都可以，而是存在收敛域的函数：它在时间轴每一侧至多按指数增长，并且必须有同一个衰减因子能同时抑制两侧（第 [2.3](konvergenzbereich-welche-dampfungen-funktionieren.html#stufe-2-3) 节）。

</li>

<li>

若 $S(p)$ 是多项式之比，积分确实会变成*有限和* $\sum_r A_r\,\mathrm{e}^{p_r t}$。指数 $p_r$ 就是 $S(p)$ 的极点（第 [4](aus-dem-integral-wird-eine-summe.html#stufe-4) 阶段）。

</li>

</ol>
:::


**所有结果背后的同一个原理。** 关于拉普拉斯变换的几乎每一个结果都由这三句话推出。下表给出每个结果的来源，各阶段对其加以解释。

| 结果 | 来源 |
|---|---|
| 特征函数 $\mathrm{e}^{pt}$，传递函数 $H(p)$ | 平移 $\mathrm{e}^{pt}$ 就是乘以 $\mathrm{e}^{-p\tau}$（第 [1](warum-gerade.html#stufe-1) 阶段） |
| 拉普拉斯变换 $S(p)$ | 基本分量 $\mathrm{e}^{pt}$ 在信号中的权重（第 [2](ein-signal-aus-lauter-bausteinen.html#stufe-2) 阶段） |
| 收敛域 | 使 $s(t)\mathrm{e}^{-\sigma t}$ 绝对可积的所有衰减率 $\sigma$（第 [2.3](konvergenzbereich-welche-dampfungen-funktionieren.html#stufe-2-3) 节） |
| 卷积 $\to$ 乘积，级联 | 每个基本分量都乘以 $H(p)$（第 [3](aus-der-faltung-wird-eine-multiplikation.html#stufe-3) 阶段） |
| 求导 $\to p$，积分 $\to 1/p$ | $\frac{\mathrm{d}}{\mathrm{d} t}\mathrm{e}^{pt}=p\,\mathrm{e}^{pt}$ 和 $\int_{-\infty}^t\mathrm{e}^{p\tau}\mathrm{d}\tau=\mathrm{e}^{pt}/p$（第 [3](aus-der-faltung-wird-eine-multiplikation.html#stufe-3) 阶段） |
| 微分方程 $\to$ 多项式之比 | 每次求导变成一个因子 $p$（第 [3](aus-der-faltung-wird-eine-multiplikation.html#stufe-3) 阶段） |
| 极点，部分分式 | 有限个基本分量的指数和权重（第 [4](aus-dem-integral-wird-eine-summe.html#stufe-4) 阶段） |
| 稳定性 | 因果基本分量 $\mathrm{e}^{p_r t}$ 仅当 $\operatorname{Re} p_r<0$ 时才衰减（第 [4](aus-dem-integral-wird-eine-summe.html#stufe-4) 阶段） |
| 傅里叶变换 | 直线 $\sigma=0$ 上的同一种叠加（第 [2](ein-signal-aus-lauter-bausteinen.html#stufe-2) 阶段） |

**如何使用本章。**每个阶段都是一篇简短的文章，包括基本思路、可展开解答的典型问题以及练习（★ 到 ★★★）。请先自己尝试，解答可在每道练习下方展开。完成一个阶段后再进入下一个。

:::merke 本章的参考模型
所有例子都使用同样的两个要素：

<ul>

<li>

一个 $RC=1$ s 的 **RC 低通滤波器**（例如 $R=1\,\mathrm{M\Omega}$，$C=1\,\mu\text{F}$）。它的冲激响应和传递函数为

$$h(t)=\frac{1}{RC}\,\mathrm{e}^{-t/RC}\varepsilon(t)=\mathrm{e}^{-t}\varepsilon(t),\qquad H(p)=\frac{1}{1+pRC}=\frac{1}{p+1},\quad \operatorname{Re} p>-1,$$

其中 $t$ 的单位为 s，$p$ 的单位为 $1/\mathrm{s}$；

</li>

<li>

⁠**单位阶跃** $s(t)=\varepsilon(t)$，其 $S(p)=1/p$，$\operatorname{Re} p>0$。

</li>

</ul>

脚本 `rechnung_kap2.py` 可重新计算文中的数值和曲线。
:::
