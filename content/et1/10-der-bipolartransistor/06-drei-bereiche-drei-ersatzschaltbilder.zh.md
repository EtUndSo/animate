---
title: 第 4 阶段：三个工作区，三种等效电路
pfad: 电气工程 / 第 1 学期 / ET1 – 电气工程基础 1：电路分析导论 / 双极型晶体管
adresse: elektrotechnik/1-semester/grundlagen-der-elektrotechnik/der-bipolartransistor
knoten: 第 10 章：双极型晶体管
order: 1200600
summary: 含指数函数的电路很难手工求解。本阶段用三个线性片段代替曲面。
tags: 截止区, 饱和区, 阈值电压, 饱和电压, 等效电路
lang: zh
---

<span class="anker" id="stufe-4"></span>

:::zweck
含指数函数的电路很难手工求解。本阶段用三个线性片段代替曲面。
:::

**基本思路。** 两个二极管各自可以导通或截止。由此得到各种工作状态。BE 二极管截止时，没有电子出发，什么也不流动。这就是__截止区__。BE 二极管导通而 CB 二极管截止时，集电极收走所有电子，$I_\mathrm{C}=B\,I_\mathrm{B}$ 成立。这就是放大区。如果 $U_\mathrm{CE}$ 下降到 CB 二极管也明显导通，集电极就会送回电子。这时它不能再收走全部电子，基区被电子充满，$I_\mathrm{C}$ 保持在 $B\,I_\mathrm{B}$ 以下。这就是__饱和区__。和二极管（[第 9 章](/wissen/zh/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/halbleiter-und-dioden/halbleiter-und-dioden.html)）一样，用直线代替曲线：输入特性曲线在 0.6 V 处有一个拐点，电流控制特性曲线变成斜率为 $B$ 的直线，在饱和时折成水平，输出特性曲线在 0.2 V 右侧变成水平（图 [6](der-arbeitspunkt.html#abb-6)）。

:::definition 定义 4.1 (npn 晶体管的工作区)
<span class="anker" id="satz-4-1"></span>

取__阈值电压__ $U_\mathrm{BE,on}=0.6$ V 和__饱和电压__ $U_\mathrm{CE,sat}=0.2$ V，则有：

<span class="anker" id="gl-4-1"></span>
<span class="anker" id="gl-4-2"></span>
<span class="anker" id="gl-4-3"></span>
$$\begin{aligned} \text{截止区：}\quad & U_\mathrm{BE}<U_\mathrm{BE,on}\;\Rightarrow\; I_\mathrm{B}=I_\mathrm{C}=0,\\ \text{放大区：}\quad & U_\mathrm{BE}=U_\mathrm{BE,on},\ I_\mathrm{B}>0,\quad I_\mathrm{C}=B\,I_\mathrm{B},\quad U_\mathrm{CE}\ge U_\mathrm{CE,sat},\\ \text{饱和区：}\quad & U_\mathrm{BE}=U_\mathrm{BE,on},\ I_\mathrm{B}>0,\quad U_\mathrm{CE}=U_\mathrm{CE,sat},\quad I_\mathrm{C}\le B\,I_\mathrm{B}. \end{aligned} \tag{4.1|4.2|4.3}$$
:::

⁠**如何理解：**每个工作区都有一个由理想元件构成的线性__等效电路__，适用于 B、C、E 之间（图 [5](#abb-5)）。在截止区，所有接线端都开路。在两个导通的工作区，B 和 E 之间是一个 0.6 V 的电压源；C 和 E 之间，在放大区是一个受控电流源，在饱和区是一个 0.2 V 的电压源。在公共节点处始终有 $I_\mathrm{E}=I_\mathrm{B}+I_\mathrm{C}$。**适用条件：**这是粗略但行之有效的近似。阈值并不是真正的开关（第 [2](warum-strom-durch-die-gesperrte-diode-fliet.html#stufe-2) 阶段）；0.6 V 对应 T 在 2 mA 时的情况，20 mA 时应为 0.66 V。0.2 V 这个值取决于类型。

:::abbildung et1/k10esb 5
npn 晶体管的三种等效电路。左：截止区，开路。中：放大区，含受控电流源。右：饱和区，含两个电压源。$I_\mathrm{B}$ 和 $I_\mathrm{C}$ 在 E 上方的节点处汇合。
:::

::::beispiel
对 T（$B=200$）有：$I_\mathrm{B}=10$ µ A 且 $U_\mathrm{CE}=6$ V 是放大区，所以 $I_\mathrm{C}=2$ mA。$I_\mathrm{B}=30$ µ A 且 $I_\mathrm{C}=3.9$ mA 是饱和区，因为 $B\,I_\mathrm{B}=6$ mA 大于电路允许的电流。$U_\mathrm{BE}=0.3$ V 是截止区。
::::

⁠**极限情况：**当 $B\,I_\mathrm{B}=I_\mathrm{C}$ 且 $U_\mathrm{CE}=U_\mathrm{CE,sat}$ 时，晶体管正好处在放大区和饱和区的边界上。两种等效电路在那里给出相同的结果。

:::frage 电流明明不再跟随了，为什么叫饱和？
饱和的不是电流，而是基区：它被电子塞得过满。因此，对双极型晶体管来说，这个词指的是输出特性曲线左侧的陡峭部分。对 MOSFET 来说，平坦部分才叫饱和。这两个词含义不同。
:::

**pnp 晶体管。** 在 pnp 晶体管中，n 和 p 互换（图 [1](drei-schichten-zwei-spannungen.html#abb-1)）。机理不变，只是空穴取代了电子的角色。发射极处于最高电位，所有符号都反过来。沿用 npn 的名称，现在 $U_\mathrm{BE,on}=-0.6$ V 和 $U_\mathrm{CE,sat}=-0.2$ V 都是负值。如果 $I_\mathrm{B}$ 和 $I_\mathrm{C}$ 以流出元件为正，二者都是正值，并有：

<span class="anker" id="gl-4-4"></span>
$$\begin{aligned} &\text{截止区：} U_\mathrm{BE}>-0.6\,\mathrm{V};\qquad \text{放大区：} I_\mathrm{C}=B\,I_\mathrm{B},\ U_\mathrm{CE}\le-0.2\,\mathrm{V};\\ &\text{饱和区：} U_\mathrm{CE}=-0.2\,\mathrm{V},\ I_\mathrm{C}\le B\,I_\mathrm{B}. \end{aligned} \tag{4.4}$$

实际中 npn 晶体管更常见，因为硅中电子的迁移率约为空穴的三倍。pnp 形式主要用于发射极要接正电源的场合。

:::aufgabe 练习 4 ★ 判断工作区
<span class="anker" id="aufg-4"></span>

确定 T 的工作区以及所缺的电流或电压。 (a) $I_\mathrm{B}=20$ µ A，$U_\mathrm{CE}=5$ V。 (b) $I_\mathrm{B}=40$ µ A，$I_\mathrm{C}=3$ mA。 (c) $U_\mathrm{BE}=-1$ V，$U_\mathrm{CE}=12$ V。 (d) $B=200$ 的 pnp 晶体管：$U_\mathrm{CE}=-5$ V，$I_\mathrm{B}=10$ µ A。

:::loesung
(a) $I_\mathrm{B}>0$ 且 $U_\mathrm{CE}>0.2$ V：放大区，$I_\mathrm{C}=4$ mA。 (b) $B\,I_\mathrm{B}=8$ mA $>3$ mA：饱和区，$U_\mathrm{CE}=0.2$ V。 (c) $U_\mathrm{BE}<0.6$ V：截止区，$I_\mathrm{B}=I_\mathrm{C}=0$。 (d) $U_\mathrm{CE}\le-0.2$ V 且 $I_\mathrm{B}>0$：放大区，$I_\mathrm{C}=2$ mA，$U_\mathrm{BE}=-0.6$ V。
:::
:::
