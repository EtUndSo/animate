---
title: 第 7 阶段：负反馈稳定工作点
pfad: 电气工程 / 第 1 学期 / 电气工程基础 / 双极型晶体管
order: 1200900
summary: 第 5 阶段的工作点依赖于 B 和 U BE ，而这两者都不可靠。本阶段说明电路如何自己把电流稳定住。
tags: 电流负反馈, 电压负反馈
lang: zh
---

<span class="anker" id="stufe-7"></span>

:::zweck
第 [5](der-arbeitspunkt.html#stufe-5) 阶段的工作点依赖于 $B$ 和 $U_\mathrm{BE}$，而这两者都不可靠。本阶段说明电路如何自己把电流稳定住。
:::

**基本思路。** 在参考模型中，$I_\mathrm{C}=B\cdot10$ µ A。$B=100$ 的个体通过 1 mA（$U_\mathrm{CE}=9$ V），$B=400$ 的个体则进入饱和。固定的电压 $U_\mathrm{BE}$ 更糟：电流固定时，$U_\mathrm{BE}$ 每开尔文下降约 2 mV，而 18 mV 就使电流加倍，所以只要升温 9 K，$I_\mathrm{C}$ 就加倍。

解决办法是在发射极接一个电阻。分压器使基极电位几乎固定。这时电流在一个环路中与自身对抗：

$I_\mathrm{C}$ 上升 $\to$ $R_\mathrm{E}$ 上的电压上升 $\to$ $\varphi_\mathrm{E}$ 上升 $\to$ $U_\mathrm{BE}=\varphi_\mathrm{B}-\varphi_\mathrm{E}$ 下降 $\to$ 注入减少 $\to$ $I_\mathrm{C}$ 下降。

结果削弱了原因：这就是负反馈，这里称为__电流负反馈__，因为流过 $R_\mathrm{E}$ 的电流产生了反向电压。最终 $U_\mathrm{BE}$ 只变化几毫伏，电流由 $R_\mathrm{E}$ 上的欧姆定律决定，而不再由指数函数决定。第二种形式把 $R_\mathrm{B}$ 接到集电极（图 [8](#abb-8) 中部）。$I_\mathrm{C}$ 上升时，$U_\mathrm{CE}$ 下降，$I_\mathrm{B}=(U_\mathrm{CE}-U_\mathrm{BE})/R_\mathrm{B}$ 也随之下降。这就是__电压负反馈__。

:::abbildung et1/k10gegenkopplung 8
左：带基极分压器的电流负反馈。中：电压负反馈。右：参考模型中 $I_\mathrm{C}$ 随 $B$ 的变化。没有负反馈时，电流与 $B$ 成正比增长，直到饱和（灰色）。电流负反馈（蓝色）几乎保持平坦，电压负反馈（橙色）介于两者之间。
:::

:::satz 定理 7.1 (带负反馈的工作点)
<span class="anker" id="satz-7-1"></span>

带分压器 $R_1$、$R_2$ 的电流负反馈，$R_\mathrm{i}=R_1\parallel R_2$：

<span class="anker" id="gl-7-1"></span>
$$U_\mathrm{q}=U_\mathrm{CC}\frac{R_2}{R_1+R_2},\quad I_\mathrm{B}=\frac{U_\mathrm{q}-U_\mathrm{BE}}{(1+B)R_\mathrm{E}+R_\mathrm{i}},\quad I_\mathrm{C}=\frac{U_\mathrm{q}-U_\mathrm{BE}}{R_\mathrm{E}\bigl(1+\frac1B\bigr)+\frac{R_\mathrm{i}}{B}}. \tag{7.1}$$

当 $R_\mathrm{E}\gg R_\mathrm{i}/B$ 且 $B\gg1$ 时，$I_\mathrm{C}\approx(U_\mathrm{q}-U_\mathrm{BE})/R_\mathrm{E}$；若还有 $U_\mathrm{q}\gg U_\mathrm{BE}$，则 $I_\mathrm{C}\approx U_\mathrm{CC}R_2/\bigl(R_\mathrm{E}(R_1+R_2)\bigr)$。

$R_\mathrm{B}$ 从集电极接到基极的电压负反馈：

<span class="anker" id="gl-7-2"></span>
$$I_\mathrm{C}=\frac{U_\mathrm{CC}-U_\mathrm{BE}}{R_\mathrm{C}\bigl(1+\frac1B\bigr)+\frac{R_\mathrm{B}}{B}}\approx\frac{U_\mathrm{CC}-U_\mathrm{BE}}{R_\mathrm{C}+\frac{R_\mathrm{B}}{B}},\qquad\text{当 } R_\mathrm{C}\gg\frac{R_\mathrm{B}}{B}\text{ 时：}\ I_\mathrm{C}\approx\frac{U_\mathrm{CC}-U_\mathrm{BE}}{R_\mathrm{C}}. \tag{7.2}$$
:::

⁠**如何理解：**$U_\mathrm{q}$ 和 $R_\mathrm{i}$ 把分压器描述为等效电压源（[第 5 部分](/wissen/zh/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/quellen-und-ersatzquellen/quellen-und-ersatzquellen.html)）：$U_\mathrm{q}$ 是它的开路电压，$R_\mathrm{i}$ 是它的内阻。在分母中，$R_\mathrm{E}$ 几乎完全起作用，$R_\mathrm{i}$ 则要除以 $B$。**适用条件：**放大区。这一点要在最后检验。这里 $U_\mathrm{BE}$ 是固定值；式 [(7.1)](#gl-7-1) 的最后一个近似要求 $U_\mathrm{q}$ 足够大。

:::herleitung 由网孔得出公式
分压器变成电源 $U_\mathrm{q}$ 串联 $R_\mathrm{i}$。利用 $I_\mathrm{E}=(1+B)I_\mathrm{B}$，经过基极和发射极的网孔方程为

$$U_\mathrm{q}=I_\mathrm{B}R_\mathrm{i}+U_\mathrm{BE}+I_\mathrm{B}(1+B)R_\mathrm{E}.$$

解出 $I_\mathrm{B}$ 并乘以 $B$，即得式 [(7.1)](#gl-7-1)。对电压负反馈，流过 $R_\mathrm{C}$ 的电流为 $I_\mathrm{C}+I_\mathrm{B}$，流过 $R_\mathrm{B}$ 的只有 $I_\mathrm{B}$。利用 $I_\mathrm{B}=I_\mathrm{C}/B$，网孔方程为

$$U_\mathrm{CC}-U_\mathrm{BE}=\Bigl(\frac{I_\mathrm{C}}{B}+I_\mathrm{C}\Bigr)R_\mathrm{C}+\frac{I_\mathrm{C}}{B}R_\mathrm{B}.$$

解出 $I_\mathrm{C}$，即得式 [(7.2)](#gl-7-2)。
:::

::::beispiel
参考模型：$U_\mathrm{q}=2.7$ V，$R_\mathrm{i}=6.98$ k$\Omega$，$R_\mathrm{i}/B=35\,\Omega\ll1$ k$\Omega$。于是 $I_\mathrm{C}=2.1\,\mathrm{V}/1040\,\Omega=2.02$ mA，$U_\mathrm{CE}=12\,\mathrm{V}-6.06\,\mathrm{V}-2.03\,\mathrm{V}=3.91$ V，处于放大区。基极电位为 2.63 V，分压器的电流为 300 µ A，是 $I_\mathrm{B}$ 的 30 倍。

| $I_\mathrm{C}$ | $B=100$ | $B=200$ | $B=400$ |
|---|---|---|---|
| 无负反馈（$I_\mathrm{B}=10$ µ A） | 1 mA | 2 mA | 3.93 mA（饱和） |
| 电压负反馈（$R_\mathrm{B}=540$ k$\Omega$） | 1.35 mA | 1.99 mA | 2.62 mA |
| 电流负反馈 | 1.94 mA | 2.02 mA | 2.06 mA |

温度的影响也几乎消失了：升温 50 K 使 $U_\mathrm{BE}$ 降低 0.1 V，由式 [(7.1)](#gl-7-1)，$I_\mathrm{C}$ 只上升 4.8 %。若电压 $U_\mathrm{BE}$ 固定，电流将变为 47 倍。电压负反馈的效果较差，因为这里 $R_\mathrm{B}/B=2.7$ k$\Omega$ 相对于 3 k$\Omega$ 并不小。取 $R_\mathrm{B}=100$ k$\Omega$ 时，$I_\mathrm{C}$ 只在 2.83 mA 和 3.50 mA 之间变化，但这时只剩下 $U_\mathrm{CE}=2.2$ V。
::::

⁠**极限情况：**$R_\mathrm{E}\to0$ 给出 $I_\mathrm{C}=B(U_\mathrm{q}-U_\mathrm{BE})/R_\mathrm{i}$，即第 [5](der-arbeitspunkt.html#stufe-5) 阶段带基极电阻的公式。$B\to\infty$ 给出 $I_\mathrm{C}=(U_\mathrm{q}-U_\mathrm{BE})/R_\mathrm{E}$。

:::frage 发射极电阻的代价是什么？
有两点。$R_\mathrm{E}$ 上的电压（这里是 2 V）使集电极少了这部分信号摆幅。而且负反馈对信号同样起作用：电压增益大幅下降（第 [10](drei-grundschaltungen.html#stufe-10) 阶段）。与 $R_\mathrm{E}$ 并联一个电容器，对交流信号相当于一根导线，就消除了第二个缺点。
:::

:::ltspice $I_\mathrm{C}$ 几乎与 $B$ 无关
⁠**绘制：**`voltage` `VCC` 取 12，接网络 `cc`。分压器：`res` 31k 从 `cc` 接到 `b`，9k 从 `b` 接地。`npn` 取模型 `T`，`res` 3k 从 `cc` 接到集电极，`res` 1k 从发射极接地。

⁠**指令：**`.model T NPN(IS=1.55e-13 BF={BF} VAF=74)`，`.param BF=186`，`.step param BF list 93 186 372`，`.dc VCC 0 12 0.1`，`.meas dc ic FIND Ic(Q1) AT=12`。这三个值对应 6 V 时的 $B=100$、200、400。

⁠**你会看到：**三条几乎重合的曲线。在 12 V 处，LTspice 给出 1.94 mA；2.02 mA；2.06 mA，与计算完全一致。填入练习 [8](#aufg-8) 的数值，检验你的离散性。
:::

:::aufgabe 练习 8 ★★★ 设计工作点
<span class="anker" id="aufg-8"></span>

用 T 设计一个电流负反馈电路，要求 $U_\mathrm{CC}=15$ V，$I_\mathrm{C}=1$ mA，$R_\mathrm{E}$ 上的电压为 2 V，$U_\mathrm{CE}=6$ V。 (a) 求 $R_\mathrm{E}$ 和 $R_\mathrm{C}$，取整数值。(b) 流过 $R_2$ 的电流应为 $10\,I_\mathrm{B}$。求 $R_2$ 和 $R_1$（取整为 52 k$\Omega$ 和 225 k$\Omega$）。(c) 计算 $B=100$、200、400 时的 $I_\mathrm{C}$，并与表中的电路比较。为什么离散性更大？请在计算之前先预测结果。

:::loesung
(a) $R_\mathrm{E}=2\,\mathrm{V}/1\,\mathrm{mA}=2$ k$\Omega$，$R_\mathrm{C}=(15-6-2)\,\mathrm{V}/1\,\mathrm{mA}=7$ k$\Omega$。

(b) $I_\mathrm{B}=5$ µ A，基极电位为 2.6 V。$R_2=2.6\,\mathrm{V}/50\,\mu\text{A}=52$ k$\Omega$。流过 $R_1$ 的电流为 55 µ A：$R_1=12.4\,\mathrm{V}/55\,\mu\text{A}=225$ k$\Omega$。

(c) $U_\mathrm{q}=2.82$ V，$R_\mathrm{i}=42.2$ k$\Omega$。由式 [(7.1)](#gl-7-1) 得 $I_\mathrm{C}=0.91$ mA；1.00 mA；1.05 mA。预测：离散性更大，因为 $R_\mathrm{i}/B=211\,\Omega$ 相对于 $R_\mathrm{E}$ 不再很小。这里分压器的电流只有 $I_\mathrm{B}$ 的十倍，而不是三十倍。LTspice：0.92 mA；1.01 mA；1.06 mA。
:::
:::

:::aufgabe 练习 9 ★★ 电压负反馈
<span class="anker" id="aufg-9"></span>

取例题中的电压负反馈电路。(a) 验算 $B=200$ 时的 $I_\mathrm{C}$ 和 $U_\mathrm{CE}$。(b) 极限情况 $R_\mathrm{B}\to0$：$U_\mathrm{CE}$ 和 $I_\mathrm{C}$ 是多少？这时晶体管处于放大区吗？用式 [(4.3)](drei-bereiche-drei-ersatzschaltbilder.html#gl-4-3) 和 $U_\mathrm{CB}$ 的含义回答。

:::loesung
(a) $I_\mathrm{C}=11.4\,\mathrm{V}/(3015\,\Omega+2700\,\Omega)=1.99$ mA，$U_\mathrm{CE}=12\,\mathrm{V}-3\,\text{k}\Omega\cdot2.005\,\mathrm{mA}=5.99$ V。

(b) 基极与集电极相连：$U_\mathrm{CE}=U_\mathrm{BE}=0.6$ V，$I_\mathrm{C}=11.4\,\mathrm{V}/3015\,\Omega=3.78$ mA。由于 $U_\mathrm{CE}>0.2$ V，晶体管处于放大区，正好在 $U_\mathrm{CB}=0$ 这条线上。这就是电流镜中的 T1。
:::
:::
