---
title: 第 10 阶段：并联、分流器与负载
pfad: 电气工程 / 第 1 学期 / ET1 – 电气工程基础 1：电路分析导论 / 电流、电阻与基尔霍夫定律
adresse: elektrotechnik/1-semester/grundlagen-der-elektrotechnik/strom-widerstand-und-kirchhoff
knoten: 第 2 章：电流、电阻与基尔霍夫定律
order: 1121100
summary: 第二种基本模式：并排的电阻。这样就能回答从分压器取用电流时会发生什么。
tags: 并联, 分流器, 负载电阻
lang: zh
---

<span class="anker" id="stufe-10"></span>

:::zweck
第二种基本模式：并排的电阻。这样就能回答从分压器取用电流时会发生什么。
:::

**基本思路。** 所有电阻都接在相同的两个节点上，因而加有相同的电压。每增加一个电阻就多开一条路径，节点定律把各电流相加。因此各电导相加，就像并排导线的横截面积相加一样。

:::satz 定理 10.1 (并联与分流器)
<span class="anker" id="satz-10-1"></span>

对 $N$ 个__并联__的电阻，有

<span class="anker" id="gl-10-1"></span>
<span class="anker" id="gl-10-2"></span>
$$\begin{aligned} U&=U_1=\dots=U_N,\qquad I=I_1+\dots+I_N,\qquad I_i=G_i\,U=\frac{U}{R_i},\\ G_\mathrm{tot}&=\frac{1}{R_\mathrm{tot}}=\sum_{i=1}^{N}G_i=\sum_{i=1}^{N}\frac{1}{R_i},\qquad R_\mathrm{tot}=\Bigl(\sum_{i=1}^N\frac1{R_i}\Bigr)^{-1}. \end{aligned} \tag{10.1|10.2}$$

对两个电阻记作 $R_1\parallel R_2$：

<span class="anker" id="gl-10-3"></span>
$$R_1\parallel R_2=\frac{R_1\,R_2}{R_1+R_2},\qquad I_1=I_\mathrm{tot}\,\frac{G_1}{G_1+G_2}=I_\mathrm{tot}\,\frac{R_2}{R_1+R_2},\quad I_2=I_\mathrm{tot}\,\frac{G_2}{G_1+G_2}. \tag{10.3}$$
:::

⁠**如何理解：**各电流按电导之比分配，这就是__分流器__。在 $I_1$ 的表达式中，分子是 $R_2$：电流偏向较小的电阻。**适用条件：**两个电阻都接在相同的两个节点之间，引线是理想的。

:::herleitung 总电导与分流器
节点定律给出 $I=\sum I_i$，由于 $U$ 相同，$I=(G_1+\dots+G_N)\,U$。对两条支路，$U=I_\mathrm{tot}/(G_1+G_2)$，于是 $I_1=G_1\,U$。代入 $G=1/R$，得

$$I_1=I_\mathrm{tot}\,\frac{1/R_1}{1/R_1+1/R_2}=I_\mathrm{tot}\,\frac{R_2}{R_1+R_2}.$$
:::

::::beispiel
串联链的 $R_1$ 和 $R_2$ 并联接在 9 V 上：$G_\mathrm{tot}=0.5+1=1.5$ mS，所以 $R_\mathrm{tot}=667\,\Omega$，小于较小的那个值，$I=13.5$ mA。分流器给出 $I_1=13.5\,\mathrm{mA}\cdot1/3=4.5$ mA，$I_2=9$ mA。混合网络由内向外合并：$6\,\mathrm{k\Omega}$ 与 $1\,\mathrm{k\Omega}+2\,\mathrm{k\Omega}$ 并联得 $6\parallel3=2\,\mathrm{k\Omega}$。
::::

⁠**极限情况：**$R_2\to\infty$ 时得 $R_1$，开路支路不起作用。$R_2\to0$ 时得 0，短路承担全部电流。$R_1=R_2$ 时得 $R_1/2$。

