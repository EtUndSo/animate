---
title: 第 2 阶段：扩展量程
pfad: 电气工程 / 第 1 学期 / 电气工程基础 / 电流与电压的测量
order: 1140300
summary: 表头的量程止于 50 µ A 和 100 mV。本阶段把它变成量程 10 mA 的电流表和量程 10 V 的电压表，并说明 R iA 和 R iV 从何而来。
tags: 分流电阻, 串联电阻
lang: zh
---

<span class="anker" id="stufe-2"></span>

:::zweck
表头的量程止于 50 µ A 和 100 mV。本阶段把它变成量程 10 mA 的电流表和量程 10 V 的电压表，并说明 $R_\mathrm{iA}$ 和 $R_\mathrm{iV}$ 从何而来。
:::

**基本思路。** 表头只能承受 50 µ A。若要显示 10 mA，其余电流必须从旁边流过：__分流电阻__（并联电阻）并联在表头上，承担 9.95 mA。若要显示 10 V，表头上只能有 100 mV：__串联电阻__承担 9.9 V（图 [2](#abb-2)）。满偏时表头感受到的情况和以前一样，只是刻度的标注变了。

:::abbildung et1/k4bereich 2
同一个表头的两种用法。左：分流电阻按 199 比 1 分流。右：串联电阻按 99 比 1 分压。
:::

:::satz 定理 2.1 (分流电阻与串联电阻)
<span class="anker" id="satz-2-1"></span>

设仪表的内阻为 $R_\text{旧}$，满量程值为 $I_\text{旧}$ 或 $U_\text{旧}$。要得到新的满量程值 $I_\text{新}$ 或 $U_\text{新}=\alpha\,U_\text{旧}$，需要

<span class="anker" id="gl-2-1"></span>
$$R_\mathrm{Shunt}=R_\text{旧}\,\frac{I_\text{旧}}{I_\text{新}-I_\text{旧}},\qquad R_\mathrm V=R_\text{旧}\,(\alpha-1). \tag{2.1}$$

新的内阻为 $R_\text{旧}\parallel R_\mathrm{Shunt}$ 或 $R_\text{旧}+R_\mathrm V$。
:::

⁠**如何理解：**$\alpha>1$ 是扩展倍数，无单位。$\parallel$ 表示并联：$R_a\parallel R_b=R_aR_b/(R_a+R_b)$。分流电阻比 $R_\text{旧}$ 小，串联电阻则比它大。**适用条件：**偏转必须与电流成正比，电阻必须精确，因为它们的误差会进入读数。

:::herleitung 分流电路与分压器
分流电阻与仪表并联，$G=1/R$ 是电导。满偏时，由分流关系得

$$\frac{I_\text{旧}}{I_\text{新}}=\frac{R_\mathrm{Shunt}}{R_\mathrm{Shunt}+R_\text{旧}}=\frac{G_\text{旧}}{G_\mathrm{Shunt}+G_\text{旧}} \quad\Rightarrow\quad R_\mathrm{Shunt}=\frac{I_\text{旧}}{I_\text{新}}\,(R_\mathrm{Shunt}+R_\text{旧}).$$

解出 $R_\mathrm{Shunt}$ 即得式 [(2.1)](#gl-2-1)。串联电阻与仪表串联。由分压关系得

$$U_\text{旧}=U_\text{新}\,\frac{R_\text{旧}}{R_\text{旧}+R_\mathrm V} \quad\Rightarrow\quad \alpha=\frac{R_\text{旧}+R_\mathrm V}{R_\text{旧}}\quad\Rightarrow\quad R_\mathrm V=R_\text{旧}\,(\alpha-1).$$
:::

**例。** 对于 10 mA：$R_\mathrm{Shunt}=2\,\mathrm{k\Omega}\cdot\frac{50\,\mu\text{A}}{9.95\,\mathrm{mA}}=10.05\,\Omega$，与 2 k$\Omega$ 并联得 $R_\mathrm{iA}=10\,\Omega$。对于 10 V：$\alpha=100$，$R_\mathrm V=2\,\mathrm{k\Omega}\cdot99=198$ k$\Omega$，所以 $R_\mathrm{iV}=200$ k$\Omega$。

⁠**简而言之：**满偏时，在任何量程下电流表上的压降都是 100 mV，流过电压表的电流都是 50 µ A。由此直接得到内阻：$R_\mathrm{iA}=100\,\mathrm{mV}/10\,\mathrm{mA}=10\,\Omega$，$R_\mathrm{iV}=10\,\mathrm{V}/50\,\mu\text{A}=200$ k$\Omega$。可见，灵敏的电流量程内阻大，高的电压量程内阻也大。50 µ A 的倒数 20 k$\Omega$/V 作为特性参数标在指针式仪表上。

⁠**极限情况：**$I_\text{新}\to I_\text{旧}$ 时 $R_\mathrm{Shunt}\to\infty$，$\alpha=1$ 时 $R_\mathrm V=0$。不扩展量程就不需要元件。

**多个量程。** 多量程仪表（具有多个量程的仪表）可以切换量程（图 [3](#abb-3)）。电流表中，每多闭合一个开关就并联上一个分流电阻；电压表中，每多断开一个开关就接入一个串联电阻。式 [(2.1)](#gl-2-1) 逐步适用：此前的整体就是仪表，其内阻称为 $R_\text{旧}$。

:::abbildung et1/k4stufen 3
逐级扩展。左：每闭合一个开关就增加一个分流电阻。右：每断开一个开关就增加一个串联电阻。
:::

:::frage 分流电阻使仪表更灵敏了吗？
不，是更不灵敏了。表头满偏仍需要 50 µ A，而分流电阻使得要达到这一点需要 10 mA。
:::

:::aufgabe 练习 2 ★★ 量程开关
<span class="anker" id="aufg-2"></span>

表头采用图 [3](#abb-3) 中的电路。(a) 求电流量程 250 µ A、1 mA、10 mA 所需的 $R_1$、$R_2$、$R_3$ 及各量程的内阻。(b) 求电压量程 1 V、10 V、100 V 所需的 $R_1$、$R_2$、$R_3$。(c) 用“简而言之”中的那句话检验这两部分。

:::loesung
(a) 逐步用式 [(2.1)](#gl-2-1)：

$$\begin{aligned} R_1&=2\,\mathrm{k\Omega}\cdot\tfrac{50}{250-50}=500\,\Omega, & R^*&=2\,\mathrm{k\Omega}\parallel500\,\Omega=400\,\Omega,\\ R_2&=400\,\Omega\cdot\tfrac{250}{1000-250}=133.3\,\Omega, & R^{**}&=400\,\Omega\parallel133.3\,\Omega=100\,\Omega,\\ R_3&=100\,\Omega\cdot\tfrac{1}{10-1}=11.11\,\Omega, & R^{***}&=100\,\Omega\parallel11.11\,\Omega=10\,\Omega. \end{aligned}$$

三个分流电阻并联得 10.05 $\Omega$，与例题中的单个分流电阻相同。

(b) 每一步 $\alpha=10$：$R_1=2\,\mathrm{k\Omega}\cdot9=18$ k$\Omega$，$R^*=20$ k$\Omega$；$R_2=20\,\mathrm{k\Omega}\cdot9=180$ k$\Omega$，$R^{**}=200$ k$\Omega$；$R_3=200\,\mathrm{k\Omega}\cdot9=1.8$ M$\Omega$，$R^{***}=2$ M$\Omega$。

(c) $250\,\mu\text{A}\cdot400\,\Omega=1\,\mathrm{mA}\cdot100\,\Omega=10\,\mathrm{mA}\cdot10\,\Omega=100$ mV。电压表：$1\,\mathrm{V}/20\,\mathrm{k\Omega}=10\,\mathrm{V}/200\,\mathrm{k\Omega}=100\,\mathrm{V}/2\,\mathrm{M\Omega}=50$ µ A。
:::
:::
