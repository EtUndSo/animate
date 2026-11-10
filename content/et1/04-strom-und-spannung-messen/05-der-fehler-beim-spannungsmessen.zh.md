---
title: 第 4 阶段：测量电压的误差
pfad: 电气工程 / 第 1 学期 / ET1 – 电气工程基础 1：电路分析导论 / 电流与电压的测量
adresse: elektrotechnik/1-semester/grundlagen-der-elektrotechnik/strom-und-spannung-messen
knoten: 第 4 章：电流与电压的测量
order: 1140500
summary: 电压表接在电路之外，但仍有电流流过它。本阶段说明，在什么情况下这会使待测电压降低。
tags: 
lang: zh
---

<span class="anker" id="stufe-4"></span>

:::zweck
电压表接在电路之外，但仍有电流流过它。本阶段说明，在什么情况下这会使待测电压降低。
:::

**基本思路。** 电压表在两个节点之间开辟了第二条电流通路。它的电流必须有来处。如果由电流源（保持自身电流不变，[第 5 章](/wissen/zh/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/quellen-und-ersatzquellen/quellen-und-ersatzquellen.html)）驱动负载电阻 $R_L$，固定的电流就要分配：流过电压表的部分从 $R_L$ 中少掉，电压下降（图 [5](#abb-5)）。相反，如果 $R_L$ 直接接在理想电压源上，附加电流由电压源提供，什么也不变。所以，只有在电流不能自由补充的地方才会产生误差。在分压器中，$R_1$ 阻碍了补充：总电流增大，$R_1$ 上的压降增大，中点电压下降。

:::abbildung et1/k4spannung 5
电压表（量程 10 V，虚线内为内阻和理想仪表）接在两个等效的电路上。两种情况下它都分走 13.6 µ A，读数从 3 V 降到 2.727 V。
:::

:::satz 定理 4.1 (电压表的误差)
<span class="anker" id="satz-4-1"></span>

在带负载 $R_L$ 的电流源 $I_\mathrm q$ 上，不接仪表时 $U_L=I_\mathrm qR_L$，接入仪表时

<span class="anker" id="gl-4-1"></span>
$$U_L'=I_\mathrm q\,(R_L\parallel R_\mathrm i)=U_L\cdot\frac{1}{1+R_L/R_\mathrm i}. \tag{4.1}$$

相对误差为 $f=-R_L/(R_L+R_\mathrm i)$，所以 $R_L\ll R_\mathrm i$ 时 $f\approx-R_L/R_\mathrm i$。在分压器上同样成立，其中 $R_L=R_1\parallel R_2$。
:::

⁠**如何理解：**这个分数是误差因子。$R_L$ 是仪表在其接线端之间看到的电阻。要使误差小，需要 $R_\mathrm i\gg R_L$，理想情况是 $R_\mathrm i\to\infty$。**适用条件：**理想电源，电阻与电压无关。

:::herleitung 误差因子
由基尔霍夫电流定律 $I_\mathrm q=I_{RL}'+I_{\mathrm{i}}$，电流分配到两个并联电阻上，两者的电压都是 $U_L'$。所以 $U_L'=I_\mathrm q\,R_LR_\mathrm i/(R_L+R_\mathrm i)$，约去 $R_\mathrm i$ 即得式 [(4.1)](#gl-4-1)。在分压器上，不接仪表时 $U_2=U\,R_2/(R_1+R_2)$。接入仪表时，要用 $R_2\parallel R_\mathrm i$ 代替 $R_2$（带负载的分压器，[第 2 章](/wissen/zh/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/strom-widerstand-und-kirchhoff/strom-widerstand-und-kirchhoff.html)）：

$$U_2'=U\,\frac{R_2R_\mathrm i}{R_1R_2+R_\mathrm i(R_1+R_2)} \quad\Rightarrow\quad \frac{U_2'}{U_2}=\frac{R_\mathrm i(R_1+R_2)}{R_1R_2+R_\mathrm i(R_1+R_2)}=\frac{1}{1+(R_1\parallel R_2)/R_\mathrm i}.$$
:::

::::beispiel
在分压器上，$R_1\parallel R_2=20$ k$\Omega$，$R_L/R_\mathrm i=0.1$。读数为 $3\,\mathrm{V}/1.1=2.727$ V，所以 $f=-9.1\,\%$。用数字看这一机理：流过 $R_1$ 的电流从 100 µ A 升到 104.5 µ A，其中 90.9 µ A 流过 $R_2$，13.6 µ A 流过电压表。$I_\mathrm q=150$ µ A 加在 $R_L=20$ k$\Omega$ 上得到同样的值。内阻 10 M$\Omega$ 的数字万用表显示 2.994 V，所以 $f=-0.2\,\%$。
::::

⁠**极限情况：**$R_\mathrm i\to\infty$ 得 $f\to0$。$R_L\to0$（电源直接接在仪表上）同样得 $f\to0$。$R_\mathrm i=R_L$ 时电压减半。

:::frage 200 k$\Omega$ 听起来很大。为什么仪表还是会干扰分压器？
大或小只有与 $R_L$ 相比才有意义。分压器中只有 100 µ A。与此相比，13.6 µ A 不是一个小份额。
:::

:::aufgabe 练习 4 ★★ 高阻分压器
<span class="anker" id="aufg-4"></span>

$R_1=6$ M$\Omega$ 和 $R_2=3$ M$\Omega$ 接在 9 V 上。(a) 内阻 200 k$\Omega$ 的电压表和内阻 10 M$\Omega$ 的数字万用表在 $R_2$ 上分别显示多少？(b) 如何从读数 2.5 V 求回真值？(c) 要使误差为 1 %，需要多大的 $R_\mathrm i$？

:::loesung
(a) $R_L=6\,\mathrm{M\Omega}\parallel3\,\mathrm{M\Omega}=2$ M$\Omega$，真值为 3 V。用 200 k$\Omega$：$3\,\mathrm{V}/(1+10)=0.273$ V，$f=-91\,\%$。用 10 M$\Omega$：$3\,\mathrm{V}/(1+0.2)=2.5$ V，$f=-16.7\,\%$。

(b) 变换式 [(4.1)](#gl-4-1)：$U=U'(1+R_L/R_\mathrm i)=2.5\,\mathrm{V}\cdot1.2=3$ V。(c) $R_L/(R_L+R_\mathrm i)\le0.01$ 得 $R_\mathrm i\ge99\,R_L=198$ M$\Omega$。
:::
:::
