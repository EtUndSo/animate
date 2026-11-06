---
title: 二次型
pfad: 计算机科学 / 机器学习 / 投影、特征值与矩阵分解
order: 6220600
summary: 在多元函数中，除线性函数外，二次函数是最简单的。它们可以描述能量、误差的平方以及曲面。本节用矩阵来表示它们，展示碗形、槽形和鞍形三种基本形状，并说明在没有交叉项时如何从矩阵看出是哪种形状。
tags: 二次型
lang: zh
---

<span class="anker" id="stufe-5"></span>

:::zweck
在多元函数中，除线性函数外，二次函数是最简单的。它们可以描述能量、误差的平方以及曲面。本节用矩阵来表示它们，展示碗形、槽形和鞍形三种基本形状，并说明在没有交叉项时如何从矩阵看出是哪种形状。
:::

### 二次型

<span class="anker" id="stufe-5-1"></span>

在第 1 部分第 8.4 节中，每个只有一个输出的线性函数都是各分量的加权和 $\mathbf{w}^{\top}\mathbf{x}$。次简单的一类函数，是把每两个分量的乘积加起来：像 $x_1^2$ 这样的平方项，以及像 $x_1x_2$ 这样的交叉项。电气工程中的一个例子是两个耦合线圈的磁场能量，线圈的电感为 $L_1$、$L_2$，互感为 $M$，分别通过电流 $i_1$ 和 $i_2$：

$$W=\tfrac12L_1i_1^2+M\,i_1i_2+\tfrac12L_2i_2^2 .$$

这样的和可以写成中间夹着一个矩阵的形式。

:::definition 定义 5.1 (二次型)
<span class="anker" id="satz-5-1"></span>

对于方阵 $\mathbf{A}\in\mathbb{R}^{n\times n}$，函数

<span class="anker" id="gl-5-1"></span>
$$f(\mathbf{x})=\mathbf{x}^{\top}\mathbf{A}\mathbf{x}=\sum_{i=1}^n\sum_{l=1}^na_{il}\,x_ix_l \tag{5.1}$$

称为 $\mathbf{A}$ 的__二次型__。
:::

结果是一个数：$\mathbf{A}\mathbf{x}$ 是一个向量，$\mathbf{x}^{\top}(\mathbf{A}\mathbf{x})$ 是 $\mathbf{x}$ 与它的点积。对 $n=2$ 写出来就是

$$\mathbf{x}^{\top}\begin{pmatrix}a_{11}&a_{12}\\a_{21}&a_{22}\end{pmatrix}\mathbf{x}=a_{11}x_1^2+(a_{12}+a_{21})\,x_1x_2+a_{22}x_2^2 .$$

把 $\mathbf{x}$ 加倍，$f$ 就变为四倍：$f(c\,\mathbf{x})=c^2f(\mathbf{x})$。“二次”之名即由此而来。

