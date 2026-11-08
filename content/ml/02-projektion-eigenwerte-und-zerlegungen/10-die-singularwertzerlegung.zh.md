---
title: 奇异值分解
pfad: 计算机科学 / 机器学习 / 数学基础 / 投影、特征值与矩阵分解
knoten: 基础篇 2：投影、特征值与矩阵分解
nachschlagen: ja
order: 15221000
summary: 只有方阵才有特征向量，而且只有对称矩阵的特征向量才互相垂直。本节说明：每个矩阵，包括矩形矩阵，都有一对直角坐标系，一个在输入空间中，一个在输出空间中。矩阵把其中一个坐标系的每根轴映射为另一个坐标系中某根轴的倍数。由此得到每个矩阵的一种分解：旋转、拉伸、再旋转。
tags: 奇异值, 右奇异向量, 左奇异向量, 谱范数
lang: zh
---

<span class="anker" id="stufe-9"></span>

:::zweck
只有方阵才有特征向量，而且只有对称矩阵的特征向量才互相垂直。本节说明：每个矩阵，包括矩形矩阵，都有一对直角坐标系，一个在输入空间中，一个在输出空间中。矩阵把其中一个坐标系的每根轴映射为另一个坐标系中某根轴的倍数。由此得到每个矩阵的一种分解：旋转、拉伸、再旋转。
:::

### 保持垂直的垂直方向

<span class="anker" id="stufe-9-1"></span>

