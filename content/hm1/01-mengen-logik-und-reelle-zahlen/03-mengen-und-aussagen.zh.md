---
title: 第 1 阶段：集合与命题
pfad: 电气工程 / 第 1 学期 / 高等数学 1 / 集合、逻辑与实数
order: 1210300
summary: 公理谈论“具有某种性质的所有数”和“如果，那么”。本阶段提供表达这些内容的语言，以及一种证明集合与命题规则的可靠方法。
tags: 韦恩图, 元素, 子集, 超集, 并集, 交集, 差集, 补集
lang: zh
---

<span class="anker" id="stufe-1"></span>

:::zweck
公理谈论“具有某种性质的所有数”和“如果，那么”。本阶段提供表达这些内容的语言，以及一种证明集合与命题规则的可靠方法。
:::

**基本思路。** 对集合来说只有一个问题要紧：一个对象在不在其中？对命题也一样：真还是假？因此两个集合或命题有四种情形，三个有八种。证明一条规则，就是在一张表中逐一检查所有情形。__韦恩图__（把集合画成区域）只起示意作用，它只显示集合的一种可能位置关系（图 [1](#abb-1)）。

:::definition 定义 1.1 (集合)
<span class="anker" id="satz-1-1"></span>

集合是确定的、可区分的对象的无序汇集，这些对象称为它的__元素__。$x\in M$ 表示“$x$ 是 $M$ 的元素”，$x\notin M$ 表示相反情况。对集合 $A$、$B$ 规定：

| 符号 | 名称 | 含义 |
|---|---|---|
| $A\subset B$ | __子集__ | $A$ 的每个元素都在 $B$ 中（允许 $A=B$）；$B\supset A$：__超集__ |
| $A=B$ | 相等 | $A\subset B$ 且 $B\subset A$；否则写作 $A\ne B$ |
| $A\cup B$ | __并集__ | 所有在 $A$ 中或在 $B$ 中的元素，也包括同时在两者中的 |
| $A\cap B$ | __交集__ | 所有既在 $A$ 中又在 $B$ 中的元素 |
| $A\setminus B$ | __差集__ | $A$ 中所有不在 $B$ 中的元素 |
| $A^c$ | __补集__ | 一个固定超集中所有不在 $A$ 中的元素 |
| $\emptyset=\{\,\}$ | __空集__ | 不含任何元素 |
| $\mathcal P(A)$ | __幂集__ | $A$ 的所有子集构成的集合 |

若 $A\cap B=\emptyset$，则称 $A$ 和 $B$ __不相交__。
:::

⁠**如何理解：**在参考模型中，$A\cup B=\{1,2,3,4,5,6,7,11,12\}$，$A\cap B=\{2,3\}$，$A\setminus B=\{1,4,6,12\}$，相对于 $G$ 有 $A^c=\{5,7,8,9,10,11\}$。集合可以用性质给出：$\{x\in G:x\text{ 为偶数}\}=\{2,4,6,8,10,12\}$。有 $\mathcal P(\{5,7\})=\{\emptyset,\{5\},\{7\},\{5,7\}\}$。总有 $\emptyset\subset A$，$A\cup\emptyset=A$，$A\cap\emptyset=\emptyset$，$A\setminus B=A\cap B^c$。

:::abbildung hm1/k1venn 1
左图：$G$ 的元素分布在四个区域中。右图：着色部分是 $(A\cap B)^c$，即透镜形区域以外的全部。
:::

:::definition 定义 1.2 (命题与联结词)
<span class="anker" id="satz-1-2"></span>

命题是只能为真（$t$）或假（$f$）的断言。由命题 $\mathcal A$、$\mathcal B$ 可以得到新的命题，由下面的__真值表__确定：

| $\mathcal A$ | $\mathcal B$ | $\neg\mathcal A$ | $\mathcal A\vee\mathcal B$ | $\mathcal A\wedge\mathcal B$ | $\mathcal A\Rightarrow\mathcal B$ | $\mathcal A\Leftrightarrow\mathcal B$ |
|---|---|---|---|---|---|---|
| $t$ | $t$ | $f$ | $t$ | $t$ | $t$ | $t$ |
| $t$ | $f$ | $f$ | $t$ | $f$ | $f$ | $f$ |
| $f$ | $t$ | $t$ | $t$ | $f$ | $t$ | $f$ |
| $f$ | $f$ | $t$ | $f$ | $f$ | $t$ | $t$ |

它们的名称是__否定__、__析取__、__合取__、__蕴涵__和__等价__。
:::

⁠**如何理解：**“2 是素数”是真命题，“现在几点了？”不是命题。“每个不小于 4 的偶数都是两个素数之和”也是命题，尽管没有人知道它是否为真（哥德巴赫猜想）。命题可以依赖于一个__参数__：$\mathcal T(n):=(n\text{ 整除 }12)$ 对 $n=4$ 为真，对 $n=5$ 为假。“或”包含“两者都”。$\neg$ 的结合力最强：$\neg\mathcal A\vee\mathcal B$ 表示 $(\neg\mathcal A)\vee\mathcal B$。$\mathcal A\Leftrightarrow\mathcal B$ 与 $(\mathcal A\Rightarrow\mathcal B)\wedge(\mathcal B\Rightarrow\mathcal A)$ 意义相同。真值表中列相同的两个命题是**等价**的。若 $\mathcal A\Rightarrow\mathcal B$ 为真且 $\mathcal A$ 为真，则 $\mathcal B$ 为真。若 $\mathcal A$ 为假，蕴涵对 $\mathcal B$ 没有任何断定。

:::frage 为什么 $f\Rightarrow t$ 为真？从假的东西什么也推不出来啊。
正确的说法是：假的 $\mathcal A$ 对 $\mathcal B$ 没有任何断定。正因如此，这时蕴涵并没有被违反。这一规定是被迫的：$\mathcal E(n)$ 应当对所有 $n$ 为真，而 $n=6$ 给出 $f\Rightarrow t$，$n\le5$ 给出 $f\Rightarrow f$。如果这些行为假，$\mathcal E(n)$ 在那里就为假。只有 $t\Rightarrow f$ 对任何 $n$ 都不出现，而这就是全部断言：$\{n\ge7\}$ 包含于 $\{n>5\}$。蕴涵就是子集关系。
:::

:::satz 定理 1.3 (运算律与重言式)
<span class="anker" id="satz-1-3"></span>

__重言式__是对其组成部分的所有真值都为真的命题。对同一超集中的集合以及对命题，有下列规则：

| 名称 | 集合 | 命题 |
|---|---|---|
| 双重否定 | $(A^c)^c=A$ | $\neg(\neg\mathcal A)\Leftrightarrow\mathcal A$ |
| 交换律 | $A\cap B=B\cap A$，$A\cup B=B\cup A$ | $(\mathcal A\wedge\mathcal B)\Leftrightarrow(\mathcal B\wedge\mathcal A)$，$(\mathcal A\vee\mathcal B)\Leftrightarrow(\mathcal B\vee\mathcal A)$ |
| 结合律 | $(A\cap B)\cap C=A\cap(B\cap C)$，$\cup$ 同样 | $(\mathcal A\wedge(\mathcal B\wedge\mathcal C))\Leftrightarrow((\mathcal A\wedge\mathcal B)\wedge\mathcal C)$，$\vee$ 同样 |
| 分配律 | $A\cap(B\cup C)=(A\cap B)\cup(A\cap C)$，$A\cup(B\cap C)=(A\cup B)\cap(A\cup C)$ | $(\mathcal A\wedge(\mathcal B\vee\mathcal C))\Leftrightarrow((\mathcal A\wedge\mathcal B)\vee(\mathcal A\wedge\mathcal C))$，$(\mathcal A\vee(\mathcal B\wedge\mathcal C))\Leftrightarrow((\mathcal A\vee\mathcal B)\wedge(\mathcal A\vee\mathcal C))$ |
| 德摩根律 | $(A\cap B)^c=A^c\cup B^c$，$(A\cup B)^c=A^c\cap B^c$ | $\neg(\mathcal A\wedge\mathcal B)\Leftrightarrow(\neg\mathcal A\vee\neg\mathcal B)$，$\neg(\mathcal A\vee\mathcal B)\Leftrightarrow(\neg\mathcal A\wedge\neg\mathcal B)$ |
| 幂等律 | $A\cup A=A$，$A\cap A=A$ | $(\mathcal A\vee\mathcal A)\Leftrightarrow\mathcal A$，$(\mathcal A\wedge\mathcal A)\Leftrightarrow\mathcal A$ |
| 蕴涵 | $A\subset B\Leftrightarrow A^c\cup B=G$（$G$ 为超集） | $(\mathcal A\Rightarrow\mathcal B)\Leftrightarrow(\neg\mathcal A\vee\mathcal B)$ |
| 逆否律 | $A\subset B\Leftrightarrow B^c\subset A^c$ | $(\mathcal A\Rightarrow\mathcal B)\Leftrightarrow(\neg\mathcal B\Rightarrow\neg\mathcal A)$ |
| 传递律 | $(A\subset B\wedge B\subset C)\Rightarrow A\subset C$ | $((\mathcal A\Rightarrow\mathcal B)\wedge(\mathcal B\Rightarrow\mathcal C))\Rightarrow(\mathcal A\Rightarrow\mathcal C)$ |
:::

⁠**如何理解：**左右两边是同一条规则，因为每个集合关系都是关于元素的命题：$A\subset B$ 表示“对所有 $x$：$(x\in A)\Rightarrow(x\in B)$”，$A=B$ 表示“对所有 $x$：$(x\in A)\Leftrightarrow(x\in B)$”，而 $x\in A\cap B$、$x\in A\cup B$、$x\in A\setminus B$ 分别表示 $(x\in A)\wedge(x\in B)$、$(x\in A)\vee(x\in B)$、$(x\in A)\wedge(x\notin B)$。数字电路中的门电路就是用电路实现的 $\neg$、$\wedge$、$\vee$，而德摩根律使我们可以用或门和反相器搭出与门。

:::beweis 用真值表证明德摩根律和逆否律
逐一检查组成部分的全部四种情形。若把 $t$ 读作“$x$ 在集合中”，这同时也是对集合的证明（__元素表__）。

| $\mathcal A$ | $\mathcal B$ | $\neg\mathcal A$ | $\neg\mathcal B$ | $\neg(\mathcal A\wedge\mathcal B)$ | $\neg\mathcal A\vee\neg\mathcal B$ | $\mathcal A\Rightarrow\mathcal B$ | $\neg\mathcal B\Rightarrow\neg\mathcal A$ |
|---|---|---|---|---|---|---|---|
| $t$ | $t$ | $f$ | $f$ | $f$ | $f$ | $t$ | $t$ |
| $t$ | $f$ | $f$ | $t$ | $t$ | $t$ | $f$ | $f$ |
| $f$ | $t$ | $t$ | $f$ | $t$ | $t$ | $t$ | $t$ |
| $f$ | $f$ | $t$ | $t$ | $t$ | $t$ | $t$ | $t$ |

第 5 列与第 6 列相同，第 7 列与第 8 列也相同。其余规则的证明方法相同。包含关系的传递性来自蕴涵的传递性：由 $x\in A$ 得 $x\in B$，再得 $x\in C$。
:::

::::beispiel
$(A\cap B)^c=G\setminus\{2,3\}$ 有 10 个元素。右边是 $A^c\cup B^c=\{5,7,8,9,10,11\}\cup\{1,4,6,8,9,10,12\}$，是同样的 10 个元素。逆否律作为证明工具：不证“$n^2$ 为偶数 $\Rightarrow$ $n$ 为偶数”，而证“$n$ 为奇数 $\Rightarrow$ $n^2$ 为奇数”：$(2k+1)^2=2(2k^2+2k)+1$。
::::

⁠**极限情况：**$B=\emptyset$ 时德摩根律变为 $G=G$。论域也有关系：$(n\ge7\Leftrightarrow n>6)$ 在 $\mathbb{N}$ 中成立，而对 $n=13/2$ 它是 $f\Leftrightarrow t$，即为假。

:::aufgabe 练习 1 ★ 集合运算
<span class="anker" id="aufg-1"></span>

<ol class="al">

<li>

在参考模型中计算 $(A\cup B)^c$ 和 $A\setminus(A\cap B)$。

</li>

<li>

用元素表证明：$(A\setminus B)\cup(B\setminus A)=(A\cup B)\setminus(A\cap B)$。

</li>

<li>

$\mathcal P(A\cap B)$ 有多少个元素？预测当 $M$ 恰有 $n$ 个元素时 $\mathcal P(M)$ 有多少个元素，并说明理由。

</li>

</ol>

:::loesung
(a) $A\cup B=\{1,2,3,4,5,6,7,11,12\}$，所以 $(A\cup B)^c=\{8,9,10\}$。$A\setminus(A\cap B)=A\setminus\{2,3\}=\{1,4,6,12\}$，这就是 $A\setminus B$。 (b) 对 $x$ 在 $A$、$B$ 中的情形 $(\in,\in)$、$(\in,\notin)$、$(\notin,\in)$、$(\notin,\notin)$，两边都给出 $\notin,\in,\in,\notin$：$x$ 恰好在其中一个集合中时才属于它。 (c) $A\cap B=\{2,3\}$ 有 2 个元素，$\mathcal P(A\cap B)$ 有 $2^2=4$ 个。有 $n$ 个元素时，对每个元素单独决定：取或不取。这就是 $2^n$ 个子集。
:::
:::

:::aufgabe 练习 2 ★★ 用表格推理
<span class="anker" id="aufg-2"></span>

<ol class="al">

<li>

用八行的真值表证明蕴涵的传递性。

</li>

<li>

如果保险丝完好（$\mathcal A$），灯就亮（$\mathcal B$）。这个蕴涵为真，而灯不亮。关于保险丝能得出什么？如果灯亮呢？

</li>

<li>

$(\mathcal A\Rightarrow\mathcal B)\Leftrightarrow(\mathcal B\Rightarrow\mathcal A)$ 是重言式吗？

</li>

</ol>

:::loesung
(a) 前提 $(\mathcal A\Rightarrow\mathcal B)\wedge(\mathcal B\Rightarrow\mathcal C)$ 只对 $(\mathcal A,\mathcal B,\mathcal C)=(t,t,t)$、$(f,t,t)$、$(f,f,t)$、$(f,f,f)$ 为真。在这四行中 $\mathcal A\Rightarrow\mathcal C$ 都为真。在其余四行中前提为假，所以整个命题为真。 (b) 逆否：$\neg\mathcal B\Rightarrow\neg\mathcal A$，保险丝不完好。灯亮时什么也推不出：$f\Rightarrow t$ 这一行是允许的。 (c) 不是：当 $\mathcal A=t$，$\mathcal B=f$ 时，左边是 $f\Leftrightarrow t$，即为假。
:::
:::
