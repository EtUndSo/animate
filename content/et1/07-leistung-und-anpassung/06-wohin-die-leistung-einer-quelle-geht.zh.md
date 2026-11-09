---
title: 第 5 阶段：电源的功率去了哪里
pfad: 电气工程 / 第 1 学期 / 电气工程基础 / 功率、匹配与效率
order: 1170600
summary: 电源内部也有电阻。本阶段建立功率平衡，并定义效率。
tags: 
lang: zh
---

<span class="anker" id="stufe-5"></span>

:::zweck
电源内部也有电阻。本阶段建立功率平衡，并定义效率。
:::

**基本思路。** 在电源中，每库仑获得能量 $U_\mathrm{q}$（以焦耳计），因为化学作用把它逆着电场推向较高电位。其中一部分 $U_\mathrm{Ri}$ 在 $R_\mathrm{i}$ 中以热的形式损失，其余的 $U_\mathrm{L}$ 在负载中释放（图 [6](#abb-6)）。然后它回到起点。所有库仑都走同样的一圈，所以电压之比决定了功率中到达的比例。

:::abbildung et1/k7kreis 6
左图为接有负载的电源。右图为 $R_\mathrm{L}=16\,\Omega$ 时电荷绕行一周的电位，以 B 为参考点。电源把它抬高 9 V，$R_\mathrm{i}$ 取走 1 V，负载取走 8 V。
:::

:::definition 定义 5.1 (功率平衡与效率)
<span class="anker" id="satz-5-1"></span>

在 $I=U_\mathrm{q}/(R_\mathrm{i}+R_\mathrm{L})$ 的电路中，有

<span class="anker" id="gl-5-1"></span>
$$P_\mathrm{q}=U_\mathrm{q}\,I,\qquad P_\mathrm{v}=U_\mathrm{Ri}\,I=I^2R_\mathrm{i},\qquad P_\mathrm{L}=U_\mathrm{L}\,I=I^2R_\mathrm{L},\qquad P_\mathrm{q}=P_\mathrm{v}+P_\mathrm{L}. \tag{5.1}$$

效率是被利用的功率与电源付出的总功率之比：

<span class="anker" id="gl-5-2"></span>
$$\eta=\frac{P_\mathrm{L}}{P_\mathrm{q}}=\frac{I\,U_\mathrm{L}}{I\,U_\mathrm{q}}=\frac{U_\mathrm{L}}{U_\mathrm{q}}=\frac{R_\mathrm{L}}{R_\mathrm{L}+R_\mathrm{i}}=\frac{R_\mathrm{L}/R_\mathrm{i}}{1+R_\mathrm{L}/R_\mathrm{i}}. \tag{5.2}$$
:::

⁠**如何理解：**$P_\mathrm{q}$ 是电源产生的功率，$P_\mathrm{v}$ 是其内阻中的损耗功率，$P_\mathrm{L}$ 是有用功率。$U_\mathrm{Ri}=R_\mathrm{i}I$ 是 $R_\mathrm{i}$ 上的电压。$\eta$ 是 0 和 1 之间的纯数，只取决于比值 $R_\mathrm{L}/R_\mathrm{i}$。**适用条件：**这适用于理想电源、$R_\mathrm{i}$ 和 $R_\mathrm{L}$ 的串联。对于等效电源，内部的量并不正确（第 [7](warum-50-und-welches-ziel-gilt.html#stufe-7) 阶段）。

:::herleitung 功率平衡就是网孔定律乘以电流
网孔定律为 $U_\mathrm{q}=U_\mathrm{Ri}+U_\mathrm{L}$。乘以 $I$ 得 $P_\mathrm{q}=P_\mathrm{v}+P_\mathrm{L}$。在式 [(5.2)](#gl-5-2) 中 $I$ 被约去，因为两个电阻流过相同的电流。分压器（[第 2 部分](/wissen/zh/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/strom-widerstand-und-kirchhoff/strom-widerstand-und-kirchhoff.html)）给出 $U_\mathrm{L}=U_\mathrm{q}\,R_\mathrm{L}/(R_\mathrm{L}+R_\mathrm{i})$。
:::

::::beispiel
电池接四种负载：

| $R_\mathrm{L}$ / $\Omega$ | $I$ / A | $U_\mathrm{L}$ / V | $P_\mathrm{L}$ / W | $P_\mathrm{v}$ / W | $P_\mathrm{q}$ / W | $\eta$ |
|---|---|---|---|---|---|---|
| 0.5 | 3.6 | 1.8 | 6.48 | 25.92 | 32.4 | 20 % |
| 2 | 2.25 | 4.5 | 10.125 | 10.125 | 20.25 | 50 % |
| 8 | 0.9 | 7.2 | 6.48 | 1.62 | 8.1 | 80 % |
| 16 | 0.5 | 8 | 4 | 0.5 | 4.5 | 88.9 % |
::::

⁠**极限情况：**短路时 $R_\mathrm{L}=0$，$\eta=0$：负载保持冷态，全部功率 $P_\mathrm{q}=40.5$ W 都加热 $R_\mathrm{i}$。开路时 $R_\mathrm{L}\to\infty$，$\eta\to1$，但 $I\to0$，因而 $P_\mathrm{L}\to0$。

:::frage 效率随 $R_\mathrm{L}$ 不断升高。为什么不把负载做得任意大？
因为 $\eta$ 是一个比例，而不是一个数量。$R_\mathrm{L}$ 很大时，每库仑几乎把全部能量都释放在负载中，但几乎没有库仑到来。表中可以看出：从 8 $\Omega$ 到 16 $\Omega$，$\eta$ 升高，功率 $P_\mathrm{L}$ 下降。
:::

:::aufgabe 练习 5 ★ 建立功率平衡
<span class="anker" id="aufg-5"></span>

一个电源的 $U_\mathrm{q}=12$ V，$R_\mathrm{i}=3\,\Omega$。(a) 对 $R_\mathrm{L}=9\,\Omega$，计算式 [(5.1)](#gl-5-1) 中的所有量和 $\eta$。(b) 什么负载使 $\eta=90$ %？此时到达的功率是多少？(c) 短路时会发生什么？

:::loesung
(a) $I=12\,\mathrm{V}/12\,\Omega=1$ A，$U_\mathrm{Ri}=3$ V，$U_\mathrm{L}=9$ V，$P_\mathrm{q}=12$ W，$P_\mathrm{v}=3$ W，$P_\mathrm{L}=9$ W，$\eta=75$ %。 (b) 由 $R_\mathrm{L}/(R_\mathrm{L}+3\,\Omega)=0.9$ 得 $R_\mathrm{L}=27\,\Omega$，$I=0.4$ A，$P_\mathrm{L}=4.32$ W。 (c) $I_\mathrm{SC}=4$ A，全部 48 W 都产生在 $R_\mathrm{i}$ 中，$\eta=0$。
:::
:::
