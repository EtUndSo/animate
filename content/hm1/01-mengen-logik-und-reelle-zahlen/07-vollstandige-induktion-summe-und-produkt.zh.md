---
title: 第 5 阶段：数学归纳法、求和与求积
pfad: 电气工程 / 第 1 学期 / 高等数学 1 / 集合、逻辑与实数
order: 1210700
summary: 关于所有 ninmathbb N 的命题不能靠试验来证明。本阶段提供这种方法，并由此给出和、积与幂的严格定义。
tags: 归纳基础, 归纳步骤, 归纳假设, 归纳结论
lang: zh
---

<span class="anker" id="stufe-5"></span>

:::zweck
关于所有 $n\in\mathbb{N}$ 的命题不能靠试验来证明。本阶段提供这种方法，并由此给出和、积与幂的严格定义。
:::

**基本思路。** 每个自然数都由 1 反复往后数得到。如果证明了命题对 1 成立，又证明了它能从每个 $n$ 传递到 $n+1$，这条链就能到达每个数（图 [5](#abb-5)）。

:::satz 定理 5.1 (数学归纳法)
<span class="anker" id="satz-5-1"></span>

设 $\mathcal A(n)$ 是一列命题，$n\in\mathbb{N}$。若 (1) $\mathcal A(1)$ 为真（__归纳基础__），且 (2) 对任意 $n$，蕴涵 $\mathcal A(n)\Rightarrow\mathcal A(n+1)$ 为真（__归纳步骤__，$\mathcal A(n)$ 称为__归纳假设__），则 $\mathcal A(n)$ 对所有 $n\in\mathbb{N}$ 为真（__归纳结论__）。

⁠**第二种形式：**设 $n_0\in\mathbb{N}$ 固定。若 $\mathcal A(n_0)$ 为真，且对每个 $n\ge n_0$ 有

$$\bigl(\mathcal A(n_0)\wedge\mathcal A(n_0+1)\wedge\dots\wedge\mathcal A(n)\bigr)\Rightarrow\mathcal A(n+1),$$

则 $\mathcal A(n)$ 对所有 $n\ge n_0$ 为真。
:::

⁠**如何理解：**第二种形式允许较晚的起点，并允许把所有较早的情形作为假设。**为什么两部分都需要：**没有基础：$\mathcal A(n):=(n=n+1)$ 有成立的归纳步骤（两边加 1），却总是假的。没有步骤：$n^2-n+41$ 对 $n=1,\dots,40$ 都是素数，而对 $n=41$ 却是 $41^2$。

:::frage 归纳步骤不是把要证明的东西当作前提了吗？
不是。这里只对任意但固定的 $n$ 假设 $\mathcal A(n)$，并且只证明蕴涵 $\mathcal A(n)\Rightarrow\mathcal A(n+1)$。$\mathcal A(n)$ 为真，是由基础和这条链才得出的。
:::

:::beweis 归纳法为什么成立
$\mathbb{N}$ 有这样的性质：若 $M\subset\mathbb{N}$，$1\in M$，且由 $n\in M$ 总能得出 $n+1\in M$，则 $M=\mathbb{N}$。这就是 $\mathbb{N}$ 本身的构造。取 $M:=\{n\in\mathbb{N}:\mathcal A(n)\text{ 为真}\}$。对第二种形式，设 $\mathcal B(n):=\mathcal A(n_0)\wedge\dots\wedge\mathcal A(n)$。由前提得 $\mathcal B(n)\Rightarrow\mathcal B(n+1)$，而 $\mathbb{N}$ 的同一性质从 $n_0$ 出发，给出 $\mathcal B(n)$ 对所有 $n\ge n_0$ 成立。
:::

:::definition 定义 5.2 (和、积、幂：递归定义)
<span class="anker" id="satz-5-2"></span>

对 $x_1,x_2,\ldots\in\mathbb K$ 定义

<span class="anker" id="gl-5-1"></span>
$$\sum_{i=1}^{1}x_i:=x_1,\quad\sum_{i=1}^{n+1}x_i:=\Bigl(\sum_{i=1}^{n}x_i\Bigr)+x_{n+1},\qquad \prod_{i=1}^{1}x_i:=x_1,\quad\prod_{i=1}^{n+1}x_i:=\Bigl(\prod_{i=1}^{n}x_i\Bigr)\cdot x_{n+1}. \tag{5.1}$$

若所有 $x_i=x$，则 $x^n:=\prod_{i=1}^nx$。对 $x\ne0$ 和 $n\in\mathbb{N}$，定义 $x^0:=1$，$x^{-n}:=(x^n)^{-1}=(\frac1x)^n$。此外 $n!:=\prod_{i=1}^ni$，$0^0:=1$。
:::

⁠**如何理解：**$\sum_{i=1}^nx_i=x_1+\dots+x_n$，省略号现在由递归说明，根据定理 [5.1](#satz-5-1)，其值对每个 $n$ 都已确定。$x^0:=1$ 是被迫的，因为 $x^n\cdot x^0=x^{n+0}$ 应当成立。$0^0:=1$ 是一项约定：这样 $x^0=1$ 就延拓到 $x=0$，而 $(x+y)^2=x^2y^0+2x^1y^1+x^0y^2$ 对 $x=0$ 或 $y=0$ 仍然正确。

:::satz 定理 5.3 (和、积、幂的运算法则)
<span class="anker" id="satz-5-3"></span>

在每个域中有：

<ol class="rm">

<li>

$\sum_{i=1}^nx_i$ 和 $\prod_{i=1}^nx_i$ 的值与 $x_i$ 的次序无关。

</li>

<li>

和的乘积：$\Bigl(\sum_{i=1}^nx_i\Bigr)\Bigl(\sum_{j=1}^Ny_j\Bigr)=\sum_{i=1}^n\Bigl(\sum_{j=1}^Nx_iy_j\Bigr)$。

</li>

<li>

幂运算律，$x,y\ne0$，$p,q\in\mathbb{Z}$：$x^px^q=x^{p+q}$，$(x^p)^q=x^{p\cdot q}$，$(xy)^p=x^py^p$。

</li>

</ol>
:::

⁠**如何理解：**(i) 是对 (A1)、(A2)、(M1)、(M2) 的归纳。(ii) 说的是“每项乘每项”，就是重复使用 (AM)。对 $p,q\in\mathbb{N}$，(iii) 就是重新编号：$x^px^q=\prod_{i=1}^{p+q}x=x^{p+q}$。**为什么要求 $x\ne0$：**$0^{-1}$ 不存在，当 $x=0$ 时只允许指数 $n\ge0$，且当 $n\ge1$ 时 $0^n=0$。对 $x,y>0$，这些运算律对有理指数也成立，例如 $x^{1/2}=\sqrt x$（第 5 部分）。

:::abbildung hm1/k1induktion 5
左图中每种颜色是一层 L 形。右图是归纳步骤：$n^2$ 增加 $2n+1$ 个方格。
:::

::::beispiel [例 1] 奇数之和
断言：$\sum_{i=1}^n(2i-1)=n^2$。**基础：**$2\cdot1-1=1=1^2$。**步骤：**若公式对 $n$ 成立，则 $\sum_{i=1}^{n+1}(2i-1)=n^2+2(n+1)-1=n^2+2n+1=(n+1)^2$。**结论：**它对所有 $n$ 成立。同样可证 $\sum_{i=1}^ni=\frac{n(n+1)}2$ 和 $\sum_{i=1}^ni^3=\frac{n^2(n+1)^2}4$（练习 [6](#aufg-6)）。
::::

::::beispiel [例 2] 较晚的起点
$n!>2^n$ 对 $n\ge n_0=4$ 成立。基础：$24>16$。步骤：$(n+1)!=(n+1)\,n!>(n+1)\,2^n\ge2\cdot2^n$，因为 $n+1\ge2$。
::::

⁠**极限情况：**$n=3$ 时 $6<8$，必须从 4 开始。

::::beispiel [例 3] 所有较早的情形
每个 $n\ge2$ 都是素数的乘积。基础：2 是素数。步骤：若 $n+1$ 不是素数，则 $n+1=ab$，$2\le a,b\le n$。这里只有 $\mathcal A(n)$ 不够，需要 $\mathcal A(a)$ 和 $\mathcal A(b)$。
::::

:::aufgabe 练习 6 ★★ 归纳法练习
<span class="anker" id="aufg-6"></span>

<ol class="al">

<li>

证明 $\sum_{i=1}^ni^3=\frac{n^2(n+1)^2}4$，并检验 $n=3$。

</li>

<li>

计算 $\prod_{i=1}^5(1+\frac1i)$。预测 $\prod_{i=1}^n(1+\frac1i)$ 的公式并加以证明。

</li>

<li>

找出错误：“所有电缆颜色都相同。基础：一根电缆只有一种颜色。步骤：从 $n+1$ 根电缆中拿走一根，其余 $n$ 根颜色相同。再拿走另一根，同样如此。所以全部颜色相同。”

</li>

</ol>

:::loesung
(a) 基础：$1=\frac{1\cdot4}4$。步骤：$\frac{n^2(n+1)^2}4+(n+1)^3=\frac{(n+1)^2(n^2+4n+4)}4=\frac{(n+1)^2(n+2)^2}4$。检验：$1+8+27=36=\frac{9\cdot16}4$。 (b) $2\cdot\frac32\cdot\frac43\cdot\frac54\cdot\frac65=6$。猜想：$n+1$。基础：$1+\frac11=2$。步骤：$(n+1)(1+\frac1{n+1})=n+2$。 (c) 步骤在 $n=1$ 时失败：两根电缆拿走一根后，每次剩下的是不同的一根，两次剩下的没有公共的电缆。步骤必须对每个 $n$ 成立。
:::
:::