**带负载的分压器。** 分压器的电压要为下一级电路供电，__负载电阻__ $R_\mathrm L$ 与 $R_2$ 并联（图 [11](#abb-11)）。机理是：中间节点多开了一条路径，总电阻下降，流过 $R_1$ 的电流上升，$R_1$ 上的压降增大，中间电位下降。把 $R_2'=R_2\parallel R_\mathrm L$ 代入式 [(9.3)](reihenschaltung-und-spannungsteiler.html#gl-9-3)：

<span class="anker" id="gl-10-4"></span>
$$\frac{U_2}{U}=\frac{R_2\parallel R_\mathrm L}{R_1+R_2\parallel R_\mathrm L}=\frac{R_2\,R_\mathrm L}{R_1\,(R_2+R_\mathrm L)+R_2\,R_\mathrm L},\quad I_\mathrm L=\frac{U_2}{R_\mathrm L}=\frac{U\,R_2}{R_1\,(R_2+R_\mathrm L)+R_2\,R_\mathrm L}. \tag{10.4}$$

⁠**极限情况：**$R_\mathrm L\to\infty$ 时 $I_\mathrm L\to0$，得到空载规则。$R_\mathrm L=R_2$ 时 $U_2/U=R_2/(2R_1+R_2)=\frac12R_2/(R_1+\frac12R_2)$。

:::abbildung et1/k2belastung 11
左：带负载的分压器。右：按式 [(10.4)](#gl-10-4)，$R_1=2\,\mathrm{k\Omega}$、$R_2=1\,\mathrm{k\Omega}$、$U=9$ V 时 $U_2$ 随 $R_\mathrm L$ 的变化。$R_\mathrm L=1\,\mathrm{k\Omega}$ 时剩下 1.8 V，$10\,\mathrm{k\Omega}$ 时为 2.81 V。只有远大于 $R_1\parallel R_2=667\,\Omega$ 时，负载的影响才察觉不到。
:::

::::beispiel
对串联链，相对于空载 3 V 的相对误差 $\delta=(U_{2,0}-U_2)/U_{2,0}$ 为：$R_\mathrm L=1\,\mathrm{k\Omega}$ 时 40 %，$10\,\mathrm{k\Omega}$ 时 6.3 %，$100\,\mathrm{k\Omega}$ 时 0.66 %。误差为 $\delta=R_\mathrm i/(R_\mathrm i+R_\mathrm L)$，其中 $R_\mathrm i=R_1\parallel R_2$（练习 [11](#aufg-11)）。所以分压器的作用相当于一个内阻为 $R_\mathrm i$ 的电源（[第 5 章](/wissen/zh/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/quellen-und-ersatzquellen/quellen-und-ersatzquellen.html)）。
::::

:::ltspice 测量负载影响
⁠**绘制：**电压源 `voltage` 取 `9`，从 `in` 接地，`res` `R1 2k` 从 `in` 接到 `mid`，`R2 1k` 从 `mid` 接地，`RL` 的值取 `{RL}`，从 `mid` 接地。

⁠**指令：**`.step param RL list 1k 2k 6k 10k 100k`，`.tran 1m`，`.meas tran u2 FIND V(mid) AT=1m`。

⁠**你会看到：**SPICE Error Log 给出每一步的 $U_2$：1.80 V；2.25 V；2.70 V；2.81 V；2.98 V。把 $6\,\mathrm{k\Omega}$ 时的值与练习 [11](#aufg-11)(b) 比较。
:::

**应用：R-2R 梯形网络。** 分流器支撑着第二种 D/A 转换器（图 [12](#abb-12)）。诀窍是自相似性：最后一个节点上是 $2R\parallel2R=R$。加上前面的 $R$，又得到 $2R$。于是每个节点向右和向下看到的都是 $2R$，其电流按 1:1 分配，电压逐节点减半（由 $R$ 和 $2R\parallel2R$ 构成的分压器）。电源提供 $I_\mathrm{ref}=U_\mathrm{ref}/R$，于是得到按二进制加权的电流 $I_\mathrm{ref}/2$、$I_\mathrm{ref}/4$、$I_\mathrm{ref}/8$，依此类推。外部电路（[第 11 章](/wissen/zh/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/der-operationsverstarker/der-operationsverstaerker.html)）把汇流线保持在接地点的电位上。因此，所有下方的 $2R$ 看到的电位都相同，无论它们接到汇流线还是接地，切换时电流都不变。靠近电源的比特是最高有效位（MSB，most significant bit），末端的是最低有效位（LSB）。$I_\mathrm{out}$ 是接通的各电流之和。

:::abbildung et1/k2r2r 12
$R=1\,\mathrm{k\Omega}$、$U_\mathrm{ref}=8$ V 的 R-2R 梯形网络。红色为节点电压，蓝色为支路电流。开关处于数字 1010 的位置：流向汇流线的电流为 $4\,\mathrm{mA}+1\,\mathrm{mA}=5$ mA。
:::

:::frage 再加一个电阻，电阻怎么会变小？
这里的“更多电阻”指的是更多路径。原有支路仍流过相同的电流，新支路再流过额外的电流。电压相同时总电流变大，所以 $U/I$ 变小。
:::

:::aufgabe 练习 10 ★★ 并联与混联
<span class="anker" id="aufg-10"></span>

<ol class="al">

<li>

计算 $2$、$3$ 和 $6\,\mathrm{k\Omega}$ 并联时的 $R_\mathrm{tot}$，以及接 12 V 时的所有电流。

</li>

<li>

10 mA 分配到 $1\,\mathrm{k\Omega}$ 和 $9\,\mathrm{k\Omega}$ 上。两个电流各是多少？

</li>

<li>

$1\,\mathrm{k\Omega}$ 与 $4\,\mathrm{k\Omega}\parallel(1\,\mathrm{k\Omega}+3\,\mathrm{k\Omega})$ 串联，接在 9 V 上。求 $R_\mathrm{tot}$ 和所有电流。

</li>

</ol>

:::loesung
(a) $G_\mathrm{tot}=0.5+0.333+0.167=1$ mS，所以 $R_\mathrm{tot}=1\,\mathrm{k\Omega}$。电流为 6、4 和 2 mA，总和 12 mA。 (b) $I_1=10\,\mathrm{mA}\cdot9/10=9$ mA，$I_2=1$ mA。小电阻流过的电流是另一个的九倍。 (c) $1+3=4\,\mathrm{k\Omega}$，$4\parallel4=2\,\mathrm{k\Omega}$，$R_\mathrm{tot}=3\,\mathrm{k\Omega}$。总电流 3 mA，两条相同的支路中各 1.5 mA。
:::
:::

:::aufgabe 练习 11 ★★★ 掌握负载影响
<span class="anker" id="aufg-11"></span>

分压器为 $R_1=2\,\mathrm{k\Omega}$、$R_2=1\,\mathrm{k\Omega}$，接在 9 V 上。

<ol class="al">

<li>

由式 [(10.4)](#gl-10-4) 证明 $\delta=R_\mathrm i/(R_\mathrm i+R_\mathrm L)$，其中 $R_\mathrm i=R_1\parallel R_2$。

</li>

<li>

什么样的 $R_\mathrm L$ 使 $\delta=10\,\%$？这时 $U_2$ 是多少？

</li>

<li>

由 $200\,\Omega$ 和 $100\,\Omega$ 组成的分压器具有相同的比值。计算 $R_\mathrm L=1\,\mathrm{k\Omega}$ 时的 $U_2$。更好的电压的代价是什么？

</li>

<li>

极限情况：对原来的分压器，$R_\mathrm L\to0$ 时 $I_\mathrm L$ 是多少？

</li>

</ol>

:::loesung
(a) 空载时 $U_{2,0}=U\,R_2/(R_1+R_2)$。由式 [(10.4)](#gl-10-4) 得

$$\frac{U_2}{U_{2,0}}=\frac{R_\mathrm L\,(R_1+R_2)}{R_1R_2+R_\mathrm L\,(R_1+R_2)}=\frac{R_\mathrm L}{R_\mathrm i+R_\mathrm L},\qquad\delta=1-\frac{U_2}{U_{2,0}}=\frac{R_\mathrm i}{R_\mathrm i+R_\mathrm L}.$$

(b) $\delta=0.1$ 得 $R_\mathrm L=9\,R_\mathrm i=6\,\mathrm{k\Omega}$，$U_2=2.7$ V。

(c) $R_\mathrm i=66.7\,\Omega$，$U_2=2.81$ V，误差与前面 $10\,\mathrm{k\Omega}$ 时相同。代价是分压器中流过 30 mA 而不是 3 mA，它转换的功率为 270 mW 而不是 27 mW。

(d) $R_\mathrm L\to0$ 使 $R_2$ 短路：$I_\mathrm L=9\,\mathrm{V}/2\,\mathrm{k\Omega}=4.5$ mA。
:::
:::

:::aufgabe 练习 12 ★★★ R-2R 梯形网络
<span class="anker" id="aufg-12"></span>

一个如图 [12](#abb-12) 所示、有四个节点的梯形网络，$R=10\,\mathrm{k\Omega}$，$U_\mathrm{ref}=5$ V。

<ol class="al">

<li>

电源看到的电阻是多少？$I_\mathrm{ref}$ 和各节点电压是多少？

</li>

<li>

流过上方四个 $2R$ 的电流各是多少？

</li>

<li>

数字 1001 时 $I_\mathrm{out}$ 是多少？最小的级是多少？

</li>

</ol>

:::loesung
(a) 电源看到 $2R\parallel2R=R=10\,\mathrm{k\Omega}$，所以 $I_\mathrm{ref}=0.5$ mA。节点电压为 5；2.5；1.25；0.625 V。 (b) 0.25；0.125；0.0625；0.03125 mA。 (c) 数字 1001：$0.25+0.03125=0.281$ mA。最小的级是 31.25 µ A。
:::
:::
