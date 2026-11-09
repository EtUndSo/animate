---
title: 第 7 阶段：节点定律就是电荷守恒
pfad: 电气工程 / 第 1 学期 / 电气工程基础 / 电流、电阻与基尔霍夫定律
order: 1120800
summary: 第一类方程：电荷守恒对节点有什么要求？
tags: 
lang: zh
---

<span class="anker" id="stufe-7"></span>

:::zweck
第一类方程：电荷守恒对节点有什么要求？
:::

**基本思路。** 节点就是一段导线。如果流入多于流出，电荷就聚集在上面，其电位上升。这使流入一侧电阻上的电压下降，流出一侧电阻上的电压上升。流入减小，流出增大，直到两者相等。这种自我调节在纳秒内完成。它正是这条定律背后的机理：节点恰好稳定在没有电荷滞留的电位上。

:::satz 定理 7.1 (节点定律，基尔霍夫第一定律)
<span class="anker" id="satz-7-1"></span>

流入一个节点的所有电流之和在任何时刻都为零。等价地，流入电流之和等于流出电流之和：

<span class="anker" id="gl-7-1"></span>
$$\sum_{\nu=1}^{N}I_\nu=0\quad\text{（所有箭头指向节点）},\qquad\sum I_\mathrm{in}=\sum I_\mathrm{out}. \tag{7.1}$$

对于有 $k$ 个节点的网络，这些方程中有 $k-1$ 个是独立的。
:::

⁠**如何理解：**箭头可以自由选择。如果全部指向节点，那么至少有一个电流为负，或者全部为零。箭头方向混合时，流入的计为正，流出的计为负。**适用条件：**节点不得储存可观的电荷。只要电流相对于均衡时间变化缓慢，这一点就成立。推导中给出了具体数字。

:::abbildung et1/k2knoten 8
左：有两个流入电流和三个流出电流的节点，两者之和都是 7 mA。右：该定律也适用于包围网络一部分的闭合面，这里包围 $K_2$、$K_3$ 和 $R_\mathrm e$。$R_\mathrm e$ 中的电流留在面内，不计入。
:::

:::herleitung 由电荷守恒得节点定律
节点上的电荷 $Q_\mathrm K$ 满足 $\mathrm{d} Q_\mathrm K/\mathrm{d} t=\sum I_\nu$，因为电荷既不产生也不消失。用[第 1 部分](/wissen/zh/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/ladung-feld-und-potenzial/ladung-feld-und-potenzial.html)做一个估算，可以看出 $Q_\mathrm K$ 有多小：半径为 1 cm 的金属球的电位为 $\varphi=k_\mathrm C\,Q/r$，其中库仑常量 $k_\mathrm C=8.99\cdot10^{9}\,\mathrm{N\,m^2/C^2}$。要达到 9 V，$Q=10$ pC 就够了。3 mA 的过剩电流在 3.3 ns 内就能提供这些电荷。因此 $\mathrm{d} Q_\mathrm K/\mathrm{d} t$ 相对于电流可以忽略，于是剩下 $\sum I_\nu=0$。
:::

**为什么有一个方程是多余的。** 每条支路连接两个节点。因此其电流恰好出现在两个节点方程中，一次带 $+$（流入），一次带 $-$（流出）。把 $k$ 个方程全部相加，所有电流都抵消了。所以一个方程可由其余方程得出，而任选 $k-1$ 个方程都是独立的。

::::beispiel
网络中所有电流箭头都指向实际电流的方向：从 $K_1$ 经电阻向下，$I_\mathrm e$ 从 $K_2$ 到 $K_3$，$I_0$ 经电源从 $K_4$ 到 $K_1$。节点方程为

$$\begin{aligned} K_1:&\quad +I_0-I_\mathrm a-I_\mathrm c=0, & K_2:&\quad +I_\mathrm a-I_\mathrm b-I_\mathrm e=0,\\ K_3:&\quad +I_\mathrm c-I_\mathrm d+I_\mathrm e=0, & K_4:&\quad -I_0+I_\mathrm b+I_\mathrm d=0. \end{aligned}$$

前三个方程之和为 $I_0-I_\mathrm b-I_\mathrm d=0$，即符号相反的第四个方程。如果只把 $K_2$ 和 $K_3$ 相加，$I_\mathrm e$ 就消去了，剩下的是图 [8](#abb-8) 中的闭合面：$I_\mathrm a+I_\mathrm c=I_\mathrm b+I_\mathrm d$。**检验：**在只有两条支路的点上得 $I_1=I_2$。串联的元件中流过相同的电流。
::::

:::frage 节点上接电容器时，这条定律也成立吗？
成立。流向极板的电流和其他支路电流一样，电荷不是聚集在节点上，而是聚集在极板上。[第 3 部分](/wissen/zh/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/der-kondensator/der-kondensator.html)将讨论这一点。
:::

:::aufgabe 练习 7 ★★ 应用节点定律
<span class="anker" id="aufg-7"></span>

<ol class="al">

<li>

四个电流箭头指向节点：$I_1=5$ mA，$I_2=-2$ mA，$I_3=-1$ mA。$I_4$ 等于多少？它实际向哪个方向流动？

</li>

<li>

由网络的节点方程证明 $I_0=I_\mathrm b+I_\mathrm d$。与此对应的是哪个闭合面？

</li>

<li>

预测：只有 1 µ A 的过剩电流在推导中的金属球上停留 1 s。球的电位会是多少？为什么这不会发生？

</li>

</ol>

:::loesung
(a) $5-2-1+I_4=0$，所以 $I_4=-2$ mA：有 2 mA 从节点流出。

(b) 把 $K_1$、$K_2$、$K_3$ 相加得 $I_0-I_\mathrm b-I_\mathrm d=0$。这对应包围 $K_1$、$K_2$、$K_3$ 的闭合面，或者等价地，对应 $K_4$ 的方程。代入数字：$4=1+3$。

(c) $Q=1\,\mu\text{C}$ 得 $\varphi=k_\mathrm C\,Q/r=0.9$ MV。远在达到这个值之前，上升的电位就把过剩电荷赶走了。这就是自我调节。
:::
:::
