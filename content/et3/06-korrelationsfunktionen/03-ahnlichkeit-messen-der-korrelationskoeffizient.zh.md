---
title: 第 2 阶段：度量相似程度——相关系数
pfad: 电气工程 / 第 3 学期 / 信号与系统 / 相关函数
order: 3260300
summary: 怎样用一个数来度量两个信号有多相似？办法是度量它们的差有多大。
tags: 相关系数, 正交
lang: zh
---

<span class="anker" id="stufe-2"></span>

:::zweck
怎样用一个数来度量两个信号有多相似？办法是度量它们的差有多大。
:::

**思路。** 两个信号相似时，差信号 $\Delta(t)=s(t)-g(t)$ 的能量就小。展开得：

$$E_\Delta=\int|s-g|^2\mathrm{d} t=E_s+E_g-\int s^*g\,\mathrm{d} t-\int g^*s\,\mathrm{d} t=E_s+E_g-2\operatorname{Re}\int s^*(t)g(t)\,\mathrm{d} t.$$

因此，差别完全体现在乘积的积分中。为了不让信号本身的大小计入在内，把两个信号都归一化到能量 1。于是 $E_\Delta=2-2\operatorname{Re}\,p_{sg}$，其中__相关系数__为

<span class="anker" id="gl-2-1"></span>
$$p_{sg}=\frac{\int_{-\infty}^{\infty}s^*(t)\,g(t)\,\mathrm{d} t}{\sqrt{E_sE_g}}. \tag{2.1}$$

⁠**如何理解：**$|p_{sg}|\le1$（柯西–施瓦茨不等式）。$p=1$ 表示 $s=a\,g$ 且 $a>0$：形状相同。$p=-1$ 表示 $s=-a\,g$：形状相同，符号相反。$p=0$ 表示 $\int s^*g\,\mathrm{d} t=0$；这两个信号是__正交__的，就像[第 3 部分](/wissen/zh/elektrotechnik/3-semester/signale-und-systeme/fourier-reihe-und-transformation/fourier-reihe-und-transformation.html)中傅里叶级数的各次谐波一样。例：对于 $\operatorname{rect}(t)$ 和 $\Lambda(t)$，有 $\int\operatorname{rect}\cdot\Lambda\,\mathrm{d} t=0.75$，$E_{\operatorname{rect}}=1$，$E_\Lambda=\frac23$，因此 $p=0.919$。

:::aufgabe 练习 2 ★★ 相关系数
<span class="anker" id="aufg-2"></span>

计算下列各对信号的 $p$：(a) $\operatorname{rect}(t)$ 与 $\operatorname{rect}(t-0.5)$，(b) $\operatorname{rect}(t)$ 与 $\Lambda(t)$（结果见上文），(c) $\operatorname{rect}(t)$ 与 $\operatorname{sgn}(t)\operatorname{rect}(t)$。

:::loesung
(a) 两个矩形在长度 0.5 上重叠，因此 $\int=0.5$，且两者的能量都是 1：$p=0.5$。 (b) $\int\operatorname{rect}\cdot\Lambda\,\mathrm{d} t=\int_{-1/2}^{1/2}(1-|t|)\mathrm{d} t=0.75$，$E_\Lambda=2\int_0^1(1-t)^2\mathrm{d} t=\frac23$：$p=\frac{0.75}{\sqrt{2/3}}=0.919$。形状非常相似。 (c) $\int\operatorname{sgn}(t)\operatorname{rect}^2(t)\mathrm{d} t=0$：$p=0$；这两个信号正交，尽管它们在右半部分完全相同。
:::
:::
