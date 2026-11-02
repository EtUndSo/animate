---
title: 第 8 阶段：叠加
pfad: 电气工程 / 第 1 学期 / 电气工程基础 / 电源与等效电源
order: 1151000
summary: 如果网络的不同位置上有多个电源，只靠组就不够了。
tags: 叠加法, 独立, 灵敏度
lang: zh
---

<span class="anker" id="stufe-8"></span>

:::zweck
如果网络的不同位置上有多个电源，只靠组就不够了。__叠加法__把问题分解为每个电源一次计算。
:::

**基本思路。** 网络由三类方程确定：节点定律、网孔定律、欧姆定律。只要 $R$ 固定，这些方程中都不出现电流和电压的乘积或平方。这样的方程是线性的。如果这样的方程组对一个电源的解是 $x'$，对另一个电源的解是 $x''$，那么两个电源同时作用时的解就是 $x'+x''$。代入即可看出：每个方程都逐项相加。所以每个电源都驱动自己的电流流过网络，仿佛另一个电源不存在，这些电流在每条支路中相加。

:::satz 定理 8.1 (叠加)
<span class="anker" id="satz-8-1"></span>

在含 $n$ 个独立电压源和 $m$ 个独立电流源的线性网络中，每个支路电压和每个支路电流都满足

<span class="anker" id="gl-8-1"></span>
<span class="anker" id="gl-8-2"></span>
$$\begin{aligned} U_\mathrm{AB}&=a_1U_\mathrm{q1}+\dots+a_nU_{\mathrm{q}n}+Z_1I_\mathrm{q1}+\dots+Z_mI_{\mathrm{q}m},\\ I_\mathrm{CD}&=Y_1U_\mathrm{q1}+\dots+Y_nU_{\mathrm{q}n}+b_1I_\mathrm{q1}+\dots+b_mI_{\mathrm{q}m}. \end{aligned} \tag{8.1|8.2}$$

系数只取决于电阻，与电源无关。
:::

⁠**如何理解：**如果电源的数值不取决于网络中的任何量，它就是__独立__的。$a_k$ 是从电源 $k$ 到电压 $U_\mathrm{AB}$ 的电压增益，没有单位：电源每变化 1 伏，$U_\mathrm{AB}$ 变化这么多伏。这也称为__灵敏度__。$Z_k$ 是从电流源到这个电压的转移电阻（跨阻），单位 $\Omega$。相应地，$Y_k$（单位 S）和电流增益 $b_k$ 描述两个节点 C、D 之间的电流。$U_\mathrm{AB}$ 和 $I_\mathrm{CD}$ 代表网络中的任意电压和任意电流。**适用条件：**只适用于线性网络，并且只适用于电压和电流。

**步骤。**

<ol>

<li>

除一个电源外，关闭所有电源。数值为零的理想电压源迫使其接线端电位相等，导线的作用正是如此：它变成**短路**。数值为零的理想电流源迫使电流为零，断口的作用正是如此：它变成**断开的接线端**。实际电源的内阻留在网络中。

</li>

<li>

算出这一个电源的部分作用。通常只剩下一个分压器或分流器。

</li>

<li>

对每个电源重复，并把所有部分作用按正确的符号相加。

</li>

</ol>

:::abbildung et1/k5ueberlagerung 9
网络 N 及其两个分电路。中：电流源断开，剩下一个分压器。右：电压源是一根导线，电流源向并联的 $R_1$ 和 $R_2$ 供电。接线端 A 和 B 断开。
:::

