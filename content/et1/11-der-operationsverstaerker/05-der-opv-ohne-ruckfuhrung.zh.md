---
title: 第 3 阶段：没有反馈的运放
pfad: 电气工程 / 第 1 学期 / 电气工程基础 / 运算放大器
order: 1210500
summary: 各放大级组合成一个只有几个引脚的器件。本阶段确定它的模型，并说明它在没有外部电路时做什么：比较。
tags: 饱和, 理想运放, 闪速转换器
lang: zh
---

<span class="anker" id="stufe-3"></span>

:::zweck
各放大级组合成一个只有几个引脚的器件。本阶段确定它的模型，并说明它在没有外部电路时做什么：比较。
:::

**基本思路。** 运放有两个输入端、一个输出端和两个电源端 $U_\mathrm{B+}$、$U_\mathrm{B-}$（图 [3](#abb-3)）。它没有接地端：输出以电源的中点为参考。每个输出电流都来自电源端，而电路图中通常省略电源端。因此，看得见的三个引脚并不满足节点定律。

输出等于 $A$ 乘以 $U_\mathrm{D}$，但只到其极限为止。在 $\pm11$ V 和 $A=100000$ 时，线性段在 $\pm110$ µ V 处就结束了。任何更大的差值都会把输出推到极限，即__饱和__。

:::definition 定义 3.1 (运放模型)
<span class="anker" id="satz-3-1"></span>

<span class="anker" id="gl-3-1"></span>
$$U_\mathrm{D}=\varphi_+-\varphi_-,\qquad U_\mathrm{A}=\begin{cases}U_\mathrm{A,max}&\text{当 }A\,U_\mathrm{D}\ge U_\mathrm{A,max},\\A\,U_\mathrm{D}&\text{介于两者之间},\\U_\mathrm{A,min}&\text{当 }A\,U_\mathrm{D}\le U_\mathrm{A,min}.\end{cases} \tag{3.1}$$

__理想运放__具有 $r_\mathrm{e}\to\infty$（无输入电流）、所有频率下 $A\to\infty$、$r_\mathrm{a}=0$（输出电流自动调整，使所有节点方程和网孔方程都成立），且没有噪声。
:::

⁠**如何理解：**$U_\mathrm{A,max}<U_\mathrm{B+}$，$U_\mathrm{A,min}>U_\mathrm{B-}$，因为输出与电源之间有晶体管，其上有压降，这里各为 1 V。**适用条件：**模型是静态的，输出的惯性见第 [4](gegenkopplung.html#stufe-4) 阶段。

:::abbildung et1/k11opv 3
左：带电源引脚的电路符号。右：参考模型中的特性曲线。斜率为 $A$，线性段只有 $\pm110$ µ V 宽。注意坐标轴：若以伏特为刻度，它就是一个竖直的台阶。
:::

**比较器。** 没有反馈时，$|U_\mathrm{D}|$ 几乎总是大于窗口。这时运放只报告哪个输入端更高：$\varphi_+>\varphi_-$ 时为 $U_\mathrm{A,max}$，$\varphi_+<\varphi_-$ 时为 $U_\mathrm{A,min}$。这就是比较器。一个应用是__闪速转换器__，一种模数转换器（图 [4](#abb-4)）。分压器产生比较电压，每个比较器把 $U_\mathrm{E}$ 与其中一个相比较。所有比较器同时工作，因此得名（flash，闪光）。$n$ 位需要 $2^n-1$ 个比较器，8 位即 255 个。

:::abbildung et1/k11flash 4
2 位闪速转换器，$U_\mathrm{Ref}=6$ V，电阻相同。输入端不取电流，电阻串联，抽头位于 6、4 和 2 V。当 $U_\mathrm{E}=3.2$ V 时，只有 K3 切换到高电平。
:::

**例。** 当 $U_\mathrm{E}=3.2$ V 时，K1 处 $U_\mathrm{D}=-2.8$ V，K2 处 $-0.8$ V，K3 处 $+1.2$ V。K1 和 K2 位于 $-11$ V，K3 位于 $+11$ V。三个输出区分四个范围：2 V 以下、2 到 4 V、4 到 6 V、6 V 以上。**极限情况：**当 $A\to\infty$ 时，窗口缩为一点，特性曲线成为 $U_\mathrm{D}=0$ 处的台阶。

:::aufgabe 练习 3 ★ 比较器
<span class="anker" id="aufg-3"></span>

(a) 一个如图 [4](#abb-4) 的闪速转换器，$U_\mathrm{Ref}=9$ V。抽头在哪里？$U_\mathrm{E}=4$ V 时哪些比较器为高？(b) 3 位需要多少个比较器？(c) 运放 V 上先后加 $U_\mathrm{D}=50$ µ V 和 300 µ V。$U_\mathrm{A}$ 各为多少？

:::loesung
(a) 9、6 和 3 V。在 4 V 时只有 K3 上 $U_\mathrm{D}>0$（$+1$ V），K1 和 K2 上为 $-5$ V 和 $-2$ V。 (b) $2^3-1=7$。 (c) 5 V 在窗口内。300 µ V 时将是 30 V，输出位于 11 V。
:::
:::
