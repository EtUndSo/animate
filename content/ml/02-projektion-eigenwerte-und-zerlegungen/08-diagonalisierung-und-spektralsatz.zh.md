---
title: 对角化与谱定理
pfad: 计算机科学 / 机器学习 / 数学基础 / 投影、特征值与矩阵分解
adresse: informatik/machine-learning/mathematische-grundlagen/projektion-eigenwerte-und-zerlegungen
knoten: 第 2 章：投影、特征值与矩阵分解
nachschlagen: ja
order: 15220800
summary: 如果用矩阵自身的特征向量构成的基来描述矩阵，它就成为对角矩阵：每个坐标只被乘以相应的特征值，耦合的计算分解成彼此独立的计算。本节说明何时可以做到这一点，并证明对称矩阵总能做到，而且所用的基甚至是标准正交基。
tags: 基变换, 可对角化, 主轴
lang: zh
---

<span class="anker" id="stufe-7"></span>

:::zweck
如果用矩阵自身的特征向量构成的基来描述矩阵，它就成为对角矩阵：每个坐标只被乘以相应的特征值，耦合的计算分解成彼此独立的计算。本节说明何时可以做到这一点，并证明对称矩阵总能做到，而且所用的基甚至是标准正交基。
:::

### 基变换

<span class="anker" id="stufe-7-1"></span>

同一个箭头在不同的基下有不同的坐标。同样，同一个线性映射在不同的坐标下有不同的矩阵。有些基能使矩阵变得特别简单。

