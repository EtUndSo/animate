---
title: 特征值与特征向量
pfad: 计算机科学 / 机器学习 / 数学基础 / 投影、特征值与矩阵分解
adresse: informatik/machine-learning/mathematische-grundlagen/projektion-eigenwerte-und-zerlegungen
knoten: 第 2 章：投影、特征值与矩阵分解
nachschlagen: ja
order: 15220700
summary: 矩阵对大多数向量既旋转又拉伸。但有些方向它不旋转：沿这种方向的箭头只是变长、变短或翻转。本节求出这些方向以及相应的拉伸因子。它们是矩阵的自然坐标轴。
tags: 共轭复数, 特征向量, 特征值, 特征多项式, 特征空间, 迹, 代数重数, 几何重数
lang: zh
---

<span class="anker" id="stufe-6"></span>

:::zweck
矩阵对大多数向量既旋转又拉伸。但有些方向它不旋转：沿这种方向的箭头只是变长、变短或翻转。本节求出这些方向以及相应的拉伸因子。它们是矩阵的自然坐标轴。
:::

:::::vorwissen 所需知识：复数

<span class="anker" id="stufe-6-1"></span>

寻找拉伸因子会导出多项式方程，而并非每个多项式方程都有实数解。本小节汇总本章用到的复数知识。

**复数。** 复数 $z=x+\mathrm j\,y$ 由实部 $x$ 和虚部 $y$ 这两个实数组成。虚数单位满足 $\mathrm j^2=-1$。许多数学书把它记作 $\mathrm i$；本章像 Python 一样写成正体的 $\mathrm j$，因为 Python 把数 $3+4\,\mathrm j$ 写成 `3+4j`，而 $i$ 可以留作下标。

**共轭与模。** $z$ 的__共轭复数__是 $z^*=x-\mathrm j\,y$。有 $z\,z^*=x^2+y^2=|z|^2$，即模的平方，它是一个实数，只在 $z=0$ 时为零。一个数是实数，当且仅当 $z=z^*$。共轭与加法和乘法相容：$(z+w)^*=z^*+w^*$，$(zw)^*=z^*w^*$。对于分量为复数的向量 $\mathbf{v}$，本章中 $\mathbf{v}^*$ 表示由各分量的共轭构成的向量，不作转置。于是

$$(\mathbf{v}^*)^{\top}\mathbf{v}=\sum_i|v_i|^2>0\qquad\text{对 }\mathbf{v}\ne\mathbf{0} .$$

**欧拉公式。** 对每个实数 $\alpha$，有 $\mathrm e^{\mathrm j\alpha}=\cos\alpha+\mathrm j\sin\alpha$，这是复平面单位圆上模为 $1$ 的点。

**多项式的根。** 每个系数为实数或复数、次数 $n\ge1$ 的多项式，若重根按重数计算，则恰有 $n$ 个复数根，并且可以分解为 $n$ 个一次因式。若多项式的系数为实数，那么只要 $z$ 是根，$z^*$ 也是根：非实数根成对出现。

