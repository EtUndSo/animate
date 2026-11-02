---
title: 第 5 阶段：绝对值与距离
pfad: 电气工程 / 第 1 学期 / 高等数学 1 / 复数
order: 1220600
summary: 复数不能排序，但可以度量。本阶段把第 1 部分的距离和绝对值搬到平面上，并说明哪些法则得以保留。
tags: 距离, 反向三角不等式
lang: zh
---

<span class="anker" id="stufe-5"></span>

:::zweck
复数不能排序，但可以度量。本阶段把[第 1 部分](/wissen/zh/elektrotechnik/1-semester/hohere-mathematik-1/mengen-logik-und-reelle-zahlen/mengen-logik-und-reelle-zahlen.html)的距离和绝对值搬到平面上，并说明哪些法则得以保留。
:::

**基本思路。** 在 $\mathbb{R}$ 中，$|x|$ 度量到原点的距离。在平面上由勾股定理承担这一任务：从 0 到 $z$ 的线段是一个直角三角形的斜边，两条直角边为 $|x|$ 和 $|y|$（图 [5](#abb-5)，左）。两点间的距离是以它们的坐标差为直角边的斜边。结果是实数，所以这里又可以说“大于”了。

:::abbildung hm1/k2betrag 5
左：绝对值和距离都是斜边：$|z_1|^2=3^2+1^2$，$d(z_1,z_2)^2=2^2+1^2$。右：三角不等式：经过 $z_1$ 的路径比直接到 $z_1+z_2$ 的路径长。
:::

:::definition 定义 5.1 (距离与绝对值)
<span class="anker" id="satz-5-1"></span>

对 $z=x+\mathrm{i}y$ 和 $w=u+\mathrm{i}v$（$x,y,u,v$ 为实数），令

<span class="anker" id="gl-5-1"></span>
$$d(z,w):=\sqrt{(x-u)^2+(y-v)^2},\qquad |z|:=d(z,0)=\sqrt{x^2+y^2}. \tag{5.1}$$
:::

⁠**如何理解：**根号下是一个大于或等于零的实数，而 $\sqrt a$ 是 $b^2=a$ 的非负解（[第 1 部分](/wissen/zh/elektrotechnik/1-semester/hohere-mathematik-1/mengen-logik-und-reelle-zahlen/mengen-logik-und-reelle-zahlen.html)）。__距离__ $d(z,w)$ 只取决于差：$d(z,w)=|z-w|$。**极限情况：**对实数 $z$，$|z|=\sqrt{x^2}=|x|$，即[第 1 部分](/wissen/zh/elektrotechnik/1-semester/hohere-mathematik-1/mengen-logik-und-reelle-zahlen/mengen-logik-und-reelle-zahlen.html)的绝对值。

:::satz 定理 5.2 (绝对值与距离的运算法则)
<span class="anker" id="satz-5-2"></span>

对所有 $z,w,\tilde z\in\mathbb{C}$ 有：

<ol class="rm">

<li>

$|z|\ge0$ 且 ($|z|=0\Leftrightarrow z=0$)，同样 $d(z,w)\ge0$ 且 ($d(z,w)=0\Leftrightarrow z=w$)，

</li>

<li>

$d(z,w)=d(w,z)$，$|\overline{z}|=|{-z}|=|z|$，

</li>

<li>

$z\overline{z}=|z|^2$，因而当 $z\ne0$ 时 $1/z=\overline{z}\cdot1/|z|^2$，

</li>

<li>

$|z\cdot w|=|z|\cdot|w|$，

</li>

<li>

$\max\{|\operatorname{Re}(z)|,|\operatorname{Im}(z)|\}\le|z|\le|\operatorname{Re}(z)|+|\operatorname{Im}(z)|$，

</li>

<li>

$|z+w|\le|z|+|w|$，$d(z,w)\le d(z,\tilde z)+d(\tilde z,w)$（三角不等式），

</li>

<li>

$|z-w|\le|z|+|w|$，$\bigl||z|-|w|\bigr|\le|z-w|$，$\bigl||z|-|w|\bigr|\le|z+w|$（__反向三角不等式__）。

</li>

</ol>
:::

⁠**如何理解：**(iv)：积的绝对值等于绝对值的积。(v)：斜边至多与两条直角边之和一样长，而每条直角边至多与斜边一样长。(vi)：经过 $\tilde z$ 绕路绝不会更短。**适用条件：**这些法则无条件成立，但 $|z+w|=|z|+|w|$ 不是法则：等号在箭头指向同一方向时成立，例如 $z_2$ 和 $2z_2$：$3\sqrt5=\sqrt5+2\sqrt5$。

:::beweis 绝对值的运算法则
(i)、(ii)：平方和为零当且仅当两个平方都为零，而变号不改变平方和。

(iii)：第 [3](spiegeln-an-der-reellen-achse.html#stufe-3) 阶段的规则 (vi)，以及式 [(4.1)](dividieren-und-was-verloren-geht.html#gl-4-1)。

(iv)：由 (iii) 和 $\overline{zw}=\overline{z}\,\overline{w}$，$|zw|^2=zw\,\overline{zw}=z\overline{z}\,w\overline{w}=|z|^2|w|^2$。两个绝对值都非负，所以可以开方。

(v)：$x^2\le x^2+y^2$ 和 $y^2\le x^2+y^2$ 给出左边的不等式，$x^2+y^2\le x^2+2|x||y|+y^2=(|x|+|y|)^2$ 给出右边的不等式。

(vi)：由 (iii) 和共轭法则，

$$|z+w|^2=(z+w)(\overline{z}+\overline{w})=|z|^2+z\overline{w}+\overline{z}w+|w|^2=|z|^2+2\operatorname{Re}(z\overline{w})+|w|^2,$$

因为 $\overline{z}w$ 是 $z\overline{w}$ 的共轭复数。由 (v) 和 (iv)，$\operatorname{Re}(z\overline{w})\le|z\overline{w}|=|z||w|$。所以 $|z+w|^2\le(|z|+|w|)^2$。距离形式由 $z-w=(z-\tilde z)+(\tilde z-w)$ 得出。

(vii)：在 (vi) 中用 $-w$ 代替 $w$，得第一个不等式。由 $|z|=|(z-w)+w|\le|z-w|+|w|$ 得 $|z|-|w|\le|z-w|$，交换角色得 $|w|-|z|\le|z-w|$，合起来就是第二个不等式。在其中用 $-w$ 代替 $w$，得第三个。
:::

**例。** $|z_1|=\sqrt{10}\approx3.162$，$|z_2|=\sqrt5\approx2.236$。三角不等式：$|z_1+z_2|=|4+3\mathrm{i}|=5\le5.398$。乘积：$|z_1z_2|=|1+7\mathrm{i}|=\sqrt{50}=\sqrt{10}\cdot\sqrt5$。距离：$d(z_1,z_2)=|2-\mathrm{i}|=\sqrt5$。反向不等式：$0.926\le2.236$。对 $z_1$ 的规则 (v)：$3\le3.162\le4$。

**点集。** 因为 $|z-c|$ 是 $z$ 到 $c$ 的距离，所以 $|z-c|=r$ 表示以 $c$ 为圆心、$r$ 为半径的圆，$|z-c|\le r$ 表示圆盘。对 $\operatorname{Re}(z)$ 或 $\operatorname{Im}(z)$ 的条件则截出半平面。这样的不等式是允许的，因为两边都是实数。

:::frage 为什么根号下是 $x^2+y^2$ 而不是 $z^2$？
对实数 $z$ 有 $|z|=\sqrt{z^2}$，这很容易误导人。在 $\mathbb{C}$ 中，$z^2$ 一般不是实数，还可能是负数，例如 $(2\mathrm{i})^2=-4$。绝对值应是一个长度，而勾股定理相加的是实长度的平方。正确的写法是 $|z|=\sqrt{z\overline{z}}$。
:::

:::aufgabe 练习 6 ★★ 点集
<span class="anker" id="aufg-6"></span>

在复平面上作图：(a) $\{z:|z-1-\mathrm{i}|\le2\}$，(b) $\{z:|z-2|=|z+2\mathrm{i}|\}$，(c) $\{z:\operatorname{Re}((1+\mathrm{i})z)>1\}$。(b) 的提示：两边平方并代入 $z=x+\mathrm{i}y$。

:::loesung
(a) $|z-(1+\mathrm{i})|\le2$ 是以 $1+\mathrm{i}$ 为圆心、半径为 2 的圆盘，包括边界。

(b) 由 $(x-2)^2+y^2=x^2+(y+2)^2$ 得 $-4x+4=4y+4$，即 $y=-x$。这是过原点、斜率为 $-1$ 的直线。从几何上看，它是到 $2$ 和 $-2\mathrm{i}$ 距离相等的所有点：连接这两点的线段的垂直平分线。

(c) $(1+\mathrm{i})(x+\mathrm{i}y)=(x-y)+\mathrm{i}(x+y)$。条件为 $x-y>1$，即 $y<x-1$。这是直线 $y=x-1$ 下方的半平面，不含该直线。
:::
:::

:::aufgabe 练习 7 ★★★ 平行四边形与单位圆
<span class="anker" id="aufg-7"></span>

(a) 证明 $|z+w|^2+|z-w|^2=2|z|^2+2|w|^2$，并用 $z_1$ 和 $z_2$ 检验。它说明了平行四边形对角线的什么性质？(b) 证明：由 $|z|=1$ 可得 $1/z=\overline{z}$。用 $z=0.6+0.8\mathrm{i}$ 检验。(c) 预测对这个 $z$，$1/(2z)$ 位于何处，并计算验证。

:::loesung
(a) 与三角不等式的证明一样，$|z\pm w|^2=|z|^2\pm2\operatorname{Re}(z\overline{w})+|w|^2$。相加时交叉项消去。检验：$25+5=30=2\cdot10+2\cdot5$。平行四边形两条对角线的平方之和等于四条边的平方之和。

(b) 由 $z\overline{z}=|z|^2=1$ 得 $1/z=\overline{z}$。对 $z=0.6+0.8\mathrm{i}$ 有 $|z|^2=0.36+0.64=1$，且 $(0.6+0.8\mathrm{i})(0.6-0.8\mathrm{i})=0.36+0.64=1$。

(c) 预测：镜像后除以 $|2z|^2=4$，所以倒数在 $\overline{z}$ 的箭头上，绝对值为 $0.5$。计算：$1/(2z)=\overline{z}/2=0.3-0.4\mathrm{i}$。
:::
:::
