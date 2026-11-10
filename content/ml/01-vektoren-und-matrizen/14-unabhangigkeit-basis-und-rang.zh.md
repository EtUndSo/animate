---
title: 线性无关、基与秩
pfad: 计算机科学 / 机器学习 / 数学基础 / 向量与矩阵
adresse: informatik/machine-learning/mathematische-grundlagen/vektoren-und-matrizen
knoten: 第 1 章：向量与矩阵
nachschlagen: ja
order: 15211400
summary: 列表中有些向量并不带来新东西，因为它们可以由其他向量组合而成。本节度量一个矩阵包含多少个真正不同的方向，并说明如果特征把同样的信息记录了两次，这对数据意味着什么。
tags: 张成的空间, 线性无关, 线性相关, 基, 维数, 标准基, 秩, 满秩
lang: zh
---

<span class="anker" id="stufe-13"></span>

:::zweck
列表中有些向量并不带来新东西，因为它们可以由其他向量组合而成。本节度量一个矩阵包含多少个真正不同的方向，并说明如果特征把同样的信息记录了两次，这对数据意味着什么。
:::

### 张成的空间

<span class="anker" id="stufe-13-1"></span>

矩阵的列空间是其各列的所有线性组合构成的集合。对每个向量列表，同样的构造都给出一个集合，这个集合有它自己的名称（图 [39](#abb-39)）。

:::abbildung ml/k1spann 39
平面上三个向量列表张成的空间（蓝色），按 $1:2$ 的比例绘制。(a) 一个向量张成一条过原点的直线。(b) 同一直线上的第二个向量不改变任何东西。(c) 方向不同的两个向量张成整个平面。
:::

:::definition 定义 13.1 (张成的空间)
<span class="anker" id="satz-13-1"></span>

向量 $\mathbf{v}_1,\dots,\mathbf{v}_k\in\mathbb{R}^d$ __张成的空间__（span）是它们的所有线性组合构成的集合：

<span class="anker" id="gl-13-1"></span>
$$\operatorname{span}\{\mathbf{v}_1,\dots,\mathbf{v}_k\}=\Bigl\{\sum_{l=1}^kc_l\,\mathbf{v}_l\ :\ c_1,\dots,c_k\in\mathbb{R}\Bigr\}. \tag{13.1}$$
:::

所以，矩阵的列空间就是它的各列张成的空间。张成的空间中任意两个向量的每个线性组合也都在其中；相加和取倍数永远不会把你带出这个集合。

::::beispiel [算例]
$\operatorname{span}\{(1,\,2)^{\top}\}$ 是所有倍数 $c\,(1,\,2)^{\top}$ 构成的直线。$(1,\,2)^{\top}$ 和 $(2,\,4)^{\top}$ 张成的空间是同一条直线，因为 $(2,\,4)^{\top}=2\,(1,\,2)^{\top}$。$(1,\,0)^{\top}$ 和 $(1,\,1)^{\top}$ 张成的空间是整个平面：每个向量 $(y_1,\,y_2)^{\top}$ 都等于 $(y_1-y_2)\,(1,\,0)^{\top}+y_2\,(1,\,1)^{\top}$。在 $\mathbb{R}^3$ 中，$\operatorname{span}\{\mathbf{e}_1,\mathbf{e}_2\}$ 是所有满足 $x_3=0$ 的向量构成的平面。
::::

⁠**简而言之：**一个向量列表张成的空间，就是能由这些向量线性组合而成的一切。

### 线性无关

<span class="anker" id="stufe-13-2"></span>

在图 [39](#abb-39) (b) 中，第二个向量不带来任何新东西：它已经位于第一个向量张成的空间中。数据集也可能有同样的弱点。如果数据集包含卧室数、起居室数和房间总数，第三列就是前两列之和，不携带任何独立的信息。需要一个词来表示这样的性质：向量列表中没有多余的东西。

:::definition 定义 13.2 (线性无关)
<span class="anker" id="satz-13-2"></span>

如果

<span class="anker" id="gl-13-2"></span>
$$c_1\mathbf{v}_1+c_2\mathbf{v}_2+\dots+c_k\mathbf{v}_k=\mathbf{0} \tag{13.2}$$

只在 $c_1=c_2=\dots=c_k=0$ 时成立，就称向量 $\mathbf{v}_1,\dots,\mathbf{v}_k$ __线性无关__。否则称它们__线性相关__。
:::

等价地说，线性相关意味着：至少有一个向量是其他向量的线性组合。事实上，如果式 [(13.2)](#gl-13-2) 在某个系数 $c_l\ne0$ 时成立，就可以解出 $\mathbf{v}_l$：$\mathbf{v}_l=-\sum_{l'\ne l}(c_{l'}/c_l)\,\mathbf{v}_{l'}$。反过来，这样的表示立刻给出一个在 $\mathbf{v}_l$ 前面系数为 $-1$ 的组合。

::::beispiel [算例]
$(1,\,2)^{\top}$ 和 $(2,\,4)^{\top}$ 线性相关：$2\,(1,\,2)^{\top}-(2,\,4)^{\top}=\mathbf{0}$。向量 $(1,\,0)^{\top}$ 和 $(1,\,1)^{\top}$ 线性无关：由 $c_1(1,\,0)^{\top}+c_2(1,\,1)^{\top}=(c_1+c_2,\ c_2)^{\top}=\mathbf{0}$，先得 $c_2=0$，再得 $c_1=0$。三个向量 $(1,\,0,\,1)^{\top}$、$(0,\,1,\,1)^{\top}$ 和 $(1,\,1,\,2)^{\top}$ 线性相关，因为第三个是前两个之和。
::::

⁠**简而言之：**线性无关意味着：没有一个向量能由其他向量组合而成；不存在冗余。

### 基与维数

<span class="anker" id="stufe-13-3"></span>

要尽可能简洁地描述一个张成的空间，就取尽可能少、但又足以到达其中一切的向量。这样的列表就像一个坐标系：张成的空间中的每个向量都恰有一种用它表示的方式。

:::definition 定义 13.3 (基、维数)
<span class="anker" id="satz-13-3"></span>

由线性无关的向量组成、并且张成集合 $\mathcal S$ 的列表，称为 $\mathcal S$ 的一个__基__。基中向量的个数称为 $\mathcal S$ 的__维数__，记作 $\dim\mathcal S$。
:::

集合 $\mathcal S$ 有许多不同的基，但它们都由同样多个向量组成；这是线性代数中的一条定理，维数的定义就建立在它之上。单位向量 $\mathbf{e}_1,\dots,\mathbf{e}_d$ 构成 $\mathbb{R}^d$ 的一个基，即__标准基__；这就是 $\dim\mathbb{R}^d=d$ 的原因。

:::satz 定理 13.4 (坐标唯一)
<span class="anker" id="satz-13-4"></span>

若 $\mathbf{v}_1,\dots,\mathbf{v}_k$ 是 $\mathcal S$ 的一个基，则每个向量 $\mathbf{x}\in\mathcal S$ 都恰有一种表示 $\mathbf{x}=\sum_lc_l\mathbf{v}_l$。
:::

:::beweis 坐标唯一
至少有一种表示，因为基张成 $\mathcal S$。如果有两种，$\sum_lc_l\mathbf{v}_l=\sum_lc_l'\mathbf{v}_l$，它们的差就是 $\sum_l(c_l-c_l')\mathbf{v}_l=\mathbf{0}$。由线性无关，所有 $c_l-c_l'=0$。
:::

::::beispiel [算例]
$(1,\,0)^{\top}$ 和 $(1,\,1)^{\top}$ 构成 $\mathbb{R}^2$ 的一个基：它们线性无关，并且张成整个平面。在这个基下，向量 $(3,\,2)^{\top}$ 的坐标是 $1$ 和 $2$，因为 $(3,\,2)^{\top}=1\cdot(1,\,0)^{\top}+2\cdot(1,\,1)^{\top}$。直线 $\operatorname{span}\{(0,\,1)^{\top}\}$ 的维数是 $1$，尽管它的向量有两个分量。
::::

⁠**简而言之：**基是张成一切的、由线性无关向量组成的列表；它的长度就是维数。

### 矩阵的秩

<span class="anker" id="stufe-13-4"></span>

一个有 $n$ 列的矩阵所包含的真正不同的方向，可能少于 $n$ 个。去掉一切多余的东西之后剩下的方向个数，说明了一个矩阵实际能做多少事。

:::definition 定义 13.5 (秩)
<span class="anker" id="satz-13-5"></span>

矩阵 $\mathbf{A}$ 的__秩__ $\operatorname{rank}\mathbf{A}$ 是 $\mathbf{A}$ 中线性无关的列的最大个数。它等于这个矩阵的列空间的维数。
:::

:::satz 定理 13.6 (列秩等于行秩)
<span class="anker" id="satz-13-6"></span>

矩阵中线性无关的列的最大个数，等于线性无关的行的最大个数。特别地，对 $\mathbf{A}\in\mathbb{R}^{m\times n}$，有 $\operatorname{rank}\mathbf{A}=\operatorname{rank}\mathbf{A}^{\top}\le\min(m,n)$。
:::

若 $\operatorname{rank}\mathbf{A}=\min(m,n)$，则称 $\mathbf{A}$ __满秩__。实际中，用高斯消元法确定秩：初等行变换不改变秩，而在行阶梯形中，秩就是不全为零的行的个数。

::::beispiel [算例]
$\bigl(\begin{smallmatrix}1&2\\2&4\end{smallmatrix}\bigr)$ 的秩为 $1$：第二列是第一列的两倍，同样，第二行也是第一行的两倍。对

$$\mathbf K=\begin{pmatrix}1&0&1\\0&1&1\\1&1&2\end{pmatrix}$$

从第三行减去第一行和第二行，得到各行 $(1,0,1)$、$(0,1,1)$、$(0,0,0)$。有两行非零，所以 $\operatorname{rank}\mathbf K=2$；确实，第三列是前两列之和。公寓数据集的数据矩阵满秩，秩为 $3$。
::::

⁠**简而言之：**秩计算一个矩阵的各列包含多少个真正不同的方向，而它的各行所含的方向恰好一样多。

:::hintergrund 为什么线性无关的行与列一样多
这并非显而易见：一个 $3\times5$ 矩阵的行和列位于完全不同的空间中。一个简短的论证如下。设 $\mathbf{A}$ 有 $r$ 列线性无关，并且其余每一列都是它们的线性组合。这 $r$ 列构成矩阵 $\mathbf G\in\mathbb{R}^{m\times r}$。于是 $\mathbf{A}$ 的每一列 $\mathbf{a}_j$ 都等于 $\mathbf G$ 乘以一个有 $r$ 个分量的系数向量。把这些系数向量写成矩阵 $\mathbf F\in\mathbb{R}^{r\times n}$ 的各列，由式 [(9.2)](das-matrixprodukt.html#gl-9-2)，就有 $\mathbf{A}=\mathbf G\mathbf F$。现在逐行读同一个乘积：$\mathbf{A}$ 的第 $i$ 行是 $\mathbf G$ 的第 $i$ 行乘以 $\mathbf F$，即 $\mathbf F$ 的 $r$ 行的线性组合。所以 $\mathbf{A}$ 的所有行都位于 $\mathbf F$ 的 $r$ 行张成的空间中，这个集合的维数至多为 $r$，因此这些行中至多有 $r$ 行线性无关。所以，行所含的线性无关方向至多与列一样多。对 $\mathbf{A}^{\top}$ 应用同样的论证（它的列就是 $\mathbf{A}$ 的行），就得到相反的不等式。所以两个数相等。
:::

### 零空间与秩-零化度定理

<span class="anker" id="stufe-13-5"></span>

一个有 $n$ 列的矩阵接受来自 $n$ 个方向的向量。其中有些方向到达结果中；其余的被映射为零向量而丢失。丢失的方向构成一个单独的集合。

:::definition 定义 13.7 (零空间)
<span class="anker" id="satz-13-7"></span>

矩阵 $\mathbf{A}\in\mathbb{R}^{m\times n}$ 的__零空间__是被 $\mathbf{A}$ 映射为零向量的所有向量构成的集合：

<span class="anker" id="gl-13-3"></span>
$$\ker\mathbf{A}=\{\mathbf{x}\in\mathbb{R}^n:\ \mathbf{A}\mathbf{x}=\mathbf{0}\} . \tag{13.3}$$
:::

零空间是第 [12.4](lineare-gleichungssysteme.html#stufe-12-4) 小节中齐次方程组的解集。它总包含零向量，并且包含它的任意两个向量的每个线性组合；所以谈论它的维数是有意义的。

:::satz 定理 13.8 (秩-零化度定理)
<span class="anker" id="satz-13-8"></span>

对每个矩阵 $\mathbf{A}\in\mathbb{R}^{m\times n}$，有

<span class="anker" id="gl-13-4"></span>
$$\dim\ker\mathbf{A}+\operatorname{rank}\mathbf{A}=n . \tag{13.4}$$
:::

输入的 $n$ 个方向被分成两部分：没有到达结果的，都落入零空间。用高斯消元法可以这样看出来：在行阶梯形中有 $\operatorname{rank}\mathbf{A}$ 个主元。其余 $n-\operatorname{rank}\mathbf{A}$ 个未知数没有自己的主元，在齐次方程组中可以自由选取。它们中的每一个都贡献零空间的一个方向。

:::satz 定理 13.9 (方阵何时可逆)
<span class="anker" id="satz-13-9"></span>

对 $\mathbf{A}\in\mathbb{R}^{n\times n}$，下列各条等价：(i) $\mathbf{A}$ 可逆；(ii) $\ker\mathbf{A}=\{\mathbf{0}\}$；(iii) $\operatorname{rank}\mathbf{A}=n$；(iv) $\mathbf{A}$ 的各列线性无关。
:::

:::beweis 可逆性
由第 [11.5](einheitsmatrix-und-inverse.html#stufe-11-5) 小节，(i) 推出 (ii)。由秩-零化度定理和秩的定义，(ii)、(iii) 和 (iv) 等价。还需证明 (iii) 和 (ii) 推出 (i)。若 $\operatorname{rank}\mathbf{A}=n$，列空间就是 $\mathbb{R}^n$ 中一个维数为 $n$ 的空间，因而就是整个 $\mathbb{R}^n$。所以每个方程组 $\mathbf{A}\mathbf{c}_j=\mathbf{e}_j$ 都可解，这些解构成一个矩阵 $\mathbf{C}$ 的各列，满足 $\mathbf{A}\mathbf{C}=\mathbf{I}$。此外，$\mathbf{A}(\mathbf{C}\mathbf{A}-\mathbf{I})=\mathbf{A}\mathbf{C}\mathbf{A}-\mathbf{A}=\mathbf 0$。所以 $\mathbf{C}\mathbf{A}-\mathbf{I}$ 的每一列都位于零空间中，而由 (ii)，零空间只含零向量。因此也有 $\mathbf{C}\mathbf{A}=\mathbf{I}$，并且 $\mathbf{C}=\mathbf{A}^{-1}$。
:::

::::beispiel [算例]
$\bigl(\begin{smallmatrix}1&2\\2&4\end{smallmatrix}\bigr)$ 的零空间为 $\operatorname{span}\{(2,\,-1)^{\top}\}$，维数为 $1$，秩为 $1$：$1+1=2$。上面的矩阵 $\mathbf K$ 的零空间为 $\operatorname{span}\{(1,\,1,\,-1)^{\top}\}$，因为它的第三列是前两列之和；由 $\operatorname{rank}\mathbf K=2$ 得 $1+2=3$。
::::

**秩与可解性。** 有了秩和零空间，第 [12](lineare-gleichungssysteme.html#stufe-12) 节中的问题就可以用数来回答，即使矩阵不是方阵。有没有解？解唯一吗？对每个右端项都有解吗？

:::satz 定理 13.10 (可解性与秩)
<span class="anker" id="satz-13-10"></span>

对 $\mathbf{A}\in\mathbb{R}^{m\times n}$ 和 $\mathbf{y}\in\mathbb{R}^m$：

<ol class="rm">

<li>

$\mathbf{A}\mathbf{x}=\mathbf{y}$ 可解，当且仅当 $\operatorname{rank}(\mathbf{A}\,|\,\mathbf{y})=\operatorname{rank}\mathbf{A}$；

</li>

<li>

若方程组可解，则解唯一，当且仅当 $\operatorname{rank}\mathbf{A}=n$；

</li>

<li>

$\mathbf{A}\mathbf{x}=\mathbf{y}$ 对每个 $\mathbf{y}\in\mathbb{R}^m$ 都可解，当且仅当 $\operatorname{rank}\mathbf{A}=m$。

</li>

</ol>
:::

:::beweis 可解性与秩
(i) 由第 [12.2](lineare-gleichungssysteme.html#stufe-12-2) 小节，方程组可解，当且仅当 $\mathbf{y}$ 位于 $\mathbf{A}$ 的列空间中。若 $\mathbf{y}$ 在其中，附加的这一列不带来新方向：$(\mathbf{A}\,|\,\mathbf{y})$ 的各列与 $\mathbf{A}$ 的各列张成同一个空间，两个秩都等于它的维数。若 $\mathbf{y}$ 不在其中，就取 $\mathbf{A}$ 的 $r=\operatorname{rank}\mathbf{A}$ 个线性无关的列 $\mathbf g_1,\dots,\mathbf g_r$，再添上 $\mathbf{y}$。由 $c_1\mathbf g_1+\dots+c_r\mathbf g_r+c\,\mathbf{y}=\mathbf{0}$ 可得 $c=0$，否则 $\mathbf{y}$ 就是各 $\mathbf g_l$ 的线性组合，从而位于列空间中；于是所有 $c_l=0$。所以 $(\mathbf{A}\,|\,\mathbf{y})$ 至少有 $r+1$ 个线性无关的列，$\operatorname{rank}(\mathbf{A}\,|\,\mathbf{y})>\operatorname{rank}\mathbf{A}$。

(ii) 由第 [12.4](lineare-gleichungssysteme.html#stufe-12-4) 小节，全部解等于一个解加上零空间中的向量。所以解唯一，当且仅当 $\ker\mathbf{A}=\{\mathbf{0}\}$，而由秩-零化度定理，这意味着 $\operatorname{rank}\mathbf{A}=n$。

(iii) 每个 $\mathbf{y}$ 都位于列空间中，当且仅当列空间是整个 $\mathbb{R}^m$。而这种情况恰好在列空间的维数为 $m$，即 $\operatorname{rank}\mathbf{A}=m$ 时出现。
:::

对 $\operatorname{rank}\mathbf{A}=n=m$ 的方阵，(ii) 和 (iii) 合在一起：对每个右端项都恰有一个解，这与关于可逆性的定理一致。

::::beispiel [算例]
对 $\mathbf{A}=\bigl(\begin{smallmatrix}1&2\\2&4\end{smallmatrix}\bigr)$，$\operatorname{rank}\mathbf{A}=1$。取 $\mathbf{y}=(1,\,1)^{\top}$，增广矩阵的各行为 $(1,\,2\,|\,1)$ 和 $(2,\,4\,|\,1)$；从第二行减去第一行的两倍，剩下 $(0,\,0\,|\,-1)$，它不是零行。所以 $\operatorname{rank}(\mathbf{A}\,|\,\mathbf{y})=2\ne1$，方程组不可解，与第 [12.2](lineare-gleichungssysteme.html#stufe-12-2) 小节中一样。与此相反，取 $\mathbf{y}=(3,\,6)^{\top}$ 时，剩下 $(0,\,0\,|\,0)$，两个秩相等，方程组可解。因为 $\operatorname{rank}\mathbf{A}=1<2=n$，解不唯一：全部解为 $(1,\,1)^{\top}+t\,(2,\,-1)^{\top}$。又因为 $\operatorname{rank}\mathbf{A}=1<2=m$，存在无解的右端项。在第 [12.5](lineare-gleichungssysteme.html#stufe-12-5) 小节的超定方程组中，$\operatorname{rank}\mathbf{A}=2=n$：如果有解，解就是唯一的。但它无解，所以由 (i)，那里有 $\operatorname{rank}(\mathbf{A}\,|\,\mathbf{y})=3$。
::::

⁠**简而言之：**零空间汇集了矩阵映射为零的方向；$n$ 个输入方向分别归入零空间和秩。方程组 $\mathbf{A}\mathbf{x}=\mathbf{y}$ 可解，当且仅当右端项不使秩增大；解唯一，当且仅当零空间只含零向量。

### 线性相关的特征

<span class="anker" id="stufe-13-6"></span>

在真实的数据集中，特征有时把同样的信息记录了两次。一份问卷以千克记录体重，为了另一项分析，又以磅再记录一次。一份房屋描述给出一楼的面积、二楼的面积和总面积。对数据矩阵而言，这意味着：它的各列线性相关，它的秩小于特征的个数。

::::beispiel [算例] 一楼、二楼和总面积
四栋房屋：

$$\mathbf{X}=\begin{pmatrix}50&40&90\\60&0&60\\45&45&90\\70&30&100\end{pmatrix}\qquad(\text{面积，单位为 }\mathrm m^2).$$

第三列是前两列之和。所以 $\operatorname{rank}\mathbf{X}=2<3$，而零空间包含 $\mathbf k=(1,\,1,\,-1)^{\top}$，因为 $\mathbf{X}\mathbf k=\mathbf{0}$。由此得出两点。

<ul>

<li>

⁠**权重不唯一。**对每个数 $t$，$\mathbf{w}$ 和 $\mathbf{w}+t\,\mathbf k$ 给出同样的预测值，因为 $\mathbf{X}(\mathbf{w}+t\,\mathbf k)=\mathbf{X}\mathbf{w}+t\,\mathbf{X}\mathbf k=\mathbf{X}\mathbf{w}$。权重 $(3,\,3,\,0)^{\top}$（“一楼和二楼每平方米各计 $3$”）与 $(0,\,0,\,3)^{\top}$（“总面积每平方米计 $3$”）都给出 $(270,\,180,\,270,\,300)^{\top}$。仅从预测值无法看出指的是哪组权重，而单独解释其中任何一个权重都没有意义。

</li>

<li>

⁠**特征的格拉姆矩阵是奇异的。**由 $\mathbf{X}\mathbf k=\mathbf{0}$ 得 $\mathbf{X}^{\top}\mathbf{X}\mathbf k=\mathbf{X}^{\top}\mathbf{0}=\mathbf{0}$，其中 $\mathbf k\ne\mathbf{0}$。由第 [11.5](einheitsmatrix-und-inverse.html#stufe-11-5) 小节，$\mathbf{X}^{\top}\mathbf{X}$ 于是没有逆矩阵。

</li>

</ul>
::::

::::beispiel [算例] 千克与磅
一磅恰好是 $0.45359237$ kg，所以同一质量以磅为单位的数值，是以千克为单位的数值的 $c=1/0.45359237\approx2.20462$ 倍。三个人的身高（cm）、体重（kg）和体重（磅）：

$$\mathbf{X}=\begin{pmatrix}170&70&70\,c\\182&85&85\,c\\165&60&60\,c\end{pmatrix}\approx\begin{pmatrix}170&70&154.3\\182&85&187.4\\165&60&132.3\end{pmatrix}.$$

第三列是第二列的 $c$ 倍，所以 $\operatorname{rank}\mathbf{X}=2$，而 $(0,\,c,\,-1)^{\top}$ 位于零空间中。磅这一列不带来新信息；它只是重复了已有的信息。
::::

⁠**简而言之：**如果特征把同样的信息记录了两次，数据矩阵的各列就线性相关；这时秩小于 $d$，不同的权重给出同样的预测值，而 $\mathbf{X}^{\top}\mathbf{X}$ 不可逆。

:::aufgabe 练习 31 ★★ 秩与零空间
<span class="anker" id="aufg-31"></span>

求下列矩阵的秩和零空间：

$$\mathbf{A}_1=\begin{pmatrix}1&2&3\\2&4&6\\1&0&1\end{pmatrix}\qquad\text{和}\qquad \mathbf{A}_2=\begin{pmatrix}1&1&0\\0&1&1\\1&0&1\end{pmatrix}$$

并在每种情况下验证秩-零化度定理。两个矩阵中哪个可逆？

:::loesung
$\mathbf{A}_1$：第二行是第一行的两倍。从第二行减去第一行的两倍，再从第三行减去第一行，剩下行 $(1,2,3)$、$(0,0,0)$、$(0,-2,-2)$；交换下面两行后，这是一个有两个主元的行阶梯形，所以 $\operatorname{rank}\mathbf{A}_1=2$。零空间由方程 $x_1+2x_2+3x_3=0$ 和 $-2x_2-2x_3=0$ 给出：令 $x_3=t$，得 $x_2=-t$，$x_1=-2(-t)-3t=-t$，所以 $\ker\mathbf{A}_1=\operatorname{span}\{(1,\,1,\,-1)^{\top}\}$。验算：前两列之和为 $(3,\,6,\,1)^{\top}$，而第三列也是 $(3,\,6,\,1)^{\top}$。秩-零化度定理：$1+2=3$。$\mathbf{A}_1$ 不可逆。

$\mathbf{A}_2$：从第三行减去第一行，得到 $(0,\,-1,\,1)$；再加上第二行，得到 $(0,\,0,\,2)$。三个主元，所以 $\operatorname{rank}\mathbf{A}_2=3$，$\ker\mathbf{A}_2=\{\mathbf{0}\}$。秩-零化度定理：$0+3=3$。$\mathbf{A}_2$ 可逆；它的行列式为 $1\cdot(1-0)-1\cdot(0-1)+0=2\ne0$。
:::
:::

:::aufgabe 练习 32 ★★ 千克与磅
<span class="anker" id="aufg-32"></span>

使用第 [13.6](#stufe-13-6) 小节中三个人的数据矩阵。

<ol class="al">

<li>

给出两个不同的权重向量，使它们对全部三个人给出同样的预测值，其中一个只用千克列，另一个只用磅列。

</li>

<li>

表中的磅值四舍五入到一位小数。四舍五入后的表格中，各列仍然精确地线性相关吗？这对由舍入数据算出的秩说明了什么？

</li>

</ol>

:::loesung
(a) 权重 $(0,\,1,\,0)^{\top}$ 预测每个人以千克为单位的体重，即 $(70,\,85,\,60)^{\top}$。只用磅列的权重 $(0,\,0,\,1/c)^{\top}\approx(0,\ 0,\ 0.4536)^{\top}$ 给出同样的预测值，因为 $\frac1c\cdot c\,x=x$。两个权重向量相差 $\frac1c\,(0,\,c,\,-1)^{\top}$，这是零空间中的一个向量。

(b) 四舍五入后的磅值与千克值之比为 $154.3/70\approx2.20429$、$187.4/85\approx2.20471$ 和 $132.3/60=2.205$，并不完全相等。所以四舍五入后的各列不再精确成比例；精确计算时，四舍五入后的表格具有满秩 $3$。从内容上说，什么也没有改变：磅列携带的几乎仍然只是千克列的信息。微小的舍入就使秩从 $2$ 跳到 $3$。因此，对于测量数据或舍入数据，仅凭秩无法判断两个特征是否携带实际上相同的信息。
:::
:::

:::aufgabe 练习 33 ★★ 把城区表示成数
<span class="anker" id="aufg-33"></span>

公寓要么位于北区，要么位于南区。把这一点转换成两个特征：对北区的公寓，“北”为 $1$，否则为 $0$；“南”对南区的公寓同样如此。为了表示基础价格，再附加一个全 1 列（第 [8.5](lineare-abbildungen.html#stufe-8-5) 小节）。北区和南区交替的四套公寓给出

$$\mathbf{X}=\begin{pmatrix}1&1&0\\1&0&1\\1&1&0\\1&0&1\end{pmatrix}\qquad(\text{各列：全 1、北、南}).$$

<ol class="al">

<li>

求 $\mathbf{X}$ 的秩，以及零空间中的一个向量 $\mathbf k\ne\mathbf{0}$。其背后是各列之间的什么关系？

</li>

<li>

证明权重 $(100,\,20,\,0)^{\top}$ 和 $(80,\,40,\,20)^{\top}$ 给出同样的预测值。如何在不丢失信息的情况下消除这种线性相关？

</li>

</ol>

:::loesung
(a) 每套公寓要么位于北区，要么位于南区，所以在每一行中，列“北”加上列“南”都等于 $1$，恰好等于全 1 列。各列线性相关，$\mathbf k=(1,\,-1,\,-1)^{\top}$ 位于零空间中：$\mathbf{X}\mathbf k=\mathbf{0}$。第一列和第二列线性无关，所以 $\operatorname{rank}\mathbf{X}=2$。

(b) $\mathbf{X}\,(100,\,20,\,0)^{\top}=(120,\,100,\,120,\,100)^{\top}$，$\mathbf{X}\,(80,\,40,\,20)^{\top}=(120,\,100,\,120,\,100)^{\top}$。两个权重向量相差 $(20,\,-20,\,-20)^{\top}=20\,\mathbf k$。去掉“北”和“南”两列中的一列，例如“南”，就消除了这种线性相关。这时基础价格就是南区的价格，而“北”的权重就是北区的加价。信息并没有丢失，因为“南”总是等于 $1-\text{北}$，随时都可以算回来。
:::
:::
