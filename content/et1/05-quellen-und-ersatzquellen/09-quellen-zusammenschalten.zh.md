---
title: 第 7 阶段：电源的组合
pfad: 电气工程 / 第 1 学期 / 电气工程基础 / 电源与等效电源
order: 1150900
summary: 一个电源往往不够。串联提高电压，并联提高电流。本阶段计算这两种情况，并指出其中的危险。
tags: 环流
lang: zh
---

<span class="anker" id="stufe-7"></span>

:::zweck
一个电源往往不够。串联提高电压，并联提高电流。本阶段计算这两种情况，并指出其中的危险。
:::

**基本思路。** 串联时，流过两个电源的电流相同，在任何电流下它们的端电压都相加。并联时，两者电压相同，在任何电压下它们的电流都相加。因此串联用电压源形式计算，并联用电流源形式计算。两条直线又合成一条直线，也就是又得到一个实际电源。

:::satz 定理 7.1 (实际电源的组合)
<span class="anker" id="satz-7-1"></span>

两个电源串联或并联时，分别相当于一个电源：

<span class="anker" id="gl-7-1"></span>
$$U_\mathrm{eq}=U_\mathrm{q1}+U_\mathrm{q2},\quad R_\mathrm{eq}=R_\mathrm{q1}+R_\mathrm{q2} \qquad\text{或}\qquad I_\mathrm{eq}=I_\mathrm{q1}+I_\mathrm{q2},\quad G_\mathrm{eq}=G_\mathrm{q1}+G_\mathrm{q2}. \tag{7.1}$$

对并联，用电压源形式表示为

<span class="anker" id="gl-7-2"></span>
$$U_\mathrm{eq}=\frac{G_\mathrm{q1}U_\mathrm{q1}+G_\mathrm{q2}U_\mathrm{q2}}{G_\mathrm{q1}+G_\mathrm{q2}},\qquad R_\mathrm{eq}=R_\mathrm{q1}\parallel R_\mathrm{q2}. \tag{7.2}$$
:::

⁠**如何理解：**式 [(7.2)](#gl-7-2) 中的电压是加权平均值，内阻较小的电源权重较大。两个相同的电源并联得 $U_\mathrm{q}$ 和 $R_\mathrm{q}/2$，串联得 $2U_\mathrm{q}$ 和 $2R_\mathrm{q}$。**适用条件：**电压源串联和电流源并联在技术上没有问题。并联的电压源需要电压相同或内阻足够大：当 $U_\mathrm{q1}\neq U_\mathrm{q2}$ 时，即使不接负载也有__环流__

<span class="anker" id="gl-7-3"></span>
$$I_\mathrm{circ}=\frac{U_\mathrm{q1}-U_\mathrm{q2}}{R_\mathrm{q1}+R_\mathrm{q2}}. \tag{7.3}$$

它从较强的电源流入较弱的电源。电压不同的两个理想电压源不得并联，电流不同的两个理想电流源不得串联：这时模型无解。

:::herleitung 用电流源形式计算并联
两个电源的电压都是 $U_\mathrm{AB}$，节点定律把它们的电流相加：$I_\mathrm{A}=(I_\mathrm{q1}-G_\mathrm{q1}U_\mathrm{AB})+(I_\mathrm{q2}-G_\mathrm{q2}U_\mathrm{AB})=(I_\mathrm{q1}+I_\mathrm{q2})-(G_\mathrm{q1}+G_\mathrm{q2})U_\mathrm{AB}$。这又是式 [(5.1)](reale-quellen-und-der-arbeitspunkt.html#gl-5-1) 的形式。结合式 [(6.1)](spannungsquelle-oder-stromquelle.html#gl-6-1) 即得式 [(7.2)](#gl-7-2)。串联时，网孔定律以同样方式把电压相加。环流等于回路电压 $U_\mathrm{q1}-U_\mathrm{q2}$ 除以回路电阻。
:::

:::abbildung et1/k5zusammen 8
左：两节相同的电池并联。右：特性曲线。并联时开路电压不变，短路电流加倍。串联时开路电压加倍，短路电流不变。圆点表示接 16 $\Omega$ 时的工作点。
:::

::::beispiel
取参考模型中的两节电池。并联：9 V，1 $\Omega$，$I_\mathrm{SC}=9$ A。用电流形式检验：$4.5+4.5=9$ A，$0.5+0.5=1$ S。串联：18 V，4 $\Omega$，$I_\mathrm{SC}=4.5$ A。接 16 $\Omega$ 时，并联输出 8.47 V 和 0.529 A，串联输出 14.4 V 和 0.9 A（图 [8](#abb-8)）。这里并联作用不大，因为 2 $\Omega$ 比 16 $\Omega$ 小得多。

如果其中一节电池放电到 8 V，根据式 [(7.3)](#gl-7-3)，开路时环流为 $1\,\mathrm{V}/4\,\Omega=0.25$ A。两个接线端都是 8.5 V，按式 [(7.2)](#gl-7-2) 也是如此。
::::

⁠**极限情况：**如果内阻各只有 10 m$\Omega$，环流将是 50 A。因此大型电池单体只有在电压相同时才并联。当 $U_\mathrm{q1}=U_\mathrm{q2}$ 时，环流消失。

:::frage 两节电池并联能提供更高的电压吗？
开路时不能，两者都提供 9 V。带负载时略高一点，因为电流分到两个内阻上，内部压降只有一半。真正的好处是短路电流加倍，电荷量也加倍。
:::

:::aufgabe 练习 8 ★★ 新旧蓄电池
<span class="anker" id="aufg-8"></span>

一块新蓄电池（12.6 V，0.1 $\Omega$）与一块旧蓄电池（11.8 V，0.3 $\Omega$）并联。(a) 环流是多少？得到什么样的等效电源？(b) 负载取用 10 A。电压是多少，每块蓄电池各提供多少？(c) 负载电流超过多大时，旧蓄电池才开始输出电流？低于此值时发生什么？

:::loesung
(a) $I_\mathrm{circ}=\frac{0.8\,\mathrm{V}}{0.4\,\Omega}=2$ A。$U_\mathrm{eq}=\frac{10\,\mathrm{S}\cdot12.6\,\mathrm{V}+3.33\,\mathrm{S}\cdot11.8\,\mathrm{V}}{13.33\,\mathrm{S}}=12.4$ V，$R_\mathrm{eq}=0.1\,\Omega\parallel0.3\,\Omega=75$ m$\Omega$。验算：$12.6\,\mathrm{V}-0.1\,\Omega\cdot2\,\mathrm{A}=12.4$ V。

(b) $U=12.4\,\mathrm{V}-75\,\mathrm{m\Omega}\cdot10\,\mathrm{A}=11.65$ V。新：$\frac{12.6-11.65}{0.1}\,\mathrm{A}=9.5$ A。旧：$\frac{11.8-11.65}{0.3}\,\mathrm{A}=0.5$ A。和为 10 A。

(c) 只有当 $U<11.8$ V，即 $I_\mathrm{L}>\frac{12.4-11.8}{0.075}\,\mathrm{A}=8$ A 时，旧蓄电池才输出电流。低于此值时，电流流入旧蓄电池，新蓄电池给它充电。
:::
:::
