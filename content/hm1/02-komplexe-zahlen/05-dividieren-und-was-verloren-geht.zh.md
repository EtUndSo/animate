---
title: 第 4 阶段：除法，以及失去了什么
pfad: 电气工程 / 第 1 学期 / HöMa1 – 高等数学 1 / 复数
adresse: elektrotechnik/1-semester/hohere-mathematik-1/komplexe-zahlen
knoten: 第 2 章：复数
order: 1220500
summary: 第 3 阶段给出了一个实数乘积。本阶段由此得到除法，证明 mathbb C 是一个域，并解释为什么没有序。
tags: 
lang: zh
---

<span class="anker" id="stufe-4"></span>

:::zweck
第 [3](spiegeln-an-der-reellen-achse.html#stufe-3) 阶段给出了一个实数乘积。本阶段由此得到除法，证明 $\mathbb{C}$ 是一个域，并解释为什么没有序。
:::

**基本思路。** 除以实数是可行的：实部和虚部分别相除。所以把分数的分子分母同乘分母的共轭复数。分数的值不变，分母变为实数。在平面上，$1/z$ 分两步得到：先关于实轴作镜像，再除以 $x^2+y^2$（图 [4](#abb-4)）。交流电路计算正是这样把复阻抗构成的分式分解为实部和虚部的。

:::abbildung hm1/k2kehrwert 4
分两步得到 $z_2$ 的倒数：镜像，再除以 5。倒数位于 $\overline{z_2}$ 的箭头上。
:::

:::satz 定理 4.1 (倒数与除法)
<span class="anker" id="satz-4-1"></span>

对每个 $z=x+\mathrm{i}y\ne0$，存在数

<span class="anker" id="gl-4-1"></span>
$$z^{-1}=\frac1z=\frac{\overline{z}}{z\overline{z}}=\frac{x}{x^2+y^2}-\mathrm{i}\,\frac{y}{x^2+y^2}\qquad\text{满足}\qquad z\cdot z^{-1}=1. \tag{4.1}$$

于是对任意 $w$ 有 $\dfrac wz=w\cdot z^{-1}=\dfrac{w\,\overline{z}}{x^2+y^2}$。
:::

⁠**如何理解：**分母 $x^2+y^2$ 是实数。**适用条件：**由 $z\ne0$ 知 $x\ne0$ 或 $y\ne0$，所以 $x^2+y^2>0$。$z=0$ 没有倒数，因为对每个 $w$ 都有 $0\cdot w=0\ne1$。**极限情况：**当 $y=0$ 时，式 [(4.1)](#gl-4-1) 变为实数的倒数 $x/x^2=1/x$。

:::beweis 与倒数的乘积
设 $N:=x^2+y^2>0$。倒数是数对 $(x/N,\,-y/N)$。由式 [(1.2)](paare-statt-einzelner-zahlen.html#gl-1-2) 得

$$(x,y)\odot\Bigl(\frac xN,\frac{-y}N\Bigr)=\Bigl(\frac{x\cdot x}N-\frac{y\cdot(-y)}N,\;\frac{x\cdot(-y)}N+\frac{y\cdot x}N\Bigr)=\Bigl(\frac{x^2+y^2}N,\;0\Bigr)=(1,0).$$
:::

::::beispiel
用参考模型，分母为 $z_2\overline{z_2}=5$：

$$\frac{z_1}{z_2}=\frac{(3+\mathrm{i})(1-2\mathrm{i})}{(1+2\mathrm{i})(1-2\mathrm{i})}=\frac{3-6\mathrm{i}+\mathrm{i}-2\mathrm{i}^2}{5}=\frac{5-5\mathrm{i}}{5}=1-\mathrm{i}.$$

检验：$(1-\mathrm{i})(1+2\mathrm{i})=1+2\mathrm{i}-\mathrm{i}-2\mathrm{i}^2=3+\mathrm{i}$。此外，$1/z_2=(1-2\mathrm{i})/5=0.2-0.4\mathrm{i}$，$1/\mathrm{i}=-\mathrm{i}$。
::::

:::satz 定理 4.2 ($\mathbb{C}$ 是域)
<span class="anker" id="satz-4-2"></span>

$\mathbb{C}$ 连同 $+$ 和 $\cdot$ 满足[第 1 章](/wissen/zh/elektrotechnik/1-semester/hohere-mathematik-1/mengen-logik-und-reelle-zahlen/mengen-logik-und-reelle-zahlen.html)的所有域公理：交换律、结合律和分配律，中性元 $0\ne1$，每个 $z$ 有相反数 $-z$，每个 $z\ne0$ 有倒数 $1/z$。
:::

⁠**如何理解：**[第 1 章](/wissen/zh/elektrotechnik/1-semester/hohere-mathematik-1/mengen-logik-und-reelle-zahlen/mengen-logik-und-reelle-zahlen.html)中仅由域公理得出的结论在 $\mathbb{C}$ 中同样成立：分数运算、二项式公式，以及由 $zw=0$ 推出 $z=0$ 或 $w=0$。

:::beweis 思路
加法分别进行，从 $\mathbb{R}$ 继承全部法则，其中 $-z=-x-\mathrm{i}y$。式 [(1.2)](paare-statt-einzelner-zahlen.html#gl-1-2) 在交换下标 1 和 2 时不变：乘法是可交换的。结合律和分配律通过按式 [(1.2)](paare-statt-einzelner-zahlen.html#gl-1-2) 计算等式两边来证明。$(1,0)\odot(x,y)=(x,y)$ 说明单位元，式 [(4.1)](#gl-4-1) 说明公理 (M4)，即倒数。
:::

:::satz 定理 4.3 ($\mathbb{C}$ 不是有序的)
<span class="anker" id="satz-4-3"></span>

$\mathbb{C}$ 上不存在满足[第 1 章](/wissen/zh/elektrotechnik/1-semester/hohere-mathematik-1/mengen-logik-und-reelle-zahlen/mengen-logik-und-reelle-zahlen.html)序公理的关系“$>0$”：(T1) 对每个 $x$，$x>0$、$x=0$、$-x>0$ 中恰有一个成立。(T2) 由 $x>0$ 和 $y>0$ 推出 $x+y>0$。(T3) 由 $x>0$ 和 $y>0$ 推出 $x\cdot y>0$。
:::

⁠**如何理解：**对非实数，$z<w$ 和 $z>0$ 没有意义。只能比较 $\operatorname{Re}(z)$ 或 $|z|$ 这样的实数量。

:::beweis 反证
假设存在这样的关系。那么对每个 $x\ne0$ 都有 $x\cdot x>0$：当 $x>0$ 时由 (T3) 得出，当 $-x>0$ 时由 (T3) 和 $(-x)(-x)=x\cdot x$ 得出。特别地，$1\cdot1>0$ 且 $\mathrm{i}\cdot\mathrm{i}>0$。由 (T2) 得 $1\cdot1+\mathrm{i}\cdot\mathrm{i}>0$。这就是 $1+(-1)=0>0$，与 (T1) 矛盾。
:::

:::frage 能不能规定一个次序，比如先按实部、再按虚部？
这样排序是可以的。只是它与乘法不相容：它会给出 $\mathrm{i}>0$，但 $\mathrm{i}\cdot\mathrm{i}=-1<0$，违反 (T3)。上面的证明说明，任何规定都逃不过这一点。
:::

:::aufgabe 练习 4 ★ 除法
<span class="anker" id="aufg-4"></span>

(a) 把 $\dfrac{7+\mathrm{i}}{2-\mathrm{i}}$ 化为代数形式。(b) 计算 $\dfrac{10}{1+3\mathrm{i}}+\dfrac{3-\mathrm{i}}{1+\mathrm{i}}$。(c) 解 $(2+\mathrm{i})z-3=-2+3\mathrm{i}$ 并检验。

:::loesung
(a) $\dfrac{(7+\mathrm{i})(2+\mathrm{i})}{(2-\mathrm{i})(2+\mathrm{i})}=\dfrac{14+7\mathrm{i}+2\mathrm{i}+\mathrm{i}^2}{5}=\dfrac{13+9\mathrm{i}}5=2.6+1.8\mathrm{i}$。

(b) $\dfrac{10(1-3\mathrm{i})}{10}=1-3\mathrm{i}$，$\dfrac{(3-\mathrm{i})(1-\mathrm{i})}{2}=\dfrac{3-3\mathrm{i}-\mathrm{i}+\mathrm{i}^2}2=\dfrac{2-4\mathrm{i}}2=1-2\mathrm{i}$。和为 $2-5\mathrm{i}$。

(c) $(2+\mathrm{i})z=1+3\mathrm{i}$，所以 $z=\dfrac{(1+3\mathrm{i})(2-\mathrm{i})}{5}=\dfrac{2-\mathrm{i}+6\mathrm{i}-3\mathrm{i}^2}5=\dfrac{5+5\mathrm{i}}5=1+\mathrm{i}$。检验：$(2+\mathrm{i})(1+\mathrm{i})-3=1+3\mathrm{i}-3=-2+3\mathrm{i}$。
:::
:::

:::aufgabe 练习 5 ★★ 给 $\mathbb{C}$ 定序的一次尝试
<span class="anker" id="aufg-5"></span>

有人规定：当 $\operatorname{Re}(z)>0$ 时称 $z$ 为正。检查 (T1)、(T2) 和 (T3)，并为每条被违反的公理举出反例。

:::loesung
(T1) 不成立：对 $\mathrm{i}$ 有 $\operatorname{Re}(\mathrm{i})=0$ 和 $\operatorname{Re}(-\mathrm{i})=0$，所以 $\mathrm{i}$ 和 $-\mathrm{i}$ 都不是正的，尽管 $\mathrm{i}\ne0$。(T2) 成立，因为由第 [3](spiegeln-an-der-reellen-achse.html#stufe-3) 阶段有 $\operatorname{Re}(z+w)=\operatorname{Re}(z)+\operatorname{Re}(w)>0$。(T3) 不成立：$z=1+2\mathrm{i}$ 是正的，但 $z\cdot z=-3+4\mathrm{i}$ 的实部为 $-3$。原因在于乘积实部中的项 $-y_1y_2$。
:::
:::
