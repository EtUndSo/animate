---
title: 第 4 阶段：序公理
pfad: 电气工程 / 第 1 学期 / 高等数学 1 / 集合、逻辑与实数
order: 1210600
summary: 域公理对“大于”只字未提。不等式运算的背后有哪些假设？
tags: 全序, 三分律
lang: zh
---

<span class="anker" id="stufe-4"></span>

:::zweck
域公理对“大于”只字未提。不等式运算的背后有哪些假设？
:::

**基本思路。** 实数按大小排列在一条直线上。只需规定哪些数是正数。于是“$x$ 大于 $y$”就等于“$x-y$ 是正数”。乘以负数使直线关于零点反射，所以顺序反转（图 [4](#abb-4)）。

:::definition 定义 4.1 (全序域)
<span class="anker" id="satz-4-1"></span>

带有关系“$>0$”的域 $\mathbb K$ 称为__全序__的，如果：

<ul>

<li>

⁠**(T1)** 每个 $x\in\mathbb K$ 恰好满足关系 $x>0$、$x=0$、$(-x)>0$ 之一。

</li>

<li>

⁠**(T2)** $x>0\wedge y>0\Rightarrow x+y>0$。

</li>

<li>

⁠**(T3)** $x>0\wedge y>0\Rightarrow x\cdot y>0$。

</li>

</ul>

定义 $x>y:\Leftrightarrow x-y>0$，$x<y:\Leftrightarrow y>x$，$x\ge y:\Leftrightarrow(x=y\vee x>y)$，$x\le y$ 与此类似。
:::

⁠**如何理解：**$x>0$ 表示“$x$ 是正数”。(T2) 和 (T3)：正数的和与积都是正数。$x<0$ 与 $(-x)>0$ 意义相同：$x$ 是负数。

:::satz 定理 4.2 (不等式的运算)
<span class="anker" id="satz-4-2"></span>

在全序域中，对所有 $x,y,z,u,v$ 有：

|  |  |
|---|---|
| (O1) __三分律__ | 关系 $x<y$、$x=y$、$x>y$ 恰有一个成立 |
| (O2) 传递性 | $x<y\wedge y<z\Rightarrow x<z$ |
| (O3) 加法单调性 | $x<y\Rightarrow x+z<y+z$ |
| (O4) 乘法单调性 | $x<y\wedge z>0\Rightarrow xz<yz$ |
| (a) 反射 | $x<y\Leftrightarrow-y<-x$ |
| (b) 相加 | $x<y\wedge u<v\Rightarrow x+u<y+v$ |
| (c) 符号 | $xy>0\Leftrightarrow\bigl((x>0\wedge y>0)\vee(x<0\wedge y<0)\bigr)$ |
| (d) 平方 | $x\ne0\Rightarrow x\cdot x>0$；特别地 $1>0$ |
| (e) 取平方 | 对 $x\ge0$，$y\ge0$：$x^2\ge y^2\Leftrightarrow x\ge y$ |
:::

⁠**如何理解：**不等式经得起任何加法，但只经得起乘以正数。当 $z<0$ 时它反向：$x<y\wedge z<0\Rightarrow xz>yz$。当 $z=0$ 时，(O4) 变为 $0<0$，这是假的。若有序域中存在 $i$ 使 $i\cdot i=-1$，由 (d) 就有 $-1>0$ 和 $1>0$，再由 (T2) 得 $0>0$。所以[第 2 部分](/wissen/zh/elektrotechnik/1-semester/hohere-mathematik-1/komplexe-zahlen/komplexe-zahlen.html)的复数无法定序。也可以等价地用 (O1) 到 (O4) 代替 (T1) 到 (T3) 作为公理。

:::frage 不等式可以平方吗？
只有两边都不为负时才行，这就是 (e)。没有这个前提：$-3<2$，但 $9>4$。平方把直线的负半部分反射到正半部分，就像图 [4](#abb-4) 中的乘 $-1$。
:::

:::abbildung hm1/k1spiegel 4
参考模型 $x=-3<y=2$。乘 2 把直线从零点向外拉伸，顺序不变。乘 $-1$ 关于零点反射，顺序反转：$3>-2$。
:::

:::beweis 由 (T1) 到 (T3) 推出序的规则
(O1)：对 $x-y$ 用 (T1)。(O2)：由 (T2)，$(y-x)+(z-y)=z-x$ 是正数。(O3)：$(y+z)-(x+z)=y-x$。(O4)：由 (T3)，$(y-x)z>0$，再用 (AM) 得 $yz-xz>0$。(a)：$(-x)-(-y)=y-x$。(b)：由 (O3)，$x+u<y+u$ 且 $u+y<v+y$，再用 (O2)。

(c) “$\Leftarrow$”：当 $x,y>0$ 时这就是 (T3)。当 $x,y<0$ 时 $(-x)(-y)>0$，而 $(-x)(-y)=xy$。“$\Rightarrow$”用反证法：设 $xy>0$，但数对 $(x,y)$ 不属于右边两种情形。这时剩下四种情形。当 $x=0$ 或 $y=0$ 时 $xy=0$，与 (T1) 矛盾。当 $x<0<y$ 时，由 (O4) 得 $xy<0\cdot y=0$，与 $xy>0$ 矛盾。$y<0<x$ 时同理。(d)：当 $x\ne0$ 时，$x>0$ 或 $x<0$，由 (c) 得 $x\cdot x>0$。取 $x=1\ne0$ 得 $1>0$。

(e) “$\Leftarrow$”：$x=y$ 时无需证明。由 $x>y\ge0$，用 (O4) 并取 $z=x$ 和 $z=y$，得 $x\cdot x>y\cdot x\ge y\cdot y$。“$\Rightarrow$”用逆否命题：由 $0\le x<y$ 同样得 $x\cdot x\le x\cdot y<y\cdot y$。
:::

::::beispiel
当 $x\ne0$ 时，$x$ 为正当且仅当 $x^{-1}$ 为正，因为 $x\cdot x^{-1}=1>0$，再用 (c)。因此，解 $\frac1x>2$。当 $x>0$ 时可以乘以 $x$：$1>2x$，所以 $0<x<\frac12$。当 $x<0$ 时左边为负，无解。
::::

⁠**极限情况：**$x=\frac12$ 时得 $2>2$，这是假的，端点不属于解。

:::aufgabe 练习 5 ★★ 不等式
<span class="anker" id="aufg-5"></span>

<ol class="al">

<li>

由 (O4) 和 (a) 证明 $x<y\wedge z<0\Rightarrow xz>yz$。

</li>

<li>

对哪些实数 $x\ne1$ 有 $\frac3{x-1}>1$？分两种情形讨论。

</li>

</ol>

:::loesung
(a) 由 $z<0$ 得 $-z>0$，由 (O4) 得 $-xz<-yz$，由 (a) 得 $yz<xz$。 (b) 情形 $x>1$：乘以 $x-1>0$ 得 $3>x-1$，所以 $1<x<4$。情形 $x<1$：左边为负，无解。结果：$1<x<4$。
:::
:::
