---
title: 第 9 阶段：基本不等式
pfad: 电气工程 / 第 1 学期 / 高等数学 1 / 集合、逻辑与实数
order: 1211100
summary: 一个表达式常常算不出来，只能估计。本阶段提供五个标准估计。
tags: 伯努利, 杨氏, 均值, 几何平均, 算术平均, 柯西-施瓦茨, 闵可夫斯基, 向量
lang: zh
---

<span class="anker" id="stufe-9"></span>

:::zweck
一个表达式常常算不出来，只能估计。本阶段提供五个标准估计。
:::

**基本思路。** 几乎一切都来自一个事实：平方不为负。把 $(a-b)^2\ge0$ 展开，就得到 $2ab\le a^2+b^2$。杨氏不等式、均值不等式和柯西-施瓦茨不等式都是这一行的巧妙改写。只有伯努利不等式需要归纳法。

:::satz 定理 9.1 (五个不等式)
<span class="anker" id="satz-9-1"></span>

在 $\mathbb{R}$ 中有：

<ol class="rm">

<li>

__伯努利__：对 $x>-1$，$x\ne0$ 和 $n\ge2$，有 $(1+x)^n>1+nx$。

</li>

<li>

__杨氏__：对 $\varepsilon>0$ 和 $x,y\in\mathbb{R}$，有 $|xy|\le\frac\varepsilon2x^2+\frac1{2\varepsilon}y^2$。

</li>

<li>

__均值__：对 $x,y\ge0$，有 $\sqrt{xy}\le\frac{x+y}2$。左边是__几何平均__，右边是__算术平均__。

</li>

<li>

__柯西-施瓦茨__：对 $x_1,\dots,x_n,y_1,\dots,y_n\in\mathbb{R}$，记 $\|\vec x\|:=\sqrt{\sum_{i=1}^nx_i^2}\ge0$，有

<span class="anker" id="gl-9-1"></span>
$$\sum_{i=1}^n|x_iy_i|\le\sqrt{\sum_{i=1}^nx_i^2}\cdot\sqrt{\sum_{i=1}^ny_i^2}=\|\vec x\|\cdot\|\vec y\|. \tag{9.1}$$

</li>

<li>

__闵可夫斯基__：记 $\vec x+\vec y:=(x_1+y_1,\dots,x_n+y_n)$，有

<span class="anker" id="gl-9-2"></span>
$$\sqrt{\sum_{i=1}^n(x_i+y_i)^2}\le\sqrt{\sum_{i=1}^nx_i^2}+\sqrt{\sum_{i=1}^ny_i^2},\quad\text{即}\quad\|\vec x+\vec y\|\le\|\vec x\|+\|\vec y\|. \tag{9.2}$$

</li>

</ol>
:::

