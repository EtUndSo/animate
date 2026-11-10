---
title: 第 9 阶段：串联与分压器
pfad: 电气工程 / 第 1 学期 / ET1 – 电气工程基础 1：电路分析导论 / 电流、电阻与基尔霍夫定律
adresse: elektrotechnik/1-semester/grundlagen-der-elektrotechnik/strom-widerstand-und-kirchhoff
knoten: 第 2 章：电流、电阻与基尔霍夫定律
order: 1121000
summary: 许多网络由两种基本模式组成。本阶段把串联的电阻合并，说明电压如何分配，并由此构造一个转换器。
tags: 串联, 总电阻, 空载, 数模转换器, 比特, 缓冲器, 比较器, 译码器
lang: zh
---

<span class="anker" id="stufe-9"></span>

:::zweck
许多网络由两种基本模式组成。本阶段把串联的电阻合并，说明电压如何分配，并由此构造一个转换器。
:::

**基本思路。** 电阻之间没有分支，节点定律迫使所有电阻中流过相同的电流。中点稳定在使这一点成立的电位上。同样的电流在较大的电阻中需要更大的驱动：电场在那里对单位电荷做更多的功，其上的压降也更大。

:::satz 定理 9.1 (串联与分压器)
<span class="anker" id="satz-9-1"></span>

对 $N$ 个__串联__的电阻，有

<span class="anker" id="gl-9-1"></span>
<span class="anker" id="gl-9-2"></span>
$$\begin{aligned} I&=I_1=I_2=\dots=I_N,\qquad U=U_1+U_2+\dots+U_N,\qquad U_i=R_i\,I,\\ R_\mathrm{tot}&=\sum_{i=1}^{N}R_i,\qquad\frac{U_\nu}{U}=\frac{R_\nu}{\sum_{i=1}^NR_i}, \end{aligned} \tag{9.1|9.2}$$

因此对两个电阻有分压规则

<span class="anker" id="gl-9-3"></span>
$$\frac{U_2}{U}=\frac{R_2}{R_1+R_2},\qquad\frac{U_1}{U_2}=\frac{R_1}{R_2}. \tag{9.3}$$
:::

⁠**如何理解：**$R_\mathrm{tot}$ 是__总电阻__，即替代整条串联链的那一个电阻。各电压之比等于各电阻之比。**适用条件：**分压规则只在__空载__时成立：抽头处不得取用电流，否则 $I_1\neq I_2$（第 [10](parallelschaltung-stromteiler-und-belastung.html#stufe-10) 阶段）。

:::herleitung 总电阻与分压规则
网孔定律给出 $U=\sum U_i$，欧姆定律给出 $U_i=R_i\,I$，其中 $I$ 相同。所以 $U=(R_1+\dots+R_N)\,I$。$U_\nu=R_\nu\,I$ 与 $U$ 相除，$I$ 就约去了。
:::

::::beispiel
串联链的 $R_\mathrm{tot}=3\,\mathrm{k\Omega}$，所以 $I=3$ mA，$U_1=6$ V，$U_2=3$ V（图 [10](#abb-10) 左）。由式 [(9.3)](#gl-9-3)：$U_2=9\,\mathrm{V}\cdot1/3=3$ V。
::::

⁠**极限情况：**$R_2\to0$ 时 $U_2\to0$，短路不承受电压。$R_2\to\infty$ 时 $U_2\to U$，断开处承受全部电压。$R_1=R_2$ 时 $U$ 减半。

:::abbildung et1/k2teiler 10
左：参考模型的分压器。中：$U_\mathrm{ref}=3.2$ V 时 3 位转换器的电阻链。两端的 $R/2$ 使所有抽头移动半级。右：输出随数字 $Z$ 的变化。阶梯以虚线表示的理想直线为中心，误差最多半级。
:::

**应用：数模转换器。** __数模转换器__（D/A 转换器）把数字变成电压。三个__比特__（二进制位 $b_0$、$b_1$、$b_2$）给出数字 $Z=0$ 到 7。由 $R/2$、七个 $R$ 和 $R/2$ 组成的电阻链总电阻为 $8R$，把 $U_\mathrm{ref}$ 分成八级。各抽头上的电压为

<span class="anker" id="gl-9-4"></span>
$$U_Z=\Bigl(Z+\frac12\Bigr)\frac{U_\mathrm{ref}}{8}. \tag{9.4}$$

由开关构成的树（每比特一层）恰好让一个抽头接通。__缓冲器__是放大倍数为 1 的放大器，它输出电压而不从电阻链取用电流，使分压器保持空载。$U_\mathrm{ref}=3.2$ V 时每级为 0.4 V，$Z=5$ 给出 2.2 V。

**应用：闪速模数转换器。** 同样的电阻链也可以反过来工作。__比较器__是一种报告两个电压中哪个较高的器件，它把输入电压同时与每个抽头比较。__译码器__是一种逻辑电路，它把这些报告变成三位数字。对于数字 0 到 7，七个阈值就够了，这里是 0.2 至 2.6 V。第八个阈值可用于报告溢出。在 1.3 V 时，有三个阈值低于它，转换器输出 $Z=3$，即 $3\cdot0.4\,\mathrm{V}=1.2$ V，这是最接近的级的倍数。

:::frage 第一个电阻不会阻碍电流，使到达第二个电阻的电流变少吗？
不会，电流不会被消耗（第 [1](strom-ist-bewegte-ladung.html#stufe-1) 阶段）。电子不会在 $R_2$ 之前堆积，否则中点就会充电，直到两个电流相等。$R_2$ 会反作用于整个电路，因为那一个共同的电流是由 $R_1+R_2$ 决定的。
:::

:::aufgabe 练习 9 ★ 设计分压器
<span class="anker" id="aufg-9"></span>

<ol class="al">

<li>

要由 12 V 得到 3.3 V，$R_2=3.3\,\mathrm{k\Omega}$。计算 $R_1$。与它相邻的 E24 值是哪些（8.2 和 9.1 k$\Omega$），它们给出多大的电压？

</li>

<li>

由 $1$、$2$、$3$ 和 $6\,\mathrm{k\Omega}$ 组成的电阻链接在 24 V 上。写出电流和各分电压。

</li>

<li>

一个 3 位转换器的 $U_\mathrm{ref}=5$ V。$Z=6$ 时它输出多大电压？

</li>

</ol>

:::loesung
(a) $R_1=R_2\,(12-3.3)/3.3=8.7\,\mathrm{k\Omega}$。用 $8.2\,\mathrm{k\Omega}$ 得 3.44 V（$+4.3\,\%$），用 $9.1\,\mathrm{k\Omega}$ 得 3.19 V（$-3.2\,\%$）。 (b) $R_\mathrm{tot}=12\,\mathrm{k\Omega}$，$I=2$ mA，分电压为 2、4、6 和 12 V。 (c) $U_6=6.5\cdot5\,\mathrm{V}/8=4.06$ V。
:::
:::
