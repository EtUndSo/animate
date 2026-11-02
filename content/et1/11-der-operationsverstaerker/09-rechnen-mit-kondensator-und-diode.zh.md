---
title: 第 7 阶段：用电容器和二极管做运算
pfad: 电气工程 / 第 1 学期 / 电气工程基础 / 运算放大器
order: 1210900
summary: 到目前为止，一个电阻把电压变成电流，另一个电阻把电流变成电压。本阶段换用其他元件，规则不变。运放的名字就由此而来：它执行运算。
tags: 
lang: zh
---

<span class="anker" id="stufe-7"></span>

:::zweck
到目前为止，一个电阻把电压变成电流，另一个电阻把电流变成电压。本阶段换用其他元件，规则不变。运放的名字就由此而来：它执行运算。
:::

**基本思路。** 正输入端接地时，负输入端的节点定律表明：输入元件的电流全部流过反馈元件，$I_\mathrm{in}=-I_\mathrm{fb}$。输入元件看到 $U_\mathrm{E}$ 并提供一个电流。反馈元件看到 $U_\mathrm{A}$，必须通过同一电流。产生什么函数，完全由它们的电流-电压规律决定（图 [9](#abb-9)）。

:::satz 定理 7.1 (运算)
<span class="anker" id="satz-7-1"></span>

正输入端接地、运放理想时，有

<span class="anker" id="gl-7-1"></span>
<span class="anker" id="gl-7-2"></span>
<span class="anker" id="gl-7-3"></span>
<span class="anker" id="gl-7-4"></span>
$$\begin{aligned} \text{积分器：}&u_\mathrm{A}(t)=u_\mathrm{A}(0)-\frac{1}{R\,C}\int_0^t u_\mathrm{E}(t')\,\mathrm{d} t', \\ \text{微分器：}&u_\mathrm{A}(t)=-R\,C\,\frac{\mathrm{d} u_\mathrm{E}}{\mathrm{d} t}, \\ \text{对数放大器：}&U_\mathrm{A}=-U_T\,\ln\frac{U_\mathrm{E}}{R\,I_\mathrm{S}}, \\ \text{指数放大器：}&U_\mathrm{A}=-R\,I_\mathrm{S}\,\mathrm{e}^{U_\mathrm{E}/U_T}. \end{aligned} \tag{7.1|7.2|7.3|7.4}$$
:::

⁠**如何理解：**$R\,C$ 是以 s 为单位的时间常数，$I_\mathrm{S}$ 是二极管的反向饱和电流，$U_T=26$ mV。**适用条件：**[(7.3)](#gl-7-3) 要求 $U_\mathrm{E}>0$ 且 $U_\mathrm{E}/R\gg I_\mathrm{S}$，[(7.4)](#gl-7-4) 要求 $U_\mathrm{E}\gg U_T$，并且都要求输出在其极限之内。

:::herleitung 四个节点定律
积分器：流过 $R$ 的电流为 $i=u_\mathrm{E}/R$。它给电容器充电，$C\,\mathrm{d} u_C/\mathrm{d} t=i$。左极板固定在 0，所以 $u_\mathrm{A}=-u_C$。微分器：输入端电容器中的电流 $i=C\,\mathrm{d} u_\mathrm{E}/\mathrm{d} t$，$u_\mathrm{A}=-R\,i$。对数放大器：$I=U_\mathrm{E}/R$ 流过二极管，所以 $I=I_\mathrm{S}\,\mathrm{e}^{U_\mathrm{F}/U_T}$，二极管电压 $U_\mathrm{F}=-U_\mathrm{A}$。解出即得 [(7.3)](#gl-7-3)。指数放大器：$U_\mathrm{E}$ 加在二极管上，其电流 $I_\mathrm{S}\,\mathrm{e}^{U_\mathrm{E}/U_T}$ 流过 $R$。
:::

:::abbildung et1/k11bauteile 9
四个电路，一条规则：左边的元件把输入电压变成电流，上边的元件为此要求一个输出电压。各节点都处于虚地。
:::

**例。** ⁠**积分器**，$R=10$ k$\Omega$，$C=10$ nF，即 $R\,C=100$ µ s。当 $U_\mathrm{E}=1$ V 时，流过固定电流 100 µ A。与[第 3 部分](/wissen/zh/elektrotechnik/1-semester/grundlagen-der-elektrotechnik/der-kondensator/der-kondensator.html)的 RC 电路不同，它在充电时不减小，因为 $R$ 上的电压保持 1 V。$u_\mathrm{A}$ 以 10 V/ms 匀速下降，1.1 ms 后达到 $-11$ V。1 kHz、$\pm1$ V 的方波变成 $\pm2.5$ V 的三角波。**微分器**，$R\,C$ 相同：1 kHz、$\pm1$ V 的三角波以 4 V/ms 上升，$u_\mathrm{A}$ 变成 $\pm0.4$ V 的方波。对正弦波，其幅值随频率增大，$\hat u_\mathrm{A}/\hat u_\mathrm{E}=2\pi f\,R\,C$：1 kHz 时为 0.63，100 kHz 时为 62.8。因此它对高频噪声（第 [1](rauschen.html#stufe-1) 阶段）的放大特别强。**对数放大器**，$R=10$ k$\Omega$，$I_\mathrm{S}=1.9\cdot10^{-13}$ A：0.1 V、1 V、10 V 得到 $-0.462$ V、$-0.522$ V、$-0.582$ V。每个十倍程（因子 10）增加 $U_T\ln10=59.9$ mV。**指数放大器**，数值相同：0.5 V 得到 $-0.427$ V，每增加 18 mV，幅值加倍。

⁠**极限情况：**$u_\mathrm{E}=0$ 时积分器保持不动，维持 $u_\mathrm{A}(0)$。当 $U_\mathrm{E}<0$ 时，对数放大器的二极管截止，反馈中断，输出运行到极限：规则只在回路导通时成立。

**做乘法。** 由于 $\ln x+\ln y=\ln(x\,y)$，一条级联可以用模拟方式做乘法：两个对数放大器、一个加法器、一个指数放大器。输出端除一个固定系数外就是乘积 $U_x\,U_y$。由于 $U_T$ 和 $I_\mathrm{S}$ 随温度变化，实际中用晶体管代替二极管，并附加温度补偿。在数字计算机出现之前，这样的电路构成了计算机器，运算放大器的名字正来源于此。

:::aufgabe 练习 7 ★★ 积分器
<span class="anker" id="aufg-7"></span>

$R=100$ k$\Omega$，$C=10$ nF，$u_\mathrm{A}(0)=0$。(a) $R\,C$ 是多少？$U_\mathrm{E}=-0.2$ V 时，10 ms 后 $u_\mathrm{A}$ 位于何处？(b) 输出何时到达极限？(c) 加上 100 Hz、$\pm0.5$ V 的方波。三角波的幅值是多少？20 Hz 时会怎样？

:::loesung
(a) $R\,C=1$ ms。$u_\mathrm{A}$ 以 200 V/s 上升，10 ms 后到 $+2$ V。 (b) $11\,\mathrm{V}/(200\,\mathrm{V/s})=55$ ms 后。 (c) 5 ms 的半周期使 $u_\mathrm{A}$ 变化 2.5 V，幅值为 1.25 V。20 Hz 时摆幅为 12.5 V。当 $u_\mathrm{A}(0)=0$ 且以正半周开始时，三角波达到 $-11$ V 并到达极限。
:::
:::

:::aufgabe 练习 8 ★★ 对数放大器
<span class="anker" id="aufg-8"></span>

$R=1$ k$\Omega$，$I_\mathrm{S}=1.9\cdot10^{-13}$ A。(a) 计算 1 V 和 2 V 时的 $U_\mathrm{A}$。不用 $I_\mathrm{S}$ 预测两者之差。(b) $U_\mathrm{E}$ 从 10 mV 变到 10 V 时，$U_\mathrm{A}$ 扫过多大范围？(c) 在 330 K 而不是 300 K 时，$U_T=28.6$ mV。电流为 100 µ A 时，仅此一项使 $U_\mathrm{A}$ 偏移多少？

:::loesung
(a) 1 mA 得 $-0.582$ V，2 mA 得 $-0.600$ V。两者之差为 $U_T\ln2=18$ mV，不含 $I_\mathrm{S}$。 (b) 三个十倍程：$3\cdot59.9\,\mathrm{mV}=180$ mV。 (c) $U_\mathrm{F}$ 从 0.522 V 增加到 0.574 V，即增加 52 mV。实际上 $I_\mathrm{S}$ 也大幅上升，因此需要温度补偿。
:::
:::
