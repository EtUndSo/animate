---
title: 第 7 阶段：为什么是 50 %，以及该以什么为目标
pfad: 电气工程 / 第 1 学期 / 电气工程基础 / 功率、匹配与效率
order: 1170800
summary: 功率最大时浪费了一半。本阶段说明为什么这是不可避免的，以及什么时候仍然需要这样做。
tags: 
lang: zh
---

<span class="anker" id="stufe-7"></span>

:::zweck
功率最大时浪费了一半。本阶段说明为什么这是不可避免的，以及什么时候仍然需要这样做。
:::

**基本思路。** 由 $\eta=U_\mathrm{L}/U_\mathrm{q}$ 和电源直线可知：效率随电流线性下降，因为电流越大，留在 $R_\mathrm{i}$ 上的电压越多。而电源的功率 $P_\mathrm{q}=U_\mathrm{q}I$ 随电流线性上升。到达负载的是两者的乘积，$P_\mathrm{L}=P_\mathrm{q}\,\eta$。一条上升直线和一条下降直线的乘积是一条抛物线，顶点在中点，而下降直线在那里正好处于一半高度（图 [8](#abb-8)）。这 50 % 既非偶然，也与材料无关。

:::satz 定理 7.1 (功率与效率)
<span class="anker" id="satz-7-1"></span>

把 $U_\mathrm{L}=U_\mathrm{q}-R_\mathrm{i}I$ 除以 $U_\mathrm{q}$，并令 $x=I/I_\mathrm{SC}$，得

<span class="anker" id="gl-7-1"></span>
$$\eta=1-x,\qquad\frac{P_\mathrm{L}}{P_\mathrm{SC}}=x\,\eta=x(1-x). \tag{7.1}$$

功率匹配时 $x=\frac12$，所以 $\eta=\frac12$。
:::

⁠**如何理解：**$x$ 是电流占短路电流的比例，$\eta$ 是每库仑的能量中到达负载的比例。**简而言之：**在功率最大时，每份电荷把一半能量释放在电源中，另一半释放在负载中。**适用条件：**同第 [5](wohin-die-leistung-einer-quelle-geht.html#stufe-5) 阶段。**极限情况：**$x=0$ 是开路，$\eta=1$；$x=1$ 是短路，$\eta=0$。两种情况下都有 $P_\mathrm{L}=0$。

:::abbildung et1/k7kurven 8
左图：负载功率和效率随 $R_\mathrm{L}/R_\mathrm{i}$ 的变化。功率最大值位于 1 处，此时 $\eta=0.5$。右图是同样的曲线随电流的变化：$\eta$ 变成直线，功率变成抛物线。以 $P_\mathrm{L,max}=P_\mathrm{SC}/4$ 归一化。
:::

**三种目标。** 哪种工作方式正确，取决于看重什么。

| 匹配 | 条件 | 结果 | $\eta$ | 应用 |
|---|---|---|---|---|
| 电压 | $R_\mathrm{L}\gg R_\mathrm{i}$ | $U_\mathrm{L}\approx U_\mathrm{q}$，几乎与负载无关 | 接近 1 | 电网、电池、电压表 |
| 电流 | $R_\mathrm{L}\ll R_\mathrm{i}$ | $I\approx I_\mathrm{SC}$，几乎与负载无关 | 接近 0 | 电流表、电流源 |
| 功率 | $R_\mathrm{L}=R_\mathrm{i}$ | $P_\mathrm{L}$ 最大 | $\frac12$ | 天线、信号处理 |

::::beispiel
在这块电池上，$R_\mathrm{L}=200\,\Omega$ 时电压为 8.91 V，是 $U_\mathrm{q}$ 的 99 %。$R_\mathrm{L}=0.02\,\Omega$ 时电流为 4.46 A，是 $I_\mathrm{SC}$ 的 99 %。从 2 $\Omega$ 换到 8 $\Omega$ 损失 36 % 的功率，并把电池中的热量降到 16 %。
::::

⁠**电力工程。**功率在 kW 量级，电源中的热量既费钱又危及电源。人们要求高效率，即 $R_\mathrm{i}\ll R_\mathrm{L}$。一块 18 V、60 m$\Omega$ 的电动工具电池在 120 A 启动时仍能达到 $\eta=1-7.2\,\mathrm{V}/18\,\mathrm{V}=60$ %，内部产生 $(120\,\mathrm{A})^2\cdot60\,\mathrm{m\Omega}=864$ W。一盏 1.8 W 的工作灯相当于 180 $\Omega$，$\eta=180/180.06=99.97$ %。在这里，匹配意味着电池中有 1350 W 的热量。

⁠**通信工程。**功率在 µ W 量级。接收机只能取用天线提供的功率。重要的是功率的绝对值，而不是比例，电源中的热量也无妨。一根 10 mV、50 $\Omega$ 的天线向 50 $\Omega$ 恰好输出 0.5 µ W，向 5 $\Omega$ 或 500 $\Omega$ 只输出 0.165 µ W。

**等效电源：最大值不变，50 % 不再成立。** 电源往往是一个网络。图 [9](#abb-9) 所示是一个内阻为 $R_\mathrm{q}$ 的电源，并联了 $R$。对接线端 A、B 而言，它是一个等效电源（[第 5 部分](/wissen/zh/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/quellen-und-ersatzquellen/quellen-und-ersatzquellen.html)），$R_\mathrm{i}=R_\mathrm{q}\parallel R$，$U_\mathrm{OC}=U_\mathrm{q}R/(R_\mathrm{q}+R)$。对负载来说，只有接线端上的直线起作用，所以最大值位于 $R_\mathrm{L}=R_\mathrm{i}$，此时

<span class="anker" id="gl-7-2"></span>
$$U_\mathrm{L}=U_\mathrm{q}\,\frac{R}{2(R_\mathrm{q}+R)},\qquad P_\mathrm{L}=\frac{U_\mathrm{L}^2}{R_\mathrm{L}}=\frac{U_\mathrm{q}^2\,R}{4\,R_\mathrm{q}(R_\mathrm{q}+R)}. \tag{7.2}$$

但真实电源的工作负载是 $R_\mathrm{tot}=R_\mathrm{q}+R\parallel R_\mathrm{L}$，由此得

<span class="anker" id="gl-7-3"></span>
$$P_\mathrm{q}=\frac{U_\mathrm{q}^2}{R_\mathrm{tot}}=\frac{U_\mathrm{q}^2\,(2R_\mathrm{q}+R)}{2R_\mathrm{q}(R_\mathrm{q}+R)},\qquad\eta=\frac{P_\mathrm{L}}{P_\mathrm{q}}=\frac12\,\frac{R}{2R_\mathrm{q}+R}<\frac12\quad\text{当 }R<\infty\text{ 时。} \tag{7.3}$$

:::abbildung et1/k7netz 9
左图为匹配时的网络及实际功率。右图为其等效电源。对负载而言两者相同，在电源内部则不同。
:::

:::herleitung 式 [(7.3)](#gl-7-3) 的变形
由 $R_\mathrm{L}=R_\mathrm{q}R/(R_\mathrm{q}+R)$ 得 $R\parallel R_\mathrm{L}=R^2R_\mathrm{q}/(R^2+2R_\mathrm{q}R)=R\,R_\mathrm{q}/(R+2R_\mathrm{q})$。于是 $R_\mathrm{tot}=2R_\mathrm{q}(R_\mathrm{q}+R)/(2R_\mathrm{q}+R)$。一般地，分压公式给出 $U_\mathrm{L}=U_\mathrm{q}(R\parallel R_\mathrm{L})/R_\mathrm{tot}=U_\mathrm{q}\,R\,R_\mathrm{L}/\bigl(R_\mathrm{q}(R+R_\mathrm{L})+R\,R_\mathrm{L}\bigr)$。代入即得式 [(7.2)](#gl-7-2) 中的公式。于是 $P_\mathrm{L}=U_\mathrm{L}^2(R_\mathrm{q}+R)/(R_\mathrm{q}R)$。$P_\mathrm{L}$ 与 $P_\mathrm{q}$ 之商约简后即为式 [(7.3)](#gl-7-3)。
:::

::::beispiel
对于 $U_\mathrm{q}=18$ V，$R_\mathrm{q}=6\,\Omega$，$R=3\,\Omega$，有 $R_\mathrm{i}=2\,\Omega$，$U_\mathrm{OC}=6$ V。当 $R_\mathrm{L}=2\,\Omega$ 时，负载上为 3 V，得到 4.5 W。流过 $R_\mathrm{q}$ 的电流为 2.5 A，其中 1 A 流过 $R$。这样 $R_\mathrm{q}$ 中为 37.5 W，$R$ 中为 3 W，加上负载，$P_\mathrm{q}=45$ W，$\eta=10$ %。等效电源看起来显示 50 %，因为它对内部什么也没有说明。流过 $R$ 的电流在没有负载时也存在，开路时网络就已经以 36 W 发热。
::::

⁠**极限情况：**当 $R\to\infty$ 时，这条支路不复存在，式 [(7.3)](#gl-7-3) 又给出 $\eta=\frac12$。

:::frage 最大值处 $\eta=50$ % 是否意味着匹配时我“损失”了一半能量？
对于有真实内阻的电源，是的，它和负载发热一样多。功率小时这可以接受。在能量昂贵或电源敏感的场合，工作点要远在最大值的右侧。
:::

:::aufgabe 练习 7 ★ 属于哪种目标？
<span class="anker" id="aufg-7"></span>

归类并计算：(a) 10 M$\Omega$ 的电压表接在电池上。读数偏离 9 V 多少？(b) 0.1 $\Omega$ 的电流表接在 5 V 和 1 k$\Omega$ 的电路中。它使电流改变百分之几？(c) 12 V、50 m$\Omega$ 的电源适配器接 6 $\Omega$。$\eta$ 是多少？(d) 在同一电源适配器上进行功率匹配会有什么结果？

:::loesung
(a) 电压匹配：$R_\mathrm{L}\gg R_\mathrm{i}$。电流为 0.9 µ A，内部压降为 1.8 µ V。 (b) 电流匹配：电源表现为高内阻。电流从 5 mA 下降 0.01 %。 (c) 电压匹配：$\eta=6/6.05=99.2$ %。 (d) $R_\mathrm{L}=50$ m$\Omega$ 时，负载上有 720 W，电源适配器中也有 720 W，这会造成损坏。
:::
:::

:::aufgabe 练习 8 ★★★ 匹配时的网络
<span class="anker" id="aufg-8"></span>

一个 $U_\mathrm{q}=24$ V、$R_\mathrm{q}=4\,\Omega$ 的电源接有 $R=12\,\Omega$，负载与 $R$ 并联。(a) 求 $R_\mathrm{i}$ 和 $U_\mathrm{OC}$。(b) 计算匹配时的 $U_\mathrm{L}$ 和 $P_\mathrm{L}$。(c) 计算 $P_\mathrm{q}$ 和 $\eta$，一次由各电流计算，一次用式 [(7.3)](#gl-7-3)。(d) $R$ 应为多大才能使 $\eta=45$ %？

:::loesung
(a) $R_\mathrm{i}=4\,\Omega\parallel12\,\Omega=3\,\Omega$，$U_\mathrm{OC}=24\,\mathrm{V}\cdot12/16=18$ V。 (b) $U_\mathrm{L}=9$ V，$P_\mathrm{L}=(9\,\mathrm{V})^2/3\,\Omega=27$ W $=U_\mathrm{OC}^2/(4R_\mathrm{i})$。 (c) 负载上 3 A，$R$ 上 0.75 A，所以电源输出 3.75 A。$P_\mathrm{q}=90$ W $=56.25\,\mathrm{W}+6.75\,\mathrm{W}+27\,\mathrm{W}$，$\eta=30$ %，与 $\frac12\cdot12/20$ 相同。 (d) 由 $\frac12R/(8\,\Omega+R)=0.45$ 得 $R=72\,\Omega$。
:::
:::