⁠**如何理解：**$\vec x=(x_1,\dots,x_n)$ 是一个__向量__，即一列 $n$ 个数，$\|\vec x\|$ 是它的__范数__。当 $n=2$ 时，由勾股定理，这就是从原点到点 $(x_1,x_2)$ 的箭头的长度。于是式 [(9.2)](#gl-9-2) 就是箭头的三角不等式，而在第 8 部分，式 [(9.1)](#gl-9-1) 将引出内积。在杨氏不等式中，$\varepsilon$ 是一种汇率：一个小的 $x$ 项要用一个大的 $y$ 项来换。**为什么需要这些前提：**伯努利：$x=-4$，$n=3$ 给出 $-27>-11$，这是假的，所以需要 $x>-1$。$x=0$ 或 $n=1$ 时等号成立。均值：$x=y=-1$ 给出 $1\le-1$，这是假的。杨氏：$\varepsilon=-1$ 使右边为负。

:::abbildung hm1/k1mittel 9
左图：用半圆表示均值，半径是算术平均，分点上方的高是几何平均。高决不大于半径。右图：$n=3$ 时的伯努利不等式，直线在 $x=0$ 处与曲线相切，当 $x>-1$ 时位于曲线下方。
:::

:::beweis 五个不等式
⁠**伯努利**，从 $n_0=2$ 开始归纳。基础：$(1+x)^2=1+2x+x^2>1+2x$，因为由定理 [4.2](anordnungsaxiome.html#satz-4-2) (d)，$x^2>0$。步骤：因为 $1+x>0$，由 (O4) 可以把归纳假设乘以 $1+x$：$(1+x)^{n+1}>(1+nx)(1+x)=1+(n+1)x+nx^2>1+(n+1)x$。

⁠**杨氏。**由定理 [7.2](intervallschachtelung-und-wurzeln.html#satz-7-2)，$\sqrt\varepsilon$ 存在，且 $\sqrt\varepsilon>0$。平方不为负：

$$0\le\Bigl(\sqrt\varepsilon\,x\pm\frac1{\sqrt\varepsilon}\,y\Bigr)^2=\varepsilon x^2\pm2xy+\frac1\varepsilon y^2.$$

这给出 $\mp2xy\le\varepsilon x^2+\frac1\varepsilon y^2$。因为 $|xy|=\max\{xy,-xy\}$，除以 2 后即得断言。

⁠**均值。**对 $\sqrt x$ 和 $\sqrt y$ 用 $\varepsilon=1$ 的杨氏不等式：$\sqrt x\sqrt y\le\frac12x+\frac12y$，而 $\sqrt x\sqrt y=\sqrt{xy}$。

⁠**柯西-施瓦茨。**若所有 $x_i=0$ 或所有 $y_i=0$，则是 $0\le0$。否则 $\|\vec x\|>0$，$\|\vec y\|>0$，令 $\xi_i:=x_i/\|\vec x\|$，$\eta_i:=y_i/\|\vec y\|$。把式 [(9.1)](#gl-9-1) 除以 $\|\vec x\|\|\vec y\|$，只需证 $\sum_{i=1}^n|\xi_i\eta_i|\le1$。有 $\sum_i\xi_i^2=\frac1{\|\vec x\|^2}\sum_ix_i^2=1$，同样 $\sum_i\eta_i^2=1$。对 $\xi_i^2$、$\eta_i^2$ 用均值不等式，

$$\sum_{i=1}^n|\xi_i\eta_i|=\sum_{i=1}^n\sqrt{\xi_i^2\eta_i^2}\le\sum_{i=1}^n\frac{\xi_i^2+\eta_i^2}2=\frac12+\frac12=1.$$

⁠**闵可夫斯基。**设 $s_i:=x_i+y_i$，即 $\vec s=\vec x+\vec y$。依次用 (AM)、$a\le|a|$，再对数组 $x_i,s_i$ 和 $y_i,s_i$ 用式 [(9.1)](#gl-9-1)：

$$\|\vec s\|^2=\sum_ix_is_i+\sum_iy_is_i\le\sum_i|x_is_i|+\sum_i|y_is_i|\le\bigl(\|\vec x\|+\|\vec y\|\bigr)\|\vec s\|.$$

当 $\|\vec s\|=0$ 时，式 [(9.2)](#gl-9-2) 左边为 0。否则除以 $\|\vec s\|$。
:::

::::beispiel
伯努利：$1.01^{10}>1.1$，精确值 $1.1046$。当 $x$ 很小时，$1+nx$ 是很好的近似：电阻上的电压增加 1 %，功率约增加 2 %，精确值是 2.01 %。当 $x$ 很大时它很粗糙：$2^{10}=1024$ 对 11。杨氏，取 $x=2$，$y=8$：$\varepsilon=1$ 时是 $16\le34$，$\varepsilon=4$ 时是 $16\le16$。柯西-施瓦茨，取 $\vec x=(3,4)$，$\vec y=(1,2)$：$3+8=11\le5\sqrt5\approx11.18$。闵可夫斯基：$\|(4,6)\|=\sqrt{52}\approx7.21\le5+\sqrt5\approx7.24$。
::::

⁠**极限情况：**$x=y$ 时两个平均相等，半圆中的高正好在圆心上。

:::frage 什么时候用哪个不等式？
接近 1 的数的幂：伯努利。估计乘积：杨氏、均值。乘积之和：柯西-施瓦茨。和的平方根：闵可夫斯基。
:::

:::aufgabe 练习 10 ★★★ 估计
<span class="anker" id="aufg-10"></span>

<ol class="al">

<li>

证明 $2^{n-1}\ge n$ 对所有 $n\in\mathbb{N}$ 成立。（第 [7](intervallschachtelung-und-wurzeln.html#stufe-7) 阶段要用到这个不等式。）

</li>

<li>

从下方估计 $0.995^{20}$，并与精确值比较。

</li>

<li>

一个矩形的面积为 16。用均值不等式证明周长至少为 16。边长为多少时等号成立？

</li>

<li>

对 $\vec x=(1,2,2)$，$\vec y=(2,-1,2)$ 检验柯西-施瓦茨不等式和闵可夫斯基不等式。

</li>

<li>

证明：对 $\vec y=t\,\vec x$，$t\in\mathbb{R}$，式 [(9.1)](#gl-9-1) 中等号成立。

</li>

</ol>

:::loesung
(a) 对 $n=1,2$ 是 $1\ge1$ 和 $2\ge2$。对 $n\ge3$，由伯努利不等式，$2^{n-1}=(1+1)^{n-1}>1+(n-1)=n$。 (b) $x=-0.005$，$n=20$：$0.995^{20}>1-0.1=0.9$。精确值 $0.9046$，这个下界比它低 0.5 %。 (c) 边长 $a,b>0$，$ab=16$：周长 $2(a+b)\ge2\cdot2\sqrt{ab}=16$。$a=b=4$ 时等号成立，即正方形。 (d) $\|\vec x\|=\sqrt{1+4+4}=3$，$\|\vec y\|=\sqrt{4+1+4}=3$。柯西-施瓦茨：$2+2+4=8\le9$。闵可夫斯基：$\vec x+\vec y=(3,1,4)$，$\|\vec x+\vec y\|=\sqrt{26}\approx5.10\le6$。 (e) $\sum_i|x_i\cdot tx_i|=|t|\sum_ix_i^2=|t|\,\|\vec x\|^2$。右边：$\|t\vec x\|=\sqrt{t^2\sum_ix_i^2}=|t|\,\|\vec x\|$，所以 $\|\vec x\|\,\|\vec y\|=|t|\,\|\vec x\|^2$。
:::
:::
