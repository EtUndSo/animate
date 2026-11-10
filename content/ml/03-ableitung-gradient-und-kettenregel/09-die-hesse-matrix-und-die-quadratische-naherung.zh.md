---
title: 黑塞矩阵与二次近似
pfad: 计算机科学 / 机器学习 / 数学基础 / 导数、梯度与链式法则
adresse: informatik/machine-learning/mathematische-grundlagen/ableitung-gradient-und-kettenregel
knoten: 第 3 章：导数、梯度与链式法则
nachschlagen: ja
order: 15230900
summary: 梯度描述地形的倾斜度，但不描述它的弯曲。黑塞矩阵汇集了二阶偏导数。它是对称的，借助它，线性近似就变成了二次近似。它的特征值说明地形沿不同方向弯曲得有多强，并把本节与第 2 章中的二次型联系起来。
tags: 二阶偏导数, 黑塞矩阵, 混合差分, 二阶方向导数
lang: zh
---

<span class="anker" id="stufe-8"></span>

:::zweck
梯度描述地形的倾斜度，但不描述它的弯曲。黑塞矩阵汇集了二阶偏导数。它是对称的，借助它，线性近似就变成了二次近似。它的特征值说明地形沿不同方向弯曲得有多强，并把本节与[第 2 章](/wissen/zh/informatik/machine-learning/mathematische-grundlagen/projektion-eigenwerte-und-zerlegungen/projektion-eigenwerte-und-zerlegungen.html)中的二次型联系起来。
:::

### 二阶偏导数

<span class="anker" id="stufe-8-1"></span>

偏导数 $\partial_jf$ 本身又是 $\mathbf{x}$ 的函数。可以对它们再求一次偏导数，对同一个变量或对另一个变量。这描述了沿 $x_i$ 方向继续前进时，沿 $x_j$ 方向的斜率如何变化。

:::definition 定义 8.1 (二阶偏导数)
<span class="anker" id="satz-8-1"></span>

$f:\mathbb{R}^d\to\mathbb{R}$ 的__二阶偏导数__为

<span class="anker" id="gl-8-1"></span>
$$\frac{\partial^2f}{\partial x_i\,\partial x_j}=\frac{\partial}{\partial x_i}\Bigl(\frac{\partial f}{\partial x_j}\Bigr), \tag{8.1}$$

即先对 $x_j$、再对 $x_i$ 求导。$i=j$ 时记作 $\partial^2f/\partial x_i^2$。$i\ne j$ 时，它们称为混合偏导数。
:::

::::beispiel [算例]
对 $f(\mathbf{x})=x_1^2x_2+x_2^2$，有 $\partial_1f=2x_1x_2$ 和 $\partial_2f=x_1^2+2x_2$，因此

$$\begin{gathered} \frac{\partial^2f}{\partial x_1^2}=\frac{\partial}{\partial x_1}(2x_1x_2)=2x_2,\qquad \frac{\partial^2f}{\partial x_2\,\partial x_1}=\frac{\partial}{\partial x_2}(2x_1x_2)=2x_1,\\ \frac{\partial^2f}{\partial x_1\,\partial x_2}=\frac{\partial}{\partial x_1}(x_1^2+2x_2)=2x_1,\qquad \frac{\partial^2f}{\partial x_2^2}=\frac{\partial}{\partial x_2}(x_1^2+2x_2)=2 . \end{gathered}$$

在点 $(1,\,2)$ 处，它们分别为 $4$、$2$、$2$ 和 $2$。两个混合偏导数相等，尽管它们是沿不同途径得到的。
::::

⁠**简而言之：**二阶偏导数就是把一个偏导数再求一次偏导数；混合偏导数描述沿另一个方向行走时，沿某一方向的斜率如何变化。

### 黑塞矩阵

<span class="anker" id="stufe-8-2"></span>

$d$ 元函数有 $d^2$ 个二阶偏导数。正如一阶导数汇集在梯度中，人们也把它们汇集成一个对象，这里是一个方阵。