设 $\mathbf s_1,\dots,\mathbf s_n$ 是 $\mathbb{R}^n$ 的一组基，$\mathbf{S}$ 是以这些向量为列的矩阵。由[第 1 章第 13.5 节](/wissen/zh/informatik/machine-learning/mathematische-grundlagen/vektoren-und-matrizen/unabhangigkeit-basis-und-rang.html#stufe-13-5)，它是可逆的。若 $\mathbf{x}$ 在这组基下的坐标为 $\mathbf{c}$，则 $\mathbf{x}=\sum_ic_i\mathbf s_i=\mathbf{S}\mathbf{c}$，反过来 $\mathbf{c}=\mathbf{S}^{-1}\mathbf{x}$。用 $\mathbf{A}$ 映射 $\mathbf{x}$，像 $\mathbf{A}\mathbf{x}$ 的坐标就是 $\mathbf{S}^{-1}\mathbf{A}\mathbf{x}=\mathbf{S}^{-1}\mathbf{A}\mathbf{S}\,\mathbf{c}$。因此在新坐标下，这个映射通过矩阵 $\mathbf{S}^{-1}\mathbf{A}\mathbf{S}$ 起作用：先换算到旧坐标，再作映射，最后换算回来。

:::definition 定义 7.1 (基变换)
<span class="anker" id="satz-7-1"></span>

若 $\mathbf{S}$ 可逆，则 $\mathbf{B}=\mathbf{S}^{-1}\mathbf{A}\mathbf{S}$ 称为 $\mathbf{A}$ 在以 $\mathbf{S}$ 的列构成的基下的矩阵。从 $\mathbf{A}$ 到 $\mathbf{B}$ 的过渡称为__基变换__。
:::

以这种方式联系起来的两个矩阵称为相似矩阵。它们描述的是同一个映射，只是所用的坐标不同。

:::satz 定理 7.2 (基变换不改变的量)
<span class="anker" id="satz-7-2"></span>

$\mathbf{A}$ 与 $\mathbf{S}^{-1}\mathbf{A}\mathbf{S}$ 有相同的特征多项式，因而有相同的特征值、相同的迹和相同的行列式。
:::

:::beweis 基变换
有 $\mathbf{S}^{-1}\mathbf{A}\mathbf{S}-\lambda\mathbf{I}=\mathbf{S}^{-1}(\mathbf{A}-\lambda\mathbf{I})\mathbf{S}$。由[第 1 章第 14.5 节](/wissen/zh/informatik/machine-learning/mathematische-grundlagen/vektoren-und-matrizen/die-determinante.html#stufe-14-5)的运算规则，它的行列式为 $\det\mathbf{S}^{-1}\cdot\det(\mathbf{A}-\lambda\mathbf{I})\cdot\det\mathbf{S}=\det(\mathbf{A}-\lambda\mathbf{I})$。由式 [(6.5)](eigenwerte-und-eigenvektoren.html#gl-6-5)，迹和行列式由特征值决定。
:::

::::beispiel [算例]
对于 $\mathbf{A}=\bigl(\begin{smallmatrix}4&1\\2&3\end{smallmatrix}\bigr)$ 和[第 1 章第 13.3 节](/wissen/zh/informatik/machine-learning/mathematische-grundlagen/vektoren-und-matrizen/unabhangigkeit-basis-und-rang.html#stufe-13-3)中的基 $(1,\,0)^{\top}$、$(1,\,1)^{\top}$，有 $\mathbf{S}=\bigl(\begin{smallmatrix}1&1\\0&1\end{smallmatrix}\bigr)$ 和 $\mathbf{S}^{-1}=\bigl(\begin{smallmatrix}1&-1\\0&1\end{smallmatrix}\bigr)$。于是

$$\mathbf{S}^{-1}\mathbf{A}\mathbf{S}=\begin{pmatrix}1&-1\\0&1\end{pmatrix}\begin{pmatrix}4&5\\2&5\end{pmatrix}=\begin{pmatrix}2&0\\2&5\end{pmatrix}.$$

迹仍为 $7$，行列式仍为 $10$，而特征值现在位于一个三角矩阵的对角线上：$2$ 和 $5$。
::::

⁠**简而言之：**在以 $\mathbf{S}$ 的列构成的基下，映射 $\mathbf{A}$ 的矩阵为 $\mathbf{S}^{-1}\mathbf{A}\mathbf{S}$；特征值、迹和行列式都保持不变。

### 对角化

<span class="anker" id="stufe-7-2"></span>

最简单的矩阵是对角矩阵：它把每个坐标乘以各自的数，而不把坐标混合起来。如果取特征向量作为基，每个基向量都只被乘以它的特征值。所以在这组基下，矩阵是对角矩阵。

:::satz 定理 7.3 (对角化)
<span class="anker" id="satz-7-3"></span>

若 $\mathbf{A}\in\mathbb{R}^{n\times n}$ 有属于特征值 $\lambda_1,\dots,\lambda_n$ 的 $n$ 个线性无关的特征向量 $\mathbf s_1,\dots,\mathbf s_n$，且 $\mathbf{S}$ 是以这些向量为列的矩阵，则

<span class="anker" id="gl-7-1"></span>
$$\mathbf{S}^{-1}\mathbf{A}\mathbf{S}=\boldsymbol{\Lambda}=\operatorname{diag}(\lambda_1,\dots,\lambda_n),\qquad\text{从而}\qquad \mathbf{A}=\mathbf{S}\boldsymbol{\Lambda}\mathbf{S}^{-1} . \tag{7.1}$$

反之：若 $\mathbf{A}$ 能写成这种形式，则 $\mathbf{S}$ 的列都是特征向量。
:::

:::beweis 对角化
由[第 1 章第 9.2 节](/wissen/zh/informatik/machine-learning/mathematische-grundlagen/vektoren-und-matrizen/das-matrixprodukt.html#stufe-9-2)，$\mathbf{A}\mathbf{S}$ 的第 $i$ 列是乘积 $\mathbf{A}\mathbf s_i=\lambda_i\mathbf s_i$，而 $\mathbf{S}\boldsymbol{\Lambda}$ 的第 $i$ 列同样是 $\lambda_i\mathbf s_i$。所以 $\mathbf{A}\mathbf{S}=\mathbf{S}\boldsymbol{\Lambda}$。$\mathbf{S}$ 的各列线性无关，所以 $\mathbf{S}$ 可逆，从左边乘以 $\mathbf{S}^{-1}$ 即得式 [(7.1)](#gl-7-1)。把同一个等式 $\mathbf{A}\mathbf{S}=\mathbf{S}\boldsymbol{\Lambda}$ 倒过来读，就得到逆命题。
:::

能写成这种形式的矩阵称为__可对角化__的。由第 [6.8](eigenwerte-und-eigenvektoren.html#stufe-6-8) 节的定理，例如当所有 $n$ 个特征值互不相同时，总是如此。剪切不可对角化，因为它缺少一个特征向量。旋转 $90^\circ$ 也不能用实数对角化，只能用复数对角化。不过两者都是可逆的：可逆与可对角化是两种不同的性质。

::::beispiel [算例]
对于特征向量为 $(1,\,1)^{\top}$ 和 $(1,\,-2)^{\top}$ 的 $\mathbf{A}=\bigl(\begin{smallmatrix}4&1\\2&3\end{smallmatrix}\bigr)$，

$$\mathbf{S}=\begin{pmatrix}1&1\\1&-2\end{pmatrix},\qquad \mathbf{S}^{-1}=\frac13\begin{pmatrix}2&1\\1&-1\end{pmatrix},\qquad \mathbf{S}^{-1}\mathbf{A}\mathbf{S}=\frac13\begin{pmatrix}2&1\\1&-1\end{pmatrix}\begin{pmatrix}5&2\\5&-4\end{pmatrix}=\begin{pmatrix}5&0\\0&2\end{pmatrix}.$$
::::

⁠**简而言之：**有 $n$ 个线性无关特征向量的矩阵，在这些特征向量构成的基下是对角矩阵：$\mathbf{A}=\mathbf{S}\boldsymbol{\Lambda}\mathbf{S}^{-1}$。

### 解耦：幂与序列

<span class="anker" id="stufe-7-3"></span>

这有什么用，可以从一个反复作用的矩阵看出来。A、B 两地每年交换居民：A 地 $20\,\%$ 的居民迁往 B 地，B 地 $30\,\%$ 的居民迁往 A 地，其余的人留在原地。若 $\mathbf{x}_k$ 包含第 $k$ 年的两地人口，则

$$\mathbf{x}_{k+1}=\mathbf M\mathbf{x}_k\qquad\text{其中}\qquad \mathbf M=\begin{pmatrix}0.8&0.3\\0.2&0.7\end{pmatrix}.$$

两地的人口是耦合的：每个新的数都取决于两个旧的数。$k$ 年后，$\mathbf{x}_k=\mathbf M^k\mathbf{x}_0$。直接计算幂 $\mathbf M^k$ 很繁琐，而且看不出长期会发生什么。在特征基下则很简单。

:::satz 定理 7.4 (特征基下的幂与序列)
<span class="anker" id="satz-7-4"></span>

若 $\mathbf{A}=\mathbf{S}\boldsymbol{\Lambda}\mathbf{S}^{-1}$，则 $\mathbf{A}^k=\mathbf{S}\boldsymbol{\Lambda}^k\mathbf{S}^{-1}$，其中 $\boldsymbol{\Lambda}^k=\operatorname{diag}(\lambda_1^k,\dots,\lambda_n^k)$。对于序列 $\mathbf{x}_{k+1}=\mathbf{A}\mathbf{x}_k$，有

<span class="anker" id="gl-7-2"></span>
$$\mathbf{x}_k=\sum_{i=1}^nc_i\,\lambda_i^k\,\mathbf s_i\qquad\text{其中}\qquad \mathbf{c}=\mathbf{S}^{-1}\mathbf{x}_0 . \tag{7.2}$$
:::

:::beweis 幂
$\mathbf{A}^2=\mathbf{S}\boldsymbol{\Lambda}\mathbf{S}^{-1}\mathbf{S}\boldsymbol{\Lambda}\mathbf{S}^{-1}=\mathbf{S}\boldsymbol{\Lambda}^2\mathbf{S}^{-1}$，因为中间的 $\mathbf{S}^{-1}\mathbf{S}=\mathbf{I}$ 消掉了；每个幂都同样如此。把 $\mathbf{x}_0=\sum_ic_i\mathbf s_i$ 分解为特征向量之和，$\mathbf{A}$ 的每次作用都只把每个部分乘以它的特征值。
:::

在特征基的坐标 $\mathbf{c}$ 下，每一步都是把每个坐标乘以它自己的数：$c_i\mapsto\lambda_ic_i$。一个含 $n$ 个未知数的耦合计算，变成了 $n$ 个各含一个未知数的独立计算。这些坐标是解耦的。长期来看，模最大的特征值所对应的部分占主导。

::::beispiel [算例]
$\mathbf M$ 的迹为 $1.5$，行列式为 $0.56-0.06=0.5$，因而特征值为 $1$ 和 $0.5$。属于特征值 $1$ 的特征向量是 $\mathbf s_1=(3,\,2)^{\top}$，因为 $\mathbf M\mathbf s_1=(2.4+0.6,\ 0.6+1.4)^{\top}=\mathbf s_1$；属于特征值 $0.5$ 的特征向量是 $\mathbf s_2=(1,\,-1)^{\top}$。若起初 A 地住着 $1000$ 人，B 地无人居住，则 $\mathbf{x}_0=(1000,\,0)^{\top}=200\,\mathbf s_1+400\,\mathbf s_2$，由式 [(7.2)](#gl-7-2)，

$$\mathbf{x}_k=200\begin{pmatrix}3\\2\end{pmatrix}+400\cdot0.5^k\begin{pmatrix}1\\-1\end{pmatrix}=\begin{pmatrix}600+400\cdot0.5^k\\400-400\cdot0.5^k\end{pmatrix}.$$

一年后两地人口为 $(800,\,200)^{\top}$，两年后为 $(700,\,300)^{\top}$，长期则稳定在 $(600,\,400)^{\top}$。属于特征值 $0.5$ 的部分每年减半，属于特征值 $1$ 的部分保持不变。
::::

⁠**简而言之：**在特征基下，矩阵的每个幂都变成特征值的幂；耦合的序列分解为彼此独立的序列，每个特征向量对应一个。

:::hintergrund 序列中的同一原理与傅里叶变换
像[第 1 章第 8.2 节](/wissen/zh/informatik/machine-learning/mathematische-grundlagen/vektoren-und-matrizen/lineare-abbildungen.html#stufe-8-2)中柴火炉那样的后效，会以固定的权重把序列的每个值混入随后的各个值。结果的每个值都取决于序列的多个值，一切都是耦合的。把序列分解为复振荡 $\mathrm e^{\mathrm j\omega n}$，每个复振荡都只被乘以它自己的一个数，耦合就消失了。傅里叶变换对序列和函数所做的，正是基变换 $\mathbf{S}^{-1}$ 对向量所做的：它换算到这些振荡的坐标。

对于循环往复的序列，这种对应甚至就是字面意义上的对角化。如果一个序列的最后一个值之后又接着第一个值，它就是循环往复的，就像一家昼夜不停运转、实行三班倒的企业的班次：夜班之后又是早班。循环的后效在数学中称为循环卷积，$y_k=\sum_lh_{(k-l)\bmod n}\,x_l$，它是一个矩阵。它的第一列是对第一个位置上单独一个 $1$ 的响应 $(h_0,\dots,h_{n-1})^{\top}$，其余各列是这一列的循环移位。它的特征向量是复振荡 $\mathbf f_m=\bigl(1,\ \mathrm e^{\mathrm j2\pi m/n},\ \mathrm e^{\mathrm j2\pi\cdot2m/n},\dots\bigr)^{\top}$，属于 $\mathbf f_m$ 的特征值是权重的离散傅里叶变换的值 $H[m]=\sum_qh_q\,\mathrm e^{-\mathrm j2\pi mq/n}$。所以，离散傅里叶变换的矩阵除了因子 $1/n$ 之外，就是使每个循环卷积对角化的那个 $\mathbf{S}^{-1}$，而且它同时适用于所有权重。以 $n=3$ 个班次、$h=(1,\,0.5,\,0)$ 为例：矩阵 $\Bigl(\begin{smallmatrix}1&0&0.5\\0.5&1&0\\0&0.5&1\end{smallmatrix}\Bigr)$ 把 $\mathbf f_0=(1,1,1)^{\top}$ 映射为 $1.5\,\mathbf f_0$，而 $1.5=H[0]=h_0+h_1+h_2$。
:::

### 对称矩阵的特征值是实数

<span class="anker" id="stufe-7-4"></span>

对称矩阵有许多特别简单之处。第一点：它们的特征值总是实数。所以对称矩阵不会像第 [6.6](eigenwerte-und-eigenvektoren.html#stufe-6-6) 节中的旋转那样，使某个平面在其自身内旋转。

:::satz 定理 7.5 (实特征值)
<span class="anker" id="satz-7-5"></span>

实对称矩阵的每个特征值都是实数。
:::

:::beweis 实特征值
设 $\mathbf{A}\mathbf{v}=\lambda\mathbf{v}$，$\mathbf{v}\ne\mathbf{0}$，其中 $\lambda$ 和 $\mathbf{v}$ 暂时允许是复数。对两边取共轭，$\mathbf{A}$ 保持不变，因为它是实矩阵：$\mathbf{A}\mathbf{v}^*=\lambda^*\mathbf{v}^*$。用两种方法计算数 $(\mathbf{v}^*)^{\top}\mathbf{A}\mathbf{v}$。一种利用 $\mathbf{A}\mathbf{v}=\lambda\mathbf{v}$：

$$(\mathbf{v}^*)^{\top}\mathbf{A}\mathbf{v}=\lambda\,(\mathbf{v}^*)^{\top}\mathbf{v} .$$

另一种利用 $\mathbf{A}=\mathbf{A}^{\top}$ 和 $\mathbf{A}\mathbf{v}^*=\lambda^*\mathbf{v}^*$：

$$(\mathbf{v}^*)^{\top}\mathbf{A}\mathbf{v}=(\mathbf{A}^{\top}\mathbf{v}^*)^{\top}\mathbf{v}=(\mathbf{A}\mathbf{v}^*)^{\top}\mathbf{v}=\lambda^*\,(\mathbf{v}^*)^{\top}\mathbf{v} .$$

所以 $(\lambda-\lambda^*)\,(\mathbf{v}^*)^{\top}\mathbf{v}=0$。由第 [6.1](eigenwerte-und-eigenvektoren.html#stufe-6-1) 节，$(\mathbf{v}^*)^{\top}\mathbf{v}=\sum_i|v_i|^2>0$，所以 $\lambda=\lambda^*$，$\lambda$ 是实数。
:::

于是对于实特征值，也存在实特征向量，因为 $(\mathbf{A}-\lambda\mathbf{I})\mathbf{v}=\mathbf{0}$ 是一个实方程组。

::::beispiel [算例]
$\bigl(\begin{smallmatrix}5&2\\2&2\end{smallmatrix}\bigr)$ 的特征多项式为 $\lambda^2-7\lambda+6$，判别式为 $49-24=25>0$，实特征值为 $6$ 和 $1$。对于任意对称 $2\times2$ 矩阵 $\bigl(\begin{smallmatrix}a&b\\b&c\end{smallmatrix}\bigr)$，判别式为 $(a+c)^2-4(ac-b^2)=(a-c)^2+4b^2\ge0$；所以正如定理所说，特征值总是实数。
::::

⁠**简而言之：**对称矩阵只有实特征值和实特征向量。

### 对称矩阵的特征向量互相垂直

<span class="anker" id="stufe-7-5"></span>

$\bigl(\begin{smallmatrix}4&1\\2&3\end{smallmatrix}\bigr)$ 的特征向量彼此斜交。对于对称矩阵，这种情况不会发生。

:::satz 定理 7.6 (正交的特征向量)
<span class="anker" id="satz-7-6"></span>

对称矩阵属于不同特征值的特征向量互相垂直。
:::

:::beweis 正交的特征向量
设 $\mathbf{A}\mathbf{v}_1=\lambda_1\mathbf{v}_1$，$\mathbf{A}\mathbf{v}_2=\lambda_2\mathbf{v}_2$，且 $\lambda_1\ne\lambda_2$。用两种方法计算 $\mathbf{v}_1^{\top}\mathbf{A}\mathbf{v}_2$：一是 $\mathbf{v}_1^{\top}(\lambda_2\mathbf{v}_2)=\lambda_2\,\mathbf{v}_1^{\top}\mathbf{v}_2$，二是利用 $\mathbf{A}^{\top}=\mathbf{A}$ 得到 $(\mathbf{A}\mathbf{v}_1)^{\top}\mathbf{v}_2=\lambda_1\,\mathbf{v}_1^{\top}\mathbf{v}_2$。所以 $(\lambda_1-\lambda_2)\,\mathbf{v}_1^{\top}\mathbf{v}_2=0$，由于 $\lambda_1\ne\lambda_2$，得 $\mathbf{v}_1^{\top}\mathbf{v}_2=0$。
:::

::::beispiel [算例]
$\bigl(\begin{smallmatrix}5&2\\2&2\end{smallmatrix}\bigr)$ 有属于特征值 $6$ 的特征向量 $(2,\,1)^{\top}$，因为 $(10+2,\ 4+2)^{\top}=6\,(2,\,1)^{\top}$；还有属于特征值 $1$ 的特征向量 $(1,\,-2)^{\top}$，因为 $(5-4,\ 2-4)^{\top}=(1,\,-2)^{\top}$。它们的点积为 $2-2=0$，见图 [19](#abb-19)。

:::abbildung ml/k2rsenkrecht 19
对称矩阵 $\bigl(\begin{smallmatrix}5&2\\2&2\end{smallmatrix}\bigr)$ 属于特征值 $6$ 的特征向量 $(2,1)^{\top}$ 与属于特征值 $1$ 的特征向量 $(1,-2)^{\top}$ 的点积：二者互相垂直。
:::
::::

⁠**简而言之：**对于对称矩阵，属于不同特征值的特征向量互相垂直。

:::hintergrund 为什么恰恰是对称性使特征方向互相垂直
证明只在一处用到了对称性：$(\mathbf{A}\mathbf{v}_1)^{\top}\mathbf{v}_2=\mathbf{v}_1^{\top}(\mathbf{A}\mathbf{v}_2)$。对于对称矩阵，这个等式对所有向量都成立；在点积中可以把 $\mathbf{A}$ 从一侧移到另一侧。点积衡量 $\mathbf{v}_2$ 中有多少指向 $\mathbf{v}_1$ 的方向。若 $\mathbf{A}$ 把一个方向拉伸 $\lambda_1$ 倍，把另一个方向拉伸 $\lambda_2$ 倍，那么这个分量在左边被乘以 $\lambda_1$，在右边被乘以 $\lambda_2$。只有当没有东西可乘，也就是这个分量为零时，两边才可能相等。对于非对称矩阵，这条移动规则不成立，特征方向可以是斜交的。

由此还得出第二个重要性质。若 $\mathbf{q}$ 是特征向量，且 $\mathbf{z}$ 垂直于 $\mathbf{q}$，则 $\mathbf{A}\mathbf{z}$ 也垂直于 $\mathbf{q}$：$(\mathbf{A}\mathbf{z})^{\top}\mathbf{q}=\mathbf{z}^{\top}\mathbf{A}\mathbf{q}=\lambda\,\mathbf{z}^{\top}\mathbf{q}=0$。所以对称矩阵把一个特征向量的正交补映射到它自身之中。可以在那里寻找下一个特征向量，依此类推。下一小节的证明正是这样进行的。
:::

### 谱定理

<span class="anker" id="stufe-7-6"></span>

前面两个定理使人猜想：每个对称矩阵在一组由特征向量构成的标准正交基下都是对角矩阵。即使有重特征值，这一点也成立。一个矩阵的特征值的集合称为它的谱，定理的名称即由此而来。

:::satz 定理 7.7 (谱定理)
<span class="anker" id="satz-7-7"></span>

对每个对称矩阵 $\mathbf{A}\in\mathbb{R}^{n\times n}$，都存在一组由特征向量构成的标准正交基 $\mathbf{q}_1,\dots,\mathbf{q}_n$，相应的特征值 $\lambda_1,\dots,\lambda_n$ 都是实数。利用正交矩阵 $\mathbf{Q}=\begin{pmatrix}\mathbf{q}_1&\cdots&\mathbf{q}_n\end{pmatrix}$ 和 $\boldsymbol{\Lambda}=\operatorname{diag}(\lambda_1,\dots,\lambda_n)$，有

<span class="anker" id="gl-7-3"></span>
$$\mathbf{A}=\mathbf{Q}\boldsymbol{\Lambda}\mathbf{Q}^{\top}=\sum_{i=1}^n\lambda_i\,\mathbf{q}_i\mathbf{q}_i^{\top} . \tag{7.3}$$
:::

:::beweis 谱定理
逐步进行。由第 [6.3](eigenwerte-und-eigenvektoren.html#stufe-6-3) 节，$\mathbf{A}$ 至少有一个特征值 $\lambda_1$；由第 [7.4](#stufe-7-4) 节，它是实数，并且有一个实特征向量，归一化后记为 $\mathbf{q}_1$。把 $\mathbf{q}_1$ 扩充为 $\mathbb{R}^n$ 的一组标准正交基，例如对 $\mathbf{q}_1,\mathbf{e}_1,\dots,\mathbf{e}_n$ 进行格拉姆-施密特正交化，并跳过出现 $\tilde{\mathbf{q}}=\mathbf{0}$ 的向量。其余的基向量构成矩阵 $\mathbf{W}\in\mathbb{R}^{n\times(n-1)}$ 的列，$\mathbf{Q}_1=\begin{pmatrix}\mathbf{q}_1&\mathbf{W}\end{pmatrix}$ 是正交矩阵。于是

$$\mathbf{Q}_1^{\top}\mathbf{A}\mathbf{Q}_1=\begin{pmatrix}\mathbf{q}_1^{\top}\mathbf{A}\mathbf{q}_1&\mathbf{q}_1^{\top}\mathbf{A}\mathbf{W}\\\mathbf{W}^{\top}\mathbf{A}\mathbf{q}_1&\mathbf{W}^{\top}\mathbf{A}\mathbf{W}\end{pmatrix}=\begin{pmatrix}\lambda_1&\mathbf{0}^{\top}\\\mathbf{0}&\mathbf{B}\end{pmatrix}$$

其中 $\mathbf{B}=\mathbf{W}^{\top}\mathbf{A}\mathbf{W}$ 是对称的 $(n-1)\times(n-1)$ 矩阵。左下角出现零，是因为 $\mathbf{A}\mathbf{q}_1=\lambda_1\mathbf{q}_1$ 垂直于 $\mathbf{W}$ 的各列；右上角的零同样如此，因为 $\mathbf{A}$ 是对称的。对 $\mathbf{B}$ 重复同样的步骤，直到剩下一个 $1\times1$ 矩阵。这样为 $\mathbf{B}$ 找到一个正交矩阵 $\mathbf{Q}_B$，使 $\mathbf{Q}_B^{\top}\mathbf{B}\mathbf{Q}_B$ 成为对角矩阵之后，$\mathbf{Q}=\mathbf{Q}_1\bigl(\begin{smallmatrix}1&\mathbf{0}^{\top}\\\mathbf{0}&\mathbf{Q}_B\end{smallmatrix}\bigr)$ 作为正交矩阵之积是正交矩阵，并且 $\mathbf{Q}^{\top}\mathbf{A}\mathbf{Q}=\bigl(\begin{smallmatrix}\lambda_1&\mathbf{0}^{\top}\\\mathbf{0}&\mathbf{Q}_B^{\top}\mathbf{B}\mathbf{Q}_B\end{smallmatrix}\bigr)=\boldsymbol{\Lambda}$ 是对角矩阵。因为 $\mathbf{Q}^{-1}=\mathbf{Q}^{\top}$，得 $\mathbf{A}=\mathbf{Q}\boldsymbol{\Lambda}\mathbf{Q}^{\top}$。求和形式由[第 1 章第 9.5 节](/wissen/zh/informatik/machine-learning/mathematische-grundlagen/vektoren-und-matrizen/das-matrixprodukt.html#stufe-9-5)得出，因为 $\mathbf{Q}\boldsymbol{\Lambda}$ 的列为 $\lambda_i\mathbf{q}_i$。
:::

由第 [2.3](projektion-auf-eine-gerade.html#stufe-2-3) 节，每一项 $\mathbf{q}_i\mathbf{q}_i^{\top}$ 都是向沿 $\mathbf{q}_i$ 方向的直线的投影。所以对称矩阵是向互相垂直的坐标轴的投影之和，每个投影以相应的特征值为权重。对于重特征值，$\mathbf{q}_i$ 在其特征空间中的选择是自由的：特征空间的任何一组标准正交基都可以。每个 $\mathbf{q}_i$ 的符号也是自由的。有些书把特征值按降序排列，有些则不然。

::::beispiel [算例]
对于 $\mathbf{A}=\bigl(\begin{smallmatrix}5&2\\2&2\end{smallmatrix}\bigr)$，$\mathbf{q}_1=(2,\,1)^{\top}/\sqrt5$ 和 $\mathbf{q}_2=(1,\,-2)^{\top}/\sqrt5$ 是属于 $6$ 和 $1$ 的归一化特征向量。于是

$$6\cdot\frac15\begin{pmatrix}4&2\\2&1\end{pmatrix}+1\cdot\frac15\begin{pmatrix}1&-2\\-2&4\end{pmatrix}=\frac15\begin{pmatrix}25&10\\10&10\end{pmatrix}=\begin{pmatrix}5&2\\2&2\end{pmatrix}.$$
::::

⁠**简而言之：**每个对称矩阵都是 $\mathbf{Q}\boldsymbol{\Lambda}\mathbf{Q}^{\top}$：它在一个适当旋转的坐标系中是对角矩阵，也是向互相垂直的坐标轴的投影的加权和。

:::hintergrund 对称矩阵从何而来
凡是矩阵描述与顺序无关的两两关系的地方，都会出现对称矩阵。[第 1 章第 10 节](/wissen/zh/informatik/machine-learning/mathematische-grundlagen/vektoren-und-matrizen/transponierte-symmetrie-und-gram-matrix.html#stufe-10)中的格拉姆矩阵 $\mathbf{X}^{\top}\mathbf{X}$ 和 $\mathbf{X}\mathbf{X}^{\top}$ 包含点积，而 $\mathbf{u}^{\top}\mathbf{v}=\mathbf{v}^{\top}\mathbf{u}$。由第 [5.2](quadratische-formen.html#stufe-5-2) 节，二次型的矩阵总可以选为对称的。按直线距离测量的城市间距离表是对称的，因为从 A 到 B 的距离与从 B 到 A 的相同。对所有这些矩阵，谱定理都保证特征值为实数、特征方向互相垂直。
:::

### 主轴

<span class="anker" id="stufe-7-7"></span>

在第 [5.3](quadratische-formen.html#stufe-5-3) 节中，只要二次型的矩阵是对角矩阵，就很容易看出它的形状。如果把坐标适当地旋转，谱定理能使每个对称矩阵都成为对角矩阵。这样交叉项就消失了。

:::satz 定理 7.8 (二次型的主轴)
<span class="anker" id="satz-7-8"></span>

若 $\mathbf{A}=\mathbf{Q}\boldsymbol{\Lambda}\mathbf{Q}^{\top}$，且 $c_i=\mathbf{q}_i^{\top}\mathbf{x}$ 是 $\mathbf{x}$ 在特征基下的坐标，则

<span class="anker" id="gl-7-4"></span>
$$\mathbf{x}^{\top}\mathbf{A}\mathbf{x}=\lambda_1c_1^2+\lambda_2c_2^2+\dots+\lambda_nc_n^2 . \tag{7.4}$$
:::

:::beweis 主轴
令 $\mathbf{c}=\mathbf{Q}^{\top}\mathbf{x}$，得 $\mathbf{x}^{\top}\mathbf{A}\mathbf{x}=\mathbf{x}^{\top}\mathbf{Q}\boldsymbol{\Lambda}\mathbf{Q}^{\top}\mathbf{x}=\mathbf{c}^{\top}\boldsymbol{\Lambda}\mathbf{c}=\sum_i\lambda_ic_i^2$。
:::

因此，特征向量的方向称为二次型的__主轴__。若所有特征值都为正，等高线 $\mathbf{x}^{\top}\mathbf{A}\mathbf{x}=1$ 是一个椭圆，在 $\mathbb{R}^3$ 中则是一个椭球面。它的轴位于 $\mathbf{q}_i$ 的方向上，沿 $\mathbf{q}_i$ 方向的半轴长度为 $1/\sqrt{\lambda_i}$，因为对于 $\mathbf{x}=t\,\mathbf{q}_i$，恰好在 $t=\pm1/\sqrt{\lambda_i}$ 时有 $\mathbf{x}^{\top}\mathbf{A}\mathbf{x}=\lambda_it^2=1$。大的特征值对应陡峭的方向和短的半轴。

:::abbildung ml/k2ellipse 20
等高线 $5x_1^2+4x_1x_2+2x_2^2=1$（蓝色）和 $=\tfrac14$（浅蓝色）都是椭圆。它们的轴（灰色）位于特征向量 $\mathbf{q}_1=(2,1)^{\top}/\sqrt5$（属于特征值 $6$）和 $\mathbf{q}_2=(1,-2)^{\top}/\sqrt5$（属于特征值 $1$）的方向上。外侧椭圆的半轴为 $1/\sqrt6\approx0.41$（红色）和 $1/\sqrt1=1$（绿色）：在大特征值的方向上，二次型上升得最陡，椭圆在那里也最窄。
:::

::::beispiel [算例]
对于 $f(\mathbf{x})=5x_1^2+4x_1x_2+2x_2^2$，特征基下的坐标为 $c_1=(2x_1+x_2)/\sqrt5$ 和 $c_2=(x_1-2x_2)/\sqrt5$，并且

$$5x_1^2+4x_1x_2+2x_2^2=6\,c_1^2+c_2^2=\tfrac65(2x_1+x_2)^2+\tfrac15(x_1-2x_2)^2 .$$

右边展开后得 $\tfrac15\bigl(24x_1^2+24x_1x_2+6x_2^2+x_1^2-4x_1x_2+4x_2^2\bigr)=5x_1^2+4x_1x_2+2x_2^2$。等高线 $f=1$ 就是图 [20](#abb-20) 中的椭圆，半轴为 $1/\sqrt6\approx0.408$ 和 $1$。
::::

⁠**简而言之：**在特征基下，每个二次型都成为不含交叉项的和 $\sum_i\lambda_ic_i^2$；特征向量是其椭圆的主轴，半轴为 $1/\sqrt{\lambda_i}$。

:::hintergrund 两种配方方式
在第 [5.4](quadratische-formen.html#stufe-5-4) 节中，同一个二次型也可以写成 $5(x_1+0.4x_2)^2+1.2x_2^2$。那里的系数 $5$ 和 $1.2$ 与这里的特征值 $6$ 和 $1$ 是不同的数。两种分解都正确，但新坐标不同：在配方中，$x_1+0.4x_2$ 和 $x_2$ 是斜坐标；在谱定理中，$c_1,c_2$ 是一个旋转后的直角坐标系中的坐标。只有第二种分解显示出椭圆的轴。两者的共同之处在别处：正系数、负系数和零系数的个数相同。这对把二次型分解为若干独立坐标的平方和的任何分解都成立；这个定理称为西尔维斯特惯性定律。正因为如此，配方和特征值对碗形、槽形还是鞍形总是给出相同的判断。
:::

:::aufgabe 练习 21 ★ 对角化
<span class="anker" id="aufg-21"></span>

设 $\mathbf{A}=\bigl(\begin{smallmatrix}2&2\\1&3\end{smallmatrix}\bigr)$ 是练习 [17](eigenwerte-und-eigenvektoren.html#aufg-17) 中的矩阵。

<ol class="al">

<li>

给出满足 $\mathbf{A}=\mathbf{S}\boldsymbol{\Lambda}\mathbf{S}^{-1}$ 的 $\mathbf{S}$ 和 $\boldsymbol{\Lambda}$，并验证该等式。

</li>

<li>

分别直接计算和按 $\mathbf{S}\boldsymbol{\Lambda}^3\mathbf{S}^{-1}$ 计算 $\mathbf{A}^3$。

</li>

</ol>

:::loesung
(a) 由练习 [17](eigenwerte-und-eigenvektoren.html#aufg-17)：特征值为 $4$ 和 $1$，特征向量为 $(1,\,1)^{\top}$ 和 $(2,\,-1)^{\top}$。所以

$$\mathbf{S}=\begin{pmatrix}1&2\\1&-1\end{pmatrix},\qquad \boldsymbol{\Lambda}=\begin{pmatrix}4&0\\0&1\end{pmatrix},\qquad \mathbf{S}^{-1}=\frac13\begin{pmatrix}1&2\\1&-1\end{pmatrix},$$

因为 $\det\mathbf{S}=-3$。验算：$\mathbf{S}\boldsymbol{\Lambda}\mathbf{S}^{-1}=\bigl(\begin{smallmatrix}4&2\\4&-1\end{smallmatrix}\bigr)\cdot\tfrac13\bigl(\begin{smallmatrix}1&2\\1&-1\end{smallmatrix}\bigr)=\tfrac13\bigl(\begin{smallmatrix}6&6\\3&9\end{smallmatrix}\bigr)=\bigl(\begin{smallmatrix}2&2\\1&3\end{smallmatrix}\bigr)$。

(b) 直接计算：$\mathbf{A}^2=\bigl(\begin{smallmatrix}6&10\\5&11\end{smallmatrix}\bigr)$，$\mathbf{A}^3=\mathbf{A}^2\mathbf{A}=\bigl(\begin{smallmatrix}12+10&12+30\\10+11&10+33\end{smallmatrix}\bigr)=\bigl(\begin{smallmatrix}22&42\\21&43\end{smallmatrix}\bigr)$。经由特征基：$\boldsymbol{\Lambda}^3=\operatorname{diag}(64,\,1)$，$\mathbf{S}\boldsymbol{\Lambda}^3=\bigl(\begin{smallmatrix}64&2\\64&-1\end{smallmatrix}\bigr)$，且

$$\mathbf{S}\boldsymbol{\Lambda}^3\mathbf{S}^{-1}=\frac13\begin{pmatrix}64+2&128-2\\64-1&128+1\end{pmatrix}=\begin{pmatrix}22&42\\21&43\end{pmatrix}.$$

对于高次幂，第二种途径要短得多：只需对特征值求幂。
:::
:::

:::aufgabe 练习 22 ★★ 解耦一个序列
<span class="anker" id="aufg-22"></span>

斐波那契数 $0,1,1,2,3,5,\dots$ 满足 $F_{k+2}=F_{k+1}+F_k$。令 $\mathbf{x}_k=(F_{k+1},\,F_k)^{\top}$，则 $\mathbf{x}_{k+1}=\bigl(\begin{smallmatrix}1&1\\1&0\end{smallmatrix}\bigr)\mathbf{x}_k$。

<ol class="al">

<li>

求该矩阵的特征值和特征向量。

</li>

<li>

用式 [(7.2)](#gl-7-2) 推导 $F_k$ 的公式，并对 $k=5$ 加以验证。

</li>

<li>

当 $k$ 很大时，$F_{k+1}/F_k$ 表现如何？为什么？

</li>

</ol>

:::loesung
(a) $p(\lambda)=\lambda^2-\lambda-1$，根为 $\varphi=\tfrac{1+\sqrt5}2\approx1.618$ 和 $\psi=\tfrac{1-\sqrt5}2\approx-0.618$。$(\mathbf{A}-\lambda\mathbf{I})\mathbf{v}=\mathbf{0}$ 的第一行为 $(1-\lambda)v_1+v_2=0$；由于 $p(\lambda)=0$，第二行 $v_1-\lambda v_2=0$ 与第一行等价。特征向量为 $\mathbf s_1=(\varphi,\,1)^{\top}$ 和 $\mathbf s_2=(\psi,\,1)^{\top}$。

(b) $\mathbf{x}_0=(F_1,\,F_0)^{\top}=(1,\,0)^{\top}=c_1\mathbf s_1+c_2\mathbf s_2$ 要求 $c_1+c_2=0$ 且 $c_1\varphi+c_2\psi=1$，所以 $c_1=1/(\varphi-\psi)=1/\sqrt5$，$c_2=-1/\sqrt5$。由式 [(7.2)](#gl-7-2)，$\mathbf{x}_k=\tfrac1{\sqrt5}(\varphi^k\mathbf s_1-\psi^k\mathbf s_2)$；它的第二个分量为

$$F_k=\frac{\varphi^k-\psi^k}{\sqrt5} .$$

对于 $k=5$：$\varphi^5=\tfrac{11+5\sqrt5}2$，$\psi^5=\tfrac{11-5\sqrt5}2$，所以 $F_5=\tfrac{5\sqrt5}{\sqrt5}=5$。数值上：$\varphi^5\approx11.090$，$\psi^5\approx-0.090$，$(11.090+0.090)/2.236\approx5.000$。

(c) 由于 $|\psi|<1$，$\psi^k$ 趋于零，$F_{k+1}/F_k$ 趋于 $\varphi\approx1.618$，即黄金比。与第 [7.3](#stufe-7-3) 节一样，模最大的特征值所对应的部分占主导；每多走一步，它就乘以 $\varphi$。
:::
:::

:::aufgabe 练习 23 ★★ 谱分解
<span class="anker" id="aufg-23"></span>

<ol class="al">

<li>

把 $\mathbf{A}=\bigl(\begin{smallmatrix}3&4\\4&-3\end{smallmatrix}\bigr)$ 写成 $\mathbf{Q}\boldsymbol{\Lambda}\mathbf{Q}^{\top}$ 的形式，以及和 $\lambda_1\mathbf{q}_1\mathbf{q}_1^{\top}+\lambda_2\mathbf{q}_2\mathbf{q}_2^{\top}$ 的形式。

</li>

<li>

求二次型 $3x_1^2+8x_1x_2-3x_2^2$ 的主轴，并把它写成 $\lambda_1c_1^2+\lambda_2c_2^2$。它是第 [5.3](quadratische-formen.html#stufe-5-3) 节中的哪种基本形状？

</li>

<li>

矩阵 $\Bigl(\begin{smallmatrix}2&0&0\\0&3&1\\0&1&3\end{smallmatrix}\Bigr)$ 有二重特征值 $2$。给出一组由特征向量构成的标准正交基。它是唯一的吗？

</li>

</ol>

:::loesung
(a) 迹为 $0$，行列式为 $-9-16=-25$，所以 $\lambda^2-25=0$，$\lambda=\pm5$。对于 $5$：$\bigl(\begin{smallmatrix}-2&4\\4&-8\end{smallmatrix}\bigr)$，$\mathbf{q}_1=(2,\,1)^{\top}/\sqrt5$。对于 $-5$：$\bigl(\begin{smallmatrix}8&4\\4&2\end{smallmatrix}\bigr)$，$\mathbf{q}_2=(1,\,-2)^{\top}/\sqrt5$。取 $\mathbf{Q}=\tfrac1{\sqrt5}\bigl(\begin{smallmatrix}2&1\\1&-2\end{smallmatrix}\bigr)$ 和 $\boldsymbol{\Lambda}=\operatorname{diag}(5,\,-5)$，有 $\mathbf{A}=\mathbf{Q}\boldsymbol{\Lambda}\mathbf{Q}^{\top}$，并且

$$5\cdot\frac15\begin{pmatrix}4&2\\2&1\end{pmatrix}-5\cdot\frac15\begin{pmatrix}1&-2\\-2&4\end{pmatrix}=\begin{pmatrix}3&4\\4&-3\end{pmatrix}.$$

(b) 这个二次型的矩阵正是该矩阵。令 $c_1=(2x_1+x_2)/\sqrt5$，$c_2=(x_1-2x_2)/\sqrt5$，则

$$3x_1^2+8x_1x_2-3x_2^2=5c_1^2-5c_2^2=(2x_1+x_2)^2-(x_1-2x_2)^2 ,$$

展开即为 $4x_1^2+4x_1x_2+x_2^2-x_1^2+4x_1x_2-4x_2^2$。主轴沿 $(2,\,1)^{\top}$ 和 $(1,\,-2)^{\top}$ 方向。一个特征值为正，一个为负：这是一个鞍形，它的轴相对于坐标轴旋转了一个角度。

(c) $\mathbf{e}_1$ 是属于 $2$ 的特征向量。右下角的块 $\bigl(\begin{smallmatrix}3&1\\1&3\end{smallmatrix}\bigr)$ 的特征值为 $4$（特征向量 $(1,\,1)^{\top}$）和 $2$（特征向量 $(1,\,-1)^{\top}$）。因此，由特征向量构成的一组标准正交基为

$$\mathbf{e}_1,\qquad \tfrac1{\sqrt2}(0,\,1,\,-1)^{\top}\quad\text{属于特征值 }2,\qquad \tfrac1{\sqrt2}(0,\,1,\,1)^{\top}\quad\text{属于特征值 }4 .$$

它不是唯一的。属于 $2$ 的特征空间是由 $\mathbf{e}_1$ 和 $(0,\,1,\,-1)^{\top}$ 张成的平面，这个平面的任何一组标准正交基都可以，例如 $\tfrac1{\sqrt2}\bigl(\mathbf{e}_1+\tfrac1{\sqrt2}(0,1,-1)^{\top}\bigr)$ 和 $\tfrac1{\sqrt2}\bigl(\mathbf{e}_1-\tfrac1{\sqrt2}(0,1,-1)^{\top}\bigr)$。只有属于单重特征值 $4$ 的特征向量是唯一的（不计符号）。
:::
:::