⁠**算例：**对于 $\mathbf{A}=\bigl(\begin{smallmatrix}5&2\\2&2\end{smallmatrix}\bigr)$，$f(\mathbf{x})=5x_1^2+4x_1x_2+2x_2^2$。在点 $\mathbf{x}=(1,\,-1)^{\top}$ 处，$f=5-4+2=3$；验算：$\mathbf{A}\mathbf{x}=(3,\,0)^{\top}$，$\mathbf{x}^{\top}\mathbf{A}\mathbf{x}=3$。图 [14](#abb-14) 在这一点逐项算出了双重和 [(5.1)](#gl-5-1)。在点 $(1,\,1)^{\top}$ 处，$f=11$；在原点处，$f=0$。两个线圈的能量为 $W=\tfrac12\,\mathbf i^{\top}\bigl(\begin{smallmatrix}L_1&M\\M&L_2\end{smallmatrix}\bigr)\,\mathbf i$，其中电流向量为 $\mathbf i=(i_1,\,i_2)^{\top}$；这个矩阵称为电感矩阵。

:::abbildung ml/k2rqf 14
$\mathbf{A}=\bigl(\begin{smallmatrix}5&2\\2&2\end{smallmatrix}\bigr)$ 的二次型在点 $\mathbf{x}=(1,-1)^{\top}$ 处按双重和计算：共四项，$\mathbf{A}$ 的每个元素对应一项。
:::

⁠**简而言之：**二次型 $\mathbf{x}^{\top}\mathbf{A}\mathbf{x}$ 是各分量的平方项与交叉乘积项之和，以 $\mathbf{A}$ 的元素为权重。

### 只有对称部分起作用

<span class="anker" id="stufe-5-2"></span>

在 $n=2$ 的表达式中，$a_{12}$ 和 $a_{21}$ 只以和的形式出现。因此矩阵 $\bigl(\begin{smallmatrix}5&4\\0&2\end{smallmatrix}\bigr)$ 和 $\bigl(\begin{smallmatrix}5&2\\2&2\end{smallmatrix}\bigr)$ 具有相同的二次型。总可以选取其中对称的那个。

:::satz 定理 5.2 (对称部分)
<span class="anker" id="satz-5-2"></span>

对每个方阵 $\mathbf{A}$ 和每个 $\mathbf{x}$，有

<span class="anker" id="gl-5-2"></span>
$$\mathbf{x}^{\top}\mathbf{A}\mathbf{x}=\mathbf{x}^{\top}\Bigl(\frac{\mathbf{A}+\mathbf{A}^{\top}}2\Bigr)\mathbf{x} . \tag{5.2}$$
:::

:::beweis 对称部分
数 $\mathbf{x}^{\top}\mathbf{A}\mathbf{x}$ 等于它自身的转置，所以 $\mathbf{x}^{\top}\mathbf{A}\mathbf{x}=(\mathbf{x}^{\top}\mathbf{A}\mathbf{x})^{\top}=\mathbf{x}^{\top}\mathbf{A}^{\top}\mathbf{x}$。两个表达式的平均值为 $\mathbf{x}^{\top}\frac{\mathbf{A}+\mathbf{A}^{\top}}2\mathbf{x}$。
:::

矩阵 $\frac12(\mathbf{A}+\mathbf{A}^{\top})$ 是对称的。因此在本章中，二次型总是配一个对称矩阵。读取方法如下：对角线上是各平方项的系数，每个非对角元素是相应交叉项系数的一半。

⁠**算例：**二次型 $3x_1^2-6x_1x_2+x_2^2$ 的对称矩阵为 $\bigl(\begin{smallmatrix}3&-3\\-3&1\end{smallmatrix}\bigr)$。$\mathbb{R}^3$ 中的二次型 $x_1^2+2x_2^2+4x_3^2+2x_1x_3$ 的矩阵为 $\Bigl(\begin{smallmatrix}1&0&1\\0&2&0\\1&0&4\end{smallmatrix}\Bigr)$；交叉项 $2x_1x_3$ 平分到元素 $(1,3)$ 和 $(3,1)$ 上。

⁠**简而言之：**二次型只“看得见”其矩阵的对称部分；因此总是用对称矩阵来写它。

### 碗形、槽形与鞍形

<span class="anker" id="stufe-5-3"></span>

有两个变量时，可以把二次型画成平面上方的曲面，以 $f(\mathbf{x})$ 为高度；还可以像地图那样画出它的等高线，即高度相等的线。矩阵为对角矩阵时最简单。这时没有交叉项，$f(\mathbf{x})=a_{11}x_1^2+a_{22}x_2^2$。根据两个元素的符号，出现三种基本形状（图 [15](#abb-15)）。

:::abbildung ml/k2formen 15
上：二次型 $x_1^2+2x_2^2$（碗形）、$x_1^2$（槽形）和 $x_1^2-x_2^2$（鞍形）在正方形 $|x_1|,|x_2|\le1$ 上的图像；下：它们的等高线。碗形的等高线是椭圆（$f=\tfrac14,\tfrac12,1$），槽形的等高线是成对的平行线，虚线是直线 $x_1=0$，槽形在其上的高度为零。鞍形的等高线是双曲线，$f=\tfrac14,\tfrac12$ 用深色，$f=-\tfrac14,-\tfrac12$ 用浅色；虚线是 $f=0$ 的两条直线。
:::

<ul>

<li>

⁠**碗形：**两个对角元素都为正，例如 $f=x_1^2+2x_2^2$。这时对每个 $\mathbf{x}\ne\mathbf{0}$ 都有 $f(\mathbf{x})>0$，只在原点处 $f=0$。等高线是围绕原点的椭圆，半轴位于坐标轴上。

</li>

<li>

⁠**槽形：**一个元素为正，另一个为零，例如 $f=x_1^2$。这时 $f\ge0$，但在整条直线 $x_1=0$ 上 $f=0$：曲面在那里有一条笔直的谷底。等高线是成对的平行线。

</li>

<li>

⁠**鞍形：**两个元素符号不同，例如 $f=x_1^2-x_2^2$。沿 $x_1$ 轴，曲面向两侧上升；沿 $x_2$ 轴，曲面向两侧下降。等高线是双曲线。

</li>

</ul>

若两个元素都为负，碗就倒扣过来，成为穹顶形。一个负元素和一个零元素给出倒扣的槽，即脊形。变量多于两个时同样如此：对角元素的符号决定形状。

⁠**算例：**对于碗形 $f=x_1^2+2x_2^2$，等高线 $f=1$ 是一个椭圆，在 $x_1$ 轴上的半轴为 $1$，在 $x_2$ 轴上的半轴为 $1/\sqrt2\approx0.707$：在 $(1,\,0)^{\top}$ 和 $(0,\,1/\sqrt2)^{\top}$ 处 $f=1$。对于鞍形 $f=x_1^2-x_2^2$，有 $f(1,\,0)=1$，$f(0,\,1)=-1$，$f(1,\,1)=0$。

⁠**简而言之：**没有交叉项时，可以从对角线上的符号读出形状：全为正是碗形，正与零是槽形，符号混合是鞍形。

### 配方

<span class="anker" id="stufe-5-4"></span>

有交叉项时，形状就不能一眼看出了。$5x_1^2+4x_1x_2+2x_2^2$ 是碗形吗？交叉项可能为负。你在中学学过一个消去交叉项的工具：配方。它把二次型写成平方和，再像上一小节那样，从各平方项的系数读出形状。

:::herleitung 两个变量的配方
设 $a\ne0$。从含 $x_1$ 的项中提出 $a$，然后配方：

$$ax_1^2+2bx_1x_2+cx_2^2=a\Bigl(x_1^2+\frac{2b}ax_1x_2\Bigr)+cx_2^2=a\Bigl(x_1+\frac bax_2\Bigr)^2-\frac{b^2}ax_2^2+cx_2^2 .$$

因此

<span class="anker" id="gl-5-3"></span>
$$ax_1^2+2bx_1x_2+cx_2^2=a\Bigl(x_1+\frac bax_2\Bigr)^2+\Bigl(c-\frac{b^2}a\Bigr)x_2^2 . \tag{5.3}$$
:::

右边是两个平方项之和。当 $\mathbf{x}$ 取遍整个平面时，新变量 $z_1=x_1+\frac bax_2$ 和 $z_2=x_2$ 取遍所有数对。所以在变量 $z_1,z_2$ 下，二次型不再有交叉项，$a$ 与 $c-b^2/a$ 的符号决定它是碗形、槽形还是鞍形。

⁠**算例 1：**$5x_1^2+4x_1x_2+2x_2^2$ 中 $a=5$，$b=2$，$c=2$：

$$5x_1^2+4x_1x_2+2x_2^2=5\,(x_1+0.4\,x_2)^2+1.2\,x_2^2 .$$

两个系数都为正：该二次型是碗形。在 $\mathbf{x}=(1,\,-1)^{\top}$ 处验算：$5\cdot0.36+1.2=3$。

⁠**算例 2：**$x_1^2+6x_1x_2+x_2^2=(x_1+3x_2)^2-8x_2^2$。两个系数符号不同：是鞍形。确实有 $f(1,\,0)=1>0$，$f(1,\,-1)=1-6+1=-4<0$。

⁠**简而言之：**配方把二次型写成平方和；各平方项系数的符号表明它是碗形、槽形还是鞍形。

:::hintergrund 配方就是高斯消元
式 [(5.3)](#gl-5-3) 中的数，与把第 1 部分第 12.3 节的高斯消元法应用于对称矩阵 $\bigl(\begin{smallmatrix}a&b\\b&c\end{smallmatrix}\bigr)$ 时出现的数相同。为了在对角线下方得到零，从第二行减去第一行的 $\frac ba$ 倍，得到 $\bigl(\begin{smallmatrix}a&b\\0&c-b^2/a\end{smallmatrix}\bigr)$。这个阶梯形的对角元素，即所谓的主元，恰好就是各平方项的系数，而消元因子 $\frac ba$ 出现在第一个括号中。对于矩阵 $\bigl(\begin{smallmatrix}5&2\\2&2\end{smallmatrix}\bigr)$：因子为 $0.4$，主元为 $5$ 和 $1.2$。有 $n$ 个变量时也照此继续：每一步消元都为一个变量配方。二次型是碗形，当且仅当所有主元都为正。由第 1 部分第 14.5 节的规则，主元之积等于行列式，这里是 $5\cdot1.2=6=5\cdot2-2\cdot2$。
:::

:::aufgabe 练习 14 ★ 二次型与矩阵
<span class="anker" id="aufg-14"></span>

<ol class="al">

<li>

写出二次型 $2x_1^2-2x_1x_2+3x_2^2$ 和 $x_1x_2$ 的对称矩阵。

</li>

<li>

计算 $\bigl(\begin{smallmatrix}1&3\\-1&2\end{smallmatrix}\bigr)$ 的二次型及其对称矩阵。

</li>

<li>

不经计算判断 $3x_1^2+x_2^2$、$-x_1^2$ 和 $2x_1^2-x_2^2+x_3^2$ 是碗形、槽形、鞍形还是其他形状。

</li>

</ol>

:::loesung
(a) 对角线上是各平方项的系数，非对角元素是交叉项系数的一半：$2x_1^2-2x_1x_2+3x_2^2$ 的矩阵为 $\bigl(\begin{smallmatrix}2&-1\\-1&3\end{smallmatrix}\bigr)$，$x_1x_2$ 的矩阵为 $\bigl(\begin{smallmatrix}0&1/2\\1/2&0\end{smallmatrix}\bigr)$。

(b) $\mathbf{x}^{\top}\bigl(\begin{smallmatrix}1&3\\-1&2\end{smallmatrix}\bigr)\mathbf{x}=x_1^2+(3-1)\,x_1x_2+2x_2^2=x_1^2+2x_1x_2+2x_2^2$。对称矩阵为 $\tfrac12(\mathbf{A}+\mathbf{A}^{\top})=\bigl(\begin{smallmatrix}1&1\\1&2\end{smallmatrix}\bigr)$。

(c) $3x_1^2+x_2^2$：两个系数都为正，是碗形。$-x_1^2$：一个系数为负，一个为零，所以是倒扣的槽形，即沿 $x_2$ 轴的脊形。$2x_1^2-x_2^2+x_3^2$：符号有正有负，是鞍形；沿 $x_1$ 和 $x_3$ 方向二次型上升，沿 $x_2$ 方向下降。
:::
:::

:::aufgabe 练习 15 ★★ 配方
<span class="anker" id="aufg-15"></span>

配方并判断形状：

$$f_1=2x_1^2+8x_1x_2+11x_2^2,\qquad f_2=x_1^2+4x_1x_2+4x_2^2,\qquad f_3=x_1^2+4x_1x_2+x_2^2 .$$

对于槽形，写出使 $f=0$ 的直线；对于鞍形，给出一个 $f<0$ 的点。

:::loesung
用式 [(5.3)](#gl-5-3)：

<ul>

<li>

$f_1$：$a=2$，$b=4$，$c=11$，所以 $f_1=2(x_1+2x_2)^2+(11-8)\,x_2^2=2(x_1+2x_2)^2+3x_2^2$。两个系数都为正：碗形。

</li>

<li>

$f_2=(x_1+2x_2)^2+0\cdot x_2^2$：槽形。它在直线 $x_1+2x_2=0$ 上为零，即沿 $(2,\,-1)^{\top}$ 方向为零。

</li>

<li>

$f_3=(x_1+2x_2)^2-3x_2^2$：符号不同，是鞍形。取 $x_2=1$ 和 $x_1=-2$，第一个平方项就为零：$f_3(-2,\,1)=4-8+1=-3<0$。

</li>

</ul>
:::
:::

:::aufgabe 练习 16 ★★ 耦合线圈
<span class="anker" id="aufg-16"></span>

两个耦合线圈的电感为 $L_1=4\,\mathrm{mH}$ 和 $L_2=1\,\mathrm{mH}$。

<ol class="al">

<li>

对能量 $W=\tfrac12L_1i_1^2+M\,i_1i_2+\tfrac12L_2i_2^2$ 进行配方。

</li>

<li>

$M$ 取哪些值时，对所有电流 $(i_1,\,i_2)\ne(0,\,0)$ 都有 $W>0$？由此对耦合系数 $k=M/\sqrt{L_1L_2}$ 能得出什么结论？

</li>

</ol>

:::loesung
(a) 在式 [(5.3)](#gl-5-3) 中，$a=\tfrac12L_1$，$2b=M$，$c=\tfrac12L_2$，所以 $b/a=M/L_1$，$b^2/a=M^2/(2L_1)$：

$$W=\tfrac12L_1\Bigl(i_1+\frac M{L_1}\,i_2\Bigr)^2+\tfrac12\Bigl(L_2-\frac{M^2}{L_1}\Bigr)i_2^2=2\,\mathrm{mH}\,\Bigl(i_1+\frac M{4\,\mathrm{mH}}\,i_2\Bigr)^2+\Bigl(\frac12\,\mathrm{mH}-\frac{M^2}{8\,\mathrm{mH}}\Bigr)i_2^2 .$$

(b) 第一个系数为正。要使 $W>0$ 对所有电流 $\ne(0,\,0)$ 成立，充分必要条件是第二个系数也为正：$L_2-M^2/L_1>0$，即 $M^2<L_1L_2=4\,(\mathrm{mH})^2$，$|M|<2\,\mathrm{mH}$。对耦合系数而言，这意味着 $|k|=|M|/\sqrt{L_1L_2}<1$。在 $|k|=1$，即理想的全耦合情形下，二次型就只是槽形：对于相应的电流比 $i_1=-\tfrac M{L_1}\,i_2$，储存的能量将为零。所以，正是磁场能量永不为负这一事实迫使 $|k|\le1$。
:::
:::
