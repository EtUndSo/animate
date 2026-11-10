---
title: 矩阵乘积
pfad: 计算机科学 / 机器学习 / 数学基础 / 向量与矩阵
adresse: informatik/machine-learning/mathematische-grundlagen/vektoren-und-matrizen
knoten: 第 1 章：向量与矩阵
nachschlagen: ja
order: 15211000
summary: 先后作用的两个线性映射又给出一个线性映射，从而给出一个矩阵。本节求出这个矩阵。结果就是矩阵乘积，它的定义由这一任务必然得出。
tags: 矩阵乘积, 外积
lang: zh
---

<span class="anker" id="stufe-9"></span>

:::zweck
先后作用的两个线性映射又给出一个线性映射，从而给出一个矩阵。本节求出这个矩阵。结果就是矩阵乘积，它的定义由这一任务必然得出。
:::

### 矩阵乘积

<span class="anker" id="stufe-9-1"></span>

先用矩阵 $\mathbf{B}\in\mathbb{R}^{n\times k}$ 映射向量 $\mathbf{x}\in\mathbb{R}^k$，再用矩阵 $\mathbf{A}\in\mathbb{R}^{m\times n}$ 映射结果 $\mathbf{B}\mathbf{x}\in\mathbb{R}^n$（图 [33](#abb-33)）。复合 $\mathbf{x}\mapsto\mathbf{A}(\mathbf{B}\mathbf{x})$ 是线性的，因为两级中的每一级都保持和与倍数。所以由第 [8.2](lineare-abbildungen.html#stufe-8-2) 小节中的定理，它有一个矩阵。这个矩阵的第 $l$ 列是 $\mathbf{e}_l$ 的像：第一级把这个单位向量变成 $\mathbf{B}$ 的列 $\mathbf{B}\mathbf{e}_l$，第二级再把这一列乘以 $\mathbf{A}$。

:::abbildung ml/k1hinter 33
上：先后作用的两个线性映射，先 $\mathbf{B}$，后 $\mathbf{A}$。下：同一个映射一步完成，用的是单个矩阵 $\mathbf{A}\mathbf{B}$。矩阵乘积正是为此而定义的：两条途径给出同样的结果。
:::

:::definition 定义 9.1 (矩阵乘积)
<span class="anker" id="satz-9-1"></span>

对 $\mathbf{A}\in\mathbb{R}^{m\times n}$ 和 $\mathbf{B}\in\mathbb{R}^{n\times k}$，__矩阵乘积__ $\mathbf{A}\mathbf{B}\in\mathbb{R}^{m\times k}$ 是元素如下的矩阵：

<span class="anker" id="gl-9-1"></span>
$$(\mathbf{A}\mathbf{B})_{il}=\sum_{j=1}^{n}a_{ij}\,b_{jl},\qquad i=1,\dots,m,\quad l=1,\dots,k . \tag{9.1}$$
:::

元素 $(i,l)$ 是 $\mathbf{A}$ 的第 $i$ 行与 $\mathbf{B}$ 的第 $l$ 列的点积。只有当 $\mathbf{A}$ 的列数与 $\mathbf{B}$ 的行数相同时，乘积才有定义：两个型中“内侧”的数必须一致，$(m\times n)\cdot(n\times k)$，结果的型则由“外侧”的数给出，为 $m\times k$。

:::satz 定理 9.2 (乘积就是复合)
<span class="anker" id="satz-9-2"></span>

对所有 $\mathbf{x}\in\mathbb{R}^k$，有 $(\mathbf{A}\mathbf{B})\,\mathbf{x}=\mathbf{A}\,(\mathbf{B}\mathbf{x})$。
:::

:::herleitung 复合
由式 [(7.1)](das-matrix-vektor-produkt.html#gl-7-1) 和式 [(9.1)](#gl-9-1)，左边的第 $i$ 个分量为

$$\sum_{l=1}^k(\mathbf{A}\mathbf{B})_{il}\,x_l=\sum_{l=1}^k\sum_{j=1}^na_{ij}\,b_{jl}\,x_l=\sum_{j=1}^na_{ij}\Bigl(\sum_{l=1}^kb_{jl}\,x_l\Bigr)=\sum_{j=1}^na_{ij}\,(\mathbf{B}\mathbf{x})_j ,$$

这就是 $\mathbf{A}(\mathbf{B}\mathbf{x})$ 的第 $i$ 个分量。中间一步交换了两个求和符号，并把 $a_{ij}$ 移到内层求和的前面。
:::

::::beispiel [算例]
对 $\mathbf{A}=\bigl(\begin{smallmatrix}1&2\\0&1\end{smallmatrix}\bigr)$ 和 $\mathbf{B}=\bigl(\begin{smallmatrix}0&1\\1&0\end{smallmatrix}\bigr)$，有

$$\mathbf{A}\mathbf{B}=\begin{pmatrix}2&1\\1&0\end{pmatrix}.$$

四个元素中的每一个都是按式 [(9.1)](#gl-9-1) 求出的和（图 [34](#abb-34)）。

:::abbildung ml/k1rprodukt 34
逐个元素计算矩阵乘积：元素 $(i,l)$ 是 $\mathbf{A}$ 的第 $i$ 行乘以 $\mathbf{B}$ 的第 $l$ 列。
:::

用 $\mathbf{x}=(1,\,2)^{\top}$ 验算：$\mathbf{B}\mathbf{x}=(2,\,1)^{\top}$，然后 $\mathbf{A}(\mathbf{B}\mathbf{x})=(4,\,1)^{\top}$；直接计算则是 $(\mathbf{A}\mathbf{B})\mathbf{x}=(2+2,\ 1+0)^{\top}=(4,\,1)^{\top}$。
::::

⁠**简而言之：**矩阵乘积 $\mathbf{A}\mathbf{B}$ 是映射“先 $\mathbf{B}$，后 $\mathbf{A}$”的矩阵；它的元素 $(i,l)$ 是 $\mathbf{A}$ 的第 $i$ 行乘以 $\mathbf{B}$ 的第 $l$ 列。

:::hintergrund 矩阵乘积为什么恰好这样定义
乍一看，式 [(9.1)](#gl-9-1) 显得很随意。逐个元素地把矩阵相乘似乎更自然。但矩阵乘积并不是随意的发明，而是由一个要求确定的：它应当是复合的矩阵。由第 [8.2](lineare-abbildungen.html#stufe-8-2) 小节中的定理，这个矩阵是唯一的，而它的第 $l$ 列必须是 $\mathbf{e}_l$ 在两个映射先后作用下的像，即 $\mathbf{A}$ 乘以 $\mathbf{B}$ 的第 $l$ 列。把它逐个分量写出来，恰好得到式 [(9.1)](#gl-9-1)。逐元素的乘积没有这样的意义：它不描述两个映射的复合。
:::

### 一次处理许多向量

<span class="anker" id="stufe-9-2"></span>

由乘积的推导，$\mathbf{A}\mathbf{B}$ 的第 $l$ 列是 $\mathbf{A}$ 与 $\mathbf{B}$ 的第 $l$ 列的乘积。所以可以把矩阵乘积读作并排放置的若干个矩阵-向量乘积：

<span class="anker" id="gl-9-2"></span>
$$\mathbf{A}\begin{pmatrix}\mathbf{B}\mathbf{e}_1&\cdots&\mathbf{B}\mathbf{e}_k\end{pmatrix}=\begin{pmatrix}\mathbf{A}\mathbf{B}\mathbf{e}_1&\cdots&\mathbf{A}\mathbf{B}\mathbf{e}_k\end{pmatrix}. \tag{9.2}$$

同样，$\mathbf{A}\mathbf{B}$ 的第 $i$ 行是 $\mathbf{A}$ 的第 $i$ 行乘以 $\mathbf{B}$。

对数据而言，这意味着：如果要把几个加权和用于所有样本，就把各个权重向量作为矩阵 $\mathbf{W}$ 的各列并排写出。于是乘积 $\mathbf{X}\mathbf{W}$ 的第 $l$ 列包含用第 $l$ 个权重向量得出的预测值。

::::beispiel [算例]
除了用 $\mathbf{w}=(3,\,10,\,-4)^{\top}$（千欧元）估算购买价格，还要用权重 $\mathbf{w}_{\mathrm M}=(12,\,30,\,-8)^{\top}$（欧元）估算月租金。取 $\mathbf{W}=\begin{pmatrix}\mathbf{w}&\mathbf{w}_{\mathrm M}\end{pmatrix}\in\mathbb{R}^{3\times2}$，得

$$\mathbf{X}\mathbf{W}=\begin{pmatrix}60&2&3\\40&1&1\\90&4&6\\70&3&2\end{pmatrix}\begin{pmatrix}3&12\\10&30\\-4&-8\end{pmatrix}=\begin{pmatrix}188&756\\126&502\\286&1152\\232&914\end{pmatrix}.$$

第 $i$ 行包含对公寓 $i$ 的两个估计值，第 $1$ 列是所有购买价格，第 $2$ 列是所有租金。
::::

⁠**简而言之：**$\mathbf{A}\mathbf{B}$ 的各列是 $\mathbf{A}$ 乘以 $\mathbf{B}$ 的各列；$\mathbf{X}\mathbf{W}$ 把几个加权和同时用于所有样本。

### 运算规则：顺序很重要

<span class="anker" id="stufe-9-3"></span>

对数而言，$2\cdot3=3\cdot2$。对矩阵而言，这并不成立，原因也很容易看出：先旋转再拉伸，与先拉伸再旋转是不同的（图 [35](#abb-35)）。

:::abbildung ml/k1reihenfolge 35
单位正方形以及 $\mathbf{e}_1$（红色）和 $\mathbf{e}_2$（绿色），旁边是它在 $\mathbf{S}\mathbf R$ 和 $\mathbf R\mathbf{S}$ 作用下的像。这里 $\mathbf R$ 是旋转 $90^\circ$，$\mathbf{S}=\operatorname{diag}(2,\,0.5)$ 是拉伸。顺序决定了矩形是在水平方向上变长还是在竖直方向上变长。
:::

:::satz 定理 9.3 (矩阵乘积的运算规则)
<span class="anker" id="satz-9-3"></span>

对型相容的矩阵和标量 $c$，有：

<ol class="rm">

<li>

$(\mathbf{A}\mathbf{B})\mathbf{C}=\mathbf{A}(\mathbf{B}\mathbf{C})$ （结合律）；

</li>

<li>

$\mathbf{A}(\mathbf{B}+\mathbf{C})=\mathbf{A}\mathbf{B}+\mathbf{A}\mathbf{C}$ 和 $(\mathbf{A}+\mathbf{B})\mathbf{C}=\mathbf{A}\mathbf{C}+\mathbf{B}\mathbf{C}$ （分配律）；

</li>

<li>

$c\,(\mathbf{A}\mathbf{B})=(c\,\mathbf{A})\mathbf{B}=\mathbf{A}(c\,\mathbf{B})$。

</li>

</ol>

但一般来说 $\mathbf{A}\mathbf{B}\ne\mathbf{B}\mathbf{A}$：矩阵乘积**不**满足交换律。
:::

规则 (i) 由意义得出：两边都是映射“先 $\mathbf{C}$，再 $\mathbf{B}$，后 $\mathbf{A}$”的矩阵，因为对每个 $\mathbf{x}$ 都有 $(\mathbf{A}\mathbf{B})(\mathbf{C}\mathbf{x})=\mathbf{A}(\mathbf{B}(\mathbf{C}\mathbf{x}))=\mathbf{A}((\mathbf{B}\mathbf{C})\mathbf{x})$。规则 (ii) 和 (iii) 可以用式 [(9.1)](#gl-9-1) 和求和规则逐个元素地验证。

::::beispiel [算例 1]
对旋转 $\mathbf R=\mathbf R_{90^\circ}=\bigl(\begin{smallmatrix}0&-1\\1&0\end{smallmatrix}\bigr)$ 和拉伸 $\mathbf{S}=\operatorname{diag}(2,\,0.5)$，

$$\mathbf{S}\mathbf R=\begin{pmatrix}0&-2\\0.5&0\end{pmatrix},\qquad \mathbf R\mathbf{S}=\begin{pmatrix}0&-0.5\\2&0\end{pmatrix}.$$

先旋转再拉伸，把 $\mathbf{e}_1$ 变成 $(0,\,0.5)^{\top}$；先拉伸再旋转，把它变成 $(0,\,2)^{\top}$。
::::

::::beispiel [算例 2]
由第 [9.1](#stufe-9-1) 小节，$\mathbf{A}\mathbf{B}=\bigl(\begin{smallmatrix}2&1\\1&0\end{smallmatrix}\bigr)$，但 $\mathbf{B}\mathbf{A}=\bigl(\begin{smallmatrix}0&1\\1&2\end{smallmatrix}\bigr)$。型不同时就更明显了：对 $\mathbf{A}\in\mathbb{R}^{2\times3}$ 和 $\mathbf{B}\in\mathbb{R}^{3\times2}$，$\mathbf{A}\mathbf{B}$ 是 $2\times2$ 矩阵，而 $\mathbf{B}\mathbf{A}$ 是 $3\times3$ 矩阵。
::::

⁠**简而言之：**在矩阵乘积中，可以重新加括号，也可以展开，但不能交换顺序。

:::hintergrund 括号的位置为什么能节省计算时间
由规则 (i)，$(\mathbf{A}\mathbf{B})\mathbf{x}=\mathbf{A}(\mathbf{B}\mathbf{x})$。结果相同，计算量却不同。对两个 $n\times n$ 矩阵，乘积 $\mathbf{A}\mathbf{B}$ 的 $n^2$ 个元素中，每个都需要 $n$ 次乘法和 $n-1$ 次加法，合计约 $2n^3$ 次基本算术运算；之后计算 $(\mathbf{A}\mathbf{B})\mathbf{x}$ 还要约 $2n^2$ 次。途径 $\mathbf{A}(\mathbf{B}\mathbf{x})$ 由两个矩阵-向量乘积组成，每个约 $2n^2$ 次。当 $n=1000$ 时，前者约需 $2\cdot10^9$ 次基本算术运算，后者约需 $4\cdot10^6$ 次，相差 $500$ 倍。所以，要把一长串矩阵作用于一个向量时，应当从右往左计算，而决不先求出乘积矩阵。
:::

### 两个线性级就是一个

<span class="anker" id="stufe-9-4"></span>

把几个线性计算级串联起来，并不会产生新种类的映射。由第 [9.1](#stufe-9-1) 小节，这一点已经很清楚，但它值得单独成为一条定理，因为它标示出了线性规则的界限。

:::satz 定理 9.4 (串联的线性映射)
<span class="anker" id="satz-9-4"></span>

若 $f(\mathbf{x})=\mathbf{B}\mathbf{x}$ 和 $g(\mathbf{u})=\mathbf{A}\mathbf{u}$ 是线性的，则复合 $\mathbf{x}\mapsto g(f(\mathbf{x}))$ 也是线性的，其矩阵就是单个矩阵 $\mathbf{A}\mathbf{B}$。由线性级组成的任何有限链也是如此。
:::

无论串联多少个线性级，结果总能用单个矩阵一步算出。所以，一串线性级能做的事，单个矩阵就已经能做到。在日常购物中就能小规模地见到这一点：先把价格从欧元换算成美元，再减去 $10$ % 的折扣，两步合起来就是一个单一的换算系数。

::::beispiel [算例]
第一级把三个数变成两个，$\mathbf{B}=\bigl(\begin{smallmatrix}1&2&0\\0&1&-1\end{smallmatrix}\bigr)$，第二级再把两个数变回三个，$\mathbf{A}=\Bigl(\begin{smallmatrix}2&1\\1&-1\\0&3\end{smallmatrix}\Bigr)$。合起来就是单个矩阵

$$\mathbf{A}\mathbf{B}=\begin{pmatrix}2&5&-1\\1&1&1\\0&3&-3\end{pmatrix}.$$

用 $\mathbf{x}=(1,\,1,\,1)^{\top}$ 验算：$\mathbf{B}\mathbf{x}=(3,\,0)^{\top}$，而 $\mathbf{A}(3,\,0)^{\top}=(6,\,3,\,0)^{\top}$；同样，$(\mathbf{A}\mathbf{B})\mathbf{x}=(2+5-1,\ 1+1+1,\ 0+3-3)^{\top}=(6,\,3,\,0)^{\top}$。
::::

⁠**简而言之：**串联的线性级合起来构成单个线性映射；它的矩阵是各个矩阵的乘积。

### 外积

<span class="anker" id="stufe-9-5"></span>

点积 $\mathbf{u}^{\top}\mathbf{v}$ 是“行乘列”，结果是一个数。如果把顺序反过来，变成“列乘行”，那么由式 [(9.1)](#gl-9-1) 得到的是整个矩阵：第一个向量的一个分量与第二个向量的一个分量的所有乘积构成的表格，就像一张乘法表。

:::definition 定义 9.5 (外积)
<span class="anker" id="satz-9-5"></span>

对 $\mathbf{u}\in\mathbb{R}^m$ 和 $\mathbf{v}\in\mathbb{R}^n$，__外积__ $\mathbf{u}\mathbf{v}^{\top}\in\mathbb{R}^{m\times n}$ 是元素如下的矩阵：

<span class="anker" id="gl-9-3"></span>
$$(\mathbf{u}\mathbf{v}^{\top})_{ij}=u_i\,v_j . \tag{9.3}$$
:::

它是一个 $m\times1$ 矩阵与一个 $1\times n$ 矩阵的矩阵乘积。每一列都是 $\mathbf{u}$ 的倍数，即 $v_j\,\mathbf{u}$；每一行都是 $\mathbf{v}^{\top}$ 的倍数。

::::beispiel [算例]
$$\begin{pmatrix}1\\2\\3\end{pmatrix}\begin{pmatrix}4&5\end{pmatrix}=\begin{pmatrix}4&5\\8&10\\12&15\end{pmatrix}.$$
::::

借助外积，每个矩阵乘积都可以写成一个和：“$\mathbf{A}$ 的第 $j$ 列乘以 $\mathbf{B}$ 的第 $j$ 行”，对 $j$ 求和，

<span class="anker" id="gl-9-4"></span>
$$\mathbf{A}\mathbf{B}=\sum_{j=1}^n\mathbf{a}_j\,\bigl(\mathbf{B}\ \text{的第 $j$ 行}\bigr) . \tag{9.4}$$

右边的元素 $(i,l)$ 是 $\sum_ja_{ij}\,b_{jl}$，与式 [(9.1)](#gl-9-1) 完全相同。对第 [9.1](#stufe-9-1) 小节中的 $\mathbf{A}=\bigl(\begin{smallmatrix}1&2\\0&1\end{smallmatrix}\bigr)$ 和 $\mathbf{B}=\bigl(\begin{smallmatrix}0&1\\1&0\end{smallmatrix}\bigr)$，两个外积之和又给出 $\mathbf{A}\mathbf{B}$（图 [36](#abb-36)）。

:::abbildung ml/k1raeusser 36
把矩阵乘积写成外积之和：$\mathbf{A}$ 的第 $j$ 列乘以 $\mathbf{B}$ 的第 $j$ 行，对 $j=1,2$ 求和。
:::

⁠**简而言之：**外积 $\mathbf{u}\mathbf{v}^{\top}$ 是所有乘积 $u_iv_j$ 构成的表格；每个矩阵乘积都是这类表格之和。

:::aufgabe 练习 21 ★ 乘积与型
<span class="anker" id="aufg-21"></span>

<ol class="al">

<li>

对 $\mathbf{C}=\bigl(\begin{smallmatrix}1&2\\3&4\end{smallmatrix}\bigr)$ 和 $\mathbf{D}=\bigl(\begin{smallmatrix}0&1\\1&1\end{smallmatrix}\bigr)$，计算 $\mathbf{C}\mathbf{D}$ 和 $\mathbf{D}\mathbf{C}$。

</li>

<li>

设 $\mathbf{A}\in\mathbb{R}^{2\times3}$，$\mathbf{B}\in\mathbb{R}^{3\times4}$，$\mathbf{x}\in\mathbb{R}^4$。表达式 $\mathbf{A}\mathbf{B}$、$\mathbf{B}\mathbf{A}$、$\mathbf{A}\mathbf{B}\mathbf{x}$、$\mathbf{B}\mathbf{x}\mathbf{A}$ 中哪些有定义？结果分别是什么型的？

</li>

<li>

计算外积 $(1,\,-1)^{\top}(2,\,0,\,3)$，并验证每一行都是 $(2,\,0,\,3)$ 的倍数。

</li>

</ol>

:::loesung
(a) $\mathbf{C}\mathbf{D}=\bigl(\begin{smallmatrix}1\cdot0+2\cdot1&1\cdot1+2\cdot1\\3\cdot0+4\cdot1&3\cdot1+4\cdot1\end{smallmatrix}\bigr)=\bigl(\begin{smallmatrix}2&3\\4&7\end{smallmatrix}\bigr)$，$\mathbf{D}\mathbf{C}=\bigl(\begin{smallmatrix}0+3&0+4\\1+3&2+4\end{smallmatrix}\bigr)=\bigl(\begin{smallmatrix}3&4\\4&6\end{smallmatrix}\bigr)$。两者不同。

(b) $\mathbf{A}\mathbf{B}$：$(2\times3)\cdot(3\times4)$ 型相容，结果的型为 $2\times4$。$\mathbf{B}\mathbf{A}$：$(3\times4)\cdot(2\times3)$，内侧的数 $4\ne2$，没有定义。$\mathbf{A}\mathbf{B}\mathbf{x}$：$(2\times4)\cdot(4\times1)$ 型相容，结果是 $\mathbb{R}^2$ 中的一个向量。$\mathbf{B}\mathbf{x}\mathbf{A}$：$\mathbf{B}\mathbf{x}$ 的型为 $3\times1$，而 $(3\times1)\cdot(2\times3)$ 型不相容，内侧的数 $1\ne2$；没有定义。

(c) $(1,\,-1)^{\top}(2,\,0,\,3)=\bigl(\begin{smallmatrix}2&0&3\\-2&0&-3\end{smallmatrix}\bigr)$。第一行是 $1\cdot(2,0,3)$，第二行是 $-1\cdot(2,0,3)$。
:::
:::

:::aufgabe 练习 22 ★★ 两次旋转
<span class="anker" id="aufg-22"></span>

<ol class="al">

<li>

用式 [(8.3)](lineare-abbildungen.html#gl-8-3) 计算 $\mathbf R_\alpha\mathbf R_\beta$。这是哪个旋转？顺便得到了三角学中的哪两个公式？

</li>

<li>

计算 $\mathbf R_{90^\circ}^2=\mathbf R_{90^\circ}\mathbf R_{90^\circ}$ 和 $\mathbf R_{90^\circ}^4$，并从几何上解释结果。

</li>

<li>

$\mathbf R_\alpha\mathbf R_\beta=\mathbf R_\beta\mathbf R_\alpha$ 成立吗？为什么这与矩阵不可交换的规则并不矛盾？

</li>

</ol>

:::loesung
(a) 乘开得

$$\mathbf R_\alpha\mathbf R_\beta=\begin{pmatrix}\cos\alpha\cos\beta-\sin\alpha\sin\beta&-(\cos\alpha\sin\beta+\sin\alpha\cos\beta)\\\sin\alpha\cos\beta+\cos\alpha\sin\beta&\cos\alpha\cos\beta-\sin\alpha\sin\beta\end{pmatrix}.$$

从几何上看，这是“先旋转 $\beta$，再旋转 $\alpha$”，也就是旋转 $\alpha+\beta$；由式 [(8.3)](lineare-abbildungen.html#gl-8-3)，这个旋转的矩阵是 $\mathbf R_{\alpha+\beta}$。比较各元素，就得到和角公式 $\cos(\alpha+\beta)=\cos\alpha\cos\beta-\sin\alpha\sin\beta$ 和 $\sin(\alpha+\beta)=\sin\alpha\cos\beta+\cos\alpha\sin\beta$。矩阵乘积直接给出这两个公式，你不必把它们背下来。

(b) $\mathbf R_{90^\circ}^2=\bigl(\begin{smallmatrix}0&-1\\1&0\end{smallmatrix}\bigr)\bigl(\begin{smallmatrix}0&-1\\1&0\end{smallmatrix}\bigr)=\bigl(\begin{smallmatrix}-1&0\\0&-1\end{smallmatrix}\bigr)=-\mathbf{I}$：两次旋转 $90^\circ$ 就是旋转半圈，每个点都变为它关于原点的对称点。$\mathbf R_{90^\circ}^4=(-\mathbf{I})(-\mathbf{I})=\mathbf{I}$：旋转四次四分之一圈就是旋转一整圈。

(c) 成立：两个乘积都是 $\mathbf R_{\alpha+\beta}=\mathbf R_{\beta+\alpha}$，因为平面上绕同一点的旋转可以按任意顺序进行。“不可交换”只意味着 $\mathbf{A}\mathbf{B}=\mathbf{B}\mathbf{A}$ **并非总是**成立。对某些特定的矩阵对，例如平面上的两个旋转或两个对角矩阵，它仍然可以成立。
:::
:::

:::aufgabe 练习 23 ★★ 正确的括号
<span class="anker" id="aufg-23"></span>

设 $\mathbf{A}\in\mathbb{R}^{100\times1000}$，$\mathbf{B}\in\mathbb{R}^{1000\times1000}$，$\mathbf{x}\in\mathbb{R}^{1000}$。估计 $(\mathbf{A}\mathbf{B})\mathbf{x}$ 和 $\mathbf{A}(\mathbf{B}\mathbf{x})$ 各需多少次基本算术运算。$m\times n$ 矩阵与 $n\times k$ 矩阵的乘积按约 $2mnk$ 次计。

:::loesung
$(\mathbf{A}\mathbf{B})\mathbf{x}$：$100\times1000$ 矩阵与 $1000\times1000$ 矩阵的乘积 $\mathbf{A}\mathbf{B}$ 约需 $2\cdot100\cdot1000\cdot1000=2\cdot10^8$ 次运算，之后 $(\mathbf{A}\mathbf{B})\mathbf{x}$ 还需约 $2\cdot100\cdot1000=2\cdot10^5$ 次；合计约 $2.002$ 亿次。$\mathbf{A}(\mathbf{B}\mathbf{x})$：$\mathbf{B}\mathbf{x}$ 约需 $2\cdot1000\cdot1000=2\cdot10^6$ 次，之后 $\mathbf{A}(\mathbf{B}\mathbf{x})$ 约需 $2\cdot10^5$ 次；合计约 $220$ 万次。第二种途径约快 $91$ 倍，结果相同。
:::
:::
