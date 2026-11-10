---
title: 链式法则
pfad: 计算机科学 / 机器学习 / 数学基础 / 导数、梯度与链式法则
adresse: informatik/machine-learning/mathematische-grundlagen/ableitung-gradient-und-kettenregel
knoten: 第 3 章：导数、梯度与链式法则
nachschlagen: ja
order: 15230300
summary: 许多函数是把一个函数代入另一个函数得到的。链式法则说明这样一个复合函数的导数怎样由各部分的导数得出：把各级的因子相乘。这对任意多个环节的链都成立。最后介绍逻辑斯谛函数，它的导数可以用函数本身表示。
tags: 复合, 逻辑斯谛函数
lang: zh
---

<span class="anker" id="stufe-2"></span>

:::zweck
许多函数是把一个函数代入另一个函数得到的。链式法则说明这样一个复合函数的导数怎样由各部分的导数得出：把各级的因子相乘。这对任意多个环节的链都成立。最后介绍逻辑斯谛函数，它的导数可以用函数本身表示。
:::

### 复合

<span class="anker" id="stufe-2-1"></span>

函数 $(3x+1)^2$ 分两步计算：先算 $u=3x+1$，再算 $u^2$。许多公式都是这样构成的，即依次执行一些简单的步骤。认出了这种构造方式，就能由各步的导数拼出整个导数。

:::definition 定义 2.1 (复合)
<span class="anker" id="satz-2-1"></span>

如果 $g$ 和 $f$ 是函数，并且每个值 $g(x)$ 都落在 $f$ 有定义的范围内，那么称函数

$$(f\circ g)(x)=f\bigl(g(x)\bigr)$$

为 $f$ 与 $g$ 的__复合__，读作“$f$ 复合 $g$”。先作用的函数 $g$ 称为内层函数，$f$ 称为外层函数。
:::

::::beispiel [算例]
对于 $F(x)=(3x+1)^2$，内层函数是 $g(x)=3x+1$，外层函数是 $f(u)=u^2$，所以 $F=f\circ g$。在点 $1$ 处，$g(1)=4$，$F(1)=f(4)=16$。顺序很重要：$(g\circ f)(x)=g(f(x))=3x^2+1$ 是另一个函数，它在点 $1$ 处的值是 $4$。
::::

⁠**简而言之：**复合 $f\circ g$ 先作用 $g$，再作用 $f$；顺序不能交换。

### 链式法则

<span class="anker" id="stufe-2-2"></span>

