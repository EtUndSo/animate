---
title: 第 5 阶段：实际电源与工作点
pfad: 电气工程 / 第 1 学期 / 电气工程基础 / 电源与等效电源
order: 1150700
summary: 电池带负载时保持不住电压。本阶段说明其原因，并求出负载在特性曲线上确定的那个点。
tags: 等效电路, 实际电压源, 实际电流源, 负载线, 工作点
lang: zh
---

<span class="anker" id="stufe-5"></span>

:::zweck
电池带负载时保持不住电压。本阶段说明其原因，并求出负载在特性曲线上确定的那个点。
:::

**基本思路。** 在电池中，化学反应推动电荷，并为此提供每库仑固定的能量，这就是源电压。但电流必须穿过电池本身：离子在电解液中迁移，电子通过电极和连接件。在此过程中能量以热的形式损失，就像在电阻中一样。到达接线端的只是余下的部分。电流越大，内部压降越大。这个压降与电流成正比，所以特性曲线是一条下降的直线。

:::abbildung et1/k5arbeitsgerade 6
左：接负载的实际电压源。右：电源从开路到短路的特性曲线（蓝色）和每个负载的负载线。交点就是工作点：16 $\Omega$ 时为 0.5 A 和 8 V，2 $\Omega$ 时为 2.25 A 和 4.5 V。
:::

:::definition 定义 5.1 (实际电源)
<span class="anker" id="satz-5-1"></span>

__等效电路__是由理想元件组成、在接线端上与真实元件行为相同的电路。__实际电压源__是理想电压源与 $R_\mathrm{q}$ 串联，__实际电流源__是理想电流源与 $G_\mathrm{q}$ 并联：

<span class="anker" id="gl-5-1"></span>
$$U_\mathrm{AB}=U_\mathrm{q}-R_\mathrm{q}\,I_\mathrm{A}, \qquad\qquad I_\mathrm{A}=I_\mathrm{q}-G_\mathrm{q}\,U_\mathrm{AB}. \tag{5.1}$$
:::

⁠**如何理解：**$U_\mathrm{q}$ 是开路电压。$R_\mathrm{q}$ 是内阻或源电阻，单位 $\Omega$：9 V 方形电池约 2 $\Omega$，汽车蓄电池约 10 m$\Omega$。$I_\mathrm{q}$ 是短路电流，$G_\mathrm{q}$ 是源电导，单位 S。第一个方程是等效电路中的网孔定律，第二个是节点定律：从 $I_\mathrm{q}$ 中分出 $G_\mathrm{q}U_\mathrm{AB}$，其余流向外部。**适用条件：**只要 $R_\mathrm{q}$ 不随电流变化，这条直线就成立。真实电池在大电流下和老化后会偏离。

**负载线。** 负载给出第二个方程 $U_\mathrm{AB}=R_\mathrm{L}I_\mathrm{A}$。这条过原点的直线称为__负载线__。两个方程必须同时成立。这只有在交点上才可能，这个交点就是__工作点__。令 $U_\mathrm{q}-R_\mathrm{q}I_\mathrm{A}=R_\mathrm{L}I_\mathrm{A}$，得：

<span class="anker" id="gl-5-2"></span>
$$I_\mathrm{A}=\frac{U_\mathrm{q}}{R_\mathrm{q}+R_\mathrm{L}},\qquad U_\mathrm{AB}=\frac{R_\mathrm{L}}{R_\mathrm{q}+R_\mathrm{L}}\,U_\mathrm{q}. \tag{5.2}$$

背后的机制：如果电源输出的电流大于负载取走的电流，电荷就会在接线端 A 积累，其电位随之升高。于是电源的电流下降，负载的电流上升。这一过程持续到两个电流相等为止。

