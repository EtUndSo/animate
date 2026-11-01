---
title: 随机信号
pfad: 电气工程 / 第 3 学期 / 信号与系统 / 随机信号
order: 3270100
summary: 均值、分布、功率谱密度， 系统中的噪声与最佳接收机
tags: 样本函数, 随机过程, 随机变量, 数学期望, 自相关函数, 平稳, 各态历经, 直流分量
lang: zh
---

## 本文内容

电阻的噪声、语音、数据流：这类信号无法预测。人们不知道它们的确切波形，却知道它们的*平均性质*：它们通常有多大，变化有多快，包含哪些频率。本文说明如何描述这样的随机信号，LTI 系统对它们有什么作用，以及怎样才能最可靠地在噪声中检测出一个已知信号。

:::merke 三句话的答案（读完本文后应觉得理所当然）
<ol>

<li>

随机信号用平均值来描述：均值、功率、方差、自相关函数和概率密度函数。对于各态历经过程，可以由单个足够长的信号求出它们。

</li>

<li>

自相关函数的傅里叶变换就是功率谱密度。LTI 系统把它乘以 $|H(f)|^2$，与能量信号的情形（[第 6 部分](/wissen/zh/elektrotechnik/3-semester/signale-und-systeme/korrelationsfunktionen/korrelationsfunktionen.html)）完全一样。

</li>

<li>

在白噪声背景下，匹配滤波器 $h(t)=s(T-t)$ 是最佳的。它达到的信噪比为 $E_s/N_0$，与信号形状无关。

</li>

</ol>
:::

**所有结论背后的同一个原理。** 用平均值来代替未知的信号本身，而平均运算是线性的：

