---
title: 自动微分
pfad: 计算机科学 / 机器学习 / 数学基础 / 导数、梯度与链式法则
adresse: informatik/machine-learning/mathematische-grundlagen/ableitung-gradient-und-kettenregel
knoten: 第 3 章：导数、梯度与链式法则
nachschlagen: ja
order: 15231100
summary: 借助计算图，可以机械地计算导数，无需变换公式，而且除基本运算的舍入外是精确的。这称为自动微分。组合局部导数有两种方式：前向，与计算同步进行；或者反向，从结果到输入。反向模式只需一遍就给出一个数对其所有输入的导数，本节说明为什么这样做的代价如此之小。
tags: 自动微分, 前向模式, 切线值, 伴随值, 反向模式
lang: zh
---

<span class="anker" id="stufe-10"></span>

:::zweck
借助计算图，可以机械地计算导数，无需变换公式，而且除基本运算的舍入外是精确的。这称为自动微分。组合局部导数有两种方式：前向，与计算同步进行；或者反向，从结果到输入。反向模式只需一遍就给出一个数对其所有输入的导数，本节说明为什么这样做的代价如此之小。
:::

### 什么是自动微分

<span class="anker" id="stufe-10-1"></span>

得到一个计算的导数有三条途径。可以用法则变换公式；这称为符号求导，由第 [9.1](rechengraphen.html#stufe-9-1) 节，这样做时公式会迅速膨胀。可以在两个邻近的点处对函数求值并构成差商；这称为数值求导，它只是近似正确，第 [11](numerische-ableitung-und-gradientenprufung.html#stufe-11) 节研究它的误差。第三条途径兼具另外两条的优点。

:::definition 定义 10.1 (自动微分)
<span class="anker" id="satz-10-1"></span>

__自动微分__通过把链式法则应用于一个计算的计算图来计算它的导数：用计算中的数对局部导数求值，并按对路径求和的方式把它们组合起来。
:::

自动微分用数而不是用公式计算，因此不会有表达式膨胀。它不作任何近似：结果是精确的导数，只受到各个计算步骤舍入的影响。而且它适用于每个由基本运算构成的程序，即使有循环和分支也可以，因为对给定的输入，程序给出一个计算图。第 [9.1](rechengraphen.html#stufe-9-1) 节例子中的逐步计算就已经是自动微分了。

::::beispiel [算例]
对式 [(9.1)](rechengraphen.html#gl-9-1)，上一节由局部导数组合出了导数 $5$、$8$ 和 $3$，既没有把 $f$ 的公式乘开，也没有对它求导。这就是自动微分，只不过还没有确定计算顺序的固定程序。下面两个小节给出这个顺序。
::::

⁠**简而言之：**自动微分用数把链式法则应用于计算图；它除舍入外是精确的，而且不需要公式。

### 前向模式

<span class="anker" id="stufe-10-2"></span>

第一种可能是跟随计算本身。先规定沿哪个方向改变输入，然后在每个节点处，除了它的值以外，再一并记录它在这种改变下变化得有多快。

:::definition 定义 10.2 (前向模式)
<span class="anker" id="satz-10-2"></span>

在__前向模式__中，为输入选定一个方向 $\dot{\mathbf{x}}\in\mathbb{R}^n$，并对每个节点 $b$，除其值以外再计算数

<span class="anker" id="gl-10-1"></span>
$$\dot b=\sum_{a\text{ 为 }b\text{ 的前驱}}\frac{\partial b}{\partial a}\,\dot a , \tag{10.1}$$

计算顺序与各值的计算顺序相同。这个数称为 $b$ 的__切线值__；输入节点以 $\dot{\mathbf{x}}$ 的各分量作为切线值。
:::

这个名称让人想起第 [1.2](die-ableitung.html#stufe-1-2) 节中的切线，但它是一个数：切线值 $\dot b$ 是让输入沿直线 $\mathbf{x}+t\,\dot{\mathbf{x}}$ 移动时节点 $b$ 的变化率。式 [(10.1)](#gl-10-1) 就是针对单个节点、沿这条曲线的链式法则式 [(6.4)](die-kettenregel-fur-mehrere-variablen.html#gl-6-4)。一遍之后，结果处得到 $\dot f=\nabla f(\mathbf{x})^{\top}\dot{\mathbf{x}}$。如果计算有多个输出，那里得到的是雅可比矩阵与方向的乘积 $\mathbf{J}\,\dot{\mathbf{x}}$。取 $\dot{\mathbf{x}}=\mathbf{e}_j$，一遍就给出对 $x_j$ 的偏导数，有多个输出时则给出雅可比矩阵的第 $j$ 列。因此，对 $n$ 元函数的整个梯度，前向模式需要 $n$ 遍。

::::beispiel [算例]
对式 [(9.1)](rechengraphen.html#gl-9-1)，在点 $(1,\,2,\,3)$ 处取方向 $\dot{\mathbf{x}}=\mathbf{e}_2=(0,\,1,\,0)^{\top}$，得到表 [5](#tab-5)。结果处得到 $\dot f=8=\partial f/\partial x_2$。为求 $\partial f/\partial x_1$ 和 $\partial f/\partial x_3$，还需要用 $\mathbf{e}_1$ 和 $\mathbf{e}_3$ 再做两遍。

<span class="anker" id="tab-5"></span>

**表 5:** $f=(x_1+x_2)\,(x_2+x_3)$ 在点 $(1,\,2,\,3)$ 处沿方向 $\dot{\mathbf{x}}=\mathbf{e}_2$ 的前向模式。

| 节点 | 计算 | 值 | 切线值 |  |
|---|---|---|---|---|
| $x_1$ | 输入 | $1$ | $\dot x_1$ | $0$ |
| $x_2$ | 输入 | $2$ | $\dot x_2$ | $1$ |
| $x_3$ | 输入 | $3$ | $\dot x_3$ | $0$ |
| $v_1$ | $x_1+x_2$ | $3$ | $\dot v_1=\dot x_1+\dot x_2$ | $1$ |
| $v_2$ | $x_2+x_3$ | $5$ | $\dot v_2=\dot x_2+\dot x_3$ | $1$ |
| $f$ | $v_1\cdot v_2$ | $15$ | $\dot f=v_2\,\dot v_1+v_1\,\dot v_2$ | $5+3=8$ |
::::

⁠**简而言之：**前向模式为每个值一并记录它的切线值；一遍给出沿一个方向的导数，即雅可比矩阵的一列。

:::hintergrund 用对偶数实现前向模式
前向模式可以看作用扩充的数进行计算。用形如 $a+\dot a\,\varepsilon$ 的数对进行计算，其中 $\varepsilon$ 是一个新符号，唯一的规则是 $\varepsilon^2=0$；这样的数称为对偶数。加法和乘法照常进行：$(a+\dot a\varepsilon)+(b+\dot b\varepsilon)=(a+b)+(\dot a+\dot b)\varepsilon$，$(a+\dot a\varepsilon)(b+\dot b\varepsilon)=ab+(a\dot b+\dot ab)\varepsilon$，因为项 $\dot a\dot b\varepsilon^2$ 消失了。所以 $\varepsilon$ 前面的因子恰好遵循和法则与乘积法则。对式 [(9.1)](rechengraphen.html#gl-9-1)，令 $x_1=1$，$x_2=2+\varepsilon$，$x_3=3$，得到 $(3+\varepsilon)(5+\varepsilon)=15+8\varepsilon+\varepsilon^2=15+8\varepsilon$：一次计算就得到值和对 $x_2$ 的导数。对一元函数 $\varphi$，令 $\varphi(a+\dot a\varepsilon)=\varphi(a)+\varphi'(a)\,\dot a\,\varepsilon$，这对应于线性近似，其中小项的平方不起作用。对偶数是威廉·金登·克利福德（William Kingdon Clifford）于 1873 年引入的，远早于任何计算机。
:::

### 反向模式

<span class="anker" id="stufe-10-3"></span>

前向模式针对一个输入，问每个节点对它的依赖有多强。反向模式提出相反的问题：结果对每个节点的依赖有多强？这个问题可以从结果出发反向回答，最后就同时知道了所有输入的答案。

:::definition 定义 10.3 (反向模式)
<span class="anker" id="satz-10-3"></span>

节点 $a$ 的__伴随值__是 $\bar a=\partial f/\partial a$，即把该节点看作其余计算的输入时，结果对它的导数。在__反向模式__中，先进行前向计算并保存所有的值。然后令 $\bar f=1$，并按相反的顺序计算各节点：

<span class="anker" id="gl-10-2"></span>
$$\bar a=\sum_{b\text{ 为 }a\text{ 的后继}}\bar b\,\frac{\partial b}{\partial a}. \tag{10.2}$$

输入节点的伴随值构成梯度 $\nabla f(\mathbf{x})$。
:::

之所以需要相反的顺序，是因为每个节点都需要它的后继的伴随值，而这些后继在计算中排在它之后。每个伴随值都与其节点具有相同的形状；如果一个节点是向量或矩阵，那么它的伴随值也是向量或矩阵，就像第 [7.6](ableiten-nach-vektoren-und-matrizen.html#stufe-7-6) 节中矩阵乘积的反向法则那样。

:::satz 定理 10.4 (反向模式给出梯度)
<span class="anker" id="satz-10-4"></span>

对每个节点 $a$，按式 [(10.2)](#gl-10-2) 计算出的数 $\bar a$ 是对从 $a$ 到结果的所有路径的求和，沿每条路径取局部导数之积。对输入节点，由第 [9.4](rechengraphen.html#stufe-9-4) 节，这就是 $f$ 的偏导数。
:::

:::beweis 反向模式给出梯度
把从 $a$ 到结果的所有路径按它们的第一条边分组。每条路径都以一条通向某个后继 $b$ 的边开始，然后作为一条从 $b$ 到结果的路径继续下去。因此，经过 $b$ 的那些路径合起来贡献 $\frac{\partial b}{\partial a}$ 乘以从 $b$ 到结果的所有路径之和。如果对所有后继，这个和都已正确算出，即等于 $\bar b$，那么 $a$ 的和恰好就是式 [(10.2)](#gl-10-2)。对结果本身，结论以 $\bar f=1$ 成立，对应空路径。由于是反向计算，后继总是先于 $a$ 被处理，于是结论逐个节点地传递，一直到输入。
:::

::::beispiel [算例]
对式 [(9.1)](rechengraphen.html#gl-9-1)，在点 $(1,\,2,\,3)$ 处得到表 [6](#tab-6) 和图 [19](#abb-19)。仅仅一遍反向传递就给出了全部三个偏导数 $(5,\,8,\,3)$，而前向模式要三遍才能得到它们。

<span class="anker" id="tab-6"></span>

**表 6:** $f=(x_1+x_2)\,(x_2+x_3)$ 在点 $(1,\,2,\,3)$ 处的反向模式；各值取自表 [3](rechengraphen.html#tab-3)。

| 节点 | 按式 [(10.2)](#gl-10-2) 的计算 | 伴随值 |
|---|---|---|
| $f$ | 起点 | $\bar f=1$ |
| $v_2$ | $\bar f\cdot\partial f/\partial v_2=1\cdot v_1$ | $\bar v_2=3$ |
| $v_1$ | $\bar f\cdot\partial f/\partial v_1=1\cdot v_2$ | $\bar v_1=5$ |
| $x_3$ | $\bar v_2\cdot1$ | $\bar x_3=3$ |
| $x_2$ | $\bar v_1\cdot1+\bar v_2\cdot1$ | $\bar x_2=5+3=8$ |
| $x_1$ | $\bar v_1\cdot1$ | $\bar x_1=5$ |

:::abbildung ml/k3rueckwaerts 19
$f=(x_1+x_2)\,(x_2+x_3)$ 的计算图中在点 $(1,\,2,\,3)$ 处的前向值和反向值：绿色为前向计算的值，红色为伴随值，边上的灰色数字为局部导数。反向计算时，每个伴随值逆着箭头方向传递，并乘以该边的局部导数；在一个节点引出两条边的地方，例如 $x_2$ 处，各贡献相加。
:::
::::

⁠**简而言之：**反向模式先进行前向计算并保存所有的值，再反向计算伴随值 $\bar a=\sum\bar b\,\partial b/\partial a$；一遍反向传递就给出整个梯度。

### 反向流动中的模式

<span class="anker" id="stufe-10-4"></span>

由表 [4](rechengraphen.html#tab-4)，基本运算在反向计算时以简单而反复出现的方式表现。熟悉这些模式的人，几乎不用计算就能写出伴随值，并能迅速发现推导中的错误。

:::satz 定理 10.5 (基本运算的模式)
<span class="anker" id="satz-10-5"></span>

<ol class="al">

<li>

⁠**加法**把它的伴随值原封不动地传给每个输入。

</li>

<li>

⁠**乘法**传给每个输入的，是它的伴随值乘以**另一个**输入的值。

</li>

<li>

⁠**最大值**把它的伴随值全部传给较大的输入，较小的输入得到 $0$。

</li>

<li>

一元函数把伴随值乘以它的局部导数，对逻辑斯谛函数即乘以 $b\,(1-b)$。

</li>

<li>

如果一个节点被多次使用，那么它的所有后继的贡献**相加**。

</li>

</ol>
:::

每条结论都是式 [(10.2)](#gl-10-2) 加上表 [4](rechengraphen.html#tab-4) 中的局部导数。由 (b) 得出一个有用的观察：如果一个因子是另一个的一千倍，那么较小因子的伴随值就是较大因子的伴随值的一千倍。因此，输入的数量级相差很大，会导致偏导数同样相差很大。

::::beispiel [算例]
在表 [6](#tab-6) 中，乘法进行了交换：$v_1$ 得到 $v_2=5$，$v_2$ 得到 $v_1=3$。加法把这些值原封不动地传了下去，而 $x_2$ 作为有两个后继的节点，汇集了 $5+3=8$。一个有最大值的例子：对 $f=\max(x_1,x_2)\cdot x_3$，在点 $(1,\,2,\,3)$ 处，$v=\max(1,2)=2$，$f=6$。反向计算得 $\bar v=x_3=3$ 和 $\bar x_3=v=2$；最大值把 $\bar v$ 传给较大的输入 $x_2$，所以 $\bar x_2=3$，$\bar x_1=0$。实际上，只要 $x_1<x_2$ 保持成立，$x_1$ 的微小变化就不会改变结果。
::::

⁠**简而言之：**加法分发，乘法交换，最大值转交，在分支处相加。

### 计算量

<span class="anker" id="stufe-10-5"></span>

为什么反向模式如此重要？因为它给出一个有极多输入的函数的梯度，代价几乎和函数值本身一样低。比较各种方法就能看清这一点。

对 $n$ 元函数的梯度，前向模式需要 $n$ 遍，每个输入方向一遍。一遍的代价是对 $f$ 求一次值的一个小倍数，因为每个基本运算都要附带计算它的切线值。差商甚至需要 $n+1$ 次或 $2n$ 次求值。相反，反向模式总是恰好需要一次前向计算和一遍反向传递，无论 $n$ 有多大。在反向传递中，每条边恰好用一次，作一次乘法和一次加法。所以它的代价同样只是前向计算的一个小倍数。

:::satz 定理 10.6 (前向模式与反向模式的计算量)
<span class="anker" id="satz-10-6"></span>

设 $\mathbf{g}:\mathbb{R}^n\to\mathbb{R}^m$ 由一个基本运算构成的计算图给出，求一次值花费时间 $T$。则整个雅可比矩阵在前向模式下约花费 $c\cdot n\cdot T$，在反向模式下约花费 $c\cdot m\cdot T$。数 $c$ 与 $n$ 和 $m$ 无关。若把每次基本算术运算算作一步，可以证明，函数值与梯度合起来所需的步数至多是单求函数值的四倍；若把内存访问也算进去，$c$ 仍小于 $6$，实践中常在 $2$ 到 $3$ 之间。所以对一个数（$m=1$），反向模式下整个梯度的代价只是一次求值的一个固定的小倍数。
:::

证明这个定理的方法是：对每个基本运算，数一数它的反向步骤所需的计算步数与它本身相比是多少。由此得出一条经验法则：输入多、输出只有一个，例如一个依赖于数百万个调节旋钮的数，就需要反向模式。输入少、输出多，就需要前向模式。对一个输入和输出都很多的函数的完整雅可比矩阵，没有这样的窍门；在那里，每种方法都要花费很多遍。

反向模式有一个代价：内存。反向传递需要前向计算的所有值，因为要用它们对局部导数求值。所以必须保留每个中间值，直到反向传递经过了它。在长计算中，这部分内存往往才是真正的限制。

::::beispiel [算例]
设一个函数有 $n=10^6$ 个输入，求一次值需要一秒。前向模式求梯度需要 $10^6$ 遍，即至少 $10^6$ 秒，略多于 $11$ 天。中心差商需要 $2\cdot10^6$ 次求值，略多于 $23$ 天，而且结果只是近似正确。反向模式需要一次前向计算和一遍反向传递，取 $c\approx3$，也就只需几秒钟。
::::

⁠**简而言之：**反向模式以一次求值的一个固定小倍数的代价给出一个数的全部 $n$ 个偏导数，与 $n$ 无关；为此它付出的代价是保存所有中间值所需的内存。

:::hintergrund 反向模式为什么如此便宜，以及它的由来
对所有路径的和可能有非常多的项。把十个计算步骤串联起来，每一步都把它的前驱用两次，例如 $v_{k+1}=v_k\cdot v_k$，那么输入与结果之间就有 $2^{10}=1024$ 条路径，$50$ 步时则超过 $10^{15}$ 条。反向模式从不逐条计算这些路径。它把经过同一个节点的所有路径汇总到该节点的伴随值中，并把这个部分和继续用于所有前驱。这与第 [9.1](rechengraphen.html#stufe-9-1) 节中逐步应用乘积法则的思想相同：一个中间结果只算一次，然后多次使用。于是每条边花费一次乘法和一次加法，计算量随边的数目增长，而不是随路径的数目增长。可以只保留一部分中间值，在反向传递时重新计算其余的值，以此降低内存需求；如果分配得巧妙，内存以及计算时间超出单次求值的倍数，就都只随计算长度呈对数增长。

前向模式于 1964 年作为计算机程序被描述。反向模式是塞波·林纳因马（Seppo Linnainmaa）1970 年在赫尔辛基大学的硕士论文中提出的，目的是估计所有计算步骤的舍入误差如何影响结果；结果对每个中间步骤的灵敏度，恰好就是该步骤的伴随值。1980 年出现了能为任意计算自动生成反向模式的程序。
:::

### 结合方式：向量乘雅可比矩阵

<span class="anker" id="stufe-10-6"></span>

两种模式的区别也可以用矩阵来描述。一个由级 $\mathbf{g}_1,\dots,\mathbf{g}_L$ 组成、以一个数结束的计算，由式 [(6.1)](die-kettenregel-fur-mehrere-variablen.html#gl-6-1)，其雅可比矩阵为

$$\mathbf{J}=\mathbf{J}_L\,\mathbf{J}_{L-1}\cdots\mathbf{J}_1 ,$$

其中 $\mathbf{J}_L$ 是一行，因为最后一级只有一个输出。无论怎样加括号，乘积都相同；但由[第 1 章第 9.3 节](/wissen/zh/informatik/machine-learning/mathematische-grundlagen/vektoren-und-matrizen/das-matrixprodukt.html#stufe-9-3)，计算量却大不相同。反向模式从左结合：$\bigl((\mathbf{J}_L\mathbf{J}_{L-1})\,\mathbf{J}_{L-2}\bigr)\cdots$。每一步把一行乘以一个矩阵，又得到一行，即相应级的转置伴随值。前向模式从右结合：$\mathbf{J}_L\bigl(\cdots(\mathbf{J}_2\,(\mathbf{J}_1\dot{\mathbf{x}}))\bigr)$。对单个向量 $\dot{\mathbf{x}}$，这也很便宜；但对整个梯度，它需要 $n$ 个这样的向量，其代价就如同把矩阵 $\mathbf{J}_2\mathbf{J}_1$、$\mathbf{J}_3\mathbf{J}_2\mathbf{J}_1,\dots$ 完全乘出来一样高。

还有第二点：雅可比矩阵从不被构造出来。每个反向步骤都利用基本运算的法则，直接计算伴随值与雅可比矩阵的乘积。对矩阵-向量乘积 $\mathbf{y}=\mathbf{A}\mathbf{x}$，由式 [(7.6)](ableiten-nach-vektoren-und-matrizen.html#gl-7-6)，这就是 $\bar{\mathbf{x}}=\mathbf{A}^{\top}\bar{\mathbf{y}}$，不需要别的矩阵；对逐元素函数，由式 [(5.4)](die-jacobi-matrix.html#gl-5-4)，这是与各导数的逐分量乘积，无需建立对角矩阵。这也是必要的：如果一级有 $10^5$ 个输入和 $10^5$ 个输出，它的雅可比矩阵就有 $10^{10}$ 个元素，每个数 8 字节，共 $80$ GB。

::::beispiel [算例]
设一个计算由三个级 $\mathbb{R}^{1000}\to\mathbb{R}^{1000}$ 和最后一级 $\mathbb{R}^{1000}\to\mathbb{R}$ 组成。由[第 1 章第 9.3 节](/wissen/zh/informatik/machine-learning/mathematische-grundlagen/vektoren-und-matrizen/das-matrixprodukt.html#stufe-9-3)，一行与一个 $1000\times1000$ 矩阵的乘积约需 $2\cdot10^6$ 次基本算术运算，两个这样的矩阵的乘积约需 $2\cdot10^9$ 次。从左结合，是三次行与矩阵的乘积，合计约 $6\cdot10^6$ 次。从右结合，是两次矩阵乘积和一次行与矩阵的乘积，合计约 $4\cdot10^9$ 次，约为前者的 $670$ 倍。
::::

⁠**简而言之：**反向模式从左边用一行去乘雅可比矩阵链，前向模式从右边用一列去乘；雅可比矩阵本身从不被构造出来。

:::aufgabe 练习 35 ★ 反向通过平方
<span class="anker" id="aufg-35"></span>

设 $f=(x_1x_2+x_3)^2$，与练习 [32](rechengraphen.html#aufg-32) 中相同。

<ol class="al">

<li>

在点 $(1,\,2,\,3)$ 处用反向模式计算所有伴随值，并像表 [6](#tab-6) 那样列成表。

</li>

<li>

对同一个梯度，前向模式需要多少遍？对 $\dot{\mathbf{x}}=\mathbf{e}_1$ 执行这一遍。

</li>

</ol>

:::loesung
(a) 利用练习 [32](rechengraphen.html#aufg-32) 中的值：

| 节点 | 计算 | 伴随值 |
|---|---|---|
| $f$ | 起点 | $\bar f=1$ |
| $v_2$ | $\bar f\cdot2v_2$ | $\bar v_2=10$ |
| $v_1$ | $\bar v_2\cdot1$ | $\bar v_1=10$ |
| $x_3$ | $\bar v_2\cdot1$ | $\bar x_3=10$ |
| $x_2$ | $\bar v_1\cdot x_1$ | $\bar x_2=10$ |
| $x_1$ | $\bar v_1\cdot x_2$ | $\bar x_1=20$ |

(b) 三遍，每个输入一遍。取 $\dot{\mathbf{x}}=\mathbf{e}_1$：$\dot v_1=x_2\dot x_1+x_1\dot x_2=2$，$\dot v_2=\dot v_1+\dot x_3=2$，$\dot f=2v_2\,\dot v_2=10\cdot2=20=\partial f/\partial x_1$。
:::
:::

:::aufgabe 练习 36 ★★ 计算图中的逻辑斯谛函数
<span class="anker" id="aufg-36"></span>

设 $f(x_1,x_2)=\sigma(2x_1-x_2)$，其中 $\sigma$ 是逻辑斯谛函数。

<ol class="al">

<li>

画出 $v_1=2x_1$、$v_2=v_1-x_2$、$f=\sigma(v_2)$ 的计算图，并在点 $(1,\,1)$ 处进行前向计算。

</li>

<li>

计算所有伴随值。节点 $\sigma$ 计算其局部导数时需要哪个保存的数？

</li>

<li>

验证：$\nabla f(\mathbf{x})=\sigma'(2x_1-x_2)\,(2,\,-1)^{\top}$。

</li>

</ol>

:::loesung
(a) 这个图的边为 $x_1\to v_1$、$v_1\to v_2$、$x_2\to v_2$ 和 $v_2\to f$。在点 $(1,\,1)$ 处前向计算：$v_1=2$，$v_2=1$，$f=\sigma(1)\approx0.7311$。

(b) $\bar f=1$；$\bar v_2=\bar f\cdot f\,(1-f)\approx0.7311\cdot0.2689\approx0.1966$；$\bar v_1=\bar v_2\cdot1\approx0.1966$；$\bar x_2=\bar v_2\cdot(-1)\approx-0.1966$；$\bar x_1=\bar v_1\cdot2\approx0.3932$。由表 [4](rechengraphen.html#tab-4)，节点 $\sigma$ 计算其局部导数时只需要它自己保存的输出 $f$。

(c) 由链式法则，$\nabla f=\sigma'(2x_1-x_2)\,\nabla(2x_1-x_2)=\sigma'(2x_1-x_2)\,(2,\,-1)^{\top}$，所以在点 $(1,\,1)$ 处为 $0.1966\cdot(2,\,-1)^{\top}=(0.3932,\ -0.1966)^{\top}$。
:::
:::

:::aufgabe 练习 37 ★★ 对偶数
<span class="anker" id="aufg-37"></span>

<ol class="al">

<li>

用对偶数 $x=0+1\varepsilon$ 计算 $p(x)=(x+1)(x+2)(x+3)(x+4)$，并读出 $p(0)$ 和 $p'(0)$。

</li>

<li>

同样地，在点 $x=1+\varepsilon$ 处计算 $(x^2+1)^3$，并与链式法则比较。

</li>

</ol>

:::loesung
(a) 取 $x=\varepsilon$：

$$(1+\varepsilon)(2+\varepsilon)=2+3\varepsilon,\quad (2+3\varepsilon)(3+\varepsilon)=6+11\varepsilon,\quad (6+11\varepsilon)(4+\varepsilon)=24+50\varepsilon .$$

所以 $p(0)=24$，$p'(0)=50$；$\varepsilon$ 前面的系数恰好就是第 [9.1](rechengraphen.html#stufe-9-1) 节的算例中的 $p_k'$。

(b) $(1+\varepsilon)^2=1+2\varepsilon$，加 $1$ 得 $2+2\varepsilon$；$(2+2\varepsilon)^2=4+8\varepsilon$，$(4+8\varepsilon)(2+2\varepsilon)=8+24\varepsilon$。链式法则在点 $1$ 处给出 $3\,(x^2+1)^2\cdot2x=3\cdot4\cdot2=24$。
:::
:::

:::aufgabe 练习 38 ★★★ 选哪种模式？
<span class="anker" id="aufg-38"></span>

<ol class="al">

<li>

一个计算有 $3$ 个输入和 $1000$ 个输出，另一个有 $1000$ 个输入和 $3$ 个输出。对整个雅可比矩阵，前向模式和反向模式各需要多少遍？

</li>

<li>

设 $f(\mathbf{x})=\mathbf{c}^{\top}\mathbf{B}\mathbf{x}$，其中 $\mathbf{B}\in\mathbb{R}^{n\times n}$ 是稠密矩阵，分两级计算：$\mathbf{y}=\mathbf{B}\mathbf{x}$ 和 $f=\mathbf{c}^{\top}\mathbf{y}$。一遍前向传递计算 $\mathbf{c}^{\top}(\mathbf{B}\dot{\mathbf{x}})$，一遍反向传递计算 $\bar{\mathbf{x}}=\mathbf{B}^{\top}\mathbf{c}$。设一次矩阵-向量乘积约需 $2n^2$ 次、一次点积约需 $2n$ 次基本算术运算，对两种途径分别数一数整个梯度需要多少次基本算术运算。

</li>

<li>

为什么反向模式比前向模式需要更多内存？前向模式可以立即忘掉哪些值？

</li>

</ol>

:::loesung
(a) 有 $3$ 个输入和 $1000$ 个输出时，前向模式需要 $3$ 遍，反向模式需要 $1000$ 遍；应选前向模式。有 $1000$ 个输入和 $3$ 个输出时，情况正好相反：$1000$ 遍前向传递对 $3$ 遍反向传递。

(b) 用前向模式，梯度需要 $n$ 遍，取 $\dot{\mathbf{x}}=\mathbf{e}_1,\dots,\mathbf{e}_n$，每遍包括一次矩阵-向量乘积 $\mathbf{B}\dot{\mathbf{x}}$ 和一次点积，合计约 $n\,(2n^2+2n)\approx2n^3$ 次基本算术运算。用反向模式，$\bar{\mathbf{y}}=\mathbf{c}$，而 $\bar{\mathbf{x}}=\mathbf{B}^{\top}\mathbf{c}$ 需要一次矩阵-向量乘积，约 $2n^2$ 次；再加上前向计算，约 $2n^2+2n$ 次。因此反向模式的速度约为前向模式的 $n/2$ 倍。

(c) 反向传递需要前向计算中的值来求局部导数的值，而且它要等前向计算结束后才开始。因此所有中间值都必须保存到那时。在前向模式中，值和切线值一起向前推进；一旦节点的所有后继都已算出，两者就都不再需要，可以忘掉。
:::
:::
