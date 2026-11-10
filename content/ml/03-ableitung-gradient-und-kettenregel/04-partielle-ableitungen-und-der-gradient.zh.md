---
title: 偏导数与梯度
pfad: 计算机科学 / 机器学习 / 数学基础 / 导数、梯度与链式法则
adresse: informatik/machine-learning/mathematische-grundlagen/ableitung-gradient-und-kettenregel
knoten: 第 3 章：导数、梯度与链式法则
nachschlagen: ja
order: 15230400
summary: 如果一个数取决于许多输入，可以每次只把一个输入稍作改变，而把其他输入固定。这样得到的斜率称为偏导数。它们合在一起构成一个向量，即梯度；有了梯度，第 1 节中的线性近似就变成用平面作的近似。本节最后说明这种近似在什么情况下确实成立。
tags: d 元函数, 水平集, 等高线, 截线, 偏导数, 梯度, 切平面, 可微
lang: zh
---

<span class="anker" id="stufe-3"></span>

:::zweck
如果一个数取决于许多输入，可以每次只把一个输入稍作改变，而把其他输入固定。这样得到的斜率称为偏导数。它们合在一起构成一个向量，即梯度；有了梯度，第 [1](die-ableitung.html#stufe-1) 节中的线性近似就变成用平面作的近似。本节最后说明这种近似在什么情况下确实成立。
:::

### 多元函数

<span class="anker" id="stufe-3-1"></span>

在[第 1 章第 2.2 节](/wissen/zh/informatik/machine-learning/mathematische-grundlagen/vektoren-und-matrizen/das-skalarprodukt.html#stufe-2-2)中，对一套公寓的预测值是各特征的加权和 $\hat y=\mathbf{w}^{\top}\mathbf{x}$。如果把特征固定，问预测值怎样依赖于权重，那么 $\hat y$ 就是一个依赖于 $d$ 个数 $w_1,\dots,w_d$ 的数。同样，[第 2 章第 5.1 节](/wissen/zh/informatik/machine-learning/mathematische-grundlagen/projektion-eigenwerte-und-zerlegungen/quadratische-formen.html#stufe-5-1)中的二次型 $\mathbf{x}^{\top}\mathbf{A}\mathbf{x}$ 依赖于 $\mathbf{x}$ 的所有分量。这样的对应关系需要一个专门的概念。

:::definition 定义 3.1 (多元函数、等高线)
<span class="anker" id="satz-3-1"></span>

函数 $f:\mathbb{R}^d\to\mathbb{R}$ 把每个向量 $\mathbf{x}\in\mathbb{R}^d$ 对应到一个数 $f(\mathbf{x})=f(x_1,\dots,x_d)$；它称为__$d$ 元函数__。对一个数 $c$，满足 $f(\mathbf{x})=c$ 的所有 $\mathbf{x}$ 组成的集合称为 $f$ 在值 $c$ 处的__水平集__。当 $d=2$ 时，它通常是一条曲线，这时称为__等高线__。
:::

对两个变量，可以借助地形的图景来理解。向量 $\mathbf{x}=(x_1,\,x_2)^{\top}$ 是地图上的一个位置，$f(\mathbf{x})$ 是这个位置上地面的高度。$f$ 的图像，即空间中点 $(x_1,\,x_2,\,f(x_1,x_2))$ 的集合，就是地面的表面。等高线就像登山地图上那样，把高度相同的所有位置连起来。等高线密的地方，地面陡；等高线疏的地方，地面平缓。变量多于两个时就没有这个图景了，但计算方法不变。

::::beispiel [算例]
在第 [3](#stufe-3) 节到第 [8](die-hesse-matrix-und-die-quadratische-naherung.html#stufe-8) 节中，我们一直使用函数

<span class="anker" id="gl-3-1"></span>
$$f(\mathbf{x})=x_1^2\,x_2+x_2^2 . \tag{3.1}$$

在点 $\mathbf{x}=(1,\,2)^{\top}$ 处，$f(1,2)=1\cdot2+4=6$。等高线 $f=6$ 由满足 $x_1^2x_2+x_2^2=6$ 的所有点组成。$x_1=0$ 时，这个方程变为 $x_2^2=6$，所以点 $(0,\ \sqrt6)^{\top}\approx(0,\ 2.449)^{\top}$ 在这条等高线上。一般地，对每个固定的 $x_1$，这个方程都是关于 $x_2$ 的二次方程，它的正解 $x_2=\tfrac12\bigl(\sqrt{x_1^4+24}-x_1^2\bigr)$ 描述了 $x_1$ 轴上方的整条等高线；$x_1=1$ 时，它给出 $\tfrac12(5-1)=2$。图 [6](#abb-6) 画出了几条等高线。
::::

⁠**简而言之：**$d$ 元函数把每个向量对应到一个数；有两个变量时，可以把它想象成一片地形，它的等高线把高度相同的位置连起来。

### 偏导数

<span class="anker" id="stufe-3-2"></span>

如果只改变一个输入，$f$ 的反应有多强？把其他所有输入固定，$f$ 就成了一个普通的一元函数。在地形的图景中，就是沿一条平行于某根坐标轴的直线把地面切开。切面的边缘是一条曲线，即__截线__，它的斜率就是要求的灵敏度。

:::definition 定义 3.2 (偏导数)
<span class="anker" id="satz-3-2"></span>

$f:\mathbb{R}^d\to\mathbb{R}$ 在点 $\mathbf{x}$ 处对 $x_j$ 的__偏导数__为

<span class="anker" id="gl-3-2"></span>
$$\frac{\partial f}{\partial x_j}(\mathbf{x})=\lim_{h\to0}\frac{f(\mathbf{x}+h\,\mathbf{e}_j)-f(\mathbf{x})}{h}, \tag{3.2}$$

前提是这个极限存在。其中 $\mathbf{e}_j$ 是[第 1 章第 1.6 节](/wissen/zh/informatik/machine-learning/mathematische-grundlagen/vektoren-und-matrizen/vektoren-daten-als-zahlenlisten.html#stufe-1-6)中的第 $j$ 个单位向量。也简写作 $\partial_jf(\mathbf{x})$。
:::

向量 $\mathbf{x}+h\,\mathbf{e}_j$ 与 $\mathbf{x}$ 只在第 $j$ 个分量上不同，相差 $h$。所以这个定义就是第 [1.2](die-ableitung.html#stufe-1-2) 节中的普通导数，只不过用于把除 $x_j$ 以外的所有变量都固定后得到的函数。由此得到计算规则：对 $x_j$ 求导，把其他所有变量都当作常数。符号 $\partial$ 是一个圆体的 d，它提醒人们只有一部分变量在变动。

::::beispiel [算例]
对于 $f(\mathbf{x})=x_1^2x_2+x_2^2$，对 $x_1$ 求导时把变量 $x_2$ 当作常数，反之亦然：

$$\frac{\partial f}{\partial x_1}=2x_1\,x_2,\qquad \frac{\partial f}{\partial x_2}=x_1^2+2x_2 .$$

在点 $(1,\,2)$ 处，得到 $4$ 和 $5$。截线显示了同样的结果（图 [6](#abb-6)）：把 $x_2=2$ 固定，剩下 $f(x_1,2)=2x_1^2+4$，它在 $x_1=1$ 处的斜率为 $4x_1=4$。把 $x_1=1$ 固定，剩下 $f(1,x_2)=x_2+x_2^2$，它在 $x_2=2$ 处的斜率为 $1+2x_2=5$。

:::abbildung ml/k3schnitt 6
偏导数是截线的斜率：$f(\mathbf{x})=x_1^2x_2+x_2^2$ 在点 $(1,\,2)$ 处。(a) 值为 $2$、$4$、$6$（黑色）、$8$ 和 $10$ 的等高线，以及经过 $(1,\,2)$ 的两条截取直线。(b) 沿蓝色直线 $x_2=2$，地面按 $2x_1^2+4$ 起伏，在 $x_1=1$ 处斜率为 $4$。(c) 沿红色直线 $x_1=1$，地面按 $x_2+x_2^2$ 起伏，在 $x_2=2$ 处斜率为 $5$。
:::
::::

⁠**简而言之：**偏导数 $\partial f/\partial x_j$ 是沿 $x_j$ 轴方向的斜率：对 $x_j$ 求导，把其他所有变量固定。

### 梯度

<span class="anker" id="stufe-3-3"></span>

$d$ 元函数在每一点都有 $d$ 个偏导数。把它们合成一个向量，就能像对 $\mathbf{x}$ 本身那样用它们计算。

:::definition 定义 3.3 (梯度)
<span class="anker" id="satz-3-3"></span>

如果 $f:\mathbb{R}^d\to\mathbb{R}$ 的所有偏导数在点 $\mathbf{x}$ 处都存在，就称列向量

<span class="anker" id="gl-3-3"></span>
$$\nabla f(\mathbf{x})=\begin{pmatrix}\partial_1f(\mathbf{x})\\ \vdots\\ \partial_df(\mathbf{x})\end{pmatrix}\in\mathbb{R}^d \tag{3.3}$$

为 $f$ 在点 $\mathbf{x}$ 处的__梯度__。符号 $\nabla$ 读作“nabla”。
:::

梯度的形状与 $\mathbf{x}$ 相同：每个变量对应一个元素，写成一列。这个约定在本章中始终适用；第 [7](ableiten-nach-vektoren-und-matrizen.html#stufe-7) 节还会回到这一点，因为并不是所有书都这样约定。给每个点 $\mathbf{x}$ 配上它的梯度，就得到一个箭头场，地图上的每个位置都有一个箭头。这些箭头指向哪里，由第 [4](richtungsableitung-und-steilster-anstieg.html#stufe-4) 节说明。

::::beispiel [算例]
对于 $f(\mathbf{x})=x_1^2x_2+x_2^2$，有

$$\nabla f(\mathbf{x})=\begin{pmatrix}2x_1x_2\\ x_1^2+2x_2\end{pmatrix},\qquad \nabla f(1,2)=\begin{pmatrix}4\\5\end{pmatrix},\qquad \nabla f(0,1)=\begin{pmatrix}0\\2\end{pmatrix} .$$

对于平方和 $f(\mathbf{x})=x_1^2+x_2^2+x_3^2$，有 $\nabla f(\mathbf{x})=(2x_1,\,2x_2,\,2x_3)^{\top}=2\mathbf{x}$。
::::

⁠**简而言之：**梯度是由所有偏导数组成的列向量，形状与 $\mathbf{x}$ 相同。

### 空间中的线性近似

<span class="anker" id="stufe-3-4"></span>

对一元函数，切线在某一点附近代替函数。有两个变量时，代替它的是一个平面。在放大镜下，光滑的地面在某一点附近看起来像一块倾斜的平板：这就是__切平面__。经过点 $(\mathbf{x},\,f(\mathbf{x}))$ 的平面形如 $f(\mathbf{x})+m_1h_1+m_2h_2$，其中 $\mathbf{h}=(h_1,\,h_2)^{\top}$ 是地图上的位移，$m_1$、$m_2$ 是平板沿两根坐标轴方向的倾斜度。要让它贴合地面，它沿坐标轴的倾斜度必须与截线的斜率一致，即 $m_j=\partial_jf(\mathbf{x})$。

由此得到多元函数的线性近似：

<span class="anker" id="gl-3-4"></span>
$$f(\mathbf{x}+\mathbf{h})\approx f(\mathbf{x})+\nabla f(\mathbf{x})^{\top}\mathbf{h}=f(\mathbf{x})+\sum_{j=1}^d\partial_jf(\mathbf{x})\,h_j . \tag{3.4}$$

这个公式说明了一件值得注意的事：如果把几个输入同时改变一小点，**它们的作用就相加**。每个变量贡献 $\partial_jf\cdot h_j$，就好像只有它自己被改变了一样。对于大的变化，这就不再成立了，因为这时各变量会相互影响彼此的作用，例如在 $x_1^2x_2$ 中。对于小的变化，这些交互作用是小量的乘积，比各自的作用消失得更快，正像乘积法则中角上的小块一样。

::::beispiel [算例]
对于 $f(\mathbf{x})=x_1^2x_2+x_2^2$ 在点 $\mathbf{x}=(1,\,2)^{\top}$ 处、位移 $\mathbf{h}=(0.01,\ 0.02)^{\top}$，有

$$f(\mathbf{x}+\mathbf{h})\approx f(\mathbf{x})+\nabla f(\mathbf{x})^{\top}\mathbf{h}=6+4\cdot0.01+5\cdot0.02=6+0.14=6.14 .$$

精确值是 $f(1.01,\ 2.02)=1.0201\cdot2.02+2.02^2=2.060602+4.0804=6.141002$。误差 $0.001002$ 远小于变化量 $0.14$ 本身。图 [7](#abb-7) 逐步展示了这个点积。

:::abbildung ml/k3rlinear 7
线性近似中的变化量，即梯度与位移的点积：每个变量贡献它的偏导数乘以它自己的变化量。
:::
::::

⁠**简而言之：**在 $\mathbf{x}$ 附近，$f(\mathbf{x}+\mathbf{h})\approx f(\mathbf{x})+\nabla f(\mathbf{x})^{\top}\mathbf{h}$：变化很小时，各变量的作用相加。

### 可微性

<span class="anker" id="stufe-3-5"></span>

到目前为止，近似式 [(3.4)](#gl-3-4) 只是说得通而已。对一元函数，它由导数的存在得出。对多元函数，仅有偏导数存在还不足以保证它成立，下面的反例说明了这一点。因此，要直接要求这个近似本身成立：它的误差应当比位移消失得更快，就像在式 [(1.4)](die-ableitung.html#gl-1-4) 中误差 $r(h)$ 比 $h$ 消失得更快一样。不能除以一个向量；因此不是除以 $h$，而是除以[第 1 章第 3.1 节](/wissen/zh/informatik/machine-learning/mathematische-grundlagen/vektoren-und-matrizen/normen-die-groe-eines-vektors.html#stufe-3-1)中的长度 $\lVert\mathbf{h}\rVert$。

:::definition 定义 3.4 (可微性)
<span class="anker" id="satz-3-4"></span>

如果存在一个向量 $\mathbf{g}\in\mathbb{R}^d$ 满足下式，就称函数 $f:\mathbb{R}^d\to\mathbb{R}$ 在点 $\mathbf{x}$ 处__可微__：

<span class="anker" id="gl-3-5"></span>
$$\lim_{\mathbf{h}\to\mathbf{0}}\frac{f(\mathbf{x}+\mathbf{h})-f(\mathbf{x})-\mathbf{g}^{\top}\mathbf{h}}{\lVert\mathbf{h}\rVert}=0 . \tag{3.5}$$

极限 $\mathbf{h}\to\mathbf{0}$ 的意思是：只要 $\lVert\mathbf{h}\rVert$ 足够小且 $\mathbf{h}\ne\mathbf{0}$，这个商就任意接近 $0$，不论 $\mathbf{h}$ 从哪个方向趋近。
:::

:::satz 定理 3.5 (可微意味着：梯度与线性近似)
<span class="anker" id="satz-3-5"></span>

如果 $f$ 在点 $\mathbf{x}$ 处可微，那么所有偏导数在该点都存在，并且式 [(3.5)](#gl-3-5) 中的向量就是梯度：$\mathbf{g}=\nabla f(\mathbf{x})$。反过来，如果所有偏导数在 $\mathbf{x}$ 附近都存在，并且在点 $\mathbf{x}$ 处连续，那么 $f$ 在点 $\mathbf{x}$ 处可微。
:::

:::beweis 这个向量就是梯度
在式 [(3.5)](#gl-3-5) 中特别地取 $\mathbf{h}=t\,\mathbf{e}_j$，其中 $t\ne0$ 是一个数；于是 $\lVert\mathbf{h}\rVert=|t|$，$\mathbf{g}^{\top}\mathbf{h}=t\,g_j$。商变为 $\frac{f(\mathbf{x}+t\mathbf{e}_j)-f(\mathbf{x})-t\,g_j}{|t|}$，并且趋于 $0$。那么 $\frac{f(\mathbf{x}+t\mathbf{e}_j)-f(\mathbf{x})}{t}-g_j$ 也趋于 $0$，因为这个数的绝对值与前者相同。所以对 $x_j$ 的偏导数存在，并且等于 $g_j$。这对每个 $j$ 都成立。
:::

在实践中，重要的是第二个结论。多项式、指数函数、逻辑斯谛函数，以及由它们通过基本算术运算和复合构造出来的一切函数，在它们有定义的地方都有连续的偏导数。因此这样的函数是可微的，式 [(3.4)](#gl-3-4) 对它们成立。本章中的例外是折点，例如 $|x|$ 或 $\max(x,\,0)$ 中的折点。

:::warnung 仅有偏导数还不够
函数 $f(x_1,x_2)=\dfrac{x_1x_2}{x_1^2+x_2^2}$，补充定义 $f(0,0)=0$，在两根坐标轴上都为零，因为那里 $x_1x_2=0$。所以它沿坐标轴经过原点的截线是水平的：$\partial_1f(0,0)=\partial_2f(0,0)=0$，原点处的梯度是 $\mathbf{0}$。因此线性近似预测 $f$ 在原点附近几乎为 $0$。但在对角线 $x_1=x_2=t$（$t\ne0$）上，$f(t,t)=t^2/(2t^2)=\tfrac12$，不论 $t$ 多小都是如此。这个函数在原点处跳跃，没有一个平面能贴合它。尽管两个偏导数都存在，它在原点处却不可微。因此，要从梯度的存在推出线性近似，就需要可微性，例如通过偏导数的连续性来保证。
:::

::::beispiel [算例]
对于 $f(\mathbf{x})=x_1^2x_2+x_2^2$，偏导数 $2x_1x_2$ 和 $x_1^2+2x_2$ 都是多项式，因而处处连续，$f$ 处处可微。在式 [(3.4)](#gl-3-4) 处的算例中，$\lVert\mathbf{h}\rVert=\sqrt{0.0001+0.0004}\approx0.0224$ 时误差为 $0.001002$，所以式 [(3.5)](#gl-3-5) 中的商约为 $0.045$。把 $\mathbf{h}$ 减半为 $(0.005,\ 0.01)^{\top}$，误差为 $f(1.005,\ 2.01)-6-0.07=0.000250\ldots$，商约为 $0.022$：它随 $\mathbf{h}$ 减半，并且趋于 $0$。
::::

⁠**简而言之：**可微是指用梯度作的线性近似的误差比 $\lVert\mathbf{h}\rVert$ 消失得更快；偏导数连续就能保证这一点，仅仅存在则不能。

:::hintergrund 为什么偏导数连续就够了
从 $\mathbf{x}$ 到 $\mathbf{x}+\mathbf{h}$，不走斜线，而是分两段平行于坐标轴走：先沿 $x_1$ 方向走 $h_1$，再沿 $x_2$ 方向走 $h_2$。每一段上只有一个变量在变化，由一元函数的中值定理，变化量恰好是 $\partial_jf\cdot h_j$，只是偏导数要在这一段上的某个中间点处求值。如果偏导数连续，它们在中间点处的值就接近在点 $\mathbf{x}$ 处的值，两段之和与 $\nabla f(\mathbf{x})^{\top}\mathbf{h}$ 只相差一个比 $\lVert\mathbf{h}\rVert$ 消失得更快的量。在反例中，恰恰是这一步失效了：它的偏导数在原点以外虽然存在，却不连续。例如在坐标轴 $x_1=0$ 上，$\partial_1f(0,x_2)=1/x_2$，越接近原点，它就变得越大，可以任意大，而在原点处它的值是 $0$。
:::

:::aufgabe 练习 9 ★ 偏导数与梯度
<span class="anker" id="aufg-9"></span>

计算在给定点处的偏导数和梯度。

<ol class="al">

<li>

$f(\mathbf{x})=3x_1-2x_2+5$，在点 $(4,\,-1)$ 处；

</li>

<li>

$f(\mathbf{x})=x_1\,\mathrm{e}^{x_2}$，在点 $(2,\,0)$ 和点 $(1,\,1)$ 处；

</li>

<li>

$f(\mathbf{x})=x_1x_2+x_2x_3+x_3x_1$，在点 $(1,\,2,\,3)$ 处。

</li>

</ol>

:::loesung
(a) $\partial_1f=3$，$\partial_2f=-2$，所以在每一点都有 $\nabla f=(3,\,-2)^{\top}$。

(b) $\partial_1f=\mathrm{e}^{x_2}$，$\partial_2f=x_1\mathrm{e}^{x_2}$。在点 $(2,\,0)$ 处，$\nabla f=(1,\,2)^{\top}$；在点 $(1,\,1)$ 处，$\nabla f=(\mathrm{e},\,\mathrm{e})^{\top}\approx(2.718,\ 2.718)^{\top}$。

(c) $\partial_1f=x_2+x_3$，$\partial_2f=x_1+x_3$，$\partial_3f=x_1+x_2$；所以在点 $(1,\,2,\,3)$ 处，$\nabla f=(5,\,4,\,3)^{\top}$。
:::
:::

:::aufgabe 练习 10 ★★ 二元函数的线性近似
<span class="anker" id="aufg-10"></span>

设 $f(\mathbf{x})=x_1\,\mathrm{e}^{x_2}$。

<ol class="al">

<li>

用点 $(2,\,0)$ 处的线性近似计算 $f(2.1,\ -0.05)$ 的近似值，并与精确值比较。

</li>

<li>

两个变化中哪一个对 $f$ 的变化贡献更大？为什么它们在线性近似中恰好相互抵消，在精确值中却没有？

</li>

</ol>

:::loesung
(a) 由练习 [9](#aufg-9)，$f(2,0)=2$，$\nabla f(2,0)=(1,\,2)^{\top}$。取 $\mathbf{h}=(0.1,\ -0.05)^{\top}$：

$$f(2.1,\ -0.05)\approx2+1\cdot0.1+2\cdot(-0.05)=2+0.1-0.1=2.0 .$$

精确值是 $2.1\,\mathrm{e}^{-0.05}\approx2.1\cdot0.951229\approx1.99758$。误差约为 $0.0024$。

(b) 两个变化的贡献一样大，分别为 $+0.1$ 和 $-0.1$，它们在线性近似中相互抵消。但在精确值中，两个变量相互影响：$x_1$ 变大时，$f$ 对 $x_2$ 的反应更强，因为 $\partial_2f=x_1\mathrm{e}^{x_2}$ 随 $x_1$ 增大。因此 $x_2$ 的减小所起的作用比线性近似所假定的略强。这样的交互作用是两个变化的乘积，这里约为 $0.1\cdot(-0.05)=-0.005$，属于线性近似所略去的二阶项。第 [8](die-hesse-matrix-und-die-quadratische-naherung.html#stufe-8) 节会把它们算出来（练习 [29](die-hesse-matrix-und-die-quadratische-naherung.html#aufg-29)）。
:::
:::

:::aufgabe 练习 11 ★★ 等高线与截线
<span class="anker" id="aufg-11"></span>

设 $f(\mathbf{x})=x_1^2x_2+x_2^2$，如式 [(3.1)](#gl-3-1)。

<ol class="al">

<li>

$f$ 在点 $(2,\,1)$ 处的值是多少？在同一条等高线上再找一个 $x_1=0$ 的点。

</li>

<li>

计算 $\nabla f(2,1)$，以及经过 $(2,\,1)$ 的两条截线的方程。检验它们的斜率。

</li>

</ol>

:::loesung
(a) $f(2,1)=4\cdot1+1=5$。取 $x_1=0$，等高线要求 $x_2^2=5$，所以例如 $(0,\ \sqrt5)\approx(0,\ 2.236)$ 位于这条等高线上。

(b) $\nabla f(2,1)=(2\cdot2\cdot1,\ 4+2\cdot1)^{\top}=(4,\,6)^{\top}$。沿 $x_2=1$ 的截线是 $f(x_1,1)=x_1^2+1$，在 $x_1=2$ 处的斜率为 $2x_1=4$。沿 $x_1=2$ 的截线是 $f(2,x_2)=4x_2+x_2^2$，在 $x_2=1$ 处的斜率为 $4+2x_2=6$。两个斜率都与梯度的分量一致。
:::
:::

:::aufgabe 练习 12 ★★★ 连续却不可微
<span class="anker" id="aufg-12"></span>

设 $f(x_1,x_2)=\sqrt{|x_1x_2|}$。

<ol class="al">

<li>

证明两个偏导数在原点处都存在，并且都为 $0$。

</li>

<li>

取 $\mathbf{h}=(t,\,t)^{\top}$，证明当 $\mathbf{g}=\mathbf{0}$ 时，式 [(3.5)](#gl-3-5) 中的商不趋于 $0$。为什么由此可知 $f$ 在原点处不可微，尽管 $f$ 在那里连续？

</li>

</ol>

:::loesung
(a) 在两根坐标轴上都有 $x_1x_2=0$，所以 $f=0$。因此对每个 $h\ne0$ 都有 $\frac{f(h,0)-f(0,0)}{h}=0$，对第二个变量也是如此。原点处的两个偏导数都是 $0$。

(b) 如果 $f$ 在原点处可微，那么由第 [3.5](#stufe-3-5) 节中的定理，式 [(3.5)](#gl-3-5) 中的向量必须是梯度 $\mathbf{0}$。但取 $\mathbf{h}=(t,\,t)^{\top}$ 时，$f(\mathbf{h})=\sqrt{t^2}=|t|$，$\lVert\mathbf{h}\rVert=\sqrt2\,|t|$，所以

$$\frac{f(\mathbf{h})-f(\mathbf{0})-\mathbf{0}^{\top}\mathbf{h}}{\lVert\mathbf{h}\rVert}=\frac{|t|}{\sqrt2\,|t|}=\frac1{\sqrt2}\approx0.707 ,$$

对任意小的 $t\ne0$ 都是如此。这个商不趋于 $0$，所以 $f$ 不可微。尽管如此，$f$ 是连续的，因为当 $\mathbf{x}$ 趋于 $\mathbf{0}$ 时，$|f(\mathbf{x})|=\sqrt{|x_1|\,|x_2|}\le\max(|x_1|,|x_2|)\le\lVert\mathbf{x}\rVert$ 趋于 $0$。地面在原点处没有缺口，但沿对角线有一道折痕，没有一个平面能贴合它。
:::
:::
