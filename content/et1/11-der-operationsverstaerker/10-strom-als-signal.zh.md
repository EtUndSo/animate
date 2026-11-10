---
title: 第 8 阶段：以电流为信号
pfad: 电气工程 / 第 1 学期 / ET1 – 电气工程基础 1：电路分析导论 / 运算放大器
adresse: elektrotechnik/1-semester/grundlagen-der-elektrotechnik/der-operationsverstarker
knoten: 第 11 章：运算放大器
order: 1211000
summary: 到目前为止，信号都是电压。但许多信号源提供的是电流。本阶段把电流变成电压，并说明运放可以模拟负电阻。
tags: 跨阻放大器, 微分电阻, 负阻抗变换器
lang: zh
---

<span class="anker" id="stufe-8"></span>

:::zweck
到目前为止，信号都是电压。但许多信号源提供的是电流。本阶段把电流变成电压，并说明运放可以模拟负电阻。
:::

**电流变电压。** 光电二极管提供的电流几乎与其电压无关。在__跨阻放大器__中，这个电流直接流入虚地，并且必须流过 $R$（图 [10](#abb-10) 左）：

<span class="anker" id="gl-8-1"></span>
$$U_\mathrm{A}=-R\,I_\mathrm{E},\qquad r_\mathrm{in}=\frac{\Delta U_-}{\Delta I_\mathrm{E}}=\frac{R}{1+A}. \tag{8.1}$$

当 $R=1$ M$\Omega$ 时，2 µ A 变成 $-2$ V。节点只移动 $2\,\mathrm{V}/A=20$ µ V。这就是 10 $\Omega$ 的小输入电阻，一个针对变化量的值（__微分电阻__）。电源看到的几乎是短路，其内阻不起作用。

**负电阻。** 在正电压下，电阻沿参考箭头方向吸取电流（负载惯例，[第 2 章](/wissen/zh/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/strom-widerstand-und-kirchhoff/strom-widerstand-und-kirchhoff.html)）。__负阻抗变换器__（NIC）则把电流推出去（图 [10](#abb-10) 右）。接线端 1 接正输入端，从那里经一个 $R$ 到输出。从输出经一个相同的 $R$ 到负输入端，再从那里经 $R_2$ 到接地点。由 $\varphi_+=\varphi_-$ 得 $U_1=U_2$。

:::satz 定理 8.1 (NIC)
<span class="anker" id="satz-8-1"></span>

<span class="anker" id="gl-8-2"></span>
$$R_\mathrm{in}=\frac{U_1}{I_1}=-R_2. \tag{8.2}$$

只有当接线端 1 上对接地点起作用的电阻 $R_\mathrm{i}$ 小于 $R_2$ 时，规则才成立。
:::

⁠**如何理解：**$I_1$ 以流入接线端 1 为正，$U_1$ 相对接地点。$U_2$ 和 $I_2$ 属于 $R_2$。$R_\mathrm{i}$ 是接线端 1 外部所接的全部，例如并联的电源和负载。**适用条件：**$U_\mathrm{A}=U_1(1+R/R_2)$ 必须在极限之内。

:::herleitung 为什么符号翻转，规则何时成立
流过 $R_2$ 的电流为 $I_2=U_2/R_2$，没有电流流入输入端，所以它也流过下方的 $R$：输出位于 $U_\mathrm{A}=U_2+R\,I_2$。上方的 $R$ 上电压相同，电流也相同，方向是从输出到接线端 1。所以 $I_1=-I_2$，$R_\mathrm{in}=U_1/I_1=-R_2$。

这里有两条反馈，下方的 $R$ 构成负反馈，上方的 $R$ 构成正反馈。$U_\mathrm{A}$ 变化时，$\varphi_-$ 按比例 $\beta_-=R_2/(R_2+R)$ 变化，$\varphi_+$ 按 $\beta_+=R_\mathrm{i}/(R_\mathrm{i}+R)$ 变化。只有 $\beta_->\beta_+$，即 $R_\mathrm{i}<R_2$ 时，负反馈才占优。
:::

:::abbildung et1/k11nic 10
左：以电流源为输入的跨阻放大器。右：NIC，$R=10$ k$\Omega$，$R_2=5$ k$\Omega$，接线端 1 上为 1 V：输出位于 3 V，把 0.2 mA 从接线端推出。
:::

::::beispiel
取 $R=10$ k$\Omega$、$R_2=5$ k$\Omega$、$U_1=1$ V，则 $I_2=0.2$ mA，$U_\mathrm{A}=3$ V，$I_1=-0.2$ mA，即 $R_\mathrm{in}=-5$ k$\Omega$。能量来自运放的电源。**应用：**一个 1 mA、内阻 $R_\mathrm{q}=10$ k$\Omega$ 的电流源接 1 k$\Omega$ 时只输出 0.909 mA，因为一部分流过 $R_\mathrm{q}$。并联一个 $R_2=R_\mathrm{q}$ 的 NIC：电导 $1/R_\mathrm{q}-1/R_2$ 变为零，负载得到 1 mA。实际电源就像理想电源一样工作。NIC 恰好提供被 $R_\mathrm{q}$ 分走的 0.1 mA。
::::

⁠**极限情况：**没有负载时 $R_\mathrm{i}=R_\mathrm{q}=R_2$，两条反馈同样强，环路增益为零，规则不再成立。

:::aufgabe 练习 9 ★★★ 补偿电流源
<span class="anker" id="aufg-9"></span>

一个 $R=10$ k$\Omega$、$R_2=4.7$ k$\Omega$ 的 NIC 与一个 2 mA、$R_\mathrm{q}=4.7$ k$\Omega$ 的电源并联。负载为 1 k$\Omega$。(a) 没有 NIC 和有 NIC 时，负载分别得到多大电流？(b) 运放输出位于何处？(c) 负载电阻到多大时，输出的 11 V 还够用？(d) 为什么电路有负载时稳定，没有负载时不稳定？

:::loesung
(a) 没有 NIC 时 $2\,\mathrm{mA}\cdot4.7/5.7=1.65$ mA，有 NIC 时 2 mA。 (b) $U_1=2$ V，$I_2=0.426$ mA，$U_\mathrm{A}=2\,\mathrm{V}+10\,\mathrm{k\Omega}\cdot0.426\,\mathrm{mA}=6.26$ V。 (c) $U_\mathrm{A}=U_1(1+R/R_2)=3.13\,U_1\le11$ V 得 $U_1\le3.52$ V，即 $R_\mathrm{L}\le1.76$ k$\Omega$。 (d) 有负载时 $R_\mathrm{i}=R_\mathrm{q}\parallel1\,\mathrm{k\Omega}=825\,\Omega<R_2$，负反馈占优。没有负载时 $R_\mathrm{i}=R_2$，两条反馈相互抵消。
:::
:::
