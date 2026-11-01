---
title: 相关函数
pfad: 电气工程 / 第 3 学期 / 信号与系统 / 相关函数
order: 3260100
summary: 两个信号有多相似？ 能量又如何分布在各个频率上？
tags: 信号能量, 能量信号, 功率, 功率信号, 相关系数, 正交, 自相关函数, 互相关函数
lang: zh
---

## 本文内容

雷达发出一个脉冲，并在接收信号中寻找它的回波。手机在噪声中寻找一个已知的同步序列。二者提出的是同一个问题：**一个信号与另一个信号有多相似？在什么时移下最相似？**答案由相关函数给出。此外，相关函数的傅里叶变换还表明信号的能量如何分布在各个频率上。

:::merke 三句话的答案（读完本文后应觉得理所当然）
<ol>

<li>

两个信号的相似程度用它们乘积的积分来度量。相关函数对每个时移 $\tau$ 都这样做；它是与反转信号的卷积。

</li>

<li>

自相关函数的傅里叶变换是能量谱密度 $|S(f)|^2$。自相关函数在 $\tau=0$ 处的值就是能量（帕塞瓦尔定理）。

</li>

<li>

LTI 系统把能量谱密度乘以 $|H(f)|^2$，并把自相关函数与 $h$ 的自相关函数做卷积。

</li>

</ol>
:::

**所有结论背后的同一个原理。** 相关就是与反转信号的卷积。因此，卷积的所有工具都适用：

