---
title: 点积
pfad: 计算机科学 / 机器学习 / 数学基础 / 向量与矩阵
knoten: 基础篇 1：向量与矩阵
nachschlagen: ja
order: 15210300
summary: 两个分量个数相同的向量，把它们的分量两两相乘、再把乘积相加，就得到一个数。这个计算是整个机器学习中最常用的计算：它把测量值变成估计值，并把数据与一个模式进行比对。
tags: 点积, 权重, 加权和, 模型, 预测值, 全 1 向量, 均值
lang: zh
---

<span class="anker" id="stufe-2"></span>

:::zweck
两个分量个数相同的向量，把它们的分量两两相乘、再把乘积相加，就得到一个数。这个计算是整个机器学习中最常用的计算：它把测量值变成估计值，并把数据与一个模式进行比对。
:::

### 两个向量的点积

<span class="anker" id="stufe-2-1"></span>

购物小票是这样算的：每件商品的数量乘以价格，然后全部相加。对任意两个向量做同样的计算，就称为点积。

可以把它想象成一行与一列相遇。第一个向量写成一行，第二个向量写成一列放在旁边。然后把行的第一个元素与列的第一个元素相乘，第二个与第二个相乘，依此类推，再把乘积相加：

$$\begin{pmatrix}1&2&3\end{pmatrix}\begin{pmatrix}4\\-1\\2\end{pmatrix}=1\cdot4+2\cdot(-1)+3\cdot2=8 .$$

:::definition 定义 2.1 (点积)
<span class="anker" id="satz-2-1"></span>

两个向量 $\mathbf{u},\mathbf{v}\in\mathbb{R}^d$ 的__点积__是数

<span class="anker" id="gl-2-1"></span>
$$\mathbf{u}^{\top}\mathbf{v}=\sum_{j=1}^{d}u_j\,v_j=u_1v_1+u_2v_2+\dots+u_dv_d . \tag{2.1}$$
:::

记号 $\mathbf{u}^{\top}\mathbf{v}$ 恰好说明了计算过程：$\mathbf{u}^{\top}$ 是写成一行的 $\mathbf{u}$，这一行与列 $\mathbf{v}$ 相遇。结果是一个标量，因此点积也称为标量积。

:::satz 定理 2.2 (点积的运算规则)
<span class="anker" id="satz-2-2"></span>

对所有 $\mathbf{u},\mathbf{v},\mathbf{q}\in\mathbb{R}^d$ 和每个标量 $c$，有：

<ol class="rm">

<li>

$\mathbf{u}^{\top}\mathbf{v}=\mathbf{v}^{\top}\mathbf{u}$ （对称性）；

</li>

<li>

$(c\,\mathbf{u})^{\top}\mathbf{v}=c\,(\mathbf{u}^{\top}\mathbf{v})$ 且 $(\mathbf{u}+\mathbf{q})^{\top}\mathbf{v}=\mathbf{u}^{\top}\mathbf{v}+\mathbf{q}^{\top}\mathbf{v}$ （线性，对第二个向量同样成立）；

</li>

<li>

$\mathbf{u}^{\top}\mathbf{u}=\sum_ju_j^2\ge0$，并且只有当 $\mathbf{u}=\mathbf{0}$ 时才有 $\mathbf{u}^{\top}\mathbf{u}=0$。

</li>

</ol>
:::

