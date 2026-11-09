---
title: 第 1 阶段：合并电阻
pfad: 电气工程 / 第 1 学期 / 电气工程基础 / 电源与等效电源
order: 1150300
summary: 不含电源的电阻网络在两个接线端上的特性曲线过原点，所以一个数就够了。本阶段通过逐步合并求出这个数。
tags: 混联电路, 总电阻, 电导
lang: zh
---

<span class="anker" id="stufe-1"></span>

:::zweck
不含电源的电阻网络在两个接线端上的特性曲线过原点，所以一个数就够了。本阶段通过逐步合并求出这个数。
:::

**基本思路。** __混联电路__由互相嵌套的串联组和并联组构成。如果两个电阻的公共节点上没有接别的东西，它们就是串联的。这时流过两者的是同一个电流，电荷无处分流。如果两个电阻接在同样的两个节点上，它们就是并联的。这时两者上的电压相同。每一个这样的组本身都是一个小的一端口网络，其特性曲线是一个电阻。用这个电阻代替它，电路的其余部分毫无察觉。这样由内向外反复进行。

:::abbildung et1/k5gruppe 1
左：由六个电阻组成的负载网络。叠放的三个电阻并联，合为 10 $\Omega$，再与 $R_\mathrm{c}$ 串联，合为 15 $\Omega$。右：经过这两步之后的网络。
:::

:::definition 定义 1.1 (总电阻)
<span class="anker" id="satz-1-1"></span>

__总电阻__ $R_\mathrm{AB}$ 是不含电源的一端口网络的比值 $U_\mathrm{AB}/I_\mathrm{A}$。对图 [1](#abb-1) 的网络有

<span class="anker" id="gl-1-1"></span>
$$R_\mathrm{AB}=R_\mathrm{a}+R_\mathrm{b}\parallel\bigl(R_\mathrm{c}+R_\mathrm{d}\parallel R_\mathrm{e}\parallel R_\mathrm{f}\bigr) =R_\mathrm{a}+\left[G_\mathrm{b}+\frac{1}{R_\mathrm{c}+\dfrac{1}{G_\mathrm{d}+G_\mathrm{e}+G_\mathrm{f}}}\right]^{-1}. \tag{1.1}$$
:::

⁠**如何理解：**$R$ 是电阻，单位 $\Omega$；$G=1/R$ 是它的__电导__，单位西门子（S）。串联时电阻相加，并联时电导相加。因此在第二种形式中，每个并联组都写成电导之和。带指数 $-1$ 的方括号再把结果取倒数。**适用条件：**这种方法需要真正的组。如果中间节点上还接着第三条支路，两个相邻的电阻就不再是串联的（第 [2](symmetrie-nutzen.html#stufe-2) 和第 [3](stern-und-dreieck.html#stufe-3) 阶段）。

::::beispiel
代入图 [1](#abb-1) 中的数值：$G_\mathrm{d}+G_\mathrm{e}+G_\mathrm{f}=50+33.3+16.7$ mS $=100$ mS，即 10 $\Omega$。再串联 $R_\mathrm{c}$：15 $\Omega$。与 $R_\mathrm{b}$ 并联：$30\,\Omega\parallel15\,\Omega=10\,\Omega$。再串联 $R_\mathrm{a}$：$R_\mathrm{AB}=16\,\Omega$。反向计算得到各电流：A、B 之间加 8 V 时流过 0.5 A。$R_\mathrm{a}$ 上压降为 3 V，其余部分还剩 5 V。流过 $R_\mathrm{b}$ 的电流为 $5\,\mathrm{V}/30\,\Omega=166.7$ mA，流过 $R_\mathrm{c}$ 的电流为 $5\,\mathrm{V}/15\,\Omega=333.3$ mA。两者之和为 500 mA。
::::

⁠**极限情况：**当 $R_\mathrm{b}\to0$ 时，式 [(1.1)](#gl-1-1) 变为 $R_\mathrm{AB}=R_\mathrm{a}=6\,\Omega$。短路把后面的一切都旁路了，电荷走导线。

:::frage 这些步骤可以按任意顺序进行吗？
不可以。一个组往往要等内部的组合并之后才出现：在原图中 $R_\mathrm{c}$ 和 $R_\mathrm{b}$ 并不并联，因为它们之间还接着叠放的三个电阻。所以要从离接线端最远的组开始，向接线端推进。
:::

:::aufgabe 练习 1 ★ 改变负载网络
<span class="anker" id="aufg-1"></span>

以图 [1](#abb-1) 的网络为出发点。在下列情况下 $R_\mathrm{AB}$ 是多少：(a) $R_\mathrm{b}$ 因断线而失效，(b) $R_\mathrm{c}$ 被短路，(c) $R_\mathrm{d}$ 被短路，(d) $R_\mathrm{f}$ 失效？计算之前先预测：四种变化中哪一种影响最小？

:::loesung
预测：影响最小的是 (d)，因为 $R_\mathrm{f}$ 是其并联组中最大的电阻，电流最小。

(a) $R_\mathrm{AB}=6\,\Omega+15\,\Omega=21\,\Omega$。 (b) $R_\mathrm{AB}=6\,\Omega+30\,\Omega\parallel10\,\Omega=13.5\,\Omega$。 (c) 整个并联组被旁路：$R_\mathrm{AB}=6\,\Omega+30\,\Omega\parallel5\,\Omega=10.29\,\Omega$。 (d) $20\,\Omega\parallel30\,\Omega=12\,\Omega$，所以 $R_\mathrm{AB}=6\,\Omega+30\,\Omega\parallel17\,\Omega=16.85\,\Omega$。
:::
:::
