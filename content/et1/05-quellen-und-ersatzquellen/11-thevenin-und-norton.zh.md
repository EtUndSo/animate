---
title: 第 9 阶段：戴维南与诺顿
pfad: 电气工程 / 第 1 学期 / 电气工程基础 / 电源与等效电源
order: 1151100
summary: N 要给许多不同的负载供电。到目前为止，每换一个负载就得把整个网络重算一遍。本阶段用一条直线一劳永逸地代替这个网络。
tags: 等效电压源, 等效电流源, 负载特性曲线
lang: zh
---

<span class="anker" id="stufe-9"></span>

:::zweck
N 要给许多不同的负载供电。到目前为止，每换一个负载就得把整个网络重算一遍。本阶段用一条直线一劳永逸地代替这个网络。
:::

**基本思路。** 设想把负载换成一个电流源，它恰好从网络中取走电流 $I_\mathrm{A}$。网络察觉不到任何差别，因为它在接线端上感受到的只有这个电流。现在网络只含电阻和电源，可以使用叠加。因此 $U_\mathrm{AB}$ 由两部分组成：内部电源的贡献，它与电流无关；以及 $I_\mathrm{A}$ 的贡献，它与电流成正比。常数减去系数乘电流，就是一条直线。线性网络从外部看像一条直线，全部原因就在于此。

:::satz 定理 9.1 (等效电源：戴维南与诺顿)
<span class="anker" id="satz-9-1"></span>

每个线性一端口网络在其接线端上的行为都像一个__等效电压源__，也同样像一个__等效电流源__：

<span class="anker" id="gl-9-1"></span>
$$U_\mathrm{AB}=U_\mathrm{i}-R_\mathrm{i}\,I_\mathrm{A},\qquad\qquad I_\mathrm{A}=I_\mathrm{i}-G_\mathrm{i}\,U_\mathrm{AB}, \tag{9.1}$$

其中

<span class="anker" id="gl-9-2"></span>
$$U_\mathrm{i}=U_\mathrm{OC},\qquad I_\mathrm{i}=I_\mathrm{SC},\qquad R_\mathrm{i}=\frac{1}{G_\mathrm{i}}=\frac{U_\mathrm{OC}}{I_\mathrm{SC}}. \tag{9.2}$$
:::

