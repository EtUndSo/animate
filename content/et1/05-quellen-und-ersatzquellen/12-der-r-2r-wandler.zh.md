---
title: 第 10 阶段：R-2R 转换器
pfad: 电气工程 / 第 1 学期 / ET1 – 电气工程基础 1：电路分析导论 / 电源与等效电源
adresse: elektrotechnik/1-semester/grundlagen-der-elektrotechnik/quellen-und-ersatzquellen
knoten: 第 5 章：电源与等效电源
order: 1151200
summary: 处理器只认识比特，扬声器需要电压。R-2R 转换器完成这一翻译。它把叠加和等效电源集中在一个电路里。
tags: 数模转换器
lang: zh
---

<span class="anker" id="stufe-10"></span>

:::zweck
处理器只认识比特，扬声器需要电压。R-2R 转换器完成这一翻译。它把叠加和等效电源集中在一个电路里。
:::

**基本思路。** __数模转换器__把带有比特 $d_2d_1d_0$ 的二进制数变成电压。在图 [12](#abb-12) 中，每个开关把它的 2$R$ 电阻接到 $U_\mathrm{ref}$（比特 1）或 0 V（比特 0）。接在 0 V 上的开关就是一个关闭的电压源。所以叠加已经包含在结构之中：每个置位的比特是一个电源，其余的都是导线。由 $R$ 和 $2R$ 组成的梯形网络经过这样的设计：每一梯级使作用减半。

:::abbildung et1/k5r2r 12
三比特 R-2R 转换器，开关位置为 101。每个转换开关把它的电阻接到 $U_\mathrm{ref}$ 或接地点。输出从右上方引出。
:::

:::satz 定理 10.1 (R-2R 梯形网络)
<span class="anker" id="satz-10-1"></span>

对图 [12](#abb-12) 的转换器，输出开路时有

<span class="anker" id="gl-10-1"></span>
$$U_\mathrm{out}=U_\mathrm{ref}\left(\frac{d_2}{2}+\frac{d_1}{4}+\frac{d_0}{8}\right),\qquad R_\mathrm{i}=R. \tag{10.1}$$
:::

⁠**如何理解：**$d_k$ 为 0 或 1，$U_\mathrm{ref}$ 是固定的参考电压（几伏），$R$ 通常为几 k$\Omega$。最高有效位贡献参考电压的一半，后面每一位贡献前一位的一半。$R_\mathrm{i}$ 与开关位置无关：关闭时 $U_\mathrm{ref}$ 变为 0 V，这时不管开关处于什么位置，每条支路都通向接地点。**适用条件：**理想开关，本身没有电阻，输出不带负载。

:::herleitung 从左到右的等效电源
在左边的节点上，2$R$ 接接地点，2$R$ 接 $U_0=d_0U_\mathrm{ref}$。这是一个 $\frac12U_0$、$2R\parallel2R=R$ 的等效电源。加上串联电阻后变为 $\frac12U_0$ 和 $2R$。在下一个节点上，它与接 $U_1=d_1U_\mathrm{ref}$ 的 2$R$ 相遇：又是两条相同的支路，也就是式 [(7.2)](quellen-zusammenschalten.html#gl-7-2) 的求平均，得等效电源 $\frac12\bigl(\frac12U_0+U_1\bigr)$，电阻又是 $R$。最后一个节点重复这一过程：

$$U_\mathrm{out}=\tfrac12\Bigl(\tfrac12\bigl(\tfrac12U_0+U_1\bigr)+U_2\Bigr)=\tfrac12U_2+\tfrac14U_1+\tfrac18U_0.$$

叠加给出同样的数。以电源 $U_1$ 为例：在中间节点上，它向左看到 2$R$，向右看到 $R+2R=3R$，合起来是 $\frac65R$。分压给出那里的 $\frac{6/5}{6/5+2}=\frac38U_1$。到输出的路径再分压一次，系数为 $\frac{2R}{R+2R}=\frac23$，于是 $\frac38\cdot\frac23=\frac14$。
:::

::::beispiel
取 $U_\mathrm{ref}=8$ V，$R=1$ k$\Omega$，各比特的权重为 4 V、2 V 和 1 V。位置 101 给出 5 V。负载 $R_\mathrm{L}=R$ 与 $R_\mathrm{i}$ 构成分压器，使其减半为 2.5 V。因此实际的转换器后面接一个输入电阻很高的运算放大器（[第 11 章](/wissen/zh/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/der-operationsverstarker/der-operationsverstaerker.html)）：它几乎不取电流，梯形网络保持开路。
::::

⁠**极限情况：**位置 000 给出 0 V，位置 111 给出 7 V，比 $U_\mathrm{ref}$ 低一级。

:::ltspice 转换器在计数
⁠**绘制：**图 [12](#abb-12) 去掉开关：2$R$ 从节点 `n0` 到接地点，然后 `n0`、`n1`、`n2` 各经 2$R$ 接到一个对接地点的电源 `voltage`，节点之间接 $R$，$R=1$ k$\Omega$。各电源按二进制计数：`PULSE(0 8 1m 1u 1u 1m 2m)`，`PULSE(0 8 2m 1u 1u 2m 4m)`，`PULSE(0 8 4m 1u 1u 4m 8m)`。

⁠**指令：**`.tran 8m`

⁠**你会看到：**`V(n2)` 是阶梯，每级 1 V，从 0 V 到 7 V。在 `n2` 上接 1 k$\Omega$ 负载时，它只升到 3.5 V。接 3 k$\Omega$ 时，最高一级上出现你在练习 [12](#aufg-12)(c) 中的结果。
:::

:::frage 最左边那个单独的 2$R$ 电阻有什么用？
它使梯形网络均匀。有了它，每个节点左边的全部电路都是一个 $2R$ 的等效电源，正如该节点自身开关的支路一样。只有这样才会出现两条相同的支路和纯粹的平均值。没有它，左支路将是 $3R$，权重就不再是二进制的了。
:::

:::aufgabe 练习 12 ★★ 四比特
<span class="anker" id="aufg-12"></span>

(a) 四比特转换器工作在 $U_\mathrm{ref}=16$ V。每级、最大值和 1011 时的电压各是多少？(b) 八比特、5 V 时每级是多少？(c) 例中的三比特转换器处于 111，向 $R_\mathrm{L}=3R$ 供电。电压是多少？

:::loesung
(a) 每级 $16\,\mathrm{V}/2^4=1$ V。最大值 $15$ V。1011：$8+0+2+1=11$ V。公式继续写为 $d_3/2+d_2/4+d_1/8+d_0/16$。

(b) $5\,\mathrm{V}/256=19.5$ mV。

(c) 开路 7 V，内阻 $R$。分压：$7\,\mathrm{V}\cdot\frac{3R}{R+3R}=5.25$ V。
:::
:::
