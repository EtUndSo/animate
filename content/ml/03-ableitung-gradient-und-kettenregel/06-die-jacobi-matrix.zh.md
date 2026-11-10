---
title: 雅可比矩阵
pfad: 计算机科学 / 机器学习 / 数学基础 / 导数、梯度与链式法则
adresse: informatik/machine-learning/mathematische-grundlagen/ableitung-gradient-und-kettenregel
knoten: 第 3 章：导数、梯度与链式法则
nachschlagen: ja
order: 15230600
summary: 许多计算步骤给出的不是一个数，而是好几个数：矩阵-向量乘积把一个向量变成另一个向量。对这样的函数，雅可比矩阵汇集了所有输出对所有输入的偏导数。它是线性近似的矩阵；对两种最常见的构件，即线性映射和逐元素函数，它的形式特别简单。
tags: 向量值, 雅可比矩阵
lang: zh
---

<span class="anker" id="stufe-5"></span>

:::zweck
许多计算步骤给出的不是一个数，而是好几个数：矩阵-向量乘积把一个向量变成另一个向量。对这样的函数，雅可比矩阵汇集了所有输出对所有输入的偏导数。它是线性近似的矩阵；对两种最常见的构件，即线性映射和逐元素函数，它的形式特别简单。
:::

### 有多个输出的函数

<span class="anker" id="stufe-5-1"></span>