⁠**如何理解：**第一种形式以戴维南命名，第二种以诺顿命名。$U_\mathrm{OC}$ 是接线端断开时的电压，$I_\mathrm{SC}$ 是流过短接的接线端的电流。$R_\mathrm{i}$ 在两种形式中相同。这条直线也称为__负载特性曲线__。$R_\mathrm{i}$ 小时通常选戴维南形式，$R_\mathrm{i}$ 大时选诺顿形式（第 [6](spannungsquelle-oder-stromquelle.html#stufe-6) 阶段）。**适用条件：**一端口网络必须是线性的，负载不必。这一结论只对接线端成立，对内部的功率没有任何说明（第 [6](spannungsquelle-oder-stromquelle.html#stufe-6) 阶段）。

:::herleitung 由叠加得到直线
在接线端接上设想的电流源 $I_\mathrm{A}$，由式 [(8.1)](uberlagerung.html#gl-8-1) 得

$$U_\mathrm{AB}=\underbrace{\sum_k a_kU_{\mathrm{q}k}+\sum_k Z_kI_{\mathrm{q}k}}_{\text{内部电源}}\;\underbrace{-\,R_\mathrm{i}I_\mathrm{A}}_{\text{接线端电流}}.$$

当 $I_\mathrm{A}=0$ 时，留下第一部分，所以它就是 $U_\mathrm{OC}$。当所有内部电源都关闭时，留下第二部分：这时 $R_\mathrm{i}$ 是关闭后的网络在 A、B 之间的总电阻。负号来自参考箭头：$I_\mathrm{A}$ 从 A 流出，在内部即从 B 流向 A，这时 A 的电位较低。由 $U_\mathrm{AB}=0$ 得 $I_\mathrm{A}=I_\mathrm{SC}=U_\mathrm{OC}/R_\mathrm{i}$。整理即得第二种形式。
:::

**求这两个数的三种途径。**

<ol>

<li>

⁠**开路和短路：**计算或测量 $U_\mathrm{OC}$ 和 $I_\mathrm{SC}$，由式 [(9.2)](#gl-9-2) 得 $R_\mathrm{i}$。

</li>

<li>

⁠**关闭电源：**电压源换成导线，电流源换成断口，然后求 A、B 之间的总电阻。这就是 $R_\mathrm{i}$。此外还需要 $U_\mathrm{OC}$ 或 $I_\mathrm{SC}$ 中的一个量。

</li>

<li>

⁠**两种负载情况：**如果不允许短路，就用两个负载测量点 $(I_\mathrm{x},U_\mathrm{x})$ 和 $(I_\mathrm{y},U_\mathrm{y})$。两点都在直线上，$U_\mathrm{x}=U_\mathrm{i}-R_\mathrm{i}I_\mathrm{x}$，$U_\mathrm{y}=U_\mathrm{i}-R_\mathrm{i}I_\mathrm{y}$。相减并代入得

<span class="anker" id="gl-9-3"></span>
$$R_\mathrm{i}=-\frac{U_\mathrm{x}-U_\mathrm{y}}{I_\mathrm{x}-I_\mathrm{y}},\qquad U_\mathrm{i}=U_\mathrm{x}+R_\mathrm{i}I_\mathrm{x}=\frac{U_\mathrm{x}I_\mathrm{y}-U_\mathrm{y}I_\mathrm{x}}{I_\mathrm{y}-I_\mathrm{x}}. \tag{9.3}$$

</li>

</ol>

:::abbildung et1/k5ersatz 10
左：网络 N，右：它的两个等效电源。在接线端上，三者无法区分。
:::

::::beispiel
对 N，$U_\mathrm{OC}=9$ V 已由第 [8](uberlagerung.html#stufe-8) 阶段得知。短路时，$R_2$ 处于两个相连的接线端之间，不通过电流。电压源驱动 $U_\mathrm{q1}/R_1=3$ A 流过接线端，电流源驱动 1.5 A：$I_\mathrm{SC}=U_\mathrm{q1}/R_1+I_\mathrm{q2}=4.5$ A。由此得 $R_\mathrm{i}=9\,\mathrm{V}/4.5\,\mathrm{A}=2\,\Omega$。第二种途径证实了这一点：关闭电源后 $R_1$ 和 $R_2$ 并联，$6\,\Omega\parallel3\,\Omega=2\,\Omega$。诺顿形式为 $I_\mathrm{i}=4.5$ A，$G_\mathrm{i}=0.5$ S（图 [10](#abb-10)）。

这正是第 [5](reale-quellen-und-der-arbeitspunkt.html#stufe-5) 阶段中电池的数值。不用再看网络，对 16 $\Omega$ 就得到 $I_\mathrm{A}=9\,\mathrm{V}/18\,\Omega=0.5$ A 和 $U_\mathrm{AB}=8$ V。**检验**（在原电路中）：经 $R_1$ 流来 $(18-8)\,\mathrm{V}/6\,\Omega=1.667$ A，加上 1.5 A，共 3.167 A。其中 $R_2$ 取走最大的部分 $8\,\mathrm{V}/3\,\Omega=2.667$ A，0.5 A 流向负载。如果 $I_\mathrm{q2}=0$，就剩下分电路 1 的分压器，$U_\mathrm{i}=\frac{R_2}{R_1+R_2}U_\mathrm{q1}=6$ V，$I_\mathrm{i}=U_\mathrm{q1}/R_1=3$ A，$R_\mathrm{i}=R_1\parallel R_2$ 不变。

:::abbildung et1/k5geraden 11
N 在一个电源和两个电源作用下的特性曲线。每个电源都使直线向上平移，斜率 $R_\mathrm{i}=2\,\Omega$ 不变，因为它只取决于电阻。6 V 与 3 V 之和以及 3 A 与 1.5 A 之和就是叠加。
:::
::::

::::beispiel [第二个例子] 实际电流源
理想电流源 $I_\mathrm{q}=3$ A 并联 $R_\mathrm{q}=20\,\Omega$，经 $R_\mathrm{v}=10\,\Omega$ 向接线端 A 供电。它的另一极是 B，A、B 之间接 $R_\mathrm{p}=30\,\Omega$。短路时 $R_\mathrm{p}$ 被旁路，分流得 $I_\mathrm{SC}=I_\mathrm{q}\frac{R_\mathrm{q}}{R_\mathrm{q}+R_\mathrm{v}}=2$ A。开路时 $R_\mathrm{v}$ 和 $R_\mathrm{p}$ 串联。它们的电流为 $I_\mathrm{q}\frac{R_\mathrm{q}}{R_\mathrm{q}+R_\mathrm{v}+R_\mathrm{p}}=1$ A，所以 $U_\mathrm{OC}=R_\mathrm{p}\cdot1\,\mathrm{A}=30$ V。两者之商为 $R_\mathrm{i}=15\,\Omega$。关闭时电流源变成断口，其并联电阻保留：$R_\mathrm{i}=R_\mathrm{p}\parallel(R_\mathrm{q}+R_\mathrm{v})=15\,\Omega$，或用电导表示为 $G_\mathrm{i}=G_\mathrm{p}+\frac{1}{R_\mathrm{q}+R_\mathrm{v}}$。
::::

⁠**极限情况：**如果理想电压源直接接在接线端上，$R_\mathrm{i}=0$，诺顿形式不存在。如果理想电流源与某个接线端串联，$R_\mathrm{i}=\infty$，戴维南形式不存在。如果各电源恰好相互抵消，则 $U_\mathrm{OC}=0$，$I_\mathrm{SC}=0$。这时比值失效，但途径 2 仍能给出 $R_\mathrm{i}$。

:::ltspice 网络与等效电源并排比较
⁠**绘制：**N 用 `voltage` 18、`res` 6 和 `res` 3，电流源值为 1.5，从接地点到 `a`。旁边单独画等效电源，用 `voltage` 9 和 `res` 2，一直到网络节点 `b`。在 `a` 和 `b` 上各接一个值为 `{IZ}` 的电流源 `current` 到接地点。

⁠**指令：**`.param IZ=0`，`.step param IZ list 0 0.5 2.25 4.5`，`.op`

⁠**你会看到：**`V(a)` 和 `V(b)` 完全重合：9 V，8 V，4.5 V，0 V。用同样的方法搭建练习 [11](#aufg-11) 的网络：`IZ=0` 时那里显示你算出的 $U_\mathrm{OC}$，在你算出的 $I_\mathrm{SC}$ 处 `V(a)` 降到零。
:::

:::frage N 现在真的和电池一样了吗？
在接线端上是的。任何负载在两者上都显示相同的电流和相同的电压。在内部则不然：开路时 N 中 $R_2$ 上消耗 27 W，$R_1$ 上消耗 13.5 W，而电池处于静止状态。等效电源只回答接线端上的问题，别的问题一概不答。
:::

:::aufgabe 练习 10 ★★ 两种负载情况
<span class="anker" id="aufg-10"></span>

在一个未知的线性设备上，接线端接 10 $\Omega$ 时测得 10 V 和 1 A，接 4 $\Omega$ 时测得 8 V 和 2 A。(a) 用式 [(9.3)](#gl-9-3) 求 $R_\mathrm{i}$、$U_\mathrm{i}$ 和 $I_\mathrm{SC}$。(b) 预测接 1 $\Omega$ 时的电流和电压。

:::loesung
(a) $R_\mathrm{i}=-\frac{10-8}{1-2}\,\Omega=2\,\Omega$，$U_\mathrm{i}=10\,\mathrm{V}+2\,\Omega\cdot1\,\mathrm{A}=12$ V。用分式验算：$\frac{10\cdot2-8\cdot1}{2-1}\,\mathrm{V}=12$ V。$I_\mathrm{SC}=6$ A。

(b) $I_\mathrm{A}=12\,\mathrm{V}/3\,\Omega=4$ A，$U_\mathrm{AB}=4$ V。
:::
:::

:::aufgabe 练习 11 ★★★ 两个实际电源
<span class="anker" id="aufg-11"></span>

B 与节点 C 之间接 2 $\Omega$，并与之并联一个 5 A 的理想电流源，方向从 B 到 C。从 C 经 3 $\Omega$ 到节点 D。从 D 经一个 4 V 的理想电压源到接线端 A，其正极接 D。A 与 B 之间接 5 $\Omega$。(a) 用叠加法计算 $U_\mathrm{OC}$。(b) 通过关闭电源计算 $R_\mathrm{i}$，并由此求 $I_\mathrm{SC}$。(c) 极限情况：电压源为 10 V。开路和短路显示什么，现在 $R_\mathrm{i}$ 是多少？

:::loesung
(a) 只有电流源（电压源换成导线，接线端断开）：5 A 向 2 $\Omega$ 与 $3\,\Omega+5\,\Omega$ 的并联供电，即 $2\,\Omega\parallel8\,\Omega=1.6\,\Omega$，C 相对于 B 为 8 V。由 3 $\Omega$ 和 5 $\Omega$ 分压得 $U'=8\,\mathrm{V}\cdot\frac58=5$ V。

只有电压源（电流源断开）：它驱动 $4\,\mathrm{V}/10\,\Omega=0.4$ A 从正极经 3 $\Omega$ 和 2 $\Omega$ 到 B，再经 5 $\Omega$ 从 B 到 A。所以 A 比 B 低 2 V：$U''=-2$ V。合起来：$U_\mathrm{OC}=3$ V。一般地，若 $R_\mathrm{q1}$ 为 3 $\Omega$，$R_\mathrm{q2}$ 为 2 $\Omega$，$R_3$ 为 5 $\Omega$，则 $U_\mathrm{OC}=\frac{I_\mathrm{q2}R_\mathrm{q2}-U_\mathrm{q1}}{R_\mathrm{q1}+R_\mathrm{q2}+R_3}\,R_3$。

(b) 关闭电源后，3 $\Omega$ 和 2 $\Omega$ 串联，再与 5 $\Omega$ 并联：$R_\mathrm{i}=5\,\Omega\parallel5\,\Omega=2.5\,\Omega$。于是 $I_\mathrm{SC}=3\,\mathrm{V}/2.5\,\Omega=1.2$ A。直接计算：带 2 $\Omega$ 的电流源相当于 10 V 串 2 $\Omega$（第 [6](spannungsquelle-oder-stromquelle.html#stufe-6) 阶段）。5 $\Omega$ 被短路，所以 $I_\mathrm{SC}=(10\,\mathrm{V}-4\,\mathrm{V})/5\,\Omega=1.2$ A。

(c) 电压为 10 V 时，两部分相互抵消：$U_\mathrm{OC}=0$，$I_\mathrm{SC}=0$。比值不确定，但 $R_\mathrm{i}$ 仍为 2.5 $\Omega$，因为它与电源无关。从外部看，这个网络是一个纯电阻。
:::
:::
