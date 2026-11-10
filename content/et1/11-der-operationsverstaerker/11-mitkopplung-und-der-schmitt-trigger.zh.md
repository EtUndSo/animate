---
title: 第 9 阶段：正反馈与施密特触发器
pfad: 电气工程 / 第 1 学期 / ET1 – 电气工程基础 1：电路分析导论 / 运算放大器
adresse: elektrotechnik/1-semester/grundlagen-der-elektrotechnik/der-operationsverstarker
knoten: 第 11 章：运算放大器
order: 1211100
summary: 若把同相放大器的两个输入端对调，同样的方程给出同样的数。但电路的行为完全不同。本阶段说明规则为什么在这里失效，以及实际发生了什么。
tags: 迟滞, 施密特触发器, 不稳定
lang: zh
---

<span class="anker" id="stufe-9"></span>

:::zweck
若把同相放大器的两个输入端对调，同样的方程给出同样的数。但电路的行为完全不同。本阶段说明规则为什么在这里失效，以及实际发生了什么。
:::

**基本思路。** 现在 $U_\mathrm{E}$ 接负输入端，分压器接到正输入端（图 [11](#abb-11)）。计算式 $U_\mathrm{D}=\beta\,U_\mathrm{A}-U_\mathrm{E}$ 和 $U_\mathrm{A}=A\,U_\mathrm{D}$ 在 $U_\mathrm{E}=1$ V 时的解为 $U_\mathrm{A}=5.00025$ V。这是一个平衡，但不稳定，就像山顶上的球。向上 1 µ V 的扰动抬高正输入端，于是 $U_\mathrm{D}$ 增大，于是输出继续上升。结果加强了原因。输出一直运行到极限并停在那里。在那里规则不成立：$U_\mathrm{D}\ne0$。

在极限处，电路记住了自己的状态。输出位于 $+11$ V 时，正输入端位于 $+2.2$ V。只要 $U_\mathrm{E}$ 低于此值，就有 $U_\mathrm{D}>0$，什么都不变。$U_\mathrm{E}$ 超过 2.2 V 时，输出翻转，正输入端跳到 $-2.2$ V。这又加强了翻转。要翻转回来，$U_\mathrm{E}$ 必须降到 $-2.2$ V 以下。输出取决于历史，这称为__迟滞__。这种电路称为反相__施密特触发器__。

:::satz 定理 9.1 (施密特触发器)
<span class="anker" id="satz-9-1"></span>

令 $\beta=R_1/(R_1+R_2)$，输出翻转的条件是

<span class="anker" id="gl-9-1"></span>
$$\text{向下翻转：}U_\mathrm{E}=\beta\,U_\mathrm{A,max},\qquad\text{向上翻转：}U_\mathrm{E}=\beta\,U_\mathrm{A,min}. \tag{9.1}$$

迟滞宽度为 $\beta\,(U_\mathrm{A,max}-U_\mathrm{A,min})$。在两个阈值之间，两种状态都可能。
:::

⁠**如何理解：**一旦 $U_\mathrm{D}$ 改变符号，输出就翻转。**适用条件：**$A\beta>1$，否则正反馈不足以翻转。

:::herleitung 同一方程，不同符号
考虑第 [4](gegenkopplung.html#stufe-4) 阶段的惯性，现在有 $\tau\,\mathrm{d} U_\mathrm{A}/\mathrm{d} t=A(\beta\,U_\mathrm{A}-U_\mathrm{E})-U_\mathrm{A}=(A\beta-1)\,U_\mathrm{A}-A\,U_\mathrm{E}$。$U_\mathrm{A}$ 前面的系数现在为正。偏离平衡的量按 $\mathrm{e}^{+t/\tau_\mathrm{M}}$ 增长，$\tau_\mathrm{M}=\tau/(A\beta-1)=0.80$ µ s，与第 [4](gegenkopplung.html#stufe-4) 阶段大小相同。这样，1 µ V 的扰动在 13 µ s 内变成 11 V。如果电源没有限制，上升也没有限制，电路将是__不稳定__的。只有饱和才使它停下来。
:::

:::abbildung et1/k11schmitt 11
左：反相施密特触发器。右：参考模型中的迟滞回线，$\beta=0.2$：从左边来时在 $+2.2$ V 翻转，从右边来时在 $-2.2$ V 翻转。箭头表示运行方向。
:::

::::beispiel
阈值为 $\pm0.2\cdot11\,\mathrm{V}=\pm2.2$ V，迟滞宽 4.4 V。在 $U_\mathrm{E}=2.2$ V 翻转后不久，$U_\mathrm{D}=-2.2\,\mathrm{V}-2.2\,\mathrm{V}=-4.4$ V，远离窗口。用处：带噪声的信号缓慢穿过阈值时，会使比较器来回切换多次。在施密特触发器中，第一次翻转后阈值跳开 4.4 V，小于这一宽度的噪声不会引起第二次翻转。
::::

⁠**极限情况：**$\beta\to0$ 得到第 [3](der-opv-ohne-ruckfuhrung.html#stufe-3) 阶段的比较器。$U_\mathrm{E}=0$ 时两种状态都可能，取决于历史。

:::frage 输入端对调时，LTspice 的 `.op` 显示 5.00025 V。仿真错了吗？
没有，它回答的是另一个问题。`.op` 求解平衡方程，而这个解确实存在。平衡能否保持，要由时间过程决定。器件中总有噪声，所以输出会跑开。第 [10](wo-die-regeln-enden.html#stufe-10) 阶段的 LTspice 方框用 `.tran` 展示了这一点。
:::

:::aufgabe 练习 10 ★★ 施密特触发器
<span class="anker" id="aufg-10"></span>

(a) $R_1=10$ k$\Omega$，$R_2=90$ k$\Omega$：阈值在哪里？迟滞多宽？(b) 当 $R_1=10$ k$\Omega$ 时，选择 $R_2$ 使阈值为 $\pm1$ V。(c) 用 (a) 的电路，$U_\mathrm{E}$ 从 $-5$ V 变到 $+5$ V 再返回。画出 $U_\mathrm{A}(U_\mathrm{E})$ 的草图。(d) 0 到 5 V 的电源使输出范围为 0.5 V 到 4.5 V，$\beta=0.2$。阈值在哪里？

:::loesung
(a) $\beta=0.1$：阈值 $\pm1.1$ V，宽度 2.2 V。 (b) $\beta=1/11$，所以 $R_2=100$ k$\Omega$。 (c) 在 $-5$ V 时输出位于 $+11$ V。它保持到 $U_\mathrm{E}=+1.1$ V，跳到 $-11$ V，并保持到 $5$ V。返回时到 $-1.1$ V 才跳回。 (d) $0.2\cdot4.5\,\mathrm{V}=0.9$ V 和 $0.2\cdot0.5\,\mathrm{V}=0.1$ V。
:::
:::
