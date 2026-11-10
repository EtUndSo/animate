---
title: 第 4 阶段：积分变成求和
pfad: 电气工程 / 第 3 学期 / ET3 – 电气工程基础 3：信号与系统 / 拉普拉斯变换
adresse: elektrotechnik/3-semester/signale-und-systeme/laplace-transformation
knoten: 第 2 章：拉普拉斯变换
order: 3220700
summary: 按字面意义理解那个猜想：对于系统理论几乎总在处理的那些信号，信号是复指数函数的 有限和 。极点就是指数。
tags: 部分分式展开, 稳定性, 自然响应
lang: zh
---

<span class="anker" id="stufe-4"></span>

:::zweck
按字面意义理解那个猜想：对于系统理论几乎总在处理的那些信号，信号是复指数函数的*有限和*。极点就是指数。
:::

**思路。** 对于由 $R$、$L$、$C$ 构成的网络，以及所有由微分方程描述的系统，$S(p)$ 是多项式之比。在单极点的情况下，__部分分式展开__把它写成

$$S(p)=A_0+\sum_{r=1}^{R}\frac{A_r}{p-p_r},\qquad A_r=\lim_{p\to p_r}(p-p_r)\,S(p).$$

每一项都是*单个基本分量*的变换：若收敛域位于极点右侧，由 [(2.2)](konvergenzbereich-welche-dampfungen-funktionieren.html#gl-2-2)，$A_r/(p-p_r)$ 对应 $A_r\,\mathrm{e}^{p_r t}\varepsilon(t)$；由 [(2.4)](konvergenzbereich-welche-dampfungen-funktionieren.html#gl-2-4)，常数项 $A_0$ 对应 $A_0\,\delta(t)$。因此，对于右边信号，

<span class="anker" id="gl-4-1"></span>
$$s(t)=A_0\,\delta(t)+\sum_{r=1}^{R}A_r\,\mathrm{e}^{p_r t}\,\varepsilon(t). \tag{4.1}$$

⁠**简而言之：**拉普拉斯变换为有理函数的右边信号，是基本分量 $\mathrm{e}^{p_r t}$ 的有限和。极点就是指数，部分分式系数就是权重。

这意味着，借助图 [1](warum-gerade.html#abb-1) 的地图，可以从极点读出任何这类信号：$\operatorname{Re} p_r$ 告诉你基本分量是衰减还是增长，$\operatorname{Im} p_r$ 告诉你它振荡得多快。一对共轭极点 $p_r,p_r^*$ 合起来给出一个实的衰减振荡。这也是__稳定性__的核心：因果基本分量 $\mathrm{e}^{p_r t}\varepsilon(t)$ 当且仅当 $\operatorname{Re} p_r<0$ 时衰减。因此，若 $H(p)$ 的所有极点都位于左半平面，因果系统就是稳定的。

**例。** 第 [3](aus-der-faltung-wird-eine-multiplikation.html#stufe-3) 阶段中的阶跃响应有极点 $0$ 和 $-1$：

$$g(t)=\underbrace{1\cdot\mathrm{e}^{0\cdot t}}_{\text{极点 $0$（来自 $S$）}}\;\underbrace{-\;1\cdot\mathrm{e}^{-t}}_{\text{极点 $-1$（来自 $H$）}}\qquad(t>0).$$

输入的极点给出由输入强制产生的部分（终值电压 1）。系统的极点给出 RC 电路的__自然响应__，即时间常数为 $RC=1$ s 的衰减。这一点普遍成立：输出 $G=SH$ 既包含输入的极点，也包含系统的极点。

:::zusatz 积分为什么会坍缩成求和：留数定理
本节需要用到复变函数中的留数定理。它解释了为什么 [(2.1)](der-trick-dampfen-zerlegen-zuruckmultiplizieren.html#gl-2-1) 与 [(4.1)](#gl-4-1) 是一回事，以及为什么收敛域决定信号。

设 $S(p)$ 是分子次数低于分母次数、且只有单极点的多项式之比。

<ul>

<li>

⁠**$t>0$：**用一个向*左*的大半圆把积分直线闭合。在那里 $\operatorname{Re} p\to-\infty$，因此 $|\mathrm{e}^{pt}|=\mathrm{e}^{\operatorname{Re} p\,t}\to0$，且 $S(p)\to0$。在极限下，半圆没有贡献（约当引理）。闭合路径沿逆时针方向，由留数定理得

$$s(t)=\sum_{\text{直线左侧的极点}}\operatorname*{Res}_{p=p_r}\bigl[S(p)\,\mathrm{e}^{pt}\bigr]=\sum_{\text{左侧}}A_r\,\mathrm{e}^{p_r t}.$$

单极点处的留数为 $\lim_{p\to p_r}(p-p_r)S(p)\mathrm{e}^{pt}=A_r\mathrm{e}^{p_rt}$：恰好就是部分分式系数。

</li>

<li>

⁠**$t<0$：**此时 $\mathrm{e}^{pt}$ 在 $\operatorname{Re} p\to+\infty$ 时趋于零。向*右*闭合；路径沿顺时针方向，因而出现一个负号：

$$s(t)=-\sum_{\text{直线右侧的极点}}A_r\,\mathrm{e}^{p_r t}.$$

</li>

</ul>

⁠**结论：**直线的位置，也就是收敛域，决定了哪些极点给出因果基本分量（直线左侧），哪些给出反因果基本分量（直线右侧）。例：$S(p)=\frac{1}{(p+1)(p+2)}=\frac{1}{p+1}-\frac{1}{p+2}$（图 [5](#abb-5)）。若直线位于两极点之间，$-2<\sigma<-1$，则 $-2$ 对 $t>0$ 起作用，$-1$ 对 $t<0$ 起作用：

$$s(t)=-\mathrm{e}^{-2t}\varepsilon(t)-\mathrm{e}^{-t}\varepsilon(-t).$$

在直线 $\sigma=-1.5/\mathrm s$ 上数值计算得：$s(1\,\mathrm{s})=-0.1353=-\mathrm{e}^{-2}$，$s(-1\,\mathrm{s})=-2.7183=-\mathrm{e}^{1}$。若直线位于两个极点的右侧，同一公式给出因果信号 $(\mathrm{e}^{-t}-\mathrm{e}^{-2t})\varepsilon(t)$；若位于两个极点的左侧，则给出反因果信号 $-(\mathrm{e}^{-t}-\mathrm{e}^{-2t})\varepsilon(-t)$。

:::abbildung et3/k2residuen 5
带状区域 $-2<\operatorname{Re} p<-1$（蓝色）中的积分直线 $\sigma=-1.5/\mathrm s$，以及将其闭合的半圆（红色）。
:::
:::

:::aufgabe 练习 7 ★★★ （拓展阅读）同一公式，两个信号
<span class="anker" id="aufg-7"></span>

$S(p)=\dfrac{1}{p+1}$。

<ol class="al">

<li>

收敛域为 $\operatorname{Re} p>-1$。用留数定理计算反演公式，分 $t>0$ 和 $t<0$ 两种情况。

</li>

<li>

对收敛域 $\operatorname{Re} p<-1$ 做同样的计算。

</li>

<li>

与基本变换对 [(2.2)](konvergenzbereich-welche-dampfungen-funktionieren.html#gl-2-2) 和 [(2.3)](konvergenzbereich-welche-dampfungen-funktionieren.html#gl-2-3) 比较。对于不给出收敛域的说法“$S(p)=1/(p+1)$”，你从中得到什么启示？

</li>

</ol>

:::loesung
(a) 直线位于极点右侧，例如 $\sigma=0$。$t>0$ 时向左闭合：极点 $-1$ 在内部，$\operatorname*{Res}_{p=-1}\frac{\mathrm{e}^{pt}}{p+1}=\mathrm{e}^{-t}$，因此 $s(t)=\mathrm{e}^{-t}$。$t<0$ 时向右闭合：直线右侧没有极点，因此 $s(t)=0$。合起来，$s(t)=\mathrm{e}^{-t}\varepsilon(t)$。

(b) 直线位于极点左侧，例如 $\sigma=-2$。$t>0$ 时向左闭合：没有极点，$s(t)=0$。$t<0$ 时向右闭合：极点在内部，路径为顺时针，$s(t)=-\mathrm{e}^{-t}$。合起来，$s(t)=-\mathrm{e}^{-t}\varepsilon(-t)$。

(c) 这恰好是 $p_0=-1$ 时的基本变换对 [(2.2)](konvergenzbereich-welche-dampfungen-funktionieren.html#gl-2-2) 和 [(2.3)](konvergenzbereich-welche-dampfungen-funktionieren.html#gl-2-3)。仅凭“$S(p)=1/(p+1)$”这一说法无法确定信号。只有给出收敛域，才能明确极点位于直线的哪一侧，以及它给出的是因果还是反因果基本分量。
:::
:::

:::frage 拉普拉斯变换背后是否不止“从代入特征函数的卷积积分得到 $H(p)$”这段计算，而是任意函数都可以写成复指数函数之和？
是的，这正是问题的核心。没有它，特征函数的那段计算只不过是个奇特的结论，因为它本身只对 $\mathrm{e}^{pt}$ 这一个信号成立。正是因为（几乎）每个信号都能由这样的基本分量（构件）组合而成，它才能对*每个*输入信号给出结论。以下三点细化使这一说法变得精确：

<ol>

<li>

一般来说，它不是求和，而是*积分*：无穷多个基本分量 $\mathrm{e}^{pt}$，每个都带有无穷小的权重。这些基本分量位于 $p$ 平面中的一条竖直线 $\operatorname{Re} p=\sigma$ 上（第 [2](ein-signal-aus-lauter-bausteinen.html#stufe-2) 阶段）。

</li>

<li>

并非任意函数都可以，而是存在收敛域的函数：它在时间轴每一侧至多按指数增长，并且必须有同一个衰减因子能同时抑制两侧（第 [2.3](konvergenzbereich-welche-dampfungen-funktionieren.html#stufe-2-3) 节）。

</li>

<li>

若 $S(p)$ 是多项式之比，积分确实会变成*有限和* $\sum_r A_r\,\mathrm{e}^{p_r t}$。指数 $p_r$ 就是 $S(p)$ 的极点（第 [4](#stufe-4) 阶段）。

</li>

</ol>
:::