:::definition 定义 8.2 (黑塞矩阵)
<span class="anker" id="satz-8-2"></span>

称 $d\times d$ 矩阵

<span class="anker" id="gl-8-2"></span>
$$\mathbf{H}_f(\mathbf{x})=\begin{pmatrix}\dfrac{\partial^2f}{\partial x_1^2}&\cdots&\dfrac{\partial^2f}{\partial x_1\,\partial x_d}\\ \vdots&&\vdots\\ \dfrac{\partial^2f}{\partial x_d\,\partial x_1}&\cdots&\dfrac{\partial^2f}{\partial x_d^2}\end{pmatrix},\qquad \bigl(\mathbf{H}_f(\mathbf{x})\bigr)_{ij}=\frac{\partial^2f}{\partial x_i\,\partial x_j}(\mathbf{x}), \tag{8.2}$$

为 $f$ 在点 $\mathbf{x}$ 处的__黑塞矩阵__。
:::

这个矩阵以数学家奥托·黑塞（Otto Hesse）命名；有些书记作 $\nabla^2f$。它的第 $j$ 列是函数 $\partial_jf$ 的梯度。因此它与梯度的雅可比矩阵密切相关，也就是与向量值函数 $\mathbf{x}\mapsto\nabla f(\mathbf{x})$ 的雅可比矩阵：后者的元素 $(i,j)$ 是 $\partial(\partial_if)/\partial x_j$，即按另一种顺序求的导数。下一小节表明，两种顺序几乎总是给出相同的结果；这时黑塞矩阵就是梯度的雅可比矩阵。

::::beispiel [算例]
对 $f(\mathbf{x})=x_1^2x_2+x_2^2$，由上一小节，

$$\mathbf{H}_f(\mathbf{x})=\begin{pmatrix}2x_2&2x_1\\2x_1&2\end{pmatrix},\qquad \mathbf{H}_f(1,2)=\begin{pmatrix}4&2\\2&2\end{pmatrix}.$$

