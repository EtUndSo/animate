---
title: 第 7 阶段：区间套与平方根
pfad: 电气工程 / 第 1 学期 / 高等数学 1 / 集合、逻辑与实数
order: 1210900
summary: 公理保证了分界的存在。本阶段把这一点变成一种构造方法，并由此证明 x 2=2 在 mathbb R 中恰有一个正解。
tags: 区间, 非负数, 平方根
lang: zh
---

<span class="anker" id="stufe-7"></span>

:::zweck
公理保证了分界的存在。本阶段把这一点变成一种构造方法，并由此证明 $x^2=2$ 在 $\mathbb{R}$ 中恰有一个正解。
:::

**基本思路。** 把要找的数夹在两个分数之间，然后一次次把区间对半分，直到它任意小（图 [7](#abb-7)）。每个区间都在前一个区间之内。完备性保证存在一个位于所有区间中的点。在 $\mathbb{Q}$ 中这个点可能不存在。__区间__是 $[a,b]:=\{x\in\mathbb{R}:a\le x\le b\}$，__非负数__是 $\mathbb{R}_0^+:=\{x\in\mathbb{R}:x\ge0\}$。

:::satz 定理 7.1 (区间套)
<span class="anker" id="satz-7-1"></span>

设数 $a_n,b_n\in\mathbb{R}$，$n\in\mathbb{N}$，满足 $a_1\le a_2\le a_3\le\dots\le b_3\le b_2\le b_1$ 和

<span class="anker" id="gl-7-1"></span>
$$\forall\varepsilon>0\ \exists n\in\mathbb{N}:\ 0\le b_n-a_n<\varepsilon. \tag{7.1}$$

则恰好存在一个 $x\in\mathbb{R}$，使 $a_n\le x\le b_n$ 对所有 $n\in\mathbb{N}$ 成立。
:::

⁠**如何理解：**$\varepsilon$（希腊字母 epsilon）是任意小的正数。式 [(7.1)](#gl-7-1) 的意思是：区间 $[a_n,b_n]$ 变得比任何给定长度都小。**为什么需要这些前提：**没有式 [(7.1)](#gl-7-1)，$x$ 就不唯一：对 $a_n=-\frac1n$，$b_n=1+\frac1n$，整个 $[0,1]$ 都在所有区间中。在 $\mathbb{Q}$ 中定理不成立：图 [7](#abb-7) 中的分数 $a_n,b_n$ 满足全部条件，但没有分数位于所有区间中。

:::beweis 区间套
⁠**存在性。**对任意 $n,k$，设 $m$ 是这两个数中较大的一个。则 $a_n\le a_m\le b_m\le b_k$。所以每个 $b_k$ 都是 $A:=\{a_n:n\in\mathbb{N}\}$ 的上界。由定理 [6.5](das-vollstandigkeitsaxiom.html#satz-6-5) (i)，$x:=\sup A$ 存在。有 $a_n\le x$，因为 $x$ 是上界；有 $x\le b_k$，因为 $x$ 是最小的上界。

⁠**唯一性。**若 $x<\tilde x$ 都在所有区间中，则 $b_n-a_n\ge\tilde x-x=:\varepsilon>0$ 对所有 $n$ 成立，与式 [(7.1)](#gl-7-1) 矛盾。
:::

:::abbildung hm1/k1schachtelung 7
对 $x^2=2$ 进行对分：若中点的平方小于 2，中点成为新的左端点，否则成为新的右端点。长度为 $b_n-a_n=2^{1-n}$。
:::

:::satz 定理 7.2 (平方根)
<span class="anker" id="satz-7-2"></span>

对每个 $y\in\mathbb{R}_0^+$，恰好存在一个 $x\in\mathbb{R}_0^+$ 使 $x^2=y$。记作 $x=\sqrt y$（“$y$ 的__平方根__”）。对 $x,y\ge0$ 有 $\sqrt{xy}=\sqrt x\sqrt y$。
:::

⁠**如何理解：**平方根是非负解，$\sqrt{4}=2$ 而不是 $-2$。方程 $z^2=2$ 有两个解：$\sqrt2$ 和 $-\sqrt2$，因为 $(-1)(-1)=1$。乘积法则需要 $x,y\ge0$：$\sqrt{(-1)(-1)}=1$，但 $\sqrt{-1}$ 在 $\mathbb{R}$ 中不存在。**极限情况** $y=0$：唯一的解是 $x=0$。

:::beweis $y=2$ 时的存在性、唯一性、乘积法则
从 $a_1=1$，$b_1=2$ 开始，按图 [7](#abb-7) 对分。所有 $a_n$、$b_n$ 都是分数，所以由定理 [6.1](das-vollstandigkeitsaxiom.html#satz-6-1)，决不会有 $a_n^2=2$ 或 $b_n^2=2$。这给出 $a_n^2<2<b_n^2$，以及 $b_n-a_n=2^{1-n}\le\frac1n$，因为 $2^{n-1}\ge n$（练习 [10](elementare-ungleichungen.html#aufg-10)）。由定理 [6.5](das-vollstandigkeitsaxiom.html#satz-6-5) (vi)，式 [(7.1)](#gl-7-1) 成立，所以存在 $x$，使 $a_n\le x\le b_n$ 对所有 $n$ 成立。

为什么 $x^2=2$：由 $a_n\le x\le b_n$ 和定理 [4.2](anordnungsaxiome.html#satz-4-2) (e) 得 $a_n^2\le x^2\le b_n^2$。2 也在 $[a_n^2,b_n^2]$ 中。这个区间的长度是 $(b_n-a_n)(b_n+a_n)\le4\cdot\frac1n$。所以 $x^2$ 与 2 的距离小于任何正数，因而为零。对其他 $y>0$，从 $[0,y+1]$ 开始；若某个中点 $m$ 恰好满足 $m^2=y$，则 $x=m$。对 $y=0$，$x=0$。**唯一性：**由 $u>v\ge0$ 得 $u^2>v^2$，两个不同的非负数有不同的平方。

⁠**乘积法则：**$\sqrt x\sqrt y\ge0$ 且 $(\sqrt x\sqrt y)^2=xy$（M1，M2），而非负解是唯一的。
:::

::::beispiel
六步之后 $1.40625\le\sqrt2\le1.4375$，宽度 $2^{-5}=0.03125$。小数是同一种思路，只是分成十份而不是两份：每一位数字把区间缩小到十分之一。所以每个实数都有表示式 [(0.1)](von-grund-auf-zahlbereiche-und-dezimalzahlen.html#gl-0-1)。
::::

:::frage 从计算器上读出 $\sqrt2$ 不就够了吗？何必费这么大劲？
对任何数值来说，这就够了。但计算器显示的是一个分数，$1.414213562$，它的平方不是 2。这里的问题是：究竟有没有一个数，平方恰好是 2？在 $\mathbb{Q}$ 中没有，在 $\mathbb{R}$ 中有，而这个差别日后支撑着极限和连续性。
:::

:::aufgabe 练习 8 ★★★ 3 的平方根
<span class="anker" id="aufg-8"></span>

<ol class="al">

<li>

对 $x^2=3$ 进行三步对分，从 $[1,2]$ 开始。结果的宽度是多少？

</li>

<li>

证明 $\sqrt3\notin\mathbb{Q}$。提示：不能被 3 整除的数具有 $3k\pm1$ 的形式。

</li>

<li>

同样的证明对 $\sqrt4$ 在哪里行不通？

</li>

</ol>

:::loesung
(a) 中点 $1.5$：$2.25<3$，所以得 $[1.5, 2]$。中点 $1.75$：$3.0625>3$，所以得 $[1.5, 1.75]$。中点 $1.625$：$2.640625<3$，所以得 $[1.625, 1.75]$。宽度 $\frac18=0.125$。 (b) 假设：$\sqrt3=\frac pq$，$p,q\in\mathbb{N}$，不全被 3 整除。则 $p^2=3q^2$。若 $p=3k\pm1$，则 $p^2=3(3k^2\pm2k)+1$，不能被 3 整除。所以 $p=3k$，于是 $q^2=3k^2$，同样 $q$ 被 3 整除。矛盾。 (c) 由 $p^2=4q^2$ 得 $p=2k$ 和 $k^2=q^2$。这对 $q$ 的整除性没有任何断定：$\sqrt4=\frac21$。
:::
:::
