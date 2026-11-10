---
title: 线性映射
pfad: 计算机科学 / 机器学习 / 数学基础 / 向量与矩阵
adresse: informatik/machine-learning/mathematische-grundlagen/vektoren-und-matrizen
knoten: 第 1 章：向量与矩阵
nachschlagen: ja
order: 15210900
summary: 矩阵不只是一张表格，也是一条把一个向量变成另一个向量的计算规则。本节说明哪些规则可以这样写出来，即恰好是线性的规则，以及矩阵在几何上对空间做了什么。
tags: 映射, 线性的, 旋转, 拉伸, 剪切, 仿射, 截距
lang: zh
---

<span class="anker" id="stufe-8"></span>

:::zweck
矩阵不只是一张表格，也是一条把一个向量变成另一个向量的计算规则。本节说明哪些规则可以这样写出来，即恰好是线性的规则，以及矩阵在几何上对空间做了什么。
:::

### 线性映射

<span class="anker" id="stufe-8-1"></span>

许多计算把一个数字列表变成另一个列表。由公寓的特征估算出购买价格和租金；由水表的读数计算出每个月的用水量。这样的规则称为__映射__ $f\colon\mathbb{R}^n\to\mathbb{R}^m$：它给每个向量 $\mathbf{x}\in\mathbb{R}^n$ 指定一个向量 $f(\mathbf{x})\in\mathbb{R}^m$。

