---
title: 范数：向量的大小
pfad: 计算机科学 / 机器学习 / 数学基础 / 向量与矩阵
knoten: 基础篇 1：向量与矩阵
nachschlagen: ja
order: 15210400
summary: 一个向量有多大？这个问题有好几个正确答案。本节介绍其中最重要的三个，说明它们的共同点，并展示它们的用途：衡量一个误差有多大。
tags: 欧几里得范数, 长度, 归一化的, 归一化, 1-范数, 最大范数, 范数, 三角不等式
lang: zh
---

<span class="anker" id="stufe-3"></span>

:::zweck
一个向量有多大？这个问题有好几个正确答案。本节介绍其中最重要的三个，说明它们的共同点，并展示它们的用途：衡量一个误差有多大。
:::

### 欧几里得范数

<span class="anker" id="stufe-3-1"></span>

箭头最直观的大小就是它的长度。在平面上，勾股定理给出了这个长度：箭头 $(3,\,-4)^{\top}$ 是直角边为 $3$ 和 $4$ 的直角三角形的斜边，所以它的长度是 $\sqrt{3^2+4^2}=5$。在空间中，两次应用勾股定理，就得到三个平方之和的平方根。在任何维数下都使用同一个公式。

:::definition 定义 3.1 (欧几里得范数)
<span class="anker" id="satz-3-1"></span>

向量 $\mathbf{x}\in\mathbb{R}^d$ 的__欧几里得范数__为

<span class="anker" id="gl-3-1"></span>
$$\lVert\mathbf{x}\rVert_2=\sqrt{\mathbf{x}^{\top}\mathbf{x}}=\sqrt{x_1^2+x_2^2+\dots+x_d^2} . \tag{3.1}$$

在本系列中，不带下标的 $\lVert\mathbf{x}\rVert$ 总是指欧几里得范数。
:::

它也称为向量的__长度__，又因为其中的平方，称为 $L_2$ 范数。长度为 $1$ 的向量称为__归一化的__向量。把向量 $\mathbf{x}\ne\mathbf{0}$ 除以它的长度，$\mathbf{x}/\lVert\mathbf{x}\rVert$ 就是归一化的，并且指向同一方向。这一步称为__归一化__。