对 $\mathbf{A}$ 对称的二次函数 $f(\mathbf{x})=\tfrac12\mathbf{x}^{\top}\mathbf{A}\mathbf{x}+\mathbf{b}^{\top}\mathbf{x}+c$，由第 [7](ableiten-nach-vektoren-und-matrizen.html#stufe-7) 节，$\nabla f(\mathbf{x})=\mathbf{A}\mathbf{x}+\mathbf{b}$，因此在每个点处都有 $\mathbf{H}_f=\mathbf{A}$。对第 [4](richtungsableitung-und-steilster-anstieg.html#stufe-4) 节中的碗形 $x_1^2+4x_2^2$，$\mathbf{A}=\operatorname{diag}(2,\,8)$。
::::

⁠**简而言之：**黑塞矩阵汇集所有二阶偏导数；对二次函数 $\tfrac12\mathbf{x}^{\top}\mathbf{A}\mathbf{x}+\mathbf{b}^{\top}\mathbf{x}+c$，它处处等于 $\mathbf{A}$。

### 施瓦茨定理

<span class="anker" id="stufe-8-3"></span>

在算例中，两个混合偏导数相等。这不是巧合，而是对所有二阶导数没有跳跃的函数都成立。

:::satz 定理 8.3 (施瓦茨定理)
<span class="anker" id="satz-8-3"></span>

如果 $f$ 的所有二阶偏导数在 $\mathbf{x}$ 附近都存在，并且在点 $\mathbf{x}$ 处连续，那么在该点处

<span class="anker" id="gl-8-3"></span>
$$\frac{\partial^2f}{\partial x_i\,\partial x_j}=\frac{\partial^2f}{\partial x_j\,\partial x_i} \tag{8.3}$$

对所有 $i,j$ 成立。这时黑塞矩阵是对称的。
:::

其原因可以从一个根本不涉及求导顺序的计算中看出。从 $\mathbf{x}$ 出发，沿 $x_1$ 方向移动 $h$，沿 $x_2$ 方向移动 $k$，构成__混合差分__

$$\Delta(h,k)=f(x_1+h,\,x_2+k)-f(x_1+h,\,x_2)-f(x_1,\,x_2+k)+f(x_1,\,x_2).$$

把第一项与第三项、第二项与第四项合并，$\Delta$ 就是差 $f(x_1+h,\cdot)-f(x_1,\cdot)$ 在沿 $x_2$ 方向走一步 $k$ 时的变化：沿 $x_2$ 方向走时，沿 $x_1$ 方向的上升如何变化？除以 $hk$ 后，对很小的 $h$ 和 $k$，它趋近于先对 $x_1$、再对 $x_2$ 求的导数。如果改为把前两项和后两项合并，同一个数就被解读为沿 $x_1$ 方向走一步时沿 $x_2$ 方向的上升的变化，这个商就趋近于按另一种顺序求的导数。两个极限都属于同一个数 $\Delta/(hk)$。连续性保证了两次取极限的先后顺序无关紧要。

::::beispiel [算例]
对 $f(\mathbf{x})=x_1^2x_2+x_2^2$，在点 $(1,\,2)$ 处取 $h=k=0.1$，有

$$\Delta=f(1.1,\ 2.1)-f(1.1,\ 2)-f(1,\ 2.1)+f(1,2)=6.951-6.42-6.51+6=0.021,$$

因此 $\Delta/(hk)=2.1$，接近混合偏导数 $2x_1=2$。偏差的原因是 $2x_1$ 在 $x_1=1$ 与 $x_1=1.1$ 之间不是常数。
::::

⁠**简而言之：**二阶导数连续时，求导的顺序无关紧要，黑塞矩阵是对称的。

:::hintergrund 二阶导数不连续时
没有连续性，这个定理可能不成立。经典的反例是 $f(x_1,x_2)=x_1x_2\,\frac{x_1^2-x_2^2}{x_1^2+x_2^2}$，并规定 $f(0,0)=0$。在坐标轴上计算一阶偏导数，得到 $\partial_1f(0,x_2)=-x_2$ 和 $\partial_2f(x_1,0)=x_1$。把前者对 $x_2$ 求导，在原点处得 $-1$；把后者对 $x_1$ 求导，得 $+1$。所以原点处的两个混合偏导数不同，因为二阶导数在那里有跳跃。本章中没有折点的函数不会出现这种情况；它们由多项式、指数函数和基本算术运算构成，在有定义的地方处处具有任意阶的连续导数。
:::

### 二次近似

<span class="anker" id="stufe-8-4"></span>

在一元情形，第 [1.5](die-ableitung.html#stufe-1-5) 节用一条抛物线改进了切线。在多元情形，取代切平面的是一个弯曲的曲面，它的弯曲由黑塞矩阵描述。

:::satz 定理 8.4 (二次近似)
<span class="anker" id="satz-8-4"></span>

如果 $f$ 在 $\mathbf{x}$ 附近具有连续的二阶偏导数，那么

<span class="anker" id="gl-8-4"></span>
$$f(\mathbf{x}+\mathbf{h})=f(\mathbf{x})+\nabla f(\mathbf{x})^{\top}\mathbf{h}+\tfrac12\,\mathbf{h}^{\top}\mathbf{H}_f(\mathbf{x})\,\mathbf{h}+r_2(\mathbf{h})\qquad\text{其中}\qquad\lim_{\mathbf{h}\to\mathbf{0}}\frac{r_2(\mathbf{h})}{\lVert\mathbf{h}\rVert^2}=0 . \tag{8.4}$$
:::

:::herleitung 沿一条直线的二次近似
把 $f$ 限制在过 $\mathbf{x}$、方向为 $\mathbf{h}$ 的直线上：$\phi(t)=f(\mathbf{x}+t\,\mathbf{h})$。这是一个一元函数。由式 [(6.4)](die-kettenregel-fur-mehrere-variablen.html#gl-6-4)，$\phi'(t)=\nabla f(\mathbf{x}+t\mathbf{h})^{\top}\mathbf{h}=\sum_jh_j\,\partial_jf(\mathbf{x}+t\mathbf{h})$。再用式 [(6.4)](die-kettenregel-fur-mehrere-variablen.html#gl-6-4) 对每一项求一次导数，这次是对函数 $\partial_jf$：

$$\phi''(t)=\sum_{j=1}^dh_j\sum_{i=1}^d\frac{\partial^2f}{\partial x_i\,\partial x_j}(\mathbf{x}+t\mathbf{h})\,h_i=\mathbf{h}^{\top}\mathbf{H}_f(\mathbf{x}+t\mathbf{h})\,\mathbf{h} .$$

$\phi$ 在点 $0$ 处的二次近似式 [(1.6)](die-ableitung.html#gl-1-6) 在 $t=1$ 处取值，为 $\phi(1)\approx\phi(0)+\phi'(0)+\tfrac12\phi''(0)$，这正是式 [(8.4)](#gl-8-4)。误差比 $\lVert\mathbf{h}\rVert^2$ 更快地趋于零，这一点由二阶导数的连续性得出。
:::

新的项 $\tfrac12\mathbf{h}^{\top}\mathbf{H}_f\mathbf{h}$ 是[第 2 章第 5.1 节](/wissen/zh/informatik/machine-learning/mathematische-grundlagen/projektion-eigenwerte-und-zerlegungen/quadratische-formen.html#stufe-5-1)意义下的二次型，其矩阵就是黑塞矩阵。所以在 $\mathbf{x}$ 附近，函数看起来像一个平面加上一个二次型。

::::beispiel [算例]
对 $f(\mathbf{x})=x_1^2x_2+x_2^2$，在点 $(1,\,2)$ 处，取与第 [3.4](partielle-ableitungen-und-der-gradient.html#stufe-3-4) 节相同的 $\mathbf{h}=(0.01,\ 0.02)^{\top}$，可得下式，见图 [15](#abb-15)：

$$\tfrac12\,\mathbf{h}^{\top}\mathbf{H}_f\mathbf{h}=\tfrac12\bigl(4\cdot0.01^2+2\cdot2\cdot0.01\cdot0.02+2\cdot0.02^2\bigr)=\tfrac12\,(0.0004+0.0008+0.0008)=0.001$$

二次近似为 $6+0.14+0.001=6.141$，精确值为 $6.141002$。误差从 $0.001002$ 降到了 $0.000002$。剩下的是三阶项：$x_1^2x_2$ 中含有项 $h_1^2h_2=0.0001\cdot0.02=0.000002$，任何二次近似都捕捉不到它。

:::abbildung ml/k3rtaylor2 15
二次近似的曲率项写成双重求和；两个混合项 $h_1\cdot2\cdot h_2$ 和 $h_2\cdot2\cdot h_1$ 合并成了中间那一项。
:::
::::

⁠**简而言之：**在 $\mathbf{x}$ 附近，$f(\mathbf{x}+\mathbf{h})\approx f(\mathbf{x})+\nabla f(\mathbf{x})^{\top}\mathbf{h}+\tfrac12\mathbf{h}^{\top}\mathbf{H}_f(\mathbf{x})\mathbf{h}$：平面加二次型。

### 沿某方向的曲率

<span class="anker" id="stufe-8-5"></span>

从 $\mathbf{x}$ 出发沿方向 $\mathbf{u}$ 行走时，地形弯曲得有多强？上一小节的推导已经给出了答案：$\phi(t)=f(\mathbf{x}+t\mathbf{u})$ 在点 $0$ 处的二阶导数是 $\mathbf{u}^{\top}\mathbf{H}_f(\mathbf{x})\mathbf{u}$。

:::definition 定义 8.5 (沿某方向的曲率)
<span class="anker" id="satz-8-5"></span>

对长度为 $1$ 的向量 $\mathbf{u}$，称

<span class="anker" id="gl-8-5"></span>
$$\frac{\mathrm{d}^2}{\mathrm{d} t^2}f(\mathbf{x}+t\,\mathbf{u})\Big|_{t=0}=\mathbf{u}^{\top}\mathbf{H}_f(\mathbf{x})\,\mathbf{u} \tag{8.5}$$

为 $f$ 在点 $\mathbf{x}$ 处沿方向 $\mathbf{u}$ 的__二阶方向导数__。它衡量沿这个方向的截线的曲率。
:::

利用[第 2 章](/wissen/zh/informatik/machine-learning/mathematische-grundlagen/projektion-eigenwerte-und-zerlegungen/projektion-eigenwerte-und-zerlegungen.html)的结果，可以立即说出这个曲率最大和最小是多少。黑塞矩阵是对称的，由[第 2 章第 7.6 节](/wissen/zh/informatik/machine-learning/mathematische-grundlagen/projektion-eigenwerte-und-zerlegungen/diagonalisierung-und-spektralsatz.html#stufe-7-6)的谱定理，它具有实特征值和互相垂直的特征向量。

:::satz 定理 8.6 (曲率与特征值)
<span class="anker" id="satz-8-6"></span>

设 $\lambda_{\min}$ 和 $\lambda_{\max}$ 是对称黑塞矩阵 $\mathbf{H}_f(\mathbf{x})$ 的最小特征值和最大特征值。则对每个满足 $\lVert\mathbf{u}\rVert=1$ 的方向 $\mathbf{u}$，有

<span class="anker" id="gl-8-6"></span>
$$\lambda_{\min}\le\mathbf{u}^{\top}\mathbf{H}_f(\mathbf{x})\,\mathbf{u}\le\lambda_{\max}. \tag{8.6}$$

沿一个特征向量的方向，曲率恰好等于对应的特征值。如果 $\mathbf{H}_f(\mathbf{x})$ 正定，那么沿每个方向的曲率都是正的；如果它不定，那么地形沿某些方向向上弯曲，沿另一些方向向下弯曲。
:::

这个不等式就是[第 2 章第 8.5 节](/wissen/zh/informatik/machine-learning/mathematische-grundlagen/projektion-eigenwerte-und-zerlegungen/positiv-definite-matrizen.html#stufe-8-5)中关于二次型在单位圆上的最大值和最小值的结论。对属于特征值 $\lambda$ 的特征向量 $\mathbf{u}$，有 $\mathbf{u}^{\top}\mathbf{H}_f\mathbf{u}=\lambda\,\mathbf{u}^{\top}\mathbf{u}=\lambda$。正定和不定这两个概念来自[第 2 章第 8 节](/wissen/zh/informatik/machine-learning/mathematische-grundlagen/projektion-eigenwerte-und-zerlegungen/positiv-definite-matrizen.html#stufe-8)；在那里，二次型的形状可以从它的特征值读出：碗形、槽形或鞍形。通过二次近似式 [(8.4)](#gl-8-4)，这一点可以搬到 $\mathbf{x}$ 附近的地形上：当黑塞矩阵正定时，曲率项的等高线是椭圆；由[第 2 章第 7.7 节](/wissen/zh/informatik/machine-learning/mathematische-grundlagen/projektion-eigenwerte-und-zerlegungen/diagonalisierung-und-spektralsatz.html#stufe-7-7)，椭圆的主轴沿特征向量的方向，并且在曲率大的方向上较短。

::::beispiel [算例 1]
对碗形 $f(\mathbf{x})=x_1^2+4x_2^2$，$\mathbf{H}_f=\operatorname{diag}(2,\,8)$，特征值为 $2$ 和 $8$。沿 $x_1$ 方向的曲率为 $2$，沿 $x_2$ 方向为 $8$，沿方向 $\mathbf{u}=(1,\,1)^{\top}/\sqrt2$ 为 $\tfrac12(2+8)=5$。这解释了第 [4.4](richtungsableitung-und-steilster-anstieg.html#stufe-4-4) 节中拉长的等高线：沿 $x_2$ 方向，碗弯曲得强四倍，碗壁在那里更陡，椭圆在这个方向上较窄。
::::

::::beispiel [算例 2]
对 $f(\mathbf{x})=x_1^2x_2+x_2^2$，在点 $(1,\,2)$ 处，$\mathbf{H}_f=\bigl(\begin{smallmatrix}4&2\\2&2\end{smallmatrix}\bigr)$。由[第 2 章第 6.5 节](/wissen/zh/informatik/machine-learning/mathematische-grundlagen/projektion-eigenwerte-und-zerlegungen/eigenwerte-und-eigenvektoren.html#stufe-6-5)，迹 $6$ 和行列式 $4$ 给出特征值 $3\pm\sqrt5$，约为 $5.236$ 和 $0.764$。两者都是正的，黑塞矩阵正定：在 $(1,\,2)$ 附近，地形沿每个方向都向上弯曲。沿方向 $\mathbf{u}=(1,\,1)^{\top}/\sqrt2$，曲率为

$$\mathbf{u}^{\top}\mathbf{H}_f\mathbf{u}=\tfrac12\,(4+2+2+2)=5,$$

它位于 $0.764$ 与 $5.236$ 之间，见图 [16](#abb-16)。

:::abbildung ml/k3rkruemmung 16
$f(\mathbf{x})=x_1^2x_2+x_2^2$ 在点 $(1,\,2)$ 处沿角平分线方向的曲率；因子 $\tfrac12$ 来自 $u_iu_j=\tfrac12$。
:::
::::

⁠**简而言之：**沿方向 $\mathbf{u}$ 的曲率是 $\mathbf{u}^{\top}\mathbf{H}_f\mathbf{u}$；它介于黑塞矩阵的最小特征值和最大特征值之间，而这些特征值的符号决定地形像碗形还是像鞍形那样弯曲。

:::hintergrund 不建立黑塞矩阵，求黑塞矩阵与向量的乘积
变量很多时，黑塞矩阵非常庞大：有一百万个变量时，它有 $10^{12}$ 个元素。但人们常常只需要它与一个向量 $\mathbf{v}$ 的乘积。不建立这个矩阵也能得到这个乘积。数 $\nabla f(\mathbf{x})^{\top}\mathbf{v}=\sum_jv_j\,\partial_jf(\mathbf{x})$ 是 $\mathbf{x}$ 的函数，它的梯度的分量为 $\sum_jv_j\,\partial^2f/\partial x_i\partial x_j$，所以 $\nabla_{\mathbf{x}}\bigl(\nabla f(\mathbf{x})^{\top}\mathbf{v}\bigr)=\mathbf{H}_f(\mathbf{x})\,\mathbf{v}$。对 $f(\mathbf{x})=x_1^2x_2+x_2^2$ 和 $\mathbf{v}=(1,\,1)^{\top}$，$\nabla f^{\top}\mathbf{v}=2x_1x_2+x_1^2+2x_2$，其梯度为 $(2x_2+2x_1,\ 2x_1+2)^{\top}$，在点 $(1,\,2)$ 处为 $(6,\,4)^{\top}$，这正是 $\mathbf{H}_f\mathbf{v}=(4+2,\ 2+2)^{\top}$。所以要计算的是两个梯度，而不是一个有 $d^2$ 个元素的矩阵。
:::

:::aufgabe 练习 28 ★ 黑塞矩阵
<span class="anker" id="aufg-28"></span>

在给定的点处计算黑塞矩阵，并检验其对称性。

<ol class="al">

<li>

$f(\mathbf{x})=x_1^3+x_1x_2^2$，在点 $(1,\,2)$ 处；

</li>

<li>

$f(\mathbf{x})=\mathrm{e}^{x_1+2x_2}$，在点 $(0,\,0)$ 处。这个矩阵的秩是多少？

</li>

<li>

$f(\mathbf{x})=x_1x_2x_3$，在点 $(1,\,2,\,3)$ 处。

</li>

</ol>

:::loesung
(a) $\partial_1f=3x_1^2+x_2^2$，$\partial_2f=2x_1x_2$，所以

$$\mathbf{H}_f(\mathbf{x})=\begin{pmatrix}6x_1&2x_2\\2x_2&2x_1\end{pmatrix},\qquad \mathbf{H}_f(1,2)=\begin{pmatrix}6&4\\4&2\end{pmatrix};$$

混合偏导数 $\partial_2(3x_1^2+x_2^2)=2x_2$ 与 $\partial_1(2x_1x_2)=2x_2$ 相等。

(b) 由 $f=\mathrm{e}^{x_1+2x_2}$，有 $\partial_1f=f$，$\partial_2f=2f$，所以 $\mathbf{H}_f=f\cdot\bigl(\begin{smallmatrix}1&2\\2&4\end{smallmatrix}\bigr)$，在原点处为 $\bigl(\begin{smallmatrix}1&2\\2&4\end{smallmatrix}\bigr)$。第二行是第一行的两倍；秩为 $1$，特征值为 $5$ 和 $0$。这是吻合的：$f$ 只取决于 $x_1+2x_2$，沿方向 $(2,\,-1)^{\top}$ 是常数，因而在那里没有弯曲。

(c) $\partial_1f=x_2x_3$，$\partial_2f=x_1x_3$，$\partial_3f=x_1x_2$，所以

$$\mathbf{H}_f(\mathbf{x})=\begin{pmatrix}0&x_3&x_2\\x_3&0&x_1\\x_2&x_1&0\end{pmatrix},\qquad \mathbf{H}_f(1,2,3)=\begin{pmatrix}0&3&2\\3&0&1\\2&1&0\end{pmatrix}.$$
:::
:::

:::aufgabe 练习 29 ★★ 二次近似
<span class="anker" id="aufg-29"></span>

设 $f(\mathbf{x})=x_1\,\mathrm{e}^{x_2}$，与练习 [10](partielle-ableitungen-und-der-gradient.html#aufg-10) 中相同。

<ol class="al">

<li>

计算 $\mathbf{H}_f(2,0)$。

</li>

<li>

用点 $(2,\,0)$ 处的二次近似计算 $f(2.1,\ -0.05)$ 的近似值，并把它与练习 [10](partielle-ableitungen-und-der-gradient.html#aufg-10) 中的线性近似以及精确值比较。

</li>

</ol>

:::loesung
(a) $\partial_1^2f=0$，$\partial_1\partial_2f=\mathrm{e}^{x_2}$，$\partial_2^2f=x_1\mathrm{e}^{x_2}$，所以 $\mathbf{H}_f(2,0)=\bigl(\begin{smallmatrix}0&1\\1&2\end{smallmatrix}\bigr)$。

(b) 取 $\mathbf{h}=(0.1,\ -0.05)^{\top}$，有

$$\tfrac12\,\mathbf{h}^{\top}\mathbf{H}_f\mathbf{h}=\tfrac12\bigl(0+2\cdot1\cdot0.1\cdot(-0.05)+2\cdot0.05^2\bigr)=\tfrac12\,(-0.01+0.005)=-0.0025 .$$

二次近似为 $2+0-0.0025=1.9975$，线性近似为 $2.0$，精确值为 $1.997582$。误差从 $0.0024$ 降到 $0.00008$。交叉项 $-0.005$ 就是练习 [10](partielle-ableitungen-und-der-gradient.html#aufg-10) 中的交互作用。
:::
:::

:::aufgabe 练习 30 ★★ 斜置碗形的曲率
<span class="anker" id="aufg-30"></span>

设 $f(\mathbf{x})=x_1^2+4x_2^2+x_1x_2$。

<ol class="al">

<li>

把 $f$ 写成 $\tfrac12\mathbf{x}^{\top}\mathbf{H}\mathbf{x}$ 的形式，并给出 $\mathbf{H}$。

</li>

<li>

计算 $\mathbf{H}$ 的特征值，以及沿方向 $\mathbf{e}_1$、$\mathbf{e}_2$ 和 $(1,\,-1)^{\top}/\sqrt2$ 的曲率。检验式 [(8.6)](#gl-8-6)。

</li>

<li>

沿哪个方向曲率最大？给出一个特征向量。

</li>

</ol>

:::loesung
(a) 取 $\mathbf{H}=\bigl(\begin{smallmatrix}2&1\\1&8\end{smallmatrix}\bigr)$，$\tfrac12\mathbf{x}^{\top}\mathbf{H}\mathbf{x}$ 给出 $\tfrac12\,(2x_1^2+2x_1x_2+8x_2^2)=x_1^2+x_1x_2+4x_2^2$。这个矩阵也是 $f$ 的黑塞矩阵。

(b) 迹为 $10$，行列式为 $16-1=15$，所以 $\lambda^2-10\lambda+15=0$，$\lambda=5\pm\sqrt{10}$，约为 $8.162$ 和 $1.838$。曲率为 $\mathbf{e}_1^{\top}\mathbf{H}\mathbf{e}_1=2$、$\mathbf{e}_2^{\top}\mathbf{H}\mathbf{e}_2=8$，对 $\mathbf{u}=(1,\,-1)^{\top}/\sqrt2$ 为 $\tfrac12\,(2-1-1+8)=4$。三者都介于 $1.838$ 和 $8.162$ 之间。

(c) 沿属于 $\lambda=5+\sqrt{10}$ 的特征向量的方向，曲率最大。由 $(\mathbf{H}-\lambda\mathbf{I})\mathbf{v}=\mathbf{0}$ 的第一行得 $(2-\lambda)v_1+v_2=0$，所以 $\mathbf{v}=(1,\ 3+\sqrt{10})^{\top}\approx(1,\ 6.162)^{\top}$，归一化后约为 $(0.160,\ 0.987)^{\top}$。这几乎就是 $x_2$ 方向，只是被交叉项 $x_1x_2$ 稍微转动了一点。
:::
:::

:::aufgabe 练习 31 ★★★ 不相等的混合偏导数
<span class="anker" id="aufg-31"></span>

设当 $\mathbf{x}\ne\mathbf{0}$ 时 $f(x_1,x_2)=x_1x_2\,\dfrac{x_1^2-x_2^2}{x_1^2+x_2^2}$，且 $f(0,0)=0$。

<ol class="al">

<li>

用差商证明：当 $x_2\ne0$ 时 $\partial_1f(0,x_2)=-x_2$，且 $\partial_1f(0,0)=0$。用同样的方法计算 $\partial_2f(x_1,0)$。

</li>

<li>

由此推出原点处的两个混合偏导数分别为 $-1$ 和 $+1$。施瓦茨定理的哪个前提被违反了？

</li>

</ol>

:::loesung
(a) 在坐标轴 $x_1=0$ 上，$f=0$。对 $x_2\ne0$，

$$\partial_1f(0,x_2)=\lim_{h\to0}\frac{f(h,x_2)-0}{h}=\lim_{h\to0}x_2\,\frac{h^2-x_2^2}{h^2+x_2^2}=x_2\cdot\frac{-x_2^2}{x_2^2}=-x_2 .$$

在原点处，$f(h,0)=0$，所以 $\partial_1f(0,0)=0$；因此公式 $-x_2$ 对 $x_2=0$ 也成立。同样，$\partial_2f(x_1,0)=\lim_k x_1\frac{x_1^2-k^2}{x_1^2+k^2}=x_1$。

(b) 先对 $x_1$、再对 $x_2$ 求导：$\frac{\partial}{\partial x_2}(-x_2)=-1$。先对 $x_2$、再对 $x_1$ 求导：$\frac{\partial}{\partial x_1}(x_1)=+1$。原点处的两个混合偏导数不同。被违反的是二阶导数在原点处的连续性：在原点以外，混合偏导数在 $x_2$ 轴上处处为 $-1$，在 $x_1$ 轴上处处为 $+1$。所以它在原点处跳跃，而两种求导顺序是从不同的方向趋近原点的。
:::
:::