在[第 1 章第 8 节](/wissen/zh/informatik/machine-learning/mathematische-grundlagen/vektoren-und-matrizen/lineare-abbildungen.html#stufe-8)中，线性映射 $\mathbf{x}\mapsto\mathbf{A}\mathbf{x}$ 把 $\mathbb{R}^n$ 中的向量映射为 $\mathbb{R}^m$ 中的向量；在[第 1 章第 15.2 节](/wissen/zh/informatik/machine-learning/mathematische-grundlagen/vektoren-und-matrizen/elementweise-rechnen-und-tensoren.html#stufe-15-2)中，一个函数被分别作用于向量的每个分量。在这两种情况下，从一个向量都得出好几个数。其中每个数本身都是一个多元函数。

:::definition 定义 5.1 (向量值函数)
<span class="anker" id="satz-5-1"></span>

函数 $\mathbf{g}:\mathbb{R}^n\to\mathbb{R}^m$ 把每个 $\mathbf{x}\in\mathbb{R}^n$ 对应到一个向量

$$\mathbf{g}(\mathbf{x})=\begin{pmatrix}g_1(\mathbf{x})\\ \vdots\\ g_m(\mathbf{x})\end{pmatrix}\in\mathbb{R}^m$$

这样的函数称为__向量值__函数。函数 $g_1,\dots,g_m:\mathbb{R}^n\to\mathbb{R}$ 称为它的分量函数。
:::

本章把向量值函数像向量一样用粗体表示；函数值为一个数的函数用非粗体表示。

::::beispiel [算例]
在第 [5](#stufe-5) 节和第 [6](die-kettenregel-fur-mehrere-variablen.html#stufe-6) 节中，我们一直使用如下函数 $\mathbf{g}:\mathbb{R}^2\to\mathbb{R}^2$：

<span class="anker" id="gl-5-1"></span>
$$\mathbf{g}(\mathbf{x})=\begin{pmatrix}x_1x_2\\ 2x_1+x_2^2\end{pmatrix},\qquad \mathbf{g}(1,2)=\begin{pmatrix}2\\6\end{pmatrix}. \tag{5.1}$$

它的分量函数是 $g_1(\mathbf{x})=x_1x_2$ 和 $g_2(\mathbf{x})=2x_1+x_2^2$。
::::

⁠**简而言之：**向量值函数 $\mathbf{g}:\mathbb{R}^n\to\mathbb{R}^m$ 由 $m$ 个 $n$ 元函数组成，每个输出对应一个。

### 雅可比矩阵

<span class="anker" id="stufe-5-2"></span>

每个分量函数 $g_i$ 都有 $n$ 个偏导数，对每个输入各有一个。合起来共有 $m\cdot n$ 个数。把它们排成一张表格，每个输出占一行，每个输入占一列。

:::definition 定义 5.2 (雅可比矩阵)
<span class="anker" id="satz-5-2"></span>

如果 $\mathbf{g}:\mathbb{R}^n\to\mathbb{R}^m$ 的各分量函数的所有偏导数在点 $\mathbf{x}$ 处都存在，就称 $m\times n$ 矩阵

<span class="anker" id="gl-5-2"></span>
$$\mathbf{J}_{\mathbf{g}}(\mathbf{x})=\begin{pmatrix}\dfrac{\partial g_1}{\partial x_1}&\cdots&\dfrac{\partial g_1}{\partial x_n}\\ \vdots&&\vdots\\ \dfrac{\partial g_m}{\partial x_1}&\cdots&\dfrac{\partial g_m}{\partial x_n}\end{pmatrix},\qquad \bigl(\mathbf{J}_{\mathbf{g}}(\mathbf{x})\bigr)_{ij}=\frac{\partial g_i}{\partial x_j}(\mathbf{x}), \tag{5.2}$$

为 $\mathbf{g}$ 在点 $\mathbf{x}$ 处的__雅可比矩阵__。
:::

第 $i$ 行属于输出 $g_i$；它是这个输出的梯度，写成一行：$\nabla g_i(\mathbf{x})^{\top}$。第 $j$ 列属于输入 $x_j$；它说明只改变 $x_j$ 时所有输出同时怎样反应。对只有一个输出的函数 $f:\mathbb{R}^n\to\mathbb{R}$，雅可比矩阵是一个 $1\times n$ 矩阵，即写成一行的梯度：$\mathbf{J}_f(\mathbf{x})=\nabla f(\mathbf{x})^{\top}$。这个矩阵以数学家卡尔·古斯塔夫·雅各布·雅可比（Carl Gustav Jacob Jacobi）命名。

::::beispiel [算例]
对于式 [(5.1)](#gl-5-1) 中的 $\mathbf{g}$，有

$$\mathbf{J}_{\mathbf{g}}(\mathbf{x})=\begin{pmatrix}x_2&x_1\\2&2x_2\end{pmatrix},\qquad \mathbf{J}_{\mathbf{g}}(1,2)=\begin{pmatrix}2&1\\2&4\end{pmatrix}.$$

第一列 $(2,\,2)^{\top}$ 说明：$x_1$ 增加一个小量 $h$ 时，两个输出都增加约 $2h$。第二列 $(1,\,4)^{\top}$ 说明：$x_2$ 增加时，第二个输出的反应是第一个输出的四倍。
::::

⁠**简而言之：**雅可比矩阵的每一行对应一个输出，每一列对应一个输入；它的元素 $(i,j)$ 是 $\partial g_i/\partial x_j$。

### 用雅可比矩阵作线性近似

<span class="anker" id="stufe-5-3"></span>

每个分量函数都有自己的线性近似式 [(3.4)](partielle-ableitungen-und-der-gradient.html#gl-3-4)。把所有 $m$ 个近似式上下排列起来，左边是 $\mathbf{g}(\mathbf{x}+\mathbf{h})$ 的各分量，右边是雅可比矩阵的各行乘以 $\mathbf{h}$。按照[第 1 章第 7.2 节](/wissen/zh/informatik/machine-learning/mathematische-grundlagen/vektoren-und-matrizen/das-matrix-vektor-produkt.html#stufe-7-2)的行视角，这就是一个矩阵-向量乘积。

:::satz 定理 5.3 (向量值函数的线性近似)
<span class="anker" id="satz-5-3"></span>

如果 $\mathbf{g}$ 的每个分量函数都在点 $\mathbf{x}$ 处可微，那么

<span class="anker" id="gl-5-3"></span>
$$\mathbf{g}(\mathbf{x}+\mathbf{h})=\mathbf{g}(\mathbf{x})+\mathbf{J}_{\mathbf{g}}(\mathbf{x})\,\mathbf{h}+\mathbf{r}(\mathbf{h})\qquad\text{其中}\qquad\lim_{\mathbf{h}\to\mathbf{0}}\frac{\lVert\mathbf{r}(\mathbf{h})\rVert}{\lVert\mathbf{h}\rVert}=0 . \tag{5.3}$$
:::

:::beweis 向量值函数的线性近似
$\mathbf{J}_{\mathbf{g}}(\mathbf{x})\,\mathbf{h}$ 的第 $i$ 个分量是 $\nabla g_i(\mathbf{x})^{\top}\mathbf{h}$。由可微性的定义式 [(3.5)](partielle-ableitungen-und-der-gradient.html#gl-3-5)，对每个 $i$，商 $r_i(\mathbf{h})/\lVert\mathbf{h}\rVert$ 都趋于 $0$。由于 $\lVert\mathbf{r}\rVert\le|r_1|+\dots+|r_m|$，$\lVert\mathbf{r}(\mathbf{h})\rVert/\lVert\mathbf{h}\rVert$ 也趋于 $0$。
:::

因此在 $\mathbf{x}$ 附近，$\mathbf{g}$ 的作用就像线性映射 $\mathbf{h}\mapsto\mathbf{J}_{\mathbf{g}}(\mathbf{x})\,\mathbf{h}$；而由[第 1 章第 8.2 节](/wissen/zh/informatik/machine-learning/mathematische-grundlagen/vektoren-und-matrizen/lineare-abbildungen.html#stufe-8-2)，每个线性映射恰好对应一个矩阵。雅可比矩阵就是这个矩阵。在放大镜下，$\mathbf{g}$ 使 $\mathbf{x}$ 周围的小网格发生的变形，与矩阵 $\mathbf{J}_{\mathbf{g}}(\mathbf{x})$ 使单位网格发生的变形相同：网格被旋转、拉伸或剪切，但直线仍然几乎是直的。

::::beispiel [算例]
对于式 [(5.1)](#gl-5-1) 中的 $\mathbf{g}$ 在点 $(1,\,2)$ 处、$\mathbf{h}=(0.1,\ -0.1)^{\top}$，有

$$\mathbf{J}_{\mathbf{g}}(1,2)\,\mathbf{h}=\begin{pmatrix}2\cdot0.1+1\cdot(-0.1)\\2\cdot0.1+4\cdot(-0.1)\end{pmatrix}=\begin{pmatrix}0.1\\-0.2\end{pmatrix}, \qquad \mathbf{g}(1.1,\ 1.9)\approx\begin{pmatrix}2.1\\5.8\end{pmatrix}.$$

精确值是 $\mathbf{g}(1.1,\ 1.9)=(2.09,\ 5.81)^{\top}$。图 [10](#abb-10) 逐行展示了这个乘积。

:::abbildung ml/k3rjacobi 10
$\mathbf{g}$ 在点 $\mathbf{x}=(1,\,2)^{\top}$ 处的线性近似中的变化量，写成矩阵-向量乘积：每一行都是一个输出的梯度与位移的点积。
:::
::::

⁠**简而言之：**在 $\mathbf{x}$ 附近，$\mathbf{g}(\mathbf{x}+\mathbf{h})\approx\mathbf{g}(\mathbf{x})+\mathbf{J}_{\mathbf{g}}(\mathbf{x})\,\mathbf{h}$；雅可比矩阵是 $\mathbf{g}$ 在局部所表现出的那个线性映射的矩阵。

### 两个重要的雅可比矩阵

<span class="anker" id="stufe-5-4"></span>

有两种构件在数据计算中随处可见：矩阵-向量乘积，以及分别作用于每个分量的函数。它们的雅可比矩阵一再用到，而且两者都不用计算就能写出来。

:::satz 定理 5.4 (各构件的雅可比矩阵)
<span class="anker" id="satz-5-4"></span>

<ol class="al">

<li>

对于 $\mathbf{g}(\mathbf{x})=\mathbf{A}\mathbf{x}+\mathbf{b}$，其中 $\mathbf{A}\in\mathbb{R}^{m\times n}$，$\mathbf{b}\in\mathbb{R}^m$，在每一点都有 $\mathbf{J}_{\mathbf{g}}(\mathbf{x})=\mathbf{A}$。

</li>

<li>

如果 $\mathbf{g}:\mathbb{R}^n\to\mathbb{R}^n$ 把一个可导的一元函数 $\varphi$ 作用于每个分量，即 $g_i(\mathbf{x})=\varphi(x_i)$，那么

<span class="anker" id="gl-5-4"></span>
$$\mathbf{J}_{\mathbf{g}}(\mathbf{x})=\operatorname{diag}\bigl(\varphi'(x_1),\,\dots,\,\varphi'(x_n)\bigr). \tag{5.4}$$

</li>

</ol>
:::

:::beweis 各构件的雅可比矩阵
(a) 第 $i$ 个分量是 $g_i(\mathbf{x})=\sum_ka_{ik}x_k+b_i$。对 $x_j$ 求导后，只剩下 $k=j$ 的那一项，所以 $\partial g_i/\partial x_j=a_{ij}$。(b) 分量 $g_i=\varphi(x_i)$ 只依赖于 $x_i$。因此它对 $x_j$ 的导数在 $j\ne i$ 时为 $0$，在 $j=i$ 时为 $\varphi'(x_i)$。
:::

这两个结果都有一个简单的原因。仿射映射除了平移 $\mathbf{b}$ 之外本来就是线性的；它的最佳线性近似就是去掉 $\mathbf{b}$ 的它自己。对于逐元素函数，每个输入只作用于它自己的输出；对角线以外的所有元素都为零，因为不同的分量之间没有联系。

::::beispiel [算例]
对于 $\mathbf{A}=\bigl(\begin{smallmatrix}1&2\\0&-1\\3&1\end{smallmatrix}\bigr)$，$\mathbf{x}\mapsto\mathbf{A}\mathbf{x}$ 的雅可比矩阵处处都是 $\mathbf{A}$ 本身。把每个分量平方，即 $\varphi(t)=t^2$，那么在点 $\mathbf{x}=(1,\,-2,\,3)^{\top}$ 处，雅可比矩阵为 $\operatorname{diag}(2,\,-4,\,6)$。把逻辑斯谛函数作用于 $\mathbf{x}=(0,\,2)^{\top}$ 的每个分量，由式 [(2.4)](die-kettenregel.html#gl-2-4)，雅可比矩阵为 $\operatorname{diag}\bigl(\sigma'(0),\,\sigma'(2)\bigr)\approx\operatorname{diag}(0.25,\ 0.105)$。
::::

⁠**简而言之：**$\mathbf{x}\mapsto\mathbf{A}\mathbf{x}+\mathbf{b}$ 的雅可比矩阵是 $\mathbf{A}$；逐元素函数的雅可比矩阵是由各个导数组成的对角矩阵。

:::hintergrund 雅可比矩阵的行列式作为面积因子
由[第 1 章第 14.3 节](/wissen/zh/informatik/machine-learning/mathematische-grundlagen/vektoren-und-matrizen/die-determinante.html#stufe-14-3)，线性映射把每个图形的面积都乘以同一个因子 $|\det\mathbf{A}|$。由于 $\mathbf{g}$ 在局部的作用像 $\mathbf{J}_{\mathbf{g}}(\mathbf{x})$，这对 $\mathbf{g}$ 也近似成立：$\mathbf{x}$ 周围面积为 $F$ 的小正方形变成一个近似于平行四边形的图形，其面积为 $|\det\mathbf{J}_{\mathbf{g}}(\mathbf{x})|\cdot F$。对于式 [(5.1)](#gl-5-1) 中的 $\mathbf{g}$，$\det\mathbf{J}_{\mathbf{g}}(1,2)=2\cdot4-1\cdot2=6$：在 $(1,\,2)$ 附近，$\mathbf{g}$ 把面积放大到大约六倍。一个著名的例子是极坐标 $\mathbf{g}(r,\varphi)=(r\cos\varphi,\ r\sin\varphi)^{\top}$。它的雅可比矩阵的两列是 $(\cos\varphi,\,\sin\varphi)^{\top}$ 和 $(-r\sin\varphi,\,r\cos\varphi)^{\top}$，行列式为 $r\cos^2\varphi+r\sin^2\varphi=r$。边长为 $\Delta r$ 和 $\Delta\varphi$ 的小长方形变成圆环的一小块，面积约为 $r\,\Delta r\,\Delta\varphi$，因为距离为 $r$、角度为 $\Delta\varphi$ 的弧长为 $r\,\Delta\varphi$。
:::

:::aufgabe 练习 17 ★ 计算雅可比矩阵
<span class="anker" id="aufg-17"></span>

计算在给定点处的雅可比矩阵。

<ol class="al">

<li>

$\mathbf{g}(\mathbf{x})=(x_1+x_2,\ x_1-x_2,\ x_1x_2)^{\top}$，在点 $(3,\,1)$ 处；

</li>

<li>

$\mathbf{g}(\mathbf{x})=(\mathrm{e}^{x_1},\,\mathrm{e}^{x_2},\,\mathrm{e}^{x_3})^{\top}$，在点 $(0,\,1,\,-1)$ 处；

</li>

<li>

式 [(3.1)](partielle-ableitungen-und-der-gradient.html#gl-3-1) 中的 $f(\mathbf{x})=x_1^2x_2+x_2^2$，在点 $(1,\,2)$ 处。这个矩阵是什么形状？它是什么？

</li>

</ol>

:::loesung
(a) 雅可比矩阵有三行两列：

$$\mathbf{J}_{\mathbf{g}}(\mathbf{x})=\begin{pmatrix}1&1\\1&-1\\x_2&x_1\end{pmatrix},\qquad \mathbf{J}_{\mathbf{g}}(3,1)=\begin{pmatrix}1&1\\1&-1\\1&3\end{pmatrix}.$$

(b) 这个函数是逐元素的；由式 [(5.4)](#gl-5-4)，$\mathbf{J}=\operatorname{diag}(\mathrm{e}^0,\,\mathrm{e}^1,\,\mathrm{e}^{-1})\approx\operatorname{diag}(1,\ 2.718,\ 0.368)$。

(c) 只有一个输出的函数有一个 $1\times2$ 的雅可比矩阵，也就是写成一行的梯度：$\mathbf{J}_f(1,2)=(4\ \ 5)=\nabla f(1,2)^{\top}$。
:::
:::

:::aufgabe 练习 18 ★★ 平面映射的线性近似
<span class="anker" id="aufg-18"></span>

设 $\mathbf{g}(\mathbf{x})=(x_1^2-x_2,\ x_1x_2)^{\top}$。

<ol class="al">

<li>

计算 $\mathbf{J}_{\mathbf{g}}(2,1)$，并用它求 $\mathbf{g}(2.05,\ 0.9)$ 的近似值。与精确值比较。

</li>

<li>

怎样移动输入，才能使第一个输出改变，而第二个输出在线性近似下完全不变？给出一个这样的位移 $\mathbf{h}$。

</li>

</ol>

:::loesung
(a) $\mathbf{J}_{\mathbf{g}}(\mathbf{x})=\bigl(\begin{smallmatrix}2x_1&-1\\x_2&x_1\end{smallmatrix}\bigr)$，所以 $\mathbf{J}_{\mathbf{g}}(2,1)=\bigl(\begin{smallmatrix}4&-1\\1&2\end{smallmatrix}\bigr)$，并且 $\mathbf{g}(2,1)=(3,\,2)^{\top}$。取 $\mathbf{h}=(0.05,\ -0.1)^{\top}$，有

$$\mathbf{J}_{\mathbf{g}}\mathbf{h}=\begin{pmatrix}0.2+0.1\\0.05-0.2\end{pmatrix}=\begin{pmatrix}0.3\\-0.15\end{pmatrix},\qquad \mathbf{g}(2.05,\ 0.9)\approx\begin{pmatrix}3.3\\1.85\end{pmatrix}.$$

精确值是 $\mathbf{g}(2.05,\ 0.9)=(4.2025-0.9,\ 1.845)^{\top}=(3.3025,\ 1.845)^{\top}$。

(b) 在线性近似下，第二个输出改变 $h_1+2h_2$；对于沿方向 $(2,\,-1)^{\top}$ 的 $\mathbf{h}$，它为零。沿这个向量恰好走一步时，第一个输出改变 $4\cdot2-1\cdot(-1)=9$。所以两个输入都必须改变：$x_1$ 增大，$x_2$ 减小，减小量是增大量的一半，例如 $\mathbf{h}=(0.02,\ -0.01)^{\top}$，其作用为 $(0.09,\ 0)^{\top}$。
:::
:::

:::aufgabe 练习 19 ★★★ $\mathbf{g}$ 把面积放大多少
<span class="anker" id="aufg-19"></span>

设 $\mathbf{g}$ 如式 [(5.1)](#gl-5-1)。

<ol class="al">

<li>

计算以 $(1,\,2)$、$(1.1,\ 2)$、$(1.1,\ 2.1)$ 和 $(1,\ 2.1)$ 为顶点的正方形的四个顶点的像。

</li>

<li>

这些像几乎构成一个平行四边形。用从 $\mathbf{g}(1,2)$ 出发的两条边的像估计它的面积，并与 $|\det\mathbf{J}_{\mathbf{g}}(1,2)|\cdot0.01$ 比较。

</li>

</ol>

:::loesung
(a) 由 $\mathbf{g}(\mathbf{x})=(x_1x_2,\ 2x_1+x_2^2)^{\top}$：

$$\mathbf{g}(1,2)=\begin{pmatrix}2\\6\end{pmatrix},\quad \mathbf{g}(1.1,\,2)=\begin{pmatrix}2.2\\6.2\end{pmatrix},\quad \mathbf{g}(1.1,\,2.1)=\begin{pmatrix}2.31\\6.61\end{pmatrix},\quad \mathbf{g}(1,\,2.1)=\begin{pmatrix}2.1\\6.41\end{pmatrix}.$$

(b) 从 $\mathbf{g}(1,2)$ 出发的两条边的像是 $(0.2,\ 0.2)^{\top}$ 和 $(0.1,\ 0.41)^{\top}$。由[第 1 章第 14.1 节](/wissen/zh/informatik/machine-learning/mathematische-grundlagen/vektoren-und-matrizen/die-determinante.html#stufe-14-1)，它们张成的平行四边形的面积为 $|0.2\cdot0.41-0.1\cdot0.2|=0.062$。雅可比矩阵预测的是 $|\det\mathbf{J}_{\mathbf{g}}(1,2)|\cdot0.01=6\cdot0.01=0.06$。偏差的原因是这个正方形并非任意小；第四个顶点位于 $(2.31,\ 6.61)$，也只是几乎落在一个真正的平行四边形应有的位置 $(2.3,\ 6.61)$ 上。
:::
:::