::::beispiel [算例]
向量 $\mathbf{x}=(3,\,-4)^{\top}$ 的长度为 $\lVert\mathbf{x}\rVert_2=5$（图 [12](#abb-12)）。归一化后为 $\mathbf{x}/5=(0.6,\ -0.8)^{\top}$。在空间中，$\lVert(1,\,2,\,2)^{\top}\rVert=\sqrt{1+4+4}=3$。

:::abbildung ml/k1rl2 12
$(3,\,-4)^{\top}$ 的欧几里得范数：各分量平方，相加，开平方。平方时负号消失。
:::
::::

⁠**简而言之：**欧几里得范数是箭头的长度，即各分量平方和的平方根。

### 1-范数

<span class="anker" id="stufe-3-2"></span>

在街道呈直角网格的城市里，出租车不能斜穿街区。要从原点到达点 $(3,\,-4)^{\top}$，它沿一个方向行驶 $3$ 个街区，再沿另一个方向行驶 $4$ 个街区，共 $7$ 个街区。1-范数衡量的就是这个长度。

:::definition 定义 3.2 (1-范数)
<span class="anker" id="satz-3-2"></span>

向量 $\mathbf{x}\in\mathbb{R}^d$ 的__1-范数__为

<span class="anker" id="gl-3-2"></span>
$$\lVert\mathbf{x}\rVert_1=|x_1|+|x_2|+\dots+|x_d|=\sum_{j=1}^d|x_j| . \tag{3.2}$$
:::

它也称为 $L_1$ 范数，或者按照曼哈顿的街道网格称为曼哈顿范数。

::::beispiel [算例]
对 $\mathbf{x}=(3,\,-4)^{\top}$，$\lVert\mathbf{x}\rVert_1=7$（图 [13](#abb-13)），而 $\lVert(1,\,2,\,2)^{\top}\rVert_1=1+2+2=5$。

:::abbildung ml/k1rl1 13
$\mathbf{x}=(3,\,-4)^{\top}$ 的 1-范数：把各分量的绝对值相加。
:::

这里 1-范数比欧几里得长度大，因为沿街道绕行的路比直线长。
::::

⁠**简而言之：**1-范数把各分量的绝对值相加；它是穿过直角街道网格的路程。

### 最大范数

<span class="anker" id="stufe-3-3"></span>

在质量检验中，往往只有最差的那个偏差才重要。一个零件有三个尺寸，每个尺寸与标称值的偏差最多只能是 $0.1$ mm。零件是否合格，只由三个偏差中最大的那个决定。

:::definition 定义 3.3 (最大范数)
<span class="anker" id="satz-3-3"></span>

向量 $\mathbf{x}\in\mathbb{R}^d$ 的__最大范数__是各分量绝对值中的最大者：

<span class="anker" id="gl-3-3"></span>
$$\lVert\mathbf{x}\rVert_\infty=\max_{j=1,\dots,d}|x_j| . \tag{3.3}$$
:::

它也称为 $L_\infty$ 范数。使用无穷符号的原因见下一小节。

::::beispiel [算例]
$\lVert(3,\,-4)^{\top}\rVert_\infty=4$，$\lVert(1,\,2,\,2)^{\top}\rVert_\infty=2$。如果一个零件的偏差为 $(0.05,\ -0.08,\ 0.02)$ mm，它们的最大范数是 $0.08$ mm，零件合格。
::::

⁠**简而言之：**最大范数是各分量绝对值中的最大者，即最差的那个单项偏差。

### 什么是范数

<span class="anker" id="stufe-3-4"></span>

这三种范数的衡量方式不同，但它们共有三条性质，这是人们对任何大小的度量都会期待的。只有零向量的大小为零。长一倍的向量就大一倍。绕道永远不会比直达的路更短。

:::definition 定义 3.4 (范数)
<span class="anker" id="satz-3-4"></span>

$\mathbb{R}^d$ 上的__范数__给每个向量 $\mathbf{x}$ 指定一个实数 $\lVert\mathbf{x}\rVert$，使得对所有 $\mathbf{u},\mathbf{v},\mathbf{x}\in\mathbb{R}^d$ 和所有标量 $c$ 有：

<ol>

<li>

$\lVert\mathbf{x}\rVert\ge0$，并且只有当 $\mathbf{x}=\mathbf{0}$ 时才有 $\lVert\mathbf{x}\rVert=0$；

</li>

<li>

$\lVert c\,\mathbf{x}\rVert=|c|\,\lVert\mathbf{x}\rVert$；

</li>

<li>

$\lVert\mathbf{u}+\mathbf{v}\rVert\le\lVert\mathbf{u}\rVert+\lVert\mathbf{v}\rVert$ （__三角不等式__）。

</li>

</ol>
:::

三角不等式得名于由箭头 $\mathbf{u}$、$\mathbf{v}$ 和 $\mathbf{u}+\mathbf{v}$ 构成的三角形：边 $\mathbf{u}+\mathbf{v}$ 永远不会比另外两边之和更长。

**$p$-范数。** 1-范数和欧几里得范数是一整族范数中的两个特例。对每个数 $p\ge1$，__$p$-范数__为

<span class="anker" id="gl-3-4"></span>
$$\lVert\mathbf{x}\rVert_p=\Bigl(\sum_{j=1}^d|x_j|^p\Bigr)^{1/p} . \tag{3.4}$$

$p=1$ 时它是 1-范数，$p=2$ 时它是欧几里得范数。$p$ 越大，最大的分量在和中的支配作用就越强。当 $p\to\infty$ 时，只剩下这个分量；这就是最大范数记作 $\lVert\cdot\rVert_\infty$ 的原因。

**单位球。** 观察所有大小为 $1$ 的向量构成的集合，就能看出一个范数是怎样衡量的。这个集合称为该范数的__单位球__，尽管它不一定是球形（图 [14](#abb-14)）。对欧几里得范数，它在平面上是半径为 $1$ 的圆。对 1-范数，它是菱形 $|x_1|+|x_2|=1$：在每个象限中它是一条线段，例如当 $x_1,x_2\ge0$ 时为 $x_1+x_2=1$。对最大范数，它是顶点为 $(\pm1,\,\pm1)$ 的正方形，因为在这个正方形上，两个分量中较大的那个的绝对值恰好为 $1$。

:::abbildung ml/k1einheitskugeln 14
平面上三种范数的单位球：1-范数的菱形（左，橙色）、欧几里得范数的圆（中，蓝色）和最大范数的正方形（右，绿色）；每幅图中都用灰色画出另外两种，以供比较。三者都经过点 $(\pm1,\,0)$ 和 $(0,\,\pm1)$。
:::

::::beispiel [算例]
对 $\mathbf{x}=(3,\,-4)^{\top}$，得到 $\lVert\mathbf{x}\rVert_1=7$，$\lVert\mathbf{x}\rVert_2=5$，$\lVert\mathbf{x}\rVert_3=91^{1/3}\approx4.498$，$\lVert\mathbf{x}\rVert_{10}=1\,107\,625^{1/10}\approx4.022$（图 [15](#abb-15)），以及 $\lVert\mathbf{x}\rVert_\infty=4$。随着 $p$ 增大，$p$-范数趋近于各分量绝对值中的最大者，这里是 $4$。原因在和中已经可以看出：$p=10$ 时，$4^{10}$ 几乎是 $3^{10}$ 的十八倍，和的方根几乎不比单独 $4^{10}$ 的方根大。

:::abbildung ml/k1rlp 15
$\mathbf{x}=(3,\,-4)^{\top}$ 的两个 $p$-范数，$p=3$ 和 $p=10$。$p$ 越大，最大分量那一项的支配作用就越强。
:::
::::

1-范数满足条件 (N1) 至 (N3)，这可以直接验证：(N1) 和 (N2) 成立，因为 $|x_j|\ge0$ 且 $|c\,x_j|=|c|\,|x_j|$。(N3) 由数的三角不等式 $|u_j+v_j|\le|u_j|+|v_j|$ 对所有 $j$ 求和得出。最大范数同理。对欧几里得范数，三角不等式在直观上是显然的，因为两点之间的直达路线永远不会比经过第三点的绕行路线更长。

⁠**简而言之：**范数衡量向量的大小，使得只有零向量的大小为零、倍数相应地增大，并且三角不等式成立；$p$-范数构成一族，其中包括 $L_1$、$L_2$ 和 $L_\infty$。

:::hintergrund 为什么要求 $p\ge1$，以及为什么“零范数”不是范数
当 $p<1$ 时，式 [(3.4)](#gl-3-4) 违反三角不等式。取 $p=\tfrac12$，有 $\lVert(1,0)^{\top}\rVert_{1/2}=1$ 和 $\lVert(0,1)^{\top}\rVert_{1/2}=1$，但 $\lVert(1,1)^{\top}\rVert_{1/2}=(1+1)^2=4>1+1$。它的“单位球”向内凹陷，呈星形。

人们常读到所谓的“$L_0$ 范数”：不为零的分量的个数。它很适合用来衡量一个向量实际用到了多少个特征。但它不是范数，因为它违反 (N2)：向量 $2\mathbf{x}$ 的非零分量与 $\mathbf{x}$ 一样多，而不是两倍。
:::

:::hintergrund 并非每个范数都来自点积
欧几里得范数是由点积构造的，$\lVert\mathbf{x}\rVert^2=\mathbf{x}^{\top}\mathbf{x}$。由此可以得出一个称为平行四边形恒等式的等式。用点积的运算规则展开，得到

$$\lVert\mathbf{u}+\mathbf{v}\rVert^2=\lVert\mathbf{u}\rVert^2+2\,\mathbf{u}^{\top}\mathbf{v}+\lVert\mathbf{v}\rVert^2 ,\qquad \lVert\mathbf{u}-\mathbf{v}\rVert^2=\lVert\mathbf{u}\rVert^2-2\,\mathbf{u}^{\top}\mathbf{v}+\lVert\mathbf{v}\rVert^2 ,$$

两行相加，得到 $\lVert\mathbf{u}+\mathbf{v}\rVert^2+\lVert\mathbf{u}-\mathbf{v}\rVert^2=2\lVert\mathbf{u}\rVert^2+2\lVert\mathbf{v}\rVert^2$：在平行四边形中，两条对角线的平方和等于四条边的平方和。每个由点积导出的范数都必须满足这个等式。1-范数不满足：取 $\mathbf{u}=\mathbf{e}_1$ 和 $\mathbf{v}=\mathbf{e}_2$，左边为 $\lVert(1,1)^{\top}\rVert_1^2+\lVert(1,-1)^{\top}\rVert_1^2=4+4=8$，右边却是 $2+2=4$。所以不存在以 1-范数为长度的点积。因此，1-范数不能像点积那样衡量角度。
:::

### 误差向量及其大小

<span class="anker" id="stufe-3-5"></span>

模型给出预测值，而到了某个时候你会得知实际值。这时你想知道预测得有多好。每个样本都有一个偏差，这些偏差构成一个向量。它的范数是整体误差大小的一种度量。

:::definition 定义 3.5 (误差向量)
<span class="anker" id="satz-3-5"></span>

设 $\hat y_1,\dots,\hat y_N$ 是一个模型对 $N$ 个样本的预测值，$y_1,\dots,y_N$ 是实际值，则向量

<span class="anker" id="gl-3-5"></span>
$$\hat{\mathbf{y}}-\mathbf{y}=(\hat y_1-y_1,\,\dots,\,\hat y_N-y_N)^{\top} \tag{3.5}$$

称为__误差向量__。这里 $\hat{\mathbf{y}}=(\hat y_1,\dots,\hat y_N)^{\top}$ 是预测值向量，$\mathbf{y}=(y_1,\dots,y_N)^{\top}$ 是实际值向量。
:::

对误差向量使用哪种范数，取决于你最担心哪种误差。符号不起作用，因为每种范数给 $\mathbf{y}-\hat{\mathbf{y}}$ 的大小都与 $\hat{\mathbf{y}}-\mathbf{y}$ 相同。

::::beispiel [算例]
四套公寓已经售出，实际价格为 $\mathbf{y}=(200,\,130,\,290,\,240)^{\top}$ 千欧元。两位评估师 A 和 B 事先作过估价：

$$\hat{\mathbf{y}}_{\mathrm A}=(210,\,120,\,300,\,230)^{\top},\qquad \hat{\mathbf{y}}_{\mathrm B}=(200,\,130,\,290,\,280)^{\top}.$$

他们的误差向量为 $\hat{\mathbf{y}}_{\mathrm A}-\mathbf{y}=(10,\,-10,\,10,\,-10)^{\top}$ 和 $\hat{\mathbf{y}}_{\mathrm B}-\mathbf{y}=(0,\,0,\,0,\,40)^{\top}$。评估师 A 每次都偏差一点；评估师 B 三次完全准确，一次偏差很大。三种范数的评判各不相同（表 [2](#tab-2)）。欧几里得范数的计算见图 [16](#abb-16)。

:::abbildung ml/k1rfehler 16
两个误差向量的欧几里得范数，单位为千欧元。B 的单个大误差对平方和的贡献为 $1\,600$，是 A 的四个小误差合起来的四倍。
:::

<span class="anker" id="tab-2"></span>

**表 2:** 两位评估师的误差向量的范数，单位为千欧元。

|  | $\lVert\cdot\rVert_1$ | $\lVert\cdot\rVert_2$ | $\lVert\cdot\rVert_\infty$ |
|---|---|---|---|
| 评估师 A，$\hat{\mathbf{y}}_{\mathrm A}-\mathbf{y}$ | $40$ | $\sqrt{4\cdot100}=20$ | $10$ |
| 评估师 B，$\hat{\mathbf{y}}_{\mathrm B}-\mathbf{y}$ | $40$ | $\sqrt{1600}=40$ | $40$ |

按 1-范数，两人一样好：每人总共偏差 $40$ 千欧元。按欧几里得范数，A 的误差只有 B 的一半；按最大范数，只有 B 的四分之一。如果你认为每一千欧元的偏差都同样糟糕，无论出在哪套公寓上，就用 $L_1$ 衡量。如果你认为一个大的离群值比许多小误差更糟，就用 $L_2$ 衡量。如果你只担心最坏的情况，就用 $L_\infty$ 衡量。
::::

⁠**简而言之：**误差向量汇集了所有预测值的偏差；它的范数衡量误差的大小，而范数的选择决定了哪些误差最受重视。

:::hintergrund 为什么平方和重罚大误差，却几乎忽略小误差
在欧几里得范数中，每个偏差都以平方的形式进入。偏差 $0.1$ 贡献 $0.01$，而偏差 $10$ 贡献 $100$。平方使小的数更小，使大的数更大。因此，单个大误差 $40$ 贡献 $1600$，是四个各为 $10$ 的误差合起来的四倍。与此相反，1-范数处处以同样的速度增长：每一单位的偏差代价相同，不论它属于小误差还是大误差。这也是它能清楚地区分“恰好为零”和“略有偏差”的原因，而平方和对两者几乎不加区分。需要哪种性质，取决于任务，这也正是存在多种范数的原因。
:::

### 有效值

<span class="anker" id="stufe-3-6"></span>

欧几里得范数随分量个数的增加而增大。如果用四套公寓评价一位评估师，用四百套评价另一位，后者的误差向量要长得多，即使每套公寓的估价同样好。要按每个样本比较误差，就必须消除分量个数的影响。

:::definition 定义 3.6 (有效值)
<span class="anker" id="satz-3-6"></span>

向量 $\mathbf{x}\in\mathbb{R}^n$ 的__有效值__（均方根值）为

<span class="anker" id="gl-3-6"></span>
$$\operatorname{rms}(\mathbf{x})=\frac{\lVert\mathbf{x}\rVert}{\sqrt n}=\sqrt{\frac1n\sum_{i=1}^nx_i^2} . \tag{3.6}$$
:::

缩写 rms 代表“root mean square”：各平方的均值的平方根。有效值是一个分量的典型大小。如果所有分量的绝对值都是 $a$，有效值就恰好是 $a$。

这个名称在电工学中很常见：交流电压的有效值是其平方的时间平均值的平方根。对采样信号，式 [(3.6)](#gl-3-6) 是同样的计算，只是用采样值代替了积分。如果在正弦的恰好一个周期内、在 $n\ge3$ 个等间距点上采样，得到的甚至恰好就是正弦的有效值 $1/\sqrt2$。

::::beispiel [算例]
上一小节中两位评估师的误差向量的有效值为 $\operatorname{rms}(\hat{\mathbf{y}}_{\mathrm A}-\mathbf{y})=20/\sqrt4=10$ 和 $\operatorname{rms}(\hat{\mathbf{y}}_{\mathrm B}-\mathbf{y})=40/\sqrt4=20$ 千欧元：A 的典型偏差是 $10$ 千欧元。振幅为 $1$ 的正弦，在一个周期内的四个等间距点上采样，得到采样值 $\mathbf{x}=(0,\,1,\,0,\,-1)^{\top}$，有效值为 $1/\sqrt2\approx0.707$（图 [17](#abb-17)）。

:::abbildung ml/k1rrms 17
采样正弦的有效值：各平方相加，除以分量个数，再开平方。
:::
::::

⁠**简而言之：**有效值 $\lVert\mathbf{x}\rVert/\sqrt n$ 是一个分量的典型大小，它使分量个数不同的向量可以相互比较。

:::hintergrund 有多少个分量可以很大？
有效值限制了有多少个分量能有较大的绝对值。如果 $n$ 个分量中有 $k$ 个的绝对值至少为 $a>0$，那么仅这 $k$ 个分量对平方和的贡献就至少是 $k\,a^2$。整个平方和是 $n\operatorname{rms}(\mathbf{x})^2$，所以 $k\,a^2\le n\operatorname{rms}(\mathbf{x})^2$，即

$$\frac kn\le\Bigl(\frac{\operatorname{rms}(\mathbf{x})}{a}\Bigr)^2 .$$

所以，绝对值至少为 $a$ 的分量最多只占比例 $(\operatorname{rms}/a)^2$。能达到有效值两倍的分量最多占四分之一，能达到有效值十倍的最多占百分之一。对 $\operatorname{rms}=20$ 的评估师 B，最多 $(20/30)^2=4/9\approx44$ % 的误差可以达到 $30$ 或更大；实际上是四个中的一个，即 $25$ %。这个估计称为切比雪夫不等式。
:::

:::aufgabe 练习 7 ★ 计算范数
<span class="anker" id="aufg-7"></span>

设 $\mathbf{x}=(2,\,-1,\,0,\,2)^{\top}$。

<ol class="al">

<li>

计算 $\lVert\mathbf{x}\rVert_1$、$\lVert\mathbf{x}\rVert_2$、$\lVert\mathbf{x}\rVert_3$ 和 $\lVert\mathbf{x}\rVert_\infty$，以及归一化向量 $\mathbf{x}/\lVert\mathbf{x}\rVert$。

</li>

<li>

验证 $\lVert\mathbf{x}\rVert_\infty\le\lVert\mathbf{x}\rVert_2\le\lVert\mathbf{x}\rVert_1$。解释为什么这个大小顺序对每个向量都成立。

</li>

</ol>

:::loesung
(a) $\lVert\mathbf{x}\rVert_1=2+1+0+2=5$，$\lVert\mathbf{x}\rVert_2=\sqrt{4+1+0+4}=3$，$\lVert\mathbf{x}\rVert_3=(8+1+0+8)^{1/3}=17^{1/3}\approx2.571$，$\lVert\mathbf{x}\rVert_\infty=2$。归一化向量为 $\mathbf{x}/3=(\tfrac23,\,-\tfrac13,\,0,\,\tfrac23)^{\top}$，其长度为 $\sqrt{(4+1+4)/9}=1$。

(b) 有 $2\le3\le5$，而 $\lVert\mathbf{x}\rVert_3$ 的值 $2.571$ 也介于两者之间。一般地：若 $|x_k|$ 是各分量绝对值中的最大者，则 $\lVert\mathbf{x}\rVert_\infty^2=x_k^2\le\sum_jx_j^2=\lVert\mathbf{x}\rVert_2^2$，因为这个和包含 $x_k^2$，其余各项都非负。而 $\lVert\mathbf{x}\rVert_1^2=\bigl(\sum_j|x_j|\bigr)^2=\sum_jx_j^2+\sum_{j\ne l}|x_j|\,|x_l|\ge\lVert\mathbf{x}\rVert_2^2$，因为交叉项都非负。直观地说：直线距离永远不会长于穿过街道网格的路程，也永远不会短于其中最长的那一段。
:::
:::

:::aufgabe 练习 8 ★★ 房产经纪人的估价有多准？
<span class="anker" id="aufg-8"></span>

第 [2.2](das-skalarprodukt.html#stufe-2-2) 小节中的房产经纪人给出的预测值为 $\hat{\mathbf{y}}=(188,\,126,\,286,\,232)^{\top}$；实际价格为 $\mathbf{y}=(200,\,130,\,290,\,240)^{\top}$ 千欧元。

<ol class="al">

<li>

计算误差向量、它的三种范数和有效值。她对哪套公寓的估价偏差最大？

</li>

<li>

关于符号，你注意到了什么？从现在起，房产经纪人在每个预测值上都加 $7$ 千欧元。计算新的误差向量及其范数。按三种范数来看，她是否都有所改进？

</li>

</ol>

:::loesung
(a) 误差向量为 $\hat{\mathbf{y}}-\mathbf{y}=(188-200,\ 126-130,\ 286-290,\ 232-240)^{\top}=(-12,\,-4,\,-4,\,-8)^{\top}$。它的范数为：$\lVert\cdot\rVert_1=28$，$\lVert\cdot\rVert_2=\sqrt{144+16+16+64}=\sqrt{240}\approx15.49$，$\lVert\cdot\rVert_\infty=12$，有效值为 $\sqrt{240}/2\approx7.75$ 千欧元。她对公寓 1 的估价偏差最大，相差 $12$ 千欧元。

(b) 所有误差都是负的：房产经纪人一贯估得偏低，她的误差含有直流分量。每个预测值加上 $7$ 千欧元之后，误差向量变为 $(-5,\,3,\,3,\,-1)^{\top}$，其中 $\lVert\cdot\rVert_1=12$，$\lVert\cdot\rVert_2=\sqrt{25+9+9+1}=\sqrt{44}\approx6.63$，$\lVert\cdot\rVert_\infty=5$，有效值为 $\sqrt{44}/2\approx3.32$。按全部三种范数，她都有所改进。加上的 $7$ 恰好是误差绝对值的均值，$(12+4+4+8)/4=7$：它去掉了误差的直流分量，只留下交流分量。
:::
:::