::::beispiel
接 16 $\Omega$ 时，$I_\mathrm{A}=9\,\mathrm{V}/18\,\Omega=0.5$ A，$U_\mathrm{AB}=8$ V，内部压降为 1 V。接 2 $\Omega$ 时为 2.25 A 和 4.5 V。两点都在直线上：$9\,\mathrm{V}-2\,\Omega\cdot2.25\,\mathrm{A}=4.5$ V。两点的差值把内阻显示为斜率：$\Delta U_\mathrm{AB}/\Delta I_\mathrm{A}=3.5\,\mathrm{V}/(-1.75\,\mathrm{A})=-2\,\Omega$。
::::

⁠**极限情况：**当 $R_\mathrm{L}\to\infty$ 时，式 [(5.2)](#gl-5-2) 给出开路 $U_\mathrm{AB}=U_\mathrm{q}$；当 $R_\mathrm{L}\to0$ 时，给出短路电流 $I_\mathrm{SC}=U_\mathrm{q}/R_\mathrm{q}=4.5$ A。当 $R_\mathrm{q}\to0$ 时，剩下理想电压源。非线性负载也可以这样处理：这时它的特性是一条曲线，交点仍然是解（[第 9 部分](/wissen/zh/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/halbleiter-und-dioden/halbleiter-und-dioden.html)）。

:::ltspice 电池的特性曲线
⁠**绘制：**`voltage`，值为 9，从 `q` 到接地点；`res`，值为 2，从 `q` 到 `a`。负载用名为 `I1` 的电流源 `current`，从 `a` 到接地点。

⁠**指令：**`.dc I1 0 4.5 0.05`

⁠**你会看到：**`V(a)` 沿直线从 0 A 时的 9 V 降到 4.5 A 时的 0 V。0.5 A 时为 8 V，2.25 A 时为 4.5 V，正是图 [6](#abb-6) 中的点。为练习 [6](#aufg-6) 把数值改为 12.6 和 0.01，并运行到 200 A（`.dc I1 0 200 1`）。在 150 A 和 20 A 处读出你算出的端电压。
:::

:::frage 电池内部有 2 $\Omega$，为什么仪表测得的是 9 V？
因为仪表几乎不取电流（[第 4 部分](/wissen/zh/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/strom-und-spannung-messen/strom-und-spannung-messen.html)）。输入电阻为 10 M$\Omega$ 时，电流为 0.9 µ A，内部压降为 1.8 µ V。测到的实际上就是开路电压。内阻只有带负载时才显现出来。
:::

:::aufgabe 练习 6 ★ 起动时的车灯
<span class="anker" id="aufg-6"></span>

汽车蓄电池为 12.6 V、10 m$\Omega$。起动机相当于 74 m$\Omega$。(a) 计算起动时的电流和端电压。(b) 短路电流会是多少？(c) 车灯单独工作时取 20 A。这时端电压是多少，因而车灯的电阻是多少？(d) 车灯和起动机同时工作时端电压是多少？为什么车灯会变暗？

:::loesung
(a) $I_\mathrm{A}=12.6\,\mathrm{V}/84\,\mathrm{m\Omega}=150$ A，$U_\mathrm{AB}=12.6\,\mathrm{V}-10\,\mathrm{m\Omega}\cdot150\,\mathrm{A}=11.1$ V。

(b) $I_\mathrm{SC}=12.6\,\mathrm{V}/10\,\mathrm{m\Omega}=1260$ A。

(c) $U_\mathrm{AB}=12.6\,\mathrm{V}-0.2\,\mathrm{V}=12.4$ V，所以 $R=12.4\,\mathrm{V}/20\,\mathrm{A}=0.62\,\Omega$。

(d) 车灯与起动机并联：$0.62\,\Omega\parallel74\,\mathrm{m\Omega}=66.1\,\mathrm{m\Omega}$。与 10 m$\Omega$ 分压：$U_\mathrm{AB}=10.94$ V。蓄电池输出 165.6 A，车灯得到 17.65 A 而不是 20 A。起动机的大电流在内部产生 1.66 V 压降，车灯也受其影响。车灯的功率从 248 W 降到 193 W。
:::
:::
