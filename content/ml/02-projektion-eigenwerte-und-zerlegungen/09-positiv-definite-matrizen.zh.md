---
title: 正定矩阵
pfad: 计算机科学 / 机器学习 / 数学基础 / 投影、特征值与矩阵分解
knoten: 基础篇 2：投影、特征值与矩阵分解
nachschlagen: ja
order: 15220900
summary: 如果一个二次型除原点外处处为正，它就是碗形。本节给这一性质一个名称，并介绍检验它的几种判别法：借助特征值、借助主元以及借助行列式。此外还有两个推论：二次型在单位圆上的最大值和最小值，以及一种只有碗形才有的分解。
tags: 正定, 半正定, 不定, 瑞利商
lang: zh
---

<span class="anker" id="stufe-8"></span>

:::zweck
如果一个二次型除原点外处处为正，它就是碗形。本节给这一性质一个名称，并介绍检验它的几种判别法：借助特征值、借助主元以及借助行列式。此外还有两个推论：二次型在单位圆上的最大值和最小值，以及一种只有碗形才有的分解。
:::

### 正定与半正定

<span class="anker" id="stufe-8-1"></span>

第 [5.3](quadratische-formen.html#stufe-5-3) 节中的碗形和槽形在一点上有区别：碗形在原点以外处处为正，槽形只是不为负。这两种性质有固定的名称。

:::definition 定义 8.1 (正定，半正定)
<span class="anker" id="satz-8-1"></span>

若对称矩阵 $\mathbf{A}\in\mathbb{R}^{n\times n}$ 满足

<span class="anker" id="gl-8-1"></span>
$$\mathbf{x}^{\top}\mathbf{A}\mathbf{x}>0\qquad\text{对所有}\ \mathbf{x}\ne\mathbf{0} , \tag{8.1}$$

则称它为__正定__的；若对所有 $\mathbf{x}$ 都有 $\mathbf{x}^{\top}\mathbf{A}\mathbf{x}\ge0$，则称它为__半正定__的。
:::

对称性是定义的一部分。对二次型来说，这并不构成限制，因为由第 [5.2](quadratische-formen.html#stufe-5-2) 节，起作用的反正只是对称部分。但要让下一小节的判别法成立，就需要对称性。每个正定矩阵也是半正定的。

⁠**算例：**$\bigl(\begin{smallmatrix}5&2\\2&2\end{smallmatrix}\bigr)$ 是正定的，因为由第 [5.4](quadratische-formen.html#stufe-5-4) 节，$\mathbf{x}^{\top}\mathbf{A}\mathbf{x}=5(x_1+0.4x_2)^2+1.2x_2^2$，而它只在 $x_2=0$、进而 $x_1=0$ 时为零。矩阵 $\bigl(\begin{smallmatrix}1&2\\2&4\end{smallmatrix}\bigr)$ 的二次型为 $x_1^2+4x_1x_2+4x_2^2=(x_1+2x_2)^2\ge0$；它是半正定的，但不是正定的，因为对 $\mathbf{x}=(2,\,-1)^{\top}$，二次型为零。它的图像是一个槽形，谷底沿 $(2,\,-1)^{\top}$ 方向。

⁠**简而言之：**正定的意思是：二次型在原点以外为正，是碗形；半正定的意思是：二次型处处不为负。

### 特征值判别法

<span class="anker" id="stufe-8-2"></span>

主轴形式 [(7.4)](diagonalisierung-und-spektralsatz.html#gl-7-4) 立即回答了这个问题：若所有 $\lambda_i$ 都为正，则对坐标的每一种不全为零的选取，和 $\sum_i\lambda_ic_i^2$ 都为正；否则就不是这样。

:::satz 定理 8.2 (特征值判别法)
<span class="anker" id="satz-8-2"></span>

对称矩阵是正定的，当且仅当它的所有特征值都为正；是半正定的，当且仅当没有特征值为负。
:::

:::beweis 特征值判别法
若所有 $\lambda_i>0$ 且 $\mathbf{x}\ne\mathbf{0}$，则也有 $\mathbf{c}=\mathbf{Q}^{\top}\mathbf{x}\ne\mathbf{0}$，因为 $\mathbf{Q}$ 可逆；由式 [(7.4)](diagonalisierung-und-spektralsatz.html#gl-7-4)，$\mathbf{x}^{\top}\mathbf{A}\mathbf{x}=\sum_i\lambda_ic_i^2>0$。反之，若某个特征值 $\lambda_i\le0$，则对特征向量 $\mathbf{x}=\mathbf{q}_i$，二次型为 $\mathbf{q}_i^{\top}\mathbf{A}\mathbf{q}_i=\lambda_i\le0$，$\mathbf{A}$ 不是正定的。对于半正定的情形，做法相同，只是用 $\ge$ 代替 $>$。
:::

若对称矩阵既有正特征值又有负特征值，它的二次型就在某些方向上为正，在另一些方向上为负：这是鞍形。这样的矩阵称为__不定__的。相应地，只有负特征值的矩阵称为负定的；它的二次型是穹顶形。

⁠**算例：**$\bigl(\begin{smallmatrix}5&2\\2&2\end{smallmatrix}\bigr)$ 的特征值为 $6$ 和 $1$：正定。$\bigl(\begin{smallmatrix}1&2\\2&4\end{smallmatrix}\bigr)$ 的特征值为 $5$ 和 $0$：半正定。$\bigl(\begin{smallmatrix}1&3\\3&1\end{smallmatrix}\bigr)$ 的元素全为正，但特征值为 $4$ 和 $-2$：不定，因为对 $\mathbf{x}=(1,\,-1)^{\top}$，二次型为 $1-6+1=-4$。所以元素为正并不能说明定性。

⁠**简而言之：**对称矩阵是正定的，当且仅当所有特征值都为正；正特征值和负特征值同时出现时是鞍形。

:::hintergrund 为什么对称性是定义的一部分
有些书通过二次型定义正定，另一些书则通过特征值来定义。由上面的定理，对于对称矩阵这两者是一回事，对于非对称矩阵则不然。矩阵 $\bigl(\begin{smallmatrix}2&-5\\0&2\end{smallmatrix}\bigr)$ 是三角矩阵，特征值为 $2$ 和 $2$，都为正。但它的二次型是 $2x_1^2-5x_1x_2+2x_2^2$，对 $\mathbf{x}=(1,\,1)^{\top}$ 等于 $2-5+2=-1$。原因在于：二次型只“看得见”对称部分 $\bigl(\begin{smallmatrix}2&-2.5\\-2.5&2\end{smallmatrix}\bigr)$，其特征值为 $4.5$ 和 $-0.5$，而特征值属于整个矩阵。因此，在不要求对称性的情况下使用这个概念，就必须始终说明所指的是哪种定义。
:::

### 不用特征值的判别法

<span class="anker" id="stufe-8-3"></span>

对大矩阵来说，计算特征值很费事。第 [5.4](quadratische-formen.html#stufe-5-4) 节的配方提供了一种不用特征值的判别法，由它又得出第二种用行列式的判别法。

:::satz 定理 8.3 (正定性的判别法)
<span class="anker" id="satz-8-3"></span>

对于对称矩阵 $\mathbf{A}\in\mathbb{R}^{n\times n}$，下列条件等价：

<ol class="rm">

<li>

$\mathbf{A}$ 是正定的；

</li>

<li>

不作行交换的高斯消元法给出 $n$ 个正的主元；

</li>

<li>

所有顺序主子式都为正：对 $k=1,\dots,n$，左上角 $k\times k$ 子矩阵的行列式都大于零。

</li>

</ol>

对于 $n=2$ 和 $\mathbf{A}=\bigl(\begin{smallmatrix}a&b\\b&c\end{smallmatrix}\bigr)$，这意味着：$a>0$ 且 $ac-b^2>0$。
:::

对于 $n=2$，这就是式 [(5.3)](quadratische-formen.html#gl-5-3)：主元为 $a$ 和 $c-b^2/a$，二次型是碗形当且仅当二者都为正，而在 $a>0$ 时，条件 $c-b^2/a>0$ 与 $ac-b^2>0$ 等价。对于更大的 $n$，正如第 [5.4](quadratische-formen.html#stufe-5-4) 节的背景方框所述，每一步消元都为一个变量配方。左上角 $k\times k$ 子矩阵的行列式是前 $k$ 个主元之积，因此主元全为正，当且仅当顺序主子式全为正。行列式判别法也称为西尔维斯特判据。

有两点需要注意。第一，仅有 $\det\mathbf{A}>0$ 是不够的：$\operatorname{diag}(-1,\,-3)$ 的行列式为 $3$，却是负定的。第二，这个判别法不能简单地照搬到半正定的情形：$\operatorname{diag}(0,\,-1)$ 的顺序主子式为 $0$ 和 $0$，都不为负，但它并不是半正定的。

⁠**算例：**对于

$$\mathbf{A}=\begin{pmatrix}2&1&0\\1&2&1\\0&1&2\end{pmatrix}$$

顺序主子式为 $2$、$\det\bigl(\begin{smallmatrix}2&1\\1&2\end{smallmatrix}\bigr)=3$ 和 $\det\mathbf{A}=2\cdot3-1\cdot2=4$，全为正：$\mathbf{A}$ 是正定的。主元为 $2$、$\tfrac32$ 和 $\tfrac43$，即相邻两个主子式之商。验算：特征值为 $2-\sqrt2$、$2$ 和 $2+\sqrt2$，全为正，其积为 $(4-2)\cdot2=4$。

⁠**简而言之：**对称矩阵是正定的，当且仅当所有主元或所有顺序主子式都为正；对于 $2\times2$ 矩阵，这意味着 $a>0$ 且 $ac-b^2>0$。

### 格拉姆矩阵是半正定的

<span class="anker" id="stufe-8-4"></span>

基础篇 1 第 10 节中出现过格拉姆矩阵 $\mathbf{X}^{\top}\mathbf{X}$ 和 $\mathbf{X}\mathbf{X}^{\top}$；在本章中，$\mathbf{A}^{\top}\mathbf{A}$ 出现在正规方程里。它们总是半正定的，原因很简单：它们的二次型是一个长度的平方。

:::satz 定理 8.4 (格拉姆矩阵)
<span class="anker" id="satz-8-4"></span>

对每个矩阵 $\mathbf{A}\in\mathbb{R}^{m\times n}$，$\mathbf{A}^{\top}\mathbf{A}$ 都是半正定的。它是正定的，当且仅当 $\mathbf{A}$ 的列线性无关。
:::

:::beweis 格拉姆矩阵
$\mathbf{A}^{\top}\mathbf{A}$ 是对称的，并且 $\mathbf{x}^{\top}\mathbf{A}^{\top}\mathbf{A}\mathbf{x}=(\mathbf{A}\mathbf{x})^{\top}(\mathbf{A}\mathbf{x})=\lVert\mathbf{A}\mathbf{x}\rVert^2\ge0$。它恰好在 $\mathbf{A}\mathbf{x}=\mathbf{0}$ 时为零。在各列线性无关时，这只对 $\mathbf{x}=\mathbf{0}$ 发生。
:::

把列换成行，同样的结论对 $\mathbf{A}\mathbf{A}^{\top}$ 也成立。这个定理事后解释了第 [3.5](die-beste-naherungslosung.html#stufe-3-5) 节：在各列线性无关时，$\mathbf{A}^{\top}\mathbf{A}$ 是正定的，因而只有正特征值，并且可逆。

⁠**算例：**$\mathbf{H}^{\top}\mathbf{H}=\bigl(\begin{smallmatrix}2&1\\1&2\end{smallmatrix}\bigr)$ 的特征值为 $3$ 和 $1$：正定，这与 $\mathbf{H}$ 的列线性无关相符。对于 $\mathbf{A}=\bigl(\begin{smallmatrix}1&2\\2&4\end{smallmatrix}\bigr)$，得到 $\mathbf{A}^{\top}\mathbf{A}=\bigl(\begin{smallmatrix}5&10\\10&20\end{smallmatrix}\bigr)$，其行列式为 $0$，特征值为 $25$ 和 $0$：半正定，但不是正定。

⁠**简而言之：**$\mathbf{A}^{\top}\mathbf{A}$ 总是半正定的，因为 $\mathbf{x}^{\top}\mathbf{A}^{\top}\mathbf{A}\mathbf{x}=\lVert\mathbf{A}\mathbf{x}\rVert^2$；在各列线性无关时，它是正定的。

### 单位圆上的最大值与最小值

<span class="anker" id="stufe-8-5"></span>

二次型随 $\mathbf{x}$ 长度的平方而增长。它在不同方向上增长得有多快，只要代入长度为 $1$ 的向量就能看出来。它在哪个方向上最大？

:::satz 定理 8.5 (二次型的极值)
<span class="anker" id="satz-8-5"></span>

设 $\mathbf{A}$ 是对称矩阵，最小特征值为 $\lambda_{\min}$，最大特征值为 $\lambda_{\max}$。对每个向量 $\mathbf{x}\ne\mathbf{0}$，有

<span class="anker" id="gl-8-2"></span>
$$\lambda_{\min}\le\frac{\mathbf{x}^{\top}\mathbf{A}\mathbf{x}}{\mathbf{x}^{\top}\mathbf{x}}\le\lambda_{\max} . \tag{8.2}$$

最大值在属于 $\lambda_{\max}$ 的特征向量处取得，最小值在属于 $\lambda_{\min}$ 的特征向量处取得。
:::

:::beweis 极值
令 $\mathbf{c}=\mathbf{Q}^{\top}\mathbf{x}$，则 $\mathbf{x}^{\top}\mathbf{x}=\mathbf{c}^{\top}\mathbf{c}=\sum_ic_i^2$，因为 $\mathbf{Q}$ 保持长度不变，并且 $\mathbf{x}^{\top}\mathbf{A}\mathbf{x}=\sum_i\lambda_ic_i^2$。所以这个商为

$$\frac{\sum_i\lambda_ic_i^2}{\sum_ic_i^2}=\sum_i\lambda_i\,g_i\qquad\text{其中}\qquad g_i=\frac{c_i^2}{\sum_lc_l^2}\ge0,\quad \sum_ig_i=1 .$$

这是特征值的加权平均，而平均值总是位于被平均的各值中最小者与最大者之间。对于 $\mathbf{x}=\mathbf{q}_i$，唯一不为零的权重是 $g_i=1$，商等于 $\lambda_i$。
:::

式 [(8.2)](#gl-8-2) 中的商称为__瑞利商__。当 $\lVert\mathbf{x}\rVert=1$ 时，它就是二次型本身：在单位圆上，二次型的值介于最小特征值与最大特征值之间。

⁠**算例：**对于 $\mathbf{A}=\bigl(\begin{smallmatrix}5&2\\2&2\end{smallmatrix}\bigr)$，瑞利商在 $\mathbf{e}_1$ 处为 $5$，在 $\mathbf{e}_2$ 处为 $2$，在 $(1,\,1)^{\top}/\sqrt2$ 处为 $\tfrac{5+4+2}2=5.5$，在 $(1,\,-1)^{\top}/\sqrt2$ 处为 $\tfrac{5-4+2}2=1.5$。所有值都介于 $1$ 和 $6$ 之间。它在 $\mathbf{q}_1=(2,\,1)^{\top}/\sqrt5$ 处达到 $6$：$\tfrac15(20+8+2)=6$。这个商与 $\mathbf{x}$ 的长度无关；图 [21](#abb-21) 对 $\mathbf{x}=(1,\,1)^{\top}$ 不用平方根就算出了它。

:::abbildung ml/k2rrayleigh 21
$\mathbf{A}=\bigl(\begin{smallmatrix}5&2\\2&2\end{smallmatrix}\bigr)$ 在点 $\mathbf{x}=(1,1)^{\top}$ 处的瑞利商：分子和分母都写成和；商 $\tfrac{11}2=5.5$ 介于特征值 $1$ 和 $6$ 之间。
:::

⁠**简而言之：**在单位圆上，二次型的值介于最小特征值与最大特征值之间，这两个极值在特征方向上取得。

### Cholesky 分解

<span class="anker" id="stufe-8-6"></span>

配方把正定二次型写成平方和。把各个平方中的表达式合成一个向量，二次型就是这个向量长度的平方。由此得到矩阵的一种分解。

:::satz 定理 8.6 (Cholesky 分解)
<span class="anker" id="satz-8-6"></span>

对称矩阵 $\mathbf{A}$ 是正定的，当且仅当存在对角元素为正的下三角矩阵 $\mathbf L$，使得

<span class="anker" id="gl-8-3"></span>
$$\mathbf{A}=\mathbf L\mathbf L^{\top} . \tag{8.3}$$

这个矩阵 $\mathbf L$ 是唯一的，称为 $\mathbf{A}$ 的 Cholesky 因子。
:::

若 $\mathbf{A}=\mathbf L\mathbf L^{\top}$，则 $\mathbf{x}^{\top}\mathbf{A}\mathbf{x}=\lVert\mathbf L^{\top}\mathbf{x}\rVert^2$ 是平方和，而且由于 $\mathbf L$ 可逆，它只在 $\mathbf{x}=\mathbf{0}$ 时为零。这是一个方向。另一个方向，即每个正定矩阵都有这样的因子，就是配方：对于 $n=2$，可以从式 [(5.3)](quadratische-formen.html#gl-5-3) 中读出它，

$$\mathbf L=\begin{pmatrix}\sqrt a&0\\b/\sqrt a&\sqrt{c-b^2/a}\end{pmatrix},$$

对于更大的 $n$，就逐个变量地继续配方。由基础篇 1 第 14.5 节，$\det\mathbf{A}=\det\mathbf L\cdot\det\mathbf L^{\top}=(l_{11}\cdots l_{nn})^2$。

⁠**算例：**对于 $\mathbf{A}=\bigl(\begin{smallmatrix}4&2\\2&5\end{smallmatrix}\bigr)$，有 $a=4$，$b=2$，$c=5$，所以 $l_{11}=2$，$l_{21}=1$，$l_{22}=\sqrt{5-1}=2$：

$$\mathbf L=\begin{pmatrix}2&0\\1&2\end{pmatrix},\qquad \mathbf L\mathbf L^{\top}=\begin{pmatrix}4&2\\2&1+4\end{pmatrix}=\mathbf{A} .$$

二次型为 $4x_1^2+4x_1x_2+5x_2^2=(2x_1+x_2)^2+(2x_2)^2$；两个平方中的表达式就是 $\mathbf L^{\top}\mathbf{x}$ 的分量。行列式为 $20-4=16=(2\cdot2)^2$。

⁠**简而言之：**每个正定矩阵都是 $\mathbf L\mathbf L^{\top}$，其中 $\mathbf L$ 是下三角矩阵；这个分解就是矩阵形式的配方。

:::aufgabe 练习 24 ★ 判断定性
<span class="anker" id="aufg-24"></span>

用两种不同的判别法判断下列矩阵是正定、半正定、负定还是不定：

$$\mathbf{A}_1=\begin{pmatrix}3&1\\1&2\end{pmatrix},\qquad \mathbf{A}_2=\begin{pmatrix}2&6\\6&18\end{pmatrix},\qquad \mathbf{A}_3=\begin{pmatrix}1&3\\3&2\end{pmatrix},\qquad \mathbf{A}_4=\begin{pmatrix}-2&1\\1&-1\end{pmatrix}.$$

:::loesung
<ul>

<li>

$\mathbf{A}_1$：$a=3>0$ 且 $ac-b^2=6-1=5>0$：正定。特征值：迹为 $5$，行列式为 $5$，$\lambda=\tfrac{5\pm\sqrt5}2\approx3.62$ 和 $1.38$，都为正。

</li>

<li>

$\mathbf{A}_2$：$a=2>0$，但 $ac-b^2=36-36=0$。特征值为 $20$ 和 $0$：半正定，而非正定。配方得 $2(x_1+3x_2)^2$，是槽形。

</li>

<li>

$\mathbf{A}_3$：$ac-b^2=2-9=-7<0$；两个特征值之积为 $-7$，因此符号相反：不定。它们是 $\tfrac{3\pm\sqrt{37}}2\approx4.54$ 和 $-1.54$。

</li>

<li>

$\mathbf{A}_4$：$a=-2<0$，不是正定的。对于 $-\mathbf{A}_4=\bigl(\begin{smallmatrix}2&-1\\-1&1\end{smallmatrix}\bigr)$，有 $a=2>0$ 和 $ac-b^2=1>0$，所以 $-\mathbf{A}_4$ 正定，$\mathbf{A}_4$ 负定。$\mathbf{A}_4$ 的特征值：迹为 $-3$，行列式为 $1$，$\lambda=\tfrac{-3\pm\sqrt5}2\approx-0.38$ 和 $-2.62$，都为负：穹顶形。

</li>

</ul>
:::
:::

:::aufgabe 练习 25 ★★ 一个陷阱
<span class="anker" id="aufg-25"></span>

<ol class="al">

<li>

矩阵 $\bigl(\begin{smallmatrix}1&-4\\0&1\end{smallmatrix}\bigr)$ 只有正特征值。它的二次型是正的吗？找一个说明情况相反的向量，并解释这个矛盾。

</li>

<li>

$t$ 取哪些数时，$\bigl(\begin{smallmatrix}1&t\\t&4\end{smallmatrix}\bigr)$ 是正定的？取哪些数时是半正定的？

</li>

</ol>

:::loesung
(a) 特征值为 $1$ 和 $1$，但在 $\mathbf{x}=(1,\,1)^{\top}$ 处，二次型 $x_1^2-4x_1x_2+x_2^2$ 等于 $1-4+1=-2<0$。这并不矛盾：特征值判别法只适用于对称矩阵。对二次型起作用的只有对称部分 $\bigl(\begin{smallmatrix}1&-2\\-2&1\end{smallmatrix}\bigr)$，而它的特征值为 $3$ 和 $-1$；该二次型是不定的。

(b) 用 $2\times2$ 判别法：$a=1>0$，且 $ac-b^2=4-t^2>0$ 恰好在 $|t|<2$ 时成立。半正定要求特征值 $\ge0$。特征值之和是迹 $5>0$，之积是行列式 $4-t^2$；两个特征值都 $\ge0$，当且仅当 $4-t^2\ge0$，即 $|t|\le2$。在 $t=\pm2$ 时，矩阵是半正定的，但不是正定的，特征值为 $5$ 和 $0$；当 $|t|>2$ 时，它是不定的。
:::
:::

:::aufgabe 练习 26 ★★ 瑞利商与 Cholesky 分解
<span class="anker" id="aufg-26"></span>

设 $\mathbf{A}=\bigl(\begin{smallmatrix}4&2\\2&5\end{smallmatrix}\bigr)$。

<ol class="al">

<li>

计算特征值，以及在点 $\mathbf{e}_1$、$\mathbf{e}_2$ 和 $(1,\,1)^{\top}$ 处的瑞利商。验证式 [(8.2)](#gl-8-2)。

</li>

<li>

用 Cholesky 因子求解 $\mathbf{A}\mathbf{x}=(2,\,9)^{\top}$：先自上而下求解 $\mathbf L\mathbf{z}=(2,\,9)^{\top}$，再自下而上求解 $\mathbf L^{\top}\mathbf{x}=\mathbf{z}$。

</li>

</ol>

:::loesung
(a) 迹为 $9$，行列式为 $16$：$\lambda=\tfrac{9\pm\sqrt{81-64}}2=\tfrac{9\pm\sqrt{17}}2\approx6.56$ 和 $2.44$。瑞利商在 $\mathbf{e}_1$ 处为 $4$，在 $\mathbf{e}_2$ 处为 $5$，在 $(1,\,1)^{\top}$ 处为 $\tfrac{4+2+2+5}2=\tfrac{13}2=6.5$。三者都介于 $2.44$ 与 $6.56$ 之间；第三个接近最大值，因为 $(1,\,1)^{\top}$ 几乎指向属于较大特征值的特征向量的方向。

(b) 由第 [8.6](#stufe-8-6) 节：$\mathbf L=\bigl(\begin{smallmatrix}2&0\\1&2\end{smallmatrix}\bigr)$。自上而下：$2z_1=2$，所以 $z_1=1$；$z_1+2z_2=9$，所以 $z_2=4$。再自下而上求解 $\mathbf L^{\top}\mathbf{x}=\mathbf{z}$：$2x_2=4$，所以 $x_2=2$；$2x_1+x_2=1$，所以 $x_1=-\tfrac12$。验算：$\mathbf{A}(-\tfrac12,\,2)^{\top}=(-2+4,\ -1+10)^{\top}=(2,\,9)^{\top}$。两个三角方程组取代了一个一般的方程组。
:::
:::
