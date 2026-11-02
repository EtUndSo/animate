---
title: 第 1 阶段：用数对代替单个的数
pfad: 电气工程 / 第 1 学期 / 高等数学 1 / 复数
order: 1220200
summary: 在 mathbb R 中 x 2=-1 无解。本阶段构造一个更大的数集，方程在其中有解，并且 mathbb R 原样包含在内。
tags: 代数形式
lang: zh
---

<span class="anker" id="stufe-1"></span>

:::zweck
在 $\mathbb{R}$ 中 $x^2=-1$ 无解。本阶段构造一个更大的数集，方程在其中有解，并且 $\mathbb{R}$ 原样包含在内。
:::

**基本思路。** 每一次数的扩充都解决一个此前无解的方程：$x+1=0$ 从 $\mathbb{N}$ 通向 $\mathbb{Z}$，$2x=1$ 从 $\mathbb{Z}$ 通向 $\mathbb{Q}$，$x^2=2$ 从 $\mathbb{Q}$ 通向 $\mathbb{R}$。而 $x^2=-1$ 的情况不同。抛物线 $y=x^2$ 永远到不了高度 $-1$（图 [1](#abb-1)），因为在 $\mathbb{R}$ 中 $x^2\ge0$（[第 1 部分](/wissen/zh/elektrotechnik/1-semester/hohere-mathematik-1/mengen-logik-und-reelle-zahlen/mengen-logik-und-reelle-zahlen.html)）。这里不是像 $\sqrt2$ 那样在其他点之间缺一个点，而是数轴上的每个点都被排除了。解必须位于直线之外。因此要增加第二个坐标：用数对 $(x,y)$ 来运算。数对 $(x,0)$ 应仍是实数，而 $(0,1)$ 的平方应为 $(-1,0)$。

:::abbildung hm1/k2parabel 1
直线 $y=2$ 与抛物线相交两次，解 $\pm\sqrt2$ 位于数轴上。直线 $y=-1$ 与它永不相交：没有实数 $x$ 能满足 $x^2=-1$。
:::

:::definition 定义 1.1 (复数)
<span class="anker" id="satz-1-1"></span>

复数集为 $\mathbb{C}:=\{(x,y):x,y\in\mathbb{R}\}$，其加法 $\oplus$ 和乘法 $\odot$ 为：

<span class="anker" id="gl-1-1"></span>
<span class="anker" id="gl-1-2"></span>
$$\begin{aligned} (x_1,y_1)\oplus(x_2,y_2)&:=(x_1+x_2,\;y_1+y_2),\\ (x_1,y_1)\odot(x_2,y_2)&:=(x_1x_2-y_1y_2,\;x_1y_2+x_2y_1). \end{aligned} \tag{1.1|1.2}$$

零元为 $(0,0)$，单位元为 $(1,0)$，虚数单位为 $\mathrm{i}:=(0,1)$。
:::

⁠**如何理解：**$x$ 和 $y$ 是没有单位的实数，$\oplus$ 和 $\odot$ 是数对的新运算。**极限情况：**当 $y_1=y_2=0$ 时，式 [(1.1)](#gl-1-1) 和式 [(1.2)](#gl-1-2) 给出数对 $(x_1+x_2,0)$ 和 $(x_1x_2,0)$。所以数对 $(x,0)$ 的运算与实数 $x$ 完全相同。因此写 $x$ 代替 $(x,0)$，写 $+$ 代替 $\oplus$，写 $\cdot$ 代替 $\odot$，并有 $\mathbb{R}\subset\mathbb{C}$。

:::satz 定理 1.2 (虚数单位与代数形式)
<span class="anker" id="satz-1-2"></span>

<ol class="rm">

<li>

有 $\mathrm{i}^2=-1$。

</li>

<li>

每个复数都有唯一的__代数形式__ $z=x+\mathrm{i}y$，其中 $x,y\in\mathbb{R}$。

</li>

<li>

在代数形式下，$(x_1+\mathrm{i}y_1)+(x_2+\mathrm{i}y_2)=(x_1+x_2)+\mathrm{i}(y_1+y_2)$，并且

</li>

</ol>

<span class="anker" id="gl-1-3"></span>
$$(x_1+\mathrm{i}y_1)(x_2+\mathrm{i}y_2)=(x_1x_2-y_1y_2)+\mathrm{i}(x_1y_2+x_2y_1). \tag{1.3}$$
:::

⁠**如何理解：**公式 [(1.3)](#gl-1-3) 无需死记：展开括号，代入 $\mathrm{i}^2=-1$，再整理。$x_1x_2-y_1y_2$ 中的减号就是 $\mathrm{i}^2$。数学中虚数单位记作 $\mathrm{i}$，电气工程中记作 $\mathrm{j}$，因为那里 $i$ 表示电流。本章使用正体的 $\mathrm{i}$。**适用条件：**$x$ 和 $y$ 必须是实数。否则表示法不唯一：$\mathrm{i}=\mathrm{i}+\mathrm{i}\cdot0=0+\mathrm{i}\cdot1$。

:::beweis 用数对运算
(i) 由式 [(1.2)](#gl-1-2)，$\mathrm{i}\cdot\mathrm{i}=(0,1)\odot(0,1)=(0\cdot0-1\cdot1,\;0\cdot1+0\cdot1)=(-1,0)=-1$。

(ii) 对实数 $y$，$\mathrm{i}y=(0,1)\odot(y,0)=(0\cdot y-1\cdot0,\;0\cdot0+y\cdot1)=(0,y)$，所以 $x+\mathrm{i}y=(x,0)\oplus(0,y)=(x,y)$。数对唯一确定 $x$ 和 $y$。

(iii) 由 (ii)，等式右边正是式 [(1.1)](#gl-1-1) 和式 [(1.2)](#gl-1-2) 中的数对。
:::

**例。** 参考模型的和与积：

$$z_1+z_2=(3+1)+\mathrm{i}(1+2)=4+3\mathrm{i},\qquad z_1z_2=(3+\mathrm{i})(1+2\mathrm{i})=3+6\mathrm{i}+\mathrm{i}+2\mathrm{i}^2=1+7\mathrm{i}.$$

数对公式 [(1.2)](#gl-1-2) 给出同样的结果：$(3\cdot1-1\cdot2,\;3\cdot2+1\cdot1)=(1,7)$。$\mathrm{i}$ 的幂以 4 为周期重复：$\mathrm{i}^1=\mathrm{i}$，$\mathrm{i}^2=-1$，$\mathrm{i}^3=-\mathrm{i}$，$\mathrm{i}^4=1$。所以只有 $n$ 除以 4 的余数起作用，例如 $\mathrm{i}^{10}=\mathrm{i}^8\,\mathrm{i}^2=-1$。

:::frage $\mathrm{i}$ 真的存在吗，还是只是一种计算技巧？
在数轴上确实没有 $\mathrm{i}$，这一点疑虑是对的。但 $\mathrm{i}$ 是数对 $(0,1)$，而式 [(1.2)](#gl-1-2) 是关于数对的明确规则。“虚”只是一个历史名称。
:::

:::aufgabe 练习 1 ★ 代数形式下的运算
<span class="anker" id="aufg-1"></span>

化为 $x+\mathrm{i}y$ 的形式：(a) $(4-\mathrm{i})(2+3\mathrm{i})$，(b) $(1+\mathrm{i})^2$，并由此求 $(1+\mathrm{i})^4$，(c) $\mathrm{i}^{27}+\mathrm{i}^{42}$。

:::loesung
(a) $8+12\mathrm{i}-2\mathrm{i}-3\mathrm{i}^2=11+10\mathrm{i}$。(b) $(1+\mathrm{i})^2=1+2\mathrm{i}+\mathrm{i}^2=2\mathrm{i}$，所以 $(1+\mathrm{i})^4=(2\mathrm{i})^2=-4$。(c) 由 $27=4\cdot6+3$ 得 $\mathrm{i}^{27}=\mathrm{i}^3=-\mathrm{i}$，由 $42=4\cdot10+2$ 得 $\mathrm{i}^{42}=\mathrm{i}^2=-1$。和为 $-1-\mathrm{i}$。
:::
:::
