---
title: 第 8 阶段：距离与绝对值
pfad: 电气工程 / 第 1 学期 / 高等数学 1 / 集合、逻辑与实数
order: 1211000
summary: 极限衡量两个数有多接近。为此需要距离，以及一条关于绕路的规则。
tags: 距离, 绝对值, 三角不等式, 反向三角不等式
lang: zh
---

<span class="anker" id="stufe-8"></span>

:::zweck
极限衡量两个数有多接近。为此需要距离，以及一条关于绕路的规则。
:::

**基本思路。** 两个数之间的距离是直线上它们之间线段的长度。长度与方向无关，绕道第三个点决不会更短（图 [8](#abb-8)）。绝对值是到零的距离。

:::definition 定义 8.1 (距离与绝对值)
<span class="anker" id="satz-8-1"></span>

对 $x,y\in\mathbb{R}$，

<span class="anker" id="gl-8-1"></span>
$$d(x,y):=\begin{cases}x-y,&x\ge y\\y-x,&x<y\end{cases}\qquad\text{和}\qquad|x|:=d(x,0)=\begin{cases}x,&x\ge0\\-x,&x<0\end{cases} \tag{8.1}$$

分别称为 $x$ 与 $y$ 的__距离__和 $x$ 的__绝对值__。
:::

⁠**如何理解：**$d$ 取自英文 distance。由定义得

<span class="anker" id="gl-8-2"></span>
$$d(x,y)=d(x-y,0)=|x-y|,\ \ -|x|\le x\le|x|,\ \ |x|=\max\{x,-x\},\ \ -|x|=\min\{x,-x\}. \tag{8.2}$$

在参考模型中，$|x|=3$，$|y|=5$，$d(x,y)=|{-3}-5|=8$。式 [(8.1)](#gl-8-1) 中的负号有迷惑性：当 $x<0$ 时 $-x$ 是正数，绝对值决不为负。带公差的值这样写：$|U-5\,\mathrm V|\le0.1\,\mathrm V$ 表示 $U$ 在 4.9 V 和 5.1 V 之间。

:::satz 定理 8.2 (距离与绝对值的性质)
<span class="anker" id="satz-8-2"></span>

对所有 $x,y,z\in\mathbb{R}$ 有：

|  | 距离 | 绝对值 |
|---|---|---|
| 正性 | $d(x,y)\ge0$ | $\vert x\vert \ge0$ |
| 定性 | $d(x,y)=0\Leftrightarrow x=y$ | $\vert x\vert =0\Leftrightarrow x=0$ |
| 对称性、乘积 | $d(x,y)=d(y,x)$ | $\vert xy\vert =\vert x\vert \vert y\vert $；对 $z\ne0$：$\vert x/z\vert =\vert x\vert /\vert z\vert $ |
| __三角不等式__ | $d(x,y)\le d(x,z)+d(z,y)$ | $\vert x+y\vert \le\vert x\vert +\vert y\vert $ |

此外还有 $|x-y|\le|x|+|y|$、__反向三角不等式__ $\bigl||x|-|y|\bigr|\le|x\pm y|$ 和 $|x|=\sqrt{x^2}$。
:::

⁠**如何理解：**三角不等式从上方估计和，反向三角不等式从下方估计。

:::frage 为什么 $|x+y|=|x|+|y|$ 不成立？
只有同号或者有一项为零时它才成立。异号时两项部分抵消：$|-3+5|=2<8$。最坏的情况下两个误差相加，这就是不等式所说的。
:::

:::abbildung hm1/k1betrag 8
参考模型 $x=-3$，$y=5$。直接走，$d(x,y)=8$。绕道 $z=7$ 得 $10+2=12$。对 $x$ 和 $y$ 之间的每个 $z$，例如 $z=1$，恰好得 8（$4+4$）。
:::

:::beweis 三角不等式及其推论
定性和对称性见式 [(8.1)](#gl-8-1)。**$d$ 的三角不等式。**不失一般性（简称“不妨设”：其余情形通过改名可化为这一情形），设 $x<y$；$x=y$ 时左边为 0。$z=x$ 或 $z=y$ 时有一项为 0，不等式成为等式。剩下三种情形。$x<y<z$：$d(x,z)+d(z,y)=2z-x-y>2y-x-y=y-x$。$x<z<y$：和恰好是 $y-x$。$z<x<y$：和是 $x+y-2z>x+y-2x=y-x$。

⁠**乘积。**若 $xy=0$，由定理 [3.2](korperaxiome.html#satz-3-2) (v) 两边都是 0。若 $xy>0$，由定理 [4.2](anordnungsaxiome.html#satz-4-2) (c)，$x$、$y$ 同号，$|x||y|$ 是 $xy$ 或 $(-x)(-y)$，两者都是 $xy$。$xy<0$ 同理。对商：$z\cdot\frac xz=x$ 给出 $|z|\,|\frac xz|=|x|$。

⁠**绝对值。**$|x+y|=|x-(-y)|=d(x,-y)\le d(x,0)+d(0,-y)=|x|+|y|$，因为 $|-y|=|y|$。用 $-y$ 代替 $y$ 得 $|x-y|\le|x|+|y|$。

⁠**反向三角不等式。**$|x|=|(x-y)+y|\le|x-y|+|y|$，所以 $|x|-|y|\le|x-y|$。交换 $x$ 和 $y$ 也有 $|y|-|x|\le|x-y|$。由式 [(8.2)](#gl-8-2)，两者的最大值是 $\bigl||x|-|y|\bigr|$。用 $-y$ 代替 $y$ 得带 $+$ 号的形式。

⁠**平方根。**$|x|\ge0$ 且 $|x|^2=x^2$，所以 $|x|$ 是 $z^2=x^2$ 唯一的非负解。
:::

::::beispiel
取 $x=-3$，$y=5$：$|x+y|=2\le8=|x|+|y|$，$\bigl||x|-|y|\bigr|=2\le|x+y|=2$。
::::

⁠**极限情况** $y=0$：所有不等式都变为 $|x|=|x|$。

:::aufgabe 练习 9 ★★ 绝对值不等式
<span class="anker" id="aufg-9"></span>

<ol class="al">

<li>

把 $\{x\in\mathbb{R}:|x-2|\le3\}$ 写成区间。

</li>

<li>

在 $x=-1$ 和 $x=2$ 处分情形求解 $|x-2|+|x+1|\le5$。

</li>

<li>

两个电压满足 $|U_1-5\,\mathrm V|\le0.1\,\mathrm V$，$|U_2-3\,\mathrm V|\le0.2\,\mathrm V$。$U_1+U_2$ 与 8 V 最多相差多少？给出达到这个值的一对电压。

</li>

</ol>

:::loesung
(a) $-3\le x-2\le3$，所以是 $[-1,5]$。 (b) 对 $x\ge2$：$2x-1\le5$，所以 $2\le x\le3$。对 $-1\le x<2$：$(2-x)+(x+1)=3\le5$，恒成立。对 $x<-1$：$1-2x\le5$，所以 $-2\le x<-1$。合起来：$[-2,3]$。 (c) $|(U_1+U_2)-8\,\mathrm V|\le|U_1-5\,\mathrm V|+|U_2-3\,\mathrm V|\le0.3\,\mathrm V$。在 $U_1=5.1\,\mathrm V$，$U_2=3.2\,\mathrm V$ 时达到。
:::
:::