矩阵-向量乘积有两条特殊性质（第 [7.1](das-matrix-vektor-produkt.html#stufe-7-1) 小节）：$\mathbf{A}(\mathbf{u}+\mathbf{v})=\mathbf{A}\mathbf{u}+\mathbf{A}\mathbf{v}$ 和 $\mathbf{A}(c\,\mathbf{x})=c\,\mathbf{A}\mathbf{x}$。先相加还是先映射，结果都一样；先取倍数还是先映射，同样如此。在平面上，这两条性质可以从网格上看出来：这样的映射把直线变成直线或单个的点，使原点保持不动，并把平行且等距的网格线变成平行且等距的直线或点。

:::definition 定义 8.1 (线性映射)
<span class="anker" id="satz-8-1"></span>

如果对所有 $\mathbf{u},\mathbf{v}\in\mathbb{R}^n$ 和所有标量 $c$ 都有下式成立，就称映射 $f\colon\mathbb{R}^n\to\mathbb{R}^m$ 是__线性的__：

<span class="anker" id="gl-8-1"></span>
$$f(\mathbf{u}+\mathbf{v})=f(\mathbf{u})+f(\mathbf{v})\qquad\text{且}\qquad f(c\,\mathbf{u})=c\,f(\mathbf{u}) . \tag{8.1}$$
:::

两个条件合起来是说：$f$ 保持线性组合，$f(c_1\mathbf{u}+c_2\mathbf{v})=c_1f(\mathbf{u})+c_2f(\mathbf{v})$。每个线性映射都把零向量映射为零向量，因为 $f(\mathbf{0})=f(0\cdot\mathbf{u})=0\cdot f(\mathbf{u})=\mathbf{0}$。

::::beispiel [算例]
从 $\mathbb{R}^2$ 到 $\mathbb{R}^2$ 的映射 $f(\mathbf{x})=(x_1+x_2,\ 2x_1)^{\top}$ 是线性的。它的两个分量都是 $x_j$ 的倍数之和，而这样的和满足式 [(8.1)](#gl-8-1) 中的条件；例如 $f(\mathbf{u}+\mathbf{v})=(u_1+v_1+u_2+v_2,\ 2u_1+2v_1)^{\top}=f(\mathbf{u})+f(\mathbf{v})$。映射 $g(\mathbf{x})=x_1x_2$ 不是线性的，因为只要 $x_1x_2\ne0$，就有 $g(2\mathbf{x})=4x_1x_2\ne2\,g(\mathbf{x})$。$h(\mathbf{x})=\mathbf{x}+\mathbf 1$ 也不是线性的，因为 $h(\mathbf{0})=\mathbf 1\ne\mathbf{0}$。
::::

⁠**简而言之：**如果一个映射保持和与倍数，它就是线性的；这时它把线性组合映射为线性组合。

:::hintergrund 超市收银台的线性
超市收银台的计算是线性的。它把所购商品数量的列表变成应付金额；把两次购物合在一起放上传送带，费用就是两个金额之和；每样东西都买双倍，费用也是双倍。这恰好就是式 [(8.1)](#gl-8-1) 中的条件。带批量折扣的计价方式就不是线性的，买双倍花的钱比双倍价格少；含固定基本费的计价方式也不是：在那里，空的购物也要花钱，这违反了 $f(\mathbf{0})=\mathbf{0}$。录音（第 [1.3](vektoren-daten-als-zahlenlisten.html#stufe-1-3) 小节）也常常被线性地处理：先把两段录音混合再调轻，与先把每段分别调轻再混合，得到的结果相同。
:::

### 每个线性映射都是一个矩阵

<span class="anker" id="stufe-8-2"></span>

每个矩阵都给出一个线性映射 $\mathbf{x}\mapsto\mathbf{A}\mathbf{x}$。反过来也成立吗？成立，而且原因很简单：每个向量都是单位向量的线性组合，而线性映射保持线性组合。所以，只要知道 $n$ 个单位向量被映射到哪里，就知道每个向量被映射到哪里。

:::satz 定理 8.2 (线性映射的矩阵)
<span class="anker" id="satz-8-2"></span>

对每个线性映射 $f\colon\mathbb{R}^n\to\mathbb{R}^m$，恰有一个矩阵 $\mathbf{A}\in\mathbb{R}^{m\times n}$，使得对所有 $\mathbf{x}\in\mathbb{R}^n$ 都有 $f(\mathbf{x})=\mathbf{A}\mathbf{x}$。它的各列是单位向量的像：

<span class="anker" id="gl-8-2"></span>
$$\mathbf{a}_j=f(\mathbf{e}_j),\qquad j=1,\dots,n . \tag{8.2}$$
:::

:::beweis 线性映射的矩阵
由式 [(1.6)](vektoren-daten-als-zahlenlisten.html#gl-1-6)，$\mathbf{x}=\sum_jx_j\mathbf{e}_j$。因为 $f$ 是线性的，得到

$$f(\mathbf{x})=f\Bigl(\sum_{j=1}^nx_j\mathbf{e}_j\Bigr)=\sum_{j=1}^nx_j\,f(\mathbf{e}_j)=\sum_{j=1}^nx_j\,\mathbf{a}_j=\mathbf{A}\mathbf{x} ,$$

最后一步依据的是列视角，即式 [(7.3)](das-matrix-vektor-produkt.html#gl-7-3)。如果还有第二个矩阵 $\mathbf{B}$，对所有 $\mathbf{x}$ 都有 $\mathbf{B}\mathbf{x}=f(\mathbf{x})$，那么取 $\mathbf{x}=\mathbf{e}_j$，$\mathbf{B}$ 的第 $j$ 列就等于 $f(\mathbf{e}_j)=\mathbf{a}_j$，对每个 $j$ 都是如此。因此 $\mathbf{B}=\mathbf{A}$。
:::

::::beispiel [算例]
对 $f(\mathbf{x})=(x_1+x_2,\ 2x_1)^{\top}$，有 $f(\mathbf{e}_1)=(1,\,2)^{\top}$ 和 $f(\mathbf{e}_2)=(1,\,0)^{\top}$。所以

$$\mathbf{A}=\begin{pmatrix}1&1\\2&0\end{pmatrix},\qquad\text{验算：}\qquad \mathbf{A}\begin{pmatrix}3\\-1\end{pmatrix}=\begin{pmatrix}2\\6\end{pmatrix}=f\bigl((3,\,-1)^{\top}\bigr).$$
::::

⁠**简而言之：**线性映射与矩阵是一回事；矩阵的第 $j$ 列是单位向量 $\mathbf{e}_j$ 的像。

:::hintergrund 作为矩阵的后效：各列是移位后的响应
在柴火炉中，一块木柴在燃烧的那一小时里放出全部热量，在之后的一小时里通过余烬还放出一半；这是一个大大简化的图景。如果在第 $n$ 小时恰好添加 $x[n]$ 块木柴，那么这一小时的热量（以木柴块数计）为 $y[n]=x[n]+0.5\,x[n-1]$。考虑三个小时，第一个小时之前炉中什么也没有燃烧。这个计算是线性的，所以它有一个矩阵。由式 [(8.2)](#gl-8-2)，矩阵的第 $j$ 列是对单位向量 $\mathbf{e}_j$ 的响应，即对第 $j$ 小时单独一块木柴的响应。这个响应是 $(1,\,0.5)$，移动了 $j-1$ 小时：

$$\mathbf{A}=\begin{pmatrix}1&0&0\\0.5&1&0\\0&0.5&1\end{pmatrix}.$$

第三列只含 $1$，因为考察在三个小时之后就结束了。对 $\mathbf{x}=(2,\,4,\,6)^{\top}$，矩阵给出 $(2,\,5,\,8)^{\top}$，与公式的结果相同。这样，每个这种带固定权重的后效（在数学中称为卷积）都是一个矩阵-向量乘积，而上面的定理解释了原因：知道了对每一块单独木柴的响应，就知道了对任何一串木柴的响应。
:::

:::hintergrund 数据还是映射？同一张表格的两种角色
矩阵可以是数据的集合，如数据矩阵 $\mathbf{X}$；也可以是映射，如前一个方框中柴火炉的矩阵。形式上两者是一样的，有时同一个矩阵甚至同时扮演两种角色：数据矩阵也是把权重变成预测值的映射 $\mathbf{w}\mapsto\mathbf{X}\mathbf{w}$。它把权重所在的 $\mathbb{R}^d$ 映射到预测值列表所在的 $\mathbb{R}^N$ 中。所以阅读公式时，值得问一问：一个矩阵是以哪种角色出现的。
:::

### 平面上的线性映射

<span class="anker" id="stufe-8-3"></span>

在平面上，可以看出矩阵做了什么。画出顶点为 $\mathbf{0}$、$\mathbf{e}_1$、$\mathbf{e}_1+\mathbf{e}_2$ 和 $\mathbf{e}_2$ 的单位正方形及其像。因为映射保持线性组合，正方形变成顶点为 $\mathbf{0}$、$\mathbf{a}_1$、$\mathbf{a}_1+\mathbf{a}_2$ 和 $\mathbf{a}_2$ 的平行四边形。它在原点处的两条边就是矩阵的两列（图 [32](#abb-32)）。平面的整个网格都以同样的方式变形：每个小格都变成这个平行四边形的一个平移副本。

:::abbildung ml/k1ebene 32
平面上的四个线性映射。灰色虚线：单位正方形；蓝色：它的像。红色箭头是 $\mathbf{e}_1$ 的像 $\mathbf{a}_1$，绿色箭头是 $\mathbf{e}_2$ 的像 $\mathbf{a}_2$；它们就是矩阵的两列。在压扁中，$\mathbf{a}_2=\mathbf{0}$，正方形变成从 $\mathbf{0}$ 到 $\mathbf{e}_1$ 的线段。
:::

<ul>

<li>

逆时针__旋转__ $90^\circ$ 把 $\mathbf{e}_1$ 变成 $(0,\,1)^{\top}$，把 $\mathbf{e}_2$ 变成 $(-1,\,0)^{\top}$；它们就是这个矩阵的两列。

</li>

<li>

__拉伸__ $\operatorname{diag}(2,\,0.5)$ 把平面在水平方向拉宽到两倍，在竖直方向压缩到一半高度。

</li>

<li>

__剪切__ $\bigl(\begin{smallmatrix}1&1\\0&1\end{smallmatrix}\bigr)$ 使 $\mathbf{e}_1$ 保持不动，把 $\mathbf{e}_2$ 推向右边：每个点都向右移动，移动的距离等于它的高度。

</li>

<li>

矩阵 $\operatorname{diag}(1,\,0)$ 保留第一个分量，把第二个分量置为零。它把整个平面压扁到 $x_1$ 轴上。

</li>

</ul>

::::beispiel [算例] 任意角度的旋转
逆时针旋转角度 $\alpha$ 时，$\mathbf{e}_1$ 落到单位圆上的点 $(\cos\alpha,\,\sin\alpha)^{\top}$，而比它再转过 $90^\circ$ 的 $\mathbf{e}_2$ 落到点 $(-\sin\alpha,\,\cos\alpha)^{\top}$。所以由式 [(8.2)](#gl-8-2)，旋转矩阵为

<span class="anker" id="gl-8-3"></span>
$$\mathbf R_\alpha=\begin{pmatrix}\cos\alpha&-\sin\alpha\\\sin\alpha&\cos\alpha\end{pmatrix}. \tag{8.3}$$

当 $\alpha=90^\circ$ 时，得到图 [32](#abb-32) 中的矩阵。它把点 $(1,\,1)^{\top}$ 旋转到 $(-1,\,1)^{\top}$；拉伸把同一个点映射到 $(2,\ 0.5)^{\top}$，剪切把它映射到 $(2,\,1)^{\top}$，压扁把它映射到 $(1,\,0)^{\top}$。
::::

⁠**简而言之：**$2\times2$ 矩阵使平面的网格变形；单位正方形变成由它的两列张成的平行四边形。

### 只有一个输出的线性函数

<span class="anker" id="stufe-8-4"></span>

把一个样本的特征变成单个数的模型，是从 $\mathbb{R}^d$ 到 $\mathbb{R}$ 的映射。如果它是线性的，那么由第 [8.2](#stufe-8-2) 小节中的定理，它的矩阵只有一行，含 $d$ 个元素。

:::satz 定理 8.3 (线性函数就是加权和)
<span class="anker" id="satz-8-3"></span>

每个线性映射 $f\colon\mathbb{R}^d\to\mathbb{R}$ 都具有 $f(\mathbf{x})=\mathbf{w}^{\top}\mathbf{x}$ 的形式，其中权重为 $w_j=f(\mathbf{e}_j)$。
:::

这就是第 [8.2](#stufe-8-2) 小节中的定理在 $m=1$ 时的情形：$1\times d$ 矩阵就是行 $\mathbf{w}^{\top}$，它与 $\mathbf{x}$ 的乘积就是点积。所以，第 [2.2](das-skalarprodukt.html#stufe-2-2) 小节中的加权和并不只是众多规则中的一种，而是只有一个输出的最一般的线性规则。

::::beispiel [算例]
房产经纪人的规则是 $f(\mathbf{x})=3x_1+10x_2-4x_3$。有 $f(\mathbf{e}_1)=3$，$f(\mathbf{e}_2)=10$，$f(\mathbf{e}_3)=-4$，所以 $\mathbf{w}=(3,\,10,\,-4)^{\top}$。权重 $w_j=f(\mathbf{e}_j)$ 是这条规则对一个假想样本的取值，这个样本只有一个单位的特征 $j$，其他什么都没有：它说明这个特征的一个单位贡献多少。
::::

⁠**简而言之：**每个只有一个输出的线性映射都是加权和 $\mathbf{w}^{\top}\mathbf{x}$，权重 $w_j$ 是它在 $\mathbf{e}_j$ 处的值。

### 仿射映射

<span class="anker" id="stufe-8-5"></span>

房产经纪人发现她的估价一律偏低。于是她在每个加权和上都加上 $20$ 千欧元的基础金额。这条新规则不再是线性的：它给假想的公寓 $\mathbf{x}=\mathbf{0}$ 指定的是 $20$，而不是 $0$。它是一个线性映射，后面再接一次平移。

:::definition 定义 8.4 (仿射映射)
<span class="anker" id="satz-8-4"></span>

如果映射 $f\colon\mathbb{R}^n\to\mathbb{R}^m$ 具有形式

<span class="anker" id="gl-8-4"></span>
$$f(\mathbf{x})=\mathbf{A}\mathbf{x}+\mathbf{b} \tag{8.4}$$

其中 $\mathbf{A}\in\mathbb{R}^{m\times n}$ 是矩阵，$\mathbf{b}\in\mathbb{R}^m$ 是固定的向量，就称它为__仿射__映射。对只有一个输出的情形（$m=1$），写作 $f(\mathbf{x})=\mathbf{w}^{\top}\mathbf{x}+b$，并把数 $b$ 称为__截距__。
:::

当 $\mathbf{b}\ne\mathbf{0}$ 时，仿射映射不是线性的，因为 $f(\mathbf{0})=\mathbf{b}\ne\mathbf{0}$。用网格的图景来说，平面先变形，然后作为整体平移 $\mathbf{b}$；原点落到 $\mathbf{b}$ 处。在日常用语中，仿射规则也常被称为“线性的”。在本系列中，只有 $\mathbf{b}=\mathbf{0}$ 的映射才称为线性映射。

对所有样本同时计算时，借助全 1 向量 $\mathbf 1\in\mathbb{R}^N$ 写出仿射预测：

<span class="anker" id="gl-8-5"></span>
$$\hat{\mathbf{y}}=\mathbf{X}\mathbf{w}+b\,\mathbf 1 . \tag{8.5}$$

项 $b\,\mathbf 1$ 给每个预测值加上同样的数 $b$。

::::beispiel [算例]
取 $\mathbf{w}=(3,\,10,\,-4)^{\top}$ 和 $b=20$，预测值 $(188,\,126,\,286,\,232)^{\top}$ 变为

$$\hat{\mathbf{y}}=\mathbf{X}\mathbf{w}+20\cdot\mathbf 1=(208,\,146,\,306,\,252)^{\top}\ \text{千欧元}.$$
::::

⁠**简而言之：**仿射映射是线性映射加上一个固定的平移，$\mathbf{A}\mathbf{x}+\mathbf{b}$；只有一个输出时，这个平移称为截距。

:::hintergrund 附加一个 1 的技巧
如果给每个样本附加一个取固定值 $1$ 的分量，仿射函数就可以写成线性函数：

$$\mathbf{w}^{\top}\mathbf{x}+b=\begin{pmatrix}w_1&\cdots&w_d&b\end{pmatrix}\begin{pmatrix}x_1\\\vdots\\x_d\\1\end{pmatrix}.$$

这样，截距就成了一个取值恒为 $1$ 的特征的权重。对整个数据集，就给数据矩阵附加一个全 1 列：$\begin{pmatrix}\mathbf{X}&\mathbf 1\end{pmatrix}\begin{pmatrix}\mathbf{w}\\b\end{pmatrix}=\mathbf{X}\mathbf{w}+b\,\mathbf 1$。对公寓数据集，增广数据矩阵的各行为 $(60,2,3,1)$、$(40,1,1,1)$、$(90,4,6,1)$、$(70,3,2,1)$，与向量 $(3,\,10,\,-4,\,20)^{\top}$ 相乘，又得到 $(208,\,146,\,306,\,252)^{\top}$。有了这个技巧，仿射规则就不需要单独的理论：对线性映射成立的一切，在多一维的空间中对它们也成立。
:::

:::aufgabe 练习 18 ★ 线性还是非线性？
<span class="anker" id="aufg-18"></span>

判断下列映射中哪些是线性的，并给出每个线性映射的矩阵：

$$\begin{gathered} f_1(\mathbf{x})=(2x_1,\ x_1-x_2)^{\top},\qquad f_2(\mathbf{x})=x_1^2,\qquad f_3(\mathbf{x})=(x_2,\ x_1)^{\top},\\ f_4(x)=2x+3,\qquad f_5(\mathbf{x})=(0,\ 0)^{\top} \end{gathered}$$

其中 $\mathbf{x}\in\mathbb{R}^2$，对 $f_4$ 则是 $x\in\mathbb{R}$。

:::loesung
<ul>

<li>

$f_1$ 是线性的；两个分量都是 $x_j$ 的倍数之和。各列为 $f_1(\mathbf{e}_1)=(2,\,1)^{\top}$ 和 $f_1(\mathbf{e}_2)=(0,\,-1)^{\top}$，所以矩阵为 $\bigl(\begin{smallmatrix}2&0\\1&-1\end{smallmatrix}\bigr)$。

</li>

<li>

$f_2$ 不是线性的：只要 $x_1\ne0$，就有 $f_2(2\mathbf{x})=4x_1^2\ne2f_2(\mathbf{x})$。

</li>

<li>

$f_3$ 是线性的，矩阵为 $\bigl(\begin{smallmatrix}0&1\\1&0\end{smallmatrix}\bigr)$；它交换两个分量。

</li>

<li>

$f_4$ 不是线性的，因为 $f_4(0)=3\ne0$。它是仿射的，截距为 $3$。

</li>

<li>

$f_5$ 是线性的，矩阵为零矩阵；两个条件都成立，因为 $\mathbf{0}+\mathbf{0}=\mathbf{0}$ 且 $c\,\mathbf{0}=\mathbf{0}$。

</li>

</ul>
:::
:::

:::aufgabe 练习 19 ★★ 由单位向量的像求矩阵
<span class="anker" id="aufg-19"></span>

<ol class="al">

<li>

给出旋转 $30^\circ$ 的矩阵，并计算 $(2,\,0)^{\top}$ 的像。

</li>

<li>

关于角平分线 $x_1=x_2$ 的反射交换两个分量。给出它的矩阵以及 $(3,\,1)^{\top}$ 的像。

</li>

<li>

一个线性映射满足 $f\bigl((1,\,1)^{\top}\bigr)=(1,\,4)^{\top}$ 和 $f\bigl((2,\,-1)^{\top}\bigr)=(5,\,-1)^{\top}$。求它的矩阵。提示：用列 $\mathbf{a}_1,\mathbf{a}_2$ 写出这两个条件。

</li>

</ol>

:::loesung
(a) 由式 [(8.3)](#gl-8-3)，利用 $\cos30^\circ=\sqrt3/2\approx0.866$ 和 $\sin30^\circ=\tfrac12$：

$$\mathbf R_{30^\circ}=\begin{pmatrix}0.866&-0.5\\0.5&0.866\end{pmatrix},\qquad \mathbf R_{30^\circ}\begin{pmatrix}2\\0\end{pmatrix}=\begin{pmatrix}\sqrt3\\1\end{pmatrix}\approx\begin{pmatrix}1.732\\1\end{pmatrix}.$$

像是第一列的两倍，即一个长度为 $2$、倾角为 $30^\circ$ 的箭头。

(b) $\mathbf{e}_1$ 变为 $\mathbf{e}_2$，$\mathbf{e}_2$ 变为 $\mathbf{e}_1$，所以矩阵为 $\bigl(\begin{smallmatrix}0&1\\1&0\end{smallmatrix}\bigr)$，而 $(3,\,1)^{\top}$ 变为 $(1,\,3)^{\top}$。

(c) 由线性，$f\bigl((1,1)^{\top}\bigr)=\mathbf{a}_1+\mathbf{a}_2=(1,\,4)^{\top}$，$f\bigl((2,-1)^{\top}\bigr)=2\mathbf{a}_1-\mathbf{a}_2=(5,\,-1)^{\top}$。两个方程相加，得 $3\mathbf{a}_1=(6,\,3)^{\top}$，所以 $\mathbf{a}_1=(2,\,1)^{\top}$，$\mathbf{a}_2=(1,4)^{\top}-(2,1)^{\top}=(-1,\,3)^{\top}$。矩阵为 $\bigl(\begin{smallmatrix}2&-1\\1&3\end{smallmatrix}\bigr)$。验算：$\bigl(\begin{smallmatrix}2&-1\\1&3\end{smallmatrix}\bigr)(2,\,-1)^{\top}=(5,\,-1)^{\top}$。
:::
:::

:::aufgabe 练习 20 ★★ 由水表读数求用水量的矩阵
<span class="anker" id="aufg-20"></span>

一个新水表在四个月的月末分别显示读数 $x[1],\dots,x[4]$（单位：立方米）；第一个月之前它的读数为 $x[0]=0$。第 $n$ 个月的用水量是差 $y[n]=x[n]-x[n-1]$，$n=1,\dots,4$。

<ol class="al">

<li>

为什么这个计算是线性的？通过计算对四个单位向量的响应，建立它的 $4\times4$ 矩阵。

</li>

<li>

分别用矩阵和用公式计算读数 $\mathbf{x}=(1,\,2,\,4,\,7)^{\top}$ 对应的用水量。

</li>

</ol>

:::loesung
(a) 结果的每个分量 $y[n]=x[n]-x[n-1]$ 都是 $\mathbf{x}$ 各分量的固定倍数之和，所以这个计算是线性的。对位置 $1$ 处单独的 $1$，即 $\mathbf{x}=\mathbf{e}_1=(1,0,0,0)^{\top}$，响应是 $(1,\,-1,\,0,\,0)^{\top}$：读数先升到 $1$，然后又降回 $0$。同样，这个计算对 $\mathbf{e}_2$ 的响应为 $(0,\,1,\,-1,\,0)^{\top}$，对 $\mathbf{e}_3$ 为 $(0,\,0,\,1,\,-1)^{\top}$，对 $\mathbf{e}_4$ 为 $(0,\,0,\,0,\,1)^{\top}$；对最后这个 $1$，四个月在读数回落之前就结束了。这些响应就是各列：

$$\mathbf{A}=\begin{pmatrix}1&0&0&0\\-1&1&0&0\\0&-1&1&0\\0&0&-1&1\end{pmatrix}.$$

(b) 用矩阵：$\mathbf{A}\,(1,2,4,7)^{\top}=(1,\ -1+2,\ -2+4,\ -4+7)^{\top}=(1,\,1,\,2,\,3)^{\top}$。用公式：$y[1]=1-0=1$，$y[2]=2-1=1$，$y[3]=4-2=2$，$y[4]=7-4=3$。所以这四个月分别用了 $1$、$1$、$2$ 和 $3$ 立方米水。
:::
:::
