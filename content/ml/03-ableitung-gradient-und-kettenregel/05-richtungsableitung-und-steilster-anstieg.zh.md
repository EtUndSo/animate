---
title: 方向导数与最速上升
pfad: 计算机科学 / 机器学习 / 数学基础 / 导数、梯度与链式法则
adresse: informatik/machine-learning/mathematische-grundlagen/ableitung-gradient-und-kettenregel
knoten: 第 3 章：导数、梯度与链式法则
nachschlagen: ja
order: 15230500
summary: 偏导数说明只改变一个输入时函数如何反应。如果把所有输入同时朝一个方向移动，就用方向导数来衡量斜率。借助方向导数，本节说明梯度指向最速上升的方向，并且垂直于等高线。一个例子说明，最陡的下坡路却不一定通向最低点。
tags: 方向导数
lang: zh
---

<span class="anker" id="stufe-4"></span>

:::zweck
偏导数说明只改变一个输入时函数如何反应。如果把所有输入同时朝一个方向移动，就用方向导数来衡量斜率。借助方向导数，本节说明梯度指向最速上升的方向，并且垂直于等高线。一个例子说明，最陡的下坡路却不一定通向最低点。
:::

### 方向导数

<span class="anker" id="stufe-4-1"></span>

在野外，人们很少正好朝北或正好朝东走。站在点 $\mathbf{x}$ 处朝某个方向出发，感受到的斜率取决于方向。一个方向用长度为 $1$ 的向量 $\mathbf{u}$ 来描述。长度必须固定：步子迈大一倍，每一步升高的也多一倍，地面却并没有变陡。

:::definition 定义 4.1 (方向导数)
<span class="anker" id="satz-4-1"></span>

对满足 $\lVert\mathbf{u}\rVert=1$ 的向量 $\mathbf{u}$，称

<span class="anker" id="gl-4-1"></span>
$$D_{\mathbf{u}}f(\mathbf{x})=\lim_{t\to0}\frac{f(\mathbf{x}+t\,\mathbf{u})-f(\mathbf{x})}{t} \tag{4.1}$$

为 $f$ 在点 $\mathbf{x}$ 处沿方向 $\mathbf{u}$ 的__方向导数__，前提是这个极限存在。
:::

当 $\mathbf{u}=\mathbf{e}_j$ 时，这就是对 $x_j$ 的偏导数。在地形的图景中，就是沿经过 $\mathbf{x}$、方向为 $\mathbf{u}$ 的直线把地面切开，方向导数就是这条截线的斜率。不过，并不需要对每个方向都重新计算它。

:::satz 定理 4.2 (方向导数与梯度)
<span class="anker" id="satz-4-2"></span>

如果 $f$ 在点 $\mathbf{x}$ 处可微，那么对每个长度为 $1$ 的向量 $\mathbf{u}$，有

<span class="anker" id="gl-4-2"></span>
$$D_{\mathbf{u}}f(\mathbf{x})=\nabla f(\mathbf{x})^{\top}\mathbf{u} . \tag{4.2}$$
:::