:::beweis 点积的运算规则
(i) 由每个分量都满足 $u_jv_j=v_ju_j$ 得出。(ii) 就是求和规则式 [(1.2)](vektoren-daten-als-zahlenlisten.html#gl-1-2)：$\sum_j(c\,u_j)v_j=c\sum_ju_jv_j$，以及 $\sum_j(u_j+q_j)v_j=\sum_ju_jv_j+\sum_jq_jv_j$。(iii) 每一项 $u_j^2$ 都非负。只有当每一项都为零，即每个 $u_j=0$ 时，和才为零。
:::

⁠**算例：**对于 $\mathbf{u}=(1,\,2,\,3)^{\top}$ 和 $\mathbf{v}=(4,\,-1,\,2)^{\top}$，得到 $\mathbf{u}^{\top}\mathbf{v}=8$ 和 $\mathbf{u}^{\top}\mathbf{u}=14$（图 [6](#abb-6)）。交换顺序，结果仍是同一个数 $\mathbf{v}^{\top}\mathbf{u}=4\cdot1+(-1)\cdot2+2\cdot3=8$，正如对称性所要求的。

:::abbildung ml/k1rskp 6
逐步计算两个点积：分量乘分量，再把乘积相加。一个向量与自身的点积就是它各分量的平方和。
:::

⁠**简而言之：**点积把两个向量逐个分量相乘，再把乘积相加；它是一个数。

:::hintergrund 同一运算的其他写法
许多书中用 $\mathbf{u}\cdot\mathbf{v}$ 或 $\langle\mathbf{u},\mathbf{v}\rangle$ 代替 $\mathbf{u}^{\top}\mathbf{v}$；英文称为 **dot product** 或 **inner product**。所指的是同一个数。本系列写作 $\mathbf{u}^{\top}\mathbf{v}$，因为从这种写法就能看出是一行与一列相遇。一旦涉及数字表格，这种写法的好处就显现出来了。
:::

### 权重与加权和

<span class="anker" id="stufe-2-2"></span>

一位房产经纪人在心里大致这样估算一套公寓的价格：每平方米约值 $3$ 千欧元，每个房间再加 $10$ 千欧元，离市中心每远一公里就减去 $4$ 千欧元。也就是说，她给每个特征乘上各自的因子，再把所有结果相加。

一个特征在这种计算中所乘的数，称为它的__权重__。一个大的正权重意味着：该特征每增加一个单位，结果就大幅上升。负权重意味着该特征使结果降低。

:::definition 定义 2.3 (加权和)
<span class="anker" id="satz-2-3"></span>

对权重向量 $\mathbf{w}=(w_1,\dots,w_d)^{\top}$ 和样本 $\mathbf{x}\in\mathbb{R}^d$，__加权和__为

<span class="anker" id="gl-2-2"></span>
$$\hat y=\mathbf{w}^{\top}\mathbf{x}=\sum_{j=1}^{d}w_j\,x_j . \tag{2.2}$$
:::

由样本的特征算出一个数的固定计算规则称为__模型__。模型对一个样本给出的数称为它的__预测值__。$\hat y$ 中 $y$ 上面的“帽子”表示这是一个计算出来的估计值，而不是测量值。在本章中，权重总是给定的；好的权重从何而来，是另一个问题。

⁠**算例：**房产经纪人使用的权重为 $\mathbf{w}=(3,\,10,\,-4)^{\top}$，单位依次是千欧元每平方米、千欧元每房间和千欧元每公里。对公寓 1，$\hat y_1=\mathbf{w}^{\top}\mathbf{x}_1=188$（图 [7](#abb-7)），即 $188$ 千欧元。

:::abbildung ml/k1rgewicht 7
房产经纪人对公寓 1 的估价：每个特征乘以它的权重，再求和。三个特征的贡献分别为 $180$、$20$ 和 $-12$ 千欧元。
:::

同样，其他公寓的预测值为 $\hat y_2=126$，$\hat y_3=286$，$\hat y_4=232$。每个乘积 $w_jx_j$ 的单位都是千欧元，因为特征的单位与权重分母中的单位相互抵消。正因为如此，这三个乘积才可以相加。

⁠**简而言之：**加权和是权重与特征的点积 $\mathbf{w}^{\top}\mathbf{x}$；它是由特征作出预测的最简单的模型。

:::hintergrund 权重大并不意味着特征重要
在房产经纪人的估价中，房间的权重 $10$ 是面积权重 $3$ 的三倍多。然而对公寓 1，面积贡献了 $180$ 千欧元，房间数只贡献了 $20$ 千欧元。原因在于：权重是按特征的每个单位计的，而面积的单位数很多。如果以 $10\,\mathrm m^2$ 为单位计量面积，公寓 1 就只有 $6$ 个单位大，同一个模型需要的权重就变成 $30$ 千欧元每 $10\,\mathrm m^2$。预测值不变，只是权重变成了原来的十倍。所以权重有多大，取决于所选的单位。要想知道一个特征对预测值贡献多少，必须看乘积 $w_jx_j$，而不能只看权重。
:::

### 用点积表示和与均值

<span class="anker" id="stufe-2-3"></span>

许多日常计算都是与一个特别简单的第二个向量的点积。最常用的是所有分量的和与平均值。

__全 1 向量__ $\mathbf 1\in\mathbb{R}^n$ 的分量全是 1。与它的点积就是把所有分量相加：$\mathbf 1^{\top}\mathbf{v}=v_1+\dots+v_n$。

:::definition 定义 2.4 (均值)
<span class="anker" id="satz-2-4"></span>

向量 $\mathbf{v}\in\mathbb{R}^n$ 各分量的__均值__为

<span class="anker" id="gl-2-3"></span>
$$\bar v=\frac1n\sum_{i=1}^nv_i=\frac1n\,\mathbf 1^{\top}\mathbf{v} . \tag{2.3}$$
:::

这类计算还有很多：与单位向量的点积取出一个分量，$\mathbf{e}_j^{\top}\mathbf{v}=v_j$，因为其余各乘积都含有一个零。向量与自身的点积是平方和，$\mathbf{v}^{\top}\mathbf{v}=\sum_iv_i^2$。数量乘以价格再求和，就得到一张账单的金额。在一点 $t$ 处计算多项式 $p(t)=c_1+c_2t+\dots+c_nt^{n-1}$ 的值，就是求它的系数 $\mathbf{c}=(c_1,\dots,c_n)^{\top}$ 与幂次 $\mathbf{z}=(1,\,t,\,t^2,\dots,t^{n-1})^{\top}$ 的点积 $\mathbf{c}^{\top}\mathbf{z}$。对于 $p(t)=1+2t+3t^2$ 和 $t=2$，结果是 $(1,\,2,\,3)\,(1,\,2,\,4)^{\top}=1+4+12=17$。

⁠**算例：**从一月到三月，公寓 1 的用电量为 $\mathbf{u}=(200,\,250,\,300)^{\top}$ kWh（第 [1.4](vektoren-daten-als-zahlenlisten.html#stufe-1-4) 小节）。总计为 $\mathbf 1^{\top}\mathbf{u}=750$ kWh，平均每月 $\bar u=250$ kWh（图 [8](#abb-8)）。二月的用电量为 $\mathbf{e}_2^{\top}\mathbf{u}=250$ kWh。

:::abbildung ml/k1rmittel 8
把用电量的和与均值写成与全 1 向量的点积，单位为 kWh。
:::

如果三个月里每千瓦时的电价为 $\mathbf{p}=(0.32,\ 0.34,\ 0.28)^{\top}$ 欧元，电费就是价格与用量的点积：$\mathbf{p}^{\top}\mathbf{u}=233$ 欧元（图 [9](#abb-9)）。每个乘积 $p_ju_j$ 是一个月的金额，单位是欧元每 kWh 乘以 kWh，即欧元。

:::abbildung ml/k1rstrom 9
把电费写成点积：每个月的价格乘以用量，再求和，单位为欧元。
:::

⁠**简而言之：**和、均值、取出一个分量以及平方和，分别是与 $\mathbf 1$、$\tfrac1n\mathbf 1$、$\mathbf{e}_j$ 和向量自身的点积。

### 点积用于模式比对

<span class="anker" id="stufe-2-4"></span>

假设要检查一个测量信号是否在相邻采样值之间来回跳变。为此，把要寻找的模式写成一个向量，这里是 $\mathbf{w}=(1,\,-1,\,1,\,-1)^{\top}$，然后求它与信号的点积。

图 [10](#abb-10) 展示了其中的过程。每个采样值都与同一位置上的模式值相乘。如果信号在某个位置上与模式同号，乘积为正；如果异号，乘积为负。如果信号处处都跟随模式，那么加起来的只有正的贡献，和就很大。如果信号与模式毫无关系，正负贡献就会相互抵消。

:::abbildung ml/k1muster 10
用点积与模式比对。上面是模式 $\mathbf{w}=(1,-1,1,-1)^{\top}$，中间是两个信号，下面是各位置 $j$ 上的乘积 $w_j\,x_j$。左边，信号 $\mathbf{x}=(2,-1,3,-2)^{\top}$ 与模式同步跳变：所有乘积都为正，和为 $8$。右边，$\mathbf{x}'=(2,2,3,3)^{\top}$ 平稳上升：乘积相互抵消，和为 $0$。
:::

更准确地说：位置 $j$ 对点积 $\mathbf{w}^{\top}\mathbf{x}$ 的贡献是 $w_jx_j$。若 $w_j$ 与 $x_j$ 同号，它为正；若异号，它为负。符号一致的位置上数值的绝对值越大，点积就越大。

在信号处理中，这种计算称为相关。两个实序列 $x[n]$ 和 $y[n]$ 在移位为零时的互相关是 $\sum_nx[n]\,y[n]$。把两个有限长信号的采样值写成向量 $\mathbf{x}$ 和 $\mathbf{y}$，这恰好就是点积 $\mathbf{x}^{\top}\mathbf{y}$。信号的能量 $\sum_nx[n]^2$ 同样是 $\mathbf{x}^{\top}\mathbf{x}$。所以模式比对并不是新工具，它正是相关器在信号中搜索已知模式时所用的那个工具。

⁠**算例：**用交替模式 $\mathbf{w}=(1,\,-1,\,1,\,-1)^{\top}$，对 $\mathbf{x}=(2,\,-1,\,3,\,-2)^{\top}$ 得 $\mathbf{w}^{\top}\mathbf{x}=8$，对 $\mathbf{x}'=(2,\,2,\,3,\,3)^{\top}$ 得 $\mathbf{w}^{\top}\mathbf{x}'=0$（图 [11](#abb-11)）。用恒定模式 $\mathbf 1=(1,\,1,\,1,\,1)^{\top}$ 时情况正好相反：$\mathbf 1^{\top}\mathbf{x}=2$，而 $\mathbf 1^{\top}\mathbf{x}'=10$。所以信号 $\mathbf{x}$ 主要在交替变化，而 $\mathbf{x}'$ 主要保持恒定。

:::abbildung ml/k1rmuster 11
交替模式 $\mathbf{w}$ 与两个信号。上面，$\mathbf{x}$ 跟随模式：四个乘积全为正。下面，$\mathbf{x}'$ 平稳上升：乘积两两抵消。
:::

房产经纪人的加权和也是一种模式比对。她的模式 $\mathbf{w}=(3,\,10,\,-4)^{\top}$ 描述了什么样的公寓值钱：面积大、房间多、距离近。一套公寓与这个模式越吻合，它的预测值就越高。

⁠**简而言之：**如果 $\mathbf{x}$ 在模式 $\mathbf{w}$ 取较大值的位置上也取同号的较大值，点积 $\mathbf{w}^{\top}\mathbf{x}$ 就大；它就是移位为零时的相关。

:::hintergrund 相关函数完全由点积组成
互相关不只在一个位置上把信号与模式比较，而是对每一种可能的移位都进行比较。对每个移位 $k$，它的值是一个点积：信号与移动了 $k$ 步的模式的点积。所以整个相关函数是一串点积，每个移位对应一个。在信号中藏有该模式的地方，正的贡献不断累积，相关函数在那里取得最大值。雷达接收机就是这样找到自身脉冲的回波，无线电接收机也是这样找到一个已知数据帧的开头。在机器学习中，移位通常固定为零：把一个样本作为整体与一个模式比较。
:::

:::aufgabe 练习 4 ★ 验证运算规则
<span class="anker" id="aufg-4"></span>

设 $\mathbf{u}=(1,\,0,\,2)^{\top}$，$\mathbf{v}=(3,\,-1,\,1)^{\top}$，$\mathbf{q}=(0,\,2,\,1)^{\top}$。计算 $\mathbf{u}^{\top}\mathbf{v}$、$\mathbf{v}^{\top}\mathbf{u}$、$\mathbf{u}^{\top}(\mathbf{v}+\mathbf{q})$、$\mathbf{u}^{\top}\mathbf{v}+\mathbf{u}^{\top}\mathbf{q}$、$(3\mathbf{u})^{\top}\mathbf{v}$ 和 $\mathbf{u}^{\top}\mathbf{u}$。每一组比较分别体现了哪条规则？

:::loesung
有 $\mathbf{u}^{\top}\mathbf{v}=3+0+2=5$ 和 $\mathbf{v}^{\top}\mathbf{u}=3+0+2=5$：点积是对称的，规则 (i)。由 $\mathbf{v}+\mathbf{q}=(3,\,1,\,2)^{\top}$，得 $\mathbf{u}^{\top}(\mathbf{v}+\mathbf{q})=3+0+4=7$，而 $\mathbf{u}^{\top}\mathbf{v}+\mathbf{u}^{\top}\mathbf{q}=5+(0+0+2)=7$：对第二个向量是线性的，规则 (ii)。此外，$(3\mathbf{u})^{\top}\mathbf{v}=(3,0,6)\,(3,-1,1)^{\top}=9+0+6=15=3\cdot5$，同样是规则 (ii)。最后，$\mathbf{u}^{\top}\mathbf{u}=1+0+4=5>0$，正如规则 (iii) 对 $\mathbf{u}\ne\mathbf{0}$ 所要求的。
:::
:::

:::aufgabe 练习 5 ★★ 房产经纪人的估价
<span class="anker" id="aufg-5"></span>

使用第 [2.2](#stufe-2-2) 小节中的权重 $\mathbf{w}=(3,\,10,\,-4)^{\top}$。

<ol class="al">

<li>

计算全部四套公寓的预测值。它们的单位是什么？

</li>

<li>

在公寓 2 中砌了一堵墙，使它在面积不变的情况下有两个房间。预测值如何变化？为什么这个变化与面积无关？

</li>

<li>

一位同事说：“对房产经纪人来说，房间最重要；它们的权重最大。”通过比较三项贡献 $w_jx_{1j}$，对公寓 1 检验这一说法。

</li>

</ol>

:::loesung
(a) 与第 [2.2](#stufe-2-2) 小节中相同：$188$、$126$、$286$ 和 $232$，单位都是千欧元。之所以是千欧元，是因为每个权重的单位都是“千欧元每特征单位”，而特征的单位在乘积中被约去。

(b) 公寓 2 变为 $(40,\,2,\,1)^{\top}$。预测值从 $126$ 升到 $120+20-4=136$，即增加 $10$。一般地，第二个特征改变 $\Delta x_2$ 时，加权和改变 $w_2\,\Delta x_2$，因为 $\mathbf{w}^{\top}(\mathbf{x}+\Delta x_2\,\mathbf{e}_2)=\mathbf{w}^{\top}\mathbf{x}+\Delta x_2\,\mathbf{w}^{\top}\mathbf{e}_2=\mathbf{w}^{\top}\mathbf{x}+\Delta x_2\,w_2$。其他特征对此不起作用。这正是点积的线性：每个特征单独作出贡献，与其他特征之间没有相互作用。

(c) 公寓 1 的三项贡献为 $w_1x_{11}=180$、$w_2x_{12}=20$ 和 $w_3x_{13}=-12$。面积的贡献远远超过其他两项，尽管它的权重按绝对值是三个中最小的。那位同事的说法把每单位的权重与对预测值的贡献混为一谈了；面积的单位数非常多。
:::
:::

:::aufgabe 练习 6 ★★ 检测上升信号的模式
<span class="anker" id="aufg-6"></span>

要检查一个含四个采样值的信号是否在上升。建议使用的模式是 $\mathbf{w}=(-3,\,-1,\,1,\,3)^{\top}$。

<ol class="al">

<li>

对 $\mathbf{x}=(1,2,3,4)^{\top}$、$(4,3,2,1)^{\top}$、$(5,5,5,5)^{\top}$ 和 $(1,3,2,4)^{\top}$ 计算 $\mathbf{w}^{\top}\mathbf{x}$，并解释结果。

</li>

<li>

为什么每个恒定信号 $c\,\mathbf1$ 给出的结果都恰好为零？请利用 $\mathbf 1^{\top}\mathbf{w}$。

</li>

</ol>

:::loesung
(a) $\mathbf{w}^{\top}(1,2,3,4)^{\top}=-3-2+3+12=10$：信号上升，结果明显为正。$\mathbf{w}^{\top}(4,3,2,1)^{\top}=-12-3+2+3=-10$：信号下降，结果同样明显为负。$\mathbf{w}^{\top}(5,5,5,5)^{\top}=-15-5+5+15=0$：恒定，没有上升。$\mathbf{w}^{\top}(1,3,2,4)^{\top}=-3-3+2+12=8$：信号总体上升，中间有一次回落，结果比平稳上升时略小。这个模式给靠前的值负权重，给靠后的值正权重；所以它响应的是：靠后的值是否大于靠前的值。

(b) $\mathbf 1^{\top}\mathbf{w}=-3-1+1+3=0$。因此，对恒定信号有 $\mathbf{w}^{\top}(c\,\mathbf 1)=c\,\mathbf{w}^{\top}\mathbf 1=c\cdot0=0$。由于各权重之和为零，这个模式完全忽略各采样值共同的直流分量：它只度量各采样值之间的差。
:::
:::
