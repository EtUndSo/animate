---
title: 第 2 阶段：量词与反证法
pfad: 电气工程 / 第 1 学期 / 高等数学 1 / 集合、逻辑与实数
order: 1210400
summary: 所有公理都具有“对所有 x 存在 y ”的形式。本阶段说明如何阅读和否定这样的语句，以及如何把否定变成证明。
tags: 全称量词, 存在量词, 反例, 反证假设, 罗素悖论
lang: zh
---

<span class="anker" id="stufe-2"></span>

:::zweck
所有公理都具有“对所有 $x$ 存在 $y$”的形式。本阶段说明如何阅读和否定这样的语句，以及如何把否定变成证明。
:::

**基本思路。** “对 $\{x_1,x_2,\dots\}$ 中所有 $x$，$\mathcal A(x)$ 成立”是一个长长的“且”：$\mathcal A(x_1)\wedge\mathcal A(x_2)\wedge\dots$ “存在一个 $x$”是一个长长的“或”。否定时，德摩根律把“且”变成“或”。因此否定时“对所有”变成“存在”。

:::definition 定义 2.1 (量词)
<span class="anker" id="satz-2-1"></span>

$\forall$ 表示“对所有”（__全称量词__），$\exists$ 表示“至少存在一个”（__存在量词__），$\exists_1$ 表示“恰好存在一个”，$\nexists$ 表示“不存在”。
:::

⁠**如何理解：**参考模型中的真例子有 $\forall x\in A:x\le12$；$\exists x\in A:x>5$（例如 $x=6$）；$\exists_1x\in A\cap B:x>2$（即 $x=3$）；$\nexists x\in B:x=9$。整除也是带量词的命题：$m\mid p$（“$m$ 整除 $p$”）表示 $\exists n\in\mathbb{N}:m\cdot n=p$，所以 $6\mid12$，因为 $6\cdot2=12$，而 $7\nmid12$。素数的集合是 $\{p\in\mathbb{N}\setminus\{1\}:\nexists m\in\{2,\dots,p-1\}\text{ 使 }m\mid p\}$。

:::satz 定理 2.2 (否定规则)
<span class="anker" id="satz-2-2"></span>

<span class="anker" id="gl-2-1"></span>
$$\neg\bigl(\forall x\in M:\mathcal A(x)\bigr)\Leftrightarrow\bigl(\exists x\in M:\neg\mathcal A(x)\bigr),\quad \neg\bigl(\exists y\in N:\mathcal B(y)\bigr)\Leftrightarrow\bigl(\forall y\in N:\neg\mathcal B(y)\bigr). \tag{2.1}$$
:::

⁠**如何理解：**交换量词，否定命题；量词嵌套时依次进行。在参考模型中，$\forall n\in\mathbb{N}:\mathcal E(n)$ 的否定是假命题 $\exists n\in\mathbb{N}:(n\ge7\wedge n\le5)$。**证明思路：**由德摩根律，$\neg(\mathcal A(x_1)\wedge\mathcal A(x_2)\wedge\dots)$ 就是 $\neg\mathcal A(x_1)\vee\neg\mathcal A(x_2)\vee\dots$；第二条规则同样得出。**极限情况** $M=\emptyset$：“对所有 $x\in\emptyset$”总为真，“存在 $x\in\emptyset$”总为假。

:::frage 五个例子足以证明“对所有”吗？
不足以。一个例子只检验一个 $x$。而根据式 [(2.1)](#gl-2-1)，只要一个__反例__就能推翻“对所有”的命题。反过来，“存在”用一个例子就能证明。
:::

::::beispiel 嵌套的量词
设 $H$ 是一个家庭的设备，$F$ 是保险丝，$K(g,s)$ 表示“设备 $g$ 接在保险丝 $s$ 上”。那么

$$\mathcal P:=\bigl(\forall g\in H\ \exists s\in F:K(g,s)\bigr),\qquad \mathcal Q:=\bigl(\exists s\in F\ \forall g\in H:K(g,s)\bigr)$$

说的是不同的事（图 [2](#abb-2)）：在 $\mathcal P$ 中，$s$ 可以随设备而定；在 $\mathcal Q$ 中，一个保险丝供全部设备。由 $\mathcal Q$ 可得 $\mathcal P$，反之不成立。**不同量词的次序不可交换。**否定分别是 $\neg\mathcal P=(\exists g\ \forall s:\neg K(g,s))$，即有一台设备不接在任何保险丝上，以及 $\neg\mathcal Q=(\forall s\ \exists g:\neg K(g,s))$，即每个保险丝都至少漏掉一台设备。

:::abbildung hm1/k1quantoren 2
右图满足两个命题，左图只满足第一个。
:::
::::

:::satz 定理 2.3 (反证法)
<span class="anker" id="satz-2-3"></span>

若 $\neg\mathcal A\Rightarrow\mathcal B$ 为真且 $\mathcal B$ 为假，则 $\mathcal A$ 为真。
:::

⁠**如何理解：**先假设断言的反面（__反证假设__），一直推理到得出假的结论。看一下真值表就明白其中的机制：若 $\neg\mathcal A$ 为真，则 $\mathcal B$ 也必须为真。所以 $\neg\mathcal A$ 为假。若要用反证法证明蕴涵 $\mathcal A\Rightarrow\mathcal B$，由德摩根律，假设是 $\mathcal A\wedge\neg\mathcal B$。**例：**不存在最小的正有理数。假设：$r$ 是最小的。那么 $r/2$ 是有理数，是正数，且小于 $r$。这是假的，所以不存在这样的 $r$。

**为什么需要公理。** 设 $M=\{N:N\notin N\}$ 是所有不包含自身的集合的集合（__罗素悖论__，1903）。若 $M\in M$ 为真，则 $M$ 不满足条件，所以 $M\notin M$。若 $M\notin M$ 为真，则 $M$ 满足条件，所以 $M\in M$。两者都不可能，这种构造是不允许的。“这句话是假的”这句话同样自相矛盾。这样的发现引发了数学的基础危机，从希尔伯特要求无矛盾的体系（1900）到哥德尔不完备性定理（1931）。教训是：确定性只相对于约定的假设而存在。所以要把数建立在公理之上。

:::aufgabe 练习 3 ★★ 否定与反证
<span class="anker" id="aufg-3"></span>

<ol class="al">

<li>

否定：“每个电路都含有一个会发热的元件。”

</li>

<li>

否定 $\forall\varepsilon>0\ \exists n\in\mathbb{N}:\frac1n<\varepsilon$。交换量词后命题为真还是为假？

</li>

<li>

用反证法证明：若 $n^2$ 为奇数，则 $n$ 为奇数。

</li>

</ol>

:::loesung
(a) “存在一个电路，其中没有元件发热。” (b) 否定：$\exists\varepsilon>0\ \forall n\in\mathbb{N}:\frac1n\ge\varepsilon$。交换后：$\exists n\in\mathbb{N}\ \forall\varepsilon>0:\frac1n<\varepsilon$ 为假，因为取 $\varepsilon=\frac1n$ 得 $\frac1n<\frac1n$。而原命题为真，这由第 [6](das-vollstandigkeitsaxiom.html#stufe-6) 阶段说明。 (c) 假设：$n^2$ 为奇数且 $n$ 为偶数，$n=2k$。则 $n^2=2\cdot2k^2$ 为偶数，矛盾。
:::
:::
