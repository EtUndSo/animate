---
title: 角度与相似度
pfad: 计算机科学 / 机器学习 / 数学基础 / 向量与矩阵
knoten: 基础篇 1：向量与矩阵
nachschlagen: ja
order: 15210600
summary: 两个向量即使长度不同，也可以指向相近的方向。本节度量它们之间的夹角。其基础是一个不等式，它还确切地说明了模式比对在什么情况下反应最强。
tags: 夹角, 正交, 余弦相似度
lang: zh
---

<span class="anker" id="stufe-5"></span>

:::zweck
两个向量即使长度不同，也可以指向相近的方向。本节度量它们之间的夹角。其基础是一个不等式，它还确切地说明了模式比对在什么情况下反应最强。
:::

### 柯西-施瓦茨不等式

<span class="anker" id="stufe-5-1"></span>

在长度固定时，两个向量的点积最大能有多大？做个试验：$\mathbf{u}=(1,\,2,\,2)^{\top}$ 的长度为 $3$，$\mathbf{v}=(2,\,0,\,1)^{\top}$ 的长度为 $\sqrt5\approx2.24$。它们的点积为 $2+0+2=4$，明显小于两个长度之积 $3\cdot2.24\approx6.71$。如果改取 $\mathbf{v}=2\mathbf{u}$，即同一方向上长度为 $6$ 的向量，则 $\mathbf{u}^{\top}(2\mathbf{u})=2\cdot9=18=3\cdot6$：恰好等于两个长度之积。它不可能更大了。

:::satz 定理 5.1 (柯西-施瓦茨不等式)
<span class="anker" id="satz-5-1"></span>

对所有 $\mathbf{u},\mathbf{v}\in\mathbb{R}^d$，有

<span class="anker" id="gl-5-1"></span>
$$|\mathbf{u}^{\top}\mathbf{v}|\le\lVert\mathbf{u}\rVert\,\lVert\mathbf{v}\rVert . \tag{5.1}$$

当且仅当两个向量中的一个是另一个的倍数时，等号成立。
:::

:::beweis 柯西-施瓦茨不等式
若 $\mathbf{v}=\mathbf{0}$，两边都为零。否则，对任意数 $t$ 考虑向量 $\mathbf{u}-t\,\mathbf{v}$。它的长度的平方永远不为负，由点积的运算规则，

$$0\le\lVert\mathbf{u}-t\,\mathbf{v}\rVert^2=\lVert\mathbf{u}\rVert^2-2t\,\mathbf{u}^{\top}\mathbf{v}+t^2\lVert\mathbf{v}\rVert^2 .$$

这对每个 $t$ 都成立，因此也对 $t=\mathbf{u}^{\top}\mathbf{v}/\lVert\mathbf{v}\rVert^2$ 成立；右边作为 $t$ 的抛物线，正是在这一点取得最小值。代入得

$$0\le\lVert\mathbf{u}\rVert^2-2\,\frac{(\mathbf{u}^{\top}\mathbf{v})^2}{\lVert\mathbf{v}\rVert^2}+\frac{(\mathbf{u}^{\top}\mathbf{v})^2}{\lVert\mathbf{v}\rVert^2}=\lVert\mathbf{u}\rVert^2-\frac{(\mathbf{u}^{\top}\mathbf{v})^2}{\lVert\mathbf{v}\rVert^2}.$$