| 结论 | 来源 |
|---|---|
| 均值、功率、方差 | 集平均与时间平均（第 [1](#stufe-1) 至第 [3](#stufe-3) 阶段） |
| 自相关函数、协方差、互相关函数 | 对两个时刻取值的乘积求平均（第 [4](#stufe-4) 阶段） |
| 概率密度函数 | 在集合中或在时间上低于某一门限的比例（第 [5](#stufe-5) 阶段） |
| 独立变量之和 | 概率密度的卷积，因此趋于高斯分布（第 [6](#stufe-6)、[7](#stufe-7) 阶段） |
| 功率谱密度、维纳–李关系 | 卷积积分中数学期望的线性（第 [8](#stufe-8) 阶段） |
| 白噪声 | 恒定的功率谱密度，自相关函数 $=N_0\delta$（第 [9](#stufe-9) 阶段） |
| 匹配滤波器 | 柯西–施瓦茨不等式：信号与自身的相关最大（第 [10](#stufe-10) 阶段） |
| 误码率 | 高斯曲线位于门限另一侧的面积（第 [11](#stufe-11) 阶段） |

**如何使用本文。**每个阶段包括基本思路、可展开解答的典型问题以及练习（★ 到 ★★★）。请先自己尝试，解答可在每道练习下方展开。

:::merke 本文的参考模型
<ul>

<li>

⁠**均匀分布的随机数**，取值在 $-\frac12$ 与 $\frac12$ 之间（方差为 $\frac{1}{12}$），也用作离散时间白噪声。

</li>

<li>

⁠**电阻** $R=1\,\mathrm{k\Omega}$，温度 290 K，带宽 20 kHz（音频）。

</li>

<li>

⁠**递归系统** $g(n)=s(n)+0.6\,g(n-1)$，取自[第 4 部分](/wissen/zh/elektrotechnik/3-semester/signale-und-systeme/abtastung-und-zeitdiskrete-systeme/abtastung-und-zeitdiskrete-systeme.html)。

</li>

</ul>

脚本 `rechnung_kap7.py` 可复算这些数值，其中一部分还用模拟的随机数加以验证。
:::

## 第 1 阶段：随机过程

<span class="anker" id="stufe-1"></span>

:::zweck
怎样描述一个不知道其波形的信号？设想许多同类的信号，并对它们取平均。
:::

**思路。** 在相同温度下测量许多结构完全相同的电阻的噪声，就会得到许多不同的曲线 ${}^ks(t)$，$k=1,2,\dots$（图 [1](#abb-1)）。其中每一条称为一个__样本函数__或一个实现。所有样本函数构成的设想中的总体（集合，即样本函数族）称为__随机过程__ $s(t)$。所有样本函数在某一固定时刻 $t_1$ 的取值构成一个__随机变量__ $s(t_1)$。

:::definition 定义 1.1 (集平均)
<span class="anker" id="satz-1-1"></span>

<span class="anker" id="gl-1-1"></span>
<span class="anker" id="gl-1-2"></span>
$$\begin{aligned} \mathrm E\{s(t_1)\}&=\lim_{M\to\infty}\frac1M\sum_{k=1}^M{}^ks(t_1),\qquad \mathrm E\{F[s(t_1)]\}=\lim_{M\to\infty}\frac1M\sum_{k=1}^MF\bigl[{}^ks(t_1)\bigr],\\ \varphi_{ss}(t_1,t_2)&=\mathrm E\{s(t_1)\,s(t_2)\}. \end{aligned} \tag{1.1|1.2}$$
:::

⁠**如何理解：**$\mathrm E\{\cdot\}$ 称为__数学期望__或集平均：在同一时刻对所有样本函数取平均，也就是在图 [1](#abb-1) 中沿竖直方向取平均。取 $F[x]=x^2$，就得到均方值。__自相关函数__对两个时刻取值的乘积求平均。它表明 $t_2$ 时刻的值与 $t_1$ 时刻的值关联有多强。

:::abbildung et3/k7schar
一个随机过程的三个样本函数（模拟得到，均值为 1）。集平均沿竖直方向求取，即在同一个 $t_1$ 处对所有样本函数求平均（红色虚线）。时间平均沿水平方向求取，即沿着一个样本函数求平均。
:::

## 第 2 阶段：平稳性与各态历经性

<span class="anker" id="stufe-2"></span>

:::zweck
无限的集合是永远得不到的，通常只有单个信号。什么时候这就足够了？
:::

若把所有观测时刻都平移同一段时间 $t_0$ 时，过程的任何平均值都不改变，就称该过程是__平稳__的：

<span class="anker" id="gl-2-1"></span>
$$\mathrm E\{F[s(t_1)]\}=\mathrm E\{F[s(t_1+t_0)]\},\qquad\mathrm E\{F[s(t_1),s(t_2)]\}=\mathrm E\{F[s(t_1+t_0),s(t_2+t_0)]\}. \tag{2.1}$$

这时均值 $m_s=\mathrm E\{s(t)\}$ 是常数，而自相关函数只取决于时间差 $\tau=t_2-t_1$：$\varphi_{ss}(\tau)=\mathrm E\{s(t)s(t+\tau)\}$。如果一个平稳过程的每个样本函数的时间平均还都等于相应的集平均，就称它是__各态历经__（遍历）的：

<span class="anker" id="gl-2-2"></span>
$$\mathrm E\{F[s(t)]\}=\overline{F[{}^ks(t)]}=\lim_{T\to\infty}\frac{1}{2T}\int_{-T}^{T}F\bigl[{}^ks(t)\bigr]\,\mathrm{d} t\quad\text{对每个}\ k. \tag{2.2}$$

⁠**如何理解：**平稳意味着统计特性不随时间变化。各态历经意味着：单个样本函数只要观测得足够久，就会在时间进程中呈现出整个集合所呈现的一切。恒温下电阻的噪声是各态历经的。正因为如此，才能用单台测量仪器来表征噪声。

:::frage 每个平稳过程都是各态历经的吗？
不是。例：每个样本函数都是一个常数，其值只随机抽取一次，${}^ks(t)=c_k$。这个过程是平稳的，因为没有任何量依赖于 $t$。但样本函数的时间平均是 $c_k$，它对每个样本函数都不同，并不等于集平均。单个样本函数永远“看不到”其他的取值。
:::

## 第 3 阶段：均值、功率、方差

<span class="anker" id="stufe-3"></span>

:::zweck
最重要的一阶平均值及其直观含义。
:::

数学期望是线性的：对任意随机变量，$\mathrm E\{\sum_ia_is_i\}=\sum_ia_i\mathrm E\{s_i\}$。对平稳过程定义：

<span class="anker" id="gl-3-1"></span>
$$m_s=\mathrm E\{s(t)\},\qquad L_s=\mathrm E\{s^2(t)\},\qquad\sigma_s^2=L_s-m_s^2. \tag{3.1}$$

⁠**如何理解：**对各态历经过程，$m_s$ 就是时间平均，即信号的__直流分量__；$L_s$ 是平方的时间平均，即__功率__（[第 6 部分](/wissen/zh/elektrotechnik/3-semester/signale-und-systeme/korrelationsfunktionen/korrelationsfunktionen.html)）。__方差__ $\sigma_s^2$ 等于功率减去直流分量的功率，也就是__交流功率__。它的平方根，即__标准差__ $\sigma_s$，是交流分量的有效值。万用表拨到 AC 挡时显示 $\sigma_s$，拨到 DC 挡时显示 $m_s$。

:::aufgabe 练习 1 ★ 信号的平均值
<span class="anker" id="aufg-1"></span>

一个各态历经信号的直流分量为 2 V，有效值（包括所有分量，即“真有效值”）为 2.5 V。归一化功率、方差和标准差各是多少？

:::loesung
$L_s=2.5^2=6.25$ V$^2$，$\sigma_s^2=L_s-m_s^2=6.25-4=2.25$ V$^2$，$\sigma_s=1.5$ V。拨到 AC 挡的仪表显示 1.5 V。
:::
:::

## 第 4 阶段：自相关、协方差与互相关

<span class="anker" id="stufe-4"></span>

:::zweck
随机信号变化得有多快？自相关函数给出答案：经过时间 $\tau$ 之后，信号与自身还有多相似。
:::

:::satz 定理 4.1 (平稳过程自相关函数的性质)
<span class="anker" id="satz-4-1"></span>

<span class="anker" id="gl-4-1"></span>
$$\varphi_{ss}(0)=L_s,\qquad\varphi_{ss}(\tau)=\varphi_{ss}(-\tau),\qquad|\varphi_{ss}(\tau)|\le\varphi_{ss}(0). \tag{4.1}$$

对各态历经过程，$\varphi_{ss}(\tau)=\overline{s(t)s(t+\tau)}$，即[第 6 部分](/wissen/zh/elektrotechnik/3-semester/signale-und-systeme/korrelationsfunktionen/korrelationsfunktionen.html)中功率信号的自相关函数。
:::

:::herleitung $\tau=0$ 处的最大值
$\mathrm E\{[s(t)\pm s(t+\tau)]^2\}\ge0$，因为平方的数学期望永不为负。展开并利用线性：$\mathrm E\{s^2(t)\}+\mathrm E\{s^2(t+\tau)\}\pm2\mathrm E\{s(t)s(t+\tau)\}\ge0$，因此 $2\varphi_{ss}(0)\pm2\varphi_{ss}(\tau)\ge0$。偶对称性：在定义中作代换 $t\to t-\tau$。
:::

**协方差。** 若先减去均值，就得到__自协方差函数__

<span class="anker" id="gl-4-2"></span>
$$\mu_{ss}(\tau)=\mathrm E\{[s(t)-m_s][s(t+\tau)-m_s]\}=\varphi_{ss}(\tau)-m_s^2,\qquad\mu_{ss}(0)=\sigma_s^2. \tag{4.2}$$

若过程不含周期分量，相距很远的取值就变得相互独立：当 $\tau\to\infty$ 时，$\varphi_{ss}(\tau)\to m_s^2$，$\mu_{ss}(\tau)\to0$。

**互相关与和。** 对两个过程，$\varphi_{uv}(\tau)=\mathrm E\{u(t)v(t+\tau)\}$，且 $\varphi_{vu}(\tau)=\varphi_{uv}(-\tau)$；互协方差为 $\mu_{uv}(\tau)=\varphi_{uv}(\tau)-m_um_v$。对和 $s=u+v$，展开得

<span class="anker" id="gl-4-3"></span>
$$\varphi_{ss}(\tau)=\varphi_{uu}+\varphi_{uv}+\varphi_{vu}+\varphi_{vv},\qquad L_s=L_u+L_v+2\varphi_{uv}(0),\qquad\sigma_s^2=\sigma_u^2+\sigma_v^2+2\mu_{uv}(0). \tag{4.3}$$

⁠**简而言之：**只有当信号互不相关时，功率才直接相加。否则还要加上交叉项。两个相同的信号给出四倍的功率，两个相反的信号给出零功率。

:::aufgabe 练习 2 ★★ 两个噪声源
<span class="anker" id="aufg-2"></span>

把两个有效值分别为 3 mV 和 4 mV 的零均值噪声电压相加。在下列情况下，和的有效值是多少：(a) 二者不相关，(b) 二者形状相同（$\varphi_{uv}(0)=\sigma_u\sigma_v$），(c) 二者形状相同但符号相反（$\varphi_{uv}(0)=-\sigma_u\sigma_v$）？

:::loesung
(a) $\sigma=\sqrt{9+16}=5$ mV。(b) $\sigma^2=9+16+2\cdot12=49$，因此为 7 mV：幅度直接相加。(c) $\sigma^2=9+16-24=1$，因此为 1 mV：两个信号几乎相互抵消。
:::
:::

## 第 5 阶段：分布函数与概率密度

<span class="anker" id="stufe-5"></span>

:::zweck
平均值并不能说明一切。信号取各个值的频繁程度如何？这由分布来描述。
:::

:::definition 定义 5.1 (分布)
<span class="anker" id="satz-5-1"></span>

<span class="anker" id="gl-5-1"></span>
$$P_s(x)=\mathrm{Prob}[s(t)\le x],\qquad p_s(x)=\frac{\mathrm{d} P_s(x)}{\mathrm{d} x},\qquad P_s(x)=\int_{-\infty}^xp_s(\xi)\,\mathrm{d}\xi. \tag{5.1}$$
:::

⁠**如何理解：**__分布函数__ $P_s(x)$（累积分布函数）是集合中信号低于门限 $x$ 的部分所占的比例（对各态历经过程：信号低于门限 $x$ 的时间所占的比例）。它从 $P_s(-\infty)=0$ 单调上升到 $P_s(\infty)=1$。__概率密度函数__ $p_s(x)$ 永不为负，面积为 1，而 $p_s(x)\,\mathrm{d} x$ 是信号落在 $x$ 与 $x+\mathrm{d} x$ 之间的概率。由它可以得到所有的一阶平均值：

<span class="anker" id="gl-5-2"></span>
$$m_s=\int x\,p_s(x)\,\mathrm{d} x,\qquad L_s=\int x^2p_s(x)\,\mathrm{d} x,\qquad\mathrm E\{F[s]\}=\int F(x)\,p_s(x)\,\mathrm{d} x. \tag{5.2}$$

**例：均匀分布。** 在以 $m_s$ 为中心、宽度为 $a$ 的区间内，所有取值出现的可能性都相同：$p_s(x)=\frac1a\operatorname{rect}\bigl(\frac{x-m_s}{a}\bigr)$。于是

$$L_s=\frac1a\int_{m_s-a/2}^{m_s+a/2}x^2\mathrm{d} x=\frac{a^2}{12}+m_s^2,\qquad\sigma_s^2=\frac{a^2}{12}.$$

参考模型中的随机数（$a=1$，$m_s=0$）的方差为 $\frac1{12}=0.0833$。

**特性曲线。** 若信号通过一条特性曲线（传输特性）$y=k(x)$（带饱和的放大器、整流器、量化器），它的分布就会改变。对单调的特性曲线，每个区间的概率保持不变：

<span class="anker" id="gl-5-3"></span>
$$p_g(y)\,|\mathrm{d} y|=p_s(x)\,|\mathrm{d} x|\qquad\Longrightarrow\qquad p_g(y)=\frac{p_s(x)}{|k'(x)|},\qquad P_g\bigl(k(x)\bigr)=P_s(x)\ \ (k\ \text{单调递增}). \tag{5.3}$$

特性曲线陡峭的地方，取值被分散到较宽的范围内，概率密度随之减小。利用这一规则，可以把任意分布变换成所需的分布。例：$k(x)=(2|x|-x^2)\operatorname{sgn}x$ 把 $[-1,1]$ 上的三角分布变换为均匀分布（练习 [4](#aufg-4)）。

**量化。** __量化器__把每个值替换为 $M$ 个量化电平中最接近的那一个。若各电平均匀分布、间隔为 $\Delta$，且没有过载，则误差在 $-\frac\Delta2$ 与 $\frac\Delta2$ 之间近似均匀分布，因而方差为 $\frac{\Delta^2}{12}$。对于在全部 $M$ 个电平上均匀分布的信号（方差为 $\frac{(M\Delta)^2}{12}$），信噪比为 $M^2$，用分贝表示为 $20\lg M\approx6\,\text{dB/比特}$：8 比特时为 48 dB，16 比特时为 96 dB。

:::aufgabe 练习 3 ★ 均匀分布
<span class="anker" id="aufg-3"></span>

一个信号在 1 V 与 3 V 之间均匀分布。计算 $m_s$、$L_s$、$\sigma_s^2$ 以及信号高于 2.5 V 的概率。

:::loesung
$a=2$ V，$m_s=2$ V。$\sigma_s^2=\frac{a^2}{12}=\frac13$ V$^2$，$L_s=\frac13+4=4.33$ V$^2$。区间的四分之一位于 2.5 V 以上，因此 $\mathrm{Prob}=\frac{0.5}{2}=0.25$。
:::
:::

:::aufgabe 练习 4 ★★ 变换分布
<span class="anker" id="aufg-4"></span>

一个信号在 $[-1,1]$ 上具有三角形概率密度 $p_s(x)=\Lambda(x)$。

<ol class="al">

<li>

求 $0\le x\le1$ 时的 $P_s(x)$。

</li>

<li>

利用式 [(5.3)](#gl-5-3) 证明：$x\ge0$ 时取 $k(x)=(2x-x^2)$（并作奇延拓），就得到 $[-1,1]$ 上的均匀分布。提示：对均匀分布，$P_g(y)=\frac12+\frac y2$。

</li>

</ol>

:::loesung
(a) 当 $0\le x\le1$ 时，$P_s(x)=\frac12+\int_0^x(1-\xi)\,\mathrm{d}\xi=\frac12+x-\frac{x^2}{2}$。

(b) 根据式 [(5.3)](#gl-5-3)，必须有 $P_g(k(x))=P_s(x)$，即 $\frac12+\frac{k(x)}{2}=\frac12+x-\frac{x^2}{2}$。由此得 $k(x)=2x-x^2$。特性曲线在 $x=0$ 处陡峭（斜率为 2），那里三角形概率密度最大；在边缘处则很平缓。这样，频繁出现的值被拉开，稀少的值被挤拢。模拟得到一个高度为 0.5 的平坦直方图。
:::
:::

:::aufgabe 练习 4a ★★★ （拓展阅读）最佳量化器
<span class="anker" id="aufg-4a"></span>

一个量化器的门限为 $u_i$，量化电平值为 $v_i$（当 $u_i<x\le u_{i+1}$ 时取电平 $i$），其均方误差为 $N_q=\sum_i\int_{u_i}^{u_{i+1}}(v_i-x)^2p_s(x)\,\mathrm{d} x$。

<ol class="al">

<li>

通过对 $v_i$ 求导证明：在最佳点，$v_i$ 位于概率密度在其区间上的质心处。

</li>

<li>

通过对 $u_i$ 求导证明：在最佳点，$u_i$ 恰好位于 $v_{i-1}$ 与 $v_i$ 的正中间。

</li>

<li>

为什么对均匀分布的信号，均匀量化器是最佳的？

</li>

</ol>

:::loesung
(a) $\frac{\partial N_q}{\partial v_i}=\int_{u_i}^{u_{i+1}}2(v_i-x)p_s(x)\mathrm{d} x=0$，因此 $v_i=\dfrac{\int_{u_i}^{u_{i+1}}x\,p_s\,\mathrm{d} x}{\int_{u_i}^{u_{i+1}}p_s\,\mathrm{d} x}$，即质心。

(b) $u_i$ 既是区间 $i-1$ 的上限，又是区间 $i$ 的下限：$\frac{\partial N_q}{\partial u_i}=(v_{i-1}-u_i)^2p_s(u_i)-(v_i-u_i)^2p_s(u_i)=0$，因此 $u_i=\frac12(v_{i-1}+v_i)$。每个值被分配给电平值离它更近的那个电平。

(c) 对于恒定的概率密度，每个区间的质心就是它的中点。宽度相等、以各自中点为电平值的区间满足这两个条件，量化间隔为 $\Delta=a/M$。
:::
:::

## 第 6 阶段：联合分布、独立与不相关

<span class="anker" id="stufe-6"></span>

:::zweck
同时考虑两个随机变量：它们何时相互关联？对它们的和又能得出什么？
:::

两个变量的__联合分布__为 $P_{sg}(x,y)=\mathrm{Prob}[s\le x\ \text{且}\ g\le y]$，其密度（联合概率密度）为 $p_{sg}=\frac{\partial^2P_{sg}}{\partial x\,\partial y}$。由它可以得到每个变量各自的分布（$P_{sg}(x,\infty)=P_s(x)$）以及相关 $\varphi_{sg}=\iint xy\,p_{sg}(x,y)\,\mathrm{d} x\,\mathrm{d} y$。对于联合平稳的过程，一切都只取决于 $s(t)$ 与 $g(t+\tau)$ 之间的时移 $\tau$。

:::definition 定义 6.1 (独立，不相关)
<span class="anker" id="satz-6-1"></span>

若 $p_{sg}(x,y)=p_s(x)\,p_g(y)$，则称 $s$ 和 $g$ __统计独立__。若 $\mu_{sg}=\varphi_{sg}-m_sm_g=0$，则称它们__不相关__。
:::

由独立可以推出不相关：$\varphi_{sg}=\int xp_s\mathrm{d} x\cdot\int yp_g\mathrm{d} y=m_sm_g$。反之则不成立：不相关只意味着不存在*线性*关系（练习 [5](#aufg-5)）。

**两个独立变量之和。** 只要 $f=u$ 且 $g=x-u$（$u$ 任意），和 $s=f+g$ 就取值 $x$：

<span class="anker" id="gl-6-1"></span>
$$p_s(x)=\int_{-\infty}^{\infty}p_{fg}(u,x-u)\,\mathrm{d} u=p_f(x)*p_g(x)\quad(\text{独立}). \tag{6.1}$$

这就是[第 1 部分](/wissen/zh/elektrotechnik/3-semester/signale-und-systeme/lti-systeme-und-faltung/lti-systeme-und-faltung.html)中的卷积，它在那里出现于掷骰子的例子中。两个均匀分布变量之和具有三角形概率密度，三个变量之和的概率密度已近似呈钟形（图 [2](#abb-2)）。

:::abbildung et3/k7summen
独立随机变量之和的概率密度函数，每个变量都在 $[-\frac12,\frac12]$ 上均匀分布。仅仅三个变量之和，就已接近具有相同方差的高斯曲线（在 $x=0$ 处：0.75 对 0.80）。
:::

:::aufgabe 练习 5 ★★ 不相关，却不独立
<span class="anker" id="aufg-5"></span>

$s$ 在 $[-1,1]$ 上均匀分布，$g=s^2$。证明 $s$ 与 $g$ 不相关，尽管 $g$ 完全由 $s$ 决定。

:::loesung
$m_s=0$，且 $\mathrm E\{sg\}=\mathrm E\{s^3\}=\frac12\int_{-1}^1x^3\mathrm{d} x=0$，因此 $\mu_{sg}=0-0\cdot m_g=0$：不相关。尽管如此，$s$ 决定了 $g$ 的值。这种关系是二次的，而相关只能反映线性关系：对正的 $s$，$g$ 随 $s$ 增大而增大；对负的 $s$，$g$ 随 $s$ 增大而减小；平均起来，这两种趋势相互抵消。
:::
:::

## 第 7 阶段：高斯分布

<span class="anker" id="stufe-7"></span>

:::zweck
为什么噪声常常服从高斯分布？怎样用高斯分布进行计算？
:::

把许多概率密度相互卷积，结果就趋于一条高斯曲线（__中心极限定理__，[第 3 部分](/wissen/zh/elektrotechnik/3-semester/signale-und-systeme/fourier-reihe-und-transformation/fourier-reihe-und-transformation.html)）。噪声通常是非常多微小的独立贡献之和，例如许多电子的运动。因此它服从高斯分布。

:::satz 定理 7.1 (高斯（正态）分布)
<span class="anker" id="satz-7-1"></span>

<span class="anker" id="gl-7-1"></span>
$$p_s(x)=\frac{1}{\sqrt{2\pi\sigma_s^2}}\,\mathrm{e}^{-(x-m_s)^2/(2\sigma_s^2)},\qquad P_s(x)=\frac12+\frac12\operatorname{erf}\Bigl(\frac{x-m_s}{\sqrt{2\sigma_s^2}}\Bigr)=\frac12\operatorname{erfc}\Bigl(\frac{m_s-x}{\sqrt{2\sigma_s^2}}\Bigr) \tag{7.1}$$

其中__误差函数__ $\operatorname{erf}(x)=\frac{2}{\sqrt\pi}\int_0^x\mathrm{e}^{-\xi^2}\mathrm{d}\xi$，$\operatorname{erfc}=1-\operatorname{erf}$。
:::

⁠**如何理解：**均值和方差完全确定了高斯分布。在均值周围 $\pm\sigma_s$ 的范围内有 68.3 % 的取值，$\pm2\sigma_s$ 内有 95.4 %，$\pm3\sigma_s$ 内有 99.73 %。高斯曲线的积分没有闭合形式，因此引入函数 erf，它可以查表或用数值方法计算。对于大的 $x$，$\operatorname{erfc}(x)\approx\frac{\mathrm{e}^{-x^2}}{\sqrt\pi\,x}$。

**计算规则。** 两个独立的高斯变量之和仍服从高斯分布，且 $m_s=m_1+m_2$，$\sigma_s^2=\sigma_1^2+\sigma_2^2$。高斯过程通过 LTI 系统后仍是高斯过程，因为卷积积分是一个（无限的）加权和。此外，对于两个联合高斯变量，“不相关”与“独立”是一回事：若归一化互协方差 $\rho=\mu_{sg}/(\sigma_s\sigma_g)$ 为零，联合概率密度就分解为乘积。

:::zusatz 二维高斯概率密度
对于零均值、联合高斯分布、相关系数为 $\rho$ 的 $s,g$，

$$p_{sg}(x,y)=\frac{1}{2\pi\sigma_s\sigma_g\sqrt{1-\rho^2}}\exp\Bigl(-\frac{\sigma_g^2x^2+\sigma_s^2y^2-2\rho\sigma_s\sigma_gxy}{2\sigma_s^2\sigma_g^2(1-\rho^2)}\Bigr).$$

它可以借助归一化的和变量与差变量 $\frac{s}{\sigma_s}\pm\frac{g}{\sigma_g}$ 求得：这两个变量互不相关，方差为 $2(1\pm\rho)$，并且由于服从高斯分布而相互独立。等概率密度线是椭圆；在归一化坐标 $x/\sigma_s$、$y/\sigma_g$ 中，椭圆的轴沿着这些和与差的方向。当 $\rho=0$ 时，它们变为圆（在 $\sigma_s=\sigma_g$ 时），概率密度等于两个单独概率密度的乘积。
:::

:::aufgabe 练习 6 ★ 用高斯分布计算
<span class="anker" id="aufg-6"></span>

一个噪声电压服从高斯分布，$m=0$，$\sigma=1$ mV。

<ol class="al">

<li>

它大于 2 mV 的概率是多少？（提示：$\operatorname{erfc}(1.414)=0.0455$。）

</li>

<li>

把两个这样的独立电压相加。和服从什么分布？

</li>

</ol>

:::loesung
(a) $\mathrm{Prob}[x>2\,\mathrm{mV}]=\frac12\operatorname{erfc}\bigl(\frac{2}{\sqrt2}\bigr)=\frac12\operatorname{erfc}(1.414)=0.023$，即 2.3 %。

(b) 服从高斯分布，$m=0$，$\sigma^2=2$ mV$^2$，$\sigma=1.41$ mV。
:::
:::

## 第 8 阶段：LTI 系统中的随机信号与功率谱密度

<span class="anker" id="stufe-8"></span>

:::zweck
LTI 系统对随机信号有什么作用？每个样本函数都被卷积。因此，平均值遵循简单的规则。
:::

**均值。** 对每个样本函数有 ${}^kg={}^ks*h$。数学期望是线性的，可以移入卷积积分之中：

<span class="anker" id="gl-8-1"></span>
$$m_g=\mathrm E\Bigl\{\int s(\tau)h(t-\tau)\mathrm{d}\tau\Bigr\}=\int\mathrm E\{s(\tau)\}\,h(t-\tau)\,\mathrm{d}\tau=m_s\int h\,\mathrm{d}\tau=m_s\,H(0). \tag{8.1}$$

均值像直流分量一样被传输。

:::satz 定理 8.1 (平稳过程的维纳–李关系)
<span class="anker" id="satz-8-1"></span>

<span class="anker" id="gl-8-2"></span>
$$\varphi_{gg}(\tau)=\varphi_{ss}(\tau)*\varphi^E_{hh}(\tau),\qquad\Phi_{gg}(f)=\Phi_{ss}(f)\,|H(f)|^2, \tag{8.2}$$

其中 $\varphi^E_{hh}(\tau)=\int h(\vartheta)h(\vartheta+\tau)\mathrm{d}\vartheta$ 是冲激响应的自相关函数（确定性自相关函数），$\Phi_{ss}(f)\;\bullet\!\!-\!\!\circ\;\varphi_{ss}(\tau)$ 称为__功率谱密度__。功率为

<span class="anker" id="gl-8-3"></span>
$$L_s=\varphi_{ss}(0)=\int_{-\infty}^{\infty}\Phi_{ss}(f)\,\mathrm{d} f. \tag{8.3}$$
:::

:::herleitung 维纳–李关系
写出两个卷积积分，使用不同的积分变量：

$$g(t)g(t+\tau)=\iint s(t-\alpha)\,s(t+\tau-\beta)\,h(\alpha)h(\beta)\,\mathrm{d}\alpha\,\mathrm{d}\beta.$$

把数学期望移入二重积分。对平稳过程，$\mathrm E\{s(t-\alpha)s(t+\tau-\beta)\}=\varphi_{ss}(\tau-\beta+\alpha)$。令 $\vartheta=\beta-\alpha$：

$$\varphi_{gg}(\tau)=\int\varphi_{ss}(\tau-\vartheta)\underbrace{\int h(\alpha)h(\alpha+\vartheta)\,\mathrm{d}\alpha}_{\varphi^E_{hh}(\vartheta)}\,\mathrm{d}\vartheta=\varphi_{ss}*\varphi^E_{hh}.$$

在频域中，$\varphi^E_{hh}$ 变为 $|H|^2$（[第 6 部分](/wissen/zh/elektrotechnik/3-semester/signale-und-systeme/korrelationsfunktionen/korrelationsfunktionen.html)）。
:::

⁠**如何理解：**$\Phi_{ss}(f)$ 表示功率如何分布在各个频率上。它是实的，永不为负，对实信号而言是偶函数。LTI 系统把每个频率上的功率乘以 $|H(f)|^2$，系统的相位不起作用。这与[第 6 部分](/wissen/zh/elektrotechnik/3-semester/signale-und-systeme/korrelationsfunktionen/korrelationsfunktionen.html)中能量信号的规则相同，只是现在用于随机过程。（注：严格地说，$\Phi_{ss}$ 定义为对持续时间为 $T$ 的信号片段的短时频谱所取的极限 $\lim_{T\to\infty}\frac1T\mathrm E\{|S_T(f)|^2\}$。这一极限与自相关函数的傅里叶变换相同，这才是维纳–辛钦定理真正的内容。）

:::ltspice 带均值的噪声通过低通和高通
⁠**绘制：**行为源 `bv` 接在节点 `s` 上，取 `V=1+white(1e3*time)`。`white(x)` 给出 $-0.5$ 与 $0.5$ 之间的随机值，在每个整数 $x$ 处取一个新值，相邻值之间平滑过渡，因此这里每毫秒取一个新值。与它并联一个 RC 低通（`res` 取 `1Meg`，接到 `tp`；`cap` 取 `1u`，接地）和一个 CR 高通（`cap` 取 `1u`，接到 `hp`；`res` 取 `1Meg`，接地）。

⁠**指令：**`.tran 0 200 0 0.1m`。

⁠**读数：**把显示范围缩放到 20 s 至 200 s，即暂态过程结束之后的时间段。按住 Ctrl 键单击曲线名称，就会显示可见范围内的均值（Average）和有效值（RMS）。

⁠**你会看到：**输入的均值为 1 V。把 `V(tp)` 和 `V(hp)` 的均值与你在练习 [7](#aufg-7) 中的结果比较。低通输出的起伏要小得多：画出 `V(s)-1` 和 `V(tp)-1`，它们的有效值约为 0.25 和 0.01。低通大致只让宽广的功率谱密度中低于 $1/(2\pi RC)=0.16$ Hz 的部分通过，而根据式 [(8.3)](#gl-8-3)，功率就是功率谱密度曲线下的面积。
:::

:::aufgabe 练习 7 ★ 均值通过滤波器
<span class="anker" id="aufg-7"></span>

均值为 1 V 的噪声分别通过一个 RC 低通滤波器和一个 CR 高通滤波器。两个输出的均值各是多少？为什么？

:::loesung
RC 低通滤波器：$H(0)=1$，均值为 1 V。CR 高通滤波器：$H(0)=0$，均值为 0。电容不让直流电流通过，因此直流分量被阻断。
:::
:::

## 第 9 阶段：白噪声与热噪声

<span class="anker" id="stufe-9"></span>

:::zweck
最重要的干扰模型：在所有频率上功率谱密度都相同的噪声。
:::

:::definition 定义 9.1 (白噪声)
<span class="anker" id="satz-9-1"></span>

对所有 $f$ 都有 $\Phi_{ss}(f)=N_0$ 的零均值过程称为__白噪声__。它的自相关函数为 $\varphi_{ss}(\tau)=N_0\,\delta(\tau)$。
:::

⁠**如何理解：**不同时刻的取值互不相关，无论它们靠得多近。功率 $\int N_0\mathrm{d} f$ 为无穷大：白噪声是一种极限模型，就像狄拉克冲激一样。实际测到的总是经过滤波的噪声，即“有色”噪声：

<span class="anker" id="gl-9-1"></span>
$$\Phi_{gg}(f)=N_0|H(f)|^2,\qquad\varphi_{gg}(\tau)=N_0\,\varphi^E_{hh}(\tau),\qquad L_g=N_0\int|h(t)|^2\mathrm{d} t=N_0\int|H(f)|^2\mathrm{d} f. \tag{9.1}$$

在截止频率为 $f_\mathrm g$ 的理想低通之后：$L_g=2N_0f_\mathrm g$，$\varphi_{gg}(\tau)=2N_0f_\mathrm g\operatorname{si}(2\pi f_\mathrm g\tau)$（图 [3](#abb-3)）。自相关函数在 $\tau=k/(2f_\mathrm g)$（$k\neq0$）处为零：以奈奎斯特率采得的样本值互不相关。

:::abbildung et3/k7tp
白噪声通过理想低通后的自相关函数：$2N_0f_\mathrm g\operatorname{si}(2\pi f_\mathrm g\tau)$。在 $\tau=0$ 处它等于功率 $2N_0f_\mathrm g$。在红点处（$\tau=k/(2f_\mathrm g)$）它为零。
:::

**热噪声。** 电子的热运动在每个电阻 $R$ 上产生噪声电压。在开路状态下，在频率范围 $|f|\le f_\mathrm g$ 内测量：

<span class="anker" id="gl-9-2"></span>
$$\mathrm E\{u^2\}=4kT_\mathrm{abs}Rf_\mathrm g,\qquad N_0=2kT_\mathrm{abs}R,\qquad L_{\max}=kT_\mathrm{abs}f_\mathrm g, \tag{9.2}$$

其中玻尔兹曼常数 $k=1.38\cdot10^{-23}$ W s/K。在室温（290 K）下，$kT\approx4\cdot10^{-21}$ W/Hz，即每 GHz 带宽 4 pW。$L_{\max}$ 是在功率匹配时最多能从电阻取出的功率。在参考模型中（$1\,\mathrm{k\Omega}$，20 kHz），有效值为 $\sqrt{\mathrm E\{u^2\}}=0.57$ µ V。这个数量级限制了传声器放大器所能达到的灵敏度。频谱直到约 $10^{12}$ Hz 都是平坦的。

:::ltspice 测量热噪声
LTspice 为每个电阻都加上它的热噪声。`.noise` 分析计算某个节点上的噪声密度 `V(onoise)`，单位为 V$/\sqrt{\mathrm{Hz}}$。测量语句 `.meas noise urms INTEG V(onoise)` 在分析的频率范围内对它按平方积分（如式 [(8.3)](#gl-8-3)），并给出有效值。`.temp 16.85` 把温度设为 290 K。

⁠**电阻：**`res` 取 `{Rx}`，从节点 `a` 接地；与它并联一个值为 0 的电流源 `current`（名称为 `I1`）。它不构成任何负载，`.noise` 只是把它用作参考源。指令 `.param Rx=1k` 和 `.noise V(a) I1 lin 20001 1 20k`。结果：4.0 nV$/\sqrt{\mathrm{Hz}}$，`urms` $=0.57$ µ V，与上文相同。设 `Rx=1Meg`，并与你在练习 [8](#aufg-8) 中的结果比较。

⁠**$kT/C$：**电压源 `voltage` `V1`，值为 0 和 `AC 1`；`res` 取 `{Rx}`，接到 `out`；`cap` 取 `1p`，接地。指令 `.step param Rx list 1k 1Meg` 和 `.noise V(out) V1 dec 200 1 1T`，再加上 `.temp 16.85` 以及同样的测量语句 `urms`。两个电阻得到的 `urms` 相同。把这个值与你在练习 [9](#aufg-9)(b) 中的结果比较。
:::

:::aufgabe 练习 8 ★ 电阻的噪声
<span class="anker" id="aufg-8"></span>

计算一个 $1\,\mathrm{M\Omega}$ 电阻在 290 K、20 kHz 带宽下的噪声电压有效值。它是 $1\,\mathrm{k\Omega}$ 电阻的多少倍？为什么恰好是这个倍数？

:::loesung
有效值随 $\sqrt R$ 增长：变为 $\sqrt{1000}=31.6$ 倍，因此为 $0.566\cdot31.6=17.9$ µ V。
:::
:::

:::aufgabe 练习 9 ★★ $kT/C$ 噪声
<span class="anker" id="aufg-9"></span>

电阻的热噪声（$N_0=2kTR$）通过该电阻与电容 $C$ 构成的 RC 电路（$h(t)=\frac{1}{RC}\mathrm{e}^{-t/RC}\varepsilon(t)$）。

<ol class="al">

<li>

利用式 [(9.1)](#gl-9-1) 证明：电容上的噪声功率为 $kT/C$，与 $R$ 无关。

</li>

<li>

当 $C=1$ pF、温度为 290 K 时，有效值是多少？为什么在这里减小电阻无济于事？

</li>

</ol>

:::loesung
(a) $\int h^2\mathrm{d} t=\frac{1}{(RC)^2}\int_0^\infty\mathrm{e}^{-2t/RC}\mathrm{d} t=\frac{1}{2RC}$。因此 $L=N_0\cdot\frac{1}{2RC}=\frac{2kTR}{2RC}=\frac{kT}{C}$。

(b) $\sqrt{4\cdot10^{-21}/10^{-12}}\,\mathrm{V}=\sqrt{4\cdot10^{-9}}\,\mathrm{V}=63$ µ V。较小的电阻在每赫兹上产生的噪声确实较少，但 RC 电路的频带随之变宽（$1/RC$ 变大）。两种效应恰好相互抵消。只有更大的电容才能减小噪声。
:::
:::

## 第 10 阶段：匹配滤波器（相关滤波器）

<span class="anker" id="stufe-10"></span>

:::zweck
一个已知的脉冲 $s(t)$ 受噪声干扰后到达。用什么样的滤波器，才能使它在采样时刻 $T$ 显现得最清楚？
:::

**出发点。** 接收机输入端为 $s(t)+n(t)$，其中 $n$ 为白噪声。滤波器 $h$ 输出 $y=g+n_e$，其中有用分量为 $g=s*h$，噪声分量为 $n_e=n*h$。在 $T$ 时刻采样。该时刻的信噪比为

$$\frac{S_a}{N}=\frac{g^2(T)}{\mathrm E\{n_e^2(T)\}}=\frac{\bigl[\int h(\tau)s(T-\tau)\mathrm{d}\tau\bigr]^2}{N_0\int|h(\tau)|^2\mathrm{d}\tau}=\frac{E_s}{N_0}\cdot\underbrace{\frac{\bigl[\int h(\tau)s(T-\tau)\mathrm{d}\tau\bigr]^2}{\int|h|^2\mathrm{d}\tau\int|s(T-\tau)|^2\mathrm{d}\tau}}_{=|p|^2\le1}.$$

右边的分式是 $h(\tau)$ 与 $s(T-\tau)$ 之间的相关系数（[第 6 部分](/wissen/zh/elektrotechnik/3-semester/signale-und-systeme/korrelationsfunktionen/korrelationsfunktionen.html)）的平方。它至多为 1，并且恰好在二者形状相同时等于 1。

:::satz 定理 10.1 (匹配滤波器)
<span class="anker" id="satz-10-1"></span>

在白噪声背景下，可达到的最佳信噪比为

<span class="anker" id="gl-10-1"></span>
$$\Bigl(\frac{S_a}{N}\Bigr)_{\max}=\frac{E_s}{N_0},\qquad\text{条件为}\qquad h(t)=a\,s(T-t),\quad H(f)=a\,S^*(f)\,\mathrm{e}^{-\mathrm{j}2\pi fT}. \tag{10.1}$$
:::

⁠**如何理解：**最佳冲激响应就是信号本身经时间反转并平移 $T$ 后的结果，即__匹配滤波器__（相关滤波器）。它在无噪声时的输出为 $g(t)=a\,\varphi^E_{ss}(t-T)$，即信号的自相关函数平移后的结果，而采样恰好发生在其最大值处。令人惊讶的是，结果只取决于信号的*能量*，而与信号的形状无关。一个短而高的脉冲与一个能量相同的长而平的脉冲效果一样好。为使滤波器是因果的，$T$ 至少要等于信号的持续时间。与之等价的是__相关接收机__（相关器）：它把接收信号乘以 $s(t)$，再在信号的持续时间内积分。

:::aufgabe 练习 10 ★★ 噪声中的矩形脉冲
<span class="anker" id="aufg-10"></span>

接收到一个高度为 1 V、持续时间为 1 ms 的矩形脉冲，同时还有功率谱密度为 $N_0=10^{-6}$ V$^2$/Hz 的白噪声。

<ol class="al">

<li>

匹配滤波器是什么样的？它达到的 $S_a/N$ 是多少（以 dB 表示）？

</li>

<li>

无噪声时输出是什么样的？必须在什么时刻采样？

</li>

<li>

把脉冲缩短到 0.25 ms，高度不变。有什么变化？

</li>

</ol>

:::loesung
(a) $h(t)=a\,s(T-t)$：仍是一个 1 ms 的矩形，当 $T\ge1$ ms 时是因果的。$E_s=1\,\mathrm{V^2}\cdot1\,\mathrm{ms}=10^{-3}$ V$^2$s，因此 $S_a/N=10^{-3}/10^{-6}=1000$，即 30 dB。

(b) 矩形的自相关函数，即一个宽 2 ms 的三角形，平移了 $T$：它从 $t=T-1$ ms 开始上升，在 $t=T$ 处达到最大值。取 $T=1$ ms 时，恰好在脉冲结束的时刻采样；此时滤波器已经“看到”了整个脉冲。

(c) $E_s$ 降为四分之一，$S_a/N=250$，即 24 dB，差了 6 dB。起作用的只有能量。高度相同时，较短的脉冲意味着较少的能量。
:::
:::

## 第 11 阶段：二进制接收的误码率

<span class="anker" id="stufe-11"></span>

:::zweck
接收机必须作出判决：脉冲发送了没有？它出错的频率有多高？
:::

**思路。** 匹配滤波器输出端的采样值服从高斯分布，方差为 $N$（噪声）；若发送了脉冲，其均值为 $\sqrt{S_a}$，否则为 0。接收机把它与判决门限 $C$ 比较。当噪声把取值推过门限时，就发生错误。两种差错概率就是两条高斯曲线位于门限另一侧的面积：

<span class="anker" id="gl-11-1"></span>
$$P_{e1}=\mathrm{Prob}[y_1\le C]=\tfrac12\operatorname{erfc}\Bigl(\frac{\sqrt{S_a}-C}{\sqrt{2N}}\Bigr),\qquad P_{e0}=\mathrm{Prob}[y_0>C]=\tfrac12\operatorname{erfc}\Bigl(\frac{C}{\sqrt{2N}}\Bigr). \tag{11.1}$$

若两种情况发送得一样频繁，平均误码率（差错概率）为 $\frac12(P_{e1}+P_{e0})$。当门限恰好位于中间，即 $C=\sqrt{S_a}/2$ 时，它最小。采用匹配滤波器（$S_a/N=E_s/N_0$）时：

<span class="anker" id="gl-11-2"></span>
$$P_{e,\min}=\tfrac12\operatorname{erfc}\sqrt{\frac{E_s}{8N_0}}. \tag{11.2}$$

⁠**如何理解：**误码率只取决于 $E_s/N_0$，而且下降得极快：10 dB 时为 $5.7\cdot10^{-2}$，16 dB 时为 $8\cdot10^{-4}$，20 dB 时为 $2.9\cdot10^{-7}$（图 [4](#abb-4)）。只要信号能量多几个分贝，就能把一个无法使用的传输变成几乎无差错的传输。

:::abbildung et3/k7pe
采用匹配滤波器的通断键控接收的最小误码率。红点：10 dB、16 dB、20 dB。
:::

:::aufgabe 练习 11 ★★ 误码率
<span class="anker" id="aufg-11"></span>

<ol class="al">

<li>

计算 $E_s/N_0=10$ dB 时的 $P_{e,\min}$。提示：$\operatorname{erfc}(1.118)=0.114$。

</li>

<li>

为什么最佳门限位于 0 与 $\sqrt{S_a}$ 的正中间？若把门限向上移，$P_{e1}$ 和 $P_{e0}$ 会怎样变化？

</li>

</ol>

:::loesung
(a) $E_s/N_0=10$：$\sqrt{10/8}=1.118$，$P_{e,\min}=\frac12\cdot0.114=0.057$。

(b) 两条高斯曲线的宽度相同。两块差错面积之和在两条曲线的交点处最小，由对称性可知交点就在正中间。若把门限向上移，$P_{e0}$ 会变小，但 $P_{e1}$ 增大得更多，因为门限移进了上方那条曲线的密集部分。
:::
:::

## 第 12 阶段：离散时间随机信号

<span class="anker" id="stufe-12"></span>

:::zweck
上述一切同样适用于随机数序列，只是用求和代替积分。
:::

若以 $T\le\frac{1}{2f_\mathrm g}$ 对一个带限于 $f_\mathrm g$ 的过程采样，样本值就构成一个离散时间过程 $s(n)$。分布、数学期望和相关的定义都与前面相同，只是时间平均变为求和，例如 $\varphi_{ss}(m)=\lim_{M\to\infty}\frac{1}{2M+1}\sum_{n=-M}^{M}s(n)s(n+m)$。通过单位脉冲响应为 $h(n)$ 的 LSI 系统后：

<span class="anker" id="gl-12-1"></span>
$$m_g=m_s\sum_nh(n),\qquad\varphi_{gg}(m)=\varphi_{ss}(m)*\varphi^E_{hh}(m),\qquad\Phi_{gg,\mathrm a}(f)=\Phi_{ss,\mathrm a}(f)\,|H_\mathrm a(f)|^2, \tag{12.1}$$

其中周期功率谱密度为 $\Phi_{ss,\mathrm a}(f)=\sum_m\varphi_{ss}(m)\mathrm{e}^{-\mathrm{j}2\pi fm}$，且 $L_s=\int_{-1/2}^{1/2}\Phi_{ss,\mathrm a}\mathrm{d} f$。__离散时间白噪声__ 满足 $\Phi_{ss,\mathrm a}=N$ 和 $\varphi_{ss}(m)=N\delta(m)$：相继的数互不相关。与连续时间的情形不同，它的功率是有限的，$L_s=N$。

**例 1：对两个值取平均。** 均匀分布的白噪声（$\sigma_s^2=\frac1{12}$）通过 $h(n)=\frac12[\delta(n)+\delta(n-1)]$，即 $g(n)=\frac12[s(n)+s(n-1)]$。利用 $\varphi^E_{hh}=\frac14\delta(m+1)+\frac12\delta(m)+\frac14\delta(m-1)$：

$$\varphi_{gg}(m)=\tfrac{\sigma_s^2}{4}\delta(m+1)+\tfrac{\sigma_s^2}{2}\delta(m)+\tfrac{\sigma_s^2}{4}\delta(m-1).$$

方差减半为 $\frac{1}{24}$，而且相邻的输出值现在是相关的（它们共用一个输入值）。输出值服从三角分布，因为每个输出值都是两个独立的均匀分布数之和的一半。用 200,000 个数进行模拟，得到的方差为 0.0415，理论值为 $\frac1{24}=0.0417$。

**例 2：递归滤波器（AR(1) 过程，即一阶自回归过程）。** 方差为 $\sigma_s^2$ 的白噪声通过 $h(n)=b^n\varepsilon(n)$（[第 4 部分](/wissen/zh/elektrotechnik/3-semester/signale-und-systeme/abtastung-und-zeitdiskrete-systeme/abtastung-und-zeitdiskrete-systeme.html)）。利用 $\varphi^E_{hh}(m)=\sum_kb^kb^{k+|m|}=\frac{b^{|m|}}{1-b^2}$：

<span class="anker" id="gl-12-2"></span>
$$\varphi_{gg}(m)=\frac{\sigma_s^2}{1-b^2}\,b^{|m|},\qquad\Phi_{gg,\mathrm a}(f)=\frac{\sigma_s^2}{1-2b\cos(2\pi f)+b^2}. \tag{12.2}$$

当 $b=0.6$ 时，输出方差是输入方差的 $1.56$ 倍，相邻值的相关系数为 $0.6$。$b$ 越接近 1，低频分量就越强（图 [5](#abb-5)）。

:::abbildung et3/k7ar
AR(1) 过程的功率谱密度，以 1 为周期。$b=0.6$ 时其值从 6.25（$f=0$）变化到 0.39（$f=\frac12$），$b=0.9$ 时从 100 变化到 0.28。
:::

:::aufgabe 练习 12 ★★ AR(1) 过程
<span class="anker" id="aufg-12"></span>

均匀分布的白噪声（$\sigma_s^2=\frac1{12}$）通过 $g(n)=s(n)+0.6\,g(n-1)$。

<ol class="al">

<li>

计算输出方差和 $\varphi_{gg}(1)/\varphi_{gg}(0)$。

</li>

<li>

利用几何级数推导 $\varphi^E_{hh}(m)=\frac{b^{|m|}}{1-b^2}$。

</li>

<li>

输出还是均匀分布的吗？你大致预期是什么分布？为什么？

</li>

</ol>

:::loesung
(a) $\sigma_g^2=\frac{1/12}{1-0.36}=0.130$，$\varphi_{gg}(1)/\varphi_{gg}(0)=b=0.6$。模拟结果为 0.130 和 0.600。

(b) 当 $m\ge0$ 时：$\sum_{k\ge0}b^kb^{k+m}=b^m\sum_kb^{2k}=\frac{b^m}{1-b^2}$。单位脉冲响应的自相关函数是偶函数，因此一般地有 $b^{|m|}$。

(c) 不再是均匀分布：每个输出值都是许多独立输入值的加权和，$g(n)=\sum_kb^ks(n-k)$。根据中心极限定理，它近似服从高斯分布。当 $b=0.6$ 时，只有少数几项有明显贡献，因此这种近似比较粗略，但分布已经明显呈钟形。
:::
:::

:::kern 要点
<ul>

<li>

集平均 $\mathrm E\{\cdot\}$；平稳：与平移无关；各态历经：时间平均 $=$ 集平均。

</li>

<li>

$m_s$（直流分量），$L_s=\mathrm E\{s^2\}$（功率），$\sigma_s^2=L_s-m_s^2$（交流功率）。

</li>

<li>

自相关函数：$\varphi_{ss}(0)=L_s$，偶函数，最大值在 0 处；协方差 $\mu=\varphi-m^2$；和：$\sigma_s^2=\sigma_u^2+\sigma_v^2+2\mu_{uv}(0)$。

</li>

<li>

$P_s(x)=\mathrm{Prob}[s\le x]$，$p_s=P_s'$；$m_s=\int xp_s$，$L_s=\int x^2p_s$；均匀分布 $\sigma^2=a^2/12$。

</li>

<li>

特性曲线：$p_g(y)|\mathrm{d} y|=p_s(x)|\mathrm{d} x|$；量化误差（量化噪声）$\Delta^2/12$，每比特 6 dB。

</li>

<li>

独立 $\Rightarrow$ 不相关；独立变量之和：$p_s=p_f*p_g$；高斯分布：$\frac{1}{\sqrt{2\pi\sigma^2}}\mathrm{e}^{-(x-m)^2/2\sigma^2}$。

</li>

<li>

LTI：$m_g=m_sH(0)$，$\varphi_{gg}=\varphi_{ss}*\varphi^E_{hh}$，$\Phi_{gg}=\Phi_{ss}|H|^2$，$L=\int\Phi\,\mathrm{d} f$。

</li>

<li>

白噪声：$\Phi=N_0$，$\varphi=N_0\delta$；热噪声 $\mathrm E\{u^2\}=4kTRf_\mathrm g$，$kT\approx4$ pW/GHz。

</li>

<li>

匹配滤波器：$h=a\,s(T-t)$，$(S_a/N)_{\max}=E_s/N_0$；$P_{e,\min}=\frac12\operatorname{erfc}\sqrt{E_s/(8N_0)}$。

</li>

</ul>
:::
