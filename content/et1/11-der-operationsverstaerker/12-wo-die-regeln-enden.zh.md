---
title: 第 10 阶段：规则的终点
pfad: 电气工程 / 第 1 学期 / ET1 – 电气工程基础 1：电路分析导论 / 运算放大器
adresse: elektrotechnik/1-semester/grundlagen-der-elektrotechnik/der-operationsverstarker
knoten: 第 11 章：运算放大器
order: 1211200
summary: 到这里为止，运放除了 A 和极限之外都是理想的。本阶段按大小整理实际偏差，并总结计算步骤。
tags: 失调电压, 输入偏置电流, 共模抑制, 特征频率, 压摆率, 过驱动
lang: zh
---

<span class="anker" id="stufe-10"></span>

:::zweck
到这里为止，运放除了 $A$ 和极限之外都是理想的。本阶段按大小整理实际偏差，并总结计算步骤。
:::

**基本思路。** 实际偏差通过两条途径起作用。一类偏差移动环路所调节到的点：晶体管 T1 和 T2 从不完全相同，所以静止点不是 $U_\mathrm{D}=0$，而是 $U_\mathrm{D}=U_\mathrm{off}$。另一类偏差减小裕量 $A\beta$。首先是频率：为了使环路不振荡，内部电容限制了带宽。电容上的电压跟不上快速信号，$A$ 下降。

| 量 | 原因 | 在参考模型中的影响 |
|---|---|---|
| $A$ 有限，$10^5$ 到 $10^6$ | 各级增益有限 | 偏差 $1/(A\beta)=0.005$ % |
| __失调电压__ $U_\mathrm{off}$ | 输入晶体管不相同，随温度、电源、老化而变 | 输出端 $U_\mathrm{off}/\beta=5$ mV，$U_\mathrm{E}=0$ 时也有 |
| __输入偏置电流__ $I_\mathrm{B}$ | T1 和 T2 的基极电流 | 流过 $R_2$：$I_\mathrm{B}R_2=2$ mV |
| 共模 | 实际电流源 T3，支路不相同 | 见下文 |
| $A(f)$ | 内部电容 | $\vert A(f)\vert \approx f_\mathrm{T}/f$，见下文 |
| 输出 | 输出级晶体管 | $\pm11$ V，20 mA，$r_\mathrm{a}/(1+A\beta)=3.75$ m$\Omega$ |
| 噪声 | 自身的晶体管 | 10 nV/$\sqrt{\text{Hz}}$：20 kHz 内 1.41 µ V |

