---
title: 第 3 阶段：相关函数与相关积
pfad: 电气工程 / 第 3 学期 / 信号与系统 / 相关函数
order: 3260400
summary: 回波与发送脉冲相似，但发生了时移。因此要对每个时移 tau 进行比较。
tags: 自相关函数, 互相关函数, 相关积
lang: zh
---

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

:::abbildung et3/k6korr 1
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
