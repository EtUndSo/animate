---
title: 距离与单位
pfad: 计算机科学 / 机器学习 / 数学基础 / 向量与矩阵
knoten: 基础篇 1：向量与矩阵
nachschlagen: ja
order: 15210500
summary: 如果两个样本的向量彼此靠近，它们就相似。本节度量距离，说明结果取决于所选的单位，并介绍一种使各特征可以相互比较的方法。
tags: 距离, 特征列, 中心化的, 标准差, 标准化
lang: zh
---

<span class="anker" id="stufe-4"></span>

:::zweck
如果两个样本的向量彼此靠近，它们就相似。本节度量距离，说明结果取决于所选的单位，并介绍一种使各特征可以相互比较的方法。
:::

### 两个数据点之间的距离

<span class="anker" id="stufe-4-1"></span>

两套公寓如果在所有特征上都只略有差别，它们就是相似的。这些差别包含在差向量 $\mathbf{u}-\mathbf{v}$ 中，即从一个点指向另一个点的箭头。范数告诉你这个箭头有多大。

:::definition 定义 4.1 (距离)
<span class="anker" id="satz-4-1"></span>

两个向量 $\mathbf{u},\mathbf{v}\in\mathbb{R}^d$ 关于某个范数的__距离__是它们之差的范数 $\lVert\mathbf{u}-\mathbf{v}\rVert$。如无其他说明，指的是欧几里得距离。
:::

人们对距离所期待的性质，都由范数的性质得出：距离永远不为负，只有对相同的点才为零；从 $\mathbf{u}$ 到 $\mathbf{v}$ 的距离与从 $\mathbf{v}$ 到 $\mathbf{u}$ 的一样大，因为 $\mathbf{v}-\mathbf{u}=-(\mathbf{u}-\mathbf{v})$；经过第三点 $\mathbf{q}$ 的路线永远不会更短，$\lVert\mathbf{u}-\mathbf{v}\rVert\le\lVert\mathbf{u}-\mathbf{q}\rVert+\lVert\mathbf{q}-\mathbf{v}\rVert$。这就是把三角不等式 (N3) 应用于 $\mathbf{u}-\mathbf{v}=(\mathbf{u}-\mathbf{q})+(\mathbf{q}-\mathbf{v})$。

**距离与点积。** 用点积的运算规则展开欧几里得距离的平方，得到

<span class="anker" id="gl-4-1"></span>
$$\lVert\mathbf{u}-\mathbf{v}\rVert^2=(\mathbf{u}-\mathbf{v})^{\top}(\mathbf{u}-\mathbf{v})=\lVert\mathbf{u}\rVert^2+\lVert\mathbf{v}\rVert^2-2\,\mathbf{u}^{\top}\mathbf{v} . \tag{4.1}$$

所以在长度固定时，点积越大，距离就越小。两者都衡量相似程度，只是方向相反。