矩阵 $\mathbf{A}=\bigl(\begin{smallmatrix}2&3\\0&2\end{smallmatrix}\bigr)$ 是三角矩阵，有二重特征值 $2$，但只有一个特征方向：$(\mathbf{A}-2\mathbf{I})\mathbf{v}=\mathbf{0}$ 意味着 $3v_2=0$，所以只有 $\mathbf{e}_1$ 的倍数才符合条件（练习 [19](eigenwerte-und-eigenvektoren.html#aufg-19)）。由第 [7.2](diagonalisierung-und-spektralsatz.html#stufe-7-2) 节，它不可对角化。尽管如此，它把单位圆变成一个椭圆（图 [23](#abb-23)），而椭圆有两根互相垂直的轴。圆上的哪些箭头落在这两根轴上？

我们要找的东西比特征向量的要求更低：箭头可以改变方向。我们要找两个互相垂直的单位向量 $\mathbf{v}_1$、$\mathbf{v}_2$，使它们的像 $\mathbf{A}\mathbf{v}_1$ 和 $\mathbf{A}\mathbf{v}_2$ 也互相垂直。两个像是否垂直，由它们的点积判断：

$$(\mathbf{A}\mathbf{v}_1)^{\top}(\mathbf{A}\mathbf{v}_2)=\mathbf{v}_1^{\top}\,\mathbf{A}^{\top}\mathbf{A}\,\mathbf{v}_2 .$$

这里出现了格拉姆矩阵 $\mathbf{A}^{\top}\mathbf{A}$。即使 $\mathbf{A}$ 不对称，它也是对称的，并且由谱定理，它有一组由特征向量构成的标准正交基。若 $\mathbf{v}_2$ 是 $\mathbf{A}^{\top}\mathbf{A}$ 属于特征值 $\lambda_2$ 的特征向量，且 $\mathbf{v}_1$ 垂直于 $\mathbf{v}_2$，则点积为 $\lambda_2\,\mathbf{v}_1^{\top}\mathbf{v}_2=0$。所以 $\mathbf{A}^{\top}\mathbf{A}$ 的特征向量正好满足要求。取 $\mathbf{v}_1=\mathbf{v}_2$ 作同样的计算，就得到像的长度：$\lVert\mathbf{A}\mathbf{v}_i\rVert^2=\mathbf{v}_i^{\top}\mathbf{A}^{\top}\mathbf{A}\mathbf{v}_i=\lambda_i$。

⁠**算例：**对于 $\mathbf{A}=\bigl(\begin{smallmatrix}2&3\\0&2\end{smallmatrix}\bigr)$，有 $\mathbf{A}^{\top}\mathbf{A}=\bigl(\begin{smallmatrix}4&6\\6&13\end{smallmatrix}\bigr)$，其迹为 $17$，行列式为 $52-36=16$。特征多项式 $\lambda^2-17\lambda+16=(\lambda-16)(\lambda-1)$ 的根为 $16$ 和 $1$。归一化的特征向量为属于 $16$ 的 $\mathbf{v}_1=(1,\,2)^{\top}/\sqrt5$ 和属于 $1$ 的 $\mathbf{v}_2=(-2,\,1)^{\top}/\sqrt5$。它们的像

$$\mathbf{A}\mathbf{v}_1=\frac1{\sqrt5}\begin{pmatrix}8\\4\end{pmatrix},\qquad \mathbf{A}\mathbf{v}_2=\frac1{\sqrt5}\begin{pmatrix}-1\\2\end{pmatrix}$$

的点积为 $\tfrac15(-8+8)=0$，长度为 $\sqrt{80/5}=4=\sqrt{16}$ 和 $1=\sqrt1$（图 [22](#abb-22)）。

:::abbildung ml/k2rsvdidee 22
像 $\mathbf{A}\mathbf{v}_1=(8,4)^{\top}/\sqrt5$ 和 $\mathbf{A}\mathbf{v}_2=(-1,2)^{\top}/\sqrt5$ 互相垂直，长度的平方为 $16$ 和 $1$，即 $\mathbf{A}^{\top}\mathbf{A}$ 的特征值。
:::

⁠**简而言之：**对称矩阵 $\mathbf{A}^{\top}\mathbf{A}$ 的特征向量是一些互相垂直的方向，它们在 $\mathbf{A}$ 下的像仍然互相垂直；像的长度为 $\sqrt{\lambda_i}$。

### 奇异值

<span class="anker" id="stufe-9-2"></span>

像的长度是矩阵最重要的指标：它们表明矩阵在其主方向上拉伸得有多强。由第 [8.4](positiv-definite-matrizen.html#stufe-8-4) 节，$\mathbf{A}^{\top}\mathbf{A}$ 是半正定的，所以它的特征值不为负，可以开平方。

:::definition 定义 9.1 (奇异值)
<span class="anker" id="satz-9-1"></span>

设 $\mathbf{A}\in\mathbb{R}^{m\times n}$，$\lambda_1\ge\lambda_2\ge\dots\ge\lambda_n\ge0$ 是 $\mathbf{A}^{\top}\mathbf{A}$ 按降序排列的特征值，重特征值按重数计算。数

<span class="anker" id="gl-9-1"></span>
$$d_j=\sqrt{\lambda_j},\qquad d_1\ge d_2\ge\dots\ge d_n\ge0 , \tag{9.1}$$

称为 $\mathbf{A}$ 的__奇异值__。
:::

许多书用 $\sigma_j$ 代替 $d_j$。本章中奇异值总是带下标；基础篇 1 中不带下标的 $d$ 表示特征（feature）的个数，那是另一回事。

:::satz 定理 9.2 (奇异值与秩)
<span class="anker" id="satz-9-2"></span>

不为零的奇异值的个数就是 $\mathbf{A}$ 的秩。
:::

:::beweis 奇异值与秩
设 $\mathbf{v}_1,\dots,\mathbf{v}_n$ 是 $\mathbf{A}^{\top}\mathbf{A}$ 属于 $\lambda_1,\dots,\lambda_n$ 的标准正交特征向量。每个向量都可以写成 $\mathbf{x}=\sum_jc_j\mathbf{v}_j$，所以 $\mathbf{A}\mathbf{x}=\sum_jc_j\,\mathbf{A}\mathbf{v}_j$：列空间由像 $\mathbf{A}\mathbf{v}_1,\dots,\mathbf{A}\mathbf{v}_n$ 张成。由上一小节，这些像两两垂直，长度为 $d_j$。$d_j=0$ 的像是零向量，没有贡献。其余的像互相垂直且不为零；除以各自的长度后，它们是标准正交的，由第 [1.1](orthonormalbasen-und-orthogonale-matrizen.html#stufe-1-1) 节的定理，它们线性无关。它们构成列空间的一组基，其个数就是秩。
:::

下文中矩阵的秩记作 $r$。有 $d_1\ge\dots\ge d_r>0$ 和 $d_{r+1}=\dots=d_n=0$。

⁠**算例：**$\mathbf{A}=\bigl(\begin{smallmatrix}2&3\\0&2\end{smallmatrix}\bigr)$ 的奇异值为 $d_1=4$ 和 $d_2=1$，秩为 $2$。它的特征值为 $2$ 和 $2$：奇异值与特征值一般是不同的数。矩阵 $\bigl(\begin{smallmatrix}1&2\\2&4\end{smallmatrix}\bigr)$ 有 $\mathbf{A}^{\top}\mathbf{A}=\bigl(\begin{smallmatrix}5&10\\10&20\end{smallmatrix}\bigr)$，特征值为 $25$ 和 $0$，因此奇异值为 $5$ 和 $0$，秩为 $1$。

⁠**简而言之：**奇异值 $d_j$ 是 $\mathbf{A}^{\top}\mathbf{A}$ 的特征值的平方根；它们衡量 $\mathbf{A}$ 在其主方向上拉伸得有多强，正奇异值的个数就是秩。

### 奇异向量

<span class="anker" id="stufe-9-3"></span>

每个正奇异值都对应两个方向：一个输入方向 $\mathbf{v}_j$，以及它的像的方向。

:::definition 定义 9.3 (奇异向量)
<span class="anker" id="satz-9-3"></span>

$\mathbf{A}^{\top}\mathbf{A}$ 属于特征值 $d_1^2,\dots,d_n^2$ 的标准正交特征向量 $\mathbf{v}_1,\dots,\mathbf{v}_n$ 称为 $\mathbf{A}$ 的__右奇异向量__。对于 $d_j>0$，

<span class="anker" id="gl-9-2"></span>
$$\mathbf{u}_j=\frac{\mathbf{A}\mathbf{v}_j}{d_j},\qquad\text{从而}\qquad \mathbf{A}\mathbf{v}_j=d_j\mathbf{u}_j , \tag{9.2}$$

称为相应的__左奇异向量__。
:::

这两个名称来自这些向量在下一小节的分解中所处的位置。左奇异向量也是标准正交的，因为

$$\mathbf{u}_i^{\top}\mathbf{u}_j=\frac{\mathbf{v}_i^{\top}\mathbf{A}^{\top}\mathbf{A}\mathbf{v}_j}{d_id_j}=\frac{d_j^2\,\mathbf{v}_i^{\top}\mathbf{v}_j}{d_id_j},$$

它在 $i=j$ 时为 $1$，否则为 $0$。它们是 $\mathbf{A}\mathbf{A}^{\top}$ 的特征向量，并且反方向的等式也成立：

$$\mathbf{A}^{\top}\mathbf{u}_j=\frac{\mathbf{A}^{\top}\mathbf{A}\mathbf{v}_j}{d_j}=d_j\mathbf{v}_j,\qquad \mathbf{A}\mathbf{A}^{\top}\mathbf{u}_j=d_j\,\mathbf{A}\mathbf{v}_j=d_j^2\,\mathbf{u}_j .$$

$\mathbf{A}$ 把 $\mathbf{v}_j$ 映射为 $d_j\mathbf{u}_j$，$\mathbf{A}^{\top}$ 把 $\mathbf{u}_j$ 映射为 $d_j\mathbf{v}_j$。

:::warnung 符号要配套
特征向量只确定到相差一个符号。如果把 $\mathbf{v}_j$ 作为 $\mathbf{A}^{\top}\mathbf{A}$ 的特征向量算出，再另外把 $\mathbf{u}_j$ 作为 $\mathbf{A}\mathbf{A}^{\top}$ 的特征向量算出，某个 $\mathbf{u}_j$ 就可能得到错误的符号，这时 $\mathbf{A}\mathbf{v}_j=-d_j\mathbf{u}_j$。稳妥的做法是借助式 [(9.2)](#gl-9-2)：先选定 $\mathbf{v}_j$，再计算 $\mathbf{u}_j=\mathbf{A}\mathbf{v}_j/d_j$。若把 $\mathbf{v}_j$ 和 $\mathbf{u}_j$ 同时反号，一切仍然正确。
:::

⁠**算例：**对于 $\mathbf{A}=\bigl(\begin{smallmatrix}2&3\\0&2\end{smallmatrix}\bigr)$，得 $\mathbf{u}_1=\mathbf{A}\mathbf{v}_1/4=(2,\,1)^{\top}/\sqrt5$ 和 $\mathbf{u}_2=\mathbf{A}\mathbf{v}_2/1=(-1,\,2)^{\top}/\sqrt5$。验算：$\mathbf{A}\mathbf{A}^{\top}=\bigl(\begin{smallmatrix}13&6\\6&4\end{smallmatrix}\bigr)$ 把 $(2,\,1)^{\top}$ 映射为 $(32,\,16)^{\top}=16\,(2,\,1)^{\top}$。向量 $(-2,\,-1)^{\top}/\sqrt5$ 也是 $\mathbf{A}\mathbf{A}^{\top}$ 属于 $16$ 的归一化特征向量，但用它的话，$\mathbf{A}\mathbf{v}_1=-4\,\mathbf{u}_1$。

⁠**简而言之：**右奇异向量 $\mathbf{v}_j$ 是 $\mathbf{A}^{\top}\mathbf{A}$ 的特征向量，左奇异向量是 $\mathbf{u}_j=\mathbf{A}\mathbf{v}_j/d_j$；两组向量都是标准正交的，并且 $\mathbf{A}\mathbf{v}_j=d_j\mathbf{u}_j$。

### 分解

<span class="anker" id="stufe-9-4"></span>

把对所有 $j$ 成立的等式 $\mathbf{A}\mathbf{v}_j=d_j\mathbf{u}_j$ 并排写在一起，就得到整个矩阵的一种分解。

:::satz 定理 9.4 (奇异值分解)
<span class="anker" id="satz-9-4"></span>

每个秩为 $r$ 的矩阵 $\mathbf{A}\in\mathbb{R}^{m\times n}$ 都可以写成

<span class="anker" id="gl-9-3"></span>
$$\mathbf{A}=\mathbf{U}\mathbf{D}\mathbf{V}^{\top} \tag{9.3}$$

其中 $\mathbf{U}\in\mathbb{R}^{m\times m}$ 和 $\mathbf{V}\in\mathbb{R}^{n\times n}$ 是正交矩阵，$\mathbf{D}\in\mathbb{R}^{m\times n}$ 的对角线上是奇异值 $d_1\ge\dots\ge d_r>0$，其余元素都是零。$\mathbf{V}$ 的列是右奇异向量，$\mathbf{U}$ 的前 $r$ 列是相应的左奇异向量。一种等价的形式是紧凑形式

<span class="anker" id="gl-9-4"></span>
$$\mathbf{A}=\sum_{j=1}^rd_j\,\mathbf{u}_j\mathbf{v}_j^{\top} . \tag{9.4}$$
:::

:::beweis 奇异值分解
对于 $j\le r$，有 $\mathbf{A}\mathbf{v}_j=d_j\mathbf{u}_j$。对于 $j>r$，有 $d_j=0$，所以 $\lVert\mathbf{A}\mathbf{v}_j\rVert=0$，$\mathbf{A}\mathbf{v}_j=\mathbf{0}$。若 $r<m$，就把 $\mathbf{u}_1,\dots,\mathbf{u}_r$ 扩充为 $\mathbb{R}^m$ 的一组标准正交基，例如像谱定理的证明中那样用格拉姆-施密特正交化。由基础篇 1 第 9.2 节，$\mathbf{A}\mathbf{V}$ 的第 $j$ 列是向量 $\mathbf{A}\mathbf{v}_j$，而 $\mathbf{U}\mathbf{D}$ 的第 $j$ 列在 $j\le r$ 时是 $d_j\mathbf{u}_j$，否则是零向量。所以 $\mathbf{A}\mathbf{V}=\mathbf{U}\mathbf{D}$。因为 $\mathbf{V}$ 是正交矩阵，$\mathbf{V}\mathbf{V}^{\top}=\mathbf{I}$，从右边乘以 $\mathbf{V}^{\top}$ 得 $\mathbf{A}=\mathbf{U}\mathbf{D}\mathbf{V}^{\top}$。紧凑形式由基础篇 1 第 9.5 节得出：$\mathbf{U}\mathbf{D}$ 的第 $j$ 列乘以 $\mathbf{V}^{\top}$ 的第 $j$ 行，再对 $j$ 求和；只有 $j\le r$ 的项不为零。
:::

$\mathbf{D}$ 的形状取决于 $\mathbf{A}$ 的形状。例如对于 $m=3$、$n=2$，$\mathbf{D}=\Bigl(\begin{smallmatrix}d_1&0\\0&d_2\\0&0\end{smallmatrix}\Bigr)$。常用的缩写是 SVD，取自英文名称 **singular value decomposition**。

⁠**算例：**对于 $\mathbf{A}=\bigl(\begin{smallmatrix}2&3\\0&2\end{smallmatrix}\bigr)$，

$$\mathbf{A}=\underbrace{\frac1{\sqrt5}\begin{pmatrix}2&-1\\1&2\end{pmatrix}}_{\mathbf{U}}\underbrace{\begin{pmatrix}4&0\\0&1\end{pmatrix}}_{\mathbf{D}}\underbrace{\frac1{\sqrt5}\begin{pmatrix}1&2\\-2&1\end{pmatrix}}_{\mathbf{V}^{\top}},$$

因为 $\mathbf{U}\mathbf{D}=\tfrac1{\sqrt5}\bigl(\begin{smallmatrix}8&-1\\4&2\end{smallmatrix}\bigr)$，并且 $\mathbf{U}\mathbf{D}\mathbf{V}^{\top}=\tfrac15\bigl(\begin{smallmatrix}8+2&16-1\\4-4&8+2\end{smallmatrix}\bigr)=\bigl(\begin{smallmatrix}2&3\\0&2\end{smallmatrix}\bigr)$。写成紧凑形式：

$$4\cdot\frac15\begin{pmatrix}2&4\\1&2\end{pmatrix}+1\cdot\frac15\begin{pmatrix}2&-1\\-4&2\end{pmatrix}=\begin{pmatrix}1.6&3.2\\0.8&1.6\end{pmatrix}+\begin{pmatrix}0.4&-0.2\\-0.8&0.4\end{pmatrix}=\begin{pmatrix}2&3\\0&2\end{pmatrix}.$$

⁠**简而言之：**每个矩阵都是 $\mathbf{U}\mathbf{D}\mathbf{V}^{\top}$，其中有两个正交矩阵，奇异值位于 $\mathbf{D}$ 的对角线上；等价地，每个矩阵都是和 $\sum_jd_j\mathbf{u}_j\mathbf{v}_j^{\top}$。

:::hintergrund 为什么每个矩阵都有这种分解
并非每个矩阵都有特征向量，而矩阵的特征向量也不总是互相垂直。奇异值分解用一个技巧绕过了这两个障碍：它用的不是 $\mathbf{A}$ 的特征向量，而是 $\mathbf{A}^{\top}\mathbf{A}$ 的特征向量。对每个 $\mathbf{A}$，这个矩阵都是对称且半正定的，谱定理保证它有一组由特征向量构成的标准正交基，特征值都 $\ge0$。代价是：需要两组基而不是一组，一组用于输入，一组用于输出。

奇异向量也可以不借助 $\mathbf{A}^{\top}\mathbf{A}$ 来描述。把式 [(8.2)](positiv-definite-matrizen.html#gl-8-2) 应用于 $\mathbf{A}^{\top}\mathbf{A}$，每个单位向量都满足 $\lVert\mathbf{A}\mathbf{v}\rVert^2=\mathbf{v}^{\top}\mathbf{A}^{\top}\mathbf{A}\mathbf{v}\le\lambda_1=d_1^2$，等号在 $\mathbf{v}_1$ 处成立。所以 $\mathbf{v}_1$ 是被 $\mathbf{A}$ 拉伸得最厉害的方向，$d_1$ 就是这个最大的拉伸。在所有垂直于 $\mathbf{v}_1$ 的单位向量中，被拉伸得最厉害的是 $\mathbf{v}_2$，依此类推；这可以用与式 [(8.2)](positiv-definite-matrizen.html#gl-8-2) 的证明中相同的加权平均计算来说明，只需令 $c_1=0$。所以这个分解按顺序列出了各个方向，从拉伸最强的到拉伸最弱的。

奇异值是唯一的。若所有 $d_j$ 互不相同且为正，则每一对 $\mathbf{v}_j,\mathbf{u}_j$ 都确定到相差一个共同的符号。若有相等的奇异值，自由度就更大：正交矩阵 $\mathbf{Q}$ 的奇异值全为 $1$，而对每个正交矩阵 $\mathbf{V}$，分解 $\mathbf{Q}=(\mathbf{Q}\mathbf{V})\,\mathbf{I}\,\mathbf{V}^{\top}$ 都是一个奇异值分解。
:::

### 旋转、拉伸、旋转

<span class="anker" id="stufe-9-5"></span>

把 $\mathbf{A}\mathbf{x}=\mathbf{U}\bigl(\mathbf{D}(\mathbf{V}^{\top}\mathbf{x})\bigr)$ 从右往左读，每个矩阵都分三步起作用（图 [23](#abb-23)）：

<ol>

<li>

由式 [(1.2)](orthonormalbasen-und-orthogonale-matrizen.html#gl-1-2)，$\mathbf{V}^{\top}\mathbf{x}$ 算出 $\mathbf{x}$ 在由各 $\mathbf{v}_j$ 构成的基下的坐标 $c_j=\mathbf{v}_j^{\top}\mathbf{x}$。从几何上看，这是一个把 $\mathbf{v}_j$ 转到 $\mathbf{e}_j$ 上的旋转或反射。

</li>

<li>

$\mathbf{D}$ 把每个坐标 $c_j$ 乘以 $d_j$。若 $m>n$，$\mathbf{D}$ 在后面补上零；若 $m<n$，$\mathbf{D}$ 丢掉最后几个坐标。单位圆变成一个椭圆，它的轴位于坐标轴上。

</li>

<li>

$\mathbf{U}$ 把 $\mathbf{e}_j$ 转到 $\mathbf{u}_j$ 上，这又是一个旋转或反射。

</li>

</ol>

所以，除反射之外，每个线性映射都是一次旋转、一次沿坐标轴的拉伸和又一次旋转。它把单位圆变成椭圆，把单位球变成椭球，半轴为 $d_j\mathbf{u}_j$。若 $\det\mathbf{A}<0$，其中至少有一次反射，因为由基础篇 1 第 14.5 节，$\det\mathbf{A}=\det\mathbf{U}\cdot\det\mathbf{D}\cdot\det\mathbf{V}^{\top}$，而 $\det\mathbf{D}\ge0$。

:::abbildung ml/k2svd 23
矩阵 $\mathbf{A}=\bigl(\begin{smallmatrix}2&3\\0&2\end{smallmatrix}\bigr)$ 表示为旋转、拉伸、旋转。左上：单位圆，以及 $\mathbf{v}_1=(1,2)^{\top}/\sqrt5$（红色）和 $\mathbf{v}_2=(-2,1)^{\top}/\sqrt5$（绿色）。$\mathbf{V}^{\top}$ 旋转 $-63.4^\circ$，把 $\mathbf{v}_1$ 转到 $\mathbf{e}_1$ 上，把 $\mathbf{v}_2$ 转到 $\mathbf{e}_2$ 上（左下）。$\mathbf{D}$ 把第一根轴拉伸 $d_1=4$ 倍，把第二根轴拉伸 $d_2=1$ 倍（右下）。$\mathbf{U}$ 旋转 $26.6^\circ$，把两根轴转到 $\mathbf{u}_1=(2,1)^{\top}/\sqrt5$ 和 $\mathbf{u}_2=(-1,2)^{\top}/\sqrt5$ 上（右上）。黑点 $\mathbf{x}=\mathbf{e}_2$ 无论走哪条路，最后都落在 $\mathbf{A}\mathbf{x}=(3,2)^{\top}$。上方的直接路径就是 $\mathbf{A}$ 本身：单位圆变成半轴为 $4\,\mathbf{u}_1$ 和 $1\cdot\mathbf{u}_2$ 的椭圆。
:::

⁠**算例：**对于 $\mathbf{x}=\mathbf{e}_2$ 和 $\mathbf{A}=\bigl(\begin{smallmatrix}2&3\\0&2\end{smallmatrix}\bigr)$，坐标为 $\mathbf{V}^{\top}\mathbf{x}=(2,\,1)^{\top}/\sqrt5$。拉伸后得 $\mathbf{D}\mathbf{V}^{\top}\mathbf{x}=(8,\,1)^{\top}/\sqrt5$，再旋转，得

$$\mathbf{U}\mathbf{D}\mathbf{V}^{\top}\mathbf{x}=\frac15\begin{pmatrix}2&-1\\1&2\end{pmatrix}\begin{pmatrix}8\\1\end{pmatrix}=\frac15\begin{pmatrix}15\\10\end{pmatrix}=\begin{pmatrix}3\\2\end{pmatrix}=\mathbf{A}\mathbf{e}_2 .$$

$\mathbf{V}$ 的列为 $(\cos\theta,\,\sin\theta)^{\top}$ 和 $(-\sin\theta,\,\cos\theta)^{\top}$，其中 $\cos\theta=1/\sqrt5$，所以它是旋转 $\theta\approx63.4^\circ$，而 $\mathbf{V}^{\top}$ 旋转 $-63.4^\circ$ 转回去。$\mathbf{U}$ 是旋转 $26.6^\circ$，因为 $\cos26.6^\circ\approx2/\sqrt5$。

⁠**简而言之：**除反射之外，每个矩阵都是先旋转、再沿坐标轴拉伸、然后再旋转；单位圆变成半轴为 $d_j\mathbf{u}_j$ 的椭圆。

### 秩 1 的构件与矩阵的各个空间

<span class="anker" id="stufe-9-6"></span>

紧凑形式 [(9.4)](#gl-9-4) 中的每一项 $d_j\mathbf{u}_j\mathbf{v}_j^{\top}$ 的秩都为 $1$，因为它的所有列都是 $\mathbf{u}_j$ 的倍数。它对向量的作用如下：

$$d_j\mathbf{u}_j\mathbf{v}_j^{\top}\mathbf{x}=d_j\,(\mathbf{v}_j^{\top}\mathbf{x})\,\mathbf{u}_j .$$

它读出 $\mathbf{x}$ 沿 $\mathbf{v}_j$ 的坐标，乘以 $d_j$，再把结果沿 $\mathbf{u}_j$ 方向输出。矩阵是 $r$ 个这样的构件之和，按它们的大小 $d_j$ 排列。顺带地，这个分解还给出了与矩阵相关的各个子空间的标准正交基。

:::satz 定理 9.5 (奇异向量张成什么)
<span class="anker" id="satz-9-5"></span>

设 $\mathbf{A}=\mathbf{U}\mathbf{D}\mathbf{V}^{\top}$，秩为 $r$。则：

<ol class="rm">

<li>

$\mathbf{u}_1,\dots,\mathbf{u}_r$ 是 $\mathbf{A}$ 的列空间的一组标准正交基，$\mathbf{u}_{r+1},\dots,\mathbf{u}_m$ 是该列空间的正交补的一组标准正交基；

</li>

<li>

$\mathbf{v}_{r+1},\dots,\mathbf{v}_n$ 是 $\mathbf{A}$ 的零空间的一组标准正交基，$\mathbf{v}_1,\dots,\mathbf{v}_r$ 是 $\mathbf{A}^{\top}$ 的列空间的一组标准正交基。

</li>

</ol>
:::

:::beweis 空间
(i) 每个 $\mathbf{A}\mathbf{x}=\sum_{j\le r}d_j(\mathbf{v}_j^{\top}\mathbf{x})\mathbf{u}_j$ 都在 $\mathbf{u}_1,\dots,\mathbf{u}_r$ 张成的空间中；反过来，$\mathbf{u}_j=\mathbf{A}(\mathbf{v}_j/d_j)$ 是一个像。$\mathbf{U}$ 的其余各列垂直于这些向量，所以由第 [4.4](projektion-auf-einen-unterraum.html#stufe-4-4) 节，它们张成正交补。(ii) 由于各 $\mathbf{u}_j$ 线性无关且各 $d_j$ 为正，$\mathbf{A}\mathbf{x}=\mathbf{0}$ 当且仅当对所有 $j\le r$ 都有 $\mathbf{v}_j^{\top}\mathbf{x}=0$，即 $\mathbf{x}$ 只有沿 $\mathbf{v}_{r+1},\dots,\mathbf{v}_n$ 的坐标。最后，$\mathbf{A}^{\top}=\mathbf{V}\mathbf{D}^{\top}\mathbf{U}^{\top}$ 是 $\mathbf{A}^{\top}$ 的一个奇异值分解，其中 $\mathbf{U}$ 和 $\mathbf{V}$ 互换了角色；把 (i) 用于 $\mathbf{A}^{\top}$ 就得到其余结论。
:::

这些数与基础篇 1 第 13.5 节的秩-零化度定理相符：零空间的维数为 $n-r$。

⁠**算例：**第 [3.2](die-beste-naherungslosung.html#stufe-3-2) 节中列为 $(1,\,0,\,1)^{\top}$ 和 $(0,\,1,\,1)^{\top}$ 的矩阵 $\mathbf{H}$ 有 $\mathbf{H}^{\top}\mathbf{H}=\bigl(\begin{smallmatrix}2&1\\1&2\end{smallmatrix}\bigr)$，特征值为 $3$ 和 $1$，因此奇异值为 $d_1=\sqrt3$ 和 $d_2=1$，右奇异向量为 $\mathbf{v}_1=(1,\,1)^{\top}/\sqrt2$、$\mathbf{v}_2=(1,\,-1)^{\top}/\sqrt2$。左奇异向量为

$$\mathbf{u}_1=\frac{\mathbf{H}\mathbf{v}_1}{\sqrt3}=\frac1{\sqrt6}\begin{pmatrix}1\\1\\2\end{pmatrix},\qquad \mathbf{u}_2=\frac{\mathbf{H}\mathbf{v}_2}{1}=\frac1{\sqrt2}\begin{pmatrix}1\\-1\\0\end{pmatrix}.$$

它们构成平面 $x_3=x_1+x_2$ 的一组标准正交基，与第 [4.3](projektion-auf-einen-unterraum.html#stufe-4-3) 节中的那组不同。再补上 $\mathbf{u}_3=(1,\,1,\,-1)^{\top}/\sqrt3$，即第 [4.4](projektion-auf-einen-unterraum.html#stufe-4-4) 节中归一化的法向量，基就完整了。在完整的分解中，$\mathbf{D}=\Bigl(\begin{smallmatrix}\sqrt3&0\\0&1\\0&0\end{smallmatrix}\Bigr)$。零空间只含零向量，因为 $r=n=2$。

⁠**简而言之：**矩阵是 $r$ 个秩为 $1$ 的构件 $d_j\mathbf{u}_j\mathbf{v}_j^{\top}$ 之和；$d_j>0$ 的 $\mathbf{u}_j$ 张成列空间，$d_j=0$ 的 $\mathbf{v}_j$ 张成零空间。

### 对称矩阵

<span class="anker" id="stufe-9-7"></span>

对称矩阵已经有一个借助标准正交基的分解 $\mathbf{A}=\mathbf{Q}\boldsymbol{\Lambda}\mathbf{Q}^{\top}$。它与奇异值分解有什么关系？

:::satz 定理 9.6 (对称矩阵的奇异值)
<span class="anker" id="satz-9-6"></span>

对称矩阵的奇异值是其特征值的绝对值 $|\lambda_i|$。若 $\mathbf{q}_i$ 是属于 $\lambda_i\ne0$ 的归一化特征向量，则 $\mathbf{v}=\mathbf{q}_i$ 是一个右奇异向量，$\mathbf{u}=\operatorname{sign}(\lambda_i)\,\mathbf{q}_i$ 是相应的左奇异向量。
:::

:::beweis 对称矩阵
有 $\mathbf{A}^{\top}\mathbf{A}=\mathbf{A}^2=\mathbf{Q}\boldsymbol{\Lambda}^2\mathbf{Q}^{\top}$，所以 $\mathbf{A}^{\top}\mathbf{A}$ 的特征向量为 $\mathbf{q}_i$，特征值为 $\lambda_i^2$，奇异值为 $\sqrt{\lambda_i^2}=|\lambda_i|$。由式 [(9.2)](#gl-9-2)，$\mathbf{u}=\mathbf{A}\mathbf{q}_i/|\lambda_i|=(\lambda_i/|\lambda_i|)\,\mathbf{q}_i$。
:::

若 $\mathbf{A}$ 是半正定的，谱分解和奇异值分解就是同一个分解，且 $\mathbf{U}=\mathbf{V}=\mathbf{Q}$。对于负特征值，符号移到 $\mathbf{U}$ 中。对于非对称矩阵，特征值和奇异值一般没有什么关系，特征值为 $2,2$、奇异值为 $4,1$ 的 $\bigl(\begin{smallmatrix}2&3\\0&2\end{smallmatrix}\bigr)$ 就说明了这一点。不过二者之间总有一个联系：每个特征值的模都不超过 $d_1$；这由下一小节得出。

⁠**算例：**$\mathbf{A}=\bigl(\begin{smallmatrix}1&3\\3&1\end{smallmatrix}\bigr)$ 有特征值 $4$（对应 $\mathbf{q}_1=(1,\,1)^{\top}/\sqrt2$）和 $-2$（对应 $\mathbf{q}_2=(1,\,-1)^{\top}/\sqrt2$）。奇异值为 $4$ 和 $2$。取 $\mathbf{v}_2=\mathbf{q}_2$，得 $\mathbf{A}\mathbf{v}_2=(-2,\,2)^{\top}/\sqrt2=2\cdot(-1,\,1)^{\top}/\sqrt2$，所以 $\mathbf{u}_2=-\mathbf{q}_2$。

⁠**简而言之：**对于对称矩阵，奇异值是特征值的绝对值；对于半正定矩阵，奇异值分解就是谱分解。

### 谱范数

<span class="anker" id="stufe-9-8"></span>

一个矩阵最多能把向量拉长多少？对于向量，范数衡量大小。对于矩阵，一个自然的大小度量是它最大的拉长因子。

:::definition 定义 9.7 (谱范数)
<span class="anker" id="satz-9-7"></span>

矩阵 $\mathbf{A}$ 的__谱范数__为

$$\lVert\mathbf{A}\rVert_2=\max_{\mathbf{x}\ne\mathbf{0}}\frac{\lVert\mathbf{A}\mathbf{x}\rVert}{\lVert\mathbf{x}\rVert} .$$
:::

:::satz 定理 9.8 (最大拉伸与最小拉伸)
<span class="anker" id="satz-9-8"></span>

对每个奇异值为 $d_1\ge\dots\ge d_n$ 的 $\mathbf{A}\in\mathbb{R}^{m\times n}$ 和每个 $\mathbf{x}\in\mathbb{R}^n$，有

<span class="anker" id="gl-9-5"></span>
$$d_n\,\lVert\mathbf{x}\rVert\le\lVert\mathbf{A}\mathbf{x}\rVert\le d_1\,\lVert\mathbf{x}\rVert . \tag{9.5}$$

这两个界在 $\mathbf{x}=\mathbf{v}_1$ 和 $\mathbf{x}=\mathbf{v}_n$ 处取到。特别地，$\lVert\mathbf{A}\rVert_2=d_1$。
:::

:::beweis 最大拉伸与最小拉伸
令 $\mathbf{c}=\mathbf{V}^{\top}\mathbf{x}$，则 $\lVert\mathbf{c}\rVert=\lVert\mathbf{x}\rVert$，并且 $\lVert\mathbf{A}\mathbf{x}\rVert^2=\mathbf{x}^{\top}\mathbf{A}^{\top}\mathbf{A}\mathbf{x}=\sum_jd_j^2c_j^2$。它介于 $d_n^2\sum_jc_j^2$ 与 $d_1^2\sum_jc_j^2$ 之间。它就是 $\mathbf{A}^{\top}\mathbf{A}$ 的瑞利商 [(8.2)](positiv-definite-matrizen.html#gl-8-2) 乘以 $\lVert\mathbf{x}\rVert^2$。
:::

两个推论。第一，$\lVert\mathbf{A}\mathbf{x}\rVert\le\lVert\mathbf{A}\rVert_2\lVert\mathbf{x}\rVert$，因此 $\lVert\mathbf{A}\mathbf{B}\mathbf{x}\rVert\le\lVert\mathbf{A}\rVert_2\lVert\mathbf{B}\rVert_2\lVert\mathbf{x}\rVert$，所以 $\lVert\mathbf{A}\mathbf{B}\rVert_2\le\lVert\mathbf{A}\rVert_2\lVert\mathbf{B}\rVert_2$：两个映射相继作用时，它们最大的拉伸因子至多相乘。第二，每个特征向量都满足 $\lVert\mathbf{A}\mathbf{v}\rVert=|\lambda|\,\lVert\mathbf{v}\rVert$，所以对方阵的每个特征值都有 $|\lambda|\le d_1$。对于由实向量 $\mathbf{a},\mathbf{b}$ 构成的复特征向量 $\mathbf{v}=\mathbf{a}+\mathrm j\mathbf{b}$，只要令 $\lVert\mathbf{v}\rVert^2=(\mathbf{v}^*)^{\top}\mathbf{v}=\lVert\mathbf{a}\rVert^2+\lVert\mathbf{b}\rVert^2$，同样的结论也成立，因为由式 [(9.5)](#gl-9-5)，$\lVert\mathbf{A}\mathbf{v}\rVert^2=\lVert\mathbf{A}\mathbf{a}\rVert^2+\lVert\mathbf{A}\mathbf{b}\rVert^2$ 介于 $d_n^2\lVert\mathbf{v}\rVert^2$ 与 $d_1^2\lVert\mathbf{v}\rVert^2$ 之间；因此对于方阵 $\mathbf{A}$，也有 $|\lambda|\ge d_n$。

⁠**算例：**对于 $\mathbf{A}=\bigl(\begin{smallmatrix}2&3\\0&2\end{smallmatrix}\bigr)$，有 $\lVert\mathbf{A}\rVert_2=4$。单位向量被拉伸得少一些：$\lVert\mathbf{A}\mathbf{e}_1\rVert=\lVert(2,\,0)^{\top}\rVert=2$，$\lVert\mathbf{A}\mathbf{e}_2\rVert=\lVert(3,\,2)^{\top}\rVert=\sqrt{13}\approx3.61$。因子 $4$ 只在 $\mathbf{v}_1=(1,\,2)^{\top}/\sqrt5$ 处达到，最小因子 $1$ 在 $\mathbf{v}_2$ 处达到。特征值 $2$ 介于 $1$ 和 $4$ 之间。

⁠**简而言之：**谱范数 $\lVert\mathbf{A}\rVert_2=d_1$ 是 $\mathbf{A}$ 拉长向量的最大因子；最小因子是 $d_n$。

:::hintergrund 多天线：由奇异值分解得到并行信道
具有多个发射天线和接收天线的无线电系统称为 MIMO 系统。每个接收天线收到的都是所有发射信号的混合。在一个简单的模型中，接收到的向量为 $\mathbf{y}=\mathbf{K}\mathbf{x}+\boldsymbol\nu$：$\mathbf{x}$ 包含各天线的发射信号，信道矩阵 $\mathbf{K}$ 描述每个发射天线的信号以多大强度到达每个接收天线，$\boldsymbol\nu$ 是噪声。

如果发射机和接收机都知道分解 $\mathbf{K}=\mathbf{U}\mathbf{D}\mathbf{V}^{\top}$，发射机就发送 $\mathbf{x}=\mathbf{V}\tilde{\mathbf{x}}$，接收机计算 $\tilde{\mathbf{y}}=\mathbf{U}^{\top}\mathbf{y}$。于是

$$\tilde{\mathbf{y}}=\mathbf{U}^{\top}\mathbf{U}\mathbf{D}\mathbf{V}^{\top}\mathbf{V}\tilde{\mathbf{x}}+\mathbf{U}^{\top}\boldsymbol\nu=\mathbf{D}\tilde{\mathbf{x}}+\tilde{\boldsymbol\nu} .$$

混合的信道变成了 $r$ 个独立的信道：$\tilde y_j=d_j\tilde x_j+\tilde\nu_j$。每个信道传输各自的数据流，增益为 $d_j$。在此过程中噪声只是被旋转，长度保持不变，因为 $\mathbf{U}^{\top}$ 是正交矩阵。可用的并行信道数就是信道矩阵的秩，每个信道的好坏由它的奇异值表明。这就是实践中的旋转、拉伸、旋转：发射机预先旋转，信道拉伸，接收机再转回来。
:::

:::aufgabe 练习 27 ★★ 手算一个分解
<span class="anker" id="aufg-27"></span>

设 $\mathbf{A}=\bigl(\begin{smallmatrix}3&0\\4&5\end{smallmatrix}\bigr)$。

<ol class="al">

<li>

计算 $\mathbf{A}^{\top}\mathbf{A}$、它的特征值以及 $\mathbf{A}$ 的奇异值。

</li>

<li>

求 $\mathbf{v}_1,\mathbf{v}_2$，再由式 [(9.2)](#gl-9-2) 求出 $\mathbf{u}_1,\mathbf{u}_2$。验证 $\mathbf{A}=\mathbf{U}\mathbf{D}\mathbf{V}^{\top}$。

</li>

<li>

把奇异值与 $\mathbf{A}$ 的特征值作比较。哪些一致，哪些不一致？

</li>

</ol>

:::loesung
(a) $\mathbf{A}^{\top}\mathbf{A}=\bigl(\begin{smallmatrix}9+16&20\\20&25\end{smallmatrix}\bigr)=\bigl(\begin{smallmatrix}25&20\\20&25\end{smallmatrix}\bigr)$，迹为 $50$，行列式为 $625-400=225$，所以 $\lambda^2-50\lambda+225=(\lambda-45)(\lambda-5)$。奇异值为 $d_1=\sqrt{45}=3\sqrt5\approx6.708$ 和 $d_2=\sqrt5\approx2.236$。

(b) $\mathbf{A}^{\top}\mathbf{A}$ 的特征向量：属于 $45$ 的 $\mathbf{v}_1=(1,\,1)^{\top}/\sqrt2$ 和属于 $5$ 的 $\mathbf{v}_2=(-1,\,1)^{\top}/\sqrt2$。于是

$$\mathbf{u}_1=\frac{\mathbf{A}\mathbf{v}_1}{d_1}=\frac{(3,\,9)^{\top}}{\sqrt2\cdot3\sqrt5}=\frac{(1,\,3)^{\top}}{\sqrt{10}},\qquad \mathbf{u}_2=\frac{\mathbf{A}\mathbf{v}_2}{d_2}=\frac{(-3,\,1)^{\top}}{\sqrt2\cdot\sqrt5}=\frac{(-3,\,1)^{\top}}{\sqrt{10}} .$$

验算：$\mathbf{U}\mathbf{D}=\tfrac1{\sqrt{10}}\bigl(\begin{smallmatrix}3\sqrt5&-3\sqrt5\\9\sqrt5&\sqrt5\end{smallmatrix}\bigr)=\tfrac1{\sqrt2}\bigl(\begin{smallmatrix}3&-3\\9&1\end{smallmatrix}\bigr)$，并且

$$\mathbf{U}\mathbf{D}\mathbf{V}^{\top}=\frac1{\sqrt2}\begin{pmatrix}3&-3\\9&1\end{pmatrix}\frac1{\sqrt2}\begin{pmatrix}1&1\\-1&1\end{pmatrix}=\frac12\begin{pmatrix}6&0\\8&10\end{pmatrix}=\begin{pmatrix}3&0\\4&5\end{pmatrix}.$$

(c) 三角矩阵的特征值为 $3$ 和 $5$。乘积一致：$3\cdot5=15=3\sqrt5\cdot\sqrt5=|\det\mathbf{A}|$。和则不一致：$8$ 对 $4\sqrt5\approx8.94$。特征值的绝对值介于 $d_2$ 与 $d_1$ 之间：$2.236\le3$，$5\le6.708$。
:::
:::

:::aufgabe 练习 28 ★★ 一个矩形矩阵
<span class="anker" id="aufg-28"></span>

设 $\mathbf{A}=\Bigl(\begin{smallmatrix}1&1\\1&1\\1&-1\end{smallmatrix}\Bigr)$。

<ol class="al">

<li>

求奇异值和奇异向量 $\mathbf{v}_1,\mathbf{v}_2,\mathbf{u}_1,\mathbf{u}_2$。

</li>

<li>

补上 $\mathbf{u}_3$，写出完整的分解 $\mathbf{A}=\mathbf{U}\mathbf{D}\mathbf{V}^{\top}$。

</li>

<li>

给出列空间及其正交补的标准正交基。

</li>

</ol>

:::loesung
(a) $\mathbf{A}^{\top}\mathbf{A}=\bigl(\begin{smallmatrix}3&1\\1&3\end{smallmatrix}\bigr)$ 的特征值为 $4$（特征向量 $\mathbf{v}_1=(1,\,1)^{\top}/\sqrt2$）和 $2$（特征向量 $\mathbf{v}_2=(1,\,-1)^{\top}/\sqrt2$）。所以 $d_1=2$，$d_2=\sqrt2$，并且

$$\mathbf{u}_1=\frac{\mathbf{A}\mathbf{v}_1}2=\frac{(2,\,2,\,0)^{\top}}{2\sqrt2}=\frac{(1,\,1,\,0)^{\top}}{\sqrt2},\qquad \mathbf{u}_2=\frac{\mathbf{A}\mathbf{v}_2}{\sqrt2}=\frac{(0,\,0,\,2)^{\top}}{\sqrt2\cdot\sqrt2}=(0,\,0,\,1)^{\top} .$$

(b) $\mathbf{u}_3$ 垂直于这两个向量：$\mathbf{u}_3=(1,\,-1,\,0)^{\top}/\sqrt2$。完整的分解为

$$\mathbf{A}=\begin{pmatrix}1/\sqrt2&0&1/\sqrt2\\1/\sqrt2&0&-1/\sqrt2\\0&1&0\end{pmatrix}\begin{pmatrix}2&0\\0&\sqrt2\\0&0\end{pmatrix}\frac1{\sqrt2}\begin{pmatrix}1&1\\1&-1\end{pmatrix}.$$

(c) 由第 [9.6](#stufe-9-6) 节的定理，$\mathbf{u}_1,\mathbf{u}_2$ 是列空间的一组标准正交基，$\mathbf{u}_3$ 是正交补的一组标准正交基。检验：列 $(1,\,1,\,1)^{\top}=\sqrt2\,\mathbf{u}_1+\mathbf{u}_2$ 和 $(1,\,1,\,-1)^{\top}=\sqrt2\,\mathbf{u}_1-\mathbf{u}_2$ 位于 $\mathbf{u}_1,\mathbf{u}_2$ 张成的空间中，并且都垂直于 $\mathbf{u}_3$。
:::
:::

:::aufgabe 练习 29 ★★★ 奇异值的性质
<span class="anker" id="aufg-29"></span>

<ol class="al">

<li>

证明：对于方阵，$|\det\mathbf{A}|=d_1d_2\cdots d_n$。

</li>

<li>

证明：$\mathbf{A}$ 和 $\mathbf{A}^{\top}$ 有相同的正奇异值。

</li>

<li>

证明：对于 $\mathbf{u}\ne\mathbf{0}$ 和 $\mathbf{v}\ne\mathbf{0}$，外积 $\mathbf{u}\mathbf{v}^{\top}$ 恰有一个正奇异值，即 $\lVert\mathbf{u}\rVert\,\lVert\mathbf{v}\rVert$。

</li>

<li>

证明：若 $\mathbf{Q}$ 是正交矩阵，则 $\mathbf{Q}\mathbf{A}$ 与 $\mathbf{A}$ 有相同的奇异值。

</li>

</ol>

:::loesung
(a) 由基础篇 1 第 14.5 节，$\det\mathbf{A}=\det\mathbf{U}\cdot\det\mathbf{D}\cdot\det\mathbf{V}^{\top}$。两个正交矩阵的行列式为 $\pm1$，而 $\mathbf{D}$ 是对角矩阵，行列式为 $d_1\cdots d_n$。因此 $|\det\mathbf{A}|=d_1\cdots d_n$。

(b) 由 $\mathbf{A}=\mathbf{U}\mathbf{D}\mathbf{V}^{\top}$ 得 $\mathbf{A}^{\top}\mathbf{A}=\mathbf{V}\mathbf{D}^{\top}\mathbf{D}\mathbf{V}^{\top}$ 和 $\mathbf{A}\mathbf{A}^{\top}=\mathbf{U}\mathbf{D}\mathbf{D}^{\top}\mathbf{U}^{\top}$。对角矩阵 $\mathbf{D}^{\top}\mathbf{D}$ 和 $\mathbf{D}\mathbf{D}^{\top}$ 的对角线上有相同的元素 $d_j^2>0$，只是零的个数不同。$\mathbf{A}^{\top}$ 的奇异值是 $(\mathbf{A}^{\top})^{\top}\mathbf{A}^{\top}=\mathbf{A}\mathbf{A}^{\top}$ 的特征值的平方根，因此仍是这些 $d_j$，再补上一些零。

(c) $(\mathbf{u}\mathbf{v}^{\top})^{\top}(\mathbf{u}\mathbf{v}^{\top})=\mathbf{v}\,\mathbf{u}^{\top}\mathbf{u}\,\mathbf{v}^{\top}=\lVert\mathbf{u}\rVert^2\,\mathbf{v}\mathbf{v}^{\top}$。这个矩阵把 $\mathbf{v}$ 映射为 $\lVert\mathbf{u}\rVert^2\lVert\mathbf{v}\rVert^2\,\mathbf{v}$，把每个垂直于 $\mathbf{v}$ 的向量映射为零。因此它的特征值为 $\lVert\mathbf{u}\rVert^2\lVert\mathbf{v}\rVert^2$，其余都是 $0$，唯一的正奇异值是 $\lVert\mathbf{u}\rVert\,\lVert\mathbf{v}\rVert$。

(d) $(\mathbf{Q}\mathbf{A})^{\top}(\mathbf{Q}\mathbf{A})=\mathbf{A}^{\top}\mathbf{Q}^{\top}\mathbf{Q}\mathbf{A}=\mathbf{A}^{\top}\mathbf{A}$。两个矩阵有相同的格拉姆矩阵，因而有相同的奇异值。直观地说：在 $\mathbf{A}$ 之后再作一次旋转或反射，不改变椭圆的形状，只改变它的位置。
:::
:::
