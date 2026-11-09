---
title: 第 3 阶段：一个曲面，多条特性曲线
pfad: 电气工程 / 第 1 学期 / 电气工程基础 / 双极型晶体管
order: 1200500
summary: 数据手册给出多条坐标轴不同的特性曲线。本阶段把它们归结为同一个对象。
tags: 特性曲线, 截面, 曲线族, 输入特性曲线, 控制特性曲线, 电流控制特性曲线, 输出特性曲线, 传输特性曲线
lang: zh
---

<span class="anker" id="stufe-3"></span>

:::zweck
数据手册给出多条坐标轴不同的特性曲线。本阶段把它们归结为同一个对象。
:::

**基本思路。** $I_\mathrm{C}$ 依赖于两个电压。两个变量的函数是一个曲面，就像地图上方的地形：地图的两个方向是 $U_\mathrm{BE}$ 和 $U_\mathrm{CE}$，地形的高度是 $I_\mathrm{C}$（图 [3](#abb-3)）。固定一个电压，就得到一条__特性曲线__（两个量之间的关系，[第 5 部分](/wissen/zh/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/quellen-und-ersatzquellen/quellen-und-ersatzquellen.html)），它是地形的一个__截面__。多个平行截面构成__曲线族__。所以并不存在许多种依赖关系，而只有一个地形的多种视图。沿 $U_\mathrm{BE}$ 方向是一面陡坡（红色），沿 $U_\mathrm{CE}$ 方向先是一道棱边，然后是几乎水平的平面（绿色）。

:::abbildung et1/k10flaeche 3
参考模型的曲面 $I_\mathrm{C}(U_\mathrm{BE},U_\mathrm{CE})$。红色：$U_\mathrm{CE}=6$ V 处的截面，呈指数型。绿色：$U_\mathrm{BE}=0.6$ V 处的截面，先陡后几乎水平。两者在工作点相交。
:::

:::satz 定理 3.1 (模型曲面)
<span class="anker" id="satz-3-1"></span>

当 $U_\mathrm{BE}\gg U_T$ 且 $U_\mathrm{CE}\ge0$ 时，参考模型给出

<span class="anker" id="gl-3-1"></span>
$$I_\mathrm{C}=\underbrace{I_\mathrm{S}\,\mathrm{e}^{U_\mathrm{BE}/U_T}}_{\text{注入}}\cdot\underbrace{\bigl(1-\mathrm{e}^{-U_\mathrm{CE}/U_T}\bigr)}_{\text{收集}}\cdot\underbrace{\Bigl(1+\frac{U_\mathrm{CE}-6\,\mathrm{V}}{80\,\mathrm{V}}\Bigr)}_{\text{微小斜率}},\qquad I_\mathrm{B}=\frac{I_\mathrm{S}}{B}\,\mathrm{e}^{U_\mathrm{BE}/U_T}. \tag{3.1}$$
:::

⁠**如何理解：**第一个因子就是式 [(2.1)](warum-strom-durch-die-gesperrte-diode-fliet.html#gl-2-1)。一旦集电极比发射极高出几个 $U_T$，第二个因子就趋于 1：它计量集电极送回多少电子，在 $U_\mathrm{CE}=0.05$ V 时为 15 %，0.1 V 时还有 2 %，0.2 V 时只有 0.05 %。第三个因子描述随 $U_\mathrm{CE}$ 的轻微增长（第 [9](tangente-statt-kurve.html#stufe-9) 阶段）。$I_\mathrm{S}$ 和 $B$ 是 $U_\mathrm{CE}=6$ V 时的值。**适用条件：**这是适用于小电流和中等电流的模型。

:::herleitung 因子 $1-\mathrm{e}^{-U_\mathrm{CE}/U_T}$
穿过基区的电子电流与其两侧边缘之间的密度梯度成正比。每侧边缘都跟随其边界上的电压：发射极一侧为 $\mathrm{e}^{U_\mathrm{BE}/U_T}$，集电极一侧为 $\mathrm{e}^{U_\mathrm{BC}/U_T}$，其中由式 [(1.1)](drei-schichten-zwei-spannungen.html#gl-1-1) 有 $U_\mathrm{BC}=-U_\mathrm{CB}=U_\mathrm{BE}-U_\mathrm{CE}$。所以 $I_\mathrm{C}\sim\mathrm{e}^{U_\mathrm{BE}/U_T}-\mathrm{e}^{(U_\mathrm{BE}-U_\mathrm{CE})/U_T}=\mathrm{e}^{U_\mathrm{BE}/U_T}(1-\mathrm{e}^{-U_\mathrm{CE}/U_T})$。$U_\mathrm{BE}$ 的指数函数和 $U_\mathrm{CE}$ 方向的棱边是同一个差值的两面。
:::

:::abbildung et1/k10schnitte 4
式 [(3.1)](#gl-3-1) 的四个截面。左：$U_\mathrm{CE}=6$ V 时的输入特性曲线和控制特性曲线，形状相同，$I_\mathrm{B}$ 轴的刻度相差 200 倍。中：$I_\mathrm{B}=5$ 到 20 µ A 的输出特性曲线，虚线为边界 $U_\mathrm{CE}=U_\mathrm{BE}$。右：斜率为 $B$ 的电流控制特性曲线。
:::

| 特性曲线 | 固定量 | 坐标轴 | 形状及原因 |
|---|---|---|---|
| __输入特性曲线__ | $U_\mathrm{CE}$ | $I_\mathrm{B}$ 对 $U_\mathrm{BE}$ | 二极管型，拐点约在 0.6 V：BE 边界就是一个二极管 |
| __控制特性曲线__ | $U_\mathrm{CE}$ | $I_\mathrm{C}$ 对 $U_\mathrm{BE}$ | 形状相同，高 $B$ 倍：注入 |
| __电流控制特性曲线__ | $U_\mathrm{CE}$ | $I_\mathrm{C}$ 对 $I_\mathrm{B}$ | 斜率为 $B$ 的直线：指数函数被约去 |
| __输出特性曲线__ | $U_\mathrm{BE}$ 或 $I_\mathrm{B}$ | $I_\mathrm{C}$ 对 $U_\mathrm{CE}$ | 先陡后几乎平坦，像电流源：收集 |

电流控制特性曲线也称为__传输特性曲线__。电流很大时它变平，$B$ 下降：此时基区充满电子，简单的计算不再成立。图 [4](#abb-4) 中的边界 $U_\mathrm{CE}=U_\mathrm{BE}$ 就是 $U_\mathrm{CB}=0$ 的位置。在它的左边，CB 二极管已经微弱导通，但曲线要到约 0.2 V 以下才明显下弯。

::::beispiel
$U_\mathrm{CE}=6$ V 处的截面：0.582 V、0.600 V 和 0.618 V 给出 1.0 mA、2.0 mA 和 4.0 mA。$U_\mathrm{BE}=0.6$ V 处的截面：$U_\mathrm{CE}=0.05$ V；0.2 V；6 V；14 V 给出 1.58 mA；1.85 mA；2.00 mA；2.20 mA。
::::

⁠**极限情况：**当 $U_\mathrm{CE}=0$ 时，$I_\mathrm{C}=0$：基区两侧边缘一样高，没有梯度。

:::frage 那么电流到底依不依赖于 $U_\mathrm{CE}$？
依赖，但程度大不相同。到 0.2 V 为止依赖很强，之后每伏约 1 %。作为比较：$U_\mathrm{BE}$ 上的 1 mV 就有 3.9 % 的作用。“依赖”并不等于“同样强烈地依赖”。地形在两个方向上都有斜率，只是相差悬殊。
:::

:::ltspice 输出特性曲线族
⁠**绘制：**`npn`，模型名称为 `T`，发射极接地，集电极接名为 `VCE` 的 `voltage`，基极接 `current`，取 `{IB0}`，方向从地到基极。

⁠**指令：**`.model T NPN(IS=1.55e-13 BF=186 VAF=74)`，`.param IB0=10u`，`.step param IB0 list 5u 10u 15u 20u`，`.dc VCE 0 12 0.02`。这些参数在 6 V 和 27 °C 时给出 T 的数值，因为 LTspice 按 $U_\mathrm{CB}=0$ 计算 $B$ 和 $I_\mathrm{S}$。

⁠**你会看到：**`Ic(Q1)` 中有四条曲线，到 0.2 V 为止很陡，之后略有上升。当 $I_\mathrm{B}=10$ µ A 时，LTspice 显示 6 V 处为 1.996 mA，12 V 处为 2.147 mA，计算结果为 2.00 mA 和 2.15 mA。请与练习 [3](#aufg-3) 比较。
:::

:::aufgabe 练习 3 ★ 读懂截面
<span class="anker" id="aufg-3"></span>

(a) 由式 [(3.1)](#gl-3-1) 求 $U_\mathrm{BE}=0.6$ V 时 $U_\mathrm{CE}=0.1$ V 和 12 V 对应的 $I_\mathrm{C}$。你计算的是哪条特性曲线？(b) 求 $U_\mathrm{CE}=6$ V 时 $U_\mathrm{BE}=0.56$ V 和 0.62 V 对应的 $I_\mathrm{C}$。这是哪条特性曲线？(c) 预测：与 6 V 时相比，$U_\mathrm{CE}=0.05$ V 时的曲线 $I_\mathrm{C}(I_\mathrm{B})$ 是什么样子？

:::loesung
(a) $1.81$ mA 和 $2.15$ mA，这是固定 $U_\mathrm{BE}$ 的截面：输出特性曲线。 (b) 0.43 mA 和 4.32 mA，这是固定 $U_\mathrm{CE}$ 的截面：控制特性曲线。60 mV 带来 10 倍的变化。 (c) 仍是一条过原点的直线，只是更平缓。式 [(3.1)](#gl-3-1) 中的 $I_\mathrm{B}$ 与 $U_\mathrm{CE}$ 无关，另外两个因子在 $U_\mathrm{CE}$ 固定时为常数：$0.854\cdot0.926=0.79$，斜率是 158 而不是 200。
:::
:::