**例。** 求接线端断开时 N 中的 $U_\mathrm{AB}$（图 [9](#abb-9)）。分电路 1：分压器，$U'=\frac{R_2}{R_1+R_2}\,U_\mathrm{q1}=\frac13\cdot18\,\mathrm{V}=6$ V。分电路 2：$U''=(R_1\parallel R_2)\,I_\mathrm{q2}=2\,\Omega\cdot1.5\,\mathrm{A}=3$ V。相加：$U_\mathrm{AB}=9$ V。因此系数是：$U_\mathrm{q1}$ 的 $a=\frac13$，$I_\mathrm{q2}$ 的 $Z=2\,\Omega$。**检验**（用 A 点的节点定律）：经 $R_1$ 流来 $(18-9)\,\mathrm{V}/6\,\Omega=1.5$ A，加上电流源的 1.5 A，经 $R_2$ 流走 $9\,\mathrm{V}/3\,\Omega=3$ A。支路电流也叠加：$R_1$ 中有分电路 1 的 $2$ A 和分电路 2 的 $-0.5$ A。**极限情况：**两个电源都加倍时，$U_\mathrm{AB}$ 加倍到 18 V，因为系数不变。

:::herleitung N 的系数
接线端断开时，A 点的节点定律为 $(U_\mathrm{q1}-U_\mathrm{AB})/R_1+I_\mathrm{q2}=U_\mathrm{AB}/R_2$。解出所求电压：

$$U_\mathrm{AB}=\frac{R_2}{R_1+R_2}\,U_\mathrm{q1}+\frac{R_1R_2}{R_1+R_2}\,I_\mathrm{q2}.$$

这就是式 [(8.1)](#gl-8-1) 的形式：每一项属于一个电源，系数中只含电阻。
:::

**界限：功率。** 电阻上的功率是电压的二次函数，$P=UI=U^2/R$（[第 7 部分](/wissen/zh/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/leistung-anpassung-und-wirkungsgrad/leistung-und-anpassung.html)）。在 $R_2$ 上，相加会得到 $(6\,\mathrm{V})^2/3\,\Omega+(3\,\mathrm{V})^2/3\,\Omega=15$ W。实际是 $(9\,\mathrm{V})^2/3\,\Omega=27$ W。缺少的是交叉项 $2U'U''/R_2=12$ W。功率不能叠加，电压和电流可以。后面会出现一个例外：对频率不同的交流量，交叉项的时间平均值为零。同样，一旦网络中有二极管，叠加也不再成立（[第 9 部分](/wissen/zh/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/halbleiter-und-dioden/halbleiter-und-dioden.html)）。

:::frage 为什么不能把关闭的电压源从网络中拿掉？
因为零伏并不等于“什么都没有”。电源仍是线路的一部分，只是不再维持电压。把它拿掉，就切断了经过它的电流路径。那是电流源的情况，不是电压源的情况。
:::

:::aufgabe 练习 9 ★★ 两个电源，一个负载
<span class="anker" id="aufg-9"></span>

从节点 C 有三条支路通向公共接地点：$R_3=4\,\Omega$ 直接相连，$R_\mathrm{s}=2\,\Omega$ 与 $U_\mathrm{s}=12$ V 串联，$R_\mathrm{t}=4\,\Omega$ 与 $U_\mathrm{t}=6$ V 串联（两个正极都朝向 C）。(a) 用叠加法并以一般公式计算 $R_3$ 上的电压 $U_3$。用节点定律检验。(b) 比较 $R_3$ 中的实际功率与各部分功率之和。(c) $U_3$ 对 $U_\mathrm{t}$ 的灵敏度是多少？由此不必全部重算，$U_\mathrm{t}=8$ V 时结果是什么？

:::loesung
(a) 关闭 $U_\mathrm{t}$：$R_\mathrm{t}\parallel R_3=2\,\Omega$，分压 $U_3'=\frac{2}{2+2}\cdot12\,\mathrm{V}=6$ V。关闭 $U_\mathrm{s}$：$R_\mathrm{s}\parallel R_3=\frac43\,\Omega$，分压 $U_3''=\frac{4/3}{4+4/3}\cdot6\,\mathrm{V}=1.5$ V。所以 $U_3=7.5$ V。一般形式：

$$U_3=\frac{R_\mathrm{t}R_3}{R_\mathrm{s}R_\mathrm{t}+R_3(R_\mathrm{s}+R_\mathrm{t})}\,U_\mathrm{s}+\frac{R_\mathrm{s}R_3}{R_\mathrm{s}R_\mathrm{t}+R_3(R_\mathrm{s}+R_\mathrm{t})}\,U_\mathrm{t}.$$

节点定律：$\frac{12-7.5}{2}\,\mathrm{A}+\frac{6-7.5}{4}\,\mathrm{A}=2.25\,\mathrm{A}-0.375\,\mathrm{A}=1.875$ A，而 $7.5\,\mathrm{V}/4\,\Omega=1.875$ A。6 V 电源吸收电流。

(b) 各部分功率：9 W 和 0.5625 W，和为 9.56 W。实际：$(7.5\,\mathrm{V})^2/4\,\Omega=14.06$ W。

(c) $a_\mathrm{t}=\frac{1.5\,\mathrm{V}}{6\,\mathrm{V}}=\frac14$。对 8 V：$U_3=6\,\mathrm{V}+\frac14\cdot8\,\mathrm{V}=8$ V。
:::
:::
