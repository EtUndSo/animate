---
title: 第 5 阶段：规则与虚地
pfad: 电气工程 / 第 1 学期 / 电气工程基础 / 运算放大器
order: 1210700
summary: 第 4 阶段用 A 进行计算。但偏差极小。本阶段由此得出一条适用于所有负反馈电路的规则，并把它用于最重要的情况：输入接在负端。
tags: 反相放大器
lang: zh
---

<span class="anker" id="stufe-5"></span>

:::zweck
第 [4](gegenkopplung.html#stufe-4) 阶段用 $A$ 进行计算。但偏差极小。本阶段由此得出一条适用于所有负反馈电路的规则，并把它用于最重要的情况：输入接在负端。
:::

**基本思路。** 只要输出没有到达极限，任何电路中都有 $|U_\mathrm{D}|\le11\,\mathrm{V}/100000=110$ µ V。与伏特级的电压相比，这微不足道。所以按 $U_\mathrm{D}=0$ 计算，误差只有 $1/(A\beta)$ 的量级。这样就不再需要 $A$ 了。

:::satz 定理 5.1 (负反馈运放的规则)
<span class="anker" id="satz-5-1"></span>

只要 $U_\mathrm{A,min}<U_\mathrm{A}<U_\mathrm{A,max}$，就有

<ol>

<li>

$\varphi_+=\varphi_-$：输出自动调整，使差值消失。

</li>

<li>

$I_+=I_-=0$：没有电流流入输入端。

</li>

<li>

输出提供所需的任何电流。对输出节点不列节点方程。

</li>

</ol>

在负输入端列节点定律，解出 $U_\mathrm{A}$，最后检查极限。
:::

在__反相放大器__中，正输入端接地，$U_\mathrm{E}$ 经 $R_1$ 到达负输入端，$R_2$ 从输出引回（图 [7](#abb-7)）。由 $\varphi_-=\varphi_+=0$ 和 $I_-=0$ 得

<span class="anker" id="gl-5-1"></span>
$$\frac{U_\mathrm{E}}{R_1}+\frac{U_\mathrm{A}}{R_2}=0\quad\Rightarrow\quad U_\mathrm{A}=-\frac{R_2}{R_1}\,U_\mathrm{E},\qquad R_\mathrm{in}=\frac{U_\mathrm{E}}{I_1}=R_1. \tag{5.1}$$

⁠**如何理解：**$I_1$ 是流过 $R_1$ 的电流。$R_\mathrm{in}$ 是电源看到的电阻：只有 $R_1$，因为它的右端固定在 0 V。$A$ 有限时，$G=-(R_2/R_1)\big/\bigl(1+1/(A\beta)\bigr)$，$\beta=R_1/(R_1+R_2)$ 不变。**适用条件：**与规则相同，且 $A\beta\gg1$。

:::herleitung 反相放大器中有限的 $A$
对 $R_1$ 和 $R_2$ 组成的分压器应用叠加，得 $\varphi_-=(R_2\,U_\mathrm{E}+R_1\,U_\mathrm{A})/(R_1+R_2)$。由 $\varphi_+=0$ 得 $U_\mathrm{D}=-\varphi_-$，即 $U_\mathrm{A}=-A\,\varphi_-$。解得 $U_\mathrm{A}(1+A\beta)=-A\,(1-\beta)\,U_\mathrm{E}$，其中 $1-\beta=R_2/(R_1+R_2)$。由于 $A(1-\beta)=A\beta\cdot R_2/R_1$，即得该公式。环路把 $U_\mathrm{E}$ 看作固定值，所以 $\beta$ 与第 [4](gegenkopplung.html#stufe-4) 阶段的分压器相同。
:::

**虚地的机理。** 当 $U_\mathrm{E}=1$ V 时，$R_1$ 上的电压驱动 100 µ A 的电流流向负输入端。它进不了运放，所以只能流过 $R_2$。要让 100 µ A 流过 40 k$\Omega$，$R_2$ 的右端必须低 4 V，因此输出变为 $-4$ V。电流继续流入输出端，经下方的输出晶体管流向 $U_\mathrm{B-}$（图 [7](#abb-7) 中的红线）。节点上只留下极小的电压 $\varphi_-=-U_\mathrm{D}=U_\mathrm{A}/(-A)=+40$ µ V。这个节点表现得像接地点，但并不是：

<ul>

<li>

真正的接地点吸收电流。虚地把电流转交给 $R_2$，节点与接地点之间没有电流。

</li>

<li>

真正的接地点始终处于 0 V。虚地保持其电位，只是因为输出在不断调整。输出到达极限时，虚地就消失了（图 [7](#abb-7) 下部）。

</li>

<li>

如果用导线把节点接到接地点，100 µ A 就流向那里，$R_2$ 中没有电流，$U_\mathrm{A}=0$。

</li>

</ul>

**为什么仍然没有输入电流。** 两个输入端之间几乎没有电压，但也没有导体。它们电位相同，却并不相连：40 µ V 加在 $r_\mathrm{e}=1$ M$\Omega$ 上得到 40 pA，比 $I_1$ 小 250 万倍。两者共同起作用：差分级是高阻的，而环路几乎不给它留下电压。

:::frage 节点上是 0 V，又有电流到来，那负输入端的电阻不就是零吗？
对电源来说确实如此：在 $R_1$ 后面，它看到的是一个不管流来多少电流都保持电位的点。但做到这一点的是经 $R_2$ 起作用的输出。输入端本身仍是 1 M$\Omega$ 的高阻。
:::

:::abbildung et1/k11invert 7
上：反相放大器，红色为 $U_\mathrm{E}=+1$ V 时的电流路径。下：极限：$\hat u_\mathrm{E}=3.5$ V 本应得到 14 V，输出在 $\pm11$ V 处到达极限。这时 $\varphi_-$ 升到 0.6 V，虚地消失。
:::

**例。** $U_\mathrm{A}=-4\cdot1\,\mathrm{V}=-4$ V，$A$ 有限时更精确地为 $-3.9998$ V。$R_\mathrm{in}=10$ k$\Omega$。对接地点接 2 k$\Omega$ 负载时流过 2 mA，输出吸收 2.1 mA：负载加反馈。电源 $U_\mathrm{E}$ 对此毫无察觉。**极限情况：**$R_2=R_1$ 只改变符号。$R_2\to0$ 得 $U_\mathrm{A}=0$。

**第一个界限。** 规则 1 以输出能达到所要求的电压为前提。当 $G=-4$ 时，这在 $|U_\mathrm{E}|=11\,\mathrm{V}/4=2.75$ V 处结束。超过此值，$U_\mathrm{A}=\mp11$ V 固定，环路断开，由 $R_1$ 和 $R_2$ 组成的分压器决定节点电位：$\varphi_-=0.8\,U_\mathrm{E}+0.2\,U_\mathrm{A}$，在 3.5 V 时为 $+0.6$ V。

:::aufgabe 练习 5 ★★ 反相放大器
<span class="anker" id="aufg-5"></span>

$R_1=4.7$ k$\Omega$，$R_2=47$ k$\Omega$，$U_\mathrm{E}=0.5$ V。(a) 求 $U_\mathrm{A}$、$I_1$ 和 $R_\mathrm{in}$。(b) 当 $A=100000$ 时，$\varphi_-$ 和精确的 $G$ 是多少？(c) 输出端接 1 k$\Omega$ 负载。输出电流多大？它从哪里来？(d) $U_\mathrm{E}$ 到多大时输出还够用？$U_\mathrm{E}=2$ V 时 $\varphi_-$ 多大？

:::loesung
(a) $U_\mathrm{A}=-10\cdot0.5\,\mathrm{V}=-5$ V，$I_1=106.4$ µ A，$R_\mathrm{in}=4.7$ k$\Omega$。 (b) $\varphi_-=5\,\mathrm{V}/A=50$ µ V。由 $\beta=4.7/51.7=0.0909$ 得 $G=-10/(1+1.1\cdot10^{-4})=-9.9989$。 (c) 负载承载 5 mA，反馈承载 0.106 mA。流入输出端 5.11 mA，再流向 $U_\mathrm{B-}$。 (d) $|U_\mathrm{E}|\le1.1$ V。在 2 V 时 $U_\mathrm{A}=-11$ V，$\varphi_-=(47\cdot2-4.7\cdot11)\,\mathrm{V}/51.7=0.818$ V。
:::
:::