::::beispiel [算例]
由求根公式，$\lambda^2-1.2\lambda+1=0$ 的根为 $\lambda=0.6\pm\sqrt{0.36-1}=0.6\pm\mathrm j\,0.8$，这是一对模为 $\sqrt{0.36+0.64}=1$ 的共轭复数。对于 $\mathbf{v}=(1,\,-\mathrm j)^{\top}$，有 $\mathbf{v}^*=(1,\,\mathrm j)^{\top}$，$(\mathbf{v}^*)^{\top}\mathbf{v}=1\cdot1+\mathrm j\cdot(-\mathrm j)=1+1=2$（图 [16](#abb-16)）。

:::abbildung ml/k2rkomplex 16
$\mathbf{v}=(1,-\mathrm j)^{\top}$ 的点积 $(\mathbf{v}^*)^{\top}\mathbf{v}$：每一项都是 $v_i^*v_i=|v_i|^2$，因为 $\mathrm j\cdot(-\mathrm j)=-\mathrm j^2=1$。
:::
::::

⁠**简而言之：**满足 $\mathrm j^2=-1$ 的复数 $x+\mathrm jy$ 使每个多项式方程都有解；共轭把虚部变号，$zz^*=|z|^2$ 是实数。

:::::

### 特征向量与特征值

<span class="anker" id="stufe-6-2"></span>

在[第 1 章第 8.3 节](/wissen/zh/informatik/machine-learning/mathematische-grundlagen/vektoren-und-matrizen/lineare-abbildungen.html#stufe-8-3)中，平面上的网格被矩阵旋转、拉伸和剪切。在此过程中，大多数箭头都会改变方向。但对某些矩阵，存在这样的方向：沿该方向的箭头仍然留在它所在的过原点的直线上，只是被拉伸、压缩或翻转（图 [17](#abb-17)）。

:::abbildung ml/k2eigen 17
矩阵 $\mathbf{A}=\bigl(\begin{smallmatrix}4&1\\2&3\end{smallmatrix}\bigr)$ 把单位圆（灰色）映射为一个椭圆（蓝色）。箭头 $\mathbf{v}_1=(1,1)^{\top}/\sqrt2$（红色）留在自己的直线上，被拉伸为原长的五倍；箭头 $\mathbf{v}_2=(1,-2)^{\top}/\sqrt5$（绿色）被拉伸为原长的两倍；它们的像用浅色画出。灰色直线是两个特征方向。相反，单位向量 $\mathbf{e}_1$ 被映射为 $(4,2)^{\top}$（虚线），方向发生了改变。
:::

:::definition 定义 6.1 (特征向量，特征值)
<span class="anker" id="satz-6-1"></span>

设 $\mathbf{A}\in\mathbb{R}^{n\times n}$。若向量 $\mathbf{v}\ne\mathbf{0}$ 对某个数 $\lambda$ 满足下式，就称它为 $\mathbf{A}$ 的__特征向量__：

<span class="anker" id="gl-6-1"></span>
$$\mathbf{A}\mathbf{v}=\lambda\,\mathbf{v} . \tag{6.1}$$

数 $\lambda$ 称为相应的__特征值__。
:::

零向量被排除在外，因为 $\mathbf{A}\mathbf{0}=\lambda\mathbf{0}$ 对每个数 $\lambda$ 都成立，什么也说明不了。而特征值可以为零：这时特征向量被映射为 $\mathbf{0}$。负的特征值使箭头翻转。本章中特征值记作 $\lambda$ 或 $\lambda_i$。英语中的 **eigenvalue**、**eigenvector** 沿用了德语前缀 **eigen**（意为“自身的”），中文译作“特征”。

::::beispiel [算例]
对于 $\mathbf{A}=\bigl(\begin{smallmatrix}4&1\\2&3\end{smallmatrix}\bigr)$，

$$\mathbf{A}\begin{pmatrix}1\\1\end{pmatrix}=\begin{pmatrix}5\\5\end{pmatrix}=5\begin{pmatrix}1\\1\end{pmatrix},\qquad \mathbf{A}\begin{pmatrix}1\\-2\end{pmatrix}=\begin{pmatrix}2\\-4\end{pmatrix}=2\begin{pmatrix}1\\-2\end{pmatrix},\qquad \mathbf{A}\begin{pmatrix}1\\0\end{pmatrix}=\begin{pmatrix}4\\2\end{pmatrix}.$$

所以 $(1,\,1)^{\top}$ 是属于特征值 $5$ 的特征向量，$(1,\,-2)^{\top}$ 是属于特征值 $2$ 的特征向量。向量 $(1,\,0)^{\top}$ 不是特征向量，因为 $(4,\,2)^{\top}$ 不是它的倍数。
::::

⁠**简而言之：**特征向量不被矩阵旋转，只被乘以一个数；这个数就是特征值。

:::hintergrund 同样的思想用于无限长的序列：复利
$100$ 欧元的存款余额在每年 $5$ % 的利息下增长为 $100$、$105$、$110.25$、… 欧元，一般地，$n$ 年后为 $a_n=100\cdot1.05^n$。规则“把每个值换成下一年的值”把序列 $(a_0,a_1,a_2,\dots)$ 变成序列 $(a_1,a_2,a_3,\dots)$。它是线性的：把两个序列之和平移，得到的是平移后序列之和，数乘也是如此。对这笔存款余额，它给出

$$(105,\ 110.25,\ \dots)=1.05\cdot(100,\ 105,\ \dots) .$$

序列的形状保持不变，只多了一个数值因子：序列 $a_n=100\cdot1.05^n$ 是平移的一个特征向量，特征值是利率因子 $1.05$。式 [(6.1)](#gl-6-1) 对矩阵说的是同一件事。除这类序列外，平移也没有别的特征向量：由对所有 $n$ 成立的 $a_{n+1}=\lambda\,a_n$ 可得 $a_n=a_0\,\lambda^n$。在两种情况下，无论是序列还是向量，都存在被线性规则只乘以一个数的对象。
:::

### 特征多项式

<span class="anker" id="stufe-6-3"></span>

不靠猜测，怎样求特征值？把式 [(6.1)](#gl-6-1) 改写，使所有项都在一边：$\mathbf{A}\mathbf{v}-\lambda\mathbf{v}=\mathbf{0}$，即 $(\mathbf{A}-\lambda\mathbf{I})\mathbf{v}=\mathbf{0}$。我们要找这样的 $\lambda$，使这个齐次方程组有解 $\mathbf{v}\ne\mathbf{0}$。由[第 1 章第 11.5 节](/wissen/zh/informatik/machine-learning/mathematische-grundlagen/vektoren-und-matrizen/einheitsmatrix-und-inverse.html#stufe-11-5)，这意味着：矩阵 $\mathbf{A}-\lambda\mathbf{I}$ 不可逆。由[第 1 章第 14.6 节](/wissen/zh/informatik/machine-learning/mathematische-grundlagen/vektoren-und-matrizen/die-determinante.html#stufe-14-6)，这恰好在其行列式为零时成立。

:::definition 定义 6.2 (特征多项式)
<span class="anker" id="satz-6-2"></span>

对于 $\mathbf{A}\in\mathbb{R}^{n\times n}$，

<span class="anker" id="gl-6-2"></span>
$$p(\lambda)=\det(\mathbf{A}-\lambda\mathbf{I}) \tag{6.2}$$

称为 $\mathbf{A}$ 的__特征多项式__。
:::

:::satz 定理 6.3 (特征值是根)
<span class="anker" id="satz-6-3"></span>

数 $\lambda$ 是 $\mathbf{A}$ 的特征值，当且仅当 $p(\lambda)=0$。
:::

特征多项式的次数为 $n$。对于 $2\times2$ 矩阵，它是

<span class="anker" id="gl-6-3"></span>
$$\det\begin{pmatrix}a-\lambda&b\\c&d-\lambda\end{pmatrix}=(a-\lambda)(d-\lambda)-bc=\lambda^2-(a+d)\,\lambda+(ad-bc) . \tag{6.3}$$

由“所需知识：复数”小节，按重数计算，它恰有 $n$ 个复数根。所以，若允许复数特征值并把重根按重数计算，$n\times n$ 矩阵就有 $n$ 个特征值。

::::beispiel [算例]
对于 $\mathbf{A}=\bigl(\begin{smallmatrix}4&1\\2&3\end{smallmatrix}\bigr)$，$p(\lambda)=\lambda^2-7\lambda+(12-2)=\lambda^2-7\lambda+10=(\lambda-5)(\lambda-2)$。特征值为 $5$ 和 $2$，与上一小节相同。对于对角矩阵 $\operatorname{diag}(3,\,-1)$，$p(\lambda)=(3-\lambda)(-1-\lambda)$，根为 $3$ 和 $-1$：对角矩阵的特征值就在它的对角线上，特征向量是单位向量。
::::

⁠**简而言之：**特征值是特征多项式 $\det(\mathbf{A}-\lambda\mathbf{I})$ 的根；按重数计算并包括复数特征值，$n\times n$ 矩阵有 $n$ 个特征值。

### 计算特征向量

<span class="anker" id="stufe-6-4"></span>

知道一个特征值 $\lambda$ 后，相应的特征向量就是齐次方程组 $(\mathbf{A}-\lambda\mathbf{I})\mathbf{v}=\mathbf{0}$ 的解 $\mathbf{v}\ne\mathbf{0}$。可以用高斯消元法求出它们。只要 $\mathbf{v}$ 是特征向量，每个倍数 $c\,\mathbf{v}$（$c\ne0$）也是特征向量，因为 $\mathbf{A}(c\mathbf{v})=c\lambda\mathbf{v}=\lambda(c\mathbf{v})$。所以特征向量从来不是唯一的；唯一的只是它的方向，有时甚至连方向也不唯一。

:::definition 定义 6.4 (特征空间)
<span class="anker" id="satz-6-4"></span>

$\mathbf{A}-\lambda\mathbf{I}$ 的零空间称为 $\mathbf{A}$ 属于特征值 $\lambda$ 的__特征空间__。
:::

它包含属于 $\lambda$ 的所有特征向量以及零向量。作为零空间，它是第 [4.1](projektion-auf-einen-unterraum.html#stufe-4-1) 节意义下的子空间。

::::beispiel [算例]
对于 $\mathbf{A}=\bigl(\begin{smallmatrix}4&1\\2&3\end{smallmatrix}\bigr)$ 和 $\lambda=5$，

$$\mathbf{A}-5\mathbf{I}=\begin{pmatrix}-1&1\\2&-2\end{pmatrix}.$$

两行给出同一个要求：$-v_1+v_2=0$。特征空间是 $(1,\,1)^{\top}$ 的所有倍数构成的直线。对于 $\lambda=2$，$\mathbf{A}-2\mathbf{I}=\bigl(\begin{smallmatrix}2&1\\2&1\end{smallmatrix}\bigr)$，条件为 $2v_1+v_2=0$；特征空间是沿 $(1,\,-2)^{\top}$ 方向的直线。归一化后，特征向量为 $\mathbf{v}_1=(1,\,1)^{\top}/\sqrt2$ 和 $\mathbf{v}_2=(1,\,-2)^{\top}/\sqrt5$，与图 [17](#abb-17) 中相同。它们并不互相垂直：$(1,\,1)(1,\,-2)^{\top}=-1\ne0$。
::::

⁠**简而言之：**属于 $\lambda$ 的特征向量是 $(\mathbf{A}-\lambda\mathbf{I})\mathbf{v}=\mathbf{0}$ 的解 $\mathbf{v}\ne\mathbf{0}$；它们与零向量一起构成特征空间。

### 迹与行列式

<span class="anker" id="stufe-6-5"></span>

式 [(6.3)](#gl-6-3) 中出现了两个可以直接从矩阵读出的数：$ad-bc$ 是行列式，$a+d$ 是对角元素之和。这个和有自己的名称。两个数都以简单的方式与特征值相联系，因此可以用来验算。

:::definition 定义 6.5 (迹)
<span class="anker" id="satz-6-5"></span>

方阵 $\mathbf{A}\in\mathbb{R}^{n\times n}$ 的__迹__是它的对角元素之和：

<span class="anker" id="gl-6-4"></span>
$$\operatorname{tr}\mathbf{A}=a_{11}+a_{22}+\dots+a_{nn}=\sum_{i=1}^na_{ii} . \tag{6.4}$$
:::

:::satz 定理 6.6 (由特征值得到迹与行列式)
<span class="anker" id="satz-6-6"></span>

若 $\lambda_1,\dots,\lambda_n$ 是 $\mathbf{A}$ 的特征值（按重数计算并包括复数特征值），则

<span class="anker" id="gl-6-5"></span>
$$\operatorname{tr}\mathbf{A}=\lambda_1+\lambda_2+\dots+\lambda_n,\qquad \det\mathbf{A}=\lambda_1\cdot\lambda_2\cdots\lambda_n . \tag{6.5}$$

此外，对 $\mathbf{A}\in\mathbb{R}^{m\times n}$ 和 $\mathbf{B}\in\mathbb{R}^{n\times m}$，有 $\operatorname{tr}(\mathbf{A}\mathbf{B})=\operatorname{tr}(\mathbf{B}\mathbf{A})$。
:::

:::herleitung 迹与行列式
对于 $n=2$：多项式 $\lambda^2-(a+d)\lambda+(ad-bc)$ 分解为 $(\lambda-\lambda_1)(\lambda-\lambda_2)=\lambda^2-(\lambda_1+\lambda_2)\lambda+\lambda_1\lambda_2$。比较系数得 $a+d=\lambda_1+\lambda_2$ 和 $ad-bc=\lambda_1\lambda_2$。

对于任意 $n$，$p(\lambda)$ 同样分解为 $(\lambda_1-\lambda)(\lambda_2-\lambda)\cdots(\lambda_n-\lambda)$；符号是对的，因为 $\det(\mathbf{A}-\lambda\mathbf{I})$ 中出现的是 $(-\lambda)^n$ 这一项。令 $\lambda=0$，左边得 $\det\mathbf{A}$，右边得 $\lambda_1\cdots\lambda_n$。对于迹，比较 $\lambda^{n-1}$ 的系数。右边的系数为 $(-1)^{n-1}(\lambda_1+\dots+\lambda_n)$。左边，在拉普拉斯展开中只有对角元素之积 $(a_{11}-\lambda)\cdots(a_{nn}-\lambda)$ 能产生 $\lambda$ 这么高的幂次，其系数为 $(-1)^{n-1}(a_{11}+\dots+a_{nn})$。

对于最后一个结论：$\operatorname{tr}(\mathbf{A}\mathbf{B})=\sum_i(\mathbf{A}\mathbf{B})_{ii}=\sum_i\sum_la_{il}b_{li}$，$\operatorname{tr}(\mathbf{B}\mathbf{A})=\sum_l\sum_ib_{li}a_{il}$。这是同一个双重和，只是求和顺序不同。
:::

::::beispiel [算例]
对于 $\mathbf{A}=\bigl(\begin{smallmatrix}4&1\\2&3\end{smallmatrix}\bigr)$，$\operatorname{tr}\mathbf{A}=7=5+2$（图 [18](#abb-18)），$\det\mathbf{A}=10=5\cdot2$。对于 $\bigl(\begin{smallmatrix}5&2\\2&2\end{smallmatrix}\bigr)$，$\operatorname{tr}=7$，$\det=6$；所以特征值是 $\lambda^2-7\lambda+6=0$ 的解，即 $6$ 和 $1$。对于行为 $(1,0,2)$、$(0,1,1)$ 的 $\mathbf{A}\in\mathbb{R}^{2\times3}$ 和 $\mathbf{B}=\mathbf{A}^{\top}$，$\mathbf{A}\mathbf{B}=\bigl(\begin{smallmatrix}5&2\\2&2\end{smallmatrix}\bigr)$，迹为 $7$；$\mathbf{B}\mathbf{A}$ 是一个 $3\times3$ 矩阵，对角元素为 $1$、$1$ 和 $5$，迹同样为 $7$。

:::abbildung ml/k2rspur 18
$\mathbf{A}=\bigl(\begin{smallmatrix}4&1\\2&3\end{smallmatrix}\bigr)$ 的迹作为对角元素之和；它等于特征值 $5$ 与 $2$ 之和。
:::
::::

⁠**简而言之：**迹是对角元素之和，也是特征值之和；行列式是特征值之积。

### 复数特征值

<span class="anker" id="stufe-6-6"></span>

旋转 $90^\circ$ 不会让任何箭头留在它的直线上：每个箭头都再转过一个直角。所以它不可能有实特征向量。特征多项式表明了取而代之的是什么。

::::beispiel [算例 1]
对于旋转 $\bigl(\begin{smallmatrix}0&-1\\1&0\end{smallmatrix}\bigr)$，$p(\lambda)=\lambda^2+1$，根为 $\lambda=\mathrm j$ 和 $\lambda=-\mathrm j$。特征值是纯虚数。复特征向量 $(1,\,-\mathrm j)^{\top}$ 属于 $\lambda=\mathrm j$，因为 $\bigl(\begin{smallmatrix}0&-1\\1&0\end{smallmatrix}\bigr)(1,\,-\mathrm j)^{\top}=(\mathrm j,\,1)^{\top}=\mathrm j\,(1,\,-\mathrm j)^{\top}$。
::::

::::beispiel [算例 2]
第 [1.4](orthonormalbasen-und-orthogonale-matrizen.html#stufe-1-4) 节中的旋转 $\mathbf{Q}=\bigl(\begin{smallmatrix}0.6&-0.8\\0.8&0.6\end{smallmatrix}\bigr)$ 的特征多项式为 $p(\lambda)=\lambda^2-1.2\lambda+1$，由关于复数的算例，其特征值为 $0.6\pm\mathrm j\,0.8=\cos\alpha\pm\mathrm j\sin\alpha=\mathrm e^{\pm\mathrm j\alpha}$，其中 $\alpha\approx53.13^\circ$。一般地，旋转角为 $\alpha$ 的旋转的特征值是 $\mathrm e^{\pm\mathrm j\alpha}$。
::::

所以实矩阵可以有复数特征值。由于它的特征多项式系数为实数，复数特征值成共轭对出现。实特征向量只能属于实特征值：若 $\mathbf{v}$ 是实向量且 $\mathbf{A}\mathbf{v}=\lambda\mathbf{v}$，那么 $\lambda\mathbf{v}$ 作为实向量的像是实的，从而 $\lambda$ 也是实的。复数特征值表明矩阵在某个平面内作旋转。

⁠**简而言之：**实矩阵可以有复数特征值，它们总是成共轭对出现；旋转角为 $\alpha$ 的旋转的特征值为 $\mathrm e^{\pm\mathrm j\alpha}$。

:::hintergrund 旋转就是乘以 $\mathrm e^{\mathrm j\alpha}$
借助复数，可以直接看出这个结果。把箭头 $(x_1,\,x_2)^{\top}$ 与复数 $z=x_1+\mathrm jx_2$ 等同起来，也就是与复平面上的一个点等同起来。于是旋转 $\alpha$ 就是乘以 $\mathrm e^{\mathrm j\alpha}$：$\mathrm e^{\mathrm j\alpha}z=(x_1\cos\alpha-x_2\sin\alpha)+\mathrm j\,(x_1\sin\alpha+x_2\cos\alpha)$，这恰好是[第 1 章第 8.3 节](/wissen/zh/informatik/machine-learning/mathematische-grundlagen/vektoren-und-matrizen/lineare-abbildungen.html#stufe-8-3)中旋转矩阵作用下 $\mathbf{Q}\mathbf{x}$ 的两个分量。因此，在复数写法中，旋转就是乘以一个数，而这个数正是一个特征值。第二个特征值 $\mathrm e^{-\mathrm j\alpha}$ 属于共轭写法 $z^*$，它按相反方向旋转。
:::

### 多重特征值

<span class="anker" id="stufe-6-7"></span>

特征多项式可能有二重根。这时 $n$ 个特征值中有两个重合。一个特征值出现的次数本身就是一个数。

:::definition 定义 6.7 (代数重数)
<span class="anker" id="satz-6-7"></span>

特征值 $\lambda$ 的__代数重数__是 $\lambda$ 作为特征多项式的根的重数。
:::

::::beispiel [算例]
矩阵 $2\mathbf{I}=\operatorname{diag}(2,\,2)$ 的特征多项式为 $p(\lambda)=(2-\lambda)^2$：特征值 $2$ 的代数重数为 $2$。[第 1 章第 8.3 节](/wissen/zh/informatik/machine-learning/mathematische-grundlagen/vektoren-und-matrizen/lineare-abbildungen.html#stufe-8-3)中的剪切 $\bigl(\begin{smallmatrix}1&1\\0&1\end{smallmatrix}\bigr)$ 的特征多项式为 $p(\lambda)=(1-\lambda)^2$：特征值 $1$ 的代数重数也是 $2$。矩阵 $\bigl(\begin{smallmatrix}4&1\\2&3\end{smallmatrix}\bigr)$ 有两个不同的特征值，代数重数都是 $1$。
::::

⁠**简而言之：**代数重数计算一个特征值作为特征多项式的根出现了多少次。

### 特征向量有多少个

<span class="anker" id="stufe-6-8"></span>

上面两个有二重特征值的例子表现完全不同。矩阵 $2\mathbf{I}$ 把每个箭头都拉伸为原长的两倍；每个向量 $\ne\mathbf{0}$ 都是特征向量，特征空间是整个平面。剪切把每个点按其高度向右推移；只有 $x_1$ 轴上的箭头留在自己的直线上。它的特征空间是 $\ker\bigl(\begin{smallmatrix}0&1\\0&0\end{smallmatrix}\bigr)$，即沿 $(1,\,0)^{\top}$ 方向的直线。区别在于特征空间的维数。

:::definition 定义 6.8 (几何重数)
<span class="anker" id="satz-6-8"></span>

特征值的__几何重数__是它的特征空间的维数。
:::

它至少为 $1$，因为每个特征值都有特征向量；它至多等于代数重数，后一点本章不作证明。对于 $2\mathbf{I}$，两种重数都是 $2$；对于剪切，代数重数为 $2$，几何重数为 $1$：剪切缺少一个特征向量。

:::satz 定理 6.9 (不同的特征值，线性无关的特征向量)
<span class="anker" id="satz-6-9"></span>

属于两两不同的特征值 $\lambda_1,\dots,\lambda_k$ 的特征向量 $\mathbf{v}_1,\dots,\mathbf{v}_k$ 线性无关。若 $n\times n$ 矩阵有 $n$ 个不同的特征值，则它的特征向量构成一组基。
:::

:::beweis 线性无关的特征向量
对于两个特征向量：设 $c_1\mathbf{v}_1+c_2\mathbf{v}_2=\mathbf{0}$。作用 $\mathbf{A}$ 得 $c_1\lambda_1\mathbf{v}_1+c_2\lambda_2\mathbf{v}_2=\mathbf{0}$。从中减去第一个等式的 $\lambda_2$ 倍，剩下 $c_1(\lambda_1-\lambda_2)\mathbf{v}_1=\mathbf{0}$。由于 $\lambda_1\ne\lambda_2$ 且 $\mathbf{v}_1\ne\mathbf{0}$，得 $c_1=0$，进而 $c_2=0$。对于更多特征向量，做法相同：如果存在线性相关关系，就取非零系数尽可能少的一个。作用 $\mathbf{A}$，再减去该关系乘以 $\lambda$（所涉及的某个特征值）的结果，就会得到一个非零系数更少的相关关系，矛盾。
:::

::::beispiel [算例]
$\bigl(\begin{smallmatrix}4&1\\2&3\end{smallmatrix}\bigr)$ 的特征向量 $(1,\,1)^{\top}$ 和 $(1,\,-2)^{\top}$ 属于不同的特征值 $5$ 和 $2$；它们线性无关，因为 $\det\bigl(\begin{smallmatrix}1&1\\1&-2\end{smallmatrix}\bigr)=-3\ne0$。相反，剪切只有特征方向 $(1,\,0)^{\top}$；它没有两个线性无关的特征向量。
::::

⁠**简而言之：**几何重数计算一个特征值有多少个线性无关的特征向量；它可能小于代数重数，但不同的特征值总有线性无关的特征向量。

### 特征值的运算规则

<span class="anker" id="stufe-6-9"></span>

知道一个矩阵的特征向量，也就知道了许多由它构造出的矩阵的特征向量。这些规则都直接由式 [(6.1)](#gl-6-1) 得出。

:::satz 定理 6.10 (运算规则)
<span class="anker" id="satz-6-10"></span>

设 $\mathbf{A}\mathbf{v}=\lambda\mathbf{v}$，$\mathbf{v}\ne\mathbf{0}$。则：

<ol class="rm">

<li>

对每个自然数 $k$，$\mathbf{A}^k\mathbf{v}=\lambda^k\mathbf{v}$；

</li>

<li>

对每个数 $\beta$，$(\mathbf{A}+\beta\mathbf{I})\mathbf{v}=(\lambda+\beta)\mathbf{v}$；

</li>

<li>

$\mathbf{A}$ 可逆当且仅当没有特征值为零，此时 $\mathbf{A}^{-1}\mathbf{v}=\frac1\lambda\mathbf{v}$；

</li>

<li>

$\mathbf{A}^{\top}$ 与 $\mathbf{A}$ 有相同的特征值，但一般有不同的特征向量。

</li>

</ol>
:::

:::beweis 运算规则
(i) $\mathbf{A}^2\mathbf{v}=\mathbf{A}(\lambda\mathbf{v})=\lambda\mathbf{A}\mathbf{v}=\lambda^2\mathbf{v}$，依此类推。(ii) $(\mathbf{A}+\beta\mathbf{I})\mathbf{v}=\lambda\mathbf{v}+\beta\mathbf{v}$。(iii) 由式 [(6.5)](#gl-6-5)，$\det\mathbf{A}$ 是特征值之积，所以它不为零，当且仅当没有特征值为零。把 $\mathbf{A}\mathbf{v}=\lambda\mathbf{v}$ 乘以 $\mathbf{A}^{-1}$，得 $\mathbf{v}=\lambda\mathbf{A}^{-1}\mathbf{v}$。(iv) 由[第 1 章第 14.5 节](/wissen/zh/informatik/machine-learning/mathematische-grundlagen/vektoren-und-matrizen/die-determinante.html#stufe-14-5)，$\det(\mathbf{A}^{\top}-\lambda\mathbf{I})=\det\bigl((\mathbf{A}-\lambda\mathbf{I})^{\top}\bigr)=\det(\mathbf{A}-\lambda\mathbf{I})$；二者有相同的特征多项式。
:::

::::beispiel [算例]
对于 $\mathbf{A}=\bigl(\begin{smallmatrix}4&1\\2&3\end{smallmatrix}\bigr)$，矩阵 $\mathbf{A}^2=\bigl(\begin{smallmatrix}18&7\\14&11\end{smallmatrix}\bigr)$ 的特征值为 $25$ 和 $4$：$\mathbf{A}^2(1,\,1)^{\top}=(25,\,25)^{\top}$。矩阵 $\mathbf{A}-5\mathbf{I}$ 的特征值为 $0$ 和 $-3$，它不可逆。逆矩阵 $\mathbf{A}^{-1}=\tfrac1{10}\bigl(\begin{smallmatrix}3&-1\\-2&4\end{smallmatrix}\bigr)$ 的特征值为 $\tfrac15$ 和 $\tfrac12$：$\mathbf{A}^{-1}(1,\,-2)^{\top}=\tfrac1{10}(5,\,-10)^{\top}=\tfrac12(1,\,-2)^{\top}$。转置 $\mathbf{A}^{\top}=\bigl(\begin{smallmatrix}4&2\\1&3\end{smallmatrix}\bigr)$ 的特征值同样是 $5$ 和 $2$，但 $\mathbf{A}^{\top}(1,\,1)^{\top}=(6,\,4)^{\top}$：它的特征向量是 $(2,\,1)^{\top}$ 和 $(1,\,-1)^{\top}$。
::::

⁠**简而言之：**幂、平移 $\beta\mathbf{I}$ 和求逆保持特征向量不变，并以同样的方式改变特征值；转置只保持特征值不变。

:::aufgabe 练习 17 ★ 特征值与特征向量
<span class="anker" id="aufg-17"></span>

求下列矩阵的特征值和特征空间：

$$\mathbf{A}_1=\begin{pmatrix}2&2\\1&3\end{pmatrix},\qquad \mathbf{A}_2=\begin{pmatrix}3&0\\0&3\end{pmatrix},\qquad \mathbf{A}_3=\begin{pmatrix}1&3\\3&1\end{pmatrix}.$$

每次都验算迹和行列式。哪个矩阵的特征向量互相垂直？

:::loesung
$\mathbf{A}_1$：迹为 $5$，行列式为 $6-2=4$，所以 $\lambda^2-5\lambda+4=(\lambda-4)(\lambda-1)$。对于 $\lambda=4$：$\mathbf{A}_1-4\mathbf{I}=\bigl(\begin{smallmatrix}-2&2\\1&-1\end{smallmatrix}\bigr)$，特征空间沿 $(1,\,1)^{\top}$ 方向。对于 $\lambda=1$：$\mathbf{A}_1-\mathbf{I}=\bigl(\begin{smallmatrix}1&2\\1&2\end{smallmatrix}\bigr)$，特征空间沿 $(2,\,-1)^{\top}$ 方向。验算：$4+1=5$，$4\cdot1=4$。两个特征向量不垂直：$(1,\,1)(2,\,-1)^{\top}=1$。

$\mathbf{A}_2=3\mathbf{I}$：$p(\lambda)=(3-\lambda)^2$，特征值 $3$ 是二重的；特征空间是整个平面。验算：$3+3=6$，$3\cdot3=9$。可以选两个互相垂直的特征向量，例如 $\mathbf{e}_1$ 和 $\mathbf{e}_2$，但也可以选两个斜交的。

$\mathbf{A}_3$：迹为 $2$，行列式为 $1-9=-8$，所以 $\lambda^2-2\lambda-8=(\lambda-4)(\lambda+2)$。特征向量：属于 $4$ 的 $(1,\,1)^{\top}$ 和属于 $-2$ 的 $(1,\,-1)^{\top}$。验算：$4-2=2$，$4\cdot(-2)=-8$。它们互相垂直；$\mathbf{A}_3$ 是对称的，第 [7.5](diagonalisierung-und-spektralsatz.html#stufe-7-5) 节说明这并非巧合。
:::
:::

:::aufgabe 练习 18 ★ 三角矩阵
<span class="anker" id="aufg-18"></span>

证明：上三角矩阵的特征值就是它的对角元素。求 $\Bigl(\begin{smallmatrix}2&1&0\\0&3&1\\0&0&5\end{smallmatrix}\Bigr)$ 的特征值和特征向量。

:::loesung
对于上三角矩阵，$\mathbf{A}-\lambda\mathbf{I}$ 仍是上三角矩阵，其对角元素为 $a_{ii}-\lambda$。由[第 1 章第 14.4 节](/wissen/zh/informatik/machine-learning/mathematische-grundlagen/vektoren-und-matrizen/die-determinante.html#stufe-14-4)，它的行列式等于对角元素之积：$p(\lambda)=(a_{11}-\lambda)\cdots(a_{nn}-\lambda)$。它的根就是各对角元素。

因此，给定矩阵的特征值为 $2$、$3$ 和 $5$。对于 $2$：$\mathbf{A}-2\mathbf{I}=\Bigl(\begin{smallmatrix}0&1&0\\0&1&1\\0&0&3\end{smallmatrix}\Bigr)$ 要求 $v_3=0$ 和 $v_2=0$，特征向量为 $(1,\,0,\,0)^{\top}$。对于 $3$：$\Bigl(\begin{smallmatrix}-1&1&0\\0&0&1\\0&0&2\end{smallmatrix}\Bigr)$ 要求 $v_3=0$ 和 $v_2=v_1$，特征向量为 $(1,\,1,\,0)^{\top}$。对于 $5$：$\Bigl(\begin{smallmatrix}-3&1&0\\0&-2&1\\0&0&0\end{smallmatrix}\Bigr)$ 要求 $v_2=3v_1$ 和 $v_3=2v_2$，特征向量为 $(1,\,3,\,6)^{\top}$。验算：$\mathbf{A}(1,\,3,\,6)^{\top}=(2+3,\ 9+6,\ 30)^{\top}=5\,(1,\,3,\,6)^{\top}$。
:::
:::

:::aufgabe 练习 19 ★★ 重数
<span class="anker" id="aufg-19"></span>

对于 $\mathbf{B}_1=\bigl(\begin{smallmatrix}2&0\\0&2\end{smallmatrix}\bigr)$、$\mathbf{B}_2=\bigl(\begin{smallmatrix}2&3\\0&2\end{smallmatrix}\bigr)$ 和 $\mathbf{B}_3=\Bigl(\begin{smallmatrix}1&0&0\\0&1&1\\0&0&1\end{smallmatrix}\Bigr)$，求出所有特征值及其代数重数和几何重数。

:::loesung
$\mathbf{B}_1=2\mathbf{I}$：特征值 $2$，代数重数 $2$，特征空间是整个平面，几何重数 $2$。

$\mathbf{B}_2$：三角矩阵，特征值 $2$，代数重数 $2$。$\mathbf{B}_2-2\mathbf{I}=\bigl(\begin{smallmatrix}0&3\\0&0\end{smallmatrix}\bigr)$ 要求 $v_2=0$；特征空间是 $x_1$ 轴，几何重数 $1$。与剪切一样，$\mathbf{B}_2$ 缺少一个特征向量。

$\mathbf{B}_3$：三角矩阵，特征值 $1$，代数重数 $3$。$\mathbf{B}_3-\mathbf{I}=\Bigl(\begin{smallmatrix}0&0&0\\0&0&1\\0&0&0\end{smallmatrix}\Bigr)$ 只要求 $v_3=0$；特征空间为 $\operatorname{span}\{\mathbf{e}_1,\mathbf{e}_2\}$，几何重数 $2$。这里几何重数介于 $1$ 和代数重数之间。
:::
:::

:::aufgabe 练习 20 ★★ 一个旋转和一个反射
<span class="anker" id="aufg-20"></span>

<ol class="al">

<li>

计算旋转 $30^\circ$ 的特征值，并写成 $\mathrm e^{\pm\mathrm j\alpha}$ 的形式。

</li>

<li>

第 [1.5](orthonormalbasen-und-orthogonale-matrizen.html#stufe-1-5) 节中的反射 $\bigl(\begin{smallmatrix}0.6&0.8\\0.8&-0.6\end{smallmatrix}\bigr)$ 也是正交矩阵。求它的特征值和特征向量，并从几何上加以解释。

</li>

<li>

证明：正交矩阵的每个实特征值都是 $1$ 或 $-1$。

</li>

</ol>

:::loesung
(a) 旋转 $30^\circ$ 的矩阵为 $\bigl(\begin{smallmatrix}\sqrt3/2&-1/2\\1/2&\sqrt3/2\end{smallmatrix}\bigr)$，迹为 $\sqrt3$，行列式为 $1$。所以 $p(\lambda)=\lambda^2-\sqrt3\,\lambda+1$，且

$$\lambda=\frac{\sqrt3\pm\sqrt{3-4}}2=\frac{\sqrt3}2\pm\mathrm j\,\frac12=\cos30^\circ\pm\mathrm j\sin30^\circ=\mathrm e^{\pm\mathrm j\,30^\circ} .$$

(b) 迹为 $0$，行列式为 $-0.36-0.64=-1$，所以 $p(\lambda)=\lambda^2-1$，特征值为 $1$ 和 $-1$。对于 $1$：$\bigl(\begin{smallmatrix}-0.4&0.8\\0.8&-1.6\end{smallmatrix}\bigr)$，特征向量为 $(2,\,1)^{\top}$。对于 $-1$：$\bigl(\begin{smallmatrix}1.6&0.8\\0.8&0.4\end{smallmatrix}\bigr)$，特征向量为 $(1,\,-2)^{\top}$。从几何上看：沿 $(2,\,1)^{\top}$ 方向的反射轴上的点保持不动，特征值为 $1$；与之垂直的方向被翻转，特征值为 $-1$。两个特征向量互相垂直，因为矩阵是对称的。

(c) 设 $\mathbf{Q}\mathbf{v}=\lambda\mathbf{v}$，其中 $\lambda$ 为实数，$\mathbf{v}\ne\mathbf{0}$ 为实向量。由式 [(1.3)](orthonormalbasen-und-orthogonale-matrizen.html#gl-1-3)，$\lVert\mathbf{v}\rVert=\lVert\mathbf{Q}\mathbf{v}\rVert=|\lambda|\,\lVert\mathbf{v}\rVert$，所以 $|\lambda|=1$，$\lambda=\pm1$。对于留在自身直线上的箭头，刚体运动只能让它保持原样或将它翻转，而不能拉伸它。
:::
:::