$F=f\circ g$ 对 $x$ 的微小变化如何反应？可以追踪这个变化依次通过两级的过程。按照线性近似，第一级把微小变化 $\Delta x$ 大约以 $\Delta u\approx g'(x)\,\Delta x$ 的形式传递下去。第二级再把这个变化以 $\Delta y\approx f'(u)\,\Delta u$ 的形式传递下去。合起来就是 $\Delta y\approx f'(u)\,g'(x)\,\Delta x$。就像由两个传动级组成的齿轮传动一样，各级的因子相乘（图 [4](#abb-4)）。

:::abbildung ml/k3getriebe 4
把链式法则看作齿轮传动：$y=(3x+1)^2$ 在点 $1$ 处。三条数轴的比例相同。长为 $\Delta x=0.01$ 的一段（蓝色）被第一级拉伸到三倍，成为 $\Delta u=0.03$（橙色），再被第二级拉伸到大约八倍，成为 $\Delta y=0.2409\approx0.24$（红色）。
:::

:::satz 定理 2.2 (链式法则)
<span class="anker" id="satz-2-2"></span>

如果 $g$ 在点 $x$ 处可导，$f$ 在点 $g(x)$ 处可导，那么 $f\circ g$ 在点 $x$ 处可导，并且

<span class="anker" id="gl-2-1"></span>
$$(f\circ g)'(x)=f'\bigl(g(x)\bigr)\cdot g'(x). \tag{2.1}$$
:::

重要的是导数在哪里求值：$g'$ 在点 $x$ 处求值，$f'$ 却在点 $u=g(x)$ 处求值，也就是在外层函数实际工作的地方。记 $u=g(x)$，$y=f(u)$，这个法则常写成 $\frac{\mathrm{d} y}{\mathrm{d} x}=\frac{\mathrm{d} y}{\mathrm{d} u}\cdot\frac{\mathrm{d} u}{\mathrm{d} x}$。看起来好像 $\mathrm{d} u$ 约掉了。作为助记方法这很有用，但不能作为理由，因为这些符号不是分数，而是极限。

:::beweis 链式法则
设 $u=g(x)$。由线性近似式 [(1.4)](die-ableitung.html#gl-1-4)，$g(x+h)=u+g'(x)\,h+r_g(h)$，其中 $r_g(h)/h\to0$；$f(u+k)=f(u)+f'(u)\,k+r_f(k)$，其中 $r_f(k)/k\to0$；这里约定 $r_f(0)=0$。令 $k=g(x+h)-u=g'(x)\,h+r_g(h)$。于是

$$f\bigl(g(x+h)\bigr)-f(u)=f'(u)\,k+r_f(k)=f'(u)\,g'(x)\,h+f'(u)\,r_g(h)+r_f(k).$$

除以 $h$ 后，中间一项趋于 $0$。对最后一项，只要 $k\ne0$，就写成 $r_f(k)/h=\bigl(r_f(k)/k\bigr)\cdot(k/h)$；第一个因子趋于 $0$，因为 $k$ 随 $h$ 一起趋于 $0$，第二个因子趋于 $g'(x)$。如果 $k=0$，这一项本来就是 $0$。剩下的是 $f'(u)\,g'(x)$。
:::

::::beispiel [算例]
对于 $F(x)=(3x+1)^2$，有 $g'(x)=3$，$f'(u)=2u$。在点 $1$ 处，$u=g(1)=4$，所以

$$F'(1)=f'(4)\cdot g'(1)=8\cdot3=24 .$$

验算：展开后 $F(x)=9x^2+6x+1$，所以 $F'(x)=18x+6$，$F'(1)=24$。图 [4](#abb-4) 用数字展示了同一件事：$F(1.01)=4.03^2=16.2409$，而线性近似预测的是 $16+24\cdot0.01=16.24$。
::::

⁠**简而言之：**对复合函数，各级的导数相乘，每个导数都在它那一级工作的点处求值：$(f\circ g)'(x)=f'(g(x))\,g'(x)$。

### 多个环节的链

<span class="anker" id="stufe-2-3"></span>

大多数计算都不止两步。链式法则可以反复使用：有三级时，$f_3\circ f_2\circ f_1=f_3\circ(f_2\circ f_1)$，两次应用式 [(2.1)](#gl-2-1) 就得到三个因子的乘积。级数任意多时也是如此。

:::satz 定理 2.3 (多环节的链式法则)
<span class="anker" id="satz-2-3"></span>

设 $u_0=x$，$u_k=f_k(u_{k-1})$，$k=1,\dots,L$，并且每个函数 $f_k$ 都在点 $u_{k-1}$ 处可导。那么

<span class="anker" id="gl-2-2"></span>
$$\frac{\mathrm{d} u_L}{\mathrm{d} x}=f_L'(u_{L-1})\cdot f_{L-1}'(u_{L-2})\cdots f_1'(u_0). \tag{2.2}$$
:::

由此得出计算的顺序。每个因子都需要它那一级工作时的值。因此，先像普通求值那样算出中间值 $u_1,u_2,\dots$，然后才算各个因子。之后按什么顺序把这些因子相乘，对数来说无关紧要。

::::beispiel [算例]
设 $y=\dfrac1{(x^2+1)^3}$，取点 $x=1$。这条链有三个环节：

$$u_1=x^2+1=2,\qquad u_2=u_1^3=8,\qquad y=\frac1{u_2}=\frac18 .$$

各因子为 $\frac{\mathrm{d} u_1}{\mathrm{d} x}=2x=2$，$\frac{\mathrm{d} u_2}{\mathrm{d} u_1}=3u_1^2=12$，$\frac{\mathrm{d} y}{\mathrm{d} u_2}=-\frac1{u_2^2}=-\frac1{64}$，所以

$$\frac{\mathrm{d} y}{\mathrm{d} x}=2\cdot12\cdot\Bigl(-\frac1{64}\Bigr)=-\frac{24}{64}=-0.375 .$$

验算：由幂法则和链式法则，$y=(x^2+1)^{-3}$ 的导数是 $-3\,(x^2+1)^{-4}\cdot2x$，在点 $1$ 处为 $-6/16=-0.375$。
::::

⁠**简而言之：**对很长的链，导数是所有环节的导数之积；先算中间值，再算因子。

### 逻辑斯谛函数

<span class="anker" id="stufe-2-4"></span>

有些量应当平滑地位于两个界限之间，例如介于 $0$ 和 $1$ 之间的比例。逻辑斯谛函数就把每个实数映射到这个范围内，没有跳跃，没有折点，而且一直增长。它也描述饱和增长：一个量先近乎指数地增长，然后趋近一个上限。它的导数是链式法则的一个好例子，而且形式很特别。

:::definition 定义 2.4 (逻辑斯谛函数)
<span class="anker" id="satz-2-4"></span>

函数

<span class="anker" id="gl-2-3"></span>
$$\sigma(x)=\frac1{1+\mathrm{e}^{-x}} \tag{2.3}$$

称为__逻辑斯谛函数__（logistic 函数）。
:::

当 $x$ 是很大的正数时，$\mathrm{e}^{-x}$ 几乎为 $0$，$\sigma(x)$ 几乎为 $1$。当 $x$ 是绝对值很大的负数时，$\mathrm{e}^{-x}$ 极大，$\sigma(x)$ 几乎为 $0$。在点 $0$ 处，$\sigma(0)=\tfrac12$。此外有 $\sigma(-x)=1-\sigma(x)$，因为 $\frac1{1+\mathrm{e}^{x}}=\frac{\mathrm{e}^{-x}}{\mathrm{e}^{-x}+1}=1-\frac1{1+\mathrm{e}^{-x}}$；因此图像关于点 $(0,\,\tfrac12)$ 中心对称（图 [5](#abb-5)）。

:::satz 定理 2.5 (逻辑斯谛函数的导数)
<span class="anker" id="satz-2-5"></span>

有

<span class="anker" id="gl-2-4"></span>
$$\sigma'(x)=\sigma(x)\,\bigl(1-\sigma(x)\bigr). \tag{2.4}$$

导数处处为正，且至多为 $\tfrac14$；它在点 $0$ 处取得最大值 $\tfrac14$。
:::

:::herleitung 逻辑斯谛函数的导数
这个函数是一条有三个环节的链：$u_1=-x$，$u_2=1+\mathrm{e}^{u_1}$，$\sigma=1/u_2$。各因子为 $-1$、$\mathrm{e}^{u_1}=\mathrm{e}^{-x}$ 和 $-1/u_2^2$。由式 [(2.2)](#gl-2-2)，

$$\sigma'(x)=-\frac1{(1+\mathrm{e}^{-x})^2}\cdot\mathrm{e}^{-x}\cdot(-1)=\frac{\mathrm{e}^{-x}}{(1+\mathrm{e}^{-x})^2}=\frac1{1+\mathrm{e}^{-x}}\cdot\frac{\mathrm{e}^{-x}}{1+\mathrm{e}^{-x}} .$$

第一个因子是 $\sigma(x)$。第二个因子是 $\frac{(1+\mathrm{e}^{-x})-1}{1+\mathrm{e}^{-x}}=1-\sigma(x)$。由于 $\sigma(x)$ 介于 $0$ 和 $1$ 之间，两个因子都为正。对介于 $0$ 和 $1$ 之间的数 $p$，有 $p\,(1-p)=\tfrac14-(p-\tfrac12)^2\le\tfrac14$，当且仅当 $p=\tfrac12$，即 $x=0$ 时等号成立。
:::

:::abbildung ml/k3logistisch 5
逻辑斯谛函数 $\sigma$（蓝色）从 $0$ 上升到 $1$，在点 $0$ 处最陡。它的导数（红色）在那里取得最大值 $\tfrac14$，向两侧迅速变小。图中标出了算例中点 $0$ 和点 $2$ 处的值。
:::

::::beispiel [算例]
在点 $2$ 处，$\mathrm{e}^{-2}\approx0.1353$，所以 $\sigma(2)\approx1/1.1353\approx0.8808$，并且

$$\sigma'(2)=\sigma(2)\,\bigl(1-\sigma(2)\bigr)\approx0.8808\cdot0.1192\approx0.1050 .$$

一旦算出了 $\sigma(2)$，求导数就只需要一次减法和一次乘法，不必再算指数函数。在点 $10$ 处，$\sigma(10)\approx0.99995$，$\sigma'(10)\approx0.0000454$：在远处，函数几乎是水平的，输入的微小变化几乎传不到输出。
::::

⁠**简而言之：**逻辑斯谛函数 $\sigma(x)=1/(1+\mathrm{e}^{-x})$ 把每个数平滑地映射到 $0$ 与 $1$ 之间的区间内；它的导数是 $\sigma(1-\sigma)$，至多为 $\tfrac14$，并且只用函数值就能算出。

:::aufgabe 练习 5 ★ 钟形曲线
<span class="anker" id="aufg-5"></span>

设 $f(x)=\mathrm{e}^{-x^2}$。

<ol class="al">

<li>

确定内层函数和外层函数，并计算 $f'(x)$。

</li>

<li>

计算 $f'(0)$、$f'(1)$ 和 $f'(-1)$，并在图像上解释它们的符号。

</li>

</ol>

:::loesung
(a) 内层函数是 $u=-x^2$，$u'=-2x$；外层函数是 $\mathrm{e}^u$，其导数为 $\mathrm{e}^u$。由链式法则，$f'(x)=\mathrm{e}^{-x^2}\cdot(-2x)=-2x\,\mathrm{e}^{-x^2}$。

(b) $f'(0)=0$：图像在点 $0$ 处有一条水平切线，峰顶就在那里。$f'(1)=-2/\mathrm{e}\approx-0.7358$：在峰顶右侧，图像下降。$f'(-1)=2/\mathrm{e}\approx0.7358$：在峰顶左侧，图像上升。由于 $f(-x)=f(x)$，点 $\pm1$ 处的斜率大小相等、符号相反。
:::
:::

:::aufgabe 练习 6 ★★ 有三个环节的链
<span class="anker" id="aufg-6"></span>

设 $y=\sqrt{1+x^4}$。

<ol class="al">

<li>

把这个函数分解成三个环节 $u_1$、$u_2$、$y$，并在点 $x=1$ 处先算出所有中间值，再算出所有因子。

</li>

<li>

把 $\frac{\mathrm{d} y}{\mathrm{d} x}$ 在点 $1$ 处的值作为各因子之积算出来，再用一步完成的链式法则验算。

</li>

</ol>

:::loesung
(a) 三个环节是 $u_1=x^4$、$u_2=1+u_1$ 和 $y=\sqrt{u_2}$。在点 $1$ 处，中间值为 $u_1=1$、$u_2=2$ 和 $y=\sqrt2\approx1.4142$。因子为 $\frac{\mathrm{d} u_1}{\mathrm{d} x}=4x^3=4$、$\frac{\mathrm{d} u_2}{\mathrm{d} u_1}=1$ 和 $\frac{\mathrm{d} y}{\mathrm{d} u_2}=\frac1{2\sqrt{u_2}}=\frac1{2\sqrt2}\approx0.3536$。

(b) 乘积为 $4\cdot1\cdot\frac1{2\sqrt2}=\frac2{\sqrt2}=\sqrt2\approx1.4142$。一步完成：$y'=\frac1{2\sqrt{1+x^4}}\cdot4x^3$，在点 $1$ 处即为 $\frac4{2\sqrt2}=\sqrt2$。
:::
:::

:::aufgabe 练习 7 ★★ 逻辑斯谛函数的性质
<span class="anker" id="aufg-7"></span>

<ol class="al">

<li>

利用式 [(2.4)](#gl-2-4) 和 $\sigma(-x)=1-\sigma(x)$ 证明 $\sigma'(-x)=\sigma'(x)$。这对 $\sigma'$ 的图像意味着什么？

</li>

<li>

计算 $\sigma(1)$ 和 $\sigma'(1)$，精确到四位小数。

</li>

<li>

计算二阶导数 $\sigma''$，用 $\sigma$ 表示，并确定它在 $x>0$ 和 $x<0$ 时的符号。这对 $\sigma$ 的图像的曲率说明了什么？

</li>

</ol>

:::loesung
(a) 由 $\sigma(-x)=1-\sigma(x)$，得 $\sigma'(-x)=\sigma(-x)\,\bigl(1-\sigma(-x)\bigr)=\bigl(1-\sigma(x)\bigr)\,\sigma(x)=\sigma'(x)$。$\sigma'$ 的图像关于纵轴对称，如图 [5](#abb-5) 所示。

(b) $\mathrm{e}^{-1}\approx0.3679$，所以 $\sigma(1)=1/1.3679\approx0.7311$，$\sigma'(1)\approx0.7311\cdot0.2689\approx0.1966$。

(c) 用乘积法则和链式法则：$\sigma''=(\sigma-\sigma^2)'=\sigma'-2\sigma\sigma'=\sigma'\,(1-2\sigma)=\sigma(1-\sigma)(1-2\sigma)$。当 $x>0$ 时，$\sigma>\tfrac12$，所以 $1-2\sigma<0$，$\sigma''<0$：图像在那里向下弯曲。当 $x<0$ 时，$\sigma''>0$，图像向上弯曲。在点 $0$ 处，曲率改变符号；斜率在那里最大。
:::
:::

:::aufgabe 练习 8 ★★★ 反函数的导数
<span class="anker" id="aufg-8"></span>

对 $x>0$，有 $\mathrm{e}^{\ln x}=x$。

<ol class="al">

<li>

用链式法则对等式两边关于 $x$ 求导，并在假定 $\ln$ 可导的前提下推出 $(\ln x)'=1/x$。

</li>

<li>

对 $(\sqrt x)^2=x$ 作同样的处理，并与幂法则比较。

</li>

<li>

逻辑斯谛函数的反函数是 $\ell(p)=\ln\frac{p}{1-p}$，$0<p<1$。验证 $\ell(\sigma(x))=x$，并分别直接计算和借助 $\sigma'$ 计算 $\ell'(p)$。

</li>

</ol>

:::loesung
(a) 左边是一个复合函数，内层函数是 $\ln x$，外层函数是 $\mathrm{e}^u$。由链式法则，它的导数是 $\mathrm{e}^{\ln x}\cdot(\ln x)'=x\cdot(\ln x)'$。右边的导数是 $1$。所以 $x\,(\ln x)'=1$，即 $(\ln x)'=1/x$。

(b) 由 $(\sqrt x)^2=x$ 得 $2\sqrt x\cdot(\sqrt x)'=1$，所以 $(\sqrt x)'=\frac1{2\sqrt x}=\tfrac12x^{-1/2}$，恰好是 $n=\tfrac12$ 时的幂法则。

(c) 有 $1-\sigma(x)=\frac{\mathrm{e}^{-x}}{1+\mathrm{e}^{-x}}$，所以 $\frac{\sigma(x)}{1-\sigma(x)}=\frac1{\mathrm{e}^{-x}}=\mathrm{e}^x$，$\ell(\sigma(x))=\ln\mathrm{e}^x=x$。直接计算：$\ell(p)=\ln p-\ln(1-p)$，并且

$$\ell'(p)=\frac1p+\frac1{1-p}=\frac{1}{p\,(1-p)} .$$

借助 $\sigma'$：对 $\ell(\sigma(x))=x$ 求导，得 $\ell'(\sigma(x))\cdot\sigma'(x)=1$，所以 $\ell'(p)=\frac1{\sigma'(x)}=\frac1{p(1-p)}$，其中 $p=\sigma(x)$。$\sigma$ 平坦的地方，它的反函数就陡峭。
:::
:::
