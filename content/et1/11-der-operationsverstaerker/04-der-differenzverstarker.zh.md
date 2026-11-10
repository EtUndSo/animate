---
title: 第 2 阶段：差分放大器
pfad: 电气工程 / 第 1 学期 / ET1 – 电气工程基础 1：电路分析导论 / 运算放大器
adresse: elektrotechnik/1-semester/grundlagen-der-elektrotechnik/der-operationsverstarker
knoten: 第 11 章：运算放大器
order: 1210400
summary: 两条线路上相同的干扰应当消失，而它们之间的差值应被放大。为此需要一种输出只取决于两个电压之差的电路。
tags: 共模电压, 同相输入端, 反相输入端
lang: zh
---

<span class="anker" id="stufe-2"></span>

:::zweck
两条线路上相同的干扰应当消失，而它们之间的差值应被放大。为此需要一种输出只取决于两个电压之差的电路。
:::

**基本思路。** 两个相同的晶体管 T1 和 T2 的发射极接在公共节点 E 上（图 [2](#abb-2)）。下面是 T3。它的基极接固定电压 $U_\mathrm{bias}$，因此起电流源的作用（[第 10 章](/wissen/zh/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/der-bipolartransistor/der-bipolartransistor.html)），从节点抽走固定电流 $I_0$。基极电流很小，所以 $I_\mathrm{C1}+I_\mathrm{C2}=I_0$。总和固定，只有分配能变化。

若两个基极升高相同的量，E 随之升高，因为 T3 使电流固定，从而 $U_\mathrm{BE}$ 也固定。什么都不变。这个公共部分称为__共模电压__，$U_\mathrm{cm}=(\varphi_++\varphi_-)/2$。若只有 T2 的基极升高，T2 就多取电流。T1 恰好少得这么多。右侧集电极电阻上的压降增大，左侧的减小，两个集电极之间的电压随之偏转。

:::abbildung et1/k11diff 2
左：差分放大器，$I_0=2$ mA，$R_\mathrm{C}=3$ k$\Omega$。T3 使总和固定。右：电流分配：在 $U_\mathrm{D}=0$ 附近，每条支路流过 1 mA；在 100 mV 时，97.9 % 流过 T2。
:::

:::satz 定理 2.1 (差分放大器)
<span class="anker" id="satz-2-1"></span>

T1 的基极接输入 $\varphi_-$，T2 的基极接输入 $\varphi_+$。令 $U_\mathrm{D}=\varphi_+-\varphi_-$，$U_\mathrm{A}=U_\mathrm{a1}-U_\mathrm{a2}$，则

<span class="anker" id="gl-2-1"></span>
$$I_\mathrm{C2}=\frac{I_0}{1+\mathrm{e}^{-U_\mathrm{D}/U_T}},\qquad I_\mathrm{C1}=\frac{I_0}{1+\mathrm{e}^{U_\mathrm{D}/U_T}},\qquad U_\mathrm{A}=R_\mathrm{C}\,(I_\mathrm{C2}-I_\mathrm{C1}). \tag{2.1}$$

当 $|U_\mathrm{D}|\ll U_T$ 时，这是一条直线：

<span class="anker" id="gl-2-2"></span>
$$U_\mathrm{A}=A_\mathrm{D}\,U_\mathrm{D},\qquad A_\mathrm{D}=S\,R_\mathrm{C}=\frac{I_0\,R_\mathrm{C}}{2\,U_T}=\frac{U_{R_\mathrm{C}}}{U_T}. \tag{2.2}$$
:::

⁠**如何理解：**$S=I_\mathrm{C}/U_T$ 是单个晶体管在 $I_\mathrm{C}=I_0/2$ 时的跨导。$U_{R_\mathrm{C}}=I_0R_\mathrm{C}/2$ 是一个集电极电阻上的静态电压。$\varphi_+$ 称为__同相输入端__，因为输出与它同向变化；$\varphi_-$ 称为__反相输入端__。**适用条件：**晶体管相同，都处于放大区，基极电流远小于 $I_0$。

:::herleitung 分配与增益
两个发射极电位相同，所以 $U_\mathrm{BE2}-U_\mathrm{BE1}=U_\mathrm{D}$。由 $I_\mathrm{C}=I_\mathrm{S}\,\mathrm{e}^{U_\mathrm{BE}/U_T}$ 得 $I_\mathrm{C2}/I_\mathrm{C1}=\mathrm{e}^{U_\mathrm{D}/U_T}$。与 $I_\mathrm{C1}+I_\mathrm{C2}=I_0$ 联立即得 [(2.1)](#gl-2-1)。对小变化：总和固定，所以 $\Delta I_\mathrm{C1}=-\Delta I_\mathrm{C2}$。两者都等于 $S$ 乘以各自 $U_\mathrm{BE}$ 的变化，因此这两个变化大小相等、方向相反。它们的差是 $U_\mathrm{D}$，所以每个结承担 $\pm U_\mathrm{D}/2$。于是 $\Delta I_\mathrm{C2}=S\,U_\mathrm{D}/2$，$U_\mathrm{A}=2R_\mathrm{C}\,\Delta I_\mathrm{C2}=S\,R_\mathrm{C}\,U_\mathrm{D}$。
:::

::::beispiel
静态时每条支路流过 1 mA，集电极位于 $12\,\mathrm{V}-3\,\mathrm{V}=9$ V。$S=38.5$ mS，所以 $A_\mathrm{D}=3\,\mathrm{V}/26\,\mathrm{mV}=115$。当 $U_\mathrm{D}=1$ mV 时，两条支路之间转移 $\pm19.2$ µ A，每个集电极移动 57.7 mV，合计 $U_\mathrm{A}=115$ mV。两个输入端上 100 mV 的干扰对此毫无影响。
::::

⁠**极限情况：**$U_\mathrm{D}=0$ 时每条支路为 $I_0/2$。当 $|U_\mathrm{D}|\gg U_T$ 时，全部电流流过一个晶体管，$U_\mathrm{A}\to\pm R_\mathrm{C}I_0=\pm6$ V。线性范围只有几个 $U_T$ 宽：在 26 mV 处，直线给出 3.0 V，精确曲线给出 2.77 V。

**输入。** 输入信号 $U_\mathrm{D}$ 加在两个串联的 BE 结上，输入电阻为 $2\,r_\mathrm{BE}=2B/S=10.4$ k$\Omega$。总电流为 20 µ A 而不是 2 mA 时，输入电阻为 1.04 M$\Omega$，每个基极只取 50 nA。参考模型中的 $r_\mathrm{e}$ 和 $I_\mathrm{B}$ 就来源于此。

**从差分放大器到运放。** $A_\mathrm{D}=U_{R_\mathrm{C}}/U_T$ 停留在几百，因为 $U_{R_\mathrm{C}}$ 不可能超过电源电压。用电流镜（[第 10 章](/wissen/zh/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/der-bipolartransistor/der-bipolartransistor.html)）代替电阻，可把两个电流变化引到同一侧，在那里它的作用相当于两个 $r_\mathrm{CE}$ 并联。这样得到 $S\,r_\mathrm{CE}/2=U_\mathrm{Early}/(2U_T)\approx1400$。后面再接一个电压放大级和一个射极跟随器，以获得低输出电阻。总共达到 $10^5$ 到 $10^6$。这个值取决于 $B$、$U_\mathrm{Early}$ 和温度：很大，但不精确。

:::frage 只抬高一个基极时，为什么每个晶体管上只有一半的差值？
因为节点 E 随之升高了一半。T2 想要更多电流，但总和固定，于是 E 升高，直到 T1 恰好让出这么多。固定的总和要求两个 $U_\mathrm{BE}$ 的变化大小相等、方向相反。谁把全部差值都放在一个结上，得到的就是真实 $A_\mathrm{D}$ 的两倍。
:::

:::ltspice 电流分配
⁠**绘制：**两个 `npn` Q1、Q2，模型 `T`。集电极各经一个 `res` 3k 接 `voltage` 12，节点 `a1`、`a2`。两个发射极接节点 `e`，从那里经 `current` 2m 接到一个 `voltage` $-12$。Q1 的基极接地，Q2 的基极接 `voltage` `VP`。

⁠**指令：**`.model T NPN(IS=1.55e-13 BF=186 VAF=74)`，`.dc VP -0.2 0.2 0.1m`，`.meas dc u1 FIND V(a1)-V(a2) AT=-0.5m`，`.meas dc u2 FIND V(a1)-V(a2) AT=0.5m`，`.meas dc ad PARAM (u2-u1)/1m`。

⁠**你会看到：**`Ic(Q1)` 和 `Ic(Q2)` 在 0 处相交，在 100 mV 时 Q2 承载 97.8 % 的电流。`ad` 为 111.4，计算值为 115，因为 LTspice 用 $U_T=25.85$ mV 计算，并计入了 $r_\mathrm{CE}$。请代入练习 [2](#aufg-2) 的数值。
:::

:::aufgabe 练习 2 ★★ 差分级
<span class="anker" id="aufg-2"></span>

一个由晶体管 T 构成的差分级工作在 $I_0=1$ mA、$R_\mathrm{C}=5$ k$\Omega$、$U_\mathrm{CC}=12$ V。(a) 求 $S$、$A_\mathrm{D}$ 和集电极的静态电位。(b) $U_\mathrm{D}=2$ mV 时 $U_\mathrm{A}$ 多大？转移了多少电流？(c) 两个输入端都升高 1 V。E、各电流和 $U_\mathrm{A}$ 会怎样？(d) 预测：若 $I_0$ 加倍、$R_\mathrm{C}$ 减半，$A_\mathrm{D}$ 会变吗？

:::loesung
(a) $S=0.5\,\mathrm{mA}/26\,\mathrm{mV}=19.2$ mS，$A_\mathrm{D}=96.2$，集电极位于 $12\,\mathrm{V}-2.5\,\mathrm{V}=9.5$ V。 (b) $U_\mathrm{A}=192$ mV。转移 $S\,U_\mathrm{D}/2=19.2$ µ A。 (c) E 升高 1 V，$U_\mathrm{BE}$ 和各电流不变，$U_\mathrm{A}=0$。 (d) 不变：$A_\mathrm{D}=U_{R_\mathrm{C}}/U_T$，而 $U_{R_\mathrm{C}}=2.5$ V 保持不变。
:::
:::
