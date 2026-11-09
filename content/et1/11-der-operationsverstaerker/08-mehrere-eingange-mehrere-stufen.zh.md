---
title: 第 6 阶段：多个输入，多个放大级
pfad: 电气工程 / 第 1 学期 / 电气工程基础 / 运算放大器
order: 1210800
summary: 规则原本针对一个输入和一个运放。本阶段说明，它无需新的思路就能处理多个输入和整条级联，因为所有方程都保持线性。
tags: 加法器, 减法器
lang: zh
---

<span class="anker" id="stufe-6"></span>

:::zweck
规则原本针对一个输入和一个运放。本阶段说明，它无需新的思路就能处理多个输入和整条级联，因为所有方程都保持线性。
:::

**基本思路。** 在__加法器__中，多个电阻接到负输入端（图 [8](#abb-8)）。节点保持在 0 V，所以每个电源只看到自己的电阻，驱动 $U_{\mathrm{E}i}/R_{\mathrm{E}i}$，与其他电源无关。虚地使各电源彼此解耦。所有电流合起来流过反馈电阻 $R_\mathrm{F}$。在__减法器__中，每个输入端各接一个电压。这里用[第 5 部分](/wissen/zh/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/quellen-und-ersatzquellen/quellen-und-ersatzquellen.html)的叠加：每次只算一个电源，另一个变成导线。

:::satz 定理 6.1 (加法器、减法器、级联)
<span class="anker" id="satz-6-1"></span>

<span class="anker" id="gl-6-1"></span>
$$U_\mathrm{A}=-R_\mathrm{F}\sum_i\frac{U_{\mathrm{E}i}}{R_{\mathrm{E}i}}, \tag{6.1}$$

<span class="anker" id="gl-6-2"></span>
$$U_\mathrm{A}=\frac{R_1+R_2}{R_1}\cdot\frac{R_4}{R_3+R_4}\,U_\mathrm{E2}-\frac{R_2}{R_1}\,U_\mathrm{E1}. \tag{6.2}$$

当 $R_3=R_1$、$R_4=R_2$ 时，剩下 $U_\mathrm{A}=\frac{R_2}{R_1}\,(U_\mathrm{E2}-U_\mathrm{E1})$。级联的各级相乘：$G=G_1\,G_2$。
:::

⁠**如何理解：**在 [(6.2)](#gl-6-2) 中，$U_\mathrm{E1}$ 经 $R_1$ 接负输入端，$U_\mathrm{E2}$ 接正输入端前的分压器 $R_3$、$R_4$，$R_2$ 引回反馈。**适用条件：**运放处于线性范围。叠加时只有总和必须在极限之内，分项结果只是计算量。

:::herleitung 用叠加法求减法器
当 $U_\mathrm{E2}=0$ 时，$R_3$、$R_4$ 中没有电流，正输入端位于 0 V。这就是反相放大器：$U_\mathrm{A1}=-(R_2/R_1)\,U_\mathrm{E1}$。当 $U_\mathrm{E1}=0$ 时，电源变成导线，所以 $R_1$ 仍然接地，不能略去，因为输出经 $R_2$ 驱动电流流过它。这就是同相放大器，$\varphi_+=U_\mathrm{E2}\,R_4/(R_3+R_4)$：$U_\mathrm{A2}=\bigl(1+R_2/R_1\bigr)\varphi_+$。两者之和即 [(6.2)](#gl-6-2)。
:::

:::abbildung et1/k11addsub 8
左：加法器：三个电源的电流在节点汇合，流过 $R_\mathrm{F}$。右：减法器，$R_1=R_3$，$R_2=R_4$：在 2.00 V 和 2.05 V 时，两个输入端都位于 1.64 V。
:::

::::beispiel
⁠**加法器**，$R_\mathrm{F}=40$ k$\Omega$，$R_\mathrm{E1}=R_\mathrm{E2}=10$ k$\Omega$，$R_\mathrm{E3}=20$ k$\Omega$，输入 $0.5$ V、$-0.2$ V、$0.1$ V：电流为 50、$-20$ 和 5 µ A，合计 35 µ A，所以 $U_\mathrm{A}=-1.4$ V。**减法器**，$R_1=R_3=10$ k$\Omega$，$R_2=R_4=40$ k$\Omega$，$U_\mathrm{E1}=2.00$ V，$U_\mathrm{E2}=2.05$ V：$\varphi_+=0.8\cdot2.05\,\mathrm{V}=1.64$ V。流过 $R_1$ 的电流为 $(2.00-1.64)\,\mathrm{V}/10\,\mathrm{k\Omega}=36$ µ A，所以 $U_\mathrm{A}=1.64\,\mathrm{V}-36\,\mu\text{A}\cdot40\,\mathrm{k\Omega}=0.2$ V。叠加得 $-8.0\,\mathrm{V}+8.2\,\mathrm{V}$，结果相同。约 2 V 的共模不见了。**级联**，两个反相放大器，$G_1=-4$，$G_2=-2$：0.5 V 变成 $-2$ V，再变成 $+4$ V，所以 $G=+8$。
::::

⁠**极限情况：**$U_\mathrm{E1}=U_\mathrm{E2}$ 时结果为 0。

**较大电路的步骤。** 先确定输入端的电位，再从左到右逐级计算。在级联中，每个输出都是下一级的输入，是一个具有固定值的电位。

:::frage 在第 6 部分，级联的二端口网络会相互加载。为什么这里可以直接相乘？
因为第一级的输出电阻几乎为零。第二级的 10 k$\Omega$ 加在 3.75 m$\Omega$ 上，电压损失只是原值的 $4\cdot10^{-7}$。第一级的环路把它补偿了。
:::

:::aufgabe 练习 6 ★★★ 加法器与不相等的电阻
<span class="anker" id="aufg-6"></span>

(a) 一个加法器的 $R_\mathrm{F}=20$ k$\Omega$，输入电阻为 10、20 和 5 k$\Omega$。输入 1 V、$-2$ V 和 0.5 V 时 $U_\mathrm{A}$ 多大？(b) 在例中的减法器上，$R_4$ 偏大 1 %（40.4 k$\Omega$）。计算 $U_\mathrm{E2}$ 和 $U_\mathrm{E1}$ 前的系数。(c) $U_\mathrm{E1}=U_\mathrm{E2}=2$ V 时产生多大的输出电压？(d) 现在输入 2.00 V 和 2.05 V 时 $U_\mathrm{A}$ 是多少？为什么减法器必须用公差很小的电阻？

:::loesung
(a) $U_\mathrm{A}=-(2\cdot1+1\cdot(-2)+4\cdot0.5)\,\mathrm{V}=-2$ V。 (b) $U_\mathrm{E2}$ 前：$5\cdot40.4/50.4=4.0079$，$U_\mathrm{E1}$ 前：4。 (c) $2\,\mathrm{V}\cdot0.0079=15.9$ mV，而不是 0。 (d) $4.0079\cdot2.05\,\mathrm{V}-8\,\mathrm{V}=0.216$ V，而不是 0.200 V。这 8 % 的误差几乎全部来自共模。偏差 1 % 的电阻使抑制只有 $4/0.0079$，即 54 dB，比运放本身还差。
:::
:::