| 结论 | 来源 |
|---|---|
| 相关系数 | 两个归一化信号之差的能量（第 [2](#stufe-2) 阶段） |
| 相关积 | 与反转并共轭后的信号做卷积（第 [3](#stufe-3) 阶段） |
| 自相关函数为偶函数，最大值在 0 处 | 反转；并且信号与自身最相似（第 [3](#stufe-3) 阶段） |
| 能量谱密度、帕塞瓦尔定理 | 反转与共轭变为 $S^*$，卷积变为乘积（第 [4](#stufe-4) 阶段） |
| 维纳–李关系 | 卷积的结合律（第 [5](#stufe-5) 阶段） |
| 离散时间、周期、DFT | 同样的计算，只是改用求和（第 [7](#stufe-7) 阶段） |

**如何使用本文。**每个阶段包括基本思路、可展开解答的典型问题以及练习（★ 到 ★★★）。请先自己尝试，解答可在每道练习下方展开。

:::merke 本文的参考模型
矩形脉冲 $\operatorname{rect}(t)$、三角脉冲 $\Lambda(t)$、指数脉冲 $\varepsilon(t)\mathrm{e}^{-t}$（$RC=1$ s 的 RC 电路的冲激响应）以及序列 $(1,2,1)$。脚本 `rechnung_kap6.py` 可复算这些数值。
:::

## 第 1 阶段：能量与功率

<span class="anker" id="stufe-1"></span>

:::zweck
在比较信号之前，需要一个度量信号“大小”的量。在系统理论中，这个量就是能量；对于无限长的信号，则是功率。
:::

在电阻 $R$ 上，从 $t_1$ 到 $t_2$ 这段时间内有能量 $\frac1R\int u^2\mathrm{d} t$ 转化为热。去掉因子 $1/R$，这个表达式就称为__信号能量__：

<span class="anker" id="gl-1-1"></span>
$$E_s=\int_{-\infty}^{\infty}|s(t)|^2\,\mathrm{d} t. \tag{1.1}$$

若它有限，则称 $s$ 为__能量信号__（例如任何脉冲）。若信号无限长地持续下去而不衰减（余弦、阶跃），它的能量就是无穷大。这时改为度量平均__功率__：

<span class="anker" id="gl-1-2"></span>
$$L_s=\lim_{T\to\infty}\frac{1}{2T}\int_{-T}^{T}|s(t)|^2\,\mathrm{d} t. \tag{1.2}$$

若它有限，则称 $s$ 为__功率信号__。对于周期信号，在一个周期上取平均就足够了。对于狄拉克冲激，能量和功率都没有定义（$\delta^2$ 不存在）。

:::aufgabe 练习 1 ★ 能量还是功率？
<span class="anker" id="aufg-1"></span>

求下列信号的能量或功率：(a) $a\operatorname{rect}(t/T)$，(b) $\varepsilon(t)\mathrm{e}^{-t}$，(c) $A\cos(2\pi Ft)$，(d) $\varepsilon(t)$。

:::loesung
(a) $E=a^2|T|$。(b) $E=\int_0^\infty\mathrm{e}^{-2t}\mathrm{d} t=\frac12$。(c) 能量无穷大，功率为 $\frac{A^2}{2}$（$\cos^2$ 的平均值为 $\frac12$）。(d) 能量无穷大，功率为 $\lim\frac{1}{2T}\int_0^T1\,\mathrm{d} t=\frac12$：信号在一半的时间里为 1。
:::
:::

## 第 2 阶段：度量相似程度——相关系数

<span class="anker" id="stufe-2"></span>

:::zweck
怎样用一个数来度量两个信号有多相似？办法是度量它们的差有多大。
:::

**思路。** 两个信号相似时，差信号 $\Delta(t)=s(t)-g(t)$ 的能量就小。展开得：

$$E_\Delta=\int|s-g|^2\mathrm{d} t=E_s+E_g-\int s^*g\,\mathrm{d} t-\int g^*s\,\mathrm{d} t=E_s+E_g-2\operatorname{Re}\int s^*(t)g(t)\,\mathrm{d} t.$$

因此，差别完全体现在乘积的积分中。为了不让信号本身的大小计入在内，把两个信号都归一化到能量 1。于是 $E_\Delta=2-2\operatorname{Re}\,p_{sg}$，其中__相关系数__为

<span class="anker" id="gl-2-1"></span>
$$p_{sg}=\frac{\int_{-\infty}^{\infty}s^*(t)\,g(t)\,\mathrm{d} t}{\sqrt{E_sE_g}}. \tag{2.1}$$

⁠**如何理解：**$|p_{sg}|\le1$（柯西–施瓦茨不等式）。$p=1$ 表示 $s=a\,g$ 且 $a>0$：形状相同。$p=-1$ 表示 $s=-a\,g$：形状相同，符号相反。$p=0$ 表示 $\int s^*g\,\mathrm{d} t=0$；这两个信号是__正交__的，就像[第 3 部分](/wissen/zh/elektrotechnik/3-semester/signale-und-systeme/fourier-reihe-und-transformation/fourier-reihe-und-transformation.html)中傅里叶级数的各次谐波一样。例：对于 $\operatorname{rect}(t)$ 和 $\Lambda(t)$，有 $\int\operatorname{rect}\cdot\Lambda\,\mathrm{d} t=0.75$，$E_{\operatorname{rect}}=1$，$E_\Lambda=\frac23$，因此 $p=0.919$。

:::aufgabe 练习 2 ★★ 相关系数
<span class="anker" id="aufg-2"></span>

计算下列各对信号的 $p$：(a) $\operatorname{rect}(t)$ 与 $\operatorname{rect}(t-0.5)$，(b) $\operatorname{rect}(t)$ 与 $\Lambda(t)$（结果见上文），(c) $\operatorname{rect}(t)$ 与 $\operatorname{sgn}(t)\operatorname{rect}(t)$。

:::loesung
(a) 两个矩形在长度 0.5 上重叠，因此 $\int=0.5$，且两者的能量都是 1：$p=0.5$。 (b) $\int\operatorname{rect}\cdot\Lambda\,\mathrm{d} t=\int_{-1/2}^{1/2}(1-|t|)\mathrm{d} t=0.75$，$E_\Lambda=2\int_0^1(1-t)^2\mathrm{d} t=\frac23$：$p=\frac{0.75}{\sqrt{2/3}}=0.919$。形状非常相似。 (c) $\int\operatorname{sgn}(t)\operatorname{rect}^2(t)\mathrm{d} t=0$：$p=0$；这两个信号正交，尽管它们在右半部分完全相同。
:::
:::

## 第 3 阶段：相关函数与相关积

<span class="anker" id="stufe-3"></span>

:::zweck
回波与发送脉冲相似，但发生了时移。因此要对每个时移 $\tau$ 进行比较。
:::

:::definition 定义 3.1 (能量信号的相关函数)
<span class="anker" id="satz-3-1"></span>

<span class="anker" id="gl-3-1"></span>
$$\varphi^E_{sg}(\tau)=\int_{-\infty}^{\infty}s^*(t)\,g(t+\tau)\,\mathrm{d} t=s^*(-\tau)*g(\tau). \tag{3.1}$$

当 $g=s$ 时，它称为__自相关函数__（ACF）$\varphi^E_{ss}(\tau)$，否则称为__互相关函数__（CCF）。除以 $\sqrt{E_sE_g}$ 后，称为归一化相关函数。
:::

⁠**如何理解：**把 $g$ 向左平移 $\tau$，再求乘积的积分。第二个等号是问题的核心：相关就是与反转并共轭后的信号做卷积。因此，相关也称为__相关积__。与卷积不同，这里没有任何反转；两个信号沿同一方向走。

:::herleitung 把相关写成卷积
在式 [(3.1)](#gl-3-1) 中令 $t=-\vartheta$：$\int s^*(-\vartheta)\,g(\tau-\vartheta)\,\mathrm{d}\vartheta$。这就是 $s^*(-\tau)$ 与 $g(\tau)$ 的卷积积分。
:::

:::satz 定理 3.2 (相关函数的性质)
<span class="anker" id="satz-3-2"></span>

<span class="anker" id="gl-3-2"></span>
<span class="anker" id="gl-3-3"></span>
$$\begin{aligned} &\varphi^E_{gs}(\tau)=\varphi^{E*}_{sg}(-\tau),\qquad\varphi^E_{ss}(\tau)=\varphi^{E*}_{ss}(-\tau)\ \ (\text{对实信号}\ s\ \text{为偶函数}),\\ &|\varphi^E_{ss}(\tau)|\le\varphi^E_{ss}(0)=E_s. \end{aligned} \tag{3.2|3.3}$$

时限信号的自相关函数的持续时间是信号本身的两倍。
:::

⁠**如何理解：**信号在不平移时与自身最相似，此时自相关函数的值就是信号的能量。矩形的自相关函数是三角形：$\varphi^E_{ss}=\operatorname{rect}(-\tau)*\operatorname{rect}(\tau)=\Lambda(\tau)$，其宽度是矩形的两倍（图 [1](#abb-1) 左）。

**例：寻找回波。** 发送信号为 $s=\operatorname{rect}(t)$；接收信号是经过衰减和延迟的回波 $g=0.5\operatorname{rect}(t-3)$。互相关函数为 $\varphi^E_{sg}(\tau)=0.5\,\Lambda(\tau-3)$：它的最大值位于 $\tau=3$，即延迟处；最大值的高度 $0.5=0.5\cdot E_s$ 表明了衰减（图 [1](#abb-1) 右）。雷达就是这样测量距离的。

:::abbildung et3/k6korr
左：矩形的自相关函数是三角形，最大值 $=E_s=1$，位于 $\tau=0$ 处，宽度加倍。右：发送脉冲与回波 $0.5\operatorname{rect}(t-3)$ 之间的互相关函数在延迟 $\tau=3$ 处取最大值。
:::

:::frage 卷积和相关看起来几乎一样。区别在哪里？
在卷积 $\int s(\tau)h(t-\tau)\mathrm{d}\tau$ 中，第二个信号是倒着走的（$-\tau$）：系统“记得”过去。在相关 $\int s^*(t)g(t+\tau)\mathrm{d} t$ 中，两个信号都正着走：把一个形状恰好叠放在另一个形状上，度量二者吻合得有多好。在数学上，区别恰恰就是反转；正因为如此，相关就是与反转信号的卷积。
:::

:::ltspice 用滑动积分器寻找回波
一个在每一时刻都对过去一秒积分的滤波器，构成 $y(t)=\int_{t-1}^{t}g(u)\,\mathrm{d} u$。取 $s=\operatorname{rect}(t)$ 时，这恰好就是式 [(3.1)](#gl-3-1) 中的互相关函数，只是延迟了 0.5 s：$y(t)=\varphi^E_{sg}(t-0.5)$。滤波器在信号到来的同时对所有 $\tau$ 计算它。

⁠**绘制：**电压源 `voltage` 接在节点 `g` 上，取 `PULSE(0 0.5 2.5 1u 1u 1)`，即回波 $0.5\operatorname{rect}(t-3)$。两个行为源 `bv`：一个接在节点 `int` 上，取 `V=idt(V(g))`（变上限积分）；另一个接在节点 `y` 上，取 `V=V(int)-delay(V(int),1)`（对过去一秒的积分）。

⁠**指令：**`.tran 0 6 0 1m`，`.meas tran ymax MAX V(y)`。

⁠**你会看到：**`V(y)` 是三角形 $0.5\,\Lambda(t-3.5)$，其最大值 0.5 位于 $t=3.5$ s：即 3 s 的延迟再加上 0.5 s，因为滤波器要到回波结束时才完成积分。高度 0.5 就是回波的衰减。

⁠**对于练习 [3](#aufg-3)：**输入取 `PULSE(0 1 0 1u 1u 1 2 2)`，即双矩形，每个矩形都比正文中晚 0.5 s。对 `y` 使用

`V=V(int)-delay(V(int),1)+delay(V(int),2)-delay(V(int),3)`。

这个滤波器在两个与双矩形相匹配的窗口上积分，`V(y)` 就是双矩形平移了 3 s 的自相关函数。与你在练习 [3](#aufg-3)(a) 中的结果比较。
:::

:::aufgabe 练习 3 ★★ 回波与重复
<span class="anker" id="aufg-3"></span>

<ol class="al">

<li>

一个信号由两个矩形组成：$s(t)=\operatorname{rect}(t)+\operatorname{rect}(t-2)$。求它的自相关函数。从中怎样看出重复？

</li>

<li>

对该信号验证式 [(3.3)](#gl-3-3)。

</li>

</ol>

:::loesung
(a) 利用 $\operatorname{rect}(-\tau)=\operatorname{rect}(\tau)$ 和 $\operatorname{rect}*\operatorname{rect}=\Lambda$，四个部分乘积给出

$$\varphi^E_{ss}(\tau)=2\Lambda(\tau)+\Lambda(\tau-2)+\Lambda(\tau+2).$$

$\tau=\pm2$ 处的旁峰显示了重复的间隔。在那里，每次都只有两个矩形中的一个落在另一个上。在 $\tau=0$ 处，两个矩形都叠在一起，因此高度加倍。

(b) $\varphi^E_{ss}(0)=2=E_s=1+1$，而旁峰的值只有 1。
:::
:::

## 第 4 阶段：能量谱密度

<span class="anker" id="stufe-4"></span>

:::zweck
相关函数的傅里叶变换是什么？它表明能量如何分布在各个频率上。
:::

:::satz 定理 4.1 (能量信号的维纳–辛钦定理)
<span class="anker" id="satz-4-1"></span>

<span class="anker" id="gl-4-1"></span>
$$\varphi^E_{ss}(\tau)=s^*(-\tau)*s(\tau)\;\circ\!\!-\!\!\bullet\;S^*(f)\,S(f)=|S(f)|^2,\qquad\varphi^E_{sg}(\tau)\;\circ\!\!-\!\!\bullet\;S^*(f)\,G(f). \tag{4.1}$$
:::

⁠**如何理解：**$|S(f)|^2$ 称为__能量谱密度__。它是实的，永不为负，并且对实信号而言是 $f$ 的偶函数。信号的相位丢失了：幅度谱相同的所有信号都有相同的自相关函数。$S^*G$ 称为__互能量谱密度__。推导只需要卷积定理、时间反转和共轭：$s^*(-\tau)\circ\!\!-\!\!\bullet\,S^*(f)$（[第 3 部分](/wissen/zh/elektrotechnik/3-semester/signale-und-systeme/fourier-reihe-und-transformation/fourier-reihe-und-transformation.html)）。

**帕塞瓦尔定理。** 在 $\tau=0$ 处，自相关函数就是能量。利用面积定理：

<span class="anker" id="gl-4-2"></span>
$$E_s=\varphi^E_{ss}(0)=\int_{-\infty}^{\infty}|s(t)|^2\,\mathrm{d} t=\int_{-\infty}^{\infty}|S(f)|^2\,\mathrm{d} f. \tag{4.2}$$

两个正交信号的频谱也是正交的：$\int s^*g\,\mathrm{d} t=\int S^*G\,\mathrm{d} f=0$。

**例：指数脉冲。** $s(t)=\varepsilon(t)\mathrm{e}^{-t}$ 的频谱为 $S(f)=\frac{1}{1+\mathrm{j}2\pi f}$，因此 $|S|^2=\frac{1}{1+(2\pi f)^2}$。它同时也是 $\operatorname{Re}\{S\}$，而 $\operatorname{Re}\{S\}$ 的逆变换是信号的偶部（[第 3 部分](/wissen/zh/elektrotechnik/3-semester/signale-und-systeme/fourier-reihe-und-transformation/fourier-reihe-und-transformation.html)）：

$$\varphi^E_{ss}(\tau)=\tfrac12\mathrm{e}^{-|\tau|},\qquad E_s=\varphi^E_{ss}(0)=\tfrac12.$$

在时域中由 $\int_0^\infty\mathrm{e}^{-2t}\mathrm{d} t=\frac12$，在频域中由 $\int\frac{\mathrm{d} f}{1+(2\pi f)^2}=\frac12$，都得到同样的值。图 [2](#abb-2) 给出了信号、它的自相关函数以及两个频谱。

:::abbildung et3/k6exp
指数脉冲（$RC=1$ s）。左：信号及其自相关函数 $\frac12\mathrm{e}^{-|\tau|}$（偶函数，最大值 $=E_s=\frac12$）。右：幅度谱和能量谱密度，后者衰减得更快：能量集中在低频。
:::

:::aufgabe 练习 4 ★ 验证帕塞瓦尔定理
<span class="anker" id="aufg-4"></span>

在时域中计算 $\operatorname{rect}(t)$ 的能量，再利用式 [(4.2)](#gl-4-2) 由其频谱计算。由此可以得出 si 函数的哪个著名积分？

:::loesung
时域：$E=\int\operatorname{rect}^2\mathrm{d} t=1$。频域：$\int\operatorname{si}^2(\pi f)\mathrm{d} f$。因此 $\int_{-\infty}^\infty\operatorname{si}^2(\pi f)\mathrm{d} f=1$。
:::
:::

## 第 5 阶段：相关与 LTI 系统

<span class="anker" id="stufe-5"></span>

:::zweck
LTI 系统对自相关函数和能量谱密度有什么作用？怎样用互相关来测量一个系统？
:::

:::satz 定理 5.1 (维纳–李关系)
<span class="anker" id="satz-5-1"></span>

对于 $g=s*h$：

<span class="anker" id="gl-5-1"></span>
$$\varphi^E_{gg}(\tau)=\varphi^E_{ss}(\tau)*\varphi^E_{hh}(\tau)\;\circ\!\!-\!\!\bullet\;|G(f)|^2=|S(f)|^2\,|H(f)|^2, \tag{5.1}$$

<span class="anker" id="gl-5-2"></span>
$$\varphi^E_{sg}(\tau)=\varphi^E_{ss}(\tau)*h(\tau)\;\circ\!\!-\!\!\bullet\;|S(f)|^2\,H(f). \tag{5.2}$$
:::

:::herleitung 维纳–李关系
$\varphi^E_{gg}=g^*(-\tau)*g(\tau)=[s^*(-\tau)*h^*(-\tau)]*[s(\tau)*h(\tau)]$。利用交换律和结合律重新排列：$[s^*(-\tau)*s(\tau)]*[h^*(-\tau)*h(\tau)]=\varphi^E_{ss}*\varphi^E_{hh}$。同理，$\varphi^E_{sg}=s^*(-\tau)*s(\tau)*h(\tau)$。
:::

⁠**如何理解：**系统把每个频率上的能量乘以 $|H|^2$。系统的相位对能量没有影响。式 [(5.2)](#gl-5-2) 是一种测量方法：若输入的自相关函数几乎是一个加权狄拉克冲激 $c\,\delta(\tau)$（非常短的脉冲或宽带噪声，[第 7 部分](/wissen/zh/elektrotechnik/3-semester/signale-und-systeme/zufallssignale/zufallssignale.html)），则输入与输出之间的互相关函数几乎就是 $c\,h(\tau)$，即除因子 $c$ 外就是冲激响应。与 $|H|^2$ 不同，它还包含相位。

:::ltspice RC 电路前后的能量
⁠**绘制：**行为源 `bv` 接在节点 `s` 上，取 `V=exp(-time)*(time>0)`，即指数脉冲 $\varepsilon(t)\mathrm{e}^{-t}$。因子 `(time>0)` 使 LTspice 以 0 V 计算 $t=0$ 时的初始状态，因此电容从未充电的状态开始。其后接 RC 电路（`res` 取 `1Meg`，`cap` 取 `1u`），输出接节点 `g`。

⁠**指令：**`.tran 0 30 0 1m`，以及用来求式 [(1.1)](#gl-1-1) 中能量的 `.meas tran Es INTEG V(s)*V(s)` 和 `.meas tran Eg INTEG V(g)*V(g)`。

⁠**你会看到：**`Es` $=0.500$，与第 [4](#stufe-4) 阶段中的 $E_s=\varphi^E_{ss}(0)=\frac12$ 一致。把 `Eg` 与你在练习 [5](#aufg-5) 中的结果比较。输出能量较小，因为 RC 电路把每个频率上的能量乘以 $|H|^2\le1$。
:::

:::aufgabe 练习 5 ★★ 输出端的能量
<span class="anker" id="aufg-5"></span>

指数脉冲 $\varepsilon(t)\mathrm{e}^{-t}$ 通过一个 $RC=1$ s 的 RC 电路。

<ol class="al">

<li>

求 $|G(f)|^2$，并由此求输出能量。提示：$\int_{-\infty}^\infty\frac{\mathrm{d} x}{(1+x^2)^2}=\frac\pi2$。

</li>

<li>

用 $g(t)=t\,\mathrm{e}^{-t}\varepsilon(t)$ 在时域中验证（[第 1 部分](/wissen/zh/elektrotechnik/3-semester/signale-und-systeme/lti-systeme-und-faltung/lti-systeme-und-faltung.html)，两个级联的 RC 电路）。

</li>

</ol>

:::loesung
(a) $|G|^2=|S|^2|H|^2=\frac{1}{(1+(2\pi f)^2)^2}$。令 $x=2\pi f$：$E_g=\frac{1}{2\pi}\int\frac{\mathrm{d} x}{(1+x^2)^2}=\frac{1}{2\pi}\cdot\frac\pi2=\frac14$。

(b) $\int_0^\infty t^2\mathrm{e}^{-2t}\mathrm{d} t=\frac{2}{2^3}=\frac14$。两种方法的结果一致。能量从 $\frac12$ 降到 $\frac14$，因为第二个 RC 电路进一步衰减了较高的频率。
:::
:::

## 第 6 阶段：带通信号的相关

<span class="anker" id="stufe-6"></span>

:::zweck
带通信号的相关函数同样用复包络来计算（[第 5 部分](/wissen/zh/elektrotechnik/3-semester/signale-und-systeme/tiefpass-und-bandpasssysteme/tiefpass-und-bandpasssysteme.html)）。
:::

两个实带通信号的互相关函数仍然是带通信号：

$$\varphi^E_{sg}(\tau)=\operatorname{Re}\bigl\{\varphi^E_{sgT}(\tau)\,\mathrm{e}^{\mathrm{j}2\pi f_0\tau}\bigr\}.$$

反转后的信号具有包络 $s_T^*(-t)$，因为

$$s(-t)=\operatorname{Re}\bigl\{s_T(-t)\mathrm{e}^{-\mathrm{j}2\pi f_0t}\bigr\}=\operatorname{Re}\bigl\{s_T^*(-t)\mathrm{e}^{\mathrm{j}2\pi f_0t}\bigr\}.$$

利用[第 5 部分](/wissen/zh/elektrotechnik/3-semester/signale-und-systeme/tiefpass-und-bandpasssysteme/tiefpass-und-bandpasssysteme.html)中的传输关系 $g_T=\frac12s_T*h_T$：

<span class="anker" id="gl-6-1"></span>
$$\varphi^E_{sgT}(\tau)=\tfrac12\bigl[s_T^*(-\tau)*g_T(\tau)\bigr]=\tfrac12\int_{-\infty}^{\infty}s_T^*(t)\,g_T(t+\tau)\,\mathrm{d} t,\qquad E_s=\varphi^E_{ss}(0)=\varphi^E_{ssT}(0). \tag{6.1}$$

⁠**如何理解：**两个带通信号的相关，等于它们包络的相关的一半，再调制到载波上。带通信号的能量是其复包络能量的一半：幅度为 $|s_T|$ 的余弦，平均起来只有一半的功率。

## 第 7 阶段：离散时间相关与周期相关

<span class="anker" id="stufe-7"></span>

:::zweck
对于样本值，积分变为求和。借助 DFT 可以快速计算相关。
:::

:::satz 定理 7.1 (离散时间相关)
<span class="anker" id="satz-7-1"></span>

<span class="anker" id="gl-7-1"></span>
$$\varphi^E_{sg}(m)=\sum_{n=-\infty}^{\infty}s^*(n)\,g(n+m)=s^*(-m)*g(m),\qquad E_s=\sum_n|s(n)|^2=\int_{-1/2}^{1/2}|S_\mathrm a(f)|^2\,\mathrm{d} f, \tag{7.1}$$

<span class="anker" id="gl-7-2"></span>
$$\varphi^E_{ss}(m)\;\circ\!\!-\!\!\bullet\;|S_\mathrm a(f)|^2\ (\text{周期为}\ 1),\qquad\varphi^E_{gg}(m)=\varphi^E_{ss}(m)*\varphi^E_{hh}(m). \tag{7.2}$$
:::

对于采样后的低通信号，有 $\varphi^E_{sg}(mT)=T\sum_ns^*(nT)g((n+m)T)$ 和 $E_s=T\sum_n|s(nT)|^2$。离散时间能量信号是平方可和的序列。

**例。** $s=(1,2,1)$：当 $m=-2,\dots,2$ 时，$\varphi^E_{ss}=(1,4,6,4,1)$。最大值 $6=E_s$ 位于 $m=0$，偶对称，有五个值而不是三个。在 $f=0$ 处用维纳–辛钦定理验证：$|S_\mathrm a(0)|^2=(1+2+1)^2=16=\sum_m\varphi^E_{ss}(m)$。

**周期相关。** 与卷积的情形一样（[第 4 部分](/wissen/zh/elektrotechnik/3-semester/signale-und-systeme/abtastung-und-zeitdiskrete-systeme/abtastung-und-zeitdiskrete-systeme.html)），对于周期为 $M$ 的序列有：

<span class="anker" id="gl-7-3"></span>
$$\varphi^E_{sgd}(m)=\sum_{n=0}^{M-1}s_d^*(n)\,g_d(n+m)\;\circ\!\!-\!\!\bullet\;S_d^*(k)\,G_d(k). \tag{7.3}$$

用 FFT 来计算时，这称为__快速相关__。为了使周期相关重现普通的相关，$M$ 必须足够大。对于 $(1,2,1)$，取 $M=3$ 得到相互重叠的序列 $(6,5,5)$，而取 $M=5$ 得到 $(6,4,1,1,4)$，即循环排列的普通自相关函数。

**功率信号。** 对于能量无穷大的信号，要取平均：

<span class="anker" id="gl-7-4"></span>
$$\varphi^L_{sg}(\tau)=\lim_{T\to\infty}\frac1T\int_{-T/2}^{T/2}s^*(t)\,g(t+\tau)\,\mathrm{d} t. \tag{7.4}$$

若两个信号都是周期相同的周期信号，取一个周期就足够了，而且相关函数也是周期的。例：$A\cos(2\pi Ft+\varphi_0)$ 的自相关函数为 $\frac{A^2}{2}\cos(2\pi F\tau)$。相位 $\varphi_0$ 消失了，而在 $\tau=0$ 处，自相关函数等于功率 $\frac{A^2}{2}$。

:::aufgabe 练习 6 ★ 离散自相关函数
<span class="anker" id="aufg-6"></span>

<ol class="al">

<li>

手算验证 $(1,2,1)$ 的自相关函数。

</li>

<li>

求 $(1,-1)$ 的自相关函数。$\varphi(\pm1)<0$ 说明该信号有什么特点？

</li>

</ol>

:::loesung
(a) $\varphi(0)=1+4+1=6$，$\varphi(\pm1)=1\cdot2+2\cdot1=4$，$\varphi(\pm2)=1\cdot1=1$。

(b) $\varphi(0)=2$，$\varphi(\pm1)=-1$。时移为 1 时取负值，意味着相邻的值往往符号相反：信号变化很快。与此相符，$|S_\mathrm a(f)|^2=|1-\mathrm{e}^{-\mathrm{j}2\pi f}|^2=2-2\cos(2\pi f)$ 在 $f=0$ 处为零，在 $f=\frac12$ 处最大：这是一个高通信号。
:::
:::

:::aufgabe 练习 7 ★★ 余弦的自相关函数
<span class="anker" id="aufg-7"></span>

利用式 [(7.4)](#gl-7-4)，在一个周期上推导 $A\cos(2\pi Ft+\varphi_0)$ 的自相关函数。为什么 $\varphi_0$ 会消失？这对用自相关函数测量相位意味着什么？

:::loesung
令 $\omega=2\pi F$，并利用 $\cos a\cos b=\frac12[\cos(a-b)+\cos(a+b)]$：

$$\frac1T\int_0^TA^2\cos(\omega t+\varphi_0)\cos(\omega t+\omega\tau+\varphi_0)\mathrm{d} t=\frac{A^2}{2}\cos(\omega\tau)+\frac{A^2}{2T}\int_0^T\cos(2\omega t+\omega\tau+2\varphi_0)\mathrm{d} t.$$

第二个积分跨越两个完整的周期，因此为零。相位 $\varphi_0$ 只是平移了时间原点，而对所有时间取平均并不知道原点在哪里。因此，单个信号的自相关函数无法测量相位。相反，*两个*信号的相位差则由互相关函数显示出来。
:::
:::

:::kern 要点
<ul>

<li>

$E_s=\int|s|^2\mathrm{d} t$；$L_s=\lim\frac{1}{2T}\int_{-T}^T|s|^2\mathrm{d} t$。

</li>

<li>

$p_{sg}=\frac{\int s^*g\,\mathrm{d} t}{\sqrt{E_sE_g}}$，$|p|\le1$，$p=0$：正交。

</li>

<li>

$\varphi^E_{sg}(\tau)=\int s^*(t)g(t+\tau)\mathrm{d} t=s^*(-\tau)*g(\tau)$；$\varphi^E_{gs}(\tau)=\varphi^{E*}_{sg}(-\tau)$。

</li>

<li>

自相关函数：偶函数（对实信号），最大值 $\varphi^E_{ss}(0)=E_s$，持续时间加倍。

</li>

<li>

$\varphi^E_{ss}\leftrightarrow|S|^2$，$\varphi^E_{sg}\leftrightarrow S^*G$；帕塞瓦尔定理 $\int|s|^2\mathrm{d} t=\int|S|^2\mathrm{d} f$。

</li>

<li>

维纳–李关系：$\varphi^E_{gg}=\varphi^E_{ss}*\varphi^E_{hh}$，$|G|^2=|S|^2|H|^2$；$\varphi^E_{sg}=\varphi^E_{ss}*h$。

</li>

<li>

带通：$\varphi^E_{sgT}=\frac12s_T^*(-\tau)*g_T(\tau)$。

</li>

<li>

离散：$\varphi(m)=\sum s^*(n)g(n+m)$，$\leftrightarrow|S_\mathrm a|^2$；周期：$S_d^*G_d$。

</li>

</ul>
:::
