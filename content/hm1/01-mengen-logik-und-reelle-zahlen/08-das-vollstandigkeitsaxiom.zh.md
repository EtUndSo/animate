---
title: 第 6 阶段：完备性公理
pfad: 电气工程 / 第 1 学期 / HöMa1 – 高等数学 1 / 集合、逻辑与实数
adresse: elektrotechnik/1-semester/hohere-mathematik-1/mengen-logik-und-reelle-zahlen
knoten: 第 1 章：集合、逻辑与实数
order: 1210800
summary: mathbb Q 满足到目前为止的所有公理。然而还缺少一样东西：平方等于 2 的那个数。本阶段说明这一点，并给出把 mathbb R 与 mathbb Q 区分开的公理。
tags: 有上界, 上界, 有下界, 下界, 有界, 上确界, 下确界, 最大值
lang: zh
---

<span class="anker" id="stufe-6"></span>

:::zweck
$\mathbb{Q}$ 满足到目前为止的所有公理。然而还缺少一样东西：平方等于 2 的那个数。本阶段说明这一点，并给出把 $\mathbb{R}$ 与 $\mathbb{Q}$ 区分开的公理。
:::

**基本思路。** $\mathbb{N}$ 和 $\mathbb{Z}$ 有看得见的缺口。$\mathbb{Q}$ 看起来没有缺口：两个分数 $p/q<u/v$ 之间总有另一个分数，$\frac12(p/q+u/v)=p/q+\frac12(u/v-p/q)$。然而仍有一些位置，没有分数落在那里（图 [6](#abb-6)）。完备性的意思是：每一个这样的分界都是一个数。

:::satz 定理 6.1 (2 的平方根不是分数)
<span class="anker" id="satz-6-1"></span>

不存在 $r\in\mathbb{Q}$ 使 $r^2=2$。
:::

:::beweis 反证法
假设：$r=\frac pq$，$p,q\in\mathbb{N}$（符号无关紧要），约分到 $p$ 和 $q$ 不全为偶数。由 $r^2=2$ 得 $p^2=2q^2$，所以 $p^2$ 是偶数。由第 [1](mengen-und-aussagen.html#stufe-1) 阶段的逆否命题，$p$ 是偶数，$p=2k$。代入：$4k^2=2q^2$，所以 $q^2=2k^2$，同样 $q$ 是偶数。于是 $p$ 和 $q$ 都是偶数，与约分矛盾。
:::

⁠**如何理解：**所以 $r^2=2$ 在 $\mathbb{Q}$ 中无解。对 $r^2=4$，这个证明理所当然地行不通（练习 [8](intervallschachtelung-und-wurzeln.html#aufg-8)）。

:::abbildung hm1/k1luecke 6
$D$ 中的分数和满足 $x^2>2$ 的分数可以任意接近，例如 1.414 和 1.415。它们之间的那个位置不是分数。
:::

:::definition 定义 6.2 (界、上确界、下确界)
<span class="anker" id="satz-6-2"></span>

设 $\mathbb K$ 是全序的，$M\subset\mathbb K$。

<ol class="rm">

<li>

若存在 $S\in\mathbb K$，使 $x\le S$ 对所有 $x\in M$ 成立，则称 $M$ __有上界__。每个这样的 $S$ 称为__上界__。类似地，用 $R\le x$ 定义__有下界__和__下界__。两者兼备称为__有界__。

</li>

<li>

若 $S$ 是上界，且对每个上界 $\tilde S$ 有 $S\le\tilde S$，则称 $S$ 为 $M$ 的__上确界__，$S=\sup M$（最小上界）。

</li>

<li>

若 $R$ 是下界，且对每个下界 $\tilde R$ 有 $\tilde R\le R$，则称 $R$ 为 $M$ 的__下确界__，$R=\inf M$（最大下界）。

</li>

<li>

若 $S$ 在 $M$ 中，则称之为__最大值__（$\max M$）；若 $R$ 在 $M$ 中，则称之为__最小值__（$\min M$）。

</li>

</ol>
:::

⁠**如何理解：**界位于外侧，而且不唯一：$\{2,3,5,7\}$ 有上界 7，也有上界 100。这里 $\sup=\max=7$，$\inf=\min=2$。$\mathbb{N}$ 有下界 1，没有上界（定理 [6.5](#satz-6-5)）。

:::frage 上确界不就是最大的元素吗？
只有当它在集合中时才是。$M=\{2-\frac1n:n\in\mathbb{N}\}=\{1,\frac32,\frac53,\dots\}$ 有 $\min M=1$ 和 $\sup M=2$，但没有最大值，因为 $2\notin M$。在参考模型中，$D$ 有上界，例如 $1.5$。然而 $D$ 在 $\mathbb{Q}$ 中没有上确界：每个上界都有一个更小的上界。
:::

:::definition 定义 6.3 (完备性公理 (V))
<span class="anker" id="satz-6-3"></span>

全序域 $\mathbb K$ 称为__完备__的，如果每个有下界的非空集合 $M\subset\mathbb K$ 都有最大下界 $\inf M\in\mathbb K$。
:::

⁠**如何理解：**关键在于“$\in\mathbb K$”。$\mathbb{Q}$ 不是完备的：$\{x\in\mathbb{Q}:x>0,\ x^2>2\}$ 有下界且非空，但在 $\mathbb{Q}$ 中没有最大下界。候选者本应是 $\sqrt2\notin\mathbb{Q}$。**为什么要求“非空”和“有界”：**对 $M=\emptyset$，每个数都是下界，不存在最大的下界。$M=\mathbb{Z}$ 没有下界。

:::satz 定理 6.4 (主定理)
<span class="anker" id="satz-6-4"></span>

本质上恰好存在一个包含 $\mathbb{Q}$ 的完备全序域。它就是__实数域__ $\mathbb{R}$，其序在 $\mathbb{Q}$ 上与通常的序一致。
:::

⁠**如何理解：**证明过于冗长，这里只需知道它的意义：三组公理在改名的意义下唯一确定 $\mathbb{R}$，所以才可以说**唯一的**实数。这取代了暂定的定义。域 $\{0,1\}$ 只满足域公理，$\mathbb{Q}$ 还满足序公理，只有 $\mathbb{R}$ 满足全部三组。与 (V) 等价的要求是每个柯西数列都收敛（第 4 章）。

:::satz 定理 6.5 (完备性的推论)
<span class="anker" id="satz-6-5"></span>

在 $\mathbb{R}$ 中有：

<ol class="rm">

<li>

每个有上界的非空集合 $M$ 都有上确界，且 $\sup M=-\inf(-M)$，其中 $-M:=\{-x:x\in M\}$。

</li>

<li>

集合的上确界和下确界是唯一的。

</li>

<li>

若 $S=\sup M$，则对每个 $y<S$ 存在 $x\in M$，使 $y<x\le S$。下确界有相应的结论。

</li>

<li>

$\mathbb{N}$ 没有上界。

</li>

<li>

__阿基米德定理：__对所有 $x,y>0$，存在 $n\in\mathbb{N}$，使 $nx>y$。

</li>

<li>

对每个 $x>0$，存在 $n\in\mathbb{N}$，使 $0<\frac1n<x$（欧多克索斯）。

</li>

</ol>
:::

⁠**如何理解：**(iii)：紧贴上确界的下方总有集合的元素。(v)：走足够多的小步 $x$，就能超过任何高度 $y$。对 $x=0.001$ 和 $y=1000$，$n=1\,000\,001$ 就够了。对 $x=0$，(v) 不成立，因为 $nx=0$。(vi)：对 $x=0.003$，$n=334$ 就够了。也可以把 (v) 作为公理。这比 (V) 弱，因为 $\mathbb{Q}$ 满足它。

:::beweis 推论
(i) $M$ 非空，$-M$ 也非空；若 $S$ 是 $M$ 的上界，则由定理 [4.2](anordnungsaxiome.html#satz-4-2) (a)，$-S$ 是 $-M$ 的下界。(V) 给出 $R=\inf(-M)$。因为反射把上界变成下界并使顺序反转，所以 $-R$ 是 $M$ 的最小上界。

(ii) 若 $S_1$、$S_2$ 都是上确界，则两者都是上界。于是 $S_1\le S_2$，因为 $S_1$ 是最小的，同样 $S_2\le S_1$。由 (O1)，$S_1=S_2$。

(iii) 反证：若存在 $y<S$ 而没有这样的 $x$，则 $x\le y$ 对所有 $x\in M$ 成立（否定，式 [(2.1)](quantoren-und-indirekter-beweis.html#gl-2-1)）。于是 $y$ 是比 $S$ 小的上界，与 $\sup M$ 的定义矛盾。$x\le S$ 成立，是因为 $S$ 是上界。

(iv) 反证：否则由 (i) 存在 $S=\sup\mathbb{N}$。由 (iii)，存在 $n\in\mathbb{N}$ 使 $S-1<n$。于是 $n+1>S$ 且 $n+1\in\mathbb{N}$，与“上界”矛盾。

(v) 反证：设 $nx\le y$ 对所有 $n$ 成立。因为 $x^{-1}>0$，由 (O4) 得 $n\le yx^{-1}$ 对所有 $n$ 成立，与 (iv) 矛盾。(vi)：在 (v) 中取 $y:=1$，得 $nx>1$，所以 $x>\frac1n>0$。
:::

:::aufgabe 练习 7 ★★ 确定界
<span class="anker" id="aufg-7"></span>

确定在 $\mathbb{R}$ 中的上确界、下确界、最大值和最小值（若存在），并说明理由： (a) $M_1=\{x\in\mathbb{Q}:x^2\le4\}$， (b) $M_2=\{\frac{(-1)^n}n:n\in\mathbb{N}\}$， (c) $M_3=\{x\in\mathbb{Q}:x^2<3\}$。如果只在 $\mathbb{Q}$ 中寻找，(c) 中缺少这些量中的哪些？

:::loesung
(a) $M_1=\{x\in\mathbb{Q}:-2\le x\le2\}$：$\sup=\max=2$，$\inf=\min=-2$。 (b) $M_2=\{-1,\frac12,-\frac13,\frac14,\dots\}$：$\sup=\max=\frac12$，$\inf=\min=-1$。 (c) $\sup M_3=\sqrt3$，$\inf M_3=-\sqrt3$，没有最大值和最小值，因为 $\sqrt3\notin\mathbb{Q}$（练习 [8](intervallschachtelung-und-wurzeln.html#aufg-8)）。在 $\mathbb{Q}$ 中上确界和下确界也不存在：每个有理上界都有一个更小的上界。
:::
:::
