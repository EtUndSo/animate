---
title: 第 10 阶段：三种基本电路
pfad: 电气工程 / 第 1 学期 / 电气工程基础 / 双极型晶体管
order: 1201200
summary: 输入和输出各需要两个接线端，而晶体管总共只有三个。所以有一个接线端对信号来说是公共的。本阶段算出这三种可能。
tags: 共发射极电路, 共集电极电路, 射极跟随器, 共基极电路, 电压摆幅, 缓冲器
lang: zh
---

<span class="anker" id="stufe-10"></span>

:::zweck
输入和输出各需要两个接线端，而晶体管总共只有三个。所以有一个接线端对信号来说是公共的。本阶段算出这三种可能。
:::

**基本思路。** 公共接线端决定电路的名称（图 [12](#abb-12)）。在__共发射极电路__中，信号从基极输入，从集电极输出。$u_\mathrm{in}$ 全部加在 BE 通路上，产生 $i_\mathrm{c}=S\,u_\mathrm{in}$。这个电流流过 $R_\mathrm{C}$，把集电极电位拉低：输出是反相的。在__共集电极电路__中，信号从基极输入，从发射极输出。发射极跟随基极：如果发射极不动，$U_\mathrm{BE}$ 就会改变，由此产生的电流会立即经 $R_\mathrm{E}$ 把它抬起来。因此它也称为__射极跟随器__。在__共基极电路__中，基极固定，信号从发射极输入。发射极下降时，$U_\mathrm{BE}$ 上升，更大的电流把集电极拉低：输入和输出同向变化。其幅值与共发射极电路相同。

:::abbildung et1/k10grundschaltungen 12
上：三种基本电路。下：它们在参考模型中的特性曲线，$U_\mathrm{CC}=12$ V。共发射极（$R_\mathrm{C}=3$ k$\Omega$）：下降，在 0.6 V 附近很陡。共集电极（$R_\mathrm{E}=3$ k$\Omega$）：输出比输入低约 0.6 V（灰色）。共基极：相当于共发射极关于纵轴的镜像，上升。
:::

:::satz 定理 10.1 (基本电路的电压增益)
<span class="anker" id="satz-10-1"></span>

对放大区中的小信号，忽略 $r_\mathrm{CE}$，$A=u_\mathrm{out}/u_\mathrm{in}$：

<span class="anker" id="gl-10-1"></span>
$$A_\text{共发射极}=-S\,R_\mathrm{C}=-\frac{U_{R_\mathrm{C}}}{U_T},\qquad A_\text{共集电极}=\frac{S\,R_\mathrm{E}}{1+S\,R_\mathrm{E}}<1,\qquad A_\text{共基极}=+S\,R_\mathrm{C}. \tag{10.1}$$

带发射极电阻时，$A=-R_\mathrm{C}/(R_\mathrm{E}+1/S)\approx-R_\mathrm{C}/R_\mathrm{E}$；考虑 $r_\mathrm{CE}$ 时，$A_\text{共发射极}=-S\,(R_\mathrm{C}\parallel r_\mathrm{CE})$。
:::

⁠**如何理解：**$U_{R_\mathrm{C}}=I_\mathrm{C}R_\mathrm{C}$ 是集电极电阻上的直流电压，在参考模型中为 6 V。**简而言之：**共发射极电路的增益等于集电极电阻上的直流电压除以 $U_T$。其中既没有 $B$，也没有晶体管类型。**适用条件：**$|u_\mathrm{be}|\ll U_T$，$R_\mathrm{C}\ll r_\mathrm{CE}$，由内阻小的电源驱动。

:::herleitung 小信号下的三个网孔
对信号来说，$U_\mathrm{CC}$ 相当于地。共发射极：$u_\mathrm{be}=u_\mathrm{in}$，$u_\mathrm{out}=-R_\mathrm{C}i_\mathrm{c}=-R_\mathrm{C}S\,u_\mathrm{in}$，再由 $S=I_\mathrm{C}/U_T$ 得 $S\,R_\mathrm{C}=I_\mathrm{C}R_\mathrm{C}/U_T$。带发射极电阻：$u_\mathrm{in}=u_\mathrm{be}+R_\mathrm{E}S\,u_\mathrm{be}$，$u_\mathrm{in}$ 的大部分加在 $R_\mathrm{E}$ 上，其余部分 $u_\mathrm{be}=u_\mathrm{in}/(1+S\,R_\mathrm{E})$ 起控制作用。共集电极：$u_\mathrm{out}=R_\mathrm{E}S\,u_\mathrm{be}$，$u_\mathrm{be}=u_\mathrm{in}-u_\mathrm{out}$，解方程即可。共基极：基极不动，所以 $u_\mathrm{be}=-u_\mathrm{in}$，$u_\mathrm{out}=-R_\mathrm{C}S\,u_\mathrm{be}=+S\,R_\mathrm{C}u_\mathrm{in}$。
:::

**例。** 共发射极电路在点 A：$A=-6\,\mathrm{V}/26\,\mathrm{mV}=-231$，考虑 $r_\mathrm{CE}$ 后更准确的值是 $-215$。输入 1 mV 变成输出 0.23 V。中点允许的__电压摆幅__（输出幅值）接近 6 V，但输入为 25 mV 时切线早已失效。对于 2.6 mV 的小信号极限，输出为 0.6 V。放大器的工作点必须位于斜率近似恒定的区域，摆幅还应尽可能大。负反馈版本的 $A=-3\,\text{k}\Omega/(1\,\text{k}\Omega+12.9\,\Omega)=-2.96$：只有 1.3 % 的 $u_\mathrm{in}$ 加在 BE 通路上，但增益几乎只由两个电阻决定。$R_\mathrm{E}=3$ k$\Omega$、2 mA 的射极跟随器：$S\,R_\mathrm{E}=231$，$A=0.996$。它的优势不在电压，而在电流：电流增益为 $1+B=201$。它用作__缓冲器__：几乎不给电源增加负担，并以低阻抗驱动负载。**极限情况：**负反馈形式中 $R_\mathrm{E}\to0$ 给出 $-S\,R_\mathrm{C}$。射极跟随器中 $R_\mathrm{E}\to\infty$ 给出 $A\to1$。

| 电路 | $A$ | 输入电阻 | 输出电阻 | 用途 |
|---|---|---|---|---|
| 共发射极 | $-231$ | $r_\mathrm{BE}=2.6$ k$\Omega$ | $R_\mathrm{C}=3$ k$\Omega$ | 放大电压 |
| 共集电极 | $0.996$ | $r_\mathrm{BE}+(1+B)R_\mathrm{E}=606$ k$\Omega$ | $1/S=13\,\Omega$ | 缓冲，电流放大 |
| 共基极 | $+231$ | $1/S=13\,\Omega$ | $R_\mathrm{C}=3$ k$\Omega$ | 放大低阻抗信号源 |

:::frage 实际的共发射极电路的特性曲线不是比共基极电路平缓吗？为什么说幅值相同？
在直接驱动、$R_\mathrm{C}$ 相同且电流相同时，幅值才相同。如果基极前有串联电阻或带内阻的电源，它就与 $r_\mathrm{BE}$ 构成分压器，只有一部分 $u_\mathrm{in}$ 到达 BE 通路。这时共发射极电路的特性曲线就较平缓。在共基极电路中不存在这个分压器，因为低阻抗信号源接在发射极上。
:::

:::ltspice 共发射极电路的传输特性曲线
⁠**绘制：**`voltage` `VCC` 取 12，接 `res` 3k 到集电极（网络 `c`），`npn` 取模型 `T`，发射极接地，基极接 `voltage` `VE`。

⁠**指令：**第 [3](eine-flache-viele-kennlinien.html#stufe-3) 阶段的模型，`.dc VE 0.5 0.7 0.1m`，`.meas dc a1 FIND V(c) AT=0.5995`，`.meas dc a2 FIND V(c) AT=0.6005`，`.meas dc au PARAM (a2-a1)/1m`。

⁠**你会看到：**$U_\mathrm{out}$ 在约 60 mV 的窗口内从 12 V 降到接近 0。`au` 给出 $-213$，计算值为 $-215$。LTspice 按 $U_T=25.86$ mV 计算，在 $U_\mathrm{BE}=0.6$ V 时为 1.98 mA。做练习 [12](#aufg-12) 时，把 `VCC` 设为 9，电阻设为 4.7k，`AT` 值设为 0.582 和 0.583：`au` 在 0.98 mA 时给出 $-169$。
:::

:::aufgabe 练习 12 ★★★ 放大器和跟随器
<span class="anker" id="aufg-12"></span>

T 工作在 $I_\mathrm{C}=1$ mA，$U_\mathrm{CE}=4.3$ V，$U_\mathrm{CC}=9$ V，$R_\mathrm{C}=4.7$ k$\Omega$。 (a) 只根据 $R_\mathrm{C}$ 上的电压，预测共发射极电路的 $A$ 有多大。(b) 当 $\hat u_\mathrm{in}=2$ mV 时，输出幅值是多少？$r_\mathrm{CE}$ 如何改变结果？(c) 接 470 $\Omega$ 的发射极电阻：$A$ 是多少？(d) 接成 $R_\mathrm{E}=4.7$ k$\Omega$ 的射极跟随器：$A$ 是多少？输出反相吗？

:::loesung
(a) $U_{R_\mathrm{C}}=4.7$ V，所以 $A=-4.7\,\mathrm{V}/26\,\mathrm{mV}=-181$。

(b) $\hat u_\mathrm{out}=0.36$ V。考虑 $r_\mathrm{CE}=78$ k$\Omega$ 后，$A=-S(R_\mathrm{C}\parallel r_\mathrm{CE})=-171$，只小 6 %。

(c) $A=-4.7\,\text{k}\Omega/(470\,\Omega+26\,\Omega)=-9.5$。近似式 $-R_\mathrm{C}/R_\mathrm{E}$ 给出 $-10$。

(d) $S\,R_\mathrm{E}=181$，$A=0.994$。输出不反相，发射极与基极同相跟随。
:::
:::