::::beispiel [算例]
公寓 1 和 2 相差 $\mathbf{x}_1-\mathbf{x}_2=(20,\,1,\,2)^{\top}$。它们的欧几里得距离为 $\sqrt{405}\approx20.12$（图 [18](#abb-18)）；按 1-范数是 $20+1+2=23$，按最大范数是 $20$。

:::abbildung ml/k1rabstand 18
公寓 1 和 2 之间的欧几里得距离：先求差，再求它的长度。
:::

用 $\mathbf{u}=(1,\,2,\,2)^{\top}$ 和 $\mathbf{v}=(2,\,0,\,1)^{\top}$ 验证式 [(4.1)](#gl-4-1)：左边为 $\lVert(-1,\,2,\,1)^{\top}\rVert^2=6$，右边为 $9+5-2\cdot4=6$。
::::

⁠**简而言之：**两个数据点之间的距离是它们之差的范数；距离近就意味着相似。

### 距离取决于单位

<span class="anker" id="stufe-4-2"></span>

在刚才的算例中，距离 $20.12$ 几乎恰好等于面积之差 $20\,\mathrm m^2$。距离的平方 $405$ 中有 $400$ 来自面积。相差一个房间和两公里几乎不起作用，而这仅仅是因为以平方米计的面积是很大的数。

另外三套公寓说明了由此带来的后果。问题是：公寓 B 和 C 中哪一套与公寓 A 更相似？

$$\text{A}=(60,\,2)^{\top},\qquad \text{B}=(63,\,4)^{\top},\qquad \text{C}=(54,\,2)^{\top}\qquad(\text{面积，单位 m}^2,\ \text{房间数}).$$

以平方米计，$\lVert\text{A}-\text{B}\rVert=\sqrt{9+4}\approx3.61$，$\lVert\text{A}-\text{C}\rVert=\sqrt{36+0}=6$：B 更近。如果以 $10\,\mathrm m^2$ 为单位计量面积，则 $\text{A}=(6,\,2)^{\top}$，$\text{B}=(6.3,\ 4)^{\top}$，$\text{C}=(5.4,\ 2)^{\top}$，而 $\lVert\text{A}-\text{B}\rVert=\sqrt{0.09+4}\approx2.02$，$\lVert\text{A}-\text{C}\rVert=0.6$：现在 C 更近。图 [19](#abb-19) 给出了两种图景。

:::abbildung ml/k1einheiten 19
同样的三套公寓，左图中面积以 $\mathrm m^2$ 为单位，右图中以 $10\,\mathrm m^2$ 为单位。每幅图的两根坐标轴比例相同，所以线段的长度就是欧几里得距离。左图中 B 离 A 更近（虚线：以 A 为圆心、经过 B 的圆）；右图中 C 更近。
:::

其中的机制很简单。距离的平方包含每个特征之差的平方。如果用另一个单位计量某个特征，它的数值就变为原来的 $c$ 倍，它对距离平方的贡献变为原来的 $c^2$ 倍。其他特征的贡献保持不变。数值大的特征几乎单独决定了距离；数值小的特征则几乎被淹没。

⁠**简而言之：**样本之间的距离取决于各特征的单位；哪个样本与另一个最相似，可能随单位的改变而改变。

:::hintergrund 每一种单位选择都是一种加权
欧几里得距离把平方米、房间数和公里的平方相加。从计算上说，这行得通，因为计算机只看到数字。从物理上说，这是不同种类的量之和，而单位决定了每种量占多大分量。以 $\mathrm m^2$ 给出面积的人，就在无意中决定了：相差 $1\,\mathrm m^2$ 与相差一个房间同样重要。并不存在由自然给定的正确选择。必须有意识地作出选择，而下面的方法就是这样一种有意识的选择。
:::

### 与均值的偏差

<span class="anker" id="stufe-4-3"></span>

为了使各特征可以相互比较，要对每个特征单独考察它在所有样本上的取值。在表 [1](vektoren-daten-als-zahlenlisten.html#tab-1) 中，这就是各列：所有公寓的面积构成向量 $\mathbf{v}=(60,\,40,\,90,\,70)^{\top}\in\mathbb{R}^4$。这样的向量属于一个特征，它的分量个数与样本个数相同。这里称它为__特征列__。

在比较时，重要的不是面积有多大，而是它们彼此相差多少。因此，把每个面积都作为与平均值的偏差来度量。在电工学中，这一步称为：去掉直流分量，只保留交流分量。

:::definition 定义 4.2 (中心化向量)
<span class="anker" id="satz-4-2"></span>

对均值为 $\bar v$ 的 $\mathbf{v}\in\mathbb{R}^N$，

<span class="anker" id="gl-4-2"></span>
$$\tilde{\mathbf{v}}=\mathbf{v}-\bar v\,\mathbf 1=(v_1-\bar v,\,\dots,\,v_N-\bar v)^{\top} \tag{4.2}$$

称为__中心化的__向量。它的分量就是与均值的偏差。
:::

这些偏差总是相互抵消：$\mathbf 1^{\top}\tilde{\mathbf{v}}=\mathbf 1^{\top}\mathbf{v}-\bar v\,\mathbf 1^{\top}\mathbf 1=N\bar v-\bar v\,N=0$。所以中心化向量的均值为零。

::::beispiel [算例]
面积 $\mathbf{v}=(60,\,40,\,90,\,70)^{\top}$ 的均值为 $\bar v=65$。中心化后为 $\tilde{\mathbf{v}}=(-5,\,-25,\,25,\,5)^{\top}$，这些偏差相加确实为零（图 [20](#abb-20)）。房间数 $(2,\,1,\,4,\,3)^{\top}$ 的均值为 $2.5$，中心化后为 $(-0.5,\ -1.5,\ 1.5,\ 0.5)^{\top}$；距离 $(3,\,1,\,6,\,2)^{\top}$ 的均值为 $3$，中心化后为 $(0,\,-2,\,3,\,-1)^{\top}$。

:::abbildung ml/k1rzentriert 20
面积的均值，以及与均值的偏差之和，单位为 $\mathrm m^2$。
:::
::::

⁠**简而言之：**中心化就是从每个分量中减去均值；剩下的是偏差，它们之和为零。

### 标准差

<span class="anker" id="stufe-4-4"></span>

一个特征波动有多大，可以从它的偏差大小看出。一个分量的典型大小就是第 [3.6](normen-die-groe-eines-vektors.html#stufe-3-6) 小节中的有效值。把它用于中心化向量，就得到与均值的典型偏差。用电工学的语言来说：交流分量的有效值。

:::definition 定义 4.3 (标准差)
<span class="anker" id="satz-4-3"></span>

向量 $\mathbf{v}\in\mathbb{R}^N$ 的__标准差__是它的中心化向量的有效值：

<span class="anker" id="gl-4-3"></span>
$$\operatorname{std}(\mathbf{v})=\operatorname{rms}(\tilde{\mathbf{v}})=\frac{\lVert\mathbf{v}-\bar v\,\mathbf 1\rVert}{\sqrt N}=\sqrt{\frac1N\sum_{i=1}^N(v_i-\bar v)^2} . \tag{4.3}$$
:::

标准差与特征的单位相同。当且仅当所有分量都相等时，它为零。许多文献在式 [(4.3)](#gl-4-3) 中除以 $N-1$ 而不是 $N$。样本很多时，两者差别很小。本系列除以 $N$；若某处要用别的除数，会专门说明。

::::beispiel [算例]
中心化的面积 $(-5,\,-25,\,25,\,5)^{\top}$ 的平方和为 $1\,300$，所以 $\operatorname{std}(\mathbf{v})=\sqrt{325}\approx18.03\,\mathrm m^2$，计算过程见图 [21](#abb-21)。同样可得房间数的标准差为 $\sqrt{5/4}\approx1.118$，距离的标准差为 $\sqrt{14/4}\approx1.871$ km。

:::abbildung ml/k1rstd 21
面积的标准差：把偏差平方，取平均，再开平方。结果 $\sqrt{325}\approx18.03$ 的单位是 $\mathrm m^2$。
:::
::::

⁠**简而言之：**标准差是与均值的偏差的有效值，即一个特征的典型波动。

:::hintergrund 直流分量和交流分量分担功率
一个向量是它的直流分量 $\bar v\,\mathbf 1$ 与交流分量 $\tilde{\mathbf{v}}$ 之和。对于长度的平方，点积的运算规则给出

$$\lVert\bar v\,\mathbf 1+\tilde{\mathbf{v}}\rVert^2=\bar v^2\,\mathbf 1^{\top}\mathbf 1+2\,\bar v\,\mathbf 1^{\top}\tilde{\mathbf{v}}+\lVert\tilde{\mathbf{v}}\rVert^2=N\bar v^2+0+\lVert\tilde{\mathbf{v}}\rVert^2 ,$$

因为偏差之和为零。除以 $N$，就变成 $\operatorname{rms}(\mathbf{v})^2=\bar v^2+\operatorname{std}(\mathbf{v})^2$。这与交直流混合电流的分解相同：它在电阻上的功率等于直流分量的功率与交流分量的功率之和。对于面积：$\operatorname{rms}^2=(3600+1600+8100+4900)/4=4550=65^2+325$。
:::

### 标准化

<span class="anker" id="stufe-4-5"></span>

现在，每个特征都可以用它自身的典型波动来度量。不说“比平均值大 $25\,\mathrm m^2$”，而说“比平均值高 $1.39$ 个标准差”。用这种说法，每个特征都具有相同的数量级，不论它原来是用什么单位测量的。

:::definition 定义 4.4 (标准化)
<span class="anker" id="satz-4-4"></span>

设特征 $j$ 的特征列的均值为 $\bar x_j$，标准差为 $s_j>0$。把这个特征__标准化__，就是计算

<span class="anker" id="gl-4-4"></span>
$$z_{ij}=\frac{x_{ij}-\bar x_j}{s_j},\qquad i=1,\dots,N, \tag{4.4}$$

并用这些数代替原来的值。数 $z_{ij}$ 称为标准化值。
:::

标准化后的特征列均值为 $0$，标准差为 $1$，因为中心化使均值为零，除以 $s_j$ 使典型偏差为一。这些值不再带有单位。

::::beispiel [算例 1] 公寓数据集
用均值 $65$、$2.5$、$3$ 和标准差 $18.03$、$1.118$、$1.871$，四套公寓变为

$$\begin{aligned} \mathbf{z}_1&\approx(-0.28,\ -0.45,\ 0)^{\top}, & \mathbf{z}_2&\approx(-1.39,\ -1.34,\ -1.07)^{\top},\\ \mathbf{z}_3&\approx(1.39,\ 1.34,\ 1.60)^{\top}, & \mathbf{z}_4&\approx(0.28,\ 0.45,\ -0.53)^{\top}. \end{aligned}$$

现在三个特征都位于同一数值范围内。
::::

::::beispiel [算例 2] A、B 和 C
第 [4.2](#stufe-4-2) 小节中的三套公寓平均面积为 $59\,\mathrm m^2$，标准差为 $\sqrt{14}\approx3.74\,\mathrm m^2$；平均有 $8/3$ 个房间，标准差为 $\sqrt{8/9}\approx0.943$。标准化后，$\lVert\text A-\text B\rVert\approx2.27$，$\lVert\text A-\text C\rVert\approx1.60$。所以与 A 最相似的是 C，而且这一判断不再取决于面积的单位。
::::

单位被消去，这一点普遍成立：

:::satz 定理 4.5 (标准化值与单位无关)
<span class="anker" id="satz-4-5"></span>

如果把一个特征换算成另一个单位，即对所有 $i$ 有 $v_i'=\alpha\,v_i+\beta$，其中 $\alpha>0$ 和 $\beta$ 是数，那么它的标准化值保持不变。
:::

:::beweis 与单位无关
均值变为 $\bar v'=\frac1N\sum_i(\alpha\,v_i+\beta)=\alpha\,\bar v+\beta$，偏差变为 $v_i'-\bar v'=\alpha\,(v_i-\bar v)$。由式 [(4.3)](#gl-4-3)，于是有 $\operatorname{std}(\mathbf{v}')=|\alpha|\operatorname{std}(\mathbf{v})=\alpha\operatorname{std}(\mathbf{v})$。在商式 [(4.4)](#gl-4-4) 中，$\alpha$ 被约去，而 $\beta$ 在中心化时就已经消失了。
:::

项 $\beta$ 也涵盖了零点平移的换算，例如从摄氏度换算成华氏度。

⁠**简而言之：**标准化把每个特征作为与均值的偏差、以其标准差的倍数来度量；此后，距离不再取决于单位。

:::hintergrund 为什么用标准差作为尺度？
对每个特征都需要一个尺度，它在换算单位时与各值之间的差按同一个因子变化。这样它就会被约去。凡是由该特征各值之间的差计算出来、并且具有该特征单位的量，都能做到这一点：标准差可以，从最小值到最大值的极差也可以。通常选用标准差，是因为它考虑了所有的值，而不只是两个极端值。

把两个标准化样本 $\mathbf{z}_a$ 和 $\mathbf{z}_b$ 相减，就能看出标准化对距离有什么作用。均值消去了，$z_{aj}-z_{bj}=(x_{aj}-x_{bj})/s_j$，剩下的是

$$\lVert\mathbf{z}_a-\mathbf{z}_b\rVert^2=\sum_{j=1}^d\frac{(x_{aj}-x_{bj})^2}{s_j^2} .$$

所以，标准化值之间的距离就是普通距离，只是特征 $j$ 上差的平方以权重 $1/s_j^2$ 计入。对公寓 A 和 B，这等于 $3^2/14+2^2/(8/9)=9/14+9/2\approx5.14$，其平方根为 $2.27$，与上面相同。

不过，标准化本身也是一种决定。它在距离中给每个特征相同的权重，即使某个特征对所讨论的问题毫无作用。一个在所有样本中取值都相同的特征，标准差为零，无法标准化；但它也区分不了样本，对任何距离都没有贡献。
:::

:::aufgabe 练习 9 ★ 直流分量与交流分量
<span class="anker" id="aufg-9"></span>

一个信号的采样值为 $\mathbf{x}=(1,\,3,\,1,\,-1)^{\top}$。计算均值、中心化向量、标准差和有效值。验证 $\operatorname{rms}(\mathbf{x})^2=\bar x^2+\operatorname{std}(\mathbf{x})^2$。

:::loesung
均值为 $\bar x=(1+3+1-1)/4=1$，中心化向量为 $\tilde{\mathbf{x}}=(0,\,2,\,0,\,-2)^{\top}$。标准差为 $\sqrt{(0+4+0+4)/4}=\sqrt2\approx1.414$，有效值为 $\sqrt{(1+9+1+1)/4}=\sqrt3\approx1.732$。验算：$\operatorname{rms}^2=3=1^2+(\sqrt2)^2=\bar x^2+\operatorname{std}^2$。直流分量与交流分量按 $1:2$ 的比例分担“功率”$3$。
:::
:::

:::aufgabe 练习 10 ★★ 哪套公寓与公寓 1 最相似？
<span class="anker" id="aufg-10"></span>

<ol class="al">

<li>

用表 [1](vektoren-daten-als-zahlenlisten.html#tab-1) 中的值，计算公寓 1 到公寓 2、3 和 4 的欧几里得距离。到公寓 2 的距离平方中，有多大比例来自面积？

</li>

<li>

用第 [4.5](#stufe-4-5) 小节中的标准化值计算同样的距离。现在到公寓 2 的距离平方中，有多大比例来自面积？

</li>

<li>

在两种情况下，分别是哪套公寓与公寓 1 最相似？如果标准化没有改变答案，那么它在这里改变了什么？

</li>

</ol>

:::loesung
(a) 用表中的值：

$$\begin{aligned} \lVert\mathbf{x}_1-\mathbf{x}_2\rVert&=\sqrt{20^2+1^2+2^2}=\sqrt{405}\approx20.12,\\ \lVert\mathbf{x}_1-\mathbf{x}_3\rVert&=\sqrt{30^2+2^2+3^2}=\sqrt{913}\approx30.22,\\ \lVert\mathbf{x}_1-\mathbf{x}_4\rVert&=\sqrt{10^2+1^2+1^2}=\sqrt{102}\approx10.10 . \end{aligned}$$

在到公寓 2 的距离平方 $405$ 中，有 $400$ 来自面积，即 $98.8$ %。

(b) 用第 [4.5](#stufe-4-5) 小节中的标准化向量，$\mathbf{z}_1-\mathbf{z}_2\approx(1.109,\ 0.894,\ 1.069)^{\top}$，各分量的平方为 $1.231$、$0.800$ 和 $1.143$。距离为 $\sqrt{3.174}\approx1.78$。同样得到 $\lVert\mathbf{z}_1-\mathbf{z}_3\rVert\approx2.92$ 和 $\lVert\mathbf{z}_1-\mathbf{z}_4\rVert\approx1.18$。现在，到公寓 2 的距离平方中来自面积的比例为 $1.231/3.174\approx38.8$ %。

(c) 在两种情况下，最相似的都是公寓 4，其次是公寓 2，然后是公寓 3。这里顺序没有改变，因为在这个小数据集中，大公寓同时房间更多、离市中心也更远；三个特征说明的大致是同一回事。改变的是公寓 4 **为什么**最相似：用原始值时，几乎只由面积决定；标准化之后，三个特征的贡献大致相同。答案仍然相同，这只是这些数据的巧合；对于第 [4.2](#stufe-4-2) 小节中的公寓 A、B 和 C，答案就改变了。
:::
:::

:::aufgabe 练习 11 ★★ 摄氏度还是华氏度
<span class="anker" id="aufg-11"></span>

在四天里，每天中午测得的气温分别为 $10$、$20$、$15$ 和 $25$ $^\circ$C。

<ol class="al">

<li>

换算成华氏度（$F=1.8\,C+32$）。用两种单位分别计算均值和标准差。

</li>

<li>

用两种单位分别计算标准化值，并加以比较。

</li>

<li>

如果用负的因子换算一个特征，例如 $v_i'=-v_i$，标准化值会怎样？

</li>

</ol>

:::loesung
(a) 换算成华氏度后，各值为 $1.8\cdot10+32=50$、$68$、$59$ 和 $77$。用摄氏度，均值为 $17.5$，标准差为 $\sqrt{(56.25+6.25+6.25+56.25)/4}=\sqrt{31.25}\approx5.590$；用华氏度，均值为 $63.5=1.8\cdot17.5+32$，标准差为 $\approx10.062=1.8\cdot5.590$。项 $32$ 只平移均值；因子 $1.8$ 还会拉伸标准差。

(b) 两种单位下的标准化值都是 $\approx(-1.342,\ 0.447,\ -0.447,\ 1.342)$。这正是第 [4.5](#stufe-4-5) 小节中的定理所说的：项在中心化时消失，因子与标准差相互约去。

(c) 当 $v_i'=-v_i$ 时，所有与均值的偏差都乘以 $-1$，而标准差乘以 $|-1|=1$。所以标准化值改变符号。对样本之间的距离而言，这没有影响，因为 $\lVert-\mathbf{u}\rVert=\lVert\mathbf{u}\rVert$；数据集只是作了一次镜像反射。
:::
:::