失调是使输出为零的输入电压。在环路中建立起 $\varphi_+-\varphi_-=U_\mathrm{off}$，分压器又把它放大 $1/\beta$ 倍。运放自身的噪声与第 [1](rauschen.html#stufe-1) 阶段的传感器按平方相加：2.31 µ V 而不是 1.82 µ V，SNR 下降 2.1 dB，降到 52.7 dB。

:::definition 定义 10.1 (共模抑制)
<span class="anker" id="satz-10-1"></span>

__共模抑制__ CMRR（common mode rejection ratio）比较差值的增益与共模的增益：

<span class="anker" id="gl-10-1"></span>
$$\mathrm{CMRR}=\frac{A}{A_\mathrm{cm}},\qquad \mathrm{CMRR}_\mathrm{dB}=20\lg\frac{A}{A_\mathrm{cm}}. \tag{10.1}$$

理想情况下 $\mathrm{CMRR}\to\infty$，常见值为 60 dB（$A_\mathrm{cm}/A=10^{-3}$）到 120 dB（$10^{-6}$）。
:::

⁠**如何理解：**机理：实际的 T3 有有限的 $r_\mathrm{CE}$。共模上升时，E 上升，总电流增加 $U_\mathrm{cm}/r_\mathrm{CE}$。对第 [2](der-differenzverstarker.html#stufe-2) 阶段的差分级，取 $r_\mathrm{CE}=40$ k$\Omega$，每个集电极随共模变化的系数为 $R_\mathrm{C}/(2r_\mathrm{CE})=0.0375$，而对差值为 57.7：63.7 dB。参考模型中为 90 dB，即 $A_\mathrm{cm}=3.16$。在第 [6](mehrere-eingange-mehrere-stufen.html#stufe-6) 阶段的减法器上，2 V 共模相当于 $2\,\mathrm{V}/31600=63$ µ V 的差值，在输出端为 0.32 mV，占测得的 0.2 V 的 0.16 %。

**频率。** 在 $f_A=f_\mathrm{T}/A=10$ Hz 以上，$A$ 每十倍频程下降 10 倍，$|A(f)|\approx f_\mathrm{T}/f$。在__特征频率__ $f_\mathrm{T}$ 处，$|A|=1$。只要 $|A(f)|\,\beta\gg1$，环路就起作用。在 $f_G=\beta\,f_\mathrm{T}$ 处裕量耗尽：

<span class="anker" id="gl-10-2"></span>
$$|G(f)|=\frac{1/\beta}{\sqrt{1+(f/f_G)^2}},\qquad f_G=\beta\,f_\mathrm{T},\qquad G\,f_G=f_\mathrm{T}. \tag{10.2}$$

⁠**如何理解：**$G=5$ 时带宽达到 200 kHz。增益与带宽之积是固定的：$G=1$ 时为 1 MHz，$G=100$ 时只有 10 kHz。第 [4](gegenkopplung.html#stufe-4) 阶段的时间常数 $\tau_G=0.80$ µ s 是同一个值：$1/(2\pi\cdot200\,\mathrm{kHz})$。**极限情况：**当 $f\gg f_G$ 时，$|G|\to|A|$，反馈不再起作用。

:::abbildung et1/k11bode 12
开环增益和电路增益随频率的变化，两轴都是对数坐标。两条曲线之间的距离就是裕量 $|A|\beta$。它在 1 kHz 时仍为 200，在 200 kHz 时耗尽。
:::

:::ltspice 带宽与锁定
⁠**绘制：**符号 `UniversalOpAmp2`（文件夹 OpAmps），参数 `Avol=100k GBW=1Meg Slew=0.5Meg`、`Ilimit=20m Rail=1`，电源 `voltage` $\pm12$。外部电路与第 [4](gegenkopplung.html#stufe-4) 阶段的方框相同，`VE` 设 `AC 1`。

⁠**指令：**`.ac dec 50 1 10Meg`，`.meas ac g0 FIND mag(V(a)) AT=10`，`.meas ac fg WHEN mag(V(a))=g0/sqrt(2)`。

⁠**你会看到：**`fg` = 199 kHz，计算值为 200 kHz。然后交换输入端，把 `VE` 设为 `PULSE(-3 3 1m 1u 1u 1m 2m)`，运行 `.tran 4m`：`V(a)` 在 $\pm10.98$ V 之间跳变。用 $\pm1$ V 代替 $\pm3$ V 时，输出保持不动，这就是第 [9](mitkopplung-und-der-schmitt-trigger.html#stufe-9) 阶段的迟滞。做练习 [11](#aufg-11) 时把 `R1` 设为 1k，`R2` 设为 100k。
:::

:::zusatz 压摆率
内部充电电流是有限的。因此输出有一个最高速度，即__压摆率__，典型值 0.5 V/µ s。图 [5](gegenkopplung.html#abb-5) 中的阶跃实际上因此需要约 10 µ s，而不是几 µ s。幅值 11 V 的正弦波只有在约 7.2 kHz 以下才不失真，尽管带宽要大得多。
:::

:::merke 计算流程
<ol>

<li>

⁠**无反馈**（比较器）：$U_\mathrm{A}=U_\mathrm{A,max}$ 或 $U_\mathrm{A,min}$，$U_\mathrm{D}\ne0$。

</li>

<li>

⁠**检查符号：**设想把输出抬高。若 $U_\mathrm{D}$ 下降，就是负反馈；若上升，就是正反馈。

</li>

<li>

⁠**负反馈：**假定 $U_\mathrm{D}=0$，用节点定律和欧姆定律算出 $U_\mathrm{A}$。若它在极限之内，计算有效。否则运放__过驱动__：$U_\mathrm{A}$ 位于极限，$U_\mathrm{D}\ne0$，用这个固定的 $U_\mathrm{A}$ 计算网络。

</li>

<li>

⁠**正反馈：**通常 $U_\mathrm{A}$ 位于极限，$U_\mathrm{D}\ne0$。阈值由 $U_\mathrm{D}$ 的符号变化得出。

</li>

<li>

⁠**精度：**信号频率下的 $1/(A\beta)$，输出端的 $U_\mathrm{off}/\beta$ 和 $I_\mathrm{B}R_2$。

</li>

</ol>
:::

:::aufgabe 练习 11 ★★★ 测量放大器
<span class="anker" id="aufg-11"></span>

用 V 把 10 mV 的传感器信号放大到约 1 V：$R_1=1$ k$\Omega$，$R_2=100$ k$\Omega$，同相。(a) $\beta$、$G$ 和由 $A$ 引起的偏差是多少？(b) 电路能工作到多高的频率？5 kHz 时 $|G|$ 多大？(c) 输出端的失调多大？它占信号的多少？$I_\mathrm{B}$ 又增加多少？(d) 输入到多大时输出还够用？(e) 一个 $R\,C=10$ ms 的积分器有同样的失调。$U_\mathrm{E}=0$ 时其输出变化多快？何时到达极限？

:::loesung
(a) $\beta=1/101$，$G\approx101$，偏差 $101/A=0.10$ %。 (b) $f_G=1\,\mathrm{MHz}/101=9.9$ kHz。$|G(5\,\mathrm{kHz})|=101/\sqrt{1+(5/9.9)^2}=90.2$。这样的电路在 5 kHz 时就损失十分之一。 (c) $101\cdot1\,\mathrm{mV}=101$ mV，即 1.01 V 信号的 10 %。另加 $I_\mathrm{B}R_2=5$ mV。 (d) $11\,\mathrm{V}/101=109$ mV。 (e) $1\,\mathrm{mV}/10\,\mathrm{ms}=0.1$ V/s，110 s 后到达极限。因此实际的积分器需要一个复位开关，或在 $C$ 上并联一个大电阻。
:::
:::