乘以 $\lVert\mathbf{v}\rVert^2>0$，就得到 $(\mathbf{u}^{\top}\mathbf{v})^2\le\lVert\mathbf{u}\rVert^2\lVert\mathbf{v}\rVert^2$；开平方即得式 [(5.1)](#gl-5-1)。

当且仅当对这个 $t$ 有 $\lVert\mathbf{u}-t\,\mathbf{v}\rVert=0$，即 $\mathbf{u}=t\,\mathbf{v}$ 时，等号成立。反过来，对 $\mathbf{u}=c\,\mathbf{v}$ 确实有 $|\mathbf{u}^{\top}\mathbf{v}|=|c|\,\lVert\mathbf{v}\rVert^2=\lVert\mathbf{u}\rVert\,\lVert\mathbf{v}\rVert$。
:::

⁠**算例：**对 $\mathbf{u}=(1,\,2,\,2)^{\top}$ 和 $\mathbf{v}=(2,\,0,\,1)^{\top}$，$|\mathbf{u}^{\top}\mathbf{v}|=4\le3\cdot\sqrt5\approx6.71$。不等号严格成立，因为 $\mathbf{v}$ 不是 $\mathbf{u}$ 的倍数。

有了这个不等式，就可以证明第 [3.4](normen-die-groe-eines-vektors.html#stufe-3-4) 小节中只作了直观论证的结论：欧几里得范数的三角不等式。我们有

$$\lVert\mathbf{u}+\mathbf{v}\rVert^2=\lVert\mathbf{u}\rVert^2+2\,\mathbf{u}^{\top}\mathbf{v}+\lVert\mathbf{v}\rVert^2\le\lVert\mathbf{u}\rVert^2+2\,\lVert\mathbf{u}\rVert\,\lVert\mathbf{v}\rVert+\lVert\mathbf{v}\rVert^2=\bigl(\lVert\mathbf{u}\rVert+\lVert\mathbf{v}\rVert\bigr)^2 ,$$

开平方即得 (N3)。

⁠**简而言之：**点积的绝对值至多等于两个长度之积，并且恰好在两个向量位于过原点的同一条直线上时等于这个积。

:::hintergrund 点积为什么能识别模式：精确的表述
在第 [2.4](das-skalarprodukt.html#stufe-2-4) 小节中，模式比对只是一个直观的图景：如果信号跟随模式，点积 $\mathbf{w}^{\top}\mathbf{x}$ 就大。柯西-施瓦茨不等式把它变成了一个精确的表述。如果只比较长度 $\lVert\mathbf{x}\rVert$ 相同的信号，那么 $\mathbf{w}^{\top}\mathbf{x}$ 总是介于 $-\lVert\mathbf{w}\rVert\,\lVert\mathbf{x}\rVert$ 和 $+\lVert\mathbf{w}\rVert\,\lVert\mathbf{x}\rVert$ 之间。恰好是模式的正倍数的那个信号取得最大值，负倍数取得最小值。所以在能量相同的所有信号中，比对对模式本身的反应最强。

⁠**算例：**交替模式 $\mathbf{w}=(1,-1,1,-1)^{\top}$ 的长度为 $2$。在所有长度为 $2$ 的信号中，$\mathbf{x}=\mathbf{w}$ 给出最大值 $4=2\cdot2$，信号 $(2,0,0,0)^{\top}$ 只给出 $2$，$\mathbf{x}=-\mathbf{w}$ 给出最小值 $-4$。

在通信工程中，这是相关接收机和匹配滤波器（matched filter）的基础。这种滤波器以时间反转的发送信号作为冲激响应；因此在采样时刻，它恰好计算接收信号与发送信号的点积。这种滤波器使信噪比达到最大，这一点正是用这个不等式证明的。
:::

### 两个向量之间的夹角

<span class="anker" id="stufe-5-2"></span>

从原点出发的两个箭头构成一个夹角。它说明两者的方向有多相似，而与它们的长短无关。在平面上，可以用量角器量出它。对于有许多分量的向量，需要一个公式，而点积提供了这个公式。

:::herleitung 平面上的点积
箭头 $\mathbf{u}$、$\mathbf{v}$ 和它们的连接箭头 $\mathbf{u}-\mathbf{v}$ 构成一个三角形。若 $\varphi$ 是 $\mathbf{u}$ 与 $\mathbf{v}$ 之间的夹角，中学几何中的余弦定理给出

$$\lVert\mathbf{u}-\mathbf{v}\rVert^2=\lVert\mathbf{u}\rVert^2+\lVert\mathbf{v}\rVert^2-2\,\lVert\mathbf{u}\rVert\,\lVert\mathbf{v}\rVert\cos\varphi .$$

由式 [(4.1)](abstande-und-einheiten.html#gl-4-1)，同一个左边等于 $\lVert\mathbf{u}\rVert^2+\lVert\mathbf{v}\rVert^2-2\,\mathbf{u}^{\top}\mathbf{v}$。比较两行，剩下

$$\mathbf{u}^{\top}\mathbf{v}=\lVert\mathbf{u}\rVert\,\lVert\mathbf{v}\rVert\cos\varphi .$$

所以在平面和空间中，点积等于两个长度之积乘以夹角的余弦。
:::

在更高维中没有量角器。所以把推导反过来，把这个公式用作定义。

:::definition 定义 5.2 (夹角)
<span class="anker" id="satz-5-2"></span>

对都不等于 $\mathbf{0}$ 的 $\mathbf{u},\mathbf{v}\in\mathbb{R}^d$，$\mathbf{u}$ 与 $\mathbf{v}$ 之间的__夹角__ $\varphi$ 是满足下式的数 $\varphi\in[0^\circ,180^\circ]$：

<span class="anker" id="gl-5-2"></span>
$$\cos\varphi=\frac{\mathbf{u}^{\top}\mathbf{v}}{\lVert\mathbf{u}\rVert\,\lVert\mathbf{v}\rVert} . \tag{5.2}$$
:::

这个定义之所以可行，只是因为由柯西-施瓦茨不等式，右边总是介于 $-1$ 和 $1$ 之间。对每个这样的数，在 $0^\circ$ 与 $180^\circ$ 之间恰有一个角与之对应。点积的符号说明夹角是锐角（$\mathbf{u}^{\top}\mathbf{v}>0$）、直角（$\mathbf{u}^{\top}\mathbf{v}=0$）还是钝角（$\mathbf{u}^{\top}\mathbf{v}<0$）。

⁠**算例：**对 $(1,\,0)^{\top}$ 和 $(1,\,1)^{\top}$，$\cos\varphi=1/\sqrt2$，所以 $\varphi=45^\circ$。对 $(1,\,0,\,1)^{\top}$ 和 $(1,\,1,\,0)^{\top}$，$\cos\varphi=\tfrac12$，所以 $\varphi=60^\circ$（图 [22](#abb-22)）。对 $\mathbf{u}=(1,\,2,\,2)^{\top}$ 和 $\mathbf{v}=(2,\,0,\,1)^{\top}$，$\cos\varphi=4/(3\sqrt5)\approx0.596$，所以 $\varphi\approx53.4^\circ$。

:::abbildung ml/k1rwinkel 22
$(1,\,0,\,1)^{\top}$ 与 $(1,\,1,\,0)^{\top}$ 之间的夹角：分子是点积，分母是两个长度。
:::

⁠**简而言之：**两个向量夹角的余弦等于它们的点积除以两个长度之积。

### 正交向量

<span class="anker" id="stufe-5-3"></span>

如果两个向量的点积为零，那么两者在对方的方向上都没有任何贡献。在平面上，这时两个箭头互相垂直。这种情况非常重要，所以有专门的名称。

:::definition 定义 5.3 (正交)
<span class="anker" id="satz-5-3"></span>

若 $\mathbf{u}^{\top}\mathbf{v}=0$，则称两个向量 $\mathbf{u},\mathbf{v}\in\mathbb{R}^d$ __正交__。
:::

若两个向量都不等于 $\mathbf{0}$，由式 [(5.2)](#gl-5-2)，它们的夹角恰为 $90^\circ$。零向量与每个向量都正交。

:::satz 定理 5.4 (勾股定理)
<span class="anker" id="satz-5-4"></span>

若 $\mathbf{u}$ 与 $\mathbf{v}$ 正交，则 $\lVert\mathbf{u}+\mathbf{v}\rVert^2=\lVert\mathbf{u}\rVert^2+\lVert\mathbf{v}\rVert^2$。
:::

这直接由 $\lVert\mathbf{u}+\mathbf{v}\rVert^2=\lVert\mathbf{u}\rVert^2+2\,\mathbf{u}^{\top}\mathbf{v}+\lVert\mathbf{v}\rVert^2$ 得出，因为中间一项为零。

⁠**算例 1：**$(1,\,2,\,2)^{\top}$ 与 $(2,\,0,\,-1)^{\top}$ 正交，因为 $2+0-2=0$。它们的和 $(3,\,2,\,1)^{\top}$ 的长度平方为 $14=9+5$。

⁠**算例 2：互不干扰的两个模式。**第 [2.4](das-skalarprodukt.html#stufe-2-4) 小节中的恒定模式 $\mathbf 1=(1,\,1,\,1,\,1)^{\top}$ 与交替模式 $\mathbf{w}=(1,\,-1,\,1,\,-1)^{\top}$ 正交，$\mathbf 1^{\top}\mathbf{w}=0$。由 $2$ 倍恒定模式和 $1$ 倍交替模式组成的信号为 $\mathbf{x}=2\cdot\mathbf 1+\mathbf{w}=(3,\,1,\,3,\,1)^{\top}$。与恒定模式比对得 $\mathbf 1^{\top}\mathbf{x}=8=2\cdot4$，与交替模式比对得 $\mathbf{w}^{\top}\mathbf{x}=4=1\cdot4$（图 [23](#abb-23)）。每次比对都恰好找到自己的那一份，再乘以 $\lVert\mathbf 1\rVert^2=\lVert\mathbf{w}\rVert^2=4$；另一份对它毫无干扰。

:::abbildung ml/k1rortho 23
两个模式正交（上）。把信号 $\mathbf{x}=2\cdot\mathbf 1+\mathbf{w}$ 分别与每个模式比对，得到该模式所占份额的 $4$ 倍。
:::

⁠**简而言之：**正交意味着点积为零；正交的箭头互相垂直，对它们勾股定理成立。

:::hintergrund 正交模式为什么互不干扰，以及这与傅里叶系数有什么关系
如果一个信号是两个正交模式的线性组合 $\mathbf{x}=\alpha\,\mathbf 1+\beta\,\mathbf{w}$，运算规则给出

$$\mathbf 1^{\top}\mathbf{x}=\alpha\,\mathbf 1^{\top}\mathbf 1+\beta\,\mathbf 1^{\top}\mathbf{w}=\alpha\,\lVert\mathbf 1\rVert^2+0 ,\qquad\text{所以}\qquad \alpha=\frac{\mathbf 1^{\top}\mathbf{x}}{\lVert\mathbf 1\rVert^2} .$$

所以与一个模式比对，只测出该模式自己的份额，因为另一个模式的贡献随因子 $\mathbf 1^{\top}\mathbf{w}=0$ 一起消失了。如果两个模式不正交，每次比对都会把另一份的一部分也算进来。

傅里叶级数的系数正是这样构成的。对周期为 $T$、$\omega_0=2\pi/T$ 的信号 $s(t)$，有

$$a_k=\frac{2}{T}\int_0^Ts(t)\cos(k\omega_0t)\,\mathrm{d} t=\frac{\int_0^Ts(t)\cos(k\omega_0t)\,\mathrm{d} t}{\int_0^T\cos^2(k\omega_0t)\,\mathrm{d} t}\qquad(k\ge1),$$

因为 $\int_0^T\cos^2(k\omega_0t)\,\mathrm{d} t=T/2$。两个函数乘积的积分起着点积的作用，而不同频率的余弦函数和正弦函数在这个意义下是正交的：它们乘积在一个周期上的积分为零。正因为如此，可以单独计算每一个傅里叶系数，而无需知道其他系数。
:::

### 余弦相似度

<span class="anker" id="stufe-5-4"></span>

有时向量的长度无关紧要。一篇文本可以用一个向量来描述，它的第 $j$ 个分量统计固定词表中第 $j$ 个词在文本中出现的次数。一篇关于一场足球比赛的详细报道，比关于同一场比赛的简短消息更频繁地出现“进球”和“球”这两个词，但比例相同。两个向量长度不同，却指向同一方向。对内容而言，重要的是方向。

:::definition 定义 5.5 (余弦相似度)
<span class="anker" id="satz-5-5"></span>

两个向量 $\mathbf{u},\mathbf{v}\ne\mathbf{0}$ 的__余弦相似度__是数

<span class="anker" id="gl-5-3"></span>
$$\frac{\mathbf{u}^{\top}\mathbf{v}}{\lVert\mathbf{u}\rVert\,\lVert\mathbf{v}\rVert}\in[-1,\,1] , \tag{5.3}$$

即它们夹角的余弦。
:::

若两个向量指向同一方向，它为 $1$；若它们正交，它为 $0$；若它们指向相反方向，它为 $-1$。把其中一个向量乘以一个正数，它不变，因为这个数会被约去。

⁠**算例：**三篇文本，以及其中“进球”“球”和“选举”这三个词的出现次数：

$$\mathbf{x}_1=(3,\,2,\,0)^{\top},\qquad \mathbf{x}_2=(6,\,4,\,0)^{\top},\qquad \mathbf{x}_3=(0,\,1,\,3)^{\top} .$$

文本 2 是关于同一场比赛、篇幅长一倍的报道；文本 3 主要关于一次选举。文本 1 与文本 2 的余弦相似度为 $1$，文本 1 与文本 3 的为 $2/\sqrt{130}\approx0.175$（图 [24](#abb-24)）。同样，文本 2 与文本 3 的也等于 $4/(\sqrt{52}\,\sqrt{10})=4/\sqrt{520}\approx0.175$。

:::abbildung ml/k1rkosinus 24
词频的两个余弦相似度：每次都是分子为点积，分母为两个长度。
:::

与此不同，距离为 $\lVert\mathbf{x}_1-\mathbf{x}_2\rVert=\sqrt{13}\approx3.61$，$\lVert\mathbf{x}_1-\mathbf{x}_3\rVert=\sqrt{19}\approx4.36$，$\lVert\mathbf{x}_2-\mathbf{x}_3\rVert=\sqrt{54}\approx7.35$。按距离，文本 1 离文本 3 几乎不比离文本 2 远，尽管文本 2 的主题与它完全相同。余弦相似度立刻就能识别出这一点：它等于 $1$，而与文本 3 的夹角约为 $79.9^\circ$，几乎是直角。

⁠**简而言之：**余弦相似度只比较两个向量的方向，而不考虑它们的长度。

:::hintergrund 余弦相似度与相关并不相同
如果先把两个分量个数相同的向量中心化（第 [4.3](abstande-und-einheiten.html#stufe-4-3) 小节），它们夹角的余弦衡量的是：各分量是否同时高于或同时低于各自的均值。这个数称为相关系数。不中心化，结果往往完全不同。例如：$\mathbf{a}=(1,2,3)^{\top}$，$\mathbf{b}=(3,4,5)^{\top}$，$\mathbf{c}=(3,2,1)^{\top}$。$\mathbf{a}$ 与 $\mathbf{b}$ 的余弦相似度约为 $0.983$，$\mathbf{a}$ 与 $\mathbf{c}$ 的也有 $0.714$，两者都明显为正。中心化后，$\tilde{\mathbf{a}}=(-1,0,1)^{\top}$，$\tilde{\mathbf{b}}=(-1,0,1)^{\top}$，$\tilde{\mathbf{c}}=(1,0,-1)^{\top}$：$\mathbf{a}$ 与 $\mathbf{b}$ 的相关系数为 $1$，而 $\mathbf{a}$ 与 $\mathbf{c}$ 的却是 $-1$，因为 $\mathbf{c}$ 恰好在 $\mathbf{a}$ 上升的地方下降。未中心化的余弦相似度之所以为正，只是因为所有的数都是正的，因而三个向量大致指向同一方向。
:::

### 点积作为影子长度

<span class="anker" id="stufe-5-5"></span>

与归一化向量的点积有一个简单的几何意义。设想一条过原点、沿归一化向量 $\mathbf{u}$ 方向的直线，让光线垂直照射到这条直线上。箭头 $\mathbf{x}$ 就会在直线上投下一个影子（图 [25](#abb-25)）。这个影子有多长？

:::abbildung ml/k1schatten 25
箭头 $\mathbf{x}=(3,1)^{\top}$ 在沿归一化向量 $\mathbf{u}=(0.6,\,0.8)^{\top}$ 方向的直线上的影子。光线垂直照射到这条直线上（虚线）。影子（浅蓝色）的长度为 $\mathbf{u}^{\top}\mathbf{x}=\lVert\mathbf{x}\rVert\cos\varphi=2.6$，终止于点 $(\mathbf{u}^{\top}\mathbf{x})\,\mathbf{u}=(1.56,\,2.08)^{\top}$。
:::

:::satz 定理 5.6 (影子长度)
<span class="anker" id="satz-5-6"></span>

设 $\mathbf{u}\in\mathbb{R}^d$ 是归一化的，即 $\lVert\mathbf{u}\rVert=1$。则 $\mathbf{u}^{\top}\mathbf{x}$ 是 $\mathbf{x}$ 在沿 $\mathbf{u}$ 方向的直线上的影子的带符号长度：影子终止于点 $(\mathbf{u}^{\top}\mathbf{x})\,\mathbf{u}$，而连接箭头 $\mathbf{x}-(\mathbf{u}^{\top}\mathbf{x})\,\mathbf{u}$ 与 $\mathbf{u}$ 正交。
:::

:::beweis 影子长度
由于 $\mathbf{u}^{\top}\mathbf{u}=\lVert\mathbf{u}\rVert^2=1$，得到 $\mathbf{u}^{\top}\bigl(\mathbf{x}-(\mathbf{u}^{\top}\mathbf{x})\,\mathbf{u}\bigr)=\mathbf{u}^{\top}\mathbf{x}-(\mathbf{u}^{\top}\mathbf{x})\,\mathbf{u}^{\top}\mathbf{u}=0$。所以连接箭头垂直于直线；这恰好是光线射来的方向。影子端点 $(\mathbf{u}^{\top}\mathbf{x})\,\mathbf{u}$ 与原点的距离为 $|\mathbf{u}^{\top}\mathbf{x}|$，因为 $\mathbf{u}$ 的长度为 $1$。若 $\mathbf{u}^{\top}\mathbf{x}>0$，它位于 $\mathbf{u}$ 的方向上；若 $\mathbf{u}^{\top}\mathbf{x}<0$，则位于相反方向上。在由 $\mathbf{x}$、影子和连接箭头构成的直角三角形中，$\mathbf{x}$ 是斜边；因此影子长度也等于 $\lVert\mathbf{x}\rVert\cos\varphi$。
:::

如果 $\mathbf{u}$ 不是归一化的，那么 $\mathbf{u}^{\top}\mathbf{x}$ 等于 $\mathbf{x}$ 在 $\mathbf{u}$ 方向上的影子长度乘以 $\lVert\mathbf{u}\rVert$。

⁠**算例：**$\mathbf{u}=(0.6,\ 0.8)^{\top}$ 是归一化的，因为 $0.36+0.64=1$。对 $\mathbf{x}=(3,\,1)^{\top}$，影子长度为 $\mathbf{u}^{\top}\mathbf{x}=2.6$，计算过程见图 [26](#abb-26)；影子端点为 $2.6\,\mathbf{u}=(1.56,\ 2.08)^{\top}$，连接箭头为 $\mathbf{x}-2.6\,\mathbf{u}=(1.44,\ -1.08)^{\top}$。它与 $\mathbf{u}$ 正交：$0.6\cdot1.44-0.8\cdot1.08=0$。由 $\lVert\mathbf{x}\rVert=\sqrt{10}\approx3.162$，得到 $\cos\varphi=2.6/3.162\approx0.822$，所以 $\varphi\approx34.7^\circ$。

:::abbildung ml/k1rschatten 26
用点积表示 $\mathbf{x}$ 在归一化向量 $\mathbf{u}$ 方向上的影子长度。
:::

对加权和而言，这意味着：如果权重是归一化的，$\mathbf{w}^{\top}\mathbf{x}$ 就说明样本 $\mathbf{x}$ 在 $\mathbf{w}$ 方向上伸展多远。所有给出相同值 $\mathbf{w}^{\top}\mathbf{x}$ 的点都投下相同的影子。因此，它们在平面上位于一条垂直于 $\mathbf{w}$ 的直线上，在空间中位于一个垂直于 $\mathbf{w}$ 的平面上。

⁠**简而言之：**对归一化向量 $\mathbf{u}$，$\mathbf{u}^{\top}\mathbf{x}$ 是 $\mathbf{x}$ 在沿 $\mathbf{u}$ 方向的直线上投下的影子的长度。

:::aufgabe 练习 12 ★ 夹角与正交
<span class="anker" id="aufg-12"></span>

<ol class="al">

<li>

计算 $(2,\,1,\,2)^{\top}$ 与 $(1,\,0,\,1)^{\top}$ 之间的夹角，并验证柯西-施瓦茨不等式。

</li>

<li>

$(1,\,1,\,0)^{\top}$ 与 $(1,\,-1,\,3)^{\top}$ 正交吗？

</li>

<li>

求一个与 $\mathbf{u}=(1,\,2)^{\top}$ 正交的向量 $\mathbf{v}\ne\mathbf{0}$，并对 $\mathbf{u}$ 和 $\mathbf{v}$ 验证勾股定理。

</li>

</ol>

:::loesung
(a) 点积为 $2+0+2=4$，长度为 $3$ 和 $\sqrt2$。所以 $\cos\varphi=4/(3\sqrt2)\approx0.943$，$\varphi\approx19.5^\circ$。柯西-施瓦茨不等式：$4\le3\sqrt2\approx4.243$。

(b) $1\cdot1+1\cdot(-1)+0\cdot3=0$：是的，它们正交。

(c) 对 $\mathbf{v}=(v_1,v_2)^{\top}$，条件要求 $v_1+2v_2=0$。一个解是 $\mathbf{v}=(2,\,-1)^{\top}$，它的每个非零倍数也都是解。验证勾股定理：$\mathbf{u}+\mathbf{v}=(3,\,1)^{\top}$ 的长度平方为 $10$，而 $\lVert\mathbf{u}\rVert^2+\lVert\mathbf{v}\rVert^2=5+5=10$。
:::
:::

:::aufgabe 练习 13 ★★ 哪篇文本相似？
<span class="anker" id="aufg-13"></span>

四篇文本，同样统计了“进球”“球”和“选举”这三个词：$\mathbf{x}_a=(2,\,0,\,1)^{\top}$，$\mathbf{x}_b=(0,\,3,\,0)^{\top}$，$\mathbf{x}_c=(4,\,0,\,2)^{\top}$，$\mathbf{x}_d=(1,\,1,\,1)^{\top}$。

<ol class="al">

<li>

计算文本 $a$ 与其他三篇文本中每一篇的余弦相似度和欧几里得距离。

</li>

<li>

按距离和按余弦相似度，分别是哪篇文本与文本 $a$ 最相似？解释其中的差别。

</li>

</ol>

:::loesung
(a) 各长度为 $\lVert\mathbf{x}_a\rVert=\sqrt5$、$\lVert\mathbf{x}_b\rVert=3$、$\lVert\mathbf{x}_c\rVert=\sqrt{20}$ 和 $\lVert\mathbf{x}_d\rVert=\sqrt3$，由此得到：

<ul>

<li>

与文本 $b$：$\mathbf{x}_a^{\top}\mathbf{x}_b=0$，余弦相似度为 $0$；距离为 $\sqrt{4+9+1}=\sqrt{14}\approx3.74$；

</li>

<li>

与文本 $c$：$\mathbf{x}_a^{\top}\mathbf{x}_c=8+0+2=10$，余弦相似度为 $10/(\sqrt5\sqrt{20})=1$；距离为 $\sqrt{4+0+1}=\sqrt5\approx2.24$；

</li>

<li>

与文本 $d$：$\mathbf{x}_a^{\top}\mathbf{x}_d=3$，余弦相似度为 $3/(\sqrt5\sqrt3)\approx0.775$；距离为 $\sqrt{1+1+0}=\sqrt2\approx1.41$。

</li>

</ul>

(b) 按距离，最近的是文本 $d$；按余弦相似度，最近的则是文本 $c$。文本 $c$ 满足 $\mathbf{x}_c=2\mathbf{x}_a$：词的分布相同，只是长了一倍，所以内容上是同一个主题。距离惩罚了较大的长度；余弦相似度只看方向。文本 $d$ 很短，因而离每一篇短文本都很近，即使没有共同的主题。要比较内容，这里合适的度量是余弦相似度，而文本 $b$ 与文本 $a$ 毫无共同之处。
:::
:::

:::aufgabe 练习 14 ★★★ 归一化向量的距离与夹角
<span class="anker" id="aufg-14"></span>

<ol class="al">

<li>

证明：对夹角为 $\varphi$ 的归一化向量 $\mathbf{u},\mathbf{v}$，有 $\lVert\mathbf{u}-\mathbf{v}\rVert^2=2-2\cos\varphi$。如果事先把所有样本都归一化，这对“按距离相似”和“按余弦相似度相似”这两种排序意味着什么？

</li>

<li>

用第 [5.4](#stufe-5-4) 小节中归一化后的文本 $\mathbf{x}_1$ 和 $\mathbf{x}_3$ 验证这个公式。

</li>

<li>

证明：当且仅当 $\mathbf{u}^{\top}\mathbf{v}=\lVert\mathbf{u}\rVert\,\lVert\mathbf{v}\rVert$ 时，$\lVert\mathbf{u}+\mathbf{v}\rVert=\lVert\mathbf{u}\rVert+\lVert\mathbf{v}\rVert$ 成立。什么情况下是这样？

</li>

</ol>

:::loesung
(a) 由式 [(4.1)](abstande-und-einheiten.html#gl-4-1)，$\lVert\mathbf{u}-\mathbf{v}\rVert^2=\lVert\mathbf{u}\rVert^2+\lVert\mathbf{v}\rVert^2-2\,\mathbf{u}^{\top}\mathbf{v}=1+1-2\cos\varphi$，因为对归一化向量有 $\mathbf{u}^{\top}\mathbf{v}=\cos\varphi$。所以距离是余弦相似度的递减函数：余弦越大，距离越小。因此，如果事先把所有样本都归一化，距离和余弦相似度给出的样本排序就完全相同。

(b) 归一化后的文本为 $\mathbf{x}_1/\sqrt{13}$ 和 $\mathbf{x}_3/\sqrt{10}$，它们夹角的余弦为 $0.1754$。公式给出 $2-2\cdot0.1754\approx1.649$。直接计算：$\mathbf{x}_1/\sqrt{13}-\mathbf{x}_3/\sqrt{10}\approx(0.832,\ 0.238,\ -0.949)^{\top}$，其长度平方为 $0.692+0.057+0.900\approx1.649$。

(c) 两边都非负，所以可以比较它们的平方。有 $\lVert\mathbf{u}+\mathbf{v}\rVert^2=\lVert\mathbf{u}\rVert^2+2\,\mathbf{u}^{\top}\mathbf{v}+\lVert\mathbf{v}\rVert^2$ 和 $(\lVert\mathbf{u}\rVert+\lVert\mathbf{v}\rVert)^2=\lVert\mathbf{u}\rVert^2+2\,\lVert\mathbf{u}\rVert\,\lVert\mathbf{v}\rVert+\lVert\mathbf{v}\rVert^2$。两者相等，当且仅当 $\mathbf{u}^{\top}\mathbf{v}=\lVert\mathbf{u}\rVert\,\lVert\mathbf{v}\rVert$。由柯西-施瓦茨不等式及其等号成立的情形，这当且仅当其中一个向量是另一个的倍数时成立，而且倍数因子必须 $\ge0$，否则点积就会是负的。直观地说：只有当三角形是扁平的、并且两个箭头指向同一方向时，三角不等式才变为等式。
:::
:::
