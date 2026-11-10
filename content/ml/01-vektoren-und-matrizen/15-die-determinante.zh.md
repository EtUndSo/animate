---
title: 行列式
pfad: 计算机科学 / 机器学习 / 数学基础 / 向量与矩阵
adresse: informatik/machine-learning/mathematische-grundlagen/vektoren-und-matrizen
knoten: 第 1 章：向量与矩阵
nachschlagen: ja
order: 15211500
summary: 线性映射使平面的网格变形，面积在此过程中变大或变小。本节求出面积变化的倍数。这个倍数是单独一个数，即行列式，它还说明矩阵是否可逆。
tags: 行列式, 定向, 拉普拉斯展开
lang: zh
---

<span class="anker" id="stufe-14"></span>

:::zweck
线性映射使平面的网格变形，面积在此过程中变大或变小。本节求出面积变化的倍数。这个倍数是单独一个数，即行列式，它还说明矩阵是否可逆。
:::

### $2\times2$ 矩阵的行列式

<span class="anker" id="stufe-14-1"></span>

单位正方形的面积为 $1$。矩阵 $\mathbf{A}$ 把它映射为由它的两列张成的平行四边形（第 [8.3](lineare-abbildungen.html#stufe-8-3) 小节）。这个平行四边形的面积有多大？图 [40](#abb-40) 对 $\mathbf{A}=\bigl(\begin{smallmatrix}3&1\\1&2\end{smallmatrix}\bigr)$ 展示了这一点。

:::abbildung ml/k1det 40
左：面积为 $1$ 的单位正方形；右：它在 $\mathbf{A}=\bigl(\begin{smallmatrix}3&1\\1&2\end{smallmatrix}\bigr)$ 作用下的像，即由列 $\mathbf{a}_1$ 和 $\mathbf{a}_2$ 构成的平行四边形。它的面积为 $5=3\cdot2-1\cdot1$。虚线：外接矩形，可以借助它算出面积。
:::

:::herleitung 平行四边形的面积
设两列为 $\mathbf{a}_1=(a,\,c)^{\top}$ 和 $\mathbf{a}_2=(b,\,d)^{\top}$，四个数都为正，并且 $\mathbf{a}_2$ 位于 $\mathbf{a}_1$ 的左上方，如图 [40](#abb-40) 所示。顶点为 $\mathbf{0}$、$\mathbf{a}_1$、$\mathbf{a}_1+\mathbf{a}_2$、$\mathbf{a}_2$ 的平行四边形恰好放进边长为 $a+b$ 和 $c+d$ 的矩形中。要只留下平行四边形，就从矩形中切去两个直角边为 $a$ 和 $c$ 的三角形、两个直角边为 $b$ 和 $d$ 的三角形，以及两个边长为 $b$ 和 $c$ 的矩形：

$$(a+b)(c+d)-2\cdot\tfrac12ac-2\cdot\tfrac12bd-2\,bc=ac+ad+bc+bd-ac-bd-2bc=ad-bc .$$

对 $\mathbf{A}=\bigl(\begin{smallmatrix}3&1\\1&2\end{smallmatrix}\bigr)$：$4\cdot3-3-2-2=5$。
:::

:::definition 定义 14.1 ($2\times2$ 矩阵的行列式)
<span class="anker" id="satz-14-1"></span>

矩阵 $\mathbf{A}=\bigl(\begin{smallmatrix}a&b\\c&d\end{smallmatrix}\bigr)$ 的__行列式__是数

<span class="anker" id="gl-14-1"></span>
$$\det\mathbf{A}=ad-bc . \tag{14.1}$$
:::

它的绝对值是由各列张成的平行四边形的面积，也就是 $\mathbf{A}$ 使单位正方形面积变化的倍数。它与逆矩阵式 [(11.2)](einheitsmatrix-und-inverse.html#gl-11-2) 的分母中出现的是同一个数。

::::beispiel [算例]
$\det\bigl(\begin{smallmatrix}3&1\\1&2\end{smallmatrix}\bigr)=6-1=5$，$\det\bigl(\begin{smallmatrix}2&1\\1&1\end{smallmatrix}\bigr)=2-1=1$，$\det\operatorname{diag}(2,\,0.5)=1$，$\det\bigl(\begin{smallmatrix}1&2\\2&4\end{smallmatrix}\bigr)=0$。拉伸改变正方形的形状，但不改变它的面积：宽度增大的倍数，恰好由高度的缩小抵消。
::::

⁠**简而言之：**$2\times2$ 矩阵的行列式 $ad-bc$ 的绝对值，就是映射使单位正方形面积变化的倍数。

### 行列式的符号

<span class="anker" id="stufe-14-2"></span>

面积永远不为负，行列式却可以为负。它的符号携带了额外的信息：映射是否对平面作了镜像反射。

在单位正方形中，$\mathbf{e}_2$ 位于 $\mathbf{e}_1$ 的逆时针方向。如果对像也是如此，即 $\mathbf{a}_2$ 也位于 $\mathbf{a}_1$ 的逆时针方向，则 $\det\mathbf{A}>0$。如果 $\mathbf{a}_2$ 位于 $\mathbf{a}_1$ 的顺时针方向，平面就被镜像反射了，$\det\mathbf{A}<0$。这一性质称为__定向__：正的行列式保持定向，负的行列式使定向反转。

::::beispiel [算例]
关于 $x_1$ 轴的反射 $\operatorname{diag}(1,\,-1)$ 的行列式为 $-1$：面积不变，定向反转。交换矩阵的两列，行列式就改变符号：$\det\bigl(\begin{smallmatrix}1&3\\2&1\end{smallmatrix}\bigr)=1-6=-5$。旋转 $90^\circ$ 的 $\det=0\cdot0-(-1)\cdot1=1$，剪切的 $\det=1\cdot1-1\cdot0=1$，而压扁 $\operatorname{diag}(1,\,0)$ 的行列式为 $0$。
::::

⁠**简而言之：**行列式的绝对值是面积因子；它的符号说明映射是否作了镜像反射。

### 面积因子对每个图形都成立

<span class="anker" id="stufe-14-3"></span>

到目前为止，我们考察的是单位正方形。但线性映射对平面上的每个位置都一视同仁，所以它使每个图形的面积都按同一个倍数变化。

:::satz 定理 14.2 (面积因子)
<span class="anker" id="satz-14-2"></span>

若 $\mathbf{A}\in\mathbb{R}^{2\times2}$ 映射一个面积为 $F$ 的图形，则像的面积为 $|\det\mathbf{A}|\cdot F$。
:::

:::herleitung 面积因子
在图形上铺一张由边长为 $h$ 的小正方形组成的细网格。以 $\mathbf{q}$ 为一个顶点的小正方形，其顶点为 $\mathbf{q}$、$\mathbf{q}+h\mathbf{e}_1$、$\mathbf{q}+h\mathbf{e}_1+h\mathbf{e}_2$ 和 $\mathbf{q}+h\mathbf{e}_2$。它的像的顶点为 $\mathbf{A}\mathbf{q}$、$\mathbf{A}\mathbf{q}+h\mathbf{a}_1$、$\mathbf{A}\mathbf{q}+h\mathbf{a}_1+h\mathbf{a}_2$ 和 $\mathbf{A}\mathbf{q}+h\mathbf{a}_2$：这是由 $h\mathbf{a}_1$ 和 $h\mathbf{a}_2$ 构成、平移到 $\mathbf{A}\mathbf{q}$ 处的平行四边形。它的面积为 $h^2\,|\det\mathbf{A}|$，与小正方形在哪里无关。所以每个小正方形都按同一个倍数 $|\det\mathbf{A}|$ 变大或变小。图形近似地由这样的小正方形组成，网格越细，近似就越精确。因此这个倍数对整个图形都成立。
:::

::::beispiel [算例]
半径为 $1$ 的圆盘面积为 $\pi$。拉伸 $\operatorname{diag}(3,\,2)$ 把它变成半轴为 $3$ 和 $2$ 的椭圆。椭圆的面积为 $\pi\cdot3\cdot2=6\pi$，恰好是圆盘面积的 $|\det\mathbf{A}|=6$ 倍。顶点为 $\mathbf{0}$、$\mathbf{e}_1$、$\mathbf{e}_2$ 的三角形面积为 $\tfrac12$；在 $\bigl(\begin{smallmatrix}3&1\\1&2\end{smallmatrix}\bigr)$ 作用下，它变成顶点为 $\mathbf{0}$、$(3,1)^{\top}$、$(1,2)^{\top}$、面积为 $\tfrac52$ 的三角形。
::::

⁠**简而言之：**线性映射使每个图形的面积都按同一个倍数 $|\det\mathbf{A}|$ 变化，因为它对网格的每个小格都一视同仁。

### 更大矩阵的行列式

<span class="anker" id="stufe-14-4"></span>

在空间中，单位立方体变成由矩阵的三列张成的平行六面体，即一个歪斜的盒子。它的体积就是映射使体积变化的倍数。对更大的矩阵，也有这样一个数。计算它的方法，是把它归结为更小矩阵的行列式。

:::definition 定义 14.3 (行列式)
<span class="anker" id="satz-14-3"></span>

对 $\mathbf{A}\in\mathbb{R}^{1\times1}$，$\det\mathbf{A}=a_{11}$。对 $n\ge2$ 的 $\mathbf{A}\in\mathbb{R}^{n\times n}$，

<span class="anker" id="gl-14-2"></span>
$$\det\mathbf{A}=\sum_{j=1}^n(-1)^{1+j}\,a_{1j}\,\det\mathbf{A}_{1j} , \tag{14.2}$$

其中 $\mathbf{A}_{1j}$ 是从 $\mathbf{A}$ 中删去第一行和第 $j$ 列后得到的 $(n-1)\times(n-1)$ 矩阵。这一规则称为按第一行的__拉普拉斯展开__。
:::

当 $n=2$ 时，式 [(14.2)](#gl-14-2) 又给出 $a_{11}a_{22}-a_{12}a_{21}$。同样也可以按任何其他行或列展开，元素 $a_{ij}$ 取符号 $(-1)^{i+j}$；结果总是一样的。当 $n=3$ 时，$|\det\mathbf{A}|$ 是由三列构成的平行六面体的体积，而符号说明这三列与 $\mathbf{e}_1,\mathbf{e}_2,\mathbf{e}_3$ 的手性是否相同（右手定则），还是成镜像关系。

::::beispiel [算例]
对第 [12.3](lineare-gleichungssysteme.html#stufe-12-3) 小节中的系数矩阵

$$\mathbf{A}=\begin{pmatrix}1&2&1\\2&1&1\\1&1&2\end{pmatrix},$$

按第一行作拉普拉斯展开，得到 $\det\mathbf{A}=-4$（图 [41](#abb-41)）。

:::abbildung ml/k1rlaplace 41
按第一行的拉普拉斯展开：第一行的每个元素乘以去掉它所在的行和列后剩下的矩阵的行列式，符号正负交替。
:::
::::

对上三角矩阵（对角线以下全为零），反复按第一列展开，就得到对角元素的乘积，例如 $\det\Bigl(\begin{smallmatrix}2&1&3\\0&3&1\\0&0&4\end{smallmatrix}\Bigr)=2\cdot3\cdot4=24$。

⁠**简而言之：**$n\times n$ 矩阵的行列式通过拉普拉斯展开归结为更小的行列式；它的绝对值是映射使体积变化的倍数。

### 行列式的运算规则

<span class="anker" id="stufe-14-5"></span>

最重要的规则直接由几何图景得出。先后作用两个映射时，第一个按它的倍数改变体积，第二个再按它自己的倍数改变结果。这两个倍数相乘。

:::satz 定理 14.4 (行列式的运算规则)
<span class="anker" id="satz-14-4"></span>

对 $\mathbf{A},\mathbf{B}\in\mathbb{R}^{n\times n}$ 和数 $c$，有：

<ol class="rm">

<li>

$\det(\mathbf{A}\mathbf{B})=\det\mathbf{A}\cdot\det\mathbf{B}$；

</li>

<li>

$\det\mathbf{A}^{\top}=\det\mathbf{A}$；

</li>

<li>

若 $\mathbf{A}$ 可逆，则 $\det\mathbf{A}^{-1}=1/\det\mathbf{A}$；

</li>

<li>

$\det(c\,\mathbf{A})=c^n\det\mathbf{A}$；

</li>

<li>

把一行的倍数加到另一行上，行列式不变；交换两行，行列式改变符号；把一行乘以 $c$，行列式也乘以 $c$。

</li>

</ol>
:::

规则 (iii) 由 (i) 以及 $\mathbf{A}\mathbf{A}^{-1}=\mathbf{I}$ 和 $\det\mathbf{I}=1$ 得出。规则 (iv) 是说：把单位立方体的全部 $n$ 条棱都拉伸为原来的 $c$ 倍，它的体积就变为原来的 $c^n$ 倍。规则 (v) 使高斯消元法成为计算行列式的实用方法：把矩阵化为行阶梯形，记下交换的次数，再把对角元素相乘。

::::beispiel [算例 1]
由于 $\det\bigl(\begin{smallmatrix}2&1\\1&1\end{smallmatrix}\bigr)=1$ 且 $\det\bigl(\begin{smallmatrix}3&1\\1&2\end{smallmatrix}\bigr)=5$，乘积 $\bigl(\begin{smallmatrix}7&4\\4&3\end{smallmatrix}\bigr)$ 的行列式必定为 $5$：$21-16=5$。
::::

::::beispiel [算例 2]
在第 [12.3](lineare-gleichungssysteme.html#stufe-12-3) 小节的高斯消元中，系数矩阵通过加上倍数和一次交换，化成了对角元素为 $1$、$-1$、$-4$ 的阶梯形。所以它的行列式为 $(-1)\cdot\bigl(1\cdot(-1)\cdot(-4)\bigr)=-4$，与拉普拉斯展开的结果相同。
::::

⁠**简而言之：**乘积的行列式是各行列式的乘积，因为映射先后作用时体积因子相乘；实际中用高斯消元法计算行列式。

:::hintergrund 为什么初等行变换恰好这样改变行列式
由规则 (ii)，也可以对列而不是对行作变换，而各列张成平行四边形或平行六面体。把一列的倍数加到另一列上，比如 $\mathbf{a}_2\to\mathbf{a}_2+t\,\mathbf{a}_1$，与 $\mathbf{a}_1$ 相对的那条边就沿着平行于 $\mathbf{a}_1$ 的方向滑动。平行四边形像一叠被侧推的扑克牌那样被剪切。底和高都不变，面积也就不变。在空间中，平行六面体同样如此：每个平行于底面的截面都只是平移，而不改变；在每个高度上截面面积都相等的立体，体积也相等（祖暅原理，又称卡瓦列里原理）。交换两列，面积不变，但从第一列到第二列的旋转方向反过来了，符号也随之改变。把一列乘以 $c$，一条棱变为原来的 $c$ 倍长，体积也变为原来的 $c$ 倍。对 $2\times2$ 矩阵，公式 $ad-bc$ 直接证实了这一点，例如对剪切：$a\,(d+t\,c)-(b+t\,a)\,c=ad-bc$。

反过来，三条性质就已经完全确定了行列式：$\det\mathbf{I}=1$；交换两行改变符号；固定除一行以外的所有行时，行列式对这一行是线性的。具有这三条性质的每个关于矩阵的函数都是行列式。原因在于高斯消元法：它通过初等行变换把每个方阵化为 $\mathbf{I}$ 或一个含零行的矩阵，而每种变换的效果都由这三条性质确定。因此，许多教材用这些性质来定义行列式，并由此推导出拉普拉斯展开。
:::

:::hintergrund 为什么不用拉普拉斯展开计算行列式
$n\times n$ 矩阵的拉普拉斯展开要调用 $n$ 个 $n-1$ 阶行列式，其中每一个又要调用 $n-1$ 个 $n-2$ 阶行列式，依此类推。完全写开，这会产生 $n!$ 个乘积。当 $n=20$ 时，这超过 $2\cdot10^{18}$ 个，对计算机来说也太多了。与此相反，高斯消元法只需约 $\tfrac23n^3$ 次基本算术运算，对 $n=20$ 只有几千次。所以，拉普拉斯展开是一种定义，也是用于小矩阵和推导的工具，而不是计算方法。
:::

### 行列式与可逆性

<span class="anker" id="stufe-14-6"></span>

如果行列式为零，单位正方形就变成没有面积的图形，即一条线段或一个点。映射把平面压扁了，而被压扁的东西无法复原。

:::satz 定理 14.5 (行列式与可逆性)
<span class="anker" id="satz-14-5"></span>

方阵 $\mathbf{A}$ 可逆，当且仅当 $\det\mathbf{A}\ne0$。
:::

:::beweis 行列式与可逆性
若 $\mathbf{A}$ 可逆，则由规则 (i)，$\det\mathbf{A}\cdot\det\mathbf{A}^{-1}=\det\mathbf{I}=1$，所以 $\det\mathbf{A}\ne0$。反过来，若 $\det\mathbf{A}\ne0$，就用高斯消元法把 $\mathbf{A}$ 化为行阶梯形。由规则 (v)，行列式在此过程中至多乘上非零的因子，所以阶梯形的行列式也不为零。它等于阶梯形对角元素的乘积，所以这些元素没有一个为零，共有 $n$ 个主元。因此 $\operatorname{rank}\mathbf{A}=n$，再由第 [13.5](unabhangigkeit-basis-und-rang.html#stufe-13-5) 小节中的定理，$\mathbf{A}$ 可逆。
:::

因此，结合第 [13.5](unabhangigkeit-basis-und-rang.html#stufe-13-5) 小节中的定理，对方阵而言下列各条等价：$\det\mathbf{A}\ne0$，$\mathbf{A}$ 可逆，$\operatorname{rank}\mathbf{A}=n$，$\ker\mathbf{A}=\{\mathbf{0}\}$，各列线性无关。

::::beispiel [算例]
第 [13.4](unabhangigkeit-basis-und-rang.html#stufe-13-4) 小节中的矩阵 $\mathbf K$ 满足 $\det\mathbf K=1\cdot(2-1)-0+1\cdot(0-1)=0$，与 $\operatorname{rank}\mathbf K=2$ 一致。高斯消元法算例中的系数矩阵满足 $\det=-4\ne0$，因而可逆；正因为如此，那个方程组恰有一个解。
::::

⁠**简而言之：**方阵可逆，当且仅当它的行列式不为零，也就是说，它不把空间压扁。

:::hintergrund 行列式小并不意味着“几乎奇异”
你也许会认为，行列式很小的矩阵几乎是奇异的。事实并非如此。矩阵 $0.1\,\mathbf{I}_{10}$ 的行列式为 $0.1^{10}=10^{-10}$，但它完全可逆：它的逆矩阵是 $10\,\mathbf{I}_{10}$，它所做的只是把所有长度缩小到十分之一。这个极小的行列式只是因为因子 $0.1$ 对十个方向中的每一个都乘了一次。反过来，$\operatorname{diag}(1000,\,0.001)$ 的行列式为 $1$，尽管它在一个方向上几乎把平面压扁了。行列式度量的是体积，而体积取决于尺度。一个矩阵是否“几乎”破坏了信息，无法从它的行列式可靠地读出。
:::

:::aufgabe 练习 34 ★ 计算行列式
<span class="anker" id="aufg-34"></span>

<ol class="al">

<li>

计算 $\bigl(\begin{smallmatrix}2&4\\1&2\end{smallmatrix}\bigr)$ 和 $\Bigl(\begin{smallmatrix}1&2&0\\3&1&2\\0&1&1\end{smallmatrix}\Bigr)$ 的行列式。两个矩阵中哪个可逆？

</li>

<li>

顶点为 $(0,\,0)$、$(3,\,1)$ 和 $(1,\,2)$ 的三角形面积是多少？

</li>

<li>

由向量 $(1,\,0,\,0)^{\top}$、$(1,\,2,\,0)^{\top}$ 和 $(0,\,1,\,3)^{\top}$ 构成的平行六面体的体积是多少？

</li>

</ol>

:::loesung
(a) $\det\bigl(\begin{smallmatrix}2&4\\1&2\end{smallmatrix}\bigr)=4-4=0$：不可逆；第二列是第一列的两倍。对 $3\times3$ 矩阵，按第一行展开：

$$1\cdot\det\begin{pmatrix}1&2\\1&1\end{pmatrix}-2\cdot\det\begin{pmatrix}3&2\\0&1\end{pmatrix}+0=1\cdot(1-2)-2\cdot3=-7 .$$

它是可逆的。

(b) 这个三角形是由 $(3,1)^{\top}$ 和 $(1,2)^{\top}$ 构成的平行四边形的一半，该平行四边形的面积为 $|\det\bigl(\begin{smallmatrix}3&1\\1&2\end{smallmatrix}\bigr)|=5$；所以三角形的面积为 $2.5$。由面积因子也能得出同样的结果：顶点为 $\mathbf{0}$、$\mathbf{e}_1$、$\mathbf{e}_2$、面积为 $\tfrac12$ 的三角形被映射到这个三角形上。

(c) 以这些向量为列，得到 $\Bigl(\begin{smallmatrix}1&1&0\\0&2&1\\0&0&3\end{smallmatrix}\Bigr)$，这是一个上三角矩阵，行列式为 $1\cdot2\cdot3=6$。体积为 $6$。
:::
:::

:::aufgabe 练习 35 ★★ 验证运算规则
<span class="anker" id="aufg-35"></span>

<ol class="al">

<li>

对 $\mathbf{C}=\bigl(\begin{smallmatrix}1&2\\3&4\end{smallmatrix}\bigr)$ 和 $\mathbf{D}=\bigl(\begin{smallmatrix}0&1\\1&1\end{smallmatrix}\bigr)$ 验证 $\det(\mathbf{C}\mathbf{D})=\det\mathbf{C}\cdot\det\mathbf{D}$，并计算 $\det(3\,\mathbf{C})$。

</li>

<li>

证明每个旋转矩阵 $\mathbf R_\alpha$ 的行列式都为 $1$。这在几何上意味着什么？

</li>

<li>

不经计算，解释为什么有两列相同的矩阵的行列式为 $0$。

</li>

</ol>

:::loesung
(a) $\det\mathbf{C}=4-6=-2$，$\det\mathbf{D}=0-1=-1$，而 $\mathbf{C}\mathbf{D}=\bigl(\begin{smallmatrix}2&3\\4&7\end{smallmatrix}\bigr)$，其 $\det=14-12=2=(-2)\cdot(-1)$。此外，$3\mathbf{C}=\bigl(\begin{smallmatrix}3&6\\9&12\end{smallmatrix}\bigr)$，其 $\det=36-54=-18=3^2\cdot(-2)$，正如 $n=2$ 时的规则 (iv) 所说。

(b) $\det\mathbf R_\alpha=\cos\alpha\cdot\cos\alpha-(-\sin\alpha)\cdot\sin\alpha=\cos^2\alpha+\sin^2\alpha=1$。旋转不改变任何面积，也不作镜像反射。

(c) 两个相同的列线性相关。由各列张成的平行四边形或平行六面体是扁平的，面积或体积为零。由规则 (v) 也能得出同样的结论，只需借助 $\det\mathbf{A}^{\top}=\det\mathbf{A}$ 把它推广到列：交换两个相同的列，矩阵保持不变，而行列式却必须改变符号。所以 $\det\mathbf{A}=-\det\mathbf{A}$，从而 $\det\mathbf{A}=0$。
:::
:::
