---
title: 第 6 阶段：联合分布、独立与不相关
pfad: 电气工程 / 第 3 学期 / ET3 – 电气工程基础 3：信号与系统 / 随机信号
adresse: elektrotechnik/3-semester/signale-und-systeme/zufallssignale
knoten: 第 7 章：随机信号
order: 3270700
summary: 同时考虑两个随机变量：它们何时相互关联？对它们的和又能得出什么？
tags: 联合分布, 统计独立, 不相关
lang: zh
---

<span class="anker" id="stufe-6"></span>

:::zweck
同时考虑两个随机变量：它们何时相互关联？对它们的和又能得出什么？
:::

两个变量的__联合分布__为 $P_{sg}(x,y)=\mathrm{Prob}[s\le x\ \text{且}\ g\le y]$，其密度（联合概率密度）为 $p_{sg}=\frac{\partial^2P_{sg}}{\partial x\,\partial y}$。由它可以得到每个变量各自的分布（$P_{sg}(x,\infty)=P_s(x)$）以及相关 $\varphi_{sg}=\iint xy\,p_{sg}(x,y)\,\mathrm{d} x\,\mathrm{d} y$。对于联合平稳的过程，一切都只取决于 $s(t)$ 与 $g(t+\tau)$ 之间的时移 $\tau$。

:::definition 定义 6.1 (独立，不相关)
<span class="anker" id="satz-6-1"></span>

若 $p_{sg}(x,y)=p_s(x)\,p_g(y)$，则称 $s$ 和 $g$ __统计独立__。若 $\mu_{sg}=\varphi_{sg}-m_sm_g=0$，则称它们__不相关__。
:::

由独立可以推出不相关：$\varphi_{sg}=\int xp_s\mathrm{d} x\cdot\int yp_g\mathrm{d} y=m_sm_g$。反之则不成立：不相关只意味着不存在*线性*关系（练习 [5](#aufg-5)）。

**两个独立变量之和。** 只要 $f=u$ 且 $g=x-u$（$u$ 任意），和 $s=f+g$ 就取值 $x$：

<span class="anker" id="gl-6-1"></span>
$$p_s(x)=\int_{-\infty}^{\infty}p_{fg}(u,x-u)\,\mathrm{d} u=p_f(x)*p_g(x)\quad(\text{独立}). \tag{6.1}$$

这就是[第 1 章](/wissen/zh/elektrotechnik/3-semester/signale-und-systeme/lti-systeme-und-faltung/lti-systeme-und-faltung.html)中的卷积，它在那里出现于掷骰子的例子中。两个均匀分布变量之和具有三角形概率密度，三个变量之和的概率密度已近似呈钟形（图 [2](#abb-2)）。

:::abbildung et3/k7summen 2
独立随机变量之和的概率密度函数，每个变量都在 $[-\frac12,\frac12]$ 上均匀分布。仅仅三个变量之和，就已接近具有相同方差的高斯曲线（在 $x=0$ 处：0.75 对 0.80）。
:::

:::aufgabe 练习 5 ★★ 不相关，却不独立
<span class="anker" id="aufg-5"></span>

$s$ 在 $[-1,1]$ 上均匀分布，$g=s^2$。证明 $s$ 与 $g$ 不相关，尽管 $g$ 完全由 $s$ 决定。

:::loesung
$m_s=0$，且 $\mathrm E\{sg\}=\mathrm E\{s^3\}=\frac12\int_{-1}^1x^3\mathrm{d} x=0$，因此 $\mu_{sg}=0-0\cdot m_g=0$：不相关。尽管如此，$s$ 决定了 $g$ 的值。这种关系是二次的，而相关只能反映线性关系：对正的 $s$，$g$ 随 $s$ 增大而增大；对负的 $s$，$g$ 随 $s$ 增大而减小；平均起来，这两种趋势相互抵消。
:::
:::