:::beweis 方向导数与梯度
在式 [(3.5)](partielle-ableitungen-und-der-gradient.html#gl-3-5) 中特别地取 $\mathbf{h}=t\,\mathbf{u}$，$t\ne0$；于是 $\lVert\mathbf{h}\rVert=|t|$。商 $\frac{f(\mathbf{x}+t\mathbf{u})-f(\mathbf{x})-t\,\nabla f(\mathbf{x})^{\top}\mathbf{u}}{|t|}$ 趋于 $0$，因而 $\frac{f(\mathbf{x}+t\mathbf{u})-f(\mathbf{x})}{t}-\nabla f(\mathbf{x})^{\top}\mathbf{u}$ 也趋于零。
:::

::::beispiel [算例]
对于 $f(\mathbf{x})=x_1^2x_2+x_2^2$ 在点 $(1,\,2)$ 处，$\nabla f=(4,\,5)^{\top}$，取方向 $\mathbf{u}=(0.6,\ 0.8)^{\top}$，它的长度为 $\sqrt{0.36+0.64}=1$，则

$$D_{\mathbf{u}}f(1,2)=4\cdot0.6+5\cdot0.8=2.4+4.0=6.4$$

见图 [8](#abb-8)。沿相反方向 $-\mathbf{u}$，斜率为 $-6.4$；沿与 $\mathbf{u}$ 垂直的方向 $(0.8,\ -0.6)^{\top}$，斜率为 $3.2-3.0=0.2$。

:::abbildung ml/k3rrichtung 8
方向导数是梯度与方向的点积：$f(\mathbf{x})=x_1^2x_2+x_2^2$ 在点 $\mathbf{x}=(1,\,2)^{\top}$ 处。
:::
::::

⁠**简而言之：**沿单位向量 $\mathbf{u}$ 方向的斜率是点积 $\nabla f(\mathbf{x})^{\top}\mathbf{u}$。

### 最速上升的方向

<span class="anker" id="stufe-4-2"></span>

朝哪个方向走，上坡才最陡？由式 [(4.2)](#gl-4-2)，要找的是使点积 $\nabla f(\mathbf{x})^{\top}\mathbf{u}$ 最大的单位向量 $\mathbf{u}$。[第 1 章](/wissen/zh/informatik/machine-learning/mathematische-grundlagen/vektoren-und-matrizen/vektoren-und-matrizen.html)已经为此提供了工具：柯西-施瓦茨不等式。

:::satz 定理 4.3 (最速上升)
<span class="anker" id="satz-4-3"></span>

设 $f$ 在点 $\mathbf{x}$ 处可微，并且 $\nabla f(\mathbf{x})\ne\mathbf{0}$。那么对每个长度为 $1$ 的向量 $\mathbf{u}$，有

<span class="anker" id="gl-4-3"></span>
$$-\lVert\nabla f(\mathbf{x})\rVert\le D_{\mathbf{u}}f(\mathbf{x})\le\lVert\nabla f(\mathbf{x})\rVert . \tag{4.3}$$

上界只在 $\mathbf{u}=\nabla f(\mathbf{x})/\lVert\nabla f(\mathbf{x})\rVert$ 时达到，下界只在 $\mathbf{u}=-\nabla f(\mathbf{x})/\lVert\nabla f(\mathbf{x})\rVert$ 时达到。因此，梯度指向最速上升的方向，它的长度就是沿这个方向的斜率；负梯度指向最速下降的方向。
:::

:::beweis 最速上升
由[第 1 章第 5.1 节](/wissen/zh/informatik/machine-learning/mathematische-grundlagen/vektoren-und-matrizen/winkel-und-ahnlichkeit.html#stufe-5-1)的柯西-施瓦茨不等式，$|\nabla f(\mathbf{x})^{\top}\mathbf{u}|\le\lVert\nabla f(\mathbf{x})\rVert\,\lVert\mathbf{u}\rVert=\lVert\nabla f(\mathbf{x})\rVert$，并且当且仅当 $\mathbf{u}$ 是 $\nabla f(\mathbf{x})$ 的倍数时等号成立。长度为 $1$ 的倍数是 $\pm\nabla f(\mathbf{x})/\lVert\nabla f(\mathbf{x})\rVert$。代入后得到 $\pm\nabla f(\mathbf{x})^{\top}\nabla f(\mathbf{x})/\lVert\nabla f(\mathbf{x})\rVert=\pm\lVert\nabla f(\mathbf{x})\rVert$。
:::

利用[第 1 章第 5.2 节](/wissen/zh/informatik/machine-learning/mathematische-grundlagen/vektoren-und-matrizen/winkel-und-ahnlichkeit.html#stufe-5-2)中 $\nabla f(\mathbf{x})$ 与 $\mathbf{u}$ 之间的夹角 $\varphi$，有 $D_{\mathbf{u}}f(\mathbf{x})=\lVert\nabla f(\mathbf{x})\rVert\cos\varphi$。沿梯度方向走，$\varphi=0$，$\cos\varphi=1$。偏离 $90^\circ$，斜率为零。逆着梯度走，斜率为负且绝对值最大。由[第 1 章第 5.5 节](/wissen/zh/informatik/machine-learning/mathematische-grundlagen/vektoren-und-matrizen/winkel-und-ahnlichkeit.html#stufe-5-5)，$\nabla f(\mathbf{x})^{\top}\mathbf{u}$ 是梯度在方向为 $\mathbf{u}$ 的直线上的影长，而当直线指向箭头本身的方向时，影子最长。

这个定理包含三个前提。第一，必须有 $\nabla f(\mathbf{x})\ne\mathbf{0}$；如果梯度为零，由式 [(4.2)](#gl-4-2)，沿每个方向的斜率都为零，没有哪个方向比别的方向更陡。第二，$f$ 必须可微，否则式 [(4.2)](#gl-4-2) 不成立。第三，定理比较的是欧几里得长度相同的方向；如果用别的方式衡量步长，最陡的方向就会改变（见下面的背景方框）。

::::beispiel [算例]
对于 $f(\mathbf{x})=x_1^2x_2+x_2^2$ 在点 $(1,\,2)$ 处，$\lVert\nabla f\rVert=\sqrt{16+25}=\sqrt{41}\approx6.403$，最陡方向为 $(4,\,5)^{\top}/\sqrt{41}\approx(0.625,\ 0.781)^{\top}$。没有哪个方向的斜率更大。上一小节中的方向 $\mathbf{u}=(0.6,\ 0.8)^{\top}$ 与它只相差约 $1.8^\circ$；所以它的斜率 $6.4$ 已经几乎达到最大值。沿与梯度垂直的方向 $(5,\,-4)^{\top}/\sqrt{41}$，斜率为 $(20-20)/\sqrt{41}=0$。
::::

⁠**简而言之：**梯度指向最速上升的方向，它的长度就是该方向上的斜率；逆着梯度走，下坡最陡。

:::hintergrund 最陡的方向取决于怎样衡量步长
定理比较的是欧几里得范数下满足 $\lVert\mathbf{u}\rVert=1$ 的所有方向 $\mathbf{u}$。[第 1 章第 3 节](/wissen/zh/informatik/machine-learning/mathematische-grundlagen/vektoren-und-matrizen/normen-die-groe-eines-vektors.html#stufe-3)还介绍了其他范数。如果允许所有满足 $\lVert\mathbf{u}\rVert_\infty\le1$ 的步子，即每个分量都可以介于 $-1$ 和 $1$ 之间，那么当每个分量 $u_j$ 都取与 $\partial_jf$ 同号的 $+1$ 或 $-1$ 时，$\nabla f^{\top}\mathbf{u}=\sum_j\partial_jf\cdot u_j$ 最大。这时最陡的方向是逐分量取符号得到的 $\operatorname{sign}(\nabla f)$，斜率为 $\sum_j|\partial_jf|=\lVert\nabla f\rVert_1$。反之，如果允许所有满足 $\lVert\mathbf{u}\rVert_1\le1$ 的步子，就把全部预算都投入 $|\partial_jf|$ 最大的那个分量：最陡的方向是一根坐标轴，斜率为 $\lVert\nabla f\rVert_\infty$。对 $\nabla f=(4,\,5)^{\top}$，这分别给出斜率为 $9$ 的方向 $(1,\,1)^{\top}$ 和斜率为 $5$ 的方向 $(0,\,1)^{\top}$。因此，“梯度是最陡的方向”是关于欧几里得长度的结论。它还取决于变量的单位：如果用别的单位衡量 $x_1$，步子的长度就会改变，最陡的方向也随之改变，就像[第 1 章第 4.2 节](/wissen/zh/informatik/machine-learning/mathematische-grundlagen/vektoren-und-matrizen/abstande-und-einheiten.html#stufe-4-2)中的距离一样。
:::

### 梯度垂直于等高线

<span class="anker" id="stufe-4-3"></span>

沿着等高线走，既不上升也不下降。所以沿等高线方向的斜率为零，而由上一小节，斜率恰好在与梯度垂直的那些方向上为零。因此梯度垂直于等高线。更确切地说：

:::satz 定理 4.4 (梯度与等高线)
<span class="anker" id="satz-4-4"></span>

设 $f$ 在点 $\mathbf{x}$ 处可微，$\nabla f(\mathbf{x})\ne\mathbf{0}$，$c=f(\mathbf{x})$。线性近似经过 $\mathbf{x}$ 的水平集，即满足 $\nabla f(\mathbf{x})^{\top}\mathbf{h}=0$ 的点 $\mathbf{x}+\mathbf{h}$ 的集合，在两个变量时是经过 $\mathbf{x}$ 且垂直于梯度的直线。它是 $f$ 在值 $c$ 处的等高线的切线。
:::

这条直线与等高线相切，这一点由放大镜得出：在 $\mathbf{x}$ 附近，$f$ 与它的线性近似只相差一个比 $\lVert\mathbf{h}\rVert$ 消失得更快的误差，因此它们在值 $c$ 处的等高线也只相差很少，以至于两者在 $\mathbf{x}$ 处方向相同。练习 [22](die-kettenregel-fur-mehrere-variablen.html#aufg-22) 给出一个用链式法则的证明。变量多于两个时，水平集是一个曲面，对它同样成立：梯度垂直于这个曲面。

::::beispiel [算例]
对于碗形 $f(\mathbf{x})=x_1^2+4x_2^2$，有 $\nabla f(\mathbf{x})=(2x_1,\,8x_2)^{\top}$，在点 $(1,\,1)$ 处等于 $(2,\,8)^{\top}$。经过这一点的等高线是椭圆 $x_1^2+4x_2^2=5$。方向 $\mathbf{t}=(4,\,-1)^{\top}$ 垂直于梯度，因为 $2\cdot4+8\cdot(-1)=0$。从 $(1,\,1)$ 出发沿这个方向走一段 $s$，有

$$f(1+4s,\ 1-s)=(1+4s)^2+4\,(1-s)^2=5+20s^2 .$$

函数值只变化 $20s^2$，比 $s$ 消失得更快：这条直线与等高线相切，是它的切线。图 [9](#abb-9) 画出了许多点处的梯度；每个梯度都垂直于经过它的起点的等高线。

:::abbildung ml/k3hoehen 9
等高线（灰色）上的梯度（红色，缩短画出）。(a) 对圆碗，所有梯度都恰好背离中心。(b) 对拉长的碗，梯度同样垂直于等高线，但只在坐标轴上才恰好背离中心。在点 $(1,\,1)$（黑色）处，用蓝色画出了最速下降的方向。在 (a) 中它指向最低点，在 (b) 中它与指向最低点的方向（虚线）相差约 $31^\circ$。
:::
::::

⁠**简而言之：**沿等高线，$f$ 不变；所以梯度垂直于等高线。

### 最速下降与最低点

<span class="anker" id="stufe-4-4"></span>

对于圆碗，最陡的下坡路通向中心，这是理所当然的。对于拉长的碗，这就错了；这个区别很重要，因为人们很容易对梯度期望过高，以为它知道的比实际更多。

对于 $f(\mathbf{x})=x_1^2+x_2^2$，有 $\nabla f(\mathbf{x})=2\mathbf{x}$。所以负梯度 $-2\mathbf{x}$ 从每一点出发都恰好指向原点，即碗的最低点。对于 $f(\mathbf{x})=x_1^2+4x_2^2$，有 $-\nabla f(\mathbf{x})=(-2x_1,\,-8x_2)^{\top}$，只有当 $x_1=0$ 或 $x_2=0$，即在坐标轴上时，它才是 $-\mathbf{x}$ 的倍数。在其他所有地方，最速下降的方向都会偏离最低点。

原因在于等高线的形状。梯度只知道地面在它的起点处怎样倾斜；它垂直于那里的等高线。等高线被拉长时，这条垂线与指向中心的方向是斜交的。在这个例子中，$f$ 沿 $x_2$ 方向增长的速度是沿 $x_1$ 方向的四倍；碗壁在 $x_2$ 方向上更陡，最速下降的方向主要是横穿碗壁。

::::beispiel [算例]
在点 $(1,\,1)$ 处，$-\nabla f=(-2,\,-8)^{\top}$，长度为 $\sqrt{68}\approx8.246$，所以最速下降的方向是 $(-0.243,\ -0.970)^{\top}$。指向最低点的方向是 $(-1,\,-1)^{\top}/\sqrt2\approx(-0.707,\ -0.707)^{\top}$。两者夹角的余弦为

$$\frac{(-2)\cdot(-1)+(-8)\cdot(-1)}{\sqrt{68}\cdot\sqrt2}=\frac{10}{\sqrt{136}}\approx0.857,$$

所以夹角约为 $31^\circ$。由式 [(4.2)](#gl-4-2)，沿指向最低点的方向，斜率只有 $-10/\sqrt2\approx-7.07$，而沿最速下降的方向则为 $-8.246$。
::::

⁠**简而言之：**负梯度指向最陡的下坡方向，但只有当等高线是圆时，它才指向最低点；等高线被拉长时，它会偏离最低点。

:::aufgabe 练习 13 ★ 许多方向上的斜率
<span class="anker" id="aufg-13"></span>

设 $f(\mathbf{x})=x_1^2+4x_2^2$，$\mathbf{x}=(1,\,1)^{\top}$。

<ol class="al">

<li>

计算沿方向 $\mathbf{e}_1$、$\mathbf{e}_2$、$(1,\,1)^{\top}/\sqrt2$ 和 $(-1,\,1)^{\top}/\sqrt2$ 的方向导数。

</li>

<li>

与 $\lVert\nabla f(\mathbf{x})\rVert$ 比较。四个方向中哪一个最接近最陡的方向？

</li>

</ol>

:::loesung
(a) 有 $\nabla f(1,1)=(2,\,8)^{\top}$。由式 [(4.2)](#gl-4-2)：

$$D_{\mathbf{e}_1}f=2,\qquad D_{\mathbf{e}_2}f=8,\qquad D_{(1,1)/\sqrt2}f=\frac{2+8}{\sqrt2}\approx7.071,\qquad D_{(-1,1)/\sqrt2}f=\frac{-2+8}{\sqrt2}\approx4.243 .$$

(b) $\lVert\nabla f\rVert=\sqrt{68}\approx8.246$；正如式 [(4.3)](#gl-4-3) 所要求的，没有哪个斜率比它大。最接近最陡方向的是 $\mathbf{e}_2$，斜率为 $8$。$\mathbf{e}_2$ 与 $\nabla f$ 之间夹角的余弦为 $8/\sqrt{68}\approx0.970$，所以夹角约为 $14^\circ$；对 $(1,\,1)^{\top}/\sqrt2$，夹角约为 $31^\circ$。
:::
:::

:::aufgabe 练习 14 ★★ 作为等高线的双曲线
<span class="anker" id="aufg-14"></span>

设 $f(\mathbf{x})=x_1x_2$，$\mathbf{x}=(2,\,1)^{\top}$。

<ol class="al">

<li>

计算 $\nabla f(\mathbf{x})$、最陡的方向以及沿这个方向的斜率。

</li>

<li>

经过 $\mathbf{x}$ 的等高线是 $x_2=2/x_1$。计算这条曲线在 $x_1=2$ 处的斜率，把它的切线方向写成向量，并检验这个向量垂直于 $\nabla f(\mathbf{x})$。

</li>

</ol>

:::loesung
(a) $\nabla f(\mathbf{x})=(x_2,\,x_1)^{\top}$，所以在点 $(2,\,1)$ 处为 $(1,\,2)^{\top}$。最陡的方向是 $(1,\,2)^{\top}/\sqrt5\approx(0.447,\ 0.894)^{\top}$，沿这个方向的斜率为 $\sqrt5\approx2.236$。

(b) 等高线 $x_2=2/x_1$ 的斜率为 $-2/x_1^2$，所以在 $x_1=2$ 处为 $-\tfrac12$。一个切线方向是 $(1,\,-\tfrac12)^{\top}$，乘以 $2$ 后为 $(2,\,-1)^{\top}$。有 $(1,\,2)(2,\,-1)^{\top}=2-2=0$：梯度垂直于等高线。
:::
:::

:::aufgabe 练习 15 ★★ 线性函数
<span class="anker" id="aufg-15"></span>

设 $f(\mathbf{x})=\mathbf{a}^{\top}\mathbf{x}+b$，其中 $\mathbf{a}\in\mathbb{R}^d$ 固定，$\mathbf{a}\ne\mathbf{0}$，$b$ 是一个数。

<ol class="al">

<li>

证明在每一点都有 $\nabla f(\mathbf{x})=\mathbf{a}$。$d=2$ 时等高线是什么？

</li>

<li>

对[第 1 章](/wissen/zh/informatik/machine-learning/mathematische-grundlagen/vektoren-und-matrizen/vektoren-und-matrizen.html)中的公寓，$\hat y=\mathbf{w}^{\top}\mathbf{x}+b$，$\mathbf{w}=(3,\,10,\,-4)^{\top}$，其中 $x_1$ 是以 $\mathrm m^2$ 计的面积，$x_2$ 是房间数，$x_3$ 是以 km 计的到市中心的距离。在满足 $\lVert\mathbf{u}\rVert=1$ 的特征变化 $\mathbf{u}$ 中，哪一个使预测值提高得最多？提高多少？

</li>

<li>

如果以 $10\,\mathrm m^2$ 为单位给出面积，权重 $w_1=3$ 就变为 $30$。现在最陡的方向是什么？从中可以对最速上升定理得出什么认识？

</li>

</ol>

:::loesung
(a) $\partial_k(\mathbf{a}^{\top}\mathbf{x}+b)=a_k$，所以处处有 $\nabla f=\mathbf{a}$。当 $d=2$ 时，等高线是直线 $a_1x_1+a_2x_2+b=c$；它们彼此平行，并且都垂直于 $\mathbf{a}$。

(b) 对 $\mathbf{x}$ 的梯度是 $\mathbf{w}=(3,\,10,\,-4)^{\top}$，$\lVert\mathbf{w}\rVert=\sqrt{9+100+16}=\sqrt{125}\approx11.18$。长度为 $1$ 的最陡变化是 $\mathbf{u}=\mathbf{w}/\sqrt{125}\approx(0.268,\ 0.894,\ -0.358)^{\top}$，它使预测值提高约 $11.18$ 千欧元：面积稍大一些，房间明显多一些，离市中心稍近一些。

(c) 在新单位下，$\mathbf{w}'=(30,\,10,\,-4)^{\top}$，$\lVert\mathbf{w}'\rVert=\sqrt{1016}\approx31.87$，最陡的方向是 $\mathbf{w}'/\lVert\mathbf{w}'\rVert\approx(0.941,\ 0.314,\ -0.125)^{\top}$：现在它几乎完全落在面积这一分量上。同样的公寓，同样的价格，最陡的方向却不同了。最速上升定理比较的是在所选坐标中欧几里得长度相同的步子，而“长度 $1$”是什么意思取决于单位，正如[第 1 章第 4.2 节](/wissen/zh/informatik/machine-learning/mathematische-grundlagen/vektoren-und-matrizen/abstande-und-einheiten.html#stufe-4-2)中的距离一样。对单位不同的特征，只有经过[第 1 章第 4.5 节](/wissen/zh/informatik/machine-learning/mathematische-grundlagen/vektoren-und-matrizen/abstande-und-einheiten.html#stufe-4-5)中的标准化之后，最陡的方向才有意义。
:::
:::

:::aufgabe 练习 16 ★★★ 最速下降何时指向中心？
<span class="anker" id="aufg-16"></span>

设 $f(\mathbf{x})=a\,x_1^2+b\,x_2^2$，其中 $a,b>0$ 是数。

<ol class="al">

<li>

证明：$-\nabla f(\mathbf{x})$ 是 $-\mathbf{x}$ 的正倍数，当且仅当 $a=b$ 或 $\mathbf{x}$ 位于某根坐标轴上（$\mathbf{x}\ne\mathbf{0}$）。

</li>

<li>

取 $a=1$，$b=4$，计算在点 $(1,\,1)$、$(2,\,1)$ 和 $(4,\,1)$ 处 $-\nabla f$ 与 $-\mathbf{x}$ 之间的夹角。沿直线 $x_2=1$ 向外走时，这个夹角怎样变化？

</li>

</ol>

:::loesung
(a) 有 $-\nabla f(\mathbf{x})=(-2ax_1,\,-2bx_2)^{\top}$。这个向量等于 $c\,(-x_1,\,-x_2)^{\top}$（其中 $c>0$），当且仅当 $2ax_1=c\,x_1$ 且 $2bx_2=c\,x_2$。如果两个坐标都不为零，就得到 $2a=c=2b$，即 $a=b$。如果 $x_1=0$，取 $c=2b$ 即可；如果 $x_2=0$，取 $c=2a$ 即可。所以，对圆碗，最速下降处处指向原点；对拉长的碗，只在坐标轴上如此。

(b) 取 $a=1$，$b=4$，有 $-\nabla f=(-2x_1,\,-8x_2)^{\top}$：

$$\begin{aligned} (1,\,1)&:\ \cos\varphi=\frac{2+8}{\sqrt{68}\,\sqrt2}\approx0.857,\ \varphi\approx31.0^\circ;\\ (2,\,1)&:\ \cos\varphi=\frac{8+8}{\sqrt{80}\,\sqrt5}=0.8,\ \varphi\approx36.9^\circ;\\ (4,\,1)&:\ \cos\varphi=\frac{32+8}{\sqrt{128}\,\sqrt{17}}\approx0.857,\ \varphi\approx31.0^\circ . \end{aligned}$$

沿直线 $x_2=1$，夹角从 $x_1=0$ 处的 $0^\circ$ 起先增大，然后又减小；在很远的外侧，这个点几乎位于 $x_1$ 轴的方向上，那里最速下降又几乎指向中心。
:::
:::
